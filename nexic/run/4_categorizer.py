"""
Animal Taxonomy Classifier
===========================
Takes a Bradley-Terry ratings CSV and classifies each animal into:
  1. "non-mesozoic"  — extant animals, mammals, synapsids, post-Mesozoic taxa
  2. "dinosaur"      — explicit Mesozoic dinosaurs (Dinosauria clade)
  3. "mesozoic-other" — Mesozoic non-dinosaurs (pterosaurs, marine reptiles, etc.)

Uses Wikipedia API for taxonomy lookups. Run locally (needs internet access).

Usage:
    python classify_animals.py ratings.csv
    # produces: ratings_classified.csv
"""

import csv
import json
import re
import sys
import time
import urllib.request
import urllib.parse
import urllib.error
from pathlib import Path


# ---------------------------------------------------------------------------
# Name corrections for U+FFFD encoding corruption
# ---------------------------------------------------------------------------
# The source CSV had certain accented characters corrupted to U+FFFD, which the
# Bradley-Terry script's normalization turned into deletions or spaces.
# These substring replacements repair the correct spellings in the output.
NAME_CORRECTIONS = {
    "Alano Espa ol":         "Alano Español",
    "Alano Espaol":          "Alano Español",
    "Baird s Beaked Whale":  "Baird's Beaked Whale",
    "Bairds Beaked Whale":   "Baird's Beaked Whale",
    "Cimarr n Uruguayo":     "Cimarrón Uruguayo",
    "Cimarrn Uruguayo":      "Cimarrón Uruguayo",
    "Galap gos Islands":     "Galápagos Islands",
    "Galapgos Islands":      "Galápagos Islands",
    "Lettered Ara ari":      "Lettered Araçari",
    "Lettered Araari":       "Lettered Araçari",
    "Molina s Hog-nosed":    "Molina's Hog-nosed",
    "Molinas Hog-nosed":     "Molina's Hog-nosed",
    "Morelet s Crocodile":   "Morelet's Crocodile",
    "Morelets Crocodile":    "Morelet's Crocodile",
    "R ppell's Griffon":     "Rüppell's Griffon",
    "Rppell's Griffon":      "Rüppell's Griffon",
    "arplaninac":            "Šarplaninac",
    "Zalmoxes shqiperorum":  "Zalmoxes shqiperorum",
}


def correct_name(name):
    """Repair known U+FFFD-corrupted names using the corrections table."""
    for mangled, correct in NAME_CORRECTIONS.items():
        if mangled in name:
            name = name.replace(mangled, correct)
    return name


# ---------------------------------------------------------------------------
# Known classification lists (saves API calls for common/tricky cases)
# ---------------------------------------------------------------------------

# Clades that are Mesozoic dinosaurs (including birds-as-dinosaurs only if extinct)
DINOSAUR_CLADES = {
    "dinosauria", "theropoda", "sauropoda", "ornithischia", "saurischia",
    "ceratopsia", "thyreophora", "ornithopoda", "marginocephalia",
    "pachycephalosauria", "ankylosauria", "stegosauria",
    "dromaeosauridae", "troodontidae", "tyrannosauridae",
    "abelisauridae", "carcharodontosauridae", "spinosauridae",
    "allosauridae", "megalosauridae", "coelophysidae",
    "oviraptoridae", "therizinosauridae", "compsognathidae",
    "ceratopsidae", "hadrosauridae", "iguanodontidae",
    "titanosauria", "diplodocidae", "brachiosauridae",
}

# Mesozoic non-dinosaurs
MESOZOIC_OTHER_CLADES = {
    "pterosauria", "plesiosauria", "plesiosauridae", "elasmosauridae",
    "ichthyosauria", "mosasauridae", "nothosauria",
    "rhynchosauria", "phytosauria", "aetosauria",
    "rauisuchidae", "rauisuchia", "poposauroidea",
    "protorosauria", "tanystropheidae", "choristodera",
}

# Explicit overrides for tricky names the API might misidentify
MANUAL_OVERRIDES = {
    # Modern birds are NOT dinosaurs for this classification
    # (user wants "Mesozoic dinosaur" specifically)
    # Extinct Mesozoic dinosaurs:
    "Tyrannosaurus rex": "dinosaur",
    "Triceratops horridus": "dinosaur",
    "Velociraptor mongoliensis": "dinosaur",
    "Deinonychus antirrhopus": "dinosaur",
    "Utahraptor ostrommaysorum": "dinosaur",
    "Allosaurus fragilis": "dinosaur",
    "Spinosaurus aegyptiacus": "dinosaur",
    "Spinosaurus aegypticus": "dinosaur",
    "Giganotosaurus carolinii": "dinosaur",
    "Compsognathus longipes": "dinosaur",
    "Ankylosaurus magniventris": "dinosaur",
    "Stegosaurus stenops": "dinosaur",
    "Stegosaurus ungulatus": "dinosaur",
    "Diplodocus carnegii": "dinosaur",
    "Apatosaurus ajax": "dinosaur",
    "Brontosaurus excelsus": "dinosaur",
    "Argentinosaurus huinculensis": "dinosaur",
    "Europasaurus holgeri": "dinosaur",
    "Ohmdenosaurus liasicus": "dinosaur",
    # Mesozoic non-dinosaurs:
    "Quetzalcoatlus northropi": "mesozoic-other",   # pterosaur
    "Hatzegopteryx thambema": "mesozoic-other",     # pterosaur
    "Pteranodon longiceps": "mesozoic-other",       # pterosaur
    "Dimorphodon macronyx": "mesozoic-other",       # pterosaur
    "Mosasaurus hoffmannii": "mesozoic-other",      # mosasaur
    "Tylosaurus proriger": "mesozoic-other",        # mosasaur
    "Tylosaurus nepaeolicus": "mesozoic-other",     # mosasaur
    "Prognathodon spp.": "mesozoic-other",          # mosasaur
    "Prognathodon saturator": "mesozoic-other",     # mosasaur
    "Globidens alabamaensis": "mesozoic-other",     # mosasaur
    "Clidastes propython": "mesozoic-other",        # mosasaur
    "Kronosaurus queenslandicus": "mesozoic-other", # pliosaur
    "Pliosaurus funkei": "mesozoic-other",          # pliosaur
    "Pliosaurus spp. (a large one!)": "mesozoic-other",  # pliosaur
    "Pliosaurus spp.": "mesozoic-other",            # pliosaur
    "Liopleurodon ferox": "mesozoic-other",         # pliosaur
    "Rhomaleosaurus spp.": "mesozoic-other",        # pliosaur
    "Megacephalosaurus eulerti": "mesozoic-other",  # pliosaur
    "Sachicasaurus vitae": "mesozoic-other",        # pliosaur
    "Ichthyosaurus somersetensis": "mesozoic-other",  # ichthyosaur
    "Temnodontosaurus platyodon": "mesozoic-other", # ichthyosaur
    "Ophthalmosaurus icenicus": "mesozoic-other",   # ichthyosaur
    "Shastasaurus sikkanniensis": "mesozoic-other", # ichthyosaur
    "Cymbospondylus youngorum": "mesozoic-other",   # ichthyosaur
    "Cymbospondylus buchseri": "mesozoic-other",    # ichthyosaur
    "Thalattoarchon saurophagis": "mesozoic-other", # ichthyosaur
    "Himalayasaurus tibetensis": "mesozoic-other",  # ichthyosaur
    "Shonisaurus popularis": "mesozoic-other",      # ichthyosaur
    "Elasmosaurus platyurus": "mesozoic-other",     # plesiosaur
    "Albertonectes vanderveldei": "mesozoic-other",  # plesiosaur
    "Deinosuchus riograndensis": "mesozoic-other",  # Mesozoic croc
    "Deinosuchus rugosus": "mesozoic-other",        # Mesozoic croc
    "Sarcosuchus imperator": "mesozoic-other",      # Mesozoic croc
    "Smilosuchus gregorii": "mesozoic-other",       # phytosaur
    "Postosuchus kirkpatricki": "mesozoic-other",   # rauisuchian
    "Rauisuchus tiradentes": "mesozoic-other",      # rauisuchian
    "Saurosuchus galilei": "mesozoic-other",        # rauisuchian
    "Fasolasuchus tenax": "mesozoic-other",         # rauisuchian
    "Prestosuchus chiniquensis": "mesozoic-other",  # rauisuchian
    "Batrachotomus kupferzellensis": "mesozoic-other",  # rauisuchian
    "Erythrosuchus africanus": "mesozoic-other",    # archosauriform
    "Proterosuchus spp.": "mesozoic-other",         # archosauriform
    "Kaprosuchus saharicus": "mesozoic-other",      # Mesozoic croc
    "Dakosaurus maximus": "mesozoic-other",         # metriorhynchid
    "Stomatosuchus inermis": "mesozoic-other",      # Mesozoic croc
    "Carbonemys cofrinii": "non-mesozoic",          # Cenozoic turtle
    "Leptosuchus spp.": "mesozoic-other",           # phytosaur
    "Smok wawelski": "mesozoic-other",              # Triassic archosaur
    "Mastodonsaurus spp.": "mesozoic-other",        # Triassic temnospondyl
    # Synapsids / pre-mammalian (Permian-Triassic, not Mesozoic dinosaurs):
    "Dimetrodon grandis": "non-mesozoic",
    "Dimetrodon angelensis": "non-mesozoic",
    "Inostrancevia alexandri": "non-mesozoic",
    "Anteosaurus magnificus": "non-mesozoic",
    "Rubidgea atrox": "non-mesozoic",
    "Estemmenosuchus uralensis": "non-mesozoic",
    "Lystrosaurus maccaigi": "non-mesozoic",
    # Modern/extant birds — not Mesozoic dinosaurs:
    "Ostrich": "non-mesozoic",
    "Southern Cassowary": "non-mesozoic",
    "Harpy Eagle": "non-mesozoic",
    "Golden Eagle": "non-mesozoic",
    # Extinct but post-Mesozoic (terror birds, elephant birds, moas, etc.):
    "Titanis walleri": "non-mesozoic",
    "Kelenken guillermoi": "non-mesozoic",
    "Phorusrhacos longissimus": "non-mesozoic",
    "Brontornis burmeisteri": "non-mesozoic",
    "Gastornis gigantea": "non-mesozoic",
    "Gastornis parisiensis": "non-mesozoic",
    "Vorombe titan": "non-mesozoic",           # elephant bird
    "South Island Giant Moa": "non-mesozoic",  # moa
    "Dromornis stirtoni": "non-mesozoic",       # mihirung/thunder bird
    "Bullockornis planei": "non-mesozoic",      # mihirung
    "Haast's Eagle": "non-mesozoic",            # Pleistocene eagle
    "Giant Teratorn": "non-mesozoic",           # Pleistocene
    "Merriam's Teratorn": "non-mesozoic",       # Pleistocene
    "Andalgalornis steulleti": "non-mesozoic",  # terror bird
    "Patagornis marshi": "non-mesozoic",        # terror bird
    "Cuban Giant Owl": "non-mesozoic",          # Pleistocene
    # Cenozoic crocs:
    "Purussaurus brasiliensis": "non-mesozoic",
    "Quinkana fortirostrum": "non-mesozoic",
    # Saber-toothed cats, prehistoric mammals:
    "Smilodon fatalis": "non-mesozoic",
    "Smilodon populator": "non-mesozoic",
    "Smilodon gracilis": "non-mesozoic",
    # -----------------------------------------------------------------------
    # Bulk overrides for all remaining names not caught by name-based classifier
    # -----------------------------------------------------------------------
    # Extant animals / domestic breeds:
    "African (Common) Puff Adder": "non-mesozoic",
    "African Wild Ass": "non-mesozoic",
    "Alano Espa ol": "non-mesozoic", "Alano Espa ols": "non-mesozoic",
    "Alano Español": "non-mesozoic", "Alano Españols": "non-mesozoic",
    "Alaskan Malamute": "non-mesozoic",
    "Alexandrine Parakeet": "non-mesozoic",
    "American Feral Pig": "non-mesozoic",
    "American Kestrel": "non-mesozoic",
    "American Mammoth Jackstock (Donkey)": "non-mesozoic",
    "American Robin": "non-mesozoic",
    "Amblycheila cylindriformis": "non-mesozoic",  # beetle
    "Anatolian Predatory Bush-cricket": "non-mesozoic",
    "Ankole-Watusi": "non-mesozoic",  # cattle
    "Arapaima (Pirarucu)": "non-mesozoic",
    "Argentine Black and White Tegu": "non-mesozoic",
    "Asian House Shrew": "non-mesozoic",
    "Asiatic Wild Ass (Onager)": "non-mesozoic",
    "Atlantic Goliath Grouper Fish": "non-mesozoic",
    "Atlantic Portuguese Man o' War": "non-mesozoic",
    "Atlantic Sailfish": "non-mesozoic",
    "Atlantic Torpedo": "non-mesozoic",
    "Auckland Tree Weta": "non-mesozoic",
    "Australian Kelpie": "non-mesozoic",
    "Australian Staghound": "non-mesozoic",
    "Baird's Tapir": "non-mesozoic",
    "Bali Tigress": "non-mesozoic",
    "Banded Krait": "non-mesozoic",
    "Banteng": "non-mesozoic",
    "Barbary Stag": "non-mesozoic",
    "Bed Bug": "non-mesozoic",
    "Belgian Blue": "non-mesozoic",  # cattle
    "Bengal Tigress": "non-mesozoic",
    "Beroid Comb Jelly": "non-mesozoic",
    "Bigclaw Snapping Shrimp": "non-mesozoic",
    "Bili Ape": "non-mesozoic",  # chimpanzee
    "Bipalium kewense": "non-mesozoic",  # flatworm
    "Black Drongo": "non-mesozoic",
    "Black Mouth Curs": "non-mesozoic",  # dog
    "Blond Capuchins": "non-mesozoic",
    "Bloodhound": "non-mesozoic",
    "Blue Petrel": "non-mesozoic",
    "Blue Racer": "non-mesozoic",  # snake
    "Blue-eyed Darner": "non-mesozoic",  # dragonfly
    "Bobbit Worm": "non-mesozoic",
    "Boerbel": "non-mesozoic",  # dog
    "Bongo": "non-mesozoic",  # antelope
    "Bonobo": "non-mesozoic",
    "Boomslang": "non-mesozoic",
    "Border Collie": "non-mesozoic",
    "Boxer": "non-mesozoic",
    "Brazilian Dogo": "non-mesozoic",
    "Brazilian Whiteknee Tarantula": "non-mesozoic",
    "Brown Skua": "non-mesozoic",
    "Bucktooth Tetra": "non-mesozoic",
    "Bushpig": "non-mesozoic",
    "Butler's Garter Snake": "non-mesozoic",
    "Cane (Giant) Toad": "non-mesozoic",
    "Cape Bushbuck (Imbabala)": "non-mesozoic",
    "Cape Griffon (Vulture)": "non-mesozoic",
    "Capybara": "non-mesozoic",
    "Chacoan Peccary": "non-mesozoic",
    "Chain Pickerel": "non-mesozoic",
    "Chianina": "non-mesozoic",  # cattle
    "Chinese Goral": "non-mesozoic",
    "Chital": "non-mesozoic",  # deer
    "Cimarr n Uruguayo": "non-mesozoic",  # dog (corrupted Cimarrón)
    "Cimarrón Uruguayo": "non-mesozoic",
    "Cobalt Blue Tarantula": "non-mesozoic",
    "Collared Mangabey": "non-mesozoic",
    "Collared Peccary (Javelina)": "non-mesozoic",
    "Collared Pika": "non-mesozoic",
    "Colombian White-faced Capuchin": "non-mesozoic",
    "Common (Small-spotted) Genet": "non-mesozoic",
    "Common Buzzard": "non-mesozoic",
    "Common Collared Lizard": "non-mesozoic",
    "Common Eider": "non-mesozoic",
    "Common Eland": "non-mesozoic",
    "Common Garter Snake": "non-mesozoic",
    "Common Green Darner": "non-mesozoic",
    "Common Kestrel": "non-mesozoic",
    "Common Kingsnake": "non-mesozoic",
    "Common Quail": "non-mesozoic",
    "Common Tern": "non-mesozoic",
    "Common Warthog": "non-mesozoic",
    "Cubera Snapper": "non-mesozoic",
    "Darwin's (Lesser) Rhea": "non-mesozoic",
    "Desert Warthog": "non-mesozoic",
    "Desmarest's Hutia": "non-mesozoic",
    "Dogo Argentino": "non-mesozoic", "Dogo Argentinos": "non-mesozoic",
    "Domestic Yak": "non-mesozoic",
    "Dragon Headed Katydid": "non-mesozoic",
    "Drill": "non-mesozoic",  # primate
    "Dwyer's Snake": "non-mesozoic",
    "Eastern (Common) Brown Snake": "non-mesozoic",
    "Eastern Barred Bandicoot": "non-mesozoic",
    "Eastern Garter Snake": "non-mesozoic",
    "Eastern Indigo Snake": "non-mesozoic",
    "Eastern Subterranean Termite (Soldier)": "non-mesozoic",
    "Epomis dejeani": "non-mesozoic",  # beetle
    "Etruscan Shrew": "non-mesozoic",
    "Eugryllacris guomashan": "non-mesozoic",  # cricket
    "Eurasian Hoopoe": "non-mesozoic",
    "European Bee-eater": "non-mesozoic",
    "European Conger": "non-mesozoic",
    "European Green Woodpecker": "non-mesozoic",
    "European Hamster": "non-mesozoic",
    "European Honey Buzzard": "non-mesozoic",
    "European Medicinal Leech": "non-mesozoic",
    "European Sturgeon (Beluga)": "non-mesozoic",
    "Fahaka Pufferfish": "non-mesozoic",
    "Fang's Pufferfish": "non-mesozoic",
    "Fila Brasileiro": "non-mesozoic",  # dog
    "Fire Salamander": "non-mesozoic",
    "Flat Needlefish": "non-mesozoic",
    "Galap gos Islands Feral Dog": "non-mesozoic",
    "Galápagos Islands Feral Dog": "non-mesozoic",
    "Galgo Patagonico": "non-mesozoic",  # dog
    "Gaur": "non-mesozoic",
    "Gelada": "non-mesozoic",
    "Gemsbok": "non-mesozoic",
    "German Cockroach": "non-mesozoic",
    "Gila Monster": "non-mesozoic",
    "Gold Tegu": "non-mesozoic",
    "Golden Dorado": "non-mesozoic",
    "Golden Tree (Ornate Flying) Snake": "non-mesozoic",
    "Goliath Frog": "non-mesozoic",
    "Gray Four-eyed Opossum": "non-mesozoic",
    "Great Black-backed Gull": "non-mesozoic",
    "Great Blue Skimmer": "non-mesozoic",
    "Great Danes": "non-mesozoic",
    "Great Grey (Northern) Shrike": "non-mesozoic",
    "Great Skua (Bonxie)": "non-mesozoic",
    "Great Tit": "non-mesozoic",
    "Greater Arid-land Katydid": "non-mesozoic",
    "Greater Kudu": "non-mesozoic",
    "Greater Rhea": "non-mesozoic",
    "Greater Roadrunner": "non-mesozoic",
    "Green Moray (Eel)": "non-mesozoic",
    "Grey Butcherbird": "non-mesozoic",
    "Grey Shrikethrush (mated pair)": "non-mesozoic",
    "Grivet": "non-mesozoic",  # monkey
    "Guanaco": "non-mesozoic",
    "Gull Dong": "non-mesozoic",  # dog
    "Herring Gull": "non-mesozoic",
    "Himalayan Red Panda": "non-mesozoic",
    "Hokkaido Inu": "non-mesozoic",
    "Horrid King Assassin Bug": "non-mesozoic",
    "House Sparrow": "non-mesozoic",
    "Impala": "non-mesozoic",
    "Indian Gaur": "non-mesozoic",
    "Ivory-billed Woodpecker": "non-mesozoic",
    "Jagdterriers": "non-mesozoic",
    "Jagdterriers (pack of3/4)": "non-mesozoic",
    "Kaluga Sturgeon": "non-mesozoic",
    "Kiang": "non-mesozoic",  # wild ass
    "King Brown (Mulga) Snake": "non-mesozoic",
    "Klipspringer": "non-mesozoic",
    "Knight Anole": "non-mesozoic",
    "Komodo Dragon": "non-mesozoic",
    "Kulang Asil": "non-mesozoic",  # chicken breed
    "Lake Darner": "non-mesozoic",
    "Land Mullet": "non-mesozoic",  # skink
    "Lar Gibbon": "non-mesozoic",
    "Largetooth Sawfish": "non-mesozoic",
    "Laughing Kookaburra": "non-mesozoic",
    "Leonberger": "non-mesozoic",  # dog
    "Lesser Kudu": "non-mesozoic",
    "Lettered Ara ari": "non-mesozoic",  # toucan (Araçari)
    "Lettered Araçari": "non-mesozoic",
    "Loggerhead Shrike": "non-mesozoic",
    "Lowland Anoa": "non-mesozoic",
    "Magnificent Frigatebird": "non-mesozoic",
    "Magnificent Sea Anemone": "non-mesozoic",
    "Mainland Serow": "non-mesozoic",
    "Malay (Rooster)": "non-mesozoic",
    "Malayan Tapir": "non-mesozoic",
    "Malayan Tigress": "non-mesozoic",
    "Mangrove Snapper": "non-mesozoic",
    "Manticora imperator": "non-mesozoic",  # beetle
    "Marimbondo-tatu": "non-mesozoic",  # wasp
    "Mbu Puffer": "non-mesozoic",
    "Meadow Vole": "non-mesozoic",
    "Megacephala virginica": "non-mesozoic",  # beetle
    "Megalara garuda": "non-mesozoic",  # wasp
    "Mexican Beaded LIzard": "non-mesozoic",
    "Microtityus jaumei": "non-mesozoic",  # scorpion
    "Mishmi Takin": "non-mesozoic",
    "Mombasa Golden Starburst Tarantula": "non-mesozoic",
    "Morning Sun Star": "non-mesozoic",  # starfish
    "Mountain Anoa": "non-mesozoic",
    "Mountain Bluebird": "non-mesozoic",
    "Mountain Tapir": "non-mesozoic",
    "Muskellunge": "non-mesozoic",
    "Muskox": "non-mesozoic",
    "Mussurana": "non-mesozoic",  # snake
    "Myrmecia brevinoda": "non-mesozoic",  # ant
    "New Guinea Singing Dog": "non-mesozoic",
    "Nguni": "non-mesozoic",  # cattle
    "Nilgai": "non-mesozoic",
    "North Sulawesi Babirusa": "non-mesozoic",
    "Northern (Abyssinian) Ground Hornbill": "non-mesozoic",
    "O'Halloran Hounds": "non-mesozoic",
    "Odontomachus monticola": "non-mesozoic",  # ant
    "Okapi": "non-mesozoic",
    "Omus dejeani": "non-mesozoic",  # beetle
    "Osprey": "non-mesozoic",
    "Pacific Electric Ray": "non-mesozoic",
    "Painted Coral Snake": "non-mesozoic",
    "Painted Moray": "non-mesozoic",
    "Patas Monkey": "non-mesozoic",
    "Perentie": "non-mesozoic",  # monitor lizard
    "Piraiba": "non-mesozoic",  # catfish
    "Portuguese Man o' War": "non-mesozoic",
    "Prairie Yellowjacket": "non-mesozoic",
    "Prairie Yellowjackets": "non-mesozoic",
    "Presa Canario": "non-mesozoic", "Presa Canarios": "non-mesozoic",
    "Pygmy Coral Snake": "non-mesozoic",
    "Pygmy Hog": "non-mesozoic",
    "Pyrenean Mountain Dog": "non-mesozoic",
    "Rainbow Lorikeet": "non-mesozoic",
    "Red Grouper": "non-mesozoic",
    "Red Kite": "non-mesozoic",
    "Red Panda": "non-mesozoic",
    "Red River Hog": "non-mesozoic",
    "Red-footed Cannibalfly": "non-mesozoic",
    "Red-legged Seriema (Crested Cariama)": "non-mesozoic",
    "Red-throated Loon": "non-mesozoic",
    "Reeves's Muntjac": "non-mesozoic",
    "Rook": "non-mesozoic",
    "Rosecone Cuttlefish": "non-mesozoic",
    "Ruby-throated Hummingbird": "non-mesozoic",
    "Russian Blue": "non-mesozoic",  # cat breed
    "Sable": "non-mesozoic",  # marten
    "Saga pedo": "non-mesozoic", "Sago pedo": "non-mesozoic",  # cricket
    "Saint Bernard": "non-mesozoic", "Saint Bernards": "non-mesozoic",
    "Sand (Gould's) Goanna": "non-mesozoic",
    "Savuti Pride": "non-mesozoic",  # lions
    "Scalloped Hammerhead": "non-mesozoic",
    "Secretary Bird": "non-mesozoic",
    "Sectretary Bird": "non-mesozoic",  # typo variant
    "Serama (Rooster)": "non-mesozoic",
    "Shar Pei": "non-mesozoic",
    "Sharpe's Grysbok": "non-mesozoic",
    "Shiba Inu": "non-mesozoic",
    "Shining Bronze-cuckoo": "non-mesozoic",
    "Shoebill": "non-mesozoic",
    "Short-eared Dog (Small-eared Zorro)": "non-mesozoic",
    "Shortfin Mako": "non-mesozoic",
    "Sia ferox": "non-mesozoic",  # insect
    "Siberian Tigress": "non-mesozoic",
    "Silvery Marmoset": "non-mesozoic",
    "Smalltooth Sawfish": "non-mesozoic",
    "Smooth Newt": "non-mesozoic",
    "Snow Petrel": "non-mesozoic",
    "South American (Brazilian) Tapir": "non-mesozoic",
    "South American Bushmaster": "non-mesozoic",
    "South American Coati": "non-mesozoic",
    "Southern Crested Caracara": "non-mesozoic",
    "Southern Ground-hornbill": "non-mesozoic",
    "Southern Ground-hornbills": "non-mesozoic",
    "Southern Mussurana": "non-mesozoic",
    "Spatterdock Darner": "non-mesozoic",
    "Spiny Dogfish": "non-mesozoic",
    "Staghounds": "non-mesozoic",
    "Stygian Robber": "non-mesozoic",  # robber fly
    "Sugar Glider": "non-mesozoic",
    "Sumatran Tigress": "non-mesozoic",
    "Surinam Horned Frog": "non-mesozoic",
    "Swamp Darner": "non-mesozoic",
    "Swinford Bandog": "non-mesozoic",  # dog
    "Takin": "non-mesozoic",
    "Tasmanian Devil": "non-mesozoic",
    "Tawny Frogmouth": "non-mesozoic",
    "Texas Brown Tarantula": "non-mesozoic",
    "Texas Horned Lizard": "non-mesozoic",
    "Texas Longhorn": "non-mesozoic",  # cattle
    "Titan Triggerfish": "non-mesozoic",
    "Vaquita": "non-mesozoic",
    "Venezuelan Red Howler": "non-mesozoic",
    "Vervet Monkey": "non-mesozoic",
    "Virginia Opossum": "non-mesozoic",
    "Wahoo": "non-mesozoic",  # fish
    "Wandering Albatross": "non-mesozoic",
    "Warthog": "non-mesozoic",
    "Water Bug": "non-mesozoic",
    "West African Lungfish": "non-mesozoic",
    "West Caucasian Tur": "non-mesozoic",
    "West Indian Ocean Coelacanth": "non-mesozoic",
    "Western Jackdaw": "non-mesozoic",
    "Western Marsh Harrier": "non-mesozoic",
    "Western Pygmy Marmoset": "non-mesozoic",
    "White Sturgeon": "non-mesozoic",
    "White-lipped Peccary": "non-mesozoic",
    "White-tailed Dunnart": "non-mesozoic",
    "Wild Yak": "non-mesozoic",
    "arplaninac": "non-mesozoic",  # Šarplaninac dog
    "Šarplaninac": "non-mesozoic",
    # Cenozoic/Paleozoic extinct animals (NOT Mesozoic):
    "Agriotherium africanum": "non-mesozoic",     # Cenozoic bear
    "Albanosmilus jourdani": "non-mesozoic",       # Cenozoic barbourofelid
    "American Mastodon": "non-mesozoic",           # Cenozoic
    "American Scimitar": "non-mesozoic",           # Homotherium serum
    "Anachlysictis gracilis": "non-mesozoic",      # Cenozoic sparassodont
    "Anancus arvernensis": "non-mesozoic",         # Cenozoic proboscidean
    "Ankalagon saurognathus": "non-mesozoic",      # Cenozoic mesonychid
    "Ankylorhiza tiedemani": "non-mesozoic",       # Cenozoic whale
    "Anomalocaris spp.": "non-mesozoic",           # Cambrian (Paleozoic)
    "Archaeotherium mortoni": "non-mesozoic",      # Cenozoic entelodont
    "Arthropleura armata": "non-mesozoic",         # Carboniferous (Paleozoic)
    "Astrapotherium magnum": "non-mesozoic",       # Cenozoic
    "Aurochs": "non-mesozoic", "Aurochs (Holocene)": "non-mesozoic",
    "Aurochs (Pleistocene)": "non-mesozoic",
    "Australopithecus africanus": "non-mesozoic",  # Cenozoic hominin
    "Barylambda faberi": "non-mesozoic",           # Cenozoic pantodont
    "Borhyaena tuberata": "non-mesozoic",          # Cenozoic sparassodont
    "Borson's Mastodon": "non-mesozoic",           # Cenozoic
    "Boryaena tuberata": "non-mesozoic",           # duplicate spelling
    "Boverisuchus magnifrons": "non-mesozoic",     # Eocene croc
    "Brachycrus spp.": "non-mesozoic",             # Cenozoic oreodont
    "Brontoscorpio anglicus": "non-mesozoic",      # Silurian (Paleozoic)
    "Chapalmalania altaefrontis": "non-mesozoic",  # Cenozoic procyonid
    "Chilotherium wimani": "non-mesozoic",         # Cenozoic rhino
    "Columbian Mammoth": "non-mesozoic",
    "Cretan Dwarf Mammoth": "non-mesozoic",
    "Crocodylus thorbjarnarsoni": "non-mesozoic",  # Pleistocene croc
    "Cynthiacetus maxwelli": "non-mesozoic",       # Cenozoic whale
    "Daphoenodon spp.": "non-mesozoic",            # Cenozoic bear-dog
    "Deinotherium thraceiensis": "non-mesozoic",   # Cenozoic proboscidean
    "Dinictis felina": "non-mesozoic",             # Cenozoic nimravid
    "Dinopithecus ingens": "non-mesozoic",         # Cenozoic baboon
    "Dorudon serratus": "non-mesozoic",            # Cenozoic whale
    "Ekorus ekakeran": "non-mesozoic",             # Cenozoic mustelid
    "Equus giganteus": "non-mesozoic",             # Cenozoic horse
    "Eremotherium spp.": "non-mesozoic",           # Cenozoic ground sloth
    "European Scimitar": "non-mesozoic",           # Homotherium
    "Garganornis ballmanni": "non-mesozoic",       # Miocene bird
    "Hapalops spp.": "non-mesozoic",               # Cenozoic ground sloth
    "Harpagolestes immanis": "non-mesozoic",       # Cenozoic mesonychid
    "Helicoprion clerci": "non-mesozoic",          # Permian (Paleozoic) fish
    "Hemicyon sansaniensis": "non-mesozoic",       # Cenozoic bear-dog
    "Hesperocyon spp.": "non-mesozoic",            # Cenozoic canid
    "Holmesina septentrionalis": "non-mesozoic",   # Cenozoic armadillo
    "Hurdia victoria": "non-mesozoic",             # Cambrian (Paleozoic)
    "Hyracotherium leporinum": "non-mesozoic",     # Cenozoic horse
    "Indarctos oregonensis": "non-mesozoic",       # Cenozoic bear
    "Jaekelopterus rhenaniae": "non-mesozoic",     # Devonian (Paleozoic)
    "Kerberos langebadreae": "non-mesozoic",       # Cenozoic hyaenodont
    "Kubanochoerus gigas": "non-mesozoic",         # Cenozoic pig
    "Lycaenops ornatus": "non-mesozoic",           # Permian gorgonopsid (synapsid)
    "Machaeroides eothen": "non-mesozoic",         # Cenozoic creodont
    "Macroeuphractus outesi": "non-mesozoic",      # Cenozoic armadillo
    "Megalictis ferox": "non-mesozoic",            # Cenozoic mustelid
    "Megalochelys atlas": "non-mesozoic",          # Cenozoic tortoise
    "Megalochoerus khinzikebirus": "non-mesozoic", # Cenozoic pig
    "Mesohippus spp.": "non-mesozoic",             # Cenozoic horse
    "Metamynodon planifrons": "non-mesozoic",      # Cenozoic amynodont
    "Microleo attenboroughi": "non-mesozoic",      # Cenozoic marsupial lion
    "Miracinonyx trumani": "non-mesozoic",         # Cenozoic American cheetah
    "Mukupirna nambensis": "non-mesozoic",         # Cenozoic marsupial
    "Nimravus brachyops": "non-mesozoic",          # Cenozoic nimravid
    "Nuralagus rex": "non-mesozoic",               # Cenozoic rabbit
    "Obdurodon tharalkooschild": "non-mesozoic",   # Cenozoic platypus
    "Palaeoloxodon mnaidriensis": "non-mesozoic",  # Cenozoic dwarf elephant
    "Parahelicoprion spp.": "non-mesozoic",        # Paleozoic fish
    "Paranthropus boisei": "non-mesozoic",         # Cenozoic hominin
    "Paranthropus robustus": "non-mesozoic",
    "Pasimachus californicus": "non-mesozoic",     # beetle
    "Pasimachus depressus": "non-mesozoic",
    "Patriofelis ferox": "non-mesozoic",           # Cenozoic creodont
    "Pelorovis spp.": "non-mesozoic",              # Cenozoic buffalo
    "Perucetus colossus": "non-mesozoic",          # Cenozoic whale
    "Plionarctos edensis": "non-mesozoic",         # Cenozoic bear
    "Proailurus lemanensis": "non-mesozoic",       # Cenozoic felid
    "Protocyon troglodytes": "non-mesozoic",       # Cenozoic canid
    "Pseudocyon sansaniensis": "non-mesozoic",     # Cenozoic bear-dog
    "Pterygotus grandidentatus": "non-mesozoic",   # Paleozoic sea scorpion
    "Pulmonoscorpius kirktonensis": "non-mesozoic",# Carboniferous scorpion
    "Pygmy Mammoth": "non-mesozoic",
    "Quercylurus major": "non-mesozoic",           # Cenozoic cat
    "Saivodus striatus": "non-mesozoic",           # Carboniferous shark
    "Sarkastodon mongoliensis": "non-mesozoic",    # Cenozoic creodont
    "Sibotherium ka": "non-mesozoic",              # Cenozoic
    "Southern Mammoth": "non-mesozoic",
    "Steppe Mammoth": "non-mesozoic",
    "Stegodon trigonocephalus": "non-mesozoic",    # Cenozoic proboscidean
    "Synoplotherium vorax": "non-mesozoic",        # Cenozoic mesonychid
    "Synthetoceras tricornatus": "non-mesozoic",   # Cenozoic protoceratid
    "Tartarocyon cazanavei": "non-mesozoic",       # Cenozoic amphicyonid
    "Thalassocnus spp.": "non-mesozoic",           # Cenozoic aquatic sloth
    "Theriodictis platensis": "non-mesozoic",      # Cenozoic canid
    "Thylophorops lorenzinii": "non-mesozoic",     # Cenozoic sparassodont
    "Tiktaalik roseae": "non-mesozoic",            # Devonian (Paleozoic)
    "Ursavus elmensis": "non-mesozoic",            # Cenozoic bear
    "Wakaleo schouteni": "non-mesozoic",           # Cenozoic marsupial lion
    "Wakaleo vanderleuri": "non-mesozoic",
    "Whollydooleya tomnpatrichorum": "non-mesozoic", # Cenozoic marsupial
    "Wonambi naracoortensi": "non-mesozoic",       # Pleistocene snake
    "Woolly Mammoth": "non-mesozoic",
    "Xiphiorhynchus rotundus": "non-mesozoic",     # Cenozoic billfish
    "Ysengrinia spp.": "non-mesozoic",             # Cenozoic amphicyonid
    # Synapsids (Permian-Triassic, user's category 1):
    "Ischigualastia jenseni": "non-mesozoic",      # Triassic dicynodont
    "Lisowicia bojani": "non-mesozoic",            # Triassic dicynodont
    "Placerias hesternus": "non-mesozoic",         # Triassic dicynodont
    "Tapinocephalus atherstonei": "non-mesozoic",  # Permian dinocephalian
    # Mesozoic mammals (user groups with non-mesozoic):
    "Didelphodon vorax": "non-mesozoic",           # Cretaceous mammal
    "Gobiconodon spp.": "non-mesozoic",            # Cretaceous mammal
    "Repenomamus robustus": "non-mesozoic",        # Cretaceous mammal
    "Repenomamus giganticus": "non-mesozoic",
    "Triconodon mordax": "non-mesozoic",           # Mesozoic mammal
    # Mesozoic non-dinosaurs (additional):
    "Archelon ischyros": "mesozoic-other",         # Cretaceous sea turtle
    "Beelzebufo ampinga": "mesozoic-other",        # Cretaceous frog
    "Cretoxyrhina mantelli": "mesozoic-other",     # Cretaceous shark
    "Dromaeosauroides bornholmensis": "mesozoic-other",  # wait — this IS a dromaeosaurid = dinosaur!
    "Kyhytysuka sachicarum": "mesozoic-other",     # Cretaceous ichthyosaur
    "Leedsichthys problematicus": "mesozoic-other",# Jurassic fish
    "Onchopristis numida": "mesozoic-other",       # Cretaceous sawfish
    "Sillosuchus longicervix": "mesozoic-other",   # Triassic archosaur
    "Trochosuchus acutus": "mesozoic-other",       # Mesozoic croc
    "Tusotheuthis longa": "mesozoic-other",        # Cretaceous squid
    "Oculudentavis khaungraae": "mesozoic-other",  # Cretaceous (disputed, likely lizard)
    # Mesozoic dinosaurs (additional):
    "Dromaeosauroides bornholmensis": "dinosaur",  # Cretaceous dromaeosaurid
    "Eocarcharia dinops": "dinosaur",              # Cretaceous carcharodontosaurid
    "Moros intrepidus": "dinosaur",                # Cretaceous tyrannosauroid
    "Shaochilong maortuensis": "dinosaur",         # Cretaceous carcharodontosaurid
    "Aletopelta coombsi": "dinosaur",              # Cretaceous ankylosaur
    "Gigantophis garstini": "non-mesozoic",        # Eocene snake
    "Platybelodon spp.": "non-mesozoic",           # Miocene proboscidean
    "Proborhyaena gigantea": "non-mesozoic",       # Cenozoic sparassodont
    "Proterogyrinus scheelei": "non-mesozoic",     # Carboniferous (Paleozoic)
    "Proterogyrinus scheeleri": "non-mesozoic",    # alternate spelling
    "Thylacine": "non-mesozoic",                   # recently extinct marsupial
    "Thylacine (hunting pair)": "non-mesozoic",
}


def strip_group_qualifiers(name):
    """Extract the base species/animal name, stripping group modifiers.

    'Cheetah (coalition of 5)' → 'Cheetah'
    'Dire Wolf (pack of 3)'   → 'Dire Wolf'
    'Lioness (pride of 2)'    → 'Lioness'
    'Bengal Tiger'             → 'Bengal Tiger'
    'Smilodon fatalis (female)' → 'Smilodon fatalis'
    """
    # Remove group/count qualifiers
    name = re.sub(
        r"\s*\("
        r"(?:pack|coalition|pride|clan|pod|flock|group|troop|herd|float|romp|"
        r"venue|skulk|murder|unkindness|rafter|squadron|band|mischief|"
        r"richness|aerie|pair|mated pair|monogamic pair|hunting pair|school|shoal)"
        r"\s+(?:of\s+)?\d[\d\s/\-]*\)",
        "", name, flags=re.IGNORECASE
    )
    # Remove count suffixes like "Rottweilers (8)" or "Kangals (3)"
    name = re.sub(r"\s*\(\d+\)", "", name)
    # Remove count prefixes like "Dogo Argentinos (2)" → "Dogo Argentino"
    # (but be careful not to strip meaningful parentheticals)
    # Remove sex/age qualifiers
    name = re.sub(
        r"\s*\((?:male|female|sow|boar|cow|bull|hen|stallion|"
        r"both unarmed|unarmed|armed|armed with [\w\s]+|"
        r"strong male|large [\w]+|breeding pair)\)",
        "", name, flags=re.IGNORECASE
    )
    # Remove trailing count like "Kangals (5)" already handled
    # Strip trailing 's' from pluralized group names: "Rottweilers" → "Rottweiler"
    # (only if the name was clearly pluralized for a group count)
    name = name.strip()
    return name


_last_429_time = 0  # tracks when we last hit a 429


def _wiki_request(url, max_retries=5):
    """Make a Wikipedia API request with proper User-Agent and 429 backoff."""
    global _last_429_time
    # If we recently hit a 429, wait extra before even trying
    since_429 = time.time() - _last_429_time
    if since_429 < 30:
        cooldown = 30 - since_429
        time.sleep(cooldown)

    req = urllib.request.Request(url, headers={
        "User-Agent": "AnimalPowerRatings/1.0 (taxonomy classifier; Python urllib)"
    })
    for attempt in range(max_retries):
        try:
            with urllib.request.urlopen(req, timeout=10) as resp:
                return json.loads(resp.read().decode())
        except urllib.error.HTTPError as e:
            if e.code == 429:
                _last_429_time = time.time()
                wait = 30 * (2 ** attempt)  # 30s, 60s, 120s, 240s, 480s
                print(f"    Rate limited (429). Waiting {wait}s before retry...")
                time.sleep(wait)
            elif attempt < max_retries - 1:
                time.sleep(2)
            else:
                raise
        except Exception as e:
            if attempt < max_retries - 1:
                time.sleep(2)
            else:
                raise


def search_wikipedia(query, max_retries=5):
    """Search Wikipedia and return the first matching page title, or None.
    Returns False (not None) on API failure to distinguish 'no results' from 'error'."""
    url = "https://en.wikipedia.org/w/api.php?" + urllib.parse.urlencode({
        "action": "query",
        "list": "search",
        "srsearch": query,
        "srlimit": 1,
        "format": "json",
    })
    try:
        data = _wiki_request(url, max_retries)
        results = data.get("query", {}).get("search", [])
        if results:
            return results[0]["title"]
        return None  # no results found (legitimate)
    except Exception as e:
        print(f"    Wikipedia search failed for {query!r}: {e}")
        return False  # API error — should retry later


def get_page_categories_and_extract(title, max_retries=5):
    """Get Wikipedia categories and first section of article text for a page.
    Returns None on API failure to distinguish from 'page exists but is empty'."""
    url = "https://en.wikipedia.org/w/api.php?" + urllib.parse.urlencode({
        "action": "query",
        "titles": title,
        "prop": "categories|extracts",
        "cllimit": "50",
        "exintro": "true",
        "explaintext": "true",
        "exsectionformat": "plain",
        "format": "json",
    })
    try:
        data = _wiki_request(url, max_retries)
        pages = data.get("query", {}).get("pages", {})
        for page_id, page_data in pages.items():
            if page_id == "-1":
                return [], ""
            cats = [c["title"].replace("Category:", "").lower()
                    for c in page_data.get("categories", [])]
            extract = page_data.get("extract", "")
            return cats, extract
        return [], ""
    except Exception as e:
        print(f"    Wikipedia fetch failed for {title!r}: {e}")
        return None  # API error — should retry later


def classify_from_text(categories, extract):
    """Classify an animal based on Wikipedia categories and intro text.

    Returns: 'dinosaur', 'mesozoic-other', 'non-mesozoic', or None if unsure.
    """
    all_text = " ".join(categories).lower() + " " + extract.lower()

    # Check for dinosaur indicators
    dino_keywords = [
        "dinosaur", "theropod", "sauropod", "ornithischian", "saurischian",
        "ceratopsian", "hadrosaurid", "ankylosaur", "stegosaur",
        "dromaeosaurid", "tyrannosaurid", "abelisaurid", "carcharodontosaurid",
        "spinosaurid", "allosaurid", "oviraptorid", "therizinosaurid",
        "pachycephalosaur", "iguanodont", "titanosaur", "diplodocid",
    ]
    is_dinosaur = any(kw in all_text for kw in dino_keywords)

    # Check for Mesozoic non-dinosaur indicators
    meso_other_keywords = [
        "pterosaur", "plesiosaur", "ichthyosaur", "mosasaur", "nothosaur",
        "pliosaur", "elasmosaur", "marine reptile",
        "rhynchosaur", "phytosaur", "aetosaur", "rauisuchid", "rauisuchia",
        "crocodylomorph",  # Mesozoic crocs
        "metriorhynchid", "thalattosuch", "temnospondyl",
        "archosauriform", "proterosuchid", "erythrosuchid",
    ]
    is_meso_other = any(kw in all_text for kw in meso_other_keywords)

    # Check time period
    mesozoic_keywords = [
        "cretaceous", "jurassic", "triassic", "mesozoic",
        "late cretaceous", "early cretaceous", "late jurassic",
    ]
    is_mesozoic_era = any(kw in all_text for kw in mesozoic_keywords)

    # Check for clearly non-Mesozoic era indicators
    non_mesozoic_era_keywords = [
        "cenozoic", "pleistocene", "holocene", "miocene", "pliocene",
        "oligocene", "eocene", "paleocene", "paleogene", "neogene",
        "paleozoic", "permian", "carboniferous", "devonian", "silurian",
        "ordovician", "cambrian",
    ]
    is_non_mesozoic_era = any(kw in all_text for kw in non_mesozoic_era_keywords)

    # Check for other modern/extant indicators
    modern_keywords = [
        "extant", "living species", "mammal", "primate", "canid", "felid",
        "bovid", "cervid", "ursid", "mustelid", "cetacean", "pinniped",
        "bird of prey", "passerine", "accipitridae", "falconidae",
        "insect", "arachnid", "crustacean", "mollus",
        "elephant bird", "moa", "terror bird", "phorusrhacid",
        "ratite",
    ]
    is_modern = is_non_mesozoic_era or any(kw in all_text for kw in modern_keywords)

    synapsid_keywords = [
        "synapsid", "therapsid", "pelycosaur", "dicynodont", "gorgonopsid",
        "dinocephalian", "anomodont", "cynodont",
    ]
    is_synapsid = any(kw in all_text for kw in synapsid_keywords)

    # Classification logic
    # The tricky case: a Mesozoic dinosaur article that mentions "Cenozoic" in
    # passing (e.g. "birds survived into the Cenozoic") vs a post-Mesozoic bird
    # article that mentions "Dinosauria" cladistically. The key signal is whether
    # a Mesozoic era keyword (Cretaceous/Jurassic/Triassic) is present alongside
    # the dinosaur keyword — if so, the animal itself lived in the Mesozoic.
    if is_synapsid:
        return "non-mesozoic"
    if is_meso_other:
        return "mesozoic-other"
    if is_dinosaur and is_mesozoic_era:
        return "dinosaur"  # Mesozoic era + dinosaur = real Mesozoic dinosaur
    if is_dinosaur and not is_mesozoic_era and is_modern:
        return "non-mesozoic"  # dinosaur keyword but only non-Mesozoic eras → post-Mesozoic bird
    if is_dinosaur and not is_mesozoic_era and not is_modern:
        return "dinosaur"  # dinosaur keyword, no era info → assume Mesozoic
    if is_mesozoic_era and not is_modern:
        return "mesozoic-other"  # Mesozoic but not clearly dinosaur
    return "non-mesozoic"  # default


# ---------------------------------------------------------------------------
# Name-based classification (no API calls needed)
# ---------------------------------------------------------------------------

# Dinosaur genus suffixes and name patterns
_DINO_SUFFIXES = [
    "saurus", "raptor", "ceratops", "venator", "titan",
    "tyrannus", "dromaeus", "ornithomimus",
]

# Known dinosaur genera (first word of binomial names)
_DINO_GENERA = {
    "Tyrannosaurus", "Tarbosaurus", "Allosaurus", "Acrocanthosaurus",
    "Carcharodontosaurus", "Giganotosaurus", "Mapusaurus", "Saurophaganax",
    "Spinosaurus", "Suchomimus", "Baryonyx", "Irritator", "Oxalaia",
    "Ceratosaurus", "Dilophosaurus", "Carnotaurus", "Abelisaurus",
    "Majungasaurus", "Rugops", "Aucasaurus", "Ekrixinatosaurus",
    "Skorpiovenator", "Pycnonemosaurus",
    "Velociraptor", "Deinonychus", "Utahraptor", "Dakotaraptor",
    "Achillobator", "Dromaeosaurus", "Austroraptor", "Linheraptor",
    "Triceratops", "Torosaurus", "Styracosaurus", "Pentaceratops",
    "Eotriceratops", "Titanoceratops", "Nasutoceratops", "Diabloceratops",
    "Einiosaurus", "Chasmosaurus", "Protoceratops", "Zuniceratops",
    "Pachyrhinosaurus", "Utahceratops",
    "Stegosaurus", "Kentrosaurus", "Dacentrurus", "Hesperosaurus",
    "Ankylosaurus", "Euoplocephalus", "Gastonia", "Gargoyleosaurus",
    "Zuul", "Minmi", "Sauropelta",
    "Apatosaurus", "Brontosaurus", "Diplodocus", "Argentinosaurus",
    "Patagotitan", "Futalognkosaurus", "Sauroposeidon", "Brachiosaurus",
    "Europasaurus", "Ohmdenosaurus", "Astrodon", "Rhoetosaurus",
    "Amargasaurus", "Sonorasaurus", "Paralititan", "Shunosaurus",
    "Edmontosaurus", "Parasaurolophus", "Lambeosaurus", "Shantungosaurus",
    "Iguanodon", "Camptosaurus", "Tenontosaurus", "Rhabdodon",
    "Zalmoxes", "Magnapaulia",
    "Pachycephalosaurus", "Dracorex",
    "Therizinosaurus", "Deinocheirus", "Gigantoraptor", "Anzu",
    "Citipati", "Gallimimus", "Ornithomimus", "Oviraptor",
    "Coelophysis", "Herrerasaurus", "Eoraptor", "Eodromaeus",
    "Compsognathus", "Ornitholestes", "Sinosauropteryx",
    "Yutyrannus", "Nanuqsaurus", "Albertosaurus", "Gorgosaurus",
    "Daspletosaurus", "Lythronax", "Teratophoneus", "Qianzhousaurus",
    "Alioramus", "Alectrosaurus", "Suskityrannus", "Timurlengia",
    "Gojirasaurus", "Liliensternus", "Monolophosaurus", "Cryolophosaurus",
    "Megalosaurus", "Torvosaurus", "Metriacanthosaurus", "Afrovenator",
    "Neovenator", "Megaraptor", "Australovenator", "Siats", "Orkoraptor",
    "Concavenator", "Sinraptor", "Yangchuanosaurus", "Meraxes",
    "Blikanasaurus", "Riojasaurus",
    "Phuwiangosaurus", "Stenonychosaurus",
    "Thanos", "Maip", "Sigilmassasaurus",
    "Yi", "Ambopteryx", "Archaeopteryx",  # Mesozoic birds/near-birds
}

# Mesozoic non-dinosaur genera
_MESO_OTHER_GENERA = {
    # Pterosaurs
    "Quetzalcoatlus", "Hatzegopteryx", "Pteranodon", "Dimorphodon",
    # Marine reptiles
    "Mosasaurus", "Tylosaurus", "Prognathodon", "Globidens", "Clidastes",
    "Pliosaurus", "Kronosaurus", "Liopleurodon", "Rhomaleosaurus",
    "Megacephalosaurus", "Sachicasaurus",
    "Ichthyosaurus", "Temnodontosaurus", "Ophthalmosaurus", "Shastasaurus",
    "Cymbospondylus", "Thalattoarchon", "Himalayasaurus", "Shonisaurus",
    "Elasmosaurus", "Albertonectes",
    # Mesozoic crocs and archosaurs
    "Deinosuchus", "Sarcosuchus", "Smilosuchus", "Kaprosuchus",
    "Stomatosuchus", "Dakosaurus",
    "Postosuchus", "Rauisuchus", "Saurosuchus", "Fasolasuchus",
    "Prestosuchus", "Batrachotomus", "Erythrosuchus", "Proterosuchus",
    "Smok",
    # Mesozoic temnospondyls
    "Mastodonsaurus", "Koolasuchus",
    # Mesozoic marine crocs
    "Geosaurus", "Metriorhynchus",
    "Leptosuchus",  # phytosaur
    "Carbonemys",   # actually Cenozoic but often grouped with Mesozoic
}

# Obviously modern/non-mesozoic animals (common names)
_MODERN_ANIMALS = {
    # Big cats
    "Lion", "Lioness", "Tiger", "Leopard", "Leopardess", "Jaguar", "Jaguaress",
    "Cheetah", "Cougar", "Panther", "Puma", "Snow Leopard", "Snow Leopardess",
    "Clouded Leopard", "Clouded Leopardess",
    # Other cats
    "Cat", "Bobcat", "Lynx", "Ocelot", "Serval", "Caracal", "Margay", "Jaguarundi",
    "Wildcat", "Feral Cat", "Sand Cat", "Fishing Cat",
    # Canids
    "Wolf", "Wolves", "Coyote", "Dingo", "Fox", "Jackal", "Dhole",
    "African Wild Dog", "Bush Dog", "Maned Wolf",
    # Bears
    "Bear", "Grizzly", "Polar Bear",
    # Dogs (domestic)
    "Terrier", "Shepherd", "Mastiff", "Bulldog", "Rottweiler", "Pitbull",
    "Kangal", "Akita", "Doberman", "Poodle", "Retriever", "Malinois",
    "Husky", "Chihuahua", "Shih Tzu", "Borzoi", "Greyhound", "Wolfhound",
    "Ridgeback", "Pinscher", "Corso", "Boerboel", "Tosa",
    # Marine mammals
    "Whale", "Dolphin", "Orca", "Porpoise", "Seal", "Sea Lion", "Walrus",
    "Narwhal", "Beluga", "Manatee",
    # Primates
    "Gorilla", "Chimpanzee", "Orangutan", "Baboon", "Mandrill", "Macaque",
    "Human", "Neanderthal", "Homo",
    # Ungulates
    "Elephant", "Rhinoceros", "Hippopotamus", "Giraffe", "Zebra", "Horse",
    "Donkey", "Camel", "Bison", "Buffalo", "Cattle", "Bull", "Cow",
    "Elk", "Moose", "Deer", "Antelope", "Gazelle", "Wildebeest",
    "Goat", "Sheep", "Ibex",
    # Mustelids & small carnivores
    "Wolverine", "Badger", "Otter", "Weasel", "Mink", "Fisher", "Marten",
    "Tayra", "Grison", "Ferret", "Honey Badger",
    # Birds (all modern)
    "Eagle", "Hawk", "Falcon", "Owl", "Vulture", "Condor",
    "Crow", "Raven", "Jay", "Magpie",
    "Swan", "Goose", "Duck", "Pelican", "Heron", "Stork",
    "Ostrich", "Cassowary", "Emu", "Kiwi", "Penguin",
    "Parrot", "Macaw", "Cockatoo", "Kea",
    "Chicken", "Turkey", "Peacock", "Peafowl",
    # Reptiles (extant)
    "Crocodile", "Alligator", "Caiman", "Gharial", "Gavial",
    "Monitor", "Iguana", "Gecko", "Chameleon", "Skink",
    "Cobra", "Mamba", "Viper", "Python", "Anaconda", "Boa",
    "Rattlesnake", "Taipan",
    "Turtle", "Tortoise",
    # Fish (extant)
    "Shark", "Piranha", "Barracuda", "Catfish", "Pike",
    "Marlin", "Swordfish", "Eel", "Stingray",
    # Invertebrates
    "Spider", "Scorpion", "Centipede", "Crab", "Lobster",
    "Ant", "Wasp", "Hornet", "Beetle", "Mantis", "Dragonfly",
    "Octopus", "Squid", "Jellyfish",
    # Other mammals
    "Hyena", "Mongoose", "Civet", "Raccoon", "Skunk",
    "Bat", "Hedgehog", "Porcupine", "Rabbit", "Hare",
    "Rat", "Mouse", "Squirrel", "Beaver",
    "Kangaroo", "Wombat", "Koala", "Quoll",
    "Armadillo", "Anteater", "Sloth", "Pangolin", "Aardvark",
    "Fossa",
}

# Prehistoric but non-Mesozoic genera (Cenozoic, Paleozoic, etc.)
_NON_MESO_GENERA = {
    # Saber-toothed cats
    "Smilodon", "Homotherium", "Machairodus", "Megantereon", "Xenosmilus",
    "Amphimachairodus", "Dinofelis", "Barbourofelis",
    # Prehistoric mammals
    "Arctodus", "Arctotherium", "Megatherium", "Mylodon", "Doedicurus",
    "Glyptodon", "Mammuthus", "Mammut", "Mastodon",
    "Megacerops", "Paraceratherium", "Arsinoitherium",
    "Andrewsarchus", "Daeodon", "Entelodon",
    "Simbakubwa", "Megistotherium", "Hyaenodon",
    "Josephoartigasia", "Phoberomys",
    "Basilosaurus", "Livyatan", "Brygmophyseter", "Acrophyseter",
    "Zygophyseter", "Ambulocetus", "Pakicetus",
    "Epicyon", "Amphicyon", "Borophagus",
    "Dire Wolf", "Cave Bear", "Cave Hyena", "Cave Lion",
    "Woolly Mammoth", "Woolly Rhinoceros",
    "Elasmotherium", "Megacamelus", "Sivatherium",
    "Thylacosmilus", "Thylacoleo", "Marsupial Lion",
    "Diprotodon", "Procoptodon",
    "Gigantopithecus", "Archaeoindris",
    "Kolponomos", "Enhydriodon",
    "Macrauchenia", "Toxodon",
    # Terror birds & post-Mesozoic birds
    "Titanis", "Kelenken", "Phorusrhacos", "Brontornis", "Gastornis",
    "Vorombe", "Dromornis", "Bullockornis",
    "Haast",  # Haast's Eagle
    # Cenozoic crocs
    "Purussaurus", "Quinkana", "Barinasuchus", "Gryposuchus",
    "Rhamphosuchus", "Mourasuchus",
    # Cenozoic sharks & fish
    "Carcharocles", "Otodus", "Dunkleosteus", "Rhizodus",
    "Xiphactinus", "Hyneria",
    # Synapsids (Permian/Paleozoic)
    "Dimetrodon", "Inostrancevia", "Anteosaurus", "Rubidgea",
    "Estemmenosuchus", "Lystrosaurus", "Titanophoneus", "Titanosuchus",
    "Sphenacodon", "Secodontosaurus", "Edaphosaurus",
    # Other Cenozoic
    "Dinocrocuta", "Percrocuta",
    "Titanoboa",  # Cenozoic snake
    "Megalania",  # Cenozoic lizard
    "Quetzalcoatlus",  # wait, this is Mesozoic - remove if present
    "Steller",  # Steller's Sea Cow etc.
}
# Fix: Quetzalcoatlus is Mesozoic, remove from non-meso
_NON_MESO_GENERA.discard("Quetzalcoatlus")


def classify_by_name(name):
    """Try to classify an animal purely from its name, no API needed.

    Returns 'dinosaur', 'mesozoic-other', 'non-mesozoic', or None if unsure.
    """
    # Check manual overrides first
    if name in MANUAL_OVERRIDES:
        return MANUAL_OVERRIDES[name]

    # Extract first word (potential genus)
    first_word = name.split()[0] if name else ""

    # Check genus lists
    if first_word in _DINO_GENERA:
        return "dinosaur"
    if first_word in _MESO_OTHER_GENERA:
        return "mesozoic-other"
    if first_word in _NON_MESO_GENERA:
        return "non-mesozoic"

    # Check dinosaur name suffixes (covers genera not in our list)
    name_lower = name.lower()
    for suffix in _DINO_SUFFIXES:
        # Check if any word in the name ends with a dino suffix
        for word in name_lower.split():
            if word.endswith(suffix) and len(word) > len(suffix):
                return "dinosaur"

    # Check for common modern animal keywords
    for keyword in _MODERN_ANIMALS:
        kw_lower = keyword.lower()
        # Match as whole word or at word boundary
        if kw_lower in name_lower.split() or name_lower.endswith(kw_lower):
            return "non-mesozoic"
        # Also check if name contains the keyword as a substring with word boundaries
        if f" {kw_lower}" in f" {name_lower}" or f"{kw_lower} " in f"{name_lower} ":
            return "non-mesozoic"

    return None  # unsure — needs Wikipedia lookup


def classify_animal(base_name, cache):
    """Classify a single animal. Uses cache to avoid repeated API calls.
    Returns 'retry' if API calls failed, so the entry can be re-attempted later."""
    if base_name in cache:
        return cache[base_name]

    # Try name-based classification first (no API needed)
    result = classify_by_name(base_name)
    if result is not None:
        cache[base_name] = result
        return result

    # Fall back to Wikipedia for ambiguous names
    time.sleep(1.5)  # rate limit between successive API calls
    title = search_wikipedia(base_name)
    if title is False:
        # API error — don't cache, mark for retry
        return "retry"
    if title is None:
        # No results — try with just the genus (first word of a binomial name)
        words = base_name.split()
        if len(words) >= 2 and words[0][0].isupper() and words[1][0].islower():
            title = search_wikipedia(words[0])
            if title is False:
                return "retry"
        if not title:
            cache[base_name] = "non-mesozoic"  # genuinely not found
            return "non-mesozoic"

    # Get page info
    time.sleep(1.5)  # rate limit: stay well under Wikipedia's threshold
    page_result = get_page_categories_and_extract(title)
    if page_result is None:
        # API error on page fetch — mark for retry
        return "retry"

    categories, extract = page_result
    result = classify_from_text(categories, extract)
    if result is None:
        result = "non-mesozoic"  # default

    cache[base_name] = result
    return result


def classify_ratings_file(csv_path):
    """Read a ratings CSV, correct corrupted names, classify, and write output.

    Writes each row to the output file as soon as it's classified, so progress
    is preserved if the script is interrupted. On restart, it resumes from
    where it left off by reading already-written rows from the output file.
    """
    rows = []
    with open(csv_path, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)

    print(f"Loaded {len(rows)} animals from {csv_path}")

    # Correct names and extract base species names
    corrected_names = {}
    base_names = {}
    corrections_applied = 0
    for row in rows:
        animal = row["animal"]
        fixed = correct_name(animal)
        if fixed != animal:
            corrections_applied += 1
        corrected_names[animal] = fixed
        base = strip_group_qualifiers(fixed)
        base_names[animal] = base

    if corrections_applied:
        print(f"Repaired {corrections_applied} corrupted name(s).")

    unique_bases = sorted(set(base_names.values()))
    print(f"Found {len(unique_bases)} unique base species names to look up.")

    # Check for existing output to resume from
    out_path = csv_path.rsplit(".", 1)[0] + "_classified.csv"
    already_done = {}  # rank -> (animal, power, category) for completed rows
    cache = {}
    retry_count = 0
    if Path(out_path).exists():
        with open(out_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["category"] == "retry":
                    retry_count += 1
                    continue  # don't cache or mark as done — will re-attempt
                already_done[row["rank"]] = row
                # Rebuild cache from previous successful classifications
                base = strip_group_qualifiers(row["animal"])
                cache[base] = row["category"]
        msg = f"Resuming: {len(already_done)} rows done"
        if retry_count:
            msg += f", {retry_count} to retry"
        print(f"{msg}.\n")
    else:
        print()

    # Rewrite entire output file: keep completed rows, re-attempt retries and new rows
    out_file = open(out_path, "w", newline="", encoding="utf-8")
    writer = csv.writer(out_file)
    writer.writerow(["rank", "animal", "power", "category"])

    counts = {"dinosaur": 0, "mesozoic-other": 0, "non-mesozoic": 0, "retry": 0}

    try:
        for row in rows:
            animal_original = row["animal"]
            rank = row["rank"]
            animal_fixed = corrected_names[animal_original]
            base = base_names[animal_original]

            # Use cached result from previous run if available
            if rank in already_done:
                cat = already_done[rank]["category"]
                counts[cat] += 1
                writer.writerow([rank, animal_fixed, row["power"], cat])
                continue

            # Classify (uses cache, tries name-based first, then API)
            if base not in cache:
                # Check if name-based will handle it (for logging)
                name_result = classify_by_name(base)
                cat = classify_animal(base, cache)
                done_so_far = len(cache)
                source = "name" if name_result is not None else "wiki"
                print(f"  [{done_so_far}/{len(unique_bases)}] ({source:4s}) {base:50s} → {cat}")
            else:
                cat = cache[base]

            counts[cat] += 1
            writer.writerow([rank, animal_fixed, row["power"], cat])
            out_file.flush()  # ensure it's written to disk immediately

    except KeyboardInterrupt:
        print(f"\n\nInterrupted! Progress saved to {out_path}")
        print(f"  Run the same command again to resume.")
        raise
    finally:
        out_file.close()

    if counts["retry"] > 0:
        print(f"\n{counts['retry']} entries need retry. Run again to re-attempt.")
    print(f"\nClassification complete:")
    print(f"  Dinosaurs:       {counts.get('dinosaur', 0)}")
    print(f"  Mesozoic other:  {counts.get('mesozoic-other', 0)}")
    print(f"  Non-Mesozoic:    {counts.get('non-mesozoic', 0)}")
    print(f"  Retry needed:    {counts.get('retry', 0)}")
    print(f"\nSaved to {out_path}")


if __name__ == "__main__":
    csv_path = sys.argv[1] if len(sys.argv) > 1 else "duels_ratings.csv"
    classify_ratings_file(csv_path)

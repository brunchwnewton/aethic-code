#!/usr/bin/env python3
"""Category graph: which entries name the same animal, and which are its other sex (new; input of coupled_fit.py).

Usage:  python3 category_graph.py [duels.csv]       -> category_graph.csv, category_graph.txt

Two kinds of link, between cleaned entry names (step 3's cleaning and aliases):
  taxon   child -> parent: the child is a living population or subspecies of the species the parent names, so their
          votes describe one animal. Found three ways:
            name     the child is a qualifier plus another entry's name, the longest such entry being the parent
                     ('West African Lion' -> 'African Lion' -> 'Lion', 'Bengal Tiger' -> 'Tiger');
            bracket  another entry's name plus a bracketed population qualifier ('African Leopard (Congo)');
            curated  subspecies whose names hide the species (CURATED: 'Kodiak Bear' -> 'Brown Bear', the grey wolf
                     subspecies -> 'Grey Wolf').
          Candidates are vetted by step 7's rule for its population lists: other species, extinct and fossil forms,
          settings ('(on land)') and loose names are cut (REJECT and NOT_LINKED give each reason). Links nest, so the
          taxon links form trees.
  female, male   child -> base: the child is the same animal's female or male form ('Lioness' -> 'Lion',
          'African Lioness' -> 'African Lion', 'Grey Wolf (female)' -> 'Grey Wolf', 'Human (male)' -> 'Human').
          Only plain sex qualifiers count; '(large male)', '(Serengeti male)' and the like are particular fighters and
          stay unlinked. A sex link crosses the trees, so the graph as a whole is not a tree.
Groups ('(pride of 3)') are never linked here: step 3 already ties each group to its solo animal.

category_graph.csv lists every candidate with its status, so a link can be switched on or off by editing that file;
coupled_fit.py reads the kept rows. Edits to the tables below take effect when this script is rerun."""
import sys, re, csv, collections, importlib.util

spec = importlib.util.spec_from_file_location('bt', '3_bt_fit.py'); bt = importlib.util.module_from_spec(spec); spec.loader.exec_module(bt)

FEMALE = {'female', 'sow', 'cow', 'hen', 'doe', 'bitch', 'vixen'}
MALE = {'male', 'boar', 'bull', 'stallion', 'dog', 'buck', 'stag', 'rooster', 'silverback'}
XESS = {'Lioness': 'Lion', 'Tigress': 'Tiger', 'Leopardess': 'Leopard', 'Jaguaress': 'Jaguar'}
# a bracket that marks a particular fighter (sex, size, age, arms, group) rather than a population
FIGHTER = re.compile(r"\b(?:males?|females?|sows?|boars?|cows?|bulls?|hens?|does?|bitch|vixen|stallions?|dog|bucks?|stags?|roosters?|"
                     r"she|silverback|large|small|big|huge|juvenile|young|old|adult|strong|armed|unarmed|with|spears?|clubs?|"
                     r"pairs?|pack|coalition|pride|clan|pod|flock|group|troop|herd|school|shoal|venue|skulk|of)\b|\d", re.I)
SETTING = re.compile(r"\b(?:in|on|battle|water|land)\b", re.I)
SPELLING = {'Grey Fox': 'Gray Fox'}          # base-name spelling variants seen only inside sex forms

# ---- vetting of the name and bracket candidates: child -> reason it is not the parent's species ----
REJECT = {
    # under Lion
    'American Lion': 'extinct species (Panthera atrox)', 'Barbary Lion': 'extinct in the wild; left out by step 7 as well',
    'California Sea Lion': 'a pinniped', 'South American Sea Lion': 'a pinniped', "Steller's (Northern) Sea Lion": 'a pinniped',
    'Early Middle Pleistocene European Cave Lion': 'extinct species (cave lion)', 'Eurasian Cave Lion': 'extinct species (Panthera spelaea)',
    'Marsupial Lion': 'a marsupial (Thylacoleo)', 'Natodomeri Lion': 'Pleistocene fossil lion',
    'Sambir Lion': 'not a recognized living population; its only matchup is against the fossil Bornean tiger',
    'Pleistocene African Lion': 'fossil form',
    # under Tiger
    'Bali Tiger': 'extinct subspecies (1940s)', 'Caspian Tiger': 'extinct subspecies (1970s)', 'Bornean Tiger': 'fossil form',
    'Longdan Tiger': 'extinct species (Panthera zdanskyi)', 'Ngandong Tiger': 'Pleistocene fossil subspecies',
    'Trinil Tiger': 'Pleistocene fossil subspecies', 'Wanhsien Tiger': 'Pleistocene fossil form',
    # leopards, cheetahs, jaguars and the other cats
    'Clouded Leopard': 'another genus (Neofelis)', 'Snow Leopard': 'another species (Panthera uncia)', 'European Ice Age Leopard': 'fossil form',
    'Clouded Leopardess': 'female clouded leopard, another genus', 'Snow Leopardess': 'female snow leopard, another species',
    'Sunda Clouded Leopard': 'separate species (Neofelis diardi)', 'American Cheetah': 'another genus (Miracinonyx)',
    'Giant Cheetah': 'extinct species (Acinonyx pardinensis)', 'European Jaguar': 'extinct species (Panthera gombaszoegensis)',
    'Pleistocene Jaguar': 'fossil form', 'Pleistocene North American Jaguar': 'fossil form', 'Pleistocene Cougar': 'fossil form',
    'Mountain Lioness': 'a female cougar', 'Sunda Leopard Cat': 'separate species since 2017 (Prionailurus javanensis)',
    'African Wildcat': "'Wildcat' spans two species since the 2017 split (Felis silvestris, F. lybica); left out, as in step 7",
    'Asiatic Wildcat': 'as African Wildcat', 'European Wildcat': 'as African Wildcat', 'Scottish Wildcat': 'as African Wildcat',
    # bears, canids
    'Steppe Brown Bear': 'Pleistocene form', 'Mexican Grizzly Bear': 'extinct (1960s)', 'Pleistocene Polar Bear': 'fossil form',
    'Pleistocene Coyote': 'fossil form', 'European Dhole': 'Pleistocene form',
    # deer, hippos, whales, others
    'European Elk': 'a moose', 'Irish Elk': 'extinct deer (Megaloceros)', 'European Hippopotamus': 'extinct species',
    'Pygmy Hippopotamus': 'another genus (Choeropsis)', 'Dwarf Sperm Whale': 'another genus (Kogia)', 'Pygmy Sperm Whale': 'another genus (Kogia)',
    'Asian Straight-tusked Elephant': 'another extinct species (Palaeoloxodon namadicus)', 'Giant Fossa': 'extinct species (Cryptoprocta spelea)',
    'Archaic Human': 'other Homo species', 'Australian Blacktip Shark': 'separate species (Carcharhinus tilstoni)',
    'Papuan Harpy Eagle': 'another genus (Harpyopsis)', 'Mertens\' Water Monitor': 'separate species (Varanus mertensi)',
    'West African Gaboon Viper': 'usually a separate species (Bitis rhinoceros)', 'Southern Mussurana': 'another Clelia species',
    "Hall's New Guinea Crocodile": 'separate species since 2019 (Crocodylus halli)', 'Papuan Olive Python': 'another genus (Apodora)',
    'Yellow Spotted False Monitor': 'another Callopistes species', 'Giant Water Bug': "'water bug' is a loose name for several families",
    # bracketed settings: the same animal in a stated setting, not a population
    'Bull Shark (in shallow water)': 'a setting, not a population', 'Salmon Shark (salmon/river battle)': 'a setting, not a population',
    'Yacare Caiman (on land)': 'a setting, not a population',
}
# ---- subspecies whose names do not contain the species' entry name: (child, parent, note) ----
CURATED = [
    ('Grizzly Bear', 'Brown Bear', 'Ursus arctos horribilis; keeps its own populations, so it is a category inside Brown Bear'),
    ('Kodiak Bear', 'Brown Bear', 'U. a. middendorffi'), ('Gobi Bear', 'Brown Bear', 'U. a. gobiensis'), ('Tibetan Blue Bear', 'Brown Bear', 'U. a. pruinosus'),
    ('Cinnamon Black Bear', 'American Black Bear', 'U. americanus cinnamomum'), ('Florida Black Bear', 'American Black Bear', 'U. a. floridanus'),
    ('Glacier Bear', 'American Black Bear', 'blue-grey morph, U. a. emmonsii'), ('Haida Gwaii Black Bear', 'American Black Bear', 'U. a. carlottae'),
    ('Kermode Bear', 'American Black Bear', 'U. a. kermodei'),
    ('Himalayan Black Bear', 'Asiatic Black Bear', 'U. thibetanus laniger'), ('Ussuri Black Bear', 'Asiatic Black Bear', 'U. t. ussuricus'),
    ('Alexander Archipelago Wolf', 'Grey Wolf', 'C. lupus ligoni'), ('Arabian Wolf', 'Grey Wolf', 'C. l. arabs'), ('Arctic Wolf', 'Grey Wolf', 'C. l. arctos'),
    ('Eurasian Wolf', 'Grey Wolf', 'C. l. lupus'), ('Iberian Wolf', 'Grey Wolf', 'C. l. signatus'), ('Indian Wolf', 'Grey Wolf', 'C. l. pallipes'),
    ('Italian Wolf', 'Grey Wolf', 'C. l. italicus'), ('Mackenzie Valley Wolf', 'Grey Wolf', 'C. l. occidentalis'), ('Mexican Wolf', 'Grey Wolf', 'C. l. baileyi'),
    ('Northwestern Wolf', 'Grey Wolf', 'C. l. occidentalis'), ('Steppe Wolf', 'Grey Wolf', 'C. l. campestris'), ('Tundra Wolf', 'Grey Wolf', 'C. l. albus'),
    ('Eastern Lowland Gorilla', 'Eastern Gorilla', 'Gorilla beringei graueri'), ('Mountain Gorilla', 'Eastern Gorilla', 'G. b. beringei'),
    ('Western Lowland Gorilla', 'Western Gorilla', 'G. gorilla gorilla'),
    ('Sumatran Elephant', 'Asian Elephant', 'Elephas maximus sumatranus'), ('Borneo Pygmy Elephant', 'Asian Elephant', 'E. m. borneensis'),
    ('Plains Bison', 'American Bison', 'Bison bison bison'), ('Wood Bison', 'American Bison', 'B. b. athabascae; step 7 pairs them too'),
    ('Florida Panther', 'Cougar', 'Puma concolor coryi'), ('Brazilian Puma', 'Cougar', 'a South American cougar population'),
    ('Bili Ape', 'Common Chimpanzee', 'a population of eastern chimpanzees'),
]
# ---- considered by hand and left unlinked: (child, parent, reason) ----
NOT_LINKED = [
    ('Himalayan Wolf', 'Grey Wolf', 'species status debated (Canis lupus chanco or C. himalayensis)'),
    ('Eastern Wolf', 'Grey Wolf', 'often treated as a separate species (Canis lycaon)'), ('Egyptian Wolf', 'Grey Wolf', 'an African golden wolf (Canis lupaster)'),
    ('Atlas Bear', 'Brown Bear', 'extinct (19th century)'),
    ('African Forest Buffalo', 'African (Cape) Buffalo', 'a subspecies under half the Cape buffalo\'s mass; the entry names the Cape form'),
]


def base_of(name, names):
    name = SPELLING.get(name, name); name = bt.ALIASES.get(name, name)
    return name if name in names else None


def taxon_candidates(names):
    out = {}
    for n in sorted(names):
        m = re.match(r'^(.*\S)\s*\(([^()]*)\)$', n)
        if m:                                                              # bracketed qualifier at the end
            if FIGHTER.search(m.group(2)): continue
            b = base_of(m.group(1), names)
            if b and b != n: out[n] = (b, 'bracket')
            continue
        w = n.split()
        for k in range(1, len(w)):                                         # longest proper word-suffix that is an entry
            s = ' '.join(w[k:])
            if s in names:
                if not FIGHTER.search(' '.join(w[:k])): out[n] = (s, 'name')
                break
    return out


def sex_links(names):
    out = {}
    for n in sorted(names):
        m = re.match(r'^(.*\S)\s*\(([^()]*)\)$', n)
        if m and m.group(2).strip().lower() in FEMALE | MALE:
            b = base_of(m.group(1), names)
            if b: out[n] = (b, 'female' if m.group(2).strip().lower() in FEMALE else 'male')
            continue
        w = n.split()
        if w and w[-1] in XESS:
            b = base_of(' '.join(w[:-1] + [XESS[w[-1]]]), names)
            if b: out[n] = (b, 'female')
            continue
        m = re.match(r'^(.*?)\b[Ss]he-(\w+)$', n)
        if m:
            b = base_of(m.group(1) + m.group(2).capitalize(), names)
            if b: out[n] = (b, 'female')
    return out


def build(path='duels.csv'):
    df, _ = bt.load(path); names = set(df.a) | set(df.b)
    real = df[(df.p >= bt.P_LO) & (df.p <= bt.P_HI)]; cnt = collections.Counter(list(real.a) + list(real.b))
    cand = taxon_candidates(names)
    unknown = [c for c in REJECT if c not in cand]
    assert not unknown, f'REJECT names that are not candidates: {unknown}'
    rows = [dict(child=c, parent=p, link='taxon', status='rejected' if c in REJECT else 'kept', how=how, note=REJECT.get(c, ''))
            for c, (p, how) in cand.items()]
    for c, p, note in CURATED:
        assert c in names and p in names, (c, p); assert c not in cand, f'{c} is already a candidate'
        rows.append(dict(child=c, parent=p, link='taxon', status='kept', how='curated', note=note))
    for c, p, note in NOT_LINKED:
        assert c in names and p in names, (c, p)
        rows.append(dict(child=c, parent=p, link='taxon', status='rejected', how='curated', note=note))
    for c, (b, kind) in sex_links(names).items():
        rows.append(dict(child=c, parent=b, link=kind, status='kept', how='sex form', note=''))
    kept = {r['child']: r['parent'] for r in rows if r['status'] == 'kept' and r['link'] == 'taxon'}
    for c in kept:                                                         # no cycles
        seen, x = {c}, kept[c]
        while x in kept: assert x not in seen, f'cycle at {c}'; seen.add(x); x = kept[x]
    root = lambda x: root(kept[x]) if x in kept else x
    for r in rows: r['root'] = root(r['child']) if r['link'] == 'taxon' and r['status'] == 'kept' else ''
    rows.sort(key=lambda r: (r['link'] != 'taxon', r['status'] != 'kept', r['root'] or r['parent'], r['parent'], r['child']))
    with open('category_graph.csv', 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=['child', 'parent', 'link', 'status', 'how', 'root', 'note']); w.writeheader(); w.writerows(rows)
    # readable view: each taxon tree, with the sex forms of its members
    kids = collections.defaultdict(list)
    for c, p in kept.items(): kids[p].append(c)
    sexf = collections.defaultdict(list)
    for r in rows:
        if r['link'] != 'taxon' and r['status'] == 'kept': sexf[r['parent']].append(f"{r['link']}: {r['child']} [{cnt[r['child']]}]")
    lines = ['Category graph: taxon trees (indented children), the sex forms of each member, [retained real matchups].', '']
    def show(n, depth):
        lines.append('    ' * depth + f'{n} [{cnt[n]}]' + (f"   ({'; '.join(sexf[n])})" if sexf[n] else ''))
        for c in sorted(kids[n]): show(c, depth + 1)
    roots = sorted({root(c) for c in kept})
    for r_ in roots: show(r_, 0); lines.append('')
    lines.append('Sex forms of animals outside the trees:')
    for b in sorted(sexf):
        if b not in kept and b not in kids: lines.append(f'{b} [{cnt[b]}]   ({"; ".join(sexf[b])})')
    open('category_graph.txt', 'w').write('\n'.join(lines) + '\n')
    nk = sum(1 for r in rows if r['status'] == 'kept' and r['link'] == 'taxon'); ns = sum(1 for r in rows if r['link'] != 'taxon')
    print(f'taxon links kept {nk} ({collections.Counter(r["how"] for r in rows if r["status"] == "kept" and r["link"] == "taxon")}) in {len(roots)} trees; '
          f'rejected {sum(1 for r in rows if r["status"] == "rejected")}; sex links {ns} '
          f'({collections.Counter(r["link"] for r in rows if r["link"] != "taxon")})')
    print('wrote category_graph.csv, category_graph.txt')
    return rows


if __name__ == '__main__':
    build(sys.argv[1] if len(sys.argv) > 1 else 'duels.csv')

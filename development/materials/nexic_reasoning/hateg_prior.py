#!/usr/bin/env python3
"""hateg_prior.py (version 4.4, R842, Oct 22 2026): the prior that no formidable theropod ever reached Hateg Island, on
the author's species draw, his definition of the formidable class, and his estimator: the Poisson probability of zero
formidable arrivals, with its confidence distribution from the herbivores' rate; and stage one of the Accordance
Principle on that prior, read on two percentiles (kappa's and the Hateg probability's) and as factors (the level at
which the principle carries the claim that the alternative was less productive of observers by at least a given
factor). Supplement to the long Nexic paper
(sec:hat, sec:hat-prior) and the Optimal Earth paper (sec:hateg-chain).  Run:  python3 hateg_prior.py    (standard
library only; deterministic; prints every figure the papers quote from it).

WHAT CHANGED FROM VERSION 3.1 (R816), AT THE AUTHOR'S DIRECTION (Oct 21 2026). The estimator. Version 3.1 averaged
the absence's probability exp(-mu_T) over a scale-invariant prior on the rate, which gave (1 - f)^k = (34/48)^8 =
0.0634 on the main reading; it is superseded. In the author's words (quoted in ASCII; verbatim in the long paper's
chain, fn:hateg-chain): "the probability of no theropods on Hateg island is best calculated by simply the probability
of zero arrivals under the Poisson distribution given by hazard/time rate for theropods given by (herbivore
rate)*(f/(1-f)) where f is the fraction of possible options for each colonization event which are formidable theropod
clades (roughly approximated as the species proportion), and then we explicitly note that we have a confidence
interval on the herbivore rate given the 8 herbivore arrivals in the time interval of Hateg island's existence, which
in turn contributes to the confidence interval of the total no-formidable-theropods-probability" (the "*" his
correction of a "/" in the original message); "I'm concerned that 8 isn't the true genuine herbivore hazard rate -
only our sample estimate of the true hazard rate! So THAT is what I think should be driving the confidence bounds,
no?"; "maybe I would consider referring to the median of the total confidence range rather than subbing 8 for the
'central tendency probability' that gets fed into the accordance principle ... Also please give a few bounds as well,
like the 90th and the 75th, so we can get a feel for the actual continuous spread of it"; "the kappas come with their
own quantiles giving kappa"; "set up the table to have the kappa percentile as one column, and the actual Hateg
probability percentile as another column, and then we get the canonical ratio and linkage bounds from there"; and "one
version still which gives us the joint percentile for the probability that the canonical ratio upper bound is below
different given values ... the probability that formidable theropods arriving drops the probability for humans by at
least some coefficient". The canonical ratio is his name for P(H|A')/P(H|A). The census (the pool, the
arrivals, the class, the bet) is unchanged from version 3.1. Every variant is recomputed on the new estimator, at the
median: the uniform-prior variant, which has no counterpart without a prior, is dropped; the repeats variant takes the
median of the occupancy model's confidence distribution; the absence-as-data variant takes the total rate from all k
arrivals, giving exp(-mu f).

THE MODEL. An overall arrival process with rate Lambda(t) = c * g(t) runs while the island exists. Each firing draws
one species uniformly from the pool S(t) of species then living in the archipelago outside the island, so species s
arrives at rate Lambda(t)/N(t) while it lives. With s_f(t) the formidable share of the pool,
    non-formidable arrivals K ~ Poisson(mu_H),  mu_H = c * F_n,  F_n = int g(t) (1 - s_f(t)) dt,
    formidable arrivals       ~ Poisson(mu_T),  mu_T = c * F_f,  F_f = int g(t) s_f(t) dt,
independent of each other (Poisson thinning), so that mu_T = mu_H * F_f/F_n; with a steady composition, s_f(t) = f,
mu_T = mu_H * f/(1 - f), the herbivores' expected number times the odds of a formidable draw, the shape g dropping out.
The absence is the Poisson zero term,
    P0 = exp(-mu_T) = exp(-mu_H * f/(1 - f)).
mu_H is estimated from k, the arrivals seen, all non-formidable. k is a sample of mu_H, not mu_H itself, so mu_H has
a confidence distribution, and P0 with it. For a count the exact (Garwood) construction gives two, C_lo(mu) =
P(K >= k | mu) for lower bounds and C_hi(mu) = P(K > k | mu) for upper bounds (the exact interval at level 1 - alpha is
[C_lo^-1(alpha/2), C_hi^-1(1 - alpha/2)] = [chi2(alpha/2; 2k)/2, chi2(1 - alpha/2; 2k + 2)/2], whose coverage is
guaranteed); their average is the mid-p confidence distribution,
    C(mu) = P(K > k | mu) + P(K = k | mu)/2,
a single continuous distribution, whose coverage is approximate. The central value fed into the accordance numbers is
its median mu_med, which solves C = 1/2 and is median-unbiased; the spread is its percentiles. P0 falls steadily as
mu_H rises, so the median of P0 is P0 at mu_med, and P0's q-th percentile is P0 at mu_H's (1-q)-th: no mean is taken,
so nothing is pulled by the long upper tail. The plug-in value at mu_H = k (the maximum-likelihood estimate) and the
exact intervals are printed for comparison. The census's own judgements (f and k) are not in this spread; section 2
prints them as variants.

STAGE ONE (sections 5-9). The Accordance Principle bounds the canonical ratio P(H|A')/P(H|A) by kappa times the prior
odds except on probability at most 1/(1+kappa), so kappa is a percentile of the realization, kappa_beta = beta/(1-beta);
the principle licenses kappa >= 1, at kappa = 1 in strict form (the draw is postulated in its lower tail), so the scale
begins at the 50th percentile. On the absence the prior has its own percentile, from the confidence distribution, and
the bound is read on the two together: at (beta, gamma) the canonical ratio is at most kappa_beta times the odds of P0
at its gamma-th percentile, and the linkage at least (1 - r)/(1 + r) (sections 6-7). Read as factors (section 8), the
principle carries the claim that the canonical ratio is at most 1/N, for N fixed in advance, at the level kappa/(1+kappa)
at the kappa that puts the bound at 1/N, with no credit where that kappa falls below one, a level valid however it
depends on the realized prior (the long paper's Lemma, the level reading); averaged over the confidence distribution
it is a confidence-weighted level, not a guarantee at the unknown prior. CANONICAL QUANTILES (section 9; the author,
Oct 22 2026: "those probabilities themselves ARE actually most intuitively my view for the 'canonical quantiles'", and
"I think of canonical quantiles as monotonically decreasing with canonical ratio, that way 0.99 canonical quantile gives
our own scenario's observer probability 'more significance'"): the same levels read the other way, on one uniformly
spaced scale. With kappa_q = max(1, q/(1-q)), U uniform on (0,1) and the prior P drawn from its confidence distribution
independently of U, the canonical variable V = kappa_U * odds(P) is the principle's bound read at a random percentile
of the realization. The canonical quantile of a value c is Pr[V > c], one minus section 8's averaged level; the
canonical ratio at canonical quantile q is the (1 - q)-quantile of V, so it falls as q rises, and the claim that the
canonical ratio is at most that value is carried at level 1 - q. Computed by integrating the level against the
confidence distribution's density, the equal mixture of the Gamma(k) and Gamma(k+1) densities (Gauss-Legendre, from
the point where the credit begins), and inverting by bisection; bounds are printed rounded up (a cut 1/N with N
rounded down, a bound above one rounded up, to three significant figures). For a prior that is a point (the
configuration) the canonical ratio at canonical quantile q is kappa_(1-q) times its odds, and above q = 1/2 it stays at
the median's. Version 4.4 (R842, the author, Oct 22 2026: "my instinct is to have spacing at every 0.05 for the
canonical quantiles, (and maybe write them as percentiles for visual ease), and then also include 0.99 and 0.01 for
symmetry") writes the canonical quantiles as percentages, every 5% from 5% to 95% with 1% and 99%. What the levels
are: like the level reading's, each is a level over the realization of a declared attribute, jointly with the prior
realized, and not a level conditional on that prior (at independence, a declared side of prior 0.035 has canonical
ratio one on either side, and the median bound at its odds, carried at level 1/2 whenever that side realizes, fails
every time it does; the level allows it, since it happens with probability 0.035); averaged over the confidence
distribution, a weighted calibration index of this construction, not a posterior probability (which would need a
joint model of the prior and the realization) and not a coverage guarantee (which would need a repeated-sampling
argument); and V is an envelope, the principle's bound read at a random percentile, not the canonical ratio's
distribution (on a two-cell draw the accordance ratio has mean one, kappa_U an infinite mean). The confidence
distribution's coverage is approximate (mid-p; the exact Garwood interval is printed beside it), and every interval is
conditional on the model, the census and the classification of the island's theropods. The absence is not used as data
(it is the attribute being priced), and by thinning the author's conditioning on it leaves the others' likelihood
unchanged. Repeats: the author takes two arrivals of one species to be rare (true if the real pool is several times
the census) and arrivals of one clade's different species to be told apart by the fossils, so k counts the lineages
the island's fossils distinguish; section 2 prints the occupancy-corrected figure for a pool no larger than the
census.

THE ISLAND'S THEROPOD RECORD, AND THE AUTHOR'S BET. Under the author's definition A (no formidable theropod on the
island over its documented interval) holds only if each of the island's theropod records belongs to a lineage with a
detour. The author bets that they will prove avian. The records, each with its readings (latest last):
  isolated teeth referred to velociraptorine dromaeosaurids (Csiki & Grigorescu 1998; Smith et al. 2002), with the
    describers' caution that isolated teeth give "a greater apparent than real diversity";
  "troodontid-like" teeth, "probably more closely related to troodontids" (Csiki & Grigorescu 1998);
  teeth of the Richardoestesia and Paronychodon kinds, lineage undetermined (Malafaia et al. 2023);
  a Maastrichtian tooth from the NVS site near Valioara, Paraves indet. 1 (Osi, Kollati & Nagy 2025);
  the Elopteryx femora: a bird (Andrews), most probably a dromaeosaurid (Le Loeuff et al. 1992, as reported by Kessler
    et al. 2005), "a derived maniraptoran" (Csiki & Grigorescu 1998), a eumaniraptoran, possibly a troodontid or a
    pygostylian bird (Naish & Dyke 2004), most probably a derived maniraptoran reminiscent of the alvarezsaurids
    (Kessler et al. 2005, from a femur referred tentatively), possibly one clade with Balaur and Gargantuavis (Mayr et
    al. 2020), a paravian and avialan, "a secondarily flightless bird" (Stoicescu et al. 2024);
  the tibiotarsi: first referred to Elopteryx; giant owls, Bradycneme and Heptasteornis (Harrison & Walker 1975);
    troodontids in parts (several authors, 1985-1993, "little supporting evidence", per Kessler et al. 2005), a
    referral Selles et al. 2021 report later work to have ruled out; a non-maniraptoran tetanuran (Csiki & Grigorescu
    1998); Heptasteornis an alvarezsaurid and Bradycneme an indeterminate maniraptoran (Naish & Dyke 2004); Bradycneme a
    junior synonym of Elopteryx, Heptasteornis an alvarezsaurid (Stoicescu et al. 2024);
  FGGUB R.351, once referred to Elopteryx as a distal femur: "may represent a small abelisaurid", "if not avialian"
    (Csiki & Grigorescu 1998); since identified as "the distal end of a moderately large metatarsal, belonging probably
    to a hadrosaur" (Kessler, Grigorescu & Csiki 2005), so no longer a theropod record on its describers' latest reading;
  Balaur: a dromaeosaurid (Csiki et al. 2010; Brusatte et al. 2013), an avialan (Cau et al. 2015), possibly a junior
    synonym of Elopteryx (Mayr et al. 2020; "very possible", Stoicescu et al. 2024);
  the Nalat-Vad middle-sized vertebra (Smith et al. 2002), a "possible medium-sized taxon" (CS15), and an
    "indeterminate medium-sized taxon" in a later review (Malafaia et al. 2023), perhaps the same.
The prior computed here is the prior of A as the author's bet reads the record: all these fossils, Heptasteornis
included, are counted as flying lineages, not as arrivals. On its latest readings Heptasteornis is an alvarezsaurid, a
non-volant, non-formidable arrival, and k is then 9 (printed below). The author counts a middle-sized theropod "of a
dromeosaur or something" as formidable; extending his bet to the Nalat-Vad vertebra is this estimate's assumption, not
his.

THE ISLAND'S ARRIVALS, k (non-volant dinosaurs of any size, giant flightless birds included; flying lineages excluded,
as the author directs). Titanosaurs, three lineages (Diez Diaz et al. 2025); Struthiosaurus (CS15); the telmatosaurids,
Telmatosaurus with Kryptohadros (Magyar et al. 2026); Transylvanosaurus (Augustin et al. 2022); Ferenceratops with
Zalmoxes robustus (Maidment et al. 2026); Gargantuavis (Mayr et al. 2020; disputed by Buffetaut & Angst 2020).
k = 8; 6 by class; 7 if Gargantuavis flew in; 9 with Zalmoxes robustus apart (as an iguanodontian) or with
Heptasteornis as an alvarezsaurid (a non-volant, non-formidable arrival); 11 with Uriash and Kryptohadros apart too.

THE POOL, f (dinosaurs outside the Transylvanian landmass, giant flightless birds included, Santonian to the end of the
island's record, about 67.0 Ma; any size; body fossils only). Two counts, applied to both sides:
  NAMED: named species (valid; a variant adds the contested Tarascosaurus and Craspedodon). Contested: names whose
    validity is disputed in the literature (with Betasuchus and Orthomerus in the refuge's bin); nomina dubia without such
    a dispute (Hypselosaurus, Rhodanosaurus) are left out of the named count, and in the forms count their cells are
    already occupied.
  FORMS: named species, plus one form for each cell of clade x stage x island that only indeterminate records occupy,
    plus indeterminate records that their describers distinguish from the named species of their cell. Contested names
    count unless they may be synonyms of a named species in their cell (Variraptor of Pyroraptor). Every record is
    counted by its describers' latest reading, as the reading it is.
  Stages: Santonian 86.3-83.6; early Campanian (C33r) 83.6-79.9; middle-late Campanian 79.9-72.1; early Maastrichtian
  (to the top of C31r) 72.1-69.3; late Maastrichtian to the island's record end 69.3-67.0; after the record 67.0-66.0.
  Records dated only to upper C30n or to the late Maastrichtian straddle the last two. Islands: IA Ibero-Armorica,
  AA Austroalpine, AD Adria, NE the northern islands (Belgium, the Netherlands), CR Crimea, BG the Balkan (Moesian)
  margin. Sources: CS15 (Csiki-Sava et al. 2015, ZooKeys 469); Fondevilla et al. 2019 (Earth-Sci. Rev. 191: 168-189);
  Malafaia et al. 2023 (Diversity 15: 141); Osi et al. 2010; Osi & Buffetaut 2011; Osi & Prondvai 2013; Tortosa et al.
  2014; Maidment et al. 2026; Selles et al. 2021 (Sci. Rep. 11: 4855); Osi, Kollati & Nagy 2025 (Palaeobiodiv.
  Palaeoenv. 105: 499-515); Debeljak, Kosir, Buffetaut & Otonicar 2002 (Mem. Soc. Geol. It. 57: 193-201; title only);
  the species' descriptions as listed.

THE RATE'S WINDOW. The herbivores' rate is estimated over the window from the island's emergence (93.9 Ma) to the
end of its record (67.0 Ma), 26.9 Myr. The window's length cancels in P0 and sets only the rates per Myr; the
stage-by-stage variant weights the shares over the stages with data (86.3-67.0 Ma).

THE REFUGE'S HORIZON. k and A's prior run to the record's end (67.0 Ma); the refuge needed the absence to last to the
boundary, so its price adds the predators' exposure from 67.0 to 66.0 Ma: their expected number, at the median rate
and at each percentile, is scaled by (93.9 - 66.0)/(93.9 - 67.0) = 27.9/26.9.

THE JOINT. P(refuge) = P_LC * P0, with P_LC from the companion's surrogate test (sea_levels): 67/5000 at the window's
exact extremes, 89/2000 at the canonical tolerance, about 0.11 on the least favourable separating settings.

THE PREMISE CHECK. Of the islands in the R813 compilation that received four or more large herbivore lineages, how many
never received a terrestrial predator.


FOR THE AUTHOR (pending). The objections paragraph says "flighted ancestry is precisely what makes the colonization of
an island feasible", while the premise has eight non-volant arrivals; and it places the island's small theropods outside
the class as maniraptorans whose ancestry plausibly passed through a volant stage, which would place the dromaeosaurids
and troodontids he now counts outside it too. Ornithomimosaurs are counted as non-formidable here; the author has not
ruled on them. Whether the bet covers the middle-sized vertebra. Kozina's age is the review's placement; its primary
descriptions were not read. His single example's 6% ((1/2)^4, the negative-binomial count of four herbivore
colonizations against none carnivorous, in his section on the island) is the probability that none of a fixed number of
draws is a carnivore; on the Poisson zero-arrival estimator, four herbivore arrivals and f = 1/2 give exp(-4) = 0.018
at the count itself and 0.015 at the median (printed in section 2). The papers keep his 6% as his single example.
"""
import math

T0, T_REC, T_BND = 93.9, 67.0, 66.0     # window start (island emergent from the Cenomanian top), record end, boundary

BINS = {"S": (86.3, 83.6), "eC": (83.6, 79.9), "mlC": (79.9, 72.1), "eM": (72.1, 69.3), "lM": (69.3, 67.0),
        "tM": (67.0, 66.0)}
REC_BINS = ["S", "eC", "mlC", "eM", "lM"]

# (label, side F/N, status: 'valid' | 'contested' | 'form', island, bins, note, source)
POOL = [
    # ---------------- formidable: theropods of lineages without a volant, aquatic or alvarezsaurid detour, any size
    #                  (the author's definition, Oct 14 2026); ornithomimosaurs outside, pending his ruling
    ("Iharkut early-branching tetanuran", "F", "form", "AA", ["S"],
     "medium-sized; the top predators of Iharkut", "Osi et al. 2010; CS15 pp. 35, 39; Malafaia et al. 2023"),
    ("Iharkut abelisaurid", "F", "form", "AA", ["S"],
     "about 1.8 m, 'relatively small'; femur and ungual", "Osi & Buffetaut 2011"),
    ("Pneumatoraptor fodori", "F", "valid", "AA", ["S"],
     "a paravian, 'possibly' a dromaeosaurid on its describers' reading; formidable unless an avialan",
     "Osi, Apesteguia & Kowalewski 2010"),
    ("Muthmannsdorf tetanuran ('Megalosaurus' pannoniensis, nomen dubium)", "F", "form", "AA", ["eC"],
     "two teeth compared with Iharkut's early-branching tetanurans", "Malafaia et al. 2023; CS15"),
    ("Tarascosaurus salluvicus", "F", "contested", "IA", ["eC"],
     "abelisaurid, about 3 m (3-4 m); validity disputed", "Le Loeuff & Buffetaut 1991; Osi & Buffetaut 2011; Tortosa et al. 2014"),
    ("Arcovenator escotae", "F", "valid", "IA", ["mlC"],
     "majungasaurine abelisaurid, 5-6 m; cf. Arcovenator at Lano, Armuna, Chera, Poyos", "Tortosa et al. 2014; Fondevilla et al. 2019"),
    ("Pyroraptor olympius", "F", "valid", "IA", ["mlC", "eM"],
     "read as a dromaeosaurid (or an unenlagiine); teeth referred to it at Montrebei, middle C31r; remains at Lo Hueco "
     "referred to a small eudromaeosaurian, Variraptor (a possible synonym) and the tentatively dromaeosaurid material of "
     "Taveiro share its cell", "Allain & Taquet 2000; Fondevilla et al. 2019; Malafaia et al. 2023"),
    ("Taveiro troodontid material", "F", "form", "IA", ["mlC", "eM"],
     "'tentatively attributed to troodontids'; the Taveiro fauna, Campanian-early Maastrichtian; Iberian troodontids "
     "marked '?' in CS15's Table 1", "Malafaia et al. 2023; CS15"),
    ("Lo Hueco medium-sized abelisauroid", "F", "form", "IA", ["mlC", "eM"],
     "late Campanian-Maastrichtian; the only abelisauroid record overlapping the early Maastrichtian", "Malafaia et al. 2023"),
    ("Iberian large tetanuran teeth (aff. Megalosauridae, Taveiro; M. cf. pannoniensis, Viso)", "F", "form", "IA",
     ["mlC", "eM"], "large-sized crowns; Campanian-early Maastrichtian", "Malafaia et al. 2023"),
    ("late-Maastrichtian abelisaurids (Vitrolles-La-Plaine; South Pyrenees; cf. Arcovenator, Blasi, upper C30n, and "
     "Moli del Baro-1 and 172-i/04e, lower C29r)", "F", "form", "IA", ["lM", "tM"],
     "medium-sized; medium to large crowns; the C29r teeth share the cell in the refuge's bin",
     "Malafaia et al. 2023; Fondevilla et al. 2019"),
    ("late-Maastrichtian dromaeosaurid teeth (Peguera-1; Blasi, upper C30n; Moli del Baro-1, C29r)", "F", "form", "IA",
     ["lM", "tM"], "teeth referred to Dromaeosauridae", "Fondevilla et al. 2019"),
    ("Kozina dromaeosaurid teeth", "F", "form", "AD", ["lM", "tM"],
     "teeth assigned to indeterminate dromaeosaurids; Adriatic-Dinaric platform; late Maastrichtian on the review's "
     "placement (primary descriptions not read)", "Malafaia et al. 2023; Debeljak et al. 2002"),
    ("Kozina troodontid-like teeth", "F", "form", "AD", ["lM", "tM"],
     "a 'troodontid-like morphotype'; same site and placement; described less firmly than the island's 'probably more "
     "closely related to troodontids' (the variant leaving out the tentative troodontid forms is printed)",
     "Malafaia et al. 2023"),
    ("Tamarro insperatus", "F", "valid", "IA", ["tM"], "troodontid, C29r; after the island's record", "Selles et al. 2021"),
    ("Betasuchus bredai", "F", "contested", "NE", ["tM"], "ceratosaur; Maastricht Formation; often a nomen dubium",
     "CS15"),
    # ---------------- non-formidable dinosaurs of any size, giant flightless birds included
    ("Atsinganosaurus velauciensis", "N", "valid", "IA", ["mlC"], "titanosaur", "Garcia et al. 2010; Diez Diaz et al. 2021"),
    ("Garrigatitan meridionalis", "N", "valid", "IA", ["mlC"], "titanosaur", "Diez Diaz et al. 2021"),
    ("Lirainosaurus astibiae", "N", "valid", "IA", ["mlC"], "titanosaur, C32n.2n", "Sanz et al. 1999; Fondevilla et al. 2019"),
    ("Lohuecotitan pandafilandi", "N", "valid", "IA", ["mlC", "eM"], "titanosaur", "Diez Diaz et al. 2016"),
    ("Qunkasaura pintiquiniestra", "N", "valid", "IA", ["mlC", "eM"], "titanosaur", "Mocho et al. 2024"),
    ("Ampelosaurus atacis", "N", "valid", "IA", ["eM"], "titanosaur", "Le Loeuff 1995"),
    ("Abditosaurus kuehnei", "N", "valid", "IA", ["eM"], "titanosaur, about 70.5 Ma", "Vila et al. 2022"),
    ("late-Maastrichtian titanosaurs of the Tremp Basin (Serraduy, Moli del Baro-2)", "N", "form", "IA", ["lM", "tM"],
     "C30n-C29r", "Fondevilla et al. 2019"),
    ("Hungarosaurus tormai", "N", "valid", "AA", ["S"], "nodosaurid, 4-4.5 m", "Osi 2005; Osi & Prondvai 2013"),
    ("Iharkut second nodosaurid (cf. Struthiosaurus)", "N", "form", "AA", ["S"],
     "2-2.5 m; distinguished from Hungarosaurus by its describers", "Osi & Prondvai 2013"),
    ("Struthiosaurus austriacus", "N", "valid", "AA", ["eC"], "nodosaurid, about 2.7 m", "Bunzel 1871; CS15"),
    ("Struthiosaurus languedocensis", "N", "valid", "IA", ["eC"], "nodosaurid, C33r", "Garcia & Pereda-Suberbiola 2003"),
    ("Struthiosaurus sp., Lano", "N", "form", "IA", ["mlC"], "C32n.2n", "Fondevilla et al. 2019"),
    ("Nodosauridae indet., Els Nerets", "N", "form", "IA", ["eM"], "middle C31r", "Fondevilla et al. 2019"),
    ("ankylosaurians, Fontllonga-6 and Lestaillats", "N", "form", "IA", ["lM"], "C31n-C30r", "Fondevilla et al. 2019"),
    ("Mochlodon suessi", "N", "valid", "AA", ["eC"], "rhabdodontid, 1.6-1.8 m", "Bunzel 1871; Osi et al. 2012"),
    ("Rhabdodontidae indet., Villeveyrac", "N", "form", "IA", ["eC"], "C33r", "Fondevilla et al. 2019"),
    ("Obelignathus septimanicus", "N", "valid", "IA", ["mlC", "eM"], "rhabdodontid; formerly Rhabdodon septimanicus",
     "Czepinski & Madzia 2025"),
    ("Matheronodon provincialis", "N", "valid", "IA", ["mlC"], "rhabdodontid, about 5 m", "Godefroit et al. 2017"),
    ("Rhabdodon priscus", "N", "valid", "IA", ["eM"], "rhabdodontid, 5-6 m", "Matheron 1869; Osi et al. 2012"),
    ("Pareisactus evrostos", "N", "valid", "IA", ["eM"], "rhabdodontid, middle-upper C31r", "Parraga & Prieto-Marquez 2019"),
    ("Ajkaceratops kozmai", "N", "valid", "AA", ["S"], "ceratopsian (with 'Mochlodon vorosi'), small",
     "Osi et al. 2010; Maidment et al. 2026"),
    ("Craspedodon lonzeensis", "N", "contested", "NE", ["S"], "?neoceratopsian or hadrosauroid; possibly a nomen dubium",
     "Godefroit & Lambert 2007; CS15"),
    ("Riabininohadros weberae", "N", "valid", "CR", ["eM", "lM"], "styracostern, small; Maastrichtian",
     "Lopatin & Averianov 2020; CS15"),
    ("Tethyshadros insularis", "N", "valid", "AD", ["eC"], "hadrosauroid, about 81.5-80.5 Ma", "Dalla Vecchia 2009; Chiarenza et al. 2021"),
    ("Kozina hadrosaur", "N", "form", "AD", ["lM", "tM"],
     "hadrosaur remains; the Kozina site's placement as above (Debeljak et al. not read; the hadrosaur from the "
     "Slovenian Press Agency's account of the finds)", "Debeljak et al. 1999, 2002"),
    ("Hadrosauridae indet., Lano", "N", "form", "IA", ["mlC"], "C32n.2n", "Fondevilla et al. 2019"),
    ("non-euhadrosaurian hadrosaurid, Vitrolles-La-Plaine (with Hadrosauridae indet., La Solana)", "N", "form", "IA",
     ["lM"], "late Maastrichtian; distinguished from the lambeosaurines as non-euhadrosaurian",
     "Fondevilla et al. 2019; Malafaia et al. 2023"),
    ("Adynomosaurus arcanus", "N", "valid", "IA", ["eM"], "lambeosaurine, about 70 Ma", "Prieto-Marquez et al. 2019"),
    ("Blasisaurus canudoi", "N", "valid", "IA", ["lM", "tM"], "lambeosaurine, upper C30n", "Cruzado-Caballero et al. 2010"),
    ("Canardia garonnensis", "N", "valid", "IA", ["lM", "tM"], "lambeosaurine, late Maastrichtian", "Prieto-Marquez et al. 2013"),
    ("?Ornithomimosauria, Lano", "N", "form", "IA", ["mlC"], "an ungual; non-formidable by diet", "Isasmendi et al. 2022"),
    ("?Ornithomimosauria, Vratsa", "N", "form", "BG", ["lM", "tM"], "a humerus, Kajlaka Formation", "CS15; Malafaia et al. 2023"),
    ("Gargantuavis philoinos", "N", "valid", "IA", ["mlC", "eM"], "giant flightless bird, 57-75 kg",
     "Buffetaut & Le Loeuff 1998; Buffetaut & Angst 2019"),
    # after the island's record only (the refuge's bin)
    ("Pararhabdodon isonensis", "N", "valid", "IA", ["tM"], "lambeosaurine, C29r", "Casanovas-Cladellas et al. 1993"),
    ("Arenysaurus ardevoli", "N", "valid", "IA", ["tM"], "lambeosaurine", "Pereda-Suberbiola et al. 2009"),
    ("Fylax thyrakolasus", "N", "valid", "IA", ["tM"], "hadrosauroid, C29r", "Prieto-Marquez & Carrera Farias 2021"),
    ("Calvarius rapidus", "N", "valid", "IA", ["tM"], "small styracostern, latest Maastrichtian", "Prieto-Marquez & Selles 2023"),
    ("Beranuy giant ornithuromorph", "N", "form", "IA", ["tM"], "C29r; distinct from Gargantuavis", "Perez-Pueyo et al. 2021"),
    ("Orthomerus dolloi", "N", "contested", "NE", ["tM"], "hadrosaurid; Maastricht Formation; often a nomen dubium; "
     "counted as Betasuchus is", "CS15"),
]
VARIANT_VARIRAPTOR = ("Variraptor mechinorum", "F", "contested", "IA", ["mlC", "eM"],
                      "?dromaeosaurid; nomen dubium or a synonym of Pyroraptor", "Le Loeuff & Buffetaut 1998")
EXCLUDED = ["Variraptor (a possible synonym of Pyroraptor, in its cell; a variant counts it)",
            "Richardoestesia, Paronychodon (whose troodontid attribution Torices et al. 2015 question, per Selles et al. "
            "2021) and other tooth morphotypes of undetermined clade, on both sides",
            "teeth referred only to Paraves indet. (Iharkut's Paraves indet. 1, Lano; the island's NVS tooth), "
            "undetermined between the formidable lineages and the birds, on both sides",
            "Hypselosaurus, Rhodanosaurus (nomina dubia in cells already occupied)",
            "La Boucharde abelisaurid tibia (middle Campanian: the cell Arcovenator occupies)",
            "ichnofossils on both sides"]

P_LC = [("exact extremes, 67/5000", 67 / 5000), ("canonical tolerance, 89/2000", 89 / 2000),
        ("least favourable separating settings, 218/2000", 0.109)]

ISLANDS = [("Crete", 4, 0), ("Cyprus", 2, 0), ("Sicily-Malta", 2, 0), ("Sardinia-Corsica", 4, 2), ("Balearics", 2, 0),
           ("Tilos", 1, 0), ("Gargano", 1, 0), ("Tusco-Sardinian palaeo-islands", 4, 0), ("Flores", 3, 1),
           ("Sumba", 1, 1), ("Timor", 2, 1), ("Sulawesi", 8, 0), ("Luzon", 7, 0), ("Mindanao", 3, 0), ("Cuba", 2, 1),
           ("Hispaniola", 2, 1), ("Jamaica", 1, 0), ("Puerto Rico", 2, 0), ("Bahamas", 1, 1), ("Madagascar", 5, 1),
           ("New Zealand", 1, 1), ("New Caledonia", 2, 1), ("Viti Levu", 1, 1), ("Mauritius", 1, 0),
           ("Galapagos", 1, 0), ("Santarosae", 1, 0), ("Canary Islands", 1, 0)]

K_LINEAGE, K_CLASS, K_PLUS1, K_MAX, K_NO_GARGANTUAVIS = 8, 6, 9, 11, 7


PCTS = (0.025, 0.05, 0.10, 0.125, 0.25, 0.5, 0.75, 0.875, 0.90, 0.95, 0.975)   # percentiles of P0 printed
LEVELS = (0.50, 0.75, 0.90, 0.95)                                               # central intervals printed
KAP_PCTS = (0.5, 0.75, 0.8, 0.9, 0.95)        # kappa's percentiles (the principle's scale; licensed from the 50th)
HAT_PCTS = (0.10, 0.25, 0.5, 0.75, 0.90)      # the Hateg probability's percentiles (its confidence distribution)


def admitted(rec, count, contested):
    status = rec[2]
    if count == "forms":
        return status in ("valid", "contested", "form")
    return status == "valid" or (contested and status == "contested")


def pooled(pool, count, contested=True, bins=REC_BINS):
    nf = sum(1 for r in pool if r[1] == "F" and admitted(r, count, contested) and set(r[4]) & set(bins))
    nn = sum(1 for r in pool if r[1] == "N" and admitted(r, count, contested) and set(r[4]) & set(bins))
    return nf, nn


def resolved(pool, count, contested=True, bins=REC_BINS, g=lambda b: 1.0):
    """F_f, F_n from the stage-by-stage composition, Lambda(t) = c g(t) with g constant within a stage."""
    Ff = Fn = 0.0
    for b in bins:
        nf = sum(1 for r in pool if r[1] == "F" and admitted(r, count, contested) and b in r[4])
        nn = sum(1 for r in pool if r[1] == "N" and admitted(r, count, contested) and b in r[4])
        if nf + nn == 0:
            continue
        dt = BINS[b][0] - BINS[b][1]
        Ff += g(b) * dt * nf / (nf + nn)
        Fn += g(b) * dt * nn / (nf + nn)
    return Ff, Fn


def pois_pmf(n, mu):
    return math.exp(-mu + n * math.log(mu) - math.lgamma(n + 1))


def pois_cdf(n, mu):
    """P(K <= n) for K ~ Poisson(mu)."""
    if n < 0:
        return 0.0
    term = math.exp(-mu)
    total = term
    for i in range(1, n + 1):
        term *= mu / i
        total += term
    return total


def solve_increasing(fun, target, lo, hi):
    """The x in [lo, hi] at which the increasing function fun reaches target (bisection)."""
    for _ in range(300):
        mid = 0.5 * (lo + hi)
        if fun(mid) < target:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def garwood(k, conf=0.95):
    """The exact (Garwood) two-sided interval for a Poisson mean given k: mu_L solves P(K >= k | mu_L) = alpha/2
    (0 if k = 0), mu_U solves P(K > k | mu_U) = 1 - alpha/2, i.e. P(K <= k | mu_U) = alpha/2; equivalently
    chi2(alpha/2; 2k)/2 and chi2(1 - alpha/2; 2k + 2)/2."""
    a = 1.0 - conf
    top = 10.0 * k + 60.0
    lo = 0.0 if k == 0 else solve_increasing(lambda m: 1.0 - pois_cdf(k - 1, m), a / 2, 1e-12, top)
    hi = solve_increasing(lambda m: 1.0 - pois_cdf(k, m), 1.0 - a / 2, 1e-12, top)
    return lo, hi


def midp_cd(mu, k):
    """The mid-p confidence distribution of a Poisson mean given k: P(K > k | mu) + P(K = k | mu)/2, the average of
    the exact construction's two, P(K >= k | mu) and P(K > k | mu); increasing in mu."""
    return (1.0 - pois_cdf(k, mu)) + 0.5 * pois_pmf(k, mu)


def mu_q(q, k):
    """The q-th percentile of mu_H's mid-p confidence distribution."""
    return solve_increasing(lambda m: midp_cd(m, k), q, 1e-12, 10.0 * k + 60.0)


def mu_med(k):
    return mu_q(0.5, k)


U_GRID = 4000                                   # midpoints of the confidence distribution's quantile scale
_MU_CACHE = {}


def mu_grid(k):
    """mu_H at the midpoints of its mid-p confidence distribution, u = (i + 1/2)/U_GRID: a sample of the distribution
    by its quantiles, for averaging over it."""
    if k not in _MU_CACHE:
        _MU_CACHE[k] = [mu_q((i + 0.5) / U_GRID, k) for i in range(U_GRID)]
    return _MU_CACHE[k]


def kappa_cdf(t):
    """The principle's guarantee on its percentile scale: Pr[kappa-scale <= t] >= t/(1+t) for t >= 1 (kappa = 1 in
    strict form); below the median it licenses nothing, so no credit is taken there."""
    return t / (1.0 + t) if t >= 1.0 else 0.0


def prob_factor(n_fold, odds_of_mu, k):
    """The level at which the principle carries the claim that the canonical ratio is at most 1/n_fold, i.e. that the
    alternative is less productive of observers by at least n_fold times: kappa_cdf((1/n_fold)/odds), the level at the
    kappa that puts the bound at 1/n_fold (valid however it depends on the realized prior, by the level reading),
    averaged over the prior's confidence distribution: a confidence-weighted level, not a guarantee at the prior."""
    c = 1.0 / n_fold
    g = mu_grid(k)
    return sum(kappa_cdf(c / odds_of_mu(m)) for m in g) / len(g)


def cd_density(mu, k):
    """The density of mu_H's mid-p confidence distribution. P(K > k | mu) + P(K = k | mu)/2 is the average of
    P(K >= k | mu) and P(K >= k + 1 | mu), which are the Gamma(k) and Gamma(k + 1) distribution functions at mu, so the
    density is the average of the two Gamma densities."""
    if mu <= 0.0:
        return 0.0
    lm = math.log(mu)
    return 0.5 * (math.exp((k - 1) * lm - mu - math.lgamma(k)) + math.exp(k * lm - mu - math.lgamma(k + 1)))


def gauss_legendre(n):
    """Nodes and weights of n-point Gauss-Legendre quadrature on [-1, 1] (Newton's method on the Legendre polynomial)."""
    xs, ws = [], []
    for i in range(1, n + 1):
        x = math.cos(math.pi * (i - 0.25) / (n + 0.5))
        for _ in range(100):
            p0_, p1_ = 1.0, x
            for j in range(2, n + 1):
                p0_, p1_ = p1_, ((2 * j - 1) * x * p1_ - (j - 1) * p0_) / j
            dp = n * (x * p1_ - p0_) / (x * x - 1.0)
            dx = p1_ / dp
            x -= dx
            if abs(dx) < 1e-15:
                break
        xs.append(x)
        ws.append(2.0 / ((1.0 - x * x) * dp * dp))
    return xs, ws


GL_X, GL_W = gauss_legendre(16)


def integrate(fun, a, b, panels=28):
    """Composite 16-point Gauss-Legendre quadrature of fun over [a, b]."""
    h = (b - a) / panels
    total = 0.0
    for p in range(panels):
        mid = a + (p + 0.5) * h
        total += 0.5 * h * sum(w * fun(mid + 0.5 * h * x) for x, w in zip(GL_X, GL_W))
    return total


def level_of(c, odds_of_mu, k):
    """Pr[V <= c] for the canonical variable V = kappa_U * o, with U uniform and mu_H from its mid-p confidence
    distribution: section 8's averaged level of the claim that the canonical ratio is at most c. Given mu,
    Pr[kappa_U * o(mu) <= c] is c/(c + o(mu)) where o(mu) <= c and 0 otherwise (the level of the long paper's Lemma, the
    level reading); o falls as mu rises, so the credit begins at the mu where o(mu) = c, and the level is integrated
    against the distribution's density from there."""
    top = 10.0 * k + 60.0
    if odds_of_mu(1e-12) <= c:
        lo = 0.0
    elif odds_of_mu(top) > c:
        return 0.0
    else:
        a, b = 1e-12, top
        for _ in range(200):
            mid = 0.5 * (a + b)
            if odds_of_mu(mid) > c:
                a = mid
            else:
                b = mid
        lo = b
    return integrate(lambda m: c / (c + odds_of_mu(m)) * cd_density(m, k), lo, top)


def canonical_quantile_of(c, odds_of_mu, k):
    """The canonical quantile of the value c: Pr[V > c], one minus the level of the claim that the canonical ratio is
    at most c. It falls as c rises."""
    return 1.0 - level_of(c, odds_of_mu, k)


def canonical_ratio_at(q, odds_of_mu, k):
    """The canonical ratio at canonical quantile q: the least c with Pr[V > c] <= q, i.e. the (1 - q)-quantile of V,
    by geometric bisection on level_of."""
    lo, hi = 1e-9, 1e6
    for _ in range(64):
        mid = math.sqrt(lo * hi)
        if level_of(mid, odds_of_mu, k) >= 1.0 - q:
            hi = mid
        else:
            lo = mid
    return hi


def kappa_q(q):
    """The principle's scale at canonical quantile q, extended below the median at the median's value."""
    return max(1.0, q / (1.0 - q))


def _sig3(x, up):
    d = math.floor(math.log10(x))
    s = 10.0 ** (d - 2)
    v = (math.ceil(x / s - 1e-9) if up else math.floor(x / s + 1e-9)) * s
    return f"{v:.0f}" if v >= 100 else (f"{v:.1f}" if v >= 10 else f"{v:.2f}")


def fmt_bound(c):
    """A bound on the canonical ratio, rounded up: 1/N with N rounded down, or a value above one rounded up."""
    return f"1/{_sig3(1.0 / c, up=False)}" if c < 1.0 else _sig3(c, up=True)


def fmt_range(c1, c2):
    a, b = sorted((c1, c2))
    return f"${fmt_bound(a)}$--${fmt_bound(b)}$"


def p0(ratio, mu):
    """The Poisson probability of no formidable arrival, the predators' expected number being mu * ratio."""
    return math.exp(-mu * ratio)


def p0_pct(ratio, q, k):
    """P0's q-th percentile: P0 at mu_H's (1-q)-th, since P0 falls steadily as mu_H rises."""
    return p0(ratio, mu_q(1.0 - q, k))


def p0_level(ratio, level, k):
    """P0's central interval at the given level, from the mid-p distribution."""
    return p0_pct(ratio, (1.0 - level) / 2, k), p0_pct(ratio, (1.0 + level) / 2, k)


def binom_pmf(d, n, p):
    return math.comb(n, d) * p ** d * (1.0 - p) ** (n - d)


def mu_repeats_median(n_pool, d_seen):
    """Repeats on a pool of n_pool equally likely non-formidable species, d_seen of them arrived: each is seen with
    probability pi = 1 - exp(-mu/n_pool), so the count of distinct arrivals is Binomial(n_pool, pi). The median of pi's
    mid-p confidence distribution, P(D > d | pi) + P(D = d | pi)/2 = 1/2, mapped to mu = -n ln(1 - pi)."""
    cd = lambda p: sum(binom_pmf(i, n_pool, p) for i in range(d_seen + 1, n_pool + 1)) + 0.5 * binom_pmf(d_seen, n_pool, p)
    pi = solve_increasing(cd, 0.5, 1e-12, 1.0 - 1e-12)
    return -n_pool * math.log(1.0 - pi)


def odds(p):
    return p / (1 - p)


def f_of(pool, count="forms", contested=True):
    nf, nn = pooled(pool, count, contested)
    return nf, nn, nf / (nf + nn)


def pct(q):
    return f"{100 * q:g}"


def main():
    out = {}
    T = T0 - T_REC
    TB = T0 - T_BND
    K = K_LINEAGE
    med = mu_med(K)
    print("=" * 112)
    print("1. THE POOL (outside the Transylvanian landmass; any size; Santonian to the island's record end, 67.0 Ma)")
    for r in POOL:
        print(f"   {r[1]}  {r[2]:9s} {r[3]}  {','.join(r[4]):10s} {r[0]}   [{r[5]}; {r[6]}]")
    print("   excluded: " + "; ".join(EXCLUDED))

    print("=" * 112)
    print("2. THE ABSENCE, P0 = exp(-mu_H f/(1 - f)), at the median of mu_H's confidence distribution given the k arrivals"
          " seen, to the island's record end")
    print(f"   k = {K} non-formidable arrivals over the window {T0}-{T_REC} Ma ({T:.1f} Myr)")
    lo_med = solve_increasing(lambda m: 1.0 - pois_cdf(K - 1, m), 0.5, 1e-12, 200.0)
    hi_med = solve_increasing(lambda m: 1.0 - pois_cdf(K, m), 0.5, 1e-12, 200.0)
    print(f"   mu_H, the herbivores' expected number over the window (mid-p confidence distribution): median {med:.4f}"
          f" (plug-in at k: {K}; the exact construction's two medians {lo_med:.4f} and {hi_med:.4f})")
    print(f"   the herbivores' rate: median {med / T:.4f}/Myr")
    print("   mu_H's percentiles: " + "; ".join(f"{pct(q)}th {mu_q(q, K):.3f}" for q in PCTS))
    for lv in LEVELS:
        lo, hi = mu_q((1 - lv) / 2, K), mu_q((1 + lv) / 2, K)
        print(f"   mu_H, central {pct(lv)}% interval (mid-p): {lo:.4f} to {hi:.4f}; rate {lo / T:.4f} to {hi / T:.4f}/Myr")
    for lv in (0.95, 0.90):
        lo, hi = garwood(K, lv)
        print(f"   mu_H, exact (Garwood) {pct(lv)}% interval: {lo:.4f} to {hi:.4f}  (check: P(K >= {K} | {lo:.4f}) = "
              f"{1 - pois_cdf(K - 1, lo):.5f}; P(K <= {K} | {hi:.4f}) = {pois_cdf(K, hi):.5f})")
    readings = [("FORMS (main)", "forms", True), ("NAMED, valid only", "named", False),
                ("NAMED, with the contested names", "named", True)]
    for name, cnt, con in readings:
        nf, nn = pooled(POOL, cnt, con)
        f = nf / (nf + nn)
        ratio = f / (1 - f)
        Ffr, Fnr = resolved(POOL, cnt, con)
        rr = Ffr / Fnr
        out[name] = dict(nf=nf, nn=nn, f=f, ratio=ratio, rr=rr)
        print(f"   {name}: f = {nf}/{nf + nn} = {f:.4f}; f/(1 - f) = {nf}/{nn} = {ratio:.5f};"
              f"  stage-by-stage share {Ffr / (Ffr + Fnr):.3f} (F_f/F_n = {rr:.5f})")
        print(f"      the predators' rate: median {med * ratio / T:.4f}/Myr")
        print(f"      P0 median = exp(-{med:.4f} x {ratio:.5f}) = {p0(ratio, med):.5f}   (plug-in at k = {K}: "
              f"{p0(ratio, K):.5f})")
        print("      P0 central intervals (mid-p): " + "; ".join(
            f"{pct(lv)}% {p0_level(ratio, lv, K)[0]:.5f} to {p0_level(ratio, lv, K)[1]:.5f}" for lv in LEVELS))
        lo, hi = garwood(K, 0.95)
        print(f"      P0 exact (Garwood) 95% interval: {p0(ratio, hi):.5f} to {p0(ratio, lo):.5f}")
        for k in (K_CLASS, K_NO_GARGANTUAVIS, K_LINEAGE, K_PLUS1, K_MAX):
            mk = mu_med(k)
            print(f"      k = {k:2d}:  mu_H median {mk:.4f};  P0 {p0(ratio, mk):.4f};  stage-by-stage {p0(rr, mk):.4f}")
    m = out["FORMS (main)"]
    pm = p0(m["ratio"], med)
    print(f"   main reading: P0 = exp(-{med:.4f} x {m['nf']}/{m['nn']}) = {pm:.4f}, about 1 in {1 / pm:.1f}")
    print(f"   the absence used as data (it lets the attribute help price itself; the total rate's median from all {K} "
          f"arrivals, mu_T = mu f): exp(-{med:.4f} f) = {math.exp(-med * m['f']):.4f}")
    mu_r = mu_repeats_median(m["nn"], K)
    print(f"   repeats on a pool no larger than the census ({m['nn']} non-formidable forms; {K} seen; mu_H median "
          f"{mu_r:.3f}): P0 = {p0(m['ratio'], mu_r):.4f}; P(a repeat among {K} draws from {m['nn']}) = "
          f"{1 - math.prod((m['nn'] - i) / m['nn'] for i in range(K)):.2f}")
    m7 = mu_med(K_NO_GARGANTUAVIS)
    pool_nb = [r for r in POOL if "Gargantuavis" not in r[0] and "ornithuromorph" not in r[0]]
    nf, nn, fb = f_of(pool_nb)
    print(f"   Gargantuavis a flier (k = {K_NO_GARGANTUAVIS}): pool kept, P0 = {p0(m['ratio'], m7):.4f}; "
          f"birds left out on both sides, f = {nf}/{nf + nn} = {fb:.3f}, P0 = {p0(odds(fb), m7):.4f}")
    nf, nn, fv = f_of(POOL + [VARIANT_VARIRAPTOR])
    print(f"   Variraptor counted as a species of its own: f = {nf}/{nf + nn} = {fv:.3f}, P0 = {p0(odds(fv), med):.4f}")
    pool_np = [r for r in POOL if not r[0].startswith("Pneumatoraptor")]
    nf, nn, fn_ = f_of(pool_np)
    print(f"   Pneumatoraptor read as an avialan (left out; its cell's other records are Paraves indet. teeth, not "
          f"counted): f = {nf}/{nf + nn} = {fn_:.3f}, P0 = {p0(odds(fn_), med):.4f}")
    paravian = ("Pyroraptor", "Pneumatoraptor", "Taveiro troodontid", "late-Maastrichtian dromaeosaurid",
                "Kozina dromaeosaurid", "Kozina troodontid", "Tamarro")
    pool_pv = [r for r in POOL if not r[0].startswith(paravian)]
    nf, nn, fp = f_of(pool_pv)
    print(f"   the pool's paravians read as the author's bet reads the island's (fliers, left out): f = {nf}/{nf + nn} = "
          f"{fp:.3f}, P0 = {p0(odds(fp), med):.4f}")
    pool_tt = [r for r in POOL if not r[0].startswith(("Taveiro troodontid", "Kozina troodontid"))]
    nf, nn, ft = f_of(pool_tt)
    print(f"   the tentative troodontid forms (Taveiro, Kozina) left out: f = {nf}/{nf + nn} = {ft:.3f}, "
          f"P0 = {p0(odds(ft), med):.4f}")
    pool_kz = [r for r in POOL if not r[0].startswith("Kozina")]
    nf, nn, fk = f_of(pool_kz)
    print(f"   the Kozina site left out, both sides: f = {nf}/{nf + nn} = {fk:.3f}, P0 = {p0(odds(fk), med):.4f}")
    pool_old = [r for r in pool_kz if not r[0].startswith("Taveiro troodontid")]
    nf, nn, fo_ = f_of(pool_old)
    print(f"   Kozina and the Taveiro troodontids left out (the census before version 3.1's review): f = {nf}/{nf + nn} = "
          f"{fo_:.3f}, P0 = {p0(odds(fo_), med):.4f}")
    pool_om = [(r[0], "F") + r[2:] if r[0].startswith("?Ornithomimosauria") else r for r in POOL]
    nf, nn, fo = f_of(pool_om)
    print(f"   ornithomimosaurs counted as formidable: f = {nf}/{nf + nn} = {fo:.3f}, P0 = {p0(odds(fo), med):.4f}")
    pool_weak = [r for r in POOL if not r[0].startswith(("Lo Hueco", "Muthmannsdorf"))]
    nf, nn, fw = f_of(pool_weak)
    print(f"   the two least secure predator forms (Lo Hueco, Muthmannsdorf) dropped: f = {nf}/{nf + nn} = {fw:.3f},"
          f" P0 = {p0(odds(fw), med):.4f}")
    print("   the confidence that P0 exceeds a given value (main reading), the distribution's mass below mu_H = "
          "-ln(value)/(f/(1 - f)): " + "; ".join(f"{lab} {midp_cd(-math.log(x) / m['ratio'], K):.4f}"
                                                  for lab, x in (("6%", 0.06), ("1/16", 1.0 / 16), ("12%", 0.12))))
    r16 = math.log(16) / med
    print(f"   sensitivity: P0 = 1/16 at the median needs f/(1 - f) = ln 16/{med:.4f} = {r16:.4f}, f = "
          f"{r16 / (1 + r16):.3f}")
    print(f"   the author's single example (f = 1/2, four herbivore arrivals): (1 - f)^4 = {0.5 ** 4:.4f} (his negative-"
          f"binomial count); the Poisson zero term exp(-mu) at mu = 4, {math.exp(-4):.4f}, and at the median for k = 4, "
          f"{mu_med(4):.4f}, {math.exp(-mu_med(4)):.4f}")

    print("=" * 112)
    print(f"3. THE REFUGE'S HORIZON (predators' exposure to the boundary, 66.0 Ma: the ratio scaled by {TB:.1f}/{T:.1f};"
          f" k and its window unchanged)")
    bnd = {}
    for name, cnt, con in readings:
        o = out[name]
        rb = o["ratio"] * TB / T
        o["rb"] = rb
        Ffr, Fnr = resolved(POOL, cnt, con)
        Fft, _ = resolved(POOL, cnt, con, bins=["tM"])
        rrb = (Ffr + Fft) / Fnr
        lo95, hi95 = p0_level(rb, 0.95, K)
        bnd[name] = p0(rb, med)
        print(f"   {name:36s} k = {K}: P0 median {p0(rb, med):.5f}; central 95% {lo95:.5f} to {hi95:.5f}; "
              f"stage-by-stage {p0(rrb, med):.4f};  k = {K_CLASS}: {p0(rb, mu_med(K_CLASS)):.4f}")
        print("      percentiles: " + "; ".join(f"{pct(q)}th {p0_pct(rb, q, K):.5f}" for q in PCTS))

    print("=" * 112)
    print("4. THE PREMISE CHECK: Cenozoic islands, the same random variable read directly")
    big = [(n, h, p) for n, h, p in ISLANDS if h >= 4]
    none = sum(1 for _, _, p in big if p == 0)
    print(f"   islands with >= 4 large-herbivore colonizations: {len(big)}; with no terrestrial predator ever: {none} "
          f"({none / len(big):.2f})")

    print("=" * 112)
    print("5. THE PRINCIPLE'S PERCENTILE SCALE (general): at the beta-th percentile of the realization the canonical ratio")
    print("   P(H|A')/P(H|A) is at most kappa_beta = beta/(1-beta) times the prior odds, failing with probability at most")
    print("   1 - beta = 1/(1+kappa_beta); licensed from the 50th percentile (kappa = 1, strict form) up. Read here for a")
    print("   prior of 0.01, with the linkage (1 - r)/(1 + r).")
    for b in (0.5, 0.6, 0.75, 0.8, 0.9, 0.95, 0.99):
        kap = b / (1 - b)
        r = kap * odds(0.01)
        print(f"   {pct(b):>4s}th  kappa {kap:6.2f}  fails with probability at most {1 - b:.2f}  canonical ratio at most "
              f"{r:.4f}  linkage at least {(1 - r) / (1 + r):.3f}")

    print("=" * 112)
    print("6. STAGE ONE, ON TWO PERCENTILES: kappa's (the principle's scale) and the Hateg probability's (its confidence")
    print("   distribution from the herbivores' rate); the canonical ratio is at most kappa_beta * odds(P(A|LC) at its")
    print("   gamma-th percentile), and the linkage at least (1 - r)/(1 + r).")
    for name, _, _ in readings:
        o = out[name]
        print(f"   {name}:")
        for b in KAP_PCTS:
            kap = b / (1 - b)
            cells = []
            for g in HAT_PCTS:
                p = p0_pct(o["ratio"], g, K)
                r = kap * odds(p)
                cells.append(f"{pct(g)}th P {p:.4f}: r {r:.4f} L {(1 - r) / (1 + r):6.3f}")
            print(f"      kappa {pct(b)}th ({kap:.0f}) | " + " | ".join(cells))
    print("   the configuration (its prior a point; the principle's percentile alone):")
    for b in KAP_PCTS:
        kap = b / (1 - b)
        print(f"      kappa {pct(b)}th ({kap:.0f}) | " + " | ".join(
            f"P_LC {plc:.4f}: r {kap * odds(plc):.4f} L {(1 - kap * odds(plc)) / (1 + kap * odds(plc)):6.3f}"
            for _, plc in P_LC))

    print("=" * 112)
    print("7. THE REFUGE AND THE FORWARD PREDICTION: the occupied branch's prior is P_LC * P(A|LC) counted to the")
    print("   boundary; the canonical ratio of the branch that turned arboreal only after the boundary to the occupied one")
    print("   is at most kappa_beta * odds of that prior, on the same two percentiles (printed as 1/N).")
    for name, _, _ in readings:
        o = out[name]
        print(f"   {name}: the refuge's price, P_LC * P0 to the boundary, at the Hateg median "
              + "; ".join(f"{plc * bnd[name]:.6f}" for _, plc in P_LC)
              + "; over its central 95% interval "
              + "; ".join(f"{plc * p0_pct(o['rb'], 0.025, K):.6f} to {plc * p0_pct(o['rb'], 0.975, K):.6f}" for _, plc in P_LC))
        for lname, plc in P_LC:
            print(f"      P_LC {lname}:")
            for b in KAP_PCTS:
                kap = b / (1 - b)
                print(f"         kappa {pct(b)}th | " + " | ".join(
                    f"{pct(g)}th 1/{1 / (kap * odds(plc * p0_pct(o['rb'], g, K))):.1f}" for g in HAT_PCTS))
    for lname, plc in P_LC:
        print(f"   the configuration alone, {lname:44s} " + "; ".join(
            f"kappa {pct(b)}th 1/{1 / ((b / (1 - b)) * odds(plc)):.1f}" for b in KAP_PCTS))

    print("=" * 112)
    print("8. THE FACTOR READING: the level at which the principle carries the claim that the alternative cuts the")
    print("   probability of observers by at least N times (the canonical ratio at most 1/N, N fixed in advance):")
    print("   kappa/(1+kappa) at the kappa that puts the bound at 1/N, with no credit where that kappa falls below one (the")
    print("   level reading), averaged over the confidence distribution: a confidence-weighted level, not a guarantee at")
    print("   the unknown prior.")
    NS = (1, 2, 3, 5, 10, 20, 50, 100, 300, 1000)
    for name, _, _ in readings:
        r = out[name]["ratio"]
        print(f"   the absence, {name:32s} " + "  ".join(
            f"{n}x {prob_factor(n, lambda m, r=r: odds(p0(r, m)), K):.3f}" for n in NS))
    for lname, plc in P_LC:
        o = odds(plc)
        print(f"   the configuration, P_LC {plc:.4f}            " + "  ".join(f"{n}x {kappa_cdf((1.0 / n) / o):.3f}" for n in NS))
    for name, _, _ in readings:
        rb = out[name]["rb"]
        for lname, plc in P_LC:
            print(f"   the refuge, {name:32s} P_LC {plc:.4f} " + "  ".join(
                f"{n}x {prob_factor(n, lambda m, rb=rb, plc=plc: odds(plc * p0(rb, m)), K):.3f}" for n in NS))

    print("=" * 112)
    print("9. CANONICAL QUANTILES, written as percentages: the canonical variable V = kappa(U) * odds(P), kappa(q) =")
    print("   max(1, q/(1-q)), U uniform and the prior from its confidence distribution independently of U. The canonical")
    print("   quantile of a value c is Pr[V > c], one minus section 8's averaged level (integrated here, not averaged over the")
    print("   grid); the canonical ratio at canonical quantile q is the least c with Pr[V > c] <= q, falling as q rises, and the")
    print("   claim that the canonical ratio is at most it is carried at level 1 - q: a level over the realization of a declared")
    print("   attribute, not conditional on the prior realized, and, averaged over the confidence distribution, a weighted")
    print("   calibration index of this construction, not a posterior probability or a coverage guarantee. V is an envelope,")
    print("   the principle's bound read at a random percentile, not the canonical ratio's distribution. For a point prior the")
    print("   canonical ratio at q is kappa(1-q) times the odds, the median's above 50%. Bounds rounded up.")
    QL = (0.01,) + tuple(round(0.05 * i, 2) for i in range(1, 20)) + (0.99,)
    QO = (0.01, 0.05, 0.10, 0.25, 0.50, 0.75, 0.90, 0.95, 0.99)
    pq = pct
    print("   the accordance ratio at canonical quantile q (any attribute, its prior given), kappa(1-q): " + "; ".join(
        f"{pq(q)}%: {kappa_q(1 - q):.3g}" for q in QL))
    rf, rnv, rnc = out["FORMS (main)"]["ratio"], out["NAMED, valid only"]["ratio"], out["NAMED, with the contested names"]["ratio"]
    rbf = out["FORMS (main)"]["rb"]
    lc_lo, lc_hi, lc_lf = (plc for _, plc in P_LC)
    o_abs = lambda r: (lambda m: odds(p0(r, m)))
    o_ref = lambda r, plc: (lambda m: odds(plc * p0(r, m)))
    cols = {"forms": o_abs(rf), "named_c": o_abs(rnc), "named_v": o_abs(rnv),
            "ref_lo": o_ref(rbf, lc_lo), "ref_hi": o_ref(rbf, lc_hi)}
    tab = {q: {name: canonical_ratio_at(q, fn, K) for name, fn in cols.items()} for q in QL}
    for q in QL:
        t = tab[q]
        cf = [kappa_q(1 - q) * odds(p) for p in (lc_lo, lc_hi, lc_lf)]
        print(f"   {pq(q):>2s}%: absence, forms {t['forms']:.5g}; named {t['named_c']:.5g} (contested) to {t['named_v']:.5g} "
              f"(valid); configuration {cf[0]:.5g} to {cf[1]:.5g} (least favourable {cf[2]:.5g}); refuge {t['ref_lo']:.5g} "
              f"to {t['ref_hi']:.5g}")

    def row(q):
        t = tab[q]
        cf = [kappa_q(1 - q) * odds(p) for p in (lc_lo, lc_hi)]
        return (f"      ${pq(q)}$ & ${fmt_bound(t['forms'])}$ & {fmt_range(t['named_c'], t['named_v'])} & "
                f"{fmt_range(cf[0], cf[1])} & {fmt_range(t['ref_lo'], t['ref_hi'])} \\\\")
    print("   the table, rows LaTeX-ready, canonical quantiles in percent: Table tab:hat-canonical in the long paper, every 5%")
    print("   with 1% and 99%:")
    for q in QL:
        print(row(q))
    print("   Table tab:hateg-canonical in Optimal Earth, at 1, 5, 10, 25, 50, 75, 90, 95 and 99%:")
    for q in QO:
        print(row(q))
    print("   the canonical quantile of the factor one (the claim that the alternative was no more productive), P(A) for a "
          f"point prior: forms {100 * canonical_quantile_of(1.0, cols['forms'], K):.3f}%; named "
          f"{100 * canonical_quantile_of(1.0, cols['named_c'], K):.2f}% (contested) to "
          f"{100 * canonical_quantile_of(1.0, cols['named_v'], K):.2f}% (valid); configuration {100 * lc_lo:.2f}% to "
          f"{100 * lc_hi:.2f}%; refuge {100 * canonical_quantile_of(1.0, cols['ref_lo'], K):.3f}% to "
          f"{100 * canonical_quantile_of(1.0, cols['ref_hi'], K):.3f}%")
    print("   the canonical quantiles of the cuts 2x, 5x, 10x, 20x, 100x on the count of forms (one minus section 8's levels, "
          "integrated): " + "; ".join(f"{n}x {100 * canonical_quantile_of(1.0 / n, cols['forms'], K):.2f}%"
                                      for n in (2, 5, 10, 20, 100)))
    print("   up to canonical quantile 50% the configuration's bound is the lower; above it the configuration's stays at its"
          " median and the absence's passes it above the absence's canonical quantile of the configuration's odds: "
          f"canonical tolerance {100 * canonical_quantile_of(odds(lc_hi), cols['forms'], K):.3f}%; exact extremes "
          f"{100 * canonical_quantile_of(odds(lc_lo), cols['forms'], K):.3f}%")
    mm = odds(p0_pct(rf, 0.5, K))
    print(f"   the two-percentile bound with kappa and the Hateg probability both at their medians, {mm:.5f}, sits at "
          f"canonical quantile {100 * canonical_quantile_of(mm, cols['forms'], K):.2f}% (at most 75%: Proposition "
          "prop:canonical-scale)")
    print("   the forward prediction on named species (the refuge, named, to the boundary), and on the least favourable "
          "separating settings (forms):")
    for q in (0.1, 0.5, 0.9):
        nm = [canonical_ratio_at(q, o_ref(out[nm]["rb"], plc), K)
              for nm in ("NAMED, valid only", "NAMED, with the contested names") for plc in (lc_lo, lc_hi)]
        lf = canonical_ratio_at(q, o_ref(rbf, lc_lf), K)
        print(f"      {pq(q)}%: named, cut at least {_sig3(1 / max(nm), False)}- to {_sig3(1 / min(nm), False)}-fold "
              f"(bounds {min(nm):.5g} to {max(nm):.5g}); least favourable, forms: cut at least {_sig3(1 / lf, False)}-fold "
              f"(bound {lf:.5g})")

if __name__ == "__main__":
    main()

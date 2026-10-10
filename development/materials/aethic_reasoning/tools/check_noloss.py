# No-loss checker: every baseline label defined once; every baseline paragraph present verbatim (anywhere) or ledgered; footnotes conserved.
import re, json, hashlib, sys, collections
inv = json.load(open(sys.argv[1])); new = open(sys.argv[2], encoding='utf-8').read()
ledger = json.load(open(sys.argv[3])) if len(sys.argv) > 3 else {}          # {para_hash: "destination / reason"}
HEAD = re.compile(r'\n(?=\s*\\(?:section|subsection|subsubsection|paragraph)\*?\{)')
def split(t): return re.split(r'\n\s*\n', HEAD.sub('\n\n', t))
def norm(t): t = re.sub(r'(?m)^\s*%.*$', '', t); return re.sub(r'\s+', ' ', t).strip()
have = {hashlib.md5(norm(p).encode()).hexdigest()[:12] for p in split(new) if len(norm(p)) > 40}
strip = lambda t: re.sub(r'(?<!\\)%.*', '', t)
labs = collections.Counter(re.findall(r'\\label\{([^}]*)\}', strip(new)))
base_labs = collections.Counter(re.findall(r'\\label\{([^}]*)\}', strip(open(inv['source'], encoding='utf-8').read())))
miss_lab = sorted(l for l in base_labs if labs[l] != base_labs[l])
miss_par = [(u['start'], u['title'][:40], h, ph) for u in inv['units'] for h, ph in zip(u['paras'], u['para_heads']) if h not in have and h not in ledger]
fn_base = sum(u['footnotes'] for u in inv['units']); src0 = open(inv['source'], encoding='utf-8').read()
fn_delta = new.count('\\footnote{') - src0.count('\\footnote{')
n_par = sum(len(u['paras']) for u in inv['units'])
print(f"labels: {len(miss_lab)} of {len(base_labs)} changed in count | paragraphs: {n_par - len(miss_par)}/{n_par} present or ledgered | footnote delta (whole paper): {fn_delta:+d}")
for s, t, h, ph in miss_par[:12]: print(f"  MISSING para {h} (from L{s} {t}): {ph[:80]}")
for l in miss_lab[:12]: print(f"  LABEL {l}: defined {labs[l]} times (baseline {base_labs[l]})")
sys.exit(0 if not miss_lab and not miss_par and fn_delta == 0 else 1)

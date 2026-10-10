# Baseline inventory of Sections 3, 4 (and 6's weighted apparatus) for the no-loss overhaul.
import re, json, hashlib, sys
SRC = sys.argv[1]; OUT = sys.argv[2]
src = open(SRC, encoding='utf-8').read(); L = src.split('\n')
HEAD = re.compile(r'\n(?=\s*\\(?:section|subsection|subsubsection|paragraph)\*?\{)')
def split(t): return re.split(r'\n\s*\n', HEAD.sub('\n\n', t))
def norm(t): t = re.sub(r'(?m)^\s*%.*$', '', t); return re.sub(r'\s+', ' ', t).strip()
secs = [(i + 1, re.sub(r'\}.*', '', l.split('{', 1)[1])) for i, l in enumerate(L) if re.match(r'\s*\\section\*?\{', l)]
def span(title):
    for n, (ln, t) in enumerate(secs):
        if t.startswith(title): return ln, (secs[n + 1][0] - 1 if n + 1 < len(secs) else len(L))
S3, S4, S6 = span('The Aethus as a Mathematical Object'), span('Incorporation of Aethic Weighting'), span('Constructing the Third Postulate')
units = []
WHOLE = [(secs[n][0], (secs[n + 1][0] - 1 if n + 1 < len(secs) else len(L)), str(n + 1)) for n in range(len(secs))]
for a, b, tag in [(1, secs[0][0] - 1, '0')] + WHOLE:
    (a, b) = (a, b)
    cuts = [i + 1 for i in range(a - 1, b) if re.match(r'\s*\\(section|subsection|subsubsection)\*?\{', L[i])] + [b + 1]
    for x, y in zip(cuts, cuts[1:]):
        body = '\n'.join(L[x - 1:y - 1]); title = re.sub(r'\}.*', '', L[x - 1].split('{', 1)[1])[:70]
        labels = re.findall(r'\\label\{([^}]*)\}', body)
        envs = [m.group(1) + (':' + m.group(2)[:50] if m.group(2) else '') for m in re.finditer(r'\\begin\{(defin|boxdef|prince|theorem|lemma|coro|corollary|proposition|tcolorbox)\}(?:\[([^\]]*)\]|\{([^}]*)\})?', body)]
        paras = [norm(p) for p in split(body) if len(norm(p)) > 40]
        units.append(dict(sec=tag, start=x, end=y - 1, title=title, labels=labels, envs=envs, footnotes=body.count('\\footnote{'),
                          paras=[hashlib.md5(p.encode()).hexdigest()[:12] for p in paras], para_heads=[p[:90] for p in paras]))
# incoming references from outside each unit
refs = [(m.group(2), src.count('\n', 0, m.start()) + 1) for m in re.finditer(r'\\(ref|autoref|eqref|pageref|hyperref\[)\{?([^}\]]+)', src)]
for u in units:
    labs = set(u['labels']); u['incoming'] = sum(1 for lab, ln in refs if lab in labs and not (u['start'] <= ln <= u['end']))
json.dump(dict(source=SRC, S3=S3, S4=S4, S6=S6, units=units), open(OUT, 'w'), indent=1)
tot = lambda k: sum(len(u[k]) if isinstance(u[k], list) else u[k] for u in units)
print(f"S3 L{S3[0]}-{S3[1]}  S4 L{S4[0]}-{S4[1]}  S6 L{S6[0]}-{S6[1]} | units {len(units)} | labels {tot('labels')} | formal envs {tot('envs')} | footnotes {tot('footnotes')} | paragraphs {tot('paras')}")

#!/usr/bin/env python3
"""Step 10 — the named characters of the arena page.

Usage:  python3 10_characters.py     reads characters.json, outputs/titan_classes.csv, outputs/human_model.json
                                     -> the block between /*EXTRA*/ and /*END EXTRA*/ in ../arena.html
                                     and, where rotg_characters.json exists (private, not in git), -> ../arena_rotg.html
A character is not a class on a body: he is a tier of his own, placed by one figure and a few traits (characters.json says what each means).
The page itself only knows how to show a fighter that is frail, strikes hard, is swift, elusive or nimble, or is drawn as a shade.
arena_rotg.html is the same page with the private characters added and its own lists put first; nothing in it is copied by hand, so every
change to arena.html reaches it the next time this runs, and step 8 runs this whenever it rewrites arena.html."""
import json, math, os
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
TITAN_WARRIOR = 0.3884808165     # the Titan Warrior on the scale of the author's first table; a character's figure over this is his odds against one
ORDER = "{ const rk = f => f.group === 'ROTG characters' ? 0 : /^ROTG/.test(f.group) ? 1 : 2; DATA.fighters = DATA.fighters.map((f, i) => [f, i]).sort((a, b) => rk(a[0]) - rk(b[0]) || a[1] - b[1]).map(x => x[0]); }"   # the themed page lists its own first
SD = (0.7, 1.0)                  # spread given to a character's log score and duel log-odds: wider than a school's


def block(cfg, T, g, themed, M=None):
    lo = lambda elo: (elo - 1000) * math.log(10) / 400; tw = T.loc['Titan Warrior']; out = []
    for c in cfg['characters']:
        r = math.log(c['figure'] / TITAN_WARRIOR) + c.get('tactics', 0.0); b = T.loc[c['body']]; mu = math.log(tw.score) + g * c.get('carry', 1.0) * r; duel = lo(tw.duel_elo) + r
        out.append(dict(name=c['name'], group='ROTG characters', mu=mu, sd=SD[0], duel=duel, duel_sd=SD[1], usk=0, ask=0, arm=0, gun=False, weapon=c.get('weapon', 'none'), armour='none', mass=c.get('mass', 75),
                        frail=True, dur=math.log(b.score), ddur=lo(b.duel_elo), strike=c.get('strike', 1), swift=c.get('swift', 0), look=c.get('look'), elusive=bool(c.get('elusive')), nimble=c.get('nimble', 0)))
        if c.get('mount'):   # in the saddle: he and the horse by the group rule, the saddle's premium in a duel, and none of what he does on foot
            h = M['horses'][c['mount']]; k = M['k']; e = out[-1]; e.update(mu=k * math.log(math.exp(e['mu'] / k) + h['score'] ** (1 / k)), duel=e['duel'] + M['duel'], mass=e['mass'] + h['kg'], swift=0, elusive=False, nimble=0,
                                                                  mount=dict(name=h['label'], kg=h['kg'], length=h['length'], shape=h['shape'], coat=h['coat'], body=h['body'], dark=h['dark'], accent=h['accent']))
        print(f"{'themed' if themed else 'public'}: {c['name']}: {math.exp(r):,.0f} to 1 against a Titan Warrior (his figure alone: {c['figure'] / TITAN_WARRIOR:,.0f} to 1); score {math.exp(mu):,.0f} (lion = 100), duel rating {1000 + 400 / math.log(10) * duel:,.0f}")
    return (('DATA.themed = true; ' if themed else '') + 'DATA.fighters.push(...' + json.dumps(out, separators=(',', ':')) + '); ' + (ORDER + ' ' if themed else '') + 'DATA.setups = ' + json.dumps(cfg.get('setups', []), separators=(',', ':')) + ';'
            + ("\nif (typeof document !== 'undefined') document.title = 'ROTG arena';" if themed else ''))


def main():
    os.chdir(HERE); pub = json.load(open('characters.json', encoding='utf-8')); T = pd.read_csv('outputs/titan_classes.csv').set_index('cls'); model = json.load(open('outputs/human_model.json')); g = model['gamma']; g = g[0] if isinstance(g, list) else g; M = model.get('mount')
    page = open('../arena.html', encoding='utf-8').read(); a, b = page.index('/*EXTRA*/') + len('/*EXTRA*/'), page.index('/*END EXTRA*/'); put = lambda js: page[:a] + '\n' + js + '\n' + page[b:]
    open('../arena.html', 'w', encoding='utf-8').write(put(block(pub, T, g, False, M))); print('refreshed the characters in ../arena.html')
    if os.path.exists('rotg_characters.json'):
        prv = json.load(open('rotg_characters.json', encoding='utf-8')); both = dict(characters=pub['characters'] + prv.get('characters', []), setups=prv.get('setups', []) + pub.get('setups', []))
        open('../arena_rotg.html', 'w', encoding='utf-8').write(put(block(both, T, g, True, M))); print('wrote ../arena_rotg.html')


if __name__ == '__main__':
    main()

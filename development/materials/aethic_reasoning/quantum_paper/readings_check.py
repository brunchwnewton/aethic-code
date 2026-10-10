"""readings_check.py -- the check behind Proposition "Where the two readings part"
(Quantum Mechanics from Records, Section "A finite correspondence model").

Generates random finite models: refinement trees of record cells whose leaf weights are
zero or positive and whose internal weights are the sums of their sub-cells', with a random
set Base of base contradictions. For every state A of positive weight it computes validity
under the two readings of the structural coefficients, using the direct form of the fixed
point (Proposition "The fixed point closes at once"):

    valid(A)  iff  A not in Base  and  some proper descendant B of A has a cone free of Base

  (S) every record cell is a proper child;
  (W) cells of zero kernel weight are no proper children.

It reports how many states were checked, whether (W)-validity ever holds without
(S)-validity (the proposition says never), and whether the proposition's characterization
of the states valid under (S) but not under (W) is right in every case.

Usage:  python3 readings_check.py [trials] [seed]      (defaults: 4000 20261006)
Python 3, standard library only.
"""
import random
import sys


def gen_tree(rng, depth):
    nodes = {}
    counter = [0]

    def make(d):
        nid = counter[0]
        counter[0] += 1
        if d < depth and rng.random() < 0.6:
            kids = [make(d + 1) for _ in range(rng.randint(2, 3))]
            nodes[nid] = (kids, sum(nodes[k][1] for k in kids))
        else:
            nodes[nid] = ([], 0 if rng.random() < 0.3 else rng.randint(1, 5))
        return nid

    make(0)
    return nodes


def descendants(nodes, a, tied):
    """Proper descendants of a (reflexive); under (W) cells of zero weight are skipped."""
    out, stack = {a}, [a]
    while stack:
        x = stack.pop()
        for c in nodes[x][0]:
            if tied and nodes[c][1] == 0:
                continue
            if c not in out:
                out.add(c)
                stack.append(c)
    return out


def valid(nodes, a, base, tied):
    return a not in base and any(not (descendants(nodes, b, tied) & base)
                                 for b in descendants(nodes, a, tied))


def main(trials=4000, seed=20261006):
    rng = random.Random(seed)
    n = w_not_s = differ = correct = 0
    for _ in range(trials):
        nodes = gen_tree(rng, rng.randint(1, 4))
        base = {x for x in nodes if rng.random() < 0.3}
        for a in nodes:
            if nodes[a][1] == 0:
                continue
            n += 1
            vs, vw = valid(nodes, a, base, False), valid(nodes, a, base, True)
            w_not_s += (vw and not vs)
            differ += (vs != vw)
            positive = [b for b in descendants(nodes, a, False) if nodes[b][1] > 0]
            null = [b for b in descendants(nodes, a, False) if nodes[b][1] == 0]
            predicted = (a not in base
                         and all(descendants(nodes, b, True) & base for b in positive)
                         and any(not (descendants(nodes, b, False) & base) for b in null))
            correct += ((vs and not vw) == predicted)
    print(f"trials = {trials}, seed = {seed}")
    print(f"states of positive weight checked: {n}")
    print(f"valid under (W) but not under (S): {w_not_s}")
    print(f"states where the readings differ: {differ}")
    print(f"characterization correct: {correct} of {n}")


if __name__ == "__main__":
    args = [int(x) for x in sys.argv[1:3]]
    main(*args)

"""Exact arithmetic for the marked-lattice estimates in the Q3 note."""
from __future__ import annotations
import json
from collections import Counter
from itertools import combinations
from pathlib import Path
import sympy as sp


def negative_chain(weights: list[int]) -> sp.Matrix:
    if not weights or min(weights) < 2:
        raise ValueError("Use a nonempty Hirzebruch--Jung chain with weights >= 2.")
    q = sp.diag(*[-n for n in weights])
    for i in range(len(weights) - 1):
        q[i, i+1] = q[i+1, i] = 1
    return q


def charge(q: sp.Matrix, d: sp.Matrix) -> sp.Rational:
    return sp.factor(-(d.T * q.inv() * d)[0])


out: dict = {"single_curve": [], "pairs": [], "surviving_chains": []}
for n in range(2, 9):
    b = charge(sp.Matrix([[-n]]), sp.Matrix([n-2]))
    out["single_curve"].append({"weight": n, "canonical_charge": str(b),
      "lower_P_over_8pi2": str(sp.Rational(2,3)*(1+b))})

for s in (0, 1, 2):
    q = sp.Matrix([[-3,s],[s,-3]])
    b = charge(q, sp.Matrix([1,1]))
    assert b == sp.Rational(2,3-s)
    out["pairs"].append({"intersection": s,"charge": str(b),
        "lower_P_over_8pi2": str(sp.Rational(2,3)*(1+b))})

for r in range(1, 13):
    q = negative_chain([3]+[2]*(r-1))
    d = sp.Matrix([1]+[0]*(r-1))
    b = charge(q,d)
    assert b == sp.Rational(r,2*r+1)
    lower = sp.factor(sp.Rational(2,3)*(1+b))
    assert lower == 1-sp.Rational(1,6*r+3)
    out["surviving_chains"].append({"rank":r,"charge":str(b),
        "lower_P_over_8pi2":str(lower)})

# The three families of five degree-one rational curves in Proposition 4.3.
curves = [(m,i) for m in (-1,0,1) for i in range(5)]
def intersection(c, e):
    m,i = c; n,j = e
    if c == e: return -3
    k = abs(m-n)
    if k == 0: return 2
    if k == 1: return 1
    return 5 if i == j else 0
counts = Counter(intersection(c,e) for c,e in combinations(curves,2))
assert counts == {0:20,1:50,2:30,5:5}
out["Godeaux_pair_counts"] = dict(sorted(counts.items()))

# Check the Schur complement for a single -3 vertex with -2 tails.
for left in range(1,6):
    for right in range(1,6):
        q = negative_chain([2]*left+[3]+[2]*right)
        d = sp.zeros(left+right+1,1); d[left]=1
        b = charge(q,d)
        target = 1/(3-sp.Rational(left,left+1)-sp.Rational(right,right+1))
        assert b == target and b >= sp.Rational(1,2)

out["normalization"] = {
  "single_minus_three": "64*pi^2/9 = (8/9)*(8*pi^2)",
  "two_disjoint_minus_three": "80*pi^2/9 = (10/9)*(8*pi^2)",
  "admissible_total_charge": "beta < 1/2 when p_star < 8*pi^2"
}
path = Path(__file__).with_name("exact_lattice_values.json")
path.write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps(out,ensure_ascii=False,indent=2))

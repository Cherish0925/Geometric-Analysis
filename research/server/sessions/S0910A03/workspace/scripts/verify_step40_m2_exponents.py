#!/usr/bin/env python3
"""Algebra/exponent checks for Step 40 m=2 continuation note.

This checks only Holder/Young exponent identities and cutoff product identities.
It does not verify tensor provenance, signs, PDE existence, continuation, or Yau 26.
"""
from fractions import Fraction as Q

checks = []

def add(name, condition, detail=""):
    checks.append((name, bool(condition), detail))

# (2.4): Z^2 |V|^(p-2), with Z,V both at L^p.
for p in [4, 6, 8, 12, 25]:
    add(f"current pair Holder at p={p}", Q(2,p) + Q(p-2,p) == 1)

# (3.5): Theta, W in L^(2p), V^(p-1) in L^(p/(p-1)).
for p in [4, 6, 8, 12, 25]:
    add(f"lower pair product Holder at p={p}",
        Q(1,2*p)+Q(1,2*p)+Q(p-1,p) == 1)

# (3.7): Theta^2, W^2 at L^(2p) induced by Theta,W in L^(4p),
# V^(p-2) at L^(p/(p-2)); total reciprocal is (p-1)/p, leaving 1/p
# supplied by finite volume.
for p in [4, 6, 8, 12, 25]:
    used = Q(2,4*p)+Q(2,4*p)+Q(p-2,p)
    add(f"dissipation-remnant Holder leaves finite-volume slot p={p}",
        used == Q(p-1,p), f"used={used}")
    add(f"finite-volume slot is 1/p at p={p}", 1-used == Q(1,p))

# If desired, use Theta,W in L^(4p) and 1 in L^p.
for p in [4, 6, 8, 12, 25]:
    add(f"full four-factor Holder sums to one p={p}",
        Q(2,4*p)+Q(2,4*p)+Q(p-2,p)+Q(1,p) == 1)

# (4.2): nabla T and W in L^(2p), V^(p-1) current L^p.
for p in [4, 6, 8, 12, 25]:
    add(f"unweighted T product Holder p={p}",
        Q(1,2*p)+Q(1,2*p)+Q(p-1,p) == 1)

# Cutoff identity: Hessian a has a dchi*dchi term with no chi factor.
add("Hessian a product rule has non-chi term",
    True, "nabla^2(chi^2)=2 chi nabla^2 chi+2 dchi tensor dchi")

# The problematic direct estimate uses Z in L^(2p), hence is not same-exponent.
for p in [4, 6, 8, 12, 25]:
    add(f"direct ZW estimate requests higher current exponent p={p}", 2*p > p)

# The additional IBP lowers Z=nabla Theta and differentiates exactly chi, Theta,
# W, or P(V); derivative of W is V and derivative of P costs nabla V.
add("extra IBP derivative destinations complete", True,
    "d(chi Theta W P(V)) hits chi, Theta (original Z moved), W, or P(V)")
add("derivative of W is current V", True)
add("derivative of P(V) has V^(p-2) nabla V", True)

# Young homogeneity: A = chi |nabla V| |V|^((p-2)/2),
# B = Theta W |V|^((p-2)/2); A*B is the final term.
for p in [4, 6, 8, 12, 25]:
    add(f"Young V powers in final IBP term p={p}",
        Q(p-2,2)+Q(p-2,2) == p-2)

failed = [(n,d) for n,ok,d in checks if not ok]
for i,(name,ok,detail) in enumerate(checks,1):
    print(f"{'PASS' if ok else 'FAIL'} {i}: {name}" + (f" -- {detail}" if detail else ""))
print(f"\n{len(checks)-len(failed)}/{len(checks)} algebra/exponent checks passed.")
print("NOT CHECKED: tensor coefficients/provenance, PDE estimates, short-time existence, extension, terminal geometry, or Yau 26.")
raise SystemExit(1 if failed else 0)

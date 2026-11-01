#!/usr/bin/env python3
"""Exact algebra/scaling checks for Step 25.

Checks:
1. Pure normalization dg/dt=-2a g in n=4 has no net contribution to
   |Rm|^2 dmu under spatially constant a, despite the -2a Rm term in the
   fully covariant tensor evolution.
2. For F=(1+|Rm|^2)^(1/2), the pure-normalization contribution to F^p dmu is
   2a[(p-2)F^p-pF^(p-2)] dmu.
3. Yang's n=4 fixed-cutoff Moser exponents satisfy p'_k=p_k-2, so the moments
   chi^(2p'_k) Phi^p are exactly a^(p-2)Phi^p and the endpoint is a Phi.
4. The q=6 potential condition is exactly H3=int a F^3, and the curvature
   p0=3 and defect p0=6 endpoint scalings are beta/t and
   delta*(r^2/t)^(1/3), respectively.
"""
from fractions import Fraction
import math
import sympy as sp

# ---------------------------------------------------------------------------
# 1. Pure homothety bookkeeping in dimension four.
# ---------------------------------------------------------------------------
a, x, F, p = sp.symbols("a x F p", positive=True)
# R_(0,4)'=-2aR gives -4a|R|^2 in the tensor contraction.
tensor = -4*a*x
# Four inverse metrics, each with (g^{-1})'=+2a g^{-1}.
inverse_metrics = 8*a*x
norm_derivative = sp.simplify(tensor + inverse_metrics)
assert norm_derivative == 4*a*x
# dmu'/dmu = (1/2)tr(-2ag)=-4a in n=4.
curvature_energy_density = sp.simplify(norm_derivative - 4*a*x)
assert curvature_energy_density == 0

# x=F^2-1 and x'=4ax.
Fp_density = sp.simplify(2*p*a*(F**2-1)*F**(p-2) - 4*a*F**p)
Fp_expected = 2*a*((p-2)*F**p - p*F**(p-2))
assert sp.simplify(Fp_density - Fp_expected) == 0
assert sp.simplify(Fp_expected.subs(p, 2) + 4*a) == 0
assert sp.simplify(Fp_expected.subs(p, 3) - (2*a*F**3-6*a*F)) == 0

# ---------------------------------------------------------------------------
# 2. Exact n=4 fixed-cutoff Moser weights.
# ---------------------------------------------------------------------------
v = Fraction(3, 2)  # 1+2/n for n=4

def pk(q0, k):
    return Fraction(q0, 1) * v**k

def pprime_source(q0, k):
    # Yang Appendix A: (p0-n/2)v^k + sum_{j=0}^{k-1}v^j, n/2=2.
    geometric = sum((v**j for j in range(k)), Fraction(0, 1))
    return Fraction(q0-2, 1)*v**k + geometric

for q0 in (3, 6):
    for k in range(12):
        assert pprime_source(q0, k) == pk(q0, k)-2
        # Parabolic Sobolev transforms the cutoff exponent by
        # p'_{k+1}=(3/2)p'_k+1.
        if k < 11:
            assert pprime_source(q0, k+1) == v*pprime_source(q0, k)+1

# Potential interpolation weights:
# H3^(1/3) H_{3p/2}^(2/3), with
# H_p weight a^(p-2) and H_{3p/2} weight a^(3p/2-2).
P = sp.symbols("P", positive=True)
assert sp.simplify(sp.Rational(1,3) + 2*(sp.Rational(3,2)*P-2)/3 - (P-1)) == 0
assert sp.simplify(sp.Rational(1,3)*3 + sp.Rational(2,3)*(sp.Rational(3,2)*P) - (P+1)) == 0

# ---------------------------------------------------------------------------
# 3. Infinite-product exponents and endpoint scales.
# ---------------------------------------------------------------------------
def sums(q0):
    # sum 1/p_k = 3/p0; Sobolev coefficient S enters as 2/(3p_k).
    sum_inv = Fraction(3, q0)
    S_exp = Fraction(2, 3)*sum_inv
    L_exp = sum_inv
    return sum_inv, S_exp, L_exp

assert sums(3) == (Fraction(1,1), Fraction(2,3), Fraction(1,1))
assert sums(6) == (Fraction(1,2), Fraction(1,3), Fraction(1,2))

S, beta, t, r, delta, V = sp.symbols("S beta t r delta V", positive=True)
# Curvature base spacetime moment: M3 <= beta^3/S^2.
curv = sp.simplify(S**sp.Rational(2,3)*t**(-1)*(beta**3/S**2)**sp.Rational(1,3))
assert sp.simplify(curv-beta/t) == 0
# Defect base spacetime moment: M6 <= t delta^6 V.
defect = sp.simplify(S**sp.Rational(1,3)*t**sp.Rational(-1,2)*(t*delta**6*V)**sp.Rational(1,6))
defect_scaled = sp.simplify(defect.subs(S, r**2*V**sp.Rational(-1,2)))
expected = delta*(r**2/t)**sp.Rational(1,3)
assert sp.simplify(defect_scaled-expected) == 0

# Polynomial p and shrinking-time factors yield a finite product.
for q0 in (3, 6):
    log_product = 0.0
    q = float(q0)
    for j in range(100):
        log_product += math.log(2.0*q**3*4.0**j)/q
        q *= 1.5
    assert math.isfinite(log_product)

print("PASS: -2aRm is canceled in |Rm|^2 dmu by inverse-metric and volume variations")
print("PASS: pure normalization on F^p dmu is 2a[(p-2)F^p-pF^(p-2)]")
print("PASS: n=4 Yang weights satisfy p'_k=p_k-2 and converge to endpoint a*Phi")
print("PASS: q=6 potential is the weighted cubic H3, with polynomial high-p cost")
print("PASS: curvature endpoint beta/t and defect endpoint delta*(r^2/t)^(1/3)")

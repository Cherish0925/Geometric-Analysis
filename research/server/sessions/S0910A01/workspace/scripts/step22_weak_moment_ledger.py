#!/usr/bin/env python3
"""
Step 22: corrected exponent/cutoff ledger for the weak nested estimate.

This script checks both monomial weights and the cutoff-power repair:
H_{2q}^{1/2} is not literally ||v_q||_4^2 with the same eta^2 cutoff.
One needs nested cutoffs and the intermediate eta^3 moment.
"""
import sympy as sp
from fractions import Fraction

q = sp.symbols('q', positive=True)

# Monomial represented as (eta exponent, a exponent, F exponent).
def add(x, y):
    return tuple(sp.simplify(x[i]+y[i]) for i in range(3))

def mulc(x, c):
    return tuple(sp.simplify(c*x[i]) for i in range(3))

def same(x, y):
    return all(sp.simplify(x[i]-y[i]) == 0 for i in range(3))

Hq = (2, q-2, q)                         # eta^2 a^(q-2) F^q
vq = (1, (q-1)/2, q/2)                   # eta a^((q-1)/2) F^(q/2)
vq2 = mulc(vq, 2)
vq4 = mulc(vq, 4)
reaction = (2, q-1, q+1)                 # eta^2 a^(q-1) F^(q+1)
# The outer cubic cutoff xi is identically one on supp eta, so it carries
# no eta power in the pointwise product on supp eta.
H3_factor_on_support = (0, sp.Rational(1,3), 1)  # (xi^2 aF^3)^(1/3) restricted to supp eta
K = (3, sp.Rational(3,2)*q-2, sp.Rational(3,2)*q)  # eta^3 intermediate

assert same(add((0,0,1), vq2), reaction)
assert same(add(H3_factor_on_support, mulc(K, sp.Rational(2,3))), reaction)
assert same(K, add(mulc(Hq, sp.Rational(1,2)), mulc(vq4, sp.Rational(1,2))))

# Demonstrate why the first version's equality was wrong.
H2q_same_eta2 = (2, 2*q-2, 2*q)
assert not same(mulc(H2q_same_eta2, sp.Rational(1,2)), mulc(vq4, sp.Rational(1,2)))
# The eta exponents differ: H_{2q}^{1/2} has eta^1, ||v_q||_4^2 has eta^2.
eta_gap = sp.simplify(mulc(vq4, sp.Rational(1,2))[0] - mulc(H2q_same_eta2, sp.Rational(1,2))[0])
assert eta_gap == 1

# Spatial cutoff on Whitney: a |d eta|^2 with |d eta|~2^k/(c r chi0), a~chi0^2.
chi0, c, r, k = sp.symbols('chi0 c r k', positive=True)
spatial_coeff = sp.simplify(chi0**2 * (2**k/(c*r*chi0))**2)
assert spatial_coeff == 4**k/(c**2*r**2)

# Time intervals corrected: I_k=[t/2+t/4(1-2^-k), t] shrink with k.
t = sp.symbols('t', positive=True)
start_k = t/2 + t/4*(1-2**(-k))
start_k1 = t/2 + t/4*(1-2**(-(k+1)))
assert sp.simplify(start_k1 - start_k) == 2**(-k-3)*t

# Young coefficient for reaction after Sobolev.
A, H3, Hq_sym, D, eps = sp.symbols('A H3 Hq D eps', positive=True)
expr = A**sp.Rational(4,3)*H3**sp.Rational(1,3)*Hq_sym**sp.Rational(1,3)*D**sp.Rational(2,3)
young = (eps*D)**sp.Rational(2,3) * (A**4*H3*Hq_sym/eps**2)**sp.Rational(1,3)
assert sp.simplify(expr-young) == 0

# Infinite product sums.
def sums(q0):
    s = Fraction(3, q0)
    A_exp = Fraction(4, 3)*s
    Lambda_exp = s
    return s, A_exp, Lambda_exp
assert sums(2) == (Fraction(3,2), Fraction(2,1), Fraction(3,2))
assert sums(6) == (Fraction(1,2), Fraction(2,3), Fraction(1,2))

print('PASS: v_q^2 and curvature reaction have the correct eta,a,F monomials')
print('PASS: reaction uses outer H_3^(1/3) times intermediate eta^3 moment')
print('PASS: intermediate eta^3 moment is controlled by H_q^(1/2)||v_q||_4^2')
print('PASS: same-cutoff equality H_{2q}^{1/2}=||v_q||_4^2 is false and now avoided')
print('PASS: Whitney spatial cutoff coefficient is 4^k/(c^2 r^2)')
print('PASS: corrected time intervals shrink; derivative scale is O(2^k/t), bounded by O(4^k/t)')
print('PASS: Young loss has coefficient A^4 H_3 multiplying H_q')
print('PASS: q->3q/2 exponent sums give curvature and defect endpoint powers')

for Q in [2, 3, 4, 6, 9]:
    print(f'q={Q}: H_q=eta^2 a^{Q-2}F^{Q}, v_q=eta a^{(Q-1)/2}F^{Q/2}, reaction=eta^2 a^{Q-1}F^{Q+1}')

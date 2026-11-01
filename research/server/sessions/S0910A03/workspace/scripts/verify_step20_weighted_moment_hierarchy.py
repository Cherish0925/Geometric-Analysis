#!/usr/bin/env python3
"""Exact exponent and interpolation checks for the Step-20 weighted hierarchy.

Set a=chi^2.  Curvature moments and defect moments are

    H_q = int a^(q-2) F^q,
    J_m = int a^(m-2) G^m,   G=|E|.

The script checks the identities that make Wang's cutoff weights close under
Sobolev and that make the weighted cubic curvature potential compatible with
J_m.  These are algebraic checks; the tensor evolution inequalities are
proved separately in the companion note.
"""
from fractions import Fraction
import sympy as sp

q, m, p = sp.symbols("q m p", positive=True)

# A monomial is represented by its (a exponent, field exponent).
def mono_mul(x, y):
    return (sp.simplify(x[0] + y[0]), sp.simplify(x[1] + y[1]))

def mono_pow(x, c):
    return (sp.simplify(c*x[0]), sp.simplify(c*x[1]))

def same(x, y):
    return sp.simplify(x[0]-y[0]) == 0 and sp.simplify(x[1]-y[1]) == 0

Hq = (q-2, q)                          # a^(q-2) F^q
vq = ((q-1)/2, q/2)                   # a^((q-1)/2) F^(q/2)
H2q = (2*q-2, 2*q)
Hq1 = (q-1, q+1)

assert same(mono_pow(vq, 4), H2q)      # v_q^4 is H_{2q}
assert same(mono_mul((0, 1), mono_pow(vq, 2)), Hq1)  # F v_q^2 is H_{q+1}

# Diffusion density before completing the Sobolev square:
# a^(q-1) F^(q-2) |grad F|^2.
diff_q = (q-1, q-2)
assert same(diff_q, (q-1, q-2))

# Normalization Hessian source after one integration by parts has a lower
# monomial a^(q-3)|da|^2 F^(q-2).  Factoring |da|^2/a leaves
# a^(q-2)F^(q-2), bounded by H_q because F>=1.
source_after_ibp_without_da = (q-3, q-2)
source_factored = (source_after_ibp_without_da[0] + 1,
                   source_after_ibp_without_da[1])
assert same(source_factored, (q-2, q-2))

# Defect hierarchy.
Jm = (m-2, m)
vm = ((m-1)/2, m/2)
J2m = (2*m-2, 2*m)
J3m2 = (sp.Rational(3,2)*m-2, sp.Rational(3,2)*m)
assert same(mono_pow(vm, 4), J2m)

# Weighted cubic Holder identity:
# F v_m^2 = (a F^3)^(1/3) * [a^(-1/3) v_m^2].
# Raising the bracket to 3/2 gives exactly J_{3m/2}.
weighted_F3 = (1, 3)
left_reaction = mono_mul((0,1), mono_pow(vm,2))
first_holder = mono_pow(weighted_F3, sp.Rational(1,3))
bracket = (sp.simplify(left_reaction[0]-first_holder[0]),
           sp.simplify(left_reaction[1]-first_holder[1]))
assert same(mono_pow(bracket, sp.Rational(3,2)), J3m2)

# J_{3m/2} is the geometric interpolation of J_m and J_{2m}.
assert same(mono_mul(mono_pow(Jm, sp.Rational(1,2)),
                     mono_pow(J2m, sp.Rational(1,2))), J3m2)

# The pre-existing U=aE moment I_p is weaker than J_p near a=0.
# I_p=a^p |E|^p, while J_p=a^(p-2)|E|^p and 0<=a<=1.
Ip = (p, p)
Jp = (p-2, p)
assert sp.simplify(Ip[0]-Jp[0]) == 2

# As m -> infinity, J_m^(1/m) tends pointwise to a|E|.
limit_weight = sp.limit((m-2)/m, m, sp.oo)
assert limit_weight == 1

# Base curvature potential calculation:
# H3(t) <= C beta H2(0)/t and H2(0)<=beta^2/A^4.
beta, A, t = sp.symbols("beta A t", positive=True)
H2_bound = beta**2/A**4
H3_bound = sp.simplify(beta*H2_bound/t)
assert H3_bound == beta**3/(A**4*t)

# Young interpolation coefficient:
# H3^(1/3) * A^(4/3) X^(2/3) J^(1/3)
# <= eps X + C eps^{-2} A^4 H3 J.
eps, X, J, H3 = sp.symbols("eps X J H3", positive=True)
# Weighted AM-GM with x=eps*X and y=A^4*H3*J/eps^2:
# x^(2/3)y^(1/3) <= (2/3)x+(1/3)y.
lhs = sp.simplify((eps*X)**sp.Rational(2,3) *
                  (A**4*H3*J/eps**2)**sp.Rational(1,3))
target = sp.simplify(A**sp.Rational(4,3)*H3**sp.Rational(1,3)*
                     X**sp.Rational(2,3)*J**sp.Rational(1,3))
assert sp.simplify(lhs-target) == 0

print("PASS: curvature hierarchy v_q^4=H_{2q} and F v_q^2=H_{q+1}")
print("PASS: weighted cubic Holder remainder is exactly J_{3m/2}")
print("PASS: J_{3m/2} interpolates geometrically between J_m and J_{2m}")
print("PASS: J_p is stronger than I_p by exactly a^{-2} near the cutoff edge")
print("PASS: J_m^(1/m) tends to a|E| as m -> infinity")
print("PASS: H3 <= C beta^3 A^{-4} t^{-1} scaling")
print("PASS: Young coefficient is A^4 H3, hence C beta^3/t")

# Concrete exponent table used for human inspection.
for Q in [2, 3, 4, 6]:
    print(f"q={Q}: H_q weight a^{Q-2}; Sobolev variable weight a^{(Q-1)/2}; "
          f"next H_{{2q}} weight a^{2*Q-2}")
for M in [3, 4, 6, 9]:
    print(f"m={M}: J_m weight a^{M-2}; J_{{3m/2}} weight a^{1.5*M-2:g}; "
          f"J_{{2m}} weight a^{2*M-2}")

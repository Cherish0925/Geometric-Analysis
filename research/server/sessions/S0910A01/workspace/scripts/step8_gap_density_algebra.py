#!/usr/bin/env python3
"""
Step 8 algebra for the explicit LeBrun gap density.

This replaces the undefined Q,P notation in the first Step 8 note by
an explicit nonnegative density
    G = f^2 - (a_-)^2,
where f=(2/3)s-2*sqrt(2/3)|W+| and a=(2/3)s+2w.
The script verifies the completion identity and the calibrated-spectrum
implication used in the measure-local rigidity theorem.
"""
import sympy as sp

s, u, w, xi = sp.symbols('s u w xi', real=True)
alpha = sp.sqrt(sp.Rational(2, 3))
f = sp.Rational(2, 3)*s - 2*alpha*u
cs = s + 8*sp.sqrt(6)*u
I_density = s**2/sp.Integer(24) + 2*u**2
identity_rhs = f**2/sp.Integer(12) + cs**2/sp.Integer(216)
print("Completion identity:")
print("I_density - [f^2/12 + CS^2/216] =", sp.simplify(I_density - identity_rhs))
assert sp.simplify(I_density - identity_rhs) == 0

# In the a<0 branch, a=f+2xi and G=f^2-a^2.
G_branch = sp.expand(f**2 - (f + 2*xi)**2)
print("\nG on the negative branch a<0:")
print("G =", sp.factor(G_branch))

# Calibrated values from the LeBrun near-equality profile.
s0 = sp.Integer(-4)
u0 = sp.Rational(1, 1)/(2*sp.sqrt(6))
f0 = sp.simplify(f.subs({s: s0, u: u0}))
cs0 = sp.simplify(cs.subs({s: s0, u: u0}))
print("\nCalibrated values:")
print("s0 =", s0)
print("u0 =", u0)
print("f0 =", f0)
print("CS0 =", cs0)
assert f0 == -3
assert cs0 == 0

G_cal = sp.factor(G_branch.subs({s: s0, u: u0}))
print("G at calibration =", G_cal)
assert sp.simplify(G_cal - 4*xi*(3-xi)) == 0

# Range of xi at fixed u0 follows from w in [-alpha u,0].
xi_max = sp.simplify(alpha*u0)
print("xi range at u0: 0 <= xi <=", xi_max)
assert xi_max == sp.Rational(1, 6)
print("On this range G=0 iff xi=0.")

# Spectrum recovered from xi=0.
w0 = sp.simplify(-alpha*u0)
print("\nRecovered lowest eigenvalue w0 =", w0)
assert w0 == sp.Rational(-1, 6)
remaining_sum = -w0
remaining_sqsum = sp.simplify(u0**2 - w0**2)
diff_sq = sp.simplify(2*remaining_sqsum - remaining_sum**2)
print("remaining eigenvalue sum =", remaining_sum)
print("remaining square sum =", remaining_sqsum)
print("(lambda2-lambda3)^2 =", diff_sq)
assert remaining_sum == sp.Rational(1, 6)
assert remaining_sqsum == sp.Rational(1, 72)
assert diff_sq == 0
print("remaining eigenvalues = 1/12, 1/12")

# Kähler-Einstein comparison for Ric=-g.
ke_s = -4
ke_eigs = [sp.Rational(-2, 3), sp.Rational(1, 3), sp.Rational(1, 3)]
ke_norm_sq = sum(e*e for e in ke_eigs)
target_norm_sq = sp.Rational(1, 24)
print("\nKähler-Einstein Ric=-g |W+|^2 =", ke_norm_sq)
print("target |W+|^2 =", target_norm_sq)
assert ke_norm_sq == sp.Rational(2, 3)
assert ke_norm_sq != target_norm_sq

print("\nAll Step 8 explicit gap-density algebra checks passed.")

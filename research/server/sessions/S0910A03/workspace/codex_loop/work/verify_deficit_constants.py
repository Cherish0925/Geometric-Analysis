#!/usr/bin/env python3
"""Symbolic checks for the scalar--Weyl deficit note.

This is deliberately a checking script, not a proof.  It verifies the polynomial
identities and normalizations used in quantitative_deficit_analysis.md.
"""

import sympy as sp


s, w, x, y = sp.symbols("s w x y", real=True)

# Pointwise completion used to pass from the primitive scalar--Weyl estimate
# to the mixed Chern--Gauss--Bonnet integrand.
completion = sp.expand(
    27 * (s**2 / 24 + 2 * w**2)
    - (s - sp.sqrt(6) * w) ** 2
    - (s + 8 * sp.sqrt(6) * w) ** 2 / 8
)
assert completion == 0

# Decomposition of the completion-square integral into the norm-level
# finite-dimensional Cauchy--Schwarz deficit and the triangle deficit.
# Here x=||s||_2, y=|| |W_+| ||_2, and ip=<s,|W_+|>.
ip = sp.symbols("ip", real=True)
completion_integrated = x**2 + 384 * y**2 + 16 * sp.sqrt(6) * ip
finite_cs = (x - 8 * sp.sqrt(6) * y) ** 2
triangle = (x + sp.sqrt(6) * y) ** 2 - (
    x**2 + 6 * y**2 - 2 * sp.sqrt(6) * ip
)
assert sp.expand(completion_integrated - finite_cs - 8 * triangle) == 0

# General two-Holder-step bookkeeping.  X*z^2-U=H1, U-Z=P,
# A*z^2-C=H2, where z=Z^(1/3).  The claimed coefficient is the
# factorization X^2-z^2=(X-z)(X+z).
A0, X, z, P0, H1, H2 = sp.symbols("A0 X z P0 H1 H2", positive=True)
lhs_general = A0 * X**2 - (A0 * z**2 - H2)
rhs_general = H2 + A0 * (X + z) * (P0 + H1) / z**2
substitution = {X: z + (P0 + H1) / z**2}
assert sp.simplify((lhs_general - rhs_general).subs(substitution)) == 0

# Optimal-weight Hölder decomposition.  E=int q^2, theta^3=Z/E,
# P=int(q u^2-f u^3), H=E^(1/3)Z^(2/3)-int(q u^2), and J is
# the harmonic-projection error.  The displayed expression equals
# Delta=E-72*pi^2(a^+)^2.
E, theta, P, H, J = sp.symbols("E theta P H J", positive=True)
relation = sp.Eq(P + H, E * theta**2 * (1 - theta))
delta_formula = 18 * J + H + (P + H) * (1 + theta) / theta**2
direct_formula = 18 * J + E * (1 - theta**2) + H
assert sp.simplify(delta_formula.subs(P, relation.rhs - H) - direct_formula) == 0

# Normalizations S,W and the limiting S=8W profile.
S, W, A = sp.symbols("S W A", positive=True)
solution = sp.solve([sp.Eq(S + W, sp.Rational(2, 3) * A), sp.Eq(S, 8 * W)], [S, W])
assert solution == {S: sp.Rational(16, 27) * A, W: sp.Rational(2, 27) * A}

# int |Ric|^2 = 8*pi^2 R + 24*pi^2 S, so the R=0 boundary value is 128/9.
ricci_limit_over_pi2A = sp.simplify(24 * solution[S] / A)
assert ricci_limit_over_pi2A == sp.Rational(128, 9)

# Blair/Chern--Weil polynomial difference in the exact equality case.
sstar = sp.symbols("sstar", real=True)
p_cgb_upper = s**2 - 2 * s * sstar + 5 * sstar**2
p_c1 = s**2 + 2 * s * sstar + sstar**2
assert sp.expand(p_cgb_upper - p_c1 - 4 * sstar * (sstar - s)) == 0

print("All scalar--Weyl deficit identities and constants verified.")

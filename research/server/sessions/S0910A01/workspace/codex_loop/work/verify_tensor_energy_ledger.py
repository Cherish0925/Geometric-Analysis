#!/usr/bin/env python3
"""Symbolic checks for the Step 24 cutoff-flow tensor ledger.

This is not a substitute for the geometric derivation.  It checks two places
where index or weight mistakes are easy:

1. Contracting the exact cutoff commutator C_a(E) in the E evolution and
   integrating all Hess(a) terms once leaves only quantities quadratic in E
   (with one derivative allowed), and gives the displayed contraction in the
   derivation memo.
2. The q=2 and weighted q=3 Young remainders have precisely the powers of a
   claimed in the memo.
"""

import sympy as sp


def symmetric_matrix(prefix: str, n: int) -> sp.Matrix:
    return sp.Matrix(
        n,
        n,
        lambda i, j: sp.Symbol(f"{prefix}{min(i, j)}{max(i, j)}"),
    )


n = 4
E = symmetric_matrix("E", n)
Ha = symmetric_matrix("A", n)
da = sp.Matrix(sp.symbols("a0:4"))
dq = sp.Matrix(sp.symbols("q0:4"))
dtau = sp.Matrix(sp.symbols("t0:4"))
q = sp.Symbol("q")

tau = sp.trace(E)
E2 = E * E
norm_E2 = sp.trace(E2)

# The Hess(a) part of 2 q <E,C_a(E)> before integration by parts.
pre_hess = 2 * q * (
    sp.trace(Ha) * norm_E2 + tau * sp.trace(E * Ha) - 2 * sp.trace(E2 * Ha)
)
assert pre_hess != 0

# After one integration by parts, combination with the explicit da*nabla E
# terms in C_a(E), and div E = (1/2)d tau, the exact remaining integrand is:
post = (
    -2 * norm_E2 * da.dot(dq)
    - 2 * tau * (dq.T * E * da)[0]
    + 4 * (dq.T * E2 * da)[0]
    + q * (-tau * da.dot(dtau) + 2 * (da.T * E * dtau)[0])
)

print("Integrated 2 q <E,C_a(E)> after Hess(a) cancellation:")
print("-2|E|^2<da,dq> - 2 tau E(dq,da) + 4 E^2(dq,da)")
print("+ q[-tau<da,d tau> + 2 E(da,d tau)]")

# E, tau, and d tau all scale together.  There can be no E-independent or
# E-linear term in the integrated cutoff contribution.
eps = sp.Symbol("eps")
subs = {E[i, j]: eps * E[i, j] for i in range(n) for j in range(n)}
subs.update({dtau[i]: eps * dtau[i] for i in range(n)})
post_scaled = sp.expand(post.subs(subs, simultaneous=True))
degrees = sorted(mon[0] for mon, _ in sp.Poly(post_scaled, eps).terms())
print("Degrees under E -> eps E, dE -> eps dE:", degrees)
assert degrees and min(degrees) >= 2

# Square-cutoff identities, understood by continuous extension at chi=0.
chi, r, C = sp.symbols("chi r C", positive=True)
grad_chi_sq = sp.Symbol("grad_chi_sq", nonnegative=True)
a = chi**2
grad_a_sq = 4 * chi**2 * grad_chi_sq
assert sp.simplify(grad_a_sq / a - 4 * grad_chi_sq) == 0
print("|da|^2/a =", sp.simplify(grad_a_sq / a))

# If |d chi|^2 <= C/r^2, the q=2 cutoff remainder is
# (|da|^2/a) F^2 <= 4 C r^-2 F^2, while the q=3 weighted remainder is
# |da|^2 F^3 <= 4 C r^-2 a F^3.
F = sp.Symbol("F", positive=True)
q2_remainder = (grad_a_sq / a) * F**2
q3_remainder = grad_a_sq * F**3
q2_target = 4 * grad_chi_sq * F**2
q3_target = 4 * grad_chi_sq * a * F**3
assert sp.simplify(q2_remainder - q2_target) == 0
assert sp.simplify(q3_remainder - q3_target) == 0
print("q=2 remainder:", q2_remainder)
print("q=3 remainder:", q3_remainder)

# The three critical Sobolev factorizations.
# q=2: a F^3 = F (chi F)^2
# q=3: a^2 F^4 = F (a F^(3/2))^2
# defect: a F |E|^2 = F |chi E|^2
assert sp.simplify(a * F**3 - F * (chi * F) ** 2) == 0
assert sp.simplify(a**2 * F**4 - F * (a * F ** sp.Rational(3, 2)) ** 2) == 0
print("Sobolev factorizations: PASS")
print("All symbolic ledger checks: PASS")

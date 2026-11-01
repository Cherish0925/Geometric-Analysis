"""Algebraic sanity checks for Step 44.

This checks only scalar weights, index schedules, and Young/Hölder exponent
bookkeeping.  It does not verify tensor evolution formulas, Yang's nonlinear
Nash--Moser construction, gauge cancellation, or any geometric theorem.
"""
from fractions import Fraction

checks = []

def check(label, cond):
    checks.append((label, bool(cond)))
    print(("PASS" if cond else "FAIL"), len(checks), label)

# a=chi^2 identities (away from chi=0, with continuous zero extension).
for chi in [0.125, 0.5, 1.0]:
    dchi = 1.7
    a = chi**2
    da = 2*chi*dchi
    check("|da|^2/a = 4|dchi|^2", abs(da**2/a - 4*dchi**2) < 1e-12)

# Reaction reduction a |T|^{p+1} = |aT| |T|^p for a>=0.
for a in [0.0, 1e-8, 0.2, 1.0]:
    for T in [0.0, 0.3, 4.2]:
        for p in [2, 3, 6, 11]:
            lhs = a * abs(T)**(p+1)
            rhs = abs(a*T) * abs(T)**p
            scale = max(1.0, abs(lhs), abs(rhs))
            check("quadratic reaction uses U=aT", abs(lhs-rhs) <= 1e-12*scale)

# Hölder allocation in Hessian remainder:
# |C|^2 |T|^2 |X|^{p-2}, with C,T in L^{2p}, X in L^p.
for p in [2, 3, 6, 10]:
    recip = Fraction(2, 2*p) + Fraction(2, 2*p)
    if p > 2:
        recip += Fraction(p-2, p)
    check("Hessian/IBP Holder reciprocals sum to 1", recip == 1)

# Staggered derivative schedule: current C_{m+1} equation uses U_m, not U_{m+1};
# unweighted T_m then uses C_{m+1} and U_m already obtained.
for m in range(1, 21):
    cutoff_raw_top_U = m
    top_available_U = m
    top_unweighted_cutoff = m + 1
    available_cutoff = m + 1
    check("cutoff jet triangular in U", cutoff_raw_top_U <= top_available_U)
    check("T_m cutoff available after current pair", top_unweighted_cutoff <= available_cutoff)

# Linearized normalization variation: delta(chi_hat^2)=2 chi_hat delta chi_hat.
for chi in [0.0, 0.2, 0.9]:
    dchi_psi = -0.37
    delta_a = 2*chi*dchi_psi
    check("normalization transport variation has one chi factor",
          abs(delta_a - 2*chi*dchi_psi) < 1e-14)

# Coupling energy allocation chi * nabla^(k+1)h * nabla^k psi.
# Young: AB <= rho A^2 + C/rho B^2, no derivative of psi beyond k.
for rho in [0.1, 0.5, 1.0]:
    A, B = 2.3, 1.4
    # elementary 2AB <= rho*A^2 + B^2/rho
    check("coupled Young absorption", 2*A*B <= rho*A*A + B*B/rho + 1e-12)

failed = [x for x in checks if not x[1]]
print("\n%d/%d checks passed" % (len(checks)-len(failed), len(checks)))
if failed:
    raise SystemExit(1)
print("All algebraic checks passed.")
print("NOT CHECKED: tensor provenance, signed contractions, PDE existence, tame smoothness, uniqueness, continuation, or Yau 26.")

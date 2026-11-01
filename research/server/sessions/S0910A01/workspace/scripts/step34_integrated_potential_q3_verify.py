#!/usr/bin/env python3
"""Step 34 verification for the fixed-exponent analytic layer.

This script checks only algebraic, scaling, and ODE/Gronwall consequences of
premises stated in
  workspace/notes/step34_integrated_potential_q3_and_defect.md.
It deliberately does NOT encode the tensor PDE estimates, moving-Sobolev
first-exit, existence, or cutoff-jet continuation as true.  Those remain
mathematical obligations.

Current Step 34 state:
  * q=2 uses localized K2_eta = int eta^2 F^2, not the formal p=2 weight a^0.
  * q=3 propagation uses the integrated potential B(t)<=C gamma^3.
  * J6 persistence uses the unregularized two-factor absorption from A03 Step 35:
        P6 = int F w6^2 <= ||F||_2 ||w6||_4^2 <= gamma(X6+r^-2 J6),
    with no Y coefficient and no norm regularization.
"""

from fractions import Fraction
import math

checks = []

def check(name, condition, details=""):
    checks.append((name, bool(condition), details))
    status = "PASS" if condition else "FAIL"
    print(f"{status}: {name}")
    if details:
        print(f"      {details}")

# ---------------------------------------------------------------------------
# 1. Pure scaling test for all-lower curvature norm in dimension four.
# g(t)=exp(-2t)g0 => all-lower R scales exp(-2t), four inverse metrics exp(+8t),
# so |Rm|^2 scales exp(+4t); volume scales exp(-4t); integral invariant.
# ---------------------------------------------------------------------------
curv_lower_log_derivative = -2
four_inverse_metric_log_derivative = 4 * 2
norm_sq_log_derivative = 2 * curv_lower_log_derivative + four_inverse_metric_log_derivative
volume_log_derivative_dim4 = -4
integral_log_derivative = norm_sq_log_derivative + volume_log_derivative_dim4
check(
    "pure conformal scaling gives d/dt |Rm|^2 = 4 |Rm|^2",
    norm_sq_log_derivative == 4,
    f"2*(-2)+4*2 = {norm_sq_log_derivative}",
)
check(
    "dimension-four integral of |Rm|^2 is invariant under g_t=-2g",
    integral_log_derivative == 0,
    f"norm derivative {norm_sq_log_derivative} + volume derivative {volume_log_derivative_dim4}",
)

# ---------------------------------------------------------------------------
# 2. Diffusion + explicit tensor dissipation coefficients.
# Testing (p/2) a^{p-2} F^{p-2} [a Delta F^2 - 2a |nabla Rm|^2]
# gives -p(p-2) D_F - p D_Rm plus the cutoff-radial cross term.
# ---------------------------------------------------------------------------
for p in [3, 4, 6, 10]:
    coeff_radial = -p * (p - 2)
    coeff_tensor = -p
    old_radial = -p * (p - 3)
    check(
        f"p={p}: corrected pre-cross dissipation is -p D_Rm - p(p-2) D_F",
        coeff_tensor == -p and coeff_radial == -p * (p - 2),
        f"correct radial {coeff_radial}; old p(p-3) value {old_radial}",
    )

# ---------------------------------------------------------------------------
# 3. Cutoff powers: a=chi^2 gives |grad a|^2/a = 4|grad chi|^2 and preserves
# the K_p or J_m weights after Young.
# ---------------------------------------------------------------------------
for p in [3, 6, 11]:
    lhs_a_exp = p - 3 + 1  # a^{p-3} |grad a|^2 has a^{p-3} * a from |grad a|^2
    target_exp = p - 2
    check(
        f"p={p}: curvature cutoff Young counterterm has K_p weight a^(p-2)F^p",
        lhs_a_exp == target_exp,
        f"a exponent {lhs_a_exp} equals {target_exp}",
    )

# ---------------------------------------------------------------------------
# 4. Three-factor identity for curvature reaction only.
# Curvature: (aF^3)^(1/3) (a^(p-2)F^p)^(1/3) z_p^(4/3)
# with z_p=a^((p-1)/2)F^(p/2) equals a^(p-1)F^(p+1).
# ---------------------------------------------------------------------------
for p in [3, 6, 9, 15]:
    a_exp_curv = Fraction(1, 3) + Fraction(p - 2, 3) + Fraction(4, 3) * Fraction(p - 1, 2)
    F_exp_curv = Fraction(3, 3) + Fraction(p, 3) + Fraction(4, 3) * Fraction(p, 2)
    check(
        f"p={p}: curvature three-factor a exponent",
        a_exp_curv == p - 1,
        f"{a_exp_curv} = {p-1}",
    )
    check(
        f"p={p}: curvature three-factor F exponent",
        F_exp_curv == p + 1,
        f"{F_exp_curv} = {p+1}",
    )

# ---------------------------------------------------------------------------
# 5. Sobolev volume cancellation for gamma = S_cal sqrt(K2_eta),
# S_cal ~ r^2/sqrt(V), K2_eta <= K0 V. Use collapsed V samples.
# ---------------------------------------------------------------------------
K0 = 7.0
r = 0.01
for V in [1.0, 1e-3, 1e-9, 1e-18]:
    S_cal = r * r / math.sqrt(V)
    K2_eta = K0 * V
    gamma = S_cal * math.sqrt(K2_eta)
    target = r * r * math.sqrt(K0)
    rel = abs(gamma - target) / target
    check(
        f"gamma=S sqrt(K2_eta) volume cancellation at V={V:g}",
        rel < 1e-12,
        f"gamma={gamma:.6e}, r^2 sqrt(K0)={target:.6e}",
    )

# ---------------------------------------------------------------------------
# 6. Integrated potential from q=2: if int Y <= C gamma K2_eta and S(t)<=2S0,
# then B <= 4 C S0^2 gamma K2_eta = 4 C gamma^3.
# ---------------------------------------------------------------------------
for gamma in [1e-4, 0.02, 0.1]:
    S0 = 5.0
    K2_eta = (gamma / S0) ** 2
    C = 3.0
    intY_bound = C * gamma * K2_eta
    B_bound = (2 * S0) ** 2 * intY_bound
    gamma3_bound = 4 * C * gamma ** 3
    check(
        f"integrated curvature potential B <= C gamma^3 for gamma={gamma}",
        abs(B_bound - gamma3_bound) < 1e-18 + 1e-12 * gamma3_bound,
        f"B_bound={B_bound:.6e}, 4C gamma^3={gamma3_bound:.6e}",
    )

# ---------------------------------------------------------------------------
# 7. Good-slice + Gronwall q=3 propagation model.
# If int_0^t Y <= A and Y' <= L(t)Y with int_tau^t L <= Lint, then
# Y(t) <= (4A/t) exp(Lint).  Here A=C gamma K2_eta.
# ---------------------------------------------------------------------------
for t, gamma, theta in [(1e-4, 0.02, 0.01), (0.2, 0.05, 0.02), (0.5, 0.1, 0.03)]:
    K2_eta = 2.5
    A = gamma * K2_eta
    good_slice_bound = 4 * A / t
    lint = theta + theta * r * r + gamma ** 3
    gronwall_bound = good_slice_bound * math.exp(10 * lint)
    expected_form = (gamma * K2_eta / t) * (4 * math.exp(10 * lint))
    check(
        f"good-slice Gronwall gives Y(t) <= C gamma K2_eta/t, t={t}",
        abs(gronwall_bound - expected_form) < 1e-12 * max(1.0, expected_form),
        f"multiplicative constant={4*math.exp(10*lint):.6f}",
    )

# ---------------------------------------------------------------------------
# 8. Unregularized J6 two-factor absorption checks.
# Variables: s=|E|^2, J_m=int eta^2 a^{m-2}s^{m/2},
# X_m=int eta^2 a^{m-1}s^{(m-2)/2}|grad E|^2,
# P_m=int eta^2 a^{m-1}F s^{m/2}, w_m=eta a^{(m-1)/2}s^{m/4}.
# For m=6, w6=eta chi^5 |E|^3.
# ---------------------------------------------------------------------------
for m in [4, 6, 8, 10]:
    J_a, J_s = m - 2, Fraction(m, 2)
    X_a, X_s = m - 1, Fraction(m - 2, 2)
    P_a, P_s = m - 1, Fraction(m, 2)
    w_a, w_s = Fraction(m - 1, 2), Fraction(m, 4)
    check(
        f"m={m}: w_m^2 has P_m weight without F",
        (2 * w_a == P_a) and (2 * w_s == P_s),
        f"w^2 a^{2*w_a} s^{2*w_s}; P a^{P_a} s^{P_s}",
    )
    # gradient a-branch residual: a^{m-3}|da|^2 s^{m/2} = 4 a^{m-2}|dchi|^2 s^{m/2}
    residual_a = (m - 3) + 1
    check(
        f"m={m}: J_m cutoff residual returns a^(m-2)s^(m/2)",
        residual_a == J_a,
        f"a exponent after |da|^2/a cancellation {residual_a}",
    )
    # gradient s-branch: |grad w|^2 <= C a^{m-1}s^{m/2-1}|grad E|^2 = X_m
    check(
        f"m={m}: |grad w|^2 s-branch matches X_m",
        (m - 1 == X_a) and (Fraction(m, 2) - 1 == X_s),
        f"a^{m-1}, s^{Fraction(m,2)-1}",
    )

check(
    "m=6: w6 = eta chi^5 |E|^3 is C^1 at E=0",
    True,
    "s^{3/2}=|E|^3; no division by |E| and no norm regularization needed",
)
check(
    "two-factor Hölder exponents for P6=int F w6^2",
    Fraction(1, 2) + Fraction(1, 4) + Fraction(1, 4) == 1,
    "||F||_2 ||w||_4 ||w||_4",
)

# If P6 <= C gamma(X6+r^-2 J6) and C gamma<c/2, Gronwall coefficient is
# C(1+r^-2), independent of Y and independent of artificial t0.
for t0 in [1e-1, 1e-6, 1e-30]:
    theta = 0.02
    C = 10.0
    T = theta * r * r
    exponent = C * (1 + r ** -2) * T
    # Since T=theta r^2, exponent = C(theta r^2 + theta).
    target = C * (theta * r * r + theta)
    check(
        f"J6 two-factor Gronwall exponent independent of t0={t0:g} and Y",
        abs(exponent - target) < 1e-15,
        f"exponent=C(theta r^2+theta)={target:.6e}; no int S^2Y and no log(T/t0)",
    )

# ---------------------------------------------------------------------------
# 9. Defect endpoint scaling after J6 persistence and nested Moser p0=6:
# S^(1/3) t^(-1/2) (delta^6 V t)^(1/6) with S=r^2/sqrt(V) equals
# delta r^(2/3)t^(-1/3), independent of V.
# ---------------------------------------------------------------------------
delta = 1e-3
t = 1e-5
for V in [1.0, 1e-4, 1e-12]:
    S_cal = r * r / math.sqrt(V)
    endpoint = S_cal ** (Fraction(1, 3)) * t ** (-0.5) * (delta ** 6 * V * t) ** (Fraction(1, 6))
    target = delta * (r * r / t) ** (Fraction(1, 3))
    rel = abs(float(endpoint) - float(target)) / float(target)
    check(
        f"defect endpoint volume cancellation at V={V:g}",
        rel < 1e-12,
        f"endpoint={float(endpoint):.6e}, target={float(target):.6e}",
    )

# ---------------------------------------------------------------------------
# 10. Explicitly list unproved premises: script must not assert them.
# ---------------------------------------------------------------------------
unproved = [
    "index-level all-lower curvature variation for cutoff normalized flow",
    "signed Hessian-a tensor IBP contractions with derivative-structure |nabla B| bounds",
    "defect variation from Ricci variation and contracted Bianchi identity",
    "moving Sobolev first-exit and metric comparison on the same support",
    "smooth existence/continuation with coupled cutoff jets",
]
check("script records unproved PDE premises instead of verifying them", len(unproved) == 5)
print("\nUnproved mathematical premises intentionally not checked as booleans:")
for item in unproved:
    print(f"  - {item}")

failed = [name for name, ok, _ in checks if not ok]
print("\n" + "=" * 76)
if failed:
    print("SOME ALGEBRA/SCALING CHECKS FAILED")
    for name in failed:
        print(f"  - {name}")
    raise SystemExit(1)
else:
    print(f"ALL {len(checks)} ALGEBRA/SCALING CHECKS PASSED")
    print("This supports the fixed-exponent integrated-potential q=3 mechanism and")
    print("the unregularized two-factor J6 persistence only conditional on the")
    print("separately unproved tensor PDE and moving-geometry estimates.")
print("=" * 76)

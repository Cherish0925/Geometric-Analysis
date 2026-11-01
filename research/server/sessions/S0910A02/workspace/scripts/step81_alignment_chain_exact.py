"""Step 81: exact analysis of the summed-Weitzenboeck alignment chain for
positive Einstein 4-manifolds.

Goal: decide whether the b_+ = 3 "harmonic-form alignment" mechanism can
obstruct positive Einstein metrics on the chi = 8, tau = 0 mixed rows.

Conventions (all pinned to Wu/LeBrun and Gursky-LeBrun sources):
  * W^+ is the endomorphism of Lambda^+ with eigenvalues alpha >= beta >= gamma,
    alpha + beta + gamma = 0, and |W^+|^2 = alpha^2 + beta^2 + gamma^2.
    (Wu/LeBrun Lemma 2: |W^+|^2 >= (3/2) alpha^2.)
  * Weitzenboeck on self-dual 2-forms (Wu/LeBrun line 141):
        (d + d*)^2 omega = nabla* nabla omega - 2 W^+(omega) + (s/3) omega.
  * Chern-Gauss-Bonnet / signature, endomorphism norm:
        2 chi + 3 tau = (1/4 pi^2) int ( 2|W^+|^2 + s^2/24 - |E|^2/2 ).
    Checked below on round S^4 and on Kaehler-Einstein CP^2.
  * Normalization: Ric = 3g, s = 12, lambda = 3.  Bishop: V <= Vol(S^4) = 8 pi^2/3.

Outputs a JSON record under workspace/data/.
"""

import json
import math
import os

PI2 = math.pi ** 2
S = 12.0          # scalar curvature for Ric = 3g
V_MAX = 8 * PI2 / 3   # Bishop bound (round S^4 with Ric = 3g)

out = {"conventions": {
    "Weitzenbock": "(d+d*)^2 w = nabla*nabla w - 2W^+(w) + (s/3) w",
    "Wnorm": "|W^+|^2 = alpha^2+beta^2+gamma^2 (endomorphism of Lambda^+)",
    "CGB": "2chi+3tau = (1/4pi^2) int (2|W^+|^2 + s^2/24 - |E|^2/2)",
    "normalization": "Ric = 3g, s = 12, V <= 8pi^2/3 (Bishop)"}}

# ---------------------------------------------------------------------------
# 1. Convention checks
# ---------------------------------------------------------------------------
checks = {}

# Round S^4: W = 0, E = 0, s = 12, V = 8pi^2/3, chi = 2, tau = 0.
lhs = 2 * 2 + 3 * 0
rhs = (1 / (4 * PI2)) * (0 + (S ** 2 / 24) * V_MAX)
checks["S4_CGB"] = {"2chi+3tau": lhs, "formula": rhs, "ok": abs(lhs - rhs) < 1e-9}

# Einstein (E=0, s=12 const):  int|W^+|^2 = 2pi^2(2chi+3tau) - 3V.
def weyl_plus_energy(chi, tau, V):
    return 2 * PI2 * (2 * chi + 3 * tau) - 3 * V

# Kaehler-Einstein CP^2: chi=3, tau=1, W^+ = diag(s/6,-s/12,-s/12)
# => |W^+|^2 = s^2/24 = 6, so int|W^+|^2 = 6V. Solve for V.
# 6V = 2pi^2*9 - 3V  =>  9V = 18pi^2  =>  V = 2pi^2.
V_CP2 = 2 * PI2
checks["CP2_volume"] = {
    "V": V_CP2,
    "int_Wplus2_from_CGB": weyl_plus_energy(3, 1, V_CP2),
    "int_Wplus2_from_Kahler": 6 * V_CP2,
    "ok": abs(weyl_plus_energy(3, 1, V_CP2) - 6 * V_CP2) < 1e-9,
    "bishop_ok": V_CP2 < V_MAX}

# Weitzenbock pointwise check on CP^2 Kahler form (nabla omega = 0, |omega|^2 = 2):
alpha_K, beta_K, gamma_K = S / 6, -S / 12, -S / 12
w2 = 2.0
checks["CP2_Weitzenbock_pointwise"] = {
    "-2W(w,w)+(s/3)|w|^2": -2 * alpha_K * w2 + (S / 3) * w2,
    "ok": abs(-2 * alpha_K * w2 + (S / 3) * w2) < 1e-12}

out["convention_checks"] = checks

# ---------------------------------------------------------------------------
# 2. The chain.
#
# Let {omega_a}, a = 1..b_+, be a Q-orthonormal basis of harmonic self-dual
# 2-forms.  Since Q(w,e) = int <w,e> dV for self-dual harmonic forms, this basis
# is L^2-orthonormal: int |omega_a|^2 = 1.  Put T = sum_a omega_a (x) omega_a,
# a nonnegative symmetric endomorphism of Lambda^+ with int tr T = b_+.
#
# (W1) Weitzenbock, summed:   int <W^+, T> >= (s/6) b_+ = 2 b_+.
# (W2) von Neumann / Ky Fan:  <W^+,T> <= alpha t_1 + beta t_2 + gamma t_3
#                                     <= trT [ alpha - (alpha-beta) theta ],
#      theta := t_2 / trT in [0, 1/3]  (t_i = eigenvalues of T, decreasing).
#      With theta = 0 this is Wu/LeBrun Lemma 2: <W^+,T> <= sqrt(2/3)|W^+| trT.
# (W3) Cauchy-Schwarz:        int |W^+| trT <= ||W^+||_2 ||trT||_2.
# (W4) Concentration factor:  kappa := ||trT||_2 sqrt(V) / b_+ >= 1
#      (equality iff trT is constant).
#
# Chain:  2 b_+ <= C_theta * ||W^+||_2 * kappa * b_+ / sqrt(V),
# where C_theta = max over eigenvalue patterns of
#        [alpha - (alpha-beta) theta] / |W^+|.
#
# ==> b_+ CANCELS.  Setting A := int|W^+|^2 / V, the chain reads
#        2 <= C_theta * kappa * sqrt(A),
# and a contradiction requires  C_theta * kappa * sqrt(A) < 2.
# ---------------------------------------------------------------------------

def C_theta(theta, n=400001):
    """max_{x in [-1/2,1]} [1 - (1-x) theta] / sqrt(2(1+x+x^2)),  x = beta/alpha."""
    best, best_x = -1.0, None
    for i in range(n):
        x = -0.5 + 1.5 * i / (n - 1)
        val = (1.0 - (1.0 - x) * theta) / math.sqrt(2.0 * (1.0 + x + x * x))
        if val > best:
            best, best_x = val, x
    return best, best_x

c0, x0 = C_theta(0.0)
out["C_theta_at_0"] = {"value": c0, "argmax_beta_over_alpha": x0,
                       "sqrt_2_over_3": math.sqrt(2 / 3),
                       "matches_WuLeBrun_Lemma2": abs(c0 - math.sqrt(2 / 3)) < 1e-6,
                       "extremal_pattern": "beta = -alpha/2 (Kaehler eigenvalue pattern)"}

# ---------------------------------------------------------------------------
# 3. Key identity:  theta = 0, kappa = 1  <=>  Gursky-LeBrun.
#    2 <= sqrt(2/3) sqrt(A)  <=>  A >= 6  <=>  int|W^+|^2 >= 6V = int s^2/24.
# ---------------------------------------------------------------------------
out["chain_equals_GurskyLeBrun"] = {
    "statement": ("with theta=0, kappa=1 the chain is exactly "
                  "int|W^+|^2 >= 6V = int s^2/24, i.e. Gursky-LeBrun"),
    "threshold_A": (2 / math.sqrt(2 / 3)) ** 2,
    "s2_over_24": S ** 2 / 24,
    "ok": abs((2 / math.sqrt(2 / 3)) ** 2 - 6.0) < 1e-12}

# ---------------------------------------------------------------------------
# 4. A for the mixed rows (chi = 8, tau = 0) and the irreducible deficit.
# ---------------------------------------------------------------------------
def A_of(chi, tau, V):
    return weyl_plus_energy(chi, tau, V) / V

rows = {}
for name, (chi, tau) in {"mixed_row_chi8_tau0": (8, 0),
                         "row_tau_plus2": (8, 2),
                         "row_tau_minus2": (8, -2),
                         "CP2_KE_control": (3, 1)}.items():
    # A is decreasing in V, so A is minimized at V = V_MAX (Bishop).
    A_min = A_of(chi, tau, V_MAX)
    entry = {"chi": chi, "tau": tau,
             "int_Wplus2_at_Vmax": weyl_plus_energy(chi, tau, V_MAX),
             "A_min_at_Bishop_Vmax": A_min,
             "deficit_factor_sqrt_A_over_6": math.sqrt(A_min / 6.0),
             "V_needed_for_A_below_6": 2 * PI2 * (2 * chi + 3 * tau) / 9.0,
             "V_needed_exceeds_Bishop": 2 * PI2 * (2 * chi + 3 * tau) / 9.0 > V_MAX}
    rows[name] = entry
rows["CP2_KE_control"]["A_at_actual_V"] = A_of(3, 1, V_CP2)
rows["CP2_KE_control"]["chain_is_equality_at_actual_V"] = (
    abs(A_of(3, 1, V_CP2) - 6.0) < 1e-9)
out["rows"] = rows

# ---------------------------------------------------------------------------
# 5. Closure threshold in theta:  need C_theta < 2/(kappa sqrt(A)).
# ---------------------------------------------------------------------------
def theta_threshold(A, kappa=1.0):
    target = 2.0 / (kappa * math.sqrt(A))
    if C_theta(0.0, 20001)[0] < target:
        return 0.0
    lo, hi = 0.0, 1.0 / 3.0
    if C_theta(hi, 20001)[0] >= target:
        return None            # unreachable even at maximal isotropy theta=1/3
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        if C_theta(mid, 20001)[0] >= target:
            lo = mid
        else:
            hi = mid
    return hi

thresholds = {}
for label, (A, kappa) in {
        "A=6 (Kahler critical), kappa=1": (6.0, 1.0),
        "A=9 (chi=8,tau=0 at Bishop Vmax), kappa=1": (9.0, 1.0),
        "A=9, kappa=1.2": (9.0, 1.2),
        "A=12, kappa=1": (12.0, 1.0),
        "A=18, kappa=1": (18.0, 1.0),
        "A=30, kappa=1": (30.0, 1.0)}.items():
    thresholds[label] = {"A": A, "kappa": kappa,
                         "theta_star": theta_threshold(A, kappa),
                         "theta_max_possible": 1.0 / 3.0}
out["theta_thresholds"] = thresholds

# ---------------------------------------------------------------------------
# 6. Summary verdict
# ---------------------------------------------------------------------------
out["verdict"] = {
    "b_plus_cancels": True,
    "theta0_kappa1_chain_is_exactly_GurskyLeBrun": True,
    "A_min_for_chi8_tau0": rows["mixed_row_chi8_tau0"]["A_min_at_Bishop_Vmax"],
    "irreducible_deficit_factor": rows["mixed_row_chi8_tau0"]["deficit_factor_sqrt_A_over_6"],
    "sqrt_3_over_2": math.sqrt(1.5),
    "closure_requires": ("theta-bar >= theta_star(A,kappa) AND kappa near 1 AND "
                         "A near its Bishop minimum; theta_star is the only "
                         "b_+-sensitive quantity in the whole chain"),
    "three_lump_configuration": ("drives theta -> 0 and kappa -> infinity "
                                 "simultaneously, defeating both requirements")}

dest = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                    "data", "step81_alignment_chain_exact.json")
with open(dest, "w") as fh:
    json.dump(out, fh, indent=2)

print(json.dumps({
    "output": dest,
    "S4_CGB_ok": checks["S4_CGB"]["ok"],
    "CP2_ok": checks["CP2_volume"]["ok"],
    "CP2_Weitzenbock_ok": checks["CP2_Weitzenbock_pointwise"]["ok"],
    "C_0": c0,
    "argmax_x": x0,
    "A_min_chi8": rows["mixed_row_chi8_tau0"]["A_min_at_Bishop_Vmax"],
    "deficit": rows["mixed_row_chi8_tau0"]["deficit_factor_sqrt_A_over_6"],
    "sqrt_1.5": math.sqrt(1.5),
    "CP2_A": rows["CP2_KE_control"]["A_at_actual_V"],
    "theta_star_A9": thresholds["A=9 (chi=8,tau=0 at Bishop Vmax), kappa=1"]["theta_star"],
}, indent=2))

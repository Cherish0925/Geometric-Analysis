"""Step 81 Part 2: Spectral analysis of the Weitzenboeck operator
L = nabla*nabla - 2W^+ + (s/3) on self-dual 2-forms.

Key question: does b_+ = 3 force a Weyl energy contradiction on chi=8, tau=0 rows?

The operator L has kernel = H^2_+ (harmonic SD forms), dim = b_+.
On Kahler-Einstein CP^2: L has 1-dim kernel, potential V = diag(0, 6, 6) >= 0.
On a hypothetical positive Einstein metric with b_+ = 3: L needs 3 zero modes,
forcing more "negative potential" (2alpha - s/3 > 0 on a larger set).

This script computes:
1. The spectral potential analysis of L for various eigenvalue patterns
2. The "cross-form" algebraic constraints from b_+ >= 2
3. The volume-Weyl tradeoff forced by b_+ = 3
"""

import json
import math
import os

PI2 = math.pi ** 2
S = 12.0
V_MAX = 8 * PI2 / 3  # Bishop bound
V_S2xS2 = 16 * PI2 / 9  # Product Einstein S^2 x S^2 with Ric=3g

out = {}

# ---------------------------------------------------------------------------
# 1. Spectral potential of L for various W^+ eigenvalue patterns
# ---------------------------------------------------------------------------
def L_potential_eigenvalues(alpha, beta):
    """Returns the three eigenvalues of V = -2W^+ + (s/3)Id."""
    gamma = -alpha - beta
    return (S/3 - 2*alpha, S/3 - 2*beta, S/3 - 2*gamma)

patterns = {}
# Kaehler: alpha = s/6 = 2, beta = gamma = -1
v = L_potential_eigenvalues(2, -1)
patterns["Kaehler (alpha=2,beta=-1)"] = {
    "eigenvalues": v, "min_eigenvalue": min(v),
    "nonneg": all(x >= 0 for x in v),
    "zero_modes": "1 (Kaehler form)"}

# Round S4: W+ = 0, alpha = beta = gamma = 0
v = L_potential_eigenvalues(0, 0)
patterns["S4 (alpha=0)"] = {
    "eigenvalues": v, "min_eigenvalue": min(v),
    "nonneg": all(x >= 0 for x in v)}

# Generic: alpha=3, beta=0, gamma=-3
v = L_potential_eigenvalues(3, 0)
patterns["Generic (alpha=3,beta=0)"] = {
    "eigenvalues": v, "negative_eigenvalue": S/3-6,
    "neg_depth": 6-S/3}

# Large alpha: alpha=6, beta=-3, gamma=-3
v = L_potential_eigenvalues(6, -3)
patterns["Large_alpha (alpha=6,beta=-3)"] = {
    "eigenvalues": v, "negative_eigenvalue": S/3-12}

out["spectral_patterns"] = patterns

# ---------------------------------------------------------------------------
# 2. Key algebraic constraint: two forms can't both be in the alpha-eigenline
#
# At a point where omega_1 and omega_2 are both nonzero and linearly
# independent: the Gram matrix G of (omega_1, omega_2, omega_3) has rank >= 2.
# If both lie in the 1D alpha-eigenline of W+, they must be proportional,
# contradicting L^2 orthogonality.
#
# Therefore at such points, the effective W+ pairing is:
# <W+, T> = alpha*t1 + beta*t2 + gamma*t3, NOT alpha*trT.
# With t2 > 0, the improvement is at least (alpha - beta)*t2.
# ---------------------------------------------------------------------------

def weitzenbock_improvement(alpha, beta, t2_frac):
    """Improvement in <W+,T>/trT relative to the rank-1 bound alpha.
    t2_frac = t2/trT (isotropy parameter)."""
    gamma = -alpha - beta
    # rank-1 bound: <W+,T>/trT <= alpha
    # actual: alpha*(1-t2_frac-t3_frac) + beta*t2_frac + gamma*t3_frac
    # worst case t3 = 0: alpha*(1-t2_frac) + beta*t2_frac = alpha - (alpha-beta)*t2_frac
    return (alpha - beta) * t2_frac

# At Kaehler: alpha=2, beta=-1, improvement = 3*t2_frac
# At generic: alpha=3, beta=0, improvement = 3*t2_frac
out["cross_form_improvement"] = {
    "formula": "delta = (alpha - beta) * theta, where theta = t2/trT",
    "Kaehler_factor": 2 - (-1),  # = 3
    "generic_factor": 3 - 0,      # = 3
    "note": ("Two independent forms at same point force theta > 0. "
             "Quantifying theta requires eigenvalue perturbation for L.")}

# ---------------------------------------------------------------------------
# 3. The maximum principle constraint on |omega|^2
#
# For a harmonic SD form omega with L omega = 0:
# Delta|omega|^2 = -2|nabla omega|^2 + 2<omega, nabla*nabla omega>
#                = -2|nabla omega|^2 + 2<omega, (2W+ - s/3)omega>
#                = -2|nabla omega|^2 + 4W+(omega,omega) - 2(s/3)|omega|^2
#
# At a maximum of |omega|^2: Delta|omega|^2 >= 0, so:
# 4W+(omega,omega) >= 2(s/3)|omega|^2, hence W+(omega,omega) >= (s/6)|omega|^2.
# If omega is in the alpha-eigenline: 4 alpha >= 2s/3, so alpha >= 2.
# If omega is in the beta-eigenline: 4 beta >= 2s/3, so beta >= 2.
# Since alpha >= beta, the constraint alpha(p_max) >= 2 is always satisfied.
# The constraint beta(p_max) >= 2 would require beta = alpha (isotropic W+).
#
# For constant-norm omega: nabla omega in Lambda^1 (x) omega^perp, and
# W+(omega,omega) = (s/6)|omega|^2 everywhere. This forces alpha = 2 everywhere,
# hence Kaehler. So b+ >= 2 excludes constant-norm harmonic SD forms.
# ---------------------------------------------------------------------------

out["max_principle"] = {
    "at_maximum_of_|omega|^2": {
        "constraint": "alpha(p_max) >= s/6 = 2",
        "consequence": "|W+|(p_max) >= sqrt(6) (Kahler bound for |W+| at max)"},
    "constant_norm_exclusion": {
        "statement": "b+ >= 2 excludes any constant-norm harmonic SD form",
        "reason": "constant norm + Weitzenbock forces W+(omega,omega)=(s/6)|omega|^2, hence Kahler pattern, hence b+=1",
        "source": "Wu/LeBrun lines 128-130, 176-178"},
    "non_constant_norm": {
        "statement": "Every harmonic SD form on b+ >= 2 Einstein has non-constant norm",
        "quantitative_consequence": ("max|omega|^2 > 1/V strictly (since int|omega|^2=1 "
                                     "and omega is non-constant). But no universal lower "
                                     "bound on the gap max-min is known.")}}

# ---------------------------------------------------------------------------
# 4. The CLR/spectral reformulation
#
# L = nabla*nabla + V, V = -2W+ + (s/3)Id on Lambda+ (rank 3 bundle).
# dim ker L = b+.
# The negative part of V: V_- has one eigenvalue (2alpha - s/3)_+ = (2alpha-4)_+
# in the alpha-eigendirection.
#
# By CLR-type estimates (adapted for compact manifolds):
# b+ <= N_0(L) <= C / Y^2 * rank * int (2alpha-4)_+^2 dV
#
# where Y = 12*sqrt(V) is the Yamabe constant.
#
# Rearranging: int (2alpha-4)_+^2 >= b+ * Y^2 / (C * rank)
#            = b+ * 144V / (3C)
#            = 48 b+ V / C
#
# Upper bound: (2alpha-4)_+^2 <= (2alpha)^2 = 4alpha^2 <= (8/3)|W+|^2
# So: int (2alpha-4)_+^2 <= (8/3)(32pi^2 - 3V) for Einstein, chi=8, tau=0.
#
# Combining: (8/3)(32pi^2-3V) >= 48*3*V/C = 144V/C
# => 256pi^2 - 24V >= 1296V/C... wait, 8/3*32pi^2 = 256pi^2/3.
# ---------------------------------------------------------------------------

def clr_analysis(b_plus, chi, tau, V_est=None):
    """CLR-type analysis for the Weitzenbock operator."""
    if V_est is None:
        V_est = V_MAX * 0.99  # slightly below Bishop
    
    int_Wplus2 = 2 * PI2 * (2*chi + 3*tau) - 3 * V_est
    max_neg_potential2 = (8/3) * int_Wplus2  # crude upper bound on int(2alpha-4)_+^2
    
    # Yamabe constant for Einstein Ric=3g
    Y2 = 144 * V_est
    rank = 3  # rank of Lambda+
    
    # CLR: b+ <= C * rank * max_neg_potential2 / Y2
    # => C >= b+ * Y2 / (rank * max_neg_potential2)
    C_needed = b_plus * Y2 / (rank * max_neg_potential2)
    
    # Compare with known CLR constants
    # On R^4, scalar: L_4 = 1/(16 pi^2) ~ 0.00633
    # Rank-3 bundle: 3 * L_4 ~ 0.019
    L4_R4 = 3.0 / (16 * PI2)  # bundle-adjusted R^4 constant
    
    return {
        "b_plus": b_plus,
        "chi": chi, "tau": tau,
        "V_est": V_est,
        "int_Wplus2": int_Wplus2,
        "max_neg_potential2": max_neg_potential2,
        "Y2": Y2,
        "C_needed_for_contradiction": C_needed,
        "R4_CLR_constant": L4_R4,
        "would_contradict_on_R4": C_needed > L4_R4,
        "note": ("If C_needed > C_actual, then b+ > N_0(L), contradiction. "
                 "C_actual on compact manifold >> C on R^4.")}

out["CLR_analysis"] = {
    "at_near_Bishop_V": clr_analysis(3, 8, 0, V_MAX * 0.99),
    "at_S2xS2_V": clr_analysis(3, 8, 0, V_S2xS2),
    "at_half_Bishop_V": clr_analysis(3, 8, 0, V_MAX * 0.5)}

# ---------------------------------------------------------------------------
# 5. The volume-Weyl tradeoff with b+ = 3
#
# Key identities for Einstein, chi=8, tau=0, Ric=3g, s=12:
# * int|W+|^2 + int|W-|^2 + 6V = 64pi^2     [full CGB]  
# * int|W+|^2 = 32pi^2 - 3V                  [one-chirality CGB]
# * V <= 8pi^2/3 (Bishop), strict for M != S^4
# * V(S^4) = 8pi^2/3, V(CP^2) = 2pi^2, V(S^2xS^2) = 16pi^2/9
#
# If b+ = 3 forces int|W+|^2 >= f(3)*V for some f(3) > 9,
# then 32pi^2 - 3V > 9V, i.e., V < 32pi^2/12 = 8pi^2/3.
# But V < 8pi^2/3 is already guaranteed by M != S^4 for b+ >= 1.
# So f(3) > 9 gives NO new constraint!
#
# Need f(3) > 32pi^2/V - 3 for the ACTUAL V of the metric.
# ---------------------------------------------------------------------------

out["volume_weyl_tradeoff"] = {
    "identity": "int|W+|^2 = 32pi^2 - 3V for Einstein, chi=8, tau=0",
    "A_min_at_Bishop": 9.0,
    "A_at_S2xS2": (32*PI2 - 3*V_S2xS2) / V_S2xS2,
    "A_at_CP2": (32*PI2 - 3*2*PI2) / (2*PI2),
    "key_observation": ("f(3) > 9 gives no contradiction since V < 8pi^2/3 is "
                       "already known for b+ >= 1. Need either: "
                       "(a) f(3) > 32pi^2/V_actual - 3, or "
                       "(b) a direct b+-dependent UPPER bound on V, or "
                       "(c) the CLR reformulation with quantitative constants."),
    "S2xS2_A": round((32*PI2 - 3*V_S2xS2) / V_S2xS2, 6)}

# ---------------------------------------------------------------------------
# 6. The "Derdzinski defect" quantification
#
# On a positive Einstein 4-manifold:
# * Derdzinski: W+ has Kahler pattern (beta = -alpha/2) everywhere iff
#   nabla W+ = 0, iff metric is locally Kahler/symmetric.
# * For b+ >= 2: not locally Kahler, so Derdzinski defect is positive.
# * Define delta_D(x) = |beta/alpha + 1/2| (deviation from Kahler pattern).
#
# The refined Kato inequality (Gursky-LeBrun, line 189):
# |nabla W+|^2 >= (5/3)|nabla|W+||^2
# gives: |nabla W+|^2 - |nabla|W+||^2 >= (2/3)|nabla|W+||^2
# The excess (5/3 vs 1) is related to the dimension of the normal bundle
# of W+ in the space of symmetric trace-free endomorphisms.
#
# From the Derdzinski Bochner formula:
# 0 = (1/2)Delta|W+|^2 + |nabla W+|^2 + (s/2)|W+|^2 - 18 det W+
# Integrating: int|nabla W+|^2 = 18 int det W+ - (s/2) int|W+|^2
#
# The algebraic inequality: 3 sqrt(6) det W+ <= |W+|^3
# (equality iff Kahler pattern)
# Defect: |W+|^3 - 3sqrt(6) det W+ >= c * delta_D^2 * |W+|^3
# (this is the quantitative Derdzinski defect)
# ---------------------------------------------------------------------------

def derdz_defect(x):
    """Ratio det(W+)/|W+|^3 as function of x = beta/alpha.
    Maximum at x = -1/2 (Kahler): value = 1/(3 sqrt(6))."""
    if abs(x) > 0.5 + 1e-10 or x > 1 + 1e-10:
        return None
    y = 1 + x + x**2
    det_ratio = -x * (1 + x) / (2 * y)**1.5
    max_ratio = 1 / (3 * math.sqrt(6))
    return {"x": x, "det_ratio": det_ratio, "max_ratio": max_ratio,
            "defect": 1 - det_ratio / max_ratio}

out["derdzinski_defect"] = {
    "Kahler_x=-0.5": derdz_defect(-0.5),
    "x=0": derdz_defect(0.0),
    "x=0.25": derdz_defect(0.25),
    "x=1.0 (spherical)": derdz_defect(1.0)}

# ---------------------------------------------------------------------------
# 7. Summary and honest assessment
# ---------------------------------------------------------------------------
out["summary"] = {
    "b_plus_cancels_from_crude_chain": True,
    "crude_chain_is_exactly_GurskyLeBrun": True,
    "margin_sqrt_3_over_2": math.sqrt(1.5),
    "margin_percent": (math.sqrt(1.5) - 1) * 100,
    "three_improvements_needed": [
        "1. Degeneracy defect: W+ != Kahler pattern on b+>=2 Einstein",
        "2. Isotropy of T: two independent forms force theta > 0 at overlap",
        "3. CLR/spectral: b+ zero modes force negative potential budget"
    ],
    "none_quantified_by_known_tools": True,
    "equality_case_topologically_excluded": True,
    "known_positive_Einstein_b+": {
        "S4": {"b+": 0},
        "CP2": {"b+": 1},
        "S2xS2": {"b+": 1},
        "Bl_k_CP2 (1<=k<=8)": {"b+": 1},
        "Page": {"b+": 1},
        "Chen-LeBrun-Weber": {"b+": 1}},
    "all_known_have_b+_le_1": True,
    "this_is_evidence_not_theorem": True,
    "conclusion": ("The alignment mechanism is alive but unproved. The gap is "
                  "22.5% at Bishop volume. The equality case (Kahler, b+=1) is "
                  "topologically excluded on the mixed rows. Three quantitative "
                  "improvements could close the gap, but none follows from "
                  "currently known techniques. A b+-dependent Weyl energy "
                  "inequality would be a theorem about positive Einstein "
                  "4-manifolds in its own right.")}

dest = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                    "data", "step81_spectral_analysis.json")
with open(dest, "w") as fh:
    json.dump(out, fh, indent=2)
print(json.dumps({"output": dest, "ok": True,
                  "A_S2xS2": round((32*PI2-3*V_S2xS2)/V_S2xS2, 4),
                  "C_needed_near_Bishop": out["CLR_analysis"]["at_near_Bishop_V"]["C_needed_for_contradiction"],
                  "CLR_R4": out["CLR_analysis"]["at_near_Bishop_V"]["R4_CLR_constant"]}, indent=2))

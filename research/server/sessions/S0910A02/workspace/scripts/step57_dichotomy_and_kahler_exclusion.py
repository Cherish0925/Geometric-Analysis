#!/usr/bin/env python3
"""
Step 57: Kähler exclusion, van Kampen, higher-genus, Bauer-Furuta scope, 
and the unified dichotomy for the four-dimensional noncollapsed wall.

This script records finite arithmetic checks and logical structures.
It does not prove a theorem, but organizes verifiable route-control data.
"""
import json
from fractions import Fraction

result = {}

# ============================================================
# 1. Even-row Kähler exclusion for (Σ₂×Σ₂)/⟨ι×ι⟩
# ============================================================
# Source: Baraglia (Constraints-on-embedded-spheres) lines 30-38.
# If [S] can be represented by a sphere, adding a handle gives genus 1.
# Then for any spinc structure s with SW(X,s) ≠ 0 and b₊(X) > 1:
#   |⟨c(s),[S]⟩| + [S]² ≤ 0.
# A +2-sphere gives [S]² = 2 > 0, contradiction.
# Therefore SW(X,s) = 0 for all s, hence no nonzero numerical SW basic class.
#
# Kähler exclusion: any Kähler manifold X with b₊ > 1 has SW(X,±K_X) = ±1
# by Taubes' theorem (symplectic => nonvanishing SW). K_X non-torsion if K² > 0.
# So: +2 sphere + b₊ > 1 => no Kähler structure.
#
# More generally: any symplectic structure on a manifold with b₊ > 1 gives
# nonzero SW invariants, contradicting the +2-sphere adjunction bound.

N = 36  # number of A₁ nodes in (Σ₂×Σ₂)/⟨ι×ι⟩
kahler_exclusion = []
for r in range(N+1):
    b_plus = 9 + r
    b_minus = 45 - r
    b_plus_rev = b_minus  # in reverse orientation
    # In original orientation: r reversed nodes => r spheres of square +2
    has_plus2_orig = (r > 0)
    has_plus2_rev = ((N - r) > 0)  # 36-r compatible nodes become reversed in reverse orientation
    # Kähler exclusion: need +2-sphere AND b₊ > 1
    kahler_excluded_orig = (has_plus2_orig and b_plus > 1)
    kahler_excluded_rev = (has_plus2_rev and b_plus_rev > 1)
    kahler_excluded_both = kahler_excluded_orig and kahler_excluded_rev
    
    kahler_exclusion.append({
        "r": r,
        "b_plus_orig": b_plus,
        "b_minus_orig": b_minus,
        "b_plus_rev": b_minus,  # b₊ in reverse = b₋ in original
        "plus2_spheres_orig": r,
        "plus2_spheres_rev": N - r,
        "kahler_excluded_original_orientation": kahler_excluded_orig,
        "kahler_excluded_reverse_orientation": kahler_excluded_rev,
        "kahler_excluded_both_orientations": kahler_excluded_both,
    })

# Verify: for r=0,36 one orientation has 0 reversed => no +2 sphere => not excluded
assert not kahler_exclusion[0]["kahler_excluded_both_orientations"]
assert not kahler_exclusion[36]["kahler_excluded_both_orientations"]
# For 1 ≤ r ≤ 35: excluded in BOTH orientations
for r in range(1, 36):
    assert kahler_exclusion[r]["kahler_excluded_both_orientations"], f"r={r} not excluded"

result["kahler_exclusion"] = {
    "theorem": (
        "For 1 ≤ r ≤ 35, M_r admits no Kähler (or symplectic) structure in either orientation. "
        "Proof: M_r with r reversed A₁ nodes contains r non-torsion embedded spheres of "
        "self-intersection +2 with b₊ = 9+r > 1. By adjunction (Baraglia/Kronheimer lines 30-38), "
        "any sphere class with [S]²>0 contradicts SW(X,s)≠0 for b₊>1 simple type. "
        "Taubes' theorem gives nonvanishing SW for any symplectic/Kähler structure with b₊>1. "
        "In reverse orientation, 36-r ≥ 1 reversed nodes give +2-spheres with b₊ = 45-r > 1. "
        "Therefore no symplectic/Kähler structure exists in either orientation."
    ),
    "consequence": (
        "Aubin-Yau negative KE and all algebraic-surface Einstein existence machines "
        "require Kähler structure. Hence no mixed row r=1,...,35 can be settled by "
        "Kähler-geometric Einstein existence. This strictly strengthens the Noether parity "
        "obstruction (which only excluded odd r from having complex structures)."
    ),
    "endpoint_check": {
        "r_0": "Not excluded in original orientation (0 +2-spheres). "
                "Known Einstein by Aubin-Yau on the smooth double-cover diffeotype.",
        "r_36": "Not excluded in reverse orientation (0 +2-spheres there). "
                 "Orientation-reverse of r=0, hence same Einstein metric as unoriented manifold.",
    },
    "live_representatives": list(range(1, 19)),
    "total_live": 18,
}

# ============================================================
# 2. Van Kampen proof for π₁ = 1 on all sign-pattern fillings
# ============================================================
# Source: On-Einstein-Metrics-on-4-Manifolds-with-Finite-Cyclic, lines 210-219 (Catanese)
# and lines 170-208 (A₁ minimal resolution ≅ smoothing ≅ T*S² = O(-2) disk bundle).
#
# Setup:
# - O = (Σ₂×Σ₂)/⟨ι×ι⟩ has 36 A₁ singularities.
# - M₀ = all-compatible smooth resolution = smooth double cover of P¹×P¹
#   branched over a smooth connected (6,6) curve. Simply connected by:
#   (a) P¹×P¹ is simply connected.
#   (b) Branch divisor in |O(6,6)| is smooth, connected, ample => Lefschetz/Catanese
#       gives simply connected double cover.
# - W = M₀ minus 36 open tubular neighborhoods of exceptional (-2)-spheres.
# - Each tubular neighborhood D⁻ is the total space of the -2 disk bundle over S²,
#   diffeomorphic to T*S², hence simply connected. Boundary = RP³.
# - The +2 disk bundle D⁺ over S² is also simply connected. Boundary = RP³.
# - For either filling: the inclusion RP³ → D± induces the zero map on π₁
#   because D± is simply connected.
#
# Van Kampen:
# M_r = W ∪ (some D⁻ and some D⁺), where the gluing is along RP³ boundaries.
# π₁(M_r) = π₁(W) * π₁(D₁) * ... * π₁(D₃₆) / (identification of boundary images)
#          = π₁(W) / {normal closure of images of π₁(RP³) → π₁(W)}
# Since π₁(M₀) = π₁(W) / {same boundary images} = 1 (because M₀ is s.c.),
# and the boundary images are the same regardless of filling sign,
# π₁(M_r) = 1 for all r.

result["van_kampen"] = {
    "statement": "All sign-pattern fillings M_r, 0 ≤ r ≤ 36, are simply connected.",
    "proof_sketch": (
        "M₀ is simply connected: it is the smooth double cover of P¹×P¹ branched "
        "over a smooth connected (6,6) curve, and Catanese's proposition (source lines 210-219) "
        "gives π₁ = 1 for cyclic covers of simply connected bases branched over smooth "
        "connected flexible divisors. Let W = M₀ \\ ⊔ₖ N_k where N_k are open tubular "
        "neighborhoods of the 36 exceptional (-2)-spheres. Each N_k has boundary RP³ and "
        "is simply connected (disk bundle over S²). For any sign pattern, M_r is obtained "
        "from W by attaching either -2 or +2 disk bundles over S² along the same RP³ boundaries. "
        "Both ±2 disk bundles are simply connected (deformation retract to S²), so the inclusion "
        "RP³ → D± induces the zero map on π₁. Van Kampen gives "
        "π₁(M_r) = π₁(W)/{normal closure of images of π₁(RP³_k)} = π₁(M₀) = 1."
    ),
    "key_input": "Both ±2 disk bundles over S² are simply connected with boundary RP³.",
    "consequence": (
        "All M_r have amenable (trivial) fundamental group, hence zero simplicial volume. "
        "Gromov-norm and Sambusetti/BCG-type obstructions requiring nonzero simplicial volume "
        "are vacuous for this entire family."
    ),
}

# ============================================================
# 3. Higher-genus generalization: (Σ_h×Σ_h)/⟨ι×ι⟩
# ============================================================
# Genus h hyperelliptic involution on Σ_h has 2(h+1) fixed points.
# Product action has N = 4(h+1)² fixed points, each A₁.
# χ(Σ_h×Σ_h) = (2-2h)² = 4(h-1)², σ = 0, K² = 8(h-1)².
# Orbifold: χ_orb = (4(h-1)² + N)/2 = (4(h-1)² + 4(h+1)²)/2 = 4(h²+1).
# Resolution: χ = 4(h²+1) + N = 4(h²+1) + 4(h+1)² = 8(h²+h+1).
# K²_orb = 8(h-1)²/2 = 4(h-1)². τ_orb = (K² - 2χ_orb)/3? No, use σ = 0.
# Actually, σ(Σ_h×Σ_h) = 0, so σ_orb = 0/2 = 0 (product has σ=0).
# Wait, for double cover: σ(X̃)/2 = σ_orb for branch on singular cover?
# Better: use the all-compatible resolution.
# b₁(M₀) = 0 because hyperelliptic involution acts as -1 on H¹.
# b₂ = χ - 2 = 8(h²+h+1) - 2 = 8h²+8h+6.
# K² = 4(h-1)² for the all-compatible resolution.
# τ = (K² - 2χ + N(... )) ... let me compute more carefully.
# 
# Actually from the product: σ(product) = 0, so each resolution node contributes ±1 to σ.
# Compatible (-2)-sphere: contributes -1 to intersection form.
# Reversed (+2)-sphere: contributes +1 to intersection form.
# So τ(M_r) = 0_orbifold_contribution + (-1)(N-r) + (+1)(r) = -N + 2r.
# Wait, the orbifold quotient of σ=0 product has σ_orb = 0. Resolving N nodes by
# -2 spheres gives τ = 0 - N = -N? No.
# 
# Let me compute from scratch. M₀ = double cover of P¹×P¹ branched over smooth (6,6).
# For h=2: K = π*O(1,1), K² = 2*1*1*2 = 4. χ = 56. 
# τ = (K² - 2χ)/(-1)? No, for a surface: σ = (1/3)(c₁² - 2c₂) = (K² - 2χ)/3 = (4-112)/3 = -108/3 = -36. Good.
# Check: τ = -36, b₊ = (2χ+3τ-2)/2 = (112-108-2)/2 = 1... wait.
# b₊ - b₋ = τ = -36. b₊ + b₋ = b₂ = χ-2 = 54. So b₊ = (54-36)/2 = 9, b₋ = 45. Good.
#
# For general h: χ = 8(h²+h+1), N = 4(h+1)².
# M₀ = double cover of P¹×P¹ branched over smooth (2h+2, 2h+2) curve.
# K = π*O(h-1, h-1). K² = 2*(h-1)*(h-1)*2 = 4(h-1)².
# τ = (K² - 2χ)/3 = (4(h-1)² - 16(h²+h+1))/3 = (4h²-8h+4-16h²-16h-16)/3
#   = (-12h²-24h-12)/3 = -4(h²+2h+1) = -4(h+1)² = -N.
# And τ(M_r) = -N + 2r.
# b₊ = (b₂ + τ)/2 = (8h²+8h+6 - N + 2r)/2.
# b₂ = χ-2 = 8h²+8h+6.
# b₊ = (8h²+8h+6 - 4(h+1)² + 2r)/2 = (8h²+8h+6 - 4h²-8h-4 + 2r)/2 = (4h²+2+2r)/2 = 2h²+1+r.
# b₋ = b₂ - b₊ = 8h²+8h+6 - 2h² - 1 - r = 6h²+8h+5-r.
#
# Hitchin-Thorpe: 2χ ≥ 3|τ|.
# 2χ = 16(h²+h+1).
# 3|τ| = 3|2r-N| = 3|2r-4(h+1)²|.
# For r ≤ N/2: 3|τ| = 3(N-2r) = 12(h+1)²-6r.
# HT margin: 16(h²+h+1) - 12(h+1)² + 6r = 16h²+16h+16-12h²-24h-12+6r = 4h²-8h+4+6r = 4(h-1)²+6r.
# For r ≥ N/2: 3|τ| = 3(2r-N) = 6r-12(h+1)².
# HT margin: 16(h²+h+1) - 6r + 12(h+1)² = 16h²+16h+16+12h²+24h+12-6r = 28h²+40h+28-6r
#           = 4(7h²+10h+7)-6r = 4(h-1)²+6(N-r).
# By symmetry: margin = 4(h-1)² + 6*min(r, N-r).
# For h ≥ 2: 4(h-1)² ≥ 4 > 0. So HT is STRICT for all r and all h ≥ 2.

higher_genus = []
for h in range(2, 6):
    Nh = 4*(h+1)**2
    chi_h = 8*(h**2 + h + 1)
    b2_h = chi_h - 2
    K2_h = 4*(h-1)**2
    tau_0 = -Nh  # all-compatible
    b_plus_0 = 2*h**2 + 1
    b_minus_0 = b2_h - b_plus_0
    
    # HT margin at r=0: 4(h-1)²
    ht_margin_min = 4*(h-1)**2
    
    # Orientation pairing: r ↔ N-r
    live_max = Nh // 2
    
    higher_genus.append({
        "h": h,
        "N_nodes": Nh,
        "chi": chi_h,
        "b2": b2_h,
        "K2_all_compatible": K2_h,
        "tau_all_compatible": tau_0,
        "b_plus_all_compatible": b_plus_0,
        "b_minus_all_compatible": b_minus_0,
        "HT_margin_formula": f"4(h-1)² + 6*min(r,N-r) = {ht_margin_min} + 6*min(r,{Nh}-r)",
        "HT_margin_minimum": ht_margin_min,
        "HT_strict_all_rows": ht_margin_min > 0,
        "live_representatives": f"r=1,...,{live_max}",
        "kahler_excluded_all_mixed_rows": True,
        "simply_connected_all_rows": True,  # same van Kampen argument
    })

result["higher_genus_generalization"] = {
    "family": "(Σ_h × Σ_h)/⟨ι×ι⟩ for genus h ≥ 2 hyperelliptic curves",
    "formulas": {
        "N": "4(h+1)²",
        "chi": "8(h²+h+1)",
        "b2": "8h²+8h+6",
        "tau_r": "-4(h+1)² + 2r",
        "b_plus_r": "2h² + 1 + r",
        "b_minus_r": "6h²+8h+5-r",
        "HT_margin": "4(h-1)² + 6·min(r, N-r)",
    },
    "conclusion": (
        "Strict Hitchin-Thorpe holds for every h ≥ 2 and every 0 ≤ r ≤ N. "
        "No enlargement of the family produces a topological contradiction. "
        "The entire two-parameter family sits strictly inside HT, "
        "so a third wall of this shape adds no new information."
    ),
    "sample_data": higher_genus,
}

# ============================================================
# 4. Bauer-Furuta scope check
# ============================================================
# Kotschick (Monopole-classes-and-Einstein-metrics) lines 132-168:
# All known Bauer/Furuta/Ishida-LeBrun connected-sum nonvanishing results
# require Kähler (symplectic) summands with b₁=0 and b₊ ≡ 3 (mod 4).
# The mixed rows M_r (1 ≤ r ≤ 35) are:
# - Not Kähler/symplectic in either orientation (proved above)
# - Simply connected (van Kampen)
# - Do not decompose along the +2-sphere neighborhood (boundary = RP³, not S³)
#
# The inversion: does any known nonvanishing input reach these rows?
# All inputs run through: (a) Kähler summands (Taubes → SW ≠ 0), or
# (b) connected-sum splittings along S³ with Kähler pieces.
# Since M_r is not Kähler and does not split into Kähler pieces, no known input applies.

result["bauer_furuta_scope"] = {
    "question": "Can any known Bauer-Furuta or generic monopole nonvanishing reach a mixed row?",
    "answer": "No known input applies.",
    "reasoning": [
        "All known connected-sum nonvanishing (Kotschick Theorem 10, Ishida-LeBrun Cor 13) "
        "require symplectic/Kähler summands with b₊ ≡ 3 (mod 4) and nonvanishing SW.",
        "Mixed rows M_r (1 ≤ r ≤ 35) are not Kähler/symplectic in either orientation (Theorem above).",
        "The +2-sphere neighborhood has boundary RP³, not S³ or a homology sphere, "
        "so the +2-sphere does not represent a connected-sum splitting.",
        "No other mechanism is known to produce nonzero generic monopole classes on these manifolds.",
    ],
    "caveat": (
        "This is a statement about currently known mechanisms, not a vanishing theorem. "
        "A genuinely new source of generic monopole classes on non-Kähler simply connected "
        "manifolds with embedded +2-spheres could change this assessment. "
        "But the fact that all known four-dimensional Einstein nonexistence and existence "
        "theorems for b₊ > 1 simply connected manifolds run through monopole/SW classes, "
        "which are killed by the +2-sphere, makes such a breakthrough the only available "
        "four-dimensional refutation route."
    ),
}

# ============================================================
# 5. Multi-bubble estimate source gap
# ============================================================
result["multi_bubble_estimate_gap"] = {
    "statement": (
        "The reduction theorem conditionally uses the refined EH desingularization estimate: "
        "after killing all first obstructions, the operator-norm Ricci defect is O(t^{1/2}) → 0. "
        "This estimate is sourced from Ozuch (Higher-order-obstructions) lines 783-789, "
        "which cites Biquard 2013 Section 14 for the EH-region estimate."
    ),
    "source_status": {
        "Ozuch_lines_715_789": "Read and verified in session (lines give the approximate metric "
                                "definition, weighted controls, and the projected defect bound).",
        "Biquard_2013_Section_14": "CITED BUT NOT RETRIEVED. This session has not read Biquard's "
                                   "original paper. The estimate is imported through Ozuch's reference.",
    },
    "multi_bubble_caveat": (
        "Ozuch's construction handles finitely many simultaneous EH insertions with disjoint "
        "gluing balls. For 36 bubbles: (1) the transition annuli must be mutually disjoint, "
        "which holds when all insertion scales t_j are comparable and small relative to the "
        "inter-node distance (which is fixed on the orbifold). (2) Reversed attaching uses "
        "the same Riemannian ALE metric but tests R_- rather than R_+; the local estimate "
        "transfers because EH is orientation-reversibly isometric. (3) The non-interaction "
        "of first obstructions at different nodes holds because each obstruction coefficient λ_k^j "
        "is a local boundary flux involving only the j-th bubble's data (Ozuch lines 650-654)."
    ),
    "recommended_action": (
        "Either retrieve Biquard 2013 to source-close the EH-region estimate directly, "
        "or state the reduction explicitly as conditional on: (a) Biquard's displayed estimate "
        "[Biq13, Section 14] as cited in Ozuch, and (b) non-interaction of 36 simultaneous "
        "disjoint EH insertions at comparable scale."
    ),
}

# ============================================================
# 6. The unified dichotomy
# ============================================================
result["dichotomy"] = {
    "statement": (
        "In dimension four, the mechanism by which tight operator-norm Ricci pinching "
        "(positive or negative) drives ALE bubble insertions precisely into the region "
        "where all four-dimensional Einstein existence and nonexistence tools are void "
        "is governed by a single structural principle:"
    ),
    "principle": (
        "A reversed ALE bubble — forced exactly when the first obstruction requires the "
        "opposite-chirality curvature block — inserts a non-torsion embedded sphere of "
        "self-intersection +2. This +2-sphere annihilates every nonzero ordinary SW basic class "
        "(adjunction with handle → genus 1, giving |⟨c,[S]⟩| + [S]² ≤ 0, contradicted by [S]²=2) "
        "whenever b₊ > 1. In particular it kills all Kähler/symplectic structure in both "
        "orientations (Taubes' SW nonvanishing). The Einstein nonexistence tools (LeBrun, "
        "Ishida-LeBrun, Kotschick) all require nonzero monopole/SW classes as input. "
        "The Einstein existence tools (Aubin-Yau, Kähler-Einstein, Tian) all require "
        "Kähler/algebraic structure. Both machines are voided by the +2-sphere mechanism."
    ),
    "mirror_walls": {
        "positive": (
            "(S²×S²)/Z₂ with 4 A₁ nodes, R₊=R₋=diag(Λ,0,0), 5 rows with r=1,2,3 live. "
            "Source: Steps 44-50."
        ),
        "negative": (
            "(Σ₂×Σ₂)/⟨ι×ι⟩ with 36 A₁ nodes, R₊=R₋=diag(-1,0,0), 37 rows with r=1,...,18 live "
            "(up to orientation). Source: Steps 55-57."
        ),
    },
    "correlation": (
        "The two rows retaining SW classes in one orientation (r=0 and r=N) are exactly "
        "the two rows known to be Einstein: the all-compatible row is a Kähler-Einstein "
        "manifold (Aubin-Yau or del Pezzo), and the all-reversed row is its orientation "
        "reverse carrying the same unoriented Einstein metric. This correlation is structural, "
        "not accidental: compatible bubbling is holomorphic/algebraic and lands where "
        "algebraic geometry already supplies a metric."
    ),
    "content": (
        "Yau Problem 26 in dimension four (noncollapsed) is at least as hard as producing "
        "Einstein metrics on simply connected closed 4-manifolds with b₊ ≥ 2 and no "
        "monopole classes. That is a real result about the difficulty of the problem, "
        "not progress toward its resolution."
    ),
    "untouched": [
        "Positive collapse (n=4)",
        "Negative collapse and diameter escape (n=4)",
        "Non-SU(2) ALE bubbles",
        "All dimensions n ≥ 5",
        "The H4-dual normalized-flux necessity bridge",
        "Lean formalization obligation",
    ],
}

# ============================================================
# Write output
# ============================================================
import os, pathlib
_script_dir = pathlib.Path(__file__).resolve().parent
_ws = _script_dir.parent          # workspace/
out_path = str(_ws / "data" / "step57_dichotomy_and_kahler_exclusion.json")
os.makedirs(os.path.dirname(out_path), exist_ok=True)
with open(out_path, 'w') as f:
    json.dump(result, f, indent=2)

print(json.dumps({
    "status": "ok",
    "output": out_path,
    "kahler_excluded_range": "r=1,...,35 (both orientations)",
    "simply_connected_all_rows": True,
    "HT_strict_all_genus_h_ge_2": True,
    "bauer_furuta_reaches_mixed_rows": False,
    "biquard_source_retrieved": False,
    "live_representatives_h2": list(range(1,19)),
}, indent=2))

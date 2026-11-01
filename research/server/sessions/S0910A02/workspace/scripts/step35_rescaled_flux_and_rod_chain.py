#!/usr/bin/env python3
"""
Step 35: execute two route-changing checks for Yau26 Route A / collapsed front.

1. Rescaled bubble-frame Wronskian check: distinguish reading the growing H_2
   coefficient by pairing with r^{-4} (log if one transports inward through a
   long neck) from reading the decaying H^4 coefficient by pairing with r^2
   (fixed-R or power-bounded, no log in t). This is arithmetic/model evidence,
   not a full nonlinear proof.

2. Collapsed toric rod-chain check: in the alpha-family, rod length and rod
   spacing are the same A^{-1/2} order. Rescaling by sqrt(A) produces a chain,
   not a single isolated Schwarzschild bolt. Energy per rod is 8*pi^2; if chi
   rods saturate 8*pi^2 chi, any independent nut energy would force a CGB
   contradiction. This is bookkeeping/model evidence, not a global metric.
"""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "step35_rescaled_flux_and_rod_chain.json"
OUT.parent.mkdir(parents=True, exist_ok=True)

# ---------- Part A: Wronskian / variation-of-parameters scalings ----------
# Radial l=2 operator in 4D: L f = f'' + 3 f'/r - 8 f/r^2.
# Homogeneous y_grow=r^2, y_decay=r^-4. W = y_grow*y_decay' - y_grow'*y_decay = -6 r^-3.
# Coefficient variations for L f = S use:
#   a_grow'(r) = - y_decay*S/W = (1/6) r^{-1} S    (up to sign convention)
#   a_decay'(r) =  y_grow*S/W = -(1/6) r^5 S.
# Thus reading growing coeff over [r0,r1] has int S dr/r; reading decaying coeff has int S r^5 dr.

def grow_coeff_contamination_constS(delta, r0, r1):
    return (delta / 6.0) * math.log(r1 / r0)

def decay_coeff_contamination_constS(delta, r0, r1):
    return (delta / 36.0) * (r1**6 - r0**6)

# Bubble-frame model from strategist: ghat=t^{-2}g, |E|_ghat <= t^2 delta as (0,2)-scale,
# ambient quadratic term signal coefficient is t^2 * (R_+ v), and nonconservation
# over fixed rho in [1,R] is t^2 delta log R when pairing against the decaying test.
# Relative error = delta log R + tail matching O(1/R), with limits delta->0 then R->infty.

sample_deltas = [1e-1, 1e-2, 1e-3, 1e-4]
fixed_Rs = [2, 5, 10, 50, 100]
tiny_ts = [1e-3, 1e-9, 1e-30]

rescaled_table = []
for delta in sample_deltas:
    for R in fixed_Rs:
        rel = delta * math.log(R) + 1.0 / R
        rescaled_table.append({"delta": delta, "R": R, "relative_error_delta_logR_plus_tail": rel})

old_neck_log_table = []
for delta in [1e-2, 1e-4]:
    for t in tiny_ts:
        # Old reading growing coefficient from ALE scale to balance scale.
        r0 = math.sqrt(t)
        r_bal = t ** (2.0/3.0)
        # Note for t<1, sqrt(t) > t^(2/3)? e.g. .0316 > .01; interval orientation changes.
        # Absolute log magnitude is what mattered in Step 34.
        logmag = abs(math.log(r_bal / r0))
        old_neck_log_table.append({
            "delta": delta,
            "t": t,
            "r_ALE_sqrt_t": r0,
            "r_balance_t_2over3": r_bal,
            "abs_delta_log_ratio_over_6": (delta/6.0)*logmag,
            "relative_log_magnitude_delta_log_1_over_t": delta*math.log(1/t)
        })

# Formal proof of no t-coupling in iterated limit: for epsilon choose R>2/epsilon then delta<epsilon/(2 log R)
iterated_limit_certificate = []
for eps in [1e-1, 1e-2, 1e-3]:
    # Choose R so the tail is at most eps/8, then choose delta so the log term
    # is at most eps/2.  This leaves strict room below eps.
    R = max(10.0, 8.0/eps)
    delta_bound = (eps/2.0) / math.log(R)
    rel_at_bound = delta_bound*math.log(R) + 1.0/R
    iterated_limit_certificate.append({
        "epsilon": eps,
        "choose_R": R,
        "tail_1_over_R": 1.0/R,
        "then_delta_less_than": delta_bound,
        "relative_error_bound_at_delta_bound": rel_at_bound,
        "less_than_epsilon": rel_at_bound < eps
    })

wronskian_scalings = {
    "radial_operator": "L f = f'' + 3 f'/r - 8 f/r^2; y_grow=r^2, y_decay=r^-4, W=-6 r^-3",
    "coefficient_variations": {
        "read_growing_coefficient_with_decay_test": "a_grow' ~ S/r -> integral S dr/r, logarithmic across a long neck",
        "read_decaying_coefficient_with_growing_test": "a_decay' ~ S r^5 -> integral S r^5 dr, power/fixed-scale, no log(1/t)"
    },
    "old_neck_log_table": old_neck_log_table,
    "rescaled_bubble_frame": {
        "statement": "With ghat=t^{-2}g, Ricci defect scale in bubble frame is t^2 delta; ambient quadratic signal is t^2(R_+ v). On rho in [1,R] with fixed R, relative Wronskian nonconservation is O(delta log R)+O(1/R), no log(1/t).",
        "relative_error_samples": rescaled_table,
        "iterated_limit_certificate": iterated_limit_certificate,
        "conclusion": "The Step-34 condition delta log(1/t)->0 is an artifact of reading/transporting the H2 coefficient through the neck. In the bubble-frame fixed-R comparison, one first lets delta_i->0 for fixed R, then R->infty; no rate coupling between t_i and delta_i is forced by this model."
    },
    "actual_remaining_input": "Need existence of a second-order blow-up k = lim (ghat_i - EH)/t_i^2 solving DRic_EH(k)=Lambda EH + O(delta_i) with quadratic growth, and matching of k's quadratic part to the orbifold 2-jet. C^{1,alpha} cap W^{2,q} convergence alone does not transmit a 2-jet for non-Einstein g_i."
}

# ---------- Part B: toric rod chain / ALF bookkeeping ----------
# Use Step 19/25/34 formulas for formal alpha-family rods:
# A_m=m^alpha, rod length L=pi/sqrt(1+2A), flux Phi=2/(1+2A), bolt energy 8*pi^2.
# Spacing is same order as rod length in the polygon model, so rescaling by sqrt(A) yields finite spacing.

alphas = [1.1, 1.5, 2.0]
ms = [8, 32, 128, 512]
rod_chain_rows = []
for alpha in alphas:
    for m in ms:
        A = m**alpha
        L = math.pi / math.sqrt(1 + 2*A)
        # rescale distances by sqrt(2A) (as in Step 34 Schwarzschild rescaling)
        L_hat = math.sqrt(2*A) * L
        # Step 34 mass parameter
        M_hat = math.sqrt(2*A) * (A + 1/3) / ((2*A + 1)**1.5)
        mu = (2*((-1+math.sqrt(9+24*A))/2) + 1) / (((-1+math.sqrt(9+24*A))/2)*(((-1+math.sqrt(9+24*A))/2)+2))
        phi = 2/(1+2*A)
        rod_chain_rows.append({
            "alpha": alpha,
            "m_rods": m,
            "A": A,
            "rod_length_L": L,
            "scaled_length_sqrt2A_L": L_hat,
            "limit_scaled_length_pi": math.pi,
            "relative_error_scaled_length": abs(L_hat-math.pi)/math.pi,
            "Schwarzschild_M_hat": M_hat,
            "M_hat_error_from_half": abs(M_hat-0.5),
            "smoothness_ratio_mu": mu,
            "cone_defect_1_minus_mu": 1-mu,
            "per_rod_flux_phi": phi,
            "total_flux_m_phi": m*phi
        })

energy_rows = []
for chi in [4, 10, 50, 200]:
    for rods in [chi, max(0, chi-2)]:
        bolt_energy = rods * 8 * math.pi**2
        cgb_limit = chi * 8 * math.pi**2
        slack = cgb_limit - bolt_energy
        energy_rows.append({
            "chi": chi,
            "rod_count_model": rods,
            "bolt_energy_total": bolt_energy,
            "CGB_collapse_limit_8pi2_chi": cgb_limit,
            "slack_for_nuts_or_other_curvature": slack,
            "no_slack_if_rods_equal_chi": rods == chi
        })

rod_chain_bookkeeping = {
    "formulas": {
        "rod_length": "L=pi/sqrt(1+2A)",
        "scaled_length": "sqrt(2A)*L -> pi, so neighboring rods/nuts remain at finite separation after bolt rescaling if rod spacing is same order",
        "mass": "Mhat=sqrt(2A)(A+1/3)/(2A+1)^(3/2)->1/2",
        "energy_per_rod": "8*pi^2, same as Euclidean Schwarzschild ALF quantum",
        "smoothness_ratio": "mu(A)<1 for A>0 and ->0 as A->infty; two-bolt exact positive Einstein closure smooth only at A=0"
    },
    "rod_chain_rows": rod_chain_rows,
    "energy_no_slack_rows": energy_rows,
    "interpretation": "The rescaled collapsed limit is not an isolated single Schwarzschild bolt if adjacent rod lengths/spacings are also A^{-1/2}; it is a periodic/infinite toric Ricci-flat rod-chain problem. If each topological rod consumes 8*pi^2 and the CGB collapse limit supplies exactly 8*pi^2 chi, any additional independent nut/strut curvature energy would contradict no-slack. If a periodic strut-free Weyl solution exists, it becomes a BREAK model rather than an obstruction."
}

result = {
    "title": "Step 35 rescaled flux correction and toric ALF rod-chain bookkeeping",
    "scope": "Execution-level checks for four-dimensional positive noncollapsed/collapsed subroutes; not a proof/refutation of Yau-26.",
    "wronskian_scalings": wronskian_scalings,
    "rod_chain_bookkeeping": rod_chain_bookkeeping,
    "source_status": {
        "Cheeger_Naber": "Local Knowledge source confirms bounded Ricci + noncollapse gives harmonic-radius weak type estimates and cone-annulus control; exact Anderson 1989 source not acquired in this script.",
        "edge_cone_Weyl_sources": "Knowledge requests in this step did not retrieve source-grade Atiyah-LeBrun or Israel-Khan/Myers texts; claims about struts/periodic arrays remain literature targets, not source-established in this session."
    }
}

OUT.write_text(json.dumps(result, indent=2), encoding="utf-8")
print(json.dumps({
    "output": str(OUT),
    "rescaled_limit_all_certificates_pass": all(row["less_than_epsilon"] for row in iterated_limit_certificate),
    "scaled_length_last_rows": [rod_chain_rows[-4], rod_chain_rows[-1]],
    "key_conclusion": wronskian_scalings["rescaled_bubble_frame"]["conclusion"]
}, indent=2))

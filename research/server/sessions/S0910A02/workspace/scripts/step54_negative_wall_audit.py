#!/usr/bin/env python3
"""
Step 54 audit computations for the Yau-26 negative ADE wall.

The script records exact finite checks, not theorem proofs:
  * Correct the Step-53 LeBrun table at p=1/3: LeBrun nonexistence includes
    k >= A/3, while the stable pinching margin from Steps 3-4 is strict only for p>1/3.
  * Verify a concrete projective quintic surface with one ordinary double point:
        F = z^3 (x^2+y^2+w^2) + h_5(x,y,w),
        h_5=x^5+y^5+w^5+x*y*w^3.
    In the affine chart z=1, the singular equations have only x=y=w=0.
    In the hyperplane z=0, the plane quintic h_5=0 is smooth by affine-chart
    Groebner checks. Hence the projective hypersurface has exactly one singular
    point [0:0:0:1], with nondegenerate quadratic term x^2+y^2+w^2: an A1 node.
  * Record canonical-class arithmetic: for a degree-d hypersurface in CP^3,
    K_X = O_X(d-4); for d=5 it is ample on the canonical model. The crepant
    minimal resolution of an A1 point preserves K^2 but contains a (-2)-curve E
    with K.E=0, so K is nef and big but not ample.
  * Check the Burns potential determinant used in Step 53.
"""
from __future__ import annotations

import json
import math
from fractions import Fraction
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "workspace" / "data"
DATA.mkdir(parents=True, exist_ok=True)


def stable_pinching_gap(p: Fraction) -> dict:
    threshold = Fraction(1, 3)
    lebrun_nonexistence_applies = p >= threshold
    if p <= threshold:
        margin = None
        delta = None
        margin_note = "stable Steps-3-4 pinching margin is zero/not strict at p<=1/3"
    else:
        root = math.sqrt(float((p - threshold) / 2))
        delta = root / (1 + root)
        margin = f"sqrt(({p}-1/3)/2)"
        margin_note = "strict stable pinching margin for p>1/3"
    return {
        "p": str(p),
        "LeBrun_nonexistence_k_ge_A_over_3_applies": lebrun_nonexistence_applies,
        "strict_pinching_margin_formula": margin,
        "delta_lower_bound_numeric_if_strict": delta,
        "distinction": margin_note,
    }


def groebner_is_origin_only(eqs, vars_) -> tuple[bool, list[str]]:
    G = sp.groebner(eqs, *vars_, order="lex")
    basis = [str(g.as_expr()) for g in G.polys]
    wanted = {str(v) for v in vars_}
    return set(basis) == wanted, basis


def check_plane_quintic_smooth(h5, x, y, w) -> dict:
    # Projective smoothness of h5=0 in P^2: in each chart x=1, y=1, w=1,
    # the equations h5=dh/du=dh/dv=0 have no affine solution.  We check by
    # Groebner basis [1].  This is faster than a homogeneous saturation.
    charts = {}
    for chart_var, subs, free in [
        ("x=1", {x: 1}, (y, w)),
        ("y=1", {y: 1}, (x, w)),
        ("w=1", {w: 1}, (x, y)),
    ]:
        f = sp.expand(h5.subs(subs))
        eqs = [f] + [sp.diff(f, v) for v in free]
        G = sp.groebner(eqs, *free, order="lex")
        basis = [str(g.as_expr()) for g in G.polys]
        charts[chart_var] = {"groebner_basis": basis, "no_affine_solution": basis == ["1"]}
    return {"charts": charts, "smooth": all(c["no_affine_solution"] for c in charts.values())}


def check_nodal_quintic() -> dict:
    x, y, w, z = sp.symbols("x y w z")
    q = x*x + y*y + w*w
    h5 = x**5 + y**5 + w**5 + x*y*w**3
    F = z**3 * q + h5

    # z=1 chart: singular point conditions F=Fx=Fy=Fw=Fz=0 reduce to
    # q=0 and grad(q+h5)=0; F itself then equals h5, but Euler and q/gradient
    # imply it in this checked zero-dimensional situation, so we include it for safety.
    f_aff = q + h5
    z1_eqs = [q, f_aff, sp.diff(f_aff, x), sp.diff(f_aff, y), sp.diff(f_aff, w)]
    z1_origin_only, z1_basis = groebner_is_origin_only(z1_eqs, (x, y, w))

    # Hyperplane z=0: since F_z=3 z^2 q=0, singularity is singularity of plane h5=0.
    plane = check_plane_quintic_smooth(h5, x, y, w)

    H0 = sp.hessian(f_aff, (x, y, w)).subs({x: 0, y: 0, w: 0})
    det_H0 = sp.det(H0)
    d = 5
    return {
        "homogeneous_quintic_F": str(F),
        "z_eq_1_singular_groebner_basis": z1_basis,
        "z_eq_1_only_origin": z1_origin_only,
        "z_eq_0_plane_quintic_smooth_check": plane,
        "projective_singular_locus": "exactly [0:0:0:1]" if z1_origin_only and plane["smooth"] else "check failed",
        "local_affine_equation_z_eq_1": str(f_aff),
        "quadratic_part": str(q),
        "hessian_at_node": [[int(H0[i, j]) for j in range(3)] for i in range(3)],
        "hessian_det": int(det_H0),
        "ordinary_double_point_A1": bool(det_H0 != 0 and z1_origin_only and plane["smooth"]),
        "canonical_model_K": "For degree d=5 hypersurface in CP^3, K_X=O_X(d-4)=O_X(1), ample on the canonical model.",
        "canonical_square": d * (d - 4) ** 2,
        "crepant_resolution_K": "Resolving the A1 rational double point is crepant: K_M=pi^*K_X and K^2 remains 5.",
        "not_ample_on_resolution": "The exceptional curve E has E^2=-2 and K_M.E=0, so K_M is nef and big but not ample.",
    }


def burns_check() -> dict:
    s = sp.symbols("s", positive=True)
    det_g = 1 + 1/s
    fp = sp.diff(sp.log(det_g), s)
    return {
        "potential": "phi(s)=s+log(s), s=|z|^2, complex dimension 2",
        "det_g": str(det_g),
        "d_log_det_ds": str(sp.simplify(fp)),
        "ricci_form_nonzero": True,
        "scalar_flat_not_Ricci_flat": True,
        "scaled_operator_norm": "nonzero Ricci endomorphism of t*g_Burns is order t^{-1}, so a Burns (-1)-bubble is visible to ||Ric+g||_op",
    }


result = {
    "lebrun_threshold_correction": {
        "message": "LeBrun nonexistence uses k>=A/3; the strict near-pinching lower margin from Steps 3-4 is positive only for p=k/A>1/3.",
        "rows": [stable_pinching_gap(p) for p in [Fraction(0, 1), Fraction(1, 3), Fraction(2, 5), Fraction(2, 3), Fraction(1, 1)]],
    },
    "explicit_A1_negative_KE_orbifold_model": check_nodal_quintic(),
    "burns_noncrepant_check": burns_check(),
    "volume_escape_constants": {
        "if_Ric_plus_g_op_le_delta": {
            "scalar_range_4d": "s in [-4(1+delta), -4(1-delta)]",
            "volume_from_scalar_integral": "If LeBrun gives int s^2 >= 32*pi^2*A, then Vol >= 32*pi^2*A / (16(1+delta)^2) = 2*pi^2*A/(1+delta)^2.",
            "CGB_warning": "For varying general-type geography, c2 and A both vary; this bounded check does not prove a family-uniform volume theorem beyond the selected geography.",
            "verdict": "Global volume escape is not the leading fixed-topology loophole; local collapse/curvature concentration remains the serious gap. Family-uniform constants require geography bounds, not established here."
        }
    },
    "reduction_shape": {
        "negative_wall_candidate": "For any canonical surface/orbifold X0 with ample K and ADE points admitting its negative KE orbifold metric, the crepant minimal resolution M has explicit near-negative-Einstein metrics from compatible Ricci-flat ADE bubbles when the first obstruction vector lies in the KE kernel. Thus P4^- would imply that M carries some Einstein metric.",
        "not_a_counterexample": "The session has not proved that such M carries no Einstein metric of any sign; it only lacks the Aubin-Yau KE metric in its resolved complex structure and is not reached by LeBrun blow-up nonexistence.",
        "known_residual_loopholes_ranked": [
            "1. Smooth Einstein nonexistence on minimal general-type resolutions with (-2)-curves is not known in the session record; this is exactly why the statement is a hardness reduction, not a refutation.",
            "2. Local collapse/diameter escape in negative sign remains outside Cheeger-Naber noncollapsed ALE analysis and outside Min-Oo because d^2 max|K| may blow up.",
            "3. Non-Kähler Ricci-flat ALE bubbles or non-SU(2) asymptotics need classification/source closure; current session has not proved they all preserve K^2.",
            "4. The full H4-dual necessity bridge for arbitrary near-pinched sequences remains unproved; the explicit construction side is stronger than the necessity side.",
            "5. n>=5 codimension-four stratum obstruction is only a programme, not a next theorem."
        ],
    },
    "A03_step54_negative_flow_status": {
        "accepted_correction": "A02 should withdraw the strong A^{-1/2} impossibility interpretation from Step 52/53; A03 notes volume-weighted eligible cores can cancel A in the terminal average, so c/sqrt(A) was at most a sufficient estimate from one crude bound.",
        "still_unproved": "A03 Step54 also withdraws its Step53 Theorem 5.1: the coupled start theorem is not proved; a triangular output-velocity iteration is pending verification.",
        "allocation": "The negative flow chain remains conditional rather than refuted; A02 should not cite either family-uniform success or A^{-1/2} impossibility."
    }
}

out = DATA / "step54_negative_wall_audit.json"
out.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
print(json.dumps({
    "status": "ok",
    "output": str(out.relative_to(ROOT)),
    "node_check": result["explicit_A1_negative_KE_orbifold_model"]["ordinary_double_point_A1"],
    "projective_singular_locus": result["explicit_A1_negative_KE_orbifold_model"]["projective_singular_locus"],
    "p_1_3_row": result["lebrun_threshold_correction"]["rows"][1],
    "A03_flow_status": result["A03_step54_negative_flow_status"],
}, indent=2))

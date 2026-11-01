"""
Step 15 (S0910A02): boundary-bubble / pinched-relaxation probes for the
positive toric volume-gap fork.

Purpose
-------
Do NOT solve the exact reduced Einstein system on m=8,10 polygons: exact
smooth toric/Hermitian positive Einstein examples are classified/known only in
small corner counts, and exact-system failure for m>6 is not evidence about
Yau-26 pinched metrics.  Instead test the enemy identified in Steps 13--14 and
by the Step-15 strategist note:

    volume collapse in the invariant class, if possible, should look like
    localized negative base curvature on rods / shrinking fixed-sphere bolts,
    i.e. an Eguchi--Hanson/ALE boundary bubble at each rod.

This script implements two levels of computable relaxation.

R0: edge-ODE + spectral/GB scaling model.
    Each rod has constant edge curvature K_B=-A, hence fixed-sphere meridian
    equation Q'' + (1+2A) Q = 0 with unit closure.  Rod flux Phi=2/(1+2A).
    Taking A=m^2 gives total flux ~2/m -> 0 while the base area is kept fixed
    above the Faber--Krahn floor and negative base curvature is localized in
    thin collars.  This proves the *coarse 2D constraints alone* cannot give
    the volume gap.

R1: local Ricci-pinching jet test near one shrinking rod.
    Use Fermi coordinates (r,s) at a p=0 rod and the Step-12/14 boundary
    expansion for a twist-free metric
        g = dr^2 + a(r)^2 ds^2 + p(r)^2 dtheta^2 + q(r,s)^2 dphi^2,
    with K_B(rod)=-A, a(r)=cosh(sqrt(A) r),
        p(r)=r + p3 r^3,             p3=-A/3-1/6,
        q(r,s)=Q(s)*(1 + (A/2) r^2), Q=sin(omega s)/omega,
        omega^2=1+2A.
    The coefficients make the Einstein equations correct to leading order on
    the rod.  We sample at r=c/sqrt(A) and compute the exact Ricci operator of
    this truncated local model via multiply-warped product formulas.  This is
    *not* a construction of a closed metric; it tests whether C^0 pinching is
    immediately destroyed by large negative edge curvature or whether the
    obstruction is genuinely a higher/gluing obstruction.

Outputs are saved as JSON for later agents.
"""
import json, math, os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.abspath(os.path.join(HERE, "..", "data"))
os.makedirs(DATA, exist_ok=True)

j0 = 2.404825557695773
area_fk_delta0 = math.pi * j0**2 / 2.0


def rod_constant_A(A):
    omega2 = 1.0 + 2.0*A
    omega = math.sqrt(omega2)
    L = math.pi / omega
    Phi = 2.0 / omega2
    area_fixed_sphere = 2.0 * math.pi * Phi
    return dict(A=A, K_B_edge=-A, omega=omega, rod_length=L,
                rod_flux=Phi, fixed_sphere_area=area_fixed_sphere)


def r0_scaling(m, A=None, area_base=None):
    if A is None:
        A = float(m*m)
    if area_base is None:
        # Keep a fixed interior reservoir above Faber--Krahn; this makes
        # lambda_1 <= 2 plausible/easy in the relaxation rather than forcing
        # the base to shrink.
        area_base = max(10.0, 1.1*area_fk_delta0)
    rd = rod_constant_A(A)
    total_flux = m * rd["rod_flux"]
    vol4 = 2.0 * math.pi**2 * total_flux
    # Base GB target for all-right-angle disk-like m-gon.
    gb_target = 2.0*math.pi - 0.5*math.pi*m
    # If collars carry curvature about -A over total area gb_deficit/A, then
    # the negative integral matches the target up to whatever positive
    # curvature is placed in the reservoir.  For m>4 target is negative.
    # The per-edge collar area needed for the negative part alone:
    neg_needed = max(0.0, -gb_target)
    collar_area_total = neg_needed / A if A > 0 else float('inf')
    collar_area_per_edge = collar_area_total / m
    # with edge length L, a collar width of roughly collar_area_per_edge/L
    collar_width = collar_area_per_edge / rd["rod_length"] if rd["rod_length"] > 0 else float('inf')
    # Compare width with bubble length scale 1/sqrt(A).
    bubble_scale = 1.0 / math.sqrt(A) if A > 0 else float('inf')
    return dict(m=m, chi=m, A=A, area_base=area_base,
                area_fk_delta0=area_fk_delta0,
                lambda1_upper_target=2.0,
                GB_target=gb_target,
                rod=rd,
                total_flux=total_flux,
                volume4=vol4,
                collar_area_total_for_negative_GB=collar_area_total,
                collar_area_per_edge=collar_area_per_edge,
                collar_width_estimate=collar_width,
                bubble_scale=bubble_scale,
                width_over_bubble_scale=collar_width/bubble_scale if bubble_scale > 0 else None,
                interpretation=("R0 feasible scaling if only spectral area, GB, and edge unit-closure "
                                "constraints are imposed; it is not a Ricci-pinched metric."))


# ---------- R1 local Ricci operator for truncated edge model ----------
# Base metric dr^2 + a(r)^2 ds^2, fibers p^2 dtheta^2 + q^2 dphi^2.
# Ric_B = K_B g_B, K_B=-a_rr/a.
# Ric_base = Ric_B - Hess(p)/p - Hess(q)/q.
# Ric_theta/g_theta = -Delta p/p - <grad p,grad q>/(p q).
# Ric_phi/g_phi     = -Delta q/q - <grad p,grad q>/(p q).

def local_quantities(A, c=0.05, t=0.5):
    # A positive means K_B(edge)=-A.  Evaluate at r=c/sqrt(A), s=t*L.
    if A <= 0:
        raise ValueError("A must be positive")
    sqrtA = math.sqrt(A)
    omega2 = 1.0 + 2.0*A
    omega = math.sqrt(omega2)
    L = math.pi/omega
    r = c/sqrtA
    s = t*L
    # base coefficient a=cosh(sqrt(A) r), exact constant base curvature -A.
    a = math.cosh(sqrtA*r)
    ar = sqrtA*math.sinh(sqrtA*r)
    arr = A*math.cosh(sqrtA*r)
    KB = -arr/a
    # p expansion
    p3 = -A/3.0 - 1.0/6.0
    p = r + p3*r**3
    pr = 1.0 + 3.0*p3*r**2
    prr = 6.0*p3*r
    ps = 0.0
    pss = 0.0
    prs = 0.0
    # Q and q expansion
    Q = math.sin(omega*s)/omega
    Qs = math.cos(omega*s)
    Qss = -omega*math.sin(omega*s)  # = -omega^2 Q
    factor = 1.0 + 0.5*A*r**2
    q = Q*factor
    qr = Q*A*r
    qrr = Q*A
    qs = Qs*factor
    qss = Qss*factor
    qrs = Qs*A*r
    # Hessians in base coordinates.
    # Hess_rr=f_rr; Hess_ss=f_ss + a a_r f_r; Hess_rs=f_rs-(a_r/a)f_s.
    def hess(fr, frr, fs, fss, frs):
        hrr = frr
        hss = fss + a*ar*fr
        hrs = frs - (ar/a)*fs
        return hrr, hss, hrs
    hp_rr, hp_ss, hp_rs = hess(pr, prr, ps, pss, prs)
    hq_rr, hq_ss, hq_rs = hess(qr, qrr, qs, qss, qrs)
    # Laplacian and gradient product.
    def lap(fr, frr, fss):
        return frr + (ar/a)*fr + (1.0/a**2)*fss
    lap_p = lap(pr, prr, pss)
    lap_q = lap(qr, qrr, qss)
    gradpq = pr*qr + (1.0/a**2)*ps*qs
    # Coordinate Ricci components on base.
    Ric_rr = KB*1.0 - hp_rr/p - hq_rr/q
    Ric_ss = KB*a*a - hp_ss/p - hq_ss/q
    Ric_rs = - hp_rs/p - hq_rs/q
    # Endomorphism g^{-1}Ric on base in coordinate basis.
    base_end = np.array([[Ric_rr, Ric_rs/(a*a)], [Ric_rs, Ric_ss/(a*a)]], dtype=float)
    base_eigs = np.linalg.eigvals(base_end).real.tolist()
    Ric_theta = -lap_p/p - gradpq/(p*q)
    Ric_phi = -lap_q/q - gradpq/(p*q)
    eigs = base_eigs + [Ric_theta, Ric_phi]
    delta = max(abs(x-1.0) for x in eigs)
    return dict(A=A, c=c, t=t, r=r, s=s, L=L,
                p=p, q=q, a=a, K_B=KB,
                p3=p3,
                omega=omega,
                ricci_operator_eigenvalues=eigs,
                delta_from_Ric_equals_g=delta,
                base_endomorphism=base_end.tolist(),
                vertical_theta=Ric_theta,
                vertical_phi=Ric_phi,
                note=("Truncated edge expansion sampled at r=c/sqrt(A). "
                      "Small c tests a very thin collar near the rod; large A is the boundary-bubble limit."))


def scan_local():
    As = [4, 9, 16, 25, 64, 100, 400, 1600]
    cs = [0.01, 0.02, 0.05, 0.1, 0.2]
    ts = [0.25, 0.5, 0.75]
    table = []
    for A in As:
        for c in cs:
            deltas = []
            eig_min = 1e9
            eig_max = -1e9
            bad = 0
            for t in ts:
                try:
                    q = local_quantities(A, c=c, t=t)
                    deltas.append(q["delta_from_Ric_equals_g"])
                    eig_min = min(eig_min, min(q["ricci_operator_eigenvalues"]))
                    eig_max = max(eig_max, max(q["ricci_operator_eigenvalues"]))
                except Exception:
                    bad += 1
            table.append(dict(A=A, c=c, max_delta=max(deltas) if deltas else None,
                              eig_min=eig_min, eig_max=eig_max, bad=bad))
    # For each A, choose best c in the sampled set (min max_delta).
    best_by_A = []
    for A in As:
        rows = [r for r in table if r["A"] == A and r["max_delta"] is not None]
        best_by_A.append(min(rows, key=lambda r: r["max_delta"]))
    return table, best_by_A


r0_cases = [r0_scaling(m, A=float(m*m)) for m in [4, 6, 8, 10, 20, 50, 100]]
local_table, best_by_A = scan_local()
# Representative samples at A=m^2 and c=0.02,0.05.
representatives = []
for m in [6, 8, 10, 20, 50]:
    for c in [0.01, 0.02, 0.05]:
        representatives.append(local_quantities(float(m*m), c=c, t=0.5))

report = {
    "title": "Step 15 boundary-bubble pinched-relaxation probes",
    "source_scope_correction": {
        "exact_FEM_warning": "Solving exact Einstein equations on m=8,10 would test nonexistence/classification, not the delta-pinched volume-gap question.",
        "classification_status": "2311.04840 classifies T^2-invariant Einstein 4-manifolds only with nonnegative sectional curvature; LeBrun classifies Hermitian Einstein as KE or Page/CLW. General smooth T^2-invariant Einstein classification is not known from sources read here.",
    },
    "R0_edge_ODE_spectral_GB_relaxation": {
        "description": "Coarse necessary-condition model with constant K_B=-A on every rod, base area fixed above Faber-Krahn, and negative GB stored in thin boundary collars.",
        "cases": r0_cases,
        "finding": "Taking A=m^2 gives total_flux=2m/(1+2m^2) ~ 1/m and Vol4~2*pi^2/m, while the base area can remain above the spectral floor; hence spectral+GB+unit-closure alone cannot prove a chi-uniform volume gap.",
    },
    "R1_local_truncated_edge_Ricci_probe": {
        "metric": "dr^2+cosh(sqrt(A)r)^2 ds^2 + (r+(-A/3-1/6)r^3)^2 dtheta^2 + [sin(omega s)/omega*(1+A r^2/2)]^2 dphi^2, omega^2=1+2A",
        "table": local_table,
        "best_by_A": best_by_A,
        "representatives_midrod": representatives,
        "finding": "The boundary jet supports arbitrarily large negative K_B at r=0 by construction, but the naive third-order truncation is Ricci-close only in an extremely thin sub-collar; at r=c/sqrt(A) the defect is governed mainly by c and truncation error, not by m alone. This means local jets do not immediately forbid boundary bubbles, but a genuine delta-pinched family needs the full higher-order/ALE gluing obstruction analysis, not this truncated ansatz.",
    },
    "interpretation_for_Yau26": [
        "The computation does not prove or refute P_4^+.",
        "It refutes a possible shortcut: the unweighted spectral bound, Gauss-Bonnet, and rod unit-closure by themselves are too weak, because a relaxed edge-bubble scaling has total flux tending to zero.",
        "The decisive remaining BUILD/BREAK question is exactly the Biquard/Ozuch boundary-bubble obstruction: can the large negative edge-curvature/shrinking-bolt jets be extended around the polygon with C^0 Ricci defect tending to zero, or does the first obstruction produce an O(1) non-scalar Ricci defect as in the interior Eguchi-Hanson gluing normal form?",
    ],
}

OUT = os.path.join(DATA, "step15_boundary_bubble_relaxation.json")
with open(OUT, "w") as f:
    json.dump(report, f, indent=2)
print(json.dumps({
    "title": report["title"],
    "R0_summary": report["R0_edge_ODE_spectral_GB_relaxation"]["finding"],
    "R0_cases_brief": [
        {"m": c["m"], "A": c["A"], "total_flux": c["total_flux"],
         "Vol4": c["volume4"], "collar_width_over_scale": c["width_over_bubble_scale"]}
        for c in r0_cases
    ],
    "R1_best_by_A": best_by_A,
    "R1_midrod_samples": [
        {"A": q["A"], "c": q["c"], "delta": q["delta_from_Ric_equals_g"],
         "eigs": q["ricci_operator_eigenvalues"]}
        for q in representatives if q["A"] in [36.0,64.0,100.0]
    ],
    "saved": OUT,
}, indent=2))

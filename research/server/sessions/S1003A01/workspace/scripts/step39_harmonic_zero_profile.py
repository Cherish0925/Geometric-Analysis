"""Step 39: canonical harmonic self-dual form and singular AK pocket profile.

For an exact-CH perpendicular cell, let
    Omega = (1/2) d(phi sigma_f),  phi'/phi = 2 a_f/(a_g a_h),
normalized to the CH Kahler form on the exact collar.  In the original smooth
metric g,
    Omega = u^2 (e^{0f}+e^{gh}),  |Omega|_g^2 = 2 u^4,
so Omega is a smooth closed self-dual (hence harmonic) form with zero exceptional
period and a zero along the bolt.  On the complement of the zero set,
    ghat = u^2 g
is almost Kahler with |Omega|_ghat^2=2.  This script evaluates:
  * cohomological pinning and amplitude depletion for Omega in g;
  * the harmonic Weitzenbock gradient energy of Omega in g;
  * the formal hatted AK quantities s_hat, |nabla Omega|_ghat^2=4 nu^2,
    s_star=s_hat+4 nu^2 and the volume of s_star-positive pockets.

The hatted metric is singular at the bolt.  Its pocket values are mechanism
measurements for this realizable zero-form geometry, not an application of a
closed smooth almost-Kahler theorem.

Usage:
  python step39_harmonic_zero_profile.py RECORD --out OUTPUT.json [--n 5000]
"""
import argparse
import json
import sys
from pathlib import Path

import jax
import jax.numpy as jnp
import numpy as np
from scipy.integrate import cumulative_trapezoid

jax.config.update("jax_enable_x64", True)
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from perp_dual_cost import make_cell, load_record, seed_vector  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("record")
    ap.add_argument("--out", required=True)
    ap.add_argument("--n", type=int, default=5000)
    args = ap.parse_args()

    rec = load_record(args.record)
    x0 = float(rec["x0"])
    X = float(rec["X"])
    deg = int(rec.get("deg", rec.get("degU", 6)))
    cell = make_cell(x0, deg, 500, smooth_mode=True, X=X)
    z = jnp.asarray(seed_vector(cell, rec))
    prof = cell.prof_factory(z)

    def slots(x):
        G, h = prof(x)
        d = jnp.diag(h)
        return G, jnp.sqrt(jnp.array([d[2], d[1], d[0]]))  # (f,g,h)

    def jet(x):
        G, A = slots(x)
        Ax = jax.jacfwd(lambda xx: slots(xx)[1])(x)
        Axx = jax.jacfwd(jax.jacfwd(lambda xx: slots(xx)[1]))(x)
        Gx = jax.grad(lambda xx: slots(xx)[0])(x)
        At = 2 * jnp.sqrt(G) * Ax
        Att = 4 * G * Axx + 2 * Gx * Ax
        return G, A, At, Att

    ell = np.log(X / x0)
    # Resolve the bolt powers and the mesoscopic transition independently.
    edges = np.unique(np.concatenate([
        [0.0],
        np.geomspace(1e-10, 1e-3, 50),
        np.geomspace(1e-3, 5e-2, 35),
        np.linspace(5e-2, 1.0, max(80, args.n // 20)),
    ]))
    gx, gw = np.polynomial.legendre.leggauss(20)
    uq = np.concatenate([(lo + hi) / 2 + (hi - lo) / 2 * gx for lo, hi in zip(edges[:-1], edges[1:])])
    wu = np.concatenate([(hi - lo) / 2 * gw for lo, hi in zip(edges[:-1], edges[1:])])
    xs = x0 * np.exp(ell * uq)
    wx = wu * ell * xs

    G, A, At, Att = [np.asarray(v) for v in jax.vmap(jet)(jnp.asarray(xs))]
    af, ag, ah = A.T
    y = At / A
    yt = Att / A - y**2
    S = y.sum(1)
    W = af * ag * ah
    dtdx = 1 / (2 * np.sqrt(G))

    def integ_dt(f):
        return float(np.sum(f * dtdx * wx))

    # Canonical potential, accurately normalized from the outer collar.
    ud = np.concatenate([np.geomspace(1e-12, 1e-3, 30000, endpoint=False), np.linspace(1e-3, 1.0, 250000)])
    xd = x0 * np.exp(ell * ud)
    Gd, Ad = [np.asarray(v) for v in jax.vmap(slots)(jnp.asarray(xd))]
    phit_over_phi_dtdu = 2 * Ad[:, 0] / (Ad[:, 1] * Ad[:, 2]) * (1 / (2 * np.sqrt(Gd))) * ell * xd
    Ld = cumulative_trapezoid(phit_over_phi_dtdu, ud, initial=0.0)
    Ld -= Ld[-1]
    logphi = np.log(X) + np.interp(uq, ud, Ld)
    phi = np.exp(logphi)
    u2 = phi / (ag * ah)
    u = np.sqrt(u2)
    qform = 2 * u2**2  # |Omega|_g^2 for Omega=(1/2)d(phi sigma_f)

    # Curvature in the original metric.
    def Porb(ai, aj, ak):
        return 2 * (ai**4 - (aj**2 - ak**2)**2) / W**2

    Porb_all = np.stack([Porb(af, ag, ah), Porb(ag, ah, af), Porb(ah, af, ag)], 1)
    R00 = -(yt + y**2).sum(1)
    Rii = -yt - S[:, None] * y + Porb_all
    scal = R00 + Rii.sum(1)

    gam = np.stack([
        (ag**2 + ah**2 - af**2) / (ag * ah),
        (ah**2 + af**2 - ag**2) / (ah * af),
        (af**2 + ag**2 - ah**2) / (af * ag),
    ], 1)

    def gdot(ai, aj, ak, di, dj, dk):
        num = aj**2 + ak**2 - ai**2
        den = aj * ak
        return (2 * (aj * dj + ak * dk - ai * di) * den - num * (dj * ak + aj * dk)) / den**2

    dfa, dga, dha = At.T
    gamt = np.stack([
        gdot(af, ag, ah, dfa, dga, dha),
        gdot(ag, ah, af, dga, dha, dfa),
        gdot(ah, af, ag, dha, dfa, dga),
    ], 1)
    v = At - gam
    vt = Att - gamt
    vj = np.roll(v, -1, 1)
    vk = np.roll(v, -2, 1)
    aj = np.roll(A, -1, 1)
    ak = np.roll(A, -2, 1)
    Rp = -vt / (2 * A) + (-v - vj * vk / 2) / (aj * ak)
    Wplus = Rp - scal[:, None] / 12
    Wff = Wplus[:, 0]

    # In the rescaled Ric=-g metric gbar=6g, psibar=6 Omega still has q=|psibar|^2=qform.
    # The negative-Kahler branch A_{psi,1/2} pulls back to the original-scale operator
    # 6 A = diag(-2q,q,q).  Thus this is the scale-invariant Kähler-model Weyl error.
    kahler_target_original_scale = np.stack([-2 * qform, qform, qform], 1)
    kahler_weyl_error = integ_dt(W * np.sum((Wplus - kahler_target_original_scale)**2, axis=1))

    # Smooth harmonic form: Weitzenbock identity gives its gradient energy.
    grad_density = W * qform * (2 * Wff - scal / 3)
    grad_energy = integ_dt(grad_density)

    # Conformal AK structure on the complement of the bolt.
    lam0 = 2 * af / (ag * ah)
    upr = 0.5 * u * (lam0 - y[:, 1] - y[:, 2])
    lam0t = lam0 * (y[:, 0] - y[:, 1] - y[:, 2])
    nut_conf = 0.5 * (lam0t - yt[:, 1] - yt[:, 2])
    upp = u * (nut_conf + (0.5 * (lam0 - y[:, 1] - y[:, 2]))**2)
    shat = (-6 * (upp + S * upr) + scal * u) / u**3
    qshape = np.log(ag / ah)
    qshape_t = y[:, 1] - y[:, 2]
    nu = -(qshape_t + 4 * np.sinh(qshape) / af) / (2 * u)
    torsion = 4 * nu**2
    sstar = shat + torsion
    dVhat_dt = W * u**4
    pocket = sstar >= 0
    Vhat = integ_dt(dVhat_dt)
    Vpos = integ_dt(dVhat_dt * pocket)
    int_torsion = integ_dt(dVhat_dt * torsion)
    int_sstar_pos = integ_dt(dVhat_dt * np.maximum(sstar, 0))
    int_sstar = integ_dt(dVhat_dt * sstar)

    # Locate radial components of the pocket on the quadrature sample.
    transitions = np.flatnonzero(pocket[1:] != pocket[:-1]) + 1
    bounds = [0] + transitions.tolist() + [len(xs)]
    comps = []
    for lo, hi in zip(bounds[:-1], bounds[1:]):
        if pocket[(lo + hi - 1) // 2]:
            comps.append({
                "x_lo": float(xs[lo]),
                "x_hi": float(xs[hi - 1]),
                "t_proxy_lo": float(np.arcsinh(np.sqrt(xs[lo]))),
                "t_proxy_hi": float(np.arcsinh(np.sqrt(xs[hi - 1]))),
                "sample_sstar_max": float(np.max(sstar[lo:hi])),
            })

    # Host conversion in the Ric=-6 normalization: V_host/(2 pi^2)=A/36.
    pocket_fraction_coefficient_per_k_over_A = 36 * Vpos
    torsion_per_cell_over_2pi2 = int_torsion

    amp_defect_original = integ_dt(W * (qform - 2)**2)
    # Under gbar=6g and psibar=6 Omega: q is unchanged, Weyl L2 is unchanged,
    # dV multiplies by 36, and the one-derivative two-form energy multiplies by 6.
    amp_defect_ric_minus_one = 36 * amp_defect_original
    grad_energy_ric_minus_one = 6 * grad_energy
    # The record stores P and J in 8*pi^2 units.  Use P for the trace-free-Ricci
    # branch numerator, and J for the full |Ric+g|^2 numerator; they differ by
    # the scalar-deviation term unless s is exactly constant.
    pnorm = float(rec.get("P", rec.get("P_direct", np.nan)))
    jnorm = float(rec.get("J", rec.get("cost", np.nan)))
    ricci_tracefree_over_2pi2 = 4 * pnorm
    einstein_residual_over_2pi2 = 4 * jnorm
    scalar_deviation_over_2pi2 = einstein_residual_over_2pi2 - ricci_tracefree_over_2pi2
    branch_P_over_2pi2 = ricci_tracefree_over_2pi2 + kahler_weyl_error + amp_defect_ric_minus_one
    branch_J_over_2pi2 = einstein_residual_over_2pi2 + kahler_weyl_error + amp_defect_ric_minus_one

    out = {
        "record": args.record,
        "normalization": "profile uses Ric_CH=-6g; raw one-derivative and volume-weighted form integrals are converted explicitly below to gbar=6g, Ric=-g; reported integrals divide actual values by 2*pi^2 unless dimensionless",
        "form": {
            "Omega": "(1/2)d(phi sigma_f), equal to the host Kahler form on the collar",
            "closed_self_dual_harmonic": True,
            "exceptional_period": 0.0,
            "bolt_zero": True,
            "q_equals_norm_squared": "2*u^4",
        },
        "x0": x0,
        "X": X,
        "pinning": {
            "int_dVhat": Vhat,
            "expected_X2_over_4": X**2 / 4,
            "residual": Vhat - X**2 / 4,
            "int_q_dV_g": integ_dt(W * qform),
            "expected_X2_over_2": X**2 / 2,
        },
        "smooth_harmonic_form_on_g": {
            "profile_scale_int_q_minus_2_sq": amp_defect_original,
            "profile_scale_int_two_minus_q": integ_dt(W * (2 - qform)),
            "profile_scale_int_grad_Omega_sq_by_integrated_Weitzenbock": grad_energy,
            "ric_minus_one_int_q_minus_2_sq": amp_defect_ric_minus_one,
            "ric_minus_one_int_grad_psibar_sq": grad_energy_ric_minus_one,
            "int_Wplus_minus_negative_Kahler_model_sq_scale_invariant": kahler_weyl_error,
            "ric_minus_one_tracefree_Ricci_P_over_2pi2": ricci_tracefree_over_2pi2,
            "ric_minus_one_full_Einstein_residual_J_over_2pi2": einstein_residual_over_2pi2,
            "ric_minus_one_scalar_deviation_over_2pi2": scalar_deviation_over_2pi2,
            "ric_minus_one_branch_P_numerator_over_2pi2": branch_P_over_2pi2,
            "ric_minus_one_branch_J_numerator_over_2pi2": branch_J_over_2pi2,
            "ric_minus_one_branch_P_plus_derivative_over_2pi2": branch_P_over_2pi2 + grad_energy_ric_minus_one,
            "ric_minus_one_branch_J_plus_derivative_over_2pi2": branch_J_over_2pi2 + grad_energy_ric_minus_one,
            "weitz_integrand_min_not_pointwise_gradient_density": float(np.min(grad_density)),
            "u_min_sample": float(np.min(u)),
            "u_max_sample": float(np.max(u)),
        },
        "singular_hatted_AK_mechanism": {
            "scope": "ghat=u^2 g is singular at the bolt; pocket statistics do not invoke a closed smooth AK theorem",
            "profile_scale_int_torsion_4nu2": int_torsion,
            "ric_minus_one_int_torsion_4nu2": 6 * int_torsion,
            "int_sstar": int_sstar,
            "int_positive_part_sstar": int_sstar_pos,
            "positive_pocket_volume": Vpos,
            "positive_pocket_fraction_of_replaced_CH_ball": Vpos / Vhat,
            "positive_pocket_fraction_global_coefficient_per_k_over_A": pocket_fraction_coefficient_per_k_over_A,
            "pocket_components": comps,
            "sstar_sample_range": [float(np.min(sstar)), float(np.max(sstar))],
        },
        "cohomology_on_a_closed_CH_host": {
            "class": "the pullback of the host Kahler class: collar matching and zero exceptional periods",
            "period_angle_eta": 1.0,
            "exceptional_area_alpha": 0.0,
            "scope": "eta=1 is topological for this fixed pullback class on a negative KE host; an unrestricted harmonic/self-dual direction may drift outside this Hodge-index plane",
            "AKGamma_not_applicable": "Omega has zeros and ghat is singular",
        },
        "global_sparse_replication": {
            "host_normalized_volume_V_over_2pi2": "A/36",
            "if_disjoint_cells_are_glued": "global pocket fraction = (36*Vpos)*(k/A); in Ric=-g normalization the branch average over the reference host volume is branch_per_cell*(k/A), with actual final-volume correction at finite density",
            "profile_scale_torsion_per_cell_over_2pi2": torsion_per_cell_over_2pi2,
            "ric_minus_one_torsion_per_cell_over_2pi2": 6 * torsion_per_cell_over_2pi2,
            "negative_Kahler_branch_P_average_coefficient_per_k_over_A": branch_P_over_2pi2,
            "negative_Kahler_branch_J_average_coefficient_per_k_over_A": branch_J_over_2pi2,
            "negative_Kahler_branch_derivative_average_coefficient_per_k_over_A": grad_energy_ric_minus_one,
        },
        "sample_consistency": {
            "max_rel_kappa_minus_shat_minus_6nu2": float(np.max(np.abs(6 * Wff / u2 - shat - 6 * nu**2) / (1 + 6 * nu**2))),
            "s_range": [float(np.min(scal)), float(np.max(scal))],
        },
    }
    Path(args.out).write_text(json.dumps(out, indent=1) + "\n")
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()

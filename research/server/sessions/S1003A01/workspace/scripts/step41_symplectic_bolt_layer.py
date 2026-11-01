"""Step 41: a smooth symplectic rotation of the certified perpendicular cell and
its singular almost-Kaehler normalization.

The metric is the certified diagonal cell with its (bolt, fibre) eigenframe
rotated by eps*chi(u), where chi is identically one near the bolt and zero near
the exact-CH collar.  The canonical closed self-dual form is integrated inward
from the CH Kahler form.  If p=int_E Omega, then p != 0 makes the form nowhere
zero, while p -> 0 resolves the bolt zero in a layer of normal radius O(|p|).

For ghat=v^2 g with v^2=|Omega|_g/sqrt(2), the script evaluates
    shat^2 dmu_ghat = (s_g - 6 Delta_g v/v)^2 dmu_g
and the scalar variance.  It also evaluates the original Einstein action J6.
The calculation is floating evidence for the matched asymptotic law; the
existence theorem uses only smoothness, strict certified margin, continuity,
and the exact sign formula p'(0)=-pi int chi' Phi > 0.

Normalization: Ric_CH=-6g, Omega=(1/2)d(phi_i sigma_i),
int_E Omega=pi*phi_bolt.  The orbit integral is already included in dmu.
"""
import argparse
import json
import sys
from pathlib import Path

import jax
import jax.numpy as jnp
import numpy as np
from scipy.integrate import solve_ivp

jax.config.update("jax_enable_x64", True)
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from perp_dual_cost import DualCell, load_record, seed_vector  # noqa: E402
from o11_perp_cell import ANG, PI, curvature_scalars, rot2  # noqa: E402
from o11_rotated_cell import euler_E  # noqa: E402

JGEN = jnp.array([[0.0, 0.0, 1.0], [0.0, 0.0, 0.0], [-1.0, 0.0, 0.0]])


def smooth_step(z):
    """C-infinity step, zero on z<=0 and one on z>=1."""
    zc = jnp.clip(z, 1.0e-8, 1.0 - 1.0e-8)
    a = jnp.exp(-1.0 / zc)
    b = jnp.exp(-1.0 / (1.0 - zc))
    mid = a / (a + b)
    return jnp.where(z <= 0.0, 0.0, jnp.where(z >= 1.0, 1.0, mid))


def build(record, cut_a, cut_b, action_nq):
    rec = load_record(record)
    deg = int(rec.get("deg", rec.get("degU", 6)))
    x0, X = float(rec["x0"]), float(rec["X"])
    cell = DualCell(x0, X, deg, deg, action_nq)
    cell.aligned = False
    cell.wpow = 2
    z = jnp.asarray(np.asarray(seed_vector(cell, rec), float))
    base = cell.prof_factory(z)
    ell = float(np.log(X / x0))

    def chi(u):
        return 1.0 - smooth_step((u - cut_a) / (cut_b - cut_a))

    chip = jax.grad(chi)

    def base_u(u):
        x = x0 * jnp.exp(ell * u)
        G, D = base(x)
        return x, G, D

    def profile_x(x, eps):
        u = jnp.log(x / x0) / ell
        G, D = base(x)
        R = rot2(eps * chi(u))
        return G, R @ D @ R.T

    def metric(y, eps):
        G, H = profile_x(y[0], eps)
        E = euler_E(y[1:])
        ang = E.T @ H @ E
        out = jnp.zeros((4, 4)).at[0, 0].set(1.0 / (4.0 * G))
        return out.at[1:, 1:].set(ang)

    def fields_one(x, eps):
        y = jnp.concatenate([jnp.array([x]), ANG])
        s, r0, _, _ = curvature_scalars(lambda yy: metric(yy, eps), y)
        G, H = profile_x(x, eps)
        dv_dx = PI**2 * jnp.sqrt(jnp.linalg.det(H) / G)
        return s, r0, dv_dx

    fields_many = jax.jit(jax.vmap(fields_one, in_axes=(0, None)))

    def original_action(eps):
        s, r0, dv = fields_many(cell.xx, eps)
        pd = jnp.sum(r0 * dv * cell.wx) / (8 * PI**2)
        sd = jnp.sum((s + 24.0)**2 * dv * cell.wx) / (32 * PI**2)
        sg = jnp.sum(s*s * dv * cell.wx)
        return pd, pd + sd, sd, sg

    def Mj(u, eps):
        x, G, D = base_u(u)
        diag = jnp.diag(D)
        det = jnp.prod(diag)
        lam = ell * x * diag / jnp.sqrt(G * det)
        return jnp.diag(lam) - eps * chip(u) * JGEN

    def Mnp(u, eps):
        return np.asarray(Mj(jnp.asarray(u), jnp.asarray(eps)), float)

    def integrate_form(eps, umin=1.0e-11):
        sol = solve_ivp(lambda uu, yy: Mnp(uu, eps) @ yy, (1.0, umin),
                        np.array([0.0, 0.0, X]), method="Radau", rtol=2e-10,
                        atol=2e-12, dense_output=True, max_step=2e-3)
        if not sol.success:
            raise RuntimeError(sol.message)
        psi0 = sol.sol(umin)
        period = float(np.pi * psi0[0])
        return sol, period

    def q_and_lap(u, psi, eps):
        """Q=|Omega|^2/2; f=sqrt(Q)=|Omega|/sqrt2; v=sqrt(f)."""
        x, G, D = base_u(u)
        det = jnp.linalg.det(D)
        Q = psi @ D @ psi / det

        def logv(uu, pp):
            _, _, DD = base_u(uu)
            QQ = pp @ DD @ pp / jnp.linalg.det(DD)
            return 0.25 * jnp.log(QQ)

        state_u = Mj(u, eps) @ psi
        lu = jax.jvp(logv, (u, psi), (jnp.array(1.0), state_u))[1]
        speed = 2.0 * jnp.sqrt(G) / (ell * x)  # du/dt

        def lt_fun(uu, pp):
            xx, GG, _ = base_u(uu)
            pp_u = Mj(uu, eps) @ pp
            llu = jax.jvp(logv, (uu, pp), (jnp.array(1.0), pp_u))[1]
            return 2.0 * jnp.sqrt(GG) / (ell * xx) * llu

        lt = speed * lu
        lt_u_total = jax.jvp(lt_fun, (u, psi), (jnp.array(1.0), state_u))[1]
        ltt = speed * lt_u_total

        def log_sqrtdet(uu):
            _, _, DD = base_u(uu)
            return 0.5 * jnp.log(jnp.linalg.det(DD))

        mean = speed * jax.grad(log_sqrtdet)(u)
        lap_over_v = ltt + lt*lt + mean*lt
        f = jnp.sqrt(Q)
        return Q, f, lt, lap_over_v

    qlap_many = jax.jit(jax.vmap(q_and_lap, in_axes=(0, 0, None)))
    return rec, cell, base, fields_many, original_action, integrate_form, qlap_many, ell, x0, X, chi


def trap(y, u):
    return float(np.trapz(y, u))


def run_one(eps, objs, nlog, nlin):
    (rec, cell, base, fields_many, original_action, integrate_form,
     qlap_many, ell, x0, X, chi) = objs
    sol, period = integrate_form(eps)
    # Geometric resolution in u resolves normal radii because u is quadratic in
    # bolt distance.  The last point begins a uniform outer grid.
    ug = np.geomspace(1.0e-10, 5.0e-2, nlog, endpoint=False)
    ul = np.linspace(5.0e-2, 1.0, nlin)
    u = np.unique(np.concatenate([ug, ul]))
    psi = sol.sol(u).T
    Q, f, lt, lap = [np.asarray(a) for a in qlap_many(jnp.asarray(u), jnp.asarray(psi), eps)]
    x = x0 * np.exp(ell * u)

    # Coordinate curvature is expensive; evaluate it once on the same resolved
    # radial grid.  Constant rotation near the bolt makes this exactly the base
    # scalar in the resolving layer.
    sb = []
    batch = 500
    for i in range(0, len(x), batch):
        ss, _, dvx = fields_many(jnp.asarray(x[i:i+batch]), eps)
        sb.append((np.asarray(ss), np.asarray(dvx)))
    s = np.concatenate([a[0] for a in sb])
    dvdu = np.concatenate([a[1] for a in sb]) * ell * x

    Shat = trap((s - 6.0*lap)**2 * dvdu, u)
    Sg = trap(s*s * dvdu, u)
    Vhat = trap(Q * dvdu, u)  # dmu_hat=f^2 dmu_g=Q dmu_g
    Ihat = trap(f * (s - 6.0*lap) * dvdu, u)
    variance = Shat - Ihat*Ihat/Vhat
    gradv = trap(f * lt*lt * dvdu, u)
    # Integration-by-parts expression for int shat dmu_hat.
    Iparts = trap((6.0*f*lt*lt + s*f) * dvdu, u)

    P, J, scalar_dev, Sg_gauss = [float(v) for v in original_action(eps)]
    # Bolt frame: Q^(1/2)=f and p=pi psi_1.  The exact leading value is
    # f(0)=|p|/(pi*b^2), b^2=x0.
    fbolt_exact = abs(period) / (np.pi*x0)
    return {
        "eps": eps,
        "exceptional_period_p": period,
        "p_over_eps": period/eps,
        "original_metric": {"P_over_8pi2": P, "J_over_8pi2": J,
                            "scalar_deviation_over_8pi2": scalar_dev,
                            "Sg_gauss": Sg_gauss, "Sg_resolved_trap": Sg},
        "AK_conformal_metric": {
            "f_bolt_exact": fbolt_exact,
            "f_first_sample": float(f[0]),
            "f_min_sample": float(np.min(f)),
            "Vhat": Vhat,
            "int_shat": Ihat,
            "int_shat_by_parts": Iparts,
            "int_shat_identity_relative_error": abs(Ihat-Iparts)/(1+abs(Ihat)),
            "int_shat_sq": Shat,
            "scalar_variance": variance,
            "int_grad_v_sq": gradv,
            "P_hat_minus_P_from_CGB": (Shat-Sg)/12.0,
        },
        "scaling": {"p2_times_Shat": period*period*Shat,
                    "p2_times_scalar_variance": period*period*variance,
                    "p2_times_Phat_minus_P": period*period*(Shat-Sg)/12.0},
        "grid": {"n": len(u), "u_min": float(u[0])},
    }


def local_model(objs):
    """Extract f_p(r)^2=a^2 p^2+kappa^2 r^2+... at p=0 and its
    predicted leading scalar-variance coefficient."""
    (rec, cell, base, fields_many, original_action, integrate_form,
     qlap_many, ell, x0, X, chi) = objs
    g1 = float(jax.grad(lambda xx: base(xx)[0])(jnp.asarray(x0)))
    sol0, _ = integrate_form(0.0)
    us = np.array([1.0e-6, 3.0e-7, 1.0e-7, 3.0e-8])
    ps = sol0.sol(us).T
    _, ff, _, _ = [np.asarray(v) for v in qlap_many(jnp.asarray(us), jnp.asarray(ps), 0.0)]
    xs = x0*np.exp(ell*us)
    rr = np.sqrt((xs-x0)/g1)
    kappas = ff/rr
    kappa = float(kappas[-1])
    a = 1.0/(np.pi*x0)  # f_p(0)=a |p|
    # dmu_g ~ 2*pi^2*b^2*r dr, b^2=x0. For v=sqrt(f),
    # integral_0^infty (Delta v/v)^2 r dr = 7*kappa^2/(32*a^2*p^2).
    pred = 36.0*(2*np.pi**2*x0)*7.0*kappa*kappa/(32.0*a*a)
    return {"G_x_bolt": g1, "period_coefficient_a": a,
            "u_samples": us.tolist(), "kappa_samples": kappas.tolist(),
            "kappa_limit_estimate": kappa,
            "model": "f_p(r)^2=a^2 p^2+kappa^2 r^2+O(p^2 r^2+r^4)",
            "predicted_limit_p2_times_scalar_variance": pred}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("record")
    ap.add_argument("--eps", nargs="+", type=float, default=[0.02, 0.01, 0.005, 0.0025])
    ap.add_argument("--cut-a", type=float, default=0.12)
    ap.add_argument("--cut-b", type=float, default=0.62)
    ap.add_argument("--action-nq", type=int, default=350)
    ap.add_argument("--nlog", type=int, default=3500)
    ap.add_argument("--nlin", type=int, default=1200)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    objs = build(a.record, a.cut_a, a.cut_b, a.action_nq)
    model = local_model(objs)
    results = []
    for e in a.eps:
        r = run_one(e, objs, a.nlog, a.nlin)
        results.append(r)
        print(json.dumps({"eps": e, "p": r["exceptional_period_p"],
                          "J": r["original_metric"]["J_over_8pi2"],
                          "Shat": r["AK_conformal_metric"]["int_shat_sq"],
                          "p2Shat": r["scaling"]["p2_times_Shat"]}, indent=1), flush=True)
    out = {"record": a.record,
           "normalization": "Ric_CH=-6g; Omega=(1/2)d(phi sigma); p=int_E Omega=pi phi_bolt",
           "cutoff": {"type": "C-infinity monotone", "one_for_u_le": a.cut_a, "zero_for_u_ge": a.cut_b},
           "bolt_local_model": model,
           "results": results,
           "scope": "floating matched-asymptotic evidence; strict subthreshold existence uses the certified eps=0 action and continuity"}
    Path(a.out).write_text(json.dumps(out, indent=1) + "\n")
    print(a.out)


if __name__ == "__main__":
    main()

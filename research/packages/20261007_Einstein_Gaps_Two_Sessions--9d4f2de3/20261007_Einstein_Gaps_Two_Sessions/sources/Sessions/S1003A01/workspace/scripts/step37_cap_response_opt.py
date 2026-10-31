"""Step 37b: compactly supported U(1)_- response optimization on the congruence-transported cell.

Base metric G0 = L bar_g L (step37_cap_congruence_transport.build).  Response:

    G = G0 + sum_{j,m,(al,be)} c_{j m al be} psi_j(r) A_m(z) sym(theta^al (x) theta^be),

where theta^al = sqrt(lamCH_al) v_al^T L is the G0-orthonormal coframe when the outer metric is
CH (and approximately so otherwise), psi_j are C^3 bumps 256 t^4(1-t)^4 on radial intervals
inside (a, Rcell), and A_m are U(1)_- invariant angular functions
  1, c2=(|z1|^2-|z2|^2)/r^2, c2^2, Re(z1 z2)/r^2, Im(z1 z2)/r^2.
All modes vanish near the bolt (r<a) and outside the last bump, so bolt, topology,
marking and the exact outer metric are untouched.  Frames v_al are equivariant under the
standard SU(2) on C^2, hence the response is U(1)_- invariant (diag(e^{ia},e^{-ia})).

Objective: D/(8 pi^2) = exact radial core (r<a) + stratified scrambled Sobol on shells.
Optimization uses one seed; validation uses fresh seeds.  Floating evidence only.
"""
import argparse, json, math, sys, time
from pathlib import Path
import numpy as np
import jax, jax.numpy as jnp
from scipy.optimize import minimize

jax.config.update("jax_enable_x64", True)
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import step36_cap_perp_transplant as s36  # noqa: E402
import step37_cap_congruence_transport as s37  # noqa: E402
from perp_dual_cost import load_record  # noqa: E402

SQ6 = math.sqrt(6.0)
PAIRS = [(i, j) for i in range(4) for j in range(i, 4)]


def make(rec, outer, a, b, taper, bumps, nang):
    cell, zz, prof, G0metric, Rcell = s37.build(rec, outer, a, b, 1.0, taper)
    X = float(rec["X"])

    def coframe(xi):
        rr = jnp.linalg.norm(xi)
        x = jnp.minimum(jnp.sinh(rr/SQ6)**2, X)
        G, h = prof(x)
        lam = jnp.array([(x+x*x)/G, h[0,0], h[1,1], h[2,2]])
        lch = jnp.array([1.0, x, x, x*(1+x)])
        xr = jnp.sinh(rr/SQ6)**2
        lchc = jnp.array([1.0, 6*xr/(rr*rr), 6*xr/(rr*rr), 6*xr*(1+xr)/(rr*rr)])
        z = jnp.array([xi[0]+1j*xi[1], xi[2]+1j*xi[3]])
        V = [s36.real2(v)/rr for v in s36.frames0(z)]
        if taper is None:
            am = 1.0
        else:
            am = 1.0 - s36.smoother7(jnp.clip((rr-taper[0])/(taper[1]-taper[0]), 0.0, 1.0))
        sq = jnp.exp(0.5*am*jnp.log(lam/lch))
        # theta^al = sqrt(lchc_al)*sq_al*v_al  (L is diagonal in the v frame)
        return [jnp.sqrt(lchc[k])*sq[k]*V[k] for k in range(4)], z, rr

    def angular(z, rr):
        r2 = rr*rr
        c2 = (jnp.abs(z[0])**2-jnp.abs(z[1])**2)/r2
        w = z[0]*z[1]/r2
        return jnp.array([1.0, c2, c2*c2, jnp.real(w), jnp.imag(w)])[:nang]

    nb = len(bumps); nmode = nb*nang*len(PAIRS)

    def metric(xi, coeff, aa, bb):
        g0 = G0metric(xi, None, aa, bb)
        th, z, rr = coframe(xi)
        ang = angular(z, rr)
        rad = jnp.array([s36.response_bump(jnp.clip((rr-l)/(r-l), 0.0, 1.0)) for (l, r) in bumps])
        C = coeff.reshape(nb, nang, len(PAIRS))
        amp = jnp.einsum("j,m,jmp->p", rad, ang, C)
        M = jnp.zeros((4,4))
        for p, (i, j) in enumerate(PAIRS):
            t = jnp.outer(th[i], th[j])
            M = M + amp[p]*(0.5*(t+t.T) if i != j else t)
        return g0 + M
    return cell, zz, prof, metric, Rcell, nmode


def nodes(edges, nlog2, seed):
    P, W = [], []
    for k, (r0, r1) in enumerate(zip(edges[:-1], edges[1:])):
        pts, vol = s36.qmc_annulus(r0, r1, nlog2, seed*1000+k)
        P.append(pts); W.append(np.full(len(pts), vol/len(pts)))
    return np.concatenate(P), np.concatenate(W)


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("record")
    ap.add_argument("--outer", choices=["cap", "ch"], default="cap")
    ap.add_argument("--a", type=float, default=0.45); ap.add_argument("--b", type=float, default=0.7)
    ap.add_argument("--taper", default="")
    ap.add_argument("--bumps", default="0.45:0.9,0.6:1.4,1.0:2.2,1.6:3.2,2.4:4.2,3.4:5.4,4.4:6.6")
    ap.add_argument("--nang", type=int, default=5)
    ap.add_argument("--nshell", type=int, default=20); ap.add_argument("--nlog2", type=int, default=10)
    ap.add_argument("--vlog2", type=int, default=11); ap.add_argument("--vseeds", default="11,12")
    ap.add_argument("--maxiter", type=int, default=60); ap.add_argument("--bound", type=float, default=0.3)
    ap.add_argument("--batch", type=int, default=256)
    ap.add_argument("--out")
    args = ap.parse_args(); rec = load_record(args.record)
    taper = tuple(map(float, args.taper.split(":"))) if args.taper else None
    bumps = [tuple(map(float, s.split(":"))) for s in args.bumps.split(",")]
    cell, zz, prof, metric, Rcell, nmode = make(rec, args.outer, args.a, args.b, taper, bumps, args.nang)
    Rint = min(Rcell, taper[1]) if taper else Rcell
    Rint = max(Rint, max(r for _, r in bumps))
    edges = [args.a + (Rint-args.a)*(k/args.nshell)**2 for k in range(args.nshell+1)]
    Ric = s36.ricci_of(metric); fields = s36.point_fields(metric, Ric)
    core, xa = s36.core_integrals(cell, zz, prof, args.a)
    corev = float(core[0]/(8*np.pi**2))
    K = 8*np.pi**2

    def batch_obj(c, pts, w):
        vv = jax.vmap(fields, in_axes=(0, None, None, None))(pts, c, args.a, args.b)
        return jnp.sum(vv[:, 0]*w)/K, jnp.min(vv[:, 5])
    vg = jax.jit(jax.value_and_grad(lambda c, p, w: batch_obj(c, p, w)[0]))
    fv = jax.jit(jax.vmap(fields, in_axes=(0, None, None, None)))

    def evaluate(c, pts, w):
        tot = 0.0; mn = 1e9; P = 0.0
        for i in range(0, len(pts), 1024):
            vv = np.asarray(fv(jnp.asarray(pts[i:i+1024]), jnp.asarray(c), args.a, args.b))
            tot += float((vv[:, 0]*w[i:i+1024]).sum()); P += float((vv[:, 1]*w[i:i+1024]).sum())
            mn = min(mn, float(vv[:, 5].min()))
        return corev+tot/K, float(core[1]/K)+P/K, mn

    P0, W0 = nodes(edges, args.nlog2, 0)
    t0 = time.time(); hist = []

    def fg(c):
        val = 0.0; grad = np.zeros(nmode)
        for i in range(0, len(P0), args.batch):
            v, g = vg(jnp.asarray(c), jnp.asarray(P0[i:i+args.batch]), jnp.asarray(W0[i:i+args.batch]))
            val += float(v); grad += np.asarray(g)
        val += corev
        if not np.isfinite(val):
            return 1e6, np.zeros(nmode)
        hist.append(val); print(json.dumps(dict(it=len(hist), D=val, t=time.time()-t0)), flush=True)
        return val, grad

    c0 = np.zeros(nmode)
    base_in = fg(c0)[0]
    res = minimize(fg, c0, jac=True, method="L-BFGS-B", bounds=[(-args.bound, args.bound)]*nmode,
                   options=dict(maxiter=args.maxiter, ftol=1e-12, gtol=1e-7, maxls=25))
    copt = np.asarray(res.x)
    val = []
    for s in [int(x) for x in args.vseeds.split(",")]:
        Pv, Wv = nodes(edges, args.vlog2, s)
        b0 = evaluate(c0, Pv, Wv); b1 = evaluate(copt, Pv, Wv)
        val.append(dict(seed=s, base_D=b0[0], base_P=b0[1], opt_D=b1[0], opt_P=b1[1], opt_min_eig=b1[2], base_min_eig=b0[2]))
        print(json.dumps(val[-1]), flush=True)
    out = dict(record=args.record, outer=args.outer, a=args.a, b=args.b, taper=args.taper, bumps=bumps,
               nang=args.nang, nmode=nmode, edges=edges, core_D=corev, insample_base=base_in,
               insample_opt=float(res.fun), success=bool(res.success), message=str(res.message), nit=int(res.nit),
               max_abs_coeff=float(np.abs(copt).max()), n_at_bound=int((np.abs(copt) > args.bound-1e-9).sum()),
               coeff=copt.tolist(), validation=val, history=hist, seconds=time.time()-t0,
               status="floating QMC optimization; validation on fresh scrambled Sobol seeds")
    if args.out: Path(args.out).write_text(json.dumps(out, indent=1)+"\n")
    print(json.dumps({k: out[k] for k in ["outer", "insample_base", "insample_opt", "nit", "max_abs_coeff", "n_at_bound", "seconds"]}))


if __name__ == "__main__":
    main()

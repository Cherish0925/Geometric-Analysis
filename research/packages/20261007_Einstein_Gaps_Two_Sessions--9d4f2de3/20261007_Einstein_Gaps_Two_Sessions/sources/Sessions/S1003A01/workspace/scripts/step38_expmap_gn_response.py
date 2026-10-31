"""Step 38: curvature-residual-conditioned response of the certified cell in a Calabi exp chart.

This is a floating construction experiment.  It repairs two weaknesses of the Step-37
response test:

1. the base cap is pulled back by its own exponential map (step37_cap_expmap_transport);
2. coefficients are whitened by the discrete Gauss--Newton Gram form of the complete
   weighted Cholesky-frame residual map, rather than by metric amplitude or volume alone.

The base is the full certified x0=.03, X=128 cell transported by congruence. Responses are
supported outside a prescribed bolt neighbourhood. The nonlinear family is

    g(c) = B(c)^T g0 B(c),  B=I + (1/2) g0^{-1} h(c),

where h is a sum of smooth radial/angular symmetric-coframe modes. At c=0 this has
variation h. Positivity requires B to remain nonsingular and is sampled, not proven over
the continuum. The fit residual is the Cholesky-frame tensor Ric(g)+g, weighted so its
Euclidean square is the quadrature approximation to D/(8 pi^2). An SVD removes weak or
redundant directions and whitens the derivative of this full moving-frame, moving-volume
residual. At a non-Einstein base it is not the frozen-weight intrinsic norm of D(Ric+g)[h].

Validation uses the exact CH cell and the unmodified cap base as pointwise controls on
identical Sobol nodes. The code integrates only the response band: opt-minus-base is the
complete response change because the response vanishes outside it, while cap-minus-CH is
only a partial-band difference and is not a complete cell cost. Independent scrambled
replicates estimate empirical uncertainty in these smaller differences.
No output is an interval enclosure or a lower bound.
"""
import argparse, json, math, sys, time
from pathlib import Path
import numpy as np
import jax, jax.numpy as jnp
from scipy.optimize import least_squares

jax.config.update("jax_enable_x64", True)
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import step36_cap_perp_transplant as s36  # noqa: E402
import step37_cap_congruence_transport as s37  # noqa: E402
import step37_cap_expmap_transport as s37e  # noqa: E402
from perp_dual_cost import load_record  # noqa: E402

SQ6 = math.sqrt(6.0)
K8 = 8.0*math.pi**2
PAIRS = [(i, j) for i in range(4) for j in range(i, 4)]
CERT_D = 0.5*(0.995670030344086 + 0.995670030355131)


def parse_intervals(text):
    return [tuple(map(float, s.split(":"))) for s in text.split(",") if s]


def make_family(rec, environment, a, b, nstep, supports, nang):
    # build_exp supplies the correctly marked cap base and the same cell profile/coframe data.
    cell, zz, prof, gcap, Rcell, phi, gexp, gch = s37e.build_exp(rec, a, b, nstep)
    _, _, _, gstar, _ = s37.build(rec, "ch", a, b, 1.0, None)
    gbase = gcap if environment == "cap" else gstar
    X = float(rec["X"])

    def mode_data(xi):
        rr = jnp.linalg.norm(xi)
        x = jnp.minimum(jnp.sinh(rr/SQ6)**2, X)
        G, hprof = prof(x)
        lam = jnp.array([(x+x*x)/G, hprof[0,0], hprof[1,1], hprof[2,2]])
        lch = jnp.array([1.0, x, x, x*(1+x)])
        xr = jnp.sinh(rr/SQ6)**2
        lchc = jnp.array([1.0, 6*xr/(rr*rr), 6*xr/(rr*rr), 6*xr*(1+xr)/(rr*rr)])
        sq = jnp.sqrt(lam/lch)
        z = jnp.array([xi[0]+1j*xi[1], xi[2]+1j*xi[3]])
        V = [s36.real2(v)/rr for v in s36.frames0(z)]
        # This is exactly orthonormal for the transported CH cell and close to so in the
        # small cap switching band.  The GN whitening, not this raw normalization, sets scale.
        th = [jnp.sqrt(lchc[k])*sq[k]*V[k] for k in range(4)]
        c2 = (jnp.abs(z[0])**2-jnp.abs(z[1])**2)/(rr*rr)
        w = z[0]*z[1]/(rr*rr)
        ang_all = jnp.array([1.0, c2, jnp.real(w), jnp.imag(w), c2*c2])
        ang = ang_all[:nang]
        rad = jnp.array([s36.response_bump(jnp.clip((rr-l)/(r-l), 0.0, 1.0))
                         for l, r in supports])
        return th, ang, rad

    nm = len(supports)*nang*len(PAIRS)

    def metric(xi, coeff, aa, bb):
        g0 = gbase(xi, None, aa, bb)
        th, ang, rad = mode_data(xi)
        C = coeff.reshape(len(supports), nang, len(PAIRS))
        amp = jnp.einsum("j,m,jmp->p", rad, ang, C)
        h = jnp.zeros((4,4))
        for p, (i, j) in enumerate(PAIRS):
            q = jnp.outer(th[i], th[j])
            h = h + amp[p]*(0.5*(q+q.T) if i != j else q)
        # Congruence response is positive whenever B is nonsingular; it agrees with g0+h
        # to first order, so its GN form is D(Ric+g)[h].
        B = jnp.eye(4) + 0.5*jnp.linalg.solve(g0, h)
        return B.T@g0@B
    return cell, zz, prof, metric, gstar, Rcell, nm


def fit_nodes(edges, nlog2, seed):
    pts, weights = [], []
    for k, (r0, r1) in enumerate(zip(edges[:-1], edges[1:])):
        p, vol = s36.qmc_annulus(r0, r1, nlog2, seed*1000+k)
        pts.append(p); weights.append(np.full(len(p), vol/len(p)))
    return np.concatenate(pts), np.concatenate(weights)


def tensor_residual(metric, Ric):
    # Ten independent orthonormal-frame entries; sqrt(2) on off diagonals gives Frobenius norm.
    def one(x, coeff, weight, aa, bb):
        g = metric(x, coeff, aa, bb); ric = Ric(x, coeff, aa, bb); E = ric+g
        L = jnp.linalg.cholesky(g)
        A = jnp.linalg.solve(L, E)
        A = jnp.linalg.solve(L, A.T).T  # L^{-1} E L^{-T}
        vv = []
        for i, j in PAIRS:
            vv.append(A[i,j] if i == j else jnp.sqrt(2.0)*A[i,j])
        dv = jnp.sqrt(jnp.linalg.det(g))
        return jnp.asarray(vv)*jnp.sqrt(weight*dv/K8)
    return one


def cv_validate(metric, gstar, coeff, a, b, Rval, nshell, nlog2, seeds, batch):
    Ric = s36.ricci_of(metric); F = s36.point_fields(metric, Ric)
    Ric0 = s36.ricci_of(gstar); F0 = s36.point_fields(gstar, Ric0)
    vf = jax.jit(jax.vmap(F, in_axes=(0, None, None, None)))
    v0 = jax.jit(jax.vmap(F0, in_axes=(0, None, None, None)))
    edges = [a+(Rval-a)*(k/nshell)**2 for k in range(nshell+1)]
    zero = np.zeros_like(coeff)
    reps = []
    for seed in seeds:
        shells = []; total = 0.0; improvement = 0.0; var_sum = 0.0; imp_var_sum = 0.0; min_eig = 1e300
        for k, (r0, r1) in enumerate(zip(edges[:-1], edges[1:])):
            pts, vol = s36.qmc_annulus(r0, r1, nlog2, seed*1000+k)
            A, C, B = [], [], []
            for i in range(0, len(pts), batch):
                q = jnp.asarray(pts[i:i+batch])
                A.append(np.asarray(vf(q, jnp.asarray(coeff), a, b)))
                C.append(np.asarray(vf(q, jnp.asarray(zero), a, b)))
                B.append(np.asarray(v0(q, jnp.zeros(1), a, b)))
            A = np.concatenate(A); C = np.concatenate(C); B = np.concatenate(B)
            diff = (A[:,0]-B[:,0])*vol/K8
            imp = (A[:,0]-C[:,0])*vol/K8
            d = float(diff.mean()); se = float(diff.std(ddof=1)/math.sqrt(len(diff)))
            di = float(imp.mean()); sei = float(imp.std(ddof=1)/math.sqrt(len(imp)))
            total += d; improvement += di; var_sum += se*se; imp_var_sum += sei*sei
            min_eig = min(min_eig, float(A[:,5].min()))
            shells.append(dict(r0=r0, r1=r1, cap_minus_ch=d, cap_minus_ch_se=se,
                               response_improvement=di, response_improvement_se=sei,
                               opt=float(A[:,0].mean()*vol/K8), base=float(C[:,0].mean()*vol/K8),
                               ch=float(B[:,0].mean()*vol/K8)))
        reps.append(dict(seed=seed, partial_cap_minus_ch=total, partial_response_improvement=improvement,
                         partial_cap_minus_ch_se=math.sqrt(var_sum),
                         partial_response_improvement_se=math.sqrt(imp_var_sum), min_eig=min_eig, shells=shells))
        print(json.dumps({k: reps[-1][k] for k in ["seed","partial_cap_minus_ch","partial_response_improvement","partial_cap_minus_ch_se","partial_response_improvement_se","min_eig"]}), flush=True)
    vals = np.array([r["partial_cap_minus_ch"] for r in reps])
    imps = np.array([r["partial_response_improvement"] for r in reps])
    return dict(cert_reference=CERT_D, scope=[a,Rval], reps=reps, mean_partial_cap_minus_ch=float(vals.mean()),
                cap_minus_ch_replicate_se=float(vals.std(ddof=1)/math.sqrt(len(vals))) if len(vals)>1 else None,
                mean_response_improvement=float(imps.mean()),
                response_replicate_se=float(imps.std(ddof=1)/math.sqrt(len(imps))) if len(imps)>1 else None,
                edges=edges)


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("record")
    ap.add_argument("--environment", choices=["cap","ch"], default="cap")
    ap.add_argument("--a", type=float, default=.45); ap.add_argument("--b", type=float, default=.7)
    ap.add_argument("--nstep", type=int, default=64)
    ap.add_argument("--supports", default="0.45:0.82,0.58:1.08,0.82:1.5")
    ap.add_argument("--nang", type=int, default=2, choices=range(1,6))
    ap.add_argument("--fit-edges", default="0.45,0.52,0.62,0.78,1.02,1.5")
    ap.add_argument("--fit-nlog2", type=int, default=5); ap.add_argument("--fit-seed", type=int, default=0)
    ap.add_argument("--svd-rtol", type=float, default=1e-5); ap.add_argument("--ybound", type=float, default=.35)
    ap.add_argument("--max-nfev", type=int, default=20)
    ap.add_argument("--solver", choices=["gn1","trf"], default="gn1",
                    help="gn1: one whitened Gauss--Newton step with nonlinear line search; trf: iterative least squares")
    ap.add_argument("--validate-nlog2", type=int, default=7); ap.add_argument("--validate-nshell", type=int, default=16)
    ap.add_argument("--validate-batch", type=int, default=256)
    ap.add_argument("--validate-seeds", default="11,12,13")
    ap.add_argument("--no-opt", action="store_true"); ap.add_argument("--no-validate", action="store_true")
    ap.add_argument("--out", required=True)
    args = ap.parse_args(); t0 = time.time(); rec = load_record(args.record)
    supports = parse_intervals(args.supports); edges = list(map(float, args.fit_edges.split(",")))
    cell, zz, prof, metric, gstar, Rcell, nm = make_family(rec, args.environment, args.a, args.b,
                                                           args.nstep, supports, args.nang)
    Ric = s36.ricci_of(metric); Rone = tensor_residual(metric, Ric)
    pts, weights = fit_nodes(edges, args.fit_nlog2, args.fit_seed)
    P = jnp.asarray(pts); W = jnp.asarray(weights)
    rv = jax.jit(lambda c: jax.vmap(Rone, in_axes=(0,None,0,None,None))(P,c,W,args.a,args.b).reshape(-1))
    jv = jax.jit(jax.jacfwd(rv))
    c0 = jnp.zeros(nm)
    r0 = np.asarray(rv(c0)); J0 = np.asarray(jv(c0))
    U, s, Vt = np.linalg.svd(J0, full_matrices=False)
    keep = s > s[0]*args.svd_rtol
    T = (Vt[keep].T/s[keep])
    Tj = jnp.asarray(T)
    def ry(y): return rv(Tj@y)
    rjy = jax.jit(ry); jjy = jax.jit(jax.jacfwd(ry))
    y0 = np.zeros(int(keep.sum())); base_fit = float(r0@r0)
    pred = -U[:,keep].T@r0
    print(json.dumps(dict(nmode=nm, rank=int(keep.sum()), smax=float(s[0]),
                               smin_kept=float(s[keep][-1]), base_fit=base_fit,
                               linear_pred_norm=float(np.linalg.norm(pred)))), flush=True)
    if args.no_opt:
        yopt = np.zeros_like(y0); solmeta = dict(success=True, message="no-opt", nfev=0)
    elif args.solver == "gn1":
        # Since J0 T=U_keep, -U_keep^T r0 is the exact least-squares step for the
        # linearized curvature residual in whitened coordinates.  Test it nonlinearly
        # along a bounded line; no repeated expensive residual Jacobian is needed.
        direction = np.clip(pred, -args.ybound, args.ybound)
        trials = []
        for alpha in [0.0, .125, .25, .5, .75, 1.0]:
            yy = alpha*direction; rr = np.asarray(rjy(jnp.asarray(yy))); val = float(rr@rr)
            trials.append(dict(alpha=alpha, support_D=val, ymax=float(np.max(np.abs(yy)))))
            print(json.dumps(trials[-1]), flush=True)
        best = min(trials, key=lambda z:z["support_D"]); yopt = best["alpha"]*direction
        solmeta = dict(success=True, message="one whitened GN direction plus nonlinear line search",
                       nfev=len(trials), support_cost=best["support_D"], trials=trials)
    else:
        calls = [0]
        def fun(y):
            calls[0] += 1; rr = np.asarray(rjy(jnp.asarray(y)))
            print(json.dumps(dict(call=calls[0], support_D=float(rr@rr), ymax=float(np.max(np.abs(y))))), flush=True)
            return rr
        def jac(y): return np.asarray(jjy(jnp.asarray(y)))
        sol = least_squares(fun, y0, jac=jac, method="trf", x_scale=1.0,
                            bounds=(-args.ybound,args.ybound), ftol=1e-11, xtol=1e-11,
                            gtol=1e-9, max_nfev=args.max_nfev, verbose=0)
        yopt = np.asarray(sol.x); solmeta = dict(success=bool(sol.success), message=str(sol.message),
                                                 nfev=int(sol.nfev), njev=int(sol.njev or 0),
                                                 support_cost=float(sol.fun@sol.fun), optimality=float(sol.optimality))
    copt = T@yopt
    out = dict(record=args.record, environment=args.environment, a=args.a, b=args.b, nstep=args.nstep,
               supports=supports, nang=args.nang, nmode=nm, fit_edges=edges, fit_nlog2=args.fit_nlog2,
               fit_seed=args.fit_seed, base_fit_support=base_fit, singular_values=s.tolist(),
               svd_rtol=args.svd_rtol, retained_rank=int(keep.sum()), transform=T.tolist(),
               y=yopt.tolist(), coeff=copt.tolist(), max_abs_y=float(np.max(np.abs(yopt))) if len(yopt) else 0.,
               max_abs_coeff=float(np.max(np.abs(copt))) if len(copt) else 0., solver=solmeta)
    if not args.no_validate:
        seeds = [int(x) for x in args.validate_seeds.split(",")]
        out["control_variate"] = cv_validate(metric, gstar, copt, args.a, args.b,
                                                max(r for _,r in supports),
                                                args.validate_nshell, args.validate_nlog2, seeds,
                                                args.validate_batch)
    out["seconds"] = time.time()-t0
    Path(args.out).write_text(json.dumps(out, indent=1)+"\n")
    print(json.dumps({k: out[k] for k in ["environment","retained_rank","max_abs_y","max_abs_coeff","solver","seconds"]}), flush=True)


if __name__ == "__main__":
    main()

"""Step 37d: congruence transport in the cap's own geodesic normal coordinates at p in D'.

The step-36/37 chart (X,Y) divisor-flat, (Z,W) normal-exponential is Fermi-type about D'.
The transported CH cell is defined in CH *exponential* coordinates at its center, so in that
chart the far tail is compared with a non-isometric marking.  Here the cap is pulled back by
its exponential map at p:

    phi(xi) = gamma_xi(1),    gexp(xi) = Dphi(xi)^T g_C(phi(xi)) Dphi(xi),

computed by RK4 integration of the geodesic equation with JAX (all derivatives exact for the
discretized flow).  Then G = L bar_g L with bar_g=(1-H)g_CH + H gexp, exactly as in step37.

Checks produced: Gauss lemma gexp(xi) xi = xi, det Dphi>0, and a CH self-test in which the
same ODE exponential map applied to the Bergman metric reproduces the analytic CH
exponential-chart metric used for the cell.
"""
import argparse, json, math, sys, time
from pathlib import Path
import numpy as np
import jax, jax.numpy as jnp

jax.config.update("jax_enable_x64", True)
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import step36_cap_perp_transplant as s36  # noqa: E402
import step37_cap_congruence_transport as s37  # noqa: E402
from perp_dual_cost import load_record  # noqa: E402

SQ6 = math.sqrt(6.0)
U_SER = [1, 1/2, 0, 1/120, -1/336, 1/800, -31/55440, 601/2293200]
FF_SER = [1, 0, 1/10, -1/21, 11/400, -73/4620, 41989/4586400, -493/92400]
CC_SER = [0, -1/10, 1/21, -11/400, 73/4620, -41989/4586400, 493/92400]
SW = 0.05


def poly(c, s):
    out = 0.0*s
    for k in reversed(c):
        out = out*s + k
    return out


def cap_metric_safe(y):
    """Exact Calabi cap (Ric=-g) in (X,Y,Z,W); analytic at the divisor Z=W=0."""
    X, Y, Z, W = y
    ss = Z*Z + W*W
    big = ss > SW
    sb = jnp.where(big, ss, 1.0)
    ub = jnp.cosh(jnp.sqrt(1.5*sb))**(2.0/3.0)
    qb = (2.0/3.0)*(ub*ub-1.0/ub)
    u = jnp.where(big, ub, poly(U_SER, ss))
    ff = jnp.where(big, qb/sb, poly(FF_SER, ss))
    cc = jnp.where(big, (1.0-qb/sb)/sb, poly(CC_SER, ss))
    q = ff*ss
    vh = jnp.array([-0.5*Y, 0.5*X]); vn = jnp.array([-W, Z]); vr = jnp.array([Z, W])
    hh = u*jnp.eye(2) + q*jnp.outer(vh, vh)
    nn = ff*jnp.eye(2) + cc*jnp.outer(vr, vr)
    hn = ff*jnp.outer(vh, vn)
    top = jnp.concatenate([hh, hn], axis=1); bot = jnp.concatenate([hn.T, nn], axis=1)
    return jnp.concatenate([top, bot], axis=0)


def bergman6(y):
    """CH with Ric=-g in ball coordinates scaled so that g(0)=Id: y=sqrt6*q."""
    return s36.bergman(y/SQ6)


def make_exp(gfun, nstep, n0=0.0):
    """Exponential chart at y0=(0,0,n0,0) with the orthonormal frame E=diag(u^-1/2,u^-1/2,1,n0/sqrt q)
    (for gfun=cap; for n0=0 or other metrics E=Id).  The frame preserves the complex orientation
    X+iY, Z+iW, so CH's Kaehler form is matched with the cap's."""
    y0 = jnp.array([0.0, 0.0, n0, 0.0])
    if n0 > 0:
        g0 = np.asarray(gfun(y0))
        E = jnp.asarray(np.diag(1.0/np.sqrt(np.diag(g0))))
        assert np.abs(g0-np.diag(np.diag(g0))).max() < 1e-12
    else:
        E = jnp.eye(4)
    def christ(y):
        g = gfun(y); gi = jnp.linalg.inv(g); dg = jax.jacfwd(gfun)(y)
        gl = 0.5*(jnp.einsum("jli->lij", dg)+jnp.einsum("ilj->lij", dg)-jnp.einsum("ijl->lij", dg))
        return jnp.einsum("kl,lij->kij", gi, gl)

    def rhs(st):
        y, v = st[:4], st[4:]
        G = christ(y)
        return jnp.concatenate([v, -jnp.einsum("kij,i,j->k", G, v, v)])

    def phi(xi):
        h = 1.0/nstep
        def body(st, _):
            k1 = rhs(st); k2 = rhs(st+0.5*h*k1); k3 = rhs(st+0.5*h*k2); k4 = rhs(st+h*k3)
            return st + h*(k1+2*k2+2*k3+k4)/6.0, None
        st, _ = jax.lax.scan(body, jnp.concatenate([y0, E@xi]), None, length=nstep)
        return st[:4]

    def gexp(xi):
        J = jax.jacfwd(phi)(xi)
        return J.T @ gfun(phi(xi)) @ J
    return phi, gexp


def build_exp(rec, a, b, nstep, taper=None, n0=0.0):
    cell, zz, prof, G0, Rcell = s37.build(rec, "ch", a, b, 1.0, taper)
    phi, gexp = make_exp(cap_metric_safe, nstep, n0)
    deg = int(rec["deg"]); X = float(rec["X"])

    # reuse the L used by build(): recompute here
    def Lmat(xi):
        rr = jnp.linalg.norm(xi); x = jnp.minimum(jnp.sinh(rr/SQ6)**2, X)
        G, h = prof(x)
        lam = jnp.array([(x+x*x)/G, h[0,0], h[1,1], h[2,2]]); lch = jnp.array([1.0, x, x, x*(1+x)])
        if taper is None:
            am = 1.0
        else:
            am = 1.0-s36.smoother7(jnp.clip((rr-taper[0])/(taper[1]-taper[0]), 0.0, 1.0))
        sq = jnp.exp(0.5*am*jnp.log(lam/lch))
        z = jnp.array([xi[0]+1j*xi[1], xi[2]+1j*xi[3]])
        V = [s36.real2(v)/rr for v in s36.frames0(z)]
        return sum((sq[k]*jnp.outer(V[k], V[k]) for k in range(4)), jnp.zeros((4,4)))

    def gch(xi):
        rr = jnp.linalg.norm(xi); x = jnp.sinh(rr/SQ6)**2
        lam = jnp.array([1.0, 6*x/(rr*rr), 6*x/(rr*rr), 6*x*(1+x)/(rr*rr)])
        z = jnp.array([xi[0]+1j*xi[1], xi[2]+1j*xi[3]])
        V = [s36.real2(v)/rr for v in s36.frames0(z)]
        return sum((lam[k]*jnp.outer(V[k], V[k]) for k in range(4)), jnp.zeros((4,4)))

    def metric(xi, coeff, aa, bb):
        rr = jnp.linalg.norm(xi)
        H = s36.smoother7(jnp.clip((rr-aa)/(bb-aa), 0.0, 1.0))
        gbar = (1.0-H)*gch(xi) + H*gexp(xi)
        L = Lmat(xi)
        return L@gbar@L
    return cell, zz, prof, metric, Rcell, phi, gexp, gch


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("record")
    ap.add_argument("--a", type=float, default=0.45); ap.add_argument("--b", type=float, default=0.7)
    ap.add_argument("--taper", default="")
    ap.add_argument("--nstep", type=int, default=64)
    ap.add_argument("--nshell", type=int, default=16); ap.add_argument("--nlog2", type=int, default=8)
    ap.add_argument("--seed", type=int, default=0); ap.add_argument("--Rmax", type=float, default=0.0)
    ap.add_argument("--checks", action="store_true"); ap.add_argument("--out")
    ap.add_argument("--n0", type=float, default=0.0, help="normal distance of the cell centre from D'")
    args = ap.parse_args(); rec = load_record(args.record)
    taper = tuple(map(float, args.taper.split(":"))) if args.taper else None
    cell, zz, prof, metric, Rcell, phi, gexp, gch = build_exp(rec, args.a, args.b, args.nstep, taper, args.n0)
    out = dict(record=args.record, a=args.a, b=args.b, taper=args.taper, nstep=args.nstep, n0=args.n0)
    rng = np.random.default_rng(3)
    if args.checks:
        chk = []
        _, gexpCH = make_exp(bergman6, args.nstep)
        for rr in [0.5, 1.5, 3.0, 5.0, 7.6]:
            v = rng.normal(size=4); v = rr*v/np.linalg.norm(v); xi = jnp.asarray(v)
            ge = np.asarray(jax.jit(gexp)(xi)); gc = np.asarray(gch(xi)); gec = np.asarray(jax.jit(gexpCH)(xi))
            J = np.asarray(jax.jit(jax.jacfwd(phi))(xi))
            chk.append(dict(r=rr, gauss_lemma_cap=float(np.abs(ge@v - v).max()),
                            det_Dphi=float(np.linalg.det(J)),
                            CH_ode_vs_analytic=float(np.abs(gec-gc).max()/np.abs(gc).max()),
                            cap_vs_CH_relative=float(np.abs(ge-gc).max()/np.abs(gc).max()),
                            min_eig_cap_exp=float(np.linalg.eigvalsh(ge).min())))
            print(json.dumps(chk[-1]), flush=True)
        out["checks"] = chk
    Ric = s36.ricci_of(metric); fields = s36.point_fields(metric, Ric)
    vf = jax.jit(jax.vmap(fields, in_axes=(0, None, None, None)))
    core, xa = s36.core_integrals(cell, zz, prof, args.a)
    R = Rcell if not taper else min(Rcell, taper[1])
    if args.Rmax > 0: R = min(R, args.Rmax)
    edges = [args.a + (R-args.a)*(k/args.nshell)**2 for k in range(args.nshell+1)]
    K = 8*np.pi**2; tot = np.zeros(5); shells = []; t0 = time.time()
    for k, (r0, r1) in enumerate(zip(edges[:-1], edges[1:])):
        pts, vol = s36.qmc_annulus(r0, r1, args.nlog2, args.seed*1000+k)
        vals = np.concatenate([np.asarray(vf(jnp.asarray(pts[i:i+128]), jnp.zeros(3), args.a, args.b)) for i in range(0, len(pts), 128)])
        good = np.isfinite(vals).all(1)
        m = vals[good, :5].mean(0)*vol; se = vals[good, 0].std()*vol/math.sqrt(max(good.sum(), 1))
        tot += m
        z1 = pts[:, 0]**2+pts[:, 1]**2; z2 = pts[:, 2]**2+pts[:, 3]**2; c2 = (z1-z2)/(z1+z2)
        dens = vals[:, 0]*vol/len(pts)/K
        bins = np.clip(((c2+1)/2*4).astype(int), 0, 3)
        sh = dict(r0=r0, r1=r1, D=float(m[0]/K), se=float(se/K), P=float(m[1]/K), nbad=int((~good).sum()),
                  min_eig=float(vals[good, 5].min()) if good.any() else None,
                  by_c2_quarter=[float(dens[good & (bins == j)].sum()) for j in range(4)], t=time.time()-t0)
        shells.append(sh); print(json.dumps(sh), flush=True)
    out.update(core_D=float(core[0]/K), shells=shells, D_over_8pi2=float((core[0]+tot[0])/K),
               P_over_8pi2=float((core[1]+tot[1])/K), Rint=R, seconds=time.time()-t0,
               status="floating; cap in its own geodesic normal coordinates at p in D'")
    if args.out: Path(args.out).write_text(json.dumps(out, indent=1)+"\n")
    print(json.dumps({k: out[k] for k in ["core_D", "D_over_8pi2", "P_over_8pi2", "seconds"]}))


if __name__ == "__main__":
    main()

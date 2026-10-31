"""Perpendicular O11 cell: optimize and compare trace-free cost P and Einstein cost J.

The metric ansatz and curvature evaluator are imported read-only from the peer Session
S1003A02 (`o11_perp_cell.py`).  Its normalization is Ric_CH=-6 g, s_CH=-24:

  P = int |Ric^o|^2,
  J = int |Ric+6g|^2 = P + (1/4) int (s+24)^2.

P is scale invariant. J_6 with the numeral 6 held fixed is not; under simultaneous
rescaling of metric and Einstein constant, J_6(g)=J_1(6g). Thus after rescaling 6g
to Ric=-g, J is exactly the fixed-cell cost used in I54/I55. Values printed below
are divided by 8*pi^2, so the topological threshold is 1.

For fixed-slot perpendicular cells the old axes are (bolt, transverse, CH fibre).
The cyclic bolt-adapted axes used for the slice transgression are
(new a,new b,new c)=(old b,old c,old a); hence c collapses at the bolt.  The script
reports T/(8*pi^2)=Y^2+Pi on an optional profile grid.

Usage examples:
  python perp_dual_cost.py eval PEER_JSON
  python perp_dual_cost.py opt --x0 0.03 --target J --seed PEER_JSON --deg 6 --nq 400
  python perp_dual_cost.py opt --x0 0.1 --target P --deg 8 --nq 500 --out result.json
"""
from pathlib import Path
import argparse, json, math, sys, time

import numpy as np
import jax
import jax.numpy as jnp
jax.config.update('jax_enable_x64', True)
from scipy.optimize import minimize

ROOT = Path(__file__).resolve().parents[4]
PEER_SCRIPTS = ROOT / 'Sessions' / 'S1003A02' / 'workspace' / 'scripts'
sys.path.insert(0, str(PEER_SCRIPTS))
from o11_perp_cell import PerpCell, PI, ANG, metric_from, curvature_scalars, cheb, rot2  # noqa: E402


def load_record(path):
    text = Path(path).read_text().strip()
    if not text:
        raise ValueError(f'empty seed file: {path}')
    rec = json.loads(text.splitlines()[-1])
    return rec


class DualCell(PerpCell):
    def prof_factory(self, z):
        """Stable exact parametrization.

        The inherited formula enforces the bolt condition by adding a shift to
        cG[0].  Algebraically the raw cG[0] cancels identically.  With LM records
        it grew to 1e9, and the floating add/subtract left a spurious geometric
        coefficient.  Compute the effective cG[0] directly from cF and cG[1:].
        This is exactly equivalent over the reals and agrees with the rigorous
        exact-dyadic interpretation.
        """
        x0, ell = self.x0, self.ell
        dU, dw = self.degU, self.degw
        cF=z[:dU]; rawG=z[dU:2*dU]; cw=z[2*dU:2*dU+dw]
        tm=cheb(dU,jnp.array(-1.0))
        eff0=-(jnp.sum(cF*tm)+jnp.sum(rawG[1:]*tm[1:]))
        cG=rawG.at[0].set(eff0)
        def sm(u): return 10*u**3-15*u**4+6*u**5
        def prof(x):
            u=jnp.log(x/x0)/ell; Bu=cheb(max(dU,dw),2*u-1)
            qF=(1-u)**3*jnp.sum(cF*Bu[:dU]); qG=(1-u)**3*jnp.sum(cG*Bu[:dU]); su=sm(u)
            G=(x-x0+(x**2+x0)*su)*jnp.exp(qG)
            wr=u**self.wpow*(1-u)**3*jnp.sum(cw*Bu[:dw])
            if self.aligned:
                F=(x-x0)*jnp.exp(qF)+(x0+x**2)*su
                h=jnp.diag(jnp.array([x,x*jnp.exp(wr),F]))
            else:
                F=(x-x0)*jnp.exp(qF)+x0*su; w=jnp.log1p(x)*su+wr
                h=jnp.diag(jnp.array([F,x,x*jnp.exp(w)]))
                if self.degr>=0 and self.beta0!=0.0:
                    v=jnp.clip((u-.05)/.95,0.0,1.0); st=sm(v)
                    cr=z[2*dU+dw:2*dU+dw+self.degr]
                    extra=v**3*(1-v)**3*jnp.sum(cr*cheb(self.degr,2*v-1)) if self.degr>0 else 0.0*v
                    beta=self.beta0*(1-st-extra); Rm=rot2(beta); h=Rm@h@Rm.T
            return G,h
        return prof

    def costs(self, z):
        s, ric0, wa, wb, dv = self.fields(z)
        W = self.wx * dv
        p = jnp.sum(ric0 * W) / (8 * PI**2)
        q = jnp.sum((s + 24.0)**2 * W) / (32 * PI**2)
        return p, p + q, q

    def target(self, z, name):
        p, j, q = self.costs(z)
        return p if name == 'P' else j

    def full_report(self, z):
        p, j, q = self.costs(z)
        s, ric0, wa, wb, dv = self.fields(z)
        W = self.wx * dv
        vol = jnp.sum(W)
        sint = jnp.sum(s * W)
        s2 = jnp.sum(s*s * W)
        base = self.report(z)
        base.update(P_direct=float(p), J=float(j), scalar_deviation=float(q),
                    volume=float(vol), scalar_integral=float(sint), scalar_square=float(s2),
                    s_min=float(jnp.min(s)), s_max=float(jnp.max(s)))
        return base


def make_cell(x0, deg, nq, smooth_mode=True, X=1.0):
    c = DualCell(x0, X, deg, deg, nq)
    c.aligned = False
    c.wpow = 2 if smooth_mode else 1
    return c


def adapted_slice(cell, z, x):
    """Return bolt-adapted (a,b,c,a_dot,b_dot,c_dot), with dot=d/dt."""
    prof = cell.prof_factory(z)
    G, h = prof(x)
    # Fixed perpendicular branch is diagonal: old axes (bolt, transverse, CH fibre).
    old = jnp.sqrt(jnp.diag(h))
    # cyclic even permutation: new=(old2,old3,old1), so new c is the bolt axis
    abc = jnp.array([old[1], old[2], old[0]])
    dabc_dx = jax.jacfwd(lambda xx: jnp.array([
        jnp.sqrt(jnp.diag(prof(xx)[1]))[1],
        jnp.sqrt(jnp.diag(prof(xx)[1]))[2],
        jnp.sqrt(jnp.diag(prof(xx)[1]))[0]]))(x)
    dots = 2*jnp.sqrt(G)*dabc_dx
    return G, abc, dots


def transgression_parts(cell, z, xs):
    vals = jax.vmap(lambda x: adapted_slice(cell, z, x))(jnp.asarray(xs))
    Gs, abc, dots = vals
    a, b, c = abc[:, 0], abc[:, 1], abc[:, 2]
    ad, bd, cd = dots[:, 0], dots[:, 1], dots[:, 2]
    root = jnp.sqrt(a*b)
    pp = (b*ad - c + (a*a-b*b)/c)/root
    pm = (a*bd - c - (a*a-b*b)/c)/root
    e2w = a/b
    zz = c/root
    Y = cd - (e2w + 1/e2w) + zz*zz + pp*pm/2
    Pi = e2w*pp*pp + pm*pm/e2w - (pp*pm)**2/4
    return np.asarray(Y), np.asarray(Pi), np.asarray(Y*Y+Pi)


def profile_report(cell, z, n=401):
    # Avoid the removable 0/0 at the bolt; cluster logarithmically.
    u = np.linspace(2e-6, 1.0, n)
    xs = cell.x0*np.exp(cell.ell*u)
    Y, Pi, T = transgression_parts(cell, z, xs)
    # Curvature/cumulative Einstein cost on the same grid. This is slower but independent
    # of the optimization quadrature and exposes where the threshold is accumulated.
    prof = cell.prof_factory(z)
    g = metric_from(prof)
    def at(x):
        y = jnp.concatenate([jnp.array([x]), ANG])
        s, r0, wa, wb = curvature_scalars(g, y)
        G, h = prof(x)
        dv = PI**2*jnp.sqrt(jnp.linalg.det(h)/G)
        return s, r0, dv
    s, r0, dv = [np.asarray(v) for v in jax.vmap(at)(jnp.asarray(xs))]
    jd = (r0 + (s+24)**2/4)*dv
    pd = r0*dv
    def cumtrap(y):
        return np.concatenate([[0.0], np.cumsum((y[1:]+y[:-1])*np.diff(xs)/2)])
    HJ = cumtrap(jd)/(8*PI**2)
    HP = cumtrap(pd)/(8*PI**2)
    # In normalized units, the cumulative positive density B from the localized
    # J identity is B = HJ - 1 + T/(8pi2). This is not an independent certificate:
    # B-T = HJ-1 is just the cumulative threshold excess.
    intF = HJ - 1 + T
    kmin = int(np.nanargmin(T))
    # First crossing of the accumulated Einstein threshold, if present.
    cross = np.where(HJ >= 1)[0]
    out = dict(T_bolt_limit=1.0, T_collar=float(T[-1]), Y_collar=float(Y[-1]),
               Pi_collar=float(Pi[-1]), expected_T_collar=9.0,
               min_T=float(T[kmin]), x_at_min_T=float(xs[kmin]),
               min_Pi=float(np.nanmin(Pi)), max_Pi=float(np.nanmax(Pi)),
               P_grid=float(HP[-1]), J_grid=float(HJ[-1]),
               min_intF_minus_T=float(np.nanmin(intF-T)),
               threshold_cross_x=(float(xs[cross[0]]) if len(cross) else None))
    lines = [dict(x=float(x), Y=float(y), Pi=float(p), T=float(t),
                  P_cum=float(pc), J_cum=float(jc), intF=float(fi))
             for x, y, p, t, pc, jc, fi in zip(xs, Y, Pi, T, HP, HJ, intF)]
    return out, lines


def seed_vector(cell, rec):
    z = rec.get('z')
    if z is None:
        return np.zeros(cell.nparam)
    z = np.asarray(z, dtype=float)
    if len(z) == cell.nparam:
        return z
    # Embed/truncate each of cF,cG,cw separately when changing degree.
    olddeg = int(rec.get('degU', len(z)//3))
    oldw = int(rec.get('degw', olddeg))
    out = np.zeros(cell.nparam)
    n = min(olddeg, cell.degU)
    out[:n] = z[:n]
    out[cell.degU:cell.degU+n] = z[olddeg:olddeg+n]
    nw = min(oldw, cell.degw)
    out[2*cell.degU:2*cell.degU+nw] = z[2*olddeg:2*olddeg+nw]
    return out


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest='cmd', required=True)
    ae = sub.add_parser('eval'); ae.add_argument('record'); ae.add_argument('--profile', action='store_true')
    ao = sub.add_parser('opt')
    ao.add_argument('--x0', type=float, required=True); ao.add_argument('--target', choices=['P','J'], required=True)
    ao.add_argument('--deg', type=int, default=6); ao.add_argument('--nq', type=int, default=400)
    ao.add_argument('--seed'); ao.add_argument('--rough', action='store_true'); ao.add_argument('--maxiter', type=int, default=5000)
    ao.add_argument('--profile', action='store_true'); ao.add_argument('--out')
    args = ap.parse_args()

    if args.cmd == 'eval':
        rec = load_record(args.record)
        deg = int(rec.get('deg', rec.get('degU', 6))); x0 = float(rec['x0'])
        c = make_cell(x0, deg, 500, smooth_mode=int(rec.get('wpow', 2)) == 2, X=float(rec.get('X', 1.0)))
        z = seed_vector(c, rec)
        out = dict(mode='eval', source=args.record, x0=x0, deg=deg, wpow=c.wpow,
                   costs=c.full_report(jnp.asarray(z)), z=z.tolist())
        if args.profile:
            out['profile'], lines = profile_report(c, jnp.asarray(z))
            out['profile_lines'] = lines
        print(json.dumps(out)); return

    c = make_cell(args.x0, args.deg, args.nq, smooth_mode=not args.rough)
    rec = load_record(args.seed) if args.seed else {}
    z0 = seed_vector(c, rec)
    target = args.target
    fun = jax.jit(lambda z: c.target(z, target)); grad = jax.jit(jax.grad(lambda z: c.target(z, target)))
    # Compile before timing the optimizer.
    initial = c.full_report(jnp.asarray(z0)); _ = float(fun(jnp.asarray(z0))); _ = np.asarray(grad(jnp.asarray(z0)))
    t0 = time.time()
    res = minimize(lambda z: float(fun(jnp.asarray(z))), z0,
                   jac=lambda z: np.asarray(grad(jnp.asarray(z))), method='L-BFGS-B',
                   options=dict(maxiter=args.maxiter, ftol=2e-15, gtol=2e-11, maxls=60))
    z = jnp.asarray(res.x)
    out = dict(mode='opt', target=target, x0=args.x0, deg=args.deg, nq=args.nq, wpow=c.wpow,
               seed=args.seed, initial=initial, final=c.full_report(z),
               success=bool(res.success), message=str(res.message), nit=int(res.nit),
               grad_inf=float(np.max(np.abs(res.jac))), sec=time.time()-t0,
               z=[float(v) for v in res.x])
    if args.profile:
        out['profile'], lines = profile_report(c, z)
        out['profile_lines'] = lines
    text = json.dumps(out)
    print(text)
    if args.out:
        Path(args.out).write_text(text+'\n')


if __name__ == '__main__':
    main()

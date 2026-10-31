"""Conformal (Yamabe) selection on a complete CH-asymptotic diagonal cell, with an exact check.

Theorem being tested (Step 21 note): for g with e=s+24 and u>0 solving
    -6 Lap u + s u + 24 u^3 = 0,  u -> 1 at infinity      (s_{u^2 g} = -24),
one has, when boundary terms vanish,
    J6(g) - J6(u^2 g) = int [ 3 (Lap u/u)^2 + 24 |grad u|^2 + e^2/4 ] dV_g,
    P(g)  - P(u^2 g)  = int [ 3 (Lap u/u)^2 + 24 |grad u|^2 ] dV_g.

Here the cell metric on [x0,X] is the stored diagonal profile and, beyond X, exact CH
(G=x+x^2, h=diag(x,x,x+x^2), Ric=-6).  u solves the radial BVP on [x0, X*ext] with the natural
(zero-flux) bolt condition and u=1 at the far end (u-1 ~ x^{-(1+sqrt3)} in CH).  The left side
is computed *directly* from the conformal Ricci formula
    Ric_c = Ric - 2(Hess f - df df) - (Lap f + 2|df|^2) g,  f = log u,
so that agreement tests the integrated identity (integration by parts + Gauss-Bonnet
conformal invariance), not just algebra.  Float64 finite-volume numerics.

Usage: python yamabe_cell_check.py RECORD --N 60000 --ext 1e4 --out OUT.json
"""
import argparse, json, math
from pathlib import Path
import numpy as np
import scipy.sparse as sps
import scipy.sparse.linalg as spl
import jax, jax.numpy as jnp
jax.config.update('jax_enable_x64', True)
from perp_dual_cost import DualCell, load_record, seed_vector


def cell_fields(rec, xs):
    deg = int(rec['deg']); x0 = float(rec['x0']); X = float(rec['X'])
    c = DualCell(x0, X, deg, deg, 50); c.aligned = False; c.wpow = 2
    z = jnp.asarray(np.asarray(seed_vector(c, rec), float)); prof = c.prof_factory(z)

    def radii(x):
        G, h = prof(x); return jnp.sqrt(jnp.array([h[1, 1], h[2, 2], h[0, 0]])), G

    def state(x):
        a, G = radii(x); da = jax.jacfwd(lambda xx: radii(xx)[0])(x)*2*jnp.sqrt(G)
        a1, a2, a3 = a
        u = jnp.array([da[0]-(a2*a2+a3*a3-a1*a1)/(a2*a3), da[1]-(a3*a3+a1*a1-a2*a2)/(a3*a1),
                       da[2]-(a1*a1+a2*a2-a3*a3)/(a1*a2)])
        return u, a, G, da

    def at(x):
        u, a, G, da = state(x); ud = jax.jacfwd(lambda xx: state(xx)[0])(x)*2*jnp.sqrt(G)
        u1, u2, u3 = u; H = jnp.array([u1+u2*u3/2, u2+u3*u1/2, u3+u1*u2/2])
        r = ud/a; v = 2*H/jnp.array([a[1]*a[2], a[2]*a[0], a[0]*a[1]])
        zc = r-v; s = -2*jnp.sum(r+v); zs = jnp.sum(zc)
        R0 = (s-2*zs)/4; Ri = (s+2*zs)/4-zc
        return G, jnp.prod(a), jnp.concatenate([jnp.array([R0]), Ri]), da/a
    G, W, R, dlog = [np.asarray(q) for q in jax.jit(jax.vmap(at))(jnp.asarray(xs))]
    return G, W, R, dlog, x0, X


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('record'); ap.add_argument('--N', type=int, default=60000)
    ap.add_argument('--ext', type=float, default=1e4); ap.add_argument('--out')
    a = ap.parse_args(); rec = load_record(a.record)
    x0 = float(rec['x0']); X = float(rec['X'])
    # tau=log x grid; cell nodes strictly inside (x0,X], exterior nodes beyond.
    t0 = math.log(x0); tX = math.log(X); t1 = math.log(X*a.ext)
    nc = int(a.N*(tX-t0)/(t1-t0))
    tc = t0+(tX-t0)*(np.arange(1, nc+1)/nc)**1.0
    te = np.linspace(tX, t1, a.N-nc+1)[1:]
    # bolt layer: add geometric refinement near x0 (x-x0 ~ r^2)
    tb = t0+(tc[0]-t0)*np.geomspace(1e-6, 1, 200)[:-1]
    tau = np.concatenate([tb, tc, te]); x = np.exp(tau)
    ic = x <= X*(1+1e-14)
    G = np.empty_like(x); W = np.empty_like(x); R = np.empty((len(x), 4)); dlog = np.empty((len(x), 3))
    G[ic], W[ic], R[ic], dlog[ic], _, _ = cell_fields(rec, x[ic])
    xe = x[~ic]; G[~ic] = xe+xe*xe; W[~ic] = np.sqrt(xe*xe*xe*(1+xe)); R[~ic] = -6.0
    st = np.sqrt(G)  # dt = dx/(2 sqrt G)
    # a1=sqrt(x)?  exterior radii in (a1,a2,a3)=(s2,s3,s1) slot order: sqrt(x), sqrt(x+x^2), sqrt(x)
    dlog[~ic] = np.stack([2*st[~ic]*0.5/xe, 2*st[~ic]*(1+2*xe)/(2*(xe+xe*xe)), 2*st[~ic]*0.5/xe], 1)
    s = R.sum(1); e = s+24
    rho = W/(2*st)                 # sqrt(det g) per dx per unit orbit form
    q = rho*4*G                    # flux coefficient
    dvol = math.pi**2*W/st         # 2 pi^2 rho dx  (Vol element per dx)
    # finite-volume Laplacian on nonuniform x-grid; zero flux at the bolt (q(x0)=0)
    n = len(x); xm = np.concatenate([[x0], .5*(x[1:]+x[:-1]), [x[-1]]])
    qm = np.interp(xm, x, q); qm[0] = 0.0
    hl = np.diff(x)
    dxc = np.diff(xm)
    # Lap u_k = [qm_{k+1/2}(u_{k+1}-u_k)/h_k - qm_{k-1/2}(u_k-u_{k-1})/h_{k-1}]/(rho_k dxc_k)
    cR = np.zeros(n); cL = np.zeros(n)
    cR[:-1] = qm[1:-1]/hl; cL[1:] = qm[1:-1]/hl
    Lop = sps.diags([cL[1:], -(cL+cR), cR[:-1]], [-1, 0, 1], format='csr')
    Lop = sps.diags(1/(rho*dxc))@Lop
    u = np.ones(n)
    for it in range(30):
        Fv = -6*(Lop@u)+s*u+24*u**3
        Jm = -6*Lop+sps.diags(s+72*u**2)
        Fv[-1] = u[-1]-1; Jm = Jm.tolil(); Jm[n-1, :] = 0; Jm[n-1, n-1] = 1; Jm = Jm.tocsr()
        du = spl.spsolve(Jm, -Fv); u += du
        if np.max(np.abs(du)) < 1e-15: break
    # Use the equation itself: Lap u/u = (s+24u^2)/6 (no second differences of u).
    Lu = u*(s+24*u**2)/6
    # derivatives along t (one numerical derivative of log u only)
    ux = np.gradient(u, x); f = np.log(u); fx = np.gradient(f, x)
    ft = 2*st*fx; Lf = Lu/u-(ft**2)  # Lap log u = Lap u/u - |df|^2
    ftt = Lf-dlog.sum(1)*ft          # Lap f = f_tt + (W_t/W) f_t
    Rc = np.empty_like(R)
    Rc[:, 0] = R[:, 0]-2*(ftt-ft**2)-(Lf+2*ft**2)
    for i in range(3):
        Rc[:, 1+i] = R[:, 1+i]-2*ft*dlog[:, i]-(Lf+2*ft**2)
    def integ(y):
        k = np.searchsorted(x, X*a.ext/100)  # exclude the Dirichlet end layer (u-1 negligible there)
        return float(np.sum(.5*(y[1:k]+y[:k-1])*np.diff(x[:k]))/(8*math.pi**2))
    J_g = integ(np.sum((R+6)**2, 1)*dvol); P_g = integ(np.sum((R-s[:, None]/4)**2, 1)*dvol)
    sc = Rc.sum(1)/u**2
    J_c = integ(np.sum((Rc+6*u[:, None]**2)**2, 1)*dvol)
    P_c = integ(np.sum((Rc-(Rc.sum(1)/4)[:, None])**2, 1)*dvol)
    t1_ = integ(3*(Lu/u)**2*dvol); t2_ = integ(24*4*G*ux**2*dvol); t3_ = integ(e**2/4*dvol)
    m = (x > x0*1.001) & (x < X*a.ext/10)
    out = dict(record=a.record, x0=x0, X=X, N=n, ext=a.ext, newton_iter=it, u_min=float(u.min()), u_max=float(u.max()),
               u_at_bolt=float(u[0]), u_at_X=float(np.interp(X, x, u)),
               J_g=J_g, P_g=P_g, J_c_direct=J_c, P_c_direct=P_c,
               sc_plus24_max=float(np.max(np.abs(sc[m]+24))),
               lhs_J=J_g-J_c, rhs_J=t1_+t2_+t3_, lhs_P=P_g-P_c, rhs_P=t1_+t2_,
               terms=dict(lap=t1_, grad=t2_, scalar=t3_), stored_J=rec.get('J'))
    print(json.dumps(out, indent=1))
    if a.out: Path(a.out).write_text(json.dumps(out, indent=1)+'\n')


if __name__ == '__main__':
    main()

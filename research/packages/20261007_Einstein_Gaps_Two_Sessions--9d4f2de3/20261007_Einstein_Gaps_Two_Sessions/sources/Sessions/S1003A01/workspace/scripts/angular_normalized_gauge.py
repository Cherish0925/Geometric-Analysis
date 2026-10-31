"""Scalar-normalized and gauge-resolved j=1 angular second variation of a CH cell.

Mathematical content (Step 24).
At a base with s=-24 put B=-Delta>=0 and sigma=Ds[h].  The Yamabe-normalized path
g_t -> u_t^2 g_t (u_t -> 1 on the CH end) has, by the exact selection identity
J6(g)-J6(u^2 g)=int[24|grad u|^2+3(Lap u/u)^2+(s+24)^2/4],
second variation

   Qn(h) = QJ(h) - D(h),   D(h) = (2/3) <sigma,(B+6)(B+8)^{-1} sigma>
                               = (2/3)(|sigma|^2 - 2<sigma,(B+8)^{-1}sigma>),

with scalar response v = -(1/6)(B+8)^{-1} sigma and normalized tangent h+2v g.
Hence QJ-(2/3)|sigma|^2 <= Qn <= QJ-(1/2)|sigma|^2 (rigorous form bounds).

Gauge: for K X = L_X g - (1/2)(div X) g one has v = div X/4 and h+2vg = L_X g.
Pure trace h = phi g has normalized tangent 0, so Qn(phi g)=0 exactly at an exactly
normalized base.  Both are checked numerically here.

Everything lives in the fixed-left-row j=1 sector: F_b = sqrt3 Ad(q)_{0b}, b=0,1,2,
which is the complete multiplicity space of one left-isotypic copy.
Radial functions are localized C^infinity bumps (times u^2 at the bolt).
(B+8)^{-1} is solved by P2 finite elements per angular column on the cell plus an
exact-CH extension to x=ext*X (Galerkin => R from below, so computed Qn is an
upper approximation of exact Qn on the given space).

Units: all quadratic forms are in units of 8 pi^2, as J6/(8 pi^2).

Usage:
  python angular_normalized_gauge.py RECORD --nrad 4 --nvec 3 --nel 24 --nq 6 --out OUT.json
"""
import argparse, json, math, time
from pathlib import Path

import numpy as np
import jax
import jax.numpy as jnp
from numpy.polynomial.legendre import leggauss
jax.config.update('jax_enable_x64', True)

from perp_dual_cost import DualCell, load_record, seed_vector
from o11_rotated_cell import euler_E, curvature_scalars
from angular_isotype_probe import ad_row0

OFFDIAG = [(i, j) for i in range(4) for j in range(i+1, 4)]
DIAGDIFF = [(0, 3), (1, 3), (2, 3)]


def bump(z):
    inside = jnp.abs(z) < 1
    zz = jnp.where(inside, z, 0.0)
    return jnp.where(inside, jnp.exp(1.0 - 1.0/(1.0 - zz*zz)), 0.0)


def build(record, nrad, nvec, nel, nq, nqa, uhi, ext, n2, n3, trace_block, angular='col', vpow=2):
    rec = load_record(record); x0 = float(rec['x0']); X = float(rec['X']); deg = int(rec['deg'])
    cell = DualCell(x0, X, deg, deg, 200); cell.aligned = False; cell.wpow = 2
    z = jnp.asarray(np.asarray(seed_vector(cell, rec), float)); prof = cell.prof_factory(z)
    ell = math.log(X/x0)

    def ch_prof(x):
        return x + x*x, jnp.diag(jnp.array([x, x, x*(1+x)]))

    # radial bumps in u = log(x/x0)/ell
    def centers(n):
        d = uhi/(n - 1 + 1.5); return d*np.arange(n), 1.5*d
    cr, wr = centers(nrad); cv, wv = centers(nvec)

    def radial(u, cs, w, p=2):
        return jnp.stack([u**p*bump((u - c)/w) for c in cs])

    # angular Haar quadrature (normalized), as in angular_isotype_conformal
    alphas = 2*math.pi*(np.arange(nqa)+.37)/nqa; betas = 2*math.pi*(np.arange(nqa)+.11)/nqa
    ec, wc = leggauss(nqa); wc = .5*wc
    angs = []; wang = []
    for aa in alphas:
        for bb in betas:
            for cc, ww in zip(ec, wc):
                angs.append([float(aa), math.acos(float(cc)), float(bb)]); wang.append(ww/nqa/nqa)
    angs = jnp.asarray(angs); wang = jnp.asarray(wang)

    def Fb(y):
        # Euler rotation R=Rz(psi)Ry(theta)Rz(phi).  The left-invariant vector fields
        # act on the ROW index of R in this convention (checked: the angular Laplacian is
        # scalar on each row, but distinguishes rows).  A fixed row is one irreducible copy
        # of the left j=1 representation; the multiplicity space is a fixed COLUMN.
        if angular == 'row':
            return jnp.sqrt(3.0)*ad_row0(y[1], y[3], 0.5*y[2])
        ps, th, ph = y[1], y[2], y[3]
        cp, sp, ct, st, cf, sf = jnp.cos(ps), jnp.sin(ps), jnp.cos(th), jnp.sin(th), jnp.cos(ph), jnp.sin(ph)
        return jnp.sqrt(3.0)*jnp.array([cp*ct*cf-sp*sf, sp*ct*cf+cp*sf, -st*cf])

    def make_base(pf):
        def base(y):
            G, h = pf(y[0]); E = euler_E(y[1:])
            gm = jnp.zeros((4, 4)).at[0, 0].set(1/(4*G))
            return gm.at[1:, 1:].set(E.T@h@E)
        def coframe(y):
            G, h = pf(y[0]); E = euler_E(y[1:])
            C = jnp.zeros((4, 4)).at[0, 0].set(1.0).at[1:, 1:].set(E)
            L = jnp.diag(jnp.concatenate([jnp.array([1/(2*jnp.sqrt(G))]), jnp.sqrt(jnp.diag(h))]))
            return L@C
        return base, coframe
    base, coframe = make_base(prof)
    base_ch, _ = make_base(ch_prof)

    S_list = []
    for A, Bq in OFFDIAG:
        S_list.append(np.zeros((4, 4))); S_list[-1][A, Bq] = S_list[-1][Bq, A] = 1.0
    for A, Bq in DIAGDIFF:
        S_list.append(np.zeros((4, 4))); S_list[-1][A, A] = 1.0; S_list[-1][Bq, Bq] = -1.0
    S_arr = jnp.asarray(np.stack(S_list))

    n_tf = 9*3*nrad; n_tr = (3*nrad if trace_block else 0); n_kx = 4*3*nvec
    n = n_tf + n_tr + n_kx

    def vecfields(y):
        u = jnp.log(y[0]/x0)/ell; fv = radial(u, cv, wv, vpow); F = Fb(y)
        Minv = jnp.linalg.inv(coframe(y))      # columns: orthonormal frame vectors
        out = []
        for b in range(3):
            for k in range(nvec):
                for A in range(4):
                    out.append(F[b]*fv[k]*Minv[:, A])
        return jnp.stack(out)                   # (n_kx, 4)

    def modes(y):
        u = jnp.log(y[0]/x0)/ell; fr = radial(u, cr, wr); F = Fb(y)
        g = base(y); M = coframe(y)
        tens = jnp.einsum('ai,mab,bj->mij', M, S_arr, M)   # coordinate tensors of frame basis
        out = [F[b]*fr[k]*tens[m] for b in range(3) for k in range(nrad) for m in range(9)]
        if trace_block:
            out += [F[b]*fr[k]*g for b in range(3) for k in range(nrad)]
        Xs = vecfields(y); dX = jax.jacfwd(vecfields)(y)    # dX[i,rho,mu]=d_mu X^rho
        dg = jax.jacfwd(base)(y)                            # dg[a,b,c]=d_c g_ab
        gi = jnp.linalg.inv(g)
        LX = (jnp.einsum('ir,abr->iab', Xs, dg) + jnp.einsum('irm,rn->imn', dX, g)
              + jnp.einsum('mr,irn->imn', g, dX))
        divX = 0.5*jnp.einsum('ab,iab->i', gi, LX)
        KX = LX - 0.5*divX[:, None, None]*g[None]
        return jnp.concatenate([jnp.stack(out), KX]), divX

    def metric(y, c):
        md, _ = modes(y)
        return base(y) + jnp.tensordot(c, md, axes=1)

    def volw(y, gm):
        return jnp.sqrt(jnp.linalg.det(gm))/jnp.sin(y[2])

    def dens(y, c):
        gm = metric(y, c); s, r0, _, _ = curvature_scalars(lambda yy: metric(yy, c), y)
        return (r0 + (s + 24.0)**2/4)*volw(y, gm)

    def sfun(y, c):
        return curvature_scalars(lambda yy: metric(yy, c), y)[0]

    def pointdata(y):
        g = base(y); gi = jnp.linalg.inv(g); md, divX = modes(y)
        gram = jnp.einsum('mij,nkl,ik,jl->mn', md, md, gi, gi)
        sig = jax.jacfwd(sfun, argnums=1)(y, jnp.zeros(n))
        dmd = jax.jacfwd(lambda yy: modes(yy)[0])(y)        # [m,i,j,k] = d_k h_ij
        dg = jax.jacfwd(base)(y)                            # [a,b,c] = d_c g_ab
        t = jnp.einsum('dik->dki', dg) + dg - jnp.einsum('kid->dki', dg)   # d_k g_di + d_i g_dk - d_d g_ki
        Gam = 0.5*jnp.einsum('ld,dki->lki', gi, t)
        nab = (dmd - jnp.einsum('lki,mlj->mijk', Gam, md) - jnp.einsum('lkj,mil->mijk', Gam, md))
        delta = -jnp.einsum('ik,mijk->mj', gi, nab)        # (delta h)_j = -nabla^i h_ij
        dF = jax.jacfwd(Fb)(y)
        return sig, gram, divX, Fb(y), volw(y, g), delta, dF, gi

    def lap_F(bf, y):
        def grad_flux(yy):
            gm = bf(yy); gi = jnp.linalg.inv(gm); vol = jnp.sqrt(jnp.linalg.det(gm))
            dF = jax.jacfwd(Fb)(yy)              # (3,4)
            return vol*jnp.einsum('mn,bn->bm', gi, dF)
        dflux = jax.jacfwd(grad_flux)(y)          # (3,4,4)
        vol = jnp.sqrt(jnp.linalg.det(bf(y)))
        return jnp.einsum('bmm->b', dflux)/vol

    # radial elements
    eg, wg = leggauss(nq)
    def elements(ua, ub, ne):
        edges = np.linspace(ua, ub, ne+1); return [(edges[i], edges[i+1]) for i in range(ne)]
    el_h = elements(0.0, uhi, nel)
    el_f = el_h + elements(uhi, 1.0, n2) + elements(1.0, 1.0 + math.log(ext)/ell, n3)

    def gauss_pts(els):
        us = []; wu = []
        for ua, ub in els:
            us += list(.5*(ub-ua)*eg + .5*(ub+ua)); wu += list(.5*(ub-ua)*wg)
        us = np.array(us); xs = x0*np.exp(ell*us); wx = np.array(wu)*ell*xs
        return us, xs, wx
    us_h, xs_h, wx_h = gauss_pts(el_h)
    us_f, xs_f, wx_f = gauss_pts(el_f)

    meta = dict(x0=x0, X=X, deg=deg, nrad=nrad, nvec=nvec, nel=nel, nq=nq, nqa=nqa, uhi=uhi, ext=ext,
                n2=n2, n3=n3, angular=angular, vpow=vpow, n_tf=n_tf, n_tr=n_tr, n_kx=n_kx, n=n, bump_halfwidth=float(wr))
    return dict(Fb=Fb, modes=modes, vecfields=vecfields, coframe=coframe, dens=dens, pointdata=pointdata, lap_F=lap_F, base=base, base_ch=base_ch,
                angs=angs, wang=wang, us_h=us_h, xs_h=xs_h, wx_h=wx_h, us_f=us_f, xs_f=xs_f,
                wx_f=wx_f, el_f=el_f, eg=eg, wg=wg, ell=ell, x0=x0, X=X, prof=prof, rec=rec, meta=meta)


def p2_shape(xi):
    N = np.array([xi*(xi-1)/2, 1-xi*xi, xi*(xi+1)/2])
    dN = np.array([xi-.5, -2*xi, xi+.5])
    return N, dN


def whiten(H, G, tol=1e-10):
    ge, gv = np.linalg.eigh((G+G.T)/2); keep = ge > ge.max()*tol
    Q = gv[:, keep]/np.sqrt(ge[keep])[None, :]
    Hn = Q.T@H@Q; Hn = (Hn+Hn.T)/2
    ev, V = np.linalg.eigh(Hn)
    return ev, Q@V, int(keep.sum())


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('record')
    ap.add_argument('--nrad', type=int, default=4); ap.add_argument('--nvec', type=int, default=3)
    ap.add_argument('--nel', type=int, default=24); ap.add_argument('--nq', type=int, default=6)
    ap.add_argument('--nqa', type=int, default=3); ap.add_argument('--uhi', type=float, default=0.9)
    ap.add_argument('--ext', type=float, default=100.0); ap.add_argument('--n2', type=int, default=8)
    ap.add_argument('--n3', type=int, default=24); ap.add_argument('--trace', action='store_true')
    ap.add_argument('--angular', default='col', choices=['col', 'row']); ap.add_argument('--vpow', type=int, default=2)
    ap.add_argument('--chunk', type=int, default=64); ap.add_argument('--out')
    a = ap.parse_args(); t0 = time.time()
    B = build(a.record, a.nrad, a.nvec, a.nel, a.nq, a.nqa, a.uhi, a.ext, a.n2, a.n3, a.trace, a.angular, a.vpow)
    meta = B['meta']; n = meta['n']; angs = B['angs']; wang = np.asarray(B['wang']); na_ = len(wang)
    dens = B['dens']; c0 = jnp.zeros(n)

    # ---- Hessian points
    pts = []; pw = []
    for x, wx in zip(B['xs_h'], B['wx_h']):
        for k in range(na_):
            pts.append([x, *np.asarray(angs[k])]); pw.append(wx*wang[k])
    pts = jnp.asarray(pts); pw = jnp.asarray(pw)
    hess_pt = jax.jit(jax.vmap(lambda y: jax.hessian(dens, argnums=1)(y, c0)))
    val_pt = jax.jit(jax.vmap(lambda y: dens(y, c0)))
    pd_pt = jax.jit(jax.vmap(B['pointdata']))
    H = np.zeros((n, n)); J0 = 0.0; Sg = np.zeros((n, n)); Gm = np.zeros((n, n))
    npt = pts.shape[0]; nx = len(B['xs_h'])
    sig_all = np.zeros((npt, n)); F_all = np.zeros((npt, 3)); div_all = np.zeros((npt, meta['n_kx'])); V_all = np.zeros(npt)
    del_all = np.zeros((npt, n, 4)); dF_all = np.zeros((npt, 3, 4)); gi_all = np.zeros((npt, 4, 4))
    for i in range(0, npt, a.chunk):
        yy = pts[i:i+a.chunk]; ww = np.asarray(pw[i:i+a.chunk])
        H += 2*np.einsum('p,pij->ij', ww, np.asarray(hess_pt(yy)))
        J0 += 2*float(np.sum(ww*np.asarray(val_pt(yy))))
        sig, gram, divX, F, V, dl, dF, gi = [np.asarray(t) for t in pd_pt(yy)]
        Gm += 2*np.einsum('p,pij->ij', ww*V, gram); Sg += 2*np.einsum('p,pi,pj->ij', ww*V, sig, sig)
        sig_all[i:i+len(ww)] = sig; F_all[i:i+len(ww)] = F; div_all[i:i+len(ww)] = divX; V_all[i:i+len(ww)] = V
        del_all[i:i+len(ww)] = dl; dF_all[i:i+len(ww)] = dF; gi_all[i:i+len(ww)] = gi
    H = (H+H.T)/2; Gm = (Gm+Gm.T)/2; Sg = (Sg+Sg.T)/2
    t_h = time.time() - t0

    # angular projections at Hessian radii: c[x,b,mode] = <sigma, F_b>_Haar ; same for divX
    sigr = sig_all.reshape(nx, na_, n); Fr = F_all.reshape(nx, na_, 3); Vr = V_all.reshape(nx, na_)
    csig = np.einsum('k,xkb,xkm->xbm', wang, Fr, sigr)
    cdiv = np.einsum('k,xkb,xkm->xbm', wang, Fr, div_all.reshape(nx, na_, -1))
    Vx = Vr.mean(1); V_spread = float(np.max(np.abs(Vr - Vx[:, None]))/np.max(np.abs(Vx)))
    # span check: residual of sigma outside span{F_b}
    sig_recon = np.einsum('xbm,xkb->xkm', csig, Fr)
    span_res = float(np.sqrt(np.sum(wang[None, :, None]*(sigr - sig_recon)**2)/max(np.sum(wang[None, :, None]*sigr**2), 1e-300)))

    # ---- FEM for (B+8) y = c on all radial elements
    base = B['base']; base_ch = B['base_ch']; lap_F = B['lap_F']; X = B['X']; x0 = B['x0']; ell = B['ell']
    eg, wg = B['eg'], B['wg']; el_f = B['el_f']; nqp = len(eg)
    Fbv = jax.vmap(B['Fb'])
    lapv = {k: jax.jit(jax.vmap(lambda y, bf=bf: lap_F(bf, y))) for k, bf in [('in', base), ('ch', base_ch)]}
    basev = {k: jax.jit(jax.vmap(bf)) for k, bf in [('in', base), ('ch', base_ch)]}
    angs_np = np.asarray(angs)
    def coeffs(x):
        key = 'in' if x <= X*(1+1e-12) else 'ch'
        ys = jnp.asarray(np.column_stack([np.full(na_, x), angs_np]))
        L = np.asarray(lapv[key](ys)); F = np.asarray(Fbv(ys))
        Kb = np.einsum('k,kc,kb->cb', wang, F, L)    # Kb[c,b] = <F_c, Lap F_b>
        gm = np.asarray(basev[key](ys[:1]))[0]
        V = math.sqrt(np.linalg.det(gm))/math.sin(float(angs_np[0, 1])); ginv_xx = 1/gm[0, 0]
        return V, ginv_xx, Kb
    ys_t = jnp.asarray(np.column_stack([np.full(na_, 1.0), angs_np])); Ft = np.asarray(Fbv(ys_t))
    haar_gram = np.einsum('k,kb,kc->bc', wang, Ft, Ft); haar_mean = np.einsum('k,kb->b', wang, Ft)
    K_samples = {str(xx): np.diag(coeffs(xx)[2]).tolist() for xx in [0.1, 1.0, 10.0]}
    nE = len(el_f); nnode = 2*nE + 1; ndof = 3*nnode
    A = np.zeros((ndof, ndof)); coef_cache = []
    for e, (ua, ub) in enumerate(el_f):
        for q in range(nqp):
            xi = eg[q]; u = .5*(ub-ua)*xi + .5*(ub+ua); x = x0*math.exp(ell*u)
            V, gxx, Kb = coeffs(x); coef_cache.append((V, gxx, Kb))
            N, dN = p2_shape(xi); dxdxi = .5*(ub-ua)*ell*x; dNdx = dN/dxdxi
            w = wg[q]*dxdxi*V
            idx = [2*e, 2*e+1, 2*e+2]
            for bb in range(3):
                for cc in range(3):
                    M = w*((8.0*(bb == cc) - Kb[bb, cc])*np.outer(N, N))
                    if bb == cc: M = M + w*gxx*np.outer(dNdx, dNdx)
                    rows = [bb*nnode+i for i in idx]; cols = [cc*nnode+j for j in idx]
                    A[np.ix_(rows, cols)] += M
    A = (A+A.T)/2
    # RHS from csig on the Hessian elements (identical first nel elements, same Gauss points)
    nel = meta['nel']
    def load(cfun):   # cfun: array (nx,3,m) at Hessian Gauss points
        m = cfun.shape[2]; Fv = np.zeros((ndof, m))
        for e in range(nel):
            ua, ub = el_f[e]
            for q in range(nqp):
                ix = e*nqp + q; xi = eg[q]; x = B['xs_h'][ix]
                N, _ = p2_shape(xi); dxdxi = .5*(ub-ua)*ell*x; V = coef_cache[e*nqp+q][0]
                w = wg[q]*dxdxi*V
                for bb in range(3):
                    Fv[[bb*nnode+2*e+i for i in range(3)], :] += w*np.outer(N, cfun[ix, bb, :])
        return Fv
    Fsig = load(csig)
    Ysol = np.linalg.solve(A, Fsig)
    R = 2*Fsig.T@Ysol; R = (R+R.T)/2                       # <sigma,(B+8)^{-1}sigma>/(8pi^2)
    # continuity check of coefficients at X
    Vin, gin, Kin = coeffs(X*(1-1e-9)); Vout, gout, Kout = coeffs(X*(1+1e-9))
    # v at Hessian points: v = -(1/6) y
    vnod = -Ysol/6.0
    vpt = np.zeros((nx, 3, n)); dvpt = np.zeros((nx, 3, n))
    for e in range(nel):
        ua, ub = el_f[e]
        for q in range(nqp):
            N, dN = p2_shape(eg[q]); dxdxi = .5*(ub-ua)*ell*B['xs_h'][e*nqp+q]
            for bb in range(3):
                nodes = [bb*nnode+2*e+i for i in range(3)]
                vpt[e*nqp+q, bb, :] = N@vnod[nodes, :]
                dvpt[e*nqp+q, bb, :] = (dN/dxdxi)@vnod[nodes, :]
    # Bianchi operator of the normalized tangent T=h+2vg (h trace free): beta(T)=delta h + 2 dv.
    vP = np.repeat(vpt, na_, axis=0); dvP = np.repeat(dvpt, na_, axis=0)    # (npt,3,n)
    dv_cov = np.einsum('pbm,pbk->pmk', vP, dF_all)                          # angular+x derivative of F part
    dv_cov[:, :, 0] += np.einsum('pbm,pb->pm', dvP, F_all)
    beta = del_all + 2*dv_cov                                               # (npt,n,4)
    wB = 2*np.asarray(pw)*V_all
    Bm = np.einsum('p,pmj,pjk,pnk->mn', wB, beta, gi_all, beta); Bm = (Bm+Bm.T)/2
    Bd = np.einsum('p,pmj,pjk,pnk->mn', wB, del_all, gi_all, del_all); Bd = (Bd+Bd.T)/2
    dT = del_all - 2*dv_cov                                                  # delta(h+2vg)
    Bl = np.einsum('p,pmj,pjk,pnk->mn', wB, dT, gi_all, dT); Bl = (Bl+Bl.T)/2
    # normalized Gram: <h,k> + 2v tr k + 2w tr h + 16 v w ; tr of tf/KX seeds is 0, trace seeds tr=4phi
    Vw = 2*np.asarray(B['wx_h'])*Vx
    VV = np.einsum('x,xbm,xbn->mn', Vw, vpt, vpt)
    GT = Gm + 16*VV
    # (GT is used only on trace-free seeds and K X modes; trace seeds have zero normalized tangent.)
    D = (2.0/3.0)*(Sg - 2*R); Qn = H - D; Qn = (Qn+Qn.T)/2
    t_all = time.time() - t0

    ntf, ntr, nkx = meta['n_tf'], meta['n_tr'], meta['n_kx']
    I_tf = np.arange(ntf); I_tr = np.arange(ntf, ntf+ntr); I_kx = np.arange(ntf+ntr, n)
    def sub(Mx, I): return Mx[np.ix_(I, I)]
    out = dict(record=a.record, **meta, J0=J0, stored_J=B['rec'].get('J'), sec_hessian=t_h, sec=t_all,
               V_angle_spread=V_spread, sigma_outside_span_rel=span_res, haar_gram=haar_gram.tolist(),
               haar_mean=haar_mean.tolist(), K_diag_samples=K_samples,
               coeff_jump_at_X=dict(V=[Vin, Vout], gxx=[gin, gout], K_in=Kin.tolist(), K_out=Kout.tolist()))
    # tf seed spectra
    blocks = {}
    for name, Mx in [('raw', H), ('lower_bound', H-(2/3)*Sg), ('upper_bound', H-.5*Sg), ('normalized', Qn)]:
        ev, _, rk = whiten(sub(Mx, I_tf), sub(Gm, I_tf)); blocks[name] = [float(v) for v in ev[:8]]
    evT, VT, rkT = whiten(sub(Qn, I_tf), sub(GT, I_tf))
    blocks['normalized_TGram'] = [float(v) for v in evT[:8]]
    out['tf_spectra'] = blocks
    # Bianchi gauge-fixed normalized spectra Qn + c|beta(T)|^2 on trace-free seeds
    bgf = {}
    for cpen in [0.1, 1.0, 10.0, 100.0]:
        ev, Vv, _ = whiten(sub(Qn, I_tf) + cpen*sub(Bm, I_tf), sub(GT, I_tf))
        lowv = Vv[:, 0]; bfrac = float(lowv@sub(Bm, I_tf)@lowv)
        bgf[str(cpen)] = dict(eigs=[float(v) for v in ev[:8]], lowest_Qn=float(lowv@Qtf_@lowv) if (Qtf_ := sub(Qn, I_tf)) is not None else None,
                              lowest_bianchi=bfrac)
    out['bianchi_gauge_fixed'] = bgf
    evd, _, _ = whiten(sub(Bd, I_tf), sub(Gm, I_tf)); evb, _, _ = whiten(sub(Bm, I_tf), sub(GT, I_tf))
    out['tf_divergence_ratio_eigs'] = [float(v) for v in evd[:8]]
    out['tf_bianchi_ratio_eigs'] = [float(v) for v in evb[:8]]
    # Ritz values of Qn on the numerical kernels of the Bianchi map and of the L2-slice map delta T
    for name, Mk in [('bianchi_slice', Bm), ('L2_slice', Bl)]:
        evk, Vk, _ = whiten(sub(Mk, I_tf), sub(GT, I_tf)); res = {}
        for eps in [1e-4, 1e-3, 1e-2, 1e-1]:
            sel = Vk[:, evk < eps]
            if sel.shape[1] == 0: res[str(eps)] = dict(dim=0); continue
            Qk = sel.T@sub(Qn, I_tf)@sel; Qk = (Qk+Qk.T)/2; ek = np.linalg.eigvalsh(Qk)
            res[str(eps)] = dict(dim=int(sel.shape[1]), eigs=[float(v) for v in ek[:6]])
        out[name + '_Qn_ritz'] = res
    evn, Vn, _ = whiten(sub(Qn, I_tf), sub(GT, I_tf))
    out['normalized_low_modes_bianchi_ratio'] = [float(Vn[:, i]@sub(Bm, I_tf)@Vn[:, i]) for i in range(min(6, Vn.shape[1]))]
    if meta['n_kx']:
        evk, Vk, _ = whiten(sub(Bm, I_kx), sub(GT, I_kx))
        out['bianchi_on_gauge_tangents_eigs'] = [float(v) for v in evk[:8]]
    # diagonal data of seeds: share of D in raw
    out['tf_mode_D_over_QJ_median'] = float(np.median(np.diag(D)[I_tf]/np.diag(H)[I_tf]))
    # trace benchmark: Qn should vanish
    if ntr:
        out['trace_benchmark'] = dict(QJ_diag=[float(v) for v in np.diag(H)[I_tr]], D_diag=[float(v) for v in np.diag(D)[I_tr]],
                                      Qn_diag=[float(v) for v in np.diag(Qn)[I_tr]],
                                      rel=float(np.linalg.norm(sub(Qn, I_tr))/np.linalg.norm(sub(H, I_tr))))
    # gauge benchmark: v(KX) = divX/4 and Qn(KX) ~ 0
    if nkx:
        vk = vpt[:, :, I_kx]; dk = cdiv/4.0
        num = np.einsum('x,xbm->m', Vw, (vk-dk)**2); den = np.einsum('x,xbm->m', Vw, dk**2)
        relv = np.sqrt(num/np.maximum(den, 1e-300))
        sigK = np.sqrt(np.diag(Sg)[I_kx]); hK = np.sqrt(np.abs(np.diag(H)[I_kx]))
        evK, _, _ = whiten(sub(Qn, I_kx), sub(GT, I_kx))
        evKraw, _, _ = whiten(sub(H, I_kx), sub(Gm, I_kx))
        out['gauge_benchmark'] = dict(v_vs_divX4_rel_median=float(np.median(relv)), v_vs_divX4_rel_max=float(np.max(relv)),
                                      v_vs_divX4_rel_by_mode=[float(v) for v in relv],
                                      Qn_KX_diag=[float(v) for v in np.diag(Qn)[I_kx]],
                                      QJ_KX_diag=[float(v) for v in np.diag(H)[I_kx]],
                                      order='modes ordered (column b, radial k, frame A) with A fastest',
                                      Qn_KX_TGram_eigs=[float(v) for v in evK], raw_KX_eigs_min=float(evKraw[0]),
                                      raw_KX_eigs_max=float(evKraw[-1]))
        # gauge quotient on tf+KX span: complement of KX tangents in GT
        I_g = np.concatenate([I_tf, I_kx]); Gs = sub(GT, I_g); Qs = sub(Qn, I_g)
        ge, gv = np.linalg.eigh(Gs); keep = ge > ge.max()*1e-10; W = gv[:, keep]/np.sqrt(ge[keep])
        Qw = W.T@Qs@W; Kpos = np.arange(ntf, ntf+nkx)
        # coordinates of KX tangents in whitened basis
        Kw = W.T@Gs[:, Kpos]                     # GT-inner products -> whitened coords
        Uk, sk, _ = np.linalg.svd(Kw, full_matrices=False); Uk = Uk[:, sk > sk[0]*1e-8]
        P = np.eye(Qw.shape[0]) - Uk@Uk.T
        Ec, Vc = np.linalg.eigh(P@Qw@P)
        # remove the gauge zeros introduced by projection
        comp = [i for i in range(len(Ec)) if np.linalg.norm(Uk.T@Vc[:, i]) < 1e-6]
        evq = np.sort(Ec[comp])
        out['gauge_quotient_eigs'] = [float(v) for v in evq[:10]]
        out['gauge_quotient_dim'] = len(comp)
        # overlap of low normalized tf modes with KX tangent span
        ovl = []
        for i in range(min(6, VT.shape[1])):
            vfull = np.zeros(len(I_g)); vfull[:ntf] = VT[:, i]
            vw = np.linalg.lstsq(W, vfull, rcond=None)[0]
            nrm = vfull@Gs@vfull
            ovl.append(float(np.linalg.norm(Uk.T@(W.T@Gs@vfull))**2/nrm))
        out['tf_low_modes_gauge_overlap'] = ovl
        # tf-only slice: h in tf span with <h+2v g, L_X g> = 0 for every X in the family.
        Cc = GT[np.ix_(I_tf, I_kx)]
        Uc, sc, Vhc = np.linalg.svd(Cc.T, full_matrices=True); rc = int(np.sum(sc > sc[0]*1e-9))
        Ns = Vhc.T[:, rc:]
        evs, Vs, rks = whiten(Ns.T@sub(Qn, I_tf)@Ns, Ns.T@sub(GT, I_tf)@Ns)
        evr, _, _ = whiten(Ns.T@sub(H, I_tf)@Ns, Ns.T@sub(Gm, I_tf)@Ns)
        out['tf_slice_dim'] = int(Ns.shape[1]); out['tf_slice_normalized_eigs'] = [float(v) for v in evs[:10]]
        out['tf_slice_raw_eigs'] = [float(v) for v in evr[:10]]
        # radial localization of lowest slice modes: Gram weight per radial bump k
        nr = meta['nrad']; loc = []
        for i in range(min(4, Vs.shape[1])):
            av = Ns@Vs[:, i]; w = np.zeros(nr)
            for k in range(nr):
                idx = [b*nr*9 + k*9 + m for b in range(3) for m in range(9)]
                w[k] = av[idx]@sub(Gm, I_tf)[np.ix_(idx, idx)]@av[idx]
            loc.append((w/w.sum()).tolist())
        out['tf_slice_low_mode_radial_weights'] = loc
        out['radial_bump_centers_u'] = [float(c) for c in (meta['uhi']/(nr-1+1.5))*np.arange(nr)]
        # Gauge-invariant Rayleigh quotient on tf seeds: denominator = GT norm of the part of
        # the normalized tangent orthogonal to span{L_X g}.  Uses Qn only on tf seeds (accurate);
        # valid because Qn is gauge invariant up to the Ward term of the (nearly stationary) base.
        Gkk = sub(GT, I_kx); Gsl = sub(GT, I_tf) - Cc@np.linalg.pinv(Gkk, rcond=1e-12)@Cc.T
        Gsl = (Gsl+Gsl.T)/2; Qtf = sub(Qn, I_tf)
        gsl = {}
        for tol in [1e-2, 1e-3, 1e-4, 1e-6]:
            ge, gv = np.linalg.eigh(Gsl); keep = ge > tol*np.max(np.diag(sub(GT, I_tf)))
            Wq = gv[:, keep]/np.sqrt(ge[keep]); ev = np.linalg.eigvalsh(Wq.T@Qtf@Wq)
            gsl[str(tol)] = dict(dim=int(keep.sum()), eigs=[float(v) for v in ev[:8]])
        out['gauge_invariant_quotient'] = gsl
        # pure-gauge content of tf span: Gram eigenvalues of slice part relative to full
        ge0 = np.linalg.eigvalsh(np.linalg.solve(sub(GT, I_tf) + 1e-300*np.eye(ntf), Gsl))
        out['slice_fraction_eigs_low'] = [float(v) for v in np.sort(ge0)[:10]]
    out['interpretation'] = ('finite j=1 fixed-row block; normalized = exact Yamabe-normalized second variation up to FEM '
                             'and base-normalization residual; lower/upper are rigorous form bounds; gauge quotient uses '
                             'normalized-tangent Gram complement of K X modes')
    text = json.dumps(out, indent=1); print(text)
    if a.out: Path(a.out).write_text(text + '\n')


if __name__ == '__main__':
    main()

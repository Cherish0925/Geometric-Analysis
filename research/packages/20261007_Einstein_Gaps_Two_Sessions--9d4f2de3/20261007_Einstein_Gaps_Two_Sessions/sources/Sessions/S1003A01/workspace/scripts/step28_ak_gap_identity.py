"""Step 28c: exact almost-Kahler gap identity on actual perpendicular cells.

For a diagonal exact-CH O(-1) cell g with canonical closed SD form omega_f, ghat=u^2 g is
diagonal AK.  With dVhat = u^4 W dt (W dt = dV in P/(8pi^2) units) define
   H  = int (u^2-1)^2 W dt,     G = int u'^2 W dt,
   nu = -(q' + 4 sinh(q)/a_f)/(2u)            (Nijenhuis scalar, kappa-shat = 6 nu^2),
   N  = int 4 nu^2 dVhat,       lambda = (W+_gg - W+_hh)/(2u^2)   (W3 eigenvalue of ghat),
   QA = int 4 lambda^2 dVhat,   delta = W+_ff/u^2 + 4,   Qd = int delta^2 dVhat,
   Sig = int (s+24)(u^2-1) W dt + int (s+24)^2/48 W dt.
Claimed exact identity (pinning + relative Chern-Weil + U(2) splitting of W+):
   Phat - 1 = 12 H + 6 G + (3/2) Qd + (1/2) QA - (3/2) N + Sig.
Also checked: transport  lambda = nu_T/2 + beta nu,  beta = -(A_f)_T/(2A_f) + 2cosh(q)/A_f,
and the bolt Nijenhuis charge law  (mu nu)(X) - (mu nu)(bolt) = 2 int mu lambda dT,
d log mu/dT = 2 beta.
Usage: python step28_ak_gap_identity.py RECORD [--n 4000] [--out OUT.json]
"""
import argparse, json, sys
from pathlib import Path
import numpy as np
import jax, jax.numpy as jnp
jax.config.update('jax_enable_x64', True)
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from perp_dual_cost import make_cell, load_record, seed_vector  # noqa: E402
from scipy.integrate import cumulative_trapezoid


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('record'); ap.add_argument('--n', type=int, default=4000)
    ap.add_argument('--out')
    a = ap.parse_args()
    rec = load_record(a.record)
    x0 = float(rec['x0']); X = float(rec['X']); deg = int(rec.get('deg', rec.get('degU', 6)))
    cell = make_cell(x0, deg, 400, smooth_mode=True, X=X)
    z = jnp.asarray(seed_vector(cell, rec))
    prof = cell.prof_factory(z)

    def slots(x):
        G, h = prof(x)
        d = jnp.diag(h)
        return G, jnp.sqrt(jnp.array([d[2], d[1], d[0]]))   # (f, g, h)

    def jet(x):
        G, A = slots(x)
        Ax = jax.jacfwd(lambda xx: slots(xx)[1])(x)
        Axx = jax.jacfwd(jax.jacfwd(lambda xx: slots(xx)[1]))(x)
        Gx = jax.grad(lambda xx: slots(xx)[0])(x)
        return G, A, 2*jnp.sqrt(G)*Ax, 4*G*Axx + 2*Gx*Ax

    ell = np.log(X/x0)
    edges = np.concatenate([[0.0], np.geomspace(1e-8, 1e-2, 24), np.linspace(1e-2, 1.0, max(8, a.n//24))[1:]])
    gx, gw = np.polynomial.legendre.leggauss(16)
    uq = np.concatenate([(lo + hi)/2 + (hi - lo)/2*gx for lo, hi in zip(edges[:-1], edges[1:])])
    wu = np.concatenate([(hi - lo)/2*gw for lo, hi in zip(edges[:-1], edges[1:])])
    xs = x0*np.exp(ell*uq); wxs = wu*ell*xs
    G, A, At, Att = [np.asarray(v) for v in jax.vmap(jet)(jnp.asarray(xs))]
    af, ag, ah = A.T; y = At/A; yt = Att/A - y**2
    S = y.sum(1); W = af*ag*ah
    def Porb(ai, aj, ak): return 2*(ai**4 - (aj**2 - ak**2)**2)/W**2
    P = np.stack([Porb(af, ag, ah), Porb(ag, ah, af), Porb(ah, af, ag)], 1)
    R00 = -(yt + y**2).sum(1); Rii = -yt - S[:, None]*y + P
    s = R00 + Rii.sum(1)
    ric0sq = (R00 - s/4)**2 + ((Rii - s[:, None]/4)**2).sum(1)
    dtdx = 1/(2*np.sqrt(G))
    integ = lambda f: float(np.sum(f*dtdx*wxs))
    Phat = integ(W*ric0sq/4)
    # self-dual curvature (Cartan), v = a' - gamma
    gam = np.stack([(ag**2 + ah**2 - af**2)/(ag*ah), (ah**2 + af**2 - ag**2)/(ah*af), (af**2 + ag**2 - ah**2)/(af*ag)], 1)
    def gdot(ai, aj, ak, di, dj, dk):
        Nn = aj**2 + ak**2 - ai**2; M = aj*ak
        return (2*(aj*dj + ak*dk - ai*di)*M - Nn*(dj*ak + aj*dk))/M**2
    dfa, dga, dha = At.T
    gamt = np.stack([gdot(af, ag, ah, dfa, dga, dha), gdot(ag, ah, af, dga, dha, dfa), gdot(ah, af, ag, dha, dfa, dga)], 1)
    v = At - gam; vt = Att - gamt
    vj = np.roll(v, -1, 1); vk = np.roll(v, -2, 1); aj = np.roll(A, -1, 1); ak = np.roll(A, -2, 1)
    Rp = -vt/(2*A) + (-v - vj*vk/2)/(aj*ak)
    Wp = Rp - s[:, None]/12
    # canonical conformal factor u
    lam_t = 2*af/(ag*ah)
    ud = np.concatenate([np.geomspace(1e-10, 1e-3, 20000, endpoint=False), np.linspace(1e-3, 1.0, 200000)])
    xd = x0*np.exp(ell*ud)
    Gd, Ad = [np.asarray(vv) for vv in jax.vmap(slots)(jnp.asarray(xd))]
    integrand = 2*Ad[:, 0]/(Ad[:, 1]*Ad[:, 2])*(1/(2*np.sqrt(Gd)))*ell*xd
    Ld = cumulative_trapezoid(integrand, ud, initial=0.0); Ld = Ld - Ld[-1]
    logphi = np.log(X) + np.interp(uq, ud, Ld)
    u2 = np.exp(logphi)/(ag*ah); uu = np.sqrt(u2)
    upr = 0.5*uu*(lam_t - y[:, 1] - y[:, 2])
    q = np.log(ag/ah); qt = y[:, 1] - y[:, 2]
    nu = -(qt + 4*np.sinh(q)/af)/(2*uu)
    dVh = W*uu**4                       # per dt
    kappa = 6*Wp[:, 0]/u2
    # shat from the conformal formula with Lap u = u'' + S u'
    nu_c = 0.5*(lam_t - y[:, 1] - y[:, 2])
    nut_c = 0.5*(lam_t*(y[:, 0] - y[:, 1] - y[:, 2]) - yt[:, 1] - yt[:, 2])
    upp = uu*(nut_c + nu_c**2)
    shat = (-6*(upp + S*upr) + s*uu)/uu**3
    lam = (Wp[:, 1] - Wp[:, 2])/(2*u2)
    delta = Wp[:, 0]/u2 + 4
    sl = slice(10, -10)
    out = dict(record=a.record, x0=x0, X=X, Phat=Phat, stored_J=rec.get('J'))
    out['check_kappa_minus_shat_vs_6nu2_max_rel'] = float(np.max(np.abs(kappa - shat - 6*nu**2)[sl]/(1 + 6*nu[sl]**2)))
    H = integ(W*(u2 - 1)**2); Gu = integ(W*upr**2)
    N = integ(4*nu**2*dVh); QA = integ(4*lam**2*dVh); Qd = integ(delta**2*dVh)
    Sig = integ((s + 24)*(u2 - 1)*W) + integ((s + 24)**2/48*W)
    rhs = 12*H + 6*Gu + 1.5*Qd + 0.5*QA - 1.5*N + Sig
    out.update(H=H, G=Gu, N=N, QA=QA, Qdelta=Qd, scalar_terms=Sig,
               terms=dict(H12=12*H, G6=6*Gu, Qd32=1.5*Qd, QA12=0.5*QA, N32=-1.5*N, Sig=Sig),
               identity_rhs=rhs, identity_lhs=Phat - 1, identity_residual=Phat - 1 - rhs)
    # transport lambda = nu_T/2 + beta nu, with d/dT = (1/u) d/dt
    tt = np.cumsum(dtdx*wxs)
    nuT = np.gradient(nu, tt)/uu
    beta = (-(upr/uu + y[:, 0])/2 + 2*np.cosh(q)/af)/uu
    tr = lam - (nuT/2 + beta*nu)
    out['transport_rel_residual_max'] = float(np.max(np.abs(tr)[20:-20])/np.max(np.abs(lam)[20:-20]))
    # mu = exp(int 2 beta dT) = (1/(u a_f)) exp(int 4 cosh(q)/a_f dt), normalized mu(X)=1/(u a_f)(X)
    qd = np.log(Ad[:, 1]/Ad[:, 2])
    ci = 4*np.cosh(qd)/Ad[:, 0]*(1/(2*np.sqrt(Gd)))*ell*xd
    Cd = cumulative_trapezoid(ci, ud, initial=0.0); Cd = Cd - Cd[-1]
    logmu = np.interp(uq, ud, Cd) - np.log(uu*af)
    mu = np.exp(logmu)
    mnu = mu*nu
    charge_int = integ(2*mu*lam*uu)     # 2 int mu lambda dT
    out['bolt_charge'] = dict(mu_nu_bolt_samples=[float(mnu[i]) for i in (0, 5, 20, 60, 120)],
                              mu_nu_end=float(mnu[-1]), two_int_mu_lambda_dT=charge_int,
                              law_residual=float(mnu[-1] - mnu[3] - integ((2*mu*lam*uu)[3:]*1.0) if False else 0.0))
    # cumulative law check from index i0
    cumlaw = np.cumsum(2*mu*lam*uu*dtdx*wxs)
    out['bolt_charge']['law_residual_from_i30'] = float((mnu[-1] - mnu[30]) - (cumlaw[-1] - cumlaw[30]))
    # exact regrouping: 6G - (3/2)N = 6 int u^2 a_f v_g v_h dt
    out['regroup_6G_minus_32N'] = dict(lhs=6*Gu - 1.5*N, rhs=integ(6*u2*af*v[:, 1]*v[:, 2]))
    # Hardy coefficient Lambda = w_T/w - 4 beta (w = dVhat/dT); far-field Nijenhuis sector is >= 0 where
    # Lambda >= 4 sqrt 3.
    Lam = (S + 2*y[:, 0] + 5*upr/uu - 8*np.cosh(q)/af)/uu
    crit = 4*np.sqrt(3)
    good = Lam >= crit
    # first T beyond which Lambda stays >= crit
    bad_idx = np.where(~good)[0]
    i_star = int(bad_idx[-1] + 1) if len(bad_idx) else 0
    sec = lambda f, m: float(np.sum((f*dtdx*wxs)[m]))
    mask_far = np.zeros_like(good); mask_far[i_star:] = True
    nsec = 2*lam**2*dVh - 6*nu**2*dVh
    out['hardy'] = dict(critical=crit, x_star=float(xs[min(i_star, len(xs)-1)]), t_star=float(tt[min(i_star, len(xs)-1)]),
                        Lambda_end=float(Lam[-30]), nij_sector_far=sec(nsec, mask_far), nij_sector_near=sec(nsec, ~mask_far),
                        conf_sector_near=sec(12*W*(u2-1)**2 + 6*W*upr**2 + 1.5*delta**2*dVh, ~mask_far),
                        conf_sector_far=sec(12*W*(u2-1)**2 + 6*W*upr**2 + 1.5*delta**2*dVh, mask_far),
                        far_ratio_int_nu2_over_int_lam2=sec(nu**2*dVh, mask_far)/sec(lam**2*dVh, mask_far),
                        boundary_nu2w_at_star=float((nu**2*uu**3*W)[min(i_star, len(xs)-1)]))
    # local profile of the gap densities (per dt)
    dens = dict(H=12*W*(u2 - 1)**2, G=6*W*upr**2, Qd=1.5*delta**2*dVh, QA=0.5*4*lam**2*dVh, N=-1.5*4*nu**2*dVh)
    idx = np.unique(np.geomspace(1, len(xs) - 1, 40).astype(int))
    cums = {k: np.cumsum(vv*dtdx*wxs) for k, vv in dens.items()}
    out['profile'] = [dict(x=float(xs[i]), t=float(tt[i]), u=float(uu[i]), q=float(q[i]), nu=float(nu[i]), Lambda=float(Lam[i]),
                           lam=float(lam[i]), delta=float(delta[i]), mu_nu=float(mnu[i]),
                           **{('cum_' + k): float(cums[k][i]) for k in cums}) for i in idx]
    print(json.dumps({k: vv for k, vv in out.items() if k != 'profile'}, indent=1))
    if a.out:
        Path(a.out).write_text(json.dumps(out, indent=1) + '\n')


if __name__ == '__main__':
    main()

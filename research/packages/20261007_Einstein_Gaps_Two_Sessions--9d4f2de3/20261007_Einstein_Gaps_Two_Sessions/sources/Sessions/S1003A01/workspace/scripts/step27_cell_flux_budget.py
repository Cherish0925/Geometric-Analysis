"""Step 27: evaluate the bolt-anchored flux laws and channel budgets on perpendicular cells.

Input: a cell record (JSON with x0, X, deg, z) in the repaired DualCell parametrization.
Metric (x-gauge): g = dx^2/(4G) + F s1^2 + x s2^2 + x e^w s3^2, so d/dt = 2 sqrt(G) d/dx.
Slots: h (collapsing at bolt) = s1, g = s2, f (CH fibre) = s3.
Independent Ricci (diagonal Bianchi IX, d s_i = 2 s_j^s_k) is recomputed here.

Reports (all in P/(8 pi^2) units, dt-integrals over the core [bolt, X]; beyond X the
metric is exact CH where C=E=D=0, J=0, W beta' = X^2):
  * channel energies P_C=int W C^2/3, P_E=int W E^2/6, P_D=int W D^2/8 and their sum vs P;
  * flux laws  J(X)-J(bolt)=int W(Pi_q-D),  (W beta')(X)-(W beta')(bolt)=int W(Pi_b-E);
  * zeroth-order drift budgets int W Pi_q - b^2 (=int W D) and int W Pi_b + b^2/2 - X^2 (=int W E);
  * coupled Bianchi residual for (W^{4/3}C)';
  * flux lower bounds (int W D phi)^2/(8 int W phi^2) for phi in small bases;
  * volume deficit V_CH(R)-V_cell with sinh^2 R = X  (V in int W dt units).
Usage: python step27_cell_flux_budget.py RECORD [--n 4000] [--out OUT.json]
"""
import argparse, json, sys
from pathlib import Path
import numpy as np
import jax, jax.numpy as jnp
jax.config.update('jax_enable_x64', True)
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from perp_dual_cost import make_cell, load_record, seed_vector  # noqa: E402


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
        At = 2*jnp.sqrt(G)*Ax
        Att = 4*G*Axx + 2*Gx*Ax
        return G, A, At, Att

    # Gauss-Legendre panels in u=log(x/x0)/ell, geometric near the removable bolt singularity
    ell = np.log(X/x0)
    edges = np.concatenate([[0.0], np.geomspace(1e-8, 1e-2, 24), np.linspace(1e-2, 1.0, max(8, a.n//24))[1:]])
    gx, gw = np.polynomial.legendre.leggauss(16)
    u = np.concatenate([(lo + hi)/2 + (hi - lo)/2*gx for lo, hi in zip(edges[:-1], edges[1:])])
    wu = np.concatenate([(hi - lo)/2*gw for lo, hi in zip(edges[:-1], edges[1:])])
    xs = x0*np.exp(ell*u); wxs = wu*ell*xs
    G, A, At, Att = [np.asarray(v) for v in jax.vmap(jet)(jnp.asarray(xs))]
    af, ag, ah = A.T; y = At/A; yt = Att/A - y**2
    S = y.sum(1); W = af*ag*ah
    def Porb(ai, aj, ak): return 2*(ai**4 - (aj**2 - ak**2)**2)/W**2
    P = np.stack([Porb(af, ag, ah), Porb(ag, ah, af), Porb(ah, af, ag)], 1)
    R00 = -(yt + y**2).sum(1)
    Rii = -yt - S[:, None]*y + P
    s = R00 + Rii.sum(1)
    C = R00 - s/4; E = Rii[:, 0] - (Rii[:, 1] + Rii[:, 2])/2; D = Rii[:, 1] - Rii[:, 2]
    Piq = P[:, 1] - P[:, 2]; Pib = P[:, 0] - (P[:, 1] + P[:, 2])/2
    qp = y[:, 1] - y[:, 2]; bp = y[:, 0] - (y[:, 1] + y[:, 2])/2
    dtdx = 1/(2*np.sqrt(G))
    def integ(f):  # dt integral, Gauss-Legendre in u
        return float(np.sum(f*dtdx*wxs))
    def cum(f):
        return np.cumsum(f*dtdx*wxs)
    b2 = x0
    PC, PE, PD = integ(W*C**2/3), integ(W*E**2/6), integ(W*D**2/8)
    ric0sq = (R00 - s/4)**2 + ((Rii - s[:, None]/4)**2).sum(1)
    Pdirect = integ(W*ric0sq/4)
    Jq = W*qp; Jb = W*bp
    V = integ(W)
    # volume excess relative to CH at equal x (CH: W dt/dx = x/2), no cancellation
    vol_excess = float(np.sum((W*dtdx - xs/2)*wxs)) - x0**2/4
    out = dict(record=a.record, x0=x0, X=X, b2=b2,
               P_direct=Pdirect, P_channels=PC + PE + PD, P_C=PC, P_E=PE, P_D=PD,
               stored_J=rec.get('J'), s_minmax=[float(s.min()), float(s.max())],
               Jq_bolt=float(Jq[0]), Jb_bolt=float(Jb[0]), Jq_end=float(Jq[-1]), Jb_end=float(Jb[-1]),
               expected=dict(Jq_bolt=-b2, Jb_bolt=-b2/2, Jq_end=0.0, Jb_end=X**2))
    out['flux_q_residual'] = float(Jq[-1] - Jq[0] - integ(W*(Piq - D)))
    out['flux_b_residual'] = float(Jb[-1] - Jb[0] - integ(W*(Pib - E)))
    out['int_W_D'] = integ(W*D); out['int_W_Piq_minus_b2'] = integ(W*Piq) - b2
    out['int_W_E'] = integ(W*E); out['int_W_Pib_plus_b2half_minus_X2'] = integ(W*Pib) + b2/2 - X**2
    out['int_W_Piq'] = integ(W*Piq); out['int_W_Pib'] = integ(W*Pib)
    # coupled Bianchi residual (W^{4/3}C)' - W^{4/3}[(2/3)b'E + q'D/2 + s'/4]
    Phi = W**(4/3)*C
    st = np.gradient(s, xs)/dtdx
    Phit = np.gradient(Phi, xs)/dtdx
    rhs = W**(4/3)*((2/3)*bp*E + qp*D/2 + st/4)
    sl = slice(10, -10)
    out['coupled_bianchi_rel_residual'] = float(np.max(np.abs(Phit - rhs)[sl])/np.max(np.abs(rhs)[sl]))
    out['radial_source_split'] = dict(int_W43_bpE=integ(W**(4/3)*(2/3)*bp*E), int_W43_qpD=integ(W**(4/3)*qp*D/2),
                                      Phi_end=float(Phi[-1]))
    # flux (Cauchy-Schwarz) lower bounds with phi=1 and best phi in span{1, u, u^2,...} weights
    def best_bound(field, coef, basis):
        Bm = np.stack(basis, 1)
        bvec = np.array([integ(W*field*Bm[:, i]) for i in range(Bm.shape[1])])
        Gm = np.array([[integ(W*Bm[:, i]*Bm[:, j]) for j in range(Bm.shape[1])] for i in range(Bm.shape[1])])
        return float(bvec @ np.linalg.solve(Gm, bvec)/coef)
    tt = cum(np.ones_like(xs)); T = tt[-1]
    bases = {k: [(tt/T)**j for j in range(k)] for k in (1, 2, 4, 8)}
    out['flux_bounds_D'] = {k: best_bound(D, 8, bs) for k, bs in bases.items()}
    out['flux_bounds_E'] = {k: best_bound(E, 6, bs) for k, bs in bases.items()}
    out['flux_bounds_C'] = {k: best_bound(C, 3, bs) for k, bs in bases.items()}
    out['V_cell'] = V; out['V_CH'] = X**2/4; out['volume_deficit'] = -vol_excess; out['T_core'] = T
    # Chiral charges b_+ = 2 + v1 v2 v3 - |v|^2 (v=a'-gamma), b_- = |w|^2 - w1 w2 w3 - 2 (w=a'+gamma),
    # gamma_i=(a_j^2+a_k^2-a_i^2)/(a_j a_k).  Pointwise identity (P/(8pi^2) density per dt):
    #   W|Ric0|^2/4 = b_pm' + W|W^pm|^2 + W s^2/48,  so |W^pm|^2 is recovered and must be >= 0.
    gam = np.stack([(ag**2 + ah**2 - af**2)/(ag*ah), (ah**2 + af**2 - ag**2)/(ah*af), (af**2 + ag**2 - ah**2)/(af*ag)], 1)
    def gdot(ai, aj, ak, di, dj, dk):
        N = aj**2 + ak**2 - ai**2; M = aj*ak
        return (2*(aj*dj + ak*dk - ai*di)*M - N*(dj*ak + aj*dk))/M**2
    dfa, dga, dha = At.T
    gamt = np.stack([gdot(af, ag, ah, dfa, dga, dha), gdot(ag, ah, af, dga, dha, dfa), gdot(ah, af, ag, dha, dfa, dga)], 1)
    v = At - gam; w = At + gam; vt = Att - gamt; wt = Att + gamt
    bplus = 2 + v.prod(1) - (v**2).sum(1); bminus = (w**2).sum(1) - w.prod(1) - 2
    def dprod(m, mt):
        return mt[:, 0]*m[:, 1]*m[:, 2] + m[:, 0]*mt[:, 1]*m[:, 2] + m[:, 0]*m[:, 1]*mt[:, 2]
    bpt = dprod(v, vt) - 2*(v*vt).sum(1); bmt = 2*(w*wt).sum(1) - dprod(w, wt)
    dens = W*ric0sq/4; sdens = W*s**2/48
    Wp = (dens - sdens - bpt)/W; Wm = (dens - sdens - bmt)/W
    out['charges'] = dict(bplus_bolt=float(bplus[0]), bminus_bolt=float(bminus[0]), bplus_end=float(bplus[-1]),
                          bminus_end=float(bminus[-1]), expected_end=[2 - 9*X**2, 2 - 3*X**2],
                          bplus_max=float(bplus.max()), bminus_max=float(bminus.max()),
                          min_Wplus_sq=float(Wp[sl].min()), max_Wplus_sq=float(Wp[sl].max()),
                          min_Wminus_sq=float(Wm[sl].min()))
    Sx = integ(W*(s**2/48 - 12))
    depl = integ(24*W - dens + sdens + bpt)
    WmI = integ(dens - sdens - bmt)
    out['weyl_volume_split'] = dict(
        weyl_plus_depletion=depl, int_W_Wminus_sq=WmI, scalar_excess=Sx, volume_excess=vol_excess,
        relative_plus_should_be_P=float(1 + 36*vol_excess - depl + Sx),
        relative_minus_should_be_P=float(-5 + 12*vol_excess + WmI + Sx))
    bp_charge, bm_charge = bplus, bminus
    # Invariant closed self-dual 2-form omega_f = d(phi sigma_f), phi'/phi = 2 a_f/(a_g a_h),
    # normalized to the CH Kahler form on the collar (phi(X)=X=sinh^2 R).  omega = m(e^{0f}+e^{gh}),
    # m = 2 phi/(a_g a_h); CH has m=2.  u = sqrt(m/2) is the almost-Kahler conformal factor
    # (ghat=u^2 g has |omega|=const).  int W u^4 is pinned to V_CH by Stokes; omega vanishes on the bolt.
    lam = 2*af/(ag*ah)
    # accurate antiderivative of lam dt on a dense grid (only zeroth-order slots needed)
    from scipy.integrate import cumulative_trapezoid
    ud = np.concatenate([np.geomspace(1e-10, 1e-3, 20000, endpoint=False), np.linspace(1e-3, 1.0, 200000)])
    xd = x0*np.exp(ell*ud)
    Gd, Ad = [np.asarray(vv) for vv in jax.vmap(slots)(jnp.asarray(xd))]
    lamd = 2*Ad[:, 0]/(Ad[:, 1]*Ad[:, 2])*(1/(2*np.sqrt(Gd)))*ell*xd   # lam dt/du
    Ld = cumulative_trapezoid(lamd, ud, initial=0.0); Ld = Ld - Ld[-1]   # = -int_u^1 lam dt
    logphi = np.log(X) + np.interp(u, ud, Ld)
    m = 2*np.exp(logphi)/(ag*ah); uu = np.sqrt(m/2)
    upr = 0.5*uu*(lam - y[:, 1] - y[:, 2])          # exact: u'/u = (lam - y_g - y_h)/2
    # Self-dual curvature operator, diagonal in (e^{0i}+e^{jk})/sqrt2 (Cartan; normalization fixed by
    # round S^4 -> identity and CH -> diag(-6,0,0)):  R+_ii = -v_i'/(2a_i) + (-v_i - v_j v_k/2)/(a_j a_k)
    vj = np.roll(v, -1, 1); vk = np.roll(v, -2, 1); aj = np.roll(A, -1, 1); ak = np.roll(A, -2, 1)
    Rp = -vt/(2*A) + (-v - vj*vk/2)/(aj*ak)
    Wff = Rp[:, 0] - s/12
    nu = 0.5*(lam - y[:, 1] - y[:, 2])
    lamt = lam*(y[:, 0] - y[:, 1] - y[:, 2])
    nut = 0.5*(lamt - yt[:, 1] - yt[:, 2])
    upp = uu*(nut + nu**2)
    Lap = upp + S*upr
    shat = (-6*Lap + s*uu)/uu**3
    Nhat = 4*Wff/uu**2 - (2/3)*shat           # = s*-s for the almost-Kahler pair (u^2 g, omega_f)
    rel = lambda dens_t, ch_dens_x: float(np.sum((dens_t*dtdx - ch_dens_x)*wxs) + np.sum(0) )
    I_shat = float(np.sum((W*shat*uu**4*dtdx + 24*xs/2)*wxs)) + 6*x0**2      # int shat dVhat - CH
    I_CW = float(np.sum((W*((2/3)*shat*uu**4 + 2*uu**2*Wff)*dtdx + 24*xs/2)*wxs)) + 6*x0**2
    out['self_dual_curvature'] = dict(
        trace_minus_s_over_4_max=float(np.max(np.abs(Rp.sum(1) - s/4)[sl])),
        norm_minus_Wplus_sq_max=float(np.max(np.abs(((Rp - s[:, None]/12)**2).sum(1) - Wp)[sl])),
        Wff_range=[float(Wff[sl].min()), float(Wff[sl].max())],
        int_W_24_minus_normRp=integ(W*(24 - ((Rp - s[:, None]/12)**2).sum(1))))
    # alternative chiral charge with the opposite product sign, b = 2 - |v|^2 - v1 v2 v3
    bpt2 = -dprod(v, vt) - 2*(v*vt).sum(1)
    Wp2 = (dens - sdens - bpt2)/W
    out['self_dual_curvature']['norm_minus_Wplus_sq_alt_max'] = float(np.max(np.abs(((Rp - s[:, None]/12)**2).sum(1) - Wp2)[sl]))
    out['self_dual_curvature']['min_Wplus_sq_alt'] = float(Wp2[sl].min())
    out['almost_kahler_CW'] = dict(I_shat_minus_CH=I_shat, Delta_s_ibp=None,
        I_CW_minus_CH=I_CW, N_total=integ(W*Nhat*uu**4), N_hat_min=float((Nhat*uu**4)[sl].min()),
        N_hat_min_over_bulk=float(Nhat[len(Nhat)//10:-10].min()))
    out['almost_kahler'] = dict(
        u_bolt=float(uu[0]), u_end=float(uu[-1]), pinning_int_W_u4_minus_VCH=float(np.sum((W*uu**4*dtdx - xs/2)*wxs) - x0**2/4),
        int_W_u4_minus_u2=integ(W*(uu**4 - uu**2)), int_W_uprime_sq=integ(W*upr**2),
        int_W_splus24_u2=integ(W*(s + 24)*uu**2),
        Delta_s=integ(W*(24*(uu**4 - uu**2) + 6*upr**2 + (s + 24)*uu**2)))
    out['R_CH_match'] = float(np.arcsinh(np.sqrt(X)))
    # profile summaries
    idx = np.unique(np.geomspace(1, len(xs) - 1, 40).astype(int))
    out['profile'] = [dict(x=float(xs[i]), t=float(tt[i]), af=float(af[i]), ag=float(ag[i]), ah=float(ah[i]),
                           q=float(np.log(ag[i]/ah[i])), Jq=float(Jq[i]), Jb=float(Jb[i]), C=float(C[i]),
                           E=float(E[i]), D=float(D[i]), WPiq=float(W[i]*Piq[i]), WPib=float(W[i]*Pib[i]),
                           cumPC=float(cum(W*C**2/3)[i]), cumPE=float(cum(W*E**2/6)[i]), cumPD=float(cum(W*D**2/8)[i]),
                           bplus=float(bp_charge[i]), bminus=float(bm_charge[i]), Wplus_sq=float(Wp[i]), Wminus_sq=float(Wm[i]),
                           cum_vol_minus_CH=float(cum(W)[i] - xs[i]**2/4),
                           cum_weyl_depl=float(cum(24*W - dens + sdens + bpt)[i]))
                      for i in idx]
    txt = json.dumps(out, indent=1)
    print(json.dumps({k: v for k, v in out.items() if k != 'profile'}, indent=1))
    if a.out:
        Path(a.out).write_text(txt + '\n')


if __name__ == '__main__':
    main()

"""Step 43: Yamabe / Weyl / LeBrun ledger of an exact-CH perpendicular cell.

Input: a diagonal perpendicular cell record (repaired DualCell parametrization, profile scale
Ric_CH=-6g).  The complete metric is the cell on [x0,X] followed by exact CH.

We solve the Yamabe problem  -6 Lap u + s u + 24 u^3 = 0, u -> 1  (s_{u^2 g} = -24), zero flux at
the bolt, and evaluate, *relative to the replaced CH ball* and converted to the Ric=-g scale
(g1 = 6 g, scalar -4) used by A02's Theorem Y and LeBrun's Proposition 4:

    DeltaV   = Vol(hat g_1) - Vol(CH_1)                      (Yamabe volume excess)
    D_W      = int (2/3 - |W+_{hat g_1}|^2) dV_{hat g_1}      (Weyl-energy deficit; CH integrand 0)
    P(hat g) = P(g) - 24 int|grad u|^2 - 3 int (Lap u/u)^2   (exact conformal identity)
    LeB      = (4/9) int (sqrt6 |W+_{hat g_1}| - 2)^2 dV_{hat g_1}
    Psi      = int Psi(W+_{hat g_1}) dV_{hat g_1}, Psi(W)=4/3+2|W|^2-phi(-mu_min W)   (A02 Lemma 48.2)

and checks the exact relative Gauss-Bonnet/signature identity (Y0):
    8 pi^2 - P(hat g) = 4 D_W - 4 DeltaV.
Slacks (8 pi^2 units):  F_LeB = 4 DeltaV - (8pi^2 - P(hat g)) - LeB    (zero-period LeBrun slack)
                         F_Y   = 4 DeltaV - (8pi^2 - P(hat g)) - 2 Psi  (Theorem Y slack).
Conversions: g1=6g; |W|_1 = |W|_g/6 pointwise; dV_1 = 36 dV_g; hat g = u^2 g.
All integrals are floating-point quadratures (trapezoid on a bolt-refined grid).

Usage: python step43_yamabe_lebrun_ledger.py RECORD --out OUT.json [--N 80000] [--ext 1e4]
"""
import argparse
import json
import math
import sys
from pathlib import Path

import jax
import jax.numpy as jnp
import numpy as np
import scipy.sparse as sps
import scipy.sparse.linalg as spl

jax.config.update("jax_enable_x64", True)
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from perp_dual_cost import make_cell, load_record, seed_vector  # noqa: E402


def phi_A02(x):
    r = (6 * x + 14) / 9
    return np.where(x <= 2 / 3, 0.5 * r**3 - 4 / 3, 4 * x)


def cell_curvature(rec, xs):
    x0 = float(rec["x0"]); X = float(rec["X"]); deg = int(rec.get("deg", rec.get("degU", 6)))
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
        return G, A, 2 * jnp.sqrt(G) * Ax, 4 * G * Axx + 2 * Gx * Ax

    G, A, At, Att = [np.asarray(v) for v in jax.jit(jax.vmap(jet))(jnp.asarray(xs))]
    af, ag, ah = A.T
    y = At / A; yt = Att / A - y**2; S = y.sum(1); W = af * ag * ah

    def Porb(ai, aj, ak):
        return 2 * (ai**4 - (aj**2 - ak**2)**2) / W**2
    Porb_all = np.stack([Porb(af, ag, ah), Porb(ag, ah, af), Porb(ah, af, ag)], 1)
    R00 = -(yt + y**2).sum(1)
    Rii = -yt - S[:, None] * y + Porb_all
    scal = R00 + Rii.sum(1)
    gam = np.stack([(ag**2 + ah**2 - af**2) / (ag * ah), (ah**2 + af**2 - ag**2) / (ah * af),
                    (af**2 + ag**2 - ah**2) / (af * ag)], 1)

    def gdot(ai, aj, ak, di, dj, dk):
        num = aj**2 + ak**2 - ai**2; den = aj * ak
        return (2 * (aj * dj + ak * dk - ai * di) * den - num * (dj * ak + aj * dk)) / den**2
    dfa, dga, dha = At.T
    gamt = np.stack([gdot(af, ag, ah, dfa, dga, dha), gdot(ag, ah, af, dga, dha, dfa),
                     gdot(ah, af, ag, dha, dfa, dga)], 1)
    v = At - gam; vt = Att - gamt
    vj = np.roll(v, -1, 1); vk = np.roll(v, -2, 1); aj = np.roll(A, -1, 1); ak = np.roll(A, -2, 1)
    Rp = -vt / (2 * A) + (-v - vj * vk / 2) / (aj * ak)
    Wplus = Rp - scal[:, None] / 12
    Ric = np.concatenate([R00[:, None], Rii], 1)
    return G, W, Ric, scal, Wplus


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("record"); ap.add_argument("--out", required=True)
    ap.add_argument("--N", type=int, default=80000); ap.add_argument("--ext", type=float, default=1e4)
    a = ap.parse_args()
    rec = load_record(a.record)
    x0 = float(rec["x0"]); X = float(rec["X"]); ell = math.log(X / x0)
    # cell grid in uu=log(x/x0)/ell, bolt-refined (x-x0 ~ r^2), exterior log grid
    uu = np.unique(np.concatenate([np.geomspace(1e-12, 1e-3, 3000), np.linspace(1e-3, 1, a.N)]))
    xc = x0 * np.exp(ell * uu)
    xe = X * np.exp(np.linspace(0, math.log(a.ext), a.N // 2))[1:]
    x = np.concatenate([xc, xe]); ic = np.arange(len(x)) < len(xc)
    Gc, Wc, Ricc, sc, Wpc = cell_curvature(rec, xc)
    G = np.concatenate([Gc, xe + xe**2]); Wv = np.concatenate([Wc, np.sqrt(xe**3 * (1 + xe))])
    Ric = np.concatenate([Ricc, -6.0 * np.ones((len(xe), 4))])
    s = Ric.sum(1)
    Wp = np.concatenate([Wpc, np.tile([-4.0, 2.0, 2.0], (len(xe), 1))])
    rho = Wv / (2 * np.sqrt(G))           # dV_g / (2 pi^2 dx)
    q = rho * 4 * G
    n = len(x); xm = np.concatenate([[x0], .5 * (x[1:] + x[:-1]), [x[-1]]])
    qm = np.interp(xm, x, q); qm[0] = 0.0
    hl = np.diff(x); dxc = np.diff(xm)
    cR = np.zeros(n); cL = np.zeros(n); cR[:-1] = qm[1:-1] / hl; cL[1:] = qm[1:-1] / hl
    Lop = sps.diags(1 / (rho * dxc)) @ sps.diags([cL[1:], -(cL + cR), cR[:-1]], [-1, 0, 1], format="csr")
    # Solve for v=u-1 (rows of Lop sum to ~0 with entries up to 1e14 near the bolt; acting on
    # u=1+v would inject roundoff of order entries*eps).  e=s+24 is the source.
    e = s + 24.0
    v = np.zeros(n)
    for it in range(60):
        Fv = -6 * (Lop @ v) + e + (s + 72) * v + 72 * v**2 + 24 * v**3
        Jm = (-6 * Lop + sps.diags(s + 72 + 144 * v + 72 * v**2)).tolil()
        Fv[-1] = v[-1]; Jm[n - 1, :] = 0; Jm[n - 1, n - 1] = 1
        dv = spl.spsolve(Jm.tocsr(), -Fv); v += dv
        dumax = float(np.max(np.abs(dv)))
        if dumax < 1e-15:
            break
    u = 1 + v
    u4m1 = 4 * v + 6 * v**2 + 4 * v**3 + v**4
    Lu_u = (s + 24 * u**2) / 6
    ux = np.gradient(u, x)
    k = np.searchsorted(x, X * a.ext / 100)
    w8 = 2 * math.pi**2 / (8 * math.pi**2)   # integrals of (f rho dx) * 2pi^2, in 8pi^2 units

    nc = int(ic.sum())

    def trap(y, xx):
        return float(np.sum(.5 * (y[1:] + y[:-1]) * np.diff(xx)))

    def I(f, fext=None):
        """Cell segment [x0,X] with integrand f, exterior [X, X ext/100] with fext (default f)."""
        fe = f if fext is None else fext
        yc = (f * rho)[:nc]; ye = (fe * rho)[nc - 1:k]
        return (trap(yc, x[:nc]) + trap(ye, x[nc - 1:k])) * w8

    Pg = I(np.sum((Ric - s[:, None] / 4)**2, 1))
    Jg = I(np.sum((Ric + 6)**2, 1))
    grad = I(24 * 4 * G * ux**2); lap = I(3 * Lu_u**2)
    Phat = Pg - grad - lap
    VCH = (2 * math.pi**2 * X**2 / 4) / (8 * math.pi**2)
    Vcell_hat = I(u**4, u4m1)          # cell hat-volume + exterior hat-volume excess
    dV6 = Vcell_hat - VCH
    Vg_rel = I(np.ones_like(u), np.zeros_like(u)) - VCH   # volume excess of g itself (profile scale)
    dV1 = 36 * dV6
    W2g = np.sum(Wp**2, 1)
    WCH = 24 * VCH
    # D_W = int(24 u^4 - |W+|_g^2) dV_g relative to the CH ball (whose integrand vanishes)
    DW = I(24 * u**4 - W2g, 24 * u4m1)
    DW_check = 24 * dV6 + (WCH - I(W2g, np.zeros_like(u)))
    # Gauss-Bonnet check on g itself: 8pi^2 - P_g = 4 dWeyl - 2*[int s^2/24 - 24 V_CH] (8pi^2 units)
    dWeyl = WCH - I(W2g, np.zeros_like(u))
    S24rel = I(s**2 / 24, np.zeros_like(u)) - 24 * VCH
    GB_g_residual = (1 - Pg) - (4 * dWeyl - 2 * S24rel)
    # Tail-free Yamabe volume: with the integrated Yamabe equation (zero flux at bolt and infinity),
    #   int s^2 dV_g - 576 hatV  (relative) = int [e^2 + 48 e v - 1152 v^3 - 576 v^4] dV_g,
    # whose integrand vanishes where e=0 up to O(v^3).  Hence (8pi^2 units, profile scale)
    Xpos = I((e**2 + 48 * e * v - 1152 * v**3 - 576 * v**4) / 24)
    dV6_id = (S24rel - Xpos) / 24
    Y0_lhs = 1 - Phat
    Y0_rhs = 4 * DW - 4 * dV1
    absW = np.sqrt(W2g)
    LeB = (4 / 9) * I((math.sqrt(6) * absW - 12 * u**2)**2)
    lam = Wp / (6 * u[:, None]**2)                  # W+ eigenvalues of hat g_1 (Ric=-g scale)
    xmin = -lam.min(1); W2_1 = np.sum(lam**2, 1)
    Psi_pt = 4 / 3 + 2 * W2_1 - phi_A02(xmin)
    Psi = I(36 * u**4 * Psi_pt)
    dist2 = I(36 * u**4 * (1.5 * (xmin - 2 / 3)**2 + 2 * (0.5 * (np.sort(lam, 1)[:, 2] - np.sort(lam, 1)[:, 1]))**2))
    amin = np.argmin(Wp[ic], 1)
    aligned = bool(np.all(amin == 0))
    misaligned_x = [float(xc[amin != 0].min()), float(xc[amin != 0].max())] if not aligned else None
    misaligned_vol = I(np.concatenate([(amin != 0).astype(float), np.zeros(n - nc)]), np.zeros_like(u))
    saving = 1 - Phat
    out = dict(record=a.record, x0=x0, X=X, N=n, newton_iter=it, units="8 pi^2, relative to the replaced CH ball, Ric=-g scale for volumes",
               u_bolt=float(u[0]), u_min=float(u.min()), u_max=float(u.max()),
               P_g=Pg, J_g=Jg, P_g_stored=rec.get("P"), J_g_stored=rec.get("J"),
               conformal_grad=grad, conformal_lap=lap, P_hat=Phat,
               DeltaV=dV1, D_W=DW, D_W_alt=DW_check,
               Y0_lhs_saving=Y0_lhs, Y0_rhs=Y0_rhs, Y0_residual=Y0_lhs - Y0_rhs,
               fourDeltaV=4 * dV1, fourD_W=4 * DW,
               LeB_term=LeB, Psi_int=Psi, twoPsi=2 * Psi, dist2_int=dist2,
               F_LeB=4 * dV1 - saving - LeB, F_Y=4 * dV1 - saving - 2 * Psi,
               mu_min_eigvector_is_Kahler_slot_everywhere=aligned, misaligned_x_range=misaligned_x,
               misaligned_volume_profile_8pi2=misaligned_vol, Vg_rel_profile_8pi2=Vg_rel,
               DeltaV_profile_8pi2=dV6, newton_last_du=dumax,
               hatV_cell_excess_profile=I(u4m1, np.zeros_like(u)), hatV_ext_excess_profile=I(np.zeros_like(u), u4m1),
               GB_g_residual=GB_g_residual, dWeyl_rel=dWeyl, S24_rel=S24rel, v_at_X=float(v[nc - 1]),
               Xpos_identity=Xpos, dV6_identity=dV6_id, DeltaV_identity=36 * dV6_id,
               saving_hat_identity=1 - Pg + 2 * Xpos, twoXpos_vs_grad_plus_lap=[2 * Xpos, grad + lap],
               F_LeB_identity=4 * 36 * dV6_id - (1 - Pg + 2 * Xpos) - LeB,
               F_Y_identity=4 * 36 * dV6_id - (1 - Pg + 2 * Xpos) - 2 * Psi,
               int_equation_trap=I(e + (s + 72) * v + 72 * v**2 + 24 * v**3),
               int_e_trap=I(e), int_v_trap=I(v),
               int_equation_fv=float(np.sum((e + (s + 72) * v + 72 * v**2 + 24 * v**3) * rho * dxc)) * w8,
               int_e_fv=float(np.sum(e * rho * dxc)) * w8, int_v_fv=float(np.sum(v * rho * dxc)) * w8,
               Yamabe_ineq_S24_minus_24dV=S24rel - 24 * dV6,
               residual_max=float(np.max(np.abs((-6 * (Lop @ v) + e + (s + 72) * v + 72 * v**2 + 24 * v**3)[1:-1]))),
               Wplus_g_min_max_slot0=[float(Wp[ic, 0].min()), float(Wp[ic, 0].max())])
    Path(a.out).write_text(json.dumps(out, indent=1) + "\n")
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()

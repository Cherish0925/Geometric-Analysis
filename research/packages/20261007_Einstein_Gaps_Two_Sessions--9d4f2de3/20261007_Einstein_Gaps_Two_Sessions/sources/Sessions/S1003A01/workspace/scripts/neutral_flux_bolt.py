"""Neutral-mode transport carried to the smooth bolt (S1003A01 Step 15).

Diagonal Bianchi IX, g = dt^2 + a1^2 s1^2 + a2^2 s2^2 + a3^2 s3^2, d s_i = 2 s_j ^ s_k.
Cell convention (perp_rigorous_enclosure.FrozenCell): a1^2 = F (collapses at the bolt x = x0),
a2^2 = x, a3^2 = x e^w (the CH Kaehler/fast direction), dt = dx/(2 sqrt G).  On exact CH,
F = x, so a1 = a2.  (Peer S1003A02 labels: their a3 = our a1, their a1 = our a3.)

Exact identity (Ric_ii = -(W L_i)'/W + alg_i, L_i = a_i'/a_i, W = a1 a2 a3):
    q = log(a2/a1),   (W q')' = W (V - E),
    V = 4 (a2^2 - a1^2)(a1^2 + a2^2 - a3^2) / W^2,   E = Ric_22 - Ric_11 = Ric°_22 - Ric°_11.
Bolt: a1 = t + O(t^3), a2, a3 = b + O(t^2), b^2 = x0, so W q' -> -b^2.
Green function G(t) = int_t^T dt'/W = b^-2 log(b/t) + gamma + o(1);  Phi_G = q + G W q'.
With exact CH at T (q = q' = 0):
    (I1)  int_0^T W (V - E) dt = b^2,
    (IG)  int_0^T G W (V - E) dt = b^2 gamma.
P/(8 pi^2) = (1/4) int W |Ric°|^2 dt >= (1/8) int W E^2 dt, so for any psi
    (int psi W E)^2 <= 8 (P/8pi^2) int psi^2 W.
This script evaluates all terms, checks I1/IG and the pointwise ODE numerically, and reports the
share of P that the neutral observables span{1, G} can certify.
Usage: python neutral_flux_bolt.py RECORD.json [--n 8001] [--out OUT.json]
"""
import argparse, json, math, sys
from pathlib import Path
import numpy as np
from scipy.integrate import simpson, cumulative_simpson
sys.path.insert(0, str(Path(__file__).resolve().parent))
from flint import arb, acb, ctx
from perp_rigorous_enclosure import FrozenCell


def evaluate(rec, n):
    ctx.prec = 80
    x0 = float(rec.get('x0', .01)); X = float(rec['X'])
    cell = FrozenCell(rec, x0=x0)
    ell = math.log(X/x0)
    v = np.linspace(0.0, 1.0, n)                 # u = v^2 removes the sqrt(t) structure
    ve = v.copy(); ve[0] = 1e-7                  # evaluation point standing in for the v=0 limit
    rows = []
    for vv in ve:
        u = vv*vv
        R, vol, pr = cell.ricci(acb(arb(u)), want_profile=True)
        f = lambda z: float(z.real.mid())
        x = f(pr['x']); y = x0*math.expm1(ell*u)
        F = y*f(pr['FH']); G = y*f(pr['GH']); w = f(pr['w'])
        Rf = [f(r) for r in R]
        rows.append([u, x, y, F, G, w] + Rf)
    A = np.array(rows)
    u, x, y, F, G, w = A[:, :6].T; R = A[:, 6:]
    a1 = np.sqrt(F); a2 = np.sqrt(x); a3 = np.sqrt(x*np.exp(w)); W = a1*a2*a3
    # dt/dv = (dx/du)(du/dv)/(2 sqrt G) = ell x * 2v / (2 sqrt G)
    dtdv = ell*x*ve/np.sqrt(G)
    t = cumulative_simpson(dtdv, x=v, initial=0.0)
    s = R.sum(1); ric0sq = ((R - s[:, None]/4)**2).sum(1)
    E = R[:, 2] - R[:, 1]
    V = 4*(a2**2 - a1**2)*(a1**2 + a2**2 - a3**2)/W**2
    b2 = x0; b = math.sqrt(x0); T = t[-1]
    # Green function with the bolt logarithm removed analytically: 1/W - 1/(b^2 t) = O(t)
    reg = np.empty_like(t); reg[1:] = (1/W[1:] - 1/(b2*t[1:]))*dtdv[1:]; reg[0] = 0.0
    creg = cumulative_simpson(reg, x=v, initial=0.0)
    Ireg = creg[-1]
    with np.errstate(divide='ignore'):
        Gf = (Ireg - creg) + np.log(T/np.where(t > 0, t, np.nan))/b2
    gamma = Ireg + math.log(T/b)/b2
    # neutral field and its flux; q' by differentiation in v (independent of the ODE identity)
    q = 0.5*np.log(x/F)
    qv = np.gradient(q, v, edge_order=2)
    Wqp = W*qv/dtdv
    WV = W*V*dtdv; WE = W*E*dtdv          # densities in dv
    cumVE = cumulative_simpson(WV - WE, x=v, initial=0.0)
    ode_res = Wqp[5:-5] - (-b2 + cumVE[5:-5])
    sl = slice(1, None)
    def I(fv):  # integrate a dv-density that may be singular only at v[0] (log-integrable)
        g = np.array(fv, float); g[0] = 0.0 if not np.isfinite(g[0]) else g[0]
        return float(simpson(g, x=v))
    GWE = np.where(t > 0, Gf, 0)*WE; GWV = np.where(t > 0, Gf, 0)*WV
    G2W = np.where(t > 0, Gf**2, 0)*W*dtdv
    I1V, I1E = I(WV), I(WE); IGV, IGE = I(GWV), I(GWE)
    RG = I(G2W); M1 = I(W*dtdv)
    P = 0.25*I(W*ric0sq*dtdv); PE = 0.125*I(W*E*E*dtdv)
    Jv = 0.25*I(W*((R + 6)**2).sum(1)*dtdv)
    # best bound from psi in span{1, G}: (1/8) m^T M^{-1} m
    m = np.array([I1E, IGE]); Mg = np.array([[M1, I(np.where(t > 0, Gf, 0)*W*dtdv)],
                                            [I(np.where(t > 0, Gf, 0)*W*dtdv), RG]])
    span_bound = float(m @ np.linalg.solve(Mg, m))/8
    # where is the G-observable paid: cumulative of G W E from the bolt
    cGWE = cumulative_simpson(np.nan_to_num(GWE), x=v, initial=0.0)
    cP = cumulative_simpson(0.25*W*ric0sq*dtdv, x=v, initial=0.0)
    probe = {}
    for tt in [0.05, 0.1, 0.2, 0.4, 0.8, 1.2, 1.6, 2.0, 2.5]:
        if tt < T:
            k = int(np.searchsorted(t, tt))
            probe[str(tt)] = dict(q=float(q[k]), Phi_G=float(q[k] + Gf[k]*Wqp[k]), Wqp=float(Wqp[k]),
                                  G=float(Gf[k]), cum_GWE=float(cGWE[k]), cum_P=float(cP[k]),
                                  ratio_a3_a2=float(a3[k]/a2[k]), rho_peer=float(a2[k]/a1[k]))
    return dict(record=rec.get('_path'), x0=x0, X=X, T_geodesic=float(T), n=n,
                P_over_8pi2=P, J_over_8pi2=Jv, P_record=rec.get('P'), J_record=rec.get('J'),
                E_channel_share=PE/P, gamma=float(gamma), b2_gamma=float(b2*gamma),
                I1=dict(int_WV=I1V, int_WE=I1E, VminusE=I1V - I1E, expected=b2),
                IG=dict(int_GWV=IGV, int_GWE=IGE, VminusE=IGV - IGE, expected=float(b2*gamma)),
                compliance_RG=RG, CS_bound_from_G=IGE**2/(8*RG), span1G_bound=span_bound,
                span_bound_share_of_P=span_bound/P,
                ode_residual_max=float(np.max(np.abs(ode_res))), Wqp_bolt=float(Wqp[1]),
                probes=probe)


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('records', nargs='+')
    ap.add_argument('--n', type=int, default=8001); ap.add_argument('--out')
    a = ap.parse_args(); res = []
    for p in a.records:
        rec = json.loads(Path(p).read_text()); rec['_path'] = p
        r = evaluate(rec, a.n); res.append(r)
        print(json.dumps({k: r[k] for k in r if k != 'probes'}, indent=1), flush=True)
    if a.out: Path(a.out).write_text(json.dumps(res, indent=1) + '\n')


if __name__ == '__main__':
    main()

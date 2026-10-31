"""Independent reconstruction and cost check for saturation_optimal_control outputs.

Reads an optimizer JSON (state nodes X=(x,z,p,chi,eta), node controls U, duration T).
1. Re-integrates the scale-free dynamics with the collocation's piecewise-linear controls
   (DOP853, tight tolerance) and reports the mismatch with the recorded nodes.
2. Rebuilds the actual metric dt^2+sum a_i^2 sigma_i^2 (h(0)=0), computes the Ricci
   tensor from the classical diagonal Bianchi-IX formulas
      Ric00=-sum(y_i'+y_i^2), Ric_ii=-y_i'-y_i sum y_j + Pot_i,
   with y_i' obtained by *numerical differentiation* of the reconstructed y_i(t)
   (not from the control formulas), and integrates  hatP = int W |Ric0|^2/4 dt.
3. Checks the C^1 match of the terminal orbit with an exact complex-hyperbolic orbit
   after homothety.
Usage: python saturation_verify.py file.json [...]
"""
import json, math, sys
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp
from scipy.interpolate import CubicSpline


def pots(x, z):
    em4 = np.exp(-4*x/3); ep2 = np.exp(2*x/3); ep8 = np.exp(8*x/3)
    VD = 4*z**-4*(em4-ep2)+4*(ep2*z*z-em4*z**8)
    Vx = 4*z**-4*(ep8-em4)+4*z*z*(em4-ep2)
    VH = (2/3)*z**-4*(ep8-2*ep2+em4)-(4/3)*z*z*(ep2+em4)+(2/3)*em4*z**8
    return VD, Vx, VH


def rhs(s, Y, Uf):
    x, z, p, chi, eta, h, t = Y
    Hb, Eb, Db = Uf(s)
    VD, Vx, VH = pots(x, z)
    xi = chi+eta/2
    r = math.exp(h)
    return [chi, -eta*z/3, p*p-xi*xi/3-eta*eta/4+VH/2-Hb/2,
            -2*p*chi+Vx-Eb+Db/2, -2*p*eta+VD-Db, p, r]


def check(path):
    rec = json.loads(Path(path).read_text())
    X = np.array(rec['X'], float); U = np.array(rec['U'], float); T = float(rec['T'])
    N = X.shape[0]-1; sn = np.linspace(0, T, N+1)
    def Uf(s):
        return [np.interp(s, sn, U[:, i]) for i in range(3)]
    # multiple shooting: integrate each collocation interval from its recorded node
    # (the forward problem is exponentially unstable, so a single shot is meaningless)
    h0, t0 = 0.0, 0.0; node_mis = 0.0; cost = 0.0; scs = []
    for kk in range(N):
        Y0 = list(X[kk])+[h0, t0]
        sol = solve_ivp(rhs, (sn[kk], sn[kk+1]), Y0, args=(Uf,), method='DOP853', rtol=1e-12,
                        atol=1e-13, dense_output=True)
        node_mis = max(node_mis, float(np.max(np.abs(sol.y[:5, -1]-X[kk+1]))))
        s = np.linspace(sn[kk], sn[kk+1], 41)
        x, z, p, chi, eta, h, t = sol.sol(s)
        h0, t0 = float(h[-1]), float(t[-1])
        q = -3*np.log(z); beta = x+q/2; xi = chi+eta/2; r = np.exp(h)
        L = np.vstack([h+2*beta/3, h-beta/3+q/2, h-beta/3-q/2])
        y = np.vstack([p+2*xi/3, p-xi/3+eta/2, p-xi/3-eta/2])/r       # dL/dt
        yp = np.vstack([CubicSpline(t, y[i])(t, 1) for i in range(3)])  # numerical d/dt
        Pot = []
        for i in range(3):
            j, k = (i+1) % 3, (i+2) % 3
            Pot.append(2*np.exp(2*L[i]-2*L[j]-2*L[k])-8*np.exp(-2*L[i])*np.sinh(L[j]-L[k])**2)
        Pot = np.array(Pot)
        R0 = -np.sum(yp+y*y, axis=0)
        Ri = -yp-y*np.sum(y, axis=0)+Pot
        sc = R0+Ri.sum(0); scs.append(sc)
        ric0 = (R0-sc/4)**2+np.sum((Ri-sc/4)**2, axis=0)
        W = np.exp(L.sum(0))
        from scipy.integrate import simpson
        cost += float(simpson(W*ric0/4, x=t))
    sc = np.concatenate(scs)
    # terminal C^1 comparison with an exact CH orbit after homothety
    tch = float(rec['t_ch'])
    a = np.exp(L[:, -1]); ad = a*y[:, -1]
    sh, ch = math.sinh(tch), math.cosh(tch)
    aCH = np.array([sh*ch, sh, sh]); adCH = np.array([ch*ch+sh*sh, ch, ch])
    lam = a[1]/aCH[1]
    term_mis = float(max(np.max(np.abs(a/lam-aCH)), np.max(np.abs(ad-adCH))))
    return {'path': str(path), 'eps': rec['eps'], 'N': N, 'collocation_cost': rec['cost'],
            'reintegrated_cost': cost, 'node_mismatch': node_mis,
            'terminal_CH_C1_mismatch': term_mis, 'min_scalar': float(sc.min()), 'max_scalar': float(sc.max()),
            'collapse_ratio_initial': float(X[0, 1]**3)}


if __name__ == '__main__':
    out = [check(p) for p in sys.argv[1:]]
    print(json.dumps(out, indent=1))

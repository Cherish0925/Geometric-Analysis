"""Hamilton--Jacobi reading of certified perpendicular cells (S1003A01 Step 17).

For each record, along the cell trajectory (bolt -> exact CH collar):
  * kappa = 2 u1 u2 u3/lambda_2  (signed cubic),  Q = sum a_i^2 Phi_{u_i}^2 / W  (>=0),
    so that for the seed S=-c Phi:   -H_S = c(1-c) Q + c kappa,
    and exactly  P/(8pi^2) = c + int (W/4)|z+2c a grad_u Phi/W|^2 + int[c(1-c)Q+c kappa].
  * c_max = sup{c in (0,1]: c(1-c)Q + c kappa >= 0 along this trajectory}
          = min(1, inf_{kappa<0} (1+kappa/Q))   (a NECESSARY condition for the seed
    certificate; a valid certificate needs the inequality on all reachable states).
  * the 'optimal costate' p_u = W z/(2a) (equality case of the square completion) and its
    projection onto -grad Phi; the residual measures the needed state-function correction.
  * the near-N quadratic discriminant: distance of the state from the invariant manifold
    N={u1=u3=0} on which Phi and grad Phi vanish.
Output JSON with integrals and a few profiles.
Usage: python hj_witness_analysis.py RECORD.json [...] --out OUT.json
"""
import argparse, json, sys
from pathlib import Path
import numpy as np
from scipy.integrate import simpson
sys.path.insert(0, str(Path(__file__).resolve().parent))
from joint_dual_calibration import load_profile


def integ(y, v):
    y = np.asarray(y, float).copy(); y[~np.isfinite(y)] = 0.
    return float(simpson(y, x=v))


def analyse(path, n):
    rec, v, t, dtdv, W, z, e, ec, u, H, bspin, a = load_profile(path, n)
    mu = dtdv  # dt = dtdv dv
    lam2 = a[:, 0]*a[:, 2]/a[:, 1]
    kappa = 2*u[:, 0]*u[:, 1]*u[:, 2]/lam2
    gPhi = bspin  # (2H1, u1u3, 2H3)
    Q = np.sum(a**2*gPhi**2, axis=1)/W
    P = integ(mu*W*np.sum(z*z, 1)/4, v)
    out = dict(record=path, x0=float(rec.get('x0', .01)), X=float(rec['X']), P=P)
    # exact identity check at c=1 and c=1/2
    for c in (1.0, 0.5):
        sq = W/4*np.sum((z+2*c*a*gPhi/W[:, None])**2, 1)
        rhs = c+integ(mu*sq, v)+integ(mu*(c*(1-c)*Q+c*kappa), v)
        out[f'identity_residual_c{c}'] = rhs-P
    out['int_kappa'] = integ(mu*kappa, v)
    out['int_Q'] = integ(mu*Q, v)
    neg = kappa < 0
    ratio = np.where(neg & (Q > 0), 1+kappa/np.where(Q > 0, Q, 1), np.inf)
    i = int(np.argmin(ratio))
    out['c_max_along_trajectory'] = float(min(1., ratio[i]))
    out['c_max_location'] = dict(t=float(t[i]), u=u[i].tolist(), a=a[i].tolist(), Q=float(Q[i]), kappa=float(kappa[i]))
    # Optimal costate p_u = W z/(2a); seed direction -grad Phi
    pu = W[:, None]*z/(2*a)
    w = mu*np.sum(a**2/W[:, None]*0+1, 1)  # placeholder weight
    # natural metric for the control: |a p|^2/W  (since W|z|^2/4 = sum a_i^2 p_i^2/W)
    def ip(X, Y): return integ(mu*np.sum(a**2*X*Y, 1)/W, v)
    cbest = ip(pu, -gPhi)/ip(-gPhi, -gPhi)
    resid = pu+cbest*gPhi
    out['costate'] = dict(norm2_pu=ip(pu, pu), c_proj=cbest,
                          share=ip(pu, -gPhi)**2/(ip(pu, pu)*ip(gPhi, gPhi)),
                          residual_norm2=ip(resid, resid))
    # cumulative structure of the seed integrand at c=1
    cum_k = np.concatenate([[0], np.cumsum(0.5*(kappa[1:]*mu[1:]+kappa[:-1]*mu[:-1])*np.diff(v))])
    dist_N = np.sqrt(u[:, 0]**2+u[:, 2]**2)
    sel = np.linspace(0, len(t)-1, 41).astype(int)
    out['profile'] = dict(t=t[sel].tolist(), u1=u[sel, 0].tolist(), u2=u[sel, 1].tolist(), u3=u[sel, 2].tolist(),
                          kappa=kappa[sel].tolist(), Q=Q[sel].tolist(), cum_kappa=cum_k[sel].tolist(),
                          dist_N=dist_N[sel].tolist(), ratio_a2a1=(a[sel, 1]/a[sel, 0]).tolist(),
                          ratio_a3a1=(a[sel, 2]/a[sel, 0]).tolist())
    # where along the path is u2 = 2 (degeneracy of A=[[2,u2],[u2,2]])
    s = np.sign(u[:, 1]-2); k = np.where(np.diff(s) != 0)[0]
    out['u2_equals_2_at_t'] = [float(t[j]) for j in k]
    out['negative_kappa_t_range'] = [float(t[neg].min()), float(t[neg].max())] if neg.any() else None
    return out


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('records', nargs='+'); ap.add_argument('--n', type=int, default=8001)
    ap.add_argument('--out')
    A = ap.parse_args(); res = [analyse(p, A.n) for p in A.records]
    for r in res:
        print(json.dumps({k: r[k] for k in r if k != 'profile'}, indent=1))
    if A.out: Path(A.out).write_text(json.dumps(res, indent=1)+'\n')

if __name__ == '__main__': main()

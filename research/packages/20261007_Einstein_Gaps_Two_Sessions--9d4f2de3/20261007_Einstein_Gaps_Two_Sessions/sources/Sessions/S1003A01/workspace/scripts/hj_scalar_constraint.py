"""Effect of the scalar constraint s=-24 on the Hamilton--Jacobi seed (Step 21).

By the conformal-selection theorem (notes/step21_...md) the diagonal cell problem may be
restricted to metrics with s=-24, where J6=P.  In the control formulation s = Lambda - 2 sum z,
Lambda = -8 sum a_i H_i / W, so admissible controls lie on the state-dependent affine plane
    sum_i z_i = c(a,u) := (Lambda + 24)/2.
Square completion restricted to that plane gives, for any S,
    W|z|^2/4 - dS/dt >= (W/12) (c - sum_i zeta_i)^2 - H_S,   zeta_i = 2 a_i S_{u_i}/W,
so the subsolution condition weakens to  H_S <= sigma_S := (W/12)(c - sum zeta)^2.
For the seed S=-k Phi:  -H_S = k(1-k)Q + k kappa  (Step 17).  This script evaluates along
witness trajectories the old and constrained pointwise margins and the best k.
A trajectory check is only a necessary condition for a certificate.
Usage: python hj_scalar_constraint.py RECORD [...] --out OUT.json
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
    rec, v, t, dtdv, W, z, e, ec, u, H, gPhi, a = load_profile(path, n)
    mu = dtdv
    lam2 = a[:, 0]*a[:, 2]/a[:, 1]
    kappa = 2*u[:, 0]*u[:, 1]*u[:, 2]/lam2
    Q = np.sum(a**2*gPhi**2, axis=1)/W
    Hs = np.stack([u[:, 0]+u[:, 1]*u[:, 2]/2, u[:, 1]+u[:, 2]*u[:, 0]/2, u[:, 2]+u[:, 0]*u[:, 1]/2], 1)
    Lam = -8*np.sum(a*Hs, 1)/W
    cpl = (Lam+24)/2
    s_rec = Lam-2*np.sum(z, 1)
    out = dict(record=path, P=integ(mu*W*np.sum(z*z, 1)/4, v),
               s_plus24_rms=float(np.sqrt(integ(mu*W*(s_rec+24)**2, v)/integ(mu*W, v))))
    res = {}
    for k in (1.0, .9, .75, .5, .25, .1):
        zeta = -2*k*a*gPhi/W[:, None]
        sig = W/12*(cpl-np.sum(zeta, 1))**2
        m_old = k*(1-k)*Q+k*kappa
        m_new = m_old+sig
        res[str(k)] = dict(min_old=float(m_old.min()), min_new=float(m_new.min()),
                           t_min_new=float(t[np.argmin(m_new)]),
                           frac_neg_old=float(integ(mu*(m_old < 0), v)/integ(mu, v)),
                           frac_neg_new=float(integ(mu*(m_new < 0), v)/integ(mu, v)),
                           int_neg_old=integ(mu*np.minimum(m_old, 0), v), int_neg_new=integ(mu*np.minimum(m_new, 0), v),
                           int_sigma=integ(mu*sig, v))
    out['seed'] = res
    return out


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('records', nargs='+'); ap.add_argument('--n', type=int, default=8001)
    ap.add_argument('--out'); A = ap.parse_args()
    res = [analyse(p, A.n) for p in A.records]
    print(json.dumps(res, indent=1))
    if A.out: Path(A.out).write_text(json.dumps(res, indent=1)+'\n')


if __name__ == '__main__': main()

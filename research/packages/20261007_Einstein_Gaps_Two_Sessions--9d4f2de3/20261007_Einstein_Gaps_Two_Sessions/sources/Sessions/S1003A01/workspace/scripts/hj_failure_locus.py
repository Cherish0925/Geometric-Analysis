"""Where does the relative Chern--Simons calibration Phi lose pointwise control? (Step 17)

Along a stored cell, with xi=(u1,u3), v_pm=(u1 pm u3)/sqrt2 and the transverse CS Hessian
Phi = (1+u2/2) v_+^2 + (1-u2/2) v_-^2 + O(...) exactly (Phi=u1^2+u3^2+u1u2u3), report:
  * region F0 = {Q + kappa < 0}: no c in (0,1] gives H_{-c Phi}<=0 there;
  * u2 range on F0, the v_- fraction |v_-|^2/|xi|^2, distance |xi| to the Kahler manifold N;
  * share of the negative cubic integral int kappa_- coming from F0 and from |u2-2|<0.5.
"""
import sys, json
from pathlib import Path
import numpy as np
from scipy.integrate import simpson
sys.path.insert(0, str(Path(__file__).resolve().parent))
from joint_dual_calibration import load_profile

res = []
for p in sys.argv[1:]:
    rec, v, t, dtdv, W, z, e, ec, u, H, bs, a = load_profile(p, 8001)
    lam2 = a[:, 0]*a[:, 2]/a[:, 1]
    kap = 2*u[:, 0]*u[:, 1]*u[:, 2]/lam2
    Q = np.sum(a**2*bs**2, 1)/W
    vp = (u[:, 0]+u[:, 2])/np.sqrt(2); vm = (u[:, 0]-u[:, 2])/np.sqrt(2)
    xi2 = vp**2+vm**2
    F0 = (Q+kap < 0)
    kneg = np.minimum(kap, 0)
    I = lambda y: float(simpson(np.where(np.isfinite(y), y, 0)*dtdv, x=v))
    near2 = np.abs(u[:, 1]-2) < 0.5
    out = dict(record=p, x0=rec.get('x0'), X=rec['X'],
               int_kappa_neg=I(kneg), int_kappa_pos=I(np.maximum(kap, 0)),
               share_kneg_in_F0=I(kneg*F0)/I(kneg), share_kneg_u2near2=I(kneg*near2)/I(kneg),
               F0_t=[float(t[F0].min()), float(t[F0].max())] if F0.any() else None,
               F0_u2=[float(u[F0, 1].min()), float(u[F0, 1].max())] if F0.any() else None,
               F0_vminus_fraction_median=float(np.median((vm**2/np.maximum(xi2, 1e-300))[F0])) if F0.any() else None,
               F0_dist_N_max=float(np.sqrt(xi2[F0]).max()) if F0.any() else None,
               int_Q_plus_kappa_neg_part=I(np.minimum(Q+kap, 0)))
    res.append(out); print(json.dumps(out, indent=1))
Path(__file__).resolve().parent.parent.joinpath('data/hj/cs_hessian_failure.json').write_text(json.dumps(res, indent=1)+'\n')

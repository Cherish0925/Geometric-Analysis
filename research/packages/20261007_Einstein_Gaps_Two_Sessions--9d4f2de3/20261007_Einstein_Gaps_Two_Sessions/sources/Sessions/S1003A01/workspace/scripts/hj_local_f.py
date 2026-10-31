"""Local calibration coefficient f(t) suggested by the witness costate (Step 17).

Equality in the square completion requires z_i = 2 a_i S_{u_i}/W.  For S=-f Phi near the
witness this gives the pointwise least-squares coefficient
    f(t) = sum_i a_i^2 p_i (-Phi_{u_i}) / sum_i a_i^2 Phi_{u_i}^2,   p_i = W z_i/(2 a_i)
(weights a_i^2/W are the control metric).  Also reports Phi(t) and the share of P paid
before each t, so the decrease of f can be compared with where Phi and the cost live.
Output: data/hj/local_f_<tag>.csv
"""
import sys
from pathlib import Path
import numpy as np
from scipy.integrate import cumulative_simpson
sys.path.insert(0, str(Path(__file__).resolve().parent))
from joint_dual_calibration import load_profile

for p in sys.argv[1:]:
    rec, v, t, dtdv, W, z, e, ec, u, H, gP, a = load_profile(p, 8001)
    pu = W[:, None]*z/(2*a)
    wts = a**2/W[:, None]
    f = np.sum(wts*pu*(-gP), 1)/np.maximum(np.sum(wts*gP**2, 1), 1e-300)
    coh = np.sum(wts*pu*(-gP), 1)/np.sqrt(np.maximum(np.sum(wts*gP**2, 1)*np.sum(wts*pu**2, 1), 1e-300))
    Phi = u[:, 0]**2+u[:, 2]**2+u[:, 0]*u[:, 1]*u[:, 2]
    dens = W*np.sum(z*z, 1)/4
    cumP = cumulative_simpson(np.nan_to_num(dens*dtdv), x=v, initial=0.)
    tag = Path(p).stem
    out = Path(__file__).resolve().parent.parent/'data/hj'/f'local_f_{tag}.csv'
    sel = np.unique(np.concatenate([np.linspace(0, len(t)-1, 400).astype(int)]))
    np.savetxt(out, np.column_stack([t, f, coh, Phi, u[:, 1], cumP])[sel], delimiter=',',
               header='t,f_local,cosine,Phi,u2,cumP', comments='')
    for tt in (0.02, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.2, 1.5, 2.0):
        i = np.searchsorted(t, tt)
        print(tag, f't={t[i]:.2f} f={f[i]:.4f} cos={coh[i]:.4f} Phi={Phi[i]:.4f} u2={u[i,1]:.3f} cumP={cumP[i]:.4f}')

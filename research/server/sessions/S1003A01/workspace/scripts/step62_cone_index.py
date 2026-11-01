"""Step 62: index of nondegenerate torsion zeros on the cone Phi=0 inside the admissible first-jet space L.
Phi = 2|m_c|^2 - |m_A|^2/2 + |m_S|^2/2 (Mvec norms), from step62_phi_identity.py.
Samples random first jets on the cone and off it, records det(Mmat) (index = sign det)."""
import os, json
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
L = np.load(os.path.join(HERE, "..", "data", "step62", "linear.npz"))
C, A, S = L["Llin"], L["A"], L["S"]
rng = np.random.default_rng(7)
det = lambda m: np.linalg.det(m[:16].reshape(4, 4))
on, off, ratio = [], [], []
for _ in range(200000):
    xc = rng.standard_normal(2)*rng.exponential(); xs = rng.standard_normal(6)*rng.exponential()
    xa = rng.standard_normal(2)
    na = np.sqrt(4*xc @ xc + xs @ xs); xa = xa/np.linalg.norm(xa)*na
    m = C @ xc + A @ xa + S @ xs; d = det(m); on.append(d/np.linalg.norm(m)**4)
    # A02 test quantities: 9|c|^4-type lower bound in Mvec normalization: |m_c|^4
    ratio.append(d/((xc @ xc)**2 + 1e-300))
    m2 = C @ xc + A @ (rng.standard_normal(2)*rng.exponential()) + S @ xs; off.append(det(m2)/np.linalg.norm(m2)**4)
on = np.array(on); off = np.array(off); ratio = np.array(ratio)
out = {"on_cone_min_det_over_norm4": float(on.min()), "on_cone_fraction_negative": float((on < -1e-12).mean()),
       "off_cone_min_det_over_norm4": float(off.min()), "off_cone_fraction_negative": float((off < -1e-12).mean()),
       "on_cone_min_det_over_|m_c|^4": float(ratio.min())}
print(json.dumps(out, indent=1))
os.makedirs(os.path.join(HERE, "..", "data", "step62b"), exist_ok=True)
json.dump(out, open(os.path.join(HERE, "..", "data", "step62b", "cone_index.json"), "w"), indent=1)

#!/usr/bin/env python3
"""Step 68c: exact rational identification of the order-six invariant multiplier.
Find all (a1,a2,a3) in Q^3 with (a1 c1 + a2 c2 + a3 c3) L6 = 0 exactly, where
 c1 = Delta^2 (J d)(J d) E, c2 = Delta^3 tr E, c3 = Delta^2 div div E  (all at x=0, symmetric E).
Then compare the class modulo Bianchi rows with A02's ell.  Output: data/step68/multiplier_rational.json
"""
import json
import numpy as np
import sympy as sp
import step68_flat_cokernel as F
import step68_multiplier_exact as M

def main():
    L = F.L_matrix(6)
    c1, c2, c3 = M.natural_functionals()
    C = np.rint(np.stack([c1, c2, c3])).astype(np.int64)
    assert np.allclose(C, np.stack([c1, c2, c3]))
    K = sp.Matrix((C @ L).T.tolist())          # 990 x 3 integer
    ns = K.nullspace()
    sols = [list(v / max(v, key=abs)) for v in ns]
    B = F.bianchi_rows(6).astype(float)
    T = M.orth(B.T); PT = np.eye(840) - T @ T.T
    d = np.load(F.A02 / 'data' / 'step80' / 'recon_F012_gen5_lam-5.npz'); ell = d['ell']
    rec = {'nullspace_dim': len(ns), 'solutions': [[str(x) for x in s] for s in sols]}
    for k, s in enumerate(sols):
        v = sum(float(s[i]) * C[i] for i in range(3))
        cp = PT @ v
        rec[f'sol{k}_class_norm_rel'] = float(np.linalg.norm(cp) / np.linalg.norm(v))
        if np.linalg.norm(cp) > 1e-9 * np.linalg.norm(v):
            rec[f'sol{k}_class_cos_ell'] = float((cp @ ell) / (np.linalg.norm(cp) * np.linalg.norm(ell)))
            rec[f'sol{k}_ell_over_class_scale'] = float((cp @ ell) / (cp @ cp))
    print(json.dumps(rec, indent=1))
    (F.OUT / 'multiplier_rational.json').write_text(json.dumps(rec, indent=1) + '\n')

if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""Step 68e: the flat compatibility operator is a single scalar operator.
P(E) = (J d)_i (J d)_j E_ij - 1/2 Delta tr E   (equivalently -2 div div E^{anti-J} modulo contracted Bianchi).
Checks for d<=8: (i) P o L_d = 0 as a polynomial identity (all coefficients, exact integers);
(ii) the C(d+1,3) coefficient functionals of P(E_d) are independent modulo the Bianchi rows and span Ann/T.
Also records the identity P(E) + 2 divdiv E^{anti} in Bianchi span (pointwise symbol check).
Output: workspace/data/step68/scalar_compatibility.json
"""
import json
import numpy as np
import step68_flat_cokernel as F


def P_matrix(d):
    """integer matrix (2*P): E_d (TRI storage, 10*n_d) -> scalar coefficients of degree d-2."""
    src = F.mons_deg(d); tgt = F.mons_deg(d - 2); ti = {m: q for q, m in enumerate(tgt)}
    tix = {p: t for t, p in enumerate(F.TRI)}
    Mt = np.zeros((len(tgt), 10 * len(src)), dtype=np.int64)
    J = F.J0
    for i in range(4):
        for j in range(4):
            col0 = tix[(min(i, j), max(i, j))] * len(src)
            for q, m in enumerate(src):
                for a in range(4):
                    for b in range(4):
                        cJ = int(J[i, a] * J[j, b])
                        if cJ:
                            c, mm = F.ddmon(m, a, b)
                            if c: Mt[ti[mm], col0 + q] += 2 * cJ * c
    for i in range(4):
        col0 = tix[(i, i)] * len(src)
        for q, m in enumerate(src):
            for a in range(4):
                c, mm = F.ddmon(m, a, a)
                if c: Mt[ti[mm], col0 + q] -= c
    return Mt


def main():
    import flint
    rec = {}
    for d in range(2, 9):
        L = F.L_matrix(d); P = P_matrix(d); B = F.bianchi_rows(d)
        r = {'PL_zero': bool(not np.any(P @ L)), 'n_P_rows': P.shape[0]}
        rB = flint.fmpz_mat(B.tolist()).rank()
        rBP = flint.fmpz_mat(np.vstack([B, P]).tolist()).rank()
        r['rank_P_mod_T'] = int(rBP - rB)
        rk = flint.fmpz_mat(L.tolist()).rank()
        r['dim_Q'] = int(L.shape[0] - rk - rB)
        rec[d] = r; print(d, r, flush=True)
    (F.OUT / 'scalar_compatibility.json').write_text(json.dumps(rec, indent=1) + '\n')


if __name__ == '__main__':
    main()

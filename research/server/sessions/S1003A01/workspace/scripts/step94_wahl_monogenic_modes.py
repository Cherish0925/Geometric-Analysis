"""Exact character count for homogeneous flat Dirac modes at a Wahl point.

Conventions follow Step 93/94.  Gamma=1/n^2(1,n-1) acts on
(z1,z2) with weights (1,n-1), and the two positive-spinor fibres of the
extendible twist m=n*j have weights (m,m-n).

A homogeneous polynomial spinor has monomials z1^a z2^b zb1^c zb2^d.
Equivariance means coordinate weight minus fibre weight is zero, because
coefficients transform contragrediently to the fibre.  The compatible flat Dirac operator is represented, up to nonzero constants, by
  D=[[d_z1,d_zb2],[-d_z2,d_zb1]].
It preserves the stated equivariance sectors. We form its exact rational matrix in every degree.
"""
from __future__ import annotations

import json
from pathlib import Path
import sympy as sp


def comps(total: int, parts: int):
    if parts == 1:
        yield (total,)
        return
    for i in range(total + 1):
        for tail in comps(total - i, parts - 1):
            yield (i,) + tail


def wt(exp, n):
    a, b, c, d = exp
    return a + (n - 1) * b - c - (n - 1) * d


def dec(exp, idx):
    e = list(exp)
    if e[idx] == 0:
        return None, 0
    coeff = e[idx]
    e[idx] -= 1
    return tuple(e), coeff


def kernel_data(n: int, j: int, ell: int):
    N = n * n
    m = (n * j) % N
    fw = (m, (m - n) % N)
    inputs = []
    for comp in (0, 1):
        for e in comps(ell, 4):
            if (wt(e, n) - fw[comp]) % N == 0:
                inputs.append((comp, e))

    terms = []
    for col, (comp, e) in enumerate(inputs):
        if comp == 0:
            # row0 d_z1(phi0), row1 -d_z2(phi0)
            for row, idx, sign in ((0, 0, 1), (1, 1, -1)):
                ee, cc = dec(e, idx)
                if cc:
                    terms.append((row, ee, col, sign * cc))
        else:
            # row0 d_zb2(phi1), row1 d_zb1(phi1)
            for row, idx, sign in ((0, 3, 1), (1, 2, 1)):
                ee, cc = dec(e, idx)
                if cc:
                    terms.append((row, ee, col, sign * cc))
    outs = sorted({(row, e) for row, e, _, _ in terms})
    oi = {v: i for i, v in enumerate(outs)}
    M = sp.zeros(len(outs), len(inputs))
    for row, e, col, coeff in terms:
        M[oi[(row, e)], col] += coeff
    rank = M.rank()
    return {
        "ell": ell,
        "input_dim_complex": len(inputs),
        "output_dim_complex": len(outs),
        "rank_complex": rank,
        "kernel_dim_complex": len(inputs) - rank,
    }


def main():
    result = {"convention": "coefficient weight=fibre weight; (m,m-n); D=[[d_z1,d_zb2],[-d_z2,d_zb1]]"}
    for n in range(3, 12, 2):
        nr = {"N": n * n, "forced_twists": {}}
        for j in range(2, n):
            rows = [kernel_data(n, j, ell) for ell in range(0, 16)]
            nz = [r["ell"] for r in rows if r["kernel_dim_complex"] > 0]
            nr["forced_twists"][str(j)] = {
                "first_nonzero_degree": min(nz) if nz else None,
                "rows": rows,
            }
        result[str(n)] = nr
    out = Path(__file__).resolve().parents[1] / "data" / "step94" / "wahl_monogenic_modes.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n")
    print(out)
    for n, nr in result.items():
        if n == "convention":
            continue
        print("n", n, {j: x["first_nonzero_degree"] for j, x in nr["forced_twists"].items()})


if __name__ == "__main__":
    main()

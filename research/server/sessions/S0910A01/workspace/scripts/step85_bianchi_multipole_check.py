#!/usr/bin/env python3
"""
Step 85: Bianchi/harmonic checks for the raw Ozuch H^4 multipoles.

The Strategist warning is correct: trace-free pointwise tensors are not generally
TT tensor fields.  Before using a Green transfer, one must know the actual gauge
compatible source.  This script checks the flat leading H^4 multipole families
that appear in Ozuch's formulas:

    H_row = sum_j (x^T C_{2j} x) C_{2j} / r^6,
    H_col = sum_j (x^T C_{j2} x) C_{j2} / r^6.

It verifies that these raw leading sums are trace-free, divergence-free, and
componentwise harmonic in R^4\{0}.  This is only the leading flat multipole; the
compact-product source S_j^eps still includes cutoff, singular subtraction,
curvature, projection and gauge corrections.
"""
import json
from pathlib import Path
import numpy as np
import sympy as sp

OUT = Path("Sessions/S0910A01/workspace/data/step85_bianchi_multipole_check.json")

# Numeric matrices first.
def wedge(i, j, n=4):
    A = np.zeros((n, n), dtype=int)
    A[i, j] = 1
    A[j, i] = -1
    return A

e12,e13,e14,e23,e24,e34 = wedge(0,1), wedge(0,2), wedge(0,3), wedge(1,2), wedge(1,3), wedge(2,3)
wp = [e12+e34, e13-e24, e14+e23]
wm = [e12-e34, e13+e24, e14-e23]
C = np.array([[wp[a] @ wm[b] for b in range(3)] for a in range(3)], dtype=int)
zeta = 1

# Completeness identity used for divergence cancellation:
# div_b sum_j (x^T A_j x) B_j / r^6 = r^-8 [2 r^2 sum_j (B_j A_j x)_b - 6 sum_j (x^T A_j x)(B_j x)_b]
# Check polynomially by random sampling and by sympy.
def div_scaled_numeric(x, family):
    r2 = float(np.dot(x, x))
    v = np.zeros(4)
    for M in family:
        xMx = float(x @ M @ x)
        v += 2*r2*(M @ M @ x) - 6*xMx*(M @ x)
    return v

rowfam = [C[zeta,j].astype(float) for j in range(3)]
colfam = [C[j,zeta].astype(float) for j in range(3)]

rng = np.random.default_rng(85)
num = {}
for name, fam in [("row_C2j", rowfam), ("col_Cj2", colfam)]:
    vals = []
    for _ in range(10000):
        x = rng.normal(size=4)
        vals.append(float(np.linalg.norm(div_scaled_numeric(x, fam))))
    num[name] = {"max_scaled_divergence_norm_random": max(vals), "mean_scaled_divergence_norm_random": float(np.mean(vals))}

# Sympy exact check.
x = sp.symbols('x0:4')
r2 = sum(xi**2 for xi in x)

def sym_matrix(M):
    return sp.Matrix([[sp.Integer(int(M[i,j])) for j in range(4)] for i in range(4)])

Csp = [[sym_matrix(C[a,b]) for b in range(3)] for a in range(3)]


def exact_checks(fam):
    H = [[sp.Integer(0) for _ in range(4)] for _ in range(4)]
    for M in fam:
        xvec = sp.Matrix(x)
        f = (xvec.T * M * xvec)[0] / r2**3
        for a in range(4):
            for b in range(4):
                H[a][b] += f * M[a,b]
    trace = sp.simplify(sum(H[a][a] for a in range(4)))
    div = [sp.simplify(sum(sp.diff(H[a][b], x[a]) for a in range(4))) for b in range(4)]
    lap = [[sp.simplify(sum(sp.diff(H[a][b], xi, 2) for xi in x)) for b in range(4)] for a in range(4)]
    # Multiply by powers of r2 to make rational simplification robust.
    div_scaled = [sp.simplify(v * r2**4) for v in div]
    lap_scaled = [[sp.simplify(lap[a][b] * r2**5) for b in range(4)] for a in range(4)]
    return {
        "trace_zero": bool(sp.simplify(trace) == 0),
        "divergence_scaled_components": [str(v) for v in div_scaled],
        "divergence_zero": all(sp.simplify(v) == 0 for v in div_scaled),
        "laplacian_scaled_max_nonzero_repr": [str(lap_scaled[a][b]) for a in range(4) for b in range(4) if sp.simplify(lap_scaled[a][b]) != 0][:5],
        "componentwise_harmonic": all(sp.simplify(lap_scaled[a][b]) == 0 for a in range(4) for b in range(4)),
    }

exact = {
    "row_C2j": exact_checks([Csp[zeta][j] for j in range(3)]),
    "col_Cj2": exact_checks([Csp[j][zeta] for j in range(3)]),
}

result = {
    "scope": "flat leading Ozuch H^4 multipole gauge check only",
    "numeric_divergence_check": num,
    "exact_symbolic_check": exact,
    "interpretation": {
        "raw_H4_result": "The row and column H^4 leading sums are trace-free, divergence-free and harmonic on R^4 minus the origin; the flat P_e source is zero away from the singularity.",
        "caution": "This does not mean every invariant compact-product source is TT. The actual S_j^epsilon in c_ij=L_i G_P^perp S_j^epsilon is a distributional/cutoff/gauge-corrected object produced by matching the ALE and orbifold expansions and projecting away global kernel modes.",
        "use_for_next_step": "The flat multipole can be used as the singular model for deriving source moments; the next missing piece is the compact-product Bianchi correction and projection, not a pointwise trace-free assumption."
    }
}
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(result, indent=2))
print(json.dumps(result, indent=2))
print(f"Wrote {OUT}")

#!/usr/bin/env python3
"""Step 83: full Weyl-sector audit of the A1 log-Weyl annulus.

The inherited FND:A1construction uses the fact that the difference K between
an Einstein orbifold normal quadratic jet H0 and the EH particular far-field H1
is a *pure Weyl* quadratic tensor.  Step 68 spot-checked the log-annulus Ricci
formula on one diagonal W+ sample.  Here we verify it on a 10-dimensional basis
of all four-dimensional Weyl tensors (5 self-dual + 5 anti-self-dual sectors).

For each Weyl basis element C, set
    K_ij = -1/3 C_{ikjl} x^k x^l.
We check trace K = div K = Delta K = K(x,.) = 0, D Ric_e(K)=0, and for
eta=r^p, p=1,2,-1,
    D Ric_e(eta K)=-(eta_tt+6 eta_t) K/(2 r^2).
This proves the annular identity sector-by-sector by linearity, including all
five angular components in either chirality; it is not restricted to the U(2)
invariant component.
"""
from __future__ import annotations

import json
from pathlib import Path
import sympy as sp

WORKSPACE = Path(__file__).resolve().parents[1]
OUT = WORKSPACE / "data" / "step83_full_weyl_log_annulus_audit.json"
OUT.parent.mkdir(parents=True, exist_ok=True)

x = sp.symbols('x0:4', real=True)
r2 = sum(xi*xi for xi in x)


def twoform(pairs):
    M = [[sp.Integer(0) for _ in range(4)] for __ in range(4)]
    for i, j, c in pairs:
        M[i][j] += sp.Integer(c)
        M[j][i] -= sp.Integer(c)
    return M

# Self-dual and anti-self-dual bases in orientation 0123.  Common normalization
# cancels in all zero identities; the factor 1/4 below matches the convention of
# the Step 68 script.
SD = [
    twoform([(0,1,1),(2,3,1)]),
    twoform([(0,2,1),(3,1,1)]),
    twoform([(0,3,1),(1,2,1)]),
]
ASD = [
    twoform([(0,1,1),(2,3,-1)]),
    twoform([(0,2,1),(3,1,-1)]),
    twoform([(0,3,1),(1,2,-1)]),
]

# A rational basis of Sym^2_0(R^3): two diagonal and three off-diagonal terms.
STF3 = []
A = sp.zeros(3); A[0,0]=1; A[1,1]=-1; STF3.append(("diag_1_-1_0", A.copy()))
A = sp.zeros(3); A[0,0]=1; A[1,1]=1; A[2,2]=-2; STF3.append(("diag_1_1_-2", A.copy()))
for i,j,name in [(0,1,"off_01"),(0,2,"off_02"),(1,2,"off_12")]:
    A = sp.zeros(3); A[i,j]=1; A[j,i]=1; STF3.append((name, A.copy()))


def make_C(block, A):
    C = [[[[sp.Integer(0) for _l in range(4)] for _k in range(4)] for _j in range(4)] for _i in range(4)]
    for a in range(3):
        for b in range(3):
            if A[a,b] == 0:
                continue
            for i in range(4):
                for j in range(4):
                    Bij = block[a][i][j]
                    if Bij == 0:
                        continue
                    for k in range(4):
                        for l in range(4):
                            Bkl = block[b][k][l]
                            if Bkl:
                                C[i][j][k][l] += sp.Rational(1,4) * A[a,b] * Bij * Bkl
    return C


def K_from_C(C):
    return [[sp.simplify(-sp.Rational(1,3)*sum(C[i][k][j][l]*x[k]*x[l]
                                                for k in range(4) for l in range(4)))
             for j in range(4)] for i in range(4)]


def dRic(h):
    tr = sum(h[a][a] for a in range(4))
    out = [[None for _ in range(4)] for __ in range(4)]
    for i in range(4):
        for j in range(4):
            term = sum(sp.diff(sp.diff(h[k][j], x[k]), x[i]) +
                       sp.diff(sp.diff(h[k][i], x[k]), x[j]) for k in range(4))
            term -= sum(sp.diff(h[i][j], xi, 2) for xi in x)
            term -= sp.diff(sp.diff(tr, x[i]), x[j])
            out[i][j] = sp.factor(sp.simplify(sp.Rational(1,2)*term))
    return out


def all_zero(mat_or_vec):
    if isinstance(mat_or_vec, list) and mat_or_vec and isinstance(mat_or_vec[0], list):
        return all(sp.simplify(v)==0 for row in mat_or_vec for v in row)
    return all(sp.simplify(v)==0 for v in mat_or_vec)

basis_results = []
for chirality, block in [("W_plus", SD), ("W_minus", ASD)]:
    for name, A in STF3:
        C = make_C(block, A)
        K = K_from_C(C)
        traceK = sp.simplify(sum(K[i][i] for i in range(4)))
        divK = [sp.simplify(sum(sp.diff(K[i][j], x[i]) for i in range(4))) for j in range(4)]
        lapK = [[sp.simplify(sum(sp.diff(K[i][j], xi, 2) for xi in x)) for j in range(4)] for i in range(4)]
        radK = [sp.simplify(sum(K[i][j]*x[j] for j in range(4))) for i in range(4)]
        DRK = dRic(K)
        eta_checks = []
        for p in [sp.Integer(1), sp.Integer(2), sp.Integer(-1)]:
            eta = r2**(sp.Rational(p,2))
            h = [[sp.simplify(eta*K[i][j]) for j in range(4)] for i in range(4)]
            DR = dRic(h)
            rhs = [[sp.factor(sp.simplify(-sp.Rational(1,2)/r2*(p**2+6*p)*eta*K[i][j]))
                    for j in range(4)] for i in range(4)]
            diff = [[sp.simplify(DR[i][j]-rhs[i][j]) for j in range(4)] for i in range(4)]
            eta_checks.append({"p": int(p), "identity_holds": bool(all_zero(diff))})
        basis_results.append({
            "chirality": chirality,
            "basis": name,
            "trace_zero": bool(traceK == 0),
            "divergence_zero": bool(all_zero(divK)),
            "laplacian_zero": bool(all_zero(lapK)),
            "radial_gauge_zero": bool(all_zero(radK)),
            "DRic_K_zero": bool(all_zero(DRK)),
            "monomial_eta_checks": eta_checks,
            "nonzero_component_count": sum(1 for i in range(4) for j in range(4) if K[i][j] != 0),
        })

all_ok = all(
    r["trace_zero"] and r["divergence_zero"] and r["laplacian_zero"] and
    r["radial_gauge_zero"] and r["DRic_K_zero"] and
    all(c["identity_holds"] for c in r["monomial_eta_checks"])
    for r in basis_results
)

data = {
    "purpose": "Audit that the log-Weyl annulus formula is valid for every Weyl angular sector, not only the U(2)-invariant sample.",
    "basis": "5 Sym^2_0 modes in W+ and 5 in W- built from self-dual/anti-self-dual two-form bases.",
    "all_basis_checks_pass": bool(all_ok),
    "checked_properties": [
        "trace K = 0",
        "div K = 0",
        "Delta K = 0",
        "K(x,.) = 0 radial gauge",
        "D Ric_e K = 0",
        "D Ric_e(r^p K)=-(p^2+6p) r^p K/(2r^2) for p=1,2,-1"
    ],
    "results": basis_results,
    "interpretation": {
        "pure_weyl": "If H0 and H1 are Einstein-compatible quadratic normal jets with the same Ricci contraction, K=H0-H1 is a Weyl quadratic jet; all such jets are covered by this basis.",
        "chirality": "Both W+ and W- sectors pass. Reversing EH chirality or the product orientation only changes which 5-dimensional block contributes, not the annulus estimate.",
        "A1_quotient": "K is homogeneous of degree 2 and the tensor pullback by -I is even, so every sector descends through the A1 quotient once the local orthonormal marking is fixed.",
        "operator_bound": "For eta=psi(log(r/b)/L), the formula gives O(1/L) operator defect because K=O(r^2) and the background metric on the annulus is uniformly equivalent to e for R small."
    }
}
OUT.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(json.dumps({"output": str(OUT), "all_basis_checks_pass": bool(all_ok), "basis_count": len(basis_results)}, indent=2))

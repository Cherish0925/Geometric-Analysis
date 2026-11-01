#!/usr/bin/env python3
"""Step 68: spot-check the 20260912 log-Weyl interpolation formula.

For a sample constant Weyl tensor C on R^4, set
    K_ij = -1/3 C_{ikjl} x^k x^l.
Then K should be trace-free, divergence-free, harmonic and radial-gauge.  The
manuscript claims that for eta=psi(log(r/b)/L), in n=4,
    D Ric_e(eta K) = -(1/(2 r^2)) (eta_tt + 6 eta_t) K
where eta_t=d eta/d(log r).  Equivalently with eta(t)=psi(t/L), this becomes
-(1/(2r^2))(psi''/L^2+6 psi'/L)K.
"""
from __future__ import annotations

import json
from pathlib import Path
import sympy as sp

WORKSPACE = Path(__file__).resolve().parents[1]
OUT = WORKSPACE / "data" / "step68_log_weyl_operator_check.json"
OUT.parent.mkdir(parents=True, exist_ok=True)

x = sp.symbols('x0:4', real=True)
r2 = sum(xi*xi for xi in x)
t = sp.log(sp.sqrt(r2))
eta = sp.Function('eta')
E = eta(t)

# 2-form basis entries, normalized up to common factors (normalization irrelevant
# for testing the differential identity).  Use an ASD/SD off-diagonal Weyl block
# through a trace-free diagonal W+ operator.
def twoform(pairs):
    M = [[sp.Integer(0) for _ in range(4)] for __ in range(4)]
    for (i,j,c) in pairs:
        M[i][j] += sp.Integer(c)
        M[j][i] -= sp.Integer(c)
    return M

# Self-dual-ish basis in orientation 0123.
B = [
    twoform([(0,1,1),(2,3,1)]),
    twoform([(0,2,1),(3,1,1)]),
    twoform([(0,3,1),(1,2,1)]),
    twoform([(0,1,1),(2,3,-1)]),
    twoform([(0,2,1),(3,1,-1)]),
    twoform([(0,3,1),(1,2,-1)]),
]
# A tracefree W+ component.
eigs = [sp.Integer(2), sp.Integer(-1), sp.Integer(-1), sp.Integer(0), sp.Integer(0), sp.Integer(0)]
C = [[[[sp.Integer(0) for l in range(4)] for k in range(4)] for j in range(4)] for i in range(4)]
for A, lam in enumerate(eigs):
    if lam == 0:
        continue
    for i in range(4):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    C[i][j][k][l] += lam * B[A][i][j] * B[A][k][l] / sp.Integer(4)

# K_ij = -1/3 C_{i k j l} x_k x_l.  The factor is irrelevant.
K = [[sp.simplify(-sp.Rational(1,3)*sum(C[i][k][j][l]*x[k]*x[l] for k in range(4) for l in range(4))) for j in range(4)] for i in range(4)]

traceK = sp.simplify(sum(K[i][i] for i in range(4)))
divK = [sp.simplify(sum(sp.diff(K[i][j], x[i]) for i in range(4))) for j in range(4)]
lapK = [[sp.simplify(sum(sp.diff(K[i][j], xi, 2) for xi in x)) for j in range(4)] for i in range(4)]
radK = [sp.simplify(sum(K[i][j]*x[j] for j in range(4))) for i in range(4)]

def dRic(h):
    tr = sum(h[a][a] for a in range(4))
    out = [[None for _ in range(4)] for __ in range(4)]
    for i in range(4):
        for j in range(4):
            term = sum(sp.diff(sp.diff(h[k][j], x[k]), x[i]) + sp.diff(sp.diff(h[k][i], x[k]), x[j]) for k in range(4))
            term -= sum(sp.diff(h[i][j], xi, 2) for xi in x)
            term -= sp.diff(sp.diff(tr, x[i]), x[j])
            out[i][j] = sp.simplify(sp.Rational(1,2)*term)
    return out

h = [[sp.simplify(E*K[i][j]) for j in range(4)] for i in range(4)]
DR = dRic(h)
# Sympy has trouble representing derivatives with respect to log(r) as an
# independent variable.  We instead compare after substituting concrete
# eta=exp(a t)=r^a for several a values; then eta_t=a eta, eta_tt=a^2 eta and
# the formula is algebraic.
checks = []
for aval in [sp.Integer(1), sp.Integer(2), sp.Integer(-1)]:
    subsE = r2**(sp.Rational(aval,2))  # exp(a log r)=r^a
    DRa = [[sp.simplify(expr.subs(E, subsE).doit()) for expr in row] for row in DR]
    # Direct substitution above may not replace Derivative forms, so recompute h for monomial.
    ha = [[sp.simplify(subsE*K[i][j]) for j in range(4)] for i in range(4)]
    DRa = dRic(ha)
    rhs = [[sp.simplify(-sp.Rational(1,2)/r2*(aval**2 + 6*aval)*subsE*K[i][j]) for j in range(4)] for i in range(4)]
    diff = [[sp.simplify(DRa[i][j]-rhs[i][j]) for j in range(4)] for i in range(4)]
    ok = all(d == 0 for row in diff for d in row)
    checks.append({"a": int(aval), "identity_holds": bool(ok)})

result = {
    "K_trace_zero": bool(traceK == 0),
    "K_divergence_zero": [bool(v == 0) for v in divK],
    "K_laplacian_zero": all(lapK[i][j] == 0 for i in range(4) for j in range(4)),
    "K_radial_gauge_zero": [bool(v == 0) for v in radK],
    "nonzero_components_K": [(i,j,str(K[i][j])) for i in range(4) for j in range(4) if K[i][j] != 0],
    "monomial_eta_checks": checks,
    "formula": "D Ric_e(eta(log r) K)=-(eta_tt+6 eta_t)K/(2 r^2) for this sample K; eta=psi(t/L) gives manuscript eq. FND:logoperator.",
}
OUT.write_text(json.dumps(result, indent=2, ensure_ascii=False))
print(json.dumps({"output": str(OUT), "K_checks": {k: result[k] for k in ["K_trace_zero", "K_divergence_zero", "K_laplacian_zero", "K_radial_gauge_zero"]}, "monomial_eta_checks": checks}, indent=2))

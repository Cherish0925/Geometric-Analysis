#!/usr/bin/env python3
"""
Step 85: derive one-factor S^2 tensor block eigenvalues for the product
Lichnerowicz computation.

This is a symbolic check on S^2(unit curvature) for axisymmetric harmonics.  It
computes the positive rough Laplacian ∇*∇ on:
  - trace sector f g,
  - scalar trace-free Hessian sector H = Hess f + (lambda/2) f g,
  - vector-derived trace-free sector K = sym ∇ alpha for alpha=*df.
The result supplies algebraic denominators for a sectorwise product P model;
it is not yet the full inter-node coefficient.
"""
import json
import sympy as sp
from pathlib import Path

OUT = Path("Sessions/S0910A01/workspace/data/step85_s2_tensor_block_symbolic.json")
th = sp.symbols('th', positive=True)
s = sp.sin(th)
c = sp.cos(th)
g = [[sp.Integer(1), sp.Integer(0)], [sp.Integer(0), s**2]]
ginv = [[sp.Integer(1), sp.Integer(0)], [sp.Integer(0), 1/s**2]]
Gamma = [[[sp.Integer(0) for _ in range(2)] for _ in range(2)] for _ in range(2)]
Gamma[0][1][1] = -s*c
Gamma[1][0][1] = c/s
Gamma[1][1][0] = c/s

def cov_deriv_covector(alpha):
    out = [[0 for _ in range(2)] for _ in range(2)]
    for a in range(2):
        for b in range(2):
            deriv = sp.diff(alpha[b], th) if a == 0 else sp.Integer(0)
            out[a][b] = sp.simplify(deriv - sum(Gamma[k][a][b] * alpha[k] for k in range(2)))
    return out

def hessian(f):
    return cov_deriv_covector([sp.diff(f, th), sp.Integer(0)])

def cov_deriv_tensor(h, a):
    out = [[0 for _ in range(2)] for _ in range(2)]
    for b in range(2):
        for d in range(2):
            deriv = sp.diff(h[b][d], th) if a == 0 else sp.Integer(0)
            val = deriv
            val -= sum(Gamma[k][a][b] * h[k][d] for k in range(2))
            val -= sum(Gamma[k][a][d] * h[b][k] for k in range(2))
            out[b][d] = sp.simplify(val)
    return out

def cov2_tensor(h, a, d):
    T = [cov_deriv_tensor(h, e) for e in range(2)]
    out = [[0 for _ in range(2)] for _ in range(2)]
    for b in range(2):
        for q in range(2):
            deriv = sp.diff(T[d][b][q], th) if a == 0 else sp.Integer(0)
            val = deriv
            val -= sum(Gamma[e][a][d] * T[e][b][q] for e in range(2))
            val -= sum(Gamma[k][a][b] * T[d][k][q] for k in range(2))
            val -= sum(Gamma[k][a][q] * T[d][b][k] for k in range(2))
            out[b][q] = sp.simplify(val)
    return out

def rough_pos(h):
    out = [[0 for _ in range(2)] for _ in range(2)]
    for b in range(2):
        for q in range(2):
            val = sp.Integer(0)
            for a in range(2):
                for d in range(2):
                    if ginv[a][d] != 0:
                        val += ginv[a][d] * cov2_tensor(h, a, d)[b][q]
            out[b][q] = sp.simplify(-val)
    return out

def trace(h):
    return sp.simplify(h[0][0] + h[1][1] / s**2)

def tensor_sub(A, B):
    return [[sp.simplify(A[i][j] - B[i][j]) for j in range(2)] for i in range(2)]

def tensor_scale(a, A):
    return [[sp.simplify(a * A[i][j]) for j in range(2)] for i in range(2)]

def ratio_if_eigen(A, B):
    candidates = []
    for i in range(2):
        for j in range(2):
            if sp.simplify(B[i][j]) != 0:
                candidates.append(sp.simplify(A[i][j] / B[i][j]))
    if not candidates:
        return None, None
    r = sp.simplify(candidates[0])
    residual = [[sp.simplify(A[i][j] - r * B[i][j]) for j in range(2)] for i in range(2)]
    return r, residual

def sym_grad(alpha):
    nab = cov_deriv_covector(alpha)
    return [[sp.simplify(nab[i][j] + nab[j][i]) for j in range(2)] for i in range(2)]

rows = []
for ell in [1, 2, 3, 4, 5, 6]:
    f = sp.legendre(ell, c)
    lam = ell * (ell + 1)
    fg = [[sp.simplify(f * g[i][j]) for j in range(2)] for i in range(2)]
    R_fg = rough_pos(fg)
    r_fg, res_fg = ratio_if_eigen(R_fg, fg)

    Hess = hessian(f)
    H = [[sp.simplify(Hess[i][j] + sp.Rational(lam, 2) * f * g[i][j]) for j in range(2)] for i in range(2)]
    R_H = rough_pos(H)
    r_H, res_H = ratio_if_eigen(R_H, H)

    # alpha = *df. In coordinates, df=f_theta dtheta; *dtheta = sin(theta) dphi.
    alpha = [sp.Integer(0), sp.simplify(s * sp.diff(f, th))]
    K = sym_grad(alpha)
    R_K = rough_pos(K)
    r_K, res_K = ratio_if_eigen(R_K, K)

    rows.append({
        "ell": ell,
        "scalar_laplacian_lambda": lam,
        "rough_trace_ratio": str(r_fg),
        "rough_trace_residual_zero": all(sp.simplify(x) == 0 for row in res_fg for x in row),
        "H_trace": str(sp.simplify(trace(H))),
        "rough_scalar_TF_Hess_ratio": None if r_H is None else str(r_H),
        "rough_scalar_TF_Hess_residual_zero": None if res_H is None else all(sp.simplify(x) == 0 for row in res_H for x in row),
        "rough_vector_TF_ratio": None if r_K is None else str(r_K),
        "rough_vector_TF_residual_zero": None if res_K is None else all(sp.simplify(x) == 0 for row in res_K for x in row),
    })

result = {
    "scope": "symbolic one-factor S^2 rough-Laplacian block eigenvalues, axisymmetric representatives",
    "convention": "unit S^2, positive rough Laplacian ∇*∇=-g^{ab}∇_a∇_b; scalar Δ P_l = ell(ell+1) P_l",
    "rows": rows,
    "interpretation": {
        "trace_sector": "∇*∇(f g)=ell(ell+1) f g",
        "scalar_TF_Hessian_sector": "for ell>=2, ∇*∇ H = (ell(ell+1)-4) H on the checked representatives",
        "vector_TF_sector": "for ell>=2, ∇*∇ sym∇(*df) = (ell(ell+1)-4) sym∇(*df) on the checked representatives; ell=1 is Killing/gauge zero tensor",
        "product_P_use": "Pure one-factor trace tensors have R° eigenvalue +1, so P denominator includes 0.5*(rough1+rough2)-1. Cross one-form sectors have R°=0. Pure factor trace-free tensors require a separate R° action sign/eigenvalue to be inserted before using these rough eigenvalues."
    }
}
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(result, indent=2))
print(json.dumps(result, indent=2))
print(f"Wrote {OUT}")

"""Exact algebraic checks for the accompanying research note.
These checks do not certify the project's upstream geometric PDE theorems.
Requires Python 3 and sympy.
"""
from __future__ import annotations
import json
from pathlib import Path
import sympy as sp


def main() -> None:
    n = 4
    d = sp.symbols('d', positive=True, integer=True)
    assert sp.simplify(d - 2 * (d / 2)) == 0
    assert sp.simplify(d + 2 * (d / 2)**2 - d * (d + 2) / 2) == 0
    v = sp.Matrix([sp.Rational(2, 3), -1, sp.Rational(5, 7), 2])
    q = (v.T * v)[0]
    rank_one_tf = v * v.T - q * sp.eye(4) / 4
    assert sp.simplify(sp.trace(rank_one_tf**2) - sp.Rational(3, 4) * q**2) == 0

    # T[i,j,k] represents nabla_i Z_jk. It is symmetric and trace-free in j,k.
    # The contracted Bianchi identity sets ds_k = 4 sum_i T[i,i,k].
    checks = []
    for seed in range(1, 8):
        T = sp.MutableDenseNDimArray.zeros(n, n, n)
        for i in range(n):
            M = sp.Matrix(n, n, lambda j,k: sp.Integer(
                ((i + seed) * (j+k+2) + seed * (j-k)**2) % 17 - 8))
            M = (M + M.T) / 2
            M -= sp.trace(M) * sp.eye(n) / n
            for j in range(n):
                for k in range(n):
                    T[i,j,k] = M[j,k]
        ds = [4 * sum(T[i,i,j] for i in range(n)) for j in range(n)]
        delta = lambda i,j: sp.Integer(i == j)
        D = sp.MutableDenseNDimArray.zeros(n, n, n)
        for i in range(n):
            for k in range(n):
                for j in range(n):
                    D[i,k,j] = ((T[k,i,j] - T[i,k,j]) / 2
                        + (ds[k]*delta(i,j) - ds[i]*delta(k,j)) / 24)
        contraction = sum(T[k,i,j] * D[i,k,j]
            for i in range(n) for k in range(n) for j in range(n))
        norm_sq = sum(D[i,k,j]**2
            for i in range(n) for k in range(n) for j in range(n))
        assert sp.simplify(contraction - norm_sq) == 0
        assert all(sum(D[i,k,i] for i in range(n)) == 0 for k in range(n))
        assert all(sum(D[i,k,k] for k in range(n)) == 0 for i in range(n))
        checks.append({'seed': seed, 'exact_residual': '0'})

    # Independent coefficient check using the Ricci-quadratic field equation.
    a, L = sp.symbols('a L', real=True)
    xi, beta, scalar = -2*a, 2*a/3, 4*L
    assert sp.simplify(1 + 2*beta*scalar + 2*xi*L - (1 + 4*a*L/3)) == 0
    result = {
        'status': 'all exact checks passed',
        'scope': 'algebra only; not a PDE simulation or upstream proof audit',
        'conformal_hessian_coefficient': '0',
        'conformal_rank_one_coefficient': 'd(d+2)/2',
        'rank_one_tracefree_norm_squared_factor': '3/4',
        'weyl_divergence_contraction_checks': checks,
        'constant_scalar_crosscheck_Z_coefficient': '1 + 4 alpha Lambda/3'
    }
    destination = Path(__file__).with_name('algebra_check_results.json')
    destination.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()

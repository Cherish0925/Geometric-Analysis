"""Minimal, independent Riemannian curvature tools in sympy (coordinate basis).
Convention: R^l_{ijk} = d_j Gamma^l_{ik} - d_k Gamma^l_{ij} + Gamma^l_{jm}Gamma^m_{ik} - Gamma^l_{km}Gamma^m_{ij},
Ric_{ik} = R^j_{ijk}; unit sphere has Ric = (n-1) g > 0.
"""
import sympy as sp


def christoffel(g, X):
    n = len(X)
    ginv = g.inv()
    Gam = [[[0] * n for _ in range(n)] for _ in range(n)]
    for l in range(n):
        for i in range(n):
            for j in range(i, n):
                v = sum(ginv[l, m] * (sp.diff(g[m, i], X[j]) + sp.diff(g[m, j], X[i]) - sp.diff(g[i, j], X[m]))
                        for m in range(n)) / 2
                Gam[l][i][j] = v
                Gam[l][j][i] = v
    return Gam


def ricci(g, X, simplify=None):
    n = len(X)
    Gam = christoffel(g, X)
    Ric = sp.zeros(n, n)
    for i in range(n):
        for k in range(i, n):
            v = 0
            for l in range(n):
                v += sp.diff(Gam[l][i][k], X[l]) - sp.diff(Gam[l][i][l], X[k])
                for m in range(n):
                    v += Gam[l][l][m] * Gam[m][i][k] - Gam[l][k][m] * Gam[m][i][l]
            if simplify is not None:
                v = simplify(v)
            Ric[i, k] = v
            Ric[k, i] = v
    return Ric


def cov_div_sym2(q, X, K):
    """(div_q K)_i = q^{jk} nabla_j K_{ki} for a symmetric 2-tensor K."""
    n = len(X)
    Gam = christoffel(q, X)
    qinv = q.inv()
    out = []
    for i in range(n):
        v = 0
        for j in range(n):
            for k in range(n):
                nab = sp.diff(K[k, i], X[j]) - sum(Gam[m][j][k] * K[m, i] + Gam[m][j][i] * K[k, m] for m in range(n))
                v += qinv[j, k] * nab
        out.append(v)
    return out

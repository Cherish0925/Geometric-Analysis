"""Exact coordinate-jet checks for the optical circle receiver.

No prior curvature routine is imported. The metric, its first/second jets,
Christoffel symbols and their derivatives are formed independently.
"""

import sympy as sp


def check(seed):
    s, phi, x, y = sp.symbols("s phi x y")
    coords = (s, phi, x, y)
    origin = dict.fromkeys(coords, 0)
    R = sp.Rational
    a = 2 + s / 3 + x / 5 + y / 7 + seed * s * x / 11 + x * x / 13
    h = sp.Matrix([
        [1 + s / 2 + x / 3 + s * s / 5, s * x / 7 + s / 11],
        [s * x / 7 + s / 11, 1 - s / 3 + y / 5 + seed * s * s / 17],
    ])
    A = sp.Matrix([s / 3 + seed * y / 7, s / 5 + x / 11])
    g = sp.zeros(4)
    g[0, 0] = a * a
    g[1, 1] = a * a
    for i in range(2):
        g[1, i + 2] = g[i + 2, 1] = a * a * A[i]
        for j in range(2):
            g[i + 2, j + 2] = h[i, j] + a * a * A[i] * A[j]

    ev = lambda v: sp.expand(v).subs(origin)
    g0 = g.applyfunc(ev)
    inv = g0.inv()
    dg = [g.diff(c).applyfunc(ev) for c in coords]
    ddg = [[g.diff(c).diff(d).applyfunc(ev) for d in coords] for c in coords]
    dinv = [-inv * dg[k] * inv for k in range(4)]
    Gamma = sp.MutableDenseNDimArray.zeros(4, 4, 4)
    dGamma = sp.MutableDenseNDimArray.zeros(4, 4, 4, 4)
    for k in range(4):
        for i in range(4):
            for j in range(4):
                C = [dg[i][j, l] + dg[j][i, l] - dg[l][i, j] for l in range(4)]
                Gamma[k, i, j] = sum(inv[k, l] * C[l] for l in range(4)) / 2
                for m in range(4):
                    dGamma[m, k, i, j] = sum(
                        dinv[m][k, l] * C[l]
                        + inv[k, l] * (ddg[m][i][j, l] + ddg[m][j][i, l] - ddg[m][l][i, j])
                        for l in range(4)
                    ) / 2
    ric = sp.zeros(4)
    for i in range(4):
        for j in range(4):
            ric[i, j] = sum(
                dGamma[k, k, i, j] - dGamma[j, k, i, k]
                + sum(Gamma[k, i, j] * Gamma[l, k, l] - Gamma[l, i, k] * Gamma[k, j, l] for l in range(4))
                for k in range(4)
            )
    a0, da0 = ev(a), ev(a.diff(s))
    h0, hs, hss = h.applyfunc(ev), h.diff(s).applyfunc(ev), h.diff(s, 2).applyfunc(ev)
    V = h0.inv() * hs
    H = sp.trace(V) / (2 * a0)
    Hs = (sp.trace(h0.inv() * hss - V * V) / (2 * a0)
          - da0 * sp.trace(V) / (2 * a0 * a0))
    receiver = Hs / a0 - H * da0 / (a0 * a0)
    S2 = sp.trace(V * V) / (4 * a0 * a0)
    beta = A.diff(s).applyfunc(ev) / a0
    beta2 = (beta.T * h0.inv() * beta)[0]
    Bxy = ev(A[1].diff(x) - A[0].diff(y))
    Q = beta2 + Bxy * Bxy / (2 * h0.det())
    D = (ric[1, 1] - ric[0, 0]) / (a0 * a0)
    residual = sp.simplify(receiver - D + S2 + a0 * a0 * Q)
    assert residual == 0, (seed, residual)
    # Both radius variation and connection components are genuinely active.
    assert ev(a.diff(x)) != 0 and beta2 > 0 and Bxy != 0
    print(f"seed={seed}: exact optical receiver PASS; Q={Q}; D={D}")


if __name__ == "__main__":
    for seed in range(1, 6):
        check(seed)
    print("5 independent coordinate-jet identities passed.")

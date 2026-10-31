"""Exact local and end-data checks; no Einstein filling is asserted."""

import sympy as s


def zero(expr):
    return s.factor(s.cancel(expr)) == 0


def boundary_scalar():
    # Arbitrary two-jets of every orbit-shape and connection function.
    r, v, a, b = s.symbols("r v a b", real=True)
    first = s.symbols("r1 v1 a1 b1", real=True)
    second = s.symbols("r2 v2 a2 b2", real=True)
    fields = (r, v, a, b)
    jet = dict(zip(fields, first)) | dict(zip(first, second))

    def d(expr):
        return sum(s.diff(expr, x) * dx for x, dx in jet.items())

    M = s.Matrix([[r + v**2 / r, v / r], [v / r, 1 / r]])
    Minv = s.Matrix([[1 / r, -v / r], [-v / r, r + v**2 / r]])
    A = s.Matrix([a, b])
    MA = M * A
    g = s.Matrix([[1 + (A.T * MA)[0], MA[0], MA[1]],
                  [MA[0], M[0, 0], M[0, 1]],
                  [MA[1], M[1, 0], M[1, 1]]])
    inv = s.Matrix([[1, -a, -b],
                    [-a, Minv[0, 0] + a*a, Minv[0, 1] + a*b],
                    [-b, Minv[1, 0] + a*b, Minv[1, 1] + b*b]])
    assert all(zero(x) for x in g * inv - s.eye(3))
    dg = g.applyfunc(d)

    def partial(i, j, k):
        return dg[j, k] if i == 0 else s.S.Zero

    Gamma = [[[s.factor(sum(inv[k, ell] *
                   (partial(i, j, ell) + partial(j, i, ell)
                    - partial(ell, i, j)) for ell in range(3))/2)
               for j in range(3)] for i in range(3)] for k in range(3)]
    Ric = s.zeros(3)
    for i in range(3):
        for j in range(3):
            expr = d(Gamma[0][i][j])
            if j == 0:
                expr -= sum(d(Gamma[k][i][k]) for k in range(3))
            expr += sum(Gamma[k][i][j] * Gamma[ell][k][ell]
                        - Gamma[ell][i][k] * Gamma[k][j][ell]
                        for k in range(3) for ell in range(3))
            Ric[i, j] = s.factor(expr)
    scalar = s.factor(sum(inv[i, j] * Ric[i, j]
                          for i in range(3) for j in range(3)))
    shape = s.factor(s.trace(Minv * M.applyfunc(d) * Minv * M.applyfunc(d))/2)
    assert zero(shape - (first[0]**2 + first[1]**2)/r**2)
    assert zero(scalar + shape/2)
    assert not zero(scalar + shape)
    print("PASS: full boundary Ricci contraction, arbitrary shape and connection jets")


def global_pairing():
    # z=tanh(t), so sech^3(t) dt = sqrt(1-z^2) dz.
    z = s.symbols("z", real=True)
    c = s.symbols("c", real=True)
    mass = s.integrate(s.sqrt(1-z*z), (z, -1, 1))
    assert mass == s.pi/2
    delta_H = c * mass
    twice_energy = c*c * mass
    assert s.simplify(c * delta_H - twice_energy) == 0
    n = s.symbols("n", integer=True, nonzero=True)
    assert s.simplify(delta_H.subs(c, 2*n/s.pi)) == n
    assert s.simplify(twice_energy.subs(c, 2*n/s.pi)) == 2*n*n/s.pi
    assert s.simplify(delta_H.subs(c, 2/s.pi)) != 0
    print("PASS: finite capacity, positive pairing, nonzero relative integer winding")


def actual_metric():
    # Reuse the exact independent coordinate calculation from round7,
    # and check the different constant-charge profile here directly.
    t = s.symbols("t", real=True)
    c = s.symbols("c", real=True)
    f = s.cosh(t)
    aprime = c/f**3
    q = s.simplify(f**3 * aprime)
    Q = s.simplify(aprime**2/2)
    Ric_tt = -3*s.diff(f, t, 2)/f - Q
    assert q == c
    assert s.diff(q, t) == 0
    assert s.simplify(Ric_tt + 3 + Q) == 0
    assert s.simplify((Ric_tt + 3).subs({c: 1, t: 0})) == -s.Rational(1, 2)
    primitive = c*(s.sech(t)*s.tanh(t) + s.atan(s.sinh(t)))/2
    assert s.simplify(s.diff(primitive, t)-aprime) == 0
    print("PASS: complete constant-charge profile has a nonzero diagonal Einstein residual")


if __name__ == "__main__":
    boundary_scalar()
    global_pairing()
    actual_metric()
    print("Analytic end convergence, OT nonexistence and Yamabe theorem are in the notes.")

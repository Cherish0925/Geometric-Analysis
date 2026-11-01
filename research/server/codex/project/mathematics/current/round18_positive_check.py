"""Finite algebra for round18_positive.md; no PDE/classification certification."""

import sympy as sp


def verify():
    a, b, x = sp.symbols("a b x", real=True)
    c = -a - b
    tr2 = a * a + b * b + c * c
    det = a * b * c
    disc = sp.expand(tr2**3 / 2 - 27 * det**2)
    vandermonde = (a - b) ** 2 * (b - c) ** 2 * (c - a) ** 2
    assert sp.expand(disc - vandermonde) == 0
    assert sp.discriminant(x**3 - tr2 * x / 2 - det, x) == disc
    assert sp.simplify(disc.subs(b, a)) == 0
    assert disc.subs({a: 1, b: 0}) == 4
    print("PASS 1: exact trace-free Weyl discriminant and repeated-spectrum test")

    # Infinitesimal independent rotations on oriented tangent/normal planes.
    p, q = sp.symbols("p q", real=True)
    J = sp.Matrix([[0, -p, 0, 0], [p, 0, 0, 0],
                   [0, 0, 0, -q], [0, 0, q, 0]])
    pairs = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
    e = [sp.eye(4)[:, i] for i in range(4)]

    def wedge(u, v):
        return sp.Matrix([u[i]*v[j] - u[j]*v[i] for i, j in pairs])

    exterior = sp.Matrix.hstack(
        *[wedge(J*e[i], e[j]) + wedge(e[i], J*e[j]) for i, j in pairs]
    )
    E = sp.eye(6)
    sd = sp.Matrix.hstack(E[:, 0] + E[:, 5], E[:, 1] - E[:, 4],
                         E[:, 2] + E[:, 3])
    asd = sp.Matrix.hstack(E[:, 0] - E[:, 5], E[:, 1] + E[:, 4],
                          E[:, 2] - E[:, 3])
    for basis, rate in [(sd, p + q), (asd, q - p)]:
        rep = sp.simplify(basis.T * exterior * basis / 2)
        assert rep == sp.Matrix([[0, 0, 0], [0, 0, -rate], [0, rate, 0]])
        assert exterior * basis == basis * rep
    print("PASS 2: Weyl-bundle restriction is a trivial line plus sum/difference plane")

    for normal_euler in range(-7, 8, 2):
        assert (2 + normal_euler) % 2 == 1
        assert (2 - normal_euler) % 2 == 1
    print("PASS 3: both Weyl bundles have odd w2 on every odd sphere")

    chi, tau = 4, 2
    assert sp.Rational(chi + tau, 4) == sp.Rational(3, 2)
    assert sp.Rational(chi - tau, 4) == sp.Rational(1, 2)
    assert (chi + tau) % 4 != 0 and (chi - tau) % 4 != 0
    print("PASS 4: neither orientation has integral canonical Spin^c index")

    assert 12 * tau == 24
    assert (chi - 2 + tau) // 2 == 2
    assert (chi - 2 - tau) // 2 == 0
    print("PASS 5: signature and Betti-number normalization")

    Jc = sp.Matrix([[0, -1, 0, 0], [1, 0, 0, 0],
                    [0, 0, 0, -1], [0, 0, 1, 0]])
    entries = sp.symbols("h0:10", real=True)
    symmetric = sp.zeros(4)
    pos = 0
    for i in range(4):
        for j in range(i, 4):
            symmetric[i, j] = symmetric[j, i] = entries[pos]
            pos += 1
    H = (symmetric + Jc.T * symmetric * Jc) / 2
    assert sp.simplify(Jc * H + (Jc * H).T) == sp.zeros(4)
    grad = sp.Matrix(sp.symbols("v0:4", real=True))
    assert sp.expand((grad.T * Jc * grad)[0]) == 0
    print("PASS 6: J-invariant Hessian gives Killing J-gradient preserving its potential")


if __name__ == "__main__":
    verify()

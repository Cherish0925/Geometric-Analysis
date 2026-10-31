"""Exact constraints and curvature checks for the round-6 connector models."""

import sympy as s


def zero(expr):
    value = s.simplify(s.cancel(expr))
    assert value == 0, value


# An explicit analytic closed shape loop, in the local chart z=tan(theta).
# The theta formulas in the note show that the data extend over theta mod pi.
z = s.symbols("z", real=True)
M = s.Matrix(
    [[4 + z**2, 3 * z], [3 * z, 1 + 4 * z**2]]
) / (2 * (1 + z**2))
zero(M.det() - 1)
b2 = 9 / (2 * (25 + 28 * z**2) * (1 + z**2))
b = s.sqrt(b2)
h = s.diag(b2, 1, 1)
h[1:3, 1:3] = M
hi = s.simplify(h.inv())
K = s.zeros(3)
K[0, 1] = K[1, 0] = b / 2
q = s.Matrix([1, 0])
Q = s.cancel((q.T * M.inv() * q)[0] / 2)
zero(Q - (1 + 4 * z**2) / (4 * (1 + z**2)))


def derivative(expr, index):
    return s.diff(expr, z) if index == 0 else s.Integer(0)


Gamma = [
    [
        [
            s.cancel(
                sum(
                    hi[k, ell]
                    * (
                        derivative(h[ell, j], i)
                        + derivative(h[ell, i], j)
                        - derivative(h[i, j], ell)
                    )
                    for ell in range(3)
                )
                / 2
            )
            for j in range(3)
        ]
        for i in range(3)
    ]
    for k in range(3)
]
Ric = s.zeros(3)
for i in range(3):
    for j in range(3):
        Ric[i, j] = s.cancel(
            sum(
                derivative(Gamma[k][i][j], k)
                - derivative(Gamma[k][i][k], j)
                + sum(
                    Gamma[k][i][j] * Gamma[ell][k][ell]
                    - Gamma[ell][i][k] * Gamma[k][j][ell]
                    for ell in range(3)
                )
                for k in range(3)
            )
        )
scalar = s.cancel(s.trace(hi * Ric))
zero(scalar + 6 + Q)
H = s.trace(hi * K)
zero(H)
K2 = s.simplify(s.trace(hi * K * hi * K))
zero(K2 - Q)
zero(scalar + K2 - H**2 + 6)

# Contracted Codazzi, with no assumption that shape and charge are aligned.
for j in range(3):
    divergence = 0
    for i in range(3):
        for k in range(3):
            cov = derivative(K[k, j], i) - sum(
                Gamma[ell][i][k] * K[ell, j]
                + Gamma[ell][i][j] * K[k, ell]
                for ell in range(3)
            )
            divergence += hi[i, k] * cov
    zero(divergence - derivative(H, j))

shape_energy = s.cancel(s.trace(M.inv() * M.diff(z) * M.inv() * M.diff(z)) / (2 * b2))
zero(shape_energy - 12 - 2 * Q)
# The orbit has trace-free shape A=(2b)^(-1) M^-1 M_z in the initial slice.
orbit_shape = M.inv() * M.diff(z) / (2 * b)
zero(-orbit_shape.det() - 3 - Q / 2)

# Full radial Ricci error and charge for a variable toral Kottler mass.
r = s.symbols("r", positive=True)
c = s.symbols("c", real=True)
m = s.Function("m")(r)
V = r**2 - m / r
p = s.diff(m, r, 2) / (2 * r)
w = s.diff(m, r) / r**2
zero(-s.diff(V, r, 2) / 2 - s.diff(V, r) / r + 3 - p)
zero(-s.diff(V, r) / r - V / r**2 + 3 - w)
D = r**2 + c**2 * V
charge = c * (r**2 * s.diff(V, r) - 2 * r * V)
zero(charge - c * (3 * m - r * s.diff(m, r)))
zero(s.diff(charge, r) + 2 * c * r**2 * (p - w))
zero(
    V * s.diff(charge, r) ** 2 / (r**2 * D**2)
    - 4 * c**2 * r**2 * V * (p - w) ** 2 / D**2
)

# Weyl eigenvalue parameter; two sectional entries omega, four -omega/2.
omega = m / r**3 + p / 3 - 2 * w / 3
scalar4 = -12 + 2 * p + 2 * w
zero(-s.diff(V, r, 2) / 2 - (p - 3) + scalar4 / 6 - omega)
zero(-V / r**2 - (w - 3) + scalar4 / 6 - omega)
zero(-s.diff(V, r) / (2 * r) - (p + w - 6) / 2 + scalar4 / 6 + omega / 2)

# Exact positive-mass black-hole twist integral via a boundary primitive.
V1 = r**2 - 1 / r
D1 = r**2 + c**2 * V1
flux_primitive = V1 * r + V1 * r**2 * s.diff(D1, r) / (2 * D1) - 2 * (r**3 - 1)
zero(s.diff(flux_primitive, r) - 9 * c**2 / (2 * D1**2))
zero(flux_primitive.subs(r, 1))
zero(s.limit(flux_primitive, r, s.oo) - 3 * c**2 / (2 * (1 + c**2)))

print("PASS: complete 3D Ricci scalar and all momentum constraints;")
print("      charged neck shape energy, norm and positive orbit curvature;")
print("      all radial Ricci eigenvalues, Maxwell block, Weyl and twist integral.")

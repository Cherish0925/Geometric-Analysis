#!/usr/bin/env python3
"""Exact local checks for canonical shear; topology/PDE existence are proof inputs."""

import sympy as s


def check(label, value):
    if isinstance(value, s.MatrixBase):
        assert value.applyfunc(s.simplify) == s.zeros(*value.shape), label
    else:
        assert s.simplify(value) == 0, (label, value)
    print("PASS:", label)


coords = t, phi, x, y = s.symbols("t phi x y", real=True)
a, z = s.Function("a")(t), s.Function("z")(t)


def parity(indices):
    return (-1) ** sum(indices[i] > indices[j]
                       for i in range(len(indices)) for j in range(i + 1, len(indices)))


def wedge(left, right):
    result = {}
    for I, u in left.items():
        for J, v in right.items():
            raw = I + J
            if len(set(raw)) != len(raw):
                continue
            key = tuple(sorted(raw))
            result[key] = result.get(key, 0) + parity(raw) * u * v
    return {I: s.simplify(v) for I, v in result.items() if s.simplify(v) != 0}


def exterior_derivative(form):
    result = {}
    for I, value in form.items():
        for j, coordinate in enumerate(coords):
            piece = wedge({(j,): s.diff(value, coordinate)}, {I: 1})
            for key, coefficient in piece.items():
                result[key] = result.get(key, 0) + coefficient
    return {I: s.simplify(v) for I, v in result.items() if s.simplify(v) != 0}


def two_form_matrix(form):
    out = s.zeros(4)
    for (i, j), value in form.items():
        out[i, j], out[j, i] = value, -value
    return out


theta = {(1,): 1, (2,): z}
omega_E = {(0, 1): a, (0, 2): a * z}
omega = {**omega_E, (2, 3): y**-2}
assert exterior_derivative(omega) == {}
print("PASS: closed canonical plane form")
check("symplectic volume normalization", wedge(omega, omega)[(0, 1, 2, 3)] - 2 * a / y**2)

G = s.Matrix([[1, 0, 0, 0],
              [0, a*a, a*a*z, 0],
              [0, a*a*z, a*a*z*z + y**-2, 0],
              [0, 0, 0, y**-2]])
Gi = G.inv()
check("metric determinant", G.det() - a*a / y**4)
Omega = two_form_matrix(omega)
raised = Gi * Omega * Gi.T
check("exact norm squared two", sum(Omega[i, j] * raised[i, j]
                                    for i in range(4) for j in range(4)) / 2 - 2)
star = s.Matrix(4, 4, lambda i, j: a / (2*y**2) * sum(
    s.LeviCivita(i, j, k, l) * raised[k, l] for k in range(4) for l in range(4)))
check("exact self-duality", star - Omega)

connection = {(1,): -s.diff(a, t), (2,): -s.diff(a, t) * z}
curvature = exterior_derivative(connection)
check("Euler curvature dt-circle entry", curvature[(0, 1)] + s.diff(a, t, 2))
check("Euler curvature shear correction",
      curvature[(0, 2)] + s.diff(a, t, 2)*z + s.diff(a, t)*s.diff(z, t))
check("negative hyperbolic Euler sign",
      curvature[(0, 1)].subs(s.diff(a, t, 2), a) + omega_E[(0, 1)])

ell, R, normalization = s.symbols("ell R normalization", positive=True)
radius = ell * s.cosh(t) / (2*s.pi)
even_bump = s.exp(-1 / (R**2 - t**2)) / normalization
correction_density = s.diff(radius, t) * even_bump
check("balanced Euler correction is odd",
      correction_density.subs(t, -t) + correction_density)
# Oddness plus symmetric support proves zero total integral analytically;
# the primitive vanishes near both endpoints as explained in the note.

aa, zp, zpp, k, beta_norm = s.symbols("aa zp zpp k beta_norm", real=True)
Q = aa**2 * zp**2 * beta_norm**2 / 2
mixed = -aa * (zpp + 3*k*zp) * beta_norm / 2
Ein = s.Matrix([[-Q, 0, 0, 0], [0, Q, mixed, 0],
                [0, mixed, -Q, 0], [0, 0, 0, 0]])
check("full Ricci defect trace", s.trace(Ein) + Q)
tf = Ein - s.trace(Ein) * s.eye(4) / 4
check("trace-free Ricci norm", s.trace(tf.T * tf)
      - s.Rational(11, 4)*Q**2 - aa**2*(zpp+3*k*zp)**2*beta_norm**2/2)
check("scalar square loss", (-4-Q)**2 - 16 - 8*Q - Q**2)

I3, I5, J3, T = s.symbols("I3 I5 J3 T", positive=True)
Bs = 8*s.pi*ell**3*I3 + s.pi*ell**5*I5/2
P = s.pi*ell**3*J3 + 11*s.pi*ell**5*I5/8
D = ell**3*(J3+2*I3)/(32*s.pi) + 3*ell**5*I5/(64*s.pi)
check("exact LB polynomial", D - (P+Bs/4)/(32*s.pi**2))
check("Ricci-energy identity at exact canonical period",
      P+(32*s.pi**2*T+Bs)/4 - (8*s.pi**2*T+32*s.pi**2*D))

omega_vector = s.Matrix([s.sqrt(2), 0, 0])
model = s.Rational(1, 2) * (s.Rational(2, 3)*s.eye(3) - omega_vector*omega_vector.T)
check("allowed negative-Einstein Weyl model",
      model - s.diag(-s.Rational(2, 3), s.Rational(1, 3), s.Rational(1, 3)))
check("canonical norm and volume give p=T", (2/(4*s.pi**2))*(2*s.pi**2*T) - T)

N = s.Matrix([[0, 1], [0, 0]])
J = s.Matrix([[0, 1], [-1, 0]])
n, m = s.symbols("n m", integer=True)
check("surviving transvection is nilpotent", N*N)
check("transvection preserves intersection form", (s.eye(2)+N).T*J*(s.eye(2)+N)-J)
check("nonzero powers retain the shear", (s.eye(2)+n*N)*(s.eye(2)+m*N)
      - s.eye(2)-(n+m)*N)
print("All exact checks passed; global Euler patching, SW, and virtual Kahler obstruction are analytic/topological proofs.")

"""Exact first-jet checks; this does not certify global geometric PDE arguments."""
from itertools import combinations
import sympy as s


def zero(expression):
    assert s.expand(expression) == 0, s.factor(expression)


forms = []
for pairs in [((0, 1), (2, 3)), ((0, 2), (3, 1)), ((0, 3), (1, 2))]:
    form = s.zeros(4)
    for i, j in pairs:
        form[i, j], form[j, i] = 1, -1
    forms.append(form)
omega = forms[0]
t = s.symbols("t", nonzero=True, real=True)
dt = s.symbols("h0:4", real=True)
a = s.symbols("a0:4", real=True)
b = s.symbols("b0:4", real=True)
grad = [a[i] * forms[1] + b[i] * forms[2] for i in range(4)]
u = s.Matrix(dt) / (3 * t)


def wedge(alpha, beta):
    return alpha * beta.T - beta * alpha.T


interior_u = omega.T * u
Q = []
for i in range(4):
    ei = s.eye(4).col(i)
    interior_i = omega.T * ei
    Q.append(grad[i] - wedge(u, interior_i) + wedge(ei, interior_u))


def norm_forms(sequence):
    return sum(matrix[i, j] ** 2 for matrix in sequence
               for i, j in combinations(range(4), 2))


def alternating(sequence):
    return {(i, j, k): sequence[i][j, k] + sequence[j][k, i] + sequence[k][i, j]
            for i, j, k in combinations(range(4), 3)}


domega = alternating(grad)
altQ = alternating(Q)
for (i, j, k), value in altQ.items():
    zero(value - domega[i, j, k]
         - 2 * (u[i] * omega[j, k] + u[j] * omega[k, i] + u[k] * omega[i, j]))
for matrix in Q:
    zero(sum(matrix[i, j] * omega[i, j] for i, j in combinations(range(4), 2)))
    zero(matrix[0, 1] - matrix[2, 3])
    zero(matrix[0, 2] - matrix[3, 1])
    zero(matrix[0, 3] - matrix[1, 2])
print("PASS: conformal connection correction is self-dual, angular, and has the asserted alternation")


def divergence(derivatives):
    return s.Matrix([
        sum(derivatives[i][v, w] * forms[v][i, j] * forms[w][k, l]
            for i in range(4) for v in range(3) for w in range(3)) / 2
        for j in range(4) for k in range(4) for l in range(4)
    ])


model = s.diag(-s.Rational(4, 3), s.Rational(2, 3), s.Rational(2, 3))
dA = [dt[i] * model - 2 * t * s.Matrix([[0, a[i], b[i]],
                                      [a[i], 0, 0], [b[i], 0, 0]])
      for i in range(4)]
J = divergence(dA)
coeff_Q = [[sum(matrix[i, j] * forms[r][i, j]
                for i, j in combinations(range(4), 2)) / 2 for r in (1, 2)]
           for matrix in Q]
angular_A = [-2 * t * s.Matrix([[0, c[0], c[1]], [c[0], 0, 0], [c[1], 0, 0]])
             for c in coeff_Q]
J_Q = divergence(angular_A)
for value in J - J_Q:
    zero(value)
print("PASS: full 64-component sourced identity J(t, grad omega)=t D(Q)")
zero(J.dot(J) - 2 * t**2 * norm_forms(Q)
     - 4 * t**2 * sum(value**2 for value in altQ.values()))
print("PASS: exact divergence norm identity for all twelve first-jet variables")

# The kernel consists of four free amplitude derivatives, not constant t.
kernel_grad = [s.simplify(grad[i] - Q[i]) for i in range(4)]
for i in range(4):
    substitution = {a[i]: kernel_grad[i][0, 2], b[i]: kernel_grad[i][0, 3]}
    for value in Q[i].subs(substitution):
        zero(value)
variables = list(dt) + list(a) + list(b)
quadratic = s.hessian(s.expand(J.dot(J).subs(t, 1)), variables) / 2
assert quadratic.rank() == 8
assert len(quadratic.nullspace()) == 4
assert all(eigen.is_nonnegative is True for eigen in quadratic.eigenvals())
print("PASS: rank-eight divergence symbol with four-dimensional conformal kernel")

# Check the conformal volume and covariant-three-tensor weights.
r = s.symbols("r", positive=True)
zero(r**(-s.Rational(4, 3)) * 2 * r**2
     - 2 * r**(s.Rational(4, 3)) * r**(-s.Rational(2, 3)))
print("PASS: exact weighted conformal energy exponent -4/3")

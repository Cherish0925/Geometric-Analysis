"""Coordinate Ricci checks for the fixed closed product-block construction.

This checks local tensor identities, not global topology or prior art.
Run: qiushi-yau26 env numeric python round11_closed_gluing_check.py
"""

import sympy as s

a, p, z, v, w, x = s.symbols("a p z v w x", real=True)
sqrt3 = s.sqrt(3)


def simp(expr):
    return s.factor(s.cancel(s.expand(expr)))


def deriv(expr, index):
    if index == 0:
        return p*s.diff(expr, a) + 3*a*s.diff(expr, p) + v*s.diff(expr, z) + w*s.diff(expr, v)
    if index == 2:
        return s.diff(expr, x)
    return s.S.Zero


def ricci(metric):
    inverse = metric.inv().applyfunc(simp)
    gamma = [[[s.S.Zero for _ in range(4)] for _ in range(4)] for _ in range(4)]
    for k in range(4):
        for i in range(4):
            for j in range(i, 4):
                value = simp(sum(inverse[k, l]*(deriv(metric[l, j], i)
                    + deriv(metric[l, i], j) - deriv(metric[i, j], l)) for l in range(4))/2)
                gamma[k][i][j] = gamma[k][j][i] = value
    result = s.zeros(4)
    for i in range(4):
        for j in range(i, 4):
            value = sum(deriv(gamma[k][i][j], k) - deriv(gamma[k][i][k], j)
                + sum(gamma[k][i][j]*gamma[l][k][l] - gamma[l][i][k]*gamma[k][j][l]
                    for l in range(4)) for k in range(4))
            result[i, j] = result[j, i] = simp(value)
    return result


def assert_matrix_zero(matrix, label):
    for i in range(4):
        for j in range(4):
            value = simp(matrix[i, j])
            assert value == 0, (label, i, j, value)
    print(f"PASS: {label}, all 16 matrix entries")


# Shear: beta = dx + dy is closed, but div_h beta = 3 is nonzero.
# h = (dx^2 + exp(2x)dy^2)/3, and a''=3a.
theta = s.Matrix([0, 1, z, z])
metric = s.diag(1, 0, s.Rational(1, 3), s.exp(2*x)/3) + a*a*theta*theta.T
frame = s.Matrix([[1, 0, 0, 0], [0, 1/a, -sqrt3*z, -sqrt3*s.exp(-x)*z],
                  [0, 0, sqrt3, 0], [0, 0, 0, sqrt3*s.exp(-x)]])
assert_matrix_zero(frame.T*metric*frame-s.eye(4), "shear orthonormal frame")
actual = frame.T*(ricci(metric)+3*metric)*frame
beta = s.Matrix([sqrt3, sqrt3*s.exp(-x)])
beta_sq = simp((beta.T*beta)[0])
expected = s.zeros(4)
expected[0, 0] = -a*a*v*v*beta_sq/2
expected[1, 1] = a*a*v*v*beta_sq/2
expected[0, 1] = expected[1, 0] = 3*a*v/2
for i in range(2):
    expected[i+2, 1] = expected[1, i+2] = -a*(w+3*p*v/a)*beta[i]/2
    for j in range(2):
        expected[i+2, j+2] = -a*a*v*v*beta[i]*beta[j]/2
assert_matrix_zero(actual-expected, "full shear Ricci defect, including divergence and 3k term")
assert simp((actual-expected).trace()) == 0


# Hyperbolic path with nonzero trace: h_z=(dx^2+exp(2x+2z)dy^2)/3.
# S=diag(0,v), H=v, div S=-v dx, so this tests the trace and mixed blocks.
metric_path = s.diag(1, a*a, s.Rational(1, 3), s.exp(2*x+2*z)/3)
frame_path = s.diag(1, 1/a, sqrt3, sqrt3*s.exp(-x-z))
actual_path = frame_path.T*(ricci(metric_path)+3*metric_path)*frame_path
expected_path = s.diag(-w-v*v, -p*v/a, 0, -w-(p/a+v)*v)
expected_path[0, 2] = expected_path[2, 0] = -sqrt3*v
assert_matrix_zero(actual_path-expected_path, "path Ricci defect, including H and Codazzi terms")


# A malformed sign or omitted lapse derivative must fail the same checks.
wrong = expected.copy()
wrong[0, 1] = wrong[1, 0] = -3*a*v/2
assert simp(actual[0, 1]-wrong[0, 1]) != 0
wrong = expected.copy()
wrong[2, 1] = wrong[1, 2] = -a*(w+p*v/a)*beta[0]/2
assert simp(actual[2, 1]-wrong[2, 1]) != 0
wrong_path = expected_path.copy()
wrong_path[1, 1] = 0
assert simp(actual_path[1, 1]-wrong_path[1, 1]) != 0
print("PASS: three incorrect mixed/trace formulas rejected")
print("All coordinate checks passed. Global assembly and uniform estimates are proved in the note.")

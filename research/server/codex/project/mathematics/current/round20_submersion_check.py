"""Coordinate check of the nonflat-connection terms used in Round 20.

The local example has hyperbolic base and fibres, minimal fibres,
and a nonintegrable horizontal distribution. It is not a closed example.
"""

import sympy as s

t, r, u, v = s.symbols("t r u v", real=True)
x = [t, r, u, v]
g = s.diag(1, s.exp(2*t), 1, s.exp(2*u))
g[1, 1] += t*t*s.exp(2*u)
g[1, 3] = g[3, 1] = t*s.exp(2*u)
gi = g.inv()

def clean(f):
    return s.simplify(s.expand(f))

gamma = [[[clean(sum(gi[k, l] * (
    s.diff(g[l, j], x[i]) + s.diff(g[l, i], x[j])
    - s.diff(g[i, j], x[l])) for l in range(4))/2)
    for j in range(4)] for i in range(4)] for k in range(4)]
ric = s.Matrix(4, 4, lambda i, j: clean(sum(
    s.diff(gamma[k][i][j], x[k]) - s.diff(gamma[k][i][k], x[j])
    + sum(gamma[k][i][j]*gamma[l][k][l]
          - gamma[l][i][k]*gamma[k][j][l] for l in range(4))
    for k in range(4))))
frame = s.Matrix.hstack(
    s.Matrix([1, 0, 0, 0]),
    s.Matrix([0, s.exp(-t), 0, -t*s.exp(-t)]),
    s.Matrix([0, 0, 1, 0]),
    s.Matrix([0, 0, 0, s.exp(-u)]))
assert (frame.T*g*frame-s.eye(4)).applyfunc(clean) == s.zeros(4)
error = (frame.T*(ric+g)*frame).applyfunc(clean)

# [X_1,X_2]^V = -exp(-t) partial_v; both ordered A entries count.
A2 = s.exp(2*(u-t))/2
assert clean(error[0, 0]+A2) == 0
assert clean(error[1, 1]+A2) == 0
assert clean(error[0, 1]) == 0
assert clean(error[0, 0]+error[1, 1]+2*A2) == 0
assert clean(error[2, 2]+error[3, 3]-A2) == 0
assert clean(s.trace(error)+A2) == 0
# Omitting either A term would fail on this actual coordinate metric.
assert A2 != 0 and clean(error[2, 2]+error[3, 3]) != 0
print("PASS: orthonormal horizontal/vertical frame")
print("PASS: horizontal defect = -|A|^2 I, horizontal trace = -2|A|^2")
print("PASS: vertical defect trace = |A|^2; scalar defect = -|A|^2")
print("Scope: local tensor identities, not the global signature theorem.")

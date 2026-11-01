#!/usr/bin/env python3
"""Exact full-jet algebra for the product-profile elliptic estimate.

Checks the eight-dimensional tangent-jet divergence, not only the
rank-one symbol. Does not certify the imported local mean-value theorem.
"""
import sympy as s

k = s.symbols("k", positive=True)
W = s.diag(-2*k/3, k/3, k/3)
I = s.eye(3)

def N(A):
    return A*A + k*A/3 - 2*k*k*I/9

def DN(A, H):
    return A*H + H*A + k*H/3

def Q(A):
    return -2*k*A - 6*A*A + 2*s.trace(A*A)*I

assert N(W) == s.zeros(3)
assert Q(W) == s.zeros(3)
print("PASS: polynomial and Einstein equation vanish on product orbit")

# Five orthogonal traceless-symmetric directions, with integer entries.
dirs = [s.diag(-2, 1, 1), s.diag(0, 1, -1)]
for a, b in ((1, 2), (0, 1), (0, 2)):
    H = s.zeros(3)
    H[a, b] = H[b, a] = 1
    dirs.append(H)
for index, H in enumerate(dirs):
    A = DN(W, H)
    if index < 3:
        assert s.simplify(s.trace(A*A) - k*k*s.trace(H*H)) == 0
    else:
        assert A == s.zeros(3)
print("PASS: DN has singular value k on normal space and kernel orbit tangent")

# Unit self-dual basis has matrices omega/sqrt(2), where omega below has
# exterior norm sqrt(2). W4_ijkl = sum W_ab omega_a,ij omega_b,kl / 2.
omega = []
for pairs in (((0, 1), (2, 3)),
              ((0, 2), (3, 1)),
              ((0, 3), (1, 2))):
    A = s.zeros(4)
    for a, b in pairs:
        A[a, b], A[b, a] = 1, -1
    omega.append(A)

x = s.symbols("x0:8", real=True)
T = []
for i in range(4):
    A = s.zeros(3)
    A[0, 1] = A[1, 0] = x[2*i]
    A[0, 2] = A[2, 0] = x[2*i+1]
    T.append(A)

delta = []
for j in range(4):
    for a in range(4):
        for b in range(4):
            delta.append(sum(T[i][u, v]*omega[u][i, j]*omega[v][a, b]/2
                             for i in range(4)
                             for u in range(3) for v in range(3)))
J = s.Matrix(delta).jacobian(x)
G = J.T*J
assert G.eigenvals() == {s.Integer(1): 4, s.Integer(3): 4}
assert J.rank() == 8
assert (G - s.eye(8)).is_positive_semidefinite
# |T|^2 = 2 |x|^2, hence |delta T|^2 >= |T|^2/2.
assert sum(s.trace(A*A) for A in T) == 2*sum(v*v for v in x)
print("PASS: full tangent-jet Gram eigenvalues 1 (x4), 3 (x4), rank 8")
print("PASS: |delta T_tangent|^2 >= |T_tangent|^2/2")

# At the model DQ has mixed normal signs: this prevents an automatic
# positive-potential maximum-principle conclusion from this calculation.
expected = [2*k, -6*k, -6*k, 0, 0]
for H, lam in zip(dirs, expected):
    dQ = -2*k*H - 6*(W*H + H*W) + 4*s.trace(W*H)*I
    assert dQ == lam*H
print("PASS: DQ normal eigenvalues 2k, -6k, -6k; tangent eigenvalues zero")

assert 1 + (4*s.sqrt(2))**2 == 33
assert 4*33 == 132
print("PASS: safe jet coercivity constants sqrt(33)/k and 132/k^2")
print("All exact Round-16 rigidity checks passed.")

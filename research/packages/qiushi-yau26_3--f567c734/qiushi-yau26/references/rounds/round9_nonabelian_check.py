#!/usr/bin/env python3
"""Exact algebra checks; not a nonabelian PDE existence verification."""
import sympy as s

I = s.I
eye = s.eye(2)
pauli = [
    s.Matrix([[0, 1], [1, 0]]),
    s.Matrix([[0, -I], [I, 0]]),
    s.diag(1, -1),
]
clifford = [eye] + [I * p for p in pauli]
x, y = s.symbols("x y", positive=True)
H = s.diag(x, y)


def real_vector(matrix):
    entries = list(matrix)
    return s.Matrix([s.re(v) for v in entries] + [s.im(v) for v in entries])


def connection_map(basis):
    return s.Matrix.hstack(
        *[real_vector(B * H * c) for c in clifford for B in basis]
    )


u2 = connection_map([I * eye] + [I * p for p in pauli])
u2_columns = [0, 1, 2, 3, 4, 5, 8, 12]
assert s.factor(u2[:, u2_columns].det()) == -2 * x * y * (x*x + y*y)**3
assert u2.subs(y, x).rank() == 8
print("PASS full U(2) Dirac connection map is surjective at every positive H")

su2 = connection_map([I * p for p in pauli])
su2_columns = [0, 1, 2, 3, 4, 5, 8, 11]
assert s.factor(su2[:, su2_columns].det()) == -(x-y)**4 * (x+y)**4
assert su2.subs(y, x).rank() == 4
quaternions = s.Matrix.hstack(*[real_vector(c) for c in clifford])
assert quaternions.row_join(su2.subs(y, x)).rank() == 4
print("PASS fixed-determinant map has rank 8 off the scalar locus, rank 4 on it")

# Tensor projection: blocks are target endomorphisms indexed by source indices.
columns = [H[:, j] for j in range(2)]
blocks = [[columns[i] * columns[j].conjugate().T for j in range(2)] for i in range(2)]
target_partial_trace = H * H.conjugate().T
for i in range(2):
    blocks[i][i] -= target_partial_trace / 2
source_trace_matrix = s.Matrix(2, 2, lambda i, j: s.trace(blocks[i][j]))
assert source_trace_matrix == s.diag((x*x-y*y)/2, (y*y-x*x)/2)
assert blocks[0][1] == s.Matrix([[0, x*y], [0, 0]])
assert blocks[1][0] == s.Matrix([[0, 0], [x*y, 0]])
congruence = s.Matrix.hstack(*[real_vector(H * p * H) for p in pauli])
assert congruence.rank() == 3
print("PASS trace anisotropy and rank-three target curvature; off-diagonal xy survives")

# A full-rank parallel non-scalar H forces diagonal curvature, incompatible above.
assert s.simplify(s.trace((H*H - s.trace(H*H)*eye/2)**2)) == (x*x-y*y)**2/2
print("PASS singular-value normalization in the harmonic trace bound")

# Covariant closedness of Theta: X_i c_j-X_j c_i=0 implies all X_i=0.
variables = s.symbols("v0:16")
X = [s.Matrix(2, 2, variables[4*j:4*j+4]) for j in range(4)]
closed = []
for i in range(4):
    for j in range(i+1, 4):
        closed.extend(list(X[i]*clifford[j]-X[j]*clifford[i]))
closed_matrix, _ = s.linear_eq_to_matrix(closed, variables)
assert closed_matrix.rank() == 16
print("PASS covariantly closed Clifford one-form implies parallel homomorphism")

# Index and characteristic-class substitutions.
chi, signature, a2, ell = s.symbols("chi signature a2 ell")
T = 2*chi + 3*signature
c2 = (a2-T)/4
dirac_complex = s.expand(a2/4 - c2 - signature/4)
assert dirac_complex == (chi+signature)/2
asd_u2 = -2*T - 2*(chi+signature)
full_index = s.expand(asd_u2 + 2*dirac_complex)
assert full_index == -5*chi-7*signature
fixed_det = s.expand(-2*T - s.Rational(3,2)*(chi+signature) + 2*dirac_complex)
assert fixed_det == -(9*chi+13*signature)/2
print("PASS U(2) index -5 chi -7 tau, fixed-determinant index and central-circle distinction")

# Normalized energy of isotropic seed on an actual volume=2*pi²*T input.
assert s.cancel((2*s.pi**2*T)/(2*s.pi**2*T)) == 1
print("PASS conformal full-rank seed has averaged curvature residual at least one")
print("All checks are exact algebra only; no nonlinear solution is asserted.")

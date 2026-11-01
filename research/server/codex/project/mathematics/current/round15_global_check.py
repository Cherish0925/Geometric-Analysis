#!/usr/bin/env python3
"""Exact algebra for round15_global.md; not a PDE or boundary solver."""

import sympy as s


def check(name, residual):
    if isinstance(residual, s.MatrixBase):
        residual = residual.applyfunc(s.simplify)
        zero = s.zeros(*residual.shape)
    else:
        residual = s.simplify(residual)
        zero = 0
    if residual != zero:
        raise AssertionError(f"{name}: {residual}")
    print(f"PASS {name}")


AB, AF, chi, kappa_int = s.symbols("AB AF chi kappa_int", real=True)
action = -6*AB*AF+2*AF*kappa_int
check("Product boundary action",
      action.subs(kappa_int, 2*s.pi*chi+3*AB)-4*s.pi*chi*AF)

R = s.symbols("R", positive=True)
k = s.sqrt(3)
disk_volume = 2*s.pi*AF/k**2*(s.cosh(k*R)-1)
disk_H = 2*s.pi*AF*s.cosh(k*R)
check("Disk product action", -6*disk_volume+2*disk_H-4*s.pi*AF)
check("Disk boundary volume variation",
      6*s.diff(disk_volume, R)-2*s.diff(disk_H, R))

kap = s.symbols("kap", real=True)
metric_boundary = s.eye(3)
A = s.diag(kap, 0, 0)
Pi = A-kap*metric_boundary
check("Boundary momentum trace", s.trace(Pi)+2*kap)
check("Recover second fundamental form",
      Pi-s.trace(Pi)*metric_boundary/2-A)
q1, q2 = s.symbols("q1 q2", real=True)
Q = s.Matrix([[0, 0, 0], [0, q1, q2], [0, q2, -q1]])
check("Product fiber TT momentum", s.trace(Pi*Q))
check("Boundary scalar constraint",
      -6+6-kap**2+s.trace(A*A))
u, normal_plus, normal_minus = s.symbols("u normal_plus normal_minus")
momentum_plus = normal_plus/2-kap*u
momentum_minus = normal_minus/2+kap*u
check("Interface Robin cancellation",
      momentum_plus+momentum_minus-(normal_plus+normal_minus)/2)

I1, I3 = s.symbols("I1 I3", positive=True)
D = s.Matrix([[1, -1], [-1, 1]])/(2*I1)
ones = s.ones(2, 1)
check("Throat response constant kernel", D*ones)
check("Throat response symmetry", D-D.T)
neck_conormals = -s.ones(2, 1)/(4*I3)
check("Circle integrated total source",
      2*s.pi*(neck_conormals[0]+neck_conormals[1])+s.pi/I3)

# An exact algebraic capacitance model. No particular hyperbolic surface
# is asserted to realize these chosen entries.
tau, d = s.symbols("tau d", positive=True)
C = tau*(s.eye(4)-s.ones(4)/4)
L = s.Matrix([[1, -1, 0, 0], [-1, 1, 0, 0],
              [0, 0, 1, -1], [0, 0, -1, 1]])
K = C+d*L
check("Exterior capacitance constant kernel", C*s.ones(4, 1))
check("Assembled constant kernel", K*s.ones(4, 1))
check("Assembled symmetry", K-K.T)
V = s.Matrix.hstack(s.ones(4, 1),
                   s.Matrix([1, 1, -1, -1]),
                   s.Matrix([1, -1, 0, 0]),
                   s.Matrix([0, 0, 1, -1]))
check("Positive complement eigenvalues",
      K*V-V*s.diag(0, tau, tau+2*d, tau+2*d))
rho = s.symbols("rho", positive=True)
balanced_source = rho*s.Matrix([-1, -1, 1, 1])
solution = -balanced_source/tau
check("Balanced source compatible", sum(balanced_source))
check("Balanced averaged matching solved", K*solution+balanced_source)
unbalanced_source = rho*s.Matrix([-1, -1, -1, -1])
if s.simplify(sum(unbalanced_source)) == 0:
    raise AssertionError("Nonzero aggregate source was accepted")
print("PASS nonzero aggregate source rejected")
print("All 17 exact identities and one incompatible-source test passed.")

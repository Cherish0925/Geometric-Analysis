"""Independent exact checks of the intrinsic spinor regularity argument.

This checks identities, not the existence theorem or its literature novelty.
Run: qiushi-yau26 env numeric python round3_independent_checks.py
"""

import sympy as s

z, w = s.symbols("z w", nonzero=True)
I = s.I
sinx, cosx = (z-z**-1)/(2*I), (z+z**-1)/2
siny, cosy = (w-w**-1)/(2*I), (w+w**-1)/2
J1 = s.Matrix([[0, 0, 0], [0, 0, -1], [0, 1, 0]])
J2 = s.Matrix([[0, 0, 1], [0, 0, 0], [-1, 0, 0]])
connection = [siny*J1, 2*sinx*J2]
variables = [z, w]


def partial(field, axis):
    return field.applyfunc(lambda f: s.expand(I*variables[axis]*s.diff(f, variables[axis])))


def nabla(field, axis):
    return (partial(field, axis)+connection[axis]*field).applyfunc(s.expand)


def mean(expr):
    # Constant Laurent coefficient = normalized integral on the flat torus.
    return s.expand(expr).coeff(z, 0).coeff(w, 0).simplify()


u = s.Matrix([cosx, siny, cosx*cosy])
du = [nabla(u, i) for i in range(2)]
hess = [[nabla(du[j], i) for j in range(2)] for i in range(2)]
lap = hess[0][0]+hess[1][1]
F = partial(connection[1], 0)-partial(connection[0], 1)
F += connection[0]*connection[1]-connection[1]*connection[0]
F = F.applyfunc(s.expand)
assert (hess[0][1]-hess[1][0]-F*u).applyfunc(s.expand) == s.zeros(3, 1)
assert (F+F.T).applyfunc(s.expand) == s.zeros(3)

hessian_energy = mean(sum(hess[i][j].dot(hess[i][j]) for i in range(2) for j in range(2)))
laplacian_energy = mean(lap.dot(lap))
curvature_gradient = mean((F*du[1]).dot(du[0])-(F*du[0]).dot(du[1]))
curvature_section = mean((F*u).dot(F*u))  # half the ordered i,j sum
assert hessian_energy == laplacian_energy+curvature_gradient+curvature_section
assert curvature_gradient != 0 and curvature_section != 0
assert hessian_energy != laplacian_energy+curvature_section
assert hessian_energy != laplacian_energy+curvature_gradient
print("Nonabelian periodic connection: Hessian identity passed")
print("Hessian, Laplacian, F-gradient, half F-section energies:",
      hessian_energy, laplacian_energy, curvature_gradient, curvature_section)

# No anti-self-dual Weyl block enters the positive-spin connection.
wp = s.symbols("wp0:5", real=True)
wm = s.symbols("wm0:5", real=True)
scalar = s.symbols("scalar", real=True)


def tracefree(v):
    return s.Matrix([[v[0], v[1], v[2]], [v[1], v[3], v[4]],
                     [v[2], v[4], -v[0]-v[3]]])


Wplus, Wminus = tracefree(wp), tracefree(wm)
B = s.Matrix(3, 3, s.symbols("b0:9", real=True))
R = (Wplus+scalar*s.eye(3)/12).row_join(B)
R = R.col_join(B.T.row_join(Wminus+scalar*s.eye(3)/12))
positive_connection = R[:3, :]
assert not any(positive_connection.has(v) for v in wm)
norm = sum(entry**2 for entry in positive_connection)
expected = sum(entry**2 for entry in Wplus)+scalar**2/48+sum(entry**2 for entry in B)
assert s.expand(norm-expected) == 0
print("Positive-spin curvature projection and scalar normalization: passed")

# Topological budgets used in the blow-up corollary.
assert s.Rational(108*25, 32) == s.Rational(675, 8)
assert s.Rational(108, 8)*4 == 54
print("Deficit/volume coefficients 54 and 675/8: passed")

# All averaged interpolation estimates must retain volume powers.
volume = s.symbols("volume", positive=True)
assert s.simplify(volume**(-s.Rational(1, 2))*volume**s.Rational(1, 2)) == 1
assert s.simplify((volume**s.Rational(1, 4))**2/volume**s.Rational(1, 2)) == 1
print("Normalized L4-squared / L2 scaling: passed")

# Exact square identities used to pass from monopoles to topology.
sc, unorm, wmin = s.symbols("sc unorm wmin", real=True)
aw = s.sqrt(s.Rational(2, 3))*unorm
calibration = sc+8*s.sqrt(6)*unorm
q = -sc+s.sqrt(6)*unorm
lowest = 2*sc/3+2*wmin
gap = (2*sc/3-2*aw)**2-lowest**2
energy = sc**2/24+2*unorm**2
assert s.simplify(calibration**2+18*gap-216*energy+18*lowest**2) == 0
assert s.simplify(calibration**2-216*energy+8*q**2) == 0
assert s.Rational(436)+54+1 == 491
assert s.Rational(675)+s.Rational(675, 8) == s.Rational(6075, 8) < 760

A, b, first_betti, m = s.symbols("A b first_betti m", real=True)
T_N = 4-4*first_betti-b
D = 4*m-T_N
T_M = A-D
class_square = A-b
assert s.expand(class_square-T_M-(4*m-4+4*first_betti)) == 0
assert s.expand(T_M/A-s.Rational(2, 3)-(s.Rational(1, 3)-D/A)) == 0
assert D.subs({m: 2, first_betti: 0}) == b+4
assert D.subs({m: 3, first_betti: 0}) == b+8
assert s.Rational(486)*s.Rational(65, 64)**2 == s.Rational(1026675, 2048)
assert s.Rational(65, 64)**2/2 == s.Rational(4225, 8192)
print("Completed-square budgets and connected-sum class-square identities: passed")

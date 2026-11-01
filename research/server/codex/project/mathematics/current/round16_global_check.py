"""Exact finite checks for round16_global.md; not a lattice/topology verifier."""
from itertools import combinations
import sympy as s

x1, y1, x2, y2 = s.symbols("x1 y1 x2 y2", positive=True)
coords = (x1, y1, x2, y2)
eta = (1 / (3 * y1), 0, 1 / (3 * y2), 0)
omega = {(0, 1): 1 / (3 * y1**2), (2, 3): 1 / (3 * y2**2)}
count = 0


def check(name, value):
    global count
    assert value, name
    count += 1
    print("PASS", name)


def equal(a, b):
    return s.simplify(a - b) == 0


deta = {
    (i, j): s.diff(eta[j], coords[i]) - s.diff(eta[i], coords[j])
    for i, j in combinations(range(4), 2)
}
check("positive-sign cusp primitive", all(equal(v, omega.get(key, 0)) for key, v in deta.items()))
ginv = s.diag(3 * y1**2, 3 * y1**2, 3 * y2**2, 3 * y2**2)
check("primitive squared norm 2/3", equal((s.Matrix(eta).T * ginv * s.Matrix(eta))[0], s.Rational(2, 3)))
t = s.log(y1 * y2) / s.sqrt(6)
dt = s.Matrix([s.diff(t, z) for z in coords])
check("unit cusp height gradient", equal((dt.T * ginv * dt)[0], 1))
volume_density = 1 / (9 * y1**2 * y2**2)
check("Kahler square equals twice volume", equal(2 * omega[0, 1] * omega[2, 3], 2 * volume_density))
r, z = s.symbols("r z", real=True)
ys = s.Matrix([s.exp((r + z) / 2), s.exp((r - z) / 2)])
jac = -ys.jacobian([r, z]).det()
check("cusp volume density in log coordinates", equal(jac / (9 * ys[0]**2 * ys[1]**2), s.exp(-r) / 18))
lam = s.symbols("lam", positive=True)
check("primitive invariant under diagonal cusp scaling", equal(lam / (3 * lam * y1), 1 / (3 * y1)))
a, b, c, d = s.symbols("a b c d")
A = s.Matrix([[a, b], [c, d]])
check("det(A-I)=2-trace(A) for det A=1", equal((A-s.eye(2)).det() - (2-a-d), A.det()-1))
check("det(A+I)=2+trace(A) for det A=1", equal((A+s.eye(2)).det() - (2+a+d), A.det()-1))
A0 = s.Matrix([[2, 1], [1, 1]])
check("test Sol monodromy is hyperbolic unimodular", A0.det() == 1 and A0.trace() > 2)
check("test Sol monodromy has no +/-1 eigenvalues", (A0-s.eye(2)).det() != 0 and (A0+s.eye(2)).det() != 0)
h, g = s.symbols("h g", positive=True)
check("reducible limit retains closed volume", equal((4*s.pi*h/3)*(4*s.pi*(g-1)/3), 4*s.pi**2*(4*h*(g-1))/9))
check("determinant curvature limit coefficient", equal(12/(2*s.sqrt(2)*s.sqrt(2)), 3))
check("wrong-sign primitive rejected", not all(equal(-v, omega.get(key, 0)) for key, v in deta.items()))
print(f"{count} exact finite checks passed; tree actions, lattice theorems, compact-core topology and convergence require the written proofs.")

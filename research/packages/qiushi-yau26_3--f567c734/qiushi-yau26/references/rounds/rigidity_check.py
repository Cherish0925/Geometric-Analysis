"""Exact algebra checks for rigidity.md; no metric-existence certificate."""

import sympy as sp

t = sp.Rational(1, 12)
eigenvalues = (-2 * t, t, t)
x0 = sum(value**2 for value in eigenvalues)
y0 = sp.prod(eigenvalues)
s = -4
potential = s * x0 / 2 - 18 * y0
assert (x0, y0, potential) == (
    sp.Rational(1, 24), sp.Rational(-1, 864), sp.Rational(-1, 16)
)

lam1, lam2, lam3, x, y = sp.symbols("lam1 lam2 lam3 x y", real=True)
f = x + 36 * y + 24 * (x - x0) ** 2
fx, fy = sp.diff(f, x), sp.diff(f, y)
fxx, fxy, fyy = sp.diff(f, x, 2), sp.diff(f, x, y), sp.diff(f, y, 2)
p, q, r = lam1 - lam2, lam2 - lam3, lam3 - lam1

def diagonal(other, gap):
    return 8 * fx - 4 * other * fy + gap**2 * (
        4 * fxx + other**2 * fyy - 4 * other * fxy
    )

def mixed(other, left, right, pair):
    return -2 * fx - 2 * other * fy + left * right * (
        4 * fxx + pair * fyy + 2 * other * fxy
    )

matrix = sp.Matrix([
    [diagonal(lam3, p), mixed(lam2, p, q, lam1*lam3), mixed(lam1, p, r, lam2*lam3)],
    [mixed(lam2, p, q, lam1*lam3), diagonal(lam1, q), mixed(lam3, q, r, lam1*lam2)],
    [mixed(lam1, p, r, lam2*lam3), mixed(lam3, q, r, lam1*lam2), diagonal(lam2, r)],
])
reaction = (s*x - 36*y)*fx + (sp.Rational(3, 2)*s*y - x*x)*fy
at_center = {lam1: eigenvalues[0], lam2: eigenvalues[1], lam3: eigenvalues[2], x: x0, y: y0}
matrix0 = matrix.subs(at_center)
assert matrix0 == sp.Matrix([[8, -8, -2], [-8, 32, -8], [-2, -8, 8]])
assert reaction.subs(at_center) == sp.Rational(1, 16)
shifted = matrix0 - sp.eye(3)
minors = [shifted[:n, :n].det() for n in (1, 2, 3)]
assert minors == [7, 153, 243]

eps = sp.Rational(1, 10000)
assert sp.Rational(2, 3)*eps + 3*eps**2 <= eps
assert sp.Rational(5, 144)*eps + sp.Rational(1, 3)*eps**2 + eps**3 <= eps/20
assert 720*eps + 768*eps**2 <= 721*eps
assert 360*eps + 768*eps**2 <= 361*eps
assert 1443*eps < sp.Rational(1, 2)
assert sp.Rational(157, 5)*eps + 36*eps**2 < 32*eps
assert sp.Rational(1, 16) - 32*eps > sp.Rational(1, 32)

# Independent symbol check for the high-frequency metric perturbation.
# Indices 0,1,2,3 correspond to the positively oriented orthonormal frame.
xi = (1, 0, 0, 0)
q_symbol = sp.diag(0, 1, -1, 0)
assert sp.trace(q_symbol) == 0
assert q_symbol * sp.Matrix(xi) == sp.zeros(4, 1)
cotton = sp.MutableDenseNDimArray.zeros(4, 4, 4)
cotton_plus = sp.MutableDenseNDimArray.zeros(4, 4, 4)
cotton_minus = sp.MutableDenseNDimArray.zeros(4, 4, 4)
for i in range(4):
    for j in range(4):
        for k in range(4):
            cotton[i, j, k] = xi[k]*q_symbol[i, j] - xi[j]*q_symbol[i, k]
for i in range(4):
    for j in range(4):
        for k in range(4):
            assert cotton[i, j, k] == -cotton[i, k, j]
            assert cotton[i, j, k] + cotton[j, k, i] + cotton[k, i, j] == 0
            star = sp.Rational(1, 2) * sum(
                sp.LeviCivita(j, k, a, b)*cotton[i, a, b]
                for a in range(4) for b in range(4)
            )
            cotton_plus[i, j, k] = (cotton[i, j, k] + star)/2
            cotton_minus[i, j, k] = (cotton[i, j, k] - star)/2
for k in range(4):
    assert sum(cotton[i, i, k] for i in range(4)) == 0
symbol_norms = tuple(
    sum(tensor[i, j, k]**2 for i in range(4) for j in range(4) for k in range(4))
    for tensor in (cotton, cotton_plus, cotton_minus)
)
assert symbol_norms == (4, 2, 2)

# The local polynomial necessarily loses derivative sign near the zero tensor.
u = sp.symbols("u", positive=True)
psi = f.subs({x: u**2, y: -u**3/(3*sp.sqrt(6))})
radial_derivative = sp.diff(psi, u, 2) + sp.Rational(2, 3)*sp.diff(psi, u)/u
assert sp.limit(radial_derivative, u, 0) == -sp.Rational(10, 3)
assert sp.simplify(sp.diff(psi, u).subs(u, 1/sp.sqrt(24)) + 1/sp.sqrt(24)) == 0

print("Exact checks passed.")
print("(norm squared, determinant, norm-Weitzenbock potential):", (x0, y0, potential))
print("Spectral-multiplier derivative matrix:", matrix0)
print("Leading principal minors of M0-I:", minors)
print("Reaction at target:", reaction.subs(at_center))
print("Certified spectral-box radius:", eps)
print("Cotton symbol squared norms (full, self-dual, anti-self-dual):", symbol_norms)
print("Local multiplier's radial derivative coefficient at zero:", sp.limit(radial_derivative, u, 0))

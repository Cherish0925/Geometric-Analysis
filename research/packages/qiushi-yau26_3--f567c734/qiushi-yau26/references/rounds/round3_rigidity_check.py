"""Exact algebra checks for the intrinsic monopole Hessian argument.

The general inequalities and manifold statements are proved in the note.
This script tests the curvature signs on an actual nonflat connection,
the Clifford chirality projection, and the divergence-energy coefficients.
"""

import sympy as sp

R = sp.Rational
y = sp.symbols("y", real=True)
b = 1 + sp.sin(y)
f = 2 + sp.cos(y)
bp, fp, fpp = sp.diff(b, y), sp.diff(f, y), sp.diff(f, y, 2)

# On the flat T^4 take A = i sin(y) dx and u = exp(i x) f(y).
# Covariant derivative in x multiplies by i b. Curvature F_xy=-i b'.
hessian2 = b**4 * f**2 + fpp**2 + b**2 * fp**2 + (bp * f + b * fp)**2
laplace2 = (-b**2 * f + fpp)**2
curvature_cross = -2 * b * bp * f * fp
half_fu2 = bp**2 * f**2

def avg(expr):
    return sp.simplify(sp.integrate(sp.expand_trig(sp.expand(expr)),
                                    (y, -sp.pi, sp.pi)) / (2 * sp.pi))

torus_values = [avg(v) for v in
                (hessian2, laplace2, curvature_cross, half_fu2)]
assert torus_values[0] == sum(torus_values[1:])
assert torus_values[2] != 0  # This example detects the cross-term sign.

# The absorption in dimension four: H^2 <= L^2+rG^2+4 K F H+K^2 F^2/2.
H, K, F = sp.symbols("H K F", nonnegative=True)
assert sp.expand(H**2 / 2 + 8 * K**2 * F**2 - 4 * K * F * H
                 - (H - 4 * K * F)**2 / 2) == 0
assert 2 * (8 + R(1, 2)) == 17

# Euclidean Clifford matrices c(e_j)^2=-I with a chirality block on which
# all anti-self-dual 2-forms vanish and all self-dual generators survive.
I2, Z2 = sp.eye(2), sp.zeros(2)
pauli = [sp.Matrix([[0, 1], [1, 0]]),
         sp.Matrix([[0, -sp.I], [sp.I, 0]]),
         sp.Matrix([[1, 0], [0, -1]])]

def blocks(a, b, c, d):
    return a.row_join(b).col_join(c.row_join(d))

cliff = [blocks(Z2, I2, -I2, Z2)]
cliff += [blocks(Z2, sp.I * s, sp.I * s, Z2) for s in pauli]
for i in range(4):
    for j in range(4):
        assert cliff[i] * cliff[j] + cliff[j] * cliff[i] == (
            -2 * sp.eye(4) if i == j else sp.zeros(4))

sd = [cliff[0] * cliff[1] + cliff[2] * cliff[3],
      cliff[0] * cliff[2] + cliff[3] * cliff[1],
      cliff[0] * cliff[3] + cliff[1] * cliff[2]]
asd = [cliff[0] * cliff[1] - cliff[2] * cliff[3],
       cliff[0] * cliff[2] - cliff[3] * cliff[1],
       cliff[0] * cliff[3] - cliff[1] * cliff[2]]
positive_block = None
for sl in (slice(0, 2), slice(2, 4)):
    if all(v[sl, sl] == Z2 for v in asd):
        positive_block = sl
        assert all(v[sl, sl] != Z2 for v in sd)
assert positive_block is not None

# Eliminate the weighted gradient in the previously checked first-jet
# formula using the weighted two-form Hodge identity.
rho, grad, ext, amp, cross, B = sp.symbols(
    "rho grad ext amp cross B", real=True)
grad_A = rho**2 * grad / 32 + rho**2 * amp / 96
grad_minus_div = (rho**2 * (grad - 2 * ext) / 64
                  + rho**2 * amp / 32 - rho * cross / 16)
div2 = grad_A - grad_minus_div
weighted_hodge_grad = 2 * ext - B + 4 * cross / rho - 2 * amp
eliminated = sp.expand(div2.subs(grad, weighted_hodge_grad))
claimed = (-rho**2 * B / 64 + rho**2 * ext / 16
           - 5 * rho**2 * amp / 96 + rho * cross / 8)
assert sp.simplify(eliminated - claimed) == 0

s, rterm = sp.symbols("s rterm", real=True)
B_decomp = s * rho**2 / 3 + rho**4 / 6 - 2 * rterm
potential = -s * rho**4 / 192 - rho**6 / 384 + rho**2 * rterm / 32
assert sp.expand(-rho**2 * B_decomp / 64 - potential) == 0
assert potential.subs({s: -4, rho: sp.sqrt(2), rterm: 0}) == R(1, 16)

print("Exact round-three rigidity checks passed.")
print("Torus averages (Hessian, Laplacian, F-gradient cross, half F-u):",
      torus_values)
print("Hessian absorption coefficient:", 17)
print("Anti-self-dual Clifford action vanishes on positive block:",
      positive_block)
print("Forced divergence-energy target:", R(1, 16))

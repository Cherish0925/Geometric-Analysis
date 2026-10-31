"""Exact algebra for round9_bundle.md; no Einstein existence claim.

Run: qiushi-yau26 env numeric python round9_bundle_check.py
"""

import sympy as s


def check(expr, label):
    assert s.simplify(expr) == 0, (label, expr)
    print(f"PASS {label}")


# Shared Hodge polarization. x,y are half the full squared norms;
# z,w are the positive-definite inner products in the two Hodge halves.
x, y, z, w, c, v = s.symbols("x y z w c v", real=True)
P = x+y+2*z
N = x+y-2*w
check((P+N)/2-(x+y+z-w), "two-orientation monopole sum")
check((P-N)/2-(z+w), "two-orientation monopole difference")
S = c*(2*v-1)
check(S**2-c**2-4*c**2*v*(v-1), "Hodge interval discriminant")
rplus = 2*v-1+2*s.sqrt(v*(v-1))
rminus = 2*v-1-2*s.sqrt(v*(v-1))
check(rplus*rminus-1, "reciprocal Hodge endpoints")
check((c*rplus/2)*(c*rminus/2)-c**2/4,
      "endpoint intersection product")
check((c*rplus/2)+(c*rminus/2)-S, "endpoint monopole budget")
V0 = 4*s.pi**2*c
check(4*s.pi**2*c*rminus-V0*rminus, "Jacobian-energy normalization")

# Bochner/Hodge identity, including the full near-Einstein error.
B2, J2, H2, exact2, error = s.symbols("B2 J2 H2 exact2 error", real=True)
energy = (B2+2*J2+error)/2
check((energy-H2).subs(J2, H2+exact2)-(B2/2+exact2+error/2),
      "exact and near-Einstein energy-gap decomposition")

# For the inherited area-preserving shear metrics, dπ is harmonic,
# its Hessian square is shear²/2, and the horizontal Ricci defect
# trace cancels it. This is not an Einstein metric.
shear = s.symbols("shear", real=True)
Phi = s.diag(-shear**2/2, 0, -shear**2/2, shear**2/2)
pullback_target = s.diag(1, 1, 0, 0)
error_density = s.trace(Phi*pullback_target)
check(error_density+shear**2/2, "full horizontal Ricci error")
check(shear**2/4+error_density/2,
      "harmonic-gap cancellation in actual near-Einstein input")

# Algebraic volume/energy inversion: e=(sqrt(v)-sqrt(v-1))²
# is equivalently v=(1+e)²/(4e).
ee = s.symbols("ee", positive=True)
vv = (1+ee)**2/(4*ee)
check(ee**2-2*(2*vv-1)*ee+1, "energy-volume threshold inversion")

# Exact graph-fibre pullback identity in an arbitrary tangent frame:
# DΦ(X,0)=(X, ε df(X)V), hence h_fibre=h+ε²|V|² df⊗df.
ep, f1, f2, v1, v2 = s.symbols("ep f1 f2 v1 v2", real=True)
J = s.Matrix([[1, 0], [0, 1], [ep*v1*f1, ep*v1*f2],
              [ep*v2*f1, ep*v2*f2]])
df = s.Matrix([f1, f2])
graph = J.T*J-s.eye(2)-ep**2*(v1*v1+v2*v2)*(df*df.T)
for i in range(2):
    for k in range(2):
        check(graph[i, k], f"graph-fibre induced metric ({i},{k})")

print("All exact checks passed; analytic, group-compactness and gluing arguments are in the note.")

"""
Step 79: linearize Ozuch's first obstruction under a scale-dependent tilt.

For the product block R = diag(Lambda,0,0) on Lambda^+ and an in-kernel
base direction zeta0=omega_2, compute D_phi lambda at zeta0 on the unit sphere.
This shows which second-order components can be cancelled by a tilt
phi(t)=phi0+t psi+o(t), so mu_2,mu_3 are not independent yes/no verdicts.

The convention follows Ozuch lines 652-654 and 706:
  lambda_k(phi) = c < R phi, phi_(k) >
in an adapted orthonormal frame phi_(1)=phi, phi_(2), phi_(3).
At phi0=e2 we use adapted basis (e2, e1, e3), so component 2 is the out-of-kernel
direction and component 3 is the in-kernel tangent direction.
"""

import json
import sympy as sp

# Symbols
Lam, eps, a, b, cst = sp.symbols('Lambda eps a b c', nonzero=True)

# Fixed product curvature block in original basis (e1,e2,e3)=(omega1,omega2,omega3).
R = sp.diag(Lam, 0, 0)
e1 = sp.Matrix([1, 0, 0])
e2 = sp.Matrix([0, 1, 0])
e3 = sp.Matrix([0, 0, 1])

# Unit direction tilted from e2 toward a e1 + b e3. Normalize to order eps^2.
v = e2 + eps * (a*e1 + b*e3)
phi = sp.simplify(v / sp.sqrt((v.T*v)[0]))

# Build a smooth adapted orthonormal frame to first/second order by Gram-Schmidt.
# Out-of-kernel frame vector starts at e1 and is orthogonalized against phi.
w2 = e1 - (e1.T*phi)[0] * phi
phi2 = sp.simplify(w2 / sp.sqrt((w2.T*w2)[0]))
# Remaining frame starts at e3 and is orthogonalized against phi and phi2.
w3 = e3 - (e3.T*phi)[0] * phi - (e3.T*phi2)[0] * phi2
phi3 = sp.simplify(w3 / sp.sqrt((w3.T*w3)[0]))

basis = [phi, phi2, phi3]
lambdas = [sp.simplify(cst * (phi.T * R * bk)[0]) for bk in basis]
series = [sp.series(expr, eps, 0, 4).removeO().expand() for expr in lambdas]
linear = [sp.diff(expr, eps).subs(eps, 0).simplify() for expr in lambdas]
quadratic = [sp.diff(expr, eps, 2).subs(eps, 0).simplify()/2 for expr in lambdas]

# Solve the order-t^2 reduced equation Dlambda(psi)+mu=0 symbolically.
mu1, mu2, mu3 = sp.symbols('mu1 mu2 mu3')
D = sp.Matrix(linear)  # linear map from scalar a,b through symbolic expressions
# Equations: [0, c Lambda a, 0] + [mu1, mu2, mu3]=0
solution_for_a = sp.solve(sp.Eq(linear[1] + mu2, 0), a)

# If mu1=0 by determinant, only mu2 is cancellable; mu3 remains.
results = {
    "step": 79,
    "purpose": "linearize first obstruction lambda under scale-dependent tilt from ker R",
    "curvature_block": "R=diag(Lambda,0,0) in (omega1,omega2,omega3)",
    "base_direction": "phi0=omega2; adapted frame at phi0: (phi1,phi2,phi3)=(omega2,omega1,omega3)",
    "tilt": "phi(eps)=normalize(omega2 + eps*(a omega1 + b omega3))",
    "lambda_series_to_order_eps3": [str(s) for s in series],
    "D_phi_lambda_at_phi0": [str(x) for x in linear],
    "quadratic_terms": [str(x) for x in quadratic],
    "rank": {
        "variables": ["a (out-of-kernel tilt toward omega1)", "b (in-kernel rotation toward omega3)"],
        "image": "span of obstruction component k=2 only, with Dlambda_2=c*Lambda*a",
        "rank_over_nonzero_Lambda": 1,
        "kernel_direction": "b is the in-kernel SO(2) rotation; it does not change lambda to first order",
    },
    "reduced_second_order_equation": {
        "expansion": "If phi(t)=phi0+t*(a omega1+b omega3)+o(t), then t*lambda(phi(t))+t^2*mu(phi0)=t^2*(Dlambda(a,b)+mu)+o(t^2).",
        "mu1": "not cancellable by first-order tilt; for product rank-one block mu1=0 by Ozuch Lemma 2.14 determinant formula in the adapted basis",
        "mu2": "cancellable by choosing a=-mu2/(c*Lambda)",
        "mu3": "surviving compatibility component in coker(Dlambda), unless an additional admissible variable changes it",
        "solution_a_for_mu2": [str(s) for s in solution_for_a],
    },
    "scientific_consequence": "The coefficient computation should output a required out-of-kernel tilt and a residual compatibility condition, not a two-number existence verdict mu2=mu3=0.",
}

print(json.dumps(results, indent=2))
out = "Sessions/S0910A01/workspace/data/step79_tilt_linearization.json"
with open(out, "w") as f:
    json.dump(results, f, indent=2)
print(f"Wrote {out}")

"""Exact chiral-connection verification for the rational Bianchi-VIII AKE metric.

All calculations take place in Q(p,y)/(y^2-(3p-1)(3p+1)(3p^2+1)).
The script checks the Cartan connection identities proposed after Step 58,
derives the three W^+ eigenvalues, and verifies the eta and W_3^+ norm
profiles used in the radial integral identities.
"""
import json
import os
import sympy as s

p, y = s.symbols("p y", positive=True)
D = (3*p - 1)*(3*p + 1)*(3*p**2 + 1)
c = (1-p)*(1+p)/(2*(3*p**2+1))


def red(expr):
    """Reduce a rational expression modulo y^2-D."""
    expr = s.cancel(s.together(expr))
    num, den = s.fraction(expr)
    modulus = s.Poly(y**2-D, y)
    num = s.rem(s.Poly(s.expand(num), y), modulus).as_expr()
    den = s.rem(s.Poly(s.expand(den), y), modulus).as_expr()
    pp = s.Poly(den, y)
    a, b = pp.nth(0), pp.nth(1)
    if b != 0:
        num = s.expand(num*(a-b*y))
        den = s.expand(a*a-b*b*D)
        num = s.rem(s.Poly(num, y), modulus).as_expr()
    return s.factor(s.cancel(num/den))


def Dt(expr):
    """Geodesic derivative along the positive branch y=sqrt(D)."""
    return red(c*y*(s.diff(expr, p) + s.diff(expr, y)*s.diff(D, p)/(2*y)))


h = [
    -y*(3*p**3-9*p**2+3*p-1)/((3*p-1)*(3*p**2+1)**2),
    y*(3*p**3+9*p**2+3*p+1)/((3*p+1)*(3*p**2+1)**2),
    y*(3*p**4+1)/(2*p*(3*p**2+1)**2),
]
W = [
    y*(p-1)/(8*p*(3*p+1)),
    y*(p+1)/(8*p*(3*p-1)),
    -6*p*y*(p-1)*(p+1)/((3*p-1)*(3*p+1)*(3*p**2+1)**2),
]
h = [red(z) for z in h]
W = [red(z) for z in W]

# de^i=h_i e^{0i}+2W_i e^{jk}.  C_i is the spatial connection coefficient.
C = [red(W[(i+1)%3] + W[(i+2)%3] - W[i]) for i in range(3)]
b = [red(h[i]-C[i]) for i in range(3)]
d = [red(h[i]+C[i]) for i in range(3)]

rad_d = [red(Dt(d[i])+h[i]*d[i]-1) for i in range(3)]
tan_d = [red(2*W[i]*d[i]-d[(i+1)%3]*d[(i+2)%3]+1) for i in range(3)]
# Equality of radial and tangential coefficients is the Einstein/chiral block symmetry.
b_match = [red(Dt(b[i])+h[i]*b[i]-(2*W[i]*b[i]+b[(i+1)%3]*b[(i+2)%3])) for i in range(3)]
assert all(z == 0 for z in rad_d+tan_d+b_match)

# In the convention of the accompanying Cartan derivation the non-scalar
# chiral eigenvalues are 1-(b_i'+h_i b_i).
w = [red(1-(Dt(b[i])+h[i]*b[i])) for i in range(3)]
w_expected = [
    -4*(9*p**6-18*p**5-9*p**4-6*p**3+9*p**2-1)/(3*p**2+1)**3,
    -4*(9*p**6+18*p**5-9*p**4+6*p**3+9*p**2-1)/(3*p**2+1)**3,
    8*(9*p**6-9*p**4+9*p**2-1)/(3*p**2+1)**3,
]
assert all(red(w[i]-w_expected[i]) == 0 for i in range(3))
assert red(sum(w)) == 0

X1 = (1-p)**3*(3*p+1)/(16*p**3)
X2 = (1+p)**3*(3*p-1)/(16*p**3)
eta2 = red(2*X1*X2*(w[0]-w[1])**2)
W32 = red((X2*w[0]+X1*w[1]-w[2])**2/2)
eta_expected = -18*(p-1)**3*(p+1)**3*(3*p-1)*(3*p+1)/(3*p**2+1)**4
W3_expected = 81*(p-1)**4*(p+1)**4*(3*p-1)**2*(3*p+1)**2/(2*(3*p**2+1)**6)
assert red(eta2-eta_expected) == 0
assert red(W32-W3_expected) == 0

# The opposite chiral curvature coefficients are exactly (+1,-1), hence
# its trace-free block vanishes pointwise.  Record endpoint spectra too.
out = {
    "radial_d_residuals": [str(z) for z in rad_d],
    "tangential_d_residuals": [str(z) for z in tan_d],
    "b_matching_residuals": [str(z) for z in b_match],
    "C": [str(z) for z in C],
    "b": [str(z) for z in b],
    "d": [str(z) for z in d],
    "Wplus_eigenvalues": [str(s.factor(z)) for z in w],
    "Wplus_trace": str(red(sum(w))),
    "Wplus_limit_p1": [str(s.limit(z, p, 1, dir='-')) for z in w],
    "eta_squared": str(eta2),
    "W3plus_squared": str(W32),
    "opposite_chiral_radial_coefficients": ["1", "1", "1"],
    "opposite_chiral_tangential_coefficients": ["-1", "-1", "-1"],
    "half_conformal_flatness": True,
}
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
outdir = os.path.join(root, "data", "step59")
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, "chiral_exact.json"), "w") as fh:
    json.dump(out, fh, indent=2)
print(json.dumps(out, indent=2))

"""Step 45: Killing moment identity on the exact self-dual Einstein cell.

For a Killing field K on an Einstein four-manifold with W+=0 and Ric^0=0,
    nabla_X (dK)^+ = (s/6) (X ^ K)^+ .
Check on Taub-NUT-AdS (Ric=-g, s=-4) with K = 2 d/dpsi (2pi-periodic, weight-one
Hopf generator; Euler angle psi of period 4pi), frame e0=A dR,e1=B s1,e2=B s2,e3=C s3:
    K^flat = 2 C e3,  dK = a e03 + b e12,  a = 2 (C^2)'/(A C),  b = -2 C^2/B^2,
    (dK)^+ = (a+b)/2 (e03+e12),  |(dK)^+| = |a+b|/sqrt2 .
Predicted radial derivative (proper distance): (|s|/6)|(e0^K)^+| = (2/3)(2C)/sqrt2.
Output: workspace/data/step45/killing_moment_check.json
"""
import json, os
import sympy as sp

R, ell = sp.symbols('R ell', positive=True)
H = 1 + ell / R
out = {}
for name, F in [('TN', sp.Integer(1)), ('TNAdS', 1 + R * (R + 2 * ell) / 3)]:
    A = sp.sqrt(H / F); B = R * sp.sqrt(H); C = ell * sp.sqrt(F / H)
    a = 2 * sp.diff(C**2, R) / (A * C)
    b = -2 * C**2 / B**2
    dKp = sp.simplify((a + b) / sp.sqrt(2))          # signed |(dK)^+|
    lhs = sp.simplify(sp.diff(dKp, R) / A)           # derivative in proper radial distance
    s = 0 if name == 'TN' else -4
    rhs = sp.simplify(sp.Rational(abs(s), 6) * 2 * C / sp.sqrt(2))
    out[name] = dict(dK_plus_norm=str(sp.factor(dKp)), radial_derivative=str(sp.simplify(lhs)),
                     predicted=str(rhs), identity_residual=str(sp.simplify(lhs - rhs)),
                     K_norm=str(sp.simplify(2 * C)),
                     R_where_dKplus_reaches_bolt_value_sqrt2=str(sp.solve(sp.Eq(dKp, sp.sqrt(2)), R)) if name == 'TNAdS' else None)
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'step45')
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, 'killing_moment_check.json'), 'w') as fh:
    json.dump(out, fh, indent=1)
print(json.dumps(out, indent=1))

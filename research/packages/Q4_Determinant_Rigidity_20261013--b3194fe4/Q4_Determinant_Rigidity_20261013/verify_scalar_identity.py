"""Exact polynomial checks for the shifted-Weyl scalar equation.

These checks verify its algebraic substitutions, not elliptic regularity,
maximum principles, or Armstrong's topological theorem.
"""
from __future__ import annotations
import json
from pathlib import Path
import sympy as sp

x, y, z = sp.symbols('x y z', real=True)
a = x + y + z
u = x*y + x*z + y*z
det_A = x*y*z
W = sp.diag(a/3-x, a/3-y, a/3-z)
W2 = sp.trace(W*W)
det_W = W.det()
# Delta u = -1/2 Delta |W|^2, and
# Delta |W|^2 = -s |W|^2 + 36 det W - 2 |nabla W|^2.
# Here s=-4a. We omit the common gradient term in this polynomial check.
lap_u_algebraic = -2*a*W2 - 18*det_W
residuals = {
    'trace_W': sp.trace(W),
    'sigma2_identity': a*a/3 - W2/2 - u,
    'determinant_shift': det_W - (-2*a**3/27 + a*u/3 - det_A),
    'scalar_equation': lap_u_algebraic + 2*a*u - 18*det_A,
    'cubic_trace': sp.trace(W**3) - 3*det_W,
}
for label, expr in residuals.items():
    assert sp.expand(expr) == 0, (label, sp.expand(expr))

# The normalizations at constant-curvature and Kahler--Einstein points.
t = sp.symbols('a', positive=True)
models = {
    'real_hyperbolic': sp.diag(t/3,t/3,t/3),
    'kahler_einstein': sp.diag(t,0,0),
}
model_records = {}
for label, A in models.items():
    u_A = (t*t-sp.trace(A*A))/2
    assert sp.simplify(2*t*u_A-18*A.det()) == 0
    model_records[label] = {'sigma2': str(u_A), 'det_A': str(A.det())}

out = {'polynomial_residuals': {k: '0' for k in residuals},
       'constant_model_checks': model_records,
       'scope': 'Exact algebra only; the geometric proof is in the accompanying TeX.'}
path = Path(__file__).with_name('verification.json')
path.write_text(json.dumps(out, ensure_ascii=False, indent=2)+'\n')
print(json.dumps(out, ensure_ascii=False, indent=2))

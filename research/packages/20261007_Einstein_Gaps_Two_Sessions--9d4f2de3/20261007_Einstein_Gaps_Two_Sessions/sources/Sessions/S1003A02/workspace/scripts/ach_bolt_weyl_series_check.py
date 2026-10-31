"""Numerical coordinate-curvature limit at the validated Einstein bolt using the full
order-6 Fuchsian series, including the free t^4 anisotropy d.

This checks whether the bolt Weyl limits used in Theorem E depend on d and independently
compares the two chiral squared norms with the peer's Cartan computation.  It is a numerical
cross-check; the exact Cartan matrices are in
Sessions/S1003A01/workspace/scripts/ach_bolt_weyl_exact.py.
"""
from pathlib import Path
import sys
import sympy as sp
import jax
import jax.numpy as jnp
jax.config.update("jax_enable_x64", True)

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from ach_bolt_fuchs import series, s as ss, d as dd
from o11_rotated_cell import metric_from, curvature_scalars, ANG

SIG, DEL, GAM = series(6)

def poly_fun(expr, dval):
    p = sp.Poly(sp.expand(expr.subs(dd, sp.Float(dval, 30))), ss)
    coeff = [float(c) for c in reversed(p.all_coeffs())]
    # all_coeffs is descending; reverse gives ascending
    def f(x):
        z = jnp.asarray(0.0, dtype=jnp.float64)
        for c in reversed(coeff):
            z = z*x + c
        return z
    return f

def evaluate(dval, t):
    fs, fd, fg = [poly_fun(e, dval) for e in (SIG, DEL, GAM)]
    b = 4.0/5.0
    def prof(x):
        sig, de, ga = fs(x), fd(x), fg(x)
        A, B, C = b + sig + de/2, b + sig - de/2, 1 + ga
        return x, jnp.diag(jnp.array([A*A, B*B, x*C*C]))
    x = t*t
    vals = curvature_scalars(metric_from(prof), jnp.concatenate([jnp.array([x]), ANG]))
    return [float(v) for v in vals]

if __name__ == "__main__":
    for dval in [0.0, 0.28697953, 0.286999618893, 0.28701987]:
        print("d", dval)
        for t in [1e-2, 5e-3, 2e-3, 1e-3]:
            print(t, evaluate(dval, t))

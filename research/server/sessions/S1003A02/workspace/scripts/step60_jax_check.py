"""Decisive independent check (JAX, orthonormal-frame W+) of the sigma^2 t^2 coefficient of F+ = 4|W+|^2+s^2/12
for g = delta + sig*A + t*(h2 + sig*K) at one point, pure W^- (or Ric^o) jet.  Compares with step59 script's
X1-based value.  Usage: python step60_jax_check.py [Wm|Rz]"""
import sys, os
mode = sys.argv[1] if len(sys.argv) > 1 else 'Wm'
sys.argv = ['x', mode]
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import jax; jax.config.update('jax_enable_x64', True)
import jax.numpy as jnp
import sympy as sp
import step60_corrector_columns as C
from step57_kernel_log_coefficient import density_Fplus_from_jet

pt = (sp.Rational(1), sp.Rational(2, 3), sp.Rational(-1, 2), sp.Rational(3, 5))
def fj(M):
    J0, J1, J2 = C.jets(M, pt)
    return (np.array(J0, dtype=float), np.array(J1, dtype=float), np.array(J2, dtype=float))
Aj = fj(C.A); Hj = fj(C.H)
K0 = sp.Rational(3, 2) * C.sym(C.H * C.A) - sp.Rational(1, 4) * (C.H * C.A).trace() * sp.eye(4)
for lab, Kj in [('K=0', None), ('k0W', fj(K0))]:
    if Kj is None: Kj = tuple(np.zeros_like(a) for a in Aj)
    def F(sig, t):
        g = jnp.eye(4) + sig * Aj[0] + t * (Hj[0] + sig * Kj[0])
        dg = sig * Aj[1] + t * (Hj[1] + sig * Kj[1])
        ddg = sig * Aj[2] + t * (Hj[2] + sig * Kj[2])
        return density_Fplus_from_jet(g, dg, ddg)[0]
    d = jax.grad(jax.grad(jax.grad(jax.grad(F, 0), 0), 1), 1)(0., 0.) / 4.0
    # script value
    Ajs = C.jets(C.A, pt); Hjs = C.jets(C.H, pt)
    Y, dens = C.Yvec(Ajs, Hjs, None if lab == 'K=0' else C.jets(K0, pt))
    X1 = np.array(Y[:36], dtype=float).reshape(6, 6); s1 = float(Y[36])
    print(lab, 'JAX sig^2 t^2 coeff =', float(d), ' script signed =', float(dens),
          ' script |X1|_F version =', 4 * np.sum(X1 * X1) + s1 ** 2 / 12, ' sym-only =',
          4 * np.sum(((X1 + X1.T) / 2) ** 2) + s1 ** 2 / 12)

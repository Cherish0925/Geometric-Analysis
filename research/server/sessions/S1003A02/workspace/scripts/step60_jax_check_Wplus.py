"""JAX vs exact-script sigma^2 t^2 density at a point, in the (s, W+) sector (X0 != 0), K = 0 and an invariant K."""
import sys, os
sys.argv = ['x', 'Wm']
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import jax; jax.config.update('jax_enable_x64', True)
import jax.numpy as jnp
import sympy as sp
import step60_corrector_columns as C
from step59_exact_log_coefficient import riemann_from_ops, h2_field, density_sig2, invariant_K
from step57_kernel_log_coefficient import density_Fplus_from_jet

Z3 = sp.zeros(3, 3)
R = riemann_from_ops(sp.Matrix([[2, 0, 0], [0, -3, 1], [0, 1, 1]]), Z3, -24, Z3)
H = h2_field(R)
Kinv = invariant_K([sp.Rational(v, 7) for v in (3, 1, -2, 0, 5, 1, 0, -1, 2, 4)])
pt = (sp.Rational(1), sp.Rational(2, 3), sp.Rational(-1, 2), sp.Rational(3, 5))
for lab, K in [('K=0', sp.zeros(4, 4)), ('Kinv', Kinv)]:
    Aj = C.jets(C.A, pt); Hj = C.jets(H, pt); Kj = C.jets(K, pt)
    sig = sp.Symbol('sig')
    Pj = [[[Hj[0][i][j] + sig * Kj[0][i][j] for j in range(4)] for i in range(4)],
          [[[Hj[1][i][j][k] + sig * Kj[1][i][j][k] for k in range(4)] for j in range(4)] for i in range(4)],
          [[[[Hj[2][i][j][k][l] + sig * Kj[2][i][j][k][l] for l in range(4)] for k in range(4)] for j in range(4)]
           for i in range(4)]]
    dens, spr = density_sig2(Aj, Pj)
    f = lambda J: tuple(np.array(x, dtype=float) for x in J)
    a, hh, kk = f(Aj), f(Hj), f(Kj)
    def F(s_, t):
        g = jnp.eye(4) + s_ * a[0] + t * (hh[0] + s_ * kk[0])
        return density_Fplus_from_jet(g, s_ * a[1] + t * (hh[1] + s_ * kk[1]), s_ * a[2] + t * (hh[2] + s_ * kk[2]))[0]
    d22 = jax.grad(jax.grad(jax.grad(jax.grad(F, 0), 0), 1), 1)(0., 0.) / 4.0
    d02 = jax.grad(jax.grad(F, 1), 1)(0., 0.) / 2.0
    print(lab, 'JAX s^2t^2', float(d22), ' script', float(dens.coef(2, 0)), '| JAX t^2', float(d02), ' script',
          float(dens.coef(0, 0)))

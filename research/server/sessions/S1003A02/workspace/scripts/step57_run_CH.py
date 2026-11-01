import sys, os, json, time
import numpy as np
import jax, jax.numpy as jnp
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from step57_kernel_log_coefficient import *

nu_pts = int(sys.argv[1]) if len(sys.argv) > 1 else 8
nphi = int(sys.argv[2]) if len(sys.argv) > 2 else 24
Ds = [int(a) for a in sys.argv[3].split(',')] if len(sys.argv) > 3 else [2]
t0 = time.time()
X, W = s3_quadrature(nu_pts, nphi)
print('quad points', X.shape[0], 'vol/2pi^2', float(W.sum()) / (2 * np.pi ** 2))
EIGHTPI2 = 8 * np.pi ** 2
out = {}
for Jname, J in [('CH_perp_J2', J2), ('CH_parallel_Jz', Jz)]:
    Bf = ddbar_metric(lambda y: 0.5 * jnp.dot(y, y) ** 2, J)
    Cf = ddbar_metric(lambda y: jnp.dot(y, y) ** 3 / 3, J)
    inv = invariant_K_basis()
    fields = [K for _, K in inv]
    c1, c2, b, Q = run_background(Bf, Cf, X, W, fields, Jname)
    c0 = (c1 + c2) / EIGHTPI2
    val, leak, kap, nk = minimise(c0, b / EIGHTPI2, Q / EIGHTPI2)
    print(Jname, 'c_AABB', c1 / EIGHTPI2, 'c_AAC', c2 / EIGHTPI2, 'F(K=0)', c0, 'min_inv', val, 'leak', leak, 'ker', nk,
          'time', time.time() - t0)
    print('  kappa', dict(zip([str(n) for n, _ in inv], np.round(kap, 6))))
    out[Jname] = dict(c_AABB=c1 / EIGHTPI2, c_AAC=c2 / EIGHTPI2, F0=c0, min_inv=val, leak=leak)
    for D in Ds:
        basis = make_K_basis(D)
        fields = [K_field(E, m, D) for E, m in basis]
        c1, c2, b, Q = run_background(Bf, Cf, X, W, fields, Jname)
        val, leak, kap, nk = minimise(c0, b / EIGHTPI2, Q / EIGHTPI2)
        print(Jname, 'D', D, 'nK', len(fields), 'min', val, 'leak', leak, 'ker', nk, 'time', time.time() - t0)
        out[Jname]['min_D%d' % D] = val
        out[Jname]['leak_D%d' % D] = leak
print(json.dumps(out, indent=1))

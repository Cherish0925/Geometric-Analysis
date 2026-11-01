"""
Step 58: independent geometric test of Theorem 57.Phi on product backgrounds Sigma_1(K1) x Sigma_2(K2).

Background jets are taken from conformal coordinates of constant-curvature surfaces,
    g_i = (1 + K_i rho^2/4)^{-2} |dz_i|^2 = (1 - K_i rho^2/2 + 3 K_i^2 rho^4/16 + ...) |dz_i|^2,
NOT normal coordinates, and C (quartic part) is nonzero.  This is independent of the 20x20 general-form
parametrisation of step57_general_form.py.

Burns tail: Kahler form zeta = (e12+e34)/sqrt2 (coordinates x1,y1,x2,y2).
  layout 'par' : factors in planes (x1,y1),(x2,y2): product Kahler form = zeta  -> R+ = diag(s/4,0,0), mu1 = s/4
  layout 'perp': factors in planes (x1,x2),(y1,y2) with the second factor oriented so that its Kahler form
                 e13 - e24 is self-dual: zeta is in the kernel of R+, mu = (0, s/4, 0)
Prediction (57.Phi): Phi = -mu1(mu1-mu2-mu3)/2 - (mu2-mu3)^2/2 = -s^2/32 in both layouts, s = 2(K1+K2),
independent of Ric deg = (K1-K2)/2 * (g1 - g2) and of W^-.
usage: python step58_product_tests.py K1 K2 layout D nu nphi
"""
import sys, os, json, time
import numpy as np
import jax, jax.numpy as jnp
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from step57_kernel_log_coefficient import *

K1 = float(sys.argv[1]); K2 = float(sys.argv[2]); layout = sys.argv[3]
D = int(sys.argv[4]) if len(sys.argv) > 4 else 4
nu_pts = int(sys.argv[5]) if len(sys.argv) > 5 else 8
nphi = int(sys.argv[6]) if len(sys.argv) > 6 else 24
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, '..', 'data', 'step58_products', 'step58_product_%s_K%g_K%g_D%d_q%d_%d.json' % (layout, K1, K2, D, nu_pts, nphi))
E8 = 8 * np.pi ** 2
t0 = time.time()

if layout == 'par':
    P1, P2 = (0, 1), (2, 3)
elif layout == 'perp':
    P1, P2 = (0, 2), (1, 3)
else:
    raise SystemExit('layout par|perp')

def proj(P):
    m = np.zeros((4, 4)); m[P[0], P[0]] = m[P[1], P[1]] = 1; return jnp.array(m)
E1, E2 = proj(P1), proj(P2)

def Bf(x):
    r1 = x[P1[0]] ** 2 + x[P1[1]] ** 2; r2 = x[P2[0]] ** 2 + x[P2[1]] ** 2
    return -0.5 * K1 * r1 * E1 - 0.5 * K2 * r2 * E2
def Cf(x):
    r1 = x[P1[0]] ** 2 + x[P1[1]] ** 2; r2 = x[P2[0]] ** 2 + x[P2[1]] ** 2
    return 3. / 16 * K1 ** 2 * r1 ** 2 * E1 + 3. / 16 * K2 ** 2 * r2 ** 2 * E2

# sanity: scalar curvature of delta + B + C at origin
gfull = lambda x: jnp.eye(4) + Bf(x) + Cf(x)
_, Ric, s = density_from_jet(*jet(gfull, jnp.zeros(4)))
print('s(0) =', float(s), 'expected', 2 * (K1 + K2), 'Ric diag', np.round(np.diag(np.array(Ric)), 10))

X, W = s3_quadrature(nu_pts, nphi)
basis = make_K_basis(D)
fields = [K_field(E, m, D) for E, m in basis]
c1, c2, b, Q = run_background(Bf, Cf, X, W, fields, layout)
c0 = (c1 + c2) / E8
val, leak, kap, nk = minimise(c0, b / E8, Q / E8)
sc = 2 * (K1 + K2)
pred = -sc ** 2 / 32
res = dict(K1=K1, K2=K2, layout=layout, D=D, nu=nu_pts, nphi=nphi, nK=len(fields), s=sc,
           c_AABB=c1 / E8, c_AAC=c2 / E8, F_K0=c0, Phi=val, leak=leak, ker=nk, Phi_pred=pred,
           err=val - pred, time=time.time() - t0)
print(json.dumps(res, indent=1))
json.dump(res, open(OUT, 'w'), indent=1)

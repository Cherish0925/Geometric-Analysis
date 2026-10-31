"""JAX version of the U(2) cell optimisation with exact gradients.
Same parametrisation as u2_cell_opt.py (Kahler optimum times exp(phi p_i)),
plus optional radius-dependent extra freedom.  Usage:
  python u2_cell_jax.py x0 X deg [nq]
Prints JSON with P/(8pi^2) for the Kahler optimum and the non-Kahler minimum,
and kappa_est = (P-1)/x0.
"""
import sys, os, json
os.environ.setdefault('XLA_FLAGS', '--xla_force_host_platform_device_count=1')
import jax, jax.numpy as jnp
jax.config.update('jax_enable_x64', True)
import numpy as np
import sympy as sp
from scipy.optimize import minimize
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import u2_xcoord as UX

args = (UX.x, UX.F, UX.F1, UX.F2, UX.G, UX.G1)
ric0f = sp.lambdify(args, UX.exprs['ric0sq'], modules=jnp)
sf = sp.lambdify(args, UX.exprs['s'], modules=jnp)
wpf = sp.lambdify(args, UX.exprs['wpsq_c'], modules=jnp)
wmf = sp.lambdify(args, UX.exprs['wmsq_c'], modules=jnp)

def chebvals(n, z):
    T = [jnp.ones_like(z), z]
    for k in range(2, n):
        T.append(2*z*T[-1] - T[-2])
    return jnp.stack(T[:n])

def setup(x0, X, nq):
    e, w = np.polynomial.legendre.leggauss(nq)
    eta = 0.5*(e+1); weta = 0.5*w
    xi = eta**2; dxi = 2*eta*weta
    L = X - x0
    xx = x0 + L*xi
    M = np.array([[x0**3/4, -0.5, x0**2, 1/x0], [3*x0**2/4, 0, 2*x0, -1/x0**2],
                  [X**3/4, -0.5, X**2, 1/X], [3*X**2/4, 0, 2*X, -1/X**2]])
    c1, c2, al, be = np.linalg.solve(M, np.array([-x0, 0, X**2, 2*X]))
    K = xx + c1*xx**3/4 - c2/2 + al*xx**2 + be/xx
    K1 = 1 + 3*c1*xx**2/4 + 2*al*xx - be/xx**2
    K2 = 6*c1*xx/4 + 2*al + 2*be/xx**3
    return dict(xi=jnp.array(xi), xx=jnp.array(xx), wx=jnp.array(dxi*L), L=L, K=(jnp.array(K), jnp.array(K1), jnp.array(K2)))

def make_cost(geo, deg):
    xi, xx, wx, L = geo['xi'], geo['xx'], geo['wx'], geo['L']
    K, K1, K2 = geo['K']
    z = 2*xi - 1
    # polynomial basis and its x-derivatives (via autodiff in xi)
    def basis(xiv):
        return chebvals(deg, 2*xiv - 1)
    B = basis(xi)
    dB = jax.vmap(jax.jacfwd(basis))(xi).T / L       # d/dx
    ddB = jax.vmap(jax.jacfwd(jax.jacfwd(basis)))(xi).T / L**2
    phi = (1 - xi)**3; phi1 = -3*(1 - xi)**2/L; phi2 = 6*(1 - xi)/L**2
    B0m1 = basis(jnp.array(0.0))   # value at xi=0 (bolt)
    def fieldsF(c):
        p = c @ B; p1 = c @ dB; p2 = c @ ddB
        q = phi*p; q1 = phi1*p + phi*p1; q2 = phi2*p + 2*phi1*p1 + phi*p2
        E = jnp.exp(q)
        return K*E, (K1 + K*q1)*E, (K2 + 2*K1*q1 + K*(q2 + q1**2))*E
    def unpack(zv):
        c1 = zv[:deg]
        c2 = zv[deg:]
        # bolt regularity: p1(0)+p2(0)=0 -> shift constant of c2
        shift = -(c1 @ B0m1 + c2 @ B0m1)
        c2 = c2.at[0].add(shift)
        return c1, c2
    def pieces(zv):
        c1, c2 = unpack(zv)
        F, F1, F2 = fieldsF(c1)
        G, G1, _ = fieldsF(c2)
        dv = jnp.pi**2*xx*jnp.sqrt(F/G)*wx
        return F, F1, F2, G, G1, dv
    def cost(zv):
        F, F1, F2, G, G1, dv = pieces(zv)
        return jnp.sum(ric0f(xx, F, F1, F2, G, G1)*dv)/(8*jnp.pi**2)
    def extras(zv):
        F, F1, F2, G, G1, dv = pieces(zv)
        s = sf(xx, F, F1, F2, G, G1); wp = wpf(xx, F, F1, F2, G, G1); wm = wmf(xx, F, F1, F2, G, G1)
        return dict(S=float(jnp.sum(s**2*dv)), Wp=float(jnp.sum(wp*dv)), Wm=float(jnp.sum(wm*dv)),
                    Fcell=float(jnp.sum((s**2/12 + 4*wp)*dv)), minF=float(F.min()), minG=float(G.min()))
    return jax.jit(cost), jax.jit(jax.grad(cost)), extras

def run(x0, X, deg, nq=800, z0=None):
    geo = setup(x0, X, nq)
    cost, grad, extras = make_cost(geo, deg)
    if z0 is None:
        z0 = np.zeros(2*deg)
    f = lambda z: float(cost(jnp.array(z)))
    g = lambda z: np.array(grad(jnp.array(z)))
    P0 = f(np.zeros(2*deg))
    res = minimize(f, z0, jac=g, method='L-BFGS-B', options=dict(maxiter=20000, ftol=1e-15, gtol=1e-12))
    ex = extras(jnp.array(res.x))
    Fball = 144*np.pi**2*X**2/2
    return dict(x0=x0, X=X, deg=deg, nq=nq, P_kahler=P0, P_min=res.fun, kappa_est=(res.fun - 1)/x0,
                identity_check=(res.fun - 1) - (ex['Fcell'] - Fball)/(8*np.pi**2), msg=str(res.message),
                minF=ex['minF'], minG=ex['minG']), res.x

if __name__ == '__main__':
    x0 = float(sys.argv[1]); X = float(sys.argv[2]); deg = int(sys.argv[3])
    nq = int(sys.argv[4]) if len(sys.argv) > 4 else 800
    out, z = run(x0, X, deg, nq)
    print(json.dumps(out))
    here = os.path.dirname(os.path.abspath(__file__))
    np.save(os.path.join(here, '..', 'data', f'u2jax_x0{x0}_X{X}_deg{deg}.npy'), z)

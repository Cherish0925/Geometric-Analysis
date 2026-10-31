"""Small Burns cells in a complex-space-form bulk of either scalar sign.

The U(2)-invariant aligned ansatz is
    g = dx^2/(4K) + x((s1)^2+(s2)^2) + K(s3)^2.
The complex-space-form collar is K_bulk=x+kappa*x^2, with scalar
s=-24*kappa in the conventions of o11_rotated_cell.py.  kappa=+1 is
complex hyperbolic and kappa=-1 is Fubini--Study (on X<1).

K is the four-constant extremal interpolation used by the existing cell
code, now with signed outer curvature.  We then allow the same compactly
supported U(2) profile variations as Cell.  The quantity printed as P is
int |Ric^0|^2/(8*pi^2); the Einstein bulk ball has zero P, so the predicted
universal aligned response is
    P = 1 + 6*kappa*x0 + O(x0^2)
      = 1 - x0 R^+(omega,omega) + O(x0^2).
"""
import sys, json, time
import numpy as np
import jax, jax.numpy as jnp
jax.config.update('jax_enable_x64', True)
from scipy.optimize import minimize
from o11_rotated_cell import Cell, PI


def kahler_K_signed(x0, X, kappa):
    M = np.array([
        [x0**3/4, -0.5, x0**2, 1/x0],
        [3*x0**2/4, 0, 2*x0, -1/x0**2],
        [X**3/4, -0.5, X**2, 1/X],
        [3*X**2/4, 0, 2*X, -1/X**2],
    ])
    rhs = np.array([-x0, 0.0, kappa*X**2, 2*kappa*X])
    c1, c2, al, be = np.linalg.solve(M, rhs)
    return lambda x: x + c1*x**3/4 - c2/2 + al*x**2 + be/x


def run(x0, X, kappa, deg=8, nq=500):
    K = kahler_K_signed(x0, X, kappa)
    c = Cell(x0, X, deg, 0, 0, 0.05, nq, K=K)
    z0 = np.zeros(c.nparam)
    # At theta=0, w and rotation sectors are absent.  P itself needs no
    # background subtraction because the complex-space-form bulk is Einstein.
    Pf = jax.jit(lambda z: c.P(z, 0.0))
    gf = jax.jit(jax.grad(lambda z: c.P(z, 0.0)))
    t0 = time.time()
    res = minimize(lambda z: float(Pf(jnp.array(z))), z0,
                   jac=lambda z: np.array(gf(jnp.array(z))), method='L-BFGS-B',
                   options=dict(maxiter=5000, ftol=1e-15, gtol=1e-11, maxls=80))
    zz = jnp.array(res.x)
    # Independent direct integrals; do not use Cell.report because that routine
    # subtracts the hard-coded CH scalar/Weyl ball.
    s, r0, wa, wb, dv = c.fields(zz, 0.0)
    wt = c.wx*dv
    P = float(jnp.sum(r0*wt))/(8*PI**2)
    S = float(jnp.sum(s*s*wt))/(8*PI**2)
    WA = float(jnp.sum(wa*wt))/(8*PI**2)
    WB = float(jnp.sum(wb*wt))/(8*PI**2)
    xx = np.geomspace(x0, X, 2000)
    kval = np.array([K(float(x)) for x in xx])
    return dict(x0=x0, X=X, kappa=kappa, scalar_bulk=-24*kappa,
                Rplus_omega=-6*kappa, deg=deg, nq=nq, P=P,
                slope=(P-1)/x0, predicted_slope=6*kappa,
                S_over_8pi2=S, WA_over_8pi2=WA, WB_over_8pi2=WB,
                min_K=float(kval.min()), msg=str(res.message), nit=int(res.nit),
                grad_inf=float(np.max(np.abs(res.jac))), z=[float(v) for v in res.x],
                sec=time.time()-t0)


if __name__ == '__main__':
    x0 = float(sys.argv[1]); X = float(sys.argv[2]); kappa = float(sys.argv[3])
    deg = int(sys.argv[4]) if len(sys.argv)>4 else 8
    nq = int(sys.argv[5]) if len(sys.argv)>5 else 500
    print(json.dumps(run(x0, X, kappa, deg, nq)))

"""Perpendicular CH cell with an explicit far-field antisymmetric Einstein 'mass-mode' tail.

Base: the fixed-slot perpendicular DualCell profile (bolt smooth, exact CH collar at X, third-order
contact).  Added: the exact x-gauge linear antisymmetric Einstein mode of CH (scripts/
ch_linear_mode_solve.py, check_xgauge_mass_mode.py), truncated with an analytically chosen shape:
    v_- = c f_-(x) h(x^2/X^2),   h(y)=(1-y)^4(1+4y),   f_-=x/(1+x)^{5/2},
    theta_t(x) = -(1/(2k)) int_x^X f_-^2 h ds,  k=(x/(1+x))^2,
    Theta = c chi(x) theta_t(x),   chi = C^3 step in log x from x_a to x_b,
    F -> F e^{-2Theta},  w -> w - Theta(1+2x)/(1+x),  G -> G + Theta x + 2x^2(1+x)Theta'.
Theta = 0 near the bolt, and Theta vanishes to order >=4 at X, so bolt smoothness, exact collar and
third-order contact are preserved.  The last entry of z is the tail amplitude c.

Predicted optimal truncation cost of the tail (8 pi^2 units, linear theory): about c^2/(2X^2)*int h'^2
= 0.79 c^2/X^2 for this h; the ideal infinite-collar tail costs zero.

Usage: python perp_tail_cell.py SEED X DEG OUT [--c0 -0.9] [--xa 0.5 --xb 4] [--nq 1400]
"""
import argparse, json, math, time
from pathlib import Path
import numpy as np
import jax, jax.numpy as jnp
jax.config.update('jax_enable_x64', True)
from scipy.optimize import minimize
from perp_dual_cost import DualCell, load_record
from perp_collar_continue import physical_extension_seed

GL_T, GL_W = np.polynomial.legendre.leggauss(64)
GL_T = jnp.asarray(0.5*(GL_T+1)); GL_W = jnp.asarray(0.5*GL_W)


def step7(t):
    t = jnp.clip(t, 0.0, 1.0)
    return t**4*(35 - 84*t + 70*t**2 - 20*t**3)


class TailCell(DualCell):
    def setup_tail(self, xa, xb):
        self.xa, self.xb = xa, xb
        self.nparam_base = self.nparam
        self.nparam = self.nparam + 1

    def theta_t(self, x):
        X = self.X
        L = jnp.log(X/x)
        s = x*jnp.exp(L*GL_T)
        y = (s/X)**2
        integrand = s**2/(1+s)**5*(1-y)**4*(1+4*y)*s*L
        I = jnp.sum(GL_W*integrand)
        k = (x/(1+x))**2
        return -I/(2*k)

    def Theta(self, x, c):
        chi = step7((jnp.log(x) - math.log(self.xa))/(math.log(self.xb) - math.log(self.xa)))
        return c*chi*self.theta_t(x)

    def prof_factory(self, z):
        base = DualCell.prof_factory(self, z[:self.nparam_base])
        c = z[self.nparam_base]
        def prof(x):
            G, h = base(x)
            F = h[0, 0]; w = jnp.log(h[2, 2]/x)
            Th = self.Theta(x, c)
            dTh = jax.grad(lambda xx: self.Theta(xx, c))(x)
            Fn = F*jnp.exp(-2*Th)
            wn = w - Th*(1+2*x)/(1+x)
            Gn = G + Th*x + 2*x*x*(1+x)*dTh
            return Gn, jnp.diag(jnp.array([Fn, x, x*jnp.exp(wn)]))
        return prof


def stripped_seed(old, cell, c0, deg, ns=5000):
    """Project (old profile extended by exact CH) MINUS the linear tail c0*Theta onto the base basis,
    so that the polynomial part does not double count the far field carried by the explicit tail."""
    from numpy.polynomial.chebyshev import chebvander
    from perp_collar_continue import old_profile, smooth
    x0 = cell.x0; Xn = cell.X; ell = math.log(Xn/x0); Xold = float(old['X'])
    un = np.linspace(1e-5, 1-1e-5, ns); x = x0*np.exp(ell*un)
    F = np.empty(ns); G = np.empty(ns); w = np.empty(ns); m = x < Xold
    F[m], G[m], w[m] = old_profile(old, x[m])
    F[~m] = x[~m]; G[~m] = x[~m]+x[~m]**2; w[~m] = np.log1p(x[~m])
    Th = np.asarray(jax.vmap(lambda xx: cell.Theta(xx, c0))(jnp.asarray(x)))
    dTh = np.asarray(jax.vmap(jax.grad(lambda xx: cell.Theta(xx, c0)))(jnp.asarray(x)))
    F = F*np.exp(2*Th); w = w + Th*(1+2*x)/(1+x); G = G - Th*x - 2*x*x*(1+x)*dTh
    S = smooth(un); om3 = (1-un)**3
    qF = np.log(np.maximum((F-x0*S)/(x-x0), 1e-300)); qG = np.log(np.maximum(G/((x-x0)+(x*x+x0)*S), 1e-300))
    wr = w - np.log1p(x)*S
    V = chebvander(2*un-1, deg-1); good = un < .995
    W = 1 + 2*np.exp(-(un/.06)**2)
    def ls(y, den):
        A = V[good]*np.sqrt(W[good, None]); b = (y/den)[good]*np.sqrt(W[good])
        return np.linalg.lstsq(A, b, rcond=1e-12)[0]
    return np.r_[ls(qF, om3), ls(qG, om3), ls(wr, un*un*om3), c0]


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('seed'); ap.add_argument('X', type=float)
    ap.add_argument('deg', type=int); ap.add_argument('out')
    ap.add_argument('--c0', type=float, default=0.0); ap.add_argument('--xa', type=float, default=0.5)
    ap.add_argument('--xb', type=float, default=4.0); ap.add_argument('--nq', type=int, default=1400)
    ap.add_argument('--maxiter', type=int, default=4000); ap.add_argument('--target', default='J')
    ap.add_argument('--strip', action='store_true')
    a = ap.parse_args()
    old = load_record(a.seed); x0 = float(old['x0'])
    c = TailCell(x0, a.X, a.deg, a.deg, a.nq); c.aligned = False; c.wpow = 2; c.setup_tail(a.xa, a.xb)
    if a.strip:
        z0 = stripped_seed(old, c, a.c0, a.deg)
    elif 'c_tail' in old and float(old['X']) == a.X and int(old['deg']) == a.deg:
        z0 = np.asarray(old['z'], float)
        if a.c0 != 0.0: z0[-1] = a.c0
    elif float(old['X']) == a.X and int(old['deg']) == a.deg:
        z0 = np.r_[np.asarray(old['z'], float), a.c0]
    else:
        zb, _ = physical_extension_seed(old, a.X, a.deg); z0 = np.r_[zb, a.c0]
    fun = jax.jit(lambda z: c.target(z, a.target)); grad = jax.jit(jax.grad(lambda z: c.target(z, a.target)))
    p0, j0, q0 = [float(v) for v in c.costs(jnp.asarray(z0))]
    print('seed', dict(P=p0, J=j0, c=float(z0[-1])), flush=True)
    t = time.time()
    res = minimize(lambda z: float(fun(jnp.asarray(z))), z0, jac=lambda z: np.asarray(grad(jnp.asarray(z))),
                   method='L-BFGS-B', options=dict(maxiter=a.maxiter, ftol=1e-16, gtol=1e-12, maxls=80))
    p, j, q = [float(v) for v in c.costs(jnp.asarray(res.x))]
    out = dict(x0=x0, X=a.X, deg=a.deg, target=a.target, nq=a.nq, P=p, J=j, scalar=q, c_tail=float(res.x[-1]),
               xa=a.xa, xb=a.xb, source=a.seed, seed_costs=dict(P=p0, J=j0), success=bool(res.success),
               message=str(res.message), nit=int(res.nit), grad_inf=float(np.max(np.abs(res.jac))),
               z=[float(v) for v in res.x], sec=time.time()-t)
    print(json.dumps({k: v for k, v in out.items() if k != 'z'})); Path(a.out).write_text(json.dumps(out)+'\n')

if __name__ == '__main__': main()

"""General U(2)-invariant (biaxial, a=b) blow-up cells in a signed space-form bulk.

Metric:  g = dx^2/(4G) + x(s1^2+s2^2) + F s3^2,   d s_i = 2 s_j^s_k, int s_123 = 2 pi^2.
Kaehler iff F = G.  Bolt at x0: F(x0)=G(x0)=0, F'(x0)G'(x0)=1 (ordinary O(-1) bolt).
Bulk collars (all Einstein with Ric = lam g):
   'CSF' : F = G = x + k x^2          lam = -6k  (k=+1 complex hyperbolic, k=-1 Fubini-Study)
   'RSF' : F = x, G = x + 2k x^2      lam = -6k  (k=+1 real hyperbolic H^4, k=-1 round S^4)
The RSF identification is verified symbolically below (Ric = lam g).
Profile:  F = Fb(x) [1 - (x0/x)(1 - sig(u))] exp(qF),  G likewise with Gb, qG, where
u = log(x/x0)/log(X/x0), sig = smoothstep(u) with sig'(0)=sig'(1)=0, q = (1-u)^2 * Chebyshev series,
and the constant term of qG is fixed by F'(x0)G'(x0)=1.  F,G are C^1 at X (densities contain only
second derivatives, so no singular contribution arises at the junction).
Energies (normalized by 8 pi^2):  P = int |Ric0|^2,  J = P + (1/4) int (s-4 lam)^2.
Usage: python u2_general_cell.py bulk k x0 X deg target [nq] [out.json]
"""
import sys, json, time
from pathlib import Path
import numpy as np
import sympy as sp
import jax, jax.numpy as jnp
jax.config.update('jax_enable_x64', True)
from scipy.optimize import minimize

xs = sp.symbols('x', positive=True)
F0, F1, F2, G0, G1 = sp.symbols('F0 F1 F2 G0 G1')


def symbolic_densities():
    Ff, Gf = sp.Function('F')(xs), sp.Function('G')(xs)
    A = [sp.sqrt(xs), sp.sqrt(xs), sp.sqrt(Ff)]
    D = lambda f: sp.diff(f, xs) * 2 * sp.sqrt(Gf)
    u, lam_ = [], []
    for i in range(3):
        j, k = (i + 1) % 3, (i + 2) % 3
        u.append(D(A[i]) - (A[j]**2 + A[k]**2 - A[i]**2) / (A[j] * A[k]))
    H = [u[i] + u[(i + 1) % 3] * u[(i + 2) % 3] / 2 for i in range(3)]
    r = [D(u[i]) / A[i] for i in range(3)]
    v = [2 * H[i] / (A[(i + 1) % 3] * A[(i + 2) % 3]) for i in range(3)]
    ric0sq = sum((r[i] - v[i])**2 for i in range(3))
    s = -2 * sum(r[i] + v[i] for i in range(3))
    w = A[0] * A[1] * A[2] / 4 / (2 * sp.sqrt(Gf))     # (abc/4) dt/dx  -> P/(8pi^2) per dx
    rep = {sp.Derivative(Ff, (xs, 2)): F2, sp.Derivative(Ff, xs): F1, sp.Derivative(Gf, xs): G1}
    Pd = sp.simplify((w * ric0sq).subs(rep).subs({Ff: F0, Gf: G0}))
    sd = sp.simplify(s.subs(rep).subs({Ff: F0, Gf: G0}))
    wd = sp.simplify(w.subs({Ff: F0, Gf: G0}))
    return Pd, sd, wd, (Ff, Gf, s, ric0sq)


def verify_bulks(sd_expr, Pd_expr):
    k = sp.symbols('k')
    res = {}
    for name, Fb, Gb in [('CSF', xs + k * xs**2, xs + k * xs**2), ('RSF', xs, xs + 2 * k * xs**2)]:
        sub = {F0: Fb, F1: sp.diff(Fb, xs), F2: sp.diff(Fb, xs, 2), G0: Gb, G1: sp.diff(Gb, xs)}
        res[name] = (sp.simplify(sd_expr.subs(sub)), sp.simplify(Pd_expr.subs(sub)))
    return res


BULK = {'CSF': (lambda x, k: x + k * x**2, lambda x, k: 1 + 2 * k * x, lambda x, k: 2 * k + 0 * x,
                lambda x, k: x + k * x**2, lambda x, k: 1 + 2 * k * x),
        'RSF': (lambda x, k: x, lambda x, k: 1 + 0 * x, lambda x, k: 0 * x,
                lambda x, k: x + 2 * k * x**2, lambda x, k: 1 + 4 * k * x)}


def cheb(n, z):
    T = [jnp.ones_like(z), z]
    for _ in range(2, n):
        T.append(2 * z * T[-1] - T[-2])
    return jnp.stack(T[:n])


class GeneralCell:
    def __init__(self, bulk, k, x0, X, deg, nq=600):
        self.bulk, self.k, self.x0, self.X, self.deg = bulk, k, x0, X, deg
        self.lam = -6.0 * k
        Pd, sd, wd, _ = symbolic_densities()
        args = (xs, F0, F1, F2, G0, G1)
        self.Pf = sp.lambdify(args, Pd, 'jax'); self.sf = sp.lambdify(args, sd, 'jax')
        self.wf = sp.lambdify(args, wd, 'jax')
        e, w = np.polynomial.legendre.leggauss(nq)
        self.ell = np.log(X / x0)
        u = 0.5 * (e + 1); wu = 0.5 * w
        self.u = jnp.array(u); self.wu = jnp.array(wu)
        self.nparam = 2 * deg

    def fields(self, z):
        x0, ell, k, deg = self.x0, self.ell, self.k, self.deg
        Fb, Fb1, Fb2, Gb, Gb1 = BULK[self.bulk]
        cF, cG = z[:deg], z[deg:]
        # bolt: F'(x0) = Fb(x0)/x0 e^{qF(0)}, G'(x0) = Gb(x0)/x0 e^{qG(0)}
        T0 = cheb(deg, jnp.array(-1.0))
        target = -jnp.log(Fb(x0, k) * Gb(x0, k) / x0**2)
        cG = cG.at[0].add(target - jnp.sum(cF * T0) - jnp.sum(cG * T0))

        def prof(x):
            u = jnp.log(x / x0) / ell
            sig = u**3 * (10 - 15 * u + 6 * u**2)
            base = 1 - (x0 / x) * (1 - sig)
            Bz = cheb(deg, 2 * u - 1)
            qF = (1 - u)**2 * jnp.sum(cF * Bz); qG = (1 - u)**2 * jnp.sum(cG * Bz)
            return Fb(x, k) * base * jnp.exp(qF), Gb(x, k) * base * jnp.exp(qG)

        def at(u):
            x = x0 * jnp.exp(ell * u)
            Ffun = lambda xx: prof(xx)[0]; Gfun = lambda xx: prof(xx)[1]
            F, G = prof(x)
            dF = jax.grad(Ffun)(x); d2F = jax.grad(jax.grad(Ffun))(x); dG = jax.grad(Gfun)(x)
            args = (x, F, dF, d2F, G, dG)
            return self.Pf(*args), self.sf(*args), self.wf(*args), x, F, G
        Pd, sd, wd, x, F, G = jax.vmap(at)(self.u)
        dx = self.wu * ell * x
        return Pd, sd, wd, dx, F, G

    def energies(self, z):
        Pd, sd, wd, dx, F, G = self.fields(z)
        P = jnp.sum(Pd * dx)
        Ssc = jnp.sum(wd * (sd - 4 * self.lam)**2 / 4 * dx)
        return P, P + Ssc, Ssc


def run(bulk, k, x0, X, deg, target, nq=600):
    c = GeneralCell(bulk, k, x0, X, deg, nq)
    idx = 0 if target == 'P' else 1
    f = jax.jit(lambda z: c.energies(z)[idx])
    g = jax.jit(jax.grad(lambda z: c.energies(z)[idx]))
    z0 = np.zeros(c.nparam)
    t0 = time.time()
    P0, J0, S0 = [float(v) for v in c.energies(jnp.array(z0))]
    res = minimize(lambda z: float(f(jnp.array(z))), z0, jac=lambda z: np.array(g(jnp.array(z))),
                   method='L-BFGS-B', options=dict(maxiter=6000, ftol=1e-16, gtol=1e-12, maxls=80))
    zz = jnp.array(res.x)
    P, J, S = [float(v) for v in c.energies(zz)]
    _, _, _, _, F, G = c.fields(zz)
    return dict(bulk=bulk, k=k, lam=-6 * k, x0=x0, X=X, deg=deg, target=target, nq=nq,
                P0=P0, J0=J0, P=P, J=J, scalar_part=S, P_slope=(P - 1) / x0, J_slope=(J - 1) / x0,
                minF=float(jnp.min(F)), minG=float(jnp.min(G)), success=bool(res.success),
                nit=int(res.nit), grad_inf=float(np.max(np.abs(res.jac))), z=[float(v) for v in res.x],
                sec=time.time() - t0)


if __name__ == '__main__':
    if sys.argv[1] == 'verify':
        Pd, sd, wd, _ = symbolic_densities()
        print(verify_bulks(sd, Pd))
        sys.exit()
    bulk, k, x0, X, deg, target = sys.argv[1], float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]), int(sys.argv[5]), sys.argv[6]
    nq = int(sys.argv[7]) if len(sys.argv) > 7 else 600
    out = run(bulk, k, x0, X, deg, target, nq)
    text = json.dumps(out); print(text)
    if len(sys.argv) > 8:
        Path(sys.argv[8]).write_text(text + '\n')

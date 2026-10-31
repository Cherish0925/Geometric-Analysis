"""O11: blow-up cells in complex-hyperbolic space with a relative rotation between
the Burns (exceptional) complex structure and the complex-hyperbolic one.

Metric (SU(2)_L-invariant, Bianchi IX with rotating eigenframe):
    g = dx^2/(4 G(x)) + h_ij(x) s^i s^j,   s^i = sigma^i / 2 (Euler left-invariant forms,
    sum s_i^2 = unit round S^3, volume 2 pi^2),
    h = Rot2(phi) diag(x e^{w}, x e^{-w}, F) Rot2(phi)^T .
U(2)/Kahler cells of u2_cell_jax_log.py are phi = const, w = 0.
Bolt (exceptional sphere) at x = x0: F = G = 0, F'G' = 1, w = 0; phi locally constant there.
Outer boundary x = X: F, G match complex hyperbolic F=G=x+x^2 (C^1, as in the U(2) runs),
w and phi vanish to C^2.  A constant phi is an isometry (right translation), so only
the RELATIVE angle theta = phi(bolt) - phi(X) is a modulus; theta in [0, pi/2].

Curvature: automatic differentiation of the coordinate metric in (x, psi, vartheta, varphi)
at one generic angle point (curvature scalars are SU(2)_L-invariant).

Output (JSON): P/(8pi^2) = int |Ric^0|^2 / (8pi^2), the separate terms
4 dW+ /(8pi^2) and dS/12/(8pi^2) relative to the complex-hyperbolic ball (complex
orientation of CH), and the identity residual (P-1) - (4dW+ + dS/12)/(8 pi^2).
Usage:  python o11_rotated_cell.py x0 X theta degU degw degr u1 [nq] [--opt]
"""
import sys, os, json, time
import numpy as np
import jax, jax.numpy as jnp
jax.config.update('jax_enable_x64', True)
from scipy.optimize import minimize

PI = np.pi
ANG = jnp.array([0.37, 1.13, 0.71])  # generic (psi, vartheta, varphi)


def euler_E(ang):
    psi, th, ph = ang
    return jnp.array([[0.0, jnp.sin(psi), -jnp.cos(psi)*jnp.sin(th)],
                      [0.0, jnp.cos(psi), jnp.sin(psi)*jnp.sin(th)],
                      [1.0, 0.0, jnp.cos(th)]]) / 2.0   # rows: s^1, s^2, s^3 in (psi, th, ph)


def rot2(p):
    c, s = jnp.cos(p), jnp.sin(p)
    return jnp.array([[c, 0.0, s], [0.0, 1.0, 0.0], [-s, 0.0, c]])


def metric_from(prof):
    """prof(x) -> (G, hmatrix).  Returns g(y) for y=(x, psi, th, ph)."""
    def g(y):
        G, h = prof(y[0])
        E = euler_E(y[1:])
        ang = E.T @ h @ E
        top = jnp.zeros((4, 4)).at[0, 0].set(1.0/(4.0*G))
        return top.at[1:, 1:].set(ang)
    return g


# Lambda^2 machinery in an oriented orthonormal frame (e0,e1,e2,e3)
PAIRS = [(0, 1), (0, 2), (0, 3), (2, 3), (3, 1), (1, 2)]
SQ = 1/np.sqrt(2)
LA = np.zeros((3, 6)); LB = np.zeros((3, 6))
for k in range(3):
    LA[k, k] = SQ; LA[k, 3+k] = SQ      # e0^ek + e_i^e_j  (one chirality)
    LB[k, k] = SQ; LB[k, 3+k] = -SQ     # e0^ek - e_i^e_j
LA = jnp.array(LA); LB = jnp.array(LB)


def curvature_scalars(g, y):
    gm = g(y)
    gi = jnp.linalg.inv(gm)
    def Gam(yy):
        dg = jax.jacfwd(g)(yy)                # dg[a,b,c] = d_c g_ab
        gii = jnp.linalg.inv(g(yy))
        # t[d,b,c] = d_b g_dc + d_c g_db - d_d g_bc ;  dg[d,c,b] = d_b g_dc ; dg[d,b,c] = d_c g_db ; dg[b,c,d] = d_d g_bc
        t = jnp.einsum('dcb->dbc', dg) + dg - jnp.einsum('bcd->dbc', dg)
        return 0.5*jnp.einsum('ad,dbc->abc', gii, t)
    Gm = Gam(y)
    dG = jax.jacfwd(Gam)(y)                  # dG[a,b,c,e] = d_e Gamma^a_bc
    # R^a_{bcd} = d_c Gam^a_{db} - d_d Gam^a_{cb} + Gam^a_{ce} Gam^e_{db} - Gam^a_{de} Gam^e_{cb}
    R = (jnp.einsum('adbc->abcd', dG) - jnp.einsum('acbd->abcd', dG)
         + jnp.einsum('ace,edb->abcd', Gm, Gm) - jnp.einsum('ade,ecb->abcd', Gm, Gm))
    Rl = jnp.einsum('ae,ebcd->abcd', gm, R)
    L = jnp.linalg.cholesky(gm)
    M = jnp.linalg.inv(L).T                  # columns: orthonormal frame vectors
    Rh = jnp.einsum('abcd,ai,bj,ck,dl->ijkl', Rl, M, M, M, M)
    ric = jnp.einsum('ijil->jl', Rh)
    s = jnp.trace(ric)
    ric0 = ric - s/4*jnp.eye(4)
    Rop = jnp.array([[Rh[i, j, k, l] for (k, l) in PAIRS] for (i, j) in PAIRS])
    WA = LA @ Rop @ LA.T - s/12*jnp.eye(3)
    WB = LB @ Rop @ LB.T - s/12*jnp.eye(3)
    return s, jnp.sum(ric0**2), jnp.sum(WA**2), jnp.sum(WB**2)


def kahler_K(x0, X):
    Mm = np.array([[x0**3/4, -0.5, x0**2, 1/x0], [3*x0**2/4, 0, 2*x0, -1/x0**2],
                   [X**3/4, -0.5, X**2, 1/X], [3*X**2/4, 0, 2*X, -1/X**2]])
    c1, c2, al, be = np.linalg.solve(Mm, np.array([-x0, 0, X**2, 2*X]))
    return lambda x: x + c1*x**3/4 - c2/2 + al*x**2 + be/x


def cheb(n, z):
    T = [jnp.ones_like(z), z]
    for k in range(2, n):
        T.append(2*z*T[-1] - T[-2])
    return jnp.stack(T[:n])


class Cell:
    def __init__(self, x0, X, degU, degw, degr, u1, nq=400, K=None):
        self.x0, self.X, self.degU, self.degw, self.degr, self.u1 = x0, X, degU, degw, degr, u1
        self.ell = np.log(X/x0)
        self.K = kahler_K(x0, X) if K is None else K
        e, w = np.polynomial.legendre.leggauss(nq)
        uA = 0.5*(e+1)*u1; wA = 0.5*w*u1
        uB = u1 + 0.5*(e+1)*(1-u1); wB = 0.5*w*(1-u1)
        u = np.concatenate([uA, uB]); wu = np.concatenate([wA, wB])
        self.xx = jnp.array(x0*np.exp(self.ell*u))
        self.wx = jnp.array(wu*self.ell*x0*np.exp(self.ell*u))   # dx
        self.nparam = 2*degU + degw + degr
        self.loc = False          # if True: two extra params (za, zb) place the rotation on [a,b] in log x

    def prof_factory(self, z, theta):
        x0, ell, u1 = self.x0, self.ell, self.u1
        dU, dw, dr = self.degU, self.degw, self.degr
        cF = z[:dU]; cG = z[dU:2*dU]; cw = z[2*dU:2*dU+dw]; cr = z[2*dU+dw:2*dU+dw+dr]
        if self.loc:
            za, zb = z[2*dU+dw+dr], z[2*dU+dw+dr+1]
            la = np.log(x0) + 0.03*ell + jax.nn.sigmoid(za)*0.9*ell
            lb = la + jax.nn.sigmoid(zb)*(np.log(self.X) - la)
        shift = -(jnp.sum(cF*cheb(dU, jnp.array(-1.0))) + jnp.sum(cG*cheb(dU, jnp.array(-1.0))))
        cG = cG.at[0].add(shift)                  # bolt regularity F'G'=1
        K = self.K
        def prof(x):
            u = jnp.log(x/x0)/ell
            zc = 2*u - 1
            Bu = cheb(max(dU, dw, 1), zc)
            qF = (1-u)**3*jnp.sum(cF*Bu[:dU]); qG = (1-u)**3*jnp.sum(cG*Bu[:dU])
            Kx = K(x)
            F = Kx*jnp.exp(qF); G = Kx*jnp.exp(qG)
            w = u*(1-u)**3*jnp.sum(cw*Bu[:dw]) if dw > 0 else 0.0*u
            if self.loc:
                v = jnp.clip((jnp.log(x) - la)/(lb - la), 0.0, 1.0)
            else:
                v = jnp.clip((u - u1)/(1 - u1), 0.0, 1.0)
            step = 10*v**3 - 15*v**4 + 6*v**5
            extra = v**3*(1-v)**3*jnp.sum(cr*cheb(dr, 2*v-1)) if dr > 0 else 0.0*v
            phi = theta*(1 - step - extra)
            Rm = rot2(phi)
            h = Rm @ jnp.diag(jnp.array([x*jnp.exp(w), x*jnp.exp(-w), F])) @ Rm.T
            return G, h
        return prof

    def fields(self, z, theta):
        g = metric_from(self.prof_factory(z, theta))
        def at(x):
            y = jnp.concatenate([jnp.array([x]), ANG])
            s, r0, wa, wb = curvature_scalars(g, y)
            G, h = self.prof_factory(z, theta)(x)
            dv = PI**2*jnp.sqrt(jnp.linalg.det(h)/G)
            return s, r0, wa, wb, dv
        return jax.vmap(at)(self.xx)

    def P(self, z, theta):
        s, r0, wa, wb, dv = self.fields(z, theta)
        return jnp.sum(r0*dv*self.wx)/(8*PI**2)

    def report(self, z, theta, wplus='A'):
        s, r0, wa, wb, dv = self.fields(z, theta)
        W = self.wx*dv
        wp = wa if wplus == 'A' else wb
        wm = wb if wplus == 'A' else wa
        X = self.X
        P = float(jnp.sum(r0*W))/(8*PI**2)
        S = float(jnp.sum(s**2*W)); Wp = float(jnp.sum(wp*W)); Wm = float(jnp.sum(wm*W))
        dWp = 4*(Wp - 12*PI**2*X**2)/(8*PI**2); dS = (S - 288*PI**2*X**2)/12/(8*PI**2)
        return dict(P=P, fourdWp=dWp, dS12=dS, resid=(P-1) - (dWp + dS), Wm_over_12pi2=Wm/(12*PI**2))


def checks():
    out = {}
    x0 = 0.05
    for name, FF in [('flat', lambda x: x), ('CH', lambda x: x + x**2), ('Burns', lambda x: x - x0)]:
        prof = lambda x, FF=FF: (FF(x), jnp.diag(jnp.array([x, x, FF(x)])))
        g = metric_from(prof)
        vals = []
        for ang in [ANG, jnp.array([1.9, 0.4, 2.5])]:
            y = jnp.concatenate([jnp.array([0.37]), ang])
            vals.append([float(v) for v in curvature_scalars(g, y)])
        out[name] = vals
    # rotated-constant invariance for CH
    prof = lambda x: (x + x**2, rot2(0.8) @ jnp.diag(jnp.array([x, x, x + x**2])) @ rot2(0.8).T)
    y = jnp.concatenate([jnp.array([0.37]), ANG])
    out['CH_rot_const'] = [float(v) for v in curvature_scalars(metric_from(prof), y)]
    return out


if __name__ == '__main__':
    if sys.argv[1] == 'check':
        print(json.dumps(checks(), indent=1)); sys.exit()
    x0, X, theta = float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3])
    degU, degw, degr = int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6])
    u1 = float(sys.argv[7]); nq = int(sys.argv[8]) if len(sys.argv) > 8 and not sys.argv[8].startswith('--') else 400
    opt = '--opt' in sys.argv
    wplus = 'B' if '--wB' in sys.argv else 'A'
    c = Cell(x0, X, degU, degw, degr, u1, nq)
    zinit = np.zeros(c.nparam)
    if '--loc' in sys.argv:
        c.loc = True; c.nparam += 2
        # start: rotation on [0.2 ell, 0.8 ell] above log x0 (centred near the crossover x ~ sqrt(x0))
        zinit = np.concatenate([zinit, [np.log(0.17/0.73), np.log(0.75/0.25)]])
    z0 = jnp.array(zinit)
    t0 = time.time()
    Pf = jax.jit(lambda z: c.P(z, theta)); gf = jax.jit(jax.grad(lambda z: c.P(z, theta)))
    base = c.report(z0, theta, wplus)
    out = dict(x0=x0, X=X, theta=theta, degU=degU, degw=degw, degr=degr, u1=u1, nq=nq, base=base, loc=c.loc)
    if opt:
        res = minimize(lambda z: float(Pf(jnp.array(z))), zinit,
                       jac=lambda z: np.array(gf(jnp.array(z))), method='L-BFGS-B',
                       options=dict(maxiter=3000, ftol=1e-14, gtol=1e-10))
        out['opt'] = c.report(jnp.array(res.x), theta, wplus)
        out['msg'] = str(res.message); out['nit'] = int(res.nit)
        out['z'] = [float(v) for v in res.x]
    out['sec'] = time.time() - t0
    print(json.dumps(out))

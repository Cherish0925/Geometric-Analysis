"""O11 orthogonal cell (theta = pi/2) in a fixed-frame triaxial ansatz.

Step-6 rotated cells put the bolt-collapsing direction and the CH fibre in the
same eigen-slot F and rotate the frame; at theta=pi/2 their triaxial slot w was
forced to vanish at the bolt and could not carry the CH fibre, which may be the
origin of the observed log(1/x0) growth.  Here, at theta=pi/2, the frame is FIXED:

    g = dx^2/(4G) + F s1^2 + x e^{-w} s2^2 + x e^{w} s3^2 ,

bolt at x0 in the s1 slot (F=G=0, F'G'=1, w(x0)=0 so the bolt S^2 is round),
complex-hyperbolic collar at X in the s3 slot:  F -> x, x e^w -> x+x^2,
x e^{-w} -> x/(1+x)*... (fixed by the product convention), G -> x+x^2 (C^1).
Relative to the Burns form (s1) the CH form (s3) is rotated by pi/2.

Prediction of the SO(3)_+-equivariant linear-response picture (Step 8 note):
(P-1)/x0 -> 6(1+sin^2 theta) = 12 at theta=pi/2, with no log growth.

Usage: python o11_perp_cell.py x0 [degU degw nq]
"""
import sys, json, time
import numpy as np
import jax, jax.numpy as jnp
jax.config.update('jax_enable_x64', True)
from scipy.optimize import minimize
from o11_rotated_cell import cheb, rot2, metric_from, curvature_scalars, ANG, PI


def smooth(u):
    return 10*u**3 - 15*u**4 + 6*u**5


class PerpCell:
    def __init__(self, x0, X=1.0, degU=6, degw=6, nq=300, u1=0.05):
        self.x0, self.X, self.degU, self.degw = x0, X, degU, degw
        self.ell = np.log(X/x0)
        e, w = np.polynomial.legendre.leggauss(nq)
        uA = 0.5*(e+1)*u1; wA = 0.5*w*u1
        uB = u1 + 0.5*(e+1)*(1-u1); wB = 0.5*w*(1-u1)
        u = np.concatenate([uA, uB]); wu = np.concatenate([wA, wB])
        self.xx = jnp.array(x0*np.exp(self.ell*u))
        self.wx = jnp.array(wu*self.ell*x0*np.exp(self.ell*u))
        self.nparam = 2*degU + degw
        self.aligned = False
        self.wpow = 1   # wpow=2 makes the bolt anisotropy O((x-x0)^2): smooth charge-4 mode
        self.beta0 = 0.0; self.degr = 0

    def prof_factory(self, z):
        x0, ell, X = self.x0, self.ell, self.X
        dU, dw = self.degU, self.degw
        cF = z[:dU]; cG = z[dU:2*dU]; cw = z[2*dU:2*dU+dw]
        shift = -(jnp.sum(cF*cheb(dU, jnp.array(-1.0))) + jnp.sum(cG*cheb(dU, jnp.array(-1.0))))
        cG = cG.at[0].add(shift)

        def prof(x):
            u = jnp.log(x/x0)/ell
            Bu = cheb(max(dU, dw), 2*u-1)
            qF = (1-u)**3*jnp.sum(cF*Bu[:dU]); qG = (1-u)**3*jnp.sum(cG*Bu[:dU])
            su = smooth(u)
            G = (x - x0 + (x**2 + x0)*su)*jnp.exp(qG)
            wr = u**self.wpow*(1-u)**3*jnp.sum(cw*Bu[:dw])
            if self.aligned:
                # control: bolt and CH fibre both in the s3 slot (theta=0)
                F = (x - x0)*jnp.exp(qF) + (x0 + x**2)*su
                h = jnp.diag(jnp.array([x, x*jnp.exp(wr), F]))
            else:
                F = (x - x0)*jnp.exp(qF) + x0*su
                w = jnp.log1p(x)*su + wr
                # coordinate x := s2-eigenvalue; bolt round iff w(x0)=0; CH collar: x, x+x^2
                h = jnp.diag(jnp.array([F, x, x*jnp.exp(w)]))
                if self.degr >= 0 and self.beta0 != 0.0:
                    # adiabatic family: bolt direction R(beta0) e1, CH fibre e3,
                    # relative angle theta = pi/2 - beta0
                    v = jnp.clip((u - 0.05)/0.95, 0.0, 1.0)
                    st = 10*v**3 - 15*v**4 + 6*v**5
                    cr = z[2*dU+dw:2*dU+dw+self.degr]
                    extra = v**3*(1-v)**3*jnp.sum(cr*cheb(self.degr, 2*v-1)) if self.degr > 0 else 0.0*v
                    beta = self.beta0*(1 - st - extra)
                    Rm = rot2(beta)
                    h = Rm @ h @ Rm.T
            return G, h
        return prof

    def fields(self, z):
        prof = self.prof_factory(z)
        g = metric_from(prof)

        def at(x):
            y = jnp.concatenate([jnp.array([x]), ANG])
            s, r0, wa, wb = curvature_scalars(g, y)
            G, h = prof(x)
            return s, r0, wa, wb, PI**2*jnp.sqrt(jnp.linalg.det(h)/G)
        return jax.vmap(at)(self.xx)

    def P(self, z):
        s, r0, wa, wb, dv = self.fields(z)
        return jnp.sum(r0*dv*self.wx)/(8*PI**2)

    def report(self, z):
        s, r0, wa, wb, dv = self.fields(z)
        W = self.wx*dv; X = self.X
        P = float(jnp.sum(r0*W))/(8*PI**2)
        S = float(jnp.sum(s**2*W))
        out = dict(P=P)
        for lab, wp in (('A', wa), ('B', wb)):
            Wp = float(jnp.sum(wp*W))
            dWp = 4*(Wp - 12*PI**2*X**2)/(8*PI**2); dS = (S - 288*PI**2*X**2)/12/(8*PI**2)
            out['resid_'+lab] = (P-1) - (dWp + dS); out['fourdWp_'+lab] = dWp
        out['dS12'] = dS
        return out


if __name__ == '__main__':
    x0 = float(sys.argv[1])
    degU = int(sys.argv[2]) if len(sys.argv) > 2 else 6
    degw = int(sys.argv[3]) if len(sys.argv) > 3 else 6
    nq = int(sys.argv[4]) if len(sys.argv) > 4 else 300
    c = PerpCell(x0, 1.0, degU, degw, nq)
    c.aligned = '--aligned' in sys.argv
    c.wpow = 2 if '--smooth' in sys.argv else 1
    for a in sys.argv:
        if a.startswith('--theta='):
            c.beta0 = np.pi/2 - float(a.split('=')[1]); c.degr = 6; c.nparam += 6
    t0 = time.time()
    z0 = np.zeros(c.nparam)
    Pf = jax.jit(c.P); gf = jax.jit(jax.grad(c.P))
    base = c.report(jnp.array(z0))
    res = minimize(lambda z: float(Pf(jnp.array(z))), z0, jac=lambda z: np.array(gf(jnp.array(z))),
                   method='L-BFGS-B', options=dict(maxiter=4000, ftol=1e-15, gtol=1e-11))
    opt = c.report(jnp.array(res.x))
    print(json.dumps(dict(x0=x0, degU=degU, degw=degw, nq=nq, aligned=c.aligned, wpow=c.wpow, theta=float(np.pi/2-c.beta0), base=base, opt=opt,
                          slope=(opt['P']-1)/x0, msg=str(res.message), nit=int(res.nit),
                          z=[float(v) for v in res.x], sec=time.time()-t0)))

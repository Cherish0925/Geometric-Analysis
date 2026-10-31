"""O11 perpendicular Burns cell in complex-hyperbolic space: explicit competitors that
exploit the logarithmic neck interaction.

Metric (diagonal Bianchi IX, proper radial time t, d sigma_i = 2 sigma_j ^ sigma_k):
    g = dt^2 + a1^2 s1^2 + a2^2 s2^2 + a3^2 s3^2 ,
slot 3 = bolt (Burns) direction, slot 2 = CH Kahler fibre, slot 1 = remaining direction.
Exact models:
    Burns  : a1=a2=sqrt(t^2+x0), a3=t           (u=(0,0,-x0/(t^2+x0)))
    CH     : a1=a3=sinh t, a2=sinh t cosh t     (u=(0,3 sinh^2 t,0), Ric=-6g)
Reference cell (exact smooth bolt at t=0, exact CH beyond the cutoff):
    c(t)=x0*chi(t),  a1=sqrt(S^2+c) e^{phi1}, a2=sqrt(S^2+c) C e^{phi2}, a3=S e^{phi3},
with S=sinh t, C=cosh t, chi=1 near the bolt and 0 near the collar, and phi_i = x0 * (compactly
supported Chebyshev-bump series in s=log t).  The bolt is never touched by phi.

Cost (units of 8 pi^2), with u_i = adot_i - (a_j^2+a_k^2-a_i^2)/(a_j a_k), H_i=u_i+u_j u_k/2,
lambda_i = a_j a_k/a_i (peer S1003A01 Step 6, cross-checked against direct curvature):
    P - 1 = int [S1+S2+S3 + 2 u1 u2 u3/lambda2] dt          (relative calibration, Phi_bolt=1, Phi_CH=0)
    P     = int sum lambda_i/4 (udot_i - 2H_i/lambda_i)^2 dt  (uncalibrated check)
    J - P = 1/4 int a1a2a3 [sum(udot_i/a_i + 2H_i/(a_j a_k)) - 12]^2 dt
Neck prediction (this Step): with u2 u3 ~ -3 x0 and u1 = x0 v(s),
    density per ds = x0^2 [ (v_s+2v-3)^2/4 - 6 v ]  ->  min -18 x0^2 at v=9/2,
    so  P-1 = -9 x0^2 log(1/x0) + O(x0^2).

Usage: python o11_perp_logneck.py x0 [--deg N] [--target P|J] [--nq N] [--out file] [--plateau v]
"""
import sys, json, time, argparse
import numpy as np
import jax, jax.numpy as jnp
jax.config.update('jax_enable_x64', True)
from scipy.optimize import minimize

NEWTON_IT = 80
TC = float(np.arcsinh(1.0))          # collar: x = sinh^2 t = 1


def smoothstep(y):
    y = jnp.clip(y, 0.0, 1.0)
    return y**4*(35 - 84*y + 70*y**2 - 20*y**3)   # C^3 step


class Cell:
    def __init__(self, x0, deg=24, nq=1600, s_lo_off=-1.0, s_hi=np.log(0.6), chi_lo=np.log(0.35), chi_hi=np.log(0.8), ninner=80, smooth=False, ncore=0, nout=0, t_out=0.03):
        self.x0 = x0; self.deg = deg; self.smooth = smooth; self.ncore = ncore; self.nout = nout; self.t_out = t_out
        self.sb = 0.5*np.log(x0)
        self.s_lo = self.sb + s_lo_off; self.s_hi = s_hi
        self.chi_lo, self.chi_hi = chi_lo, chi_hi
        # quadrature: t in [0, t1] Gauss, log t in [log t1, log TC] Gauss (split)
        t1 = np.sqrt(x0)*np.exp(-3.0)
        e, w = np.polynomial.legendre.leggauss(ninner)
        tA = 0.5*(e+1)*t1; wA = 0.5*w*t1
        L = np.log(TC) - np.log(t1)
        nB = nq
        e2, w2 = np.polynomial.legendre.leggauss(nB)
        sB = np.log(t1) + 0.5*(e2+1)*L; tB = np.exp(sB); wB = 0.5*w2*L*tB
        self.tt = jnp.array(np.concatenate([tA, tB])); self.wt = jnp.array(np.concatenate([wA, wB]))
        self.nparam = 3*deg + 3*ncore + 4*nout + 3

    def a_of_t(self, z, t):
        x0 = self.x0
        s = jnp.log(t)
        S = jnp.sinh(t); C = jnp.cosh(t)
        chi = 1 - smoothstep((s - self.chi_lo)/(self.chi_hi - self.chi_lo))
        c = x0*chi
        y = 2*(s - self.s_lo)/(self.s_hi - self.s_lo) - 1
        inside = (y > -1) & (y < 1)
        yc = jnp.clip(y, -1, 1)
        env = jnp.where(inside, (1 - yc**2)**4, 0.0)
        T = [jnp.ones_like(yc), yc]
        for k in range(2, self.deg):
            T.append(2*yc*T[-1] - T[-2])
        T = jnp.stack(T[:self.deg])
        zz = z[:3*self.deg].reshape(3, self.deg)
        phi = x0*env*(zz @ T)
        # explicit plateau carrying the neck optimum C* (last three parameters)
        zp = z[-3:]
        pl = smoothstep((s - (self.sb - 0.5))/3.0)*(1 - smoothstep((s - np.log(0.03))/(np.log(0.5) - np.log(0.03))))
        phi = phi + x0*pl*zp
        rho = t**2/(t**2 + x0)
        if self.ncore > 0:
            # bolt-regular core modes: phi1,phi2 even with phi1-phi2=O(t^4); phi3=O(t^2)
            yr = 2*rho - 1
            Tr = [jnp.ones_like(yr), yr]
            for k in range(2, self.ncore):
                Tr.append(2*yr*Tr[-1] - Tr[-2])
            Tr = jnp.stack(Tr[:self.ncore])*(1 - rho)**2
            zc = z[3*self.deg:3*self.deg + 3*self.ncore].reshape(3, self.ncore)
            common = zc[0] @ Tr; diff = rho**2*(zc[1] @ Tr); p3 = rho*(zc[2] @ Tr)
            phi = phi + x0*jnp.array([common + diff, common - diff, p3])
        r = jnp.sqrt(S**2 + c)
        if self.nout > 0:
            # outer modes in t on [t_out, TC]: corrections to phi_i and to the Burns-tail cutoff chi
            yo = 2*(t - self.t_out)/(TC - self.t_out) - 1
            ino = (yo > -1) & (yo < 1); yoc = jnp.clip(yo, -1, 1)
            envo = jnp.where(ino, (1 - yoc**2)**4, 0.0)
            To = [jnp.ones_like(yoc), yoc]
            for k in range(2, self.nout):
                To.append(2*yoc*To[-1] - To[-2])
            To = jnp.stack(To[:self.nout])*envo
            zo = z[3*self.deg + 3*self.ncore:3*self.deg + 3*self.ncore + 4*self.nout].reshape(4, self.nout)
            phi = phi + x0*(zo[:3] @ To)
            r = jnp.sqrt(S**2 + x0*(chi + zo[3] @ To))
        if self.smooth:
            # CH anisotropy cosh t switched on as (cosh t - 1)*beta, beta = smoothstep(t^2/(4 x0)):
            # a2^2-a1^2 = O(t^10) at the bolt, and beta == 1 (exact CH) for t >= 2 sqrt(x0)
            beta = smoothstep(t**2/(4*x0))
            C = 1 + (C - 1)*beta
        return jnp.array([r*jnp.exp(phi[0]), r*C*jnp.exp(phi[1]), S*jnp.exp(phi[2])])

    def u_of_t(self, z, t):
        a = self.a_of_t(z, t)
        ad = jax.jacfwd(lambda tt: self.a_of_t(z, tt))(t)
        u = jnp.array([ad[0] - (a[1]**2 + a[2]**2 - a[0]**2)/(a[1]*a[2]),
                       ad[1] - (a[2]**2 + a[0]**2 - a[1]**2)/(a[2]*a[0]),
                       ad[2] - (a[0]**2 + a[1]**2 - a[2]**2)/(a[0]*a[1])])
        return u, a

    def dens(self, z, t):
        u, a = self.u_of_t(z, t)
        ud = jax.jacfwd(lambda tt: self.u_of_t(z, tt)[0])(t)
        H = jnp.array([u[0] + u[1]*u[2]/2, u[1] + u[2]*u[0]/2, u[2] + u[0]*u[1]/2])
        lam = jnp.array([a[1]*a[2]/a[0], a[2]*a[0]/a[1], a[0]*a[1]/a[2]])
        s1 = lam[0]/4*(ud[0] + 2*H[0]/lam[0])**2
        s2 = lam[1]/4*(ud[1] - (2*u[1] - u[0]*u[2])/lam[1])**2
        s3 = lam[2]/4*(ud[2] + 2*H[2]/lam[2])**2
        cub = 2*u[0]*u[1]*u[2]/lam[1]
        psq = jnp.sum(lam/4*(ud - 2*H/lam)**2)
        Sig = jnp.sum(ud/a + 2*H/(jnp.roll(a, -1)*jnp.roll(a, -2)))
        scal = a[0]*a[1]*a[2]/4*(Sig - 12)**2
        return jnp.array([s1, s2, s3, cub, psq, scal, u[0], u[1], u[2]])

    def terms(self, z):
        D = jax.vmap(lambda t: self.dens(z, t))(self.tt)
        I = D[:, :6].T @ self.wt
        return I, D

    def Pm1(self, z):
        I, _ = self.terms(z)
        return I[0] + I[1] + I[2] + I[3]

    def Jm1(self, z):
        I, _ = self.terms(z)
        return I[0] + I[1] + I[2] + I[3] + I[5]


def run(x0, deg, nq, target, plateau=None, maxiter=3000, s_hi=np.log(0.6), z0in=None, smooth=False, ncore=0, nout=0):
    c = Cell(x0, deg, nq, s_hi=s_hi, smooth=smooth, ncore=ncore, nout=nout)
    f = c.Pm1 if target == 'P' else c.Jm1
    sc = 1.0/x0**2
    fj = jax.jit(lambda z: f(z)*sc); gj = jax.jit(jax.grad(lambda z: f(z)*sc))
    z0 = np.zeros(c.nparam) if z0in is None else np.array(z0in)
    if plateau is not None:
        z0[-3:] = [9/4, 5/4 if c.smooth else 3/4, 1/2]
    if False:
        # seed: phi1 constant ~ plateau so that u1 ~ x0*plateau in the neck (linear: u1 ~ 3 phi1 + phi1_s - ...)
        z0[0] = plateau/3.0
    t0 = time.time()
    # Newton on the (nearly quadratic, phi = x0 * z) cost, with backtracking
    hj = jax.jit(jax.hessian(lambda z: f(z)*sc))
    z = jnp.array(z0); fz = float(fj(z)); newton_log = []
    for it in range(NEWTON_IT):
        g = np.array(gj(z)); Hm = np.array(hj(z))
        ev = np.linalg.eigvalsh(0.5*(Hm + Hm.T))
        shift = max(0.0, -ev.min()*1.1 + 1e-10*abs(ev).max())
        step = -np.linalg.solve(Hm + shift*np.eye(len(g)), g)
        lam = 1.0
        while lam > 1e-6:
            zn = z + lam*jnp.array(step); fn = float(fj(zn))
            if fn < fz: break
            lam *= 0.5
        if it > 3 and it % 10: newton_log.append(dict(it=it, f=fz)); 
        else: newton_log.append(dict(it=it, f=fz, gnorm=float(np.linalg.norm(g)), evmin=float(ev.min()), evmax=float(ev.max()), lam=lam))
        if fn >= fz: break
        dec = fz - fn; z, fz = zn, fn
        if dec < 1e-13*max(1, abs(fz)): break
    z0 = np.array(z)
    res = minimize(lambda z: float(fj(jnp.array(z))), z0, jac=lambda z: np.array(gj(jnp.array(z))),
                   method='L-BFGS-B', options=dict(maxiter=maxiter, ftol=1e-15, gtol=1e-10, maxcor=30))
    zs = jnp.array(res.x)
    I, D = c.terms(zs)
    I0, _ = c.terms(jnp.zeros(c.nparam))
    I = np.array(I); I0 = np.array(I0)
    out = dict(x0=x0, deg=deg, nq=nq, target=target, log_inv_x0=float(np.log(1/x0)),
               ref=dict(Pm1=float(I0[:4].sum()), P_uncal=float(I0[4]), Jm1=float(I0[:4].sum() + I0[5])),
               opt=dict(S1=float(I[0]), S2=float(I[1]), S3=float(I[2]), cubic=float(I[3]),
                        Pm1=float(I[:4].sum()), P_uncal_minus1=float(I[4] - 1), scal=float(I[5]),
                        Jm1=float(I[:4].sum() + I[5])),
               Pm1_over_x02=float(I[:4].sum()/x0**2), Jm1_over_x02=float((I[:4].sum() + I[5])/x0**2),
               msg=str(res.message), nit=int(res.nit), gnorm=float(np.linalg.norm(gj(zs))),
               sec=time.time() - t0, newton=newton_log, z=[float(v) for v in res.x])
    # neck plateau of u1/x0 sampled
    tt = np.array(c.tt); u1 = np.array(D[:, 6])
    sel = (tt > np.sqrt(x0)*np.e**1.5) & (tt < 0.15)
    if sel.any():
        out['u1_over_x0_neck_median'] = float(np.median(u1[sel]/x0))
    return out, c, zs


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('x0', type=float)
    ap.add_argument('--deg', type=int, default=24)
    ap.add_argument('--nq', type=int, default=1600)
    ap.add_argument('--target', default='P')
    ap.add_argument('--plateau', type=float, default=None)
    ap.add_argument('--maxiter', type=int, default=3000)
    ap.add_argument('--out', default=None)
    ap.add_argument('--shi', type=float, default=float(np.log(0.6)))
    ap.add_argument('--init', default=None)
    ap.add_argument('--smooth', action='store_true')
    ap.add_argument('--ncore', type=int, default=0)
    ap.add_argument('--nout', type=int, default=0)
    a = ap.parse_args()
    z0in = None
    if a.init:
        r = json.load(open(a.init)); zz = np.array(r['z'][:3*r['deg']]).reshape(3, r['deg'])
        z0in = np.zeros((3, a.deg)); m = min(a.deg, r['deg']); z0in[:, :m] = zz[:, :m]; z0in = np.concatenate([z0in.ravel(), np.zeros(3*a.ncore + 4*a.nout + 3)])
    out, c, zs = run(a.x0, a.deg, a.nq, a.target, a.plateau, a.maxiter, a.shi, z0in, a.smooth, a.ncore, a.nout)
    out['s_hi'] = a.shi; out['smooth'] = a.smooth; out['ncore'] = a.ncore; out['nout'] = a.nout
    txt = json.dumps(out)
    print(json.dumps({k: v for k, v in out.items() if k != 'z'}))
    if a.out:
        open(a.out, 'w').write(txt + '\n')

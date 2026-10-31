"""Independent verification of the S1003A01 large-collar perpendicular CH cell.

This implementation reconstructs the metric profile from the stored coefficients but
does not import the peer's DualCell, curvature, or spin-diagnostic modules.  It evaluates
the exact Cartan/spin formulas in x using JAX derivatives and split Gauss quadrature.

Usage:
  python o11_collar_independent_verify.py RECORD [--n N] [--out FILE]
"""
from pathlib import Path
import argparse, json
import numpy as np
import jax
import jax.numpy as jnp
jax.config.update("jax_enable_x64", True)


def cheb(n, y):
    vals = [jnp.ones_like(y)]
    if n > 1:
        vals.append(y)
    for _ in range(2, n):
        vals.append(2*y*vals[-1] - vals[-2])
    return jnp.stack(vals[:n])


def smooth(u):
    return 10*u**3 - 15*u**4 + 6*u**5


class Metric:
    def __init__(self, rec):
        self.x0 = float(rec["x0"]); self.X = float(rec["X"]); self.deg = int(rec["deg"])
        self.ell = float(np.log(self.X/self.x0)); z = jnp.asarray(rec["z"], dtype=jnp.float64)
        d = self.deg
        self.cF = z[:d]
        cG0 = z[d:2*d]
        shift = -(jnp.dot(self.cF, cheb(d, jnp.array(-1.0))) + jnp.dot(cG0, cheb(d, jnp.array(-1.0))))
        self.cG = cG0.at[0].add(shift)
        self.cw = z[2*d:3*d]

    def profile(self, x):
        u = jnp.log(x/self.x0)/self.ell; B = cheb(self.deg, 2*u-1)
        qF = (1-u)**3*jnp.dot(self.cF, B)
        qG = (1-u)**3*jnp.dot(self.cG, B)
        su = smooth(u)
        G = (x-self.x0 + (x*x+self.x0)*su)*jnp.exp(qG)
        F = (x-self.x0)*jnp.exp(qF) + self.x0*su
        wr = u**2*(1-u)**3*jnp.dot(self.cw, B)
        w = jnp.log1p(x)*su + wr
        return G, F, w

    def axes(self, x):
        # Bolt-adapted cyclic axes: (old s2, old s3, old s1).
        G, F, w = self.profile(x)
        return G, jnp.array([jnp.sqrt(x), jnp.sqrt(x*jnp.exp(w)), jnp.sqrt(F)])

    def spin(self, x):
        G, a = self.axes(x)
        dax = jax.jacfwd(lambda xx: self.axes(xx)[1])(x)
        adot = 2*jnp.sqrt(G)*dax
        u = jnp.array([
            adot[0]-(a[1]**2+a[2]**2-a[0]**2)/(a[1]*a[2]),
            adot[1]-(a[2]**2+a[0]**2-a[1]**2)/(a[2]*a[0]),
            adot[2]-(a[0]**2+a[1]**2-a[2]**2)/(a[0]*a[1])])
        return G, a, u

    def density_x(self, x):
        G, a, u = self.spin(x)
        dux = jax.jacfwd(lambda xx: self.spin(xx)[2])(x)
        ud = 2*jnp.sqrt(G)*dux
        H = jnp.array([u[0]+u[1]*u[2]/2, u[1]+u[2]*u[0]/2, u[2]+u[0]*u[1]/2])
        lam = jnp.array([a[1]*a[2]/a[0], a[2]*a[0]/a[1], a[0]*a[1]/a[2]])
        S1 = lam[0]/4*(ud[0]+2*H[0]/lam[0])**2
        S2 = lam[1]/4*(ud[1]-(2*u[1]-u[0]*u[2])/lam[1])**2
        S3 = lam[2]/4*(ud[2]+2*H[2]/lam[2])**2
        cubic = 2*u[0]*u[1]*u[2]/lam[1]
        Ppos = jnp.sum(lam/4*(ud-2*H/lam)**2)
        Sigma = jnp.sum(ud/a + 2*H/(jnp.roll(a,-1)*jnp.roll(a,-2)))
        scalar = jnp.prod(a)/4*(Sigma-12)**2
        inv = 1/(2*jnp.sqrt(G))
        # Boundary primitive for the relative completion (no u2^2 term).
        primitive = u[0]**2 + u[2]**2 + u[0]*u[1]*u[2]
        return jnp.array([S1,S2,S3,cubic,Ppos,scalar,primitive])*inv


def integrate(metric, n):
    # Integrate in logarithmic u with fixed subintervals; this resolves both bolt and long collar.
    e,w = np.polynomial.legendre.leggauss(n)
    cuts = np.array([0.0, 0.01, 0.04, 0.12, 0.30, 0.60, 0.85, 1.0])
    us=[]; ws=[]
    for lo,hi in zip(cuts[:-1], cuts[1:]):
        us.append(lo+(hi-lo)*(e+1)/2); ws.append((hi-lo)*w/2)
    us=np.concatenate(us); ws=np.concatenate(ws)
    xs=metric.x0*np.exp(metric.ell*us); dxdu=metric.ell*xs
    vals=np.asarray(jax.vmap(metric.density_x)(jnp.asarray(xs)))
    I=np.sum((ws*dxdu)[:,None]*vals,axis=0)
    return I


def endpoint(metric):
    prof=metric.profile
    x0=metric.x0; X=metric.X
    Fp=jax.grad(lambda x: prof(x)[1]); Gp=jax.grad(lambda x: prof(x)[0]); wp=jax.grad(lambda x: prof(x)[2])
    # Jets near bolt fitted against d=x-x0 (functions are explicit and differentiable).
    return dict(
        bolt=dict(G=float(prof(x0)[0]),F=float(prof(x0)[1]),w=float(prof(x0)[2]),
                  Fp=float(Fp(x0)),Gp=float(Gp(x0)),FpGp=float(Fp(x0)*Gp(x0)),wp=float(wp(x0))),
        collar=dict(G=float(prof(X)[0]),F=float(prof(X)[1]),w=float(prof(X)[2]),
                    Gp=float(Gp(X)),Fp=float(Fp(X)),wp=float(wp(X)),
                    expected=[X+X*X,X,float(np.log1p(X)),1+2*X,1,1/(1+X)]))


def main():
    ap=argparse.ArgumentParser(); ap.add_argument("record"); ap.add_argument("--n",type=int,default=300); ap.add_argument("--out")
    a=ap.parse_args(); rec=json.loads(Path(a.record).read_text().strip().splitlines()[-1]); m=Metric(rec)
    ns=sorted(set([max(80,a.n//2),a.n,2*a.n]))
    out={"record":a.record,"x0":m.x0,"X":m.X,"deg":m.deg,"endpoint":endpoint(m),"quadratures":{}}
    for n in ns:
        I=integrate(m,n)
        out["quadratures"][str(n)]={"S1":float(I[0]),"S2":float(I[1]),"S3":float(I[2]),"cubic":float(I[3]),
                                     "P_relative":float(1+I[:4].sum()),"P_positive":float(I[4]),
                                     "scalar":float(I[5]),"J":float(1+I[:4].sum()+I[5])}
    # Fine positivity and endpoint-primitive samples.
    xg=m.x0*np.exp(m.ell*np.linspace(1e-8,1,20001)); pr=jax.vmap(m.profile)(jnp.asarray(xg))
    G=np.asarray(pr[0]); F=np.asarray(pr[1]); w=np.asarray(pr[2])
    out["positivity"]={"min_G_over_dx":float(np.min(G/(xg-m.x0))),"min_F_over_dx":float(np.min(F/(xg-m.x0))),
                       "min_exp_w":float(np.min(np.exp(w))),"max_exp_w":float(np.max(np.exp(w)))}
    text=json.dumps(out,indent=1); print(text)
    if a.out: Path(a.out).write_text(text+"\n")

if __name__=="__main__": main()

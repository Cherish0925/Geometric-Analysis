"""Diagonal perpendicular O(-1) cells with an exact real-hyperbolic collar.

Metric in x-coordinates:
  g = dx^2/(4 G) + F sigma1^2 + x sigma2^2 + x exp(w) sigma3^2,
  d sigma_i=2 sigma_j^sigma_k, int sigma123=2 pi^2.
Slot 1 collapses at the O(-1) bolt.  The RSF/H4 collar is
  F=x, G=x+2 x^2, w=0,
which has Ric=-6 g.  In geodesic radius t this is the round profile
  a_i=sinh(sqrt(2)t)/sqrt(2),
so the Einstein normalization matches the CH cell calculations.

The ansatz follows the certified CH perpendicular family, but replaces the collar and
uses base positivity factors adapted to H4.  It is exploratory floating-point evidence,
not an interval certificate.  Outputs P=integral |Ric0|^2/(8pi^2) and
J=P+(1/4)integral(s+24)^2/(8pi^2).
"""
import argparse, json, time
from pathlib import Path
import numpy as np
import sympy as sp
import jax, jax.numpy as jnp
from scipy.optimize import minimize
jax.config.update('jax_enable_x64', True)

x=sp.symbols('x',positive=True)
F0,F1,F2,G0,G1,w0,w1,w2=sp.symbols('F0 F1 F2 G0 G1 w0 w1 w2',real=True)

def symbolic():
    F=sp.Function('F')(x); G=sp.Function('G')(x); w=sp.Function('w')(x)
    a=[sp.sqrt(F),sp.sqrt(x),sp.sqrt(x*sp.exp(w))]
    D=lambda q:2*sp.sqrt(G)*sp.diff(q,x)
    ap=[D(q) for q in a]; app=[D(q) for q in ap]
    lg=[ap[i]/a[i] for i in range(3)]; sec=[app[i]/a[i] for i in range(3)]
    ric=[-sum(sec)]
    for i,(j,k) in enumerate(((1,2),(0,2),(0,1))):
        ric.append(-sec[i]-lg[i]*(lg[j]+lg[k])+2*(a[i]**4-(a[j]**2-a[k]**2)**2)/(a[i]**2*a[j]**2*a[k]**2))
    s=sp.simplify(sum(ric)); m=s/4; ric0=sp.simplify(sum((q-m)**2 for q in ric))
    vol=sp.simplify(a[0]*a[1]*a[2]/(2*sp.sqrt(G))) # orbit volume /(2pi^2) per dx
    rep={sp.diff(F,x,2):F2,sp.diff(F,x):F1,sp.diff(G,x):G1,sp.diff(w,x,2):w2,sp.diff(w,x):w1,F:F0,G:G0,w:w0}
    # P/(8pi2) = int vol*ric0/4; scalar part = int vol*(s+24)^2/16
    return sp.simplify((vol*ric0/4).subs(rep)),sp.simplify((vol*(s+24)**2/16).subs(rep)),sp.simplify(s.subs(rep))
PD,SD,SE=symbolic()
ARGS=(x,F0,F1,F2,G0,G1,w0,w1,w2)
PF=sp.lambdify(ARGS,PD,'jax'); SF=sp.lambdify(ARGS,SD,'jax'); SC=sp.lambdify(ARGS,SE,'jax')

def cheb(n,z):
    T=[jnp.ones_like(z)]
    if n>1:T.append(z)
    for _ in range(2,n):T.append(2*z*T[-1]-T[-2])
    return jnp.stack(T)

def smooth(u): return u**3*(10-15*u+6*u*u)

class Cell:
    def __init__(self,x0,X,deg,nq=800):
        self.x0,self.X,self.deg=x0,X,deg; self.ell=np.log(X/x0); self.nparam=3*deg
        e,w=np.polynomial.legendre.leggauss(nq); self.u=jnp.asarray((e+1)/2); self.wq=jnp.asarray(w/2)
    def fields(self,z):
        d=self.deg; cF=z[:d];cG=z[d:2*d];cW=z[2*d:]
        # bolt: F'(x0)G'(x0)=1.  The base below has F'=G'=1 before the
        # exponential factors, so qF(0)+qG(0)=0.
        T0=cheb(d,jnp.array(-1.0)); cG=cG.at[0].add(-jnp.sum(cF*T0)-jnp.sum(cG*T0))
        def prof(xx):
            uu=jnp.log(xx/self.x0)/self.ell; ss=2*uu-1; S=smooth(uu); B=cheb(d,ss)
            qF=(1-uu)**3*jnp.sum(cF*B);qG=(1-uu)**3*jnp.sum(cG*B)
            # exact H4 exterior: F=x, G=x+2x^2, w=0.  Both vanish at bolt and stay positive.
            FF=(xx-self.x0)*jnp.exp(qF)+self.x0*S
            GG=((xx-self.x0)+(2*xx**2+self.x0)*S)*jnp.exp(qG)
            ww=uu**2*(1-uu)**3*jnp.sum(cW*B)
            return FF,GG,ww
        def at(uu):
            xx=self.x0*jnp.exp(self.ell*uu)
            ff=lambda yy:prof(yy)[0];gg=lambda yy:prof(yy)[1];ww=lambda yy:prof(yy)[2]
            F,G,w=prof(xx); vals=(xx,F,jax.grad(ff)(xx),jax.grad(jax.grad(ff))(xx),G,jax.grad(gg)(xx),w,jax.grad(ww)(xx),jax.grad(jax.grad(ww))(xx))
            return PF(*vals),SF(*vals),SC(*vals),xx,F,G,w
        p,s,sc,xx,F,G,w=jax.vmap(at)(self.u); dx=self.wq*self.ell*xx
        return p,s,sc,dx,F,G,w
    def costs(self,z):
        p,s,sc,dx,*_=self.fields(z); P=jnp.sum(p*dx);S=jnp.sum(s*dx);return P,P+S,S

def run(x0,X,deg,target,nq,seed=None,maxiter=7000,biaxial=False,random_scale=0.,random_seed=0):
    c=Cell(x0,X,deg,nq); z0=np.zeros(c.nparam)
    if seed:
        r=json.loads(Path(seed).read_text()); old=np.asarray(r['z']);od=int(r['deg']);
        for j in range(3):z0[j*deg:j*deg+min(od,deg)]=old[j*od:j*od+min(od,deg)]
    if random_scale:
        rng=np.random.default_rng(random_seed); z0 += random_scale*rng.standard_normal(c.nparam)
    idx=0 if target=='P' else 1
    if biaxial:
        y0=z0[:2*deg]
        lift=lambda y:jnp.concatenate([y,jnp.zeros(deg)])
        f=jax.jit(lambda y:c.costs(lift(y))[idx]);g=jax.jit(jax.grad(lambda y:c.costs(lift(y))[idx]))
        p0,j0,s0=map(float,c.costs(lift(jnp.asarray(y0))));_=float(f(jnp.asarray(y0)));_=np.asarray(g(jnp.asarray(y0)))
        t=time.time();res=minimize(lambda y:float(f(jnp.asarray(y))),y0,jac=lambda y:np.asarray(g(jnp.asarray(y))),method='L-BFGS-B',options=dict(maxiter=maxiter,ftol=1e-16,gtol=1e-12,maxls=80))
        zout=np.r_[res.x,np.zeros(deg)]
    else:
        f=jax.jit(lambda z:c.costs(z)[idx]);g=jax.jit(jax.grad(lambda z:c.costs(z)[idx]))
        p0,j0,s0=map(float,c.costs(jnp.asarray(z0)));_=float(f(jnp.asarray(z0)));_=np.asarray(g(jnp.asarray(z0)))
        t=time.time();res=minimize(lambda z:float(f(jnp.asarray(z))),z0,jac=lambda z:np.asarray(g(jnp.asarray(z))),method='L-BFGS-B',options=dict(maxiter=maxiter,ftol=1e-16,gtol=1e-12,maxls=80))
        zout=res.x
    P,J,S=map(float,c.costs(jnp.asarray(zout)));_,_,_,_,F,G,w=c.fields(jnp.asarray(zout))
    return dict(background='H4_Ric-6',x0=x0,X=X,deg=deg,target=target,nq=nq,biaxial=biaxial,
                random_scale=random_scale,random_seed=random_seed,P0=p0,J0=j0,P=P,J=J,scalar=S,
                minF=float(F.min()),minG=float(G.min()),maxabsw=float(jnp.max(jnp.abs(w))),success=bool(res.success),
                nit=int(res.nit),grad_inf=float(np.max(np.abs(res.jac))),z=zout.tolist(),sec=time.time()-t)

def main():
    p=argparse.ArgumentParser();p.add_argument('x0',type=float);p.add_argument('X',type=float);p.add_argument('deg',type=int);p.add_argument('target',choices=['P','J']);p.add_argument('out');p.add_argument('--nq',type=int,default=800);p.add_argument('--seed');p.add_argument('--biaxial',action='store_true');p.add_argument('--random-scale',type=float,default=0.);p.add_argument('--random-seed',type=int,default=0);a=p.parse_args()
    r=run(a.x0,a.X,a.deg,a.target,a.nq,a.seed,biaxial=a.biaxial,random_scale=a.random_scale,random_seed=a.random_seed);print(json.dumps(r));Path(a.out).write_text(json.dumps(r)+'\n')
if __name__=='__main__':main()

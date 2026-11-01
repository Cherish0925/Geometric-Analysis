#!/usr/bin/env python3
"""Search scalar-minus-six T^3 centers for reduced initial contraction.

For f(z)=sum_{k=1}^K a_k sin(kz), let
 h_f=dz^2+exp(2f)dx^2+exp(-2f)dy^2.
Solve -8u''-2(f')^2u=-6u^5 and q=u^4 h_f.  Since R_q=-6,
P=Ric_q+3I=S'(0), and in dimension 3 each complementary sectional curvature
is -P_i.  We minimize sup max(K_q,0)=-min P, the worst initial contraction of
the reflected Koiso germ.

Numerical shape search only; it cannot establish an infimum over all T^3
metrics or over this Fourier family.
"""
from __future__ import annotations
import json,sys,time
from pathlib import Path
import numpy as np
from scipy.integrate import solve_bvp
from scipy.optimize import differential_evolution,minimize

MODE=sys.argv[1] if len(sys.argv)>1 else 'pilot'
if MODE=='pilot': K,MAXITER,POPSIZE=(3,14,8)
elif MODE=='refine': K,MAXITER,POPSIZE=(4,28,10)
else: raise ValueError(MODE)
TWOPI=2*np.pi
cache={}

def evaluate(coeff,dense=False):
    coeff=np.asarray(coeff,float); key=tuple(np.round(coeff,10))+(dense,)
    if key in cache:return cache[key]
    def fp(x): return sum((k+1)*coeff[k]*np.cos((k+1)*x) for k in range(K))
    def fpp(x): return sum(-(k+1)**2*coeff[k]*np.sin((k+1)*x) for k in range(K))
    def ode(x,y):
        u,up=y; return np.vstack((up,.75*u**5-.25*fp(x)**2*u))
    def bc(ya,yb):return np.array([ya[0]-yb[0],ya[1]-yb[1]])
    n=601 if not dense else 1201; x=np.linspace(0,TWOPI,n)
    mean=np.mean(fp(x)**2); u0=max((mean/3)**.25,.08)
    guess=np.vstack((u0*(1+.015*np.cos(2*x)),-.03*u0*np.sin(2*x)))
    try:
        sol=solve_bvp(ode,bc,x,guess,tol=3e-8 if not dense else 2e-10,max_nodes=25000)
        if not sol.success: raise RuntimeError(sol.message)
        xx=np.linspace(0,TWOPI,2001 if not dense else 8001)
        u,up=sol.sol(xx); upp=ode(xx,np.vstack((u,up)))[1]
        pp=2*up/u; ppp=2*(upp/u-(up/u)**2)
        r=np.vstack((-2*fp(xx)**2-2*ppp,
          -fpp(xx)-fp(xx)*pp-ppp-pp**2,
           fpp(xx)+fp(xx)*pp-ppp-pp**2))/u**4
        P=r+3; scalar=r.sum(0)
        posK=np.maximum(-P,0)
        # p=16 smooth maximum for optimization; report true grid maximum separately.
        scale=max(float(posK.max()),1e-10); smooth=scale*(np.mean((posK/scale)**16)+1e-30)**(1/16)
        row={'success':True,'coeff':[float(x) for x in coeff],
          'objective_smooth':float(smooth),'max_positive_sectional':float(posK.max()),
          'P_min':float(P.min()),'P_max':float(P.max()),
          'P_component_min':[float(v.min()) for v in P],
          'P_component_max':[float(v.max()) for v in P],
          'scalar_error':float(np.abs(scalar+6).max()),'traceP_error':float(np.abs(P.sum(0)-3).max()),
          'u_min':float(u.min()),'u_max':float(u.max()),'nodes':int(sol.x.size),
          'fprime_rms':float(np.sqrt(np.mean(fp(xx)**2))),'fprime_max':float(np.abs(fp(xx)).max()),
          'volume':float(np.trapezoid(u**6,xx))}
    except Exception as e:
        row={'success':False,'coeff':[float(x) for x in coeff],'objective_smooth':1e4,'max_positive_sectional':1e4,'error':str(e)}
    cache[key]=row;return row

def obj(c):return evaluate(c)['objective_smooth']

def main():
    bounds=[(.15,10.0)]+[(-5.0,5.0)]*(K-1)
    baselines=[]
    for A in [.5,1,2,3,5,8]:
        c=np.zeros(K);c[0]=A;baselines.append(evaluate(c,True))
    t0=time.time()
    de=differential_evolution(obj,bounds,seed=7503,maxiter=MAXITER,popsize=POPSIZE,
      polish=False,workers=1,updating='immediate',tol=2e-4,atol=2e-4,disp=True)
    nm=minimize(obj,de.x,method='Nelder-Mead',options={'maxiter':350,'xatol':1e-5,'fatol':1e-5})
    best=evaluate(nm.x,True)
    # Keep the strongest evaluated points (coarse values) for landscape context.
    vals=sorted((v for k,v in cache.items() if v.get('success')),key=lambda x:x['objective_smooth'])[:20]
    out={'scope':'finite Fourier center-shape search; not a global infimum','mode':MODE,'K':K,
      'objective':'sup positive sectional curvature = -min(Ric+3I), sampled; smooth p16 optimized',
      'baselines':baselines,'differential_evolution':{'x':de.x.tolist(),'fun':float(de.fun),'nfev':int(de.nfev),'message':str(de.message)},
      'nelder_mead':{'x':nm.x.tolist(),'fun':float(nm.fun),'nfev':int(nm.nfev),'message':str(nm.message)},
      'best_dense':best,'top_coarse':vals,'wall_s':time.time()-t0}
    path=Path(__file__).resolve().parents[1]/'data'/f'step75_center_shape_search_{MODE}.json'
    path.write_text(json.dumps(out,indent=2),encoding='utf-8')
    print('BEST',json.dumps(best,indent=2));print('wrote',path)
if __name__=='__main__':main()

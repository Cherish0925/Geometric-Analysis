#!/usr/bin/env python3
"""General cohomogeneity-one scalar-minus-six T^3 center search.

Let h=dz^2+exp(2p(z))dx^2+exp(2q(z))dy^2 with independent periodic p,q.
Solve the Yamabe ODE for g=u^4 h and R_g=-6, then minimize
  ||Ric_g+2g||_{op,infinity},
the traceless Koiso acceleration.  The universal topological lower bound is 1:
if this norm were <1, all sectional curvatures would be strictly negative.

Finite Fourier search only, not an infimum theorem.
"""
from __future__ import annotations
import json,sys,time
from pathlib import Path
import numpy as np
from scipy.integrate import solve_bvp
from scipy.optimize import differential_evolution,minimize
MODE=sys.argv[1] if len(sys.argv)>1 else 'pilot'
if MODE=='pilot': K,MIT,POP=(2,18,9)
elif MODE=='refine': K,MIT,POP=(3,32,10)
else: raise ValueError(MODE)
TWOPI=2*np.pi; cache={}

def evalc(c,dense=False):
 c=np.asarray(c,float); key=tuple(np.round(c,9))+(dense,)
 if key in cache:return cache[key]
 ap=c[:K]; aq=c[K:]
 def vals(x):
  p=sum(ap[k]*np.sin((k+1)*x) for k in range(K)); q=sum(aq[k]*np.sin((k+1)*x) for k in range(K))
  pp=sum((k+1)*ap[k]*np.cos((k+1)*x) for k in range(K)); qp=sum((k+1)*aq[k]*np.cos((k+1)*x) for k in range(K))
  ppp=sum(-(k+1)**2*ap[k]*np.sin((k+1)*x) for k in range(K)); qpp=sum(-(k+1)**2*aq[k]*np.sin((k+1)*x) for k in range(K))
  return p,q,pp,qp,ppp,qpp
 def Rh(x):
  p,q,pp,qp,ppp,qpp=vals(x); return -2*(ppp+qpp+pp**2+qp**2+pp*qp)
 def ode(x,y):
  u,up=y; p,q,pp,qp,ppp,qpp=vals(x); rr=Rh(x)
  return np.vstack((up,-(pp+qp)*up+(rr*u+6*u**5)/8))
 def bc(ya,yb):return np.array([ya[0]-yb[0],ya[1]-yb[1]])
 try:
  x=np.linspace(0,TWOPI,801); rav=np.mean(Rh(x)); u0=max((-rav/6)**.25 if rav<0 else .45,.1)
  guess=np.vstack((u0*(1+.01*np.cos(x)),np.zeros_like(x)))
  sol=solve_bvp(ode,bc,x,guess,tol=5e-8 if not dense else 3e-10,max_nodes=30000)
  if not sol.success:raise RuntimeError(sol.message)
  xx=np.linspace(0,TWOPI,2401 if not dense else 10001);u,up=sol.sol(xx);upp=ode(xx,np.vstack((u,up)))[1]
  p,q,pp,qp,ppp,qpp=vals(xx)
  phi=2*up/u; phipp=2*(upp/u-(up/u)**2)
  rh0=-(ppp+pp**2)-(qpp+qp**2)
  rhx=-(ppp+pp**2+pp*qp); rhy=-(qpp+qp**2+pp*qp)
  ric=np.vstack((rh0-2*phipp-(pp+qp)*phi,
    rhx-phipp-(2*pp+qp)*phi-phi**2,
    rhy-phipp-(pp+2*qp)*phi-phi**2))/u**4
  E=ric+2; P=ric+3; scalar=ric.sum(0)
  scale=max(float(np.abs(E).max()),1e-10); smooth=scale*(np.mean((np.abs(E)/scale)**18)+1e-30)**(1/18)
  row={'success':True,'coeff_p':ap.tolist(),'coeff_q':aq.tolist(),'objective_smooth':float(smooth),
   'E_op_sup':float(np.abs(E).max()),'E_component_range':[[float(x.min()),float(x.max())] for x in E],
   'max_positive_sectional':float(np.maximum(-P,0).max()),'P_min':float(P.min()),'P_max':float(P.max()),
   'scalar_error':float(np.abs(scalar+6).max()),'traceE_error':float(np.abs(E.sum(0)).max()),
   'u_min':float(u.min()),'u_max':float(u.max()),'nodes':int(sol.x.size),
   'base_scalar_range':[float(Rh(xx).min()),float(Rh(xx).max())],
   'volume':float(np.trapezoid(u**6*np.exp(p+q),xx))}
 except Exception as e:row={'success':False,'coeff':c.tolist(),'objective_smooth':1e5,'E_op_sup':1e5,'error':str(e)}
 cache[key]=row;return row

def obj(c):return evalc(c)['objective_smooth']
def main():
 # Include reciprocal and equal-warps baselines.
 bas=[]
 for A in [.5,1,2,4,8]:
  c=np.zeros(2*K);c[0]=A;c[K]=-A;bas.append({'type':'reciprocal',**evalc(c,True)})
  c=np.zeros(2*K);c[0]=A;c[K]=A;bas.append({'type':'equal',**evalc(c,True)})
 bounds=[(-8,8)]*(2*K);t0=time.time()
 de=differential_evolution(obj,bounds,seed=7511,maxiter=MIT,popsize=POP,polish=False,tol=5e-4,atol=5e-4,disp=True)
 nm=minimize(obj,de.x,method='Nelder-Mead',options={'maxiter':550,'xatol':2e-5,'fatol':2e-5})
 best=evalc(nm.x,True)
 top=sorted((v for v in cache.values() if v.get('success')),key=lambda r:r['objective_smooth'])[:20]
 out={'scope':'finite independent p,q Fourier search; not an infimum','mode':MODE,'K':K,'universal_lower_bound':1,
  'objective':'sup operator norm Ric+2g, smoothed p18 for optimization','baselines':bas,
  'differential_evolution':{'x':de.x.tolist(),'fun':float(de.fun),'nfev':int(de.nfev)},
  'nelder_mead':{'x':nm.x.tolist(),'fun':float(nm.fun),'nfev':int(nm.nfev),'message':str(nm.message)},
  'best_dense':best,'top_coarse':top,'wall_s':time.time()-t0}
 path=Path(__file__).resolve().parents[1]/'data'/f'step75_general_center_shape_search_{MODE}.json';path.write_text(json.dumps(out,indent=2),encoding='utf-8')
 print('BEST',json.dumps(best,indent=2));print('wrote',path)
if __name__=='__main__':main()

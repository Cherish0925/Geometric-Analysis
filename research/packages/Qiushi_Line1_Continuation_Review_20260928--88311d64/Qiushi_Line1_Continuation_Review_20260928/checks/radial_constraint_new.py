from radial_search_new import Model
import numpy as np
from scipy.optimize import minimize
import json,time,sys

def profiles(m,p):
 v,vt,vtt=np.einsum('ijk,k->ij',m.B[0],p[:m.n]);w,wt,wtt=np.einsum('ijk,k->ij',m.B[1],p[m.n:2*m.n]);phi,pt,ptt=np.einsum('ijk,k->ij',m.B[2],p[2*m.n:]);F=np.exp(v)*m.F0
 return F,w,wt,phi,pt

def ct(m,p):
 F,w,wt,phi,pt=profiles(m,p)
 return np.sum(m.weights*m.mu/m.r2*(2*F*(pt**2-wt**2)-8*(np.cosh(2*w)-1)-8*np.sinh(2*w)**2/F))-(m.mu+2)

def cjac(m,p):
 out=np.empty(m.dim)
 for k in range(m.dim):
  pc=p.astype(complex);pc[k]+=1e-24j;out[k]=ct(m,pc).imag/1e-24
 return out
if __name__ == '__main__':
 mu=float(sys.argv[1]) if len(sys.argv)>1 else .001;R=float(sys.argv[2]) if len(sys.argv)>2 else 3.;n=3
 m=Model(mu,R,n,q=24)
 for sign in [1,-1]:
  p=np.zeros(m.dim);p[2*m.n+n]=1;C=ct(m,p)+mu+2;p[2*m.n+n]=sign*np.sqrt((mu+2)/C)
  print('start',sign,m.fun(p),ct(m,p),p[2*m.n+n],flush=True)
  start=time.time(); opt=minimize(m.fun,p,jac=m.jac,method='SLSQP',constraints=[{'type':'eq','fun':lambda p:ct(m,p),'jac':lambda p:cjac(m,p)}],bounds=[(-5,5)]*m.dim,options={'maxiter':700,'ftol':1e-10})
  high=Model(mu,R,n,q=46)
  print(json.dumps({'mu':mu,'R':R,'sign':sign,'j':float(opt.fun),'check':float(high.fun(opt.x)),'constraint':float(ct(m,opt.x)),'check_constraint':float(ct(high,opt.x)),'success':bool(opt.success),'msg':str(opt.message),'nit':int(opt.nit),'elapsed':time.time()-start,'p':opt.x.tolist()}),flush=True)

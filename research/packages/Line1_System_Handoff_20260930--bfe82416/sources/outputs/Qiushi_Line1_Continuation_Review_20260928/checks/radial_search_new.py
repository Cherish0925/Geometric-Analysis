import numpy as np
from numpy.polynomial import Polynomial,Legendre
from scipy.special import expit
from scipy.optimize import minimize
from numpy.polynomial.legendre import leggauss
import json,sys,time

def cutoff(x):
 y=(x-.6)/.3; S=np.zeros_like(x); S[x>=.9]=1
 d=np.zeros_like(x); dd=np.zeros_like(x); m=(x>.6)&(x<.9)
 q=y[m]; k=-1/q+1/(1-q); a=expit(k); kp=1/q**2+1/(1-q)**2; kpp=-2/q**3+2/(1-q)**3
 S[m]=a; d[m]=a*(1-a)*kp/.3; dd[m]=a*(1-a)*(kpp+(1-2*a)*kp**2)/.3**2
 return 1-S,-d,-dd

def basis(x,xt,xtt,p,n):
 c,cd,cdd=cutoff(x); arr=[]
 for k in range(n):
  pol=Legendre.basis(k).convert(kind=Polynomial)(Polynomial([-1,2]))*Polynomial([0]*p+[1])
  z=pol(x);zd=pol.deriv()(x);zdd=pol.deriv(2)(x)
  norm=np.max(np.abs(pol(np.linspace(0,1,3001))*cutoff(np.linspace(0,1,3001))[0]))
  arr.append(np.array([z*c,(zd*c+z*cd)*xt,(zdd*c+2*zd*cd+z*cdd)*xt**2+(zd*c+z*cd)*xtt])/norm)
 return np.array(arr).transpose(1,2,0)

class Model:
 def __init__(self,mu,R,n=3,q=22):
  self.mu=mu;self.R=R;L=np.log(R/np.sqrt(mu));self.L=L
  edges=np.unique(np.r_[np.linspace(0,L,max(25,int(L*10))),np.array([.6,.9])*L,np.array([.6,.9])*np.log(8),np.log(np.sqrt(mu+(R*R-mu)*np.array([.6,.9]))/np.sqrt(mu))])
  edges=edges[(edges>=0)&(edges<=L)];g,gw=leggauss(q);t=np.concatenate([(a+b)/2+(b-a)/2*g for a,b in zip(edges[:-1],edges[1:])]);self.weights=np.concatenate([(b-a)/2*gw for a,b in zip(edges[:-1],edges[1:])]);self.t=t; r2=mu*np.exp(2*t);self.r2=r2
  data=[(t/L,np.ones_like(t)/L,np.zeros_like(t)),(t/np.log(8),np.ones_like(t)/np.log(8),np.zeros_like(t)),((r2-mu)/(R*R-mu),2*r2/(R*R-mu),4*r2/(R*R-mu))]
  self.B=[np.concatenate([basis(*args,p,n) for args in data],axis=2) for p in [1,2,0]]; self.n=3*n; self.dim=9*n
  x,xt,xtt=data[2];c,cx,cxx=cutoff(x);ct=cx*xt;ctt=cxx*xt**2+cx*xtt
  a=mu+mu**2/2;b=mu**3/3;H=-a/r2+b/r2**2;Ht=2*a/r2-4*b/r2**2;Htt=-4*a/r2+16*b/r2**2
  self.F0=1+r2/6+c*H;self.F0t=r2/3+ct*H+c*Ht;self.F0tt=2*r2/3+ctt*H+2*ct*Ht+c*Htt
 def residual(self,par):
  v,vt,vtt=np.einsum('ijk,k->ij',self.B[0],par[:self.n]);w,wt,wtt=np.einsum('ijk,k->ij',self.B[1],par[self.n:2*self.n]);p,pt,ptt=np.einsum('ijk,k->ij',self.B[2],par[2*self.n:])
  ev=np.exp(v);F=ev*self.F0;Ft=ev*(self.F0t+self.F0*vt);Ftt=ev*(self.F0tt+2*self.F0t*vt+self.F0*(vtt+vt**2)); a=np.exp(2*p)
  EV=self.r2-.5*(Ftt+4*Ft);EH=self.r2-Ft+4*(1-F);ep=self.r2*(a-1)
  D0=EV+ep-3*F*ptt-2*Ft*pt
  D3=EV+ep-F*ptt-(2*Ft+4*F)*pt-2*F*pt**2
  DH=EH+ep-F*ptt-(Ft+4*F)*pt-2*F*pt**2
  c=4*(np.cosh(2*w)-1);z=8*np.sinh(2*w)**2/F
  U=-F*wtt-(Ft+2*F)*wt+4*np.sinh(4*w)/F-4*np.sinh(2*w)
  res=np.array([D0-2*F*wt**2,D3-z,np.sqrt(2)*(DH+c),np.sqrt(2)*(U-2*F*pt*wt)])
  return res
 def fun(self,p):
  return np.sum(self.weights*np.sum(self.residual(p)**2,axis=0))
 def jac(self,p):
  out=np.empty(self.dim)
  for k in range(self.dim):
   pc=p.astype(complex);pc[k]+=1e-24j;out[k]=self.fun(pc).imag/1e-24
  return out

if __name__=='__main__':
 mu=float(sys.argv[1]) if len(sys.argv)>1 else .001;R=float(sys.argv[2]) if len(sys.argv)>2 else 3.;n=int(sys.argv[3]) if len(sys.argv)>3 else 3;starts=int(sys.argv[4]) if len(sys.argv)>4 else 4
 m=Model(mu,R,n);rng=np.random.default_rng(20260928); print('baseline',m.fun(np.zeros(m.dim)),flush=True)
 for seed in range(starts):
  p0=np.zeros(m.dim)
  if seed:
   p0=rng.normal(0,.15,m.dim);p0[2*m.n:]+=rng.normal(0,.3,m.n)
  start=time.time();opt=minimize(m.fun,p0,jac=m.jac,method='L-BFGS-B',bounds=[(-2,2)]*m.dim,options={'maxiter':700,'maxls':40,'gtol':1e-7,'ftol':1e-12})
  chk=Model(mu,R,n,q=42).fun(opt.x)
  rec={'mu':mu,'R':R,'n':n,'seed':seed,'j':float(opt.fun),'j_check':float(chk),'success':bool(opt.success),'message':str(opt.message),'iters':int(opt.nit),'grad_inf':float(np.max(abs(opt.jac))),'elapsed':time.time()-start,'p':opt.x.tolist()}
  print(json.dumps(rec),flush=True)

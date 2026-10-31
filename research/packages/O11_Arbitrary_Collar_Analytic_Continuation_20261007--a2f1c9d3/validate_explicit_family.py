"""Floating/high-precision checks only; analytic remainder proof is separate."""
import mpmath as mp
import numpy as np
import json, argparse
mp.mp.dps=65
class J:
 def __init__(self,x,d=0,dd=0): self.x=mp.mpf(x);self.d=mp.mpf(d);self.dd=mp.mpf(dd)
 @staticmethod
 def of(x):return x if isinstance(x,J) else J(x)
 def __add__(self,y):
  y=J.of(y);return J(self.x+y.x,self.d+y.d,self.dd+y.dd)
 __radd__=__add__
 def __neg__(self):return J(-self.x,-self.d,-self.dd)
 def __sub__(self,y):return self+-J.of(y)
 def __rsub__(self,y):return J.of(y)+-self
 def __mul__(self,y):
  y=J.of(y);return J(self.x*y.x,self.d*y.x+self.x*y.d,self.dd*y.x+2*self.d*y.d+self.x*y.dd)
 __rmul__=__mul__
 def inv(self):return J(1/self.x,-self.d/self.x**2,2*self.d**2/self.x**3-self.dd/self.x**2)
 def __truediv__(self,y):return self*J.of(y).inv()
 def __rtruediv__(self,y):return J.of(y)*self.inv()
 def fun(self,f,df,ddf):return J(f(self.x),df(self.x)*self.d,ddf(self.x)*self.d**2+df(self.x)*self.dd)
 def sqrt(self):return self.fun(mp.sqrt,lambda x:1/(2*mp.sqrt(x)),lambda x:-1/(4*x**mp.mpf('1.5')))
 def exp(self):return self.fun(mp.exp,mp.exp,mp.exp)
 def log(self):return self.fun(mp.log,lambda x:1/x,lambda x:-1/x**2)
 def sinh(self):return self.fun(mp.sinh,mp.cosh,mp.sinh)
 def cosh(self):return self.fun(mp.cosh,mp.sinh,mp.cosh)
 def __pow__(self,n):
  if n==0:return J(1)
  if n<0:return (self**(-n)).inv()
  res=J(1)
  for _ in range(n):res=res*self
  return res

def cutoff(x):
 if x.x<=1:return J(0)
 if x.x>=2:return J(1)
 a=(-(x-1).inv()).exp();b=(-(2-x).inv()).exp()
 return a/(a+b)

def lengths(t,ep,T):
 t=J(t,1);sh=t.sinh();ch=t.cosh()
 B=[(t*t+ep).sqrt(),(t*t+ep).sqrt(),t]
 C=[sh,sh*ch,sh]
 N=[(sh*sh+ep).sqrt()*mp.exp(ep*mp.mpf(9)/4),
    (sh*sh+ep).sqrt()*ch*mp.exp(ep*mp.mpf(3)/4),
    sh*mp.exp(ep/2)]
 qi=cutoff(t/mp.sqrt(ep));qo=1-cutoff(t/T)
 return [C[i]*(qo*((B[i]/C[i]).log()+qi*(N[i]/B[i]).log())).exp() for i in range(3)]

def density(t,ep,T):
 a=lengths(t,ep,T);u=[];ud=[]
 for i in range(3):
  j,k=(i+1)%3,(i+2)%3
  ga=(a[j]*a[j]+a[k]*a[k]-a[i]*a[i])/(a[j]*a[k])
  u.append(a[i].d-ga.x);ud.append(a[i].dd-ga.d)
 av=[x.x for x in a]
 H=[u[i]+u[(i+1)%3]*u[(i+2)%3]/2 for i in range(3)]
 la=[av[(i+1)%3]*av[(i+2)%3]/av[i] for i in range(3)]
 s1=la[0]/4*(ud[0]+2*H[0]/la[0])**2
 s2=la[1]/4*(ud[1]-(2*u[1]-u[0]*u[2])/la[1])**2
 s3=la[2]/4*(ud[2]+2*H[2]/la[2])**2
 cub=2*u[0]*u[1]*u[2]/la[1]
 sig=sum(ud[i]/av[i]+2*H[i]/(av[(i+1)%3]*av[(i+2)%3]) for i in range(3))
 sc=av[0]*av[1]*av[2]/4*(sig-12)**2
 return s1+s2+s3+cub,sc

def integ(fun,a,b,n):
 xs,ws=np.polynomial.legendre.leggauss(n)
 out=[mp.mpf(0),mp.mpf(0)]
 for xx,ww in zip(xs,ws):
  x=(a+b)/2+(b-a)/2*mp.mpf(float(xx));val=fun(x)
  for i in range(2):out[i]+=mp.mpf(float(ww))*(b-a)/2*val[i]
 return out

def evaluate(ep,T,n):
 ep=mp.mpf(ep);T=mp.mpf(T)
 # inner exact Burns region: relative P = 0, scalar = 27 ep^2
 out=[mp.mpf(0),27*ep**2]
 v=integ(lambda r:tuple(x*mp.sqrt(ep) for x in density(mp.sqrt(ep)*r,ep,T)),mp.mpf(1),mp.mpf(2),n)
 for i in range(2):out[i]+=v[i]
 v=integ(lambda s:tuple(x*mp.exp(s) for x in density(mp.exp(s),ep,T)),mp.log(2*mp.sqrt(ep)),mp.log(T),n)
 for i in range(2):out[i]+=v[i]
 v=integ(lambda t:density(t,ep,T),T,2*T,n)
 for i in range(2):out[i]+=v[i]
 return {'epsilon':mp.nstr(ep,8),'T':mp.nstr(T,8),'quadrature_order':n,
         'P_minus_1_over_e2':mp.nstr(out[0]/ep**2,30),
         'J_minus_1_over_e2':mp.nstr(sum(out)/ep**2,30),
         'P_remainder_scaled':mp.nstr(out[0]/ep**2+9*mp.log(1/ep),30),
         'J_remainder_scaled':mp.nstr(sum(out)/ep**2+9*mp.log(1/ep),30),
         'scalar_over_e2':mp.nstr(out[1]/ep**2,30)}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--n',type=int,default=96);p.add_argument('--T',default='1');p.add_argument('--eps',nargs='+',default=['1e-4','1e-6','1e-8','1e-10']);args=p.parse_args()
 rows=[]
 for ep in args.eps:
  r=evaluate(ep,args.T,args.n);rows.append(r);print(json.dumps(r),flush=True)
 with open('/mnt/data/line1_analytic_continuation_20261007/explicit_family_validation_'+str(args.n)+'.json','w') as f:json.dump(rows,f,indent=2)

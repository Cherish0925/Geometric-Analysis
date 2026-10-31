import numpy as np
from scipy.special import roots_legendre
from scipy.optimize import minimize
import json,sys,time
n=int(sys.argv[1]) if len(sys.argv)>1 else 192
z,wq=roots_legendre(n); x=(z+1)/2; wq=wq/2
D=6

def smooth(a,b):
 t=np.clip((x-a)/(b-a),0,1); mid=(x>a)&(x<b)
 s=35*t**4-84*t**5+70*t**6-20*t**7
 d=(140*t**3-420*t**4+420*t**5-140*t**6)/(b-a)*mid
 dd=(420*t**2-1680*t**3+2100*t**4-840*t**5)/(b-a)**2*mid
 return s,d,dd
s,sp,spp=smooth(.4,.8)
c,cp,cpp=smooth(.72,.95); c,cp,cpp=1-c,-cp,-cpp

def bases(p):
 F=[];Fp=[];Fpp=[]
 for j in range(D):
  a=j*np.pi; co=np.cos(a*x); si=np.sin(a*x)
  f=x**p*co; fp=p*x**(p-1)*co-a*x**p*si
  fpp=p*(p-1)*x**(p-2)*co-2*p*a*x**(p-1)*si-a*a*x**p*co
  F.append(c*f); Fp.append(cp*f+c*fp); Fpp.append(cpp*f+2*cp*fp+c*fpp)
 return np.array(F),np.array(Fp),np.array(Fpp)
f,fp,fpp=bases(2); g,gp,gpp=bases(4)

def value(p,details=False):
 R=np.exp(p[0]); T=R*np.exp(p[1]); a0=np.exp(p[2]); t=T*x
 r=np.where(x>.4,R+T*(x-1),R/3); y=r/np.sqrt(6)
 ba=.5*np.log(a0*a0+t*t); bap=T*T*x/(a0*a0+t*t); bapp=T*T*(a0*a0-t*t)/(a0*a0+t*t)**2
 bb=np.log(t); bbp=1/x; bbpp=-1/x**2
 ca=np.log(np.sqrt(6)*np.sinh(y)); cap=T/np.sqrt(6)/np.tanh(y); capp=-T*T/6/np.sinh(y)**2
 cb=ca+np.log(np.cosh(y)); cbp=cap+T/np.sqrt(6)*np.tanh(y); cbpp=capp+T*T/6/np.cosh(y)**2
 def mix(a,ap,app,b,bp,bpp): return (1-s)*a+s*b,(1-s)*ap+s*bp+sp*(b-a),(1-s)*app+s*bpp+2*sp*(bp-ap)+spp*(b-a)
 a,ap,app=mix(ba,bap,bapp,ca,cap,capp); b,bp,bpp=mix(bb,bbp,bbpp,cb,cbp,cbpp)
 aa=p[3:3+D]; bbv=p[3+D:3+2*D]; ww=p[3+2*D:3+3*D]
 a=a+aa@f; ap=ap+aa@fp; app=app+aa@fpp
 b=b+bbv@f; bp=bp+bbv@fp; bpp=bpp+bbv@fpp
 v=ww@g; vp=ww@gp; vpp=ww@gpp
 L=np.array([a+v,a-v,b]); Lp=np.array([ap+vp,ap-vp,bp])/T; Lpp=np.array([app+vpp,app-vpp,bpp])/T**2
 A2=np.exp(2*L); ratio2=Lpp+Lp**2
 lam0=-ratio2.sum(0)
 lam=[]
 prod=A2.prod(0)
 for i in range(3):
  j=(i+1)%3; k=(i+2)%3
  lam.append(-ratio2[i]-Lp[i]*(Lp[j]+Lp[k])+2*(A2[i]**2-(A2[j]-A2[k])**2)/prod)
 lam=np.array(lam)
 dens=np.exp(L.sum(0))*((lam0+1)**2+((lam+1)**2).sum(0))*T
 J=np.dot(wq,dens)
 if details:return {'J_over_2pi2':float(J.real),'ratio_to_8pi2':float(J.real/4),'R':float(R.real),'T':float(T.real),'a0':float(a0.real),'maxw':float(np.max(np.abs(v))),'p':[float(q.real) for q in p]}
 return J

def jac(p):
 out=[]
 for k in range(len(p)):
  q=p.astype(complex);q[k]+=1j*1e-20
  out.append(value(q).imag/1e-20)
 return np.array(out)

rng=np.random.default_rng(830)
bounds=[(-1,2.7),(-.65,.4),(-4,1.5)]+[(-10,10)]*(3*D)
start=time.time(); results=[]
for case in range(12):
 p=np.zeros(3+3*D);p[:3]=[np.log([1,2,4,6][case%4]),0,np.log([.1,.4,.8][case//4])]
 if case>0:p[3:]=rng.normal(0,.07,3*D)
 ret=minimize(lambda p:float(value(p)),p,jac=jac,method='L-BFGS-B',bounds=bounds,options={'maxiter':400,'ftol':1e-12,'gtol':1e-7,'maxls':30})
 out=value(ret.x,True);out.update(case=case,iterations=int(ret.nit),success=bool(ret.success),message=str(ret.message),elapsed=time.time()-start)
 results.append(out); print(json.dumps(out),flush=True)
 with open('/tmp/o11_triaxial_results.json','w') as h:json.dump(results,h,indent=2)

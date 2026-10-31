from radial_search_new import Model
from radial_constraint_new import profiles,ct,cjac
from scipy.optimize import minimize
import numpy as np,json,time
m=Model(.001,3,3,q=24);rng=np.random.default_rng(773)
for target in [.1,.5,1.,2.001]:
 for sign in [1,-1]:
  p=np.zeros(m.dim);p[m.n:2*m.n]=rng.normal(0,.02,m.n);p[2*m.n+3]=1
  fixed=ct(m,np.r_[p[:2*m.n],np.zeros(m.n)])+m.mu+2
  C=ct(m,p)+m.mu+2-fixed;p[2*m.n+3]=sign*np.sqrt((target-fixed)/C)
  fun=lambda p:ct(m,p)+(m.mu+2)-target
  t=time.time();opt=minimize(m.fun,p,jac=m.jac,method='SLSQP',constraints=[{'type':'eq','fun':fun,'jac':lambda p:cjac(m,p)}],bounds=[(-5,5)]*m.dim,options={'maxiter':700,'ftol':2e-10})
  high=Model(.001,3,3,q=46)
  print(json.dumps({'mu':.001,'R':3,'target_muTminusP':target,'sign':sign,'j':float(opt.fun),'j_check':float(high.fun(opt.x)),'constraint_error':float(fun(opt.x)),'constraint_check_error':float(ct(high,opt.x)+2.001-target),'success':bool(opt.success),'message':str(opt.message),'nit':int(opt.nit),'elapsed':time.time()-t,'w_coefficient_norm':float(np.linalg.norm(opt.x[m.n:2*m.n])),'p':opt.x.tolist()}),flush=True)

"""Direct least-squares matching of full SPD logarithmic matrix nodal fields.

Unknowns are the six symmetric components of X at every interior Chebyshev-Fourier
node on a half cylinder. Endpoint values are fixed to the charged Koiso center and
expanding attachment. Exact first/second endpoint jets are imposed in residual
evaluation. A small H2 regularizer keeps the finite discretization stable; its
weight is reported separately from the geometric residual.
"""
from pathlib import Path
import argparse,importlib.util,json,math,numpy as np
from scipy.optimize import least_squares
HERE=Path(__file__).resolve().parent;SESSION=HERE.parents[1]
p=HERE/'step98_full_matrix_joint_transition.py';sp=importlib.util.spec_from_file_location('fm',p);fm=importlib.util.module_from_spec(sp);sp.loader.exec_module(fm)


def pack_sym(X):return np.stack([X[:,:,i,j] for i,j in fm.PAIR3],axis=2).ravel()
def unpack_sym(v,nri,ns):
 z=v.reshape(nri,ns,6);X=np.zeros((nri,ns,3,3))
 for c,(i,j) in enumerate(fm.PAIR3):X[:,:,i,j]=z[:,:,c];X[:,:,j,i]=z[:,:,c]
 return X

def baseline_X(geom,R,nr,sign):
 t,Dt,D2t=fm.chebyshev_lobatto_01(nr);ns=len(geom['s']);I=np.eye(3)[None,:,:]*np.ones((ns,1,1));z=np.zeros_like(I)
 coeff=fm.quintic_coefficients(z,2*sign*geom['A'],2*geom['B'],2*R*I,2*I,np.zeros_like(I),R)
 return t,Dt/R,D2t/(R*R),fm.eval_poly(coeff,t)

def q_from_X(geom,X):
 q=np.zeros_like(X)
 for a in range(len(X)):
  for b in range(X.shape[1]):q[a,b]=geom['sq'][b]@fm.sym_exp(X[a,b])@geom['sq'][b]
 return q

def solve_side(geom,R,nr,sign,max_nfev,reg,exclude_endpoints):
 t,Dr,D2r,X0=baseline_X(geom,R,nr,sign);ns=len(geom['s']);x0=pack_sym(X0[1:-1]);target_qnn=2*(geom['ric0']+3*geom['q0']+2*np.einsum('sij,sjk,skl->sil',geom['k0'],np.linalg.inv(geom['q0']),geom['k0']))
 def detail(x):
  X=X0.copy();X[1:-1]=unpack_sym(x,nr-2,ns);q=q_from_X(geom,X);qn,qnn=fm.normal_derivatives(q,Dr,D2r);qn[0]=2*sign*geom['k0'];qnn[0]=target_qnn;qn[-1]=2*q[-1];qnn[-1]=4*q[-1]
  return q,fm.full_residual(q,Dr,D2r,qn_override=qn,qnn_override=qnn),X
 def geometric_vector(res):
  arr=res['packed'][1:-1] if exclude_endpoints else res['packed']
  return arr.ravel()
 def fun(x):
  q,res,X=detail(x);F=geometric_vector(res)
  if reg>0:
   # Regularize perturbation curvature in the logarithmic matrix, excluding endpoints.
   dX=X-X0;curv=np.einsum('ab,bsij->asij',D2r,dX)[1:-1]
   F=np.concatenate([F,math.sqrt(reg)*curv.ravel()])
  return F
 q0,res0,_=detail(x0);ls=least_squares(fun,x0,jac_sparsity=None,max_nfev=max_nfev,method='trf',diff_step=2e-4,x_scale='jac',verbose=0,ftol=1e-7,xtol=1e-7,gtol=1e-7)
 q1,res1,X1=detail(ls.x)
 line=[]
 for a in [0,.1,.25,.5,.75,1]:
  q,re,X=detail(x0+a*(ls.x-x0));line.append({'alpha':a,'geometric_vector_norm':float(np.linalg.norm(geometric_vector(re))),**fm.summarize_half(R*t,re)})
 return {'side':'positive' if sign>0 else 'negative','unknown_count':len(x0),'regularization':reg,
         'baseline':fm.summarize_half(R*t,res0),'baseline_geometric_norm':float(np.linalg.norm(geometric_vector(res0))),
         'final':fm.summarize_half(R*t,res1),'final_geometric_norm':float(np.linalg.norm(geometric_vector(res1))),
         'solver':{'success':bool(ls.success),'status':int(ls.status),'message':ls.message,'nfev':int(ls.nfev),'cost_including_regularizer':float(ls.cost),'optimality':float(ls.optimality),'step_norm':float(np.linalg.norm(ls.x-x0))},'line':line}
def main():
 a=argparse.ArgumentParser();a.add_argument('--nr',type=int,default=13);a.add_argument('--ns',type=int,default=16);a.add_argument('--R',type=float,default=1.0);a.add_argument('--wind',type=int,default=2);a.add_argument('--S',type=float,default=1.);a.add_argument('--Qmax',type=float,default=.5);a.add_argument('--max-nfev',type=int,default=4);a.add_argument('--reg',type=float,default=1e-4);a.add_argument('--exclude-endpoints',action='store_true');a.add_argument('--output',default='workspace/data/step98_direct_spd_transition.json');z=a.parse_args();g=fm.center_geometry(z.ns,z.wind,z.S,z.Qmax);p=solve_side(g,z.R,z.nr,+1,z.max_nfev,z.reg,z.exclude_endpoints);n=solve_side(g,z.R,z.nr,-1,z.max_nfev,z.reg,z.exclude_endpoints);out={'model':'direct full SPD nodal transition','parameters':vars(z),'positive':p,'negative':n,'joint':{'baseline_sup':max(p['baseline']['operator_sup'],n['baseline']['operator_sup']),'final_sup':max(p['final']['operator_sup'],n['final']['operator_sup']),'baseline_norm':math.hypot(p['baseline_geometric_norm'],n['baseline_geometric_norm']),'final_norm':math.hypot(p['final_geometric_norm'],n['final_geometric_norm'])},'status':'Finite discretization only.'};path=Path(z.output);path=path if path.is_absolute() else SESSION/path;path.write_text(json.dumps(out,indent=2));print(json.dumps({'output':str(path),'positive':p,'negative':n,'joint':out['joint']},indent=2))
if __name__=='__main__':main()

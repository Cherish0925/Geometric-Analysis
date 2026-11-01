#!/usr/bin/env python3
"""Continue a validated local Koiso germ toward nonflat expanded entry data.

1. Integrate the exact T^2-invariant Einstein Cauchy equations from the Step-69
   scalar-minus-six center only to t*=0.15, where independent mode runs agree
   and Hamilton/momentum residuals are still small.
2. Fix metric and shape at t*.  On [t*,R], parameterize corrections that vanish
   with first derivative at t*, and minimize all five orthonormal components of
   Ric+3g by Gauss--Newton.
3. Continue with soft (not exact) interface costs for S-I and intrinsic Ricci.
   The exit anisotropy and its normal flux remain free for the Step-73 tail.

This is a restricted finite spectral test, not a well-posedness or existence
proof.  The Cauchy integration is used only as a local-germ generator.
"""
from __future__ import annotations
import importlib.util,json,math,sys,time
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import least_squares
import jax
jax.config.update('jax_enable_x64',True)
import jax.numpy as jnp
from jax import jit,jacfwd

MODE=sys.argv[1] if len(sys.argv)>1 else 'pilot'
if MODE=='pilot': KZ,NZ,NR,R_LIST,MAX0,MAX1=(5,32,29,[2.0,4.0,6.0],70,70)
elif MODE=='refine': KZ,NZ,NR,R_LIST,MAX0,MAX1=(7,48,41,[4.0,6.0,8.0],120,120)
else:raise ValueError(MODE)
TSTAR=.15; TWOPI=2*np.pi
parent=Path(__file__).resolve().parent
old=sys.argv[:];sys.argv=[sys.argv[0],'pilot']
spec=importlib.util.spec_from_file_location('s75base',parent/'step75_full_residual_core_search.py')
base=importlib.util.module_from_spec(spec);spec.loader.exec_module(base);sys.argv=old
z_np=TWOPI*np.arange(NZ)/NZ
Z_np,Z1_np,Z2_np=base.real_fourier_basis(z_np,KZ);NM=Z_np.shape[1]
raw=np.stack(base.yamabe_center(z_np));C0=np.stack([np.linalg.lstsq(Z_np,v,rcond=None)[0] for v in raw])

def project(v):return (np.linalg.lstsq(Z_np,v,rcond=None)[0]@Z_np.T)
def deriv(v,order=1):
 c=np.linalg.lstsq(Z_np,v,rcond=None)[0];return c@(Z1_np if order==1 else Z2_np).T

def ric3_np(L):
 Lz=np.stack([deriv(x) for x in L]);Lzz=np.stack([deriv(x,2) for x in L])
 return base.intrinsic_ric_np(L,Lz,Lzz)

def constraints(L,S):
 ric=ric3_np(L);H=S.sum(0);ham=ric.sum(0)-H*H+np.sum(S*S,axis=0)+6
 a,b,c=L;sa,sb,sc=S
 mom=np.exp(-a)*(-deriv(sb)-deriv(sc)+deriv(b)*(sa-sb)+deriv(c)*(sa-sc))
 return ham,mom

def make_germ():
 L0=C0@Z_np.T;S0=np.zeros_like(L0);y0=np.concatenate((L0.ravel(),S0.ravel()))
 n=NZ
 def rhs(t,y):
  L=np.stack([project(y[i*n:(i+1)*n]) for i in range(3)])
  S=np.stack([project(y[(i+3)*n:(i+4)*n]) for i in range(3)])
  ric=ric3_np(L);H=S.sum(0);acc=np.stack([project(ric[i]+3-H*S[i]) for i in range(3)])
  return np.concatenate((S.ravel(),acc.ravel()))
 sol=solve_ivp(rhs,(0,TSTAR),y0,method='DOP853',rtol=2e-10,atol=2e-12,max_step=.001)
 if not sol.success:raise RuntimeError(sol.message)
 y=sol.y[:,-1];L=np.stack([project(y[i*n:(i+1)*n]) for i in range(3)]);S=np.stack([project(y[(i+3)*n:(i+4)*n]) for i in range(3)])
 ham,mom=constraints(L,S)
 return L,S,{'nfev':int(sol.nfev),'steps':int(sol.t.size),'ham_sup':float(np.abs(ham).max()),'mom_sup':float(np.abs(mom).max()),
  'H_range':[float(S.sum(0).min()),float(S.sum(0).max())],'S_range':[float(S.min()),float(S.max())]}

LINNER,SINNER,GERM=make_germ()
CL=np.stack([np.linalg.lstsq(Z_np,v,rcond=None)[0] for v in LINNER]);CS=np.stack([np.linalg.lstsq(Z_np,v,rcond=None)[0] for v in SINNER])
Z=jnp.asarray(Z_np);Z1=jnp.asarray(Z1_np);Z2=jnp.asarray(Z2_np);CLj=jnp.asarray(CL);CSj=jnp.asarray(CS)
LOCAL=[.28,.42,.65,1.0];NG=8

def radial_basis(x,X):
 V=[];V1=[];V2=[];names=[]
 for ell in LOCAL:
  y=x/ell;e=np.exp(-y*y);V.append(y*y*e);V1.append(e*(2*y-2*y**3)/ell);V2.append(e*(2-10*y*y+4*y**4)/(ell*ell));names.append(f'loc{ell}')
 s=x/X
 for j in range(NG):
  # s^2 cos(j*pi*s), normalized jointly to avoid huge coefficients.
  k=j*np.pi;v=s*s*np.cos(k*s)
  v1=(2*s*np.cos(k*s)-k*s*s*np.sin(k*s))/X
  v2=(2*np.cos(k*s)-4*k*s*np.sin(k*s)-k*k*s*s*np.cos(k*s))/(X*X)
  scale=max(np.sqrt(np.mean(v*v)+np.mean((X*v1)**2)+np.mean((X*X*v2)**2)),1e-12)
  V.append(v/scale);V1.append(v1/scale);V2.append(v2/scale);names.append(f'glob{j}')
 return np.array(V).T,np.array(V1).T,np.array(V2).T,names

def intrinsic_jax(L,Lz,Lzz):
 a,b,c=L;az,bz,cz=Lz;_,bzz,czz=Lzz;em=jnp.exp(-2*a)
 return jnp.stack((-em*((bzz-az*bz)+bz*bz+(czz-az*cz)+cz*cz),-em*((bzz-az*bz)+bz*bz+bz*cz),-em*((czz-az*cz)+cz*cz+bz*cz)))

def make_problem(R,wi):
 X=R-TSTAR
 # Concentrate points near inner germ, but retain full physical interval.
 inner=np.linspace(0,min(1.2,X),16,endpoint=False);outer=np.linspace(min(1.2,X),X,NR-len(inner));x_np=np.unique(np.r_[inner,outer]);r_np=TSTAR+x_np
 B_np,B1_np,B2_np,names=radial_basis(x_np,X);J=B_np.shape[1]
 B=jnp.asarray(B_np);B1=jnp.asarray(B1_np);B2=jnp.asarray(B2_np);x=jnp.asarray(x_np)
 wr=np.empty(len(x_np));wr[0]=(x_np[1]-x_np[0])/2;wr[-1]=(x_np[-1]-x_np[-2])/2;wr[1:-1]=(x_np[2:]-x_np[:-2])/2;wr/=X;sqw=jnp.sqrt(jnp.asarray(wr)[:,None]/NZ)
 def fields(v):
  coef=v.reshape(3,J,NM);l0=jnp.einsum('im,zm->iz',CLj,Z);s0=jnp.einsum('im,zm->iz',CSj,Z)
  l0z=jnp.einsum('im,zm->iz',CLj,Z1);l0zz=jnp.einsum('im,zm->iz',CLj,Z2);s0z=jnp.einsum('im,zm->iz',CSj,Z1);s0zz=jnp.einsum('im,zm->iz',CSj,Z2)
  F=jnp.einsum('rj,ijm,zm->irz',B,coef,Z);Fr=jnp.einsum('rj,ijm,zm->irz',B1,coef,Z);Frr=jnp.einsum('rj,ijm,zm->irz',B2,coef,Z);Fz=jnp.einsum('rj,ijm,zm->irz',B,coef,Z1);Fzz=jnp.einsum('rj,ijm,zm->irz',B,coef,Z2);Frz=jnp.einsum('rj,ijm,zm->irz',B1,coef,Z1)
  L=l0[:,None,:]+x[None,:,None]*s0[:,None,:]+F;Lr=s0[:,None,:]+Fr;Lrr=Frr
  Lz=l0z[:,None,:]+x[None,:,None]*s0z[:,None,:]+Fz;Lzz=l0zz[:,None,:]+x[None,:,None]*s0zz[:,None,:]+Fzz;Lrz=s0z[:,None,:]+Frz
  return L,Lr,Lrr,Lz,Lzz,Lrz
 def comp(v):
  L,Lr,Lrr,Lz,Lzz,Lrz=fields(v);a,b,c=L;ar,br,cr=Lr;arr,brr,crr=Lrr;az,bz,cz=Lz;_,bzz,czz=Lzz;_,brz,crz=Lrz;em=jnp.exp(-2*a)
  E0=3-ar*ar-arr-br*br-brr-cr*cr-crr;E1=jnp.exp(-a)*(ar*bz+ar*cz-br*bz-cr*cz-brz-crz);E2=3-ar*ar-ar*br-ar*cr-arr+em*(az*bz+az*cz-bz*bz-bzz-cz*cz-czz);E3=3-ar*br-br*br-br*cr-brr+em*(az*bz-bz*bz-bz*cz-bzz);E4=3-ar*cr-br*cr-cr*cr-crr+em*(az*cz-bz*cz-cz*cz-czz)
  return jnp.stack((E0,E1,E2,E3,E4)),(L,Lr,Lrr,Lz,Lzz,Lrz)
 def res(v):
  E,f=comp(v);out=[(jnp.stack((E[0],jnp.sqrt(2.)*E[1],E[2],E[3],E[4]))*sqw[None]).reshape(-1)]
  if wi>0:
   L,Lr,Lrr,Lz,Lzz,Lrz=f;ric=intrinsic_jax(L[:,-1],Lz[:,-1],Lzz[:,-1]);w=math.sqrt(wi/(3*NZ));out.extend([w*(Lr[:,-1]-1).reshape(-1),.2*w*ric.reshape(-1)])
  return jnp.concatenate(out)
 return {'R':R,'X':X,'r':r_np,'J':J,'fields':fields,'comp':comp,'res':res}

def diag(v,pr,label):
 E=np.asarray(pr['comp'](jnp.asarray(v))[0]);L,Lr,Lrr,Lz,Lzz,Lrz=[np.asarray(x) for x in pr['comp'](jnp.asarray(v))[1]];r=pr['r'];tr=E[0]+E[2];ds=np.sqrt((E[0]-E[2])**2+4*E[1]**2);op=np.maximum.reduce((abs((tr-ds)/2),abs((tr+ds)/2),abs(E[3]),abs(E[4])));ric=base.intrinsic_ric_np(L[:,-1],Lz[:,-1],Lzz[:,-1]);d=L[1]-L[2];dr=Lr[1]-Lr[2]
 return {'label':label,'operator_sup':float(op.max()),'operator_rms':float(np.sqrt(np.mean(op**2))),'argmax_r':float(r[np.unravel_index(np.argmax(op),op.shape)[0]]),'component_sup':{k:float(abs(E[i]).max()) for i,k in enumerate(['E_rr','E_rz','E_zz','E_x','E_y'])},'inner':{'value_error':float(abs(L[:,0]-LINNER).max()),'shape_error':float(abs(Lr[:,0]-SINNER).max()),'component_sup':{k:float(abs(E[i,0]).max()) for i,k in enumerate(['E_rr','E_rz','E_zz','E_x','E_y'])}},'exit':{'S_I_sup':float(abs(Lr[:,-1]-1).max()),'S_I_rms':float(np.sqrt(np.mean((Lr[:,-1]-1)**2))),'d_r_sup':float(abs(dr[-1]).max()),'intrinsic_Ric_sup':float(abs(ric).max()),'anisotropy_osc':float(np.ptp(d[-1])),'L_range':[float(L[:,-1].min()),float(L[:,-1].max())]},'coef_norm':float(np.linalg.norm(v)),'residual_l2':float(np.linalg.norm(np.asarray(pr['res'](jnp.asarray(v)))))}
def solve(pr,x0,n):
 rf=jit(pr['res']);jf=jit(jacfwd(pr['res']));fun=lambda x:np.asarray(rf(jnp.asarray(x)),float);jac=lambda x:np.asarray(jf(jnp.asarray(x)),float)
 return least_squares(fun,x0,jac=jac,method='trf',tr_solver='lsmr',x_scale='jac',bounds=(-20,20),max_nfev=n,ftol=5e-11,xtol=5e-11,gtol=5e-11)
def main():
 print('germ',GERM,'KZ',KZ,'variables/radial',3*(len(LOCAL)+NG)*NM)
 out={'scope':'full five-component continuation from numerical local Koiso germ at t=.15; finite spectral evidence only','mode':MODE,'germ':GERM,'Kz':KZ,'runs':[]};cdir=Path(__file__).resolve().parents[1]/'data'/f'step75_germ_entry_coeff_{MODE}';cdir.mkdir(parents=True,exist_ok=True)
 for R in R_LIST:
  pr=make_problem(R,0);x=np.zeros(3*pr['J']*NM);d0=diag(x,pr,'linear_extension');t=time.time();a=solve(pr,x,MAX0);d1=diag(a.x,pr,'residual_only');pr2=make_problem(R,1);b=solve(pr2,a.x,MAX1);d2=diag(b.x,pr2,'soft_entry');print('R',R,'op',d0['operator_sup'],d1['operator_sup'],d2['operator_sup'],'exit',d2['exit'],'wall',time.time()-t,flush=True);out['runs'].append({'R':R,'initial':d0,'residual_only':d1,'soft_entry':d2,'solvers':[{'nfev':int(a.nfev),'cost':float(a.cost),'message':str(a.message)},{'nfev':int(b.nfev),'cost':float(b.cost),'message':str(b.message)}]});np.save(cdir/f'R{R:g}.npy',b.x)
 path=Path(__file__).resolve().parents[1]/'data'/f'step75_germ_to_entry_{MODE}.json';path.write_text(json.dumps(out,indent=2),encoding='utf-8');print('wrote',path)
if __name__=='__main__':main()

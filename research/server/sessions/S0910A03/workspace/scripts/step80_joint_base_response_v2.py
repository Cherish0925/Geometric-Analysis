#!/usr/bin/env python3
"""Inner-layer high-jet comparison for the Step 80 reflected connector.

Reuses the Step 80 OT Gaussian residuals but replaces the ad-hoc second-jet
carrier near r=0 by the exact even Taylor germ through r^4,
  L=L0 + p r^2/2 + w r^4/24,
where p=Ric(q0)+3 and w=D Ric[2p^flat]-6p in (a,b,c) variables.
The polynomial is cut off only after an inner radius, and all free corrections
vanish through r^4 (start at r^6).  This tests whether the persistent r~0.2
peak in v1 was caused by a wrong fourth jet.
"""
from __future__ import annotations
import importlib.util,json,sys,time,math
from pathlib import Path
import numpy as np
from scipy.optimize import least_squares
import jax
jax.config.update('jax_enable_x64',True)
import jax.numpy as jnp
from jax import jit,jacfwd

MODE=sys.argv[1] if len(sys.argv)>1 else 'pilot'
root=Path(__file__).resolve().parents[1]
old=sys.argv[:];sys.argv=[sys.argv[0],'pilot']
spec=importlib.util.spec_from_file_location('s80',root/'scripts'/'step80_joint_base_response.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);sys.argv=old
R_LIST=[2.,4.,6.]; RINNER=.75; J=10; MAXN=120
# Center in (a,b,c).
L0=np.stack((m.center[0],(m.center[1]+m.center[2])/2,(m.center[1]-m.center[2])/2))
def derivs(L):
 c=np.stack([np.linalg.lstsq(m.Z_np,q,rcond=None)[0] for q in L]);return c@m.Z1_np.T,c@m.Z2_np.T
def ric_np(L):
 Lz,Lzz=derivs(L);return m.intrinsic_ric_np(L[0],L[1]+L[2],L[1]-L[2],Lz[0],Lz[1]+Lz[2],Lz[1]-Lz[2],Lzz[0],Lzz[1]+Lzz[2],Lzz[1]-Lzz[2])
pabc=ric_np(L0)+3
# Directional derivative in log fields: q variation is 2p q automatically.
eps=3e-5
wabc=(ric_np(L0+eps*pabc)-ric_np(L0-eps*pabc))/(2*eps)-6*pabc
# Transform abc -> a,sigma=b+c,v=b-c.
def trans(Q):return np.stack((Q[0],Q[1]+Q[2],Q[1]-Q[2]))
L0t=trans(L0); pt=trans(pabc); wt=trans(wabc)
C0=np.stack([np.linalg.lstsq(m.Z_np,q,rcond=None)[0] for q in L0t])
PC=np.stack([np.linalg.lstsq(m.Z_np,q,rcond=None)[0] for q in pt])
WC=np.stack([np.linalg.lstsq(m.Z_np,q,rcond=None)[0] for q in wt])
Z=jnp.asarray(m.Z_np);Z1=jnp.asarray(m.Z1_np);Z2=jnp.asarray(m.Z2_np)
C0j=jnp.asarray(C0);PCj=jnp.asarray(PC);WCj=jnp.asarray(WC)

def grid(R):
 # Fixed fine inner resolution independent of R.
 inn=np.linspace(0,RINNER,25,endpoint=False);out=np.linspace(RINNER,R,17);return np.unique(np.r_[inn,out])
def cutoff_arrays(r,R):
 # eta=1 through .5, quintic smoothstep to 0 by 1.25; numerical derivatives
 x=(r-.5)/.75;eta=np.where(r<=.5,1.,np.where(r>=1.25,0.,1-(10*x**3-15*x**4+6*x**5)))
 # analytic derivatives in transition
 e1=np.zeros_like(r);e2=np.zeros_like(r);mask=(r>.5)&(r<1.25);xx=x[mask]
 e1[mask]=-(30*xx**2-60*xx**3+30*xx**4)/.75
 e2[mask]=-(60*xx-180*xx**2+120*xx**3)/(.75**2)
 return eta,e1,e2
def basis(r,R):
 s=r/R;V=[];V1=[];V2=[]
 # global even powers start at r^6 and permit broad response.
 for j in range(J):
  k=j*math.pi; # s^6 cos(k s)
  v=s**6*np.cos(k*s)
  v1=(6*s**5*np.cos(k*s)-k*s**6*np.sin(k*s))/R
  v2=(30*s**4*np.cos(k*s)-12*k*s**5*np.sin(k*s)-k*k*s**6*np.cos(k*s))/(R*R)
  sc=max(np.sqrt(np.mean(v*v)+np.mean((R*v1)**2)+np.mean((R*R*v2)**2)),1e-12)
  V.append(v/sc);V1.append(v1/sc);V2.append(v2/sc)
 # fixed physical local modes r^6 exp(-(r/ell)^2)
 for ell in [.25,.4,.65,1.0]:
  x=r/ell;e=np.exp(-x*x);v=x**6*e
  v1=e*(6*x**5-2*x**7)/ell
  v2=e*(30*x**4-26*x**6+4*x**8)/(ell*ell)
  V.append(v);V1.append(v1);V2.append(v2)
 return np.array(V).T,np.array(V1).T,np.array(V2).T

def make(R,variant,entry):
 rnp=grid(R);Bnp,B1np,B2np=basis(rnp,R);eta,e1,e2=cutoff_arrays(rnp,R);nr=len(rnp);nm=m.NM;nb=Bnp.shape[1]
 r=jnp.asarray(rnp);B=jnp.asarray(Bnp);B1=jnp.asarray(B1np);B2=jnp.asarray(B2np);et=jnp.asarray(eta);et1=jnp.asarray(e1);et2=jnp.asarray(e2)
 comps=(0,1,2) if variant=='joint' else (2,);nc=len(comps)
 wr=np.empty(nr);wr[0]=(rnp[1]-rnp[0])/2;wr[-1]=(rnp[-1]-rnp[-2])/2;wr[1:-1]=(rnp[2:]-rnp[:-2])/2
 # do NOT divide by R: fixed inner layer keeps fixed objective weight.
 sq=jnp.sqrt(jnp.asarray(wr)[:,None]/m.NZ)
 def field(v):
  co=v.reshape(nc,nb,nm)
  l0=jnp.einsum('im,zm->iz',C0j,Z);l0z=jnp.einsum('im,zm->iz',C0j,Z1);l0zz=jnp.einsum('im,zm->iz',C0j,Z2)
  pp=jnp.einsum('im,zm->iz',PCj,Z);ppz=jnp.einsum('im,zm->iz',PCj,Z1);ppzz=jnp.einsum('im,zm->iz',PCj,Z2)
  ww=jnp.einsum('im,zm->iz',WCj,Z);wwz=jnp.einsum('im,zm->iz',WCj,Z1);wwzz=jnp.einsum('im,zm->iz',WCj,Z2)
  T=.5*r*r;Q=r**4/24;T1=r;Q1=r**3/6;T2=jnp.ones_like(r);Q2=r*r/2
  raw=l0[:,None,:]+T[None,:,None]*pp[:,None,:]+Q[None,:,None]*ww[:,None,:]
  rawr=T1[None,:,None]*pp[:,None,:]+Q1[None,:,None]*ww[:,None,:]
  rawrr=T2[None,:,None]*pp[:,None,:]+Q2[None,:,None]*ww[:,None,:]
  rawz=l0z[:,None,:]+T[None,:,None]*ppz[:,None,:]+Q[None,:,None]*wwz[:,None,:]
  rawzz=l0zz[:,None,:]+T[None,:,None]*ppzz[:,None,:]+Q[None,:,None]*wwzz[:,None,:]
  rawrz=T1[None,:,None]*ppz[:,None,:]+Q1[None,:,None]*wwz[:,None,:]
  # Blend exact germ to a common cosh expansion after the inner layer.
  A=jnp.logaddexp(r,-r)-math.log(2);Ar=jnp.tanh(r);Arr=1/jnp.cosh(r)**2
  outer=l0[:,None,:]+jnp.stack((A,2*A,jnp.zeros_like(A)))[:,:,None]
  outerr=jnp.stack((Ar,2*Ar,jnp.zeros_like(Ar)))[:,:,None]
  outerrr=jnp.stack((Arr,2*Arr,jnp.zeros_like(Arr)))[:,:,None]
  outerz=jnp.broadcast_to(l0z[:,None,:],rawz.shape);outerzz=jnp.broadcast_to(l0zz[:,None,:],rawzz.shape);outerrz=jnp.zeros_like(rawrz)
  L=outer+et[None,:,None]*(raw-outer)
  Lr=outerr+et1[None,:,None]*(raw-outer)+et[None,:,None]*(rawr-outerr)
  Lrr=outerrr+et2[None,:,None]*(raw-outer)+2*et1[None,:,None]*(rawr-outerr)+et[None,:,None]*(rawrr-outerrr)
  Lz=outerz+et[None,:,None]*(rawz-outerz);Lzz=outerzz+et[None,:,None]*(rawzz-outerzz);Lrz=outerrz+et1[None,:,None]*(rawz-outerz)+et[None,:,None]*(rawrz-outerrz)
  for k,c in enumerate(comps):
   F=jnp.einsum('rj,jm,zm->rz',B,co[k],Z);Fr=jnp.einsum('rj,jm,zm->rz',B1,co[k],Z);Frr=jnp.einsum('rj,jm,zm->rz',B2,co[k],Z)
   Fz=jnp.einsum('rj,jm,zm->rz',B,co[k],Z1);Fzz=jnp.einsum('rj,jm,zm->rz',B,co[k],Z2);Frz=jnp.einsum('rj,jm,zm->rz',B1,co[k],Z1)
   L=L.at[c].add(F);Lr=Lr.at[c].add(Fr);Lrr=Lrr.at[c].add(Frr);Lz=Lz.at[c].add(Fz);Lzz=Lzz.at[c].add(Fzz);Lrz=Lrz.at[c].add(Frz)
  return L,Lr,Lrr,Lz,Lzz,Lrz
 def comp(v):
  L,Lr,Lrr,Lz,Lzz,Lrz=field(v);a,s,vv=L;ar,sr,vr=Lr;arr,srr,vrr=Lrr;az,sz,vz=Lz;_,szz,vzz=Lzz;_,srz,vrz=Lrz
  b=(s+vv)/2;c=(s-vv)/2;br=(sr+vr)/2;cr=(sr-vr)/2;brr=(srr+vrr)/2;crr=(srr-vrr)/2;bz=(sz+vz)/2;cz=(sz-vz)/2;bzz=(szz+vzz)/2;czz=(szz-vzz)/2;brz=(srz+vrz)/2;crz=(srz-vrz)/2;em=jnp.exp(-2*a)
  E0=3-ar*ar-arr-br*br-brr-cr*cr-crr;E1=jnp.exp(-a)*(ar*bz+ar*cz-br*bz-cr*cz-brz-crz);E2=3-ar*ar-ar*br-ar*cr-arr+em*(az*bz+az*cz-bz*bz-bzz-cz*cz-czz);E3=3-ar*br-br*br-br*cr-brr+em*(az*bz-bz*bz-bz*cz-bzz);E4=3-ar*cr-br*cr-cr*cr-crr+em*(az*cz-bz*cz-cz*cz-czz)
  return jnp.stack((E0,E1,E2,E3,E4)),(L,Lr,Lrr,Lz,Lzz,Lrz)
 def res(v):
  E,f=comp(v);out=[(jnp.stack((E[0],jnp.sqrt(2.)*E[1],E[2],E[3],E[4]))*sq[None]).reshape(-1)]
  if entry:
   L,Lr,Lrr,Lz,Lzz,Lrz=f;S=jnp.stack((Lr[0,-1],(Lr[1,-1]+Lr[2,-1])/2,(Lr[1,-1]-Lr[2,-1])/2));out.append(.06*(S-1).reshape(-1))
  out.append(1e-5*v);return jnp.concatenate(out)
 return {'r':rnp,'nb':nb,'nc':nc,'field':field,'comp':comp,'res':res}
def diag(x,R,p,variant):
 E=np.asarray(p['comp'](jnp.asarray(x))[0]);L,Lr,Lrr,Lz,Lzz,Lrz=[np.asarray(q) for q in p['comp'](jnp.asarray(x))[1]];op=m.exact_op(E);ii=np.unravel_index(np.argmax(op),op.shape);S=np.stack((Lr[0],(Lr[1]+Lr[2])/2,(Lr[1]-Lr[2])/2))
 return {'variant':variant,'operator_sup':float(op.max()),'operator_rms':float(np.sqrt(np.mean(op**2))),'argmax_r':float(p['r'][ii[0]]),'component_sup':[float(np.abs(E[i]).max()) for i in range(5)],'exit_S_I_sup':float(np.abs(S[:,-1]-1).max()),'center_component_sup':[float(np.abs(E[i,0]).max()) for i in range(5)]}
def solve(p,x):
 rf=jit(p['res']);jf=jit(jacfwd(p['res']));return least_squares(lambda y:np.asarray(rf(jnp.asarray(y)),float),x,jac=lambda y:np.asarray(jf(jnp.asarray(y)),float),method='trf',tr_solver='lsmr',x_scale='jac',bounds=(-20,20),max_nfev=MAXN,ftol=2e-10,xtol=2e-10,gtol=2e-10)
def main():
 out={'scope':'inner-layer high-jet finite-mode comparison; exact only relative to projected center','jet':{'p_ranges':[[float(q.min()),float(q.max())] for q in pt],'w_ranges':[[float(q.min()),float(q.max())] for q in wt],'normal_w_recurrence_sup':float(np.abs(wabc.sum(0)+2*np.sum(pabc*pabc,0)).max())},'runs':[]};cd=root/'data'/'step80_v2_coeff';cd.mkdir(exist_ok=True)
 for R in R_LIST:
  row={'R':R,'variants':{}}
  for v in ['shape_only','joint']:
   p=make(R,v,True);x=np.zeros(p['nc']*p['nb']*m.NM);d0=diag(x,R,p,v);t=time.time();s=solve(p,x);d=diag(s.x,R,p,v);row['variants'][v]={'initial':d0,'final':d,'solver':{'nfev':int(s.nfev),'optimality':float(s.optimality),'message':str(s.message)},'wall':time.time()-t};np.save(cd/f'R{R:g}_{v}.npy',s.x);print(R,v,d0['operator_sup'],d['operator_sup'],d['argmax_r'],d['exit_S_I_sup'],flush=True)
  out['runs'].append(row)
 path=root/'data'/'step80_joint_base_response_v2.json';path.write_text(json.dumps(out,indent=2));print('wrote',path)
if __name__=='__main__':main()

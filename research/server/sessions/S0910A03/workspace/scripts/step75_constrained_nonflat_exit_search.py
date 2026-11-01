#!/usr/bin/env python3
"""Constraint-compatible full-Ricci search with a fixed nonflat expanded exit.

This repairs the first Step-75 pilot.  On [0,R] x T^3 use
 g=dr^2+e^(2a)dz^2+e^(2b)dx^2+e^(2c)dy^2.
The Step-69 scalar-minus-six center q0 and all reflection jets are fixed.  The
second normal jet is fixed to the Koiso value L_i,rr(0)=Ric_i(q0)+3.  Free
corrections are even, vanish through second order at the center, and vanish
through second order at the exit.  The outer data are deliberately nonflat:
 cosh(R)^2 q0 with S=tanh(R) I.
Thus the Step-73 adiabatic tail, rather than an obstructed exact flat boundary,
is the intended continuation.

Every optimization evaluates all five orthonormal components of Ric+3g.  This
is a finite spectral experiment in the diagonal orthogonally-transitive class,
not a nonlinear existence theorem.
"""
from __future__ import annotations
import importlib.util
import json
import math
import sys
import time
from pathlib import Path

import numpy as np
from scipy.linalg import null_space
from scipy.optimize import minimize
from numpy.polynomial.chebyshev import chebval, chebder

import jax
jax.config.update('jax_enable_x64', True)
import jax.numpy as jnp
from jax import jit, value_and_grad

MODE=sys.argv[1] if len(sys.argv)>1 else 'pilot'
if MODE not in ('pilot','refine'): raise ValueError(MODE)
# Load the validated center/grid definitions without running its main().
parent=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('step75base',parent/'step75_full_residual_core_search.py')
base=importlib.util.module_from_spec(spec); spec.loader.exec_module(base)

if MODE=='pilot':
    R_LIST=[2.0,4.0,6.0]; RAWJ=17; ADAM=550; LBFGS=500
else:
    R_LIST=[4.0,6.0,8.0]; RAWJ=23; ADAM=1200; LBFGS=900
P=12.0
WHIGH=1e-9

s_np=base.s_np; z_np=base.z_np
Z_np,Z1_np,Z2_np=base.Z_np,base.Z1_np,base.Z2_np
center=base.center; center_z=base.center_z; center_zz=base.center_zz
center_ric=base.center_ric
NM=base.NM; NR=base.NR; NZ=base.NZ
# Galerkin projection of the required extra acceleration Ric(q0)+2I.
gcoef=np.stack([np.linalg.lstsq(Z_np,center_ric[i]+2.0,rcond=None)[0] for i in range(3)])
gval=gcoef@Z_np.T; gz=gcoef@Z1_np.T; gzz=gcoef@Z2_np.T
center_tangent_mismatch=center_ric-(gval-2.0)


def radial_null_basis(R:float):
    """Even Chebyshev basis satisfying F(0)=F''(0)=F(R)=F'(R)=F''(R)=0."""
    degs=[2*j for j in range(RAWJ)]
    C=np.zeros((5,RAWJ))
    for jj,d in enumerate(degs):
        c=np.zeros(d+1); c[d]=1.0
        c1=chebder(c,1); c2=chebder(c,2)
        C[0,jj]=chebval(0.0,c)
        C[1,jj]=chebval(0.0,c2)
        C[2,jj]=chebval(1.0,c)
        C[3,jj]=chebval(1.0,c1)
        C[4,jj]=chebval(1.0,c2)
    C=C/np.linalg.norm(C,axis=1)[:,None]
    N=null_space(C,rcond=1e-13)  # RAWJ x Jfree
    x=s_np
    V=np.zeros((NR,RAWJ)); V1=np.zeros_like(V); V2=np.zeros_like(V)
    for jj,d in enumerate(degs):
        c=np.zeros(d+1); c[d]=1.0
        V[:,jj]=chebval(x,c)
        V1[:,jj]=chebval(x,chebder(c,1))/R
        V2[:,jj]=chebval(x,chebder(c,2))/(R*R)
    E=V@N
    # Orthonormalize discrete values; same transform applies to derivatives.
    Q,T=np.linalg.qr(E)
    X=N@np.linalg.inv(T)
    return V@X,V1@X,V2@X,X,C


def rho_arrays(R,ell):
    """Even Koiso second-jet carrier, with value/first/second jet zero at exit."""
    r=R*s_np; ss=s_np
    x=(r/ell)**4
    e=np.exp(-x)
    p=.5*r*r*e
    pr=r*e*(1.0-2.0*x)
    prr=e*(1.0-14.0*x+8.0*x*x)
    w=(1.0-ss*ss)**3
    # derivatives with respect to physical r
    wr=-6.0*ss*(1.0-ss*ss)**2/R
    wrr=(-6.0+30.0*ss*ss-24.0*ss**4)/(R*R)
    return p*w,pr*w+p*wr,prr*w+2*pr*wr+p*wrr


def make_problem(R,ell):
    BV,BVr,BVrr,_,C=radial_null_basis(R)
    J=BV.shape[1]
    rho,rhor,rhorr=rho_arrays(R,ell)
    # Boundary-condition unit checks.
    bcerr=max(np.max(np.abs(BV[0])),np.max(np.abs(BVrr[0])),
              np.max(np.abs(BV[-1])),np.max(np.abs(BVr[-1])),np.max(np.abs(BVrr[-1])),
              abs(rho[0]),abs(rhor[0]),abs(rhorr[0]-1.0),abs(rho[-1]),abs(rhor[-1]),abs(rhorr[-1]))
    B=jnp.asarray(BV); Br=jnp.asarray(BVr); Brr=jnp.asarray(BVrr)
    rhoj=jnp.asarray(rho); rhorj=jnp.asarray(rhor); rhorrj=jnp.asarray(rhorr)
    Z=jnp.asarray(Z_np); Z1=jnp.asarray(Z1_np); Z2=jnp.asarray(Z2_np)
    C0=jnp.asarray(base.center_coef); G=jnp.asarray(gcoef)
    rj=jnp.asarray(R*s_np)

    def fields(v):
        coef=v.reshape(3,J,NM)
        A=base.logcosh(rj); Ar=jnp.tanh(rj); Arr=1/jnp.cosh(rj)**2
        l0=jnp.einsum('im,zm->iz',C0,Z); l0z=jnp.einsum('im,zm->iz',C0,Z1); l0zz=jnp.einsum('im,zm->iz',C0,Z2)
        gv=jnp.einsum('im,zm->iz',G,Z); gvz=jnp.einsum('im,zm->iz',G,Z1); gvzz=jnp.einsum('im,zm->iz',G,Z2)
        F=jnp.einsum('rj,ijm,zm->irz',B,coef,Z)
        Fr=jnp.einsum('rj,ijm,zm->irz',Br,coef,Z)
        Frr=jnp.einsum('rj,ijm,zm->irz',Brr,coef,Z)
        Fz=jnp.einsum('rj,ijm,zm->irz',B,coef,Z1)
        Fzz=jnp.einsum('rj,ijm,zm->irz',B,coef,Z2)
        Frz=jnp.einsum('rj,ijm,zm->irz',Br,coef,Z1)
        L=l0[:,None,:]+A[None,:,None]+rhoj[None,:,None]*gv[:,None,:]+F
        Lr=Ar[None,:,None]+rhorj[None,:,None]*gv[:,None,:]+Fr
        Lrr=Arr[None,:,None]+rhorrj[None,:,None]*gv[:,None,:]+Frr
        Lz=l0z[:,None,:]+rhoj[None,:,None]*gvz[:,None,:]+Fz
        Lzz=l0zz[:,None,:]+rhoj[None,:,None]*gvzz[:,None,:]+Fzz
        Lrz=rhorj[None,:,None]*gvz[:,None,:]+Frz
        return L,Lr,Lrr,Lz,Lzz,Lrz

    def residual(v):
        L,Lr,Lrr,Lz,Lzz,Lrz=fields(v)
        a,b,c=L; ar,br,cr=Lr; arr,brr,crr=Lrr
        az,bz,cz=Lz; _,bzz,czz=Lzz; _,brz,crz=Lrz
        em2a=jnp.exp(-2*a)
        E00=3-ar*ar-arr-br*br-brr-cr*cr-crr
        E0z=jnp.exp(-a)*(ar*bz+ar*cz-br*bz-cr*cz-brz-crz)
        Ezz=3-ar*ar-ar*br-ar*cr-arr+em2a*(az*bz+az*cz-bz*bz-bzz-cz*cz-czz)
        Ex=3-ar*br-br*br-br*cr-brr+em2a*(az*bz-bz*bz-bz*cz-bzz)
        Ey=3-ar*cr-br*cr-cr*cr-crr+em2a*(az*cz-bz*cz-cz*cz-czz)
        return jnp.stack((E00,E0z,Ezz,Ex,Ey)),(L,Lr,Lrr,Lz,Lzz,Lrz)

    def objective(v):
        E,_=residual(v)
        sq=E[0]**2+2*E[1]**2+E[2]**2+E[3]**2+E[4]**2
        lp=jnp.mean((sq+1e-24)**(P/2))**(1/P)
        coef=v.reshape(3,J,NM)
        shell=jnp.zeros(NM).at[max(0,NM-4):].set(1.0)
        return lp+WHIGH*jnp.sum(coef**2*shell[None,None,:])
    return J,bcerr,fields,residual,objective


def diagnostics(v,R,ell,problem):
    J,bcerr,fields,residual,obj=problem
    E_j,fld=residual(jnp.asarray(v)); E=np.asarray(E_j)
    L,Lr,Lrr,Lz,Lzz,Lrz=[np.asarray(x) for x in fld]
    tr=E[0]+E[2]; rad=np.sqrt((E[0]-E[2])**2+4*E[1]**2)
    lm=.5*(tr-rad); lp=.5*(tr+rad)
    op=np.maximum.reduce((np.abs(lm),np.abs(lp),np.abs(E[3]),np.abs(E[4])))
    H=np.sum(Lr,axis=0); shear=np.sum((Lr-1)**2,axis=0)
    ident=np.sum(Lrr,axis=0)+np.sum(Lr**2,axis=0)-3+E[0]
    ric_exit=base.intrinsic_ric_np(L[:,-1,:],Lz[:,-1,:],Lzz[:,-1,:])
    q0_d=L[1,0]-L[2,0]; qR_d=L[1,-1]-L[2,-1]
    return {
      'R_physical':R,'ell':ell,'free_radial_dim':J,'boundary_basis_error':float(bcerr),
      'objective':float(obj(jnp.asarray(v))),
      'full_residual':{'operator_sup':float(op.max()),'operator_rms':float(np.sqrt(np.mean(op**2))),
        'component_sup':{k:float(np.abs(E[i]).max()) for i,k in enumerate(['E_rr','E_rz_orth','E_zz','E_x','E_y'])},
        'argmax_r':float(R*s_np[np.unravel_index(np.argmax(op),op.shape)[0]])},
      'center':{'shape_sup':float(np.abs(Lr[:,0]).max()),
        'tangent_mismatch_sup':float(np.abs(center_tangent_mismatch).max()),
        'E_component_sup':{k:float(np.abs(E[i,0]).max()) for i,k in enumerate(['E_rr','E_rz_orth','E_zz','E_x','E_y'])}},
      'exit':{'S_minus_tanhR_I_sup':float(np.abs(Lr[:,-1]-np.tanh(R)).max()),
        'S_minus_I_sup':float(np.abs(Lr[:,-1]-1).max()),
        'intrinsic_Ric_sup':float(np.abs(ric_exit).max()),
        'scaled_intrinsic_Ric_sup':float(np.abs(ric_exit).max()/np.cosh(R)**2),
        'anisotropy_oscillation':float(np.ptp(qR_d)),
        'anisotropy_change_sup':float(np.abs(qR_d-q0_d).max())},
      'normal_identity_pointwise_sup':float(np.abs(ident).max()),
      'field_range':[float(L.min()),float(L.max())],
      'coefficient_norm':float(np.linalg.norm(v)),
    }


def run_one(R):
    # Scan the forced second-jet carrier before optimizing free modes.
    ell_candidates=[x for x in (0.35,0.5,0.7,1.0,1.4,2.0) if x<0.9*R]
    scan=[]; best=None
    for ell in ell_candidates:
        pr=make_problem(R,ell); J=pr[0]; v=np.zeros(3*J*NM)
        d=diagnostics(v,R,ell,pr); scan.append(d)
        if best is None or d['objective']<best[0]: best=(d['objective'],ell,pr,v)
    _,ell,pr,v=best; J=pr[0]
    print(f"R={R:g} carrier scan:",[(d['ell'],round(d['full_residual']['operator_sup'],4),round(d['objective'],4)) for d in scan],flush=True)
    obj=pr[4]; vg=jit(value_and_grad(obj))
    def fg(x):
        val,gr=vg(jnp.asarray(x)); return float(val),np.asarray(gr)
    initial=diagnostics(v,R,ell,pr)
    # L-BFGS first is stable from zero; Adam only if it improves the incumbent.
    t0=time.time()
    res=minimize(fg,v,jac=True,method='L-BFGS-B',bounds=[(-12,12)]*v.size,
      options={'maxiter':LBFGS,'maxls':40,'ftol':1e-13,'gtol':1e-9,'maxcor':25})
    incumbent=np.asarray(res.x); incval=float(res.fun)
    # Short Adam escape, always retaining the best point including L-BFGS and zero.
    x=incumbent.copy(); m=np.zeros_like(x); q=np.zeros_like(x); bestx=(incval,x.copy())
    for it in range(1,ADAM+1):
        val,gr=fg(x)
        if val<bestx[0]: bestx=(val,x.copy())
        m=.9*m+.1*gr; q=.999*q+.001*gr*gr
        lr=2e-4*(.5+.5*math.cos(math.pi*it/ADAM))+2e-5
        x=np.clip(x-lr*(m/(1-.9**it))/(np.sqrt(q/(1-.999**it))+1e-8),-12,12)
    res2=minimize(fg,bestx[1],jac=True,method='L-BFGS-B',bounds=[(-12,12)]*v.size,
      options={'maxiter':LBFGS,'maxls':40,'ftol':1e-13,'gtol':1e-9,'maxcor':25})
    choices=[(initial['objective'],v,'zero'),(float(res.fun),np.asarray(res.x),'lbfgs1'),(float(res2.fun),np.asarray(res2.x),'lbfgs2')]
    val,x,label=min(choices,key=lambda y:y[0])
    final=diagnostics(x,R,ell,pr)
    final['selected_stage']=label; final['optimizer_messages']=[str(res.message),str(res2.message)]; final['wall_s']=time.time()-t0
    return scan,initial,final,x


def main():
    print(f"Step75 constrained nonflat-exit search {MODE}: Kz={base.KZ}, grid={NR}x{NZ}, rawJ={RAWJ}")
    print(f"center scalar projection error={np.max(np.abs(base.center_scalar+6)):.3e}; tangential Galerkin mismatch={np.max(np.abs(center_tangent_mismatch)):.3e}")
    out={'scope':'full five-component finite spectral test; fixed Step69 center and nonflat cosh(R)^2 q0 exit; not an existence theorem',
      'mode':MODE,'grid':{'Kz':base.KZ,'Nr':NR,'Nz':NZ,'raw_even_radial':RAWJ},
      'center_scalar_projection_error_sup':float(np.max(np.abs(base.center_scalar+6))),
      'center_tangent_projection_mismatch_sup':float(np.max(np.abs(center_tangent_mismatch))),
      'runs':[]}
    cdir=Path(__file__).resolve().parents[1]/'data'/f'step75_constrained_coefficients_{MODE}'; cdir.mkdir(parents=True,exist_ok=True)
    for R in R_LIST:
        scan,ini,fin,x=run_one(R)
        out['runs'].append({'R':R,'carrier_scan':scan,'initial':ini,'final':fin})
        np.save(cdir/f'R{R:g}.npy',x)
        print(f"R={R:g}: {ini['full_residual']['operator_sup']:.6g} -> {fin['full_residual']['operator_sup']:.6g}; obj {ini['objective']:.6g}->{fin['objective']:.6g}; exit {fin['exit']}",flush=True)
    path=Path(__file__).resolve().parents[1]/'data'/f'step75_constrained_nonflat_exit_{MODE}.json'
    path.write_text(json.dumps(out,indent=2),encoding='utf-8'); print('wrote',path)

if __name__=='__main__': main()

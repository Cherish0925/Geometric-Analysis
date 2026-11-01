#!/usr/bin/env python3
"""Full-residual core-entry search with exact center jet and free exit flux.

This is the corrected Step-75 experiment.  It keeps the validated Step-69
scalar-minus-six center q0, reflection, and the exact Koiso second normal jet.
A bounded even carrier realizes that jet; free even boundary-layer and global
modes vanish through order two at the center.  The exit metric and shape are
free.  All five orthonormal components of Ric+3g are minimized.  A second
continuation adds soft costs for S->I and scaled intrinsic Ricci->0, never the
obstructed condition d_r(R)=0 exactly.

Finite spectral experiment in the diagonal orthogonally-transitive class only.
"""
from __future__ import annotations
import importlib.util,json,math,sys,time
from pathlib import Path
import numpy as np
from numpy.polynomial import Polynomial,Chebyshev
from scipy.optimize import least_squares
import jax
jax.config.update('jax_enable_x64',True)
import jax.numpy as jnp
from jax import jit,jacfwd

MODE=sys.argv[1] if len(sys.argv)>1 else 'pilot'
if MODE=='pilot':
    KZ,NZ,NR,R_LIST,MAX0,MAX1=(5,32,31,[2.0,4.0,6.0],75,75)
elif MODE=='refine':
    KZ,NZ,NR,R_LIST,MAX0,MAX1=(7,48,45,[4.0,6.0,8.0],130,130)
else: raise ValueError(MODE)
TWOPI=2*np.pi
parent=Path(__file__).resolve().parent
oldargv=sys.argv[:]; sys.argv=[sys.argv[0],'pilot']
spec=importlib.util.spec_from_file_location('s75base',parent/'step75_full_residual_core_search.py')
base=importlib.util.module_from_spec(spec); spec.loader.exec_module(base)
sys.argv=oldargv

z_np=TWOPI*np.arange(NZ)/NZ
Z_np,Z1_np,Z2_np=base.real_fourier_basis(z_np,KZ); NM=Z_np.shape[1]
raw=np.stack(base.yamabe_center(z_np))
C0=np.stack([np.linalg.lstsq(Z_np,v,rcond=None)[0] for v in raw])
center=C0@Z_np.T; center_z=C0@Z1_np.T; center_zz=C0@Z2_np.T
center_ric=base.intrinsic_ric_np(center,center_z,center_zz)
center_scalar=center_ric.sum(0)
Gcoef=np.stack([np.linalg.lstsq(Z_np,center_ric[i]+2,rcond=None)[0] for i in range(3)])
Gval=Gcoef@Z_np.T

Z=jnp.asarray(Z_np); Z1=jnp.asarray(Z1_np); Z2=jnp.asarray(Z2_np)
C0j=jnp.asarray(C0); Gj=jnp.asarray(Gcoef)
LOCAL_ELL=[0.28,0.40,0.58,0.85,1.25]
NGLOBAL=9


def radial_free_basis(r,R):
    vals=[]; d1=[]; d2=[]; names=[]
    # Local even modes, each O(1), vanishing through second order at r=0.
    for ell in LOCAL_ELL:
        x=r/ell; e=np.exp(-x*x)
        vals.append(x**4*e)
        d1.append(e*(4*x**3-2*x**5)/ell)
        d2.append(e*(12*x**2-18*x**4+4*x**6)/(ell*ell))
        names.append(f'local_{ell}')
    # Global even polynomial modes s^4 T_j(2s^2-1), normalized in value norm.
    sp=Polynomial([0,1]); arg=2*sp**2-1
    for j in range(NGLOBAL):
        p=sp**4*Chebyshev.basis(j).convert(kind=Polynomial)(arg)
        v=p(r/R); v1=p.deriv(1)(r/R)/R; v2=p.deriv(2)(r/R)/(R*R)
        scale=max(np.sqrt(np.mean(v*v)),1e-12)
        vals.append(v/scale); d1.append(v1/scale); d2.append(v2/scale); names.append(f'global_{j}')
    return np.array(vals).T,np.array(d1).T,np.array(d2).T,names


def carrier(r,ell):
    x=r/ell; e=np.exp(-x*x)
    return .5*ell*ell*(1-e),r*e,e*(1-2*x*x)


def make_problem(R,ell,interface_weight):
    # Grid includes a fixed-resolution inner region and a uniform outer region.
    inner=np.linspace(0,min(1.5,R),max(16,int(NR*min(1.5,R)/R)),endpoint=False)
    outer=np.linspace(min(1.5,R),R,NR-len(inner))
    r_np=np.unique(np.concatenate((inner,outer)))
    B_np,B1_np,B2_np,names=radial_free_basis(r_np,R); J=B_np.shape[1]
    rho_np,rho1_np,rho2_np=carrier(r_np,ell)
    r=jnp.asarray(r_np); B=jnp.asarray(B_np); B1=jnp.asarray(B1_np); B2=jnp.asarray(B2_np)
    rho=jnp.asarray(rho_np); rho1=jnp.asarray(rho1_np); rho2=jnp.asarray(rho2_np)
    # Trapezoidal physical weights, normalized to average over r,z.
    wr=np.empty(len(r_np)); wr[0]=(r_np[1]-r_np[0])/2; wr[-1]=(r_np[-1]-r_np[-2])/2
    wr[1:-1]=(r_np[2:]-r_np[:-2])/2; wr=wr/R
    sqrtw=jnp.sqrt(jnp.asarray(wr)[:,None]/NZ)

    def fields(v):
        coef=v.reshape(3,J,NM)
        A=base.logcosh(r); Ar=jnp.tanh(r); Arr=1/jnp.cosh(r)**2
        l0=jnp.einsum('im,zm->iz',C0j,Z); l0z=jnp.einsum('im,zm->iz',C0j,Z1); l0zz=jnp.einsum('im,zm->iz',C0j,Z2)
        gv=jnp.einsum('im,zm->iz',Gj,Z); gvz=jnp.einsum('im,zm->iz',Gj,Z1); gvzz=jnp.einsum('im,zm->iz',Gj,Z2)
        F=jnp.einsum('rj,ijm,zm->irz',B,coef,Z)
        Fr=jnp.einsum('rj,ijm,zm->irz',B1,coef,Z)
        Frr=jnp.einsum('rj,ijm,zm->irz',B2,coef,Z)
        Fz=jnp.einsum('rj,ijm,zm->irz',B,coef,Z1)
        Fzz=jnp.einsum('rj,ijm,zm->irz',B,coef,Z2)
        Frz=jnp.einsum('rj,ijm,zm->irz',B1,coef,Z1)
        L=l0[:,None,:]+A[None,:,None]+rho[None,:,None]*gv[:,None,:]+F
        Lr=Ar[None,:,None]+rho1[None,:,None]*gv[:,None,:]+Fr
        Lrr=Arr[None,:,None]+rho2[None,:,None]*gv[:,None,:]+Frr
        Lz=l0z[:,None,:]+rho[None,:,None]*gvz[:,None,:]+Fz
        Lzz=l0zz[:,None,:]+rho[None,:,None]*gvzz[:,None,:]+Fzz
        Lrz=rho1[None,:,None]*gvz[:,None,:]+Frz
        return L,Lr,Lrr,Lz,Lzz,Lrz

    def components(v):
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

    def residual(v):
        E,f=components(v)
        core=jnp.stack((E[0],jnp.sqrt(2.)*E[1],E[2],E[3],E[4]))*sqrtw[None]
        out=[core.reshape(-1)]
        coef=v.reshape(3,J,NM)
        # Very weak shell regularization only.
        shell=jnp.zeros(NM).at[max(0,NM-4):].set(1.)
        out.append(2e-6*(coef*shell[None,None,:]).reshape(-1))
        if interface_weight>0:
            L,Lr,Lrr,Lz,Lzz,Lrz=f
            ric=intrinsic_ric_jax(L[:,-1],Lz[:,-1],Lzz[:,-1])
            w=math.sqrt(interface_weight/(3*NZ))
            out.append(w*(Lr[:,-1]-1).reshape(-1))
            out.append(.25*w*ric.reshape(-1))
        return jnp.concatenate(out)
    return {'r':r_np,'J':J,'names':names,'fields':fields,'components':components,'residual':residual}


def intrinsic_ric_jax(L,Lz,Lzz):
    a,b,c=L; az,bz,cz=Lz; _,bzz,czz=Lzz; em2a=jnp.exp(-2*a)
    return jnp.stack((-em2a*((bzz-az*bz)+bz*bz+(czz-az*cz)+cz*cz),
      -em2a*((bzz-az*bz)+bz*bz+bz*cz),
      -em2a*((czz-az*cz)+cz*cz+bz*cz)))


def diagnostics(v,R,ell,pr,label):
    E=np.asarray(pr['components'](jnp.asarray(v))[0]); f=[np.asarray(x) for x in pr['components'](jnp.asarray(v))[1]]
    L,Lr,Lrr,Lz,Lzz,Lrz=f; r=pr['r']
    tr=E[0]+E[2]; disc=np.sqrt((E[0]-E[2])**2+4*E[1]**2)
    op=np.maximum.reduce((np.abs((tr-disc)/2),np.abs((tr+disc)/2),np.abs(E[3]),np.abs(E[4])))
    ricR=base.intrinsic_ric_np(L[:,-1],Lz[:,-1],Lzz[:,-1])
    req=1+Gval
    d=L[1]-L[2]; dr=Lr[1]-Lr[2]
    H=Lr.sum(0); shear=np.sum((Lr-1)**2,axis=0)
    normal=Lrr.sum(0)+np.sum(Lr**2,axis=0)-3+E[0]
    bal=np.exp(2*R)*(H[-1]-3)+3+np.trapezoid(np.exp(2*r)[:,None]*(shear+E[0]),r,axis=0)
    return {'label':label,'R_physical':R,'carrier_ell':ell,'residual_l2':float(np.linalg.norm(np.asarray(pr['residual'](jnp.asarray(v))))),
      'operator_sup':float(op.max()),'operator_rms':float(np.sqrt(np.mean(op**2))),
      'component_sup':{k:float(np.abs(E[i]).max()) for i,k in enumerate(['E_rr','E_rz_orth','E_zz','E_x','E_y'])},
      'argmax_r':float(r[np.unravel_index(np.argmax(op),op.shape)[0]]),
      'center':{'S_sup':float(np.abs(Lr[:,0]).max()),'second_jet_error_sup':float(np.abs(Lrr[:,0]-req).max()),
        'component_sup':{k:float(np.abs(E[i,0]).max()) for i,k in enumerate(['E_rr','E_rz_orth','E_zz','E_x','E_y'])}},
      'exit':{'S_minus_I_sup':float(np.abs(Lr[:,-1]-1).max()),'S_minus_I_rms':float(np.sqrt(np.mean((Lr[:,-1]-1)**2))),
        'd_r_sup':float(np.abs(dr[-1]).max()),'weighted_anisotropy_flux_sup':float(np.max(np.exp(L[0,-1]+L[1,-1]+L[2,-1])*np.abs(dr[-1]))),
        'intrinsic_Ric_sup':float(np.abs(ricR).max()),'anisotropy_oscillation':float(np.ptp(d[-1])),
        'logmetric_min':float(L[:,-1].min()),'logmetric_max':float(L[:,-1].max())},
      'normal_identity_pointwise_sup':float(np.abs(normal).max()),'normal_budget_quad_sup':float(np.abs(bal).max()),
      'coefficient_norm':float(np.linalg.norm(v)),'coefficient_max':float(np.abs(v).max()),'field_range':[float(L.min()),float(L.max())]}


def solve_stage(pr,x0,maxn):
    rfun=jit(pr['residual']); jfun=jit(jacfwd(pr['residual']))
    def fun(x): return np.asarray(rfun(jnp.asarray(x)),float)
    def jac(x): return np.asarray(jfun(jnp.asarray(x)),float)
    return least_squares(fun,x0,jac=jac,method='trf',tr_solver='lsmr',x_scale='jac',bounds=(-15,15),
      max_nfev=maxn,ftol=5e-11,xtol=5e-11,gtol=5e-11,verbose=0)


def main():
    print(f"Step75 corrected core-entry GN {MODE}: Kz={KZ}, Nz={NZ}, nominal Nr={NR}")
    print(f"center scalar projection error={np.abs(center_scalar+6).max():.3e}")
    out={'scope':'all-five-component finite spectral search; exact Step69 center/Koiso 2-jet; free exit shape and nonflat metric; not existence',
      'mode':MODE,'Kz':KZ,'Nz':NZ,'center_scalar_projection_error_sup':float(np.abs(center_scalar+6).max()),'runs':[]}
    cdir=Path(__file__).resolve().parents[1]/'data'/f'step75_core_entry_coefficients_{MODE}'; cdir.mkdir(parents=True,exist_ok=True)
    for R in R_LIST:
        scans=[]
        for ell in [0.22,0.30,0.42,0.60,0.85]:
            pr=make_problem(R,ell,0.0); x=np.zeros(3*pr['J']*NM); d=diagnostics(x,R,ell,pr,'carrier')
            scans.append((d['residual_l2'],ell,pr,d))
        scans.sort(key=lambda q:q[0]); _,ell,pr,d0=scans[0]
        print('R',R,'carrier scans',[(round(e,2),round(d['operator_sup'],3),round(q,3)) for q,e,p,d in scans],flush=True)
        t0=time.time(); x0=np.zeros(3*pr['J']*NM); res0=solve_stage(pr,x0,MAX0); dres=diagnostics(res0.x,R,ell,pr,'residual_only')
        # Continue with soft entry objective; rebuild basis-identical problem.
        pr1=make_problem(R,ell,1.0); res1=solve_stage(pr1,res0.x,MAX1); dent=diagnostics(res1.x,R,ell,pr1,'soft_entry')
        print(f"R={R:g}: carrier op {d0['operator_sup']:.4g}; residual-only {dres['operator_sup']:.4g}, exitS {dres['exit']['S_minus_I_sup']:.3g}; soft {dent['operator_sup']:.4g}, exitS {dent['exit']['S_minus_I_sup']:.3g}; wall {time.time()-t0:.1f}s",flush=True)
        row={'R':R,'carrier_scan':[d for q,e,p,d in scans],'selected_ell':ell,'residual_only':dres,'soft_entry':dent,
          'solvers':[{'message':str(res0.message),'nfev':int(res0.nfev),'cost':float(res0.cost),'optimality':float(res0.optimality)},
                     {'message':str(res1.message),'nfev':int(res1.nfev),'cost':float(res1.cost),'optimality':float(res1.optimality)}]}
        out['runs'].append(row); np.save(cdir/f'R{R:g}_res.npy',res0.x); np.save(cdir/f'R{R:g}_entry.npy',res1.x)
    path=Path(__file__).resolve().parents[1]/'data'/f'step75_core_entry_gauss_newton_{MODE}.json'; path.write_text(json.dumps(out,indent=2),encoding='utf-8'); print('wrote',path)

if __name__=='__main__': main()

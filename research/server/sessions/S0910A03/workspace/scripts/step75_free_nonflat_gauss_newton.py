#!/usr/bin/env python3
"""Gauss--Newton search with free nonflat expanded exit data.

Metric and equations are the same full five-component Gaussian system used in
Step 75.  The Step-69 center q0 is fixed and reflection is exact.  Corrections
use
  B_j(r)=R^2 (1-cos(j*pi*r/R))/(j*pi)^2.
Thus B_j(0)=B'_j(0)=B'_j(R)=0, while B''_j(0)=1.  The Einstein equations,
not a prescribed CMC source, choose the center second jet and outer nonflat
profile.  At the exit S=tanh(R) I exactly; for R growing this is the umbilic
entry required by the Step-73 tail.  We solve all five Ricci residuals by
nonlinear least squares and then inspect the true operator sup norm.

Finite spectral evidence only; no continuum existence inference.
"""
from __future__ import annotations
import importlib.util,json,math,sys,time
from pathlib import Path
import numpy as np
from scipy.optimize import least_squares,minimize
import jax
jax.config.update('jax_enable_x64',True)
import jax.numpy as jnp
from jax import jit,jacfwd,value_and_grad

MODE=sys.argv[1] if len(sys.argv)>1 else 'pilot'
if MODE=='pilot':
    KZ,J,NR,NZ,R_LIST,MAXN=(3,8,19,20,[2.0,4.0,6.0],90)
elif MODE=='refine':
    KZ,J,NR,NZ,R_LIST,MAXN=(5,12,29,32,[4.0,6.0,8.0],160)
else: raise ValueError(MODE)
TWOPI=2*np.pi
parent=Path(__file__).resolve().parent
# Import only for the validated Yamabe center and intrinsic-Ricci utility.
oldargv=sys.argv[:]; sys.argv=[sys.argv[0],'pilot']
spec=importlib.util.spec_from_file_location('s75base',parent/'step75_full_residual_core_search.py')
base=importlib.util.module_from_spec(spec); spec.loader.exec_module(base)
sys.argv=oldargv

s_np=np.linspace(0,1,NR); z_np=TWOPI*np.arange(NZ)/NZ
Z_np,Z1_np,Z2_np=base.real_fourier_basis(z_np,KZ); NM=Z_np.shape[1]
raw=np.stack(base.yamabe_center(z_np))
C0=np.stack([np.linalg.lstsq(Z_np,v,rcond=None)[0] for v in raw])
center=C0@Z_np.T; center_z=C0@Z1_np.T; center_zz=C0@Z2_np.T
center_ric=base.intrinsic_ric_np(center,center_z,center_zz)
center_scalar=np.sum(center_ric,axis=0)
# Fourier projection of the exact Koiso correction L_rr-logcosh_rr=Ric(q0)+2.
Gcoef=np.stack([np.linalg.lstsq(Z_np,center_ric[i]+2,rcond=None)[0] for i in range(3)])

s=jnp.asarray(s_np); Z=jnp.asarray(Z_np); Z1=jnp.asarray(Z1_np); Z2=jnp.asarray(Z2_np)
C0j=jnp.asarray(C0)


def make_problem(R):
    r=R*s_np
    BV=[]; B1=[]; B2=[]
    for j in range(1,J+1):
        kp=j*np.pi
        BV.append(R*R*(1-np.cos(kp*s_np))/(kp*kp))
        B1.append(R*np.sin(kp*s_np)/kp)
        B2.append(np.cos(kp*s_np))
    BV=np.array(BV).T; B1=np.array(B1).T; B2=np.array(B2).T
    Bj=jnp.asarray(BV); B1j=jnp.asarray(B1); B2j=jnp.asarray(B2); rj=R*s

    def fields(v):
        coef=v.reshape(3,J,NM)
        A=base.logcosh(rj); Ar=jnp.tanh(rj); Arr=1/jnp.cosh(rj)**2
        l0=jnp.einsum('im,zm->iz',C0j,Z)
        l0z=jnp.einsum('im,zm->iz',C0j,Z1)
        l0zz=jnp.einsum('im,zm->iz',C0j,Z2)
        F=jnp.einsum('rj,ijm,zm->irz',Bj,coef,Z)
        Fr=jnp.einsum('rj,ijm,zm->irz',B1j,coef,Z)
        Frr=jnp.einsum('rj,ijm,zm->irz',B2j,coef,Z)
        Fz=jnp.einsum('rj,ijm,zm->irz',Bj,coef,Z1)
        Fzz=jnp.einsum('rj,ijm,zm->irz',Bj,coef,Z2)
        Frz=jnp.einsum('rj,ijm,zm->irz',B1j,coef,Z1)
        return (l0[:,None,:]+A[None,:,None]+F,
                Ar[None,:,None]+Fr,
                Arr[None,:,None]+Frr,
                l0z[:,None,:]+Fz,l0zz[:,None,:]+Fzz,Frz)

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

    # Physical uniform-grid quadrature; sqrt(2) on E_rz gives Frobenius base weight.
    def residual(v):
        E,f=components(v)
        core=jnp.stack((E[0],jnp.sqrt(2.0)*E[1],E[2],E[3],E[4])).reshape(-1)
        coef=v.reshape(3,J,NM)
        # Tiny regularization suppresses unresolved highest radial/Fourier shells.
        kr=(jnp.arange(J)+1)/J
        shell=jnp.zeros(NM).at[max(0,NM-4):].set(1.0)
        reg=2e-5*(coef*(kr[None,:,None]**3+shell[None,None,:])).reshape(-1)
        # Keep exit corrections O(1) relative to expansion without making them flat.
        Fexit=f[0][:,-1,:]-(jnp.einsum('im,zm->iz',C0j,Z)+base.logcosh(jnp.array(R)))
        exitreg=2e-4*Fexit.reshape(-1)
        return jnp.concatenate((core,reg,exitreg))
    return fields,components,residual,BV,B1,B2


def koiso_initial():
    """Use j=1 to impose exact projected center second jet; otherwise zero."""
    v=np.zeros((3,J,NM)); v[:,0,:]=Gcoef
    return v.reshape(-1)


def diagnostics(v,R,problem,label):
    fields,components,residual,BV,B1,B2=problem
    Ej,fj=components(jnp.asarray(v)); E=np.asarray(Ej); f=[np.asarray(x) for x in fj]
    L,Lr,Lrr,Lz,Lzz,Lrz=f
    tr=E[0]+E[2]; disc=np.sqrt((E[0]-E[2])**2+4*E[1]**2)
    lm=.5*(tr-disc); lp=.5*(tr+disc)
    op=np.maximum.reduce((np.abs(lm),np.abs(lp),np.abs(E[3]),np.abs(E[4])))
    ricR=base.intrinsic_ric_np(L[:,-1],Lz[:,-1],Lzz[:,-1])
    # center second jet mismatch to projected Koiso data
    req=(Gcoef@Z_np.T)+1.0
    secerr=Lrr[:,0]-req
    # exact normal identity and integrated budget
    H=np.sum(Lr,axis=0); sh=np.sum((Lr-1)**2,axis=0)
    normal=Lrr.sum(axis=0)+np.sum(Lr**2,axis=0)-3+E[0]
    rr=R*s_np
    bal=np.exp(2*R)*(H[-1]-3)+3+np.trapezoid(np.exp(2*rr)[:,None]*(sh+E[0]),rr,axis=0)
    corr_exit=L[:,-1]-center-base.logcosh(jnp.array(R))
    return {'label':label,'R_physical':R,'residual_l2':float(np.linalg.norm(np.asarray(residual(jnp.asarray(v))))),
      'operator_sup':float(op.max()),'operator_rms':float(np.sqrt(np.mean(op**2))),
      'component_sup':{k:float(np.abs(E[i]).max()) for i,k in enumerate(['E_rr','E_rz_orth','E_zz','E_x','E_y'])},
      'argmax_r':float(rr[np.unravel_index(np.argmax(op),op.shape)[0]]),
      'center':{'S_sup':float(np.abs(Lr[:,0]).max()),'second_jet_error_sup':float(np.abs(secerr).max()),
        'component_sup':{k:float(np.abs(E[i,0]).max()) for i,k in enumerate(['E_rr','E_rz_orth','E_zz','E_x','E_y'])}},
      'exit':{'S_minus_I_sup':float(np.abs(Lr[:,-1]-1).max()),
        'correction_sup':float(np.abs(corr_exit).max()),'correction_oscillation':float(np.max(np.ptp(corr_exit,axis=1))),
        'anisotropy_oscillation':float(np.ptp(L[1,-1]-L[2,-1])),
        'intrinsic_Ric_sup':float(np.abs(ricR).max()),
        'scaled_curvature_already_in_Ric_sup':float(np.abs(ricR).max()),
        'logmetric_min':float(L[:,-1].min())},
      'normal_identity_pointwise_sup':float(np.abs(normal).max()),'normal_budget_quad_sup':float(np.abs(bal).max()),
      'coefficient_norm':float(np.linalg.norm(v)),'coefficient_max':float(np.abs(v).max()),
      'field_range':[float(L.min()),float(L.max())]}


def solve_R(R):
    problem=make_problem(R); residual=problem[2]
    rjit=jit(residual); jjit=jit(jacfwd(residual))
    def fun(x): return np.asarray(rjit(jnp.asarray(x)),dtype=float)
    def jac(x): return np.asarray(jjit(jnp.asarray(x)),dtype=float)
    starts=[('zero',np.zeros(3*J*NM)),('koiso_j1',koiso_initial())]
    attempts=[]; best=None
    for name,x0 in starts:
        d0=diagnostics(x0,R,problem,name+'_initial')
        print(f" R={R:g} {name} initial op={d0['operator_sup']:.5g} secondjet={d0['center']['second_jet_error_sup']:.3g}",flush=True)
        t0=time.time()
        res=least_squares(fun,x0,jac=jac,method='trf',tr_solver='lsmr',x_scale='jac',
          bounds=(-20,20),max_nfev=MAXN,ftol=2e-11,xtol=2e-11,gtol=2e-11,verbose=0)
        d=diagnostics(res.x,R,problem,name+'_least_squares')
        d['solver']={'success':bool(res.success),'status':int(res.status),'message':str(res.message),'nfev':int(res.nfev),'njev':int(res.njev),'cost':float(res.cost),'optimality':float(res.optimality),'wall_s':time.time()-t0}
        attempts.append({'initial':d0,'final':d})
        print(f" R={R:g} {name} LS op={d['operator_sup']:.6g} rms={d['operator_rms']:.4g} cost={res.cost:.4g} nfev={res.nfev}",flush=True)
        if best is None or d['operator_sup']<best[0]: best=(d['operator_sup'],res.x,d)
    return attempts,best,problem


def main():
    print(f"Step75 free-exit Gauss-Newton {MODE}: Kz={KZ}, J={J}, grid={NR}x{NZ}, variables={3*J*NM}")
    print(f"center projected scalar error={np.abs(center_scalar+6).max():.3e}")
    out={'scope':'all-five-component finite Gaussian metric search; free nonflat exit with exact umbilic slope; not continuum existence',
      'mode':MODE,'grid':{'Kz':KZ,'J':J,'Nr':NR,'Nz':NZ,'variables':3*J*NM},
      'radial_basis':'R^2(1-cos(j*pi*r/R))/(j*pi)^2: center value/slope and exit slope fixed; center second jet and exit profile free',
      'center_scalar_projection_error_sup':float(np.abs(center_scalar+6).max()),'runs':[]}
    cdir=Path(__file__).resolve().parents[1]/'data'/f'step75_free_exit_coefficients_{MODE}'; cdir.mkdir(parents=True,exist_ok=True)
    for R in R_LIST:
        attempts,best,problem=solve_R(R); op,x,d=best
        out['runs'].append({'R':R,'attempts':attempts,'selected':d})
        np.save(cdir/f'R{R:g}.npy',x)
    path=Path(__file__).resolve().parents[1]/'data'/f'step75_free_nonflat_gauss_newton_{MODE}.json'
    path.write_text(json.dumps(out,indent=2),encoding='utf-8'); print('wrote',path)

if __name__=='__main__': main()

"""Explore anisotropic/high-shear perturbations of the collapsed saturation entry.

This imports the exact full-control collocation problem and changes only the initial
first jet in the regularized variables
    (x,z,p,chi,eta) = I_eps(A) + (x0,0,0,chi0,eta0).
The exact Taub-bolt/Lambda-Taub-NUT ray is x0=chi0=eta0=0.  Nonzero data do not
come from a proved regular bolt matching theorem; they deliberately enlarge the
entry set to test whether anisotropic collapsed jets could undercut the biaxial
value and to identify the dangerous shear directions.

Environment:
  SAT_ENTRY_X, SAT_ENTRY_CHI, SAT_ENTRY_ETA are additive entry perturbations.
  SAT_W_X, SAT_W_CHI, SAT_W_ETA optionally set warm-start entry perturbations.
The output records the exact initial chiral charge, optimizer status and trajectory.
"""
from __future__ import annotations
import json, math, os, sys
from pathlib import Path
import numpy as np
import casadi as ca
import saturation_optimal_control as so

OUT=Path(__file__).resolve().parents[1]/'data'/'saturation_control'


def entry_delta(eps):
    z=eps**(1/3); mode=os.environ.get('SAT_ENTRY_MODE','raw')
    if mode=='regular':
        # Controlled F-structure scaling: x=X z^3, chi=C z, eta=N z.
        return np.array([float(os.environ.get('SAT_ENTRY_X',0))*z**3,0,0,
                         float(os.environ.get('SAT_ENTRY_CHI',0))*z,
                         float(os.environ.get('SAT_ENTRY_ETA',0))*z],float)
    return np.array([float(os.environ.get('SAT_ENTRY_X',0)),0,0,
                     float(os.environ.get('SAT_ENTRY_CHI',0)),
                     float(os.environ.get('SAT_ENTRY_ETA',0))],float)

def warm_delta(eps):
    z=eps**(1/3); mode=os.environ.get('SAT_W_MODE','raw')
    if mode=='regular':
        return np.array([float(os.environ.get('SAT_W_X',0))*z**3,0,0,
                         float(os.environ.get('SAT_W_CHI',0))*z,
                         float(os.environ.get('SAT_W_ETA',0))*z],float)
    return np.array([float(os.environ.get('SAT_W_X',0)),0,0,
                     float(os.environ.get('SAT_W_CHI',0)),
                     float(os.environ.get('SAT_W_ETA',0))],float)

def solve(eps,N,warm=None):
    de=entry_delta(eps); opti=ca.Opti(); X=opti.variable(5,N+1); U=opti.variable(3,N+1)
    A=opti.variable(); tch=opti.variable(); T=opti.variable(); dt=T/N
    opti.subject_to(X[:,0]==so.entry_ca(eps,A)+ca.DM(de))
    opti.subject_to(X[:,-1]==so.ch_ca(tch))
    J=0
    for k in range(N):
        xk,xn=X[:,k],X[:,k+1]; uk,un=U[:,k],U[:,k+1]
        fk,fn=so.f_rhs(xk,uk),so.f_rhs(xn,un)
        xm=(xk+xn)/2+dt*(fk-fn)/8; um=(uk+un)/2; fm=so.f_rhs(xm,um)
        opti.subject_to(xn-xk==dt*(fk+4*fm+fn)/6)
        J+=dt*(so.running_cost(uk)+4*so.running_cost(um)+so.running_cost(un))/6
    opti.minimize(J)
    opti.subject_to(opti.bounded(.15,A,5)); opti.subject_to(opti.bounded(.701,tch,4))
    opti.subject_to(opti.bounded(.2,T,30)); opti.subject_to(opti.bounded(-3,X[0,:],6))
    opti.subject_to(opti.bounded(max(.03,.55*eps**(1/3)),X[1,:],1.7))
    opti.subject_to(opti.bounded(-40,X[2:5,:],40)); opti.subject_to(opti.bounded(-400,U,400))
    A0=float(os.environ.get('SAT_A0',.8)); t0=float(os.environ.get('SAT_T0CH',1.2)); T0=float(os.environ.get('SAT_TAU0',7))
    X0,U0=so.hermite_guess(eps,N,A0,t0,T0); X0+=de[:,None]*(1-np.linspace(0,1,N+1))[None,:]**3
    opti.set_initial(A,A0); opti.set_initial(tch,t0); opti.set_initial(T,T0); opti.set_initial(X,X0); opti.set_initial(U,U0)
    if warm:
        rec=json.loads(Path(warm).read_text()); A0=rec['A']; t0=rec['t_ch']; T0=rec['T']
        oldX=np.asarray(rec['X'],float).T; oldU=np.asarray(rec['U'],float).T
        sn=np.linspace(0,1,N+1); sox=np.linspace(0,1,oldX.shape[1])
        Xi=np.vstack([np.interp(sn,sox,row) for row in oldX]); Ui=np.vstack([np.interp(sn,sox,row) for row in oldU])
        target=so.entry_np(eps,A0)+de; source=Xi[:,0]+warm_delta(eps)
        Xi+=(target-source)[:,None]*(1-sn)[None,:]**3
        opti.set_initial(A,A0); opti.set_initial(tch,t0); opti.set_initial(T,T0); opti.set_initial(X,Xi); opti.set_initial(U,Ui)
    opti.solver('ipopt',{'expand':True,'print_time':False,'ipopt':{'print_level':0,'max_iter':3500,'tol':2e-8,'acceptable_tol':2e-6,'linear_solver':'mumps','mu_strategy':'adaptive'}})
    try:
        sol=opti.solve(); ok=True; stats=sol.stats(); val=lambda v:np.array(sol.value(v),float)
    except RuntimeError:
        ok=False; stats=opti.stats(); val=lambda v:np.array(opti.debug.value(v),float)
    xv,uv=val(X),val(U); Av=float(val(A)); tv=float(val(tch)); Tv=float(val(T)); Jv=float(val(J))
    bp=np.array([so.bplus_np(xv[:,k]) for k in range(N+1)])
    rec={'eps':eps,'N':N,'success':ok,'return_status':stats.get('return_status'),'iterations':stats.get('iter_count'),
         'entry_delta':de.tolist(),'cost':Jv,'A':Av,'t_ch':tv,'T':Tv,'initial_state':xv[:,0].tolist(),
         'terminal_state':xv[:,-1].tolist(),'bplus_initial':float(bp[0]),'bplus_terminal':float(bp[-1]),
         'min_bplus':float(bp.min()),'max_bplus':float(bp.max()),'X':xv.T.tolist(),'U':uv.T.tolist(),'bplus':bp.tolist()}
    tag=os.environ.get('SAT_TAG','aniso'); path=OUT/f'{tag}.json'; path.write_text(json.dumps(rec,indent=1))
    print(json.dumps({k:v for k,v in rec.items() if k not in ('X','U','bplus')},indent=1)); print(path)
    return 0 if ok else 1

if __name__=='__main__':
    raise SystemExit(solve(float(sys.argv[1]),int(sys.argv[2]),sys.argv[3] if len(sys.argv)>3 and sys.argv[3]!='-' else None))

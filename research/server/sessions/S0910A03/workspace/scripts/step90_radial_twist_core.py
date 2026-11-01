"""
Step 90: integrate the exact constant-charge radial free-T^2 reduced system.

Ansatz on a polar base disk:
  gamma = dr^2 + psi(r)^2 dtheta^2,
  M = diag(exp(alpha), exp(-alpha)), q=(q0,0),
  Q = Q0 exp[-3(sigma-sigma0) - (alpha-alpha0)].

The exact reduced equations imply, with u=sigma', v=alpha', H=psi'/psi,
  u' = 6+Q-u^2-Hu,
  v' = Q-Hv-uv,
  H' = -K-H^2,
  K  = -3+Q+H u,
plus the rr horizontal equation.  Eliminating K yields the evolution below.
Smooth-center series at r=0:
  u=((6+Q0)/2)r+O(r^3), v=(Q0/2)r+O(r^3),
  H=1/r-(Q0/2)r+O(r^3), psi=r-(Q0/4)r^3+O(r^5).
The script integrates and records the unused rr constraint residual, thereby
checking whether the evolution subsystem propagates the full exact equations.
"""
from pathlib import Path
import argparse, json
import numpy as np
from scipy.integrate import solve_ivp


def rhs(r, y, q0):
    sigma, alpha, u, v, H, logpsi = y
    Q = 0.5*q0*q0*np.exp(-3*sigma-alpha)
    K = -3 + Q + H*u
    return [u, v,
            6+Q-u*u-H*u,
            Q-H*v-u*v,
            -K-H*H,
            H]


def integrate(Q0, rmax=4.0):
    # Normalize sigma0=alpha0=0, so q0=sqrt(2Q0).
    q0=np.sqrt(2*Q0)
    eps=min(1e-5,1e-3/max(1.0,np.sqrt(Q0)))
    # Leading smooth series, sufficient for a residual/phase pilot.
    u1=(6+Q0)/2
    v1=Q0/2
    sigma0=0.5*u1*eps**2
    alpha0=0.5*v1*eps**2
    H0=1/eps-(Q0/2)*eps
    logpsi0=np.log(eps)-(Q0/4)*eps**2
    y0=[sigma0,alpha0,u1*eps,v1*eps,H0,logpsi0]

    def stop_bad(r,y):
        return 50-max(abs(y[2]),abs(y[3]),abs(y[4]),abs(y[0]),abs(y[1]))
    stop_bad.terminal=True
    stop_bad.direction=-1
    sol=solve_ivp(lambda r,y:rhs(r,y,q0),(eps,rmax),y0,rtol=1e-10,atol=1e-12,
                  max_step=2e-3,events=stop_bad,dense_output=False)
    r=sol.t; sigma,alpha,u,v,H,logpsi=sol.y
    Q=0.5*q0*q0*np.exp(-3*sigma-alpha)
    K=-3+Q+H*u
    up=6+Q-u*u-H*u
    # rr equation E_rr= K-u'+3-Q-u^2/2-v^2/2 = 0.
    Err=K-up+3-Q-0.5*u*u-0.5*v*v
    # Physical charge amplitude and damping coefficient.
    w=np.sqrt(2*Q)
    D=0.5*(3*u+v)
    # Constraint-normalized error away from r=0.
    scale=1+np.abs(K)+np.abs(up)+Q+u*u+v*v
    rel=np.abs(Err)/scale
    # Radii at which physical Q is damped to benchmarks.
    radii={}
    for target in [1.0,0.1,0.01,1e-3,1e-4]:
        idx=np.where(Q<=target)[0]
        radii[str(target)]=float(r[idx[0]]) if len(idx) else None
    return {
      'Q0':float(Q0),'q0':float(q0),'success':bool(sol.success),
      'message':sol.message,'r_final':float(r[-1]),'n_steps':int(len(r)),
      'Q_final':float(Q[-1]),'w_final':float(w[-1]),
      'sigma_final':float(sigma[-1]),'alpha_final':float(alpha[-1]),
      'u_final':float(u[-1]),'v_final':float(v[-1]),'H_final':float(H[-1]),
      'K_min':float(np.min(K)),'K_max':float(np.max(K)),
      'D_min':float(np.min(D)),'D_max':float(np.max(D)),
      'max_abs_rr_constraint':float(np.max(np.abs(Err))),
      'max_rel_rr_constraint':float(np.max(rel)),
      'rr_constraint_at_final':float(Err[-1]),
      'radii_Q_below':radii,
      'sample':[
        {'r':float(r[i]),'Q':float(Q[i]),'sigma':float(sigma[i]),
         'alpha':float(alpha[i]),'u':float(u[i]),'v':float(v[i]),
         'H':float(H[i]),'K':float(K[i]),'Err':float(Err[i])}
        for i in np.linspace(0,len(r)-1,min(24,len(r)),dtype=int)
      ]
    }

if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('--rmax',type=float,default=4.0)
    args=ap.parse_args()
    results=[integrate(Q,args.rmax) for Q in [0.1,1,3,10,30,100]]
    out={'ansatz':'exact constant-charge radial free-T2 core','runs':results}
    p=Path('workspace/data/step90_radial_twist_core.json');p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(out,indent=2),encoding='utf-8')
    print(json.dumps(out,indent=2))
    print(f'\nwrote {p}')

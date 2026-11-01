"""
Step 90: forced discharge of the exact radial charged core.

Integrate the exact constant-charge core to a chosen switch radius, then prescribe
physical mixed forcing b(r) to drive w=sqrt(2Q) to zero over a collar. Evolve the
remaining reduced variables with the area and orbit equations exact (T=Theta=0),
and monitor the two horizontal Ricci defects. This tests whether small mixed
forcing alone can taper twist while every Ricci block remains small.
"""
from pathlib import Path
import json, numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq


def core_rhs(r,y):
    sigma,alpha,u,v,H,w=y
    Q=.5*w*w; K=-3+Q+H*u
    return [u,v,6+Q-u*u-H*u,Q-H*v-u*v,-K-H*H,-.5*(3*u+v)*w]

def init(Q0):
    eps=min(1e-6,1e-4/max(1,np.sqrt(Q0)))
    u1=(6+Q0)/2;v1=Q0/2
    return eps,np.array([.5*u1*eps**2,.5*v1*eps**2,u1*eps,v1*eps,
                         1/eps-(Q0/2)*eps,np.sqrt(2*Q0)])

def core_to_Q(Q0,target):
    eps,y0=init(Q0)
    def evt(r,y): return .5*y[5]**2-target
    evt.terminal=True;evt.direction=-1
    sol=solve_ivp(core_rhs,(eps,5),y0,rtol=1e-11,atol=1e-13,max_step=5e-4,events=evt,dense_output=True)
    if len(sol.t_events[0])==0: raise RuntimeError('target not reached')
    rs=float(sol.t_events[0][0]);ys=sol.y_events[0][0]
    return rs,ys

def run(Q0,delta,L=1.0,target_factor=1.0):
    # Switch when w = target_factor*delta. Then choose a C1 physical forcing
    # b=-A sin^2(pi s/L) whose integral (with damping) kills w exactly at L.
    targetQ=.5*(target_factor*delta)**2
    rs,y0=core_to_Q(Q0,targetQ)
    w0=y0[5]

    # Determine A by a nonlinear scalar shooting solve. Since Q becomes tiny,
    # the result approaches the round-cusp linear prediction, but the integrated
    # geometry still depends on A through Q=w^2/2.
    def evolve(A,save=False):
        def rhs(s,y):
            sigma,alpha,u,v,H,w=y
            Q=.5*w*w; K=-3+Q+H*u
            shape=np.sin(np.pi*s/L)**2
            b=-A*shape
            return [u,v,6+Q-u*u-H*u,Q-H*v-u*v,-K-H*H,
                    b-.5*(3*u+v)*w]
        sol=solve_ivp(rhs,(0,L),y0,rtol=2e-10,atol=2e-12,max_step=L/2000,dense_output=False)
        return sol
    def fA(A): return evolve(A).y[5,-1]
    # Bracket from zero to a conservative multiple of w0/L.
    hi=max(10*w0/L,10*delta)
    while fA(hi)>0: hi*=2
    A=brentq(fA,0,hi,xtol=1e-13)
    sol=evolve(A,True)
    s=sol.t;sigma,alpha,u,v,H,w=sol.y
    Q=.5*w*w;K=-3+Q+H*u
    up=6+Q-u*u-H*u
    # We enforced T=Theta=0 and theta-theta base equation through K definition.
    Err=K-up+3-Q-.5*u*u-.5*v*v
    b=-A*np.sin(np.pi*s/L)**2
    return {
      'Q0':Q0,'delta':delta,'target_factor':target_factor,'L':L,
      'switch_r':rs,'switch_Q':float(.5*w0*w0),'switch_w':float(w0),
      'forcing_amplitude_A':float(A),'max_abs_b':float(np.max(np.abs(b))),
      'A_over_delta':float(A/delta),'w_final':float(w[-1]),
      'Q_max_taper':float(np.max(Q)),'Q_final':float(Q[-1]),
      'max_abs_Err':float(np.max(np.abs(Err))),
      'max_abs_T':0.0,'max_abs_Theta':0.0,
      'end':{'u':float(u[-1]),'v':float(v[-1]),'H':float(H[-1]),
             'sigma':float(sigma[-1]),'alpha':float(alpha[-1]),'K':float(K[-1])},
      'success':bool(sol.success),
      'sample':[
        {'s':float(s[i]),'Q':float(Q[i]),'w':float(w[i]),'b':float(b[i]),
         'u':float(u[i]),'v':float(v[i]),'H':float(H[i]),'Err':float(Err[i])}
        for i in np.linspace(0,len(s)-1,20,dtype=int)
      ]
    }

if __name__=='__main__':
    out={'description':'forced radial charge taper with area/orbit equations exact',
         'runs':[]}
    for Q0 in [1,10,100]:
      for delta in [0.1,0.03,0.01]:
        for L in [0.5,1.0,2.0]:
          out['runs'].append(run(Q0,delta,L,target_factor=1.0))
    p=Path('workspace/data/step90_radial_twist_taper.json');p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(out,indent=2),encoding='utf-8')
    # Compact stdout.
    print(json.dumps([{k:r[k] for k in ['Q0','delta','L','switch_r','A_over_delta','max_abs_Err','w_final']} for r in out['runs']],indent=2))
    print(f'\nwrote {p}')

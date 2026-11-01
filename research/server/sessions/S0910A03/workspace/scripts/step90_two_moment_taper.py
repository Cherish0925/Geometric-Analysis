"""
Step 90: two-moment sign-changing taper.

Use a two-mode forcing b=-A phi1 + B phi2, with smooth-enough sin^4 modes,
to shoot both w(L)=0 and the horizontal constraint C(L)=0.  This tests whether
the O(delta^2) terminal constraint left by monotone discharge is a real finite-
dimensional obstruction or can be canceled with an O(delta) sign-changing
Maxwell control.  The area, orbit, and theta-theta horizontal equations remain
exactly enforced.
"""
from pathlib import Path
import json, numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import root

# Reuse a compact implementation of the exact core.
def core_rhs(r,y):
    sigma,alpha,u,v,H,w=y;Q=.5*w*w;K=-3+Q+H*u
    return [u,v,6+Q-u*u-H*u,Q-H*v-u*v,-K-H*H,-.5*(3*u+v)*w]
def core_to(Q0,target):
    eps=min(1e-6,1e-4/max(1,np.sqrt(Q0)));u1=(6+Q0)/2;v1=Q0/2
    y0=[.5*u1*eps**2,.5*v1*eps**2,u1*eps,v1*eps,1/eps-(Q0/2)*eps,np.sqrt(2*Q0)]
    def ev(r,y):return .5*y[5]**2-target
    ev.terminal=True;ev.direction=-1
    sol=solve_ivp(core_rhs,(eps,6),y0,rtol=1e-11,atol=1e-13,max_step=5e-4,events=ev)
    return float(sol.t_events[0][0]),sol.y_events[0][0]

def run(Q0,delta,L):
    rs,ybase=core_to(Q0,.5*delta**2)
    # State appends exact constraint C, initialized by core propagation as 0.
    y0=np.r_[ybase,0.0]
    def shapes(s):
        # Both modes vanish to fourth order at endpoints. phi2 is shifted to the
        # later half, enabling a small recharge/counterpulse to cancel C.
        phi1=np.sin(np.pi*s/L)**4
        phi2=np.sin(np.pi*s/L)**4*(s/L)
        return phi1,phi2
    def evolve(par):
        A,B=par
        def rhs(s,y):
            sigma,alpha,u,v,H,w,C=y;Q=.5*w*w;K=-3+Q+H*u
            p1,p2=shapes(s);b=-A*p1+B*p2
            return [u,v,6+Q-u*u-H*u,Q-H*v-u*v,-K-H*H,
                    b-.5*(3*u+v)*w,-2*(u+H)*C-w*b]
        return solve_ivp(rhs,(0,L),y0,rtol=1e-10,atol=1e-12,max_step=L/3000)
    # Initialize A using monotone round-cusp scale and small B.
    guess=[.4*delta if L==1 else .03*delta, .05*delta]
    solroot=root(lambda p: [evolve(p).y[5,-1],evolve(p).y[6,-1]],guess,tol=1e-10)
    sol=evolve(solroot.x);s=sol.t;sigma,alpha,u,v,H,w,C=sol.y
    A,B=solroot.x;p1=np.sin(np.pi*s/L)**4;p2=p1*(s/L);b=-A*p1+B*p2
    Q=.5*w*w;K=-3+Q+H*u
    # Direct constraint expression for cross-check.
    up=6+Q-u*u-H*u
    Cdirect=K-up+3-Q-.5*u*u-.5*v*v
    return {'Q0':Q0,'delta':delta,'L':L,'switch_r':rs,
      'root_success':bool(solroot.success),'root_message':solroot.message,
      'A':float(A),'B':float(B),'A_over_delta':float(A/delta),'B_over_delta':float(B/delta),
      'max_abs_b_over_delta':float(np.max(np.abs(b))/delta),
      'w_min':float(w.min()),'w_max':float(w.max()),'w_final':float(w[-1]),
      'C_final_evolved':float(C[-1]),'C_final_direct':float(Cdirect[-1]),
      'max_constraint_crosscheck':float(np.max(np.abs(C-Cdirect))),
      'max_abs_C_over_delta2':float(np.max(np.abs(C))/delta**2),
      'end':{'u':float(u[-1]),'v':float(v[-1]),'H':float(H[-1]),'K':float(K[-1])},
      'sample':[{'s':float(s[i]),'w':float(w[i]),'b':float(b[i]),'C':float(C[i])}
                for i in np.linspace(0,len(s)-1,20,dtype=int)]}

if __name__=='__main__':
  out={'forcing':'b=-A sin^4(pi s/L)+B(s/L)sin^4(pi s/L)','runs':[]}
  for Q0 in [1,10,100]:
    for delta in [.1,.03,.01]:
      for L in [1.0,2.0]:out['runs'].append(run(Q0,delta,L))
  p=Path('workspace/data/step90_two_moment_taper.json');p.parent.mkdir(parents=True,exist_ok=True)
  p.write_text(json.dumps(out,indent=2),encoding='utf-8')
  print(json.dumps([{k:r[k] for k in ['Q0','delta','L','root_success','A_over_delta','B_over_delta','max_abs_b_over_delta','w_min','w_final','C_final_evolved','C_final_direct']} for r in out['runs']],indent=2))
  print(f'\nwrote {p}')

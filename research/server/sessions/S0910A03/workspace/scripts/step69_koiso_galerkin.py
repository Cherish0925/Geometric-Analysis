"""Galerkin pilot for the T^2-invariant Koiso Einstein germ on T^3.

Metric: G=dt^2+exp(2a)dtheta^2+exp(2b)dx^2+exp(2c)dy^2,
with a,b,c periodic in theta.  The exact Gaussian Einstein equations Ric_G=-3G are
  a_tt = Ric_a^a + 3 - H a_t, etc., H=a_t+b_t+c_t.
Initial data are the scalar-minus-six Yamabe metric from
step69_collapsed_koiso_center.py and zero shape operator.

This is an exploratory spectral Galerkin integration of an elliptic Cauchy
problem.  Resolution agreement over a finite time is evidence about this seed,
not a proof of global existence/nonexistence.
"""
from __future__ import annotations
import json
from pathlib import Path
import numpy as np
from scipy.integrate import solve_bvp, solve_ivp

A = 1.0
TWOPI = 2*np.pi


def fp(x): return A*np.cos(x)
def f(x): return A*np.sin(x)


def yamabe_ode(x, y):
    u, up = y
    return np.vstack((up, 0.75*u**5 - 0.25*fp(x)**2*u))


def yamabe_bc(ya, yb):
    return np.array([ya[0]-yb[0], ya[1]-yb[1]])


def yamabe_solution():
    x=np.linspace(0,TWOPI,801)
    u0=(np.mean(fp(x)**2)/3)**0.25
    guess=np.vstack((u0*(1+0.02*np.cos(2*x)),-0.04*u0*np.sin(2*x)))
    sol=solve_bvp(yamabe_ode,yamabe_bc,x,guess,tol=2e-11,max_nodes=40000)
    if not sol.success: raise RuntimeError(sol.message)
    return sol


def project(v, m):
    vh=np.fft.rfft(v)
    if m+1 < len(vh): vh[m+1:]=0
    return np.fft.irfft(vh,n=len(v))


def deriv(v, order=1):
    n=len(v); k=np.fft.rfftfreq(n,1/n)
    vh=np.fft.rfft(v)
    return np.fft.irfft((1j*k)**order*vh,n=n)


def ricci3(a,b,c):
    at=deriv(a); bt=deriv(b); ct=deriv(c)
    bss=np.exp(-2*a)*(deriv(b,2)-at*bt)
    css=np.exp(-2*a)*(deriv(c,2)-at*ct)
    bs=np.exp(-a)*bt; cs=np.exp(-a)*ct
    ra=-(bss+bs**2)-(css+cs**2)
    rb=-(bss+bs**2+bs*cs)
    rc=-(css+cs**2+bs*cs)
    return ra,rb,rc


def constraints(a,b,c,sa,sb,sc):
    ra,rb,rc=ricci3(a,b,c)
    H=sa+sb+sc
    # Gauss/Hamilton constraint for Ric_G=-3G:
    # R(g_t)-H^2+|S|^2+6=0.
    ham=ra+rb+rc-H**2+(sa**2+sb**2+sc**2)+6
    # Orthonormal theta component of div S - dH.
    mom=np.exp(-a)*(-deriv(sb)-deriv(sc)+deriv(b)*(sa-sb)+deriv(c)*(sa-sc))
    return ham,mom,(ra,rb,rc)


def run_mode(sol,m,t_end=0.8):
    n=8*m
    x=np.linspace(0,TWOPI,n,endpoint=False)
    u=sol.sol(x)[0]
    a0=project(2*np.log(u),m)
    b0=project(2*np.log(u)+f(x),m)
    c0=project(2*np.log(u)-f(x),m)
    z=np.zeros(n)
    y0=np.concatenate((a0,b0,c0,z,z,z))

    def rhs(t,y):
        blocks=[project(y[i*n:(i+1)*n],m) for i in range(6)]
        a,b,c,sa,sb,sc=blocks
        ra,rb,rc=ricci3(a,b,c)
        H=sa+sb+sc
        aa=project(ra+3-H*sa,m)
        bb=project(rb+3-H*sb,m)
        cc=project(rc+3-H*sc,m)
        return np.concatenate((sa,sb,sc,aa,bb,cc))

    sample_t=np.linspace(0,t_end,81)
    ivp=solve_ivp(rhs,(0,t_end),y0,method='DOP853',rtol=2e-9,atol=2e-11,
                  t_eval=sample_t,max_step=0.005)
    records=[]
    for j,t in enumerate(ivp.t):
        blocks=[project(ivp.y[i*n:(i+1)*n,j],m) for i in range(6)]
        a,b,c,sa,sb,sc=blocks
        ham,mom,rics=constraints(a,b,c,sa,sb,sc)
        H=sa+sb+sc
        shear2=(sa-H/3)**2+(sb-H/3)**2+(sc-H/3)**2
        records.append({
            't':float(t),'H_min':float(H.min()),'H_max':float(H.max()),
            'S_min':float(min(sa.min(),sb.min(),sc.min())),
            'S_max':float(max(sa.max(),sb.max(),sc.max())),
            'shear_max':float(np.sqrt(shear2).max()),
            'ham_sup':float(np.abs(ham).max()),'mom_cov_sup':float(np.abs(mom).max()),
            'log_metric_min':float(min(a.min(),b.min(),c.min())),
            'log_metric_max':float(max(a.max(),b.max(),c.max())),
            'scalar3_min':float(np.min(sum(rics))),
            'scalar3_max':float(np.max(sum(rics))),
        })
    return {
        'modes':m,'grid':n,'success':bool(ivp.success),'message':ivp.message,
        'nfev':int(ivp.nfev),'last_time':float(ivp.t[-1]),'records':records,
        'final_fields':{
            key:[float(v) for v in project(ivp.y[i*n:(i+1)*n,-1],m)]
            for i,key in enumerate(['a','b','c','sa','sb','sc'])
        }
    }


def main():
    sol=yamabe_solution()
    outputs=[]
    for m in [6,8,10,12]:
        print('running modes',m,flush=True)
        outputs.append(run_mode(sol,m))
        print(' final',outputs[-1]['records'][-1],flush=True)
    # Compare scalar summaries at common sample times.
    comparisons=[]
    for idx,t in enumerate(outputs[0]['records']):
        vals=np.array([[o['records'][idx][k] for k in
                       ['H_min','H_max','S_min','S_max','shear_max']]
                      for o in outputs])
        comparisons.append({'t':t['t'],'max_spread':float(np.ptp(vals,axis=0).max())})
    out={'description':'T2-invariant Koiso Galerkin pilot; not a proof',
         'runs':outputs,'summary_spread':comparisons}
    path=Path(__file__).resolve().parents[1]/'data'/'step69_koiso_galerkin.json'
    path.write_text(json.dumps(out,indent=2),encoding='utf-8')
    print('wrote',path)

if __name__=='__main__': main()

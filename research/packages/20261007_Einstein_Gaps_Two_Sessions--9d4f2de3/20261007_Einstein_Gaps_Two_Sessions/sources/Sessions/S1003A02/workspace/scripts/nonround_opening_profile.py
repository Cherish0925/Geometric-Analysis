"""Locate where the contact-slot anisotropy q is removed on non-round saturation paths.

For scale-free variables X=(x,z,p,chi,eta), q=-3 log z and dq/dtau=eta.
The physical mean scale obeys d log r/dtau=p.  Its absolute normalization is
fixed by the exact-CH terminal state, r(T)=sinh(t_ch) cosh(t_ch)^(1/3), so
W=r^3.  This script records where q descends from its post-entry maximum to
zero, and how the D-action int Dbar^2/8 dtau is distributed in W and q.
It is descriptive numerical evidence, not a lower-bound certificate.
"""
from __future__ import annotations
import json, math, sys
from pathlib import Path
import numpy as np

OUT = Path(__file__).resolve().parents[1]/"data"/"saturation_control"/"nonround_opening_profile.json"


def cumtrap(y, h):
    y=np.asarray(y,float)
    return np.concatenate([[0.0], np.cumsum(h*(y[:-1]+y[1:])/2)])


def crossing_desc(q, start, target):
    """First index at/after start with q<=target."""
    jj=np.nonzero(q[start:]<=target)[0]
    return int(start+jj[0]) if len(jj) else len(q)-1


def analyse(path):
    R=json.loads(Path(path).read_text())
    X=np.asarray(R['X'],float); U=np.asarray(R['U'],float)
    n=R['N']; h=R['T']/n; tau=np.linspace(0,R['T'],n+1)
    x,z,p,chi,eta=X.T
    q=-3*np.log(z)
    # Reconstruct mean radius backward from the exact CH terminal scale.
    tch=R['t_ch']; rT=math.sinh(tch)*math.cosh(tch)**(1/3)
    I=cumtrap(p,h)
    logr=math.log(rT)-(I[-1]-I)
    W=np.exp(3*logr)
    Lh=3*U[:,0]**2/16; Le=U[:,1]**2/6; Ld=U[:,2]**2/8
    cH,cE,cD=cumtrap(Lh,h),cumtrap(Le,h),cumtrap(Ld,h)
    iq=int(np.argmax(q)); qmax=float(q[iq])
    rows=[]
    # Fractions of the required descent qmax -> 0 completed.
    for frac in (0.1,0.25,0.5,0.75,0.9,0.99):
        target=(1-frac)*qmax
        j=crossing_desc(q,iq,target)
        rows.append({'fraction_of_q_descent':frac,'index':j,'tau':float(tau[j]),
                     'q':float(q[j]),'W':float(W[j]),'r':float(np.exp(logr[j])),
                     'bplus':float(R['bplus'][j]),'cum_D_from_start':float(cD[j]),
                     'D_cost_since_qmax':float(cD[j]-cD[iq]),
                     'total_cost_since_qmax':float((cH+cE+cD)[j]-(cH+cE+cD)[iq])})
    # Distribution of D action over volume decades and before/after q maximum.
    totD=float(cD[-1]); bins=[]
    edges=[0,1,10,100,1000,1e4,1e6,float('inf')]
    segD=h*(Ld[:-1]+Ld[1:])/2; Wmid=np.sqrt(W[:-1]*W[1:])
    for lo,hi in zip(edges[:-1],edges[1:]):
        val=float(segD[(Wmid>=lo)&(Wmid<hi)].sum())
        bins.append({'W_range':[lo,hi],'D_cost':val,'fraction_D':val/totD if totD else 0})
    # D action by q-descent quartile.
    qbins=[]
    for f0,f1 in zip((0,.25,.5,.75),(.25,.5,.75,1.0)):
        j0=crossing_desc(q,iq,(1-f0)*qmax); j1=crossing_desc(q,iq,(1-f1)*qmax)
        qbins.append({'descent_fraction_range':[f0,f1], 'indices':[j0,j1],
                      'D_cost':float(cD[j1]-cD[j0]),
                      'W_range':[float(W[j0]),float(W[j1])]})
    return {'file':Path(path).name,'cost':R['cost'],'t_ch':tch,'T':R['T'],
            'q_initial':float(q[0]),'q_max':qmax,'qmax_index':iq,
            'qmax_tau':float(tau[iq]),'qmax_W':float(W[iq]),
            'W_initial':float(W[0]),'W_terminal':float(W[-1]),
            'channel_cost_trapezoid':{'H':float(cH[-1]),'E':float(cE[-1]),'D':totD,
                                      'total':float(cH[-1]+cE[-1]+cD[-1])},
            'q_descent_rows':rows,'D_by_W':bins,'D_by_q_descent_quartile':qbins}


def main(paths):
    out=[analyse(p) for p in paths]
    OUT.write_text(json.dumps(out,indent=1)+'\n')
    for r in out:
        print(r['file'], 'qmax',r['q_max'],'at W',r['qmax_W'],'D',r['channel_cost_trapezoid']['D'])
        for x in r['q_descent_rows']:
            if x['fraction_of_q_descent'] in (.25,.5,.75,.99):
                print(' ',x)
        print(' D/W',[(b['W_range'],round(b['D_cost'],4)) for b in r['D_by_W']])

if __name__=='__main__':
    main(sys.argv[1:])

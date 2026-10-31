"""Calibrated (ASD scalar-flat) flow of the scale-free diagonal Bianchi-IX system.

The control-optimal field c*(X) realizing sup_c(db_+/dtau - L) = 0 (Step 34) defines
the calibrated vector field f_cal(X) = f(X, c*(X)).  Along it L = db_+/dtau, i.e. the
cost of a calibrated segment is exactly Delta b_+; and every path satisfies
   Phat = Delta b_+ + int L(c - c*) dtau,  L quadratic with weights (3/16,1/6,1/8).

Test (endpoint separation): integrate f_cal BACKWARD from exact CH first jets ch(tau)
and FORWARD from the Lambda-Taub-NUT collapsed entry ray, and record where the leaves go
(z -> 0 collapse, b_+ limit, blow-up).  A backward leaf from ch(tau), tau in (0.70,0.758),
ending on the collapsed Berger set b_+ -> -2 would be a connector of cost 4-9 sinh^4 tau < 1.

Also checks: c*(X) on exact CH (should NOT vanish; CH is not calibrated) and the identity
L(c*) = db_+/dtau(c*).
Output: workspace/data/saturation_control/calibrated_flow_leaves.json
"""
import json, math
from pathlib import Path
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp

OUT = Path(__file__).resolve().parents[1]/'data'/'saturation_control'/'calibrated_flow_leaves.json'

x,z,p,chi,eta=sp.symbols('x z p chi eta', real=True)
H,E,D=sp.symbols('H E D', real=True)
ex=sp.exp(x/3)
af=ex**2/z; ag=1/(ex*z); ah=z**2/ex
vf=p+sp.Rational(2,3)*chi+sp.Rational(1,3)*eta
vg=p-sp.Rational(1,3)*chi+sp.Rational(1,3)*eta
vh=p-sp.Rational(1,3)*chi-sp.Rational(2,3)*eta
gf=(ag**2+ah**2-af**2)/(ag*ah); gg=(ah**2+af**2-ag**2)/(ah*af); gh=(af**2+ag**2-ah**2)/(af*ag)
uf,ug,uh=af*vf-gf,ag*vg-gg,ah*vh-gh
bp=2-uf**2-ug**2-uh**2-uf*ug*uh
wf,wg,wh=af*vf+gf,ag*vg+gg,ah*vh+gh
bm=wf**2+wg**2+wh**2-wf*wg*wh-2
em4=sp.exp(-4*x/3); ep2=sp.exp(2*x/3); ep8=sp.exp(8*x/3)
VD=4*z**-4*(em4-ep2)+4*(ep2*z**2-em4*z**8)
Vx=4*z**-4*(ep8-em4)+4*z**2*(em4-ep2)
VH=sp.Rational(2,3)*z**-4*(ep8-2*ep2+em4)-sp.Rational(4,3)*z**2*(ep2+em4)+sp.Rational(2,3)*em4*z**8
xi=chi+eta/2
V=[x,z,p,chi,eta]
f=[chi,-eta*z/3,p**2-xi**2/3-eta**2/4+VH/2-H/2,-2*p*chi+Vx-E+D/2,-2*p*eta+VD-D]
g=[sp.diff(bp,v) for v in V]
Hs=-sp.Rational(4,3)*g[2]; Es=-3*g[3]; Ds=2*g[3]-4*g[4]
fcal=[fi.subs({H:Hs,E:Es,D:Ds}) for fi in f]
Lcal=3*Hs**2/16+Es**2/6+Ds**2/8
bdot=sum(gi*fi for gi,fi in zip(g,fcal))
F=sp.lambdify(V,fcal,'numpy'); BP=sp.lambdify(V,bp,'numpy'); BM=sp.lambdify(V,bm,'numpy')
CST=sp.lambdify(V,[Hs,Es,Ds],'numpy'); LC=sp.lambdify(V,Lcal,'numpy'); BD=sp.lambdify(V,bdot,'numpy')

def ch_np(t):
    s,c=math.sinh(t),math.cosh(t); r=s*c**(1/3)
    return np.array([math.log(c),1.0,r*(c/s+math.tanh(t)/3),r*math.tanh(t),0.0])
def entry_np(eps,A):
    zz=eps**(1/3); U=math.sqrt(1+2*A*A); W=2*A*A/U
    return np.array([0.0,zz,zz*(2*U+W)/3,0.0,zz*(U-W)])

def run(X0,sign,Tmax=60.0):
    def rhs(t,X): return sign*np.array(F(*X),dtype=float)
    def ev_small(t,X): return X[1]-1e-4
    ev_small.terminal=True
    def ev_big(t,X): return 50-np.max(np.abs(X))
    ev_big.terminal=True
    def ev_zneg(t,X): return X[1]-1e-12
    ev_zneg.terminal=True
    sol=solve_ivp(rhs,(0,Tmax),X0,rtol=1e-10,atol=1e-12,events=[ev_small,ev_big],max_step=0.05,dense_output=False)
    Xs=sol.y.T
    bps=np.array([BP(*X) for X in Xs]); bms=np.array([BM(*X) for X in Xs])
    q=-3*np.log(np.abs(Xs[:,1]))
    idx=np.unique(np.linspace(0,len(Xs)-1,25).astype(int))
    return {'status':int(sol.status),'msg':sol.message,'tau_end':float(sol.t[-1]),
            'end_state':Xs[-1].tolist(),'bplus_start':float(bps[0]),'bplus_end':float(bps[-1]),
            'bplus_min':float(bps.min()),'bplus_max':float(bps.max()),
            'bminus_start':float(bms[0]),'bminus_end':float(bms[-1]),
            'q_end':float(q[-1]),'z_min':float(Xs[:,1].min()),
            'profile':[{'tau':float(sol.t[i]),'X':Xs[i].tolist(),'bplus':float(bps[i]),'bminus':float(bms[i])} for i in idx]}

def main():
    out={'identity_check':[], 'CH_controls':[], 'backward_from_CH':[], 'forward_from_entry':[]}
    rng=np.random.default_rng(1)
    for _ in range(5):
        X=np.array([rng.normal()*.5,abs(rng.normal())*.5+.3,rng.normal(),rng.normal(),rng.normal()])
        out['identity_check'].append({'L_cal':float(LC(*X)),'bdot_cal':float(BD(*X))})
    for t in [0.3,0.7,0.73,0.758,1.0,2.0]:
        X=ch_np(t); out['CH_controls'].append({'tau':t,'cstar':[float(v) for v in CST(*X)],'bplus':float(BP(*X)),'bminus':float(BM(*X)),
                                                 'bplus_exact':2-9*math.sinh(t)**4})
    for t in [0.5,0.70,0.72,0.74,0.758,0.8,1.0,1.5,2.3]:
        r=run(ch_np(t),-1.0); r['tau_CH']=t; r['cost_if_connected_to_minus2']=(2-9*math.sinh(t)**4)+2
        out['backward_from_CH'].append(r)
        print('back',t,r['msg'][:30],'tau_end',round(r['tau_end'],3),'b+ end',round(r['bplus_end'],4),'zmin',round(r['z_min'],5),'q_end',round(r['q_end'],3))
    for eps in [1/16,1/64]:
        for A in [0.5,1.0,2.0]:
            r=run(entry_np(eps,A),1.0); r['eps']=eps; r['A']=A
            out['forward_from_entry'].append(r)
            print('fwd',eps,A,r['msg'][:30],'tau_end',round(r['tau_end'],3),'b+',round(r['bplus_start'],4),'->',round(r['bplus_end'],4),'q_end',round(r['q_end'],3),'end',np.round(r['end_state'],3))
    OUT.write_text(json.dumps(out,indent=1)+'\n')
    print(json.dumps({k:out[k] for k in ['identity_check','CH_controls']},indent=1))

if __name__=='__main__': main()

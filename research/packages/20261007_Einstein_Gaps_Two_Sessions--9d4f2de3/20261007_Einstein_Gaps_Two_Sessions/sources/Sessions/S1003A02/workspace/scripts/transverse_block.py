"""Transverse (g<->h antisymmetric) linearization of the calibrated flow on the biaxial set.

Sigma = {q=0, eta=0} (z=1) is invariant under the full controlled system with D=0 and
under the calibrated flow (g<->h symmetry: q->-q, eta->-eta).  CH jets lie in Sigma; the
collapsed Taub-NUT entry has q ~ log(1/eps) and lies outside.  At points of Sigma the
Jacobian of f_cal splits into symmetric (x,p,chi) and antisymmetric (q,eta) blocks.

This script computes the 2x2 antisymmetric block A(X) of f_cal in (q,eta), together with
its eigenvalues, along (i) exact CH jets ch(tau), (ii) the calibrated backward leaves from
CH jets, (iii) the round point and Burns-like region.  Control enters the antisymmetric
block only through D (eta' = ... - D), with cost (D-D*)^2/8.

Linear-quadratic consequence used in the note: along a base path in Sigma with transition
matrix Phi of A, steering a transverse deviation d0=(q0,eta0) at tau0 to 0 at tau1 costs at
least d0^T G(tau0,tau1)^{-1} d0 (to first order), where
G = int_{tau0}^{tau1} Phi(tau0,s) b b^T Phi(tau0,s)^T * 2 ds,  b=(0,-1)
(1/(2*(1/8)) = 2 weight from L=(dD)^2/8 minus the exact cross term vanishing at c*).
Output: workspace/data/saturation_control/transverse_block.json
"""
import json, math
from pathlib import Path
import numpy as np
import sympy as sp

OUT=Path(__file__).resolve().parents[1]/'data'/'saturation_control'/'transverse_block.json'
x,q,p,chi,eta=sp.symbols('x q p chi eta', real=True)
z=sp.exp(-q/3)
ex=sp.exp(x/3)
af=ex**2/z; ag=1/(ex*z); ah=z**2/ex
vf=p+sp.Rational(2,3)*chi+sp.Rational(1,3)*eta
vg=p-sp.Rational(1,3)*chi+sp.Rational(1,3)*eta
vh=p-sp.Rational(1,3)*chi-sp.Rational(2,3)*eta
gf=(ag**2+ah**2-af**2)/(ag*ah); gg=(ah**2+af**2-ag**2)/(ah*af); gh=(af**2+ag**2-ah**2)/(af*ag)
uf,ug,uh=af*vf-gf,ag*vg-gg,ah*vh-gh
bp=2-uf**2-ug**2-uh**2-uf*ug*uh
em4=sp.exp(-4*x/3); ep2=sp.exp(2*x/3); ep8=sp.exp(8*x/3)
VD=4*z**-4*(em4-ep2)+4*(ep2*z**2-em4*z**8)
Vx=4*z**-4*(ep8-em4)+4*z**2*(em4-ep2)
VH=sp.Rational(2,3)*z**-4*(ep8-2*ep2+em4)-sp.Rational(4,3)*z**2*(ep2+em4)+sp.Rational(2,3)*em4*z**8
xi=chi+eta/2
# state (x,q,p,chi,eta); q'=eta since z'=-eta z/3
bx,bq,bpp,bc,be=[sp.diff(bp,v) for v in (x,q,p,chi,eta)]
Hs=-sp.Rational(4,3)*bpp; Es=-3*bc; Ds=2*bc-4*be
fq=eta
fe=-2*p*eta+VD-Ds
J=sp.Matrix([[sp.diff(fq,q),sp.diff(fq,eta)],[sp.diff(fe,q),sp.diff(fe,eta)]])
Jsig=J.subs({q:0,eta:0})
Jsig=sp.simplify(Jsig)
Dsig=sp.simplify(Ds.subs({q:0,eta:0}))
Jf=sp.lambdify((x,p,chi),Jsig,'numpy')
print('D* on Sigma =',Dsig)
print('A on Sigma =',Jsig)

def ch(t):
    s,c=math.sinh(t),math.cosh(t); r=s*c**(1/3)
    return math.log(c), r*(c/s+math.tanh(t)/3), r*math.tanh(t)

rows=[]
for t in [0.2,0.4,0.6,0.7,0.758,0.9,1.2,1.6,2.3]:
    X=ch(t); A=np.array(Jf(*X),dtype=float); ev=np.linalg.eigvals(A)
    rows.append({'tau_CH':t,'x':X[0],'p':X[1],'chi':X[2],'A':A.tolist(),'eig':[complex(e).real for e in ev],'eig_im':[complex(e).imag for e in ev]})
A0=np.array(Jf(0.0,1.0,0.0),dtype=float)
out={'D_star_on_Sigma':str(Dsig),'A_on_Sigma':str(Jsig),'CH':rows,
     'round_point':{'A':A0.tolist(),'eig':[complex(e).real for e in np.linalg.eigvals(A0)],'eig_im':[complex(e).imag for e in np.linalg.eigvals(A0)]}}
OUT.write_text(json.dumps(out,indent=1)+'\n')
for r in rows: print(r['tau_CH'],np.round(r['A'],4).tolist(),np.round(r['eig'],4),np.round(r['eig_im'],4))
print('round',out['round_point'])

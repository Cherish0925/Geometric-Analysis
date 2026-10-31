"""Exact chiral charge at a controlled anisotropic Berger/F-structure end.

Regular scale-free variables are (x,z,p,chi,eta), with the collapsing h-circle
satisfying a_h/a_g=z^3 and a_f/a_g=e^x.  Finite orbit curvature requires
x=X z^3; finite first jets require p=Pz, chi=Cz, eta=Nz.  This script computes
the z->0 limit of b_+ and identifies its excess over the biaxial value -2.
"""
import json
from pathlib import Path
import sympy as sp
z,X,P,C,N=sp.symbols('z X P C N', real=True)
x=X*z**3; p=P*z; chi=C*z; eta=N*z
q=-3*sp.log(z); beta=x+q/2; xi=chi+eta/2
af=sp.exp(2*beta/3); ag=sp.exp(-beta/3+q/2); ah=sp.exp(-beta/3-q/2)
pf=af*(p+2*xi/3); pg=ag*(p-xi/3+eta/2); ph=ah*(p-xi/3-eta/2)
gf=(ag**2+ah**2-af**2)/(ag*ah)
gg=(ah**2+af**2-ag**2)/(ah*af)
gh=(af**2+ag**2-ah**2)/(af*ag)
u=[sp.simplify(pf-gf),sp.simplify(pg-gg),sp.simplify(ph-gh)]
ul=[sp.simplify(sp.limit(v,z,0,dir='+')) for v in u]
bp=sp.simplify(2-sum(v*v for v in ul)-sp.prod(ul))
# The opposite chirality uses w_i=p_i+gamma_i and
# b_-=sum w_i^2-w1*w2*w3-2 in the Step-27 normalization.
wl=[sp.simplify(sp.limit(v,z,0,dir='+')) for v in [pf+gf,pg+gg,ph+gh]]
bm=sp.simplify(sum(v*v for v in wl)-sp.prod(wl)-2)
ex=sp.factor(bp+2)
out={'u_limit':[str(v) for v in ul],'w_limit':[str(v) for v in wl],
     'bplus_limit':str(sp.factor(bp)),'bminus_limit':str(sp.factor(bm)),
     'bplus_plus_2':str(ex),
     'scope':'finite-charge normalized first-jet family x=X z^3, p=Pz, chi=Cz, eta=Nz; not by itself a bounded-curvature collar'}
print(json.dumps(out,indent=1))
(Path(__file__).resolve().parents[1]/'data'/'collapse_chiral_charge_limit.json').write_text(json.dumps(out,indent=1)+'\n')

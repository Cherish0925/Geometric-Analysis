"""Exact symbolic reduction of the b_+ Hamilton--Jacobi calibration.

Derives the control-minimized Hamiltonian for V=b_+ and the characteristic
coefficient K entering V=b_++phi(q,eta) in the scale-free system.
"""
import json
from pathlib import Path
import sympy as sp

x,z,p,chi,eta=sp.symbols('x z p chi eta', positive=True, real=True)
H,E,D=sp.symbols('H E D', real=True)
ex=sp.exp(x/3)
af=ex**2/z
ag=1/(ex*z)
ah=z**2/ex
vf=p+sp.Rational(2,3)*chi+sp.Rational(1,3)*eta
vg=p-sp.Rational(1,3)*chi+sp.Rational(1,3)*eta
vh=p-sp.Rational(1,3)*chi-sp.Rational(2,3)*eta
pf,pg,ph=af*vf,ag*vg,ah*vh
gf=(ag**2+ah**2-af**2)/(ag*ah)
gg=(ah**2+af**2-ag**2)/(ah*af)
gh=(af**2+ag**2-ah**2)/(af*ag)
uf,ug,uh=pf-gf,pg-gg,ph-gh
b=sp.expand(2-uf**2-ug**2-uh**2-uf*ug*uh)

em4=sp.exp(-4*x/3); ep2=sp.exp(2*x/3); ep8=sp.exp(8*x/3)
VD=4*z**-4*(em4-ep2)+4*(ep2*z**2-em4*z**8)
Vx=4*z**-4*(ep8-em4)+4*z**2*(em4-ep2)
VH=sp.Rational(2,3)*z**-4*(ep8-2*ep2+em4)-sp.Rational(4,3)*z**2*(ep2+em4)+sp.Rational(2,3)*em4*z**8
xi=chi+eta/2
f0=[chi,-eta*z/3,p**2-xi**2/3-eta**2/4+VH/2,-2*p*chi+Vx,-2*p*eta+VD]
vars=[x,z,p,chi,eta]
g=[sp.diff(b,v) for v in vars]
# q=-3log z, but b derivative is in z; phi contribution later uses q'=eta.
bdot0=sp.expand(sum(gi*fi for gi,fi in zip(g,f0)))
bp,bc,be=g[2],g[3],g[4]
H0=bdot0+bp**2/sp.Integer(3)+sp.Rational(3,2)*bc**2+2*(bc/2-be)**2
m=sp.factor(sp.trigsimp(sp.simplify(H0)))
K=sp.factor(sp.trigsimp(sp.simplify(f0[4]-2*bc+4*be)))
controls={
 'Hstar':sp.factor(-sp.Rational(4,3)*bp),
 'Estar':sp.factor(-3*bc),
 'Dstar':sp.factor(2*bc-4*be),
}
out={
 'H0_sup_dbminusL':str(m),
 'm_minus_H0':str(-m),
 'K':str(K),
 'controls':{k:str(v) for k,v in controls.items()},
 'bplus':str(sp.factor(b)),
}
path=Path(__file__).resolve().parents[1]/'data'/'saturation_control'/'hj_symbolic_reduction.json'
path.write_text(json.dumps(out,indent=1)+'\n')
print(json.dumps(out,indent=1))

"""Chiral charge and beta-pinning mismatch on a CH-shaped orbit with arbitrary first jet."""
import json
from pathlib import Path
import sympy as sp
s,c,m,v=sp.symbols('s c m v', positive=True, real=True)
# Geometry: af=s c, ag=ah=s. First jet: yf=m+2v/3, yg=yh=m-v/3,
# so v=yf-(yg+yh)/2 and m=(yf+yg+yh)/3.
a,b,d=s*c,s,s
yf=m+2*v/3; yg=m-v/3; yh=yg
pf=a*yf; pg=b*yg; ph=d*yh
gf=(b*b+d*d-a*a)/(b*d); gg=(d*d+a*a-b*b)/(d*a); gh=(a*a+b*b-d*d)/(a*b)
u=[sp.factor(pf-gf),sp.factor(pg-gg),sp.factor(ph-gh)]
bp=sp.factor(2-sum(x*x for x in u)-sp.prod(u))
# c^2-s^2=1. Reduce c^2 to 1+s^2 where possible.
bp_red=sp.factor(bp.subs(c**2,1+s**2))
B=sp.factor((v-s/c)/4)
out={'u':[str(x) for x in u],'bplus':str(bp),'bplus_c2_1ps2':str(bp_red),
     'Btilde':str(B),'CH_velocity':{'m':'(c/s+1/c*s? mean of coth+tanh)','v':'tanh=t=s/c'}}
print(json.dumps(out,indent=1))
(Path(__file__).resolve().parents[1]/'data'/'ch_orbit_beta_charge.json').write_text(json.dumps(out,indent=1)+'\n')

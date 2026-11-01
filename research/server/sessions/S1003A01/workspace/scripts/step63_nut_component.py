"""Factor/saturate the exact nut constraints using Singular.
Writes a Singular input for L1..L5 with R3=1-R1-R2 and analyzes components
away from boundary weights R1 R2 R3 and away from isotropy discriminant.
"""
import json, sympy as sp, os
here=os.path.dirname(__file__)
D=json.load(open(os.path.join(here,'../data/step63/bix_nut_series_order5.json')))
d1,d2,R1,R2,R3=sp.symbols('d1 d2 R1 R2 R3')
loc={str(x):x for x in [d1,d2,R1,R2,R3]}
L=[]
for x in D['length_conditions']:
    e=sp.sympify(x,locals=loc).subs(R3,1-R1-R2)
    L.append(sp.factor(sp.together(e).as_numer_denom()[0]))
# tracefree anisotropy entries d1,d2,d3; discriminant
Dscr=(d1-d2)*(2*d1+d2)*(d1+2*d2)
prod=R1*R2*(1-R1-R2)*Dscr
S=lambda e:str(sp.expand(e)).replace('**','^')
lines=['LIB "primdec.lib";','option(redSB);','ring r=0,(R1,R2,d1,d2,z),dp;']
lines.append('ideal I='+','.join(S(e) for e in L)+';')
# Rabinowitsch localization: 1-z*prod=0 is equivalent to saturation away from prod.
lines.append('ideal J=I,1-z*('+S(prod)+');')
lines += ['ideal G=std(J);','print("dim interior="); print(dim(G));','print("vdim interior="); print(vdim(G));',
          'print("interior std="); print(G);','print("minAss interior="); print(minAssGTZ(G));']
# Full ideal components too
lines += ['ideal GI=std(I);','print("dim full="); print(dim(GI));','print("minAss full="); print(minAssGTZ(GI));']
path=os.path.join(here,'../data/step63/bix_nut_component.sing')
open(path,'w').write('\n'.join(lines)+'\n')
print(path)

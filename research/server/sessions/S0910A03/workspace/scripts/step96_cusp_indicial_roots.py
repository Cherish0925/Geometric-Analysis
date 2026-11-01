"""Indicial-root calculation for the all-block matching operator at a round cusp.

Background quotient fields, y->0:
  gamma=y^-2(dy^2+ds^2), phi=-log y, sigma=-2log y,
  U=constant, q_charge=0.
For s-zero indicial variations (dot phi,dot sigma,dot U)~y^lambda, derive
trace-H, T, traceless-H and orbit Z polynomials. Charge is a first-order block
whose invariant norm carries a y^3 redshift relative to the b-derivative.
"""
import sympy as sp
from pathlib import Path
import json

la=sp.symbols('lambda', real=True)
# Linearized T=L sigma-6: -12 phi + lambda(lambda-5)sigma.
Tphi=-12
Tsig=la*(la-5)
# Linearized trace H=R-Delta sigma-|d sigma|^2/2+6.
Hphi=-2*la*(la-1)+12
Hsig=-la*(la-1)+2*la
M=sp.Matrix([[Hphi,Hsig],[Tphi,Tsig]])
det_trace=sp.factor(M.det())
# H_yy-H_ss = -sigma''+2phi' sigma'-sigma'^2/2;
# after linearization and removal of y^(lambda-2): -lambda[(lambda-1)sigma+4phi].
TFphi=-4*la
TFsig=-la*(la-1)
# orbit equation tau_sigma U: lambda(lambda-3) per target component.
Zpoly=sp.factor(la*(la-3))

roots=[]
for root in [-1,0,3,4]:
    null=M.subs(la,root).nullspace()
    vec=[sp.simplify(x) for x in null[0]] if null else []
    tf=sp.simplify(TFphi.subs(la,root)*vec[0]+TFsig.subs(la,root)*vec[1]) if vec else None
    roots.append({'lambda':root,'trace_T_null_vector_phi_sigma':[str(x) for x in vec],
                  'traceless_H_residual_on_vector':str(tf),'survives_full_H':bool(tf==0)})

out={
 'background':{'gamma':'y^-2(dy^2+ds^2)','phi':'-log y','sigma':'-2 log y','U':'constant','charge':'0'},
 'trace_H_row':[str(Hphi),str(Hsig)],
 'T_row':[str(Tphi),str(Tsig)],
 'trace_scalar_determinant':str(det_trace),
 'trace_scalar_roots':[-1,0,3,4],
 'traceless_H_row':[str(TFphi),str(TFsig)],
 'scalar_root_checks':roots,
 'full_scalar_roots':[-1,0,3],
 'orbit_Z_polynomial':str(Zpoly),
 'orbit_roots':[0,3],
 'charge_block':{
   'equation':'Bmix=e^(-3sigma/2) M^(-1/2) dq',
   'b_form':'|Bmix| ~ y^3 |(y d_y, y d_s) q|',
   'indicial_kernel':'lambda=0 constant coordinate charge',
   'redshift':'q~y^lambda produces |Bmix|~y^(lambda+3); horizontal Q is quadratic and ~y^(2lambda+6) near q=0'
 },
 'interpretation':(
   'The growing scalar root -1 is excluded by AH weights; lambda=0 gives boundary/scale data; '
   'lambda=3 gives normalizable scalar and orbit modes. The trace-only lambda=4 mode violates '
   'traceless H and is not a full solution. Constant charge is a genuine linear end mode whose '
   'mixed Ricci cost is redshifted by three b-powers, explaining a potential escaping near-kernel.'
 )
}
path=Path('workspace/data/step96_cusp_indicial_roots.json');path.write_text(json.dumps(out,indent=2))
print(json.dumps(out,indent=2))

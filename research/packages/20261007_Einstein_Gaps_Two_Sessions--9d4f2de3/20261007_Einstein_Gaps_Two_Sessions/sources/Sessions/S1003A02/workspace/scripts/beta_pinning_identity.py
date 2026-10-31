"""Exact fibre/base (beta) pinning identity for diagonal Bianchi-IX metrics.

Compact variables follow ach_projected.py, with fibre f and contact slots g,h:
  kappa=a_f/(a_g a_h), zeta=1/(a_g a_h), q=log(a_g/a_h),
  v=y_f-(y_g+y_h)/2 = beta', beta=log(kappa/sqrt(zeta)).
Let E=Ric_ff-(Ric_gg+Ric_hh)/2.  The CH-radial mismatch
  B~=log(kappa/sqrt(1+zeta)) + (v-kappa^{-1})/4
vanishes on every exact CH orbit.  This script derives
  B~' = F_beta - E/4
and examines F_beta near the ACH equilibrium curve.
"""
import json
from pathlib import Path
import sympy as sp

yf,yg,yh,k,q,z=sp.symbols('yf yg yh k q z', positive=True, real=True)
ef,eg,eh=sp.symbols('ef eg eh', real=True)
S=yf+yg+yh
Pf=2*k**2-8*z**2*sp.sinh(q)**2/k**2
Pg=-2*k**2+4*z*sp.exp(-q)+4*z**2*sp.sinh(2*q)/k**2
Ph=-2*k**2+4*z*sp.exp(q)-4*z**2*sp.sinh(2*q)/k**2
F=sp.Matrix([6-yf*S+Pf-ef,6-yg*S+Pg-eg,6-yh*S+Ph-eh,
             k*(yf-yg-yh),yg-yh,-z*(yg+yh)])
X=sp.Matrix([yf,yg,yh,k,q,z])
v=yf-(yg+yh)/2
B=sp.log(k/sp.sqrt(1+z))+(v-1/k)/4
dB=sp.simplify(sum(sp.diff(B,X[i])*F[i] for i in range(6)))
dB0=sp.simplify(dB.subs({ef:0,eg:0,eh:0}))
ctrl=sp.simplify(dB-dB0)
E=ef-(eg+eh)/2
# ACH block coordinates from ach_block_verify.py.
ub,s1b,s2b,ab=sp.symbols('ub s1b s2b ab', real=True)
u,s1,s2,ah=z*ub,z*s1b,z*s2b,z*ab
ch,sh=sp.cosh(q),sp.sinh(q)
rhs=sp.Matrix([u+2*ch*z,s1-2*ch*z,s2+4*ch*z])
A=sp.Matrix([[1,-1,6],[1,-1,-2],[2,3,2]])
dyf,ds,dk=[sp.expand(w) for w in A.LUsolve(rhs)]
a=ah-4*sh*z
block_sub={yf:2+dyf,yg:1+(ds+a)/2,yh:1+(ds-a)/2,k:1+dk}
Fb=sp.factor(sp.together(dB0.subs(block_sub)))
# Taylor coefficients in z for bounded ACH block variables.  trigsimp exposes
# cancellations hidden by the rational form of the full expression.
Fb0=sp.trigsimp(sp.simplify(Fb.subs(z,0)))
Fb1=sp.trigsimp(sp.simplify(sp.diff(Fb,z).subs(z,0)))
Fb2=sp.trigsimp(sp.simplify(sp.diff(Fb,z,2).subs(z,0)/2))
# Exact CH: k=coth(t), z=csch(t)^2, q=0 and corresponding y.
t=sp.symbols('t', positive=True)
ch_sub={yf:sp.coth(t)+sp.tanh(t),yg:sp.coth(t),yh:sp.coth(t),
        k:sp.coth(t),q:0,z:sp.csch(t)**2}
out={
 'B':str(B),
 'control_part':str(ctrl),
 'control_check':str(sp.simplify(ctrl+E/4)),
 'free_drift':str(sp.factor(dB0)),
 'free_on_CH':str(sp.simplify(dB0.subs(ch_sub))),
 'B_on_CH':str(sp.simplify(B.subs(ch_sub))),
 'block_coefficients_z0_z1_z2':[str(Fb0),str(Fb1),str(Fb2)],
}
print(json.dumps(out,indent=1))
(Path(__file__).resolve().parents[1]/'data'/'beta_pinning_identity.json').write_text(json.dumps(out,indent=1)+'\n')

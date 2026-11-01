#!/usr/bin/env python3
"""Symbolically verify the invariant base equation and physical cusp weights.

For g = gamma_B + e^sigma M on a 2D base, det M=1 and the H^2 metric
normalization <V,W>=1/2 tr(M^-1 V M^-1 W), verify in the diagonal Gaussian
case that
 E_B = Ric(gamma_B)-Hess sigma - 1/2 d sigma^2 - 1/2 U*h +3 gamma_B
matches the direct Ricci formulas.  Also check the physical-coordinate orbit
source weight rho dvol(gamma_B)=e^{3r} dr dz on the round cusp.
"""
import json
from pathlib import Path
import sympy as sp
r,z=sp.symbols('r z', real=True)
a=sp.Function('a')(r,z); s=sp.Function('s')(r,z); v=sp.Function('v')(r,z)
D=sp.diff
ar,az=D(a,r),D(a,z); sr,sz=D(s,r),D(s,z); vr,vz=D(v,r),D(v,z)
arr,azz=D(a,r,2),D(a,z,2); srr,szz=D(s,r,2),D(s,z,2)
# gamma=dr^2+e^{2a}dz^2. Ric endomorphism eigenvalues both K=-e^{-a}(e^a)_{rr}.
K=-(arr+ar**2)
# Hess sigma in orthonormal frame (e_r,e_z=e^-a partial_z).
hrr=srr
hrz=sp.exp(-a)*(D(s,r,z)-ar*sz)
hzz=sp.exp(-2*a)*(szz+sp.exp(2*a)*ar*sr-az*sz)
# diagonal H^2 map coordinate v has pullback dv tensor dv.
EBrr=sp.expand(K-hrr-sp.Rational(1,2)*sr**2-sp.Rational(1,2)*vr**2+3)
EBrz=sp.expand(-hrz-sp.Rational(1,2)*sp.exp(-a)*sr*sz-sp.Rational(1,2)*sp.exp(-a)*vr*vz)
EBzz=sp.expand(K-hzz-sp.Rational(1,2)*sp.exp(-2*a)*sz**2-sp.Rational(1,2)*sp.exp(-2*a)*vz**2+3)
# Direct Gaussian formulas after b=(s+v)/2,c=(s-v)/2.
b=(s+v)/2;c=(s-v)/2
br,cr=D(b,r),D(c,r); brr,crr=D(b,r,2),D(c,r,2)
bz,cz=D(b,z),D(c,z); bzz,czz=D(b,z,2),D(c,z,2); brz,crz=D(b,r,z),D(c,r,z)
E0=3-ar**2-arr-br**2-brr-cr**2-crr
E1=sp.exp(-a)*(ar*bz+ar*cz-br*bz-cr*cz-brz-crz)
E2=3-ar**2-ar*br-ar*cr-arr+sp.exp(-2*a)*(az*bz+az*cz-bz**2-bzz-cz**2-czz)
checks={
 'E_rr_base_identity_minus_direct':sp.simplify(EBrr-E0),
 'E_rz_base_identity_minus_direct':sp.simplify(EBrz-E1),
 'E_zz_base_identity_minus_direct':sp.simplify(EBzz-E2),
}
# Frozen physical cusp a=r, sigma=2r+const.
frozen={
 'EB_rr':sp.simplify(EBrr.subs({a:r,s:2*r,D(a,r):1,D(a,r,2):0,D(a,z):0,D(s,r):2,D(s,r,2):0,D(s,z):0,D(s,z,2):0,D(s,r,z):0})),
 'EB_rz':sp.simplify(EBrz.subs({a:r,s:2*r,D(a,r):1,D(a,z):0,D(s,r):2,D(s,z):0,D(s,r,z):0})),
 'EB_zz':sp.simplify(EBzz.subs({a:r,s:2*r,D(a,r):1,D(a,r,2):0,D(a,z):0,D(s,r):2,D(s,z):0,D(s,z,2):0})),
}
t=sp.symbols('t', negative=True)
# t=-e^-r: e^{2lambda}=e^{2r}; rho=e^{2r}; dt=e^-r dr, so e^{2lambda}rho dt=e^{3r}dr.
physical_weight=sp.simplify(sp.exp(2*r)*sp.exp(2*r)*sp.exp(-r))
out={
 'base_identity':{k:str(vv) for k,vv in checks.items()},
 'all_identity_residuals_zero':all(vv==0 for vv in checks.values()),
 'frozen_cusp':{k:str(vv) for k,vv in frozen.items()},
 'frozen_cusp_expected':'E_B = -1/2 dv tensor dv in orthonormal (dr,e^-r dz) frame',
 'physical_forcing_weight':str(physical_weight),
 'physical_orbit_equation':'d_r(e^{3r} v_r)+d_z(e^r v_z)=-e^{3r}(E_x-E_y)',
 'lattice_scaling':'G -> N^{-2}G changes sigma by -2 log N but leaves M and U unchanged',
}
p=Path(__file__).resolve().parents[1]/'data'/'step80_base_identity.json';p.write_text(json.dumps(out,indent=2))
print(json.dumps(out,indent=2));print('wrote',p)

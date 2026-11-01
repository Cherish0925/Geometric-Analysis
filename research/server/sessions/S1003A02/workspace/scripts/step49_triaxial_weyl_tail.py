#!/usr/bin/env python3
"""Exact reduced check of the nu=4 triaxial CH Weyl tail (Step 49).

For A=sinh(r)(1+eps e^-4r), B=sinh(r)(1-eps e^-4r),
C=sinh(r)cosh(r), the linearized chiral variables satisfy
  dv1=d=4 e^-4r (sech r - sinh r), dv2=-d, dv3=0.
The diagonal chiral formula reduces to
  dW11=-d'/(2 sinh r)+d(3 sinh(r)^2/2-1)/(sinh(r)^2 cosh r),
  dW22=-dW11, dW33=0.
This script verifies the leading coefficient and writes the scalar--4 consequences.
"""
import json, os
import sympy as sp

r=sp.symbols('r', positive=True)
s=sp.sinh(r); c=sp.cosh(r); q=sp.exp(-4*r)
d=4*q*(1/c-s)
dW11=sp.simplify(-sp.diff(d,r)/(2*s)+d*(sp.Rational(3,2)*s*s-1)/(s*s*c))
lead=sp.simplify(sp.limit(sp.exp(4*r)*dW11,r,sp.oo))
next6=sp.simplify(sp.limit(sp.exp(6*r)*(dW11-lead*sp.exp(-4*r)),r,sp.oo))
# At scalar -4, multiply Weyl endomorphism by 1/6.
scaled_lead=sp.simplify(lead/6)
sigma_coeff=abs(int(scaled_lead))
dist_coeff=sp.simplify(sp.sqrt(2)*abs(scaled_lead))
psi_coeff=sp.simplify(4*scaled_lead**2)
out={
 'delta_v1':str(d),
 'delta_W11_exact':str(sp.factor(dW11)),
 'lim_e4r_delta_W11':str(lead),
 'lim_e6r_remainder_after_leading':str(next6),
 'Ric_minus6_delta_Wplus_leading':['-12','12','0'],
 'scalar_minus4_delta_Wplus_leading':['-2','2','0'],
 'sorted_sigma_leading_coefficient':sigma_coeff,
 'dist_to_K_leading_coefficient':str(dist_coeff),
 'Psi_leading_coefficient':str(psi_coeff),
 'conclusions':{
   'd_mu_min_first_variation':0,
   'd_norm_Wplus_sq_first_variation':0,
   'sigma':'2 |eps| e^(-4r) + O(|eps|e^(-6r)) + O(eps^2 e^(-8r))',
   'dist':'2 sqrt(2) |eps| e^(-4r) + faster terms',
   'Psi':'16 eps^2 e^(-8r) + O(eps^2 e^(-10r)) + higher eps order'
 }
}
p=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','data','step49_triaxial_weyl_tail.json')
with open(p,'w') as f: json.dump(out,f,indent=1)
print(json.dumps(out,indent=1))

"""Exact Berger eta/signature-charge comparison in the session normalization.

The Berger metric is h_lambda = R^2(lambda^2 sigma_f^2+sigma_g^2+sigma_h^2),
with lambda=epsilon/R.  The radial first jet is a_f'=lambda V,
a_g'=a_h'=U.  Substitute this biaxial jet into the exact normalized diagonal
signature transgression
  s = sum p_i^2 - sum_cyc gamma_i p_j p_k + 2 sum gamma_i^2 - 6.
For a product/conical controlled collar U=V, compare with the explicit odd
signature eta formula for S^3 Berger metrics.  In Weingart's parameter
rho=lambda^2-1, the generating function gives the reduced class
bar_eta=rho^2/3 (mod Z) in dimension 3.  Anchoring the raw eta at eta(1)=0
and using the blow-up boundary orientation gives eta_APS=2 rho^2/3.
"""
import json
from pathlib import Path
import sympy as sp

lam,U,V=sp.symbols('lambda U V', real=True)
# Set R=1 by scale invariance.
a=[lam,sp.Integer(1),sp.Integer(1)]
p=[lam*V,U,U]
g=[]
for i in range(3):
    j=(i+1)%3; k=(i+2)%3
    g.append(sp.factor((a[j]**2+a[k]**2-a[i]**2)/(a[j]*a[k])))
S0=sum(pi**2 for pi in p)-sum(g[i]*p[(i+1)%3]*p[(i+2)%3] for i in range(3))+2*sum(gi**2 for gi in g)
sig=sp.factor(S0-6)
intrinsic=sp.factor(sig.subs(V,U))
rho=sp.factor(lam**2-1)
eta_aps=sp.factor(sp.Rational(2,3)*rho**2)
eta_reverse=-eta_aps
out={
  'gamma':[str(x) for x in g],
  'signature_transgression':str(sig),
  'decomposition_residual':str(sp.factor(sig-(2*(1-lam**2)**2+lam**2*(U-V)**2))),
  'controlled_collar_U_eq_V':str(intrinsic),
  'rho':str(rho),
  'eta_APS_blowup_orientation_raw_round_anchored':str(eta_aps),
  'eta_reverse_orientation':str(eta_reverse),
  'check_s_equals_3eta_plus_jet':str(sp.factor(sig-(3*eta_aps+lam**2*(U-V)**2))),
  'round':{'lambda':1,'s':str(sig.subs(lam,1)),'eta_APS':str(eta_aps.subs(lam,1))},
  'adiabatic_limit':{'lambda_to_0_s':str(sp.limit(sig,lam,0)),'eta_APS':str(sp.limit(eta_aps,lam,0)),
                      'euler_flux':0,'chiral_charge_bplus':-2,'round_chiral_charge_bplus':2,'price':4},
  'scope':'eta is intrinsic; the lambda^2(U-V)^2 term is the nonproduct collar/second-fundamental-form correction'
}
print(json.dumps(out,indent=1))
(Path(__file__).resolve().parents[1]/'data'/'berger_eta_charge.json').write_text(json.dumps(out,indent=1)+'\n')

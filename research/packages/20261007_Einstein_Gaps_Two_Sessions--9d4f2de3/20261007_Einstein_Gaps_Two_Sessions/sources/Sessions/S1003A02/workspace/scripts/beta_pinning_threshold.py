"""Threshold table for the exact beta-pinning lemma on a CH tail.

For B~=log(kappa/sqrt(1+zeta))+(beta'-kappa^{-1})/4,
 |Delta B~-int F_beta| <= sqrt(3 P_hat/8)*sqrt(int dt/W).
On CH, W=sinh(t)^3 cosh(t) and int_T^inf dt/W = 1/(2sinh^2 T)-.5 log(1+sinh(T)^-2).
Thus a mismatch C (after free-drift allowance) forces P_hat >= 8 C^2/(3 I(T)).
"""
import json,math
from pathlib import Path
from scipy.optimize import brentq

def I(t):
 u=1/math.sinh(t)**2
 return .5*(u-math.log1p(u))
rows=[]
for C in [.05,.1,.15,.2,.25,.3,.5,1]:
 target=8*C*C/3
 tau=brentq(lambda t:I(t)-target,1e-5,10)
 rows.append({'mismatch':C,'tau_P_for_cost_1':tau,'bound_at_tau_0p70':8*C*C/(3*I(.70))})
out={'formula':'P_hat >= 8 C^2/(3 I(T)), I(T)=1/(2sinh(T)^2)-log(1+sinh(T)^-2)/2',
     'I_0p70':I(.70),'rows':rows}
print(json.dumps(out,indent=1))
(Path(__file__).resolve().parents[1]/'data'/'beta_pinning_threshold.json').write_text(json.dumps(out,indent=1)+'\n')

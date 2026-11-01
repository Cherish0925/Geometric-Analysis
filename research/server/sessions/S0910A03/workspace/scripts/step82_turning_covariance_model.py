#!/usr/bin/env python3
"""Explore the algebraic first-return balance under J' and volume identities.

This is not an Einstein connector solver.  It asks a narrower structural
question: do the exact integrated slice balances alone prohibit I from
turning?  At I=0 write u=alpha(v-<v>)+u_perp.  The most favorable correlation
for fixed second moments is measured against the shear penalty.  We also
solve the homogeneous (z-independent, B0=0, E=0) balance as a control.
"""
from __future__ import annotations
import json
from pathlib import Path
import numpy as np

# At a return I=0, <u>=0.  Algebraically the geometric term is
# T=2<u v>+1/2<v^2>-<B0^2>.
# Scan sinusoidal profiles with means and phases.
z=np.linspace(0,2*np.pi,200000,endpoint=False)
rows=[]
for m in [0.0,0.5,1.0,2.0,3.0]:
  for A in [0.25,0.5,1.0,2.0,3.0]:
    v=m+A*np.cos(z)
    for alpha in [0.0,0.5,1.0,2.0]:
      u=alpha*A*np.cos(z)  # mean zero
      for shear_ratio in [0.0,0.5,1.0,2.0]:
        B0sq=(shear_ratio*A*np.sin(z))**2
        T=float(np.mean(2*u*v+0.5*v*v-B0sq))
        if T>=3:
          rows.append({'v_mean':m,'v_amp':A,'alpha':alpha,'shear_ratio':shear_ratio,'turn_term':T})

# Homogeneous moment control at I=0 has u=0 pointwise and T=v^2/2.
# The integrated I/J balances alone put the algebraic turning threshold at
# v=sqrt(6), but a flat homogeneous exact Einstein slice must also satisfy
# the contracted Gauss equation H^2-|S|^2=v^2/2=6, hence v=sqrt(12).
# Thus the sqrt(6) row is deliberately labelled moment-only.  At v=sqrt(12),
# the local exact Einstein equations give a genuine compatible reversal germ.
hom=[]
for v in [0,1,np.sqrt(6),np.sqrt(12),4]:
  hom.append({'v':float(v),'v_prime_from_J':float(6-v*v),
              'moment_I_prime_over_V':float(-3+0.5*v*v),
              'flat_exact_Gauss_residual':float(0.5*v*v-6)})

# Volume: V'=I+J, so at I=0, V'/V=<v>.  J/V=<v>.
# Define y=J/V. For E=0, y'=6-y^2-y*(I/V).
# At return I=0: y'=6-y^2. This gives only a mean bound, while
# <v^2>=y^2+Var(v), so inhomogeneity can enlarge the favorable term.
out={
 'scope':'Algebraic compatibility of integrated balances only; no PDE existence or reachability',
 'first_return_term':'T=2 Cov(u,v)+<v^2>/2-<|B0|^2>',
 'number_of_sinusoidal_profiles_with_T_ge_3':len(rows),
 'sample_compatible_profiles':rows[:20],
 'homogeneous_control':hom,
 'local_exact_reversal_germ':'For flat homogeneous slices with u=0 and orbit p=sqrt(3), v=2p=sqrt(12), Hamilton holds, mixed constraint is zero, and u_prime=3; this proves local exact reversal is allowed away from the reflected center but not reachability from that center.',
 'normalized_J_dynamics_exact':"Let x=I/V, y=J/V. With E=0, V'/V=x+y and J'=6V, hence y'=6-y(x+y). At x=0, y'=6-y^2.",
 'key_result':'The integrated balances do not by themselves obstruct reversal. Positive covariance and orbit-expansion variance can make T>=3 even with moderate shear. Any exclusion must control covariance/variance by intrinsic orbit energy, the matrix equation, or base constraints; any construction must realize these profiles dynamically while keeping all E components small.',
 'important_distinction':'An algebraically favorable slice need not be reachable from a reflected scalar-minus-six center. The VII0 collapse is precisely a reachability failure despite available favorable algebraic states.'
}
p=Path(__file__).resolve().parents[1]/'data'/'step82_turning_covariance_model.json'
p.write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2));print('wrote',p)

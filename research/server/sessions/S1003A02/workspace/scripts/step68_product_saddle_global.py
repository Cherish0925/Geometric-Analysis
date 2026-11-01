#!/usr/bin/env python3
"""Global invariant calculation for the Step-68 product variation k=fQ.

This avoids the invalid use of the non-automorphic local differential dz^2 in
a closed-surface integral.  It differentiates the diffeomorphism-invariant
functional P using standard TT variation formulas and the identities for a
holomorphic quadratic differential Q on a constant-curvature surface:
 delta Q=0, tr Q=0, nabla* nabla Q=-2 K1 Q.

For k=fQ, Delta_2 f=mu f, the gauge-fixed Ricci variation is
 Ric'_0=(K1+mu/2)k and s'=0.  The full Hessian also contains the background
Ricci contraction with the second metric/volume response.  Rather than infer
it from a noncompact coordinate patch, this script leaves that coefficient
symbolic and records the two competing formulas to be resolved tensorially.
"""
import sympy as sp, json
from pathlib import Path
K1,K2,mu,C=sp.symbols('K1 K2 mu C',real=True)
generator=mu*(mu+2*(K1-K2))/4
local_patch=(mu**2+(K1-K2)*mu+6*K1*(K1-K2))/4
out={
 'Ricci_prime_antiHermitian':'(mu/2) k',
 'scalar_prime':'0',
 'q2_prime_and_second':'0 along fixed omega compatible path',
 'generator_candidate':str(generator),
 'nonautomorphic_patch_candidate':str(local_patch),
 'warning':'Re(dz^2) on H^2 is not deck-invariant on a closed hyperbolic surface; integration by parts can acquire fundamental-domain boundary terms. The patch coefficient cannot by itself refute the global formula.',
 'decisive_remaining_identity':'Compute the integrated second-order AAD identity globally for k=fQ, especially (rho0,t2^-) and rho0_prime, or evaluate an automorphic Q numerically on a closed quotient.'
}
p=Path(__file__).resolve().parents[1]/'data'/'step68_product_saddle_global.json';p.write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))

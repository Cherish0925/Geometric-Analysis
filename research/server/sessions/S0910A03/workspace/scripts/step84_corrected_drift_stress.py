#!/usr/bin/env python3
"""Step 84: algebraic verification of the corrected weighted Bochner stress term.

Conventions:
  L = Delta + <grad sigma, grad> = rho^{-1} div(rho grad), rho=e^sigma.
  For a map U from a two-dimensional base into H^2 of sectional curvature -1,
  1/2 L |dU|^2 = |D dU|^2 + <dU, D tau_sigma>
                   + <(Ric_B-Hess sigma), U*h> + target_term.
  The Einstein reduction gives
    Ric_B-Hess sigma = -3 gamma_B + 1/2 d sigma^2
                       + 1/2 U*h + E_B.

This script checks the two-dimensional contractions.  If A is the Gram matrix
A_ij=<U_i,U_j>, then <U*h,U*h>=tr(A^2), the quartic base-stress term is
(1/2)tr(A^2), and negative target curvature contributes
2 det(A)=|dU|^4-tr(A^2).  Their sum is
  |dU|^4 - (1/2)tr(A^2),
which lies between (1/2)|dU|^4 and (3/4)|dU|^4 in rank two.
"""
from __future__ import annotations
import json
from pathlib import Path
import sympy as sp

# Gram matrix of dU in an orthonormal base frame.
a,b,c = sp.symbols('a b c', real=True)
A = sp.Matrix([[a,c],[c,b]])
trA = sp.trace(A)
trA2 = sp.trace(A*A)
detA = A.det()
quartic_stress = sp.Rational(1,2)*trA2
negative_target = 2*detA
quartic_total = sp.expand(quartic_stress + negative_target)
quartic_alt = sp.expand(trA**2 - sp.Rational(1,2)*trA2)
identity = sp.simplify(quartic_total-quartic_alt)

# Eigenvalue representation, useful for sharp bounds.
l1,l2 = sp.symbols('l1 l2', nonnegative=True)
Qeig = sp.expand((l1+l2)**2-sp.Rational(1,2)*(l1**2+l2**2))
lower_res = sp.factor(Qeig-sp.Rational(1,2)*(l1+l2)**2)
upper_res = sp.factor(sp.Rational(3,4)*(l1+l2)**2-Qeig)

# Round cusp benchmark in physical Gaussian coordinates:
# gamma=dr^2+e^(2r)dz^2, sigma=2r, U constant.
# Ric=-gamma, Hess sigma=diag(0,2), hence Ric-Hess=diag(-1,-3).
round_cusp = {
    'metric':'dr^2+e^(2r) dz^2',
    'sigma':'2r',
    'Ric_minus_Hess_sigma_orthonormal':[-1,-3],
    'einstein_reduction_check_rr':'-3 + (1/2)*4 = -1',
    'einstein_reduction_check_zz':'-3 + 0 = -3',
}

# Demonstrate why the Step 83 cosh benchmark is not Einstein for the same sigma.
r=sp.symbols('r', real=True)
# gamma=dr^2+cosh(r)^2 dz^2 has Ric=-gamma; Hess(2r)_zz in ON frame=2 tanh r.
# E_B = Ric-Hess-1/2 dsigma^2+3g for U constant.
cosh_Err=sp.simplify(-1-0-2+3)
cosh_Ezz=sp.simplify(-1-2*sp.tanh(r)-0+3)

out={
 'bochner_convention':{
   'operator':'L=Delta+<grad sigma,grad>=rho^{-1}div(rho grad)',
   'drift_curvature':'Ric_B-Hess sigma',
   'base_equation':'Ric_B-Hess sigma=-3 gamma_B+(1/2)d sigma tensor d sigma+(1/2)U*h+E_B',
 },
 'gram_algebra':{
   'A':'[[a,c],[c,b]] positive semidefinite',
   'trA':str(trA),
   'trA2':str(trA2),
   'detA':str(detA),
   'base_stress_quartic_half_trA2':str(quartic_stress),
   'negative_target_term_2detA':str(negative_target),
   'total':str(quartic_total),
   'total_as_trace_expression':str(quartic_alt),
   'identity_residual':str(identity),
 },
 'sharp_rank_two_bounds':{
   'eigenvalue_expression':str(Qeig),
   'Q_minus_half_trace_squared':str(lower_res),
   'three_quarters_trace_squared_minus_Q':str(upper_res),
   'conclusion':'(1/2)|dU|^4 <= Q <= (3/4)|dU|^4 for nonnegative Gram eigenvalues',
 },
 'benchmarks':{
   'round_cusp':round_cusp,
   'cosh_base_with_sigma_2r':{
      'E_B_rr':str(cosh_Err),
      'E_B_zz':str(cosh_Ezz),
      'conclusion':'not an exact Einstein benchmark except asymptotically in zz',
   },
 },
 'forcing_form':{
   'pointwise':'<dU,D tau_sigma> is retained; no derivative of the Ricci defect is estimated pointwise',
   'integrated':'int eta^2 rho <dU,D tau_sigma> = -int eta^2 rho |tau_sigma|^2 - 2 int eta rho <dU(grad eta),tau_sigma> plus boundary flux',
   'consequence':'bounded orbit defect controls tension itself; integration by parts converts D(tension) to a favorable -|tension|^2 term and cutoff/boundary pairings',
 },
}
path=Path(__file__).resolve().parents[1]/'data'/'step84_corrected_drift_stress.json'
path.write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
print('wrote',path)

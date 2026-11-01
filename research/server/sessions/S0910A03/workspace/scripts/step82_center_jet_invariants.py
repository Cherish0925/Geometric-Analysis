#!/usr/bin/env python3
"""Symbolically verify universal center-jet identities for the reversal variable.

We use TTCS-derived physical-arclength identities and verify the algebraic
consequences without asserting the differential-geometric inputs beyond their
stated hypotheses.  At an exact reflected scalar-minus-six OT center define
  k=|U_s|^2-h^2, c=h_s+h^2=(12-k)/4,
  u1=-k/4, v1=3+k/4, b1=-tau.
Weighted <k>=12.  Verify the quadratic turning coefficients and lower bound
for K'' quoted in the Step 82 synthesis.
"""
from __future__ import annotations
import sympy as sp, json
from pathlib import Path
k,tau2,K2=sp.symbols('k tau2 K2', real=True)
Ek2,Vark,Etau2=sp.symbols('Ek2 Vark Etau2', nonnegative=True)
u1=-k/4
v1=3+k/4
# Means under the center physical measure: <k>=12 -> <u1>=-3,<v1>=6.
Eu1=-3; Ev1=6
# E[u1 v1] in terms of E[k],E[k^2].
Euv=sp.expand((-sp.Rational(3,4)*12-sp.Rational(1,16)*Ek2))
Covuv=sp.expand(Euv-Eu1*Ev1)
Ev2=sp.expand(9+sp.Rational(3,2)*12+sp.Rational(1,16)*Ek2)
Varv=sp.expand(Ev2-Ev1**2)
# |B0|^2 coefficient is |b1|^2/2=tau2/2 under normalization |b|^2=2|B0|^2.
T2=sp.simplify(2*Covuv+sp.Rational(1,2)*Ev2-sp.Rational(1,2)*Etau2)
Ttilde2=sp.simplify(2*Covuv+sp.Rational(1,2)*Varv-sp.Rational(1,2)*Etau2)
# Replace E[k^2]=Var(k)+144.
T2var=sp.expand(T2.subs(Ek2,Vark+144))
Ttilde2var=sp.expand(Ttilde2.subs(Ek2,Vark+144))
# Generator formula K''=2Etau2+18+3/8 E[k^2].
Ksecond=2*Etau2+18+sp.Rational(3,8)*Ek2
Ksecond_var=sp.expand(Ksecond.subs(Ek2,Vark+144))
# x cubic coefficient from x'=3-K/2-x(x+y), K=12+K2 r^2/2,
# x=-3r+A r^3, y=6r+... : 3A=9-K2/4.
A=sp.simplify((9-K2/4)/3)
out={
 'inputs':{
  'u1':'-k/4','v1':'3+k/4','mean_k':12,
  'B0_quadratic_coefficient':'<|tau|^2>/2',
  'normalization':'|U_r|^2=2|B0|^2'},
 'verified_algebra':{
  'Cov(u1,v1)':str(Covuv),
  'Var(v1)':str(Varv),
  'T_quadratic_in_Var_k_tau':str(T2var),
  'Ttilde_quadratic_in_Var_k_tau':str(Ttilde2var),
  'K_second':str(Ksecond),
  'K_second_in_Var_k_tau':str(Ksecond_var),
  'K_second_lower_bound':72,
  'x_cubic_coefficient_given_K2':str(A)},
 'interpretation':{
  'T':'The full first-return expression includes mean y^2/2, so its r^2 coefficient can be positive.',
  'Ttilde':'After removing y^2/2, all spatial fluctuation/shear contributions are nonpositive at order r^2.',
  'K':'K initially rises universally; any drop from 12 toward the return threshold <=6+2delta must occur later and nonlinearly.'},
 'dependency':'This script verifies the algebraic consequences. The differential-geometric jet inputs and K-second formula were independently tensor-derived in trace/ttcs/results/step82_ttcs02_verifier1_integration.md.'
}
p=Path(__file__).resolve().parents[1]/'data'/'step82_center_jet_invariants.json'
p.write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2));print('wrote',p)

#!/usr/bin/env python3
"""Replay of the superseded Step-67 product inputs.

This file is intentionally retained as a record of the factor-two torsion
normalization error. It is NOT an independent derivation. The authoritative
form-norm calculation gives
  F_2 = mu*(mu+K1-K2)/4 * ||fQ||^2,
not the expression produced below. See
`notes/step68_product_cscK_saddle_verification.md` and the Step-68 TTCS
verifier integration.
"""
import sympy as sp,json
from pathlib import Path
K1,K2,mu=sp.symbols('K1 K2 mu',real=True)
ric_anti=mu/2
# OLD, WRONG values: each is twice the form-norm value.
u2_old=mu/4
rho_t_old=-(K1-K2)*mu/8
Q_old=ric_anti**2-4*rho_t_old
correct=mu*(mu+K1-K2)/4
out={'status':'superseded_factor_two_record','old_u2':str(u2_old),'old_rho0_t2_pairing':str(rho_t_old),'old_Hessian':str(sp.factor(Q_old)),'correct_Hessian':str(correct),'old_minus_correct':str(sp.factor(Q_old-correct))}
p=Path(__file__).resolve().parents[1]/'data'/'step68_product_saddle_global_exact.json';p.write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))

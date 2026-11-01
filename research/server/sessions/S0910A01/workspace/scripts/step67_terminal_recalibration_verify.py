#!/usr/bin/env python3
"""Structural/algebra checks for Step 67 terminal recalibration recovery.

This script is not a proof of the Seiberg--Witten theorem.  It verifies the
algebraic constants and the square identity used after the monopole/Chern--Weil
inputs are accepted.
"""
from pathlib import Path
import json
import sympy as sp

root = Path('Sessions/S0910A01')
note = root / 'workspace/notes/step67_terminal_recalibration_recovery.md'
text = note.read_text()

checks = []

def check(name, cond, detail=''):
    checks.append({'name': name, 'passed': bool(cond), 'detail': detail})
    print(f"[{'PASS' if cond else 'FAIL'}] {name}{': ' + detail if detail else ''}")

# 1. Square identity: s^2/24 + 2u^2 = f^2/12 + (s+8sqrt(6)u)^2/216
s, u = sp.symbols('s u', real=True)
f = sp.Rational(2, 3)*s - 2*sp.sqrt(sp.Rational(2, 3))*u
identity_residual = sp.simplify(s**2/sp.Integer(24) + 2*u**2 - f**2/sp.Integer(12) - (s + 8*sp.sqrt(6)*u)**2/sp.Integer(216))
check('square_identity_exact', identity_residual == 0, str(identity_residual))

# 2. Constants from D_av <= J <= Q/(8pi^2)
Q = sp.symbols('Q', positive=True)
pi = sp.pi
square_const = sp.simplify(864*pi**2*(Q/(8*pi**2))/Q)
gap_const = sp.simplify(48*pi**2*(Q/(8*pi**2))/Q)
scalar_const = sp.Integer(4)
total_const = sp.simplify(1 + scalar_const + square_const + gap_const)
check('square_constant_108', square_const == 108, str(square_const))
check('gap_constant_6', gap_const == 6, str(gap_const))
check('total_constant_119', total_const == 119, str(total_const))

# 3. Selected average cancellation: int Phi <= Cdelta2 A and Vol(P)>=alpha A.
C, delta2, A, alpha = sp.symbols('C delta2 A alpha', positive=True)
mean = sp.simplify(C*delta2*A/(alpha*A))
check('A_cancels_in_selected_mean', mean == C*delta2/alpha, str(mean))

# 4. Textual safeguards: terminal, q>=0 no q_+, trace-free vs Einstein defect, sign-free G.
check('terminal_reapplies_topology_not_transport', 'does **not** transport' in text and 'reapplies' in text)
check('q_nonnegative_no_q_plus', 'q>=0' in text and 'such a term is absent' in text and 'q_+' not in text)
check('trace_free_distinguished_from_Einstein_defect', 'E^\\circ' in text and '\\mathcal E=\\operatorname{Ric}_g+g' in text)
check('negative_part_sign_free_formulation', '\\mathcal G=f^2-a_{*,-}^2' in text and 'does not require `s<0`' in text)
check('liouville_pullback_interface_present', 'unit-tangent-bundle' in text and 'A_\\rho\\Phi_i' in text)
check('step65_broken_display_repaired', 'Gronwall gives\n### 5.1' not in (root/'workspace/notes/step65_per_datum_existence_theorem.md').read_text())

out = root / 'workspace/data/step67_terminal_recalibration_verify.json'
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps({'checks': checks, 'passed': sum(c['passed'] for c in checks), 'total': len(checks)}, indent=2))

passed = sum(c['passed'] for c in checks)
print(f"\n=== Summary: {passed}/{len(checks)} passed ===")
print(f"Wrote {out}")
if passed != len(checks):
    raise SystemExit(1)

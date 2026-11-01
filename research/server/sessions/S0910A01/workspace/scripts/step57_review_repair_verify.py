#!/usr/bin/env python3
"""Structural checks for Step 57 Preceptor repair.

This is not a PDE proof.  It verifies that the durable notes no longer carry
specific invalid claims found in Step 56 and that the repaired proof ledger
contains the coupled DeTurck and uniform-scope ingredients required by the
review.
"""
from pathlib import Path
import json

ROOT = Path('Sessions/S0910A01')
NOTE57 = ROOT/'workspace/notes/step57_preceptor_deTurck_uniqueness_and_scope_review.md'
NOTE56 = ROOT/'workspace/notes/step56_common_time_and_terminal_compactness.md'
ROUTE56 = ROOT/'workspace/plans/route_assessment_step56.md'
OUT = ROOT/'workspace/data/step57_review_repair_verify.json'

texts = {p.name: p.read_text() for p in [NOTE57, NOTE56, ROUTE56]}

checks = []
def check(name, ok, detail):
    checks.append({'name': name, 'ok': bool(ok), 'detail': detail})

n57 = texts[NOTE57.name]
n56 = texts[NOTE56.name]
r56 = texts[ROUTE56.name]

# 1. Raw metric uniqueness is explicitly invalidated, not used as a proof.
check('raw_metric_uniqueness_invalidated',
      'raw metric-difference estimate' in n56 and 'is invalid' in n56 and 'ungauged Ricci linearization contains second-order' in n56,
      'Step56 patched to reject raw ungauged uniqueness estimate')
check('route56_rejects_raw_uniqueness',
      'raw metric estimate' in r56 and 'invalid' in r56 and 'transported-cutoff DeTurck pair' in r56,
      'route assessment patched')

# 2. Coupled DeTurck pair comparison includes both variables and averaged weighted dissipation.
check('coupled_variables_present',
      all(s in n57 for s in ['H=G_1-G_2', 'b=\\beta_1-\\beta_2', 'transported-cutoff DeTurck']),
      'metric and scalar differences appear')
check('averaged_dissipation_present',
      '(\\beta_1^2+\\beta_2^2)|DH|^2' in n57 and '\\bar A^{ab}=\\tfrac12' in n57,
      'averaged principal coefficient/dissipation recorded')
check('scalar_transport_present',
      '\\partial_tb=\\beta_1^2W(G_1)\\cdot Db' in n57 and 'W(G_1)-W(G_2)=A_1*DH+A_0*H' in n57,
      'scalar transport difference uses metric derivative coupling')
check('gauge_interface_or_splice_present',
      ('reverse DeTurck gauge lemma' in n57 and 'existence-style restart' in n57 and 'autonomous-PDE' in n57),
      'note separates pair uniqueness from geometric gauge and gives uniqueness-free splice alternative')

# 3. Finite current-pair dependency is not hidden.
check('finite_pair_dependency_visible',
      'Finite current-pair induction remains a real proof dependency' in n57 and '(U_7,C_8)' in n57 and 'A03 Step 60 supplied' in n57,
      'general commutator expansion marked as dependency, with A03 Step60 candidate assimilation')
check('current_terms_listed',
      all(s in n57 for s in ['\\chi C_{m+2}*U', '\\chi C_2*U_m', '\\chi C_2*T_m', 'C_1*U_m']),
      'top cutoff, signed Hessian, and cutoff-jet exchange terms appear')
check('no_literal_backslash_n_typo', '\\n \\chi' not in n57, 'no accidental literal \\n in displayed T_m equation')

# 4. Scope: A cancellation/uniform IL target preserved, no revived A^-1/2 in A01 patched notes.
check('step56_A_cancellation_scope',
      'factor $A_i$ cancels' in n56 and 'uniform over\nthe stated IL class' in n56,
      'Step56 conclusion patched to IL-class uniform target')
check('step57_A_cancellation_scope',
      'The factor \\(A_i\\) cancels' in n57 and '\\varepsilon_{\\rm IL}>0' in n57,
      'Step57 states uniform IL gap conditional on uniform constants')
for label, txt in [('note56', n56), ('route56', r56), ('note57', n57)]:
    bad = ['A_i^{-1/2}', 'A^{-1/2}', '1/\\sqrt A', 'depending on the topology\n$(A,D)$']
    check(f'no_revived_A_loss_{label}', not any(b in txt for b in bad), f'forbidden phrases absent in {label}')

# 5. Not mistaken for full Yau26.
check('full_goal_not_claimed',
      'not final resolution of Yau 26' in n57 and 'positive\npinching' in n57 and 'dimensions n >= 5' in n57,
      'restricted theorem separated from full goal')

OUT.parent.mkdir(parents=True, exist_ok=True)
summary = {'passed': sum(c['ok'] for c in checks), 'total': len(checks), 'checks': checks}
OUT.write_text(json.dumps(summary, indent=2, ensure_ascii=False))
print('=== Step57 review repair structural checks ===')
for c in checks:
    print(f"[{'PASS' if c['ok'] else 'FAIL'}] {c['name']} -- {c['detail']}")
print(f"=== Summary: {summary['passed']}/{summary['total']} passed ===")
print(f"Wrote {OUT}")
if summary['passed'] != summary['total']:
    raise SystemExit(1)

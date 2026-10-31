"""Exact checks for Lemma Z (Step 33): b_+ depends only on u; monotone b_+ path; neutral family.
Output: workspace/data/static_charge/lemmaZ_exact.json"""
import json
from pathlib import Path
import sympy as sp

A, s, lam, u1, u2, u3 = sp.symbols('A s lambda u1 u2 u3', real=True)
f = lambda u: u[0]**2+u[1]**2+u[2]**2+u[0]*u[1]*u[2]          # b_+ = 2 - f
h = lambda w: w[0]**2+w[1]**2+w[2]**2-w[0]*w[1]*w[2]-2        # b_-
gam_coll = [lam, lam, 2-lam**2]                               # h-slot collapsed Berger, ratio lam
out = {
 'stage1_f': str(sp.factor(f([A, 1, -2]))),
 'stage1_df_dA': str(sp.diff(f([A, 1, -2]), A)),
 'stage2_f': str(sp.expand(f([A, s, -2*s]))),
 'stage2_df_ds': str(sp.factor(sp.diff(f([A, s, -2*s]), s))),
 'neutral_bplus': str(sp.simplify(2-f([A, A, -2]))),
 'neutral_bminus_lam0': str(sp.simplify(h([A+2*g for g in [0, 0, 2]][0:2]+[-2+4]))),
 'neutral_bminus_lam': str(sp.factor(h([A+2*lam, A+2*lam, -2+2*(2-lam**2)]))),
 'CH_end_bplus': str(sp.simplify(2-f([3*sp.sinh(s)**2, 0, 0]))),
}
print(json.dumps(out, indent=1))
p = Path(__file__).resolve().parents[1]/'data'/'lemmaZ_exact.json'
p.write_text(json.dumps(out, indent=1)+'\n')

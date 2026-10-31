# Yau 26 — verification artifacts

- `report_tex/` — LaTeX sources of the report (compile `yau26_report.tex` with XeLaTeX + ctex, twice).
- `verify/` — independent symbolic / high-precision checks of the log-Weyl construction
  (`v1_core.py` → `v1b_family.py` → `v1c_htilde.py`; `v2_logidentity.py`; `v3b_football.py SIGMA EXP...`; `v4_tail.py`) and their logs.
- `audit_bundle/`, `audit_obstructions/` — referee-style re-derivations of the surface-bundle chapter and of the quantitative obstruction propositions.
- `final_review/` — adversarial review scripts for the report's own new statements.
- `wormhole/` — exploratory (inconclusive) Gaussian-gauge evolution code for Problem W.
- `repro_run1/` — output of the package's own `scripts/reproduce.py` (all five groups passed).

Requirements: Python 3.11, sympy 1.14, numpy 2.4, scipy 1.17, mpmath 1.3.
Run `v1_core.py` first (it writes `biaxial_ricci.pkl` used by `v1b_family.py`).
SHA-256 of every file is listed in the report, section 9.

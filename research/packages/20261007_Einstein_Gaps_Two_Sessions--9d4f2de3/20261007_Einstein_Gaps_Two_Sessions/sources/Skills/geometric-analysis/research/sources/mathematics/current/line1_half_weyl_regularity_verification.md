# Verification record: equation-to-budget estimate

23 September 2026. Development baseline: `6065e33`.

The proof is in `line1_half_weyl_regularity.md`; its self-contained bundle
argument, spectral functional calculus and composition are separate from
the finite checks. The classical harmonic-Weyl PDE was checked against
LeBrun, arXiv:1903.00956v2, equation (9), on 23 September 2026.

Executed locally:

```sh
/data/qiushi/.venv/bin/python check_line1_half_weyl_regularity.py
pandoc line1_half_weyl_regularity.md --from=markdown+tex_math_single_backslash --standalone --metadata-file=line1_paper.yaml -o line1_half_weyl_regularity.tex
xelatex -interaction=batchmode -halt-on-error line1_half_weyl_regularity.tex
xelatex -interaction=batchmode -halt-on-error line1_half_weyl_regularity.tex
git diff --check
```

All 15 exact algebraic checks passed. Three intentional errors were rejected:
the scalar sign in the Einstein Weyl equation, a missing factor one-half
in the splitting residual, and an incorrect amplitude coefficient in the
Kähler--Einstein orbit distance. The final PDF has five pages and compiled
twice without a TeX error. These checks do not certify the analytic theorem,
exhaust publication priority, or establish a new Yau26 branch.

The central analytic point is the Hessian-slot interchange in equation (8).
Its commutator introduces Ricci and the bundle curvature but no derivative
of bundle curvature. Treating the half-Weyl tensor as a section of
`Sym0(Lambda+)` ensures that the opposite Weyl block does not enter this
curvature term. The residual source remains an explicit input outside the
exact/harmonic regime.

No installed Skill, user Session, service or live system was changed.

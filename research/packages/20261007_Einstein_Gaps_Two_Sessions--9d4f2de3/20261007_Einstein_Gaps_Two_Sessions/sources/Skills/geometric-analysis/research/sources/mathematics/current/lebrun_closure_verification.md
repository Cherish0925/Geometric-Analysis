# Closure verification

22 September 2026. Source baseline: local commit 5d8f86c.

The mathematical note is lebrun_stability_closure.md; its generated
standalone TeX and PDF have the same stem. The new material consolidates
the polarized application and its Einstein-sign cases. It does not
replace the existing integral calibration proof.

Two read-only reviews checked:

- conformal covariance with the explicit spinor identification; the order
  of metric, structure and weight quantifiers; the uniform constant transfer;
  the scalar-flat branch and threshold endpoints;
- Theorem 3.3's positive-budget scope, the elementary nonpositive-budget
  Chern--Weil identity, and the Ricci-flat exception at zero budget without
  blow-ups or handles.

No substantive interface error was found. The inspected LeBrun PDFs are
the author-hosted/arXiv preprint. The journal publication was identified,
but its subscription text was not inspected. Accordingly the note does
not attribute the preprint's zero-corner wording to the journal edition.

The program check_lebrun_closure.py passed four exact symbolic identities,
the constant comparisons, and the first 100 arithmetic examples. These
check transcription and algebra, not the integral calibration lemma or
gauge theoretic existence. The full analytic proof was not independently
re-certified in this check.

Reproduction:

~~~sh
python check_lebrun_closure.py
pandoc lebrun_stability_closure.md \
  --from=markdown+tex_math_single_backslash --standalone \
  --number-sections --to=latex --output=lebrun_stability_closure.tex
xelatex -interaction=batchmode -halt-on-error lebrun_stability_closure.tex
xelatex -interaction=batchmode -halt-on-error lebrun_stability_closure.tex
~~~

Dependencies: Python with SymPy, Pandoc, XeLaTeX with the standard AMS and
mathrsfs packages. No Session directory or live Qiushi service is required.
Installed Skills, research Session state, and services were not modified.

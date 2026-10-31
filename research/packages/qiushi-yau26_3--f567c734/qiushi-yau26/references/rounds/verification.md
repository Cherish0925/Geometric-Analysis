# Reproduction

All six scripts below were executed successfully in this research workspace
on 19 September 2026. They use Python 3.12.13 and SymPy 1.14.0 through the
existing `qiushi-yau26 env numeric` adapter. No environment was installed,
upgraded, or modified.

Run from this directory:

```bash
qiushi-yau26 env numeric python curvature_box.py
qiushi-yau26 env numeric python fixed_ratio_check.py
qiushi-yau26 env numeric python construction_checks.py
qiushi-yau26 env numeric python rigidity_check.py
qiushi-yau26 env numeric python rigidity_review_check.py
qiushi-yau26 env numeric python global_check.py
```

The same scripts can be run with an ordinary Python interpreter providing
SymPy 1.14.0. They do not read the old Session directories or require live
Qiushi services. They print their results; no output directory is needed.

| Script | Result actually checked |
| --- | --- |
| `curvature_box.py` | Exact separate concavity; all 16 Ricci-box vertices; each polynomial comparison over its full interval; both connector inverse formulas and their joining point. PASS. |
| `fixed_ratio_check.py` | Exact optimal Weyl amplitude; Ricci-coordinate derivative; ratio branches, joining values, inverse equations, and strict improvement formulas. PASS. |
| `construction_checks.py` | 13 exact curvature, projection, integral, hyperbolic-path, and restricted vertical-response checks. PASS. |
| `rigidity_check.py` | Target potential, positive matrix and minors, rational spectral-box bounds, radial obstruction coefficient, and Cotton symbol. PASS. |
| `rigidity_review_check.py` | Independent reconstruction from individual eigenvalue equations; explicit divergence-free four-index first jet; invariant Hessian and Cotton projection. PASS. |
| `global_check.py` | Algebraic Weyl energies, monopole integrals, calibration density, connector CGB balance, and coarse inverse bound. PASS. |

Selected exact outputs:

\[
\operatorname{minors}(M_0-I)=(7,153,243),\quad P(A_0)=1/16,
\quad \rho_{\rm spectral}=1/10000;
\]
\[
|C_{\rm symbol}|^2=4,\quad |C^+_{\rm symbol}|^2=2;
\qquad
\int 2(\operatorname{sech}^7t-2\operatorname{sech}^9t)dt=-15\pi/32.
\]

For the explicit \(E_D\) algebraic witness, the spectral and mixed monopole
integrals divided by \(V_*\) are approximately `16.861244175408` and
`39.124329350241`, respectively. Their required lower bounds are `16` and
`36`. These numbers describe algebraic curvature data, not a constructed
Einstein metric.

The analytic arguments are in the notes. Their independent checks are in
`independent_review.md` and `rigidity_review.md`. The construction proposition
uses the stated global manuscript estimates; these scripts do not re-prove
those estimates, establish a global inverse, solve a PDE, or certify Yau26.

The interpreter used resolves to:

`/data/qiushi/runtime/releases/gpu-python-3-12-13-c5028c26082aae76bb0d68b42399085e0112394cf9a7fd14adcfb89cea5a1af1/bin/python`

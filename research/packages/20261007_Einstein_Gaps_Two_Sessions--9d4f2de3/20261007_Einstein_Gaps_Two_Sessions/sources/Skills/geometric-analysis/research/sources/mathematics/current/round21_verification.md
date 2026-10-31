# Round 21 verification

22 September 2026. Local research branch local/yau26-round21-20260922,
based on commit 0e25de5. No installed Skill, running service or research
Session was changed.

## Executed checks

Python 3.12.13 and SymPy 1.14.0. From this directory:

    /data/qiushi/qiushi_engine_v09/.venv/bin/python round21_analytic_check.py
    /data/qiushi/qiushi_engine_v09/.venv/bin/python round21_comparison_check.py
    /data/qiushi/qiushi_engine_v09/.venv/bin/python round4_rigidity_check.py

All three programs exited with status zero. The scripts also run with an
ordinary Python installation providing SymPy; the interpreter above records
the actual local execution.

The new analytic checker reported:

    PASS: Hessian identity signs and coefficients on a nonabelian connection
    PASS: full twelve-variable Weyl-divergence contraction
    PASS: zero-order divergence coercivity, full twelve-variable PSD matrix: {15/4 - sqrt(193)/4: 4, sqrt(193)/4 + 15/4: 4, 0: 4}
    PASS: polynomial weighted identity and calibrated constant 1/16
    PASS: general-amplitude identity, both calibration branches, and Hodge endpoint
    PASS: both Einstein signs and the signed Kahler calibration

The comparison checker reported:

    PASS: signed Einstein-ray optimization
    PASS: trace-free and scalar-variance decomposition
    PASS: realized product-surface ratios approach 1/3 strictly below
    PASS: b+=1 topology and integer separation
    PASS: closed-band pointwise constant; endpoint kept distinct

The inherited checker reported:

    Exact round-four rigidity checks passed.
    Truncation scalar cost: 117/4
    Residual bound coefficients before rounding: 44/27 1724/9 24586/3
    Integral-family coefficient: 1215
    Optimal negative Einstein scale: lambda=-R2/S

The last line uses the positive magnitude of the negative Einstein scale;
the new comparison note instead uses a signed \(\lambda\), with optimizer
\(\lambda=R_2/S\). These are the same optimization convention after changing
the sign of the parameter.

## Analytic and source review

The main investigator and a separate reviewing agent checked the bundle
Hessian identity, the curvature action on \(\Lambda^+\), the amplitude
integration by parts, weak Bianchi testing, the pointwise derivative
coercivity, the parameterized contraction, and the Kähler endpoint.
The derivative estimate removes closedness from the assumptions; the
small-amplitude region is handled using its relative volume and the
fourth-power gradient bound. The signed corollary was checked by a
second analyst after the main investigator derived it.
The written arguments, not the program outputs,
establish the analytic claims.

Primary-source checks used:

- [LeBrun, *Ricci Curvature, Minimal Volumes, and Seiberg–Witten Theory*,
  arXiv manuscript](https://arxiv.org/pdf/math/0003068): polarized input,
  Proposition 3.2, Theorem 3.3, Corollary 3.4, and the separate absolute
  Ricci-energy computation. The Stony Brook copy is the same manuscript,
  not an independently checked published edition.
- [Li–Liu, *Uniqueness of symplectic canonical class, surface cone and
  symplectic cone of 4-manifolds with \(b^+=1\)*](https://arxiv.org/pdf/math/0012048):
  the chamber discriminant and the negative-chamber canonical
  nonvanishing statement in Section 2.1 and Theorem 2.2.

The chamber and comparison reviews also checked the nonvacuous
product-surface family, the integer limitation for \(b_+=1\), the
Ricci-flat exception in the defect definition, and the strict threshold.

These are exact algebra checks and bounded proof reviews. They are not a
Lean formalization, a certification of all earlier research, or an
exhaustive literature-priority search.

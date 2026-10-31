# Period-inertia deduction: local verification

Date: 2026-09-23. Baseline: `8113dd10c97d2bac242075a78ffa896c55bc588c`.
Branch: `local/yau26-period-global-20260923`.

The new note proves constant-sign alignment of actual positive Chern periods
under the endpoint deficit and a quantitative scalar Poincare bound. Its
main cup consequence is a bound on the second largest eigenvalue of the
normalized intersection matrix. Its matrix decomposition retains the
uncontrolled negative Gram matrix. It assumes neither common positive
class square nor a lower bound by `2 chi + 3 tau`.

Verification performed:

- Read the endpoint application's hypotheses, normalization, harmonic
  alignment, Weyl fit and first derivative estimates.
- Compared with Round 18's full-intersection polytope and scalar covariance
  theorem, and Round 2's measurable alignment and Walsh argument.
- Ran `python3 line1_period_inertia_check.py`: all 31 exact checks passed.
  These check finite tensor/phase algebra, constants, normalization,
  polarization and a positive/negative Gram model. They do not prove the
  endpoint gauge/PDE input or replace the analytic proof.
- Ran `git diff --check`: passed.
- An independent agent read the proof and checker. It checked the phase
  inequalities at zeros, Poincare use, constants, finite-sign subsequence,
  Hodge normalization, min--max, pair obstruction, spectral alternative,
  and the exact common-functional refinement. No blocking mathematical
  defect was found. Its wording correction, replacing "equivalent matrix
  form" with "matrix form", was applied; the displayed matrix bounds are
  consequences rather than an exactly reversible formulation of (3).
- Verified the classical endpoint source against LeBrun's primary paper,
  *Ricci Curvature, Minimal Volumes, and Seiberg--Witten Theory*, Theorem 2.3
  and Proposition 4.1. The latter contains the beta-two curvature functional
  and cscK equality statement. Source:
  <https://www.math.stonybrook.edu/~claude/min.pdf>.

Scope: this is a deduction from the existing actual endpoint supply, in a
different hypothesis regime from Round 18. It is not a claim of new gauge
solvability, a new realized topology, an unconditional full-cup rank-one
theorem, or nonexistence of all Einstein metrics. The algebraic negative
Gram example is explicitly not presented as an actual monopole example.

All files and history remain local. No running instance, research data,
or shared runtime was changed.

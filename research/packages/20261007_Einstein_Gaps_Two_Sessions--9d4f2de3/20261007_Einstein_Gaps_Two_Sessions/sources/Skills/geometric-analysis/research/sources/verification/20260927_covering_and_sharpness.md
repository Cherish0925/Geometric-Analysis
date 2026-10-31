# Covering, sharpness and ALE matching: proof and verification record

27 September 2026. Base `46e7efc`.
Local branch: `local/yau26-global-cost-20260927`.
Unified [proof](../continuation/20260927_covering_geometry_and_sharp_subfamilies.md).

## Mathematical changes

I43 strengthens base collapse to collapse of genuine local universal
covers, in normalized upper mean. Its proof averages the covering-ball
contradiction by original-metric geodesic flow, with no sheet bound.
CFG comparison covers and bilipschitz path lifting allow the geometric
input to be supplied by a different, uniformly equivalent metric.
Li II smoothing then gives a genuine approximate-input gap under uniform
fixed-scale local L2 nonconcentration, and hence under uniform local
L^(2+eta) control. Actual fields are never moved to the smoothed metric.
The same gap strengthens the upper energy wall without diameter.
Maximal local fibered rank and specified elliptic curvature equations
give two other rigorously scoped geometric inputs.

I44 determines the exact all-metric infimum on the real handle-only
complex-hyperbolic surgery family, including nonattainment for
0<h<1/3. This is an explicit deduction from classical budgets and
gluing, not a claim to a new gluing method. For general blowup/handle
metrics, signature cancellation removes all scalar cap cost from a
sufficient coefficient-four criterion. Relative transgression computes
the precise minimum for full conformal CH collars. An explicit smooth
four-ball example proves that round induced boundary alone cannot give
a cheap full-collar-compatible cap.

The I39 extension begins with the actual local positive-charge cores
and asks about global matching. It excludes a global first-order ALE
limit with finite first-order curvature energy and bounded physical
derivative, retaining all connection sources. The initial pointwise
decay assumption was removed using an L4 primitive for exact L2 chiral
forms. Root then weakened exact Einstein to first-order trace-free
Ricci o(epsilon); physical bounded Ricci supplies that condition.
The two reviewers checked the stronger formulation and its scale factors.
Global first-order compactness and same-scale matching remain hypotheses.

## Primary-source scope checks

- [Naber--Zhang](https://arxiv.org/pdf/1412.1326), Proposition 5.9,
  printed pp.53--54: specified Ricci-limit model and maximal fibered
  fundamental-group rank imply local covering volume. Not their stronger
  harmonic-radius theorem with different splitting requirements.
- [Cheeger--Fukaya--Gromov](https://www.ihes.fr/~gromov/wp-content/uploads/2018/08/384.pdf),
  definition (1.1.4)--(1.1.5), p.331; Theorem 1.3, p.332; proof of cover
  injectivity, p.365. Genuine normal covers are essential here.
- [Li II preprint](https://arxiv.org/pdf/0911.3104), Theorem 1.1,
  Section 3 and (3.8): fixed-scale small unnormalized full-curvature
  energy, definite-time smoothing, and factor-two metric comparison.
  The preprint is worded for complete noncompact metrics. The
  [published abstract](https://link.springer.com/article/10.1007/s10455-011-9290-0)
  explicitly states the compact version; its full publisher text was not
  retrieved. The proof records the direct compact bootstrap adaptation
  and its proper-ball safeguard. No inaccessible statement is silently
  treated as fully read.
- [Weber](https://nyjm.albany.edu/j/2017/23-64p.pdf), Theorem 1.1:
  collapse-independent small-energy regularity for the specified
  elliptic metric classes, not all bounded-Ricci metrics.
- [LeBrun](https://arxiv.org/abs/math/0003068): scalar/projection budget,
  Ricci-energy gluing and its upper sequence remain classical inputs.
  The precise inherited scalar/volume limits are used, not merely the
  Ricci-energy infimum without a compatible sequence.

The full Li I local theorem was not obtained in the bounded source
search. The general approximate Euler-density-only extension therefore
remains unproved; the local-smoothing abstract does not certify it.

## Parallel derivation and cross-review

Three clean-context GPT-6 Astra/max agents worked read-only. Root alone
edited the local project, preserving the frozen source tree and avoiding
concurrent file overwrites.

- `endpoint_geometry_20260927b`: genuine covering volume, source scope,
  comparison-metric bridge, Li smoothing and supercritical input. After
  the first result, continued to weaker geometric hypotheses and reviewed
  the completed Sections 1--4.1.
- `sharp_cost_20260927b`: all-metric handle formula, signature cancellation,
  exact conformal-collar cost and explicit round-boundary obstruction.
  Subsequently reviewed the sourced ALE proof and its finite-energy
  upgrade independently.
- `global_torsion_20260927b`: signed-degree matching, first-order sourced
  ALE theorem, replacement of pointwise decay by finite energy, and the
  approximate-Ricci extension. Subsequently checked the cover averaging
  and sharp surgery identities.

Root independently checked the main algebra, Cartan sign/normalization,
ALE primitive construction, and primary-source hypotheses. Review fixes
included upper integrals rather than unsupported measurability, full
Spin-c trivialization rather than an unspecified flat determinant twist,
physical versus rescaled Ricci norms, and preserving the scalar branch
of the canonical weight.

Subagent agreement is not external mathematical certification. The
arguments, scopes and citations above are the reviewable evidence.

## Finite validation

- `python3 tools/check_mixed_current.py`: 26 tests passed, including four
  new checks for handle/signature defect, Weyl-only cap cancellation,
  curvature/Euler normalization and the explicit round-boundary flux.
- `python3 tools/check_actual_topological_cost.py`: 7 tests passed.
- `python3 tools/check_boundary_compatibility.py`: 7 tests passed.

These check finite identities only. They do not prove compactness,
Ricci-flow estimates, actual nonvanishing or worldwide novelty.
Separate integration checks passed: 89 distinct catalogue IDs with
existing proof paths and dependencies; 242 local links across the six
changed Markdown entry/proof/evidence documents; no unexpected control
characters; and `git diff --check`. A literal form-feed in an initial
formula draft was detected and corrected before these final checks.

## Continuation boundary

The balanced family's all-metric coefficient is still open, even though
its linear order is already proved and a different subfamily now has an
exact infimum. The general weak zero-Weyl endpoint is open outside the
newly verified geometric/first-order classes. First-order ALE hypotheses
are not deduced from normalized global budgets. Intrinsic round boundary
does not prescribe the full extrinsic collar, and a costly prescribed
cut does not exclude a better cut. Fixed E_D and full Yau26 remain open.

The project mathematics Skill guided actual-class/weight quantifiers,
normalization and local-to-global distinctions. No installed Skill,
immutable source, live service or external destination was changed.
No new web-upload packet was prepared.

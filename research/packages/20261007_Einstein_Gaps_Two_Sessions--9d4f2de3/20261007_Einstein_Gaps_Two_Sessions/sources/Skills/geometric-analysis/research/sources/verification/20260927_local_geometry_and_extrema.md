# Local geometry, marked annuli and variational extrema

27 September 2026. Base `cee6c6b`.
Local branch: `local/yau26-variational-global-20260927`.
Unified [proof](../continuation/20260927_local_geometry_and_variational_extrema.md).
No web-upload package was produced.

## Mathematical changes

**I45** closes the bounded-Ricci Euler-density endpoint theorem left open
by I43. The new use of Cheeger--Tian's bounded-Ricci covering extension
removes all-center small-energy and special elliptic-metric premises.
Euler/Fubini selects a positive-volume set of low-energy centers; local
isometries and original-metric Liouville measure transfer the forbidden
mode back to the closed manifold. Splicing the tail with the inherited
finite pencil improves its exponent from beta^{-4} to beta^{-2}, with
the stated numerator. The corresponding compactified weight is t rather
than t^3. Pointwise Ricci and the Euler-density bound remain in scope.

Continuation after that proof derives the Euler budget from the
topological ratio chi/T_+ in the small-defect regime. Noether's inequality
then supplies a universal ratio bound on the entire subcritical
minimal-general-type surgery family. Combining with the old critical-band
obstruction proves the universal pointwise pencil inequality for every
metric and all surgery counts in that actual-input family. A separate
characteristic calculation locates the remaining bounded-Ricci escape
in divergent negative-chiral Chern/Weyl density and chi/T_+; it cannot
occur on fixed topology. The pure integral problem is still different.

**I46** directly controls marked quotient annuli without first-order ALE
compactness. Calibration supplies the uniform integrability needed for
critical Dirac compactness. The limiting pair of parallel spinors allows
exactly odd cyclic 1/n(1,-2), with two determinant classes. Forbidden
positive-spinor lifts yield stronger counts: individually amplitude-
calibrated annuli cannot occur with positive density, regardless of their
small radii. Equivariant local solutions of the actual weighted equations
on hyperbolic quotient balls realize both allowed lifts. Their losses
vanish uniformly across all inner annular scales, so these exceptions
cannot be removed by another local inequality of the proposed kind.

The coefficient work extends I41/I44, rather than counting every formula
as a separate result. The infimum below one is exactly the sharp positivity
parameter of a quadratic-curvature functional. Hypothetical smooth
minimizers have a specific constant-scalar stationary equation and cannot
be Bach-flat, Kahler or Ricci-parallel when their defect lies in (0,1).
Directional-cost formulas apply to weak unit forms and arbitrary smooth
self-dual forms, including their zeros. They prove the coefficient-four
bound for all Hermitian metrics, but do not supply small directional cost
for the balanced surgery family.

## Sources and analytic scope

- [Cheeger--Tian](https://doi.org/10.1090/S0894-0347-05-00511-4),
  Theorem 0.8, printed p.489, and Remark 8.22, p.515; covering geometry
  in Remarks 2.7 and 4.8, pp.501 and 507. Relevant original pages were
  read from the [institutional collection](https://www.math.stonybrook.edu/Courses/MAT683/201001/MAT683S10.pdf).
  Theorem 0.8 is a one-ball hypothesis; no global collapse assumption
  is imported. Remark 8.22 gives C1-alpha/W2-q covering geometry for
  bounded Ricci, not a full pointwise curvature estimate.
- [Lott, Section 3.1](https://math.berkeley.edu/~lott/4d3.pdf) independently
  uses Theorem 0.8 and Remark 8.22 in the bounded-Ricci context. This was
  corroboration, not a replacement for reading Cheeger--Tian.
- [Armstrong, Theorem 3.3.5 and pp.70--72](https://johnarmstrongmaths.com/publications/resources/thesis.pdf):
  the ASD Einstein almost-Kahler obstruction used here is local. It is
  not a claim to the general negative Goldberg conjecture.
- [Haydys, Example 121(b)](https://haydys.net/misc/IntroGaugeTheory_LectNotes.pdf):
  the Spin-c(4) representation convention. The exceptional cyclic types
  and determinant restrictions are computed explicitly in the proof.
- [Catino, Section 2](https://www.mate.polimi.it/wp-content/themes/mymate/send_new.php?file=qdd205&tipo=1):
  classical quadratic-curvature first variations. Its tau>=-1/4 rigidity
  range does not cover the new variational parameter tau<-1/4.
- [Liedtke, Theorem 2.1](https://arxiv.org/pdf/math/0702548) and
  [Bauer--Catanese--Pignatelli, p.5](https://www.mathe8.uni-bayreuth.de/de/team/prof-fabrizio-catanese-old/pdf/101.pdf):
  the full minimal-general-type Noether inequality and characteristic
  identities, with no regularity or ampleness premise. They provide the
  automatic Euler-ratio bound, not a new gauge solvability theorem.

The direct compactness argument inside the CT charts is included in the
proof. Bounded Ricci upgrades the vanishing L2 residual to each finite
Lp; harmonic-coordinate elliptic estimates give strong interior metric
convergence. No Ricci derivative estimate or complete extension of the
upstairs chart is required. The model parameter is constant. The fixed
physical scale chosen from the density bound is not discarded by a false
scale-invariance claim for the entire residual.

## Parallel derivation and independent checks

Three clean-context GPT-6 Astra/max agents worked read-only while root
alone edited this task's branch.

- `local_smoothing_euler_20260927c` developed the bounded-Ricci Euler
  extension, checked the full parameter splice, and independently audited
  Sections 2--2.4. A second pass re-read the precise original regularity
  and Armstrong hypotheses and verified the local-isometry averaging.
- `multiscale_matching_20260927c` developed the annular compactness and
  packing argument, classified all free quotient holonomies, continued
  to the one-spinor marked-class count, and constructed both local
  resonant solutions. It also independently checked the variational
  identities in Section 1.
- `balanced_coefficient_20260927c` developed the directional and weak-form
  coefficient criteria, checked Section 1, then independently reviewed
  critical compactness, packing scales, marked characters, and the actual
  equivariant contraction and long-neck estimates.

Root checked the primary regularity input, integrated the proofs, and
derived/checked the algebra and final scope. Review corrections included
explicit constant t and closedness, retaining harmonic-chart regularity,
distinguishing the S^- representation from S^- tensor L, preserving
physical orientation, and using outer-scale rather than inner-scale
errors in the local long-neck construction. No unresolved analytic
objection from these reviews was promoted to a theorem. This is internal
proof review, not external certification or a worldwide priority finding.

## Finite and integration validation

- `python tools/check_mixed_current.py`: 35 tests passed. Nine additional
  checks cover the variational parameter, directional costs, form scaling,
  compactified exponent, cyclic characters, Clifford seed, physical
  annular exponents, surgery Euler ratio, and the opposite-bundle densities.
- `python tools/check_actual_topological_cost.py`: 7 tests passed.
- `python tools/check_boundary_compatibility.py`: 7 tests passed.

These are finite algebra checks, not proofs of compactness, regularity,
actual global solvability or novelty. Catalogue, links and whitespace
passed separately: 91 distinct catalogue IDs with existing proof paths
and dependencies, 269 local links in the six changed Markdown files,
no unexpected control characters or repeated equation tags, Python AST
parsing, and `git diff --check`. Links are rechecked after final additions.

## Exact continuation boundary

The unrestricted integral-Ricci zero-end theorem remains open. The new
bounded-Ricci theorem forces chi/V to diverge in a hypothetical endpoint
sequence in that class; it does not create pointwise Ricci control.
The annular theorem does not supply a global neck decomposition, its
markings, bounded overlap or amplitude calibration. The local exceptions
still need smooth filling and global matching. The balanced-family
all-metric coefficient remains undetermined; the new cost formulas
identify a sufficient directional estimate, not its automatic validity.
Fixed E_D, diameter-free exact realization and full Yau26 are not decided.

The project Skill was used for actual-class/weight quantifiers and norm
conventions, not as a restriction on methods. No immutable manuscript,
installed Skill, live service or external repository was changed.

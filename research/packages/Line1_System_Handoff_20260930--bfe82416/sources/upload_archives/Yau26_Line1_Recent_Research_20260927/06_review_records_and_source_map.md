# Prior verification records, current scope, and source map

Research snapshot: 844e62f7304d9f890914a6a4370ec39291ddc26e.

Full internal review records, not executable scripts or logs. They report the checks actually performed at the time; historical open statements are updated by the present guide. Finite checks, proof review and priority comparison are distinct.

Read 00_READ_FIRST.md for superseded statements. Each source below is complete and byte-preserved. Original local links remain relative to their source; locate other texts using Volume 6. Formula numbers restart in each source.


---

## Source 1: 20260927_linear_cost.md

Original path: verification/20260927_linear_cost.md

SHA-256: 6b5cba75dfa7d6ae1a59d563dcf11bf133273ffe147d077bf6c4e86f7dc1fbdf

BEGIN COMPLETE SOURCE

# Linear beta=2 cost: proof continuation and checks

27 September 2026. Base `168bea5269692fce531c4fea72d51a0a5766bb54`.
Local task branch: `local/yau26-mixed-flux-20260927`.
Main proof: [linear cost and small-h order](../continuation/20260927_mixed_current_and_signed_cores.md).

## What changed mathematically

I38 localized the positive topological cost of a hypothetical E=o(h)
sequence but did not exclude it. The new proof, I40, does exclude it.
The bounded KE model annihilates the calibrated actual spinor. Retaining
that cancellation in the exact Hessian identity removes the old additive
volume term. The class-square condition controls determinant ASD energy
by the unknown gradient energy plus the actual defect. Weak Bianchi then
absorbs that unknown energy, rather than assuming its smallness.

This yields Sigma,p-T+ <=C(rV+D2), the required mixed-term estimate,
and the all-metric window E+(U-1-h)+>=c h. The previously realized
small-h family consequently has inf E comparable to h. An explicit
square-shortfall variant retains linear order when the shortfall is
O(Ah). The main theorem does not use the stronger, still open estimate
Sigma<=C(P_Ric+D2). Its rV term includes scalar variation.

The construction-side calculation separately proves a reverse-surgery
cap-energy inequality, with coefficient4 sharp in its specified cheap-cap
class. This is not a claim of optimal coefficient over all metrics.
Nearby-beta transfer and signed-current square completion are direct
corollaries/identities, not additional independent main discoveries.

## Sources and actual dependencies

The new downloaded note was read completely and preserved byte-for-byte;
see [receipt](../guidance/source/20260927_mixed_current_receipt.json).
Its mixed-current refinement, axial cancellation and actual curvature
equation retain their source attribution in Sections1--3 of the proof.

The proof uses the inherited functional pencil's actual conformal supply,
same-solution amplitude, phase and curvature-model bounds; the preceding
actual-cost proof's low-amplitude estimate and scalar-slack identity;
and the bounded-form criterion's exact Hessian, polynomial divergence
and weak-Bianchi formulas. All are linked from the proof. None requires
the not-yet-proved linear conclusion. Classical upper-bound gluing is
used only for the upper half of the final order comparison.

The project mathematical Skill was read in full. It guided preservation of
the actual-class quantifiers and the separation of analytic proof, finite
calculation, scope and priority. It did not supply an automatic theorem
or authorize changing an installed Skill or live research system.

## Parallel work and targeted independent re-derivations

Three clean-context agents used the owner's requested `gpt-6-astra`,
`max`, read-only, on bounded tasks. Root owned all file edits.

- `direct_mixed_20260927`: derived the refined Hessian--Bianchi closure,
  checked the low-amplitude/phase dependencies and the square-shortfall
  extension. It did not assume a Sobolev constant or a curvature derivative.
- `signed_flux_20260927`: independently checked the polynomial model's
  action, exact Hessian signs and curvature norms, Chern--Weil constants,
  noncircularity and signed-current completion; derived nearby-beta transfer.
- `actual_construction_20260927`: independently derived the all-metric
  sign/rescaling branches, constants49/112, feasible frontier, exact family
  asymptotics and reverse-surgery cost. Construction attempts did not produce
  an actual sublinear metric in the stated family.

After integration, all three read the relevant complete sections, not just
the proposed conclusion. Their specific corrections were incorporated:
the family is in §3, Theorem5 of the boundary proof; uniform torsion bounds
require bounded kappa; the shortfall variant explicitly drops the square
condition; and coefficient4 requires h->0 and diagonal gluing errors o(h).
Root separately checked the same-solution dependencies and each absorption.
These are internal mathematical checks, not external peer review.

## Finite checks

- `python3 tools/check_mixed_current.py`: 13 tests passed.
- `python3 tools/check_actual_topological_cost.py`: 7 tests passed.
- `python3 tools/check_boundary_compatibility.py`: 7 tests passed.

The new checks cover exact graded exterior algebra in transgression,
signed square completion, primitive derivatives, model roots, mass,
topological bootstrap constants, all-metric conversion, surgery identity
and the auxiliary Eguchi--Hanson radial profile. They do not certify
PDE existence, integration estimates, all-metric quantifiers or originality.
The finite tests supplement, rather than replace, Sections4--5's proof.

The result catalogue's 85 IDs were checked for uniqueness, dependency
resolution and existing proof paths. Local links in changed proof/navigation
files were checked; the source note's bytes and SHA-256 match the download.
`git diff --check` passed. These are archival checks, not mathematical evidence.

## Retained construction-side tests, not premises of I40

The bounded-spinor Liouville shortcut was rejected. On the standard
Eguchi--Hanson space X=O(-2), the canonical section s_Z of E=O(Z), with
|s_Z|^2=(r^2-a^2)/(r^2+a^2), has an ASD Chern connection: the radial
calculation is r^3(1-a^4/r^4) d(log|s_Z|^2)/dr=4a^2. Tensoring it with
a parallel positive spinor gives a bounded, nonparallel twisted harmonic
spinor. In the framing used by the construction analysis its relative
charge is -2 and determinant ASD energy is 32pi^2. Its cubic torsion is
zero because Phi wedge nabla Phi=0. This is an ideal core, not a solution
of the full positive-weight SW curvature equation, and its charge has the
wrong sign to pay a handle's positive charge. The metric and twisted-mode
background is [Franchetti--Krasnov](https://arxiv.org/abs/2309.08453).

The same analysis found a useful approximate-core flux certificate. On
annuli of radii r_i where |Phi|>=m>0, put w_i=Vol(A_i)/r_i^4,
f_i=int_Ai|F_{S+}|^2 and q_i=int_Ai|nabla Phi|^4. Coarea and Holder
give suitable boundary radii with total absolute flux at most
C(sum w_i)^(1/4)[m^(-1)(sum f_i)^(1/2)(sum q_i)^(1/4)
+m^(-3)(sum q_i)^(3/4)]. Thus O(Ah) annular volume-ratio and curvature
budgets plus o(Ah) quartic budget suffice for o(Ah) flux. The hypotheses
were not derived from arbitrary near-Einstein input and are not silently
inserted into I40. The actual proof instead closes the global spinor budget.

## Continuation and remaining boundaries

The previous saved trajectory ended after a local commit and a final
response. The inspected record did not exhibit a quota or scheduler error,
and it did not establish an independently running continuation process.
No such process or automatic between-turn persistence is claimed here.
In this turn, intermediate current and core results were followed by the
next sufficient estimate, which led to the main closure and its cost variant.

Zero-Weyl weak rigidity remains distinct: beta=2 model annihilation does
not persist there, and a small Dirac residual alone is insufficient.
The stronger scalar-variance-free estimate and the global optimal coefficient
are open; neither is needed for the completed linear-order theorem.
No fixed-E_D Einstein decision, diameter-free realization or full Yau26
solution is claimed. A further clean-context agent was assigned the zero-end
coupled equations, not another review of the completed small-h theorem.

That continuation produced Section8 after the main closure was committed
as `b2653dc`. Agent `zero_endpoint_system_20260927` derived a regularized
coupled Lichnerowicz test at the available norms. Root introduced the
reciprocal scalar test and its Jensen defect; the agent independently
checked it and added the growing-weight scalar test. They give strong
torsion-length convergence in all normalized Lq below2, small-torsion
volume O(sqrt eta), and a net derivative balance with limit64/27.
All statements retain a possible concentrated derivative defect and
possible topological charge on the low-torsion region. The construction
does not require the unweighted Dirac residual to converge in L2.
Root independently checked the test derivatives and curvature signs;
the Clifford defect inequality, reciprocal identity and derivative
square completion have additional finite checks. These extend I39,
not a new zero-end gap theorem.

The signed-flux agent then independently read all of Section8, verified
both scalar-test norms, the weighted Dirac commutator, curvature duality
factor4, smoothness at zeros, the quartic sign and limits64/27 and1/27.
No mathematical correction was needed. It confirmed separately why the
positive S+ ideal-core sign cannot be transferred to S- tensor L: the
latter contains positive uncontrolled opposite-Weyl curvature. This
precise remaining boundary is recorded in (8.12), not hidden by the new
length-concentration conclusion.

Everything remains local. No push, external publication, service or Session
change, installed Skill modification or inherited proof overwrite occurred.
The frozen eight-volume package was not regenerated. Current navigation
identifies I40 separately, so older exported statements do not silently
become the latest research state.


END COMPLETE SOURCE


---

## Source 2: 20260927_conformal_and_endpoint.md

Original path: verification/20260927_conformal_and_endpoint.md

SHA-256: ff105d8c73aa129938dfdf21b46a4e5d84c9db3dd8a278d2fb0ee4da54b4e1ca

BEGIN COMPLETE SOURCE

# Conformal separation and endpoint continuation: evidence record

27 September 2026. Base: `1b9a80d`.
Local branch: `local/yau26-endpoint-continuation-20260927`.
Proof: [conformal separation and zero-end system](../continuation/20260927_conformal_separation_and_zero_end.md).

## Changes to mathematical conclusions

I41 removes scalar variance from the inherited I40 slack theorem by passing
to the negative Yamabe representative and transferring exact conformal
energies back. It is global, retains square shortfall explicitly, and
strengthens the defect to traceless-Ricci anisotropy J. The BF application
is an actual geography/supply family outside the old quadratic band, not
a formal intersection matrix. The new conformal excess identity also
reduces sub-unit minimizing sequences to scalar-normalized metrics.

I42 first proves local coercivity using bounded-Ricci regular charts and
exact ASD/almost-Kaehler incompatibility. Exponential lifting and geodesic
flow averaging remove any base injectivity premise. Cheeger--Tian then
supplies a positive fraction of curvature-regular balls from bounded
Euler density for EXACT Einstein metrics. The resulting upper-energy
margin stays positive through h=1/4. A separate approximate-input result
retains its bounded-diameter hypotheses.

The direct torsion continuation saturates determinant ASD energy against
a bounded model, cancels the opposite-Weyl bulk in the signed Chern
identity, and locates the remaining cost in a critical mixed transition
term. The construction arm solves both local positive-weight gauge
equations and realizes a positive relative charge, with vanishing
quadratic energies but a nonvanishing quartic radial cost. This establishes
an actual local mechanism, not a closed-manifold endpoint counterexample.
The construction was then extended by perturbed right inverses to a fixed
hyperbolic background: Ric=-g, W^pm=0, canonical weight2 and both local
gauge equations hold exactly. Winding, normal-derivative and determinant
curvature matching still require a global exterior.

## Proof dependencies and classical sources

Part I depends on the preceding refined beta=2 theorem, not on an assumed
sharp coefficient. Negative Yamabe theory, conformal invariance, and
Chern--Weil identities remain classical inputs. The exact variational
comparison does not assert pointwise Ricci preservation under conformal
change. The BF family checks the movable geography threshold, the full
Ishida--LeBrun supply hypotheses, all relevant parity conditions and the
class-square inequality.

The geometric proof was checked against the following primary sources:

- [Cheeger--Naber](https://arxiv.org/pdf/1406.6534), Theorem 1.13 and
  Definition 2.9, for bounded-Ricci harmonic-radius input.
- [Armstrong's thesis](https://johnarmstrongmaths.com/publications/resources/thesis.pdf),
  Section 3.3.3, for the local exact incompatibility.
- [Normal exponential cover geometry](https://arxiv.org/html/2601.16176v1#S2.SS3),
  for the fixed-scale lifted metric, with no assertion of a global covering map.
- [Cheeger's author presentation](https://sites.duke.edu/scshgap/files/2016/08/dim4dukebeamer.pdf),
  slides 2--3, for the unnormalized, collapse-independent Einstein epsilon
  regularity used in Theorem 10, and slide 13 for the curvature convention.
  The original paper is [Cheeger--Tian](https://doi.org/10.1090/S0894-0347-05-00511-4).
  Its full publisher PDF was not retrieved in this run; the cited theorem
  statement was read in the author's presentation. No bounded-Ricci-only
  replacement is inferred from that statement.
- [Dirichlet Schauder theory](https://ocw.mit.edu/courses/18-156-differential-analysis-spring-2004/pages/lecture-notes/),
  lectures 11--17, for the local construction's fixed-ball right inverses.

The BF comparison uses [Ishida--LeBrun](https://arxiv.org/html/math/0111228)
and [Braungardt--Kotschick](https://arxiv.org/pdf/math/0306021), with the
already preserved actual-supply proof. Classical shrinking-core upper
bounds retain their LeBrun attribution.

## Parallel work and internal checks

Three Astra/max research roles worked read-only while root integrated the
proofs in one local manuscript. They were given successive concrete tasks,
not repeated requests for a new general roadmap.

- `endpoint_actual_bubbles`: local geometric coercivity, exponential
  averaging, exact Einstein Euler-density extension and uniform wall;
  then checked whether the wall forces new actual topology-only exclusions.
- `torsion_signed_topology`: determinant saturation, signed localization,
  full projected torsion derivatives, positive relative flux, and actual
  local gauge construction.
- `zero_endpoint_system_20260927`: conformal/BF and approximate-wall
  derivations, independent checking of the local construction, and the
  reduced sharp-coefficient problem.

Corrections retained in the text include the reciprocal-mean contribution
to the saturation rate; ordinary versus invariant-weight cover inputs;
moving geography thresholds; the distinction between Hessian norm and
squared integral; actual versus formal examples; and exact versus
approximate Einstein regularity. Agent agreement is not itself evidence
of global correctness; the displayed arguments and source hypotheses
are what a further mathematical review must examine.

## Finite checks

- `python3 tools/check_mixed_current.py`: 22 tests passed.
- `python3 tools/check_actual_topological_cost.py`: 7 tests passed.
- `python3 tools/check_boundary_compatibility.py`: 7 tests passed.
- `git diff --check`: passed.
- Result catalogue: 87 distinct IDs; all source paths and dependencies
  present. Final integration checked 289 local links across the seven
  changed entry/proof/evidence documents; none were broken.

The new finite tests check conformal energy identities, the linear wall,
moving BF arithmetic, determinant-saturation coefficients, exact and
approximate upper-wall reductions, Clifford projection identities,
right-inverse symbols, local torsion polynomials, signed radial integrals
and their limiting constants. These do not prove elliptic compactness,
contraction estimates, actual gauge nonvanishing, or global topology.

## Continuation boundary

The unrestricted weak-error zero endpoint, the all-metric optimal small-h
coefficient, and fixed E_D's Einstein decision remain open. The local core
does not close the exterior matching problem. The uniform upper energy
wall does not by itself force existing smooth families into that wall:
the recorded topology gives an upper bound, not the missing lower pinning.

Section 3.2 further reduces coefficient4 to a precise first-order
three-loss estimate on actual scalar-normalized sequences. Genuine cscK
products bound the existing isotropic estimate's coefficient and show
that merely optimizing it cannot establish4. The sharper three-loss
comparison is retained as unproved, not promoted to the theorem registry.

The project mathematical Skill was read in full and used to preserve actual
input quantifiers, normalization, proof dependencies and the separation of
local construction from global realization. Frozen research originals,
installed Skills and running systems were not modified. No new web packet,
external synchronization or publication was made.


END COMPLETE SOURCE


---

## Source 3: 20260927_covering_and_sharpness.md

Original path: verification/20260927_covering_and_sharpness.md

SHA-256: c4ca515a57a270cb5afda344679595405142e0cac46c9ae72419acb51c4da35b

BEGIN COMPLETE SOURCE

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


END COMPLETE SOURCE


---

## Source 4: 20260927_local_geometry_and_extrema.md

Original path: verification/20260927_local_geometry_and_extrema.md

SHA-256: 8ffa8cc1fe50f6583564caed6e9fa95358d7598e5111697771d4f5dfcc758b41

BEGIN COMPLETE SOURCE

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


END COMPLETE SOURCE


---

## Source 5: 20260927_full_core_and_extrema.md

Original path: verification/20260927_full_core_and_extrema.md

SHA-256: efe4444250e3bd8b1771c8c98ef329ccb3bd501794812bc6304347ecd4a21f54

BEGIN COMPLETE SOURCE

# Full-core cost, elliptic endpoint and extrema: verification record

27 September 2026. Base `0c8059f`; local branch
`local/yau26-resonant-fillings-20260927`.
[Unified proof](../continuation/20260927_full_core_cost_and_extremal_metrics.md).
No web package, external upload, live runtime change or installed Skill edit.

## What changed mathematically

- I47 determines the all-smooth-core curvature-cost infimum for the physical
  resonant quotient left by I46, including arbitrary interior topology.
  Classical scalar-flat Kahler ALE truncations match the lower bound.
  Retaining its sign gives pure-Ricci atoms for minimal-resolution and
  lower-integer branches. A separate faithful-flat-line argument removes
  first-order expansion hypotheses from the corresponding ALE exclusion.
- I48 replaces pointwise Ricci control by a specific elliptic inequality
  and a small normalized local integral lower-Ricci budget. Neither input
  is inferred from arbitrary L2 closeness. Euler density is still required.
- The I44 extension retains all ordinary-SW remainders and links them to
  the full quadratic-curvature gradient. Stationary balanced low-level
  competitors have explicit pointwise and fourth-moment concentration;
  pointwise-near-Einstein csc competitors have a relative gradient lower
  bound. The balanced coefficient and attainment remain undecided.

These are manuscript results with complete arguments in the linked file.
Independent agent review is a check, not external mathematical certification
or a priority finding. No theorem is justified by the number of files/tests.

## Primary inputs actually checked

- [Lock--Viaclovsky](https://msp.org/gt/2016/20-3/gt-v20-n3-p13-s.pdf),
  (1-5), (3-1), (3-5): positive-cotangent eta convention and ALE formulas.
  The boundary sign is fixed explicitly; reversing orientation changes
  the conclusion. Weyl norms are Hilbert--Schmidt endomorphism norms.
- [Calderbank--Singer](https://arxiv.org/pdf/math/0206229), Theorem A and
  Section 4.1: scalar-flat Kahler ALE metrics on cyclic minimal resolutions.
  This is the matching classical construction, not a new gluing claim.
- [Suvaina](https://arxiv.org/pdf/1102.2672), Lemmas 4.1--4.2, Remark 4.3:
  ALE covering context. The proof instead displays its volume-rigidity
  argument; it does not need a full ALE classification.
- [Moroianu](https://moroianu.perso.math.cnrs.fr/tex/1997cmp.pdf), Lemma 3.1:
  parallel Spin-c curvature identity, hence flat determinant when Ricci=0.
- [Dai--Wei--Zhang](https://web.math.ucsb.edu/~wei/paper/Dai-Wei-Zhang.pdf),
  Theorem 1.1, Corollary 1.5, (2.5)--(2.6), Remark 1.2: normalized Sobolev,
  small local lower-Ricci budget and proper-ball conditions. Finite budget
  alone is not their hypothesis.
- [Tian--Viaclovsky](https://arxiv.org/pdf/math/0310302), early Section 3
  integration-by-parts lemmas: the local bootstrap is written out with one
  fixed outer-ball probability measure. Later global hypotheses are not
  borrowed implicitly.
- [Cheeger--Tian, original institutional collection](https://www.math.stonybrook.edu/Courses/MAT683/201001/MAT683S10.pdf),
  Theorem 0.8 and Remark 8.22, independently re-read: compactly contained
  balls suffice, and the bounded-Ricci extension gives covering geometry,
  not pointwise full-curvature bounds. Apply it inside the good neighborhood
  where Ricci has already been bounded. No ambient global Ricci bound is
  needed at that step.
- [Catino](https://arxiv.org/abs/1404.0569), Propositions 2.1 and 4.1:
  Euler--Lagrange and Cotton identities. The parameter is held fixed during
  variation, the tensor Laplacian sign and full Cotton norm are specified.
- [LeBrun](https://arxiv.org/pdf/math/0003068), ordinary SW/Weitzenbock
  normalization: the present remainder decomposition keeps the losses from
  one ordinary solution; it does not claim a new nonvanishing theorem.

## Parallel work and cross-review

Three clean-context `gpt-6-astra` agents at `max` effort worked read-only;
the root integrated proofs in this single branch.

1. `resonant_filling_20260927d`: full-core eta argument, faithful determinant,
   independent checks of root's sharpness/pure-Ricci extensions; then reviewed
   the normalized elliptic bridge, proper-ball dichotomy, original CT scope
   and local-only Liouville averaging.
2. `sharp_coefficient_20260927d`: same ordinary-solution remainders and
   Cotton concentration; then independently checked root's nonstationary
   gradient extension, its sign and the unrestricted variation normalization.
3. `weak_endpoint_20260927d`: integral-Ricci elliptic bridge; then independently
   derived the ordinary-SW coefficients in a Clifford frame and checked the
   weighted Weyl/Cotton constants and oriented topological budget.

Review changes incorporated: explicitly connected manifold; radii in (3.14)
restricted to `(0,1]`; `u_minus=3T_minus/A` distinguished from the minimum of
two orientations; low-level hypothesis retained; τ frozen during variation;
Hilbert--Schmidt and spectral norms distinguished.

## Executed checks

```
python3 tools/check_full_core_and_extrema.py
Ran 21 tests ... OK

python3 tools/check_mixed_current.py
Ran 35 tests ... OK
```

New checks use exact rational Dedekind sums for odd orders 3--101, continued
fractions, oriented counterchecks, Chern-Weil normalization, resolution
energies, binary/trivalent boundary arithmetic, the full Clifford-frame
Dirac/Hopf coefficients, polynomial loss identities, the signed coefficient
balance, Weyl Cauchy constants, parameter/gradient normalization and the
small-diameter constants. They do not verify the PDE bootstrap, compactness,
ALE existence or full theorem correctness by computation.

`tools/library.py verify` also passed: 884 inherited files, 10,191 source
records and 648 navigation links, with no failures. The result catalogue
has 93 distinct IDs, all proof paths and dependencies present. These counts
measure archive integrity and navigation, not mathematical contribution.
`git diff --check` passed.

## Remaining decisive steps

The raw weak input does not yet force an embedded complete marked-core
decomposition. Uniform full-core cost does not bound Euler characteristic
when quotient orders grow, and normalized counts do not exclude finitely
many cores in growing volume. The elliptic equation and small local Lp
budget are not supplied for general approximate metrics. The signed balance
(4.16) still needs a proof or a same-family construction changing its sign
at scale Ah. No fixed Dehn-twist Einstein decision, unrestricted integral
endpoint theorem, balanced optimal coefficient or full Yau26 solution is
recorded.


END COMPLETE SOURCE


---

## Source 6: 20260927_signed_balance_and_flow.md

Original path: verification/20260927_signed_balance_and_flow.md

SHA-256: 2c5a5b3a335b43dd5168b27e2429c141dad9a4689eaa50954a8db11e605a1e5e

BEGIN COMPLETE SOURCE

# Signed balance and conformal flow: proof and verification record

27 September 2026. Base commit 754bc3a; local branch
local/yau26-signed-balance-20260927.
[Unified proof](../continuation/20260927_signed_balance_and_conformal_flow.md).
No upload packet, external publication, running-service change or installed
Skill update was made. The frozen mathematical baseline is unchanged.

## Mathematical changes

**I49: actual evolution from static budgets.** The classical scalar-preserving
conformal Ricci flow has volume derivative minus trace-free Ricci energy.
The established all-metric gap, classical Ricci lower bound and opposite
Chern--Weil wall give three simultaneous differential inequalities.
Their explicit integration bounds maximal smooth lifetime uniformly for
the realized balanced small-h family, even though its integral gap tends
to zero. The starting near-minimizing metrics exist with an explicit slack;
an attained minimizer or preserved pinching is not assumed.

The Cotton/actual-field argument additionally gives genuine flow descent
inside a specified pointwise tube. A finite tube-escape time is not a
description of the eventual singularity and is not ordinary Ricci-flow
convergence.

**X06: a real sharp boundary for signed spinor payment.** Anti-Hermitian
TT deformations of negative KE products, followed by negative Yamabe
normalization, admit actual unperturbed ordinary SW solutions. The
gauge-fixed linearization is checked both by the classical divisor
description and by an explicit sum-of-squares identity. Its metric source
vanishes at first order; mixed connection variation produces nonzero
directional spinor energy.

On one fixed smooth product, degenerating the second surface gives actual
small Laplace eigenvalues. A diagonal small perturbation then gives
signed remainder/Weyl loss tending to two and Ricci/Weyl loss tending to
zero. Together with the exact upper bound at h=0, this determines the
sharp coefficient of the Weyl payment even allowing a fixed Ricci term.
The construction has h=0,U=3; it does not refute the balanced h>0
coefficient-four target.

**Variational and endpoint interfaces.** The full Hessian is completed
in TT/conformal variables, without substituting an Einstein-background
formula at a non-Einstein critical metric. Pure conformal directions are
positive and stability reduces to a specified TT quadratic form.

The stationary endpoint theorem retains a global Sobolev inequality and
explicit topology bounds; its elliptic equation is derived from the
actual quadratic-curvature Euler--Lagrange equation. A separate
noncollapsed maximal-curvature extraction gives terminal Ricci-flat ASD
ALE metric cores. Same-scale nonzero field control and an entire surgery
core are not inferred from this metric extraction.

## Primary inputs checked

- [Lu--Qing--Zheng, A Note on Conformal Ricci Flow](https://arxiv.org/pdf/1109.5377),
  Theorem 1.1, equations (1.1), (1.2), (2.3): short-time existence,
  pressure equation and classical volume variation. Laplacian signs
  and scalar-minus-four normalization were converted explicitly.
- [Okonek--Teleman](https://library.slmath.org/books/Book37/files/okonek.pdf),
  Theorem 3.1.2, printed pp. 413--414: canonical negative-Kahler
  empty-divisor solution. The proof also supplies a direct kernel
  calculation; nonlinear uniqueness alone is not used as regularity.
- [Scala](https://www.numdam.org/item/10.5802/aif.2640.pdf),
  Theorem 3.3 and Section 4, printed pp. 1274--1276: metric derivatives
  of Dirac and SW curvature equations. The path tensor and the
  endomorphism variation have the requisite factor of two.
- [Catino](https://arxiv.org/pdf/1404.0569), equation (2.1):
  quadratic-curvature critical equation. Constant scalar is retained,
  including the parameter where the trace equation alone degenerates.
- [Anderson](https://arxiv.org/pdf/math/0312111),
  Theorem 1.1 and Proposition 3.5: Sobolev/energy compactness for the
  stated elliptic Ricci system. This is not Einstein compactness
  applied directly to arbitrary approximate metrics.
- [Bando--Kasue--Nakajima](https://doi.org/10.1007/BF01389045):
  ALE structure is invoked only after obtaining a complete exact
  Ricci-flat limit with finite curvature energy and Euclidean growth.

The hyperbolic collar and Rayleigh construction is written explicitly.
Classical existence/regularity results are inputs, not claimed as new.
The catalogue records manuscript proofs, not global priority or external
certification.

## Parallel construction and independent checks

Three clean-context GPT-6 Astra agents at max effort worked read-only.
The root wrote and integrated the proof in this single task branch.

1. signed_spinor_balance_20260927e constructed the genuine SW
   deformation, proved the signed simplification, and continued from
   a fixed-background positive ratio to a fixed-smooth-manifold sharp
   Weyl-payment sequence.
2. variational_attainment_20260927e derived the conformal flow equations
   and full Hessian. It independently checked the actual SW path,
   invertibility, variation coefficients and sharpness ratios, then
   reviewed Sections 1--4 of the written proof.
3. core_extraction_20260927e proved the stationary/Sobolev endpoint and
   maximal-curvature core extraction. It independently rederived the
   flow cancellations, all wall integrals and the tube estimate, then
   reviewed written Sections 1, 2, 5 and 6.

Review changes incorporated:

- use an actual nonempty near-minimizing initial window with slack, not
  an upper infimum that might be unattained;
- distinguish the specified opposite-orientation budget from an
  unlabelled minimum;
- freeze the quadratic-functional parameter during each variation;
- prove the ratio bound at every smooth flow time, not only initially;
- retain shrinking individual SW implicit-function radii in the
  degenerating-background construction;
- pass to a convergent positive-volume subsequence before restoring
  physical scale in the compactness argument;
- justify the Ricci-flat limit's single end and the whole-truncation
  signed-energy bound;
- do not transfer a metric blow-up to a normalized nonzero spinor
  without the required rescaled error estimate.

The project Skill was read for the actual-class, auxiliary-weight and
norm conventions. It was neither edited nor treated as a restriction on
new proof methods.

## Executed finite and integrity checks

The commands below both passed:

    python3 tools/check_signed_balance_and_flow.py
    Ran 18 tests ... OK

    python3 tools/check_full_core_and_extrema.py
    Ran 21 tests ... OK

The new checks cover pressure/gradient cancellations, defect evolution,
wall normalization and intersection order, integration and asymptotic
time constants, nonempty-window slack, the tube rate, actual remainder
polynomials, the canonical solution square completion, mixed connection
norms, sharpness ratios, the collar integral, full Hessian completion,
and endpoint volume/model constants. They do not prove PDE existence,
compactness or correctness of the entire theorem by computation.

The result catalogue has 95 distinct IDs with all proof paths and
dependencies present. A formatting check finds no control characters and
balanced inline/display mathematical delimiters in the new proof.
Archive integrity and local navigation are checked by the existing
library verifier; its machine-readable receipt is
[catalog/verification.json](../catalog/verification.json).
The final run passed: 884 inherited files, 10,191 source records and
654 local navigation links, with no failures. These are preservation
counts, not counts of mathematical contributions. The initial navigation
check preceded this receipt's creation and reported that one missing
link; after writing the receipt, verification passed. The final
whitespace check also passed.

## Exact remaining questions

The balanced h>0 coefficient requires its full signed comparison at
scale Ah, or a different argument controlling all metrics. The h=0
sharp model proves the universal shortcut false, not this target false.
The reduced TT Hessian has not been proved indefinite.

For the unrestricted weak zero endpoint, neither exact stationarity nor
the stated Sobolev/noncollapse assumptions follow from raw averaged
budgets. A metric terminal core and an actual calibrated field on that
core are distinct outputs. The field-survival estimate and full
marked matching remain open.

The flow bound does not classify the forced breakdown, give a uniform
lower existence time, or settle fixed E_D. No complete Yau26 conclusion
is claimed.


END COMPLETE SOURCE


# Current result scope and source coverage

These catalogue entries are reading metadata, not additional proofs.

The snapshot catalogue had one missing JSON comma at I48. It is repaired in this packaging branch without changing any mathematical text.

## Commits since the last baseline

b2653dc Prove linear small-surgery Einstein separation by refined spinor self-test
1b9a80d Continue zero-end equations with torsion length concentration and weighted balance
46e7efc Extend conformal Einstein separation and geometric zero-end theory
cee6c6b Extend Yau26 covering coercivity, sharp surgery costs and ALE matching
0c8059f Prove bounded-Ricci endpoint bridge and actual annular matching bounds
754bc3a Prove sharp full-core costs and connect actual fields to extrema
844e62f Connect integral gaps to conformal flow and prove sharp actual Weyl payment

## I38: Actual weighted-spinor cost and signed Chern concentration

status: manuscript-theorem

scope: The inherited actual beta=2 conformal-monopole supply and small normalized kappa=r+D2/V, with its fixed class through all positive weights. The small-h consequence uses precisely the previously realized two-chirality-window family.

statement: An exact constant-rescaling identity gives 8sqrt(6)K_A=Sigma+O(kappa V). Signed Chern transgression gives c2(S+)<=C(kappa+epsilon)V+C integral_{1/2<rho<1}|nabla_A Phi|^4. Thus E=o(h) on the specified family requires leading projective L2 energy outside the small-amplitude set and quartic energy at least cAh in a transition layer of volume and L2 energy o(Ah), forcing gradient blowup there.

boundary: This result was a necessary-concentration theorem. I40 subsequently excludes that concentration under the stated actual beta=2 square/window hypotheses and proves the linear lower bound. Its refinement to a radial/phase mixed term is attributed to the 27 September web note, not counted as an independent local discovery.

## I39: Actual cubic torsion and opposite-spinor weak Dirac bridge

status: manuscript-theorem

scope: The same actual weighted positive spinors along a hypothetical beta->infinity, kappa->0 sequence, with a^2>=T+ for the inherited uniform Hessian budget. A separate local construction solves the actual positive-weight equations on shrinking Euclidean or fixed negative-hyperbolic balls, without global class supply or boundary matching.

statement: The smooth cubic torsion obeys an exact opposite-spinor Dirac identity and a coupled actual curvature relation. Its Dirac residual vanishes in normalized Lq, q<2. New scalar tests strengthen its mean mass to |t|^2->128/81 in every normalized Lq, q<2, at the zero endpoint, and bound the relative volume of small torsion by C sqrt(eta). A globally regularized coupled Lichnerowicz identity identifies a net derivative cost tending to64/27 without presuming a small critical L2 residual.

boundary: Local actual positive-charge cores remain possible. The latest continuation excludes matching through a global first-order hyperkahler ALE limit with trivial full positive background, finite first-order curvature energy and bounded physical derivative (or torsion/current). Exact Einstein is unnecessary; physical bounded Ricci suffices for first-order chirality. The first-order/global hypotheses are not supplied by averaged endpoint budgets. Bare signed degree is only the relative Euler obstruction for sections, not actual differential matching. No closed counterexample or unrestricted endpoint gap follows.

## I40: Linear actual-spinor cost and sharp small-h Einstein separation

status: manuscript-theorem

scope: Closed oriented four-manifolds with actual conformal monopole supply fixed through all auxiliary weights. Beta=2, p>0, a^2>=T+, kappa=r+D2/V<=1 for the analytic theorem; metricwise p>=A and T+=A(1-h), 0<h<=1/3 for the all-metric conclusion.

statement: The bounded KE curvature model annihilates the calibrated spinor, yielding Hessian-plus-quartic energy <=C(K+Theta+B). The square condition bounds B by K+Theta; weak Bianchi and polynomial divergence coercivity absorb K. Thus Sigma,p-T+<=C(rV+D2) and mixed critical energy <=CTheta. Every metric satisfies E+(U-1-h)+>=c h. The realized h->0 family has c1 h<=inf E<=4h/(1+h). A class-square shortfall y gives c h^2/(h+y); low-cost reverse surgery identifies coefficient4 only within its stated replacement class.

boundary: This determines order, not the optimal leading coefficient over all metrics or publication priority. I40 itself retains scalar variance in rV; I41 subsequently removes it by conformal transfer. Beta=2 model annihilation does not settle the zero-Weyl endpoint. Actual gauge suppliers remain explicit; no compactness or new supplier is presumed.

## I41: Scalar-free conformal separation and realized linear energy windows

status: manuscript-theorem

scope: Actual positive conformal-monopole input with p>0; arbitrary smooth metrics and explicit square shortfall Y=(T-a^2)+. All-metric applications use metricwise p>=A, T=A(1-h). Necessary invariant-weight covering input is retained.

statement: Negative Yamabe transfer of I40 proves Sigma<=C(P+D2+sqrt((P+D2)Y)) without scalar variance or a small-error premise. If Y=0, e(1+J/18)>=1+(1+c0)h+(2+c0)(p/A-1), J=4P/R. Chiral elimination strengthens the all-metric gap to J; an actual BF geography family lies outside the old quadratic strip but inside the new linear one. Conformal energy identities exactly characterize sub-unit minimizing sequences of E and J.

boundary: The new BF family is an actual exclusion relative to the recorded old window, not a worldwide priority finding or a constructed near-Einstein upper sequence. Conformal control does not preserve pointwise Ricci error. The later positivity-parameter bridge does not prove attainment: any smooth minimizer with 0<inf E<1 would be negative csc and neither Bach-flat, Kahler nor Ricci-parallel. The balanced-family coefficient remains open.

## I42: Zero-end geometric coercivity, curvature-scale degeneration and Euler-density gap

status: manuscript-theorem

scope: Bounded self-dual near-closed forms and constant Weyl-model amplitude t in [0,1/4]. Local bounded-Ricci noncollapse; or bounded sectional curvature with no injectivity premise; or EXACT negative Einstein with bounded chi/V. Actual applications use p>0 and the same supplied form.

statement: Local incompatibility controls the noncollapsed volume fraction. Exponential lifting and Liouville averaging control the curvature-regular fraction without a sheet bound, excluding bounded-curvature collapse. Cheeger-Tian plus Fubini proves D_beta/V>=epsilon(chi/V bound) for exact Einstein and beta>=4, without diameter, volume, noncollapse or class-square bounds. A budget chi/A<=B yields e<=G(h)-c(B) uniformly through h=1/4. Separately bounded-diameter pointwise inputs satisfy delta_-^2+(G(h)-e)+>=c(D) under their stated projection/square input.

boundary: The curvature radius, not pointwise curvature everywhere, tends to zero in measure. I42 itself treated the Euler-density case only for exact Einstein; I45 now supplies the bounded-Ricci approximate extension. Neither gives an unrestricted integral endpoint gap, exact realization or fixed-ED decision.

## I43: Covering-volume coercivity and smoothing-to-endpoint separation

status: manuscript-theorem

scope: Bounded Ricci and bounded actual self-dual forms, model parameter t in [0,1/4]. Fixed positive fraction of local universal covering volume; or complete uniformly equivalent bounded-sectional comparison metric; or pointwise negative near-Einstein input with uniformly small fixed-scale local full-curvature L2 energy. Specified elliptic metrics separately allow bounded Euler density.

statement: Geodesic-flow averaging bounds the good-cover volume fraction by the actual deficit with no sheet count. Zero-end sequences must have local-cover volume tending to zero in upper mean. CFG plus bilipschitz path lifting and Li II smoothing give a diameter-free beta>=4 gap and upper-energy margin under local nonconcentration, including uniform local L^(2+eta) budgets. Naber-Zhang maximal local fibered rank provides another explicit covering input. Weber supplies a distinct elliptic-metric Euler-density extension.

boundary: I43's uniform small local L2 premise is stronger than averaged energy density; I45 removes it in the bounded-Ricci class using the original metric's CT covering regularity. Ricci flow in I43 supplies only a comparison metric; actual fields/errors stay in the original metric. No exact realization or fixed-ED decision follows.

## I44: Sharp surgery subfamilies and the chiral cost of compatible blowdown

status: manuscript-theorem

scope: The established actual class on M=X#k CPbar2#ell(S1xS3), X closed complex hyperbolic, A=c1^2(X), h=(k+4ell)/A. Cap results retain full marked collar compatibility. Exact infimum uses k=0 and 0<=h<=1/3.

statement: The handle-only family has inf_all_metrics E=4h/(1+h), unattained for 0<h<1/3; k=o(Ah) gives asymptotic coefficient4. Signed signature cancellation gives E>=4h/(1+h)-2Cplus/[pi^2 A(1+h)^2], with no scalar cap cost. Every E/h->c<4 sequence forces cap cost at least pi^2(4-c)/2 per Ah. Full conformal CH collars have exactly computable positive minimum cap cost; round intrinsic boundary alone permits arbitrarily large compulsory cost via an explicit smooth ball metric.

boundary: The exact subfamily formula uses classical bounds/construction, not new gluing or a priority finding. Directional estimates give coefficient4 for Hermitian/conditional weak-form inputs. Low-level stationary balanced metrics have liminf delta_minus>=1/(4sqrt2); pointwise-near-Einstein csc competitors have relative quadratic gradient liminf>=1/3. The full Hessian is strictly positive on nonconstant pure conformal directions; possible instability is in the unresolved reduced TT form. X06 forbids universally discarding the Weyl payment, not balanced coefficient4. I49 uses the budgets dynamically without attainment. Balanced coefficient4 remains open.

## I45: Bounded-Ricci Euler-density endpoint gap and improved entire pencil

status: manuscript-theorem

scope: Closed oriented smooth four-manifolds, |Ric|<=K, bounded smooth self-dual form, constant t in [0,1/4], and bounded Euler density. Small defect derives that density from chi/T+; actual p>=A and chi/A<=B is another source. The classical general-type surgery family supplies a uniform bound automatically by Noether's inequality.

statement: avg Z_t>=c(K,L,Lambda0), without diameter, base noncollapse, a global Sobolev bound, Einsteinness, or all-center small energy. CT bounded-Ricci covering regularity, Euler/Fubini selection and Liouville averaging give the proof. The actual entire pencil improves to (1+b_a)(r+D_beta/V)>=c(beta-2)^2/beta^2; special square control removes b_a. For every metric and all surgery counts on the eligible minimal-general-type blowup/handle family, delta_-^2+D_beta/V>=c(beta-2)^2/beta^2 with universal c. Bounded-Ricci zero-end escape must have chi/T+->infinity and opposite-spinor Chern density diverging, not fixed topology.

boundary: Pointwise Ricci remains part of the general geometric theorem; the pointwise defect supplies it in applications. Euler density may be derived from the stated topology, not from unrestricted integral Ricci. Constants are non-effective; improved decay is not claimed optimal. The pointwise family theorem is not an all-metric integral zero-end theorem or a general realization/priority claim.

## I46: Actual annular holonomy costs, marked-class counts and resonant local solutions

status: manuscript-theorem

scope: Orientation-preserving C2-close flat quotient annuli, fixed finite family of free groups and actual restricted Spin-c lifts. Inherited bounded actual spinor and torsion/curvature budgets; bounded overlap for packing conclusions.

statement: Two constant-norm parallel limits are possible exactly on odd cyclic 1/n(1,-2) with the two specified determinant classes. All other marked lifts pay a normalized calibration, determinant-energy or torsion-Dirac cost; critical compactness uses calibration uniform integrability and Vitali. A forbidden positive-spinor lift alone pays amplitude/curvature cost, giving a radius-independent density exclusion for amplitude-calibrated annuli. Both allowed lifts have genuine local weighted solutions on negative-hyperbolic quotient necks, with losses vanishing uniformly across arbitrary inner scales.

boundary: The original averaged budgets do not themselves supply a marked annular decomposition or bounded overlap. Constants are not uniform over unbounded quotient orders. Actual local resonant solutions have an orbifold apex, not a smooth filling or a closed endpoint sequence. Neither a universal endpoint gap nor full global matching follows.

## I47: Sharp full-core cost of the actual resonant quotient and faithful determinant obstruction

status: manuscript-theorem

scope: Entire smooth compact oriented cores with outward conical collar of physical quotient 1/n(1,-2), odd n>=3; or lifted rescaled C2-close collars. Interior topology and quotient order unrestricted. Separate complete Ric>=0 ALE theorem with faithful flat line at infinity.

statement: The infimum over all smooth exact-collar fillings of integral(Ric0^2+4Wplus^2+s^2/12) is 4pi^2(n-1)/n. The lower bound uses boundary integrality; classical scalar-flat Kahler ALE truncations match it on minimal resolutions. Approximate collars cost O(delta^2/n). Small-volume cores force raw actual-defect atoms and bounded-overlap density bounds. Nonpositive integer branches force pure Ricci atoms with no gauge or volume premise. A faithful flat determinant cannot extend over nontrivial smooth Ric>=0 ALE; hence a parallel positive actual spinor alone excludes resonant Ricci-flat ALE filling without first-order hypotheses.

boundary: This is a sharp filling/actual-cost connection using classical models, not a new ALE construction or priority claim. Intrinsic boundary geometry or an orbifold apex is not an entire smooth filling. An actual terminal ALE truncation can be such a filling, but is not thereby the full exceptional/handle surgery region. Cost does not uniformly control Euler number when n grows. Original weak input still does not supply the core decomposition.

## I48: Integral endpoint gaps in explicit elliptic curvature classes

status: manuscript-theorem

scope: Closed connected oriented four-manifolds and bounded smooth self-dual form. First version: bounded Euler density, |rough-Laplacian Ric|<=A|Rm||Ric|, and small k_p(r0)=r0^2 sup_x(avg_Br0 rho_minus^p)^(1/p), p>2; threshold depends on dimension and p, gap also on r0,A and remaining budgets. Alternative version: exact scalar-minus-four Q_theta-critical metrics, bounded theta, global Sobolev inequality with coefficient V^(-1/2), 0<T_plus<=T0 and chi<=chi0. These are different sufficient hypotheses, not automatic consequences of small L2 error.

statement: The first version obtains local Ricci sup bounds and a zero-end gap via normalized Sobolev absorption, curvature bootstrap, Euler/Fubini selection, proper-ball/small-diameter dichotomy and covering averaging, without diameter or noncollapse premises. Escaping elliptic sequences must have normalized lower-Ricci concentration at every fixed scale. The alternative derives two-sided volume and curvature-energy bounds from small model error plus topology, then uses the actual elliptic critical equation and Anderson compactness to obtain an impossible regular-chart limit. In both versions avg Z_t>=c for 0<=t<=1/4; actual supply gives the corresponding endpoint pencil. On fixed topology, stationary endpoint escape must lose the specified global Sobolev control.

boundary: The local budget must be small, not just finite. The stationary alternative retains its global Sobolev and absolute topological bounds, not merely chi/T_plus. Neither stationarity nor these budgets follows from Yamabe normalization or minimizing-sequence status. The unrestricted integral endpoint and beta=2 balanced coefficient remain open.

## I49: Uniform finite conformal-flow time from vanishing integral gaps and two energy walls

status: manuscript-theorem

scope: Closed scalar-minus-four initial metrics on the realized balanced small-h family; actual all-metric scalar/Ricci budgets and E>=c1 h, 0<c1<4; U=1+h+O(h^2) and initial b=P/(4V)<=h+o(h). Genuine initial metrics exist with E<=4h/(1+h)+h^2.

statement: Conformal Ricci flow satisfies V'=-P. With y=V/(2pi^2 A), every smooth time obeys -y'>=max{4mu*y/(4-mu),4(1+h-y),4(y-U)/3}. Explicit integration gives limsup Tmax<=1+log(4/c1), although the integral defect gap vanishes. The separate actual SW/Cotton estimate gives relative E descent until pointwise exit or loss of smooth continuation, with no continuous choice of gauge class.

boundary: This is conformal Ricci flow, not normalized Ricci flow. The all-time comparison does not preserve or need initial pinching. It bounds maximal classical smooth time, not a specific singularity mechanism or sharp lifetime. The flow result neither settles balanced coefficient4 nor turns failure of a flow into an independent all-metrics nonexistence proof.

## X06: Actual ordinary-SW deformations attain the sharp Weyl-payment coefficient

status: counterexample

scope: One fixed smooth product of closed hyperbolic surfaces, the second of genus two, with its canonical Spin-c class; h=0,U=3. Anti-Hermitian TT deformations are Yamabe-normalized and supplied with genuine unperturbed SW solutions.

statement: For H=f h1 and Delta f=lambda f, actual solutions satisfy P/K->lambda, signed S/K->1 and F/K->(lambda+2)/4. Degenerating the second factor and taking a diagonal perturbation gives S/F->2 and P/F->0. The exact h=0 identity gives S<=2F, so every proposed universal S<=cF+CP with c<2 and fixed finite C fails.

boundary: The actual solution is unperturbed, not a formal class. Individual implicit-function radii may shrink. This is not the balanced h>0 surgery family and does not refute its coefficient4 target; it proves that the Weyl payment cannot be universally discarded or reduced.

## O10: Weak-error exclusion at the zero-Weyl endpoint

status: open

scope: General bounded smooth self-dual forms with normalized L2 Hodge budget, and separately the narrower actual weighted-monopole supplier with a^2>=T+, without geometric compactness assumptions.

statement: Determine whether the sum of normalized Ric+g, W+, length and closedness errors has a positive lower bound depending only on those two budgets.

boundary: I45 closes the bounded-Ricci Euler-density case. I48 has local-integral and alternative stationary/global-Sobolev versions. Exact quadratic-critical noncollapsed curvature blow-up now supplies actual terminal metric cores with vanishing signed cost, excluding I47's physical resonant types. It does not supply a same-scale nonzero field, the full surgery core, or a bubble tree. The unrestricted integral target remains open.

## O11: Optimal all-metric small-h coefficient

status: open

scope: Actual conformal monopole input with p>=A>0, a^2>=T_+=A(1-h), and small E+D2/R.

statement: Determine the optimal leading coefficient of inf E/h over all metrics on the realized family. I41 proves the formerly requested stronger estimate Sigma<=C(P_Ric+D2), globally and with a square-shortfall version. Its Section 3.2 reduces coefficient4 to the first-order actual remainder bound Sigma<=(8/9)D2+32pi^2(p-A)+o(Ah); that sharper bound remains unproved. Genuine cscK products show improving the isotropic constant alone cannot yield4.

boundary: Order and scalar-variance-free slack are closed; the balanced coefficient is not. Retain the signed target (S-2F)_+=o(Ah): X06 forbids universally dropping 2F even with Ricci allowance. I44's Hessian reduces stability to an unresolved TT form, not a conformal negative mode. I49 yields actual finite flow time for genuine near-minimizers without attainment; no singularity classification or coefficient4 follows.

## O12: Diameter-free realization on the complex-hyperbolic numerical boundary

status: open

scope: Actual conformal monopole supply, p>=T_+=3T_->0 with bounded T_+, and sufficiently small pointwise negative Ricci defect, without a diameter bound.

statement: Determine whether these inputs force a complex-hyperbolic metric on the same smooth manifold, or identify an actual counterexample with all hypotheses.

boundary: Automatic saturation and volume control do not yet control long ends and fillings. Tau-zero shear examples do not lie on this numerical boundary.

## O02: Unrestricted Einstein existence on ED and nonzero-shear closed inputs

status: open

scope: All smooth Einstein metrics, not just adapted, symmetric, nearby or near-minimal-volume ones.

statement: A negative nonsymmetric Einstein output has not been constructed or excluded on the designated input manifolds. Full-curvature minimum attainment is one equivalent formulation in the specified families.

boundary: Local repair and spectral/diameter restrictions do not exhaust these outputs.

## Complete source locations

- continuation/20260927_mixed_current_and_signed_cores.md → 01_linear_gap_and_actual_applications.md, source 1; 36865 bytes; SHA-256 ea0c4955b56edf70fc5a19d5fd5f4553a1c0c8962a442cdd8c43362b6aabcf79.
- continuation/20260927_conformal_separation_and_zero_end.md → 01_linear_gap_and_actual_applications.md, source 2; 67263 bytes; SHA-256 8f37b7ceb8fce5ce2f33ad6a87f5a8afcfe4cfd0b19282ed6ea8ae3689aebca9.
- continuation/20260927_covering_geometry_and_sharp_subfamilies.md → 02_endpoint_covering_and_sharp_subfamilies.md, source 1; 41289 bytes; SHA-256 fdbfa874d5611fe54ad75ad00cd0a2f05946777c2598b6d4922abf09df40ad76.
- continuation/20260927_local_geometry_and_variational_extrema.md → 02_endpoint_covering_and_sharp_subfamilies.md, source 2; 50890 bytes; SHA-256 68abdebe39870e7e984169eb9b434a88b0a974b98da8e10b7effa494e7c1b7e6.
- continuation/20260927_full_core_cost_and_extremal_metrics.md → 03_full_cores_signed_extrema_and_flow.md, source 1; 41263 bytes; SHA-256 4625dbfb968571ae91292fc6944d4c969b8a4db681cb8a6cea114ee2529b9302.
- continuation/20260927_signed_balance_and_conformal_flow.md → 03_full_cores_signed_extrema_and_flow.md, source 2; 31580 bytes; SHA-256 9d726a0c5653f223eedb424d985704918dd1fdf8ac0d01317d5d063a6cc39dd7.
- mathematics/current/line1_integral_rigidity_paper.md → 04_analytic_foundations.md, source 1; 43113 bytes; SHA-256 ca664aa1f07d2907c8bd0b346d4e0b824cb858335fa2a8d15c9cce33ba7e3d54.
- mathematics/current/round21_analytic.md → 04_analytic_foundations.md, source 2; 20154 bytes; SHA-256 9e39e932ae9f109d9ab3f959a243046e243beb20900c3f4e95be8dc424f5eb22.
- mathematics/current/line1_functional_pencil.md → 04_analytic_foundations.md, source 3; 18863 bytes; SHA-256 13f0324dab4999ffba998cd60e8a1d8c152b97aae6f40218aca599230c4201ae.
- mathematics/current/line1_compactified_pencil.md → 04_analytic_foundations.md, source 4; 12073 bytes; SHA-256 0d971e1519c9d8b5edddcbd71f158c3ca08acf943d5ae4a7eb3f359af2628bed.
- mathematics/current/line1_energy_envelope_gap.md → 04_analytic_foundations.md, source 5; 10305 bytes; SHA-256 8cd0c429b2f403b1c31bb24333efc7397afba5742394a2951dd56aa5e24c3ad4.
- mathematics/current/line1_two_chirality_topology.md → 05_actual_topology_and_prior_field_equations.md, source 1; 12028 bytes; SHA-256 91eb14bc07220c6d66e2b97af97501d324bc1dad999ba7b9d2f41368217fa5a6.
- mathematics/current/line1_bauer_furuta_geography.md → 05_actual_topology_and_prior_field_equations.md, source 2; 13266 bytes; SHA-256 1ef42b7981722b1ec8a4325e85e460cc5dda1805b64827def3c7d4afe07de3e9.
- mathematics/current/round14_twisted_rigidity.md → 05_actual_topology_and_prior_field_equations.md, source 3; 11854 bytes; SHA-256 77b52d2c7a8b3e8a9fd6a71f0109cbebcd825e34d428b1be30dffaf1bb505bc8.
- continuation/20260926_boundary_compatibility.md → 05_actual_topology_and_prior_field_equations.md, source 4; 22633 bytes; SHA-256 e182615cd26b7031d4275ae9c5930e244e6088cbad39ac9770c835ba7f5bca19.
- continuation/20260926_actual_topological_cost.md → 05_actual_topology_and_prior_field_equations.md, source 5; 26796 bytes; SHA-256 5b189c3143977efe8ab65b4f22c06ef2e8d354d30faa69180a0f07eadf95772b.
- verification/20260927_linear_cost.md → 06_review_records_and_source_map.md, source 1; 9283 bytes; SHA-256 6b5cba75dfa7d6ae1a59d563dcf11bf133273ffe147d077bf6c4e86f7dc1fbdf.
- verification/20260927_conformal_and_endpoint.md → 06_review_records_and_source_map.md, source 2; 7304 bytes; SHA-256 ff105d8c73aa129938dfdf21b46a4e5d84c9db3dd8a278d2fb0ee4da54b4e1ca.
- verification/20260927_covering_and_sharpness.md → 06_review_records_and_source_map.md, source 3; 7121 bytes; SHA-256 c4ca515a57a270cb5afda344679595405142e0cac46c9ae72419acb51c4da35b.
- verification/20260927_local_geometry_and_extrema.md → 06_review_records_and_source_map.md, source 4; 8602 bytes; SHA-256 8ffa8cc1fe50f6583564caed6e9fa95358d7598e5111697771d4f5dfcc758b41.
- verification/20260927_full_core_and_extrema.md → 06_review_records_and_source_map.md, source 5; 6660 bytes; SHA-256 efe4444250e3bd8b1771c8c98ef329ccb3bd501794812bc6304347ecd4a21f54.
- verification/20260927_signed_balance_and_flow.md → 06_review_records_and_source_map.md, source 6; 8619 bytes; SHA-256 2c5a5b3a335b43dd5168b27e2429c141dad9a4689eaa50954a8db11e605a1e5e.

## Deliberately deferred material

- mathematics/current/line1_energy_selection.md; mathematics/current/line1_yamabe_endpoint.md: The new conformal-separation paper rederives the required conformal identities and normalization. These remain historical/source references rather than missing local proof steps.
- mathematics/current/lebrun_stability_closure.md; mathematics/current/round21_chambers.md: The included independent integral-rigidity paper Sections 9-10 already contains the needed chamber, loop-insertion and classical-family arguments.
- Old eight-volume realization, monodromy, ED and slow-mode papers: Independent preserved branches already in the earlier reading package; not prerequisites for the present sharp actual-SW construction or flow theorem. Not withdrawn.
- External primary literature, computation scripts, numerical logs and runtime traces: Primary theorem links and locations stay in the proofs/review records. Executable assets remain local and can be supplied for a specific requested calculation. No external PDF or runtime data is bundled.
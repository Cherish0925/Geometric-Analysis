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

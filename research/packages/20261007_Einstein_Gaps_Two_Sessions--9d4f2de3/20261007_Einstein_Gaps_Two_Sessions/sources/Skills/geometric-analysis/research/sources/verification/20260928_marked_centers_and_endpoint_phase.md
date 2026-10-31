# Matched caps, first-order stability, and endpoint continuation

28 September 2026. Base commit 3409fe5e9b094cffa39f1c08534ee6234c49dd25.
Local branch: local/yau26-marked-slice-20260928.

## Mathematical changes

The main positive conclusion is now
[matched critical-energy caps and gauge-free stability, I53](../continuation/20260928_intrinsic_caps_and_stability.md).
For a Euclidean annulus with small C0 error a and small full-curvature
energy E0, a smooth ball cap matches its outer germ exactly at cost
C(E0+a²). This is proved using localized DeTurck smoothing with the
full Lie derivative, a weighted Bernstein quotient, fixed-input
frozen-collar estimates, critical Sobolev absorption and two matches.

Euler's identity supplies an O(A) global curvature budget without scalar
normalization. Partial blowdown retains bad cores and charges their
number. The finite bound allows o(Q) unstructured cores and small
mean-square amplitudes, needing only Lh tending to infinity.
Consequently the infimum over every shrinking C0 tube of selected
actual recovery bases, also modulo diffeomorphisms, divided by h tends
to four. A fixed sub-four deficit requires positive distance from
these orbits. Neither all-metric optimality nor the sharpness of the
quadratic amplitude modulus is claimed.

The companion proof is
[moving centers and harmonic slices](../continuation/20260928_marked_centers_and_harmonic_slices.md).
X09 is an actual balanced recovery construction, not a coordinate-only
model: scalar-minus-four metrics are C0-near, both attain recovery
coefficient four, and their actual gauge residual is small, yet every
exact Diff0 Bianchi gauge relative to the selected fixed base has
unbounded bilipschitz distortion.

The proof uses relative Yamabe normalization, clustering of whole handle
regions, a harmonic-map limit, and the exceptional homology mark.
Hartman's uniqueness is used on the smooth CH limit, not on the
non-Einstein resolved metrics. Existence of a harmonic diffeomorphism
is not asserted. The diagonal selects the recovery bases; it is not
a conclusion for every previously prescribed base.

The same proof immediately continues to positive coverage. Moving the
reference centers absorbs the example exactly. The I52 estimates extend
uniformly over compact configuration families, and under arbitrary
positive conformal factors and orientation-preserving pullbacks.
Independently, the conformal Hessian estimate shows that X09 already
satisfies the fixed-base approximate criterion. These extensions are
recorded with I52, not assigned separate result numbers.

The second record,
[opposite-spinor curvature](../continuation/20260928_zero_endpoint_phase_curvature.md),
derives a polynomial equation through zeros and its weighted integral
test. Commuting derivatives retains a critical opposite-Weyl/gradient
interaction. The local negative-index seed is an actual fixed-seed
local extension via the inherited contraction, not a closed endpoint
counterexample. This work does not change the open status of O10.

O11 remains open over all metrics because the required marked annular
structure has not been extracted from arbitrary near-minimizers.
The matched cap itself was completed during this continuation and is
no longer a missing premise.

## Parallel work and independent checks

Two clean-context gpt-6-astra/max agents and one continued Astra agent
worked simultaneously with the root within the available slots.
The thread limit prevented another fresh spawn; an existing context was
reused transparently. Every agent was read-only; only the root edited.

- intrinsic_gauge_20260928: donor Jacobi calculations, marked-center
  construction, relative normalization and harmonic-limit proof.
- gauge_free_energy_20260928: intrinsic energy/cap route, primary-source
  smoothing checks, independent audit of the marked construction,
  conformal saturation and approximate-gauge Hessian estimate;
  full localized cap proof and independent partial-blowdown/tube checks.
- high_index_global_20260927g: actual opposite-spinor Ricci equation,
  transgression and local index-sign check; another independent audit
  of the marked harmonic-limit argument.
- Root: independent Schwarzschild curvature/block calculation,
  exact Bianchi/harmonic identity, topology/normalization and diagonal
  checks, compact-configuration extension, conformal transfer, integration
  of complete proofs and finite verification; Euler budget without
  normalization, partial-blowdown identity and bad-core selection.

The cap proof then underwent two further independent mathematical
audits by intrinsic_gauge_20260928 and high_index_global_20260927g.
Both checked the q-weighted derivative powers, uniform time,
uniform-in-time collar jets, boundary flux, critical absorption,
input-dependent eta selection and exact matching. Neither found a
remaining substantive gap within that audit. The root checked the
displayed equations and application separately.

Material changes made during these checks:

- A handle between fixed distinct points does not converge to the smooth
  CH manifold. Both mouths are clustered, with separate physical scales.
- Uniform relative normalization does not require unproved uniform
  donor derivatives: the common first factor cancels, and a second
  maximum-principle comparison is global.
- Small gauge residual does not imply an exact controlled gauge; it
  does still activate the approximate stability theorem in this example.
- Near-stationarity in the uniform family retains the stronger
  exterior P budget of I52, not merely o(Q).
- The local homology argument uses fixed enclosing topological
  neighborhoods, not only shrinking terminal pieces.
- A uniform cap modulus would already suffice. The completed proof gives
  a quadratic amplitude bound; retaining bad cores then weakens the
  required range from L/A tending to infinity to Lh tending to infinity.
- Scalar normalization is not needed for the global full-curvature
  budget. This avoids silently assuming a normalized metric stays
  C0-close to the actual annuli.
- The variable-q flow uses the full Lie derivative L_(qW), not q L_W.
  Both the coordinate equation and geometric boundary transport need it.
- One may integrate the Hessian-cutoff term by parts, or use the
  independently checked integrable coefficient C(1+a/sqrt(t)).
- Exact matching chooses eta after the individual smooth datum. Its
  derivative-dependent constants never enter the final universal bound.
- Endpoint phase and Lichnerowicz radial terms cancel. Their difference
  is not a positive error estimate.
- The unfixed opposite-Weyl block remains in the derivative transgression
  even under the pointwise principal constraints. Exact prolongation on
  an open set removes that algebraic freedom, but the weak proof then
  needs derivative products not controlled by the present budgets.

These checks are internal mathematical review, not a journal
certification or a claim of worldwide originality.

## Primary sources and inherited proofs

- [Hartman, On Homotopic Harmonic Maps, p.675, Section 1(H)](https://math.jhu.edu/~js/Math646/hartman.harmonic.pdf):
  uniqueness in the homotopy class of a rank-four harmonic isometry
  into a strictly negatively curved target.
- [LeBrun, Theorem 4.3](https://arxiv.org/html/math/0003068):
  the classical actual surgery construction, as developed in I52.
- [Armstrong thesis, Sections 3.3.1--3.3.3](https://johnarmstrongmaths.com/publications/resources/thesis.pdf):
  the exact endpoint mechanism, not a weak-integral gap theorem.
- [Yang, Convergence of Riemannian manifolds with integral bounds on curvature I, equation (9.7)](https://www.numdam.org/item/10.24033/asens.1644.pdf):
  localized curvature evolution. Its stronger Lp Ricci theorem is not
  imported as a consequence of the present L2 input.
- [Schnürer--Schulze--Simon, Theorem 4.4](https://arxiv.org/pdf/0706.0421):
  independent initial-time interior derivative check on frozen collars.
  The variable-q common existence time is established in the new proof.
- [Cheng, pseudolocality for incomplete manifolds](https://arxiv.org/abs/2210.15397)
  and [Martens, critical-energy smoothing](https://arxiv.org/abs/2408.11115):
  inspected for the cap route. Positive-time smoothing is not identified
  with a matched extension to the original collar.
- I52, Sections 3--4: actual recovery, normalization, graph estimate,
  approximate gauge and conformal Hessian estimate.
- I41, Sections 14--15.1: Clifford conventions and fixed-seed actual
  hyperbolic local construction.

The project Skill preserved supplier quantifiers and the distinction
between V-scale and Ah-scale targets. The mathematical inputs were the
full current manuscripts. No installed Skill, live service or shared
runtime was modified.

## Reproduction and preservation

Run from the project root:

    python3 tools/check_marked_centers_and_harmonic_slices.py
    python3 tools/check_endpoint_covariance_and_surgery_limits.py
    python3 tools/check_constant_weight_and_global_fit.py
    python3 tools/library.py verify
    git diff --check

The new finite checks cover the Euler rearrangement, exact partial-cap
identity, quotient cancellation, pointwise harmonic identity,
conformal algebra, Schwarzschild mode potentials, scalar stress-test
formula, scale exponents, Clifford anchor, unfixed Weyl block and
negative-index seed. They do not certify parabolic continuation,
PDE compactness, actual gluing, harmonic removability, the supplied
nonlinear contraction or the uniform-family theorem.

Pre-edit history is preserved in
/data/qiushi/research/Yau26_Research_backups/20260927_3409fe5_i52.bundle.
Its prior restoration receipt records a full fsck-checked restore.
The 884-file mathematical baseline and 10,191 source records are not
edited. No web-review package is produced and no research is uploaded.

Execution results and final artifact hashes are recorded below after
rendering and the final preservation check.

### Executed checks, 28 September 2026

- New finite suite: 15 tests passed.
- Inherited endpoint/surgery suite: 22 tests passed.
- Inherited same-weight/global-fit suite: 19 tests passed.
- Library verification: 884 baseline files, 10,191 archived source
  records and 790 navigation links checked; zero failures.
- All three new manuscripts compiled to TeX/PDF without reported
  warnings: matched caps 8 pages, marked centers 10 pages, endpoint
  equations 5 pages.
- PDF inspection sampled the cap statement and partial-blowdown
  formulas, harmonic-limit argument and endpoint prolongation page;
  no clipping or missing formulas appeared.
- Whitespace check passed. No preserved baseline or source archive
  file was edited.

These 56 finite checks do not replace the written analytic proofs.
The catalogue uses manuscript-theorem status, not formal or external
certification.

Final source and artifact SHA-256:

| Artifact | SHA-256 |
| --- | --- |
| Matched caps MD | f4b0ba5966f3e532aa3fc9bbd02328163b6e6da272210414af3ecc834384fde6 |
| Matched caps TeX | edb0007eeab5b6b47569fd38043e034eb4e7eb67d512413b417ad17f6ea65673 |
| Matched caps PDF | 2eafdfc32f3c13183ca444e7b5dc392a8e157e4f0c725ffedefaade442de4744 |
| Marked centers MD | e8e771f0cfa241480a8c884cff096a1ce13a76e8b1099dc72a36ad95f57e1475 |
| Marked centers TeX | 27db3f00fb3eb2c916b81f1affb690588a6b6821f48ed1af993eb9dbe9355acf |
| Marked centers PDF | aab683ab8efe3066700a1dd85aecd319e4d120d461890d0f9605ccd3c150f152 |
| Endpoint MD | 99e17090cd3caa7882f3e584d074d6ba6f1bbb8ef4db1d398efb5c143cddf599 |
| Endpoint TeX | 465c8fdba85234f4f67cd659399175eba60adccf01fad9293cf7c7210fcffe9f |
| Endpoint PDF | 5ad8c58475e4ce71bacdd68fa3488fb2fdc2922a1a326c949a7ae31df0b63b0f |
| New finite check | e4bed8f9a79bd0f62ff49929e8d5644a0e5ea1aac3cdf7a873416de539033787 |

The local commit and restored Git-bundle receipt are maintained under
/data/qiushi/research/Yau26_Research_backups, separately from this
versioned scientific record. No web-review archive was created.

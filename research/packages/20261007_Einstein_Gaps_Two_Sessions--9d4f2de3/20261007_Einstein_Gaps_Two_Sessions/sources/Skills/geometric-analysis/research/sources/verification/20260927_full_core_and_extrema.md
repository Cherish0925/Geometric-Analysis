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

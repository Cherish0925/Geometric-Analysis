# Gauge supply, global propagation, collapse, and singular realization

24 September 2026. Current research entry after
[compact realization](20260924_global_realization.md). The four proof notes
below address different restrictions of that result. They are not four
independent claims of world-first discovery, nor a partition of all Yau26
inputs. Their common question is which information lets an approximate
Einstein metric lead to a conclusion about its original smooth manifold.

## 1. Gauge input need not live on the manifold carrying the output

The [finite-cover theorem](20260924_virtual_gauge_realization.md) allows
actual monopole inputs on a finite cover \(N\to M\), with no bound on its
degree \(d\). Under bounded base diameter, a per-sheet projection floor
\(p/d\ge A_0\), and bilateral saturation, it produces an exact metric
on the **base** with universal cover \(\mathbb H^2\times\mathbb H^2\).
For a nonorientable base, one actual input on an oriented finite cover
suffices. At the Miyaoka–Yau numerical boundary, one actual input with
\(p\ge d(2\chi+3\tau)(M)\) gives a locally complex-hyperbolic metric
directly from small pointwise Ricci defect.

The mechanism is to descend the scalar distance of the Weyl operator from
its equality orbit, not the auxiliary form or Chern class. Degree cancels
in the normalized estimates. Compactness and smooth-type preservation are
then proved downstairs. There is no assertion that an arbitrary Einstein
metric found upstairs is invariant and descends.

A concrete diagonal quotient of two even-genus hyperbolic surfaces has
\(\chi+\tau\equiv2\pmod4\) and hence no almost-complex structure in
either orientation, but has the required cover inputs and an exact product
quotient metric. This is a classical equality example, not a new manifold.
It demonstrates why allowing cover supply genuinely enlarges the input
description, and why the conclusion is Riemannian rather than global KE.

## 2. Large volume no longer forces a small total residual

The preceding no-diameter repair theorem required small unnormalized
\(L^2\) Ricci residual. The
[uniformly local repair theorem](20260924_uniformly_local_repair.md)
replaces that condition by an explicit propagation estimate. If the full
gauged Einstein operator has **positive quadratic-form coercivity**
\(\lambda\), and the actual manifold satisfies
\[
 \operatorname{Vol}B_R(x)\le C_G(1+R)^d e^{HR},\qquad H^2<8\lambda,
\]
then an exponentially weighted energy identity gives
\[
 \|L_g^{-1}f\|_{C^{2,\alpha}_{\rm uloc}}
       \le C\|f\|_{C^{0,\alpha}_{\rm uloc}}.
\]
With the stated local regularity hypotheses, pointwise small Ricci defect
therefore gives an exact negative Einstein metric, without diameter,
volume or global-residual smallness. The proof retains every tensor mode.

Fixed cyclic covers of a closed hyperbolic manifold have uniform linear
ball growth and Koiso coercivity. Independent small perturbations in each
cell can have total residual growing like \(t\sqrt m\), yet satisfy the
uniform repair criterion. These manifolds already admit Einstein metrics;
the increment is a uniform repair neighbourhood for distributed errors.
The [bounded-chart corollary](20260924_higher_dimensional_local_repair.md)
states the analytic argument in every dimension \(n\ge3\), including the
cyclic-cover examples and their dimension-dependent coercivity constants. The
four-dimensional no-bubble theorem is one supplier of its local charts,
not part of the weighted inverse identity itself.

## 3. Genuine collapse now has an actual-form connection

The [collapsed bulk theorem](20260924_collapsed_bilateral_bulk.md)
uses maximal local nilpotency rank in the Euclidean-model regime of
Naber–Zhang. For bilateral gauge deficit
\(K=2r+q_++q_-\to0\) and pointwise Ricci defect tending to zero,
local universal-cover balls approach \(\mathbb H^2\times\mathbb H^2\)
outside an exceptional set with
\[
                         \operatorname{Vol}(\mathcal E)/V\le CK^{1/4}.
\]
There is no diameter, base-ball volume, homotopy or total-volume bound.
The essential transfer is an estimate for **local averages** whose
constant is independent of covering multiplicity. It is false for
unnormalized integrals, as an explicit pinching-surface product shows.

This changes the local input regime to include genuine collapse. It does
not give a global repair theorem: maximal rank is not automatic, the small
exceptional set can carry topology, and transition maps and low modes are
not controlled by its volume alone.

## 4. With nonzero second homotopy, allow the singular limit

The [orbifold and smoothing theorem](20260924_orbifold_smoothing_bridge.md)
removes \(\pi_2=0\) from the **compactification** conclusion. Bounded
diameter, actual positive projection and simultaneous small Ricci/gauge
defects yield a negative KE orbifold with a global orbifold complex
structure. Smooth ALE blow-up limits are anti-self-dual.

To obtain an exact metric on the original smooth type, the note gives a
separate theorem: a global Q-Gorenstein smoothing, together with matching
of each whole geometric filling to its Milnor fiber **with its boundary
marking**, gives an oriented diffeomorphism to a smooth fiber. Canonical
ampleness and Aubin–Yau then provide the required exact metric. The
Lee–Park logarithmic-tangent obstruction criterion supplies a checkable
global smoothing condition; nodal hypersurfaces give an explicit classical
example. Merely classifying a terminal ALE bubble does not supply the
whole filling or this matching.

This is an alternative to excluding every bubble. The raw geometric data
prove the orbifold conclusion; the additional smoothing and marked-topology
conditions remain additional, not hidden consequences of saturation.

## 5. The next mathematical decisions are now distinct

| Mechanism | What is now available | What is not supplied |
| --- | --- | --- |
| Cover gauge supply | Exact geometry on the base, independent of cover degree | Arbitrary descent of an upstairs Einstein metric |
| Weighted propagation | Volume-independent correction of distributed residuals | Inversion in the presence of kernels or uncontrolled growth |
| Collapsed rewinding | Product geometry on the maximal-rank bulk | Global deck matching, bad-region topology and full inversion |
| Singular compactification | KE orbifold and a marked smoothing realization criterion | Automatic QG smoothing and whole-filling identification |

These results suggest two focused continuations, not another general
route list. One is to classify the global transition and low-mode data of
the product-type collapsed regions, where the positive-coercivity repair
theorem does not apply. The other is to determine when the geometric
fillings produced by actual near-saturation must meet the relative Milnor
criterion, or to construct a counterexample. Either can change exact
existence; merely shrinking an average error or classifying one more
terminal bubble cannot substitute for it.

The retained diameter-free integral obstruction theory remains independent
and valid under its own actual-input assumptions. None of these additions
proves the unrestricted obstruction/existence dichotomy or completes a
Yau26 sign branch. All proofs, classical dependencies, exact model tests and
local commits remain in this project; inherited sources and live systems
are unchanged.

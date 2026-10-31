# Step 21 — Entropy supplier, real-hyperbolic cells, exact-collar rigidity, and off-bolt Weyl spectra

Conventions: curvature operator norms and Chern–Weil formulas are those of `theorem_package_v1.md`. For the real-hyperbolic calculations the exact normalization is
\[
K=-2,\qquad \operatorname{Ric}=-6g,\qquad s=-24.
\]
Thus all cell costs below are divided by \(8\pi^2\). The corresponding scalar-\(-12\), sectional-curvature-\(-1\) formulas follow by scale invariance.

## 1. Exact-collar Einstein rigidity has no exceptional topology

Step 20 proved by analytic continuation and Hirzebruch proportionality that an Einstein metric agreeing with \(\mathbb{CH}^2\) on a collar is locally complex hyperbolic throughout. The temporary topological calculation only excluded \(\ell\ne2k\). The locally symmetric continuation actually closes every case.

**Lemma R (closed form).** Let \(U\) be a connected smooth marked cell with an exact \(\mathbb{CH}^2\) collar. If an Einstein metric on \(U\) extends that collar, then \(U\) is the standard complex-hyperbolic ball cell. Hence its marked topology is trivial: \(k=\ell=0\).

**Proof.** Einstein metrics are real analytic in harmonic coordinates. The tensor \(\nabla\mathrm{Rm}\) vanishes and the complex-hyperbolic curvature tensor holds on the collar, hence on all of connected \(U\). The universal cover \(\widetilde U\) develops by a local isometry into \(\mathbb{CH}^2\). The collar \(S^3\times(a,b)\) is simply connected, so its preimage is a disjoint union of isometric collar copies. On each copy, the developing map agrees with the inclusion of a geodesic-sphere collar after a global isometry of \(\mathbb{CH}^2\); analyticity/local-symmetry continuation extends this to the connected component of the ball complement. Any two ball complements in \(\mathbb{CH}^2\) intersect, so there can be only one such lift. The deck group therefore preserves that lift. Because it covers the simply connected collar and acts freely, the deck group is trivial. The developing map is the standard ball filling, and no marked blow-up or handle topology remains. \(\square\)

The upshot is stronger than the previous \(\ell\ne2k\) statement: every exact-collar cell with \((k,\ell)\ne(0,0)\) has positive defect at each fixed smooth metric. A zero infimum, if it occurs, must arise through degeneration: the collar recedes to a complete ACH limit, collapse occurs, or topology concentrates through a non-Euclidean neck. Lemma Q' already excludes an almost-Euclidean neck for a blow-up minimizing below \(8\pi^2\).

## 2. Volume entropy is a new field-free supplier

The actual source `Knowledge/objects/papers/ENTROPIES-VOLUMES-AND-EINSTEIN-METRICS--0ee1eb110f9d--94203f883336/object.md` states Kotschick's entropy-strengthened Einstein inequality
\[
\chi(X)\ge \frac32|\sigma(X)|+\frac{\lambda(X)^4}{108\pi^2},
\]
and Corollary 3 (Sambusetti/BCG): if a closed Einstein four-manifold \(X\) maps with nonzero degree \(d\) to a closed real-hyperbolic four-manifold \(Y\), then
\[
\chi(X)\ge \frac32|\sigma(X)|+|d|\chi(Y),
\]
with equality only when \(X\) is real hyperbolic. The proof uses Besson--Courtois--Gallot entropy, Bishop comparison after Einstein normalization, and exact rigidity; it does not use monopoles.

For
\[
X=Y\#k\overline{\mathbb{CP}}^{\,2}
\]
the pinch map has degree one, \(\sigma(Y)=0\), and
\[
\chi(X)=\chi(Y)+k,\qquad \sigma(X)=-k.
\]
The Einstein inequality would require \(k\ge3k/2\), impossible for every \(k\ge1\). Therefore:

**Theorem H (entropy-supplied Einstein nonexistence).** Every blow-up \(Y\#k\overline{\mathbb{CP}}^{\,2}\), \(k\ge1\), of a closed oriented real-hyperbolic four-manifold admits no Einstein metric.

This extends the supplier portfolio beyond gauge fields: the supplier is the homological minimal-volume entropy, unchanged by simply connected blow-up summands. It establishes exact nonexistence but not a positive \(L^2\) Einstein gap for the low-blow-up range. The entropy proof uses a pointwise Einstein/Ricci normalization before Bishop comparison. Small critical \(L^2\) trace-free Ricci does not provide that pointwise hypothesis. This is the same critical-exponent obstruction encountered in field transport and compactness, now in entropy form.

The Yamabe-invariant search did not find a theorem proving
\[
Y(Y\#k\overline{\mathbb{CP}}^{\,2})=Y(Y)
\]
for a closed real-hyperbolic four-manifold. The Kotschick source contains no Yamabe computation. Hence the constant-scalar lower theorem below remains conditional on the scalar-energy/volume input; it is not promoted to an unconditional gap theorem.

For reference, raw Chern–Weil gives only
\[
P(g)\ge \frac1{24}\int s_g^2+4\pi^2k-8\pi^2\chi(Y),
\]
and therefore the unconditional Hitchin--Thorpe-scale positivity \(P\ge4\pi^2(k-2\chi(Y))\) only when \(k>2\chi(Y)\).

## 3. Same-metric real-hyperbolic cell identities

Let \(U\cong D\#\overline{\mathbb{CP}}^{\,2}\) agree to the necessary collar jet with the real-hyperbolic ball \(B\), in the orientation where the exceptional class has square \(-1\). Relative Chern–Weil gives
\[
\frac{P(U)}{8\pi^2}-1
=4\frac{\int_U|W^+|^2}{8\pi^2}
+\frac{\int_U s^2/12-48\operatorname{Vol}(B)}{8\pi^2}. \tag{3.1}
\]
For
\[
J= P+\frac14\int_U(s+24)^2,
\]
the pointwise identity
\[
\frac{s^2}{12}+\frac{(s+24)^2}{4}=\frac{(s+18)^2}{3}+36
\]
gives
\[
\frac{J(U)}{8\pi^2}-1
=4\frac{\int_U|W^+|^2}{8\pi^2}
+\frac{\int_U(s+18)^2/3}{8\pi^2}
+\frac{36\operatorname{Vol}(U)-48\operatorname{Vol}(B)}{8\pi^2}. \tag{3.2}
\]
Thus a subthreshold \(J\)-cell would require a large enough volume deficit, with scalar near \(-18\) on the useful portion, to defeat the nonnegative Weyl and square terms. For a constant-scalar \(s=-24\) cell, (3.1) is
\[
P-8\pi^2=4\int|W^+|^2+48\{\operatorname{Vol}(U)-\operatorname{Vol}(B)\}.
\]
Consequently \(\operatorname{Vol}(U)\ge\operatorname{Vol}(B)\) implies the sharp \(P\ge8\pi^2\) lower bound. On a closed blow-up, an analogous hyperbolic-volume comparison for scalar \(-24\) metrics would yield the exact coefficient \(8\pi^2\) per blow-up. No such Yamabe-volume theorem is presently established here.

## 4. Numerical pressure on finite-scale real-hyperbolic saving

Peer code `Sessions/S1003A01/workspace/scripts/h4_perp_cell.py` uses
\[
F=x,\qquad G=x+2x^2,
\]
which was symbolically checked to have \(s=-24\), \(P=0\). It implements ordinary \(O(-1)\) bolt regularity and exact H4 two-jet contact. The peer large-collar \(X=64\), degree-16 \(P\)-optimized values are
\[
\begin{array}{c|c}
x_0&P/(8\pi^2)\\\hline
.003&1.00605638296\\
.01&1.02046688095\\
.03&1.06306956649.
\end{array}
\]
The new independent channel evaluator `workspace/scripts/h4_cell_channel_analysis.py` reconstructs these records at 1600-node quadrature. Its identities close to \(<4\times10^{-13}\). Data are in `workspace/data/h4_cell_channels.json`. The volume ratios are
\[
1.0000167741,\quad1.0000479885,\quad1.0001185601,
\]
the scalar means are \(-23.99985,-23.99959,-23.99905\), and the fractions of volume with \(|s+18|\le3\) are only about \(1.3\times10^{-7},1.4\times10^{-6},1.2\times10^{-5}\). The scalar-volume channels in (3.1) are positive and contribute approximately \(2.004x_0,2.004x_0,1.995x_0\), while the inferred \(4W^+\) terms are positive and smaller (roughly second order). Thus these profiles realize Theorem F's \(+2x_0\) response rather than a nonlinear saving.

The scan was extended to \(x_0=.1,.3,1\) at \(X=64\), degree 18. The floating values were
\[
P/(8\pi^2)=1.22129,\ 1.71385,\ 3.78377,
\]
with volume ratios \(1.00041,1.00131,1.00539\) and scalar still near \(-24\). The \(x_0=.3,1\) optimizers hit their iteration limits, but their large positive margins make them useful exclusions of an obvious continuation to a subthreshold branch, not minimizer estimates. A separate \(J\)-targeted run at \(x_0=.03,X=64\) gave
\[
P/(8\pi^2)=1.06462009,\qquad J/(8\pi^2)=1.06507303,
\]
again with no volume deficit and no scalar-near-\(-18\) region. Records: `workspace/data/h4_cell_channels_extended.json` and source JSON files beside it.

This is restricted numerical evidence. It does not prove the all-metric or even full diagonal infimum. It does show that the CH finite-collar surprise was actively sought in the H4 analogue over a much wider bolt-scale range and that the only available nonlinear channels remained on the positive side.

## 5. Off-bolt Weyl splitting for Theorem E

At the bolt, both chiral Weyl blocks have forced multiplicity \((2,1)\); this cannot test conformal Kählerness. The new script `workspace/scripts/ach_weyl_degeneracy_offbolt.py` integrates the exact Einstein ODE from the bolt series, reconstructs the exact radial two-jet, and independently evaluates both chiral curvature-operator blocks in coordinates. It sampled the central shooting parameter and both endpoints of the validated \(d\)-interval. Data: `workspace/data/ach_capd/weyl_degeneracy_offbolt.json`.

At \(t=.5\), uniformly across the three sampled parameters, the central spectra are approximately
\[
W_A=(-0.845829,-0.841893,1.687721),
\]
\[
W_B=(-1.96026,0.49655,1.46371).
\]
The smallest eigenvalue gaps are about \(3.94\times10^{-3}\) and \(0.967\). The reconstructed scalar is \(-24\) and \(|\operatorname{Ric}^\circ|\approx2.5\times10^{-11}\), which strongly cross-checks the coordinate curvature evaluation.

If both chiral Weyl blocks have simple spectrum at one point, then no conformal rescaling can be Kähler in either orientation near that point: a Kähler four-metric has the \((1,2)\) Weyl eigenvalue multiplicity in its complex orientation, and eigenvalue multiplicity is conformally invariant in dimension four. Since the metric is analytic, positivity of the discriminant at one point would also exclude a conformally Kähler open set anywhere in that orientation.

Current status: compelling floating evidence, not yet a theorem for the Ważewski-selected orbit. The validated existence theorem selects an unspecified \(d_0\) in the full interval; sampling endpoints and center does not enclose every \(d\). The clean next computation is interval transport of all 40 Fuchsian \(d\)-boxes to \(t=.5\), followed by an outward-rounded orthonormal-frame evaluation of both Weyl discriminants. The observed smaller gap \(3.9\times10^{-3}\) is plausible for CAPD/Arb certification.

## 6. Updated common picture

The direct-gap theory now has three distinct suppliers with different analytical continuations:

1. monopole/harmonic fields supply curvature alignment and differential prolongation;
2. the ambient self-dual curvature operator supplies the signed local topology-response law;
3. volume entropy supplies exact Einstein nonexistence on hyperbolic blow-ups.

All three become difficult at the same dimension-four critical exponent when one asks for a quantitative near-Einstein theorem. Metric-wise fields can be lost in bubbling; \(L^2\) curvature does not provide uniform Sobolev/harmonic-radius control; and entropy comparison needs pointwise Ricci control rather than critical \(L^2\) trace-free Ricci. This identifies a genuine common obstruction rather than three unrelated technical failures.

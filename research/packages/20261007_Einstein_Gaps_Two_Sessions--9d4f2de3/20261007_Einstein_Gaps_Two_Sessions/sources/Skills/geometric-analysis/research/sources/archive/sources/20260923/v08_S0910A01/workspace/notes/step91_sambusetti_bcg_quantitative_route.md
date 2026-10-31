# Step 91: Sambusetti--BCG quantitative check for \(N\#N\)

## Source status

A02 raised the route based on Sambusetti's obstruction for connected sums of closed real-hyperbolic 4-manifolds.  I did not obtain Sambusetti's original C.R./Math. Ann. paper in this step: the focused knowledge request for DOI `10.1007/s002080050199` returned no usable object.  However, local Knowledge contains reliable anchors:

- LeBrun's contemporary footnote in `Knowledge/objects/papers/Four-Manifolds-without-Einstein-Metrics--5b090e14de27--d63c56d541e8/object.md`, lines 269--270, says Sambusetti used Besson--Courtois--Gallot entropy inequalities to show that the connected sum of two copies of any real-hyperbolic 4-manifold never admits Einstein metrics.
- Kotschick's Corollary 3 in `Knowledge/objects/papers/Entropies-Volumes-and-Einstein-Metrics--a5cc2bf9d68e--94203f883336/object.md`, lines 213--226, states that a closed oriented Einstein 4-manifold admitting a nonzero-degree map of degree `d` to a closed real-hyperbolic 4-manifold `Y` satisfies `chi >= 3|sigma|/2 + |d| chi(Y)`, with equality only if the domain is also real hyperbolic.  This supplies the needed all-sign no-Einstein conclusion for `N#N` when combined with the positive and zero sign arguments.
- `Knowledge/objects/papers/Einstein-metrics-and-exotic-smooth-structures--a999e7d0e856--006355a6a43b/object.md`, lines 66--73, says Sambusetti proved a topological obstruction for 4-manifolds admitting a nonzero-degree map onto compact real or complex hyperbolic 4-manifolds, and that the obstruction is homotopy-invariant.

The exact original Sambusetti paper remains a historical-attribution source gap, but the mathematical theorem needed here is recovered through Kotschick's statement and BCG.  The quantitative derivation below uses BCG directly and does not depend on a connected-sum entropy additivity theorem.

## Degree-two BCG lower bound for \(M=N\#N\)

Let \(N\) be a closed oriented real-hyperbolic 4-manifold with sectional curvature \(-1\), so
\[
\operatorname{Ric}_{g_0}=-3g_0,\qquad
\operatorname{Vol}(N,g_0)=\frac{4\pi^2}{3}\chi(N),\qquad \tau(N)=0.
\]
For \(M=N\#N\), there is a degree-two continuous map
\[
f:M\to N
\]
obtained by mapping both punctured summands to \(N\) with degree one and collapsing the neck.  BCG gives for every metric \(g\) on \(M\)
\[
h(g)^4\operatorname{Vol}(M,g)
\ge 2\cdot 3^4\operatorname{Vol}(N,g_0).
\]
If \(\operatorname{Ric}_g\ge -3(1+\varepsilon)g\), Bishop--Gromov gives
\[
h(g)\le 3\sqrt{1+\varepsilon}.
\]
Therefore
\[
\operatorname{Vol}(M,g)
\ge \frac{2\operatorname{Vol}(N,g_0)}{(1+\varepsilon)^2}.
\]
This part is for arbitrary metrics satisfying the Ricci lower bound; the Einstein equation is not used.  The essential volume lower bound is BCG applied to the degree-two map, while Bishop supplies only the entropy upper bound used to convert BCG into a volume estimate.

## Chern--Gauss--Bonnet upper bound under two-sided negative Ricci pinching

Assume in addition the normalized negative pinching
\[
-3(1+\varepsilon)g\le \operatorname{Ric}_g\le -3(1-\varepsilon)g,
\qquad 0<\varepsilon<1.
\]
Let \(r_i\) be Ricci eigenvalues.  The Chern--Gauss--Bonnet integrand contains
\[
\frac{s^2}{24}-\frac{|E|^2}{2}
=\frac{s^2}{6}-\frac{|\operatorname{Ric}|^2}{2}.
\]
This is not \(\frac14\sum_{i<j}r_ir_j\); that intermediate formula was an error in the first message.  Write \(r_i=-3x_i\), where \(x_i\in[1-\varepsilon,1+\varepsilon]\).  Then
\[
\frac{s^2}{24}-\frac{|E|^2}{2}
=\frac32\left[(\sum_i x_i)^2-3\sum_i x_i^2\right].
\]
The earlier Step 91 text had an erroneous factor \(1/3\) in the first term of this bracket; A02 message #616 caught it.  At \(x_i=1\) the corrected expression gives \(6\), as it must for \(\operatorname{Ric}=-3g\).  This quadratic is concave in each variable, so its minimum on the box occurs at a vertex.  For \(0<\varepsilon\le1/3\) the minimum vertex is \(x_1=\cdots=x_4=1-\varepsilon\), giving
\[
\frac{s^2}{24}-\frac{|E|^2}{2}\ge 6(1-\varepsilon)^2.
\]
The final incompatibility threshold below is always \(<1/3\) for \(\chi(N)\ge2\), so this range is sufficient for the near-pinched question.
For \(M=N\#N\),
\[
\chi(M)=2\chi(N)-2,
\]
so Chern--Gauss--Bonnet gives
\[
8\pi^2(2\chi(N)-2)
\ge 6(1-\varepsilon)^2\operatorname{Vol}(M,g),
\]
that is
\[
\operatorname{Vol}(M,g)
\le \frac{8\pi^2(2\chi(N)-2)}{6(1-\varepsilon)^2}
=\frac{2\operatorname{Vol}(N,g_0)(1-1/\chi(N))}{(1-\varepsilon)^2}.
\]

## Quantitative obstruction

The BCG lower bound and CGB upper bound are incompatible when
\[
\left(\frac{1-\varepsilon}{1+\varepsilon}\right)^2>1-\frac1{\chi(N)}.
\]
Equivalently
\[
\varepsilon<\varepsilon_\chi:=
\frac{1-\sqrt{1-1/\chi(N)}}{1+
\sqrt{1-1/\chi(N)}}
=\frac{1}{4\chi(N)}+O(\chi(N)^{-2}).
\]
In absolute operator norm \(\delta=3\varepsilon\) for \(|\operatorname{Ric}+3g|\le\delta g\), the threshold is approximately
\[
\delta<\frac{3}{4\chi(N)}.
\]
The executable calculation and table are in `workspace/scripts/step91_sambusetti_bcg_pinching_threshold.py` and `workspace/data/step91_sambusetti_bcg_pinching_threshold.json`.

## Meaning for the negative branch

This is a genuine quantitative obstruction to making \(N\#N\) too close to \(\operatorname{Ric}=-3g\).  It goes in the opposite direction from a counterexample construction: it says a defect below the explicit \(O(1/\chi(N))\) threshold is impossible if the above two-sided pinching holds.  Therefore a hyperbolic connected-sum refutation of the normalized negative branch would need a family of no-Einstein manifolds with maximum Ricci defect \(\delta_i\to0\) while staying on the allowed side of this lower bound.  It need not have the exact rate \(C/\chi(N_i)\); any decay to zero would defeat a fixed normalized negative interval.  Conversely, a construction below the threshold would contradict the BCG--CGB estimate rather than sharpen it.  Increasing hyperbolic volume does not by itself dilute a maximum-norm neck error; a useful construction must exhibit a geometric mechanism that genuinely reduces the local connector defect.

The result does not prove or disprove the full Yau--26 proposition.  It gives a central target for A03's graph/hyperbolic connector: construct \(N_i\#N_i\) metrics with \(\delta_i\to0\), or prove a stronger connector lower bound preventing such decay.  It also clarifies that Lohkamp's negative-Ricci flexibility is not enough for a fixed tight negative interval: if \(\operatorname{Ric}\in[-b,-a]g\), constant scaling preserves the ratio \(b/a\), so fitting a prescribed interval \([c,C]\) with \(c<C<0\) requires comparable two-sided pinching, not just \(\operatorname{Ric}<0\).  Positive-only intervals are unaffected by negative-Ricci flexibility.

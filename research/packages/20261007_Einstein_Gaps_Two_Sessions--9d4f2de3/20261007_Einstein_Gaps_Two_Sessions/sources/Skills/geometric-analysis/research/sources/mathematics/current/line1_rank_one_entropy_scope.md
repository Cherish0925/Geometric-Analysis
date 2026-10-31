# Rank-one degree entropy does not add a budget in the classical monopole family

23 September 2026. This is a composition of classical mapping rigidity,
canonical-divisor positivity, and curvature inequalities. It closes one
specific proposed route to an independent budget; it is not a new Einstein
nonexistence theorem. It applies to the entire classical family below, not
only to the ball-quotient examples used in the two-chirality application.

## 1. Statement

Let
\[
 M=X\#k\overline{\mathbb {CP}}^{\,2}\#m(S^1\times S^3),\qquad
 A=c_1^2(X)>0,\quad h=(k+4m)/A,
\]
where \(X\) is a closed minimal complex surface of general type and
\(k,m\ge0\). Give \(X\) its complex orientation. Then:

1. Every continuous map from \(M\) to a closed real-hyperbolic
   four-manifold has degree zero.
2. If \(f:M\to Y\) maps to a closed complex-hyperbolic surface and
   \(D=|\deg f|>0\), then
   \[
   \boxed{D\,c_1^2(Y)\le A.}                              \tag{1}
   \]
3. For every metric whose Ricci eigenvalues lie in
   \([-1-\delta,-1+\delta]\), with \(0\le\delta<1\), the classical
   scalar monopole bound gives
   \[
   \boxed{\operatorname{Vol}(M,g)
          \ge\frac{2\pi^2 A}{(1+\delta)^2}.}              \tag{2}
   \]
   Every ordinary degree-to-complex-hyperbolic BCG/Bishop lower bound is
   no larger than \(64/81\) times the right side of (2).

Consequently, the ordinary rank-one target degree inequalities do not
strengthen the available volume lower budget for pointwise negative
Ricci input on this family. For exact negative Einstein candidates their
energy and Chern--Weil consequences are already weaker than the classical
monopole Ricci-energy bound. This is a comparison of these specified
inequalities, not a claim that all entropy, representation, or harmonic-map
methods have been exhausted.

## 2. Why all degree comes from the Kähler summand

For any aspherical target \(Y\), pinch the connected-sum necks to obtain
\[
 q:M\longrightarrow
 X\vee\bigvee_{1}^{k}\overline{\mathbb {CP}}^{\,2}
      \vee\bigvee_{1}^{m}(S^1\times S^3).
\]
This map induces the free-product isomorphism on fundamental groups.
Maps to \(Y=K(\pi_1Y,1)\) are classified, up to free homotopy, by
fundamental-group homomorphisms up to conjugation. Thus every \(f\) is
homotopic to \(F\circ q\) for a map on the wedge, obtained by restricting
its fundamental-group homomorphism to the summands. The fundamental class
is sent by \(q\) to the sum of their fundamental classes, so degrees add.

The simply connected projective-plane summands map null-homotopically.
A map from \(S^1\times S^3\) to \(Y\) is homotopic to one factoring
through \(S^1\), since this realizes the same fundamental-group map.
These summands therefore have degree zero. There is a continuous map
\(f_X:X\to Y\) satisfying
\[
 \deg f_X=\deg f.                                        \tag{3}
\]
This argument does not presume that the unknown metric on \(M\) is
Kähler or that an embedded copy of the punctured \(X\) is geometrically
adapted to it.

Minimal surfaces of general type are projective and hence Kähler. Give
\(X\) any Kähler metric and replace \(f_X\) by its harmonic representative
into the closed nonpositively curved target. For a real-hyperbolic target,
Sampson's rank theorem gives rank at most two, so its four-dimensional
degree is zero. For a complex-hyperbolic target, a nonzero degree forces
real rank four somewhere; harmonic rigidity then makes the map
holomorphic or antiholomorphic. These precise alternatives are recorded
in Carlson--Toledo, Corollary 3.7; harmonic representative existence is
also used there. In complex dimension two conjugating the target complex
structure preserves its real orientation and its canonical square.

## 3. The degree bound is a canonical intersection calculation

We can therefore assume \(f_X:X\to Y\) is holomorphic of degree \(D\).
It is surjective and generically finite. The determinant of its
differential gives the canonical divisor identity
\[
 K_X=f_X^*K_Y+R,
\]
where the ramification divisor \(R\) is effective. The canonical class
\(K_X\) is nef because \(X\) is minimal of general type; \(K_Y\) is
ample, so \(f_X^*K_Y\) is nef. It follows that
\[
 A-Dc_1^2(Y)
 =K_X^2-(f_X^*K_Y)^2
 =R\cdot(K_X+f_X^*K_Y)\ge0.
\]
This proves (1), including maps with ramification and exceptional fibres.
No assumption that \(f_X\) is an unramified covering is used.

## 4. Compare the budgets at the actual pointwise normalization

Normalize the complex-hyperbolic metric \(g_Y\) by
\(\operatorname{Ric}_{g_Y}=-g_Y\), and write \(B=c_1^2(Y)\). Then
\[
 V_Y=2\pi^2B,\qquad h_{\rm vol}(g_Y)^4=64/9.
\]
For example, the holomorphic-sectional-curvature \(-4\) normalization
has Ricci \(-6g\) and entropy \(4\); scaling by six gives the displayed
values. Equivalently they give exactly the \(32/81\) coefficient in
Kotschick's complex-hyperbolic degree obstruction.

BCG's degree inequality and Bishop comparison under
\(\operatorname{Ric}_g\ge-(1+\delta)g\) give
\[
 h_{\rm vol}(g)^4 V\ge (64/9)D V_Y,
 \qquad h_{\rm vol}(g)^4\le9(1+\delta)^2.
\]
Hence the lower number furnished by this method is
\[
 \boxed{V\ge\frac{64}{81}
              \frac{2\pi^2DB}{(1+\delta)^2}.}             \tag{4}
\]
On the other hand, the polarized actual monopole class on \(M\) has
\((a_g^+)^2\ge A\), including the classical small-\(b_+\) chamber and
handle-insertion hypotheses supplied in the inherited closure proof.
The scalar inequality gives
\[
 32\pi^2A\le\int s^2
           \le16(1+\delta)^2V,
\]
which is (2). By (1), the right side of (4) is at most \(64/81\) of
the right side of (2). This comparison is uniform over every target
and every degree map. An arbitrary collection of such lower bounds
can be maximized, not added; its supremum remains dominated.

For any normalized exact negative Einstein metric put
\(e=\int|\operatorname{Ric}|^2/(8\pi^2A)=V/(2\pi^2A)\).
Equation (4) reads \(e\ge(64/81)DB/A\le64/81\).
The classical all-metrics Ricci bound is stronger:
\[
 e\ge1+h.                                                \tag{5}
\]
Indeed, the scalar--Weyl defect \(\mathscr D_{\rm LB}\ge0\) gives
\(\int|\operatorname{Ric}|^2
 =8\pi^2(2p-T)+32\pi^2\mathscr D_{\rm LB}\), with
\(p\ge A\), \(T=A(1-h)\). Thus (5) does not depend on attainment of an
energy infimum.

In the range \(0<h<1/3\), the stronger classical Einstein envelope
\(e\ge F(h)>1+h\) already implies all these entropy lower bounds.
In terms of the two-chirality upper budget \(U\), Kotschick's necessary
degree inequality is \(U>(64/81)DB/A\); any candidate with
\(U\ge F(h)\) automatically passes it. It therefore cannot close the
remaining region \(U-F(h)>0\) by this particular comparison.

## 5. Scope and research consequence

This note provides a family-wide reason to stop repeatedly seeking the
missing budget from ordinary four-dimensional rank-one target degree
comparisons on the classical family. The result includes the realized
ball-quotient cover examples, but is not limited to them.

It does not cover Bauer--Furuta connected sums of non-Kähler symplectic
summands: the Kähler source and nef canonical argument above would have
to be replaced. It also does not bound the manifold's actual minimal
entropy from above, rule out additional quantitative stability inputs,
or concern targets of higher rank, representations without ordinary
degree maps, noncompact targets, or orbifold degree transfers.
It supplies no new pointwise approximation and no new no-Einstein type.
The unrestricted integral dilution examples in Round 18 and the
real-hyperbolic surgery comparison in Round 19 remain different results.

## Sources and finite checks

- Carlson--Toledo, *Harmonic mappings of Kähler manifolds to locally
  symmetric spaces*, IHÉS 69 (1989), Corollaries 3.3--3.7:
  <https://www.numdam.org/item/10.1007/BF02698844.pdf>.
- Besson--Courtois--Gallot, *Entropies et rigidités des espaces localement
  symétriques de courbure strictement négative*, GAFA 5 (1995), main theorem:
  <https://www.aimath.org/WWN/entropyrigidity/papers/BessonCourtoisGallot.pdf>.
- Kotschick, *Entropies, volumes, and Einstein metrics*, Corollary 3,
  equation (15): <https://arxiv.org/html/math/0410215>.
- LeBrun, *Ricci Curvature, Minimal Volumes, and Seiberg--Witten Theory*,
  Proposition 3.2 and the Ricci-energy inequality:
  <https://arxiv.org/html/math/0003068>.

`check_line1_rank_one_entropy_scope.py` checks the scale factors, the
volume/energy domination, and the translation to Kotschick's coefficient.
It does not check the harmonic-map or Seiberg--Witten existence theorems.

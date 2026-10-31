# Canonical classes and the full ordinary Seiberg--Witten basic set

21 September 2026.

## 1. Statement

Let \(M=M(h,g;u,f)\), \(h\ge1\), \(g\ge2\), be obtained by
self-gluing the two boundary components of
\(B=F_{h,2}\times\Sigma_g\) by
\((\phi,x)\mapsto(-\phi+u(x),f(x))\). The gluing is as in
`round11_graph_topology.md`; in particular \(u\ne0\) in integral
cohomology and \(f\) is orientation preserving. We use the symplectic
forms and the closed metric sequence
constructed in `round11_closed_gluing.md`.

Here \(\chi=4h(g-1)\ge4\), while the stable-letter quotient
\(\pi_1(M)\to\mathbb Z\) gives \(b_1\ge1\). Since \(\tau=0\),
\(b^+=b^-=\chi/2+b_1-1\ge2\); the chamber-independent gauge
theory and Taubes theorem below therefore apply in both orientations.

The two symplectic forms determine an oriented splitting
\(TM=E\oplus F\) into real two-plane bundles. Here \(E\) is tangent
to the first surface factor on block interiors and to the
\((t,\phi)\) planes on the neck; \(F\) is the complementary plane
bundle used by the symplectic pair. Set

\[
 x=e(E),\qquad y=e(F),\qquad a=x+y,\qquad b=x-y.
 \tag{1}
\]

Thus \(a=c_1(TM,J_+)\) and \(b=c_1(TM,J_-)\); the corresponding
canonical bundle classes are \(-a\) and \(-b\).
All unqualified intersection products use the \(J_+\) orientation.

**Theorem.** The canonical data satisfy

\[
 x^2=y^2=0,\qquad x\cdot y=\chi(M),
 \qquad
 \begin{pmatrix}a^2&a\cdot b\\a\cdot b&b^2\end{pmatrix}
 =\begin{pmatrix}2\chi&0\\0&-2\chi\end{pmatrix}.
 \tag{2}
\]

The ordinary Seiberg--Witten basic first-Chern classes are exactly

\[
 \boxed{\mathcal B(M)=\{a,-a\},\qquad
        \mathcal B(-M)=\{b,-b\}.}
 \tag{3}
\]

These are statements about integral first-Chern classes, not only
their real images. No order condition on \([f]\), and no rank condition
on \(I-f_*\), is required. The argument does not enumerate distinct
Spin\(^c\) structures sharing a first-Chern class when two-torsion
is present. In the explicit torsion-free example from Round 11 that
ambiguity does not arise.

The proof uses the actual near-Einstein construction to constrain
the entire basic set; it is not a computation by formal gluing of
Seiberg--Witten polynomials. It also gives, in both orientations,

\[
 \alpha^2(M)=\beta^2(M)=2\chi(M)
 \tag{4}
\]

for LeBrun's period-plane minimax and monopole convex-hull invariants.
Equation (4) concerns all monopole classes, potentially more than
the ordinary basic classes in (3).

This calculation does not exclude an arbitrary negative Einstein
metric. It determines the available ordinary basic classes and shows
that the numerical convex-hull and period-plane refinements cannot
raise the topological monopole budget above \(2\chi\).

## 2. Euler classes of the two plane bundles

The gluing preserves \(E\): derivatives of the circle-valued shear
mix the transverse plane into the circle direction, but do not mix
an \(E\)-vector into the transverse plane. In signed normal and
circle coordinates, its restriction to \(E\) is the constant matrix
\(-I\). This observation permits a particularly simple connection.

Choose a connection on \(TF_{h,2}\) which is flat in the product
frames on its boundary collars. Pull it back to \(E\) in the block.
Its flat collar connections glue across the constant transition
\(-I\). The resulting global Euler form is supported in the block
interior and is pulled back from a two-form on \(F_{h,2}\).
Its square vanishes pointwise. Thus \(x^2=0\).

The Euler and Pontryagin identities for an oriented two-plane
splitting give

\[
 e(TM)=x y,\qquad p_1(TM)=x^2+y^2.
\]

Since \(\tau(M)=0\), their evaluations give \(xy=\chi\) and
\(y^2=0\). Expanding (1) proves (2). In particular the two canonical
classes are not two positive-square basic classes in one orientation:
the second one is a basic class for the opposite orientation.

## 3. Energy saturation constrains every basic class

Write \(Q=2\chi>0\). Round 11 supplies metrics \(g_j\) with

\[
 \frac{1}{32\pi^2}\int_M s_{g_j}^2\,d\mu_{g_j}
       =:A_j\longrightarrow Q.
 \tag{5}
\]

For each monopole class \(c\), the scalar-curvature estimate gives
\((c_{g_j}^+)^2\le A_j\). The estimate and its normalization are
proved from the monopole equations in `round11_variational.md`,
Section 2; the primary source is
[LeBrun, *Ricci Curvature, Minimal Volumes, and Seiberg--Witten Theory*, Section 2](https://arxiv.org/pdf/math/0003068).

If \(c\) is an ordinary basic class, its nonzero invariant requires
nonnegative expected dimension

\[
 d(c)=\frac{c^2-(2\chi+3\tau)}4=\frac{c^2-Q}4\ge0.
\]

Negative-dimensional generic moduli spaces are empty. Conversely,
the projection estimate implies \(c^2\le A_j\), hence \(c^2\le Q\).
It follows that every ordinary basic class has

\[
 c^2=Q,\qquad d(c)=0,
 \qquad \|c_{g_j}^-\|^2=(c_{g_j}^+)^2-Q\longrightarrow0.
 \tag{6}
\]

Here \(\|c^-\|^2=-c^-\cdot c^-\). The same holds for the
canonical class \(a\). Cauchy--Schwarz on the two Hodge summands
therefore gives

\[
 |a\cdot c|
 \le\sqrt{(a_{g_j}^+)^2(c_{g_j}^+)^2}
       +\|a_{g_j}^-\|\,\|c_{g_j}^-\|
 \le A_j+(A_j-Q).
\]

Taking the limit proves the metric-independent constraint

\[
                  |a\cdot c|\le Q.                       \tag{7}
\]

This argument obtains simple type directly from the sharp
scalar-energy sequence, so a separate simple-type theorem is not
being assumed.

## 4. Product tori and the neck subspace

Every product of embedded loops in the interior of \(F_{h,2}\)
and in \(\Sigma_g\) is an embedded torus with trivial normal
bundle. The adjunction inequality forces every basic class to have
zero pairing with such a torus. If a particular torus is torsion
or nullhomologous, the same zero pairing is automatic. The precise
self-intersection-zero torus consequence is stated in
[Fintushel--Stern, *Knots, Links, and 4-Manifolds*, Section 2, p. 9](https://arxiv.org/pdf/dg-ga/9612014).

The product tori span
\(H_1(F_{h,2};\mathbb R)\otimes H_1(\Sigma_g;\mathbb R)\).
Künneth's theorem and \(H^2(F_{h,2};\mathbb R)=0\) therefore give

\[
 c|_B=d\,\eta,\qquad a|_B=(2-2g)\eta,                    \tag{8}
\]

where \(\eta\) is the pullback of the integral generator of
\(H^2(\Sigma_g)\), and \(d=c[\{p\}\times\Sigma_g]\).
Since \(2-2g\ne0\), every basic class can be written over
\(\mathbb R\) as

\[
 c=t a+r,\qquad
 t=\frac d{2-2g},\qquad
 r\in R:=\ker\bigl(H^2(M;\mathbb R)\to H^2(B;\mathbb R)\bigr).
 \tag{9}
\]

Cut along the nonseparating gluing hypersurface
\(Y=S^1\times\Sigma_g\). The Mayer--Vietoris connecting map
\(\delta:H^1(Y;\mathbb R)\to H^2(M;\mathbb R)\) has image
\(R\). Its classes have representatives
\(\rho(t)dt\wedge\theta\), where \(\theta\) is closed on
\(Y\), and \(\rho\) is supported in a small neck with
\(\int\rho\,dt=1\). Any two such representatives have zero
wedge product. Consequently

\[
                         R\cdot R=0.                     \tag{10}
\]

Use (6) in (9). If \(t=0\), (10) would give \(c^2=0\),
contrary to \(Q>0\). For \(t\ne0\),

\[
 Q=t^2Q+2t(a\cdot r),\qquad
 a\cdot c=\frac Q2\left(t+\frac1t\right).                 \tag{11}
\]

For a real nonzero \(t\), \(|t+t^{-1}|\ge2\), with equality
only for \(t=\pm1\). Combining (7) and (11) forces

\[
              c=\pm a+r,\qquad r\in R,\qquad a\cdot r=0. \tag{12}
\]

Thus neither a different fibre evaluation nor a nonzero canonical
pairing in the neck subspace can produce another basic class.

## 5. Taubes extremality removes the remaining neck classes

Fix one of the positive-orientation symplectic forms \(\Omega\)
from Round 11. On any neck slice \(Y\), its restriction is the
fibre area form \(\omega\); the term containing \(dt\) restricts
to zero. Thus

\[
 [\Omega|_Y]=\operatorname{Area}(\Sigma_g,\omega)\eta,
 \qquad a|_Y=(2-2g)\eta.
\]

The connecting-map pairing, evaluated using the representatives
above, gives for every \(r=\delta[\theta]\in R\)

\[
 r\cdot[\Omega]
 =\frac{\operatorname{Area}(\Sigma_g,\omega)}{2-2g}\,
      r\cdot a.                                         \tag{13}
\]

The common sign from the orientation convention for \(\delta\)
cancels in the ratio. Equation (12) therefore implies
\(|c\cdot[\Omega]|=|a\cdot[\Omega]|\).

[Taubes, *More Constraints on Symplectic Forms from Seiberg--Witten Invariants*, Theorem 2](https://archive.intlpress.com/site/pub/files/_fulltext/journals/mrl/1995/0002/0001/MRL-1995-0002-0001-a002.pdf)
states that the canonical bundle class uniquely maximizes the absolute
symplectic pairing among basic classes, up to sign. Its equality
conclusion is an equality of integral classes. Since that canonical
class is \(-a\), (12)--(13) force \(c=\pm a\) integrally.
Both signs occur, and their invariants have absolute value one by
Taubes's theorem. This proves the first assertion of (3).

The same argument applies in the opposite symplectic orientation.
There \(b^2_{-M}=Q\), the scalar-energy limit is unchanged, the
neck subspace is still isotropic, and the restriction of the
symplectic form to \(Y\) is again proportional to the restriction
of \(b\). It yields \(\mathcal B(-M)=\{b,-b\}\).

## 6. A direct check in the smallest even-Betti example

For completeness, the example \(h=1,g=2\) with
\(f_* =\operatorname{diag}(H,H)\),
\(H=\left(\begin{smallmatrix}2&1\\1&1\end{smallmatrix}\right)\),
has a shorter real-cohomology conclusion before invoking Taubes
extremality. Its neck exact sequence is

\[
 H^1(B;\mathbb R)\xrightarrow{D}H^1(Y;\mathbb R)
 \xrightarrow{\delta}H^2(M;\mathbb R)\longrightarrow H^2(B;\mathbb R).
\]

The image of \(D\), in
\(H^1(Y)=\mathbb R[d\phi]\oplus H^1(\Sigma_g)\), is

\[
              \operatorname{im}(I-f^*)+\mathbb R[u].      \tag{14}
\]

There is no circle component: the two boundary evaluations of a
one-form on \(F_{h,2}\) are opposite, and the gluing reverses the
circle. Its remaining contribution is a multiple of \(u\).
Here \(\det(I-f_*)=1\), so \(R\) is one-dimensional, generated
by \(\delta[d\phi]\), with \(d\phi\) normalized to have
period one. Its pairing with \(a\) is
\(\pm(2-2g)\ne0\). Hence \(R\cap a^\perp=0\), and (12)
already gives \(c=\pm a\) over \(\mathbb R\).

Round 11's integer Smith-normal-form computation gives
\(H_1(M;\mathbb Z)=\mathbb Z^4\), so \(H^2(M;\mathbb Z)\)
has no torsion. This also gives the integral conclusion directly.
The example has
\(\chi=4\), \(\tau=0\), \(b_1=4\), \(b^+=b^-=5\), and
the canonical Gram matrix is \(\operatorname{diag}(8,-8)\).

## 7. Convex-hull and minimax values, and the Einstein question

Let \(\mathcal C(M)\subset H^2(M;\mathbb R)\) be the finite
set of nonzero monopole classes. The definitions of \(\beta^2\)
and \(\alpha^2\) are those in
[LeBrun, *Four-Manifolds, Curvature Bounds, and Convex Geometry*, Definition 4.3 and Section 5](https://arxiv.org/pdf/math/0611450):

\[
 \beta^2=\max_{v\in\operatorname{Hull}(\mathcal C)}v^2,
 \qquad
 \alpha^2=\inf_{H}\max_{c\in\mathcal C}(c_H^+)^2,
\]

where \(H\) ranges over maximal positive subspaces of the real
intersection form. For a convex combination \(v\) of monopole
classes, the projection norm is at most \(\sqrt{A_j}\) by (5)
and the triangle inequality. Thus \(v^2\le A_j\), implying
\(\beta^2\le Q\). The actual Hodge planes of \(g_j\) are
admissible in the minimax, so \(\alpha^2\le\lim A_j=Q\).
The canonical monopole class has square \(Q\), which gives both
opposite inequalities. This proves (4). Reverse orientation gives
the same result.

Equation (3) does not classify monopole classes invisible to ordinary
Seiberg--Witten invariants, nor the Bauer--Furuta invariant. Equation
(4) nevertheless bounds every monopole class in the numerical schemes
specified there. A further gauge-theoretic obstruction would need
information beyond simply increasing these two numbers.

The two symplectic orientations also cannot be pooled into a single
positive-square basic set: (2) records their opposite intersection
signs. In particular, the calculation leaves intact the remaining
possibility from Round 11 of a genuinely non-Kähler negative Einstein
metric with normalized volume strictly above \(4\pi^2\chi\).
No adapted splitting, holomorphic structure, or graph-preserving
property has been imposed on such an unknown metric.

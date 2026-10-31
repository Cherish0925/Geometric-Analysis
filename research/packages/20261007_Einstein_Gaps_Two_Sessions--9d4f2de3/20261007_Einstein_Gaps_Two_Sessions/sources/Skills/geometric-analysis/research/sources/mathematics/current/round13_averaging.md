# Collapsing-circle averaging and the nonlinear Einstein error

This note addresses the nonsymmetric modes of a possible exact repair of
the closed collars constructed in round 11. It is a local tensor estimate,
not an assumption that an exact metric preserves the approximate symmetry.

## 1. Geometric hypotheses and statement

Let a smooth circle action of period \(2\pi\) act freely and isometrically
on \((U,b)\), with generator \(X\), orbit radius \(a=|X|_b\), and
averaging operator

\[
 \mathsf A T=(2\pi)^{-1}\int_0^{2\pi}\Phi_\theta^*T\,d\theta.
\]

Assume on the invariant open set under consideration

\[
0<a\le1,\qquad |\mathrm{Rm}_b|\le C_0,\qquad
|\nabla X|_b\le C_0a.
\tag{1}
\]

All norms and derivatives below use \(b\). Let \(q=b+h\) be positive
definite and \(\|h\|_{C^2(b)}\le\eta\le\eta_0\), where \(\eta_0\)
is a sufficiently small dimensional constant. Set

\[
\bar q=\mathsf A q,\qquad k=q-\bar q.
\]

**Proposition.** Uniformly in the orbit radius,

\[
 |k|\le C a^2\eta,\qquad |\nabla k|\le C a\eta,
 \qquad |\nabla^2k|\le2\eta,
\tag{2}
\]

and, for any fixed real \(\lambda\),

\[
\left|\mathrm{Ric}_{\bar q}-\lambda\bar q
 -\mathsf A(\mathrm{Ric}_{q}-\lambda q)\right|_b
 \le C a^2\eta^2.
\tag{3}
\]

The constant depends on \(C_0\) and dimension, not an injectivity
radius. In particular, an exact Einstein metric \(q\) in this
\(C^2\) neighborhood produces a circle-invariant metric \(\bar q\)
with Einstein error \(O(a^2\eta^2)\), rather than merely
\(O(\eta^2)\).

## 2. Why two powers of the orbit radius occur

Covariant differentiation commutes with pullback by a \(b\)-isometry.
Thus \(\mathsf A\nabla^jk=0\), for \(j=0,1,2\), and
\(\|k\|_{C^2}\le2\eta\).

For any tensor \(T\) with \(\mathsf A T=0\), pull it back along an
orbit to its starting point. This is a periodic function with values
in a fixed finite-dimensional normed vector space and mean zero.
The one-dimensional periodic Poincare estimates give

\[
|T|\le C\sup_{\text{orbit}}|\mathcal L_XT|,
\qquad
|T|\le C\sup_{\text{orbit}}|\mathcal L_X^2T|.
\tag{4}
\]

The radius \(a\) is constant along each orbit. For a tensor of fixed
rank,

\[
\mathcal L_XT=\nabla_XT+(\nabla X)*T.
\]

Applying the first estimate to \(T=\nabla k\) therefore gives
\(|\nabla k|\le Ca\eta\). For the second estimate applied to
\(k\), differentiate this Lie derivative once more. The resulting
terms are bounded by

\[
C\{a^2|\nabla^2k|+
(a|\nabla X|+|\nabla_XX|)|\nabla k|+
(|\nabla X|^2+|\nabla_X\nabla X|)|k|\}.
\]

Since \(X\) is Killing, its second covariant derivative is a curvature
contraction with \(X\). Assumptions (1) consequently bound every
coefficient here by \(Ca^2\). The second estimate in (4) yields
\(|k|\le Ca^2\eta\). No PDE estimate or inverse Einstein operator is
being used in this step.

## 3. Averaging the nonlinear equation

Let \(F(g)=\mathrm{Ric}_g-\lambda g\). Tensorial naturality and
circle invariance of \(\bar q\) imply

\[
\mathsf A(DF_{\bar q}k)=DF_{\bar q}(\mathsf A k)=0.
\tag{5}
\]

In the fixed background connection, the difference-of-connections
formula for Ricci gives the pointwise Taylor remainder estimate

\[
|F(\bar q+k)-F(\bar q)-DF_{\bar q}k|
\le C\bigl(|k||\nabla^2k|+|\nabla k|^2+
|k||\nabla k|+|k|^2\bigr).
\tag{6}
\]

The coefficients are uniformly bounded because \(\bar q\) is
\(C^2\)-close to \(b\), the metrics are uniformly equivalent, and
\(|\mathrm{Rm}_b|\) is bounded. The term \(-\lambda g\) has no
Taylor remainder. Insert (2), average (6), and use (5) to obtain (3).

## 4. Consequence for a weighted obstruction

If \(q\) is exact Einstein and \(\bar a=|X|_{\bar q}\), then
\(\bar a/a\) is uniformly bounded above and below. In any orthonormal
horizontal/vertical pair for \(\bar q\),

\[
\bar D=\mathrm{Ric}_{\bar q}(\bar U,\bar U)
       -\mathrm{Ric}_{\bar q}(\bar T,\bar T)
\quad\hbox{satisfies}\quad
|\bar D|\le Ca^2\eta^2.
\tag{7}
\]

Thus a scalar receiver whose error weight is \(1/a\) in physical
normal time has a total nonsymmetric forcing at most

\[
\int |\bar D|/a\,dt\le C\eta^2\int a\,dt.
\tag{8}
\]

For the round-11 collar, \(\int a\,dt\le2a(L)/\sqrt3\).
The collapsing end radius suppresses this forcing. This is the
relevant comparison for an obstruction; the coarser unweighted
\(O(\eta^2)\) bound would instead lose a factor \(1/\ell\).

The quotient metric and radius of \(\bar q\) can depend on the fibre
point. One must therefore use the optical receiver of
`round13_radius.md`, when its global foliation hypotheses hold, rather
than applying the older receiver which assumed \(a=a(t)\).

Here is a direct all-mode consequence, with its geometric hypothesis
made explicit. Suppose the averaged quotient admits the optical
foliation of `round13_radius.md` between the marked faces, and for
some end scale \(A\le1\) and constants \(c_0,C_1,d_0>0\),

\[
 \bar a_\pm\ge c_0A,\quad |H_\pm|\le C_1\eta,\quad
 A_{\rm opt}=\sup_x\int\bar a^2 ds\le C_1A,\quad
 d_{\mathcal T}([h_-],[h_+])\ge d_0.
\tag{9}
\]

Then the optical receiver, applied to \(\bar q\) and (7), gives

\[
 d_0^2\le C\eta+C A^2\eta^2.                       \tag{10}
\]

Consequently \(\eta\) has a positive lower bound depending only on
the displayed constants and \(d_0\), not the collapsing parameter.
The putative Einstein metric \(q\) need not have any circle symmetry.
This excludes small repairs in **all tensor modes** whenever (9)
holds. The radius/foliation bounds in (9) are conditions on the
averaged metric, not consequences claimed from \(C^2\)-smallness
alone. In particular, caustics or failure of a common optical arrival
face have not been eliminated.

Even without (9), the averaging reduction shows that nonzero circle
modes cannot supply an arbitrary order-one forcing to the invariant
equations while remaining geometrically \(C^2\)-small.

## 5. The order \(a^2\eta^2\) is genuine

On a flat product with circle radius \(a\) in dimension \(n\ge3\),
put \(u=\eta a^2\cos\theta\) and \(q=e^{2u}b\). Then
\(\bar q\) is a constant multiple of \(b\), hence Ricci flat.
The conformal Ricci formula gives in each transverse unit direction

\[
\mathsf A\mathrm{Ric}_{q}
=-(n-2)\mathsf A(u_\theta^2/a^2)
=-\tfrac{n-2}{2}\eta^2a^2.
\tag{11}
\]

Thus the Ricci-averaging commutator has exactly the order in (3).
For small \(\eta\), this example has \(C^2\)-distance at most
\(C\eta\) from \(b\); a fixed rescaling of \(\eta\) places it in
the convention of the proposition.
This example tests the estimate, not the Einstein equation: these
\(q\)'s are not asserted to be Einstein. The companion exact symbolic
check derives their Ricci tensor from the coordinate connection.

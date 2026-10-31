# A necessary restriction on the proposed rank-one route

> Final connection: this counterexample explains why the Ricci-energy hypothesis in the subsequently proved `O10_Topological_Escape.md` is essential. It does not contradict that lemma or the finite-density O10 theorem.

2026-09-29. This note addresses a specific proposed inference for a section of a Hermitian line bundle. It is not an O10 counterexample.

## Claim that cannot be used

The following properties, without any control of the geometry or an equation for the section, do **not** force normalized first-Chern square to vanish:

\[
 |\sigma_j|\to1\text{ in measure},\qquad
 \|\sigma_j\|_{L^4_{\rm avg}}+\|\nabla\sigma_j\|_{L^2_{\rm avg}}\le C,
 \qquad |F_j|\le C.
\tag{1}
\]

In particular, replacing the last condition by uniform integrability of curvature squares does not make the implication valid.

## Construction

Let L be a degree-one Hermitian line bundle on an oriented two-sphere. Choose three nested coordinate discs

\[
 D_0\Subset D_1\Subset D_2\Subset S^2.
\]

Choose a smooth section s with one simple zero in D0 and norm identically one outside D0. Such a section exists: the degree-one clutching description gives a single-index-one section, and its positive norm away from the zero can be rescaled to one outside D0. The Hermitian metric and the section are fixed from now on.

Choose a unitary connection whose curvature is supported outside D2. To see this directly, start with any unitary connection and choose a smooth imaginary two-form F supported outside D2 with

\[
 \frac{i}{2\pi}\int_{S^2}F=1.
\]

The difference between F and the original curvature is exact, so adding a global imaginary one-form to the connection realizes F. On D2 the connection is flat; since D2 is simply connected it admits a parallel frame there. These choices do not require s to be parallel.

Let g0 be a fixed smooth metric, round on D1. Choose a smooth function \(0\le\chi\le1\), equal to one on D1 and zero outside D2. For \(0<\epsilon<1\), set

\[
 g_\epsilon=\epsilon^{2\chi}g_0.
\tag{2}
\]

The curvature F has uniformly bounded norm with respect to these metrics, because the metrics equal g0 on its support. Their areas converge to a positive number: the region outside D2 keeps its fixed positive area.

The amplitude defect is supported in D0, whose area is multiplied by \(\epsilon^2\). Thus \(|s|\to1\) in normalized measure. On the other hand, the covariant Dirichlet energy in two dimensions is conformally invariant:

\[
 \int_{S^2}|\nabla s|_{g_\epsilon}^2\,dA_{g_\epsilon}
 =\int_{S^2}|\nabla s|_{g_0}^2\,dA_{g_0}=:E_s<\infty.
\tag{3}
\]

Now take

\[
 M=S^2\times S^2,
 \qquad G_\epsilon=g_\epsilon\oplus g_\epsilon,
 \qquad E=\operatorname{pr}_1^*L\otimes\operatorname{pr}_2^*L,
 \qquad \sigma=s\otimes s.
\]

Use the product connection. The amplitude defect is supported in the union of the two product sets with one factor in D0, and hence has vanishing relative volume. The section is uniformly bounded. Its Dirichlet energy is

\[
 \int_M|\nabla\sigma|^2\,dV_{G_\epsilon}
 =2E_s\int_{S^2}|s|^2\,dA_{g_\epsilon},
\tag{4}
\]

which is bounded. The total volume is bounded below, so the normalized energy is bounded as well.

The curvature is the sum of the two pulled-back curvatures. Orthogonality of the product factors and the support property give a uniform pointwise curvature bound. Nevertheless,

\[
 \boxed{c_1(E)^2[M]=2,\qquad
 \frac{c_1(E)^2[M]}{\operatorname{Vol}(M,G_\epsilon)}
 \longrightarrow\frac2{V_0}>0.}
\tag{5}
\]

All properties (1) hold, and the claimed Chern-square conclusion fails.

## Why this does not contradict O10

The construction does not have nearly negative Einstein Ricci curvature. On D1, round curvature rescales by \(\epsilon^{-2}\), and its squared integral diverges. The covariant rough Laplacian of s also need not be uniformly controlled.

Therefore a rank-one argument for the actual derived section \(\sigma\in L^5\) must use additional information from the original system. The most natural candidates are the normalized small Einstein residual, a genuine equation for sigma, or a signed differential identity linking its phase current to the actual self-dual curvature. A proof using only (1), even with the pointwise curvature strengthening shown here, cannot work.

## The same counterexample can have harmonic curvature

The failure is not repaired merely by adding \(\delta F=0\). On each sphere replace the connection by one with harmonic curvature

\[
 F_\epsilon=-\frac{2\pi i}{\operatorname{Area}(g_\epsilon)}
             dA_{g_\epsilon}.
\]

These forms have uniformly bounded pointwise norms in the varying metrics. They also have uniformly bounded coefficients in a fixed g0 norm, because the conformal factors in (2) are at most one and the areas stay bounded below.

Fix one reference connection with curvature \(F_*\). On the fixed sphere, choose its connection difference as

\[
 \alpha_\epsilon=d_{g_0}^*\Delta_{g_0}^{-1}(F_\epsilon-F_*).
\]

The difference has integral zero, and therefore \(d\alpha_\epsilon=F_\epsilon-F_*\). Fixed-metric elliptic estimates give a uniform W1,p bound for every finite p, hence a uniform C0 bound for p greater than two. The fixed section s retains a uniformly bounded covariant Dirichlet energy by two-dimensional conformal invariance and this connection bound.

On the product of the two identical spheres, the sum of the two pulled-back harmonic curvatures is self-dual and parallel. The amplitude, energy, and Chern-square conclusions above still hold. Ricci curvature remains uncontrolled. This strengthened version isolates why the Ricci hypothesis in the logarithmic resolvent lemma is substantive rather than optional.

# Doubling surface-cusp Einstein metrics on arbitrary circle bundles

21 September 2026.

## 1. A fixed-topology near-Einstein doubling lemma

Let \(P_\ell\to\Sigma\) be a fixed principal circle bundle over a closed
hyperbolic surface of genus \(g\ge2\), with Chern number \(\ell\in\mathbb Z\).
Fix the circle period and a complete invariant Einstein metric \(G\) on
\((0,\infty)\times P_\ell\), with
\(\operatorname{Ric}_G=-3G\), one smooth conformally compact end and one
surface-cusp end. Suppose its cusp has an equivariant identification with
\((R_0,\infty)\times P_\ell\) in which

\[
G_0=\frac13\,dr^2+c_0^2e^{-2r}\theta^2+h,\qquad
h=\frac13 h_\Sigma,\qquad
d\theta=f\,dA_h,\quad f\ \hbox{constant},
\tag{1}
\]

and, for \(j=0,1,2\),

\[
\left|\nabla_{G_0}^j(G-G_0)\right|_{G_0}
\le C_j e^{-\beta r},\qquad \beta>0.
\tag{2}
\]

The connection form \(\theta\) is global on \(P_\ell\); it is not a
global potential on the base. Normalize it by \(\theta(K)=1\) for the
fixed \(2\pi\)-periodic generator. Consequently
\(f\,\operatorname{Area}_h(\Sigma)=2\pi\ell\).
The constant \(c_0>0\) absorbs the circle-period normalization in the
source model.

**Doubling lemma.** For sufficiently small \(0<d<a_0\), with
\(a_0^\beta+d^2/a_0^2\) sufficiently small, there is a smooth,
complete, invariant metric \(g_{a_0,d}\) on the fixed manifold
\(\mathbb R\times P_\ell\), with two smooth conformally compact ends,
such that both ends are unchanged copies of the end of \(G\), and

\[
\boxed{\quad
\left\|g_{a_0,d}^{-1}
  (\operatorname{Ric}_{g_{a_0,d}}+3g_{a_0,d})\right\|_{\infty,\mathrm{op}}
\le C\left(a_0^\beta+a_0^2+\frac{d^2}{a_0^2}\right).
\quad}
\tag{3}
\]

Here \(C\) depends on the fixed source, bundle, connection and cutoff,
not on \(a_0,d\). In particular, taking \(d=a_0^2\) gives defect tending
to zero. The boundary conformal metrics and bundle degree are fixed
throughout the family.

Li--Liu's [*Poincaré--Einstein 4-manifolds with cusps*,
arXiv:2605.25462](https://arxiv.org/pdf/2605.25462), Definition 1.2,
Theorem 1.5, and the invariant construction in Sections 3--4 supply
these sources for every \(\ell\). Their cusp models (3)--(4) have constant
base and connection curvature; Definition 1.2 gives (2) at every finite
order. Their principal-circle ansatz provides the equivariant
identification. Their theorem constructs one PE end and one cusp,
not the two-PE approximate metric below. The doubling is a deduction
from that input.

## 2. The central metric and all its Ricci blocks

On \([-T-1,T+1]\times P_\ell\), put

\[
a(t)=d\cosh(\sqrt3\,t),\qquad
g_C=dt^2+a(t)^2\theta^2+h,\qquad
T=\frac1{\sqrt3}\operatorname{arcosh}(a_0/d).
\tag{4}
\]

Thus \(a(\pm T)=a_0\). The circle quotient has product metric
\(dt^2+h\). Let \(U=a^{-1}K\), let \(X,Y\) be horizontal vectors
tangent to \(\Sigma\), and set \(F=d\theta\). Circle-reduction formulas
give, with tensor norm \(|F|_{\rm tens}^2=F_{ij}F^{ij}\),

\[
\begin{aligned}
(\operatorname{Ric}_{g_C}+3g_C)(\partial_t,\partial_t)&=0,\\
(\operatorname{Ric}_{g_C}+3g_C)(U,U)
  &=\frac{a^2}{4}|F|_{\rm tens,h}^2,\\
(\operatorname{Ric}_{g_C}+3g_C)(X,Y)
  &=-\frac{a^2}{2}\langle\iota_XF,\iota_YF\rangle_h .
\end{aligned}
\tag{5}
\]

Every mixed component vanishes. Indeed, \(a''=3a\), the base Ricci
tensor is \(-3h\), the Hessian of \(a\) vanishes in surface directions,
and \(F=f\,dA_h\) is parallel with no radial component.
The mixed divergence of \(a^3F\) is zero even though \(a\) varies radially.

Since \(|F|_{\rm tens,h}^2=2f^2\), the four error eigenvalues are exactly

\[
0,\quad \frac{a^2f^2}{2},\quad
-\frac{a^2f^2}{2},\quad-\frac{a^2f^2}{2}.
\tag{6}
\]

On \(|t|\le T+1\), \(a(t)\le C a_0\), so the full operator error is
\(O(a_0^2)\). This applies to nontrivial bundles as well as to
\(\ell=0\); no nonexistent global base potential is used.

## 3. Relative two-jet matching on a collar of fixed width

Write \(s=t-T\) on the right overlap \(0\le s\le1\). Let
\(R=\log(c_0/a_0)\) and \(r=R-\sqrt3\,s\).
The source cusp model pulled back to this collar is

\[
\widehat G_0=ds^2+a_0^2e^{2\sqrt3s}\theta^2+h.
\tag{7}
\]

The source remainder has uniform covariant two-jet bound

\[
\sum_{j=0}^2
\left|\nabla_{\widehat G_0}^{\,j}
(\widehat G-\widehat G_0)\right|_{\widehat G_0}
\le C a_0^\beta.
\tag{8}
\]

The exponent remains \(\beta\), since
\(e^{-\beta R}=(a_0/c_0)^\beta\).
The proper-distance change introduces only fixed factors \(\sqrt3\).
On the same collar the central lapse is exactly

\[
a(T+s)=a_0\cosh(\sqrt3s)
       +\sqrt{a_0^2-d^2}\sinh(\sqrt3s).
\tag{9}
\]

For \(j=0,1,2\), its difference from \(a_0e^{\sqrt3s}\), divided by
\(a_0\), is bounded by \(C d^2/a_0^2\), using

\[
0\le a_0-\sqrt{a_0^2-d^2}
=\frac{d^2}{a_0+\sqrt{a_0^2-d^2}}
\le\frac{d^2}{a_0}.
\tag{10}
\]

In covariant form this gives

\[
\sum_{j=0}^2
\left|\nabla_{\widehat G_0}^{\,j}
(g_C-\widehat G_0)\right|_{\widehat G_0}
\le C d^2/a_0^2.
\tag{11}
\]

There is no inverse-injectivity-radius factor in these estimates.
For (11), use the unit vertical covector
\(\zeta=a_0e^{\sqrt3s}\theta\). Its structure equation is
\(d\zeta=\sqrt3\,ds\wedge\zeta+a_0e^{\sqrt3s}F\).
The coefficients and fixed-order derivatives in a lifted base frame
are uniformly bounded as \(a_0\to0\).
The difference tensor is a scalar \(O(d^2/a_0^2)\) times \(\zeta^2\),
and its first two scalar derivatives have the same bound.
Equation (8) is already covariant in this collapsing model, not an
estimate of unnormalized coordinate entries.

The left overlap is identical with \(s=-t-T\). Only the radial coordinate
is reversed.

## 4. Gluing and the uniform nonlinear estimate

Choose a fixed smooth \(\chi:[0,1]\to[0,1]\), zero near zero and one
near one. On the right collar set

\[
g=(1-\chi(s))g_C+\chi(s)\widehat G.
\tag{12}
\]

Use its reflected counterpart on the left, and continue with unmodified
copies of \(G\) beyond the collars. This is smooth because the cutoff
is constant near the endpoints; it is positive by convexity.
Equations (8)--(11) and the bounded covariant first and second
derivatives of \(\chi\) give

\[
\sum_{j=0}^2
|\nabla_{\widehat G_0}^{\,j}(g-\widehat G_0)|_{\widehat G_0}
\le C\left(a_0^\beta+d^2/a_0^2\right)=:Cq.
\tag{13}
\]

For \(Cq<1/2\), the metrics are uniformly equivalent.
Writing \(\nabla^0=\nabla^{\widehat G_0}\), the connection difference is

\[
A^k_{ij}=\frac12g^{k\ell}
  (\nabla_i^0g_{j\ell}+\nabla_j^0g_{i\ell}-\nabla_\ell^0g_{ij}),
\]

and
\[
\operatorname{Ric}(g)_{ij}-\operatorname{Ric}(\widehat G_0)_{ij}
=\nabla_k^0A^k_{ij}-\nabla_j^0A^k_{ik}
 +A^k_{k\ell}A^\ell_{ij}-A^k_{j\ell}A^\ell_{ik}.
\]

Hence the Ricci difference has norm at most \(C(q+q^2)\).
This pointwise estimate uses no elliptic inverse, Sobolev constant,
or injectivity-radius lower bound.
The model (7) satisfies (5), with exponential \(a\), so its defect is
\(O(a_0^2)\). This proves (3) on both collars. Equation (6) proves
it in the center; the defect is exactly zero on the retained source.

## 5. Global geometry and quantized circle curvature

Both gluings identify the same marked \(P_\ell\) by the identity.
They reverse only the radial coordinate on one copy. They do not reverse
the fibre generator, base orientation or connection. Thus the resulting
manifold is \(\mathbb R\times P_\ell\), with fixed Chern number.

The circle action is free, since \(a\ge d>0\) in the middle and the
source action is free, including at conformal infinity. The compact
middle is smooth and each outer end is an unchanged complete PE end.
The glued metric is therefore complete, with a smooth conformal
compactification whose two boundary metrics are fixed.

For \(\ell\ne0\), the family realizes lapse degeneration in the
quantized-curvature estimate of [the connector analysis](round10_connector.md).
The middle quotient has product metric \(dt^2+h\).
The surface \(\Sigma_0=\{t=0\}\times\Sigma\) is a stable minimal
separator, with zero second fundamental form and quotient normal Ricci
curvature. For \(A=\operatorname{Area}_h(\Sigma)\), its lapse is \(V=d\),
so

\[
\left(\int_{\Sigma_0}V^2\right)
\left(\int_{\Sigma_0}V^{-4}\right)=A^2d^{-2}\longrightarrow\infty,
\qquad
\epsilon\ge\frac{\pi^2\ell^2d^2}{A^2}.
\tag{14}
\]

The actual central error is \(2\pi^2\ell^2d^2/A^2\).
In the exact Jacobi identity, \(E(n,n)=0\) and
\(E(U,U)=d^2|F|_{\rm tens}^2/4\); thus the error difference cancels
the positive twist term exactly, as stability requires.
The topological flux stays nonzero while the lapse collapses.
This realizes the permitted escape, but does not prove optimality of
the global error rate (3).

The mechanism relies on a noncollapsed negatively curved quotient
surface while only the circle collapses. Then \(a^2|F|^2\to0\).
It does not extend by the same substitution to a full torus AH cusp,
where all flat directions collapse, or to an ACH Nil cusp, where base
collapse keeps the analogous twist contribution at order one.

Thus exact boundary connectedness cannot by itself yield a
dimension-only near-Einstein defect gap, even for fixed nontrivial
circle-bundle topology and fixed conformal infinities. This is not a
closed four-manifold construction, a torus-ended connector, or an
all-sign Einstein obstruction on a closed smooth manifold.

The exact source theorem is Li--Liu's. The present doubling calculation
is its application to the approximate connector question; no
first-occurrence claim is made. It belongs to the existing
connector/construction analysis, not a separate scientific mainline.

The [coordinate checker](round10_cusp_doubling_check.py) independently
derives the central Ricci tensor from Christoffel symbols in the local
model \(\theta=d\phi+\kappa e^z\,dw\) and
\(h=(dz^2+e^{2z}dw^2)/3\). All sixteen tensor components, the
orthonormal error spectrum, and the Chern/lapse identities pass.
It does not replace the source theorem or the covariant gluing proof.

# A global obstruction to charged torus Einstein connectors

21 September 2026.

## 1. Statement

The obstruction retains connection curvature. It does not assume
orthogonal transitivity, diagonal fibre metric, constant boundary shape,
zero charge, or nonnegative boundary Yamabe class.

**Theorem 1 (free-circle boundary connectedness).** Let
\(\overline M^{n+1}\), \(n\ge2\), be a compact connected smooth manifold
with nonempty boundary. Suppose its interior carries a smooth conformally
compact Einstein metric \(\operatorname{Ric}_{g_+}=-ng_+\). Suppose a
free isometric circle action extends smoothly and freely to
\(\overline M\). Write its principal bundle as
\[
S^1\longrightarrow\overline M\longrightarrow\overline N.
\tag{1.1}
\]
Then \(\partial\overline M\) is connected. The principal bundle need
not be trivial.

Smooth conformal compactness means that a defining function \(x\)
exists with \(x^2g_+\) smooth positive definite up to the boundary. No
sign condition is imposed on boundary scalar curvature.

**Corollary 1.1.** There is no complete Einstein metric
\(\operatorname{Ric}=-3g\) on \(\mathbb R\times T^3\) with two smooth
conformally compact AH ends and a free isometric \(T^2\) action extending
freely to both ends, with marked orbit space the compact annulus.

Indeed either primitive circle subgroup acts freely, including at both
ends. Theorem 1 contradicts the two boundary components. No charge or
bundle-triviality calculation is needed for this implication.

## 2. Circle reduction and an auxiliary static spacetime

Let \(K\) be the circle generator, \(V=|K|_{g_+}>0\), and \(h\) the
Riemannian quotient metric. The connection
\(\eta=V^{-2}g_+(K,\cdot)\) is globally defined on the total space;
its curvature is \(d\eta=\pi^*F\) for a two-form \(F\) on \(N\).
There need not be any global connection potential on \(N\). Locally,
\[
g_+=V^2(d\phi+\alpha)^2+h,\qquad F=d\alpha.
\tag{2.1}
\]
Write \(F^2=F_{ij}F^{ij}\), twice the usual squared two-form norm, and
\((FF)_{ij}=F_{ik}F_j{}^k\), with all contractions using \(h\).
The circle curvature formulas give
\[
\begin{split}
\operatorname{Ric}_{g_+}(X^H,Y^H)
 &=\operatorname{Ric}_h(X,Y)-V^{-1}\nabla^2V(X,Y)
     -\tfrac{V^2}{2}(FF)(X,Y),\\
\operatorname{Ric}_{g_+}(V^{-1}K,V^{-1}K)
 &=-V^{-1}\Delta_hV+\tfrac{V^2}{4}F^2.
\end{split}
\tag{2.2}
\]
For example, these follow by Koszul's formula from
\([X^H,Y^H]=[X,Y]^H-VF(X,Y)E\),
\([X^H,E]=-X(\log V)E\), \(E=V^{-1}K\), and
\[
\begin{split}
\nabla_{X^H}Y^H&=(\nabla^h_XY)^H-\tfrac V2F(X,Y)E,\\
\nabla_{X^H}E&=\tfrac V2(\iota_XF)^{\sharp,H},\\
\nabla_EX^H&=\tfrac V2(\iota_XF)^{\sharp,H}+X(\log V)E,\\
\nabla_EE&=-(\nabla\log V)^H.
\end{split}
\tag{2.3}
\]
Thus the Einstein equation implies the global quotient identities
\[
\operatorname{Ric}_h-V^{-1}\nabla^2V=-nh+\tfrac{V^2}{2}FF,
\qquad V^{-1}\Delta V=n+\tfrac{V^2}{4}F^2.
\tag{2.4}
\]

On the new product \(\mathbb R_t\times N\), define
\[
g_L=-V^2dt^2+h.
\tag{2.5}
\]
This is an auxiliary metric built from global quotient data, not an
isometric transformation of the original bundle. Removing the connection
from this new metric does **not** assume \(F=0\) in (2.1).
The static warped-product identities give, for \(E_0=V^{-1}\partial_t\),
\[
\begin{split}
\operatorname{Ric}_L(X,Y)&=\operatorname{Ric}_h(X,Y)-V^{-1}\nabla^2V(X,Y)
                       =-nh(X,Y)+\tfrac{V^2}{2}(FF)(X,Y),\\
\operatorname{Ric}_L(E_0,E_0)&=V^{-1}\Delta_hV
                       =n+\tfrac{V^2}{4}F^2,\\
\operatorname{Ric}_L(E_0,X)&=0.
\end{split}
\tag{2.6}
\]
For every null \(Z=aE_0+X\), with \(|X|_h^2=a^2\),
\[
\boxed{\operatorname{Ric}_L(Z,Z)
=V^2\left(\tfrac{a^2}{4}F^2+\tfrac12|\iota_XF|_h^2\right)\ge0.}
\tag{2.7}
\]
This proves null convergence and hence ANEC. The auxiliary metric need
not be Lorentzian Einstein when \(F\ne0\); only its null Ricci sign
is needed. Neither the mixed Riemannian Einstein equation nor a global
potential \(\alpha\) is required.

## 3. Compact optical geometry gives global causality

Average a defining function over the circle to make \(x\) invariant.
Since the action is free at the boundary,
\(\overline V=xV>0\) and \(\overline h=x^2h>0\) extend smoothly to the
compact quotient. Consequently
\[
k=V^{-2}h=\overline V^{-2}\overline h
\tag{3.1}
\]
is a smooth positive metric on \(\overline N\).

The smooth optical metric on \(\mathbb R\times\overline N\) is
\[
\widehat g_L=V^{-2}g_L=-dt^2+k.
\tag{3.2}
\]
Thus \(t\) is temporal. Orient the causal cone by \(\dot t>0\).
Every future causal tangent obeys
\[
\dot t\ge|\dot y|_k.
\tag{3.3}
\]
The completion is globally hyperbolic **as a spacetime with boundary**.
Temporal \(t\) gives strong causality. In bounded time slabs the spatial
parts of causal curves are uniformly Lipschitz when parameterized by
\(t\). Compactness of \(\overline N\) and the limit-curve argument give
closed causal relations in each slab. Thus causal diamonds are closed
subsets of compact sets \([t(p),t(q)]\times\overline N\). Alternatively,
an inextendible causal curve with finite upper or lower \(t\)-endpoint
would have a spatial limit by (3.3) and could be extended there.

The conformal factor \(\Omega=V^{-1}=x/\overline V\)
vanishes simply at the boundary. Each boundary component is timelike and
has the form \(\mathcal I_j=\mathbb R\times\partial_j\overline N\).
Its \(t=0\) cut is compact spacelike with induced metric
\(k|_{T\partial_j\overline N}\).

## 4. Boundary noncommunication concludes the proof

Galloway--Schleich--Witt--Woolgar, *The AdS/CFT Correspondence Conjecture
and Topological Censorship*, Theorem 2, forbids causal communication
between different timelike conformal boundary components of a globally
hyperbolic completion satisfying ANEC when one component has a compact
spacelike cut. The cut condition substitutes for genericity; no vacuum or
boundary Yamabe hypothesis appears. Definitions and the theorem are in
Section II of the [primary text](https://arxiv.org/pdf/hep-th/9912119).
The stated dimension range is \(n+1\ge3\).

If \(\partial\overline N\) had two components, connectedness gives a
smooth path \(y:[0,1]\to\overline N\) between them whose open segment
lies inside \(N\). Choose \(t(s)\) with
\[
\dot t>|\dot y|_k.
\tag{4.1}
\]
Then \((t(s),y(s))\) is future timelike and joins the two conformal
boundaries, contradicting the theorem by (2.7)--(3.3). Thus
\(\partial\overline N\) is connected. A circle bundle over a connected
base has connected total space, by local triviality and connectedness of
the fibre. Hence \(\partial\overline M\) is connected as well.
\(\square\)

## 5. Research consequence and scope

Corollary 1.1 closes the exact two-ended AH connector problem in the full
marked free-\(T^2\) class, including nonzero charge and nonconstant shape.
The obstruction uses both ends, not a local prohibition on throats. The
analytic charged Einstein germs and strictly stable local separators of
`round9_global.md` remain compatible: they cannot extend to both AH ends.

A free action on the entire compactification is substantive. This proof
does cover nontrivial circle bundles, but not collapsed circle orbits,
nonsymmetric Einstein metrics on the same topological cylinder, or
nonsmooth conformal infinity. No boundary-isometry extension theorem is
assumed or proved. For comparison, Chen's explicit circle-bundle PE
constructions collapse the circle/Hopf fibre to form disc bundles and
have connected conformal boundary; see Theorems 1.1, 1.4, 1.5 and Remark
1.3 in [the primary paper](https://arxiv.org/pdf/0908.1430). They do not
contradict this theorem.

This is not a uniform near-Einstein Ricci gap. Small two-sided Ricci errors
add indefinite terms to (2.7); their integrals along complete null curves
are not controlled by pointwise smallness alone, so ANEC need not hold.
Degenerating approximate connectors and unrestricted Yau26 remain open.

The dimension restriction cannot be removed: in dimension two,
\(g=dr^2+\cosh^2r\,d\phi^2\) on \(\mathbb R\times S^1\) has
\(\operatorname{Ric}=-g\), a free circle action, and two smooth AH ends.
Its auxiliary spacetime has dimension \(1+1\), outside the cited
boundary-noncommunication theorem.

No priority claim is made. The curvature algebra has an independent exact
coordinate check in `round9_signature_check.py`, including nonflat base
metric, variable fibre length, and multicomponent curvature. These check
the reduced curvature algebra; the global proof is Sections 3--4, not
the test count. The earlier connection-retaining Lorentzian construction
also works for trivial bundles, but the static auxiliary metric above
removes its needless triviality and fibre-shrinking restrictions.

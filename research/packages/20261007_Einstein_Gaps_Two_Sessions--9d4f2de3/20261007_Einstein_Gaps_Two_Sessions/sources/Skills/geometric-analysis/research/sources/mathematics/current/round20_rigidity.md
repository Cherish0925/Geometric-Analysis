# What an integral monopole gap can control in the period domain

22 September 2026. This note gives an all-metric period bound without
scalar-energy saturation, states the exact linear-algebra condition that turns it
into compact confinement, and tests that condition on actual exact
Einstein metrics. The compactness mechanism is classical finite-dimensional
geometry combined with classical monopole estimates. Round 4 improves its
radius but does not supply the missing directions. No general bound on the
rank of the actual monopole set is proved.

## 1. A projection bound valid away from scalar saturation

Let \(M\) be a closed connected oriented smooth four-manifold, \(b^+\ge2\),
and put \(T=2\chi+3\tau\). For a metric with

\[
 R_2=\int|\operatorname{Ric}|^2>0,
 \qquad
 e=4-\frac{(\int s)^2}{VR_2}
   =\frac{4P+L}{R_2},
 \quad
 P=\int|\operatorname{Ric}^{\circ}|^2,
 \quad L=\int(s-\bar s)^2,
 \tag{1}
\]

write \(H=H_g^+\subset H^2(M;\mathbb R)\) and \(p_H(a)=(a_H^+)^2\).
An actual monopole class is the real Chern class of a spin-c structure
solvable for every smooth metric, not merely an element of a formal
convex hull.

**Proposition 1 (classical radius and integral-gap radius).** If \(e<1\),
then \(T>0\), and every actual monopole class satisfies

\[
 p_H(a)\le U_{\rm cl}(e,T)
 :=\frac{3(4-e)}{8(1-e)}T.                         \tag{2}
\]

Fix \(C\ge0\), and let \(\varepsilon(C)\in(0,1/4]\) be an all-sign
constant from Round 4/5: if \(p_H(a)>0\) and \(a^2\ge-Cp_H(a)\), then

\[
 e+\left(\frac{T}{p_H(a)}-\frac23\right)_+
       \ge\varepsilon(C).                              \tag{3}
\]

For any collection \(\mathcal A\) of actual classes with

\[
 a^2\ge-CT\quad(a\in\mathcal A),\qquad
 e<\varepsilon(C),
\]

one has the simultaneous bound

\[
 \boxed{p_H(a)\le U(e,T,C)
 :=\frac{T}{\,2/3+\varepsilon(C)-e\,}
 \quad(a\in\mathcal A).}                              \tag{4}
\]

In particular the same bound with \(C=0\) holds for every actual special
class \(a^2\ge T\). These statements apply to every possible non-Ricci-flat
Einstein output, by setting \(e=0\); they are not tied to an input metric
or a construction ansatz. A nonzero actual class with positive square
also excludes Ricci-flat metrics by the scalar inequality.

**Proof.** Chern--Weil and \(\int s^2=4(R_2-P)\) give

\[
 4\pi^2T=2\|W^+\|_2^2+\frac{R_2}{6}-\frac{2P}{3}
       \ge\frac{R_2-4P}{6}
       \ge\frac{1-e}{6}R_2.                           \tag{5}
\]

Thus \(T>0\) and \(R_2\le24\pi^2T/(1-e)\). The classical projected
monopole estimate is

\[
 p_H(a)\le\frac32T+\frac{3P}{16\pi^2}.                \tag{6}
\]

It follows directly from [LeBrun, *Ricci Curvature, Minimal Volumes, and
Seiberg--Witten Theory*, Proposition 3.1](https://arxiv.org/pdf/math/0003068)
and Chern--Weil. Substituting \(P\le eR_2/4\) proves (2).
For (4), if \(p_H(a)<T\), the claim follows because its denominator is
positive and less than one. Otherwise \(a^2\ge-CT\ge-Cp_H(a)\), so (3)
applies; its positive part must be positive because \(e<\varepsilon(C)\).
Rearrangement proves (4). Zero projection causes no division. \(\square\)

This is not a new curvature estimate: (4) is a reformulation of the
completed integral gap, and (2) is entirely classical. It records exactly
what can be used without the additional scalar error

\[
 B_a=\int s^2-32\pi^2a^2
\]

being small. In particular no Round 18 phase-correlation or spectral-cluster
conclusion has been used.

## 2. The extra hypothesis for confinement of the whole period plane

Let \(Q\) be the intersection form, of signature \((b^+,b^-)\), and let
\(\mathcal D\) be its space of maximal positive subspaces. For finite nonempty
\(\mathcal A=\{a_1,\ldots,a_m\}\) put

\[
 W=\operatorname{span}_{\mathbb R}\mathcal A,
 \qquad
 K_U=\{H\in\mathcal D:p_H(a_i)\le U\text{ for all }i\}.
 \tag{7}
\]

**Theorem 2 (the exact properness criterion).** The height
\(H\mapsto\max_i p_H(a_i)\) on \(\mathcal D\) is proper if and only if
\(W\) contains a maximal positive subspace or a maximal negative subspace
for \(Q\). Equivalently, all \(K_U\) are compact precisely under that
condition. If the condition fails, every nonempty \(K_U\) is noncompact.
Under this criterion, (2), or the stronger (4) under its square-cost hypothesis,
confines all the corresponding metric period planes on this fixed marked
manifold to an explicitly bounded compact subset of \(\mathcal D\).

Here is an explicit bound when \(W\) contains a maximal positive subspace
\(P_0\). Choose a \(Q\)-orthonormal basis

\[
 u_j=\sum_i c_{ji}a_i\quad(1\le j\le b^+),\qquad
 D=U\sum_j\left(\sum_i|c_{ji}|\right)^2.                 \tag{8}
\]

Every \(H\in K_U\) is the graph of \(X:P_0\to P_0^{\perp_Q}\), and

\[
 \boxed{\quad
 \|X\|_{\rm op}^2\le1-\frac1{D-b^++1}.
 \quad}                                                   \tag{9}
\]

If \(D<b^+\), \(K_U\) is empty. All norms in (9) come from \(Q\) on
\(P_0\) and \(-Q\) on its orthogonal complement.

**Proof.** Projection is linear, so the triangle inequality on \(H\)
gives \(p_H(u_j)\le U(\sum_i|c_{ji}|)^2\). In the graph coordinates
with \(Q=\operatorname{diag}(I,-I)\), solve the projection equation to get

\[
 p_H(u)=u^{\mathsf T}(I-X^{\mathsf T}X)^{-1}u,
 \qquad
 \operatorname{tr}(I-X^{\mathsf T}X)^{-1}\le D.           \tag{10}
\]

Each eigenvalue on the left is at least one. Its largest is therefore
at most \(D-b^++1\), proving (9). Thus \(X\) stays a fixed distance
from the boundary \(X^{\mathsf T}X=I\). The constraints defining \(K_U\)
are closed inside this bounded coordinate set, so \(K_U\) is compact.

For the negative version apply the same argument to \(H^{\perp_Q}\)
and \(-Q\), using

\[
 |a_{i,H}^-|^2=p_H(a_i)-a_i^2\le U-a_i^2.               \tag{11}
\]

If some right side is negative, \(K_U\) is empty. Otherwise these finitely
many bounds control the negative projections of a basis for a maximal
negative subspace contained in \(W\).

For necessity, first suppose \(W\) is nondegenerate and contains neither
kind of maximal definite subspace. Then \(W^{\perp_Q}\) has both signs.
Its orthogonal group has noncompact one-parameter boosts fixing every
\(a_i\). Starting from any \(H_0\in K_U\), their orbit stays in \(K_U\)
and escapes compact subsets of \(\mathcal D\): the orthogonal group's
action on the positive-plane domain has compact stabilizer and is proper.

If \(W\) is degenerate, choose
\(0\ne l\in W\cap W^{\perp_Q}\). Let \(J_0\) be the involution acting
as \(+1\) on \(H_0\) and \(-1\) on \(H_0^{\perp_Q}\), and put

\[
 d=Q(l,J_0l)>0,\qquad m=J_0l/d,\qquad
 Z=\operatorname{span}(l,m)^{\perp_Q}.
 \tag{11a}
\]

Both \(l,m\) are null, \(Q(l,m)=1\), and \(Z\) is \(J_0\)-invariant.
The decomposition \(\mathbb Rl\oplus\mathbb Rm\oplus Z\) is orthogonal
for the positive Hodge inner product \(Q(\,\cdot,J_0\,\cdot)\).
Since \(Q(l,w)=0\) for all \(w\in W\), every such \(w\) is \(cl+z\).
Let \(A_t\in O(Q)\) scale \(l\) by \(e^{-t}\), \(m\) by \(e^t\), and
fix \(Z\). For \(H_t=A_t^{-1}H_0\),

\[
 \|cl+z\|_{H_t}^2=e^{-2t}c^2d+\|z\|_{H_0}^2,
 \qquad
 \|m\|_{H_t}^2=e^{2t}/d.                              \tag{11b}
\]

Because \(2p_H(w)=\|w\|_H^2+Q(w,w)\), all the heights of the \(a_i\)
decrease while the norm of the fixed vector \(m\) diverges. Thus
\(H_t\in K_U\) and escapes compact subsets. Finally, a degenerate \(W\)
cannot contain either kind of maximal definite subspace: its nonzero
radical would lie in that subspace's definite orthogonal complement.
This completes both directions. \(\square\)

The compactness theorem itself also follows from the classical radius
(2). The integral gap supplies a strictly smaller allowed radius at
\(e=0\), not a new compactness mechanism. Neither statement is geometric
compactness of Einstein metrics.

## 3. Exact Einstein calibration: degeneration survives all special classes

The following test is genuine degeneration, not just pulling back one
metric by unbounded mapping classes.

**Proposition 3.** Fix \(M=\Sigma_g\times\Sigma_h\), \(g,h\ge2\), with
the product orientation, and let \(a=c_1(M)\). There is a family of
product hyperbolic metrics \(G_\ell\), \(\ell\downarrow0\), for which

\[
 \operatorname{Ric}_{G_\ell}=-G_\ell,\qquad
 e=0,\qquad a^2=T=p_{H_{G_\ell}}(a)>0,\qquad
 \int s^2=32\pi^2T.                                   \tag{12}
\]

The full set of real special monopole classes of \(M\) is exactly
\(\{a,-a\}\). Nevertheless its period planes escape every compact
subset even of the quotient \(O(Q;\mathbb Z)\backslash\mathcal D\).
In particular quotienting by orientation-preserving diffeomorphisms
does not repair this failure.

**Proof of the class statement.** The canonical classes are actual by
the symplectic Seiberg--Witten theorem. The product has

\[
 V=16\pi^2(g-1)(h-1),\quad T=8(g-1)(h-1),
 \quad b^+=b^-=1+2gh.
\]

For any real special monopole \(c\), the scalar inequality gives

\[
 T\le c^2\le p_{H_G}(c)\le\frac{\int s^2}{32\pi^2}=T.
 \tag{13}
\]

All are equalities. In particular \(c^-=0\), and equality in the
scalar estimate gives a parallel nonzero self-dual form representing
\(c\). This is the equality proof of [LeBrun, *Four-Manifolds, Curvature
Bounds, and Convex Geometry*, Proposition 3.2](https://arxiv.org/pdf/math/0611450).
The product's restricted holonomy is \(SO(2)\times SO(2)\); its parallel
self-dual two-forms form the single line spanned by the sum of the two
area forms. Thus \(c=ta\), and \(c^2=a^2>0\) gives \(t=\pm1\).
This argument handles all actual special classes, not merely those with
nonzero ordinary invariants. It makes no assertion about nonspecial
ordinary monopoles.

**Proof of quotient-period escape.** Choose a fixed nonseparating curve
\(\gamma\subset\Sigma_g\). Hyperbolic pants gluing with its boundary
length set to \(\ell\) gives hyperbolic metrics \(k_\ell\) in which its
geodesic has length \(\ell\). Keep the second metric \(k_h\) fixed and
set \(G_\ell=k_\ell\oplus k_h\). The collar theorem supplies, for small
\(\ell\), an embedded fixed-width cylinder around \(\gamma\), with

\[
 k_\ell=dr^2+\ell^2\cosh^2r\,d\theta^2,
 \quad -1<r<1,\quad\theta\in\mathbb R/\mathbb Z.
 \tag{14}
\]

The classical collar lemma in equivalent conformal coordinates is recalled
in [Rupflin--Topping, *Horizontal curves of hyperbolic metrics*, Lemma
A.1](https://arxiv.org/pdf/1605.06691).

Fix \(f\in C_c^\infty(-1,1)\) with \(\int f\,dr=1\). The form
\(\eta_\ell=f(r)dr\), extended by zero, is smooth and closed. It represents
the fixed primitive integral class \(u=\operatorname{PD}[\gamma]\);
its integral on a transverse loop is its algebraic intersection with
\(\gamma\). Its energy is

\[
 \|\eta_\ell\|_2^2
  =\ell\int_{-1}^1f(r)^2\cosh r\,dr=C_f\ell.            \tag{15}
\]

The harmonic representative \(\alpha_\ell\) of \(u\) has no larger
energy. Choose a fixed nonzero primitive integral class
\(v\in H^1(\Sigma_h;\mathbb Z)\) and its harmonic representative
\(\beta\). The product harmonic form \(\alpha_\ell\wedge\beta\)
represents the fixed primitive integral two-class \(x=u\otimes v\ne0\).
Product norms give

\[
 \|x\|_{H_{G_\ell}}^2
 =\|\alpha_\ell\|_2^2\|\beta\|_2^2
 \le C_f\|\beta\|_2^2\ell\longrightarrow0,              \tag{16}
\]

where \(\|x\|_H^2=Q(x_H^+,x_H^+)-Q(x_H^-,x_H^-)\) is the
positive-definite Hodge norm on \(H^2\).

For the fixed integral lattice \(\Lambda=H^2(M;\mathbb Z)/\mathrm{tors}\),
the function

\[
 \sigma(H)=\min_{0\ne z\in\Lambda}\|z\|_H
 \tag{17}
\]

is positive and continuous on \(\mathcal D\), and invariant under
\(O(Q;\mathbb Z)\). Positivity follows from lattice discreteness;
continuity follows because on a neighborhood of any positive-definite
norm only finitely many lattice vectors can realize its minimum.
It therefore descends to a positive continuous function on the quotient,
bounded below on every compact subset. Equation (16) implies
\(\sigma(H_{G_\ell})\to0\), proving the claimed escape. \(\square\)

All local curvature tensors in this example are those of
\(\mathbb H^2\times\mathbb H^2\); neither curvature blow-up nor a change
of smooth topology is used. The injectivity radius collapses. The class
\(x\) detecting escape is not asserted to be a monopole. It lies in the
indefinite mixed Kunneth summand, invisible to the special-class line.

For the forbidden Round 4 Weyl orbit
\(\mathcal O_0=\operatorname{Orb}\operatorname{diag}(-1/6,1/12,1/12)\),
these exact Einstein metrics give, pointwise,

\[
 W^+=\operatorname{diag}(-2/3,1/3,1/3),\quad
 \operatorname{dist}(W^+,\mathcal O_0)^2=\frac38,
 \quad q=-s+\sqrt6|W^+|=6.                              \tag{18}
\]

Thus \(\Delta_+=\int q^2-72\pi^2p_H(a)=0\) and the negative
Chern-square cost vanishes, yet the calibration defect in Round 4 is
\(3/8\). Its Weyl-orbit term cannot be discarded in favor of relative
Einstein defect. The ratio \(T/p_H(a)=1\) keeps this example outside the
forbidden (2/3) band, exactly as it must.

## 4. What this settles, and what it does not

Equations (2)--(4) are honest constraints on all output period planes
without scalar saturation. Theorem 2 gives the exact algebraic
criterion for properness of these simultaneous class-height constraints.
Proposition 3 shows that even the
entire actual special-class set, zero Ricci defect, zero negative-square
cost, and exact scalar saturation need not satisfy that condition; the
failure persists after the natural integral marking quotient.

There is no contradiction with Round 18: on this example the monopole
span is one-dimensional and its nontrivial phase covariance has rank zero.
Round 18 controls fields arising from the specified actual classes, not
the full harmonic self-dual space.

For completeness, the elementary packing bound for any finite actual
set with \(a^2\ge-CT\) and (4) is

\[
 \#\mathcal A\le
 \left(1+\frac{2\sqrt{2U+CT}}{\sigma(H)}\right)^{b_2(M)}.
 \tag{19}
\]

Indeed \(\|a\|_H^2=2p_H(a)-a^2\le2U+CT\), and disjoint Hodge balls
of radius \(\sigma(H)/2\) about these distinct real lattice classes fit
inside the ball of radius \(\sqrt{2U+CT}+\sigma(H)/2\). This counts
real classes, not spin-c structures distinguished only by torsion.
The dependence on the lattice systole and dimension is explicit. Neither
the preceding proof nor the exact calibration yields a bound on the
number of linearly independent actual classes solely from \(e\) and \(C\).
The example disproves an unrestricted period-compactness inference; it
does not disprove an as-yet-unproved gauge-theoretic rank theorem.

The contribution here is a completed consequence and a decisive test of
the proposed extension, not a new general Einstein obstruction. The
classical ingredients and the inherited gap have been kept separate.
The accompanying checker verifies (2), the graph projection identities,
and the exact Einstein/Weyl calibration. The collar, lattice compactness,
and monopole existence arguments are analytic proofs above, not claims
certified by finite computation.

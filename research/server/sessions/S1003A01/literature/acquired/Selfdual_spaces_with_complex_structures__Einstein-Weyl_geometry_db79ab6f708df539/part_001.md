---
retention_scope: session
part: 1
total_parts: 2
---

[Part 1/2 of: Selfdual spaces with complex structures, Einstein-Weyl geometry and geodesics]

---
source_file: Selfdual_spaces_with_complex_structures__Einstein-Weyl_geometry_and_geodesics_70e3cd5ec76b.pdf
converter: mathpix
format: mmd
---

\section*{Annales de l'institut Fourier}

\author{
David M J. Calderbank Henrik Pedersen
}

Selfdual spaces with complex structures, EinsteinWeyl geometry and geodesics

Annales de l'institut Fourier, tome 50, n° 3 (2000), p. 921-963
<http://www.numdam.org/item?id=AIF_2000__50_3_921_0>
© Annales de l'institut Fourier, 2000, tous droits réservés.
L'accès aux archives de la revue « Annales de l'institut Fourier » (http://annalif.ujf-grenoble.fr/) implique l'accord avec les conditions générales d'utilisation (http://www.numdam.org/conditions). Toute utilisation commerciale ou impression systématique est constitutive d'une infraction pénale. Toute copie ou impression de ce fichier doit contenir la présente mention de copyright.

\title{
SELFDUAL SPACES WITH COMPLEX STRUCTURES, EINSTEIN-WEYL GEOMETRY AND GEODESICS
}

\author{
by D.M.J. CALDERBANK and H. PEDERSEN
}

\section*{1. Introduction.}

Selfdual conformal 4-manifolds play a central role in low dimensional differential geometry. The selfduality equation is integrable, in the sense that there is a twistor construction for solutions, and so one can hope to find many explicit examples [2], [23]. One approach is to look for examples with symmetry. Since the selfduality equation is the complete integrability condition for the local existence of orthogonal (and antiselfdual) complex structures, it is also natural to look for solutions equipped with such complex structures. Our aim herein is to study the geometry of this situation in detail and present a framework unifying the theories of hypercomplex structures and scalar-flat Kähler metrics with symmetry [7], [12], [19]. Within this framework, there are explicit examples of hyperKähler, selfdual Einstein, hypercomplex and scalar-flat Kähler metrics parameterised by arbitrary functions.

The key tool in our study is the Jones and Tod construction [16], which shows that the reduction of the selfduality equation by a conformal vector field is given by the Einstein-Weyl equation together with the linear equation for an abelian monopole. This correspondence between a selfdual space $M$ with symmetry and an Einstein-Weyl space $B$ with a monopole is remarkable for three reasons:
(i) It provides a geometric interpretation of the symmetry reduced equation for an arbitrary conformal vector field.

\footnotetext{
Keywords : Sefdual manifolds - Hermitian surfaces - Conformal symmetry - Einstein-Weyl 3-manifolds - Geodesic congruences - Abelian monopoles - Twistor theory.
Math. classification : 53A30-32L25 - 53B35-57M50.
}
(ii) It is a constructive method for building selfdual spaces out of solutions to a linear equation on an Einstein-Weyl space.
(iii) It can be used in the other direction to construct Einstein-Weyl spaces from selfdual spaces with symmetry.

We add to this correspondence by proving that invariant antiselfdual complex structures on $M$ correspond to shear-free geodesic congruences on $B$, i.e., foliations of $B$ by oriented geodesics, such that the transverse conformal structure is invariant along the leaves. This generalises Tod's observation [29] that the Einstein-Weyl spaces arising from scalar-flat Kähler metrics with Killing fields [19] admit a shear-free geodesic congruence which is also twist-free (i.e., surface-orthogonal).

In order to explain how the scalar-flat Kähler story and the analogous story for hypercomplex structures [7], [12] fit into our more general narrative, we begin, in Section 2, by reviewing, in a novel way, the construction of a canonical "Kähler-Weyl connection" on any conformal Hermitian surface [9], [32]. We give a representation theoretic proof of the formula for the antiselfdual Weyl tensor on such a surface [1] and discuss its geometric and twistorial interpretation when the antiselfdual Weyl tensor vanishes. We use twistor theory throughout the paper to explain and motivate the geometric constructions, although we find it easier to make these constructions more general, explicit and precise by direct geometric arguments.

Having described the four dimensional context, we lay the three dimensional foundations for our study in Section 3. We begin with some elementary facts about congruences, and then go on to show that the Einstein-Weyl equation is the complete integrability condition for the existence of shear-free geodesic congruences in a three dimensional Weyl space. As in Section 2, we discuss the twistorial interpretation, this time in terms of the associated "minitwistor space" [14], and explain the minitwistor version of the Kerr theorem, which has only been discussed informally in the existing literature (and usually only in the flat case). We also show that at any point where the Einstein-Weyl condition does not hold, there are at most two possible directions for a shear-free geodesic congruence. The main result of our work in this section, however, is a reformulation of the Einstein-Weyl equation in the presence of a shear-free geodesic congruence. More precisely, we show in Theorem 3.8 that the Einstein-Weyl equation is equivalent to the fact that the divergence and twist of this congruence are both monopoles of a special kind. These "special" monopoles play a crucial
role in the sequel.
We end Section 3 by giving examples. We first explain how the Einstein-Weyl spaces arising as quotients of scalar-flat Kähler metrics and hypercomplex structures fit into our theory: they are the cases of vanishing twist and divergence respectively. In these cases it is known that the remaining nonzero special monopole (i.e., the divergence and twist respectively) may be used to construct a hyperKähler metric [3], [7], [12], motivating some of our later results. We also give some new examples: indeed, in Theorem 3.10, we classify explicitly the Einstein-Weyl spaces admitting a geodesic congruence generated by a conformal vector field preserving the Weyl connection. We call such spaces Einstein-Weyl with a geodesic symmetry. They are parameterised by an arbitrary holomorphic function of one variable.

The following section contains the central results of this paper, in which the four and three dimensional geometries are related. We begin by giving a new differential geometric proof of the Jones and Tod correspondence [16] between oriented conformal structures and Weyl structures, which reduces the selfduality condition to the Einstein-Weyl condition (see 4.1). Although other direct proofs can be found in the literature [12], [17], [19], they either only cover special cases, or are not sufficiently explicit for our purposes. Our next result, Theorem 4.2, like the Jones and Tod construction, is motivated by twistor theory. Loosely stated, it is as follows.

Theorem. - Suppose $M$ is an oriented conformal 4-manifold with a conformal vector field, and $B$ is the corresponding Weyl space. Then invariant antiselfdual complex structures on $M$ correspond to shear-free geodesic congruences on $B$.

In fact we show explicitly how the Kähler-Weyl connection may be constructed from the divergence and twist of the congruence. This allows us to characterise the hypercomplex and scalar-flat Kähler cases of our correspondence, reobtaining the basic constructions of [3], [7], [12], [19], as well as treating quotients of hypercomplex, scalar-flat Kähler and hyperKähler manifolds by more general holomorphic conformal vector fields. As a consequence, we show in Theorem 4.3 that every Einstein-Weyl space is locally the quotient of some scalar-flat Kähler metric and also of some hypercomplex structure, and that it is a local quotient of a hyperKähler metric (by a holomorphic conformal vector field) if and
only if it admits a shear-free geodesic congruence with linearly dependent divergence and twist.

We clarify the scope of these results in Section 5 where we show that our constructions can be applied to all selfdual Einstein metrics with a conformal vector field. Here, we make use of the fact that a selfdual Einstein metric with a Killing field is conformal to a scalar-flat Kähler metric [31].

The last four sections are concerned exclusively with examples. In Section 6 we show how our methods provide some insight into the construction of Einstein-Weyl structures from $\mathbb{R}^{4}$ [26]. As a consequence, we observe that there is a one parameter family of Einstein-Weyl structures on $S^{3}$ admitting shear-free twist-free geodesic congruences. This family is complementary to the more familiar Berger spheres, which admit shear-free divergence-free geodesic congruences [7], [12].

In Section 7, we generalise this by replacing $\mathbb{R}^{4}$ with a Gibbons-Hawking hyperKähler metric [13] constructed from a harmonic function on $\mathbb{R}^{3}$. If the corresponding monopole is invariant under a homothetic vector field on $\mathbb{R}^{3}$, then the hyperKähler metric has an extra symmetry, and hence another quotient Einstein-Weyl space. We first treat the case of axial symmetry, introduced by Ward [33], and then turn to more general symmetries. The Gibbons-Hawking metrics constructed from monopoles invariant under a general Killing field give new implicit solutions of the Toda field equation. On the other hand, from the monopoles invariant under dilation, we reobtain the Einstein-Weyl spaces with geodesic symmetry.

In Section 8 we look at the constant curvature metrics on $\mathcal{H}^{3}, \mathbb{R}^{3}$ and $S^{3}$ from the point of view of congruences and use this prism to explain properties of the selfdual Einstein metrics fibering over them. Then in the final section, we consider once more the Einstein-Weyl spaces constructed from harmonic functions on $\mathbb{R}^{3}$, and use them to construct torus symmetric selfdual conformal structures. These include those of Joyce [17], some of which live on $k \mathbb{C} P^{2}$, and also an explicit family of hypercomplex structures depending on two holomorphic functions of one variable.

This paper is primarily concerned with the richness of the local geometry of selfdual spaces with symmetry, and we have not studied completeness or compactness questions in any detail. Indeed, the local nature of the Jones and Tod construction makes it technically difficult to tackle such issues from this point of view, and doing so would have added considerably to the length of this paper. Nevertheless, there remain interesting problems which we hope to address in the future.

Acknowledgements. - Thanks to Paul Gauduchon, Michael Singer and Paul Tod for helpful discussions. The diagrams were produced using Xfig and Mathematica.

\section*{2. Conformal structures and Kähler-Weyl geometry.}

Associated to an orthogonal complex structure $J$ on a conformal manifold is a distinguished torsion-free connection $D$. The conformal structure is preserved by this connection and, in four dimensions, so is $J$. Such a connection is called a Kähler-Weyl connection [5]: if it is the Levi-Civita connection of a compatible Riemannian metric, then this metric is Kähler. In this section, we review this construction, which goes back to Lee and Vaisman (see [9], [21], [32]).

It is convenient in conformal geometry to make use of the density bundles $L^{w}$ (for $w \in \mathbb{R}$ ). On an $n$-manifold $M, L^{w}$ is the oriented real line bundle associated to the frame bundle by the representation $A \mapsto|\operatorname{det} A|^{w / n}$ of $\operatorname{GL}(n)$. The fibre $L_{x}^{w}$ may be constructed canonically as the space of maps $\rho:\left(\Lambda^{n} T_{x} M\right) \backslash 0 \rightarrow \mathbb{R}$ such that $\rho(\lambda \omega)=|\lambda|^{-w / n} \rho(\omega)$ for all $\lambda \in \mathbb{R}^{\times}$and $\omega \in\left(\Lambda^{n} T_{x} M\right) \backslash 0$.

A conformal structure $\boldsymbol{c}$ on $M$ is a positive definite symmetric bilinear form on $T M$ with values in $L^{2}$, or equivalently a metric on the bundle $L^{-1} T M$. (When tensoring with a density line bundle, we generally omit the tensor product sign.)

The line bundles $L^{w}$ are trivialisable and a nonvanishing (usually positive) section of $L^{1}$ (or $L^{w}$ for $w \neq 0$ ) will be called a length scale or gauge (of weight $w$ ). We also say that tensors in $L^{w} \otimes(T M)^{j} \otimes\left(T^{*} M\right)^{k}$ have weight $w+j-k$. If $\mu$ is a positive section of $L^{1}$, then $\mu^{-2} \boldsymbol{c}$ is a Riemannian metric on $M$, which will be called compatible. A conformal structure may equally be defined by the associated "conformal class" of compatible Riemannian metrics.

A Weyl derivative is a covariant derivative $D$ on $L^{1}$. It induces covariant derivatives on $L^{w}$ for all $w$. The curvature of $D$ is a real 2-form $F^{D}$ which will be called the Faraday curvature or Faraday 2-form. If $F^{D}=0$ then $D$ is said to be closed. It follows that there are local length scales $\mu$ with $D \mu=0$. If such a length scale exists globally then $D$ is said to be exact. Conversely, a length scale $\mu$ induces an exact Weyl derivative $D^{\mu}$ such that $D^{\mu} \mu=0$. Consequently, we sometimes refer to an exact Weyl derivative as
a gauge. The space of Weyl derivatives on $M$ is an affine space modelled on the space of 1-forms.

Any connection on $T M$ induces a Weyl derivative on $L^{1}$. Conversely, on a conformal manifold, the Koszul formula shows that any Weyl derivative determines uniquely a torsion-free connection $D$ on $T M$ with $D \boldsymbol{c}=0$ (see [5]). Such connections are called Weyl connections. Linearising the Koszul formula with respect to $D$ shows that $(D+\gamma)_{X} Y=$ $D_{X} Y+\gamma(X) Y+\gamma(Y) X-\langle X, Y\rangle \gamma$, where $\langle.,$.$\rangle denotes the conformal$ structure, and $X, Y$ are vector fields. Notice that here, and elsewhere, we make free use of the sharp isomorphism $\sharp: T^{*} M \rightarrow L^{-2} T M$. We sometimes write $\gamma \Delta X(Y)=\iota_{Y}(\gamma \wedge X)$ for the last two terms.
2.1. Definition. - A Kähler-Weyl structure on a conformal manifold $M$ is given by a Weyl derivative $D$ and an orthogonal complex structure $J$ such that $D J=0$.

Suppose now that $M$ is a conformal $n$-manifold $(n=2 m>2)$ and that $J$ is an orthogonal complex structure. Then $\Omega_{J}:=\langle J .,$.$\rangle is a section$ of $L^{2} \Lambda^{2} T^{*} M$, called the conformal Kähler form. It is a nondegenerate weightless 2-form. (In general, we identify bilinear forms and endomorphism by $\Phi(X, Y)=\langle\Phi(X), Y\rangle$.)
2.2. Proposition (cf. [21]). - Suppose that $\Omega$ is a nondegenerate weightless 2-form. Then there is a unique Weyl derivative $D$ such that $d^{D} \Omega$ is trace-free with respect to $\Omega$, in the sense that $\sum d^{D} \Omega\left(e_{i}, e_{i}^{\prime},.\right)=0$, where $e_{i}, e_{i}^{\prime}$ are frames for $L^{-1} T M$ with $\Omega\left(e_{i}, e_{j}^{\prime}\right)=\delta_{i j}$.

Proof. - Pick any Weyl derivative $D^{0}$ and set $D=D^{0}+\gamma$ for some 1-form $\gamma$. Then $d^{D} \Omega=d^{D^{0}} \Omega+2 \gamma \wedge \Omega$ and so the traces differ by
$$\begin{aligned}
2(\gamma \wedge \Omega)\left(e_{i}, e_{i}^{\prime}, .\right) & =2 \gamma\left(e_{i}\right) \Omega\left(e_{i}^{\prime}, .\right)+2 \gamma\left(e_{i}^{\prime}\right) \Omega\left(., e_{i}\right)+2 \gamma \Omega\left(e_{i}, e_{i}^{\prime}\right) \\
& =2(n-2) \gamma .
\end{aligned}$$
Since $n>2$ it follows that there is a unique $\gamma$ such that $d^{D} \Omega$ is trace-free. □
2.3. Proposition. - Suppose that $J$ is an orthogonal complex structure on a conformal manifold $M$ and that $d^{D} \Omega_{J}=0$. Then $D$ defines a Kähler-Weyl structure on $M$, i.e., $D J=0$.

Proof. - For any vector field $X, D_{X} J$ anticommutes with $J$ (since $J^{2}=-\mathrm{id}$ ) and is skew (since $J$ is skew, and $D$ is conformal).

Hence $\left\langle\left(D_{J X} J-J D_{X} J\right) Y, Z\right\rangle$, which is symmetric in $X, Y$ because $J$ is integrable and $D$ is torsion-free, is also skew in $Y, Z$. It must therefore vanish for all $X, Y, Z$. If we now impose $d^{D} \Omega_{J}=0$ we obtain:
$$\begin{aligned}
0= & d^{D} \Omega(X, Y, Z)-d^{D} \Omega(X, J Y, J Z) \\
= & \left\langle\left(D_{X} J\right) Y, Z\right\rangle+\left\langle\left(D_{Y} J\right) Z, X\right\rangle+\left\langle\left(D_{Z} J\right) X, Y\right\rangle \\
& -\left\langle\left(D_{X} J\right) J Y, J Z\right\rangle-\left\langle\left(J D_{Y} J\right) J Z, X\right\rangle-\left\langle\left(J D_{Z} J\right) X, J Y\right\rangle \\
= & 2\left\langle\left(D_{X} J\right) Y, Z\right\rangle .
\end{aligned}$$
Hence $D J=0$. \(\square\)

Now if $n=4$ and $D$ is the unique Weyl derivative such that $d^{D} \Omega_{J}$ is trace-free, then in fact $d^{D} \Omega_{J}=0$ since wedge product with $\Omega_{J}$ is an isomorphism from $T^{*} M$ to $L^{2} \Lambda^{3} T^{*} M$. Hence, by Proposition 2.3, $D J=0$. To summarise:
2.4. Theorem (cf. [32]). - Any Hermitian conformal structure on any complex surface $M$ induces a unique Kähler-Weyl structure on $M$. The Weyl derivative is exact if and only if the conformal Hermitian structure admits a compatible Kähler metric.

On an oriented conformal 4-manifold, orthogonal complex structures are either selfdual or antiselfdual, in the sense that the conformal Kähler form is either a selfdual or an antiselfdual weightless 2-form. In this paper we shall be concerned primarily with antiselfdual complex structures on selfdual conformal manifolds, i.e., conformal manifolds $M$ with $W^{-}=0$, where $W^{-}$is the antiselfdual part of the Weyl tensor. In this case, as is well known (see [2]), there is a complex 3-manifold $Z$ fibering over $M$, called the twistor space of $M$. The fibre $Z_{x}$ given by the 2-sphere of orthogonal antiselfdual complex structures on $T_{x} M$, and the antipodal map $J \mapsto-J$ is a real structure on $Z$. The fibres are called the (real) twistor lines of $Z$ and are holomorphic rational curves in $Z$. The canonical bundle $K_{Z}$ of $Z$ is easily seen to be of degree -4 on each twistor line. As shown in [10], [25], any Weyl derivative on $M$ whose Faraday 2-form is selfdual induces a holomorphic structure on $L_{\mathbb{C}}^{1}$, the pullback of $L^{1} \otimes \mathbb{C}$, and (up to reality conditions) this process is invertible; this is the Ward correspondence for line bundles, or the Penrose correspondence for selfdual Maxwell fields.

The Kähler-Weyl connection arising in Theorem 2.4 can be given a twistor space interpretation. Any antiselfdual complex structure $J$ defines divisors $\mathcal{D}, \overline{\mathcal{D}}$ in $Z$, namely the sections of $Z$ given by $J,-J$. Since
the divisor $\mathcal{D}+\overline{\mathcal{D}}$ intersects each twistor line twice, the holomorphic line bundle $[\mathcal{D}+\overline{\mathcal{D}}] K_{Z}^{1 / 2}$ is trivial on each twistor line: more precisely, by viewing $J_{x}$ as a constant vector field on $L^{2} \Lambda_{-}^{2} T_{x}^{*} M$, its orthogonal projection canonically defines a vertical vector field on $Z$ holomorphic on each fibre and vanishing along $\mathcal{D}+\overline{\mathcal{D}}$. Therefore $[\mathcal{D}+\overline{\mathcal{D}}]$ is a holomorphic structure on the vertical tangent bundle of $Z$. In fact the vertical bundle of $Z$ is $L_{\mathbb{C}}^{-1} K_{Z}^{-1 / 2}$ and so $J$ determines a holomorphic structure on $L_{\mathbb{C}}^{-1}$, which, since $[\mathcal{D}+\overline{\mathcal{D}}]$ is real, gives a Weyl derivative on $M$ with selfdual Faraday curvature [11].

Similarly, by projecting each twistor line stereographically onto the orthogonal complement of $J$ in $L^{2} \Lambda_{-}^{2} T^{*} M$, which we denote $L^{2} K_{J}$, we see that the pullback of $L^{2} K_{J}$ to $Z$ has a section $s$ meromorphic on each fibre with a zero at $J$ and a pole at $-J$. Therefore the divisor $\mathcal{D}-\overline{\mathcal{D}}$ defines a holomorphic structure on this pullback bundle and hence a covariant derivative with (imaginary) selfdual curvature on $L^{2} K_{J}$. This curvature may be identified with the Ricci form, since if it vanishes, $[\mathcal{D}-\overline{\mathcal{D}}]$ is trivial, and so $s$, viewed as a meromorphic function on $Z$, defines a fibration of $Z$ over $\mathbb{C} P^{1}$; that is, $M$ is hypercomplex.

The selfduality of the Faraday and Ricci forms may be deduced directly from the selfduality of the Weyl tensor. To see this, we need a few basic facts from Weyl and Kähler-Weyl geometry.

First of all, let $D$ be a Weyl derivative on a conformal $n$-manifold and let $R^{D, w}$ denote the curvature of $D$ on $L^{w-1} T M$. Then it is well known that
$$R_{X, Y}^{D, w}=W_{X, Y}+w F^{D}(X, Y) \operatorname{id}-r^{D}(X) \Delta Y+r^{D}(Y) \Delta X .$$
Here $W$ is the Weyl tensor and $r^{D}$ is the normalised Ricci tensor, which decomposes under the orthogonal group as
$$r^{D}=r_{0}^{D}+\frac{1}{2 n(n-1)} \operatorname{scal}{ }^{D} \text { id }-\frac{1}{2} F^{D},$$
where $r_{0}^{D}$ is symmetric and trace-free, and the trace part defines the scalar curvature of $D$.
2.5. Proposition. - On a Kähler-Weyl $n$-manifold $(n>2)$ with Weyl derivative $D, F^{D} \wedge \Omega_{J}$ and the commutator $\left[R_{X, Y}^{D, w}, J\right]$ both vanish. If $n>4$ it follows that $F^{D}=0$, while for $n=4, F^{D}$ is orthogonal to $\Omega_{J}$.

Also if $R^{D}=R^{D, 1}$ then the symmetric Ricci tensor is given by the formula
$$\frac{1}{2}\left\langle R_{J e_{i}, e_{i}}^{D} X, J Y\right\rangle=(n-2) r_{0}^{D}(X, Y)+\frac{1}{n} \operatorname{scal}^{D}\langle X, Y\rangle,$$
where on the left we are summing over a weightless orthonormal basis $e_{i}$. Consequently the symmetric Ricci tensor is $J$-invariant.

Proof. - The first two facts are immediate from $d^{D} \Omega_{J}=0$ and $D J=0$ respectively. If $n>4$ then wedge product with $\Omega_{J}$ is injective on 2-forms, while for $n=4, F^{D} \wedge \Omega_{J}$ is the multiple $\pm\left\langle F^{D}, \Omega_{J}\right\rangle$ of the weightless volume form, since $\Omega_{J}$ is antiselfdual. The final formula is a consequence of the first Bianchi identity:
$$\begin{aligned}
& \frac{1}{2}\left\langle R_{J e_{i}, e_{i}}^{D} X, J Y\right\rangle=\left\langle R_{X, e_{i}}^{D} J e_{i}, J Y\right\rangle=\left\langle R_{X, e_{i}}^{D} e_{i}, Y\right\rangle \\
& \quad=F^{D}\left(X, e_{i}\right)\left\langle e_{i}, Y\right\rangle-\left\langle r^{D}(X) \Delta e_{i} e_{i}, Y\right\rangle+\left\langle r^{D}\left(e_{i}\right) \Delta X e_{i}, Y\right\rangle \\
& \quad=(n-2) r_{0}^{D}(X, Y)+\frac{1}{n} \operatorname{scal}^{D}\langle X, Y\rangle-\frac{1}{2}(n-4) F^{D}(X, Y)
\end{aligned}$$
and the last term vanishes since $F^{D}=0$ for $n>4$. \(\square\)

Now suppose $n=4$. Then $W_{X, Y}^{+}$commutes with $J$, and so
$$\begin{aligned}
J \circ W_{X, Y}^{-}-W_{X, Y}^{-} \circ J=J \circ( & \left.r^{D}(X) \Delta Y-r^{D}(Y) \Delta X\right) \\
& -\left(r^{D}(X) \Delta Y-r^{D}(Y) \Delta X\right) \circ J .
\end{aligned}$$
The bundle of antiselfdual Weyl tensors may be identified with the rank 5 bundle of symmetric trace-free maps $L^{2} \Lambda_{-}^{2} T^{*} M \rightarrow \Lambda_{-}^{2} T^{*} M$, where $W^{-}(U \wedge V)(X \wedge Y)=\left\langle W_{U, V}^{-} X, Y\right\rangle$ and we identify $L^{2} \Lambda_{-}^{2} T^{*} M$ with $L^{-2} \Lambda_{-}^{2} T M$. Under the unitary group $L^{2} \Lambda_{-}^{2} T^{*} M$ decomposes into the span of $J$ and the weightless canonical bundle $L^{2} K_{J}$. This bundle of Weyl tensors therefore decomposes into three pieces: the Weyl tensors acting by scalars on $\langle J\rangle$ and $L^{2} K_{J}$; the symmetric trace-free maps $L^{2} K_{J} \rightarrow K_{J}$ (acting trivially on $\langle J\rangle$ ); and the Weyl tensors mapping $\langle J\rangle$ into $K_{J}$ and vice versa. These subbundles have ranks 1,2 and 2 respectively. Since no nonzero Weyl tensor acts trivially on $K_{J}$, it follows that the above formula determines $W^{-}$uniquely in terms of $r^{D}$. Now this is an invariant formula which is linear in $r^{D}$, so $r_{0}^{D}$ and $F_{+}^{D}$ cannot contribute: they are sections of (isomorphic) irreducible rank 3 bundles. Thus the first and third components of $W^{-}$are given by scal ${ }^{D}$ and $F_{-}^{D}$ respectively, and the second component must vanish. The numerical factors can now be found by taking a trace.
2.6. Proposition (cf. [1]). - On a Kähler-Weyl 4-manifold with Weyl derivative $D$,
$$W^{-}=\frac{1}{4} \operatorname{scal}^{D}\left(\frac{1}{3} \mathrm{id}_{\Lambda_{-}^{2}}-\frac{1}{2} \Omega_{J} \otimes \Omega_{J}\right)-\frac{1}{2}\left(J F_{-}^{D} \otimes \Omega_{J}+\Omega_{J} \otimes J F_{-}^{D}\right),$$
where $J F_{-}^{D}=F_{-}^{D} \circ J$. In particular $W^{-}=0$ if and only if $F_{-}^{D}=0$ and $\mathrm{scal}^{D}=0$.

The Ricci form $\rho^{D}$ on $M$ is defined to be the curvature of $D$ on the weightless canonical bundle $L^{2} K_{J}$. Therefore
$$\begin{aligned}
\rho^{D}(X, Y) & =-\frac{i}{2}\left\langle R_{X, Y}^{D} e_{k}, J e_{k}\right\rangle \\
& =-\frac{i}{2}\left(\left\langle R_{X, e_{k}}^{D} e_{k}, J Y\right\rangle-\left\langle R_{Y, e_{k}}^{D} e_{k}, J X\right\rangle\right) \\
& =i\left(2 r_{0}^{D}(J X, Y)+\frac{1}{4} \operatorname{scal}^{D}\langle J X, Y\rangle+2 F_{-}^{D}(J X, Y)\right) .
\end{aligned}$$
Thus $W^{-}=0$ if and only if $\rho^{D}$ and $F^{D}$ are selfdual 2-forms.

\section*{3. Shear-free geodesic congruences and Einstein-Weyl geometry.}

On a conformal manifold, a foliation with oriented one dimensional leaves may be described by a weightless unit vector field $\chi$. (If $K$ is any nonvanishing vector field tangent to the leaves, then $\chi= \pm K /|K|$.) Such a foliation, or equivalently, such a $\chi$, is often called a congruence.

If $D$ is any Weyl derivative, then $D \chi$ is a section of $T^{*} M \otimes L^{-1} T M$ satisfying $\langle D \chi, \chi\rangle=0$, since $\chi$ has unit length. Let $\chi^{\perp}$ be the orthogonal complement of $\chi$ in $L^{-1} T M$. Under the orthogonal group of $\chi^{\perp}$ acting trivially on the span of $\chi$, the bundle $T^{*} M \otimes \chi^{\perp}$ decomposes into four irreducible components: $L^{-1} \Lambda^{2}\left(\chi^{\perp}\right), L^{-1} S_{0}^{2}\left(\chi^{\perp}\right), L^{-1}$ (multiples of the identity $\chi^{\perp} \mapsto \chi^{\perp}$ ), and $L^{-1} \chi^{\perp}$ (the $\chi^{\perp}$-valued 1-forms vanishing on vectors orthogonal to $\chi$ ).

The first three components of $D \chi$ may be found by taking the skew, symmetric trace-free and tracelike parts of $D_{\chi}-\chi \otimes D_{\chi} \chi$, while the final component is simply $D_{\chi} \chi$. These components are respectively called the twist, shear, divergence, and acceleration of $\chi$ with respect to $D$. If any of these vanish, then the congruence $\chi$ is said to be twist-free, shear-free, divergence-free, or geodesic accordingly.
3.1. Proposition. - Let $\chi$ be a unit section of $L^{-1} T M$. Then the shear and twist of $\chi$ are independent of the choice of Weyl derivative $D$. Furthermore there is a unique Weyl derivative $D^{\chi}$ with respect to which $\chi$ is divergence-free and geodesic.

This follows from the fact that $(D+\gamma) \chi=D \chi+\gamma(\chi) \mathrm{id}-\chi \otimes \gamma$.
The twist is simply the Frobenius tensor of $\chi^{\perp}$ (i.e., the $\chi$ component of the Lie bracket of sections of $\chi^{\perp}$ ), while the shear measures the Lie derivative of the conformal structure of $\chi^{\perp}$ along $\chi$ (which makes sense even though $\chi$ is weightless).
3.2. Remark. - If $D^{\chi}$ is exact, with $D^{\chi} \mu=0$, then $K=\mu \chi$ is a geodesic divergence-free vector field of unit length with respect to the metric $g=\mu^{-2} c$. If $\chi$ is also shear-free, then $K$ is a Killing field of $g$. Note conversely that any nonvanishing conformal vector field $K$ is a Killing field of constant length $a$ for the compatible metric $a^{2}|K|^{-2} \boldsymbol{c}: \chi=K /|K|$ is then a shear-free congruence, and $D^{\chi}$ is the exact Weyl derivative $D^{|K|}$, which we call the constant length gauge of $K$.

We now turn to the study of geodesic congruences in three dimensional Weyl spaces and their relationship to Einstein-Weyl geometry and minitwistor theory (see [14], [20], [26]). We discuss the "mini-Kerr theorem" which is rather a folk theorem in the existing literature, and rewrite the Einstein-Weyl condition in a novel way by finding special monopole equations associated to a shear-free geodesic congruence.

The minitwistor space of an oriented geodesically convex Weyl space is its space of oriented geodesics. We assume that this is a manifold (i.e., we ignore the fact that it may not be Hausdorff), as we shall only be using minitwistor theory to probe the local geometry of the Weyl space. The minitwistor space is four dimensional, and has a distinguished family of embedded 2-spheres corresponding to the geodesics passing through given points in the Weyl space.

Now let $\chi$ be a geodesic congruence on an oriented Weyl space $B$ with Weyl connection $D^{B}$. Then
$$D^{B} \chi=\tau(\mathrm{id}-\chi \otimes \chi)+\kappa * \chi+\Sigma,$$
where the divergence and twist, $\tau$ and $\kappa$, are sections of $L^{-1}$ and $\Sigma$ is the shear. Note that $D^{\chi}=D^{B}-\tau \chi$.

Equation (3.1) admits a natural complex interpretation, which we give in order to compare our formulae to those in the literature [15], [26]. Let $\mathcal{H}=\chi^{\perp} \otimes \mathbb{C}$ in the complexified weightless tangent bundle. Then $\mathcal{H}$ has a complex bilinear inner product on each fibre and the orientation of $B$ distinguishes one of the two null lines: if $e_{1}, e_{2}$ is an oriented real orthonormal basis, then $e_{1}+i e_{2}$ is null. Let $Z$ be a section of this null line with $\langle Z, \bar{Z}\rangle=1$. Such a $Z$ is unique up to pointwise multiplication by a unit complex number: at each point it is of the form $\left(e_{1}+i e_{2}\right) / \sqrt{2}$. Now $D^{B} \chi=\rho Z \otimes \bar{Z}+\bar{\rho} \bar{Z} \otimes Z+\sigma Z \otimes Z+\bar{\sigma} \bar{Z} \otimes \bar{Z}$, where $\rho=\tau+i \kappa$ and $\sigma=\Sigma(\bar{Z}, \bar{Z})$ are sections of $L^{-1} \otimes \mathbb{C}$. Note that $\sigma$ depends on the choice of $Z$ : the ambiguity can partially be removed by requiring that $D_{\chi}^{B} Z=0$, but we shall instead work directly with $\Sigma$.
3.3. Conventions. - There are two interesting sign conventions for the Hodge star operator of an oriented conformal manifold. The first satisfies $\alpha \wedge \tilde{*} \beta=\langle\alpha, \beta\rangle \underline{\mathrm{or}}$, where or is the unit section of $L^{n} \Lambda^{n} T^{*} M$ given by the orientation. This is convenient when computing the star operator of an explicit example. The second satisfies $* 1=\underline{\text { or }}$ and $\iota_{X} * \alpha=*(X \wedge \alpha)$, which is a more useful property in many theoretical calculations. Also $*^{2}=(-1)^{\frac{1}{2} n(n-1)}$ depends only on the dimension of the manifold, not on the degree of the form. If $\alpha$ is a $k$-form, then $* \alpha=(-1)^{\frac{1}{2} k(k-1)} \tilde{*} \alpha$.
3.4. Proposition. - The curvature of $D^{B}$ applied to the geodesic congruence $\chi$ is given by
$$\begin{aligned}
R_{X, Y}^{B, 0} \chi=\iota_{\chi}[ & D_{X}^{B} \tau \chi \wedge Y-D_{Y}^{B} \tau \chi \wedge X-D_{X}^{B} \kappa * Y+D_{Y}^{B} \kappa * X \\
& \left.+\left(\tau^{2}-\kappa^{2}\right) X \wedge Y-2 \tau \kappa \chi \wedge *(X \wedge Y)\right]+\left(D_{X}^{B} \Sigma\right)(Y) \\
& -\left(D_{Y}^{B} \Sigma\right)(X)-\tau(\Sigma(X)\langle\chi, Y\rangle-\Sigma(Y)\langle\chi, X\rangle) \\
& +\kappa *(Y \wedge \Sigma(X)-X \wedge \Sigma(Y))
\end{aligned}$$
and also by its decomposition
$$\begin{aligned}
& R_{X, Y}^{B, 0} \chi \\
& \quad=r_{0}^{B}(Y, \chi) X-\frac{1}{2} F^{B}(Y, \chi) X+\left(r_{0}^{B}(X)+\frac{1}{6} \operatorname{scal}^{B} X-\frac{1}{2} F^{B}(X)\right)\langle\chi, Y\rangle \\
& -r_{0}^{B}(X, \chi) Y+\frac{1}{2} F^{B}(X, \chi) Y-\left(r_{0}^{B}(Y)+\frac{1}{6} \operatorname{scal}^{B} Y-\frac{1}{2} F^{B}(Y)\right)\langle\chi, X\rangle
\end{aligned}$$

The first formula follows from $R_{X, Y}^{B, 0} \chi=D_{X}^{B}\left(D^{B} \chi\right)_{Y}-D_{Y}^{B}\left(D^{B} \chi\right)_{X}$, using
$$\begin{aligned}
D_{X}^{B}\left(D^{B} \chi\right)= & D_{X}^{B} \tau(\mathrm{id}-\chi \otimes \chi)+D_{X}^{B} \kappa * \chi \\
& -\tau\left(D_{X}^{B} \chi \otimes \chi+\chi \otimes D_{X}^{B} \chi\right)+\kappa * D_{X}^{B} \chi+D_{X}^{B} \Sigma .
\end{aligned}$$

The second formula follows easily from $R_{X, Y}^{B, 0}=-r^{B}(X) \triangle Y+r^{B}(Y) \triangle X$ where $r^{B}=r_{0}^{B}+\frac{1}{12} \mathrm{scal}^{B}-\frac{1}{2} F^{B}$.

In order to compare the rather different formulae in Proposition 3.4, we shall first take $Y$ parallel to $\chi$ and $X$ orthogonal to $\chi$. The formulae reduce to
$$\begin{aligned}
& D_{\chi}^{B} \tau X+D_{\chi}^{B} \kappa J X+\left(\tau^{2}-\kappa^{2}\right) X+2 \tau \kappa J X \\
& \quad+\Sigma\left(D_{X}^{B} \chi\right)+\left(D_{\chi}^{B} \Sigma\right)(X)+\tau \Sigma(X)-\kappa \Sigma(J X) \\
& \quad=-R_{X, \chi}^{B, 0} \chi \\
& =-r_{0}^{B}(X)+r_{0}^{B}(X, \chi) \chi+\frac{1}{2}\left(F^{B}(X)-F^{B}(X, \chi) \chi\right) \\
& \quad-r_{0}^{B}(\chi, \chi) X-\frac{1}{6} \operatorname{scal}^{B} X,
\end{aligned}$$
where $J X:=\iota_{X} * \chi$ and we have used the fact that
$$\left(D_{X}^{B} \Sigma\right)(\chi)+\Sigma\left(D_{X}^{B} \chi\right)=0 .$$
If we contract with another vector field $Y$ orthogonal to $\chi$, then we obtain
$$\begin{aligned}
D_{\chi}^{B} \tau & \langle X, Y\rangle+D_{\chi}^{B} \kappa\langle J X, Y\rangle+\left\langle\left(D_{\chi}^{B} \Sigma\right)(X), Y\right\rangle \\
& +\left(\tau^{2}-\kappa^{2}\right)\langle X, Y\rangle+2 \tau \kappa\langle J X, Y\rangle+2 \tau\langle\Sigma(X), Y\rangle+\langle\Sigma(X), \Sigma(Y)\rangle \\
& =-r_{0}^{B}(X, Y)+\frac{1}{2} F^{B}(X, Y)-\left(r_{0}^{B}(\chi, \chi)-\frac{1}{6} \operatorname{scal}^{B}\right)\langle X, Y\rangle .
\end{aligned}$$
Decomposing this into irreducibles gives the equations
$$\begin{aligned}
D_{\chi}^{B} \tau+\tau^{2}-\kappa^{2}+\frac{1}{2}|\Sigma|^{2}+\frac{1}{2} r_{0}^{B}(\chi, \chi)+\frac{1}{6} \operatorname{scal}^{B} & =0, \\
D_{\chi}^{B} \kappa+2 \tau \kappa+\frac{1}{2}\left\langle\chi, * F^{B}\right\rangle & =0, \\
D_{\chi}^{B} \Sigma+2 \tau \Sigma+\operatorname{sym}_{0}^{\chi^{\perp}} r_{0}^{B} & =0,
\end{aligned}$$
which may, assuming $D_{\chi}^{B} Z=0$, be rewritten as
$$\begin{aligned}
D_{\chi}^{B} \rho+\rho^{2}+\sigma \bar{\sigma}+\frac{1}{2} r_{0}^{B}(\chi, \chi)+\frac{1}{6} \operatorname{scal}^{B}+\frac{i}{2}\left\langle\chi, * F^{B}\right\rangle & =0, \\
D_{\chi}^{B} \sigma+(\rho+\bar{\rho}) \sigma+r_{0}^{B}(\bar{Z}, \bar{Z}) & =0 .
\end{aligned}$$

Along a single geodesic, these formulae describe the evolution of nearby geodesics in the congruence and therefore may be interpreted infinitesimally (cf. [26]). We say that a vector field $X$ along an oriented
geodesic $\Gamma$ with weightless unit tangent $\chi$ is a Jacobi field if and only if $\left(D^{B}\right)_{\chi, \chi}^{2} X=R_{\chi, X}^{B, 0} \chi$. The space of Jacobi fields orthogonal to $\Gamma$ is four dimensional, since the initial data for the Jacobi field equation is $X, D_{\chi}^{B} X$. In fact this is the tangent space to the minitwistor space at $\Gamma$. If we now consider a two dimensional family of Jacobi fields spanning (at each point on an open subset of $\Gamma$ ) the plane orthogonal to $\Gamma$, then we may write $D_{\chi}^{B} X=\tau X+\kappa J X+\Sigma(X)$ for the Jacobi fields $X$ in this family. If we differentiate again with respect to $\chi$, we reobtain the equations (3.2)-(3.6).

A geodesic congruence gives rise to such a two dimensional family of Jacobi fields along each geodesic in the congruence. We define the Lie derivative $\mathcal{L}_{\chi} X$ of a vector field $X$ along $\chi$ to be the horizontal part of $D_{\chi}^{B} X-D_{X}^{B} \chi$. Then if $\mathcal{L}_{\chi} X=0, X$ is a Jacobi field, and such Jacobi fields are determined along a geodesic by their value at a point. Next note that $\mathcal{L}_{\chi} J=0$ (i.e., $\mathcal{L}_{\chi}(J X)=J \mathcal{L}_{\chi} X$ ) if and only if $\chi$ is shear-free. However, equation (3.4) shows that if $\chi$ is a shear-free, then $r_{0}^{B}(X, Y)=-\frac{1}{2} r_{0}^{B}(\chi, \chi)\langle X, Y\rangle$ for all $X, Y$ orthogonal to $\chi$. More generally, this equation shows that $J$ is a well defined complex structure on the space of Jacobi fields orthogonal to a geodesic $\Gamma$ if and only if $r_{0}^{B}(X, Y)=-\frac{1}{2} r_{0}^{B}(\chi, \chi)\langle X, Y\rangle$ for all $X, Y$ orthogonal to $\Gamma$. The Jacobi fields defined by a congruence are then invariant under $J$ if and only if the congruence is shear-free.
3.5. Definition (cf. [14]). - A Weyl space $B, D^{B}$ is said to be Einstein-Weyl if and only if $r_{0}^{B}=0$.

As mentioned above, the space of orthogonal Jacobi fields along a geodesic is the tangent space to the minitwistor space at that geodesic. Therefore, if $B$ is Einstein-Weyl, the minitwistor space admits a natural almost complex structure. This complex structure turns out to be integrable, and so the minitwistor space of an Einstein-Weyl space is a complex surface $\mathcal{S}$ containing a family of rational curves, called minitwistor lines, parameterised by points in $B$ [14]. These curves have normal bundle $\mathcal{O}(2)$ and are invariant under the real structure on $\mathcal{S}$ defined by reversing the orientation of a geodesic. Conversely, any complex surface with real structure, containing a real (i.e., invariant) rational curve with normal bundle $\mathcal{O}(2)$, determines an Einstein-Weyl space as the real points in the Kodaira moduli space of deformations of this curve. We therefore have a twistor construction for Einstein-Weyl spaces, called the Hitchin correspondence. We note that the canonical bundle $K_{\mathcal{S}}$ of $\mathcal{S}$ has degree-4 on each minitwistor line.

Since geodesics correspond to points in the minitwistor space, a geodesic congruence defines a real surface $\mathcal{C}$ intersecting each minitwistor line once. By the definition of the complex structure on $\mathcal{S}$, the surface $\mathcal{C}$ is a holomorphic curve if and only if the geodesic congruence is shear-free. This may be viewed as a minitwistor version of the Kerr theorem: every shear-free geodesic congruence in an Einstein-Weyl space is obtained locally from a holomorphic curve in the minitwistor space. In particular, we have the following.
3.6. Proposition. - Let $B, D^{B}$ be a three dimensional Weyl space. Then the following are equivalent:
\begin{itemize}
\item[(i)] $B$ is Einstein-Weyl.
\item[(ii)] Given any point $b \in B$ and any unit vector $v \in L^{-1} T_{b} B$, there is a shear-free geodesic congruence $\chi$ defined on a neighbourhood of $b$ with $\chi_{b}=v$.
\item[(iii)] Given any point $b \in B$ there are three shear-free geodesic congruences defined on a neighbourhood of $b$ which are pairwise non-tangential at $b$.
\end{itemize}

Proof. - Clearly (ii) implies (iii). It is immediate from (3.4) that (ii) implies (i); to obtain the stronger result that (iii) implies (i) suppose that $B$ is not Einstein-Weyl, i.e., at some point $b \in B, r_{0}^{B} \neq 0$. If $\chi$ is a shear-free geodesic congruence near $b$ then by equation (3.4), $r_{0}^{B}$ is a multiple of the identity on $\chi^{\perp}$, and one easily sees that this multiple must be the middle eigenvalue $\lambda_{0} \in L_{b}^{-2}$ of $r_{0}^{B}$ at $b$. Now at $b, r_{0}^{B}$ may be written $\alpha \otimes \sharp \beta+\beta \otimes \sharp \alpha+\lambda_{0}$ id where $\alpha, \beta \in T_{b}^{*} B$ with $\langle\alpha, \beta\rangle=-\frac{3}{2} \lambda_{0}$. The directions of $\sharp \alpha$ and $\sharp \beta$ are uniquely determined by $r_{0}^{B}$ and $\chi$ must lie in one of these directions. Hence if $B$ is not Einstein-Weyl at $b$, there are at most two possible directions at $b$ (up to sign) for a shear-free geodesic congruence. (Note that the linear algebra involved here is the same as that used to show that there are at most two principal directions of a nonzero antiselfdual Weyl tensor in four dimensions; see, for instance [1]. Our result is just the symmetry reduction of this fact.)

Finally, to see that (i) implies (ii), we simply observe that given any minitwistor line and any point on that line, we can find, in a neighbourhood of that point, a transverse holomorphic curve. This curve will also intersect nearby minitwistor lines exactly once. \(\square\)

We now want to study Einstein-Weyl spaces with a shear-free geodesic congruence in more detail. As motivation for our main result, notice that the curve $\mathcal{C}$ in the minitwistor space given by $\chi$ defines divisors $\mathcal{C}+\overline{\mathcal{C}}$ and $\mathcal{C}-\overline{\mathcal{C}}$ such that the line bundles $[\mathcal{C}+\overline{\mathcal{C}}] K_{\mathcal{S}}^{1 / 2}$ and $[\mathcal{C}-\overline{\mathcal{C}}]$ are trivial on each minitwistor line. It is well known [16] that such line bundles correspond to solutions $(w, A)$ of the abelian monopole equation $* D^{B} w=d A$, where $w$ is a section of $L^{-1}$ and $A$ is a 1-form. Therefore, we should be able to find two special solutions of this monopole equation, one real and one imaginary, associated to any shear-free geodesic congruence.

These solutions turn out to be $\kappa$ and $i \tau$. To see this, we return to the curvature equations in Proposition 3.4 and look at the horizontal components. If $X, Y$ are orthogonal to a geodesic congruence $\chi$ on any three dimensional Weyl space then
$$\begin{aligned}
D_{X}^{B} \tau Y & -D_{Y}^{B} \tau X+D_{X}^{B} \kappa J Y-D_{Y}^{B} \kappa J X \\
& +\left(D_{X}^{B} \Sigma\right)(Y)-\left(D_{Y}^{B} \Sigma\right)(X)+\kappa *(Y \wedge \Sigma(X)-X \wedge \Sigma(Y)) \\
& =r_{0}^{B}(Y, \chi) X-\frac{1}{2} F^{B}(Y, \chi) X-r_{0}^{B}(X, \chi) Y+\frac{1}{2} F^{B}(X, \chi) Y .
\end{aligned}$$
If $\chi$ is shear-free this reduces to the equation
$$D_{X}^{B} \tau-D_{J X}^{B} \kappa+r_{0}^{B}(\chi, X)+\frac{1}{2} F^{B}(\chi, X)=0,$$
where $X \perp \chi$. From this, and our earlier formulae, we have:
3.7. Proposition. - Let $\chi$ be shear-free geodesic congruence with divergence $\tau$ and twist $\kappa$ in a three dimensional Weyl space $B$. Then $\chi$ satisfies the equations
$$\begin{aligned}
D_{\chi}^{B} \tau+\tau^{2}-\kappa^{2}+\frac{1}{6} \operatorname{scal}^{B} & =0, \\
D_{\chi}^{B} \kappa+2 \tau \kappa+\frac{1}{2}\left\langle\chi, * F^{B}\right\rangle & =0, \\
\left(D^{B} \tau-D^{B} \kappa \circ J\right)_{\mid \chi^{\perp}}+\frac{1}{2} \iota_{\chi} F^{B} & =0,
\end{aligned}$$
if and only if $B$ is Einstein-Weyl.
The last equation, like the first two (see (3.5)), admits a natural complex formulation in terms of $\rho$. Instead, however, we shall combine these equations to give the following result.
3.8. Theorem. - The three dimensional Einstein-Weyl equations are equivalent to the following special monopole equations for a shear-free geodesic congruence $\chi$ with $D^{B} \chi=\tau(\mathrm{id}-\chi \otimes \chi)+\kappa * \chi$ :
$$\begin{aligned}
& * D^{B} \tau=-\frac{1}{2} * \iota_{\chi} F^{B}-\frac{1}{6} \operatorname{scal}^{B} * \chi-\left(\tau^{2}+\kappa^{2}\right) * \chi+d(\kappa \chi), \\
& * D^{B} \kappa=\frac{1}{2} F^{B}-d(\tau \chi) .
\end{aligned}$$
(By "monopole equations", we mean that the right hand sides are closed 2-forms. Note also that these equations are not independent: they are immediately equivalent to (3.7) and (3.11), or to (3.8) and (3.10).)

Proof. - The equations of the previous proposition are equivalent to the following:
$$\begin{aligned}
& D^{B} \tau=D^{B} \kappa \circ J+\left(\kappa^{2}-\tau^{2}\right) \chi-\frac{1}{6} \operatorname{scal}^{B} \chi-\frac{1}{2} \iota_{\chi} F^{B}, \\
& D^{B} \kappa=-D^{B} \tau \circ J-2 \tau \kappa \chi-\frac{1}{2} * F^{B} .
\end{aligned}$$
Applying the star operator readily yields the equations of the theorem. The second equation is clearly a monopole equation, since $F^{B}$ is closed. It remains to check that the right hand side of the first equation is closed:
$$\begin{aligned}
& d\left(\frac{1}{2} \chi \wedge * F^{B}+\frac{1}{6} \mathrm{scal}^{B} * \chi+\left(\tau^{2}+\kappa^{2}\right) * \chi\right) \\
& \quad=\frac{1}{2} d^{B} \chi \wedge * F^{B}-\frac{1}{2} \chi \wedge * \delta^{B} F^{B}+\frac{1}{6} D^{B} \mathrm{scal}^{B} \wedge * \chi \\
& \quad+\left(2 \tau D^{B} \tau+2 \kappa D^{B} \kappa\right) \wedge * \chi+\left(\frac{1}{6} \mathrm{scal}^{B}+\tau^{2}+\kappa^{2}\right) * \delta^{B} \chi \\
& \quad=\frac{1}{2} \chi \wedge *\left(\frac{1}{3} D^{B} \mathrm{scal}^{B}-\delta^{B} F^{B}\right) \\
& \quad+\left(\kappa\left\langle\chi, * F^{B}\right\rangle+2 \tau D_{\chi}^{B} \tau+2 \kappa D_{\chi}^{B} \kappa+2 \tau\left(\frac{1}{6} \mathrm{scal}^{B}+\tau^{2}+\kappa^{2}\right)\right) * 1 .
\end{aligned}$$
Here $\delta^{B}=\operatorname{tr} D^{B}$ is the divergence on forms, and so the first term vanishes by virtue of the second Bianchi identity. The remaining multiple of the orientation form $* 1$ is
$$\kappa\left\langle\chi, * F^{B}\right\rangle+2 \kappa D_{\chi}^{B} \kappa+2 \kappa(2 \kappa \tau)+2 \tau D_{\chi}^{B} \tau+2 \tau\left(\frac{1}{6} \operatorname{scal}^{B}+\tau^{2}-\kappa^{2}\right),$$
which vanishes by the previous proposition. \(\square\)

Two key special cases of this theorem have already been studied.

\section*{LeBrun-Ward geometries}

Suppose an Einstein-Weyl space admits a shear-free geodesic congruence which is also twist-free. Then $\kappa=0$ and so the Einstein-Weyl equations (3.7), (3.11) are:
$$\begin{aligned}
D_{\chi}^{B} \tau+\tau^{2} & =-\frac{1}{6} \text { scal }^{B}, \\
F^{B}=2 d(\tau \chi) & =2 D^{B} \tau \wedge \chi .
\end{aligned}$$
As observed by Tod [29], these Einstein-Weyl spaces are the spaces first studied by LeBrun [19], [20] and Ward [33], who described them using coordinates in which the above equations reduce to the $\operatorname{SU}(\infty)$ Toda field equation $u_{x x}+u_{y y}+\left(e^{u}\right)_{z z}=0$. Consequently these Einstein-Weyl spaces are also said to be Toda.

It may be useful here to sketch how this follows from our formulae, since Lemma 4.1 in [29], given there without proof, is only true after making use of the gauge freedom to set $z=f(\tilde{z})$ and rescale the metric by $f^{\prime}(\tilde{z})^{-2}$. The key point is that since $D^{L W}:=D^{B}-2 \tau \chi$ is locally exact by (3.13), there is locally a canonical gauge (up to homothety) in which to work, which we call the LeBrun-Ward gauge $\mu_{L W}$. Since $\chi$ is twist-free and also geodesic with respect to $D^{L W}$, the 1-form $\mu_{L W}^{-1} \chi$ is locally exact. Taking this to be $d z$ and introducing isothermal coordinates $(x, y)$ on the quotient of $B$ by $\chi$, we may write $g_{L W}=\mathrm{e}^{u}\left(d x^{2}+d y^{2}\right)+d z^{2}$ for some function $u(x, y, z)$, since $\chi$ is shear-free. By computing the divergence of $\chi$ we then find that the Toda monopole is $\tau=-\frac{1}{2} u_{z} \mu_{L W}^{-1}$, and equation (3.12) reduces easily in this gauge to the Toda equation. One of the reasons for the interest in this equation is that it may be used to construct hyperKähler and scalar-flat Kähler 4-manifolds [3], [19], as we shall see in the next section.

LeBrun [19] shows that these spaces are characterised by the existence of a divisor $\mathcal{C}$ in the minitwistor space with $[\mathcal{C}+\overline{\mathcal{C}}]=K_{\mathcal{S}}^{-1 / 2}$. This agrees with our assertion that $[\mathcal{C}+\overline{\mathcal{C}}] K_{\mathcal{S}}^{1 / 2}$ corresponds to the monopole $\kappa$.

In [4], it is shown that an Einstein-Weyl space admits at most a three dimensional family of shear-free twist-free geodesic congruences.

\section*{Gauduchon-Tod geometries}

Suppose an Einstein-Weyl space admits a shear-free geodesic congruence which is also divergence-free. Then $\tau=0$ and so the Einstein-Weyl equations (3.7), (3.11) are:
$$\kappa^{2}=\frac{1}{6} \text { scal }^{B},$$
$$* D^{B} \kappa=\frac{1}{2} F^{B} .$$
It follows that these are the geometries which arose in the work of Gauduchon and Tod [12] and also Chave, Tod and Valent [7] on hypercomplex 4-manifolds with triholomorphic conformal vector fields. Gauduchon and Tod essentially observe the following equivalent formulation of these equations.
3.9. Proposition. - The connection $D^{\kappa}=D^{B}-\kappa * 1$ on $L^{-1} T B$ is flat.

Proof. - The curvature of $D^{\kappa}$ is easily computed to be:
$$\begin{aligned}
R_{X, Y}^{\kappa}=-r_{0}^{B}(X) \triangle & Y+r_{0}^{B}(Y) \triangle X-\frac{1}{6} \operatorname{scal}^{B} X \triangle Y+\frac{1}{2} F^{B}(X) \triangle Y \\
& -\frac{1}{2} F^{B}(Y) \triangle X-D_{X}^{B} \kappa * Y+D_{Y}^{B} \kappa * X+\kappa^{2} X \triangle Y .
\end{aligned}$$
Now $D_{X}^{B} \kappa * Y-D_{Y}^{B} \kappa * X=\left(* D^{B} \kappa\right)(X) \Delta Y-\left(* D^{B} \kappa\right)(Y) \Delta Y$, so equations (3.14) and (3.15) imply that $R_{X, Y}^{\kappa}$ vanishes if $B$ is Einstein-Weyl. (Conversely if there is a $\chi$ with $R_{X, Y}^{\kappa} \chi=0$ for all $X, Y$, then $B$ is Einstein-Weyl.) \(\square\)

This shows that the existence of a single shear-free divergence-free geodesic congruence gives an entire 2-sphere of such congruences and we say that these Einstein-Weyl spaces are hyperCR [6]. There is also a simple minitwistor interpretation of this. The divisor $\mathcal{C}$ corresponding to a shear-free divergence-free geodesic congruence has $[\mathcal{C}-\overline{\mathcal{C}}]$ trivial, i.e., $\mathcal{C}-\overline{\mathcal{C}}$ is the divisor of a meromorphic function. Hence we have a nonconstant holomorphic map from the minitwistor space to $\mathbb{C} P^{1}$, and its fibres correspond to the 2-sphere of congruences. This argument is the minitwistor analogue of the twistor characterisation of hypercomplex structures discussed in the previous section.

Since the Einstein-Weyl structure determines $\kappa$ up to sign, it follows that an Einstein-Weyl space admits at most two hyperCR structures. If it admits exactly two, then we must have $\kappa \neq 0$ and $F^{B}=0$, i.e., the Einstein-Weyl space is the round sphere.

\section*{Einstein-Weyl spaces with a geodesic symmetry}

The Einstein-Weyl equation can be completely solved in the case of Einstein-Weyl spaces admitting a shear-free geodesic congruence $\chi$ such
that $\chi=K /|K|$ with $K$ a conformal vector field preserving the Weyl connection. In this case $D^{\chi}=D^{B}-\tau \chi$ is exact, $|K|$ being a parallel section of $L^{1}$ (see Remark 3.2). We introduce $g=|K|^{-2} \boldsymbol{c}$ so that $D^{\chi}=D^{g}$. Since $K$ preserves the Weyl connection and $\mathcal{L}_{K} g=0$, we may write $\tau=\tau_{g}|K|^{-1}$, $\kappa=\kappa_{g}|K|^{-1}$, where $\partial_{K} \tau_{g}=\partial_{K} \kappa_{g}=0$. Now $\iota_{\chi} F^{B}=\iota_{\chi} d(\tau \chi)=-D^{g} \tau$ and so equation (3.9) becomes
$$\frac{1}{2} d \tau_{g}-d \kappa_{g} \circ J=0 .$$
This is solved by setting $2 \kappa_{g}-i \tau_{g}=H$, where $H$ is a holomorphic function on the quotient $C$ of $B$ by $K$. Since $D_{\chi}^{B} \tau=-\tau^{2}$ and $D_{\chi}^{B} \kappa=-\tau \kappa$, the remaining Einstein-Weyl equations reduce to $\tau \kappa+\frac{1}{2}\left\langle\chi, * F^{B}\right\rangle=0$ and $\kappa^{2}=\frac{1}{6} \mathrm{scal}^{B}$. The first of these is automatic. To solve the second we note that scal ${ }^{B}$ can be computed from the scalar curvature of the quotient metric on $C$ using a submersion formula [2], [5]. This gives scal ${ }^{B}=\operatorname{scal}^{C}-2 \tau^{2}-2 \kappa^{2}$ and hence scal ${ }^{C}=2 \tau^{2}+8 \kappa^{2}=2|2 \kappa-i \tau|^{2}$. If this is zero, then $\tau=\kappa=0$ and $D^{B}$ is flat. Otherwise we observe that $\log |H|^{2}$ is harmonic, and so rescaling the quotient metric by $|H|^{2}$ gives a metric of constant curvature 1 (i.e., the scalar curvature is 2).

Remarkably, these Einstein-Weyl spaces are also all hyperCR: since $\kappa^{2}=\frac{1}{6}$ scal $^{B}$ and $* D^{B} \kappa=\frac{1}{2} F^{B}-d(\tau \chi)=-\frac{1}{2} F^{B}$, reversing the sign of $\kappa$ (or equivalently, reversing the orientation of $B$ ) solves the equations of the previous subsection. Thus we have established the following theorem.
3.10. Theorem. - The three dimensional Einstein-Weyl spaces with geodesic symmetry are either flat with translational symmetry or are given locally by
$$\begin{aligned}
g & =|H|^{-2}\left(\sigma_{1}^{2}+\sigma_{2}^{2}\right)+\beta^{2} \\
\omega & =\frac{i}{2}(H-\bar{H}) \beta \\
d \beta & =\frac{1}{2}(H+\bar{H})|H|^{-2} \sigma_{1} \wedge \sigma_{2}
\end{aligned}$$
where $\sigma_{1}^{2}+\sigma_{2}^{2}$ is the round metric on $S^{2}$, and $H$ is any nonvanishing holomorphic function on an open subset of $S^{2}$. The geodesic symmetry $K$ is dual to $\beta$ and the monopoles associated to $K /|K|$ are $\tau=\frac{1}{2} i(H-\bar{H}) \mu_{g}^{-1}$ and $\kappa=\frac{1}{4}(H+\bar{H}) \mu_{g}^{-1}$. These spaces all admit hyperCR structures, with flat connection $D^{B}+\kappa * 1$.

The equation for $\beta$ can be integrated explicitly. Indeed if $\zeta$ is a holomorphic coordinate such that $\sigma_{1} \wedge \sigma_{2}=2 i d \zeta \wedge d \bar{\zeta} /(1+\zeta \bar{\zeta})^{2}$ then one can take
$$\beta=d \psi+\frac{i}{1+\zeta \bar{\zeta}}\left(\frac{d \zeta}{\zeta H}-\frac{d \bar{\zeta}}{\bar{\zeta} \bar{H}}\right) .$$
Of course, this is not the only possible choice: for instance one can write $d \zeta /(\zeta H)=d F$ with $F$ holomorphic and use
$$\beta=d \psi-i(F-\bar{F}) d\left(\frac{1}{1+\zeta \bar{\zeta}}\right)$$

Note that $\omega$ is dual to a Killing field of $g$ if and only if $H$ is constant, in which case we obtain the well known Einstein-Weyl structures on the Berger spheres. The Einstein metric on $S^{3}$ arises when $H$ is real, in which case the connections $D^{B} \pm \kappa * 1$ are both flat: they are the left and right invariant connections. The flat Weyl structure with radial symmetry (which is globally defined on $S^{1} \times S^{2}$ ) occurs when $H$ is purely imaginary. Gauduchon and Tod [12] prove that these are the only hyperCR structures on compact Einstein-Weyl manifolds.

The fact that the Einstein-Weyl spaces with geodesic symmetry are hyperCR may equally be understood via minitwistor theory. Indeed, any symmetry $K$ (a conformal vector field preserving the Weyl connection) on a 3-dimensional Einstein-Weyl space induces a holomorphic vector field $X$ on the minitwistor space $\mathcal{S}$. If $K$ is nonvanishing, then on each minitwistor line, $X$ will be tangent at two points (since the normal bundle is $\mathcal{O}(2)$ ) and if the line corresponds to a real point $x$, then these two tangent points in $\mathcal{S}$ will correspond to the two orientations of the geodesic generated by $K_{x}$. Hence $X$ vanishes at a point of $\mathcal{S}$ if and only if $K$ is tangent along the corresponding geodesic.

Now if $K$ is a geodesic symmetry then $X$ will be tangent to each minitwistor line precisely at the points at which it vanishes, and the zeroset of $X$ will be a divisor (rather than isolated points). This means that $X$ is a section of a line subbundle $\mathcal{H}=[\operatorname{div} X]$ of $T \mathcal{S}$ transverse to the minitwistor lines ( $\mathcal{H}$ must be transverse even where $X$ vanishes, because $K$, being real, is not null, and so the points of tangency are simple): the $\kappa$ monopole of $K$ is therefore $\mathcal{H} \otimes K_{\mathcal{S}}^{1 / 2}$. Now the integral curves of the distribution $\mathcal{H}$ in the neighbourhood $U$ of some real minitwistor line give a holomorphic map from $U$ to $\mathbb{C} P^{1}$. Viewing this as a meromorphic function (by choosing conjugate points on $\mathbb{C} P^{1}$ ) we obtain a divisor $\mathcal{C}-\overline{\mathcal{C}}$, where $\mathcal{C}+\overline{\mathcal{C}}$ is a divisor
for $T S / \mathcal{H}$, because $T S / \mathcal{H}$ is isomorphic to $T \mathbb{C} P^{1}$ over each minitwistor line. Since $K_{\mathcal{S}}^{-1}=\mathcal{H} \otimes T \mathcal{S} / \mathcal{H}$ we find that $[\mathcal{C}+\overline{\mathcal{C}}] K_{\mathcal{S}}^{1 / 2}$ is dual to $\mathcal{H} \otimes K_{\mathcal{S}}^{1 / 2}$, which explains (twistorially) why the $\kappa$ monopole of the hyperCR structure is simply the negation of the $\kappa$ monopole of the geodesic symmetry.

Another explanation is that the geodesic symmetry preserves the hyperCR congruences. Indeed, we have the following observation.
3.11. Proposition. - Suppose that $B$ is a hyperCR Einstein-Weyl space with flat connection $D^{B}+\kappa * 1$. Then a vector field $K$ preserves the hyperCR congruences $\chi$ (i.e., $\mathcal{L}_{K} \chi=0$ for each $\chi$ ) if and only if it is a geodesic symmetry with twist $\kappa$.

Proof. - Since $\chi$ is a weightless vector field,
$$\mathcal{L}_{K} \chi=D_{K}^{B} \chi-D_{\chi}^{B} K+\frac{1}{3}\left(\operatorname{tr} D^{B} K\right) \chi .$$
This vanishes if and only if $D_{\chi}^{B} K=\frac{1}{3}\left(\operatorname{tr} D^{B} K\right) \chi-\kappa *(K \wedge \chi)$. Hence $\mathcal{L}_{K} \chi=0$ for all of the hyperCR congruences $\chi$ if and only if $D^{B} K=\frac{1}{3}\left(\operatorname{tr} D^{B} K\right) \mathrm{id}+\kappa * K$. This formula shows that $K$ is a conformal vector field, and that $K /|K|$ is a shear-free geodesic congruence with twist $\kappa$. Also $K$ preserves the flat connection $D^{B}+\kappa * 1$, since it preserves the parallel sections. Finally, note that the twist of $K$ is determined by the conformal structure from the skew part of $D^{|K|} K$, so it is also preserved by $K$. Hence $K$ preserves $D^{B}$ and is therefore a geodesic symmetry. \(\square\)

\section*{4. The Jones and Tod construction.}

In [16], Jones and Tod proved that the quotient of a selfdual conformal manifold $M$ by a conformal vector field $K$ is Einstein-Weyl: the twistor lines in the twistor space $Z$ of $M$ project to rational curves with normal bundle $\mathcal{O}(2)$ in the space $\mathcal{S}$ of trajectories of the holomorphic vector field on $Z$ induced by $K$. Furthermore the Einstein-Weyl space comes with a solution of the monopole equation from which $M$ can be recovered: indeed $Z$ is (an open subset of) the total space of the line bundle over $\mathcal{S}$ determined by this monopole. In other words there is a correspondence between selfdual spaces with symmetry and Einstein-Weyl spaces with monopoles. In this section, we explain the differential geometric constructions involved in the Jones and Tod correspondence, and prove that invariant antiselfdual
complex structures on $M$ correspond to shear-free geodesic congruences on $B$. These direct methods, although motivated by the twistor approach, also reveal what happens when $M$ is not selfdual.

Therefore we let $M$ be an oriented conformal manifold with a conformal vector field $K$, and (by restricting to an open set if necessary) we assume $K$ is nowhere vanishing. Let $D^{|K|}$ be the constant length gauge of $K$, so that $\left\langle D^{|K|} K,.\right\rangle$ is a weightless 2-form. One can compute $D^{|K|}$ in terms of an arbitrary Weyl derivative $D$ by the formula
$$D^{|K|}=D-\frac{\langle D K, K\rangle}{\langle K, K\rangle}=D-\frac{1}{4} \frac{(\operatorname{tr} D K) K}{\langle K, K\rangle}+\frac{1}{2} \frac{\left(d^{D} K\right)(K, .)}{\langle K, K\rangle},$$
where $\left(d^{D} K\right)(X, Y)=\left\langle D_{X} K, Y\right\rangle-\left\langle D_{Y} K, X\right\rangle$.
The key observation for the Jones and Tod construction is that there is a unique Weyl derivative $D^{\text {sd }}$ on $M$ such that $\left\langle D^{+} K,.\right\rangle$ is a weightless selfdual 2-form: let $\omega=-\left(* d^{D} K\right)(K,) /.\langle K, K\rangle$ (which is independent of $D$ ) and define
$$D^{\mathrm{sd}}=D^{|K|}+\frac{1}{2} \omega=D-\frac{1}{4} \frac{(\operatorname{tr} D K) K}{\langle K, K\rangle}+\frac{1}{2} \frac{\left(d^{D} K\right)(K, .)-\left(* d^{D} K\right)(K, .)}{\langle K, K\rangle} .$$
Since $D$ is arbitrary, we may take $D=D^{\text {sd }}$ to get $\left(D^{\text {sd }} K-* D^{\text {sd }} K\right)(K,)=$. from which it is immediate that $D^{\text {sd }} K=* D^{\text {sd }} K$ since an antiselfdual 2-form is uniquely determined by its contraction with a nonzero vector field. The Weyl derivative $D^{\text {sd }}$ plays a central role in the proof that $D^{B}=D^{|K|}+\omega$ is Einstein-Weyl on $B$. Notice that the conformal structure and Weyl derivatives $D^{|K|}, D^{\text {sd }}, D^{B}$ do indeed descend to $B$ because $K$ is a Killing field in the constant length gauge and $\omega$ is a basic 1-form. Since the Lie derivative of Weyl derivatives on $L^{1}$ is given by $\mathcal{L}_{K} D=\frac{1}{n} d \operatorname{tr} D K+F^{D}(K,$.$) , it follows that F^{\text {sd }}(K,)=.F^{B}(K,)=$.0 .

We call $D^{B}$ the Jones-Tod Weyl structure on $B$.
4.1. Theorem (cf. [16]). - Suppose $M$ is an oriented conformal 4-manifold and $K$ a conformal vector field such that $B=M / K$ is a manifold. Let $D^{|K|}$ be the constant length gauge of $K$ and $\omega=-2\left(* D^{|K|} K\right)(K,) /.\langle K, K\rangle$. Then the Jones-Tod Weyl structure $D^{B}=D^{|K|}+\omega$ is Einstein-Weyl on $B$ if and only if $M$ is selfdual.

Note that $* D^{B}|K|^{-1}=-* \omega|K|^{-1}$ is a closed 2-form. Conversely, if $\left(B, D^{B}\right)$ is an Einstein-Weyl 3-manifold and $w \in \mathrm{C}^{\infty}\left(B, L^{-1}\right)$ is a non-vanishing solution of the monopole equation $d * D^{B} w=0$ then there is
a selfdual 4-manifold $M$ with symmetry over $B$ such that $* D^{B} w$ is the curvature of the connection defined by the horizontal distribution.

Proof. - The monopole equation on $B$ is equivalent, via the definition of $\omega$, to the fact that $D^{\text {sd }}$ lies midway between $D^{B}$ and $D^{|K|}$. So it remains to show that under this condition, the Einstein-Weyl equation on $B$ is equivalent to the selfduality of $M$. The space of antiselfdual Weyl tensors is isomorphic to $S_{0}^{2}\left(K^{\perp}\right)$ via the map sending $W^{-}$to $W_{., K}^{-} K$, and so it suffices to show that $r_{0}^{B}=0$ if and only if $W_{., K}^{-} K=0$.

Since $D^{\text {sd }}$ is basic, as a Weyl connection on $T M, 0=\left(\mathcal{L}_{K} D^{\text {sd }}\right)_{X}=$ $R_{K, X}^{\text {sd }}+D_{X}^{\text {sd }} D^{\text {sd }} K$. Therefore
$$D_{X}^{\mathrm{sd}} D^{\mathrm{sd}} K=W_{X, K}+r^{\mathrm{sd}}(K) \Delta X-r^{\mathrm{sd}}(X) \Delta K .$$
If we now take the antiselfdual part of this equation, contract with $K$ and $Y$, and take $\langle X, K\rangle=\langle Y, K\rangle=0$, then we obtain
$$\begin{aligned}
2\left\langle W_{\bar{X}, K}^{-} K, Y\right\rangle+r^{\mathrm{sd}}(X, Y)\langle K, K\rangle+r^{\mathrm{sd}} & (K, K)\langle X, Y\rangle \\
& +*\left(K \wedge r^{\mathrm{sd}}(K) \wedge X \wedge Y\right)=0 .
\end{aligned}$$
Symmetrising in $X, Y$, we see that $W^{-}=0$ if and only if the horizontal part of the symmetric Ricci endomorphism of $D^{\text {sd }}$ is a multiple of the identity. The first submersion formula [2] relates the Ricci curvature of $D^{|K|}$ on $B$ to the horizontal Ricci curvature of $D^{|K|}$ on $M$. If we combine this with the fact that $D^{\text {sd }}=D^{|K|}+\frac{1}{2} \omega$ and $D^{B}=D^{|K|}+\omega$, then we find that
$$\begin{aligned}
\operatorname{sym} \operatorname{Ric}_{B}^{D^{B}}(X, Y)=\operatorname{sym} \operatorname{Ric}_{M}^{D^{\text {sd }}}(X, Y)+2\langle & \left.D_{X}^{|K|} K, D_{Y}^{|K|} K\right\rangle \\
& +\frac{1}{2} \omega(X) \omega(Y)+\mu\langle X, Y\rangle
\end{aligned}$$
for some section $\mu$ of $L^{-2}$. Since $D_{K}^{|K|} K=0, \omega$ vanishes on the plane spanned by $D^{|K|} K$, and so, by comparing the lengths of $\omega$ and $D^{|K|} K$, we verify that the trace-free part of $2\left\langle D_{X}^{|K|} K, D_{Y}^{|K|} K\right\rangle+\frac{1}{2} \omega(X) \omega(Y)$ vanishes. Hence $W^{-}=0$ on $M$ if and only if $D^{B}$ is Einstein-Weyl on $B$. \(\square\)

The inverse construction of $M$ from $B$ can be carried out explicitly by writing ${ }_{B}{ }_{B} D^{B}{ }_{W}=d A$ on $U \subset B$, so that the real line bundle $M$ is locally isomorphic to $U \times \mathbb{R}$ with connection $d t+A$, where $t$ is the fibre coordinate. Then the conformal structure $\boldsymbol{c}_{M}=\pi^{*} \boldsymbol{c}_{B}+w^{-2}(d t+A)^{2}$ is
selfdual and $K=\partial / \partial t$ is a unit Killing field of the representative metric $g_{M}=\pi^{*} w^{2} \boldsymbol{c}_{B}+(d t+A)^{2}$. Note that $w= \pm|K|^{-1}$ and that the orientations on $M$ and $B$ are related by $*(\xi \wedge \alpha)=\left(*_{B} \alpha\right) w|K|$ where $\alpha$ is any 1-form on $B$ and $\xi=K|K|^{-1}$. This ensures that if $D^{B}=D^{|K|}+\omega$, then the equation $-\left(*_{B} \omega\right) \mathrm{W}=*_{B} D^{B} \mathrm{~W}=d A$ is equivalent to $*(\xi \wedge \omega)|K|^{-1}=-d(d t+A)$ and hence $\omega=-\iota_{K}\left({ }^{*} d^{D} K\right) /|K|^{2}$ as above.

Jones and Tod also observe that any other solution $\left(w_{1}, A_{1}\right)$ of the monopole equation on $B$ corresponds to a selfdual Maxwell field on $M$ with potential $\widetilde{A}_{1}=A_{1}-\left(w_{1} / w\right)(d t+A)$. Indeed, since $(d t+A)=|K|^{-1} \xi$, one readily verifies that
$$d \widetilde{A}_{1}=\left(w^{-1}|K|^{-1} \xi \wedge D^{B} w_{1}+d A_{1}\right)-\frac{w_{1}}{w}\left(w^{-1}|K|^{-1} \xi \wedge D^{B} w+d A\right),$$
which is selfdual by the monopole equations for $w$ and $w_{1}$, together with the orientation conventions above.

We now want to explain the relationship between invariant complex structures on $M$ and shear-free geodesic congruences on $B$. That these should be related is again clear from the twistor point of view: indeed if $\mathcal{D}$ is an invariant divisor on $Z$, then it descends to a divisor $\mathcal{C}$ in $\mathcal{S}$, which in turn defines, at least locally, a shear-free geodesic congruence. The line bundles $[\mathcal{D}+\overline{\mathcal{D}}] K_{Z}^{1 / 2}$ and $[\mathcal{D}-\overline{\mathcal{D}}]$ are the pullbacks of $[\mathcal{C}+\overline{\mathcal{C}}] K_{\mathcal{S}}^{1 / 2}$ and $[\mathcal{C}-\overline{\mathcal{C}}]$ and so we expect the Faraday and Ricci forms on $M$ to be related to the twist and divergence of the congruence on $B$. In order to see all this in detail, and without the assumption of selfduality, we carry out the constructions directly.

Suppose that $J$ is an antiselfdual complex structure on $M$ with $\mathcal{L}_{K} J=0$, so that $K$ is a holomorphic conformal vector field. If $D$ is the Kähler-Weyl connection, then $D K=-\kappa_{0} \mathrm{id}+\frac{1}{2} \tau_{0} J+\frac{1}{2}\left(d^{D} K\right)^{+}$ where $\left(d^{D} K\right)^{+}$is a selfdual 2-form and $\kappa_{0}, \tau_{0}$ are functions.

Now let $\kappa=\kappa_{0}|K|^{-1}, \tau=\tau_{0}|K|^{-1}, \xi=K|K|^{-1}, \chi=J \xi$. Since $d^{D} K=\tau_{0} J+\left(d^{D} K\right)^{+}$, it follows that
$$d^{D} K(K, .)|K|^{-2}=\tau \chi+\left(d^{D} K\right)^{+}(K, .)|K|^{-2},$$
and
$$\left(* d^{D} K\right)(K, .)|K|^{-2}=-\tau \chi+\left(d^{D} K\right)^{+}(K, .)|K|^{-2} .$$
Therefore $D^{\text {sd }}=D+\kappa \xi+\tau \chi$ and $\left(d^{D} K\right)^{+}(K,.)|K|^{-2}=\tau \chi-\omega$.
4.2. Theorem. - Let $M$ be an oriented conformal 4-manifold with conformal vector field $K$ and suppose that $J$ is an invariant antiselfdual almost complex structure on $M$. Then $J$ is integrable if and only if $\chi=J \xi=J K /|K|$ is a shear-free geodesic congruence on the Jones-Tod Weyl space $B$. Furthermore, the Kähler-Weyl structure associated to $J$ is given by $D=D^{\mathrm{sd}}-\kappa \xi-\tau \chi$ where $D^{B} \chi=\tau(\mathrm{id}-\chi \otimes \chi)+\kappa * \chi$ on $B$.

Proof. - Clearly $\chi$ is invariant and horizontal, hence basic. Let $\tau, \kappa$ be invariant sections of $L^{-1}$ and set $D=D^{\mathrm{sd}}-\kappa \xi-\tau \chi$. If $J$ is integrable then we have seen above that the Kähler-Weyl connection is of this form. Therefore it suffices to prove that $D J=0$ if and only if $D^{B} \chi=\tau(\mathrm{id}-\chi \otimes \chi)+\kappa * \chi$ on $B$. Since $J=\xi \wedge \chi-*(\xi \wedge \chi)$ this is a straightforward computation. Let $X$ be any vector field on $M$. Then
$$D_{X} J=D_{X} \xi \wedge \chi+\xi \wedge D_{X} \chi-*\left(D_{X} \xi \wedge \chi-\xi \wedge D_{X} \chi\right) .$$
Now $D=D^{|K|}+\frac{1}{2} \omega-\kappa \xi-\tau \chi$ and so, since $D^{|K|} \xi=-\frac{1}{2} * \xi \wedge \omega$, we have
$$D_{X} \xi=-\frac{1}{2} *(X \wedge \xi \wedge \omega)-\frac{1}{2}\langle\xi, X\rangle \omega-\kappa(X-\langle\xi, X\rangle \xi)+\tau\langle\xi, X\rangle \chi .$$
Also $D=D^{B}-\frac{1}{2} \omega-\kappa \xi-\tau \chi$ and so
$$D_{X} \chi=D_{X}^{B} \chi-\frac{1}{2} \omega(\chi) X+\langle\chi, X\rangle \omega-\tau(X-\langle\chi, X\rangle \chi)+\kappa\langle\chi, X\rangle \xi .$$
Therefore
$$\begin{aligned}
D_{X} \xi \wedge \chi=\frac{1}{2}\langle\chi, X\rangle *(\xi \wedge \omega)-\frac{1}{2} \omega(\chi) *(\xi \wedge X) \\
-\kappa(X-\langle\xi, X\rangle \xi) \wedge \chi-\frac{1}{2}\langle\xi, X\rangle \omega \wedge \chi \\
\xi \wedge D_{X} \chi=\xi \wedge D_{X}^{B} \chi-\frac{1}{2} \omega(\chi) \xi \wedge X+\frac{1}{2}\langle\chi, X\rangle \xi \wedge \omega \\
-\tau \xi \wedge(X-\langle\chi, X\rangle \chi)
\end{aligned}$$
and so
$$\begin{aligned}
\xi \wedge D_{X} \chi-*\left(D_{X} \xi \wedge \chi\right) & =\xi \wedge D_{X}^{B} \chi-\tau \xi \wedge(X-\langle\chi, X\rangle \chi) \\
& +\kappa *((X-\langle\xi, X\rangle \xi) \wedge \chi)+\frac{1}{2}\langle\xi, X\rangle *(\omega \wedge \chi) .
\end{aligned}$$
Since the right hand side is vertical, it follows that $D_{X} J=0$ if and only if
$$\begin{aligned}
D_{X}^{B} \chi-\left\langle D_{X}^{B} \chi, \xi\right\rangle=\tau(X-\langle\chi, X\rangle \chi-\langle\xi, X\rangle \xi) & +\kappa \iota_{X} *_{B} \chi \\
& -\frac{1}{2}\langle\xi, X\rangle *(\xi \wedge \omega \wedge \chi) .
\end{aligned}$$
If $X$ is parallel to $\xi$, this holds automatically since $\mathcal{L}_{K} \chi=0$, and so by considering $X \perp \xi$ we obtain the theorem. \(\square\)

When $M$ is selfdual, this theorem unifies (the local aspects of) LeBrun's treatment of scalar-flat Kähler metrics with symmetry [19], [20] and the hypercomplex structures with symmetry studied by Chave, Tod and Valent [7] and Gauduchon and Tod [12]. To see this, note that since $D$ is canonically determined by $\Omega_{J}$, and $\mathcal{L}_{K} \Omega_{J}=0$, it follows that $\mathcal{L}_{K} D=0$ on $L^{1}$, which means that $d \kappa_{0}=F^{D}(K,$.$) . Since K$ is a conformal vector field, it follows that $\mathcal{L}_{K} D=0$ on $T M$ as well, which gives:
$$\frac{1}{2} d \tau_{0}(X) J+\frac{1}{2} D_{X}\left(d^{D} K\right)^{+}+W_{K, X}-r^{D}(K) \Delta X+r^{D}(X) \Delta K=0 .$$
If we contract this with $J$, we obtain $d \tau_{0}=2 r_{0}^{D}(J K,)=.-i \rho^{D}(K,$.$) . Thus$ $\rho^{D}$ and $F^{D}$ are the selfdual Maxwell fields associated to the monopoles $i \tau$ and $\kappa$ respectively. Since they are selfdual, it follows that $d \kappa_{0}=0$ if and only if $M, J$ is locally scalar-flat Kähler, while $d \tau_{0}=0$ if and only if $M, J$ is locally hypercomplex.
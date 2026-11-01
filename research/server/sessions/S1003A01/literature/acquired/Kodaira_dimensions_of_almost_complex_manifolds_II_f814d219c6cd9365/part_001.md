---
retention_scope: session
part: 1
total_parts: 2
---

[Part 1/2 of: Kodaira dimensions of almost complex manifolds II]

---
source_file: Kodaira_dimensions_of_almost_complex_manifolds_II_b65ea8374f0a.pdf
converter: mathpix
format: mmd
---

\section*{Manuscript version: Author's Accepted Manuscript}

The version presented in WRAP is the author's accepted manuscript and may differ from the published version or Version of Record.

\section*{Persistent WRAP URL:}
http://wrap.warwick.ac.uk/163848

\section*{How to cite:}

Please refer to published version for the most recent bibliographic citation information.

\section*{Copyright and reuse:}

The Warwick Research Archive Portal (WRAP) makes this work by researchers of the University of Warwick available open access under the following conditions.

Copyright © and all moral rights to the version of the paper presented here belong to the individual author(s) and/or other copyright owners. To the extent reasonable and practicable the material made available in WRAP has been checked for eligibility before being made available.

Copies of full items can be used for personal research or study, educational, or not-for-profit purposes without prior permission or charge. Provided that the authors, title and full bibliographic details are credited, a hyperlink and/or URL is given for the original metadata page and the content is not changed in any way.

\section*{Publisher's statement:}

Please refer to the repository item page, publisher's statement section, for further information.

For more information, please contact the WRAP Team at: wrap@warwick.ac.uk.

\title{
KODAIRA DIMENSIONS OF ALMOST COMPLEX MANIFOLDS II
}

\author{
HAOJIE CHEN AND WEIYI ZHANG
}

\begin{abstract}
This is the second of a series of papers where we study the plurigenera, the Kodaira dimension and the Iitaka dimension on compact almost complex manifolds. By using the pseudoholomorphic pluricanonical map, we define the second version of Kodaira dimension as well as Iitaka dimension on compact almost complex manifolds. We show that almost complex structures with the top Kodaira dimension are integrable. For compact almost complex 4-manifolds with Kodaira dimension one, we obtain elliptic fibration like structural description. Some vanishing theorems in complex geometry are generalized to the almost complex setting.
\end{abstract}

For tamed symplectic 4-manifolds, we show that the almost Kodaira dimension is bounded above by the symplectic Kodaira dimension, by using a probabilistic combinatorics style argument. The appendix also contains a few results including answering a question of the second author that there is a unique subvariety in exceptional curve classes for irrational symplectic 4-manifolds, as well as extending Evans-Smith's constraint on symplectic embeddings of certain rational homology balls by removing the assumption on the intersection form.

\section*{Contents}
1. Introduction ..... 2
2. Pluricanonical maps ..... 5
2.1. Pseudoholomorphic subvarieties ..... 6
2.2. Pseudoholomorphic structures ..... 8
2.3. Pluricanonical maps ..... 9
3. Bounding $\kappa^{J}$ by symplectic Kodaira dimension ..... 13
4. Vanishingness of plurigenera ..... 19
5. Further discussion and open problems ..... 21
5.1. Hodge theory ..... 22
5.2. Comparison of Iitaka dimensions ..... 23
5.3. Extension of pseudoholomorphic sections ..... 23
5.4. Examples ..... 24
5.5. Symplectic and almost contact invariants ..... 25
References ..... 25
Appendix A. Uniqueness of exceptional curves for irrational symplectic 4-manifolds ..... 28

\section*{1. Introduction}

The Iitaka dimension for a holomorphic line bundle $L$ over a compact complex manifold is a numerical invariant to measure the size of the space of holomorphic sections. It could be defined as the growth rate of the dimension of the space $H^{0}\left(X, L^{\otimes d}\right)$, or equivalently the maximal image dimension of the rational map to the projective space determined by powers of $L$, or 1 less than the dimension of the section ring of $L$. When $L$ is the canonical bundle $\mathcal{K}_{X}$, the corresponding Iitaka dimension is called the Kodaira dimension of $X$.

In the first paper of this series [5], we have generalized the notions of the Iitaka dimension and Kodaira dimension to compact almost complex manifolds using the growth rate of the pseudoholomorphic sections of the corresponding complex line bundle endowed with a pseudoholomorphic structure, or equivalently, a bundle almost complex structure.

More precisely, let $E$ be a complex vector bundle over a connected compact almost complex manifold $(X, J)$. A bundle almost complex structure $\mathcal{J}$ on $E$ is a special almost complex structure on the total space of the $E$, see [5, 6]. There is a bijection between bundle almost complex structures and the pseudoholomorphic structures on $E$. The $(E, \mathcal{J})$-genus is defined as $P_{E, \mathcal{J}}:=\operatorname{dim} H^{0}(X,(E, \mathcal{J}))$, where $H^{0}(X,(E, \mathcal{J}))$ denotes the space of $(J, \mathcal{J})$ pseudoholomorphic sections. As shown by Hodge theory in [5], $P_{E, \mathcal{J}}$ is of finite dimension. The $m^{\text {th }}$ plurigenus of $(X, J)$ is defined to be $P_{m}(X, J)=\operatorname{dim} H^{0}\left(X, \mathcal{K}_{X}^{\otimes m}\right)$ where $\mathcal{K}_{X}^{\otimes m}$ is endowed with a canonical bundle almost complex structure induced from $J$ (see Section 2.2 or [5]).

Definition 1.1. Let $L$ be a complex line bundle with a bundle almost complex structure $\mathcal{J}$ over $(X, J)$. The Iitaka dimension $\kappa^{J}(X,(L, \mathcal{J}))$ is defined as
$$\kappa^{J}(X,(L, \mathcal{J}))=\left\{\begin{array}{cl}
-\infty, & \text { if } P_{L^{\otimes m}, \mathcal{J}}=0 \text { for any } m \geq 0 \\
\limsup _{m \rightarrow \infty} \frac{\log P_{L^{\otimes m}, \mathcal{J}}}{\log m}, & \text { otherwise. }
\end{array}\right.$$

The Kodaira dimension $\kappa^{J}(X)$ is defined by choosing $L=\mathcal{K}_{X}$ and $\mathcal{J}$ to be the bundle almost complex structure induced by $\bar{\partial}$.

In this paper, we will introduce the second version of the Iitaka dimension and Kodaira dimension on compact almost complex manifolds which is the maximal image dimension of the rational map to th projective space by holomormphic sections of $L^{\otimes m}$. In the complex setting, important structural results and speculations were obtained using this interpretation.

Assume that $L$ is a complex line bundle over a compact almost complex manifold $(X, J)$ with a bundle almost complex structure $\mathcal{J}$. As in complex setting, the map $\Phi_{L, \mathcal{J}}: X \backslash B \rightarrow \mathbb{C} P^{N}$ is defined as $\Phi_{L, \mathcal{J}}(x)=\left[s_{0}(x): \cdots: s_{N}(x)\right]$, where $\left\{s_{i}\right\}$ constitutes a basis of the linear space $H^{0}(X,(L, \mathcal{J}))$, and $B \subset X$ is the set of the base locus, i.e. the set of points $x \in X$ such that $s_{i}(x)=0$ for all $0 \leq i \leq N$. When $L$ is $\mathcal{K}_{X}^{\otimes m}$ with the standard bundle almost complex structure, $\Phi_{L, \mathcal{J}}$ is denoted by $\Phi_{m}$ and called the pluricanonical map.

We first show that $\Phi_{L, \mathcal{J}}$ is pseudoholomorphic between $X \backslash B$ and the standard projective space. Following the study of pseudoholomorphic maps from an almost complex manifolds to a complex manifold, we prove that the image of $\Phi_{L, \mathcal{J}}(X \backslash B)$ is a locally closed but not necessarily closed analytic subvariety in $\mathbb{C} P^{N}$. As a result, we define

Definition 1.2. The Iitaka dimension $\kappa_{J}(X,(L, \mathcal{J}))$ of a complex line bundle $L$ with a bundle almost complex structure $\mathcal{J}$ over $(X, J)$ is defined as
$$\kappa_{J}(X,(L, \mathcal{J}))=\left\{\begin{array}{cl}
-\infty, & \text { if } P_{L^{\otimes m}}=0 \text { for any } m \geq 0 \\
\max \operatorname{dim}_{\mathbb{C}} \Phi_{L^{\otimes m}}(X \backslash B), & \text { otherwise. }
\end{array}\right.$$

The Kodaira dimension $\kappa_{J}(X)$ is defined by choosing $L=\mathcal{K}_{X}$ and $\mathcal{J}$ to be the bundle almost complex structure induced by $J$.

It is a natural question (Question 2.8) to ask whether the two versions of Iitaka dimensions $\kappa^{J}$ and $\kappa_{J}$ are equivalent.

We have shown that the plurigenera $P_{m}(X, J)$ are birational invariants on compact almost complex 4-manifolds in [5]. It follows that $\kappa_{J}(X)$ is also a birational invariant in dimension 4 (Theorem 2.6).

We then apply the Kodaira dimension $\kappa_{J}(X)$ to study the properties of $(X, J)$. By definition, $\kappa_{J}(X,(L, \mathcal{J})) \leq \operatorname{dim}_{\mathbb{C}} X$. When the top value $\operatorname{dim}_{\mathbb{C}} X$ is achieved, we prove that $J$ is integrable. The following is Theorem 2.4.
Theorem 1.3. Let $(X, J)$ be a compact almost complex manifold and $L$ be a complex line bundle with a bundle almost complex structure $\mathcal{J}$.
\begin{itemize}
\item[(1)] If $\kappa_{J}(X,(L, \mathcal{J}))=\operatorname{dim}_{\mathbb{C}} X$, then $J$ is integrable.
\item[(2)] If $P_{L, \mathcal{J}} \geq 2$, then $\kappa_{J}(X,(L, \mathcal{J})) \geq 1$.
\end{itemize}

Although a non-integrable almost complex structure cannot have $\kappa_{J}$ being equal to its complex dimension, the examples of compact $2 n$-dimensional nonintegrable almost complex manifolds in Section 6.3 of our first paper [5] realize all the values of $\{-\infty, 0,1, \cdots, n-1\}$ for $\kappa_{J}(X)$ (as well as $\kappa^{J}(X)$ ) for any $n \geq 2$. The examples are based on a 4-dimensional example with Kodaira dimension 1, which is a deformation of the product complex structure on $T^{2} \times \Sigma_{g \geq 2}$.

For almost complex manifolds with line bundles whose almost complex Iitaka dimensions take value between 1 and $n-1$, we expect that there are important structural result of $X$. The following is such a result (Theorem 2.7).
Theorem 1.4. Let $(X, J)$ be a compact almost complex 4-manifold. If the pluricanonical map is base-point-free and $\kappa_{J}(X)=1$, then $X$ admits a pseudoholomorphic fibration with each fiber an elliptic curve and finitely many singular fibers.

The examples of almost complex 4 -manifolds with $\kappa^{J}=\kappa_{J}=1$ contain all the smooth pseudoholomorphic elliptic fibrations over a Riemann surface of genus greater than one with tamed almost complex structures.

In dimension 4, there is a version of symplectic Kodaira dimension $\kappa^{s}$ [18], which measures the positivity of the symplectic canonical class (see Definition 3.3). This

Kodaira dimension is a diffeomorphism invariant of any symplectic 4-manifold loc. cit., and it coincides with the complex Kodaira dimension if the symplectic 4-manifold admits a complex structure [7]. The invariant provides a rough classification scheme for symplectic 4-manifolds [18]. It is studied extensively in 4-manifolds theory, e.g. its behaviour under various symplectic surgeries like fiber sum, Luttinger surgery, and rational blowdown (see the references in [19]). It is also used to show some smooth structures are exotic.

It is natural to ask the connection between the almost complex Kodaira dimensions and the symplectic Kodaira dimension in dimension 4. We are able to bound the Kodaira dimension $\kappa^{J}(X)$ from above by $\kappa^{s}$ at least when the almost complex structure $J$ is tamed. Recall that an almost complex structure $J$ is said to be tamed if there is a symplectic form $\omega$ such that the bilinear form $\omega(\cdot, J \cdot)$ is positive definite. To establish this result, we introduce an intermediate Iitaka dimension $\kappa_{W}^{J}(X, e)$ for tamed almost complex structure $J$ and $e \in H^{2}(M, \mathbb{Z})$. The Weil divisor version of Kodaira dimension is defined as $\kappa_{W}^{J}(X):=\kappa_{W}^{J}\left(X, K_{X}\right)$, where $K_{X}$ is the first Chern class of $\mathcal{K}_{X}$. Roughly speaking, this version of Iitaka dimension measures the growth rate of the numbers of all pseudoholomorphic curves in the multiples of the class $e$. Among various estimates of this Iitaka dimensions in Section 3, we have the following comparison results for Kodaira dimensions.
Theorem 1.5. Let $(X, J)$ be a tamed compact almost complex 4-manifold. Then
$$\kappa^{J}(X) \leq \kappa_{W}^{J}(X) \leq \kappa^{s}(X) .$$

As a corollary (Corollary 3.7), for any tamed almost complex structure $J$ on a compact complex surface $\left(X, J_{X}\right), \kappa^{J}(X) \leq \kappa^{J_{X}}(X)$.

Theorem 1.5 is obtained through estimations of pseudoholomorphic curves in multiples of the canonical class using a very rough and "overdetermined" parametrization of the moduli space of pseudoholomorphic subvarieties in class $m K_{X}$. These points given by the parametrization fix a unique element in the moduli space and, at the same time, the number of the points as $m$ grows is bounded above by a polynomial whose degree matches up with symplectic Kodaira dimension. This is very similar to the style of estimates in probabilistic combinatorics.

We next study how the positivity of line bundles is related to the almost complex Iitaka dimension. The relation between positivity/negativity of certain curvatures and vanishing of groups of holomorphic sections has been an active topic in complex geometry, at least dating back to Kodaira vanishing theorem. A negative line bundle on a compact complex manifold, i.e. a holomorphic line bundle whose first Chern class is a negative class, always has negative Iitaka dimension. Applying the intersection theory of almost complex manifolds developed in [41] and some Bochner-type arguments on almost Hermitian manifolds, we prove the following theorem.
Theorem 1.6. Let $(X, J)$ be a compact almost complex $2 n$-manifold and $L$ be a complex line bundle over $X$.
\begin{itemize}
\item[(1)] If there is a $J$-compatible symplectic form $\omega$ such that $[\omega]^{n-1} \cdot c_{1}(L)<$ 0 , then for any bundle almost complex structure $\mathcal{J}$ on $L, P_{L, \mathcal{J}}=0$ and $\kappa^{J}(X,(L, \mathcal{J}))=\kappa_{J}(X,(L, \mathcal{J}))=-\infty$.
\end{itemize}
\begin{itemize}
\item[(2)] If $X$ admits a Hermitian metric with positive Chern scalar curvature everywhere or a Gauduchon metric with positive total Chern scalar curvature, then $\kappa^{J}(X)=\kappa_{J}(X)=-\infty$.
\end{itemize}

It gives a generalization of results obtained by Yau in the Kähler case [37] and by Yang in the Hermitian case [36]. Theorem 1.6 is proved by combining Theorems 4.2 and 4.3 later.

The last section of the paper contains some speculations and open problems generated from the study of almost complex Iitaka dimensions. It is divided into 5 subsections on different aspects. It seems that our paper is just a start of a vast area with a rich source of interesting problems for almost complex manifolds. It is related to many other fields such as Hodge theory, birational geometry, complex geometry, and topology of manifolds. We expect Section 5 would provide the reader with a glance of these interesting problems.

Finally, there is an appendix on the uniqueness of exceptional curves for irrational symplectic 4-manifolds. Its main result gives an affirmative answer to a question of the second author [39].

Theorem 1.7. Let $M$ be a compact symplectic 4-manifold which is not diffeomorphic to $\mathbb{C} P^{2} \# k \overline{\mathbb{C} P^{2}}, k \geq 1$. Then for any tamed $J$, there is a unique $J$ -holomorphic subvariety in any exceptional curve class $E$, whose irreducible components are smooth rational curves of negative self-intersection. Moreover, this $J$ -holomorphic subvariety is an exceptional curve of the first kind when $M$ is also not diffeomorphic to $S^{2} \times \Sigma_{g} \# k \overline{\mathbb{C} P^{2}}$.

On the other hand, as noticed in [39, 40 ] as a somewhat surprising result, there are many integrable complex structures on rational surfaces where this statement does not hold. The link of the appendix with this paper is through Proposition A.5, which says that there is a unique $J$-holomorphic subvariety in any positive combination of exceptional curve classes for any tamed almost complex structure $J$ on a symplectic 4-manifold which is not diffeomorphic to a rational or ruled surface. It is used in the proof of Theorem 1.5 when the symplectic Kodaira dimension is zero.

As a by-product of the proof of Theorem 1.7, we are able to improve the result of [9] on the symplectic version of the upper bound of Wahl singularities by removing their assumption on the dimension of self-dual harmonic forms.

The first author is partially supported by NSFC grant (11901530) and Zhejiang Provincial Natural Science Foundation (LY19A010017). He would like to thank Professors Kefeng Liu, Xiaokui Yang and Fangyang Zheng for their helpful conversations. The second author would like to thank Giancarlo Urzúa for his interest and discussion on Theorem A.3.

\section*{2. Pluricanonical maps}

In this section, we will give another definition of Iitaka dimension for almost complex manifolds. The corresponding version of Kodaira dimension is the maximum dimension of the image attained by a pluricanonical map. For this sake, we first
derive some general properties of the image of a pseudoholomorphic map onto a complex manifold in Section 2.1. These are used to establish structural results for pluricanonical maps.
2.1. Pseudoholomorphic subvarieties. In [41], we give a definition of pseudoholomorphic subvarieties for an arbitrary even dimension. A $J$-holomorphic subvariety $\Theta$ of an almost complex manifold $(M, J)$ is a finite set of pairs $\left\{\left(V_{i}, m_{i}\right), 1 \leq\right.$ $i \leq m\}$, where each $V_{i}$ is an irreducible $J$-holomorphic subvariety and each $m_{i}$ is a positive integer. Here an irreducible $J$-holomorphic subvariety is the image of a somewhere immersed pseudoholomorphic map $\phi: X \rightarrow M$ from a compact connected smooth almost complex manifold $X$. When each $V_{i}$ has complex dimension one, we call $\Theta$ a complex 1-subvariety.

When $(M, J)$ is a complex manifold, the source $\left(X, J_{X}\right)$ could still be an almost complex manifold. Hence, it seems there are more $J$-holomorphic subvarieties than complex analytic subvarieties at a first glance. However, we observe that when $(M, J)$ is a complex manifold, a $J$-holomorphic subvariety is exactly a complex analytic subvariety.

Proposition 2.1. If there is a somewhere immersed pseudoholomorphic map $\phi$ : $X \rightarrow M$ from a compact connected smooth almost complex manifold $\left(X, J_{X}\right)$ to a complex manifold $(M, J)$, then $J_{X}$ is integrable. Therefore, a finite set of pairs $\left\{\left(V_{i}, m_{i}\right), 1 \leq i \leq m\right\}$ on $(M, J)$ is a $J$-holomorphic subvariety if and only if it is a complex analytic subvariety.

Proof. We will use a similar method as for Theorem 5.5 of [41]. However, since $\operatorname{dim} X$ might be different from $\operatorname{dim} M$, we will need to do extra projections. We can cover $M$ by complex coordinate patches. Hence, we can assume our target is an open subset $U \subset \mathbb{C}^{n}$, with coordinates $\left(z_{1}, \cdots, z_{n}\right)$. Since $\phi$ is somewhere immersed, we have $\operatorname{dim}_{\mathbb{C}} X=m \leq n$. Let $\left\{\sigma_{1}, \cdots, \sigma_{m}\right\}$ be a choice of $m$ elements in $\{1, \cdots, n\}$. Denote the image of projecting $U$ to the subspace spanned by $z_{\sigma_{1}}, \ldots z_{\sigma_{m}}$ coordinates by $U_{\sigma_{1}, \cdots, \sigma_{m}}$ or simply $U_{\mathbb{C}^{m}}$ if there is no confusion. Also denote the projection of $\left.\phi\right|_{X_{U}}$ to $\mathbb{C}_{z_{\sigma_{1}}, \cdots, z_{\sigma_{m}}}^{m}$ components by $p r_{\sigma_{1} \cdots \sigma_{m}} \phi$.

For each such choice of $\left\{\sigma_{1}, \cdots, \sigma_{m}\right\}$, we look at the projection from $\mathbb{C}^{n}$ to $m$ coordinates $\left(z_{\sigma_{1}}, \cdots, z_{\sigma_{m}}\right)$. This gives us a complex vector bundle over $X_{U} \times U_{\mathbb{C}^{m}}$ whose fiber over $\left(x, p r_{\sigma_{1} \cdots \sigma_{m}} \phi(x)\right)$ is the complex vector space of all complex linear maps $L_{\sigma_{1} \cdots \sigma_{m}}: T_{x} X \rightarrow \mathbb{C}^{m}$. Here $X_{U}$ is the set $\phi^{-1}(U) \subset X$. By taking fiberwise complex determinant, we have a complex line bundle $\mathcal{L}_{\sigma_{1} \cdots \sigma_{m}}$ over $X_{U} \times U_{\mathbb{C}^{m}}$, whose fibers are $\operatorname{det} L_{\sigma_{1} \cdots \sigma_{m}}: \Lambda_{\mathbb{C}}^{m} T_{x} X \rightarrow \Lambda_{\mathbb{C}}^{m} \mathbb{C}^{m} \cong \mathbb{C}$. Its total space has a standard almost complex structure, see the proof of Theorem 5.5 in [41].

Then the pseudoholomorphic map $\phi$ induces pseudoholomorphic maps $\phi_{\mathcal{L}_{\sigma_{1} \cdots \sigma_{m}}}(x)=$ $\left(x, \phi(x), \operatorname{det}\left(d\left(p r_{\sigma_{1} \cdots \sigma_{m}} \phi\right)_{x}\right)_{\mathbb{C}}\right)$ from $X_{U}$ to $\mathcal{L}_{\sigma_{1} \cdots \sigma_{m}}$. Hence, the singularity subset of $\phi$ (in $X_{U}$ ) is the intersection of $\phi_{\mathcal{L}_{\sigma_{1} \cdots \sigma_{m}}}^{-1}\left(X_{U} \times U_{\mathbb{C}^{m}} \times\{0\}\right)$ for all possible subsets $\left\{\sigma_{1}, \cdots, \sigma_{m}\right\}$. Applying Theorem 3.8 of [41], we know each $\phi_{\mathcal{L}_{\sigma_{1} \cdots \sigma_{m}}}^{-1}\left(X_{U} \times U_{\mathbb{C}^{m}} \times\{0\}\right)$ is a subset with finite $2(m-1)$-dimensional Hausdorff measure if it is not the whole $X_{U}$. Since $\phi$ is somewhere immersed and $X$ is connected, there must be $\left\{\sigma_{1}, \cdots, \sigma_{m}\right\}$
such that $\phi_{\mathcal{L}_{\sigma_{1} \cdots \sigma_{m}}}^{-1}\left(X_{U} \times U_{\mathbb{C}^{m}} \times\{0\}\right)$ is not the whole $X_{U}$ (but possibly it is empty). It implies the singular subset $\mathcal{S}_{\phi}$ has finite $2(m-1)$-dimensional Hausdorff measure. In particular, the closure of $X \backslash \mathcal{S}_{\phi}$ is $X$.

On $X \backslash \mathcal{S}_{\phi}$, the map $\phi$ is an immersion. In particular, it is local diffeomorphic to its image and thus the complex coordinates of $(M, J)$ could be pulled back by $\phi$. It implies the Nijenhuis tensor $\left.N_{J_{X}}\right|_{X \backslash \mathcal{S}_{\phi}}=0$. Since the closure of $X \backslash \mathcal{S}_{\phi}$ is $X$, we know $N_{J_{X}}=0$. That is $J_{X}$ is integrable.

The second statement follows from a theorem of Remmert [26] which says that the image of a proper holomorphic map between two complex manifolds is a complex analytic subvariety of the target. Hence, it implies that if $\left\{\left(V_{i}, m_{i}\right), 1 \leq i \leq m\right\}$ on $(M, J)$ is a $J$-holomorphic subvariety, then it is a complex analytic subvariety. The reverse direction follows from Hironaka's resolution of singularities. This completes the proof of the lemma. \(\square\)

This proof also shows that the image of the singularity subset $\phi\left(\mathcal{S}_{\phi}\right)$ is a complex analytic subvariety assuming a positive answer to Question 3.9 of [41], and thus a $J$-holomorphic subvariety of $M$. When $\phi$ is a general proper pseudoholomorphic map, we can still have a similar conclusion as Proposition 2.1, although we only have a less precise description of the image of the singularity subset.

Proposition 2.2. Let $\phi: X \rightarrow M$ be a proper pseudoholomorphic map from a closed almost complex manifold $\left(X, J_{X}\right)$ to a complex manifold $(M, J)$. Then the image of $\phi$ is a complex analytic subvariety.

Proof. We look at the differential of $d \phi: T X \rightarrow T M$ and view it as a linear transformation at each point of $X$. Since $\phi$ is a pseudoholomorphic map, the rank of this linear transformation at each point is an even integer no greater than $\min \left\{2 \operatorname{dim}_{\mathbb{C}} X, 2 \operatorname{dim}_{\mathbb{C}} M\right\}$. Define the rank of $\phi$ by $\operatorname{rk}(\phi)=\frac{1}{2} \sup _{x \in X} \operatorname{rk}\left(d \phi_{x}\right)$. We call any point $x \in X$ with $\operatorname{rk}(\phi)=\frac{1}{2} \operatorname{rk}\left(d \phi_{x}\right)$ a regular point and any other point a critical point.

We apply a result of Sard 27: If $f: N_{1} \rightarrow N_{2}$ is a $C^{k}$ map for $k \geq \max \{n-m+$ $1,1\}$ and if $A_{r} \subset N_{1}$ is the set of points $x \in N_{1}$ such that $d f_{x}$ has rank no greater than $r$, then the $(r+\epsilon)$-dimensional Hausdorff measure of $\phi\left(A_{r}\right)$ is zero, for any $\epsilon>0$.

In our setting, we choose $r=2 \operatorname{rk}(\phi)-2$. Thus $A_{r}$ is the set of critical points. In particular, the above version of Sard's theorem implies that the Hausdorff measure $\mathcal{H}^{2 \operatorname{rk}(\phi)-1}\left(\phi\left(A_{r}\right)\right)=0$.

On the other hand, the set of regular points is an open dense subset in $X$. The openness is apparent and the denseness means $\overline{X \backslash A_{r}}=X$. To show the denseness, we look at the $\operatorname{rk}(\phi)^{\text {th }}$ wedge product of both the complex vector bundles $T X$ and $T M$, denoted by $\Lambda_{\mathbb{C}}^{\mathrm{rk}(\phi)} T X$ and $\Lambda_{\mathbb{C}}^{\mathrm{rk}(\phi)} T M$. Then the 1-jet bundle $\mathcal{E}=J^{1}(X, M)$ induces a complex vector bundle $\mathcal{E}^{\mathrm{rk}(\phi)}$ (over $X \times M$ ) whose fibers are induced complex linear maps from $\Lambda_{\mathbb{C}}^{\mathrm{rk}(\phi)} T_{x} X$ to $\Lambda_{\mathbb{C}}^{\mathrm{rk}(\phi)} T_{\phi(x)} M$. Its total space inherits a standard almost complex structure from the standard almost complex structure $\mathcal{J}$ of $J^{1}(X, M)$. The pseudoholomorphic map $\phi$ induces a pseudoholomorphic section
$\left(x, \phi(x),\left(d \phi_{x}\right)_{\mathbb{C}}\right)$ of $J^{1}(X, M)$ and in turn a pseudoholomorphic section of $\mathcal{E}^{\mathrm{rk}(\phi)}$. The zero locus of this section is just $A_{r}$. By the extension of unique continuation for pseudoholomorphic submanifolds, i.e. Proposition 2.3 of [41], we know $A_{r}$ cannot contain an open subset of $X$ since it is the intersection of two almost complex submanifolds, i.e. the image of the zero section and the induced section $\left(x, \phi(x), \Lambda_{\mathbb{C}}^{\mathrm{rk}(\phi)}\left(d \phi_{x}\right)_{\mathbb{C}}\right)$. Since $X$ is a manifold, we have $\overline{X \backslash A_{r}}=X$.

Applying the rank theorem (see e.g. [17]), we know the image of an open neighborhood of $x \in X \backslash A_{r}$ is diffeomorphic to $\mathbb{R}^{2 \operatorname{rk}(\phi)}=\mathbb{R}^{r+2}$. Since $\phi$ is pseudoholomorphic, the image of the open neighborhood is an (almost) complex submanifold of $M$. Hence, it is $\mathbb{C}^{\mathrm{rk}(\phi)}$. In particular, the image $\phi\left(X \backslash A_{r}\right)$ is a complex analytic variety. Then Lemma 2.2 follows from a theorem of Shiffman [28] (see also [16]) by taking $k=\operatorname{rk}(\phi)$.

Theorem 2.3 (Shiffman). Let $U$ be open in $\mathbb{C}^{n}$ and let $E$ be closed in $U$. Let $X$ be a pure $k$-dimensional complex analytic subvariety in $U \backslash E$, and let $\bar{X}$ be the closure of $X$ in $U$. If $\mathcal{H}^{2 k-1}(E)=0$ then $\bar{X}$ is a pure $k$-dimensional complex analytic subvariety in $U$. \(\square\)

If we study a rational map from a closed almost complex manifold $\left(X, J_{X}\right)$ to a complex manifold $(M, J)$, i.e. a proper pseudoholomorphic map $\phi: X \backslash B \rightarrow Y$ where $B$ has Hausdorff codimension at least two, we know the image $\phi(X \backslash B)$ has the structure of analytic subvariety locally near any point in the image following from the argument of Proposition 2.2. By abuse of notation, we call the image an open analytic subvariety.
2.2. Pseudoholomorphic structures. In this subsection, we recall the one-toone correspondence of pseudoholomorphic structures and bundle almost complex structures on a complex vector bundle $E$ over the almost complex manifold $(X, J)$ as established in [5,6].

A pseudoholomorphic structure on $E$ is given by a differential operator $\bar{\partial}_{E}$ : $\Gamma(X, E) \rightarrow \Gamma\left(X,\left(T^{*} X\right)^{0,1} \otimes E\right)$ which satisfies the Leibniz rule
$$\bar{\partial}_{E}(f s)=\bar{\partial} f \otimes s+f \bar{\partial}_{E} s$$
where $f$ is a smooth function and $s$ is a section of $E$. A particularly important pseudoholomorphic structure is the natural one $\bar{\partial}_{m}: \Gamma\left(X, \mathcal{K}_{X}^{\otimes m}\right) \rightarrow\left(T^{*} X\right)^{0,1} \otimes$ $\Gamma\left(X, \mathcal{K}_{X}^{\otimes m}\right)$ for $m \geq 2$ on the pluricanonical bundle $\mathcal{K}_{X}^{\otimes m}$ induced from the $\bar{\partial}$ operator inductively by the product rule
$$\bar{\partial}_{m}\left(s_{1} \otimes s_{2}\right)=\bar{\partial} s_{1} \otimes s_{2}+s_{1} \otimes \bar{\partial}_{m-1} s_{2} .$$

For any Hermitian bundle $\left(E, h_{E}\right)$ with a pseudoholomorphic structure $\bar{\partial}_{E}$, there is a unique Hermitian connection ∇ so that its (0, 1)-component $\nabla^{(0,1)}=\bar{\partial}_{E}$ (see Lemma 3.3 in [5]).

We can define a unique dual pseudoholomorphic structure $\bar{\partial}_{E^{*}}: \Gamma\left(X, E^{*}\right) \rightarrow$ $\Gamma\left(X,\left(T^{*} X\right)^{0,1} \otimes E^{*}\right)$ on the dual bundle $E^{*}$ : for any section $s^{*} \in \Gamma\left(X, E^{*}\right)$ and any
section $s^{\prime} \in \Gamma(X, E)$, let
$$\left(\bar{\partial}_{E^{*}}\left(s^{*}\right)\right)\left(s^{\prime}\right)=\bar{\partial}\left(s^{*}\left(s^{\prime}\right)\right)-s^{*}\left(\bar{\partial}_{E}\left(s^{\prime}\right)\right) .$$
It is easy to verify that $\bar{\partial}_{E^{*}}$ satisfies the Leibniz rule, giving a pseudoholomorphic structure.

On the other hand, a bundle almost complex structure as in [6] is an almost complex structure $\mathcal{J}$ on $T E$ so that
\begin{itemize}
\item[(i)] the projection is $(\mathcal{J}, J)$-holomorphic,
\item[(ii)] $\mathcal{J}$ induces the standard complex structure on each fiber, i.e. multiplying by $i$,
\item[(iii)] the fiberwise addition $\alpha: E \times_{M} E \rightarrow E$ and the fiberwise multiplication by a complex number $\mu: \mathbb{C} \times E \rightarrow E$ are both pseudoholomorphic.
\end{itemize}

It is shown in 6 that a bundle almost complex structure $\mathcal{J}$ on $E$ determines a pseudoholomorphic structure $\bar{\partial}_{\mathcal{J}}$, and the map $\mathcal{J} \mapsto \bar{\partial}_{\mathcal{J}}$ is a bijection between the spaces of bundle almost complex structures and pseudoholomorphic structures on $E$. Furthermore, it is shown as Corollary 2.4 in [5] that $\bar{\partial}_{\mathcal{J}} s=0$ if and only if $s$ is $(J, \mathcal{J})$ holomorphic for any $s \in \Gamma(X, E)$. We denote this space of pseudoholomorphic sections by $H^{0}(X,(E, \mathcal{J}))$. In particular, the space of pseudoholomorphic sections of $\left(\mathcal{K}_{X}^{\otimes m}, \bar{\partial}_{m}\right)$ is denoted by $H^{0}\left(X, \mathcal{K}_{X}^{\otimes m}\right)$.

These two equivalent ways of description of a pseudoholomorphic section have their respective use. The PDE description was used to show the dimension of pseudoholomorphic sections is finite, while the geometric description bridges to the intersection theory of almost complex submanifolds [41]. In particular, when $E$ is a complex line bundle over 4-manifold $(X, J)$, the zero locus of a pseudoholomorphic section $s$ is a $J$-holomorphic 1-subvariety in class $c_{1}(E)$.
2.3. Pluricanonical maps. One can still define pluricanonical maps for a compact almost complex manifold $(X, J)$. More generally, for any complex line bundle $L$ with a bundle almost complex structure $\mathcal{J}, \Phi_{L, \mathcal{J}}: X \rightarrow \mathbb{C} P^{N}$ is defined as $\Phi_{L, \mathcal{J}}(x)=$ $\left[s_{0}(x): \cdots: s_{N}(x)\right]$, where $\left\{s_{i}\right\}$ constitutes a basis of the linear space $H^{0}(X,(L, \mathcal{J}))$. When $L=\mathcal{K}_{X}^{\otimes m}$ and $\mathcal{J}=\mathcal{J}_{J}$ induced by $\bar{\partial}_{m}, \Phi_{L, \mathcal{J}}$ is denoted by $\Phi_{m}$ and called the pluricanonical map. This map is well defined because the transition map for a complex line bundle takes value in GL(1, C). Hence, changing the local coordinates would lead to a common multiple of all $s_{i}$.

Furthermore, $\Phi_{L, \mathcal{J}}$ is a pseudoholomorphic map from $(X, J)$ to $\left(\mathbb{C} P^{N}, J_{\text {std }}\right)$. It can be seen from each map $\Phi_{L, \mathcal{J}}^{i j}(x)=\frac{s_{j}}{s_{i}}(x)$. Each $\Phi_{L, \mathcal{J}}^{i j}$ is a section of the trivial bundle over $X \backslash\left\{s_{i}^{-1}(0)\right\}$. The map $\frac{1}{s_{i}(x)}$ is a pseudoholomorphic section of the dual bundle $L^{*}$ over $X \backslash\left\{s_{i}^{-1}(0)\right\}$ with respect to the pseudoholomorphic structure on $L^{*}$ dual to $\bar{\partial}_{\mathcal{J}}$, by applying (1) to the relation $1=s_{i} \cdot \frac{1}{s_{i}}$. By applying (1) again, we deduce that $\Phi_{L, \mathcal{J}}^{i j}$ is a pseudoholomorphic section of the trivial bundle over $X \backslash\left\{s_{i}^{-1}(0)\right\}$. Hence, it implies that $\Phi_{L, \mathcal{J}}: X \backslash B \rightarrow \mathbb{C} P^{N}$ is a pseudoholomorphic map. Here $B \subset X$ is the set of the base locus, i.e. the set of points $x \in X$ such that $s_{i}(x)=0$ for all $0 \leq i \leq N$.

We are able to use the image $\Phi_{L}(X \backslash B)$, in particular its dimension, to study the almost complex manifold $(X, J)$. By the argument of Proposition 2.2, we know the image is an open analytic subvariety. Clearly, $\operatorname{dim}_{\mathbb{C}} \Phi_{L}(X \backslash B) \leq \operatorname{dim}_{\mathbb{C}} X$. Moreover, we have the following.

Theorem 2.4. Let $(X, J)$ be a compact almost complex manifold and $L$ be a complex line bundle with a bundle almost complex structure. If $\operatorname{dim}_{\mathbb{C}} \Phi_{L}(X \backslash B)=\operatorname{dim}_{\mathbb{C}} X$, then $J$ is integrable. If $P_{L}(X, J)=\operatorname{dim} H^{0}(X,(L, \mathcal{J})) \geq 2$, then $\operatorname{dim}_{\mathbb{C}} \Phi_{L}(X \backslash B) \geq$ 1.

Proof. If $\Phi_{L}(X \backslash B)$ is the set of finitely many points, then we know that for any two pseudoholomorphic sections $s_{1}, s_{2}$ of $L$, we have $s_{2}-k s_{1}=0$ in an open subset of $X$ for some constant $k$. However, it implies $s_{2}-k s_{1} \equiv 0$ by Proposition 2.3 of [41]. Hence if $P_{L}(X, J) \geq 2$, the image has $\operatorname{dim}_{\mathbb{C}} \Phi_{L}(X \backslash B) \geq 1$.

When $\operatorname{dim}_{\mathbb{C}} \Phi_{L}(X \backslash B) \geq 1$, by the unique continuation for pseudoholomorphic submanifolds, Proposition 2.3 of [41], both the base locus $B$ and the singularity subset of $\Phi_{L}$ cannot contain an open subset of $X$. Moreover, since the singularities of the image $\Phi_{L}(X \backslash B)$ has complex codimension at least 1 in $\Phi_{L}(X \backslash B)$, its preimage also does not contain an open subset of $X$. We now look at the complement of these subsets of $X$, which is called the regular part $X_{\text {reg }}$ by abuse of terminology.

When $\operatorname{dim}_{\mathbb{C}} \Phi_{L}(X \backslash B)=2$, we know the pseudoholomorphic map $\Phi_{L}$ maps $X_{\text {reg }}$ diffeomorphically to its image. Hence $\left.J\right|_{X_{\text {reg }}}$ is integrable, which in turn implies $J$ is integrable on whole $X$ since $X=\overline{X_{\text {reg }}}$. \(\square\)

As a result, we can define another version of Iitaka dimension for almost complex manifolds.

Definition 2.5. The Iitaka dimension $\kappa_{J}(X,(L, \mathcal{J}))$ of a complex line bundle $L$ with a bundle almost complex structure $\mathcal{J}$ over $(X, J)$ is defined as
$$\kappa_{J}(X,(L, \mathcal{J}))=\left\{\begin{array}{cl}
-\infty, & \text { if } P_{L^{\otimes m}}=0 \text { for any } m \geq 0 \\
\max \operatorname{dim} \Phi_{L^{\otimes m}}\left(X \backslash B_{m, L, \mathcal{J}}\right), & \text { otherwise. }
\end{array}\right.$$

The Kodaira dimension $\kappa_{J}(X)$ is defined by choosing $L=\mathcal{K}_{X}$ and $\mathcal{J}$ to be the bundle almost complex structure induced by $J$.

In Theorem 5.3 of [5], we have proved that there is a one-to-one correspondence between elements of $H^{0}\left(X, \mathcal{K}_{X}^{\otimes m}\right)$ and $H^{0}\left(Y, \mathcal{K}_{Y}^{\otimes m}\right)$ when there is a pseudoholomorphic degree one map between closed almost complex 4-manifolds $(X, J)$ and $\left(Y, J_{Y}\right)$. Moreover, these elements coincide at an open subset of each $X$ and $Y$ whose complements are proper subvarieties of $X$ and $Y$ respectively. Hence, it follows that $\kappa_{J}(X)$ is a birational invariant.

Theorem 2.6. Let $u:(X, J) \rightarrow\left(Y, J_{Y}\right)$ be a degree one pseudoholomorphic map between closed almost complex 4-manifolds. Then $\kappa_{J}(X)=\kappa_{J_{Y}}(Y)$.

It essentially follows from Theorem 6.10 in [5] that all the values $\{-\infty, 0,1, \cdots, n-$ $1\}$ could be realized by $\kappa_{J}(X)$ when ( $X, J$ ) is non-integrable. It is clear for values
$-\infty$ and 0 . For examples with $\kappa_{J} \geq 1$, we look at the non-integrable almost complex structures on $T^{2} \times S$ in Section 6.3 of [5]. By Lemma 6.5 in [5], the pluricanonical maps are base-point-free and have the same image as that of a Riemann surface $S$ with $g \geq 2$. In particular, it has dimension 1. By taking product of this $T^{2} \times S$ with other Riemann surfaces $T^{2}$ and $\Sigma_{g}$, we know the image of pluricanonical map is the product of Riemann surfaces by the Künneth formula, Proposition 6.8 in [5]. This gives us all the possible values of $\kappa_{J}$.

Below is a structural result for almost complex 4-manifolds with $\kappa_{J}=1$. It shows that these manifolds are in fact generalizations of elliptic surfaces.

Theorem 2.7. Let $(X, J)$ be a compact almost complex 4-manifold admitting a basepoint-free pluricanonical map. If $\kappa_{J}(X)=1$, then $X$ admits a pseudoholomorphic fibration with each fiber an elliptic curve and finitely many singular fibers.

Proof. Let $\Phi_{m}$ be the base-point-free pluricanonical map. Then by Proposition 2.2, the image $\Phi_{m}(X)$ is a projective curve in a projective space. Notice the intersection number argument to prove Theorem 1.2 of [41] still works when the target space is a pseudoholomorphic curve. Hence the preimage $\Phi_{m}^{-1}(p), p \in \Phi_{m}(X)$, is a $J$ -holomorphic 1-subvariety. Then $\Phi_{m}(X)$ is in fact a Riemann surface since otherwise at a singular point $p \in \Phi_{m}(X)$, a point where the fiber $\Phi_{m}^{-1}(p)$ is smooth is a singular point of $X$.

By the argument of Proposition 2.1, the set of critical values of the map $\Phi_{m}$ is an analytic subvariety of $\Phi_{m}(X)$ of (real) codimension at least 2. In our situation, it has to be a set of finitely many points.

For a fiber $C_{p}=\Phi_{m}^{-1}(p)$, it is the zero locus of a pluricanonical section. Hence $\left[C_{p}\right]=m K_{X}$. Moreover, because $\Phi_{m}$ is base-point-free, any two fibers are disjoint. Hence, $\left[C_{p}\right]^{2}=0=K_{X} \cdot\left[C_{p}\right]$. By adjunction formula, $C_{p}$ is a $J$-holomorphic 1-subvariety whose connected components are possibly multiple elliptic curves. Moreover, for generic $p, C_{p}$ is a disjoint union of smooth elliptic curves.

We look at the collection of all connected components $C_{p, i}$ of all the fibers $C_{p}$. It is given the natural topology by Hausdorff convergence. It could also be endowed with a natural Riemann surface structure. Without loss of generality, we can assume a generic fiber has multiplicity one. If a connected component $C_{p, i}$ has multiplicity one, then choose a holomorphic disk intersecting it transversely at a smooth point. It will intersect at nearby fibers $C_{p^{\prime}}$ uniquely at one point and hence it is locally homeomorphic to $\Phi_{m}(X)$ near $p$. If the connected component $C_{p, i}$ has multiplicity $l>1$, we know for any nearby $q$, there will be $l$ smooth elliptic curves in $C_{q}$ approaching to ( $\left|C_{p, i}\right|, l$ ) since critical value $p$ is isolated. Hence any disk intersecting $C_{p, i}$ transversely at a smooth point will also intersect transeversely the $l$ smooth elliptic curves in $C_{q}$ approaching to $\left(\left|C_{p, i}\right|, l\right)$ for any nearby $q$. Hence, the local model is a covering of disk over disk branched at origin, i.e. $z \mapsto z^{l}$.

In summary, we have a Riemann surface $\Sigma$ and a branched covering $\pi: \Sigma \rightarrow$ $\Phi_{m}(X)$ such that the pluricanonical map $\Phi_{m}$ is factored through $\Sigma$ as $\pi \circ \Phi_{m}^{\prime}$. Moreover, each fiber of the pseudoholomorphic map $\Phi_{m}^{\prime}: X \rightarrow \Sigma$ is a (connected) elliptic curve. \(\square\)

This result is complementary to Theorem 6.7 in [5]. We expect to classify almost complex 4-manifolds with $\kappa_{J}(X)=\kappa^{J}(X)=1$.

The two versions $\kappa^{J}$ and $\kappa_{J}$ are equal to each other and equal to the original Iitaka dimension when $J$ is integrable and $L$ is a holomorphic line bundle.

Question 2.8. Is $\kappa_{J}(X,(L, \mathcal{J}))=\kappa^{J}(X,(L, \mathcal{J}))$ for a complex line bundle $L$ with bundle almost complex structure $\mathcal{J}$ over $(X, J)$ ?

In general, we even do not know whether $\kappa^{J}$ is an integer. In dimension 4, Question 2.8 is equivalent to: if $\kappa_{J}(X,(L, \mathcal{J}))=1$, is it true that $\kappa^{J}(X,(L, \mathcal{J}))=1$ ?

As in the complex setting, we could also study the canonical model of an almost complex manifold by the graded ring construction. When $\Phi_{L, \mathcal{J}}$ is base-point-free, we know $\Phi_{L, \mathcal{J}}(X)$ is an analytic subvariety of the projective space $P\left(H^{0}(X,(L, \mathcal{J}))\right)$ by Proposition 2.2 and hence a projective subvariety by Chow's Theorem.

When $\Phi_{L, \mathcal{J}}$ has base points, we are able to show that it is still true in dimension 4.

Proposition 2.9. Let $\phi$ be a pseudoholomorphic map from $X \backslash B$ to a closed complex manifold $(M, J)$, where $\left(X, J_{X}\right)$ is a closed almost complex 4-manifold, $B \subset X$ is the intersection of $\psi_{i}^{-1}\left(Z_{i}\right)$ for pseudoholomorphic maps $\psi_{i}: X \rightarrow M_{i}$ where $Z_{i}$ is an almost complex submanifold of $M_{i}$. Then $\overline{\phi(X \backslash B)}$ is an analytic subvariety of $M$.

Proof. When $\operatorname{dim}_{\mathbb{C}} \phi(X \backslash B)=0$, since $X \backslash B$ is connected, it will be mapped to a single point. Thus its closure is itself and there is nothing to prove.

When $\operatorname{dim}_{\mathbb{C}} \phi(X \backslash B)=2$, we know the pseudoholomorphic map $\phi$ maps $X_{\text {reg }}$ diffeomorphically to its image. Hence $\left.J\right|_{X_{\text {reg }}}$ is integrable, which in turn implies $J$ is integrable on whole $X$ since $X=\overline{X_{\text {reg }}}$. Hence, it is reduced to the classical complex setting, and the closure $\overline{\phi(X \backslash B)}$ is an analytic subvariety, thus a projective subvariety of $\mathbb{C} P^{N}$. Moreover, the set $\overline{\phi(X \backslash B)} \backslash \phi(X \backslash B)$ is a collection of subvarieties.

When $\operatorname{dim}_{\mathbb{C}} \phi(X \backslash B)=1$, we need to show $\overline{\phi(X \backslash B)}$ is an analytic curve in $\mathbb{C} P^{N}$. We have shown $\phi(X \backslash B)$ is an open analytic curve. If $\overline{\phi(X \backslash B) \backslash \phi(X \backslash}$ $B) \neq \emptyset$, choose a point $p$ from it. Suppose a sequence of points $p_{i}$ approach to $p$. Since critical values are isolated points, we can assume $p_{i}$ are regular value. Hence, the inverse image $\phi^{-1}\left(p_{i}\right)$ are almost complex submanifolds of $X \backslash B$. Since $p \in \overline{\phi(X \backslash B)} \backslash \phi(X \backslash B)$, all limiting points of these fibers $\phi^{-1}\left(p_{i}\right)$ belong to $B$. Since $B$ is a union of pseudoholomorphic 1-subvarieties and finitely many points by Theorem 1.2 of [41] and positivity of intersection of pseudoholomorphic curves, we can choose a pseudoholomorphic disk that intersects $B$ only at such a limiting point. Because $p \in \overline{\phi(X \backslash B)} \backslash \phi(X \backslash B)$, the disk will be mapped to a punctured disk in $\phi(X \backslash B)$ around $p$. In particular, it implies the set $\overline{\phi(X \backslash B) \backslash \phi(X \backslash B) \text { has }}$ Hausdorff dimension 0.

Now $\overline{\phi(X \backslash B)}$ defines a rectifiable current in $M$. The boundary $\partial(\overline{\phi(X \backslash B)}) \subset$ $K \cup A$, where $A$ is the set of critical points and $K=\overline{\phi(X \backslash B) \backslash \phi(X \backslash B) \text {. Since }}$
$\mathcal{H}^{1}(K \cup A)=0$, we know $\partial(\overline{\phi(X \backslash B)})=0$ by Support Theorem ( [10] p. 378). Hence, $\overline{\phi(X \backslash B)}$ is an analytic curve of $M$ by Theorem 5.2.1 of [16]. \(\square\)

We believe that a more careful analysis of the neighborhood of the base locus and the points in the closure would lead us to the same statement for higher dimensions.

Corollary 2.10. Let $B$ be the set of base locus of a complex line bundle $(L, \mathcal{J})$ over an almost complex 4-manifold $(X, J)$. Then the closure $\overline{\Phi_{L, \mathcal{J}}(X \backslash B)}$ is a projective subvariety of $\mathbb{C} P^{N}$, where $N=\operatorname{dim} H^{0}(X,(L, \mathcal{J}))$.
Proof. It is an analytic subvariety of $\mathbb{C} P^{N}$ by Proposition 2.9, and hence a projective subvariety by Chow's Theorem. \(\square\)

As remarked above, we expect $\overline{\Phi_{L, \mathcal{J}}(X \backslash B)}$ to be a projective subvariety of $\mathbb{C} P^{N}$, where $N=\operatorname{dim} H^{0}(X,(L, \mathcal{J}))$ for any almost complex manifold $(X, J)$.

Given a complex line bundle $L$ with a bundle almost complex structure $\mathcal{J}$. It determines a pseudoholomorphic structure $\bar{\partial}_{\mathcal{J}}$ and thus induces that on $L^{\otimes m}, m>0$. For any two complex line bundles $L_{1}, L_{2}$ with bundle almost complex structures $\mathcal{J}_{1}, \mathcal{J}_{2}$, we can define a pseudoholomorphic structure on $L_{1} \otimes L_{2}$ by Leibniz rule. In turn, it determines a bundle almost complex structure $\mathcal{J}_{1} \otimes \mathcal{J}_{2}$ on $L_{1} \otimes L_{2}$. Moreover, pseudoholomorphic sections $s_{1}, s_{2}$ of ( $L_{1}, \mathcal{J}_{1}$ ) and ( $L_{2}, \mathcal{J}_{2}$ ) give rise to pseudoholomorphic section $s_{1} \cdot s_{2}$. We define the section ring of $(L, \mathcal{J})$ to be
$$R(X, L, \mathcal{J})=\oplus_{d=0}^{\infty} H^{0}\left(X, L^{\otimes d}\right) .$$
When $L=\mathcal{K}_{X}$ and $\mathcal{J}=\mathcal{J}_{J}$, we will call the section ring the canonical ring and the corresponding scheme $\operatorname{Proj}(R)$ the canonical model of $X$.

When $(X, J)$ is a complex manifold, the Iitaka dimension is also equal to the tran-scendental degree of the quotient field of the section ring. For projective varieties, the canonical ring is finitely generated [1]. Moreover, it is isomorphic to the closure of the image of $\Phi_{m}$ when $m$ is large. We expect these also hold for a general almost complex manifold $(X, J)$. However, we remark that the section ring need not to be finitely generated even for holomorphic line bundles over projective manifolds.

\section*{3. Bounding $\kappa^{J}$ by symplectic Kodaira dimension}

We have seen that the Iitaka dimensions of a non-integrable almost complex 4-manifold are usually very small. This could be interpreted as saying that we do not have many Cartier divisors for a non-integrable almost complex structure. Meanwhile, we can also look at the growth rate of the dimension of the space of Weil divisors, i.e. the moduli space of the $J$-holomorphic subvarieties $\mathcal{M}_{m e}$ in positive multiple of a class $e \in H^{2}(M, \mathbb{Z})$. In this section, we will give another generalization of Iitaka dimension by assuming the almost complex structure is tamed. We will show this corresponding version of Kodaira dimension is in general greater than the previous two versions $\kappa^{J}$ and $\kappa_{J}$, but is bounded above by the symplectic Kodaira dimension.

When $e$ is a spherical class, we have shown in [40] that, for any almost complex structure, $\mathcal{M}_{e}$ behaves like linear system in algebraic geometry. However, for a
general class $e$ and a general almost complex structure, the moduli space is very complicated. We suggest the following way to estimate (an upper bound for) its dimension. Recall there is a natural topology on $\mathcal{M}_{e}$ defined in terms of convergent sequences (see e.g. [32]). A sequence $\left\{\Theta_{k}\right\}$ in $\mathcal{M}_{e}$ converges to a given element $\Theta$ if the following two conditions are met:
\begin{itemize}
\item[-] $\lim _{k \rightarrow \infty}\left(\sup _{z \in|\Theta|} \operatorname{dist}\left(z,\left|\Theta_{k}\right|\right)+\sup _{z^{\prime} \in\left|\Theta_{k}\right|} \operatorname{dist}\left(z^{\prime},|\Theta|\right)\right)=0$.
\item[-] $\lim _{k \rightarrow \infty} \sum_{\left(C^{\prime}, m^{\prime}\right) \in \Theta_{k}} m^{\prime} \int_{C^{\prime}} \nu=\sum_{(C, m) \in \Theta} m \int_{C} \nu$ for any given smooth 2-form $\nu$.
\end{itemize}

If for any element $x \in \mathcal{M}_{e}$, there is a open neighborhood $U \subset \mathcal{M}_{e}$ and a continuous map from a complex manifold $\mathcal{X}_{U}$ onto $U$, we would say the local dimension of $\mathcal{M}_{e}$ at $x$ is bounded above by $\operatorname{dim}_{\mathbb{C}} \mathcal{X}_{U}$. The manifold $\mathcal{X}_{U}$ is called a local parameter space. We can define $\operatorname{dim} \mathcal{M}_{e}$ to be the infimum of the dimensions of all the possible parameter spaces.

We can thus define
$$\kappa_{W}^{J}(X, e)=\left\{\begin{array}{cl}
-\infty, & \text { if } \mathcal{M}_{m e}=\emptyset \text { for all } m \geq 0 \\
\limsup m \rightarrow \infty & \frac{\log \left(1+\operatorname{dim} \mathcal{M}_{m e}\right)}{\log m},
\end{array}\right. \text { otherwise. }$$

When $e$ is the canonical class, we will simply write $\kappa_{W}^{J}(X)$ for this Weil divisor version of Kodaira dimension.

Lemma 3.1. When $(X, J)$ is a compact 4-dimensional tamed almost complex manifold, $\kappa^{J}(X,(L, \mathcal{J})) \leq \kappa_{W}^{J}\left(X, c_{1}(L)\right)$.

Proof. It follows from two facts. First, the zero locus of sections $s \in H^{0}\left(X,\left(L^{\otimes m}, \mathcal{J}\right)\right)$ is a $J$-holomorphic subvariety in class $m c_{1}(L)$ by Corollary 1.3 of [41].

Second, if two non-trivial pseudoholomorphic sections $s_{1}, s_{2}$ of $(L, \mathcal{J})$ have the same zero locus $Z$ (counted with multiplicities), then $s_{1}=k s_{2}$ for a nonzero constant $k$. If it is not true, then there is a point $x \notin Z$ such that $s_{1}(x)=k s_{2}(x)$ for some constant $k \neq 0$, but $s_{1} \neq k s_{2}$. By the definition of bundle almost complex structure, $s_{1}-k s_{2}$ is also a pseudoholomorphic section of $(L, \mathcal{J})$. However, its zero locus contains $Z \cup\{x\}$. In particular, the homology class of the zero locus is different from $c_{1}(L)$ since any $J$-holomorphic subvariety has non-trivial homology when $J$ is tamed. This contradiction implies that the zero locus of $(L, \mathcal{J})$ determines the pseudoholomorphic section up to a nonzero constant.

These two facts together imply that $\mathbb{P} H^{0}\left(X,\left(L^{\otimes m}, \mathcal{J}\right)\right)$ is embedded in $\mathcal{M}_{m c_{1}(L)}$. Hence $\operatorname{dim} \mathcal{M}_{m c_{1}(L)} \geq P_{L^{\otimes m}, \mathcal{J}}$, and thus $\kappa^{J}(X,(L, \mathcal{J})) \leq \kappa_{W}^{J}\left(X, c_{1}(L)\right)$. \(\square\)

In general, $\kappa_{W}^{J}$ is greater than $\kappa^{J}$.
Proposition 3.2. Suppose $(X, J)$ is a compact tamed almost complex 4-manifold with $b^{+}=1$. Let $e \in H^{2}(X, \mathbb{Z})$ be a class in the positive cone with $e \cdot e>0$. Then $\kappa_{W}^{J}(X, e) \geq 2$.

Meanwhile, $\kappa_{J} \leq 1$ for non-integrable $J$ as shown in Theorem 2.4.

Proof. We let $\iota_{e}=e \cdot e-K_{J} \cdot e$. By Seiberg-Witten wall crossing formula and SW=Gr [20,31], then for any sufficiently large integer $n$, there is an element in $\mathcal{M}_{n e}$ passing through any given $\frac{1}{2} \iota_{n e}$ points if $b_{1} \neq 2$. If $b_{1}=2$, there is an element in $\mathcal{M}_{n e}$ passing through any given $\frac{1}{2} \iota_{n e}-1$ points and intersecting each of the chosen generators of $H_{1}(X, \mathbb{Z})$ /torsion (see e.g. Proposition 1.1 in [33]).

We first choose an element in $\mathcal{M}_{n e}$, say $\Theta$. Choose $\frac{1}{2} \iota_{n e}$ points $x_{i}$ (or $\frac{1}{2} \iota_{n e}-1$ points when $b_{1}=2$ ) on the smooth part of $|\Theta|$. Choose the same number of ( $J$ -holomorphic) disks $D_{i}$ containing these points and transverse to $|\Theta|$. We assume $D_{i} \cap|\Theta|=x_{i}$. When we choose the disks small, the corresponding elements in $\mathcal{M}_{n e}$ passing through one point in each disk would intersect $D_{i}$ only once. Hence, the elements determined by elements in $D_{1} \times \cdots \times D_{\frac{1}{2} \iota_{n e}}$ (or $D_{1} \times \cdots \times D_{\frac{1}{2} \iota_{n e}-1}$ and two circles) are different. Hence, $\operatorname{dim} \mathcal{M}_{n e} \geq \frac{1}{2} \iota_{n e}-1$. This implies $\kappa_{W}^{J}(X, e) \geq 2$. \(\square\)

If $e$ is the class of a symplectic form tamed by $J$, then by the argument of Theorem 3.6, we have $\kappa_{W}^{J}(X, e)=2$.

We can bound $\kappa_{W}^{J}(X)$ from above by the symplectic Kodaira dimension [18], whose definition is recalled in the following.

Definition 3.3. For a minimal compact symplectic 4-manifold ( $X, \omega$ ) with symplectic canonical class $K_{\omega}$, the Kodaira dimension of $(X, \omega)$ is defined in the following way:
$$\kappa^{s}(X, \omega)=\left\{\begin{array}{ccc}
-\infty & \text { if } K_{\omega} \cdot[\omega]<0 \text { or } & K_{\omega} \cdot K_{\omega}<0, \\
0 & \text { if } K_{\omega} \cdot[\omega]=0 \text { and } & K_{\omega} \cdot K_{\omega}=0, \\
1 & \text { if } K_{\omega} \cdot[\omega]>0 \text { and } & K_{\omega} \cdot K_{\omega}=0, \\
2 & \text { if } K_{\omega} \cdot[\omega]>0 \text { and } & K_{\omega} \cdot K_{\omega}>0 .
\end{array}\right.$$

The Kodaira dimension of a non-minimal manifold is defined to be that of any of its minimal models.

Here $K_{\omega}$ is defined as the first Chern class of the cotangent bundle for any almost complex structure compatible with $\omega$. We remark that $\kappa^{s}$ is independent of the symplectic form $\omega$ and thus a smooth invariant.

First, we need a lemma. This is an adaption of Lemma 2.5 in [40]. Here, we no longer assume $e$ is $J$-nef and $\Theta \in \mathcal{M}_{e}$ is connected. However, we fix more points on each irreducible components.

Lemma 3.4. Let $J$ be an almost complex structure on a compact smooth 4-manifold $X^{4}$ and $x_{1}, \cdots, x_{k} \in X$. Let $\Theta=\left\{\left(C_{i}, m_{i}\right), 1 \leq i \leq n\right\} \in \mathcal{M}_{e}$ be a subvariety passing through these points such that there are at least $\max \left\{e \cdot e_{C_{i}}+1,0\right\}$ points in this set with multiplicities $m_{i}$ on the smooth part of each irreducible component $C_{i}$. Then there are no other such subvarieties in the class $e$.

Proof. Suppose there is another subvariety $\Theta^{\prime} \in \mathcal{M}_{e}$ passing through this set of points with multiplicities.

We rewrite two subvarieties $\Theta, \Theta^{\prime} \in \mathcal{M}_{e}$, allowing $m_{i}=0$ in the notation, such that they share the same set of irreducible components formally, i.e. $\Theta=\left\{\left(C_{i}, m_{i}\right)\right\}$
and $\Theta^{\prime}=\left\{\left(C_{i}, m_{i}^{\prime}\right)\right\}$. Then for each $C_{i}$, if $m_{i} \leq m_{i}^{\prime}$, we change the components to $\left(C_{i}, 0\right)$ and $\left(C_{i}, m_{i}^{\prime}-m_{i}\right)$. At the same time, if a point $x$, as one of $x_{1}, \cdots, x_{k}$, is on $C_{i}$, then the weight is reduced by $m_{i}$ as well. Similar procedure applies to the case when $m_{i}>m_{i}^{\prime}$. Apply this process to all $i$ and discard finally all components with multiplicity 0 and denote them by $\Theta_{0}, \Theta_{0}^{\prime}$ and still use $\left(C_{i}, m_{i}\right)$ and $\left(C_{i}, m_{i}^{\prime}\right)$ to denote their components. Notice they are homologous, formally having homology class
$$e-\sum_{m_{k_{i}}<m_{k_{i}}^{\prime}} m_{k_{i}} e_{C_{k_{i}}}-\sum_{m_{l_{j}}^{\prime}<m_{l_{j}}} m_{l_{j}}^{\prime} e_{C_{l_{j}}}-\sum_{m_{q_{p}}^{\prime}=m_{q_{p}}} m_{q_{p}}^{\prime} e_{C_{q_{p}}} .$$

There are two ways to express the class, by taking $e=e_{\Theta}$ or $e=e_{\Theta^{\prime}}$ in the above formula. Namely, it is
$$\sum_{m_{k_{i}}<m_{k_{i}}^{\prime}}\left(m_{k_{i}}^{\prime}-m_{k_{i}}\right) e_{C_{k_{i}}}+\text { others }=e_{\Theta_{0}^{\prime}}^{\prime}=e_{\Theta_{0}}=\sum_{m_{l_{j}}^{\prime}<m_{l_{j}}}\left(m_{l_{j}}-m_{l_{j}}^{\prime}\right) e_{C_{l_{j}}}+\text { others } .$$
Here the term "others" means the terms $m_{i} e_{C_{i}}$ or $m_{i}^{\prime} e_{C_{i}}$ where $i$ is not taken from $k_{i}, l_{j}$ or $q_{p}$.

Now $\Theta_{0}$ and $\Theta_{0}^{\prime}$ have no common components. By the process we just applied, counted with weight, there are at least $e \cdot e_{\Theta_{0}}+\sum_{i: C_{i} \in \Theta_{0}} m_{i}$ points on $\Theta_{0}$. These points are also contained in $\Theta_{0}^{\prime}$ with right weights. Hence $\Theta_{0}$ and $\Theta_{0}^{\prime}$ would intersect at least $e \cdot e_{\Theta_{0}}+\sum_{i: C_{i} \in \Theta_{0}} m_{i}$ points with weight.

We notice that $e \cdot e_{\Theta_{0}} \geq e_{\Theta_{0}} \cdot e_{\Theta_{0}^{\prime}} \geq 0$. In fact, the difference $e-e_{\Theta_{0}}=e-e_{\Theta_{0}^{\prime}}$ has 3 types of terms, any of them pairing non-negatively with the class $e_{\Theta_{0}}$. For the terms with index $k_{i}$, i.e. the terms with $m_{k_{i}}<m_{k_{i}}^{\prime}$, we use the expression of $e_{\Theta_{0}}=\sum_{m_{l_{j}}^{\prime}<m_{l_{j}}}\left(m_{l_{j}}-m_{l_{j}}^{\prime}\right) e_{C_{l_{j}}}+$ others to pair with. Since the irreducible curves involved in the expression are all different from $C_{k_{i}}$, we have $e_{C_{k_{i}}} \cdot e_{\Theta_{0}} \geq 0$. Similarly, for $C_{l_{j}}$, we use the expression of $e_{\Theta_{0}^{\prime}}=\sum_{m_{k_{i}}<m_{k_{i}}^{\prime}}\left(m_{k_{i}}^{\prime}-m_{k_{i}}\right) e_{C_{k_{i}}}+$ others. We have $e_{C_{l_{j}}} \cdot e_{\Theta_{0}^{\prime}} \geq 0$. For $C_{q_{p}}$, we could use either $e_{\Theta_{0}}$ or $e_{\Theta_{0}^{\prime}}$. Since $e_{\Theta_{0}}=e_{\Theta_{0}^{\prime}}$, we have $\left(e-e_{\Theta_{0}}\right) \cdot e_{\Theta_{0}} \geq 0$.

Since $\Theta \neq \Theta^{\prime}$, we know $\sum_{i: C_{i} \in \Theta_{0}} m_{i}>0$. Hence $e \cdot e_{\Theta_{0}}+\sum_{i: C_{i} \in \Theta_{0}} m_{i}>e_{\Theta_{0}} \cdot e_{\Theta_{0}^{\prime}}$. This inequality $e \cdot e_{\Theta_{0}}>e_{\Theta_{0}}^{2}$ implies there are more intersections than the homology intersection number $e_{\Theta_{0}}^{2}$ of our new subvarieties $\Theta_{0}$ and $\Theta_{0}^{\prime}$. This contradicts to the local positivity of intersection and the fact that $\Theta_{0}, \Theta_{0}^{\prime}$ have no common component. The contradiction implies that $\Theta$ is the unique such subvariety as described in the statement. \(\square\)

We are ready to prove the main result of this section.
Theorem 3.5. Let $(X, J)$ be a compact tamed almost complex 4-manifold. Then
$$\kappa_{W}^{J}(X) \leq \kappa^{s}(X) .$$
Proof. For any pseudoholomorphic section $s \in H^{0}\left(X, \mathcal{K}_{X}^{\otimes m}\right)$, it is a $\left(J, \mathcal{J}_{J}\right)$-holomorphic map from $X$ to the total space of $\mathcal{K}_{X}^{\otimes m}$ endowed with the standard bundle almost
complex structure induced by $\bar{\partial}_{m}$. Hence, by Corollary 1.3 of [41], we know the zero locus is a $J$-holomorphic 1-subvariety in class $m K_{X}$.

When $\kappa^{s}(X)=-\infty$, the canonical class is not effective, so $\mathcal{M}_{m K_{X}}=\emptyset, \forall m>0$. Hence, $\kappa_{W}^{J}(X)=-\infty$.

When $\kappa^{s}(X)=0$, then $K_{X}=K_{X_{\text {min }}}+\sum E_{i}$, where $n K_{X_{\text {min }}}=0$ for $n=1$ or 2. Moreover, by Proposition A.5, there is a unique $J$-holomorphic representative for positive linear combination of -1 classes, for any tamed $J$. This shows $\mathcal{M}_{m K_{X}}$ is a single point. Hence, $\kappa_{W}^{J}(X)=0=\kappa^{s}(X)$.

When $\kappa^{s}(X)=1$ or 2, we know $\mathcal{M}_{K_{X}} \neq \emptyset$ when $b^{+}>1$ and $\mathcal{M}_{2 K_{X}} \neq \emptyset$ when $b^{+}=1$. Hence, we will estimate the elements in $\mathcal{M}_{m K_{X}}$ or $\mathcal{M}_{2 m K_{X}}$ respectively. For simplicity of notation, we will only deal with the case when $\mathcal{M}_{K_{X}} \neq \emptyset$ and estimate $\mathcal{M}_{m K_{X}}$. The other case (i.e. when $\mathcal{M}_{2 K_{X}} \neq \emptyset$ ) is almost identical.

When $\kappa^{s}(X)=1, K_{X}=K_{X_{\text {min }}}+\sum E_{i}$, where $K_{X_{\text {min }}}^{2}=0$. Let us first assume $X$ is minimal. Then $K_{X}=K_{X_{\text {min }}}$ is $J$-nef by Lemma 2.1 of [39]. Hence $K_{X} \cdot\left[C_{i}\right]=0$ for any irreducible component of a $J$-holomorphic subvariety $\Theta=\left\{\left(C_{i}, m_{i}\right)\right\}$ in class $m K_{X}$. In particular, each connected component of $\Theta$ has square 0. Moreover, by Theorem 1.4 of [23], each irreducible component is a torus with square zero or a -2 sphere.

In fact, choose a $J$-tame symplectic form $\omega$ with integral cohomology class, we know there are at most $m C_{K_{X}}:=m\left\lceil\frac{[\omega] \cdot K_{X}}{\inf _{C}[\omega] \cdot[C]}\right\rceil$ irreducible components (counted with multiplicities) for any elements in $\mathcal{M}_{m K_{X}}$. Here, we take the infimum over all non-trivial $J$-holomorphic curves $C$, which is non-zero by our our assumption that $[\omega]$ is an integral class. For any $\Theta \in \mathcal{M}_{m K_{X}}$, choose a point on the smooth part of each irreducible component $C_{i}$ with multiplicity $m_{i}$. By Lemma 3.4, there is a unique $J$-holomorphic subvariety in $\mathcal{M}_{m K_{X}}$ passing through these points. Hence, $X^{m C_{K}}$ contains a parameter space of $\mathcal{M}_{m K_{X}}$. This tells us that $\operatorname{dim}\left(M_{m K_{X}}\right) \leq$ $m C_{K} \operatorname{dim}(X)$, so $\lim _{m \rightarrow \infty} \frac{\log \left(1+\operatorname{dim}\left(M_{m K_{X}}\right)\right.}{\log (m)} \leq \lim _{m \rightarrow \infty} \frac{\log \left(1+m C_{K} \operatorname{dim}(X)\right)}{\log (m)}=1$, which implies $\kappa_{W}^{J}(X) \leq 1$.

If $X$ is non minimal, for any element $\Theta \in \mathcal{M}_{m K_{X}}$, by Theorem 3 of [29] (also see the proof of Proposition A.2), there exists another tamed almost complex structure $J^{\prime}$ for which $\Theta$ is $J^{\prime}$-holomorphic and $J^{\prime}$ is integrable on a neighborhood of $|\Theta|$. By Corollary 2.10 of [39], we always have a smooth $J^{\prime}$-holomorphic -1 rational curve. Since $K_{X} \cdot E=-1<0$ for any -1 classes, we know this rational curve is a component of $\Theta$. We blow it down, and change the configuration of $\Theta$ correspondingly. Keep doing so until we get a minimal manifold $X^{\prime}$, i.e. a manifold containing no smooth spheres of self-intersection -1. Hence, $\Theta$ changes to a pseudoholomorphic subvariety $\Theta_{0}$ in the nef class $m K_{\text {min }}$. In particular, we know each irreducible component of $\Theta_{0}$ is a torus with square zero or a -2 sphere. This implies each component in original $\Theta$ has non-positive self-intersection. Then we choose a point on each irreducible component $C_{i}$ of $\Theta$ with multiplicity $m_{i}$, we know there is a unique $J$ -holomorphic subvariety in $\mathcal{M}_{m K_{X}}$ passing through them. Since there are at most $m C_{K_{X}}$ irreducible components for any elements in $\mathcal{M}_{m K_{X}}$, we know $X^{m C_{K}}$ contains a parameter space of $\mathcal{M}_{m K_{X}}$. This implies $\kappa_{W}^{J}(X) \leq 1$.

Let us look at the case of $\kappa^{s}(X)=2$. We also first assume it is minimal. Again, $K_{X}$ is $J$-nef by Lemma 2.1 of [39]. Then we can choose $m K_{X} \cdot\left[C_{i}\right]+1$ points with multiplicities $m_{i}$ on the smooth part of each irreducible component of an element in $\mathcal{M}_{m K_{X}}$, we know there is a unique one passing through these points by Lemma 3.4. These points vary in a family of dimension at most $4 \sum m_{i}\left(m K_{X} \cdot\left[C_{i}\right]+1\right) \leq$ $4 m^{2} K_{X}^{2}+4 m\left\lceil\frac{[\omega] \cdot K_{X}}{\min _{C}[\omega] \cdot[C]}\right\rceil$. In other words, $\operatorname{dim} \mathcal{M}_{m K_{X}} \leq 4 m^{2} K_{X}^{2}+4 m\left\lceil\frac{[\omega] \cdot K_{X}}{\min _{C}[\omega] \cdot[C]}\right\rceil$. Hence $\kappa_{W}^{J}(X) \leq 2$.

Now we assume $X$ is not minimal. By Lemma 2.1 of [39], if $K_{X} \cdot[C]<0$ for an irreducible curve $C$, then $C$ is a -1 rational curve. Hence, for any $\Theta \in \mathcal{M}_{m K_{X}}$, we can choose $m K_{X} \cdot\left[C_{i}\right]+1$ points with multiplicity $m_{i}$ on the smooth part of each irreducible component $C_{i}$ which is not a -1 rational curve. By Lemma 3.4, we know there is a unique such element in $\mathcal{M}_{m K_{X}}$ passing through these points with multiplicities. Now these points vary in a family of dimension at most $4 \sum m_{i}\left(m K_{X}\right.$. $\left.\left[C_{i}\right]+1\right)$. Notice for any $\Theta \in \mathcal{M}_{m K_{X}}$, the sum of the multiplicities $m_{i}$ for components of $\Theta$ is bounded from above by $m C_{K_{X}}$. Hence, we have
$$\begin{aligned}
\operatorname{dim} \mathcal{M}_{m K_{X}} & \leq 4 \sum_{C_{i} \notin \mathcal{E}_{K_{J}}} m_{i}\left(m K_{X} \cdot\left[C_{i}\right]+1\right) \\
& =4 m^{2} K_{X}^{2}+\sum_{C_{i} \in \mathcal{E}_{K_{J}}} 4 m_{i}(m+1)+\sum_{C_{i} \notin \mathcal{E}_{K_{J}}} 4 m_{i} \\
& \leq 4 m^{2} K_{\min }^{2}-4 k m^{2}+4 m^{2} C_{K_{X}}+4 m C_{K_{X}} \\
& =\left(4 K_{\min }^{2}-4 k+4 C_{K_{X}}\right) m^{2}+4 m C_{K_{X}}
\end{aligned}$$
where $k$ is the number of -1 classes in $X$. This implies $\kappa_{W}^{J}(X) \leq 2$. \(\square\)

Proof of Theorem 1.5. It follows from Lemma 3.1 and Theorem 3.5. \(\square\)

The estimates in the above proof might remind the reader about estimates in probabilistic combinatorics. The coefficients of the polynomials in our estimates are not optimal.

Remark 3.6. In the proof of Theorem 3.5, we have shown that $\kappa_{W}^{J}(X)=\kappa^{s}(X)$ when $\kappa^{s}(X) \leq 0$.

Moreover, when $(X, J)$ is a compact tamed almost complex 4-manifold with $b^{+}=1$ and $\kappa^{s}(X)=2$, the equality also holds. The result follows from applying Proposition 3.2 to $e=K_{X_{\text {min }}}$.

Corollary 3.7. Let $J$ be a compact tamed almost complex structure on a complex surface $\left(X, J_{X}\right)$. Then
$$\kappa^{J}(X) \leq \kappa^{J_{X}}(X) .$$
Proof. By [7], $\kappa^{J_{X}}(X)=\kappa^{s}(X)$ for any 4-manifold admitting both complex and symplectic structures. Then the result follows from Theorem 1.5. \(\square\)

\section*{4. Vanishingness of plurigenera}

A negative line bundle on a compact complex manifold is a holomorphic line bundle whose Chern class is a negative class. The Iitaka dimension of a negative line bundle is always negative infinity by the positive intersection of complex manifolds. On an almost complex 4-manifold, we have the following.

Proposition 4.1. Let $L$ be a complex line bundle over a compact almost complex 4 -manifold $(X, J)$. If there is a $J$-tamed symplectic form $\omega$ such that $[\omega] \cdot c_{1}(L)<0$, then for any bundle almost complex structure $\mathcal{J}$ on $L$, we have $P_{L, \mathcal{J}}=0$ and $\kappa^{J}(X,(L, \mathcal{J}))=-\infty$.

Proof. If $P_{L, \mathcal{J}}>0$, then there is a nonzero section in $H^{0}(X,(L, \mathcal{J}))$. By Corollary 4.2 in [5] and Corollary 1.3 in [41], its zero locus is a $J$-holomorphic 1-subvariety in class $c_{1}(L)$. Then the tameness of $J$ implies that $[\omega] \cdot c_{1}(L) \geq 0$, a contradiction.

Similarly $P_{L^{\otimes m}, \mathcal{J}}=0$ for $m>1$ and $\kappa^{J}(M,(L, \mathcal{J}))=-\infty$. \(\square\)

In particular, if there is a $J$-tamed symplectic form $\omega$ on an almost complex 4 -manifold $(X, J)$ such that $[\omega]=-c_{1}(L)$, then for any bundle almost complex structure $\mathcal{J}$ on $L, P_{L, \mathcal{J}}=0$ and $\kappa^{J}(M,(L, \mathcal{J}))=-\infty$. As a specific example, any tamed $J$ on $\mathbb{C} P^{2}$ has the plurigenera $P_{m}=0, m>0$, and the Kodaira dimension $\kappa^{J}=-\infty$ (this also follows from Corollary 3.7).

To generalize the above to higher dimensions, one effective way is to prove a result similar to Corollary 1.3 in [41] for almost complex submanifolds with any codimensions. Another way is to apply the analytic method. We prove the following result which only uses Theorem 3.8 in [41] and a Bochner type formula on almost complex manifolds.

Theorem 4.2. Let $L$ be a complex line bundle over a compact almost complex $2 n$ -manifold $(X, J)$. If there is a $J$-compatible symplectic form $\omega$ such that $[\omega]^{n-1}$. $c_{1}(L)<0$, then for any bundle almost complex structure $\mathcal{J}$ on $L, P_{L, \mathcal{J}}=0$ and $\kappa^{J}(X,(L, \mathcal{J}))=\kappa_{J}(X,(L, \mathcal{J}))=-\infty$.

Proof. We prove it by contradiction. Assume that $s \in H^{0}(X,(L, \mathcal{J}))$ is a nonzero section. Denote $V=\{x \in X \mid s(x)=0\}$. By Theorem 3.8 in [41], $V$ is a closed set with Hausdorff dimension $2 n-2$ (if nonempty). In particular, $V$ has measure zero and the complement $U=X \backslash V$ is a dense open set.

Assume that $h$ is an arbitrary Hermitian metric on $L$ with $|s|_{h}^{2}=h(s, s) \geq 0$. Let $g$ be the almost Kähler metric on $X$ determined by $\omega$ and $J$, and denote ∇ the unique Hermitian connection on $L$ such that $\nabla^{0,1}=\bar{\partial}_{L}$ (see Lemma 3.3 in [5]). On $U$, we have $\nabla s=\nabla^{1,0} s=\xi \otimes s$, for some $\xi \in \Lambda^{1,0}(U)$. From
$$d|s|_{h}^{2}=\nabla|s|_{h}^{2}=h(\nabla s, s)+h(s, \nabla s)=\xi|s|_{h}^{2}+\bar{\xi}|s|_{h}^{2},$$
we get that $\xi=\frac{\partial|s|_{h}^{2}}{|s|_{h}^{2}}=\partial \log |s|_{h}^{2}$.
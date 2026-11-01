---
retention_scope: session
part: 2
total_parts: 2
---

[Part 2/2 of: Kodaira dimensions of almost complex manifolds II]

Denote the curvature form of $h$ on $L$ by $\Theta$. Then $\left.\Theta\right|_{U}=d \xi=d \partial \log |s|_{h}^{2}$. By the Chern-Weil theory, we have $c_{1}(L)=\left[\frac{\sqrt{-1}}{2 \pi} \Theta\right]$. Also, on $U$, we have
$$\begin{aligned}
\sqrt{-1} \operatorname{tr}_{\omega}\left(\bar{\partial} \partial \log |s|_{h}^{2}\right) & =\sqrt{-1}\left(\frac{\operatorname{tr}_{\omega}\left(\bar{\partial} \partial|s|_{h}^{2}\right)|s|_{h}^{2}-\operatorname{tr}_{\omega}\left(\bar{\partial}|s|_{h}^{2} \wedge \partial|s|_{h}^{2}\right)}{|s|_{h}^{4}}\right) \\
& =\sqrt{-1} \frac{\operatorname{tr}_{\omega}\left(\bar{\partial} \partial|s|_{h}^{2}\right)}{|s|_{h}^{2}}+|\xi|^{2}
\end{aligned}$$
where $\operatorname{tr}_{\omega} \cdot$ denotes the contraction operator on a $(1,1)$ form by $\omega^{-1}$. So we get the identity
$$-\sqrt{-1} \operatorname{tr}_{\omega}\left(\bar{\partial} \partial|s|_{h}^{2}\right)=|\nabla s|_{h}^{2}-\sqrt{-1} \operatorname{tr}_{\omega}\left(\bar{\partial} \partial \log |s|_{h}^{2}\right)|s|_{h}^{2} .$$
For any function $f$, since $d \partial f=-d \bar{\partial} f$, we have $\partial \bar{\partial} f=-\bar{\partial} \partial f$. Denote $\Delta_{\omega}=$ $-\sqrt{-1} \operatorname{tr}_{\omega} \bar{\partial} \partial=\sqrt{-1} \operatorname{tr}_{\omega} \partial \bar{\partial}$ acting on smooth functions of $X$. It is an elliptic operator which differs from the Levi-Civita Laplacian by some first order terms (see Lemma 3.2 in [34]). So the maximum principle also holds in this case. Extend $\mathrm{tr}_{\omega}$ to any 2-form $\phi$ by defining $\operatorname{tr}_{\omega} \phi=\operatorname{tr}_{\omega} \phi^{1,1}$, where $\phi^{1,1}$ is the $(1,1)$ component of $\phi$. From (2) and the density of $U$, we obtain the Bochner type formula on $X$ (in the integrable case, see 35 for example):
$$\Delta_{\omega}|s|_{h}^{2}=|\nabla s|_{h}^{2}-\sqrt{-1} \operatorname{tr}_{\omega} \Theta|s|_{h}^{2}$$
Now by assumption, we have
$$\begin{aligned}
0>[\omega]^{n-1} \cdot c_{1}(L) & =\int_{X} \frac{\sqrt{-1}}{2 \pi} \Theta \wedge \omega^{n-1}=\int_{X} \frac{\sqrt{-1}}{2 \pi} \Theta^{1,1} \wedge \omega^{n-1} \\
& =\int_{X} \frac{\sqrt{-1} \operatorname{tr}_{\omega} \Theta^{1,1}}{2 n \pi} \omega^{n}=\int_{X} \frac{\sqrt{-1} \operatorname{tr}_{\omega} \Theta}{2 n \pi} \omega^{n}
\end{aligned}$$
This gives that the average of $\sqrt{-1} \operatorname{tr}_{\omega} \Theta$ is negative. Next, we do a conformal change of the metric $h$ to make it to be a negative constant (see similar arguments in [11 35]). To obtain this, for any smooth real function $\varphi$ on $X, h^{\prime}=e^{\varphi} h$ is also a Hermitian metric on $L$. The Hermitian connection of $h^{\prime}$ has connection one form $\xi^{\prime}=\xi+\partial \varphi$ and curvature form $\Theta^{\prime}=\Theta+d \partial \varphi$. Then on $X, \sqrt{-1} \operatorname{tr}_{\omega} \Theta^{\prime}=\sqrt{-1} \operatorname{tr}_{\omega} \Theta-\Delta_{\omega} \varphi$. Let $k=\int_{X} \frac{\sqrt{-1} \operatorname{tr}_{\omega} \Theta}{2 n \pi} \omega^{n}<0$. Since $\omega$ is closed (a Gauduchon metric is sufficient), $\int_{X} \Delta_{\omega} f \omega^{n}=0$ for any smooth function $f$. By the Hodge decomposition of smooth functions with respect to $\Delta_{\omega}$, the Poisson equation $\Delta_{\omega} \varphi=\sqrt{-1} \operatorname{tr}_{\omega} \Theta-\frac{2 n k \pi}{\int_{X} \omega^{n}}$ has a smooth solution. Choosing this solution $\varphi$, we get that
$$\sqrt{-1} \operatorname{tr}_{\omega} \Theta^{\prime}=\frac{2 n k \pi}{\int_{X} \omega^{n}}=k_{1},$$
where $k_{1}$ is a negative constant.
Return to the Bochner formula for the Hermitian metric $h^{\prime}$, we have
$$\Delta_{\omega}|s|_{h^{\prime}}^{2}=|\nabla s|_{h^{\prime}}^{2}-k_{1}|s|_{h^{\prime}}^{2} .$$

Since $X$ is compact, there is a maximum point $p$ of $|s|_{h^{\prime}}^{2}$ with $|s|_{h^{\prime}}^{2}(p)>0$. By the maximum principle, $\Delta_{\omega}|s|_{h^{\prime}}^{2}(p) \leq 0$, but $\left(|\nabla s|_{h^{\prime}}^{2}-k_{1}|s|_{h^{\prime}}^{2}\right)(p)>0$, a contradiction. Therefore, $H^{0}(X,(L, \mathcal{J}))=0$.

As $c_{1}\left(L^{\otimes m}\right) \cdot[\omega]^{n-1}=m c_{1}(L) \cdot[\omega]^{n-1}<0$, we similarly get that $H^{0}\left(X,\left(L^{\otimes m}, \mathcal{J}\right)\right)=$ 0 and $\kappa^{J}(X,(L, \mathcal{J}))=-\infty$. \(\square\)

From the proof above, we also prove the following vanishing of plurigenera, which is a generalization of the known results in the complex setting (in the Kähler case by Yau [37] and in more general Hermitian case by Yang [36]).
Theorem 4.3. Let $(X, J)$ be a compact almost complex manifolds. If one of the following is satisfied:
(1) $X$ holds a Hermitian metric with positive Chern scalar curvature everywhere,
(2) $X$ holds a Gauduchon metric with positive total Chern scalar curvature, then $\kappa^{J}(X)=\kappa_{J}(X)=-\infty$.
Proof. Let $\omega$ be an almost Hermitian metric on $X$. It naturally induces a Hermitian metric on the canonical bundle $\mathcal{K}$ as discussed in Section 3. The unique Hermitian connection ∇ on $\mathcal{K}$ is induced by the Chern connection (see e.g. Remark 3.4 in [5]). Denote $\Theta$ to be the curvature 2-form. It is well known [34] that $-\sqrt{-1} \operatorname{tr}_{\omega} \Theta=s^{C}$ where $s^{C}$ is the Chern scalar curvature of the Chern connection. Let $\sigma \in H^{0}\left(X, \mathcal{K}_{X}^{\otimes m}\right)$. The same calculation as above gives that
$$\Delta_{\omega}|\sigma|^{2}=|\nabla \sigma|^{2}+m s^{C}|\sigma|^{2} .$$
If $s^{C}>0$, using the maximum principle again, we derive that $\sigma=0$.
Next, assume that the total Chern scalar curvature $k=\int_{X} s^{C} \omega^{n}>0$ with $\omega$ being a Gauduchon metric, i.e. $\partial \bar{\partial} \omega^{n-1}=0$. Denote $\Delta_{\omega}=\sqrt{-1} \operatorname{tr}_{\omega} \partial \bar{\partial}$ to be the generalized Laplacian. For any smooth function $f$, as
$$\int_{X} \Delta_{\omega} f \omega^{n}=\int_{X} \sqrt{-1} n \partial \bar{\partial} f \wedge \omega^{n-1}=\int_{X} \sqrt{-1} n f \wedge \partial \bar{\partial} \omega^{n-1}=0,$$
where we use the Gauduchon condition in the last step, the Poisson equation $\Delta_{\omega} \varphi=-s^{C}+\frac{k}{\int_{X} \omega^{n}}$ has a smooth solution $\varphi$. Define a Hermitian metric on $\mathcal{K}^{\otimes m}$ by $h^{\prime}=e^{\varphi} h_{\omega}$, where $h_{\omega}$ denotes the Hermitian metric induced by $\omega$. Then the curvature form $\Theta^{\prime}$ of $h^{\prime}$ has $\sqrt{-1} \operatorname{tr}_{\omega} \Theta^{\prime}=\sqrt{-1} \operatorname{tr}_{\omega} \Theta-\Delta_{\omega} \varphi=-\frac{k}{\int_{X} \omega^{n}}<0$. Let $\sigma \in H^{0}\left(X, \mathcal{K}^{\otimes m}\right)$. The Bochner formula with respect to $h^{\prime}$ then reads:
$$\Delta_{\omega}|\sigma|_{h^{\prime}}^{2}=|\nabla \sigma|_{h^{\prime}}^{2}+\frac{k}{\int_{X} \omega^{n}}|\sigma|_{h^{\prime}}^{2}$$
Therefore, the maximum principle gives that $\sigma=0$. The proof is finished. \(\square\)

\section*{5. Further discussion and open problems}

In this last section, we would discuss some speculations and open problems generated from this series of papers. For more discussions and in particular the relation with the intersection theory of almost complex manifolds and other aspects of almost complex geometry, we recommend 42.
5.1. Hodge theory. It would be very interesting to compare the cohomology group $H^{0}\left(X, \mathcal{K}_{X}\right) \cong H_{\tilde{\partial}}^{2,0}(X)$ with the $J$-anti-invariant cohomology $H_{J}^{-}(X)$ defined in 21 when $\operatorname{dim} X=4$. Both are birational invariants [2,5]. The zero loci of elements in both groups support $J$-holomorphic subvarieties in the canonical class. For $H_{J}^{-}(X)$, both statements are shown in [2]. The non-integrable almost complex structures of Section 6.3 of [5] on $T^{2} \times S$ have $\operatorname{dim} H^{0}\left(X, \mathcal{K}_{X}\right) \geq g-1$. On the other hand, Conjecture 2.5 in [8] says the dimension of the $J$-anti-invariant cohomology $H_{J}^{-}(X)$ is greater than 2 only if $J$ is integrable. It would be interesting to calculate $H_{J}^{-}(X)$ for these examples explicitly.

In higher dimensions, we could similarly define a cohomology group $M H_{J}^{-}(X)(M$ stands for middle). We look at the bundle of real parts of $(n, 0)$ forms $\Lambda_{\mathbb{R}}^{n, 0}$ where $n=$ $\operatorname{dim}_{\mathbb{C}} X$, whose space of sections is denoted by $\Omega_{\mathbb{R}}^{n, 0}$. The almost complex structure $J$ on $X$ induces a complex line bundle structure on $\Lambda_{\mathbb{R}}^{n, 0}$. It can be described concretely by its action on a section $\beta$ as $J \beta\left(v_{1}, v_{2}, \cdots, v_{n}\right):=-\beta\left(J v_{1}, v_{2}, \cdots, v_{n}\right)$. We define $M H_{J}^{-}(X)$ to be the subgroup of $H^{n}(X, \mathbb{R})$ whose element has a representative in $\Omega_{\mathbb{R}}^{n, 0}$. For any Riemannian metric $g$ compatible with $J, \Lambda_{\mathbb{R}}^{n, 0}$ is a subbundle of $\Lambda_{g}^{+}$. Hence, a closed form in $\Omega_{\mathbb{R}}^{n, 0}$ is a self-dual harmonic form. As discussed in [2], any representative of any element in $M H_{J}^{-}(X)$ corresponds to a $J$-holomorphic subvariety of complex dimension $n-1$ in the canonical class up to Question 3.9 in [41]. It would be interesting to compare $H^{0}\left(X, \mathcal{K}_{X}\right) \cong H_{\bar{\partial}}^{n, 0}(X)$ with $M H_{J}^{-}(X)$.

It would be great to understand more about the groups $\mathcal{H}_{\bar{\partial}_{E}}^{(p, q)}(X, E)$. When $E$ is a holomorphic bundle over a complex manifold $X$, they are isomorphic to the Dolbeault cohomology groups of holomorphic bundles by Hodge theory. Especially, when $E$ is the trivial line bundle, these are just the classical Dolbeault cohomology groups. When $q=0$ or $\operatorname{dim}_{\mathbb{C}} X$, the groups depend only on $J$ and $\bar{\partial}_{E}$ [5], in particular, it is independent of the defining Hermitian metric. Whether its dimension is also an invariant of the almost complex structure $J$ when $E$ is a trivial bundle and $0<q<\operatorname{dim}_{\mathbb{C}} X$ is a famous question of Kodaira-Spencer in Hirzebruch's 1954 problem list [13], which is answered negatively recently by Tom Holt and the second author [14]. The method works very effectively to compute $\mathcal{H}_{\bar{\partial}}^{(p, q)}(X)$ explicitly for nilmanifolds. It would be appealing to apply the techniques to compute general $\mathcal{H}_{\bar{\partial}_{E}}^{(p, q)}(X, E)$.

Many aspects of Dolbeault cohomology groups for complex manifolds extend to our setting. For example, it is clear from the definition that $\mathcal{H}_{\bar{\partial}_{E}}^{(n, q)}(X, E) \cong$ $\mathcal{H}_{\bar{\partial}_{E}}^{(0, q)}\left(X, \mathcal{K}_{X} \otimes E\right)$. When $q=0$ and $E$ is the trivial line bundle, it is equal to $H^{0}\left(X, \mathcal{K}_{X}\right)$. We also have Serre duality for the groups $\mathcal{H}_{\bar{\partial}_{E}}^{(p, q)}(X, E)$, namely, $\mathcal{H}_{\bar{\partial}_{E}}^{(p, q)}(X, E) \cong\left(\mathcal{H}_{\bar{\partial}_{E^{*}}}^{(n-p, n-q)}\left(X, E^{*}\right)\right)^{*}$ (see Proposition 3.7 in [5]).

Another interesting direction is to show the dimension of $\mathcal{H}_{\bar{\partial}}^{(p, 0)}(X):=\mathcal{H}_{\bar{\partial}_{\mathcal{O}}}^{(p, 0)}(X, \mathcal{O})$ is a birational invariant, namely it is invariant under degree 1 pseudoholomorphic maps. It is shown in Theorem 5.5 in [5] for $\operatorname{dim} X=4$.
5.2. Comparison of Iitaka dimensions. We have defined three versions of Iitaka dimension for almost complex manifolds. The versions $\kappa^{J}$ and $\kappa_{J}$ are defined for arbitrary almost complex structure $J$. The last version $\kappa_{W}^{J}$ is defined for tamed almost complex structures on 4-manifolds. One is able to formulate a similar definition of $\kappa_{W}^{J}$ in higher dimensions. Generalization of positivity of intersection in [41] to singular subvarieties should lead to similar results as in dimension 4.

Question 2.8 asks whether $\kappa_{J}(X,(L, \mathcal{J}))=\kappa^{J}(X,(L, \mathcal{J}))$. On the other hand, $\kappa_{W}^{J}\left(X, c_{1}(L)\right)$ is in general larger. By definition, $\kappa_{J}$ takes value from $-\infty$ and integers $0,1, \cdots, n$. However, we do not know whether $\kappa^{J}(X,(L, \mathcal{J})) \leq \operatorname{dim}_{\mathbb{C}} X$ and whether it always takes integer values, although we expect these are true because of Question 2.8. We also would like to show $\kappa_{W}^{J}(X, e) \leq 2$ in general. By Theorem 3.5, It is true for the corresponding Kodaira dimension, i.e. when $e=K_{X}$. In particular, it implies $\kappa^{J}(X) \leq 2$ when $(X, J)$ is a tamed almost complex manifold.

The second version of our Kodaira dimensions $\kappa_{J}$ is the simplest invariant provided by the image of $\Phi_{L, \mathcal{J}}$. We would like to know more about this image. It has been shown that $\Phi_{L, \mathcal{J}}(X \backslash B)$ is an open analytic subvariety. It is believed to be true that $\overline{\Phi_{L, \mathcal{J}}(X \backslash B)}$ is a projective subvariety, as shown in Corollary 2.10 when $\operatorname{dim}_{\mathbb{R}} X=4$.

The study of this problem would also tell us what a rational map in almost complex setting should be like, as we have shown in Proposition 2.9 for dimension 4. In general, the study of pseudoholomorphic rational maps, i.e. pseudoholomorphic maps defined on the complement of a pseudoholomorphic subvariety in an almost complex manifold, is very important. The fundamental question is whether the closure of its image and the complement of the image in it are pseudoholomorphic subvarieties in the target almost complex manifold.

In addition, we would like to know whether the transcendental degree of the quotient field of the section ring is equal to $\kappa_{J}$. In particular, we expect (the closure of) the image of the pluricanonical map $\Phi_{m}$ would be stable for large $m$, and equal to $\operatorname{Proj}\left(R\left(X, K_{X}\right)\right)$.
5.3. Extension of pseudoholomorphic sections. Hartogs type extension is very important in studying our Kodaira dimensions. For example, we would like to know

Question 5.1. If $(L, \mathcal{J})$ is a pseudoholomorphic bundle over $(X, J)$ and $B \subset X$ is a pseudoholomorphic subvariety of complex codimension at least two, does any pseudoholomorphic section of $(L, \mathcal{J})$ over $X \backslash B$ extend to a pseudoholomorphic section over $X$ ?

Theorem 5.2 in [5] establishes this Hartogs extension when $\operatorname{dim} X=4$. In general, Question 5.1 would help to prove the invariance of $\kappa^{J}$ and $\kappa_{J}$ under degree 1 pseudoholomorphic maps, i.e. the birational invariance of $\kappa^{J}$ and $\kappa_{J}$, in all dimensions. It would be helpful in obtaining other results, e.g. Question 2.8. It would also help to answer the following question.

Question 5.2. Let $f: X \rightarrow M$ be a generically surjective pseudoholomorphic rational map such that $\operatorname{dim} X=\operatorname{dim} M$. Do we have $\kappa^{J}(X) \geq \kappa^{J}(M)$.

This answer is even not known when $f$ is defined on whole $X$. Notice we do not have the generalization of Iitaka conjecture. For any pseudoholomorphic surface bundle over surface $f: X \rightarrow M$ whose total space $X$ is not complex and both base and fiber have genus greater than one, we have $\kappa^{J}(F)+\kappa^{J}(M)=2>\kappa^{J}(X)$. Hence, the additivity of Kodaira dimension, as explored in [22, 38] for other kinds of Kodaira dimensions, would not hold for almost complex Kodaira dimensions.

Another important type of extension result in complex geometry is the extendability of analytic subvarieties, for example Theorem 2.3. We expect it also holds for pseudoholomorphic subvarieties. More generally, we would like to study the extendability of pseudoholomorphic maps between almost complex manifolds, generalizing the classical Picard theorem.
5.4. Examples. We would like to calculate more examples. We are particularly interested in finding more or even obtaining structural results for non-integrable almost complex structures with large Kodaira (or Iitaka) dimensions. For instance, do we have a version of Iitaka fibration? Do we know $\kappa^{J}=n-1$ only when the manifold is a pseudoholomorphic elliptic fibration over a complex manifolds? In dimension 4, we have the second part of Theorem 1.4.

In Section 6.3 of [5], we have examples of non-integrable almost complex structures with large Kodaira dimension. These examples are deformations of complex structures. It would be very interesting to know some non-integrable almost complex structures on symplectic non-Kähler manifolds with large Kodaira dimension. Some special pseudoholomorphic elliptic fibrations might work.

The values of Kodaira dimensions and dimensions of holomorphic $p$-forms for some special ambient space are also very interesting. In particular, we are interested in almost complex structures on $\mathbb{C} P^{n}$ and $S^{6}$. On $S^{6}$, there is a standard non-integrable almost complex structure denoted by J. In Section 7 of [5], we compute Kodaira dimensions of J (and then -J) as well as the value of the Hodge numbers $h^{1,0}, h^{2,0}$. Similar results are proven to hold on strictly nearly Kähler 6-manifolds (see [4]). It is known that there are two connected components of all the almost complex structures on $S^{6}$ [3], containing J and -J respectively. We would like to know whether our calculation would help to compute Kodaira dimension for other almost complex structures on $S^{6}$ and almost complex structures on other homogeneous spaces.

We would like to calculate examples of the Iitaka dimension for a general complex line bundle. For example, we are interested in the following almost complex structures on homogeneous spaces.

Assume that $G$ is a compact connected semisimple Lie group and $T \subset G$ a maximal torus. Let $\mathfrak{g}$ and $\mathfrak{t}$ be Lie algebras of $G$ and $T$ respectively. The set of all roots $R$ is by definition constituted of all elements $\alpha \in i \mathfrak{t} \subset \mathfrak{t} \otimes \mathbb{C}$ such that there exists a nonzero $X \in \mathfrak{g} \otimes \mathbb{C}$ with $[H, X]=\langle\alpha, H\rangle X$ for all $H \in \mathfrak{t}$, or equivalently, the characters of the corresponding irreducible representation of $T$, if we identify the character group $\operatorname{Hom}\left(T, \mathbb{C}^{*}\right)$ with $\left(\mathbb{C}^{*}\right)^{\operatorname{dim} T} \subset \mathfrak{t} \otimes \mathbb{C}$. The eigenspaces are denoted $\mathfrak{g}_{\alpha}$.

The tangent space of $G / T$ at the coset $e T$ decomposes, in terms of Lie algebra, as
$$(\mathfrak{g} / \mathfrak{t}) \otimes \mathbb{C}=\oplus_{\alpha \in R} \mathfrak{g}_{\alpha} .$$
By left action, such a decomposition induces a decomposition of $T^{*}(G / T) \otimes \mathbb{C}$. By choosing a regular element $H_{0} \in i \mathfrak{t}$, we have the decomposition of $R=R^{+} \cup R^{-}$to positive and negative roots. Notice $R^{+}=-R^{-}$as $\alpha \in R$ if and only if $-\alpha \in R$. We have
$$\left[\mathfrak{g}_{\alpha}, \mathfrak{g}_{\beta}\right] \subset \mathfrak{g}_{\alpha+\beta}$$
for any positive roots $\alpha, \beta$.
In fact, the decomposition $R=R^{+} \cup R^{-}$is a decomposition $T(G / T) \otimes \mathbb{C}=$ $T_{1,0}(G / T) \oplus T_{0,1}(G / T)$, thus gives rise an almost complex structure on $G / T$. The relation (4) is the integrability condition. This is the well known complex structure on $G / T$.

We can modify this construction a bit such that $R$ is decomposed as a disjoint union of two sets $R_{1}$ and $R_{2}$, with the relation $R_{1}=-R_{2}$. But we do not require the condition (4). This gives different choices of non-integrable almost complex structures on $G / T$. What is the Iitaka dimension of the anti-canonical bundle, or some other complex line bundle?
5.5. Symplectic and almost contact invariants. We can define symplectic invariants by
$$\tilde{\kappa}^{s}(X, \omega)=\sup _{J \text { tamed by } \omega} \kappa,$$
where $\kappa$ could be either $\kappa^{J}, \kappa_{J}$ or $\kappa_{W}^{J}$. We would like to explore more about it. In particular, whether these symplectic invariants are diffeomorphism invariants in dimension 4? The version for $\kappa_{W}^{J}$ is better understood and studied in Section 3. One can also define symplectic invariants in a similar manner for $h^{p, 0}$.

We are also able to define invariants for almost contact structures in the following way. For any almost contact manifold $\left(M^{2 n-1}, J\right)$, the product $M^{2 n-1} \times S^{1}$ admits a natural almost complex structure. Then our almost complex invariants $\kappa^{J}, \kappa_{J}$, $\kappa_{W}^{J}$ and $h^{p, 0}$ on $M \times S^{1}$ would induce almost contact invariants on $(M, J)$. It is particularly interesting to study them for all 3-manifolds.

\section*{References}
\begin{itemize}
\item[] [1] C. Birkar, P. Cascini, C. Hacon, J. McKernan, Existence of minimal models for varieties of log general type, J. Amer. Math. Soc. 23 (2010), no. 2, 405-468.
\item[] [2] L. Bonthrone, W. Zhang, $J$-holomorphic curves from closed $J$-anti-invariant forms, arXiv:1808.09356, Comm. Anal. Geom., to appear.
\item[] [3] R. Bryant, S.-S. Chern's study of almost-complex structures on the six-sphere, Internat. J. Math. 32 (2021), no. 12, Paper No. 2140006, 15 pp.
\item[] [4] H. Chen, G. Wang, Kodaira dimension of nearly Kähler 6-manifolds, Acta Math. Sinica, Chinese Series. 64 (2021), no. 1, 87-98.
\item[] [5] H. Chen, W. Zhang, Kodaira dimensions of almost complex manifolds I, arXiv:1808.00885.
\item[] [6] P. De Bartolomeis, G. Tian, Stability of complex vector bundles, J. Differential Geom. 43 (1996), no. 2, 231-275.
\end{itemize}
\begin{itemize}
\item[] [7] J.G. Dorfmeister, W. Zhang, The Kodaira Dimension of Lefschetz Fibrations, Asian J. Math. 13 (2009), no. 3, 341-357.
\item[] [8] T. Draghici, T.J. Li, W. Zhang, On the $J$-anti-invariant cohomology of almost complex 4-manifolds, Q. J. Math. 64 (2013), no. 1, 83-111.
\item[] [9] J.D. Evans, I. Smith, Bounds on Wahl singularities from symplectic topology, Algebr. Geom. 7 (2020), no. 1, 59-85.
\item[] [10] H. Federer, Geometric measure theory, Die Grundlehren der mathematischen Wissenschaften, Band 153 Springer-Verlag New York Inc., New York 1969 xiv+676 pp.
\item[] [11] P. Gauduchon, La 1-forme de torsion d'une variété hermitienne compacte, Math. Ann. 267 (1984), no. 4, 495-518.
\item[] [12] P. Griffiths, J. Harris, Principles of algebraic geometry, Pure and Applied Mathematics. Wiley-Interscience, New York, 1978.
\item[] [13] F. Hirzebruch, Some problems on differentiable and complex manifolds, Ann. of Math. (2) 60, (1954), 213-236.
\item[] [14] T. Holt, W. Zhang, Harmonic forms on the Kodaira-Thurston manifold, arXiv:2001.10962, Adv. Math., to appear.
\item[] [15] S. Iitaka, On D-dimensions of algebraic varieties, J. Math. Soc. Japan 23 (1971), 356-373.
\item[] [16] J. R. King, The currents defined by analytic varieties, Acta Math. 127 (1971), no. 3-4, 185-220.
\item[] [17] J.M. Lee, Introduction to smooth manifolds, Graduate Texts in Mathematics, 218. Springer-Verlag, New York, 2003. xviii+628 pp. ISBN: 0-387-95495-3.
\item[] [18] T.J. Li, Symplectic 4-manifolds with Kodaira dimension zero, J. Differential Geom. 74 (2006), no. 2, 321-352.
\item[] [19] T.J. Li, Kodaira Dimension in Low Dimensional Topology, Tsinghua lectures in mathematics, 265-291, Adv. Lect. Math. (ALM), 45, Int. Press, Somerville, MA
\item[] [20] T.J. Li, A.-K. Liu, The equivalence between $S W$ and $G r$ in the case where $b^{+}=1$, Internat. Math. Res. Notices (1999), no. 7, 335-345.
\item[] [21] T.J. Li, W. Zhang, Comparing tamed and compatible symplectic cones and cohomological properties of almost complex manifolds, Comm. Anal. Geom. 17 (2009), no. 4, 651-683.
\item[] [22] T.-J. Li, W. Zhang, Additivity and relative Kodaira dimensions, Geometry and Analysis, Vol. II, 103-135, Adv. Lect. Math. (ALM), 18, International Press, (2011).
\item[] [23] T.J. Li, W. Zhang, $J$-holomorphic curves in a nef class, Int. Math. Res. Not. (2015) Vol. 2015 12070-12104.
\item[] [24] M. Micallef, B. White, The structure of branch points in minimal surfaces and in pseudoholomorphic curves, Ann. of Math. (2) 141 (1995), no. 1, 35-85.
\item[] [25] J. Rana, G. Urzúa, Optimal bounds for $T$-singularities in stable surfaces, Adv. Math. 345 (2019), 814-844.
\item[] [26] R. Remmert, Projektionen analytischer Mengen, (German) Math. Ann. 130 (1956), 410-441.
\item[] [27] A. Sard, Hausdorff measure of critical images on Banach manifolds, Amer. J. Math. 87 (1965), 158-174.
\item[] [28] B. Shiffman, On the removal of singularities of analytic sets, Michigan Math. J. 15 (1968), 111-120.
\item[] [29] J.-C. Sikorav, Singularities of $J$-holomorphic curves, Math. Z. 226 (1997), no. 3, 359-373.
\item[] [30] C. Taubes, SW ⇒ Gr: from the Seiberg-Witten equations to pseudo-holomorphic curves, J. Amer. Math. Soc. 9 (1996), no. 3, 845-918.
\item[] [31] C. Taubes, Seiberg Witten and Gromov invariants for symplectic 4-manifolds. Edited by Richard Wentworth, First International Press Lecture Series, 2. International Press, Somerville, MA, 2000. vi+401 pp. ISBN: 1-57146-061-6.
\item[] [32] C. Taubes, Tamed to compatible: Symplectic forms via moduli space integration, J. Symplectic Geom. 9 (2011), 161-250.
\item[] [33] C. Taubes, Tamed to compatible when $b^{2+}=1$ and $b^{1}=2$, arXiv:1708.04279.
\item[] [34] V. Tosatti, A general Schwarz Lemma for almost-Hermitian manifolds, Comm. Anal. Geom. 15 (2007), no.5, 1063-1086.
\end{itemize}
[35] X. Yang, Hermitian manifolds with semi-positive holomorphic sectional curvature. Math. Res. Lett. 23 (2016), 939-952.
[36] X. Yang, Scalar curvature on compact complex manifolds, Tran. Amer. Math. Soc. 371 (2019), 2073-2087.
[37] S-T. Yau, On the curvature of compact Hermitian manifolds, Invent. Math. 25 (1974), 213-239.
[38] W. Zhang, Geometric structures, Gromov norm and Kodaira dimensions, Adv. Math. 308 (2017), 1-35.
[39] W. Zhang, The curve cone of almost complex 4-manifolds, Proc. Lond. Math. Soc. (3) 115 (2017), no. 6, 1227-1275.
[40] W. Zhang, Moduli space of J-holomorphic subvarieties, Selecta Math. (N.S.) 27 (2021), no. 2, Paper No. 29, 44 pp.
[41] W. Zhang, Intersection of almost complex submanifolds, Camb. J. Math. 6 (2018), no. 4, 451-496.
[42] W. Zhang, From smooth to almost complex, Proceedings of the eighth ICCM, to appear.

\section*{Appendix A. Uniqueness of exceptional curves for irrational symplectic 4-manifolds}

In this appendix, we would give an affirmative answer to the following question, which is Question 4.18 in [39].
Question A.1. Suppose $M$ is symplectic 4-manifold, which is not diffeomorphic to $\mathbb{C} P^{2} \# k \overline{\mathbb{C} P^{2}}$. Let $E \in \mathcal{E}_{K_{J}}$. Is it true that for any subvariety $\Theta=\left\{\left(C_{i}, m_{i}\right)\right\}$ in class $E$, i.e. $E=\sum m_{i}\left[C_{i}\right]$, each $C_{i}$ is a smooth rational curve?

Here, a class $E \in \mathcal{E}_{K_{J}}$ (called an exceptional curve class) is a $K_{J}$-spherical class such that $E^{2}=K_{J} \cdot E=-1$, where $K_{J}$ is the canonical class of $J$ and a $K_{J}$-spherical class is a class $e$ which could be represented by a smoothly embedded sphere and $g_{J}(e):=\frac{1}{2}\left(e \cdot e+K_{J} \cdot e\right)+1=0$. For a generic tamed $J$, any exceptional curve class is represented by a unique embedded $J$-holomorphic sphere with self-intersection -1.

The answer to Question A. 1 was known to be true for irrational ruled surfaces [40], and there are even many integrable complex structures on rational surfaces where the statement does not hold 39, 40].

Before answering Question A.1, we first prove the following result, which is essentially Proposition 2.11 of [9].
Proposition A.2. Suppose that $(M, \omega)$ is a non rational or ruled symplectic 4-manifold and $J$ is an $\omega$-tame almost complex structure. If $\Theta \in \mathcal{M}_{E}$ for a class $E \in \mathcal{E}_{K_{J}}$, then $\Theta$ is an exceptional curve of the first kind.

Recall that a $J$-holomorphic subvariety $\Theta$ is called an exceptional curve of the first kind if there exists a neighborhood $\left(N, J^{\prime}\right)$ of $\Theta$ where $J^{\prime}$ is an integrable complex structure with $\left.J^{\prime}\right|_{|\Theta|}=J_{|\Theta|}$, an open neighborhood $N^{\prime}$ of $0 \in \mathbb{C}^{2}$, and a holomorphic birational map $\pi: N \rightarrow N^{\prime}$, such that $\Theta$ is a $J^{\prime}$-holomorphic 1-subvariety and $\pi^{-1}(0)=\Theta$.
Proof. We first show that there exists a tamed almost complex structure $J^{\prime}$ for which $\Theta$ is $J^{\prime}$-holomorphic and $J^{\prime}$ is integrable on a neighborhood of $|\Theta|$. It essentially follows from Theorem 3 of [29], with a couple of remarks. By Theorem 1 of [29], there exists a complex structure $J_{1}$ on a neighborhood $U_{0}$ of $\operatorname{Sing}(|\Theta|)$ coinciding with $J$ on $\operatorname{Sing}(|\Theta|)$ and such that $|\Theta| \cap U_{0}$ is a $J_{1}$-complex curve. The first remark is that we can choose $J_{1}$ and $U_{0}$ such that it is arbitrarily close to $J$ in the $C^{0}$ norm. This follows because it is clear from original construction of Micallef-White [24] that the $C^{1}$-diffeomorphism of $U_{0}$ and a neighborhood of the origin in the complex plane has Jacobian the identity matrix at the singular points. Hence, by choosing $U_{0}$ small, $J_{1}$ is $C^{0}$ close to $J$ in $U_{0}$. We then extend $J_{1}$ to $M$ as an almost complex structure so that $J_{1}$ is close to $J$ on a neighborhood $U$ of $|\Theta|$ and the regular part $C_{1}$ of $|\Theta|$ is still $J_{1}$-complex. We can assume that $C_{1} \cap U_{0}$ is a finite union of punctured disks $D_{k}$.

As in [29], we can assume $\operatorname{Sing}(C)$ meets every component of $C$. Then $C_{1}$ has no closed component, thus its normal bundle is trivial as a complex bundle. Thus we can find a tubular neighborhood $T_{1}$ and a diffeomorphism $\tau:\left(T_{1}, C_{1}\right) \rightarrow\left(C_{1} \times\right.$
$\left.\mathbb{C}, C_{1} \times\{0\}\right)$. We transport the structure $J_{1}$ to obtain $\tau_{*}\left(J_{1}\right)=J_{2}$ on $C_{1} \times \mathbb{C}$ such that $C_{1} \times\{0\}$ is $J_{2}$-complex.

Let $J_{0}=\left.J\right|_{C_{1}} \times i$ on $C_{1} \times \mathbb{C}$. Let $A_{k} \subset D_{k}$ be annuli (with respect to $J_{1}$ ), and $A$ be the union of $A_{k}$. Denote $A^{\prime}$ and $A_{k}^{\prime}$ respectively for those $J_{0}$-holomorphic curves that are ( $J_{0}, J_{1}$ )-biholomorphic to $A$ and $A_{k}$ on $C_{1}$ and $D_{k}$ respectively. The map could be chosen arbitrarily close to the identity by our construction. We then apply the extension lemma used in 29 to $A, A^{\prime}$ to get a diffeomorphism $\psi$ between neighborhoods $N$ and $N^{\prime}$ of $A$ and $A^{\prime}$ that extends the previous one between $A$ and $A^{\prime}$, such that $\psi_{*}\left(J_{0}\right)=\tau_{*}\left(J_{1}\right)$. We impose that it extends to a self-diffeomorphism (still denote $\psi$ ) of $C_{1} \times \mathbb{C}$, such that it is arbitrarily close to identity at $C_{1} \times\{0\}$.

Since the restriction of $\tau_{*}^{-1} \circ \psi_{*}$ on $C_{1}$ is the identity, by choosing the tubular neighborhood $T_{1}$ smaller, we can get $\tau_{*}^{-1} \circ \psi_{*}\left(J_{0}\right)$ arbitrarily $C^{0}$ close to $J$. Hence the complex structure
$$\tilde{J}=\left\{\begin{array}{cl}
\tau_{*}^{-1} \circ \psi_{*}\left(J_{0}\right), & \text { on } T_{2} \backslash U_{0} \\
J_{1}, & \text { on } U_{0}
\end{array}\right.$$
defined as in [29] (extend to whole $M$ by a cutoff function) is arbitrarily $C^{0}$ close to the original tamed $J$. Hence, it is tamed.

We then prove the proposition by induction on the number of irreducible components of $\Theta$. Let $\Theta=\left\{\left(C_{i}, m_{i}\right), 1 \leq i \leq n\right\} \in \mathcal{M}_{E}$, where each $C_{i}$ is an irreducible $J$-holomorphic curve. We have
$$-1=K \cdot E=K \cdot \Theta=\sum_{i=1}^{n} m_{i} K \cdot\left[C_{i}\right] .$$
Hence, there is some $i$ such that $K \cdot\left[C_{i}\right]<0$. By Lemma 2.1 of [39], we know $C_{i}$ is a smooth rational -1-curve. We write $\pi: M \rightarrow M^{\prime}$ for the blowing down map with respect to the above chosen $J^{\prime}$ that is integrable on a neiborhood of $|\Theta|$.

We notice that if $\pi_{*}(\Theta)$ is not a point, then $K_{M^{\prime}} \cdot \pi_{*} E=-1$. It follows from the calculation of Lemma 2.13 in [9] or the combinatorial blowdown calculation in [39] as the classes of in $\mathcal{E}_{K_{J}}$ are orthogonal when $M$ is non rational or ruled. Then by induction, $\Theta$ can be blown down to a point. Therefore $\Theta$ is an exceptional curve of the first kind. \(\square\)

By the above understanding of Sikorav's result, the argument of [9] would lead to the following more complete version of their main result.

Theorem A.3. Let $X$ be a symplectic 4-manifold with $K_{X}=[\omega]$. If there is a symplectic embedding of rational homology ball $\iota: B_{p, q} \rightarrow X$, such that the rational blow-up of $\iota\left(B_{p, q}\right)$ is non-rational, then
$$l \leq 4 K_{X}^{2}+7,$$
where $l$ is the length of the continued fraction expansion of $\frac{p^{2}}{p q-1}$. When, $p=n, q=1$ (then $l=n-1$ ), we get the stronger inequality $l \leq 2 K_{X}^{2}+1$.

In particular, it would lead to the same bound of the length of Wahl singularities (i.e. cyclic quotient singularities of type $\frac{1}{p^{2}}(p q-1,1)$ ), for which an optimal bound is obtained in 25.

Proof. As remarked in [9], by Proposition A. 2 and the above understanding of Sikorav's result, their argument is able to obtain the above statement when the rational blow-up of $\iota\left(B_{p, q}\right)$ is non-ruled, by appealing to Lemma 2.1 of 39 instead of their Corollary 2.2.

We can show that the rational blow-up of $\iota\left(B_{p, q}\right)$, denoted by $W$, cannot be irrationally ruled. If it were, we blow down the exceptional curves $k$ times to get a minimal model $S$. We have $K_{S}^{2} \leq 0$ since $W$ is irrationally ruled. We have the relation $K_{S}^{2}-k=K_{W}^{2}=K_{X}^{2}-l$. As in [9], the number $l$ is also the number of (negative) spheres $\left\{C_{1}, \cdots, C_{l}\right\}$ in the chain of exceptional divisor of the singularity of type $\frac{1}{p^{2}}(p q-1,1)$. We can choose a tamed almost complex structure $J$ such that each $C_{i}$ is $J$-holomorphic. By Theorem 1.2 of [40], each negative rational curve is an irreducible component of the finitely many (disjoint) reducible subvarieties in the fiber class $T$. We can further choose this $J$ such that it is integrable in a neighborhood of the union of these reducible subvarieties. When $W$ is symplectically non-minimal, or equivalently, there is at least one reducible subvariety in the class $T$, by Corollary 2.10 of [39], we know there is at least one smooth $J$-holomorphic -1 rational curve (which must be an irreducible component of a reducible subvariety in the class $T$ ). Blow it down and continue this process, we known each reducible subvariety in the class $T$ can be reduced to a smooth sphere of square 0 by blowdown. Hence, in particular, we know $l \leq k$. Since $K_{X}^{2}=[\omega]^{2}>0$, we have $K_{S}^{2}=K_{X}^{2}+$ $(k-l)>0$, which is a contradiction. \(\square\)

We will now give an affirmative answer to Question A. 1 also for other symplectic 4-manifolds. More precisely, we have the following.

Theorem A.4. Let $M$ be a symplectic 4-manifold which is not diffeomorphic to $\mathbb{C} P^{2} \# k \overline{\mathbb{C} P^{2}}, k \geq 1$. Then for any tamed $J$, there is a unique $J$-holomorphic subvariety in any class $E \in \mathcal{E}_{K_{J}}$, whose irreducible components are smooth rational curves of negative self-intersection. Moreover, this $J$-holomorphic subvariety is an exceptional curve of the first kind when $M$ is not ruled.

Proof. When $M$ is an irrational ruled surface $S^{2} \times \Sigma_{g} \# k \overline{\mathbb{C} P^{2}}, g \geq 1$, it follows from Theorem 1.1 of [40].

We now prove the theorem when $M$ is neither rational nor ruled. In this situation, there is at lease one $J$-holomorphic subvariety in class $E$ which is an exceptional curve of the first kind as explained in the following. For generic tamed almost complex structure, $E$ is represented by a smooth rational curve. By Gromov compactness, we have a $J$-holomorphic stable map representing $E$. By Proposition A.2, this is an exceptional curve of first kind. We call it $\Theta_{0}$. In particular, there is a smooth rational -1-curve $E^{\prime}$. For convenience, we also call its homology class $E^{\prime}$. Since $M$ is not rational or ruled, we know $E \cdot E^{\prime}=0$.

Then we prove the uniqueness. Suppose there is another $J$-holomorphic subvariety in class $E$, say $\Theta=\left\{\left(C_{i}, m_{i}\right)\right\}_{i=1}^{n}$. By Theorem 3 of [29], there exists another tamed almost complex structure $J^{\prime}$ for which $\Theta_{0}$ and $\Theta$ are both $J^{\prime}$-holomorphic and $J^{\prime}$ is integrable on a neighborhood of $\left|\Theta_{0}\right| \cup|\Theta|$. We may therefore assume without loss of generality that $J=J^{\prime}$ in the following.

There are two cases of blowdowns. If there is some $C_{i}$ with $E^{\prime}=\left[C_{i}\right]$, then we simply blow down $E^{\prime}$ by $\pi_{1}: M \rightarrow M^{\prime}$ and $\pi_{1 *}([\Theta])=\pi_{1 *}\left(\left[\Theta_{0}\right]\right)$ become an exceptional curve class $\pi_{1 *} E$ in $M^{\prime}$.

If $E^{\prime}$ is not an irreducible component of $\Theta$, we have $E^{\prime} \cdot\left[C_{i}\right] \geq 0, \forall i$. Since $E \cdot E^{\prime}=0$, we have $E^{\prime} \cdot\left[C_{i}\right]=0, \forall i$. We blow down the curve $E^{\prime}$ by $\pi_{2}: M \rightarrow \tilde{M}$. Now $\pi_{j *}\left(\Theta_{0}\right)$ and $\pi_{j *}(\Theta)$ are still $\pi_{j *} J$-holomorphic subvarieties representing $\pi_{j *}(E)$ for $j=1,2$. By induction and Lemma 2.13 of [9], we can continue blowing down $\Theta_{0}$ to a smooth point. Call the composition of the sequence of (first and second types of) blowdowns by $\pi: M \rightarrow M_{0}$. We have $\pi_{*}([\Theta])=\pi_{*}\left(\left[\Theta_{0}\right]\right)=0$. Since $J$ is tamed, we know $\pi(|\Theta|)=\{p t s\}$. In other words, we have proved that the support $|\Theta| \subset\left|\Theta_{0}\right|$. In other words, $\Theta$ and $\Theta_{0}$ share the same irreducible components, but their multiplicities (nonnegative, but could be zero) might be different.

Now we show that these multiplicities are in fact the same. For doing so, we rewrite the homology classes of each $C_{i}$. Since $\Theta_{0}$ is an exceptional curve of first kind, each $C_{i}$ corresponds to a -1-rational curve in each blowdown. In other words, there are $n$ second cohomology classes $E_{1}, \cdots, E_{n}$ which can be represented by embedded symplectic spheres with $E_{i}^{2}=-1, i=1, \cdots, n$, and $E_{i} \cdot E_{j}=0$ for $i \neq j$, such that $\left[C_{i}\right]=E_{i}-\sum_{j>i} m_{i j} E_{j}$. Here $\left(m_{i j}\right)_{i, j=1}^{n}$ is a strict upper triangular square matrix whose entries are 0 or 1 . In particular, $E=E_{1}$ and $E^{\prime}=E_{n}=\left[C_{n}\right]$. Thus $\left[C_{i}\right], i=1, \cdots, n$, are linearly independent. Hence there is a unique way to represent the class $E$ by the linear combination of $\left[C_{i}\right]$. This implies each irreducible component of $\Theta$ and $\Theta_{0}$ has the same multiplicity, i.e. $\Theta=\Theta_{0}$. Hence, we finish the proof of uniqueness when $M$ is neither rational nor ruled, and thus all the statements in the theorem. \(\square\)

The result of Theorem A. 4 is sharp. When $M=\mathbb{C} P^{2} \# k \overline{\mathbb{C} P^{2}}$ with $k \geq 1$, a $J$-holomorphic subvariety in class $E$ need not to be an exceptional curve of the first kind.

If $M=\mathbb{C} P^{2} \# \overline{\mathbb{C} P^{2}}$, we look at a Hirzebruch surface $\mathbb{F}_{3}$. It contains a -3-curve in class $2 E_{1}-H$. Then along with a fiber, it constitutes a $J$-holomorphic subvariety in class $E_{1}=\left(2 E_{1}-H\right)+\left(H-E_{1}\right)$ which is not an exceptional curve of the first kind.

For $k=2$, we blow up at a point not on the -3-curve of $\mathbb{F}_{3}$. If we call the blow up divisor $E_{2}$, then the subvariety $\left\{\left(2 E_{1}-H, 1\right),\left(H-E_{1}-E_{2}, 1\right),\left(E_{2}, 1\right)\right\} \in \mathcal{M}_{E_{1}}$ is not an exceptional curve of the first kind. For $k>2$, we can continue this process by blowing up points outside the support of this subvariety.

When $S^{2} \times \Sigma_{g} \# k \overline{\mathbb{C} P^{2}}, g \geq 1$ and $k>1$, there are also examples of integrable complex structure $J$ such that a subvariety in class $E \in \mathcal{E}_{K_{J}}$ is not an exceptional curve of the first kind. We first blow up a fiber to get two exceptional rational curves in classes $E_{1}$ and $T-E_{1}$ respectively. Then we blow up the intersection of these two
rational curves. The subvariety $\left\{\left(T-E_{1}-E_{2}, 1\right),\left(E_{2}, 1\right),\left(E_{1}-E_{2}, 1\right)\right\} \in \mathcal{M}_{T-E_{2}}$ is not an exceptional curve of the first kind. This phenomenon is the essential underlying reason for the totally different proofs of Question A. 1 for the irrational ruled case in [40] and the non ruled case in this paper.

When $M=\mathbb{C} P^{2} \# k \overline{\mathbb{C} P^{2}}$ with $k \geq 8$, even the statement of Question A. 1 is not true, see [40].

The argument of Theorem A. 4 could be used to prove other uniqueness results of subvarieties. The following is used in our proof of Theorem 3.4. We will skip some steps appeared in the proof of Theorem A.4.

Proposition A.5. Suppose $M^{4}$ is not rational or ruled, and $J$ is a tamed almost complex structure. Let $\left\{E_{1}, \cdots, E_{n}\right\}$ be the set of exceptional curve classes. Then there is a unique $J$-holomorphic subvariety in any class $k_{1} E_{1}+\cdots+k_{n} E_{n}$ where $k_{i}$ are non-negative integers.

Proof. First, there exists a $J$-holomorphic subvariety $\Theta_{0}$ in any class $k_{1} E_{1}+\cdots+$ $k_{n} E_{n}$ provided by a combination of $J$-holomorphic subvarieties in classes $E_{i}$.

Suppose there is another, say $\Theta=\left\{\left(C_{i}, m_{i}\right)\right\}_{i=1}^{n}$. As in the proof of Theorem A.4, we may assume $J$ is integrable on a neighborhood of $\left|\Theta_{0}\right| \cup|\Theta|$. We keep blowing down $\Theta_{0}$ to a smooth point, and denote the composition of the sequence of blowdowns by $\pi: M \rightarrow M_{0}$. We have $\pi_{*}([\Theta])=\pi_{*}\left(\left[\Theta_{0}\right]\right)=0$. Since $J$ is tamed, we know $\pi(|\Theta|)=\{p t s\}$. In other words, we have proved that $\Theta$ and $\Theta_{0}$ share the same irreducible components. We can apply the same argument to show the multiplicities are the same. Hence, we have shown $\Theta=\Theta_{0}$. \(\square\)

Department of Mathematics, Zhejiang Normal University, Jinhua Zhejiang, 321004, China

Email address: chj@zjnu.edu.cn
Mathematics Institute, University of Warwick, Coventry, CV4 7AL, England
Email address: weiyi.zhang@warwick.ac.uk
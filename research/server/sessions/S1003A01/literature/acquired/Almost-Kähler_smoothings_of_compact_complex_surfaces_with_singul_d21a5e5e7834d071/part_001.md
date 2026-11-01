---
retention_scope: session
part: 1
total_parts: 3
---

[Part 1/3 of: Almost-Kähler smoothings of compact complex surfaces with singularities.]

---
source_file: 1806_07773.pdf
converter: mathpix
format: mmd
---

\title{
Almost-Kähler smoothings of compact complex surfaces with $A_{1}$ singularities.
}

\author{
Caroline Vernier
}

June 21, 2018

\begin{abstract}
This paper is concerned with the existence of metrics of constant Hermitian scalar curvature on almost-Kähler manifolds obtained as smoothings of a constant scalar curvature Kähler orbifold, with $A_{1}$ singularities. More precisely, given such an orbifold that does not admit nontrivial holomorphic vector fields, we show that an almost-Kähler smoothing $\left(M_{\varepsilon}, \omega_{\varepsilon}\right)$ admits an almost-Kähler structure $\left(\hat{J}_{\varepsilon}, \hat{g}_{\varepsilon}\right)$ of constant Hermitian curvature. Moreover, we show that for $\varepsilon>0$ small enough, the $\left(M_{\varepsilon}, \omega_{\varepsilon}\right)$ are all symplectically equivalent to a fixed symplectic manifold $(\hat{M}, \hat{\omega})$ in which there is a surface $S$ homologous to a 2-sphere, such that $[S]$ is a vanishing cycle that admits a representant that is Hamiltonian stationary for $\hat{g}_{\varepsilon}$.
\end{abstract}

\section*{1 Introduction}

\subsection*{1.1 Context: gluing methods in Kähler geometry.}

Let $M$ be a compact complex manifold of Kähler type. The program of Calabi is concerned with the existence of canonical metrics in a given Kähler class $\Omega$ on $M$. More specifically, Calabi proposed the study of the functional
$$\omega \in \Omega_{>0} \mapsto \int_{M} s(\omega)^{2} \frac{\omega^{m}}{m!} ;$$
here $\Omega_{>0}$ denotes the set of definite positive representants of the cohomology class $\Omega$, and $s(\omega)$ is the scalar curvature of the associated metric. The critical points of this functional are called extremal metrics, and they are the candidates for canonical metrics in this framework.

Computing the corresponding Euler-Lagrange equation, one obtains that a Kähler metric is extremal if and only if the Hamiltonian vector field $X_{s(\omega)}$ is real holomorphic. In particular, constant scalar curvature metrics are extremal, and both notions coincide if $M$ admits no non-trivial holomorphic vector field.

Non-trivial holomorphic vector fields appear as an obstruction in constructions of constant scalar curvature metrics. More precisely, on a Kähler manifold $(M, J, \omega)$, the obstructions on the structure of the Lie algebra $\mathfrak{h}(M, J)$ of holomorphic vector fields found by Matsushima [28], or the Futaki invariant [17], involve the following subset of $\mathfrak{h}(M, J)$ :
$$\mathfrak{h}_{0}(M, J)=\{X \in \mathfrak{h}(M, J), \exists p \in M \mid X(p)=0\} .$$
On a Kähler manifold (or orbifold), $\mathfrak{h}_{0}(M)$ form a Lie subalgebra of the Lie algebra $\mathfrak{h}(M, J)$ (see for instance [24], Theorem 1). Therefore, it will be natural to assume that $\mathfrak{h}_{0}(M, J)=\{0\}$, to ensure that said obstructions do not appear.

This will be the case if the group of automorphisms of the $(M, J)$ is discrete. However, it is not a necessary condition; if $M$ is a torus, obtained as the quotient of $\mathbb{C}^{2}$ by a lattice, we do have $\mathfrak{h}_{0}(M)=\{0\}$, as it turns out in this case that all holomorphic vector fields are parallel.

The existence of canonical metrics on a given Kähler manifold is an open problem in general. As a consequence, the construction of classes of examples through gluing methods has been the focus of many works. For instance, Arezzo and Pacard [2, 3] have obtained constant scalar curvature Kähler (cscK) metrics on blow-up of cscK manifolds or orbifolds; Arezzo, Lena and Mazzieri have generalized these methods to resolutions of compact orbifolds with isolated singularities; Biquard and Rollin [8] have studied smoothings of canonical singularities, generalizing results by Spotti [42] on smoothings of $A_{1}$ singularities in the Kähler-Einstein case. In the case of extremal metrics, one may cite the works of Arezzo, Pacard and Singer [4] or Szekelyhidi [45, 46].

Another aspect of the existence problem for extremal metrics is its generalisation to almost-Kähler manifolds. These are symplectic manifolds $(M, \omega)$ endowed with a compatible almost-complex structure, that is not assumed to be integrable. The space $\mathcal{A} \mathcal{C}_{\omega}$ of almost complex structures is known to be a contractible Fréchet space, endowed with a natural Kähler structure. The action of the group of Hamiltonian symplectomorphisms acts on $\mathcal{A} \mathcal{C}_{\omega}$ by pullback. The key observation, due to Donaldson [14] (generalizing Fujiki's work [16] to the non-integrable setting), is that this action is Hamiltonian, with moment map given by the Hermitian scalar curvature of $(M, \omega, J)$, which is to say the trace of the curvature of the Chern connection on the anticanonical bundle.

Thus, the suitable reframing of the problem is then the study of the functional
$$J \in \mathcal{A} \mathcal{C}_{\omega} \mapsto \int_{M}\left(s^{\nabla}(J)\right)^{2} \frac{\omega^{m}}{m!},$$
which coincide with the Calabi functional in the Kähler case. In this direction, Lejmi [25] has generalised many notions linked to the existence problem of canonical metrics, and its relation to K-stability, such as the Futaki invariant. In another direction, Weinkove et al. [48, 11] study the Calabi-Yau equation on an almost-Kähler 4-manifold $(M, \omega, J)$.

\subsection*{1.2 Statement of results.}

Let $\left(M^{4}, \omega_{M}, J_{M}\right)$ be a compact Kähler orbifold with isolated singularities of type $A_{1}$, denoted $p_{1} \ldots, p_{\ell}$. This means that $M$ is endowed with a holomorphic atlas that maps neighborhoods of the $p_{i}$ to neighborhoods of 0 in $\mathbb{C}^{2} / \mathbb{Z}_{2}$.

Such orbifold surfaces, and more generally surfaces with canonical singularities, arise naturally by global quotient constructions, as well as in the context of pluricanonical Kodaira 'embeddings' of surfaces of general type. Such maps are obtained by contraction of divisors of self-intersection -2 in a surface of general type, which results in canonical singularities.

In section 3, we detail the construction of a family of smooth symplectic manifolds $M_{\varepsilon}$ indexed by a parameter $\varepsilon \in\left(0, \varepsilon_{0}\right)$, called a family of smoothings of the orbifold $\left(M, \omega_{M}\right)$. We will obtain these smoothings by a symplectic connected sum between $M$ and an ALE Kähler model $\left(X \simeq T^{*} S^{2}, J_{X}, \omega_{X}\right)$, Ricci flat, and with exact symplectic form $\omega_{X}$. The construction of this ALE metric is detailed in the Annex.

For now, we simply highlight the fundamental properties of the smoothing.
\begin{itemize}
\item[1.] The manifold $M_{\varepsilon}$ will split into $M_{\varepsilon}=\left(M \backslash \cup_{i} B\left(p_{i}, r(\varepsilon)\right)\right) \cup K_{\varepsilon}$, where $K_{\varepsilon}$ is diffeomorphic to a compact neighborhoods $\tilde{K}_{\varepsilon}$ of the zero section in $T^{*} S^{2}$. Moreover $r(\varepsilon)$ goes to 0 as $\varepsilon$ goes to 0, and $T^{*} S^{2}=\cup_{\varepsilon} \tilde{K}_{\varepsilon}$.
\item[2.] $M_{\varepsilon}$ is endowed with a symplectic form $\omega_{\varepsilon}$ such that, on the one hand, the injection $(M)$ $\cup_{i} B\left(p_{i}, r(\varepsilon)\right) \hookrightarrow M_{\varepsilon}$, sends $\omega_{M}$ to $\omega_{\varepsilon}$, and, on the other hand, the diffeomorphism $\psi_{\varepsilon}: K_{\varepsilon} \rightarrow \tilde{K}_{\varepsilon}$ sends $\varepsilon^{-2} \omega_{\varepsilon}$ to $\omega_{X}$.
\end{itemize}

From these properties, we will see in Lemma 15 that the manifolds $M_{\varepsilon}$ are all diffeomorphic, and actually symplectomorphic. Indeed, there is a canonical injection
$$H_{c}^{2}\left(M \backslash\left\{p_{1}, \ldots, p_{\ell}\right\}\right) \hookrightarrow H^{2}\left(M_{\varepsilon}, \mathbb{R}\right)$$
that sends $\left[\omega_{M}\right]$ to $\left[\omega_{\varepsilon}\right]$. In this sense, the cohomology classes of $\left[\omega_{\varepsilon}\right]$ all agree.
Furthermore, the identifications of regions of $M_{\varepsilon}$ with regions of $M$ and $X$ enable us to make sense of the convergence, when $\varepsilon$ goes to zero, of sequences of functions (or tensors) $f_{\varepsilon}: M_{\varepsilon} \rightarrow \mathbb{R}$ on compact sets of $M^{*}:=M \backslash\left\{p_{1}, \ldots, p_{\ell}\right\}$ on the one hand, and on compact sets of $X$ on the other hand.

Making this construction precise is the object of section 3. In this situation, we obtain the following result.

Theorem 1. Assume that $(M, J)$ admits no nontrivial holomorphic vector fields that vanish somewhere on $M$, and that $\left(M, \omega_{M}, J_{M}\right)$ is Kähler, of constant scalar curvature. For a positive parameter $\varepsilon$ small enough, we endow the symplectic manifolds $\left(M_{\varepsilon}, \omega_{\varepsilon}\right)$ with a family of smooth compatible almost-Kähler structures $J_{\varepsilon}, g_{\varepsilon}$ of constant Hermitian scalar curvature, such that, when $\varepsilon$ goes to zero,
\begin{itemize}
\item[-] The sequence of almost complex structures $J_{\varepsilon}$ converges, in $\mathcal{C}^{k, \alpha}$-norm, to the orbifold complex structure $J_{M}$, on every compact set of $M^{*}$, for every $k \in \mathbb{N}$.
\item[-] The pushed-forward almost complex structures $\left(\psi_{\varepsilon}\right)_{*} J_{\varepsilon}$ converges, in any $\mathcal{C}^{k, \alpha}$-norm, to the ALE complex structure $J_{X}$, on every compact set of $X$, for every $k \in \mathbb{N}$.
\end{itemize}

Remark 2. In [8], the same result is obtained in the case where $J$ in integrable.
However, the methods presented here are new. In usual gluing methods, the deformation of the approximate solution into a canonical metrics is obtained by adding a potential function. The $\partial \bar{\partial}$ -lemma makes such an approach natural in the Kähler setting. As we will see, this approach does not work so well in the almost-Kähler setting. In dimension 4, 'almost-Kähler potentials' have been used by Weinkove [48] in his study of the Calabi-Yau equation on almost-Kähler manifolds, and by Lejmi [26]. However, this method involves the use of pseudo-differential operators.

To prove our result, we will instead turn to an approach inspired by Fujiki [16] and Donaldson's [14] moment map picture for canonical metrics.

Besides the almost-Kähler setting, an element of novelty here is that the cohomology class of the $\omega_{\varepsilon}$ is different from the one obtained with gluing techniques like Arezzo and Pacard's. On blow-ups, constant curvature metric are usually obtained in a class of the form
$$\Omega=[\omega]-\sum_{i} \varepsilon^{2} \lambda_{i}\left[E_{i}\right],$$
where the $\left[E_{i}\right]$ are Poincaré-dual to the holomorphic exceptional divisor, and the $\lambda_{i}$ are positive coefficients. Instead, in our construction, the zero section of $T^{*} S^{2}$ is included in the compact sets $\tilde{K}_{\varepsilon}$, thus, via the identification $\tilde{K}_{\varepsilon} \rightarrow K_{\varepsilon} \subset M_{\varepsilon}$, yields a Lagrangian sphere $S_{\varepsilon}$ :
$$\left[\omega_{\varepsilon}\right] \cdot\left[S_{\varepsilon}\right]=0 .$$

This last observation enables us to extend another part of the results obtained by Biquard and Rollin in [8], namely the existence of a family of Hamiltonian stationary spheres corresponding to our family of metrics $\hat{g}_{\varepsilon}$. Let $(M, \omega, J, g)$ be a Kähler (or almost-Kähler) manifold. A Hamiltonian stationary surface is a Lagrangian surface $L$ which is a critical point of the area functional under Hamiltonian deformations, which is to say that, for any smooth function $F \in \mathcal{C}^{\infty}(M)$, we have
$$\frac{d}{d s}{ }_{\mid s=0} \operatorname{Vol}_{g}\left(\exp \left(s X_{F}\right)(L)\right)=0$$
where $\exp \left(s X_{F}\right)$ denotes the flow of the Hamiltonian vector field $X_{F}$. Such surfaces have been introduced and studied by Oh in [37, 36]; new examples generalizing Oh's have been obtained by Joyce, Lee and Schoen in [20]. Schoen and Wolfson [41] have studied the existence of Lagrangian surfaces that minimize the area.

In this direction, we obtain:
Theorem 3. On $\left(M_{\varepsilon}, \omega_{\varepsilon}, J_{\varepsilon}\right)$, for $\varepsilon$ small enough, the Lagrangian sphere $S_{\varepsilon}$ admits a Hamiltonian deformation that is a Hamiltonian stationary 2-sphere for the metric $g_{\varepsilon}$.

\subsection*{1.3 Outline of the method.}

Let us now flesh out some details of the gluing construction. Following the gluing methods introduced by Arezzo and Pacard in [2], we seek to endow a smooth manifold $M_{\varepsilon}$, obtained from $M$ by a connected sum construction with a suitable asymptotically locally euclidean (ALE) model $X$, with a constant Hermitian curvature structure.

For such a construction to work, the ALE surface $X$ needs to be asymptotic to $\mathbb{C}^{2} / \mathbb{Z}_{2}$, in the sense that the Riemannian metric and complex structure on $X$ converge to the Euclidean ones $J_{0}, g_{0}$ on $\mathbb{C}^{2} / \mathbb{Z}_{2}$ fast enough. This ALE model will be provided by smoothings
$$C_{\varepsilon}=\left\{z \in \mathbb{C}^{3}, z_{1}^{2}+z_{2}^{2}+z_{3}^{2}=\varepsilon^{2}\right\}$$
of the quotient singularity $\mathbb{C}^{2} / \mathbb{Z}_{2}$, which we identify to the cone
$$C=\left\{z \in \mathbb{C}^{3}, z_{1}^{2}+z_{2}^{2}+z_{3}^{2}=0\right\} .$$
For $\varepsilon>0$, these are diffeomorphic to $T^{*} S^{2}$, which is endowed with Eguchi-Hanson's Ricci-flat metric and a complex structure that is a deformation of the one obtained when blowing up the quotient singularity $\mathbb{C}^{2} / \mathbb{Z}_{2}$. We refer to the Annex for more details about the ALE model.

Remark 4. The minimal resolution of the $A_{1}$ singularity is an hyperKähler manifold biholomorphic to $T^{*} \mathbb{C} P 1$. Our choice here consists of taking a different complex structure in the hyperKähler family. This observation is the starting point of the construction of Hamiltonian stationary spheres later on.

The next step is to glue together $M$ and $X$ in a generalized connected sum, that is a smooth, compact manifold: we replace a very small neighborhood of each singularity $p_{i}$ of $M$ by a suitably scaled-down 'ball' of large radius in $X$. Performing this construction in Darboux charts, we ensure that the obtained smooth manifold $M_{\varepsilon}$ is naturally endowed with a symplectic form $\omega_{\varepsilon}$.

Then, we endow $M_{\varepsilon}$ with an almost-Kähler structure $\left(\omega_{\varepsilon}, \hat{J}_{\varepsilon}, \hat{g}_{\varepsilon}\right)$ by patching together the model structures on $M$ and $X$. This 'patching' comes at the price of the integrability of the obtained almostcomplex structure $\hat{J}_{\varepsilon}$. Then, we perturb this approximate solution into an almost-Kähler structure of constant Hermitian scalar curvature. This requires to depart from 'usual' gluing methods.

Since we are not working on a Kähler manifold, the Ricci and scalar curvature stemming from the Riemannian metric $\hat{g}_{\varepsilon}:=\omega_{\varepsilon}\left(\cdot, \hat{J}_{\varepsilon} \cdot\right)$ do not retain the same pleasant properties they have on a Kähler manifold. As a consequence, we study the Hermitian scalar curvature instead; this is motivated by the moment-map point of view of Donaldson [14].

Observe, moreover, that we have no appropriate notion of Kähler potential to perturb the symplectic form. Indeed, as was observed by Delanoe [12], symplectic forms of the form
$$\omega_{f}:=\omega_{\varepsilon}+d \hat{J}_{\varepsilon} d f$$
are not $J_{\varepsilon}$-invariant, thus do not provide an almost-Kähler structure on $M_{\varepsilon}$. Instead, we are going to fix the symplectic form $\omega_{\varepsilon}$ and modify the almost complex structure $\hat{J}_{\varepsilon}$ along directions orthogonal to the Hamiltonian action, in a way that preserves compatibility with $\omega_{\varepsilon}$.

This method allows us to rewrite the condition of constant Hermitian curvature as an elliptic fourth order PDE on $M_{\varepsilon}$. To solve it, we resort to a fixed-point method in suitable functional Banach spaces. It turns out that the linearisation of our PDE rewrites as the sum of the Lichnerowiz operator on $M_{\varepsilon}$ and an error term. Up to proper estimates of this error term, we may thus use the nice properties of the Lichnerowicz operators on the model spaces, namely the orbifold $M$ and the ALE surface $X$, to study the linearisation. This last step allows us to find a unique solution through an analogue of the inverse function theorem.

As far as Theorem 2 is concerned, the key observation is that the zero section $S$ of $T^{*} S^{2}$ is Lagrangian for the symplectic form $\omega_{X}$; moreover it corresponds to the (holomorphic) zero section of $T^{*} \mathbb{C} P^{1}$ for another choice of complex structure in the hyperKahler family; it is then a consequence of Wirtinger's inequality that $S$ is minimal for Eguchi-Hanson's metric, which coincides with Stenzel's metric as a Riemannian structure.

This property is preserved when constructing the approximate solution: we obtain a Lagrangian minimal 2-sphere in $M_{\varepsilon}$. The idea is then to perturb $S$ inside its homology class by Hamiltonian transformation, and to use the implicit function theorem to obtain Hamiltonian-stationary representants for the nearby metrics $\hat{g}_{\varepsilon}$ obtained through the gluing process.

\subsection*{1.4 Examples and perspectives.}

Let us exhibit some classes of singular surfaces to which our construction may apply.
As was pointed out to us by R. Dervan, this construction applies to surfaces with $A_{1}$ singularities and ample canonical class, since such surfaces have negative first Chern class and thus are guaranteed to have a Kähler-Einstein metric (see Aubin [5], and Kobayashi [21] for surfaces of general type) and no nontrivial holomorphic vector fields (see [22], Chapter III, Theorem 2.1).

In this direction, Miranda, in [32], studies a special case of complex surfaces with ample canonical bundle, that admit no smoothing. Thus, we may apply our construction, and these examples are outside the framework of the smoothing theorem obtained by Biquard and Rollin [8].

Similarly, Catanese, in [9], exhibits a criterion for algebraic varieties with finite automorphism group, under which they admit no smoothing. His theorem encompasses the previously obtained obstructed examples, and the surfaces satisfying to this criterion have rational double points as singularities, and so do all of their deformations.

Finally, looking at the assumptions of the main theorem, some questions arise naturally, that open some perspectives:
\begin{itemize}
\item[-] Could we extend this construction to a wider range of singularities, such as canonical singularities ?
\item[-] What if the base manifold $M$ admits nontrivial holomorphic vector fields ? For instance, could we obtain a result in the line of [44] in our context?
\end{itemize}

Another question that arises is that of higher dimensions. However, in this case, it has been proven by Hein, Radeasconu and Suvaina in [19] that an ALE model asymptotic to a singularity $\mathbb{C}^{m} / G$ has to be isomorphic to a deformation of a resolution of the quotient singularity $\mathbb{C}^{m} / G$. However, by Schlessinger's rigidity theorem [40], such singularities are actually rigid; as a consequence, in complex dimension greater than 3, the only available ALE model, up to biholomorphism, is the resolution of the singularity.

However, the double point in $\mathbb{C}^{m}$, identified to the cone
$$\mathcal{C}=\left\{z \in \mathbb{C}^{m}, \sum_{i=1}^{m} z_{i}^{2}=0\right\}$$
still admits smoothings
$$\mathcal{S}_{\varepsilon}=\left\{z \in \mathbb{C}^{m}, \sum_{i=1}^{m} z_{i}^{2}=\varepsilon\right\}$$
that can be identified to the cotangent of the sphere $T^{*} S^{m}$. Stenzel's construction [43] endows such smoothings with an ALE Ricci-flat metric. We could thus consider a similar construction, where the base $M$ has such conical singularities.

\subsection*{1.5 Organisation of the paper.}

In Section 2, we begin with recalling the general properties of almost-Kähler manifolds that are needed in the paper; we discuss especially the space of amost complex structures compatible with a given symplectic form, as well as the properties of the Hermitian scalar curvature. In Section 3, we show the existence of Darboux charts around singularities in $M$ on the one hand, and outside a compact in $X$ on the other hand, in which the gluing is performed. Section 4 is devoted to the construction of a compatible almost complex structure on $M_{\varepsilon}$, as well as estimates on its Nijenhuis tensor. In Section 5. we tackle the analysis of the equation we want to solve on $M_{\varepsilon}$. The idea is to reduce the problem to a fixed-point problem in suitable Banach spaces, in the spirit of the Inverse Function Theorem, and to compare the intervening operators to the well-understood models on $M$ and $X$. Finally, Section 6 is concerned with the proof of Theorem 2.

Acknowledgements. I would like to thank my advisors Yann Rollin and Gilles Carron for their invaluable help and support during the maturation of this paper. I would also like to thank the CIRGET for their kind welcome and the stimulating work environment; special thanks to Vestislav Apostolov, who made this visit possible.

\section*{2 Almost-Kähler preliminaries.}

Our construction will lead us into the realm of almost-Kähler geometry on a symplectic manifold. For the sake of completeness, we introduce here all the notions and identities that will appear in the main construction.

Let $(V, \omega)$ be a symplectic manifold. First, we describe the space of almost complex structures compatible with $\omega$ and how it relates to Kahler classes in Kahler geometry. Then, we discuss several notion of scalar curvature on the almost Kähler manifold $(V, \omega, J)$, and explain why the Hermitian scalar curvature is most suited to our purposes.

\subsection*{2.1 Almost complex structures compatible with a symplectic form.}

First we give some background on which (almost)-complex structures are compatible with a given symplectic form. Let $(V, \omega)$ be a symplectic manifold. We consider the set of all almost complex structures on $V$ compatible with $\omega$ :
$$\mathcal{A} \mathcal{C}_{\omega}=\left\{J \text { section of } \operatorname{End}(T V), \text { such that } J^{2}=-I d, \text { and } g_{J}:=\omega(\cdot, J \cdot) \text { is a Riemann metric }\right\} .$$
Its tangent space at a point $J \in \mathcal{A C}_{\omega}$ is then given by:
$$T_{J} \mathcal{A} \mathcal{C}_{\omega}=\{A \text { section of } \operatorname{End}(T V) \text { such that } A J=-J A, \omega(A \cdot, \cdot)+\omega(\cdot, A \cdot)=0\} .$$
Let $\mathcal{G}_{\omega}$ be the space of sections of $\operatorname{Aut}(T V)$ that preserve $\omega$,
$$\mathcal{G}_{\omega}=\Gamma(\operatorname{Aut}(T V, \omega))=\{\gamma: V \rightarrow \operatorname{Aut}(T V), \omega(\gamma X, \gamma Y)=\omega(X, Y)\} .$$
It can be understood as an infinite-dimensional Lie group, whose Lie algebra is then :
$$\mathcal{L}_{\omega}=\Gamma(\operatorname{End}(T V, \omega))=\{a: V \rightarrow \operatorname{End}(T V), \omega(a X, Y)+\omega(X, a Y)=0\} .$$
Then we have the following proposition, relating any to a.c.s. compatible with $\omega$ :
Proposition 5. The action of $\mathcal{G}_{\omega}$ on $\mathcal{A} \mathcal{C}_{\omega}$ by conjugation is transitive. In particular, given $J_{1}$ and $J_{2}$ in $\mathcal{A} \mathcal{C}_{\omega}$, there is an $a \in \mathcal{L}_{\omega}$ such that
$$J_{2}=\exp (a) J_{1} \exp (-a) ;$$
moreover, the section $A$ is unique if we assume it anticommutes with $J_{1}$ and $J_{2}$.
Conversely, for any $J \in \mathcal{A C}_{\omega}$, any tangent $\dot{J} \in T_{J} \mathcal{A} \mathcal{C}_{\omega}$ can be written as the tangent vector to a curve of this form:
$$\dot{J}=\left.\frac{d}{d t}\right|_{t=0} \exp (t a) J \exp (-t a),$$
where $a=-\frac{1}{2} J \dot{J}$.

Proof. Observe that $P=-J_{1} J_{2}$ is symmetric positive definite with respect to both associated metrics $g_{1}=\omega\left(\cdot, J_{1} \cdot\right)$ and $g_{2}=\omega\left(\cdot, J_{2} \cdot\right)$. Thus we may write it $P=B^{2}$ for a symmetric definite positive matrix $B$. Write $B=\exp (b)$ and observe that $b$ anticommutes to both $J_{1}$ and $J_{2}$ to conclude. \(\square\)

\subsection*{2.2 Action of Hamiltonian vector fields on $\mathcal{A} \mathcal{C}_{\omega}$.}

In the original construction proposed by Arezzo and Pacard, the "connected sum" on which the operation takes place is a complex manifold in a natural way, and one looks for a canonical metric in a Kähler class naturally obtained when performing the gluing.

Here we will lose this property on the connected sum. However, we will see that we can still endow it with a natural (family of) symplectic 2-forms. As a consequence, it will be more natural to keep this symplectic form fixed and move the obtained almost complex structure in $\mathcal{A} \mathcal{C}_{\omega}$.

In this section we explain ow one might perform this operation on a symplectic manifold $(V, \omega)$, and how, in the integrable case, this relates to the more traditional use of the $d d^{c}$-lemma to move around in a given Kähler class.

Since the natural structure on $V$ is the symplectic form $\omega$, it makes sense to use Hamiltonian vector fields to move the other structures around. Thus, to a smooth function $f$ on $V$, we associate the Hamiltonian vector field $X_{f}$ defined by
$$d f=\omega\left(X_{f} \cdot, \cdot\right) .$$
A Hamiltonian vector field $X_{f}$ induces a variation $a$ of complex structures via the Lie derivative:
$$a=\frac{1}{2} \mathcal{L}_{X_{f}} J .$$
This variation is compatible with $\omega$ in the following sense:
Lemma 6. The variation of complex structure $a$ is in $\mathcal{L}_{\omega}$. Moreover, a anticommutes to $J$.
Proof. We must first check that $\omega(a X, Y)+\omega(X, a Y)=0$. To do this, we use that, since $X_{f}$ is hamiltonian, it preserves $\omega$, i.e.
$$\mathcal{L}_{X_{f}} \omega=0 .$$
Thus, since $g(X, Y)=\omega(X, J Y)$, we have that
$$\mathcal{L}_{X_{f}} g(X, Y)=\omega\left(X, \mathcal{L}_{X_{f}} J Y\right) .$$
But $\mathcal{L}_{X_{f}} g$ is a symmetric tensor, thus
$$\begin{aligned}
\mathcal{L}_{X_{f}} g(X, Y) & =\mathcal{L}_{X_{f}} g(Y, X) \\
& =\omega\left(Y, \mathcal{L}_{X_{f}} J X\right) \\
& =-\omega\left(\mathcal{L}_{X_{f}} J X, Y\right) .
\end{aligned}$$

As for anticommuting with $J$, we have that
$$\begin{aligned}
2 a J X & =\left(\mathcal{L}_{X_{f}} J\right) J X \\
& =-\mathcal{L}_{X_{f}} X-J \mathcal{L}_{X_{f}}(J X) \\
& =-J\left(\mathcal{L}_{X_{f}} J\right) X
\end{aligned}$$
for any $X$. \(\square\)

Thus, from Proposition 5, we see that for any $t$, the almost complex structure
$$J_{t}=\exp (-t a) J \exp (t a)$$
is in $\mathcal{A} \mathcal{C}_{\omega}$. To $f \in \mathcal{C}^{\infty}(V)$, we may therefore associate
$$J_{f}:=J_{1} .$$

As an heuristical aparté, let us now briefly explain how this construction can be related to the $d d^{c}$-lemma in Kähler geometry.

The Lie group $\operatorname{Ham}(V, \omega)$ of exact symplectomorphisms on a symplectic manifold $(V, \omega)^{1}$ acts on $\mathcal{A} \mathcal{C}_{\omega}$ by pullback, and this action preserves $\omega$. Through the Hamiltonian construction, we identify the Lie algebra of $\operatorname{Ham}(V, \omega)$ with the set $E_{0}$ of smooth functions on $V$ with zero integral.

With this identification, the infinitesimal action is
$$P: f \in E_{0} \mapsto \mathcal{L}_{X_{f}} J \in T_{J} \mathcal{A} \mathcal{C}_{\omega} .$$

Observe that if $J, J^{\prime}$ are integrable complex structures, such that $J^{\prime}=\phi^{*} J$ for some diffeomorphism $\phi$, then the associated Riemannian metric is given by:
$$g\left(J^{\prime}, \omega\right)=\phi^{*} g\left(J,\left(\phi^{-1}\right)^{*} \omega\right) ;$$
so if $\phi \in \operatorname{Ham}(V, \omega)$, these two metrics are isometric and have the same scalar curvature. This construction does not help to find constant scalar curvatures.

However, we may consider the complexified action instead. We may not be able to complexify the Lie group, but we can consider the complexified Lie algebra of zero-mean smooth functions with values in $\mathbb{C}$. This yields a complexified infinitesimal action
$$P: E_{0}^{\mathbb{C}}=\left\{H \in \mathcal{C}^{\infty}(V, \mathbb{C}), \int_{V} H \omega^{2}=0\right\} \rightarrow T_{J} \mathcal{A} \mathcal{C}_{\omega} .$$
The resulting foliation can be understood as the orbits of $\operatorname{Ham}^{\mathbb{C}}(V, \omega)$.
The (infinitesimal) action of a purely imaginary $\sqrt{-1} f$ is then given by $J P(f)=J \mathcal{L}_{X_{f}} J=\mathcal{L}_{J X_{f}} J$. Thanks to (5), we see that, at the riemannian level, this amounts to fixing $J$ and flowing $\omega$ along $-J X_{f}$. The obtained variation is then
$$-\mathcal{L}_{J X_{f}} \omega=-d \iota_{J X_{f}} \omega=2 i \partial \bar{\partial} f .$$
so this construction is equivalent to moving $\omega$ in its Kähler class. Via pullback by a time-one Hamiltonian flow, we have
$$\phi_{f}^{*}(\omega+d J d f, J)=\left(\omega, \phi_{f}^{*} J\right) .$$

It would seem natural to adopt the same construction here; that is detailed in Szekelyhidi's paper [44]. However, as $J$ is not integrable, we run into an obstacle: the obtained almost complex structure $\phi_{f}^{*} J$ is not compatible with $\omega$.

\footnotetext{
${ }^{1} \operatorname{Ham}(V, \omega)$ can be understood as the set of symplectomorphisms which are time-one value of the flow of a timedependent Hamiltonian vector field.
}

Lemma 7. The symplectic form
$$\omega_{f}:=\omega-d J d f$$
is $J$ - invariant if, and only if, $J$ is integrable.
Proof. On the one hand we have, for any $X, Y$,
$$\begin{aligned}
(d J d f)(X, Y) & =X \cdot(J d f(Y))-Y \cdot(J d f(X))-J d f([X, Y]) \\
& =-X \cdot(J Y) \cdot f+Y \cdot(J X) \cdot f+J[X, Y] \cdot f .
\end{aligned}$$
On the other hand,
$$\begin{aligned}
(d J d f)(J X, J Y) & =J X \cdot d f(Y)-J Y \cdot d f(X)-J d f([J X, J Y]) \\
& =-J X \cdot Y \cdot f+J Y \cdot X \cdot f+J[J X, J Y] \cdot f .
\end{aligned}$$
As a consequence, the $J$-anti-invariant parf of $d J d f$ is
$$(d J d f)(X, Y)-(d J d f)(J X, J Y)=-4 J N_{J}(X, Y),$$
where $N_{J}$ denotes the Nijenhuis tensor of the almost-complex structure $J$ :
$$N_{J}(X, Y)=\frac{1}{4}([J X, J Y]-J[J X, Y]-J[X, J Y]-[X, Y]),$$
which, by the celebrated Newlander-Niremberg theorem, vanishes iff $J$ is integrable. \(\square\)

Thus, in the case where $J$ is not integrable, we rather use the exponential map construction, which does not move $J$ in the complexified orbits, but does retain the complexified action at the infinitesimal level:
$$\left.\frac{d}{d t}\right|_{t=0} J_{t}=\left.\frac{d}{d t}\right|_{t=0} \exp \left(-t \mathcal{L}_{X_{f}} J\right) J=J \mathcal{L}_{X_{f}} J$$
which coincide $J P(f)$ obtained earlier.

\subsection*{2.3 The Hermitian scalar curvature}

There are several competing notions of curvature on the almost-Kähler manifold $(V, \omega, J)$. We now discuss them and pick the most natural choice; more details can be found in Apostolov and Draghici's survey [1].

First, one can consider the different Riemannian curvature tensors derived from the metric $g_{J}$ : the Riemannian curvature tensor $\operatorname{Rm}_{g_{J}}$, the Ricci curvature $\operatorname{Ric}_{g_{J}}$ and the scalar curvature $s_{g_{J}}$. From these, one can define the Ricci form $\rho:=\operatorname{Ric}_{g_{J}}(J \cdot, \cdot)$. In the Kähler case, the complex structure is parallel, which add symmetries to Rm, and one can show that the Ricci form is closed of type (1, 1), and that its cohomology class is exactly the first Chern class of $V$. However, since $D J$ is not assumed to vanish, where $D$ denotes the Levi-Civita connection of $g_{J}$, the Ricci form is not necessarily closed or $J$-invariant; in particular, it is not a representant of the cohomology class $2 \pi c_{1}(V)$.

On the other hand, the almost complex structure $J$ allows us to see each tangent space $T_{p} V$ as a complex vector space. We will denote the resulting complex bundle by $(T V, J)$. It is identified $T^{1,0} V$ via
$$\begin{aligned}
X \in( & T V, J) \mapsto X^{1,0}:=\frac{1}{2}(X-i J X) \in T^{1,0} V \subset T V \otimes \mathbb{C} \\
& Z+\bar{Z} \hookleftarrow Z
\end{aligned}$$

We endow $(T V, J)$ with a Cauchy-Riemann operator defined by
$$\bar{\partial}_{X}^{(T V, J)} Y=2 \Re \mathfrak{e}\left(\left[X^{0,1}, Y^{1,0}\right]^{1,0}\right)$$
which, in terms of the Levi-Civita connection of $g_{J}$, rewrites
$$\bar{\partial}_{X}^{(T V, J)} Y=\frac{1}{2}\left(D_{X} Y+J D_{J X} Y\right)-\frac{1}{2} J\left(D_{X} J\right) Y .$$

Together with the Hermitian inner product $h_{J}=\frac{1}{2}\left(g_{J}-i \omega\right)$, this operator determines a Chern connection $\nabla^{J}$ on $T V$ such that $\nabla^{J,(0,1)}=\bar{\partial}^{(T V, J)}$. Since the almost Kähler structure is not assumed to be integrable, the Chern connection does not necessarily coincide with the Levi-Civita connection. Instead, both are related by
$$\nabla_{X} Y=D_{X} Y-\frac{1}{2} J\left(D_{X} J\right) Y .$$
Remark: The torsion of this Chern connection is given by the Nijenhuis tensor $N_{J}$.
The top exterior power $K_{J}^{*}:=\Lambda^{m}(T V, J)$, called the anticanonical bundle, inherits a Hermitian product and a Hermitian connection from this construction. Then, the curvature of the Chern connection on $K_{J}^{*}$ is of the form $i \rho^{\nabla}$ where $\rho^{\nabla}$ is a real, closed 2-form, and moreover, is a representant of $2 \pi c_{1}(V)$. We call it the Hermitian Ricci form.

The Hermitian scalar curvature $s^{\nabla}$ is then defined to be its trace with respect to $\omega$ :
$$s^{\nabla}=2 \Lambda \rho^{\nabla} .$$

On a Kähler manifold, i.e. when the almost complex structure is integrable, all those notions of Ricci and scalar curvature coincide. To express their relationship in the almost-Kähler setting, we need to introduce yet another notion of curvature. Observe that the (4,0)-Riemannian curvature tensor $\mathrm{Rm}_{g_{J}}$ can be identified to a symmetric endomorphism $\Lambda^{2} V \rightarrow \Lambda^{2} V$ via
$$\operatorname{Rm}_{g_{J}}(\alpha \wedge \beta)(X, Y):=\operatorname{Rm}_{g_{J}}\left(\alpha^{\sharp}, \beta^{\sharp}, X, Y\right) .$$
The twisted Ricci form, or *-Ricci form, is then defined as the image of the symplectic form by this endomorphism:
$$\rho^{*}=R_{g_{J}}(\omega),$$
and its trace with respect to $\omega$ is the *-scalar curvature :
$$s^{*}=2 \Lambda \rho^{*}=2\left(R_{g_{J}}(\omega), \omega\right) .$$
Then we have the following identites, which are proven in [1].
Proposition 8. The Riemannian, Hermitian and twisted Ricci form are related as follows:
$$\begin{aligned}
\rho^{\nabla}(X, Y) & =\rho^{*}(X, Y)-\frac{1}{4} \operatorname{tr}\left(J D_{X} J \circ D_{Y} J\right), \\
\rho^{*}(X, Y) & =\frac{1}{2}\left(\operatorname{Ric}_{g_{J}}(J X, Y)-\operatorname{Ric}_{g_{J}}(X, J Y)\right)+\frac{1}{2}\left(\left(D D^{*} J\right) X, Y\right) .
\end{aligned}$$
As far as the scalar curvatures are concerned, we have
$$s^{\nabla}=s_{g_{J}}+\frac{1}{2}|D J|^{2}=s^{*}-\frac{1}{2}|D J|^{2}=\frac{1}{2}\left(s_{g_{J}}+s^{*}\right) .$$
In this last formula, the norm of $D J$ is given by $|D J|^{2}=-\frac{1}{2} \sum_{i} \operatorname{tr}\left(D_{e_{i}} J \circ D_{e_{i}} J\right)$, with $\left\{e_{i}\right\}_{i}$ a local orthonormal frame for $g_{J}$.

In the almost Kähler context, the Hermitian Ricci form and the Hermitian scalar curvature are natural substitutes to their Riemannian counterparts.

We will thus use $s^{\nabla}$ as a generalization to our context of the Riemannian scalar curvature. Of course, the anticanonical bundle and Chern connection, hence the Hermitian scalar curvature depends on the almost complex structure we use on $V$. Hence, we will be interested in the operator
$$\begin{aligned}
s^{\nabla}: \mathcal{A} \mathcal{C}_{\omega} & \longrightarrow \mathcal{C}^{\infty}(V) \\
J & \longmapsto s^{\nabla}(J) .
\end{aligned}$$
First variation of $s^{\nabla}$. The first variation of the Hermitian scalar curvature operator with respect to $J \in \mathcal{A C}_{\omega}$ is given by the following formula, proven by Mohsen in his Master thesis [33]:

Proposition 9. Define a curve $J_{t}$ in $\mathcal{A C}{ }_{\omega}$ by
$$J_{t}=\exp (-t a) J \exp (t a),$$
for $a \in \mathcal{L}_{\omega}$ anticommuting to $J$, and set
$$\dot{J}=\left.\frac{d}{d t}\right|_{t=0} J_{t}$$
the tangent vector at $t=0$. Then the first variation of the Hermitian scalar curvature along the curve $J_{t}$ is given by:
$$\left.\frac{d}{d t}\right|_{t=0} s^{\nabla}\left(J_{t}\right)=\Lambda d(\delta \dot{J})^{b}=-\delta J(\delta \dot{J})^{b}$$
where the codifferential $\delta$ and the musical operator $b$ are taken with respect to the metric $g_{J}=\omega_{\varepsilon}(\cdot, J \cdot)$.
Remark: Recall that the vector field $\delta \dot{J}$ is given in a local orthonormal frame $\left(e_{i}\right)_{i}$ for $g$ by
$$\delta \dot{J}=-\sum\left(D_{e_{i}}^{g} \dot{J}\right)\left(e_{i}\right) .$$
Proof. We follow the proof given in Chapter 9 in [18].
We denote by $g_{t}, h_{t}$ the Riemannian metric and Hermitian inner product on $\left(T V, J_{t}\right)$. Then the isomorphism
$$\exp (-t a):(T V, J) \rightarrow\left(T V, J_{t}\right)$$
preserves $\omega$, hence induces an isomorphism of Hermitian line bundles between $\left(K_{J}^{*}, h\right)$ and $\left(K_{J_{t}}^{*}, h_{t}\right)$.
The strategy is to first compute the connection 1-form $\alpha_{t}$ of the Chern connection on $\left(K_{J_{t}}^{*}, h_{t}\right)$. Then the Hermitian Ricci curvature is given by $\rho^{\nabla^{J_{t}}}=-d \alpha_{t}$, and taking the trace, we get the Hermitian scalar curvature $s^{\nabla^{J}}=2 \Lambda_{t} d \alpha_{t}$. Thus, we need only compute $\dot{\alpha}:=\left.\frac{d}{d t}\right|_{t=0} \alpha_{t}$.

We wish to compute $\dot{\alpha}$ in terms of $\dot{J}$. Let $\left(Z_{1}, \ldots, Z_{m}\right)$ be a local orthonormal frame for $\left(T V, J, h_{J}\right)$. That is,
$$h_{J}\left(Z_{i}, Z_{j}\right)=\delta_{i j} \Leftrightarrow\left\{\begin{array}{l}
g_{J}\left(Z_{i}, Z_{j}\right)=2 \delta_{i j}, \\
\omega\left(Z_{i}, Z_{j}\right)=0 .
\end{array}\right.$$

Then $\left\{Z_{j}^{t}:=\exp (-t a) Z_{j}\right\}_{j=1 \ldots m}$ is an orthonormal frame for $\left(T V, J_{t}, h_{J_{t}}\right)$. In this frame, the connection 1-form $\alpha_{t}$ is given by
$$\alpha_{t}(X)=-i \sum_{j} h_{t}\left(\nabla_{X}^{J_{t}} Z_{j}^{t}, Z_{j}^{t}\right) .$$

We split $\nabla^{J_{t}}$ into its $(0,1)$ and $(1,0)$ parts and observe that
$$h_{t}\left(\left(\nabla^{J_{t}}\right)^{(1,0)} X, Y\right)=-h_{t}\left(X,\left(\nabla^{J_{t}}\right)^{(0,1)} Y\right)$$
thus
$$\alpha_{t}(X)=-i \sum_{j} h_{t}\left(\left(\nabla_{X}^{J_{t}}\right)^{(0,1)} Z_{j}^{t}, Z_{j}^{t}\right)-h_{t}\left(Z_{j}^{t},\left(\nabla_{X}^{J_{t}}\right)^{(0,1)} Z_{j}^{t}\right)$$
Recall that the $(0,1)$ part of $\nabla^{J_{t}}$ is $\bar{\partial}^{\left(T V, J_{t}\right)}$. Thus,
$$\begin{aligned}
\alpha_{t}(X) & =-i \sum_{j} h_{t}\left(\bar{\partial}_{X}^{\left(T V, J_{t}\right)} Z_{j}^{t}, Z_{j}^{t}\right)-h_{t}\left(Z_{j}^{t}, \bar{\partial}_{X}^{\left(T V, J_{t}\right)} Z_{j}^{t}\right) \\
& =-\sum_{j} \omega\left(\bar{\partial}_{X}^{\left(T V, J_{t}\right)} Z_{j}^{t}, Z_{j}^{t}\right) \\
& \left.=\sum_{j} \omega\left(\exp (t a) \bar{\partial}_{X}^{\left(T V, J_{t}\right)} \exp (-t a) Z_{j}, \exp (t a) Z_{j}^{t}\right)\right) \\
& \left.=\sum_{j} \omega\left(\exp (t a) \bar{\partial}_{X}^{\left(T V, J_{t}\right)} \exp (-t a) Z_{j}, Z_{j}\right)\right)
\end{aligned}$$
Now, the Cauchy-Riemann operator $\bar{\partial}^{\left(T V, J_{t}\right)}$ is given by
$$\begin{aligned}
\bar{\partial}_{X}^{\left(T V, J_{t}\right)} Z: & =2 \Re \mathfrak{e}\left(\left[X^{0,1}, Z^{1,0}\right]^{1,0}\right) \\
& =-\frac{1}{4}\left(J_{t} \mathcal{L}_{Z} J_{t}+\mathcal{L}_{J_{t} Z} J_{t}\right)(X) .
\end{aligned}$$
As a consequence,
$$\begin{aligned}
\alpha_{t}(X) & =\frac{1}{4} \sum_{j} \omega\left(\exp (t a) J_{t}\left(\mathcal{L}_{\exp (-t a) Z_{j}} J_{t}\right) X, Z_{j}\right)+\omega\left(\exp (t a)\left(\mathcal{L}_{J_{t} \exp (-t a) Z_{j}} J_{t}\right) X, Z_{j}\right) \\
& =\frac{1}{4} \sum_{j} \omega\left(J \exp (t a) J\left(\mathcal{L}_{\exp (-t a) Z_{j}} J_{t}\right) X, Z_{j}\right)+\omega\left(\exp (t a)\left(\mathcal{L}_{\exp (-t a) J Z_{j}} J_{t}\right) X, Z_{j}\right) .
\end{aligned}$$
We will now rewrite this in terms of the metric $g_{J}$ and its Levi-Civita connection $D$. We will use the local frame $\left\{e_{1}, \ldots, e_{2 m}\right\}:=\frac{1}{\sqrt{2}}\left\{Z_{1}, \ldots, Z_{m}, J Z_{1}, \ldots, J Z_{m}\right\}$; in this frame, the previous expression rewrites
$$\alpha_{t}(X)=-\frac{1}{2} \sum_{k} g_{J}\left(\exp (t a) J\left(\mathcal{L}_{\exp (-t a) e_{k}} J_{t}\right) X, e_{k}\right) .$$
We may express the Lie derivative of $J_{t}$ in terms of $D$ :
$$\begin{aligned}
\left(\mathcal{L}_{\exp (-t a) e_{k}} J_{t}\right) X & =\left(D_{\exp (-t a) e_{k}} J_{t}\right) X+\left[D\left(\exp (-t a) e_{k}\right), J_{t}\right](X) \\
& =\left(D_{\exp (-t a) e_{k}} J_{t}\right) X+D_{J_{t} X}\left(\exp (-t a) e_{k}\right)-J_{t} D_{X}\left(\exp (-t a) e_{k}\right)
\end{aligned}$$
Hence, using $\exp (t a) J_{t}=J \exp (t a)$, we get
$$\begin{aligned}
\alpha_{t}(X) & =-\frac{1}{2} \sum_{k} g_{J}\left(\exp (t a)\left(D_{\exp (-t a) e_{k}} J_{t}\right) X, e_{k}\right) \\
& +\frac{1}{2} \sum_{k} g_{J}\left(\exp (t a) D_{J_{t} X}\left(\exp (-t a) e_{k}\right), e_{k}\right) \\
& -\frac{1}{2} \sum_{k} g_{J}\left(J \exp (t a) D_{X}\left(\exp (-t a) e_{k}\right), e_{k}\right) .
\end{aligned}$$

Taking the derivative with respect to t yields
$$\begin{aligned}
\dot{\alpha}(X)=\frac{1}{2} \sum_{k} & g_{J}\left(a\left(D_{e_{k}} J\right) X, e_{k}\right)-g_{J}\left(\left(D_{a e_{k}} J\right) X, e_{k}\right)+g_{J}\left(\left(D_{e_{k}} \dot{J}\right) X, e_{k}\right) \\
& +g_{J}\left(a D_{J X} e_{k}, e_{k}\right)+g_{J}\left(D_{\dot{J} X} e_{k}, e_{k}\right)-g_{J}\left(D_{J X}\left(a e_{k}\right), e_{k}\right) \\
& -g_{J}\left(J a D_{X} e_{k}, e_{k}\right)+g_{J}\left(J D_{X}\left(a e_{k}\right), e_{k}\right) .
\end{aligned}$$
which rewrites
$$\begin{aligned}
\dot{\alpha}(X) & =\frac{1}{2}(\delta \dot{J})^{b}(X) \\
& -\frac{1}{2} \sum_{k} g_{J}\left(a\left(D_{e_{k}} J\right) X, e_{k}\right)-g_{J}\left(\left(D_{a e_{k}} J\right) X, e_{k}\right) \\
& +\frac{1}{2} \sum_{k} g_{J}\left(\left(D_{J X} a\right) e_{k}, e_{k}\right) \\
& -\frac{1}{2} \sum_{k} g_{J}\left(D_{\dot{J} X} e_{k}, e_{k}\right) \\
& +\frac{1}{2} \sum_{k} g_{J}\left(J\left(D_{X} a\right) e_{k}, e_{k}\right)
\end{aligned}$$
that is
$$\begin{aligned}
\dot{\alpha}(X) & =\frac{1}{2}(\delta \dot{J})^{b}(X) \\
& -\frac{1}{2} \sum_{k} g_{J}\left(a\left(D_{e_{k}} J\right) X, e_{k}\right)-g_{J}\left(\left(D_{a e_{k}} J\right) X, e_{k}\right)-g_{J}\left(D_{X}\left(a e_{k}, e_{k}\right)\right. \\
& +\frac{1}{2} \sum_{k} g_{J}\left(\left(D_{J X} a\right) e_{k}, e_{k}\right) \\
& -\frac{1}{2} \sum_{k} g_{J}\left(D_{\dot{J} X} e_{k}, e_{k}\right) \\
& +\frac{1}{2} \sum_{k} g_{J}\left(\left(D_{X} J a\right) e_{k}, e_{k}\right)
\end{aligned}$$

The first term $\frac{1}{2}(\delta \dot{J})^{b}(X)$ is what we expect. The other terms vanish, for the following reasons:
\begin{itemize}
\item[-] Each $e_{k}$ has norme 1, thus $g_{J}\left(D_{j X} e_{k}, e_{k}\right)=\frac{1}{2}(\dot{J} X)\left(g\left(e_{k}, e_{k}\right)=0\right.$.
\item[-] Since $a$ and $J a$ anticommute to $J$, both these endormorphisms are trace-free, and so are $D_{J X} a$ and $D_{X}(J a)$. Thus, the terms $\sum_{k} g_{J}\left(\left(D_{J X} a\right) e_{k}, e_{k}\right)$ and $\sum_{k} g_{J}\left(\left(D_{X} J a\right) e_{k}, e_{k}\right)$ vanish.
\item[-] Finally, for any $k$, the sum
$$g_{J}\left(\left(D_{e_{k}} J\right)\left(a e_{k}\right), X\right)+g_{J}\left(\left(D_{X} J\right) e_{k}, a e_{k}\right)+g_{J}\left(\left(D_{a e_{k}} J\right) X, e_{k}\right)$$
vanishes, since for any $X, Y, Z$
$$g_{J}\left(\left(D_{Y} J\right)(Z), X\right)+g_{J}\left(\left(D_{X} J\right) Y, Z\right)+g_{J}\left(\left(D_{Z} J\right) X, Y\right)=d \omega(X, Y, Z)=0 .$$
\end{itemize}
Thus we get
$$\left.\frac{d}{d t}\right|_{t=0} \rho^{\nabla}\left(J_{t}\right)=d \dot{\alpha}=\frac{1}{2} d(\delta \dot{J})^{b}(X) .$$

To get the variation, we need to take the trace. Howevern we must be careful: $\Lambda_{t}$ depends on $t$. However, we have, for any 1 -form $\alpha$,
$$2 \Lambda_{t} d \alpha=-\delta_{t} J_{t} \alpha$$
and $\delta_{t} J_{t}$ actually does not depend on $t$. Indeed,by definition, we have for any smooth function $f$ and 1-form $\alpha$,
$$\int_{V}\left(\delta_{t} \alpha\right) f \omega^{m}=\int_{V}\langle\alpha, d f\rangle_{t} \omega^{m}=\int_{V} \alpha\left(\operatorname{grad}_{t} f\right) \omega^{m} .$$
Thus,
$$\int_{V}\left(\delta_{t} J_{t} \alpha\right) f \omega^{m}=\int_{V}\left\langle J_{t} \alpha, d f\right\rangle_{t} \omega^{m}=-\int_{V} \alpha\left(J_{t} \operatorname{grad}_{t} f\right) \omega^{m}=\int_{V} \alpha\left(X_{f}\right) \omega^{m} .$$

As a consequence, we have the announced result:
$$\left.\frac{d}{d t}\right|_{t=0} s^{\nabla}\left(J_{t}\right)=\Lambda d(\delta \dot{J})^{b}=-\delta J(\delta \dot{J})^{b}$$ \(\square\)

This results has other interesting consequences. For instance, if $J_{1}$ and $J_{2}$ are in $\mathcal{A} \mathcal{C}_{\omega}$, then we get
$$\begin{aligned}
\rho^{\nabla_{J_{1}}}-\rho^{\nabla_{J_{2}}} & =d \alpha_{J_{1}}-d \alpha_{J_{2}} \\
& =-\frac{1}{2} d\left(\int_{0}^{1}\left(\delta_{t} \dot{J}\right)^{b_{t}} d t\right)
\end{aligned}$$
thus belong to the same de Rham class, the first Chern class of the symplectic manifold $(V, \omega)$.
Moreover, if one defines the total Hermitian scalar curvature as
$$S^{\nabla}=\int_{V} s^{\nabla} \operatorname{vol}_{g}$$
then it is constant on $\mathcal{A} \mathcal{C}_{\omega}$, as
$$S^{\nabla_{J_{1}}}-S^{\nabla_{J_{2}}}=-\int_{V} \Lambda d\left(\int_{0}^{1}\left(\delta_{t} \dot{J}\right)^{b_{t}} d t\right) v o l_{g}=0$$
This goes to say that the Hermitian scalar curvature on $\mathcal{A} \mathcal{C}_{\omega}$ is the correct analogue in our context of the scalar curvature on a fixed Kähler class. As an aside, note, we may push this analogy further and define a Hermitian Calabi functional by
$$\begin{aligned}
\mathcal{C}: \mathcal{A} \mathcal{C}_{\omega} & \rightarrow \mathbb{R} \\
J \mapsto \int_{V} s^{\nabla}(J)^{2} \text { vol }_{g} &
\end{aligned}$$
whose critical points are called extremal almost-Kähler metric and verify a similar condition as the extremal Kähler metrics. Such extremal almost Kähler metrics have been studied by Lejmi in [25].

Relation to the Lichnerowicz operator. Using this formula, we can now compute the linearisation of the operator that will appear in the gluing construction, which is the composition of $s^{\nabla}$ with the map $f \mapsto J_{f}$ introduced in (4). In particular, we are interested with how it relates to the linearisation of the (riemannian) scalar curvature on a Kähler manifold.

Recall that, on a Kähler manifold, the following formula holds:
$$\left.\frac{d}{d t}\right|_{t=0} s(\omega+i \partial \bar{\partial} f)=-2 \delta \delta D^{-} d f+(d s, d f)=\frac{1}{2} \Delta^{2} f+(2 i \partial \bar{\partial} f, \rho)$$

On a constant scalar curvature Kähler manifold, this reduces to the Lichnerowicz operator
$$\mathbb{L} f=\left(D^{-} d\right)^{*} D^{-} d f=\delta \delta D^{-} d f=\frac{1}{2} \Delta^{2} f+\delta(\operatorname{Ric}(d f))$$

Choose $J \in \mathcal{A C}_{\omega}$ so that $(V, J, \omega)$ is almost-Kähler. We have
$$\left.\frac{d}{d t}\right|_{t=0} J_{t f}=J \mathcal{L}_{X_{f}} J$$
thus we want to compare
$$L: f \mapsto-\delta J\left(\delta\left(J \mathcal{L}_{X_{f}} J\right)\right)^{b}$$
to $\mathbb{L}$ in an attempt to translate its good regularity properties to our context.
The main calculation is the following
Proposition 10. Let $f \in C^{3, \alpha}(V)$. Then the following holds:
$$\left.J \delta\left(J \mathcal{L}_{X_{f}} J\right)\right)^{b}=\Delta_{g} d f-2 \operatorname{Ric}\left(\operatorname{grad}_{g} f, \cdot\right)+E f$$
where the error term $E$ is given, in an orthornormal basis for $g$ of the form by
$$E f(Y)=\sum_{i} d f\left(\left(D_{e_{i}, J Y}^{2} J\right) e_{i}\right)+2 D d f\left(e_{i}, J\left(D_{Y} J\right) e_{i}\right)$$
in an orthonormal frame $\left\{e_{1}, \ldots, e_{2 m}\right\}=\frac{1}{\sqrt{2}}\left\{Z_{1}, \ldots, Z_{m}, J Z_{1}, \ldots, J Z_{m}\right\}$ on (TV, g).
Proof. The first thing we use is the following rewriting of $\dot{J}$ :
$$\begin{aligned}
\dot{J} & =J \mathcal{L}_{X_{f}} J \\
& =\mathcal{L}_{J X_{f}} J-4 N_{J}\left(X_{f}, \cdot\right) \\
& =\mathcal{L}_{\operatorname{grad}_{g}} J-4 N_{J}\left(X_{f}, \cdot\right)
\end{aligned}$$
We will compute $\delta\left(\mathcal{L}_{\operatorname{grad}_{g} f} J\right)$ and $\delta N_{J}\left(X_{f}, \cdot\right)$ separately.
For the first, let $\psi_{t}$ be the flow of $\operatorname{grad}_{g} f$. Then
$$\mathcal{L}_{\operatorname{grad}_{g} f} J=\left.\frac{d}{d t}\right|_{t=0} \psi_{t}^{*} J .$$
Now, $(V, J, \omega)$ is an almost Kähler manifold, thus $\delta J=0$, which implies
$$\psi_{t}^{*}(\delta J)=\delta^{\psi_{t}^{*} g} \psi_{t}^{*} J=0 .$$
Differentiating this equation at 0 with respect to $t$, we get
$$\delta \mathcal{L}_{\operatorname{grad}_{g} f} J=-\left.\frac{d}{d t}\right|_{t=0}\left(\delta^{\psi_{t}^{*} g}\right) J .$$
To rewrite this expression, we use the following, proven by Minerbe in his thesis [31] (Lemma 3.19):
$$\left.\frac{d}{d t}\right|_{t=0} D_{X}^{\psi_{t}^{*} g} Y=\operatorname{Rm}^{g}\left(X, \operatorname{grad}_{g} f\right) Y-D_{X, Y}^{2} \operatorname{grad}_{g} f$$

We choose an orthonormal basis $\left\{e_{i}\right\}_{i=1 \ldots 2 m}$ of $(T V, g)$ of the form $\frac{1}{\sqrt{2}}\left\{Z_{1}, \ldots, Z_{m}, J Z_{1}, \ldots, J Z_{m}\right\}$, with $\left\{Z_{i}\right\}_{i}$ an orthonormal basis for the complex vector bundle $(T M, J)$ (as in the proof of Proposition 9). In such a basis
$$\delta^{\psi_{t}^{*} g} J=-\sum_{i, j}\left(\psi_{t}^{*} g\right)^{i j} D_{e_{i}}^{\psi_{t}^{*} g} J\left(e_{j}\right),$$
where $\left(\psi_{t}^{*} g\right)^{i j}$ denotes the $(i, j)$-coefficient of the inverse of the matrix $\left(\psi_{t}^{*} g\left(e_{k}, e_{l}\right)\right)_{k, l}$. Using (9), we get
$$\begin{aligned}
\left.\frac{d}{d t}\right|_{t=0} D_{e_{i}}^{\psi_{t}^{*} g} J\left(e_{j}\right) & =\left.\frac{d}{d t}\right|_{t=0}\left(D_{e_{i}}^{\psi_{t}^{*} g}\left(J e_{j}\right)-J D_{e_{i}}^{\psi_{t}^{*} g} e_{j}\right) \\
& =\operatorname{Rm}\left(e_{i}, \operatorname{grad}_{g} f\right) J e_{j}-D_{e_{i}, J e_{j}}^{2} \operatorname{grad}_{g} f-J \operatorname{Rm}\left(e_{i}, \operatorname{grad}_{g} f\right) e_{j}+J D_{e_{i}, e_{j}}^{2} \operatorname{grad}_{g} f .
\end{aligned}$$
On the other hand, since we have chosen an orthonormal basis for $g,\left(\psi_{t}^{*} g\right)_{\mid t=0}^{i j}=\delta_{i j}$, thus
$$\left.\frac{d}{d t}\right|_{t=0}\left(\psi_{t}^{*} g\right)^{i j}=-\left.\frac{d}{d t}\right|_{t=0}\left(\psi_{t}^{*} g\right)_{i j}=-\mathcal{L}_{\operatorname{grad}_{g} f} g\left(e_{i}, e_{j}\right)=-2 D d f\left(e_{i}, e_{j}\right) .$$
Thus,
$$\begin{aligned}
-\delta \mathcal{L}_{\operatorname{grad}_{g}} J= & -\sum_{i} \operatorname{Rm}\left(e_{i}, \operatorname{grad}_{g} f\right) J e_{i}-D_{e_{i}, J e_{i}}^{2} \operatorname{grad}_{g} f-J \operatorname{Rm}\left(e_{i}, \operatorname{grad}_{g} f\right) e_{i}+J D_{e_{i}, e_{i}}^{2} \operatorname{grad}_{g} f \\
& +\sum_{i, j} 2 D d f\left(e_{i}, e_{j}\right) D_{e_{i}} J\left(e_{j}\right)
\end{aligned}$$
Now, using Bianchi's identity,
$$\begin{aligned}
\operatorname{Rm}\left(e_{i}, \operatorname{grad}_{g} f\right) J e_{i} & =-\operatorname{Rm}\left(\operatorname{grad}_{g} f, J e_{i}\right) e_{i}-\operatorname{Rm}\left(J e_{i}, e_{i}\right) \operatorname{grad}_{g} f \\
& =\operatorname{Rm}\left(J e_{i}, \operatorname{grad}_{g} f\right) e_{i}-\operatorname{Rm}\left(J e_{i}, e_{i}\right) \operatorname{grad}_{g} f
\end{aligned}$$
Now, our choice of basis gives
$$\sum_{i} \operatorname{Rm}\left(e_{i}, \operatorname{grad}_{g} f\right) J e_{i}=-\sum_{i} \operatorname{Rm}\left(J e_{i}, \operatorname{grad}_{g} f\right) e_{i},$$
thus
$$\sum_{i} \operatorname{Rm}\left(e_{i}, \operatorname{grad}_{g} f\right) J e_{i}=\frac{1}{2} \sum_{i} \operatorname{Rm}\left(e_{i}, J e_{i}\right) \operatorname{grad}_{g} f .$$
On the other hand, still thanks to the form of the local frame $\left\{e_{i}\right\}$,
$$\sum_{i} D_{e_{i}, J e_{i}}^{2} \operatorname{grad}_{g} f=\frac{1}{2} \sum_{i}\left(D_{e_{i}, J e_{i}}^{2} \operatorname{grad}_{g} f-D_{J e_{i}, e_{i}}^{2} \operatorname{grad}_{g} f\right)=\frac{1}{2} \sum_{i} \operatorname{Rm}\left(e_{i}, J e_{i}\right) \operatorname{grad}_{g} f .$$
As a consequence, the first two terms in (10) compensate one another. As for the remaining terms, we use
$$\sum_{i} \operatorname{Rm}\left(e_{i}, \operatorname{grad}_{g} f\right) e_{i}=-\operatorname{Ric}\left(\operatorname{grad}_{g} f\right),$$
thus (10) rewrites
$$\delta \mathcal{L}_{\operatorname{grad}_{g} f} J=-J D^{*} D \operatorname{grad}_{g} f-J \operatorname{Ric}\left(\operatorname{grad}_{g} f\right)-\sum_{i, j} 2 D d f\left(e_{i}, e_{j}\right) D_{e_{i}} J\left(e_{j}\right) .$$

Using Bochner's formula on 1-foms, this rewrites
$$\left(\delta \mathcal{L}_{\operatorname{grad}_{g} f} J\right)^{b}=J \Delta d f-2 \operatorname{Ric}\left(\operatorname{grad}_{g} f, J \cdot\right)-\sum_{i} 2 D_{e_{i}} d f \circ D_{e_{i}} J$$

We still have the second term of (8) to deal with. We need to compute
$$\left(\delta N_{J}\left(X_{f}, \cdot\right)\right)^{b} .$$
However, the Nijenhuis tensor rewrites as follows in terms of the Levi-Civita connection
$$g\left(N_{J}\left(X_{f}, X\right), Y\right)=\frac{1}{2} g\left(X_{f}, J\left(D_{Y} J\right) X\right) .$$
Thus,
$$\left(\delta N_{J}\left(X_{f}, \cdot\right)\right)^{b}(Y)=\delta \alpha(Y)$$
where $\alpha(X, Y):=-\frac{1}{2} g\left(\operatorname{grad}_{g} f,\left(D_{Y} J\right) X\right)$. Hence
$$\begin{aligned}
\left(\delta N_{J}\left(X_{f}, \cdot\right)\right)^{b}(Y) & =-\sum_{i} D_{e_{i}} \alpha\left(e_{i}, Y\right) \\
& =-\sum_{i} e_{i} \cdot\left(\alpha\left(e_{i}, Y\right)\right)-\alpha\left(D_{e_{i}} e_{i}, Y\right)-\alpha\left(e_{i}, D_{e_{i}} Y\right) \\
& =\frac{1}{2} \sum_{i} g\left(D_{e_{i}} \operatorname{grad}_{g} f,\left(D_{Y} J\right) e_{i}\right)+g\left(\operatorname{grad}_{g} f,\left(D_{e_{i}, Y}^{2} J\right) e_{i}\right) .
\end{aligned}$$

Moreover, observe that since $D_{Y} J$ is antisymmetric with respect to the metric $g$, while the Hessian $D d f$ is symmetric, the first term must vanish. Indeed, in a basis that simultaneously diagonalises $D d f$ and $g$, we see that
$$\begin{aligned}
\sum_{i} g\left(D_{e_{i}} \operatorname{grad}_{g} f,\left(D_{Y} J\right) e_{i}\right) & =\sum_{i} D d f\left(e_{i},\left(D_{Y} J\right) e_{i}\right) \\
& =\sum_{i} \lambda_{i} g\left(e_{i},\left(D_{Y} J\right) e_{i}\right) \\
& =-\sum_{i} \lambda_{i} g\left(\left(D_{Y} J\right) e_{i}, e_{i}\right) \\
& =-\sum_{i} g\left(D_{e_{i}} \operatorname{grad}_{g} f,\left(D_{Y} J\right) e_{i}\right) .
\end{aligned}$$
As a consequence, we are left with
$$\begin{aligned}
\left.J \delta\left(J \mathcal{L}_{X_{f}} J\right)\right)^{b}(Y) & =J \delta\left(\mathcal{L}_{\operatorname{grad}_{g} f} J\right)^{b}(Y)-4 J\left(\delta N_{J}\left(X_{f}, \cdot\right)\right)^{b}(Y) \\
& =\Delta_{g} d f(Y)-2 \operatorname{Ric}\left(\operatorname{grad}_{g} f, Y\right)-2 \sum_{i} D_{e_{i}} d f\left(\left(D_{e_{i}} J\right) Y\right)-2 \sum_{i} d f\left(D_{e_{i}, J Y}^{2} e_{i}\right)
\end{aligned}$$
which is what we set out to demonstrate, provided $J$ act on 1-forms the usual way:
$$(J \alpha)(Y)=-\alpha(J Y) .$$ \(\square\)

The error term gives the quantity we will need to estimate when comparing the linearisation of our equation to model operators on $M$ and $X$. We can see it is directly related to the lack on integrability of $J$.

Applying the codifferential $\delta$ again, we see that
$$L f=-\Delta_{g}^{2} f+2 \delta(\operatorname{Ric}(d f))+\delta E f,$$
that is, the linearised operator is equal to the Lichnerowicz operator, plus an error term of order at most 3 in $f$. The coefficients of this error term depends on (derivatives of) $D J$, which is comparable to the Nijenhuis tensor. As a consequence, $\mathcal{L}$ is an elliptic, 4th-order operator on the potential function $f$.

\section*{3 Darboux charts in the orbifold and the ALE space}

When gluing together an orbifold with the resolutions of its singularities, holomorphic charts are usually used, to obtain a "connected sum" that is naturally a complex manifold. However, here the construction will not work in holomorphic charts, as the complex structures do not match on the ALE space $X$ and the Kähler orbifold $M$; the connected sum we will obtain will have no natural complex structure inherited from that of the orbifold.

To address that issue, we will work in Darboux charts instead, and endow the connected sum with a symplectic structure.

\subsection*{3.1 On the orbifold.}

Let $\left(M, J_{M}, \omega_{M}\right)$ be a Kähler orbifold of complex dimension 2, with singularities $p_{1}, \ldots, p_{\ell}$ of type $\mathbb{C}^{2} / \mathbb{Z}_{2}$. Let $p_{i}$ be a singular point of $M$. Then, there is a neighborhood $U_{i}$ of 0 in $\mathbb{C}^{2}$ and a map
$$\phi_{i}: U_{i} \rightarrow M,$$
such that $\phi_{i}(0)=p_{i}$ and $\phi_{i}$ induces an homeomorphism
$$\tilde{\phi}_{i}: U_{i} / \mathbb{Z}_{2} \rightarrow \tilde{U}_{i} \subset M .$$

In such a chart, the Kähler form $\omega_{M}$ pulls back to a $\mathbb{Z}_{2}$ invariant, closed, nondegenerate 2-form $\omega_{i}$ on $U_{i}$.

Up to a linear transformation of the coordinates, we may assume that in this chart, at the point 0 we have
$$\omega_{i}(0)=\omega_{0}:=\frac{\sqrt{-1}}{2} \sum d z_{k} \wedge d \overline{z_{k}}$$
Moreover we may arrange that the complex structure $J_{M}$ is also equal to the standard one $J_{0}$ at 0 .
Now, since $\mathbb{Z}_{2} \subset U(2)$, the standard symplectic structure $\omega_{0}$ on $U_{i}$ is also $\mathbb{Z}_{2}$ invariant. Thus we can use the equivariant version of the relative Darboux theorem, relatively to the point 0 where both 2-forms agree, to find an equivariant symplectomorphism
$$\begin{aligned}
\psi: V_{i} \subset U_{i} & \rightarrow V_{i} \subset U_{i}, \\
\psi^{*} \omega_{i} & =\omega_{0} .
\end{aligned}$$
This is proven the usual way, by working $\mathbb{Z}_{2}$-equivariantly; the interested reader may consult [13].
This symplectomorphism passes to the quotient modulo $\mathbb{Z}_{2}$ and, composed with $\phi_{i}$, provides an orbifold Darboux chart around $p_{i} \in M$.

Moreover, since $\omega_{0}(0)=\omega_{i}(0)$, working relatively to 0 we may assume that $d \psi(0)=I$, thus in this Darboux chart, the complex structure $J_{M}$ is equal to $J_{0}$ at $p$.

\subsection*{3.2 On the ALE manifold.}

The second ingredient of the gluing construction is an ALE Kähler manifold $X$, with group at infinity $\mathbb{Z}_{2}$. We consider $X=T^{*} S^{2}$ endowed with the family of Ricci-flat Kähler metrics $\left(J_{X, \varepsilon}, g_{X, \varepsilon}\right)$ that are described in the Annex. They are obtained when considering smoothings instead of the minimal resolution of the quotient singularity. In spherical coordinates in $\mathbb{R}^{4}$, we have the following
expression:
$$\begin{aligned}
J_{X, \varepsilon} \frac{\partial}{\partial s} & =-\frac{2 s}{\sqrt{s^{4}-4}} X_{3}, J_{S} X_{1}=-\sqrt{1-\frac{4}{s^{4}}} X_{2} \\
\frac{1}{\sqrt{2} \varepsilon} g_{X, \varepsilon} & =\left(1-\frac{4}{s^{4}}\right)^{-1} d s^{2}+\frac{s^{2}}{4}\left(1-\frac{4}{s^{4}}\right) \alpha_{1}^{2}+\frac{s^{2}}{4}\left(\alpha_{2}^{2}+\alpha_{3}^{2}\right) \\
\omega_{X, \varepsilon} & =\sqrt{2} \varepsilon\left(\frac{s}{2 \sqrt{1-\frac{4}{s^{4}}}} \alpha_{3} \wedge d s+\frac{s^{2}}{4} \sqrt{1-\frac{4}{s^{4}}} \alpha_{2} \wedge \alpha_{1}\right)
\end{aligned}$$
where $s$ is the radius function of $\mathbb{R}^{4}$, and the $\alpha_{i}$ 's are a basis of invariant 1 -forms on $S^{3}$, verifying $d \alpha_{i}=2 \alpha_{j} \wedge \alpha_{k}$ for any circular permutation (i,j,k) of (1,2,3), and the $X_{i}$ 's are the associated dual basis. Thus, $\left(J_{X, \varepsilon}, g_{X, \varepsilon}\right)$ gives a Kähler structure on $T^{*} S^{2}$ that is ALE of order 4:

To endow ( $X=T^{*} S^{2}, \omega_{X}$ ) with a Darboux chart outside a compact, notice that
$$\begin{aligned}
\omega_{X, \varepsilon} & =\sqrt{2} \varepsilon d d_{J_{X, \varepsilon}}^{c}\left(\frac{s^{2}}{2}\right)=\sqrt{2} \varepsilon\left(\frac{s}{2 \sqrt{1-\frac{4}{s^{4}}}} \alpha_{3} \wedge d s+\frac{s^{2}}{4} \sqrt{1-\frac{4}{s^{4}}} \alpha_{2} \wedge \alpha_{1}\right) \\
& =f_{\varepsilon}^{\prime}(s) \alpha_{3} \wedge d s+f_{\varepsilon}(s) \alpha_{2} \wedge \alpha_{1}
\end{aligned}$$
où
$$f_{\varepsilon}(s)=\sqrt{2} \varepsilon \frac{s^{2}}{4} \sqrt{1-\frac{4}{s^{4}}}$$

Thus, setting $\frac{r^{2}}{2}=f_{\varepsilon}(s)$ gives a radial change of coordinate that provides a Darboux chart outside a compact set in $X$. Moreover this change of variable gives us the same ALE fall-off rate. Indeed, straightforward computation gives, in these new coordinates:
$$\begin{aligned}
\omega_{X, \varepsilon} & =r \alpha_{3} \wedge d r+\frac{r^{2}}{2} \alpha_{2} \wedge \alpha_{1}=\omega_{0} ; \\
g_{X, \varepsilon} & =\left(1+\frac{\varepsilon^{2}}{r^{4}}\right)^{-\frac{1}{2}} d r^{2}+\frac{r^{2}}{4}\left(1+\frac{\varepsilon^{2}}{r^{4}}\right)^{-\frac{1}{2}} \alpha_{1}^{2}+\frac{r^{2}}{4}\left(1+\frac{\varepsilon^{2}}{r^{4}}\right)^{\frac{1}{2}}\left(\alpha_{1}^{2}+\alpha_{3}^{2}\right) \\
J_{X, \varepsilon} \frac{\partial}{\partial r} & =-\frac{2 r}{\sqrt{r^{4}+\varepsilon^{2}}} X_{3} \\
J_{X, \varepsilon} X_{1} & =-\left(1+\frac{\varepsilon^{2}}{r^{4}}\right)^{-\frac{1}{2}} X_{2} .
\end{aligned}$$

From these expressions, we see that the decay rate in this ALE Darboux chart is still 4:
$$\begin{aligned}
\partial^{k}\left(J_{0}-J_{X, \varepsilon}\right) & =O\left(r^{-4-k}\right) \\
\partial^{k}\left(g_{0}-g_{X, \varepsilon}\right) & =O\left(r^{-4-k}\right) .
\end{aligned}$$
Remark 11. Moreover, in this chart, we observe that as $\varepsilon$ goes to 0, the Kähler structure on $T^{*} S^{2} \backslash S^{2}$ outside the zero section converges to the orbifold Euclidean structure in $\mathbb{C}^{2} / \mathbb{Z}_{2}$, in any $\mathcal{C}^{k}$ norm.

\subsection*{3.3 Symplectic connected sum.}

Using these charts on $M$ and $X$, we obtain a new manifold by a generalized connected sum construction, and that manifold will naturally be a symplectic one. Since $M$ has isolated singularities, we can assume that the Darboux charts around each of them are disjoint.

Define a function $\rho$ on $M$ that, in each such chart, is equal to the distance to the singularity $p_{i}$ and extend it smoothly to 1 on $M$.

On $X$, we use the radius function $r$ in our ALE Darboux chart away from the zero section of $T^{*} S^{2}$. We extend it smoothly to 1 on a compact neighborhood of the zero section.

Let $\varepsilon \in\left(0, \varepsilon_{0}\right)$ be a small gluing parameter, and let $r_{\varepsilon}:=\varepsilon^{\beta}$ for a $0<\beta<1, R_{\varepsilon}=\frac{r_{\varepsilon}}{\varepsilon}$. We identify the regions $\left\{\rho=2 r_{\varepsilon}\right\} \subset M$ and $\left\{r=2 R_{\varepsilon}\right\} \subset X$ via the homothety
$$\begin{gathered}
h_{\varepsilon^{-1}}:\{\varepsilon \leq \rho \leq 1\} \subset M \rightarrow\left\{1 \leq r \leq \varepsilon^{-1}\right\} \subset X \\
z \mapsto w=\frac{z}{\varepsilon} .
\end{gathered}$$

We perform this connected sum construction at each singularity $p_{i}$ to get a smooth compact manifold $M_{\varepsilon}$, which is naturally endowed with the symplectic form
$$\omega_{\varepsilon}= \begin{cases}\varepsilon^{2} h_{\varepsilon^{-1}}^{*} \omega_{X, \varepsilon} & \text { on }\left\{\rho \leq 2 r_{\varepsilon}\right\} \\ \omega_{M} & \text { on }\left\{\rho \geq 2 r_{\varepsilon}\right\}\end{cases}$$
The use of Darboux charts ensure that this 2-form is smooth, nondegenerate and closed.
Remark 12. There is actually another degree of freedom that we do not use here. Indeed, we could make sense of the construction with a complex nonzero parameter $\varepsilon$, which would be tantamount to introduce an action of $S^{1}$.

All the manifolds $M_{\varepsilon}$ are diffeomorphic to the minimal resolution $\hat{M}$ of the singularities $p_{i}$. Moreover, as advertised in the introduction, the region
$$M \backslash \cup_{i} B\left(p_{i}, 4 r_{\varepsilon}\right)$$
is naturally included in each $M_{\varepsilon}$, allowing us to define:
Definition 13. Suppose that we have, for each $\varepsilon \in\left(0, \varepsilon_{0}\right)$, a (smooth) function $f_{\varepsilon}: M_{\varepsilon} \rightarrow \mathbb{R}$. Let $f_{0}: M \rightarrow \mathbb{R}$ be a function defined on the orbifold $M$. Let $K$ be a compact subset of $M^{*}$. There is $\varepsilon_{1}>0$ such that for all $\varepsilon<\varepsilon_{1}, K \subset M \backslash \cup_{i} B\left(p_{i}, 4 r_{\varepsilon}\right)$. Then, for all $\varepsilon<\varepsilon_{1}, f_{\mid K}$ is defined on $M_{\varepsilon}$. We say that the sequence $\left(f_{\varepsilon}\right)_{\varepsilon}$ converges towards $f$ in $\mathcal{C}^{k}$ norm on the compact $K$ if
$$\left\|f_{\varepsilon \mid K}-f_{\mid K}\right\|_{\mathcal{C}^{k}(K)} \xrightarrow{\varepsilon \rightarrow 0} 0 .$$

This definition extends to tensors on $M_{\varepsilon}$. Then, we see that the sequence of symplectic forms $\left(\omega_{\varepsilon}\right)_{\varepsilon}$ converges to the orbifold symplectic form $\omega_{M}$, in any $\mathcal{C}^{k}$ norm, on every compact set of $M^{*}$.

Conversely, the compact set $\left\{r \leq R_{\varepsilon}\right\} \subset X$, after rescaling, is naturally included in a small region of $M_{\varepsilon}$. Thus we may define:

Definition 14. Suppose that we have, for each $\varepsilon \in\left(0, \varepsilon_{0}\right)$, a (smooth) function $f_{\varepsilon}: M_{\varepsilon} \rightarrow \mathbb{R}$. Let $f_{0}: X \rightarrow \mathbb{R}$ be a function defined on the ALE manifold $X$. Let $K$ be a compact subset of $X$, then there is $\varepsilon_{1}>0$ such that for all $\varepsilon<\varepsilon_{1}, K \subset\left\{r \leq R_{\varepsilon}\right\} \hookrightarrow M_{\varepsilon}$. Then, for all $\varepsilon<\varepsilon_{1}, h_{\varepsilon}^{*} f_{\varepsilon \mid K}$ is defined on $X$. We say that the sequence $\left(f_{\varepsilon}\right)_{\varepsilon}$ converges towards $f$ in $\mathcal{C}^{k}$ norm on the compact set $K$ if
$$\left\|h_{\varepsilon}^{*} f_{\varepsilon \mid K}-f_{\mid K}\right\|_{\mathcal{C}^{k}(K)} \xrightarrow{\varepsilon \rightarrow 0} 0 .$$

Moreover,
Lemma 15. The cohomology class $\left[\omega_{\varepsilon}\right]$ does not depend on $\varepsilon$.

Proof. Notice that, on the orbifold $M$, in a contractile neighborhood of each $p_{i}$, the orbifold version of the local $\partial \bar{\partial}$-lemma tells us that $\omega_{M}$ is exact. Thus, there is a 2 -form $\bar{\omega} \in H^{2}\left(M^{*}, \mathbb{R}\right)$, where $M^{*}:=M \backslash\left\{p_{1}, \ldots, p_{\ell}\right\}$, and functions $\varphi_{i}$ supported in a neighborhood of each $p_{i}$, such that
$$\omega_{M}=\bar{\omega}+i \sum_{j} \partial \bar{\partial} \varphi_{j} .$$
On the other hand, since $\omega_{X}=i \partial \bar{\partial} u$ is exact (see Annex), from the definition of $\omega_{\varepsilon}$ we see that we may write
$$\omega_{\varepsilon}=\bar{\omega}+\varepsilon^{2} \sum_{j} \partial \bar{\partial}\left(\gamma_{j} u\right)$$
for suitable cut-off functions $\gamma_{j}$. \(\square\)

Remark 16. A more general, Mayer-Vietoris-type argument, actually allows to identify $H^{2}(M, \mathbb{R})$ to $\left\{\alpha \in H^{2}(\hat{M}, \mathbb{R}), \alpha \cdot S=0\right\}$ via $H_{c}^{2}\left(M^{*}, \mathbb{R}\right)$, where $S$ corresponds to the zero section in $T^{*} S^{2}$.

From here, using Moser's stability theorem (see for instance [29], Theorem 3.17), we get
Corollary 17. The symplectic manifolds $\left(M_{\varepsilon}, \omega_{\varepsilon}\right)_{\varepsilon \in\left(0, \varepsilon_{0}\right)}$ are all symplectically equivalent.
Remark 18. As a consequence, we could actually work on a fixed symplectic manifold $(\hat{M}, \hat{\omega})$. As a matter of fact, this is what we will do in Section 6. However, during the gluing construction, it is more practical for the analysis to keep track of the parameter $\varepsilon$ (for instance to use Definitions 13 and 14).

\section*{4 Almost complex structures on $M_{\varepsilon}$}

The next step is to endow $M_{\varepsilon}$ with an almost complex structure that is compatible with $\omega_{\varepsilon}$. We achieve this by gluing together the complex structures $J_{M}$ on $M$ and $J_{X}$ on $X$. As these manifolds have differing complex structures, making them compatible will come at the cost of integrability, thus we will only get an almost-complex structure on $M_{\varepsilon}$.

\subsection*{4.1 On the orbifold $M$.}

Recall that we are working in orbifold Darboux charts ( $U_{i}, \phi_{i}$ ) centered at each singularity $p_{i}$. In such a chart, $J_{M}$ is, of course, compatible with $\omega_{M}$, but so is $J_{0}$, the standard complex structure in $\mathbb{C}^{2}$.

Thus, according to the proposition 5, there is a unique section $A$ of $\operatorname{End}\left(T U_{i}\right)$, anticommuting with both $J_{M}$ and $J_{0}$, such that
$$J_{M}=\exp (A) J_{0} \exp (-A) .$$

Now, multiplying $A$ by a cut-off function on $M$, we will be able to transition smoothly from $J_{M}$ to $J_{0}$ in a neighborhood of the singularities. We will lose integrability of the resulting almost complex structure in the process. On the other hand, if we can show that $J_{M}$ approaches $J_{0}$ close to each $p_{i}$, we may hope that the operation is not too drastic.

Thus, we first need an estimate of $A$ :
Lemma 19. In the orbifold Darboux coordinates $x=\left(x_{k}\right)_{k=1, \ldots, 4}$ described in paragraph 3, $J_{M}$ and $J_{0}$ coincide to first order:
$$J_{M}(x)=J_{0}+O\left(|x|^{2}\right) .$$
As a consequence, the endomorphism $A$ satisfies the following estimates:
$$\begin{aligned}
A & =O\left(|z|^{2}\right), \\
\partial A & =O(|z|), \text { and } \\
\partial^{k} A & =O(1) \text { for all } k \geq 2 .
\end{aligned}$$

Proof. Recall that in the orbifold charts that we are using, we have arranged that $J_{M}(0)=J_{0}$. Thus, in these coordinates, a Taylor development of $J_{M}$ around 0 can be written
$$J_{M}(x)_{i}^{j}=\left(J_{0}\right)_{i}^{j}+\left(J_{(1)}\right)_{i k}^{j} x_{k}+O\left(|x|^{2}\right) .$$
The tensor $J_{(1)}$, whose coefficients are the first order coefficients in the development of $J_{M}$, is a local section of $\Lambda^{1} U_{i} \otimes \operatorname{End}\left(T U_{i}\right)$. However, as $\mathbb{Z}_{2}$ acts as a multiplication by -1 on $\Lambda^{1} U_{i} \otimes \operatorname{End}\left(T U_{i}\right)$ can only be $\mathbb{Z}_{2}$-invariant if it is zero. As both $J_{M}$ and $J_{0}$ are $\mathbb{Z}_{2}$-invariant, we obtain the estimate (14). Observing that
$$\begin{aligned}
J_{M}-J_{0} & =\exp (A) J_{0} \exp (-A)-J_{0} \\
& =(\exp (2 A)-I) J_{0} \\
& =O\left(|x|^{2}\right),
\end{aligned}$$
we get the desired estimate on $A$. Writing a Taylor development of $A$ and using again that $J_{M}(x)-J_{0}=$ $O\left(|x|^{2}\right)$ allows to get the estimate on the first derivative of $A$ near 0.
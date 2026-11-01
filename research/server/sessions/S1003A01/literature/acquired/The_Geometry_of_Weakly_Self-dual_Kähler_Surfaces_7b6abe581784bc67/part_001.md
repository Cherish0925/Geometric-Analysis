---
retention_scope: session
part: 1
total_parts: 2
---

[Part 1/2 of: The Geometry of Weakly Self-dual Kähler Surfaces]

---
source_file: The_Geometry_of_Weakly_Self-dual_Kähler_Surfaces_53c04d18af3c.pdf
converter: mathpix
format: mmd
---

\title{
The Geometry of Weakly Self-dual Kähler Surfaces
}

\author{
V. APOSTOLOV ${ }^{1}$, D. M. J. CALDERBANK ${ }^{2}$ and P. GAUDUCHON ${ }^{3}$ \\ ${ }^{1}$ Département de Mathématiques, UQAM, CP 8888, Succ. Centre-ville, Montréal, Québec H3C 3P8, Canada. e-mail: apostolo@math.uqam.ca \\ ${ }^{2}$ Department of Mathematics and Statistics, University of Edinburgh, King's Building, Mayfield's Road, Edinburgh EH9 3JZ, Scotland. e-mail: davidmjc@maths.ed.ac.uk \\ ${ }^{3}$ Centre de Mathématiques, École Polytechnique, UMR 7640 du CNRS, 91128 Palaiseau, France. e-mail: pg@math.polytechnique.fr
}
(Received: 9 May 2001; accepted in final form: 18 October 2001)

\begin{abstract}
We study Kähler surfaces with harmonic anti-self-dual Weyl tensor. We provide an explicit local description, which we use to obtain the complete classification in the compact case. We give new examples of extremal Kähler metrics, including Kähler-Einstein metrics and conformally Einstein Kähler metrics. We also extend some of our results to almost Kähler 4-manifolds, providing new examples of Ricci-flat almost Kähler metrics which are not Kähler.
\end{abstract}

Mathematics Subject Classifications (2000). 53B35, 53C55.
Key words. almost-Kähler 4-manifolds, Calabi extremal metrics, Kähler surfaces, weak self-duality.

\section*{Introduction}

Self-dual Kähler surfaces have been considered in several recent works, in particular in a paper by R. Bryant [13], where self-dual Kähler surfaces appear as the four-dimensional case of a comprehensive study of Bochner-flat Kähler manifolds in all dimensions, and in a paper by two of the authors [8], where a generic equivalence has been established between self-dual Kähler surfaces and self-dual Hermitian Einstein metrics and where an explicit local description of the latter is provided.

Whereas self-dual surfaces are easily proved to be extremal, i.e., admitting a Hamiltonian Killing vector field whose momentum map is the scalar curvature, it was an a priori unexpected fact, independently discovered in the above works, that they actually admit a second Hamiltonian Killing vector field; moreover, a crucial observation of R. Bryant [13], is that the momentum map of the latter is the Pfaffian of the normalized Ricci form. Since these Killing vector fields commute, this also provides a link with the work of H. Pedersen and the second author [17], where an explicit local classification of self-dual Einstein metrics with two commuting Killing vector fields is obtained, without the hypothesis that they are Hermitian.

In this paper, we show that we can relax the assumption of self-duality, and establish the same bi-Hamiltonian structure for weakly self-dual Kähler surfaces, i.e., Kähler surfaces whose anti-self-dual Weyl tensor $W^{-}$is harmonic; this fact has its origins in the basic Matsumoto-Tanno identity for such surfaces, recently rediscovered by W. Jelonek [32], and leads to a surprisingly simple explicit expression, generalizing an expression found by Bryant in the self-dual case. On the other hand, we also observe that in Calabi's family of extremal Kähler metrics on the first Hirzebruch surface $F_{1}$, there is a unique (and completely explicit) weakly self-dual metric up to homothety. This is in contrast to the self-dual case, where the compact (smooth) examples are all locally symmetric [20].

Our results concerning weakly self-dual Kähler surfaces may be summarized as follows (definitions and more precise statements are given in the body of the paper).

THEOREM. Let $(M, g, J, \omega)$ be a weakly self-dual Kähler surface. Then $(g, J)$ is a bi-extremal Kähler metric in the sense that the scalar curvature and the Pfaffian of the normalized Ricci form of $(g, J)$ are Poisson-commuting momentum maps for Hamiltonian Killing vector fields $K_{1}$ and $K_{2}$ respectively. Furthermore, on each connected component of $M$ one of the following holds.
\begin{itemize}
\item[(i)] $K_{1}$ and $K_{2}$ are linearly independent on a dense open set. Then $(g, J, \omega)$ has the explicit local form (41-45), depending on an arbitrary polynomial of degree 4 and an arbitrary constant which is zero if and onlyif $g$ is self-dual, cf. Theorem 2.
\item[(ii)] $K_{1}$ is nonvanishing on a dense open set, but $K_{1} \wedge K_{2}$ is identically zero. Then $(g, J, \omega)$ is locally of cohomogeneity one and is given explicitly by the Calabi construction, cf. Theorem 4.
\item[(iii)] $K_{1}$ and $K_{2}$ vanish identically. Then $g$ has parallel Ricci curvature (hence is either Kähler-Einstein or locally a Kähler product of two Riemann surfaces of constant curvatures).
\end{itemize}

If $(M, g, J, \omega)$ is compact and connected, then it necessarily belongs to case (ii) or (iii) above, and in case (ii) $(M, g, J, \omega)$ is isomorphic to the weakly self-dual Calabi extremal metric on $F_{1}$ (see Theorem 5).

The path to proving this result touches upon various important themes in Kähler geometry, and along the way we introduce further ideas, results and examples. A key aspect of our approach is to study weakly self-dual Kähler surfaces within a more general setting. The Matsumoto-Tanno identity for weakly self-dual Kähler surfaces is equivalent to the fact that the primitive part $\rho_{0}$ of the Ricci form $\rho$ of $(g, J)$ satisfies an overdetermined linear differential equation. On the open set where $\rho_{0}$ is nonvanishing, the equation means that $\rho_{0}$ defines a conformally Kähler Hermitian structure $I$ inducing the opposite orientation to $J$. Many of the properties of weakly self-dual Kähler surfaces are simple consequences of the fact that the $\rho$ is a closed $J$-invariant 2-form, whose primitive part satisfies this equation. In particular,
we prove in Proposition 2 that two of the algebraic invariants (essentially the trace and the Pfaffian) of any such 2-form $\varphi$ are Poisson-commuting momentum maps for Hamiltonian Killing vector fields. Therefore, throughout the work, we develop the theory of Kähler surfaces with such 'Hamiltonian' 2-forms $\varphi$, which include other interesting examples in addition to weakly self-dual Kähler surfaces.

First of all we study the generic case that the Hamiltonian Killing vector fields are linearly independent. This means that the Kähler structure ( $g, J, \omega$ ) is toric, and in Theorem 1 we characterize the class of toric Kähler structures arising in this way from Hamiltonian 2-forms. Whereas toric Kähler surfaces in general depend essentially on an arbitrary function of two variables [1, 29], our toric surfaces, which we call 'ortho-toric', have an explicit form-given in Proposition 8-depending only on two arbitrary functions of one variable. This has the practical advantage that curvature conditions lead to ordinary differential equations for these functions. In particular, we are able to obtain explicitly all of the extremal toric Kähler structures in our class, including some new examples of Kähler metrics which are conformally Einstein, but neither self-dual nor anti-self-dual, and also some explicit Kähler-Einstein metrics. The weakly self-dual metrics in this family are classified in Theorem 2.

The case that the Hamiltonian Killing vector fields associated to a Hamiltonian 2-form $\varphi$ are linearly dependent, but not both zero, is closely related to the Calabi construction of Kähler metrics on line bundles over a Riemann surface [14]. We provide, in Theorem 3, a geometric local characterization of these Kähler metrics: they are the Kähler metrics $(g, J)$, with a Killing vector field $K$ such that the almost Hermitian pair $(g, I)$, where $I$ is equal to $J$ on span of $\{K, J K\}$ but $-J$ on the orthogonal distribution, is conformally Kähler. Over a fixed Riemann surface $\Sigma$, the general form of these Kähler metrics 'of Calabi type' again depends essentially only on functions of one variable from which it is easy to recover the Calabi extremal metrics. We present these in Proposition 14: the Riemann surface $\Sigma$ has constant curvature, and the metrics have local cohomogeneity one under $U(2), U(1,1)$ or a central extension of the Heisenberg group Nil. The weakly self-dual Calabi extremal metrics are classified in Theorem 4: there is a four parameter family, one of which is globally defined on the first Hirzebruch surface. The existence of such a metric has been independently observed by Jelonek [33].

The proof of the above theorem is completed by classifying the compact weakly self-dual Kähler surfaces. A partial classification for real analytic Kähler surfaces has been recently obtained by Jelonek [32], but we improve it in two respects: first, as speculated by Jelonek, we are able to remove the assumption of real-analyticity; second we prove that the only (non-product non-Kähler-Einstein) weakly self-dual Kähler metric on a ruled surface, is the Calabi extremal example on the first Hirzebruch surface $F_{1}$.

The paper is organized as follows. In the first section, we establish some basic facts concerning weakly self-dual Kähler surfaces; in particular, using general properties of Hamiltonian 2-forms, we show that weakly self-dual Kähler surfaces are bi-extremal
and that their anti-self-dual Weyl tensor is degenerate (some facts proved in this section also appear in Jelonek's paper [32]). We also present the rough classification, Proposition 6, that allows us to deduce the above theorem from Theorems 2, 4 and 5. The generic, toric case, and Theorem 2, are described in the second section, whereas the third section treats the Calabi examples and Theorem 4. The classification of compact weakly self-dual Kähler surfaces is given in Section 4.

In the final section we show that some of our results generalize to the class of almost Kähler 4-manifolds $(M, g, J, \omega)$ whose Ricci tensor is $J$-invariant. We first observe that the Calabi construction gives rise to new (local) examples of self-dual, Ricci-flat almost Kähler 4-manifolds (see Example 2), which provide further local counterexamples (cf. [9, 44]) to the still open Goldberg conjecture which states that a compact Einstein almost Kähler manifold must be Kähler-Einstein. Next we consider compact almost Kähler 4-manifolds with $J$-invariant Ricci tensor which are weakly self-dual, i.e., have harmonic anti-self-dual Weyl tensor. We show in Theorem 6 that weak-self-duality has strong consequences for the integrability of the corresponding almost complex structure, providing another interesting link with the Goldberg conjecture. As an application of this global result, we prove that a compact almost Kähler 4-manifold has constant sectional curvatures on the Lagrangian 2-planes if and only if it is a self-dual Kähler surface (see Corollary 1).

\section*{1. Weakly Self-dual Kähler Surfaces}

\subsection*{1.1. THE MATSUMOTO-TANNO IDENTITY}

A Kähler surface ( $M, g, J$ ) is an oriented Riemannian four-dimensional manifold equipped with a self-dual complex structure $J$, such that $\nabla J=0$, where $\nabla$ denotes the Levi-Civita connection of $g$. The Kähler form is the $J$-invariant self-dual 2-form $\omega(\cdot, \cdot)=\langle J \cdot, \cdot\rangle ; \omega$ is closed and $(M, \omega)$ is a symplectic manifold.

The vector bundle $\Lambda^{+} M$ of self-dual 2-forms is the orthogonal direct sum of the trivial bundle generated by $\omega$ and of the bundle of $J$-anti-invariant 2-forms, whereas the bundle $\Lambda^{-} M$ coincides with the bundle of primitive - or trace-free - $J$-invariant 2-forms.

We denote by $R, \mathrm{Ric}^{2}, \mathrm{Ric}_{0}, \mathrm{Scal}, W=W^{+}+W^{-}$, the curvature, the Ricci tensor, the trace-free part of Ric, the scalar curvature (i.e., the trace of Ric), and the Weyl tensor, expressed as the sum of its ±-self-dual components $W^{ \pm}$.

The Ricci form, $\rho$, of a Kähler surface is the $J$-invariant 2-form defined by $\rho(\cdot, \cdot)=\operatorname{Ric}(J \cdot, \cdot) ; \rho$ is closed and, up to a factor $2 \pi$, is a representative of the first Chern class of $(M, J)$ in de Rham cohomology; the trace-free part of $\rho$ is denoted by $\rho_{0}$.

DEFINITION 1. A Kähler surface $(M, g, J)$ is weakly self-dual if its anti-self-dual Weyl tensor $W^{-}$is harmonic, i.e., satisfies $\delta^{g} W^{-}=0$, where the codifferential $\delta^{g}$ acts on $W^{-}$as on a 2-form with values in $\Lambda^{-} M$.

Because of the Bianchi identity, the weak self-duality condition can also be defined in terms of the Ricci tensor; from this point of view, it can also be considered as a weak Einstein condition, in the sense that every Einstein metric is weakly self-dual. The link is provided by the Cotton-York tensor $C_{X, Y}(Z)$ of the Riemannian metric $g$. Recall that the Cotton-York tensor is defined by
$$C_{X, Y}(Z)=-\left(\nabla_{X} h\right)(Y, Z)+\left(\nabla_{Y} h\right)(X, Z),$$
where $h=\frac{1}{2}$ Ric $_{0}+\frac{1}{24} \operatorname{Scal} g$ denotes the normalized Ricci tensor of $g$.
The normalized Ricci tensor is the form in which the Ricci tensor appears in the well-known decomposition of the Riemannian curvature $R=h \wedge \mathrm{Id}+W$ (cf., e.g., [12]); therefore, via the (differential) Bianchi identity, the ±-self-dual components, $C^{ \pm}$, of the Cotton-York tensor are linked to the ±-self-dual components of the Weyl tensor by $\delta W^{+}=C^{+}$and $\delta W^{-}=C^{-}$.

Definition 1 can thus be rephrased as follows:
DEFINITION 2. A Kähler surface is weakly self-dual if its Cotton-York tensor is self-dual.

The normalized Ricci tensor plays a natural role throughout this work. For this reason, to simplify formulae, we write $s=\frac{1}{6} \mathrm{Scal}$ for the normalized scalar curvature, which is the trace of $h$.

LEMMA 1 ([43, 32]). For any Kähler surface $(M, g, J, \omega)$ we have
$$\nabla_{X} \rho_{0}=-2 C^{-}(J X)-\frac{1}{2} \mathrm{~d} s(X) \omega+\frac{1}{2}\left(\mathrm{~d} s \wedge J X^{b}-J \mathrm{~d} s \wedge X^{b}\right) .$$

In particular, the Kähler surface $(M, g, J, \omega)$ is weakly self-dual if and only if the following Matsumoto-Tanno identity
$$\nabla_{X} \rho_{0}=-\frac{1}{2} \mathrm{~d} s(X) \omega+\frac{1}{2}\left(\mathrm{~d} s \wedge J X^{b}-J \mathrm{~d} s \wedge X^{b}\right)$$
is satisfied ( for any vector field $X$ ).
Proof. Since $2 h=$ Ric $-s g$, the Cotton-York tensor of any Kähler surface can be written as follows:
$$\begin{aligned}
2 C_{X, Y}(Z) & =-2\left(\nabla_{X} h\right)(Y, Z)+2\left(\nabla_{Y} h\right)(X, Z) \\
& =-\left(\nabla_{X} \operatorname{Ric}\right)(Y, Z)+\left(\nabla_{Y} \operatorname{Ric}\right)(X, Z)+\mathrm{d} s(X)\langle Y, Z\rangle-\mathrm{d} s(Y)\langle X, Z\rangle \\
& =-\left(\nabla_{X} \rho\right)(Y, J Z)+\left(\nabla_{Y} \rho\right)(X, J Z)+d s(X)\langle Y, Z\rangle-\mathrm{d} s(Y)\langle X, Z\rangle \\
& =\left(\nabla_{J Z} \rho\right)(X, Y)+\mathrm{d} s(X)\langle Y, Z\rangle-\mathrm{d} s(Y)\langle X, Z\rangle .
\end{aligned}$$
(In order to obtain the last line from the preceding one, we use the fact that $\mathrm{d} \rho=0$.) We then have
$$\left(\nabla_{Z} \rho\right)(X, Y)=-2 C_{X, Y}(J Z)-\mathrm{d} s(X)\langle J Y, Z\rangle+\mathrm{d} s(Y)\langle J X, Z\rangle,$$
or, equivalently,
$$\begin{aligned}
\left(\nabla_{Z} \rho_{0}\right)(X, Y)= & -2 C_{X, Y}(J Z)-\frac{3}{2} \mathrm{~d} s(Z)\langle J X, Y\rangle- \\
& -\mathrm{d} s(X)\langle J Y, Z\rangle+\mathrm{d} s(Y)\langle J X, Z\rangle .
\end{aligned}$$

The anti-self-dual component of (3) gives identity (1); the last statement follows immediately. \(\square\)

\subsection*{1.2. TWISTOR 2-FORMS AND KÄHLER METRICS}

On any Riemannian manifold ( $M, g$ ), if $\Phi$ is an anti-self-dual 2 -form, i.e., a section of the vector bundle $\Lambda^{-} M$, then $\nabla \Phi$ is a section of the vector bundle $T^{*} M \otimes \Lambda^{-} M$. This bundle has an orthogonal direct sum decomposition
$$T^{*} M \otimes \Lambda^{-} M=V^{(0)} M \oplus V^{(1)} M,$$
in accordance with the algebraic decomposition $\mathbb{R}^{4} \otimes \Lambda^{-} \mathbb{R}^{4}=\mathbb{R}^{4} \oplus\left(\Sigma_{+} \otimes \Sigma_{-}^{3}\right)$ into irreducible sub-representations under the action of the orthogonal group. In (4), $V^{(0)} M$ corresponds to the factor $\mathbb{R}^{4}$, hence is isomorphic to $T^{*} M$, whereas $V^{(1)} M$ corresponds to the factor $\Sigma_{+} \otimes \Sigma_{-}^{3}$, so it is the kernel of the natural contraction $T^{*} M \otimes \Lambda^{-} M \rightarrow T^{*} M$. The projection of the connection to $V^{(0)} M$ may be identified with the exterior derivative or divergence on anti-self-dual 2-forms (which are related by the Hodge * operator), while the projection to $V^{(1)} M$ is often called the twistor or Penrose operator on anti-self-dual 2-forms.

DEFINITION 3. An anti-self-dual 2-form $\Phi$ is called a twistor 2-form if $\nabla \Phi$ is a section of the sub-bundle $V^{(0)} M$ of $T^{*} M \otimes \Lambda^{-} M$.

Any nonvanishing section $\Phi$ of $\Lambda^{-} M$ can be written uniquely as $\Phi=\lambda \omega_{I}$, where $\lambda=|\Phi| / \sqrt{2}$ is a positive function and $\omega_{I}$ is the Kähler form of an anti-self-dual almost-complex structure $I$ on $(M, g)$.

LEMMA 2 ([45]). If $\Phi=\lambda \omega_{I}$ is a nonvanishing section of $\Lambda^{-} M$, then $\Phi$ is a twistor 2 -form if and only if the almost-Hermitian pair $\left(\bar{g}=\lambda^{-2} g, I\right)$ is Kähler, with Kähler form $\bar{\omega}=\lambda^{-2} \omega_{I}=\lambda^{-3} \Phi$.

Proof. $\Phi$ is a twistor 2-form if and only if there exists a 1-form $\gamma$ such that, at each point of $M, \nabla \Phi=\sum_{i=1}^{3} I_{i} \gamma \otimes \omega_{i}$, where the triple $\left(I_{1}, I_{2}, I_{3}=I_{1} I_{2}\right)$ is any positively oriented, orthonormal frame of (anti-self-dual) almost-complex structures at that point, and $\omega_{i}$ is the Kähler form of $I_{i}$.

If $\Phi=\lambda \omega_{I}$ is a nonvanishing twistor 2-form on $M$, then, by choosing $I_{1}=I$, we have
$$\lambda \nabla I=(I \gamma-\mathrm{d} \lambda) \otimes I+I_{2} \gamma \otimes I_{2}+I_{3} \gamma \otimes I_{3} .$$
Since the norm of $I$ is constant, this equality implies that $I \gamma=\mathrm{d} \lambda$. Now observe that the equation
$$\lambda \nabla I=I_{3} \mathrm{~d} \lambda \otimes I_{2}-I_{2} \mathrm{~d} \lambda \otimes I_{3}$$
is equivalent to $I$ being parallel with respect to the Levi-Civita connection of $\bar{g}=\lambda^{-2} g$. Hence, if $\Phi$ is a twistor 2-form $(\bar{g}, I)$ is Kähler. Conversely, if $(\bar{g}, I)$ is Kähler then (5) holds, from which it follows that $\nabla \Phi=\nabla\left(\lambda \omega_{I}\right)$ is the section of $V^{(0)} M$ corresponding to the 1-form $\gamma=-I \mathrm{~d} \lambda$. \(\square\)

If $(M, g, J, \omega)$ is a Kähler surface then a 2-form is anti-self-dual if and only if it is trace-free and $J$-invariant, and there is the following reformulation of Definition 3.

LEMMA 3. Let $(M, g, J, \omega)$ be a Kähler surface and let $\varphi_{0}$ be an anti-self-dual 2-form. Then $\varphi_{0}$ is a twistor 2-form if and only if there is a 1-form $\beta$ such that
$$\nabla_{X} \varphi_{0}=-\beta(X) \omega+\beta \wedge J X^{b}-J \beta \wedge X^{b}$$
for any vector field $X$.
Proof. It is easily checked that the right-hand side of (6) is (the contraction with $X$ of) the general form of a section of $V^{(0)} M \cong T^{*} M$. \(\square\)

By the contracted Bianchi identity, $C^{-}$is a section of $V^{(1)} M$, and so the last statement of Lemma 1 can be rephrased as follows.

LEMMA 4. A Kähler surface is weakly self-dual if and only if the trace-free part $\rho_{0}$ of the Ricci form $\rho$ is a twistor 2-form.

Together with Lemma 2, this implies:
PROPOSITION 1. On the open set $M_{0}$ where $\rho_{0}=\lambda \omega_{I}$ does not vanish, a Kähler surface $(M, g, J, \omega)$ is weakly self-dual if and only if the pair $\left(\bar{g}=\lambda^{-2} g, I\right)$ is Kähler.

In particular it follows that on $M_{0}$, the self-dual Weyl tensor of $\bar{g}$, with the orientation induced by $I$, is degenerate, and equal to $\frac{3}{4} \bar{s} \bar{\omega} \otimes_{0} \bar{\omega}$, where $\bar{s}$ is the (normalized) scalar curvature of $\bar{g}, \bar{\omega}=\lambda^{-2} \omega_{I}$, and $\bar{\omega} \otimes_{0} \bar{\omega}$ stands for the traceless part of $\bar{\omega} \otimes \bar{\omega}$ viewed as an endomorphism of $\Lambda^{+} M$. By the conformal covariance of the Weyl tensor, it follows that on $M_{0}$, the anti-self-dual Weyl tensor of $g$ (using the orientation induced by $J$ ) is given by
$$W^{-}=\frac{3}{4} \kappa \omega_{I} \otimes_{0} \omega_{I},$$
where
$$\kappa=\bar{s} \lambda^{-2}$$
is the conformal scalar curvature of the Hermitian pair $(g, I)$, which is related to the Riemannian scalar curvature of $g$ by
$$\kappa-s=\delta \theta-|\theta|^{2} ;$$
here $\theta$ denotes the Lee form of the pair $(g, I)$, defined by $\mathrm{d} \omega_{I}=-2 \theta \wedge \omega_{I}$, see [21, 7]. Note that we have normalized the conformal scalar curvature by a factor $\frac{1}{6}$ to be consistent with our normalization of the scalar curvature $s$.

Notice that this only uses the fact that $M_{0}$ admits a nonvanishing twistor 2-form, namely $\rho_{0}$. On the other hand, $\rho_{0}$ is not anarbitrary twistor 2-form: by Lemma 1, the 1-form $\beta$ defined by $\nabla \rho_{0}$ using (6), is equal to $\frac{1}{2} \mathrm{~d} s$, and so is exact. This fact, which is equivalent to the fact that the Ricci form $\rho=\rho_{0}+\frac{3}{2} s \omega$ is closed, will be exploited in the next subsection.

\subsection*{1.3. HAMILTONIAN 2-FORMS}

DEFINITION 4. A Hamiltonian 2-form on a Kähler surface $(M, g, J, \omega)$ is a closed $J$-invariant 2-form $\varphi$ whose trace-free (i.e., anti-self-dual) part $\varphi_{0}$ is a twistor 2-form.

On a weakly self-dual Kähler surface the Ricci form $\rho$ is Hamiltonian. In general, Hamiltonian 2-forms are characterized by an analogue of the Matsumoto-Tanno identity (2).

LEMMA 5. Let $(M, g, J, \omega)$ be a Kähler surface. Then a $J$-invariant 2-form $\varphi=\varphi_{0}+\frac{3}{2} \sigma \omega$ is Hamiltonian if and only if
$$\nabla_{X} \varphi_{0}=-\frac{1}{2} \mathrm{~d} \sigma(X) \omega+\frac{1}{2}\left(\mathrm{~d} \sigma \wedge J X^{b}-J \mathrm{~d} \sigma \wedge X^{b}\right)$$
for any vector field $X$.
Proof. This is immediate from Lemma 3: in (6), $\mathrm{d} \varphi_{0}=-\frac{3}{2} d \sigma \wedge \omega$ if and only if $\beta=\frac{1}{2} \mathrm{~d} \sigma$. \(\square\)

In order to explain the use of the term 'Hamiltonian', we recall the following definition.

DEFINITION 5. A real function $f$ on a Kähler manifold $(M, g, J, \omega)$ is a (real) holomorphy potential if the gradient $\operatorname{grad}_{g} f$ is a holomorphic vector field, i.e., preserves $J$; equivalently, $f$ is a holomorphy potential if $\operatorname{grad}_{g} f$ is a Killing vector field with respect to $g$.

A holomorphy potential $f$ is therefore a momentum map for a Hamiltonian Killing vector field with respect to the symplectic form $\omega$.

To any $J$-invariant 2-form $\varphi=\varphi_{0}+\frac{3}{2} \sigma \omega$, we may associate a normalized 2-form $\tilde{\varphi}=\frac{1}{2} \varphi_{0}+\frac{1}{4} \sigma \omega$. For example, if $\varphi$ is the Ricci form $\rho$, then $\tilde{\varphi}$ is the 2-form $\tilde{\rho}$ associated to the normalized Ricci tensor: $\tilde{\rho}(\cdot, \cdot)=h(J \cdot, \cdot)$.

We are going to show that if $\varphi$ is Hamiltonian, then the trace and Pfaffian of $\tilde{\varphi}$ are holomorphy potentials.

Recall that, in general, the Pfaffian $\operatorname{pf}(\psi)$ of a 2-form $\psi$ is defined by $\frac{1}{2} \operatorname{pf}(\psi)=$ $*(\psi \wedge \psi)$, where $*$ is the Hodge operator; alternatively, $\psi \wedge \psi=\frac{1}{4} \operatorname{pf}(\psi) \omega \wedge \omega$.

Since $\tilde{\varphi}=\frac{1}{2} \varphi_{0}+\frac{1}{4} \sigma \omega$, its Pfaffian $\pi$ is given by
$$\pi=\frac{1}{4} \sigma^{2}-\frac{1}{2}\left|\varphi_{0}\right|^{2}=\left(\frac{\sigma}{2}+\lambda\right)\left(\frac{\sigma}{2}-\lambda\right),$$
where $\lambda=\left|\varphi_{0}\right| / \sqrt{2}$. We write this product as $\pi=\xi \eta$ so that $\sigma=\xi+\eta$ and $\lambda=\frac{1}{2}(\xi-\eta)$.

PROPOSITION 2. Let ( $M, g, J, \omega$ ) be a Kähler surface and let $\varphi=\varphi_{0}+\frac{3}{2} \sigma \omega$ be a Hamiltonian 2-form. Then the trace $\sigma$ and the Pfaffian $\pi$ of $\tilde{\varphi}=\frac{1}{2} \varphi_{0}+\frac{1}{4} \sigma \omega$ are Poisson-commuting holomorphy potentials.

Proof. (i) Identity (10) can be written in terms of $\tilde{\varphi}$ as
$$\nabla_{X} \tilde{\varphi}=\frac{1}{4}\left(\mathrm{~d} \sigma \wedge J X^{b}-J \mathrm{~d} \sigma \wedge X^{b}\right) .$$
Differentiating again and skew-symmetrizing, we get
$$R_{X, Y} \cdot \tilde{\varphi}=\left[R_{X, Y}, \tilde{\varphi}\right]=\frac{1}{4}\left(\nabla_{Y} \mathrm{~d} \sigma \wedge J X^{b}-\nabla_{X} \mathrm{~d} \sigma \wedge J Y^{b}-J \nabla_{Y} \mathrm{~d} \sigma \wedge X^{b}+J \nabla_{X} \mathrm{~d} \sigma \wedge Y^{b}\right) .$$
Since $\left[R_{X, Y}, \tilde{\varphi}\right]$ is $J$-invariant in $X, Y$, it follows that
$$\begin{aligned}
& \nabla_{Y} \mathrm{~d} \sigma \wedge J X-J \nabla_{Y} \mathrm{~d} \sigma \wedge X-\nabla_{X} \mathrm{~d} \sigma \wedge J Y+J \nabla_{X} \mathrm{~d} \sigma \wedge Y \\
& \quad=-\nabla_{J Y} \mathrm{~d} \sigma \wedge X-J \nabla_{J Y} \mathrm{~d} \sigma \wedge J X+\nabla_{J X} \mathrm{~d} \sigma \wedge Y+J \nabla_{J X} \mathrm{~d} \sigma \wedge J Y,
\end{aligned}$$
hence
$$S(Y) \wedge J X-J S(Y) \wedge X-S(X) \wedge J Y+J S(X) \wedge Y=0,$$
where $S(X)=\nabla_{X} \mathrm{~d} \sigma+J \nabla_{J X} \mathrm{~d} \sigma$.
As an algebraic object, $S$ is a symmetric, $J$-anti-commuting, endomorphism of $T M$; hence by contracting (13) with a vector field $Z$ and taking the trace over $Y$ and $Z$, we see that $S=0$, and therefore, $\sigma$ is a holomorphy potential.
(ii) From (12) we derive $\left(\nabla_{X} \tilde{\varphi}\right) \wedge \tilde{\varphi}=\frac{1}{2}(X \wedge J \mathrm{~d} \sigma \wedge \tilde{\varphi})$, hence
$$\mathrm{d} \pi=-2 *(J \mathrm{~d} \sigma \wedge \tilde{\varphi}) .$$
From this, we infer (again using (12)):
$$\begin{aligned}
\nabla_{X} \mathrm{~d} \pi & =-2 *\left(J \nabla_{X} \mathrm{~d} \sigma \wedge \tilde{\varphi}+J \mathrm{~d} \sigma \wedge \nabla_{X} \tilde{\varphi}\right) \\
& =-2 *\left(J \nabla_{X} \mathrm{~d} \sigma \wedge \tilde{\varphi}+\frac{1}{4} J \mathrm{~d} \sigma \wedge \mathrm{~d} \sigma \wedge J X\right) .
\end{aligned}$$
The second term of the right-hand side of (15) is clearly $J$-invariant; the first term is $J$-invariant as well since $\sigma$ is a holomorphy potential and $\tilde{\varphi}$ is $J$-invariant. Hence $\pi$ is also a holomorphy potential.
(iii) By contracting Equation (14) with $J \mathrm{~d} \sigma$, we see that $\sigma$ and $\pi$ Poisson-commute. \(\square\)

Since $\sigma$ and $\pi$ Poisson-commute, the Killing vector fields $K_{1}:=J \operatorname{grad} \sigma$ and $K_{2}:=J \operatorname{grad} \pi \operatorname{commute}$. Also $\omega\left(K_{1}, K_{2}\right)=0$.

Remark 1. The Killing vector fields $K_{1}$ and $K_{2}$ need not be nonzero or independent in general. In particular $K_{1}$ and $K_{2}$ both vanish if $\sigma$ is constant, since $\varphi$ is then parallel by (10).

Notice, however, that $K_{1}^{1,0}, K_{2}^{1,0}$, and hence $K_{1}^{1,0} \wedge K_{2}^{1,0}$, are holomorphic, so that on each connected component of $M$ there are three possibilities: \(\square\)
\begin{itemize}
\item[(i)] $K_{1} \wedge K_{2}$ is nonvanishing on a dense open set.
\item[(ii)] $K_{1}$ is nonvanishing on a dense open set, but $K_{1} \wedge K_{2}$ vanishes identically;
\item[(iii)] $K_{1}$ and $K_{2}$ vanish identically;
\end{itemize}

One consequence of this remark is the following lemma.

LEMMA 6. If $\varphi$ is a Hamiltonian 2-form on a Kähler surface $M$, then the open set $M_{0}$, where $\varphi_{0}$ is non-zero, is empty or dense in each connected component of $M$.

Proof. On each component of $M$ where $K_{1}=J \operatorname{grad}_{g} \sigma$ is nonzero, the set $U$ where $\mathrm{d} \sigma$ is nonvanishing is dense, hence $\nabla \varphi_{0}$ is nonvanishing on $U$ and so the complement of the zero set of $\varphi_{0}$ is dense in this connected component. On the other hand, if $K_{1}$ is identically zero on a component, then $\varphi_{0}$ is parallel on that component, hence identically zero or everywhere nonzero. \(\square\)

When $K_{1}$ and $K_{2}$ vanish identically, $\varphi$ does not contain much information about the geometry of $M$ (it could be just a constant multiple of $\omega$, even zero). In the other two cases, however, we shall obtain an explicit classification of Kähler surfaces with a Hamiltonian 2-form. The keys to these classifications are Proposition 2 and the following observation.

PROPOSITION 3. Let $\varphi$ be a Hamiltonian 2-form on a Kähler surface $M$ and write $\sigma=\xi+\eta$ and $\pi=\xi \eta$ for the trace and Pfaffian of $\tilde{\varphi}$.

Then on each connected component of $M$ where $\varphi_{0}$ is not identically zero, $\mathrm{d} \xi$ and $\mathrm{d} \eta$ are orthogonal.

Proof. The contraction of (10) with $\varphi_{0}$ yields
$$\left\langle\nabla_{X} \varphi_{0}, \varphi_{0}\right\rangle=\frac{1}{2}\left(\varphi_{0}(\mathrm{~d} \sigma, J X)-\varphi_{0}(J \mathrm{~d} \sigma, X)\right)=-\varphi_{0}(J \mathrm{~d} \sigma, X)$$
and, hence,
$$2 \lambda \mathrm{~d} \lambda=\mathrm{d}\left(\lambda^{2}\right)=\frac{1}{2} \mathrm{~d}\left(\left|\varphi_{0}\right|^{2}\right)=-\varphi_{0}(J \mathrm{~d} \sigma) .$$
Since $\left(\varphi_{0} \circ J\right)^{2}=\lambda^{2} I \mathrm{~d}$, we deduce that $\varphi_{0}(J \mathrm{~d} \lambda)=-\frac{1}{2} \lambda \mathrm{~d} \sigma$ and therefore
$$\varphi_{0} \circ J\left(\frac{\mathrm{~d} \sigma}{2}+\mathrm{d} \lambda\right)=-\lambda\left(\frac{\mathrm{d} \sigma}{2}+\mathrm{d} \lambda\right), \quad \varphi_{0} \circ J\left(\frac{\mathrm{~d} \sigma}{2}-\mathrm{d} \lambda\right)=\lambda\left(\frac{\mathrm{d} \sigma}{2}-\mathrm{d} \lambda\right) .$$
This means that the 1-forms $\mathrm{d} \xi$ and $\mathrm{d} \eta$, wherever they are nonzero, are eigenforms for the symmetric endomorphism $-\varphi_{0} \circ J$, corresponding to the eigenvalues $\lambda$ and $-\lambda$, respectively; in particular, they are orthogonal on the open set $M_{0}$ where $\lambda$ (i.e., $\varphi_{0}$ ) is nonzero. However, by Lemma 6 this open set is empty or dense in each connected component of $M$, and the result follows. \(\square\)

Remark 2. On the open set $M_{0}$ where $\lambda$ is nonzero, so that $\varphi_{0}=\lambda \omega_{I}$, observe that Equation (16) may be rewritten
$$I \mathrm{~d} \sigma=2 J \mathrm{~d} \lambda .$$
Indeed, supposing only that $\varphi_{0}$ is a twistor 2-form, $\bar{\omega}=\lambda^{-3} \varphi_{0}$ is closed, and so, if $\varphi=\varphi_{0}+\frac{3}{2} \sigma \omega$,
$$\mathrm{d} \varphi=\mathrm{d}\left(\varphi_{0}+\frac{3}{2} \sigma \omega\right)=3 \lambda^{2} \mathrm{~d} \lambda \wedge \bar{\omega}+\frac{3}{2} \mathrm{~d} \sigma \wedge \omega=3\left(\mathrm{~d} \lambda \wedge \omega_{I}+\frac{1}{2} \mathrm{~d} \sigma \wedge \omega\right) .$$
Hence, Equation (17) holds if and only if $\varphi$ is closed. \(\square\)

\subsection*{1.4. BI-EXTREMAL KÄHLER SURFACES}

In the case that $(M, g, J, \omega)$ is weakly self-dual and $\varphi_{0}=\rho_{0}$, we can take $\varphi=\rho$, so that $\sigma$ is the (normalized) scalar curvature $s$, and $\pi$, the Pfaffian $p$ of the normalized Ricci form $\tilde{\rho}(\cdot, \cdot)=h(J \cdot, \cdot)$; evidently, $\tilde{\rho}=\frac{1}{2} \rho_{0}+\frac{1}{4} s \omega$.

Recall that a Kähler metric is said to be extremal if the scalar curvature is a holomorphy potential.

DEFINITION 6. A Kähler metric is called bi-extremal if both the (normalized) scalar curvature $s=\operatorname{tr}_{\omega} \tilde{\rho}$ and the $\operatorname{Pfaffian} p=\operatorname{pf}(\tilde{\rho})$ of the normalized Ricci form $\tilde{\rho}$ are holomorphy potentials.

Note that the potential function $p$ appearing in the above definition is not the Pfaffian of the usual Ricci form $\rho=\rho_{0}+\frac{3}{2} s \omega$; thus, our definition for bi-extremality differs from the one given in [42, 31] (compare Theorem 5 below and [31, Th. 1.1 \& Prop. 3.8]).

Proposition 2 immediately implies:

PROPOSITION 4. A weakly self-dual Kähler metric is bi-extremal.
On a bi-extremal Kähler surface, the holomorphy potentials $s$ and $p$ automatically Poisson-commute, since $K_{2}$ preserves $g$, hence $s$, so that $\mathrm{d} s\left(K_{2}\right)=0$.

For a weakly self-dual Kähler surface, Proposition 3 generically implies that $\mathrm{d} \xi$ and $\mathrm{d} \eta$ are orthogonal, where $s=\xi+\eta$ and $p=\xi \eta$. We shall see in Sections 2 and 3 that a bi-extremal Kähler surface satisfying this orthogonality condition is weakly self-dual.

\subsection*{1.5. THE BACH TENSOR}

The Bach tensor, $B$, of an $n$-dimensional Riemannian manifold ( $M, g$ ) is defined by
$$B_{X, Y}=\sum_{i=1}^{n}\left(-\left(\nabla_{e_{i}} C\right)_{e_{i}, X}(Y)+\left(W_{e_{i}, X} h\left(e_{i}\right), Y\right)\right),$$
where, we recall, $C$ is the Cotton-York tensor and $h$ is the normalized Ricci tensor (here, $\left\{e_{i}\right\}$ is an arbitrary $g$-orthonormal frame). When $n=4$, the Bach tensor is conformal covariant of weight -2 , i.e., $B^{\phi^{-2} g}=\phi^{2} B^{g}$, and $B$ can be indifferently expressed in terms of $W^{+}$or of $W^{-}$. Specifically
$$\begin{aligned}
B_{X, Y} & =2 \sum_{i=1}^{n}\left(-\left(\nabla_{e_{i}} C^{+}\right)_{e_{i}, X}(Y)+\left(W_{e_{i}, X}^{+} h\left(e_{i}\right), Y\right)\right) \\
& =2 \sum_{i=1}^{n}\left(-\left(\nabla_{e_{i}} C^{-}\right)_{e_{i}, X}(Y)+\left(W_{e_{i}, X}^{-} h\left(e_{i}\right), Y\right)\right) ;
\end{aligned}$$
in particular, the Bach tensor vanishes whenever $W^{+}, W^{-}$or $\operatorname{Ric}_{0}$ vanishes.

If $(M, g, J)$ is a Kähler surface, the Bach tensor is easily computed by using the above identity and the fact that $W^{+}=\frac{3}{4} s \omega \otimes_{0} \omega$. Indeed, if $B^{+}$and $B^{-}$, denote the $J$-invariant and $J$-anti-invariant parts of $B$, we get
$$B^{+}=s \operatorname{Ric}_{0}+2(\nabla \mathrm{~d} s)_{0}^{+}, \quad B^{-}=-(\nabla \mathrm{d} s)^{-},$$
where $(\nabla \mathrm{d} s)_{0}^{+}$is the $J$-invariant trace-free part of the Hessian and $(\nabla \mathrm{d} s)^{-}$is the $J$-anti-invariant part. (This formula is due to Derdziński [21], where it was obtained by a different argument.)

It follows that $B$ is $J$-invariant if and only if ( $M, g, J$ ) is an extremal Kähler surface; moreover, if this holds, we get $B=s \mathrm{Ric}_{0}+2(\nabla \mathrm{~d} s)_{0}$. On the open set $U$ where $s$ has no zero, the vanishing of $B$ then means that the conformally related metric $\tilde{g}=s^{-2} g$ is Einstein. Therefore, on $U$, the following two statements are thus equivalent (see also [21]):
\begin{itemize}
\item[(i)] The Bach tensor of the Kähler surface $(M, g, J)$ vanishes;
\item[(ii)] $(M, g, J)$ is extremal and the conformally related metric $\tilde{g}=s^{-2} g$ is Einstein.
\end{itemize}

Note also that when $B$ is $J$-invariant, it is determined by the associated anti-self-dual 2-form $\tilde{B}(\cdot, \cdot)=B(J \cdot, \cdot)$, which is also given by
$$\tilde{B}=(\mathrm{d} J \mathrm{~d} s)_{0}+s \rho_{0} .$$
On a weakly self-dual Kähler surface, $C^{-}=0$, while $W^{-}=\frac{3}{4} \kappa \omega_{I} \otimes_{0} \omega_{I}$. It follows that $\tilde{B}$ is a multiple of $\kappa \rho_{0}$, which vanishes if and only if $W^{-}=0$ or $\rho_{0}=0$.

PROPOSITION 5. A weakly self-dual Kähler surface is Bach-flat (i.e., has vanishing Bach tensor) if and only if it is self-dual or Kähler-Einstein.

\subsection*{1.6. ROUGH CLASSIFICATION OF WEAKLY SELF-DUAL KÄHLER SURFACES}

We have seen in Lemma 6 that the open-set $M_{0}$, on which the trace-free part $\varphi_{0}$ of a Hamiltonian 2-form is nonzero, is empty or dense in each connected component of $M$. For a weakly self-dual Kähler surface $(M, g, J, \omega)$, the Ricci form $\rho$ is Hamiltonian, and $M_{0}$ is the set of points at which $g$ is not Kähler-Einstein. Because $\rho$ is closely linked to the anti-self-dual Weyl tensor of $M$, we can obtain more information about $M_{0}$ except when $g$ is self-dual.

We first recall the general fact, first observed by A. Derdziński in [21], that for any Kähler surface $(M, g, J)$ with nonvanishing scalar curvature $s$, the conformally related metric $\tilde{g}=s^{-2} g$ satisfies $\delta^{\tilde{g}} W^{+}=0$; moreover, up to rescaling, $\tilde{g}$ is the unique metric in the conformal class $[g]$ that satisfies this property. This follows from the fact that the self-dual Cotton-York tensor $C^{+}$of any Kähler surface can be written as
$$C^{+}(X)=-W^{+}\left(\frac{\mathrm{d} s}{s} \wedge X\right) ;$$
on the other hand, the self-dual Cotton-York tensors of two conformally related metrics $g$ and $f^{-2} g$ are related by
$$C^{+f^{-2} g}(X)=C^{+, g}(X)+W^{+}\left(\frac{\mathrm{d} f}{f} \wedge X\right) ;$$
it follows from (22) that the self-dual Cotton-York tensor of the metric $s^{-2} g$ vanishes identically; moreover, as $W^{+}$has no kernel (for $s$ nonvanishing), the latter property characterizes $s^{-2} g$ up to a constant multiple.

LEMMA 7. On each connected component of the open set $M_{0}$ where $\rho_{0}$ does not vanish, the scalar curvature $\bar{s}$ of $\bar{g}$ is a constant multiple of $\lambda^{-1}$, i.e.,
$$\bar{s}=c \lambda^{-1},$$
where $\lambda$ is the positive eigenvalue of $\operatorname{Ric}_{0}$ and $c$ is a constant.
Proof. We apply the preceding argument to the Kähler pair $(\bar{g}, I)$ on $M_{0}$ and to $g=\lambda^{2} \bar{g}$; by hypothesis, $g$ satisfies $\delta^{g} W^{-}=C^{-}=0$, where $W^{-}$is actually the self-dual Weyl tensor of $g$ for the orientation induced by $I$; from the above mentioned uniqueness property, it follows that, wherever $\bar{s}$ is non-zero, $g$ coincides with $\bar{s}^{-2} \bar{g}$ up to rescaling, i.e., that $\bar{s}$ is a locally constant multiple of $\lambda^{-1}$. However, the same holds on the interior of the zero set of $\bar{s}$. Hence by the continuity of $\bar{s}$ on $M_{0}, \bar{s}=c \lambda^{-1}$ for some constant $c$ on each connected component of $M_{0}$. \(\square\)

A more global statement may be obtained using the conformal scalar curvature $\kappa=\bar{s} \lambda^{-2}$. Since the anti-self-dual Weyl tensor of $g$ is given by $W^{-}=\frac{3}{4} \kappa \omega_{I} \otimes_{0} \omega_{I}$, it follows that $\kappa^{2}$ is equal to $\left|W^{-}\right|^{2}$ on $M_{0}$, up to a numerical factor, and hence we may extend $\kappa$ continuously to the closure of $M_{0}$. Also $\lambda$ is globally defined and continuous.

Therefore, using the fact that the closure of $M_{0}$ is a union of connected components by Lemma 6, we can rewrite Lemma 7.

LEMMA 8. Let $(M, g, J, \omega)$ be a weakly self-dual Kähler surface. Then, on each component of $M$ where $\rho_{0}$ is not identically zero, the conformal scalar curvature $\kappa$ of $(g, I)$ is linked to $\lambda$ by
$$\kappa \lambda^{3}=c,$$
where $c$ is the constant of Lemma 7. Moreover, $c=0$ if and only if $W^{-}=0$ on that component.

This lemma yields the following rough classification of weakly self-dual Kähler surfaces (see also [32]).

PROPOSITION 6. Let $(M, g, J, \omega)$ be a weakly self-dual, connected, Kähler surface. Then either:
\begin{itemize}
\item[(i)] $\rho_{0}$ is identically zero so $(g, J)$ is Kähler-Einstein; or
\item[(ii)] the scalar curvature $s$ of $g$ is constant, but $\rho_{0}$ is not identically zero; then, $(g, J)$ is locally the Kähler product of two Riemann surfaces of constant curvatures; or
\end{itemize}
\begin{itemize}
\item[(iii)] $s$ is not constant and $g$ is self-dual; or
\item[(iv)] $W^{-}$and $\rho_{0}$ have no zero: then, the Kähler metric $\left(\bar{g}=\lambda^{-2} g, I\right)$ of Proposition 1 is extremal and globally defined on $M$; in particular, $W^{-}$is degenerate everywhere.
\end{itemize}

Proof. If $s$ is constant, then by (2) the Ricci form is parallel. Hence either $g$ is locally irreducible, and is Einstein, or ( $g, J$ ) is locally the Kähler product of two Riemann surfaces of constant curvatures.

If $s$ is not constant, then by Lemma 6 the open set $M_{0}$ where $\rho_{0}$ does not vanish is an open dense subset of $M$. However, by Lemma $8, \kappa \lambda^{3}$ is constant. If this constant is zero, then $\kappa$ must vanish identically and $M$ is self-dual; otherwise $\kappa$ and $\lambda$ have no zero on $M$, so $M_{0}=M$, the Kähler pair ( $\bar{g}=\lambda^{-2} g, I$ ) is defined on $M$ and $W^{-}$is degenerate, but nonzero everywhere. As observed in Section 1.5, for a weakly selfdual Kähler surface the Bach form $\tilde{B}$ is a multiple of $\omega_{I}$. Since $B$ is a conformally covariant tensor, it follows that the Bach tensor of $\bar{g}$ is $I$-invariant, showing that $(\bar{g}, I)$ is an extremal Kähler metric. \(\square\)

Kähler-Einstein metrics and Kähler products of Riemann surfaces clearly are weakly self-dual. Since these are well studied, we henceforth assume that $s$ is not constant (on any component), i.e., $K_{1}$ is nonvanishing on a dense open set. In Section 2, we analyse the generic case that $K_{1}$ and $K_{2}$ are independent, while Section 3 is devoted to the case that $K_{1} \wedge K_{2}$ vanishes identically (but $K_{1}$ is non-zero). In both sections, we obtain an explicit local classification within the more general framework of Kähler surfaces with a Hamiltonian 2-form.

\section*{2. Ortho-toric Kähler Surfaces}

\subsection*{2.1. TORIC KÄHLER SURFACES}

We have seen in Section 1 that on a Kähler surface with a Hamiltonian 2-form $\varphi$-in particular on a weakly self-dual Kähler surface-the trace $\sigma$ and the Pfaffian $\pi$ of the associated normalized 2-form $\tilde{\varphi}$ are holomorphy potentials for Hamiltonian Killing vector fields $K_{1}=J \operatorname{grad} \sigma$ and $K_{2}=J \operatorname{grad} \pi$. Furthermore, $\sigma$ and $\pi$ Poissoncommute, i.e., $\omega\left(K_{1}, K_{2}\right)=0$.

A (usually compact) Kähler surface $(M, g, J, \omega)$, with holomorphic Killing vector fields $K_{1}$ and $K_{2}$ which are independent on a dense open set and satisfy $\omega\left(K_{1}, K_{2}\right)=0$, is said to be toric. We begin this section by recalling the local theory of such surfaces, and we therefore assume that $K_{1}$ and $K_{2}$ are everywhere independent and that $x_{1}$ and $x_{2}$ are globally defined momentum maps for $K_{1}$ and $K_{2}$.

The condition $\omega\left(K_{1}, K_{2}\right)=0$ is equivalent to the fact that $x_{1}$ and $x_{2}$ commute for the Poisson bracket determined by $\omega$. Hence, also $\left[K_{1}, K_{2}\right]=0$, and since $K_{1}$, $K_{2}, J K_{1}$ and $J K_{2}$ are all holomorphic, they all commute. In particular the rank 2 distributions $\Pi$, generated by $K_{1}$ and $K_{2}$, and $J \Pi$, generated by $J K_{1}$ and $J K_{2}$, are integrable.

These distributions $\Pi, J \Pi$ are also orthogonal, since $\left\langle J K_{1}, K_{2}\right\rangle=0$. It follows that $K_{1}, K_{2}, J K_{1}$ and $J K_{2}$ form a frame. Since they commute, the 1-forms in the dual coframe are closed, and may be written $\mathrm{d} t_{1}, \mathrm{~d} t_{2}, J \mathrm{~d} t_{1}, J \mathrm{~d} t_{2}$, where $t_{1}$ and $t_{2}$ are only given locally and up to an additive constant. Now observe that
$$\begin{aligned}
& J \mathrm{~d} t_{1}=\frac{\left|K_{2}\right|^{2} \mathrm{~d} x_{1}-\left\langle K_{1}, K_{2}\right\rangle \mathrm{d} x_{2}}{\left|K_{1} \wedge K_{2}\right|^{2}}, \\
& J \mathrm{~d} t_{2}=\frac{\left|K_{1}\right|^{2} \mathrm{~d} x_{2}-\left\langle K_{1}, K_{2}\right\rangle \mathrm{d} x_{1}}{\left|K_{1} \wedge K_{2}\right|^{2}},
\end{aligned}$$
and so
$$J \mathrm{~d} t_{i}=\sum_{j=1,2} G_{i j} \mathrm{~d} x_{j} \quad(i=1,2),$$
where $G_{i j}$ is a positive definite symmetric matrix of functions of $x_{1}$ and $x_{2}$ (note that $K_{i}=\partial / \partial t_{i}$ ). These 1-forms are closed if and only if $G_{i j}$ is the Hessian of a function of $x_{1}$ and $x_{2}$. The following well-known explicit classification is then readily obtained (see [1, 29]).

PROPOSITION 7. Let $G_{i j}$ be a positive definite 2 × 2 symmetric matrix of functions of 2 -variables $x_{1}, x_{2}$ with inverse $G^{i j}$. Then the metric
$$\sum_{i, j}\left(G_{i j} \mathrm{~d} x_{i} \mathrm{~d} x_{j}+G^{i j} \mathrm{~d} t_{i} \mathrm{~d} t_{j}\right)$$
is almost-Kähler with Kähler form
$$\omega=\mathrm{d} x_{1} \wedge \mathrm{~d} t_{1}+\mathrm{d} x_{2} \wedge \mathrm{~d} t_{2}$$
and has independent Hamiltonian Killing vector fields $\partial / \partial t_{1}, \partial / \partial t_{2}$ with Poisson-commuting momentum maps $x_{1}$ and $x_{2}$. Any almost Kähler structure with such a pair of Killing vector fields is of this form (where the $t_{i}$ are locally defined up to an additive constant), and is Kähler if and only if $G_{i j}$ is the Hessian of a function of $x_{1}$ and $x_{2}$.

\subsection*{2.2. THE ORTHO-TORIC CASE}

Propositions 2 and 3 motivate the following definition.

DEFINITION 7. A Kähler surface ( $M, g, J, \omega$ ) is ortho-toric if it admits two independent Hamiltonian Killing vector fields with Poisson-commuting momentum maps $\xi \eta$ and $\xi+\eta$ such that $\mathrm{d} \xi$ and $\mathrm{d} \eta$ are orthogonal.

An explicit classification of ortho-toric Kähler metrics follows from Proposition 7 by changing variables and imposing the orthogonality of $\mathrm{d} \xi$ and $\mathrm{d} \eta$. However, since the coordinate change is awkward, and we have not spelt out the proof of Proposition 7, we give a self-contained proof of this classification.

PROPOSITION 8. The almost-Hermitian structure $(g, J, \omega)$ defined by
$$\begin{aligned}
& g=(\xi-\eta)\left(\frac{\mathrm{d} \xi^{2}}{F(\xi)}-\frac{\mathrm{d} \eta^{2}}{G(\eta)}\right)+\frac{1}{\xi-\eta}\left(F(\xi)(\mathrm{d} t+\eta \mathrm{d} z)^{2}-G(\eta)(\mathrm{d} t+\xi \mathrm{d} z)^{2}\right) \\
& J \mathrm{~d} \xi=\frac{F(\xi)}{\xi-\eta}(\mathrm{d} t+\eta \mathrm{d} z), \quad J \mathrm{~d} t=-\frac{\xi \mathrm{d} \xi}{F(\xi)}-\frac{\eta \mathrm{d} \eta}{G(\eta)}, \\
& J \mathrm{~d} \eta=\frac{G(\eta)}{\eta-\xi}(\mathrm{d} t+\xi \mathrm{d} z), \quad J \mathrm{~d} z=\frac{\mathrm{d} \xi}{F(\xi)}+\frac{\mathrm{d} \eta}{G(\eta)}, \\
& \omega=\mathrm{d} \xi \wedge(\mathrm{~d} t+\eta \mathrm{d} z)+\mathrm{d} \eta \wedge(\mathrm{~d} t+\xi \mathrm{d} z)
\end{aligned}$$
is an ortho-toric Kähler structure for any functions $F, G$ of one variable. Every orthotoric Kähler surface is of this form, where $t, z$ are locally defined up to an additive constant.

Proof. (i) The Kähler form may be written
$$\omega=\mathrm{d}(\xi+\eta) \wedge \mathrm{d} t+\mathrm{d}(\xi \eta) \wedge \mathrm{d} z$$
which is certainly closed. If is also immediate that $\partial / \partial t$ and $\partial / \partial z$ are Hamiltonian Killing vector fields with Poisson-commuting momentum maps $\xi+\eta$ and $\xi \eta$. Since $\mathrm{d} t+i J \mathrm{~d} t$ and $\mathrm{d} z+i J \mathrm{~d} z$ are closed, $J$ is integrable, and the Kähler surface is clearly ortho-toric.
(ii) Conversely, suppose that $(g, J, \omega)$ is an ortho-toric Kähler surface with Killing vector fields $K_{1}, K_{2}$. Since the dual frame to $K_{1}, K_{2}, J K_{1}, J K_{2}$ consists of closed 1-forms, we may write it as $\mathrm{d} t, \mathrm{~d} z, J \mathrm{~d} t, J \mathrm{~d} z$, where $t$ and $z$ are locally defined up to an additive constant. Note also that $\mathrm{d} \xi, \mathrm{d} \eta, \mathrm{d} t, \mathrm{~d} z$ are linearly independent 1 -forms-where $\xi+\eta$ and $\xi \eta$ are the momentum maps of $K_{1}$ and $K_{2}$-so we may use $(\xi, \eta, t, z)$ as a coordinate system.

Since $(J \mathrm{~d} z)\left(K_{1}\right)=0$ and $(J \mathrm{~d} z)\left(K_{2}\right)=0$ we may write
$$J \mathrm{~d} z=\frac{\mathrm{d} \xi}{F}+\frac{\mathrm{d} \eta}{G}$$
for some functions $F$ and $G$ (of $\xi$ and $\eta$ ). The equations
$$0=(J \mathrm{~d} z)\left(J K_{1}\right)=-\langle J \mathrm{~d} z, \mathrm{~d} \xi+\mathrm{d} \eta\rangle$$
and
$$1=(J \mathrm{~d} z)\left(J K_{2}\right)=-\langle J \mathrm{~d} z, \eta \mathrm{~d} \xi+\xi \mathrm{d} \eta\rangle$$
give $F=|\mathrm{d} \xi|^{2}(\xi-\eta)$ and $G=|\mathrm{d} \eta|^{2}(\eta-\xi)$, using the fact that $\mathrm{d} \xi$ and $\mathrm{d} \eta$ are orthogonal. A similar argument tells us that
$$J \mathrm{~d} t=-\frac{\xi \mathrm{d} \xi}{F}-\frac{\eta \mathrm{d} \eta}{G} .$$
for the same functions $F$ and $G$. Now since $J \mathrm{~d} t$ and $J \mathrm{~d} z$ are closed, we obtain $(\xi-\eta) F_{\eta}=0$ and $(\eta-\xi) G_{\xi}=0$, so that $F=F(\xi)$ and $G=G(\eta)$. The Kähler form $\omega$ is evidently given by (27), and since we know $J \mathrm{~d} t$ and $J \mathrm{~d} z$, we readily obtain (26), and hence the metric (25). \(\square\)

Any ortho-toric Kähler surface $(M, g, J, \omega)$ comes equipped with an anti-self-dual almost-complex structure, $I$, whose Kähler form, $\omega_{I}$ is defined by
$$\begin{aligned}
\omega_{I} & =\frac{\mathrm{d} \xi \wedge J \mathrm{~d} \xi}{|\mathrm{~d} \xi|^{2}}-\frac{\mathrm{d} \eta \wedge J \mathrm{~d} \eta}{|\mathrm{~d} \eta|^{2}} \\
& =\mathrm{d} \xi \wedge(\mathrm{~d} t+\eta \mathrm{d} z)-\mathrm{d} \eta \wedge(\mathrm{~d} t+\xi \mathrm{d} z) ;
\end{aligned}$$
equivalently
$$\begin{aligned}
& I \mathrm{~d} \xi=J \mathrm{~d} \xi=\frac{F(\xi)}{\xi-\eta}(\mathrm{d} t+\eta \mathrm{d} z), \quad I \mathrm{~d} t=-\frac{\xi \mathrm{d} \xi}{F(\xi)}+\frac{\eta \mathrm{d} \eta}{G(\eta)}, \\
& I \mathrm{~d} \eta=-J \mathrm{~d} \eta=-\frac{G(\eta)}{\eta-\xi}(\mathrm{d} t+\xi \mathrm{d} z), \quad I \mathrm{~d} z=\frac{\mathrm{d} \xi}{F(\xi)}-\frac{\mathrm{d} \eta}{G(\eta)} .
\end{aligned}$$

PROPOSITION 9. For any ortho-toric Kähler surface, the almost-Hermitian pair $\left(\bar{g}=(\xi-\eta)^{-2} g, I\right)$ is Kähler.

Proof. Clearly $I \mathrm{~d} t$ and $I \mathrm{~d} z$ are closed, so $I$ is integrable. From (28), we easily infer that the Lee form $\theta$ of the Hermitian pair ( $g, I$ ), defined by $\mathrm{d} \omega_{I}=-2 \theta \wedge \omega_{I}$, is
$$\theta=-\mathrm{d} \log |\xi-\eta| .$$
It follows that $\bar{\omega}:=(\xi-\eta)^{-2} \omega_{I}$ is closed, i.e., the pair $\left(\bar{g}=(\xi-\eta)^{-2} g, I\right)$ is Kähler. \(\square\)

In particular, on any ortho-toric Kähler surface, the anti-self-dual Weyl tensor-which is the self-dual Weyl tensor of $g$ for the orientation induced by $I$-is degenerate: $W^{-}=\kappa \omega_{I} \otimes_{0} \omega_{I}$, where $\kappa$ is the conformal scalar curvature of the Hermitian pair $(g, I)$.

Remark 3. The vector fields $K_{1}$ and $K_{2}$ are still Killing with respect to $\bar{g}$ and Hamiltonian with respect to $\bar{\omega}$, with momentum maps $-(1 / \xi-\eta)$ and $-(\xi+\eta) /(2(\xi-\eta))$ respectively. However, the Kähler metric $(\bar{g}, I)$ is not ortho-toric in general, as it can be checked using Lemma 9 below.

Combining Propositions 2, 3 with 8 and 9, we obtain the following theorem.
THEOREM 1. A Kähler surface is ortho-toric if and only if it admits a Hamiltonian 2-form whose associated Killing vector fields are independent. The Kähler structure is then given explicitly in terms of two arbitrary functions $F, G$ of one variable by (25)-(27).

Indeed, using (28)-(29), notice that, by definition, $J \mathrm{~d}(\xi+\eta)=I \mathrm{~d}(\xi-\eta)$, cf. Remark 2, so the Hamiltonian 2-form $\varphi$ is $\frac{1}{2}(\xi-\eta) \omega_{I}+(\xi+\eta) \omega$.

\subsection*{2.3. ORTHO-TORIC WEAKLY SELF-DUAL KÄHLER SURFACES}

The curvature of an ortho-toric Kähler surface is entirely determined by the scalar curvature $s$ of $g$, the conformal scalar curvature $\kappa$ of the Hermitian pair $(g, I)$, and the trace-free part $\rho_{0}$ of the Ricci form of $(g, J)$.

LEMMA 9. For any ortho-toric Kähler surface $(M, g, J, \omega), \rho_{0}$ is a multiple $\mu$ of the Kähler form $\omega_{I}$ of the Hermitian pair $(g, I)$, and $\mu, s, \kappa$ are given by
$$\begin{aligned}
& \mu=\frac{F^{\prime}(\xi)-G^{\prime}(\eta)}{2(\xi-\eta)^{2}}-\frac{F^{\prime \prime}(\xi)+G^{\prime \prime}(\eta)}{4(\xi-\eta)}, \\
& s=-\frac{F^{\prime \prime}(\xi)-G^{\prime \prime}(\eta)}{6(\xi-\eta)}, \\
& \kappa=-\frac{F^{\prime \prime}(\xi)-G^{\prime \prime}(\eta)}{6(\xi-\eta)}+\frac{F^{\prime}(\xi)+G^{\prime}(\eta)}{(\xi-\eta)^{2}}-\frac{2(F(\xi)-G(\eta))}{(\xi-\eta)^{3}} .
\end{aligned}$$
In particular, on the open subset of $M$ where $\mu$ has no zero, the anti-self-dual almost-complex structure determined by $\rho_{0}$ is equal to $I$.

Proof. From (27), we infer that the volume-form $v_{g}=\frac{1}{2} \omega \wedge \omega$ of $g$ is given by
$$v_{g}=-(\xi-\eta) \mathrm{d} \xi \wedge \mathrm{~d} \eta \wedge \mathrm{~d} t \wedge \mathrm{~d} z,$$
since $t$ and $z$ are the real parts of $J$-holomorphic coordinates. By putting $v_{0}=\mathrm{d} t \wedge$ $J \mathrm{~d} t \wedge \mathrm{~d} z \wedge J \mathrm{~d} z$, we have $\rho=-\frac{1}{2} \mathrm{~d} J \mathrm{~d} \log v_{g} / v_{0}$. Now according to (26),
$$v_{0}=-\frac{\xi-\eta}{F(\xi) G(\eta)} \mathrm{d} \xi \wedge \mathrm{~d} \eta \wedge \mathrm{~d} t \wedge \mathrm{~d} z,$$
and, hence, $v_{g} / v_{0}=F(\xi) G(\eta)$; this implies
$$\rho=-\frac{1}{2} \mathrm{~d} J \mathrm{~d} \log |F(\xi)|-\frac{1}{2} \mathrm{~d} J \mathrm{~d} \log |G(\eta)|,$$
from which (31) and (32) follow easily.
From (9) and (30), we get
$$\kappa=s-2 \frac{|\mathrm{~d} \xi|^{2}+|\mathrm{d} \eta|^{2}}{(\xi-\eta)^{2}}-\frac{\Delta(\xi-\eta)}{\xi-\eta} ;$$
on the other hand, we compute that
$$\Delta \xi=-\frac{F^{\prime}(\xi)}{\xi-\eta}, \quad \Delta \eta=\frac{G^{\prime}(\eta)}{\xi-\eta} ;$$
and we obtain (33). \(\square\)

PROPOSITION 10. An ortho-toric Kähler surface $M$ is extremal if and only if $F$ and $G$ are of the form
$$F(x)=k x^{4}+\ell x^{3}+A x^{2}+B_{1} x+C_{1}, \quad G(x)=k x^{4}+\ell x^{3}+A x^{2}+B_{2} x+C_{2},$$
in which case
$$s=-2 k(\xi+\eta)-\ell,$$
and $\left(\bar{g}=(\xi-\eta)^{-2} g, I\right)$ is an extremal Kähler metric as well.
Moreover, $M$ is
\begin{itemize}
\item[-] Bach-flat if and only if $4 k\left(C_{1}-C_{2}\right)=\left(B_{1}-B_{2}\right) \ell$;
\item[-] of constant scalar curvature if and only if $k=0$;
\item[-] scalar-flat (i.e., anti-self-dual) if and only if $k=\ell=0$.
\end{itemize}

Proof. Since the scalar curvature $s$ is a function of $\xi$ and $\eta, J \operatorname{grad}_{g} s$ belongs to the span of the Killing vector fields $K_{1}$ and $K_{2}$ and commutes with them; if it is itself a Killing vector field, it has to be a linear combination of $K_{1}$ and $K_{2}$ with constant coefficients, i.e. $s=a(\xi+\eta)+b \xi \eta+c$, where $a, b, c$ are constants. By (32), this implies (34). Finally, using (21), we easily compute that the anti-self-dual 2 -form associated to the Bach tensor of an ortho-toric extremal Kähler surface is
$$\tilde{B}=\frac{4 k\left(C_{1}-C_{2}\right)-\left(B_{1}-B_{2}\right) \ell}{2(\xi-\eta)^{2}} \omega_{I} .$$
Since $B$ is also $I$-invariant, the Kähler metric $(\bar{g}, I)$ is extremal as well (see Section 1.5). \(\square\)

EXAMPLE 1. For $k \neq 0$ and $4\left(C_{1}-C_{2}\right)=\left(B_{1}-B_{2}\right) \ell / k$, we obtain explicit Bachflat Kähler surfaces with nonconstant scalar curvature. These metrics are therefore not anti-self-dual, and for $B_{1} \neq B_{2}$ they are not self-dual either (note that a self-dual Kähler surface is bi-extremal and see the next Proposition). According to Section 1.5, the metric $\tilde{g}=(2 k(\xi+\eta)+\ell)^{-2} g$, which is defined on the open subset where $2 k(\xi+\eta)+\ell \neq 0$, is Einstein, Hermitian (but non-Kähler) with a locally defined toric isometric action.

PROPOSITION 11. An ortho-toric Kähler surface $M$ is bi-extremal if and only if $F$ and $G$ are of the form
$$\begin{aligned}
& F(x)=k x^{4}+\ell x^{3}+A x^{2}+B x+C_{1}, \\
& G(x)=k x^{4}+\ell x^{3}+A x^{2}+B x+C_{2},
\end{aligned}$$
in which case the Ricci form is given by $\rho=-2 k \varphi-\ell \omega$. Hence $M$ is weakly self-dual and is
\begin{itemize}
\item[-] self-dual if and only if $C_{1}=C_{2}$;
\item[-] Kähler-Einstein if and only if $k=0$;
\item[-] Ricci-flat if and only if $k=\ell=0$.
\end{itemize}

Proof. Since a bi-extremal surface is extremal, we may apply Proposition 10. We then compute
$$\begin{aligned}
& \mu=-k(\xi-\eta)+\frac{B_{1}-B_{2}}{2(\xi-\eta)^{2}}, \\
& p=4 k^{2} \xi \eta+k \ell(\xi+\eta)+\frac{\ell^{2}}{4}-k \frac{B_{1}-B_{2}}{\xi-\eta}+\frac{\left(B_{1}-B_{2}\right)^{2}}{4(\xi-\eta)^{4}} .
\end{aligned}$$
As in the proof of Proposition 10, $p$ cannot be a $J$-holomorphy potential unless it is a linear combination of $\xi+\eta$ and $\xi \eta$ with constant coefficients; this in turn is equivalent to the condition $B_{1}=B_{2}$. Since $\mu=-2 k \lambda$ and $s=-2 k \sigma-\ell$ it follows that $\rho=-2 k \varphi-\ell \omega$. Hence $\rho$ is a Hamiltonian and so $M$ is weakly self-dual by (4).

By substituting in the expression of $\kappa$ given by (33) we get $\kappa=$ $-\left(2\left(C_{1}-C_{2}\right)\right) /\left((\xi-\eta)^{3}\right)$; since the condition $W^{-}=0$ is equivalent to $\kappa=0$, the characterization of the self-dual case follows. Also $M$ is Einstein if and only if $\mu=0$, and so the last two assertions are immediate. \(\square\)

Remark 4. For $k \neq 0$, we can set $k=-\frac{1}{2}$ and $\ell=0$ by a simultaneous affine change of $\xi$ and $\eta$. In this case $\rho=\varphi$, and so the ortho-toric reduction is defined by $\rho$. However, not all weakly self-dual Kähler surfaces can be put in ortho-toric form; for example weakly self-dual metrics belonging to the general family of cohomogeneity-one extremal metrics considered by E. Calabi [14] are not in general orthotoric, since $K_{1}$ and $K_{2}$ are then collinear. We discuss this case in Section 3.

On the other hand, the examples with $k=0$ in the above Proposition show that among Kähler-Einstein metrics (which are weakly self-dual), there are some which can be put into ortho-toric form, because even though $\rho$ does not define an orthotoric reduction, there happens to be another Hamiltonian 2-form $\varphi$. If additionally $A=\ell=0$ or $C_{1}=C_{2}$, these examples in fact have cohomogeneity one and their ortho-toric form arises from a choice of maximal torus inside the isometry group. However, the other examples do not have additional symmetries and therefore appear to be new.

PROPOSITION 12. On an ortho-toric extremal Kähler surface $M$, the space of infinitesimal symmetries of the Kähler structure is generated by $K_{1}$ and $K_{2}$ (and infinitesimal rotations in this plane if they are globally defined), except in the following two cases:
\begin{itemize}
\item[(i)] $M$ is locally a complex space form, i.e., Kähler-Einstein and self-dual; or
\item[(ii)] $M$ is Ricci-flat (hence, anti-self-dual) and, locally, of cohomogeneity one.
\end{itemize}

In terms of $F$ and $G$, these two cases are respectively described by
$$F(x)=G(x)=\ell x^{3}+A x^{2}+B x+C ;$$
and
$$F(x)=B x+C_{1}, \quad G(x)=B x+C_{2} .$$

Proof. Suppose there exist a third infinitesimal symmetry of $M$, say $K_{3}$, which does not lie in the plane spanned by $K_{1}$ and $K_{2}$; then, we must have $\mathrm{d} s\left(K_{i}\right)=0$ and $\mathrm{d} \mu\left(K_{i}\right)=0$, for $i=1,2,3$; this implies that $\mathrm{d} s$ and $\mathrm{d} \mu$ are colinear; we then infer from (35) and (37) that we have $k=0$ and $B_{1}=B_{2}$ in (34), so that $M$ is Kähler-Einstein by Proposition 11.

If, in addition, $W^{-}=0$, we obtain (39) and $g$ is then a self-dual Kähler-Einstein surface, i.e., a complex space form.

If $W^{-}$does not vanish identically, on the open set where $W^{-} \neq 0$, the Hermitian pair $(g, I)$ is invariant under the action of the Killing vector fields $K_{i}$ 's, as $I$ is determined by the eigenform of $W^{-}$corresponding to its simple eigenvalue, cf. [21, 7]; then, $\kappa$ (a constant multiple of the simple eigenvalue of $W^{-}$), the square-norm $|\theta|^{2}$ of the Lee form $\theta$ of the pair ( $g, I$ ) as well as $\delta \theta$ are also invariant under the action of $K_{i}$ 's, $i=1,2,3$; we then have $\mathrm{d}|\theta|^{2} \wedge \mathrm{~d} \kappa=0$; by using (30) and Lemma 9, we can check that this implies that $F$ and $G$ satisfy (40); by Proposition 10, the corresponding ortho-toric Kähler surface is Ricci-flat and $\kappa=-\left(2\left(C_{1}-C_{2}\right)\right) /\left((\xi-\eta)^{3}\right)$; it then follows from (30) that $\theta=\frac{1}{3} \mathrm{~d} \ln |\kappa|$; in particular, $\mathrm{d}|\theta|^{2} \wedge \theta=0$; by [8, Theorem 1], this implies that the metric is of cohomogeneity one. Since $\kappa$ is non-zero, it is not constant, and so the metric is not homogeneous.

Evidently the two cases overlap when $C_{1}=C_{2}$ and $A=\ell=0$, in which case $g$ is flat. \(\square\)

Remark 5. In fact we do not need to assume a priori that $M$ is extremal in the above proof, as long as we assume that the additional symmetry preserves $\varphi$, hence $\xi-\eta$. Then $\mathrm{d} s$ and $\mathrm{d} \xi-\mathrm{d} \eta$ are collinear, from which it is easy to deduce that $M$ is extremal.

Let us now collect the results we have established so far about weakly self-dual Kähler surfaces.

THEOREM 2. Let $(M, g, J, \omega)$ be a weakly self-dual Kähler surface. Denote by $s, \lambda$, and $p=((s / 2)+\lambda)((s / 2)-\lambda)$, the (normalized) scalar curvature, the positive eigenvalue of the trace-free Ricci tensor $\mathrm{Ric}_{0}$, and the Pfaffian of the normalized Ricci tensor, respectively. Then,
(i) $K_{1}:=J \operatorname{grad}_{g} s$ and $K_{2}:=J \operatorname{grad}_{g} p$ are commuting Killing vector fields, and on any simply connected open subset where $K_{1}$ and $K_{2}$ are linearly independent, the functions $\xi:=(s / 2)+\lambda, \eta:=(s / 2)-\lambda, t, z$ form a globally defined coordinate system with respect to which the Kähler structure $(g, J, \omega)$ is
$$g=(\xi-\eta)\left(\frac{\mathrm{d} \xi^{2}}{F(\xi)}-\frac{\mathrm{d} \eta^{2}}{G(\eta)}\right)+\frac{1}{\xi-\eta}\left(F(\xi)(\mathrm{d} t+\eta \mathrm{d} z)^{2}-G(\eta)(\mathrm{d} t+\xi \mathrm{d} z)^{2}\right),$$
$$\begin{aligned}
& J \mathrm{~d} \xi=\frac{F(\xi)}{\xi-\eta}(\mathrm{d} t+\eta \mathrm{d} z), \quad J \mathrm{~d} t=-\frac{\xi \mathrm{d} \xi}{F(\xi)}-\frac{\eta \mathrm{d} \eta}{G(\eta)}, \\
& J \mathrm{~d} \eta=\frac{G(\eta)}{\eta-\xi}(\mathrm{d} t+\xi \mathrm{d} z), \quad J \mathrm{~d} z=\frac{\mathrm{d} \xi}{F(\xi)}+\frac{\mathrm{d} \eta}{G(\eta)}, \\
& \omega=\mathrm{d} \xi \wedge(\mathrm{~d} t+\eta \mathrm{d} z)+\mathrm{d} \eta \wedge(\mathrm{~d} t+\xi \mathrm{d} z),
\end{aligned}$$
where
$$\begin{aligned}
& F(x)=k x^{4}+\ell x^{3}+A x^{2}+B x+C_{1}, \\
& G(x)=k x^{4}+\ell x^{3}+A x^{2}+B x+C_{2} .
\end{aligned}$$
(ii) Conversely, each almost Kähler structure $(g, J, \omega)$ described by (41)-(45) is Kähler and weakly self-dual with
$$s=-2 k(\xi+\eta)-\ell, \quad p=4 k^{2} \xi \eta+k \ell(\xi+\eta)+\frac{\ell^{2}}{4},$$
so that $K_{1}=\partial / \partial t$ and $K_{2}=\partial / \partial z$.
(iii) The Kähler structure described by (41)--(45) is self-dual if and only if $C_{1}=C_{2}$.

In the self-dual case, we recover the general expression found by Bryant [13, Section 4.3.2] depending on an arbitrary polynomial of degree 4 .

\section*{3. Kähler Surfaces of Calabi Type}

\subsection*{3.1. HAMILTONIAN 2-FORMS AND THE CALABI CONSTRUCTION}

In this section we classify weakly self-dual Kähler surfaces of nowhere constant scalar curvature $s$, but for which $p$ and $s$ are not independent. As in the previous section (when we assumed $p$ and $s$ were independent) we do this by finding an explicit formula for a Kähler surface $(M, g, J, \omega)$ with a Hamiltonian 2-form $\varphi=\varphi_{0}+\frac{3}{2} \sigma \omega$ such that $K_{1}:=J \operatorname{grad}_{g} \sigma$ has no zero, but $K_{2}:=J \operatorname{grad}_{g} \pi=b K_{1}$, where $\pi$ is the Pfaffian of $\tilde{\varphi}$ and $b$ is (necessarily) constant.

The general theory of Kähler surfaces with a Hamiltonian 2-form, described in Section 1, applies equally to this case. In particular, since $K_{1}$ has no zero, we may still write $\pi=\xi \eta$ and $\sigma=\xi+\eta$ for the trace and Pfaffian of $\tilde{\varphi}$, and $\mathrm{d} \xi$ and $\mathrm{d} \eta$ are orthogonal by Proposition 3.

On the other hand, the constructions of Section 2 definitely fail, because $K_{1}$ and $K_{2}$ are no longer independent: $\pi$ is an affine function of $\sigma$, so $\xi$ and $\eta$ are not independent functions. Therefore, $\mathrm{d} \xi$ and $\mathrm{d} \eta$, in addition to being orthogonal, are collinear! This is not a contradiction: we deduce that either $\xi$ or $\eta$ is constant. Since $\pi=\xi(\sigma-\xi)=\eta(\sigma-\eta)$, this constant is the constant $b$ above, so that $\pi=b(\sigma-b)$ and $\lambda= \pm \frac{1}{2}(\sigma-2 b)$.

We observe that $K_{1}$ is an eigenvector of $-\varphi_{0} \circ J$, for the eigenvalue $\lambda$, and the conformally Kähler anti-self-dual complex structure $I$ is characterized as follows:
$I$ coincides with $J$ on the distribution generated by $K_{1}$ and $J K_{1}$, but with $-J$ on the orthogonal distribution. Hence, we are in the following situation.

DEFINITION 8. A Kähler surface $(M, g, J, \omega)$ is said to be of Calabi type if it admits a nonvanishing Hamiltonian Killing vector field $K$ such the almost-Hermitian pair $(g, I)$-with $I$ equal to $J$ on the distribution spanned by $K$ and $J K$, but $-J$ on the orthogonal distribution-is conformally Kähler.

It is straightforward to obtain an explicit formula for Kähler metrics of Calabi type, using the LeBrun form of a Kähler metric with a Hamiltonian Killing vector field [37].

PROPOSITION 13. Let $(M, g, J, \omega)$ be a Kähler surface of Calabi type. Then the Kähler structure is given locally by
$$\begin{aligned}
g & =(a z-b) g_{\Sigma}+w(z) \mathrm{d} z^{2}+w(z)^{-1}(\mathrm{~d} t+\alpha)^{2}, \\
\omega & =(a z-b) \omega_{\Sigma}+\mathrm{d} z \wedge(\mathrm{~d} t+\alpha),
\end{aligned}$$
where $z$ is the momentum map of the Killing vector field $K, t$ is a function on $M$ with $\mathrm{d} t(K)=1, w$ is a function of one variable, $g_{\Sigma}$ is a metric on 2-manifold $\Sigma$ with area form $\omega_{\Sigma}, \alpha$ is a 1 -form on $\Sigma$ with $\mathrm{d} \alpha=a \omega_{\Sigma}$, and $a, b$ are constant. Conversely equations (46)-(47) define a Kähler structure of Calabi type with $K=\partial / \partial t$, for any $g_{\Sigma}$ and $V$.

Proof. The proof follows LeBrun's description [37] of Kähler metrics with a Hamiltonian Killing vector field $K$. Supposing first that $(g, J, \omega)$ is only almost Hermitian, with a Killing vector field $K=J \operatorname{grad} z$, and that $K-i J K$ is holomorphic, so that the complex quotient is locally a Riemann surface $\Sigma$. Introducing a local holomorphic coordinate $x+i y$ on $\Sigma$, we may write
$$\begin{aligned}
& g=\mathrm{e}^{u} w\left(\mathrm{~d} x^{2}+\mathrm{d} y^{2}\right)+w \mathrm{~d} z^{2}+w^{-1}(\mathrm{~d} t+\alpha)^{2}, \\
& J \mathrm{~d} x=\mathrm{d} y, \quad J \mathrm{~d} z=w^{-1}(\mathrm{~d} t+\alpha), \\
& \omega=\mathrm{e}^{u} w \mathrm{~d} x \wedge \mathrm{~d} y+\mathrm{d} z \wedge(\mathrm{~d} t+\alpha) .
\end{aligned}$$
where $\operatorname{d} t(K)=1, \alpha$ is an invariant 1-form with $\alpha(K)=0$, and $u, w$ are functions of $x, y, z$. The almost Hermitian structure $I$ is given by
$$I \mathrm{~d} x=-\mathrm{d} y, \quad I \mathrm{~d} z=w^{-1}(\mathrm{~d} t+\alpha),$$
with Kähler form
$$\omega_{I}=-\mathrm{e}^{u} w \mathrm{~d} x \wedge \mathrm{~d} y+\mathrm{d} z \wedge(\mathrm{~d} t+\alpha) .$$
We now impose the condition that $(g, J, \omega)$ and $\left(\bar{g}=\lambda^{-2} g, I, \bar{\omega}=\lambda^{-2} \omega_{I}\right)$ are Kähler for some nonvanishing function $\lambda$. Now $\mathrm{d} \omega=0$ if and only if
$$\left(\mathrm{e}^{u} w\right)_{z} \mathrm{~d} z \wedge \mathrm{~d} x \wedge \mathrm{~d} y=\mathrm{d} z \wedge \mathrm{~d} \alpha,$$
while $\lambda^{-2} \omega_{I}$ is closed if and only if
$$\begin{aligned}
\lambda \mathrm{d} z & \wedge \mathrm{~d} \alpha+\left(\left(\mathrm{e}^{u} w\right)_{z} \lambda-2 \lambda_{z} \mathrm{e}^{u} w\right) \mathrm{d} z \wedge \mathrm{~d} x \wedge \mathrm{~d} y+ \\
& +2 \lambda_{x} \mathrm{~d} x \wedge \mathrm{~d} z \wedge(\mathrm{~d} t+\alpha)+2 \lambda_{y} \mathrm{~d} y \wedge \mathrm{~d} z \wedge(\mathrm{~d} t+\alpha)+2 \lambda_{t} \mathrm{~d} t \wedge \omega_{I}=0 .
\end{aligned}$$
In the presence of (48), (49) is equivalent to
$$\left(\mathrm{e}^{u} w\right)_{z} \lambda=\lambda_{z} \mathrm{e}^{u} w, \quad \lambda_{x}=\lambda_{y}=\lambda_{t}=0,$$
which holds if and only if $\lambda=\lambda(z)$ and $\mathrm{e}^{u} w=h \lambda$ for some function $h(x, y)$.
Let $\theta$ be the complex 1-form $w \mathrm{~d} z+i(\mathrm{~d} t+\alpha)$. Then, since $\mathrm{d} x \pm i \mathrm{~d} y$ is closed, the complex structures $I$ and $J$ are integrable if and only if $\mathrm{d} \theta$ belongs to the ideals generated by $\{\theta, \mathrm{d} x-i \mathrm{~d} y\}$ and by $\{\theta, \mathrm{d} x+i \mathrm{~d} y\}$ respectively. Since $\mathrm{d} \theta(\partial / \partial t, \cdot)=0$, these conditions force $(\mathrm{d} x-i \mathrm{~d} y) \wedge \mathrm{d} \theta$ and $(\mathrm{d} x+i \mathrm{~d} y) \wedge \mathrm{d} \theta$ to vanish. Hence $I$ is integrable if and only if
$$\mathrm{d} \alpha=-w_{x} \mathrm{~d} y \wedge \mathrm{~d} z+w_{y} \mathrm{~d} x \wedge \mathrm{~d} z+f \mathrm{~d} x \wedge \mathrm{~d} y$$
while $J$ is integrable if and only if
$$\mathrm{d} \alpha=w_{x} \mathrm{~d} y \wedge \mathrm{~d} z-w_{y} \mathrm{~d} x \wedge \mathrm{~d} z+f \mathrm{~d} x \wedge d y ;$$
here $f$ is an arbitrary function. Hence $I$ and $J$ are both integrable if and only if
$$w_{x}=w_{y}=0 \quad \text { and } \quad \mathrm{d} \alpha=f \mathrm{~d} x \wedge \mathrm{~d} y$$
and $f$ is necessarily a function of $x, y$ only.
Putting together (48), (50), and (53), we see that $(g, J, \omega)$ is of Calabi type, with Killing vector field $K$, if and only if $\mathrm{e}^{u} w=h(x, y) \lambda(z)$, with $\mathrm{d} \alpha=h(x, y) \lambda_{z}, \lambda_{z z}=0$ and $w_{x}=w_{y}=0$, so that $\lambda=a z-b$ for constants $a, b$ and $w=w(z)$.

Using the freedom in the choice of $t$, we may then assume $\alpha$ is a 1-form on $\Sigma$, while $g_{\Sigma}=h(x, y)\left(\mathrm{d} x^{2}+\mathrm{d} y^{2}\right)$ is a metric on $\Sigma$, and the result follows. \(\square\)

This Proposition shows that Kähler metrics of Calabi type are essentially the same as metrics arising from the well-known Calabi construction [14] of metrics on the total space of a Hermitian line bundle over a Riemann surface. In this interpretation, the Killing vector field $K$ generates the natural circle action on the line bundle and the Kähler form is
$$\omega_{\Sigma}+\mathrm{d} J \mathrm{~d} f$$
for a function $f$ of the fibre norm $r$. Since $-\mathrm{d} J \mathrm{~d} \log r$ is the curvature of the line bundle, which is basic, the momentum map $z$ of $K$ is also a function of $r$. Hence we may locally view $f$ as a function of $z$, so that, if we write $J \mathrm{~d} z=\mathrm{d} t+\alpha$ where $\mathrm{d} t(K)=1$ and $\alpha$ is basic,
$$\mathrm{d} J \mathrm{~d} f=\left(\frac{f^{\prime}(z)}{w(z)}\right)_{z} \mathrm{~d} z \wedge(\mathrm{~d} t+\alpha)+\frac{f^{\prime}(z)}{w(z)} \mathrm{d} \alpha .$$
Therefore, in Proposition 13, setting $b=-1$ without loss of generality, we have $f^{\prime}(z)=z w(z)$.

The metrics of Proposition 13 certainly admit a Hamiltonian 2-form, namely $\varphi=(a z-b) \omega_{I}+3 a z \omega$. Hence, $\sigma=2 a z$ and $\lambda=a z-b$, so that $\xi=2 a z-b$ and $\eta=b$. The Hamiltonian Killing vector fields associated to $\varphi$ both vanish when $a=0$. On the other hand, for $a$ nonzero, we can use the freedom in the choice of $z$ to set $a=1$ and $b=0$.
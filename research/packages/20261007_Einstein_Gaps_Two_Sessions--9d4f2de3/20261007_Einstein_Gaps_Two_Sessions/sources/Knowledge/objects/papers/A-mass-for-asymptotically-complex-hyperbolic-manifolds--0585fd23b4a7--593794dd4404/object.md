# A mass for asymptotically complex hyperbolic manifolds

- Category: papers
- Identity: arxiv:0911.0306
- Content status: fulltext_ok

---

---
source_file: 0911_0306.pdf
converter: mathpix
format: mmd
---

\section*{A MASS FOR ASYMPTOTICALLY COMPLEX HYPERBOLIC MANIFOLDS.}

\begin{abstract}
We prove a positive mass theorem for complete Kähler manifolds that are asymptotic to the complex hyperbolic space.
\end{abstract}

\section*{Contents}

Introduction
\begin{itemize}
\item[1.] The real hyperbolic case.
\item[2.] A complex hyperbolic connection.
\item[2.1.] The connection.
\item[2.2.] The model case.
\item[2.3.] Kählerian Killing spinors.
\item[3.] Toward a mass.
\item[3.1.] The "mass integral" at infinity.
\item[3.2.] The mass linear functional.
\item[4.] The case of even-dimensional manifolds.
\item[4.1.] The twisted Kählerian Killing spinors.
\item[4.2.] The positive mass theorem.
\end{itemize}

Appendix : an example.

References

\section*{Introduction}

The aim of this paper is to provide a positive mass theorem in the realm of asymptotically complex hyperbolic Kähler manifolds, extending previous results by M. Herzlich [Her] and Boualem-Herzlich [BH]. Before explaining them, let us recall the history of the subject.

The classical positive mass theorem finds its roots in general relativity [ADM] and deals with asymptotically Euclidean manifolds, namely complete Riemannian manifolds $\left(M^{n}, g\right)$ whose geometry at infinity tends to that of the flat Euclidean space : $M$ is diffeomorphic to $\mathbb{R}^{n}$ outside a compact set and $g$ goes to $g_{\mathbb{R}^{n}}$ at infinity. Under a nonnegativity assumption on the curvature $\left(\mathrm{Scal}_{g} \geq 0\right)$, the positive mass theorem roughly asserts that such manifolds possess a global Riemannian invariant, which is called a mass, which is obtained by computing the limit of integrals over larger and larger spheres, which is a non-negative number and which vanishes only when the manifold is isometric to the model flat space. This "Euclidean mass" is given in some

\footnotetext{
Date: September 21, 2018.
2000 Mathematics Subject Classification.
The authors benefit from the ANR grant GeomEinstein, ANR-06-BLAN-0154-02.
}
chart at infinity by
$$\mu_{g}=-\frac{1}{4} \lim _{R \longrightarrow \infty} \int_{\mathbb{S}_{R}} *(\operatorname{div} g+d \operatorname{Tr} g),$$
where the sphere, Hodge star, the divergence and the trace are defined with respect to the Euclidean metric $g_{\mathbb{R}^{n}}$ at infinity. It is not obvious that this quantity depends only on $g$ and not on the chart but [Bart] proved it. We refer to [SY1, SY2, Wit, Bart, LP] for details and "classical" proofs and to Loh for a more recent and more general treatment. The mathematical interest of such a theorem is the rigidity result it involves: under a nonnegativity assumption on the curvature, it asserts a model metric at infinity (the Euclidean metric, here) cannot be approached at any rate, the obstruction being precisely the mass. Another striking feature of this theorem is its role as a key step in the first proof of the Yamabe theorem [LP] ; see also [ST] for a nice application of the positive mass theorem to obtain a rigidity result for compact manifolds with boundary.

It is possible to extend these ideas behind this theorem in several contexts, involving different models at infinity. The authors of [MO, AD, CH] studied the case of manifolds whose model at infinity is the real hyperbolic space $\mathbb{R} H^{n}$. More sophisticated models are also considered in [Dai, Min]. The notion of real hyperbolic mass introduced in [CH] is at the very root of our work so we need to explain what it looks like (note it is more general than what follows). Basically, while the Euclidean mass (1) is a single number, the real hyperbolic mass appears naturally as a linear functional on some finite dimensional vector space $\mathcal{N}$, attached to the model at infinity, $\mathbb{R} H^{n}$. More precisely, [CH] defines $\mathcal{N}$ as the set of functions $u$ on $\mathbb{R} H^{n}$ such that $\operatorname{Hess}_{\mathbb{R} H^{n}} u=u g_{\mathbb{R} H^{n}}$ and the mass linear functional is given by
$$\mu_{g}(u)=-\frac{1}{4} \lim _{R \longrightarrow \infty} \int_{\mathbb{S}_{R}} *\left[(\operatorname{div} g+d \operatorname{Tr} g) u-\operatorname{Tr}\left(g-g_{\mathbb{R} H^{n}}\right) d u+\left(g-g_{\mathbb{R} H^{n}}\right)(\operatorname{grad} u, .)\right]$$
where the right-hand side is computed with respect to the real hyperbolic metric $g_{\mathbb{R}} H^{n}$ at infinity. It turns out that $\mathcal{N}$ can be interpreted as the set of parallel sections for some natural vector bundle $\mathcal{E}$, endowed with a natural connection $\nabla^{R H}$ preserving a natural Lorentz metric $h$ : if you see $\mathbb{R} H^{n}$ as a hypersurface in Minkowski space $\mathbb{R}^{n, 1}$, then $(\mathcal{E}, h)$ is simply the restriction of the tangent bundle $T \mathbb{R}^{n, 1}$ and $\nabla^{R H}$ is induced by the flat connection on Minkowki space ; from this point of view, $\mathcal{N}$ identifies naturally with $\mathbb{R}^{n, 1}$. We will give more details on this picture in the first section of this text and explain why it is natural that the mass belongs to the dual of this space $\mathcal{N}$ and why the formula above is a relevant geometric invariant. The basic idea is that any Riemannian manifold carries a natural connection $\nabla^{R H}$ that is flat iff the manifold is (locally) hyperbolic ; the mass appears naturally as an obstruction to the construction of parallel sections for this connection.

The model at infinity we wish to consider is the complex hyperbolic space $\mathbb{C} H^{m}$, which is a counterpart of the real hyperbolic space $\mathbb{R} H^{n}$ in complex geometry. Up to scale, it is indeed the unique simply-connected complete Kähler manifold with constant holomorphic sectional curvature. To be concrete, let us recall that $\mathbb{C} H^{m}$ can be seen as the unit ball in $\mathbb{C}^{m}$, endowed with its standard complex structure $J$ and with the Kähler metric
$$g_{\mathbb{C} H^{m}}=g_{\mathbb{C} H^{m}}=\frac{1}{\left(1-s^{2}\right)^{2}}\left(d s^{2}+(J d s)^{2}+s^{2}\left(1-s^{2}\right) g_{F S}\right),$$
where $s$ is the radial coordinate in $\mathbb{C}^{m}$ and $g_{F S}$ is the Fubini-Study metric of $\mathbb{C} P^{m-1}$, pulled-back to $\mathbb{C}^{m} \backslash\{0\}$. Setting $s=\tanh r$, we obtain $\mathbb{C} H^{m}$ as the complex manifold $\mathbb{C}^{m}$ endowed with
$$g_{\mathbb{C} H^{m}}=d r^{2}+(\sinh 2 r)^{2} \eta^{2}+(\sinh r)^{2} g_{F S}$$
where $\eta=-\frac{J d r}{\sinh 2 r}$ is the standard contact form on $\mathbb{S}^{2 m-1}$. This is an Einstein metric with scalar curvature $-4 m(m+1)$ - the holomorphic sectional curvature is -4. The most useful description of $\mathbb{C} H^{m}$ for us is yet another one. Let $\mathbb{C}^{m, 1}$ denote the vector space $\mathbb{C}^{m+1}$ endowed with a Hermitian form $h$ of (complex) signature $(m, 1)$. Then the level set $h=-1$ in $\mathbb{C}^{m, 1}$, endowed with the induced metric, is a well-known Lorentz manifold, called Anti-de-Sitter space $A d S^{2 m, 1}$. The quotient of $A d S^{2 m, 1}$ by the scalar action of $\mathbb{S}^{1}$ is then a Riemannian manifold and it is precisely $\mathbb{C} H^{m}$.

In this paper, we define asymptotically complex hyperbolic manifolds as complete Kähler manifolds $\left(M^{2 m}, g, J\right)$ such that:
\begin{itemize}
\item[(i)] $M$ minus a compact subset is biholomorphic to $\mathbb{C} H^{m}$ minus a ball and,
\item[(ii)] through this identification, $g-g_{\mathbb{C} H^{m}}=\mathcal{O}\left(e^{-a r}\right)$ with $a>m+\frac{1}{2}$ (in $C^{1, \alpha}$ ).
\end{itemize}
Note the definition in [Her], while apparently weaker, is indeed equivalent (cf. the remark after Definition 3.1). The papers [Her, BH] prove rigidity results about asymptotically complex hyperbolic manifolds that look like the rigidity part (the vanishing mass part) of a positive mass theorem. What is the mass in this setting ?

In complete analogy with the real hyperbolic case, we will see the mass as a linear functional on some natural finite-dimensional vector space $\mathcal{N}$ attached to the model at infinity, $\mathbb{C} H^{m}$. This vector space $\mathcal{N}$ is best described as a set of parallel sections for some natural connection $\nabla^{C H}$ on some natural vector bundle $\mathcal{E}$ over $\mathbb{C} H^{m}$. The vector bundle $\mathcal{E}$ is indeed $\Lambda_{J}^{2} \mathbb{C} H^{m} \oplus T \mathbb{C} H^{m} \oplus \mathbb{R}$ and the relevant connection comes from the flat connection on $\mathbb{C}^{m, 1}$. Details will be given in the text. To keep this introduction short, let us just point out that $\mathcal{N}$ identifies naturally to the vector space $\Lambda_{J}^{2} \mathbb{C}^{m, 1}$ of $J$-invariant 2 -forms on $\mathbb{C}^{m, 1}$ and also admits a description as the set of functions $u$ satisfying a natural third-order equation. Then we define the complex hyperbolic mass by
$$\mu_{g}(u)=-\frac{1}{4} \lim _{R \longrightarrow \infty} \int_{\mathbb{S}_{R}} *\left[(\operatorname{div} g+d \operatorname{Tr} g) u-\frac{1}{2} \operatorname{Tr}\left(g-g_{\mathbb{C} H^{m}}\right) d u\right],$$
where everything on the right-hand side is computed with respect to the complex hyperbolic metric $g_{\mathbb{C} H^{m}}$ at infinity. The following positive mass theorem holds in this context.

Theorem 0.1 - Let $(M, g, J)$ be a spin asymptotically complex hyperbolic manifold with $\operatorname{Scal}_{g} \geq \operatorname{Scal}_{g_{\text {CH }} m}$. When the complex dimension of $M$ is even, we also assume that $M$ is contractible. Then $\mu_{g}$ is a well defined linear functional, up to an automorphism of the model. It vanishes if and only if ( $M, g, J)$ is the complex hyperbolic space.

The mass also satisfies a nonnegativity property : it takes non-negative values on some distinguished orbits of the action of $P U(m, 1)$. Under these assumptions, the mass may very well take infinite values : we then decide that is infinite and the finiteness of the mass does not depend on the choice of the chart at infinity. A simple criterion for the mass to be finite is that the rate of fall-off to the model metric at infinity be sufficiently fast : $a \geq 2 m+1$. A consequence of the positive mass theorem is that if $a>2 m+1$, then $(M, g, J)$ is complex hyperbolic ; it is the object of [Her, BH]. Our viewpoint yields a different proof, maybe more direct.

The spin assumption is classical : we need spinors to implement Witten's techniques [Wit]. The additional topological assumption in the even dimensional case is quite technical but could be weakened ; we refer to the text for a more precise statement. This assumption was already used in [BH]. Basically, Witten's techniques require some "special" spinors to exist on the model. Complex hyperbolic spaces of odd dimension possess such distinguished spinors, called Kählerian Killing spinors. Such spinors do not exist in the even dimensional case, so we need an extra trick. This has a cost : an additional assumption.

Let us make a general remark. The previous positive mass theorems were very related to - if not completely immersed into - physical ideas. The asymptotically complex hyperbolic realm does not share this feature (yet). We feel it is all the more interesting to observe that the very physical idea of a positive mass theorem carries over to purely mathematical settings. It might indicate that there is a general mechanism, waiting for new applications.

The structure of the paper is as follows. In a first section, we will discuss the real hyperbolic case and explain how the introduction of a natural hyperbolic connection gives a slightly different proof of the hyperbolic positive mass theorem in [CH]. This case will also serve as a helpful guide for the complex case. In a second section, we will introduce the complex hyperbolic connection and describe its basic features and in particular how it interacts with the so-called Kählerian Killing spinors. A third section is devoted to the proof of the complex hyperbolic positive mass theorem in odd complex dimensions. A short fourth section will describe how to extend these arguments to the even dimensions. Finally, an appendix describes an example.

Acknowledgements. The authors would like to thank Marc Herzlich for bringing the problem to their attention, but also Olivier Biquard, Elisha Falbel and Paul Gauduchon for useful discussions.

\section*{1. The real hyperbolic case.}

In this section, we briefly review some aspects of [CH]. The result mentioned here is not new, but we feel that the reformulation we propose might be useful. It is indeed quite simple and turns out to generalize to the complex hyperbolic setting. The basic question we address is the following : given a Riemannian manifold that looks like the hyperbolic space, how can one ensure that it is actually the hyperbolic space ? The approach suggested here consists in finding a connection characterizing the hyperbolic space, in that it is flat only on a (locally) hyperbolic manifold, and then try to build parallel sections for this connection.

Let us start with a Riemannian manifold $\left(M^{n}, g\right)$. We consider the vector bundle $\mathcal{E}=T^{*} M \oplus \mathbb{R}$ obtained as the sum of the cotangent bundle and of the trivial real line bundle. It can be endowed with a natural Lorentz metric $h$ : for $\alpha \in T_{x}^{*} M$ and $u \in \mathbb{R}$, we set
$$h(\alpha, u)=|\alpha|_{g}^{2}-u^{2} .$$
We will say that an element $(\alpha, u)$ of $\mathcal{E}$ is future light-like if $h(\alpha, u)=0$ and $u>0$. We then define a connection $\nabla^{R H}$ on $\mathcal{E}$ : if $(\alpha, u)$ is a section of $\mathcal{E}$ and $X$ a vector field on $M$,
$$\nabla_{X}^{R H}\binom{\alpha}{u}:=\binom{\nabla_{X}^{g} \alpha-u g(X, .)}{d_{X} u-\alpha(X)} .$$
This connection is metric with respect to $h$. Moreover, an easy computation shows that its curvature vanishes if and only if $g$ has sectional curvature -1, which is why
we call this connection hyperbolic. In case $(M, g)$ is $\left(\mathbb{R} H^{n}, g_{\mathbb{R}} H^{n}\right)$, this construction is clear : $\mathbb{R} H^{n}$ is embedded into Minkowski space $\mathbb{R}^{n, 1}$ as the hypersurface
$$\left\{x \in \mathbb{R}^{n+1} / x_{1}^{2}+\cdots+x_{n}^{2}-x_{n+1}^{2}=-1 \text { and } x_{n+1}>0\right\} ;$$
then $\mathcal{E}=\mathcal{E}_{\mathbb{R} H^{n}}$ identifies with $\left.T \mathbb{R}^{n, 1}\right|_{\mathbb{R} H^{n}}, h$ is induced by the Minkowski metric and $\nabla^{R H}$ by the flat Minkowski connection.

Remark 1. Note that this construction admits an obvious spherical analogue. On the same vector bundle, one can consider the obvious positive definite metric and change a sign in the formula for the connection to make it metric, which results in a spherical connection : it is flat if and only if $(M, g)$ is locally isometric to the sphere with constant sectional curvature +1.

Observe also that a section $(\alpha, u)$ of $\mathcal{E}$ is parallel for this connection if and only if $\alpha=d u$ and $\operatorname{Hess}_{g} u=u g$. We call $\mathcal{N}$ the space of parallel sections for $\nabla^{R H}$ and $\mathcal{N}^{+}$ the subset of future light-like elements of $\mathcal{N}$. Observe that in the model case, $\mathcal{N}_{\mathbb{R} H^{n}}$ identifies with $\mathbb{R}^{n, 1}$ and $\mathcal{N}_{\mathbb{R} H^{n}}^{+}$is simply the future isotropic half-cone.
Remark 2. The spherical analogue yields the equation $\operatorname{Hess}_{g} u=-u g$, which is called Obata equation and has been much studied (Oba, Gal]), in relation with the bottom of the spectrum of Riemannian manifolds with $\operatorname{Ric} \geq \operatorname{Ric}_{\mathbb{S}^{n}}$. Obata equation admits a non-trivial solution only on the standard sphere.

We are interested in trying to produce parallel sections of $\mathcal{E}$. To do this, we follow an indirect path, assuming $M$ to be spin and looking at a related spinorial connection. An imaginary Killing spinor $\psi$ on a spin Riemannian manifold $(M, g)$ is a section of the spinor bundle such that
$$\nabla^{g} \psi+\frac{i}{2} \psi=0 .$$
The space of Killing spinors is denoted by $\mathcal{K}$. The following crucial observation follows from a straightforward computation :
$$\nabla^{g} \psi+\frac{i}{2} \psi=0 \Rightarrow \nabla^{R H}\binom{d|\psi|_{g}^{2}}{|\psi|_{g}^{2}}=0 .$$
In other words, we obtain a map $Q: \mathcal{K} \longrightarrow \mathcal{N}$ by setting $Q(\psi)=\left(d|\psi|^{2},|\psi|^{2}\right)$.
To understand the relevance of imaginary Killing spinors, we must describe them on the model $\mathbb{R} H^{n}$ : basically, they are induced by the constant spinors of $\mathbb{R}^{n, 1}$ and they trivialize the spinor bundle of $\mathbb{R} H^{n}$ [CH]. Using explicit formulas (cf. [CH]), one can see that $\mathcal{N}_{\mathbb{R} H^{n}}^{+}$lies inside $Q_{\mathbb{R} H^{n}}\left(\mathcal{K}_{\mathbb{R} H^{n}}\right)$; indeed, it is sufficient to prove that one of the Killing spinors is mapped into $\mathcal{N}_{\mathbb{R} H^{n}}^{+}$and then use the equivariance of $Q$ with respect to the natural actions of $O^{+}(n, 1)$, together with the transitivity of $O^{+}(n, 1)$ on $\mathcal{N}_{\mathbb{R} H^{n}}^{+}$.

Now assume the complete Riemannian manifold $(M, g)$ is asymptotically hyperbolic in the following sense : $M$ minus a compact is diffeomorphic to $\mathbb{R} H^{n}$ minus a ball and, through this diffeomorphism, $g=g_{\mathbb{R} H^{n}}+\mathcal{O}\left(e^{-a r}\right)$ with $a>\frac{n+1}{2}$ in $C^{1, \alpha}$ ( $r$ is the distance to some point in $\mathbb{R} H^{n}$ ). We further assume that the scalar curvature $\operatorname{Scal}_{g}$ of $(M, g)$ is greater than or equal to $\operatorname{Scal}_{g_{\mathbb{R} H^{n}}}$. Then [CH] proves that for any Killing spinor $\psi$ on $\mathbb{R} H^{n}$, one can find a unique spinor $\tilde{\psi}$ that is asymptotic to $\psi$ and harmonic for some natural Dirac operator. A Witten's like argument, based on Lichnerowitz
formula, then leads to
$$\int_{M}\left(\left|\nabla^{g} \tilde{\psi}+\frac{i}{2} \tilde{\psi}\right|^{2}+\frac{1}{4}\left(\operatorname{Scal}_{g}-\operatorname{Scal}_{g_{\mathbb{R} H^{n}}}\right)|\tilde{\psi}|^{2}\right)=\lim _{R \rightarrow \infty} \int_{\mathbb{S}_{R}} \ldots$$
The right hand side can be computed explicitly : it is
$$\begin{aligned}
\mu_{g}\left(Q_{\mathbb{R} H^{n}}(\psi)\right)= & -\frac{1}{4} \lim _{R \longrightarrow \infty} \int_{\mathbb{S}_{R}} *\left[(\operatorname{div} g+d \operatorname{Tr} g)|\psi|^{2}\right. \\
& \left.-\operatorname{Tr}\left(g-g_{\mathbb{R} H^{n}}\right) d u+\left(g-g_{\mathbb{R} H^{n}}\right)\left(d|\psi|^{2}, .\right)\right],
\end{aligned}$$
where the sphere, the Hodge star, the divergence, the trace and the identification between vectors and forms on the right-hand side are taken with respect to $g_{\mathbb{R}} H^{n}$. Since $\mathcal{N}_{\mathbb{R} H^{n}}^{+} \subset Q_{\mathbb{R} H^{n}}\left(\mathcal{K}_{\mathbb{R} H^{n}}\right)$, it follows that $\mu$ yields a linear functional on the linear span of $\mathcal{N}_{\mathbb{R} H^{n}}^{+}$, namely on $\mathcal{N}_{\mathbb{R} H^{n}} \cong \mathbb{R}^{n, 1}$. In view of (5), it is clearly non-negative on $\mathcal{N}_{\mathbb{R} H^{n}}^{+}$. Besides, if $\mu$ vanishes, the left-hand side of (5) is zero, so that every $\tilde{\psi}$ is a Killing spinor on $(M, g)$; then, in view of (4), for any element $\sigma=Q_{\mathbb{R} H^{n}}(\psi)$ of $\mathcal{N}_{\mathbb{R} H^{n}}^{+}$, there is an element $\tilde{\sigma}=Q_{g}(\tilde{\psi})$ of $\mathcal{N}_{g}$ that is asymptotic to $\sigma$. As a consequence, $\mathcal{N}_{g}$ has maximal dimension, which implies that $(M, g)$ is (locally) hyperbolic. In view of its asymptotic, it is bound to be $\mathbb{R} H^{n}$.

Theorem 1.1 ([CH]) - Let $\left(M^{n}, g\right)$ be an asymptotically hyperbolic spin manifold, with $\operatorname{Scal}_{g} \geq \operatorname{Scal}_{g_{\mathbb{R} H^{n}}}$. Then the linear functional $\mu_{g}$ on $\mathcal{N}_{\mathbb{R} H^{n}}$ introduced above is well-defined up to an automorphism of $\mathbb{R} H^{n}$, it is non-negative on $\mathcal{N}_{\mathbb{R} H^{n}}^{+}$and it vanishes iff $\left(M^{n}, g\right)$ is isometric to $\mathbb{R} H^{n}$.

The fact that the orbit of $\mu_{g}$ under the action of $O^{+}(n, 1)$ does not depend on the chart at infinity is not obvious but is proved in [CH]. Under our assumptions, $\mu_{g}$ may take infinite values (i.e. formula (5) may be $+\infty$ for some $\psi$ ) and this does not depend on the chart at infinity, so we actually obtain an element of $\left(\mathcal{N}_{\mathbb{R} H^{n}}\right)^{*} / O^{+}(n, 1) \cup\{\infty\}$.

Remark 3. The standard positive mass theorem, about asymptotically Euclidean metrics, can be thought of in a similar way. Let $M$ be a spin asymptotically Euclidean manifold with non-negative scalar curvature. Witten's trick consists in trying to build parallel spinors $\tilde{\psi}$ on $M$ that are asymptotic to the constant spinors $\psi$ of the Euclidean space $\mathbb{R}^{n}$. Now every constant one-form on $\mathbb{R}^{n}$ can be written as $X \mapsto i(X \cdot \psi, \psi)$. So the rigidity part of the Euclidean positive mass theorem can be explained as follows : starting from a constant one-form $\alpha$ on $\mathbb{R}^{n}$, we pick a constant spinor $\psi$ such that $\alpha(X)=(X \cdot \psi, \psi)$; an analytical argument (based on $\mu_{g}=0$ ) provides a parallel spinor $\tilde{\psi}$ on $M$ asymptotic to $\psi$, hence a parallel one-form $\tilde{\alpha}$, given by $\tilde{\alpha}(X)=(X \cdot \tilde{\psi}, \tilde{\psi})$, that is asymptotic to $\alpha$; this yields a parallel trivialization of the cotangent bundle of $M$, so $M$ is flat and is therefore $\mathbb{R}^{n}$, owing to its asymptotic shape. The mass is the obstruction to do this. It is a single number $\mu$, but if we wish to make it fit into our picture, we might as well interpret it as a linear functional on the space of parallel sections of the flat bundle $\mathcal{E}_{\mathbb{R}^{n}}:=T^{*} \mathbb{R}^{n} \oplus \mathbb{R}:(\alpha, u) \mapsto \mu u$. The bundle $\mathcal{E}_{M}:=T^{*} M \oplus \mathbb{R}$, endowed with the Levi-Civita connection on $T^{*} M$ and the flat connection on the $\mathbb{R}$-part, is of course flat if and only if $M$ is flat, so the formalism described above still works.

\section*{2. A complex hyperbolic connection.}
2.1. The connection. Let $\left(M^{m}, g, J\right)$ be a Kähler manifold of complex dimension $m$. We wish to introduce a "complex hyperbolic connection" characterizing the complex
hyperbolic geometry, in complete analogy with the real hyperbolic connection $\nabla^{R H}$ described in section 1. This is given by the following definition. The Kähler form is denoted by $\Omega:=g(., J$.$) . We will often identify vectors and covectors thanks to the$ metric $g$. With our convention, if $\left(e_{1}, J e_{1}, \ldots, e_{m}, J e_{m}\right)$ is an orthonormal basis, then $\Omega=\sum_{k=1}^{m} J e_{k} \wedge e_{k}$.
Definition 2.1 — Let $\mathcal{E}:=\Lambda_{J}^{2} M \oplus T^{*} M \oplus \mathbb{R}$ be the vector bundle obtained as the direct sum of the bundle $\Lambda_{J}^{2} M$ of $J$-invariant 2 -forms, of the cotangent bundle and of the trivial (real) line bundle. We endow $\mathcal{E}$ with the connection $\nabla^{C H}$ defined by
$$\nabla_{X}^{C H}\left(\begin{array}{c}
\xi \\
\alpha \\
u
\end{array}\right):=\left(\begin{array}{c}
\nabla_{X}^{g} \xi+\frac{1}{2}(X \wedge \alpha+J X \wedge J \alpha) \\
\nabla_{X}^{g} \alpha+2 \iota_{X}(\xi+u \Omega) \\
d_{X} u+J \alpha(X)
\end{array}\right) .$$
The connection $\nabla^{C H}$ preserves a pseudo-Riemannian structure $h$ on $\mathcal{E}$, with signature $\left(m^{2}+1,2 m\right)$ and given by $h(\xi, \alpha, u)=|\xi|_{g}^{2}+u^{2}-\frac{|\alpha|_{g}^{2}}{2}$.

This connection $\nabla^{C H}$ is very related to the study of Hamiltonian two-forms in [ACG], where a similar but more sophisticated connection is introduced. Let us explain why this connection is natural. In analogy with section 1, we expect its curvature to measure the deviation from the complex hyperbolic geometry (in the spirit of Cartan's connections). In order to write down an explicit formula for the curvature, we introduce an algebraic operation : if $X$ and $Y$ are two vectors and $\gamma$ is an exterior form, we set:
$$C_{X, Y}(\gamma):=\left(X \wedge \iota_{Y} \gamma-Y \wedge \iota_{X} \gamma\right)+\left(J X \wedge \iota_{J Y} \gamma-J Y \wedge \iota_{J X} \gamma\right) .$$
Proposition 2.2 - The curvature of $\nabla^{C H}$ is given by
$$\operatorname{Rm}_{X, Y}^{\nabla^{C H}}=\left(\begin{array}{ccc}
\operatorname{Rm}_{X, Y}^{\nabla}-C_{X, Y} & 0 & 0 \\
0 & \operatorname{Rm}_{X, Y}^{\nabla}-\left[2 \Omega(X, Y) J+C_{X, Y}\right] & 0 \\
0 & 0 & 0
\end{array}\right) .$$
It follows that $\mathrm{Rm}^{\nabla^{C H}}$ vanishes if and only if the holomorphic sectional curvature is -4. In other words, $\left(\mathcal{E} M, \nabla^{C H}\right)$ is flat if and only if the universal cover of $\left(M^{m}, g, J\right)$ is the complex hyperbolic space $\mathbb{C} H^{m}$ of holomorphic sectional curvature -4.

The proof of this formula is a straightforward computation, which we omit. The link with the curvature of the complex hyperbolic space is explained in paragraph IX. 7 of [KN] (where the sign convention is the opposite of ours).
Remark 4. By changing $\nabla_{X}^{g} \alpha+2 \iota_{X}(\xi+u \Omega)$ into $\nabla_{X}^{g} \alpha-2 c \iota_{X}(\xi+u \Omega)$ in the formula for the connection, it is possible to obtain a family of connections characterizing every constant holomorphic curvature $4 c$ (in particular : complex projective spaces).

The parallel sections $(\xi, \alpha, u)$ for $\nabla^{C H}$ obey $\alpha=J d u$ and $\xi=-\frac{1}{2} \nabla^{g} \alpha-u \Omega$ so that they are determined by their third component $u$, which satisfies the third order equation
$$\forall X \in T M, \quad \nabla_{X}^{g} \operatorname{Hess}_{g} u=2 d u(X)+X \odot d u+J X \odot J d u,$$
where $a \odot b$ means $a \otimes b+b \otimes a$. We will denote by $\mathcal{N}$ the space of parallel sections of $\left(\mathcal{E}, \nabla^{C H}\right)$. We will also need the subspace
$$\mathcal{N}_{0}:=\{(\xi, \alpha, u) \in \mathcal{N} / g(\xi, \Omega)=u\}$$
whose relevance will be clear from paragraph 2.2.
Remark 5. The complex projective analogue ( $c=+1$ in remark 4) of this third order equation appears in Obata's work [Oba] : on a simply-connected manifold, it possesses a solution if and only if the manifold is the complex projective space of holomorphic sectional curvature 4.
2.2. The model case. We wish to describe the case where $M=\mathbb{C} H^{m}$. We start with the complex vector space $\mathbb{C}^{m+1}, m \geq 2$, endowed with the Hermitian form $<,>$ defined by
$$<z, z>=\sum_{k=1}^{m}\left|z_{k}\right|^{2}-\left|z_{m+1}\right|^{2} .$$
We denote this space by $\mathbb{C}^{m, 1}$ or $\mathbb{R}^{2 m, 2}$ (whose metric structure is preserved by the standard complex structure $J$ ). The level set $<z, z>=-1$, endowed with the restriction of $<,>$ is by definition the Anti-de-Sitter space, $A d S^{2 m, 1}$, a Lorentz manifold with constant sectional curvature -1, invariant under the natural (scalar) action of $\mathbb{S}^{1}$ on $\mathbb{C}^{m+1}$. The complex hyperbolic space $\mathbb{C} H^{m}$ is the quotient $A d S^{2 m, 1} / \mathbb{S}^{1}$, endowed with the induced metric :
![](https://cdn.mathpix.com/cropped/6e815df3-aaa1-4c0c-b1ab-1667f4b66024-08.jpg?height=135&width=323&top_left_y=1213&top_left_x=870)
Let $\nu$ be the position vector field in $\mathbb{C}^{m+1}$, identified also with the dual one-form $\langle\nu,$.$\rangle . By definition of A d S^{2 m, 1},\langle\nu, \nu\rangle=-1$ along $A d S^{2 m, 1}$ and the tangent bundle $T A d S^{2 m, 1}$ is exactly the orthogonal subspace to $\nu$ for $\langle$,$\rangle . Besides, the vector$ field $J \nu$ is tangent to the action of $\mathbb{S}^{1}$ and obeys $\langle J \nu, J \nu\rangle=-1$. If $\pi$ is the projection of $A d S^{2 m, 1}$ onto $\mathbb{C} H^{m}$, it follows that at each point of $A d S^{2 m, 1}, d \pi$ is an isometry between $\{\nu, J \nu\}^{\perp}$ and the tangent space of $\mathbb{C} H^{m}$.

To understand $\mathcal{E}=\mathcal{E}\left(\mathbb{C} H^{m}\right)$, we pick a point $z$ in $A d S^{2 m, 1}$ and look at the map $\theta_{z}: \mathcal{E}_{\pi(z)} \longrightarrow\left(\Lambda_{J}^{2} \mathbb{R}^{2 m, 2}\right)_{z}$ given by
$$\theta_{z}(\xi, \alpha, u)=\left(d \pi_{z}\right)^{*} \xi+u(\pi(z)) J \nu \wedge \nu+\frac{\nu \wedge\left(d \pi_{z}\right)^{*} \alpha+J \nu \wedge J\left(d \pi_{z}\right)^{*} \alpha}{2} .$$
It is a $\mathbb{R}$-linear isomorphism and we have
$$<\theta_{z}(\xi, \alpha, u), \theta_{z}(\xi, \alpha, u)>=|\xi|_{\pi(z)}^{2}+u(\pi(z))^{2}-\frac{1}{2}|\alpha|_{\pi(z)}^{2}=h_{\pi(z)}(\xi, \alpha, \nu) .$$
Setting $\Psi_{z}:=\theta_{z}^{-1}$, we obtain a bundle map $\Psi$ that is $\mathbb{S}^{1}$-invariant and satisfies the commutative diagram
![](https://cdn.mathpix.com/cropped/6e815df3-aaa1-4c0c-b1ab-1667f4b66024-08.jpg?height=202&width=378&top_left_y=2113&top_left_x=842)
In this way, in the case of $\mathbb{C} H^{m}$, the metric $h$ preserved by $\nabla^{C H}$ simply comes from $<,>$, via $\Psi$. At the level of sections, $\Psi$ yields an isomorphism
$$\Gamma(\mathcal{E}) \cong \Gamma\left(\left.\Lambda_{J}^{2} \mathbb{R}^{2 m, 2}\right|_{A d S^{2 m, 1}}\right)^{\mathbb{S}^{1}}$$
where the right-hand side denotes the $\mathbb{S}^{1}$-invariant sections of the bundle obtained by restricting $\Lambda_{J}^{2} \mathbb{R}^{2 m, 2}$ to $A d S^{2 m, 1}$. This isomorphism identifies $\sigma=(\xi, \alpha, u) \in \Gamma(\mathcal{E})$ with
the $\mathbb{S}^{1}$-invariant 2-form
$$\Psi^{*} \sigma=\pi^{*} \xi+\pi^{*} u J \nu \wedge \nu+\frac{\nu \wedge \pi^{*} \alpha+J \nu \wedge J \pi^{*} \alpha}{2} .$$
The bundle $\left.\Lambda_{J}^{2} \mathbb{R}^{2 m, 2}\right|_{A d S^{2 m, 1}}$ carries a natural connection $D$, inherited from the standard flat connection on $\mathbb{R}^{2 m, 2}$. The real and imaginary parts of the differential forms $d z_{k} \wedge d \bar{z}_{l}$, restricted to $A d S^{2 m, 1}$, trivialize the bundle $\left.\Lambda_{J}^{2} \mathbb{R}^{2 m, 2}\right|_{A d S^{2 m, 1}}$, are $\mathbb{S}^{1}$-invariant and $D$ -parallel. $D$ therefore induces, via $\Psi$, a flat connection on $\mathcal{E}$ and the reader might expect the following result.
Proposition 2.3 — The morphism $\Psi$ identifies $D$ and $\nabla^{C H}$ : for every horizontal vector field $H$ on $A d S^{2 m, 1}$ and for every section $\sigma$ of $\mathcal{E}, \nabla_{\pi_{*} H}^{C H} \sigma=\Psi_{*} D_{H} \Psi^{*} \sigma$.

In this statement, "horizontal" means "orthogonal to both $\nu$ and $J \nu$ ". The proof of this is a direct computation, involving only two obvious facts : $D \nu$ is the identity at each point and the Levi-Civita connection of the hyperbolic space is induced by $D$.

Note it is very important to work here with $J$-invariant 2 -forms. For instance, there is no flat $\mathbb{S}^{1}$-invariant trivialization of the bundle $\left.\Lambda^{1} \mathbb{R}^{2 m, 2}\right|_{A d S^{2 m, 1}}$.

We therefore obtain an isomorphism $\mathcal{N}_{\mathbb{C} H^{m}} \cong \Lambda_{J}^{2} \mathbb{R}^{2 m, 2}$. Let $\Lambda_{J, 0}^{2} \mathbb{R}^{2 m, 2}$ be the subspace of primitive $J$-invariant 2-forms on $\mathbb{R}^{2 m, 2}$. Since the Kähler form $\omega$ of $\mathbb{C}^{m, 1}$, restricted to $A d S^{2 m, 1}$, is given by $\omega=-J \nu \wedge \nu+\pi^{*} \Omega$, where $\Omega$ is the Kähler form of $\mathbb{C} H^{m}$, we also have (cf. (6)):
$$\mathcal{N}_{\mathbb{C} H^{m}, 0} \cong \Lambda_{J, 0}^{2} \mathbb{R}^{2 m, 2} .$$
2.3. Kählerian Killing spinors. Let $\left(M^{m}, g, J\right)$ be a spin Kähler manifold. As in the hyperbolic space, a class of special spinors somehow characterizes the complex hyperbolic space. It turns out that there is a dimension issue, so we first assume the complex dimension $m$ is odd : $m=2 l-1$. The even dimensional case will be discussed in section 4.

The spinor bundle $\Sigma$ decomposes into the orthogonal sum of the eigenspaces of the natural action of the Kähler form $\Omega=g(., J):. \Sigma=\bigoplus_{k=0}^{m} \Sigma_{k}$, where $\Sigma_{k}$ corresponds to the eigenvalue $i(m-2 k)$ (Kir for instance). We will write $\pi_{k}^{\Omega}(\psi)$ or simply $\psi_{k}$ for the $k$ th component of the spinor $\psi$ in this decomposition. From another point of view, spinors may be seen as twisted forms : $\Sigma=\bigoplus_{k=0}^{m} \Lambda^{0, k} \otimes \sqrt{\Lambda^{m, 0}}$ and then $\Sigma_{k}=\Lambda^{0, k} \otimes \sqrt{\Lambda^{m, 0}}$. Through this identification, Clifford product "." is merely $\sqrt{2}$ times the difference between exterior product and interior product ((1, 0)-vectors are identified with (0, 1)-covectors by the Hermitian inner product). As a consequence,
$$T^{1,0} \cdot \Sigma_{k} \subset \Sigma_{k+1} \quad \text { and } \quad T^{0,1} \cdot \Sigma_{k} \subset \Sigma_{k-1} .$$

The following formula defines a connection $\hat{\nabla}$ on the vector bundle $\Sigma$ :
$$\begin{aligned}
\hat{\nabla}_{X} \psi & =\nabla_{X} \psi+i c\left(X^{1,0}\right) \psi_{l-1}+i c\left(X^{0,1}\right) \psi_{l} \\
& =\nabla_{X} \psi+\frac{i}{2} c(X)\left(\psi_{l-1}+\psi_{l}\right)+\frac{1}{2} c(J X)\left(\psi_{l-1}-\psi_{l}\right) .
\end{aligned}$$
The sections of $\Sigma_{l-1} \oplus \Sigma_{l}$ that are parallel for the connection $\hat{\nabla}$ are called imaginary Kählerian Killing spinors. The dimension of the space $\mathcal{K}$ of Kählerian Killing spinors
is therefore at most $C_{2 l}^{l}$. This bound is attained on $\mathbb{C} H^{m}$, as we will see in details after corollary 2.7. First, we make a number of general useful remarks.

For future reference, let us introduce the (modified) Dirac operator $\hat{\not D}$ which is naturally associated with the connection $\hat{\nabla}:$ if $\left(\epsilon_{j}\right)_{j}$ is any $g$-orthonormal frame, it is given by
$$\hat{\not D} \psi:=\sum_{j=1}^{2 m} c\left(\epsilon_{j}\right) \hat{\nabla}_{\epsilon_{j}} \psi .$$
In [Her], another modified Dirac operator $\mathcal{D}$ is used, for analytical reasons :
$$\mathcal{D} \psi:=\hat{\not D} \psi-i(m+1)\left(\psi-\psi_{l-1}-\psi_{l}\right)=\not D \psi-i(m+1) \psi,$$
where $\not D$ is the standard Dirac operator. It should be noticed that Kählerian Killing spinors are canceled by both $\hat{\not D}$ and $\mathcal{D}$.

Given a spinor $\phi=\phi_{l-1}+\phi_{l} \in \Sigma_{l-1} \oplus \Sigma_{l}$, we will use the notation $\tilde{\phi}:=\phi_{l-1}-\phi_{l}$; $\tilde{\phi}$ is $(-1)^{l+1}$ times the conjugate $\phi_{+}-\phi_{-}$with respect to the usual decomposition into half-spinors. The Kählerian Killing equation can then be written
$$\nabla_{X} \phi=-\frac{i}{2} X \cdot \phi-\frac{1}{2}(J X) \cdot \tilde{\phi} \quad \text { or } \quad \nabla_{X} \tilde{\phi}=\frac{i}{2} X \cdot \tilde{\phi}+\frac{1}{2}(J X) \cdot \phi .$$
The following lemma is easy but very useful.
Lemma 2.4 - If $\phi$ is a Kählerian Killing spinor then
$$\begin{aligned}
& (X \cdot \phi, \phi)=-(X \cdot \tilde{\phi}, \tilde{\phi})=2 i \operatorname{Im}\left(X^{1,0} \cdot \phi_{l-1}, \phi_{l}\right) \\
& (X \cdot \tilde{\phi}, \phi)=-(X \cdot \phi, \tilde{\phi})=2 \operatorname{Re}\left(X^{1,0} \cdot \phi_{l-1}, \phi_{l}\right) .
\end{aligned}$$
In particular, $((J X) \cdot \phi, \phi)=i(X \cdot \tilde{\phi}, \phi)$.
Proof. The first statement follows from the computation
$$\begin{aligned}
(X \cdot \phi, \phi) & =\left(X \cdot\left(\phi_{l}+\phi_{l-1}\right), \phi_{l}+\phi_{l-1}\right)=\left(X \cdot \phi_{l}, \phi_{l-1}\right)+\left(X \cdot \phi_{l-1}, \phi_{l}\right) \\
& =2 i \operatorname{Im}\left(X \cdot \phi_{l-1}, \phi_{l}\right)=2 i \operatorname{Im}\left(X^{1,0} \cdot \phi_{l-1}, \phi_{l}\right)
\end{aligned}$$
and the other ones are similar. \(\square\)

In complete analogy with the real hyperbolic case, the squared norm $|\phi|^{2}$ of a Kählerian Killing spinor $\phi$ will induce a $\nabla^{C H}$-parallel section of $\mathcal{E}$. To see this, we first compute two derivatives of this function.

Lemma 2.5 - Any Kählerian Killing spinor $\phi$ obeys
$$\begin{aligned}
d|\phi|^{2}(X) & =-2 i(X \cdot \phi, \phi) \\
\nabla_{X} d|\phi|^{2}(Y) & =2(X, Y)|\phi|^{2}-2 \operatorname{Im}(Y \cdot(J X) \cdot \tilde{\phi}, \phi) .
\end{aligned}$$
Proof. The definition of Kählerian Killing spinors readily yields
$$\mathrm{d}|\phi|^{2}(X)=-\frac{i}{2}(X \cdot \phi, \phi)-\frac{1}{2}(J X \cdot \tilde{\phi}, \phi)+\frac{i}{2}(\phi, X \cdot \phi)-\frac{1}{2}(\phi, J X \cdot \tilde{\phi}),$$
which leads to $d|\phi|^{2}(X)=-2 i(X \cdot \phi, \phi)$, thanks to lemma 2.4. Differentiating once more, we find
$$\begin{aligned}
\nabla_{X} d|\phi|^{2}(Y) & =-2 i\left(Y \cdot \nabla_{X} \phi, \phi\right)-2 i\left(Y \cdot \phi, \nabla_{X} \phi\right) \\
& =-(Y \cdot X \cdot \phi, \phi)+i(Y \cdot J X \cdot \tilde{\phi}, \phi)+(Y \cdot \phi, X \cdot \phi)+i(Y \cdot \phi, J X \cdot \tilde{\phi})
\end{aligned}$$
and the result follows from elementary properties of the Clifford product. \(\square\)

At this point, it is useful to introduce the following notations : for every Kählerian Killing spinor $\phi$, we define :
$$u_{\phi}:=|\phi|^{2}, \quad \alpha_{\phi}:=J d u_{\phi}, \quad \xi_{\phi}(X, Y):=\operatorname{Im}(X \cdot Y \cdot \tilde{\phi}, \phi) .$$
Lemma 2.6 — $\xi_{\phi}$ is a $J$-invariant two-form satisfying :
$$\begin{aligned}
\nabla_{Z} \alpha_{\phi} & =-2 \iota_{Z}\left(\xi_{\phi}+u_{\phi} \Omega\right), \\
\left(\xi_{\phi}, \Omega\right) & =u_{\phi}, \\
\nabla_{Z} \xi_{\phi} & =-\frac{1}{2}\left(Z \wedge \alpha_{\phi}+J Z \wedge J \alpha_{\phi}\right) .
\end{aligned}$$
Proof. First, it is easy to check that $\xi_{\phi}$ is skewsymmetric, as a consequence of the definition of $\tilde{\phi}$. The $J$-invariance of $\xi_{\phi}$ stems from the following reformulation of its definition :
$$\xi_{\phi}(X, Y):=\operatorname{Im}\left(X^{1,0} \cdot Y^{0,1} \cdot \tilde{\phi}, \phi\right)+\operatorname{Im}\left(X^{0,1} \cdot Y^{1,0} \cdot \tilde{\phi}, \phi\right) .$$
Then formula (9) readily yields
$$\nabla_{X} \alpha_{\phi}(Y)=-2(X, J Y) u_{\phi}+2 \xi_{\phi}(J Y, J X)=-2 u_{\phi} \Omega(X, Y)-2 \xi_{\phi}(X, Y),$$
which justifies the first formula.
Let $\left(e_{1}, J e_{1}, \ldots, e_{m}, J e_{m}\right)$ be an orthonormal basis. Then we have
$$\left(\xi_{\phi}, \Omega\right)=\sum_{k=1}^{m} \xi_{\phi}\left(J e_{k}, e_{k}\right)=\sum_{k=1}^{m} \operatorname{Im}\left(J e_{k} \cdot e_{k} \cdot \tilde{\phi}, \phi\right)=\operatorname{Im}(\Omega \cdot \tilde{\phi}, \phi) .$$
Now we use the spectral decomposition of the action of the Kähler form :
$$(\Omega \cdot \tilde{\phi}, \phi)=\left(\Omega \cdot \phi_{l-1}-\Omega \cdot \phi_{l}, \phi\right)=\left(i \phi_{l-1}+i \phi_{l}, \phi\right)=i|\phi|^{2} .$$
This ensures $\left(\xi_{\phi}, \Omega\right)=|\phi|^{2}=u_{\phi}$.
Finally, to obtain the third equation, we introduce $\theta(X, Y):=2(X \cdot Y \cdot \tilde{\phi}, \phi)$ and differentiate :
$$\begin{aligned}
& \nabla_{Z} \theta(X, Y) \\
= & 2\left(X \cdot Y \cdot \nabla_{Z} \tilde{\phi}, \phi\right)+2\left(X \cdot Y \cdot \tilde{\phi}, \nabla_{Z} \phi\right) \\
= & i(X \cdot Y \cdot Z \cdot \tilde{\phi}, \phi)+(X \cdot Y \cdot(J Z) \cdot \phi, \phi)+i(X \cdot Y \cdot \tilde{\phi}, Z \cdot \phi)-(X \cdot Y \cdot \tilde{\phi},(J Z) \cdot \tilde{\phi}) \\
= & i([X \cdot Y \cdot Z-Z \cdot X \cdot Y] \cdot \tilde{\phi}, \phi)+([X \cdot Y \cdot(J Z)-(J Z) \cdot X \cdot Y] \cdot \phi, \phi) .
\end{aligned}$$
The identity $A B C-C A B=2(A, C) B-2(B, C) A$ in Clifford algebra leads to
$$\begin{aligned}
& \nabla_{Z} \theta(X, Y) \\
= & 2 i(X, Z)(Y \cdot \tilde{\phi}, \phi)-2 i(Y, Z)(X \cdot \tilde{\phi}, \phi)+2(X, J Z)(Y \cdot \phi, \phi)-2(Y, J Z)(X \cdot \phi, \phi) .
\end{aligned}$$

Lemmata 2.4 and 2.5 then yield :
$$\begin{aligned}
& \nabla_{Z} \theta(X, Y) \\
= & i(X, Z) d u_{\phi}(J Y)-i(Y, Z) d u_{\phi}(J X)+i(X, J Z) d u_{\phi}(Y)-i(Y, J Z) d u_{\phi}(X) \\
= & -i(X, Z) \alpha_{\phi}(Y)+i(Y, Z) \alpha_{\phi}(X)-i(X, J Z) J \alpha_{\phi}(Y)+i(Y, J Z) J \alpha_{\phi}(X)
\end{aligned}$$
and the result follows. \(\square\)

The computations above result in the following proposition (recall(6)).
Corollary 2.7 — If $\phi$ is a Kählerian Killing spinor, then $Q(\phi):=\left(\xi_{\phi}, \alpha_{\phi}, u_{\phi}\right)$ is an element of $\mathcal{N}_{0}$. So we have a map $Q: \mathcal{K} \longrightarrow \mathcal{N}_{0}$.

When $m=2 l-1$ for some integer $l \geq 2$, the complex hyperbolic space $\mathbb{C} H^{m}$ is known to carry a space of Kählerian Killing spinors of maximal dimension, $C_{2 l}^{l}$ [Kir]. Where do they come from ? Briefly, constant spinors on $\mathbb{C}^{m, 1}$ admit a restriction as spinors on $\operatorname{Ad} S^{2 m, 1}$ (cf. Lemma 3 in Bau]). These are the so-called imaginary Killing spinors ; they trivialize the spinor bundle of $A d S^{2 m, 1}$. Among them, thanks to the parity of $m$, some are $\mathbb{S}^{1}$-invariant (it can be seen on the graduation coming from the Kähler structure of $\mathbb{C}^{m, 1}$ ) and admit a projection into spinors along $\mathbb{C} H^{m}$ (Mor]). These "projected" spinors are exactly the Kählerian Killing spinors.

To be more explicit, we can adapt the computations of [Kir]. The manifold $\mathbb{C} H^{m}$ carries global coordinates $w_{1}, \ldots, w_{m}$, such that $\pi^{*} w_{k}=\frac{z_{k}}{z_{m+1}}$ (along $A d S^{2 m, 1}$, where $z_{m+1}$ does not vanish). These coordinates induce a trivialization of the canonical bundle, by $\sqrt{d w}:=\sqrt{d w_{1} \wedge \cdots \wedge d w_{m}}$. We will use multi-index $a=\left(a_{1}, \ldots, a_{k}\right)$ with $1 \leq a_{1}<\cdots<a_{k} \leq m$ and set $d z_{a}:=d z_{a_{1}} \wedge \cdots \wedge d z_{a_{k}}$. The computations of [Kir] say that, if $a$ is a multi-index of length $l-1$, the spinor $\varphi^{a}=\varphi_{l-1}^{a}+\varphi_{l}^{a}$ defined by
$$\varphi_{l-1}^{a}=c(l) \frac{d \bar{w}_{a}}{\left(1-|w|^{2}\right)^{l}} \otimes \sqrt{d w} \quad \text { and } \quad \varphi_{l}^{a}=\frac{c(l)}{2 i l} \bar{\partial}\left(\frac{d \bar{w}_{a}}{\left(1-|w|^{2}\right)^{l}}\right) \otimes \sqrt{d w}$$
is a Kählerian Killing spinor. In this expression, $c(l)$ is a normalization constant, which we choose to be $c(l)=\sqrt{2}^{\frac{5}{2}-3 l}$. Another family of Kählerian Killing spinors is described by spinors $\breve{\varphi}^{b}=\breve{\varphi}_{l-1}^{b}+\breve{\varphi}_{l}^{b}$ where $b$ is a multi-index of length $l$ and
$$\breve{\varphi}_{l-1}^{b}=c(l) \frac{\iota_{\bar{R}} d \bar{w}_{b}}{\left(1-|w|^{2}\right)^{l}} \otimes \sqrt{d w} \quad \text { and } \quad \breve{\varphi}_{l}^{b}=\frac{c(l)}{2 i l} \bar{\partial}\left(\frac{\iota_{\bar{R}} d \bar{w}_{b}}{\left(1-|w|^{2}\right)^{l}}\right) \otimes \sqrt{d w}$$
where $R=\sum_{k} w_{k} \partial_{w_{k}}$. These families together form a basis for the Kählerian Killing spinors of $\mathbb{C} H^{m}$. What we are interested in here is their squared norms. Let us introduce the notation $\breve{a}$ for the multi-index that is complementary to $a$ (namely, $a$ and $\breve{a}$ have no common index and the sum of their lengths is $m$ ), and also the notation $\left|w_{a}\right|^{2}:=\left|w_{a_{1}}\right|^{2}+\cdots+\left|w_{a_{k}}\right|^{2}$. An adaptation of the computations at the end of Kir yields
$$\left|\varphi_{l-1}^{a}\right|^{2}=\left|\breve{\varphi}_{l}^{\breve{a}}\right|^{2}=\frac{1-\left|w_{a}\right|^{2}}{1-|w|^{2}} \quad \text { and } \quad\left|\varphi_{l}^{a}\right|^{2}=\left|\breve{\varphi}_{l-1}^{\breve{a}}\right|^{2}=\frac{\left|w_{\breve{a}}\right|^{2}}{1-|w|^{2}},$$
hence
$$\left|\varphi^{a}\right|^{2}=\left|\breve{\varphi}^{\breve{a}}\right|^{2}=\frac{1-\left|w_{a}\right|^{2}+\left|w_{\breve{a}}\right|^{2}}{1-|w|^{2}} .$$
It follows that $\pi^{*} u_{\varphi^{a}}=-\left|z_{a}\right|^{2}+\left|z_{\breve{a}}\right|^{2}+\left|z_{m+1}\right|^{2}$ (we forget the $\breve{\varphi}$ 's since they do not yield new squared norms). Now $\alpha_{\varphi^{a}}$ and $\xi_{\varphi^{a}}$ are determined by $u_{\varphi^{a}}$ (since these are
the components of an element of $\mathcal{N}$ ). Denoting the real part of $z_{k}$ by $x_{k}$, one can check that the corresponding element of $\mathcal{N}_{0}\left(\mathbb{C} H^{m}\right) \cong \Lambda_{J, 0}^{2} \mathbb{R}^{2 m, 2}$ is
$$\beta_{\varphi^{a}}=-\sum_{j=1}^{l-1} J d x_{a_{j}} \wedge d x_{a_{j}}+\sum_{j=1}^{l} J d x_{\breve{a}_{j}} \wedge d x_{\breve{a}_{j}}+J d x_{m+1} \wedge d x_{m+1}$$
(To see this, it is sufficient to compute the scalar product of the right-hand side with $J \nu \wedge \nu$ and observe that it coincides with $\pi^{*} u_{\varphi^{a}}$.) In particular, $\left\langle\beta_{\varphi^{a}}, \beta_{\varphi^{a}}\right\rangle=m+1$. All these two-forms belong to the same orbit of the isometric and holomorphic action of $P U(m, 1)$. We will denote this orbit by $\mathcal{N}_{0, \mathbb{C} H^{m}}^{+}$. Note that, since $\Lambda_{J, 0}^{2} \mathbb{R}^{2 m, 2}$ is an irreducible representation of $P U(m, 1)$, the linear span of $\mathcal{N}_{0, \mathbb{C} H^{m}}^{+}$is the whole $\Lambda_{J, 0}^{2} \mathbb{R}^{2 m, 2}$.

\section*{3. Toward a mass.}
3.1. The "mass integral" at infinity. Let us give a precise definition for the class of manifolds we are interested in.

Definition 3.1 — A complete Kähler manifold $\left(M^{m}, g, J\right)$ is called asymptotically complex hyperbolic if there is a compact subset $K$ of $M$ and a ball $B$ in $\mathbb{C} H^{m}$ such that:
\begin{itemize}
\item[(i)] $(M \backslash K, J)$ is biholomorphic to $\mathbb{C} H^{m} \backslash B$ and,
\item[(ii)] through this identification, $e^{a r}\left(g-g_{\mathbb{C} H^{m}}\right)$ is bounded in $C^{1, \alpha}$, with respect to the complex hyperbolic metric $g_{\mathbb{C} H^{m}}$. Here, $r$ denotes the distance to some point in $\mathbb{C} H^{m}$ and we assume $a>m+\frac{1}{2}$.
\end{itemize}

In Her, it is only assumed that the complex structure $J$ of $M$ is asymptotic to the complex structure $J_{0}$ of $\mathbb{C} H^{m}$ (instead of $J=J_{0}$, as in our definition). It turns out that, if $J$ is asymptotic to $J_{0}$, then they are related by a biholomorphism, defined outside a compact set and asymptotic to the identity. To justify this, let us see $J$ and $J_{0}$ as two complex structures on a neighborhood $U$ of $\mathbb{S}^{2 m-1}$ in the unit ball of $\mathbb{C}^{m}$. Under our assumptions, they induce the same CR structure on the unit sphere, the standard CR structure of $\mathbb{S}^{2 m-1}$. The restriction of any $J_{0}$-holomorphic coordinate $z_{k}$ to the sphere is a $C R$ function. Since the standard sphere is strictly-pseudo-convex, Lewy's extension theorem makes it possible to extend this function into a $J$-holomorphic function $w_{k}$ on $U$ (shrinking $U$ if necessary). This yields a holomorphic map $w=\left(w_{1}, \ldots, w_{m}\right)$ from $\Omega$ to $\mathbb{C}^{m}$. Since $z=\left(z_{1}, \ldots, z_{m}\right)$ is a diffeomorphism onto its range and coincide with $w$ on the sphere, we may shrink $U$ to ensure $w$ is also a diffeomorphism onto its range, hence a biholomorphism between two neighborhoods of $\mathbb{S}^{2 m-1}$ in the unit ball of $\mathbb{C}^{m}$, one endowed with $J$ and the other one with the standard complex structure. The promised biholomorphism is $z^{-1} \circ w$.

In this section, we assume $(M, g, J)$ is an asymptotically complex hyperbolic manifold of odd complex dimension $m=2 l-1$ and with scalar curvature bounded from below by $-4 m(m+1)$ (the scalar curvature of $\mathbb{C} H^{m}$ ). In this setting, the spinor bundle $\left.\Sigma\right|_{M \backslash K}$ can be identified with the spinor bundle of $\mathbb{C} H^{m} \backslash B$. We may therefore extend any Kählerian Killing spinor $\phi$ on $\mathbb{C} H^{m} \backslash B$ into a spinor $\phi$ on $M$. Our aim is to understand to what extent we can make it into a Kählerian Killing spinor. In the spirit of [Wit], we first check that we can choose an extension in the kernel of a Dirac operator.

Lemma 3.2 - There is a smooth spinor $\psi:=\phi+\phi_{\text {err }}$ such that $\mathcal{D} \psi=0$ and $\phi_{\text {err }}$ decays as $e^{-b r}$ in $C^{1, \alpha}$ with $b>m+\frac{1}{2}$.

Proof. We first observe that
$$\mathcal{D} \mathcal{D}^{*}=\not D^{2}+(m+1)^{2}=\nabla^{*} \nabla+\frac{1}{4} \operatorname{Scal}+(m+1)^{2} \geq \nabla^{*} \nabla+m+1 \text {. }$$
A slight adaptation of Proposition I.3.5 in [Biq] then shows that the operator
$$\mathcal{D} \mathcal{D}^{*}: e^{b r} C^{2, \alpha} \longrightarrow e^{b r} C^{0, \alpha}$$
is an isomorphism for every $b$ such that $m-\sqrt{m^{2}+m+1}<b<m+\sqrt{m^{2}+m+1}$. Since $\mathcal{D} \phi=\left(\mathcal{D}_{g}-\mathcal{D}_{\mathbb{C} H^{m}}\right) \phi=\mathcal{O}\left(e^{-(a-1) r}\right)$, with $a>m+\frac{1}{2}$, we can pick a $b>m+\frac{1}{2}$ such that the equation $\mathcal{D} \mathcal{D}^{*} \sigma=-\mathcal{D} \phi_{0}$ admits a solution $\sigma$ in $e^{b r} C^{2, \alpha}$. Then $\phi_{\text {err }}:=\mathcal{D}^{*} \sigma$ is convenient. \(\square\)

We then invoke a Weitzenböck formula, proved in paragraph 3 of [Her] (modulo two misprints, indeed: in the formula stated, an $i$ should be added at the second and third lines and the coefficient $m-2 q$ and the fourth one should be replaced by $2(m-q))$ :
$$\begin{aligned}
\int_{S_{R}} * \zeta_{\psi, \psi}= & \int_{B_{R}}|\hat{\nabla} \psi|^{2}+\frac{1}{4} \int_{B_{R}}(\operatorname{Scal}+4 m(m+1))|\psi|^{2} \\
& +(m+1) \int_{B_{R}}\left(|\psi|^{2}-\left|\pi_{l-1}^{\Omega} \psi\right|^{2}-\left|\pi_{l}^{\Omega} \psi\right|^{2}\right),
\end{aligned}$$
where $S_{R}$ denotes the sphere $\{r=R\}$, bounding the domain $B_{R}$, and $\zeta_{\sigma, \tau}$ is the 1-form defined by
$$\zeta_{\sigma, \tau}(X)=\left(\hat{\nabla}_{X} \sigma+c(X) \mathcal{D} \sigma, \tau\right) .$$
In view of this formula, the obstruction for $\psi$ to be a Kählerian Killing spinor is precisely the "mass integral at infinity" $\lim _{R \rightarrow \infty} \int_{S_{R}} * \zeta_{\psi, \psi}$, which is a well defined element of $[0,+\infty]$, because the integrand on the right-hand side is non-negative.
Lemma 3.3 - $\lim _{R \rightarrow \infty} \int_{S_{R}} * \zeta_{\psi, \psi}=\lim _{R \rightarrow \infty} \int_{S_{R}} * \zeta_{\phi, \phi}$.
Proof. Since $\operatorname{Re} \zeta_{\sigma, \tau}$ is symmetric up to a divergence term (as noticed in [Her], p.651), we only need to check that
$$\lim _{R \rightarrow \infty} \int_{S_{R}} *\left(\zeta_{\phi, \phi_{e r r}}+\zeta_{\phi_{e r r}, \phi_{e r r}}\right)=0$$
This follows from the following estimates : $\operatorname{vol} S_{R}=\mathcal{O}\left(e^{2 m r}\right), \hat{\nabla} \phi=\mathcal{O}\left(e^{(1-a) r}\right)$ (beware $\phi$ grows in $e^{r}$ ), $\phi_{\text {err }}=\mathcal{O}\left(e^{-b r}\right), \hat{\nabla} \phi_{\text {err }}=\mathcal{O}\left(e^{-b r}\right)$ (cf. lemma 3.2), with $a>m+\frac{1}{2}$ and $b>m+\frac{1}{2}$. \(\square\)

In order to compare the metrics $g$ et $g_{0}:=g_{\mathbb{C} H^{m}}$, we introduce the symmetric endomorphism $A$ such that $g_{0}=g\left(A ., A\right.$.). Since $A$ maps $g_{0}$-orthonormal frames to $g$-orthonormal frames, it identifies the spinor bundles defined with $g$ and $g_{0}$ (cf. [CH] for instance). The associated Clifford products $c_{g}$ and $c_{g_{0}}$ are related by the formula $c_{g}(A X) \sigma=c_{g_{0}}(X) \sigma$. Note we will also write $X$. for $c_{g_{0}}(X)$ (and not for $c_{g}(X)$ ). For the sake of efficiency, we will write $u \approx v$ when $u-v=o\left(e^{-2 m r}\right)$; the terms we neglect in this way will indeed not contribute to the integral at infinity. Before computing the "mass integral at infinity", we point out a few elementary facts.
Lemma $3.4-A^{-1} J A \approx J$.

Proof. The definition $g_{0}=g(A, A)$ and the compatibility of $J$ with $g_{0}$ yield the equality $g(A J, A J)=g(A, A)$. Since $A$ and $J$ are respectively $g$-symmetric and $g$-antisymmetric, we deduce : $J A^{2} J=-A^{2}$. If $A=1+H$, this implies $J H J \approx-H$. Since $J^{2}=-1$, we obtain $J H \approx H J$ and then $J A \approx A J$, hence the result. \(\square\)

Corollary 3.5 — We have $c_{g}(\Omega) \approx c_{g_{0}}\left(\Omega_{0}\right)$ and $\pi_{k}^{\Omega} \approx \pi_{k}^{\Omega_{0}}$.
Proof. Given a $g_{0}$-orthonormal basis $\left(e_{1}, J e_{1}, \ldots, e_{m}, J e_{m}\right)$, the Clifford action of the Kähler form $\Omega_{0}$ reads $c_{g_{0}}\left(\Omega_{0}\right)=\sum_{k} J e_{k} \cdot e_{k}$. while the Kähler form $\Omega$ of $g$ acts by
$$c_{g}(\Omega)=\sum_{k=1}^{m} c_{g}\left(J A e_{k}\right) c_{g}\left(A e_{k}\right)=\sum_{k=1}^{m}\left(A^{-1} J A e_{k}\right) \cdot e_{k} \cdot .$$
The first statement is therefore a straightforward consequence of lemma 3.4. The second one follows from general considerations. We observe the skew-Hermitian endomorphisms $P:=c_{g}(\Omega)$ and $P_{0}:=c_{g_{0}}\left(\Omega_{0}\right)$ act on each fiber of the spinor bundle with the same spectrum. If $\lambda$ is one of the eigenvalues, the corresponding spectral projectors $\Pi$ and $\Pi_{0}$ (for $P$ and $P_{0}$ ) obey the formulas
$$\Pi=\frac{1}{2 \pi} \int_{C}(z-P)^{-1} d z \quad \text { and } \quad \Pi_{0}=\frac{1}{2 \pi} \int_{C}\left(z-P_{0}\right)^{-1} d z$$
where $C$ is a circle in the complex plane, centered in $\lambda$ and with small radius $\delta$. We deduce
$$\Pi-\Pi_{0}=\frac{1}{2 \pi} \int_{C}(z-P)^{-1}\left(P-P_{0}\right)\left(z-P_{0}\right)^{-1} d z$$
and then
$$\left|\Pi-\Pi_{0}\right| \leq \delta \delta^{-1}\left|P-P_{0}\right| \delta^{-1}=\delta^{-1}\left|P-P_{0}\right| .$$
The result follows at once. \(\square\)

The rest of this section is devoted to the proof of the following statement.
Proposition 3.6 - The "mass integral at infinity" is
$$\lim _{R \rightarrow \infty} \int_{S_{R}} * \zeta_{\psi, \psi}=\lim _{R \rightarrow \infty} \int_{S_{R}} *\left(-\frac{1}{4}\left(d \operatorname{Tr}_{g_{0}} g+\operatorname{div}_{g_{0}} g\right)|\phi|^{2}+\frac{1}{8} \operatorname{Tr}_{g_{0}}\left(g-g_{0}\right) \mathrm{d}|\phi|^{2}\right) .$$
Proof. To begin with, in view of corollary 3.5, we may write
$$\begin{aligned}
\zeta_{\phi, \phi}(Y) & =\left(\hat{\nabla}_{Y}^{g} \phi+c_{g}(Y) \hat{D} \phi, \phi\right)-i(m+1)\left(c_{g}(Y)\left(1-\pi_{l-1}^{\Omega}-\pi_{l}^{\Omega}\right) \phi, \phi\right) \\
& \approx\left(\hat{\nabla}_{Y}^{g} \phi+c_{g}(Y) \hat{D} \phi, \phi\right) .
\end{aligned}$$
Given a $g_{0}$-orthonormal frame $\left(e_{1}, \ldots, e_{2 m}\right)$ and a $g_{0}$-unit vector $X$, since $\phi$ is a Kählerian Killing spinor with respect to $\left(g_{0}, J_{0}\right)$, we may therefore write outside $K$ (as in [CH, Min] for instance) :
$$\begin{aligned}
\zeta_{\phi, \phi}(A X) & \approx \frac{1}{2} \sum_{j=1}^{2 m}\left(\left[c_{g}(A X), c_{g}\left(A e_{j}\right)\right] \hat{\nabla}_{A e_{j}}^{g} \phi, \phi\right) \\
& \approx \frac{1}{2} \sum_{j=1}^{2 m}\left(\left[c_{g}(A X), c_{g}\left(A e_{j}\right)\right]\left(\hat{\nabla}_{A e_{j}}^{g}-\hat{\nabla}_{A e_{j}}^{g_{0}}\right) \phi, \phi\right) \\
& \approx \frac{1}{2} \sum_{j=1}^{2 m}\left(\left[X \cdot, e_{j} \cdot\right]\left(\hat{\nabla}_{A e_{j}}^{g}-\hat{\nabla}_{A e_{j}}^{g_{0}}\right) \phi, \phi\right),
\end{aligned}$$
which expands into
$$\begin{aligned}
& \frac{1}{2} \sum_{j=1}^{2 m}\left(\left[X \cdot, e_{j} \cdot\right]\left(\nabla_{A e_{j}}^{g}-\nabla_{A e_{j}}^{g_{0}}\right) \phi, \phi\right) \\
+ & \frac{i}{4} \sum_{j=1}^{2 m}\left(\left[X \cdot, e_{j} \cdot\right]\left(c_{g}\left(A e_{j}-i J A e_{j}\right) \pi_{l-1}^{\Omega}-c_{g_{0}}\left(A e_{j}-i J A e_{j}\right) \pi_{l-1}^{\Omega_{0}}\right) \phi, \phi\right) \\
+ & \frac{i}{4} \sum_{j=1}^{2 m}\left(\left(\left[X \cdot, e_{j} \cdot\right]\left(c_{g}\left(A e_{j}+i J A e_{j}\right) \pi_{l}^{\Omega}-c_{g_{0}}\left(A e_{j}+i J A e_{j}\right) \pi_{l}^{\Omega_{0}}\right) \phi, \phi\right),\right.
\end{aligned}$$
that is
$$\begin{aligned}
& \frac{1}{2} \sum_{j=1}^{2 m}\left(\left[X \cdot, e_{j} \cdot\right]\left(\nabla_{A e_{j}}^{g}-\nabla_{A e_{j}}^{g_{0}}\right) \phi, \phi\right) \\
+ & \frac{i}{4} \sum_{j=1}^{2 m}\left(\left[X \cdot, e_{j} \cdot\right]\left(\left(e_{j}-i A^{-1} J A e_{j}\right) \cdot \pi_{l-1}^{\Omega}-\left(A e_{j}-i J A e_{j}\right) \cdot \pi_{l-1}^{\Omega_{0}}\right) \phi, \phi\right) \\
+ & \frac{i}{4} \sum_{j=1}^{2 m}\left(\left(\left[X \cdot, e_{j} \cdot\right]\left(\left(e_{j}+i A^{-1} J A e_{j}\right) \cdot \pi_{l}^{\Omega}-\left(A e_{j}+i J A e_{j}\right) \cdot \pi_{l}^{\Omega_{0}}\right) \phi, \phi\right) .\right.
\end{aligned}$$
In view of lemma 3.4 and corollary 3.5, we are left with :
$$\begin{aligned}
\zeta_{\phi, \phi}(A X) & \approx \frac{1}{2} \sum_{j=1}^{2 m}\left(\left[X \cdot, e_{j} \cdot\right]\left(\nabla_{A e_{j}}^{g}-\nabla_{A e_{j}}^{g_{0}}\right) \phi, \phi\right) \\
& +\frac{i}{4} \sum_{j=1}^{2 m}\left(\left[X \cdot, e_{j} \cdot\right]\left(\left(e_{j}-i J e_{j}\right)-\left(A e_{j}-i J A e_{j}\right)\right) \cdot \pi_{l-1}^{\Omega_{0}} \phi, \phi\right) \\
& +\frac{i}{4} \sum_{j=1}^{2 m}\left(\left[X \cdot, e_{j} \cdot\right]\left(\left(e_{j}+i A e_{j}\right)-\left(A e_{j}+i J A e_{j}\right)\right) \cdot \pi_{l}^{\Omega_{0}} \phi, \phi\right) .
\end{aligned}$$
With $A=1+H$ we can there therefore write $\zeta_{\phi, \phi}(A X) \approx I+I I+I I I$, with :
$$\begin{aligned}
I & :=\frac{1}{2} \sum_{j=1}^{2 m}\left(\left[X \cdot, e_{j} \cdot\right]\left(\nabla_{A e_{j}}^{g}-\nabla_{A e_{j}}^{g_{0}}\right) \phi, \phi\right) \\
I I & :=-\frac{i}{4} \sum_{j=1}^{2 m}\left(\left[X \cdot, e_{j} \cdot\right] H e_{j} \cdot \phi, \phi\right) \\
I I I & :=-\frac{1}{4} \sum_{j=1}^{2 m}\left(\left[X \cdot, e_{j} \cdot\right] J H e_{j} \cdot \tilde{\phi}, \phi\right) .
\end{aligned}$$
The computation of the real part of the first term is classical (cf. [CH] or lemma 10 in [Min], for instance) :
$$\operatorname{Re} I \approx-\frac{1}{4}\left(d \operatorname{Tr}_{g_{0}} g+\operatorname{div}_{g_{0}} g\right)|\phi|^{2} .$$

The second term is basically computed in [CH]. Indeed, since $H$ is symmetric, we use the identity $\left[X \cdot, e_{j} \cdot\right]=2 X_{j}+2 X \cdot e_{j}$. to obtain
$$\begin{aligned}
\operatorname{Re} I I & =-\frac{i}{2}(H X \cdot \phi, \phi)-\frac{i}{2} \sum_{j, l=1}^{2 m} H_{j l}\left(X \cdot e_{j} \cdot e_{l} \cdot \phi, \phi\right) \\
& =-\frac{i}{2}(H X \cdot \phi, \phi)+\frac{i}{2} \operatorname{Tr} H(X \cdot \phi, \phi) .
\end{aligned}$$
In the same way, the third term can be written
$$I I I=-\frac{1}{2}\left((J H X \cdot \tilde{\phi}, \phi)-\frac{1}{2} \sum_{j=1}^{2 m}\left(X \cdot e_{j} \cdot J H e_{j} \cdot \tilde{\phi}, \phi\right) .\right.$$
Lemma 3.7 - $\operatorname{Re} \sum_{j=1}^{2 m}\left(X \cdot e_{j} \cdot J H e_{j} \cdot \tilde{\phi}, \phi\right) \approx-2(J H X \cdot \tilde{\phi}, \phi)$.
Proof. Let us set $M:=J H$ and $M_{i j}:=\left(e_{i}, M e_{j}\right)$, so that
$$\sum_{j=1}^{2 m}\left(X \cdot e_{j} \cdot J H e_{j} \cdot \tilde{\phi}, \phi\right)=\sum_{j, k, p} M_{k j} X_{p}\left(e_{p} \cdot e_{j} \cdot e_{k} \cdot \tilde{\phi}, \phi\right) .$$
Lemma 3.4 ensures $J H \approx H J$. Since $H$ is symmetric and $J$ antisymmetric, we deduce that $M$ is antisymmetric up to a negligible term. In particular, $M_{k j} \approx 0$ when $k=j$, hence
$$\sum_{j=1}^{2 m}\left(X \cdot e_{j} \cdot J H e_{j} \cdot \tilde{\phi}, \phi\right) \approx \sum_{j \neq k} \sum_{p} M_{k j} X_{p}\left(e_{p} \cdot e_{j} \cdot e_{k} \cdot \tilde{\phi}, \phi\right) .$$
Given three distinct indices $j, k, p$ we consider the expression
$$\left(e_{p} \cdot e_{j} \cdot e_{k} \cdot \tilde{\phi}, \phi\right)=\left(e_{p} \cdot e_{j} \cdot e_{k} \cdot\left(\phi_{l-1}-\phi_{l}\right),\left(\phi_{l-1}+\phi_{l}\right)\right) .$$
Property (7) reduces it into
$$\left(e_{p} \cdot e_{j} \cdot e_{k} \cdot \tilde{\phi}, \phi\right)=\left(e_{p} \cdot e_{j} \cdot e_{k} \cdot \phi_{l-1}, \phi_{l}\right)-\left(e_{p} \cdot e_{j} \cdot e_{k} \cdot \phi_{l}, \phi_{l-1}\right) .$$
and since the indices are distinct, this is imaginary. So
$$\begin{aligned}
& \operatorname{Re} \sum_{j=1}^{2 m}\left(X \cdot e_{j} \cdot J H e_{j} \cdot \tilde{\phi}, \phi\right) \\
\approx & \operatorname{Re} \sum_{j \neq k} M_{k j} X_{j}\left(e_{j} \cdot e_{j} \cdot e_{k} \cdot \tilde{\phi}, \phi\right)+\operatorname{Re} \sum_{j \neq k} M_{k j} X_{k}\left(e_{k} \cdot e_{j} \cdot e_{k} \cdot \tilde{\phi}, \phi\right) \\
\approx & -\operatorname{Re} \sum_{j \neq k} M_{k j} X_{j}\left(e_{k} \cdot \tilde{\phi}, \phi\right)+\operatorname{Re} \sum_{j \neq k} M_{k j} X_{k}\left(e_{j} \cdot \tilde{\phi}, \phi\right) \\
\approx & -2 \operatorname{Re} \sum_{j \neq k} M_{k j} X_{j}\left(e_{k} \cdot \tilde{\phi}, \phi\right) \\
\approx & -2 \operatorname{Re}(M X \cdot \tilde{\phi}, \phi) \\
\approx & -2(M X \cdot \tilde{\phi}, \phi) .
\end{aligned}$$ \(\square\)

This lemma leads to
$$\operatorname{Re} I I I \approx-\frac{1}{2}(J H X \cdot \tilde{\phi}, \phi)+(J H X \cdot \tilde{\phi}, \phi)=\frac{1}{2}(J H X \cdot \tilde{\phi}, \phi) .$$
Eventually, summing $I, I I$ and $I I I$, we get :
$$\begin{aligned}
\operatorname{Re} \zeta_{\phi, \phi}(A X) \approx & -\frac{1}{4}\left(d \operatorname{Tr}_{g_{0}} g+\operatorname{div}_{g_{0}} g\right)|\phi|^{2} \\
& -\frac{i}{2}(H X \cdot \phi, \phi)+\frac{i}{2} \operatorname{Tr} H(X \cdot \phi, \phi) \\
& +\frac{1}{2}(J H X \cdot \tilde{\phi}, \phi) .
\end{aligned}$$
Lemmata 2.4 and 2.5 simplify this into
$$\begin{aligned}
\operatorname{Re} \zeta_{\phi, \phi}(A X) & \approx-\frac{1}{4}\left(d \operatorname{Tr}_{g_{0}} g+\operatorname{div}_{g_{0}} g\right)|\phi|^{2}+\frac{i}{2} \operatorname{Tr} H(X \cdot \phi, \phi) \\
& \approx-\frac{1}{4}\left(d \operatorname{Tr}_{g_{0}} g+\operatorname{div}_{g_{0}} g\right)|\phi|^{2}-\frac{1}{4} \operatorname{Tr} H \mathrm{~d}|\phi|^{2}(X) .
\end{aligned}$$
Since $g-g_{0} \approx-2 g_{0}(H .,$.$) , we have \operatorname{Tr}\left(g-g_{0}\right) \approx-2 \operatorname{Tr} H$, hence :
$$\operatorname{Re} \zeta_{\phi, \phi}(A X) \approx-\frac{1}{4}\left(d \operatorname{Tr}_{g_{0}} g+\operatorname{div}_{g_{0}} g\right)(X)|\phi|^{2}+\frac{1}{8} \operatorname{Tr}_{g_{0}}\left(g-g_{0}\right) \mathrm{d}|\phi|^{2}(X),$$
which yields the formula of proposition 3.6. \(\square\)
3.2. The mass linear functional. We consider the formula
$$\mu_{g}(\xi, \alpha, u)=-\frac{1}{4} \lim _{R \rightarrow \infty} \int_{S_{R}} *\left(\left(d \operatorname{Tr}_{g_{0}} g+\operatorname{div}_{g_{0}} g\right) u+\frac{1}{2} \operatorname{Tr}_{g_{0}}\left(g-g_{0}\right) J \alpha\right) .$$
If $(\xi, \alpha, u)$ belongs to $Q_{\mathbb{C} H^{m}}\left(\mathcal{K}_{\mathbb{C} H^{m}}\right)$, the considerations of the previous paragraph imply that $\mu_{g}(\xi, \alpha, u)$ is an element of $[0,+\infty]$. If it is infinite at some point of $Q_{\mathbb{C} H^{m}}\left(\mathcal{K}_{\mathbb{C} H^{m}}\right)$, we decide that the mass is infinite : $\mu_{g}=\infty$. Otherwise, this defines a linear functional $\mu_{g}$ on the linear span of $Q_{\mathbb{C} H^{m}}\left(\mathcal{K}_{\mathbb{C} H^{m}}\right) \subset \mathcal{N}_{\mathbb{C} H^{m}, 0}$, which is $\mathcal{N}_{\mathbb{C} H^{m}, 0}$, since it is $P U(m, 1)$ -invariant and the action of this group on $\Lambda_{J, 0}^{2} \mathbb{R}^{2 m, 2}$ is irreducible.

The previous paragraph also indicates that $\mu_{g}$ takes non-negative values on (the convex cone generated by) $Q_{\mathbb{C} H^{m}}\left(\mathcal{K}_{\mathbb{C} H^{m}}\right)$; since $Q_{\mathbb{C} H^{m}}\left(\mathcal{K}_{\mathbb{C} H^{m}}\right)$ is $P U(m, 1)$-invariant and contains one element of $\mathcal{N}_{\mathbb{C} H^{m}, 0}^{+}$(from the explicit computations in 2.3), it contains $\mathcal{N}_{\mathbb{C} H^{m}, 0}^{+}$. So $\mu_{g}$ is non-negative on $\mathcal{N}_{\mathbb{C} H^{m}, 0}^{+}$.

Assume $\mu_{g}$ vanishes on $\mathcal{N}_{\mathbb{C} H^{m}, 0}$. Then Lemma 3.2, coupled to the Bochner formula, ensures that for every $\psi$ in $\mathcal{K}_{\mathbb{C} H^{m}}$, there is a Kählerian Killing spinor $\phi$ on $(M, g)$, namely $\phi \in \mathcal{K}_{g}$, that is asymptotic to $\psi$. In particular, for any element $\beta=Q_{\mathbb{C} H^{m}}(\psi)$ of $\mathcal{N}_{\mathbb{C} H^{m}, 0}^{+}$, there is an element $\tilde{\beta}=Q_{g}(\phi)$ of $\mathcal{N}_{g, 0}$ that is asymptotic to $\beta$. Since the linear span of $\mathcal{N}_{\mathbb{C} H^{m}, 0}^{+}$is the whole $\mathcal{N}_{\mathbb{C} H^{m}, 0}$, we deduce that $\mathcal{N}_{g, 0}$ has maximal dimension, which implies that $\mathcal{N}_{g}$ has maximal dimension (add the Kähler form) : $(M, g)$ is (locally) complex hyperbolic. In view of its asymptotic, it is bound to be $\mathbb{C} H^{m}$.

The holomorphic chart at infinity in Definition 3.1 is of course not unique. Any two relevant charts $\Psi_{1}$ and $\Psi_{2}$ differ by a biholomorphism $f:=\Psi_{2} \circ \Psi_{1}^{-1}$ of $\mathbb{C} H^{m}$ such that $f^{*} g_{0}$ is asymptotic to $g_{0}$. The map $f$ therefore induces a CR-automorphism of the sphere at infinity, so that $f$ is asymptotic to an element of $P U(m, 1)$. As in the remark after Definition 3.1, we conclude $f$ is an element of $P U(m, 1)$. So the model at infinity is unique up to its natural automorphism group $P U(m, 1)$. If $\phi_{1}$ is a Kählerian Killing
spinor in the chart $\Psi_{1}$, then $\phi_{2}:=f_{*} \phi_{1}$ is a Kählerian Killing spinor in the chart $\Psi_{2}$ (by naturality). We claim that
Lemma 3.8 - $\mu_{g}^{\Psi_{1}}\left(\beta_{\phi_{1}}\right)=\mu_{g}^{\Psi_{2}}\left(\beta_{\phi_{2}}\right)$.
Proof. Recall that in the notations introduced in the previous paragraph,
$$\mu_{g}^{\Psi_{1}}\left(\beta_{\phi_{1}}\right)=\lim _{R \rightarrow \infty} \int_{S_{R}^{\Psi_{1}}} * \zeta_{\phi_{1}, \phi_{1}}=\lim _{R \rightarrow \infty} \int_{S_{R}^{\Psi_{1}}} * \zeta_{\psi_{1}, \psi_{1}} .$$
This quantity is equal to the well-defined integral
$$\begin{aligned}
& \int_{M}\left|\hat{\nabla} \psi_{1}\right|^{2}+\frac{1}{4} \int_{M}(\operatorname{Scal}+4 m(m+1))\left|\psi_{1}\right|^{2} \\
& +(m+1) \int_{M}\left(\left|\psi_{1}\right|^{2}-\left|\pi_{l-1}^{\Omega} \psi_{1}\right|^{2}-\left|\pi_{l}^{\Omega} \psi_{1}\right|^{2}\right),
\end{aligned}$$
so that we can compute it with another family of spheres :
$$\mu_{g}^{\Psi_{1}}\left(\beta_{\phi_{1}}\right)=\lim _{R \rightarrow \infty} \int_{f\left(S_{R}^{\Psi_{1}}\right)} * \zeta_{\psi_{1}, \psi_{1}}=\lim _{R \rightarrow \infty} \int_{f\left(S_{R}^{\Psi_{1}}\right)} * \zeta_{\phi_{1}, \phi_{1}} .$$
Since $f^{*} g_{0}=g_{0}$ and $f\left(S_{R}^{\Psi_{1}}\right)=S_{R}^{\Psi_{2}}$, we therefore obtain
$$\begin{aligned}
\mu_{g}^{\Psi_{1}}\left(\beta_{\phi_{1}}\right) & =\lim _{R \rightarrow \infty} \int_{f\left(S_{R}^{\Psi_{1}}\right)} * g_{0}\left(-\frac{1}{4}\left(d \operatorname{Tr}_{g_{0}} g+\operatorname{div}_{g_{0}} g\right)\left|\phi_{1}\right|_{g_{0}}^{2}+\frac{1}{8} \operatorname{Tr}_{g_{0}}\left(g-g_{0}\right) d\left|\phi_{1}\right|_{g_{0}}^{2}\right) \\
& =\lim _{R \rightarrow \infty} \int_{S_{R}^{\Psi_{2}}} * g_{0}\left(-\frac{1}{4}\left(d \operatorname{Tr}_{g_{0}} g+\operatorname{div}_{g_{0}} g\right)\left|f^{*} \phi_{2}\right|_{g_{0}}^{2}+\frac{1}{8} \operatorname{Tr}_{g_{0}}\left(g-g_{0}\right) d\left|f^{*} \phi_{2}\right|_{g_{0}}^{2}\right) . \\
& =\lim _{R \rightarrow \infty} \int_{S_{R}^{\Psi_{2}}} * g_{0}\left(-\frac{1}{4}\left(d \operatorname{Tr}_{g_{0}} g+\operatorname{div}_{g_{0}} g\right)\left|\phi_{2}\right|_{g_{0}}^{2}+\frac{1}{8} \operatorname{Tr}_{g_{0}}\left(g-g_{0}\right) d\left|\phi_{2}\right|_{g_{0}}^{2}\right) \\
& =\mu_{g}^{\Psi_{2}}\left(\beta_{\phi_{2}}\right)
\end{aligned}$$ \(\square\)

In other words, changing the chart at infinity by an automorphism $f \in P U(m, 1)$ results in turning $\mu_{g}$ to $f^{*} \mu_{g}$. So $\mu_{g}$ is well-defined up to the natural action of $P U(m, 1)$. We have proved the following result.

Theorem 3.9 - Let $\left(M^{m}, g, J\right)$ be a spin asymptotically complex hyperbolic Kähler manifold with odd complex dimension $\operatorname{Scal}_{g} \geq \operatorname{Scal}_{\mathbb{C} H^{m}}$. Then the linear functional $\mu_{g}$ on $\mathcal{N}_{\mathbb{C} H^{m}, 0}$ is well-defined up to the natural action of $P U(m, 1)$; it is non-negative on $\mathcal{N}_{\mathbb{C} H^{m}, 0}^{+}$and vanishes if and only if $\left(M^{m}, g, J\right)$ is the complex hyperbolic space.

\section*{4. The case of even-dimensional manifolds.}
4.1. The twisted Kählerian Killing spinors. To extend the ideas above to the even-dimensional case, it seems that we need Kählerian Killing spinors on even-dimensional complex hyperbolic spaces. Unfortunately, such Kählerian Killing spinors do not exist. To overcome this cruel reality, we follow [BH] and turn to the spin ${ }^{c}$ realm. We refer to [LM] for basic definitions about spin ${ }^{c}$ structures.

We consider a Kähler manifold $(M, g, J)$ with even complex dimension $m=2 l$. As in [BH], we further assume that the cohomology class of $\frac{\Omega}{i \pi}$ is integral, i.e. in the image of $H^{2}(M, \mathbb{Z}) \rightarrow H^{2}(M, \mathbb{R})$. This determines a complex line bundle $L$ endowed with a Hermitian metric and a unitary connection with curvature $F=-2 i \Omega$; the Chern class
of $L$ is $c_{1}(L)=\frac{i}{2 \pi}[F]=\frac{1}{\pi}[\Omega]$. We also assume that $(M, L)$ defines a spin ${ }^{c}$ structure, in that the bundle $T M \otimes L$ admits a spin structure. We then introduce the corresponding spinor bundle $\Sigma^{c}$, endowed with a Clifford action $c$ and a connection ∇ . The Kähler form $\Omega$ acts on this bundle, with the eigenvalues $i(m-2 k), 0 \leq k \leq m$. The eigenspaces yield subbundles $\Sigma_{k}^{c}$. We may therefore define a connection $\hat{\nabla}$ on $\Sigma^{c}$ by requiring that
$$\hat{\nabla}_{X} \psi:=\nabla_{X} \psi+i c\left(X^{1,0}\right) \psi_{l-1}+i c\left(X^{0,1}\right) \psi_{l},$$
where $\psi_{k}$ is the component of $\psi$ in $\Sigma_{k}^{c}$. The parallel sections of $\Sigma_{l-1}^{c} \oplus \Sigma_{l}^{c}$ for this connection will be called twisted Kählerian Killing spinors and the corresponding subspace will be denoted by $\mathcal{K}^{c}$.

Every computation of section 2.3 (but one) can be carried out with twisted Kählerian Killing spinors, leading to the same formulas. In particular, one can define $u_{\psi}, \alpha_{\psi}, \xi_{\psi}$ for any $\psi$ in $\mathcal{K}^{c}$ as in section 2.3 and this yields a map $Q^{c}: \mathcal{K}^{c} \rightarrow \mathcal{N}$. The only difference is that we do not get elements of $\mathcal{N}_{0}:\left(\xi_{\psi}, \Omega\right)$ is no longer $u_{\psi}$, basically because the eigenvalues of the Kähler form are now even (compare with the proof of Lemma 2.6).

Let us describe the model case, where $(M, g, J)$ is the complex hyperbolic space $\mathbb{C} H^{m}, m=2 l$, with holomorphic sectional curvature -4. With this normalization, we have $\operatorname{Ric}_{\mathbb{C}_{H^{m}}}=-2(m+1) g_{\mathbb{C H}^{m}}$. Since the Ricci form $\rho=\operatorname{Ric}(., J$.$) is i$ times the curvature of the canonical line bundle, this implies :
$$c_{1}\left(\Lambda^{m, 0}\right)=\frac{i}{2 \pi}[-i \rho]=\frac{i}{2 \pi}[2 i(m+1) \Omega]=-\frac{m+1}{\pi}[\Omega]=-(m+1) c_{1}(L) .$$
So $L \cong\left(\Lambda^{m, 0}\right)^{-\frac{1}{m+1}}$ in this case. It follows that
$$\Sigma_{k}^{c} \cong \Sigma_{k} \otimes L \cong \Lambda^{0, k} \otimes\left(\Lambda^{m, 0}\right)^{\frac{1}{2}-\frac{1}{m+1}} \cong \Lambda^{0, k} \otimes\left(\Lambda^{m, 0}\right)^{\frac{l}{2 l+1}} .$$
It turns out that the sections of $\mathcal{K}^{c}$ trivialize the bundle $\Sigma_{l-1}^{c} \oplus \Sigma_{l}^{c}$, as noticed in [BH]. Indeed, using the same notations as in section 2.3, we can define two families of twisted Kählerian Killing spinors in the following way. First, if $a$ is a multi-index of length $l-1$, we set $\varphi^{a}=\varphi_{l-1}^{a}+\varphi_{l}^{a}$ with
$$\varphi_{l-1}^{a}=c(l) \frac{d \bar{w}_{a}}{\left(1-|w|^{2}\right)^{l}} \otimes d w^{\frac{l}{2 l+1}} \quad \text { and } \quad \varphi_{l}^{a}=\frac{c(l)}{2 i l} \bar{\partial}\left(\frac{d \bar{w}_{a}}{\left(1-|w|^{2}\right)^{l}}\right) \otimes d w^{\frac{l}{2 l+1}} .$$
The normalization we choose is $c(l)=2^{1-l-\frac{l^{2}}{2 l+1}}$. We also introduce $\breve{\varphi}^{b}=\breve{\varphi}_{l-1}^{b}+\breve{\varphi}_{l}^{b}$ where $b$ is a multi-index of length $l$ and
$$\breve{\varphi}_{l-1}^{b}=c(l) \frac{\iota_{\bar{R}} d \bar{w}_{b}}{\left(1-|w|^{2}\right)^{l}} \otimes d w^{\frac{l}{2 l+1}} \quad \text { and } \quad \breve{\varphi}_{l}^{b}=\frac{c(l)}{2 i l} \bar{\partial}\left(\frac{\iota_{\bar{R}} d \bar{w}_{b}}{\left(1-|w|^{2}\right)^{l}}\right) \otimes d w^{\frac{l}{2 l+1}}$$
where $R=\sum_{k} w_{k} \partial_{w_{k}}$ as before. These families together form a basis for $\mathcal{K}^{c}$ on $\mathbb{C} H^{m}$. One can again compute the squared norms of these spinors, like in [Kir]. If $a$ is a multi-index of length $l-1$ and $b$ a multi-index of length $l$, we have
$$\left|\varphi_{l-1}^{a}\right|^{2}=\frac{1-\left|w_{a}\right|^{2}}{1-|w|^{2}}, \quad\left|\varphi_{l}^{a}\right|^{2}=\frac{\left|w_{\breve{a}}\right|^{2}}{1-|w|^{2}}, \quad\left|\breve{\varphi}_{l-1}^{b}\right|^{2}=\frac{\left|w_{b}\right|^{2}}{1-|w|^{2}}, \quad\left|\breve{\varphi}_{l}^{b}\right|^{2}=\frac{1-\left|w_{\breve{b}}\right|^{2}}{1-|w|^{2}},$$
hence
$$\left|\varphi^{a}\right|^{2}=\frac{1-\left|w_{a}\right|^{2}+\left|w_{\breve{a}}\right|^{2}}{1-|w|^{2}}, \quad\left|\breve{\varphi}^{b}\right|^{2}=\frac{1-\left|w_{\breve{b}}\right|^{2}+\left|w_{b}\right|^{2}}{1-|w|^{2}} .$$

Exactly as in the odd dimensional case, we see that the corresponding elements of $\mathcal{N}\left(\mathbb{C} H^{m}\right) \cong \Lambda_{J}^{2} \mathbb{R}^{2 m, 2}$ are
$$\begin{aligned}
Q^{c}\left(\varphi^{a}\right) & =\beta_{\varphi^{a}}=-\sum_{j=1}^{l-1} J d x_{a_{j}} \wedge d x_{a_{j}}+\sum_{j=1}^{l+1} J d x_{\breve{a}_{j}} \wedge d x_{\breve{a}_{j}}+J d x_{m+1} \wedge d x_{m+1}, \\
Q^{c}\left(\breve{\varphi}^{b}\right)=\beta_{\breve{\varphi}^{b}} & =-\sum_{j=1}^{l} J d x_{b_{j}} \wedge d x_{b_{j}}+\sum_{j=1}^{l} J d x_{\breve{b}_{j}} \wedge d x_{\breve{b}_{j}}+J d x_{m+1} \wedge d x_{m+1},
\end{aligned}$$
It follows that $\left\langle\beta_{\varphi^{a}}, \beta_{\phi^{a}}\right\rangle=<\beta_{\breve{\varphi}^{b}}, \beta_{\breve{\varphi}^{b}}>=m+1,<\beta_{\varphi^{a}}, \omega>=1$ and $<\beta_{\breve{\varphi}^{b}}, \omega>=-1$. The $\beta_{\varphi^{a}}$ 's all belong to the same orbit under the action of $P U(m, 1):$ let $\mathcal{N}_{\mathbb{C} H^{m}}^{+1}$ be this orbit. The $\beta_{\breve{\varphi}}$ 's also belong to the same orbit under the action of $P U(m, 1)$ and we denote it by $\mathcal{N}_{\mathbb{C} H^{m}}^{-1}$.

\subsection*{4.2. The positive mass theorem.}

Theorem 4.1 - Let $\left(M^{m}, g, J\right)$ be an asymptotically complex hyperbolic Kähler manifold with even complex dimension and $\mathrm{Scal}_{g} \geq \mathrm{Scal}_{\mathbb{C} H^{m}}$. We assume that the cohomology class of $\frac{\Omega}{i \pi}$ is integral, providing a line bundle $L$ as above, and that $(M, L)$ defines a spin ${ }^{c}$ structure. Then the formula (10) defines a (possibly infinite) linear functional $\mu_{g}$ on $\mathcal{N}_{\mathbb{C} H^{m}}$. It is well defined by $g$ up to the natural action of $P U(m, 1)$, non-negative on $\mathcal{N}_{\mathbb{C} H^{m}}^{+1} \cup \mathcal{N}_{\mathbb{C} H^{m}}^{-1}$ and vanishes if and only if $\left(M^{m}, g, J\right)$ is the complex hyperbolic space.

Note the assumption about $[\Omega]$ and $L$ are of course satisfied when $M$ is contractible.
Proof. The proof is nearly the same as in the odd dimensional case. The analytical part is completely similar, cf. [BH]. So, for every element $\phi$ of $\mathcal{K}_{\mathbb{C} H^{m}}^{c}$, one may find an harmonic spinor $\psi$ on $M$ that is asymptotic to $\phi$ (harmonic means in the kernel of some Dirac operator, cf. [BH]). We may then proceed to the same computation, leading to the same mass integral at infinity, $\mu_{g}$, defined on the linear span of $Q^{c}\left(\mathcal{K}^{c}\right)$ in $\mathcal{N}$. From the computations above we know that $Q^{c}\left(\mathcal{K}^{c}\right)$ contains $\mathcal{N}_{\mathbb{C} H^{m}}^{+1} \cup \mathcal{N}_{\mathbb{C} H^{m}}^{-1}$. Using the $P U(m, 1)$ invariance, it is easy to see that this is the whole $\mathcal{N}_{\mathbb{C} H^{m}}$. The nonnegativity statement is automatic and the fact that $\mu_{g}$, up to $P U(m, 1)$, depends only on $g$ is like in the odd case.

We are left to justify the rigidity part. If the mass $\mu_{g}$ vanishes, we know by construction that every element $\phi$ of $\mathcal{K}_{\mathbb{C} H^{m}}^{c}$ gives rise to an element $\psi$ of $\mathcal{K}_{g}^{c}$ that is asymptotic to $\phi$. In particular, for any element $\beta=Q_{\mathbb{C} H^{m}}^{c}(\phi)$ of $\mathcal{N}_{\mathbb{C} H^{m}}^{ \pm 1}$, there is an element $\tilde{\beta}=Q_{g}^{c}(\psi)$ of $\mathcal{N}_{g}$ that is asymptotic to $\beta$. As a consequence, $\mathcal{N}_{g}$ has maximal dimension : $(M, g)$ is complex hyperbolic. \(\square\)

\section*{Appendix : an example.}

To build a non-trivial example of asymptotically complex hyperbolic Kähler manifold, we use the symplectic point of view of [HS]. We work on $\mathbb{C}^{m}, m \geq 2$ and let $\rho=e^{t}$ be the Euclidean distance to the origin. Then $d d^{c} t=\omega_{F S}$ is the pull-back to $\mathbb{C}^{m} \backslash\{0\}$ of the Fubini-Study form on $\mathbb{C} P^{m-1}$. Every $U(m)$-invariant Kähler structure on $\mathbb{C}^{m} \backslash\{0\}$ admits a Kähler form reading
$$\omega=\psi^{\prime}(t) d t \wedge d^{c} t+\psi(t) \omega_{F S},$$
where $\psi$ is simply the derivative of a radial Kähler potential with respect to the variable $t$. The function $\psi$ and $\psi^{\prime}$ must of course be positive. In fact $\psi$ can be seen as a moment
map for the standard action of $\mathbb{S}^{1}$ on $\mathbb{C}^{m} \backslash\{0\}$ endowed with the symplectic form $\omega$. If $I$ denotes the range of the function $\psi$, we define the "momentum profile" $\Theta$ as the positive function $\Theta:=\psi^{\prime} \circ \psi^{-1}$ on $\left.I=\right] \inf \psi, \sup \psi[$. The Kähler metric extends smoothly near 0 if and only if $\inf \psi=0$ and $\Theta$ is smooth near 0 with $\Theta(0)=0$ and $\Theta^{\prime}(0)=2$. Setting $x:=\psi(t) \in I$, the Kähler form is given by
$$\omega=\omega_{\Theta}=\frac{d x \wedge d^{c} x}{\Theta(x)}+x \omega_{F S}$$
and its scalar curvature is
$$s_{\Theta}(x)=\frac{2 m(m-1)}{x}-\frac{\partial_{x x}\left(x^{m-1} \Theta(x)\right)}{x^{m-1}} .$$
The flat metric corresponds to $\Theta(x)=2 x, x \in \mathbb{R}_{+}$, the complex hyperbolic metric to $\Theta(x)=2 x+2 x^{2}, x \in \mathbb{R}_{+}$and the Fubini-Study metric on $\mathbb{C} P^{m}$ to $\Theta(x)=2 x-2 x^{2}$, $x \in[0,1]$.

Let $\Theta_{0}(x)=2 x^{2}+2 x$ be the momentum profile of the complex hyperbolic metric. We wish to build a $U(m)$-invariant Kähler metric with complex hyperbolic asymptotic and scalar curvature bounded from below by the scalar curvature of the complex hyperbolic model. We therefore need to find a positive function $\Theta$ defined on $\mathbb{R}_{+}$, such that $\Theta(0)=0, \Theta^{\prime}(0)=2, \Theta(x)$ is asymptotic to $2 x+2 x^{2}$ as $x$ goes to infinity and $s_{\Theta} \geq s_{\Theta_{0}}$. Setting $\Theta(x)=\Theta_{0}(x)-\alpha(x)$, we are lead to find a non zero function $\alpha$ such that $\Theta_{0}-\alpha$ is non-negative, $\alpha(0)=\alpha^{\prime}(0)=0, \alpha=o\left(x^{2}\right)$ as $x$ goes to infinity and $\partial_{x x}\left(x^{m-1} \alpha(x)\right) \geq 0$. Such a function $\alpha$ can be obtained by choosing
$$\alpha(x):=x^{1-m} \int_{0}^{x} \int_{0}^{y} \chi(z) d z d y,$$
where $\chi$ is a bump function with support inside $[1,+\infty[$ and with unit integral. One can then observe that $\alpha(x)$ vanishes on [0, 1] and is equivalent to $x^{2-m}$ as $x$ goes to infinity, while satisfying the desired differential inequality ; besides, the normalization of $\chi$ ensures $\alpha(x) \leq x$ for every $x \geq 0$, which guarantees $\Theta_{0}-\alpha \geq 0$. The Kähler form is then
$$\omega_{\Theta}=\omega_{\Theta_{0}}+\left(\frac{\Theta_{0}(x)}{\Theta(x)}-1\right) \frac{d x \wedge d^{c} x}{\Theta_{0}(x)}$$
with $\frac{\Theta_{0}(x)}{\Theta(x)}-1 \sim \frac{x^{-m}}{2}$. To understand the asymptotic of this, we relate $x$ to the initial variable $t_{0}$ on the complex hyperbolic space. The properties $\frac{d t_{0}}{d x}=\frac{1}{\Theta_{0}(x)}$ and $t_{0}(x=+\infty)=0$ yield $t_{0} \sim-\frac{1}{2 x}$. The geodesic distance $r$ to 0 in the complex hyperbolic model is given by $r=\tanh e^{t_{0}}$ so that $x \sim \frac{e^{2 r}}{4}$ at infinity. So our Kähler metric satisfies $\omega=\omega_{0}+\mathcal{O}\left(e^{-2 m r}\right)$.

Remark. The rate of the falloff to the model at infinity that we obtained is optimal in the radial case. In other words, a function $\alpha$ satisfying the desired properties cannot decay faster at infinity. This is due to the fact that the function $x \mapsto x^{m-1} \alpha(x)$ must be convex on $\mathbb{R}_{+}$with zero first order jet at 0 ; so either it vanishes identically or it grows at least linearly.

\section*{References}
\begin{itemize}
\item[] [AD] L. Andersson, M. Dahl, Scalar curvature rigidity for asymptotically locally hyperbolic manifolds, Ann. Global Anal. Geom. 16 (1998), no. 1, 1-27.
\item[] [ACG] V. Apostolov, D. M. J. Calderbank, P. Gauduchon, Hamiltonian 2-forms in Kähler geometry. I. General theory, J. Differential Geom. 73 (2006), no. 3, 359-412.
\end{itemize}
[ADM] R. Arnowitt, S. Deser, C. W. Misner, Coordinate invariance and energy expressions in general relativity, Phys. Rev. (2) 1221961 997-1006.
[Bart] R. Bartnik, The mass of an asymptotically flat manifold, Commun. Pure Appl. Math., 39, 661-693, (1986).
[Bau] H. Baum, Complete Riemannian manifolds with imaginary Killing spinors, Ann. Global Anal. Geom. 7 (1989), no. 3, 205-226.
[Biq] O. Biquard, Asymptotically symmetric Einstein metrics, Translated from the 2000 French original by Stephen S. Wilson. SMF/AMS Texts and Monographs, 13. American Mathematical Society, Providence, RI; Société Mathématique de France, Paris, 2006.
[BH] H. Boualem, M. Herzlich, Rigidity at infinity for even-dimensional asymptotically complex hyperbolic spaces, Ann. Sc. Norm. Super. Pisa Cl. Sci. (5) 1 (2002), no. 2, 461-469.
[CH] P. T. Chruściel, M. Herzlich, The mass of asymptotically hyperbolic Riemannian manifolds, Pacific J. Math. 212 (2003), no. 2, 231-264.
[Dai] X. Dai, A positive mass theorem for spaces with asymptotic SUSY compactification, Comm. Math. Phys. 244 (2004), no. 2, 335-345.
[Gal] S. Gallot, Équations différentielles caractéristiques de la sphère, Ann. Sci. cole Norm. Sup. (4) 12 (1979), no. 2, 235-267.
[Her] M. Herzlich, Scalar curvature and rigidity of odd-dimensional complex hyperbolic spaces, Math. Annalen, vol. 312 (1998), 641-657.
[HS] A. D. Hwang, M. A. Singer A momentum construction for circle-invariant Kähler metrics, Trans. Amer. Math. Soc. 354 (2002), no. 6, 2285-2325
[Kir] K.D. Kirchberg, Killing spinors on Kähler manifolds, Ann. Global Anal. Geom. 11 (1993), no. 2, 141-164.
[KN] S. Kobayashi, K. Nomizu, Foundations of differential geometry. Vol. II. Reprint of the 1969 original. Wiley Classics Library. New York, 1996.
[LM] H. Blaine Lawson, Jr, Marie-Louise Michelsohn, Spin geometry, Princeton Mathematical Series, 38. Princeton University Press, Princeton, NJ, 1989.
[LP] J. M. Lee, T. H. Parker, The Yamabe problem, Bull Amer. Math. Soc. New. Series 17, (37-91) 1987.
[Loh] J. Lohkamp, The Higher Dimensional Positive Mass Theorem I, arXiv:math/0608795v1.
[Min] V. Minerbe, A mass for ALF manifolds, to appear in Comm. Math. Phys.
[MO] M. Min-Oo, Scalar curvature rigidity of asymptotically hyperbolic spin manifolds, Math. Ann., 285 (1989), 527-539.
[Mor] A. Moroianu, La première valeur propre de l'opérateur de Dirac sur les variétés kählériennes compactes, Comm. Math. Phys. 169 (1995), no. 2, 373-384.
[Oba] M. Obata, Riemannian manifolds admitting a solution of a certain system of differential equations, 1966 Proc. U.S.-Japan Seminar in Differential Geometry (Kyoto, 1965) pp. 101-114 Nippon Hyoronsha, Tokyo.
[SY1] R. Schoen, S. T. Yau, On the proof of the positive mass conjecture in general relativity, Comm. Math. Phys. 65 (1979), no. 1, 45-76.
[SY2] R. Schoen, S. T. Yau, Proof of the positive mass theorem. II, Comm. Math. Phys. 79 (1981), no. 2, 231-260.
[ST] Y. Shi, L.-F. Tam, Positive mass theorem and the boundary behaviors of compact manifolds with nonnegative scalar curvature, J. Differential Geom. 62 (2002), no. 1, 79-125.
[Wit] E. Witten, A new proof of the positive energy theorem, Comm. Math. Phys. 80 (1981), no. 3, 381-402.
E-mail address: daniel.maerten@yahoo.fr, minerbe@math.jussieu.fr
Université Paris 6, Institut de Mathématiques de Jussieu, UMR CNRS 7586, 175 rue du Chevaleret, 75013 Paris, France.

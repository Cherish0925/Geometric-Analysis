---
retention_scope: session
part: 2
total_parts: 3
---

[Part 2/3 of: Harmonic maps from Kähler manifolds]

Let us explain Sampson's formula. (The reader may also refer to [Xin96, Eq. (4.35)] for a similar exposition.) First recall that the divergence of a tensor field $T \in \Gamma\left(\mathrm{~T}^{*} M \otimes \ldots\right)$ is given by
$$\operatorname{div} T=\operatorname{tr} \nabla T=\sum_{j=1}^{m}\left(\nabla_{e_{j}} T\right)\left(e_{j}, \ldots\right)$$
where $\left(e_{j}\right)_{1 \leqslant j \leqslant m}$ is any local orthonormal frame field. This definition makes sense for $T \in \Gamma\left(\mathrm{~T}^{*} M \otimes E\right)$ where $E$ is any vector bundle with a connection: take the tensor product connection in (16).
Remark 4.9. Seeing $T$ as a 1-form with values in $E$, (8) shows that $\mathrm{d}_{\nabla}^{*} T=-\operatorname{div}(T)$.
Let $f:\left(M, g_{M}\right) \rightarrow\left(N, g_{N}\right)$ be a smooth map between Riemannian manifolds. Define the first fundamental form $\theta:=f^{*} g_{N}$. Note that by definition, $\|\mathrm{d} f\|^{2}=\operatorname{tr} \theta$. Take the divergence of $\theta$ :
$$\operatorname{div}(\theta)=\langle\Delta f, \mathrm{~d} f(\cdot)\rangle+\sum_{j=1}^{m}\left\langle\mathrm{~d} f\left(e_{j}\right),\left(\nabla_{e_{j}} \mathrm{~d} f\right)(\cdot)\right\rangle .$$
This is an element of $\Gamma\left(\mathrm{T}^{*} M\right)$. Take the divergence again and use the Weitzenböck formula:
$$\begin{aligned}
\operatorname{div}^{2}(\theta) & =2\langle\nabla \Delta f, \nabla f\rangle+\|\Delta f\|^{2}+\left\|\nabla^{2} f\right\|^{2} \\
& +\operatorname{Ric}^{M}\left(\langle\nabla f, \nabla f\rangle_{N}\right)-R^{N}\left(\langle\nabla f \wedge \nabla f\rangle_{M},\langle\nabla f \wedge \nabla f\rangle_{M}\right) .
\end{aligned}$$
This is merely a rewriting of the Bochner formula (14), since $\operatorname{div} \theta-\frac{1}{2} \mathrm{~d}\|\mathrm{~d} f\|^{2}=\langle\mathrm{d} f, \nabla \Delta f\rangle$.
Sampson's computation is based on the observation that when $(M, J)$ is a complex manifold, given a bilinear form $B \in \Gamma\left(\mathrm{~T}^{*} M \otimes \mathrm{~T}^{*} M \otimes \ldots\right)$, as an alternative to the trace $\operatorname{tr} B$, one can define $\operatorname{tr}^{c}(B):=$ $\sum_{i=1}^{M} B\left(\overline{\varepsilon_{j}}, \varepsilon_{j}\right)$ where $\varepsilon_{j}=e_{j}{ }^{1,0}$. It is immediate to check that $\operatorname{tr}^{c} B=\frac{1}{4}\left[\operatorname{tr} B+i \operatorname{tr}\left(B(J \cdot, \cdot)^{1,1}\right)\right]$ and that if $B$ is symmetric then $\operatorname{tr}^{c}(B)=\frac{1}{4} \operatorname{tr} B$. In particular one can define $\operatorname{div}^{c}(T)=\operatorname{tr}^{c}(\nabla T)$.

Reproducing the calculations leading to (17) by computing $\left(\operatorname{div}^{c}\right)^{2}(\theta)$ instead of $\operatorname{div}^{2}(\theta)$, one finds:
$$\operatorname{div}^{c} \theta=\left\langle\operatorname{tr}^{c}\left(\nabla^{2} f\right), \mathrm{d} f(\cdot)\right\rangle+\left\langle\operatorname{d} f\left(\varepsilon_{l}\right),\left(\nabla_{\bar{\varepsilon}_{l}} \mathrm{~d} f\right)(\cdot)\right\rangle .$$
Be advised that in (18) we omit the summation symbol over the repeated index $l$; we maintain this convention in the remainder of this section. Since $\nabla \mathrm{d} f$ is symmetric (Proposition 1.4), $\operatorname{tr}^{c}\left(\nabla^{2} f\right)=$ $\frac{1}{4} \operatorname{tr}\left(\nabla^{2} f\right)=\frac{1}{4} \Delta f$. In particular, if $f$ is harmonic, (18) reduces to
$$\operatorname{div}^{c} \theta=\left\langle\mathrm{d} f\left(\varepsilon_{l}\right),\left(\nabla_{\bar{\varepsilon}_{l}} \mathrm{~d} f\right)(\cdot)\right\rangle .$$
Taking div ${ }^{c}$ again and using the Weitzenböck formula (12), one finds:
$$\begin{aligned}
\left(\operatorname{div}^{c}\right)^{2} \theta= & \left\langle\nabla_{\overline{\varepsilon_{j}}} \mathrm{~d} f\left(\varepsilon_{l}\right), \nabla_{\overline{\varepsilon_{l}}} \mathrm{~d} f\left(\varepsilon_{j}\right)\right\rangle+\left\langle\mathrm{d} f\left(R^{M}\left(\overline{\varepsilon_{j}}, \overline{\varepsilon_{l}}\right) \varepsilon_{j}\right), \mathrm{d} f\left(\varepsilon_{l}\right)\right\rangle \\
& -R^{N}\left(\mathrm{~d} f\left(\overline{\varepsilon_{j}}\right), \mathrm{d} f\left(\overline{\varepsilon_{l}}\right), \mathrm{d} f\left(\varepsilon_{j}\right), \mathrm{d} f\left(\varepsilon_{l}\right)\right) .
\end{aligned}$$
If $M$ is Kähler, then the curvature term $\left\langle\mathrm{d} f\left(R^{M}\left(\overline{\varepsilon_{j}}, \bar{\varepsilon}_{l}\right) \varepsilon_{j}\right), \mathrm{d} f\left(\varepsilon_{l}\right)\right\rangle$ vanishes. Indeed, this term is real (unchanged by complex conjugation by symmetry of the Riemann curvature tensor) and the Ricci curvature tensor of $M$ is of type $(1,1)$ (Proposition 3.6). Sampson's Bochner formula follows:

Proposition 4.10 (Sampson's Bochner formula for harmonic maps). Let $f: M \rightarrow N$ be a smooth harmonic map where $M$ is a Kähler manifold and $N$ is a Riemannian manifold. Then
$$\left(\operatorname{div}^{c}\right)^{2} \theta=\left\langle\nabla_{\overline{\varepsilon_{j}}} \mathrm{~d} f\left(\varepsilon_{l}\right), \nabla_{\overline{\varepsilon_{l}}} \mathrm{~d} f\left(\varepsilon_{j}\right)\right\rangle-R^{N}\left(\mathrm{~d} f\left(\bar{\varepsilon}_{j}\right), \mathrm{d} f\left(\bar{\varepsilon}_{l}\right), \mathrm{d} f\left(\varepsilon_{j}\right), \mathrm{d} f\left(\varepsilon_{l}\right)\right) .$$

It is remarkable that this Bochner formula does not involve the curvature of $M$.

Remark 4.11. It is easy to generalize Sampson's Bochner formula to any smooth map without the harmonicity condition by keeping track of the extra terms:
$$\begin{aligned}
\left(\operatorname{div}^{c}\right)^{2} \theta= & 2\left\langle\nabla_{\overline{\varepsilon_{j}}}\left(\nabla_{\overline{\varepsilon_{l}}} \mathrm{~d} f\left(\varepsilon_{l}\right)\right), \mathrm{d} f\left(\varepsilon_{j}\right)\right\rangle+\left\langle\nabla_{\overline{\varepsilon_{l}}} \mathrm{~d} f\left(\varepsilon_{l}\right), \nabla_{\overline{\varepsilon_{j}}} \mathrm{~d} f\left(\varepsilon_{j}\right)\right\rangle \\
& +\left\langle\nabla_{\overline{\varepsilon_{j}}} \mathrm{~d} f\left(\varepsilon_{l}\right), \nabla_{\overline{\varepsilon_{l}}} \mathrm{~d} f\left(\varepsilon_{j}\right)\right\rangle-R^{N}\left(\mathrm{~d} f\left(\overline{\varepsilon_{j}}\right), \mathrm{d} f\left(\overline{\varepsilon_{l}}\right), \mathrm{d} f\left(\varepsilon_{j}\right), \mathrm{d} f\left(\varepsilon_{l}\right)\right) .
\end{aligned}$$

Ohnita-Valli [OV90] give a neat variant of Sampson's Bochner formula (20), although they do not give any details for the proof. Define the energy form of $f: M \rightarrow N$ by $\varepsilon(f):=\left(f^{*} g_{N}(J \cdot, \cdot)\right)^{(1,1)}$. This is a finer version of the energy density of $f$ : the two are related by $e(f) \operatorname{vol}_{M}=\varepsilon(f) \wedge \frac{\omega^{n-1}}{(n-1)!}$.
Proposition 4.12 ([OV90, Eq. (1.3)]). Let $f: M \rightarrow N$ be a smooth map where $M$ is a Kähler manifold of complex dimension $n$ and $N$ is a Remannian manifold. Then
$$\begin{aligned}
i \partial \bar{\partial} \varepsilon(f) \wedge \frac{\omega^{n-2}}{(n-2)!}= & {\left[\left\|\nabla^{0,1} \mathrm{~d}^{1,0} f\right\|^{2}-\left\|\operatorname{tr}\left(\nabla^{0,1} \mathrm{~d}^{1,0} f\right)\right\|^{2}\right.} \\
& \left.-R^{N}\left(\mathrm{~d} f\left(\varepsilon_{j}\right), \mathrm{d} f\left(\varepsilon_{l}\right), \mathrm{d} f\left(\overline{\varepsilon_{j}}\right), \mathrm{d} f\left(\overline{\varepsilon_{l}}\right)\right)\right] \operatorname{vol}_{M} .
\end{aligned}$$

\subsection*{4.3 Proof of the Siu-Sampson theorem}

\subsection*{4.3.1 Using Sampson's Bochner formula}

Just like Eells-Sampson's rigidity Theorem 2.3, the Siu-Sampson Theorem 4.1 is simply obtained by integrating the Bochner formula over $M$, arguing that the left-hand side has zero integral, and that all terms on the right-hand side are pointwise $\geqslant 0$ and hence must vanish everywhere.

However Sampson [Sam86] (also [CT89] and [Xin96, Eq. (4.35)]) concludes perhaps too quickly from the Bochner formula (19): it is not clear (to me!) that $\left(\operatorname{div}^{c}\right)^{2} \theta$ is co-closed, or even real.

That being said, Theorem 4.1 does follow immediately from the Ohnita-Valli version of the Bochner formula (21). Indeed, observe that:
\begin{itemize}
\item[-] It is always the case that $i \partial \bar{\partial}=\frac{1}{2} \mathrm{dd}^{\mathrm{c}}$ on $\mathbb{C}$-valued differential forms. In particular, $i \partial \bar{\partial} \varepsilon(f)$ is closed, and so is $i \partial \bar{\partial} \varepsilon(f) \wedge \frac{\omega^{n-2}}{(n-2)!}$ since $\mathrm{d} \omega=0$ (i.e. $M$ is Kähler).
\item[-] Recall that $\mathrm{d}_{\nabla} \mathrm{d}^{\mathrm{c}} f=2 i \bar{\partial}_{\nabla} \mathrm{d}^{1,0} f$, in particular $\left\|\nabla^{0,1} \mathrm{~d}^{1,0} f\right\|^{2}=0$ if and only if $f$ is pluriharmonic.
\item[-] Since $\nabla^{2} f$ is symmetric, $\operatorname{tr}\left(\nabla^{0,1} \mathrm{~d}^{1,0} f\right)=\operatorname{tr}^{c}\left(\nabla^{2} f\right)=\frac{1}{4} \operatorname{tr}\left(\nabla^{2} f\right)=\frac{1}{4} \Delta f$. Therefore we have $\left\|\operatorname{tr}\left(\nabla^{0,1} \mathrm{~d}^{1,0} f\right)\right\|^{2}=0$ if and only if $f$ is harmonic.
\end{itemize}

\subsection*{4.3.2 Toledo's proof}

An elegant alternative proof was written by D. Toledo in Chapter 6 of [Amo+96]. Let us briefly explain this argument which does not require a Bochner formula beforehand.

Proof of Theorem 4.1. First assume that $N=\mathbb{R}$. Let $M$ be a Kähler manifold and let $f: M \rightarrow \mathbb{R}$ be harmonic, i.e. $\mathrm{d}^{\mathrm{c}} f \wedge \omega^{n-1}=0$ by Proposition 3.7. We want to show that $f$ is pluriharmonic i.e. $\mathrm{dd}^{\mathrm{c}} f=0$ (Proposition 3.11). Consider the form $\eta \in \Omega^{2 n}(M, \mathbb{R})$ where $n=\operatorname{dim}_{\mathbb{C}} M$ defined by
$$\eta=\mathrm{dd}^{\mathrm{c}} f \wedge \mathrm{dd}^{\mathrm{c}} f \wedge \omega^{n-2} .$$
By the linear algebra Lemma 4.14 whose proof we postpone, $\eta$ is pointwise $\leqslant 0$ with equality if and only if $\mathrm{dd}^{\mathrm{c}} f=0$. On the other hand $\mathrm{d} \eta=0$ since $\eta=\mathrm{d}\left(\mathrm{d}^{\mathrm{c}} f \wedge \mathrm{dd}^{\mathrm{c}} f \wedge \omega^{n-2}\right)$ (recall that $\mathrm{d} \omega=0$ since $M$ is Kähler), so $\int_{M} \eta=0$ by Stokes. We conclude that $\eta$ must vanish everywhere, and so must $\mathrm{dd}^{\mathrm{c}} f$.

For the general case, define $\eta \in \Omega^{2 n}(M, \mathbb{R})$ by
$$\begin{aligned}
\eta & =\mathrm{d}\left(\left\langle\mathrm{~d}_{\nabla} \mathrm{d}^{\mathrm{c}} f \wedge \mathrm{~d}^{\mathrm{c}} f\right\rangle \wedge \omega^{n-2}\right) \\
& =\left\langle\mathrm{d}_{\nabla}^{2} \mathrm{~d}^{\mathrm{c}} f \wedge \mathrm{~d}^{\mathrm{c}} f\right\rangle \wedge \omega^{n-2}+\left\langle\mathrm{d}_{\nabla} \mathrm{d}^{\mathrm{c}} f \wedge \mathrm{~d}_{\nabla} \mathrm{d}^{\mathrm{c}} f\right\rangle \wedge \omega^{n-2} .
\end{aligned}$$

By definition $\eta$ is exact, so $\int_{M} \eta=0$. A straightforward extension of the linear algebra Lemma 4.14 shows that the term $\left\langle\mathrm{d}_{\nabla} \mathrm{d}^{\mathrm{c}} f \wedge \mathrm{~d}_{\nabla} \mathrm{d}^{\mathrm{c}} f\right\rangle \wedge \omega^{n-2}$ is pointwise $\leqslant 0$, with equality if and only if $\mathrm{d}_{\nabla} \mathrm{d}^{c} f=0$.

It remains to discuss the curvature term $\left\langle\mathrm{d}_{\nabla}^{2} \mathrm{~d}^{\mathrm{c}} f \wedge \mathrm{~d}^{\mathrm{c}} f\right\rangle \wedge \omega^{n-2}$. Let us skip some details and cite Toledo [Tol99]: When rewritten using the definition of curvature $\mathrm{d}_{\nabla}^{2}=-R$, this term turns out to be the average value of $R^{N}(\mathrm{~d} f(X), \mathrm{d} f(Y), \mathrm{d} f(\bar{X}), \mathrm{d} f(\bar{Y}))$ over all unit length decomposable vectors $X \wedge Y \in \otimes^{2} \mathrm{~T}^{1,0} M$. This computation can be found in [Amo+96] or in equivalent forms in [Siu80; Sam86]. \(\square\)

Remark 4.13. I find that even in the detailed computation of [Amo+96], important arguments are overlooked: when Toledo writes $\mathrm{d}_{\nabla}^{2}=-R$, the curvature tensor $R$ should not just be the Riemann curvature tensor of $N$, but also involve the curvature of $M$. As explained in § 4.1, the fact that $R^{M}$ ends up not playing a role is a little miracle due to the fact that the Ricci tensor of a Kähler manifold is $(1,1)$.

To complete the proof we need the following linear algebra lemma, which can be seen as a special case of the Hodge-Riemann bilinear relations, a well-known result in Kähler geometry that leads to the Hodge index theorem (see e.g. [Voi08]).
Lemma 4.14. Let $(V, g, J, \omega)$ be a Hermitian vector space of complex dimension $n$. If $\alpha \in \Lambda^{1,1} V^{*}$ is a (1, 1)-form such that $\alpha \wedge \omega^{n-1}=0$, then $\alpha \wedge \alpha \wedge \omega^{n-2} \leqslant 0$, with equality if and only if $\alpha=0$.

For entertainment, we give a neat proof (mostly taken from [Amo+96]) of this not-so-easy lemma.
Proof. Define the Hermitian metric $h:=g-i \omega$, the space of complex endomorphisms $\operatorname{End}_{\mathbb{C}}(V):=\{f \in$ $\left.\operatorname{End}_{\mathbb{R}}(V) \mid f J=J f\right\}$, the space of self-adjoint endomorphisms $\mathcal{H}(V):=\left\{f \in \operatorname{End}_{\mathbb{C}}(V) \mid h(f(x), y)=\right.$ $h(x, f(y))\}$, and the unitary group $\mathrm{U}(V):=\left\{u \in \operatorname{End}_{\mathbb{C}}(V) \mid h(u(x), u(y))=h(x, y)\right\}$.

An element $\alpha \in \Lambda^{1,1} V^{*}$ is a skew-symmetric bilinear form such that $\alpha(J x, J y)=\alpha(x, y)$. Let
$$\begin{aligned}
\mathcal{H}(V) & \rightarrow \Lambda^{1,1} V^{*} \\
f & \mapsto \omega_{f}
\end{aligned}$$
where $\omega_{f}(x, y):=\omega(f x, y)$. This isomorphism is moreover $\mathrm{U}(V)$-equivariant for the natural action of $\mathrm{U}(V)$ on $\mathcal{H}(V)$ by conjugation and on $\Lambda^{1,1} V^{*}$ by pullback: $(u \cdot \alpha)(x, y):=\alpha(u x, u y)$.

We claim that the decomposition of $\mathcal{H}(V)$ as a sum of irreducible $\mathrm{U}(V)$-modules is $\mathcal{H}=\mathbb{R} i d+\mathcal{H}^{0}$, where $\mathcal{H}^{0}$ is the space of traceless self-adjoint endomorphisms. Indeed, consider the Cartan decomposition $\mathfrak{s} \mathfrak{l}(V)=\mathfrak{s} \mathfrak{u}(h) \oplus \mathfrak{p}$, where $\mathfrak{s} \mathfrak{u}(V)$ is the Lie algebra of $\operatorname{SU}(V)$ and $\mathfrak{p}=\mathcal{H}^{0}$. If there existed a nonzero proper $\mathrm{U}(h)$-invariant subspace $\mathfrak{m} \subseteq \mathfrak{p}$, then $\mathfrak{u}+\mathfrak{m}$ would be a nonzero proper ideal of the Lie algebra $\mathfrak{s} \mathfrak{u}(V)$, contradicting its well-known simplicity.

Via the $\mathrm{U}(h)$-equivariant isomorphism (23), we get a decomposition of $\Lambda^{1,1} V^{*}$ into irreducible $\mathrm{U}(h)$ -modules as $\Lambda^{1,1} V^{*}=\mathbb{R} \omega \oplus \Lambda_{0}^{1,1} V^{*}$ where $\alpha \in \Lambda_{0}^{1,1} V^{*}$ if and only if $\alpha \wedge \omega^{n-1}=0$.

To conclude, consider the inner product
$$\begin{aligned}
\Lambda^{1,1} V^{*} \times \Lambda^{1,1} V^{*} & \rightarrow \Lambda^{2 n} V^{*} \approx \mathbb{R} \\
(\alpha, \beta) & \mapsto \alpha \wedge \beta \wedge \omega^{n-2} .
\end{aligned}$$
This inner product is $\mathrm{U}(V)$-invariant, therefore in restriction to the irreducible subspace $\Lambda_{0}^{1,1} V^{*}$ it must be either positive definite or negative definite or identically zero. Compute any example to conclude. \(\square\)

Remark 4.15. Toledo's proof is very closely related to the Ohnita-Valli version of Sampson's Bochner formula (21). Indeed, it is easy to check that $\varepsilon(f)=-\frac{1}{2}\left\langle\mathrm{~d} f \wedge \mathrm{~d}^{\mathrm{c}} f\right\rangle$ and derive that $\eta=-4 i \partial \bar{\partial} \varepsilon(f) \wedge \omega^{n-2}$. One can therefore equate Toledo's identity (22) with the Ohnita-Valli formula (21) as long as one can equate the curvature terms, which is done in [Amo+96], and upgrade Lemma 4.14: the inner product (24) is actually given explicitly by
$$\alpha \wedge \alpha \wedge \frac{\omega^{n-2}}{(n-2)!}=(\operatorname{tr} \alpha)^{2}-\|\alpha\|^{2} .$$
This identity can be proved by brute force: take an orthonormal basis $\left(e_{1}, J e_{1}, \ldots\right)$ of $V$, etc.

\subsection*{4.4 First applications to rigidity}

This first straightforward consequence of Theorem 4.1 is due to Sampson [Sam86]:
Theorem 4.16. Let $f: M \rightarrow N$ where $M$ is compact Kähler and $N$ has constant negative sectional curvature. If $f$ is harmonic, then the rank of $f$ is everywhere $\leqslant 2$.

Proof. If $N$ has constant curvature $k$, then $R^{N}(X, Y, \bar{X}, \bar{Y})=k\|X \wedge Y\|^{2}$ for all $X, Y \in \mathrm{~T}_{\mathbb{C}} N$. By Theorem 4.1, $\mathrm{d} f\left(X^{1,0}\right)$ and $\mathrm{d} f\left(Y^{1,0}\right)$ must be collinear for any $X, Y \in \mathrm{~T} M$. This implies rank $(f) \leqslant 2$. \(\square\)

Remark 4.17. Combining with the existence theorem of Eells-Sampson (Theorem 2.4), we obtain topological restrictions on maps $f: M \rightarrow N$ from a compact Kähler manifold to a compact hyperbolic manifold, such as: $f_{*}: H_{k}(M, \mathbb{Z}) \rightarrow H_{k}(N, \mathbb{Z})$ is zero if $k>2$.

We shall recover Theorem 4.16 with a more algebraic proof in § 5.3. Next, we prove the strong rigidity theorem of Siu for strongly negatively curved Kähler manifolds:

Theorem 4.18. Let $M$ and $N$ be compact Kähler manifolds, with $N$ strongly negatively curved. Any harmonic map $M \rightarrow N$ is ±-holomorphic unless it has rank $\leqslant 2$ everywhere.

Corollary 4.19. Let $N$ be a compact Kähler manifold of complex dimension $\geqslant 2$ with strongly negative curvature. Any compact Kähler manifold homotopy equivalent to N must be either ±-biholomorphic to N.

Proof of Theorem 4.18 and Corollary 4.19. If $f$ is not ±-holomorphic at $x$, there exist $X_{1}, X_{2} \in \mathrm{~T}_{x}^{1,0} M$ such that $\mathrm{d} f\left(X_{1}\right)$ is not of type $(1,0)$ and $\mathrm{d} f\left(X_{2}\right)$ is not of type $(0,1)$. One can then find $X_{0} \in \mathrm{~T}_{x}^{1,0} M$ such that $\mathrm{d} f\left(X_{0}\right)$ is of mixed type (either $X_{0}=X_{1}+X_{2}$ or $X_{0}=X_{2}$ works). Given any $Y \in \mathrm{~T}_{x}^{1,0} M$, consider $\sigma:=\mathrm{d} f\left(X_{0}\right)^{1,0} \otimes \mathrm{~d} f(Y)^{0,1}-\mathrm{d} f(Y)^{1,0} \otimes \mathrm{~d} f\left(X_{0}\right)^{0,1}$. If $f$ is harmonic, then by Theorem 4.1 $R\left(\mathrm{~d} f\left(X_{0}\right), \mathrm{d} f(Y), \overline{\mathrm{d} f\left(X_{0}\right)}, \overline{\mathrm{d} f(Y)}\right)=Q(\sigma, \bar{\sigma})=0$. By strongly negative curvature of $N$, it follows $\sigma=0$. This implies that $\mathrm{d} f(Y)$ and $\mathrm{d} f\left(X_{0}\right)$ are collinear over $\mathbb{C}$, and since this is true for all $Y$, the rank of $f$ at $x$ is $\leqslant 2$. If $f$ is not holomorphic (resp. antiholomorphic) on $M$, the set $U$ (resp. $V$ ) where $\mathrm{d} f(\cdot)^{0,1} \neq 0$ (resp. $\left.\mathrm{d} f(\cdot)^{1,0} \neq 0\right)$ is open dense. Thus $f$ has rank $\leqslant 2$ on the open dense set $U \cap V$, and hence everywhere.

For Corollary 4.19, let $f: M \rightarrow N$ be a homotopy equivalence. By Theorem 2.4 we may assume $f$ is harmonic. Since $M$ and $N$ are closed, they must have same dimension and $f$ has degree 1 . In particular $f$ is surjective and has full rank $n \geqslant 4$ somewhere. By Theorem 4.18, $f$ is ±-holomorphic. If $f$ is not injective, then it must send a subvariety $Z \subseteq M$ of positive dimension to a point. This is not possible because the fundamental class of $Z$ is a nontrivial cohomology class of $M$ (the integral of a power of the Kähler form on $Z$ is the volume of $Z$, hence positive) and $f$ induces an isomorphism on cohomology. \(\square\)

Remark 4.20. Corollary 4.19 says that N is strongly rigid as a Kähler manifold. This echoes the celebrated rigidity theorem of Mostow; this will be discussed in § 5.4.

Remark 4.21. We refer to [EL95a] and [OU90] for further rigidity results concerning complex manifolds via the harmonic maps approach.

\section*{5 Applications to symmetric spaces}

We now apply the theorem of Siu and Sampson to the situation where the target Riemannian manifold is locally symmetric. We derive in particular a second version of Siu's strong rigidity theorem, and explain its relation to Mostow rigidity.
Remark 5.1. This section, especially § 5.2 and § 5.3, is largely based on Chapter 6 (mostly written by D. Toledo) of the excellent book [Amo+96] of Amorós, Burger, Corlette, Kotschick, and Toledo.

\subsection*{5.1 Symmetric spaces of noncompact type}

Let $\mathrm{X}=G / K$ be a symmetric space of noncompact type: $G$ is a semisimple Lie group without compact factors and $K$ is a maximal compact subgroup ${ }^{6}$. Denote by $\mathfrak{g}$ and $\mathfrak{k}$ the Lie algebras of $G$ and $K$ respectively, and denote $B$ the Killing form on $\mathfrak{g}$. Recall that $B$ is an $\operatorname{Ad} G$-invariant symmetric bilinear form on $\mathfrak{g}$, and it is nondegenerate because $\mathfrak{g}$ is semisimple. We have the Cartan decomposition
$$\mathfrak{g}=\mathfrak{k} \oplus \mathfrak{p}$$
where $\mathfrak{p}$ is the $B$-orthogonal of $\mathfrak{k}$. This decomposition satisfies $[\mathfrak{k}, \mathfrak{k}] \subseteq \mathfrak{k},[\mathfrak{k}, \mathfrak{p}] \subseteq \mathfrak{p}$, and $[\mathfrak{p}, \mathfrak{p}] \subseteq \mathfrak{k}$. Moreover $B$ is positive definite on $\mathfrak{p}$ and negative definite on $\mathfrak{k}$. Thus $B$ induces an inner product on $\mathrm{T}_{p} \mathrm{X} \approx p$ for any $p \in \mathrm{X}$; this globally defines a $G$-invariant Riemannian metric on X.

The curvature tensors (see § 2.3) on X have nice expressions:
Proposition 5.2. Let $o=e K \in \mathrm{X}=G / K$. For all $X, Y, Z, W \in \mathrm{~T}_{o} \mathrm{X} \approx \mathfrak{p}$, we have:
\begin{itemize}
\item[-] Riemann curvature tensor: $R(X, Y) Z=-[[X, Y], Z]$
\item[-] purely covariant Riemann tensor: $R(X, Y, Z, W)=-B[[X, Y],[Z, W]]$
\item[-] curvature operator: $Q(X \otimes Y, X \otimes Y)=-B[[X, Y],[X, Y]]$
\end{itemize}

Proof. Since $G$ is the group of isometries of $\mathbf{X}, \mathfrak{g}$ can be identified to the space of Killing vector fields. We indicate by $\bar{X}$ the Killing field associated to $X \in \mathfrak{g}$. One easily checks that $[\bar{X}, \bar{Y}]=-\overline{[X, Y]}$, where the Lie bracket is that of vector fields on the left-hand side. Let $o=e K \in \mathrm{X}$. A quick computation shows that the Levi-Civita connection of X at $o$ is given by $\left(\nabla_{X} T\right)_{o}=[\bar{X}, T]_{o}$. Note that Killing fields vanishing at $o$ correspond to the Lie subalgebra $\mathfrak{k} \subseteq \mathfrak{g}$, while Killing fields $\bar{X}$ such that $(\nabla \bar{X})_{o}=0$ correspond to $X \in \mathfrak{p} \subseteq \mathfrak{g}$ (called infinitesimal transvections).

Since $R$ is tensorial, we have, at $o$ :
$$R(X, Y) Z=R(\bar{X}, \bar{Y}) \bar{Z}=\nabla_{\bar{X}} \nabla_{\bar{Y}} \bar{Z}-\nabla_{\bar{Y}} \nabla_{\bar{X}} \bar{Z}-\nabla_{[\bar{X}, \bar{Y}]} \bar{Z} .$$
The last term is zero because $[\bar{X}, \bar{Y}]=-\overline{[X, Y]}=0$ at $o$ since $[X, Y] \in \mathfrak{k}$. The first term is rewritten $\nabla_{\bar{X}} \nabla_{\bar{Y}} \bar{Z}=\left[\bar{X}, \nabla_{\bar{Y}} \bar{Z}\right]=\nabla_{[\bar{X}, \bar{Y}]} \bar{Z}+\nabla_{\bar{Y}}[\bar{X}, \bar{Z}]$-by some sort of Leibniz rule for the Lie derivative along a Killing field. Again the first term vanishes, so $\nabla_{\bar{X}} \nabla_{\bar{Y}} \bar{Z}=\nabla_{\bar{Y}}[\bar{X}, \bar{Z}]=[\bar{Y},[\bar{X}, \bar{Z}]]$. We thus find
$$\begin{aligned}
R(X, Y) Z & =[\bar{Y},[\bar{X}, \bar{Z}]]-[\bar{X},[\bar{Y}, \bar{Z}]] \\
& =[\bar{Z},[\bar{X}, \bar{Y}]]
\end{aligned}$$
by the Jacobi identity. Conclude that $R(X, Y) Z=[Z,[X, Y]]$ using the property $[\bar{U}, \bar{V}]=-\overline{[U, V]}$. The expression of the purely covariant Riemann tensor and the curvature operator quickly follows. \(\square\)

Remark 5.3. The proof above is taken from [Pec17]. The reader will find alternative proofs in classical textbooks such as [KN96; Hel01; Pau20].

Remark 5.4. The fact that $\mathrm{X}=G / K$ is a Riemannian symmetric space, i.e. there exists a central symmetry about every point, easily implies that $\nabla R=0$. Conversely, any Riemannian manifold whose curvature tensor is parallel is locally isometric to a symmetric space $G / K$ (not necessarily of noncompact type).

A seemingly innocuous consequence of Proposition 5.2 is that the complexified curvature operator is also given by $Q(X \otimes Y, X \otimes Y)=-B^{\mathbb{C}}[[X, Y],[X, Y]]$, where $B^{\mathbb{C}}$ denotes the complex linear extension of the Killing form to $\mathfrak{p}^{\mathbb{C}}:=\mathfrak{p} \otimes \mathbb{C}$. This not only implies that $Q(\sigma, \bar{\sigma}) \leqslant 0$ for all $\sigma \in \otimes^{2} \mathfrak{p}^{\mathbb{C}}$; furthermore we have $R(X, Y)=0$ if $Q(X \otimes Y, X \otimes Y)=0$ for any $X, Y \in \mathfrak{p}^{\mathbb{C}}$, which is exceptionally strong. Since $R$ is parallel, this must hold at any point of X, therefore we obtain:

\footnotetext{
${ }^{6} G$ is assumed connected by definition of semisimple, and without loss of generality we can assume it has trivial center.
}

Corollary 5.5. Let $\mathrm{X}=G / K$ be a symmetric space of noncompact type.
\begin{itemize}
\item[(i)] X has very strongly nonpositive curvature.
\item[(ii)] At any $p \in \mathrm{X}$, we have, for all $X, Y \in \mathrm{~T}_{p} \mathrm{X} \otimes \mathbb{C}$ : if $R(X, Y, X, Y)=0$ then $R(X, Y)=0$.
\end{itemize}

Remark 5.6. A Cartan subspace of $\mathfrak{g}=\mathfrak{k}+\mathfrak{p}$ is defined to be a maximal abelian subspace of $\mathfrak{p}$. All Cartan subspaces have the same dimension, called the rank of X. It follows from Corollary 5.5 that the rank of X is the maximal dimension of a flat subspace of its tangent space.
Example 5.7. Hyperbolic space $\mathrm{X}=\mathbb{H}^{n}$, where $G=\operatorname{SO}^{+}(n, 1)$ and $K=\operatorname{SO}(n) \times\{1\}$, is a symmetric space of noncompact type of rank 1. As is well-known, $\mathbb{H}^{n}$ is isotropic with constant sectional curvature -1. This confirms (i), and note that (ii) never arises unless $X$ and $Y$ are collinear.

Hermitian symmetric spaces are another important class of examples, especially for the applications of the Siu-Sampson theorem. $\mathrm{X}=G / K$ is called Hermitian symmetric is there exists a $G$-invariant, equivalently parallel, compatible complex structure $J$ (in particular X Kähler). One can show that $\mathrm{X}=G / K$ is Hermitian symmetric if and only if $K$ has nondiscrete center [Hel01, Chap. VIII, §6].

Remark 5.8. If $\mathrm{X}=G / K$ is irreducible, i.e. $G$ is simple, the complex structure $J$ is unique up to sign, and the center of $K$ is a copy of U(1). Otherwise, $J$ is determined up to sign on each irreducible factor.

Example 5.9. A bounded domain $\Omega \subseteq \mathbb{C}^{n}$ is called a bounded symmetric domain if for all $x \in \Omega$, there exists an involutive biholomorphism of $\Omega$ with $x$ as an isolated fixed point. On such a domain, one can define a Hermitian metric called the Bergman metric for which biholomorphisms of $\Omega$ are isometries. Letting $G$ denote the biholomorphism group of $\Omega$ and $K$ the stabilizer of a point, $\mathrm{X}=G / K \approx \Omega$ is a Hermitian symmetric space of noncompact type, whose Hermitian structure is given by the Bergman metric on $\Omega$. Conversely, the Harish-Chandra embedding exhibits every Hermitian symmetric space of noncompact type as a bounded symmetric domain [Hel01, Thm 7.1]. As a fundamental example, taking the unit ball in $\mathbb{C}^{n}$ for $\Omega$ yields the ball model of complex hyperbolic space $\mathbb{H}_{\mathbb{C}}^{n}$.

\subsection*{5.2 Abelian subalgebras of $\mathfrak{p}^{\mathbb{C}}$}

Let $\mathrm{X}=G / K$ be a symmetric space of noncompact type as in § 5.1. Recall that we have the Cartan decomposition $\mathfrak{g}=\mathfrak{k} \oplus \mathfrak{p}$. In preparation of § 5.3, let us investigate abelian complex subspaces $\mathfrak{a} \subseteq \mathfrak{p}^{\mathbb{C}}$, especially their dimension. Of course, we always have $\operatorname{dim}_{\mathbb{C}} \mathfrak{a} \leqslant \operatorname{dim}_{\mathbb{C}} \mathfrak{p}^{\mathbb{C}}=\operatorname{dim} \mathrm{X}$. Can a better upper bound be achieved? Taking $\mathfrak{a}=\mathfrak{a}_{0}^{\mathbb{C}}$ where $\mathfrak{a}_{0} \subseteq \mathfrak{p}$ is a Cartan subspace shows that one cannot hope for better than $\operatorname{dim}_{\mathbb{C}} \mathfrak{a} \leqslant \operatorname{rank}(\mathrm{X})$. First let us look at a simple example where this bound does hold:

Lemma 5.10. Let $\mathrm{X}=\mathbb{H}^{n}$. If $\mathfrak{a} \subseteq \mathfrak{p}^{\mathbb{C}}$ is abelian, then $\operatorname{dim}_{\mathbb{C}} \mathfrak{a} \leqslant 1$.
Proof. As an instructive exercise, let us write both an algebraic and a geometric proof. For the algebraic proof, let $\mathfrak{g}=\mathfrak{s o}(n, 1)$. Generally, elements of $\mathfrak{s o}(p, q)$ are matrices $M=\left[\begin{array}{cc}A & B \\ { }^{t} B & D\end{array}\right] \in \mathfrak{s l}(p+q, \mathbb{R})$ with ${ }^{t} A=-A$ and ${ }^{t} D=-D$. The Cartan decomposition $\mathfrak{g}=\mathfrak{k} \oplus \mathfrak{p}$ consists in writing $M=\left[\begin{array}{cc}A & 0 \\ 0 & D\end{array}\right]+\left[\begin{array}{cc}0 & B \\ { }^{t} B & 0\end{array}\right]$. Thus $\mathfrak{p}^{\mathbb{C}}$ consits of matrices of the form $\left[\begin{array}{cc}0 & B \\ t_{B} & 0\end{array}\right]$ where $B$ is a $p \times q$ matrix with complex coefficients. When $q=1$, two such matrices commute if and only if they are collinear, and the result follows.

Now the geometric proof. Since $\mathbb{H}^{n}$ has sectional curvature -1, its Riemann curvature tensor is given by $\langle R(X, Y) Z, W\rangle=\langle X, Z\rangle\langle Y, W\rangle-\langle Y, Z\rangle\langle X, W\rangle$. A neat way to interpret this identity is that $R(X, Y)$ is the skew-adjoint endomorphism of $\mathrm{T} \mathbf{X}$ associated to $X^{\mathrm{b}} \wedge Y^{\mathrm{b}} \in \Lambda^{2} \mathrm{~T}^{*} \mathbf{X}$, where $X^{\mathrm{b}} \in \mathrm{T}^{*} \mathrm{X}$ indicates the metric dual of $X \in \mathrm{~T} \mathbf{X}$. The identification $R(X, Y)=X^{\mathrm{b}} \wedge Y^{\mathrm{b}}$ extends to $\mathrm{T}_{\mathbb{C}} \mathbf{X}$. It follows that, for all $X, Y \in \mathrm{~T}_{\mathbb{C}} \mathbf{X}, R(X, Y)=0$ if and only if $X$ and $Y$ are collinear. The conclusion ensues. \(\square\)

In the example above, all elements of $\mathfrak{p}^{\mathbb{C}}$ are semisimple. One can show that if $\mathfrak{a}$ only has semisimple elements, it is conjugate to $\mathfrak{a}_{0}^{\mathbb{C}}$ for some abelian subspace $\mathfrak{a}_{0} \subseteq \mathfrak{p}$, therefore $\operatorname{dim}_{\mathbb{C}} \mathfrak{a} \leqslant \operatorname{rank}(\mathrm{X})$. However, in general, $\mathfrak{a}$ can contain nilpotent elements, and its dimension can be much higher.

Indeed, assume X is Hermitian symmetric. The linear complex structure $J$ in $\mathrm{T}_{o} \mathrm{X} \approx \mathfrak{p}$ yields a decomposition of $\mathfrak{p}^{\mathbb{C}}$ into $\pm i$-eigenspaces as $\mathfrak{p}^{\mathbb{C}}=\mathfrak{p}^{1,0} \oplus \mathfrak{p}^{0,1}$. Since $J$ is integrable, we must have ${ }^{7}$ $\left[\mathfrak{p}^{1,0}, \mathfrak{p}^{1,0}\right] \subseteq \mathfrak{p}^{1,0}$. On the other hand, $[\mathfrak{p}, \mathfrak{p}] \subseteq \mathfrak{k}$ implies that $\left[\mathfrak{p}^{\mathbb{C}}, \mathfrak{p}^{\mathbb{C}}\right] \subseteq \mathfrak{k}^{\mathbb{C}}$; therefore $\left[\mathfrak{p}^{1,0}, \mathfrak{p}^{1,0}\right]=0$. Thus, for Hermitian symmetric spaces, $\mathfrak{a}=\mathfrak{p}^{1,0}$ shows that $\operatorname{dim}_{\mathbb{C}} \mathfrak{a}=\frac{1}{2} \operatorname{dim} \mathrm{X}$ is possible.
Example 5.11. It is instructive to work out the example $\mathrm{X}=\mathrm{SU}(p, q) / \mathrm{S}(\mathrm{U}(p) \times \mathrm{U}(q))$, similarly to $\mathfrak{s} \mathfrak{o}(p, q)$ above. This is done in [Amo+96, Example 6.9].

The following result of Carlson-Toledo shows that the bound $\operatorname{dim}_{\mathbb{C}} \mathfrak{a} \leqslant \frac{1}{2} \operatorname{dim} \mathbf{X}$ holds for all symmetric spaces of noncompact type, and is only attained for Hermitian symmetric spaces:

Theorem 5.12 (Carlson-Toledo [CT89]). Let $\mathrm{X}=G / K$ be a symmetric space of noncompact type. If $\mathfrak{a} \subseteq \mathfrak{p}^{\mathbb{C}}$ is an abelian subalgebra, then $\operatorname{dim}_{\mathbb{C}} \mathfrak{a} \leqslant \frac{1}{2} \operatorname{dim} \mathrm{X}$. Moreover, if equality holds, X is Hermitian symmetric, and provided X has no $\mathbb{H}^{2}$ factor ${ }^{8}$ we have $\mathfrak{a}=\mathfrak{p}^{1,0}$ for some invariant complex structure on X.

Proof. We only sketch the proof and refer to [CT89] for details. By Lemma 5.10, the results holds for $\mathbb{H}^{2}$. If X has no $\mathbb{H}^{2}$ factor, a technical lemma ensures that if $\mathfrak{a}$ contains a nonzero semisimple element, then $\operatorname{dim}_{\mathbb{C}} \mathfrak{a}<\frac{1}{2} \operatorname{dim} \mathrm{X}$. Thus we may assume that $\mathfrak{a}$ has no semisimple elements. Since real elements are semisimple, we have $\mathfrak{a} \cap \overline{\mathfrak{a}}=0$, and if $\operatorname{dim}_{\mathbb{C}} \mathfrak{a}=\frac{1}{2} \operatorname{dim}_{\mathbb{C}} \mathfrak{p}^{\mathbb{C}}$ then $\mathfrak{p}^{\mathbb{C}}=\mathfrak{a} \oplus \overline{\mathfrak{a}}$. This means that $\mathfrak{a}=\mathfrak{p}^{1,0}$ for some linear complex structure on $\mathfrak{p}$. One readily shows that it is compatible with the Killing form and invariant, i.e. $[\mathfrak{k}, \mathfrak{a}] \subseteq \mathfrak{a}$. \(\square\)

\subsection*{5.3 Application of the Siu-Sampson theorem}

Let us go back to the setting of the theorem of Siu and Sampson: let $f: M \rightarrow N$ be a harmonic map where $M$ is compact Kähler and $N$ is Riemannian. We now specialize to the case where $N$ is locally symmetric of noncompact type, i.e. locally isometric to a symmetric space of noncompact type $\mathrm{X}=G / K$.
Remark 5.13. If $N$ is additionally assumed complete, its universal cover $\tilde{N}$ must be isometric to $\mathrm{X}=G / K$. In other words, $N=\Gamma \backslash \mathrm{X}$ where $\Gamma<G$ is a discrete subgroup acting freely and properly on X-it is enough that $\Gamma<G$ is discrete and torsion-free ${ }^{9}$. When $N$ is not assumed complete, we merely have a developing map $\tilde{N} \rightarrow \mathrm{X}$ which is a local isometry, but neither surjective nor a covering map in general ${ }^{10}$.

Since X , hence $N$, has very strongly nonpositive curvature (see Corollary 5.5), we may apply Theorem 4.1 and conclude that $f$ is pluriharmonic, and moreover $R^{N}(X, Y, \bar{X}, \bar{Y})=0$ for all $x \in M$ and $X, Y \in \mathrm{~d} f\left(\mathrm{~T}_{x}^{1,0} M\right)$. By Corollary 5.5 (ii), it follows that $R^{N}(X, Y)=0$.

For $x \in M$, denote $\mathfrak{a}_{x}:=\mathrm{d} f\left(\mathrm{~T}_{x}^{1,0} M\right) \subseteq \mathrm{T}_{f(x)} N \otimes \mathbb{C}$. Note that $\operatorname{rank}_{x}(f)=\operatorname{dim}_{\mathbb{R}} \mathrm{d} f\left(\mathrm{~T}_{x} M\right)=$ $\operatorname{dim}_{\mathbb{C}}\left(\mathfrak{a}_{x}+\overline{\mathfrak{a}}_{x}\right)$, therefore $\operatorname{rank}_{x}(f) \leqslant 2 \operatorname{dim}_{\mathbb{C}} \mathfrak{a}_{x}$. Identifying $\mathrm{T}_{f(x)} N \approx \mathfrak{p}$, we have $\mathfrak{a}_{x} \subseteq \mathfrak{p}^{\mathbb{C}}$, and the fact that $R^{N}(X, Y)=0$ for all $X, Y \in \mathrm{~d} f\left(\mathrm{~T}_{x}^{1,0} M\right)$ translates to $\left[\mathfrak{a}_{x}, \mathfrak{a}_{x}\right]=0$, i.e. $\mathfrak{a}_{x}$ is an abelian subalgebra of $\mathfrak{p}^{\mathbb{C}}$. Let us collect these findings:

Lemma 5.14. Let $f: M \rightarrow \mathrm{X}$ be a harmonic map, where $M$ is compact Kähler and $\mathrm{X}=G / K$ is (locally) symmetric of noncompact type. If $f$ is harmonic, then $f$ is pluriharmonic. Moreover, for all $x \in M$, $\mathfrak{a}_{x}:=\mathrm{d} f\left(\mathrm{~T}_{x}^{1,0} M\right)$ is an abelian subalgebra of $\mathfrak{p}^{\mathbb{C}}$.

\footnotetext{
${ }^{7}$ On an almost complex manifold (X, J), the involutivity of the distribution $\mathrm{T}^{1,0} \mathrm{X}$, i.e. its stability under the Lie bracket, is equivalent to the vanishing of the Nijenhuis tensor.
${ }^{8} \mathrm{X}$ has no $\mathbb{H}^{2}$ factor if it is not isometric to $\mathbb{H}^{2} \times \mathrm{X}_{1}$ where $\mathrm{X}_{1}$ is a symmetric space. Equivalently, $G$ has no $\operatorname{PSL}(2, \mathbb{R})$ factor.
${ }^{9}$ It is a general fact that any isometric action of a discrete group in a proper metric space is proper [Rat06, Thm. 5.3.5].
${ }^{10}$ This is the language of $(X, G)$-structures, refer to e.g. [Gol10] for more developments.
}

We can now reinvest the analysis of the dimension of such subalgebras performed in § 5.2. Let us start with the case where $N$ is locally isometric to $\mathrm{X}=\mathbb{H}^{n}$. Equivalently, $N$ has constant sectional curvature -1. We recover Theorem 4.16 as an immediate consequence of Lemma 5.10:

Theorem 5.15 (Sampson [Sam86]). Let $f: M \rightarrow N$ be a harmonic map where $M$ is compact Kähler and $N$ is hyperbolic. Then $\operatorname{rank}(f) \leqslant 2$ everywhere.

Remark 5.16. Theorem 5.15 was refined by Carlson-Toledo [CT89]: they proved that either $f$ maps to a closed geodesic, or factorizes as $f=\psi \circ \varphi$, where $\varphi: M \rightarrow C$ is a holomorphic map to a Riemann surface $C$ and $\psi: C \rightarrow N$ is harmonic.

Next, as a consequence of Theorem 5.12 we obtain:
Theorem 5.17. Let $f: M \rightarrow N$ be a harmonic map where $M$ is compact Kähler and $N$ is locally symmetric of noncompact type modelled on $\mathrm{X}=G / K$. If $\operatorname{rank}_{x}(f)=\operatorname{dim} N$ for some $x \in N$, then X is Hermitian symmetric. Moreover, if X has no $\mathbb{H}^{2}$ factor, $f$ is holomorphic for some invariant complex structure on X .

Proof. Let $\mathfrak{a}_{x}=\mathrm{d} f\left(\mathrm{~T}_{x}^{1,0} M\right)=\operatorname{Im}\left(\mathrm{d}_{x}^{1,0} f\right)$. By the previous discussion, if $f$ is harmonic then it is pluriharmonic and $\mathfrak{a}_{x}$ is abelian. Moreover, since $\operatorname{rank}_{x}(f) \leqslant 2 \operatorname{dim}_{\mathbb{C}} \mathfrak{a}_{x}$, if $\operatorname{rank}_{x}(f)=\operatorname{dim} N$ then $\operatorname{dim}_{\mathbb{C}} \mathfrak{a}_{x} \geqslant \frac{1}{2} \operatorname{dim} N$. In this case Theorem 5.12 says that X is Hermitian symmetric, and if it has no $\mathbb{H}^{2}$ factor then $\mathfrak{a}_{x}=\mathfrak{p}^{1,0}$ for some invariant complex structure on X. In other words, $f$ is holomorphic at $x$.

Let $U=\left\{x \in M: \operatorname{dim}_{\mathbb{C}} \mathfrak{a}_{x}=\frac{1}{2} \operatorname{dim} N\right\}$. By assumption, $U$ is nonempty. By Proposition 3.11, $\mathrm{d}^{1,0} f$ is a holomorphic section of $f^{*} \mathrm{~T} N \otimes \mathbb{C}$, which is a holomorphic vector bundle as we shall see in § 6.2. Therefore the complement of $U$, which consists of the points $x \in M$ where $\mathrm{d}^{1,0} f$ does not have maximal rank, is the vanishing locus of a holomorphic function, so it is a proper subvariety. In particular, $U$ is dense. We know that $f$ is holomorphic on $U$, i.e. $\bar{\partial} f$ vanishes on $U$, hence everywhere. \(\square\)

Remark 5.18. Theorem 5.17 can be refined by trading the assumption $\operatorname{rank}_{x}(f)=\operatorname{dim} N$ for $\operatorname{rank}_{x}(f)>$ $2 p(\mathbf{X})$, where $p(\mathbf{X})$ is the maximal dimension of a subalgebra of $\mathfrak{p}^{\mathbb{C}}$ not contained in $\mathfrak{p}^{1,0}$. Siu [Siu82, Thm. 6.7] calculated $p(\mathbf{X})$ when $\mathbf{X}$ is Hermitian, Carlson-Toledo [CT93] for $\mathbf{X}$ non-Hermitian symmetric of classical type, and Carlson-Hernández [CH91] for the Cayley hyperbolic plane.

As in § 4.4, we can combine this result with the theorem of Eells-Sampson (Theorem 2.4) to derive a second version of the strong rigidity theorem of Siu (compare with Theorem 4.18):

Theorem 5.19. Let $f: M \rightarrow N$ be a homotopy equivalence where $M$ is compact Kähler and $N=\Gamma \backslash \mathrm{X}$ compact locally symmetric, where $\mathrm{X}=G / K$ is a Hermitian symmetric space of noncompact type with no $\mathbb{H}^{2}$ factor. Then $f$ is homotopic to a biholomorphism for some invariant complex structure on X .

Proof. By Theorem 2.4, we may assume $f$ harmonic. By Theorem 5.17, X is Hermitian symmetric and $f$ is holomorphic if $X$ has no $\mathbb{H}^{2}$ factor. It remains to prove that $f$ is bijective: this is the same topological argument as in the proof of Corollary 4.19. \(\square\)

Remark 5.20. The assumption that $\mathbf{X}$ has no $\mathbb{H}^{2}$ factor is essential in Theorem 5.19. Indeed, consider the case $\mathrm{X}=\mathbb{H}^{2}$. Let $X$ and $Y$ be any two closed Riemann surfaces having same genus $g>1$. The Poincaré metric ${ }^{11}$ on $Y$ gives it a hyperbolic structure. Since $X$ and $Y$ have the same topology, there exists a homeomorphism $f: X \rightarrow Y$. If Theorem 5.19 applied, $f$ would be homotopic to a biholomorphism. However, in general, $X$ and $Y$ are not biholomorphic: this is the starting point of Teichmüller theory, which says that the moduli space of complex structures is $(3 g-3)$-complex dimensional.

Remark 5.21. When X is of compact type, pluriharmonic maps $f: M \rightarrow N$ are still ±-holomorphic, however harmonic maps are not always pluriharmonic. Nevertheless, interesting results can be obtained under more or less general restrictions: refer to [Uda88; OU90] for more details.

\footnotetext{
${ }^{11}$ This is the unique conformal metric of constant curvature -1, given by the celebrated uniformization theorem.
}

\subsection*{5.4 Relation to Mostow rigidity}

We now explain the relation between Siu's strong rigidity and the famous Mostow rigidity. In its original form [Mos68], the theorem of Mostow says that any closed hyperbolic manifold $M=\Gamma \backslash \mathbb{H}^{n}$ of dimension $n>2$ is strongly rigid, in the sense that $M$ is isometric to any other closed hyperbolic manifold homotopic to it. Algebraically, this theorem translates to the fact any two uniform lattices ${ }^{12} \Gamma_{1}, \Gamma_{2}<G=\mathrm{O}^{+}(n, 1)$ that are isomorphic as groups are conjugate in $G$. Mostow then generalized his theorem in [Mos73] to any closed locally symmetric manifold of noncompact type with no 2-dimensional hyperbolic factor. This is the geometric form of Mostow's theorem; let us record the equivalent algebraic form:

Theorem 5.22 (Mostow rigidity). Let $G$ be a semisimple Lie group with trivial center without compact factors nor any $\operatorname{PSL}(2, \mathbb{R})$ factor. If $\Gamma_{1}, \Gamma_{2}<G$ are uniform lattices that are isomorphic as groups, then they are conjugate subgroups of $G$.

Siu's strong rigidity theorem, version Theorem 5.19, may be seen as a generalization of Mostow rigidity when $G$ is Hermitian. Indeed, assume both $M=\Gamma_{1} \backslash \mathrm{X}$ and $N=\Gamma_{2} \backslash \mathrm{X}$ are closed manifolds locally isometric to $\mathrm{X}=G / K$. For simplicity, assume $G$ is simple, i.e. X is irreducible. If $f: M \rightarrow N$ is a homotopy equivalence, then by Theorem $5.19 f$ is homotopic to a ±-biholomorphism. Lift $f$ to a $\left(\Gamma_{1}, \Gamma_{2}\right)$-equivariant biholomorphism $\tilde{f}: \mathbf{X} \rightarrow \mathbf{X}$. Since ±-biholomorphisms of X are isometries, as shows the Bergman metric on a bounded symmetric domain, $\tilde{f}$ coincides with an element of $G$.

Let us conclude with a few historical comments on the rigidity of lattices. Fore more details, we refer to [GP91; Spa04; Pan95]. Before Mostow's results, the local rigidity ${ }^{13}$ of lattices in a group $G$ as in Theorem 5.22 had been proven by Weil [Wei62], following Calabi and Vesentini [CV59; CV60] who first proved it for $G$ Hermitian using analytic methods similar to the ones presented in this report. Mostow used different techniques, essentially studying the dynamics of the action of $\Gamma<G$ on the ideal boundary of $\mathrm{X}=G / K$. Such techniques were further developed by Margulis to prove spectacular refinements of Mostow rigidity known as superrigidity and arithmeticity [Mar75]. On the other hand, following the work of Siu, the harmonic maps approach was successfully used by Mok [Mok89] to prove superrigidity for Hermitian Lie groups and by Corlette [Cor92] for $G=\operatorname{Sp}(n, 1)$. Gromov-Schoen [GS92] extended Corlette's argument to groups of rank 1 over local fields by generalizing the notion of harmonic map to singular targets. Finally, Mok-Siu-Yeung [MSY93], Jost-Yau [JY97], and Jost-Zuo [JZ97] generalized superrigidity for higher rank groups and quasiprojective varieties.

\section*{6 Nonabelian Hodge theory}

In this final section, we emphasize the key role of the Siu-Sampson theorem for the nonabelian Hodge correspondence from group representations to Higgs bundles. Using an extension of the Eells-Sampson theorem due to Corlette, it will be straighforward to construct a Higgs bundle out of a representation by applying the Siu-Sampson theorem: it is essentially a rephrasing of Lemma 5.14. The reader in a hurry may jump to § 6.2.1, which explains this point, and skip the rest of the section.

In order to motivate this construction, we attempt a brief introduction to the fascinating subject of nonabelian Hodge theory, which is not a trivial task. Thankfully, there are many good references: I recommend the phenomenal paper of Simpson [Sim92] and the more introductory resources [Le 91; Amo+96; Sim97; Wel08; Bra12; Got14; GR15; Wen16; Gui18; Li19; Bra20].

\footnotetext{
${ }^{12}$ A lattice $\Gamma<G$ in a Lie group is a discrete subgroup such that $\Gamma \backslash G$ has finite volume. It is called uniform if $\Gamma \backslash G$ is compact. Prasad [Pra73] extended Mostow rigidity to lattices that are not assumed uniform.
${ }^{13}$ The (local) rigidity of $\Gamma<G$ means that if $\rho_{t}: \Gamma \rightarrow G$ is a one-parameter family of injective group homomorphisms, where $\rho_{0}$ is the inclusion, such that $\rho_{t}(\Gamma)<G$ is a uniform lattice for all $t$, then $\rho_{t}$ is conjugate to $\rho_{0}$ in $G$.
}

\subsection*{6.1 From classical to nonabelian Hodge theory}

\subsection*{6.1.1 Classical Hodge theory}

For a thorough treatment of what follows, refer to e.g. [Ber+02; Voi07].
Let $M$ be a complex manifold. Let us denote $\mathcal{A}^{k}=\mathcal{A}^{k}(M, \mathbb{C})$ the space (or sheaf) of $\mathbb{C}$-valued differential $k$-forms and reserve the notation $\Omega^{k} \subseteq \mathcal{A}^{k}$ for the sheaf of $(k, 0)$-forms (see below) that are holomorphic. We have seen in § 3.1 that the complexified cotangent space decomposes as $\mathrm{T}_{\mathbb{C}}^{*} M=$ $\mathrm{T}^{* 1,0} M \oplus \mathrm{~T}^{* 0,1} M$, this induces the decomposition $\Lambda^{k} \mathrm{~T}_{\mathbb{C}}^{*} M=\bigoplus_{p+q=k}\left(\Lambda^{p} \mathrm{~T}_{\mathbb{C}}^{* 1,0} M\right) \wedge\left(\Lambda^{q} \mathrm{~T}_{\mathbb{C}}^{* 0,1} M\right)$ and accordingly $\mathcal{A}^{k}=\bigoplus \mathcal{A}^{p, q}$. The exterior derivative $\mathrm{d}: \mathcal{A}^{k} \rightarrow \mathcal{A}^{k+1}$ also splits as $\mathrm{d}=\partial+\bar{\partial}$, where $\partial: \mathcal{A}^{p, q} \rightarrow \mathcal{A}^{p+1, q}$ and $\bar{\partial}: \mathcal{A}^{p, q} \rightarrow \mathcal{A}^{p, q+1}$. The fact that $\mathrm{d}^{2}=0$ implies that $\bar{\partial}^{2}=0$, so one can consider the Dolbeault complex $\left(\mathcal{A}^{p, \cdot}, \bar{\partial}\right)$. The $\bar{\partial}$-Poincaré lemma ensures that it is an acyclic resolution of the holomorphic sheaf $\Omega^{p} \subseteq \mathcal{A}^{p, 0}$, so that it computes its cohomology: we have $\mathrm{H}^{q}\left(\Omega^{p}\right) \approx \mathrm{H}_{\mathrm{Dol}}^{p, q}$. This is the Dolbeault isomorphism, analogous to the de Rham isomorphism $\mathrm{H}^{k}(M, \mathbb{R}) \approx \mathrm{H}_{\mathrm{dR}}^{k}(M, \mathbb{R})^{14}$.

Assume that $M$ has a compatible Riemannian metric, i.e. is Hermitian. We have seen in § 1.3 that if $M$ is closed, the de Rham cohomology $\mathrm{H}_{\mathrm{dR}}^{k}(M, \mathbb{C})$ is isomorphic to the space of harmonic $k$-forms $\mathcal{H}^{k}(M, \mathbb{C})$. Does the Laplacian $\Delta=\mathrm{dd}^{*}+\mathrm{d}^{*} \mathrm{~d}$ respect the decomposition $\mathcal{A}^{k}=\bigoplus \mathcal{A}^{p, q}$, yielding a refinement $\mathcal{H}^{k}(M, \mathbb{C})=\bigoplus \mathcal{H}^{p, q}(M, \mathbb{C})$ ? The answer is yes provided $M$ is Kähler. Indeed, it is a consequence of the Kähler identities (see [Ber+02]) that $\Delta=2 \Delta_{\bar{\partial}}$, where $\Delta_{\bar{\partial}}:=\bar{\partial} \bar{\partial}^{*}+\bar{\partial}^{*} \bar{\partial}$. It follows that $\Delta$ preserves bidegree. Furthermore, we obviously have $\mathcal{H}^{p, q}(M, \mathbb{C})=\mathcal{H}_{\Delta_{\bar{\partial}}}^{p, q}(M, \mathbb{C})$, and since the operator $\Delta_{\bar{\partial}}$ is self-adjoint and elliptic, the same proof as in § 1.3 shows that $\mathrm{H}_{\text {Dol }}^{p, q}(M, \mathbb{C})=\mathcal{H}_{\Delta_{\bar{\partial}}}^{p, q}(M, \mathbb{C})$.

In summary, if $M$ is compact Kähler, then we have the decomposition $\mathcal{H}^{k}(M, \mathbb{C})=\bigoplus \mathcal{H}^{p, q}(M, \mathbb{C})$, which can canonically be rewritten
$$\mathrm{H}^{k}(M, \mathbb{C}) \approx \bigoplus_{p+q=k} \mathrm{H}_{\mathrm{Dol}}^{p, q}(M, \mathbb{C}) \approx \bigoplus_{p+q=k} \mathrm{H}^{q}\left(M, \Omega^{p}\right) .$$
Remark 6.1. Remarkably, the isomorphisms in (25) turn out to be independent of the Kähler metric. This can be shown by equating the Dolbeault and the Bott-Chern cohomology using the $\partial \bar{\partial}$-lemma.
Remark 6.2. In algebraic geometry, the decomposition of a complex vector space as $V=\bigoplus_{p+q=k} V^{p, q}$ with $V^{q, p}=\overline{V^{p, q}}$ is called a Hodge structure of weight $k^{15}$. Thus the cohomology of a compact Kähler manifold has a Hodge structure. A Hodge structure of weight $k$ is equivalent to a $\mathbb{C}^{*}$-action on $V$ such that any $\lambda \in \mathbb{R}^{*}$ acts by scalar multiplication by $\lambda^{k}$. Indeed, $V^{p, q}$ can be recovered as the subspace where any $\lambda \in \mathbb{C}^{*}$ acts by scalar multiplication by $\lambda^{p} \bar{\lambda}^{q}$. For more details, refer to [CMP17, Chap. 15].

\subsection*{6.1.2 Extension to flat Hermitian bundles}

Let $M$ be a compact Kähler manifold. It is straightforward to generalize the discussion of § 6.1.1 to differential forms with values in a complex vector bundle $E$, equipped with a flat complex connection ∇ and a compatible Hermitian metric $h$. We already mentioned in § 1.3 that the de Rham cohomology and the Hodge isomorphism extend. It remains to define the Dolbeault cohomology, which is done by decomposing $\mathrm{d}_{\nabla}$ into types as $\mathrm{d}_{\nabla}=\partial_{\nabla}+\bar{\partial}_{\nabla}$. We have $\bar{\partial}_{\nabla}^{2}=0$, so we can define the Dolbeault complex, etc. The Kähler identities extend to this situation, and similarly to the case $E=\mathbb{C}$ one proves
$$\mathrm{H}^{k}(M, E) \approx \bigoplus_{p+q=k} \mathrm{H}_{\mathrm{Dol}}^{p, q}(M, E) \approx \bigoplus_{p+q=k} \mathrm{H}^{q}\left(M, \Omega^{p}(E)\right) .$$

\footnotetext{
${ }^{14}$ On the left-hand side of these isomorphisms, we are taking the sheaf cohomology. It can be identified to the Čech cohomology, as a consequence of manifolds being assumed paracompact and Hausdorff.
${ }^{15}$ Typically, an integral structure is also required, i.e. a lattice $V_{\mathbb{Z}}$ such that $V=V_{\mathbb{Z}} \otimes \mathbb{C}$. We ignore that part of the definition, but need at least a real structure so that complex conjugation is well-defined.
}

It is well-known that the data of an operator $\bar{\partial}_{E}: \mathcal{A}^{p, q}(M, E) \rightarrow \mathcal{A}^{p, q+1}(M, E)$ satisfying the appropriate Leibniz rule and such that $\bar{\partial}_{E}^{2}=0$-called a Dolbeault operator-is equivalent to a holomorphic structure in $E$, where $s \in \mathcal{A}^{0}(E)$ is holomorphic if and only if $\bar{\partial}_{E} s=0^{16}$. In the presence of a holomorphic structure and a Hermitian metric, it is easy to show that there exists a unique compatible connection ∇ such that $\bar{\partial}_{E}=\bar{\partial}_{\nabla}$, called the Chern connection. Similary to the case $E=\mathbb{C}$, the Hodge decomposition (26) turns out to be independent of both the choice of Kähler metric on $M$ and the Hermitian metric on $E$ : it only depends on the holomorphic structure on $E$, as long as there exists a Hermitian metric whose Chern connection is flat-called a Hermite-Einstein metric. This condition is not trivial, it implies first of all that $E$ has vanishing Chern classes. Conversely, such a vector bundle admits a Hermite-Einstein metric if and only if it is polystable ${ }^{17}$. This result is known as the Hitchin-Kobayashi correspondence; when $\operatorname{dim}_{\mathbb{C}} M=1$ it is the famous theorem of Narasimhan-Seshadri [NS65], generalized to higher dimensions by Donaldson [Don85] and Uhlenbeck-Yau [UY86].

A flat structure on a complex vector bundle is equivalent to a locally constant sheaf (the sheaf of flat sections), i.e. a local system. Alternatively, it is given by a group homomorphism $\rho: \pi_{1} M \rightarrow$ $\operatorname{GL}(n, \mathbb{C})$ where $n$ is the rank of $E$, which is the holonomy of the flat connection $\nabla^{18}$. In our situation, ∇ preserving a metric means that its holonomy is unitary, i.e. $\rho: \pi_{1} M \rightarrow \mathrm{U}(n)$. All in all, the Hitchin-Kobayashi correspondence yields a bijection between conjugacy classes of unitary representations and isomorphism classes of polystable holomorphic bundles with vanishing Chern classes.

\subsection*{6.1.3 Extension to nonabelian groups}

My humble takeaway is that nonabelian Hodge theory can be viewed as an extension of classical Hodge theory for the weight $k=1$ at two different-yet related-levels:
\begin{itemize}
\item[(i)] At the "macroscopic" level: The classical case gives a Hodge structure on $\mathrm{H}^{1}(M, \mathbb{C})$. We now seek a Hodge structure on $\mathrm{H}^{1}(M, G)$ when $G=\mathrm{GL}(n, \mathbb{C})$ or a more general reductive group.
\item[(ii)] At the "microscopic" level: we saw that Hodge theory works for the cohomology $\mathrm{H}^{1}(M, E)$ with coefficients in a polystable holomorphic vector bundle $E$, i.e. correspondi to a unitary representation $\rho: \pi_{1} M \rightarrow \mathrm{U}(n)$. We seek a generalization for arbitrary flat bundles, i.e. for $\rho: \pi_{1} M \rightarrow \operatorname{GL}(n, \mathbb{C})$.
\end{itemize}

We now discuss this in a bit more detail, starting with (i). The cohomology $\mathrm{H}^{k}(M, \mathcal{F})$ is generally defined for a sheaf $\mathcal{F}$ of abelian groups: this ensures that quotient groups are well-defined. When $\mathcal{F}$ is a nonabelian sheaf, the $k=1$ cohomology $\mathrm{H}^{1}(M, \mathcal{F})$ is still well-defined as a set. Recall that for $\mathcal{F}=\mathbb{C}$, the Hodge decomposition was
$$\mathrm{H}^{1}(M, \mathbb{C}) \approx \mathrm{H}_{\mathrm{Dol}}^{0,1}(M, \mathbb{C}) \oplus \mathrm{H}_{\mathrm{Dol}}^{1,0}(M, \mathbb{C}) \approx \mathrm{H}^{1}(M, \mathcal{O}) \oplus \mathrm{H}^{0}\left(M, \Omega^{1}\right) .$$
Consider now $G=\mathrm{GL}(n, \mathbb{C})$, denote also by $G$ the constant sheaf over $M$, and $\mathcal{G}$ its sheaf of holomorphic sections. The cohomology $\mathrm{H}^{1}(M, G)$ can be identified to the space $\operatorname{Hom}\left(\pi_{1} M, G\right) / G$ of group homomorphisms up to conjugation, or to the space of $G$-local systems over $M$. The analogue of $\mathrm{H}^{1}(M, \mathcal{O})$ is $\mathrm{H}^{1}(M, \mathcal{G})$, which parametrizes holomorphic bundles of rank $n$ over $M$ up to isomorphism (this is easy to see with Čech cohomology). We shall see that the second piece $\mathrm{H}^{0}\left(M, \Omega^{1}\right)$ will be replaced by $\mathrm{H}^{0}\left(M, \operatorname{End}(\mathcal{E}) \otimes \Omega^{1}\right)$, where $\mathcal{E}$ is the holomorphic vector bundle under consideration. Note that, since the second piece (called the Higgs field) is defined relative to the first (the holomorphic bundle), the "Hodge decomposition" of $\mathrm{H}^{1}(M, G)$ is a twisted sum rather than a direct sum.

Now let us expand on (ii). We have seen that Hodge theory applies in flat bundles that preserve a Hermitian metric, equivalently, to holomorphic bundles with vanishing Chern classes that admit a

\footnotetext{
${ }^{16}$ The holomorphic structure associated to a Dolbeault operator is sometimes called the Koszul-Malgrange holomorphic structure. Its existence is a consequence of the Newlander-Nirenberg theorem.
${ }^{17}$ A vector bundle $E$ of degree 0 is called stable if any subbundle has negative degree, semistable if any subbundle has nonpositive degree, and polystable if it is a direct sum of stable bundles of degree 0.
${ }^{18}$ In the algebraic setting, which allows singularities, the equivalence between flat bundles, local systems, and representations is known as the Riemann-Hilbert correspondence.
}

Hermite-Einstein metric. Simpson extended the Kähler identities to flat bundles that admit a harmonic metric (see § 6.2), and showed that they correspond to polystable Higgs bundles with vanishing Chern classes, extending the Hitchin-Kobayashi correspondence. On the other hand, Corlette showed that harmonic flat bundles correspond to reductive representations $\rho: \pi_{1} M \rightarrow \operatorname{GL}(n, \mathbb{C}){ }^{19}$. Referring to these two correspondences, Simpson writes ([Sim91, below Thm. 1]):

> The set of flat bundles is analogous to the abelian de Rham cohomology, while the set of Higgs bundles is analogous to the abelian Dolbeault cohomology, $\mathrm{H}^{1}(\mathcal{O}) \oplus \mathrm{H}^{0}\left(\Omega^{1}\right)$. The first two parts of Theorem 1 may be interpreted as giving harmonic representatives for certain nonabelian de Rham and Dolbeault cohomology classes. The fact that the notion of harmonic representative (harmonic bundle) is the same in both cases, is the analogue of the abelian Kähler identity $\Delta_{\mathrm{d}}=2 \Delta_{\bar{\partial}}$.

\subsection*{6.2 The nonabelian Hodge correspondence}

\subsection*{6.2.1 From representations to Higgs bundles}

Let $M$ be a compact Kähler and $G$ be a reductive complex algebraic group. For simplicity, we first consider $G=\operatorname{GL}(n, \mathbb{C})$.

Consider a flat rank $n$ vector bundle $(E, \nabla)$ over $M$. Recall that this is equivalent to a $G$-local system, or to a representation $\rho: \pi_{1} M \rightarrow G$. Any Hermitian metric $h$ in $E$ induces a "unitary + self-adjoint" decomposition $\nabla=\nabla_{h}+\psi_{h}$, where $\nabla_{h}$ is a connection preserving $h$ and $\psi_{h} \in \mathcal{A}^{1}\left(M, \operatorname{Sym}_{h}(E)\right)$ is a 1-form with values in $h$-self-adjoint endomorphisms. The choice of the Hermitian metric $h$ is equivalent to a reduction of the structure group of $E$ from $G$ to $K=\mathrm{U}(n)$, given by a smooth $\rho$-equivariant ${ }^{20}$ map $f: \tilde{M} \rightarrow \mathbf{X}=G / K$ called the classifying map of the metric. Its differential $\mathrm{d} f$ can be seen as a 1 -form with value in $f^{*}(\mathrm{TX})$, and the latter bundle can be identified $\operatorname{Sym}_{h}(E)$. One readily checks that $\psi_{h}=\mathrm{d} f$ under this identification, while $\nabla_{h}$ is essentially the pullback of the Levi-Civita connection of X.

Definition 6.3. A Hermitian metric $h$ in a flat vector bundle $(E, \nabla)$ is harmonic if it satisfies one of the equivalent conditions:
\begin{itemize}
\item[(i)] $h$ is a critical point of the energy functional $\mathbf{E}(h)=\frac{1}{2} \int_{M}\left\|\psi_{h}\right\|^{2} \mathrm{~d} v_{M}$.
\item[(ii)] $\mathrm{d}_{\nabla_{h}}^{*} \psi_{h}=0$.
\item[(iii)] The classifying map $f: \tilde{M} \rightarrow \mathrm{X}=G / K$ is harmonic.
\end{itemize}

The equivalence of the conditions in Definition 6.3 is exactly Theorem 1.25.
The third characterization (iii) implies that the question of the existence and uniqueness of a harmonic metric on $(E, \nabla)$ is the same as that of $\rho$-equivariant harmonic map $f: \tilde{M} \rightarrow \mathrm{X}$. More generally, one can study $\rho$-equivariant harmonic maps $f: \tilde{M} \rightarrow N$ where $M$ and $N$ are Riemannian manifolds, with $\rho: \pi_{1} M \rightarrow \operatorname{Isom}(N)$. This is an extension of the classical situation studied by Eells-Sampson. When $N=\mathrm{X}$ is a symmetric space of noncompact type, Corlette proved:

Theorem 6.4 (Corlette [Cor88]). Let $M$ be a compact Riemannian manifold, let $\mathrm{X}=G / K$ be a symmetric space of noncompact type, and let $\rho: \pi_{1} M \rightarrow G$ be a group homomorphism. There exists a $\rho$-equivariant harmonic map $f: \tilde{M} \rightarrow \mathbf{X}$ if and only if $\rho$ is reductive.

\footnotetext{
${ }^{19} \mathrm{~A}$ representation $\rho: \pi_{1} M \rightarrow G=\mathrm{GL}(n, \mathbb{C})$ is called reductive (or completely reducible, or polystable) if its action on $\mathbb{C}^{n}$ is completely reducible. More generally, if $G$ is any algebraic group, $\Gamma:=\rho\left(\pi_{1} M\right)<G$ is called completely reducible if the identity component of its Zariski closure is a reductive subgroup, i.e. with trivial unipotent radical. Equivalently, for every parabolic subgroup $P<G$ containing $\Gamma$, there is a Levi factor of $P$ containing $\Gamma$ [Sik12].
${ }^{20}$ By definition, $f: \tilde{M} \rightarrow G / K$ is $\rho$-equivariant if $f(\gamma \cdot x)=\rho(\gamma) \cdot f(x)$ for all $x \in M$ and $\gamma \in \pi_{1} M$, where $\pi_{1} M$ acts by deck transformations on $\tilde{M}$ and $G$ acts by left translations on $G / K$.
}

Remark 6.5. Like Corlette, we stated Theorem 6.4 for a symmetric space of noncompact type, i.e. for a semisimple Lie group $G$, but it holds more generally for a reductive group such as $G=\operatorname{GL}(n, \mathbb{C})$. The same goes for most of § 5 and Lemma 6.8 below.

Remark 6.6. Labourie [Lab91] gave a more general version of Theorem 6.4, replacing X by any simply-connected Riemannian manifold $N$ of nonpositive sectional curvature "without flat half-strips". His short proof is an extension of the heat flow method of Eells-Sampson described in § 2.2.2.

Remark 6.7. An application of the classical uniqueness result for harmonic maps (due to Hartman [Har67] and Al'ber [Alb68]) shows that in Theorem 6.4, when a $\rho$-equivariant harmonic map $f$ exists, it is necessarily unique up to post-composition with elements of the centralizer of $\rho\left(\pi_{1}(M)\right)<G$.

In the language of bundles, Corlette's theorem says that a flat bundle $(E, \nabla)$ admits a (essentially unique) harmonic metric if and only if it is semisimple. We are now halfway in the nonabelian Hodge correspondence from (reductive) representations, i.e. (semisimple) flat bundles, to Higgs bundles:
$$\left.\{\text { flat bundles }\} \longrightarrow\{\text { harmonic bundles }\}--^{?} \rightarrow \text { \{Higgs bundles }\right\}$$
The second step, from harmonic bundles to Higgs bundles, is where the theorem of Siu-Sampson is critical. Specifically, we have the key lemma, which is little more than a rephrasing of Lemma 5.14:

Lemma 6.8. Let $f: M \rightarrow \mathrm{X}$, where $M$ is compact Kähler and $\mathrm{X}=G / K$ is symmetric of noncompact type. Denote by $\mathrm{d}_{\nabla}$ the exterior covariant derivative in $\Omega^{\bullet}\left(M, f^{*} \mathrm{TX}\right)$ as in § 1.3. If $f$ is harmonic, then:
$$\begin{aligned}
\left(\bar{\partial}_{\nabla}\right)^{2} & =0 \\
\bar{\partial}_{\nabla} \mathrm{d}^{1,0} f & =0 \\
{\left[\mathrm{~d}^{1,0} f, \mathrm{~d}^{1,0} f\right] } & =0
\end{aligned}$$
Remark 6.9. The expression $\left[\mathrm{d}^{1,0} f, \mathrm{~d}^{1,0} f\right]$ is an element of $\mathcal{A}^{2}\left(M, f^{*} \mathrm{~T}_{\mathbb{C}} \mathbf{X}\right)$, taking the exterior product of one-forms with the Lie bracket in $\mathrm{T}_{\mathbb{C}} X \approx \mathfrak{g}$ as coefficient pairing. When $G=\operatorname{GL}(n, \mathbb{C})$, we saw that $\mathrm{d} f=\psi_{h}$ is a one-form with values in $\operatorname{Sym}_{h}(E)$, and the Lie bracket is the commutator of endomorphisms.

Proof of Lemma 6.8. Lemma 5.14 immediately gives (29), which is a characterization of pluriharmonicity (Proposition 3.11), and (30), which is the fact that $\mathfrak{a}_{x}:=\mathrm{d} f\left(\mathrm{~T}_{x}^{1,0} M\right)$ is an abelian subalgebra of $\mathfrak{g}$ for all $x \in M$. As for (28), it is the condition that $R^{\mathrm{X}}(\mathrm{d} f(X), \mathrm{d} f(Y))=0$ for all $X, Y \in \mathrm{~T}^{0,1} M$, in other words $\left[\mathrm{d}^{0,1} f, \mathrm{~d}^{0,1} f\right]=0$, which is easily derived from $\left[\mathrm{d}^{1,0} f, \mathrm{~d}^{1,0} f\right]=0$ by conjugation. \(\square\)

Remark 6.10. Consider the vector bundle $f^{*} \mathrm{~T}_{\mathbb{C}} N$ over $M$. If $f$ is harmonic, by (28), $\bar{\partial}_{\nabla}$ is a Dolbeault operator, giving it a holomorphic structure. (29) then says that $\mathrm{d}^{1,0} f$ is a holomorphic (1, 0)-form.

Theorem 6.11 (Application of the Siu-Sampson theorem). Let $(E, \nabla)$ be a flat complex vector bundle. If $h$ is a harmonic metric on $(E, \nabla)$, then $\bar{\partial}_{E}:=\bar{\partial}_{\nabla_{h}}$ and $\varphi:=\left(\psi_{h}\right)^{1,0}$ satisfy:
$$\begin{aligned}
\bar{\partial}_{E}^{2} & =0 \\
\bar{\partial}_{E} \varphi & =0 \\
{[\varphi, \varphi] } & =0 .
\end{aligned}$$
Moreover, we have Hitchin's equation ${ }^{21}$ :
$$F^{\nabla_{h}}+\left[\varphi, \varphi^{* h}\right]=0 .$$

\footnotetext{
${ }^{21}$ Hitchin calls this equation together with $\bar{\partial}_{E} \varphi=0$ the self-duality equations [Hit87].
}

Proof. We have seen that under appropriate identifications, $\psi_{h}=\mathrm{d} f$ and $\nabla_{h}$ is the pullback of the Levi-Civita connection of X. The first part of the theorem is then simply a rephrasing of Lemma 6.8. Finally, Hitchin's equation amounts to the flatness of ∇ . Indeed, first write $F^{\nabla}=F^{\nabla_{h}}+\nabla_{h} \psi_{h}+\psi_{h} \wedge \psi_{h}=0$. Decomposing into $\pm-h$-self-adjoint components:
$$\begin{aligned}
F^{\nabla_{h}}+\psi_{h} \wedge \psi_{h} & =0 \\
\nabla_{h} \psi_{h} & =0 .
\end{aligned}$$
The second equation can be rewritten $\mathrm{d}_{\nabla_{h}} \mathrm{~d} f=0$, and we have seen in Proposition 1.12 that this is actually automatic. The first equation can be rewritten $F^{\nabla_{h}}+\frac{1}{2}\left[\psi_{h}, \psi_{h}\right]=0$. Since $\psi_{h}$ is $h$-self-adjoint, one must have $\psi^{0,1}=\left(\psi^{1,0}\right)^{*}$, i.e. $\psi=\varphi+\varphi^{* h}$. Since $[\varphi, \varphi]=\left[\varphi^{* h}, \varphi^{* h}\right]=0$, the conclusion follows. \(\square\)

Definition 6.12. A Higgs bundle is a pair $(\mathcal{E}, \varphi)$, where $\mathcal{E}$ is a holomorphic vector bundle and $\varphi$ is a holomorphic section of $\operatorname{End} \mathcal{E} \otimes \Omega^{1}$ such that $[\varphi, \varphi]=0$.

Theorem 6.11 thus says that if $(E, \nabla, h)$ is a flat harmonic bundle, then $(\mathcal{E}, \varphi)$ is a Higgs bundle, where $\mathcal{E}:=\left(E, \bar{\partial}_{E}\right)$. This complete our description of the nonabelian Hodge correspondence from representations to Higgs bundles.

\subsection*{6.2.2 From Higgs bundles to representations}

In the previous subsection, we described how to produce a harmonic flat bundle out of a representation, and then a Higgs bundle. This construction also yielded a metric $h$ satisfying Hitchin's equation (31). Note that, forgetting the flat connection $\nabla$, Hitchin's equation still makes sense given the Higgs bundle $(\mathcal{E}, \varphi)$ : one should then understand $\nabla_{h}$ as the Chern connection of $h$ in $\mathcal{E}$.

Definition 6.13. A Hermitian metric $h$ in a Higgs bundle $(\mathcal{E}, \varphi)$ with vanishing Chern classes is called Hermitian-Yang-Mills if it satisfies Hitchin's equation (31).

We saw that if $(E, \nabla, h)$ is a flat harmonic bundle, then $(\mathcal{E}, \varphi, h)$ is a Hermitian-Yang-Mills Higgs bundle, with $\bar{\partial}_{E}:=\bar{\partial}_{\nabla_{h}}$ and $\varphi:=\left(\psi_{h}\right)^{1,0}$, where $\nabla=\nabla_{h}+\psi_{h}$ is the unitary + self-adjoint decomposition of $\nabla$. Conversely, $(E, \nabla, h)$ is easily reconstructed from $(\mathcal{E}, \varphi, h)$ : put $\nabla=\nabla_{h}+\psi_{h}$, where $\nabla_{h}$ is the Chern connection of $h$ in $\mathcal{E}$, and $\psi_{h}:=\varphi+\varphi^{*} h$. It is then straightforward to check that ∇ is flat and $h$ is harmonic, using the equations $F^{\nabla_{h}}+\left[\varphi, \varphi^{* h}\right]=0, \bar{\partial}_{\nabla_{h}} \varphi=0$, and $[\varphi, \varphi]=0$. Let us put this on record:

Proposition 6.14. Let $E \rightarrow M$ be a complex vector bundle with vanishing Chern classes. There is a 1:1 correspondence between harmonic flat bundles $(E, \nabla, h)$ and Hermitian-Yang-Mills Higgs bundles $(\mathcal{E}, \varphi, h)$.

Remark 6.15. Instead of Hermitian-Yang-Mills metrics, [Bra20] says Higgs-Hermite-Einstein to emphasize that they generalize Hermite-Einstein metrics. For Higgs bundles with vanishing Chern classes, it is sensible to call them harmonic. The coincidence of harmonicity for flat bundles and Higgs bundles is the analogue of the Kähler identity $\Delta_{\mathrm{d}}=2 \Delta_{\bar{\partial}}$ that we referred to in § 6.1.3 in the words of Simpson.

To complete the nonabelian Hodge correspondence, we need the fundamental result of Hitchin [Hit87] (for the rank 2 case over a Riemann surface) and Simpson [Sim88] (for the general case), generalizing the Hitchin-Kobayashi correspondence:

Theorem 6.16 (Simpson). A Higgs bundle admits a Hermitian-Yang-Mills metric if and only if it is polystable ${ }^{22}$.

\footnotetext{
${ }^{22}$ The notion of stability for Higgs bundles is a natural refinement of the notion for holomorphic bundles: in the definition, only considers Higgs subbundles, i.e. holomorphic subbundles preserved by the Higgs field.
}

The proof of Theorem 6.16 relies on geometric analysis; it consists in minimizing a Yang-Mills functional. We shall not discuss any details and refer to the excellent [Wen16] instead.

Let us recap with a diagram slightly more detailed than (27):
![](https://cdn.mathpix.com/cropped/242d029a-52c7-4ca3-94a0-4a04c314c40f-33.jpg?height=348&width=1532&top_left_y=466&top_left_x=267)

Let us give a cute return on investment from our study of pluriharmonic maps (§ 3.2):
Proposition 6.17. Let $Q \subseteq M$ be a complex submanifold. Any polystable Higgs bundle $(\mathcal{E}, \varphi)$ on $M$ stays polystable in restriction to $Q$.

Proof. By Simpson's theorem, there exists a harmonic metric $h$ on $(\mathcal{E}, \varphi)$. Let $f: \tilde{M} \rightarrow G / K$ indicate the associated classifying map. We have seen that $h$ being harmonic amounts to $f$ being harmonic. By the Siu-Sampson theorem, $f$ is pluriharmonic (Lemma 5.14). It follows that the restriction of $f$ to $\tilde{N}$ is pluriharmonic (Proposition 3.15). This means that $h$ is still harmonic as a metric on the Higgs bundle $(\mathcal{E}, \varphi)$ restricted to $N$. By Simpson's theorem, it must be polystable. \(\square\)

\subsection*{6.2.3 More general groups}

We now briefly describe how to generalize the nonabelian Hodge correspondence to more general groups than $\operatorname{GL}(n, \mathbb{C})$. Refer to [Got14] for details and [Dup03] for background material on fiber bundles.
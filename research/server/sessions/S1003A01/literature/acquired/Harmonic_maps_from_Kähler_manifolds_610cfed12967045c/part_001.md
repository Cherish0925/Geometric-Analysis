---
retention_scope: session
part: 1
total_parts: 3
---

[Part 1/3 of: Harmonic maps from Kähler manifolds]

---
source_file: 2010_03545.pdf
converter: mathpix
format: mmd
---

\title{
Harmonic maps from Kähler manifolds
}

\author{
Brice Loustau*
}

\begin{abstract}
This report attempts a clean presentation of the theory of harmonic maps from complex and Kähler manifolds to Riemannian manifolds. After reviewing the theory of harmonic maps between Riemannian manifolds initiated by Eells-Sampson and the Bochner technique, we specialize to Kähler domains and introduce pluriharmonic maps. We prove a refined Bochner formula due to Siu and Sampson and its main consequences, such as the strong rigidity results of Siu. We also recount the applications to symmetric spaces of noncompact type and their relation to Mostow rigidity. Finally, we explain the key role of this theory for the nonabelian Hodge correspondence relating the character variety of a compact Kähler manifold and the moduli space of Higgs bundles.
\end{abstract}

Key words and phrases: Harmonic maps • Pluriharmonic maps • Kähler manifolds • Symmetric spaces ⋅ Bochner formula ⋅ Rigidity ⋅ Higgs bundles ⋅ Nonabelian Hodge

2000 Math. Subject Classification: Primary: 58E20; Secondary: 53C43 • 53C55 • 32W50 • 53C24

\section*{Introduction}

\footnotetext{
*Heidelberg University and Heidelberg Institute of Theoretical Studies. 69120 Heidelberg, Germany.
E-mail: bloustau@mathi.uni-heidelberg.de
}

\section*{Introduction}

The theory of harmonic maps between Riemannian manifolds was properly started by Eells and Sampson [ES64]. A smooth map $f: M \rightarrow N$ is harmonic if it is a critical point of the energy functional
$$\mathbf{E}(f)=\frac{1}{2} \int_{M}\|\mathrm{~d} f\|^{2} \mathrm{~d} v .$$
Equivalently, $f$ solves the corresponding Euler-Lagrange equation:
$$\Delta f=0$$
where the Laplacian $\Delta$, more commonly denoted $\tau(f)$ and called tension field, is a nonlinear operator generalizing the Riemannian Laplacian. We recall its definition in $\$ 1$ and explain why $\Delta f=0$ is equivalent to the harmonicity of the one-form $\mathrm{d} f \in \Omega^{1}\left(M, f^{*} \mathrm{~T} N\right)$ in the sense of Hodge theory.

The nonlinear PDE $\Delta f=0$ is typically determined and Eells and Sampson proved the existence of harmonic maps when the target manifold $N$ has nonpositive sectional curvature (assuming $M$ and $N$ are compact), using a heat flow technique. The success of this technique relies on a Bochner formula for maps between Riemannian manifolds generalizing the classical Bochner-Weitzenböck formulas. They additionally showed rigidity results under stronger curvature assumptions, such as nonnegative Ricci curvature for the domain manifold and negative sectional curvature for the target manifold.

In the seminal paper [Siu80], Siu adapted Eells-Sampson's Bochner techniques to the setting where $M$ is a Kähler manifold. Siu's ideas were further developed by Sampson [Sam86] and Carlson-Toledo [CT89], among others. Sampson showed that if $M$ is compact Kähler and $N$ has nonpositive Hermitian sectional curvature, any harmonic map $M \rightarrow N$ is pluriharmonic, a stronger version of harmonicity. Moreover Siu's technique yields a constraint on the relation between the image of $\mathrm{d} f$ in T $N$ and the curvature tensor of $N$, leading to strong rigidity results under appropriate curvature assumptions. In particular, there are remarkable consequences when $N=G / K$ is a symmetric space of noncompact type, that relate to the famous Mostow rigidity theorem.

This theory is key for the nonabelian Hodge correspondence initiated by Hitchin [Hit87] and Donaldson [Don87] and generalized by Corlette [Cor88] and Simpson [Sim88; Sim91; Sim92; Sim94], beautifully relating the $G$-character variety of a compact Kähler manifold $M$ and the moduli space of $G$-Higgs bundles over $M$.

The goal of this report is to give a clean presentation of these ideas and results, after developing the relevant mathematical background mostly consisting of standard differential geometry. I hope that it becomes a useful reference to non-experts in the theory of harmonic maps who may wish to apply it to other areas, such as the study of representations of discrete groups in Lie groups. Of course, there are already good references on the subject, such as the excellent book [Amo+96] which I used substantially in the preparation of these notes (especially § 5). I shall list other main references for each topic throughout subsequent sections.

\section*{Acknowledgments}

This report originated in an expository talk that I gave at the workshop Harmonic maps and rigidity ${ }^{1}$ in Sisteron, France in April 2019. I am very grateful to the organizers Alexis Gilles, Nicolas Tholozan, and Jérémy Toulisse for this wonderful experience. I also thank all the workshop participants for stimulating mathematical discussions.

I gratefully acknowledge research support from the NSF Grant DMS1107367 aka RNMS: GEometric structures And Representation varieties (the GEAR Network).

\footnotetext{
${ }^{1}$ https://math.unice.fr/~jtoulisse/conf/sisteron.html
}

\section*{1 Harmonic maps}

Let $f: M \rightarrow N$ a smooth map between Riemannian manifolds. The main goal of this section is to explain the equivalence:
$$f \text { harmonic } \Leftrightarrow \Delta f=0 \Leftrightarrow \mathrm{~d}_{\nabla}^{*} \mathrm{~d} f=0 \Leftrightarrow \mathrm{~d} f \text { is a harmonic 1-form }$$

This requires introducing the basic tools and notions of differential geometry at play in the theory of harmonic maps between Riemannian manifolds. There are quite a few good references on the subject, such as [ES64], [EL83], [EL95b], [Jos08], [Xin96], [Chi13], [Jos17, Chap. 9]. I recommend refering to these for more developments and examples.
Remark 1.1. Contrary to many authors, we will avoid writing any formulas in local coordinates.
Remark 1.2. In all this report, $M$ is assumed connected and orientable, and given a fixed orientation. In particular, the volume density $v_{M}$ on $M$ can be identified to the volume form $\operatorname{vol}_{M}$. When needed, $M$ will also be assumed compact, e.g. for the last equivalence in (1).

\subsection*{1.1 Preliminary: connections in vector bundles}

Let $E \rightarrow M$ be a smooth vector bundle. We denote by $\Gamma(E)$ the space of smooth sections ${ }^{2}$. A (linear) connection in $E$ is a $\mathbb{R}$-linear map
$$\nabla: \Gamma(E) \rightarrow \Gamma\left(\mathrm{T}^{*} M \otimes E\right)$$
that satisfies the Leibniz rule $\nabla(f s)=\mathrm{d} f \otimes s+f \nabla s$. If $X \in \Gamma(\mathrm{~T} M)$ is any vector field, we denote $\nabla_{X} s$ the contraction of $\nabla s$ with $X$. It is a basic fact that the value of $\nabla_{X} s$ at $p \in M$ only depends on $s$ and $X_{p}$.

Given a smooth metric $g$ in $E$, i.e. a smooth section of $\left(E^{*}\right)^{\otimes 2}$ such that $g_{p}$ is an inner product in $E_{p}$ for all $p \in M$, a connection ∇ is compatible with $g$ (or preserves $g$ ) if $\nabla g=0$, where we abusively still denote by $\nabla$ the induced connection in $\left(E^{*}\right)^{\otimes 2}$. Concretely, this means that $X \cdot g\left(s_{1}, s_{2}\right)=g\left(\nabla_{X} s_{1}, s_{2}\right)+g\left(s_{1}, \nabla_{X} s_{2}\right)$.

When $E=\mathrm{T} M, \nabla$ is called torsion-free if $\nabla_{X} Y-\nabla_{Y} X=[X, Y]$. A smooth metric in T $M$ is known as a Remannian metric on $M$, and one can show that there exists a unique torsion-free connection ∇ compatible with $g$, called the Levi-Civita connection. This result is known as the fundamental theorem of Riemannian geometry and can be shown via the Koszul formula, see [Lee18] or [GHL04].
Remark 1.3. We will discuss curvature tensors in § 2.3.

\section*{$1.2 f$ is harmonic if and only if $\Delta f=0$}

Let $M$ and $N$ be Riemannian manifolds and $f: M \rightarrow N$ a smooth map. We indicate by $\nabla^{M}$ and $\nabla^{N}$ are the Levi-Civita connections of $M$ and $N$ respectively. Consider the pullback vector bundle
$$E:=f^{*}(\mathrm{~T} N) \rightarrow M$$
whose fiber above $x \in M$ is $\mathrm{T}_{f(x)} N . E$ admits a pullback connection $f^{*} \nabla^{N}$ uniquely determined by the relation $\left(f^{*} \nabla^{N}\right)_{X}\left(f^{*} s\right)=f^{*}\left(\nabla_{X}^{N} s\right)$ for any section $s \in \Gamma(\mathrm{~T} N)$. Henceforth we denote it $\nabla:=f^{*} \nabla^{N}$.

Consider the vector bundle $\mathrm{T}^{*} M \otimes E \rightarrow M$. It admits a tensor product connection $\bar{\nabla}$ induced from the dual connection of $\nabla^{M}$ in $\mathrm{T}^{*} M$ and the connection ∇ in $E$. Thus $\bar{\nabla}$ is a linear map:
$$\bar{\nabla}: \Gamma\left(\mathrm{T}^{*} M \otimes E\right) \rightarrow \Gamma\left(\mathrm{T}^{*} M \otimes \mathrm{~T}^{*} M \otimes E\right) .$$

Note that $\mathrm{d} f$, which is a linear map $\mathrm{T} M \rightarrow \mathrm{~T} N$, can be seen as a section of $\mathrm{T}^{*} M \otimes E$. It therefore makes sense to consider $\bar{\nabla}(\mathrm{d} f)$, it is an element of $\Gamma\left(\mathrm{T}^{*} M \otimes \mathrm{~T}^{*} M \otimes E\right)$. In other words it is a bilinear map $\mathrm{T} M \times \mathrm{T} M \rightarrow E$. By definition, this is the Hessian of $f$. Abusing notations, we denote it $\nabla^{2} f:=\bar{\nabla}(\mathrm{d} f)$.

\footnotetext{
${ }^{2}$ More generally, we use $\Gamma(\cdot)$ for the space of sections of any sheaf, but we will (barely) use this language only in § 6.
}

Proposition 1.4. The Hessian $\nabla^{2} f$ is symmetric as a bilinear map $\mathrm{T} M \times \mathrm{T} M \rightarrow \mathrm{~T} N$.
Proof. This is essentially due to the fact that $\nabla^{M}$ and $\nabla^{N}$ are torsion-free. Let $u, v$ be tangent vectors at some $x \in M$, let us show that $\nabla^{2} f(u, v)-\nabla^{2} f(v, u)=0$. By definition of the product connection $\bar{\nabla}$,
$$\nabla_{u}(\mathrm{~d} f(v))=\left(\bar{\nabla}_{u}(\mathrm{~d} f)\right)(v)+\mathrm{d} f\left(\nabla_{u}^{M} v\right) .$$
Note that for (2) to make sense, we locally extend $v$ as a vector field around $x$. We rewrite (2) as:
$$\nabla^{2} f(u, v)=\nabla_{\mathrm{d} f(u)}^{N}(\mathrm{~d} f(v))-\mathrm{d} f\left(\nabla_{u}^{M} v\right) .$$
Thus we can write
$$\nabla^{2} f(u, v)-\nabla^{2} f(v, u)=\left[\nabla_{\mathrm{d} f(u)}^{N}(\mathrm{~d} f(v))-\nabla_{\mathrm{d} f(v)}^{N}(\mathrm{~d} f(u))\right]-\left[\mathrm{d} f\left(\nabla_{u}^{M} v\right)-\mathrm{d} f\left(\nabla_{v}^{M} u\right)\right] .$$
Since $\nabla^{M}$ and $\nabla^{N}$ are both torsion-free, (3) is rewritten
$$\nabla^{2} f(u, v)-\nabla^{2} f(v, u)=[\mathrm{d} f(u), \mathrm{d} f(v)]-\mathrm{d} f([u, v]) .$$
This is zero by naturality of the Lie backet. \(\square\)

By definition, the Laplacian $\Delta f$ is the trace of the Hessian $\nabla^{2} f$. Recall that in the presence of an inner product, one can take the trace of any symmetric bilinear form: it is the trace of the associated self-adjoint endomorphism. Let us record these definitions:

Definition 1.5. The Hessian of $f$ is the symmetric bilinear map $\nabla^{2} f: \mathrm{T} M \times \mathrm{T} M \rightarrow \mathrm{~T} N$ defined by $\nabla^{2} f=\bar{\nabla}(\mathrm{d} f)$. The Laplacian $\Delta f$ is the section of $f^{*}(\mathrm{~T} N)$ defined by $\Delta f=\operatorname{tr}\left(\nabla^{2} f\right)$.

Remark 1.6. The Hessian $\nabla^{2} f$ generalizes both the Riemannian Hessian (for real-valued functions) and the second fundamental form (for isometric immersions). The Laplacian $\Delta f$ is called tension field by most authors and denoted $\tau(f)$, probably by herd behavior after Eells-Sampson [ES64].

It is perfectly fine to define a harmonic map by $\Delta f=0$ : the reader may take this definition home and skip the remainder of this subsection. For completeness, we recall below why $\Delta f=0$ is equivalent to $f$ being a critical point of the energy functional. Essentially, this is because $\operatorname{grad} \mathbf{E}(f)=-\Delta f$ (Remark 1.9).

Let $f: M \rightarrow N$ be a smooth map. If $M$ is not compact, the energy $\mathbf{E}(f)$ can be infinite, so instead we define it on compact subsets $K \subseteq M$ :
$$\mathbf{E}_{K}(f):=\frac{1}{2} \int_{K}\|\mathrm{~d} f\|^{2} \mathrm{~d} v_{M} .$$
In (4), $\|\mathrm{d} f\|$ is the Hilbert-Schmidt norm of $f$ : Given any linear map $L: V \rightarrow W$ between Euclidean vector spaces ( $V, g_{V}$ ) and ( $W, g_{W}$ ), the Hilbert-Schmidt norm is defined by $\|L\|^{2}=\operatorname{tr}_{g_{V}}\left(L^{*} g_{W}\right)$. It is the norm relative to the tensor inner product $g_{V}^{*} \otimes g_{W}$.

Now let $V$ be any infinitesimal variation of $f$, i.e. $V \in \Gamma\left(f^{*} \mathrm{~T} N\right)$, and let $\left(f_{t}\right)$ be any 1-parameter variation of $f$ with initial tangent vector $V$, i.e. $\left(f_{t}\right): I \times M \rightarrow N$ is smooth where $I \subseteq \mathbb{R}$ is an interval containing 0, $f_{0}=f$, and $\frac{\mathrm{d}}{\mathrm{d} t}{ }_{\mid t=0} f_{t}=V$. This variation is called supported in $K$ if $f_{t}=f$ outside of $K$.

Theorem 1.7 (First variational formula for the energy). For any variation $\left(f_{t}\right)$ of $f$ supported in a compact set $K$ and with initial tangent vector $V$,
$$\frac{\mathrm{d}}{\mathrm{~d} t}{ }_{\mid t=0} \mathbf{E}_{K}\left(f_{t}\right)=-\int_{K}\langle\Delta f, V\rangle_{N} \mathrm{~d} v_{M} .$$

Proof. The first variational formula for the energy is essentially an integration by parts. First write:
$$\frac{\mathrm{d}}{\mathrm{~d} t}{ }_{\mid t=0} \mathrm{E}_{K}\left(f_{t}\right)=\frac{1}{2} \int_{K} \frac{\mathrm{~d}}{\mathrm{~d} t}{ }_{\mid t=0} \operatorname{tr}\left\langle\mathrm{~d} f_{t}, \mathrm{~d} f_{t}\right\rangle_{N} \mathrm{~d} v_{M}=\int_{K} \operatorname{tr}\left\langle\left(\mathrm{~d} f, \nabla_{\frac{\partial}{\partial t}} \mathrm{~d} f_{t}\right)_{\mid t=0}\right\rangle_{N} \mathrm{~d} v_{M}$$
where ∇ here denotes the product connection in $\mathbb{R} \times M$. For this connection, one has $\nabla_{\frac{\partial}{\partial t}} \nabla_{u}=\nabla_{u} \nabla_{\frac{\partial}{\partial t}}$ for any $u \in \mathrm{~T} M$, from this observation one can derive that $\left(\nabla_{\frac{\partial}{\partial t}} \mathrm{~d} f_{t}\right)_{\mid t=0}=\nabla V$. We therefore get
$$\frac{\mathrm{d}}{\mathrm{~d} t}{ }_{\mid t=0} \mathrm{E}_{K}\left(f_{t}\right)=\int_{K} \operatorname{tr}\langle\mathrm{~d} f, \nabla V\rangle_{N} \mathrm{~d} v_{M} .$$
By compatibility of $\nabla$ with the metric in $N$, the function $\operatorname{tr}\langle\mathrm{d} f, \nabla V\rangle_{N}$ can be written as $-\left\langle\operatorname{tr} \nabla^{2} f, V\right\rangle_{N}$ plus a coexact function (namely $\mathrm{d}^{*}\langle\mathrm{~d} f(\cdot), V\rangle$ ), and is zero outside of $K$. Stokes's theorem thus yields:
$$\frac{\mathrm{d}}{\mathrm{~d} t}{ }_{\mid t=0} \mathrm{E}_{K}\left(f_{t}\right)=-\int_{K}\left\langle\operatorname{tr} \nabla^{2} f, V\right\rangle_{N} \mathrm{~d} v_{M}=-\int_{K}\langle\Delta f, V\rangle_{N} \mathrm{~d} v_{M} .$$ \(\square\)

Remark 1.8. The end of the proof can be rewritten more convincingly using the tools of § 1.3:
$$\begin{aligned}
\frac{\mathrm{d}}{\mathrm{~d} t}{ }_{\mid t=0} \mathrm{E}_{K}\left(f_{t}\right) & =\int_{K} \operatorname{tr}\langle\mathrm{~d} f, \nabla V\rangle_{N} \mathrm{~d} v_{M} \\
& =\langle\mathrm{d} f, \nabla V\rangle_{\mathrm{L}^{2}}=\left\langle\mathrm{d}_{\nabla}^{*} \mathrm{~d} f, V\right\rangle_{\mathrm{L}^{2}}=-\langle\Delta f, V\rangle_{\mathrm{L}^{2}} .
\end{aligned}$$
Remark 1.9. The first variational formula for the energy (5) says precisely that $\operatorname{grad} \mathbf{E}(f)=-\Delta f$ on $\mathcal{C}^{\infty}(M, N)$, where the gradient is taken with respect to the Riemannian metric defined by $\langle U, V\rangle=$ $\int_{M}\langle U, V\rangle_{N} \mathrm{~d} v_{M}$ for all $U, V \in \Gamma\left(f^{*} \mathrm{~T} N\right)$. Even though $\mathcal{C}^{\infty}(M, N)$ is infinite-dimensional, it can be equipped with a smooth structure making the previous statement precise (see [KM97, Chap. 42]).

One says that $f$ is a critical point of the energy functional if $\frac{\mathrm{d}}{\mathrm{d} t}{ }_{\mid t=0} \mathrm{E}_{K}\left(f_{t}\right)=0$ for any compact $K \subseteq M$ and for any variation $\left(f_{t}\right)$ of $f$ supported in $K$. According to the previous remark, this can be simply put: grad $\mathrm{E}(f)=0$. In any case, the next corollary follows immediately from Theorem 1.7:

Corollary 1.10. Let $f: M \rightarrow N$ be a smooth map between Riemannian manifolds.
$$f \text { is harmonic } \stackrel{\text { def }}{\Leftrightarrow} \quad f \text { is a critical point of the energy functional } \quad \Leftrightarrow \quad \Delta f=0 .$$

\section*{$1.3 f$ is harmonic if and only if $\mathrm{d}_{\nabla}^{*} \mathrm{~d} f=0$}

We have seen in § 1.2 that $\mathrm{d} f$ is a section of $\mathrm{T}^{*} M \otimes E$ where $E=f^{*} \mathrm{~T} N$. We then defined a connection $\bar{\nabla}$ in $\mathrm{T}^{*} M \otimes E$ and defined the Hessian of $f$ as $\bar{\nabla}(\mathrm{d} f)$. Alternatively, one could see $\mathrm{d} f$ as a 1 -form with values in $E$. More generally, we denote $\Omega^{k}(M, E)$ the space of smooth $k$-forms with values in $E$ :
$$\Omega^{k}(M, E):=\Gamma\left(\Lambda^{k} \mathrm{~T}^{*} M \otimes E\right) .$$
The connection ∇ in $E$ extends uniquely to a linear map
$$\mathrm{d}_{\nabla}: \Omega^{k}(M, E) \rightarrow \Omega^{k+1}(M, E)$$
called the exterior covariant derivative such that $\mathrm{d}_{\nabla}(\omega \otimes s)=\mathrm{d} \omega \otimes s+(-1)^{k} \omega \wedge \nabla s$.
Note that $\mathrm{d}_{\nabla}$ does not see the metric on $M$ : it only depends on $\nabla=f^{*} \nabla^{N}$. In particular, one can consider the 2 -form $d_{\nabla}(\mathrm{d} f) \in \Omega^{2}(M, E)$, which only depends on the metric on $N$, but we shall soon see that $d_{\nabla}(\mathrm{d} f)=0$.

On the other hand, there is a tensor product connection $\bar{\nabla}: \Gamma\left(\mathrm{T}^{*} M \otimes E\right) \rightarrow \Gamma\left(\mathrm{T}^{*} M \otimes \mathrm{~T}^{*} M \otimes E\right)$ and more generally a tensor product connection
$$\bar{\nabla}: \Gamma\left(\left(T^{*} M\right)^{\otimes k} \otimes E\right) \rightarrow \Gamma\left(\left(T^{*} M\right)^{\otimes(k+1)} \otimes E\right) .$$
Since $\Lambda^{k} \mathrm{~T}^{*} M$ is a subspace of $\left(T^{*} M\right)^{\otimes k}$ (namely the subspace of antisymmetric tensors), one can restrict $\bar{\nabla}$ to this subspace and get a map $\bar{\nabla}: \Omega^{k}(M, E) \rightarrow \Gamma\left(\left(T^{*} M\right)^{\otimes(k+1)} \otimes E\right)$.

Proposition 1.11. $\mathrm{d}_{\nabla}: \Omega^{k}(M, E) \rightarrow \Omega^{k+1}(M, E)$ is the antisymmetrization of the restriction of $\bar{\nabla}$ to $\Omega^{k}(M, E)$. Concretely, given $\alpha \in \Omega^{k}(M, E)$ :
$$\mathrm{d}_{\nabla} \alpha\left(u_{0}, \ldots, u_{k}\right)=\sum_{s=0}^{k}(-1)^{s}\left(\bar{\nabla}_{u_{s}} \alpha\right)\left(u_{0}, \ldots, \widehat{u}_{s}, \ldots, u_{k}\right)$$
where the notation $\widehat{u_{s}}$ means that $u_{s}$ is omitted. For example ( $k=1$ ):
$$\left(\mathrm{d}_{\nabla} \alpha\right)(u, v)=(\bar{\nabla} \alpha)(u, v)-(\bar{\nabla} \alpha)(v, u)$$
Proof. It suffices that the antisymmetrization of $\bar{\nabla}$ verifies the characterization of the exterior covariant derivative, which is readily checked. \(\square\)

Proposition 1.12. For any smooth $f: M \rightarrow N, \mathrm{~d}_{\nabla}(\mathrm{d} f)=0$.
Proof. By Proposition 1.11, $\mathrm{d}_{\nabla}(\mathrm{d} f)$ is the antisymmetrization of $\bar{\nabla}(\mathrm{d} f)$. But recall that the Hessian $\nabla^{2} f:=\bar{\nabla}(\mathrm{d} f)$ is symmetric: Proposition 1.4. \(\square\)

Proposition 1.12 says that $\mathrm{d} f$ is always a closed 1 -form. Let us show that $f$ is harmonic if and only if $\mathrm{d} f$ is co-closed. First we need to introduce the Hodge star and the codifferential.

Definition 1.13. Let $M$ be a Riemannian manifold and let $E \rightarrow M$ be a smooth vector bundle with a metric $\langle\cdot, \cdot\rangle_{E}$.
\begin{itemize}
\item[-] The mixed product of $E$-valued differential forms is the operation:
$$\begin{aligned}
\Omega^{k}(M, E) \times \Omega^{l}(M, E) & \rightarrow \Omega^{k+l}(M, \mathbb{R}) \\
(\alpha, \beta) & \mapsto\langle\alpha \wedge \beta\rangle
\end{aligned}$$
defined by $\left\langle\omega_{1} \otimes s_{1} \wedge \omega_{2} \otimes s_{2}\right\rangle=\omega_{1} \wedge \omega_{2}\left\langle s_{1}, s_{2}\right\rangle_{E}$.
\item[-] The pointwise inner product on $\Omega^{k}(M, E)$ is the operation:
$$\begin{aligned}
\Omega^{k}(M, E) \times \Omega^{k}(M, E) & \rightarrow \mathcal{C}^{\infty}(M, \mathbb{R}) \\
(\alpha, \beta) & \mapsto\langle\alpha, \beta\rangle
\end{aligned}$$
defined by $\left\langle\omega_{1} \otimes s_{1} \wedge \omega_{2} \otimes s_{2}\right\rangle=\left\langle\omega_{1}, \omega_{2}\right\rangle_{M}\left\langle s_{1}, s_{2}\right\rangle_{E}$, where $\langle\cdot, \cdot\rangle_{M}$ is the inner product in $\Lambda^{k} \mathrm{~T}_{x}^{*} M$ induced from the inner product $\langle\cdot, \cdot\rangle_{M}$ in $\mathrm{T}_{x} M$.
\item[-] The inner product in $\Omega^{k}(M, E)$ is the operation:
$$\begin{aligned}
\Omega^{k}(M, E) \times \Omega^{k}(M, E) & \rightarrow \mathbb{R} \\
(\alpha, \beta) & \mapsto\langle\alpha, \beta\rangle_{\mathrm{L}^{2}}:=\int_{M}\langle\alpha, \beta\rangle \mathrm{d} v_{M} .
\end{aligned}$$
For this definition we assume that $M$ is compact or $\alpha$ and $\beta$ both have compact support.
\end{itemize}
\begin{itemize}
\item[-] The Hodge star in $\Omega^{\bullet}(M, E)$ is the operation:
$$\begin{aligned}
\Omega^{k}(M, E) & \rightarrow \Omega^{m-k}(M, E) \quad(m=\operatorname{dim} M) \\
\beta & \mapsto * \beta
\end{aligned}$$
characterized by the identity:
$$\langle\alpha \wedge * \beta\rangle=\langle\alpha, \beta\rangle \operatorname{vol}_{M} .$$
\end{itemize}

The following proposition is elementary and its proof is left to the reader:
Proposition 1.14. The Hodge star * in $\Omega^{\bullet}(M, E)$ (cf Definition 1.13) is well-defined. Moreover:
\begin{itemize}
\item[(i)] For any $\alpha=\omega \otimes s \in \Omega^{k}(M, E), * \alpha=(* \omega) \otimes s$, where $* \omega$ is the standard Hodge star for real-valued differential forms (i.e. take Definition 1.13 with $E=\mathbb{R}$ ).
\item[(ii)] The Hodge star is a pointwise linear isometry: $\langle * \alpha, * \beta\rangle=\langle\alpha, \beta\rangle$.
\item[(iii)] The Hodge star is an involution up to sign: for all $\alpha \in \Omega^{k}(M, R), * * \alpha=(-1)^{k(m-k)} \alpha$.
\end{itemize}

We are now ready to define the codifferential and Hodge Laplacian:
Definition 1.15. Let $M$ be a Riemannian manifold, let $E \rightarrow M$ be a vector bundle with a metric $\langle\cdot, \cdot\rangle_{E}$ and with a connection ∇ preserving the metric.
\begin{itemize}
\item[-] The codifferential in $\Omega^{\bullet}(M, E)$ is the operation:
$$\begin{aligned}
\mathrm{d}_{\nabla}^{*}: \Omega^{k}(M, E) & \rightarrow \Omega^{k-1}(M, E) \\
\alpha & \mapsto \mathrm{d}_{\nabla}^{*} \alpha:=(-1)^{m(k-1)+1} * \mathrm{~d}_{\nabla} * \alpha .
\end{aligned}$$
\item[-] The Hodge Laplacian in $\Omega^{k}(M, E)$ is the operation:
$$\begin{aligned}
\Delta: \Omega^{k}(M, E) & \rightarrow \Omega^{k}(M, E) \\
\alpha & \mapsto \Delta \alpha:=\mathrm{d}_{\nabla}^{*} \mathrm{~d}_{\nabla} \alpha+\mathrm{d}_{\nabla} \mathrm{d}_{\nabla}^{*} \alpha .
\end{aligned}$$
A $k$-form $\alpha \in \Omega^{k}(M, E)$ is called harmonic if $\Delta \alpha=0$.
\end{itemize}

The next proposition is both elementary and crucial:
Proposition 1.16. Let $M$ be a Riemannian manifold, let $E \rightarrow M$ be a vector bundle with a metric $\langle\cdot, \cdot\rangle_{E}$ and with a connection ∇ preserving the metric.
\begin{itemize}
\item[(i)] The codifferential $\mathrm{d}_{\nabla}^{*}$ is the formal adjoint of the differential $\mathrm{d}_{\nabla}$ :
$$\left\langle\mathrm{d}_{\nabla} \alpha, \beta\right\rangle_{\mathrm{L}^{2}}=\left\langle\alpha, \mathrm{d}_{\nabla}^{*} \beta\right\rangle_{\mathrm{L}^{2}}$$
whenever this is well-defined ( $\operatorname{deg} \beta=\operatorname{deg} \alpha+1$ and $\alpha$ or $\beta$ has compact support).
\item[(ii)] $A$ differential form $\alpha$ with compact support is harmonic if and only if it is closed and co-closed:
$$\Delta \alpha=0 \quad \Leftrightarrow \quad \mathrm{~d}_{\nabla} \alpha=0 \text { and } \mathrm{d}_{\nabla}^{*} \alpha=0 .$$
\end{itemize}
Proof. For (i) we write, given $\alpha \in \Omega^{k}(M, E)$ and $\beta \in \Omega^{k+1}(M, E)$, both with compact support:
$$\begin{aligned}
\left\langle\alpha, \mathrm{d}_{\nabla}^{*} \beta\right\rangle \operatorname{vol}_{M} & =\left\langle\alpha \wedge *\left(\mathrm{~d}_{\nabla}^{*} \beta\right)\right\rangle \\
& =\left\langle\alpha \wedge *\left[(-1)^{m k+1} * \mathrm{~d}_{\nabla} * \beta\right]\right\rangle \\
& =\left\langle\alpha \wedge(-1)^{m k+1}(-1)^{(m-k) k} \mathrm{~d}_{\nabla} * \beta\right\rangle \\
& =(-1)^{k+1}\left\langle\alpha \wedge \mathrm{~d}_{\nabla} * \beta\right\rangle .
\end{aligned}$$

Now write
$$\begin{aligned}
\mathrm{d}\langle\alpha \wedge * \beta\rangle & =\left\langle\mathrm{d}_{\nabla} \alpha \wedge * \beta\right\rangle+(-1)^{k}\left\langle\alpha \wedge \mathrm{~d}_{\nabla} * \beta\right\rangle \\
& =\left\langle\mathrm{d}_{\nabla} \alpha, \beta\right\rangle \operatorname{vol}_{M}-\left\langle\alpha, \mathrm{d}_{\nabla}^{*} \beta\right\rangle \operatorname{vol}_{M}
\end{aligned}$$
and integrate over $M$ (use Stokes's theorem) to find (i). Now (ii) follows easily:
$$\begin{aligned}
\langle\Delta \alpha, \alpha\rangle_{\mathrm{L}^{2}} & =\left\langle\mathrm{d}_{\nabla}^{*} \mathrm{~d}_{\nabla} \alpha, \alpha\right\rangle_{\mathrm{L}^{2}}+\left\langle\mathrm{d}_{\nabla} \mathrm{d}_{\nabla}^{*} \alpha, \alpha\right\rangle_{\mathrm{L}^{2}} \\
& =\left\langle\mathrm{d}_{\nabla} \alpha, \mathrm{d}_{\nabla} \alpha\right\rangle_{\mathrm{L}^{2}}+\left\langle\mathrm{d}_{\nabla}^{*} \alpha, \mathrm{~d}_{\nabla}^{*} \alpha\right\rangle_{\mathrm{L}^{2}}
\end{aligned}$$
and observe that $\left\langle\mathrm{d}_{\nabla} \alpha, \mathrm{d}_{\nabla} \alpha\right\rangle \geqslant 0$ with equality if and only if $\mathrm{d}_{\nabla} \alpha=0$, same for $\left\langle\mathrm{d}_{\nabla}^{*} \alpha, \mathrm{~d}_{\nabla}^{*} \alpha\right\rangle$. \(\square\)

Out of interest, let us mention the main theorem of Hodge theory in the classical case $E=\mathbb{R}$ :
Theorem 1.17. Let $M$ be a closed Riemannian manifold. There is an orthogonal decomposition
$$\Omega^{k}(M, \mathbb{R})=\underbrace{\overbrace{\mathcal{H}^{k}(M, \mathbb{R})}^{\operatorname{ker} \Delta} \oplus \overbrace{\operatorname{Im}(\mathrm{d})}^{\operatorname{Im} \Delta} \oplus \operatorname{Im}\left(\mathrm{d}^{*}\right)}_{\operatorname{ker}(d)} .$$
Moreover, the space of harmonic $k$-forms $\mathcal{H}^{k}(M, \mathbb{R}):=\operatorname{ker} \Delta$ is finite-dimensional.
Proof sketch. The proof relies on the finiteness theorem, which says that if $P$ is an elliptic operator in a vector bundle $E$, then $\operatorname{ker} P$ is finite-dimensional and there is an orthogonal decomposition $\Gamma(E)=$ $\operatorname{ker} P \oplus \operatorname{Im} P^{*}$ (see [Ber+02, Thm. 3.10]). Since $\Delta$ is elliptic and self-adjoint, we obtain $\Omega^{k}(M, \mathbb{R})=$ $\operatorname{ker} \Delta \oplus \operatorname{Im} \Delta$ as expected. To show that $\operatorname{Im} \Delta=\operatorname{Im}(\mathrm{d}) \oplus \operatorname{Im}\left(\mathrm{d}^{*}\right)$, one argues that $\operatorname{Im}(\mathrm{d})$ and $\operatorname{Im}\left(\mathrm{d}^{*}\right)$ are orthogonal (because $\mathrm{d} \circ \mathrm{d}=0$ ); they are also orthogonal to ker $\Delta$ therefore contained in $\operatorname{Im} \Delta$, on the other hand it is trivial that $\operatorname{Im} \Delta \subseteq \operatorname{Im}(\mathrm{d})+\operatorname{Im}\left(\mathrm{d}^{*}\right)$. Finally, $\mathcal{H}^{k}(M, \mathbb{R}) \oplus \operatorname{Im}(\mathrm{d})=\operatorname{ker}(\mathrm{d})$ since the inclusion $\subseteq$ is clear on the one hand, and ker(d) is orthogonal to $\operatorname{Im}\left(\mathrm{d}^{*}\right)$ on the other. \(\square\)

Corollary 1.18. The de Rham cohomology space $\mathrm{H}_{d R}^{k}(M, \mathbb{R})$ is isomorphic to $\mathcal{H}^{k}(M, \mathbb{R})$.
Remark 1.19. The Hodge decomposition and the isomorphism $H_{\mathrm{dR}}^{k} \approx \mathcal{H}^{k}$ generalize to forms with values in a vector bundle $E$ with a metric and a flat connection ∇ preserving the metric: the proof is the same. Note that if $\nabla$ is not flat, the de Rham cohomology is not even well-defined ${ }^{3}$.

Now let us come back to the setting where $E=f^{*} \mathrm{~T} N$ and $\nabla=f^{*} \nabla^{N}$. We saw that $\mathrm{d} f \in \Omega^{1}(M, E)$ is always a closed 1-form (Proposition 1.12). Weighing in Proposition 1.16 (ii), we find:

Proposition 1.20. If $M$ is compact, $\mathrm{d} f \in \Omega^{1}(M, E)$ is harmonic if and only if $\mathrm{d}_{\nabla}^{*} \mathrm{~d} f=0$.
Note that $\mathrm{d}_{\nabla}^{*} \mathrm{~d} f$ is an element of $\Omega^{0}(E)$, i.e. a section of $f^{*}(\mathrm{~T} N)$, just like $\Delta f$.
Proposition 1.21. For any smooth map $f: M \rightarrow N, \mathrm{~d}_{\nabla}^{*} \mathrm{~d} f=-\Delta f$.
Proof. This is a special case of the formula $\mathrm{d}_{\nabla}^{*} \alpha=-\operatorname{tr}_{12} \bar{\nabla} \alpha$ for any $\alpha \in \Omega^{k}(M, E)$, which is the $\mathrm{d}_{\nabla}^{*}$-analogue of (6). More concretely:
$$\mathrm{d}_{\nabla}^{*} \alpha\left(u_{1}, \ldots, u_{k-1}\right)=-\sum_{j=1}^{m} \bar{\nabla}_{e_{j}} \alpha\left(e_{j}, u_{1}, \ldots, u_{k-1}\right)$$
where $\left(e_{j}\right)_{1 \leqslant j \leqslant m}$ is any local orthonormal frame field on $M$. One can prove this formula by verifying that using it as a definition for $\mathrm{d}_{\nabla}^{*} \alpha$, it does give a formal adjoint of $\mathrm{d}_{\nabla}$ : check that $\left\langle\mathrm{d}_{\nabla}^{*} \alpha, \beta\right\rangle$ is pointwise equal to $\left\langle\alpha, \mathrm{d}_{\nabla} \beta\right\rangle$ plus a globally defined co-exact function. Alternatively, a direct proof can be given using normal coordinates: see [EL83, Lemma 1.20]. \(\square\)

\footnotetext{
${ }^{3}$ In general, $d_{\nabla}^{2}=\cdot \wedge F^{\nabla}$ on $\Omega^{k}(M, E)$, where $F^{\nabla}$ is the curvature of ∇ (see § 2.3). In particular, $F^{\nabla}=0$ if and only if the de Rham complex $\left(\Omega^{\cdot}(M, E), \mathrm{d}_{\nabla}\right)$ is indeed a complex i.e. $\mathrm{d}_{\nabla}^{2}=0$, which is necessary and sufficient to define its cohomology.
}

Remark 1.22. The formula $\mathrm{d}_{\nabla}^{*} \alpha=-\operatorname{tr}_{12} \bar{\nabla} \alpha$ says that $\mathrm{d}_{\nabla}^{*}=-\operatorname{div}$, where div is the divergence operator suitably interpreted on $\Omega^{k}(M, E)$.
Remark 1.23. Proposition 1.21 holds even if $M$ is not compact: the proof above shows that $\left\langle\mathrm{d}_{\nabla}^{*} \alpha+\right.$ $\left.\operatorname{tr}_{12} \bar{\nabla} \alpha, \beta\right\rangle_{\mathrm{L}^{2}}=0$ for any compactly supported $\beta$, but this is enough to conclude.
Remark 1.24. Warning! There is a sign discrepancy between the Laplacian of Definition 1.5 and the Hodge Laplacian: when $N=\mathbb{R}$, both operators make sense on $\Omega^{0}(M, \mathbb{R})$, and differ by a minus sign. This is the well-known disagreement between the "analyst's Laplacian" and the "geometer's Laplacian".

We can now wrap up:
Theorem 1.25. Let $f: M \rightarrow N$ be a smooth map between Riemannian manifolds.
$$f \text { harmonic } \Leftrightarrow \quad \Delta f=0 \quad \Leftrightarrow \quad \mathrm{~d}_{\nabla}^{*} \mathrm{~d} f=0 \quad \Leftrightarrow \quad \mathrm{~d} f \text { is a harmonic 1-form. }$$
Remark 1.26. $M$ must be assumed compact for the last equivalence, to apply Proposition 1.16 (ii). Otherwise it is not always true that $\Delta f=0$ if $\Delta \mathrm{d} f=0$ : take $M=\mathbb{R}^{m}, N=\mathbb{R}$, and $f\left(x_{1}, \ldots, x_{m}\right)=x_{1}^{2}$.

\section*{2 The Bochner technique}

This section is not essential for our exposition so the reader in a hurry may skip it. We explain the Bochner and Weitzenböck formulas and how it is typically used to produce rigidity results. The theorem of Siu and Sampson (§ 4) is a variation of this technique when the domain manifold is Kähler.

\subsection*{2.1 Bochner formula}

The classical Bochner formula for a smooth function $f: M \rightarrow \mathbb{R}$ is
$$\frac{1}{2} \Delta\|\nabla f\|^{2}-\langle\nabla f, \nabla \Delta f\rangle=\left\|\nabla^{2} f\right\|^{2}+\operatorname{Ric}^{M}(\nabla f, \nabla f) .$$
In this formula, $\nabla f$ is an alias for either $\mathrm{d} f$ or $\operatorname{grad} f$ (one can harmlessly switch using metric duality). Eells and Sampson [ES64] generalized the formula for a smooth function $f: M \rightarrow N$ :
$$\frac{1}{2} \Delta\|\nabla f\|^{2}-\langle\nabla f, \nabla \Delta f\rangle=\left\|\nabla^{2} f\right\|^{2}+\operatorname{Ric}^{M}\left(\langle\nabla f, \nabla f\rangle_{N}\right)-R^{N}\left(\langle\nabla f \otimes \nabla f\rangle_{M},\langle\nabla f \otimes \nabla f\rangle_{M}\right) .$$

Let us clarify the notations:
\begin{itemize}
\item[-] $\langle\nabla f, \nabla \Delta f\rangle$ is the pointwise inner product in $\Omega^{1}(M, E)$.
\item[-] $\langle\nabla f, \nabla f\rangle_{N}$ is the section of $\mathrm{T} M \otimes \mathrm{~T} M$ obtained from pairing $\nabla f$ to itself using $\langle\cdot, \cdot\rangle_{N}$.
\item[-] $\langle\nabla f \otimes \nabla f\rangle_{M}$ is the section of $\mathrm{T} N \otimes \mathrm{~T} N$ obtained from tensoring $\nabla f$ with itself using $\langle\cdot, \cdot\rangle_{M}$.
\item[-] $R^{N}$ is the curvature operator in $N$ : see § 2.3.
\end{itemize}
We shall prove the Bochner formula in § 2.4 via the Weitzenböck formula.

\subsection*{2.2 Application of the Bochner formula}

Before clarifying curvature tensors (§ 2.3) and proving the Weitzenböck and Bochner formulas (§ 2.4), let us explain the importance of the Bochner formula for the study of harmonic maps.

\subsection*{2.2.1 Rigidity}

The key idea is to require the appropriate curvature assumptions so that one controls the sign of all terms on the right-hand side of the Bochner formula (9). Ideally: $M$ has nonnegative Ricci curvature and $N$ has nonpositive sectional curvature. In that case, all these terms are pointwise nonnegative. Assuming $M$ is compact and $f$ is harmonic, one then integrates (9) to obtain rigidity results. Indeed, we have $\Delta f=0$ when $f$ is harmonic, and $\Delta\|\nabla f\|^{2}$ always integrates to zero. Let us recall why:

Lemma 2.1. Let $M$ be a compact Riemannian manifold. For any $u \in \mathcal{C}^{\infty}(M, \mathbb{R}), \int_{M} \Delta u \mathrm{~d} v_{M}=0$.
Proof. Recall that a differential form of top degree $\omega$ has zero integral if and only if it is exact. Using the definition of the codifferential d* and recalling that $* 1=\operatorname{vol}_{M}$, this amounts to saying that $u \operatorname{vol}_{M}$ has zero integral if and only if $u$ is co-exact. But $\Delta u=\mathrm{d}^{*} \mathrm{~d} u$ is obviously co-exact. \(\square\)

Remark 2.2. Alternatively, $\int_{M} \Delta u \mathrm{~d} v_{M}=0$ follows from the divergence theorem, recalling that $\Delta u=$ $\operatorname{div}(\operatorname{grad} u)$.

Let us summarize the previous observations:
$$\underbrace{\frac{1}{2} \Delta\|\nabla f\|^{2}}_{\text {integral }=0}-\underbrace{\langle\nabla f, \nabla \Delta f\rangle}_{0 \text { if } f \text { harmonic }}=\underbrace{\left\|\nabla^{2} f\right\|^{2}}_{\geqslant 0 \text { pointwise }}+\underbrace{\operatorname{Ric}^{M}\left(\langle\nabla f, \nabla f\rangle_{N}\right)}_{\geqslant 0 \text { pointwise }} \underbrace{-R^{N}\left(\langle\nabla f \otimes \nabla f\rangle_{M},\langle\nabla f \otimes \nabla f\rangle_{M}\right)}_{\geqslant 0 \text { pointwise }}$$

Integrating over $M$, under the previous curvature assumptions, if $f$ is harmonic then each of the three terms on the right-hand side must be identically zero. In particular $\nabla^{2} f=0$ everywhere: $f$ is totally geodesic. Furthermore, the vanishing of the curvature terms easily yields:

Theorem 2.3 (Eells-Sampson's strong rigidity theorem). Let $f: M \rightarrow N$ be a smooth harmonic map between Riemannian manifolds. Assume $M$ is compact and has nonnegative Ricci curvature and $N$ has nonpositive sectional curvature. Then $f$ is totally geodesic. Moreover:
\begin{itemize}
\item[(i)] If $\mathrm{Ric}^{M}$ is not identically zero, then $f$ is constant.
\item[(ii)] If $N$ has negative sectional curvature, then $f$ is constant or maps to a closed geodesic.
\end{itemize}

\subsection*{2.2.2 Heat flow}

The Bochner formula is also key for the heat flow technique developed by Eells-Sampson [ES64] and successfully to adapted to various settings by many authors. Let us quickly explain this, although we will not directly use the heat flow in this report.

Assume $\left(f_{t}\right)_{t \in I}$ is a 1-parameter family of maps $M \rightarrow N$ satisfying the heat flow equation:
$$\partial_{t} f_{t}=\Delta f_{t} .$$
One can show local existence of this flow given $f_{0}$ using classical nonlinear parabolic PDE techniques (linearization of the operator $\partial_{t}-\Delta$ and implicit function theorem, see e.g. [Jos84]). Note that the heat flow is just the gradient flow for the energy functional, since $\operatorname{grad} \mathbf{E}(f)=-\Delta(f)$ (Remark 1.9).

Assume $N$ is nonpositively curved. The second variational formula for the energy shows that it is a convex functional (see e.g. [GLM18, Prop. 3.4]), making it reasonable to expect that the heat flow might converge to an energy minimizer. When $M$ and $N$ are both compact, one can try proving convergence of the flow (maybe up to subsequence) using some compactness argument such as the Arzelà-Ascoli theorem. However there are significant obstacles to overcome, such as proving the long-time existence of the heat flow and equicontinuity of $\left(f_{t}\right)$. The Bochner formula shows that $\left\|\nabla f_{t}(x)\right\|$ is uniformly bounded in time and space, solving both these obstacles.

Let us give a some details. Denote $e\left(f_{t}\right):=\frac{1}{2}\left\|\mathrm{~d} f_{t}\right\|^{2}$ the energy density of $f_{t}$. If $\left(f_{t}\right)_{t \in I}$ satisfies (10), then $\partial_{t} e\left(f_{t}\right)=\left\langle\nabla f_{t}, \nabla \Delta f_{t}\right\rangle$. Assuming $\operatorname{Ric}^{M}$ is bounded below by $K \in \mathbb{R}$ (e.g. $M$ is compact) and $N$ has nonpositive sectional curvature, the Bochner formula (9) yields:
$$\left(\partial_{t}-\Delta\right) e\left(f_{t}\right) \leqslant K^{\prime} e\left(f_{t}\right)$$
where $K^{\prime}=-2 K$. By a generalized mean value property (more precisely: Moser's Harnack inequality for subsolutions of the heat equation [Mos64][LW08, Lemma 5.3.4]), this implies
$$\left\|e\left(f_{t}\right)\right\|_{\infty} \leqslant C \mathbf{E}\left(f_{0}\right)$$
for some constant $C>0$. In other words, the family $\left(f_{t}\right)$ has a uniformly bounded gradient. It obviously implies that it is equicontinuous, but also long-time existence of the heat flow (when $N$ is compact) by a standard "blow up in finite time" argument for nonlinear parabolic PDEs. Thus one can extract $t_{k} \rightarrow+\infty$ such that $f_{t_{k}}$ converges uniformly to some map $f_{\infty}$. There still remains work to do, involving regularity theory and Sobolev spaces, to show that $f_{\infty}$ is a smooth harmonic map, see e.g. [Jos84] for details. Let us record the following conclusion:

Theorem 2.4 (Eells-Sampson's existence theorem). Let $f: M \rightarrow N$ be smooth, where $M$ and $N$ are compact Riemannian manifolds and $N$ has nonpositive sectional curvature. Then $f$ is homotopic to a smooth harmonic map.

\subsection*{2.3 Curvature tensors}

Now is a good time to clarify our notations and conventions for curvature tensors.
Given a vector bundle $E \rightarrow M$ with a connection ∇ , it is easy to check that the linear map $\mathrm{d}_{\nabla}^{2}: \Omega^{0}(M, E) \rightarrow \Omega^{2}(M, E)$ is tensorial, i.e. $\mathcal{C}^{\infty}(M, \mathbb{R})$-linear. Therefore there exists a tensor field $F^{\nabla} \in \Omega^{2}(\operatorname{End} E)$ such that $\mathrm{d}_{\nabla}^{2}(s)=F^{\nabla} s$. The operator $F^{\nabla}$ is called the curvature of ∇ . Recalling that $\mathrm{d}_{\nabla}$ is the antisymmetrization of ∇ as in (7), $F^{\nabla}$ is concretely given by
$$F^{\nabla}(X, Y) s=\nabla_{X, Y}^{2} s-\nabla_{Y, X}^{2} s=\nabla_{X} \nabla_{Y} s-\nabla_{Y} \nabla_{X} s-\nabla_{[X, Y]} s$$
where ∇ is assumed torsion-free for the second identity. More elegantly: $F^{\nabla}(X, Y)=\left[\nabla_{X}, \nabla_{Y}\right]-\nabla_{[X, Y]}$.

\subsection*{2.3.1 Riemannian curvature tensors}

If $M$ is a Riemannian manifold, the Riemann curvature tensor $R:=F^{\nabla} \in \Gamma\left(\Lambda^{2} \mathrm{~T}^{*} M \otimes \operatorname{End}(\mathrm{~T} M)\right)$ is the curvature of the Levi-Civita connection ∇ :
$$R(X, Y) Z=\nabla_{X} \nabla_{Y} Z-\nabla_{Y} \nabla_{X} Z-\nabla_{[X, Y]} Z .$$
The purely covariant version of the Riemann curvature tensor is the 4-covariant tensor field:
$$R(X, Y, Z, W)=-\langle R(X, Y) Z, W\rangle$$
and the curvature operator is the symmetric bilinear form on $\otimes^{2} \mathrm{~T} M$ defined by:
$$Q(X \otimes Y, Z \otimes W)=R(X, Y, Z, W)$$
for decomposable tensors, and extended bilinearly to $\bigotimes^{2} \mathrm{~T} M$ (it can also be defined as a bilinear form on $\Lambda^{2} \mathrm{~T} M$ or as an endomorphism of $\otimes^{2} \mathrm{~T} M$ or $\Lambda^{2} \mathrm{~T} M$ ). The sectional curvature $K$ is
$$K(X, Y)=\frac{Q(X \otimes Y, X \otimes Y)}{\|X \wedge Y\|^{2}}$$
with $\|X \wedge Y\|^{2}=\|X\|^{2}\|Y\|^{2}-\langle X, Y\rangle^{2}$. It is defined for any two linearly independent vectors $X$ and $Y$ with same basepoint and only depends on the plane spanned by $X$ and $Y$. Finally, the Ricci curvature tensor is the symmetric bilinear form on $\mathrm{T} M$ defined by
$$\operatorname{Ric}(X, Y)=\operatorname{tr} R(X, \cdot, Y, \cdot)=\sum_{j=1}^{n} R\left(X, e_{j}, Y, e_{j}\right)$$
for any local orthonormal frame field $\left(e_{j}\right)_{1 \leqslant j \leqslant n}$.
Remark 2.5. It is certainly questionable to define the purely covariant Riemann tensor with a minus sign as in (11) and still use the same letter $R$ ! The main reason for this choice is nicer formulas for sectional curvatures. Some authors introduce the minus sign earlier (e.g. $R=-d_{\nabla}^{2}$ ), others later (e.g. $K(X, Y)=-\frac{R(X, Y, X, Y)}{\|X \wedge Y\|^{2}}$ ), but no solution is entirely satisfactory. The only unanimous convention is sectional curvature: it should agree with the Gaussian curvature when $\operatorname{dim} M=2$.

\subsection*{2.3.2 Curvature tensors in $\Omega^{k}(M, E)$}

In order to express the Weitzenböck formula, we generalize the Riemann and Ricci curvature to bundles of vector-valued forms. Let $M$ be a Riemannian manifold, let $E \rightarrow M$ be a vector bundle with a metric $\langle\cdot, \cdot\rangle_{E}$ and a connection ∇ preserving the metric. Recall that there is a product connection $\bar{\nabla}$ in the bundle $\Lambda^{k} \mathrm{~T}^{*} M \otimes E$. By definition, the curvature of that bundle is the curvature of $\bar{\nabla}$. Explicitly:
$$(R(X, Y) \alpha)\left(u_{1}, \ldots, u_{k}\right)=F^{\nabla}(X, Y)\left(\alpha\left(u_{1}, \ldots, u_{k}\right)\right)-\sum_{j=1}^{k} \alpha\left(u_{1}, \ldots, R^{M}(X, Y) u_{j}, \ldots, u_{k}\right) .$$
We then define the Ricci (or Bochner, or Weitzenböck) operator $S: \Omega^{k}(M, E) \rightarrow \Omega^{k}(M, E)$ :
$$S(\alpha)\left(u_{1}, \ldots, u_{k}\right)=\sum_{s=1}^{k}(-1)^{s-1} \operatorname{tr}\left[\left(R\left(\cdot, u_{s}\right) \alpha\right)\left(\cdot, u_{1}, \ldots, \widehat{u_{s}}, \ldots, u_{k}\right)\right]$$
Note that when $E=\mathbb{R}$ is the trivial flat bundle and $k=1, S(\alpha)=\operatorname{Ric}^{M}(\alpha)$, interpreting $\operatorname{Ric}^{M}$ as a self-adjoint endomorphism of $\Omega^{1}(M, \mathbb{R})$ by metric duality.

\subsection*{2.4 Weitzenböck and Bochner formulas}

We conclude with the neat proof of the Bochner formula via the Weitzenböck formula.
Let $M$ be a Riemannian manifold, let $E \rightarrow M$ be a vector bundle with a metric $\langle\cdot, \cdot\rangle_{E}$ and with a connection ∇ preserving the metric. In $\Omega^{k}(M, E)$ we have two Laplacian operators:
\begin{itemize}
\item[-] The Hodge Laplacian $\Delta$ introduced in Definition 1.15.
\item[-] The connection Laplacian (or trace Laplacian or rough Laplacian) $\operatorname{tr}\left(\bar{\nabla}^{2}\right)$, which can be seens as the natural extension of the Laplacian on functions (see Definition 1.5).
\end{itemize}
Remark 2.6. The connection Laplacian $\operatorname{tr}\left(\nabla^{2}\right)$ is well-defined in $\Gamma(E)$ for any vector bundle $E$ with a metric and a compatible connection ∇ . Some call Bochner Laplacian the operator $\nabla^{*} \nabla$ where $\nabla^{*}$ is the formal adjoint of $\nabla$. Since $\nabla^{*}=-\operatorname{tr} \nabla$, the Bochner Laplacian is simply minus the connection Laplacian.

The Weitzenböck formula relates both Laplacian operators:
Theorem 2.7 (Weitzenböck formula). For all $\alpha \in \Omega^{k}(M, E)$,
$$\Delta \alpha=-\operatorname{tr}\left(\bar{\nabla}^{2} \alpha\right)+S(\alpha) .$$

Remark 2.8. For $k=0$, the Weitzenböck formula reduces to Proposition 1.21, since $S=0$. Be wary that the usual Laplacian (i.e. connection Laplacian) and the Hodge Laplacian differ by a minus sign!

For $k \geqslant 1$, the Weitzenböck formula is proven by direct computation. It is written e.g. in [Xin96, Prop 1.3.4]; also refer to [EL83, (1.29)] for this and more historical references. For readers curious about the full extent of Weitzenböck formulas, we refer to [Nic13] as a starting point.

Corollary 2.9 (Bochner formula in $\Omega^{k}(M, E)$ ). For all $\alpha \in \Omega^{k}(M, E)$,
$$\frac{1}{2} \Delta\|\alpha\|^{2}+\langle\Delta \alpha, \alpha\rangle=\|\nabla \alpha\|^{2}+\langle S(\alpha), \alpha\rangle$$
Proof.
$$\begin{aligned}
\frac{1}{2} \Delta\|\alpha\|^{2} & =\frac{1}{2} \operatorname{tr} \nabla^{2}\langle\alpha, \alpha\rangle=\operatorname{tr} \nabla\langle\nabla \alpha, \alpha\rangle \\
& =\operatorname{tr}\left\langle\nabla^{2} \alpha, \alpha\right\rangle+\operatorname{tr}\langle\nabla \alpha, \nabla \alpha\rangle
\end{aligned}$$
For the first term, use the Weitzenböck formula: $\operatorname{tr}\left(\bar{\nabla}^{2} \alpha\right)=S(\alpha)-\Delta \alpha$. For the second term, note that $\operatorname{tr}\langle\nabla \alpha, \nabla \alpha\rangle$ is just $\langle\nabla \alpha, \nabla \alpha\rangle$ by definition of the pointwise inner product in $\Omega^{k+1}(M, E)$. We thus get $\frac{1}{2} \Delta\|\alpha\|^{2}=\langle S(\alpha)-\Delta \alpha, \alpha\rangle+\|\nabla \alpha\|^{2}$. \(\square\)

Corollary 2.10 (Bochner formula for maps between Riemannian manifolds). Let $f: M \rightarrow N$ be a smooth map between Riemannian manifolds.
$$\frac{1}{2} \Delta\|\nabla f\|^{2}-\langle\nabla f, \nabla \Delta f\rangle=\left\|\nabla^{2} f\right\|^{2}+\operatorname{Ric}^{M}\left(\langle\nabla f, \nabla f\rangle_{N}\right)-R^{N}\left(\langle\nabla f \otimes \nabla f\rangle_{M},\langle\nabla f \otimes \nabla f\rangle_{M}\right) .$$
Proof. The Bochner formula (14) is just a specialization of (13) when $E=f^{*} \mathrm{~T} N, k=1$ and $\alpha=\mathrm{d} f$. Indeed, $\langle S(\alpha), \alpha\rangle$ gives the two curvature terms of (14); it remains to argue that $\Delta(\mathrm{d} f)=-\nabla(\Delta f)$. Since $\mathrm{d}_{\nabla} \mathrm{d} f=0$ (Proposition 1.12), $\Delta(\mathrm{d} f)=\mathrm{d}_{\nabla} \mathrm{d}_{\nabla}^{*} \mathrm{~d} f$. Conclude recalling that $\mathrm{d}_{\nabla}^{*} \mathrm{~d} f=-\Delta f$ (Proposition 1.21). \(\square\)

\section*{3 Kähler manifolds and pluriharmonic maps}

\subsection*{3.1 Complex and Kähler manifolds}

Let $M$ be a complex manifold. In particular $M$ has an almost complex structure, i.e. $J \in \Gamma(\operatorname{End} \mathrm{~T} M)$ with $J^{2}=-1$. This is essentially the scalar multiplication by $i$ in $\mathbb{C}^{n}$, pulled back on $\mathrm{T} M$ by complex charts. Here $J$ is called integrable because it comes from a complex structure on $M$. The Newlander-Nirenberg theorem states that $J$ is integrable if and only if its Nijenhuis tensor vanishes, see e.g. [Dem12]. Note that $J$ induces an orientation of $M$ and we always assume this agrees with the given orientation.

The complexified tangent bundle of $\mathrm{T}_{\mathbb{C}} M:=\mathrm{T} M \otimes \mathbb{C}$ splits into $\pm i$-eigenspaces of $J$ as $\mathrm{T}_{\mathbb{C}} M=$ $\mathrm{T}^{1,0} M \oplus \mathrm{~T}^{0,1} M$. Accordingly, a complex tangent vector decomposes into types as $u=u^{1,0}+u^{0,1}$, with:
$$u^{1,0}=\frac{1}{2}(u-i J u) \quad u^{0,1}=\frac{1}{2}(u+i J u) .$$

The cotangent space $\mathrm{T}^{*} M$ also has a complex structure still denoted $J$, defined by $J \alpha:=\alpha \circ J$, hence the analogous decomposition $\mathrm{T}_{\mathbb{C}}^{*} M=\mathrm{T}^{* 1,0} M \oplus \mathrm{~T}^{* 0,1} M$. Thankfully, it is true that $\alpha^{1,0}(u)=\alpha\left(u^{1,0}\right)$ and $\alpha^{0,1}(u)=\alpha\left(u^{0,1}\right)$, where on the right-hand side one takes the complexification of $\alpha$.

If $f: M \rightarrow N$ is a smooth map where $M$ is a (almost) complex manifold, we write similarly
$$\mathrm{d}^{1,0} f=\frac{1}{2}(\mathrm{~d} f-i \mathrm{~d} f \circ J) \quad \mathrm{d}^{0,1} f=\frac{1}{2}(\mathrm{~d} f+i \mathrm{~d} f \circ J) .$$

These are $\mathbb{R}$-linear maps $\mathrm{T} M \rightarrow \mathrm{~T}_{\mathbb{C}} N$, or equivalently, $\mathbb{C}$-linear maps $\mathrm{T}_{\mathbb{C}} M \rightarrow \mathrm{~T}_{\mathbb{C}} N$. We also denote:
$$\mathrm{d}^{\mathrm{c}} f:=-\mathrm{d} f \circ J=-i\left(\mathrm{~d}^{1,0} f-\mathrm{d}^{0,1} f\right) .$$
Remark 3.1. If $\left(N, J_{N}\right)$ is also a (almost) complex manifold-this will not be the case in most of this report-one can further decompose $\mathrm{d}^{1,0} f$ and $\mathrm{d}^{0,1} f$ into their (1, 0)- and (0, 1)-parts with respect to $J_{N}$. We write accordingly $\mathrm{d}^{1,0} f=\partial f+\partial \bar{f}$ and $\mathrm{d}^{0,1} f=\bar{\partial} f+\bar{\partial} \bar{f} . f$ is called holomorphic if $\mathrm{d} f \circ J_{M}=J_{N} \circ \mathrm{~d} f$, which amounts to $\bar{\partial} f=0$. Equivalently, $f$ preserves types: $\mathrm{d} f\left(\mathrm{~T}^{1,0} M\right) \subseteq \mathrm{T}^{1,0} N$.

Definition 3.2. A Hermitian manifold is a smooth manifold equipped with a Riemannian metric $g$ and an integrable almost complex structure $J$ that are compatible, meaning that $g(J u, J v)=g(u, v)$.

Given a Hermitian manifold $(M, g, J)$, one defines the fundamental form $\omega$ by $\omega(u, v)=g(J u, v)$. It is a nondegenerate 2-form on $M$, in fact it is a (1, 1)-form, i.e. $\omega(J u, J v)=\omega(u, v)$. One can also define a Hermitian inner product $h$ on ( $\mathrm{T} M, J$ ) by letting $h=g-i \omega$.
Example 3.3. The Hermitian metric on $M=\mathbb{C}$ is $h=\mathrm{d} z \otimes \mathrm{~d} \bar{z}=g-i \omega$ with $g=\mathrm{d} x^{2}+\mathrm{d} y^{2}$ and $\omega=\mathrm{d} x \wedge \mathrm{~d} y$. This example should discourage anyone from using other conventions for the definition of $\omega$.

The fundamental form $\omega$ can be incoroporated in the data of a Hermitian manifold $(M, g, J, \omega)$, it being understood that $\omega(u, v)=g(J u, v)$. This relation shows that any 2 of the 3 tensors $g, J, \omega$ determine the third, this matches the well-known 2-out-of-3 property of the unitary group $\mathrm{U}(n)$.

Proposition 3.4. Let ( $M, g, I, \omega$ ) be a Hermitian manifold.
\begin{itemize}
\item[(i)] Denoting $n:=\operatorname{dim}_{\mathbb{C}} M$, one has
$$\frac{\omega^{n}}{n!}=\operatorname{vol}_{M} .$$
\item[(ii)] For all $\alpha \in \Omega^{1}(M, \mathbb{R})$
$$* \alpha=\frac{\omega^{n-1}}{(n-1)!} \wedge J \alpha$$
(See § 1.3 for the definition of the Hodge star.)
\end{itemize}
Proof. Both statements are linear algebra statements in $\mathrm{T}_{x} M$. One easily proves them using an orthonormal basis $\left(e_{1}, J e_{1}, \ldots, e_{n}, J e_{n}\right)$ of $\mathrm{T}_{x} M$. \(\square\)

Definition 3.5. A Hermitian manifold ( $M, g, J, \omega$ ) is called Kähler if $\mathrm{d} \omega=0$.
In other words, $\omega$ is required to be a symplectic structure. The simple condition $\mathrm{d} \omega=0$ has deep consequences on the geometry of $M$, starting with the existence of holomorphic coordinates identifying $(M, g, J, \omega)$ to $\mathbb{C}^{n}$ with the flat metric to first order. We shall not develop any theory of Kähler manifolds in this report: $\mathrm{d} \omega=0$ is all we need, especially for the proof of the Siu-Sampson theorem following Toledo. In fact, § 4 will be a perfect illustration of the provocative [Amo+96, Metatheorem 1.2]:

\section*{Kähler manifolds are complex manifolds whose geometry reduces to linear algebra.}

The only analysis involved in the proof in § 4.3.2 is that $\int_{M} \eta=0$ if $\eta$ is exact, the rest is linear algebra!
One can show that $\mathrm{d} \omega=0$ is equivalent to $\nabla J=0$. A straightforward yet key consequence is:
Proposition 3.6. Let $(M, g, J, \omega)$ be a Hermitian manifold. If $M$ is Kähler then the Riemann and Ricci tensors of $M$ are of type (1, 1), i.e. $R^{M}(J u, J v)=R^{M}(u, v)$ and $\operatorname{Ric}^{M}(J u, J v)=\operatorname{Ric}^{M}(u, v)$.

\subsection*{3.2 Pluriharmonic maps}

In this subsection, $N$ is any Riemannian manifold. If $(M, g, J, \omega)$ is a Kähler manifold, we can nicely combine Proposition 1.21 with Proposition 3.4 (ii) and use closedness of $\omega$ to obtain:

Proposition 3.7. Let $f: M \rightarrow N$ be a smooth map, where ( $M, g, J, \omega$ ) is a Kähler manifold of complex dimension $n$. Then
$$-\Delta f=*\left(\frac{\omega^{n-1}}{(n-1)!} \wedge \mathrm{d}_{\nabla} \mathrm{d}^{\mathrm{c}} f\right) .$$
Proof.
$$\begin{aligned}
-\Delta f & =\mathrm{d}_{\nabla}^{*} \mathrm{~d} f & & \text { by Proposition 1.21 } \\
& =(-1)^{2 n(k-1)+1} * \mathrm{~d}_{\nabla} * \mathrm{~d} f & & \text { by definition of } \mathrm{d}_{\nabla}^{*}(\text { cf Definition 1.13) } \\
& =* \mathrm{~d}_{\nabla}\left(\frac{\omega^{n-1}}{(n-1)!} \wedge \mathrm{d}^{\mathrm{c}} f\right) & & \text { by Proposition 3.4 (ii) } \\
& =*\left(\frac{\mathrm{~d}\left(\omega^{n-1}\right)}{(n-1)!} \wedge \mathrm{d}^{\mathrm{c}} f+\frac{\omega^{n-1}}{(n-1)!} \wedge \mathrm{d}_{\nabla} \mathrm{d}^{\mathrm{c}} f\right) & & \text { by definition of } \mathrm{d}_{\nabla} \\
& =*\left(\frac{\omega^{n-1}}{(n-1)!} \wedge \mathrm{d}_{\nabla} \mathrm{d}^{\mathrm{c}} f\right) & & \text { since } \mathrm{d} \omega=0 \text { (M Kähler) }
\end{aligned}$$ \(\square\)

Corollary 3.8. Let $f: M \rightarrow N$ be a smooth map, where $(M, g, J, \omega)$ is a Kähler manifold of complex dimension $n$. Then $f$ is harmonic if and only if $\omega^{n-1} \wedge \mathrm{~d}_{\nabla} \mathrm{d}^{\mathrm{c}} f=0$.

An important special case is when $\operatorname{dim}_{\mathbb{C}} M=1$, i.e. $M=C$ is a Riemann surface (complex curve), in which case any compatible metric is Kähler. Then $f: C \rightarrow N$ is harmonic if and only if $\mathrm{d}_{\nabla} \mathrm{d}^{\mathrm{c}} f=0$. Recall that $\mathrm{d}_{\nabla}$ does not see the metric on $C$ (only depends on $\nabla=f^{*} \nabla^{N}$ ), and neither does $\mathrm{d}^{\mathrm{c}}$. Therefore $f: C \rightarrow N$ being harmonic only depends on the complex structure on $C$ :

Corollary 3.9. Let $C$ be a complex curve. The harmonicity of a smooth map $f: C \rightarrow N$ does not depend on the choice of a compatible metric on $C$.

A consequence of Corollary 3.9 is the sanity of the definition of pluriharmonicity:
Definition 3.10. A smooth map $f: M \rightarrow N$ where $M$ is a complex manifold is called pluriharmonic if for every 1-dimensional complex submanifold $C \subseteq M$, the restriction $f_{\mid C}: C \rightarrow N$ is harmonic.

Pluriharmonicity can alternatively be defined by the equation $\mathrm{d}_{\nabla} \mathrm{d}^{\mathrm{c}} f=0$ :
Proposition 3.11. Let $f: M \rightarrow N$ be a smooth map where $M$ is a complex manifold.
$$f \text { pluriharmonic } \Leftrightarrow \mathrm{d}_{\nabla} \mathrm{d}^{\mathrm{c}} f=0 \text {. }$$
We also have the further characterizations:
$$f \text { pluriharmonic } \quad \Leftrightarrow \quad \bar{\partial}_{\nabla} \mathrm{d}^{1,0} f=0 \quad \Leftrightarrow \quad \partial_{\nabla} \mathrm{d}^{0,1} f=0 \quad \Leftrightarrow \quad\left(\nabla^{2} f\right)^{1,1}=0 .$$
Remark 3.12. We have naturally written $\mathrm{d}_{\nabla}=\mathrm{d}_{\nabla}^{1,0}+\mathrm{d}_{\nabla}^{0,1}=\partial_{\nabla}+\bar{\partial}_{\nabla}$.
Remark 3.13. To make sense of the Hessian in the last one, choose any compatible Riemannian metric on $M$ (see Definition 1.5). Also see Remark 3.14. Due to this characterization, pluriharmonic maps have sometimes been called (1,1)-geodesic maps.

Proof of Proposition 3.11. Recall that $\mathrm{d}_{\nabla} \mathrm{d} f=0$ (Proposition 1.12). Decomposing into types:
$$\underbrace{\partial_{\nabla} \mathrm{d}^{1,0} f}_{\left(\mathrm{d}_{\nabla} \mathrm{d} f\right)^{2,0}=0}+\underbrace{\partial_{\nabla} \mathrm{d}^{0,1} f+\bar{\partial}_{\nabla} \mathrm{d}^{1,0} f}_{\left(\mathrm{d}_{\nabla} \mathrm{d} f\right)^{1,1}=0}+\underbrace{\bar{\partial}_{\nabla} \mathrm{d}^{0,1} f}_{\left(\mathrm{d}_{\nabla} \mathrm{d} f\right)^{0,2}=0}=0$$
On the other hand:
$$\begin{aligned}
\mathrm{d}_{\nabla} \mathrm{d}^{\mathrm{c}} f & =-i \mathrm{~d}_{\nabla}\left(\mathrm{d}^{1,0} f-\mathrm{d}^{0,1} f\right) \\
& =-i\left(\partial_{\nabla} \mathrm{d}^{1,0} f+\partial_{\nabla} \mathrm{d}^{0,1} f-\bar{\partial}_{\nabla} \mathrm{d}^{1,0} f-\bar{\partial}_{\nabla} \mathrm{d}^{0,1} f\right)
\end{aligned}$$
We thus find
$$\mathrm{d}_{\nabla} \mathrm{d}^{\mathrm{c}} f=-2 i \partial_{\nabla} \mathrm{d}^{0,1} f=2 i \bar{\partial}_{\nabla} \mathrm{d}^{1,0} f .$$
It follows that $\mathrm{d}_{\nabla} \mathrm{d}^{\mathrm{c}} f=0 \Leftrightarrow \bar{\partial}_{\nabla} \mathrm{d}^{1,0} f=0 \Leftrightarrow \partial_{\nabla} \mathrm{d}^{0,1} f=0$. We also learn that $\mathrm{d}_{\nabla} \mathrm{d}^{\mathrm{c}} f$ is of type (1, 1).
If $\mathrm{d}_{\nabla} \mathrm{d}^{\mathrm{c}} f=0$, then this equation still holds on any complex curve $C \subseteq M$, where it means that $f$ is harmonic, hence $f$ is pluriharmonic. Conversely, if $f$ is pluriharmonic, then $\mathrm{d}_{\nabla} \mathrm{d}^{\mathrm{c}} f=0$ in restriction to any complex curve. As a 2-form of type (1, 1), $\mathrm{d}_{\nabla} \mathrm{d}^{\mathrm{c}} f$ vanishes if and only if it vanishes on pairs of the form $(u, J u)$. Since any such pair is tangent to some complex curve $C \subseteq M$, the conclusion follows.

It remains to show that $\mathrm{d}_{\nabla} \mathrm{d}^{\mathrm{c}} f=0 \Leftrightarrow\left(\nabla^{2} f\right)^{1,1}=0$. By Proposition 1.11,
$$\left(\mathrm{d}_{\nabla} \mathrm{d}^{\mathrm{c}} f\right)(u, v)=\bar{\nabla}_{u}\left(\mathrm{~d}^{\mathrm{c}} f(v)\right)-\bar{\nabla}_{v}\left(\mathrm{~d}^{\mathrm{c}} f(u)\right)=-\nabla^{2} f(u, J v)+\nabla^{2} f(v, J u) .$$
It follows that
$$-\left(\mathrm{d}_{\nabla} \mathrm{d}^{\mathrm{c}} f\right)(J u, v)=\nabla^{2} f(J u, J v)+\nabla^{2} f(u, v)=2\left(\nabla^{2} f\right)^{1,1}(u, v)$$
$\left(2 T^{1,1}(u, v)=T(u, v)+T(J u, J v)\right.$ holds for any 2-covariant tensor $T$.) The conclusion follows. \(\square\)

Remark 3.14. As it turns out, the tensor $\left(\nabla^{2} f\right)^{1,1}=-\frac{1}{2}\left(\mathrm{~d}_{\nabla} \mathrm{d}^{\mathrm{c}} f\right)(J u, v)$ does not depend on the choice of a compatible metric on $M$. One may call it the Levi form of $f$.

Below are some properties of pluriharmonic maps. For more results, we refer to [OU90].
Proposition 3.15. Let $f: M \rightarrow N$ where $M$ is a complex manifold and $N$ is a Riemannian manifold.
\begin{itemize}
\item[(i)] If $f$ is pluriharmonic, the restriction of $f$ to any complex submanifold of $M$ is pluriharmonic.
\item[(ii)] If $f$ is pluriharmonic, then $f$ is harmonic with respect to any compatible Kähler metric on $M$.
\item[(iii)] If $N$ is a Kähler manifold and $f$ is $\pm$-holomorphic ${ }^{4}$, then $f$ is pluriharmonic.
\end{itemize}

Remark 3.16. When $N=\mathbb{R}$, a function $f: M \rightarrow \mathbb{R}$ is pluriharmonic if and only if it is the real part of a holomorphic function. I am unsure what a generalization of that property could be.

Proof of Proposition 3.15. (i) is trivial by definition of pluriharmonicity. (ii) follows from Proposition 3.7. For (iii): if $f$ is ±-holomorphic, then $\mathrm{d}^{\mathrm{c}} f=\mathrm{d} f \circ J_{M}= \pm J_{N} \circ \mathrm{~d} f$. Since $N$ is Kähler, $\nabla J_{N}=0(\nabla J=0$ if and only if $J$ is integrable and $\mathrm{d} \omega=0$ in any almost Hermitian manifold). It easily follows that $\mathrm{d}_{\nabla}\left(J_{N} \circ \alpha\right)=$ $J_{N} \circ \mathrm{~d}_{\nabla}(\alpha)$ for any $\alpha \in \Omega^{1}\left(M, f^{*} \mathrm{~T} N\right)$. In particular, $\mathrm{d}_{\nabla} \mathrm{d}^{\mathrm{c}} f= \pm \mathrm{d}_{\nabla}\left(J_{N} \circ \mathrm{~d} f\right)= \pm J_{N} \circ \mathrm{~d} \nabla \mathrm{~d} f$. Recall that $\mathrm{d}_{\nabla} \mathrm{d} f=0$ is always true (Proposition 1.12), therefore we find $\mathrm{d}_{\nabla} \mathrm{d}^{\mathrm{c}} f=0$, i.e. $f$ is pluriharmonic. \(\square\)

Remark 3.17. Nicolas Tholozan pointed out to me that the converse of Proposition 3.15 (ii) is also true locally: if $f$ is harmonic with respect to any locally defined Kähler metric, then $f$ is pluriharmonic.

Example 3.18. As a special case of Proposition 3.15 (iii), if $N$ is Kähler manifold and $M$ is a complex submanifold, then the embedding of $M$ in $N$ is minimal (i.e. it is a harmonic isometric immersion). For example, consider complex submanifolds $\mathbb{C} P^{1} \rightarrow \mathbb{C} P^{3}$ induced by linear subspaces $\mathbb{C}^{2} \rightarrow \mathbb{C}^{4}$. Such embeddings of $\mathbb{C} P^{1} \approx S^{2}$ in $\mathbb{C} P^{3} \approx S^{4}$ thus are minimal spheres.

\footnotetext{
${ }^{4}$ We call ±-holomorphic a map that is holomorphic or antiholomorphic.
}

\section*{4 The Siu-Sampson theorem}

The main goal of this section is to explain the Siu-Sampson theorem below (Theorem 4.1), first proven by Sampson [Sam86] ${ }^{5}$ following the Bochner technique of Siu [Siu80].

Theorem 4.1 (Siu, Sampson). Let $M$ be a compact Kähler manifold and let $N$ be Riemannian manifold of nonpositive Hermitian sectional curvature. If $f: M \rightarrow N$ is harmonic, then $f$ is pluriharmonic. Moreover:
$$R^{N}(X, Y, \bar{X}, \bar{Y})=0$$
for all $x \in M$ and for all $X, Y \in \mathrm{~d} f\left(\mathrm{~T}_{x}^{1,0} M\right)$.
In (15), $R^{N}$ is the complexification of the Riemann curvature tensor of $N$ to $\mathrm{T}_{\mathbb{C}} N$. By definition, $N$ has nonpositive Hermitian sectional curvature if $R^{N}(X, Y, \bar{X}, \bar{Y}) \leqslant 0$ for all $X, Y$.

\subsection*{4.1 Strong curvature conditions}

\subsection*{4.1.1 Hermitian sectional curvature and strongly nonpositive curvature}

Theorem 4.1 requires the notion of Hermitian sectional curvature. Contrary to what its name could suggest, this is a purely Riemannian notion.

Let $N$ be a Riemannian manifold. Refer to § 2.3.1 for the definitions of the curvature tensors on $N$, such as the Riemann tensor $R$ and the curvature operator $Q$. We still denote $R$ and $Q$ the complex linear extensions of these operators to complexified vectors, e.g. $Q: \otimes^{2}\left(\mathrm{~T}_{\mathbb{C}} N\right) \times \otimes^{2}\left(\mathrm{~T}_{\mathbb{C}} N\right) \rightarrow \mathbb{C}$.

We say that $N$ has nonpositive Hermitian sectional curvature if $R(X, Y, \bar{X}, \bar{Y}) \leqslant 0$ for any $X, Y \in \mathrm{~T}_{\mathbb{C}} N$. Following Siu [Siu80], we alternatively say that $N$ has strongly nonpositive curvature.

Clearly, $N$ has strongly nonpositive curvature if and only if $Q(\sigma, \bar{\sigma}) \leqslant 0$ for any decomposable tensor $\sigma \in \bigotimes^{2}\left(\mathrm{~T}_{\mathbb{C}} N\right)$. If moreover $Q(\sigma, \bar{\sigma}) \leqslant 0$ on all $\bigotimes^{2}\left(\mathrm{~T}_{\mathbb{C}} N\right)$, we say that $N$ has very strongly nonpositive curvature. This is equivalent to $Q(\sigma, \sigma) \leqslant 0$ on $\otimes^{2} \mathrm{~T} N$, in other words $Q$ is negative semidefinite on $\otimes^{2} \mathrm{~T} N$. We have obvious analogous notions of (very) strongly nonnegative curvature.

Example 4.2. A manifold of strongly nonpositive curvature clearly has nonpositive sectional curvature. It is easy to see that the converse holds for a manifold of constant sectional curvature. More generally it holds for $\delta$-pinched curvature with $\delta \geqslant 1 / 4$ by [YZ91]. This means that for all $p \in N$, the sectional curvature at $p$ is between $-c_{p}$ and $-\delta c_{p}$ for some constant $c_{p}>0$ ( $\delta$ is always assumed in ( 0,1 ]).
Example 4.3. Of course, one expects that there are Riemannian manifolds with nonpositive yet not strongly nonpositive curvature, and it is claimed in [Amo+96] and [Zhe00], but I am not aware of an example. That being said, [AF05] produces examples of closed Riemannian manifolds of negative sectional curvature which do not admit any Riemannian metric of very strongly nonpositive curvature.
Example 4.4. By Jost-Yau [JY83], a product of hyperbolic spaces $\mathbb{H}^{2} \times \cdots \times \mathbb{H}^{2}$ has strongly nonpositive curvature. I believe that it actually has very strongly nonpositive curvature, in fact I do not know an example of manifold with strongly, but not very strongly, nonpositive curvature.

Example 4.5. Symmetric spaces of noncompact type have very strongly nonpositive curvature (see § 5). Similarly, symmetric spaces of compact type have very strongly nonnegative curvature.

Example 4.6. Y. Wu [Wu14] showed that the Teichmüller space of a closed surface of genus > 1 has very strongly nonpositive curvature.

\footnotetext{
${ }^{5}$ See Theorem 1 p. 129: Although Sampson does not use the terminology pluriharmonic, the equations $y_{\alpha \mid \bar{\beta}}^{j}=0$ mean that $\mathrm{d}_{\nabla}^{0,1} \mathrm{~d}^{1,0} f=0$, i.e. $f$ is pluriharmonic by Proposition 3.11.
}

\subsection*{4.1.2 Strongly negative curvature of Kähler manifolds}

The natural attempt to define very strongly negative curvature by $Q(\sigma, \bar{\sigma})<0$ for all nonzero $\sigma \in$ $\bigotimes^{2}\left(\mathrm{~T}_{\mathbb{C}} N\right)$ is unreasonable. Indeed, on any Kähler manifold $N$, it follows from Proposition 3.6 that $Q(\sigma, \bar{\sigma})=0$ for any $\sigma$ of type $(2,0)$ or ( 0,2 ). By definition, a Kähler manifold $N$ has strongly negative curvature if $Q(\sigma, \bar{\sigma})<0$ for all nonzero $\sigma \in \mathrm{T}^{1,0} N \otimes \mathrm{~T}^{0,1} N$ of length $\leqslant 2$, e.g. $\sigma=X \otimes \bar{Y}+Z \otimes \bar{W}$, and $N$ has very strongly negative curvature if $Q(\sigma, \bar{\sigma})<0$ for all nonzero $\sigma \in \mathrm{T}^{1,0} N \otimes \mathrm{~T}^{0,1} N$.
Example 4.7. Siu [Siu80] proved that complex hyperbolic space $\mathbb{C} H^{n}$ has very strongly negative curvature. $\mathbb{C} P^{n}$ has very strongly positive curvature. Mostow-Siu [MS80] provided an example of compact Kähler manifold with very strongly negative curvature that is not a quotient of $\mathbb{C} H^{n}$.
Example 4.8. According to [Zhe00, Theorem 9.26], a Kähler manifold of complex dimension 2 has very strong negative (resp. nonpositive) curvature if and only if it has negative (resp. nonpositive) sectional curvature. We expect this to be false in higher dimensions, but we are not aware of a counter-example.

\subsection*{4.1.3 Non-example: the Penrose twistor fibration}

Let us illustrate with a non-example that the curvature condition is critical for the Siu-Sampson theorem Theorem 4.1. Consider the map (called Penrose twistor fibration, see e.g. [Bry85])
$$f: \mathbb{C} P^{3}=\left\{\mathbb{C} \text {-lines in } \mathbb{C}^{4}\right\} \longrightarrow \mathbb{H} P^{1}=\left\{\mathbb{H} \text {-lines in } \mathbb{H}^{2}\right\}$$
defined by $f(l)=L$, where $L$ is the unique $\mathbb{H}$-line in $\mathbb{H}^{2} \approx \mathbb{C}^{4}$ containing $l$. Here $\mathbb{H}$ denotes the $\mathbb{R}$-algebra of quaternions. Topologically, $\mathbb{H} P^{1} \approx S^{7} / S^{3} \approx S^{4}$, and $\mathbb{H} P^{1}$ has a natural Riemannian (in fact quaternion-Kähler) metric of constant curvature 1, making the Hopf fibration $S^{3} \rightarrow S^{7} \rightarrow S^{4}$ a Riemannian submersion. In particular $\mathbb{H} P^{1}$ does not have nonpositive Hermitian sectional curvature.

We claim that $f$ is harmonic. Indeed, one can check that $f$ is a Riemannian submersion, and it is known since [ES64] that a Riemannian submersion is harmonic if and only if its fibers are minimal submanifolds. Here the fibers of $f$ are minimal spheres as we have seen in Example 3.18.

However $f$ is not pluriharmonic. Indeed, consider a fiber $C$ of $f$ and a transverse $\mathbb{C}$-plane $C^{\prime} \subseteq \mathbb{C}^{4}$. For any $\varepsilon>0$, it is possible to choose $C^{\prime}$ contained in the $\varepsilon$-neighborhood of $C$ in $\mathbb{C} P^{3}$ (just tilt $C$ slightly) and such that $C^{\prime}$ is not a fiber of $f$. Then the restrition of $f$ to $C^{\prime}$ is nonconstant and maps $C^{\prime}$ into the $\varepsilon$-neighborhood a point (namely $f(C)$ ) in $\mathbb{H} P^{1} \approx S^{4}$. Such a map cannot be harmonic by the maximum principle. Since $C^{\prime}$ is a complex curve in $\mathbb{C} P^{3}, f$ is not pluriharmonic.

For non-experts, let us explain why any harmonic map from a closed manifold $M$ to a Riemannian manifold $N$ whose image is contained in a small ball must be constant. For $\varepsilon$ small enough, the function $\varphi=d(p, \cdot)^{2}$ is convex on $B(p, \varepsilon)$, i.e. it has positive semidefinite Hessian. However, harmonic functions pull back convex functions to subharmonic functions. Indeed, one has the composition formula
$$\Delta(\varphi \circ f)=\mathrm{d} \varphi \circ \Delta(f)+\operatorname{tr}\left(\left(\nabla^{2} \varphi\right)(\mathrm{d} f, \mathrm{~d} f)\right)$$
so that if $\Delta f=0, \Delta(\varphi \circ f) \geqslant 0$ when $\varphi$ is convex. (The converse is true: $f$ is harmonic if it pulls back any locally defined convex function to a subharmonic function [Ish79, Thm 3.4].) This implies that any local maximum of $\varphi \circ f$ cannot be attained at an interior point of $M$ unless $f$ is constant by the maximum principle for subharmonic functions. By compactness of $M, \varphi \circ f$ does attain a global maximum, however $M$ only has interior points (no boundary), so $f$ must be constant.

\subsection*{4.2 Sampson's Bochner formula}

Siu [Siu80] was the first to find a Bochner formula (also known as Siu's $\partial \bar{\partial}$-trick) for maps between Kähler manifolds and obtain rigidity results. Sampson [Sam86] gave an improvement of Siu's Bochner formula that implies Theorem 4.1.
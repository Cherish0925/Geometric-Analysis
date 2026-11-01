---
retention_scope: session
part: 1
total_parts: 2
---

[Part 1/2 of: The Dirichlet-to-Neumann operator for divergence form problems]

---
source_file: 1707_05734.pdf
converter: mathpix
format: mmd
---

\title{
The Dirichlet-to-Neumann operator for divergence form problems
}

\author{
A.F.M. ter Elst, G. Gordon and M. Waurick
}

June 6, 2018

\begin{abstract}
We present a way of defining the Dirichlet-to-Neumann operator on general Hilbert spaces using a pair of operators for which each one's adjoint is formally the negative of the other. In particular, we define an abstract analogue of trace spaces and are able to give meaning to the Dirichlet-to-Neumann operator of divergence form operators perturbed by a bounded potential in cases where the boundary of the underlying domain does not allow for a well-defined trace. Moreover, a representation of the Dirichlet-to-Neumann operator as a first-order system of partial differential operators is provided. Using this representation, we address convergence of the Dirichlet-to-Neumann operators in the case that the appropriate reciprocals of the leading coefficients converge in the weak operator topology. We also provide some extensions to the case where the bounded potential is not coercive and consider resolvent convergence.
\end{abstract}

Keywords: Dirichlet-to-Neumann operator, resolvent convergence, continuous dependence on the coefficients.

MSC 2010: 35F45, 46E35, 47A07.

\section*{1 Introduction}

In the theory of elliptic partial differential operators, the Dirichlet-to-Neumann operator is a central object of study. In recent years it attracted a lot of attention and triggered profound research in many directions. In particular, we mention applications of the form method, relations to the extension theory of symmetric operators as well as the intimate connection to the Calderón problem, see, for instance, the references in [BE1].

The Dirichlet-to-Neumann operator relates Dirichlet boundary data to the corresponding Neumann boundary data of solutions to a partial differential equation. As an introduction, we provide a definition for the Dirichlet-to-Neumann operator in its arguably simplest form.

Let $\Omega \subset \mathbb{R}^{d}$ be a bounded domain with smooth boundary $\Gamma=\partial \Omega$ and where $d \geqslant 2$. Note that in this case, the trace map $\operatorname{Tr}$ from $H^{1}(\Omega)$ into $H^{1 / 2}(\Gamma)$ is a well-defined, surjective and
continuous operator. Let $\varphi \in H^{1 / 2}(\Gamma)$ and let $u \in H^{1}(\Omega)$ be the solution of the boundary value problem
$$-\Delta u=0 \text { weakly on } \Omega \quad \text { and } \quad \operatorname{Tr} u=\varphi .$$
The Dirichlet-to-Neumann operator $\Lambda$ assigns to $\varphi$ the normal derivative of $u$, that is, $\Lambda \varphi=\partial_{\nu} u \in H^{-1 / 2}(\Gamma)$.

We can also consider the part of $\Lambda$ in $L_{2}(\Gamma)$. If we call this restriction $\Lambda_{L_{2}(\Gamma)}$, then $\Lambda_{L_{2}(\Gamma)}$ is an unbounded operator in $L_{2}(\Gamma)$ such that for all $\varphi, \psi \in L_{2}(\Gamma)$ it follows that $\varphi \in \operatorname{dom}\left(\Lambda_{L_{2}(\Gamma)}\right)$ and $\Lambda_{L_{2}(\Gamma)} \varphi=\psi$ if and only if there exists a $u \in H^{1}(\Omega)$ such that $-\Delta u=0$ weakly on $\Omega, \operatorname{Tr} u=\varphi$ and $\psi=\partial_{\nu} u$. A problem with the above descriptions is that they only make sense if the boundary of $\Omega$ is sufficiently smooth. We may also refer to [AE1] for a variant of the Dirichlet-to-Neumann operator for domains with a rough boundary that has finite $(d-1)$-dimensional Hausdorff measure. If, however, $\Omega$ has for example a fractal boundary with infinite $(d-1)$-dimensional Hausdorff measure, then in [AE1] there is no notion of the Dirichlet-to-Neumann operator at hand simply because there is no appropriate notion of a trace. Using the concepts developed in [PTW2] (with extensions in [PTW1] and [Tro]), we are able to provide a substitute for the space $H^{1 / 2}(\Gamma)$. We note here that this 'trace-free' concept has proven to be useful for dealing with boundary value problems on domains with rough boundary, see [PSTW].

The substitute for the space $H^{1 / 2}(\Gamma)$ is a variant of 1-harmonic functions in $\Omega$. This removes the need for function evaluation at the boundary. For the definition of this substitute of $H^{1 / 2}(\Gamma)$, the only concept that we use, if we relate our findings to the Laplacian, is that the matrix $\left(\begin{array}{cc}0 & \text { div } \\ \text { grad } & 0\end{array}\right)$ is skew-symmetric on the space of infinite differentiable functions with compact support, see Example 2.3. Thus, without further effort, our results directly apply to similar problems involving the equations of linearized elasticity or the full 3-dimensional system of static Maxwell's equations. More generally, our methods apply to the covariant derivative defined on suitable $L_{2}$-tensor fields and a formal skew-adjoint.

As our central object of study, we shall deviate from the classical elliptic partial differential operator $-\Delta$ discussed above and treat abstract divergence form operators of the form
$$-D a G+m,$$
where $a$ and $m$ are bounded coercive operators (called coefficients) and $D$ and $G$ are densely defined, closed, unbounded operators in Hilbert spaces $H_{1}$ and $H_{0}$ with the property $-D^{*} \subset G$, like div and grad.

If $\operatorname{dom}(G)$, endowed with the graph norm, embeds compactly into $H_{0}$, we will also address the concept of continuous dependence of the Dirichlet-to-Neumann operator associated with (1) on the bounded coefficients $a$ and $m$ under the weak operator topology. This result has applications in homogenization problems, see [Tar] and [Wau1] Section 5.5. Moreover, it complements the study of continuous dependence of the Dirichlet-to-Neumann operator on its coefficients in [AEKS], where the authors focus on possible non-coercive cases and convergence of the principal coefficients in $L_{\infty}(\Omega)$. In order to prove convergence results, we derive a reformulation of the Dirichlet-to-Neumann operator as a system of two first-order partial differential equations, similar to [AKM].

In the present work we also consider removing the coercivity condition on $m$. That is to say, we define the abstract analogue of the Dirichlet-to-Neumann graph with $m$ being possibly not coercive. We note here that these results are the abstract counterpart of results developed in [BE1] and [AEKS]. In the case that the potentials $m$ are not coercive we consider resolvent convergence for Dirichlet-to-Neumann operators. Under different assumptions convergence of Neumann-to-Dirichlet operators was obtained in [Ron].

We mention here that a possible non-linear variant of the Dirichlet-to-Neumann operator, where the coercive operator $a$ is replaced by a (strictly) maximal monotone relation, can be discussed using the results of [TW]. This however is beyond the scope of the present manuscript and will be addressed in future work.

We briefly comment on the organization of the paper. In Section 2, we provide the basic functional analytic setting and recall some notions and results of [PTW2], [PTW1] and [Tro]. We then state the definition of the Dirichlet-to-Neumann operator in the abstract setting discussed above. We also provide an extensive example that justifies this abstraction by relating it to the classical formulation of the Dirichlet-to-Neumann operator. In Section 3 we give a representation formula for the Dirichlet-to-Neumann operator as a first-order system and show that this operator is m-sectorial, provided both $m$ and $a$ are coercive. For this we use a representation result for operators given via forms, see [AE2]. In Section 4 we prove resolvent convergence of the Dirichlet-to-Neumann operators when the coefficients converge in an appropriate weak operator topology. Under some additional hypotheses we also obtain in Theorem 4.2 uniform convergence even though the coefficients converge in the weak operator topology only. In Section 5 we consider the non-coercive case and discuss the domain and multi-valued parts of the Dirichlet-to-Neumann graph when $m$ is merely assumed to be a bounded operator, that is not necessarily coercive. Moreover, we also prove a convergence theorem for the non-coercive case in Section 6. We conclude with two more examples in Section 7.

\section*{2 The Dirichlet-to-Neumann operator and boundary spaces}

We start with a description of boundary data spaces as in [PTW2] Subsection 5.2. Throughout this paper fix Hilbert spaces $H_{0}$ and $H_{1}$. Further, let $G$ be an operator in $H_{0}$ with values in $H_{1}$ and let $D$ be an operator in $H_{1}$ with values in $H_{0}$. We assume throughout that both $G$ and $D$ are densely defined and closed, and that $-G^{*} \subset D$. We define $\stackrel{\circ}{D}=-G^{*}$ and $\stackrel{\circ}{G}=-D^{*}$.

Note that
$$(\stackrel{\circ}{G} u, q)_{H_{1}}=-(u, \stackrel{\circ}{D} q)_{H_{0}}$$
for all $u \in \operatorname{dom}(\stackrel{\circ}{G})$ and $q \in \operatorname{dom}(\stackrel{\circ}{D})$. Equivalently, the matrix
$$\left(\begin{array}{cc}
0 & \stackrel{\circ}{D} \\
\stackrel{\circ}{G} & 0
\end{array}\right)$$
with dense domain $\operatorname{dom}(\stackrel{\circ}{G}) \times \operatorname{dom}(\stackrel{\circ}{D})$ is skew-symmetric in $H_{0} \times H_{1}$.

Remark 2.1. Note that $\stackrel{-}{G}=-D^{*} \subset-\left(-G^{*}\right)^{*}=\bar{G}=G$. So one can simultaneously swap $H_{0}$ with $H_{1}$ and $D$ with $G$.

Example 2.2. All examples in this paper are of the following type. Let $H_{0}$ and $H_{1}$ be Hilbert spaces. Consider dense subspaces $\operatorname{dom}(\widehat{G}) \subset H_{0}$ and $\operatorname{dom}(\widehat{D}) \subset H_{1}$. Let $\widehat{G}: \operatorname{dom}(\widehat{G}) \rightarrow H_{1}$ and $\widehat{D}: \operatorname{dom}(\widehat{D}) \rightarrow H_{0}$ be two operators such that
$$(\widehat{G} u, q)_{H_{1}}=-(u, \widehat{D} q)_{H_{0}}$$
for all $u \in \operatorname{dom}(\widehat{G})$ and $q \in \operatorname{dom}(\widehat{D})$. Equivalently, the matrix
$$\left(\begin{array}{cc}
0 & \widehat{D} \\
\widehat{G} & 0
\end{array}\right)$$
with dense domain $\operatorname{dom}(\widehat{G}) \times \operatorname{dom}(\widehat{D})$ is skew-symmetric in $H_{0} \times H_{1}$.
Then $\widehat{G} \subset-(\widehat{D})^{*}$ and $\widehat{D} \subset-(\widehat{G})^{*}$, so both $\widehat{G}$ and $\widehat{D}$ are closable. Let $\dot{G}$ and $\stackrel{\circ}{D}$ denote the closures. Define $G=-(\stackrel{\circ}{D})^{*}$ and $D=-(\stackrel{\circ}{G})^{*}$. Since $\stackrel{\circ}{D}$ and $\stackrel{\circ}{G}$ are closed, therefore closable, it follows that $G$ and $D$ are densely defined. Obviously both $G$ and $D$ are closed. Next $G^{*}=-(\dot{D})^{* *}=-\dot{D}$ since $\dot{D}$ is closed and similarly $D^{*}=-\dot{G}$. Also $\stackrel{\circ}{D} \subset-(\widehat{G})^{*}=-(\stackrel{\circ}{G})^{*}$, so $\stackrel{\circ}{G} \subset-(\stackrel{\circ}{D})^{*}=G$. Similarly $\stackrel{\circ}{D} \subset D$. Then $G^{*}=-\stackrel{\circ}{D} \subset-D$ as required.

The classical example for this paper is as follows. Note that we do not assume any condition on the boundary of $\Omega$.

Example 2.3. Let $\Omega \subset \mathbb{R}^{d}$ be open. Define $\widehat{G}: C_{c}^{\infty}(\Omega) \rightarrow L_{2}(\Omega)^{d}$ and $\widehat{D}: C_{c}^{\infty}(\Omega)^{d} \rightarrow L_{2}(\Omega)$ by
$$\widehat{G} u=\left(\partial_{1} u, \ldots, \partial_{d} u\right) \quad \text { and } \quad \widehat{D} q=\sum_{k=1}^{d} \partial_{k} q_{k} .$$
Define $H_{0}=L_{2}(\Omega)$ and $H_{1}=L_{2}(\Omega)^{d}$. Then (2) in Example 2.2 follows from integration by parts. The associated operators are denoted by $G=\operatorname{grad}, \stackrel{\circ}{G}=\operatorname{grad}, D=\operatorname{div}$ and $\stackrel{\circ}{D}=\operatorname{div}$. It is not hard to show that $\operatorname{dom}(\operatorname{grad})=H_{0}^{1}(\Omega), \operatorname{dom}(\operatorname{grad})=H^{1}(\Omega)$ and $\operatorname{dom}(\operatorname{div})=H_{\operatorname{div}}(\Omega)=\left\{q \in L_{2}(\Omega)^{d}: \operatorname{div} q \in L_{2}(\Omega)\right\}$.

We next define an (abstract) variant of the trace spaces $H^{1 / 2}(\Gamma)$ and $H^{-1 / 2}(\Gamma)$. Throughout this paper we provide the domain of an operator with the graph norm. Define
$$\mathrm{BD}(G)=\operatorname{dom}(\stackrel{\circ}{G})^{\perp_{\operatorname{dom}(G)}} \quad \text { and } \quad \operatorname{BD}(D)=\operatorname{dom}(\stackrel{\circ}{D})^{\perp_{\operatorname{dom}(D)}} .$$
We provide $\operatorname{BD}(G)$ and $\operatorname{BD}(D)$ with the induced inner products of $\operatorname{dom}(G)$ and $\operatorname{dom}(D)$. We denote by $\pi_{\mathrm{BD}(G)}$ and $\pi_{\mathrm{BD}(D)}$ the corresponding projections onto $\operatorname{BD}(G)$ and $\operatorname{BD}(D)$, respectively.

Example 2.4. Let $\Omega, G$ and $D$ be as in Example 2.3. Then $\operatorname{BD}(G)=\left\{u \in H^{1}(\Omega):\right.$ $\Delta u=u$ weakly on $\Omega\}$. Indeed, let $u \in \operatorname{BD}(G)$. Then $u \in H^{1}(\Omega)$ and $0=(u, v)_{\operatorname{dom}(G)}=$ $(u, v)_{L_{2}(\Omega)}+(\operatorname{grad} u, \operatorname{grad} v)_{L_{2}(\Omega)}$ for all $v \in \operatorname{dom}(\dot{G})=H_{0}^{1}(\Omega)$. So $\Delta u=u$ weakly on $\Omega$. The converse inclusion is similar.

Lemma 2.5. $\operatorname{BD}(G)=\operatorname{ker}(I-D G)$ and $\operatorname{BD}(D)=\operatorname{ker}(I-G D)$.
Proof. By Remark 2.1 it suffices to prove the first equality. Let $u \in \mathrm{BD}(G)$. Then
$$(u, v)_{H_{0}}+(G u, \dot{G} v)_{H_{1}}=(u, v)_{\operatorname{dom}(G)}=0$$
for all $v \in \operatorname{dom}(\stackrel{\circ}{G})$. So $G u \in \operatorname{dom}\left((\stackrel{\circ}{G})^{*}\right)=\operatorname{dom}(D)$ and $D G u=-(\stackrel{\circ}{G})^{*} G u=u$. Therefore $u \in \operatorname{ker}(I-D G)$. The converse follows similarly. \(\square\)

Corollary 2.6. If $u \in \mathrm{BD}(G)$, then $G u \in \mathrm{BD}(D)$. If $q \in \mathrm{BD}(D)$, then $D q \in \mathrm{BD}(G)$.
Proof. Let $u \in \operatorname{BD}(G)$. Then $u \in \operatorname{dom}(D G)$ and $D G u=u \in \operatorname{dom}(D G)$. Therefore $u \in \operatorname{dom}(G D G)$ and $(I-G D) G u=G(I-D G) u=0$. So $G u \in \operatorname{ker}(I-G D)=\operatorname{BD}(D)$ by Lemma 2.5. The other statement follows similarly. \(\square\)

Define $\dot{G}: \operatorname{BD}(G) \rightarrow \operatorname{BD}(D)$ and $\dot{D}: \operatorname{BD}(D) \rightarrow \operatorname{BD}(G)$ by
$$\dot{G} u=G u \quad \text { and } \quad \dot{D} q=D q .$$

Lemma 2.7. The operators $\dot{G}$ and $\dot{D}$ are unitary. Moreover, $(\dot{G})^{*}=\dot{D}$.
Proof. See [PTW2, Theorem 5.2]. For the convenience of the reader we include the proof. Clearly $\dot{D} \dot{G}=I_{\mathrm{BD}(G)}$ and $\dot{G} \dot{D}=I_{\mathrm{BD}(D)}$ by Lemma 2.5. Moreover,
$$(\dot{G} u, q)_{\mathrm{BD}(D)}=(\dot{G} u, q)_{H_{1}}+(\dot{D} \dot{G} u, \dot{D} q)_{H_{0}}=(\dot{G} u, \dot{G} \dot{D} q)_{H_{1}}+(u, \dot{D} q)_{H_{0}}=(u, \dot{D} q)_{\mathrm{BD}(G)}$$
for all $u \in \mathrm{BD}(G)$ and $q \in \mathrm{BD}(D)$, from which the lemma follows. \(\square\)

In the situation of Example 2.3 the space $\operatorname{BD}(G)$ models the boundary data of an $H^{1}(\Omega)$-function if $\Omega$ is a bounded Lipschitz domain, as shown in [Tro, Corollary 4.4]. Indeed, let $\Gamma=\partial \Omega$. Since $\operatorname{Tr}: H^{1}(\Omega) \rightarrow H^{1 / 2}(\Gamma)$ is continuous, surjective and $\operatorname{ker} \operatorname{Tr}=$ $H_{0}^{1}(\Omega)=\operatorname{dom}(\operatorname{grad})$, it follows that
$$\left.\operatorname{Tr}\right|_{\mathrm{BD}(G)}: \operatorname{BD}(G) \rightarrow H^{1 / 2}(\Gamma)$$
is bijective and hence a topological isomorphism.
We next consider the space $\operatorname{BD}(D)$. Denote by $\operatorname{BD}(G)^{\prime}$ the space of all antilinear continuous maps from $\operatorname{BD}(G)$ into $\mathbb{C}$. There is a natural unitary map from $\operatorname{BD}(D)$ onto $\operatorname{BD}(G)^{\prime}$.

Proposition 2.8. Define $\Phi: \operatorname{BD}(D) \rightarrow \operatorname{BD}(G)^{\prime}$ by
$$(\Phi(q))(u)=(D q, u)_{H_{0}}+(q, G u)_{H_{1}} .$$
Then $\Phi$ is unitary.
Proof. Let $q \in \mathrm{BD}(D)$ and $u \in \mathrm{BD}(G)$. Then
$$\begin{aligned}
(\Phi(q))(u) & =(D q, u)_{H_{0}}+(q, G u)_{H_{1}} \\
& =(q, G u)_{H_{1}}+(D q, D G u)_{H_{0}}=(q, G u)_{\operatorname{dom}(D)}=(q, \dot{G} u)_{\operatorname{BD}(D)} .
\end{aligned}$$
Then the proposition follows from Lemma 2.7 and the Riesz representation theorem. \(\square\)

For clarity and contrast we include the proof of the next proposition. We provide $\operatorname{Tr} H^{1}(\Omega)$ with the quotient norm.

Proposition 2.9. Let $\Omega \subset \mathbb{R}^{d}$ be open, bounded with Lipschitz boundary. Then one has the following.
\begin{itemize}
\item[(a)] For all $q \in H_{\operatorname{div}}(\Omega)$ there exists a unique $Q \in\left(\operatorname{Tr} H^{1}(\Omega)\right)^{\prime}$ such that
$$\langle Q, \operatorname{Tr} u\rangle_{\left(\operatorname{Tr} H^{1}(\Omega)\right)^{\prime} \times \operatorname{Tr} H^{1}(\Omega)}=\int_{\Omega}(\operatorname{div} q) \bar{u}+\int_{\Omega} q \cdot \overline{\nabla u}$$
for all $u \in H^{1}(\Omega)$.
\item[(b)] If $q \in \operatorname{dom}(\operatorname{div})$, then $Q=0$, where $Q$ is as in (5).
\item[(c)] If $q \in H^{1}(\Omega)^{d}$, then $Q=\nu \cdot \operatorname{Tr} q$, where $\nu$ is the outward normal vector on the boundary $\Gamma$ of $\Omega$ and $Q$ is as in (5).
\end{itemize}

Proof. [a]. Define $F: H^{1}(\Omega) \rightarrow \mathbb{C}$ by
$$F(u)=\int_{\Omega}(\operatorname{div} q) \bar{u}+\int_{\Omega} q \cdot \overline{\nabla u} .$$
Then $F \in H^{1}(\Omega)^{\prime}$. Moreover, if $u \in H_{0}^{1}(\Omega)$, then $F(u)=0$. Hence there exists a unique continuous antilinear map $\widetilde{F}: \operatorname{Tr} H^{1}(\Omega) \rightarrow \mathbb{C}$ such that $\widetilde{F}(\operatorname{Tr} u)=F(u)$ for all $u \in H^{1}(\Omega)$. Then the first statement follows.
(b). We use the notation as in Example 2.3. Let $q \in \operatorname{dom}(\stackrel{\circ}{D})$. Since $\stackrel{\circ}{D}=-G^{*}$ one deduces that $F(u)=\int_{\Omega}(\operatorname{div} q) \bar{u}+\int_{\Omega} q \cdot \overline{\nabla u}=(\AA q, u)_{H_{1}}+(q, G u)_{H_{0}}=0$ for all $u \in \operatorname{dom}(G)$. So $Q=0$, because $\operatorname{dom}(G)$ is dense in $H^{1}(\Omega)$.
(c). Suppose that $q \in H^{1}(\Omega)^{d}$. Let $u \in H^{1}(\Omega)$. Then $\bar{u} q \in W^{1,1}(\Omega)^{d}$ and the divergence theorem gives
$$\int_{\Omega}(\operatorname{div} q) \bar{u}+\int_{\Omega} q \cdot \overline{\nabla u}=\int_{\Omega} \operatorname{div}(\bar{u} q)=\int_{\Gamma} \nu \cdot \operatorname{Tr}(\bar{u} q)=\int_{\Gamma}(\nu \cdot \operatorname{Tr} q) \operatorname{Tr} \bar{u} .$$
So $Q=\nu \cdot \operatorname{Tr} q$. \(\square\)

If $q \in H_{\operatorname{div}}(\Omega)$ and $Q$ is as in Proposition 2.9, then we define $(\nu q)=Q$. So $(\nu q)=\nu \cdot \operatorname{Tr} q$ if $q \in H^{1}(\Omega)^{d}$.

Example 2.10. Let $\Omega$ be a bounded Lipschitz domain with boundary $\Gamma$. Let $G$ and $D$ be as in Example 2.3. Let $\Phi$ be as in Proposition 2.8. Then
$$(\Phi(q))(u)=\langle(\nu q), \operatorname{Tr} u\rangle_{\left(\operatorname{Tr} H^{1}(\Omega)\right)^{\prime} \times \operatorname{Tr} H^{1}(\Omega)}$$
for all $q \in \mathrm{BD}(D)$ and $u \in \mathrm{BD}(G)$.
It follows from (3) and Proposition 2.8 that the spaces $\operatorname{BD}(D)$ and $H^{-1 / 2}(\Gamma)$ are isomorphic. Hence $\dot{G}$ is a variant of the Dirichlet-to-Neumann operator.

Next we introduce the (variable) coefficients for our abstract Dirichlet-to-Neumann operator. Recall that a bounded operator $M$ in a Hilbert space $H$ is called coercive if there exists a $\mu>0$ such that $\operatorname{Re} M \geqslant \mu I$, where $\operatorname{Re} M=\frac{1}{2}\left(M+M^{*}\right)$. That is $M$ is coercive if and only if there exists a $\mu>0$ such that $\operatorname{Re}(M x, x) \geqslant \mu\|x\|_{H}^{2}$ for all $x \in H$.

As for the classical Dirichlet-to-Neumann operator, we first show that the Dirichlet problem has a unique solution.

Proposition 2.11. Let $a \in \mathcal{L}\left(H_{1}\right)$ and $m \in \mathcal{L}\left(H_{0}\right)$ be coercive. Let $u_{0} \in \operatorname{BD}(G)$. Then there exists a unique $u \in \operatorname{dom}(D a G)$ such that $m u-D a G u=0$ and $u-u_{0} \in \operatorname{dom}(\dot{G})$.

For the proof of the proposition we need several auxiliary results.
Lemma 2.12. Let $H$ be a Hilbert space, $M \in \mathcal{L}(H)$ and $A$ a skew-adjoint operator in $H$. Let $\lambda>0$ and assume that $\operatorname{Re}(M x, x)_{H} \geqslant \lambda\|x\|_{H}^{2}$ for all $x \in H$. Then the operator $M+A$ is invertible. Moreover, the operator $(M+A)^{-1}$ is bounded from $H$ into $\operatorname{dom}(A)$ and $\left\|(M+A)^{-1}\right\|_{H \rightarrow \operatorname{dom}(A)} \leqslant \frac{1+\lambda+\|M\|}{\lambda}$.

Proof. If $x \in \operatorname{dom}(A)$, then $\operatorname{Re}((M+A) x, x)_{H}=\operatorname{Re}\left((M x, x)_{H} \geqslant \lambda\|x\|_{H}^{2}\right.$. Hence $M+A$ is one-to-one, its range is closed and $M+A$ is continuously invertible on its range. Since $\operatorname{Re}(M x, x)_{H}=\operatorname{Re}\left(M^{*} x, x\right)_{H}$ for all $x \in H$, we obtain similarly that $(M+A)^{*}=M^{*}-A$ is one-to-one. Therefore $M+A$ is onto. So $M+A$ is invertible and $\left\|(M+A)^{-1}\right\|_{H \rightarrow H} \leqslant \frac{1}{\lambda}$.

Since $A(M+A)^{-1}=I-M(M+A)^{-1}$, the operator $A(M+A)^{-1}$ is bounded from $H$ into $H$ and the estimate follows. \(\square\)

Next we consider matrix operators.
Lemma 2.13. Let $a \in \mathcal{L}\left(H_{1}\right)$ and $m \in \mathcal{L}\left(H_{0}\right)$ be coercive.
\begin{itemize}
\item[(a)] The operators $\left(\begin{array}{cc}m & -\stackrel{\circ}{D} \\ -G & a^{-1}\end{array}\right)$ and $\left(\begin{array}{cc}m & -D \\ -\stackrel{\circ}{G} & a^{-1}\end{array}\right)$ in $H_{0} \times H_{1}$ are invertible.
\item[(b)] The operator $\left(\begin{array}{cc}m & -\dot{D} \\ -G & a^{-1}\end{array}\right)^{-1}$ is bounded from $H_{0} \times H_{1}$ into $\operatorname{dom}(G) \times \operatorname{dom}(\stackrel{\circ}{D})$.
\item[(c)] The operator $\left(\begin{array}{cc}m & -D \\ -\stackrel{\circ}{G} & a^{-1}\end{array}\right)^{-1}$ is bounded from $H_{0} \times H_{1}$ into $\operatorname{dom}(\stackrel{\circ}{G}) \times \operatorname{dom}(D)$.
\end{itemize}

Proof. Let $H=H_{0} \times H_{1}, M=\left(\begin{array}{cc}m & 0 \\ 0 & a^{-1}\end{array}\right)$ and $A=\left(\begin{array}{cc}0 & -\stackrel{\circ}{D} \\ -G & 0\end{array}\right)$ with $\operatorname{dom}(A)=$ $\operatorname{dom}(G) \times \operatorname{dom}(\stackrel{\circ}{D})$. Since $-\stackrel{\circ}{D}^{*}=G$ and $-G^{*}=\stackrel{\circ}{D}$, the operator $A$ is skew-adjoint. Also $\operatorname{Re} a^{-1} \geqslant\|a\|^{-2} \operatorname{Re} a$, so $M$ is coercive. Therefore $M+A$ is invertible and the operator $(M+A)^{-1}$ is bounded from $H$ into $\operatorname{dom}(A)$ by Lemma 2.12. This proves the first part of Statement (a) and Statement (b)

The remaining parts of the lemma follow similarly. \(\square\)

Lemma 2.14. Let $a \in \mathcal{L}\left(H_{1}\right)$ and $m \in \mathcal{L}\left(H_{0}\right)$ be coercive. Let $u \in \operatorname{dom}(G), q \in \operatorname{dom}(D)$, $u_{0} \in \mathrm{BD}(G)$ and $q_{0} \in \mathrm{BD}(D)$.
\begin{itemize}
\item[(a)] The following conditions are equivalent.
\begin{itemize}
\item[(i)] $D q=m u, q=a G u$ and $u-u_{0} \in \operatorname{dom}(\dot{G})$.
\item[(ii)] $q=a G u, u-u_{0} \in \operatorname{dom}(\dot{G})$ and
$$(a G u, \stackrel{\circ}{G} v)_{H_{1}}=-(m u, v)_{H_{0}}$$
for all $v \in \operatorname{dom}(\stackrel{\circ}{G})$.
\item[(iii)] $\binom{u-u_{0}}{q}=\left(\begin{array}{cc}m & -D \\ -\stackrel{\circ}{G} & a^{-1}\end{array}\right)^{-1}\binom{-m u_{0}}{G u_{0}}$.
\end{itemize}
\item[(b)] The following conditions are equivalent.
\begin{itemize}
\item[(i)] $D q=m u, q=a G u$ and $q-q_{0} \in \operatorname{dom}(\stackrel{\circ}{D})$.
\item[(ii)] $\binom{u}{q-q_{0}}=\left(\begin{array}{cc}m & -\stackrel{\circ}{D} \\ -G & a^{-1}\end{array}\right)^{-1}\binom{D q_{0}}{-a^{-1} q_{0}}$.
\end{itemize}
\end{itemize}

Proof. (a). (i) ⇔ (ii). This follows immediately from the equality $D=-(\dot{G})^{*}$.
(i) ⇔ (iii) . By a simple algebraic manipulation Condition (i) is equivalent to
$$u-u_{0} \in \operatorname{dom}(\dot{G}) \quad \text { and } \quad\left(\begin{array}{cc}
m & -D \\
-G & a^{-1}
\end{array}\right)\binom{u-u_{0}}{q}=\binom{-m u_{0}}{G u_{0}} .$$
By Lemma 2.13(a) this is equivalent to Condition (iii).
[(b)]. The proof is similar. \(\square\)

Now we are able to prove Proposition 2.11.
Proof of Proposition 2.11. First we show existence. Let $u \in \operatorname{dom}(G)$ and $q \in \operatorname{dom}(D)$ be such that
$$\binom{u-u_{0}}{q}=\left(\begin{array}{cc}
m & -D \\
-\stackrel{-}{G} & a^{-1}
\end{array}\right)^{-1}\binom{-m u_{0}}{G u_{0}} .$$
Then $u$ satisfies the desired properties by Lemma 2.14 (a) (iii) ⇒ (i).
It remains to show uniqueness. Let $\tilde{u} \in \operatorname{dom}(D a G)$ and suppose that $m \tilde{u}-D a G \tilde{u}=0$ and $\tilde{u}-u_{0} \in \operatorname{dom}(\stackrel{\circ}{G})$. Set $\tilde{q}=a G \tilde{u}$. Then it follows from Lemma 2.14(a) (i) ⇒ (iii) that
$$\binom{\tilde{u}-u_{0}}{\tilde{q}}=\left(\begin{array}{cc}
m & -D \\
-\stackrel{-}{G} & a^{-1}
\end{array}\right)^{-1}\binom{-m u_{0}}{G u_{0}},$$
which implies that $u=\tilde{u}$. \(\square\)

There is a similar version of Proposition 2.11 for the Neumann problem.
Proposition 2.15. Let $a \in \mathcal{L}\left(H_{1}\right)$ and $m \in \mathcal{L}\left(H_{0}\right)$ be coercive. Let $q_{0} \in \operatorname{BD}(D)$. Then there exists a unique $u \in \operatorname{dom}(D a G)$ such that $m u-D a G u=0$ and $a G u-q_{0} \in \operatorname{dom}(\stackrel{\circ}{D})$.

Proof. This follows similarly to the proof of Proposition 2.11, but now use Lemma 2.14(b) instead of Lemma 2.14(a). \(\square\)

At this stage we are able to define the Dirichlet-to-Neumann operator with variable coefficients as an operator acting from $\operatorname{BD}(G)$ (the abstract realization of $H^{1 / 2}(\Gamma)$ ) to $\operatorname{BD}(D)$ (the abstract realization of $H^{-1 / 2}(\Gamma)$ ).

Definition 2.16. Let $a \in \mathcal{L}\left(H_{1}\right)$ and $m \in \mathcal{L}\left(H_{0}\right)$ be coercive. Define the operator
$$\Lambda: \mathrm{BD}(G) \rightarrow \mathrm{BD}(D)$$
as follows. Let $u_{0} \in \mathrm{BD}(G)$. By Proposition 2.11 there exists a unique $u \in \operatorname{dom}(D a G)$ such that $m u-D a G u=0$ and $u-u_{0} \in \operatorname{dom}(\stackrel{\circ}{G})$. Then we define $\Lambda u_{0}=\pi_{\mathrm{BD}(D)} a G u$. We call $\Lambda$ the Dirichlet-to-Neumann operator associated with $-D a G+m$.

So the graph of the operator $\Lambda$ is equal to
$$\left\{\left(\pi_{\mathrm{BD}(G)} u, \pi_{\mathrm{BD}(D)} a G u\right): u \in \operatorname{dom}(D a G) \text { and } m u-D a G u=0\right\} .$$

Theorem 2.17. Let $a \in \mathcal{L}\left(H_{1}\right)$ and $m \in \mathcal{L}\left(H_{0}\right)$ be coercive. Then the operator $\Lambda$ associated with $-D a G+m$ is bounded and invertible. Moreover,
$$\Lambda u_{0}=\left(\begin{array}{ll}
0 & \pi_{\mathrm{BD}(D)}
\end{array}\right)\left(\begin{array}{cc}
m & -D \\
-\stackrel{\circ}{G} & a^{-1}
\end{array}\right)^{-1}\binom{-m}{G} u_{0}$$
for all $u_{0} \in \operatorname{BD}(G)$ and
$$\Lambda^{-1} q_{0}=\left(\begin{array}{ll}
\pi_{\mathrm{BD}(G)} & 0
\end{array}\right)\left(\begin{array}{cc}
m & -\stackrel{\circ}{D} \\
-G & a^{-1}
\end{array}\right)^{-1}\binom{D}{-a^{-1}} q_{0}$$
for all $q_{0} \in \mathrm{BD}(D)$.
Proof. The expression for $\Lambda$ follows from Lemma 2.14(a), arguing as in the proof of Proposition 2.11. The boundedness of $\Lambda$ is then a consequence of Lemma 2.13)(c).

The proof for $\Lambda^{-1}$ is similar, using Lemma 2.14(b), Proposition 2.15 and Lemma 2.13(b). \(\square\)

\section*{3 An intermediate operator and m-sectoriality}

In Proposition 2.8 we showed that the space $\operatorname{BD}(D)$ is naturally isomorphic to $\operatorname{BD}(G)^{\prime}$. In this section we assume that there is a Hilbert space $H$ such that $\operatorname{BD}(G) \hookrightarrow H \hookrightarrow \operatorname{BD}(G)^{\prime}$ is a Gelfand triple. Then we study the part of the Dirichlet-to-Neumann operator in $H$. In the model example, Example 2.3, one can take $H=L_{2}(\Gamma)$.

Throughout this section, we adopt the notation and assumptions as in the beginning of Section 2. In addition, let $H$ be a Hilbert space and $\kappa \in \mathcal{L}(\mathrm{BD}(G), H)$. We assume that $\kappa$ is one-to-one and has dense range.

Example 3.1. Let $\Omega$ be a bounded Lipschitz domain with boundary $\Gamma$. Let $G$ and $D$ be as in Example 2.3. Let $\sigma \in\left(-\infty, \frac{1}{2}\right]$ and choose $H=H^{\sigma}(\Gamma)$. Define $\kappa: \operatorname{BD}(G) \rightarrow H$ by
$\kappa(u)=\operatorname{Tr} u$. Then $\kappa$ is one-to-one and has dense range. Note that $\kappa$ is compact if and only if $\sigma<\frac{1}{2}$.

Now suppose that $\sigma=0$, so $H=L_{2}(\Gamma)$. Let $\psi \in L_{2}(\Gamma)$ and set $u=\kappa^{*} \psi$. Then $u \in \mathrm{BD}(G)$, so $u \in H^{1}(\Omega)$ and $\Delta u=u$ weakly on $\Omega$ by Example 2.4. If $v \in \mathrm{BD}(G)$, then
$$\begin{aligned}
\int_{\Gamma} \psi \overline{\operatorname{Tr} v} & =(\psi, \kappa(v))_{L_{2}(\Gamma)}=\left(\kappa^{*} \psi, v\right)_{\mathrm{BD}(G)}=(u, v)_{\mathrm{BD}(G)} \\
& =\int_{\Omega} u \bar{v}+\int_{\Omega} \nabla u \cdot \overline{\nabla v}=\int_{\Omega}(\Delta u) \bar{v}+\int_{\Omega} \nabla u \cdot \overline{\nabla v} .
\end{aligned}$$
Alternatively, if $v \in H_{0}^{1}(\Omega)=\operatorname{dom}(\stackrel{\circ}{G})$, then
$$\int_{\Gamma} \psi \overline{\operatorname{Tr} v}=0=\int_{\Omega}(\Delta u) \bar{v}+\int_{\Omega} \nabla u \cdot \overline{\nabla v} .$$
So by linearity
$$\int_{\Gamma} \psi \overline{\operatorname{Tr} v}=\int_{\Omega}(\Delta u) \bar{v}+\int_{\Omega} \nabla u \cdot \overline{\nabla v}$$
for all $v \in H^{1}(\Omega)$. Hence $u$ has a weak normal derivative and $\partial_{\nu} u=\psi$.
We consider the Gelfand triple
$$\mathrm{BD}(G) \stackrel{\kappa}{\hookrightarrow} H \simeq H^{\prime} \stackrel{\kappa^{\prime}}{\hookrightarrow} \mathrm{BD}(G)^{\prime}$$
with $H$ as pivot space. Recall that $\operatorname{BD}(G)^{\prime}$ is naturally isomorphic to $\operatorname{BD}(D)$ by Proposition 2.8. We aim to describe the part of the Dirichlet-to-Neumann operator $\Lambda$ in $H$. We describe the image of $H$ in $\operatorname{BD}(D)$ under the above maps $H \simeq H^{\prime} \stackrel{\kappa^{\prime}}{\hookrightarrow} \operatorname{BD}(G)^{\prime} \simeq \operatorname{BD}(D)$.

Lemma 3.2. Let $\Phi: \operatorname{BD}(D) \rightarrow \operatorname{BD}(G)^{\prime}$ be as in Proposition 2.8. Define $F: H \rightarrow H^{\prime}$ by $(F \varphi)(\psi)=(\varphi, \psi)_{H}$. Then $\Phi^{-1} \circ \kappa^{\prime} \circ F=G \circ \kappa^{*}$.

Proof. Let $\varphi \in H$ and write $q=\left(\Phi^{-1} \circ \kappa^{\prime} \circ F\right)(\varphi)$. Let $u \in \operatorname{BD}(G)$. Then it follows from Lemma 2.7 and (4) that
$$\begin{aligned}
(\dot{D} q, u)_{\mathrm{BD}(G)} & =(q, \dot{G} u)_{\mathrm{BD}(D)} \\
& =(\Phi(q))(u)=\left(\left(\kappa^{\prime} \circ F\right) \varphi\right)(u)=(\varphi, \kappa(u))_{H}=\left(\kappa^{*} \varphi, u\right)_{\mathrm{BD}(G)} .
\end{aligned}$$
So $\dot{D} q=\kappa^{*} \varphi$ and $q=\dot{G} \dot{D} q=\dot{G} \kappa^{*} \varphi$. \(\square\)

Now we are able to define the part of the Dirichlet-to-Neumann operator in $H$.
Definition 3.3. Let $a \in \mathcal{L}\left(H_{1}\right)$ and $m \in \mathcal{L}\left(H_{0}\right)$ be coercive. Define the operator $\Lambda_{H}$ in $H$ as follows. Let $\varphi, \psi \in H$. Then we say that $\varphi \in \operatorname{dom}\left(\Lambda_{H}\right)$ and $\Lambda_{H} \varphi=\psi$ if there exists a $u_{0} \in \mathrm{BD}(G)$ such that $\kappa\left(u_{0}\right)=\varphi$ and $\Lambda u_{0}=\left(G \circ \kappa^{*}\right)(\psi)$, where $\Lambda$ is the Dirichlet-to-Neumann operator associated with $-D a G+m$. We call $\Lambda_{H}$ the Dirichlet-to-Neumann operator in $H$ associated with $-D a G+m$.

Despite the abundance of choice of the space $H$, see Example 3.1, the operator $-\Lambda_{H}$ is always a semigroup generator.

Theorem 3.4. Let $a \in \mathcal{L}\left(H_{1}\right)$ and $m \in \mathcal{L}\left(H_{0}\right)$ be coercive. Then the Dirichlet-to-Neumann operator $\Lambda_{H}$ associated with -DaG + $m$ is $m$-sectorial. In particular, if both a and $m$ are symmetric, then $\Lambda_{H}$ is self-adjoint.

The proof of this theorem is based on form methods and the next theorem.
Theorem 3.5. Let $\widetilde{H}, V$ be Hilbert spaces and let $j \in \mathcal{L}(V, \widetilde{H})$ with dense range. Let $\mathfrak{b}: V \times V \rightarrow \mathbb{C}$ be a continuous coercive sesquilinear form, that is there exists a $\mu>0$ such that $\operatorname{Re} \mathfrak{b}(v) \geqslant \mu\|v\|_{V}^{2}$ for all $v \in V$. Define the operator $A$ in $\widetilde{H}$ as follows. Let $x, f \in \widetilde{H}$. Then $x \in \operatorname{dom}(A)$ and $A x=f$ if there exists a $u \in V$ such that $j(u)=x$ and $\mathfrak{b}(u, v)=(f, j(v))_{\tilde{H}}$ for all $v \in V$. Then $A$ is well-defined and $m$-sectorial. If, in addition, $\mathfrak{b}$ is symmetric, then $A$ is self-adjoint.

Proof. See [AE2, Theorem 2.1]. \(\square\)

In the situation of Theorem 3.5 we call $A$ the operator associated with $(\mathfrak{b}, j)$.
Theorem 3.4 is an immediate consequence of Theorem 3.5 and the next proposition.
Proposition 3.6. Let $a \in \mathcal{L}\left(H_{1}\right)$ and $m \in \mathcal{L}\left(H_{0}\right)$ be coercive. Define the sesquilinear form $\mathfrak{b}: \operatorname{dom}(G) \times \operatorname{dom}(G) \rightarrow \mathbb{C}$ by
$$\mathfrak{b}(u, v)=(a G u, G v)_{H_{1}}+(m u, v)_{H_{0}} .$$
Then $\mathfrak{b}$ is coercive and continuous. Further define $j: \operatorname{dom}(G) \rightarrow H$ by $j=\kappa \circ \pi_{\mathrm{BD}(G)}$. Then the Dirichlet-to-Neumann operator $\Lambda_{H}$ associated with $-D a G+m$ is equal to the operator associated with $(\mathfrak{b}, j)$.

Proof. The form $\mathfrak{b}$ is coercive since both $a$ and $m$ are coercive. Obviously $\mathfrak{b}$ is continuous. Let $A$ be the operator associated with $(\mathfrak{b}, j)$. It remains to prove that $A=\Lambda_{H}$.
' $\Lambda_{H} \subset A^{\prime}$. Let $\varphi \in \operatorname{dom}\left(\Lambda_{H}\right)$ and set $\psi=\Lambda_{H} \varphi$. Then there exists a $u_{0} \in \operatorname{BD}(G)$ with $\kappa\left(u_{0}\right)=\varphi$ and $\Lambda u_{0}=\left(G \circ \kappa^{*}\right) \psi$. By definition there exists a $u \in \operatorname{dom}(D a G)$ such that $m u-D a G u=0, u-u_{0} \in \operatorname{dom}(\stackrel{\circ}{G})$ and $\Lambda u_{0}=\pi_{\mathrm{BD}(D)}(a G u)$. Then $\left(G \circ \kappa^{*}\right) \psi=\pi_{\mathrm{BD}(D)}(a G u)$ and $j(u)=\kappa \pi_{\mathrm{BD}(G)} u=\kappa\left(u_{0}\right)=\varphi$.

Next if $v \in \operatorname{dom}(\dot{G})$, then
$$\begin{aligned}
\mathfrak{b}(u, v) & =(a G u, \stackrel{\circ}{G} v)_{H_{1}}+(m u, v)_{H_{0}} \\
& =-(D a G u, v)_{H_{0}}+(D a G u, v)_{H_{0}}=0=(\psi, 0)_{H}=(\psi, j(v))_{H} .
\end{aligned}$$
If $v \in \mathrm{BD}(G)$, then Lemma 2.7 gives
$$\begin{aligned}
(\psi, j(v))_{H} & =\left(\kappa^{*} \psi, v\right)_{\mathrm{BD}(G)}=\left(G \kappa^{*} \psi, G v\right)_{\mathrm{BD}(D)}=\left(\pi_{\mathrm{BD}(D)}(a G u), G v\right)_{\mathrm{BD}(D)} \\
& =(a G u, G v)_{\operatorname{dom}(D)}=(a G u, G v)_{H_{1}}+(D a G u, D G v)_{H_{0}} \\
& =(a G u, G v)_{H_{1}}+(m u, v)_{H_{0}}=\mathfrak{b}(u, v) .
\end{aligned}$$
Since $\operatorname{dom}(G)=\operatorname{BD}(G) \oplus \operatorname{dom}(\stackrel{\circ}{G})$ it follows that $\mathfrak{b}(u, v)=(\psi, j(v))_{H}$ for all $v \in \operatorname{dom}(G)$. So $\varphi \in \operatorname{dom}(A)$ and $A \varphi=\psi$.
' $A \subset \Lambda_{H}$ '. Let $\varphi \in \operatorname{dom}(A)$ and write $\psi=A \varphi$. Then there exists a $u \in \operatorname{dom}(G)$ such that $j(u)=\varphi$ and
$$(a G u, G v)_{H_{1}}+(m u, v)_{H_{0}}=\mathfrak{b}(u, v)=(\psi, j(v))_{H}$$
for all $v \in \operatorname{dom}(G)$. If $v \in \operatorname{dom}(\stackrel{\circ}{G})$, then
$$(a G u, \stackrel{\circ}{G} v)_{H_{1}}+(m u, v)_{H_{0}}=(\psi, j(v))_{H}=0 .$$
So $a G u \in \operatorname{dom}\left((\stackrel{\circ}{G})^{*}\right)=\operatorname{dom}(D)$ and $D a G u=-(\stackrel{\circ}{G})^{*} a G u=m u$. Moreover,
$$\Lambda \pi_{\mathrm{BD}(G)} u=\pi_{\mathrm{BD}(D)}(a G u)$$
by the definition of $\Lambda$. Note that $\kappa\left(\pi_{\mathrm{BD}(G)} u\right)=j(u)=\varphi$.
Now let $v \in \mathrm{BD}(G)$. Then (6) gives
$$\begin{aligned}
\left(\kappa^{*} \psi, v\right)_{\mathrm{BD}(G)} & =(\psi, \kappa(v))_{H} \\
& =(a G u, G v)_{H_{1}}+(m u, v)_{H_{0}} \\
& =(a G u, G v)_{H_{1}}+(D a G u, D G v)_{H_{0}} \\
& =(a G u, G v)_{\operatorname{dom}(D)} \\
& =\left(\pi_{\mathrm{BD}(D)}(a G u), G v\right)_{\mathrm{BD}(D)} \\
& =\left(D \pi_{\mathrm{BD}(G)}(a G u), v\right)_{\mathrm{BD}(G)},
\end{aligned}$$
where we used Lemma 2.7 in the last step. So, $\kappa^{*} \psi=D \pi_{\mathrm{BD}(D)}(a G u)$. Hence
$$\left(G \circ \kappa^{*}\right)(\psi)=\pi_{\mathrm{BD}(D)}(a G u)=\Lambda \pi_{\mathrm{BD}(G)} u$$
by Lemma 2.7 and (7). Therefore $\varphi \in \operatorname{dom}\left(\Lambda_{H}\right)$ and $\Lambda_{H} \varphi=\psi$. \(\square\)

We next show that the operator $\Lambda_{H}$ is invertible and determine its inverse.
Proposition 3.7. The operator $\Lambda_{H}$ is invertible and
$$\Lambda_{H}^{-1} \psi=\kappa\left(\begin{array}{ll}
\pi_{\mathrm{BD}(G)} & 0
\end{array}\right)\left(\begin{array}{cc}
m & -\stackrel{\circ}{D} \\
-G & a^{-1}
\end{array}\right)^{-1}\binom{1}{-a^{-1} G} \kappa^{*} \psi$$
for all $\psi \in H$.
Proof. Since the form $\mathfrak{b}$ in Proposition 3.6 is coercive, it follows that the operator $\Lambda_{H}$ is invertible. Let $\varphi \in \operatorname{dom}\left(\Lambda_{H}\right)$ and write $\psi=\Lambda_{H} \varphi$. Then there exists a $u_{0} \in \operatorname{BD}(G)$ such that $\kappa\left(u_{0}\right)=\varphi$ and $\Lambda u_{0}=G \kappa^{*} \psi$. By Theorem 2.17 we obtain that
$$\begin{aligned}
u_{0}=\Lambda^{-1} G \kappa^{*} \psi & =\left(\begin{array}{ll}
\pi_{\mathrm{BD}(G)} & 0
\end{array}\right)\left(\begin{array}{cc}
m & -\dot{D} \\
-G & a^{-1}
\end{array}\right)^{-1}\binom{D}{-a^{-1}} G \kappa^{*} \psi \\
& =\left(\begin{array}{ll}
\pi_{\mathrm{BD}(G)} & 0
\end{array}\right)\left(\begin{array}{cc}
m & -\stackrel{\circ}{D} \\
-G & a^{-1}
\end{array}\right)^{-1}\binom{I}{-a^{-1} G} \kappa^{*} \psi,
\end{aligned}$$
where we used Lemma 2.7 in the last step. Next apply $\kappa$ to both sides. Since the inverse matrix maps $H_{0} \times H_{1}$ into $\operatorname{dom}(G) \times \operatorname{dom}(D)$ by Lemma 2.13(b), the proposition follows. \(\square\)

\section*{4 Resolvent convergence}

In this section we consider a sequence of Dirichlet-to-Neumann operators and show resolvent convergence.

Throughout this section we adopt the notation and assumptions as in the beginning of Section 2. Let $H$ be a Hilbert space and $\kappa \in \mathcal{L}(\mathrm{BD}(G), H)$ injective with dense range. Further, we let $m_{n}, m \in \mathcal{L}\left(H_{0}\right)$ and $a_{n}, a \in \mathcal{L}\left(H_{1}\right)$ for all $n \in \mathbb{N}$. Let $\mu>0$ and assume that $\operatorname{Re} m_{n}, \operatorname{Re} m \geqslant \mu I_{H_{0}}$ and $\operatorname{Re} a_{n}, \operatorname{Re} a \geqslant \mu I_{H_{1}}$ for all $n \in \mathbb{N}$. Moreover, assume that $\sup _{n}\left\|a_{n}\right\|_{\mathcal{L}\left(H_{1}\right)}<\infty$. Let $\Lambda, \Lambda_{1}, \Lambda_{2}, \ldots$ be the Dirichlet-to-Neumann operators from $\operatorname{BD}(G)$ into $\operatorname{BD}(D)$ associated with $-D a G+m,-D a_{1} G+m_{1},-D a_{2} G+m_{2}, \ldots$ as in Definition 2.16. Similarly, let $\Lambda_{H}, \Lambda_{H}^{(1)}, \Lambda_{H}^{(2)}, \ldots$ be the Dirichlet-to-Neumann operators in $H$ as in Definition 3.3.

Throughout this section we suppose in addition that the inclusion $\operatorname{dom}(G) \hookrightarrow H_{0}$ is compact.

The compactness assumption is valid in our model case, Example 2.3, if $\Omega$ has a continuous boundary or, equivalently, if $\Omega$ has the segment property.

We state two well-known consequences of the compactness assumption.
Lemma 4.1.
\begin{itemize}
\item[(a)] There exists a $c>0$ such that $\|u\|_{H_{0}} \leqslant c\|G u\|_{H_{1}}$ for all $u \in \operatorname{dom}(G) \cap \operatorname{ker}(G)^{\perp_{H_{0}}}$.
\item[(b)] The space $\operatorname{ran}(G)$ is closed in $H_{1}$.
\end{itemize}

Proof. [a]. Suppose not. Then there exists a sequence $\left(u_{n}\right)_{n \in \mathbb{N}}$ in $\operatorname{dom}(G) \cap \operatorname{ker}(G)^{\perp_{H_{0}}}$ such that $\left\|u_{n}\right\|_{H_{0}}=1$ and
$$\left\|u_{n}\right\|_{H_{0}} \geqslant n\left\|G u_{n}\right\|_{H_{1}}$$
for all $n \in \mathbb{N}$. Then $\left(u_{n}\right)_{n \in \mathbb{N}}$ is bounded in $\operatorname{dom}(G)$. We may assume without loss of generality that there exists a $u \in \operatorname{dom}(G)$ such that $\lim u_{n}=u$ weakly in $\operatorname{dom}(G)$. Since the inclusion $\operatorname{dom}(G) \subset H_{0}$ is compact we obtain that $\lim u_{n}=u$ in $H_{0}$. Then $u \in$ $\operatorname{ker}(G)^{\perp_{H_{0}}}$ since $\operatorname{ker}(G)^{\perp_{H_{0}}}$ is closed in $H_{0}$. Moreover, $\|u\|_{H_{0}}=1$ and in particular $u \neq 0$. Alternatively, (8) implies that $\|G u\|_{H_{1}} \leqslant \liminf _{n \rightarrow \infty}\left\|G u_{n}\right\|_{H_{1}}=0$. So $u \in \operatorname{ker}(G)$. Hence $u \in \operatorname{ker}(G) \cap \operatorname{ker}(G)^{\perp_{H_{0}}}=\{0\}$ and $u=0$. This is a contradiction.
[(b)]. This is a consequence of Statement (a) and the closedness of $G$. \(\square\)

We provide $\operatorname{ran}(G)$ with the induced norm of $H_{1}$. Throughout the remainder of this section we denote by $\iota: \operatorname{ran}(G) \hookrightarrow H_{1}$ the embedding map. Note that $\iota^{*}$ is the orthogonal projection from $H_{1}$ onto $\operatorname{ran}(G)$. The main result of this section is the following theorem.

Theorem 4.2. Suppose that $\lim m_{n}=m$ in the weak operator topology on $\mathcal{L}\left(H_{0}\right)$ and $\lim _{n \rightarrow \infty}\left(\iota^{*} a_{n} \iota\right)^{-1}=\left(\iota^{*} a \iota\right)^{-1}$ in the weak operator topology on $\mathcal{L}(\operatorname{ran}(G))$. Then
$$\lim \left(\Lambda_{H}^{(n)}\right)^{-1}=\Lambda_{H}^{-1}$$
in the weak operator topology on $\mathcal{L}(H)$. Moreover, if in addition the map $\kappa$ is compact, then the convergence is uniform in $\mathcal{L}(H)$.

If the $m_{n}$ are multiplication operators, then convergence in the weak operator topology can be rephrased.

Example 4.3. If $\Omega \subset \mathbb{R}^{d}$ is open, $H_{0}=L_{2}(\Omega), V_{n}, V \in L_{\infty}(\Omega)$ and $m_{n}, m$ are the multiplication operators associated with $V_{n}$ and $V$ for all $n \in \mathbb{N}$, then $\lim m_{n}=m$ in the weak operator topology on $\mathcal{L}\left(H_{0}\right)$ if and only if $\lim V_{n}=V$ in the weak*-topology on $L_{\infty}(\Omega)$.

For the proof of Theorem 4.2 we need some preliminary results. The first one contains an identity for $\Lambda$ involving $\operatorname{ran}(G)$.

Lemma 4.4.
\begin{itemize}
\item[(a)] Let $q \in H_{1}$. Then $q \in \operatorname{dom}(\stackrel{\circ}{D})$ if and only if $\iota^{*} q \in \operatorname{dom}(\stackrel{\circ}{D})$. In that case $\stackrel{\circ}{D} q=\stackrel{\circ}{D} \iota^{*} q$.
\item[(b)] The operator $\stackrel{\circ}{D}_{\iota}: \operatorname{ran}(G) \cap \operatorname{dom}(\stackrel{\circ}{D}) \rightarrow H_{0}$ is a closed and densely defined operator in $\operatorname{ran}(G)$. Moreover, $\left({ }^{\circ}{ }^{\circ} \iota\right)^{*}=-\iota^{*} G$.
\item[(c)] The operator $D_{\iota}$ is injective.
\item[(d)] The inclusion $\operatorname{dom}\left(\dot{D}_{\iota}\right) \subset H_{1}$ is compact.
\item[(e)] The operator $\left(\begin{array}{cc}m & -\stackrel{\circ}{D} \iota \\ -\iota^{*} G & \left(\iota^{*} a \iota\right)^{-1}\end{array}\right): \operatorname{dom}(G) \times(\operatorname{ran}(G) \cap \operatorname{dom}(\stackrel{\circ}{D})) \rightarrow H_{0} \times \operatorname{ran}(G)$ is invertible.
\item[(f)] The operator $\left(\begin{array}{cc}m & -\dot{D}_{\iota} \\ -\iota^{*} G & \left(\iota^{*} a \iota\right)^{-1}\end{array}\right)^{-1}$ is bounded from $H_{0} \times \operatorname{ran}(G)$ into $\operatorname{dom}(G) \times$ $\operatorname{dom}(\stackrel{\circ}{D})$.
\item[(g)] If $q_{0} \in \mathrm{BD}(D)$, then
$$\Lambda^{-1} q_{0}=\left(\begin{array}{ll}
\pi_{\mathrm{BD}(G)} & 0
\end{array}\right)\left(\begin{array}{cc}
m & -\stackrel{\circ}{D} \iota \\
-\iota^{*} G & \left(\iota^{*} a \iota\right)^{-1}
\end{array}\right)^{-1}\binom{D}{-\left(\iota^{*} a \iota\right)^{-1} \iota^{*}} q_{0} .$$
\end{itemize}

Proof. (a). First $q-\iota^{*} q \in(\operatorname{ran}(G))^{\perp_{H_{1}}}=\operatorname{ker}\left(G^{*}\right)=\operatorname{ker}(\stackrel{\circ}{D}) \subset \operatorname{dom}(\stackrel{\circ}{D})$. This shows the equivalence. Since $\stackrel{\circ}{D}\left(q-\iota^{*} q\right)=0$, the last statement follows.
(b). Let $q \in \operatorname{ran}(G)$. Since $\operatorname{dom}(\stackrel{\circ}{D})$ is dense in $H_{1}$ there exists a sequence $\left(q_{n}\right)_{n \in \mathbb{N}}$ in $\operatorname{dom}(\stackrel{\circ}{D})$ such that $\lim q_{n}=q$ in $H_{1}$. Then $\iota^{*} q_{n} \in \operatorname{ran}(G) \cap \operatorname{dom}(\stackrel{\circ}{D})$ for all $n \in \mathbb{N}$ by Statement (a) and $\lim \iota^{*} q_{n}=\iota^{*} q=q$ in $H_{1}$. So $\operatorname{ran}(G) \cap \operatorname{dom}(\stackrel{\circ}{D})$ is dense in $\operatorname{ran}(G)$.

Because $\operatorname{ran}(G)$ is closed in $H_{1}$ and $\stackrel{\circ}{D}$ is a closed operator one deduces easily that the operator $\stackrel{\circ}{D}_{\iota}$ is closed. It remains to show that $\left(\stackrel{\circ}{D}_{\iota}\right)^{*}=-\iota^{*} G$.

Let $u \in \operatorname{dom}\left(\left(\stackrel{\circ}{D}_{\iota}\right)^{*}\right)$. Write $q=\left(\stackrel{\circ}{D}_{\iota}\right)^{*} u$. Note that $q \in \operatorname{ran}(G)$. Let $q^{\prime} \in \operatorname{dom}(\stackrel{\circ}{D})$. Then Statement (a) implies that
$$\left(u, \stackrel{\circ}{D} q^{\prime}\right)_{H_{0}}=\left(u, \stackrel{\circ}{D} \iota^{*} q^{\prime}\right)_{H_{0}}=\left(u,\left(\AA^{\circ} \iota\right) \iota^{*} q^{\prime}\right)_{H_{0}}=\left(\left(\AA^{\circ} \iota\right)^{*} u, \iota^{*} q^{\prime}\right)_{\operatorname{ran}(G)}=\left(q, \iota^{*} q^{\prime}\right)_{\operatorname{ran}(G)}=\left(q, q^{\prime}\right)_{H_{1}} .$$
So $u \in \operatorname{dom}\left((\stackrel{\circ}{D})^{*}\right)=\operatorname{dom}(G)$ and $G u=-(\stackrel{\circ}{D})^{*} u=-q$. Therefore, $-\iota^{*} G u=q=\left(\stackrel{\circ}{D}_{\iota}\right)^{*} u$. This implies that $\left({ }^{\circ} D_{\iota}\right)^{*} \subset-\iota^{*} G$. The converse inclusion is easier and is left to the reader.
(c). Let $q \in \operatorname{ran}(G) \cap \operatorname{dom}(\stackrel{\circ}{D})$ and suppose that $\stackrel{\circ}{D} \iota q=0$. There exists a $u \in \operatorname{dom}(G) \cap$ $(\operatorname{ker} G)^{\perp_{H_{0}}}$ such that $q=G u$. Then $\|G u\|_{H_{1}}^{2}=-\left(q,(\stackrel{\circ}{D})^{*} u\right)_{H_{1}}=-(\stackrel{\circ}{D} \iota q, u)_{H_{0}}=0$. So $u \in \operatorname{ker} G$ and $u=0$.
(d). Let $q, q_{1}, q_{2}, \ldots \in \operatorname{dom}\left(\stackrel{\circ}{D}_{\iota}\right)$ and suppose that $\lim q_{n}=q$ weakly in $\operatorname{dom}\left(\stackrel{\circ}{D}_{\iota}\right)$. For all $n \in \mathbb{N}$ there exists a unique $u_{n} \in \operatorname{dom}(G) \cap \operatorname{ker}(G)^{\perp_{H_{0}}}$ such that $q_{n}=G u_{n}$. Since $\lim q_{n}=q$ weakly in $H_{1}$, the sequence $\left(q_{n}\right)_{n \in \mathbb{N}}$ is bounded in $H_{1}$. Hence the sequence $\left(u_{n}\right)_{n \in \mathbb{N}}$ is bounded in $H_{0}$ by Lemma 4.1(a). Passing to a subsequence if necessary, there exists a $u \in H_{0}$ such that $\lim u_{n}=u$ weakly in $H_{0}$. Since $G$ is a weakly closed operator, one deduces that $u \in \operatorname{dom}(G)$ and $G u=q$. Then $\lim u_{n}=u$ weakly in $\operatorname{dom}(G)$, so $\lim u_{n}=u$ strongly in $H_{0}$ by the compactness assumption. Note that $G^{*}=-\stackrel{\circ}{D}$. So
$$\lim _{n \rightarrow \infty}\left\|q_{n}\right\|_{H_{1}}^{2}=\lim _{n \rightarrow \infty}\left(q_{n}, G u_{n}\right)_{H_{1}}=\lim _{n \rightarrow \infty}\left(-\stackrel{\circ}{D} q_{n}, u_{n}\right)_{H_{0}}=(-\stackrel{\circ}{D} q, u)_{H_{0}}=(q, G u)_{H_{0}}=\|q\|_{H_{1}}^{2} .$$
Hence $\lim q_{n}=q$ in $H_{1}$.
(e) and (f). This is as in the proof of Lemma 2.13)(a) and (b).
(g). Let $q_{0} \in \operatorname{BD}(D)$. By Proposition 2.15 there exists a unique $u \in \operatorname{dom}(D a G)$ such that $m u-D a G u=0$ and $a G u-q_{0} \in \operatorname{dom}(\stackrel{\circ}{D})$. Then $\Lambda^{-1} q_{0}=\pi_{B D(G)} u$. Write $q=a G u$. Then $q-q_{0} \in \operatorname{dom}(\stackrel{\circ}{D})$, so $\stackrel{\circ}{D}\left(q-q_{0}\right)=\stackrel{\circ}{D} \iota^{*}\left(q-q_{0}\right)=(\stackrel{\circ}{D} \iota) \iota^{*}\left(q-q_{0}\right)$ by Statement (a). Therefore
$$D q_{0}=m u-\stackrel{\circ}{D}\left(q-q_{0}\right)=m u-\left(\stackrel{\circ}{D}_{\iota}\right) \iota^{*}\left(q-q_{0}\right) .$$
Also $\iota^{*} q=\iota^{*} a G u=\left(\iota^{*} a \iota\right) \iota^{*} G u$. Hence $\left(\iota^{*} a \iota\right)^{-1} \iota^{*} q=\iota^{*} G u$ and $-\iota^{*} G u+\left(\iota^{*} a \iota\right)^{-1} \iota^{*}\left(q-q_{0}\right)=$ $-\left(\iota^{*} a \iota\right)^{-1} \iota^{*} q_{0}$. Together with (9) this gives
$$\left(\begin{array}{cc}
m & -\stackrel{\circ}{D} \iota_{\iota} \\
-\iota^{*} G & \left(\iota^{*} a \iota\right)^{-1}
\end{array}\right)\binom{u}{\iota^{*}\left(q-q_{0}\right)}=\binom{D}{-\left(\iota^{*} a \iota\right)^{-1} \iota^{*}} q_{0} .$$
Finally use Statement (e). \(\square\)

Next we need a sequential version of Lemma 2.12.
Lemma 4.5. Let $\widetilde{H}$ be a Hilbert space, $M \in \mathcal{L}(\widetilde{H})$ and $A$ a skew-adjoint operator in $\widetilde{H}$. Further let $\left(M_{n}\right)_{n \in \mathbb{N}}$ be a sequence in $\mathcal{L}(\widetilde{H})$ and suppose that $\lim M_{n}=M$ in the weak operator topology on $\mathcal{L}(\widetilde{H})$. Assume that the inclusion $\operatorname{dom}(A) \subset \widetilde{H}$ is compact and that there exists a $\lambda>0$ such that $\operatorname{Re} M_{n} \geqslant \lambda I_{\widetilde{H}}$ for all $n \in \mathbb{N}$. Let $\left(x_{n}\right)_{n \in \mathbb{N}}$ be a sequence in $\widetilde{H}$ which converges weakly to $x \in \widetilde{H}$. Then $M+A$ is invertible and $\lim _{n \rightarrow \infty}\left(M_{n}+A\right)^{-1} x_{n}=$ $(M+A)^{-1} x$ weakly in $\operatorname{dom}(A)$.

Proof. Obviously $\operatorname{Re} M \geqslant \lambda I_{\widetilde{H}}$, so $M+A$ is invertible by Lemma 2.12. Consider $z_{n}=$ $\left(M_{n}+A\right)^{-1} x_{n}$ for all $n \in \mathbb{N}$. Then $\left\|z_{n}\right\|_{\operatorname{dom}(A)} \leqslant \frac{1+\lambda+\left\|M_{n}\right\|}{\lambda}\left\|x_{n}\right\|_{\widetilde{H}}$ for all $n \in \mathbb{N}$ by Lemma 2.12. So the sequence $\left(z_{n}\right)_{n \in \mathbb{N}}$ is bounded in $\operatorname{dom}(A)$. Passing to a subsequence, we may assume without loss of generality that there exists a $z \in \operatorname{dom}(A)$ such that $\lim z_{n}=z$ weakly in $\operatorname{dom}(A)$. Then $\lim z_{n}=z$ in $\widetilde{H}$ by the compactness assumption. Consequently, $\lim M_{n} z_{n}=M z$ weakly in $\widetilde{H}$. Now $M_{n} z_{n}+A z_{n}=x_{n}$ for all $n \in \mathbb{N}$. Take the limit $n \rightarrow \infty$ and notice that both sides converge weakly in $\widetilde{H}$. It follows that $M z+A z=x$, so $z=(M+A)^{-1} x$. Now the lemma follows by a standard subsequence argument. \(\square\)

We need one more convergence result for the proof of Theorem 4.2. This result is also of independent interest.

Proposition 4.6. Suppose that $\lim m_{n}=m$ in the weak operator topology on $\mathcal{L}\left(H_{0}\right)$ and $\lim \left(\iota^{*} a_{n} \iota\right)^{-1}=\left(\iota^{*} a \iota\right)^{-1}$ in the weak operator topology on $\mathcal{L}(\operatorname{ran}(G))$. Let $q, q_{1}, q_{2}, \ldots \in$ $\operatorname{BD}(D)$ and assume that $\lim q_{n}=q$ in $\operatorname{BD}(D)$. Then
$$\lim _{n \rightarrow \infty} \Lambda_{n}^{-1} q_{n}=\Lambda^{-1} q$$
weakly in $\operatorname{BD}(G)$.
Proof. Choose $\widetilde{H}=H_{0} \times \operatorname{ran}(G)$ and let $A=\left(\begin{array}{cc}0 & -\stackrel{\circ}{D} \iota \\ -\iota^{*} G & 0\end{array}\right)$ with $\operatorname{dom}(A)=\operatorname{dom}(G) \times$ $(\operatorname{ran}(G) \cap \operatorname{dom}(\stackrel{\circ}{D}))$. Then $A$ is skew-adjoint in $\widetilde{H}$ by Lemma 4.4(b). Moreover, the inclusion $\operatorname{dom}(A) \subset \widetilde{H}$ is compact by Lemma 4.4(d) and the compactness assumption. Further let
$$M=\left(\begin{array}{cc}
m & 0 \\
0 & \left(\iota^{*} a \iota\right)^{-1}
\end{array}\right) \quad \text { and } \quad M_{n}=\left(\begin{array}{cc}
m_{n} & 0 \\
0 & \left(\iota^{*} a_{n} \iota\right)^{-1}
\end{array}\right)$$
for all $n \in \mathbb{N}$. Then $\lim M_{n}=M$ in the weak operator topology on $\mathcal{L}(\widetilde{H})$. Since
$$\operatorname{Re}\left(\iota^{*} a_{n} \iota\right)^{-1} \geqslant\left\|\iota^{*} a_{n} \iota\right\|_{\mathcal{L}(\operatorname{ran}(G))}^{-2} \operatorname{Re}\left(\iota^{*} a_{n} \iota\right) \geqslant\left\|a_{n}\right\|_{\mathcal{L}\left(H_{1}\right)}^{-2} \operatorname{Re}\left(\iota^{*} a_{n} \iota\right)$$
for all $n \in \mathbb{N}$ and $\sup _{n}\left\|a_{n}\right\|_{\mathcal{L}\left(H_{1}\right)}<\infty$, it follows that there exists a $\lambda>0$ such that $\operatorname{Re} M_{n} \geqslant \lambda I$ for all $n \in \mathbb{N}$. We use Lemma 4.4(g) for $\Lambda^{-1}$ and $\Lambda_{n}^{-1}$. Obviously
$$\lim \left(D q_{n},-\left(\iota^{*} a_{n} \iota\right)^{-1} \iota^{*} q_{n}\right)=\left(D q,-\left(\iota^{*} a \iota\right)^{-1} \iota^{*} q\right)$$
weakly in $\widetilde{H}$. Hence
$$\lim _{n \rightarrow \infty}\left(\begin{array}{cc}
m_{n} & -\AA \iota \\
-\iota^{*} G & \left(\iota^{*} a_{n} \iota\right)^{-1}
\end{array}\right)^{-1}\binom{D}{-\left(\iota^{*} a_{n} \iota\right)^{-1} \iota^{*}} q_{n}=\left(\begin{array}{cc}
m & -\dot{D} \iota \\
-\iota^{*} G & \left(\iota^{*} a \iota\right)^{-1}
\end{array}\right)^{-1}\binom{D}{-\left(\iota^{*} a \iota\right)^{-1} \iota^{*}} q$$
weakly in $\operatorname{dom}(A)$ by Lemma 4.5. Consequently $\lim \Lambda_{n}^{-1} q_{n}=\Lambda^{-1} q$ weakly in $\operatorname{BD}(G)$ by Lemma 4.4(g). \(\square\)

Now we are able to prove the main theorem of this section.
Proof of Theorem 4.2. Let $\psi \in H$. Then $\lim \Lambda_{n}^{-1} G \kappa^{*} \psi=\Lambda^{-1} G \kappa^{*} \psi$ weakly in $\operatorname{BD}(G)$ by Proposition 4.6. Hence
$$\lim _{n \rightarrow \infty}\left(\Lambda_{H}^{(n)}\right)^{-1} \psi=\lim _{n \rightarrow \infty} \kappa \Lambda_{n}^{-1} G \kappa^{*} \psi=\kappa \Lambda^{-1} G \kappa^{*} \psi=\Lambda_{H}^{-1} \psi$$
weakly in $H$. This proves the first statement in Theorem 4.2.
Now suppose that $\kappa$ is compact. Suppose $\lim \left(\Lambda_{H}^{(n)}\right)^{-1}=\Lambda_{H}^{-1}$ in $\mathcal{L}(H)$ is false. Passing to a subsequence if necessary, there exist $\delta>0$ and $\psi_{1}, \psi_{2}, \ldots \in H$ such that
$$\left\|\left(\Lambda_{H}^{(n)}\right)^{-1} \psi_{n}-\Lambda_{H}^{-1} \psi_{n}\right\|_{H}>\delta\left\|\psi_{n}\right\|_{H}$$
for all $n \in \mathbb{N}$. Without loss of generality we may assume that $\left\|\psi_{n}\right\|_{H}=1$ for all $n \in \mathbb{N}$. Passing again to a subsequence if necessary, there exists a $\psi \in H$ such that $\lim \psi_{n}=\psi$
weakly in $H$. Then $\lim \kappa^{*} \psi_{n}=\kappa^{*} \psi$ in $\operatorname{BD}(G)$ since $\kappa$ is compact. Therefore $\lim G \kappa^{*} \psi_{n}=$ $G \kappa^{*} \psi$ in $\operatorname{BD}(D)$. Hence $\lim \Lambda_{n}^{-1} G \kappa^{*} \psi_{n}=\Lambda^{-1} G \kappa^{*} \psi$ weakly in $\operatorname{BD}(G)$ by Proposition 4.6. Using again that $\kappa$ is compact it follows that $\lim \left(\Lambda_{H}^{(n)}\right)^{-1} \psi_{n}=\left(\Lambda_{H}\right)^{-1} \psi$ in $H$. Similarly $\lim \left(\Lambda_{H}\right)^{-1} \psi_{n}=\left(\Lambda_{H}\right)^{-1} \psi$ in $H$. So $\lim \left\|\left(\Lambda_{H}^{(n)}\right)^{-1} \psi_{n}-\Lambda_{H}^{-1} \psi_{n}\right\|_{H}=0$. This contradicts (10) for large $n$. \(\square\)

In Example 6.1 and Proposition 6.2 we show that in the setting of the classical example (Example 2.3) $H$-convergence implies $\lim _{n \rightarrow \infty}\left(\iota^{*} a_{n} \iota\right)^{-1}=\left(\iota^{*} a \iota\right)^{-1}$ in the weak operator topology of $\mathcal{L}(\operatorname{ran}(G))$. Moreover, we compare it with a condition introduced in Section 6. In the real symmetric case we prove in Example 6.7 that all are actually equivalent.

\section*{5 The non-coercive case}

In this section, we drop the coerciveness condition on $m$. As a result the Dirichlet-to-Neumann operator can become multi-valued, that is, it is a graph and no longer an operator. The Dirichlet-to-Neumann graph associated with the Schrödinger operator $-\Delta+m$ has been studied in [AEKS] and [BE1].

Throughout this section we adopt the notation and assumptions as in the beginning of Section 2. Further we fix an element $m \in \mathcal{L}\left(H_{0}\right)$ and a coercive $a \in \mathcal{L}\left(H_{1}\right)$. We emphasise that we do not require that $m$ is coercive. The definition of the Dirichlet-to-Neumann graph, however, remains the same as in the single-valued case in Definition 2.16.

Definition 5.1. Set
$$\Lambda=\left\{\left(\pi_{\mathrm{BD}(G)} u, \pi_{\mathrm{BD}(D)} a G u\right) \in \mathrm{BD}(G) \times \mathrm{BD}(D): u \in \operatorname{dom}(D a G) \text { and } m u-D a G u=0\right\} .$$

We call $\Lambda$ the Dirichlet-to-Neumann graph associated with $-D a G+m$.
We briefly recall some definitions in the area of (linear) graphs. Let $H, K$ be Hilbert spaces. Then a graph $A$ is a vector subspace of $H \times K$. The domain, multi-valued part and inverse of $A$ are defined by
$$\begin{aligned}
\operatorname{dom}(A) & =\{h \in H: \text { there exists a } k \in K \text { such that }(h, k) \in A\}, \\
\operatorname{mul}(A) & =\{k \in K:(0, k) \in A\} \text { and } \\
A^{-1} & =\{(k, h) \in K \times H:(h, k) \in A\} .
\end{aligned}$$
We say that $A$ is single-valued or an operator if $\operatorname{mul}(A)=\{0\}$. The next lemma is trivial.

Lemma 5.2.
\begin{itemize}
\item[(a)] $\operatorname{mul}(\Lambda)=\left\{\pi_{\mathrm{BD}(D)} a G u: u \in \operatorname{ker}(m-D a \stackrel{\circ}{G})\right\}$.
\item[(b)] If $\operatorname{ker}(m-D a \dot{G})=\{0\}$, then $\Lambda$ is single-valued.
\end{itemize}

As in Proposition 3.6 define the sesquilinear form $\mathfrak{b}: \operatorname{dom}(G) \times \operatorname{dom}(G) \rightarrow \mathbb{C}$ by
$$\mathfrak{b}(u, v)=(a G u, G v)_{H_{1}}+(m u, v)_{H_{0}} .$$
We also need the Dirichlet-version of $\mathfrak{b}$ defined by $\stackrel{\circ}{\mathfrak{b}}=\left.\mathfrak{b}\right|_{\operatorname{dom}(\stackrel{\circ}{G}) \times \operatorname{dom}(\stackrel{\circ}{G})}$. Then $\mathfrak{b}$ and $\stackrel{\circ}{\mathfrak{b}}$ are continuous. Hence there exist $T \in \mathcal{L}(\operatorname{dom}(G))$ and $\stackrel{\circ}{T} \in \mathcal{L}(\operatorname{dom}(\stackrel{\circ}{G}))$ such that $\mathfrak{b}(u, v)=$ $(T u, v)_{\operatorname{dom}(G)}$ for all $u, v \in \operatorname{dom}(G)$ and $\stackrel{\circ}{\mathfrak{b}}(u, v)=(\stackrel{\circ}{T} u, v)_{\operatorname{dom}(\dot{G})}$ for all $u, v \in \operatorname{dom}(\stackrel{\circ}{G})$. Note that $\operatorname{ker}(\stackrel{\circ}{T})=\operatorname{ker}(m-D a \stackrel{\circ}{G})$, since $(\stackrel{\circ}{G})^{*}=-D$.

With a condition on $\operatorname{ran}(\stackrel{\circ}{T})$ we can characterise the domain of the Dirichlet-to-Neumann graph $\Lambda$.

Proposition 5.3. Suppose that $\operatorname{ran}(\stackrel{\circ}{T})$ is closed in $\operatorname{dom}(\stackrel{\circ}{G})$. Then
$$\operatorname{dom}(\Lambda)=\left\{u_{0} \in \operatorname{BD}(G):\left(G u_{0}, \pi_{\mathrm{BD}(D)} a^{*} G v\right)_{\mathrm{BD}(D)}=0 \text { for all } v \in \operatorname{ker}\left(m^{*}-D a^{*} \dot{G}\right)\right\} .$$

Proof. ' $\subset$ '. Let $u_{0} \in \operatorname{dom}(\Lambda)$. Then there exists a $u \in \operatorname{dom}(G)$ such that $m u-D a G u=0$ and $u_{0}=\pi_{B D(G)} u$. Let $v \in \operatorname{dom}(\stackrel{\circ}{G})$. Then $(m u, v)_{H_{0}}=(D a G u, v)_{H_{0}}=-(a G u, \stackrel{\circ}{G} v)_{H_{1}}$ and
$$\begin{aligned}
\left(\stackrel{\circ}{T}\left(u-u_{0}\right), v\right)_{\operatorname{dom}(\stackrel{\circ}{G})}=\stackrel{\circ}{\mathfrak{b}}\left(u-u_{0}, v\right) & =\left(a G\left(u-u_{0}\right), \stackrel{\circ}{G} v\right)_{H_{1}}+\left(m\left(u-u_{0}\right), v\right)_{H_{0}} \\
& =-\left(a G u_{0}, \stackrel{\circ}{G} v\right)_{H_{1}}-\left(m u_{0}, v\right)_{H_{0}} .
\end{aligned}$$
Note that $\stackrel{\circ}{T}\left(u-u_{0}\right) \in \operatorname{ran}(\stackrel{\circ}{T})=\left(\operatorname{ker}\left((\stackrel{\circ}{T})^{*}\right)\right)^{\perp_{\operatorname{dom}(\check{G})}}$ since $\operatorname{ran}(\stackrel{\circ}{T})$ is closed.
Now let $v \in \operatorname{ker}\left(m^{*}-D a^{*} \stackrel{\circ}{G}\right)=\operatorname{ker}\left((\stackrel{\circ}{T})^{*}\right)$. Then
$$\begin{aligned}
0 & =-\left(\stackrel{\circ}{T}\left(u-u_{0}\right), v\right)_{\operatorname{dom}(\stackrel{\circ}{G})}=\left(a G u_{0}, \stackrel{\circ}{G} v\right)_{H_{1}}+\left(m u_{0}, v\right)_{H_{0}} \\
& =\left(G u_{0}, a^{*} \dot{G} v\right)_{H_{1}}+\left(u_{0}, m^{*} v\right)_{H_{0}} \\
& =\left(G u_{0}, a^{*} \dot{G} v\right)_{H_{1}}+\left(D G u_{0}, D a^{*} \dot{G} v\right)_{H_{0}} \\
& =\left(G u_{0}, a^{*} \dot{G} v\right)_{\operatorname{dom}(D)}=\left(G u_{0}, \pi_{\mathrm{BD}(D)} a^{*} \dot{G} v\right)_{\mathrm{BD}(D)}
\end{aligned}$$
as required.
' $\supset$ '. The proof is similar and for this inclusion it is essential that $\operatorname{ran}(\stackrel{\circ}{T})$ is closed. \(\square\)

Corollary 5.4. Suppose that $\operatorname{ran}(\stackrel{\circ}{T})$ is closed in $\operatorname{dom}(\stackrel{\circ}{G})$. Then
$$\operatorname{dom}(\Lambda)=\left\{u_{0} \in \operatorname{BD}(G):\left(\Phi\left(\pi_{\mathrm{BD}(D)} a^{*} G v\right)\right)\left(u_{0}\right)=0 \text { for all } v \in \operatorname{ker}\left(m^{*}-D a^{*} \dot{G}\right)\right\},$$
where $\Phi: \operatorname{BD}(D) \rightarrow \operatorname{BD}(G)^{\prime}$ is the natural unitary map as in Proposition 2.8.
We emphasise that boundary regularity is not needed in Corollary 5.4. The next lemma gives an easy to verify condition which implies that $\stackrel{\circ}{T}$ has closed range.

Lemma 5.5. If the inclusion $\tau: \operatorname{dom}(\stackrel{\circ}{G}) \rightarrow H_{0}$ is compact, then $\stackrel{\circ}{T}$ has closed range.
Proof. There exist $\mu, \omega>0$ such that $\mu\|u\|_{\operatorname{dom}(\dot{G})}^{2} \leqslant \operatorname{Re} \stackrel{\circ}{\mathfrak{b}}(u)+\omega\|\tau u\|_{H_{0}}^{2}$ for all $u \in \operatorname{dom}(\stackrel{\circ}{G})$. Then $\mu\|u\|_{\operatorname{dom}(\stackrel{\circ}{G})}^{2} \leqslant \operatorname{Re}(\stackrel{\circ}{T} u, u)_{\operatorname{dom}(\stackrel{\circ}{G})}+\omega\left(\tau^{*} \tau u, u\right)_{\operatorname{dom}(\stackrel{\circ}{G})}=\operatorname{Re}\left(\left(\stackrel{\circ}{T}+\omega \tau^{*} \tau\right) u, u\right)_{\operatorname{dom}(\stackrel{\circ}{G})}$ for all $u \in \operatorname{dom}(\stackrel{\circ}{G})$. So $\stackrel{\circ}{T}+\omega \tau^{*} \tau$ is injective and has closed range. Similarly $(\stackrel{\circ}{T})^{*}+\omega \tau^{*} \tau$ is injective. So $\stackrel{\circ}{T}+\omega \tau^{*} \tau$ is invertible. Since $\omega \tau^{*} \tau$ is compact, the operator $\stackrel{\circ}{T}$ is Fredholm. In particular, the range of $\stackrel{\circ}{T}$ is closed. \(\square\)

Note that the operator $\tau$ is compact in the situation of Example 2.3.
Example 5.6. Let $\Omega \subset \mathbb{R}^{d}$ be a bounded Lipschitz domain with boundary $\Gamma$. Let $G$ and $D$ be as in Example 2.3. If $u_{0} \in \mathrm{BD}(G), v \in H_{0}$ and $\Phi: \operatorname{BD}(D) \rightarrow \operatorname{BD}(G)^{\prime}$ is the natural unitary map as in Proposition 2.8, then it follows from Example 2.10 and Proposition 2.9(b) that
$$\begin{aligned}
\left(\Phi\left(\pi_{\mathrm{BD}(D)} a^{*} G v\right)\right)\left(u_{0}\right) & =\left\langle\left(\nu \pi_{\mathrm{BD}(D)} a^{*} G v\right), \operatorname{Tr} u_{0}\right\rangle_{\left(\operatorname{Tr} H^{1}(\Omega)\right)^{\prime} \times \operatorname{Tr} H^{1}(\Omega)} \\
& =\left\langle\left(\nu a^{*} G v\right), \operatorname{Tr} u_{0}\right\rangle_{\left(\operatorname{Tr} H^{1}(\Omega)\right)^{\prime} \times \operatorname{Tr} H^{1}(\Omega)} \\
& =\left\langle\left(\partial_{\nu}^{a^{*}} v\right), \operatorname{Tr} u_{0}\right\rangle_{H^{-1 / 2}(\partial \Omega), H^{1 / 2}(\partial \Omega)},
\end{aligned}$$
where $\partial_{\nu}^{a^{*}}$ is the co-normal derivative. So Corollary 5.4 gives
$$\operatorname{dom}(\Lambda)=\left\{u_{0} \in \operatorname{BD}(G):\left\langle\left(\partial_{\nu}^{a^{*}} v\right), \operatorname{Tr} u_{0}\right\rangle_{H^{-1 / 2}(\partial \Omega), H^{1 / 2}(\partial \Omega)}=0 \text { for all } v \in \operatorname{ker}\left(m^{*}-D a^{*} \dot{G}\right)\right\},$$
in agreement with [McL] Proposition 4.10.
Next we turn to the Neumann-to-Dirichlet graph.
Proposition 5.7. Assume that $\operatorname{ran}(T)$ is closed in $\operatorname{dom}(G)$. Then
$$\operatorname{dom}\left(\Lambda^{-1}\right)=\left\{q_{0} \in \operatorname{BD}(D):\left(D q_{0}, \pi_{\mathrm{BD}(G)} v\right)_{\mathrm{BD}(G)}=0 \text { for all } v \in \operatorname{ker}\left(m^{*}-\stackrel{\circ}{D} a^{*} G\right)\right\} .$$
Before we prove the latter proposition, we need a lemma.
Lemma 5.8. Let $q_{0} \in \operatorname{BD}(D)$. Let $f_{0} \in \operatorname{dom}(G)$ be such that
$$\left(f_{0}, v\right)_{\operatorname{dom}(G)}=\left(D q_{0}, \pi_{\mathrm{BD}(G)} v\right)_{\mathrm{BD}(G)}$$
for all $v \in \operatorname{dom}(G)$. Let $u \in \operatorname{dom}(G)$. Then the following statements are equivalent.
\begin{itemize}
\item[(i)] $T u=f_{0}$.
\item[(ii)] $\quad u \in \operatorname{dom}(D a G), m u-D a G u=0$ and $q_{0}=\pi_{\mathrm{BD}(D)} a G u$.
\end{itemize}

Proof. (i) $\Rightarrow$ (ii) . Let $v \in \operatorname{dom}(G)$. Then
$$(m u, v)_{H_{0}}+(a G u, G v)_{H_{1}}=\mathfrak{b}(u, v)=(T u, v)_{\operatorname{dom}(G)}=\left(f_{0}, v\right)_{\operatorname{dom}(G)}=\left(D q_{0}, \pi_{\mathrm{BD}(G)} v\right)_{\mathrm{BD}(G)} .$$
Hence $(m u, v)_{H_{0}}+(a G u, \stackrel{\circ}{G} v)_{H_{1}}=0$ for all $v \in \operatorname{dom}(\stackrel{\circ}{G})$. So $a G u \in \operatorname{dom}\left((\stackrel{\circ}{G})^{*}\right)=\operatorname{dom}(D)$ and $D a G u=-(\dot{G})^{*} a G u=m u$. In particular, $u \in \operatorname{dom}(D a G)$. Alternatively, if $v \in \operatorname{BD}(G)$, then
$$\begin{aligned}
\left(D q_{0}, v\right)_{\mathrm{BD}(G)} & =\left(D q_{0}, \pi_{\mathrm{BD}(G)} v\right)_{\mathrm{BD}(G)}=(m u, v)_{H_{0}}+(a G u, G v)_{H_{1}} \\
& =(D a G u, D G v)_{H_{0}}+(a G u, G v)_{H_{1}}=(a G u, G v)_{\operatorname{dom}(D)} \\
& =\left(\pi_{\mathrm{BD}(D)} a G u, G v\right)_{\mathrm{BD}(D)}=\left(D \pi_{\mathrm{BD}(D)} a G u, v\right)_{\mathrm{BD}(G)}
\end{aligned}$$
by Lemma 2.7. So $q_{0}=\pi_{\mathrm{BD}(D)} a G u$.
(ii) ⇒ . Let $v \in \operatorname{dom}(\stackrel{\circ}{G})$. Since $(\stackrel{\circ}{G})^{*}=-D$ one deduces that
$$\begin{aligned}
(T u, v)_{\operatorname{dom}(G)} & =\mathfrak{b}(u, v)=(a G u, \stackrel{\circ}{G} v)_{H_{1}}+(m u, v)_{H_{0}} \\
& =-(D a G u, v)_{H_{0}}+(m u, v)_{H_{0}}=0=\left(D q_{0}, \pi_{\mathrm{BD}(G)} v\right)_{\mathrm{BD}(G)}=\left(f_{0}, v\right)_{\operatorname{dom}(G)} .
\end{aligned}$$
Alternatively, if $v \in \mathrm{BD}(G)$, then
$$\begin{aligned}
(T u, v)_{\operatorname{dom}(G)} & =\mathfrak{b}(u, v)=(a G u, G v)_{H_{1}}+(m u, v)_{H_{0}} \\
& =(a G u, G v)_{H_{1}}+(D a G u, D G v)_{H_{0}} \\
& =(a G u, G v)_{\operatorname{dom}(D)}=\left(\pi_{\mathrm{BD}(D)} a G u, G v\right)_{\mathrm{BD}(D)}=\left(q_{0}, G v\right)_{\mathrm{BD}(D)} \\
& =\left(D q_{0}, v\right)_{\mathrm{BD}(G)}=\left(f_{0}, v\right)_{\operatorname{dom}(G)} .
\end{aligned}$$
So by linearity $(T u, v)_{\operatorname{dom}(G)}=\left(f_{0}, v\right)_{\operatorname{dom}(G)}$ for all $v \in \operatorname{dom}(G)$ and $T u=f_{0}$. \(\square\)

Proof of Proposition 5.7. Let $q_{0} \in \operatorname{BD}(D)$. Let $f_{0} \in \operatorname{dom}(G)$ be as in Lemma 5.8. Then it follows from Lemma 5.8 that $q_{0} \in \operatorname{dom}\left(\Lambda^{-1}\right)$ if and only if $f_{0} \in \operatorname{ran}(T)$. But $\operatorname{ran}(T)=\left(\operatorname{ker}\left(T^{*}\right)\right)^{\perp_{\operatorname{dom}(G)}}$ since $\operatorname{ran}(T)$ is closed in dom $(G)$. Now $\operatorname{ker}\left(T^{*}\right)=\operatorname{ker}\left(m^{*}-\stackrel{\circ}{D}^{*} G\right)$ because $G^{*}=-\stackrel{\circ}{D}$. Hence $f_{0} \in \operatorname{ran}(T)$ if and only if $\left(D q_{0}, \pi_{\mathrm{BD}(G)} v\right)_{\mathrm{BD}(G)}=0$ for all $v \in \operatorname{ker}\left(m^{*}-\stackrel{\circ}{D} a^{*} G\right)$. \(\square\)

As in Lemma 5.5 one has the following sufficient condition for the closedness of $\operatorname{ran}(T)$.
Lemma 5.9. If the inclusion $\operatorname{dom}(G) \subset H_{0}$ is compact, then $\operatorname{ran}(T)$ is closed in $\operatorname{dom}(G)$.
In our model case Example 2.3, the inclusion $\operatorname{dom}(G) \subset H_{0}$ is compact if $\Omega$ has a continuous boundary.

We conclude with a variant of the Dirichlet-to-Neumann graph involving an intermediate space as in Section 3. Throughout the remainder of this section let $H$ be a Hilbert space and $\kappa \in \mathcal{L}(\mathrm{BD}(G), H)$ injective with dense range. Define
$$\begin{array}{r}
\Lambda_{H}=\left\{(\varphi, \psi) \in H \times H: \text { there exists a } u_{0} \in \operatorname{BD}(G)\right. \text { such that } \\
\left.\kappa\left(u_{0}\right)=\varphi \text { and }\left(u_{0}, G \kappa^{*} \psi\right) \in \Lambda\right\} .
\end{array}$$
We call $\Lambda_{H}$ the Dirichlet-to-Neumann graph in $H$ associated with $-D a G+m$. It follows from Lemma 5.2 that $\Lambda_{H}$ is single-valued if $\operatorname{ker}(m-D a \stackrel{\circ}{G})=\{0\}$.

The graph $\Lambda_{H}$ can be described with a form.
Proposition 5.10. Define $j: \operatorname{dom}(G) \rightarrow H$ by $j=\kappa \circ \pi_{\mathrm{BD}(G)}$. Then
$$\begin{aligned}
& \Lambda_{H}=\{(\varphi, \psi) \in H \times H: \text { there exists a } u \in \operatorname{dom}(G) \text { such that } \\
& \left.\qquad j(u)=\varphi \text { and } \mathfrak{b}(u, v)=(\psi, j(v))_{\operatorname{dom}(G)} \text { for all } v \in \operatorname{dom}(G)\right\} .
\end{aligned}$$

Proof. This follows as in the proof of Proposition 3.6. \(\square\)

Corollary 5.11. If $\operatorname{ker}(-D a \stackrel{\circ}{G}+m)=\{0\}$ and the inclusion $\operatorname{dom}(G) \subset H_{0}$ is compact, then $\Lambda_{H}$ is an $m$-sectorial operator.
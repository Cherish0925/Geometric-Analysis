---
retention_scope: session
part: 1
total_parts: 1
---

---
source_file: 1905_01284.pdf
converter: mathpix
format: mmd
---

\title{
ON THE DIASTATIC ENTROPY AND $\mathcal{C}^{1}$-RIGIDITY OF COMPLEX HYPERBOLIC MANIFOLDS
}

\author{
ROBERTO MOSSA
}

\begin{abstract}
Let $f:(Y, g) \rightarrow\left(X, g_{0}\right)$ be a non zero degree continuous map between compact Kähler manifolds of dimension $n \geq 2$, where $g_{0}$ has constant negative holomorphic sectional curvature. Adapting the Besson-Courtois-Gallot barycentre map techniques to the Kähler setting, we prove a gap theorem in terms of the degree of $f$ and the diastatic entropies of $(Y, g)$ and $\left(X, g_{0}\right)$ which extends the rigidity result proved by the author in [13].
\end{abstract}

\section*{Contents}
\begin{itemize}
\item[1.] Introduction and statement of the main results
\item[2.] Diastatic hessian and HSSNCT
\item[3.] The barycentre map $\widetilde{F}_{c}$
\item[4.] The proof of Theorem 1 and Theorem 2.
\end{itemize}

References

\section*{1. Introduction and statement of the main results}

It is a classical problem to determine when a continuous map between two closed smooth manifolds is homotopic to a more regular one. Of course, the father of this problems is the celebrated Mostow Rigidity Theorem which was beautifully extended in the seminal paper [2] (see also [1, 3, 4]) by G. Besson, G. Courtois and S. Gallot. This is expressed by the following result which combined with barycentre techniques developed in its proof has provided a solution of long-standing problems. Denoted by $\operatorname{Ent}_{\mathrm{v}}(M, g)$ the volume entropy of a compact Riemannian manifold $(M, g)$ we have:

Theorem A (G. Besson, G. Courtois, S. Gallot). Let $(Y, g)$ be a compact Riemannian manifold of dimension $n \geq 3$ and let $\left(X, g_{0}\right)$ be a compact negatively curved locally symmetric Riemannian manifold of the same dimension of $Y$. If

\footnotetext{
Date: November 27, 2024.
The author research was supported by FAPESP (FAPESP grant: 2018/08971-9).
}
$f: Y \rightarrow X$ is a nonzero degree continuous map, then
$$\operatorname{Ent}_{\mathrm{v}}{ }^{n}(Y, g) \operatorname{Vol}(Y, g) \geq|\operatorname{deg}(f)| \operatorname{Ent}_{\mathrm{v}}{ }^{n}\left(X, g_{0}\right) \operatorname{Vol}\left(X, g_{0}\right) .$$
Moreover, the equality is attained if and only if $f$ is homotopic to a homothetic covering $F: Y \rightarrow X$.

The following theorem (Theorem B), proved by the author of the present paper in [13], represents an extension of Theorem A in the Kähler setting by substituting the volume entropy with the diastatic entropy (introduced in [12] and studied in [10] in the homogeneous setting). We briefly recall its definition for reader convenience. Let $\pi:(\widetilde{Y}, \widetilde{g}) \rightarrow(Y, g)$ be the universal Kähler covering (i.e. $\pi$ is a holomorphic covering map and $\pi^{*} g=\widetilde{g}$ ) of a compact Kähler manifold $(Y, g)$ and assume that the diastasis function $\mathcal{D}: \widetilde{Y} \times \widetilde{Y} \rightarrow \mathbb{R}$ is globally defined, that is, defined in whole $\widetilde{Y} \times \widetilde{Y}$ (see next section of the definition of diastasis function). Then, the diastatic entropy of $(Y, g)$ is the Kähler invariant of $g$ given by
$$\operatorname{Ent}_{\mathrm{d}}(Y, g)=\mathcal{X}(\widetilde{g}) \inf \left\{c \in \mathbb{R}^{+}: \int_{\widetilde{Y}} e^{-c \mathcal{D}_{q}} \nu_{\widetilde{g}}<\infty\right\},$$
where $\mathcal{X}(\widetilde{g})=\sup _{p, q \in \widetilde{Y}}\left\|\operatorname{grad}_{p} \mathcal{D}_{q}\right\|$ and $\nu_{\widetilde{g}}$ is the volume form associated to $\widetilde{g}$. If $\mathcal{X}(\widetilde{g})=\infty$ or the infimum in (2) is not achieved by any $c \in \mathbb{R}^{+}$, we set $\operatorname{Ent}_{\mathrm{d}}(Y, g)=$ $\infty$. It is not hard to see that this definition is independent on the point $q$ (see [13] for details).

Theorem B. Let $(Y, g)$ be a compact Kähler manifold of complex dimension $n \geq 2$ and let $\left(X, g_{0}\right)$ be a compact complex hyperbolic manifold ${ }^{1}$ of the same dimension of $Y$. If $f: Y \rightarrow X$ is a nonzero degree continuous map, then
$$\operatorname{Ent}_{\mathrm{d}}{ }^{2 n}(Y, g) \operatorname{Vol}(Y, g) \geq|\operatorname{deg}(f)| \operatorname{Ent}_{\mathrm{d}}{ }^{2 n}\left(X, g_{0}\right) \operatorname{Vol}\left(X, g_{0}\right) .$$
Moreover, if $g$ and $g_{0}$ are rescaled so that $\operatorname{Ent}_{\mathrm{d}}(Y, g)=\operatorname{Ent}_{\mathrm{d}}\left(X, g_{0}\right)$, the equality is attained if and only if $f$ is homotopic to a holomorphic or anti-holomorphic isometric covering $F: Y \rightarrow X$.

Later on, S. Gallot extends Theorem A by proving the following gap result (Theorem C). Before stating his result we need the following definitions. We say that a Riemannian manifold $(Y, g)$ of dimension $m$ has bounded Hessian if, for any point $p$ of its Riemannian universal covering $(\widetilde{Y}, \widetilde{g})$, there exists a positive constant $C$ such that $\left|\lambda_{j}^{p}\right|<C$, for all $j=1, \ldots, m$, where $\lambda_{j}^{p}$ are the eingenvalues of the Hessian of $\tilde{\rho}_{p}$, the geodesic distance from $p$. We say that a family $F_{\epsilon}: Y \rightarrow X, \epsilon>0$,

\footnotetext{
${ }^{1}$ Notice that a negatively curved locally hermitian symmetric Kähler manifold is authomatically a complex hyperbolic manifold, namely its holomorphic sectional curvature is constant. This is the reason, together with the use of diastatic entropy instead of the volume entroopy, why Theorem B can be considered an extension to the Kähler setting of Theorem A.
}
of $\mathcal{C}^{1}$-maps between two compact Riemannian manifolds of the same dimension $m$ is almost-isometric if there exist two constants $A^{\prime}(\epsilon)$ and $A^{\prime \prime}(\epsilon)$ determined by $m$ and $\epsilon$ such that
$$A^{\prime}(\epsilon) \leq \frac{\left\|d_{p} F_{\epsilon}(u)\right\|}{\|u\|} \leq A^{\prime \prime}(\epsilon)$$
where $A^{\prime}(\epsilon) \rightarrow 1$ and $A^{\prime \prime}(\epsilon) \rightarrow 1$ as $\epsilon \rightarrow 0$.
Theorem C (S. Gallot (unpublished, private comunications)). Let $(Y, g)$ be a compact Riemannian manifold with bounded Hessian of dimension $m \geq 3$ and let $\left(X, g_{0}\right)$ be a compact negatively curved locally symmetric Riemannian manifold of the same dimension of $Y$. If $f: Y \rightarrow X$ is a non zero degree continuous map and there exists a sufficiently small positive constant $\epsilon$ such that
$$\operatorname{Ent}_{\mathrm{v}}{ }^{m}(Y, g) \operatorname{Vol}(Y, g)-|\operatorname{deg}(f)| \operatorname{Ent}_{\mathrm{v}}{ }^{m}\left(X, g_{0}\right) \operatorname{Vol}\left(X, g_{0}\right) \leq \epsilon,$$
then $f$ is homotopic to a $\mathcal{C}^{1}$-covering $F_{\epsilon}: Y \rightarrow X$.
Moreover, if $g$ and $g_{0}$ are normalized so that $\operatorname{Ent}_{\mathrm{v}}(Y, g)=\operatorname{Ent}_{\mathrm{v}}\left(X, g_{0}\right)$, then $F_{\epsilon}$ is almost-isometric. Furthermore if $\epsilon=0$, then $F_{0}$ is an isometric covering.

The aim of the present paper is to analyze to what extent the analogous of Theorem C holds true in the Kähler setting by substituting the volume entropy with the diastatic entropy.

In order to state Theorem 1 we need the following definitions analogous to those needed in the statement of Theorem C. We say that a Kähler manifold $(Y, g)$ has bounded diastatic Hessian if, for any point $p$ of its universal Kähler covering $(\widetilde{Y}, \widetilde{g})$ the following two conditions hold true:
$$\int_{\widetilde{Y}} \widetilde{\rho}_{p}(q) e^{-c \mathcal{D}_{p}(q)} \nu_{\widetilde{g}}(q)<\infty, \quad \forall c>\frac{\operatorname{Ent}_{\mathrm{d}}(Y, g)}{\mathcal{X}(\widetilde{g})} ;$$
there exists a positive constant $C$ such that
$$\left|\lambda_{j}^{p}\right|<C, \quad j=1, \ldots, m,$$
where $\lambda_{j}^{p}$ are the eingenvalues the Hessian of the diastasis $\mathcal{D}_{p}$.
Theorem 1. Let $(Y, g)$ be a compact Kähler manifold of complex dimension $n \geq 2$ with bounded diastatic Hessian and let $\left(X, g_{0}\right)$ be a compact complex hyperbolic manifold of the same dimension of $Y$. If $f: Y \rightarrow X$ is a non zero degree continuous map and there exists a sufficiently small positive constant $\epsilon$ such that
$$\operatorname{Ent}_{\mathrm{d}}{ }^{2 n}(Y, g) \operatorname{Vol}(Y, g)-|\operatorname{deg}(f)| \operatorname{Ent}_{\mathrm{d}}{ }^{2 n}\left(X, g_{0}\right) \operatorname{Vol}\left(X, g_{0}\right) \leq \epsilon,$$
then $f$ is homotopic to a $\mathcal{C}^{1}$-covering $F_{\epsilon}: Y \rightarrow X$. Moreover, if $g$ and $g_{0}$ are normalized so that $\operatorname{Ent}_{\mathrm{d}}(Y, g)=\operatorname{Ent}_{\mathrm{d}}\left(X, g_{0}\right)$, then $F_{\epsilon}$ is almost-isometric. Furthermore if $\epsilon=0$, then $F_{0}$ is a holomorphic or anti-holomorphic isometric covering.

Remark 1.1. We believe that the map $F_{\epsilon}$ in Theorem 1 is indeed a diffeomorphism and that condition (4) is redundant.

Conditions (4) and (5) are somehow technical, so it is natural to seek for more topological and geometrical ones yielding to the same conclusions of Theorem 1. This is achieved in Theorem 2 below which represents our second result. One first topological condition is the following. Let $\left(M_{1}, g_{1}\right)$ and $\left(M_{2}, g_{2}\right)$ be two Riemannian manifolds. We will say that $M_{1}$ is a strongly proper submanifold of $M_{2}$ if there exists an isometric immersion $\varphi:\left(M_{1}, g_{1}\right) \rightarrow\left(M_{2}, g_{2}\right)$, called a strongly proper map, such that one of its lift $\widetilde{\varphi}:\left(\widetilde{M_{1}}, \widetilde{g_{1}}\right) \rightarrow\left(\widetilde{M_{2}}, \widetilde{g_{2}}\right)$ to the Riemannian universal covering manifolds satisfies the following condition: for any $\mu>0$ and $q \in \widetilde{M}_{1}$, there exist two constants $L_{1}$ and $L_{2}$, such that
$$\tilde{\rho}_{1}(q, p)<L_{1} e^{\mu \tilde{\rho}_{2}(\widetilde{\varphi}(q), \widetilde{\varphi}(p))}+L_{2}, \quad \forall p \in \widetilde{M}_{1}$$
where $\tilde{\rho}_{1}$ and $\tilde{\rho}_{2}$ are the geodesics distances on $\left(\widetilde{M}_{1}, \widetilde{g}_{1}\right)$ and $\left(\widetilde{M}_{2}, \widetilde{g}_{2}\right)$ respectively. Notice that the previous definition does not depend on the chosen lift and that an isometric immersion $\varphi:\left(M_{1}, g_{1}\right) \rightarrow\left(M_{2}, g_{2}\right)$ is strongly proper if there exists a polynomial $P$ such that $\rho_{1}(q, p)<P\left(\rho_{2}(\widetilde{\varphi}(q), \widetilde{\varphi}(p))\right)$.

Theorem 2. Let $(Y, g)$ be a compact Kähler manifold of complex dimension $m \geq 2$ which is a strongly proper Kähler submanifold of a classical local hermitian symmetric space of non compact type and let $\left(X, g_{0}\right)$ be a compact complex hyperbolic manifold of the same dimension of $Y$. If $f: Y \rightarrow X$ is a non zero degree continuous map satisfying (6) above, then the same conclusions of Theorem 1 holds true.

The paper is organized as follows. In section 2 after recalling the main properties of Calabi's diastasis function and diastatic hessian, we focus on the properties of hermitian symmetric spaces of noncompact type needed in the proof of the main results. Section 3 is dedicated to the definition and main properties of the barycentre map in the Kähler setting. Finally Section 4 contains the proof of Theorem 1 and 2.

Acknowledgments. The author would like to thank Professor Sylvestre Gallot and Professor Fabio Zuddas for various stimulating discussions and their valuable comments. The author gratefully thanks the referee for the constructive comments and recommendations which definitely help to improve the readability and quality of the paper.

\section*{2. Diastatic hessian and HSSNCT}

First briefly recall the definition of diastasis function. Let $(\widetilde{Y}, \widetilde{g})$ be a real analytic Kähler manifold, namely a complex manifold $\widetilde{Y}$ endowed with a real analytic

Kähler metric $\widetilde{g}$. A real analytic Kähler metric $\widetilde{g}$ is characterized for the local existence of a real analytic function $\Phi: V \rightarrow \mathbb{R}$, called Kähler potential, such that $\widetilde{\omega}_{\mid V}=\frac{i}{2} \partial \bar{\partial} \Phi$, where $\widetilde{\omega}$ is the Kähler form associated to $\widetilde{g}$. Let $z=\left(z_{1}, \ldots, z_{n}\right)$ be local coordinates around a point $p_{0} \in V$, by duplicating the variables $z$ and $\bar{z}$ the real analytic Kähler potential $\Phi$ can be complex analytically continued to a function $\hat{\Phi}: U \times U \rightarrow \mathbb{C}$ defined in a neighborhood $U \times U \subset V \times V$ of $\left(p_{0}, p_{0}\right)$ which is holomorphic in the first entry and antiholomorphic in the second entry. E. Calabi in its seminal paper [5], introduced the diastasis function $\mathcal{D}: U \times U \rightarrow \mathbb{R}$, the Kähler invariant defined by:
$$\mathcal{D}(p, q):=\hat{\Phi}(z(p), \overline{z(p)})+\hat{\Phi}(z(q), \overline{z(q)})-\hat{\Phi}(z(p), \overline{z(q)})-\hat{\Phi}(z(q), \overline{z(p)}) .$$
One can see that it is uniquely determined by the Kähler metric $\widetilde{g}$, i.e. does not depend on the choice of the Kähler potential $\Phi$ or on the local system of coordinates. Moreover, when we fix one of its entries, let's say $p$, then the diastasis centred in $p$, $\mathcal{D}_{p}: U \rightarrow \mathbb{R}$ given by $\mathcal{D}_{p}(q):=\mathcal{D}(p, q)$ is a Kähler potential. The reader is referred to [9] for further details and for an updated account on projectively induced Kähler metrics.

In the proof of our results we need the following two lemmas about the diastasis function and Proposition 2.3 that summarize the properties of classical Hermitian symmetric spaces of non compact type (from now on HSSNCT). The interested reader can find in [12] and [11] a computation of the diastatic entropy and the volume entropy of a HSSNCT.

Lemma 2.1 (E. Calabi [5]). Let $\psi:\left(M_{1}, g_{1}\right) \rightarrow\left(M_{2}, g_{2}\right)$ be a holomorphic and isometric immersion between Kähler manifolds and suppose that $g_{2}$ is real analytic. Then $g_{1}$ is real analytic and for every couple of points $p, q \in M_{1}$
$$\mathcal{D}^{M_{1}}(p, q)=\mathcal{D}^{M_{2}}(\psi(p), \psi(q)),$$
where $\mathcal{D}^{M_{1}}$ and $\mathcal{D}^{M_{2}}$ are respectively the diastasis of $\left(M_{1}, g_{1}\right)$ and $\left(M_{2}, g_{2}\right)$.

Lemma 2.2. Let $\psi:\left(M_{1}, g_{1}\right) \rightarrow\left(M_{2}, g_{2}\right)$ be a holomorphic and isometric immersion between Kähler manifolds and suppose that $M_{2}$ has globally defined diastasis $\mathcal{D}^{M_{2}}: M_{2} \times M_{2} \rightarrow \mathbb{R}$. Then $M_{1}$ has globally defined diastasis $\mathcal{D}^{M_{1}}: M_{1} \times M_{1} \rightarrow \mathbb{R}$ given by
$$\mathcal{D}^{M_{1}}(p, q)=\mathcal{D}^{M_{2}}(\psi(p), \psi(q)) .$$
In particular the gradients and the hessians of $\mathcal{D}^{M_{1}}$ and $\mathcal{D}^{M_{2}}$ are (locally) related by the following identities:
$$\psi_{*}\left(\operatorname{grad}_{p} \mathcal{D}_{q}^{M_{1}}\right)=\pi\left(\operatorname{grad}_{\psi(p)} \mathcal{D}_{\psi(q)}^{M_{2}}\right)$$
where $\pi: T_{\psi(p)} M_{2} \rightarrow \psi_{*}\left(T_{p} M_{1}\right)$ is the orthogonal projection, and
$$\operatorname{Hess}_{\psi(p)} \mathcal{D}_{\psi(q)}^{M_{2}}\left(\psi_{*} \xi, \psi_{*} \zeta\right)=\operatorname{Hess}_{p} \mathcal{D}_{q}^{M_{1}}(\xi, \zeta)+\mathrm{II}_{p}(\xi, \zeta) \mathcal{D}_{q}^{M_{2}},$$
where $\mathrm{II}_{p}$ is the second fundamental form at $p \in M_{1}$.
Proof. Equality (9) is an immediate consequence of Lemma 2.1. Equality (10) is easily achieved: let $E_{1}, \ldots, E_{2 n}$ be an orthonormal basis of $T_{p} M_{1}, p \in M_{1}$ then
$$\begin{gathered}
\psi_{*}\left(\operatorname{grad}_{p} \mathcal{D}_{q}^{M_{1}}\right)=\sum_{k=1}^{2 n}\left(E_{k} \mathcal{D}_{q}^{M_{1}}\right) \psi_{*} E_{k}=\sum_{k=1}^{2 n}\left(E_{k} \mathcal{D}_{\psi(q)}^{M_{2}} \circ \psi\right) \psi_{*} E_{k} \\
=\sum_{k=1}^{2 n}\left(\psi_{*} E_{k}\right) \mathcal{D}_{\psi(q)}^{M_{2}} \psi_{*} E_{k}=\pi\left(\operatorname{grad}_{\psi(p)} \mathcal{D}_{\psi(q)}^{M_{2}}\right)
\end{gathered}$$
It remains to prove (11) For any $\xi, \zeta \in T_{p} M_{1}$ we have
$$\operatorname{Hess}_{p} \mathcal{D}_{q}^{M_{1}}(\xi, \zeta)=\xi\left(\zeta \mathcal{D}_{q}^{M_{1}}\right)-\left(\nabla_{\xi}^{M_{1}} \zeta\right) \mathcal{D}_{q}^{M_{1}}$$
and
$$\operatorname{Hess}_{\psi(p)} \mathcal{D}_{\psi(q)}^{M_{2}}\left(\psi_{*} \xi, \psi_{*} \zeta\right)=\psi_{*} \xi\left(\psi_{*} \zeta \mathcal{D}_{\psi(q)}^{M_{2}}\right)-\left(\nabla_{\psi_{*} \xi}^{M_{2}} \psi_{*} \zeta\right) \mathcal{D}_{\psi(q)}^{M_{2}}$$
hence
$$\begin{gathered}
\operatorname{Hess}_{\psi(p)} \mathcal{D}_{\psi(q)}^{M_{2}}\left(\psi_{*} \xi, \psi_{*} \zeta\right)-\operatorname{Hess}_{p} \mathcal{D}_{q}^{M_{1}}(\xi, \zeta)=\left(\nabla_{\psi_{*} \xi}^{M_{2}} \psi_{*} \zeta-\psi_{*} \nabla_{\xi}^{M_{1}} \zeta\right) \mathcal{D}_{\psi(q)}^{M_{2}} \\
=\operatorname{II}_{q}(\xi, \zeta) \mathcal{D}_{\psi(q)}^{M_{2}} .
\end{gathered}$$ \(\square\)

Proposition 2.3. Let $\left(\Omega, g^{\Omega}\right)$ be a HSSNCT, with $g^{\Omega}$ normalized in order to have holomorphic sectional curvature between $0 e-4$, then
\begin{itemize}
\item[-] the diastasis $\mathcal{D}^{\Omega}$ and the geodesic distance $\rho^{\Omega}$ are related by the following inequality
$$\mathcal{D}^{\Omega}(w, z) \geq 2 \log \cosh \left(\rho^{\Omega}(w, z)\right) ;$$
\item[-] if $\left(\Omega, g^{\Omega}\right)$ is of classical type, then
$$\mathcal{X}\left(g^{\Omega}\right)=\sup _{p, q \in \Omega}\left\|\operatorname{grad}_{p} \mathcal{D}_{q}^{\Omega}\right\|<\infty .$$
Moreover the eigenvalues of the hessian of the diastasis are bounded, more precisely for any $z, y \in \Omega$ and any unitary $\xi \in T_{z} \Omega$, we have
$$0<\operatorname{Hess}_{z} \mathcal{D}_{y}^{\Omega}(\xi, \xi)<4 .$$
\end{itemize}
Proof. We firstly consider the case of a HSSNCT of rank one, namely the complex hyperbolic space $\left(\mathbb{C} H^{n}, \widetilde{g}_{h}\right)$. Let $\mathbb{C} H^{n}=\left\{z \in \mathbb{C}^{n}:\|z\|^{2}=\left|z_{1}\right|^{2}+\cdots+\left|z_{n}\right|^{2}<1\right\}$ be the unitary disc endowed with the hyperbolic metric $\widetilde{g}_{h}$ of constant holomorphic sectional curvature -4. The associated Kähler form is $\widetilde{\omega}_{h}=-\frac{i}{2} \partial \bar{\partial} \log \left(1-\|z\|^{2}\right)$
and the diastasis is given by
$$\mathcal{D}^{h}(w, z)=-\log \left(\frac{\left(1-\|z\|^{2}\right)\left(1-\|w\|^{2}\right)}{\left|1-z w^{*}\right|^{2}}\right) .$$
Recalling the expression of geodesic distance,
$$\widetilde{\rho}_{h}(w, z)=\operatorname{arctanh}\left(\left|\frac{w-z}{1-z w^{*}}\right|\right)$$
we can conclude that the distance and the diastasis of the complex hyperbolic space are related by
$$\mathcal{D}^{h}(w, z)=2 \log \cosh \left(\widetilde{\rho}_{h}(w, z)\right) .$$

By the polydisc theorem (see e.g. [7]), for any couple of points $p, q \in \Omega$ there exists a totally geodesic polydisc $\left(P, g^{P}\right)$ of dimension $r=\operatorname{rank} \Omega$, holomorphically imbedded in $\Omega$ such that $p, q \in P$. By a $r$-dimensional polydisc $\left(P, g^{P}\right)$ we mean the following product of one dimensional complex hyperbolic spaces with holomorphic sectional curvature -4,
$$(P, g)=\left(\mathbb{C} H^{1}, \widetilde{g}_{h}\right) \times \cdots \times\left(\mathbb{C} H^{1}, \widetilde{g}_{h}\right),$$
where $P=\left\{\left(z_{1}, \ldots, z_{r}\right) \in \mathbb{C}^{r}:\left|z_{j}\right|<1, j=1, \ldots, r\right\}$. The diastasis is the sum of the diastasis of each factor:
$$\mathcal{D}^{P}(w, z)=-\sum_{j=1}^{r} \log \left(\frac{\left(1-\left|z_{j}\right|^{2}\right)\left(1-\left|w_{j}\right|^{2}\right)}{\left|1-z_{j} \bar{w}_{j}\right|^{2}}\right) .$$
By (16) we see that the geodesic distance of $P$ is given by
$$\rho^{P}(w, z)=\sqrt{\sum_{j=1}^{r} \widetilde{\rho}_{h}^{2}\left(w_{j}, z_{j}\right)}=\sqrt{\sum_{j=1}^{r} \operatorname{arctanh}^{2}\left(\left|\frac{w_{j}-z_{j}}{1-z_{j} \bar{w}_{j}}\right|\right)} .$$
Using (17) we obtain the following inequality
$$\begin{gathered}
\mathcal{D}^{P}(w, z)=\sum_{j=1}^{r} \mathcal{D}^{h}\left(w_{j}, z_{j}\right)=2 \sum_{j=1}^{r} \log \cosh \left(\widetilde{\rho}_{h}\left(w_{j}, z_{j}\right)\right) \\
\geq 2 \log \cosh \left(\rho^{P}(w, z)\right) .
\end{gathered}$$
Inequality (12) follows by combining the previous inequality, the polydisc theorem, Lemma 2.1 and the fact that a HSSNCT has globally defined diastasis (see for example [8]).

We first prove (13) and (14) for the first classical domain
$$\Omega_{1}=\Omega_{1}[m, m]=\left\{Z \in M_{m, m}: \operatorname{det}\left(I-Z Z^{*}\right)>0\right\}$$
endowed with its symmetric metric $g^{\Omega_{1}}$ of holomorphic sectional curvature between 0 and -4. The Kähler form associated to $g^{\Omega_{1}}$ is $\omega^{\Omega_{1}}=-\frac{i}{2} \partial \bar{\partial} \log \operatorname{det}\left(I-Z Z^{*}\right)$.

The diastasis centered in the origin is given by
$$\mathcal{D}_{0}^{\Omega_{1}}(Z)=-\log \operatorname{det}\left(I-Z Z^{*}\right) .$$
A straightforward computation show that
$$\begin{aligned}
d_{Z} \mathcal{D}_{0}^{\Omega_{1}} & =\sum_{h, k=1}^{m}\left(\operatorname{Tr}\left[\left(I-Z Z^{*}\right)^{-1} Z E_{k h}\right] d \bar{z}_{h k}\right. \\
& \left.+\operatorname{Tr}\left[\left(I-Z Z^{*}\right)^{-1} E_{h k} Z\right] d z_{h k}\right)
\end{aligned}$$
and
$$\begin{gathered}
\omega^{\Omega_{1}}=\frac{i}{2} \sum_{i, j, h, k=1}^{m} \operatorname{Tr}\left[\left(I-Z Z^{*}\right)^{-1} E_{i j} Z^{*}\left(I-Z Z^{*}\right)^{-1} Z E_{k h}\right. \\
\left.+\left(I-Z Z^{*}\right)^{-1} E_{i j} E_{k h}\right] d z_{i j} \wedge d \bar{z}_{h k}
\end{gathered}$$
where $z_{11}, z_{12}, \ldots, z_{m m}$ are the standard coordinates of $M_{m, m}$ denoting the entries of the matrix $Z$ and $E_{k h}$ is the matrix with all the entries zero but the $k h$-th equal to one.

Since the group of holomorphic isometries $\mathcal{G}=\operatorname{Isom}\left(\Omega_{1}, g^{\Omega_{1}}\right) \cap \operatorname{Aut}\left(\Omega_{1}\right)$ acts transitively on $\Omega_{1}$, by Lemma 2.2. we can study $\operatorname{grad} \mathcal{D}_{W}^{\Omega_{1}}$ and $\operatorname{Hess}_{Z} \mathcal{D}_{W}^{\Omega_{1}}$, assuming $W=0$. Moreover, given unitary matrices $U_{1}, U_{2} \in \mathrm{U}(m)$ the map $Z \mapsto$ $U_{1} Z U_{2}$ is a holomorphic isometry of $\left(\Omega_{1}, g^{\Omega_{1}}\right)$, that fixes the origin. Let $P^{\prime}$ be the totally geodesic Kähler embedded $m$-dimensional polydisc of equation $P^{\prime}=$ $\left\{Z \in \Omega_{1}: z_{i j}=0\right.$ if $\left.i \neq j\right\}$ (notice that $m$ is the rank of $\Omega_{1}$ ). Since $U_{1}, U_{2}$ can be choosed so that $V=U_{1} Z U_{2}$ is diagonal, by applying once again Lemma 2.2, we can assume $Z \in P^{\prime}$.

A straightforward computation shows that the gradient and the hessian of the diastasis restricted to $P^{\prime}$ are given respectively by:
$$\left.\operatorname{grad} \mathcal{D}_{0}^{\Omega_{1}}\right|_{P^{\prime}}=2 \sum_{j=1}^{m}\left(1-\left|z_{j j}\right|^{2}\right)\left(z_{j j} \frac{\partial}{\partial z_{j j}}+\bar{z}_{j j} \frac{\partial}{\partial \bar{z}_{j j}}\right)$$
and
$$\begin{aligned}
& \left.\operatorname{Hess}_{Z} \mathcal{D}_{0}^{\Omega_{1}}\right|_{P^{\prime}}=\sum_{j, k=1}^{m}\left(\frac{d z_{j k} \otimes d \bar{z}_{j k}+d \bar{z}_{j k} \otimes d z_{j k}}{\left(1-\left|z_{k k}\right|^{2}\right)\left(1-\left|z_{j j}\right|^{2}\right)}\right. \\
& \left.-\frac{\bar{z}_{j j} \bar{z}_{k k} d z_{j k} \otimes d z_{j k}+z_{j j} z_{k k} d \bar{z}_{j k} \otimes d \bar{z}_{j k}}{\left(1-\left|z_{j j}\right|^{2}\right)\left(1-\left|z_{k k}\right|^{2}\right)} \delta_{j k}\right)
\end{aligned}$$
By the previous argument we can suppose $Z \in P_{+}^{\prime}=\left\{Z \in P^{\prime} \mid z_{j j} \geq 0, j=\right.$ $1, \ldots, n\}$ and easily conclude that
$$\mathcal{X}\left(\widetilde{g}^{\Omega_{1}}\right)=\sup _{p, q \in \widetilde{Y}}\left\|\operatorname{grad}_{p} \mathcal{D}_{q}^{\Omega_{1}}\right\|<2 \sqrt{n} .$$

Consider the orthonormal basis of $T_{Z} \Omega_{1}$,
$$u_{j k}=\sqrt{\left(1-\left|z_{j j}\right|^{2}\right)\left(1-\left|z_{k k}\right|^{2}\right)}\left(\frac{\partial}{\partial z_{j k}}+\frac{\partial}{\partial \bar{z}_{j k}}\right)$$
and $u_{n+j n+k}=J u_{j k}, j, k=1, \ldots, n$ and notice that $\nabla d_{Z} \mathcal{D}_{0}^{\Omega_{1}}{ }_{\left.\right|_{P_{+}^{\prime}}}\left(u_{j k}, u_{l s}\right)$ is a diagonal matrix with eigenvalues $0<\lambda_{j k}<4$. Thus, we conclude that for $Z, W \in$ $\Omega_{1}$ and any unitary $\xi \in T_{Z} \Omega_{1}$
$$0<\nabla d_{Z} \mathcal{D}_{W}^{\Omega_{1}}(\xi, \xi)<4 .$$

We can address now the general case. Let $\left(\Omega, g^{\Omega}\right)$ be any classical HSSNCT. It is known that $\left(\Omega, g^{\Omega}\right)$ can be complex and totally geodesic embedded into $\Omega_{1}[m, m]$, for $m$ sufficiently large (this is obvious for the domains $\Omega_{1}, \Omega_{2}$ and $\Omega_{3}$, while for the domain $\Omega_{4}$, associated to the so called Spin-factor, the explicit embedding can be found at the bottom of p. 47 in [6]). Hence by Lemma 2.2 (26) and (27) we deduce the validity of (13) and (14). The proof of Proposition 2.3 is complete. □

Corollary 2.4. Let $\left(\mathbb{C} H^{n}, \widetilde{g}_{h}\right)$ be the complex hyperbolic space with associated diastasis $\mathcal{D}^{h}$ (see (15)). Denoted by $J$ the complex structure, the Hessian $\nabla d \mathcal{D}^{h}$ of the diastasis can be written
$$\begin{gathered}
\nabla d_{z} \mathcal{D}_{w}^{h}= \\
\left.=2 \widetilde{g}_{h}(z)-\frac{1}{2} d_{z} \mathcal{D}_{w}^{h} \otimes d_{z} \mathcal{D}_{w}^{h}+\frac{1}{2}\left(d_{z} \mathcal{D}_{w}^{h} \circ J_{z}\right) \otimes\left(d_{z} \mathcal{D}_{w}^{h} \circ J_{z}\right)\right),
\end{gathered}$$
for all $z, w \in \mathbb{C} H^{n}$.

Proof. Consider $\left(\mathbb{C} H^{n}, \widetilde{g}_{h}\right)$ realized as the holomorphic and totally geodesic submanifold of $\Omega_{1}[n, n]$ of equation $z_{j k}=0$ if $j>1$. Observe that the diastasis centered in the origin of $\left(\mathbb{C} H^{n}, \widetilde{g}_{h}\right)$ is the restriction of (21) to $\mathbb{C} H^{n}=\left\{Z \in \Omega_{1}[n, n]: z_{j k}=\right.$ $0, \forall j \neq 1\}$, i.e. $\mathcal{D}_{0}^{h}=-\log \operatorname{det}\left(1-\sum_{j=1}^{n}\left|z_{1 j}\right|^{2}\right)$.

Notice that the group of holomorphic isometries of $\left(\mathbb{C} H^{n}, \widetilde{g}_{h}\right)$ acts transitively on $\mathbb{C} H^{n}$ and that it contains $\mathrm{U}(n)$. Therefore, in order to prove (28), arguing as above we see that it is enough to assume $w=0$ and $z$ with $z_{12}=\cdots=z_{1 n}=0$. By (22), (23) and (25), we see that
$$\begin{aligned}
\nabla d_{z} \mathcal{D}_{0}^{h}= & \frac{\sum_{j, k=1}^{n}\left(d z_{j k} \otimes d \bar{z}_{j k}+d \bar{z}_{j k} \otimes d z_{j k}\right)-\bar{z}_{11}^{2} d z_{11} \otimes d z_{11}-z_{11}^{2} d \bar{z}_{11} \otimes d \bar{z}_{11}}{\left(1-\left|z_{11}\right|^{2}\right)^{2}} \\
& \left.=2 \widetilde{g}_{h}(z)-\frac{1}{2} d_{z} \mathcal{D}_{0}^{h} \otimes d_{z} \mathcal{D}_{0}^{h}+\frac{1}{2}\left(d_{z} \mathcal{D}_{0}^{h} \circ J_{z}\right) \otimes\left(d_{z} \mathcal{D}_{0}^{h} \circ J_{z}\right)\right) .
\end{aligned}$$ \(\square\)

\section*{3. The BARYCENTRE MAP $\widetilde{F}_{c}$}

Let $(Y, g)$ be a compact Kähler manifold with universal Kähler covering $(\widetilde{Y}, \widetilde{g})$ having globally defined diastasis. We define a positive finite measure $d \mu_{y}^{c}$ on $\widetilde{Y}$ by
$$d \mu_{y}^{c}(z)=e^{-c \mathcal{D}_{y}(z)} \nu_{\widetilde{g}}, \quad c>\frac{\operatorname{Ent}_{\mathrm{d}}(Y, g)}{\mathcal{X}(\widetilde{g})} .$$
Let $\left(X, g_{0}\right)$ be a compact complex hyperbolic manifold of the same dimension of $Y$, $f: Y \rightarrow X$ be a continuous map and let $\widetilde{f}: \widetilde{Y} \rightarrow \mathbb{C} H^{n}$ be its lift to the universal covers.

Definition 3.1. For any $c>\frac{\operatorname{Ent}_{\mathrm{d}}(Y, g)}{\mathcal{X}(\tilde{g})}$, we define the barycentre map $\widetilde{F}_{c}: \widetilde{Y} \rightarrow$ $\mathbb{C} H^{n}$, as the map that associates at $y \in \widetilde{Y}$ the point where the function $\mathcal{B}_{y}: \mathbb{C} H^{n} \rightarrow$ $\mathbb{R}^{+}$
$$x \mapsto \int_{\widetilde{Y}} \mathcal{D}^{h}(\widetilde{f}(z), x) d \mu_{y}^{c}(z)$$
attains its unique point of minimum.
Here the notion of barycentre used by G. Besson, G. Courtois and S. Gallot in [2] has been modified using in (30) the Calabi's diastasis function $\mathcal{D}^{h}$ instead of the distance $\widetilde{\rho}_{h}$. The following result assures us that the barycentre map $\widetilde{F}_{c}$ is indeed well defined.

Lemma 3.2. The function $\mathcal{B}_{y}: \mathbb{C} H^{n} \rightarrow \mathbb{R}^{+}$admits a unique point of minimum.
Proof. First we need to prove that $\mathcal{B}_{y}$ is well defined, namely that (30) is convergent. Since $X$ and $Y$ are compact, by standard Riemannian geometry we can prove that, for given $x \in X$ and $y \in Y$, there exist constants $C_{1}$ and $C_{2}$ such that $\widetilde{\rho}_{h}(x, \widetilde{f}(z)) \leq C_{1} \widetilde{\rho}(y, z)+C_{2}$. Therefore, for $\widetilde{\rho}(y, z) \gg 0$ there exists a positive constant $C_{3}$, such that:
$$\begin{gathered}
\mathcal{D}^{h}(x, \widetilde{f}(z))=2 \log \cosh \left(\widetilde{\rho}_{h}(x, \widetilde{f}(z))\right) \leq 2 \log \cosh \left(C_{1} \widetilde{\rho}(y, z)+C_{2}\right) \\
\leq C_{3} \widetilde{\rho}(y, z),
\end{gathered}$$
where in the first equality we use (17) and in the last inequality the fact that $\lim _{t \rightarrow+\infty} \frac{\log \cosh t}{t}=1$. By (4), we conclude that
$$\int_{\widetilde{Y}} \mathcal{D}^{h}(\widetilde{f}(z), x) d \mu_{y}^{c}(z)<\int_{\widetilde{Y}} C_{3} \widetilde{\rho}(y, z) d \mu_{y}^{c}(z)<\infty,$$
i.e. (30) is well defined.
We show now that the function $\mathcal{B}_{y}$ admits a point of minimum. Since $\left\|\operatorname{grad}_{z} \mathcal{D}^{h}\right\|=$ $2\|z\|<2$ for any $z \in \mathbb{C} H^{n}$, by the theorem of derivation under integral sign, we have
$$\operatorname{grad}_{x} \mathcal{B}_{y}=\int_{\widetilde{Y}} \operatorname{grad}_{x} \mathcal{D}_{\widetilde{f}(z)}^{h} d \mu_{y}^{c}(z),$$
in particular, we see that $\mathcal{B}_{y}$ and $\operatorname{grad}_{x} \mathcal{B}_{y}$ are continuous. Let $T$ be a bounded non empty open set of $\widetilde{Y}$, and define
$$K(x)=\min _{z \in T} \mathcal{D}^{h}(\tilde{f}(z), x),$$
so
$$\mathcal{B}_{y}(x)=\int_{\widetilde{Y}} \mathcal{D}_{\widetilde{f}(z)}^{h}(x) d \mu_{y}^{c}(z) \geq K(x) \int_{T} d \mu_{y}^{c}(z)$$
By (17) we see that $K(x) \rightarrow+\infty$ as $x \rightarrow \partial \mathbb{C} H^{n}$, that is $\mathcal{B}_{y}(x) \rightarrow+\infty$ as $x \rightarrow \partial \mathbb{C} H^{n}$. Therefore $\mathcal{B}_{y}$ attains its minimum in $\mathbb{C} H^{n}$.

It remains to prove that the point of minimum is unique. Since $\widetilde{Y}$ is a complete Riemannian manifold, it is enough to prove that $\mathcal{B}_{y}$ is a strictly convex function, that is, we have to prove that the hessian of $\mathcal{B}_{y}$ is positive definite. By (14) we know that $\left\|\nabla d_{z} \mathcal{D}_{w}^{h}\right\|<\infty$ for any $z, w \in \mathbb{C} H^{n}$, so by the theorem of derivation under integral sign, the hessian of $\mathcal{B}_{y}$ is continuous and given by
$$\nabla d_{z} \mathcal{B}_{y}=\int_{\widetilde{Y}} \nabla d_{z} \mathcal{D}_{\widetilde{f}(z)}^{h} d \mu_{y}^{c}(z)$$
By (14), we see that $\nabla d_{z} \mathcal{D}_{\tilde{f}(z)}^{h}$ and $\nabla d_{z} \mathcal{B}_{y}$ are positive definite. The proof is complete. \(\square\)

The main properties of the barycentre map $\widetilde{F}_{c}: \widetilde{Y} \rightarrow \mathbb{C} H^{n}$ are described by the following proposition.

Proposition 3.3. The barycentre map $\widetilde{F}_{c}: \widetilde{Y} \rightarrow \mathbb{C} H^{n}$ satisfies the following properties:
\begin{itemize}
\item[(1)] it is a $\mathcal{C}^{1}$ map, characterized by the equation
$$d_{\widetilde{F}_{c}(y)} \mathcal{B}_{y}=\int_{\widetilde{Y}} d_{\widetilde{F}_{c}(y)} \mathcal{D}_{\widetilde{f}(z)}^{h} d \mu_{y}^{c}(z)=0$$
\item[(2)] it is equivariant with respect to deck transformations and it descend to a $\mathcal{C}^{1}$ map
$$F_{c}: Y \rightarrow X$$
homotopic to $f: Y \rightarrow X$.
\end{itemize}

Proof. By Proposition 3.2 it follows that $\widetilde{F}_{c}(y)$ is characterized by the equation
$$d_{\widetilde{F}_{c}(y)} \mathcal{B}_{y}=\int_{\widetilde{Y}} d_{\widetilde{F}_{c}(y)} \mathcal{D}_{\widetilde{f}(z)}^{h} d \mu_{y}^{c}(z)=0$$
In other terms, given an orthonormal basis $e_{j}$, we define the function $\Phi: \mathbb{C} H^{n} \times \widetilde{Y} \rightarrow$ $\mathbb{R}^{2 n}$ by $\Phi(x, y)^{j}=d_{x} \mathcal{B}_{y}\left(e_{j}\right)$. Then we have $\Phi\left(\widetilde{F}_{c}(y), y\right)=0$. Since $\mathcal{X}\left(g_{0}\right)<\infty$ and $\mathcal{X}(g)<\infty$ then $\left\|d_{x} \mathcal{D}_{\tilde{f}(z)}^{h} d_{y} \mathcal{D}_{z}\right\|<\infty$ and by the theorem of derivation under
the integral sign, the differential of $\Phi$ with respect to $y$ is given by
$$d_{y} \Phi(x, y)=-c \int_{\widetilde{Y}} d_{x} \mathcal{D}_{\widetilde{f}(z)}^{h} d_{y} \mathcal{D}_{z} d \mu_{y}^{c}(z) \leq-c \mathcal{X}(g) d_{x} \mathcal{B}_{y} .$$
Arguing as in the proof of Lemma 3.2, we see that the Hessian of $\mathcal{D}_{\widetilde{f}(z)}^{h}(x)$ is bounded and positive definite and therefore the Jacobian matrix of $\Phi$ with respect to $x$ is continuous and positive definite at $\left(\widetilde{F}_{c}(y), y\right)$. Thus, we can apply the implicit function theorem and obtain the $\mathcal{C}^{1}$-regularity of the maps $F_{c}$. This concludes the proof of (1).

Consider now $\Gamma=\pi_{1}\left(Y, y_{0}\right)$ the group of deck transformations of the universal covering of $Y$. The morphism $f_{*}: \pi_{1}\left(Y, y_{0}\right) \rightarrow \pi_{1}\left(X, f\left(y_{0}\right)\right)$ induces a representation $r: \Gamma \rightarrow$ Isom $\left(\mathbb{C} H^{n}, \widetilde{g}_{0}\right) \cap \operatorname{Aut}\left(\mathbb{C} H^{n}\right)$ which satisfies $\widetilde{f} \circ \gamma=r(\gamma) \circ \widetilde{f}$ for every $\gamma \in \Gamma$. As $\gamma_{*} v_{\widetilde{g}}=v_{\widetilde{g}}$, and as $r(\gamma)$ is a holomorphic isometry of $\mathbb{C} H^{n}$, we have, for every $y \in \widetilde{Y}$ and every $x \in \widetilde{X}$ :
$$\begin{gathered}
\mathcal{B}_{\gamma y}(r(\gamma) x)=\int_{\widetilde{Y}} \mathcal{D}^{h}(\widetilde{f}(z), r(\gamma) x) e^{-c \mathcal{D}(\gamma y, z)} \nu_{\widetilde{g}} \\
=\int_{\widetilde{Y}} \mathcal{D}^{h}(\widetilde{f}(\gamma z), r(\gamma) x) e^{-c \mathcal{D}(\gamma y, \gamma z)} \nu_{\widetilde{g}} \\
=\int_{\widetilde{Y}} \mathcal{D}^{h}(r(\gamma) \widetilde{f}(z), r(\gamma) x) e^{-c \mathcal{D}(y, z)} \nu_{\widetilde{g}} \\
=\int_{\widetilde{Y}} \mathcal{D}^{h}(\widetilde{f}(z), x) d \mu_{y}^{c}(z)=\mathcal{B}_{y}(x)
\end{gathered}$$
As $\mathcal{B}_{y}$ attains its minimum at the unique point $\widetilde{F}(y)$, this equality implies that $\mathcal{B}_{\gamma y}$ attains its minimum at the unique point $r(\gamma) \widetilde{F}(y)$. That is $\widetilde{F}(\gamma y)=r(\gamma) \widetilde{F}(y)$. Therefore $\widetilde{F}_{c}$ is invariant with respect to deck transformations and it descends to a map
$$F_{c}: Y \rightarrow X .$$
In order to prove that the maps $F_{c}$ and $f$ are homotopic, consider the Dirac measure $\delta_{y}(z)$ on $\widetilde{Y}$. Let us define the positive finite measure $d \mu_{y}^{c, t}$ as follows
$$d \mu_{y}^{c, t}(z)=t d \mu_{y}^{c}(z)+(1-t) \delta_{y}(z)$$
and let $\widetilde{F}_{c, t}: \widetilde{Y} \rightarrow \mathbb{C} H^{n}$ be the map given by
$$\widetilde{F}_{c, t}(y)=\operatorname{Bar}\left(\widetilde{f}_{*} d \mu_{y}^{c, t}(z)\right),$$
i.e. $\widetilde{F}_{c, t}(y)$ is the unique point where the function $\mathcal{B}_{y, t}: \widetilde{X} \rightarrow \mathbb{R}^{+}$defined by
$$\begin{aligned}
\mathcal{B}_{y, t}(x) & =\int_{\widetilde{Y}} \mathcal{D}^{h}(\widetilde{f}(z), x) d \mu_{y}^{c, t}(z)= \\
& =t \int_{\widetilde{Y}} \mathcal{D}^{h}(\widetilde{f}(z), x) d \mu_{y}(z)+(1-t) \mathcal{D}^{h}(\widetilde{f}(y), x)
\end{aligned}$$
attains its minimum. Clearly $\widetilde{F}_{c, 1}=\widetilde{F}_{c}$. Let $\phi \in \operatorname{Isom}\left(\mathbb{C} H^{n}, \widetilde{g}_{0}\right) \cap \mathrm{Aut}\left(\mathbb{C} H^{n}\right)$ such that $\phi(x)=0$, then
$$\mathcal{D}^{h}(x, z)=\mathcal{D}^{h}(0, \phi(z))=-\log \left(1-|\phi(z)|^{2}\right)$$
therefore $\mathcal{D}^{h}(x, z) \geq 0$ and $\mathcal{D}^{h}(x, z)=0$ if and only if $x=z$, so the function $\mathcal{B}_{y, 0}$ attains its unique minimum for $x=\widetilde{f}(y)$, i.e. $\widetilde{F}_{c, 0}(y)=\widetilde{f}(y)$.

Arguing as before, we conclude that $\widetilde{F}_{c, t}(y)$ is a well defined $\mathcal{C}^{1}$ map, equivariant with respect to deck transformations. So $\widetilde{F}_{c, t}(y)$ descends to a homotopy $F_{c, t}(y)$ between $F_{c}$ and $f$. \(\square\)

\section*{4. The proof of Theorem 1 and Theorem 2.}

Let $f: Y \rightarrow X$ be the continuous function given in the hypothesis of Theorem 1 and let $\widetilde{F}_{c}: \widetilde{Y} \rightarrow X$ be the associated barycentre map, given by Definition 3.1.

In order to differentiate (31) under the integral sign, note that by (28) and $\mathcal{X}\left(\widetilde{g}_{h}\right)=2$, we get
$$\begin{gathered}
\max _{\|u\|=\|v\|=1}\left|\nabla\left(d_{\widetilde{F}_{c}(y)} \mathcal{D}_{\widetilde{f}(z)}^{h} e^{-c \mathcal{D}(y, z)}\right)(u, v)\right| \\
\leq \max _{\|u\|=\|v\|=1}\left(\left|\nabla d \mathcal{D}_{\widetilde{f}(z)}^{h}\left(d \widetilde{F}_{c}(u), v\right)\right|+\left|d \mathcal{D}^{h} \otimes d \mathcal{D}(u, v)\right|\right) e^{-c \mathcal{D}(y, z)} \\
\leq\left(6\left\|d \widetilde{F}_{c}\right\|+2 \mathcal{X}(g)\right) e^{-c \mathcal{D}(y, z)},
\end{gathered}$$
by Proposition 3.3 the map $\widetilde{F}_{c}$ descend to a map $F_{c}: Y \rightarrow X$, so, as $Y$ is compact, $\left\|d \widetilde{F}_{c}\right\|$ is bounded. Hence the norm of the derivative of the integrand in (31) is bounded by a constant function, which (by the hypothesis $c>\frac{\operatorname{Ent}_{\mathrm{d}}(Y, g)}{\mathcal{X}(\bar{g})}$ ) is integrable. Thus, bsy standard measure theory, we can derive (31) under the integral sign. For every $v \in T_{\widetilde{F}_{c}(y)} \mathbb{C} H^{n}$ and $u \in T_{y}(\widetilde{Y})$, we get
$$\begin{aligned}
& \int_{\widetilde{Y}} \nabla d_{\widetilde{F}_{c}(y)} \mathcal{D}_{\widetilde{f}(z)}^{h}\left(d_{y} \widetilde{F}_{c}(u), v\right) d \mu_{y}^{c}(z) \\
& =c \int_{\widetilde{Y}} d_{\widetilde{F}_{c}(y)} \mathcal{D}_{\widetilde{f}(z)}^{h}(v) d_{y} \mathcal{D}_{z}(u) d \mu_{y}^{c}(z)
\end{aligned}$$

Let us denote by $K, H$ and $H^{\prime}$ the symmetric endomorphisms of $T_{\widetilde{F}_{c}(y)} \mathbb{C} H^{n}$ and $T_{y} \widetilde{Y}$ defined by
$$\begin{gathered}
\widetilde{g}_{h}(K(v), w)=\frac{1}{\int_{\widetilde{Y}} d \mu_{y}^{c}(z)} \int_{\widetilde{Y}} \nabla d_{\widetilde{F}_{c}(y)} \mathcal{D}_{\widetilde{f}(z)}^{h}(v, w) d \mu_{y}^{c}(z), \\
\widetilde{g}_{h}(H(v), w)=\frac{1}{\int_{\widetilde{Y}} d \mu_{y}^{c}(z)} \int_{\widetilde{Y}} d_{\widetilde{F}_{c}(y)} \mathcal{D}_{\widetilde{f}(z)}^{h}(v) d_{\widetilde{F}_{c}(y)} \mathcal{D}_{\widetilde{f}(z)}^{h}(w) d \mu_{y}^{c}(z), \\
\widetilde{g}\left(H^{\prime}(u), t\right)=\frac{1}{\int_{\widetilde{Y}} d \mu_{y}^{c}(z)} \int_{\widetilde{Y}_{y}} d_{y} \mathcal{D}_{z}(u) d_{y} \mathcal{D}_{z}(t) d \mu_{y}^{c}(z),
\end{gathered}$$
where $v, w \in T_{F_{c}(y)} \mathbb{C} H^{n}$ and $u, t \in T_{y} \widetilde{Y}$.
By the Cauchy-Schwarz inequality and (34), we deduce
$$\left|\widetilde{g}_{h}\left(K \circ d_{y} \widetilde{F}_{c}(u), v\right)\right| \leq c \widetilde{g}_{h}(H(v), v)^{\frac{1}{2}} \widetilde{g}\left(H^{\prime}(u), u\right)^{\frac{1}{2}}$$

Lemma 4.1. With the previous notations we have
$$|\operatorname{det} K|\left|\operatorname{det}\left(d_{y} \widetilde{F}_{c}\right)\right| \leq\left(\frac{\mathcal{X}^{2}(g) c^{2}}{2 n}\right)^{n}(\operatorname{det} H)^{\frac{1}{2}}$$
and
$$\frac{(\operatorname{det} H)^{\frac{1}{2}}}{\operatorname{det} K}=\frac{(\operatorname{det} H)^{\frac{1}{2}}}{\operatorname{det}\left(2 I-\frac{1}{2} H-\frac{1}{2} J H J\right)}<\left(\frac{1}{2 n}\right)^{n} .$$
Proof. Let $\left\{v_{j}\right\}$ be an orthonormal basis of $T_{y} \mathbb{C} H^{n}$ which diagonalizes the symmetric endomorphism $H$. Now, if $d_{y} \widetilde{F}_{c}$ is not invertible, the inequality is trivial. Suppose that $d_{y} \widetilde{F}_{c}$ has maximal rank. Let $u_{j}^{\prime}=\left(K \circ d_{y} \widetilde{F}_{c}\right)^{-1}\left(v_{j}\right)$. By the Gram-Schmidt orthonormalization applied to $\left\{u_{j}^{\prime}\right\}$, with respect the positive bilinear form $\widetilde{g}\left(H^{\prime}(\cdot), \cdot\right)$, we get an orthogonal basis $\left\{u_{j}\right\}$ such that $\widetilde{g}\left(u_{j}, u_{j}\right)^{-\frac{1}{2}}=\lambda_{j}$, $j=1, \ldots, 2 n$ are the eigenvalues of $H^{\prime}$. Then
$$|\operatorname{det} K|\left|\operatorname{det}\left(d_{y} \widetilde{F}_{c}\right)\right|=\prod_{j=1}^{2 n}\left|\widetilde{g}_{h}\left(K \circ d_{y} \widetilde{F}_{c}\left(u_{j}\right), v_{j}\right)\right|\left(\operatorname{det} H^{\prime}\right)^{\frac{1}{2}},$$
hence, by (35)
$$\begin{gathered}
|\operatorname{det} K|\left|\operatorname{det}\left(d_{y} \widetilde{F}_{c}\right)\right| \leq c^{2 n}(\operatorname{det} H)^{\frac{1}{2}}\left(\operatorname{det} H^{\prime}\right)^{\frac{1}{2}} \\
\leq c^{2 n}(\operatorname{det} H)^{\frac{1}{2}}\left(\frac{1}{2 n} \operatorname{tr} H^{\prime}\right)^{n} \\
=\left(\frac{\mathcal{X}^{2}(g) c^{2}}{2 n}\right)^{n}(\operatorname{det} H)^{\frac{1}{2}},
\end{gathered}$$
where we use that the eigenvalues of $H^{\prime}$ are positive and that for any orthonormal basis $\left\{e_{1}, \ldots, e_{2 n}\right\}$ of $T_{y} \widetilde{Y}$
$$\sum_{i=1}^{2 n} \widetilde{g}\left(H^{\prime}\left(e_{i}\right), e_{i}\right)=\frac{1}{\int_{\widetilde{Y}} d \mu_{y}^{c}(z)} \int_{\widetilde{Y}}\left(\sum_{i=1}^{2 n}\left(d_{y} \mathcal{D}_{z}\left(e_{i}\right)\right)^{2}\right) d \mu_{y}^{c}(z) \leq \mathcal{X}^{2}(g) .$$
So (36) is proved. By (28) we see that $\frac{(\operatorname{det} H)^{\frac{1}{2}}}{\operatorname{det} K}=\frac{(\operatorname{det} H)^{\frac{1}{2}}}{\operatorname{det}\left(2 I-\frac{1}{2} H-\frac{1}{2} J H J\right)}$. Consider the function $H \mapsto \frac{(\operatorname{det} H)^{\frac{1}{2}}}{\operatorname{det}\left(2 I-\frac{1}{2} H-\frac{1}{2} J H J\right)}$ defined over the group of symmetric matrices non negatively defined and with trace $\leq 4$ and dimension $2 n \times 2 n$ with $n \geq 2$. By [2] Appendix B, attains its maximum at $H=\frac{2}{n} I$. Hence $\frac{(\operatorname{det} H)^{\frac{1}{2}}}{\operatorname{det} K}<\left(\frac{1}{2 n}\right)^{n}$. \(\square\)

In order to prove Theorem 1 notice that the quantity $\operatorname{Ent}_{\mathrm{d}}{ }^{2 n}(Y, g) \operatorname{Vol}(Y, g)$ is invariant by homotheties, hence it is not restrictive assume from the very beginning
that $\operatorname{Ent}_{\mathrm{d}}(Y, g)=\operatorname{Ent}_{\mathrm{d}}\left(X, g_{0}\right)=\operatorname{Ent}_{\mathrm{d}}\left(X, g_{h}\right)=2 n$. The first part of Theorem 1 will immediately follow by Theorem 3 below. The second part of Theorem 1 (the $\varepsilon=0$ case), is proved in the last part of this section.

Theorem 3. Let $(Y, g)$ and $\left(X, g_{h}\right)$ be as in Theorem 1. Assume that $\operatorname{Ent}_{\mathrm{d}}(Y, g)=$ $\operatorname{Ent}_{\mathrm{d}}\left(X, g_{h}\right)$ and that
$$\operatorname{Vol}(Y, g)<(1+\varepsilon)|\operatorname{deg}(f)| \operatorname{Vol}\left(X, g_{h}\right) .$$
If $\varepsilon>0$ is small enough and $c$ is such that $\left(\left(\frac{\mathcal{X}(g) c}{2 n}\right)^{2 n}-1\right)<\frac{\varepsilon}{(1+\varepsilon)}$, then the map $F_{c}$ is a $\mathcal{C}^{1}$ covering map such that
$$A^{\prime}(\varepsilon) \leq \frac{\left\|d_{y} F_{c}(u)\right\|}{\|u\|} \leq A^{\prime \prime}(\varepsilon) \quad \forall y \in Y, \forall u \in T_{y} Y$$
where $A^{\prime}(\varepsilon), A^{\prime \prime}(\varepsilon) \rightarrow 1$ as $\varepsilon \rightarrow 0$.

In order to prove the theorem, we need of the following five lemmata (Lemma 4.2-4.6).

Lemma 4.2. Let $Y_{\varepsilon}=\left\{y \in Y:\left|\operatorname{Jac} F_{c}(y)\right|<(1-\sqrt{\varepsilon})(1+\delta)\right\}$ where $\delta>0$ is defined by
$$\delta=\left(\frac{\mathcal{X}(g) c}{2 n}\right)^{2 n}-1 .$$
Then, for $\delta<\frac{\varepsilon}{(1+\varepsilon)}$, we have
$$\operatorname{Vol}\left(Y_{\varepsilon}\right)<2 \sqrt{\varepsilon} \operatorname{Vol}(Y) .$$

Proof. By (36) and (37) we know that $\left|\mathrm{Jac} F_{c}\right|<1+\delta$, by the definition of $Y_{\varepsilon}$ we get
$$(1+\delta) \operatorname{Vol}\left(Y \backslash Y_{\varepsilon}\right)+(1-\sqrt{\varepsilon})(1+\delta) \operatorname{Vol}\left(Y_{\varepsilon}\right) \geq \int_{Y}\left|\operatorname{Jac} F_{c}\right| \nu_{g} .$$
Using the hypothesi (39) we obtain
$$\int_{Y}\left|\operatorname{Jac} F_{c}\right| \nu_{g} \geq|\operatorname{deg}(f)| \operatorname{Vol}(X)>\frac{1}{1+\varepsilon} \operatorname{Vol}(Y)>\frac{1+\delta}{1+2 \varepsilon} \operatorname{Vol}(Y),$$
Where the last inequality follows by the assumption $\delta<\frac{\varepsilon}{(1+\varepsilon)}$. Thus
$$\operatorname{Vol}\left(Y \backslash Y_{\varepsilon}\right)+(1-\sqrt{\varepsilon}) \operatorname{Vol}\left(Y_{\varepsilon}\right)>\frac{1}{1+2 \varepsilon} \operatorname{Vol}(Y),$$
and so
$$\operatorname{Vol}\left(Y_{\varepsilon}\right)<\frac{2 \sqrt{\varepsilon}}{1+2 \varepsilon} \operatorname{Vol}(Y)<2 \sqrt{\varepsilon} \operatorname{Vol}(Y) .$$
As wished. \(\square\)

Let us denote $\widetilde{Y}_{\varepsilon}=\pi^{-1}\left(Y_{\varepsilon}\right)$. By the definition of $Y_{\varepsilon}$ and (38), we get
$$(1-\sqrt{\varepsilon})(1+\delta) \leq\left|\operatorname{Jac} \widetilde{F}_{c}(y)\right| \leq \frac{c^{2 n}(\operatorname{det} H)^{\frac{1}{2}}\left(\operatorname{det} H^{\prime}\right)^{\frac{1}{2}}}{|\operatorname{det} K|}, \quad \forall y \in \widetilde{Y} \backslash \widetilde{Y}_{\varepsilon}$$
hence, by (37) and (41), we deduce
$$\left(\operatorname{det} H^{\prime}\right) \geq\left(\frac{(1-\sqrt{\varepsilon})(1+\delta)}{c^{2 n}} \frac{|\operatorname{det} K|}{(\operatorname{det} H)^{\frac{1}{2}}}\right)^{2} \geq(1-\sqrt{\varepsilon})^{2}\left(\frac{\mathcal{X}^{2}(g)}{2 n}\right)^{2 n} .$$
Since $\operatorname{det} H^{\prime} \leq\left(\frac{\operatorname{tr} H^{\prime}}{2 n}\right)^{2 n} \leq\left(\frac{\mathcal{X}^{2}(g)}{2 n}\right)^{2 n}$, we get
$$(1-\sqrt{\varepsilon})^{2}\left(\frac{\mathcal{X}^{2}(g)}{2 n}\right)^{2 n} \leq \operatorname{det} H^{\prime} \leq\left(\frac{\mathcal{X}^{2}(g)}{2 n}\right)^{2 n}$$
As the maximum of $H^{\prime} \mapsto \operatorname{det} H^{\prime}$ is obtained at $H^{\prime}=\frac{\mathcal{X}^{2}(g)}{2 n} I$ by a principle of stability of the maximum (see 4 pag. 157), there exist a positive constant $B^{\prime}(n)$ such that, for $\varepsilon<\frac{1}{\left(2 B^{\prime}(n)\right)^{4}}$
$$\left\|H^{\prime}-\frac{\mathcal{X}^{2}(g)}{2 n} I\right\| \leq B^{\prime}(n) \varepsilon^{\frac{1}{4}}, \quad \forall y \in \widetilde{Y} \backslash \widetilde{Y}_{\varepsilon} .$$
On the other hand by (42) we obtain
$$\frac{\operatorname{det} H^{\frac{1}{2}}}{\operatorname{det} K} \geq \frac{(1-\sqrt{\varepsilon})(1+\delta)}{c^{2 n}\left(\operatorname{det} H^{\prime}\right)^{\frac{1}{2}}} \geq(1-\sqrt{\varepsilon})\left(\frac{1}{2 n}\right)^{n},$$
Where the second inequality follows by (43). By (37) we get
$$(1-\sqrt{\varepsilon})\left(\frac{1}{2 n}\right)^{n} \leq \frac{(\operatorname{det} H)^{\frac{1}{2}}}{\operatorname{det}\left(2 I-\frac{1}{2} H-\frac{1}{2} J H J\right)} \leq\left(\frac{1}{2 n}\right)^{n} .$$
As we see before the maximum of $H \mapsto \frac{(\operatorname{det} H)^{\frac{1}{2}}}{\operatorname{det}\left(2 I-\frac{1}{2} H-\frac{1}{2} J H J\right)}$ is obtained for $H=\frac{2}{n} I$, so by a principle of stability of the maximum (see [2]), there exist a positive constant $B^{\prime \prime}(n)$ such that, for $\varepsilon<\frac{1}{\left(2 B^{\prime \prime}(n)\right)^{4}}$, we have
$$\left\|H-\frac{2}{n} I\right\| \leq B^{\prime \prime}(n) \varepsilon^{\frac{1}{4}}, \quad \forall y \in \widetilde{Y} \backslash \widetilde{Y}_{\varepsilon} .$$
From now on, we benote $B(n)$ the maximum between $B^{\prime \prime}(n)$ and $B^{\prime}(n)$.

Lemma 4.3. If $\varepsilon<\frac{1}{(4 B(n))^{4}}$ and $c$ is such that $\delta=\left(\frac{\mathcal{X}(g) c}{2 n}\right)^{2 n}-1<\frac{\varepsilon}{(1+\varepsilon)}$ then, $\forall y \in \widetilde{Y} \backslash \widetilde{Y}_{\varepsilon}$, we have
$$\left\|d_{y} \widetilde{F}_{c}(u)\right\| \leq \frac{c\left(B(n) \varepsilon^{\frac{1}{4}}+\frac{2}{n}\right)^{\frac{1}{2}}\left(B(n) \varepsilon^{\frac{1}{4}}+\frac{\mathcal{X}^{2}(g)}{2 n}\right)^{\frac{1}{2}}\|u\|}{\left(2-B(n) \varepsilon^{\frac{1}{4}}\right)}$$
and
$$\left\|d_{y} \widetilde{F}_{c}(u)\right\| \geq\left(\frac{((1+\delta)(1-\sqrt{\varepsilon}))^{\frac{2 n}{2 n-1}}\left(2-B(n) \varepsilon^{\frac{1}{4}}\right)}{c\left(B(n) \varepsilon^{\frac{1}{4}}+\frac{2}{n}\right)^{\frac{1}{2}}\left(B(n) \varepsilon^{\frac{1}{4}}+\frac{\mathcal{X}^{2}(g)}{2 n}\right)^{\frac{1}{2}}}\right)^{2 n-1}\|u\|$$

Proof. By (45) we have
$$\|K-2 I\|=\left\|\frac{1}{2} H-\frac{1}{2} J^{-1} H J\right\| \leq\left\|\frac{H}{2}-\frac{I}{n}\right\|+\left\|J^{-1}\left(\frac{I}{n}-\frac{H}{2}\right) J\right\| \leq B(n) \varepsilon^{\frac{1}{4}}$$
Note that
$$\begin{gathered}
\widetilde{g}_{h}(2 v, w)-\widetilde{g}_{h}(K v, w) \leq\left|\widetilde{g}_{h}(K v, w)-\widetilde{g}_{h}(2 v, w)\right| \leq \\
\leq\|K-2 I\|\|v\|\|w\| \leq B(n) \varepsilon^{\frac{1}{4}}\|v\|\|w\|
\end{gathered}$$
and so
$$\widetilde{g}_{h}(K v, w) \geq \widetilde{g}_{h}(2 v, w)-B(n) \varepsilon^{\frac{1}{4}}\|v\|\|w\| .$$
Setting $v=d_{y} \widetilde{F}_{c}(u)$ and $w=\frac{d_{y} \widetilde{F}_{c}(u)}{\left\|d_{y} \widetilde{F}_{c}(u)\right\|}$ we obtain
$$\widetilde{g}_{h}\left(K \circ d_{y} \widetilde{F}_{c}(u), \frac{d_{y} \widetilde{F}_{c}(u)}{\left\|d_{y} \widetilde{F}_{c}(u)\right\|}\right) \geq\left\|d_{y} \widetilde{F}_{c}(u)\right\|\left(2-B(n) \varepsilon^{\frac{1}{4}}\right) .$$
By (45), we see that
$$\widetilde{g}_{h}(H(u), u)-\widetilde{g}_{h}\left(\frac{2}{n} u, u\right) \leq\left\|H-\frac{2}{n} I\right\|\|u\|^{2} \leq B(n) \varepsilon^{\frac{1}{4}}\|u\|^{2} .$$
therefore
$$\widetilde{g}_{h}(H(u), u) \leq\left(B(n) \varepsilon^{\frac{1}{4}}+\frac{2}{n}\right)\|u\|^{2} .$$
On the other hand, by (44), we get
$$\begin{aligned}
& \widetilde{g}_{h}\left(H^{\prime}(w), w\right)-\widetilde{g}_{h}\left(\frac{\mathcal{X}^{2}(g)}{2 n} w, w\right) \leq\left\|H-\frac{\mathcal{X}^{2}(g)}{2 n} I\right\|\|w\|^{2} \\
& \quad \leq B(n) \varepsilon^{\frac{1}{4}}\|w\|^{2} .
\end{aligned}$$
and so
$$\widetilde{g}_{h}\left(H^{\prime}(w), w\right) \leq\left(B(n) \varepsilon^{\frac{1}{4}}+\frac{\mathcal{X}^{2}(g)}{2 n}\right)\|w\|^{2} .$$
Substituting (49), (50) and (51) in (35) we obtain
$$\left\|d_{y} \widetilde{F}_{c}(u)\right\| \leq \frac{c\left(B(n) \varepsilon^{\frac{1}{4}}+\frac{2}{n}\right)^{\frac{1}{2}}\left(B(n) \varepsilon^{\frac{1}{4}}+\frac{\mathcal{X}^{2}(g)}{2 n}\right)^{\frac{1}{2}}\|u\|}{\left(2-B(n) \varepsilon^{\frac{1}{4}}\right)}$$

We proved equation (46). Let $0<\left|\lambda_{1}\right|^{2} \leq \cdots \leq\left|\lambda_{2 n}\right|^{2}$ the eigenvalues of the symmetric endomorphism defined by $\left(d_{y} \widetilde{F}_{c}\right)^{t} d_{y} \widetilde{F}_{c}$. So
$$0<\left|\lambda_{1}\right| \leq \cdots \leq\left|\lambda_{2 n}\right| \leq \frac{c\left(B(n) \varepsilon^{\frac{1}{4}}+\frac{2}{n}\right)^{\frac{1}{2}}\left(B(n) \varepsilon^{\frac{1}{4}}+\frac{\mathcal{X}^{2}(g)}{2 n}\right)^{\frac{1}{2}}}{\left(2-B(n) \varepsilon^{\frac{1}{4}}\right)}$$
moreover, by the definition of $Y_{\varepsilon}$ follow that for every $y \in \widetilde{Y} \backslash \widetilde{Y}_{\varepsilon}$ we have, $\prod_{j=1}^{2 n}\left|\lambda_{j}\right| \geq$ $((1+\delta)(1-\sqrt{\varepsilon}))^{2 n}$, therefore
$$\left|\lambda_{1}\right| \geq \frac{\prod_{j=1}^{2 n}\left|\lambda_{j}\right|}{\left|\lambda_{2 n}\right|^{2 n-1}} \geq\left(\frac{((1+\delta)(1-\sqrt{\varepsilon}))^{\frac{2 n}{2 n-1}}\left(2-B(n) \varepsilon^{\frac{1}{4}}\right)}{c\left(B(n) \varepsilon^{\frac{1}{4}}+\frac{2}{n}\right)^{\frac{1}{2}}\left(B(n) \varepsilon^{\frac{1}{4}}+\frac{\mathcal{X}^{2}(g)}{2 n}\right)^{\frac{1}{2}}}\right)^{2 n-1}$$
we conclude that
$$\left\|d_{y} \widetilde{F}_{c}(u)\right\| \geq\left(\frac{((1+\delta)(1-\sqrt{\varepsilon}))^{\frac{2 n}{2 n-1}}\left(2-B(n) \varepsilon^{\frac{1}{4}}\right)}{c\left(B(n) \varepsilon^{\frac{1}{4}}+\frac{2}{n}\right)^{\frac{1}{2}}\left(B(n) \varepsilon^{\frac{1}{4}}+\frac{\mathcal{X}^{2}(g)}{2 n}\right)^{\frac{1}{2}}}\right)^{2 n-1}\|u\|,$$
we just proved (47). The proof is complete. \(\square\)

For every $y \in \widetilde{Y}, u \in T_{y} \widetilde{Y}$ and $v \in T_{\widetilde{F}_{c}(y)} \widetilde{X}$ we define
$$k_{y}^{\prime}(u, v)=\frac{1}{\int_{\widetilde{Y}} d \mu_{y}(z)} \int_{\widetilde{Y}} d_{\widetilde{F}_{c}(y)} \mathcal{D}_{\widetilde{f}(z)}^{h}(v) d_{y} \mathcal{D}_{z}(u) d \mu_{y}(z)$$

Lemma 4.4. There exist a universal constant $C$ such that
$$\left\|\nabla_{w} k^{\prime}(u, v)\right\| \leq C\|u\|\|v\|\left(\|w\|+\left\|d \widetilde{F}_{c}(w)\right\|\right) .$$
Proof. Assume for the moment that the following derivations under the integral sign are allowed, for every $w \in T_{y} Y$ we have
$$\begin{gathered}
\nabla_{w} k^{\prime}(u, v) \int_{\widetilde{Y}} d \mu_{y}^{c}(z) \\
=\int_{\widetilde{Y}} \nabla d_{\widetilde{F}_{c}(y)} \mathcal{D}_{\widetilde{f}(z)}^{h}\left(d_{y} \widetilde{F}_{c}(w), v\right) d_{y} \mathcal{D}_{z}(u) d \mu_{y}^{c}(z) \\
+\int_{\widetilde{Y}} d_{\widetilde{F}_{c}(y)} \mathcal{D}_{\widetilde{f}(z)}^{h}(v) \nabla d_{y} \mathcal{D}_{z}(w, u) d \mu_{y}^{c}(z) \\
-c \int_{\widetilde{Y}} d_{\widetilde{F}_{c}(y)} \mathcal{D}_{\widetilde{f}(z)}^{h}(v) d_{y} \mathcal{D}_{z}(u) d_{y} \mathcal{D}_{z}(w) d \mu_{y}^{c}(z) \\
+c k_{y}^{\prime}(u, v) \int_{\widetilde{Y}} d_{y} \mathcal{D}_{z}(w) d \mu_{y}^{c}(z)
\end{gathered}$$
Consider the second term in the right side of the previous equality. By condition (5) the absolute values of the eigenvalues of the Hess $\mathcal{D}_{p}$ are bounded by a positive
constant $\lambda_{0}$, we have
$$\int_{\widetilde{Y}} d_{\widetilde{F}_{c}(y)} \mathcal{D}_{\widetilde{f}(z)}^{h}(v) \nabla d_{y} \mathcal{D}_{z}(w, u) d \mu_{y}^{c}(z) \leq \lambda_{0} \mathcal{X}(g)\|v\|\|w\|\|u\| \int_{\widetilde{Y}} d \mu_{y}^{c} .$$
We can repeat a similar argument to any term of (54) and conclude that there exists constant $C>0$ such that (53) is verified. Analogously we can see that the integrands of the integrals in (54) and (52) are bounded, so that the previous derivations under the integral sign are well defined. \(\square\)

Lemma 4.5. For every $y \in \widetilde{Y} \backslash \widetilde{Y}_{\varepsilon}$, with $\varepsilon<\frac{1}{(2 B(n))^{4}}$ and $c$ such that $\delta=$ $\left(\frac{\mathcal{X}(g) c}{2 n}\right)^{2 n}-1<\frac{\varepsilon}{(1+\varepsilon)}$, we have
$$\begin{gathered}
\left|k^{\prime}(u, v)-\frac{2}{c} \widetilde{g}_{h}\left(d_{y} \widetilde{F}_{c}(u), v\right)\right| \leq \\
\leq B(n) \varepsilon^{\frac{1}{4}} \frac{\left(B(n) \varepsilon^{\frac{1}{4}}+\frac{2}{n}\right)^{\frac{1}{2}}\left(B(n) \varepsilon^{\frac{1}{4}}+\frac{\mathcal{X}^{2}(g)}{2 n}\right)^{\frac{1}{2}}\|u\|\|v\|}{\left(2-B(n) \varepsilon^{\frac{1}{4}}\right)}
\end{gathered}$$
for every $u \in T_{y} \widetilde{Y}, v \in T_{\widetilde{F}_{c}(y)} \mathbb{C} H^{n}$.
Proof. By the definitions of $k^{\prime}, K$ and equality (34), we have
$$k^{\prime}(u, v)=\frac{1}{c} \widetilde{g}_{h}\left(K \circ d_{y} \widetilde{F}_{c}(u), v\right)$$
hence
$$\begin{gathered}
\left|k^{\prime}(u, v)-\frac{2}{c} \widetilde{g}_{h}\left(d_{y} \widetilde{F}_{c}(u), v\right)\right|=\frac{1}{c}\left|\widetilde{g}_{h}\left((K-2 I) d_{y} \widetilde{F}_{c}(u), v\right)\right| \\
\leq \frac{1}{c}\|K-2 I\|\left\|d_{y} \widetilde{F}_{c}(u)\right\|\|v\| \\
\leq B(n) \varepsilon^{\frac{1}{4}} \frac{\left(B(n) \varepsilon^{\frac{1}{4}}+\frac{2}{n}\right)^{\frac{1}{2}}\left(B(n) \varepsilon^{\frac{1}{4}}+\frac{\mathcal{X}^{2}(g)}{2 n}\right)^{\frac{1}{2}}\|u\|\|v\|}{\left(2-B(n) \varepsilon^{\frac{1}{4}}\right)},
\end{gathered}$$
where in the last inequality we used (46) and (48). \(\square\)

Lemma 4.6. If $\varepsilon<\frac{1}{(4 B(n))^{4}}$ and $c$ is such that $\delta=\left(\frac{\mathcal{X}(g) c}{2 n}\right)^{2 n}-1<\frac{\varepsilon}{(1+\varepsilon)}$, then for every $y \in Y$
$$(1+\delta)^{2 n} \xi(\varepsilon)^{1-2 n} \leq \frac{\left\|d_{y} \widetilde{F}_{c}(u)\right\|}{\|u\|} \leq \xi(\varepsilon),$$
where
$$\xi(\varepsilon)=\frac{c\left(B(n) \varepsilon^{\frac{1}{4}}+\frac{2}{n}\right)^{\frac{1}{2}}\left(B(n) \varepsilon^{\frac{1}{4}}+\frac{\mathcal{X}^{2}(g)}{2 n}\right)^{\frac{1}{2}}}{\left(2-B(n) \varepsilon^{\frac{1}{4}}\right)}$$
Proof. Suppose $\varepsilon<\frac{1}{(4 B(n))^{4}}$. Let $H(y, r)=\operatorname{Vol}(Y, g)^{-1} \int_{B(y, r) \subset Y} \nu_{g}$, due to the compactness of $Y$, it is a uniformly continuous map, so it is well defined the continuous function $h(r)=\min _{y} H(y, r)$. Since $h(r)$ is strictly increasing, there exists
an increasing function $\varepsilon \rightarrow r(\varepsilon)$ such that $h(r(\varepsilon))=2 \sqrt{\varepsilon}$. By Lemma 4.2 we see that
$$B(y, r(\varepsilon)) \not \subset Y_{\varepsilon}$$
for any $y$. Therefore, denoted $\widetilde{B}(y, r(\varepsilon))=\pi^{-1}(B(y, r(\varepsilon)))$, we have
$$\widetilde{Y} \backslash \widetilde{Y}_{\varepsilon} \cap \widetilde{B}(y, r(\varepsilon)) \neq \emptyset \quad \forall y \in \widetilde{Y}_{\varepsilon} .$$

By (58) for every $y^{\prime \prime} \in \widetilde{Y}$ there exist $y \in \widetilde{Y} \backslash \widetilde{Y}_{\varepsilon}$ such that the distance $d\left(y, y^{\prime \prime}\right)=$ $r \leq r(\varepsilon)$. Let $\gamma$ be a minimizing geodesic with $\gamma(0)=y$ et $\gamma(r)=y^{\prime \prime}$. Set $\varepsilon_{0}=\frac{1}{(4 B(n))^{4}}$. We define $t_{0} \in[0, r]$ the instant when $\gamma$ intersect $\widetilde{Y}_{\varepsilon_{0}}$ for the first time, if $\gamma$ does not intersect $\widetilde{Y}_{\varepsilon_{0}}$ we set $t_{0}=r$. So $\gamma\left(\left[0, t_{0}\right]\right) \subset \widetilde{Y} \backslash \widetilde{Y}_{\varepsilon_{0}}$. Define $y^{\prime}=\gamma\left(t_{0}\right)$, let $u \in T_{y^{\prime}} \widetilde{Y}$ and $v \in T_{F_{c}\left(y^{\prime}\right)} \mathbb{C} H^{n}$, we define $U$ and $V$ the parallel field long $\gamma$ and $F(\gamma)$ such that $U\left(t_{0}\right)=u$ and $V\left(t_{0}\right)=v$. By Lemma 4.4
$$\left|k_{y^{\prime}}^{\prime}(u, v)-k_{y}^{\prime}(U(0), V(0))\right| \leq C d\left(y, y^{\prime}\right)\left(1+\sup _{t}\|d \widetilde{F}(\dot{\gamma}(t))\|\right)\|u\|\|v\| .$$
Therefore by (46), for any $y \in \widetilde{Y} \backslash \widetilde{Y}_{\varepsilon}$ with $0<\varepsilon \leq \varepsilon_{0}$ we have
$$\begin{gathered}
\left|k_{y^{\prime}}^{\prime}(u, v)-k_{y}^{\prime}(U(0), V(0))\right| \leq \\
C d\left(y, y^{\prime}\right)\left(1+\frac{c\left(\frac{1}{4}+\frac{2}{n}\right)^{\frac{1}{2}}\left(\frac{1}{4}+\frac{\mathcal{X}^{2}(g)}{2 n}\right)^{\frac{1}{2}}}{\left(2-\frac{1}{4}\right)}\right)\|u\|\|v\| \leq \\
C r(\varepsilon)\left(1+\frac{c}{7 n}\left(n+2 \mathcal{X}^{2}(g)\right)^{\frac{1}{2}}(n+8)^{\frac{1}{2}}\right)\|u\|\|v\|,
\end{gathered}$$
hence, set $D(\varepsilon):=C r(\varepsilon)\left(1+\frac{c}{7 n}\left(n+2 \mathcal{X}^{2}(g)\right)^{\frac{1}{2}}(n+8)^{\frac{1}{2}}\right)$, we get:
$$k_{y^{\prime}}^{\prime}(u, v) \geq k_{y}^{\prime}(U(0), V(0))-D(\varepsilon)\|u\|\|v\| .$$
Since $V(0) \mapsto V\left(t_{0}\right)$ is an isometry between $T_{\widetilde{F}_{c}(y)} \mathbb{C} H^{n}$ and $T_{\widetilde{F}_{c}\left(y^{\prime}\right)} \mathbb{C} H^{n}$, and $\left|\operatorname{Jac} F_{c}\right|(\gamma(t)) \neq 0$, there exists $v \in T_{\widetilde{F}_{c}\left(y^{\prime}\right)} \mathbb{C} H^{n}$, with $\|v\|=1$, such that $V(0)=$ $v=\frac{d_{y^{\prime}} \widetilde{F}_{c}(U(0))}{\left\|d_{y^{\prime}} \widetilde{F}_{c}(U(0))\right\|}$. Let $K_{y}^{\prime}: T_{y} \widetilde{Y} \rightarrow T_{\widetilde{F}_{c}(y)} \mathbb{C} H^{n}$ be the linear application defined by
$$\widetilde{g}_{h}\left(K_{y}^{\prime}(u), w\right)=k_{y}^{\prime}(u, w) .$$
By (59), we have
$$\left\|K_{y^{\prime}}^{\prime}(u)\right\| \geq \widetilde{g}_{h}\left(K_{y^{\prime}}^{\prime}(u), v\right)=k_{y^{\prime}}^{\prime}(u, v) \geq k_{y}^{\prime}\left(U(0), \frac{d \widetilde{F}_{c}(U(0))}{\left\|d \widetilde{F}_{c}(U(0))\right\|}\right)-D(\varepsilon)\|u\| .$$
By (55) and (57) we get
$$\left\|K_{y^{\prime}}^{\prime}(u)\right\| \geq \frac{2}{c} \widetilde{g}_{h}\left(d \widetilde{F}_{c}\left((U(0)), \frac{d \widetilde{F}_{c}(U(0))}{\left\|d \widetilde{F}_{c}(U(0))\right\|}\right)-B(n) \xi(\varepsilon) \varepsilon^{\frac{1}{4}}\|u\|-D(\varepsilon)\|u\| .\right.$$

By (47) we obtain
$$\left\|K_{y^{\prime}}^{\prime}(u)\right\| \geq\left(\frac{2((1+\delta)(1-\sqrt{\varepsilon}))^{2 n}}{c \xi^{2 n-1}(\varepsilon)}-B(n) \xi(\varepsilon) \varepsilon^{\frac{1}{4}}-D(\varepsilon)\right)\|u\|,$$
so
$$\left|\operatorname{det}\left(K_{y^{\prime}}^{\prime}\right)\right| \geq\left(\frac{2((1+\delta)(1-\sqrt{\varepsilon}))^{2 n}}{c \xi^{2 n-1}(\varepsilon)}-B(n) \xi(\varepsilon) \varepsilon^{\frac{1}{4}}-D(\varepsilon)\right)^{2 n},$$
By the definitions of $k^{\prime}$ and $K$ and equality (34), we have
$$\widetilde{g}_{h}\left(K \circ d_{y} \widetilde{F}_{c}(u), v\right)=c k_{y}^{\prime}(u, v)=c \widetilde{g}_{h}\left(K_{y}^{\prime}(u), v\right)$$
thus
$$\operatorname{det}\left(K_{y^{\prime}}\right) \operatorname{Jac} \widetilde{F}_{c}\left(y^{\prime}\right)=c^{2 n} \operatorname{det}\left(K_{y^{\prime}}^{\prime}\right),$$
by (28) we see that $\operatorname{Tr} K_{y^{\prime}}=4 n$. So we get
$$\begin{aligned}
& \left|\operatorname{Jac} \widetilde{F}_{c}\right|\left(y^{\prime}\right)=\left(\frac{\operatorname{Tr} K_{y^{\prime}}}{4 n}\right)^{2 n}\left|\operatorname{Jac} \widetilde{F}_{c}\right|\left(y^{\prime}\right) \\
& \quad \geq\left(\frac{1}{2}\right)^{2 n}\left|\operatorname{det}\left(K_{y^{\prime}}\right)\right|\left|\operatorname{Jac} \widetilde{F}_{c}\right|\left(y^{\prime}\right) \\
& \quad=\left(\frac{c}{2}\right)^{2 n}\left|\operatorname{det}\left(K_{y^{\prime}}^{\prime}\right)\right|\left(y^{\prime}\right)
\end{aligned}$$
therefore by (60)
$$\left|\operatorname{Jac} \widetilde{F}_{c}\right|\left(y^{\prime}\right) \geq c^{2 n}\left(\frac{((1+\delta)(1-\sqrt{\varepsilon}))^{2 n}}{c \xi^{2 n-1}(\varepsilon)}-\frac{1}{2} B(n) \xi(\varepsilon) \varepsilon^{\frac{1}{4}}-\frac{1}{2} D(\varepsilon)\right)^{2 n} .$$
If $\gamma$ intersect $\overline{\widetilde{Y}_{\varepsilon_{0}}}$, by (61), we have
$$\left(1-\sqrt{\varepsilon_{0}}\right)(1+\delta) \geq c^{2 n}\left(\frac{((1+\delta)(1-\sqrt{\varepsilon}))^{2 n}}{c \xi^{2 n-1}(\varepsilon)}-\frac{1}{2} B(n) \xi(\varepsilon) \varepsilon^{\frac{1}{4}}-\frac{1}{2} D(\varepsilon)\right)^{2 n} .$$
Since the previous inequality hold for $0<\varepsilon \leq \varepsilon_{0}$ and $\delta<\frac{\varepsilon}{(1+\varepsilon)}$, we get a contradiction as $\varepsilon$ approach to zero, indeed the first member goes to $\left(1-\sqrt{\varepsilon_{0}}\right)$, on the contrary the second member goes to 1. We conclude that $\widetilde{Y}_{\varepsilon_{0}}=\emptyset$. Therefore, passing $\widetilde{F}_{c}$ to its quotient $F_{c}$, equations (46) and (47) imply (56). \(\square\)

Proof of Theorem 3: Set $A^{\prime}(\varepsilon)=(1+\delta)^{2 n} \xi(\varepsilon)^{1-2 n}$ and $A^{\prime \prime}(\varepsilon)=\xi(\varepsilon)$ in Lemma 4.6, where $\xi(\varepsilon)$ is given by (57) (notice that $\xi(\varepsilon) \geq 1$ ). \(\square\)

The proof of the first part of Theorem 1 is complete.

Conclusion of the proof of Theorem 1, the $\varepsilon=0$ case. We want to prove that when $\varepsilon=0$, then $F_{c}$ is a holomorphic or anti-holomorphic local isometry. Suppose
that $g$ is normalized in order to have
$$\operatorname{Vol}(Y, g)=\operatorname{deg}(f) \operatorname{Vol}\left(X, g_{h}\right),$$
we want to prove that there exists a riemannian covering $F:(Y, g) \rightarrow\left(X, g_{h}\right)$. Take a sequence $\left\{F_{c_{n}}\right\}$ such that $0<\mathcal{X}(g) c_{n}-c_{0}<c_{0}\left(\sqrt[2 n]{\frac{1+2 \frac{1}{n}}{1+\frac{1}{n}}}-1\right)$. For $n$ sufficiently large, say $n>n_{0}$, the sequence $\left\{F_{c_{n}}\right\}$ consists of $\mathcal{C}^{1}$ covering maps. Being $X$ and $Y$ compact the $F_{c_{n}}$ are equibounded. By inequalities (40) we get
$$\begin{aligned}
& \left\|F_{c_{n}}\left(y_{0}\right)-F_{c_{n}}(y)\right\| \leq\left\|d_{y_{0}} F_{c_{n}}\right\|\left\|y_{0}-y\right\| \leq A^{\prime \prime}(\varepsilon)\left\|y_{0}-y\right\| \\
& \quad \leq A^{\prime \prime}\left(\frac{1}{n}\right)\left\|y_{0}-y\right\|,
\end{aligned}$$
therefore the maps $F_{c_{n}}$ are equicontinuous. By the Ascoli-Arzelà theorem there exist a subsequence $c_{n} \rightarrow c_{0}$, such that $F_{c_{n}}$ uniformly converge to a continuous function $F$ with $\operatorname{deg}(F)=\operatorname{deg}\left(F_{c_{n}}\right)=\operatorname{deg}(f)$. Let $\gamma:[0,1] \rightarrow Y$ a piecewise regular curve such that $\gamma(0)=y_{1}$ and $\gamma(1)=y_{2}$ then
$$\int_{0}^{1} A^{\prime}\left(\frac{1}{n}\right)\|\dot{\gamma}(t)\| d t \leq \int_{0}^{1}\left\|d_{y} F_{c_{n}}(\dot{\gamma}(t))\right\| d t \leq \int_{0}^{1} A^{\prime \prime}\left(\frac{1}{n}\right)\|\dot{\gamma}(t)\| d t$$
hence, denoted respectively $d(\cdot, \cdot)$ and $d^{h}(\cdot, \cdot)$ the geodesic distance on $(Y, g)$ and $\left(X, g_{h}\right)$ we have
$$d^{h}\left(F\left(y_{1}\right), F\left(y_{2}\right)\right) \leq d\left(y_{1}, y_{2}\right) .$$
By [2, Proposition C.1] the map $F$ is a riemannian covering. Arguing as in the last part of proof of [13, Theorem 1.1] we deduce that $F$ is holomorphic or antiholomorphic. The proof of Theorem 1 is complete.

Proof of Theorem 2 we need to verify that conditions (4) and (5) above are satisfied and then apply Theorem 1.

Condition (4) is satisfied. Let $\varphi:(Y, g) \rightarrow\left(N, g^{N}\right)$ be the strongly proper Kähler immersion of $Y$ in an locally classical symmetric space of noncompact type $N$ and let $\widetilde{\varphi}:(\widetilde{Y}, \widetilde{g}) \rightarrow\left(\Omega, g^{\Omega}\right)$ be its lift to the Kähler universal covers. By (9) we see that $(\widetilde{Y}, \widetilde{g})$ has the diastasis globally defined. As $\lim _{t \rightarrow+\infty} \frac{\log \cosh t}{t}=1$, fixed $\mu>0$ and $q \in \widetilde{Y}$, there exists a compact set $K \subset \widetilde{Y}$, two constant $L_{1}, L_{2} \in \mathbb{R}$ and $\varepsilon>0$ such that $\forall p \in \widetilde{Y} \backslash K$,
$$\begin{gathered}
\rho(q, p)-L_{2}<L_{1} e^{\mu \rho^{\Omega}(\widetilde{\varphi}(q), \widetilde{\varphi}(p))}<L_{1} e^{\mu\left(\log \cosh \rho^{\Omega}(\widetilde{\varphi}(q), \widetilde{\varphi}(p))+\varepsilon\right)} \\
<L_{1} e^{\frac{\mu}{2}\left(\mathcal{D}^{\Omega}(\widetilde{\varphi}(q), \widetilde{\varphi}(p))+2 \varepsilon\right)}=L_{1} e^{\frac{\mu}{2}(\mathcal{D}(q, p)+2 \varepsilon),}
\end{gathered}$$
where in the first inequality we use that $\varphi$ is strongly proper (notice that this is the unique point of the proof where this hypothesis is used), in the third one we used (12), while in the last equality we applied (9). On the other hand, if we choose
$\frac{\mu}{2}>0$ small enough so that $\left(c-\frac{\mu}{2}\right)>\frac{\operatorname{Ent}_{\mathrm{d}}(Y, g)}{\mathcal{X}(g)}$ we obtain
$$\int_{\widetilde{Y} \backslash K} e^{-\left(c-\frac{\mu}{2}\right) \mathcal{D}_{q}(p)} \nu_{g}(p)<\infty .$$
Putting together (62) and (63) we see that $\int_{\widetilde{Y}} \rho(q, p) e^{-c \mathcal{D}_{q}(p)} \nu_{g}(p)$ is convergent, so (4) is verified.

Condition (5) is satisfied. Being $Y$ compact, the second fundamental form of $\widetilde{\varphi}$ is bounded. Hence the conclusion follow by combining (11), (13) and (14) setting $\psi=\widetilde{\varphi}$. \(\square\)

\section*{References}
\begin{itemize}
\item[] [1] L. Bessières, G. Besson, G. Courtois, S. Gallot, Differentiable rigidity under Ricci curvature lower bound., Duke Math. J. 161 (2012), no. 1, 29-67.
\item[] [2] G. Besson, G. Courtois, S. Gallot, Entropies et rigidités des espaces localement symétriques de courbure strictement négative, Geom. Funct. Anal. 5 (1995), 731-799.
\item[] [3] G. Besson, G. Courtois, S. Gallot, Minimal entropy and Mostow's rigidity theorems, Ergodic Theory Dynam. Systems 16 (1996), no. 4, 623-649.
\item[] [4] G. Besson, G. Courtois, S. Gallot, Lemme de Schwarz réel et applications géométriques, Acta Math. 183 (1999), no. 2, 145-169.
\item[] [5] E. Calabi, Isometric Imbeddings of Complex Manifolds, Ann. of Math. 58 (1953), 1-23.
\item[] [6] K. McCrimmon, A taste of Jordan algebras, Universitext. Springer-Verlag, New York (2004).
\item[] [7] S. Helgason, Differential geometry, Lie groups, and symmetric spaces, Graduate Studies in Mathematics, 34 (2001).
\item[] [8] A. Loi, Calabi's diastasis function for Hermitian symmetric spaces, Differential Geom. Appl. 24 (2006), no. 3, 311-319.
\item[] [9] A. Loi, M. Zedda, Kähler Immersions of Kähler Manifolds into Complex Space Forms, Lecture Notes of the Unione Matematica Italiana 23, Springer, (2018).
\item[] [10] A. Loi, -, Some remarks on homogeneous Kähler manifolds, Geometriae dedicata. 179 (2015), no. 1, 377-383
\item[] [11] —, The volume entropy of local Hermitian symmetric space of noncompact type, Differential Geom. Appl. 31 (2013), no. 5, 594-601.
\item[] [12] —, A note on diastatic entropy and balanced metrics, J. Geom. Phys. 86 (2014), 492-496.
\item[] [13] -, Diastatic entropy and rigidity of complex hyperbolic manifolds (2015), Complex Manifolds 3 (2016), 186-192.
\end{itemize}

Departamento de Matemática
Universidade de São Paulo
Rua do Mataõ 1010, 05508-090 São Paulo, SP, Brazil
E-mail address: robertom@ime.usp.br
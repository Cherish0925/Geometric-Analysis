---
retention_scope: session
part: 1
total_parts: 1
---

---
source_file: 1505_02164v1.pdf
converter: mathpix
format: mmd
---

\title{
DIASTATIC ENTROPY AND RIGIDITY OF HYPERBOLIC MANIFOLDS
}

\author{
ROBERTO MOSSA
}

\begin{abstract}
Let $f: Y \rightarrow X$ be a continuous map between a compact real analytic Kähler manifold $(Y, g)$ and a compact complex hyperbolic manifold $\left(X, g_{0}\right)$. In this paper we give a lower bound of the diastatic entropy of $(Y, g)$ in terms of the diastatic entropy of $\left(X, g_{0}\right)$ and the degree of $f$. When the lower bound is attained we get geometric rigidity theorems for the diastatic entropy analogous to the ones obtained by G. Besson, G. Courtois and S. Gallot [2] for the volume entropy. As a corollary, when $X=Y$, we show that the minimal diastatic entropy is achieved if and only if $g$ is isometric to the hyperbolic metric $g_{0}$.
\end{abstract}

\section*{Contents}
\begin{itemize}
\item[1.] Introduction and statement of main results
\item[2.] Diastasis and diastasic entropy
\item[3.] Proof of Theorem 1.1 and Corollaries 1.1 1.2 and 1.3
\end{itemize}

References

\section*{1. Introduction and statement of main results}

In this paper, we define the diastatic entropy $\operatorname{Ent}_{\mathrm{d}}(Y, g)$ of a compact real analytic Kähler manifold $(Y, g)$ with globally defined diastasis function (see Definition 2.1 and 2.2 below). This is a real analytic invariant defined, in the noncompact case, by the author in [17], where the link with Donaldson's balanced condition is studied. The diastatic entropy extends the concept of volume entropy using the diastasis function instead of the geodesic distance. Throughout this paper a compact complex hyperbolic manifold will be a compact real analytic complex manifold $\left(X, g_{0}\right)$ endowed with locally Hermitian symmetric metric with holomorphic sectional curvature strictly negative (i.e. $\left(X, g_{0}\right)$ is the compact quotient of a complex hyperbolic space, see Example 2.3 below). Our main result is the following theorem, analogous to the celebrated result of G. Besson, G. Courtois, S. Gallot on the

\footnotetext{
Date: July 29, 2021.
}
minimal volume entropy of a compact negatively curved locally symmetric manifold (see (12) below) [2. Théorème Principal]:

Theorem 1.1. Let $(Y, g)$ be a compact Kähler manifold of dimension $n \geq 2$ and let $\left(X, g_{0}\right)$ be a compact complex hyperbolic manifold of the same dimension. If $f: Y \rightarrow X$ is a nonzero degree continuous map, then
$$\operatorname{Ent}_{\mathrm{d}}(Y, g)^{2 n} \operatorname{Vol}(Y, g) \geq|\operatorname{deg}(f)| \operatorname{Ent}_{\mathrm{d}}\left(X, g_{0}\right)^{2 n} \operatorname{Vol}\left(X, g_{0}\right) .$$
Moreover the equality is attained if and only if $f$ is homotopic to a holomorphic or anti-holomorphic homotheti ${ }^{1}$ covering $F: Y \rightarrow X$.

As a first corollary we obtain a characterization of the hyperbolic metric as that metric which realizes the minimum of the diastatic entropy:

Corollary 1.1. Let $\left(X, g_{0}\right)$ be a compact complex hyperbolic manifold of dimension $n \geq 2$ and denote by $\mathcal{E}\left(X, g_{0}\right)$ the set of metrics $g$ on $X$ with globally defined diastasis and fixed volume $\operatorname{Vol}(g)=\operatorname{Vol}\left(g_{0}\right)$. Then the functional $\mathcal{F}: \mathcal{E}\left(X, g_{0}\right) \rightarrow$ $\mathbb{R} \cup\{\infty\}$ given by $g \stackrel{\mathcal{F}}{\mapsto} \operatorname{Ent}_{\mathrm{d}}(X, g)$, attains its minimum when $g$ is holomorphically or anti-holomorphically isometric to $g_{0}$.

This corollary can be seen as the diastatic version of the A. Katok and M. Gromov conjecture on the minimal volume entropy of a locally symmetric space with strictly negative curvature (see [8, p. 58]), proved by G. Besson, G. Courtois, S. Gallot in [2]. We also apply Theorem 1.1 to give a simple proof for the complex version of the Mostow and Corlette-Siu-Thurston rigidity theorems:

Corollary 1.2. (Mostow). Let $\left(X, g_{0}\right)$ and $(Y, g)$ be two compact complex hyperbolic manifolds of dimension $n \geq 2$. If $X$ and $Y$ are homotopically equivalent then they are holomorphically or anti-holomorphically homothetic.

Corollary 1.3. (Corlette-Siu-Thurston). Let $\left(X, g_{0}\right)$ and $(Y, g)$ be as in the previous corollary and with the same (constant) holomorphic sectional curvature. If $f: Y \rightarrow X$ is a continuous map such that
$$\operatorname{Vol}(Y)=|\operatorname{deg}(f)| \operatorname{Vol}(X)$$
then there exists a holomorphically or anti-holomorphically Riemannian covering $F: Y \rightarrow X$ homotopic to $f$.

The paper consists of others two sections. In Section 2 we recall the basic definitions. Section 3 is dedicated to the proof of Theorem 1.1. The proof is based on the analogous result for the volume entropy (see formula (12) below) and on

\footnotetext{
${ }^{1} F$ is said to be homothetic if $F^{*} g_{0}=\alpha g$ for some $\alpha>0$.
}

Lemma 3.2 which provides a lower bound for the diastatic entropy in terms of volume entropy.

Acknowledgments. The author would like to thank Professor Sylvestre Gallot and Professor Andrea Loi for their help and their valuable comments.

\section*{2. Diastasis and diastasic entropy}

The diastasis is a special Kähler potential defined by E. Calabi in its seminal paper [5]. Let $(\widetilde{Y}, \widetilde{g})$ be a real analytic Kähler manifold. For every point $p \in \widetilde{Y}$ there exists a real analytic function $\Phi: V \rightarrow \mathbb{R}$, called Kähler potential, defined in a neighborhood $V$ of $p$ such that $\widetilde{\omega}=\frac{i}{2} \partial \bar{\partial} \Phi$, where $\widetilde{\omega}$ is the Kähler form associated to $\widetilde{g}$. Let $z=\left(z_{1}, \ldots, z_{n}\right)$ be a local coordinates system around $p$. By duplicating the variables $z$ and $\bar{z}$ the real analytic Kähler potential $\Phi$ can be complex analytically continued to a function $\hat{\Phi}: U \times U \rightarrow \mathbb{C}$ in a neighbourhood $U \times U \subset V \times V$ of $(p, p)$ which is holomorphic in the first entry and antiholomorphic in the second one.

Definition 2.1 (Calabi, [5]). The diastasis function $\mathcal{D}: U \times U \rightarrow \mathbb{R}$ is defined by
$$\mathcal{D}(z, w):=\hat{\Phi}(z, \bar{z})+\hat{\Phi}(w, \bar{w})-\hat{\Phi}(z, \bar{w})-\hat{\Phi}(w, \bar{z}) .$$
The diastasis function centered in $w$, is the Kähler potential $\mathcal{D}_{w}: U \rightarrow \mathbb{R}$ around $w$ given by
$$\mathcal{D}_{w}(z):=\mathcal{D}(z, w) .$$
We will say that a compact Kähler manifold $(Y, g)$ has globally defined diastasis if its universal Kähler covering $(\widetilde{Y}, \widetilde{g})$ has globally defined diastasis $\mathcal{D}: \widetilde{Y} \times \widetilde{Y} \rightarrow \mathbb{R}$.

One can prove that the diastasis is uniquely determined by the Kähler metric $\widetilde{g}$ and that it does not depend on the choice of the local coordinates system or on the choice of the Kähler potential $\Phi$.

Calabi in [5] uses the diastasis to give necessary and sufficient conditions for the existence of an holomorphic isometric immersion of a real analytic Kähler manifolds into a complex space form. For others interesting applications of the diastasis function see [10, 11, 12, 13, 14, 15, 18] and reference therein.

Assume that $(\widetilde{Y}, \widetilde{g})$ has globally defined diastasis $\mathcal{D}: \widetilde{Y} \times \widetilde{Y} \rightarrow \mathbb{R}$. Its (normalized ${ }^{2}$ ) diastatic entropy is defined by:
$$\operatorname{Ent}_{\mathrm{d}}(\widetilde{Y}, \widetilde{g})=\mathcal{X}(\widetilde{g}) \inf \left\{c \in \mathbb{R}^{+}: \int_{\widetilde{Y}} e^{-c \mathcal{D}_{w}} \nu_{\widetilde{g}}<\infty\right\},$$
where $\mathcal{X}(\widetilde{g})=\sup _{y, z \in \widetilde{Y}}\left\|\operatorname{grad}_{y} \mathcal{D}_{z}\right\|$ and $\nu_{\widetilde{g}}$ is the volume form associated to $\widetilde{g}$. If $\mathcal{X}(\widetilde{g})=\infty$ or the infimum in (3) is not achieved by any $c \in \mathbb{R}^{+}$, we set

\footnotetext{
${ }^{2}$ Our definition of diastatic entropy differs respect to the one given in [17] by the normalizing factor $\mathcal{X}(\widetilde{g})$.
}
$\operatorname{Ent}_{\mathrm{d}}(\widetilde{Y}, \widetilde{g})=\infty$. The definition does not depend on the base point $w$, indeed, as
$$\left|\mathcal{D}_{w_{1}}(x)-\mathcal{D}_{w_{2}}(x)\right|=\left|\mathcal{D}_{x}\left(w_{1}\right)-\mathcal{D}_{x}\left(w_{2}\right)\right| \leq \mathcal{X}(\widetilde{g}) \rho\left(w_{1}, w_{2}\right),$$
we have
$$e^{-c \mathcal{X}(\widetilde{g}) \rho\left(w_{1}, w_{2}\right)} \int_{\widetilde{Y}} e^{-c \mathcal{D}_{w_{1}}(x)} \nu_{\widetilde{g}} \leq \int_{\widetilde{Y}} e^{-c \mathcal{D}_{w_{2}}(x)} \nu_{\widetilde{g}} \leq e^{c \mathcal{X}(\widetilde{g}) \rho\left(w_{1}, w_{2}\right)} \int_{\widetilde{Y}} e^{-c \mathcal{D}_{w_{1}}(x)} \nu_{\widetilde{g}},$$
therefore $\int_{\widetilde{Y}} e^{-c \mathcal{D}_{w_{2}}(x)} \nu_{\widetilde{g}}<\infty$ if and only if $\int e^{-c \mathcal{D}_{w_{1}}(x)} \nu_{\widetilde{g}}<\infty$.

Definition 2.2. Let $(Y, g)$ be a compact Kähler manifold with globally defined diastasis. We define the diastatic entropy of $(Y, g)$ as
$$\operatorname{Ent}_{\mathrm{d}}(Y, g)=\operatorname{Ent}_{\mathrm{d}}(\tilde{Y}, \tilde{g})$$
where $(\widetilde{Y}, \widetilde{g})$ is the universal Kähler covering of $(Y, g)$.
Example 2.3. Let $\mathbb{C} H^{n}=\left\{z \in \mathbb{C}^{n}:\|z\|^{2}=\left|z_{1}\right|^{2}+\cdots+\left|z_{n}\right|^{2}<1\right\}$ be the unitary disc endowed with the hyperbolic metric $\widetilde{g}_{h}$ of constant holomorphic sectional curvature -4. The associated Kähler form and the diastasis are respectively given by
$$\widetilde{\omega}_{h}=-\frac{i}{2} \partial \bar{\partial} \log \left(1-\|z\|^{2}\right) .$$
and
$$\mathcal{D}^{h}(w, z)=-\log \left(\frac{\left(1-\|z\|^{2}\right)\left(1-\|w\|^{2}\right)}{\left|1-z w^{*}\right|^{2}}\right) .$$
Denote by $\omega_{e}=\frac{i}{2} \partial \bar{\partial}\|z\|^{2}$ the restriction to $\mathbb{C} H^{n}$ of the flat form of $\mathbb{C}^{n}$. One has
$$\int_{\mathbb{C} H^{n}} e^{-\alpha \mathcal{D}_{0}^{h}} \frac{\omega_{h}^{n}}{n!}=\int_{\mathbb{C} H^{n}}\left(1-|z|^{2}\right)^{\alpha-n-1} \frac{\omega_{e}^{n}}{n!}<\infty \Leftrightarrow \alpha>n,$$
and by a straightforward computation one sees that $\mathcal{X}\left(\widetilde{g}_{h}\right)=2$. We conclude by (3) that
$$\operatorname{Ent}_{\mathrm{d}}\left(\mathbb{C} H^{n}, \widetilde{g}_{h}\right)=2 n .$$

Remark 2.4. It should be interesting to compute $\mathcal{X}\left(g_{B}\right)$, where $g_{B}$ is the Bergman metric of an homogeneous bounded domain. This combined with the results obtained in [17], will allow us to obtain the diastatic entropy of this domains.

\section*{3. Proof of Theorem 1.1 and Corollaries 1.1, 1.2 and 1.3}

We start by recalling the definition of volume entropy of a compact Riemannian manifold $(M, g)$. Let $\pi:(\widetilde{M}, \widetilde{g}) \rightarrow(M, g)$ its riemannian universal cover. We define the volume entropy of $(M, g)$ as
$$\operatorname{Ent}_{\mathrm{v}}(M, g)=\inf \left\{c \in \mathbb{R}^{+}: \int_{\widetilde{M}} e^{-c \widetilde{\rho}(w, x)} \nu_{\widetilde{g}}(x)<\infty\right\},$$
where $\widetilde{\rho}$ is the geodesic distance on $(\widetilde{M}, \widetilde{g})$ and $\nu_{\widetilde{g}}$ is the volume form associated to $\widetilde{g}$. By the triangular inequality, we can see that the definition does not depend on the base point $w$. As the volume entropy depends only on the Riemannian universal cover it make sense to define
$$\operatorname{Ent}_{\mathrm{v}}(\widetilde{M}, \widetilde{g})=\operatorname{Ent}_{\mathrm{v}}(M, g)$$

The classical definition of volume entropy of a compact riemannian manifold $(M, g)$, is the following
$$\operatorname{Ent}_{\mathrm{vol}}(M, g)=\lim _{t \rightarrow \infty} \frac{1}{t} \log \operatorname{Vol}\left(B_{p}(t)\right),$$
where $\operatorname{Vol}\left(B_{p}(t)\right)$ denotes the volume of the geodesic ball $B_{p}(t) \subset \widetilde{M}$, of center in $p$ and radius $t$. This notion of entropy is related with one of the main invariant for the dynamics of the geodesic flow of $(M, g)$ : the topological entropy $\operatorname{Ent}_{\text {top }}(M, g)$ of this flow. For every compact manifold $(M, g)$ A. Manning in [19] proved the inequality $\operatorname{Ent}_{\text {vol }}(M, g) \leq \operatorname{Ent}_{\text {top }}(M, g)$, which is an equality when the curvature is negative. We refer the reader to the paper [2] (see also [3] and [4]) of G. Besson, G. Courtois and S. Gallot for an overview on the volume entropy and for the proof of the celebrated minimal entropy theorem. For an explicit computation of the volume entropy $\operatorname{Ent}_{\mathrm{v}}(\Omega, g)$ of a symmetric bounded domain $(\Omega, g)$ see [16].

The next lemma shows that the classical definition of volume entropy (7) does not depend on the base point and it is equivalent to definition (6), that is
$$\operatorname{Ent}_{\mathrm{vol}}(M, g)=\operatorname{Ent}_{\mathrm{v}}(M, g) .$$

Lemma 3.1. Denote by
$$\underline{L}:=\liminf _{R \rightarrow+\infty}\left(\frac{1}{R} \log \left(\operatorname{Vol} B\left(x_{0}, R\right)\right)\right)$$
and
$$\bar{L}:=\limsup _{R \rightarrow+\infty}\left(\frac{1}{R} \log \left(\operatorname{Vol} B\left(x_{0}, R\right)\right)\right),$$
where $B\left(x_{0}, R\right) \subset(\widetilde{M}, \widetilde{g})$ is the geodesic ball of centre $x_{0}$ and radius $R$. Then the two limits does not depends on $x_{0}$ and
$$\underline{L} \leq \operatorname{Ent}_{\mathrm{v}}(M, g) \leq \bar{L} .$$
Proof. Let $x_{1}$ an arbitrary point of $M$. Set $D=d\left(x_{0}, x_{1}\right)$ and $R>D$. By the triangular inequality
$$B\left(x_{0}, R-D\right) \subset B\left(x_{1}, R\right) \subset B\left(x_{0}, R+D\right) .$$

Let $R^{\prime}=R+D$, we have
$$\begin{gathered}
\liminf _{R \rightarrow+\infty}\left(\frac{1}{R} \log \left(\operatorname{Vol} B\left(x_{1}, R\right)\right)\right) \leq \liminf _{R \rightarrow+\infty}\left(\frac{1}{R} \log \left(\operatorname{Vol} B\left(x_{0}, R+D\right)\right)\right) \\
=\liminf _{R^{\prime} \rightarrow+\infty}\left(\frac{R^{\prime}}{R^{\prime}-D} \frac{1}{R^{\prime}} \log \left(\operatorname{Vol} B\left(x_{0}, R^{\prime}\right)\right)\right) \\
\leq \liminf _{R^{\prime} \rightarrow+\infty}\left(\frac{1}{R^{\prime}} \log \left(\operatorname{Vol} B\left(x_{0}, R^{\prime}\right)\right)\right)
\end{gathered}$$
With the same argument one can prove the inequality in the other direction, so that $\underline{L}$ does not depend on $x_{0}$. Analogously we can prove that $\bar{L}$ does not depend on $x_{0}$.

By the definition of limit inferior and superior, for every $\varepsilon>0$, there exists $R_{0}(\varepsilon)$ such that, for $R \geq R_{0}(\varepsilon)$,
$$\underline{L}-\varepsilon \leq\left(\frac{1}{R} \log \left(\operatorname{Vol} B\left(x_{0}, R\right)\right)\right) \leq \bar{L}+\varepsilon$$
equivalently
$$e^{(\underline{L}-\varepsilon) R} \leq\left(\operatorname{Vol} B\left(x_{0}, R\right)\right) \leq e^{(\bar{L}+\varepsilon) R} .$$
Integrating by parts we obtain
$$\begin{aligned}
I & :=\int_{\widetilde{M}} e^{-c \widetilde{\rho}\left(x_{0}, x\right)} d v(x)=\int_{0}^{\infty} e^{-c r} \operatorname{Vol}_{n-1}\left(S\left(x_{0}, r\right)\right) d r \\
& =\left.\operatorname{Vol}\left(B\left(x_{0}, r\right)\right) e^{-c r}\right|_{0} ^{\infty}+c \int_{0}^{\infty} e^{-c r} \operatorname{Vol}\left(B\left(x_{0}, r\right)\right) d r
\end{aligned}$$
where $S\left(x_{0}, r\right)=\partial B\left(x_{0}, r\right)$. On the other hand, by (8) we get
$$\int_{R_{0}(\varepsilon)}^{\infty} e^{(\underline{L}-c-\varepsilon) r} d r \leq \int_{R_{0}(\varepsilon)}^{\infty} e^{-c r} \operatorname{Vol}\left(B\left(x_{0}, r\right)\right) d r \leq \int_{R_{0}(\varepsilon)}^{\infty} e^{-(c-\bar{L}-\varepsilon) r} d r$$
We deduce that if $c>\bar{L}$ then $I$ is convergent i.e $\bar{L} \geq \operatorname{Ent}_{\mathrm{v}}$ and that if $I$ is not convergent when $c<\underline{L}$, that is $\operatorname{Ent}_{\mathrm{v}} \geq \underline{L}$, as wished. \(\square\)

The next lemma show that the diastatic entropy is bounded from below by the volume entropy.

Lemma 3.2. Let $(Y, g)$ be a compact Kähler manifold with globally defined diastasis, then
$$\operatorname{Ent}_{\mathrm{d}}(Y, g) \geq \operatorname{Ent}_{\mathrm{v}}(Y, g) .$$
This bound is sharp when $(Y, g)$ is a compact quotient of the complex hyperbolic space. That is,
$$\operatorname{Ent}_{\mathrm{d}}\left(\mathbb{C} H^{n}, \widetilde{g}_{h}\right)=2 n=\operatorname{Ent}_{\mathrm{v}}\left(\mathbb{C} H^{n}, \widetilde{g}_{h}\right) .$$
Proof. Let $(\widetilde{Y}, \widetilde{g})$ be universal Kähler cover of $(Y, g)$. For every $w, x \in \widetilde{Y}$ we have
$$\mathcal{D}_{w}(x)=\mathcal{D}_{w}(x)-\mathcal{D}_{w}(w) \leq \sup _{z \in \widetilde{Y}}\left\|d_{z} \mathcal{D}_{w}\right\| \rho_{w}(x) \leq \mathcal{X}(\widetilde{g}) \rho_{w}(x),$$
so
$$\int_{\widetilde{Y}} e^{-c \mathcal{X}(\widetilde{g}) \rho_{w}(x)} \nu_{\widetilde{g}} \leq \int_{\widetilde{Y}} e^{-c \mathcal{D}_{w}(x)} \nu_{\widetilde{g}} .$$
Therefore, if $c \mathcal{X}(\widetilde{g}) \leq \operatorname{Ent}_{\mathrm{v}}(\widetilde{Y}, \widetilde{g})$ then $c \mathcal{X}(\widetilde{g}) \leq \operatorname{Ent}_{\mathrm{d}}(\widetilde{Y}, \widetilde{g})$. We obtain (9) by setting $c=\frac{\operatorname{Ent}_{\mathrm{v}}(\widetilde{Y}, \widetilde{g})}{\mathcal{X}(\widetilde{g})}$. Equation (10) follow by (5) and [16, Theorem 1.1]. \(\square\)

Proof of Theorem 1.1. Let $\left(X, g_{0}\right)$ as in Theorem 1.1 and let $\pi_{X}:\left(\mathbb{C} H^{n}, \widetilde{g}_{0}\right) \rightarrow$ $\left(X, g_{0}\right)$ be the universal covering. Notice that $\widetilde{g}_{0}=\lambda \widetilde{g}_{h}$ for some positive $\lambda$. Then we have
$$\begin{aligned}
& \operatorname{Vol}\left(X, g_{0}\right) \operatorname{Ent}_{\mathrm{v}}\left(X, g_{0}\right)^{2 n}=\operatorname{Vol}\left(X, g_{h}\right) \operatorname{Ent}_{\mathrm{v}}\left(X, g_{h}\right)^{2 n} \\
= & \operatorname{Vol}\left(X, g_{h}\right) \operatorname{Ent}_{\mathrm{d}}\left(X, g_{h}\right)^{2 n}=\operatorname{Vol}\left(X, g_{0}\right) \operatorname{Ent}_{\mathrm{d}}\left(X, g_{0}\right)^{2 n},
\end{aligned}$$
where the first and the third equality are consequence of the fact that $\operatorname{Ent}_{\mathrm{v}}\left(\mathbb{C} H^{n}, \widetilde{g}_{0}\right)=$ $\frac{1}{\sqrt{\lambda}} \operatorname{Ent}_{\mathrm{v}}\left(\mathbb{C} H^{n}, \widetilde{g}_{h}\right)$ and $\operatorname{Ent}_{\mathrm{d}}\left(\mathbb{C} H^{n}, \widetilde{g}_{0}\right)=\frac{1}{\sqrt{\lambda}} \operatorname{Ent}_{\mathrm{d}}\left(\mathbb{C} H^{n}, \widetilde{g}_{h}\right)$, while the second equality follows by (10). Let $f: Y \rightarrow X$ be as in Theorem 1.1, then, by 2. Théorème Principal] we know that
$$\operatorname{Ent}_{\mathrm{v}}(Y, g)^{2 n} \operatorname{Vol}(Y, g) \geq|\operatorname{deg}(f)| \operatorname{Ent}_{\mathrm{v}}\left(X, g_{0}\right)^{2 n} \operatorname{Vol}\left(X, g_{0}\right)$$
where the equality is attained if and only if $f$ is homotopic to a homothetic covering $F: Y \rightarrow X$. Putting together (9), (11) and (12) we get that
$$\operatorname{Ent}_{\mathrm{d}}(Y, g)^{2 n} \operatorname{Vol}(Y, g) \geq|\operatorname{deg}(f)| \operatorname{Ent}_{\mathrm{d}}\left(X, g_{0}\right)^{2 n} \operatorname{Vol}\left(X, g_{0}\right)$$
where the equality is attained if and only if $f$ is homotopic to a homothetic covering $F: Y \rightarrow X$.

To conclude the proof it remains to prove that $F$ is holomorphic or anti-holomorphic. Up to homotheties, it is not restrictive to assume that $g=F^{*} g_{0}$, so that its lift $\widetilde{F}: \widetilde{Y} \rightarrow \mathbb{C} H^{n}$ to the universal covering it is a global isometry. Fix a point $q \in \widetilde{Y}$, let $p=\widetilde{F}(q)$ and denote $A_{q}=\widetilde{F}^{*} J_{0 p}$ the endomorphism acting on $T_{q} \widetilde{Y}$, where $J_{0}$ is the complex structure of $\mathbb{C} H^{n}$. Denote by $\mathcal{G}_{\widetilde{Y}}$ and respectively $\mathcal{G}_{\mathbb{C} H^{n}}$ the holonomy groups of $(\widetilde{Y}, \widetilde{g})$ and respectively $\left(\mathbb{C} H^{n}, \widetilde{g}_{0}\right)$. Note that $\mathcal{G}_{\widetilde{Y}}=\widetilde{F}^{*} \mathcal{G}_{\mathbb{C} H^{n}}$ and that $\mathcal{G}_{\mathbb{C} H^{n}}=S U(n)$, therefore $\mathcal{G}_{\widetilde{Y}}$ acts irreducibly on $T_{q} \widetilde{Y}$. As $J_{0}$ commutes with the action of $\mathcal{G}_{\mathbb{C} H^{n}}$, by construction $A_{q}$ is invariant with respect to the action of $\mathcal{G}_{\widetilde{Y}}$. Therefore, denoted $\operatorname{Id}_{q}$ the identity map of $T_{q} \widetilde{Y}$, by Schur's lemma, $A_{q}=\lambda \operatorname{Id}_{q}$ with $\lambda \in \mathbb{C}$. Moreover $-\operatorname{Id}_{q}=A_{q}^{2}=\lambda^{2} \operatorname{Id}_{q}$, so $\lambda= \pm i$. By the arbitrarity of $q$ we conclude that $\widetilde{F}$ is holomorphic or anti-holomorphic.

Proof of Corollary 1.1. This is an immediate consequence of Theorem 1.1 once assumed $Y=X, \operatorname{Vol}(g)=\operatorname{Vol}\left(g_{0}\right)$ and $f=\operatorname{id}_{X}$ the identity map of $X$.

Proof of Corollary 1.2. Let $h: Y \rightarrow X$ be an homotopic equivalence and $h^{-1}$ its homotopic inverse. Substituting in (1), once with $f=h$ and once with $f=h^{-1}$,
we have respectively
$$\operatorname{Ent}_{\mathrm{d}}(Y, g)^{2 n} \operatorname{Vol}(Y, g) \geq|\operatorname{deg}(h)| \operatorname{Ent}_{\mathrm{d}}\left(X, g_{0}\right)^{2 n} \operatorname{Vol}\left(X, g_{0}\right)$$
and
$$\operatorname{Ent}_{\mathrm{d}}\left(X, g_{0}\right)^{2 n} \operatorname{Vol}\left(X, g_{0}\right) \geq\left|\operatorname{deg}\left(h^{-1}\right)\right| \operatorname{Ent}_{\mathrm{d}}(Y, g)^{2 n} \operatorname{Vol}(Y, g) .$$
We then conclude that $\operatorname{Ent}_{\mathrm{d}}(Y, g)^{2 n} \operatorname{Vol}(Y, g)=\operatorname{Ent}_{\mathrm{d}}\left(X, g_{0}\right)^{2 n} \operatorname{Vol}\left(X, g_{0}\right)$ and that $|\operatorname{deg}(h)|=1$. Therefore, by applying the last part of Theorem 1.1, we see that $h$ is homotopic to an holomorphic (or antiholomorphic) homothety $F: X \rightarrow Y$.

Proof of Corollary 1.3. Let $\pi_{Y}:\left(\mathbb{C} H^{n}, \widetilde{g}\right) \rightarrow(Y, g)$ and $\pi_{X}:\left(\mathbb{C} H^{n}, \widetilde{g}_{0}\right) \rightarrow$ $\left(X, g_{0}\right)$ be the universal coverings, since $g_{0}$ and $g$ are both hyperbolic with the same curvature, we conclude that $\widetilde{g}_{0}=\widetilde{g}$ and that $\operatorname{Ent}_{\mathrm{d}}\left(X, g_{0}\right)=\operatorname{Ent}_{\mathrm{d}}(Y, g)$. Therefore we get an equality in (1). Using again the last part of Theorem 1.1 we get $\operatorname{Vol}(Y)=|\operatorname{deg}(F)| \operatorname{Vol}(X)$ and we conclude that $F$ is locally isometric.

\section*{References}
[1] J. Arazy, A survey of invariant hilbert spaces of analytic functions on bounded symmetric domains, Contemp. Math. 185 (1995).
[2] G. Besson, G. Courtois, S. Gallot, Entropies et rigidités des espaces localement symétriques de courbure strictement négative, Geom. Funct. Anal. 5 (1995), 731-799.
[3] G. Besson, G. Courtois, S. Gallot, Minimal entropy and Mostow's rigidity theorems, Ergodic Theory Dynam. Systems 16 (1996), no. 4, 623-649.
[4] G. Besson, G. Courtois, S. Gallot, Lemme de Schwarz réel et applications géométriques, Acta Math. 183 (1999), no. 2, 145-169.
[5] E. Calabi, Isometric Imbeddings of Complex Manifolds, Ann. of Math. 58 (1953), 1-23.
[6] K. McCrimmon, A taste of Jordan algebras, Universitext. Springer-Verlag, New York (2004).
[7] S. K. Donaldson, Scalar curvature and projective embeddings, I. J. Differential Geom. 59 (2001), no. 3, 479-522.
[8] M. Gromov, Filling Riemannian manifolds, J. Diff. Geom. 18 (1983), 1-147
[9] S. Helgason, Differential geometry, Lie groups, and symmetric spaces, Graduate Studies in Mathematics, 34 (2001).
[10] A. Loi, -, Berezin quantization of homogeneous bounded domains, Geom. Dedicata 161 (2012), 119-128.
[11] A. Loi, -, The diastatic exponential of a symmetric space, Math. Z. 268 (2011), 3-4, 1057-1068.
[12] A. Loi, -, Some remarks on homogeneous Kähler manifolds, arXiv:1502.00011
[13] A. Loi, -, F. Zuddas, Symplectic capacities of Hermitian symmetric spaces, to appear in J. Symplect. Geom.
[14] A. Loi, -, F. Zuddas, The log-term of the disc bundle over a homogeneous Hodge manifold, (2013), arXiv:1402.2089
[15] A. Loi, -, F. Zuddas, Some remarks on the Gromov width of homogeneous Hodge manifolds, Int. J. Geom. Methods Mod. Phys. 11 (2014), no. 9.
[16] -, The volume entropy of local Hermitian symmetric space of noncompact type, Differential Geom. Appl. 31 (2013), no. 5, 594-601.
[17] -, A note on diastatic entropy and balanced metrics, J. Geom. Phys. 86 (2014), 492-496.
[18] -, A bounded homogeneous domain and a projective manifold are not relatives, Riv. Mat. Univ. Parma 4 (2013), no. 1, 55-59.
[19] A. Manning, Topological entropy for geodesic flows, Ann. of Math. (2) 110 (1979), no. 3, 567-573.

Departamento de Matemática, Universidade de São Paulo, Rua do Matão 1010, CEP 05508-900, So Paulo, SP, Brazil
E-mail address: roberto.mossa@gmail.com
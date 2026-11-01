---
retention_scope: session
part: 1
total_parts: 1
---

---
source_file: 1810_03240.pdf
converter: mathpix
format: mmd
---

\title{
On Effective Existence of Symmetric Differentials of Complex Hyperbolic Space Forms
}

\author{
Kwok-Kin Wong*
}

\begin{abstract}
For a noncompact complex hyperbolic space form of finite volume $X=\mathbb{B}^{n} / \Gamma$, we consider the problem of producing symmetric differentials vanishing at infinity on the Mumford compactification $\bar{X}$ of $X$ similar to the case of producing cusp forms on hyperbolic Riemann surfaces. We introduce a natural geometric measurement which measures the size of the infinity $\bar{X}-X$ called canonical radius of a cusp of $\Gamma$. The main result in the article is that there is a constant $r^{*}=r^{*}(n)$ depending only on the dimension, so that if the canonical radii of all cusps of $\Gamma$ are larger than $r^{*}$, then there exist symmetric differentials of $\bar{X}$ vanishing at infinity. As a corollary, we show that the cotangent bundle $T_{\bar{X}}$ is ample modulo the infinity if moreover the injectivity radius in the interior of $\bar{X}$ is larger than some constant $d^{*}=d^{*}(n)$ which depends only on the dimension.
\end{abstract}

\section*{1 Introduction}

Let $\Omega$ be an irreducible bounded symmetric domain and $\Gamma \subset \operatorname{Aut}_{0}(\Omega)$ be a torsion-free lattice so that $X=\Omega / \Gamma$ is a noncompact finite volume quotient with respect to the canonical Kähler-Einstein metric. Our main interest will be certain hyperbolic properties of the compactifications of $X$. We say that a complex space $M$ is (Brody) hyperbolic if there exists no non-constant holomorphic map $f: \mathbb{C} \rightarrow M$. When $M$ is compact, being hyperbolic is equivalent to that the Kobayashi pseudo distance function on $M$ is actually a distance function.

It is well-known, however, that $\bar{X}$ is in general not hyperbolic. For example, there is (noncompact) modular curve $X_{k}=\mathbb{H} / \Gamma_{0}(k)$ for some

\footnotetext{
*Department of Mathematics, The University of Hong Kong. Email: kkwongm@gmail.com
}
small $k \in \mathbb{N}$, such that $\overline{X_{k}}$ is $\mathbb{P}^{1}$ or elliptic curve. Nonetheless, suppose $X_{k}=\mathbb{H} / \Gamma_{0}(k)$ is a modular curve so that $\overline{X_{k}}$ is not hyperbolic. There is a sufficiently large $N \geq k$ such that $\overline{X_{N}}$ is hyperbolic. In this case, we say that $\overline{X_{k}}$ is hyperbolic up to cover. Such an idea has been generalized by Nadel to arithmetic quotients of bounded symmetric domain:

Theorem 1.1 (cf. Theorem 0.1, Nadel [15]). Let $\Omega$ be a bounded symmetric domain, $\Gamma \subset \operatorname{Aut}(\Omega)$ be an arithmetic lattice and $\overline{\Omega / \Gamma}$ be any compactification of $\Omega / \Gamma$. Then there is a cover $\Omega / \Gamma^{\prime} \rightarrow \Omega / \Gamma$ such that the image of any holomorphic curve $f: \mathbb{C} \rightarrow \overline{\Omega / \Gamma^{\prime}}$ lies on $\overline{\Omega / \Gamma^{\prime}}-\Omega / \Gamma^{\prime}$.

Theorem 1.1 has an important consequence on hyperbolicity of $\Omega / \Gamma$. For instance, if one takes the Satake-Baily-Borel compactification $X^{\prime}$ of $X=\Omega / \Gamma$, then one concludes that $X^{\prime}$ is hyperbolic up to cover since $X$ is compactified again by quotients of bounded symmetric domains. The hyperbolicity of the Mumford compactification $\bar{X}$, however, is still not known by our knowledge.

We are going to look at the possibly simplest situation in higher dimensions, where $\Omega=\mathbb{B}^{n}$ is the complex unit ball of dimension $n \geq 2$. Let $X=\mathbb{B}^{n} / \Gamma$ be quotient of the complex unit ball by a torsion-free lattice $\Gamma \subset \operatorname{Aut}\left(\mathbb{B}^{n}\right)$ of finite volume with respect to the canonical Kähler-Einstein metric. The noncompact manifold $X$ admits toroidal compactification $\bar{X}$ by [1] in case $\Gamma$ is arithmetic and by [12] for non-arithmetic $\Gamma$. It is shown that $\bar{X}$ possesses many hyperbolic properties (see for example, [5], [6], [7], [16]).

It is well-known that a projective manifold with ample cotangent bundle is hyperbolic. However, the converse is false. For example, take a product of Riemann surfaces of genus $\geq 2$. For the situation $\bar{X}$ is the Mumford compactification of $X=\mathbb{B}^{n} / \Gamma$, we know that it is in general not hyperbolic and hence has a non-ample cotangent bundle. We will study a weaker notion of ampleness of cotangent bundle, namely, the ampleness modulo a divisor. We say that a vector bundle $E \rightarrow M$ over a complex space is ample modulo a divisor $D \subset M$ if the global sections of the tautological line bundle $\mathcal{O}_{\mathbb{P} E^{*}}(1){ }^{1}$ induces an embedding of $\mathbb{P} E^{*}-\pi^{-1}(D)$ into some projective space, where $\pi: \mathbb{P} E^{*} \rightarrow M$ is the natural projection. To us, Nadel's theorem is a consequence of the existence of pluricanonical sections vanishing at infinity. In the same spirit, we are going to show that

Theorem 1.2 (Main Theorem). Let $X=\mathbb{B}^{n} / \Gamma$ be a quotient of the complex unit ball $\mathbb{B}^{n} \subset \mathbb{C}^{n}(n \geq 2)$ by a torsion-free lattice $\Gamma \subset \operatorname{Aut}\left(\mathbb{B}^{n}\right)$, which is not

\footnotetext{
${ }^{1}$ The notation $\mathbb{P} E$ is the projectivization of the bundle $E$ instead of the dual of $E$, which is different from literatures in algebraic geometry.
}
necessarily arithmetic, of finite volume with respect to the canonical Kähler-Einstein metric $g_{X}$ that induced from the normalized Bergman metric $g$ on $\mathbb{B}^{n}$ of constant holomorphic sectional curvature -2. Write $\bar{X}$ to be the Mumford compactification of $X$. Let $b_{1}, \ldots, b_{k} \in \partial \mathbb{B}^{n}$ be the cusps of $\Gamma$ with canonical radii $r_{1} \geq \cdots \geq r_{k}$ so that $\Omega:=\coprod_{j=1}^{k} \Omega_{b_{j}}$ is a disjoint union of neighbourhoods in $\bar{X}$ corresponding to the cusps. Denote by $\Omega^{\prime}$ the complement of $\Omega$ and by $d\left(\Omega^{\prime}\right)$ the injectivity radius of $\Omega^{\prime}$ with respect to $g$.

Then there are constants $r^{*}=r^{*}(n)$ and $d^{*}=d^{*}(n)$ depending only on the dimension $n$ such that if $d\left(\Omega^{\prime}\right) \geq d^{*}$ and $r_{1} \geq \cdots \geq r_{k} \geq r^{*}$, the cotangent bundle $T_{\bar{X}}^{*}$ is ample modulo $D=\bar{X}-X$.

We say that $\left\{X_{k}\right\}_{k=0}^{\infty}$ is a tower of coverings of $X$, if $X_{0}=X$ and for each $k \geq 0, X_{k+1} \rightarrow X_{k}$ is a finite covering such that $\pi_{1}\left(X_{k}\right) \subset \pi_{1}(X)$ is a normal subgroup and such that $\cap_{i=0}^{\infty} \pi_{1}\left(X_{k}\right)=\{1\}$. For example, it is well-known that any arithmetic quotient of $\mathbb{B}^{n}$ has a tower of coverings. Since both injectivity radii of the interior part and the canonical radii corresponding to cusp neighbourhoods increase upon lifting along the tower of coverings, a direct consequence of Theorem 1.2 is

Corollary 1.3. Suppose $\left\{X_{k}\right\}_{k=0}^{\infty}$ is a tower of coverings of $X$. Then there is $k \geq 0$ such that the cotangent bundle $T_{\overline{X_{k}}}^{*}$ is ample modulo $\overline{X_{k}}-X_{k}$. Hence if $\Gamma^{\prime}$ is any finite index subgroup of $\pi_{1}\left(X_{k}\right)$, then the cotangent bundle of $\overline{X^{\prime}}$, where $X^{\prime}=\mathbb{B}^{n} / \Gamma^{\prime}$, is ample modulo $\overline{X^{\prime}}-X^{\prime}$.

The proof of Theorem 1.2 is done by methods of $L^{2}$-estimates. From our point of view, the proof boils down to the construction of holomorphic symmetric differentials vanishing at infinity, which can also be thought of as a generalization of cusps form in modular curves. As inspired by the works of Mumford [14], Nadel [15] and Bakker-Tsimerman [5], an important element for the existence of the desired symmetric differentials is to make sure the size of the lattice " $\Gamma$ is sufficiently small" or the infinity " $D$ is not too big". Hence we introduce the notion of canonical radius of a cusp, which measures the size of the infinity corresponding to a cusp of $\Gamma$. The canonical radius is probably a well-known quantity among experts in hyperbolic geometry (see for example, [13]).

Our method relies on certain asymptotic properties of the canonical metric $g_{X}$ on $X$ and the curvature $\Theta$. On the other hand, in the proof of the ampleness modulo infinity, the injectivity radius will also play an essential role. The key point is, in the verification of the basic estimates required for $L^{2}$-estimates, the curvature term is positive and of growth $1 / \delta^{2}$ as $\delta \rightarrow 0$, where $\delta$ is the distance to the boundary. The only negativity coming from
the weight function is of growth $1 / \delta$ as $\delta \rightarrow 0$. Thus the basic estimates are verified if the canonical radii are large so that the support where the negativity occurs lie in region close enough to the boundary. Another important ingredient is the construction of locally holomorphic symmetric differentials vanishing along the infinity by applying a technique of Grauert (see Proposition 4.2).

Recently, there seems to be an interest in producing symmetric differentials for Hermitian locally symmetric spaces in relation to the fundamental group representation and Hodge theory, see for example [10], [3]. Especially in [10] Theorem 1.6 and Theorem 1.26, where the effectiveness plays an important role. We hope that in the near future, such relations can be further explored in the context of complex analytic geometry.

The organization of the rest of the article is as follows. In §2, we recall briefly the Mumford compactification of $X=\mathbb{B}^{n} / \Gamma$. In §3, several asymptotic properties of the Bergman metric and the induced canonical metric will be illustrated. In §4, the construction of symmetric differential vanishing at infinity will be done. In §5, the ampleness modulo infinity of the cotangent of $\bar{X}$ will be shown, as well as Corollary 1.3.

\section*{2 Descriptions of the Mumford Compactification of $X=\mathbb{B}^{n} / \Gamma$}

We first recall the Mumford compactification of $X=\mathbb{B}^{n} / \Gamma$. Our presentation follows [12].

Fix a cusp $b \in \partial \mathbb{B}^{n}$ of $\Gamma$. By composing a unitary transformation and the inverse Cayley transformation, we may let $b=q_{\infty}$ be the distinguish infinity of the Siegel upper half space $S$. Write $\Gamma_{\infty}=\Gamma_{q_{\infty}}=\Gamma \cap P_{\infty}$ (where $P_{\infty}:=P_{q_{\infty}} \subset \operatorname{Aut}\left(\mathbb{B}^{n}\right)$ is the isotropy subgroup of a point $q_{\infty}$ ). Let $U_{\infty}=\operatorname{rad} P_{\infty}$ be the unipotent radical of $P_{\infty}$. Note that $\Gamma \cap\left[U_{\infty}, U_{\infty}\right]$ is one dimensional and is generated by some $\tau>0$.

We let $\Omega_{b}^{(u)} \subset \bar{X}$ to be a horoball neighbourhood of the cusp $b$ of height $u>0$, which can be described more explicitly as follows. For each $u>0$, let
$$S^{(u)}:=\left\{\left(z^{\prime}, z_{n}\right) \in \mathbb{C}^{n}\left|\operatorname{Im} z_{n}>\left|z^{\prime}\right|^{2}+u\right\} .\right.$$
Thus $u_{1}>u_{2}$ implies $S^{\left(u_{1}\right)} \subset S^{\left(u_{2}\right)} \subset S^{(0)}=: S$. Consider the quotient of $S$ by $\Gamma \cap\left[U_{\infty}, U_{\infty}\right]$ given by the holomorphic covering map
$$\left.\begin{array}{llc}
\Psi: & \mathbb{C}^{n-1} \times \mathbb{C} & \rightarrow \\
& \left(z^{\prime}, z_{n}\right) & \mapsto \\
& \mapsto & \left(z^{\prime}, e^{\frac{2 \pi-1}{T} z_{n}} \times \mathbb{C}^{*}\right.
\end{array}\right):=\left(w^{\prime}, w_{n}\right),$$
where $\tau \in \mathbb{R}$ corresponds to the generator of $\Gamma \cap\left[U_{\infty}, U_{\infty}\right]$. In the Mumford compactification, the cusp is compactified by taking interior closure of $\mathbb{C}^{n-1} \times \Delta^{*} \subset \mathbb{C}^{n-1} \times \Delta$.

Let $G:=\Psi(S), G^{(u)}:=\Psi\left(S^{(u)}\right)$. For each $u>0$, the canonical projection $G^{(u)} \rightarrow \mathbb{C}^{n-1}$ realizes $G^{(u)}$ as the total space of a puncture disk bundle over $\mathbb{C}^{n-1}$. Let
$$\begin{gathered}
\hat{G}:=\left\{\left.\left(w^{\prime}, w_{n}\right) \in \mathbb{C}^{n}| | w_{n}\right|^{2}<e^{\frac{-4 \pi}{\tau}}\left|w^{\prime}\right|^{2}\right\}, \\
\hat{G}^{(u)}:=\left\{\left.\left(w^{\prime}, w_{n}\right) \in \mathbb{C}^{n}| | w_{n}\right|^{2}<e^{\frac{-4 \pi}{\tau} u} \cdot e^{-\frac{4 \pi}{\tau}\left|w^{\prime}\right|^{2}}\right\} .
\end{gathered}$$
The sets $\hat{G}$ and $\hat{G}^{(u)}$ are obtained by glueing the zero section $\mathbb{C}^{n-1} \times\{0\}$ to $G$ and $G^{(u)}$ respectively.

One may show that $G=\Phi(S) \cong S /\left(\Gamma \cap\left[U_{b}, U_{b}\right]\right)$. Hence there is a group homomorphism $\varphi: \Gamma \cap U_{b} \rightarrow \operatorname{Aut}(G)$ such that $\Phi \circ \nu=\varphi(\nu) \circ \Psi$ for any $\Gamma \cap U_{b}$. This gives rise to the identifications $\left.S /\left(\Gamma \cap U_{b}\right) \cong G / \varphi\left(\Gamma \cap U_{b}\right)\right)$ and $G^{(u)} \cong S^{(u)} /\left(\Gamma \cap\left[U_{b}, U_{b}\right]\right)$.

The boundary divisor $T_{b}$ corresponding to the cusp $b$ is actually the compact complex torus $\left(\mathbb{C}^{n-1} \times\{0\}\right) / \Lambda_{b}$ for some lattice of translations $\Lambda_{b}$. Moreover,
$$\Omega_{b}^{(u)}:=\hat{G}^{(u)} / \varphi\left(\Gamma \cap U_{b}\right) \supset G^{(u)} / \varphi\left(\Gamma \cap U_{b}\right)=\Omega_{b}^{(u)}-T_{b}$$
and $\Omega_{b}^{(u)}$ contains $T_{b}$. We have a natural open embedding
$$\Omega_{b}^{(u)}-T_{b} \hookrightarrow X=S / \Gamma .$$
for $u$ sufficiently large.
Definition 2.1. We call the smallest $u_{b}>0$ so that $\Omega_{b}^{\left(u_{b}\right)}-T_{b} \hookrightarrow X$ is an open embedding the canonical height of $b$. The Euclidean radius $r_{b}=e^{-\frac{2 \pi}{\tau} u_{b}}$ of the disk bundle $\Omega_{b}^{\left(u_{b}\right)} \rightarrow T_{b}$ would be called the canonical radius of $b$.

For any large enough $u>0$, we may identify $\Omega^{(u)}$ with a tubular neighbourhood of the zero section of a negative holomorphic line bundle $L \rightarrow T_{b}$, whose construction goes as follows. Consider the trivial line bundle
$$\mathbb{C}^{n-1} \times \mathbb{C} \rightarrow \mathbb{C}^{n-1}$$
given by the coordinate projection. For each $w=\left(w^{\prime}, w_{n}\right) \in \mathbb{C}^{n-1} \times \mathbb{C}$, we define a Hermitian metric
$$\mu(w, w):=e^{\frac{4 \pi}{\tau}\left|w^{\prime}\right|^{2}} \cdot\left|w_{n}\right|^{2} .$$

Then
$$\Theta\left(\mathbb{C}^{n-1} \times \mathbb{C}, \mu\right)=-\sqrt{-1} \partial \bar{\partial} \log \mu=-\frac{4 \pi}{\tau} \sqrt{-1} \partial \bar{\partial}\left|w^{\prime}\right|^{2}<0 .$$
We may write
$$\hat{G}^{(u)}=\left\{w \in \mathbb{C}^{n} \left\lvert\, \mu(w, w)<e^{\frac{-4 \pi}{\tau} u}\right.\right\} .$$
So $\hat{G}^{(u)}$ is a level set under the metric $\mu$. Restrict the trivial line bundle $\mathbb{C}^{n-1} \times \mathbb{C} \rightarrow \mathbb{C}^{n-1}$ to $\hat{G}^{(u)}$ and take quotients, we obtain a line bundle $L \rightarrow T_{b}$ with the induced Hermitian metric $\bar{\mu}$ of negative curvature (hence showing that $T_{b}$ is an abelian variety). The tubular neighbourhood $\Omega_{b}^{(u)}=$ $\hat{G}^{(u)} / \varphi\left(\Gamma \cap U_{b}\right)$ is just the set of vectors on $L$ with $\bar{\mu}$-length $<e^{\frac{-2 \pi}{\tau} u}$. Under the metric $\bar{\mu}$, we may view $\Omega_{b}^{(u)}$ as the total space of a disk bundle with each fibre isometric to the disk $D_{r}$ of radius $0<r=e^{\frac{-2 \pi}{\tau} u}<1$ over $T_{b}$. Then $\Omega_{b}^{(u)}-T_{b}$ is a family of puncture disks.

We summarise some important features of the Mumford compactification as follows:

Theorem 2.2 (cf. Mok [12]). Let $X=\mathbb{B}^{n} / \Gamma$ be a noncompact finite volume quotient by a torsion-free lattice.
\begin{itemize}
\item[1.] Set theoretically, the Mumford compactification is a disjoint union
$$\bar{X}=X \coprod\left(\coprod_{b} T_{b}\right),$$
where $T_{b}$ is an abelian variety and the disjoint union $\coprod_{b} T_{b}$ is taken over the finitely many cusps of $\Gamma$.
\item[2.] Each $T_{b}$ can be blown-down to a cusp b, so that the image of the blowndown of $\bar{X}$ is a normal projective variety $X^{\prime}$, which is the Satake-Baily-Borel compactification of $X$.
\item[3.] For each $T_{b}$, it admits a system of fundamental neighbourhoods $\left\{\Omega_{b}^{(u)}\right\}_{u \geq u_{b}}$ in $\bar{X}$. For some large enough $u_{0} \geq u_{b}$ (for every cusp b), the fundamental neighbourhoods of two different $T_{b}$ 's can be taken to be disjoint. As a complex manifold, we have
$$\bar{X}=X \coprod\left(\coprod_{b} \Omega_{b}^{(u)}\right) / \sim, \quad \forall u \geq u_{0},$$
where ~ identifies the same point that occurs in both $X$ and $\Omega_{b}^{(u)}$.
\end{itemize}
\begin{itemize}
\item[4.] Each fundamental neighbourhood $\Omega_{b}^{(u)}$ is a level set of a norm induced by a Hermitian metric $\bar{\mu}$ of a negative line bundle $L$ over $T_{b}$. One may identify $\Omega_{b}^{(u)}$ as an open subset of the total space of the line bundle $L$, which is then identified to the normal bundle $\mathcal{N}_{T_{b} \mid \bar{X}}$ of $T_{b}$ in $\bar{X}$.
\item[5.] Each $\Omega_{b}^{(u)} \rightarrow T_{b}$ has a structure of disk bundle. Under the norm $\|\cdot\|$ induced by $\bar{\mu}$, each disk is of radius $r=e^{-\frac{2 \pi}{\tau} u}$, where $\tau$ is the generator of $\Gamma \cap\left[U_{b}, U_{b}\right]$ (where $U_{b}=\operatorname{rad} P_{b}$ is the unipotent radical of $P_{b}$ and $P_{b} \subset \operatorname{Aut}\left(\mathbb{B}^{n}\right)$ is the isotropy subgroup of $b$ ).
\end{itemize}

\section*{3 Asymptotic Behaviour of Canonical Metric}

\subsection*{3.1 The Bergman Metric on $\mathbb{B}^{n}$}

The normalized Bergman metric $g=\left(g_{i \bar{j}}\right)$ on $\mathbb{B}^{n}$ is a Kähler-Einstein metric with the Kähler form
$$\begin{aligned}
\omega & =\sqrt{-1} \partial \bar{\partial}\left(-\log \left(1-|z|^{2}\right)\right) \\
& =\frac{\sqrt{-1}}{\left(1-|z|^{2}\right)^{2}} \sum_{i, j=1}^{n}\left[\left(1-|z|^{2}\right) \delta_{i j}+\bar{z}_{i} z_{j}\right] d z_{i} \wedge d \bar{z}_{j}
\end{aligned}$$
which is of constant holomorphic sectional curvature -2. To understand the asymptotic behaviour of $g$ as $z \rightarrow \partial \mathbb{B}^{n}$, by applying automorphisms, one may consider without loss of generality the points $z=(t, 0, \ldots, 0)$, where $0<t<1$. We immediate see by direct calculation that:

Lemma 3.1 (cf. Lemma 5, Mok [12]). Let $g=\left(g_{i \bar{j}}\right)$ be the normalized Bergman metric on $\mathbb{B}^{n}$. Then
$$g_{i \bar{j}} \sim\left\{\begin{array}{lc}
\frac{1}{\delta^{2}}, & i=j=1 \\
\frac{1}{\delta}, & i=j \geq 2 \\
0, & \text { otherwise }
\end{array}\right.$$
as $t \rightarrow 1$, i.e., $\delta(t)=1-t \rightarrow 0$.

\subsection*{3.2 Canonical Metric on $X$ Near Infinity}

We now focus on points of $X$ which lie in a cusp neighbourhood $\Omega_{b}^{(u)} \supset T_{b}$. Let $z_{1}, \ldots, z_{n}$ denote the coordinates of the upper half space presentation $S$ of $\mathbb{B}^{n}$ with Kähler form
$$\omega_{S}=\sqrt{-1} \partial \bar{\partial}\left(-\log \left(\operatorname{Im} z_{n}-\left|z^{\prime}\right|^{2}\right)\right) .$$

Fix any $u \geq u_{b}$, where $u_{b}$ is the canonical height of the cusp $b \in \partial \mathbb{B}^{n}$. Let $w_{1}, \ldots, w_{n}$ to be the local coordinates in $\Omega_{b}^{(u)}=\hat{G}^{(u)} / \varphi\left(\Gamma \cap U_{b}\right)$ and the divisor $T_{b}$ be defined by $\left\{w_{n}=0\right\}$. We may view $\left(w_{1}, \ldots, w_{n}\right) \in \hat{G}^{(u)}$. At a point $\left(w_{1}, \ldots, w_{n}\right)=\left(w^{\prime}, w_{n}\right) \in \hat{G}^{(u)}$, we have
$$w_{1}=z_{1}, \ldots, w_{n-1}=z_{n-1}, w_{n}=e^{\frac{2 \pi i}{\tau} \cdot z_{n}},$$
where $\tau>0$ corresponds to the generator of some real one-parameter group. Thus
$$d w_{1}=d z_{1}, \ldots, d w_{n-1}=d z_{n-1}, \frac{d w_{n}}{w_{n}}=\frac{2 \pi \sqrt{-1}}{\tau} d z_{n} .$$
Write $\|\cdot\|$ as the norm on $\Omega_{b}^{(u)}=\hat{G}^{(u)} / \varphi\left(\Gamma \cap U_{b}\right)$ given by the metric $\bar{\mu}$ (induced from the Hermitian metric of $L \rightarrow T_{b}$ ):
$$\|w\|:=e^{\frac{2 \pi}{\tau}\left|w^{\prime}\right|^{2}} \cdot\left|w_{n}\right| .$$
We have
$$\log \|w\|=\frac{2 \pi}{\tau}\left|w^{\prime}\right|^{2}+\log \left|w_{n}\right|=\frac{2 \pi}{\tau}\left(\left|z^{\prime}\right|^{2}-\operatorname{Im} z_{n}\right) .$$
Then
$$\begin{aligned}
\omega_{\Omega_{b}^{(u)}} & =\sqrt{-1} \partial \bar{\partial}(-\log (-\log \|w\|) \\
& =\frac{\sqrt{-1} \partial \bar{\partial} \log \|w\|}{-\log \|w\|}+\frac{\sqrt{-1} \partial(-\log \|w\|) \wedge \bar{\partial}(-\log \|w\|)}{(-\log \|w\|)^{2}} \\
& =\frac{1+\log \|w\|}{\|w\|^{2}(-\log \|w\|)^{2}} \sqrt{-1} \partial\|w\| \wedge \bar{\partial}\|w\|+\frac{1}{\|w\|(-\log \|w\|)} \sqrt{-1} \partial \bar{\partial}\|w\|
\end{aligned}$$
We may express the Hessian $\sqrt{-1} \partial \bar{\partial}\|w\|$ in terms of gradient square $\sqrt{-1} \partial\|w\| \wedge$ $\bar{\partial}\|w\|$ by noting that
$$\partial \bar{\partial}\|w\|=\frac{2 \pi}{\tau}\|w\| \partial \bar{\partial}\left|w^{\prime}\right|^{2}+\frac{\partial\|w\| \wedge \bar{\partial}\|w\|}{\|w\|} .$$
Thus
$$\omega_{\Omega_{b}^{(u)}}=\frac{1}{\|w\|^{2}(-\log \|w\|)^{2}} \sqrt{-1} \partial\|w\| \wedge \bar{\partial}\|w\|+\frac{2 \pi}{\tau} \frac{1}{(-\log \|w\|)} \sqrt{-1} \partial \bar{\partial}\left|w^{\prime}\right|^{2} .$$
For any $0<\|w\| \leq 1$, if follows from elementary calculus that $0 \leq 1-\|w\| \leq$ $-\log \|w\|$. Thus
$$\frac{1}{(-\log \|w\|)^{2}} \leq \frac{1}{(1-\|w\|)^{2}} .$$

On the other hand, observe that
$$\left(\frac{1}{\|w\|^{2}} \partial\|w\| \wedge \bar{\partial}\|w\|\right)^{2}=0, \quad\left(\partial \bar{\partial}\left|w^{\prime}\right|^{2}\right)^{n}=0 .$$
We have
$$\omega_{\Omega_{b}^{(u)}}^{n}=\left(\frac{2 \pi}{\tau}\right)^{n-1} \frac{1}{\|w\|^{2}(-\log \|w\|)^{n+1}}(\sqrt{-1})^{n} \partial\|w\| \wedge \bar{\partial}\|w\| \wedge\left(\partial \bar{\partial}\left|w^{\prime}\right|^{2}\right)^{n-1} .$$
Hence
Lemma 3.2 (cf. Proposition 1, Mok [12]). Let $g_{X}=\left\{g_{\alpha \bar{\beta}}\right\}$ be the canonical Kähler-Einstein metric on $X$ that is induced by the normalized Bergman metric on $\mathbb{B}^{n}$. Let $\Omega_{b} \subset\{0 \leq\|w\| \leq 1\}$ be a fundamental neighbourhood of the infinity $T_{b}=\left\{w_{n}=0\right\}$. Let $\delta(w):=1-\|w\|$ be the distance from a point $w \in \Omega_{b}$ to $T_{b}$.
\begin{itemize}
\item[1.] When $\|w\| \rightarrow 0$,
$$\frac{C_{1}}{\|w\|^{2}(-\log \|w\|)^{n+1}} d V \leq d V_{g_{X}} \leq \frac{C_{2}}{\|w\|^{2}(-\log \|w\|)^{n+1}} d V,$$
where $C_{1}, C_{2}>0$ are constants and $d V=\sqrt{-1} \partial \bar{\partial}|w|^{2}$ is the local Euclidean volume form near infinity.
\item[2.] When $\|w\| \rightarrow 1, g_{\alpha \bar{\beta}}$ is of growth $1 / \delta^{2}$.
\end{itemize}

Remark: The same two sided asymptotic behaviour of $g$ occurs in the Poincaré metric of the punctured complex unit disk of dimension 1, where the norm $\|w\|$ is simply the Euclidean distance.

For the dual metric $g^{*}$ on the cotangent bundle $T_{X}^{*}$, note that $g^{*}=$ $\left(\left(g_{X}\right)^{-1}\right)^{t}=\frac{1}{\operatorname{det} g_{X}}\left(\operatorname{adj} g_{X}\right)^{t}$. The norm $\|\cdot\|_{g^{*}}$ for a holomorphic section $s=s_{1} d w_{1}+\cdots+s_{n} d w_{n}$ of $\left.T_{X}^{*}\right|_{\Omega_{b}^{(N)}}$ induced by $g^{*}$ has the asymptotic behaviour given by $\frac{1}{\operatorname{det} g_{X}}$ when $\|w\| \rightarrow 0$, i.e.,
$$C_{1}\left|s_{n}\right|^{2}\|w\|^{2}(-\log \|w\|)^{n+1} \leq\|s\|_{g^{*}}^{2} \leq C_{2}\left|s_{n}\right|^{2}\|w\|^{2}(-\log \|w\|)^{n+1}$$
for some constant $C_{1}, C_{2}>0$ when $\|w\|$ is sufficiently close to 0 . Similarly, the norm of the symmetric product $\odot^{k} s$ has the asymptotic behaviour
$$C_{1}^{\prime}\left|s_{n}\right|^{2 k}\|w\|^{2 k}(-\log \|w\|)^{k(n+1)} \leq\left\|\odot^{k} s\right\|_{\odot^{k} g^{*}}^{2}=\|s\|_{g^{*}}^{2 k} \leq C_{2}^{\prime}\left|s_{n}\right|^{2 k}\|w\|^{2 k}(-\log \|w\|)^{k(n+1)},$$
for some constant $C_{1}^{\prime}, C_{2}^{\prime}>0$ when $\|w\|$ is sufficiently close to 0 .

\subsection*{3.3 Uniform Estimates of Curvature}

Consider the holomorphic tangent bundle $T_{\mathbb{B}^{n}} \rightarrow \mathbb{B}^{n}$. Since the Bergman metric $g=\left(g_{i \bar{j}}\right)$ on $\mathbb{B}^{n}$ is Kähler, the Hermitian connection $D$ with respect to $g$ agrees with the connection. The curvature of $D$ is the tensor
$$\Theta\left(T_{\mathbb{B}^{n}}, g\right):=\sqrt{-1} \Theta_{\alpha \bar{\beta} i \bar{j}} e^{\alpha} \otimes \bar{e}_{\beta} d w^{i} \wedge d \bar{w}^{j}$$
for any local coordinates $\left(w^{i}\right)$ and local holomorphic basis $\left(e_{\beta}\right)$ of $T_{\mathbb{B}^{n}}$ and dual basis $\left(e^{\alpha}\right)$ of $T_{\mathbb{B}^{n}}^{*}$. Explicitly,
$$\Theta_{\alpha \bar{\beta} i \bar{j}}=-\partial_{i} \partial_{\bar{j}} g_{\alpha \bar{\beta}}+g^{\mu \bar{\nu}} \partial_{i} g_{\alpha \bar{\nu}} \partial_{\bar{j}} g_{\mu \bar{\beta}},$$
where $\left(g^{\gamma \bar{\delta}}\right)$ is the conjugate inverse of $g=\left(g_{\alpha \bar{\beta}}\right)$. Note that $\Theta$ is independent of the choice of local holomorphic coordinates $\left(w^{i}\right)$. The Euclidean coordinates at $0 \in \mathbb{B}^{n}$ are actually complex geodesic coordinates for the Bergman metric on $\mathbb{B}^{n}$. If we normalize the Kähler form of the Bergman metric of $\mathbb{B}^{n}$, which is Kähler-Einstein, so that it has constant holomorphic sectional curvature -2, then it follows from homogeneity and the calculation at the point $0 \in \mathbb{B}^{n}$ that

Lemma 3.3 (cf. [11]). For the normalized Bergman metric on $\mathbb{B}^{n}$ with constant holomorphic sectional curvature -2, we have:
$$\begin{gathered}
-2 \leq \Theta_{\alpha \bar{\alpha} \beta \bar{\beta}} \leq-1, \\
\operatorname{Ric}_{i \bar{j}}=-(n+1) \delta_{i j} .
\end{gathered}$$

Denote by $\mathbb{P} T_{X}$ the projectivized tangent bundle of $X$ obtained by fiberwise projectivization of the holomorphic tangent bundle $\left(T_{X}, g_{X}\right) \rightarrow X{ }^{2}$. One may associate the tangent bundle $\left(T_{X}, g_{X}\right)$ to the tautological line bundle $\left(\mathcal{O}_{\mathbb{P} T_{X}}(-1), \hat{g}\right) \rightarrow \mathbb{P} T_{X}$ by fibrewise Hopf blow-up process. Each point $(x,[u]) \in \mathbb{P} T_{X}$ is described by the $x$-coordinates corresponding to the direction of base manifold and $[u]$-coordinates corresponding to the direction of the fibre $\cong \mathbb{P}^{n-1}$. The metric $\hat{g}$ on each fibre is negative definite and is actually induced from the Fubini-Study metric on $\mathbb{P}^{n-1}$. We will normalize the Fubini-Study metric to be of Ricci constant $n$. Equip $\mathbb{P} T_{X}$ with the Kähler form
$$\omega_{\mathbb{P} T_{X}}=-c_{1}\left(\mathcal{O}_{\mathbb{P} T_{X}}(-1), \hat{g}\right)=\sqrt{-1} \partial \bar{\partial} \log g_{0} .$$

\footnotetext{
${ }^{2}$ Note that some author may denote $\mathbb{P} T_{X}$ by the projectivization of the dual bundle $T_{X}^{*}$ instead of $T_{X}$.
}
where $c_{1}$ denotes the first Chern class. It follows that $\omega_{\mathbb{P} T_{X}}$ is positive when restricted respectively to the fibre direction and also the base direction. It is easily seen that

Lemma 3.4. The Ricci curvature of $\left(\mathbb{P} T_{X}, \omega_{\mathbb{P} T_{X}}\right)$ satisfies
$$-(n+1) \leq \operatorname{Ric}_{i \bar{j}} \leq n .$$

Consider the point $[u] \in \mathbb{P}^{n-1}$ in the standard chart $U_{n}=\left\{\left[v^{1}, \ldots, v^{n}\right] \in\right.$ $\left.\mathbb{P}^{n-1} \mid v^{n} \neq 0\right\}$. In a neighbourhood of $(\xi,[u])$ in $\mathbb{P} T_{X}$, we may use the local coordinates $(\xi,[u])=\left(\xi^{1}, \ldots, \xi^{n}, u^{1}, \cdots u^{n-1}\right)$ where $u^{i}=v^{i} / v^{n}$. For the line bundle $\mathcal{O}_{\mathbb{P} T_{X}}(-1) \rightarrow \mathbb{P} T_{X}$, the holomorphic fibre coordinate is given by $\lambda=v^{r}$ in a neighbourhood of $[u]$.

If $e$ is a holomorphic basis of $\mathcal{O}_{\mathbb{P} T_{X}}(-1)$ and write $\hat{g}=g_{0} e^{*} \otimes e$, then we have
$$g_{0}=\|e\|^{2}=g_{\alpha \bar{\beta}} u^{\alpha} \bar{u}^{\beta}=\sum_{\alpha, \beta=1}^{n-1} g_{\alpha \bar{\beta}}(\xi) u^{\alpha} \bar{u}^{\beta}+2 \operatorname{Re} \sum_{\alpha=1}^{n-1} g_{\alpha \bar{n}}(\xi) u^{\alpha}+g_{n \bar{n}}(\xi),$$
since $u^{n}=1$. The curvature of $\mathcal{O}_{\mathbb{P} T_{X}}(-1)$ is given by
$$\Theta\left(\mathcal{O}_{\mathbb{P} T_{X}}(-1), \hat{g}\right)=c_{1}\left(\mathcal{O}_{\mathbb{P} T_{X}}(-1), \hat{g}\right)=-\sqrt{-1} \partial \bar{\partial} \log g_{0} .$$
Since $X$ and $\mathbb{P} T_{X}$ are homogeneous, a uniform estimate of the curvature can be obtained by the computation at one point.

Assume the fibre coordinate $\lambda$ above to be a special holomorphic fibre coordinate for $\mathcal{O}_{\mathbb{P} T_{X}}(-1)$ adapted to $\hat{g}$ at $(x,[u])$, which has coordinates $\left(\xi^{1}, \ldots, \xi^{n}, 0, \ldots, 0\right)$, it is obtained by direct computation (cf. [11]) that for any $\ell \in \mathbb{N}$,
$$\Theta\left(\mathcal{O}_{\mathbb{P} T_{X}}(\ell),\left(\hat{g}^{*}\right)^{\ell}\right)(x,[u])=\ell \sqrt{-1}\left(\sum_{\alpha=1}^{n-1} d u^{\alpha} \wedge d \bar{u}^{\alpha}-\sum_{i, j=1}^{n} \Theta_{n \bar{n} i} d \xi^{i} \wedge d \bar{\xi}^{j}\right) .$$
It also implies that the hyperplane section line bundle $\left(\mathcal{O}_{\mathbb{P} T_{X}}(1), \hat{g}^{*}\right) \rightarrow \mathbb{P} T_{X}$ is of positive curvature.

\subsection*{3.3.1 Asymptotic Behaviour of Curvature}

To obtain our Main Theorem (Theorem 1.2), however, it is not enough to use the uniform estimates coming from the calculation under special coordinates
at one point and homogeneity. We will need to consider the asymptotic behaviour of the canonical metric induced by the normalized Bergman metric. Thus it is necessary to use the full calculation of the curvature. First note that we may write
$$g=\left(g_{\alpha \bar{\beta}}\right)=\frac{1}{(-\log \|w\|)^{2}}\left(h_{\alpha \bar{\beta}}\right),$$
where
$$\left(h_{\alpha \bar{\beta}}\right)=\left(\begin{array}{cc}
\left(\frac{2 \pi}{\tau}(-\log \|w\|) \delta_{\alpha \beta}-\left(\frac{2 \pi}{\tau}\right)^{2} w_{\alpha} \bar{w}_{\beta}\right) & \frac{2 \pi}{\tau} \frac{\bar{w}_{\beta}}{\bar{w}_{n}} \\
\frac{2 \pi}{\tau} \frac{w_{\alpha}}{w_{n}} & \frac{1}{\left|w_{n}\right|^{2}}
\end{array}\right), \quad 1 \leq \alpha, \beta \leq n-1 .$$
When $\|w\| \rightarrow 1$, each component $g_{\alpha \bar{\beta}}$ is of growth $1 / \delta^{2}$ where
$$\delta(w):=1-\|w\|$$
is the distance from to the boundary $\{\|w\|=1\}$. Then
$$\begin{aligned}
\Theta\left(\mathcal{O}_{\mathbb{P} T_{X}}(-1), \hat{g}\right)= & c_{1}\left(\mathcal{O}_{\mathbb{P} T_{X}}(-1), \hat{g}\right) \\
= & -\sqrt{-1} \partial \bar{\partial} \log g_{0} \\
= & -\frac{\sqrt{-1}}{g_{0}^{2}}\left[\left(g_{0} \partial_{i} \partial_{\bar{j}} g_{0}-\partial_{i} g_{0} \partial_{\bar{j}} g_{0}\right) d \xi^{i} \wedge d \bar{\xi}^{j}+\left(g_{0} \partial_{i} \partial_{\bar{\beta}} g_{0}-\partial_{i} g_{0} \partial_{\bar{\beta}} g_{0}\right) d \xi^{i} \wedge d \bar{u}^{\beta}\right. \\
& \left.+\left(g_{0} \partial_{i} \partial_{\bar{\alpha}} g_{0}-\partial_{\alpha} g_{0} \partial_{\bar{j}} g_{0}\right) d u^{\alpha} \wedge d \bar{\xi}^{j}+\left(\partial_{\alpha} \partial_{\bar{\beta}} g_{0}-\partial_{\alpha} g_{0} \partial_{\bar{\beta}} g_{0}\right) d u^{\alpha} \wedge d \bar{u}^{\beta}\right],
\end{aligned}$$
where $1 \leq i, j, \alpha, \beta \leq n$. The numerator of the R.H.S. of Equation (9) is $-\sqrt{-1}$ times
$$\begin{aligned}
& g_{0} \partial \bar{\partial} g_{0}-\partial g_{0} \wedge \bar{\partial} g_{0} \\
= & u^{\alpha} \bar{u}^{\beta} u^{\gamma} \bar{u}^{\delta}\left(g_{\gamma \bar{\delta}} \partial_{i} \partial_{\bar{j}} g_{\alpha \bar{\beta}}-\partial_{i} g_{\alpha \bar{\beta}} \partial_{\bar{j}} g_{\gamma \bar{\delta}}\right) d \xi^{i} \wedge d \bar{\xi}^{j}+u^{\alpha} u^{\gamma} \bar{u}^{\delta}\left(\partial_{\bar{j}} g_{\alpha \bar{\beta}}-\partial_{\bar{j}} g_{\gamma \bar{\delta}}\right) d u^{\alpha} \wedge d \bar{\xi}^{j} \\
& +\bar{u}^{\beta} u^{\gamma} \bar{u}^{\delta}\left(\partial_{i} g_{\alpha \bar{\beta}}-\partial_{i} g_{\alpha \bar{\delta}}\right) d \xi^{i} \wedge d \bar{u}^{\beta}+u^{\gamma} \bar{u}^{\delta}\left(g_{\alpha \bar{\beta}} g_{\gamma \bar{\delta}}-g_{\alpha \bar{\delta}} g_{\gamma \bar{\beta}}\right) d u^{\alpha} \wedge d \bar{u}^{\beta},
\end{aligned}$$
and the denominator is
$$g_{0}^{2}=g_{\alpha \bar{\beta}} g_{\gamma \bar{\delta}} u^{\alpha} \bar{u}^{\beta} u^{\gamma} \bar{u}^{\delta},$$
where $1 \leq \alpha, \beta, \gamma, \delta, i, j \leq n$. Since both the numerator and the denominator of the R.H.S. of the Equation (9) are polynomial of degree 4 in $u^{i}, \bar{u}^{j}$ 's and all possible combinations of the $u^{i}, \bar{u}^{j}$ 's in the monomials appear once, we know that

Lemma 3.5. Each component $\Theta\left(\mathcal{O}_{\mathbb{P} T_{X}}(-1), \hat{g}\right)_{i \bar{j} \alpha \bar{\beta}}$ is bounded as $\left|\left(u^{1}, \ldots, u^{n-1}, 1\right)\right| \rightarrow$ $\infty$ in any $u$-directions (i.e. the fibre directions).

Remark: For the purpose of studying asymptotic behaviour of the curvatures in some inequalities, it suffices to focus on the base directions.

We will make use of two kinds of asymptotic behaviours of $\Theta\left(\mathcal{O}_{\mathbb{P} T_{X}}(-1), \hat{g}\right)$. Let
$$\Omega:=\coprod_{b} \Omega_{b}$$
be a disjoint union of the canonical neighbourhoods of each component $T_{b}$ of the infinity , where $T_{b}$ corresponds to the cusps $b$ of $\Gamma$. Thus each $\Omega_{b}$ has a disk bundle structure over $T_{b}$ with radius less or equal than the canonical radius of $b$. We are going to view $\Omega-\coprod_{b} T_{b} \subset \mathbb{P} T_{X}$. We will also let
$$\Omega^{\prime}:=\mathbb{P} T_{X}-\Omega$$
to be the interior relatively compact part.

\section*{Curvature in the Interior}

Suppose $p \in \Omega^{\prime}$. Then $p$ lifts to a point in a fundamental domain $\mathcal{F} \subset \mathbb{B}^{n}$ of $\Gamma$. We may assume the origin $0 \in \mathcal{F}$. These is a metric ball neighbourhood of $p$ in $X$ of maximum radius measured with respect to the canonical metric $g_{X}$. The radius of the ball neighbourhood depends on the injectivity radius at the point $p$ with respect to $g_{X}$. Thus there exists $\delta>0$, which depends on the injectivity radius at $p$ with respect to $g_{X}$, such that $p \in B(0,1-\delta) \subset \mathcal{F} \subset \mathbb{B}^{n}$, where $B(z, r)$ denotes the Euclidean ball centred at $z$ with radius $r$. Now we have
$$-\log \|w\|=\frac{2 \pi}{\tau}\left(\operatorname{Im}\left(\xi_{n}\right)-\left|\xi^{\prime}\right|^{2}\right)=\frac{2 \pi}{\tau} \frac{1-|z|^{2}}{\left|1-z_{n}\right|^{2}}=\frac{2 \pi}{\tau} \frac{(1+|z|)(1-|z|)}{\left|1-z_{n}\right|^{2}}=: f(z) \delta(z),$$
where $\delta(z):=1-|z|$ and $f(z)$ is non-vanishing. In view of Equation (8), it then follows that
$$\partial_{i} g_{\alpha \bar{\beta}}=\frac{1}{\delta(z)^{3}} \psi_{i, \alpha \bar{\beta}}, \quad \partial_{\bar{j}} g_{\alpha \bar{\beta}}=\frac{1}{\delta(z)^{3}} \psi_{\bar{j}, \alpha \bar{\beta}}, \quad \partial_{i} \partial_{\bar{j}} g_{\alpha \bar{\beta}}=\frac{1}{\delta(z)^{4}} \phi_{i \bar{j}, \alpha \bar{\beta}},$$
where $\psi_{i, \alpha \bar{\beta}}, \psi_{\bar{j}, \alpha \bar{\beta}}, \phi_{i \bar{j}, \alpha \bar{\beta}}$ are functions that are bounded as $|z| \rightarrow 1$. By the explicit Equation (10) and (11), it follows that the growth of each component of the curvature is
$$\Theta\left(\mathcal{O}_{\mathbb{P} T_{X}}(-1), \hat{g}\right)_{i \bar{j} \alpha \bar{\beta}} \sim 1 / \delta^{2}, \quad \text { when }|z| \rightarrow 1,$$
where $\delta(z)=1-|z|$.

\section*{Curvature Near Infinity}

Suppose $p \in \Omega_{b} \subset \Omega$ is a point in some fundamental cusp neighbourhood $\Omega_{b}=\left\{\|w\| \leq r_{b}\right\}$ (where $0<r_{b}<1$ ) of a component $T_{b}$ of the boundary divisor of the Mumford compactification $\bar{X}$. By similar calculations as in the above, we have the asymptotic behaviour
$$\Theta\left(\mathcal{O}_{\mathbb{P} T_{X}}(-1), \hat{g}\right)_{i \bar{j} \alpha \bar{\beta}} \sim 1 / \delta^{2}, \quad \text { when }\|w\| \rightarrow 1,$$
where $\delta(w)=1-\|w\|$. Geometrically, this situation corresponds to the approaching from cups neighbourhood to the interior. It is similar to the one dimensional analogue, i.e., the Poincaré metric for punctured unit disk. The analogous situation is the approaching of an interior point to the boundary $\{|z|=1\}$.

We record the asymptotic behaviours of the curvature as follows:
Lemma 3.6. Let $\hat{g}$ be the Hermitian metric on $\mathbb{P} T_{X}$ induced from the Kähler metric on $\mathbb{P} T_{X}$ (which is induced from the canonical Kähler-Einstein metric on the base $X=\mathbb{B}^{n} / \Gamma$ and the Fubini-Study metric on each fibre $\mathbb{P}^{n-1}$ ). Let $\Omega:=\coprod_{b} \Omega_{b}$ and $\Omega^{\prime}:=\mathbb{P} T_{X}-\Omega$.
\begin{itemize}
\item[1.] Suppose $p \in \Omega^{\prime}$ is lifted to a point $z \in \mathbb{B}^{n}$. Then
$$\Theta\left(\mathcal{O}_{\mathbb{P} T_{X}}(-1), \hat{g}\right)_{i \bar{j} \alpha \bar{\beta}} \sim 1 / \delta^{2}, \quad \text { when }|z| \rightarrow 1,$$
where $\delta(z)=1-|z|$.
\item[2.] Suppose $w \in \Omega$ is contained in a fundamental neighbourhood $\Omega_{b} \subset$ $\{0 \leq\|w\| \leq 1\}$. Then
$$\Theta\left(\mathcal{O}_{\mathbb{P} T_{X}}(-1), \hat{g}\right)_{i \bar{j} \alpha \bar{\beta}} \sim 1 / \delta^{2}, \quad \text { when }\|w\| \rightarrow 1,$$
where $\delta(w)=1-\|w\|$.
\end{itemize}

\section*{4 The Construction of Symmetric Differentials Vanishing at Infinity}

In this section, we will construct symmetric differentials on $\bar{X}$ which vanishes at infinity $D=\bar{X}-X$. The construction is done by methods of $L^{2}$-estimates, which relies on the existence theorem:

Theorem 4.1 (Andreotti-Vesentini [2] and Hörmander [8]). Let $(M, g)$ be a complete Kähler manifold with Kähler form $\omega$ and Ricci form Ric $(\omega)$. Let $(\mathcal{L}, h) \rightarrow M$ be a Hermitian holomorphic line bundle with curvature form $\Theta(\mathcal{L}, h)$. Suppose $\varphi$ is a smooth function on $M$ and $c$ is a positive continuous function on $X$ such that
$$\Theta(\mathcal{L}, h)+\operatorname{Ric}(\omega)+\sqrt{-1} \partial \bar{\partial} \varphi \geq c \omega$$
everywhere on $M$. Let $f$ be a $\bar{\partial}$-closed square integrable $\mathcal{L}$-valued ( 0,1 )-form on $M$ such that $\int_{M} \frac{\|f\|_{g}^{2}}{c} d V_{g}<\infty$. Then there exists a section $u$ of $\mathcal{L} \rightarrow M$ solving the inhomogeneous problem $\bar{\partial} u=f$ and also satisfying the estimate
$$\int_{M}\|u\|_{g}^{2} e^{-\varphi} d V_{g} \leq \int_{M} \frac{\|f\|_{g}^{2}}{c} e^{-\varphi} d V_{g}<\infty .$$
Furthermore, $u$ is smooth whenever $f$ is.
Remark: When the weight function $\varphi$ is singular, the above existence theorem also holds provided that $\varphi$ can be approximated by a monotonically decreasing sequence $\left\{\varphi_{\epsilon}\right\}$ where each of $\varphi_{\epsilon}$ is smooth and plurisubharmonic. We will consider weight function of the form $\varphi \sim \log |z|^{2}$. The approximation can then be taken as $\varphi_{\epsilon} \sim \log \left(|z|^{2}+\epsilon\right)$ for $\epsilon \rightarrow 0$.

We will carry on the construction by first assuming the basic estimates in Theorem 4.1, leaving its justification to next section.

\subsection*{4.1 The Construction Assuming the Basic Estimates}

Let $U \subset X \subset \mathbb{P} T_{X}$ be an open neighbourhood of the boundary divisor $T_{b}=\left\{w_{n}=0\right\}$ corresponding to a cusp $b$ of $\Gamma$. Let $\ell, n, \gamma$ to be respectively the degree of symmetric power of the cotangent bundle, the dimension of $X=\mathbb{B}^{n} / \Gamma$ and the degree of singularity in the weight function
$$\varphi:=\gamma \chi \log \|w\|^{2},$$
where $\chi$ is a cutoff function near infinity to be specified explicitly later and $\gamma$ is a nonnegative integer.

Assume $\varepsilon>0$ such that on $\mathbb{P} T_{X}$, the basic estimates
$$\Theta\left(\mathcal{O}_{\mathbb{P} T_{X}}(\ell),\left(\hat{g}^{*}\right)^{\ell}\right)+\operatorname{Ric}\left(\omega_{\mathbb{P} T_{X}}\right)+\sqrt{-1} \partial \bar{\partial} \varphi \geq \varepsilon \omega_{\mathbb{P} T_{X}}$$
holds.
Remark: By our technique, we need to require $\ell \geq n+1+\varepsilon$. Suppose
$$(\dagger): \quad \exists \nu \in H^{0}\left(U-T_{b},\left.\mathcal{O}(\ell)\right|_{U-T_{b}}\right)$$
a nowhere zero holomorphic section so that it extends to and vanishes at $T_{b}$ of order exactly $m>0$.

Take a smooth cut-off function $\chi: \mathbb{P} T_{X} \rightarrow[0,1]$ such that for some neighbourhood $U_{1}$ of $\left(\mathbb{P} T_{X}-U\right) \cap X$
$$\chi(p)=\left\{\begin{array}{l}
1, \text { if } p \in U \\
0, \text { if } p \in U_{1} .
\end{array}\right.$$
We get a global smooth section $\eta:=\chi \nu \in \mathcal{C}_{c}^{\infty}\left(\mathbb{P} T_{X}, \mathcal{O}_{\mathbb{P} T_{X}}(\ell)\right)$. Since $\bar{\partial} \eta=$ $\nu \bar{\partial} \chi+\chi \bar{\partial} \nu$. On $U, \chi \equiv 1$ and $\left.\eta\right|_{U}=\nu \in \Gamma\left(U,\left.\mathcal{O}_{\mathbb{P} T_{X}}(\ell)\right|_{U}\right)$, it follows that $\bar{\partial} \eta \equiv 0$. On $U_{1}, \chi \equiv 0$, which also implies that $\bar{\partial} \eta \equiv 0$. Thus $\bar{\partial} \eta$ has compact support $\operatorname{Supp}(\bar{\partial} \eta) \Subset \mathbb{P} T_{X}-\left(U \cup U_{1}\right)$. It follows that
$$\int_{\mathbb{P} T_{X}}\|\bar{\partial} \eta\|^{2} e^{-\varphi} \omega_{\mathbb{P} T_{X}}^{2 n-1}<\infty .$$
Now consider the following inhomogeneous partial differential equation of unknown $u$ on $\mathbb{P} T_{X}$ :
$$\bar{\partial} u=\bar{\partial} \eta .$$
Hence by Theorem 4.1, a solution $u$ to Equation (17) exists and it satisfies the estimates
$$\int_{\mathbb{P} T_{X}}\|u\|^{2} e^{-\varphi} \omega_{\mathbb{P} T_{X}}^{2 n-1} \leq \frac{1}{\varepsilon} \int_{\mathbb{P} T_{X}}\|\bar{\partial} \eta\|^{2} e^{-\varphi} \omega_{\mathbb{P} T_{X}}^{2 n-1}<\infty .$$
Recall that the metric $\left(\hat{g}^{*}\right)^{\ell}$ is induced from the dual metric $\odot^{\ell} g^{*}$ on $S^{\ell}\left(T_{X}^{*}\right)$ and we have an isomorphism of sections $H^{0}\left(\mathbb{P} T_{X}, \mathcal{O}_{\mathbb{P} T_{X}}(\ell)\right) \cong H^{0}\left(X, S^{\ell}\left(T_{X}^{*}\right)\right)$. Thus we may identify $u$ to a section $u_{0} \in H^{0}\left(X, S^{\ell}\left(T_{X}^{*}\right)\right)$ and $\eta$ to $\eta_{0}^{\ell} \in$ $H^{0}\left(X, S^{\ell}\left(T_{X}^{*}\right)\right)$. Then Inequality (18) implies that
$$\int_{X}\left\|u_{0}\right\|_{\odot^{\ell} g^{*}}^{2} e^{-\varphi} d V_{g_{X}}<\infty .$$
Since the asymptotic behaviour of the metric $g_{X}$ when approaching to $T_{b}=$ $\left\{w_{n}=0\right\}$ is donminanted by the $w_{n}$-coordinate, we may write without loss of generality that
$$u_{0}=f\left(d w_{n}\right)^{\odot \ell}, \quad \text { in a small neighbourhood } \Delta^{n}(\varepsilon) \cong \Omega_{0} \subset \Omega_{b}^{(N)} \text { of } T_{b} .$$

Now
$$\begin{aligned}
\infty & >\int_{\Omega_{0}}\left\|u_{0}\right\|_{\odot^{\ell} g^{*}}^{2} e^{-\varphi} d V_{g_{X}} \\
& =\int_{\Omega_{0}}\left\|f\left(d w_{n}\right)^{\odot \ell}\right\|_{\odot^{\ell} g^{*}}^{2} e^{-\varphi} d V_{g_{X}} \\
& \geq \text { const } \cdot \int_{\Delta^{n}(\varepsilon)}|f|^{2} \frac{1}{\|w\|^{2(-\ell+\gamma+1)}}(-\log \|w\|)^{(\ell-1)(n+1)} d V .
\end{aligned}$$
In order to avoid $u_{0}$ to be the trivial solution, we want $f$ to vanish at $\left\{w_{n}=0\right\}$ to order at least $m+1$ for some $m \geq 0$. This is the same as requiring
$$-\ell+\gamma+1 \geq m+1 \Leftrightarrow \gamma \geq \ell+m .$$
Let
$$\sigma:=\eta-u .$$
Then $\bar{\partial} \sigma=\bar{\partial} \eta-\bar{\partial} u \equiv 0$ on $\mathbb{P} T_{X}$, which implies that $\sigma \in H^{0}\left(\mathbb{P} T_{X}, \mathcal{O}_{\mathbb{P} T_{X}}(\ell)\right)$ such that it vanishes at $T_{b}=\left\{w_{n}=0\right\}$ to order $m$.

\subsection*{4.2 The Justification of (†)}

Proposition 4.2. There exists an open neighbourhood $U \subset \bar{X} \subset \mathbb{P} T_{\bar{X}}$ of the boundary divisor $T_{b}=\left\{w_{n}=0\right\}$ corresponding to a cusp $b$ of $\Gamma$ such that there is a nowhere zero holomorphic section
$$\nu \in H^{0}\left(U-T_{b},\left.\mathcal{O}_{\mathbb{P} T_{\bar{X}}}(\ell)\right|_{U-T_{b}}\right)$$
which extends and vanishes to order exactly $\ell m>0$ at $T_{b}$.
Proof. We are going to construct a local holomorphic section
$$\nu \in H^{0}\left(U-T_{b},\left.\mathcal{O}(\ell)\right|_{U-T_{b}}\right) \cong H^{0}\left(U-T_{b},\left.S^{\ell} T_{X}^{*}\right|_{U-T_{b}}\right),$$
which is nowhere zero in $U-T_{b}$, extends to $T_{b}$ and vanishes precisely to order $m>0$ at the infinity $T_{b}$.

Take $T_{b} \subset U=\Omega_{b} \subset \bar{X}$, where $\Omega_{b}$ is a level set of the norm
$$\left\|\left(w^{\prime}, w_{n}\right)\right\|:=e^{\frac{2 \pi}{\tau}\left|w^{\prime}\right|^{2}}\left|w_{n}\right| .$$
The normal bundle
$$\mathcal{N}_{T_{b} \mid \bar{X}} \rightarrow T_{b}$$
is negative under the Hermitian metric $\mu$. By Lefschetz's embedding theorem for abelian variety (cf. for example [4] Theorem 4.5.1), $\mathcal{N}_{T_{b} \mid X}^{-m}$ is very ample for every $m \geq 3$. In fact $\mathcal{N}_{T_{b} \mid \bar{X}}^{-2}$ is already base-point free.

Let $L=\mathcal{N}_{T_{b} \mid \bar{X}}$. Identify $T_{b} \subset L$ as the zero section. Write $T_{b}=\bigcup_{\alpha} U_{\alpha}$ as a union of open covers. We have the local trivialization
$$\left.L\right|_{U_{\alpha}}=U_{\alpha} \times \mathbb{C}$$
Let $\left(z, w_{\alpha}\right) \in U_{\alpha} \times \mathbb{C}$ be the local coordinates and $e_{\alpha}$ be a holomorphic basis of $\left.L\right|_{U_{\alpha}}$. Then the coordinate functions $\left\{w_{\alpha}\right\}$ may be viewed as the sections of $L^{-1}$ and they satisfy
$$w_{\alpha} e_{\alpha}=w_{\beta} e_{\beta}, \quad \text { on }\left.L\right|_{U_{\alpha} \cap U_{\beta}} .$$
Fix $m \geq 1$. Since $L^{-(m+1)} \rightarrow T_{b}$ is base-point free, there is a holomorphic section $s \in H^{0}\left(T_{b}, L^{-(m+1)}\right)$ such that $s(p) \neq 0$ at a particular point $p \in T_{b}$. Hence $s$ is nontrivial and nonvanishing on $T_{b}$. Write
$$s=s_{\alpha} e_{\alpha}^{-(m+1)} .$$
Over $U_{\alpha} \cap U_{\beta}$, we have
$$s_{\alpha} e_{\alpha}^{-(m+1)}=s_{\beta} e_{\beta}^{-(m+1)} .$$
On $\left.L\right|_{U_{\alpha}} \cong U_{\alpha} \times \mathbb{C}$, define
$$\begin{array}{cccc}
f_{\alpha}: & U_{\alpha} \times \mathbb{C} & \rightarrow & \mathbb{C} \\
\left(z, w_{\alpha}\right) & \rightarrow & s_{\alpha}(z) w_{\alpha}^{m+1} .
\end{array}$$
Then $f=\left\{f_{\alpha}\right\}$ is a well-defined holomorphic function on $L$ since on ( $U_{\alpha} \cap$ $\left.U_{\beta}\right) \times \mathbb{C}$,
$$s_{\alpha}(z) w_{\alpha}^{m+1}=s_{\beta} e_{\beta}^{-(m+1)} e_{\alpha}^{m+1} w_{\beta}^{m+1} e_{\beta}^{m+1} e_{\alpha}^{-(m+1)}=s_{\beta}(z) w_{\beta}^{m+1} .$$
View $\Omega_{b} \subset L=\mathcal{N}_{T_{b} \mid \bar{X}}$ as an open subset. By construction, $f$ is nonconstant on $\Omega_{b}-T_{b}$ and vanishes precisely to order $m+1$ on $T_{b}$. On $\left.L\right|_{U_{\alpha}} \cong U_{\alpha} \times \mathbb{C}$,
$$\begin{aligned}
d f\left(z, w_{\alpha}\right) & =w_{\alpha}^{m}\left[w_{\alpha} d s_{\alpha}+(m+1) s_{\alpha} d w_{\alpha}\right] \\
(d f)^{\odot \ell} & =w_{\alpha}^{\ell m}\left[\sum_{k=0}^{\ell} C_{k}^{\ell}\left(w_{\alpha}^{k}\right)\left((m+1) s_{\alpha}\right)^{\ell-k}\left(d s_{\alpha}\right)^{\odot k} \odot\left(d w_{\alpha}\right)^{\odot(\ell-k)}\right]
\end{aligned}$$
So the differential $d f \in H^{0}\left(\Omega_{b}, T^{*} \Omega_{b}\right)$ vanishes precisely to order $m$ on $T_{b}$ and it follows that
$$(d f)^{\odot \ell} \in H^{0}\left(\Omega_{b}, S^{\ell} T^{*} \Omega_{b}\right)$$
vanishes precisely to order $\ell m$ on $T_{b}$. \(\square\)

\section*{5 Ampleness Modulo Infinity}

In this section, we will prove another technical result which is essentially the justification of the basic estimates for the existence Theorem 4.1 under conditions about canonical radii of cusps and injectivity radius of interior of $\bar{X}$.

We will use the weight function $\varphi$ defined by Equation (16), thus the term $\sqrt{-1} \partial \bar{\partial} \varphi$ is negative only in the base direction. By Lemma 5, the Ricci curvature $\operatorname{Ric}\left(\omega_{\mathbb{P} T_{X}}\right)$ is bounded. In particular, $\operatorname{Ric}\left(\omega_{\mathbb{P} T_{X}}\right)$ is positive in the fibre directions since each fibre is equipped with the Fubini-Study metric and negative in the base directions, which is the canonical metric induced by the normalized Bergman metric. It follows that the terms
$$\operatorname{Ric}\left(\omega_{\mathbb{P} T_{X}}\right)+\sqrt{-1} \partial \bar{\partial} \varphi$$
is the most negative along the base directions. Thus we only need to justify (*) along the base directions.

Proposition 5.1. Let $X=\mathbb{B}^{n} / \Gamma, b \in \partial \mathbb{B}^{n}$ be a cusp of $\Gamma, \tau>0$ be the generator of the one parameter subgroup $\Gamma \cap\left[U_{b}, U_{b}\right]$, where $U_{b}=\operatorname{rad} P_{b}$ is the unipotent radical of the parabolic subgroup $P_{b} \subset \operatorname{Aut}\left(\mathbb{B}^{n}\right)\left(P_{b}\right.$ is the isotropy subgroup of $b$ in $\operatorname{Aut}\left(\mathbb{B}^{n}\right)$ ). Suppose $\ell, \gamma$ are nonnegative integers and $\varepsilon>0$ such that
$$\ell-n-1-\varepsilon>0 .$$
Then there is a constant $r^{*}=r^{*}(n)>0$ such that if $\|w\| \geq r^{*}$ for any point $(w,[u]) \in \operatorname{Supp}(\chi) \subset X \subset \bar{X} \subset \mathbb{P} T_{\bar{X}}$, then
$$(*): \Theta\left(\mathcal{O}_{\mathbb{P} T_{X}}(\ell),\left(\hat{g}^{*}\right)^{\ell}\right)+\operatorname{Ric}\left(\omega_{\mathbb{P} T_{X}}\right)+\sqrt{-1} \partial \bar{\partial} \varphi \geq \varepsilon \omega_{\mathbb{P} T_{X}}$$
everywhere on $\mathbb{P} T_{X}$.
Proof. Let $\varepsilon>0$. By Equation (7), Lemma 5 and the assumption $\ell-n-$ $1-\varepsilon>0$, we have
$$\begin{aligned}
\left(*_{1}\right): & \Theta\left(\mathcal{O}_{\mathbb{P} T_{X}}(\ell),\left(\hat{g}^{*}\right)^{\ell}\right)+\operatorname{Ric}\left(\omega_{\mathbb{P} T_{X}}\right)-\varepsilon \omega_{\mathbb{P} T_{X}} \\
\geq & (\ell-n-1-\varepsilon) \sqrt{-1} \partial \bar{\partial} \log g_{0}>0 .
\end{aligned}$$
Thus it remains to show that the curvature term $\sqrt{-1} \partial \bar{\partial} \log g_{0}$ dominates the weight function term $\sqrt{-1} \partial \bar{\partial} \varphi$.

View $\bar{X} \subset \mathbb{P} T_{\bar{X}}$ by identifying $\bar{X}$ with the zero section in $\mathbb{P} T_{\bar{X}} \rightarrow \bar{X}$. Recall that for each $u \geq u_{b}$ (the canonical height of $b$ ), we may view $\left\{w_{n}=\right.$ $0\}=T_{b} \subset \Omega^{(u)} \subset \bar{X} \subset \mathbb{P} T_{\bar{X}}$, where
$$\Omega^{(u)}=\left\{\left.w=\left(w^{\prime}, w_{n}\right) \in \mathbb{C}^{n}\left|\|w\|=e^{\frac{2 \pi}{\tau}\left|w^{\prime}\right|^{2}} \cdot\right| w_{n} \right\rvert\,<e^{\frac{-2 \pi}{\tau} u}\right\} / \varphi\left(\Gamma \cap U_{b}\right)$$
is a level set of $\bar{\mu}$ (recall that $\bar{\mu}$ is the Hermitian metric of the line bundle over the boundary abelian variety $T_{b}$ which induces the norm $\|\cdot\|$ ). For $u_{1}<u_{0}$, we have $\Omega^{\left(u_{1}\right)} \supset \Omega^{\left(u_{0}\right)} \supset T_{b}$. Define on $\Omega^{u} \subset \bar{X} \subset \mathbb{P} T_{\bar{X}}\left(u<u_{1}<u_{0}\right)$ the cutoff function
$$\chi(\|w\|)= \begin{cases}1, & \|w\| \leq e^{\frac{2 \pi}{\tau} u_{0}}:=r_{0}, \\ 0, & \|w\| \geq e^{\frac{2 \pi}{\tau} u_{1}}:=r_{1} .\end{cases}$$
Note that
$$\operatorname{Supp}(\chi) \subset \Omega^{\left(u_{1}\right)}-\Omega^{\left(u_{0}\right)}=\left\{w \in \mathbb{C}^{n} \mid r_{0} \leq\|w\|<r_{1}\right\} / \varphi\left(\Gamma \cap U_{b}\right) .$$
By construction, $\chi$ depends only on $\|w\|$. Moreover, $\frac{\partial \chi}{\partial\|w\|}<0$ on $\Omega^{\left(u_{1}\right)}-$ $\Omega^{\left(u_{0}\right)}$. Define
$$\delta(w):=1-\|w\|,$$
which is just the distance from $w \in \Omega^{(u)}$ to the boundary $\{\|w\|=1\}$. Let $r_{1}=1-\delta$ and $r_{0}=1-2 \delta$. From standard arguments of mollifiers (cf. [9] Theorem 1.4.1 and the note after the proof), we have the uniform bounds
$$\left|\frac{\partial \chi}{\partial w_{i}}\right|,\left|\frac{\partial \chi}{\partial \bar{w}_{j}}\right| \leq \frac{1+\epsilon}{\delta}<\frac{2}{\delta}, \quad\left|\frac{\partial^{2} \chi}{\partial w_{i} \partial \bar{w}_{j}}\right|<\frac{1+\epsilon}{\delta^{2}}<\frac{2}{\delta^{2}}, \quad \forall 1 \leq i, j \leq n$$
for any $0<\epsilon<1$. For some $\gamma \in \mathbb{N}$, let
$$\varphi:=\gamma \chi \log \|w\|^{2},$$
where $\|w\|=\left\|\left(w^{\prime}, w_{n}\right)\right\|=e^{\frac{2 \pi}{\tau}}\left|w^{\prime}\right|^{2} \cdot\left|w_{n}\right|$ is the norm induced by the Hermitian metric $\bar{\mu}$ on $\Omega^{(u)} \rightarrow T_{b}$.

We need to obtain a pointwise estimate of $\sqrt{-1} \partial \bar{\partial} \varphi$ in $\Omega^{\left(u_{1}\right)}-\Omega^{\left(u_{0}\right)}$. First note that by chain rule,
$$\partial \bar{\partial} \chi(\|w\|)=\chi^{\prime \prime}(\|w\|) \partial\|w\| \wedge \bar{\partial}\|w\|+\chi^{\prime}(\|w\|) \partial \bar{\partial}\|w\|$$
The Hessian $\sqrt{-1} \partial \bar{\partial}\|w\|$ can be expressed in terms of gradient square $\sqrt{-1} \partial\|w\| \wedge$ $\bar{\partial}\|w\|$ as follows
$$\partial \bar{\partial}\|w\|=\frac{2 \pi}{\tau}\|w\| \partial \bar{\partial}\left|w^{\prime}\right|^{2}+\frac{\partial\|w\| \wedge \bar{\partial}\|w\|}{\|w\|} .$$

Note that $\operatorname{Supp}(\varphi) \subset \Omega^{\left(u_{1}\right)}-\Omega^{\left(u_{0}\right)}$. So $\varphi$ is a smooth function on $\mathbb{P} T_{\bar{X}}$ such that
$$\begin{aligned}
\left(*_{2}\right): & \sqrt{-1} \partial \bar{\partial} \varphi \\
= & \gamma \sqrt{-1}\left(\chi \partial \bar{\partial} \log \|w\|^{2}+\log \|w\|^{2} \partial \bar{\partial} \chi+\partial \log \|w\|^{2} \wedge \bar{\partial} \chi+\partial \chi \wedge \bar{\partial} \log \|w\|^{2}\right) \\
= & {\left[\chi \frac{4 \pi}{\tau}+\frac{4 \pi}{\tau} \chi^{\prime}(\|w\|)\|w\| \log \|w\|\right] \gamma \sqrt{-1} \partial \bar{\partial}\left|w^{\prime}\right|^{2} } \\
& +\left[2 \chi^{\prime \prime}(\|w\|) \log \|w\|+\frac{4 \chi^{\prime}(\|w\|)}{\|w\|}+\frac{2 \chi^{\prime}(\|w\|) \log \|w\|}{\|w\|}\right] \gamma \sqrt{-1} \partial\|w\| \wedge \bar{\partial}\|w\| \\
= & { \left.\left[\chi \frac{4 \pi}{\tau}+\frac{4 \pi}{\tau} \chi^{\prime}(\|w\|)\|w\| \log \|w\|\right] \gamma \sqrt{-1} \partial \bar{\partial} \right\rvert\, w^{\prime} \|^{2} \quad(\text { positive term }) } \\
& +\left[\frac{2 \chi^{\prime}(\|w\|) \log \|w\|}{\|w\|}\right] \gamma \sqrt{-1} \partial\|w\| \wedge \bar{\partial}\|w\| \quad(\text { positive term }) \\
& +\left[2 \chi^{\prime \prime}(\|w\|) \log \|w\|+\frac{4 \chi^{\prime}(\|w\|)}{\|w\|}\right] \gamma \sqrt{-1} \partial\|w\| \wedge \bar{\partial}\|w\| \quad \text { (negative term). }
\end{aligned}$$
For any $0<1-2 \delta \leq\|w\|<1-\delta<1$, as $\delta \rightarrow 0$,
$$\begin{aligned}
\frac{1}{1-\delta}<\frac{1}{\|w\|} & \leq \frac{1}{1-2 \delta}, \quad-\frac{2}{\delta}<\chi^{\prime}(\|w\|)<0, \quad-\frac{2}{\delta^{2}}<\chi^{\prime \prime}(\|w\|)<\frac{2}{\delta^{2}}, \\
-2 \delta(1+o(\delta)) & =\log (1-2 \delta) \leq \log \|w\|<\log (1-\delta)=-\delta(1+o(\delta))<0 .
\end{aligned}$$
Thus
$$\begin{aligned}
& 2 \chi^{\prime \prime}(\|w\|) \log \|w\| \geq\left\{\begin{array}{l}
2\left(\frac{2}{\delta^{2}}\right)(-2 \delta(1+o(\delta)))=-\frac{8}{\delta}(1+o(\delta)), \quad \text { if } 0<\chi^{\prime \prime}<\frac{2}{\delta^{2}}, \\
0, \quad \text { if }-\frac{2}{\delta^{2}}<\chi^{\prime \prime} \leq 0,
\end{array}\right. \\
& \Rightarrow \quad 2 \chi^{\prime \prime}(\|w\|) \log \|w\| \geq-\frac{8}{\delta}(1+o(\delta))=-\frac{8}{\delta}+O(1) .
\end{aligned}$$
and
$$\frac{4 \chi^{\prime}(\|w\|)}{\|w\|} \geq 4\left(-\frac{2}{\delta}\right)\left(\frac{1}{1-2 \delta}\right)=-8\left(\frac{1}{\delta}+\frac{2}{1-2 \delta}\right)=-\frac{8}{\delta}+O(1) .$$
Thus the negative term
$$2 \chi^{\prime \prime}(\|w\|) \log \|w\|+\frac{4 \chi^{\prime}(\|w\|)}{\|w\|} \geq-\frac{8}{\delta}+O(1)-\frac{8}{\delta}+O(1)=-\frac{16}{\delta}+O(1) .$$

It follows that
$$\begin{aligned}
R . H . S .\left(*_{2}\right) \geq & {\left[\chi \frac{4 \pi}{\tau}+\frac{4 \pi}{\tau} \chi^{\prime}(\|w\|)\|w\| \log \|w\|\right] \gamma \sqrt{-1} \partial \bar{\partial}\left|w^{\prime}\right|^{2} \quad \text { (positive term) } } \\
& +\left[\frac{2 \chi^{\prime}(\|w\|) \log \|w\|}{\|w\|}\right] \gamma \sqrt{-1} \partial\|w\| \wedge \bar{\partial}\|w\| \quad \text { (positive term) } \\
& +\left[-\frac{16}{\delta}+O(1)\right] \gamma \sqrt{-1} \partial\|w\| \wedge \bar{\partial}\|w\| \quad \text { (negative term). }
\end{aligned}$$
To verify the basic estimates with weights (*), it suffices to verify for points in $\operatorname{Supp} \chi \subset \Omega^{\left(u_{1}\right)}-\Omega^{\left(u_{0}\right)}$. All negativity comes from the weight function which lies in base directions (i.e., the $w$-directions). By the uniform estimate of the curvature via Equation (7) (or the fact that the Kähler metric along fibre $\cong \mathbb{P}^{n-1}$ is essentially the Fubini-Study metric), we know that $(*) \geq 0$ in the fibre directions (i.e., the $u$-directions). Thus it remains to consider the base directions.

Combining $\left(*_{1}\right)$ and $\left(*_{2}\right)$, we have
$$\begin{aligned}
(* *): & \Theta\left(\mathcal{O}_{\mathbb{P} T_{X}}(\ell),\left(\hat{g}^{*}\right)^{\ell}\right)+\operatorname{Ric}\left(\omega_{\mathbb{P} T_{X}}\right)-\varepsilon \omega_{\mathbb{P} T_{X}}+\sqrt{-1} \partial \bar{\partial} \varphi \\
\geq & (\ell-n-1-\varepsilon) \sqrt{-1} \partial \bar{\partial} \log g_{0} \\
& +\left[\chi \frac{4 \pi}{\tau}+\frac{4 \pi}{\tau} \chi^{\prime}(\|w\|)\|w\| \log \|w\|\right] \gamma \sqrt{-1} \partial \bar{\partial}\left|w^{\prime}\right|^{2} \\
& +\left[\frac{2 \chi^{\prime}(\|w\|) \log \|w\|}{\|w\|}\right] \gamma \sqrt{-1} \partial\|w\| \wedge \bar{\partial}\|w\| \\
& +\left[-\frac{16}{\delta}+O(1)\right] \gamma \sqrt{-1} \partial\|w\| \wedge \bar{\partial}\|w\| .
\end{aligned}$$
Observe that the negative terms on the right hand side of (**) has asymptotic behaviour at worst $1 / \delta$. By the asymptotic behaviour (13), when $\|w\| \rightarrow 1$, the curvature $\sqrt{-1} \partial \bar{\partial} \log g_{0}$ has asymptotic behaviour $1 / \delta^{2}$. Hence the curvature $\sqrt{-1} \partial \bar{\partial} \log g_{0}$ dominates the negativity coming from the weight functions. Thus we have verified the basic estimates $(*)$ for the points along the fibre in the chart $U_{n}=\left\{\left[v^{1}, \ldots, v^{n}\right] \in \mathbb{P}^{n-1} \mid v^{n} \neq 0\right\}$. Now by Lemma 3.5, the above argument holds for any point $\left(u^{1}, \ldots, u^{n-1}, 1\right)$, even when we let $u^{i} \rightarrow \infty$ for some $1 \leq i \leq n-1$. Thus the basic estimates (*) actually holds everywhere on $\mathbb{P} T_{X}$ provided any point $(w,[u]) \in \operatorname{Supp}(\chi) \subset X \subset$ $\mathbb{P} T_{X}$ is such that $\|w\|$ is sufficiently close to 1. \(\square\)

Proof of Main Theorem (Theorem 1.2). We will prove the base point freeness, separation of tangents and separation of points one by one.

\section*{Base Point Freeness}

For a given point $p \in \mathbb{P} T_{\bar{X}}-\pi^{-1}(D)$, we need to construct a holomorphic section $\sigma \in H^{0}\left(\mathbb{P} T_{\bar{X}}, \mathcal{O}_{\mathbb{P} T_{\bar{X}}}(\ell)\right)$ such that $\sigma(p) \neq 0$. Under our hypothesis of canonical radii, by Proposition 5.1 and the construction in section 4, base point freeness of $\mathcal{O}_{\mathbb{P} T_{\bar{X}}}(\ell)$ in $\Omega$ follows for any $\ell \geq n+2$. We may require the symmetric differential vanishes at infinity to order $\ell m$ for any $m \geq 1$.

On the other hand, consider a point $p \in \Omega^{\prime}$. We have $p=\left(p^{\prime},[\mu]\right)$, where $p^{\prime}$ and $[\mu]$ denote the coordinates corresponding to respectively the base and fibre in $\mathbb{P} T_{X}$. To produce symmetric differentials on $\bar{X}$, we may assume without loss of generality that, the affine coordinates of $[\mu]$ is 0. Thus locally $p=\left(p^{\prime}, 0\right) \in \Omega^{\prime} \subset \mathbb{P} T_{X}$ lies in $X \subset \mathbb{P} T_{X}$ where we have viewed $X$ as the zero section of $\mathbb{P} T_{X}$.

By composing an automorphism if necessary, we may let $p$ lifts to the origin $0 \in \mathbb{B}^{n}$ by lifting $X$ to the universal cover $\mathbb{B}^{n}$. In the fundamental domain $\mathcal{F}$ of $\Gamma$ in $\mathbb{B}^{n}$, there is $\rho>0$ determined by the injectivity radius $d\left(\Omega^{\prime}\right)$ with respect to $g$ and the size of $\Omega$ such that $B(0,1-\rho) \subset \mathcal{F}$.

In order to apply Theorem 4.1, let now
$$\rho(z)=1-|z|$$
and consider the weight function
$$\psi:=\chi \log |z|,$$
where
$$\chi= \begin{cases}1, & |z| \leq 1-2 \rho \\ 0, & |z| \geq 1-\rho\end{cases}$$
is a smooth cutoff function with $\operatorname{Supp}(\chi) \subset\{1-2 \rho<|z|<1-\rho\}$.

Then
$$\begin{aligned}
\left(*_{3}\right): & \sqrt{-1} \partial \bar{\partial} \psi \\
= & \sqrt{-1}(\chi \partial \bar{\partial} \log |z|+\log |z| \partial \bar{\partial} \chi+\partial \chi \wedge \bar{\partial} \log |z|+\partial \log |z| \wedge \bar{\partial} \chi) \\
= & \sqrt{-1}\left[\frac{\chi}{2} \partial \bar{\partial} \log |z|^{2}+\log |z|\left(\chi^{\prime \prime} \partial|z| \wedge \bar{\partial}|z|+\chi^{\prime} \partial \bar{\partial}|z|\right)\right. \\
& \left.+\chi^{\prime} \partial|z| \wedge \frac{1}{|z|} \bar{\partial}|z|+\frac{1}{|z|} \partial|z| \wedge \chi^{\prime} \bar{\partial}|z|\right] \\
= & \sqrt{-1}\left[\frac{\chi}{2} \partial \bar{\partial} \log |z|^{2}+\chi^{\prime} \log |z| \partial \bar{\partial}|z|+\left(\chi^{\prime \prime} \log |z|+\frac{2 \chi^{\prime}}{|z|}\right) \partial|z| \wedge \bar{\partial}|z|\right] \\
= & \sqrt{-1}\left[\frac{\chi}{2} \partial \bar{\partial} \log |z|^{2}+\chi^{\prime} \log |z|\left(\frac{1}{2|z|} \partial \bar{\partial}|z|^{2}-\frac{1}{|z|} \partial|z| \wedge \bar{\partial}|z|\right)\right. \\
& \left.+\left(\chi^{\prime \prime} \log |z|+\frac{2 \chi^{\prime}}{|z|}\right) \partial|z| \wedge \bar{\partial}|z|\right] \\
= & \sqrt{-1}\left[\frac{\chi}{2} \partial \bar{\partial} \log |z|^{2}+\frac{\chi^{\prime} \log |z|}{2|z|} \partial \bar{\partial}|z|^{2}\right] \quad \text { (positive term). } \\
& +\left(-\frac{\chi^{\prime} \log |z|}{|z|}+\chi^{\prime \prime} \log |z|+\frac{2 \chi^{\prime}}{|z|}\right) \sqrt{-1} \partial|z| \wedge \bar{\partial}|z| \quad \text { (negative term) }
\end{aligned}$$
By estimates similar to Equations $\left(*_{2}\right)$, we have
$$\begin{aligned}
-\frac{\chi^{\prime} \log |z|}{|z|} & \geq-\left(-\frac{2}{\rho}\right)(\log (1-2 \rho))\left(\frac{1}{1-2 \rho}\right)=-\left(-\frac{2}{\rho}\right)(-2 \rho(1+o(\rho)))\left(\frac{1}{1-2 \rho}\right) \\
& =-\frac{4}{1-2 \rho}(1+o(\rho))=O(1), \\
\chi^{\prime \prime} \log |z| & \geq \frac{2}{\rho^{2}}(\log (1-2 \rho))=\frac{2}{\rho^{2}}(-2 \rho(1+o(\rho)))=\frac{-4}{\rho}+O(1), \\
\frac{2 \chi^{\prime}}{|z|} & \geq 2\left(\frac{-2}{\rho}\right)\left(\frac{1}{1-2 \rho}\right)=-4\left(\frac{1}{\rho}+\frac{2}{1-2 \rho}\right)=\frac{-4}{\rho}+O(1) .
\end{aligned}$$
The negative term becomes
$$-\frac{\chi^{\prime} \log |z|}{|z|}+\chi^{\prime \prime} \log |z|+\frac{2 \chi^{\prime}}{|z|} \geq-\frac{8}{\rho}+O(1) .$$
Thus
$$\begin{aligned}
\text { R.H.S. }\left(*_{3}\right) \geq & \sqrt{-1}\left[\frac{\chi}{2} \partial \bar{\partial} \log |z|^{2}+\frac{\chi^{\prime} \log |z|}{2|z|} \partial \bar{\partial}|z|^{2}\right] \quad \text { (positive term) } \\
& +\left(-\frac{8}{\rho}+O(1)\right) \sqrt{-1} \partial|z| \wedge \bar{\partial}|z| \quad \text { (negative term). }
\end{aligned}$$

It follows that the negativity is of growth $1 / \rho$. To verify the basic estimates
$$\Theta\left(\mathcal{O}_{\mathbb{P} T_{X}}(\ell),\left(\hat{g}^{*}\right)^{\ell}\right)+\operatorname{Ric}\left(\omega_{\mathbb{P} T_{X}}\right)+\sqrt{-1} \partial \bar{\partial} \psi \geq \varepsilon \omega_{\mathbb{P} T_{X}},$$
on $\Omega^{\prime}=\mathbb{P} T_{X}-\Omega$, it suffices to focus on the base direction, i.e., the $z$ -coordinates. By the asymptotic behaviour (12), it follows that the curvature term is positive and of growth $1 / \rho^{2}$ as $\rho \rightarrow 0$. Thus for $\rho$ sufficient close to 0, the curvature terms dominate the negativity coming from the weight function term. Hence the Basic Estimates (20) is verified whenever $\rho$ is sufficiently close to 0.

To construct a symmetric differential non-vanishing at the point $p$, first of all, let $\chi$ be a cutoff function supported in a small neighbourhood $U$ of the interior point $p$. Let $e$ be a holomorphic basis of the line subbundle $\left.\mathcal{O}_{U}(1) \subset \mathcal{O}_{\mathbb{P} T_{X}}(1)\right|_{U}$. Since we have verified the Basic Estimates (20), by Theorem 4.1, a solution to the equation
$$\bar{\partial} u=\bar{\partial}\left(\chi e^{\ell}\right)$$
exists and satisfies the estimates
$$\int_{\mathbb{P} T_{X}}\|u\|^{2} e^{-(4 n-2) \psi} d V \leq \frac{1}{\varepsilon} \int_{\mathbb{P} T_{X}}\left\|\bar{\partial}\left(\chi e^{\ell}\right)\right\|^{2} e^{-(4 n-2) \psi} d V<\infty,$$
where $d V=\frac{\omega_{\mathbb{P} T_{X}}^{2 n-1}}{(2 n-1)!}$. Let $U \cong \Delta^{2 n-1}(\epsilon)$ be a small neighbourhood of $p$ for some $0<\epsilon<1$, which is identified to the origin in $\Delta^{2 n-1}(\epsilon)$. In the chart $\Delta^{2 n-1}(\epsilon)$, for some constant $C>0$ and $d V_{e}$ the Euclidean volume on $\mathbb{C}^{2 n-1}$, we have
$$e^{-(4 n-2) \psi} d V=C \frac{1}{|z|^{4 n-2}} d V_{e}=C \frac{1}{r^{4 n-2}} r^{4 n-3} d S=\frac{C}{r} d S$$
where $r=|z|$ is the polar radius and $d S$ is the volume form of the unit sphere. The last equality combined with the estimates (21) shows that $u$ must vanish at the point $p$ to order at least 1. Let
$$\sigma:=\chi e^{\ell}-u$$
Then $\bar{\partial} \sigma=\bar{\partial}\left(\chi e^{\ell}\right)-\bar{\partial} u=0$ implies that $\sigma$ is holomorphic. Moreover, $\sigma(p)=e^{\ell}(p)-u(p)=e^{\ell}(p) \neq 0$. Thus we have demonstrated the base point freeness of $H^{0}\left(\mathbb{P} T_{\bar{X}}, \mathcal{O}_{\mathbb{P} T_{\bar{X}}}(\ell)\right)$ in $\Omega$ for $\ell \geq n+2$.

To conclude, we have shown that $H^{0}\left(\mathbb{P} T_{\bar{X}}, \mathcal{O}_{\mathbb{P} T_{\bar{X}}}(\ell)\right)$ is base point free on $\mathbb{P} T_{\bar{X}}-\pi^{-1}(D)$ for $\ell \geq n+2$.

\section*{Separation of Tangents}

We need to show that for any $p \in \mathbb{P} T_{X}-\pi^{-1}(D)$, there is a holomorphic section $\sigma \in H^{0}\left(\mathbb{P} T_{\bar{X}}, \mathcal{O}_{\mathbb{P} T_{\bar{X}}}(\ell)\right)$ such that its differential $d \sigma_{p} \neq 0$. The assertion essentially follows similar arguments as the proof in the base point freeness. If $p \in \Omega$ is a point near infinity, then the separation of tangents essentially follows from the Lefschetz's embedding theorem for abelian variety. Here we also only need to require $\ell \geq n+2$. If $p \in \Omega^{\prime}$ is a point in the interior part, then one consider a more singular weight function $4 n \psi$ and start the construction with the local holomorphic section $z_{i} e^{\ell}$ for any coordinate function $z_{i}$. The required injectivity radius would be larger than that in the proof of base point freeness.

\section*{Separation of Points}

We need to show that for any pair of points $p, q \in \mathbb{P} T_{X}-\pi^{-1}(D)$, there are holomorphic sections $\sigma, \eta \in H^{0}\left(\mathbb{P} T_{\bar{X}}, \mathcal{O}_{\mathbb{P} T_{\bar{X}}}(\ell)\right)$ such that $\sigma(p) \neq 0, \sigma(q)=0$ and $\eta(p)=0, \eta(q) \neq 0$. There are three possibilities:
\begin{itemize}
\item[1.] $p, q \in \Omega$ are points near infinity.
\item[2.] $p \in \Omega$ and $q \in \Omega^{\prime}$.
\item[3.] $p, q \in \Omega^{\prime}$ are both in the interior part.
\end{itemize}
1) Suppose $p, q \in \Omega$. If $p$ and $q$ lie in two disjoint neighbourhoods (of sizes depending on injectivity radii), then the result follows from the construction in the proof of base point freeness applied to $p$ and $q$ separately. If both $p$ and $q$ lie in the same neighbourhood, then the assertion follows from the Lefschetz's embedding theorem for abelian variety. Here we may take any $\ell \geq n+2$.
2) Suppose $p \in \Omega$ and $q \in \Omega^{\prime}$. Then we only need to apply the construction in the proof of base point freeness for $p$ and $q$ separately.
3) Suppose $p, q \in \Omega^{\prime}$. Without loss of generality, assume $p$ is lifted to the origin 0 in the universal cover $\mathbb{B}^{n}$ and $q$ some point $a \neq 0$ in $\mathbb{B}^{n}$. There is $\rho>0$ depending on the injectivity radius so that $B(0,1-\rho)$ corresponds to the metric ball neighbourhood of $p \in X$ of maximal size.

If $a \notin B(0,1-\rho)$, then we can find two disjoint neighbourhood $B_{0}$ and $B_{a}$ (whose sizes also depend on the injectivity radii) of 0 and $a$ respectively in $\mathbb{B}^{n}$ and apply the construction of the base point freeness to produce the desired sections. This would require a larger injectivity radius than the one in the original construction of sections for base point freeness of only one
point because the radii of the neighbourhoods of $p$ and $q$ (or 0 and $a$ ) cannot be taken to be the maximal ones.

If $a \in B(0,1-\rho)$, then instead of $\psi=\chi \log |z|$, we only need to consider another weight function
$$\psi_{1}:=\chi(\log |z|+\log |z-a|) .$$
The verification of the basic estimates and construction of section then follows similarly to the case of base point freeness (which also requires a possibly larger injectivty radius since $\psi_{1}$ would give two negative terms of same order of magnitude instead of when considering $\psi$ ). \(\square\)

Proof of Corollary 1.3. It suffices to show that the injectivity radius of the interior part of $\bar{X}$ and the canonical radii of the cusps both increase upon lifting along a tower of coverings of $X$. Write $\pi_{1}\left(X_{k}\right)=\Gamma_{k}$. Since $\left\{X_{k}\right\}$ is a tower of covering of $X$, we have $\Gamma_{k+1} \subset \Gamma_{k}$ for any $k \geq 0$.

Let $p \in \Omega^{\prime}$ be a point in the interior compact part. We want to show that the injectivity radius of $p$ goes to infinity when lifted along the tower of coverings. Let $p_{0}$ be any lifting of $p$ to the universal cover $\mathbb{B}^{n}$ of $X$. By definition, the injectivity radius $d_{k}=d_{k}(p)$ is the largest radius so that the metric ball $B_{g}\left(p_{0}, d_{k}\right)$ (where $g$ is the Bergman metric of $\mathbb{B}^{n}$ ) injects into $X_{k}$ via the covering map $\mathbb{B}^{n} \rightarrow X_{k}$. This implies that
$$\left\{\gamma \in \Gamma_{k} \mid \gamma\left(\overline{B_{g}\left(p_{0}, d\right)}\right) \cap \overline{B_{g}\left(p_{0}, d\right)} \neq \emptyset\right\}=\{i d\}$$
for any $d \leq d_{k}$. Let $r>0$ be a real number. Since $\Gamma_{k}$ is discrete,
$$\left|\left\{\gamma \in \Gamma_{k} \mid \gamma\left(\overline{B_{g}\left(p_{0}, r\right)}\right) \cap \overline{B_{g}\left(p_{0}, r\right)} \neq \emptyset\right\}\right|<\infty .$$
Note that $\Gamma_{k} \rightarrow\{\mathrm{id}\}$ as $k \rightarrow \infty$, there is $k_{r} \geq 0$ such that
$$\left\{\gamma \in \Gamma_{k_{r}} \mid \gamma\left(\overline{B_{g}\left(p_{0}, r\right)}\right) \cap \overline{B_{g}\left(p_{0}, r\right)} \neq \emptyset\right\}=\{i d\}$$
for any $k \geq k_{r}$. It follows that $d_{k} \geq r$ for any $k \geq k_{r}$. Since $r>0$ is arbitrary, the sequence $\left\{d_{k}\right\}$ must be increasing and $d_{k} \rightarrow \infty$ as $k \rightarrow \infty$.

To see that the canonical radii increase upon lifting along the tower of coverings, consider in particular a cusp $b$ of $\Gamma=\Gamma_{0}$, which lifts by the covering $X_{k} \rightarrow X$ to a cusp $b_{k}$ of $\Gamma_{k} \subset \Gamma_{0}=\Gamma$.

Let $\Omega^{\left(u_{b}\right.} \subset \bar{X}$ be the fundamental neighbourhood of the infinity $T_{b}$ in $\bar{X}$, where $\Omega^{\left(u_{b}\right)} \rightarrow T_{b}$ carries the disk bundle structure so that
$$r_{0}:=e^{-\frac{2 \pi}{\tau_{0}} u_{b}}$$
is the canonical radius of $b$. Here $u_{b}>0$ is the canonical height of $b$ and $\tau_{0}>0$ is the generator of $\Gamma_{b, 0}=\Gamma_{0} \cap\left[U_{b}, U_{b}\right]$ (recall that $U_{b}=\operatorname{rad} P_{b}$ is the unipotent radical of the parabolic subgroup $P_{b} \subset \operatorname{Aut}\left(\mathbb{B}^{n}\right)$ and $P_{b}$ is the isotropy subgroup of $b$ in $\operatorname{Aut}\left(\mathbb{B}^{n}\right)$ ). Let
$$\Gamma_{b, k}:=\Gamma_{k} \cap\left[U_{b}, U_{b}\right] \subset \Gamma_{0} \cap\left[U_{b}, U_{b}\right] .$$
Since $\Gamma_{b, 0}$ is a one-parameter group generated by $\tau_{0}$, the normal subgroup $\Gamma_{b, k}$ is also a one parameter and is generated by some $\tau_{k} \geq \tau_{0}$. Since $\Gamma_{k} \rightarrow$ \{id\} as $k \rightarrow \infty$, we also have $\Gamma_{b, k} \rightarrow\{\mathrm{id}\}$ and as $k \rightarrow \infty$. It follows that $\left\{\tau_{k}\right\}$ is an increasing sequence of positive real numbers such that $\tau_{k} \rightarrow \infty$ as $k \rightarrow \infty$.

Now we identify $\mathbb{B}^{n}$ to the upper half space model $S$. Recall that the fundamental neighbourhood $\Omega^{\left(u_{b}\right)}$ of the infinity $T_{b}$ in $\bar{X}$ is obtained by taking interior closure in the punctured disk bundle structure of the horoball $B\left(u_{b}\right) / \Gamma_{b}$, where the canonical height $u_{b}$ is the smallest positive real number so that $B\left(u_{b}\right)$ is invariant under $\Gamma_{b}=\Gamma_{b, 0}$. The fundamental neighbourhood $\Omega^{\left(u_{b_{k}}\right)}$ of the infinity $T_{b_{k}}$ in $\overline{X_{k}}$ is obtained by taking interior closure of the puncture disk bundle structure of the horoball $B\left(u_{b_{k}}\right) / \Gamma_{b, k}$, where $u_{b_{k}}$ is the smallest positive real number so that $B\left(u_{b_{k}}\right)$ is invariant under $\Gamma_{b, k}$. Then $\Gamma_{b, k} \subset \Gamma_{b, 0}$ implies that $u_{b_{k}} \leq u_{b}$. Since $\Gamma_{b, k} \rightarrow\{\mathrm{id}\}$ as $k \rightarrow 0$, it follows that $\left\{u_{b_{k}}\right\}$ is a decreasing sequence of positive real numbers so that $u_{b_{k}} \rightarrow 0$ as $k \rightarrow \infty$.

The canonical radius of $b_{k}$ is given by
$$r_{k}=e^{\frac{-2 \pi}{\tau_{k}} u_{b_{k}}} .$$
Thus $r_{k}$ is an increasing sequence and $r_{k} \rightarrow 1$ as $k \rightarrow \infty$. \(\square\)

\section*{Acknowledgement}

This article contains material taken from the Ph.D thesis of the author, who would like to sincerely thank his advisor Ngaiming Mok for the continued guidance and support. The author would also like to thank the referee for valuable suggestions.

\section*{References}
\begin{itemize}
\item[] [1] Ash, A.; Mumford, D.; Rapoport, M; Tai, Y-S. Smooth compactifications of locally symmetric varieties. Second edition. With the collaboration of Peter, S. Cambridge Mathematical Library. Cambridge University Press, Cambridge, 2010. $\mathrm{x}+230 \mathrm{pp}$.
\end{itemize}
\begin{itemize}
\item[] [2] Andreotti, A.; Vesentini, Edoardo E. Carleman estimates for the Laplace-Beltrami equation on complex manifolds. Inst. Hautes tudes Sci. Publ. Math. No. 25196581130.
\item[] [3] Brunebarbe, Y.; Klingler, B.; Totaro, B. Symmetric differentials and the fundamental group. Duke Math. J. 162 (2013), no. 14, 2797-2813.
\item[] [4] Birkenhake, C; Lange, H. Complex abelian varieties. Second edition. Grundlehren der Mathematischen Wissenschaften 302. Springer-Verlag, Berlin, 2004. xii+635 pp..
\item[] [5] Bakker, B.; Tsimerman, J. The Kodaira dimension of complex hyperbolic manifolds with cusps, (arXiv:1503.05654) 2015.
\item[] [6] Cadorel, B. Symmetric differentials on complex hyperbolic manifolds with cusps. arXiv: 1606.05470v3 (2016).
\item[] [7] Di Cerbo, G.; Di Cerbo, L. F. Effective results for complex hyperbolic manifolds. J. Lond. Math. Soc. (2) 91 (2015), no. 1, 89-104.
\item[] [8] Hörmander, L. $L^{2}$ estimates and existence theorems for the $\bar{\partial}$ operator. Acta Math. 1131965 89-152.
\item[] [9] Hörmander, L. The analysis of linear partial differential operators. I. Distribution theory and Fourier analysis. Reprint of the second (1990) edition. Springer-Verlag, Berlin, 2003. x+440 pp.
\item[] [10] Klingler, B. Symmetric differentials, Kähler groups and ball quotients. Invent. Math. 192 (2013), no. 2, 257-286.
\item[] [11] Mok, N. Metric rigidity theorems on Hermitian locally symmetric manifolds. Series in Pure Mathematics, 6. World Scientific Publishing Co., Inc., Teaneck, NJ, 1989. xiv+278 pp.
\item[] [12] Mok, N. Projective algebraicity of minimal compactifications of complex-hyperbolic space forms of finite volume. Perspectives in analysis, geometry, and topology, 331-354, Progr. Math., 296, Birkhäuser/Springer, New York, 2012.
\item[] [13] Parker, J. R. On the volumes of cusped, complex hyperbolic manifolds and orbifolds. Duke Math. J. 94 (1998), no. 3, 433-464.
\item[] [14] Mumford, D. Hirzebruch's proportionality theorem in the noncompact case. Invent. Math. 42 (1977), 239-272.
\end{itemize}
\begin{itemize}
\item[] [15] Nadel, A. M. The nonexistence of certain level structures on abelian varieties over complex function fields. Ann. of Math. (2) 129 (1989), no. 1, 161-178.
\item[] [16] Wang, X. Effective very ampleness of the canonical line bundles on ball quotients. J. Geom. Anal. 25 (2015), no. 2, 740-760.
\end{itemize}
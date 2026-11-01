---
retention_scope: session
part: 2
total_parts: 4
---

[Part 2/4 of: Monopoles over 4-manifolds containing long necks, I]

Given a parameter $\mu \in \Omega^{2}(X)$ there are the following Seiberg-Witten equations for a configuration $(A, \Phi)$ over $X$ :
$$\begin{aligned}
\left(\hat{F}_{A}+i \mu\right)^{+} & =Q(\Phi) \\
D_{A} \Phi & =0,
\end{aligned}$$
where
$$Q(\Phi)=\frac{1}{4} \sum_{j=1}^{3}\left\langle\alpha_{j} \Phi, \Phi\right\rangle \alpha_{j}$$
for any local orthonormal basis $\left\{\alpha_{j}\right\}$ of imaginary-valued self-dual 2 -forms on $X$. If $\Psi$ is another section of $\mathbb{S}_{X}^{+}$then one easily shows that
$$Q(\Phi) \Psi=\langle\Psi, \Phi\rangle_{\mathbb{C}} \Phi-\frac{1}{2}|\Phi|^{2} \Psi .$$
Now let $X=\mathbb{R} \times Y$ and for present and later use recall the standard bundle isomorphisms
$$\begin{aligned}
\rho^{1}: \pi_{2}^{*}\left(\Lambda^{0}(Y) \oplus \Lambda^{1}(Y)\right) & \rightarrow \Lambda^{1}(\mathbb{R} \times Y), & & (f, a) \mapsto f d t+a, \\
\rho^{+}: \pi_{2}^{*}\left(\Lambda^{1}(Y)\right) & \rightarrow \Lambda^{+}(\mathbb{R} \times Y), & & a \mapsto \frac{1}{2}\left(d t \wedge a+*_{Y} a\right) .
\end{aligned}$$
Here $*_{Y}$ is the Hodge $*$-operator on $Y$. Let $\mu$ be the pull-back of a 2 -form $\eta$ on $Y$. Set $\vartheta=\vartheta_{\eta}$. Let $S=(A, \Phi)$ be any smooth configuration over $\mathbb{R} \times Y$ such that $A$ is in temporal gauge. Under the identification $\mathbb{S}_{\mathbb{R} \times Y}^{+}=\pi_{2}^{*}\left(\mathbb{S}_{Y}\right)$ we have
$$\rho^{+}(\sigma(\Phi, \Phi))=2 Q(\Phi) .$$
Let $\nabla_{1} \vartheta, \nabla_{2} \vartheta$ denote the 1-form and spinor parts of $\nabla \vartheta$, respectively. Then
$$\begin{aligned}
\rho^{+}\left(\frac{\partial A}{\partial t}+\nabla_{1} \vartheta_{S}\right) & =\left(\hat{F}_{A}+i \pi_{2}^{*} \eta\right)^{+}-Q(\Phi) \\
\frac{\partial \Phi}{\partial t}+\nabla_{2} \vartheta_{S} & =-d t \cdot D_{A} \Phi,
\end{aligned}$$
Thus, the downward gradient flow equation
$$\frac{\partial S}{\partial t}+\nabla \vartheta_{S}=0$$
is equivalent to the Seiberg-Witten equations (13).

\subsection*{3.3 Perturbations}

For transversality reasons we will, as in [15], add further small perturbations to the Seiberg-Witten equation over $\mathbb{R} \times Y$. The precise shape of these perturbations will depend on the situation considered. At this point we will merely
describe a set of properties of these perturbations which will suffice for the Fredholm, compactness, and gluing theory.
To any $L_{1}^{2}$ configuration $S$ over the band $\left(-\frac{1}{2}, \frac{1}{2}\right) \times Y$ there will be associated an element $h(S) \in \mathbb{R}^{N}$, where $N \geq 1$ will depend on the situation considered. If $S$ is an $L_{1}^{2}$ configuration over $\mathbf{B}^{+}=\left(a-\frac{1}{2}, b+\frac{1}{2}\right) \times Y$ where $-\infty<a<b<\infty$ then the corresponding function
$$h_{S}:[a, b] \rightarrow \mathbb{R}^{N}$$
given by $h_{S}(t)=h\left(\left.S\right|_{(t-1 / 2, t+1 / 2) \times Y}\right)$ will be smooth. These functions $h_{S}$ will have the following properties. Let $S_{o}$ be a smooth reference configuration over $\mathbf{B}^{+}$.
\begin{itemize}
\item[(P1)] For $0 \leq k<\infty$ the assignment $s \mapsto h_{S_{o}+s}$ defines a smooth map $L_{1}^{2} \rightarrow C^{k}$ whose image is a bounded set.
\item[(P2)] If $S_{n} \rightarrow S$ weakly in $L_{1}^{2}$ then $\left\|h_{S_{n}}-h_{S}\right\|_{C^{k}} \rightarrow 0$ for every $k \geq 0$.
\item[(P3)] $h_{S}$ is gauge invariant, ie $h_{S}=h_{u(S)}$ for any smooth gauge transformation $u$.
\end{itemize}
We will also choose a compact codimension 0 submanifold $\Xi \subset \mathbb{R}^{N}$ which does not contain $h(\underline{\alpha})$ for any critical point $\alpha$, where $\underline{\alpha}$ is the translationary invariant configuration over $\mathbb{R} \times Y$ determined by $\alpha$. Let $\widetilde{\mathfrak{P}}=\widetilde{\mathfrak{P}}_{Y}$ denote the space of all (smooth) 2 -forms on $\mathbb{R}^{N} \times Y$ supported in $\Xi \times Y$. For any $S$ as above and any $\mathfrak{p} \in \widetilde{\mathfrak{P}}$ let $h_{S, \mathfrak{p}} \in \Omega^{2}([a, b] \times Y)$ denote the pull-back of $\mathfrak{p}$ by the map $h_{S} \times \mathrm{Id}$. It is clear that $h_{S, \mathfrak{p}}(t, y)=0$ if $h_{S}(t) \notin \Xi$. Moreover,
$$\left\|h_{S, \mathfrak{p}}\right\|_{C^{k}} \leq \gamma_{k}\|\mathfrak{p}\|_{C^{k}}$$
where the constant $\gamma_{k}$ is independent of $S, \mathfrak{p}$.
Now let $-\infty \leq a<b \leq \infty$ and $\mathbf{B}=(a, b) \times Y$. If $\mathfrak{q}: \mathbf{B} \rightarrow \mathbb{R}$ is a smooth function then by a $(\mathfrak{p}, \mathfrak{q})$-monopole over B we shall mean a configuration $S=$ $(A, \Phi)$ over $\mathbf{B}^{+}=\left(a-\frac{1}{2}, b+\frac{1}{2}\right) \times Y$ (smooth, unless otherwise stated) which satisfies the equations
$$\begin{aligned}
\left(\hat{F}_{A}+i \pi_{2}^{*} \eta+i \mathfrak{q} h_{S, \mathfrak{p}}\right)^{+} & =Q(\Phi) \\
D_{A} \Phi & =0
\end{aligned}$$
over $\mathbf{B}$, where $\eta$ is as before. If $A$ is in temporal gauge then these equations can also be expressed as
$$\frac{\partial S_{t}}{\partial t}=-\nabla \vartheta_{S_{t}}+E_{S}(t),$$
where the perturbation term $E_{S}(t)$ depends only on the restriction of $S$ to $\left(t-\frac{1}{2}, t+\frac{1}{2}\right) \times Y$.

To reduce the number of constants later, we will always assume that $\mathfrak{q}$ and its differential $d \mathfrak{q}$ are pointwise bounded (in norm) by 1 everywhere. Note that if $\mathfrak{q}$ is constant then the equations (17) are translationary invariant. A $(\mathfrak{p}, \mathfrak{q})$-monopole with $\mathfrak{q} h_{S, \mathfrak{p}}=0$ is called a genuine monopole. In expressions like $\left\|F_{A}\right\|_{2}$ and $\|\Phi\|_{\infty}$ the norms will usually be taken over B.

For the transversality theory in Section 8 we will need to choose a suitable Banach space $\mathfrak{P}=\mathfrak{P}_{Y}$ of forms $\mathfrak{p}$ as above (of some given regularity). It will be essential that
$$\mathcal{C}\left(\mathbf{B}^{+}\right) \times \mathfrak{P} \rightarrow L^{p}\left(\mathbf{B}, \Lambda^{2}\right), \quad(S, \mathfrak{p}) \mapsto h_{S, \mathfrak{p}}$$
be a smooth map when $a, b$ are finite (here $p>2$ is the exponent used in defining the configuration space $\mathcal{C}\left(\mathbf{B}^{+}\right)$). Now, one cannot expect $h_{S, \mathfrak{p}}$ to be smooth in $S$ unless $\mathfrak{p}$ is smooth in the $\mathbb{R}^{N}$ direction (this point was overlooked in [15]). It seems natural then to look for a suitable space $\mathfrak{P}$ consisting of smooth forms $\mathfrak{p}$. Such a $\mathfrak{P}$ will be provided by Lemma 8.2. The topology on $\mathfrak{P}$ will be stronger than the $C^{\infty}$ topology, ie stronger than the $C^{k}$ topology for every $k$. The smoothness of the map (19) is then an easy consequence of property (P1) above and the next lemma.

Lemma 3.2 Let $A$ be a topological space, $U$ a Banach space, and $K \subset \mathbb{R}^{n}$ a compact subset. Then the composition map
$$C_{B}\left(A, \mathbb{R}^{n}\right) \times C^{k}\left(\mathbb{R}^{n}, U\right)_{K} \rightarrow C_{B}(A, U)$$
is of class $C^{k-1}$ for any natural number $k$. Here $C_{B}(A, \cdot)$ denotes the supremum-normed space of bounded continuous maps from $A$ into the indicated space, and $C^{k}\left(\mathbb{R}^{n}, U\right)_{K}$ is the space of $C^{k}$ maps $\mathbb{R}^{n} \rightarrow U$ with support in $K$.

Proof This is a formal exercise in the differential calculus. \(\square\)

\subsection*{3.4 Moduli spaces}

Consider the situation of Subsection 1.3. (We do not assume here that (A) holds.) We will define the moduli space $M(X ; \vec{\alpha})$. In addition to the parameter $\mu$ this will depend on a choice of perturbation forms $\mathfrak{p}_{j} \in \widetilde{\mathfrak{P}}_{Y_{j}}$ and a smooth function $\mathfrak{q}: X \rightarrow[0,1]$ such that $\|d \mathfrak{q}\|_{\infty} \leq 1, \mathfrak{q}^{-1}(0)=X_{: \frac{3}{2}}$, and $\mathfrak{q}=1$ on $[3, \infty) \times Y$.

Choose a smooth reference configuration $S_{o}=\left(A_{o}, \Phi_{o}\right)$ over $X$ which is translationary invariant and in temporal gauge over the ends, and such that $\left.S_{o}\right|_{\{t\} \times Y_{j}}$
represents $\alpha_{j} \in \widetilde{\mathcal{R}}_{Y_{j}}$. Let $p>4$ and choose $w$ as in Subsection 2.1. Let $\mathfrak{b}$ be a finite subset of $X$ and define $\mathcal{C}, \mathcal{G}_{\mathfrak{b}}, \mathcal{B}_{\mathfrak{b}}$ as in Subsections 2.1 and 2.4. For clarity we will sometimes write $\mathcal{C}(X ; \vec{\alpha})$ etc. Set $\overrightarrow{\mathfrak{p}}=\left(\mathfrak{p}_{1}, \ldots, \mathfrak{p}_{r}\right)$ and let
$$M_{\mathfrak{b}}(X ; \vec{\alpha})=M_{\mathfrak{b}}(X ; \vec{\alpha} ; \mu ; \overrightarrow{\mathfrak{p}}) \subset \mathcal{B}_{\mathfrak{b}}$$
be the subset of gauge equivalence classes of solutions $S=(A, \Phi)$ (which we simply refer to as monopoles) to the equations
$$\begin{gathered}
\left(\hat{F}_{A}+i \mu+i \mathfrak{q} \sum_{j=1}^{r} h_{S, \mathfrak{p}_{j}}\right)^{+}-Q(\Phi)=0 \\
D_{A} \Phi=0 .
\end{gathered}$$
It is clear that $\mathfrak{q} \sum_{j} h_{S, \mathfrak{p}_{j}}$ vanishes outside a compact set in $X$. If it vanishes everywhere then $S$ is called a genuine monopole. If $\mathfrak{b}$ is empty then we write $M=M_{\mathfrak{b}}$.

Note that different choices of $S_{o}$ give canonically homeomorphic moduli spaces $M_{\mathfrak{b}}(X ; \vec{\alpha})$ (and similarly for $\mathcal{B}_{\mathfrak{b}}(X ; \vec{\alpha})$ ).

Unless otherwise stated the forms $\mu$ and $\mathfrak{p}_{j}$ will be smooth. In that case every element of $M_{\mathfrak{b}}(X ; \vec{\alpha} ; \mu ; \overrightarrow{\mathfrak{p}})$ has a smooth representative, and in notation like $[S] \in M$ we will often implicitly assume that $S$ is smooth.

We define the moduli spaces $M(\alpha, \beta)=M(\alpha, \beta ; \mathfrak{p})$ of Subsection 1.2 similarly, except that we here use the equations (17) with $\mathfrak{q} \equiv 1$.

The following estimate will be crucial in compactness arguments later.
Proposition 3.1 For any element $[A, \Phi] \in M(X ; \vec{\alpha})$ one has that either
$$\Phi=0 \quad \text { or } \quad\|\Phi\|_{\infty}^{2} \leq-\frac{1}{2} \inf _{x \in X} \mathbf{s}(x)+4\|\mu\|_{\infty}+4 \gamma_{0} \max _{j}\left\|\mathfrak{p}_{j}\right\|_{\infty},$$
where $\mathbf{s}$ is the scalar curvature of $X$ and the constant $\gamma_{0}$ is as in (16).
Proof Let $\psi_{j}$ denote the spinor field of $\left.A_{o}\right|_{\{t\} \times Y_{j}}$. If $|\Phi|$ has a global maximum then the conclusion of the proposition holds by the proof of [21, Lemma 2]. Otherwise one must have $\|\Phi\|_{\infty}=\max _{j}\left\|\psi_{j}\right\|_{\infty}$ because of the Sobolev embedding $L_{1}^{p} \subset C^{0}$ on compact 4-manifolds. But the argument in [21] applied to $\mathbb{R} \times Y$ yields
$$\psi_{j}=0 \quad \text { or } \quad\left\|\psi_{j}\right\|_{\infty}^{2} \leq-\frac{1}{2} \inf _{x \in X} \mathbf{s}(x)+4\|\mu\|_{\infty}$$
for each $j$, and the proposition follows. \(\square\)

The left hand side of (20) can be regarded as a section $\Theta(S)=\widetilde{\Theta}(S, \mu, \overrightarrow{\mathfrak{p}})$ of the bundle $\Lambda^{+} \oplus \mathbb{S}^{-}$over $X$. It is clear that $\Theta$ defines a smooth map
$$\Theta: \mathcal{C} \rightarrow L^{p, w},$$
which we call the monopole map. Let $D \Theta$ denote the derivative of $\Theta$. We claim that
$$\mathcal{I}_{\Phi}^{*}+D \Theta(S): L_{1}^{p, w} \rightarrow L^{p, w}$$
is a Fredholm operator for every $S=(A, \Phi) \in \mathcal{C}$. Note that the $\mathfrak{p}_{j}$-perturbations in (20) only contribute a compact operator, so we can take $\mathfrak{p}_{j}=0$ for each $j$. We first consider the case $X=\mathbb{R} \times Y$, with $\mu=\pi_{2}^{*} \eta$ as before. By means of the isomorphisms (14), (11) and the isomorphism $\mathbb{S}^{+} \rightarrow \mathbb{S}^{-}, \phi \mapsto d t \cdot \phi$ we can think of the operator (21) as acting on sections of $\pi_{2}^{*}\left(\Lambda_{Y}^{0} \oplus \Lambda_{Y}^{1} \oplus \mathbb{S}_{Y}\right)$. If $A$ is in temporal gauge then a simple computation yields
$$\mathcal{I}_{\Phi}^{*}+D \Theta(S)=\frac{d}{d t}+P_{S_{t}},$$
where
$$P_{(B, \Psi)}=\left(\begin{array}{cc}
0 & \mathcal{I}_{\Psi}^{*} \\
\mathcal{I}_{\Psi} & H_{(B, \Psi)}
\end{array}\right)$$
for any configuration $(B, \Psi)$ over $Y$. Note that $P_{(B, \Psi)}$ is elliptic and formally self-adjoint, and if $(B, \Psi)$ is a non-degenerate critical point of $\vartheta_{\eta}$ then $\operatorname{ker} P_{(B, \Psi)}=\operatorname{ker} \mathcal{I}_{\Psi}$. Thus, the structure of the linearized equations over a cylinder is analogous to that of the instanton equations studied in [10], and the results of [10] carry over to show that (21) is a Fredholm operator.

The index of (21) is independent of $S$ and is called the expected dimension of $M(X ; \vec{\alpha})$. If $S \in \mathcal{C}$ is a monopole and $D \Theta(S): L_{1}^{p, w} \rightarrow L^{p, w}$ is surjective then $[S]$ is called a regular point of $M_{\mathfrak{b}}(X ; \vec{\alpha})$. If in addition $S \in \mathcal{C}_{\mathfrak{b}}^{*}$ then [ $S$ ] has an open neighbourhood in $M_{\mathfrak{b}}(X ; \vec{\alpha})$ which is a smooth submanifold of $\mathcal{B}_{\mathfrak{b}}^{*}$ of dimension
$$\operatorname{dim} M_{\mathfrak{b}}(X ; \vec{\alpha})=\operatorname{index}\left(\mathcal{I}_{\Phi}^{*}+D \Theta(S)\right)+|\mathfrak{b}| .$$

\section*{4 Local compactness I}

This section provides the local compactness results needed for the proof of Theorem 1.4 assuming (B1).

\subsection*{4.1 Compactness under curvature bounds}

For the moment let $B$ be an arbitrary compact, oriented Riemannian manifold with boundary, and $v$ the outward unit normal vector field along $\partial B$. Then
$$\Omega^{*}(B) \rightarrow \Omega^{*}(B) \oplus \Omega^{*}(\partial B), \quad \phi \mapsto\left(\left(d+d^{*}\right) \phi, \iota(v) \phi\right)$$
is an elliptic boundary system in the sense of [17, 2]. Here $\iota(v)$ is contraction with $v$. By [17, Theorems 20.1.2, 20.1.8] we then have:

Proposition 4.1 For $k \geq 1$ the map (23) extends to a Fredholm operator
$$L_{k}^{2}\left(B, \Lambda_{B}^{*}\right) \rightarrow L_{k-1}^{2}\left(B, \Lambda_{B}^{*}\right) \oplus L_{k-\frac{1}{2}}^{2}\left(\partial B, \Lambda_{\partial B}^{*}\right)$$
whose kernel consists of $C^{\infty}$ forms.
Lemma 4.1 Let $X$ be a spin ${ }^{c}$ Riemannian 4-manifold and $V_{1} \subset V_{2} \subset \cdots$ precompact open subsets of $X$ such that $X=\cup_{j} V_{j}$. For $n=1,2, \ldots$ let $\mu_{n}$ be a 2 -form on $V_{n}$, and $S_{n}=\left(A_{n}, \Phi_{n}\right)$ a smooth solution to the Seiberg-Witten equations (13) over $V_{n}$ with $\mu=\mu_{n}$. Let $q>4$. Then there exist a subsequence $\left\{n_{j}\right\}$ and for each $j$ a smooth $u_{j}: V_{j} \rightarrow U(1)$ with the following significance. If $k$ is any non-negative integer such that
$$\sup _{n \geq j}\left(\left\|\Phi_{n}\right\|_{L^{q}\left(V_{j}\right)}+\left\|\hat{F}\left(A_{n}\right)\right\|_{L^{2}\left(V_{j}\right)}+\left\|\mu_{n}\right\|_{C^{k}\left(V_{j}\right)}\right)<\infty$$
for every positive integer $j$ then for every $p \geq 1$ one has that $u_{j}\left(S_{n_{j}}\right)$ converges weakly in $L_{k+1}^{p}$ and strongly in $L_{k}^{p}$ over compact subsets of $X$ as $j \rightarrow \infty$.

Before giving the proof, note that the curvature term in (24) cannot be omitted. For if $\omega$ is any non-zero, closed, anti-self-dual 2-form over the 4-ball $B$ then there is a sequence $A_{n}$ of U(1) connections over $B$ such that $F\left(A_{n}\right)=i n \omega$. If $S_{n}=\left(A_{n}, 0\right)$ then there are clearly no gauge transformations $u_{n}$ such that $u_{n}\left(S_{n}\right)$ converges (in any reasonable sense) over compact subsets of $B$.

Proof Let $B \subset X$ be a compact 4-ball. After trivializing $\mathcal{L}$ over $B$ we can write $\left.A_{n}\right|_{B}=\widetilde{d}+a_{n}$, where $\widetilde{d}$ is the spin connection over $B$ corresponding to the product connection in $\left.\mathcal{L}\right|_{B}$. By the solution of the Neumann problem (see [31]) there is a smooth $\xi_{n}: B \rightarrow i \mathbb{R}$ such that $b_{n}=a_{n}-d \xi$ satisfies
$$d^{*} b_{n}=0 ;\left.\quad * b_{n}\right|_{\partial B}=0 .$$
Using the fact that $H^{1}(B)=0$ one easily proves that the map (23) is injective on $\Omega^{1}(B)$. Hence there is a constant $C$ such that
$$\|b\|_{L_{1}^{2}(B)} \leq C\left(\left\|\left(d+d^{*}\right) b\right\|_{L^{2}(B)}+\left\|\left.* b\right|_{\partial B}\right\|_{L_{1 / 2}^{2}(\partial B)}\right)$$
for all $b \in \Omega^{1}(B)$. This gives
$$\left\|b_{n}\right\|_{L_{1}^{2}(B)} \leq C\left\|d b_{n}\right\|_{L^{2}(B)}=C\left\|\hat{F}\left(A_{n}\right)\right\|_{L^{2}(B)} .$$
Set $v_{n}=\exp \left(\xi_{n}\right)$. It is now an exercise in bootstrapping, using the Seiberg-Witten equations for $S_{n}$ and interior elliptic estimates, to show that, for every $k \geq 0$ for which (24) holds and for every $p \geq 1$, the sequence $v_{n}\left(S_{n}\right)=(d+$ $\left.b_{n}, v_{n} \Phi_{n}\right)$ is bounded in $L_{k+1}^{p}$ over compact subsets of $\operatorname{int}(B)$.
To complete the proof, choose a countable collection of such balls such that the corresponding balls of half the size cover $X$, and apply Lemma A. 1. \(\square\)

\subsection*{4.2 Small perturbations}

If $S$ is any smooth configuration over a band $(a, b) \times Y$ with $a<b$, the energy of $S$ is by definition
$$\operatorname{energy}(S)=\int_{[a, b] \times Y}\left|\nabla \vartheta_{S}\right|^{2} .$$
If $S$ is a genuine monopole then $\partial_{t} \vartheta\left(S_{t}\right)=-\int_{Y}\left|\nabla \vartheta_{S_{t}}\right|^{2}$, and so the energy equals $\vartheta\left(S_{a}\right)-\vartheta\left(S_{b}\right)$. If $S$ is a $(\mathfrak{p}, \mathfrak{q})$-monopole then one no longer expects these identities to hold, because the equation (18) is not of gradient flow type. The main object of this subsection is to show that if $\|\mathfrak{p}\|_{C^{1}}$ is sufficiently small then, under suitable assumptions, the variation of $\vartheta\left(S_{t}\right)$ still controls the energy locally (Proposition 4.2), and there is a monotonicity result for $\vartheta\left(S_{t}\right)$ (Proposition 4.3).

It may be worth mentioning that the somewhat technical Lemma 4.4 and Proposition 4.2 are not needed in the second approach to compactness which is the subject of Section 5.

In this subsection $\mathfrak{q}: \mathbb{R} \times Y \rightarrow \mathbb{R}$ may be any smooth function satisfying $\|\mathfrak{q}\|_{\infty},\|d \mathfrak{q}\|_{\infty} \leq 1$. Constants will be independent of $\mathfrak{q}$. The perturbation forms $\mathfrak{p}$ may be arbitrary elements of $\widetilde{\mathfrak{P}}$.

Lemma 4.2 There is a constant $C_{0}>0$ such that if $-\infty<a<b<\infty$ and $S=(A, \Phi)$ is any $(\mathfrak{p}, \mathfrak{q})$-monopole over $(a, b) \times Y$ then there is a pointwise bound
$$|\hat{F}(A)| \leq 2\left|\nabla \vartheta_{S}\right|+|\eta|+C_{0}|\Phi|^{2}+\gamma_{0}\|\mathfrak{p}\|_{\infty} .$$

Proof Note that both sides of the inequality are gauge invariant, and if $A$ is in temporal gauge then
$$F(A)=d t \wedge \frac{\partial A_{t}}{\partial t}+F_{Y}\left(A_{t}\right),$$
where $F_{Y}$ stands for the curvature of a connection over $Y$. Now use inequalities (18) and (16). \(\square\)

Lemma 4.3 There exists a constant $C_{1}>0$ such that for any $\tau>0$ and any $(\mathfrak{p}, \mathfrak{q})$-monopole $S$ over $(0, \tau) \times Y$ one has
$$\int_{[0, \tau] \times Y}\left|\nabla \vartheta_{S}\right|^{2} \leq 2\left(\vartheta\left(S_{0}\right)-\vartheta\left(S_{\tau}\right)\right)+C_{1}^{2} \tau\|\mathfrak{p}\|_{\infty}^{2} .$$
Recall that by convention a $(\mathfrak{p}, \mathfrak{q})$-monopole over $(0, \tau) \times Y$ is actually a configuration over $\left(-\frac{1}{2}, \tau+\frac{1}{2}\right) \times Y$, so the lemma makes sense.

Proof we may assume $S$ is in temporal gauge. Then
$$\begin{aligned}
\vartheta\left(S_{\tau}\right)-\vartheta\left(S_{0}\right) & =\int_{0}^{\tau} \partial_{t} \vartheta\left(S_{t}\right) d t \\
& =\int_{[0, \tau] \times Y}\left\langle\nabla \vartheta_{S},-\nabla \vartheta_{S}+E_{S}\right\rangle d t \\
& \leq\left\|\nabla \vartheta_{S}\right\|_{2}\left(\left\|E_{S}\right\|_{2}-\left\|\nabla \vartheta_{S}\right\|_{2}\right),
\end{aligned}$$
where the norms on the last line are taken over $[0, \tau] \times Y$. If $a, b, x$ are real numbers satisfying $x^{2}-b x-a \leq 0$ then
$$x^{2} \leq 2 x^{2}-2 b x+b^{2} \leq 2 a+b^{2} .$$
Putting this together we obtain
$$\left\|\nabla \vartheta_{S}\right\|_{2}^{2} \leq 2\left(\vartheta\left(S_{0}\right)-\vartheta\left(S_{\tau}\right)\right)+\left\|E_{S}\right\|_{2}^{2},$$
and the lemma follows from the estimate (16). \(\square\)

Lemma 4.4 For all $C>0$ there exists an $\epsilon>0$ with the following significance. Let $\tau \geq 4, \mathfrak{p} \in \widetilde{\mathfrak{P}}$ with $\|\mathfrak{p}\|_{\infty} \tau^{1 / 2} \leq \epsilon$, and let $S=(A, \Phi)$ be a $(\mathfrak{p}, \mathfrak{q})$-monopole over $(0, \tau) \times Y$ satisfying $\|\Phi\|_{\infty} \leq C$. Then at least one of the following two statements must hold:
\begin{itemize}
\item[(i)] $\partial_{t} \vartheta\left(S_{t}\right) \leq 0$ for $2 \leq t \leq \tau-2$,
\item[(ii)] $\vartheta\left(S_{t_{2}}\right)<\vartheta\left(S_{t_{1}}\right)$ for $0 \leq t_{1} \leq 1, \tau-1 \leq t_{2} \leq \tau$.
\end{itemize}

Proof Given $C>0$, suppose that for $n=1,2, \ldots$ there exist $\tau_{n} \geq 4, \mathfrak{p}_{n} \in \widetilde{\mathfrak{P}}$ with $\left\|\mathfrak{p}_{n}\right\|_{\infty} \tau_{n}^{1 / 2} \leq 1 / n$, and a $\left(\mathfrak{p}_{n}, \mathfrak{q}_{n}\right)$-monopole $S_{n}=\left(A_{n}, \Phi_{n}\right)$ over $\left(0, \tau_{n}\right) \times Y$ satisfying $\left\|\Phi_{n}\right\|_{\infty} \leq C$ such that (i) is violated at some point $t=t_{n}$ and (ii) also does not hold. By Lemma 4.3 the last assumption implies
$$\left\|\nabla \vartheta_{S_{n}}\right\|_{L^{2}\left(\left[1, \tau_{n}-1\right] \times Y\right)} \leq C_{1}\left\|\mathfrak{p}_{n}\right\|_{\infty} \tau_{n}^{1 / 2} \leq C_{1} / n .$$

For $s \in \mathbb{R}$ let $\mathcal{T}_{s}: \mathbb{R} \times Y \rightarrow \mathbb{R} \times Y$ be translation by $s$ :
$$\mathcal{T}_{s}(t, y)=(t+s, y) .$$
Given $p>2$ then by Lemmas 4.2 and 4.1 we can find $u_{n}:(-1,1) \times Y \rightarrow \mathrm{U}(1)$ in $L_{2, \text { loc }}^{p}$ such that a subsequence of $u_{n}\left(\mathcal{T}_{t_{n}}^{*}\left(S_{n}\right)\right)$ converges weakly in $L_{1}^{p}$ over $\left(-\frac{1}{2}, \frac{1}{2}\right) \times Y$ to an $L_{1}^{p}$ solution $S^{\prime}$ to the equations (13) with $\mu=\pi_{2}^{*} \eta$. Then $\nabla \vartheta_{S^{\prime}}=0$. After modifying the gauge transformations we can even arrange that $S^{\prime}$ is smooth and in temporal gauge, in which case there is a critical point $\alpha$ of $\vartheta$ such that $S^{\prime}(t) \equiv \alpha$. After relabelling the subsequence above consecutively we then have
$$h_{S_{n}}\left(t_{n}\right) \rightarrow h_{S^{\prime}}(0) \notin \Xi .$$
Since $\Xi$ is closed, $h_{S_{n}}\left(t_{n}\right) \notin \Xi$ for $n$ sufficiently large. Hence, $\left.\partial_{t}\right|_{t_{n}} \vartheta\left(S_{n}(t)\right)=$ $-\left\|\nabla \vartheta_{S_{n}\left(t_{n}\right)}\right\|^{2} \leq 0$, which is a contradiction. \(\square\)

Proposition 4.2 For any constant $C>0$ there exist $C^{\prime}, \delta>0$ such that if $S=(A, \Phi)$ is any $(\mathfrak{p}, \mathfrak{q})$-monopole over $(-2, T+4) \times Y$ where $T \geq 2,\|\mathfrak{p}\|_{\infty} \leq \delta$, and $\|\Phi\|_{\infty} \leq C$, then for $1 \leq t \leq T-1$ one has
$$\int_{[t-1, t+1] \times Y}\left|\nabla \vartheta_{S}\right|^{2} \leq 2\left(\sup _{0 \leq r \leq 1} \vartheta\left(S_{-r}\right)-\inf _{0 \leq r \leq 4} \vartheta\left(S_{T+r}\right)\right)+C^{\prime}\|\mathfrak{p}\|_{\infty}^{2} .$$

Proof Choose $\epsilon>0$ such that the conclusion of Lemma 4.4 holds (with this constant $C$ ), and set $\delta=\epsilon / \sqrt{6}$. We construct a sequence $t_{0}, \ldots, t_{m}$ of real numbers, for some $m \geq 1$, with the following properties:
\begin{itemize}
\item[(i)] $-1 \leq t_{0} \leq 0$ and $T \leq t_{m} \leq T+4$,
\item[(ii)] For $i=1, \ldots, m$ one has $1 \leq t_{i}-t_{i-1} \leq 5$ and $\vartheta\left(S_{t_{i}}\right) \leq \vartheta\left(S_{t_{i-1}}\right)$.
\end{itemize}

The lemma will then follow from Lemma 4.3 The $t_{i}$ 's will be constructed inductively, and this will involve an auxiliary sequence $t_{0}^{\prime}, \ldots, t_{m+1}^{\prime}$. Set $t_{-1}=$ $t_{0}^{\prime}=0$.

Now suppose $t_{i-1}, t_{i}^{\prime}$ have been constructed for $0 \leq i \leq j$. If $t_{j}^{\prime} \geq T$ then we set $t_{j}=t_{j}^{\prime}$ and $m=j$, and the construction is finished. If $t_{j}^{\prime}<T$ then we define $t_{j}, t_{j+1}^{\prime}$ as follows:

If $\partial_{t} \vartheta\left(S_{t}\right) \leq 0$ for all $t \in\left[t_{j}^{\prime}, t_{j}^{\prime}+2\right]$ set $t_{j}=t_{j}^{\prime}$ and $t_{j+1}^{\prime}=t_{j}^{\prime}+2$; otherwise set $t_{j}=t_{j}^{\prime}-1$ and $t_{j+1}^{\prime}=t_{j}^{\prime}+4$.

Then (i) and (ii) are satisfied, by Lemma 4.4 \(\square\)

Proposition 4.3 For all $C>0$ there exists a $\delta>0$ such that if $S=(A, \Phi)$ is any $(\mathfrak{p}, \mathfrak{q})$-monopole in temporal gauge over (-1, 1) $\times Y$ such that $\|\mathfrak{p}\|_{C^{1}} \leq \delta$, $\|\Phi\|_{\infty} \leq C$, and $\left\|\nabla \vartheta_{S}\right\|_{2} \leq C$ then the following holds: Either $\left.\partial_{t}\right|_{0} \vartheta\left(S_{t}\right)<0$, or there is a critical point $\alpha$ such that $S_{t}=\alpha$ for $|t| \leq \frac{1}{2}$.

Proof First observe that if $S$ is any $C^{1}$ configuration over $\mathbb{R} \times Y$ then
$$\vartheta\left(S_{t_{2}}\right)-\vartheta\left(S_{t_{1}}\right)=\int_{t_{1}}^{t_{2}} \int_{Y}\left\langle\nabla \vartheta_{S_{t}}, \partial_{t} S_{t}\right\rangle d y d t$$
hence $\vartheta\left(S_{t}\right)$ is a $C^{1}$ function of $t$ whose derivative can be expressed in terms of the $L^{2}$ gradient of $\vartheta$ as usual.
Now suppose there is a $C>0$ and for $n=1,2, \ldots$ a $\mathfrak{p}_{n} \in \widetilde{\mathfrak{P}}$ and a $\left(\mathfrak{p}_{n}, \mathfrak{q}_{n}\right)$ - monopole $S_{n}=\left(A_{n}, \Phi_{n}\right)$ over $(-1,1) \times Y$ such that $\left\|\mathfrak{p}_{n}\right\|_{C^{1}} \leq \frac{1}{n},\left\|\Phi_{n}\right\|_{\infty} \leq C$, $\left\|\nabla \vartheta_{S_{n}}\right\|_{2} \leq C$, and $\left.\partial_{t}\right|_{0} \vartheta\left(S_{n}(t)\right) \geq 0$. Let $p>4$ and $0<\epsilon<\frac{1}{2}$. After passing to a subsequence and relabelling consecutively we can find $u_{n}:(-1,1) \times Y \rightarrow \mathrm{U}(1)$ in $L_{3, \text { loc }}^{p}$ such that $\widetilde{S}_{n}=u_{n}\left(S_{n}\right)$ converges weakly in $L_{2}^{p}$, and strongly in $C^{1}$, over $\left(-\frac{1}{2}-\epsilon, \frac{1}{2}+\epsilon\right) \times Y$ to a smooth solution $S^{\prime}$ of (13) with $\mu=\pi_{2}^{*} \eta$. We may arrange that $S^{\prime}$ is in temporal gauge. Then
$$0 \leq\left.\partial_{t}\right|_{0} \vartheta\left(\widetilde{S}_{n}(t)\right)=\left.\int_{Y}\left\langle\nabla \vartheta_{\widetilde{S}_{n}(0)},\left.\partial_{t}\right|_{0} \widetilde{S}_{n}(t)\right\rangle \rightarrow \partial_{t}\right|_{0} \vartheta\left(S_{t}^{\prime}\right) .$$
But $S^{\prime}$ is a genuine monopole, so $\partial_{t} \vartheta\left(S_{t}^{\prime}\right)=-\left\|\nabla \vartheta_{S_{t}^{\prime}}\right\|_{2}^{2}$. It also follows that $\nabla \vartheta_{S^{\prime}(0)}=0$, hence $\nabla \vartheta_{S^{\prime}}=0$ in $\left(-\frac{1}{2}-\epsilon, \frac{1}{2}+\epsilon\right) \times Y$ by unique continuation as in [15, Appendix]. Since $h_{S_{n}} \rightarrow h_{S^{\prime}}$ uniformly in $[-\epsilon, \epsilon]$, and $h_{S^{\prime}} \equiv$ const $\notin \Xi$, the function $h_{S_{n}}$ maps $[-\epsilon, \epsilon]$ into the complement of $\Xi$ when $n$ is sufficiently large. In that case, $S_{n}$ restricts to a genuine monopole on $[-\epsilon, \epsilon] \times Y$, and the assumption $\left.\partial_{t}\right|_{0} \vartheta\left(S_{n}(t)\right) \geq 0$ implies that $\nabla \vartheta_{S_{n}}=0$ on $[-\epsilon, \epsilon] \times Y$. Since this holds for any $\epsilon \in\left(0, \frac{1}{2}\right)$, the proposition follows. \(\square\)

We say a $(\mathfrak{p}, \mathfrak{q})$-monopole $S$ over $\mathbb{R}_{+} \times Y$ has finite energy if $\inf _{t>0} \vartheta\left(S_{t}\right)>-\infty$. A monopole over a 4-manifold with tubular ends is said to have finite energy if it has finite energy over each end.

Proposition 4.4 Let $C, \delta$ be given such that the conclusion of Proposition 4.3 holds. If $S=(A, \Phi)$ is any finite energy $(\mathfrak{p}, \mathfrak{q})$-monopole over $\mathbb{R}_{+} \times Y$ with $\|\mathfrak{p}\|_{C^{1}} \leq \delta, \mathfrak{q} \equiv 1,\|\Phi\|_{\infty} \leq C$, and
$$\sup _{t \geq 1}\left\|\nabla \vartheta_{S}\right\|_{L^{2}((t-1, t+1) \times Y)} \leq C$$
then the following hold:
\begin{itemize}
\item[(i)] There is a $t>0$ such that $S$ restricts to a genuine monopole on $(t, \infty) \times Y$,
\item[(ii)] $\left[S_{t}\right]$ converges in $\mathcal{B}_{Y}$ to some critical point as $t \rightarrow \infty$.
\end{itemize}

Proof Let $p>4$. If $\left\{t_{n}\right\}$ is any sequence with $t_{n} \rightarrow \infty$ as $n \rightarrow \infty$ then by Lemmas 4.1 and 4.2 there exist $u_{n} \in L_{3, \text { loc }}^{p}(\mathbb{R} \times Y ; \mathrm{U}(1))$ such that a subsequence of $u_{n}\left(\mathcal{T}_{t_{n}}^{*} S\right)$ converges weakly in $L_{2}^{p}$ (hence strongly in $C^{1}$ ) over compact subsets of $\mathbb{R} \times Y$ to a smooth $(\mathfrak{p}, \mathfrak{q})$-monopole $S^{\prime}$ in temporal gauge. Proposition 4.3 guarantees that $\partial_{t} \vartheta\left(S_{t}\right) \leq 0$ for $t \geq 1$, so the finite energy assumption implies that $\vartheta\left(S_{t}^{\prime}\right)$ is constant. By Proposition 4.3 there is a critical point $\alpha$ such that $S_{t}^{\prime}=\alpha$ for all $t$. This implies (i) by choice of the set $\Xi$ (see Subsection 3.3). Part (ii) follows by a continuity argument from the facts that $\mathcal{B}_{Y}$ contains only finitely many critical points, and the topology on $\mathcal{B}_{Y}$ defined by the $L^{2}$-metric is weaker than the usual topology. \(\square\)

The following corollary of Lemma 3.1 shows that elements of the moduli spaces defined in Subsection 3.4 have finite energy.

Lemma 4.5 Let $S$ be a configuration over $\overline{\mathbb{R}}_{+} \times Y$ and $\alpha$ a critical point of $\vartheta$ such that $S-\underline{\alpha} \in L_{1}^{p}$ for some $p \geq 2$. Then
$$\vartheta\left(S_{t}\right) \rightarrow \vartheta(\alpha) \text { as } t \rightarrow \infty .$$

\subsection*{4.3 Neck-stretching I}

This subsection contains the crucial step in the proof of Theorem 1.4 assuming (B1), namely what should be thought of as a global energy bound.

Lemma 4.6 Let $X$ be as in Subsection 1.3 and set $Z=X_{: 1}$. We identify $Y=\partial Z$. Let $\mu_{1}, \mu_{2} \in \Omega^{2}(Z)$, where $d \mu_{1}=0$. Set $\eta=\left.\mu_{1}\right|_{Y}$ and $\mu=\mu_{1}+\mu_{2}$. Let $A_{o}$ be a spin connection over $Z$, and let the Chern-Simons-Dirac functional $\vartheta_{\eta}$ over $Y$ be defined in terms of the reference connection $B_{o}=\left.A_{o}\right|_{Y}$. Then for all configurations $S=(A, \Phi)$ over $Z$ which satisfy the monopole equations (13) one has
$$\begin{aligned}
\mid 2 \vartheta_{\eta}\left(\left.S\right|_{Y}\right)+ & \int_{Z}\left(\left|\nabla_{A} \Phi\right|^{2}+\left|\hat{F}_{A}+i \mu_{1}\right|^{2}\right) \mid \\
& \leq C \operatorname{Vol}(Z)\left(1+\|\Phi\|_{\infty}^{2}+\left\|F_{A_{o}}\right\|_{\infty}+\left\|\mu_{1}\right\|_{\infty}+\left\|\mu_{2}\right\|_{\infty}+\|\mathbf{s}\|_{\infty}\right)^{2},
\end{aligned}$$
for some universal constant $C$, where $\mathbf{s}$ is the scalar curvature of $Z$.

The upper bound given here is not optimal but suffices for our purposes.

Proof Set $F_{A}^{\prime}=\hat{F}_{A}+i \mu_{1}$ and define $F_{A_{o}}^{\prime}$ similarly. Set $B=\left.A\right|_{Y}$. Without the assumption $d \mu_{1}=0$ we have
$$\begin{aligned}
\int_{Z}\left|F_{A}^{\prime}\right|^{2} & =\int_{Z}\left(2\left|\left(F_{A}^{\prime}\right)^{+}\right|^{2}+F_{A}^{\prime} \wedge F_{A}^{\prime}\right) \\
& =\int_{Z}\left(2\left|Q(\Phi)-i \mu_{2}^{+}\right|^{2}+F_{A_{o}}^{\prime} \wedge F_{A_{o}}^{\prime}-2 i d \mu_{1} \wedge\left(A-A_{o}\right)\right) \\
& +\int_{Y}\left(\hat{F}_{B}+\hat{F}_{B_{o}}+2 i \eta\right) \wedge\left(B-B_{o}\right) .
\end{aligned}$$
Without loss of generality we may assume $A$ is in temporal gauge over the collar $\iota([0,1] \times Y)$. By the Weitzenböck formula we have
$$0=D_{A}^{2} \Phi=\nabla_{A}^{*} \nabla_{A} \Phi+\hat{F}_{A}^{+}+\frac{\mathbf{s}}{4} .$$
This gives
$$\begin{aligned}
\int_{Z}\left|\nabla_{A} \Phi\right|^{2} & =\int_{Z}\left\langle\nabla_{A}^{*} \nabla_{A} \Phi, \Phi\right\rangle+\int_{Y}\left\langle\partial_{t} \Phi, \Phi\right\rangle \\
& =\int_{Z}\left(-\frac{1}{2}|\Phi|^{4}-\frac{\mathbf{s}}{4}|\Phi|^{2}+\left\langle i \mu^{+} \Phi, \Phi\right\rangle\right)+\int_{Y}\left\langle\partial_{B} \Phi, \Phi\right\rangle .
\end{aligned}$$ \(\square\)
Consider now the situation of Subsection 1.4 If (B1) holds then we can find a closed 2-form $\mu_{1}$ on $X$ whose restriction to $\mathbb{R}_{+} \times\left( \pm Y_{j}\right)$ is the pull-back of $\eta_{j}$, and whose restriction to $\mathbb{R}_{+} \times Y_{j}^{\prime}$ is the pull-back of $\eta_{j}^{\prime}$. From Lemma 4.6 we deduce:

Proposition 4.5 For every constant $C_{1}<\infty$ there exists a constant $C_{2}<\infty$ with the following significance. Suppose we are given
\begin{itemize}
\item[-] $\tau, C_{0}<\infty$ and an $r$-tuple $T$ such that $\tau \leq T_{j}$ for each $j$,
\item[-] real numbers $\tau_{j}^{ \pm}, 1 \leq j \leq r$ and $\tau_{j}^{\prime}, 1 \leq j \leq r^{\prime}$ satisfying $0 \leq T_{j}-\tau_{j}^{ \pm} \leq \tau$ and $0 \leq \tau_{j}^{\prime} \leq \tau$.
\end{itemize}
Let $Z$ be the result of deleting from $X^{(T)}$ all the necks $\left(-\tau_{j}^{-}, \tau_{j}^{+}\right) \times Y_{j}, 1 \leq j \leq r$ and all the ends $\left(\tau_{j}^{\prime}, \infty\right) \times Y_{j}^{\prime}, 1 \leq j \leq r^{\prime}$. Then for any configuration $S=$ $(A, \Phi)$ representing an element of a moduli space $M\left(X^{(T)} ; \vec{\alpha}^{\prime} ; \mu ; \overrightarrow{\mathfrak{p}}, \overrightarrow{\mathfrak{p}}^{\prime}\right)$ where
$\sum_{j=1}^{r^{\prime}} \vartheta\left(\alpha_{j}^{\prime}\right)>-C_{0}$ and $\mathfrak{p}_{j}, \mathfrak{p}_{j}^{\prime}, \mu$ all have $L^{\infty}$ norm $<C_{1}$ one has that
$$\begin{aligned}
\int_{Z}\left(\left|\nabla_{A} \Phi\right|^{2}+\left|\hat{F}_{A}+i \mu_{1}\right|^{2}\right) & +2 \sum_{j=1}^{r}\left(\vartheta\left(\left.S\right|_{\left\{-\tau_{j}^{-}\right\} \times Y_{j}}\right)-\vartheta\left(\left.S\right|_{\left\{\tau_{j}^{+}\right\} \times Y_{j}}\right)\right) \\
& +2 \sum_{j=1}^{r^{\prime}}\left(\vartheta\left(\left.S\right|_{\left\{\tau_{j}^{\prime}\right\} \times Y_{j}^{\prime}}\right)-\vartheta\left(\alpha_{j}^{\prime}\right)\right)<C_{2}(1+\tau)+2 C_{0} .
\end{aligned}$$
Thus, if each $\mathfrak{p}_{j}, \mathfrak{p}_{j}^{\prime}$ has sufficiently small $L^{\infty}$ norm then Lemma 4.5 and Proposition 4.2 provides local energy bounds over necks and ends for such monopoles. (To apply Proposition 4.2 one can take $\tau_{j}^{ \pm}$to be the point $t$ in a suitable interval where $\pm \vartheta\left(\left.S\right|_{\{t\} \times Y_{j}}\right)$ attains its maximum, and similarly for $\tau_{j}^{\prime}$.) Moreover, if these perturbation forms have sufficiently small $C^{1}$ norms then we can apply Proposition 4.3 over necks and ends. (How small the $C^{1}$ norms have to be depends on $C_{0}$.)

\section*{5 Local compactness II}

This section, which is logically independent from Section 4 provides the local compactness results needed for the proof of Theorem 1.4 assuming (B2).

While the main result of this section, Proposition 5.5, is essentially concerned with local convergence of monopoles, the arguments will, in contrast to those of Section 4, be of a global nature. In particular, function spaces over manifolds with tubular ends will play a central role.

\subsection*{5.1 Hodge theory for the operator $-d^{*}+d^{+}$}

In this subsection we will study the kernel (in certain function spaces) of the elliptic operator
$$\mathcal{D}=-d^{*}+d^{+}: \Omega^{1}(X) \rightarrow \Omega^{0}(X) \oplus \Omega^{+}(X),$$
where $X$ is an oriented Riemannian 4-manifold with tubular ends. The notation $\operatorname{ker}(\mathcal{D})$ will refer to the kernel of $\mathcal{D}$ in the space $\Omega^{1}(X)$ of all smooth 1-forms, where $X$ will be understood from the context. The results of this subsection complement those of [10].

We begin with the case of a half-infinite cylinder $X=\mathbb{R}_{+} \times Y$, where $Y$ is any closed, oriented, connected Riemannian 3-manifold. Under the isomorphisms
(14) there is the identification $\mathcal{D}=\frac{\partial}{\partial t}+P$ over $\mathbb{R}_{+} \times Y$, where $P$ is the self-adjoint elliptic operator
$$P=\left(\begin{array}{cc}
0 & -d^{*} \\
-d & * d
\end{array}\right)$$
acting on sections of $\Lambda^{0}(Y) \oplus \Lambda^{1}(Y)$ (cf (22)). Since $P^{2}$ is the Hodge Laplacian,
$$\operatorname{ker}(P)=H^{0}(Y) \oplus H^{1}(Y) .$$
Let $\left\{h_{\nu}\right\}$ be a maximal orthonormal set of eigenvectors of $P$, say $P h_{\nu}=\lambda_{\nu} h_{\nu}$.
Given a smooth 1-form $a$ over $\mathbb{R}_{+} \times Y$ we can express it as $a=\sum_{\nu} f_{\nu} h_{\nu}$, where $f_{\nu}: \mathbb{R}_{+} \rightarrow \mathbb{R}$. If $\mathcal{D} a=0$ then $f_{\nu}(t)=c_{\nu} e^{-\lambda_{\nu} t}$ for some constant $c_{\nu}$. If in addition $a \in L^{p}$ for some $p \geq 1$ then $f_{\nu} \in L^{p}$ for all $\nu$, hence $f_{\nu} \equiv 0$ when $\lambda_{\nu} \leq 0$. Elliptic inequalities for $\mathcal{D}$ then show that $a$ decays exponentially, or more precisely,
$$\left|\left(\nabla^{j} a\right)_{(t, y)}\right| \leq \beta_{j} e^{-\delta t}$$
for $(t, y) \in \mathbb{R}_{+} \times Y$ and $j \geq 0$, where $\beta_{j}$ is a constant and $\delta$ the smallest positive eigenvalue of $P$.

Now let $\sigma>0$ be a small constant and $a \in \operatorname{ker}(\mathcal{D}) \cap L^{p,-\sigma}$. Arguing as above we find that
$$a=b+c d t+\pi^{*} \psi,$$
where $b$ is an exponentially decaying form, $c$ a constant, $\pi: \mathbb{R}_{+} \times Y \rightarrow Y$, and $\psi \in \Omega^{1}(Y)$ harmonic.

We now turn to the case when $X$ is an oriented, connected Riemannian 4-manifold with tubular end $\overline{\mathbb{R}}_{+} \times Y$ (so $X \backslash \mathbb{R}_{+} \times Y$ is compact). Let $Y_{1}, \ldots, Y_{r}$ be the connected components of $Y$ and set
$$Y^{\prime}=\bigcup_{j=1}^{s} Y_{j}, \quad Y^{\prime \prime}=Y \backslash Y^{\prime},$$
where $0 \leq s \leq r$. Let $\sigma>0$ be a small constant and $\kappa: X \rightarrow \mathbb{R}$ a smooth function such that
$$\kappa= \begin{cases}-\sigma t & \text { on } \mathbb{R}_{+} \times Y^{\prime} \\ \sigma t & \text { on } \mathbb{R}_{+} \times Y^{\prime \prime},\end{cases}$$
where $t$ is the $\mathbb{R}_{+}$coordinate. Our main goal in this subsection is to describe $\operatorname{ker}(\mathcal{D}) \cap L^{p, \kappa}$.

We claim that all elements $a \in \operatorname{ker}(\mathcal{D}) \cap L^{p, \kappa}$ are closed. To see this, note first that the decomposition (26) shows that $a$ is pointwise bounded, and $d a$ decays
exponentially over the ends. Applying the proof of [11, Proposition 1.1.19] to $X_{: T}=X \backslash(T, \infty) \times Y$ we get
$$\begin{aligned}
\int_{X_{: T}}\left(\left|d^{+} a\right|^{2}-\left|d^{-} a\right|^{2}\right) & =\int_{X_{: T}} d a \wedge d a=\int_{X_{: T}} d(a \wedge d a) \\
& =\int_{\partial X_{: T}} a \wedge d a \rightarrow 0 \quad \text { as } T \rightarrow \infty .
\end{aligned}$$
Since $d^{+} a=0$, we conclude that $d a=0$.
Fix $\tau \geq 0$ and for any $a \in \Omega^{1}(X)$ and $j=1, \ldots, r$ set
$$R_{j} a=\int_{\{\tau\} \times Y_{j}} * a .$$
Recall that $d^{*}=-* d *$ on 1-forms, so if $d^{*} a=0$ then $R_{j} a$ is independent of $\tau$. Therefore, if $a \in \operatorname{ker}(\mathcal{D}) \cap L^{p, \kappa}$ then $R_{j} a=0$ for $j>s$, hence
$$\sum_{j=1}^{s} R_{j} a=\int_{\partial X_{: \tau}} * a=\int_{X_{: \tau}} d * a=0$$
Set
$$\Xi=\left\{\left(z_{1}, \ldots, z_{s}\right) \in \mathbb{R}^{s}: \sum_{j} z_{j}=0\right\} .$$

Proposition 5.1 In the situation above the map
$$\begin{aligned}
\alpha: \operatorname{ker}(\mathcal{D}) \cap L^{p, \kappa} & \rightarrow \operatorname{ker}\left(H^{1}(X) \rightarrow H^{1}\left(Y^{\prime \prime}\right)\right) \oplus \Xi, \\
a & \mapsto\left([a],\left(R_{1} a, \ldots, R_{s} a\right)\right)
\end{aligned}$$
is an isomorphism.

Proof We first prove $\alpha$ is injective. Suppose $\alpha(a)=0$. Then $a=d f$ for some function $f$ on $X$. From the decomposition (26) we see that $a$ decays exponentially over the ends. Hence $f$ is bounded, in which case
$$0=\int_{X} f d^{*} a=\int_{X}|a|^{2} .$$
This shows $\alpha$ is injective.
Next we prove $\alpha$ is surjective. Suppose $b \in \Omega^{1}(X), d b=0,\left[\left.b\right|_{Y^{\prime \prime}}\right]=0$, and $\left(z_{1}, \ldots, z_{s}\right) \in \Xi$. Let $\psi \in \Omega^{1}(Y)$ be the harmonic form representing $\left[\left.b\right|_{Y}\right] \in H^{1}(Y)$. Then
$$\left.b\right|_{\mathbb{R}_{+} \times Y}=\pi^{*} \psi+d f,$$
for some $f: \mathbb{R}_{+} \times Y \rightarrow \mathbb{R}$. Choose a smooth function $\rho: X \rightarrow \mathbb{R}$ which vanishes in a neighbourhood of $X_{: 0}$ and satisfies $\rho \equiv 1$ on $[\tau, \infty) \times Y$. Set $z_{j}=0$ for $j>s$ and let $z$ be the function on $Y$ with $\left.z\right|_{Y_{j}} \equiv \operatorname{Vol}\left(Y_{j}\right)^{-1} z_{j}$. Define
$$\widetilde{b}=b+d(\rho(t z-f)) .$$
Then over $[\tau, \infty) \times Y$ we have $\widetilde{b}=\pi^{*} \psi+z d t$, so $d^{*} \widetilde{b}=0$ in this region, and
$$\int_{X} d^{*} \widetilde{b}=-\int_{\partial X_{: \tau}} * \widetilde{b}=-\int_{Y} z=0$$
Let $\bar{\kappa}: X \rightarrow \mathbb{R}$ be a smooth function which agrees with $|\kappa|$ outside a compact set. By Proposition 2.3 we can find a smooth $\xi: X \rightarrow \mathbb{R}$ such that $d \xi \in L_{1}^{p, \bar{\kappa}}$ and
$$d^{*}(\widetilde{b}+d \xi)=0 .$$
Set $a=\widetilde{b}+d \xi$. Then $\left(d+d^{*}\right) a=0$ and $\alpha(a)=\left([b],\left(z_{1}, \ldots, z_{s}\right)\right)$. \(\square\)

The following proposition is essentially [10, Proposition 3.14] and is included here only for completeness.

Proposition 5.2 If $b_{1}(Y)=0$ and $s=0$ then the operator
$$\mathcal{D}: L_{1}^{p, \kappa} \rightarrow L^{p, \kappa}$$
has index $-b_{0}(X)+b_{1}(X)-b_{2}^{+}(X)$.
Proof By Proposition 5.1 the dimension of the kernel of (28) is $b_{1}(X)$. From Proposition 2.2 (ii) with $\mathbb{S}=0$ we see that the image of (28) is the sum of $d^{*} L_{1}^{p, \kappa}$ and $d^{+} L_{1}^{p, \kappa}$. The codimensions of these spaces in $L^{p, \kappa}$ are $b_{0}(X)$ and $b_{2}^{+}(X)$, respectively. \(\square\)

\subsection*{5.2 The case of a single moduli space}

Consider the situation of Subsection 1.3. Initially we do not assume Condition (A).

Proposition 5.3 Fix $1<q<\infty$. Let $\sigma>0$ be a small constant and $\kappa: X \rightarrow \mathbb{R}$ a smooth function such that $\kappa(t, y)=-\sigma t$ for all $(t, y) \in \mathbb{R}_{+} \times Y$. Let $A_{o}$ be a spin connection over $X$ which is translationary invariant over the ends of $X$. For $n=1,2, \ldots$ let $S_{n}=\left(A_{o}+a_{n}, \Phi_{n}\right)$ be a smooth configuration over $X$ which satisfies the monopole equations (20) with $\mu=\mu_{n}, \overrightarrow{\mathfrak{p}}=\overrightarrow{\mathfrak{p}}_{n}$.

Suppose $a_{n} \in L_{1}^{q, \kappa}$ for every $n$, and $\sup _{n}\left\|\Phi_{n}\right\|_{\infty}<\infty$. Then there exist smooth $u_{n}: X \rightarrow U(1)$ such that if $k$ is any non-negative integer with
$$\sup _{j, n}\left(\left\|\mu_{n}\right\|_{C^{k}}+\left\|\mathfrak{p}_{n, j}\right\|_{C^{k}}\right)<\infty$$
then the sequence $u_{n}\left(S_{n}\right)$ is bounded in $L_{k+1}^{p^{\prime}}$ over compact subsets of $X$ for every $p^{\prime} \geq 1$.

Before giving the proof we record the following two elementary lemmas:

Lemma 5.1 Let $E, F, G$ be Banach spaces, and $E \xrightarrow{S} F$ and $E \xrightarrow{T} G$ bounded linear maps. Set
$$S+T: E \rightarrow F \oplus G, \quad x \mapsto(S x, T x) .$$
Suppose $S$ has finite-dimensional kernel and closed range, and that $S+T$ is injective. Then $S+T$ has closed range, hence there is a constant $C>0$ such that
$$\|x\| \leq C(\|S x\|+\|T x\|)$$
for all $x \in E$.

Proof Exercise. \(\square\)

Lemma 5.2 Let $X$ be a smooth, connected manifold and $x_{0} \in X$. Let $\operatorname{Map}_{0}(X, U(1))$ denote the set of smooth maps $u: X \rightarrow U(1)$ such that $u\left(x_{0}\right)=$ 1, and let $V$ denote the set of all closed 1 -forms $\phi$ on $X$ such that $[\phi] \in$ $H^{1}(X ; \mathbb{Z})$. Then
$$\operatorname{Map}_{0}(X, U(1)) \rightarrow V, \quad u \mapsto \frac{1}{2 \pi i} u^{-1} d u$$
is an isomorphism of Abelian groups.

Proof If $\phi \in V$ define
$$u(x)=\exp \left(2 \pi i \int_{x_{0}}^{x} \phi\right),$$
where $\int_{x_{0}}^{x} \phi$ denotes the integral of $\phi$ along any path from $x_{0}$ to $x$. Then $\frac{1}{2 \pi i} u^{-1} d u=\phi$. The details are left to the reader. \(\square\)

Proof of Proposition 5.3 We may assume $X$ is connected and that (29) holds at least for $k=0$. Choose closed 3-forms $\omega_{1}, \ldots, \omega_{b_{1}(X)}$ which are supported in the interior of $X_{: 0}$ and represent a basis for $H_{c}^{3}(X)$. For any $a \in \Omega^{1}(X)$ define the coordinates of $J a \in \mathbb{R}^{b_{1}(X)}$ by
$$(J a)_{k}=\int_{X} a \wedge \omega_{k} .$$
Then $J$ induces an isomorphism $H^{1}(X) \rightarrow \mathbb{R}^{b_{1}(X)}$, by Poincaré duality. By Lemma 5.2 we can find smooth $v_{n}: X \rightarrow \mathrm{U}(1)$ such that $J\left(a_{n}-v_{n}^{-1} d v_{n}\right)$ is bounded as $n \rightarrow \infty$. We can arrange that $v_{n}(t, y)$ is independent of $t \geq 0$ for every $y \in Y$. Then there are $\xi_{n} \in L_{2}^{q, \kappa}(X ; i \mathbb{R})$ such that $b_{n}=a_{n}-v_{n}^{-1} d v_{n}-d \xi_{n}$ satisfies
$$d^{*} b_{n}=0 ; \quad R_{j} b_{n}=0, \quad j=1, \ldots, r-1$$
where $R_{j}$ is as in (27). If $r \geq 1$ this follows from Proposition 2.4 while if $r=0$ (ie if $X$ is closed) it follows from Proposition 2.3. (By Stokes' theorem we have $R_{r} b_{n}=0$ as well, but we don't need this.) Note that $\xi_{n}$ must be smooth, by elliptic regularity for the Laplacian $d^{*} d$. Set $u_{n}=\exp \left(\xi_{n}\right) v_{n}$. Then $u_{n}\left(A_{o}+a_{n}\right)=A_{o}+b_{n}$. By Proposition 5.1 and Lemma 5.1 there is a $C_{1}>0$ such that
$$\|b\|_{L_{1}^{q, \kappa}} \leq C_{1}\left(\left\|\left(d^{*}+d^{+}\right) b\right\|_{L^{q, \kappa}}+\sum_{j=1}^{r-1}\left|R_{j} b\right|+\|J b\|\right)$$
for all $b \in L_{1}^{q, \kappa}$. From inequality (16) and the curvature part of the Seiberg-Witten equations we find that $\sup _{n}\left\|d^{+} b_{n}\right\|_{\infty}<\infty$, hence
$$\left\|b_{n}\right\|_{L_{1}^{q, \kappa}} \leq C_{1}\left(\left\|d^{+} b_{n}\right\|_{L^{q, \kappa}}+\left\|J b_{n}\right\|\right) \leq C_{2}$$
for some constant $C_{2}$. We can now complete the proof by bootstrapping over compact subsets of $X$, using alternately the Dirac and curvature parts of the Seiberg-Witten equation. \(\square\)

Combining Proposition 5.3 (with $k \geq 1$ ) and Proposition 3.1 we obtain, for fixed closed 2-forms $\eta_{j}$ on $Y_{j}$ :

Corollary 5.1 If (A) holds then for every constant $C_{0}<\infty$ there exists a constant $C_{1}<\infty$ with the following significance. Suppose $\|\mu\|_{C^{1}},\left\|\mathfrak{p}_{j}\right\|_{C^{1}} \leq C_{0}$ for each $j$. Then for any $\vec{\alpha}=\left(\alpha_{1}, \ldots, \alpha_{r}\right)$ with $\alpha_{j} \in \widetilde{\mathcal{R}}_{Y_{j}}$, and any $[S] \in$ $M(X ; \vec{\alpha} ; \mu ; \overrightarrow{\mathfrak{p}})$ and $t_{1}, \ldots, t_{r} \in\left[0, C_{0}\right]$ one has
$$\left|\sum_{j=1}^{r} \lambda_{j} \vartheta\left(\left.S\right|_{\left\{t_{j}\right\} \times Y_{j}}\right)\right| \leq C_{1} .$$

Note that if $\sum_{j} \lambda_{j} \vartheta\left(\alpha_{j}\right) \geq-C_{0}$ then this gives
$$\sum_{j=1}^{r} \lambda_{j}\left(\vartheta\left(\left.S\right|_{\left\{t_{j}\right\} \times Y_{j}}\right)-\vartheta\left(\alpha_{j}\right)\right) \leq C_{0}+C_{1} .$$

\subsection*{5.3 Condition (C)}

Consider the situation in Subsection 1.4 and suppose $\gamma$ is simply-connected and equipped with an orientation $o$. Throughout this subsection (and the next) (co)homology groups will have real coefficients, unless otherwise indicated.

We associate to $(\gamma, o)$ a "height function", namely the unique integer valued function $h$ on the set of nodes of $\gamma$ whose minimum value is 0 and which satisfies $h\left(e^{\prime}\right)=h(e)+1$ whenever there is an oriented edge from $e$ to $e^{\prime}$.

Let $Z^{k}$ and $Z^{[k}$ denote the union of all subspaces $Z_{e} \subset X^{\#}$ where $e$ has height $k$ and $\geq k$, respectively. Set
$$\partial^{-} Z^{k}=\bigcup_{h(e)=k} \partial^{-} Z_{e} .$$
For each node $e$ of $\gamma$ choose a subspace $G_{e} \subset H_{1}\left(Z_{e}\right)$ such that
$$H_{1}\left(Z_{e}\right)=G_{e} \oplus \operatorname{im}\left(H_{1}\left(\partial^{-} Z_{e}\right) \rightarrow H_{1}\left(Z_{e}\right)\right) .$$
Then the natural map $F_{e} \rightarrow G_{e}^{*}$ is an isomorphism, where $G_{e}^{*}$ is the dual of the vector space $G_{e}$.

Lemma 5.3 The natural map $H^{1}\left(X^{\#}\right) \rightarrow \oplus_{e} G_{e}^{*}$ is injective. Therefore, this map is an isomorphism if and only if $\Sigma(X, \gamma, o)=0$.

Proof Let $N$ be the maximum value of $h$ and suppose $z \in H^{1}\left(X^{\#}\right)$ lies in the kernel of the map in the lemma. It is easy to show, by induction on $k=0, \ldots, N$, that $H^{1}\left(X^{\#}\right) \rightarrow H^{1}\left(Z^{k}\right)$ maps $z$ to zero for each $k$. We now invoke the Mayer-Vietoris sequence for the pair of subspaces $\left(Z^{k-1}, Z^{[k}\right)$ of $X^{\#}$ :
$$H^{0}\left(Z^{k-1}\right) \oplus H^{0}\left(Z^{[k}\right) \xrightarrow{a} H^{0}\left(\partial^{-} Z^{k}\right) \rightarrow H^{1}\left(Z^{[k-1}\right) \xrightarrow{b} H^{1}\left(Z^{k-1}\right) \oplus H^{1}\left(Z^{[k}\right) .$$
Using the fact that $\gamma$ is simply-connected it is not hard to see that $a$ is surjective, hence $b$ is injective. Arguing by induction on $k=N, N-1, \ldots, 0$ we then find that $H^{1}\left(X^{\#}\right) \rightarrow H^{1}\left(Z^{[k}\right)$ maps $z$ to zero for each $k$. \(\square\)

We will now formulate a condition on $(X, \gamma)$ which is stronger than (C) and perhaps simpler to verify. A connected, oriented graph is called a tree if it has a unique node (the root node) with no incoming edge, and any other node has a unique incoming edge.

Proposition 5.4 Suppose there is an orientation $o$ of $\gamma$ such that $(\gamma, o)$ is a tree and
$$H^{1}\left(Z^{[k}\right) \rightarrow H^{1}\left(Z^{k}\right)$$
is surjective for all $k$. Then Condition $(C)$ holds.

Proof It suffices to verify that $\Sigma(X, \gamma, o)=0$. Set
$$\begin{aligned}
& F^{[k}=\operatorname{ker}\left(H^{1}\left(Z^{[k}\right) \rightarrow H^{1}\left(\partial^{-} Z^{k}\right)\right), \\
& F^{k}=\operatorname{ker}\left(H^{1}\left(Z^{k}\right) \rightarrow H^{1}\left(\partial^{-} Z^{k}\right)\right) .
\end{aligned}$$
The Mayer-Vietoris sequence for $\left(Z^{k}, Z^{[k+1}\right)$ yields an exact sequence
$$0 \rightarrow F^{[k} \rightarrow F^{k} \oplus H^{1}\left(Z^{[k+1}\right) \rightarrow H^{1}\left(\partial^{-} Z^{[k+1}\right) .$$
If $H^{1}\left(Z^{[k}\right) \rightarrow H^{1}\left(Z^{k}\right)$ is surjective then so is $F^{[k} \rightarrow F^{k}$, hence $\operatorname{ker}\left(F^{[k} \rightarrow\right.$ $\left.F^{k}\right) \rightarrow F^{[k+1}$ is an isomorphism, in which case
$$\operatorname{dim} F^{[k}=\operatorname{dim} F^{[k+1}+\operatorname{dim} F^{k} .$$
Therefore,
$$\Sigma(X, \gamma, o)=\operatorname{dim} H^{1}\left(X^{\#}\right)-\sum_{k} \operatorname{dim} F^{k}=\operatorname{dim} H^{1}\left(X^{\#}\right)-\operatorname{dim} F^{[0}=0 .$$ \(\square\)

\subsection*{5.4 Neck-stretching II}

Consider again the situation in Subsection 1.4. The following set-up will be used in the next two lemmas. We assume that $\gamma$ is simply-connected and that $o$ is an orientation of $\gamma$ with $\Sigma(X, \gamma, o)=0$. Let $1<p<\infty$.

An end of $X$ that corresponds to an edge of $\gamma$ is either incoming or outgoing depending on the orientation $o$. (These are the ends $\mathbb{R}_{+} \times\left( \pm Y_{j}\right)$, but the sign here is unrelated to $o$.) All other ends (ie $\mathbb{R}_{+} \times Y_{j}^{\prime}, 1 \leq j \leq r^{\prime}$ ) are called neutral.

Choose subspaces $G_{e}$ of $H_{1}\left(Z_{e}\right) \approx H_{1}\left(X_{e}\right)$ as in the previous subsection, and set $g_{e}=\operatorname{dim} G_{e}$. For each component $X_{e}$ of $X$ let $\left\{q_{e k}\right\}$ be a collection of closed 3-forms on $X_{e}$ supported in the interior of $Z_{e}^{\prime}=\left(X_{e}\right)_{: 0}$ which represents
a basis for the image of $G_{e}$ in $H_{c}^{3}\left(X_{e}\right)$ under the Poincaré duality isomorphism. For any $a \in \Omega^{1}\left(Z_{e}^{\prime}\right)$ define $J_{e} a \in \mathbb{R}^{g_{e}}$ by
$$\left(J_{e} a\right)_{k}=\int_{X_{e}} a \wedge q_{e k} .$$
For each $e$ let $\mathbb{R}_{+} \times Y_{e m}, m=1, \ldots, h_{e}$ be the outgoing ends of $X_{e}$. For any $a \in \Omega^{1}\left(Z_{e}^{\prime}\right)$ define $R_{e} a \in \mathbb{R}^{h_{e}}$ by
$$\left(R_{e} a\right)_{m}=\int_{\{0\} \times Y_{e m}} * a .$$
Set $n_{e}=g_{e}+h_{e}$ and
$$L_{e} a=\left(J_{e} a, R_{e} a\right) \in \mathbb{R}^{n_{e}} .$$
For any $a \in \Omega^{1}\left(X^{(T)}\right)$ let $L a \in V=\oplus_{e} \mathbb{R}^{n_{e}}$ be the element with components $L_{e} a$.

For any tubular end $\mathbb{R}_{+} \times P$ of $X$ let $t: \mathbb{R}_{+} \times P \rightarrow \mathbb{R}_{+}$be the projection. Choose a small $\sigma>0$ and for each $e$ a smooth function $\kappa_{e}: X_{e} \rightarrow \mathbb{R}$ such that
$$\kappa_{e}= \begin{cases}\sigma t & \text { on incoming ends, } \\ -\sigma t & \text { on outgoing and neutral ends. }\end{cases}$$
Let $X^{\{T\}} \subset X$ be as in Subsection 1.4 and let $\kappa=\kappa_{T}: X^{(T)} \rightarrow \mathbb{R}$ be a smooth function such that $\kappa_{T}-\kappa_{e}$ is constant on $X_{e} \cap X^{\{T\}}$ for each $e$. (Such a function exists because $\gamma$ is simply-connected.) This determines $\kappa_{T}$ up to an additive constant.

Fix a point $x_{e} \in X_{e}$ and define a norm $\|\cdot\|_{T}$ on $V$ by
$$\|v\|_{T}=\sum_{e} \exp \left(\kappa_{T}\left(x_{e}\right)\right)\left\|v_{e}\right\|,$$
where $\|\cdot\|$ is the Euclidean norm on $R^{n_{e}}$ and $\left\{v_{e}\right\}$ the components of $v$.
Let $\mathcal{D}$ denote the operator $-d^{*}+d^{+}$on $X^{(T)}$.

Lemma 5.4 There is a constant $C$ such that for every $r$-tuple $T$ with $\min _{j} T_{j}$ sufficiently large and every $L_{1}^{p, \kappa} 1$-form a on $X^{(T)}$ we have
$$\|a\|_{L_{1}^{p, \kappa}} \leq C\left(\|\mathcal{D} a\|_{L^{p, \kappa}}+\|L a\|_{T}\right) .$$
Note that adding a constant to $\kappa$ rescales all norms in the above inequality by the same factor.

Proof Let $\tau$ be a function on $X$ which is equal to $2 T_{j}$ on the ends $\mathbb{R}_{+} \times\left( \pm Y_{j}\right)$ for each $j$. Choose smooth functions $f_{1}, f_{2}: \mathbb{R} \rightarrow \mathbb{R}$ such that $\left(f_{1}(t)\right)^{2}+\left(f_{2}(1-\right.$ $t))^{2}=1$ for all $t$, and $f_{k}(t)=1$ for $t \leq \frac{1}{3}, k=1,2$. For each $e$ define $\beta_{e}: X_{e} \rightarrow \mathbb{R}$ by
$$\beta_{e}= \begin{cases}f_{1}(t / \tau) & \text { on outgoing ends }, \\ f_{2}(t / \tau) & \text { on incoming ends, } \\ 1 & \text { elsewhere. }\end{cases}$$
Let $\bar{\beta}_{e}$ denote the smooth function on $X^{(T)}$ which agrees with $\beta_{e}$ on $X_{e} \cap X^{\{T\}}$ and is zero elsewhere.

In the following, $C, C_{1}, C_{2} \ldots$ will be constants that are independent of $T$. Set $\check{T}=\min _{j} T_{j}$. Assume $\check{T} \geq 1$.
Note that $\left|\nabla \beta_{e}\right| \leq C_{1} \check{T}^{-1}$ everywhere, and similarly for $\bar{\beta}_{e}$. Therefore
$$\left\|\beta_{e} a\right\|_{L_{1}^{p, \kappa_{e}}} \leq C_{2}\|a\|_{L_{1}^{p, \kappa_{e}}}$$
for 1-forms $a$ on $X_{e}$.
Let $\mathcal{D}_{e}$ denote the operator $-d^{*}+d^{+}$on $X_{e}$. By Proposition 5.1 the Fredholm operator
$$\mathcal{D}_{e} \oplus L_{e}: L_{1}^{p, \kappa_{e}} \rightarrow L^{p, \kappa_{j}} \oplus \mathbb{R}^{n_{e}}$$
is injective, hence it has a bounded left inverse $P_{e}$,
$$P_{e}\left(\mathcal{D}_{e} \oplus L_{e}\right)=\mathrm{Id} .$$
If $a$ is a 1-form on $X^{(T)}$ and $v \in V$ set
$$\bar{\beta}_{e}(a, v)=\left(\bar{\beta}_{e} a, v_{e}\right) .$$
Here we regard $\bar{\beta}_{e} a$ as a 1 -form on $X_{e}$. Define
$$P=\sum_{e} \beta_{e} P_{e} \bar{\beta}_{e}: L^{p, \kappa} \oplus V \rightarrow L_{1}^{p, \kappa} .$$
If we use the norm $\|\cdot\|_{T}$ on $V$ then $\|P\| \leq C_{3}$. Now
$$\begin{aligned}
P(\mathcal{D} \oplus L) a & =\sum_{e} \beta_{e} P_{e}\left(\bar{\beta}_{e} \mathcal{D} a, L_{e} a\right) \\
& =\sum_{e} \beta_{e} P_{e}\left(\mathcal{D}_{e} \bar{\beta}_{e} a+\left[\bar{\beta}_{e}, \mathcal{D}\right] a, L_{e} \bar{\beta}_{e} a\right) \\
& =\sum_{e}\left(\beta_{e} \bar{\beta}_{e} a+\beta_{e} P_{e}\left(\left[\bar{\beta}_{e}, \mathcal{D}\right] a, 0\right)\right) \\
& =a+E a,
\end{aligned}$$
where
$$\|E a\|_{L_{1}^{p, \kappa}} \leq C_{4} \check{T}^{-1}\|a\|_{L^{p, \kappa}} .$$
Therefore,
$$\|P(\mathcal{D} \oplus L)-I\| \leq C_{4} \check{T}^{-1},$$
so if $\check{T}>C_{4}$ then $z=P(\mathcal{D} \oplus L)$ will be invertible, with
$$\left\|z^{-1}\right\| \leq(1-\|z-I\|)^{-1} .$$
In that case we can define a left inverse of $\mathcal{D} \oplus L$ by
$$Q=(P(\mathcal{D} \oplus L))^{-1} P .$$
If $\check{T} \geq 2 C_{4}$ say, then $\|Q\| \leq 2 C_{3}$, whence for any $a \in L_{1}^{p, \kappa}$ we have
$$\|a\|_{L_{1}^{p, \kappa}}=\|Q(\mathcal{D} a, L a)\|_{L_{1}^{p, \kappa}} \leq C\left(\|\mathcal{D} a\|_{L^{p, \kappa}}+\|L a\|_{T}\right) .$$ \(\square\)

Lemma 5.5 Let $e$ be a node of $\gamma$ and for $n=1,2, \ldots$ let $T(n)$ be an $r$-tuple and $a_{n}$ an $L_{1}^{p, \kappa_{n}} 1$-form on $X^{(T(n))}$, where $\kappa_{n}=\kappa_{T(n)}$. Suppose
\begin{itemize}
\item[(i)] $\Sigma(X, \gamma, o)=0$,
\item[(ii)] $\min _{j} T_{j}(n) \rightarrow \infty$ as $n \rightarrow \infty$,
\item[(iii)] There is a constant $C^{\prime}<\infty$ such that
$$\kappa_{n}\left(x_{e^{\prime}}\right) \leq \kappa_{n}\left(x_{e}\right)+C^{\prime}$$
for all nodes $e^{\prime}$ of $\gamma$ and all $n$,
\item[(iv)] $\sup _{n}\left\|d^{+} a_{n}\right\|_{\infty}<\infty$.
\end{itemize}
Then there are smooth $u_{n}: X^{(T(n))} \rightarrow U(1)$ such that the sequence $b_{n}=$ $a_{n}-u_{n}^{-1} d u_{n}$ is bounded in $L_{1}^{p}$ over compact subsets of $X_{e}$, and $b_{n} \in L_{1}^{p, \kappa_{n}}$ and $d^{*} b_{n}=0$ for every $n$.

Note that (iii) implies that $e$ must be a source of $(\gamma, o)$.
Proof Without loss of generality we may assume that $\kappa_{n}\left(x_{e}\right)=1$ for all $n$, in which case
$$\sup _{n}\|1\|_{L^{p, \kappa_{n}}}<\infty .$$
By Lemmas 5.2 and 5.3 we can find smooth $v_{n}: X^{(T(n))} \rightarrow \mathrm{U}(1)$ such that
$$\sup _{n}\left\|J_{e^{\prime}}\left(a_{n}-v_{n}^{-1} d v_{n}\right)\right\|<\infty$$
for every node $e^{\prime}$, where $\|\cdot\|$ is the Euclidean norm. (Compare the proof of Proposition 5.3) Moreover, we can take $v_{n}$ translationary invariant over each
end of $X^{(T(n))}$. Proposition 2.4 then provides smooth $\xi_{n} \in L_{2}^{p, \kappa_{n}}(X ; i \mathbb{R})$ such that
$$b_{n}=a_{n}-v_{n}^{-1} d v_{n}-d \xi_{n} \in L_{1}^{p, \kappa_{n}}$$
satisfies
$$d^{*} b_{n}=0, \quad \int_{\{0\} \times Y_{j}^{\prime}} * b_{n}=0$$
for $j=1, \ldots, r^{\prime}-1$. Stokes' theorem shows that the integral vanishes for $j=r^{\prime}$ as well, and since $\gamma$ is simply-connected we obtain, for $j=1, \ldots, r$,
$$\int_{\{t\} \times Y_{j}} * b_{n}=0 \quad \text { for }|t| \leq T_{j}(n) .$$
In particular, $R_{e^{\prime}} b_{n}=0$ for all nodes $e^{\prime}$ of $\gamma$.
Set $u_{n}=v_{n} \exp \left(\xi_{n}\right)$, so that $b_{n}=a_{n}-u_{n}^{-1} d u_{n}$. By Lemma 5.4 we have
$$\begin{aligned}
\left\|b_{n}\right\|_{L_{1}^{p, \kappa_{n}}} & \leq C\left(\left\|d^{+} b_{n}\right\|_{L^{p, \kappa_{n}}}+\sum_{e^{\prime}} \exp \left(\kappa_{n}\left(x_{e^{\prime}}\right)\right)\left\|J_{e^{\prime}}\left(b_{n}\right)\right\|\right) \\
& \leq C\left(\left\|d^{+} a_{n}\right\|_{L^{p, \kappa_{n}}}+\exp \left(1+C^{\prime}\right) \sum_{e^{\prime}}\left\|J_{e^{\prime}}\left(a_{n}-v_{n}^{-1} d v_{n}\right)\right\|\right),
\end{aligned}$$
which is bounded as $n \rightarrow \infty$. \(\square\)

Proposition 5.5 Suppose $\gamma$ is simply-connected and that Condition $(C)$ holds for $(X, \gamma)$. For $n=1,2, \ldots$ let $\left[S_{n}\right] \in M\left(X^{(T(n))} ; \vec{\alpha}_{n}^{\prime} ; \mu_{n} ; \overrightarrow{\mathfrak{p}}_{n} ; \overrightarrow{\mathfrak{p}}_{n}^{\prime}\right)$, where $\min _{j} T_{j}(n) \rightarrow \infty$. Then there exist smooth maps $w_{n}: X \rightarrow U(1)$ such that if $k$ is any positive integer with
$$\sup _{j, j^{\prime}, n}\left(\left\|\mu_{n}\right\|_{C^{k}}+\left\|\mathfrak{p}_{j, n}\right\|_{C^{k}}+\left\|\mathfrak{p}_{j^{\prime}, n}^{\prime}\right\|_{C^{k}}\right)<\infty$$
then the sequence $w_{n}\left(S_{n}\right)$ is bounded in $L_{k+1}^{p^{\prime}}$ over compact subsets of $X$ for every $p^{\prime} \geq 1$.

Proof Consider the set-up in the beginning of this subsection where now $p>4$ is the exponent used in defining configuration spaces, and $o$ is an orientation of $\gamma$ for which (C) is fulfilled. By passing to a subsequence we can arrange that $\kappa_{n}\left(x_{e}\right)-\kappa_{n}\left(x_{e^{\prime}}\right)$ converges to a point $\ell\left(e, e^{\prime}\right) \in[-\infty, \infty]$ for each pair of nodes $e, e^{\prime}$ of $\gamma$. Define an equivalence relation $\sim$ on the set $\mathcal{N}$ of nodes of $\gamma$ by declaring that $e \sim e^{\prime}$ if and only if $\ell\left(e, e^{\prime}\right)$ is finite. Then we have a linear ordering on $\mathcal{N} / \sim$ such that $[e] \geq\left[e^{\prime}\right]$ if and only if $\ell\left(e, e^{\prime}\right)>-\infty$. Here $[e]$ denotes the equivalence class of $e$.

Choose $e$ such that $[e]$ is the maximum with respect to this linear ordering. Let $S_{n}=\left(A_{o}+a_{n}, \Phi_{n}\right)$. Then all the hypotheses of Lemma 5.5 are satisfied. If $u_{n}$ is as in that lemma then, as in the proof of Proposition 5.3, $u_{n}\left(S_{n}\right)=$ $\left(A_{o}+b_{n}, u_{n} \Phi_{n}\right)$ will be bounded in $L_{k+1}^{p^{\prime}}$ over compact subsets of $X_{e}$ for every $p^{\prime} \geq 1$.

For any $r$-tuple $T$ let $W^{(T)}$ be the result of gluing ends of $X \backslash X_{e}$ according to the graph $\gamma \backslash e$ and (the relevant part of) the vector $T$. To simplify notation let us assume that the outgoing ends of $X_{e}$ are $\mathbb{R}_{+} \times\left(-Y_{j}\right), j=1, \ldots, r_{1}$. Then $\mathbb{R}_{+} \times Y_{j}$ is an end of $W^{T(n)}$ for $j=1, \ldots, r_{1}$. Let $b_{n}^{\prime}$ be the 1-form on $W^{T(n)}$ which away from the ends $\mathbb{R}_{+} \times Y_{j}, 1 \leq j \leq r_{1}$ agrees with $b_{n}$, and on each of these ends is defined by cutting off $b_{n}$ :
$$b_{n}^{\prime}(t, y)= \begin{cases}f_{1}\left(t-2 T_{j}(n)+1\right) \cdot b_{n}(t, y), & 0 \leq t \leq 2 T_{j}(n), \\ 0, & t \geq 2 T_{j}(n) .\end{cases}$$
Here $f_{1}$ is as in the proof of Lemma 5.4. Then $\sup _{n}\left\|d^{+} b_{n}^{\prime}\right\|_{\infty}<\infty$. After choosing an orientation of $\gamma \backslash e$ for which (C) holds we can apply Lemma 5.5 to each component of $\gamma \backslash e$, with $b_{n}^{\prime}$ in place of $a_{n}$. Repeating this process proves the proposition. \(\square\)

Corollary 5.2 If (B2) holds then for every constant $C_{0}<\infty$ there exists a constant $C_{1}<\infty$ such that for any element $[S]$ of a moduli space $M\left(X^{(T)} ; \vec{\alpha}^{\prime} ; \mu ; \overrightarrow{\mathfrak{p}} ; \overrightarrow{\mathfrak{p}}^{\prime}\right)$ where $\min _{j} T_{j}>C_{1}$ and $\mu, \mathfrak{p}_{j}, \mathfrak{p}_{j}^{\prime}$ all have $C^{1}$-norm $<C_{0}$ one has
$$\left|\sum_{j=1}^{r} \lambda_{j}\left(\vartheta\left(\left.S\right|_{\left\{-T_{j}\right\} \times Y_{j}}\right)-\vartheta\left(\left.S\right|_{\left\{T_{j}\right\} \times Y_{j}}\right)\right)+\sum_{j=1}^{r^{\prime}} \lambda_{j}^{\prime} \vartheta\left(\left.S\right|_{\{0\} \times Y_{j}^{\prime}}\right)\right|<C_{1} .$$
The next proposition, which is essentially a corollary of Proposition 5.5 exploits the fact that Condition (C) is preserved under certain natural extensions of $(X, \gamma)$.

Proposition 5.6 Suppose $\gamma$ is simply-connected and $(C)$ holds for $(X, \gamma)$. Then for every constant $C_{0}<\infty$ there is a constant $C_{1}<\infty$ such that if $S=(A, \Phi)$ represents an element of a moduli space $M\left(X^{(T)} ; \vec{\alpha}^{\prime} ; \mu ; \overrightarrow{\mathfrak{p}} ; \overrightarrow{\mathfrak{p}}^{\prime}\right)$ where $\min _{j} T_{j}>C_{1}$ and $\mu, \mathfrak{p}_{j}, \mathfrak{p}_{j}^{\prime}$ all have $L^{\infty}$ norm $<C_{0}$ then
$$\begin{array}{ll}
\left\|\nabla \vartheta_{S}\right\|_{L^{2}\left((t-1, t+1) \times Y_{j}\right)}<C_{1} & \text { for }|t| \leq T_{j}-1, \\
\left\|\nabla \vartheta_{S}\right\|_{L^{2}\left((t-1, t+1) \times Y_{j}^{\prime}\right)}<C_{1} & \text { for } t \geq 1 .
\end{array}$$

Proof Given an edge $v$ of $\gamma$ corresponding to a pair of ends $\mathbb{R}_{+} \times\left( \pm Y_{j}\right)$ of $X$, we can form a new pair ( $X_{(j)}, \gamma_{(j)}$ ) where $X_{(j)}=X \coprod\left(\mathbb{R} \times Y_{j}\right)$, and $\gamma_{(j)}$ is obtained from $\gamma$ by splitting $v$ into two edges with a common end-point representing the component $\mathbb{R} \times Y_{j}$ of $X_{(j)}$.
Similarly, if $e$ is a node of $\gamma$ and $\mathbb{R}_{+} \times Y_{j}^{\prime}$ an end of $X_{e}$ then we can form a new pair $\left(X^{(j)}, \gamma^{(j)}\right)$ where $X^{(j)}=X \amalg\left(\mathbb{R} \times Y_{j}^{\prime}\right)$, and $\gamma^{(j)}$ is obtained from $\gamma$ by adding one node $e_{j}^{\prime}$ representing the component $\mathbb{R}_{+} \times Y_{j}^{\prime}$ of $X^{(j)}$ and one edge joining $e$ and $e_{j}^{\prime}$.
One easily shows, by induction on the number of nodes of $\gamma$, that if (C) holds for $(X, \gamma)$ then (C) also holds for each of the new pairs $\left(X_{(j)}, \gamma_{(j)}\right)$ and $\left(X^{(j)}, \gamma^{(j)}\right)$. Given this observation, the proposition is a simple consequence of Proposition 5.5. \(\square\)

\section*{6 Exponential decay}

In this section we will prove exponential decay results for genuine monopoles over half-cylinders $\mathbb{R}_{+} \times Y$ and long bands $[-T, T] \times Y$. The overall scheme of proof will be the same as that for instantons in [10], and Subsections 6.1 and 6.3 follow [10] quite closely. On the other hand, the proof of the main result of Subsection 6.2 Proposition 6.1 is special to monopoles (and is new, as far as we know).

Throughout this section $Y$ will be a closed, connected Riemannian spin ${ }^{c} 3-$manifold, and $\eta \in \Omega^{2}(Y)$ closed. We will study exponential decay towards a non-degenerate critical point $\alpha$ of $\vartheta=\vartheta_{\eta}$. We make no non-degeneracy assumptions on any other (gauge equivalence classes of) critical points, and we do not assume that (O1) holds, except implicitly in Proposition 6.3. All monopoles will be genuine (ie $\mathfrak{p}=0$ ).

Previously, Nicolaescu [29] has proved a slightly weaker exponential decay result in the case $\eta=0$, using different techniques. Other results (with less complete proofs) were obtained in [28] and [26].

\subsection*{6.1 A differential inequality}

We begin by presenting an argument from [10] in a more abstract setting, so that it applies equally well to the Chern-Simons and the Chern-Simons-Dirac functionals.

Let $E$ be a real Banach space with norm $\|\cdot\|$ and $E^{\prime}$ a real Hilbert space with inner product $\langle\cdot, \cdot\rangle$. Let $E \rightarrow E^{\prime}$ be an injective, bounded operator with dense image. We will identify $E$ as a vector space with its image in $E^{\prime}$. Set $|x|=\langle x, x\rangle^{1 / 2}$ for $x \in E^{\prime}$.
Let $U \subset E$ be an open set containing 0 and
$$f: U \rightarrow \mathbb{R}, \quad g: U \rightarrow E^{\prime}$$
smooth maps satisfying $f(0)=0, g(0)=0$, and
$$D f(x) y=\langle g(x), y\rangle$$
for all $x \in U, y \in E$. Here $D f(x): E \rightarrow \mathbb{R}$ is the derivative of $f$ at $x$. Suppose $H=D g(0): E \rightarrow E^{\prime}$ is an isomorphism (of topological vector spaces). Note that $H$ can be thought of as a symmetric operator in $E^{\prime}$. Suppose $E$ contains a countable set $\left\{e_{j}\right\}$ of eigenvectors for $H$ which forms an orthonormal basis for $E^{\prime}$. Suppose $\sigma, \lambda$ are real numbers satisfying $0 \leq \lambda<\sigma$ and such that $H$ has no positive eigenvalue less than $\sigma$.

Lemma 6.1 In the above situation there is a constant $C>0$ such that for every $x \in U$ with $\|x\| \leq C^{-1}$ one has
$$\begin{aligned}
& 2 \sigma f(x) \leq|g(x)|^{2}+C|g(x)|^{3}, \\
& 2 \lambda f(x) \leq|g(x)|^{2} .
\end{aligned}$$

Proof It clearly suffices to establish the first inequality for some $C$. By Taylor's formula [8, 8.14.3] there is a $C_{1}>0$ such that for all $x \in U$ with $\|x\| \leq C_{1}^{-1}$ one has
$$\begin{aligned}
\left|f(x)-\frac{1}{2}\langle H x, x\rangle\right| & \leq C_{1}\|x\|^{3}, \\
|g(x)-H x| & \leq C_{1}\|x\|^{2} .
\end{aligned}$$
Let $H e_{j}=\lambda_{j} e_{j}$, and set $x_{j}=\left\langle x, e_{j}\right\rangle e_{j}$. Then
$$\sigma\langle H x, x\rangle=\sigma \sum_{j} \lambda_{j}\left|x_{j}\right|^{2} \leq \sum_{j} \lambda_{j}^{2}\left|x_{j}\right|^{2}=|H x|^{2} .$$
By assumption, there is a $C_{2}>0$ such that
$$\|x\| \leq C_{2}|H x|$$
for all $x \in E$. Putting the above inequalities together we get, for $r=\|x\| \leq$ $C_{1}^{-1}$,
$$\begin{aligned}
|H x| & \leq|g(x)|+C_{1} r^{2} \\
& \leq|g(x)|+r C_{1} C_{2}|H x| .
\end{aligned}$$

If $r<\left(C_{1} C_{2}\right)^{-1}$ this gives
$$|H x| \leq\left(1-r C_{1} C_{2}\right)^{-1}|g(x)|,$$
hence
$$\begin{aligned}
2 \sigma f(x) & \leq \sigma\langle H x, x\rangle+2 \sigma C_{1} r^{3} \\
& \leq|H x|^{2}+2 \sigma r C_{1} C_{2}^{2}|H x|^{2} \\
& \leq \frac{1+2 \sigma r C_{1} C_{2}^{2}}{\left(1-r C_{1} C_{2}\right)^{2}}|g(x)|^{2} \\
& \leq\left(1+C_{3} r\right)|g(x)|^{2} \\
& \leq|g(x)|^{2}+C_{4}|g(x)|^{3}
\end{aligned}$$
for some constants $C_{3}, C_{4}$. \(\square\)

We will now apply this to the Chern-Simons-Dirac functional. Let $\alpha=$ $\left(B_{0}, \Psi_{0}\right)$ be a non-degenerate critical point of $\vartheta$. Set $K_{\alpha}=\operatorname{ker}\left(\mathcal{I}_{\alpha}^{*}\right) \subset \Gamma\left(i \Lambda^{1} \oplus \mathbb{S}\right)$ and $\widetilde{H}_{\alpha}=\left.H_{\alpha}\right|_{K_{\alpha}}: K_{\alpha} \rightarrow K_{\alpha}$. Note that any eigenvalue of $\widetilde{H}_{\alpha}$ is also an eigenvalue of the self-adjoint elliptic operator
$$\left(\begin{array}{cc}
0 & \mathcal{I}_{\alpha}^{*} \\
\mathcal{I}_{\alpha} & H_{\alpha}
\end{array}\right)$$
over $Y$ acting on sections of $i \Lambda^{0} \oplus i \Lambda^{1} \oplus \mathbb{S}$. Let $\lambda^{ \pm}$be positive real numbers such that $\widetilde{H}_{\alpha}$ has no eigenvalue in the interval $\left[-\lambda^{-}, \lambda^{+}\right]$.
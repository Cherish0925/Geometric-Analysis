---
retention_scope: session
part: 1
total_parts: 1
---

---
source_file: 2101_00481.pdf
converter: mathpix
format: mmd
---

\title{
On the ADM mass of Kähler scalar flat ALE metrics
}

\author{
Claudio Arezzo* and Karen Corrales ${ }^{\dagger}$
}

\begin{abstract}
In this paper we study the behaviour of scalar flat Kähler ALE spaces and their ADM mass under blow ups. In particular we prove that by blowing up sufficiently many points at sufficiently big mutual distance one can produce scalar flat metrics with arbitrarily large ADM mass. A general machinery for producing scalar flat non Ricci flat ALE spaces of zero ADM mass is also presented, using and integrating previous work by Rollin-Singer ([17]) and Hein-LeBrun ([11]).
\end{abstract}

\section*{1 Introduction}

The existence and geometric properties of Ricci and scalar flat metrics on ALE Kähler spaces with a given structure group at infinity have been subject of intense research in past few decades (see e.g. [8], [15], [14], [13], [7], [10], [16]). In this paper we study to which extent the machinery developed in [2] for constructing constant scalar curvature Kähler metrics on blow ups can be used and extended in this setting. Given the fact that such spaces do not carry holomorphic vector fields (which are the key obstruction for this theory) it is not hard to get the existence of scalar-flat metrics on blow ups of scalar flat ALE spaces (Theorem 3.1). While not the main focus of this paper, we point out that the new ALE scalar flat spaces produced in Theorem 3.1 can in turn be used as new models for the gluing theory, hence getting, even starting from compact cscK manifolds, infinitely may new families of cscK manifolds of different topological types.
The new interesting problem studied in this paper is to estimate the maximal size of an exceptional divisor that can be inserted in the original space. It is known that in general this question can be very subtle on compact manifolds, carrying implicitily the difficulties hidden in the notion of $K$-stability and in the Tian-Yau-Donaldson Conjecture (see for example Section 7.2 point (2) in [9] and [19]). On top of its clear geometric interest, the main motivation for this question comes from the recent and beautiful work by Hein-LeBrun ([11]) connecting various geometric and topological quantities of ALE spaces to their ADM mass, another natural invariant arising from General Relativity recalled in Section 2.2 ([4]).

\footnotetext{
*International Centre for Theoretical Physics ICTP, arezzo@ictp.it
${ }^{\dagger}$ Facultad de Matemáticas, Pontificia Universidad Católica de Chile, kacorrales@mat.uc.cl
}

Hein-LeBrun's topological formula for the ADM mass (Theorem 2.2) immediately implies that the effect of blowing up one point on the ADM mass is to increase it by an amount proportional to the volume of the exceptional divisor that one can insert, while keeping the scalar curvature zero, hence pointing again to the problem mentioned above.
The main result of this paper (Theorem 4.1) guarantees that this quantity cannot decrease when performing a second blow up at a point sufficiently far away from the first one. Iterating this scheme for multiple blow ups at sufficiently many points at sufficiently big mutual distance, we get the main applications in terms of ADM mass.

Theorem 1.1. Let $(X, \boldsymbol{\Gamma}, h, \omega)$ be an ALE scalar flat Kähler manifold with structure group $\boldsymbol{\Gamma}$ and $A D M$ mass $e \in \mathbb{R}$. Then for every $\tilde{e} \geq e$ there exists an ALE scalar flat Kähler manifold with structure group $\boldsymbol{\Gamma}$ with ADM mass $\tilde{e}$. Such manifold can be obtained from $X$ by blowing up sufficiently many points at sufficiently big mutual distance.

The above theorem indicates that, while $\Gamma$ does not determine the ADM mass of an ALE scalar flat Kähler manifold with structure group $\boldsymbol{\Gamma}$ (something easy to observe even for trivial $\Gamma$ ), the interesting quantity that can be algebraically determined by the structure group is
$\inf \{\mathrm{ADM} \operatorname{mass}(X, \boldsymbol{\Gamma}, h, \omega) \mid(X, \boldsymbol{\Gamma}, h, \omega)$ ALE scalar flat Kähler with structure group $\boldsymbol{\Gamma}\}$.
Theorem 1.1 gives also a general framework to produce scalar flat, non Ricci flat, ALE spaces with vanishing ADM mass. Specific examples were known thanks to Rollin-Singer ([17], Section 6.7) and Hein-LeBrun ([11], Theorem 4.7), but our result gives a general machinery to produce them.

Corollary 1.2. Let $(X, \boldsymbol{\Gamma}, h, \omega)$ be an ALE scalar flat Kähler manifold with structure group $\boldsymbol{\Gamma}$ and $A D M$ mass $e<0$. Then there exists an ALE scalar flat Kähler manifold with structure group $\boldsymbol{\Gamma}$ with vanishing ADM mass. Such manifold can be obtained from $X$ by blowing up sufficiently many points at sufficiently big mutual distance.

\section*{2 Preliminaries}

\subsection*{2.1 The Kähler potential of a scalar flat ALE Kähler resolution.}

We start by recalling the concept of Asymptotically Locally Euclidean (ALE for short) Kähler manifold with structure group $\boldsymbol{\Gamma}$. Let $\boldsymbol{\Gamma}=\left(\Gamma_{j}\right), j=1 \ldots, k$ be a collection of finite subgroups of the unitary group $U(m)$ each acting freely away from the origin. We say that a complete noncompact Kähler manifold ( $X, \boldsymbol{\Gamma}, h, \omega$ ) of complex dimension $m$, where $h$ is the Kähler metric and $\omega$ is the Kähler form, is an ALE Kähler manifold with structure group $\boldsymbol{\Gamma}$ if
\begin{itemize}
\item[-] there exist a compact subset $K$ such that the $j$-th connected component of $X \backslash K$ is biholomorphic via a map $\pi_{j}$ to $\left(\mathbb{C}^{m} \backslash B\right) / \Gamma_{j}$, where $B$ is a closed ball with positive radius $R>0$, and
\item[-] on each component in standard Euclidean coordinates the metric $\pi_{*} h$ satisfies
$$\left|\frac{\partial^{\alpha}}{\partial x^{\alpha}}\left(\left(\pi_{*} h\right)_{i \bar{j}}-\frac{1}{2} \delta_{i \bar{j}}\right)\right|=\mathcal{O}\left(|x|^{-\tau-|\alpha|}\right),$$
for some $\tau>0$ and every multindex $\alpha \in \mathbb{N}^{m}$.
\end{itemize}

Note that we are identifying the complex structure outside a compact subset with the standard one. This puts a restriction (widely studied) on the class of spaces allowed since in general its complex structure could be only asymptotic to the standard one and in fact the complex structure could not even admit holomorphic coordinates at infinity as shown for example by Honda ([12]) also in the scalar flat case.

While the definition allows for an ALE space to have multiple components, a remarkable Theorem by Hein-LeBrun (Propositions 1.5 and 4.2 in [11]) shows that only the case $k=1$ can actually occur. We can then assume it thoughtout the paper.

The behaviour of the Kähler potential of a scalar flat ALE Kähler metric is quite well understood (see e.g. [2] Section 7 and [1] for further details)

Proposition 2.1. Let $(X, \Gamma, h, \omega)$ be a scalar flat ALE Kähler manifold with structure group $\Gamma$. Then for $R>0$ large enough, we have that on $X \backslash \pi^{-1}\left(B_{R}\right)$ the Kähler form can be written as
\begin{itemize}
\item[-] if $\operatorname{dim}(X)=m>2$, then, for some real constant $e_{X}$,
$$\omega=i \partial \bar{\partial}\left(\frac{|x|^{2}}{2}+e_{X}|x|^{4-2 m}+\psi_{\eta}(x)\right), \quad \text { with } \quad \psi_{\eta}=\mathcal{O}\left(|x|^{3-2 m}\right),$$
\item[-] if $\operatorname{dim}(X)=2$, then for some real constant $e_{X}$,
$$\omega=i \partial \bar{\partial}\left(\frac{|x|^{2}}{2}+e_{X} \log |x|+\psi_{\eta}(x)\right), \quad \text { with } \quad \psi_{\eta}=\mathcal{O}\left(|x|^{-1}\right)$$
\end{itemize}

\subsection*{2.2 The ADM mass of a Kähler potential of an ALE Kähler manifold with structure group $\Gamma$.}

The key quantity studied in this paper is the celebrated ADM mass introduced by Arnowitt-Deser-Misner ([4]), whose geometrical nature has been clarified by Bartnik ([5]) and Chruściel ([8]).

In the context on ALE Kähler manifolds it has been the center of the beautiful paper by Hein-LeBrun ([11]) which is the original motivation of our work.
Following Hein-LeBrun's normalization conventions are chosen so that, at a given end, the mass of an ALE manifold is given by
$$m(X, h)=\lim _{R \rightarrow \infty} \frac{\boldsymbol{\Gamma}\left(\frac{m}{2}\right)}{4(m-1) \pi^{\frac{m}{2}}} \int_{S_{R} / \Gamma}\left[h_{k l, k}-h_{k k, l}\right] \mathbf{n}^{l} d a_{E}$$
where $S_{R}$ is the Euclidean coordinate sphere of radius $R, d a_{E}$ is the $(m-1)$-dimensional volume form induced on this sphere by the Euclidean metric, and n is the outward-pointing Euclidean unit normal vector.
Let us also denote by : $H^{2} \rightarrow H_{c}^{2}(X)$ the inverse of the isomorphism induced by the standard inclusion of compactly supported forms into all differential forms.
Restricting our attention to the scalar flat case, their key result is the following equivalence:
Theorem 2.2. Let $(X, \Gamma, h, \omega)$ be a scalar flat ALE Kähler manifold with structure group $\Gamma$. Then
$$m(X, h)=-\frac{\left\langle\boldsymbol{\circ}\left(c_{1}(X), \omega^{m-1}\right\rangle\right.}{(2 m-1) \pi^{m-1}}=e_{X} .$$
The first equality is a special case of Theorem C in [11], while the equality $m(X, h)=e_{X}$ is a classical observation due to LeBrun ([15]) and Rollin-Singer ([17], Section 6.8) in complex dimension 2, whose proof extends readily to any dimension.

\section*{3 Blowing up points}

In order to fix notations needed in the sequel, for every point $p \in X$ we denote by $\left(z_{1}, \ldots z_{m}\right)$ normal coordinates centred at $p$, so that near $p$ the metric $\omega$ is of the form
$$\omega=\omega_{E}+i \partial \bar{\partial} \varphi_{1}(z), \quad \varphi_{1}(z)=\mathcal{O}\left(|z|^{4}\right),$$
specifically, $\varphi_{1}(z) \leq c|z|^{4}$, where $c$ depends on the curvature of $\omega$ at $p$.
It is also convenient to isolate, among all ALE scalar flat Kähler manifolds, $\left(B l_{0} \mathbb{C}^{m},\{I d\}, h_{B S}, \eta_{B S}\right)$, where $h_{B S}$ denotes the well-know Burns-Simanca metric, normalized so to have volume of the exceptional divisor $E$ equal to 1 . Its asymptotic expansion at infinity can be written as
$$\begin{array}{ll}
\eta_{B S}=\omega_{E}+i \partial \bar{\partial} \varphi_{2}(w), & \varphi_{2}(w)=\mathcal{O}\left(|w|^{4-2 m}\right), \\
\eta_{B S}=\omega_{E}+i \partial \bar{\partial} \varphi_{2}(w), & \varphi_{2}(w)=\log \left(|w|^{2}\right), \quad \text { for } m=2
\end{array}$$
in terms of the standard coordinates on $B l_{0} \mathbb{C}^{m} \backslash E \cong \mathbb{C}^{m} \backslash\{0\}$.
On the other hand, [2, Proposition 5.4] implies that there is no nonzero holomorphic vector field vanishing somewhere on $X$ and then it is easy to observe that the proof of [2, Theorem 1.1] readily extends to the ALE case. More precisely we have

Theorem 3.1. Let $(X, \Gamma, h, \omega)$ be a scalar flat ALE Kähler manifold with structure group $\Gamma$. Given finitely many smooth points $p_{1}, \ldots p_{k} \in X$, there exists $\varepsilon_{0}\left(X, p_{1}, \ldots, p_{k}\right):=\varepsilon_{0}>0$ such that the blow-up of $X$ at $p_{1}, \ldots p_{k}$ carries zero scalar curvature Kähler forms
$$\omega_{\varepsilon} \in \pi^{*}[\omega]-\varepsilon^{2}\left(P D\left[E_{1}\right]+\cdots+P D\left[E_{k}\right]\right),$$
where the $P D\left[E_{j}\right]$ are the Poincaré duals of the $(2 m-2)$-homology classes of the exceptional divisors of the blow-up at $p_{j}$ and $\varepsilon \in\left(0, \varepsilon_{0}\right)$.
What is crucial for the scope of this paper is to make, as explicit as possible, the dependence of $\varepsilon_{0}$ on all the geometric data built in this theorem, such as the position of the points $p_{j}$ and the geometry of $X$ and of $B l_{0} \mathbb{C}^{m}$.
Let us then recall that in order to construct the scalar flat metric on $B l_{p_{1}, \ldots p_{k}} X$, the idea is to replace the metric $\omega$ on a small neighbourhood of $p_{i}$ with a suitably scaled down copy of $\eta_{B S}$.
Precisely, for a fixed $\varepsilon>0$ and $r_{\varepsilon}=\varepsilon^{m-1 / m}$, we will glue $\omega$ with $\varepsilon^{2} \eta_{B S}$ on the annulus $B_{2 r_{\varepsilon}} \backslash B_{r_{\varepsilon}}$ around each $p_{i}$, under the change of variables $z=\varepsilon w$.
Following (3) and (3), the metric on $X \backslash\left\{p_{1} \ldots, p_{k}\right\}$, which naturally extends to a metric on $B l_{p_{1}, \ldots p_{k}} X$, is defined by
$$\tilde{\omega}_{\varepsilon}=\left\{\begin{array}{l}
\omega \text { on } X \backslash \cup_{i=1}^{k} B_{2 r_{\varepsilon}}\left(p_{i}\right) \\
\omega_{E}+i \partial \bar{\partial}\left(\gamma_{1}(z) \varphi_{1}(z)+\varepsilon^{2}\left(1-\gamma_{1}(z)\right) \varphi_{2}\left(\varepsilon^{-1} z\right)\right) \quad \text { on } \quad B_{2 r_{\varepsilon}}\left(p_{i}\right) \backslash B_{r_{\varepsilon}}\left(p_{i}\right) \\
\varepsilon^{2} \eta_{B S} \quad \text { on } \quad B_{r_{\varepsilon}}\left(p_{i}\right) \backslash\left\{p_{i}\right\}
\end{array}\right.$$
where $\gamma_{1}$ is a suitable cutoff function.
Once this pre-glued metric is built the problem is to find a function $\varphi$ such that the metric $\omega_{\varepsilon}=\tilde{\omega}_{\varepsilon}+i \partial \bar{\partial} \varphi$ has zero scalar curvature. In order to solve that equation, the most important step is to show that the linear operator $L_{\tilde{\omega}_{\varepsilon}}$ associated to the scalar curvature is invertible and to obtain bounds on the norm of the inverse in suitable Banach spaces: weighted Hölder spaces, which now have to take into "weighted" account the behaviour of function near the point $p_{j}$, with weight $\delta$, and at infinity, with weight $\delta_{\infty}$.

The weighted spaces where to carry out the proof of Theorem 3.1 are the same one as those used in [2] and [18] with the extra weight $\delta_{\infty}$.

If we denote $X^{*}:=X \backslash\left\{p_{1} \ldots, p_{k}\right\}, X_{r}:=X \backslash \cup_{i=1}^{k} B_{r}\left(p_{i}\right)$ and $N_{p_{i}}$ by the identification of $B_{r}\left(p_{i}\right) \backslash\left\{p_{i}\right\}$ with $B l_{0} \mathbb{C}^{n}$, then we define
Definition 3.2. Given $l \in \mathbb{N}, \alpha \in(0,1), \delta, \delta_{\infty} \in(4-2 m, 0)$, we define
\begin{itemize}
\item[1.] The weighted space $C_{\delta, \delta_{\infty}}^{l, \alpha}\left(X^{*}\right)$ as the space of functions $\varphi \in C_{\text {loc }}^{l, \alpha}\left(X^{*}\right)$ for which the norm
$$\|\varphi\|_{C_{\delta, \delta \infty}^{l, \alpha}\left(X^{*}\right)}:=\|\varphi\|_{C_{\delta_{\infty}}^{l, \alpha}\left(X_{r_{0}}\right)}+\max _{i=1 \ldots k}\left\{\sup _{r \in\left(0,2 r_{0}\right)}\left(r^{-\delta}\|\varphi(r z)\|_{C^{l, \alpha}\left(B_{2}\left(p_{i}\right) \backslash B_{1}\left(p_{i}\right)\right)}\right)\right\}$$
\end{itemize}
is finite.
\begin{itemize}
\item[2.] The weighted space $C_{\delta}^{l, \alpha}\left(N_{p_{i}}\right)$ is defined to be the space of functions $\varphi \in C_{\text {loc }}^{l, \alpha}\left(N_{p_{i}}\right)$ for which the norm
$$\|\varphi\|_{C_{\delta}^{l, \alpha}\left(N_{p_{i}}\right)}:=\|\varphi\|_{C^{l, \alpha}\left(\left\{|w|<2 R_{0}\right\}\right)}+\sup _{R \in\left[R_{0}, \infty\right)}\left(R^{-\delta}\|\varphi(R w)\|_{C^{l, \alpha}\left(B_{2} \backslash B_{1}\right)}\right)$$
is finite.
\item[3.] The weighted space $C_{\delta, \delta_{\infty}}^{l, \alpha}\left(B l_{p_{1}, \ldots p_{k}} X\right)$ is defined for the gluing between the previous two, i.e. the space of functions $\varphi \in C_{\text {loc }}^{l, \alpha}\left(B l_{p_{1}, \ldots p_{k}} X\right)$ for which the norm
$$\begin{aligned}
\|\varphi\|_{C_{\delta, \delta_{\infty}}^{l, \alpha}\left(B l_{p_{1}, \ldots p_{k}} X\right)}= & \|\varphi\|_{C_{\delta_{\infty}}^{l, \alpha}\left(X_{2 r_{\varepsilon}}\right)}+\|\varphi\|_{C_{\delta}^{l, \alpha}\left(N_{p_{i}}\right)} \\
& +\max _{i=1 \ldots k}\left\{\sup _{r \in\left(r_{\varepsilon}, 2 r_{\varepsilon}\right)}\left(r^{-\delta}\|\varphi(r z)\|_{C^{l, \alpha}\left(B_{2}\left(p_{i}\right) \backslash B_{1}\left(p_{i}\right)\right)}\right)\right\}
\end{aligned}$$
is finite.
\end{itemize}

Throughout this paper we will denote $X_{p_{1}, \ldots p_{k}}:=X \backslash \cup_{i=1}^{k} B_{2 r_{\varepsilon}}\left(p_{i}\right)$ and $A_{p_{i}}:=B_{2 r_{\varepsilon}}\left(p_{i}\right) \backslash$ $B_{r_{\varepsilon}}\left(p_{i}\right)$, then
$$\|\varphi\|_{C_{\delta, \delta_{\infty}}^{l, \alpha}\left(B l_{p_{1}, \ldots p_{k}} X\right)}=\|\varphi\|_{C_{\delta_{\infty}}^{l, \alpha}\left(X_{p_{1}, \ldots p_{k}}\right)}+\|\varphi\|_{C_{\delta}^{l, \alpha}\left(N_{p_{i}}\right)}+\max _{i=1 \ldots k}\left\{\|\varphi\|_{C_{\delta}^{l, \alpha}\left(A_{p_{i}}\right)}\right\} .$$

Remark 3.3. Note that the norm $\|\varphi\|_{C_{\infty}^{l, \alpha}\left(X_{p_{1}, \ldots p_{k}}\right)}$ uses to the metric $\omega ;\|\varphi\|_{C_{\delta}^{l, \alpha}\left(A_{p_{i}}\right)}$ the pre-glued metric $\tilde{\omega}_{\varepsilon}$ and $\|\varphi\|_{C_{\delta}^{l, \alpha}\left(N_{p_{i}}\right)}$ uses the metric $\varepsilon^{2} \eta_{B S}$ for each $i$.

Remark 3.4. It is important to remark that the proof of Theorem 3.1 depends on whether $m=2$ or $m>2$. However, when $m=2$ we can still work weight spaces with $\delta \in(-1,0)$, but we lose the uniform control of the inverse operator and other problems appear. One way to overcome these problems is to construct a better gluing metric than the one defined by (3). If we consider
$$\hat{\omega}_{\varepsilon}=\left\{\begin{array}{l}
\omega \quad \text { on } \quad X \backslash \cup_{i=1}^{k} B_{2 r_{\varepsilon}}\left(p_{i}\right) \\
\omega_{E}+i \partial \bar{\partial}\left(\gamma_{1}(z) \varphi_{1}(z)+\varepsilon^{2}\left(1-\gamma_{1}(z)\right) \log \left|\varepsilon^{-1} z\right|\right) \quad \text { on } \quad B_{2 r_{\varepsilon}}\left(p_{i}\right) \backslash B_{r_{\varepsilon}}\left(p_{i}\right) \\
\varepsilon^{2} \eta_{B S} \quad \text { on } \quad B_{r_{\varepsilon}}\left(p_{i}\right) \backslash\left\{p_{i}\right\}
\end{array}\right.$$
then we define $\tilde{\omega}_{\varepsilon}=\hat{\omega}_{\varepsilon}+\varepsilon^{2} i \partial \bar{\partial}\left(\gamma_{1}(z)(\Gamma(z)-\log \varepsilon)\right)$, where $\Gamma$ is a solution asymptotic to $\log |z|$ near $p_{i}$ of $L_{\omega}(\Gamma)=c$, where $c$ is a constant and $L_{\omega}$ is the linearized scalar curvature operato. For more details, see [18, Section 8.4].
Therefore, the new analysis carried out in this paper does depend on $m$ we give the details only in the case $m>2$.

All proofs about the invertibility of the linearized scalar curvature, $L_{\omega_{\varepsilon}}$, contained in [2] and [18], go through verbatim also in this context so we do not reproduce them. However, we need to estimate the dependence of norms of operators, both linear and non-linear, on the geometric data of the construction. This is what we achieve in the next section.

\section*{4 Dependence on the position of the points}

The goal in this section is to study the behaviour of $\varepsilon_{0}$ on Theorem 3.1, for the blow-up at one point $p$ with the one for the blow-up at two points $p, q$, to prove that $\varepsilon_{0}(p, q) \geq \varepsilon_{0}(p)$ as $q$ goes to infinity.
Let $(X, \Gamma, h, \omega)$ be a scalar flat ALE Kähler manifold with structure group $\Gamma$ and pick two points $p, q \in X$. In the sequel we will consider $p \in X$ fixed and study the behaviour of all appearing quantities with $p$ fixed and moving $q$. Theorem 3.1 implies that
\begin{itemize}
\item[-] there exists $\varepsilon_{0}(p)>0$ such that for every $\varepsilon \in\left(0, \varepsilon_{0}(p)\right)$ the blow-up of $X$ at $p$ carries scalar flat Kähler forms
$$\omega_{\varepsilon} \in \pi^{*}[\omega]-\varepsilon^{2} a P D[E] .$$
\item[-] there exists $\varepsilon_{0}(p, q)>0$ such that for every $\varepsilon \in\left(0, \varepsilon_{0}(p, q)\right)$ the blow-up of $X$ at $p, q$ carries constant scalar curvature Kähler forms
$$\omega_{\varepsilon} \in \pi^{*}[\omega]-\varepsilon^{2} a_{p} P D\left[E_{p}\right]-\varepsilon^{2} a_{q} P D\left[E_{q}\right] .$$
\end{itemize}
Note that with a slight abuse of notation we use $\omega_{\varepsilon}$ for the pre-glued metrics $\tilde{\omega}_{\varepsilon}$ and the scalar flat metrics $\omega_{\varepsilon}$ in both cases for $B l_{p} X$ and $B l_{p, q} X$ since there is no possibility of confusion.
Thus, our main estimate is
Theorem 4.1. Let $(X, \Gamma, h, \omega)$ be a scalar flat ALE Kähler manifold with structure group $\Gamma$ and $p, q \in X$. If $\varepsilon_{0}(p)$ and $\varepsilon_{0}(p, q)$ are the constants where Theorem 3.1 holds then
$$\varepsilon_{0}(p, q) \rightarrow \varepsilon_{0} \geq \varepsilon_{0}(p), \quad \text { as } \quad r(q) \rightarrow \infty$$
where $r(q)$ is the distance between $q$ and a compact subset $K \subset X$ containing $p$.
In this case and following the metric defined in (3) we have
$$\tilde{\omega}_{\varepsilon}=\left\{\begin{array}{l}
\omega \quad \text { on } \quad X_{p, q} \\
\omega_{E}+i \partial \bar{\partial} \varphi_{p, \varepsilon}(z) \quad \text { on } \quad A_{p} \\
\omega_{E}+i \partial \bar{\partial} \varphi_{q, \varepsilon}(z) \quad \text { on } \quad A_{q} \\
\varepsilon^{2} \eta_{B S} \quad \text { on } \quad N_{p} \\
\varepsilon^{2} \eta_{B S} \quad \text { on } \quad N_{q}
\end{array}\right.$$
where $\varphi_{p, \varepsilon}(z)$ and $\varphi_{q, \varepsilon}(z)$ are the gluing potentials between $\varphi_{1}$ and $\varphi_{2}$, near $p$ and near $q$, respectively.

Remark 4.2. It is important to note that (3) and (3) imply that there exist constants $c_{p}, c_{q}$ and $c$ such that
$$\begin{aligned}
& \left\|\varphi_{p, \varepsilon}(z)\right\|_{C_{\delta}^{4, \alpha}\left(A_{p}\right)} \leq\left\|\varphi_{1}(z)\right\|_{C_{\delta}^{4, \alpha}\left(A_{p}\right)}+\varepsilon^{2}\left\|\varphi_{2}\left(\varepsilon^{-1} z\right)\right\|_{C_{\delta}^{4, \alpha}\left(A_{p}\right)} \leq\left(c_{p}+c\right) r_{\varepsilon}^{4-\delta} \\
& \left\|\varphi_{q, \varepsilon}(z)\right\|_{C_{\delta}^{4, \alpha}\left(A_{q}\right)} \leq\left\|\varphi_{1}(z)\right\|_{C_{\delta}^{4, \alpha}\left(A_{q}\right)}+\varepsilon^{2}\left\|\varphi_{2}\left(\varepsilon^{-1} z\right)\right\|_{C_{\delta}^{4, \alpha}\left(A_{q}\right)} \leq\left(c_{q}+c\right) r_{\varepsilon}^{4-\delta}
\end{aligned}$$
where $c_{p}$ and $c_{q}$ depends on the curvature of $\omega$ around $p$ and $q$, and $c$ does not depend on the point.
The simple but crucial observation, repeatedly used in the sequel, is that since the metric $\omega$ is $A L E$ then $c_{q} \leq c_{p}$ as $q$ goes to infinity. Therefore,
$$\left\|\varphi_{q, \varepsilon}(z)\right\|_{C_{\delta}^{4, \alpha}\left(A_{q}\right)} \leq\left(c_{p}+c\right) r_{\varepsilon}^{4-\delta}$$
The existence of the constant $\varepsilon_{0}$ in the theory developed in [2] and [3] comes from the estimates on the scalar curvature, its linear operator and the quadratic part to use the Fixed point Theorem. Denoting by $S\left(\omega_{\varepsilon}\right)$ as the scalar curvature, $L_{\omega_{\varepsilon}}$ its linear part, $Q_{\omega_{\varepsilon}}$ its quadratic part and $\mathcal{N}$ as the operator
$$\mathcal{N}: C_{\delta, \delta_{\infty}}^{4, \alpha}\left(B l_{p, q} X\right) \rightarrow C_{\delta, \delta_{\infty}}^{4, \alpha}\left(B l_{p, q} X\right), \quad \mathcal{N}(\varphi)=L_{\omega_{\varepsilon}}^{-1}\left(-S\left(\omega_{\varepsilon}\right)-Q_{\omega_{\varepsilon}}(\varphi)\right),$$
the key Proposition to prove the existence of cscK metrics is the following
Proposition 4.3. see e.g. [18, Proposition 8.20] For some constant $c_{1}$, let
$$\mathcal{U}:=\left\{\varphi \in C_{\delta, \delta_{\infty}}^{4, \alpha}\left(B l_{p, q} X\right):\|\varphi\|_{C_{\delta, \delta_{\infty}}^{4, \alpha}\left(B l_{p, q} X\right)} \leq c_{1} r_{\varepsilon}^{2-\delta}\right\} .$$
Then, there exists $\varepsilon_{0}(p, q)$ such that for every $\varepsilon<\varepsilon_{0}, \mathcal{N}$ is a contraction on $\mathcal{U}$ and $\mathcal{N}(\mathcal{U}) \subset$ $\mathcal{U}$. In particular, $\mathcal{N}$ has a fixed point, which gives a cscK metric on $B l_{p, q} X$ in the Kähler class $\pi^{*}[\omega]-\varepsilon^{2} a_{p} P D\left[E_{p}\right]-\varepsilon^{2} a_{q} P D\left[E_{q}\right]$.

The key estimates to prove the above Proposition are the following
\begin{itemize}
\item[(i)] there exists a constant $c_{1}$ such that if $\|\varphi\|_{C_{2, \delta \infty}^{4, \alpha}\left(B l_{p, q} X\right)} \leq c_{1}$ then
$$\|\mathcal{N}(\varphi)-\mathcal{N}(0)\|_{C_{\delta, \delta_{\infty}}^{4, \alpha}\left(B l_{p, q} X\right)} \leq \frac{1}{2}\|\varphi\|_{C_{\delta, \delta_{\infty}}^{4, \alpha}\left(B l_{p, q} X\right)}$$
\item[(ii)] for the same constant $c_{1},\|\mathcal{N}(0)\|_{C_{\delta, \delta_{\infty}}^{4, \alpha}\left(B l_{p, q} X\right)} \leq \frac{1}{2} c_{1} r_{\varepsilon}^{2-\delta}$.
\end{itemize}

Remark 4.4. Note that
$$\begin{aligned}
& \left.\|\mathcal{N}(\varphi)-\mathcal{N}(0)\|_{C_{\delta, \delta \infty}^{4, \alpha}\left(B l_{p, q} X\right)}=\left\|L_{\omega_{\varepsilon}}^{-1}\left(Q_{\omega_{\varepsilon}}(0)-Q_{\omega_{\varepsilon}}(\varphi)\right)\right\|_{C_{\delta, \delta \infty}^{4, \alpha}} \leq K_{p, q} \| Q_{\omega_{\varepsilon}}(\varphi)\right)\left\|_{C_{\delta-4, \delta \infty-4}^{0, \alpha}} \leq K_{p, q} c_{1}\right\| \varphi \|_{C_{\delta, \delta \infty}^{4, \alpha}} \\
& \left.\|\mathcal{N}(0)\|_{C_{\delta, \delta \infty}^{4, \alpha}\left(B l_{p, q} X\right)}=\left\|L_{\omega_{\varepsilon}}^{-1}\left(-S\left(\omega_{\varepsilon}\right)\right)\right\|_{C_{\delta, \delta \infty}^{4, \alpha}}\left(B l_{p, q} X\right) \leq K_{p, q} \| S\left(\omega_{\varepsilon}\right)\right) \|_{C_{\delta-4}^{0, \alpha}\left(B l_{p, q} X\right)} \leq K_{p, q} C_{p, q} r_{\varepsilon}^{4-\delta}
\end{aligned}$$
Therefore, (i) follows once $c_{1}$ is chosen less than $1 / 2 K_{p, q}$ and $\varepsilon_{0}(p, q)$ is chosen such that for every $\varepsilon<\varepsilon_{0}$
$$2 K_{p, q} C_{p, q} r_{\varepsilon}^{2}<c_{1}, \quad r_{\varepsilon}=\varepsilon^{\frac{m-1}{m}} .$$

Thus, the next two subsections will be dedicated to understand the definition and construction of $C_{p, q}$ and $K_{p, q}$. Next, they will be compared with the same constants $C_{p}$ and $K_{p}$ (in the case of $B l_{p} X$ ) when $q$ goes to infinity.

\subsection*{4.1 Comparison between $C_{p, q}$ with $C_{p}$}

In this part we will to compare the estimates on the scalar curvature for the preglued metrics for $B l_{p, q} X$ and $B l_{p} X$. It is known that there exist $C_{p}$ and $C_{p, q}$ defined by
$$\begin{aligned}
C_{p, q} & :=\inf \left\{C>0 \mid\left\|S\left(\omega_{\varepsilon}\right)\right\|_{C_{\delta-4}^{0, \alpha}\left(B l_{p, q} X\right)} \leq C_{p, q} r_{\varepsilon}^{4-\delta}\right\} \\
C_{p} & :=\inf \left\{C>0 \mid\left\|S\left(\omega_{\varepsilon}\right)\right\|_{C_{\delta-4}^{0, \alpha}\left(B l_{p} X\right)} \leq C_{p} r_{\varepsilon}^{4-\delta}\right\}
\end{aligned}$$

Lemma 4.5. There exists a compact subset $K$ which contains $p$ such that $C_{p, q} \leq C_{p}$ for every $q \in X \backslash K$.

Proof. By definition of the weighted norm, we have
$$\begin{aligned}
\left\|S\left(\omega_{\varepsilon}\right)\right\|_{C_{-4}^{0, \alpha}\left(B l_{p} X\right)} & =\left\|S\left(\omega_{E}+i \partial \bar{\partial} \varphi_{p, \varepsilon}\right)\right\|_{C_{-4}^{0, \alpha}\left(A_{p}\right)} \\
\left\|S\left(\omega_{\varepsilon}\right)\right\|_{C_{\delta-4}^{0, \alpha}\left(B l_{p, q} X\right)} & =\max \left\{\left\|S\left(\omega_{E}+i \partial \bar{\partial} \varphi_{p, \varepsilon}\right)\right\|_{C_{\delta-4}^{0, \alpha}\left(A_{p}\right)},\left\|S\left(\omega_{E}+i \partial \bar{\partial} \varphi_{q, \varepsilon}\right)\right\|_{C_{\delta-4}^{0, \alpha}\left(A_{q}\right)}\right\}
\end{aligned}$$
Moreover, given that $S(\omega)=\left(g_{\omega}\right)^{\alpha \bar{\beta}}\left(R_{\omega}\right)_{\alpha \bar{\beta}}$, then we compute
$$\begin{aligned}
\left(g_{p, \varepsilon}\right)_{j \bar{k}} & =\delta_{j k}+\frac{\partial^{2} \varphi_{p, \varepsilon}}{\partial z_{j} \partial \bar{z}_{k}}(z) \\
\left(g_{q, \varepsilon}\right)_{j \bar{k}} & =\delta_{j k}+\frac{\partial^{2} \varphi_{q, \varepsilon}}{\partial z_{j} \partial \bar{z}_{k}}(z) \\
\left(R_{p, \varepsilon}\right)_{\alpha \bar{\beta}} & =2\left(g_{p, \varepsilon}\right)^{j \bar{k}}\left[\left(\frac{\partial^{3} \varphi_{p, \varepsilon}}{\partial z_{\alpha} \partial z_{j} \partial \bar{z}_{k}}\right)\left(\frac{\partial^{3} \varphi_{p, \varepsilon}}{\partial \bar{z}_{\beta} \partial z_{j} \partial \bar{z}_{k}}\right)-\left(\frac{\partial^{4} \varphi_{p, \varepsilon}}{\partial z_{\alpha} \partial \bar{z}_{\beta} \partial z_{j} \partial \bar{z}_{k}}\right)\right] \\
\left(R_{q, \varepsilon}\right)_{\alpha \bar{\beta}} & =2\left(g_{q, \varepsilon}\right)^{j \bar{k}}\left[\left(\frac{\partial^{3} \varphi_{q, \varepsilon}}{\partial z_{\alpha} \partial z_{j} \partial \bar{z}_{k}}\right)\left(\frac{\partial^{3} \varphi_{q, \varepsilon}}{\partial \bar{z}_{\beta} \partial z_{j} \partial \bar{z}_{k}}\right)-\left(\frac{\partial^{4} \varphi_{q, \varepsilon}}{\partial z_{\alpha} \partial \bar{z}_{\beta} \partial z_{j} \partial \bar{z}_{k}}\right)\right]
\end{aligned}$$
It is immediate to check that there exists a constant $c_{1}$ such that
$$\left\|\nabla^{i} \varphi_{p, \varepsilon}\right\|_{C_{\delta-i}^{4-i, \alpha}} \leq c_{1}\left\|\varphi_{p, \varepsilon}\right\|_{C_{\delta}^{4, \alpha}}, \quad\left\|\nabla^{i} \varphi_{q, \varepsilon}\right\|_{C_{\delta-i}^{4-i, \alpha}} \leq c_{1}\left\|\varphi_{q, \varepsilon}\right\|_{C_{\delta}^{4, \alpha}},$$
where the constant $c_{1}$ is independent of the function and on the points.
Thus, there exist constants $C_{1}$, independent of $\varphi_{p, \varepsilon}$ and $\varphi_{q, \varepsilon}$, respectively, such that
$$\left\|S\left(\omega_{E}+i \partial \bar{\partial} \varphi_{p, \varepsilon}\right)\right\|_{C_{\delta-4}^{0, \alpha}\left(A_{p}\right)} \leq C_{1}\left\|\varphi_{p, \varepsilon}\right\|_{C_{\delta}^{4, \alpha}\left(A_{p}\right)}$$
$$\left\|S\left(\omega_{E}+i \partial \bar{\partial} \varphi_{q, \varepsilon}\right)\right\|_{C_{\delta-4}^{0, \alpha}\left(A_{q}\right)} \leq C_{1}\left\|\varphi_{q, \varepsilon}\right\|_{C_{\delta}^{4, \alpha}\left(A_{q}\right)}$$
Using Remark 4.2 taking a sufficiently big compact subset $K$ containing $p$, we obtain
$$\begin{aligned}
\left\|S\left(\omega_{\varepsilon}\right)\right\|_{C_{\delta-4}^{0, \alpha}\left(B l_{p, q} X\right)} & =\max \left\{\left\|S\left(\omega_{E}+i \partial \bar{\partial} \varphi_{p, \varepsilon}\right)\right\|_{C_{\delta-4}^{0, \alpha}\left(A_{p}\right)},\left\|S\left(\omega_{E}+i \partial \bar{\partial} \varphi_{q, \varepsilon}\right)\right\|_{C_{\delta-4}^{0, \alpha}\left(A_{q}\right)}\right\} \\
& \leq \max \left\{C_{1}\left\|\varphi_{p, \varepsilon}\right\|_{C_{\delta}^{4, \alpha}\left(A_{p}\right)}, C_{1}\left\|\varphi_{q, \varepsilon}\right\|_{C_{\delta}^{4, \alpha}\left(A_{q}\right)}\right\} \\
& \leq C_{1}\left(c_{p}+c\right) r_{\varepsilon}^{4-\delta} .
\end{aligned}$$
for $q \in X \backslash K$.
Therefore, $C_{p, q} \leq C_{1}\left(c_{p}+c\right)=: C_{p}$. \(\square\)

\subsection*{4.2 Comparison between $K_{p, q}$ with $K_{p}$}

In this part we will to compare the bounds on the norm of the inverse linear operator associated to the scalar curvature in the construction of metrics on $B l_{p, q} X$ and on $B l_{p} X$. It is known that for every $\varphi \in C_{\delta, \delta_{\infty}}^{4, \alpha}\left(B l_{p, q} X\right)$ and $\psi \in C_{\delta, \delta_{\infty}}^{4, \alpha}\left(B l_{p} X\right)$ there exist $K_{p, q}$ and $K_{p}$ defined by
$$\begin{aligned}
K_{p, q} & :=\inf \left\{K>0 \mid\|\varphi\|_{C_{\delta, \delta \infty}^{4, \alpha}\left(B l_{p, q} X\right)} \leq K\left\|L_{\omega_{\varepsilon}}(\varphi)\right\|_{C_{\delta-4, \delta_{\infty}-4}^{0, \alpha}\left(B l_{p, q} X\right)}\right\}, \\
K_{p} & :=\inf \left\{K>0 \mid\|\psi\|_{C_{\delta, \delta_{\infty}}^{4, \alpha}\left(B l_{p} X\right)} \leq K\left\|L_{\omega_{\varepsilon}}(\psi)\right\|_{C_{\delta-4, \delta_{\infty}-4}^{0, \alpha}\left(B l_{p} X\right)}\right\} .
\end{aligned}$$

Lemma 4.6. $K_{p, q}$ goes to $K_{0} \leq K_{p}$ as $q$ goes to infinity.
Proof. Let $\varphi \in C_{\delta, \delta_{\infty}}^{4, \alpha}\left(B l_{p, q} X\right)$. We define the functions $\chi \varphi$ on $B l_{p}(X)$ and $\bar{\chi} \varphi$ on $B l_{q} X$ as follows
$$\chi \varphi=\left\{\begin{array}{l}
\varphi(z) \text { on } X_{p, q} \\
\varphi(z) \text { on } A_{p} \\
\varphi(z) \text { on } N_{p} \\
\gamma\left(\frac{|z|}{r_{\varepsilon}}\right) \varphi(z) \text { on } A_{q} \\
0 \quad \text { on } N_{q}
\end{array} \quad \bar{\chi} \varphi=\left\{\begin{array}{l}
0 \quad \text { on } X_{p, q} \\
0 \quad \text { on } A_{p} \\
0 \quad \text { on } N_{p} \\
\bar{\gamma}\left(\frac{|z|}{r_{\varepsilon}}\right) \varphi(z) \text { on } A_{2 q} \\
\varphi(z) \text { on } A_{q} \\
\varphi(z) \text { on } N_{q}
\end{array}\right.\right.$$
where $\gamma, \bar{\gamma}: \mathbb{R} \rightarrow[0,1]$ are smooth functions such that
$$\gamma(x)=\left\{\begin{array}{lll}
1 & \text { if } & x \geq 2 \\
0 & \text { if } & x \leq 1
\end{array} \quad \text { and } \quad \bar{\gamma}(x)=\left\{\begin{array}{lll}
0 & \text { if } & x \geq 3 \\
1 & \text { if } & x \leq 2
\end{array}\right.\right.$$

Note that it is possible to identify $\bar{\chi} \varphi$ around $p$, i.e. to compute the norm of the same function but with the metric near $p$. In this case, there exists a constant $K_{1}$, depending on $p$, such that
$$\begin{gathered}
\|\bar{\chi} \varphi\|_{C_{\delta, \delta \infty}^{4, \alpha}\left(B l_{q} X\right)}=\|\bar{\chi} \varphi\|_{C_{\delta}^{4, \alpha}\left(X_{q}\right)}+\|\bar{\chi} \varphi\|_{C_{\delta}^{4, \alpha}\left(A_{q}\right)}+\|\bar{\chi} \varphi\|_{C_{\delta}^{4, \alpha}\left(N_{q}\right)} \quad(\bar{\chi} \varphi \text { has compact support }) \\
\leq K_{1}\left(\|\bar{\chi} \varphi\|_{C^{4, \alpha}\left(X_{p}\right)}+\|\bar{\chi} \varphi\|_{C_{\delta}^{4, \alpha}\left(A_{p}\right)}\right)+\|\bar{\chi} \varphi\|_{C_{\delta}^{4, \alpha}\left(N_{p}\right)} .
\end{gathered}$$
Since
$$\|\varphi\|_{C_{\delta, \delta_{\infty}}^{4, \alpha}\left(B l_{p, q} X\right)}=\|\varphi\|_{C_{\infty}^{4, \alpha}\left(X_{p, q}\right)}+\max \left\{\|\varphi\|_{C_{\delta}^{4, \alpha}\left(A_{p}\right)},\|\varphi\|_{C_{\delta}^{4, \alpha}\left(A_{q}\right)}\right\}+\|\varphi\|_{C_{\delta}^{4, \alpha}\left(N_{p}\right)}+\|\varphi\|_{C_{\delta}^{4, \alpha}\left(N_{q}\right)},$$
then we have
$$\begin{aligned}
& \|\varphi\|_{C_{\delta, \delta \infty}^{4, \alpha}\left(B l_{p, q} X\right)} \leq\|\chi \varphi\|_{C_{\delta, \delta \infty}^{4, \alpha}\left(B l_{p} X\right)}+\|\bar{\chi} \varphi\|_{C_{\delta, \delta \infty}^{4, \alpha}\left(B l_{q} X\right)} \\
& \quad \leq K_{p}\left\|L_{\omega_{\varepsilon}}(\chi \varphi)\right\|_{C_{\delta-4, \delta_{\infty}-4}^{0, \alpha}\left(B l_{p} X\right)}+K_{1}\left(\|\bar{\chi} \varphi\|_{C^{4, \alpha}\left(X_{p}\right)}+\|\bar{\chi} \varphi\|_{C_{\delta}^{4, \alpha}\left(A_{p}\right)}\right)+\|\bar{\chi} \varphi\|_{C_{\delta}^{4, \alpha}\left(N_{p}\right)} \\
& \quad \leq K_{p}\left(\left\|L_{\omega}(\chi \varphi)\right\|_{C_{\delta \infty-4}^{0, \alpha}\left(X_{p, q}\right)}+\left\|L_{\omega}(\chi \varphi)\right\|_{C_{\delta \infty-4}^{0, \alpha}\left(A_{q}\right)}+\left\|L_{\omega_{\varepsilon}}(\chi \varphi)\right\|_{C_{\delta-4}^{0, \alpha}\left(A_{p}\right)}+\left\|L_{\varepsilon^{2} \eta_{B S}}(\chi \varphi)\right\|_{C_{\delta-4}^{0, \alpha}\left(N_{p}\right)}\right. \\
& \left.\quad \quad+K_{1}\left\|L_{\omega}(\bar{\chi} \varphi)\right\|_{C^{0, \alpha}\left(X_{p}\right)}+K_{1}\left\|L_{\omega_{\varepsilon}}(\bar{\chi} \varphi)\right\|_{C_{\delta-4}^{0, \alpha}\left(A_{p}\right)}+\left\|L_{\varepsilon^{2} \eta_{B S}}(\bar{\chi} \varphi)\right\|_{C_{\delta-4}^{0, \alpha}\left(N_{p}\right)}\right) \\
& \quad \leq K_{p}\left\|L_{\omega_{\varepsilon}}(\varphi)\right\|_{C_{\delta-4, \delta_{\infty}-4}^{0, \alpha}\left(B l_{p, q} X\right)}+K_{p}\left(\left\|L_{\omega}(\chi \varphi)\right\|_{C_{\delta_{\infty}^{0, \alpha}}^{0, \alpha}\left(A_{q}\right)}+K_{1}\left(\left\|L_{\omega}(\bar{\chi} \varphi)\right\|_{C^{0, \alpha}\left(X_{p}\right)}+\left\|L_{\omega_{\varepsilon}}(\bar{\chi} \varphi)\right\|_{C_{\delta-4}^{0, \alpha}\left(A_{p}\right)}\right)\right) .
\end{aligned}$$
Moreover, as $L$ is a linear operator at each metric, we get that there exists a constant $K_{2}$, depending on $p$, such that
$$\begin{aligned}
\left\|L_{\omega}(\chi \varphi)\right\|_{C_{\delta_{\infty}-4}^{0, \alpha}\left(A_{q}\right)} & \leq K_{2}\|\chi \varphi\|_{C_{\infty}^{4, \alpha}\left(A_{q}\right)} \\
\left\|L_{\omega}(\bar{\chi} \varphi)\right\|_{C^{0, \alpha}\left(X_{p}\right)} & \leq K_{2}\|\bar{\chi} \varphi\|_{C^{4, \alpha}\left(X_{p}\right)} \\
\left\|L_{\omega_{\varepsilon}}(\bar{\chi} \varphi)\right\|_{C_{\delta-4}^{0, \alpha}\left(A_{p}\right)} & \leq K_{2}\|\bar{\chi} \varphi\|_{C_{\delta}^{4, \alpha}\left(A_{p}\right)}
\end{aligned}$$
Also, we may assume that there exist constants $K_{3}$ and $K_{4}$ depending only on $p$ as $q$ goes to infinity, such that
$$\|\bar{\chi} \varphi\|_{C^{4, \alpha}\left(X_{p}\right)} \leq K_{3}\|\bar{\chi} \varphi\|_{C^{4, \alpha}\left(X_{q}\right)}, \quad\|\bar{\chi} \varphi\|_{C_{\delta}^{4, \alpha}\left(A_{p}\right)} \leq K_{4}\|\bar{\chi} \varphi\|_{C_{\delta}^{4, \alpha}\left(A_{q}\right)} .$$
Thus, there exists a constant $K$ which depends on $p$ as $q$ goes to infinity such that
$$\|\varphi\|_{C_{\delta, \delta_{\infty}}^{4, \alpha}\left(B l_{p, q} X\right)} \leq K_{p}\left\|L_{\omega_{\varepsilon}}(\varphi)\right\|_{C_{\delta-4, \delta_{\infty}-4}^{0, \alpha}\left(B l_{p, q} X\right)}+K_{p} K\left(\|\chi \varphi\|_{C_{\delta_{\infty}}^{4, \alpha}\left(A_{q}\right)}+\|\bar{\chi} \varphi\|_{C^{4, \alpha}\left(X_{q}\right)}+\|\bar{\chi} \varphi\|_{C_{\delta}^{4, \alpha}\left(A_{q}\right)}\right) .$$

Moreover, properties on the weighted norms imply
$$\begin{gathered}
\|\chi \varphi\|_{C_{\delta_{\infty}}^{4, \alpha}\left(A_{q}\right)} \leq r(q)^{\delta_{\infty}}\|\chi \varphi\|_{C_{\delta, \delta \infty}^{4, \alpha}\left(B l_{q}(X)\right)} \\
\|\bar{\chi} \varphi\|_{C^{4, \alpha}\left(X_{q}\right)}+\|\bar{\chi} \varphi\|_{C_{\delta}^{4, \alpha}\left(A_{q}\right)} \leq r(q)^{\delta_{\infty}}\|\bar{\chi} \varphi\|_{C_{\delta, \delta}^{4, \alpha}\left(B l_{q}(X)\right)}
\end{gathered}$$
where $r(q)$ is the distance between $q$ and a compact subset $K \subset X$ containing $p$. Since $r(q)$ goes to infinity as $q$ goes to infinity and $\delta_{\infty}<0$, we get
$$\|\varphi\|_{C_{\delta, \delta \infty}^{4, \alpha}\left(B l_{p, q} X\right)} \leq K_{p}\left\|L_{\omega_{\varepsilon}}(\varphi)\right\|_{C_{\delta-4, \delta_{\infty}-4}^{0, \alpha}\left(B l_{p, q} X\right)}, \quad \text { as } q \text { goes to infinity } .$$ \(\square\)

Proof of Theorem 4.1. Following Remark 4.4 and (i), (ii), if we choose $c_{1}=1 / 2 K_{p, q}$ then
$$\varepsilon_{0}(p, q):=\left(\frac{1}{2 K_{p, q} \sqrt{C_{p, q}}}\right)^{\frac{m}{m-1}}$$
and for every $\varepsilon<\varepsilon_{0}(p, q)$ we have
$$K_{p, q} C_{p, q} r_{\varepsilon}^{2}<\frac{1}{2} c_{1} .$$
Using Lemma 4.5 and Lemma 4.6, we get, for $q$ sufficintely far away from $p$
$$\varepsilon_{0}(p, q):=\left(\frac{1}{2 K_{p, q} \sqrt{C_{p, q}}}\right)^{\frac{m}{m-1}} \geq\left(\frac{1}{2 K_{p, q} \sqrt{C_{p}}}\right)^{\frac{m}{m-1}} \longrightarrow\left(\frac{1}{2 K_{p} \sqrt{C_{p}}}\right)^{\frac{m}{m-1}} .$$
Therefore, $\varepsilon_{0}(p, q)$ goes to $\varepsilon_{0} \geq \varepsilon_{0}(p)$. \(\square\)

\section*{5 ADM mass under blow ups, proof of the main results}

We now analyze the effects of the previous results on the ADM mass of a scalar flat ALE space. Thanks to the formula due to Hein-LeBrun ([11]) (Theorem 2.2), this is easily achieved by the following

Proposition 5.1. Let $m(X, h)$ and $m\left(B l_{p} X, h_{\varepsilon}\right)$ be the $A D M$ mass of $(X, \Gamma, h, \omega)$ and $B l_{p} X$ respectively, where $h_{\varepsilon}$ is the scalar flat metric produced out of $h$ by Theorem 3.1. Then,
$$m\left(B l_{p} X, h_{\varepsilon}\right)=m(X, h)+\frac{(m-1) \varepsilon^{2(m-1)}}{(2 m-1) \pi^{m-1}} .$$

Proof. Since $\omega_{\varepsilon} \in \pi^{*}[\omega]-\varepsilon^{2} P D\left[E_{p}\right]$ and we have normalized the Burns-Simanca metric in a way that $\left[\eta_{B S}\right]=-P D\left[E_{p}\right]$ then
$$\left[\omega_{\varepsilon}\right]=[\omega]+\varepsilon^{2}[\eta], \quad c_{1}\left(B l_{p} X\right)=\pi^{*}\left(c_{1}(X)\right)-(m-1) P D\left[E_{p}\right] .$$
By Theorem 2.2 we have
$$\begin{aligned}
m\left(B l_{p} X, h_{\varepsilon}\right) & =-\frac{\left\langle\boldsymbol{o}\left(c_{1}\left(B l_{p} X\right)\right),\left[\omega_{\varepsilon}\right]^{m-1}\right\rangle}{(2 m-1) \pi^{m-1}} \\
& =-\frac{\left\langle\boldsymbol{\alpha}\left(c_{1}(X)-(m-1) P D\left[E_{p}\right]\right),\left([\omega]-\varepsilon^{2} P D\left[E_{p}\right]\right)\right\rangle}{(2 m-1) \pi^{m-1}} \\
& =m(X, h)+\frac{(m-1) \varepsilon^{2(m-1)}}{(2 m-1) \pi^{m-1}} .
\end{aligned}$$ \(\square\)

Proof of Theorem 1.1: Proposition 5.1 shows that each time we blow up a point $p$ we can increase the ADM mass of any amount up to
$$\frac{(m-1) \varepsilon_{0}(p)^{2(m-1)}}{(2 m-1) \pi^{m-1}} .$$
Theorem 4.1 shows that iterating the process taking a second point sufficiently far away from the first one, we can increase again the ADM mass by the same amount (at least). Of course, blowing up points does not change the structure groups at infinity of the original ALE space. Given that the process can be iterated infinitely many times, the theorem is proved. \(\square\)

\section*{References}
\begin{itemize}
\item[] [1] C. Arezzo, A. Della Vedova and L. Mazzieri. K-stability, Futaki invariants and cscK metrics on orbifold resolutions, arXiv:1808.08420.
\item[] [2] C. Arezzo and F. Pacard. Blowing up and desingularizing constant scalar curvature Kähler manifolds, Acta Math. 196 (2006), no.2, 179-228.
\item[] [3] C. Arezzo and F. Pacard. Blowing up Kähler manifolds with constant scalar curvature II, Annals of Math. 170 (2009), 685-738.
\item[] [4] R. Arnowitt, S. Deser, and C. W. Misner. Coordinate Invariance and Energy Expressions in General Relativity Phys. Rev. 122 (1961), 997-1006.
\item[] [5] R. Bartnik. The mass of an asymptotically flat manifold CPAM 39(1986), 661-693.
\end{itemize}
\begin{itemize}
\item[] [6] E. Calabi. Métriques kählériennes et fibrés holomorphes, Ann. Sci. École Norm. Sup. 12 (1979), 269-294.
\item[] [7] D. Calderbank and M. Singer. Einstein metrics and complex singularities, Invent. Math. 156 (2004), 405-443.
\item[] [8] P. Chruściel. Boundary conditions at spatial infinity from a Hamiltonian point of view, in Topological Properties and Global Structure of Space-Time, Adv. Sci. Inst. Ser. B Phys., 138 (1986), 49-59.
\item[] [9] S.K. Donaldson. Scalar Curvature and Stability of Toric Varieties J. Differential Geom. 62, (2002), 289-349.
\item[] [10] J. Han and J. Viaclovsky. Existence and compactness theory for ALE scalar-flat Kähler surfaces, Forum Math. 8 (2020).
\item[] [11] H. J. Hein and C. LeBrun. Mass in Kähler geometry, Commun. Math. Phys. 347 (2016), 183-221.
\item[] [12] N. Honda. Deformation of LeBrun's ALE metrics with negative mass, Comm. Math. Phys. 322 (2013), 127-148.
\item[] [13] D. Joyce. Compact Manifolds with special holonomy. Oxford Mathematical Monographs, Oxford University Press. (2000).
\item[] [14] P. Kronheimer. The construction of ALE spaces as hyper-Kähler quotients. J. Differential Geom. 29 (1989), 665-683.
\item[] [15] C. LeBrun. Counter-examples to the generalized positive action conjecture, Comm. Math. Phys., 118 (1988), 591-596.
\item[] [16] M. Lock and J. Viaclovsky. A Smörgäsbord of scalar-flat Kähler ALE surfaces, J. Reine Agnew. Math. 746 (2019), 171-208.
\item[] [17] Y. Rollin and M. Singer. Constant scalar curvature Kähler Surfaces and Parabolic stability, J. Geom. Anal. 19 (2009), 107-136.
\item[] [18] G. Székelyhidi. An introduction to extremal Kähler metrics, American Mathematical Soc., 152 (2014).
\item[] [19] G. Székelyhidi. Extremal Kähler metrics, Proceedings of the ICM, Vol. 2, Seoul 2014, 1017-1033.
\end{itemize}
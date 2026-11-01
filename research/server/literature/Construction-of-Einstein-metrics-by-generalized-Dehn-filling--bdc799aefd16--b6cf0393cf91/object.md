# Construction of Einstein metrics by generalized Dehn filling

- Category: papers
- Identity: arxiv:0911.4730
- Content status: fulltext_ok

---

---
source_file: 0911_4730.pdf
converter: mathpix
format: mmd
---

\title{
CONSTRUCTION OF EINSTEIN METRICS BY GENERALIZED DEHN FILLING
}

\author{
RICHARD H BAMLER
}

\begin{abstract}
In this paper, we present a new approach to the construction of Einstein metrics by a generalization of Thurston's Dehn filling. In particular in dimension 3, we will obtain an analytic proof of Thurston's result.
\end{abstract}

\section*{1. Introduction}

The goal of this paper is to give an analytic construction of Riemannian metrics $g$ which satisfy the Einstein equation $\operatorname{Ric}_{g}=-(n-1) g$, by a process similar to Thurston's Dehn filling (see [Thu]). We will first describe the topology of the manifolds on which these metrics live:

Let $\left(M_{\text {hyp }}^{n}, g_{\text {hyp }}\right)$ be a hyperbolic manifold of dimension $n \geq 3$ and finite volume. Denote its cusps by $N_{1}, \ldots, N_{p}$ and assume that these are diffeomorphic to $[0, \infty) \times T^{n-1}$, i.e. that the cusps are standard. We can always choose the $N_{k}$ so that they are bounded by tori $T_{k}=\partial N_{k}$ which are images of horospheres under the universal covering projection and on which $\operatorname{inj}=\mu_{n}$ where inj is the injectivity radius and $\mu_{n}$ the Margulis constant. (For a more detailed description see subsection 2.1.) Now apply the following surgery procedure: Cut $M_{\text {hyp }}$ along the $T_{k}$, throw away the cusps $N_{k}$ and glue in $p$ solid tori $\approx D^{2} \times T^{n-2}$ by identifying their boundary with the $T_{k}$. The topology of the resulting manifold can be uniquely characterized by the homotopy classes of meridional loops $\sigma_{k} \subset \partial\left(D^{2} \times T^{n-2}\right)$ inside the $T_{k}$ (i.e. images of loops $S^{1} \times\{p t\} \subset D^{2} \times T^{n-2}$ under the gluing identification $\partial\left(D^{2} \times T^{n-2}\right) \rightarrow T_{k}$ ). These homotopy classes are simple, i.e. not a nontrivial multiple of another homotopy class. Vice versa, given a homotopy class of a simple closed loop $\sigma_{k} \subset T_{k}$ for each $k$, we can produce a manifold $M_{\bar{\sigma}}=M_{\left(\sigma_{1}, \ldots, \sigma_{p}\right)}$ by this gluing. In the following we will always assume that the $\sigma_{1}, \ldots, \sigma_{p}$ are geodesic representatives (inside $T_{1}, \ldots, T_{p}$ ) of their homotopy classes and set $\ell_{k}:=\ell\left(\sigma_{k}\right)$ and $\ell_{\text {min resp. max }}:=($ min resp. max $)\left(\ell_{k}\right)$.

The statement of the theorem which we are going to prove, is now:
Theorem 1.1. There is a constant $L=L(n, V)$ such that whenever $\operatorname{vol} M_{\text {hyp }}<V$ and $\ell_{\text {min }}>L$, the manifold $M_{\bar{\sigma}}$ carries an Einstein metric $g_{\bar{\sigma}}$.

Moreover, the metrics on $M_{\bar{\sigma}}$ can be constructed in such a way that as $\ell_{\text {min }} \rightarrow$ $\infty$, the $\left(M_{\bar{\sigma}}, g_{\bar{\sigma}}\right)$ converge to the initial hyperbolic manifold $\left(M_{\text {hyp }}, g_{\text {hyp }}\right)$ in the pointed Gromov-Hausdorff sense if the basepoints are chosen away from the cusps.

\footnotetext{
Date: November 10, 2009.
}

A slightly weaker statement was also claimed in [And2]. Theorem 1.1 immediately implies the Dehn filling Theorem in dimension 3:

Corollary 1.2. Let the dimension $n=3$. There is a constant $L=L(V)$ such that whenever $\operatorname{vol} M_{\text {hyp }}<V$ and $\ell_{\text {min }}>L$, the manifold $M_{\bar{\sigma}}$ is hyperbolic.

A slightly weaker version of this theorem was proven by Thurston ([Thu]) using the deformation theory of Kleinian groups. Our methods provide a new and analytic proof of his result.

We will give a short sketch of the proof of Theorem 1.1: First, we endow the solid tori which we will glue into the hyperbolic manifold $M_{\text {hyp }}$ with a special Einstein metric called the black-hole metric. This metric is asymptotically hyperbolic to its end and thus each gluing can be arranged to be arbitrarily smooth for large $\ell_{k}$. Hence, the resulting metric is almost Einstein, i.e. its traceless Ricci tensor is small in some $C^{m, \alpha}$-sense. Eventually, we apply an inverse function theorem like argument to perturb the metric into the desired Einstein metric.

We mention that our proof builds on previous work of Tian ([Tia]) and Anderson ([And2]). Tian established the 3-dimensional case in which $M_{\text {hyp }}$ has only one cusp. Later Anderson described a construction for the higher dimensional case and developed new analytical tools of which we will also partly make use here.

We want to point out that the case in which the hyperbolic manifold $M_{\text {hyp }}$ has more than one cusp, is substantially more difficult than the case of one cusp for the following reason: The accuracy of the gluing in the first step (i.e. the construction of the almost Einstein metric) depends polynomially on the minimum $\ell_{\text {min }}$ of the $\ell_{k}$. However, as the $\ell_{k}$ get large, the invertibility of the linearized Einstein equation deteriorates logarithmically in the maximum $\ell_{\text {max }}$ of the $\ell_{k}$. So in the case of one cusp $\ell_{\text {min }}=\ell_{\text {max }}$ and thus the accuracy of the gluing increases more rapidly than the invertibility deteriorates. But if $M_{\text {hyp }}$ has more than one cusp and $\ell_{\text {min }}, \ell_{\text {max }}$ are not sufficiently controlled with respect to one another, then this consideration fails. In [And2], Anderson sketches an argument how to get around this issue by looking at certain moduli spaces of solutions of a modified Einstein equation. In this paper, we will be able to deal with the problems that arise in this multiple cusp case and we will give a complete proof of Theorem 1.1. In fact, our argument will be more elementary and we find it a more natural way of looking at the problem.

The idea behind our proof is that the reason for the bad invertibility of the linearized Einstein equation lies in certain variations of the metric (so called trivial Einstein variations) which correspond to a change of the moduli of the cross-sectional tori of the cusps. It will turn out that with respect to some cleverly chosen norms (see section 4), which treat these trivial Einstein variations separately, the invertibility of the linearized Einstein equation becomes in fact independent of $\ell_{\text {max }}$ (see our Proposition 5.1 as opposed to Proposition 3.2 in [And2]). However, these new norms make it necessary to reprove the inverse function theorem in order to be applicable to our setting (see section 5).

Another difference between our and Anderson's proof is that we have replaced the proof of Lemma 3.4 in [And2] which used to involve the theory of the moduli spaces of conformally compact Einstein metrics, by an elementary argument by which we can even show a slight generalization.

We remark that it still remains an interesting question whether the constant $L$ in Theorem 1.1 can be chosen independent of the volume of $M_{\text {hyp }}$. Hodgson and Kerckhoff (see [HK]) could confirm this in dimension 3 using algebraic techniques.

The paper is organized as follows: In section 2, we will review some basic facts which were also used in [And2]. Section 3 contains a brief recapitulation of the construction of the almost Einstein metric as described in [And2]. In sections 4 to 6 we carry out the main argument. In order to keep these chapters concise, we will defer most of the technical calculations to sections 7 and 8.

I want to thank my advisor Gang Tian for calling my attention on this subject and for his continual support. I am also indebted to the HIM in Bonn for their hospitality and Hans-Joachim Hein for many inspiring discussions.

\section*{2. Preliminaries}
2.1. Hyperbolic manifolds. We recall the thick-thin-decomposition for hyperbolic manifolds

Theorem 2.1. There is a constant $\mu_{n}>0$, the Margulis constant, such that the following holds: If $M_{\text {hyp }}^{n}$ is a finite volume hyperbolic manifold then $M_{\text {hyp }}$ can be decomposed into a thin part $M_{\text {thin }}$ and a thick part $M_{\text {thick }}$ with $M_{\text {hyp }}=$ $M_{\text {thin }} \dot{\cup} M_{\text {thick }}$ such that:
\begin{itemize}
\item[-] $\operatorname{inj} \geq \mu_{n}$ on $M_{\text {thick }}$ and $M_{\text {thick }}$ is relatively compact in $M_{\text {hyp }}$.
\item[-] $M_{\text {thin }}$ is a finite union of connected open sets $N_{1}, \ldots, N_{p}$ and $N_{1}^{\prime}, \ldots, N_{p^{\prime}}^{\prime}$ where
\begin{itemize}
\item[-] the $N_{k}$ are cusps of the form $[0, \infty) \times\left(T^{n-1} / \Gamma_{k}\right)$ for finite subgroups $\Gamma_{k}<\operatorname{Isom} T^{n-1}$ with a warped product metric
$$g_{h y p}=d s^{2}+e^{-2 s} g_{f l a t, T^{n-1} / \Gamma_{k}} .$$
In the case in which $\Gamma_{k}=\{1\}$, we call $N_{k}$ standard.
\item[-] and the $N_{k}^{\prime}$ are covered by cylindrical neighborhoods around geodesics in hyperbolic space.
Furthermore, we can choose the $N_{k}$ such that their boundaries are images of horospheres under the universal covering projection and such that inj = $\mu_{n}$ at some point on $\partial N_{k}$. In the case in which $N_{k}$ is standard this implies that $\operatorname{inj}=\mu_{n}$ on $\partial N_{k}$.
\end{itemize}
\end{itemize}
In every dimension, $\operatorname{diam} M_{\text {thick }}$ is bounded from above by a constant which only depends on an upper bound on $\mathrm{vol} M_{\text {hyp }}$ and in dimension $n \geq 4$, this is even true for the diameter of $M_{\text {thick }} \cup N_{1}^{\prime} \cup \ldots \cup N_{p^{\prime}}^{\prime}=M_{\text {hyp }} \backslash N_{1} \cup \ldots \cup N_{p}$.

We can compute the volume of the cusps in terms of the area of their boundary surface:

Lemma 2.2. There is a constant $\eta_{n}$ such that for all cusps $N_{k}$ we have
$$\operatorname{vol} N_{k}=\eta_{n} \operatorname{vol} \partial N_{k} .$$
Proof. This can be checked easily using (2.1). \(\square\)

So a bound on the volume of $M_{\text {hyp }}$ gives us a bound on the volume of the $\partial N_{k}$. Since $\partial N_{k}$ lies in the thick part, we have a bound on the injectivity radius of $\partial N_{k}$ (which is slightly larger than $\mu_{n}$ since $\partial N_{k}$ is not totally geodesic). The next lemma shows that in fact we get a bound on the diameter of $\partial N_{k}$ from an upper volume bound on $M_{\text {hyp }}$. This implies furthermore, that the tori that can occur as cusp cross-sections of a hyperbolic manifold with a given volume bound form a bounded subset in the moduli space of flat tori.

Lemma 2.3. For every $V<\infty$ and $\iota>0$ there is a $d(n, V, \iota)<\infty$ such that for any flat torus $T^{n-1}$ we have
$$\operatorname{vol} T^{n-1}<V \quad \text { and } \quad \operatorname{inj} T^{n-1}>\iota \quad \Longrightarrow \quad \operatorname{diam} T^{n-1}<d .$$
Proof. Let $\gamma:[0, l] \rightarrow T^{n-1}$ be a minimizing geodesic. Then the balls $B_{\iota}(\gamma(\iota))$, $B_{\iota}(\gamma(3 \iota)), \ldots$ are pairwise disjoint and have volume $\omega_{n-1} \iota^{n-1}$. So $l<2\left(\frac{V}{\omega_{n-1} \iota^{n-1}}+\right.$ 1) $\iota$. \(\square\)
2.2. The Einstein operator. For any symmetric bilinear form $h$ and any 1-form $\alpha$ on a Riemannian manifold $(M, g)$ we define the divergence and its formal conjugate by ( $e_{k}$ is a local orthonormal frame field)
$$\operatorname{div}_{g}(h)=-\sum_{i=1}^{n}\left(\nabla_{e_{i}} h\right)\left(e_{i}, \cdot\right), \quad\left(\operatorname{div}_{g}^{*} \alpha\right)(X, Y)=\frac{1}{2}\left(\left(\nabla_{X} \alpha\right)(Y)+\left(\nabla_{Y} \alpha\right)(X)\right) .$$
Observe that $\operatorname{div}_{g}^{*} \alpha=\frac{1}{2} \mathcal{L}_{\alpha^{\sharp}} g$. Let $h$ be a bilinear form. We can express the derivative of the Ricci curvature in the direction of $h$ by (for a computation see [Top, sec 2.3])
$$\mathrm{d} \operatorname{Ric}_{g}(h)=-\frac{1}{2} \triangle_{L} h-\operatorname{div}_{g}^{*}\left(\operatorname{div}_{g} h+\frac{1}{2} \operatorname{dtr}_{g} h\right) .$$
Here $\left(\triangle_{L} h\right)(X, Y)=(\triangle h)(X, Y)+2 R(h)(X, Y)-h(\operatorname{Ric}(X), Y)-h(X, \operatorname{Ric}(Y))$ is the Lichnerowicz Laplacian and $R(h)(X, Y)=\operatorname{tr} h(R(\cdot, X) Y, \cdot)$. Since computing the Ricci tensor is a diffeomorphism invariant operation, we have for any 1-form $\alpha$
$$\mathrm{d} \operatorname{Ric}_{g}\left(\operatorname{div}_{g}^{*} \alpha\right)=\frac{1}{2} \mathcal{L}_{\alpha^{\sharp}} \operatorname{Ric}_{g} .$$
Thus $\mathrm{dRic}_{g}$ is not an elliptic operator. In order to make it elliptic, we have to add an extra term: Let $\bar{g}$ be an arbitrary fixed background metric on $M$. We define $\Psi_{\bar{g}}:\left\{g \in C^{\infty}\left(M ; \operatorname{Sym}_{2} T^{*}\right): g>0\right\} \rightarrow C^{\infty}\left(M ; \operatorname{Sym}_{2} T^{*}\right)$ by
$$\Psi_{\bar{g}}(g):=\operatorname{Ric}_{g}+\operatorname{div}_{g}^{*}\left(\operatorname{div}_{\bar{g}} g+\frac{1}{2} \operatorname{dtr}_{\bar{g}} g\right) .$$
Its derivative at $\bar{g}$ is
$$\left(\mathrm{d} \Psi_{\bar{g}}\right)_{\bar{g}}(h)=-\frac{1}{2} \triangle_{L} h$$
hence elliptic. For our purposes we define the Einstein operator $\Phi_{\bar{g}}:\{g \in$ $\left.C^{\infty}\left(M ; \operatorname{Sym}_{2} T^{*}\right): g>0\right\} \rightarrow C^{\infty}\left(M ; \operatorname{Sym}_{2} T^{*}\right)$ by
$$\Phi_{\bar{g}}(g)=\Psi_{\bar{g}}(g)+(n-1) g .$$
We have
$$\begin{aligned}
&\left(\mathrm{d} \Phi_{\bar{g}}\right)_{\bar{g}}(h)=-\frac{1}{2} \triangle_{L} h+(n-1) h \\
& \quad=\frac{1}{2}(-\triangle h-2 R(h)+\text { Ric } \circ h+h \circ \operatorname{Ric}+2(n-1) h) .
\end{aligned}$$
Set $L_{\bar{g}}:=2\left(\mathrm{~d} \Phi_{\bar{g}}\right)_{\bar{g}}$ and call elements in the kernel of $L_{\bar{g}}$ Einstein variations. Using a Weitzenböck formula, we can express this linear operator as
$$L_{\bar{g}} h=\left(\operatorname{div}^{*} \operatorname{div}+d^{*} d\right) h-R(h)+\frac{1}{2} \operatorname{Ric} \circ h+\frac{1}{2} h \circ \operatorname{Ric}+2(n-1) h$$
where $d: C^{\infty}\left(M ; \operatorname{Sym}_{2} T^{*}\right) \rightarrow C^{\infty}\left(M ; \Lambda_{2} T^{*} \otimes T^{*}\right)$ and its formal conjugate $d^{*}$ : $C^{\infty}\left(M ; \Lambda_{2} T^{*} \otimes T^{*}\right) \rightarrow C^{\infty}\left(M ; \operatorname{Sym}_{2} T^{*}\right)$ are defined by
$$\begin{aligned}
(d h)(X, Y, Z)=\left(\nabla_{X} h\right)(Y, Z) & -\left(\nabla_{Y} h\right)(X, Z), \\
& \left(d^{*} t\right)(X, Y)=-\frac{1}{2} \sum_{i=1}^{n}\left(\left(\nabla_{e_{i}} t\right)\left(e_{i}, X, Y\right)+\left(\nabla_{e_{i}} t\right)\left(e_{i}, Y, X\right)\right) .
\end{aligned}$$
If $\bar{g}$ is Einstein with $\operatorname{Ric}_{\bar{g}}=-(n-1) \bar{g}$, we have
$$L_{\bar{g}} h=-\triangle h-2 R(h)=\left(\operatorname{div}^{*} \operatorname{div}+d^{*} d\right) h-R(h)+(n-1) h .$$
Tracing this equation gives us
$$\operatorname{tr} L_{\bar{g}} h=\nabla^{*} \nabla \operatorname{tr} h+2(n-1) \operatorname{tr} h .$$
If $\bar{g}$ is hyperbolic of constant sectional curvature -1, we get
$$L_{\bar{g}} h=-\triangle h-2 h+2\left(\operatorname{tr}_{\bar{g}} h\right) \bar{g}=\left(\operatorname{div}^{*} \operatorname{div}+d^{*} d\right) h+(\operatorname{tr} h)_{\bar{g}} \bar{g}+(n-2) h .$$

Lemma 2.4. If $M$ is closed and $\operatorname{Ric}_{g}<0$, then $\Phi_{\bar{g}}(g)=0$ implies $\operatorname{Ric}_{g}=$ $-(n-1) g$.

Proof. This Lemma can be found in [Biq1] and [And2, Lemma 2.1]. We copy the proof from the latter source since we need a variation of the argument later on. Let $\beta_{g}(h):=\operatorname{div}_{g} h+\frac{1}{2} \mathrm{dtr}_{g} h$ be the Bianchi operator. Applying $\beta_{g}$ to $\Phi_{\bar{g}}(g)=0$ yields
$$0=\beta_{g}\left(\Phi_{\bar{g}}(g)\right)=\beta_{g} \operatorname{div}_{g}^{*} \beta_{\bar{g}}(g)=\frac{1}{2}\left(\nabla^{*} \nabla \beta_{\bar{g}}(g)-\operatorname{Ric}_{g}\left(\beta_{\bar{g}}(g)\right)\right) .$$
So $\beta_{\bar{g}}(g)=0$ and the claim follows. \(\square\)

Thus, in order to construct Einstein metrics, it suffices to look for zeros of $\Phi_{\bar{g}}$.
A similar result to Lemma 2.4 holds in the differential sense:
Lemma 2.5. If $(M, \bar{g})$ is a complete Einstein manifold and $h$ a symmetric bilinear form such that $|h|(x),|\nabla h|(x) \rightarrow 0$ for $x \rightarrow \infty$, then $L_{\bar{g}} h=0$ implies
$$\mathrm{d} \operatorname{Ric}_{\bar{g}}(h)=-(n-1) h, \quad \operatorname{div}_{\bar{g}} h=0, \quad \operatorname{tr}_{\bar{g}} h=0 .$$

Proof. The proof is the same as in [And1, Lemma 3.6]. Differentiate (2.5) with respect to $g$ to find
$$0=\beta_{\bar{g}} L_{\bar{g}} h=\nabla^{*} \nabla \beta_{\bar{g}} h+(n-1) \beta_{\bar{g}} h .$$
So $\beta_{\bar{g}} h=0$. Moreover, by (2.3) we conclude $\operatorname{tr} h=0$. \(\square\)

Observe that conversely not every Einstein variation is divergence or trace free.
2.3. The hyperbolic cusp. We introduce a representation for the metric $g_{\text {hyp }}$ on a hyperbolic cusp which is different from (2.1): Consider the coordinates $\left(r, x_{2}, \ldots, x_{n}\right)$ on $\mathbb{R}_{+} \times \mathbb{R}^{n-1}$ and the hyperbolic metric
$$g_{\text {hyp }}=r^{-2} \mathrm{~d} r^{2}+r^{2}\left(\mathrm{~d} x_{2}^{2}+\ldots+\mathrm{d} x_{n}^{2}\right) .$$
Note that in these coordinates, $g_{\text {hyp }}$ is not conformally equivalent to the Euclidean metric (as opposed to the coordinates that arise after the transformation $r \rightarrow \frac{1}{r}$ ). Obviously, the metric is invariant under the action by Euclidean isometries on the last factor. Now every hyperbolic cusp is the quotient of $\mathbb{R}_{+} \times \mathbb{R}^{n-1}$ metric under a discrete subgroup of those isometries.

We will be interested in Einstein deformations of the metric $g_{h y p}$ which are invariant by the group $\mathbb{R}^{n-1}$ of Euclidean tranformations on the last factor. One type of deformation will be very essential: Let $u_{i j}$ be a symmetric $(n-1) \times(n-1)$ matrix indexed by $i, j=2, \ldots, n$. Then if $u_{i j}>-\delta_{i j}$
$$r^{-2} \mathrm{~d} r^{2}+r^{2}\left(\mathrm{~d} x_{2}^{2}+\ldots+\mathrm{d} x_{n}^{2}+u_{i j} \mathrm{~d} x_{i} \mathrm{~d} x_{j}\right)$$
is isometric to $g_{\text {hyp }}$ hence it is also Einstein. We will denote this metric by $g_{\text {hyp }}+u$. It can be checked (e.g. using (2.3)) that the equation $\Phi_{g_{h y p}}\left(g_{h y p}+u\right)=0$ is equivalent to $\operatorname{tr} u=0$. Likewise, dropping the lower bound for $u_{i j}$ and setting $h=r^{2} u_{i j} \mathrm{~d} x_{i} \mathrm{~d} x_{j}$, we find that $L_{g_{h y p}} h=0$ iff $\operatorname{tr} u=0$. We will call variations of this kind trivial Einstein variations.
2.4. The black-hole metric. We recall the definition of the black-hole metric $\left(M_{B H}, g_{B H}\right)$ as in [And2]. Introduce coordinates $\left(r, \theta, x_{3}, \ldots, x_{n}\right)$ on $\mathbb{R}^{n}=\mathbb{R}^{2} \times$ $\mathbb{R}^{n-2}$. Here, $(r, \theta)$ denote polar coordinates on the first factor such that $r$ is running from $r_{+}=2^{1 / n-1}$ to $\infty$ and $\theta$ from 0 to $\beta=\frac{4 \pi}{(n-1) r_{+}}$. The black-hole metric is defined as
$$g_{B H}=V^{-1} \mathrm{~d} r^{2}+V \mathrm{~d} \theta^{2}+r^{2}\left(\mathrm{~d} x_{3}^{2}+\ldots+\mathrm{d} x_{n}^{2}\right)$$
where
$$V(r)=r^{2}-\frac{2}{r^{n-3}} .$$
Using the coordinate transformation $r=r_{+}+\frac{1}{2} s^{2}$, we obtain
$$g_{B H}=\frac{s^{2}}{V\left(r_{+}+\frac{1}{2} s^{2}\right)} \mathrm{d} s^{2}+s^{2} \frac{V\left(r_{+}+\frac{1}{2} s^{2}\right)}{s^{2}} \mathrm{~d} \theta^{2}+\left(r_{+}+\frac{1}{2} s^{2}\right)^{2}\left(\mathrm{~d} x_{3}^{2}+\ldots+\mathrm{d} x_{n}^{2}\right) .$$

Since $\frac{V\left(r_{+}+\frac{1}{2} s^{2}\right)}{s^{2}} \rightarrow \frac{1}{2}(n-1) r_{+}$as $s \rightarrow 0$, we conclude that $g_{B H}$ is in fact smooth at the origin. The sectional curvatures of $g_{B H}$ are
$$\begin{aligned}
& K_{12}=-1+\frac{(n-3)(n-2)}{r^{n-1}}, \quad K_{1 i}=K_{2 i}=-1-\frac{n-3}{r^{n-1}}, \quad i \geq 3, \\
& K_{i j}=-1+\frac{2}{r^{n-1}}, \quad i, j \geq 3
\end{aligned}$$
Furthermore, $g_{B H}$ is Einstein with $\operatorname{Ric}_{g_{B H}}=-(n-1) g_{B H}$. For $n=3$ this metric is just the standard hyperbolic metric in cylindrical coordinates.

Observe that away from the origin the metric $g_{B H}$ is asymptotic to the standard hyperbolic metric $g_{\text {hyp }}$ from subsection 2.3. To be precise: The black-hole manifold minus a large cylinder around the core $\mathbb{R}^{n-2}$ is geometrically close to some subset of $\mathbb{H}^{n} /\langle\gamma\rangle$ where $\gamma$ is a parabolic transformation. Taking the hyperbolic metric $g_{\text {hyp }}$ as a background metric and identifying $\theta$ with $x_{2}$, we find
$$\begin{aligned}
g_{B H}-g_{h y p}=\left(V^{-1}(r)-r^{-2}\right) \mathrm{d} r^{2}+ & \left(V(r)-r^{2}\right) \mathrm{d} x_{2}^{2} \\
& =2 r^{-n+1} \frac{r^{2}}{V(r)} \cdot r^{-2} \mathrm{~d} r^{2}-2 r^{-n+1} \cdot r^{2} \mathrm{~d} x_{2}^{2} .
\end{aligned}$$
From this, we can conclude $\left|\nabla^{m}\left(g_{B H}-g_{h y p}\right)\right|=O\left(r^{-n+1}\right)$ for all $m \geq 0$.
We analyze the behaviour of this metric under the addition of small trivial Einstein deformations. Let $u_{i j}(i, j=2, \ldots, n)$ be a traceless symmetric $(n-1) \times$ $(n-1)$ matrix and set
$$g_{B H}+u=g_{B H}+r^{2} u_{i j} \mathrm{~d} x_{i} \mathrm{~d} x_{j}$$
where we set $x_{2}=\theta$. Note that $g_{B H}+u$ is only smooth away from the origin. By the closeness of $g_{B H}$ to $g_{\text {hyp }}$ we find for sufficiently small $u$ and say $r>r_{+}+1$
$$\Phi_{g_{B H}}\left(g_{B H}+u\right)=|u| O\left(r^{-n+1}\right) \quad \text { and } \quad L_{g_{B H}} u=|u| O\left(r^{-n+1}\right) .$$
Since we will need it later, we mention the following bound: Let $u$ be small and $u^{\prime}$ be another traceless symmetric $(n-1) \times(n-1)$ matrix. Then
$$\left|\left(\mathrm{d} \Phi_{g_{B H}}\right)_{g_{B H}+u}\left(u^{\prime}\right)-\left(\mathrm{d} \Phi_{g_{B H}}\right)_{g_{B H}}\left(u^{\prime}\right)\right|=|u|\left|u^{\prime}\right| O\left(r^{-n+1}\right) .$$
The same decay holds for all higher covariant derivatives of the left hand side.
It will be useful later to discuss the geometric quotients of the black-hole metric. In dimension $n=3$ the isometries of $\left(M_{B H}, g_{B H}\right)$ are the isometries of hyperbolic space. For $n>3$, all isometries leave the topological splitting $M_{B H}=\mathbb{R}^{2} \times \mathbb{R}^{n-2}$ and the coordinate $r$ invariant, so they act as a rotation or reflection in the origin on the $\mathbb{R}^{2}$ factor and as a Euclidean translation on the $\mathbb{R}^{n-2}$-factor.

Let $T^{n-1}$ be an arbitrary flat torus and $\sigma \subset T^{n-1}$ a simple closed geodesic. Given this data, we will now construct a Riemannian manifold with boundary $\widehat{N}=\widehat{N}_{T^{n-1}, \sigma}$ such that
\begin{itemize}
\item[(i)] $\widehat{N}$ is diffeomorphic to a solid torus $D^{2} \times T^{n-2}$.
\item[(ii)] The boundary $\partial \widehat{N}$ is isometric to the given $T^{n-1}$.
\end{itemize}
\begin{itemize}
\item[(iii)] Denote by $M_{B H}(r \leq R)$ the part of $M_{B H}$ on which $r \leq R$. Then there is a group of isometries $\Gamma$ of $M_{B H}$ and a number $R>0$ such that $\widehat{N}=M_{B H}(r \leq$ $R) / \Gamma$.
\item[(iv)] All isometries of $\Gamma$ keep the splitting $M_{B H}=\mathbb{R}^{2} \times \mathbb{R}^{n-2}$ and the coordinate $r$ invariant, hence $T^{n-1} \cong \partial \widehat{N}=M_{B H}(r=R) / \Gamma$.
\item[(v)] There is an isometric identification of $M_{B H}(r=R) / \Gamma$ with $T^{n-1}$ that sends the meridional loop $M_{B H}\left(r=R, x_{3}=\ldots=x_{n}=0\right) / \Gamma$ to $\sigma$.
\end{itemize}
We will later use $\widehat{N}$ to fill in the truncated cusps.
The manifold $\widehat{N}$ is constructed as follows: Since $V:\left[r_{+}, \infty\right) \rightarrow[0, \infty)$ is invertible, we can find an $R>0$ such that $V(R)=(\ell(\sigma) / \beta)^{2}$. Then $M_{B H}(r=$ $R) \cong S^{1}(\ell(\sigma)) \times \mathbb{R}^{n-2}$. Consider the cyclic subgroup $\langle[\sigma]\rangle<\pi_{1}\left(T^{n-1}\right)$ and denote by $\widetilde{T} \rightarrow T^{n-1}$ the corresponding cover. Obviously, $\sigma \subset T^{n-1}$ can be lifted to a closed geodesic loop $\widetilde{\sigma} \subset \widetilde{T}$. From this we conclude that there is an isometric identification of $M_{B H}(r=R)$ with $\widetilde{T}$ such that the loop $M_{B H}\left(r=R, x_{3}=\ldots=\right.$ $x_{n}$ ) is sent to $\widetilde{\sigma}$. Consider now the group of deck transformations $\Gamma$ of $\widetilde{T} \rightarrow T^{n-1}$. Its action on $M_{B H}(r=R) \cong \widetilde{T}$ can be uniquely continued to an isometric action on $M_{B H}$ and by the lifting property of $\sigma$ we know that this continuation is even fixed point free. Hence $M_{B H} / \Gamma$ is smooth, and the manifold $\widehat{N}:=M_{B H}(r \leq R) / \Gamma$ satisfies the conditions (i)-(v) above.

We remark that the image of the core $\mathbb{R}^{n-2}$ under the quotient map $M_{B H} \rightarrow$ $M_{B H} / \Gamma$ is a torus $\widehat{T}^{n-2}=r^{-1}\left(r_{+}\right)$which we call the core torus. Furthermore, all level sets $r^{-1}\left(r^{\prime}\right)$ for $r^{\prime}>r_{+}$are diffeomorphic to $T^{n-1}$ and we can check that $\left(r^{\prime}\right)^{-1} \operatorname{diam} r^{-1}\left(r^{\prime}\right)$ is an increasing function in $r^{\prime}$ (here diam denotes the intrinsic diameter).

\section*{3. The construction process}

We will briefly explain how the approximate Einstein metric on the manifold $M_{\bar{\sigma}}$ is constructed. Recall that we are given simple closed geodesics $\sigma_{k}$ inside the tori $T_{k} \subset M_{\text {hyp }}$ which bound the cusps $N_{k}$, and that $\operatorname{inj}=\mu_{n}$. In dimension 3 it is also important to choose the $N_{k}^{\prime}$ such that on their boundary tori $T_{k}^{\prime}$ we also have $\operatorname{inj}=\mu_{n}$.

As mentioned in subsection 2.4, we can find parameters $R_{k}$ as well as lattices $\Gamma_{k}<$ Isom $M_{B H}$ such that the $\widehat{N}_{k}:=\widehat{N}_{T_{k}, \sigma_{k}}=M_{B H}\left(r \leq R_{k}\right) / \Gamma_{k}$ are topological solid tori with boundary isometric to $T_{k}$ and such that the $\sigma_{k}$ correspond to meridians. Set $R_{\text {min }}:=\min R_{k}$ and observe that $R_{\text {min }} \rightarrow \infty$ as $\ell_{\text {min }} \rightarrow \infty$.

If we glue together the components $M_{h y p} \backslash \bigcup_{k=1}^{p} N_{k}$ and $\widehat{N}_{k}$, we obtain the manifold $M_{\bar{\sigma}}$. We can endow $M_{\bar{\sigma}}$ with an almost Einstein metric $g_{\bar{\sigma}}$ in the following sense (to simplify notation, we will denote this metric by $g_{\bar{\sigma}}$ rather than the final Einstein metric): $g_{\bar{\sigma}}$ equals $g_{h y p}$ on the first component and $g_{B H}$ on the $\widehat{N}_{k}$ except on the tubular neighborhoods $\bigcup_{k=1}^{p} B_{1} T_{k} \cap \widehat{N}_{k}$ of radius 1 around the $T_{k}$ where an interpolation between $g_{\text {hyp }}$ and $g_{B H}$ is taking place. Thus $g_{\bar{\sigma}}$ satisfies the Einstein equation on the complement of $\bigcup_{k=1}^{p} B_{1} T_{k} \cap \widehat{N}_{k}$ whereas on $\bigcup_{k=1}^{p} B_{1} T_{k} \cap \widehat{N}_{k}$ the
quantity $\operatorname{Ric}_{g_{\bar{\sigma}}}+(n-1) g_{\bar{\sigma}}$ and hence $\Phi_{g_{\bar{\sigma}}}\left(g_{\bar{\sigma}}\right)$ is very small. To be precise: for any $m$ there is a $C_{m}$ such that using the $C^{m, \alpha}$ norms defined in section 4 below, we have
$$\left\|\operatorname{Ric}_{g_{\bar{\sigma}}}+(n-1) g_{\bar{\sigma}}\right\|_{m, \alpha}<C_{m} R_{\min }^{-n+1} \quad \text { and } \quad\left\|\Phi_{g_{\bar{\sigma}}}\left(g_{\bar{\sigma}}\right)\right\|_{m, \alpha}<C_{m} R_{\min }^{-n+1} .$$

Note that in dimension $n=3$, the parts $N_{k}^{\prime}$ are already isometric to $\widehat{N}_{k}^{\prime}=\widehat{N}_{T_{k}^{\prime}, \sigma_{k}^{\prime}}$ for certain loops $\sigma_{k}^{\prime} \subset T_{k}^{\prime}$.

For further details of this construction we refer to [And2].

\section*{4. Uniform norms on $M_{\bar{\sigma}}$}

In the following let $L:=L_{g_{\bar{\sigma}}}$ and fix some $m \geq 2$ and $0<\alpha<1$. We will further fix an upper volume bound on $M_{\text {hyp }}$ and call all constants uniform which only depend on this bound, but not on $M_{\text {hyp }}$ or $\bar{\sigma}$. Observe that the Riemannian manifolds $\left(M_{\bar{\sigma}}, g_{\bar{\sigma}}\right)$, as constructed in the last section, satisfy the following uniform geometric bounds: The conjugate radius is uniformly bounded from below by some positive constant $2 \zeta$ and there are uniform bounds $C_{m}$ such that $\left\|\nabla^{m} R\right\|<C_{m}$.

Let $h$ be a symmetric bilinear form on $M_{\bar{\sigma}}$ and $x \in M_{\bar{\sigma}}$. Pull back the bundle $\operatorname{Sym}_{2} T^{*}$ and its section $h$ to the universal cover $\widetilde{B}_{\zeta}(x)$ of $B_{\zeta}(x)$. Choose exponential coordinates on $\widetilde{B}_{\zeta}(x)$ and trivialize $\operatorname{Sym}_{2} T^{*}$ by parallel transport. We can now view $h$ as a vector-valued function on a ball $B_{\zeta}(0) \subset \mathbb{R}^{n}$. Fix the constant $\zeta$ once and for all and define the local Hölder (semi)-norm of $h$ at $x$ by this representation:
$$\|h\|_{m, \alpha ; x}:=\left\|\left.h\right|_{B_{\zeta}(x)}\right\|_{m, \alpha} .$$
We note that we have Schauder estimates for these semi-norms:
$$\|h\|_{m, \alpha ; x} \leq C \sup _{x^{\prime} \in B_{\zeta}(x)}\left(\|L h\|_{m-2, \alpha ; x^{\prime}}+\|h\|_{0 ; x^{\prime}}\right)$$
such that $C$ is a uniform constant.
Using these semi-norms it is now easy to define the global Hölder norm by
$$\|h\|_{m, \alpha}:=\sup _{x \in M_{\bar{\sigma}}}\|h\|_{m, \alpha ; x} .$$

We will need another norm that guarantees a certain decay away from the thick part and the core tori. We therefore introduce a weight function $W$ (or rather the inverse of a weight function) on $M_{\bar{\sigma}}$ such that for $n>3$
$$W= \begin{cases}\left(\frac{r}{R_{k}}\right)^{0.1}+r^{-0.1} & \text { on } \widehat{N}_{k} \\ 1 & \text { on } M_{\bar{\sigma}} \backslash \bigcup_{k=1}^{p} \widehat{N}_{k}\end{cases}$$
In dimension 3 we also choose the weight $\left(\frac{r}{R_{k}^{\prime}}\right)^{0.1}+r^{-0.1}$ on the $N_{k}^{\prime} . W$ is not continuous at the $T_{k}$. However, this discontinuity will not be essential since the jump is between 1 and $1+R_{k}^{-0.1}$ and $R_{k}>r_{+}$. On each $\widehat{N}_{k}$ the weight function $W$ attains its minimum at $r=R_{k}^{1 / 2}$. For later use, choose points $c_{k} \in \widehat{N}_{k}\left(r=R_{k}^{1 / 2}\right)$
(and $c_{k}^{\prime} \in N_{k}^{\prime}\left(r=\left(R_{k}^{\prime}\right)^{1 / 2}\right.$ ) in dimension 3). They lie approximately in the centers of the $\widehat{N}_{k}$. Set
$$\|h\|_{m, \alpha ; *}:=\sup _{x \in M_{\bar{\sigma}}} W^{-1}(x)\|h\|_{m, \alpha ; x} .$$
It is immediate that we can derive uniform Schauder estimates for the norms $\|\cdot\|_{m, \alpha}$ and $\|\cdot\|_{m, \alpha ; *}$ from (4.1):
$$\begin{aligned}
\|h\|_{m, \alpha} & \leq C\left(\|L h\|_{m-2, \alpha}+\|h\|_{0}\right) \\
\|h\|_{m, \alpha ; *} & \leq C\left(\|L h\|_{m-2, \alpha ; *}+\|h\|_{0 ; *}\right)
\end{aligned}$$

Finally, we have to define a more complicated norm that guarantees decay towards some trivial Einstein variation: Let $\rho_{1}, \ldots, \rho_{p}$ be cutoff functions on $M_{\bar{\sigma}}$ such that $\rho_{k} \equiv 1$ on $\widehat{N}_{k} \backslash\left(B_{1} T_{k} \cup B_{2} \widehat{T}_{k}^{n-2}\right)$ and $\rho_{k} \equiv 0$ on $M_{\bar{\sigma}} \backslash \widehat{N}_{k}$ and $B_{1} \widehat{T}_{k}^{n-2}$ where $\widehat{T}_{k}^{n-2}$ is the core torus of $\widehat{N}_{k}$. We may assume that the $\rho_{k}$ are constructed in such a way that they satisfy some universal $C^{m}$ bound for each $m$. Let $u_{1}, \ldots, u_{p}$ be trivial Einstein variations of the hyperbolic cusp metric which we assume to be defined on the corresponding $\widehat{N}_{k}$. Represent $h$ by
$$h=\bar{h}+\sum_{k=1}^{p} \rho_{k} u_{k} .$$
and define
$$\|h\|_{m, \alpha ; * *}:=\inf _{\substack{\bar{h}, u_{1}, \ldots, u_{p} \\ \text { satisfy }(*)}}\left(\|\bar{h}\|_{m, \alpha ; *}+\sum_{k=1}^{p}\left|u_{k}\right|\right)$$
where we use an arbitrary uniform norm on the (finite dimensional) space of trivial Einstein deformations. In dimension 3 we have to alter the definition in order to also consider trivial Einstein variations $u_{k}^{\prime}$ on the $N_{k}^{\prime}$. Observe that since $W^{-1}>c>0$ we have for some uniform $C$
$$C^{-1}\|h\|_{m, \alpha} \leq\|h\|_{m, \alpha ; * *} \leq\|h\|_{m, \alpha ; *} .$$

Lemma 4.1. We have the following uniform Schauder estimate for $\|\cdot\|_{m, \alpha ; * *}$ :
$$\|h\|_{m, \alpha ; * *} \leq C\left(\|L h\|_{m-2, \alpha ; *}+\|h\|_{0 ; * *}\right) .$$
Note that the second norm is a $*$-norm.
Proof. We carry out the proof for $n>3$ (for $n=3$ we have to consider the $N_{k}^{\prime}$ as well). Choose a decomposition $h=\bar{h}+\sum_{k=1}^{p} \rho_{k} u_{k}$. From (2.8) we find that $\left\|L \rho_{k} u_{k}\right\|_{m-2, \alpha ; *} \leq C\left|u_{k}\right|$. Hence
$$\|L \bar{h}\|_{m-2, \alpha ; *} \leq\|L h\|_{m-2, \alpha ; *}+C \sum_{k=1}^{p}\left|u_{k}\right| .$$
So by the Schauder estimate for $\|\cdot\|_{m, \alpha ; *}$ we find
$$\|\bar{h}\|_{m, \alpha ; *} \leq C\left(\|L h\|_{m-2, \alpha ; *}+\sum_{k=1}^{p}\left|u_{k}\right|+\|\bar{h}\|_{0 ; *}\right)$$
hence the conclusion. \(\square\)

The following Lemma gives us a tool to estimate the $\|\cdot\|_{m, \alpha ; * *}$ norm:
Lemma 4.2. Let $h$ be a symmetric bilinear form on $M_{\bar{\sigma}}$. Choose $u_{k}$ such that $\left|\left(h-u_{k}\right)\left(c_{k}\right)\right|$ is minimal for each $k$ and set $\bar{h}=h-\sum_{k=1}^{p} \rho_{k} u_{k}$. In dimension 3 also consider $u_{k}^{\prime}$ such that $\left|\left(h-u_{k}^{\prime}\right)\left(c_{k}^{\prime}\right)\right|$ is minimal. Then there is a uniform constant $C$ such that
$$\|h\|_{m, \alpha ; * *} \leq\left(\|\bar{h}\|_{m, \alpha ; *}+\sum_{k=1}^{p}\left|u_{k}\right|\right) \leq C\|h\|_{m, \alpha ; * *}$$
Proof. Assume again $n>3$. Only the second inequality has to be shown. First observe that since $\left|\left(h-u_{k}\right)\left(c_{k}\right)\right|$ is minimal, we have $\left(h-u_{k}\right)\left(c_{k}\right) \perp u_{k}\left(c_{k}\right)$ and hence
$$\left|\left(u_{k}\right)\left(c_{k}\right)\right| \leq\left|h\left(c_{k}\right)\right| \leq C\|h\|_{m, \alpha} \leq C\|h\|_{m, \alpha ; * *} .$$
It remains to bound $\|\bar{h}\|_{m, \alpha ; *}$. Let $h=\bar{h}^{\prime}+\sum_{k=1}^{p} \rho_{k} u_{k}^{\prime}$ be an arbitrary decomposition of $h$ analogous to (*). We will show that
$$\|\bar{h}\|_{m, \alpha ; *} \leq C\left(\left\|\bar{h}^{\prime}\right\|_{m, \alpha ; *}+\sum_{k=1}^{p}\left|u_{k}^{\prime}\right|\right) .$$
Note that by the minimal choice of $u_{k}$, we have $\left|\left(u_{k}-u_{k}^{\prime}\right)\left(c_{k}\right)\right| \leq\left|\left(h-u_{k}^{\prime}\right)\left(c_{k}\right)\right|$. We now use
$$\|\bar{h}\|_{m, \alpha ; *} \leq\left\|\bar{h}^{\prime}\right\|_{m, \alpha ; *}+\sum_{k=1}^{p}\left\|\rho_{k}\left(u_{k}-u_{k}^{\prime}\right)\right\|_{m, \alpha ; *}$$
and bound the last term by $C \sum_{k=1}^{p} M_{k}\left|\left(u_{k}-u_{k}^{\prime}\right)\left(c_{k}\right)\right| \leq C \sum_{k=1}^{p} M_{k}\left|\left(h-u_{k}^{\prime}\right)\left(c_{k}\right)\right|$ where
$$M_{k}=\max _{\widetilde{N}_{k}} W^{-1}=W^{-1}\left(c_{k}\right) .$$
So if $\rho_{k}\left(c_{k}\right)=1$, then $M_{k}\left|\left(h-u_{k}^{\prime}\right)\left(c_{k}\right)\right| \leq C\left\|h-\sum_{l=1}^{p} \rho_{l} u_{l}^{\prime}\right\|_{m, \alpha ; *}=\left\|\bar{h}^{\prime}\right\|_{m, \alpha ; *}$. If not, we have a uniform bound on $R_{k}$, hence on $M_{k}$ and $M_{k}\left|\left(h-u_{k}^{\prime}\right)\left(c_{k}\right)\right| \leq$ $C\left\|\bar{h}^{\prime}\right\|_{m, \alpha}$. \(\square\)

\section*{5. Application of the inverse function theorem}

We will use the following estimate on $L^{-1}$ which we will prove in the next section:

Proposition 5.1. There are $R_{0}=R_{0}(n, V), \Lambda=\Lambda(n, V)<\infty$ such that whenever $\operatorname{vol} M_{h y p}<V$ and $R_{\min }>R_{0}$, then the operator $L=L_{g_{\bar{\sigma}}}: C^{m, \alpha}\left(M_{\bar{\sigma}} ; \operatorname{Sym}_{2} T^{*}\right) \rightarrow$ $C^{m-2, \alpha}\left(M_{\bar{\sigma}} ; \operatorname{Sym}_{2} T^{*}\right)$ is invertible and
$$\|h\|_{m, \alpha ; * *} \leq \Lambda\left\|L_{g_{\bar{\sigma}}} h\right\|_{m-2, \alpha ; *}$$
for any symmetric bilinear form $h$ on $M_{\bar{\sigma}}$.
Observe that there are different types of norms on both sides of this inequality. Thus in order to construct a perturbation of $g_{\bar{\sigma}}$ which is Einstein we cannot simply use this estimate to strictly apply the inverse function theorem on Banach spaces. However, we will show that the trivial Einstein deformations which make
the difference between these two norms, have a weak influence on the nonlinear term of the equation we want to solve.

We will now prove Theorem 1.1 assuming Proposition 5.1.
Proof of Theorem 1.1. We only consider the case $n>3$. It will be clear how to adapt the proof to the 3 dimensional case by considering the $N_{k}^{\prime}$ as well.

In the following we set $M=M_{\bar{\sigma}}, g=g_{\bar{\sigma}}, \Phi=\Phi_{g}$ and $L=L_{g}$.
Assume that $R_{\text {min }}>R_{0}$. We want to find $h \in C^{m, \alpha}\left(M ; \operatorname{Sym}_{2} T^{*}\right)$ such that the equation $\Phi(g+h)=0$ holds. It will then follow from elliptic regularity that $h$ is actually smooth. The equation is equivalent to the fixed point equation
$$h=\Psi(h)=h-L^{-1} \Phi(g+h) .$$
In order to solve this equation for large $R_{\text {min }}$, it suffices to show that there is an $\varepsilon=\varepsilon(n, V)>0$ such that $\Psi$ is $\frac{1}{2}$-Lipschitz with respect to the $\|\cdot\|_{m, \alpha ; * *}$-norm on $B_{\varepsilon}=\left\{h \in C^{m, \alpha}\left(M ; \operatorname{Sym}_{2} T^{*}\right) \quad: \quad\|h\|_{m, \alpha ; * *}<\varepsilon\right\}$. Then, assuming $R_{\text {min }}$ to be large enough, we can achieve $\|\Psi(0)\|_{m, \alpha ; * *}=\left\|L^{-1} \Phi(g)\right\|_{m, \alpha ; * *} \leq \Lambda\|\Phi(g)\|_{m-2, \alpha ; *}<$ $\frac{1}{2} \varepsilon$ and apply Banach's fixed point theorem.

For $h_{0}, h_{1} \in B_{\varepsilon}$ and $h_{t}=(1-t) h_{0}+t h_{1}$ we compute
$$\begin{aligned}
\left\|\Psi\left(h_{0}\right)-\Psi\left(h_{1}\right)\right\|_{m, \alpha ; * *} \leq & \left\|\int_{0}^{1} L^{-1}\left(L-\mathrm{d} \Phi_{g+h_{t}}\right)\left(h_{0}-h_{1}\right) \mathrm{d} t\right\|_{m, \alpha ; * *} \\
& \leq \Lambda \int_{0}^{1}\left\|\left(\mathrm{~d} \Phi_{g}-\mathrm{d} \Phi_{g+h_{t}}\right)\left(h_{0}-h_{1}\right)\right\|_{m-2, \alpha ; *} \mathrm{~d} t
\end{aligned}$$
(Observe that the subscript of $\mathrm{d} \Phi$ now indicates the point at which the derivative is taken rather than the background metric which we used to define $\Phi$.) Thus, it suffices to show that for any $h \in B_{\varepsilon}$ and $h^{\prime} \in C^{m, \alpha}\left(M ; \operatorname{Sym}_{2} T^{*}\right)$ we have
$$\left\|\mathrm{d} \Phi_{g}\left(h^{\prime}\right)-\mathrm{d} \Phi_{g+h}\left(h^{\prime}\right)\right\|_{m-2, \alpha ; *} \leq \delta(\varepsilon)\left\|h^{\prime}\right\|_{m, \alpha ; * *}$$
for some universal $\delta(\epsilon)$ with $\delta(\varepsilon) \rightarrow 0$ as $\varepsilon \rightarrow 0$.
Represent $h=\bar{h}+\sum_{k=1}^{p} \rho_{k} u_{k}$ and $h^{\prime}=\bar{h}^{\prime}+\sum_{k=1}^{p} \rho_{k} u_{k}^{\prime}$ where the $u_{k}, u_{k}^{\prime}$ are trivial Einstein variations. Then
$$\begin{aligned}
& \left\|\mathrm{d} \Phi_{g}\left(h^{\prime}\right)-\mathrm{d} \Phi_{g+h}\left(h^{\prime}\right)\right\|_{m-2, \alpha ; *} \\
& \quad \leq\left\|\mathrm{d} \Phi_{g}\left(\bar{h}^{\prime}\right)-\mathrm{d} \Phi_{g+h}\left(\bar{h}^{\prime}\right)\right\|_{m-2, \alpha ; *}+\sum_{k=1}^{p}\left\|\mathrm{~d} \Phi_{g}\left(\rho_{k} u_{k}^{\prime}\right)-\mathrm{d} \Phi_{g+h}\left(\rho_{k} u_{k}^{\prime}\right)\right\|_{m-2, \alpha ; *} .
\end{aligned}$$
The first term can immediately be bounded by $C\|h\|_{m, \alpha}\left\|\bar{h}^{\prime}\right\|_{m, \alpha ; *} \leq C^{\prime}\|h\|_{m, \alpha ; * *}\left\|\bar{h}^{\prime}\right\|_{m, \alpha ; *}$. As for the second term we have
$$\begin{aligned}
& \left\|\mathrm{d} \Phi_{g}\left(\rho_{k} u_{k}^{\prime}\right)-\mathrm{d} \Phi_{g+h}\left(\rho_{k} u_{k}^{\prime}\right)\right\|_{m-2, \alpha ; *} \\
& \leq\left\|\mathrm{d} \Phi_{g}\left(\rho_{k} u_{k}^{\prime}\right)-\mathrm{d} \Phi_{g+\rho_{k} u_{k}}\left(\rho_{k} u_{k}^{\prime}\right)\right\|_{m-2, \alpha ; *}+\left\|\mathrm{d} \Phi_{g+\rho_{k} u_{k}}\left(\rho_{k} u_{k}^{\prime}\right)-\mathrm{d} \Phi_{g+\bar{h}+\rho_{k} u_{k}}\left(\rho_{k} u_{k}^{\prime}\right)\right\|_{m-2, \alpha ; *} .
\end{aligned}$$

Now, since $u_{k}$ is a trivial Einstein variation, we can use (2.9) to bound the first term by $C\left|u_{k}\right|\left|u_{k}^{\prime}\right|$. The second term is bounded by $C\|\bar{h}\|_{m, \alpha ; *}\left|u_{k}^{\prime}\right|$. We conclude
$$\begin{gathered}
\left\|\mathrm{d} \Phi_{g}\left(h^{\prime}\right)-\mathrm{d} \Phi_{g+h}\left(h^{\prime}\right)\right\|_{m-2, \alpha ; *} \leq C\|h\|_{m, \alpha ; * *}\left\|\bar{h}^{\prime}\right\|_{m, \alpha ; *}+C \sum_{k=1}^{p}\left(\left|u_{k}\right|\left|u_{k}^{\prime}\right|+\|\bar{h}\|_{m, \alpha ; *}\left|u_{k}^{\prime}\right|\right) \\
\leq C\|h\|_{m, \alpha ; * *}\left\|\bar{h}^{\prime}\right\|_{m, \alpha ; *}+C\left(\|\bar{h}\|_{m, \alpha ; *}+\sum_{k}\left|u_{k}\right|\right) \sum_{l}\left|u_{l}^{\prime}\right| .
\end{gathered}$$
By an appropriate choice of $\bar{h}$ and $u_{k}$, the right hand side can be made arbitrarily close to $C\|h\|_{m, \alpha ; * *}\left(\left\|\bar{h}^{\prime}\right\|_{m, \alpha ; *}+\sum_{l}\left|u_{l}^{\prime}\right|\right)$ what in turn by a good choice of $\bar{h}^{\prime}$ and $u_{k}^{\prime}$ can be made arbitrarily close to $C\|h\|_{m, \alpha ; * *}\left\|h^{\prime}\right\|_{m, \alpha ; * *} \leq C \varepsilon\left\|h^{\prime}\right\|_{m, \alpha ; * *}$. This proves the desired bound and hence the theorem. \(\square\)

\section*{6. Estimates for $L^{-1}$}

This section will be occupied with the proof of Proposition 5.1. For the sake of a clear exposition of the main ideas we will defer most of the technical arguments to sections 7 and 8. We first establish a bound on the $\|\cdot\|_{m, \alpha}$-norm:

Lemma 6.1. There are $R_{0}=R_{0}(n, V), \Lambda=\Lambda(n, V)<\infty$ such that whenever $\operatorname{vol} M_{h y p}<V$ and $R_{\min }>R_{0}$, then the operator $L_{g_{\bar{\sigma}}}: C^{m, \alpha}\left(M_{\bar{\sigma}} ; \operatorname{Sym}_{2} T^{*}\right) \rightarrow$ $C^{m-2, \alpha}\left(M_{\bar{\sigma}} ; \operatorname{Sym}_{2} T^{*}\right)$ is invertible and
$$\|h\|_{m, \alpha} \leq \Lambda\left\|L_{g_{\bar{\sigma}}} h\right\|_{m-2, \alpha ; *}$$
for any symmetric bilinear form $h$ on $M_{\bar{\sigma}}$.
Proof. The proof of this Lemma is similar to that of [And2, Proposition 3.2]. Observe that in this Proposition the right hand side of the inequality reads $\Lambda \log R_{\text {max }}\left\|L_{g_{\bar{\sigma}}} h\right\|_{m-2, \alpha}$. In our case, we can don't need the $\log R_{\text {max }}$ factor, but have to make use of a stronger norm of $L_{g_{\bar{\sigma}}}$.

Recall that we have the Schauder estimate
$$\|h\|_{m, \alpha} \leq C\left(\left\|L_{g_{\bar{\sigma}}} h\right\|_{m-2, \alpha}+\|h\|_{0}\right)$$
where $C$ is uniform. So it is enough to show that:
There are $R_{0}=R_{0}(n, V), \Lambda^{\prime}=\Lambda^{\prime}(n, V)<\infty$ such that whenever vol $M_{\text {hyp }}<V$ and $R_{\text {min }}>R_{0}$, we have
$$\|h\|_{0} \leq \Lambda^{\prime}\left\|L_{g_{\bar{\sigma}}} h\right\|_{m-2, \alpha ; *}$$
for all symmetric bilinear forms $h$ on any $M_{\bar{\sigma}}$.
Assume that this statement was wrong. Then we can find a sequence of hyperbolic manifolds $M_{\text {hyp }}^{i}$ with basepoints $y^{i} \in M_{\text {thick }}^{i}$ and $\operatorname{vol} M_{\text {hyp }}^{i}$ uniformly bounded from above as well as a sequences of $\bar{\sigma}^{i}$ such that $R_{\text {min }}^{i} \rightarrow \infty$ and symmetric bilinear forms $h^{i}$ on $M^{i}=M_{\bar{\sigma}^{i}}$ such that for $g^{i}=g_{\bar{\sigma}^{i}}, L^{i}=L_{g^{i}}$ and $f^{i}:=L^{i} h^{i}$
$$\left\|h^{i}\right\|_{0}=1, \quad \text { but } \quad\left\|f^{i}\right\|_{m-2, \alpha ; *} \longrightarrow 0$$
as $i \rightarrow \infty$. So there are points $x^{i} \in M^{i}$ such that $\left|h^{i}\right|\left(x^{i}\right)>\gamma$ for some universal $\gamma>0$. The Schauder estimate gives us a uniform $C^{m, \alpha_{-}}$-bound for the $h^{i}$.

1° In the first step we show that there are sequences $d^{i} \rightarrow \infty$ and $w^{i} \rightarrow 0$ such that $\left|h^{i}\right|<w^{i}$ on $B_{d^{i}}\left(y^{i}\right)$.

Consider an arbitrary subsequence of counterexamples. After passing to a subsequence again, the pointed Riemannian manifolds $\left(M^{i}, y^{i}\right)$ Gromov-Hausdorff converge to a pointed hyperbolic manifold $\left(M_{\text {hyp }}^{\infty}, y^{\infty}\right)$ of finite volume. Furthermore, the $h^{i}$ subconverge to a symmetric bilinear form $h^{\infty}$ on $M_{h y p}^{\infty}$ such that $L^{\infty}\left(h^{\infty}\right)=0$ (here $L^{\infty}=L_{g_{h y p}^{\infty}}$ ).

Denote by $\left(M_{\text {hyp }}^{\infty}\right)^{s}$ the manifold obtained from $M_{\text {hyp }}^{\infty}$ by truncating its cusps at distance $s$ from the basepoint $y^{\infty}$. Using Stoke's theorem and (2.4), we find
$$\int_{\left(M_{h y p}^{\infty}\right)^{s}}\left|d h^{\infty}\right|^{2}+\left|\operatorname{div} h^{\infty}\right|^{2}+(n-2)\left|h^{\infty}\right|^{2}+\left(\operatorname{tr} h^{\infty}\right)^{2}=\int_{\partial\left(M_{h y p}^{\infty}\right)^{s}} Q\left(h^{\infty}, \nabla h^{\infty}\right)$$
where the right hand side goes to 0 as $s \rightarrow \infty$. So $h^{\infty} \equiv 0$ and we conclude that for any $d$ we have $\left|h^{i}\right| \rightarrow 0$ uniformly on $B_{d}\left(y^{i}\right)$ for a subsequence. Since we started with an arbitrary subsequence, this implies that for any $d$ we have $\left|h^{i}\right| \rightarrow 0$ on $B_{d}\left(y^{i}\right)$ uniformly for the whole sequence and hence the claim.

2° Next, we give an estimate for $h^{i}$ on the $\widehat{N}_{k}^{i}$ (and $N^{\prime i}{ }_{k}$ in dimension 3).
Choose coordinates $\left(r, \theta, x_{3}, \ldots, x_{n}\right)$ on these components (to be precise on their universal covers). Observe that $\widehat{N}_{k}^{i} \backslash B_{1}\left(T_{k}^{i}\right)$ carries the exact black-hole metric. We have $\left|f^{i}\right|<\left\|f^{i}\right\|_{m-2, \alpha ; *} W$. Since $\operatorname{dist}\left(y^{i}, T_{k}^{i}\right)<\operatorname{diam} M_{\text {thick }}^{i}$ is uniformly bounded, we find that $\left|h^{i}\right|<w^{i} \rightarrow 0$ around the boundaries of the $\widehat{N}_{k}^{i}$.

Consider the restriction of $h^{i}$ and $f^{i}$ to some $\widehat{N}_{k}^{i}$ and take their average under the $S^{1} \times \mathbb{R}^{n-2}$-action, i.e. let $T^{n-1}\left(r^{\prime}\right):=\widehat{N}_{k}^{i}\left(r=r^{\prime}\right)$ be the cross-sectional torus at the coordinate $r=r^{\prime}$ and set
$$\widehat{h}_{s t}^{i}(r):=\frac{1}{\operatorname{vol} T^{n-1}(r)} \int_{T^{n-1}(r)} h_{s t}^{i} .$$
Analogously define $\widehat{f^{i}}$. Obviously, $\widehat{h}^{i}$ and $\widehat{f}^{i}$ are $S^{1} \times \mathbb{R}^{n-2}$ invariant and $L^{i} \widehat{h}^{i}=\widehat{f^{i}}$. Furthermore, still
$$\left|\widehat{f^{2}}\right|<\left\|f^{i}\right\|_{m-2, \alpha ; *} W=\left\|f^{i}\right\|_{m-2, \alpha ; *}\left[\left(\frac{r}{R_{k}^{i}}\right)^{0.1}+r^{-0.1}\right]$$
and since $\nabla h^{i}$ is uniformly bounded and $\operatorname{diam} T^{n-1}(r)<C \frac{r}{R_{k}^{i}}$, we conclude
$$\left|\widehat{h}^{i}-h^{i}\right|<C \frac{r}{R_{k}^{i}} \quad \text { on } \quad T^{n-1}(r) .$$
We can now apply Proposition 8.1 to conclude
$$\left|h^{i}\right|<C\left(w^{i}+\left\|f^{i}\right\|_{m-2, \alpha ; *}+r^{-n+1.1}+\frac{r}{R_{k}^{i}}\right) .$$

3° We can make the following conclusions on $x^{i}$ : From 1° we already know that $\operatorname{dist}\left(y^{i}, x^{i}\right) \rightarrow \infty$. This implies that $x^{i}$ eventually lies in some $\widehat{N}_{k}^{i}$ (or $N^{\prime i}{ }_{k}$ in dimension 3) and $\frac{r\left(x^{i}\right)}{R_{k}^{i}} \rightarrow 0$. So by (6.1) we conclude that $r\left(x^{i}\right)$ has to stay bounded. This means that the $x^{i}$ have to stay in bounded distance to some core tori $\left(\widehat{T}_{k}^{n-2}\right)^{i}$ of $\widehat{N}_{k}^{i}$ (or of $N^{\prime i}{ }_{k}$ ).

So there is a sequence $d^{\prime i}$ such that the universal covers $\left(\widetilde{B}_{d^{i}}\left(x^{i}\right), x^{i}\right)$ Gromov-Hausdorff subconverge to the black-hole metric $\left(M_{B H}, x^{\infty}\right)$ and the $h^{i}$ subconverge to some $h^{\infty}$ on $M_{B H}$ which satisfies $L^{\infty} h^{\infty}=0$ and $h^{\infty}\left(x^{\infty}\right) \neq 0$. Moreover, since the the pointed manifolds $\left(\widehat{N}_{k}^{i}, x^{i}\right)$ collapse to a ray, $h^{\infty}$ is invariant under the $S^{1} \times \mathbb{R}^{n-2}$-action. From (6.1) we also conclude that $\left|h^{\infty}\right|<C r^{-n+1.1}$.

We can now use Proposition 8.3 to find that $h^{\infty} \equiv 0$, a contradiction. \(\square\)

Finally, we can use Lemma 6.1 to refine our result and prove Proposition 5.1:
Proof of Proposition 5.1. Analogously to the proof of Lemma 6.1, we assume that the hypothesis was wrong and that we have sequences $M^{i}, \bar{\sigma}^{i}, h^{i}$ such that $R_{\text {min }}^{i} \rightarrow$ $\infty$ and
$$\left\|h^{i}\right\|_{0 ; * *}=1, \quad \text { but } \quad\left\|f^{i}\right\|_{m-2, \alpha ; *} \longrightarrow 0$$
for $f^{i}=L^{i} h^{i}$ (we also used (4.2) here).
By Lemma 6.1 we have $\left\|h^{i}\right\|_{0} \rightarrow 0$. We now change the $h^{i}$ by certain trivial Einstein variations of the $\widehat{N}_{k}^{i}$ (or $N_{k}^{\prime i}$ in dimension 3): Let $u_{k}^{i}$ be those trivial Einstein deformations as obtained in Lemma 4.2 and set $\bar{h}^{i}=h^{i}-\sum_{k=1}^{p^{i}} \rho_{k}^{i} u_{k}^{i}$. Then, since $\left\|h^{i}\right\|_{0} \rightarrow 0$ we have $\left|u_{k}^{i}\right| \rightarrow 0$ as $i \rightarrow \infty$ and by Lemma 4.2
$$\left\|\bar{h}^{i}\right\|_{* * ; 0} \leq\left\|\bar{h}^{i}\right\|_{0 ; *} \leq C\left\|\bar{h}^{i}\right\|_{0 ; * *}$$
for some uniform constant $C$. So we conclude that $\frac{1}{2}<\left\|\bar{h}^{i}\right\|_{0 ; * *}<\frac{3}{2}$ for large $i$ and hence we have the uniform estimate $c<\left\|\bar{h}^{i}\right\|_{0 ; *}<C$. However, we still have $\left\|\bar{h}^{i}\right\|_{0} \rightarrow 0$. Finally, setting $\bar{f}^{i}=L^{i} \bar{h}^{i}$, we get $\left\|\bar{f}^{i}\right\|_{m-2, \alpha ; *} \rightarrow 0$.

By the lower bound on $\left\|\bar{h}^{i}\right\|_{0 ; *}$, we can find points $x^{i} \in M^{i}$ such that
$$W^{-1}\left(x^{i}\right)\left|\bar{h}^{i}\right|\left(x^{i}\right)>\gamma>0 .$$
Since $\left\|\bar{h}^{i}\right\|_{0} \rightarrow 0$, we conclude $W\left(x^{i}\right) \rightarrow 0$. So the $x^{i}$ eventually lie in certain $\widehat{N}_{k^{i}}^{i}$ (or $N^{\prime i}{ }_{k^{i}}$ ), $R_{k^{i}}^{i} \rightarrow \infty$ and the distance of the $x^{i}$ to both $T_{k^{i}}^{i}$ as well as $\left(\widehat{T}_{k^{i}}^{n-2}\right)^{i}$ goes to infinity. So there is a sequence $d^{\prime i}$ such that the universal covers $\left(\widetilde{B}_{d^{i}}\left(x^{i}\right), x^{i}\right)$ converge to hyperbolic space $\left(\mathbb{H}^{n}, x^{\infty}\right)$ on which we can choose coordinates $\left(r^{\infty}, x_{2}, \ldots, x_{n}\right)$ with $r^{\infty}\left(x^{\infty}\right)=1$ and $\frac{r}{r^{i}} \rightarrow r^{\infty}$ where $r^{i}:=r\left(x^{i}\right)$ (observe that we choose those coordinates in which the hyperbolic metric takes the form (2.7)). In order to analyze the limiting behaviour of $\bar{h}^{i}$, we have to distinguish three cases:

1° For a subsequence we have $r^{i}\left(R_{k^{i}}^{i}\right)^{-1 / 2} \rightarrow \infty$.

Then we have the (local) convergence
$$\left(\frac{R_{k^{i}}^{i}}{r^{i}}\right)^{0.1} W=\left(\frac{r}{r^{i}}\right)^{0.1}+\left(\frac{R_{k^{i}}^{i}}{\left(r^{i}\right)^{2}} \cdot \frac{r^{i}}{r}\right)^{0.1} \longrightarrow\left(r^{\infty}\right)^{0.1} .$$
So $\left(\frac{R_{k i}^{i}}{r^{i}}\right)^{0.1} \bar{h}^{i}$ is locally bounded and $\left(\frac{R_{k i}^{i}}{r^{i}}\right)^{0.1} \bar{f}^{i} \rightarrow 0$ locally. Hence the $\bar{h}^{i}$ subconverge to some nonzero $\bar{h}^{\infty}$ on $\mathbb{H}^{n}$ which satisfies $\left|\bar{h}^{\infty}\right|<C\left(r^{\infty}\right)^{0.1}$ and $L^{\infty} \bar{h}^{\infty}=0$ (observe here that by Schauder estimates, we have uniform local bounds on some derivatives of the $\bar{h}^{i}$ ). Since the sequence $\left(B_{d^{\prime i}}\left(x^{i}\right), x^{i}\right)$ collapses to a line, $\bar{h}^{\infty}$ must be invariant under the group $\mathbb{R}^{n-1}$ acting on the last coordinates. We can now use Proposition 7.1 to obtain a contradiction.

2° For a subsequence we have $r^{i}\left(R_{k^{i}}^{i}\right)^{-1 / 2} \rightarrow 0$.
This time we have the convergence
$$\left(r^{i}\right)^{0.1} W=\left(\frac{\left(r^{i}\right)^{2}}{R_{k^{i}}^{i}} \cdot \frac{r}{r^{i}}\right)^{0.1}+\left(\frac{r}{r^{i}}\right)^{-0.1} \longrightarrow\left(r^{\infty}\right)^{-0.1} .$$
Now we can use the same arguments as in 1° to construct $\bar{h}^{\infty}$ on $\mathbb{H}^{n}$ which obeys the bound $\left|\bar{h}^{\infty}\right|<C\left(r^{\infty}\right)^{-0.1}$. This also contradicts Proposition 7.1.

3° For a subsequence we have $r^{i}\left(R_{k^{i}}^{i}\right)^{-1 / 2} \rightarrow q$ where $0<q<\infty$.
This means that the points $x^{i}$ stay within bounded distance to the $c_{k^{i}}^{i}$. Let $c^{\infty} \in \mathbb{H}^{n}$ be one of their limit points. We have the convergence
$$\left(r^{i}\right)^{0.1} W=\left(\frac{\left(r^{i}\right)^{2}}{R_{k^{i}}^{i}} \cdot \frac{r}{r^{i}}\right)^{0.1}+\left(\frac{r}{r^{i}}\right)^{-0.1} \longrightarrow q^{0.2}\left(r^{\infty}\right)^{0.1}+\left(r^{\infty}\right)^{-0.1} .$$
Hence the same reasoning as in 1° yields a nonzero $\bar{h}^{\infty}$ which satisfies $\left|\bar{h}^{\infty}\right|<$ $C\left(\left(r^{\infty}\right)^{0.1}+\left(r^{\infty}\right)^{-0.1}\right)$. So by Proposition 7.1, $\bar{h}^{\infty}$ must be trivial.

However, by the construction of the $\bar{h}^{i}$ we get that $\left|\left(\bar{h}^{\infty}\right)\left(c^{\infty}\right)\right| \leq\left|\left(\bar{h}^{\infty}-u\right)\left(c^{\infty}\right)\right|$ for any trivial Einstein variation $u$, contradicting the fact that $\bar{h}^{\infty}$ is nonzero. \(\square\)

\section*{7. Einstein variations of the hyperbolic cusp metric}

Consider the hyperbolic metric
$$g_{\text {hyp }}=r^{-2} \mathrm{~d} r^{2}+r^{2}\left(\mathrm{~d} x_{2}^{2}+\ldots+\mathrm{d} x_{n}^{2}\right)$$
on $\mathbb{R}^{+} \times \mathbb{R}^{n-1}$ and the parabolic isometric action of $\mathbb{R}^{n-1}$ by translations on the second factor.

Set $L:=L_{g_{h y p}}$. We will prove the following result:
Proposition 7.1. Let $h$ be a symmetric bilinear form on $\mathbb{H}^{n}$ that is invariant under the $\mathbb{R}^{n-1}$-action. Assume furthermore that $|h|<r^{0.1}+r^{-0.1}$.
Then $L h=0$ implies that $h$ is trivial.
Thus, if even $|h|<r^{ \pm 0.1}$, then $h \equiv 0$.

Proof. We assume $|h|<r^{0.1}+r^{-0.1}$. Express $h=h_{i j} \mathrm{~d} x_{i} \mathrm{~d} x_{j}$ where we set $x_{1}=r$. Then the $h_{i j}$ only depend on $r$ and the bound on $|h|$ implies
$$r^{2}\left|h_{11}\right|(r), \quad\left|h_{1 i}\right|(r), \quad r^{-2}\left|h_{i j}\right|(r)<r^{0.1}+r^{-0.1}$$
for $i, j>1$.
The equation $L h=0$ writes out as (see (2.4))
$$\Delta h+2 h-2(\operatorname{tr} h) g_{h y p}=0$$
which implies
$$\begin{aligned}
r^{2}\left(r^{2} h_{11}\right)^{\prime \prime}+n r\left(r^{2} h_{11}\right)^{\prime}-2(n-1)\left(r^{2} h_{11}\right) & =0 \\
r^{2} h_{1 i}^{\prime \prime}+n r h_{1 i}^{\prime}-n h_{1 i} & =0 \\
r^{2}\left(r^{-2} h_{i j}\right)^{\prime \prime}+n r\left(r^{-2} h_{i j}\right)^{\prime}-2 \delta_{i j} \sum_{k=2}^{n} r^{-2} h_{k k} & =0
\end{aligned}$$
The trace of $h$ satisfies (see (2.3))
$$\triangle \operatorname{tr} h-2(n-1) \operatorname{tr} h=0 .$$
In terms of coordinates, this implies for $q(r)=\operatorname{tr} h(r)$
$$r^{2} q^{\prime \prime}+n r q^{\prime}-2(n-1) q=0 .$$
The solutions of (I) and (IV) are both of the form $A_{1} r^{\gamma_{1}}+A_{2} r^{\gamma_{2}}$ with $\gamma_{1 / 2}=$ $\frac{1}{2}\left(-n+1 \pm \sqrt{n^{2}+6 n-7}\right)$. Hence by the bound on $|h|$ we get $r^{2} h_{11} \equiv \operatorname{tr} h \equiv 0$ and plugging this into (III) gives
$$r^{2}\left(r^{-2} h_{i j}\right)^{\prime \prime}+n r\left(r^{-2} h_{i j}\right)^{\prime}=0 .$$
Solutions of this equation are of the form $h_{i j}(r)=A_{1} r^{2}+A_{2} r^{-n+3}$ and thus $h_{i j}=u_{i j} r^{2}$ (for $i, j>1$ ).

Finally, (II) implies $h_{1 i}(r)=A_{1} r+A_{2} r^{-n}$, hence $h_{1 i} \equiv 0$ (for $i>1$ ). \(\square\)

\section*{8. Variations of the black-hole metric}

Consider the black-hole metric
$$g=g_{B H}=V^{-1} \mathrm{~d} r^{2}+V \mathrm{~d} \theta^{2}+r^{2}\left(\mathrm{~d} x_{3}^{2}+\ldots+\mathrm{d} x_{n}^{2}\right)$$
on $M_{B H} \approx \mathbb{R}^{2} \times \mathbb{R}^{n-2}$. Set $L=L_{g}$. Recall that $g$ is asymptotic to the hyperbolic metric
$$g_{h y p}=r^{-2} \mathrm{~d} r^{2}+r^{2}\left(\mathrm{~d} \theta^{2}+\mathrm{d} x_{2}^{2}+\ldots+\mathrm{d} x_{n}^{2}\right)$$
for $r \rightarrow \infty$ in the sense that $\left|\nabla^{m}\left(g-g_{\text {hyp }}\right)\right|=O\left(r^{-n+1}\right)$. This is why we can estimate
$$\left|L_{g} h-L_{g_{h y p}} h\right| \lesssim O\left(r^{-n+1}\right)|h|+O\left(r^{-n+1}\right)|\nabla h|+O\left(r^{-n+1}\right)\left|\nabla^{2} h\right|$$
for $r \rightarrow \infty$.
In the following we will analyze Einstein variations of $g_{B H}$ or variations which are almost Einstein. We will hereby always assume that these variations are invariant under the $S^{1} \times \mathbb{R}^{n-2}$ action. When we compare $g_{B H}$ with $g_{\text {hyp }}$, this action becomes the parabolic $\mathbb{R}^{n-1}$ action.

We remark that Olivier Biquard has independently found elementary proofs of some of the following results ([Biq2]).

Proposition 8.1. Let $R>r_{+}$and assume that on $M_{B H}(r \leq R)$ we have $L h=f$ for $S^{1} \times \mathbb{R}^{n-2}$ invariant $h$ and $f$ satisfying $|h|(r)<1$ and
$$|f|(r)<\alpha\left[\left(\frac{r}{R}\right)^{0.1}+r^{-0.1}\right]$$
for all $r \leq R$ and some $\alpha<1$. Then
$$|h|(r)<C\left(|h|(R)+\alpha+r^{-n+1.1}\right)$$
for some universal constant $C$ (which is independent of $R$ ).
We will need a technical Lemma. Note that from now on whenever we use the notation $O(\varphi(r))$ for a function $\varphi(r)$, we indicate an error term whose absolute value is always (not only for $r \rightarrow \infty$ ) bounded above by $C \varphi(r)$ where $C$ is a universal constant.

Lemma 8.2. Let $a, b \in \mathbb{R}$ and $0 \leq B_{1}, B_{2} \leq \infty$. Consider a solution $f$ : $\left(B_{1}, B_{2}\right) \rightarrow \mathbb{R}$ of the ODE
$$r^{2} f^{\prime \prime}(r)+a r f^{\prime}(r)+b f(r)=\varphi(r)$$
for some $\varphi:\left(B_{1}, B_{2}\right) \rightarrow \mathbb{R}$. Assume that $a, b$ are chosen in such a way that the corresponding homogeneous ODE (for $\varphi \equiv 0$ ) has the general solution $f(r)=$ $A_{1} r^{\gamma_{1}}+A_{2} r^{\gamma_{2}}$ with $\gamma_{1}, \gamma_{2} \in \mathbb{R}$ and $\gamma_{1}<\gamma_{2}$.

Now, suppose $\varphi(r)=\sum_{k=1}^{p} O\left(r^{\delta_{k}}\right)$ where we assume that $\delta_{k} \neq \gamma_{1}, \gamma_{2}$ for each $k$. Then $f(r)=A_{1} r^{\gamma_{1}}+A_{2} r^{\gamma_{2}}+\sum_{k=1}^{p} O\left(r^{\delta_{k}}\right)$.

Here the coefficients in $O\left(r^{\delta_{k}}\right)$ only depend on $a, b, \delta$ and the coefficients in the error terms of $\varphi$.

Proof. The Lemma follows by simple integration. \(\square\)

Proof of Proposition 8.1. We assume from now on that $|h|(r)<1$ and $R>r_{+}+2$. Using the Schauder estimates we find that this implies $\left|\nabla^{l} h\right|<C_{l}$, so
$$\left|L_{g} h-L_{g_{h y p}} h\right|=O\left(r^{-n+1}\right)$$
for $r>r_{+}+1$. In coordinates, the bound on $h$ implies that
$$r^{2}\left|h_{11}\right|(r), \quad\left|h_{1 i}\right|(r), \quad r^{-2}\left|h_{i j}\right|(r)<C$$
where $i, j>1$ and $r>r_{+}+1$ for the first quantity and $r \geq r_{+}$for the rest.
We will use the equations from the last section to derive a better estimate on $h$. Set $H=|h|(R)$.

We first show how to bound $r^{2} h_{11}$. By equation (I) of the last section and (8.1) it satisfies
$$r^{2}\left(r^{2} h_{11}\right)^{\prime \prime}+n r\left(r^{2} h_{11}\right)^{\prime}-2(n-1)\left(r^{2} h_{11}\right)=r^{2} f_{11}+O\left(r^{-n+1}\right),$$
where $r^{2} f_{11}(r)=O\left(\alpha\left(\frac{r}{R}\right)^{0.1}\right)+O\left(\alpha r^{-0.1}\right)$ for $r>r_{+}+1$. Lemma 8.2 gives us
$$r^{2} h_{11}(r)=A_{1} r^{\gamma_{1}}+A_{2} r^{\gamma_{2}}+O\left(\alpha\left(\frac{r}{R}\right)^{0.1}\right)+O\left(\alpha r^{-0.1}\right)+O\left(r^{-n+1}\right),$$
where $\gamma_{1 / 2}=\frac{1}{2}\left(-n+1 \pm \sqrt{n^{2}+6 n-7}\right)$. Observe that $\gamma_{1}>0.1$ and $\gamma_{2}<-n+1$. Since $r^{2} h_{11}$ and the error terms above are bounded for say $r \in\left(r_{+}+1, r_{+}+2\right)$, we conclude that $\left|A_{2}\right|<C$ for some universal $C$. For $r=R$, we furthermore obtain $\left|A_{1}\right|<C H R^{-\gamma_{1}}+O\left(R^{\gamma_{2}-\gamma_{1}}\right)+O\left(\alpha R^{-\gamma_{1}}\right)+O\left(R^{-n+1-\gamma_{1}}\right)$. Thus
$$r^{2}\left|h_{11}\right|(r)<C\left[H\left(\frac{r}{R}\right)^{\gamma_{1}}+\alpha\left(\frac{r}{R}\right)^{0.1}+\alpha r^{-0.1}+r^{-n+1}\right]<C\left(H+\alpha+r^{-n+1}\right) .$$
Using (IV) from the last section, we conclude that the same bound holds for $\operatorname{tr} h$. Moreover, we can estimate $h_{1 i}$ for $i>1$ by the same method (this time we have to use (II) and the fundamental solutions are $r$ and $r^{-n}$ ).

Using the first estimate from (8.2), we can now bound $r^{-2} h_{i j}$ for $i, j>1$. By (III) we obtain for $r>r_{+}+1$
$$r^{2}\left(r^{-2} h_{i j}\right)^{\prime \prime}+n r\left(r^{-2} h_{i j}\right)^{\prime}=O\left(H\left(\frac{r}{R}\right)^{\gamma_{1}}\right)+O\left(\alpha\left(\frac{r}{R}\right)^{0.1}\right)+O\left(\alpha r^{-0.1}\right)+O\left(r^{-n+1}\right) .$$
Thus using $O\left(r^{-n+1}\right)<O\left(r^{-n+1.1}\right)$, we conclude from Lemma 8.2
$$r^{-2} h_{i j}(r)=A_{1}+A_{2} r^{-n+1}+O\left(H\left(\frac{r}{R}\right)^{\gamma_{1}}\right)+O\left(\alpha\left(\frac{r}{R}\right)^{0.1}\right)+O\left(\alpha r^{-0.1}\right)+O\left(r^{-n+1.1}\right) .$$
As before, we find that $\left|A_{2}\right|<C$ and setting $r=R$ yields $\left|A_{1}\right|<C H+O(H+$ $\alpha)+O\left(R^{-n+1.1}\right)$, so
$$r^{-2}\left|h_{i j}\right|(r)<C\left(H+\alpha+r^{-n+1.1}\right) .$$ \(\square\)

We will now prove the second result of this section.
Proposition 8.3. Let $h$ be an $S^{1} \times \mathbb{R}^{n-2}$ invariant Einstein variation of $g_{B H}$ and assume $|h|(r) \rightarrow 0$ for $r \rightarrow \infty$. Then $h \equiv 0$.

We note that with a little more work, it is even possible to deduce that any $S^{1} \times \mathbb{R}^{n-2}$ invariant Einstein variation $h$ with $|h|(r) \rightarrow 0$ as $r \rightarrow \infty$ is of the form
$$h=-\operatorname{tr} u \frac{n-1}{V r^{n-1}} \mathrm{~d} r^{2}-\operatorname{tr} u \frac{V V^{\prime}}{2 r} \mathrm{~d} \theta^{2}+2(\operatorname{tr} u) r^{-n+3}\left(\mathrm{~d} x_{3}^{2}+\ldots+\mathrm{d} x_{n}^{2}\right)+u_{i j} r^{2} \mathrm{~d} x_{i} \mathrm{~d} x_{j}$$
for some symmetric $(n-2) \times(n-2)$ matrix $u_{i j}$ indexed by $i, j=3, \ldots, n$.
Assume from now on that $|h|(r) \rightarrow 0$ as $r \rightarrow \infty$ and that $L h=0$. Using Proposition 8.1, we find that we even have $|h|(r)<C r^{-n+1.1}$. By Schauder's estimates we can deduce the same decay for all covariant derivatives of $h$.

Lemma 8.4. We have $\operatorname{tr} h \equiv 0, \operatorname{div} h \equiv 0$ and hence $\operatorname{dRic}_{g}(h)+(n-1) h=0$.
Proof. This follows from the maximum principle applied to (2.3) resp. (2.6) and the fact that $\operatorname{tr} h$ and $\beta(h)$ are decaying. \(\square\)

Lemma 8.5. We have $h_{1 i}=h_{i 1} \equiv 0$ for all $i \geq 2$.
Proof. Writing out the equation $\operatorname{div} h=0$ in terms of the $h_{i j}$ gives for $i \geq 2$
$$0=-(\operatorname{div} h)_{i}=V h_{1 i}^{\prime}+\left(V^{\prime}+(n-2) \frac{V}{r}\right) h_{1 i}$$
The solutions of these ODEs behave like $\frac{1}{r-r_{+}}$for $r \rightarrow r_{+}$, so the $h_{1 i}$ must be constantly zero. \(\square\)

Now we will alter $h$ by an infinitesimal diffeomorphism $\operatorname{div}_{g}^{*} \xi$ for some 1-form $\xi$ to eliminate its 11 entry. Observe that by (2.2) for every 1 -form $\xi$ we have
$$\mathrm{d} \operatorname{Ric}_{g}\left(\operatorname{div}_{g}^{*} \xi\right)+(n-1) \operatorname{div}_{g}^{*} \xi=0$$
since $g$ is Einstein. So for any 1 -form $\xi$ the bilinear form $h+\operatorname{div}_{g}^{*} \xi$ will still be an infinitesimal Einstein variation. However, we might lose the divergence or trace freeness.

Lemma 8.6. There is an $S^{1} \times \mathbb{R}^{n-2}$ invariant 1-form $\xi=\xi_{1}(r) d r$ such that for $k=h+\operatorname{div}^{*} \xi$ we have $k_{1 i}=k_{i 1}=0$ for $i=1, \ldots, n$ and $|k|(r)<C$.

Moreover, if $k \equiv 0$, then $\xi \equiv 0$ and hence $k \equiv h$.
Proof. We compute
$$\begin{aligned}
\left(\operatorname{div}^{*} \xi\right)_{11} & =\xi_{1}^{\prime}+\frac{V^{\prime}}{2 V} \xi_{1}, \\
\left(\operatorname{div}^{*} \xi\right)_{22} & =\frac{1}{2} V V^{\prime} \xi_{1} \\
\left(\operatorname{div}^{*} \xi\right)_{i i} & =r V \xi_{1} \quad \text { for } i \geq 3
\end{aligned}$$
The remaining components are zero.
We now solve the ODE $\left(\operatorname{div}^{*} \xi\right)_{11}=-h_{11}$. Observe that it is equivalent to $\left(V^{1 / 2} \xi_{1}\right)^{\prime}=-V^{1 / 2} h_{11}$ and that $V\left|h_{11}\right|<C r^{-n+1.1}$. Hence, the solution
$$\xi_{1}(r):=-\frac{1}{V^{1 / 2}} \int_{r_{+}}^{r} \frac{V h_{11}}{V^{1 / 2}}$$
satisfies $V^{1 / 2}(r)\left|\xi_{1}\right|(r) \leq C\left(r-r_{+}\right)^{1 / 2}$ which implies smoothness of $\xi$ and boundedness of $\operatorname{div}^{*} \xi$.

Now, if $k \equiv 0$, then $\operatorname{tr} h \equiv 0$ implies $\operatorname{tr} \operatorname{div}^{*} \xi \equiv 0$ and thus
$$V \xi_{1}^{\prime}+\left(V^{\prime}+(n-2) \frac{V}{r}\right) \xi_{1}=0 .$$
Hence $\xi_{1}(r)=C V^{-1}(r) r^{-n+2}$ which behaves like $\frac{C}{2(n-1)} \frac{1}{r-r_{+}}$as $r \rightarrow r_{+}$contradicting the smoothness of $\xi$. \(\square\)

We will now show that $k$ has a very simple form. In order to do this, we introduce a new coordinate $s=s(r)$ (the distance to the origin) with the property that $s\left(r_{+}\right)=0$ and $g_{B H}=\mathrm{d} s^{2}+V(r(s)) \mathrm{d} \theta^{2}+r^{2}(s)\left(\mathrm{d} x_{3}^{2}+\ldots+\mathrm{d} x_{n}^{2}\right)$. From now on we will only work in the coordinate system $\left(s, \theta, x_{3}, \ldots, x_{n}\right)$. Consider a metric $\widehat{g}$ of the form
$$\widehat{g}(s)=\left(\begin{array}{cc}
1 & 0 \\
0 & M(s)
\end{array}\right) .$$
The condition of being Einstein with $\operatorname{Ric}_{\widehat{g}}=-(n-1) \widehat{g}$ is equivalent to the following system of ODEs (see e.g. [Lin]):
$$\begin{aligned}
\left(\sqrt{\operatorname{det} M} M^{\prime} M^{-1}\right)^{\prime}-2(n-1) \sqrt{\operatorname{det} M} E_{n-1} & =0 \\
\chi_{n-2}\left(M^{\prime} M^{-1}\right)-2(n-2)(n-1) & =0
\end{aligned}$$
where $E_{n-1}$ denotes the unit matrix of rank $n-1$ and $\chi_{n-2}$ the $(n-2)$-th coefficient of the characteristic polynomial, i.e. the elementary symmetric polynomial of degree 2 in the eigenvalues. The prime denotes differentiation by $s$.

Now denote by $M=\operatorname{diag}\left(V(r(s)), r^{2}(s), \ldots, r^{2}(s)\right)$ the matrix corresponding to the black-hole metric $g=g_{B H}$ and denote the given Einstein variation corresponding to $k_{2 \leq i, j \leq n}$ by $\dot{M}=\dot{M}(s)$. Then $\dot{M}$ is a variation $\dot{M}=\dot{M}(s)$ of (I) and (II). We will moreover abbreviate $u=\sqrt{\operatorname{det} M}$ and $\dot{u}=(\sqrt{\operatorname{det} M})^{\cdot}=\frac{1}{2} u \operatorname{tr}\left(\dot{M} M^{-1}\right)$.

Lemma 8.7. $u=A \sinh (n-1) s$ for some $A>0$ and $\dot{u}=\dot{A} u$. This implies $\operatorname{tr}_{g} k=\operatorname{tr} \dot{M}\left(M^{0}\right)^{-1} \equiv 2 \dot{A}$.

Proof. Tracing (I) yields
$$u^{\prime \prime}-(n-1)^{2} u=0$$
Since $u(0)=0$, we get $u=A \sinh (n-1) s$ and a variation of this equation gives $\dot{u}=$ $\dot{A} \sinh (n-1) s+\dot{B} \cosh (n-1) s$. So $\frac{1}{2} \operatorname{tr} k=\dot{A} A^{-1}+\dot{B} A^{-1} \cosh (n-1) s / \sinh (n-1) s$. Since $\operatorname{tr} k$ is bounded, we conclude $\dot{B}=0$ and therefore $\operatorname{tr} k \equiv$ const. \(\square\)

Now observe that by the symmetries $x_{i} \rightarrow-x_{i}(i \geq 3)$, also the matrix
$$\dot{M}^{\perp}:=\left(\begin{array}{cccc}
\dot{M}_{22} & -\dot{M}_{23} & \cdots & -\dot{M}_{2 n} \\
-\dot{M}_{32} & \dot{M}_{33} & \cdots & \dot{M}_{3 n} \\
\vdots & \vdots & \ddots & \vdots \\
-\dot{M}_{n 2} & \dot{M}_{n 3} & \cdots & \dot{M}_{n n}
\end{array}\right)$$
corresponds to an Einstein variation. Moreover, we can easily see that the entries $\dot{M}_{23}, \ldots, \dot{M}_{2 n}$ are odd functions in $s$ while all the other entries are even. So $\dot{M}$ is invariant under the transformation ⟂ combined with $s \rightarrow-s$.

Lemma 8.8. $\dot{M}=Q M$ where $Q$ is a symmetric matrix with $Q_{2 i}=Q_{i 2}=0$ for $i=2, \ldots, n$. Hence $\dot{M}=\dot{M}^{\perp}$ and $\dot{M}_{22}=0$.

Proof. A variation of (I) together with Lemma 8.7 gives
$$\left(\sinh ((n-1) s)\left(M^{\prime} M^{-1}\right)^{\prime}\right)^{\prime}=0 .$$
Hence
$$\left(M^{\prime} M^{-1}\right)^{\cdot}=\frac{1}{\sinh (n-1) s} P$$
for some constant matrix $P$. Moreover, observe that
$$\left(M^{\prime} M^{-1}\right)=\dot{M}^{\prime} M^{-1}-M^{\prime} M^{-1} \dot{M} M^{-1}=M\left(M^{-1} \dot{M}\right)^{\prime} M^{-1} .$$
So $\left(M^{\prime} M^{-1}\right)^{\text {⋅ }}$ is mapped to $-\left(M^{\prime} M^{-1}\right)^{\cdot}$ under the transformation ⟂ combined with $s \rightarrow-s$. Since $\sinh (n-1) s$ is odd, this implies that $P=P^{\perp}$, i.e. that $P$ is of block form
$$P=\left(\begin{array}{cccc}
P_{22} & 0 & \cdots & 0 \\
0 & P_{33} & \cdots & P_{3 n} \\
\vdots & \vdots & \ddots & \vdots \\
0 & P_{n 3} & \cdots & P_{n n}
\end{array}\right) .$$

Since by (8.3) the lower block of $\left(M^{\prime} M^{-1}\right)$ 'stays bounded for $s \rightarrow 0$, we find that the lower block of $(\sinh (n-1) s)^{-1} P$ must also stay bounded. Hence, the lower block of $P$ must be zero. Furthermore by (8.3) and $\operatorname{tr} M^{-1} \dot{M}=\operatorname{tr} \dot{M} M^{-1} \equiv$ $2 \dot{A}$, we find $\operatorname{tr}\left(M^{\prime} M^{-1}\right) \cdot=0$ and hence $\operatorname{tr} P=0$. So $P=0$ and we conclude using (8.3) again that $\dot{M} M^{-1}=Q$ for some constant matrix $Q$.

Now again since the problem is symmetric with respect to the transformation ⟂ combined with $s \rightarrow-s$ and constant functions are even, we conclude that $Q=Q^{\perp}$. Since moreover $M_{22}(s)=Q_{22} V(r(s))$, we conclude by smoothness at the origin that $Q_{22}=0$. \(\square\)

We can now summarize the discussion above: Returning to the old coordinates $\left(r, \theta, x_{3}, \ldots, x_{n}\right)$, we have proven so far that $h$ takes the following form
$$h=-\operatorname{div}^{*} \xi+r^{2} \sum_{i, j=3}^{n} u_{i j} \mathrm{~d} x_{i} \mathrm{~d} x_{j} .$$
So $h_{22}=-\left(\operatorname{div}^{*} \xi\right)_{22}$. By the equations from the proof of Lemma 8.6, we conclude from the decay of $h$ that $V^{1 / 2} \xi_{1}(r)<C r^{-n+1.1}$ hence $r^{-2}\left|\left(\operatorname{div}^{*} \xi\right)_{i i}\right|<C r^{-n+1.1}$ for $i \geq 3$. Together with $|h|<C r^{-n+1.1}$ this implies $u_{i j}=0$ and thus $k \equiv 0$. Hence by Lemma 8.6 we have $h \equiv 0$. This concludes the proof of Proposition 8.3.

\section*{References}
\begin{itemize}
\item[] [And1] M. Anderson, "Some results on the structure of conformally compact Einstein metrics" math/0402198 (February 12, 2004), http://arxiv.org/abs/math/0402198
\item[] [And2] M. Anderson, "Dehn filling and Einstein metrics in higher dimensions", Journal of Differential Geometry 73, no. 2 (2006): 219-261
\item[] [Biq1] O. Biquard, "Asymptotically symmetric Einstein metrics", SMF/AMS Texts and Monographs, 13, American Mathematical Society (2006)
\item[] [Biq2] O. Biquard, "Polycopié on differential geometry and global analysis" (2006), http://people.math.jussieu.fr/~biquard/dgga2007.pdf
\item[] [HK] C. Hodgson, S. Kerckhoff, "Universal bounds for hyperbolic Dehn surgery", Annals of Mathematics. Second Series 162, no. 1 (2005): 367-421.
\item[] [Lin] B. Linet, "The static, cylindrically symmetric strings in general relativity with cosmological constant" Journal of Mathematical Physics 27, no. 7 (July 1986), http://link.aip.org/link/?JMP/27/1817/1
\item[] [Thu] W. Thurston, "The Geometry and Topology of Three-Manifolds" (March, 2002), http://www.msri.org/publications/books/gt3m/
\item[] [Tia] G. Tian, "On constructing hyperbolic 3-manifolds", talk at the third Gökova Geometry/Topology conference (1994)
\item[] [Top] P. Topping, "Lectures on the Ricci Flow", (Cambridge University Press, 2006)
\end{itemize}

Department of Mathematics, Princeton University, Princeton, New Jersey 08544

E-mail address: rbamler@math.princeton.edu

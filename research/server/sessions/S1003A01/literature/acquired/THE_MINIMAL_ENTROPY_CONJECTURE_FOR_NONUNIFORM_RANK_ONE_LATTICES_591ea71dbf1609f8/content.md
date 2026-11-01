---
retention_scope: session
part: 1
total_parts: 1
---

---
source_file: math_0409311v3.pdf
converter: mathpix
format: mmd
---

\title{
THE MINIMAL ENTROPY CONJECTURE FOR NONUNIFORM RANK ONE LATTICES
}

\author{
PETER A. STORM
}

\begin{abstract}
The Besson-Courtois-Gallot theorem is proven for noncompact finite volume Riemannian manifolds. In particular, no bounded geometry assumptions are made. This proves the minimal entropy conjecture for nonuniform rank one lattices.
\end{abstract}

\section*{1. Introduction}

This paper proves the Besson-Courtois-Gallot theorem [2] for finite volume spaces.
Theorem 1.1. For $n \geq 3$, let $(M, b)$ be a finite volume orientable Riemannian $n$ manifold. Let $\left(Z, g_{0}\right)$ be an $n$-dimensional orientable finite volume negatively curved locally symmetric space. If $f: M \longrightarrow Z$ is a proper map of nonzero degree then
$$h(b)^{n} \operatorname{Vol}(M, b) \geq|\operatorname{deg}(f)| h\left(g_{0}\right)^{n} \operatorname{Vol}\left(Z, g_{0}\right),$$
with equality if and only if $f$ is proper homotopic to a homothetic covering map.
(See Theorems 7.1 and 9.1.) Here $h(b)$ (resp. $h\left(g_{0}\right)$ ) denotes the volume growth entropy of the Riemannian universal cover of $(M, b)$ (resp. $\left(Z, g_{0}\right)$ ). Theorem 1.1 places no bounded geometry assumptions on $(M, b)$. Results similar to Theorem 1.1 were previously obtained by Boland-Connell-Souto [3, 7] under additional hypotheses.

The author thanks Richard Canary, Chris Connell, Gilles Courtois, Juha Heinonen, Juan Souto, and Ralf Spatzier for many helpful conversations, and for listening to various preliminary versions of Theorem 1.1. The work of this paper was inspired by [2] and [3].

\section*{2. Sketch of the Proof}

In this section, we assume the reader is familiar with the seminal Besson-CourtoisGallot paper [2]. The proof of Theorem 1.1 differs from the original proof of the Besson-Courtois-Gallot theorem [2, pg.734] in two places. At these places, the original proof fails in the noncompact setting, and a new argument is required to arrive at the same conclusion. Rather than re-sketch arguments from [2], we skip straight to the ideas of this paper not found elsewhere. To streamline the exposition, several extra assumptions will be made in this section.

Let ( $Z, g_{0}$ ) be a noncompact oriented finite volume $n$-dimensional negatively curved locally symmetric space, for $n \geq 3$. Let $(Z, b)$ be another finite volume Riemannian metric on $Z$. As in [2], for $c>h(b)$ there exist uniformly Lipschitz $\mathcal{C}^{1}$-smooth $\pi_{1}$-equivariant maps

\footnotetext{
Date: January 6th, 2006.
This research was partially supported by an NSF Postdoctoral Fellowship.
}
$$\begin{array}{rll}
\Phi_{0}:\left(\widetilde{Z}, g_{0}\right) & \longrightarrow & S_{+}^{\infty} \subset L^{2}\left(\partial\left(\widetilde{Z}, g_{0}\right)\right) \\
\Phi_{c}:(\widetilde{Z}, b) & \longrightarrow & S_{+}^{\infty} \subset L^{2}\left(\partial\left(\widetilde{Z}, g_{0}\right)\right),
\end{array}$$
where $S_{+}^{\infty}$ is the subset of strictly positive functions of unit norm, $\Phi_{0}$ is the square root of the Poisson kernel, and $\Phi_{c}$ is a synthetically defined analogue of $\Phi_{0}$ for a general Riemannian manifold. If bar : $L_{+}^{2}(\partial \widetilde{Z}) \longrightarrow\left(\widetilde{Z}, g_{0}\right)$ is the barycenter map, and $\Omega$ is the closed $n$-form bar* $d \operatorname{vol}_{g_{0}}$, then $\Phi_{0}$ calibrates the restricted closed $n$ form $\left.\Omega\right|_{S_{+}^{\infty}}$. Let $H: \widetilde{Z} \times[0,1] \longrightarrow L^{2}$ be the straight line homotopy from $\Phi_{0}$ to $\Phi_{c}$. As everything is equivariant, the closed $n$-forms $\Phi_{0}^{*} \Omega, \Phi_{c}^{*} \Omega$, and $H^{*} \Omega$ are $\pi_{1}$ invariant and descend to forms on $Z, Z$ and $Z \times[0,1]$ respectively.

Part 1 (Sections 6-7): Prove that $h(b)^{n} \operatorname{Vol}(Z, b) \geq h\left(g_{0}\right)^{n} \operatorname{Vol}\left(Z, g_{0}\right)$.
In the noncompact setting, the proof of this inequality in [2] fails at one key point. Namely, we would like to claim the equation
$$\int_{Z} \Phi_{c}^{*} \Omega-\int_{Z} \Phi_{0}^{*} \Omega \stackrel{?}{=} \int_{Z \times[0,1]} d H^{*} \Omega=\int_{Z \times[0,1]} 0=0$$
holds by Stokes' Theorem. But $Z$ is noncompact, so Stokes' Theorem may not be applied directly. Instead we must pick a compact exhaustion $Z_{i} \subset Z_{i+1} \subset \ldots$ of $Z$ by codimension zero submanifolds, and apply Stokes' theorem to each $Z_{i}$. This yields
$$\int_{Z_{i}} \Phi_{c}^{*} \Omega-\int_{Z_{i}} \Phi_{0}^{*} \Omega \pm \int_{\partial Z_{i} \times[0,1]} H^{*} \Omega=0$$
Equation (1) would follow by proving the error term in equation (2), i.e. the third summand, goes to zero as $i \rightarrow \infty$. This estimate involves:
- Finding a good compact exhaustion $\left\{Z_{i}\right\}_{i}$ such that the $(n-1)$-dimensional volume of $\left(\partial Z_{i}, b\right)$ goes to zero. This is easy using a global smooth proper 1-Lipschitz function on $(Z, b)$, which always exists [5].
- Finding a map $f: Z \longrightarrow Z$ properly homotopic to the identity such that $\left.f\right|_{\partial Z_{i}}$ is 1-Lipschitz for all $i$. This is possible because the ends of the locally symmetric space $\left(Z, g_{0}\right)$ are negatively curved cusps, which contract exponentially toward infinity. The map $f$ can be pushed out the cusps of $\left(Z, g_{0}\right)$ until it is 1-Lipschitz on the slices $\left(\partial Z_{i}, b\right)$. Homotopies which push maps further out the ends are proper homotopies, so this deformation of $f$ is admissible, despite the fact that it will not necessarily have bounded tracks in $\left(Z, g_{0}\right)$.
- Controlling the stretching of the straight line homotopy from $\Phi_{c}$ to $\Phi_{0} \circ f$. This follows from elementary estimates.
After proving the error term in equation (2) goes to zero, equation (1) follows. The rest of Part 1 proceeds as in [2].

Part 2 (Section 9): If $h(b)^{n} \operatorname{Vol}(Z, b)=h\left(g_{0}\right)^{n} \operatorname{Vol}\left(Z, g_{0}\right)$ then prove that the identity map is properly homotopic to an isometric homeomorphism.

Assume
$$h(b)^{n} \operatorname{Vol}(Z, b)=h\left(g_{0}\right)^{n} \operatorname{Vol}\left(Z, g_{0}\right) .$$
After possibly rescaling the metrics, we may also assume that $h(b)=h\left(g_{0}\right)=h$. For $c>h$, define the natural map $(\widetilde{Z}, b) \longrightarrow\left(\widetilde{Z}, g_{0}\right)$ as the composition of $\Phi_{c}$ :
$(\widetilde{Z}, b) \longrightarrow L_{+}^{2}$ and the barycenter map bar : $L_{+}^{2} \longrightarrow\left(\widetilde{Z}, g_{0}\right) \cong \mathbb{H}^{n}$. These maps descend to a family of maps $F_{c}:(Z, b) \longrightarrow\left(Z, g_{0}\right)$, which are each homotopic to the identity map $Z \longrightarrow Z$. Using equation (3) we show that $\operatorname{Jac} F_{c} \leq(c / h)^{n}$ and $\mathrm{Jac} F_{c}$ converges to the constant function 1 in $L^{1}\left(Z, d \operatorname{vol}_{b}\right)$.

For a generic point $p \in(Z, b)$, we can force some sequence of maps $F_{c_{i}}$ to converge uniformly on a small neighborhood of $p$. This is done by post-composing each $F_{c}$ by an appropriate orientation preserving isometry $\gamma_{c} \in \operatorname{Isom}^{+}\left(\widetilde{Z}, g_{0}\right)$. Using the arguments of [2], we may conclude that the maps $\gamma_{c_{i}} \circ F_{c_{i}}$ converge uniformly near $p$ to a 1-Lipschitz map $F^{p}$. A short topological argument shows that these locally defined maps can be pieced together to form a global 1-Lipschitz map $F:(Z, b) \longrightarrow$ $\left(Z, g_{0}\right)$.

The remainder of the argument is devoted to proving that $\operatorname{Jac} F=1$ a.e.. If this is not true, then $F$ strictly shrinks volume by some definite amount on a fixed compact submanifold of $(Z, b)$. After choosing a submanifold $\left\{\partial Z_{i}\right\}$ which is very far from this compact set, we modify the map $F$ near $\partial Z_{i}$ to make it proper, while adding very little volume to its image in $\left(Z, g_{0}\right)$. This modification involves coning off the map $F$ near the slice $\partial Z_{i}$, forcing it to leave compact sets at a definite rate. This coning operation adds very little volume to the image because the target manifold $\left(Z, g_{0}\right)$ has pinched negative curvature. Therefore even after coning the modified map still globally shrinks volume by some definite amount. A short topological argument shows that the modified map is proper, and so we can apply the change of variables formula to it. By the hypothesis that $(Z, b)$ and $\left(Z, g_{0}\right)$ have equal volume, the change of variables formula implies that the modified map cannot shrink volume globally. This yields a contradiction, showing that Jac $F=1$ a.e..

We may then apply the theory of quasiregular maps (see Section 3.4) to conclude that $F$ is in fact a local isometry. This implies that $(Z, b)$ is a finite volume negatively curved locally symmetric space. With this information the rest of the proof follows easily.

\section*{3. Preliminaries}

All Riemannian manifolds in this paper are assumed to be oriented and smooth with smooth Riemannian metrics.

Once and for all, let us fix the notation of Theorem 1.1 For $n \geq 3$, let $(M, b)$ be a connected finite volume Riemannian $n$-manifold. Let ( $Z, g_{0}$ ) be an $n$-dimensional finite volume negatively curved locally symmetric space. Let $f: M \longrightarrow Z$ be a proper map of nonzero degree. Since only the proper homotopy class of $f: M \longrightarrow Z$ is important, we may assume without a loss of generality that $f$ is smooth. We will denote the Riemannian universal cover of $(M, b)$ (resp. $\left(Z, g_{0}\right)$ ) by $(\widetilde{M}, b)$ (resp. $\left.\left(\widetilde{Z}, g_{0}\right)\right)$. Fix a basepoint $o \in \widetilde{Z}$. Let $f: \widetilde{M} \longrightarrow \widetilde{Z}$ also denote the lifted map between universal covers. (To avoid confusion, the domain and range of the map will always be specified.)
3.1. Volume growth entropy. Let $(N, g)$ be a connected Riemannian manifold. Let $(\widetilde{N}, g)$ be the universal cover of $N$ equipped with the lifted metric. The volume growth entropy of $(\widetilde{N}, g)$ is the number
$$h(g):=\limsup _{R \rightarrow \infty} \frac{1}{R} \log \operatorname{Vol}_{g}\left(B_{\widetilde{N}}(x, R)\right),$$
where $x \in \widetilde{N}$, and $B_{\widetilde{N}}(x, R) \subset \widetilde{N}$.
(The volume growth entropy is independent of the choice of $x \in \widetilde{N}$.)
3.2. Visual measure. For the negatively curved rank one symmetric space $\left(\widetilde{Z}, g_{0}\right)$, let $P: S_{p} \widetilde{Z} \longrightarrow \partial \widetilde{Z}$ be the standard radial homeomorphism between the unit tangent sphere and the boundary at infinity. Normalize Lebesgue measure on $S_{p} \widetilde{Z}$ to have mass 1 . Define $\mu_{p}$ to be the push-forward by $P$ of the normalized Lebesgue measure on $S_{p} \widetilde{Z}$. This probability measure is known as visual measure at $p$.
3.3. The barycenter map. Let $\left\{B_{\theta}\right\}_{\theta \in \partial Z}$ be the Busemann functions of $\left(\widetilde{Z}, g_{0}\right)$, normalized such that $B_{\theta}(o)=0$ for all $\theta \in \partial \widetilde{Z}$. Consider the Hilbert space $L^{2}(\partial \widetilde{Z})$ of square integrable functions on $\partial \widetilde{Z}$ with respect to the visual measure $\mu_{o}$. Define an $\operatorname{Isom}\left(\widetilde{Z}, g_{0}\right)$-action on $L^{2}(\partial \widetilde{Z})$ by
$$(\gamma . \phi)(\theta):=\phi\left(\gamma^{-1} . \theta\right) \cdot \sqrt{\exp \left(-h\left(g_{0}\right) B_{\theta}(\gamma . o)\right)} .$$
Then $\operatorname{Isom}\left(\widetilde{Z}, g_{0}\right)$ acts by isometries on $L^{2}(\partial \widetilde{Z})$. Let $L_{+}^{2}$ denote the strictly positive functions in $L^{2}(\partial \widetilde{Z})$. Note that $\operatorname{Isom}\left(\widetilde{Z}, g_{0}\right)$ acts by isometries on $L_{+}^{2}$.

Following [2, Sec.5], define the barycenter map bar : $L_{+}^{2} \longrightarrow\left(\widetilde{Z}, g_{0}\right)$ by the implicit equation
$$\int_{\partial \widetilde{Z}}\left\langle\nabla B_{\theta}, v\right\rangle_{\operatorname{bar}(\phi)} \phi(\theta)^{2} d \mu_{o}(\theta)=0$$
for all $v \in T_{\operatorname{bar}(\phi)} \widetilde{Z}$. The barycenter map is well defined, $\mathcal{C}^{1}$-smooth, and $\operatorname{bar}(c \phi)=$ $\operatorname{bar}(\phi)$ for all $\phi \in L_{+}^{2}$ and $c>0$ [2, Sec.5].
3.4. Quasiregular maps. The following fact will be used in the proof of Proposition 9.1

Theorem 3.1. Let $U \subset \mathbb{R}^{n}$ be open. Let $\left(U, g_{U}\right),\left(\mathbb{R}^{n}, g\right)$ be Riemannian manifolds. If $f:\left(U, g_{U}\right) \longrightarrow\left(\mathbb{R}^{n}, g\right)$ is locally 1-Lipschitz and Jac $f=1$ almost everywhere in $U$, then $f$ a local homeomorphism and a local isometry.

By the 1970s, this fact was well known to many Siberian and Finnish analysts. In particular, Theorem 3.1 follows from the more general [6, Thm.10.5], proved independently by Gol'dshtein and Martio-Rickman-Väisälä (both building on work of Reshetnyak [6]). ([6, Thm.10.5] is stated only for Euclidean space. As usual, the Riemannian case follows by considering small neighborhoods nearly isometric to Euclidean neighborhoods.) A self-contained proof of Theorem 3.1 can be obtained from the arguments of [2, App.C]. The statements of [2, App.C] are made for closed manifolds, but by using local topological degree the arguments can be applied locally to prove Theorem 3.1

\section*{4. The map into Hilbert space}

This section is a restatement of facts from 2 . Following [2, Sec.2.3,Sec.8], in this section we define a family of $\pi_{1}$-equivariant $\mathcal{C}^{1}$ maps
$$\Phi_{c}^{b}:(\widetilde{M}, b) \longrightarrow S_{+}^{\infty} \subset L^{2}(\partial \widetilde{Z}) \text { for } c>h(b):=h((\widetilde{Z}, b)) .$$
As before, $L^{2}(\partial \widetilde{Z})$ is the Hilbert space of square integrable functions on $\partial \widetilde{Z}$ with respect to the visual measure at the basepoint $o \in \widetilde{Z} . S_{+}^{\infty} \subset L^{2}(\partial \widetilde{Z})$ is the subset of strictly positive functions of unit norm.

For $c>h(b)$ define
$$\begin{aligned}
\Psi_{c}^{b}:(\widetilde{M}, b) \times \partial \widetilde{Z} & \longrightarrow \mathbb{R} \\
(p, \theta) & \longmapsto\left(\int_{\widetilde{M}} e^{-c d_{b}(p, y)} e^{-h\left(g_{0}\right) B_{\theta}(f(y))} d \operatorname{vol}_{b}(y)\right)^{1 / 2}
\end{aligned}$$
and
$$\Phi_{c}^{b}(p, \theta):=\frac{\Psi_{c}^{b}(p, \theta)}{\left(\int_{\partial \widetilde{Z}}\left(\Psi_{c}^{b}(p, \theta)\right)^{2} d \theta\right)^{1 / 2}}$$
$\Phi_{c}^{b}$ defines a map into function space by fixing its first coordinate:
$$\begin{aligned}
\Phi_{c}^{b}:(\widetilde{M}, b) & \longrightarrow\{\text { fcts. on } \partial \widetilde{Z}\} \\
p & \longmapsto \Phi_{c}^{b}(p, \cdot) .
\end{aligned}$$

Lemma 4.1. [2, Lem.2.4] The map $p \longmapsto \Phi_{c}^{b}(p, \cdot)$ is a $\pi_{1}$-equivariant $\mathcal{C}^{1}$ map from $\widetilde{M}$ into $S_{+}^{\infty} \subset L^{2}(\partial \widetilde{Z})$. Moreover, for $u \in T_{p} \widetilde{M}$,
$$\int_{\partial \widetilde{Z}}\left|u . \Phi_{c}^{b}(x, \theta)\right|^{2} d \theta \leq \frac{c^{2}}{4} b(u, u)_{p}$$
(see [1, pg.430]).
Using $\Phi_{c}^{b}$, pull back the metric on $S_{+}^{\infty}$ to $\widetilde{M}$. This defines the positive semidefinite $(0,2)$-tensor
$$g_{\Phi_{c}^{b}}(u, v):=\left\langle d \Phi_{c}^{b}(u), d \Phi_{c}^{b}(v)\right\rangle_{L^{2}(\partial \widetilde{Z})} .$$
From the inequality of Lemma 4.1, we obtain [2, pg.744]
$$\left\|d \Phi_{c}^{b}(u)\right\|^{2}=g_{\Phi_{c}^{b}}(u, u) \leq \frac{c^{2}}{4} b(u, u) .$$
The $\pi_{1}$-equivariance of $\Phi_{c}^{b}$ implies the tensor $g_{\Phi_{c}^{b}}$ is $\pi_{1}$-invariant. It thus descends to a tensor $g_{\Phi_{c}^{b}}$ on $M$.
Proposition 4.2. [2, Prop.3.4]
$$\left|J a c \Phi_{c}^{b}\right| \leq\left(\frac{c^{2}}{4 n}\right)^{n / 2} . \quad \text { In particular, } \quad \operatorname{Vol}\left(M, g_{\Phi_{c}^{b}}\right) \leq\left(\frac{c^{2}}{4 n}\right)^{n / 2} \operatorname{Vol}(M, b) .$$
(Notice inequality (4) does not immediately imply Proposition 4.2. Better estimates are required.)

For the locally symmetric space $\left(Z, g_{0}\right)$, stronger statements are true. Define
$$\begin{aligned}
\Phi_{0}:\left(\widetilde{Z}, g_{0}\right) & \longrightarrow S_{+}^{\infty}(\partial \widetilde{Z}) \\
p & \longmapsto \exp \left(-\frac{h\left(g_{0}\right)}{2} B_{\theta}(p)\right) .
\end{aligned}$$
Using $\Phi_{0}$, pullback the metric on $S_{+}^{\infty}$ to $\widetilde{Z}$. This defines the tensor
$$g_{\Phi_{0}}(u, v):=\left\langle d \Phi_{0}(u), d \Phi_{0}(v)\right\rangle_{L^{2}(\partial \widetilde{Z})} .$$
It has been proven that
$$g_{\Phi_{0}}=\frac{h\left(g_{0}\right)^{2}}{4 n} g_{0}, \quad \text { implying } \quad \operatorname{Vol}\left(Z, g_{\Phi_{0}}\right)=\left(\frac{h\left(g_{0}\right)^{2}}{4 n}\right)^{n / 2} \operatorname{Vol}\left(Z, g_{0}\right)$$
[2, pgs.743-744].

\section*{5. Calibration theory}

This section introduces the terminology from calibration theory necessary to properly cite [2, Sec.4-5].

For the purpose of giving clear definitions, let us for the moment consider a more general situation. Let $N$ be an oriented $n$-manifold. Let $\mathcal{H}$ be a (real) Hilbert manifold (e.g. $S_{+}^{\infty} \subset L^{2}$ ). Assume there exists an isometric group action $\pi_{1}(N) \times$ $\mathcal{H} \longrightarrow \mathcal{H}$. Any $\pi_{1}(N)$-equivariant $\mathcal{C}^{1}$ map defines a $\pi_{1}(N)$-invariant symmetric positive semi-definite (0, 2)-tensor
$$g_{\Theta}(u, v):=\langle d \Theta(u), d \Theta(v)\rangle_{\mathcal{H}} .$$
This tensor descends to $N$, and determines a volume form $d \mathrm{vol}_{\Theta}$. Thus we may define
$$\operatorname{Vol}(\Theta):=\int_{N} d \operatorname{vol}_{\Theta}$$

Define the comass of an $n$-form $\alpha$ on $\mathcal{H}$ to be
$$\operatorname{comass}(\alpha):=\sup \left|\alpha_{x}\left(v_{1}, \ldots, v_{n}\right)\right|,$$
where the supremum is taken over all $x \in \mathcal{H}$ and all orthonormal $n$-tuples $\left\{v_{i}\right\}_{i=1}^{n}$ of $\mathcal{H}$. Then for any $\pi_{1}(N)$-invariant $n$-form $\alpha$, we have the inequality
$$\operatorname{Vol}(\Theta) \geq \frac{1}{\operatorname{comass}(\alpha)} \int_{N} \Theta^{*} \alpha .$$
A closed $\pi_{1}(N)$-invariant $n$-form $\omega$ calibrates an immersion $\Theta$ if for all $p \in N$ and positively oriented bases $\left\{v_{1}, \ldots, v_{n}\right\}$ of $T_{p} N$ we have
$$\omega_{\Theta(p)}\left(d \Theta\left(v_{1}\right), \ldots, d \Theta\left(v_{n}\right)\right)=\operatorname{comass}(\omega) \quad\left(\operatorname{det}\left(\left\langle d \Theta\left(v_{i}\right), d \Theta\left(v_{j}\right)\right\rangle\right)_{i j}\right)^{1 / 2}$$
The most important property of a calibrating pair $\omega, \Theta$ is
$$\operatorname{Vol}(\Theta)=\frac{1}{\operatorname{comass}(\Theta)} \int_{N} \Theta^{*} \omega .$$

A key tool for proving this paper's main result is
Theorem 5.1. [2, Prop.5.7] Recall the immersion $\Phi_{0}: \widetilde{Z} \longrightarrow S_{+}^{\infty}$ of Section 4. and the $\mathcal{C}^{1}$ barycenter map bar : $L_{+}^{2} \longrightarrow \widetilde{Z}$ of Section 3.3. The form $\Omega:=$ bar $^{*}\left(\right.$ dvol $\left._{g_{0}}\right)$ is a closed $\pi_{1}(Z)$-invariant $n$-form. The restricted form $\left.\Omega\right|_{S_{+}^{\infty}}$ calibrates the immersion $\Phi_{0}$ in the Hilbert manifold $S_{+}^{\infty}$. Moreover,
$$\operatorname{comass}\left(\left.\Omega\right|_{S_{+}^{\infty}}\right)=\left(\frac{4 n}{h\left(g_{0}\right)^{2}}\right)^{n / 2} .$$

Recall that $L_{+}^{2} \subset L^{2}(\partial \widetilde{Z})$ is the subset of strictly positive functions. For later reference, we note

Lemma 5.2. If $B(0, .5)$ is the open ball of radius .5 about the origin in $L^{2}(\widetilde{Z})$, then the comass of the form $\Omega:=$ bar $^{*}\left(\right.$ dvol $\left._{g_{0}}\right)$ is uniformly bounded above on the subset $L_{+}^{2}-B(0, .5)$.

Proof: Radial projection to $S_{+}^{\infty}$ is 2-Lipschitz on $L_{+}^{2}-B(0, .5)$. The barycenter map is invariant under radial projection (see Section 3.3). The lemma now follows from the fact that the comass of $\Omega$ restricted to $S_{+}^{\infty}$ is finite. \(\square\)

\section*{6. Estimates on the straight line homotopy}

Recall that $\left(Z, g_{0}\right)$ is a connected $n$-dimensional negatively curved locally symmetric space, $(M, b)$ is a connected Riemannian $n$-manifold, and $f: M \longrightarrow Z$ is a proper map of nonzero degree. Let $f: \widetilde{M} \longrightarrow \widetilde{Z}$ also denote the lifted map between universal covers. Recall also that $S_{+}^{\infty} \subset L^{2}(\partial \widetilde{Z})$ is the subset of strictly positive functions of unit norm, and $L_{+}^{2} \subset L^{2}(\partial \widetilde{Z})$ is the subset of strictly positive functions.

Let $\Theta, \Upsilon: \widetilde{M} \longrightarrow S_{+}^{\infty} \subset L^{2}(\partial \widetilde{Z})$ be any two $\mathcal{C}^{1}$ maps which are equivariant with respect to the $\pi_{1}(M)$-action on $S_{+}^{\infty}$ induced by the homomorphism $f_{*}: \pi_{1}(M) \longrightarrow$ $\pi_{1}(Z)$. The goal of this section is to prove the straight line homotopy from $\Theta$ to $\Upsilon$ does not stretch too much. These estimates will be used in the proof of Theorem 7.1 .

Define the straight line homotopy as
$$\begin{aligned}
H: \widetilde{M} \times[0,1] \times \partial \widetilde{Z} & \longrightarrow \mathbb{R}_{+} \\
(x, t, \theta) & \longmapsto[(1-t) \Theta(x, \theta)+t \Upsilon(x, \theta)]
\end{aligned}$$
By fixing the first two coordinates, this defines a $\mathcal{C}^{1}$ map $H: \widetilde{M} \times[0,1] \longrightarrow L_{+}^{2}$. $\pi_{1}$-equivariance follows from the equivariance of $\Theta, \Upsilon$.

For a slice of the homotopy
$$\begin{aligned}
H^{t}: \widetilde{M} & \longrightarrow L_{+}^{2} \\
x & \longmapsto\{\theta \mapsto H(x, t, \theta)\} \in L_{+}^{2},
\end{aligned}$$
we now estimate how much $H^{t}$ stretches $\widetilde{M}$ in terms of $\Theta, \Upsilon$. Let $v \in T_{x} \widetilde{M}, t \in$ [0,1]. Note that $d H_{x}^{t}(v)$ is an element of the tangent space $T_{H^{t}(x)} L^{2}(\partial \widetilde{Z})=L^{2}(\partial \widetilde{Z})$. In particular, $d H_{x}^{t}(v)$ is a function of $\theta \in \partial \widetilde{Z}$. We compute
$$\left[d H_{x}^{t}(v)\right](\theta)=(1-t)\left[d \Theta_{x}(v)\right](\theta)+t\left[d \Upsilon_{x}(v)\right](\theta) .$$
Using the inequality
$$[(1-t) \delta+t \eta]^{2} \leq(1-t) \delta^{2}+t \eta^{2} \text { for all } t \in[0,1], \delta, \eta \in \mathbb{R},$$
we estimate
$$\begin{aligned}
\left\|d H_{x}^{t}(v)\right\|^{2} & =\int_{\partial \widetilde{Z}}\left[d H_{x}^{t}(v)\right](\theta)^{2} d \theta \\
& \leq \int_{\partial \widetilde{Z}}\left\{(1-t)\left[d \Theta_{x}(v)\right](\theta)^{2}+t\left[d \Upsilon_{x}(v)\right](\theta)^{2}\right\} d \theta \\
& \leq\left\|d \Theta_{x}(v)\right\|^{2}+\left\|d \Upsilon_{x}(v)\right\|^{2}
\end{aligned}$$

We now estimate how much $H$ stretches in the time direction. Let $\frac{\partial}{\partial \tau}$ be the standard positive basis vector of $T_{t}[0,1]$. We compute
$$d H_{(x, t)}\left(\frac{\partial}{\partial \tau}\right)=\left.\frac{\partial}{\partial \tau} H(x, \tau)\right|_{\tau=t}=-\Theta(x)+\Upsilon(x) .$$
Suppressing unnecessary notation, we estimate
$$\left\|\frac{\partial}{\partial \tau} H\right\|^{2}=\int_{\partial \widetilde{Z}}[\Upsilon-\Theta]^{2} \leq \int_{\partial \widetilde{Z}}\left[\Upsilon^{2}+\Theta^{2}\right]=2 .$$
Here we used the fact that $\Upsilon$ and $\Theta$ are maps to positive functions.

\section*{7. The Besson-Courtois-Gallot inequality}

The goal of this section is to prove
Theorem 7.1. For $n \geq 3$, let $(M, b)$ be a finite volume oriented Riemannian $n$ manifold. Let $\left(Z, g_{0}\right)$ be an $n$-dimensional oriented finite volume negatively curved locally symmetric space. If $f: M \longrightarrow Z$ is a proper orientation preserving map of nonzero degree then
$$h(b)^{n} \operatorname{Vol}(M, b) \geq|\operatorname{deg}(f)| h\left(g_{0}\right)^{n} \operatorname{Vol}\left(Z, g_{0}\right) .$$
(In the important special case where $M=Z$ and $f: M \longrightarrow Z$ is the identity map, several technical details do not arise. Until the argument is clear, the reader is encouraged to read the proof with this special case in mind.)

For $M$ and $Z$ compact, Theorem 7.1 was first proven in [2]. If $M$ is not compact then $Z$ is not compact, because $f$ is proper. On the other hand, if $Z$ is not compact then $M$ is not compact because $f$ has nonzero degree. We may therefore assume without a loss of generality that neither $M$ nor $Z$ is compact. Recall $\widetilde{Z}$ (resp. $\widetilde{M}$ ) is the universal cover of $Z$ (resp. $M$ ). After possibly reversing the orientation of $M$, we may assume that $f$ has positive degree. Let $f: \widetilde{M} \longrightarrow \widetilde{Z}$ also denote the lifted map. By choosing a smooth approximation, we may assume without a loss of generality that $f$ is smooth.
$\left(Z, g_{0}\right)$ is a finite volume negatively curved locally symmetric space. By the thick-thin decomposition, $Z$ has a compact submanifold whose complement splits as a smooth manifold into a product region $Y^{n-1} \times[0, \infty)$, where the manifold $Y$ may not be connected. The product structure $Y \times[0, \infty)$ can be chosen to be a standard horospherical foliation. So we may assume the $(n-1)$-dimensional $g_{0}$ volume of the leaf $Y \times\{r\}$ decreases monotonically to zero as $r \rightarrow \infty$. Moreover, we may assume that the shift map
$$\begin{aligned}
\sigma_{r}: Y \times[0, \infty) & \longrightarrow Y \times[0, \infty) \\
(y, t) & \longmapsto(y, t+r)
\end{aligned}$$
is $K(r)$-Lipschitz with $K(r)$ going to zero monotonically as $r \rightarrow \infty$.
Since $\operatorname{Vol}(M, b)$ is finite, we can prove
Lemma 7.2. (1) There exists a compact exhaustion $\left\{M_{i}\right\}$ of $M$ such that each $M_{i} \subset M$ is a smooth submanifold and the $(n-1)$-dimensional $b$-volume of $\partial M_{i}$ goes to zero as $i \rightarrow \infty$.
(2) The map $f: M \longrightarrow Z$ may be altered by a proper homotopy such that the restriction of $f: M \longrightarrow Z$ to $\cup \partial M_{i}$ is locally 1-Lipschitz.

Proof: There exists a smooth 1-Lipschitz proper function $\delta: M \longrightarrow[0, \infty)$ (see for example [5, Sec.2]). This yields the estimate
$$\begin{aligned}
\operatorname{Vol}(M, b) \geq \int_{M}|\nabla \delta| d \operatorname{vol}_{b} & \geq \int_{\delta^{-1} \text { (reg. val.) }}|\nabla \delta| d \operatorname{vol}_{b} \\
& =\int_{\text {reg. val. }}\left\{(n-1) \text { dim'l } b-\text { vol. of } \delta^{-1}(t)\right\} d t
\end{aligned}$$
where "reg. val." indicates the regular values of the function $\delta$. By Sard's Theorem there must be a sequence $t_{i} \rightarrow \infty$ such that
$$\left\{(n-1) \text { dim'l } b-\text { vol. of } \delta^{-1}\left(t_{i}\right)\right\} \longrightarrow 0 .$$

Define $M_{i}:=\delta^{-1}\left(\left[0, t_{i}\right]\right)$. This proves part (1).
Without a loss of generality, we may assume that for all $i$ the image $f\left(\partial M_{i}\right)$ is contained in the product region $Y \times(0, \infty) \subset Z$. Suppose that for all $i<i_{0}$, the restricted map $\left.f\right|_{\partial M_{i}}$ is 1-Lipschitz. We can push $f\left(\overline{M-M_{i_{0}}}\right)$ out the ends of $\left(Z, g_{0}\right)$ by a family of shift maps $\sigma_{r}$ until the restricted map $\left.\left(\sigma_{r} \circ f\right)\right|_{\partial M_{i_{0}}}$ is 1-Lipschitz. This family of shift maps can be smoothly extended to all of $M$ without altering the map $f$ on $M_{i_{0}-1} \subset M$, thus yielding a homotopy of $f$. As this homotopy only pushes further out the ends of $Z$, it is a proper homotopy. This proves part (2). \(\square\)
(If $M=Z$ then the above proof shows that the identity map is proper isotopic to a diffeomorphism $f: Z \longrightarrow Z$ such that the $\left.f\right|_{\partial M_{i}}$ is 1-Lipschitz. In particular, after pulling back the metric, one may again assume that the identity map satisfies the conclusions of the above lemma.) Without a loss of generality, less us assume the proper map $f: M \longrightarrow Z$ satisfies the conclusions of Lemma 7.2.

Recall the two $\pi_{1}$-equivariant $\mathcal{C}^{1}$ maps
$$\Phi_{c}^{b}, \Phi_{0} \circ f: \widetilde{M} \longrightarrow S_{+}^{\infty} \subset L^{2}(\partial \widetilde{Z}),$$
for $c>h(b)$. Let $H: \widetilde{M} \times[0,1] \longrightarrow L_{+}^{2}$ denote the straight line homotopy (which is $\pi_{1}$-equivariant) from $\Phi_{c}^{b}$ to $\Phi_{0} \circ f$.

By Besson-Courtois-Gallot's Theorem 5.1, $\Omega$ is a closed $\pi_{1}(Z)$-invariant $n$-form on $L_{+}^{2}$. When $\Omega$ is restricted to $S_{+}^{\infty}$, it calibrates the immersion $\Phi_{0}$. $H^{*} \Omega$ is a closed $\pi_{1}(M)$-invariant $n$-form on $\widetilde{M} \times[0,1]$. It therefore descends to a closed $n$-form on $M \times[0,1]$. Moreover,
$$\left.H^{*} \Omega\right|_{\widetilde{M} \times\{0\}}=\Phi_{c}^{b *} \Omega \quad \text { and }\left.\quad H^{*} \Omega\right|_{\widetilde{M} \times\{1\}}=\left(\Phi_{0} \circ f\right)^{*} \Omega$$
At this stage, we would like to apply Stokes' Theorem to the closed form $H^{*} \Omega$ on $M \times[0,1]$. As $M$ is not compact, we are instead forced to apply Stokes' Theorem repeatedly to the compact exhaustion $M_{i} \times[0,1] \subset M_{i+1} \times[0,1] \subset \ldots \subset M \times[0,1]$, and then prove the resulting error terms go to zero. This will now be carried out.

Define the sequence of submanifolds $L_{i}:=\partial M_{i} \subset M$. We may now apply Stokes' Theorem to the closed form $H^{*} \Omega$ restricted to $M_{i} \times[0,1]$. This yields
$$\int_{M_{i}} \Phi_{c}^{b^{*}} \Omega-\int_{M_{i}}\left(\Phi_{0} \circ f\right)^{*} \Omega= \pm \int_{L_{i} \times[0,1]} H^{*} \Omega$$

Proposition 7.3.
$$\lim _{i \rightarrow \infty}\left|\int_{L_{i} \times[0,1]} H^{*} \Omega\right|=0$$

Proof: Put the product Riemannian metric $b \times(1)$ on $M \times[0,1]$. $\Phi_{c}^{b}$ and $\Phi_{0} \circ f$ have their images in positive functions of unit norm in Hilbert space. By projecting any pair of points in the image to the plane they span, it follows that the image of the straight line homotopy $H$ lies in the complement of the ball $B_{L^{2}}(0, .5)$ of radius . 5 in $L^{2}(\partial \widetilde{Z})$. By Lemma 5.2, the comass of $\Omega$ is uniformly bounded on the subset $L_{+}^{2}-B_{L^{2}}(0, .5)$. By Lemma 7.2, the $(n-1)$-dimensional $b$-volume of the slices $L_{i}$ goes to zero. Therefore to prove the proposition it suffices to show that the restricted map
$$\left.H\right|_{L_{i} \times[0,1]}:\left(L_{i} \times[0,1], b \times(1)\right) \longrightarrow L_{+}^{2}-B_{L^{2}}(0, .5)$$
is uniformly Lipschitz for all $i$. By the estimates of Section 6, at any $(x, t) \in$ $M \times[0,1]$ we have the inequalities
$$\left\|d H^{t}(v)\right\|^{2} \leq\left\|d \Phi_{c}^{b}(v)\right\|^{2}+\left\|d\left(\Phi_{0} \circ f\right)(v)\right\|^{2} \quad \text { and } \quad\left\|\frac{\partial}{\partial \tau} H\right\|^{2} \leq 2$$
where $v \in T_{x} M$ and $\frac{\partial}{\partial \tau}$ is a unit basis of $T_{t}[0,1]$. From inequality (4) of Section 4 we have
$$\left\|d \Phi_{c}^{b}(v)\right\|^{2} \leq \frac{c^{2}}{4} b(v, v) \quad \text { and } \quad\left\|d\left(\Phi_{0} \circ f\right)(v)\right\|^{2}=\frac{h\left(g_{0}\right)^{2}}{4 n} g_{0}(d f(v), d f(v)) .$$
The restricted map $f:\left(L_{i}, b\right) \longrightarrow\left(Z, g_{0}\right)$ is 1-Lipschitz by Lemma 7.2. If $(x, t) \in$ $L_{i} \times[0,1]$ and $w \in T_{x} L_{i}$ then $g_{0}(d f(w), d f(w)) \leq b(w, w)$. This implies that
$$\left\|d H^{t}(w)\right\|^{2} \leq \frac{c^{2}+h\left(g_{0}\right)^{2}}{4} b(w, w),$$
Therefore $\left.H\right|_{L_{i} \times[0,1]}$ is $\left(\frac{c^{2}+h\left(g_{0}\right)^{2}}{4}+2\right)^{1 / 2}$-Lipschitz, where the "+2" comes from the $\frac{\partial}{\partial \tau}$ direction. \(\square\)

Proposition 7.3 immediately implies
$$\int_{M} \Phi_{c}^{b^{*}} \Omega-\int_{M}\left(\Phi_{0} \circ f\right)^{*} \Omega=\lim _{i \rightarrow \infty}\left[\int_{M_{i}} \Phi_{c}^{b^{*}} \Omega-\int_{M_{i}}\left(\Phi_{0} \circ f\right)^{*} \Omega\right]=0 .$$
Recall that by Theorem 5.1 the closed $n$-form $\Omega$ restricted to $S_{+}^{\infty}$ calibrates the immersion $\Phi_{0}$. Combining this with inequality (5) and equation (6) of Section 5 yields
$$\begin{aligned}
\operatorname{comass}\left(\left.\Omega\right|_{S_{+}^{\infty}}\right) \cdot \operatorname{Vol}\left(\Phi_{c}^{b}\right) & \geq \int_{M} \Phi_{c}^{b^{*}} \Omega=\int_{M}\left(\Phi_{0} \circ f\right)^{*} \Omega \\
& =\operatorname{deg}(f) \cdot \int_{Z} \Phi_{0}^{*} \Omega=\operatorname{deg}(f) \cdot \operatorname{comass}\left(\left.\Omega\right|_{S_{+}^{\infty}}\right) \cdot \operatorname{Vol}\left(\Phi_{0}\right)
\end{aligned}$$
From Section 4 we know
$$\left(\frac{c^{2}}{4 n}\right)^{n / 2} \operatorname{Vol}(M, b) \geq \operatorname{Vol}\left(\Phi_{c}^{b}\right) \text { and } \operatorname{Vol}\left(\Phi_{0}\right)=\left(\frac{h\left(g_{0}\right)^{2}}{4 n}\right)^{n / 2} \operatorname{Vol}\left(Z, g_{0}\right) .$$
This proves that for all $c>h(b)$,
$$\left(\frac{c^{2}}{4 n}\right)^{n / 2} \operatorname{Vol}(M, b) \geq \operatorname{deg}(f)\left(\frac{h\left(g_{0}\right)^{2}}{4 n}\right)^{n / 2} \operatorname{Vol}\left(Z, g_{0}\right) .$$
Taking $c \searrow h(b)$ yields the desired inequality, namely
$$h(b)^{n} \operatorname{Vol}(M, b) \geq \operatorname{deg}(f) h\left(g_{0}\right)^{n} \operatorname{Vol}\left(Z, g_{0}\right) .$$
This completes the proof of Theorem 7.1

\section*{8. Cones in negatively curved manifolds}

This section will recall some elementary facts about cones in negatively curved Riemannian manifolds. These facts will be used in Section 9.

Let $\left(\widetilde{Z}, g_{0}\right)$ be a simply connected $n$-dimensional symmetric space with curvature at most -1 . (Everything in this section remains true for $\widetilde{Z}$ any simply connected Riemannian manifold with curvature at most -1 .) Let $N$ be a smooth $(n-1)$ -dimensional manifold. Let $g$ be a Riemannian metric on the smooth product $N \times$
$[0, \varepsilon)$. (The metric $g$ is neither necessarily complete nor a product metric.) Let $\phi: N \longrightarrow \widetilde{Z}$ be a locally Lipschitz map, where $N$ inherits a Riemannian metric as a submanifold of $(Y \times[0, \varepsilon), g)$. Let $\theta$ be a point on the boundary at infinity of $\widetilde{Z}$.

With this notation we can define the cone
$$\mathcal{C}: N \times[0, \varepsilon) \longrightarrow \widetilde{Z}$$
by sending $(x, s) \in N \times[0, \varepsilon)$ to the point at distance $\tan \left(\frac{s \pi}{2 \varepsilon}\right)$ along the geodesic ray from $\phi(y)$ to $\theta$.

The following elementary lemma is a standard fact whose proof we include for completeness.

Lemma 8.1. For any measurable subset $U \subseteq N$ we have the inequality
$$\int_{U \times[0, \varepsilon)}|J a c \mathcal{C}| d v o l_{g} \leq \frac{1}{n-1} \int_{U}|J a c \phi| d v o l_{g} .$$
Recall that $\phi$ and $\mathcal{C}$ are locally Lipschitz, implying by Rademacher's theorem that they are differentiable almost everywhere.

Proof: By the change of variables theorem, the value of the integrals in inequality (7) are independent of the coordinate system and the Riemannian metric $g$ on $N \times[0, \varepsilon)$. So without a loss of generality we are free to make the following changes. First, we will work on the diffeomorphic manifold $N \times[0, \infty)$, where $\mathcal{C}(x, s)$ is redefined to be the point at distance $s$ along the geodesic from $\phi(x)$ to $\theta$. Second, we will use $g$ to denote a fixed Riemannian metric $g$ on $N$. Finally, we equip $N \times[0, \infty)$ with the product metric $g \times(1)$.

At each point where $d \phi$ is injective choose a basis $\left\{v_{1}, v_{2}, \ldots, v_{n-1}\right\}$ for $T_{x} N$ such that the set of vectors $\left\{d \phi\left(v_{1}\right), \ldots, d \phi\left(v_{n-1}\right)\right\}$ are orthonormal in $T_{\phi(x)} \widetilde{Z}$. (The regularity of the resulting vector field is not important.) Extend each $v_{i}$ to the vector field $V_{i}:=\left(v_{i}, 0\right)$ on $N \times[0, \infty)$.

For a smooth path $\alpha$ in $N$ such that $\alpha(0)=x$ and $\alpha^{\prime}(0)=v_{i}$, the surface
$$(t, s) \longmapsto \mathcal{C}(\alpha(t), s)$$
describes a 1-parameter family of geodesics in $\widetilde{Z}$. Therefore the vector field $d \mathcal{C}_{(x, s)}\left(V_{i}\right)$ is a Jacobi field along the geodesic
$$s \longmapsto \mathcal{C}(\alpha(0), s) .$$

Let $\pi: T \widetilde{Z} \longrightarrow T \widetilde{Z}$ map a vector in $T_{z} \widetilde{Z}$ to its component orthogonal to the geodesic from $z$ to $\theta \in \partial \widetilde{Z}$. As the curvature of $\widetilde{Z}$ is bounded above by -1, the Rauch comparison theorem tells us that
$$\left\|(\pi \circ d \mathcal{C})\left(V_{i}\right)\right\|_{\mathcal{C}(x, s)} \leq e^{-s} \cdot\left\|(\pi \circ d \phi)\left(v_{i}\right)\right\|_{\phi(x)} \leq e^{-s} .$$
Recall here that $s$ is by definition the distance from $\phi(x)=\mathcal{C}(x, 0)$ to $\mathcal{C}(x, s)$.
At points $x \in N$ where $d \phi$ is injective, we obtain the estimate
$$\begin{aligned}
& \left\|d \mathcal{C}\left(V_{1}\right) \wedge \ldots \wedge d \mathcal{C}\left(V_{n-1}\right) \wedge d \mathcal{C}\left(\partial_{s}\right)\right\|_{\mathcal{C}(x, s)} \\
& \quad=\left\|(\pi \circ d \mathcal{C})\left(V_{1}\right) \wedge \ldots \wedge(\pi \circ d \mathcal{C})\left(V_{n-1}\right) \wedge d \mathcal{C}\left(\partial_{s}\right)\right\|_{\mathcal{C}(x, s)} \\
& \quad \leq e^{-(n-1) s} \cdot\left\|d \mathcal{C}\left(\partial_{s}\right)\right\|_{\mathcal{C}(x, s)} \\
& \quad=e^{-(n-1) s} \cdot\left\|d \phi\left(v_{1}\right) \wedge \ldots \wedge d \phi\left(v_{n-1}\right)\right\|_{\phi(x)}
\end{aligned}$$

Here the first equation comes from the fact that $d \mathcal{C}\left(\partial_{s}\right)$ is orthogonal to the image of $\pi$. The final equation uses the fact that $d \mathcal{C}\left(\partial_{s}\right)$ is a unit vector and the identity $\left\|d \phi\left(v_{1}\right) \wedge \ldots \wedge d \phi\left(v_{n}\right)\right\|_{\phi(x)}=1$.

Since $g \times(1)$ is a product metric on $N \times[0, \infty)$, we obtain the equation
$$\left\|V_{1} \wedge \ldots \wedge V_{n-1} \wedge \partial_{s}\right\|_{(x, s)}=\left\|v_{1} \wedge \ldots \wedge v_{n-1}\right\|_{x} .$$
This fact yields the following inequality for all $x$ where $d \phi$ is injective.
$$\begin{aligned}
|\operatorname{Jac} \mathcal{C}(x, s)| & =\frac{\left\|d \mathcal{C}\left(V_{1}\right) \wedge \ldots \wedge d \mathcal{C}\left(V_{n-1}\right) \wedge d \mathcal{C}\left(\partial_{s}\right)\right\|_{\mathcal{C}(x, s)}}{\left\|V_{1} \wedge \ldots \wedge V_{n-1} \wedge \partial_{s}\right\|_{(x, s)}} \\
& \leq e^{-(n-1) s} \cdot \frac{\left\|d \phi\left(v_{1}\right) \wedge \ldots \wedge d \phi\left(v_{n-1}\right)\right\|_{\phi(x)}}{\left\|v_{1} \wedge \ldots \wedge v_{n-1}\right\|_{x}} \\
& =e^{-(n-1) s} \cdot|\operatorname{Jac} \phi(x)|
\end{aligned}$$
So finally we obtain the desired estimate
$$\begin{aligned}
\int_{U \times[0, \infty)}|\operatorname{Jac} \mathcal{C}| d \operatorname{vol}_{g \times(1)} & \leq \int_{0}^{\infty} \int_{U} e^{-(n-1) s} \cdot|\operatorname{Jac} \phi(x)| d \operatorname{vol}_{g}(x) d s \\
& =\left[\int_{0}^{\infty} e^{-(n-1) s} d s\right] \cdot\left[\int_{U}|\operatorname{Jac} \phi| d \operatorname{vol}_{g}\right] \\
& =\frac{1}{n-1} \int_{U}|\operatorname{Jac} \phi| d \operatorname{vol}_{g}
\end{aligned}$$ \(\square\)

We now describe an extension of Lemma 8.1 to the case of some negatively curved manifolds with nilpotent fundamental group. Let $P$ be a group of isometries of $\widetilde{Z}$ which fixes $\theta \in \partial \widetilde{Z}$. Suppose we are given a locally Lipschitz map $\phi: N \longrightarrow \widetilde{Z} / P$. Let $\widetilde{N}$ denote the universal cover of $N$, and let $\widetilde{\phi}: \widetilde{N} \longrightarrow \widetilde{Z}$ denote the lift of $\phi$. Notice that the cone
$$\mathcal{C}: \tilde{N} \times[0, \varepsilon) \longrightarrow \widetilde{Z}$$
is equivariant with respect to the actions of $\pi_{1}(N)$ on $\widetilde{N} \times[0, \varepsilon)$ and $P$ on $\widetilde{Z}$. So the "downstairs" cone
$$\mathcal{C}: N \times[0, \varepsilon) \longrightarrow \widetilde{Z} / P$$
is well defined. By applying Lemma 8.1 to a fundamental domain for $N$ in $\widetilde{N}$, we obtain the following corollary.

Corollary 8.2. For any Riemannian metric $g$ on $N \times[0, \varepsilon)$ we have the inequality
$$\int_{N \times[0, \varepsilon)}|J a c \mathcal{C}| d v o l_{g} \leq \frac{1}{n-1} \int_{N}|J a c \phi| d v o l_{g}$$

\section*{9. The equality case}

The goal of this section is to prove
Theorem 9.1. For $n \geq 3$, let $(M, b)$ be a finite volume oriented Riemannian $n$ manifold. Let $\left(Z, g_{0}\right)$ be an $n$-dimensional oriented finite volume negatively curved
locally symmetric space. If $f: M \longrightarrow Z$ is a proper orientation preserving map of nonzero degree and
$$h(b)^{n} \operatorname{Vol}(M, b)=\operatorname{deg}(f) h\left(g_{0}\right)^{n} \operatorname{Vol}\left(Z, g_{0}\right),$$
then $f$ is proper homotopic to a homothetic covering map.
Since the quantities $h(b)^{n} \operatorname{Vol}(M, b)$ and $h\left(g_{0}\right)^{n} \operatorname{Vol}\left(Z, g_{0}\right)$ are scale invariant, we may assume without a loss of generality that the curvature of $g_{0}$ is bounded above by -1 , and $\operatorname{Vol}(M, b)=\operatorname{deg}(f) \operatorname{Vol}\left(Z, g_{0}\right)$. This implies $h:=h(b)=h\left(g_{0}\right)$. For $c>h$, define the map
$$\begin{aligned}
F_{c}:(M, b) & \longrightarrow\left(Z, g_{0}\right) \\
x & \longmapsto \operatorname{bar} \circ \Phi_{c}^{b}(x) .
\end{aligned}$$
This map is $\pi_{1}$-equivariant with respect to the homomorphism $f_{*}: \pi_{1}(M) \longrightarrow$ $\pi_{1}(Z)$. Thus the straight line homotopy from $f: \widetilde{M} \longrightarrow \widetilde{Z}$ to $F_{c}: \widetilde{M} \longrightarrow \widetilde{Z}$ is similarly equivariant, and descends to a homotopy between the maps $f, F_{c}: M \longrightarrow$ $Z$.

Lemma 9.2. For all $x \in M$, $\operatorname{Jac} F_{c}(x) \leq(c / h)^{n}$. Moreover, $\left(\operatorname{Jac} F_{c}\right) \longrightarrow 1$ in $L^{1}\left(M\right.$, dvol $\left._{b}\right)$ (and thus almost everywhere) as $c \searrow h$.

Proof: Pick $x \in M$ and a positively oriented basis $\left\{v_{1}, \ldots, v_{n}\right\} \subset T_{x} M$. Let $d \operatorname{vol}_{b}$ (resp. $d \operatorname{vol}_{g_{0}}$ ) be the volume form of $(M, b)$ (resp. $\left(Z, g_{0}\right)$ ). Then
$$\begin{aligned}
\operatorname{Jac}_{c} \cdot d \operatorname{vol}_{b}\left(v_{1}, \ldots v_{n}\right) & =d \operatorname{vol}_{g_{0}}\left(d F_{c}\left(v_{1}\right), \ldots, d F_{c}\left(v_{n}\right)\right) \\
& =\Omega\left(d \Phi_{c}^{b}\left(v_{1}\right), \ldots, d \Phi_{c}^{b}\left(v_{n}\right)\right) \\
& \leq\left(\frac{4 n}{h^{2}}\right)^{n / 2}\left(\operatorname{det}\left(\left\langle d \Phi_{c}^{b}\left(v_{i}\right), d \Phi_{c}^{b}\left(v_{j}\right)\right\rangle_{L^{2}}\right)_{i j}\right)^{1 / 2} \quad(\text { Thm. } \\
& \leq\left(\frac{4 n}{h^{2}}\right)^{n / 2}\left(\frac{c^{2}}{4 n}\right)^{n / 2} d \operatorname{vol}_{b}\left(v_{1}, \ldots, v_{n}\right) \quad \text { (Lemma 4.2) } \\
& =\left(\frac{c}{h}\right)^{n} d \operatorname{vol}_{b}\left(v_{1}, \ldots, v_{n}\right) .
\end{aligned}$$
By the inequalities at the end of Section 7, and the hypotheses of Theorem 9.1 it follows that
$$\begin{aligned}
\int_{M} \mathrm{Jac} F_{c} d \mathrm{vol}_{b}=\int_{M}\left(\Phi_{c}^{b}\right)^{*} \Omega & \leq\left(\frac{4 n}{h^{2}}\right)^{n / 2} \cdot \operatorname{Vol}\left(\Phi_{c}^{b}\right) \\
& \leq\left(\frac{4 n}{h^{2}}\right)^{n / 2} \cdot\left(\frac{c^{2}}{4 n}\right)^{n / 2} \cdot \operatorname{Vol}(M, b) \\
& =\left(\frac{c}{h}\right)^{n} \cdot \operatorname{deg}(f) \cdot \operatorname{Vol}\left(Z, g_{0}\right) \\
& =\left(\frac{c}{h}\right)^{n} \cdot \operatorname{deg}(f) \cdot\left(\frac{4 n}{h^{2}}\right)^{n / 2} \cdot \operatorname{Vol}\left(\Phi_{0}\right) \\
& =\left(\frac{c}{h}\right)^{n} \cdot \operatorname{deg}(f) \cdot \int_{Z} \Phi_{0}^{*} \Omega \\
& =\left(\frac{c}{h}\right)^{n} \cdot \int_{M}\left(\Phi_{0} \circ f\right)^{*} \Omega=\left(\frac{c}{h}\right)^{n} \cdot \int_{M}\left(\Phi_{c}^{b}\right)^{*} \Omega
\end{aligned}$$

From these inequalities we can conclude that
$$\int_{M} \operatorname{Jac} F_{c} d \operatorname{vol}_{b} \longrightarrow \operatorname{Vol}(M, b)=\int_{M} 1 d \operatorname{vol}_{b} .$$
This limit and the fact that $\operatorname{Jac} F_{c} \leq(c / h)^{n}$ together imply that $\left(\operatorname{Jac} F_{c}\right) \longrightarrow 1$ in $L^{1}\left(M, d \mathrm{vol}_{b}\right)$. \(\square\)

We will now work with the lifted maps $F_{c}: \widetilde{M} \longrightarrow \widetilde{Z}$. Pick a point $p \in \widetilde{M}$. For $\delta>0$ sufficiently small, let $B_{p}$ be a convex $b$-metric ball of $b$-radius $\delta$ about $p$. By reproducing the arguments of Lemmata 7.4 and 7.5 of [2], one can show that the restricted maps $\left.F_{c}\right|_{B_{p}}$ are uniformly $L$-Lipschitz for $c-h$ sufficiently small, where $L$ is independent of $p$. (To apply the argument of [2, Lem.7.5] directly, it is necessary to restrict to a small ball. $(\widetilde{M}, b)$ may not be uniformly Ahlfors regular, i.e. there may be a sequence of metric balls in $(\widetilde{M}, b)$ of fixed radius with volume going to zero. Without uniform Ahlfors regularity the proof of [2, Lem.7.5] is not immediately valid for all of $(\widetilde{M}, b)$. Working locally is one way to circumvent this problem.)

Recall that $\left(\widetilde{Z}, g_{0}\right)$ has a basepoint $o \in \widetilde{Z}$. Then for each $c>h$ pick $g_{c} \in$ $\operatorname{Isom}^{+}\left(\widetilde{Z}, g_{0}\right)$ such that $\left.g_{c} \circ F_{c}\right|_{B_{p}}(p)=o$. By the Arzela-Ascoli theorem, there is a sequence $c_{i} \searrow h$ and an $L$-Lipschitz map $F^{p}:\left(B_{p}, p\right) \longrightarrow(\widetilde{Z}, o)$ such that $\left.g_{c} \circ F_{c_{i}}\right|_{B_{p}}$ converges uniformly to $F^{p}$. By the arguments of Lemmas 7.7 and 7.8 of [2], $F^{p}$ is in fact 1-Lipschitz.

Pick a sequence of points $\left\{p_{i}\right\} \subset \widetilde{M}$ such that the neighborhoods $B_{p_{i}}$ form a locally finite cover of $\widetilde{M}$. Using a diagonalization argument, we may piece together the locally defined maps $F^{p_{i}}$ to prove

Lemma 9.3. There is a sequence $c_{j} \searrow h$ with the following property: for any precompact open set $\mathcal{O} \subset \widetilde{M}$, and any $\varepsilon>0$, there is a $J>0$ such that $j>J$ implies that the restricted maps $F_{c_{j}}:(\mathcal{O}, b) \longrightarrow\left(\widetilde{Z}, g_{0}\right)$ are L-Lipschitz maps satisfying the inequality
$$d_{g_{0}}\left(F_{c_{j}}(x), F_{c_{j}}(y)\right) \leq d_{b}(x, y)+\varepsilon \quad \text { for any } \quad x, y \in \mathcal{O} .$$

In order to apply the Arzela-Ascoli theorem to the family of maps $\left\{F_{c_{j}}\right\}_{j}$, we must first show that the maps $F_{c_{j}}:(M, b) \longrightarrow\left(Z, g_{0}\right)$ do not leave every compact set of $Z$.

Lemma 9.4. Pick a point $q \in M$. The points $\left\{F_{c_{j}}(q)\right\}_{j} \subset Z$ are contained in a compact subset of $Z$.

Proof: The map $f: M \longrightarrow Z$ is a proper map of finite degree. A covering space argument shows that the image group $f_{*}\left(\pi_{1}(M)\right) \leq \pi_{1}(Z)$ must be of finite index. The group $f_{*}\left(\pi_{1}(M)\right)$ is therefore finitely generated. This implies the existence of a compact submanifold $C$ of $M$ containing $q$ such that the induced map
$$\left(\left.f\right|_{C}\right)_{*}: \pi_{1}(C) \longrightarrow f_{*}\left(\pi_{1}(M)\right)$$
is surjective.
Suppose that after passing to a subsequence the points $F_{c_{j}}(q)$ leave every compact subset of $M$. Then for large $j$, Lemma 9.3 implies that $F_{c_{j}}$ maps all of $C$ into a cusp of $\left(Z, g_{0}\right)$. This implies that the image of the homomorphism
$$\left(\left.F_{c_{j}}\right|_{C}\right)_{*}: \pi_{1}(C) \longrightarrow \pi_{1}(Z)$$
is a subgroup of infinite index. But $F_{c_{j}}$ is homotopic to $f$, implying that
$$\left(\left.F_{c_{j}}\right|_{C}\right)_{*}\left(\pi_{1}(C)\right)=\left(\left.f\right|_{C}\right)_{*}\left(\pi_{1}(C)\right)=f_{*}\left(\pi_{1}(M)\right) .$$
This is a contradiction. \(\square\)

We may now apply the Arzela-Ascoli theorem to conclude that, after passing to a subsequence, the maps $\left\{F_{c_{j}}:(M, b) \longrightarrow\left(Z, g_{0}\right)\right\}$ converge uniformly on compact sets to a 1-Lipschitz map $F:(M, b) \longrightarrow\left(Z, g_{0}\right)$ given locally by the maps $F^{p}$ : $\left(B_{p}, p\right) \longrightarrow(\widetilde{Z}, o)$ described above. The final and most important step of the argument is to the following proposition.

Proposition 9.5. Jac $F=1$ almost everywhere.
Proof: Since $F$ is 1 -Lipschitz, we know that $|\operatorname{Jac} F| \leq 1$ almost everywhere. In search of a contradiction, let us suppose that $\mathrm{Jac} F<1$ on a set of strictly positive measure. Then there is a $\gamma>0$ and a compact submanifold $K \subset M$ such that
$$\left(\int_{K} d \mathrm{vol}_{b}\right)-\left(\int_{K} \operatorname{Jac} F d \mathrm{vol}_{b}\right)>\gamma .$$
(The letter $\gamma$ stands for "gap.")
Let us recall some notation from Section 7. $M$ has a compact exhaustion $\left\{M_{i}\right\}$, $L_{i}:=\partial M_{i}$, and $\operatorname{Vol}\left(L_{i}\right) \longrightarrow 0$. Outside of a compact submanifold, $Z$ splits into the smooth product $Y \times[0, \infty)$, where each component of a slice $Y \times\{t\}$ is the quotient of a horosphere in $\widetilde{Z}$. (Keep in mind that neither $L_{i}$ nor $Y$ is necessarily connected.)

Fix $i$ sufficiently large such that
$$f\left(L_{i}\right) \subset Y \times[0, \infty) \subset Z, \quad K \subset M_{i}, \quad \text { and } \operatorname{Vol}\left(L_{i}\right)<\frac{\gamma}{2} .$$
The following lemma is an exercise in degree theory whose proof is left to the reader.
Lemma 9.6. $f_{*}\left[L_{i}\right]=\operatorname{deg}(f) \cdot[Y] \in H_{n-1}(Y \times[0, \infty))$.
For each component $Y^{\prime}$ of $Y$ there is a Riemannian covering space of $Z$ corresponding to $\pi_{1}\left(Y^{\prime}\right)<\pi_{1}(Z)$. Take the disjoint union of these covering spaces, one for each component of $Y$, and call the resulting covering space $\hat{Z}$. Let $\pi: \hat{Z} \longrightarrow Z$ denote the locally isometric covering map. Note that $\hat{Z}$ is diffeomorphic to $Y \times \mathbb{R}$, and each component of $\hat{Z}$ is a quotient of the symmetric space $\widetilde{Z}$ by a group of isometries with a global fixed point in the boundary at infinity $\partial \widetilde{Z}$.

We chose $i$ so that $f\left(L_{i}\right) \subset Y \times[0, \infty) \subset Z$. Therefore the restriction $\left.f\right|_{L_{i}}$ lifts to a map $\widehat{\left.f\right|_{L_{i}}}: L_{i} \longrightarrow \hat{Z}$. The map $F$ is homotopic to $f$, so in particular the restriction $\left.F\right|_{L_{i}}$ also lifts to a map $\widehat{\left.F\right|_{L_{i}}}: L_{i} \longrightarrow \hat{Z}$.

Let $L_{i} \times(-\varepsilon, \varepsilon) \subset M$ be a tubular neighborhood of $L_{i}$, oriented so that $L_{i} \times$ $\{-\varepsilon / 2\} \subset M_{i}$. Following the notation of Section 8, we define the cone of $\widehat{\left.F\right|_{L_{i}}}$
$$\mathcal{C}: L_{i} \times[0, \varepsilon) \longrightarrow \hat{Z}$$
as follows. For each point $p=\widehat{\left.F\right|_{L_{i}}}(x) \in \hat{Z}$ there is a unique geodesic ray beginning at $p$ which escapes down a finite volume end of $\hat{Z}$. Define $\mathcal{C}(x, s)$ as the point at distance $\tan \left(\frac{s \pi}{2 \varepsilon}\right)$ along this ray. Then by Corollary 8.2 we have the inequality
$$\left.\int_{L_{i} \times[0, \varepsilon)}|\operatorname{Jac} \mathcal{C}| d \operatorname{vol}_{b} \leq \frac{1}{n-1} \int_{L_{i}}|\operatorname{Jac} F|_{L_{i}} \right\rvert\, d \operatorname{vol}_{b} \leq \operatorname{Vol}\left(L_{i}\right),$$

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/de166888-0057-4e8e-8376-f64b86f5fa53-16.jpg?height=1063&width=1027&top_left_y=425&top_left_x=580}
\captionsetup{labelformat=empty}
\caption{Figure 1. A pictorial summary of the notation.}
\end{figure}
where the final inequality comes from the fact that $\left.F\right|_{L_{i}}$ is 1-Lipschitz.
Fix $\tau>0$ such that $\operatorname{Vol}(Y \times[\tau, \infty))<\frac{\gamma}{2} \cdot \operatorname{deg}(f)$. Fix $\delta \in(0, \varepsilon)$ such that
$$(\pi \circ \mathcal{C})\left(L_{i} \times\{\delta\}\right) \subset Y \times(\tau, \infty) \subset Z .$$
Define the compact submanifold $M_{i}^{\text {th }}:=M_{i} \cup\left(L_{i} \times[0, \delta]\right)$. (The letters th stand for "thickening.") Define the compact manifold $Z_{\tau}$ as the complement of $Y \times(\tau, \infty) \subset$ $Z$. Define the piecewise smooth map $p: Z \longrightarrow Z$ as the identity on $Z_{\tau}$, and $p(y, t):=(y, \tau)$ for $(y, t) \in Y \times[\tau, \infty)$. Notice that the Jacobian of $p$ is either 0 or 1 almost everywhere. It is, in other words, a volume nonincreasing map (even though it is not globally Lipschitz). See Figure 1 for a summary of this notation.

With this notation, we are prepared to define $G: M_{i}^{\text {th }} \longrightarrow Z_{\tau}$ as follows: $G:=$ $p \circ F$ on $M_{i}$, and $G:=p \circ \pi \circ \mathcal{C}$ on $L_{i} \times[0, \delta]$. Note that $G$ is Lipschitz and boundary preserving. Let $\operatorname{deg}(G)$ denote the degree of $G$ as a boundary preserving map between compact manifolds.

Lemma 9.7. $\operatorname{deg}(G)=\operatorname{deg}(f)$.
Proof of Lemma 9.7: By Lemma 9.6, $f_{*}\left[L_{i}\right]=\operatorname{deg}(f) \cdot[Y] \in H_{n-1}(Y \times[0, \infty))$. A standard fact of degree theory is that the degree of a boundary preserving map between compact manifolds equals the degree of the boundary map. (This follows
from the long exact homology sequence.) In our notation, this implies the relation $G_{*}\left[L_{i} \times\{\delta\}\right]=\operatorname{deg}(G) \cdot\left[\partial Z_{\tau}\right] \in H_{n-1}\left(\partial Z_{\tau}\right)$.

It is easy to see the map $G: M_{i}^{\text {th }} \longrightarrow Z$ is homotopic to the restriction of $f$ to $M_{i}^{\text {th }}$. This implies the relation
$$G_{*}\left[L_{i} \times\{\delta\}\right]=f_{*}\left[L_{i} \times\{\delta\}\right]=\operatorname{deg}(f) \cdot[Y] \in H_{n-1}(Y \times[0, \infty)),$$
where the restriction $\left.G\right|_{L_{i} \times\{\delta\}}$ is viewed as a map into $Y \times[0, \infty)$. The proof of this lemma is completed by the commutative diagram
![](https://cdn.mathpix.com/cropped/de166888-0057-4e8e-8376-f64b86f5fa53-17.jpg?height=198&width=896&top_left_y=782&top_left_x=612)
where the lower-right arrow is the isomorphism induced by inclusion. \(\square\)

Consider the following estimate, with explanations below.
$$\begin{aligned}
\operatorname{Vol}\left(Z_{\tau}\right) & =\operatorname{deg}(G) \int_{M_{i}^{\mathrm{th}}} \operatorname{Jac} G d \operatorname{vol}_{b} \\
& =\operatorname{deg}(f) \int_{M_{i}} \operatorname{Jac}(p \circ F) d \operatorname{vol}_{b}+\operatorname{deg}(f) \int_{L_{i} \times[0, \delta]} \operatorname{Jac}(p \circ \pi \circ \mathcal{C}) d \operatorname{vol}_{b} \\
& <\operatorname{deg}(f) \cdot\left(\operatorname{Vol}\left(M_{i}\right)-\gamma\right)+\operatorname{deg}(f) \int_{L_{i} \times[0, \delta]}|\operatorname{Jac} \mathcal{C}| d \operatorname{vol}_{b} \\
& <\operatorname{deg}(f) \cdot \operatorname{Vol}(M)-\operatorname{deg}(f) \cdot \gamma+\operatorname{deg}(f) \cdot \operatorname{Vol}\left(L_{i}\right) \\
& <\operatorname{Vol}(Z)-\frac{\gamma}{2} \cdot \operatorname{deg}(f)
\end{aligned}$$
The first line is the degree formula for a boundary preserving Lipschitz map between compact smooth manifolds. (Such a degree formula can be proved either by smooth approximation or by using [4, Lem.4.1.25].) The second line uses Lemma 9.7 and the definition of $G$. The third line uses the fact that $p: Z \longrightarrow Z$ is volume nonincreasing, inequality (8), and the fact that $\pi: \hat{Z} \longrightarrow Z$ is a local isometry. The fourth line uses inequality (9). The fifth line uses our choice of $i$ sufficiently large so that the volume of $L_{i}$ is less than $\frac{\gamma}{2}$.

Recall that we chose $\tau$ so that $\operatorname{Vol}(Z)<\operatorname{Vol}\left(Z_{\tau}\right)+\frac{\gamma}{2} \cdot \operatorname{deg}(f)$. This fact combined with the above string of inequalities yields a contradiction. Therefore there does not exist a set of positive measure on which $\operatorname{Jac} F<1$. This completes the proof of the proposition. \(\square\)

We have now proven that $F:(M, b) \longrightarrow\left(Z, g_{0}\right)$ is a 1-Lipschitz map such that $\operatorname{Jac} F=1$ almost everywhere. We may now apply Theorem 3.1 to conclude that $F$ is a local homeomorphism and a local isometry. This implies that $(M, b)$ is a finite volume negatively curved locally symmetric space. Since $F$ is 1-Lipschitz, it must take the cusps of $(M, b)$ out the cusps of $\left(Z, g_{0}\right)$. Therefore $F$ is proper. A proper local homeomorphism is a covering map. So we may conclude that $F:(M, b) \longrightarrow$ $\left(Z, g_{0}\right)$ is a locally isometric covering map.

It remains only to show that the straight line homotopy from $f$ to $F$ is proper. For this it suffices to show that an end $(M, b)$ (which we now know to be a rank
one cusp) is mapped to the same cusp of $\left(Z, g_{0}\right)$ under both $f$ and $F$. Suppose this is false. Then there is an essential closed curve $\gamma$ in a cusp of $(M, b)$ which is mapped into different cusps of $\left(Z, g_{0}\right)$ under $f$ and $F$. The homomorphism
$$f_{*}=F_{*}: \pi_{1}(M) \longrightarrow \pi_{1}(Z)$$
is injective. Therefore the closed curves $F(\gamma)$ and $f(\gamma)$ are essential and freely homotopic in $Z$. Since they lie in different cusps of $\left(Z, g_{0}\right)$, this violates the thickthin decomposition of a negatively curved locally symmetric space. This yields a contradiction. This concludes the proof of Theorem 9.1

\section*{References}
\begin{itemize}
\item[] [1] G. Besson, G. Courtois, and S. Gallot. Volume et entropie minimale des espaces localement symétriques. Invent. math., 103:417-445, 1991.
\item[] [2] G. Besson, G. Courtois, and S. Gallot. Entropies et rigidités des espaces localement symétriques de courbure strictement négative. Geom. Funct. Anal., 5(5):731-799, 1995.
\item[] [3] J. Boland, C. Connell, and J. Souto. Volume rigidity for finite volume manifolds. Amer. J. Math., 127(3):535-550, 2005.
\item[] [4] H. Federer. Geometric Measure Theory. Springer-Verlag, New York, 1969.
\item[] [5] R.E. Greene and H. Wu. $\mathcal{C}^{\infty}$ approximations of convex, subharmonic, and plurisubharmonic functions. Ann. Scient. Éc. Norm. Sup., $4^{e}$ série, 12:47-84, 1979.
\item[] [6] Yu. G. Reshetnyak. Space Mappings with Bounded Distortion, volume 73 of Transl. of Math. Monographs. Amer. Math. Soc., Providence, R.I., 1989.
\item[] [7] J. Souto. Geometric Structures on 3-Manifolds and their Deformations. Bonner mathematische schriften, Rheinischen-Friedrich-Wilhelms-Universität Bonn, 2001. Portions co-authored with J. Boland, C. Connell, and G. Kleineidam.
\end{itemize}
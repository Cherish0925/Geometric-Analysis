---
retention_scope: session
part: 1
total_parts: 2
---

[Part 1/2 of: On cohomogeneity one Hermitian non-Kähler metrics]

---
source_file: On_cohomogeneity_one_Hermitian_non-Kähler_metrics_59f47cb8bdaf.pdf
converter: mathpix
format: mmd
---

\title{
On cohomogeneity one Hermitian non-Kähler metrics
}

\author{
Daniele Angella and Francesco Pediconi \\ Dipartimento di Matematica e Informatica 'Ulisse Dini', Università degli Studi di Firenze, viale Morgagni 67/a, 50134 Firenze, Italy (daniele.angella@unifi.it, daniele.angella@gmail.com, francesco.pediconi@unifi.it)
}
(Received 13 July 2021; accepted 17 January 2022)

\begin{abstract}
We investigate the geometry of Hermitian manifolds endowed with a compact Lie group action by holomorphic isometries with principal orbits of codimension one. In particular, we focus on a special class of these manifolds constructed by following Bérard-Bergery which includes, among the others, the holomorphic line bundles on ${ }^{m-1}$, the linear Hopf manifolds and the Hirzebruch surfaces. We characterize their invariant special Hermitian metrics, such as balanced, Kähler-like, pluriclosed, locally conformally Kähler, Vaisman and Gauduchon. Furthermore, we construct new examples of cohomogeneity one Hermitian metrics solving the second-Chern-Einstein equation and the constant Chern-scalar curvature equation.
\end{abstract}

Keywords: Bérard-Bergery; Chern connection; cohomogeneity one; Hermite-Einstein; Hermitian manifold; Kähler-Einstein; non-Kähler

2020 Mathematics subject classification: Primary: 53C30; 53C21; 53C25; 53C55

\section*{1. Introduction}

One of the most useful ways to construct concrete examples of Einstein metrics is by considering Riemannian manifolds with a large symmetry group, for example, homogeneous spaces and manifolds of cohomogeneity one, see e.g. [10, 56, 57] and references therein. As another useful tool, the Calabi-Yau theorem assures the existence of Einstein metrics on compact complex Kähler manifolds with nonpositive first-Chern class [8, 59], and also the existence of Kähler-Einstein metrics on Fano manifolds has been recently understood.

The first non-homogeneous example of compact Riemannian Einstein manifold with positive scalar curvature has been provided by Page [45, 46] on $\mathbb{C P}^{2} \# \overline{\mathbb{C P}}^{2}$, and then generalized by Bérard-Bergery in [9] as follows. Let $P$ be a compact Kähler-Einstein manifold with positive scalar curvature [1, 34, 35], for example, $P=\mathbb{C P}^{1}$ in case of the Page example. Let the first-Chern class be $c_{1}(P)=p \alpha$, with $p>0$ integer and $\alpha \in H^{2}(P ; \mathbb{Z})$ indivisible. For $n>0$ integer, consider the line bundle $\mathbb{C} \rightarrow E_{n} \rightarrow P$ with $c_{1}\left(E_{n}\right)=n \alpha$, and the associated projective bundle $\mathbb{C P}^{1} \rightarrow M_{n} \rightarrow P$. Then one can use the theory of Riemannian submersion [43]

\footnotetext{
© The Author(s), 2022. Published by Cambridge University Press on behalf of The Royal Society of Edinburgh. This is an Open Access article, distributed under the terms of the Creative Commons Attribution licence (https://creativecommons.org/licenses/by/4.0/), which permits unrestricted re-use, distribution, and reproduction in any medium, provided the original work is properly cited.
}
to compute the Riemannian curvature of both $E_{n}$ and $M_{n}$. In particular, when $P=\mathrm{G} / \mathrm{K}$ is a Hermitian symmetric space, then $E_{n}$ and $M_{n}$ are cohomogeneity one, and by consequence their curvature is determined by the structure constants of the Lie algebra $\mathfrak{g}:=\operatorname{Lie}(\mathrm{G})$ and by the induced 1-parameter family of scalar products [9]. The Einstein equation is then reduced to a system of second-order ordinary differential equations (ODEs), in both the spaces $E_{n}$ and $M_{n}$, that can be integrated to get Einstein metrics which are also Hermitian, see [9, théorèmes 1.10 and 1.13].

In the complex setting, Kähler C-spaces (i.e. compact, simply-connected, homogeneous Kähler manifolds) are well understood [1, 12, 55]: in particular, they always admit a unique Kähler-Einstein metric, up to scaling. On the other hand, cohomogeneity one Kähler metrics have been studied in [4, 5, 17, 28, 35, 48-50].

In the Hermitian non-Kählerian context, since the Levi-Civita connection does not preserve the complex structure, one is led to introduce a more suitable notion of canonical metrics, for example, the second-Chern-Einstein condition. Here, by second-Chern-Einstein metric on a complex manifold, we mean a Hermitian metric on the tangent bundle that is Hermite-Einstein with respect to itself [22], see also [7, 51]. Examples of compact second-Chern-Einstein manifolds include the homogeneous Hopf surface [22, 24, 37], holomorphically parallelizable manifolds [11] and the homogeneous non-Kähler C-spaces studied by Podestà [47]; see also [2] for the almost-Kähler case. In particular, the only compact complex non-Kähler surface admitting second-Chern-Einstein metrics is the Hopf surface [24, theorem 2], see also [22]. Note that there still miss (if any) non-Kähler examples of second-Chern-Einstein metrics with negative Chern-scalar curvature on compact complex manifolds. Further problems, e.g. the constant Chern-scalar curvature problem, also known as Chern-Yamabe problem [6], are still not completely understood. Non-homogeneous examples of Hermitian metrics of positive constant Chern-scalar curvature on Hirzebruch surfaces, using the Page and Bérard-Bergery ansatz, have been constructed in [33].

In this note, motivated by the above questions, we start to investigate the curvature and the properties of Hermitian non-Kähler manifolds with large isometry groups. In particular, we focus on the Bérard-Bergery [9] standard [48] cohomogeneity one Hermitian manifolds $\left(M_{(i, n)}(\mathrm{G}, \mathrm{K}), \mathrm{J}, \mathrm{g}\right)$, with $i \in\{1,2,3,4\}$ and $n \in \mathbb{N}$, that are defined as (the total spaces of) bundles over a simply connected, irreducible, compact Hermitian symmetric space $P=\mathrm{G} / \mathrm{K}$, see definition 3.7. We compute the Chern-Ricci and Chern-scalar curvatures, see proposition 3.15. This is aimed at getting the second-Chern-Einstein and the constant Chern-scalar curvature equations, that we investigate in the last section. Here, we continue by describing the existence of special metrics.

Our first result concerns the locally conformally Kähler condition. We recall that a Hermitian metric g is called locally conformally Kähler if it admits a local conformal change to a Kähler metric [19], which is equivalent to say that $\mathrm{d} \omega=\frac{1}{m-1} \vartheta \wedge \omega$ with $\mathrm{d} \vartheta=0$, where $\omega=\mathrm{g}(\mathcal{J} \cdot, \cdot)$ is the fundamental 2-form associated with the metric, $m$ denotes the complex dimension and $\vartheta$ is the Lee form of $\mathbb{g}[\mathbf{2 3}]$, see § 3.3. In the particular case when $\vartheta$ is also exact, say $\vartheta=(m-1) \mathrm{d} \phi$, then $\exp (-\phi) \omega$ is Kähler, and $\mathbb{g}$ is called globally conformally Kähler (this includes the case $\vartheta=0$, corresponding to g itself being Kähler). When $\vartheta$ is not exact, we say that the metric is strictly locally conformally Kähler. Moreover, a strictly locally conformally Kähler
metric is called Vaisman if the Lee form $\vartheta$ is parallel with respect to the Levi-Civita connection.

It is worth noticing that homogeneous, strictly locally conformally Kähler metrics on compact manifolds are Vaisman [25, 29]. On the other hand, in the cohomogeneity one case, we prove the following.

Theorem A (see proposition 4.1, corollary 4.2 and proposition 4.3). Let $\left(M_{(i, n)}(\mathrm{G}, \mathrm{K}), \mathfrak{J}, \mathbb{g}\right)$ be one of the Bérard-Bergery standard cohomogeneity one Hermitian manifolds. Then, $g$ is locally conformally Kähler. Furthermore, $g$ is strictly locally conformally Kähler if and only if $\left(M_{(i, n)}(\mathrm{G}, \mathrm{K}), J_{)}\right.$is compact without singular orbits (case $i=3$ ) and, on such manifolds, $\mathbb{g}$ is Vaisman if and only if it is homogeneous.

Our second result concerns other kinds of special conditions for Hermitian metrics. To this regard, we recall that the balanced condition in the sense of Michelsohn [40] amounts to $\mathrm{d}^{*} \omega=0$. The pluriclosed condition, a.k.a. strong Kähler with torsion (SKT for short), means that $\mathrm{dd}^{c} \omega=0$. Moreover, the Gauduchon condition [21] refers to $\mathrm{d}^{*} \vartheta=0$, equivalently, $\mathrm{dd}^{c} \omega^{m-1}=0$.

Theorem B (see corollaries 4.7, 4.9 and proposition 4.6). Let $\left(M_{(i, n)}(\mathrm{G}, \mathrm{K}), ~ \mathbb{J}, \mathbb{g}\right)$ be one of the Bérard-Bergery standard cohomogeneity one Hermitian manifolds. The following three conditions are equivalent: $\mathbb{g}$ is pluriclosed, $\mathbb{g}$ is balanced, $\mathbb{g}$ is Kähler. Moreover, if $\left(M_{(i, n)}(\mathrm{G}, \mathrm{K}), \Downarrow\right)$ has singular orbits, then $\mathfrak{g}$ is Gauduchon if and only if it is Kähler.

Finally, we investigate the second-Chern-Einstein and the constant Chern-scalar curvature problems (see § 2.2) on this class of manifolds. Firstly, we prove a local existence and uniqueness result for second-Chern-Einstein metrics with prescribed Chern-scalar curvature (see theorem 5.1), by using a method due to Malgrange [39] already exploited by Eschenburg and Wang [20] and by Böhm [14, 15]. Then, concerning the existence of complete solutions to the second-Chern-Einstein equations, we prove the following.

Theorem C (see remark 5.2, theorem 5.3, proposition 5.5). Let $\left(M_{(i, n)}(\mathrm{G}, \mathrm{K})\right.$, J) be one of the Bérard-Bergery standard cohomogeneity one complex manifolds.
\begin{itemize}
\item[(a)] If $\left(M_{(i, n)}(\mathrm{G}, \mathrm{K})\right.$, J) has no singular orbits (cases $i=1$ and $i=3$ ), then it admits homogeneous second-Chern-Einstein metrics.
\item[(b)] If $\left(M_{(i, n)}(\mathrm{G}, \mathrm{K})\right.$, J) has one singular orbit (case $i=2$ ), then it admits a complete, non-Kähler, second-Chern-Einstein metrics of cohomogeneity one.
\item[(c)] If $\left(M_{(i, n)}(\mathrm{G}, \mathrm{K}), \complement\right)$ has two singular orbits (case $i=4$ ), then it does not admit any cohomogeneity one, submersion-type metrics which are second-Chern-Einstein.
\end{itemize}

Let us stress that the homogeneous second-Chern-Einstein metrics on $\left(M_{(1, n)}(\mathrm{G}, \mathrm{K}), \mathrm{J}\right)$ and $\left(M_{(3, n)}(\mathrm{G}, \mathrm{K}), \mathrm{J}\right)$, corresponding to case (a) in theorem C, are clearly of constant Chern-scalar curvature. They include the classical example
of the standard metric on the diagonal Hopf manifold, which corresponds in our notation to $M_{(3,1)}(\mathrm{G}, \mathrm{K})$ with $\mathrm{G}=\mathrm{SU}(m)$ and $\mathrm{K}=\mathrm{S}(\mathrm{U}(1) \times \mathrm{U}(m-1))$. On the other hand, the metrics that we constructed on manifolds with singular orbits, corresponding to cases (b) and (c) in theorem C, are weakly second-Chern-Einstein, namely, they do not have constant Chern-scalar curvature. Therefore, this brings us to investigate the constant Chern-scalar curvature problem for such manifolds. In this direction, we obtain

Theorem D (see remark 5.2, theorems 5.7, 5.8). All the Bérard-Bergery stan-dard cohomogeneity one complex manifolds $\left(M_{(i, n)}(\mathrm{G}, \mathrm{K}), J_{)}\right.$admit complete, non-Kähler metrics of cohomogeneity one with constant Chern-scalar curvature.

Note that, in complex dimension $m=2$, the compact case with two singular orbits (corresponding to $i=4$ ) reduces to the Hirzebruch surfaces. This case has been treated by Koca and Lejmi [33], who proved the existence of positive constant Chern-scalar curvature of cohomogeneity one.

The paper is organized as follows. In § 2, we recall some basics on the Chern connection and cohomogeneity one actions. In §3, we recall the construction of $\left(M_{(i, n)}(\mathrm{G}, \mathrm{K}), \mathrm{J}, \mathrm{g}\right)$ following Bérard-Bergery, and we compute the Hermitian curvatures and torsion of such manifolds. In §4, we investigate the existence of special non-Kähler Hermitian metrics, proving theorems A and B. In §5, we prove theorems C and D. Finally, in Appendix A, we collect the detailed computations needed in § 3, precisely to prove propositions 3.15 and 3.17, and in § 4, namely to prove equation (4.3).

\section*{2. Preliminaries}

In this section, we briefly recall some facts on the Chern connection and on Hermitian manifolds with cohomogeneity one actions by holomorphic isometries.

\subsection*{2.1. The Chern connection}

Let $(M, J, g)$ be a connected, complete, Hermitian manifold of real dimension $\operatorname{dim}_{\mathbb{R}} M=2 m$. Let us denote by $\omega:=\mathrm{g}(\mathcal{J} \cdot, \cdot)$ its fundamental 2-form, by $D$ its Levi-Civita connection and by ∇ its Chern connection, which is defined by
$$\left.\mathrm{g}\left(\nabla_{A} B, C\right):=\mathrm{g}\left(D_{A} B, C\right)-\frac{1}{2} \mathrm{~d} \omega( \lrcorner A, B, C\right)$$
for any $A, B, C \in \Gamma(T M)$. Since, by the Koszul formula,
$$\begin{aligned}
2 \mathrm{~g}\left(D_{A} B, C\right)= & \mathcal{L}_{A}(\mathrm{~g}(B, C))+\mathcal{L}_{B}(\mathrm{~g}(A, C))-\mathcal{L}_{C}(\mathrm{~g}(A, B)) \\
& +\mathrm{g}([A, B], C)-\operatorname{g}([A, C], B)-\operatorname{g}([B, C], A)
\end{aligned}$$
and
$$\begin{aligned}
\mathrm{d} \omega(A, B, C)= & \mathcal{L}_{A}(\mathfrak{g}(Л B, C))-\mathcal{L}_{B}(\mathfrak{g}(Л A, C))+\mathcal{L}_{C}(\mathfrak{g}(Л A, B)) \\
& +\mathfrak{g}([A, B], \sqrt{ } C)+\mathfrak{g}([B, C], \sqrt{ } A)+\mathfrak{g}([C, A], \sqrt{ } B),
\end{aligned}$$
it follows that
$$\begin{aligned}
2 \mathrm{~g}\left(\nabla_{A} B, C\right)= & \left.\mathcal{L}_{A}(\mathrm{~g}(B, C))-\mathcal{L}_{\lrcorner A}(\mathfrak{g}( \lrcorner B, C)\right)+\mathbb{g}([A, B], C) \\
& -\operatorname{g}([ \lrcorner A, B],\lrcorner C)-\mathfrak{g}([A, C], B)+\mathfrak{g}([ \lrcorner A, C],\lrcorner B) .
\end{aligned}$$
Moreover, it is well-known that the Chern connection is characterized by the following properties
$$\nabla \mathrm{g}=\nabla Л=0, \quad \Im \tau(A, B)=\tau(\Im A, B)=\tau(A, \Downarrow B),$$
where $\tau(A, B):=\nabla_{A} B-\nabla_{B} A-[A, B]$ is the torsion tensor of ∇ .
For later use, we observe the following straightforward
Lemma 2.1. For any $A \in \Gamma(T M)$ it holds that
$$\begin{aligned}
\mathcal{L}_{A} \mathfrak{l} & =-[\nabla A, \mathfrak{J}], \\
\mathcal{L}_{J A} \mathfrak{J} & =\sqrt{ } \circ \mathcal{L}_{A} \mathfrak{J} .
\end{aligned}$$
Proof. If $E \in \Gamma(\operatorname{End}(T M))$, then
$$\begin{aligned}
\left(\mathcal{L}_{A} E\right) B & =\mathcal{L}_{A}(E B)-E\left(\mathcal{L}_{A} B\right) \\
& =\nabla_{A}(E B)-\nabla_{E B} A-\tau(A, E B)-E\left(\nabla_{A} B\right)+E\left(\nabla_{B} A\right)+E(\tau(A, B)) \\
& =-[\nabla A, E] B+\left(\nabla_{A} E\right) B+E(\tau(A, B))-\tau(A, E B) .
\end{aligned}$$
Then, equation (2.6) follows by setting $E=\sqrt{ }$ and using equation (2.5). On the other hand, from equations (2.5) and (2.6) we get
$$\mathcal{L}_{Л A} \mathfrak{I}=-[\nabla Л A, \mathfrak{J}]=-[\mathbb{J} \nabla A, \mathfrak{J}]=-\mathbb{J}[\nabla A, \mathfrak{J}]=\mathscr{J} \circ \mathcal{L}_{A} \sqrt{ }$$
and so the thesis follows. \(\square\)

A real vector field $A \in \Gamma(T M)$ is holomorphic if $\mathcal{L}_{A} \unlhd=0$. Hence, we get
Corollary 2.2. Let $A \in \Gamma(T M)$. Then it holds:
\begin{itemize}
\item[-] $A$ is holomorphic if and only if
$$\nabla_{J B} A=\Im \nabla_{B} A \quad \text { for any } B \in \Gamma(T M) ;$$
\item[-] $A$ is holomorphic if and only if $\Im A$ is holomorphic.
\end{itemize}

Finally, we set $\mathrm{d}^{c}:={ }^{-1} \circ \mathrm{~d} \circ \sqrt{ }$, so that
$$\mathrm{d}=\partial+\bar{\partial}, \quad \mathrm{d}^{c}=-\sqrt{-1}(\partial-\bar{\partial}), \mathrm{dd}^{c}=2 \sqrt{-1} \partial \bar{\partial}$$
and, for any smooth function $f: M \rightarrow \mathbb{R}$, we denote by $\Delta_{\mathfrak{g}}^{\operatorname{Ch}} f:=\mathrm{g}\left(\mathrm{dd}^{c} f, \omega\right)$ the Chern-Laplacian of $f$.

\subsection*{2.2. Second-Chern-Einstein metrics}

Let $(M, J, g)$ be a connected, complete, Hermitian manifold of real dimension $\operatorname{dim}_{\mathbb{R}} M=2 m$. We recall that, by the lack of symmetries of the Chern-curvature
$$R^{\mathrm{Ch}}(\mathrm{~g})(A, B):=\nabla_{[A, B]}-\left[\nabla_{A}, \nabla_{B}\right],$$
we have (at least) two ways to trace the Ricci tensor. We call first Chern-Ricci curvature the tensor defined by
$$\operatorname{Ric}^{\mathrm{Ch}[1]}(\mathrm{g})(A, B)_{x}:=\sum_{e_{\alpha}} \mathrm{g}_{x}\left(R^{\mathrm{Ch}}(\mathrm{~g})_{x}\left(A_{x}, \sqrt{ } B_{x}\right) e_{\alpha}, \sqrt{ } e_{\alpha}\right),$$
where $\left(e_{\alpha}, J_{e_{\alpha}}\right)$ is a $(J, \mathbb{g})$-unitary frame for the tangent space at $x$. Similarly, we call second Chern-Ricci curvature the tensor defined by
$$\operatorname{Ric}^{\operatorname{Ch}[2]}(\mathrm{g})(A, B)_{x}:=\sum_{e_{\alpha}} \mathrm{g}_{x}\left(R^{\mathrm{Ch}}(\mathrm{~g})_{x}\left(e_{\alpha}, \sqrt{ } e_{\alpha}\right) A_{x}, \sqrt{ } B_{x}\right) .$$
Finally, the Chern-scalar curvature is the function given by
$$\operatorname{scal}^{\mathrm{Ch}}(\mathrm{~g})(x):=2 \sum_{e_{\alpha}} \operatorname{Ric}^{\mathrm{Ch}[\mathrm{i}]}(\mathrm{g})_{x}\left(e_{\alpha}, e_{\alpha}\right), \quad i=1,2 .$$
We remark that, according to our notation, when $\mathbb{g}$ is Kähler it holds that $\operatorname{Ric}^{\mathrm{Ch}[1]}(\mathrm{g})=\operatorname{Ric}^{\mathrm{Ch}[2]}(\mathrm{g})=\operatorname{Ric}(\mathrm{g})$ and $\operatorname{scal}^{\mathrm{Ch}}(\mathrm{g})=\operatorname{scal}(\mathrm{g})$, where Ric(g) and scal(g) denote the Riemannian Ricci tensor and the Riemannian scalar curvature of $\mathbb{g}$, respectively.

This yields to the following
DEFINITION 2.3. Let $i \in\{1,2\}$. The metric $\mathbb{g}$ is said to be weakly (respectively, strongly) $i$ th-Chern-Einstein if there exists $\lambda \in \mathcal{C}^{\infty}(M, \mathbb{R})$ (respectively, $\lambda \in \mathbb{R}$ ) such that
$$\operatorname{Ric}^{\operatorname{Ch}[i]}(\mathbb{g})=\frac{\lambda}{2 m} \mathfrak{g} .$$

We stress that the first-Chern-Einstein problem is basically understood for compact complex manifolds $X=(M, \sqrt{ })$, see [7, 52]. Indeed, strongly first-Chern-Einstein metrics with non-zero Chern-scalar curvature are Kähler-Einstein. Moreover, by conformal methods, if a Hermitian metric g is weakly first-Chern-Einstein with non-identically zero Chern-scalar curvature, then it is conformal to a Kähler metric in the class $\pm c_{1}(X)$ (see [7, theorem A]). Finally, compact complex manifolds with first-Bott-Chern class $c_{1}^{B C}(X)=0$ are the so-called non-Kähler Calabi-Yau manifolds [52] and always admit Chern-Ricci flat metrics [52, theorem 1.2], see also [53, corollary 2].

On the other hand, the second-Chern-Einstein problem seems to be geometrically more appealing, see e.g. [7, 24, 47, 51]. Note that a Hermitian metric $\mathbb{g}$ on $X=(M, \Downarrow)$ is second-Chern-Einstein according to definition 2.3 if and only if the induced Hermitian metric $h(V, W):=\mathrm{g}(V, \bar{W})$ on the holomorphic tangent bundle $T^{1,0} X$ is Hermite-Einstein by taking trace with itself [22].

Remark 2.4. We observe that the second-Chern-Einstein condition is satisfied by a Hermitian metric $\mathbb{g}$ if and only if it is satisfied by all the metrics in its conformal class (see [22]), since for any smooth function $f: M \rightarrow \mathbb{R}$ it holds that
$$\operatorname{Ric}^{\operatorname{Ch}[2]}\left(\mathrm{e}^{f} \mathrm{~g}\right)=\operatorname{Ric}^{\operatorname{Ch}[2]}(\mathbb{g})-\left(\Delta_{\mathscr{g}}^{\operatorname{Ch}} f\right) \mathbb{g} .$$
We remark that this is strongly different from the Riemannian analogue, i.e. the Einstein condition. On the other hand, we stress that a Kähler metric is second-Chern-Einstein if and only if it is Einstein.

Note that, up to our knowledge, a non-Kähler example of second-Chern-Einstein metric on a compact complex manifold of complex dimension $m>2$ with negative scalar curvature is still missing.

\subsection*{2.3. Cohomogeneity one group actions on Hermitian manifolds}

Let us consider a compact, connected real Lie group G which acts effectively by holomorphic isometries on $(M, \downharpoonleft, g)$ with cohomogeneity one [9, 10, 41, 48]. Then, the orbit space $\Omega:=\mathrm{G} \backslash M$ is homeomorphic to one of the following:
(i) $\Omega \simeq \mathbb{R}$,
(ii) $\Omega \simeq[0,+\infty)$,
(iii) $\Omega \simeq S^{1}$, (iv) $\Omega \simeq[0, \pi]$.
Up to homothety, we can choose a unit speed geodesic $\gamma: \bar{I} \rightarrow M$ which intersects orthogonally any G-orbit [9, §2.7], where the interval $I \subset \mathbb{R}$ is defined as
(i) $I:=\mathbb{R}$,
(ii) $I:=(0,+\infty)$,
(iii) $I:=(-\pi, \pi)$,
(iv) $I:=(0, \pi)$.
Then, for $r \in I$, the orbit $\mathcal{S}_{r}:=\mathrm{G} \cdot \gamma(r)$ is principal and can be identified with a fixed homogeneous space by means of the 1-parameter family of G-equivariant diffeomorphisms
$$\phi_{r}: \mathrm{G} / \mathrm{H} \rightarrow \mathcal{S}_{r}, \quad \phi_{r}(a \mathrm{H}):=a \cdot \gamma(r),$$
where $\mathrm{H} \subset \mathrm{G}$ is a closed subgroup. For $r \in \partial I$, the following cases occur:
\begin{itemize}
\item[(i)] $\partial I=\emptyset$ and all the orbits are principal;
\item[(ii)] $\partial I=\{0\}$, the orbit $\mathcal{S}_{0}:=\mathrm{G} \cdot \gamma(0)$ is non-principal and G-equivariantly diffeomorphic to a homogeneous space $\mathrm{G} / \mathrm{L}$, where $\mathrm{H} \subset \mathrm{L} \subset \mathrm{G}$ is an intermediate subgroup and L/H is a sphere, see e.g. [9, § 2.12];
\item[(iii)] $\partial I=\{ \pm \pi\}$, the orbits $\mathcal{S}_{ \pm \pi}:=\mathrm{G} \cdot \gamma( \pm \pi)$ are principal but in general $\gamma(-\pi) \neq$ $\gamma(\pi)$, see e.g. [9, § 2.10];
\item[(iv)] $\partial I=\{0, \pi\}$, the orbits $\mathcal{S}_{0}:=\mathrm{G} \cdot \gamma(0), \mathcal{S}_{\pi}:=\mathrm{G} \cdot \gamma(\pi)$ are non-principal and G-equivariantly diffeomorphic to two homogeneous space $\mathrm{G} / \mathrm{L}_{ \pm}$, with $\mathrm{H} \subset$ $\mathrm{L}_{-} \cap \mathrm{L}_{+}$and $\mathrm{L}_{ \pm} / \mathrm{H}$ are spheres, see e.g. [9, § 2.13].
\end{itemize}

The subset $M^{\text {reg }}:=\bigcup_{r \in I} \mathcal{S}_{r}$ of regular points is an open, dense submanifold of $M$ which projects onto $I$ by means of the canonical projection $M \rightarrow \Omega$ and the
restricted Riemannian metric splits as
$$\left.\mathrm{g}\right|_{M^{\mathrm{reg}}}=\mathrm{d} r^{2}+\left.\mathrm{g}\right|_{S_{r}},$$
where $r$ is the coordinate on $I$. We fix an $\operatorname{Ad}(\mathrm{G})$-invariant inner product $Q$ on the Lie algebra $\mathfrak{g}:=\operatorname{Lie}(\mathrm{G})$ and a $Q$-orthogonal decomposition $\mathfrak{g}=\mathfrak{h}+\mathfrak{m}$, with $\mathfrak{h}:=$ Lie (H). We consider identified $\mathfrak{m} \simeq T_{e \mathrm{H}} \mathrm{G} / \mathrm{H}$ by means of the evaluation map $X \mapsto$ $\left.\frac{\mathrm{d}}{\mathrm{d} s} \exp (s X) \mathrm{H}\right|_{s=0}$, where $\exp : \mathfrak{g} \rightarrow \mathrm{G}$ denotes the Lie exponential map of G. We also identify any G-invariant tensor field on G/H with the corresponding Ad(H)-invariant tensor on $\mathfrak{m}$ in the usual way.

Firstly, we define the 1-parameter family $\left(g_{r}\right) \subset \operatorname{Sym}^{2}\left(\mathfrak{m}^{*}\right)^{\operatorname{Ad}(\mathrm{H})}$ by
$$g_{r}:=\left(\phi_{r}\right)^{*}\left(\left.\mathrm{~g}\right|_{\delta_{r}}\right) .$$
We also set
$$T_{r}:=\frac{\left(\mathrm{d} \phi_{r}\right)_{e \mathrm{H}}^{-1}\left(\mathfrak{J}_{\gamma(r r)} \dot{\gamma}(r)\right)}{\left|\left(\mathrm{d} \phi_{r}\right)_{e \mathrm{H}}^{-1}\left(\mathfrak{J}_{\gamma(r)} \dot{\gamma}(r)\right)\right|_{Q}} \in \mathfrak{m}, \quad \theta_{r}:=\left.Q\left(T_{r}, \cdot\right)\right|_{\mathfrak{m}} \in \mathfrak{m}^{*} .$$
Then, for any $r \in I$, the complex structure I induces a linear complex structure $J_{r}$ on $\mathfrak{p}_{r}:=\operatorname{ker}\left(\theta_{r}\right) \subset \mathfrak{m}$ by setting
$$J_{r}: \mathfrak{p}_{r} \rightarrow \mathfrak{p}_{r}, \quad J_{r}:=\left.\left(\mathrm{d} \phi_{r}\right)_{e \mathrm{H}}^{-1} \circ \mathfrak{J}_{\gamma(r)} \circ\left(\mathrm{d} \phi_{r}\right)_{e \mathrm{H}}\right|_{\mathfrak{p}_{r}} .$$
The integrability of $\Im$ implies that, for any $X, Y \in \mathfrak{p}_{r}$,
$$\begin{aligned}
& {\left[J_{r} X, Y\right]_{\mathfrak{m}}+\left[X, J_{r} Y\right]_{\mathfrak{m}} \in \mathfrak{p}_{r},} \\
& J_{r}\left(\left[J_{r} X, Y\right]_{\mathfrak{m}}+\left[X, J_{r} Y\right]_{\mathfrak{m}}\right)=\left[J_{r} X, J_{r} Y\right]_{\mathfrak{m}}-[X, Y]_{\mathfrak{m}} .
\end{aligned}$$
Moreover, since the subgroup $\mathrm{H} \subset \mathrm{G}$ leaves any point of the geodesic $\gamma$ fixed and G acts by holomorphic isometries, it follows that
$$\left[\mathfrak{h}, T_{r}\right]=0 \quad \text { for any } r \in I$$
and so $\left(\theta_{r}, J_{r}\right)$ is a 1-parameter family of G-invariant CR structures on G/H, see e.g. [3].

We recall now the following definition [48]: G/H is said to be ordinary if G is semisimple, the normalizer $\mathrm{K}:=\mathrm{N}_{\mathrm{G}}\left(\mathrm{H}^{\circ}\right)$ of the connected component $\mathrm{H}^{\circ}$ of H is the centralizer of a torus and $\operatorname{dim} \mathrm{K}=1+\operatorname{dim} \mathrm{H}$. This implies that:
\begin{itemize}
\item[-] $T \equiv T_{r}$ and $\mathfrak{p} \equiv \mathfrak{p}_{r}$ do not depend on $r \in I$;
\item[-] the Lie algebra $\mathfrak{k}:=\operatorname{Lie}(\mathrm{K})$ splits $Q$-orthogonally as $\mathfrak{k}=\mathfrak{h} \oplus \mathbb{R} T$.
\end{itemize}

Moreover, the complex structure $\mathcal{J}$ is said to be projectable if each $J_{r}$ is $\operatorname{Ad}(\mathrm{K})$ -invariant. In this case, $\left(J_{r}\right)_{r \in I}$ is mapped onto a 1-parameter family of G-invariant complex structures on the flag manifold G/K. Since the set of invariant complex structures on a flag manifold is discrete [1, 42], it follows that $J \equiv J_{r}$ is constant.

Definition 2.5 [4, 48]. The Hermitian manifold ( $M, \mathfrak{J}, \mathbb{g}$ ) acted by G is said to be standard if the following conditions are satisfied:
\begin{itemize}
\item[-] the principal orbits are ordinary and the complex structure I is projectable;
\item[-] the non-principal orbits, if they exist, are flag manifolds with the induced complex structure.
\end{itemize}

In § 3, a distinguished kind of cohomogeneity one standard Hermitian manifolds will be investigated.

\section*{3. Bérard-Bergery standard cohomogeneity one Hermitian manifolds}

In this section, we consider a special class of standard cohomogeneity one Hermitian manifolds, following the construction of Bérard-Bergery [9]. Then, we compute the Chern connection and the Chern-Ricci tensors of such manifolds.

\subsection*{3.1. Chern connection of standard cohomogeneity one Hermitian manifolds}

Let $(M, l, g)$ be a standard cohomogeneity one Hermitian manifolds acted effectively by holomorphic isometries by a compact, connected real Lie group G.

Hereafter, we adopt the same notation introduced in § 2. Note that the complement $\mathfrak{m}$ of $\mathfrak{h}$ in $\mathfrak{g}$ admits a $Q$-orthogonal, Ad(H)-invariant decomposition $\mathfrak{m}=\mathfrak{a}+\mathfrak{p}$, where $\mathfrak{a}:=\mathbb{R} T$ is the trivial submodule. Since, by hypothesis, $\mathfrak{p}$ does not contain any trivial $\operatorname{Ad}(\mathrm{H})$-submodule, the metrics $g_{r}$ induced by $\mathfrak{g}$ on $\mathfrak{m}$ split uniquely as
$$g_{r}=\left.F(r)^{2} Q\right|_{\mathfrak{a} \otimes \mathfrak{a}}+\left.g_{r}\right|_{\mathfrak{p} \otimes \mathfrak{p}}$$
by means of the Schur lemma, where $F: I \rightarrow \mathbb{R}$ is a smooth, positive function, possibly satisfying some appropriate boundary condition.

From now on, given $V \in \mathfrak{g}$, we denote by $V^{*} \in \Gamma(T M)$ the fundamental vector field on $M$ associated with $V$, that is $V_{p}^{*}:=\left.\frac{\mathrm{d}}{\mathrm{d} s} \exp (s V) \cdot p\right|_{s=0}$, and we also set
$$N:=F \frac{\partial}{\partial r} .$$
Note that, by construction,
$$(J N)_{\gamma(r)}=T_{\gamma(r)}^{*}$$
and, for any $V, W \in \mathfrak{g}$, it holds
$$\left[V^{*}, W^{*}\right]=-[V, W]^{*}, \quad\left[N, V^{*}\right]=0 .$$
We observe also that, for any $X \in \mathfrak{p}$ and for any $Y_{1}, Y_{2} \in \mathfrak{m}$, we have
$$\mathrm{g}\left(Y_{1}^{*}, Y_{2}^{*}\right)_{\gamma(r)}=g_{r}\left(Y_{1}, Y_{2}\right), \quad\left(\mathscr{J} X^{*}\right)_{\gamma(r)}=(J X)_{\gamma(r)}^{*} .$$
By hypothesis, the fundamental vector fields $V^{*}$ are holomorphic, i.e.
$$\left[V^{*}, J A\right]=J\left[V^{*}, A\right] \quad \text { for any } A \in \Gamma(T M) \text {. }$$

By using equations (2.2) and (2.3), one can directly obtain the explicit formulas for the Levi-Civita connection and the 3-form $\mathrm{d} \omega$. Here and in the following statements, we consider the context and assume the notation as above.

Proposition 3.1. Let $X, Y, Z \in \mathfrak{p}$. Then, the non-vanishing components of the Levi-Civita connection are given by
$$\begin{aligned}
2 \mathbb{g}\left(D_{Y^{*}} X^{*}, Z^{*}\right)_{\gamma(r)} & =g_{r}([X, Y], Z)+g_{r}([Z, X], Y)+g_{r}([Z, Y], X), \\
2 \mathbb{g}\left(D_{Y^{*}} X^{*}, T^{*}\right)_{\gamma(r)} & =g_{r}([X, Y], T)+g_{r}([T, X], Y)+g_{r}([T, Y], X), \\
2 \mathbb{g}\left(D_{Y^{*}} X^{*}, N\right)_{\gamma(r)} & =-F(r) \frac{\partial}{\partial r}\left(g_{r}(X, Y)\right), \\
2 \mathbb{g}\left(D_{T^{*}} X^{*}, Z^{*}\right)_{\gamma(r)} & =-g_{r}([X, Z], T)-g_{r}([T, X], Z)-g_{r}([T, Z], X), \\
2 \mathbb{g}\left(D_{N} X^{*}, Z^{*}\right)_{\gamma(r)} & =F(r) \frac{\partial}{\partial r}\left(g_{r}(X, Z)\right), \\
2 \mathbb{g}\left(D_{Y^{*}} T^{*}, Z^{*}\right)_{\gamma(r)} & =-g_{r}([Y, Z], T)+g_{r}([T, Y], Z)-g_{r}([T, Z], Y), \\
2 \mathbb{g}\left(D_{T^{*}} T^{*}, N\right)_{\gamma(r)} & =-2 F^{\prime}(r) F(r)^{2}, \\
2 \mathbb{g}\left(D_{N} T^{*}, T^{*}\right)_{\gamma(r)} & =2 F^{\prime}(r) F(r)^{2}, \\
2 \mathbb{g}\left(D_{Y^{*}} N, Z^{*}\right)_{\gamma(r)} & =F(r) \frac{\partial}{\partial r}\left(g_{r}(Y, Z)\right), \\
2 \mathbb{g}\left(D_{T^{*}} N, T^{*}\right)_{\gamma(r)} & =2 F^{\prime}(r) F(r)^{2}, \\
2 \mathbb{g}\left(D_{N} N, N\right)_{\gamma(r)} & =2 F^{\prime}(r) F(r)^{2} .
\end{aligned}$$
Proposition 3.2. Let $X, Y, Z \in \mathfrak{p}$. Then, the 3-form $\mathrm{d} \omega$ is given by
$$\begin{aligned}
\mathrm{d} \omega\left(X^{*}, Y^{*}, Z^{*}\right)_{\gamma(r)} & =g_{r}([X, Y], J Z)+g_{r}([Y, Z], J X)+g_{r}([Z, X], J Y), \\
\mathrm{d} \omega\left(X^{*}, Y^{*}, T^{*}\right)_{\gamma(r)} & =g_{r}([T, X], J Y)+g_{r}([T, J Y], X), \\
\mathrm{d} \omega\left(X^{*}, Y^{*}, N\right)_{\gamma(r)} & =F(r) \frac{\partial}{\partial r}\left(g_{r}(J X, Y)\right)+g_{r}([X, Y], T), \\
\mathrm{d} \omega\left(X^{*}, T^{*}, N\right)_{\gamma(r)} & =0 .
\end{aligned}$$

By combining propositions 3.1 and 3.2, and by equation (2.1), we obtain explicit formulas for the Chern connection along the geodesic $\gamma(r)$. More precisely

Proposition 3.3. Let $X, Y, Z \in \mathfrak{p}$. Then the non-vanishing components of the Chern connection are
$$\begin{aligned}
2 \mathbb{g}\left(\nabla_{Y^{*}} X^{*}, Z^{*}\right)_{\gamma(r)}= & g_{r}([X, Y], Z)+g_{r}([X, J Y], J Z) \\
& +g_{r}([Z, Y], X)-g_{r}([Z, J Y], J X), \\
2 \mathbb{g}\left(\nabla_{Y^{*}} X^{*}, T^{*}\right)_{\gamma(r)}= & g_{r}([X, Y], T), \\
2 \mathbb{g}\left(\nabla_{Y^{*}} X^{*}, N\right)_{\gamma(r)}= & g_{r}([X, J Y], T), \\
2 \mathbb{g}\left(\nabla_{T^{*}} X^{*}, Z^{*}\right)_{\gamma(r)}= & F(r) \frac{\partial}{\partial r}\left(g_{r}(J X, Z)\right)-g_{r}([T, X], Z)-g_{r}([T, Z], X), \\
2 \mathbb{g}\left(\nabla_{N} X^{*}, Z^{*}\right)_{\gamma(r)}= & F(r) \frac{\partial}{\partial r}\left(g_{r}(X, Z)\right)+g_{r}([T, J X], Z)+g_{r}([T, Z], J X), \\
2 \mathbb{g}\left(\nabla_{Y^{*}} T^{*}, Z^{*}\right)_{\gamma(r)}= & 2 g_{r}([T, Y], Z)-g_{r}([Y, Z], T), \\
2 \mathbb{g}\left(\nabla_{T^{*}} T^{*}, N\right)_{\gamma(r)}= & -2 F^{\prime}(r) F(r)^{2}, \\
2 \mathbb{g}\left(\nabla_{N} T^{*}, T^{*}\right)_{\gamma(r)}= & +2 F^{\prime}(r) F(r)^{2}, \\
2 \mathbb{g}\left(\nabla_{Y^{*}} N, Z^{*}\right)_{\gamma(r)}= & g_{r}([J Y, Z], T), \\
2 \mathbb{g}\left(\nabla_{T^{*}} N, T^{*}\right)_{\gamma(r)}= & 2 F^{\prime}(r) F(r)^{2}, \\
2 \mathbb{g}\left(\nabla_{N} N, N\right)_{\gamma(r)}= & 2 F^{\prime}(r) F(r)^{2} .
\end{aligned}$$

As a direct consequence of proposition 3.3 and equation (2.6), we get
Corollary 3.4. It holds that $\left(\mathcal{L}_{N} \mathbb{J}\right)_{\gamma(r)}=0$, i.e. $[N, \sqrt{ } A]_{\gamma(r)}=\sqrt{ }[N, A]_{\gamma(r)}$ for any $A \in \Gamma(T M)$.

We can also characterize the Kähler metrics as follows. By proposition 3.2 it follows that
$$\mathrm{d} \omega\left(X^{*}, Y^{*}, T^{*}\right)_{\gamma(r)}=0 \quad \text { for any } X, Y \in \mathfrak{p}$$
if and only if the restriction $\left.g_{r}\right|_{\mathfrak{p} \otimes \mathfrak{p}}$ is $\operatorname{Ad}(\mathrm{K})$-invariant for any $r \in I$. This is equivalent to say that the metrics $\left(g_{r}\right)$ on G/H are of submersion-type with respect to the homogeneous circle bundle K/H → G/H → G/K, namely, they induce metrics on the base such that the projection is a Riemannian submersion. Moreover, if $\left.g_{r}\right|_{\mathfrak{p} \otimes \mathfrak{p}}$ is $\operatorname{Ad}(\mathrm{K})$-invariant, then the condition
$$\mathrm{d} \omega\left(X^{*}, Y^{*}, Z^{*}\right)_{\gamma(r)}=0 \quad \text { for any } X, Y, Z \in \mathfrak{p}$$
holds true if and only if the induced metrics on the flag manifold G/K are Kähler. Let us fix now a $Q$-orthogonal, Ad(K)-invariant, irreducible decomposition
$$\mathfrak{p}=\mathfrak{p}_{1}+\cdots+\mathfrak{p}_{\ell} .$$
Since flag manifolds are equal rank homogeneous spaces, namely $\operatorname{rank}(\mathrm{K})=\operatorname{rank}(\mathrm{G})$, it follows that their isotropy representations are always monotypic, namely $\mathfrak{p}_{i} \nsubseteq \mathfrak{p}_{j}$ for any $1 \leqslant i<j \leqslant \ell$. Hence, the decomposition (3.6) is unique (up to order) and, by the Schur lemma, the metrics $g_{r}$ splits uniquely as
$$g_{r}=\left.F(r)^{2} Q\right|_{\mathfrak{a} \otimes \mathfrak{a}}+\left.h_{1}(r)^{2} Q\right|_{\mathfrak{p}_{1} \otimes \mathfrak{p}_{1}}+\cdots+\left.h_{\ell}(r)^{2} Q\right|_{\mathfrak{p}_{\ell} \otimes \mathfrak{p}_{\ell}} .$$
Then, the condition
$$\mathrm{d} \omega\left(X^{*}, Y^{*}, N\right)_{\gamma(r)}=0 \quad \text { for any } X, Y \in \mathfrak{p}$$
holds true if and only if
$$\left.\operatorname{ad}(T)\right|_{\mathfrak{p}_{i}}=-2 \frac{h_{i}(r) h_{i}^{\prime}(r)}{F(r)} J \quad \text { for any } 1 \leqslant i \leqslant \ell .$$

\subsection*{3.2. Construction of Bérard-Bergery manifolds}

Let us assume that $P=P(\mathrm{G}, \mathrm{K}):=\mathrm{G} / \mathrm{K}$ is a simply-connected, irreducible compact Hermitian symmetric space, i.e. G is a connected, compact, simple Lie group and K c G is a maximal, connected, compact subgroup with centre isomorphic to the circle group [30, theorem 6.1]. Set $\operatorname{dim}_{\mathbb{R}} P=2(m-1)$, with $m \geqslant 2$, and let $p \in \mathbb{N}$ be the unique positive integer such that $p^{-1} c_{1}(P)$ is an indivisible (positive) class in the cohomology group $H^{2}(P ; \mathbb{Z})$, see [13, chapter 5, § 16]. In the following, we list the possibilities for $P$, following [10, § 7.102 and § 9.124].

\begin{tabular}[t]{|l|l|l|l|}
\hline $P$ & $m$ & $p$ & conditions \\
\hline $\mathrm{SU}\left(k_{1}+k_{2}\right) / \mathrm{S}\left(\mathrm{U}\left(k_{1}\right) \times \mathrm{U}\left(k_{2}\right)\right)$ & $k_{1} k_{2}+1$ & $k_{1}+k_{2}$ & $k_{2} \geqslant k_{1} \geqslant 1$ \\
\hline $\operatorname{SO}(2 k) / \mathrm{U}(k)$ & $\frac{k(k-1)}{2}+1$ & $2(k-1)$ & $k \geqslant 5$ \\
\hline $\operatorname{Sp}(k) / \mathrm{U}(k)$ & $\frac{k(k+1)}{2}+1$ & $k+1$ & $k \geqslant 2$ \\
\hline $\operatorname{SO}(k+2) /(\operatorname{SO}(2) \times \mathrm{SO}(k))$ & $k+1$ & $k$ & $k \geqslant 5$ \\
\hline $\mathrm{E}_{6} /$ SO $(2)$ Spin $(10)$ & 17 & 12 & - \\
\hline $\mathrm{E}_{7} / \mathrm{SO}(2) \mathrm{E}_{6}$ & 28 & 18 & - \\
\hline
\end{tabular}
Denote by H := [K, K] the commutator of K. By hypothesis, there exists an integer $s \geqslant 1$ such that $\mathrm{H} \cap \mathrm{Z}(\mathrm{K}) \simeq \mathbb{Z}_{s}$. Fix an isomorphism $\imath: \mathrm{U}(1) \rightarrow \mathrm{Z}(\mathrm{K})$ and consider the generator $\alpha:=\imath\left(\mathrm{e}^{\sqrt{-1}(2 \pi / s)}\right)$ of $\mathrm{H} \cap \mathrm{Z}(\mathrm{K})$. Then, consider the right action of $\mathbb{Z}_{s}$ on $\mathrm{H} \times \mathrm{U}(1)$ given by $(h, z) \cdot j:=\left(h \alpha^{j}, \mathrm{e}^{-\sqrt{-1}(2 j \pi / s)} z\right)$ and take the quotient $\mathrm{H} \cdot \mathrm{U}(1):=\mathrm{H} \times_{\mathbb{Z}_{s}} \mathrm{U}(1)$. We can consider identified $\mathrm{K}=\mathrm{H} \cdot \mathrm{U}(1)$ by means of a Lie group isomorphism (see e.g. [16, chapter 0, theorem 6.9]) and, for any positive
integer $n$, we take the representation
$$\rho_{n}: \mathrm{K} \rightarrow \mathrm{U}(1), \quad \rho_{n}([h, z]):=z^{-s n} .$$
Then, consider the associated bundle
$$\S_{n}=\S_{n}(\mathrm{G}, \mathrm{~K}):=\mathrm{G} \times_{\rho_{n}} \mathrm{U}(1)$$
with the projection $\pi_{n}: \S_{n} \rightarrow P$ given by $\pi_{n}([a, z]):=a \mathrm{~K}$. Note that G acts transitively on the left on $\S_{n}$ by $\tilde{a} \cdot[a, z]:=[\tilde{a} a, z]$ and the stabilizer of $[e, 1]$ is the subgroup $\operatorname{ker}\left(\rho_{n}\right)=\mathrm{H} \times \mathbb{Z}_{n} \subset \mathrm{~K}$, where
$$\mathrm{H} \times \mathbb{Z}_{n} \simeq \mathrm{H} \times_{\mathbb{Z}_{s}} \mathbb{Z}_{s n} \subset \mathrm{H} \cdot \mathrm{U}(1)=\mathrm{K} \quad \text { by } \quad(h, j) \mapsto\left[h, \mathrm{e}^{\sqrt{-1}(2 j \pi / n)}\right] .$$
We are ready to construct the family $M_{(i, n)}(\mathrm{G}, \mathrm{K})$, with $1 \leqslant i \leqslant 4$ and $n \in \mathbb{N}$, of standard cohomogeneity one Hermitian manifolds in the following way.
\begin{itemize}
\item[(i)] We set $M_{(1, n)}(\mathrm{G}, \mathrm{K}):=\S_{n} \times \mathbb{R}$ and we let G act on $M_{(1, n)}$ via $a \cdot(x, r):=$ ( $a \cdot x, r$ ). The orbit space is $\Omega=\mathbb{R}$.
\item[(ii)] We let $M_{(2, n)}(\mathrm{G}, \mathrm{K}):=\S_{n} \times_{\mathrm{U}(1)} \mathbb{C}$ be the homogeneous complex line bundle over $P$ associated with $\pi_{n}: \S_{n} \rightarrow P$ by means of the standard action of U(1) on $\mathbb{C}$. Then, $M_{(2, n)}(\mathrm{G}, \mathrm{K})$ is equivariantly diffeomorphic to the quotient of $\S_{n} \times[0,+\infty)$ by the fibration $\S_{n} \times\{0\} \rightarrow P$, on which G acts by left multiplication on the first factor.
\item[(iii)] We set $M_{(3, n)}(\mathrm{G}, \mathrm{K}):=\S_{n} \times S^{1}$ and we let G act on $M_{(3, n)}(\mathrm{G}, \mathrm{K})$ via $a$. $(x, z):=(a \cdot x, z)$. The orbit space is $\Omega=S^{1}$.
\item[(iv)] We let $M_{(4, n)}(\mathrm{G}, \mathrm{K}):=\S_{n} \times_{\mathrm{U}(1)} \mathbb{C} \mathbb{P}^{1}$ be the homogeneous $\mathbb{C P}^{1}$-bundle over $P$ associated with $\pi_{n}: \S_{n} \rightarrow P$ by means of the standard action of U(1) on $\mathbb{C P}^{1}$. Then, $M_{(4, n)}(\mathrm{G}, \mathrm{K})$ is equivariantly diffeomorphic to the quotient of $\S_{n} \times$ $[0, \pi]$ under the identification of the two boundaries by means of the fibrations $\S_{n} \times\{0\} \rightarrow P$ and $\S_{n} \times\{\pi\} \rightarrow P$, on which G acts by left multiplication on the first factor.
\end{itemize}

We observe that the manifolds in families $M_{(3, n)}(\mathrm{G}, \mathrm{K})$ and $M_{(4, n)}(\mathrm{G}, \mathrm{K})$ are compact, and the manifolds in families $M_{(2, n)}(\mathrm{G}, \mathrm{K})$ and $M_{(4, n)}(\mathrm{G}, \mathrm{K})$ are simply connected. Moreover, manifolds in family $M_{(4, n)}(\mathrm{G}, \mathrm{K})$ are almost-homogeneous in the sense of [31], i.e. the complexified Lie group $\mathbb{G}^{\mathbb{C}}$ acts on them by biholomorphisms with one open orbit, see [49].

Let $M_{(i, n)}(\mathrm{G}, \mathrm{K})$ be as above. We denote by $B$ be the Cartan-Killing form of $\mathfrak{g}:=\operatorname{Lie}(\mathrm{G})$ and we set $\mathfrak{k}:=\operatorname{Lie}(\mathrm{K}), \mathfrak{h}:=\operatorname{Lie}(\mathrm{H}), \mathfrak{a}:=\mathfrak{z}(\mathfrak{k})=\operatorname{Lie}(\mathrm{Z}(\mathrm{K}))$. Then, the positive definite $\operatorname{Ad}(\mathrm{G})$-invariant scalar product $Q:=\frac{1}{4 m}(-B)$ on $\mathfrak{g}$ determines a $\operatorname{Ad}(\mathrm{H})$-invariant, $Q$-orthogonal decomposition
$$\mathfrak{g}=\underbrace{\mathfrak{h}+\mathfrak{a}+\mathfrak{p}}_{\mathfrak{k}}, \quad \text { with }[\mathfrak{k}, \mathfrak{k}]=\mathfrak{h},[\mathfrak{h}, \mathfrak{a}]=\{0\},[\mathfrak{k}, \mathfrak{p}] \subset \mathfrak{p},[\mathfrak{p}, \mathfrak{p}] \subset \mathfrak{k} .$$

We fix a vector $T \in \mathfrak{a}$ with $Q(T, T)=1$ and we pick the only $\lambda>0$ such that
$$J:=\left.\lambda^{-1} \operatorname{ad}(T)\right|_{\mathfrak{p}}$$
is a linear complex structure on $\mathfrak{p}$ [32, chapter XI, theorem 9.6]. Note that a direct computation implies
$$-4 m=B(T, T)=\operatorname{Tr}(\operatorname{ad}(T) \circ \operatorname{ad}(T))=-\lambda^{2} \operatorname{Tr}\left(\operatorname{Id}_{2(m-1)}\right)$$
and so
$$\lambda^{2}=\frac{2 m}{m-1} .$$
Remark 3.5 [48, p. 814]. The linear complex structure $J$ on $\mathfrak{p}$ determines uniquely a G-invariant, projectable, complex structure $\mathcal{I}$ on $M_{(i, n)}(\mathrm{G}, \mathrm{K})$.

Moreover, we stress that:
\begin{itemize}
\item[-] the restriction $Q_{\mathfrak{p}}:=\left.Q\right|_{\mathfrak{p} \otimes \mathfrak{p}}$ induces a G-invariant Kähler-Einstein metric on the base space $P$ satisfying the equation $\operatorname{Ric}\left(Q_{\mathfrak{p}}\right)=2 m Q_{\mathfrak{p}}$
\item[-] the scalar product $\frac{2 m(m-1) n^{2}}{p^{2}} Q_{\mathfrak{a}}$, with $Q_{\mathfrak{a}}:=\left.Q\right|_{\mathfrak{a} \otimes \mathfrak{a}}$, corresponds to the standard metric of radius 1 on the fibres of $\pi_{n}: \S_{n} \rightarrow P$
\end{itemize}

Then, being $P$ irreducible, any G-invariant Hermitian metric $g$ on $\left(M_{(i, n)}(\mathrm{G}, \mathrm{K})\right.$, J $)$ which is of submersion-type with respect to $M_{(i, n)}(\mathrm{G}, \mathrm{K}) \rightarrow P$ is completely determined by two positive, smooth functions $f, h: I \rightarrow \mathbb{R}$, satisfying some appropriate smoothness conditions, by means of the splitting
$$g_{r}=\frac{2 m(m-1) n^{2}}{p^{2}} f(r)^{2} Q_{\mathfrak{a}}+h(r)^{2} Q_{\mathfrak{p}},$$
where $\left(g_{r}\right)$ is again the 1-parameter family of G-invariant metrics induced by g on the principal orbits. Case by case, the smoothness conditions are the following (see e.g. [54, p. 7] and [9, p. 39]).
\begin{itemize}
\item[(i)] For $i=1, I=\mathbb{R}$ and there are no boundary conditions.
\item[(ii)] For $i=2, I=(0,+\infty)$ and the conditions are: $f$ is the restriction of a smooth odd function on $\mathbb{R}$ with $f^{\prime}(0)=1$ and $h$ is the restriction of a smooth even function on $\mathbb{R}$.
\item[(iii)] For $i=3, f, h$ need to be $S^{1}$-periodic.
\item[(iv)] For $i=4, I=(0, \pi)$ and the conditions are: $f$ is the restriction of a smooth odd function on $\mathbb{R}$ satisfying $f(\pi+r)=-f(\pi-r)$ with $f^{\prime}(0)=1=-f^{\prime}(\pi)$ and $h$ is the restriction of a smooth even function on $\mathbb{R}$ satisfying $h(\pi+r)=$ $h(\pi-r)$.
\end{itemize}

Conversely, any pair of smooth functions $(f, h)$ satisfying the appropriate smoothness condition uniquely defines a smooth G-invariant Hermitian metric $\mathrm{g}=\mathrm{g}(f, h)$, which is of submersion-type.

By equations (3.7), (3.9) and (3.10), it follows that the metric $\mathrm{g}(f, h)$ is Kähler if and only if the functions $f, h$ verify
$$h(r) h^{\prime}(r)+\frac{m n}{p} f(r)=0 \quad \text { for any } r \in I \text {. }$$
Remark 3.6. We note that the smoothness condition in (iii) and equation (3.11) imply immediately that the complex manifolds $\left(M_{(3, n)}(\mathrm{G}, \mathrm{K}), J\right)$ cannot admit cohomogeneity one, submersion-type Kähler metrics (see also [4, corollary 20]). Actually, it holds more: it can be easily check that $\pi_{1}\left(\S_{n}\right)$ is finite, and so its first Betti number is $b_{1}\left(\S_{n}\right)=0$. In particular, this implies that $\left(M_{(3, n)}(\mathrm{G}, \mathrm{K})\right.$, J) do not admit Kähler metrics at all.

From now on, we will adopt the following
Definition 3.7. A Bérard-Bergery standard cohomogeneity one Hermitian manifold is a triple $\left(M_{(i, n)}(\mathrm{G}, \mathrm{K}), \mathrm{J}, \mathrm{g}\right)$, where $M_{(i, n)}(\mathrm{G}, \mathrm{K})$ is the bundle over $P=$ G/K constructed as above, J is the unique G-invariant projectable complex structure on $M_{(i, n)}(\mathrm{G}, \mathrm{K})$ as in remark 3.5 and $\mathfrak{g}=\mathrm{g}(f, h)$ is the Riemannian metric described in equation (3.10). Accordingly, any pair $\left(M_{(i, n)}(\mathrm{G}, \mathrm{K}), \Downarrow\right)$ will be called Bérard-Bergery standard cohomogeneity one complex manifold.

Let us point out that the above construction can be performed in a more general setting, i.e. by requiring that the base space $P=\mathrm{G} / \mathrm{K}$ is a Kähler C-space, see [9]. However, in this work, we will just focus in the case of $P$ being symmetric and irreducible.

Example 3.8. Consider the Hermitian symmetric space $P=\mathbb{C P}^{m-1}$, corresponding to $\mathrm{G}=\mathrm{SU}(m)$ and $\mathrm{K}=\mathrm{S}(\mathrm{U}(1) \times \mathrm{U}(m-1))$. Here, the $\mathrm{Ad}(\mathrm{G})$-invariant scalar product $Q\left(A_{1}, A_{2}\right):=-\frac{1}{2} \operatorname{Tr}\left(A_{1} A_{2}\right)$ on the Lie algebra $\mathfrak{g}=\mathfrak{s u}(m)$, defined following the above normalization, induces on $P$ the Fubini-Study metric with sectional curvature satisfying $1 \leqslant \sec \leqslant 4$. In this case, the principal orbits are equivariantly diffeomorphic to the lens space $\S_{n}=\mathbb{Z}_{n} \backslash S^{2 m-1}$, where $\mathbb{Z}_{n}$ acts on $S^{2 m-1} \subset \mathbb{C}^{m}$ via $k \cdot z:=\mathrm{e}^{-i(2 k \pi / n)} z$, and
$$\begin{array}{ll}
M_{(1, n)}(\mathrm{G}, \mathrm{~K})=\mathbb{Z}_{n} \backslash S^{2 m-1} \times \mathbb{R}, & M_{(2, n)}(\mathrm{G}, \mathrm{~K})=\mathcal{O}_{\mathbb{C P}^{m-1}}(-n), \\
M_{(3, n)}(\mathrm{G}, \mathrm{~K})=\mathbb{Z}_{n} \backslash S^{2 m-1} \times S^{1}, & M_{(4, n)}(\mathrm{G}, \mathrm{~K})=\mathbb{P}\left(\mathcal{O}_{\mathbb{C P}^{m-1}} \oplus \mathcal{O}_{\mathbb{C P}^{m-1}}(-n)\right) .
\end{array}$$
Here, we denoted by $\mathcal{O}_{\mathbb{C P}^{m-1}}$ the trivial line bundle over $\mathbb{C P}^{m-1}$, by $\mathcal{O}_{\mathbb{C P}^{m-1}}(-1)$ the tautological line bundle and by $\mathcal{O}_{\mathbb{C P}^{m-1}}(-n):=\mathcal{O}_{\mathbb{C P}^{m-1}}(-1)^{\otimes n}$. In particular:
\begin{itemize}
\item[-] if $(i, n)=(3,1)$, then we get a diagonal Hopf manifold;
\item[-] if $(i, n)=(4,1)$, then we get the connected sum $\mathbb{C P}^{m} \# \overline{\mathbb{C P}}{ }^{m}$;
\item[-] if $m=2$ and $i=4$, then we get all the Hirzebruch surfaces.
\end{itemize}

Remark 3.9. Let us consider $P=\mathbb{C} \mathbb{P}^{m-1}$ and assume that $m \geqslant 3$. Since the isotropy representation of the odd sphere $\S_{1}=S^{2 m-1}=\operatorname{SU}(m) / \operatorname{SU}(m-1)$ is monotypic, all the cohomogeneity one Hermitian metrics on $\left(M_{(i, n)}(\mathrm{G}, \mathrm{K}), \mathcal{J}\right)$ are of
submersion type with respect to the fibration $M_{(i, n)}(\mathrm{G}, \mathrm{K}) \rightarrow \mathbb{C P}^{m-1}$. This fact does not hold true in general. For example, starting from the Grassmannian $P=\widetilde{\operatorname{Gr}}\left(2, \mathbb{R}^{m+1}\right)=\mathrm{SO}(m+1) /(\mathrm{SO}(2) \times \mathrm{SO}(m-1))$ of the oriented 2-planes in $\mathbb{R}^{m+1}$, we get that $\S_{1}=V\left(2, \mathbb{R}^{m+1}\right)=\operatorname{SO}(m+1) / \mathrm{SO}(m-1)$ is the Stiefel manifold of the orthonormal 2-frames in $\mathbb{R}^{m+1}$, whose isotropy representation contains two equivalent irreducible summands.

Remark 3.10. Note that, by means of the action of G, there is a bijective correspondence between the set of G-invariant smooth functions $\tilde{\varphi}: M_{(i, n)}(\mathrm{G}, \mathrm{K}) \rightarrow \mathbb{R}$ and the set of functions $\varphi: I \rightarrow \mathbb{R}$ satisfying the appropriate smoothness condition:
\begin{itemize}
\item[(i)] if $i=1, I=\mathbb{R}$ and $\varphi$ is smooth;
\item[(ii)] if $i=2, I=(0,+\infty)$ and $\varphi$ is the restriction of a smooth even function on $\mathbb{R}$;
\item[(iii)] if $i=3, \varphi$ is smooth and $S^{1}$-periodic;
\item[(iv)] if $i=4, I=(0, \pi)$ and $\varphi$ is the restriction of a smooth even function on $\mathbb{R}$ satisfying $\varphi(\pi+r)=\varphi(\pi-r)$.
\end{itemize}

From now on, any function $\varphi: I \rightarrow \mathbb{R}$ satisfying the appropriate smoothness condition will be called admissible.

Remark 3.11. Let $\mathrm{g}=\mathrm{g}(f, h)$ a cohomogeneity one, submersion-type metric on a manifold $\left(M_{(i, n)}(\mathrm{G}, \mathrm{K}), \mathcal{J}\right)$ and $\varphi: I \rightarrow \mathbb{R}$ a positive, admissible function. Then, the metric $\varphi^{2} g$ is still a cohomogeneity one, submersion-type metric on $\left(M_{(i, n)}(\mathrm{G}, \mathrm{K}), \Downarrow\right)$ and $\varphi^{2} \mathrm{~g}=\mathrm{g}\left(\hat{f}_{\varphi}, \hat{h}_{\varphi}\right)$, with
$$\hat{f}_{\varphi}(r):=\xi_{\varphi}^{\prime}\left(\xi_{\varphi}^{-1}(r)\right) f\left(\xi_{\varphi}^{-1}(r)\right), \quad \hat{h}_{\varphi}(r):=\xi_{\varphi}^{\prime}\left(\xi_{\varphi}^{-1}(r)\right) h\left(\xi_{\varphi}^{-1}(r)\right),$$
where $\xi_{\varphi}(r):=\int_{0}^{r} \varphi(t) \mathrm{d} t$. However we stress that, even if $\mathbb{g}$ is complete, in general the conformal metric $\varphi^{2} \mathbb{g}$ is not.

\subsection*{3.3. Curvature and torsion computations for Bérard-Bergery manifolds}

We begin this section by listing the Levi-Civita connection and the Riemannian Ricci tensor of the manifolds $\left(M_{(i, n)}(\mathrm{G}, \mathrm{K}), \mathrm{J}, \mathrm{g}\right)$. By straightforward computations, from proposition 3.1 and equations (3.10), (3.8) we get

Proposition 3.12. Let $X, Y, Z \in \mathfrak{p}$. Then
$$\begin{aligned}
\left.D_{Y^{*}} X^{*}\right|_{\gamma(r)} & =\frac{\lambda}{2}\left(Q(J X, Y) T_{\gamma(r)}^{*}-\frac{p}{m n} \frac{h(r) h^{\prime}(r)}{f(r)} Q(X, Y) N_{\gamma(r)}\right), \\
\left.D_{T^{*}} X^{*}\right|_{\gamma(r)} & =-\frac{2}{\lambda}\left(\frac{m n}{p}\right)^{2} \frac{f(r)^{2}}{h(r)^{2}}(J X)_{\gamma(r)}^{*},
\end{aligned}$$
$$\begin{aligned}
\left.D_{N} X^{*}\right|_{\gamma(r)} & =\frac{2 m n}{\lambda p} f(r) \frac{h^{\prime}(r)}{h(r)} X_{\gamma(r)}^{*}, \\
\left.D_{Y^{*}} T^{*}\right|_{\gamma(r)} & =\left(\lambda-\frac{2}{\lambda}\left(\frac{m n}{p}\right)^{2} \frac{f(r)^{2}}{h(r)^{2}}\right)(J Y)_{\gamma(r)}^{*}, \\
\left.D_{T^{*}} T^{*}\right|_{\gamma(r)} & =-\frac{2 m n}{\lambda p} f^{\prime}(r) N_{\gamma(r)}, \\
\left.D_{N} T^{*}\right|_{\gamma(r)} & =\frac{2 m n}{\lambda p} f^{\prime}(r) T_{\gamma(r)}^{*}, \\
\left.D_{Y^{*}} N\right|_{\gamma(r)} & =\frac{2 m n}{\lambda p} f(r) \frac{h^{\prime}(r)}{h(r)} Y_{\gamma(r)}^{*}, \\
\left.D_{T^{*}} N\right|_{\gamma(r)} & =\frac{2 m n}{\lambda p} f^{\prime}(r) T_{\gamma(r)}^{*}, \\
\left.D_{N} N\right|_{\gamma(r)} & =\frac{2 m n}{\lambda p} f^{\prime}(r) N_{\gamma(r)} .
\end{aligned}$$
Moreover, from [27, proposition 1.14], we directly obtain
Proposition 3.13. Let $X \in \mathfrak{p}$ with $Q(X, X)=1$. Then the Riemannian Ricci tensor is given by
$$\begin{aligned}
\operatorname{Ric}(g)(N, N)_{\gamma(r)}= & \frac{2 m(m-1) n^{2}}{p^{2}} f(r)^{2}\left(-\frac{f^{\prime \prime}(r)}{f(r)}-2(m-1) \frac{h^{\prime \prime}(r)}{h(r)}\right), \\
\operatorname{Ric}(g)\left(T^{*}, T^{*}\right)_{\gamma(r)}= & \frac{2 m(m-1) n^{2}}{p^{2}} f(r)^{2}\left(-\frac{f^{\prime \prime}(r)}{f(r)}-2(m-1) \frac{f^{\prime}(r)}{f(r)} \frac{h^{\prime}(r)}{h(r)}\right. \\
& \left.+2(m-1)\left(\frac{m n}{p}\right)^{2} \frac{f(r)^{2}}{h(r)^{4}}\right), \\
\operatorname{Ric}(g)\left(X^{*}, X^{*}\right)_{\gamma(r)}= & h(r)^{2}\left(-\frac{h^{\prime \prime}(r)}{h(r)}-\frac{f^{\prime}(r)}{f(r)} \frac{h^{\prime}(r)}{h(r)}-(2 m-3) \frac{h^{\prime}(r)^{2}}{h(r)^{2}}\right. \\
& \left.-2\left(\frac{m n}{p}\right)^{2} \frac{f(r)^{2}}{h(r)^{4}}+\frac{2 m}{h(r)^{2}}\right)
\end{aligned}$$
and
$$\operatorname{Ric}(\mathbb{g})\left(N, T^{*}\right)_{\gamma(r)}=\operatorname{Ric}(\mathbb{g})\left(N, X^{*}\right)_{\gamma(r)}=\operatorname{Ric}(\mathbb{g})\left(T^{*}, X^{*}\right)_{\gamma(r)}=0 .$$
Furthermore, the Riemannian scalar curvature is
$$\begin{aligned}
\operatorname{scal}(\operatorname{g})(r)= & -2 \frac{f^{\prime \prime}(r)}{f(r)}-4(m-1) \frac{h^{\prime \prime}(r)}{h(r)}-4(m-1) \frac{f^{\prime}(r)}{f(r)} \frac{h^{\prime}(r)}{h(r)} \\
& -2(m-1)(2 m-3) \frac{h^{\prime}(r)^{2}}{h(r)^{2}}+\frac{4 m(m-1)}{h(r)^{2}}-2(m-1)\left(\frac{m n}{p}\right)^{2} \frac{f(r)^{2}}{h(r)^{4}} .
\end{aligned}$$

We compute now the Chern connection and the Chern-Ricci tensors of the manifolds $\left(M_{(i, n)}(\mathrm{G}, \mathrm{K}), \mathrm{J}, \mathrm{g}\right)$. From proposition 3.3 and equations (3.10), (3.8) we get

Proposition 3.14. Let $X, Y, Z \in \mathfrak{p}$. Then
$$\begin{aligned}
\left.\nabla_{Y^{*}} X^{*}\right|_{\gamma(r)} & =\frac{\lambda}{2}\left(Q(J X, Y) T_{\gamma(r)}^{*}+Q(X, Y) N_{\gamma(r)}\right), \\
\left.\nabla_{T^{*}} X^{*}\right|_{\gamma(r)} & =\frac{2 m n}{\lambda p} f(r) \frac{h^{\prime}(r)}{h(r)}(J X)_{\gamma(r)}^{*}, \\
\left.\nabla_{N} X^{*}\right|_{\gamma(r)} & =\frac{2 m n}{\lambda p} f(r) \frac{h^{\prime}(r)}{h(r)} X_{\gamma(r)}^{*}, \\
\left.\nabla_{Y^{*}} T^{*}\right|_{\gamma(r)} & =\left(\lambda-\frac{2}{\lambda}\left(\frac{m n}{p}\right)^{2} \frac{f(r)^{2}}{h(r)^{2}}\right)(J Y)_{\gamma(r)}^{*}, \\
\left.\nabla_{T^{*}} T^{*}\right|_{\gamma(r)} & =-\frac{2 m n}{\lambda p} f^{\prime}(r) N_{\gamma(r)}, \\
\left.\nabla_{N} T^{*}\right|_{\gamma(r)} & =\frac{2 m n}{\lambda p} f^{\prime}(r) T_{\gamma(r)}^{*}, \\
\left.\nabla_{Y^{*}} N\right|_{\gamma(r)} & =-\frac{2}{\lambda}\left(\frac{m n}{p}\right)^{2} \frac{f(r)^{2}}{h(r)^{2}} Y_{\gamma(r)}^{*}, \\
\left.\nabla_{T^{*}} N\right|_{\gamma(r)} & =\frac{2 m n}{\lambda p} f^{\prime}(r) T_{\gamma(r)}^{*}, \\
\left.\nabla_{N} N\right|_{\gamma(r)} & =\frac{2 m n}{\lambda p} f^{\prime}(r) N_{\gamma(r)} .
\end{aligned}$$

We are ready to state the following proposition, whose proof will be given in Appendix A.

Proposition 3.15. Let $X \in \mathfrak{p}$ with $Q(X, X)=1$.
\begin{itemize}
\item[(a)] The first Chern-Ricci tensor verifies
$$\begin{aligned}
& \operatorname{Ric}^{\operatorname{Ch}[1]}(\mathrm{g})\left(T^{*}, T^{*}\right)_{\gamma}(r) \\
& \quad=\frac{2 m(m-1) n^{2}}{p^{2}} f(r)^{2} \\
& \quad \times\left(-\frac{f^{\prime \prime}(r)}{f(r)}+(m-1)\left(-\frac{h^{\prime \prime}(r)}{h(r)}+\frac{h^{\prime}(r)^{2}}{h(r)^{2}}-\frac{f^{\prime}(r)}{f(r)} \frac{h^{\prime}(r)}{h(r)}\right)\right), \\
& \operatorname{Ric}^{\operatorname{Ch}[1]}(\operatorname{g})\left(X^{*}, X^{*}\right)_{\gamma(r)} \\
& =h(r)^{2}\left(\frac{2 m n}{p} \frac{f(r)}{h(r)^{2}}\left(\frac{f^{\prime}(r)}{f(r)}+(m-1) \frac{h^{\prime}(r)}{h(r)}\right)+\frac{2 m}{h(r)^{2}}\right) .
\end{aligned}$$
\end{itemize}
\begin{itemize}
\item[(b)] The second Chern-Ricci tensor verifies
$$\begin{aligned}
& \operatorname{Ric}^{\mathrm{Ch}[2]}(\mathrm{g})\left(T^{*}, T^{*}\right)_{\gamma(r)} \\
& \quad=\frac{2 m(m-1) n^{2}}{p^{2}} f(r)^{2} \\
& \quad \times\left(-\frac{f^{\prime \prime}(r)}{f(r)}+\frac{2 m(m-1) n}{p} \frac{f^{\prime}(r)}{h(r)^{2}}+\frac{2 m^{2}(m-1) n^{2}}{p^{2}} \frac{f(r)^{2}}{h(r)^{4}}\right), \\
& \operatorname{Ric}^{\mathrm{Ch}[2]}(\mathrm{g})\left(X^{*}, X^{*}\right)_{\gamma(r)} \\
& \quad=h(r)^{2}\left(-\frac{h^{\prime \prime}(r)}{h(r)}+\frac{h^{\prime}(r)^{2}}{h(r)^{2}}-\frac{f^{\prime}(r)}{f(r)} \frac{h^{\prime}(r)}{h(r)}+\frac{2 m(m-1) n}{p} f(r) \frac{h^{\prime}(r)}{h(r)^{3}}\right. \\
& \left.\quad-2\left(\frac{m n}{p}\right)^{2} \frac{f(r)^{2}}{h(r)^{4}}+\frac{2 m}{h(r)^{2}}\right) .
\end{aligned}$$
\item[(c)] Both the Chern-Ricci tensors satisfy
$$\begin{aligned}
\operatorname{Ric}^{\operatorname{Ch}[i]}(\mathrm{g})(N, N)_{\gamma(r)} & =\operatorname{Ric}^{\operatorname{Ch}[\mathrm{i}]}(\mathrm{g})\left(T^{*}, T^{*}\right)_{\gamma(r)}, \\
\operatorname{Ric}^{\operatorname{Ch}[\mathrm{i}]}(\mathrm{g})\left(N, T^{*}\right)_{\gamma(r)} & =\operatorname{Ric}^{\operatorname{Ch}[\mathrm{i}]}(\mathrm{g})\left(N, X^{*}\right)_{\gamma(r)}=\operatorname{Ric}^{\operatorname{Ch}[\mathrm{i}]}(\mathrm{g})\left(T^{*}, X^{*}\right)_{\gamma(r)}=0 .
\end{aligned}$$
\item[(d)] The Chern-scalar curvature is given by
$$\begin{aligned}
\operatorname{scal}^{\mathrm{Ch}}(\mathrm{~g})(r)= & -2 \frac{f^{\prime \prime}(r)}{f(r)}-2(m-1) \frac{h^{\prime \prime}(r)}{h(r)}+2(m-1) \\
& \times\left(\frac{h^{\prime}(r)}{h(r)}-\frac{f^{\prime}(r)}{f(r)}\right) \frac{h^{\prime}(r)}{h(r)}+4 m(m-1) \frac{1}{h(r)^{2}} \\
& +\frac{4 m(m-1) n}{p}\left(f^{\prime}(r)+(m-1) f(r) \frac{h^{\prime}(r)}{h(r)}\right) \frac{1}{h(r)^{2}} .
\end{aligned}$$
\end{itemize}

Given proposition 3.15, we are now able to study the second-Chern-Einstein equations and the constant Chern-scalar curvature equation for this special class of Hermitian cohomogeneity one manifolds. This will be done in §5.

Finally, we recall that the torsion $\tau$ of the Chern connection is given by
$$-2 \mathrm{~g}(\tau(A, B), C)=\mathrm{d} \omega(Л A, B, C)+\mathrm{d} \omega(A, \Downarrow B, C)$$
and that its trace $\vartheta(A):=\operatorname{Tr}(\tau(A, \cdot))$ is called Lee form. We recall that it satisfies $\mathrm{d} \omega^{m-1}=\vartheta \wedge \omega^{m-1}$, see [23, p 500].

From proposition 3.2 and formulas (3.8), (3.10) we obtain

Corollary 3.16. Let $X, Y, Z \in \mathfrak{p}$. Then
$$\mathrm{d} \omega\left(X^{*}, Y^{*}, N\right)_{\gamma(r)}=\frac{4 m n}{\lambda p} f(r)\left(h(r) h^{\prime}(r)+\frac{m n}{p} f(r)\right) \rho(X, Y),$$
where $\rho(X, Y):=Q_{\mathfrak{p}}(J X, Y)$ is the G-invariant Kähler-Einstein form on $P$, and
$$\mathrm{d} \omega\left(X^{*}, Y^{*}, Z^{*}\right)_{\gamma(r)}=\mathrm{d} \omega\left(X^{*}, Y^{*}, T^{*}\right)_{\gamma(r)}=\mathrm{d} \omega\left(X^{*}, T^{*}, N\right)_{\gamma(r)}=0 .$$
and, by consequence
Proposition 3.17. Let $X, Y \in \mathfrak{p}$. Then it holds $\tau\left(N, T^{*}\right)_{\gamma(r)}=\tau\left(X^{*}, Y^{*}\right)_{\gamma(r)}=0$ and
$$\begin{aligned}
\tau\left(N, X^{*}\right)_{\gamma(r)} & =\frac{2 m n}{\lambda p} \frac{f(r)}{h(r)^{2}}\left(h(r) h^{\prime}(r)+\frac{m n}{p} f(r)\right) X_{\gamma(r)}^{*}, \\
\tau\left(T^{*}, X^{*}\right)_{\gamma(r)} & =\frac{2 m n}{\lambda p} \frac{f(r)}{h(r)^{2}}\left(h(r) h^{\prime}(r)+\frac{m n}{p} f(r)\right)(J X)_{\gamma(r)}^{*} .
\end{aligned}$$
Moreover, the Lee form $\vartheta$ satisfies
$$\vartheta(N)_{\gamma(r)}=\frac{4 m(m-1) n}{\lambda p} \frac{f(r)}{h(r)^{2}}\left(h(r) h^{\prime}(r)+\frac{m n}{p} f(r)\right)$$
and $\vartheta\left(T^{*}\right)_{\gamma(r)}=\vartheta\left(X^{*}\right)_{\gamma(r)}=0$.
As a direct consequence of proposition 3.17, whose proof will be given in Appendix A, we get the following

Corollary 3.18. For any $A, B \in \Gamma(T M)$, it holds that
$$2(m-1) \tau(A, B)=(\vartheta(A) B-\vartheta(B) A)-(\vartheta(\triangle A) \Downarrow B-\vartheta(\triangle B) \cup A) .$$

\section*{4. Special Hermitian metrics on Bérard-Bergery manifolds}

In this section, we investigate the existence of special non-Kähler Hermitian metrics, such as balanced, pluriclosed, locally conformally Kähler, Vaisman and Gauduchon, on the Bérard-Bergery standard cohomogeneity one Hermitian manifolds. In particular, we prove theorems A and B.
4.1. Proof of theorem A

We begin by pointing out the following
Proposition 4.1. All the cohomogeneity one Hermitian metrics g of submersion-type on the complex manifold $\left(M_{(i, n)}(\mathrm{G}, \mathrm{K}), J^{\prime}\right)$ are locally conformally Kähler.

Proof. By [19, corollary 1.1], we know that g is locally conformally Kähler if and only if the complex structure I is parallel with respect to the Weyl connection associated with $\left(\mathrm{g}, \frac{1}{m-1} \vartheta\right)$, equivalently, the following is satisfied:
$$D_{A} \downharpoonleft B-\Im D_{A} B=\frac{1}{2(m-1)}\left(\vartheta(Л B) A-\vartheta(B) \downharpoonleft A+\mathrm{g}(A, B) \sqrt{ } \vartheta^{\#}+\mathrm{g}(Л A, B) \vartheta^{\#}\right)$$
for any $A, B \in \Gamma(T M)$, where $\vartheta^{\#} \in \Gamma(T M)$ is defined by the relation $\mathrm{g}\left(\vartheta^{\#}, \cdot\right)=\vartheta$. By using equations (2.1) and (3.16), a straightforward computation shows that the above equation is equivalent to equation (3.18). Indeed, for any $C \in \Gamma(T M)$,
$$\begin{aligned}
\mathfrak{g} & \left(D_{A} Л B-\sqrt{ } D_{A} B, C\right) \\
= & \left.\left.\mathfrak{g}\left(\nabla_{A} Л B, C\right)+\mathfrak{g}\left(\nabla_{A} B, Л_{C}\right)+\frac{1}{2} \mathrm{~d} \omega( \lrcorner A, \Downarrow B, C\right)+\frac{1}{2} \mathrm{~d} \omega( \lrcorner A, B, \Downarrow C\right) \\
= & -\mathfrak{g}\left(\tau(B, C), J_{A}\right) \\
= & \left.\left.\left.\left.\left.\frac{1}{2(m-1)} \mathfrak{g}( \lrcorner A,(\vartheta( \lrcorner B)\right\lrcorner C-\vartheta( \lrcorner C\right)\right\lrcorner B\right)-(\vartheta(B) C-\vartheta(C) B)\right) \\
= & \left.\frac{1}{2(m-1)} \mathfrak{g}(\vartheta( \lrcorner B) \mathfrak{g}(A, C)-\vartheta(B) \mathfrak{g}( \lrcorner A, C\right)+\mathfrak{g}(A, B) \mathfrak{g}\left(J^{*} \vartheta^{\#}, C\right) \\
& \left.+\mathfrak{g}( \lrcorner A, B) \mathfrak{g}\left(\vartheta^{\#}, C\right)\right) \\
= & \left.\left.\left.\frac{1}{2(m-1)} \mathfrak{g}(\vartheta( \lrcorner B) A-\vartheta(B)\right\lrcorner A+\mathfrak{g}(A, B) J^{\#}+\mathfrak{g}( \lrcorner A, B\right) \vartheta^{\#}, C\right),
\end{aligned}$$
which shows the above mentioned equivalence. \(\square\)

Corollary 4.2. Let $\left(M_{(i, n)}(\mathrm{G}, \mathrm{K}), ~ \mathfrak{J}, \mathbb{g}\right)$ be a Bérard-Bergery standard cohomogeneity one Hermitian manifold. Then, $\mathfrak{g}$ is strictly locally conformally Kähler if and only if $i=3$.

Proof. Since the complex manifolds $\left(M_{(2, n)}(\mathrm{G}, \mathrm{K}), J^{\prime}\right)$ and $\left(M_{(4, n)}(\mathrm{G}, \mathrm{K}), \mathcal{J}\right)$ are simply connected, any closed 1-form on them is necessarily exact. Moreover, by remark 3.6, it holds that $b_{1}\left(M_{(1, n)}(\mathrm{G}, \mathrm{K})\right)=0$. Therefore, any locally conformally Kähler metrics on them are necessarily globally conformally Kähler. Finally, by using again remark 3.6, the complex manifolds $\left(M_{(3, n)}(\mathrm{G}, \mathrm{K}), J\right)$ do not admit any Kähler metric. \(\square\)

Let now $\mathfrak{g}$ be a cohomogeneity one, submersion-type Hermitian metric on a complex manifold $\left(M_{(i, n)}(\mathrm{G}, \mathrm{K})\right.$, J). By proposition 4.1, it follows that $\mathrm{d} \omega=\frac{1}{m-1} \vartheta \wedge \omega$ which in turn implies that $\mathcal{L}_{A} \vartheta=0$ for any holomorphic Killing vector field $A \in$ $\Gamma(T M)$. Hence, by equations (3.1), (3.10) and proposition 3.12, the non-vanishing
components of the Levi-Civita covariant derivative of $\vartheta$ are
$$\begin{aligned}
\left(D_{N} \vartheta\right)(N)_{\gamma(r)} & =\frac{2 m n}{\lambda p}\left(f(r) \frac{\partial}{\partial r}\left(\vartheta(N)_{\gamma(r)}\right)-f^{\prime}(r) \vartheta(N)_{\gamma(r)}\right), \\
\left(D_{T^{*}} \vartheta\right)\left(T^{*}\right)_{\gamma(r)} & =\frac{2 m n}{\lambda p} f^{\prime}(r) \vartheta(N)_{\gamma(r)}, \\
\left(D_{Y^{*}} \vartheta\right)\left(X^{*}\right)_{\gamma(r)} & =\frac{\lambda p}{2 m n} \frac{h(r) h^{\prime}(r)}{f(r)} Q(X, Y) \vartheta(N)_{\gamma(r)},
\end{aligned}$$
where $\lambda$ is given by equation (3.9). By corollary 4.2, the complex manifolds $\left(M_{(1, n)}(\mathrm{G}, \mathrm{K}), \Downarrow\right),\left(M_{(2, n)}(\mathrm{G}, \mathrm{K}), \mathcal{J}\right)$ and $\left(M_{(4, n)}(\mathrm{G}, \mathrm{K}), J\right)$ cannot admit cohomogeneity one, Hermitian metric of submersion-type that are Vaisman. Moreover, from equation (4.1), we get

Proposition 4.3. A cohomogeneity one Hermitian metric $\mathbb{g}$ of submersion-type on the complex manifolds $\left(M_{(3, n)}(\mathrm{G}, \mathrm{K}), \Downarrow\right)$ is Vaisman if and only if both $f, h$ are constant.

Proof. The if part is immediate. Indeed, since $\vartheta$ is necessarily non-exact, if both $f$ and $h$ are constant, then by equations (3.17) and (4.1) it follows that $D \vartheta=0$.

Conversely, assume that $D \vartheta=0$. Note that either $\vartheta(N)_{\gamma\left(r_{\mathrm{o}}\right)}=0$ for some $r_{\mathrm{o}} \in I$, or $\vartheta(N)_{\gamma(r)}$ is nowhere vanishing. In the former case, the first equation in (4.1) yields that $\vartheta(N)_{\gamma(r)}$ is constantly zero. In fact, one gets that $\vartheta=0$, that is, $\mathbb{g}$ is Kähler. In particular, if $\mathbb{g}$ is Vaisman, then the above observation implies that $D \vartheta=0$ and $\vartheta(N)_{\gamma(r)}$ is nowhere vanishing. Hence, equations (4.1) immediately imply that $f$ and $h$ are constant. \(\square\)

Finally, we note that the manifolds $\left(M_{(1, n)}(\mathrm{G}, \mathrm{K}), J^{\prime}\right)$ (respectively $\left(M_{(3, n)}\right.$ $(\mathrm{G}, \mathrm{K}), \complement)$ ) are acted transitively by the larger group $\mathrm{G} \times \mathbb{R}$ (respectively $\mathrm{G} \times \mathrm{U}(1)$ ), and any metric $\mathrm{g}=\mathrm{g}(f, h)$ is invariant under this action if and only if the functions $f$ and $h$ are constant. This completes the proof of theorem A.

Remark 4.4. By propositions 4.1 and 4.3, the compact complex manifolds $\left(M_{(3, n)}(\mathrm{G}, \mathrm{K})\right.$, J) admit cohomogeneity one, strictly locally conformally Kähler metrics that are non-Vaisman. Remarkably, in the homogeneous case, this is excluded by [25, 29]. We stress that the Hopf manifold, which is the main example of Vaisman manifold [44], corresponds, in our notation, to $\left(M_{(3,1)}(\mathrm{G}, \mathrm{K}), J^{0}\right)$ with $\mathrm{G}=\mathrm{SU}(m)$ and $\mathrm{K}=\mathrm{S}(\mathrm{U}(1) \times \mathrm{U}(m-1))$, see example 3.8.

Remark 4.5. The locally conformally Kähler metrics by proposition 4.1 include the globally conformally Kähler, Einstein metrics by Bérard-Bergery [9, théorème 1.10]. We also recall that Einstein, locally conformally Käher, non-Kähler metrics are completed classified by [18, 36, 38], and they are either the Einstein, globally conformally Kähler metrics by [9], or they are defined on $\mathbb{C P}^{2}$ by blowing up one or two points.

\subsection*{4.2. Proof of theorem B}

We begin by characterizing the Gauduchon condition as follows.

Proposition 4.6. A cohomogeneity one Hermitian metric $\mathbb{g}$ of submersion-type on the complex manifolds $\left(M_{(i, n)}(\mathrm{G}, \mathrm{K}), \mathcal{J}\right)$ is Gauduchon if and only if it satisfies
$$\left(h(r) h^{\prime}(r)+\frac{m n}{p} f(r)\right) f(r) h(r)^{2(m-2)}=k \quad \text { for some } k \in \mathbb{R} .$$
Moreover, if $\left(M_{(i, n)}(\mathrm{G}, \mathrm{K}), \complement\right)$ has singular orbits, then $\mathfrak{g}$ is Gauduchon if and only if it is Kähler.

Proof. Let $\left(\tilde{e}_{\alpha}\right)$ be a $Q_{\mathfrak{p}}$-orthonormal basis for $\mathfrak{p}$. Then, a straightforward computation based on equation (4.1) yields
$$\begin{aligned}
\mathrm{d}^{*} \vartheta(r)= & -\left(\frac{\lambda p}{2 m n}\right)^{2} f(r)^{-2}\left(D_{N} \vartheta\right)(N)_{\gamma(r)} \\
& -\left(\frac{\lambda p}{2 m n}\right)^{2} f(r)^{-2}\left(D_{T^{*}} \vartheta\right)\left(T^{*}\right)_{\gamma(r)}-h(r)^{-2} \sum_{\alpha=1}^{2(m-1)}\left(D_{\tilde{e}_{\alpha}^{*}} \vartheta\right)\left(\tilde{e}_{\alpha}^{*}\right)_{\gamma(r)} \\
= & -\frac{\lambda p}{2 m n} f(r)^{-1} \frac{\partial}{\partial r}\left(\vartheta(N)_{\gamma(r)}\right)-(m-1) \frac{\lambda p}{m n} \frac{h^{\prime}(r)}{f(r) h(r)} \vartheta(N)_{\gamma(r)} \\
= & 2(m-1) \frac{1}{h(r)^{2}}\left(\left(h(r) h^{\prime}(r)+\frac{m n}{p} f(r)\right)\left(\frac{f^{\prime}(r)}{f(r)}+2(m-2) \frac{h^{\prime}(r)}{h(r)}\right)\right. \\
& \left.+\left(h(r) h^{\prime \prime}(r)+h^{\prime}(r)^{2}+\frac{m n}{p} f^{\prime}(r)\right)\right)
\end{aligned}$$
and so g is Gauduchon if and only if
$$\begin{aligned}
& \left(h(r) h^{\prime}(r)+\frac{m n}{p} f(r)\right)\left(\frac{f^{\prime}(r)}{f(r)}+2(m-2) \frac{h^{\prime}(r)}{h(r)}\right) \\
& \quad+\left(h(r) h^{\prime \prime}(r)+h^{\prime}(r)^{2}+\frac{m n}{p} f^{\prime}(r)\right)=0 .
\end{aligned}$$
Since $f(r), h(r)$ are positive for any $r \in I$ and
$$\begin{aligned}
& \frac{1}{f(r) h(r)^{2(m-2)}} \frac{\mathrm{d}}{\mathrm{~d} r}\left(\left(h(r) h^{\prime}(r)+\frac{m n}{p} f(r)\right) f(r) h(r)^{2(m-2)}\right) \\
& \quad=\left(h(r) h^{\prime}(r)+\frac{m n}{p} f(r)\right)\left(\frac{f^{\prime}(r)}{f(r)}+2(m-2) \frac{h^{\prime}(r)}{h(r)}\right) \\
& \quad+\left(h(r) h^{\prime \prime}(r)+h^{\prime}(r)^{2}+\frac{m n}{p} f^{\prime}(r)\right),
\end{aligned}$$
it follows that $\mathfrak{g}$ is Gauduchon if and only if equation (4.2) is satisfied.
Let us assume now that $\left(M_{(i, n)}(\mathrm{G}, \mathrm{K}), \sqrt{ }\right)$ has a singular orbit, that is $i=2$ or $i=4$. Then, the smoothness conditions at $r=0$ imply that $k=0$ in equation (4.2). Therefore, in this case, $g$ is Gauduchon if and only if it is Kähler. \(\square\)

Since the balanced condition is equivalent to $\vartheta=0$, from proposition 3.17 and equation (3.11) we immediately get

Corollary 4.7. A cohomogeneity one Hermitian metric $\mathfrak{g}$ of submersion-type on the complex manifolds $\left(M_{(i, n)}(\mathrm{G}, \mathrm{K}), \Downarrow\right)$ is balanced if and only if it is Kähler.

Remark 4.8. In particular, in view of [58, theorem 1.3], in the non-Kähler case, both the Levi-Civita and the Chern connections cannot be Kähler-like in the sense of [26, 58], namely, they do not satisfy the same symmetries as in the Kähler case.

Concerning the pluriclosed condition, a tedious but straightforward computation (see Appendix A) shows that
$$\operatorname{dd}^{c} \omega\left(X^{*}, Y^{*}, Z^{*}, W^{*}\right)_{\gamma(r)}=4 \frac{m n}{p} f(r)\left(h(r) h^{\prime}(r)+\frac{m n}{p} f(r)\right)(\rho \wedge \rho)(X, Y, Z, W),$$
where $\rho(X, Y)=Q_{\mathfrak{p}}(J X, Y)$ is again the G-invariant Kähler-Einstein form on $P$. Hence, together with equation (3.11), this proves the following

Corollary 4.9. A cohomogeneity one Hermitian metric $\mathfrak{g}$ of submersion-type on the complex manifolds $\left(M_{(i, n)}(\mathrm{G}, \mathrm{K}), \Downarrow\right)$ is pluriclosed if and only if it is Kähler.
which completes the proof of theorem B.

\section*{5. Constant Chern-scalar curvature and second-Chern-Einstein metrics}

In this section, we investigate the existence of second-Chern-Einstein metrics and of metrics with constant Chern-scalar curvature on the Bérard-Bergery standard cohomogeneity one Hermitian manifolds. In particular, we first prove a local existence and uniqueness result for second-Chern-Einstein metrics with prescribed Chern-scalar curvature. Then, we prove theorems C and D.

\subsection*{5.1. The second-Chern-Einstein equations}
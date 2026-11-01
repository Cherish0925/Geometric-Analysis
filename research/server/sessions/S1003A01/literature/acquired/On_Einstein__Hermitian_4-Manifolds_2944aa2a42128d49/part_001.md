---
retention_scope: session
part: 1
total_parts: 3
---

[Part 1/3 of: On Einstein, Hermitian 4-Manifolds]

---
source_file: 1010_0238.pdf
converter: mathpix
format: mmd
---

\title{
On Einstein, Hermitian 4-Manifolds
}

\author{
Claude LeBrun* \\ SUNY Stony Brook
}

\begin{abstract}
Let $(M, h)$ be a compact 4-dimensional Einstein manifold, and suppose that $h$ is Hermitian with respect to some complex structure $J$ on $M$. Then either $(M, J, h)$ is Kähler-Einstein, or else, up to rescaling and isometry, it is one of the following two exceptions: the Page metric on $\mathbb{C P}_{2} \# \overline{\mathbb{C P}}_{2}$, or the Einstein metric on $\mathbb{C P}_{2} \# 2 \overline{\mathbb{C P}}_{2}$ discovered in [8].
\end{abstract}

\section*{1 Introduction}

Recall [4] that a Riemannian metric is said to be Einstein if it has constant Ricci curvature. A central problem of modern Riemannian geometry is to determine which smooth compact manifolds admit Einstein metrics, and to precisely understand the moduli space of these metrics when they do exist.

The theory of Kähler-Einstein metrics provides the richest currently available source for Einstein metrics on compact manifolds. This story becomes particularly compelling in real dimension 4, not only because of the mature state of the theory of Kähler-Einstein metrics on compact complex surfaces [2, 27, 28, 29, 30], but also because gauge-theoretic phenomena unique to this dimension sometimes allow one to show [16, 17] that every Einstein metric on certain smooth compact 4-manifolds must actually be Kähler-Einstein.

In fact, there are, up to rescaling and isometries, only two known examples of Einstein metrics on compact complex surfaces which are not Kähler. The older and better-known of these is the Page metric [25] on $\mathbb{C P}_{2} \# \overline{\mathbb{C P}}_{2}$. The second, of more recent provenance [8], is a metric on $\mathbb{C P}_{2} \# 2 \overline{\mathbb{C P}}_{2}$ discovered by the present author in collaboration with Xiuxiong Chen and Brian Weber; for

\footnotetext{
*Supported in part by NSF grant DMS-0905159.
}
a somewhat different proof, see [19]. Both the of these metrics have holonomy $S O(4)$, and so are non-Kähler in the most definitive, intrinsic sense. However, both are nonetheless conformally Kähler, in the sense that each is obtained from some Kähler metric by multiplying by a smooth positive function. In particular, both are Hermitian metrics on compact complex surfaces. The purpose of this article is prove that, up to homothety, no other other such examples can exist:

Theorem A Let $\left(M^{4}, J\right)$ be a compact complex surface, and suppose that $h$ is an Einstein metric on $M$ which is Hermitian with respect to $J$, in the sense that $h(\cdot, \cdot)=h(J \cdot, J \cdot)$. Then either
\begin{itemize}
\item[-] (M, $J, h$ ) is Kähler-Einstein; or
\item[-] $M \approx \mathbb{C P}_{2} \# \overline{\mathbb{C P}}_{2}$, and $h$ is a constant times the Page metric; or
\item[-] $M \approx \mathbb{C P}_{2} \# 2 \overline{\mathbb{C P}}_{2}$ and $h$ is a constant times the metric of [8].
\end{itemize}

In [18], the present author previously proved a tantalizing partial result in this direction:

Proposition 1 Let $\left(M^{4}, J\right)$ be a compact complex surface, and suppose that $h$ is an Einstein metric on $M$ which is Hermitian with respect to $J$. Then $h$ is conformal to a $J$-compatible Kähler metric $g$. Moreover, if $h$ is not itself Kähler, then
\begin{itemize}
\item[-] $(M, J)$ has $c_{1}>0$;
\item[-] $M \approx \mathbb{C P}_{2} \# k \overline{\mathbb{C P}}_{2}, k=1,2,3$;
\item[-] h has positive Einstein constant;
\item[-] $g$ is an extremal Kähler metric;
\item[-] $g$ has scalar curvature $s>0$; and
\item[-] after suitable normalization, $h=s^{-2} g$.
\end{itemize}
Moreover, the isometry group of $(M, h)$ contains a 2-torus.

The proof of this assertion consists of three main steps. First, the Riemannian Goldberg-Sachs Theorem [1, 14, 15, 26] implies that the self-dual Weyl curvature $W_{+}$has a repeated eigenvalue at each point. If $h$ is not itself Kähler, a result of Derdziński [11, Theorem 2] then implies that this Einstein metric can be written as $h=s^{-2} g$ for an extremal Kähler metric $g$ with non-constant positive scalar curvature $s$. Finally, if $\rho$ denotes the Ricci form of $g$, one can show [18, Proposition 2] that $\rho+2 i \partial \bar{\partial} \log s$ is a positive (1,1)form. Hence $c_{1}>0$, and $(M, J)$ is a Del Pezzo surface. Since $M$ moreover admits an extremal Kähler metric of non-constant scalar curvature, its Lie algebra of holomorphic vector fields must be both non-trivial and non-semisimple. The classification of Del Pezzo surfaces [10, 23] therefore implies that $M$ must be the blow-up of $\mathbb{C P}_{2}$ at one, two, or three points general position.

For the one-point blow-up, the Page metric is the only possibility [18]. Indeed, for any extremal Kähler metric on a compact complex manifold, the the identity component of the isometry group is necessarily [6, Theorem 3] a maximal compact subgroup of the identity component of the complex automorphism group. If $M=\mathbb{C P}_{2} \# \overline{\mathbb{C P}}_{2}$, and if $g$ is a conformally Einstein Kähler metric on $M$, it then follows that $\operatorname{Iso}_{0}(M, g) \cong U(2)$. But since $\operatorname{Iso}_{0}(M, g)$ automatically preserves the scalar curvature $s$, it also acts isometrically on the Einstein metric $h=s^{-2} g$. Thus $h$ is a cohomogeneity-one Einstein metric, and the work of Bérard Bergery [3, Théorème 1.8] then shows that it must actually be a constant times the Page metric.

Unfortunately, the remaining cases of $M=\mathbb{C P}_{2} \# 2 \overline{\mathbb{C P}}_{2}$ and $\mathbb{C P}_{2} \# 3 \overline{\mathbb{C P}}_{2}$ are not amenable to elementary arguments of this flavor. Instead, this article will prove the following pair of results by a variational method:

Theorem B Modulo rescalings and biholomorphisms, there is exactly one conformally Kähler, Einstein metric $h$ on $M=\mathbb{C P}_{2} \# 2 \overline{\mathbb{C P}}_{2}$. This metric coincides with the metric of [8], and is characterized by the fact that the conformally related Kähler metric $g$ minimizes the $L^{2}$-norm of the scalar curvature among all Kähler metrics on $M$.

Theorem C Modulo rescalings and biholomorphisms, there is only one conformally Kähler, Einstein metric $h$ on $M=\mathbb{C P}_{2} \# 3 \overline{\mathbb{C P}}_{2}$. This metric is actually Kähler-Einstein, and is exactly the metric discovered by Siu [27].

Our approach stems from the study of the squared $L^{2}$-norm
$$\mathcal{C}(g)=\int_{M} s_{g}^{2} d \mu_{g}$$
of the scalar curvature, restricted to the space of Kähler metrics. An even more restricted version of this problem was introduced by Calabi [5], who constrained $g$ to only vary in a fixed Kähler class $[\omega] \in H^{2}(M, \mathbb{R})$. Calabi called the critical metrics of his restricted problem extremal Kähler metrics, and showed that the relevant Euler-Lagrange equations are equivalent to requiring that $\nabla^{1,0} s$ be a holomorphic vector field. In fact, every extremal Kähler metric turns out to be an absolute minimizer for the Calabi problem, and the proof of this [7] moreover implies that any Kähler metric $g$ with Kähler class $[\omega]=\Omega$ satisfies the sharp estimate
$$\mathcal{C}(g) \geq 32 \pi^{2} \mathcal{A}(\Omega),$$
where
$$\mathcal{A}(\Omega):=\frac{\left(c_{1} \cdot \Omega\right)^{2}}{\Omega^{2}}+\frac{1}{32 \pi^{2}}\|\mathfrak{F}(\Omega)\|^{2},$$
and where equality occurs iff $g$ is an extremal Kähler metric. Here
$$\mathfrak{F}(\Omega): H^{0}\left(M, \mathcal{O}\left(T^{1,0} M\right)\right) \rightarrow \mathbb{C}$$
denotes the Futaki invariant, and the relevant norm is the one induced by the $L^{2}$-norm on the space of holomorphy potentials [13]. In particular, for any extremal Kähler metric $g$ with Kähler class $\Omega$, one has
$$\begin{aligned}
\int_{M} s_{0}^{2} d \mu_{g} & =32 \pi^{2} \frac{\left(c_{1} \cdot \Omega\right)^{2}}{\Omega^{2}} \\
\int_{M}\left(s-s_{0}\right)_{g}^{2} d \mu_{g} & =\|\mathfrak{F}(\Omega)\|^{2}
\end{aligned}$$
where
$$s_{0}=f_{M} s d \mu_{g}=\frac{\int s d \mu_{g}}{\int d \mu_{g}}$$
denotes the average scalar curvature.
Essentially because quadratic curvature functionals are scale-invariant in real dimension 4, one has $\mathcal{A}(\lambda \Omega)=\mathcal{A}(\Omega)$ for every $\lambda \in \mathbb{R}^{+}$. Thus, if $\mathcal{K} \subset$ $H^{2}(M, \mathbb{R})$ is the Kähler cone of $(M, J)$, then letting $\check{\mathcal{K}}$ denote $\mathcal{K} / \mathbb{R}^{+}$, where the positive real numbers $\mathbb{R}^{+}$act by scalar multiplication, we often choose to consider $\mathcal{A}$ as a function $\mathcal{A}: \tilde{\mathcal{K}} \rightarrow \mathbb{R}$. But from either point of view, the following variational principle [8, 18] underpins our entire approach:

Proposition 2 Suppose that $h$ is an Einstein metric on $M$ which is conformally related to a $J$-compatible Kähler metric $g$ with Kähler class $[\omega] \in \mathcal{K}$. Then $[\omega]$ is a critical point of $\mathcal{A}$.

Fortunately, the formula for $\mathcal{A}$ can be found explicitly, although the actual expression is complicated enough that a program like Mathematica is of enormous help in reliably obtaining the correct answer. In an earlier investigation, Maschler [24] used this to marshal overwhelming numerical evidence in favor of the conjecture that $\mathcal{A}$ has exactly one critical point on either $\mathbb{C P}_{2} \# 2 \overline{\mathbb{C P}}_{2}$ and on $\mathbb{C P}_{2} \# 3 \overline{\mathbb{C P}}_{2}$. In this paper, we will instead examine explicit formulas for appropriate second derivatives of $\mathcal{A}$, and observe that these imply that the function is strictly convex on certain line segments. This allows one to show that a critical point must be invariant under certain finite groups of automorphisms, and leads to water-tight proofs of the uniqueness of the critical point. Theorems A, B and C then follow from the uniqueness, up to isometry, of extremal Kähler metrics in a fixed Kähler class [9, 12, 22].

\section*{2 The case of $\mathbb{C P} \# 2 \overline{\mathbb{C P}}_{2}$}

In this section, we will show that
$$\mathcal{A}: \check{\mathcal{K}} \rightarrow \mathbb{R}$$
has only one critical point when $M=\mathbb{C} \mathbb{P} \# 2 \overline{\mathbb{C P}}_{2}$. We begin by fixing a Kähler class, normalized by rescaling so that the proper transform of the projective line between the two blow-up points has area 1:
![](https://cdn.mathpix.com/cropped/67cca2e7-178f-4622-8f8c-0c3baa876fb4-05.jpg?height=324&width=1052&top_left_y=1774&top_left_x=518)
The pair of positive real numbers $(\beta, \gamma)$, representing the areas of the two other exceptional divisors, now provides us with global coordinates on the reduced Kähler cone $\check{\mathcal{K}}=\mathcal{K} / \mathbb{R}^{+}$, thereby giving us a diffeomorphism $\check{\mathcal{K}} \approx$ $\mathbb{R}^{+} \times \mathbb{R}^{+}$.

Let us take the two blown-up points to be $[1,0,0],[0,1,0] \in \mathbb{C P}_{2}$, and fix the maximal torus
$$\left[\begin{array}{ccc}
e^{i \theta} & & \\
& e^{i \phi} & \\
& & 1
\end{array}\right]$$
in the automophism group. Then, for any $T^{2}$-invariant metric, the moment map of the torus action will take values in a pentagon, which after translation becomes the following:
![](https://cdn.mathpix.com/cropped/67cca2e7-178f-4622-8f8c-0c3baa876fb4-06.jpg?height=450&width=505&top_left_y=885&top_left_x=814)
Let $\mathfrak{F}_{1}$ and $\mathfrak{F}_{2}$ be Futaki invariants of this Kähler class with respect to the vector fields with Hamiltonians $-x$ and $-y$. Then [21] for any $T^{2}$-invariant metric,
$$\begin{aligned}
\mathfrak{F}_{1} & =\int_{M} x\left(s-s_{0}\right) d \mu \\
& =\frac{1}{V}\left[(\beta-2 \gamma)\left(\frac{1}{3}+\gamma+\gamma^{2}\right)+\gamma(\gamma-\beta)(2+\beta+2 \gamma)\right] \\
\mathfrak{F}_{2} & =\int_{M} y\left(s-s_{0}\right) d \mu \\
& =\frac{1}{V}\left[(\gamma-2 \beta)\left(\frac{1}{3}+\beta+\beta^{2}\right)+\beta(\beta-\gamma)(2+\gamma+2 \beta)\right]
\end{aligned}$$
where
$$V=\beta \gamma+\beta+\gamma+\frac{1}{2} .$$

Note that, by Archimedes' principle, the push-forward of the volume measure of $M$ is exactly $4 \pi^{2}$ times the Euclidean measure on the moment polygon. Thus, for example, the average values $x_{0}$ and $y_{0}$ of the Hamiltonians $x$ and
$y$ on $M$ are also the $x$ and $y$ coordinates of the barycenter of the moment pentagon. This same observation also makes it straightforward to compute the following useful constants:
$$\begin{aligned}
A & :=\int_{M}\left(x-x_{0}\right)^{2} d \mu \\
& =\frac{1+6(1+\beta)\left[\beta+\beta^{2}+\beta^{3}+\gamma\left(1+4 \beta+4 \beta^{2}+2 \beta^{3}\right)+\gamma^{2}(1+\beta)^{3}\right]}{288 \pi^{2} V} \\
B & :=\int_{M}\left(y-y_{0}\right)^{2} d \mu \\
& =\frac{1+6(1+\gamma)\left[\gamma+\gamma^{2}+\gamma^{3}+\beta\left(1+4 \gamma+4 \gamma^{2}+2 \gamma^{3}\right)+\beta^{2}(1+\gamma)^{3}\right]}{288 \pi^{2} V} \\
C & :=\int_{M}\left(x-x_{0}\right)\left(y-y_{0}\right) d \mu \\
& =-\frac{1+6(1+\beta)(1+\gamma)(\beta+\gamma+3 \beta \gamma)}{576 \pi^{2} V}
\end{aligned}$$
Then
$$\|\mathfrak{F}\|^{2}=\frac{B \mathfrak{F}_{1}^{2}-2 C \mathfrak{F}_{1} \mathfrak{F}_{2}+A \mathfrak{F}_{2}^{2}}{A B-C^{2}},$$
and
$$\mathcal{A}(\Omega)=\frac{\left(c_{1} \cdot \Omega\right)^{2}}{\Omega^{2}}+\frac{1}{32 \pi^{2}} \frac{B \mathfrak{F}_{1}^{2}-2 C \mathfrak{F}_{1} \mathfrak{F}_{+} A \mathfrak{F}_{2}^{2}}{A B-C^{2}}$$
can now be shown to explicitly be given by
$$\begin{aligned}
& 3\left[3+28 \gamma+96 \gamma^{2}+168 \gamma^{3}+164 \gamma^{4}+80 \gamma^{5}+16 \gamma^{6}+16 \beta^{6}(1+\gamma)^{4}+16 \beta^{5}(5+\right. \\
& \left.24 \gamma+43 \gamma^{2}+37 \gamma^{3}+15 \gamma^{4}+2 \gamma^{5}\right)+4 \beta^{4}\left(41+228 \gamma+478 \gamma^{2}+496 \gamma^{3}+263 \gamma^{4}+\right. \\
& \left.60 \gamma^{5}+4 \gamma^{6}\right)+8 \beta^{3}\left(21+135 \gamma+326 \gamma^{2}+392 \gamma^{3}+248 \gamma^{4}+74 \gamma^{5}+8 \gamma^{6}\right)+4 \beta(7+ \\
& \left.58 \gamma+176 \gamma^{2}+270 \gamma^{3}+228 \gamma^{4}+96 \gamma^{5}+16 \gamma^{6}\right)+4 \beta^{2}\left(24+176 \gamma+479 \gamma^{2}+652 \gamma^{3}+\right. \\
& \left.\left.478 \gamma^{4}+172 \gamma^{5}+24 \gamma^{6}\right)\right] / \\
& {\left[1+10 \gamma+36 \gamma^{2}+64 \gamma^{3}+60 \gamma^{4}+24 \gamma^{5}+24 \beta^{5}(1+\gamma)^{5}+12 \beta^{4}(1+\gamma)^{2}(5+20 \gamma+\right.} \\
& \left.23 \gamma^{2}+10 \gamma^{3}\right)+16 \beta^{3}\left(4+28 \gamma+72 \gamma^{2}+90 \gamma^{3}+57 \gamma^{4}+15 \gamma^{5}\right)+12 \beta^{2}(3+24 \gamma+ \\
& \left.\left.69 \gamma^{2}+96 \gamma^{3}+68 \gamma^{4}+20 \gamma^{5}\right)+2 \beta\left(5+45 \gamma+144 \gamma^{2}+224 \gamma^{3}+180 \gamma^{4}+60 \gamma^{5}\right)\right]
\end{aligned}$$

Lemma 1 The restriction of $\mathcal{A}$ to a line segment $\beta+\gamma=$ const is always a strictly convex function on the interval where $\beta, \gamma>0$.

Proof. Machine-assisted computation reveals that $\left(\frac{\partial}{\partial \beta}-\frac{\partial}{\partial \gamma}\right)^{2} \mathcal{A}$ is given by $24\left[2304 \beta^{16}(1+\gamma)^{12}+6912 \beta^{15}(1+\gamma)^{9}\left(3+11 \gamma+12 \gamma^{2}+5 \gamma^{3}\right)+576 \beta^{14}(1+\right.$ $\gamma)^{6}\left(167+1166 \gamma+3343 \gamma^{2}+5064 \gamma^{3}+4371 \gamma^{4}+2070 \gamma^{5}+431 \gamma^{6}\right)+384 \beta^{13}(1+$ $\gamma)^{3}\left(774+7782 \gamma+35067 \gamma^{2}+92491 \gamma^{3}+157494 \gamma^{4}+180246 \gamma^{5}+139303 \gamma^{6}+\right.$ $\left.70461 \gamma^{7}+21276 \gamma^{8}+2940 \gamma^{9}\right)+\left(1+4 \gamma+6 \gamma^{2}+4 \gamma^{3}\right)^{2}\left(4+62 \gamma+457 \gamma^{2}+1922 \gamma^{3}+\right.$ $\left.4910 \gamma^{4}+7992 \gamma^{5}+8520 \gamma^{6}+5976 \gamma^{7}+2808 \gamma^{8}+864 \gamma^{9}+144 \gamma^{10}\right)+2 \beta\left(1+4 \gamma+6 \gamma^{2}+\right.$ $\left.4 \gamma^{3}\right)^{2}\left(47+620 \gamma+4023 \gamma^{2}+15275 \gamma^{3}+35790 \gamma^{4}+54420 \gamma^{5}+55668 \gamma^{6}+38844 \gamma^{7}+\right.$ $\left.18504 \gamma^{8}+5616 \gamma^{9}+864 \gamma^{10}\right)+96 \beta^{12}(1+\gamma)^{2}\left(6943+76784 \gamma+389911 \gamma^{2}+\right.$ $1189166 \gamma^{3}+2406813 \gamma^{4}+3382480 \gamma^{5}+3355525 \gamma^{6}+2334978 \gamma^{7}+1104488 \gamma^{8}+$ $\left.332712 \gamma^{9}+58398 \gamma^{10}+7572 \gamma^{11}+1938 \gamma^{12}+312 \gamma^{13}+24 \gamma^{14}\right)+96 \beta^{11}(11727+$ $153845 \gamma+945314 \gamma^{2}+3583138 \gamma^{3}+9309806 \gamma^{4}+17464406 \gamma^{5}+24300890 \gamma^{6}+$ $25383726 \gamma^{7}+19929243 \gamma^{8}+11686165 \gamma^{9}+5084700 \gamma^{10}+1671216 \gamma^{11}+457080 \gamma^{12}+$ $\left.120384 \gamma^{13}+27936 \gamma^{14}+4104 \gamma^{15}+288 \gamma^{16}\right)+16 \beta^{10}\left(91367+1213674 \gamma+7595262 \gamma^{2}+\right.$ $29525748 \gamma^{3}+79271358 \gamma^{4}+154934784 \gamma^{5}+226825122 \gamma^{6}+252558972 \gamma^{7}+$ $215533575 \gamma^{8}+141830454 \gamma^{9}+73002384 \gamma^{10}+30508200 \gamma^{11}+10969860 \gamma^{12}+$ $\left.3434616 \gamma^{13}+837216 \gamma^{14}+129168 \gamma^{15}+9504 \gamma^{16}\right)+32 \beta^{9}(46177+626348 \gamma+$ $4023003 \gamma^{2}+16156443 \gamma^{3}+45149508 \gamma^{4}+92636856 \gamma^{5}+143842384 \gamma^{6}+172157314 \gamma^{7}+$ $160870371 \gamma^{8}+118918740 \gamma^{9}+70915227 \gamma^{10}+35058495 \gamma^{11}+14629998 \gamma^{12}+$ $\left.5009448 \gamma^{13}+1277280 \gamma^{14}+206064 \gamma^{15}+15840 \gamma^{16}\right)+16 \beta^{8}(73136+1020846 \gamma+$ $6782175 \gamma^{2}+28350072 \gamma^{3}+83038113 \gamma^{4}+179966490 \gamma^{5}+297854048 \gamma^{6}+384202536 \gamma^{7}+$ $392256648 \gamma^{8}+321740742 \gamma^{9}+215533575 \gamma^{10}+119575458 \gamma^{11}+54779814 \gamma^{12}+$ $\left.19939536 \gamma^{13}+5297652 \gamma^{14}+890352 \gamma^{15}+71280 \gamma^{16}\right)+16 \beta^{7}(45406+656739 \gamma+$ $4546158 \gamma^{2}+19916894 \gamma^{3}+61505100 \gamma^{4}+141399807 \gamma^{5}+249914844 \gamma^{6}+346874028 \gamma^{7}+$ $384202536 \gamma^{8}+344314628 \gamma^{9}+252558972 \gamma^{10}+152302356 \gamma^{11}+74571048 \gamma^{12}+$ $\left.28478448 \gamma^{13}+7856640 \gamma^{14}+1371168 \gamma^{15}+114048 \gamma^{16}\right)+\beta^{2}(1065+20598 \gamma+$ $195144 \gamma^{2}+1180776 \gamma^{3}+5035692 \gamma^{4}+15925800 \gamma^{5}+38527448 \gamma^{6}+72738528 \gamma^{7}+$ $108514800 \gamma^{8}+128736096 \gamma^{9}+121524192 \gamma^{10}+90750144 \gamma^{11}+52840512 \gamma^{12}+$ $\left.23322240 \gamma^{13}+7398144 \gamma^{14}+1513728 \gamma^{15}+152064 \gamma^{16}\right)+8 \beta^{5}(16386+259536 \gamma+$ $1990725 \gamma^{2}+9755446 \gamma^{3}+33937098 \gamma^{4}+88398864 \gamma^{5}+177968682 \gamma^{6}+282799614 \gamma^{7}+$ $359932980 \gamma^{8}+370547424 \gamma^{9}+309869568 \gamma^{10}+209572872 \gamma^{11}+112623264 \gamma^{12}+$ $\left.46332864 \gamma^{13}+13651776 \gamma^{14}+2550528 \gamma^{15}+228096 \gamma^{16}\right)+2 \beta^{3}(3769+67451 \gamma+$ $590388 \gamma^{2}+3311320 \gamma^{3}+13161720 \gamma^{4}+39021784 \gamma^{5}+89001976 \gamma^{6}+159335152 \gamma^{7}+$ $226800576 \gamma^{8}+258503088 \gamma^{9}+236205984 \gamma^{10}+171990624 \gamma^{11}+98197056 \gamma^{12}+$ $\left.42587904 \gamma^{13}+13234176 \gamma^{14}+2630016 \gamma^{15}+253440 \gamma^{16}\right)+4 \beta^{6}(87921+1326312 \gamma+$ $9631862 \gamma^{2}+44500988 \gamma^{3}+145571257 \gamma^{4}+355937364 \gamma^{5}+671754360 \gamma^{6}+999659376 \gamma^{7}+$ $1191416192 \gamma^{8}+1150739072 \gamma^{9}+907300488 \gamma^{10}+583221360 \gamma^{11}+300655152 \gamma^{12}+$
$\left.119521344 \gamma^{13}+34128576 \gamma^{14}+6168960 \gamma^{15}+532224 \gamma^{16}\right)+2 \beta^{4}(18413+308550 \gamma+$ $2517846 \gamma^{2}+13161720 \gamma^{3}+48864336 \gamma^{4}+135748392 \gamma^{5}+291142514 \gamma^{6}+492040800 \gamma^{7}+$ $664304904 \gamma^{8}+722392128 \gamma^{9}+634170864 \gamma^{10}+446870688 \gamma^{11}+248402688 \gamma^{12}+$ $\left.\left.105206400 \gamma^{13}+31888800 \gamma^{14}+6148224 \gamma^{15}+570240 \gamma^{16}\right)\right] /$ $\left[1+10 \gamma+36 \gamma^{2}+64 \gamma^{3}+60 \gamma^{4}+24 \gamma^{5}+24 \beta^{5}(1+\gamma)^{5}+12 \beta^{4}(1+\gamma)^{2}(5+20 \gamma+\right.$ $\left.23 \gamma^{2}+10 \gamma^{3}\right)+16 \beta^{3}\left(4+28 \gamma+72 \gamma^{2}+90 \gamma^{3}+57 \gamma^{4}+15 \gamma^{5}\right)+12 \beta^{2}(3+24 \gamma+$ $\left.\left.69 \gamma^{2}+96 \gamma^{3}+68 \gamma^{4}+20 \gamma^{5}\right)+2 \beta\left(5+45 \gamma+144 \gamma^{2}+224 \gamma^{3}+180 \gamma^{4}+60 \gamma^{5}\right)\right]^{3}$

Because all the coefficients in both the numerator and denominator of this expression are positive, the second derivative of $\mathcal{A}$ along any line $\beta+\gamma=$ const is strictly positive whenever $\beta, \gamma>0$. This proves the claim. \(\square\)

Lemma 2 If $(\beta, \gamma) \in \mathbb{R}^{+} \times \mathbb{R}^{+} \approx \check{\mathcal{K}}$ is a critical point of $\mathcal{A}$, then $\beta=\gamma$.

Proof. Since there is an automorphism of $\mathbb{C P}_{2} \# 2 \overline{\mathbb{C P}}_{2}$ which interchanges the two exceptional divisors, we automatically have $\mathcal{A}(\beta, \gamma)=\mathcal{A}(\gamma, \beta)$. In particular, reflection across the diagonal sends critical points to critical points. Lemma 1, however, implies that there can be at most one critical point on any segment $\beta+\gamma=$ const $, \beta, \gamma>0$. If $\beta \neq \gamma$ for some critical point, we would therefore obtain a contradiction by considering the line segment joining $(\beta, \gamma)$ to $(\gamma, \beta)$. Hence every critical point must belong to the diagonal. \(\square\)

Using the the terminology of [8], we have thus shown that any critical point $\Omega \in \mathcal{K}$ of $\mathcal{A}$ must be a bilaterally symmetric Kähler class.

To conclude our discussion, we now let $F: \mathbb{R}^{+} \rightarrow \mathbb{R}$ be the function defined by
$$F(\beta)=\mathcal{A}(\beta, \beta) .$$
Explicitly, this function is given by
$$F(\beta)=\frac{9+96 \beta+396 \beta^{2}+840 \beta^{3}+954 \beta^{4}+528 \beta^{5}+96 \beta^{6}}{1+12 \beta+54 \beta^{2}+120 \beta^{3}+138 \beta^{4}+72 \beta^{5}+12 \beta^{6}}$$
Because $\mathcal{A}$ is symmetric under $(\beta, \gamma) \leftrightarrow(\gamma, \beta)$, Lemma 2 tells us that the critical points of $\mathcal{A}$ are precisely those ( $\beta, \beta$ ) for which $F^{\prime}(\beta)=0$.

Lemma 3 The above function satisfies $F^{\prime}(\beta)>0$ for all $\beta \geq 1.2$.
Proof. The derivative of $F$ is given by
$$\frac{d F}{d \beta}=\frac{12 P(\beta)}{\left(1+12 \beta+54 \beta^{2}+120 \beta^{3}+138 \beta^{4}+72 \beta^{5}+12 \beta^{6}\right)^{2}}$$
where the polynomial
$$P(\beta):=-1-15 \beta-96 \beta^{2}-336 \beta^{3}-680 \beta^{4}-720 \beta^{5}-120 \beta^{6}+624 \beta^{7}+708 \beta^{8}+300 \beta^{9}+48 \beta^{10}$$
must of course always have the same sign as $F^{\prime}(\beta)$. When $\beta>1$, however, we obviously have
$$\begin{aligned}
P(\beta) & >-(1+15+96+336+680+720+120) \beta^{6}+(624+708+300+48) \beta^{7} \\
& =\beta^{6}(1680 \beta-1968)
\end{aligned}$$
and the claim therefore follows from the fact that 1.2 > 1968/1680. \(\square\)

Lemma 4 The above function satisfies $F^{\prime \prime}(\beta)>0$ for all $\beta \in(0,1.2]$.

Proof. The second derivative of $F$ is given by
$$\frac{d^{2} F}{d \beta^{2}}=\frac{12 Q(\beta)}{\left(1+12 \beta+54 \beta^{2}+120 \beta^{3}+138 \beta^{4}+72 \beta^{5}+12 \beta^{6}\right)^{3}}$$
where the polynomial
$$\begin{aligned}
Q(\beta)= & 9+204 \beta+2142 \beta^{2}+13720 \beta^{3}+59514 \beta^{4}+183672 \beta^{5} \\
& +412044 \beta^{6}+672768 \beta^{7}+782892 \beta^{8}+611088 \beta^{9}+264456 \beta^{10} \\
& -2592 \beta^{11}-74952 \beta^{12}-42336 \beta^{13}-10800 \beta^{14}-1152 \beta^{15}
\end{aligned}$$
again has the same sign as $F^{\prime \prime}(\beta)$ in the allowed range $\beta>0$. For $\beta \in(0,1]$, we thus have
$$\begin{aligned}
Q(\beta) \quad \geq & (9+204+2142+13720+59514+183672+412044+672768+782892+ \\
& 611088+264456) \beta^{10}-(2592+74952+42336+10800+1152) \beta^{11} \\
= & (3002509-131832 \beta) \beta^{10}
\end{aligned}$$
so that $F^{\prime \prime}(\beta)>0$ in this range. Similarly, when $\beta>1$ we have
$$\begin{aligned}
Q(\beta)> & (9+204+2142+13720+59514+183672+412044+672768+782892+ \\
& 611088+264456)-(2592+74952+42336+10800+1152) \beta^{15} \\
= & 3002509-131832 \beta^{15}
\end{aligned}$$
and so, since $(1.2)^{15}<16<30.02509 / 1.31832$, we also conclude that $F^{\prime \prime}(\beta)>$ 0 for $\beta \in(1,1.2]$. Combining these two arguments now proves the claim. \(\square\)

Proposition 3 For $M=\mathbb{C P}_{2} \# 2 \overline{\mathbb{C P}}_{2}$, the function $\mathcal{A}: \check{\mathcal{K}} \rightarrow \mathbb{R}$ has exactly one critical point. Moreover, this critical point is an absolute minimum.

Proof. By Lemma 2, any critical point belongs to the line $\beta=\gamma$. Moreover, Lemma 3 says that such a critical point would necessarily satisfy $\beta \in(0,1.2]$. However, $F^{\prime}$ can only have one zero on (0, 1.2] by Lemma 4, and the uniqueness of the critical point is therefore assured.

The fact that such a critical point does actually exist follows from the observation that $\lim _{\beta \rightarrow 0} F^{\prime}(\beta)=-12<0$, whereas $F^{\prime}(1.2)>0$ by Lemma 3 . Moreover, since this unique critical point is a local minimum, it must actually be the absolute minimum of $F$ on $(0, \infty)$. However, Lemma 1 implies that
$$\mathcal{A}(\beta, \gamma)=\frac{\mathcal{A}(\beta, \gamma)+\mathcal{A}(\gamma, \beta)}{2} \geq \mathcal{A}\left(\frac{\beta+\gamma}{2}, \frac{\beta+\gamma}{2}\right)=F\left(\frac{\beta+\gamma}{2}\right)$$
for any $\beta, \gamma>0$. Thus the absolute minimum of $F$ necessarily also represents the absolute minimum of $\mathcal{A}$. \(\square\)

Theorem B now follows. Indeed, by Proposition 1, any conformally Einstein Kähler metric $\tilde{g}$ on $M=\mathbb{C} \mathbb{P} \# 2 \overline{\mathbb{C P}}_{2}$ is extremal, and, by Proposition 2, it must moreover belong to a Kähler class $\Omega$ which is a critical point of $\mathcal{A}$. However, by Proposition 3, this critical Kähler class $\Omega$ is unique up to scale. Consequently, the Kähler class of some multiple of $\tilde{g}$ must coincide with the Kähler class of the conformally Einstein Kähler metric $g$ constructed in [8]. On the other hand, extremal Kähler metrics in any fixed Kähler class are known [9] to be unique up to complex automorphisms; cf. [12, 22]. In particular, $(M, g)$ must be isometric to $(M, c \tilde{g})$ for some positive constant $c$. Moreover, since $\Omega$ actually minimizes $\mathcal{A}$ by Proposition n 3, inequality (1) implies that $g$ actually minimizes $\mathcal{C}$ among all Kähler metrics on $M=\mathbb{C} \mathbb{P} \# 2 \overline{\mathbb{C P}}_{2}$.

\section*{3 The case of $\mathbb{C P} \# 3 \overline{\mathbb{C P}}_{2}$}

We now show that
$$\mathcal{A}: \check{\mathcal{K}} \rightarrow \mathbb{R}$$
also has only one critical point when $M=\mathbb{C} \mathbb{P} \# 3 \overline{\mathbb{C P}}_{2}$. First recall that the general Kähler class on this manifold is determined by four real numbers:
![](https://cdn.mathpix.com/cropped/67cca2e7-178f-4622-8f8c-0c3baa876fb4-12.jpg?height=304&width=1078&top_left_y=808&top_left_x=492)
Let us decompose the reduced Kähler cone $\check{\mathcal{K}}=\mathcal{K} / \mathbb{R}^{+}$into the open set $\mathcal{U}$ corresponding to $\delta>0$, a second open set $\mathcal{\mathcal { U } ^ { \prime }}$ corresponding to $\delta<0$, and a lower-dimensional interface $\mathcal{P}$ cut out by the hyper-plane $\delta=0$. Each element of $\mathcal{U}$ then has a unique representative with $\delta=1$, and the remaining positive real numbers $(\alpha, \beta, \gamma)$ then provide global coordinates on $\mathcal{U}$, which is thereby identified with $\left(\mathbb{R}^{+}\right)^{3}$. The region $\mathcal{U}^{\prime}$ is actually the image of $\mathcal{U}$ under a Cremona transformation $\Phi$, where $\Phi$ is the automorphism of of $\mathbb{C P} \# 3 \overline{\mathbb{C P}}_{2}$ induced by the bimeromorphic transformation
$$\left[z_{1}: z_{2}: z_{3}\right] \longmapsto\left[\frac{1}{z_{1}}: \frac{1}{z_{2}}: \frac{1}{z_{3}}\right]$$
of $\mathbb{C P}_{2}$. Since $\mathcal{A}$ is invariant under automorphisms, it follows that we can completely understand its behavior on $\mathcal{U}^{\prime}$ by thoroughly understanding its behavior on our coordinate domain $\mathcal{U}$. The behavior of $\mathcal{A}$ on the interface $\mathcal{P}$ will of course call for a separate, careful discussion.

For the present, however, let us focus on our coordinate region $\mathcal{U}$ in the reduced Kähler cone $\check{\mathcal{K}}$. We now once again fix the 2-torus in the automorphism group corresponding to $\left[z_{1}: z_{2}: z_{3}\right] \mapsto\left[e^{i \theta} z_{1}: e^{i \phi} z_{2}: z_{3}\right]$. The image of $M$ under the moment map is then the hexagon
![](https://cdn.mathpix.com/cropped/67cca2e7-178f-4622-8f8c-0c3baa876fb4-13.jpg?height=449&width=505&top_left_y=434&top_left_x=814)
and our formulas [21] for the components of the Futaki invariant become
$$\begin{aligned}
\mathfrak{F}_{1} & =\int_{M} x\left(s-s_{0}\right) d \mu \\
& =\frac{1}{V}\left[(\alpha+\beta-2 \gamma)\left(\frac{1}{3}+\gamma+\gamma^{2}\right)+(\gamma-\alpha)(\gamma-\beta)(2+\alpha+\beta+2 \gamma)\right] \\
\mathfrak{F}_{2} & =\int_{M} y\left(s-s_{0}\right) d \mu \\
& =\frac{1}{V}\left[(\alpha+\gamma-2 \beta)\left(\frac{1}{3}+\beta+\beta^{2}\right)+(\beta-\alpha)(\beta-\gamma)(2+\alpha+\gamma+2 \beta)\right]
\end{aligned}$$
where
$$V=\alpha \beta+\alpha \gamma+\beta \gamma+\alpha+\beta+\gamma+\frac{1}{2}$$
is the volume of $(M, \Omega)$. Three other essential coefficients needed in our computation are
$$\begin{aligned}
A:= & \int_{M}\left(x-x_{0}\right)^{2} d \mu \\
= & \left(288 \pi^{2} V\right)^{-1}\left[1+6 \beta+12 \beta^{2}+12 \beta^{3}+6 \beta^{4}+6 \gamma^{2}(1+\beta)^{4}+6 \alpha^{4}(1+\gamma+\beta)^{2}+\right. \\
& 6 \gamma\left(1+5 \beta+8 \beta^{2}+6 \beta^{3}+2 \beta^{4}\right)+6 \alpha^{2}\left(2+8 \beta+9 \beta^{2}+4 \beta^{3}+\beta^{4}+6 \gamma^{2}(1+\beta)^{2}+\right. \\
& \left.2 \gamma(2+\beta)^{2}(1+2 \beta)\right)+12 \alpha^{3}\left(1+3 \beta+2 \beta^{2}+2 \gamma^{2}(1+\beta)+\gamma\left(3+6 \beta+2 \beta^{2}\right)\right)+ \\
& \left.6 \alpha\left(1+5 \beta+8 \beta^{2}+6 \beta^{3}+2 \beta^{4}+4 \gamma^{2}(1+\beta)^{3}+\gamma\left(5+20 \beta+24 \beta^{2}+12 \beta^{3}+2 \beta^{4}\right)\right)\right]
\end{aligned}$$
$$\begin{aligned}
B:= & \int_{M}\left(y-y_{0}\right)^{2} d \mu \\
= & \left(288 \pi^{2} V\right)^{-1}\left[1+6 \gamma+12 \gamma^{2}+12 \gamma^{3}+6 \gamma^{4}+6 \beta^{2}(1+\gamma)^{4}+6 \alpha^{4}(1+\beta+\gamma)^{2}+\right. \\
& 6 \beta\left(1+5 \gamma+8 \gamma^{2}+6 \gamma^{3}+2 \gamma^{4}\right)+6 \alpha^{2}\left(2+8 \gamma+9 \gamma^{2}+4 \gamma^{3}+\gamma^{4}+6 \beta^{2}(1+\gamma)^{2}+\right. \\
& \left.2 \beta(2+\gamma)^{2}(1+2 \gamma)\right)+12 \alpha^{3}\left(1+3 \gamma+2 \gamma^{2}+2 \beta^{2}(1+\gamma)+\beta\left(3+6 \gamma+2 \gamma^{2}\right)\right)+ \\
& \left.6 \alpha\left(1+5 \gamma+8 \gamma^{2}+6 \gamma^{3}+2 \gamma^{4}+4 \beta^{2}(1+\gamma)^{3}+\beta\left(5+20 \gamma+24 \gamma^{2}+12 \gamma^{3}+2 \gamma^{4}\right)\right)\right]
\end{aligned}$$
and
$$\begin{aligned}
C:= & \int_{M}\left(x-x_{0}\right)\left(y-y_{0}\right) d \mu \\
= & -\left(576 \pi^{2} V\right)^{-1}\left[1+6 \gamma+6 \gamma^{2}+12 \alpha^{4}(1+\beta+\gamma)^{2}+6 \beta^{2}\left(1+4 \gamma+3 \gamma^{2}\right)+\right. \\
& 6 \beta\left(1+5 \gamma+4 \gamma^{2}\right)+24 \alpha^{3}\left(1+3 \gamma+2 \gamma^{2}+2 \beta^{2}(1+\gamma)+\beta\left(3+6 \gamma+2 \gamma^{2}\right)\right)+ \\
& 18 \alpha^{2}\left(1+4 \gamma+3 \gamma^{2}+\beta^{2}\left(3+6 \gamma+2 \gamma^{2}\right)+2 \beta\left(2+6 \gamma+3 \gamma^{2}\right)\right)+ \\
& \left.6 \alpha\left(1+5 \gamma+4 \gamma^{2}+2 \beta^{2}\left(2+6 \gamma+3 \gamma^{2}\right)+\beta\left(5+20 \gamma+12 \gamma^{2}\right)\right)\right]
\end{aligned}$$
We then have
$$\|\mathfrak{F}\|^{2}=\frac{B \mathfrak{F}_{1}^{2}-2 C \mathfrak{F}_{1} \mathfrak{F}_{+} A \mathfrak{F}_{2}^{2}}{A B-C^{2}} .$$
This in turn allows us to compute
$$\mathcal{A}=\frac{\left(c_{1} \cdot \Omega\right)^{2}}{\Omega^{2}}+\frac{1}{32 \pi^{2}} \frac{B \mathfrak{F}_{1}^{2}-2 C \mathfrak{F}_{1} \mathfrak{F}_{+} A \mathfrak{F}_{2}^{2}}{A B-C^{2}},$$
which, upon simplification, is explicitly given by
$$\begin{aligned}
& 3\left[3+28 \gamma+96 \gamma^{2}+168 \gamma^{3}+164 \gamma^{4}+80 \gamma^{5}+16 \gamma^{6}+16 \beta^{6}(1+\gamma)^{4}+16 \alpha^{6}(1+\beta+\gamma)^{4}+16 \beta^{5}(5+\right. \\
& \left.24 \gamma+43 \gamma^{2}+37 \gamma^{3}+15 \gamma^{4}+2 \gamma^{5}\right)+4 \beta^{4}\left(41+228 \gamma+478 \gamma^{2}+496 \gamma^{3}+263 \gamma^{4}+60 \gamma^{5}+4 \gamma^{6}\right)+ \\
& 8 \beta^{3}\left(21+135 \gamma+326 \gamma^{2}+392 \gamma^{3}+248 \gamma^{4}+74 \gamma^{5}+8 \gamma^{6}\right)+4 \beta\left(7+58 \gamma+176 \gamma^{2}+270 \gamma^{3}+228 \gamma^{4}+\right. \\
& \left.96 \gamma^{5}+16 \gamma^{6}\right)+4 \beta^{2}\left(24+176 \gamma+479 \gamma^{2}+652 \gamma^{3}+478 \gamma^{4}+172 \gamma^{5}+24 \gamma^{6}\right)+16 \alpha^{5}\left(5+2 \beta^{5}+24 \gamma+\right. \\
& 43 \gamma^{2}+37 \gamma^{3}+15 \gamma^{4}+2 \gamma^{5}+\beta^{4}(15+14 \gamma)+\beta^{3}\left(37+70 \gamma+30 \gamma^{2}\right)+\beta^{2}\left(43+123 \gamma+108 \gamma^{2}+30 \gamma^{3}\right)+ \\
& \left.\beta\left(24+92 \gamma+123 \gamma^{2}+70 \gamma^{3}+14 \gamma^{4}\right)\right)+4 \alpha^{4}\left(41+4 \beta^{6}+228 \gamma+478 \gamma^{2}+496 \gamma^{3}+263 \gamma^{4}+60 \gamma^{5}+\right. \\
& 4 \gamma^{6}+\beta^{5}(60+56 \gamma)+\beta^{4}\left(263+476 \gamma+196 \gamma^{2}\right)+8 \beta^{3}\left(62+169 \gamma+139 \gamma^{2}+35 \gamma^{3}\right)+2 \beta^{2}(239+ \\
& \left.\left.876 \gamma+1089 \gamma^{2}+556 \gamma^{3}+98 \gamma^{4}\right)+4 \beta\left(57+263 \gamma+438 \gamma^{2}+338 \gamma^{3}+119 \gamma^{4}+14 \gamma^{5}\right)\right)+8 \alpha^{3}(21+ \\
& 135 \gamma+326 \gamma^{2}+392 \gamma^{3}+248 \gamma^{4}+74 \gamma^{5}+8 \gamma^{6}+8 \beta^{6}(1+\gamma)+2 \beta^{5}\left(37+70 \gamma+30 \gamma^{2}\right)+4 \beta^{4}(62+ \\
& \left.169 \gamma+139 \gamma^{2}+35 \gamma^{3}\right)+4 \beta^{3}\left(98+353 \gamma+428 \gamma^{2}+210 \gamma^{3}+35 \gamma^{4}\right)+2 \beta^{2}\left(163+735 \gamma+1179 \gamma^{2}+\right.
\end{aligned}$$
$\left.\left.856 \gamma^{3}+278 \gamma^{4}+30 \gamma^{5}\right)+\beta\left(135+736 \gamma+1470 \gamma^{2}+1412 \gamma^{3}+676 \gamma^{4}+140 \gamma^{5}+8 \gamma^{6}\right)\right)+4 \alpha(7+$ $58 \gamma+176 \gamma^{2}+270 \gamma^{3}+228 \gamma^{4}+96 \gamma^{5}+16 \gamma^{6}+16 \beta^{6}(1+\gamma)^{3}+4 \beta^{5}\left(24+92 \gamma+123 \gamma^{2}+70 \gamma^{3}+\right.$ $\left.14 \gamma^{4}\right)+4 \beta^{4}\left(57+263 \gamma+438 \gamma^{2}+338 \gamma^{3}+119 \gamma^{4}+14 \gamma^{5}\right)+2 \beta^{3}\left(135+736 \gamma+1470 \gamma^{2}+1412 \gamma^{3}+\right.$ $\left.676 \gamma^{4}+140 \gamma^{5}+8 \gamma^{6}\right)+4 \beta^{2}\left(44+278 \gamma+645 \gamma^{2}+735 \gamma^{3}+438 \gamma^{4}+123 \gamma^{5}+12 \gamma^{6}\right)+2 \beta(29+210 \gamma+$ $\left.\left.556 \gamma^{2}+736 \gamma^{3}+526 \gamma^{4}+184 \gamma^{5}+24 \gamma^{6}\right)\right)+4 \alpha^{2}\left(24+176 \gamma+479 \gamma^{2}+652 \gamma^{3}+478 \gamma^{4}+172 \gamma^{5}+\right.$ $24 \gamma^{6}+24 \beta^{6}(1+\gamma)^{2}+4 \beta^{5}\left(43+123 \gamma+108 \gamma^{2}+30 \gamma^{3}\right)+2 \beta^{4}\left(239+876 \gamma+1089 \gamma^{2}+556 \gamma^{3}+\right.$ $\left.98 \gamma^{4}\right)+4 \beta^{3}\left(163+735 \gamma+1179 \gamma^{2}+856 \gamma^{3}+278 \gamma^{4}+30 \gamma^{5}\right)+4 \beta\left(44+278 \gamma+645 \gamma^{2}+735 \gamma^{3}+\right.$ $\left.\left.\left.438 \gamma^{4}+123 \gamma^{5}+12 \gamma^{6}\right)+\beta^{2}\left(479+2580 \gamma+5058 \gamma^{2}+4716 \gamma^{3}+2178 \gamma^{4}+432 \gamma^{5}+24 \gamma^{6}\right)\right)\right] /$ $\left[1+10 \gamma+36 \gamma^{2}+64 \gamma^{3}+60 \gamma^{4}+24 \gamma^{5}+24 \beta^{5}(1+\gamma)^{5}+24 \alpha^{5}(1+\beta+\gamma)^{5}+12 \beta^{4}(1+\gamma)^{2}(5+\right.$ $\left.20 \gamma+23 \gamma^{2}+10 \gamma^{3}\right)+16 \beta^{3}\left(4+28 \gamma+72 \gamma^{2}+90 \gamma^{3}+57 \gamma^{4}+15 \gamma^{5}\right)+12 \beta^{2}\left(3+24 \gamma+69 \gamma^{2}+\right.$ $\left.96 \gamma^{3}+68 \gamma^{4}+20 \gamma^{5}\right)+2 \beta\left(5+45 \gamma+144 \gamma^{2}+224 \gamma^{3}+180 \gamma^{4}+60 \gamma^{5}\right)+12 \alpha^{4}(1+\beta+\gamma)^{2}(5+$ $\left.20 \gamma+23 \gamma^{2}+10 \gamma^{3}+10 \beta^{3}(1+\gamma)+\beta^{2}\left(23+46 \gamma+16 \gamma^{2}\right)+2 \beta\left(10+30 \gamma+23 \gamma^{2}+5 \gamma^{3}\right)\right)+$ $16 \alpha^{3}\left(4+28 \gamma+72 \gamma^{2}+90 \gamma^{3}+57 \gamma^{4}+15 \gamma^{5}+15 \beta^{5}(1+\gamma)^{2}+3 \beta^{4}\left(19+57 \gamma+50 \gamma^{2}+13 \gamma^{3}\right)+\right.$ $3 \beta^{3}\left(30+120 \gamma+155 \gamma^{2}+78 \gamma^{3}+13 \gamma^{4}\right)+3 \beta^{2}\left(24+120 \gamma+206 \gamma^{2}+155 \gamma^{3}+50 \gamma^{4}+5 \gamma^{5}\right)+$ $\left.\beta\left(28+168 \gamma+360 \gamma^{2}+360 \gamma^{3}+171 \gamma^{4}+30 \gamma^{5}\right)\right)+12 \alpha^{2}\left(3+24 \gamma+69 \gamma^{2}+96 \gamma^{3}+68 \gamma^{4}+20 \gamma^{5}+\right.$ $20 \beta^{5}(1+\gamma)^{3}+\beta^{4}\left(68+272 \gamma+366 \gamma^{2}+200 \gamma^{3}+36 \gamma^{4}\right)+4 \beta^{3}\left(24+120 \gamma+206 \gamma^{2}+155 \gamma^{3}+\right.$ $\left.50 \gamma^{4}+5 \gamma^{5}\right)+2 \beta\left(12+84 \gamma+207 \gamma^{2}+240 \gamma^{3}+136 \gamma^{4}+30 \gamma^{5}\right)+\beta^{2}\left(69+414 \gamma+864 \gamma^{2}+824 \gamma^{3}+\right.$ $\left.\left.366 \gamma^{4}+60 \gamma^{5}\right)\right)+2 \alpha\left(5+45 \gamma+144 \gamma^{2}+224 \gamma^{3}+180 \gamma^{4}+60 \gamma^{5}+60 \beta^{5}(1+\gamma)^{4}+12 \beta^{4}(15+75 \gamma+\right.$ $\left.136 \gamma^{2}+114 \gamma^{3}+43 \gamma^{4}+5 \gamma^{5}\right)+12 \beta^{2}\left(12+84 \gamma+207 \gamma^{2}+240 \gamma^{3}+136 \gamma^{4}+30 \gamma^{5}\right)+8 \beta^{3}(28+$ $\left.\left.\left.168 \gamma+360 \gamma^{2}+360 \gamma^{3}+171 \gamma^{4}+30 \gamma^{5}\right)+3 \beta\left(15+120 \gamma+336 \gamma^{2}+448 \gamma^{3}+300 \gamma^{4}+80 \gamma^{5}\right)\right)\right]$

Lemma 5 The function obtained by restricting $\mathcal{A}$ to any line of the form $\alpha+\beta=\mathbf{c o n s t}, \gamma=\widehat{\text { const }}$ is strictly convex on the segment $\alpha, \beta>0$.
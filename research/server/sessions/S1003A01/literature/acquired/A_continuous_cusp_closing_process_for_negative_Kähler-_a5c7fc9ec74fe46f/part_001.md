---
retention_scope: session
part: 1
total_parts: 5
---

[Part 1/5 of: A continuous cusp closing process for negative Kähler- ...]

---
source_file: 2401_11468.pdf
converter: mathpix
format: mmd
---

\title{
A CONTINUOUS CUSP CLOSING PROCESS FOR NEGATIVE KÄHLER-EINSTEIN METRICS
}

\author{
XIN FU, HANS-JOACHIM HEIN, AND XUMIN JIANG
}

\begin{abstract}
We give an example of a family of smooth complex algebraic surfaces of degree 6 in $\mathbb{C P}^{3}$ developing an isolated elliptic singularity. We show via a gluing construction that the unique Kähler-Einstein metrics of Ricci curvature -1 on these sextics develop a complex hyperbolic cusp in the limit, and that near the tip of the forming cusp a Tian-Yau gravitational instanton bubbles off.
\end{abstract}

\section*{Contents}
1. Introduction ..... 2
1.1. Statement of the Main Theorem ..... 2
1.2. Possible generalizations ..... 3
1.3. Outline of the proof ..... 4
1.4. Acknowledgments ..... 5
2. Building blocks of the gluing ..... 5
2.1. Degenerations of projective surfaces of general type ..... 5
2.2. Singular Kähler-Einstein metrics with hyperbolic cusps ..... 9
2.3. Tian-Yau metrics ..... 14
2.4. A new neck region between a Tian-Yau end and a hyperbolic cusp ..... 16
2.4.1. Estimates asymptotically close to the cusp (green region) ..... 18
2.4.2. Estimates on the middle neck ..... 21
2.4.3. Estimates asymptotically close to the Tian-Yau end (orange region) ..... 26
3. The glued approximate Kähler-Einstein metric ..... 29
3.1. Setting up the glued metric and the Monge-Ampère equation ..... 29
3.2. Proof of the Ricci potential estimate ..... 33
3.3. Definition of the weight functions and weighted Hölder norms ..... 44
4. Uniform estimate of the inverse of the linearization modulo obstructions ..... 45
4.1. Definition of the obstruction space ..... 45
4.1.1. Collapse to an ODE on an interval ..... 46
4.1.2. Fundamental solutions of the endpoint model operators ..... 48
4.1.3. A Liouville theorem for the limit ODE ..... 48
4.1.4. Solving $L_{\infty} \hat{v}=\hat{u}$ with a Neumann boundary condition on the left ..... 51
4.1.5. Definition of the obstruction function ..... 52
4.1.6. Proof of Proposition 4.2 ..... 54
4.2. Statement of the uniform estimate modulo obstructions and set-up of the proof ..... 55
4.3. GH limit and Liouville on the Kähler-Einstein building block (region $\Re_{1}$ ) ..... 56
4.4. GH limit and Liouville on the cusp (regions $\Re_{2}, \Re_{3}$ ) ..... 56
4.4.1. Region $\Re_{2}$ : The genuine cusp ..... 57
4.4.2. Region $\Re_{3}$ : The green gluing region between the cusp and the new neck ..... 57

\footnotetext{
Date: January 7, 2025.
}
4.5. GH limit and Liouville on the Tian-Yau building block (region $\Re_{7}$ ) ..... 57
4.6. GH limit and Liouville on the Tian-Yau end (regions $\Re_{6}, \Re_{5}$ ) ..... 57
4.6.1. Region $\Re_{6}$ : The genuine Tian-Yau end ..... 57
4.6.2. Region $\Re_{5}$ : The orange gluing region between the Tian-Yau end and the new neck ..... 58
4.7. GH limit and Liouville on the new neck (region $\Re_{4}$ ) ..... 59
4.7.1. The subcase $c=1$ : Essentially the same as the Tian-Yau end ..... 59
4.7.2. The subcase $c=0$ : Essentially the same as the cusp ..... 59
4.7.3. The subcase $0<c<1$ : The genuine new neck, i.e., the obstructed case ..... 59
5. Obstruction theory and proof of the Main Theorem ..... 60
5.1. Fixed-point iteration on the orthogonal complement of the obstruction space ..... 60
5.2. Killing the obstruction by varying the Ricci potential ..... 63
References ..... 66

\section*{1. Introduction}
1.1. Statement of the Main Theorem. Consider the family $\left\{\mathcal{X}_{\sigma}\right\}_{\sigma \in \Delta}$ of degree 6 algebraic surfaces in $\mathbb{C P}^{3}$ given by the projective closures of the affine sextics
$$\left\{\left(z_{1}, z_{2}, z_{3}\right) \in \mathbb{C}^{3}:\left(z_{1}^{6}+z_{1}^{3}\right)+\left(z_{2}^{6}+z_{2}^{3}\right)+\left(z_{3}^{6}+z_{3}^{3}\right)=\sigma\right\} .$$
Then $\mathcal{X}_{\sigma}$ is smooth for $0<|\sigma| \ll 1$ and the singular set $\mathcal{X}_{0}^{\text {sing }}$ is exactly the origin in $\mathbb{C}^{3}$. Since $\mathcal{X}_{\sigma}$ is a smooth surface of general type for $\sigma \neq 0$, it admits a unique Kähler-Einstein metric $\omega_{K E, \sigma}$ of Ricci curvature -1 by the Aubin-Yau theorem [2, 40]. It is also known by [4, 10, 23, 33] that on $\mathcal{X}_{0}^{\text {reg }}$ there exists a unique complete Kähler-Einstein metric $\omega_{K E, 0}$ of Ricci curvature -1. By [33] we have that $\omega_{K E, \sigma} \rightarrow \omega_{K E, 0}$ as $\sigma \rightarrow 0$, locally smoothly on $\mathbb{C}^{3} \backslash B_{\varepsilon}(0)$ for every fixed $\varepsilon>0$. By [10, 13] the end of $\left(\mathcal{X}_{0}^{\text {reg }}, \omega_{K E, 0}\right)$ is asymptotically complex hyperbolic at an optimal rate. This means it is asymptotic to the end of a finite-volume quotient of the complex hyperbolic plane, or in other words, of the unit ball in $\mathbb{C}^{2}$ equipped with the Bergman metric. In particular, the end of $\left(\mathcal{X}_{0}^{\text {reg }}, \omega_{K E, 0}\right)$ is asymptotically locally symmetric, but, of course, $\left(\mathcal{X}_{0}^{\text {reg }}, \omega_{K E, 0}\right)$ cannot be a locally symmetric space.

We view the smoothing of the cuspidal Einstein manifold $\left(\mathcal{X}_{0}^{\text {reg }}, \omega_{K E, 0}\right)$ by the family $\left(\mathcal{X}_{\sigma}, \omega_{K E, \sigma}\right)$ as a kind of cusp closing process, somewhat analogous to Thurston's hyperbolic Dehn surgery and its many generalizations [1, 3, 15, 21, 36], but in another way also quite different because here we have a continuous path of metrics on a fixed smooth 4-manifold. Thus, the picture in our case is actually closer to the usual cuspidal degenerations of hyperbolic Riemann surfaces, which do not exist in higher-dimensional hyperbolic or complex-hyperbolic geometry due to Mostow rigidity. The most interesting difference from the Riemann surface case, and also to some extent from the hyperbolic Dehn surgery situation, is that in our case there is a nontrivial amount of curvature and topology disappearing into the tip of the cusp. Our purpose in this paper is to make this observation precise.

Main Theorem. Fix any $R>0$. For $0<|\sigma| \ll 1$ sufficiently small relative to $R$, restrict the metric $\omega_{K E, \sigma}$ to $\mathcal{X}_{\sigma} \cap B_{|\sigma|^{1 / 3} R}(0)$, multiply it by $|\log | \sigma\left|\left.\right|^{3 / 2}\right.$ and push it forward under the map
$$\left(z_{1}, z_{2}, z_{3}\right) \mapsto \sigma^{-\frac{1}{3}}\left(z_{1}\left(1+z_{1}^{3}\right)^{\frac{1}{3}}, z_{2}\left(1+z_{2}^{3}\right)^{\frac{1}{3}}, z_{3}\left(1+z_{3}^{3}\right)^{\frac{1}{3}}\right) .$$
Then as $\sigma \rightarrow 0$, the $C^{0}$ distance of the resulting Einstein metric on $\left\{z_{1}^{3}+z_{2}^{3}+z_{3}^{3}=1\right\} \cap B_{R / 2}(0)$ to the Tian-Yau gravitational instanton is $O_{R, \varepsilon}\left(|\log | \sigma| |^{-1+\varepsilon}\right)$ for all $\varepsilon>0$. This is the only bubble, and it accounts for the total loss of $L^{2}$-curvature and Euler characteristic (108-9) in the degeneration.

\begin{figure}
\captionsetup{labelformat=empty}
\caption{Figure 1. $\left(\mathcal{X}_{\sigma}, \omega_{K E, \sigma}\right)$ for $0<|\sigma| \ll 1$. The Main Theorem describes the red part.}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/a0f996e3-fe3b-459a-a543-f9d8a2350896-03.jpg?height=892&width=1617&top_left_y=405&top_left_x=254}
\end{figure}

The Tian-Yau gravitational instanton is a complete Ricci-flat Kähler, hence hyper-Kähler metric of volume growth $O\left(r^{4 / 3}\right)$ and curvature decay $O\left(r^{-2}\right)$ on the smooth complex surface $\left\{z_{1}^{3}+z_{2}^{3}+z_{3}^{3}=1\right\}$. Its construction goes back to [38]. There exists more than one such metric even modulo automorphism and scaling. The one that appears in our theorem is characterized by being globally $i \partial \bar{\partial}$-exact and by being asymptotic to a specific model Kähler form at infinity. We emphasize that this model form is completely determined. In particular, it does not even depend on an unknown scaling factor.

See Figure 1 for a rough sketch of the geometry and topology of the main regions of $\left(\mathcal{X}_{\sigma}, \omega_{K E, \sigma}\right)$ shortly before the limit. The Main Theorem is of course proved by a gluing construction, which also yields estimates in every other region of $\mathcal{X}_{\sigma}$. In particular, we recover the locally smooth convergence of $\omega_{K E, \sigma}$ to $\omega_{K E, 0}$ over $\mathcal{X}_{0}^{\text {reg }}$ from [33]. However, most likely none of our estimates are sharp.
1.2. Possible generalizations. We expect that all of our work in this paper goes through
\begin{itemize}
\item[-] for any flat family $\left\{\mathcal{X}_{\sigma}\right\}_{\sigma \in \Delta} \subset \mathbb{C P}^{N} \times \Delta$ of surfaces of general type, embedded by a fixed power of their canonical bundles, such that $\mathcal{X}_{\sigma}$ is smooth for $\sigma \neq 0$,
\item[-] all of the singularities of $\mathcal{X}_{0}$ are cones over elliptic curves,
\item[-] and the finite group $\operatorname{Aut}\left(\mathcal{X}_{0}\right)$ acts transitively on the set of singularities.
\end{itemize}
Under the first two bullet points it is known from [29, Ch 9] that the cones are of degree at most 9. Moreover, any smoothing of such a cone is given by a del Pezzo surface of the same degree containing the elliptic curve as an anticanonical divisor. (For degrees $\geqslant 5$ this is also proved in [29, Ch 9], while for degrees $\leqslant 4$ it follows from the realization of these cones as quasi-homogeneous complete intersections in [31, Satz 1.9] and from the standard deformation theory of complete intersections [22].) We have chosen not to state our theorem in this generality because this would have forced us to introduce a lot of extraneous notation and technical arguments. The third bullet point is a much more pressing issue: as an artifact of our method, we are currently unable to deal with multiple independent singularities.

Roughly speaking, each singularity contributes a 1-dimensional obstruction space to the gluing, and we are currently not dealing with these obstructions in a systematic way-we exploit one "accidental" global degree of freedom, which restricts us to the case of a single singularity modulo $\operatorname{Aut}\left(\mathcal{X}_{0}\right)$.

In principle, the same kind of geometry also occurs in higher dimensions: every affine cone over a projective Calabi-Yau manifold admits Kähler-Einstein model metrics of cuspidal geometry. However, if the Calabi-Yau is flat, these cones are never smoothable in dimension 3 and higher [25]; in particular, they never occur as the infinity divisor in a Tian-Yau manifold that could model the smoothing near the tip of the cusp. For non-flat Calabi-Yaus, this smoothing issue disappears but the cuspidal model metrics have unbounded curvature, so it is impossible to prove (as done in [10, 13] in the flat case) that the global Kähler-Einstein metric on $\mathcal{X}_{0}^{\text {reg }}$ is asymptotic to the cusp model. This is a cuspidal version of the well-known orbifold vs. non-orbifold dichotomy for isolated conical singularities of Kähler-Einstein metrics. The non-orbifold conical case was solved in [17] using Donaldson-Sun theory [12], bypassing the $C^{2}$ estimate in the theory of the complex Monge-Ampère equation. In the cuspidal case one would either need a cuspidal Donaldson-Sun theory, or a very strong $C^{2}$ estimate in unbounded curvature.

In a different direction, in dimension 2, cones over elliptic curves are not the only singularities that can occur on canonically polarized degenerations of smooth surfaces of general type. Such singularities were classified in [24, Thm 4.24]. Examples include normal crossing singularities (see [26] for progress in this direction) as well as the cusps of Hilbert modular surfaces [23, pp.54-57]. The great advantage of the 2-dimensional case is that the natural cuspidal model metrics do have bounded curvature.
1.3. Outline of the proof. There is a very extensive literature on gluing constructions in geometric analysis and more specifically in Kähler geometry, which we will not attempt to survey here. Tian-Yau spaces were used as singularity models in [5] and [18] but the settings of these two papers are rather different from ours. In fact, our setting is in some sense a cubic analog of the classical smoothing of Kähler-Einstein surfaces with nodal singularities via Eguchi-Hanson/Stenzel gravitational instantons. This gluing construction was carried out by Spotti [35] and independently (in greater generality) by Biquard-Rollin [6]. The initial idea of our proof, dating back roughly 10 years, was that something similar can perhaps be done in the cubic situation, based on the following observation.

We identify the singularity $\left\{z_{1}^{3}+z_{2}^{3}+z_{3}^{3}=0\right\} \subset \mathbb{C}^{3}$ with the contraction of the zero section of the total space of a negative line bundle $L$ over the corresponding elliptic curve $E \subset \mathbb{C P}^{2}$. On $L$ we have a unique (up to scaling) Hermitian metric $h$ whose curvature form is minus the flat Kähler form $\omega_{E}$ representing the class $2 \pi c_{1}\left(L^{\prime}\right)$, where $L^{\prime} \rightarrow E$ denotes the line bundle dual to $L$. Thus, as a function on the cubic cone, $h=e^{-\varphi}|z|^{2}$, where $|z|$ is the standard Euclidean radius and $\varphi$ is a 0 -homogeneous function which, viewed as a function $\varphi: E \rightarrow \mathbb{R}$, satisfies $i \partial \bar{\partial} \varphi=\left.\omega_{F S}\right|_{E}-\omega_{E}$. Then the asymptotic model of the Tian-Yau metric is $i \partial \bar{\partial}(\log h)^{3 / 2}$ on $\{h>1\}$ whereas the asymptotic model of the cusp metric is $-3 i \partial \bar{\partial} \log (-\log h)$ on $\{h<1\}$. Define $t:=\log h$. Since the complete Tian-Yau metric, i.e., the relevant gravitational instanton, lives on the smooth surface $\left\{z_{1}^{3}+z_{2}^{3}+z_{3}^{3}=1\right\}$ and since we are interested in the degeneration $\left\{z_{1}^{3}+z_{2}^{3}+z_{3}^{3}=\sigma\right\}$ with $\sigma \rightarrow 0$, it is natural to pull back by the map $z \mapsto \sigma^{-1 / 3} z$ and thus replace $t$ by $t-T$ in the Tian-Yau potential, $T:=(2 / 3) \log |\sigma|$. Then
$$\omega_{\text {cusp }}=-\frac{3}{t} \omega_{E}+\frac{3}{t^{2}} i \partial t \wedge \bar{\partial} t(t<0), \quad \omega_{T Y}=\frac{3}{2}(t-T)^{\frac{1}{2}} \omega_{E}+\frac{3}{4}(t-T)^{-\frac{1}{2}} i \partial t \wedge \bar{\partial} t(t>T) .$$
Thus, both the tangential and the radial metric coefficients match up at $t=(2 / 3) T$ provided that we also rescale $\omega_{T Y}$ by a factor of const $\cdot|T|^{-3 / 2}$. This agreement is surprisingly good. In fact, it lets us write down a pre-glued metric on $\mathcal{X}_{\sigma}$ whose Ricci potential has sup norm $O(1)$ as $\sigma \rightarrow 0$.

However, to enter the gluing regime, it turns out that $O(1)$ needs to be improved to $o(1)$. Here a new idea is needed. By solving a Calabi ansatz we show that $\omega_{\text {cusp }}$ belongs to a 1-parameter family $\omega_{b}$ $(b \in \mathbb{R})$ of radial Kähler-Einstein metrics on the cubic cone such that $\omega_{0}=\omega_{\text {cusp }}$ and $\omega_{b}$ undergoes a
"geometric transition" at $b=0$. For $b>0, \omega_{b}$ extends to the total space of $L$ with an edge singularity along the zero section of $L$. These edge metrics were introduced in [5] and [13]. However, in this paper the case $b<0$ is more relevant. For $b<0, \omega_{b}$ is only defined on a subset $t>T$ of the cubic cone, $T \sim-$ const $\cdot|b|^{-1 / 3}$, and it has a horn singularity: as $t \rightarrow T, \omega_{b} \sim$ const $\cdot|b|^{1 / 2} \cdot i \partial \bar{\partial}(t-T)^{3 / 2}$. This is now a perfect match for the end of the Tian-Yau space, leading to a pre-glued metric whose Ricci potential can be $O\left(|T|^{-(3 / 2)+\varepsilon}\right)$ for any $\varepsilon>0$ if the gluing is done sufficiently close to $t=T$.

Since this decay of the Ricci potential almost matches the scaling factor of the Tian-Yau metric, which is the smallest scale in the construction, it follows from the maximum principle and from Savin's small perturbation theorem [32] that the difference between $\omega_{K E, \sigma}$ and the pre-glued metric goes to zero everywhere except on the Tian-Yau cap. To get control on the cap we need to develop a weighted Hölder space theory as in [6, 35], but unlike in [6, 35] the gluing is obstructed. This is because we are now dealing with three neck regions rather than one: the end of the Tian-Yau space, the cusp of $\mathcal{X}_{0}^{\text {reg }}$, and the new neck coming from the Calabi ansatz $\omega_{b}$ that interpolates between these two. There is a solution to the linearized PDE on the new neck that approaches 1 on the Tian-Yau side and 0 on the cusp side, and we have been unable to rule out this solution using any choice of weight. We use an ad hoc trick to get around this issue (which however prevents us from dealing with multiple independent singularities): the Ricci potential is only defined modulo a constant, and while changing this constant is the same as adding a constant to the solution of the Monge-Ampère equation, the "Einstein modulo obstructions" metric in the sense of [28] reacts in a nontrivial way to this change.
1.4. Acknowledgments. We thank O. Biquard and H. Guenancia for some very helpful discussions about the Calabi ansatz, B. Ammann, G. Tian and V. Tosatti for pointing out references [21], [8, 37] and [25], respectively, and an anonymous referee for suggestions that greatly improved our exposition. XF was supported by National Key R\&D Program of China 2024YFA1014800 and NSFC No. 12401073. HJH was partially supported by the German Research Foundation (DFG) under Germany's Excellence Strategy EXC 2044-390685587 "Mathematics Münster: Dynamics-Geometry-Structure" as well as by the CRC 1442 "Geometry: Deformations and Rigidity" of the DFG.

\section*{2. Building blocks of the gluing}
2.1. Degenerations of projective surfaces of general type. In this subsection, we give a family of canonically polarized surfaces $\mathcal{X}$ over the disk $\Delta$. Let $\mathcal{X}$ be a family of degree 6 surfaces (hence canonically polarized) in $\mathbb{C P}^{3}$ as follows:
$$\mathcal{X}_{\sigma}:=\left\{\left(Z_{1}^{6}+Z_{1}^{3} Z_{0}^{3}\right)+\left(Z_{2}^{6}+Z_{2}^{3} Z_{0}^{3}\right)+\left(Z_{3}^{6}+Z_{3}^{3} Z_{0}^{3}\right)=\sigma Z_{0}^{6}\right\} .$$
When $Z_{0} \neq 0$, in the affine coordinates $z_{1}=\frac{Z_{1}}{Z_{0}}, z_{2}=\frac{Z_{2}}{Z_{0}}, z_{3}=\frac{Z_{3}}{Z_{0}}, \mathcal{X}_{\sigma}$ is defined by
$$\left(z_{1}^{6}+z_{1}^{3}\right)+\left(z_{2}^{6}+z_{2}^{3}\right)+\left(z_{3}^{6}+z_{3}^{3}\right)=\sigma .$$
It is easy to see that this affine surface is smooth for $0<|\sigma| \ll 1$, that the origin is its unique singular point for $\sigma=0$, and that this singularity is locally analytically isomorphic (via $z_{i} \mapsto z_{i}\left(1+z_{i}^{3}\right)^{1 / 3}$ for $i=1,2,3)$ to the singularity defined by the equation
$$z_{1}^{3}+z_{2}^{3}+z_{3}^{3}=0 .$$
Also, when $Z_{0}=0, \mathcal{X}_{\sigma}$ is smooth for every $\sigma$. For instance, by symmetry, let us assume $Z_{1} \neq 0$. Then we may take affine coordinates $w_{1}=\frac{Z_{0}}{Z_{1}}, w_{2}=\frac{Z_{2}}{Z_{1}}, w_{3}=\frac{Z_{3}}{Z_{1}}$. Then the singular locus of $\mathcal{X}_{\sigma}$ will be the
common zeros of the following system of equations:
$$\begin{aligned}
1+w_{1}^{3}+w_{2}^{6}+w_{2}^{3} w_{1}^{3}+w_{3}^{6}+w_{3}^{3} w_{1}^{3}-\sigma w_{1}^{6} & =0, \\
3 w_{1}^{2}+3 w_{2}^{3} w_{1}^{2}+3 w_{3}^{3} w_{1}^{2}-6 \sigma w_{1}^{5} & =0, \\
6 w_{2}^{5}+3 w_{2}^{2} w_{1}^{3} & =0, \\
6 w_{3}^{5}+3 w_{3}^{2} w_{1}^{3} & =0 .
\end{aligned}$$
Now observe that if $w_{1}=0$, then it is easy to see that the above system has no common zeros for all values of $\sigma$. Hence when $Z_{0}=0, \mathcal{X}_{\sigma}$ is smooth for all $\sigma$.

Obviously $\left.K_{\mathcal{X}_{\sigma}} \cong \mathcal{O}(2)\right|_{\mathcal{X}_{\sigma}}$. So let us denote the zero locus of the linear homogeneous polynomial $Z_{0}$ on $\mathcal{X}_{\sigma}$ by $\mathcal{D}_{\sigma}$. Also set $\mathcal{Y}_{\sigma}:=\mathcal{X}_{\sigma} \backslash \mathcal{D}_{\sigma}$. Then
$$\mathcal{Y}_{\sigma}=\left\{\left(z_{1}^{6}+z_{1}^{3}\right)+\left(z_{2}^{6}+z_{2}^{3}\right)+\left(z_{3}^{6}+z_{3}^{3}\right)=\sigma\right\} \subset \mathbb{C}^{3} .$$
From what we said it is clear that there is a section $\Omega$ of the relative canonical bundle $K_{\mathcal{X}_{\sigma} / \Delta}$ whose restriction to $\mathcal{Y}_{\sigma}$ is a nonvanishing holomorphic volume form $\Omega_{\sigma}$ with a zero of order 2 at $\mathcal{D}_{\sigma}$.

Remark 2.1. We remark that up to scaling $\Omega_{\sigma}$ is the unique holomorphic volume form on the affine manifold $\mathcal{Y}_{\sigma}$ with zeros or poles along $\mathcal{D}_{\sigma}$. Indeed, if $\hat{\Omega}_{\sigma}$ is any other such form, then $H_{\sigma}:=\Omega_{\sigma} / \hat{\Omega}_{\sigma}$ is a nowhere vanishing holomorphic function on $\mathcal{Y}_{\sigma}$ with zeros or poles along $\mathcal{D}_{\sigma}$. Thus, either $H_{\sigma}$ or $1 / H_{\sigma}$ extends to a holomorphic function on $\mathcal{X}_{\sigma}$ and is therefore constant. More generally, in order to conclude $H_{\sigma}=$ const it suffices to assume that $\hat{\Omega}_{\sigma}$ has at most polynomial growth near $\mathcal{D}_{\sigma}$.

By equation (2.2), we know that near the singularity, the family $\mathcal{X}_{\sigma}$ is locally analytically isomorphic to the following family of Tian-Yau spaces (this terminology will become clear in Section 2.3)
$$T Y_{\sigma}:=\left\{z_{1}^{3}+z_{2}^{3}+z_{3}^{3}=\sigma\right\} .$$
We remark here that $T Y_{0}$ is obviously the affine cone over a smooth elliptic curve $E \subset \mathbb{C P}^{2}$. Thus, for the specific singularity $z=0$ in $T Y_{0}$, there is a log resolution of singularities
$$\pi: \hat{L} \rightarrow T Y_{0}$$
with exceptional divisor $E$. Here $L \rightarrow E$ denotes a negative line bundle, $\hat{L}$ denotes the total space of $L$ and $\pi$ is the contraction of the zero section of $\hat{L}$. We also remark that $T Y_{\sigma}$ is a family of affine varieties in $\mathbb{C}^{3} \times \mathbb{C} \subset \mathbb{C} \mathbb{P}^{3} \times \mathbb{C}$ and it can be compactified in $\mathbb{C P}^{3} \times \mathbb{C}$ by adding the divisor
$$E=\left\{Z_{1}^{3}+Z_{3}^{3}+Z_{3}^{3}=0\right\}$$
independently of $\sigma$, where $Z_{i}$ are the homogeneous coordinates on $\mathbb{C P}^{3}$.
Next, we fix an identification of $T Y_{\sigma}$ and $\mathcal{Y}_{\sigma}$ locally near the singularity.
Definition 2.2. We define a local analytic isomorphism of the family $\Psi_{\sigma}: \mathcal{Y}_{\sigma} \rightarrow T Y_{\sigma}$ as follows:
$$\Psi_{\sigma}\left(z_{1}, z_{2}, z_{3}\right):=\left(z_{1}\left(1+z_{1}^{3}\right)^{\frac{1}{3}}, z_{2}\left(1+z_{2}^{3}\right)^{\frac{1}{3}}, z_{3}\left(1+z_{3}^{3}\right)^{\frac{1}{3}}\right) .$$
From the implicit function theorem, it is clear that $\Psi_{\sigma}$ is invertible near $\left(z_{1}, z_{2}, z_{3}\right)=(0,0,0)$.
We will also need to identify $T Y_{0}$ with $T Y_{1}$ in some fixed neighborhood of infinity of the two spaces. Of course, this can only be done diffeomorphically, not biholomorphically.

Lemma 2.3 ([9, Lemma 5.5]). There exist $R>0$ and a smooth function $\nu: \mathbb{C}^{3} \backslash \bar{B}_{R} \rightarrow \mathbb{C}$ such that
$$\sum_{i=1}^{3}\left(z_{i}+\nu(z) \bar{z}_{i}^{2}\right)^{3}=1$$
for all $z \in T Y_{0} \backslash \bar{B}_{R}$. Moreover, $\partial^{k} \nu(z)=O\left(|z|^{-4-k}\right)$ as $|z| \rightarrow \infty$ for all $k \geqslant 0$.

Proof. Taking complex coordinates $z=\left(z_{1}, z_{2}, z_{3}\right)$ on $S^{5} \subset \mathbb{C}^{3}$, define a function $f$ by
$$f: S^{5} \times[0, \infty) \times \mathbb{C} \rightarrow \mathbb{C}, \quad f(z, r, y)=3 y\left(\sum_{i=1}^{3}\left|z_{i}\right|^{4}\right)+3 y^{2}\left(\sum_{i=1}^{3}\left|z_{i}\right|^{2} \bar{z}_{i}^{3}\right)+y^{3}\left(\sum_{i=1}^{3} \bar{z}_{i}^{6}\right)-r^{3},$$
and fix any point $p=\left(p_{1}, p_{2}, p_{3}\right) \in S^{5}$. Since
$$f(p, 0,0)=0, \quad \frac{\partial f}{\partial y}(p, 0,0)=3 \sum_{i=1}^{3}\left|p_{i}\right|^{4} \neq 0,$$
the implicit function theorem asserts the existence of a unique smooth function $g_{p}$, defined in some open neighborhood $U_{p} \times\left[0, \varepsilon_{p}\right)$ of $(p, 0)$, such that $g_{p}(p, 0)=0$ and $f\left(z, r, g_{p}(z, r)\right)=0$. An obvious covering argument on $S^{5}$ then yields a smooth function $g: S^{5} \times[0, \varepsilon) \rightarrow \mathbb{C}$ satisfying
$$g(z, 0)=0, \quad f(z, r, g(z, r))=0 .$$
We now set $R=\varepsilon^{-1}$ and define $\nu: \mathbb{C}^{3} \backslash \bar{B}_{R} \rightarrow \mathbb{C}$ by
$$\nu(z)=\frac{1}{|z|} g\left(\frac{z}{|z|}, \frac{1}{|z|}\right) .$$
The fact that $\nu$ satisfies $\sum_{i=1}^{3}\left(z_{i}+\nu(z) \bar{z}_{i}^{2}\right)^{3}=1$ for each $z \in T Y_{0} \backslash \bar{B}_{R}$ is straightforward to verify.
Now we show that $\nu(z)=O\left(|z|^{-4}\right)$. To see this, observe that $\nu(z)|z|^{4} P(z)=1$ on $\mathbb{C}^{3} \backslash \bar{B}_{R}$, where
$$P(z)=3\left(\sum_{i=1}^{3} \frac{\left|z_{i}\right|^{4}}{|z|^{4}}\right)+3(\nu(z)|z|)\left(\sum_{i=1}^{3} \frac{\left|z_{i}\right|^{2} \bar{z}_{i}^{3}}{|z|^{5}}\right)+(\nu(z)|z|)^{2}\left(\sum_{i=1}^{3} \frac{\bar{z}_{i}^{6}}{|z|^{6}}\right) .$$
It then suffices to note that $\nu(z)|z|=g\left(\frac{z}{|z|}, \frac{1}{|z|}\right) \rightarrow 0$ uniformly as $|z| \rightarrow \infty$.
In order to complete the proof of the lemma, we show that $\partial^{k} \nu(z)=O\left(|z|^{-4-k}\right)$ for all $k \geqslant 1$. We only do this for $k=1$. To this end, note that $\nu(z)=1 /\left(|z|^{4} P(z)\right)$. Thus, using the expression of $P(z)$ in (2.15), it suffices to show that $\partial(\nu(z)|z|)=O\left(|z|^{-1}\right)$. But this follows from (2.14) and from the fact that $g$ is a smooth function on $S^{5} \times[0, \varepsilon)$. The lemma is proved. \(\square\)

Now we define a diffeomorphism $\Phi$ from $T Y_{0} \backslash \bar{B}_{R}$ onto its image contained in $T Y_{1}$ as follows:
$$\Phi\left(z_{1}, z_{2}, z_{3}\right):=\left(z_{1}+\nu(z) \bar{z}_{1}^{2}, z_{2}+\nu(z) \bar{z}_{2}^{2}, z_{3}+\nu(z) \bar{z}_{3}^{2}\right) .$$
With this, we can trivialize the family $T Y_{\sigma}$ diffeomorphically at infinity.
Definition 2.4. Let $\Phi$ be defined by (2.16), $m_{\sigma}^{\prime}: T Y_{0} \rightarrow T Y_{0}$ by sending $z$ to $\sigma^{-1 / 3} z$ and $m_{\sigma}: T Y_{\sigma} \rightarrow$ $T Y_{1}$ by sending $z$ to $\sigma^{-1 / 3} z$. Then we define a family of maps $\Phi_{\sigma}: T Y_{0} \backslash B_{|\sigma|^{1 / 3} R} \rightarrow T Y_{\sigma}$ by
$$\Phi_{\sigma}:=m_{\sigma}^{-1} \circ \Phi \circ m_{\sigma}^{\prime} .$$

Lemma 2.5. Let $z \in T Y_{0}$ with $|z| \geqslant|\sigma|^{1 / 3} R$ and also set $\nu_{\sigma}(z):=\sigma^{-1 / 3} \nu\left(\sigma^{-1 / 3} z\right)$. Then
$$\Phi_{\sigma}\left(z_{1}, z_{2}, z_{3}\right)=\left(z_{1}+\nu_{\sigma}(z) \bar{z}_{1}^{2}, z_{2}+\nu_{\sigma}(z) \bar{z}_{2}^{2}, z_{3}+\nu_{\sigma}(z) \bar{z}_{3}^{2}\right)$$
with $\partial^{k} \nu_{\sigma}(z)=O\left(|\sigma||z|^{-4-k}\right)$ as $|\sigma|^{-1 / 3}|z| \rightarrow \infty$ for all $k \geqslant 0$.
Proof. By (2.17), for $z \in T Y_{0}$,
$$\Phi_{\sigma}\left(z_{1}, z_{2}, z_{3}\right)=\left(z_{1}+\sigma^{-\frac{1}{3}} \nu\left(\sigma^{-\frac{1}{3}} z\right) \bar{z}_{1}^{2}, z_{2}+\sigma^{-\frac{1}{3}} \nu\left(\sigma^{-\frac{1}{3}} z\right) \bar{z}_{2}^{2}, z_{3}+\sigma^{-\frac{1}{3}} \nu\left(\sigma^{-\frac{1}{3}} z\right) \bar{z}_{3}^{2}\right) .$$
Recall that $\partial^{k} \nu(z)=O\left(|z|^{-4-k}\right)$ as $|z| \rightarrow \infty$ for all $k \geqslant 0$. Thus,
$$\partial^{k} \nu_{\sigma}(z)=\sigma^{-\frac{1+k}{3}}\left(\partial^{k} \nu\right)\left(\sigma^{-\frac{1}{3}} z\right)=O\left(|\sigma|^{-\frac{1+k}{3}}\left(|\sigma|^{-\frac{1}{3}}|z|\right)^{-4-k}\right)=O\left(|\sigma||z|^{-4-k}\right)$$
as $|\sigma|^{-1 / 3}|z| \rightarrow \infty$. \(\square\)

Remark 2.6. By Lemma 2.5, $\Phi_{\sigma}$ is well-defined if $|z| \geqslant|\sigma|^{1 / 3} R$ for some sufficiently large but fixed $R \gg 1$. However, the gluing will later be carried out in a region where $|z|$ is much larger than this. More precisely, the gluing region is $|z|=|\sigma|^{1 / 3} e^{\left.\zeta \cdot|\log | \sigma\right|^{\alpha}}$ for some fixed $\alpha<\frac{1}{2}$ and for $\zeta \in[1,2]$.

Lastly, we use the above identifications to trivialize the family $\left\{\mathcal{X}_{\sigma}\right\}_{\sigma \in \Delta}$ diffeomorphically away from smaller and smaller neighborhoods of the singularity $(0,0,0) \in \mathcal{X}_{0} \subset \mathbb{C}^{3}$.

Lemma 2.7. There exists a $C^{5}$ diffeomorphism $G_{\sigma}$ from $\mathcal{X}_{0} \backslash\left\{|z| \leqslant 3|\sigma|^{1 / 3} R\right\}$ onto its image, which is contained in $\mathcal{X}_{\sigma} \backslash\left\{|z| \leqslant 2|\sigma|^{\frac{1}{3}} R\right\}$ and contains $\mathcal{X}_{\sigma} \backslash\left\{|z| \leqslant 4|\sigma|^{1 / 3} R\right\}$, such that the following hold:
\begin{itemize}
\item[(1)] $G_{\sigma}$ is smooth away from the hyperplane $\left\{Z_{0}=0\right\}$ and is the identity on this hyperplane.
\item[(2)] Fix $R_{0} \ll 1$ so that $\Psi$ is defined on $|z| \leqslant 3 R_{0}$. Then $G_{\sigma}=\Psi_{\sigma}^{-1} \circ \Phi_{\sigma} \circ \Psi_{0}$ for $|z| \leqslant R_{0}$.
\item[(3)] If we denote the complex structure of $\mathcal{X}_{\sigma}$ by $J_{\sigma}$, then for any $r_{0}>0$ and any smooth metric $\omega_{0}$ on $\mathcal{X}_{0} \backslash\left\{|z|<r_{0}\right\}$ we have that
$$\left|\nabla_{\omega_{0}}^{k}\left(G_{\sigma}^{*} J_{\sigma}-J_{0}\right)\right|_{\omega_{0}}=O_{r_{0}, \omega_{0}}(|\sigma|) \text { on } \mathcal{X}_{0} \backslash\left\{|z|<r_{0}\right\}$$
for all $\sigma$ sufficiently small depending on $r_{0}$ and for all $0 \leqslant k \leqslant 4$.
\end{itemize}

Proof. By construction, $\mathcal{X}=\left\{(Z, \sigma) \in \mathbb{C P}^{3} \times \Delta: p(Z)=\sigma Z_{0}^{6}\right\}$ for a certain homogeneous sextic $p$. By (2.4), all fibers $\mathcal{X}_{\sigma}=\left\{Z \in \mathbb{C P}^{3}:(Z, \sigma) \in \mathcal{X}\right\}$ intersect the plane $\left\{Z_{0}=0\right\}$ transversely in the smooth curve $\left\{Z_{0}=0, Z_{1}^{6}+Z_{2}^{6}+Z_{3}^{6}=0\right\}$. Write $\mathbb{A}^{3}$ to denote the affine chart $\left\{Z_{0} \neq 0\right\}$ and define
$$q: \mathbb{A}^{3} \rightarrow \mathbb{C}, \quad q(Z):=p(Z) / Z_{0}^{6} .$$
Let $\nabla q$ denote the type $(1,0)$ gradient of $q$ with respect to the standard Euclidean Kähler metric on $\mathbb{A}^{3}$ and let $|\nabla q|$ denote the Euclidean length of $\nabla q$. Then the smooth (1, 0)-vector field
$$V:=\left(\frac{\nabla q}{|\nabla q|^{2}}, 1\right) \in T^{1,0}\left(\mathbb{A}^{3} \times \Delta\right)$$
is defined at all points of the submanifold $\mathcal{X}^{\prime}:=\left(\mathcal{X} \backslash \mathcal{X}_{0}^{\text {sing }}\right) \cap\left(\mathbb{A}^{3} \times \Delta\right)$ and is tangent to $\mathcal{X}^{\prime}$. In fact, the time- $\sigma$ flow of $V$ maps the fiber $\mathcal{X}_{\tau}^{\prime}$ into the fiber $\mathcal{X}_{\tau+\sigma}^{\prime}$ for every $\tau$.

Claim 2.8. $V$ extends from $\mathcal{X}^{\prime}$ to $\mathcal{X} \backslash \mathcal{X}_{0}^{\text {sing }}$ as a $C^{5}$ vector field vanishing along the infinity divisor.
Proof of Claim 2.8. It suffices to check this in the chart $\left\{Z_{1} \neq 0\right\}$. Define affine coordinates $w_{1}=$ $Z_{0} / Z_{1}, w_{2}=Z_{2} / Z_{1}, w_{3}=Z_{3} / Z_{1}$ on this chart. Then $d\left(1 / w_{1}\right), d\left(w_{2} / w_{1}\right), d\left(w_{3} / w_{1}\right)$ are an orthonormal $(1,0)$-coframe with respect to the standard Euclidean metric on $\mathbb{A}^{3}=\left\{w_{1} \neq 0\right\}$. The following (0, 1)-frame (written as vectors with respect to $\partial_{\bar{w}_{1}}, \partial_{\bar{w}_{2}}, \partial_{\bar{w}_{3}}$ ) is metrically dual to this coframe:
$$V_{1}:=\left(-w_{1}^{2},-w_{1} w_{2},-w_{1} w_{3}\right), \quad V_{2}:=\left(0, w_{1}, 0\right), \quad V_{3}:=\left(0,0, w_{1}\right) .$$
With $\psi(t):=t^{6}+t^{3}$ we then have that $q=\psi\left(1 / w_{1}\right)+\psi\left(w_{2} / w_{1}\right)+\psi\left(w_{3} / w_{1}\right)$ and so
$$\overline{\nabla q}=\psi^{\prime}\left(\frac{1}{w_{1}}\right) V_{1}+\psi^{\prime}\left(\frac{w_{2}}{w_{1}}\right) V_{2}+\psi^{\prime}\left(\frac{w_{3}}{w_{1}}\right) V_{3} .$$
It follows that $\left|w_{1}\right|^{10}|\nabla q|^{2}$ is smooth and $\geqslant 36$ at $\left\{w_{1}=0\right\}$. Using this fact and the transversality of $\mathcal{X}$ to the hyperplane $\left\{Z_{0}=0\right\} \times \Delta$, we get that the $T^{1,0} \mathbb{C P}^{3}$ component of $V$ vanishes to order 6 at the infinity divisor in $\mathcal{X}$. Thus, $V$ extends as a $C^{5}$ vector field. \(\square\)

We may assume that $C^{-1} \leqslant|V|_{\omega_{0}} \leqslant C$ for some positive constant $C$ on the set $|z| \geqslant \frac{R_{0}}{2}$. Consider the flow $H_{t}$ induced by $V$ on $\mathcal{X}^{\prime} \backslash\left\{|z|<\frac{R_{0}}{2}\right\}$. For $\sigma$ sufficiently small, $H_{\sigma}$ induces a diffeomorphism from $\mathcal{X}_{0}^{\prime} \backslash\left\{|z|<\frac{3 R_{0}}{4}\right\}$ onto its image in $\mathcal{X}_{\sigma}^{\prime}$. Here we use the fact that $|V|_{\omega_{0}}$ is uniformly bounded on $\mathcal{X}^{\prime} \backslash\left\{|z|<\frac{R_{0}}{2}\right\}$, so the incompleteness of $\mathcal{X}^{\prime}$ does not affect that $H_{\sigma}$ is a diffeomorphism when $\sigma$ is sufficiently small and $|z| \geqslant \frac{3 R_{0}}{4}$. It follows that on the strip $S:=\left\{R_{0} \leqslant|z| \leqslant 2 R_{0}\right\} \cap \mathcal{X}_{0}$ we have two
diffeomorphisms $\Psi_{\sigma}^{-1} \circ \Phi_{\sigma} \circ \Psi_{0}$ and $H_{\sigma}$ onto some region of $\mathcal{X}_{\sigma}$. Use the map $\Psi_{\sigma}^{-1} \circ \Phi_{\sigma} \circ \Psi_{0}$ to identify $S$ with its image inside $\mathcal{X}_{\sigma}$. Under this identification, $H_{\sigma}$ can be seen as a family of embeddings
$$\tilde{H}_{\sigma}: S^{\prime} \rightarrow S$$
from $S^{\prime}:=\left\{1.1 R_{0} \leqslant|z| \leqslant 1.9 R_{0}\right\} \cap \mathcal{X}$ into $S$. Since $\tilde{H}_{\sigma} \rightarrow \operatorname{Id}_{S^{\prime}}$ as $\sigma \rightarrow 0, \tilde{H}_{\sigma}$ is smoothly isotopic to the identity map on $S^{\prime}$ when $\sigma$ is sufficiently small. In particular, $\tilde{H}_{\sigma}$ is given by the flow of a time-dependent vector field $\tilde{V}_{\sigma}$ defined on $\tilde{H}_{\sigma}\left(S^{\prime}\right)$. Let $\tau: S \rightarrow[0,1]$ be a smooth cut-off function given by $\tau(z)=\chi(|z|)$, where $\chi$ is a smooth increasing function equal to zero for $|z| \leqslant 1.3 R_{0}$ and equal to 1 for $|z| \geqslant 1.7 R_{0}$. Let $\tilde{I}_{\sigma}$ be the diffeomorphisms generated by the vector field $\tau \tilde{V}_{\sigma}$ for $\sigma$ sufficiently small. By construction, $\tilde{I}_{\sigma}$ is equal to the identity for $|z| \leqslant 1.2 R_{0}$ and equal to $\tilde{H}_{\sigma}$ for $|z| \geqslant 1.8 R_{0}$. Thus, the diffeomorphism
$$G_{\sigma}:= \begin{cases}\Psi_{\sigma}^{-1} \circ \Phi_{\sigma} \circ \Psi_{0} \circ \tilde{I}_{\sigma} & \text { for }|z| \leqslant 1.8 R_{0}, \\ H_{\sigma} & \text { for }|z| \geqslant 1.8 R_{0},\end{cases}$$
satisfies the desired properties. \(\square\)
2.2. Singular Kähler-Einstein metrics with hyperbolic cusps. Let $\mathcal{X}=\left\{\mathcal{X}_{\sigma}\right\}_{\sigma \in \Delta}$ be the family of sextic surfaces in $\mathbb{C P}^{3}$ discussed above. Recall that we have removed a family of hyperplane sections $\mathcal{D}=\left\{\mathcal{D}_{\sigma}\right\}_{\sigma \in \Delta}$ with $\left[2 \mathcal{D}_{\sigma}\right]=K_{\mathcal{X}_{\sigma}}$ for all $\sigma \in \Delta$, thus defining a family of affine surfaces $\mathcal{Y}_{\sigma}=\mathcal{X}_{\sigma} \backslash \mathcal{D}_{\sigma}$, and that we have also fixed a family of holomorphic volume forms $\Omega_{\sigma}$ (unique up to scaling) on $\mathcal{Y}_{\sigma}$ that vanish to order 2 along the infinity divisors $\mathcal{D}_{\sigma}$.

It is a well-known fact that the regular part of $\mathcal{X}_{0}$ admits a unique complete Kähler-Einstein metric $\omega_{K E, 0}$ with Ricci curvature -1. This fact can nowadays be viewed as a very special case of a general theory of complete Kähler-Einstein metrics on log-canonical models; see [4, Thm A] and [33, Section 3]. However, in the 2-dimensional case-particularly for surfaces of general type with elliptic singularities such as our $\mathcal{X}_{0}$-the required existence result actually goes back to work of R. Kobayashi [23, Thm 1] and of Cheng-Tian-Yau [8, 37]. We now briefly review the construction of $\omega_{K E, 0}$ in our example.

In our example, recall that $\left.K_{\mathcal{X}_{\sigma}} \cong \mathcal{O}(2)\right|_{\mathcal{X}_{\sigma}}$. Fix the embedding $\mathbb{C P}^{3} \rightarrow \mathbb{C P}^{9}$ induced by $\mathcal{O}(2)$ as
$$\left[Z_{0}, Z_{1}, Z_{2}, Z_{3}\right] \longrightarrow\left[Z_{0}^{2}, Z_{0} Z_{1}, Z_{0} Z_{2}, Z_{0} Z_{3}, Z_{1}^{2}, Z_{1} Z_{2}, Z_{1} Z_{3}, Z_{2}^{2}, Z_{2} Z_{3}, Z_{3}^{2}\right] .$$
Restricting the Fubini-Study metric on $\mathbb{C P}^{9}$ to the image of $\mathbb{C P}^{3}$, we have
$$\begin{aligned}
\omega_{F S} & :=i \partial \bar{\partial} \log \left(\left|Z_{0}^{2}\right|^{2}+\left|Z_{0} Z_{1}\right|^{2}+\left|Z_{0} Z_{2}\right|^{2}+\left|Z_{0} Z_{3}\right|^{2}+\left|Z_{1}^{2}\right|^{2}+\left|Z_{1} Z_{2}\right|^{2}+\left|Z_{1} Z_{3}\right|^{2}\right. \\
& \left.+\left|Z_{2}^{2}\right|^{2}+\left|Z_{2} Z_{3}\right|^{2}+\left|Z_{3}^{2}\right|^{2}\right) .
\end{aligned}$$
On the affine piece $Z_{0} \neq 0$, we set
$$\psi_{F S}:=\log \left(1+\left|z_{1}\right|^{2}+\left|z_{2}\right|^{2}+\left|z_{3}\right|^{2}+\left|z_{1}\right|^{4}+\left|z_{1} z_{2}\right|^{2}+\left|z_{1} z_{3}\right|^{2}+\left|z_{2}\right|^{4}+\left|z_{2} z_{3}\right|^{2}+\left|z_{3}\right|^{4}\right) .$$
For better emphasis, we also introduce the notation
$$\omega_{F S, \sigma}:=\left.\omega_{F S}\right|_{\mathcal{X}_{\sigma}}, \psi_{F S, \sigma}:=\left.\psi_{F S}\right|_{\mathcal{Y}_{\sigma}} \text { for all } \sigma \in \Delta .$$
Now let us fix a volume form $V$ on $\mathcal{X}_{0}$, which is induced by the Fubini-Study metric of the line bundle $\mathcal{O}(1)$ on $\mathbb{C P}^{9}$, such that
$$\omega_{F S, 0}=i \partial \bar{\partial} \log V .$$
Then the complex Monge-Ampère equation of interest on $\mathcal{X}_{0}$ is given by
$$\left(\omega_{F S, 0}+i \partial \bar{\partial} \psi_{0}\right)^{2}=e^{\psi_{0}} V .$$
We have the following existence result from [23, Thm 1], [4, Thm C], [33, Lemma 3.6], together with an asymptotic estimate of the solution $\psi_{0}$ from [11, Prop D], [34, Prop 3.1], [10, Thm 1.1].

Theorem 2.9. The equation (2.33) admits a solution $\psi_{0} \in C^{\infty}\left(\mathcal{X}_{0}^{\text {reg }}\right)$ satisfying
$$-(3+\varepsilon) \log \left(-\log \left|\sigma_{E}\right|_{h_{E}}\right)-C_{\varepsilon} \leqslant \pi^{*}\left(\Psi_{0}^{-1}\right)^{*} \psi_{0} \leqslant C$$
for every $\varepsilon>0$, where $\pi$ is the resolution (2.7), $\sigma_{E}$ is a defining section of $E$ inside the total space $\hat{L}$ and $h_{E}$ is any Hermitian metric on $L \rightarrow E$.

It will be convenient to rewrite the Monge-Ampère equation (2.33) in the following manner.
Lemma 2.10. Define $\psi_{K E, 0}:=\psi_{0}+\psi_{F S, 0}$, where $\psi_{0}$ is the solution provided by Theorem 2.9. Then, after adding a constant to $\psi_{K E, 0}$, the Kähler-Einstein metric $\omega_{K E, 0}:=i \partial \bar{\partial} \psi_{K E, 0}$ satisfies
$$\log \frac{\omega_{K E, 0}^{2}}{\Omega_{0} \wedge \bar{\Omega}_{0}}=\psi_{K E, 0} .$$
Proof. By construction, (2.33), we have that
$$\log \frac{\omega_{K E, 0}^{2}}{V}=\psi_{K E, 0}-\psi_{F S, 0} .$$
Recall that by definition, $V$ is the unique real volume form on the regular part of $\mathcal{X}_{0}$ that, viewed as a Hermitian metric on $K_{\mathcal{X}_{0}}$, maps to the Fubini-Study metric $h_{F S}$ under the adjunction isomorphisms $K_{\mathcal{X}_{0}} \cong \mathcal{O}_{\mathbb{C P}^{3}}(2)\left|\mathcal{X}_{0} \cong \mathcal{O}_{\mathbb{C P}^{9}}(1)\right|_{\mathcal{X}_{0}}$. On the other hand, also by construction, $\Omega_{0}$ vanishes to order 2 along the hyperplane section $\mathcal{D}_{0}=\mathcal{X}_{0} \backslash \mathcal{Y}_{0}$ and vanishes nowhere else. Thus, under the above adjunctions, $\Omega_{0}$ maps to some nonzero multiple of the section $S$ of $\left.\mathcal{O}_{\mathbb{C P}^{9}}(1)\right|_{\mathcal{X}_{0}}$ that cuts out the hyperplane $\mathcal{D}_{0}$. The square of the Hermitian norm of $\Omega_{0}$ with respect to $V$ is $\left(\Omega_{0} \wedge \bar{\Omega}_{0}\right) / V$, and $|S|_{h_{F S}}^{2}=-\psi_{F S, 0}$. Thus, we get (2.35) from (2.36) by adding $\psi_{F S, 0}+$ const to both sides. \(\square\)

We now turn to a more precise asymptotic description of $\psi_{K E, 0}$ near the singularity $p \in \mathcal{X}_{0}$. After introducing the relevant radial model potential $\psi_{\text {cusp }}$ and proving some technical lemmas, we will give the precise asymptotics of $\psi_{K E, 0}$ in Proposition 2.14, which is the final result of this section.

Working on the line bundle $L$ whose total space $\hat{L}$ resolves the singularity, let $h$ denote the Hermitian metric on $L$ (unique up to scale) whose curvature form is minus the flat Kähler form $\omega_{E}$ representing $2 \pi c_{1}\left(L^{\prime}\right) \in H^{1,1}(E, \mathbb{R})$. Here $L^{\prime}$ denotes the dual of $L$. We also denote the positively curved Hermitian metric dual to $h$ by $h^{\prime}$. Abusing notation, we view $h$ as a function on the total space of $L$ via
$$h: \hat{L} \rightarrow \mathbb{R}, \quad \xi \mapsto|\xi|_{h}^{2} .$$
We consider radial Kähler metrics $\omega=i \partial \bar{\partial} \psi(t)$ on $\{0<h \leqslant \delta\}$, where $\psi:(-\infty, \log \delta] \rightarrow \mathbb{R}$ and
$$t:=\log h .$$
Since the discussion of these model Kähler metrics (here as well as in all subsequent sections) works more or less the same way in all dimensions $n$ with $\left(L^{\prime}, h^{\prime}\right) \rightarrow\left(E, \omega_{E}\right)$ a polarized compact Calabi-Yau $(n-1)$-fold, we prefer to not specialize our computations of these metrics to the case $n=2$.

Continuing to work in the general $n$-dimensional setting, we fix a nowhere vanishing holomorphic $(n-1)$-form $\Omega_{E}$ on $E$ with
$$\omega_{E}^{n-1}=i^{(n-1)^{2}} \Omega_{E} \wedge \bar{\Omega}_{E} .$$
Note that $\Omega_{E}$ is unique up to multiplication by a unit complex number. Using this, we now construct a holomorphic volume form $\Omega_{\mathcal{C}}$ on the total space of the $\mathbb{C}^{*}$-bundle associated with $L$ or $L^{\prime}$, i.e., on the complement of the zero section in the total space of either one of these two line bundles. This form $\Omega_{\mathcal{C}}$ will be unique up to sign, and will have first-order poles along both zero sections such that its residues at these poles are equal to $\pm \Omega_{E}$. Precisely, let $p$ denote the bundle projection from the total space of
the $\mathbb{C}^{*}$-bundle onto $E$ and let $\pm Z$ denote the $(1,0)$-vector field on the total space that generates the natural $\mathbb{C}^{*}$-action coming from either $L$ or $L^{\prime}$. Then $\Omega_{\mathcal{C}}$ is determined by the equation
$$\pm Z\lrcorner \Omega_{\mathcal{C}}=p^{*} \Omega_{E} .$$

A radial (1, 1)-form $\omega=i \partial \bar{\partial} \psi(t)$ as above is positive definite if and only if
$$\psi^{\prime}(t), \psi^{\prime \prime}(t)>0 .$$
Then $\omega$ is a Kähler-Einstein metric if (2.41) holds and
$$\left(\psi^{\prime}\right)^{n-1} \psi^{\prime \prime}=e^{\psi+a}$$
for some $a \in \mathbb{R}$. If $\psi$ satisfies (2.42), then given any $k \in \mathbb{R}^{+}$, the function $\Psi(t):=\psi(k t)$ satisfies
$$\left(\Psi^{\prime}\right)^{n-1} \Psi^{\prime \prime}=e^{\Psi+a+(n+1) \log k},$$
which is the same as equation (2.42) except having a different $a$. The solutions related to the cuspidal model Kähler-Einstein metrics in our previous paper [13] are
$$\psi_{\text {cusp }}(t)=-(n+1) \log (-t), e^{a}=(n+1)^{n} .$$
Given an arbitrary $a$, the model solution is defined as
$$\psi_{\text {cusp }}(t):=-(n+1) \log (-t)+n \log (n+1)-a, \omega_{\text {cusp }}:=i \partial \bar{\partial} \psi_{\text {cusp }} .$$

Lemma 2.11. Adding a constant to $\psi_{\text {cusp }}$, i.e., choosing the constant a in (2.45) correctly, one has
$$e^{-\psi_{\text {cusp }}} \omega_{\text {cusp }}^{n}=i^{n^{2}} \Omega_{\mathcal{C}} \wedge \bar{\Omega}_{\mathcal{C}} .$$
Proof. It follows from the symmetry of $\omega_{\text {cusp }}, \Omega_{\mathcal{C}}$ and from the Kähler-Einstein condition that
$$g(t):=\frac{e^{-\psi_{\text {cusp }}} \omega_{\text {cusp }}^{n}}{i^{n^{2}} \Omega_{\mathcal{C}} \wedge \bar{\Omega}_{\mathcal{C}}}$$
is a pluriharmonic function depending only on $t$. Now
$$i \partial \bar{\partial} g(t)=g^{\prime}(t) i \partial \bar{\partial} t+i g^{\prime \prime}(t) \partial t \wedge \bar{\partial} t=0 .$$
So $g(t)$ must be a constant and (2.46) can be achieved by adding a constant to $\psi_{\text {cusp }}$. \(\square\)

To compare $\psi_{K E, 0}$ to $\psi_{\text {cusp }}$ in our main example, it is helpful to rescale the holomorphic volume forms $\Omega_{\sigma}$ by a constant so that $\Omega_{0}$ becomes asymptotic to $\Psi_{0}^{*} \Omega_{\mathcal{C}}$ at the singularity $p \in \mathcal{X}_{0}$.

Lemma 2.12. For fixed $\Omega_{0}$ and $\Omega_{\mathcal{C}}$, there is a nonzero complex constant $C$ such that
$$\left(\Psi_{0}^{-1}\right)^{*}\left(\Omega_{0} \wedge \bar{\Omega}_{0}\right)=|C|^{2} e^{-v} \Omega_{\mathcal{C}} \wedge \bar{\Omega}_{\mathcal{C}},$$
where $v$ is a pluriharmonic function satisfying for all $\varepsilon>0$ and $j \geqslant 1$ and for $t \rightarrow-\infty$ that
$$|v|=O\left(e^{\frac{t}{2}}\right),\left|\nabla_{\omega_{\text {cusp }}}^{j} v\right|_{\omega_{\text {cusp }}}=O_{\varepsilon, j}\left(e^{\frac{(1-\varepsilon) t}{2}}\right) .$$
Proof. The function $H:=\left[\left(\Psi_{0}^{-1}\right)^{*} \Omega_{0}\right] / \Omega_{\mathcal{C}}$ is a nowhere vanishing holomorphic function on $U \backslash\{0\}$ for some small open neighborhood $U$ of the singularity $0 \in T Y_{0}$. Since this is a normal isolated surface singularity in $\mathbb{C}^{3}$, the Hartogs principle [30, Thm 1.1] says that $H$ extends to a holomorphic function on $U$. We must have that $H(0) \neq 0$ because otherwise $\lim _{z \rightarrow 0} 1 / H(z)=\infty$, contradicting the Hartogs principle for $1 / H$. Let $C:=H(0)$. Then (2.49) holds with $v(z):=\log |H(0) / H(z)|^{2}$, which is obviously pluriharmonic and obviously satisfies $|v(z)|=O(|z|)=O\left(e^{t / 2}\right)$ as $|z| \rightarrow 0$ resp. $t \rightarrow-\infty$.

Now we further estimate $\left|\nabla_{\omega_{\text {cusp }}}^{j} v\right|_{\omega_{\text {cusp }}}$ for all $j \geqslant 1$. Since $v$ is in particular harmonic with respect to $\omega_{\text {cusp }}$ and since $\omega_{\text {cusp }}$ is a hyperbolic metric for $n=2$, these derivatives can be estimated using Schauder theory on the universal covers of $\omega_{\text {cusp }}$-geodesic balls of some fixed radius $r_{0} \in(0,1]$. Coordinates on
these local universal covers that make $\omega_{\text {cusp }}$ uniformly smoothly bounded can be found e.g. in [13, proof of Lemma 3.5]. The $\varepsilon$-loss in (2.50) is due to the fact that the function $t$ (which coincides with $-1 / x$ in the notation of [13]) varies by a factor of $1+O\left(r_{0}\right)$ over any $\omega_{\text {cusp }}$-ball of radius $r_{0} \ll 1$. \(\square\)

By a common rescaling of the forms $\Omega_{\sigma}$, which was our only freedom in choosing these forms, we can now arrange that $C=1$ in (2.49), i.e., that $\Omega_{0}$ is asymptotic to $\Psi_{0}^{*} \Omega_{\mathcal{C}}$ near the singularity $p \in \mathcal{X}_{0}$. According to Lemma 2.10, this leads to an additive normalization of $\psi_{K E, 0}$ such that (2.35) holds, and this equation then matches the equation (2.46) satisfied by $\psi_{\text {cusp }}$ to leading order at the singularity.

We require one additional technical lemma before stating our final result.
Lemma 2.13. Let $U$ be a neighborhood of the singularity $p=(0,0,0)$ in $T Y_{0}$. Let $\varphi$ be a function on $U \backslash\{p\}$ satisfying $i \partial \bar{\partial} \varphi=0$ and $|\varphi|=o(-\log |z|)=o(-t)$ as $|z| \rightarrow 0$ resp. $t \rightarrow-\infty$. Then $\varphi$ extends continuously as a PSH function on $U$. Moreover, $\varphi$ is the real part of a holomorphic function near the origin of $\mathbb{C}^{3}$, so, after subtracting a constant, $|\varphi|=O(|z|)=O\left(e^{t / 2}\right)$ as $|z| \rightarrow 0$ resp. $t \rightarrow-\infty$.

Proof. Consider the resolution of singularities $\pi: \hat{L} \rightarrow T Y_{0}$ from (2.7). The exceptional divisor is an elliptic curve $E$ and $\hat{L}$ is the total space of a negative holomorphic line bundle $L$ over $E$. For any point $q \in E$, there is a local holomorphic trivialization of the line bundle $\left.\hat{L}\right|_{V} \cong V \times \mathbb{C}$ for some neighborhood $V \ni q$. Let $w_{1}$ be the coordinate of $V$ and $w_{2}$ be the coordinate of $\mathbb{C}$. Then by assumption, $\varphi$ restricted to any fiber of $L$ is a smooth harmonic function on the punctured disk $\Delta^{*}$ with a sub-logarithmic pole at 0 . Hence for each fixed $w_{1}, \varphi$ can be extended continuously across 0 . So for fixed $w_{1}, \varphi$ is the real part of a holomorphic function on $\Delta$. By the mean value theorem,
$$\varphi\left(w_{1}, 0\right)=\int_{\gamma} \varphi\left(w_{1}, w_{2}\right) d w_{2}$$
where $\gamma$ is a fixed circle centered at 0. Taking $i \partial \bar{\partial}$ with respect to the variable $w_{1}$, we have that $\varphi\left(w_{1}, 0\right)$ is a harmonic function of $w_{1}$. Notice that $E$ is compact, so $\varphi\left(w_{1}, 0\right)$ is a constant. Hence $\varphi$ can be extended continuously across $\mathcal{X}_{0}^{\text {sing }}$ as a PSH function on $\mathcal{X}_{0}$.

Now we show that $\varphi$ is the real part of a holomorphic function. Note that because the line bundle $\hat{L}$ is homotopy equivalent to its zero section $E$, the de Rham cohomology $H^{1}(\hat{L}, \mathbb{R})$ is naturally isomorphic to $H^{1}(E, \mathbb{R})$. Since $i \partial \bar{\partial} \pi^{*} \varphi=0, d^{c} \pi^{*} \varphi$ is a closed real 1-form. So we have
$$d^{c} \pi^{*} \varphi=d g+a \alpha+b \beta,$$
where $a, b$ are constants, $g$ is a function on an open neighborhood of the zero section of $\hat{L}$ and $\alpha, \beta$ are closed 1 -forms on $E$ generating $H^{1}(E, \mathbb{R})$. Let $\gamma_{\alpha}, \gamma_{\beta}$ be loops in $E$ whose homology classes are Poincaré dual to $\alpha, \beta$. Note that $\varphi$ is constant on $E$ and $d g$ is exact, so the integrals of the 1 -form $d^{c} \pi^{*} \varphi-d g$ along the loops $\gamma_{\alpha}, \gamma_{\beta}$ are zero. So $a, b$ are zero. So $f:=\pi^{*} \varphi-i g$ is a holomorphic function with real part $\pi^{*} \varphi$, necessarily constant along the zero section $E$. After pushing down to the singularity, we can locally extend $f$ to a holomorphic function on an open set of $\mathbb{C}^{3}$. By subtracting a constant, we may assume that $f(p)=0$. By Taylor expansion, we deduce that $f=O(|z|)$. \(\square\)

We are now able to prove the following precise asymptotic comparison of $\psi_{K E, 0}$ and $\psi_{\text {cusp }}$. Modulo the above lemmas this is the statement of [13, Main Theorem], whose proof relies on an earlier partial result from [10, Thm 1.4]. The results of [10, 13] can be generalized to all dimensions $n \geqslant 2$ assuming that the polarized Calabi-Yau $(n-1)$-fold $\left(L^{\prime}, h^{\prime}\right) \rightarrow\left(E, \omega_{E}\right)$ in the above discussion of $\psi_{\text {cusp }}$ is flat.

Proposition 2.14. Let $\Psi_{\sigma}$ be the local holomorphic isomorphism defined in equation (2.9). Then
$$\left(\Psi_{0}^{-1}\right)^{*} \psi_{K E, 0}-\psi_{\text {cusp }}=u+v,$$
where for some constants $\mathfrak{s} \in \mathbb{R}, \delta_{0} \in \mathbb{R}^{+}$, for all $j \geqslant 0$ and for $t \rightarrow-\infty$,
$$\left|\nabla_{\omega_{\text {cusp }}}^{j}\left(u+3 \log \left(1-\frac{\mathfrak{s}}{t}\right)\right)\right|_{\omega_{\text {cusp }}}=O_{j}\left(e^{-\delta_{0} \sqrt{-t}}\right),$$
and where $v$ is a pluriharmonic function satisfying for all $\varepsilon>0$ and $j \geqslant 1$ and for $t \rightarrow-\infty$ that
$$|v|=O\left(e^{\frac{t}{2}}\right),\left|\nabla_{\omega_{\text {cusp }}}^{j} v\right|_{\omega_{\text {cusp }}}=O_{\varepsilon, j}\left(e^{\frac{(1-\varepsilon) t}{2}}\right) .$$

Remark 2.15. Composing both sides of (2.53) with the automorphism $\operatorname{scale}_{\lambda}(z)=\lambda z$ of $\mathbb{C}^{3}$ yields a new decomposition $\left(\Psi_{0}^{-1} \circ \text { scale }_{\lambda}\right)^{*} \psi_{K E, 0}-\psi_{\text {cusp }}=u_{\lambda}+v_{\lambda}$, where $u_{\lambda}, v_{\lambda}$ satisfy the same properties as before except that the constant $\mathfrak{s}$ in (2.54) gets replaced by $\mathfrak{s}-\log \lambda$. Thus, by choosing $\lambda=e^{\mathfrak{s}}$ we obtain that $u_{\lambda}$ is purely exponentially decaying and contains no powers of $1 / t$ in its expansion as $t \rightarrow-\infty$. This was already pointed out in the introduction to our previous paper [13].

This suggests making the following modification to our setup: For $\lambda=e^{\mathfrak{s}}$, replace $\Psi_{\sigma}: \mathcal{Y}_{\sigma} \rightarrow T Y_{\sigma}$ by $\operatorname{scale}_{\lambda^{-1}} \circ \Psi_{\sigma}: \mathcal{Y}_{\sigma} \rightarrow T Y_{\lambda^{-3} \sigma}$ for all $\sigma \in \Delta$. (The domains of these maps are actually just small open neighborhoods of the origin in $\mathbb{C}^{3}$ intersected with $\mathcal{Y}_{\sigma}$.) In this way, we can assume without loss of generality that $\mathfrak{s}=0$ in (2.54), i.e., that $u$ is exponentially decaying. Note that, so far, we have never actually used the map $\Psi_{\sigma}$ with $\sigma \neq 0$ except in Lemma 2.7. The statement and proof of that lemma remain unchanged if we also replace $\Phi_{\sigma}$ by $\Phi_{\lambda^{-3} \sigma}$, which again takes values in $T Y_{\lambda^{-3} \sigma}$.

However, $\Psi_{\sigma}, \Phi_{\sigma}$ will also be used as gluing maps in Section 3. The replacements $\Psi_{\sigma} \rightsquigarrow$ scale $_{\lambda^{-1} \circ} \Psi_{\sigma}$ and $\Phi_{\sigma} \rightsquigarrow \Phi_{\lambda^{-3} \sigma}$ do not worsen any of the estimates in Section 3 (or later), but being able to assume that $\mathfrak{s}=0$ in (2.54) drastically reduces the gluing error. To exploit this improvement without having to introduce even more notation, we will from now on simply assume that $\mathfrak{s}=0$ and $\lambda=1$.

Proof of Proposition 2.14. First of all, if we define
$$u:=\log \left(\frac{\left(\Psi_{0}^{-1}\right)^{*} \omega_{K E, 0}^{2}}{\omega_{c u s p}^{2}}\right),$$
then by the Kähler-Einstein equation, we have that
$$\left(\Psi_{0}^{-1}\right)^{*} \omega_{K E, 0}-\omega_{\text {cusp }}=i \partial \bar{\partial} u .$$
By [13, Main Theorem], there exist $\mathfrak{s} \in \mathbb{R}, \delta_{0} \in \mathbb{R}^{+}$such that for all $j \geqslant 0$ and for $t \rightarrow-\infty$,
$$\left|\nabla_{\omega_{\text {cusp }}}^{j}\left(u+3 \log \left(1-\frac{\mathfrak{s}}{t}\right)\right)\right|_{\omega_{\text {cusp }}}=O_{j}\left(e^{-\delta_{0} \sqrt{-t}}\right) .$$
Here we remark again that the function $-1 / t$ in this paper is the same as the function $x$ used in [13]. So at the Kähler potential level, we have that
$$\left(\Psi_{0}^{-1}\right)^{*} \psi_{K E, 0}-\psi_{\text {cusp }}=\varphi+u,$$
where $\varphi$ is a pluriharmonic function. By the estimate (2.34) of $\psi_{K E, 0}$ near the singularity and by the definition of $\psi_{\text {cusp }}$, we have $|\varphi|=O(\log (-t))=o(-t)$. Thus, by Lemma 2.13, $\varphi=\mathbf{c}+\mathbf{v}$, where $\mathbf{c}$ is a constant and v is a pluriharmonic function satisfying $|\mathbf{v}|=O(|z|)=O\left(e^{t / 2}\right)$.

It is now easy to see that the constant $\mathbf{c}$ is zero. Indeed,
$$e^{-\psi_{\text {cusp }}} \omega_{\text {cusp }}^{2}=\Omega_{\mathcal{C}} \wedge \bar{\Omega}_{\mathcal{C}}=e^{v}\left(\Psi_{0}^{-1}\right)^{*}\left(\Omega_{0} \wedge \bar{\Omega}_{0}\right)=e^{v}\left(\Psi_{0}^{-1}\right)^{*}\left(e^{-\psi_{K E, 0}} \omega_{K E, 0}^{2}\right)$$
by (2.46), by (2.49) with our chosen normalization $C=1$, and by (2.35). Therefore,
$$\mathbf{c}+u+\mathbf{v}=\left(\Psi_{0}^{-1}\right)^{*} \psi_{K E, 0}-\psi_{\text {cusp }}=\log \left(\frac{\left(\Psi_{0}^{-1}\right)^{*} \omega_{K E, 0}^{2}}{\omega_{\text {cusp }}^{2}}\right)+v=u+O\left(e^{\frac{t}{2}}\right) .$$
Since $\mathbf{v}$ goes to zero at the singularity, we get $\mathbf{c}=0$. Moreover, $\mathbf{v}=v$, so (2.50) implies (2.55). \(\square\)
2.3. Tian-Yau metrics. In this subsection we review the Tian-Yau construction [38, Thm 4.2] of a complete Ricci-flat Kähler metric on the complement of a smooth anti-canonical divisor in a smooth Fano manifold. Expositions of this construction can be found in [18, Section 3] and [19, Section 3]. We will borrow freely from these two references and show how to match their notation to ours.

As in our discussion of cusp metrics above, let $E$ be an $(n-1)$-dimensional compact Kähler manifold with trivial canonical bundle $K_{E}$ and let $L^{\prime} \rightarrow E$ be an ample line bundle, the dual of a negative line bundle $L \rightarrow E$. We fix a nowhere vanishing holomorphic ( $n-1$ )-form $\Omega_{E}$ on $E$ with
$$\int_{E} i^{(n-1)^{2}} \Omega_{E} \wedge \bar{\Omega}_{E}=\left(2 \pi c_{1}\left(L^{\prime}\right)\right)^{n-1} .$$
By Yau's resolution of the Calabi conjecture [40], there exists a unique Ricci-flat Kähler metric $\omega_{E}$ on $E$ representing the Kähler class $2 \pi c_{1}\left(L^{\prime}\right) \in H^{1,1}(E, \mathbb{R})$ and satisfying the equation
$$\omega_{E}^{n-1}=i^{(n-1)^{2}} \Omega_{E} \wedge \bar{\Omega}_{E} .$$
Up to scaling, there exists a unique Hermitian metric $h^{\prime}$ on $L^{\prime}$ whose curvature form is $\omega_{E}$, and $h^{\prime}$ is the dual of a negatively curved Hermitian metric $h$ on $L$. We now fix a choice of $h^{\prime}$. Then the Calabi model space is the subset $\mathcal{C}$ of the total space of $L^{\prime}$ consisting of all elements $\xi$ with $0<|\xi|_{h^{\prime}}<1$, endowed with a nowhere vanishing holomorphic volume form $\Omega_{\mathcal{C}}$ and a Ricci-flat Kähler metric $\omega_{\mathcal{C}}$ which is incomplete as $|\xi|_{h^{\prime}} \rightarrow 1$ and complete as $|\xi|_{h^{\prime}} \rightarrow 0$. Again as in our discussion of cusp metrics above, the holomorphic volume form $\Omega_{\mathcal{C}}$ is uniquely determined by the equation
$$Z\lrcorner \Omega_{\mathcal{C}}=p^{*} \Omega_{E},$$
where $p: \mathcal{C} \rightarrow E$ is the bundle projection and $Z$ is the holomorphic vector field generating the natural $\mathbb{C}^{*}$-action on the fibers of $p$ (i.e., the one coming from the line bundle structure of $L^{\prime}$ ). The metric $\omega_{\mathcal{C}}$ is given by the Calabi ansatz
$$\omega_{\mathcal{C}}:=i \partial \bar{\partial} \psi_{\mathcal{C}}, \quad \psi_{\mathcal{C}}:=\frac{n}{n+1}\left(-\log |\xi|_{h^{\prime}}^{2}\right)^{\frac{n+1}{n}},$$
and satisfies the Monge-Ampère equation
$$\omega_{\mathcal{C}}^{n}=i^{n^{2}} \Omega_{\mathcal{C}} \wedge \bar{\Omega}_{\mathcal{C}},$$
hence is Ricci-flat. Also define the momentum coordinate
$$\mathbf{z}:=\left(-\log |\xi|_{h^{\prime}}^{2}\right)^{\frac{1}{n}} .$$
Then the $\omega_{\mathcal{C}}$-distance to a fixed point in $\mathcal{C}$ is uniformly comparable to $\mathbf{z}^{(n+1) / 2}$ for $z \gg 1$.
We now explain the Tian-Yau construction [38] of complete Ricci-flat Kähler metrics asymptotic to a Calabi ansatz at infinity. Let $M$ be a smooth Fano manifold of complex dimension $n$, let $E \in\left|K_{M}^{-1}\right|$ be a smooth divisor, and let $L^{\prime}$ denote the holomorphic normal bundle to $E$ in $M$. Then $E$ has a trivial canonical bundle and $L^{\prime}$ is ample, so in particular we can choose a holomorphic volume form $\Omega_{E}$ on $E$ which satisfies (2.62). We fix a defining section $S$ of $E$, so that $S^{-1}$ can be viewed as a holomorphic $n$-form $\Omega_{X}$ on $X=M \backslash E$ with a simple pole along $E$. After scaling $S$ by a nonzero complex constant, we may assume that $\Omega_{E}$ is the residue of $\Omega_{X}$ along $E$. (In practice this means that $\Omega_{X}$ is asymptotic to $\Omega_{\mathcal{C}}$ with respect to a suitable diffeomorphism $\Phi$ between tubular neighborhoods of $E$ in $M$ and of the zero section in $L^{\prime}$.) Lastly, we fix a Hermitian metric $h_{M}$ on $K_{M}^{-1}$ whose curvature form is strictly positive on $M$ and restricts to the unique Ricci-flat Kähler form $\omega_{E} \in 2 \pi c_{1}\left(L^{\prime}\right)$ on $E$. Then
$$\omega_{X}^{\circ}:=\frac{n}{n+1} i \partial \bar{\partial}\left(-\log |S|_{h_{M}}^{2}\right)^{\frac{n+1}{n}}$$
defines a Kähler form on a neighborhood of infinity in $X$. This $\omega_{X}^{\circ}$ is then complete towards $E$ and is asymptotic to $\omega_{\mathcal{C}}$, where the Hermitian metric $h^{\prime}$ used in (2.65) is the restriction of $h_{M}$ to $\left.K_{M}^{-1}\right|_{E}=L^{\prime}$.

In particular, $\omega_{X}^{\circ}$ is asymptotically Ricci-flat. Moreover, since $X$ is an affine variety, it is reasonably straightforward to extend $\omega_{X}^{\circ}$ as a globally defined $i \partial \bar{\partial}$-exact Kähler form on the whole manifold $X$. Then the following is proved in [38] by solving a Monge-Ampère equation with reference metric $\omega_{X}^{\circ}$. The exponential decay statement follows from [16, Prop 2.9].

Theorem 2.16. There is a complete Ricci-flat Kähler metric $\omega_{X}$ on $X$ solving the equation
$$\omega_{X}^{n}=i^{n^{2}} \Omega_{X} \wedge \bar{\Omega}_{X} .$$
Moreover, there is a unique choice of the scaling factor of $h^{\prime}$ resp. of $h_{M}$ such that $\omega_{X}=\omega_{X}^{\circ}+i \partial \bar{\partial} \phi$, where for some $\delta_{0}>0$ and for all $k \geqslant 0$, as $z \rightarrow \infty$,
$$\left|\nabla_{\omega_{\mathcal{C}}}^{k}(\phi \circ \Phi)\right|_{\omega_{\mathcal{C}}}=O_{k}\left(e^{-\delta_{0} \mathbf{z}^{n / 2}}\right) .$$
Here we have implicitly fixed a smooth identification $\Phi$ of $M$ and of the total space of $L^{\prime}$ near $E$.
We will now apply this construction to our space $X:=T Y_{1}=\left\{z_{1}^{3}+z_{2}^{3}+z_{3}^{3}=1\right\}$, a smooth cubic in $\mathbb{C}^{3}$. We can compactify $X$ to $M$, a smooth cubic in $\mathbb{C P}^{3}$, by adding an elliptic curve $E$ at infinity. Note that $M$ is an anticanonically embedded del Pezzo surface and $L^{\prime}=-\left.K_{M}^{-1}\right|_{E}=\left.\mathcal{O}_{\mathbb{C P}^{3}}(1)\right|_{E}$. The total space of the dual bundle $L$ resolves the singularity of the cubic cone $T Y_{0}$ at the origin, and $\mathcal{C}$ is identified with a neighborhood of infinity in $T Y_{0}$. Then our diffeomorphism $\Phi=\Phi_{1}$ from (2.16), (2.17) plays the role of the smooth identification $\Phi$ in Theorem 2.16, and $\mathbf{z}^{2}=t$ for $t>0$.

The following lemma records some more detailed estimates from [18, Prop 3.4] in our setting.
Lemma 2.17. For all $\varepsilon>0$ and $k \geqslant 0$ and for $t \rightarrow+\infty$,
$$\left|\nabla_{g_{\mathcal{C}}}^{k}\left(\Phi_{1}^{*} J_{T Y_{1}}-J_{\mathcal{C}}\right)\right|_{g_{\mathcal{C}}}+\left|\nabla_{g_{\mathcal{C}}}^{k}\left(\Phi_{1}^{*} \Omega_{T Y_{1}}-\Omega_{\mathcal{C}}\right)\right|_{g_{\mathcal{C}}}=O_{\varepsilon, k}\left(e^{-\left(\frac{1}{2}-\varepsilon\right) t}\right) .$$
Moreover, there exists a global potential $\psi_{T Y_{1}}$ of $\omega_{T Y_{1}}$, i.e., $\omega_{T Y_{1}}=i \partial \bar{\partial} \psi_{T Y_{1}}$ globally on $T Y_{1}$, such that there exists $\delta_{0}>0$ such that for all $k \geqslant 0$ and for $t \rightarrow+\infty$,
$$\left|\nabla_{g_{\mathcal{C}}}^{k}\left(\Phi_{1}^{*} \psi_{T Y_{1}}-\psi_{\mathcal{C}}\right)\right|_{g_{\mathcal{C}}}+\left|\nabla_{g_{\mathcal{C}}}^{k}\left(\Phi_{1}^{*} \omega_{T Y_{1}}-\omega_{\mathcal{C}}\right)\right|_{g_{\mathcal{C}}}=O_{k}\left(e^{-\delta_{0} \sqrt{t}}\right) .$$

In our gluing construction, we will be working with a scaled copy of $\omega_{T Y_{1}}$, pulled back from $T Y_{1}$ to $T Y_{\sigma}$ via the maps of Definition 2.4. Let us first recall these maps for convenience:
$$\begin{array}{r}
\Phi: T Y_{0} \backslash \bar{B}_{R} \rightarrow T Y_{1}, \Phi(z)=z+O\left(|z|^{-2}\right) \text { as }|z| \rightarrow \infty, \\
m_{\sigma}^{\prime}: T Y_{0} \rightarrow T Y_{0}, m_{\sigma}^{\prime}(z)=\sigma^{-1 / 3} z, \\
m_{\sigma}: T Y_{\sigma} \rightarrow T Y_{1}, m_{\sigma}(z)=\sigma^{-1 / 3} z, \\
\Phi_{\sigma}: T Y_{0} \backslash \bar{B}_{|\sigma|^{1 / 3} R} \rightarrow T Y_{\sigma}, \Phi_{\sigma}=m_{\sigma}^{-1} \circ \Phi \circ m_{\sigma}^{\prime} .
\end{array}$$
Next, we introduce the following pullback objects:
$$\Omega_{T Y_{\sigma}}:=m_{\sigma}^{*} \Omega_{T Y_{1}}, \omega_{T Y_{\sigma}}:=m_{\sigma}^{*} \omega_{T Y_{1}}, \psi_{T Y_{\sigma}}:=m_{\sigma}^{*} \psi_{T Y_{1}} \text { and } g_{\mathcal{C}, \sigma}:=\left(m_{\sigma}^{\prime}\right)^{*} g_{\mathcal{C}} .$$
Then Lemma 2.17 implies the following estimates, including an additional rescaling. The strange form of the scaling factor, $|b|^{1 / 2}$ with $b<0$, is due to some conventions in Section 2.4.

Lemma 2.18. For all $b<0$ and $\sigma \in \Delta^{*}$ the following estimates hold with all of the implied constants independent of $b$ and $\sigma$. First, for all $\varepsilon>0$ and $k \geqslant 0$ and for $t-\frac{2}{3} \log |\sigma| \rightarrow+\infty$,
$$\begin{aligned}
\left|\nabla_{|b|^{\frac{1}{2}} g_{\mathcal{C}, \sigma}}^{k}\left(\Phi_{\sigma}^{*} J_{T Y_{\sigma}}-J_{\mathcal{C}}\right)\right|_{|b|^{\frac{1}{2}} g_{\mathcal{C}, \sigma}} & =O_{\varepsilon, k}\left(|b|^{-\frac{k}{4}} e^{-\left(\frac{1}{2}-\varepsilon\right)\left(t-\frac{2}{3} \log |\sigma|\right)}\right), \\
\left|\nabla_{|b|^{\frac{1}{2}} g_{\mathcal{C}, \sigma}}^{k}\left(\Phi_{\sigma}^{*} \Omega_{T Y_{\sigma}}-\Omega_{\mathcal{C}}\right)\right|_{|b|^{\frac{1}{2}} g_{\mathcal{C}, \sigma}} & =O_{\varepsilon, k}\left(|b|^{-\frac{k}{4}} e^{-\left(\frac{1}{2}-\varepsilon\right)\left(t-\frac{2}{3} \log |\sigma|\right)}\right) .
\end{aligned}$$

Moreover, there exists $\delta_{0}>0$ such that for all $k \geqslant 0$ and for $t-\frac{2}{3} \log |\sigma| \rightarrow+\infty$,
$$\begin{aligned}
\left\lvert\, \nabla_{|b|^{\frac{1}{2}} g_{\mathcal{C}, \sigma}}^{k}\right. & \left.\left(|b|^{\frac{1}{2}} \Phi_{\sigma}^{*} \psi_{T Y_{\sigma}}-|b|^{\frac{1}{2}} \psi_{\mathcal{C}, \sigma}\right)\right|_{|b|^{\frac{1}{2}} g_{\mathcal{C}, \sigma}}=O_{k}\left(|b|^{\frac{2-k}{4}} e^{-\delta_{0}\left(t-\frac{2}{3} \log |\sigma|\right)^{1 / 2}}\right), \\
\left|\nabla_{|b|^{\frac{1}{2}} g_{\mathcal{C}, \sigma}}^{k}\left(|b|^{\frac{1}{2}} \Phi_{\sigma}^{*} \omega_{T Y_{\sigma}}-|b|^{\frac{1}{2}} \omega_{\mathcal{C}, \sigma}\right)\right|_{|b|^{\frac{1}{2}} g_{\mathcal{C}, \sigma}} & =O_{k}\left(|b|^{-\frac{k}{4}} e^{-\delta_{0}\left(t-\frac{2}{3} \log |\sigma|\right)^{1 / 2}}\right) .
\end{aligned}$$
Proof. This is trivial except for the following two observations. First, $t-\frac{2}{3} \log |\sigma|=\left(m_{\sigma}^{\prime}\right)^{*} t$. Second, $J_{\mathcal{C}, \sigma}:=\left(m_{\sigma}^{\prime}\right)^{*} J_{\mathcal{C}}$ and $\Omega_{\mathcal{C}, \sigma}:=\left(m_{\sigma}^{\prime}\right)^{*} \Omega_{\mathcal{C}}$ are actually equal to $J_{\mathcal{C}}$ resp. $\Omega_{\mathcal{C}}$. \(\square\)

Lastly, we need to compare the holomorphic volume form $\Omega_{T Y_{\sigma}}$ on $T Y_{\sigma}$ to the holomorphic volume form $\Omega_{\sigma}$ on $\mathcal{Y}_{\sigma} \subset \mathcal{X}_{\sigma}$ on a uniform neighborhood of the origin in $\mathbb{C}^{3}$.

Lemma 2.19. Recall the local biholomorphism $\Psi_{\sigma}: \mathcal{Y}_{\sigma} \rightarrow T Y_{\sigma}$ from (2.9). Then for all $\sigma \in \Delta^{*}$,
$$\left(\Psi_{\sigma}^{-1}\right)^{*} \Omega_{\sigma}=(1+O(|z|)) \Omega_{T Y_{\sigma}}$$
as $|z| \rightarrow 0$, and the implied constant is independent of $\sigma$.
Proof. There exists an $\varepsilon>0$ such that for every fixed $\sigma \in \Delta^{*}$, the function $H_{\sigma}:=\left[\left(\Psi_{\sigma}^{-1}\right)^{*} \Omega_{\sigma}\right] / \Omega_{T Y_{\sigma}}$ is holomorphic on $T Y_{\sigma} \cap B_{\varepsilon}(0)$. Since all data depend holomorphically on $\sigma$, it follows that
$$H: B_{\varepsilon}(0) \backslash T Y_{0} \rightarrow \mathbb{C}, \quad z \mapsto H_{\sigma}(z) \text { with } \sigma=z_{1}^{3}+z_{2}^{3}+z_{3}^{3} \neq 0,$$
is holomorphic.
Claim 2.20. $H$ extends holomorphically to $B_{\varepsilon}(0)$.
Proof of Claim 2.20. It is enough to show that $H$ extends holomorphically to $B_{\varepsilon}(0) \backslash\{0\}$ because then the claim follows from Hartogs' theorem. Obviously the numerator, $\left(\Psi_{\sigma}^{-1}\right)^{*} \Omega_{\sigma}$, is holomorphic even at the points of $T Y_{0} \backslash\{0\}$. For the denominator, $\Omega_{T Y_{\sigma}}$, cover $\mathbb{C}^{3} \backslash\{0\}$ by the open sets $\left\{z_{i} \neq 0\right\}(i=1,2,3)$. By symmetry we only need to consider the case $i=1$. By adjunction, there exists $\gamma \in \mathbb{C}^{*}$ such that $\Omega_{T Y_{1}}$ is the restriction to the tangent bundle of $T Y_{1}$ of the 2-form $\gamma\left(d z_{2} \wedge d z_{3}\right) / z_{1}^{2}$ on $\left\{z_{1} \neq 0\right\}$. The latter is invariant under $m_{\sigma}$. Thus, $\Omega_{T Y_{\sigma}}$ is given by the same formula, so it extends as a holomorphic and nowhere vanishing section of the relative canonical bundle across $T Y_{0} \backslash\{0\}$. \(\square\)
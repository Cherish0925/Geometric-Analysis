---
retention_scope: session
part: 1
total_parts: 1
---

---
source_file: 1809_04449.pdf
converter: mathpix
format: mmd
---

\title{
RC-positivity and rigidity of harmonic maps into Riemannian manifolds
}

\author{
Jun Wang and Xiaokui Yang \\ Dedicated to Professor Lo Yang on the occasion of his 80th birthday
}

\begin{abstract}
In this paper, we show that every harmonic map from a compact Kähler manifold with uniformly RC-positive curvature to a Riemannian manifold with non-positive complex sectional curvature is constant. In particular, there is no non-constant harmonic map from a compact Kähler manifold with positive holomorphic sectional curvature to a Riemannian manifold with non-positive complex sectional curvature.
\end{abstract}

Contents
1. Introduction ..... 1
2. Harmonic maps from Hermitian manifolds to Riemannian manifolds ..... 5
3. Rigidity of pluri-harmonic maps into Riemannian manifolds ..... 8
4. Rigidity of Hermitian harmonic maps into Riemannian manifolds ..... 10
References ..... 12

\section*{1. Introduction}

The classical result of Eells-Sampson [ES64] asserts that harmonic maps from compact Riemannian manifolds with positive Ricci curvature to Riemannian manifolds with non-positive sectional curvature must be constant. By using Schwarz calculation and maximum principle, S.-T. Yau established in [Yau78] that holomorphic maps from compact Kähler manifolds with positive Ricci curvature to Hermitian manifolds with non-positive holomorphic bisectional curvature must be constant. Recently, the second author extended Yau's result and obtained in [Yang18a] that holomorphic maps from compact Hermitian manifolds with positive holomorphic sectional curvature to Hermitian manifolds with non-positive holomorphic bisectional curvature must be constant, and one of the key ingredients in the proof is a notion called "RC-positivity" introduced in [Yang18]. Moreover, Y.-T. Siu achieved in [Siu80] the complex analyticity of harmonic maps into compact Kähler manifolds with strongly negative curvature. Later, Jost-Yau explored in [JY91, JY93] rigidity theorems for various harmonic maps from Hermitian manifolds into Riemannian manifolds with

\footnotetext{
This work was partially supported by China's Recruitment Program of Global Experts.
}
non-positive complex sectional curvature (see also [Sam85, Sam86]). There are many generalizations along this line, and we refer to [EL78, Siu82, EL83, Ohn87, EL88, Uda88, OU90, YZ91, MSY93, Uda94, Ni99, Tos07, Zhang12, YHD13, Dong13, LY14, YZ18, Yang18a, Yang18b, Ni18] and the references therein.

In this paper, we aim to extend the above rigidity results to harmonic maps (and pluri-harmonic maps) from compact complex manifolds to Riemannian manifolds by using RC-positivity and ideas in [ES64, Yau78, Siu80, Sam85, Sam86, JY91, JY93, LY14, Yang18, Yang18a, Yang18b]. More precisely, we consider harmonic maps (resp. pluri-harmonic maps) from a compact complex manifold $M$ with uniformly RC-positive curvature to a Riemannian manifold $N$ with non-positive complex sectional curvature. Let's recall these curvature notions. In [Yang18b], the second author introduced the following definition.

Definition 1.1. A Hermitian holomorphic vector bundle $(\mathscr{E}, h)$ over a complex manifold $M$ is called uniformly $R C$-positive if at every point $q \in M$, there exists some vector $u \in T_{q}^{1,0} M$ such that for any nonzero vector $v \in \mathscr{E}_{q}$, one has
$$R^{\mathscr{E}}(u, \bar{u}, v, \bar{v})>0 .$$
There are many complex manifolds which have uniformly RC-positive tangent bundles (i.e., the tangent bundle admits a Hermitian metric such that its Chern curvature is uniformly RC-positive). For instances,
\begin{itemize}
\item[(1)] Kähler manifolds with positive holomorphic sectional curvature ([Yang18b, Theorem 5.1]);
\item[(2)] Hopf manifolds $\mathbb{S}^{1} \times \mathbb{S}^{2 n+1}$ with standard metrics ([LY14, formula (6.4)]);
\item[(3)] products of complex manifolds with uniformly RC-positive tangent bundles.
\end{itemize}
For more details, we refer to [Yang18, Yang18a, Yang18b] and the references therein.
As analogous to Siu's strong negativity [Siu80], Sampson proposed in [Sam85] the following definition (see also [JY91, Definition 4.2]):

Definition 1.2. Let $(N, g)$ be a Riemannian manifold. The (complexified) curvature tensor $R$ of $(N, g)$ is said to have non-positive complex sectional curvature if
$$R(Z, \bar{W}, W, \bar{Z}) \leq 0$$
for any $Z, W \in T_{\mathbb{C}} N$.
If $(N, g)$ has non-positive complex sectional curvature, then it has non-positive Riemannian sectional curvature. Moreover, a Kähler manifold $(N, g)$ has strongly nonpositive curvature in the sense of Siu if and only if its background Riemannian metric has non-positive complex sectional curvature (e.g. [LSYY17, Theorem 4.4]). Hence, compact quotients of bounded symmetric domains of type $\mathrm{I}_{m n}(m n \geq 2), \mathrm{II}_{n}(n \geq 3)$, III $_{n}(n \geq 2)$, and $\operatorname{IV}_{n}(n \geq 3)$ all have non-positive complex sectional curvature.

The first main result of this paper is the following.
Theorem 1.3. Let $(M, h)$ be a compact Kähler manifold with uniformly RC-positive curvature and $(N, g)$ be a Riemannian manifold with non-positive complex sectional curvature. Then there is no non-constant harmonic map from $(M, h)$ to $(N, g)$.

By Theorem 1.3 and [Yang18b, Theorem 5.1], we obtain
Corollary 1.4. There is no non-constant harmonic map from a compact Kähler manifold with positive holomorphic sectional curvature to a Riemannian manifold with non-positive complex sectional curvature.

Remark 1.5. We proved in [Yang18b, Corollary 1.3] that for a compact Kähler manifold $M$, if it admits a Hermitian metric with uniformly RC-positive curvature, then $M$ is projective and rationally connected. By using algebraic geometry, we can prove a more general result that: every harmonic map from a rationally connected manifold to a Riemannian manifold with non-positive complex sectional curvature is constant. It is well-known that Fano manifolds are all rationally connected ([Cam92, KMM92]). Hence, Theorem 1.3 and Corollary 1.4 are generalizations of the following well-known result: every harmonic map from a Fano manifold (i.e. a compact Kähler manifold with positive Ricci curvature [Yau78a]) to a Riemannian manifold with non-positive (complex) sectional curvature is constant.

In the following, we give the proof of Theorem 1.3 in a more general setting. Let $f:(M, h) \rightarrow(N, g)$ be a smooth map from a compact Hermitian manifold $(M, h)$ to a Riemannian manifold $(N, g)$. Jost and Yau proposed in [JY93, (H2)] the following concept: $f$ is called a Hermitian harmonic map if it satisfies
$$h^{\alpha \bar{\beta}}\left(\frac{\partial^{2} f^{i}}{\partial z^{\alpha} \partial \bar{z}^{\beta}}+\Gamma_{j k}^{i} \frac{\partial f^{j}}{\partial \bar{z}^{\beta}} \frac{\partial f^{k}}{\partial z^{\alpha}}\right) \otimes e_{i}=0 .$$
It is easy to see that when $M$ is Kähler, Hermitian harmonic maps are usual harmonic maps. On the other hand, Jost-Yau proved in [JY93] that there always exist Hermitian harmonic maps into Riemannian manifolds with non-positive sectional curvature, which generalizes the classical result of Eells-Sampson [ES64]. Moreover, $f$ is called pluri-harmonic if
$$\left(\frac{\partial^{2} f^{i}}{\partial z^{\alpha} \partial \bar{z}^{\beta}}+\Gamma_{j k}^{i} \frac{\partial f^{j}}{\partial \bar{z}^{\beta}} \frac{\partial f^{k}}{\partial z^{\alpha}}\right) d z^{\alpha} \wedge d \bar{z}^{\beta} \otimes e_{i}=0 .$$
Pluri-harmonic maps are generalizations of holomorphic maps. Indeed, a holomorphic map from a complex manifold $M$ to a Kähler manifold $(N, g)$ is pluri-harmonic. The second main result is on rigidity of pluri-harmonic maps, which is analogous to rigidity of holomorphic maps obtained in [Yang18a, Yang18b].

Theorem 1.6. Let $f: M \rightarrow(N, g)$ be a pluri-harmonic map from a compact complex manifold $M$ to a Riemannian manifold $(N, g)$ with non-positive complex sectional curvature. If $T^{1,0} M$ is uniformly $R C$-positive, then $f$ is a constant map.

The key ingredient in the proof of Theorem 1.6 is the following Chern-Lu type identity for pluri-harmonic maps.

Proposition 1.7. Let $f:(M, h) \rightarrow(N, g)$ be a pluri-harmonic map from a Hermitian manifold $(M, h)$ to a Riemannian manifold $(N, g)$. Then we have the identity
$$\partial \bar{\partial} u=\left\langle\partial_{\mathscr{F}} \partial f, \partial_{\mathscr{F}} \partial f\right\rangle+\left(R_{\alpha \bar{\beta}}^{M} \bar{\delta} h^{\gamma \bar{\nu}} h^{\mu \bar{\delta}} g_{i j} f_{\mu}^{i} f_{\bar{\nu}}^{j}-R_{i \ell k j}^{N} f_{\alpha}^{i} f_{\bar{\beta}}^{j}\left(h^{\gamma \bar{\delta}} f_{\gamma}^{k} f_{\bar{\delta}}^{\ell}\right)\right) d z^{\alpha} \wedge d \bar{z}^{\beta},$$
where $u=|\partial f|^{2}, R_{\alpha \bar{\beta} \gamma \bar{\delta}}^{M}$ is the curvature of the Chern connection on $T^{1,0} M$ and $\partial_{\mathscr{F}}$ is the induced $(1,0)$ connection on the vector bundle $\mathscr{F}=T^{* 1,0} M \otimes f^{*} T_{N}$.

By using Theorem 1.6 and ideas in [Siu80, Sam85, Sam86, YZ91, JY91, JY93, LY14], we obtain the following result. Note that, Theorem 1.3 is a special case of it.

Theorem 1.8. Let $(M, h)$ be a compact astheno-Kähler manifold (i.e. $\partial \bar{\partial} \omega_{h}^{m-2}=0$ ) and $(N, g)$ be a Riemannian manifold with non-positive complex sectional curvature. Let $f:(M, h) \rightarrow(N, g)$ be a Hermitian harmonic map. If $M$ admits a Hermitian metric $h_{0}$ with uniformly $R C$-positive curvature, then $f$ is a constant map.

There are many astheno-Kähler manifolds which are non-Kähler. For instances, non-Kähler complex surfaces and Calabi-Eckmann manifolds $\mathbb{S}^{2 p+1} \times \mathbb{S}^{2 q+1}$ ([Mat09]).

As motivated by Theorem 1.3, we propose:
Question 1.9. Does there exist a non-constant Hermitian harmonic map (resp. harmonic map) from a compact Hermitian manifold with (uniformly) RC-positive curvature to a Riemannian manifold with non-positive (complex) sectional curvature?

As a special case of Theorem 1.8, one gets
Corollary 1.10. Let $M$ be a compact complex surface and $(N, g)$ be a Riemannian manifold with non-positive complex sectional curvature. Let $f:(M, h) \rightarrow(N, g)$ be a Hermitian harmonic map. If $M$ admits a Hermitian metric $h_{0}$ with uniformly $R C$-positive curvature, then $f$ is a constant map.

As we pointed out before, the standard Hopf surface $\mathbb{S}^{1} \times \mathbb{S}^{3}$ admits uniformly RC-positive metrics, and so we get

Corollary 1.11. There is no non-constant Hermitian harmonic map from Hopf surface $\mathbb{S}^{1} \times \mathbb{S}^{3}$ (with an arbitrary Hermitian metric) to Riemannian manifolds with non-positive complex sectional curvature.

Acknowledgements. The first author would like to thank his advisor Professor Jian Zhou for his guidance. The second author is very grateful to Professor K.-F. Liu and Professor S.-T. Yau for their support, encouragement and stimulating discussions over years. We would also like to thank Y.-X. Li and V. Tosatti for some helpful discussions.
2. Harmonic maps from Hermitian manifolds to Riemannian manifolds
2.1. Connections on vector bundles. Let $\mathscr{E}$ be a Hermitian complex vector bundle or a Riemannian real vector bundle over a compact Hermitian manifold $(M, h)$ and $\nabla^{\mathscr{E}}$ be a metric connection on $\mathscr{E}$. There is a natural decomposition $\nabla^{\mathscr{E}}=\nabla^{\prime \mathscr{E}}+\nabla^{\prime \prime \mathscr{E}}$ where
$$\nabla^{\prime \mathscr{E}}: \Gamma(M, \mathscr{E}) \rightarrow \Omega^{1,0}(M, \mathscr{E}) \quad \text { and } \quad \nabla^{\prime \prime \mathscr{E}}: \Gamma(M, \mathscr{E}) \rightarrow \Omega^{0,1}(M, \mathscr{E}) .$$
Moreover, $\nabla^{\prime \mathscr{E}}$ and $\nabla^{\prime \prime} \mathscr{E}$ induce two differential operators. The first one is $\partial_{\mathscr{E}}$ : $\Omega^{p, q}(M, \mathscr{E}) \rightarrow \Omega^{p+1, q}(M, \mathscr{E})$ which is defined by
$$\partial_{\mathscr{E}}(\varphi \otimes s)=(\partial \varphi) \otimes s+(-1)^{p+q} \varphi \wedge \nabla^{\prime \mathscr{E}} s$$
for any $\varphi \in \Omega^{p, q}(M)$ and $s \in \Gamma(M, \mathscr{E})$. The operator $\bar{\partial}_{\mathscr{E}}: \Omega^{p, q}(M, \mathscr{E}) \rightarrow \Omega^{p, q+1}(M, \mathscr{E})$ is defined similarly. The operator $\partial_{\mathscr{E}} \bar{\partial}_{\mathscr{E}}+\bar{\partial}_{\mathscr{E}} \partial_{\mathscr{E}}$ is represented by the curvature tensor $R^{\mathscr{E}} \in \Gamma\left(M, \Lambda^{1,1} T^{*} M \otimes \mathscr{E}^{*} \otimes \mathscr{E}\right)$. The adjoint operators of $\partial, \bar{\partial}, \partial_{\mathscr{E}}$ and $\bar{\partial}_{\mathscr{E}}$ are denoted by $\partial^{*}, \bar{\partial}^{*}, \partial_{\mathscr{E}}^{*}$ and $\bar{\partial}_{\mathscr{E}}^{*}$ respectively.
2.2. Harmonic maps between Riemannian manifolds. Let $(M, h)$ and $(N, g)$ be two compact Riemannian manifolds. Let $f:(M, h) \rightarrow(N, g)$ be a smooth map. If $\mathscr{E}=f^{*}(T N)$, then $d f$ can be regarded as an $\mathscr{E}$-valued one form. There is an induced connection $\nabla^{\mathscr{E}}$ on $\mathscr{E}$ by the Levi-Civita connection on $T N$. In the local coordinates $\left\{x^{\alpha}\right\}_{\alpha=1}^{m},\left\{y^{i}\right\}_{i=1}^{n}$ on $M$ and $N$ respectively, the local frames of $\mathscr{E}$ are denoted by $e_{i}=f^{*}\left(\frac{\partial}{\partial y^{i}}\right)$ and
$$\nabla^{\mathscr{E}} e_{i}=f^{*}\left(\nabla \frac{\partial}{\partial y^{i}}\right)=\Gamma_{i j}^{k}(f) \frac{\partial f^{j}}{\partial x^{\alpha}} d x^{\alpha} \otimes e_{k} .$$
We also denote by $\nabla^{\mathscr{E}}$ the extension $\nabla^{\mathscr{E}}: \Omega^{p}(M, \mathscr{E}) \rightarrow \Omega^{p+1}(M, \mathscr{E})$. As a classical result, the Euler-Lagrange equation of the energy
$$E(f)=\int_{M}|d f|^{2} d v_{M}$$
is $\left(\nabla^{\mathscr{E}}\right)^{*} d f=0$, i.e.
$$h^{\alpha \beta}\left(\frac{\partial^{2} f^{i}}{\partial x^{\alpha} \partial x^{\beta}}-\Gamma_{\alpha \beta}^{\gamma} \frac{\partial f^{i}}{\partial x^{\gamma}}+\Gamma_{j k}^{i} \frac{\partial f^{j}}{\partial x^{\alpha}} \frac{\partial f^{k}}{\partial x^{\beta}}\right) \otimes e_{i}=0 .$$
A smooth map $f:(M, h) \rightarrow(N, g)$ is called a harmonic map if it satisfies (2.5).
2.3. Harmonic maps from Hermitian manifolds to Riemannian manifolds. Let $(M, h)$ be a compact Hermitian manifold, $(N, g)$ a Riemannian manifold and $\mathscr{E}=f^{*}(T N)$ with the induced Levi-Civita connection. Let $\left\{z^{\alpha}\right\}_{\alpha=1}^{m}$ be the local holomorphic coordinates on $M$ where $m=\operatorname{dim}_{\mathbb{C}} M$. There are three $\mathscr{E}$-valued 1-forms, namely,
$$\bar{\partial} f=\frac{\partial f^{i}}{\partial \bar{z}^{\beta}} d \bar{z}^{\beta} \otimes e_{i}, \quad \partial f=\frac{\partial f^{i}}{\partial z^{\alpha}} d z^{\alpha} \otimes e_{i}, \quad d f=\bar{\partial} f+\partial f$$

The $\bar{\partial}$-energy of a smooth map $f:(M, h) \rightarrow(N, g)$ is defined by
$$E^{\prime \prime}(f)=\int_{M}|\bar{\partial} f|^{2} \frac{\omega_{h}^{m}}{m!}$$
and similarly we can define the $\partial$-energy $E^{\prime}(f)$ and the total energy $E(f)$ by
$$E^{\prime}(f)=\int_{M}|\partial f|^{2} \frac{\omega_{h}^{m}}{m!}, \quad E(f)=\int_{M}|d f|^{2} \frac{\omega_{h}^{m}}{m!} .$$
Since $N$ is a Riemannian manifold, it is obvious that
$$E(f)=2 E^{\prime}(f)=2 E^{\prime \prime}(f) .$$
Let $f:(M, h) \rightarrow(N, g)$ be a smooth map and $\mathscr{E}=f^{*}(T N)$. The smooth map $f$ is harmonic if it is a critical point of the Euler-Lagrange equation of the energy $E(f)$, i.e. $\left(\nabla^{\mathscr{E}}\right)^{*} d f=0$, which is also equivalent to $\bar{\partial}_{\mathscr{E}}^{*} \bar{\partial} f=\partial_{\mathscr{E}}^{*} \partial f=0$. Hence, the harmonic map equation (2.5) can be written into the following complex version
$$h^{\alpha \bar{\beta}}\left(\frac{\partial^{2} f^{i}}{\partial z^{\alpha} \partial \bar{z}^{\beta}}-2 \Gamma_{\alpha \bar{\beta}}^{\bar{\gamma}} \frac{\partial f^{i}}{\partial \bar{z}^{\gamma}}+\Gamma_{j k}^{i} \frac{\partial f^{j}}{\partial \bar{z}^{\beta}} \frac{\partial f^{k}}{\partial z^{\alpha}}\right) \otimes e_{i}=0$$
or equivalently
$$h^{\alpha \bar{\beta}}\left(\frac{\partial^{2} f^{i}}{\partial z^{\alpha} \partial \bar{z}^{\beta}}-2 \Gamma_{\bar{\beta} \alpha}^{\gamma} \frac{\partial f^{i}}{\partial z^{\gamma}}+\Gamma_{j k}^{i} \frac{\partial f^{j}}{\partial \bar{z}^{\beta}} \frac{\partial f^{k}}{\partial z^{\alpha}}\right) \otimes e_{i}=0$$
where
$$\Gamma_{\alpha \bar{\beta}}^{\gamma}=\frac{1}{2} h^{\gamma \bar{\delta}}\left(\frac{\partial h_{\alpha \bar{\delta}}}{\partial \bar{z}^{\beta}}-\frac{\partial h_{\alpha \bar{\beta}}}{\partial \bar{z}^{\delta}}\right)=\Gamma_{\bar{\beta} \alpha}^{\gamma}=\overline{\Gamma_{\beta \bar{\alpha}}^{\bar{\gamma}}}, \quad \Gamma_{\alpha \beta}^{\gamma}=\frac{1}{2} h^{\gamma \bar{\delta}}\left(\frac{\partial h_{\alpha \bar{\delta}}}{\partial z^{\beta}}+\frac{\partial h_{\beta \bar{\delta}}}{\partial z^{\alpha}}\right) .$$

Definition 2.1. $f$ is called pluri-harmonic if it satisfies $\partial_{\mathscr{E}} \bar{\partial} f=0$, i.e.
$$\left(\frac{\partial^{2} f^{i}}{\partial z^{\alpha} \partial \bar{z}^{\beta}}+\Gamma_{j k}^{i} \frac{\partial f^{j}}{\partial \bar{z}^{\beta}} \frac{\partial f^{k}}{\partial z^{\alpha}}\right) d z^{\alpha} \wedge d \bar{z}^{\beta} \otimes e_{i}=0 .$$
$f$ is called Hermitian harmonic if it satisfies $\operatorname{tr}_{\omega_{h}} \partial_{\mathscr{E}} \bar{\partial} f=0$, i.e.
$$h^{\alpha \bar{\beta}}\left(\frac{\partial^{2} f^{i}}{\partial z^{\alpha} \partial \bar{z}^{\beta}}+\Gamma_{j k}^{i} \frac{\partial f^{j}}{\partial \bar{z}^{\beta}} \frac{\partial f^{k}}{\partial z^{\alpha}}\right) \otimes e_{i}=0 .$$
Moreover, it is easy to see that
Corollary 2.2. Let $f:(M, h) \rightarrow(N, g)$ be a smooth map from a compact Kähler manifold $(M, h)$ to a Riemannian manifold $(N, g)$. Then Hermitian harmonic maps and harmonic maps coincide.

Let $(M, g)$ be a Riemannian manifold with Levi-Civita connection ∇ . The curvature tensor is defined as $R(X, Y) Z=\nabla_{X} \nabla_{Y} Z-\nabla_{Y} \nabla_{X} Z-\nabla_{[X, Y]} Z$ for any $X, Y, Z \in \Gamma(M, T M)$. In the local coordinates $\left\{x^{i}\right\}$ of $M$, we adopt the convention $R(X, Y, Z, W)=g(R(X, Y) Z, W)=R_{i j k \ell} X^{i} Y^{j} Z^{k} W^{\ell}$. It is easy to see that
$$R_{i j k}^{\ell}=\frac{\partial \Gamma_{k j}^{\ell}}{\partial x^{i}}-\frac{\partial \Gamma_{k i}^{\ell}}{\partial x^{j}}+\Gamma_{k j}^{p} \Gamma_{p i}^{\ell}-\Gamma_{k i}^{p} \Gamma_{p j}^{\ell}$$
and $R_{i j k \ell}=g_{s \ell} R_{i j k}^{s}$.
Lemma 2.3. Let $f: M \rightarrow(N, g)$ be a smooth map from a complex manifold $M$ to a Riemannian manifold $(N, g)$. Then then (1, 1)-part of the curvature tensor of $\mathscr{E}=f^{*}(T N)$ is
$$\bar{\partial}_{\mathscr{E}} \partial_{\mathscr{E}}+\partial_{\mathscr{E}} \bar{\partial}_{\mathscr{E}}=R_{i j k}^{\ell} \frac{\partial f^{i}}{\partial z^{\alpha}} \frac{\partial f^{j}}{\partial \bar{z}^{\beta}} d z^{\alpha} \wedge d \bar{z}^{\beta} \otimes e^{k} \otimes e_{\ell} .$$
Proof. By straightforward computations, we have
$$\partial_{\mathscr{E}}\left(e_{i}\right)=\Gamma_{j i}^{k} \frac{\partial f^{j}}{\partial z^{\alpha}} d z^{\alpha} \cdot e_{k}, \quad \bar{\partial}_{\mathscr{E}}\left(e_{i}\right)=\Gamma_{j i}^{k} \frac{\partial f^{j}}{\partial \bar{z}^{\beta}} d \bar{z}^{\beta} \cdot e_{k}$$
Therefore,
$$\bar{\partial}_{\mathscr{E}} \partial_{\mathscr{E}}\left(e_{i}\right)=-\left[\frac{\partial \Gamma_{j i}^{k}}{\partial x^{\ell}} \frac{\partial f^{\ell}}{\partial \bar{z}^{\beta}} \frac{\partial f^{j}}{\partial z^{\alpha}}+\Gamma_{j i}^{k} \frac{\partial^{2} f^{j}}{\partial z^{\alpha} \partial \bar{z}^{\beta}}+\Gamma_{p \ell}^{k} \Gamma_{j i}^{\ell} \frac{\partial f^{j}}{\partial z^{\alpha}} \frac{\partial f^{p}}{\partial \bar{z}^{\beta}}\right] d z^{\alpha} \wedge d \bar{z}^{\beta} \cdot e_{k},$$
and
$$\partial_{\mathscr{E}} \bar{\partial}_{\mathscr{E}}\left(e_{i}\right)=\left[\frac{\partial \Gamma_{j i}^{k}}{\partial x^{\ell}} \frac{\partial f^{\ell}}{\partial z^{\alpha}} \frac{\partial f^{j}}{\partial \bar{z}^{\beta}}+\Gamma_{j i}^{k} \frac{\partial^{2} f^{j}}{\partial z^{\alpha} \partial \bar{z}^{\beta}}+\Gamma_{p \ell}^{k} \Gamma_{j i}^{\ell} \frac{\partial f^{j}}{\partial \bar{z}^{\beta}} \frac{\partial f^{p}}{\partial z^{\alpha}}\right] d z^{\alpha} \wedge d \bar{z}^{\beta} \cdot e_{k}$$
Hence, by using the curvature formula (2.14), we obtain (2.15). \(\square\)

The following constraint equation for pluri-harmonic maps is well-known (e.g. [OU91, Lemma 1.3]), and for readers' convenience, we include a proof here.

Lemma 2.4. If $f: M \rightarrow(N, h)$ is a pluri-harmonic map, then
$$R_{i k j \ell} f_{\alpha}^{i} f_{\bar{\beta}}^{j} f_{\gamma}^{k}=0$$
for any $\alpha, \beta, \gamma$ and $\ell$ where $f_{\alpha}^{i}=\frac{\partial f^{i}}{\partial z^{\alpha}}$ and $f_{\beta}^{j}=\frac{\partial f^{j}}{\partial \bar{z}^{\beta}}$.
Proof. Recall that $\mathscr{E}=f^{*}(T N) . f$ is pluri-harmonic, then $\bar{\partial}_{\mathscr{E}} \partial f=\partial_{\mathscr{E}} \bar{\partial} f=0$. On the other hand, by symmetric, it is easy to see that $\partial_{\mathscr{E}} \partial f=\bar{\partial}_{\mathscr{E}} \bar{\partial} f=0$. Indeed,
$$\bar{\partial}_{\mathscr{E}} \bar{\partial} f=\bar{\partial}_{\mathscr{E}}\left(\frac{\partial f^{j}}{\partial \bar{z}^{\beta}} d \bar{z}^{\beta} \otimes e_{i}\right)=\left(\frac{\partial^{2} f^{i}}{\partial \bar{z}^{\alpha} \partial \bar{z}^{\beta}}+\Gamma_{j k}^{i} \frac{\partial f^{j}}{\partial \bar{z}^{\alpha}} \frac{\partial f^{k}}{\partial \bar{z}^{\beta}}\right)\left(d \bar{z}^{\alpha} \wedge d \bar{z}^{\beta}\right) \otimes e_{i}=0 .$$
Hence, $\left(\partial_{\mathscr{E}} \bar{\partial}_{\mathscr{E}}+\bar{\partial}_{\mathscr{E}} \partial_{\mathscr{E}}\right) \partial f=0$ and by (2.15), it is equivalent to
$$R_{i j k \ell} f_{\alpha}^{i} f_{\bar{\beta}}^{j} f_{\gamma}^{k}\left(d z^{\alpha} \wedge d \bar{z}^{\beta} \wedge d z^{\gamma}\right)=0$$
for all $\ell$. By using symmetry and the Bianchi identity, we obtain
$$\left(R_{i j k \ell}-R_{k j i \ell}\right) f_{\alpha}^{i} f_{\beta}^{j} f_{\gamma}^{k}=R_{i k j \ell} f_{\alpha}^{i} f_{\bar{\beta}}^{j} f_{\gamma}^{k}=0 .$$
Hence, we get (2.16). \(\square\)

\section*{3. Rigidity of pluri-harmonic maps into Riemannian manifolds}

In this section, we shall prove Theorem 1.6. Let $f:(M, h) \rightarrow(N, g)$ be a smooth map from a compact Hermitian manifold $M$ to a Riemannian manifold $(N, g)$. Let
$$\mathscr{F}=T^{* 1,0} M \otimes f^{*}(T N)=T^{* 1,0} M \otimes \mathscr{E}$$
and $\nabla^{\mathscr{F}}$ be the induced connection on $\mathscr{F}$ by using the Chern connection on $M$ and Levi-Civita connection on $N$. We have a natural decomposition $\nabla^{\mathscr{F}}=\partial_{\mathscr{F}}+\bar{\partial}_{\mathscr{F}}$. It is obvious that $\partial f \in \Gamma(M, \mathscr{F})$.

Lemma 3.1. If $f: M \rightarrow(N, h)$ is a pluri-harmonic map, then $\bar{\partial}_{\mathscr{F}}(\partial f)=0$, i.e.
$$\bar{\partial}_{\mathscr{F}}(\partial f)=\left[\left(\frac{\partial^{2} f^{i}}{\partial z^{\alpha} \partial \bar{z}^{\beta}}+\Gamma_{j k}^{i} \frac{\partial f^{j}}{\partial \bar{z}^{\beta}} \frac{\partial f^{k}}{\partial z^{\alpha}}\right) d \bar{z}^{\beta}\right] \otimes d z^{\alpha} \otimes e_{i}=0$$
Proof. Note that $\bar{\partial}_{\mathscr{F}}(\partial f) \in \Omega^{0,1}(M, \mathscr{F})$. Since $\partial f=\frac{\partial f^{i}}{\partial z^{\alpha}} d z^{\alpha} \otimes e_{i} \in \Gamma(M, \mathscr{F})$ and $\nabla^{\mathscr{F}}$ is induced by the Chern connection on $M$ and Levi-Civita connection on $N$,
$$\bar{\partial}_{\mathscr{F}} \partial f=\bar{\partial}_{\mathscr{F}}\left(\frac{\partial f^{i}}{\partial z^{\alpha}} d z^{\alpha} \otimes e_{i}\right)=\left(\frac{\partial^{2} f^{i}}{\partial z^{\alpha} \partial \bar{z}^{\beta}}+\Gamma_{j k}^{i} \frac{\partial f^{j}}{\partial \bar{z}^{\beta}} \frac{\partial f^{k}}{\partial z^{\alpha}}\right) d \bar{z}^{\beta} \otimes d z^{\alpha} \otimes e_{i} .$$
By the definition equation (2.12) of pluri-harmonic maps, we get $\bar{\partial}_{\mathscr{F}} \partial f=0$. \(\square\)

The following result is a generalization of the classical Chern-Lu identity ([Che68, Lu68], see also [Yang18a, Lemma 5.1]).

Proposition 3.2. Let $f:(M, h) \rightarrow(N, g)$ be a pluri-harmonic map from a Hermitian manifold $M$ to a Riemannian manifold $(N, g)$. Then we have
$$\partial \bar{\partial} u=\left\langle\partial_{\mathscr{F}} \partial f, \partial_{\mathscr{F}} \partial f\right\rangle+\left(R_{\alpha \bar{\beta}} \bar{\delta}^{h \gamma^{\bar{\nu}}} h^{\mu \bar{\delta}} g_{i j} f_{\mu}^{i} f_{\bar{\nu}}^{j}-R_{i \ell k j} f_{\alpha}^{i} f_{\bar{\beta}}^{j}\left(h^{\gamma \bar{\delta}} f_{\gamma}^{k} f_{\bar{\delta}}^{\ell}\right)\right) d z^{\alpha} \wedge d \bar{z}^{\beta} .$$
and
$$\Delta_{h} u=\left|\partial_{\mathscr{F}} \partial f\right|^{2}+\left(h^{\alpha \bar{\beta}} R_{\alpha \bar{\beta} \gamma \bar{\delta}}\right) h^{\gamma \bar{\nu}} h^{\mu \bar{\delta}} g_{i j} f_{\mu}^{i} f_{\bar{\nu}}^{j}-R_{i \ell k j}\left(h^{\alpha \bar{\beta}} f_{\alpha}^{i} f_{\bar{\beta}}^{j}\right)\left(h^{\gamma \bar{\delta}} f_{\gamma}^{k} f_{\bar{\delta}}^{\ell}\right),$$
where $u=|\partial f|^{2}$ and $\Delta_{h} u=h^{\alpha \bar{\beta}} \frac{\partial^{2} u}{\partial z^{\alpha} \partial \bar{z}^{\beta}}$.
Proof. By using Bochner technique, we have
$$\begin{aligned}
\partial \bar{\partial} u & =\partial\left\langle\bar{\partial}_{\mathscr{F}} \partial f, \partial f\right\rangle+\partial\left\langle\partial f, \partial_{\mathscr{F}} \partial f\right\rangle \\
& =\partial\left\langle\partial f, \partial_{\mathscr{F}} \partial f\right\rangle \\
& =\left\langle\partial_{\mathscr{F}} \partial f, \partial_{\mathscr{F}} \partial f\right\rangle+\left\langle\partial f, \bar{\partial}_{\mathscr{F}} \partial_{\mathscr{F}} \partial f\right\rangle \\
& =\left\langle\partial_{\mathscr{F}} \partial f, \partial_{\mathscr{F}} \partial f\right\rangle+\left\langle\partial f,\left(\partial_{\mathscr{F}} \bar{\partial}_{\mathscr{F}}+\bar{\partial}_{\mathscr{F}} \partial_{\mathscr{F}}\right) \partial f\right\rangle
\end{aligned}$$
Since $\mathscr{F}=T^{* 1,0} M \otimes \mathscr{E}$, we have the curvature formula
$$\partial_{\mathscr{F}} \bar{\partial}_{\mathscr{F}}+\bar{\partial}_{\mathscr{F}} \partial_{\mathscr{F}}=R^{T^{* 1,0} M} \otimes \mathrm{Id}_{\mathscr{E}}+\mathrm{Id}_{\mathrm{T}^{* 1,0} \mathrm{M}} \otimes\left(\partial_{\mathscr{E}} \bar{\partial}_{\mathscr{E}}+\bar{\partial}_{\mathscr{E}} \partial_{\mathscr{E}}\right) .$$

Let's compute the curvature term on the target manifold. By using the expression
$$\left[\operatorname{Id}_{\mathrm{T}^{* 1,0} \mathrm{M}} \otimes\left(\partial_{\mathscr{E}} \bar{\partial}_{\mathscr{E}}+\bar{\partial}_{\mathscr{E}} \partial_{\mathscr{E}}\right)\right] \partial f=\left(R_{i j k}^{\ell} f_{\alpha}^{i} f_{\bar{\beta}}^{j} f_{\delta}^{k} d z^{\alpha} \wedge d \bar{z}^{\beta}\right) \cdot d z^{\delta} \otimes e_{\ell}$$
we obtain
$$\left\langle\partial f,\left[\operatorname{Id}_{\mathrm{T}^{* 1,0} \mathrm{M}} \otimes\left(\partial_{\mathscr{E}} \bar{\partial}_{\mathscr{E}}+\bar{\partial}_{\mathscr{E}} \partial_{\mathscr{E}}\right)\right] \partial f\right\rangle=-R_{i j k \ell} f_{\alpha}^{i} f_{\beta}^{j}\left(h^{\gamma \bar{\delta}} f_{\gamma}^{k} f_{\bar{\delta}}^{\ell}\right) d z^{\alpha} \wedge d \bar{z}^{\beta}$$
(Note that, in general, (3.6) has no positivity.) By the constraint equation (2.16) for pluri-harmonic maps, one has $-R_{i k \ell j} f_{\alpha}^{i} f_{\frac{1}{\beta}}^{j} f_{\gamma}^{k}=0$ for any $\alpha, \beta, \gamma, \ell$, and so
$$-R_{i k \ell j} f_{\alpha}^{i} f_{\bar{\beta}}^{j}\left(h^{\gamma \bar{\delta}} f_{\gamma}^{k} f_{\bar{\delta}}^{\ell}\right)=0 .$$
Then by the Bianichi identity, we get
$$\begin{aligned}
\left\langle\partial f,\left[\operatorname{Id}_{\mathrm{T}^{* 1,0} \mathrm{M}} \otimes\left(\partial_{\mathscr{E}} \bar{\partial}_{\mathscr{E}}+\bar{\partial}_{\mathscr{E}} \partial_{\mathscr{E}}\right)\right] \partial f\right\rangle & =-R_{i j k \ell} f_{\alpha}^{i} f_{\beta}^{j}\left(h^{\gamma \bar{\delta}} f_{\gamma}^{k} f_{\bar{\delta}}^{\ell}\right) d z^{\alpha} \wedge d \bar{z}^{\beta} \\
& =-R_{i \ell k j} f_{\alpha}^{i} f_{\bar{\beta}}^{j}\left(h^{\gamma \bar{\delta}} f_{\gamma}^{k} f_{\bar{\delta}}^{\ell}\right) d z^{\alpha} \wedge d \bar{z}^{\beta} .
\end{aligned}$$
On the other hand, it is easy to see that
$$\left\langle\partial f,\left[R^{T^{* 1,0} M} \otimes \operatorname{Id}_{\mathscr{E}}\right] \partial f\right\rangle=R_{\alpha \bar{\beta} \gamma \bar{\delta}} h^{\gamma \bar{\nu}} h^{\mu \bar{\delta}} g_{i j} f_{\mu}^{i} f_{\bar{\nu}}^{j} d z^{\alpha} \wedge d \bar{z}^{\beta} .$$
Hence, we get formula (3.3) and by taking trace, one has (3.4). \(\square\)

Let $(N, g)$ be a Riemannian manifold and $T_{\mathbb{C}} N:=T N \otimes \mathbb{C}$ be the complexification of the real vector bundle $T N$. We can extend the metric $g$ and $\nabla$ to $T_{\mathbb{C}} N$ in the $\mathbb{C}$-linear way and still denote them by $g$ and $\nabla$ respectively.

Definition 3.3. $(N, g)$ is said to have non-positive complex sectional curvature if
$$R(Z, \bar{W}, W, \bar{Z}) \leq 0$$
for any $Z, W \in T_{\mathbb{C}} N$.
Definition 3.4. A Hermitian manifold $(M, h)$ is called uniformly $R C$-positive if the Chern curvature tensor of the Hermitian tangent bundle $\left(T^{1,0} M, h\right)$ is uniformly RC-positive, i.e., at every point $p \in M$, there exists some vector $u \in T_{p}^{1,0} M$ such that for any nonzero vector $v \in T_{p}^{1,0} M$, one has
$$R^{h}(u, \bar{u}, v, \bar{v})=R_{\alpha \bar{\beta} \gamma \bar{\delta}} u^{\alpha} \bar{u}^{\beta} v^{\gamma} \bar{v}^{\delta}>0 .$$

Theorem 3.5. Let $f: M \rightarrow(N, g)$ be a pluri-harmonic map from a compact complex manifold to a Riemannian manifold $(N, g)$ with non-positive complex sectional curvature. If $T^{1,0} M$ is uniformly $R C$-positive, then $f$ is a constant map.

Proof. Suppose-to the contrary-that $f$ is not a constant map, then $u=|\partial f|^{2}$ is not constant. Suppose $u$ attains a maximum value at some point $p \in M$. Let $h$ be a Hermitian metric on $M$ such that has uniformly RC-positive curvature. At point $p$,
there exists a nonzero vector $a=\left(a_{\alpha}\right)$ such that the curvature of $\left(T^{1,0} M, h\right)$ has the property
$$R_{\alpha \bar{\beta} \gamma \bar{\delta}} a_{\alpha} \bar{a}_{\beta} v_{\gamma} \bar{v}_{\delta}>0$$
for all $v \neq 0$. In particular, we have
$$\sum_{i, \alpha, \beta, \gamma, \delta} R_{\alpha \bar{\beta} \gamma \bar{\delta}} a_{\alpha} \bar{a}_{\beta} f_{\delta}^{i} \overline{f_{\gamma}^{i}}>0 .$$
On the other hand, let $u^{i}=\sum_{\alpha} f_{\alpha}^{i} a_{\alpha}$, then
$$\sum_{\alpha, \beta} R_{i \ell k j} f_{\alpha}^{i} f_{\beta}^{j}\left(h^{\gamma \bar{\delta}} f_{\gamma}^{k} f_{\bar{\delta}}^{\ell}\right) a_{\alpha} \bar{a}_{\beta}=\sum_{\gamma} R_{i \ell k j} u^{i} \bar{u}^{j} f_{\gamma}^{k} f_{\bar{\gamma}}^{\ell} .$$
Since $(N, h)$ has non-positive complex sectional curvature, we deduce
$$\sum_{\gamma} R_{i \ell k j} u^{i} \bar{u}^{j} f_{\gamma}^{k} f_{\bar{\gamma}}^{\ell} \leq 0$$
By formulas (3.3), (3.9) and (3.10), we get a contradiction. Hence $f$ must be a constant. \(\square\)

By using similar arguments for the equation (3.4), we can also prove
Corollary 3.6. Let $f: M \rightarrow(N, g)$ be a pluri-harmonic map from a compact complex manifold to a Riemannian manifold $(N, g)$ with non-positive complex sectional curvature. If $M$ has a Hermitian metric $\omega$ such that the second Chern-Ricci curvature $\left(h^{\alpha \bar{\beta}} R_{\alpha \bar{\beta} \gamma \bar{\delta}}\right)$ is positive definite, then $f$ is a constant map.
4. Rigidity of Hermitian harmonic maps into Riemannian manifolds

In this section, we prove Theorem 1.8 by using Theorem 1.6 and ideas in [Siu80, Sam85, Sam86, JY91, JY93, LY14].

Lemma 4.1. Let $f:(M, h) \rightarrow(N, g)$ be a smooth map from a compact Hermitian manifold $(M, h)$ to a Riemannian manifold $(N, g)$. Then
$$\partial \bar{\partial}\{\bar{\partial} f, \bar{\partial} f\} \frac{\omega_{h}^{m-2}}{(m-2)!}=4\left(\left|\partial_{\mathscr{E}} \bar{\partial} f\right|^{2}-\left|\operatorname{tr}_{\omega_{h}} \partial_{\mathscr{E}} \bar{\partial} f\right|^{2}\right) \frac{\omega_{h}^{m}}{m!}+Q \cdot \frac{\omega_{h}^{m}}{m!},$$
where
$$Q=-4 h^{\alpha \bar{\delta}} h^{\gamma \bar{\beta}} R_{i j k \ell} \frac{\partial f^{i}}{\partial z^{\alpha}} \frac{\partial f^{k}}{\partial \bar{z}^{\beta}} \frac{\partial f^{j}}{\partial z^{\gamma}} \frac{\partial f^{\ell}}{\partial \bar{z}^{\delta}} .$$
Proof. It is well-known (e.g. [LY14, Lemma 6.10] or [OU91]) by using a standard Bochner type calculations. For readers' convenience, we sketch a proof here following Siu's $\partial \bar{\partial}$ trick. It is easy to see that $\bar{\partial}_{\mathscr{E}} \bar{\partial} f=0$. Hence, we have
$$\partial \bar{\partial}\{\bar{\partial} f, \bar{\partial} f\}=-\left\{\partial_{\mathscr{E}} \bar{\partial} f, \partial_{\mathscr{E}} \bar{\partial} f\right\}+\left\{\bar{\partial} f,\left(\bar{\partial}_{\mathscr{E}} \partial_{\mathscr{E}}+\partial_{\mathscr{E}} \bar{\partial}_{\mathscr{E}}\right) \bar{\partial} f\right\} .$$

Moreover,
$$-\left\{\partial_{\mathscr{E}} \bar{\partial} f, \partial_{\mathscr{E}} \bar{\partial} f\right\} \frac{\omega_{h}^{m-2}}{(m-2)!}=4\left(\left|\partial_{\mathscr{E}} \bar{\partial} f\right|^{2}-\left|\operatorname{tr}_{\omega_{\mathrm{h}}} \partial_{\mathscr{E}} \bar{\partial} f\right|^{2}\right) \frac{\omega_{h}^{m}}{m!},$$
and by [Huy05, Corollary 1.2.28]
$$\left\{\bar{\partial} f,\left(\bar{\partial}_{\mathscr{E}} \partial_{\mathscr{E}}+\partial_{\mathscr{E}} \bar{\partial}_{\mathscr{E}}\right) \bar{\partial} f\right\} \frac{\omega_{h}^{m-2}}{(m-2)!}=4\left\langle\sqrt{-1}\left[\bar{\partial}_{\mathscr{E}} \partial_{\mathscr{E}}+\partial_{\mathscr{E}} \bar{\partial}_{\mathscr{E}}, \Lambda_{\omega_{h}}\right] \bar{\partial} f, \bar{\partial} f\right\rangle \frac{\omega_{h}^{m}}{m!} .$$
Moreover,
$$\left\langle\sqrt{-1}\left[\bar{\partial}_{\mathscr{E}} \partial_{\mathscr{E}}+\partial_{\mathscr{E}} \bar{\partial}_{\mathscr{E}}, \Lambda_{\omega_{h}}\right] \bar{\partial} f, \bar{\partial} f\right\rangle=-h^{\alpha \bar{\delta}} h^{\gamma \bar{\beta}} R_{i j k \ell} \frac{\partial f^{i}}{\partial z^{\alpha}} \frac{\partial f^{k}}{\partial \bar{z}^{\beta}} \frac{\partial f^{j}}{\partial z^{\gamma}} \frac{\partial f^{\ell}}{\partial \bar{z}^{\delta}} .$$
Therefore, the formula (4.1) follows. \(\square\)

The following formulation is essentially obtained in [LY14, Theorem 6.11].
Theorem 4.2. Let $(M, h)$ be a compact astheno-Kähler manifold (i.e. $\partial \bar{\partial} \omega_{h}^{m-2}=0$ ) and $(N, g)$ a Riemannian manifold. Let $f:(M, h) \rightarrow(N, g)$ be a Hermitian harmonic map. If $(N, g)$ has non-positive complex sectional curvature, then $f$ is pluri-harmonic.

Proof. If $f$ is Hermitian harmonic, i.e., $\operatorname{tr}_{\omega_{h}} \partial_{\mathscr{E}} \bar{\partial} f=0$, by formula (4.1),
$$\int_{M} \partial \bar{\partial}\{\bar{\partial} f, \bar{\partial} f\} \frac{\omega_{h}^{m-2}}{(m-2)!}=4 \int_{M}\left|\partial_{\mathscr{E}} \bar{\partial} f\right|^{2} \frac{\omega_{h}^{m}}{m!}+\int_{M} Q \cdot \frac{\omega_{h}^{m}}{m!} .$$
From integration by parts, we obtain
$$4 \int_{M}\left|\partial_{\mathscr{E}} \bar{\partial} f\right|^{2} \frac{\omega_{h}^{m}}{m!}+\int_{M} Q \cdot \frac{\omega_{h}^{m}}{m!}=0 .$$
If ( $N, g$ ) has non-positive complex sectional curvature, then $Q \geq 0$ and so $\partial_{\mathscr{E}} \bar{\partial} f=0$, i.e. $f$ is pluri-harmonic. \(\square\)

In particular, one has the following result obtained in [Sam86, Theorem 1] (see also [JY91, Lemma 4.2] and [YZ91, Theorem])

Corollary 4.3. Let $(M, h)$ be a compact Kähler manifold and $(N, g)$ a Riemannian manifold. Let $f:(M, h) \rightarrow(N, g)$ be a harmonic map. If $(N, g)$ has non-positive complex sectional curvature, then $f$ is pluri-harmonic.

Proof. It follows by Corollary 2.2 and Theorem 4.2. \(\square\)

The proof of Theorem 1.8. Let $(M, h)$ be a compact astheno-Kähler manifold and $(N, g)$ be a Riemannian manifold with non-positive complex sectional curvature. By Theorem 4.2, every Hermitian harmonic map $f:(M, h) \rightarrow(N, g)$ is pluri-harmonic. Let $h_{0}$ be a Hermitian metric on $M$ such that $\left(T^{1,0} M, h_{0}\right)$ is uniformly RC-positive, then by Theorem 1.6, the pluri-harmonic map $f: M \rightarrow(N, g)$ is constant. \(\square\)

\section*{References}
\begin{itemize}
\item[] [Cam92] Campana, F. Connexité rationnelle des variétés de Fano. Ann. Sci. Ecole Norm. Sup. (4) 25 (1992), no. 5, 539-545.
\item[] [Che68] Chern, S. S. On the holomorphic mappings of hermitian manifolds of the same dimension, Proc. Symp. Pure Math, Vol. 11, 157-170 1968.
\item[] [Dong13] Dong, Y.X. Monotonicity formulae and holomorphicity of harmonic maps between Kähler manifolds. Proc. Lond. Math. Soc. (3) 107 (2013), 1221-1260.
\item[] [ES64] Eells, J.; Sampson, J. Harmonic mappings of Riemannian manifolds. Amer. J. Math. 86(1964) 109-160.
\item[] [EL78] Eells, J.; Lemaire, L. A report on harmonic maps. Bull. London Math. Soc. 10 (1978), 1-68.
\item[] [EL83] Eells, J.; Lemaire, L. Selected topics in harmonic maps. CBMS Regional Conference Series in Mathematics, 50. 1983.
\item[] [EL88] Eells, J.; Lemaire, L. Another report on harmonic maps. Bull. London Math. Soc. 20 (1988), no. 5, 385-524.
\item[] [Huy05] Huybrechts, D. Complex geometry. An introduction. Universitext. Springer-Verlag, Berlin, 2005.
\item[] [JY91] Jost, J.; Yau, S.-T. Harmonic maps and Kähler geometry. Prospects in complex geometry (Katata and Kyoto, 1989), 340-370, Lecture Notes in Math., 1468, Springer, Berlin, 1991.
\item[] [JY93] Jost, J.; Yau, S.-T. A nonlinear elliptic system for maps from Hermitian to Riemannian manifolds and rigidity theorems in Hermitian geometry. Acta Math. 170 (1993), no. 2, 221-254.
\item[] [KMM92] Kollár, J.; Miyaoka, Y.; Mori, S. Rationally connected varieties. J. Algebraic Geom. 1 (1992), no. 3, 429-448.
\item[] [LSYY17] Liu, K.; Sun,-X; Yang, X; Yau. S-.T. Curvatures of moduli space of curves and applications. Asian J. Math. 21(2017), 841-854.
\item[] [LY14] Liu, K.; Yang, X. Hermitian harmonic maps and non-degenerate curvatures. Math. Res. Lett. 21 (2014), no.4, 831-862.
\item[] [LY17] Liu, K.-F.; Yang, X.-K. Ricci curvatures on Hermitian manifolds.Trans. Amer. Math. Soc. 369 (2017), 5157-5196.
\item[] [Mat09] Matsuo, K. Astheno-Kähler structures on Calabi-Eckmann manifolds. Colloq. Math. 115 (2009), no. 1, 33-39
\item[] [Lu68] Lu, Y. Holomorphic mappings of complex manifolds, J. Differential Geom. 2 (1968), 299-312.
\item[] [MSY93] Mok, N.; Siu, Y.-T.; Yeung, S.-K. Geometric superrigidity. Invent. Math. 113 (1993), 57-83.
\item[] [Ni99] Ni, L. Hermitian harmonic maps from complete Hermitian manifolds to complete Riemannian manifolds. Math. Z. 232 (1999), no. 2, 331-355.
\item[] [Ni18] Ni, L. Liouville theorems and a Schwarz Lemma for holomorphic mappings between Kähler manifolds. arXiv:1807.02674
\item[] [Ohn87] Ohnita, Y. On pluriharmonicity of stable harmonic maps. J. London Math. Soc. (2) 35 (1987), no. 3, 563-568.
\end{itemize}
\begin{itemize}
\item[] [OU90] Ohnita, Y.; Udagawa, S. Stability, complex-analyticity and constancy of pluriharmonic maps from compact Kähler manifolds. Math. Z. 205 (1990), 629-644.
\item[] [OU91] Ohnita, Y.; Udagawa, S. Complex-analyticity of pluriharmonic maps and their constructions. Lecture Notes in Math., 1468, 371-407, 1991.
\item[] [Sam85] Sampson, J.-H. Harmonic maps in Kähler geometry: Harmonic mappings and minimal immersions, 193-205, Lecture Notes in Math., 1161, 1985.
\item[] [Sam86] Sampson, J.-H. Applications of harmonic maps to Kähler geometry. Contemp. Math., 49, 125-134, Amer. Math. Soc., Providence, RI, 1986.
\item[] [Siu80] Siu, Y.-T. The complex-analyticity of harmonic maps and the strong rigidity of compact Kähler manifolds. Ann. of Math. (2) 112 (1980), no. 1, 73-111.
\item[] [Siu82] Siu, Y.-T. Complex-analyticity of harmonic maps, vanishing and Lefschetz theorems. J. Differential Geom. 17 (1982), no. 1, 55-138.
\item[] [Tos07] Tossati, V. A general Schwarz lemma for almost-Hermitian manifolds. Comm. Anal. Geom. 15 (2007), no. 5, 1063-1086.
\item[] [Uda88] Udagawa, S. Pluriharmonic maps and minimal immersions of Kähler manifolds. J. London Math. Soc. (2) 37 (1988), no. 2, 375-384.
\item[] [Uda94] Udagawa, S. Classification of pluriharmonic maps from compact complex manifolds with positive first Chern class into complex Grassmann manifolds. Tohoku Math. J. (2) 46 (1994), no. 3, 367-391.
\item[] [YHD13] Yang, G.; Han, Y.; Dong, Y. Partial energies monotonicity and holomorphicity of Hermitian pluriharmonic maps. Sci. China Math. 56 (2013), 1019-1032.
\item[] [Yang17] Yang, X.-K. Big vector bundles and compact complex manifolds with semipositive tangent bundles. Math. Ann. 267(2017), no.1, 251-282. MR 3606441
\item[] [Yang18] Yang, X.-K. RC-positivity, rational connectedness and Yau's conjecture. Camb. J. Math. 6 (2018), 183-212.
\item[] [Yang18a] Yang, X.-K. RC-positivity, vanishing theorems and rigidity of holomorphic maps. arXiv:1807.02601
\item[] [Yang18b] Yang, X.-K. RC-positive metrics on rationally connected manifolds. arXiv:1807.03510.
\item[] [YZ18] Yang, X.-K.; Zheng, F.-Y. On real bisectional curvature for Hermitian manifolds. arXiv:1610.07165. To appear in Trans. Amer. Math. Soc.
\item[] [Yau78] Yau, S.-T. A general Schwarz lemma for Kähler manifolds, Amer. J. Math. 100 (1978), no. 1, 197-203.
\item[] [Yau78a] Yau, S.-T. On the Ricci curvature of a compact Kähler manifold and the complex Monge-Ampère equation, I, Comm. Pure Appl. Math. 31 (1978), 339-411.
\item[] [YZ91] Yau, S.-T.; Zheng, F. Negatively $\frac{1}{4}$-pinched Riemannian metric on a compact Kähler manifold. Invent. Math. 103 (1991), no. 3, 527-535.
\item[] [Zhang12] Zhang, X. Hermitian harmonic maps between almost Hermitian manifolds. Adv. Lect. Math. 2012. 485-493.
\end{itemize}

Address of Jun Wang: Tsinghua University, Yau Mathematical Science Center, Beijing, 100084, China.

Address of Xiaokui Yang: Morningside Center of Mathematics, Institute of Mathematics, Hua Loo-Keng Center of Mathematical Sciences, Academy of Mathematics and Systems Science, Chinese Academy of Sciences, Beijing, 100190, China.

E-mail address: xkyang@amss.ac.cn
---
retention_scope: session
part: 1
total_parts: 2
---

[Part 1/2 of: Conformal Kähler rigidity of Einstein four-manifolds]

---
source_file: 2607_21538.pdf
converter: mathpix
format: mmd
---

\title{
CONFORMAL KÄHLER RIGIDITY OF EINSTEIN FOUR-MANIFOLDS
}

\author{
GIOVANNI CATINO AND DAVIDE DAMENO
}

\begin{abstract}
For a compact, connected, oriented Einstein four-manifold, we prove that, if the largest eigenvalue of the self-dual Weyl curvature $W^{+}$is everywhere simple, then, after at worst passing to a double cover, the metric is conformally Kähler with positive scalar curvature; more generally, this result holds for metrics with harmonic self-dual Weyl curvature. For Einstein metrics satisfying a uniform simplicity hypothesis on the largest eigenvalue, we further prove that either $W^{+} \equiv 0$, or $W^{+}$ nowhere vanishes and the previous conclusion holds. We also obtain extensions to complete Ricci-flat four-manifolds and an optimal pinching theorem for the holomorphic sectional curvature of compact Kähler-Einstein surfaces. The proof combines LeBrun's conformal normalization with the resulting weighted divergence equation and new first-order identities. A zero-capacity argument allows this method to be used across the zero set of $W^{+}$and at infinity in the noncompact case. Finally, K3 surfaces and multicentered Gibbons-Hawking gravitational instantons show that our assumptions are sharp.
\end{abstract}

\section*{1. Introduction}

Let $(M, h)$ be an oriented Einstein manifold of dimension four, i.e., its Ricci tensor $\operatorname{Ric}_{h}$ is proportional to the metric $h$ : in this case, the curvature information, apart from the value of the scalar curvature, is all encoded in the self-dual and anti-self-dual Weyl tensors, which can be regarded as linear, symmetric, trace-free endomorphisms
$$W_{h}^{ \pm}: \Lambda^{ \pm} \longrightarrow \Lambda^{ \pm}$$
of the bundles $\Lambda^{ \pm}$, arising as eigenspaces of the Hodge operator acting on the bundle $\Lambda^{2}$ of 2-forms. Throughout the paper, we assume that every manifold we consider is connected.

We focus on the symmetric operator $W_{h}^{+}$and we denote its eigenvalues by
$$\alpha_{h} \geq \beta_{h} \geq \gamma_{h}, \quad \alpha_{h}+\beta_{h}+\gamma_{h}=0 .$$
The main aim of this paper is to show that a rather weak assumption on the two largest eigenvalues $\alpha_{h}$ and $\beta_{h}$ actually implies strong rigidity for $(M, h)$, connecting the conformal properties of $h$ with the existence of Kähler

\footnotetext{
2020 Mathematics Subject Classification. Primary 53C25, 53C24; Secondary 53C18, 53C21, 53C55.

Key words and phrases. Einstein four-manifolds, harmonic self-dual Weyl tensor, conformally Kähler metrics, gravitational instantons, Kähler-Einstein surfaces.
}
structures on $M$. More precisely, we show that, after possibly passing to a double cover of $M$ (see Section 2 for a more complete explanation),
$$\alpha_{h}>\beta_{h} \quad \text { on } M \quad \Longrightarrow \quad \beta_{h}=\gamma_{h}=-\frac{1}{2} \alpha_{h} \quad \text { on } M .$$
A well-known result due to Derdziński [16, Proposition 5] implies that the conformal metric $g=\alpha_{h}^{2 / 3} h$ is Kähler with positive scalar curvature and, as a consequence, $h$ has to be a Hermitian Einstein metric with positive scalar curvature.

More precisely, we prove the following.
Theorem 1.1. Let $(M, h)$ be a compact oriented Einstein four-manifold. Assume that
$$\alpha_{h}>\beta_{h} \quad \text { on } M .$$
Then, after at worst passing to a double cover of $M, h$ is conformal to a Kähler metric with positive scalar curvature. In particular, $h$ is a Hermitian Einstein metric with positive scalar curvature.

This result gains importance when viewed in the context of classifying compact Einstein four-manifolds with positive scalar curvature: indeed, LeBrun [33, 34] proved that, in the Hermitian, simply connected setting, $(M, h)$ is either Kähler-Einstein or isometric to the first del Pezzo surface $\mathbb{C P}^{2} \# \overline{\mathbb{C P}^{2}}$ endowed with the Page metric [47], or to the second del Pezzo surface $\mathbb{C P}^{2} \# 2 \overline{\mathbb{C P}^{2}}$ endowed with the Chen-LeBrun-Weber metric [14]. In the Kähler-Einstein case, by the classification and existence results of Tian [54] and Odaka-Spotti-Sun [45], the underlying complex surface $(M, J)$ is biholomorphic to $\mathbb{C P}^{2}, \mathbb{C P}^{1} \times \mathbb{C P}^{1}$ or $\mathbb{C P}^{2} \# k \overline{\mathbb{C P}^{2}}, 3 \leq k \leq 8$, with the blown-up points in general position. As a consequence, Theorem 1.1 provides the classification of all compact, simply connected Einstein four-manifolds $(M, h)$ with positive scalar curvature and simple largest eigenvalue of $W_{h}^{+}$ (see Corollary 1.6 for a more general result).

We point out that, in this context, the proof of Theorem 1.1 only relies on $h$ having harmonic self-dual Weyl curvature, i.e.
$$\delta_{h} W_{h}^{+} \equiv 0,$$
where $\delta_{h}$ denotes the divergence operator: this condition is satisfied by all Einstein four-manifolds [6]. Theorem 1.1 is a direct consequence of the following result.

Theorem 1.2. Let $(M, h)$ be a compact oriented Riemannian four-manifold with
$$\delta_{h} W_{h}^{+}=0 \quad \text { on } M .$$
Assume that
$$\alpha_{h}>\beta_{h} \quad \text { on } M .$$
Then, after at worst passing to a double cover of $M, h$ is conformal to a Kähler metric with positive scalar curvature.

Conversely, if $(M, g, J)$ is a compact Kähler surface, with respect to the complex orientation, and with $s_{g}>0$, then $h=s_{g}^{-2} g$ satisfies $\delta_{h} W_{h}^{+}=0$ and $\alpha_{h}>\beta_{h}$.

Given a Riemannian four-manifold $(M, h)$, on the set $\left\{W_{h}^{+} \neq 0\right\}$ we can define the conformally invariant ratio
$$\rho=\frac{\beta_{h}}{\alpha_{h}}:$$
this is a continuous function which satisfies
$$-\frac{1}{2} \leq \rho \leq 1,$$
since $W_{h}^{+}$is trace-free. One can immediately observe that
$$\begin{aligned}
\rho=-\frac{1}{2} \quad & \Longleftrightarrow \quad \beta_{h}=\gamma_{h}=-\frac{1}{2} \alpha_{h}, \\
\rho=1 \quad & \Longleftrightarrow \quad \alpha_{h}=\beta_{h}, \quad \gamma_{h}=-2 \alpha_{h} .
\end{aligned}$$
A simple computation shows that
$$\frac{\operatorname{det}\left(W_{h}^{+}\right)}{\left|W_{h}^{+}\right|^{3}}=-\frac{\rho(1+\rho)}{2^{3 / 2}\left(1+\rho+\rho^{2}\right)^{3 / 2}}:$$
the right-hand side is non-increasing on $[-1 / 2,1]$ and attains its minimum at $\rho=1$, i.e.
$$\frac{\operatorname{det}\left(W_{h}^{+}\right)}{\left|W_{h}^{+}\right|^{3}}=-\frac{1}{3 \sqrt{6}} \quad \Longleftrightarrow \quad \alpha_{h}=\beta_{h}>0 .$$
With this in mind, Theorem 1.2 can be rephrased as
$$\rho<1 \quad \text { on } M \quad \Longrightarrow \quad \rho=-\frac{1}{2} \quad \text { on } M .$$
This result improves upon the previously known results: indeed, in his seminal paper, Derdziński proved the existence of a conformal Kähler metric on $\left\{W_{h}^{+} \neq 0\right\}$ under the hypothesis $\# \operatorname{spec}\left(W_{h}^{+}\right) \leq 2$, i.e. $\rho \in\{-1 / 2,1\}$ [16]. More recently, Wu improved this result by assuming that $\operatorname{det}\left(W_{h}^{+}\right)>0$, i.e. $\rho<0$ [56], and LeBrun showed that it is sufficient to assume
$$\frac{\operatorname{det}\left(W_{h}^{+}\right)}{\left|W_{h}^{+}\right|^{3}} \geq-\frac{5 \sqrt{2}}{21 \sqrt{21}},$$
i.e. $\rho \leq 1 / 4$ [36]. By (1.1) and the previous considerations, Theorem 1.2 gives the following consequence.
Corollary 1.3. Let $(M, h)$ be a compact oriented Riemannian four-manifold with $\delta_{h} W_{h}^{+}=0$. Assume that
$$\operatorname{det}\left(W_{h}^{+}\right)>-\frac{1}{3 \sqrt{6}}\left|W_{h}^{+}\right|^{3} \quad \text { on } M .$$
Then, after at worst passing to a double cover of $M, h$ is conformal to a Kähler metric with positive scalar curvature.

The proofs build upon LeBrun's conformal method [36]: indeed, we make use of the fact that, up to passing to the double cover of $M$ determined by the eigenspace of $W_{h}^{+}$associated to $\alpha_{h}$, the smooth, real line subbundle $L \subset \Lambda^{+}$defined by this eigenspace is trivial and, therefore, we can exploit LeBrun's conformal normalization
$$g=\alpha_{h}^{2 / 3} h .$$
Together with the weighted version of the well-known Weitzenböck formula for metrics with harmonic self-dual Weyl curvature discovered by Derdziński, we obtain the crucial integral identity (3.5). The new ingredient is a system of first-order identities for the eigenvalues of $W_{g}^{+}$on its regular spectral set (Proposition 2.3); these equations imply (3.5) and therefore force an eigenform $\omega_{1}$, associated to $\alpha_{g}$, to be parallel and hence to be the Kähler form of $g$. We point out that this approach comes from merging the ideas of Derdziński [16] and LeBrun [36]: indeed, we make use of Derdziński's formulas for the derivatives of the eigenvalues of $W_{h}^{+}$, applied to the weighted self-dual Weyl curvature $\alpha_{h}^{-1 / 3} W_{g}^{+}$.

For Einstein metrics, we may allow $W_{h}^{+}$to vanish a priori by replacing the pointwise simplicity hypothesis with a uniform simplicity assumption on the largest eigenvalue. More precisely, the following results extend Theorem 1.2 and Corollary 1.3:

Theorem 1.4. Let $(M, h)$ be a compact oriented Einstein four-manifold. Assume that $W_{h}^{+} \not \equiv 0$ and that, for some constant $\rho_{0}<1$,
$$\beta_{h} \leq \rho_{0} \alpha_{h} \quad \text { on } M .$$
Then, after at worst passing to a double cover of $M, h$ is conformal to a Kähler metric with positive scalar curvature. In particular, $h$ is a Hermitian Einstein metric with positive scalar curvature.

Since $M$ is compact, obviously, if $\alpha_{h}>\beta_{h}$ everywhere, the eigenvalues satisfy the hypothesis of Theorem 1.4. We can rephrase this result in terms of $\operatorname{det}\left(W_{h}^{+}\right)$as well:

Corollary 1.5. Let $(M, h)$ be a compact oriented Einstein four-manifold. Assume that $W_{h}^{+} \not \equiv 0$ and that
$$\operatorname{det}\left(W_{h}^{+}\right) \geq-c\left|W_{h}^{+}\right|^{3} \quad \text { on } M$$
for some constant
$$0 \leq c<\frac{1}{3 \sqrt{6}} .$$
Then, after at worst passing to a double cover of $M, h$ is conformal to a Kähler metric with positive scalar curvature. In particular, $h$ is a Hermitian Einstein metric with positive scalar curvature.

Combining Theorem 1.4 with the classification of anti-self-dual Einstein four-manifolds with positive scalar curvature [20, 28] and the classification of

Hermitian Einstein four-manifolds cited above, we can classify all compact Einstein manifolds with positive scalar curvature and uniformly simple largest eigenvalue.

Corollary 1.6. Let $(M, h)$ be a compact simply connected oriented Einstein four-manifold with positive scalar curvature. Assume that
$$\beta_{h} \leq \rho_{0} \alpha_{h} \quad \text { on } M$$
for some $\rho_{0}<1$. Then, one of the following holds:
\begin{itemize}
\item[-] $(M, h)$ is, up to homothety and isometry, either $\mathbb{S}^{4}$ or $\overline{\mathbb{C} \mathbb{P}^{2}}$, endowed with their standard metrics;
\item[-] $h$ is Kähler-Einstein, and the underlying complex surface is biholomorphic to
$$\mathbb{C P}^{2}, \quad \mathbb{C P}^{1} \times \mathbb{C P}^{1}, \quad \text { or } \quad \mathbb{C P}^{2} \# k \overline{\mathbb{C P}^{2}}, \quad 3 \leq k \leq 8,$$
with the blown-up points in general position;
\item[-] h is Hermitian non-Kähler and is, up to homothety and isometry, the Page metric on $\mathbb{C P}^{2} \# \overline{\mathbb{C P}^{2}}$ or the Chen-LeBrun-Weber metric on $\mathbb{C} \mathbb{P}^{2} \# 2 \overline{\mathbb{C} \mathbb{P}^{2}}$.
\end{itemize}

The idea to prove these results is to apply the same computations used in Theorem 1.2, combined with a zero-capacity argument for the zero set of $W_{h}^{+}$. More precisely, we use the Einstein condition to show that $W_{h}^{+}$is a non-trivial solution of a system of first-order elliptic PDEs and we exploit a known result due to Bär to control the size of the zero set of $W_{h}^{+}$[4]: then, we construct a suitable sequence of Lipschitz functions $\chi_{j}$, which are compactly supported in $\left\{W_{h}^{+} \neq 0\right\}$ and allow us to deal with the boundary terms arising in the integration by parts procedure in $\left\{W_{h}^{+} \neq 0\right\}$, thanks to which we obtain again the identity (3.5) on this open subset. At this point, it is sufficient to use Derdziński's celebrated result on the zeros of $W_{h}^{+}$on Einstein four-manifolds to show that, if $W_{h}^{+} \not \equiv 0$, then $W_{h}^{+}$nowhere vanishes and this concludes the proof [16, Proposition 5 (iv)].

With these results in mind, taking the contrapositive of Theorem 1.4, we can obtain a useful restriction on Einstein metrics of nonpositive scalar curvature.

Corollary 1.7. Let $(M, h)$ be a compact oriented Einstein four-manifold with nonpositive scalar curvature. If $W_{h}^{+} \not \equiv 0$, then
$$\sup _{\left\{W_{h}^{+} \neq 0\right\}} \frac{\beta_{h}}{\alpha_{h}}=1 .$$

We highlight the fact that the spectral hypotheses in Theorems 1.1 and 1.4 are sharp: indeed, we manage to show that some K3 surfaces, endowed with a Calabi-Yau metric, admit points at which, after reversing the hyperkähler orientation, we have
$$\alpha_{h}=\beta_{h}>0 ;$$
since these spaces do not admit metrics with positive scalar curvature, we obtain that the conclusion of Theorem 1.4 fails.

The same method can be adapted to study compact Kähler-Einstein surfaces $(M, g, J)$ with nonpositive scalar curvature. In this setting, we can analyze the holomorphic sectional curvature $H$ and obtain a sharp classification result, under the same spectral hypothesis as in Theorem 1.4: more precisely, if we denote by $H_{\text {min }}$ and $H_{\text {max }}$ the minimum and the maximum of the holomorphic sectional curvature, respectively, and by $H_{\mathrm{av}}$ its average over $\mathbb{C P}^{1}$, we obtain the following result.

Theorem 1.8. Let $(M, h, J)$ be a compact Kähler-Einstein surface with nonpositive scalar curvature. Assume that there exists a constant $\theta<2 / 3$ such that, at every point where $H_{\text {max }}>H_{\text {min }}$,
$$H_{\mathrm{av}}-H_{\min } \leq \theta\left(H_{\max }-H_{\min }\right) .$$
Then $W_{h}^{-} \equiv 0$. Consequently, either $h$ is flat and $M$ is finitely covered by a flat complex torus, or $h$ has constant negative holomorphic sectional curvature and $M$ is a compact quotient of the complex ball.

At every point $p \in M$ such that $H_{\text {max }}>H_{\text {min }}$, the ratio
$$\Theta:=\frac{H_{\mathrm{av}}-H_{\min }}{H_{\max }-H_{\min }}$$
lies in [1/3, 2/3]: thus, Theorem 1.8 only assumes a uniform gap below the upper bound 2/3. Siu and Yang obtained the same rigidity theorem under a nonpositive bisectional curvature assumption and imposing $\Theta<\frac{2}{3(1+\sqrt{6 / 11})}$ [51], while Guan proved the same conclusion under the condition $\Theta \leq 1 / 2$ without a sign assumption on the bisectional curvature [25]. Our statement requires no sign assumption on the sectional or the bisectional curvature and covers every uniform bound strictly below 2/3. We point out that Theorem 1.8 is optimal: indeed, recently, compact negatively curved Kähler-Einstein manifolds which are not covered by the complex ball have been constructed via gluing and deformation methods [26], which means that the value 2/3 cannot be included.

The combination of Derdziński's Weitzenböck formula, LeBrun's conformal method and the zero-capacity argument (Proposition 4.1) can be, to some extent, also applied to noncompact Einstein four-manifolds: in particular, in the presence of suitable volume growth and curvature decay assumptions at infinity, we can adapt our line of reasoning to the complete case. It is well known that the study of the eigenvalues of $W_{h}^{+}$is closely related to the classification of the so-called gravitational instantons, i.e. complete, noncompact four-manifolds admitting a Ricci-flat metric such that the $L^{2}$-norm of the curvature tensor is finite: indeed, these spaces can be distinguished into three different types, which correspond to different multiplicities of the eigenvalues of $W_{h}^{+}$(see e.g. the recent survey [39] and the references therein). In our
setting, we are able to prove the following general result for noncompact Ricci-flat manifolds:

Theorem 1.9. Let $(M, h)$ be a complete, oriented, noncompact Ricci-flat four-manifold. Assume that $W_{h}^{+} \not \equiv 0$ and that, for some $\rho_{0}<1$,
$$\beta_{h} \leq \rho_{0} \alpha_{h} \quad \text { on } M .$$
Suppose moreover that there exist $\nu, q \geq 0$ and $p_{0} \in M$ such that
$$\left\{\begin{array}{l}
\operatorname{Vol}_{h}\left(B_{h}\left(p_{0}, R\right)\right)=O\left(R^{\nu}\right) \\
\left|\operatorname{Rm}_{h}\right|=O\left(R^{-q}\right) \quad \text { on } M \backslash B_{h}\left(p_{0}, R\right)
\end{array} \quad \text { as } R \rightarrow \infty, \quad \nu-2-\frac{2 q}{3}<0 .\right.$$
Then, after at worst passing to a double cover of $M, h$ is conformal to a Kähler metric with positive scalar curvature. In particular, $h$ is Ricci-flat, Hermitian and non-Kähler.

As far as gravitational instantons are concerned, we can obtain two rigidity results. The first is a direct consequence of Theorem 1.9: indeed, recalling the celebrated work of Bando, Kasue and Nakajima [3], we show that $(M, h)$ is a Type II gravitational instanton (i.e. Hermitian non-Kähler) having an asymptotically locally Euclidean (ALE) end, under a non-collapsing hypothesis on the volume of geodesic balls (see Corollary 6.1). Furthermore, we also apply the zero-capacity argument to prove a classification result for collapsed gravitational instantons, under the same hypothesis as in Theorem 1.4, obtaining the examples found by Biquard and Gauduchon [7], recently classified as the only collapsed Type II instantons with an asymptotically locally flat (ALF) end by Li [38] (Theorem 6.3). We highlight the fact that, as explained later (see Remark 6.4), this result can be seen as a direct consequence of Theorem 1.9 and a celebrated result due to Cheeger and Tian [12]: however, the proof we included here only relies on the zero-capacity argument and Hölder's inequality. Similar techniques involving the use of the weighted Weitzenböck formula (2.9) (but without the zero-capacity argument) are also exploited in [8].

As for the compact case, the uniform bound $\beta_{h} \leq \rho_{0} \alpha_{h}$, with $\rho_{0}<1$, is optimal: indeed, we show that there exist multicentered Gibbons-Hawking gravitational instantons $(M, h)$ [22,23] with tetrahedral symmetry which, if we consider the orientation opposite to the one induced by the hyperkähler structure, admit points where $\alpha_{h}=\beta_{h}$ and for which the conclusion of Theorem 1.9 does not hold. In this case, we also describe an explicit loss of continuity phenomenon for $\rho$ around a point where $W_{h}^{+}=0$.

The paper is organized as follows. In Section 2, we provide some preliminaries and describe LeBrun's conformal normalization: furthermore, we prove the weighted Derdziński identities and the crucial first-order identities (2.5). In Section 3, we prove Theorem 1.2 (and, therefore, Theorem 1.1) and Corollary 1.3. Section 4 deals with the zero set of $W_{h}^{+}$: here we prove Theorem 1.4 and its consequences (Corollary 1.5, Corollary 1.7). Section 5
is devoted to the proof of Theorem 1.8. Section 6 treats complete Ricci-flat manifolds and gravitational instantons: here we prove Theorem 1.9 and the classification results for noncollapsed (Corollary 6.1) and collapsed (Theorem 6.3) gravitational instantons. Finally, in Section 7 we construct the compact and noncompact examples for which the largest eigenvalue has multiplicity two, which show the optimality of our results.

Remark 1.10. We point out that, given any oriented Riemannian fourmanifold $(M, h)$, reversing the orientation causes the subbundles $\Lambda^{+}$and $\Lambda^{-}$to swap, which implies that the operators $W_{h}^{+}$and $W_{h}^{-}$are exchanged. Hence, all the results stated for $W_{h}^{+}$can also be written in terms of $W_{h}^{-}$: the only important caveat is that, if we choose to work with the anti-self-dual Weyl curvature $W_{h}^{-}$, the conformal metric $g=\alpha_{h}^{2 / 3} h$ will be Kähler with respect to the opposite orientation (here $\alpha_{h}$ is the largest eigenvalue of $W_{h}^{-}$ with respect to the previous orientation).

\section*{Acknowledgements}

The authors would like to thank Andrea Malchiodi and Benedetta Piroddi for interesting and helpful discussions regarding the examples described in Section 7. Both authors are members of the Gruppo Nazionale per le Strutture Algebriche, Geometriche e le loro Applicazioni (GNSAGA) of the Istituto Nazionale di Alta Matematica (INdAM).

\section*{2. LeBrun's conformal change}

In this section, we adapt a strategy due to LeBrun [36] based on a specific conformal change of the metric $h$. First, we recall some well-known facts about four-dimensional Riemannian geometry (see e.g. [6] for more detailed discussions). Let $(M, h)$ be a connected, oriented Riemannian four-manifold: the action of the Hodge operator $*=*_{h}$ on the bundle of 2 -forms $\Lambda^{2}$ induces the conformally invariant splitting $\Lambda^{2}=\Lambda_{h}^{+} \oplus \Lambda_{h}^{-}$, where, at every point, $\Lambda_{h}^{ \pm}$is the eigenspace of $*$ associated to the eigenvalue ±1. We call $\Lambda_{h}^{ \pm}$the subbundles of self-dual and anti-self-dual forms, respectively, and we say that a 2-form $\omega$ is self-dual (respectively, anti-self-dual) if $* \omega=\omega$ (respectively, if $* \omega=-\omega$ ): by conformal invariance of the Hodge operator on 2-forms, we know that the subbundles $\Lambda_{h}^{ \pm}$are conformally invariant, hence, throughout the paper, we will write $\Lambda^{ \pm}=\Lambda \frac{ \pm}{\bar{h}}$ for every $\bar{h} \in[h]$. Since the Weyl tensor $W_{h}$ preserves the subbundles, this decomposition also induces a splitting of $W_{h}$ into a self-dual and an anti-self-dual part, denoted respectively by $W_{h}^{+}$and $W_{h}^{-}$. Both can be regarded as linear, trace-free, symmetric endomorphisms of the subbundles $\Lambda^{ \pm}$and one has $* W_{h}^{ \pm}= \pm W_{h}^{ \pm}$: equivalently, $W_{h}^{+}$and $W_{h}^{-}$may be viewed as a self-dual and an anti-self-dual $\Lambda^{ \pm}$-valued 2-form, respectively.

We say that $(M, h)$ has harmonic Weyl curvature if $\delta_{h} W_{h}=0$ on $M$, where $\delta_{h}$ denotes the divergence operator: since $M$ is four-dimensional, the
splitting of $W_{h}$ allows us to define metrics with harmonic (anti-)self-dual Weyl curvature, i.e. metrics satisfying $\delta_{h} W_{h}^{ \pm}=0$ on $M$. The harmonic Weyl condition enjoys a weighted conformal covariance property (see also [36, 48]):

Lemma 2.1. Let $(M, h)$ be a Riemannian four-manifold and let $g=f^{-2} h$, for some smooth positive function $f$ on $M$. Then,
$$\delta_{g}\left(f W_{g}\right)=f\left(\delta_{h} W_{h}\right) .$$
In particular, we have that
$$\delta_{h} W_{h}=0 \quad \Longleftrightarrow \quad \delta_{g}\left(f W_{g}\right)=0 ;$$
furthermore, (2.1) holds independently for $W_{h}^{ \pm}$.
Proof. First, let $g=e^{2 u} h, u \in C^{\infty}(M)$ : by the conformal invariance of the $(1,3)$ version of the Weyl tensor, we obtain (see also [11])
$$\delta_{g} W_{g}=\delta_{h} W_{h}+W_{h}\left(\nabla^{h} u, \cdot, \cdot, \cdot\right) .$$
An easy computation then shows that, for every smooth function $f$ on $M$,
$$\delta_{g}\left(f W_{g}\right)=W_{h}\left(\nabla^{h} f, \cdot, \cdot, \cdot\right)+f\left[\delta_{h} W_{h}+W_{h}\left(\nabla^{h} u, \cdot, \cdot, \cdot\right)\right] .$$
Now, putting $f=e^{-u}$, we immediately obtain
$$\begin{aligned}
\delta_{g}\left(f W_{g}\right) & =W_{h}\left(\nabla^{h} f, \cdot, \cdot, \cdot\right)+f\left[\delta_{h} W_{h}-\frac{1}{f} W_{h}\left(\nabla^{h} f, \cdot, \cdot, \cdot\right)\right] \\
& =f \delta_{h} W_{h}
\end{aligned}$$
which proves the claims. The same holds for $W_{h}^{ \pm}$since the Hodge operator commutes with the covariant derivative induced by the Levi-Civita connection. \(\square\)

Remark 2.2. One can actually prove a more general result: if $(M, h)$ is a Riemannian manifold of dimension $n \geq 4$, then $\delta_{g}\left(f^{n-3} W_{g}\right)=f^{n-3}\left(\delta_{h} W_{h}\right)$, where $g=f^{-2} h$.

From now on, we focus on $W_{h}^{+}$: since, at every point $p \in M, W_{h}^{+}$is a symmetric, linear map from $\left(\Lambda^{+}\right)_{p}$ to itself, we can define its eigenvalues
$$\alpha_{h} \geq \beta_{h} \geq \gamma_{h} .$$
Let $U \subset M$ be an open set on which $\alpha_{h}>\beta_{h}$ : then, $\alpha_{h}$ is a smooth positive function on $U$. We set
$$f=\alpha_{h}^{-1 / 3}, \quad g=f^{-2} h=\alpha_{h}^{2 / 3} h .$$
By the conformal invariance of $*$ and $W_{h}^{+}$, viewed as a (1,3)-tensor, the eigenvalues of $W_{g}^{+}: \Lambda^{+} \rightarrow \Lambda^{+}$are given by
$$\alpha=f^{2} \alpha_{h}, \quad \beta=f^{2} \beta_{h}, \quad \gamma=f^{2} \gamma_{h} .$$
Consequently,
$$f \alpha=1, \quad \frac{\beta}{\alpha}=\frac{\beta_{h}}{\alpha_{h}}=\rho, \quad \gamma=-(1+\rho) \alpha .$$

All the geometric quantities below are computed with respect to $g$, unless explicitly stated otherwise. We assume that $h$ has harmonic self-dual Weyl curvature,
$$\delta_{h} W_{h}^{+}=0$$
and we introduce
$$\mathcal{W}^{+}=f W^{+},$$
whose eigenvalues are
$$\mu_{1}=1, \quad \mu_{2}=\rho, \quad \mu_{3}=-(1+\rho) ;$$
in particular, the largest eigenvalue $\mu_{1}$ is constant. Moreover, by (2.1),
$$\delta \mathcal{W}^{+}=0 .$$
Since $\alpha_{h}>\beta_{h}$ on $U$, the eigenspace of $W_{h}^{+}$associated to $\alpha_{h}$ varies smoothly on $U$, hence determining a smooth, real line bundle
$$\left.L \subset \Lambda^{+}\right|_{U}$$
over $U$. As explained in [36, Section 2], $L$ need not to be orientable; however, its sphere bundle
$$\widehat{U}:=\left\{\omega \in L:|\omega|^{2}=2\right\}$$
is a double cover of $U$ and the pullback of $L$ to $\widehat{U}$ has a global smooth section $\omega_{1}$ such that
$$\left|\omega_{1}\right|^{2}=2, \quad W^{+}\left(\omega_{1}\right)=\alpha \omega_{1} ;$$
Therefore, up to passing to this double cover, we can always assume that $L$ is orientable and, hence, trivial; for notational simplicity, whenever we pass to such a cover we use the same symbols for the pulled-back tensors and metrics. The normalization $\left|\omega_{1}\right|^{2}=2$ is chosen since, given any point $p$, a self-dual form $\eta \in\left(\Lambda^{+}\right)_{p}$ with $|\eta|^{2}=2$ corresponds to an almost complex structure $J$, compatible with $g$ and the orientation, on $T_{p} M$ such that $\eta=g(J \cdot, \cdot)$.

Following Derdziński [16], let $M_{W}$ denote the regular spectral set of $W_{g}^{+}$, namely the set of points at which the number of distinct eigenvalues is locally constant. Let $M_{W}^{U}:=M_{W} \cap U$. Since $\alpha>\beta$ on $U$, if
$$Z:=\{x \in U: \beta(x)=\gamma(x)\},$$
then
$$M_{W}^{U}=(U \backslash Z) \cup \operatorname{int}_{U} Z=U \backslash \partial_{U} Z .$$
Observe that $Z$ is closed in $U$ and its boundary has empty interior; thus $M_{W}^{U}$ is open and dense in $U$. Locally, we can complete the section $\omega_{1}$ to an oriented orthogonal frame $\left\{\omega_{1}, \omega_{2}, \omega_{3}\right\}$ of $\Lambda^{+}$, which we can express as
$$\omega_{1}=e^{12}+e^{34}, \quad \omega_{2}=e^{13}-e^{24}, \quad \omega_{3}=e^{14}+e^{23},$$
where $e^{i j}=e^{i} \wedge e^{j}$ and $\left\{e^{i}\right\}$ is a local oriented $g$-orthonormal coframe. Near any point at which $\beta \neq \gamma$, the forms $\omega_{2}$ and $\omega_{3}$ are chosen to be smooth eigenforms of $W^{+}$, i.e.,
$$W^{+}\left(\omega_{2}\right)=\beta \omega_{2}, \quad W^{+}\left(\omega_{3}\right)=\gamma \omega_{3} ;$$
on the other hand, on $\operatorname{int}_{U} Z$ the restriction of $W^{+}$to $L^{\perp}$ is a multiple of the identity, so any smooth oriented orthogonal frame of $L^{\perp}$ is an eigenframe. This observation allows us to perform all the following local computations on $M_{W}^{U}$. Since $\left|\omega_{1}\right|$ is constant, there are locally defined one-forms $a$ and $c$ [16] such that
$$\nabla \omega_{1}=a \otimes \omega_{2}-c \otimes \omega_{3},$$
where
$$a=\sum_{i=1}^{4} a_{i} e^{i}, \quad c=\sum_{i=1}^{4} c_{i} e^{i} .$$
We note that, on $M_{W}^{U}$, the completion of $\omega_{1}$ to an orthogonal basis defined by (2.2) also provides the equations for the covariant derivatives of $\omega_{2}$ and $\omega_{3}$, which yield the system
$$\left\{\begin{aligned}
\nabla \omega_{1} & =a \otimes \omega_{2}-c \otimes \omega_{3}, \\
\nabla \omega_{2} & =-a \otimes \omega_{1}+b \otimes \omega_{3} \\
\nabla \omega_{3} & =c \otimes \omega_{1}-b \otimes \omega_{2},
\end{aligned}\right.$$
where $b$ is a one-form locally defined by $b=\sum_{i=1}^{4} b_{i} e^{i}$ (see [16, Equation (32)]).

We now prove new fundamental first-order identities on the coefficients of $\omega_{i}$, in the spirit of Derdziński's local computations [16].
Proposition 2.3. On $M_{W}^{U}$, one has
$$(1-\rho) \iota_{a^{\sharp}} \omega_{3}+(2+\rho) \iota_{c^{\sharp}} \omega_{2}=0 .$$
Equivalently, if
$$k=\frac{1-\rho}{2+\rho},$$
then
$$c_{2}=k a_{1}, \quad c_{1}=-k a_{2}, \quad c_{4}=k a_{3}, \quad c_{3}=-k a_{4} .$$
Proof. Fix $p \in M_{W}^{U}$ and a neighborhood $V$ on which the eigenframe $\left\{\omega_{1}, \omega_{2}, \omega_{3}\right\}$ is smooth. Let
$$A=\frac{1}{2} \sum_{r=1}^{3} \mu_{r} \omega_{r} \otimes \omega_{r}$$
be a divergence-free section of $S_{0}^{2} \Lambda^{+}$which is diagonal in this frame, i.e.
$$A\left(\omega_{r}\right)=\mu_{r} \omega_{r}, \quad\left|\omega_{r}\right|^{2}=2 .$$
Equivalently,
$$A_{i j k l}=\frac{1}{2} \sum_{r=1}^{3} \mu_{r}\left(\omega_{r}\right)_{i j}\left(\omega_{r}\right)_{k l} .$$
We compute at a fixed point and choose the tangent frame $e_{1}, \ldots, e_{4}$ to be geodesic there: we use the fact that, for every $p \in M_{W}^{U}$, the operator $W^{+}$
can be smoothly diagonalized in an open neighborhood of $p$. The condition $\delta A=0$ is
$$0=(\delta A)_{j k l}=-\nabla_{i} A_{i j k l},$$
i.e.
$$0=\sum_{i=1}^{4} \sum_{r=1}^{3}\left[d \mu_{r}\left(e_{i}\right)\left(\omega_{r}\right)_{i j}\left(\omega_{r}\right)_{k l}+\mu_{r}\left(\nabla_{i} \omega_{r}\right)_{i j}\left(\omega_{r}\right)_{k l}+\mu_{r}\left(\omega_{r}\right)_{i j}\left(\nabla_{i} \omega_{r}\right)_{k l}\right] .$$
First, we compute (2.6) putting $j=l=2, k=1$, which yields
$$\begin{aligned}
0 & =\sum_{i=1}^{4} \sum_{r=1}^{3}\left[d \mu_{r}\left(e_{i}\right)\left(\omega_{r}\right)_{i 2}\left(\omega_{r}\right)_{12}+\mu_{r}\left(\nabla_{i} \omega_{r}\right)_{i 2}\left(\omega_{r}\right)_{12}+\mu_{r}\left(\omega_{r}\right)_{i 2}\left(\nabla_{i} \omega_{r}\right)_{12}\right] \\
& =: I+I I+I I I .
\end{aligned}$$
By (2.2) and (2.3), a direct computation gives
$$\begin{aligned}
I & =\sum_{i, r} d \mu_{r}\left(e_{i}\right)\left(\omega_{r}\right)_{i 2}\left(\omega_{r}\right)_{12}=d \mu_{1}\left(e_{1}\right) ; \\
I I & =\sum_{i=1}^{4} \mu_{1}\left(\nabla_{i} \omega_{1}\right)_{i 2}=\sum_{i=1}^{4} \mu_{1}\left(a_{i} \omega_{2}-c_{i} \omega_{3}\right)_{i 2}=\mu_{1}\left(a_{4}+c_{3}\right) ; \\
I I I & =\mu_{1}\left(\nabla_{1} \omega_{1}\right)_{12}+\mu_{2}\left(\nabla_{4} \omega_{2}\right)_{12}-\mu_{3}\left(\nabla_{3} \omega_{3}\right)_{12} \\
& =\mu_{2}\left(-a_{4} \omega_{1}+b_{4} \omega_{3}\right)_{12}-\mu_{3}\left(c_{3} \omega_{1}-b_{3} \omega_{2}\right)_{12}=-\mu_{2} a_{4}-\mu_{3} c_{3} ;
\end{aligned}$$
this implies that
$$d \mu_{1}\left(e_{1}\right)=-\left(\mu_{1}-\mu_{2}\right) a_{4}-\left(\mu_{1}-\mu_{3}\right) c_{3} .$$
Performing analogous computations with $(j, k, l)=(1,1,2),(3,1,2),(4,1,2)$, we also obtain
$$\begin{aligned}
& d \mu_{1}\left(e_{2}\right)=-\left(\mu_{1}-\mu_{2}\right) a_{3}+\left(\mu_{1}-\mu_{3}\right) c_{4} \\
& d \mu_{1}\left(e_{3}\right)=\left(\mu_{1}-\mu_{2}\right) a_{2}+\left(\mu_{1}-\mu_{3}\right) c_{1} \\
& d \mu_{1}\left(e_{4}\right)=\left(\mu_{1}-\mu_{2}\right) a_{1}-\left(\mu_{1}-\mu_{3}\right) c_{2}
\end{aligned}$$
i.e.
$$\begin{aligned}
d \mu_{1}= & {\left[-\left(\mu_{1}-\mu_{2}\right) a_{4}-\left(\mu_{1}-\mu_{3}\right) c_{3}\right] e^{1}+\left[-\left(\mu_{1}-\mu_{2}\right) a_{3}+\left(\mu_{1}-\mu_{3}\right) c_{4}\right] e^{2} } \\
& +\left[\left(\mu_{1}-\mu_{2}\right) a_{2}+\left(\mu_{1}-\mu_{3}\right) c_{1}\right] e^{3}+\left[\left(\mu_{1}-\mu_{2}\right) a_{1}-\left(\mu_{1}-\mu_{3}\right) c_{2}\right] e^{4} \\
= & \left(\mu_{1}-\mu_{2}\right)\left(-a_{4} e^{1}-a_{3} e^{2}+a_{2} e^{3}+a_{1} e^{4}\right) \\
& +\left(\mu_{1}-\mu_{3}\right)\left(-c_{3} e^{1}+c_{4} e^{2}+c_{1} e^{3}-c_{2} e^{4}\right)
\end{aligned}$$
Now, one has that
$$\begin{aligned}
& \iota_{a^{\sharp} \omega_{3}}=-a_{4} e^{1}-a_{3} e^{2}+a_{2} e^{3}+a_{1} e^{4} \\
& \iota_{c^{\sharp}} \omega_{2}=-c_{3} e^{1}+c_{4} e^{2}+c_{1} e^{3}-c_{2} e^{4},
\end{aligned}$$
which means that
$$d \mu_{1}=\left(\mu_{1}-\mu_{2}\right) \iota_{a^{\sharp}} \omega_{3}+\left(\mu_{1}-\mu_{3}\right) \iota_{c^{\sharp}} \omega_{2} ;$$
we point out that this equation also appears in [56, Section 2] and it is a rewriting of Derdziński's first-order identity for the first eigenvalue [16].

We now apply (2.8) to $A=\mathcal{W}^{+}=f W^{+}$. By (2.1), $A$ is divergence-free, and its eigenvalues are
$$\mu_{1}=1, \quad \mu_{2}=\rho, \quad \mu_{3}=-(1+\rho) .$$
Thus $d \mu_{1}=0$, and (2.8) becomes
$$0=(1-\rho) \iota_{a^{\sharp}} \omega_{3}+(2+\rho) \iota_{c^{\sharp}} \omega_{2},$$
which proves (2.4). Substituting (2.7) into (2.4) and comparing coefficients yields (2.5). \(\square\)

Remark 2.4. The weight $f$ is crucial for removing the terms involving $d \alpha$ from (2.8). Indeed, $f=\alpha_{h}^{-1 / 3}$ is precisely the conformal factor for which $\delta\left(f W^{+}\right)=0$ and $\mu_{1}=1$.

We shall also use the Weitzenböck formula for divergence-free sections of $S_{0}^{2} \Lambda^{+}$in the weighted conformal form exploited by LeBrun [36, Equations (8)-(9)], derived from the standard identity for metrics with harmonic self-dual Weyl curvature due to Derdziński [16]. Since $\mathcal{W}^{+}=f W^{+}$is divergence-free, we have
$$\delta^{\nabla} \mathcal{W}^{+} \equiv 0,$$
where we view $\mathcal{W}^{+}$as a $\Lambda^{+}$-valued 2-form, $\delta^{\nabla}=-* d^{\nabla} *$ and $d^{\nabla}$ is the exterior covariant derivative induced by the Levi-Civita connection on $\Lambda^{+}$: since $\mathcal{W}^{+}$is self-dual, we also obtain
$$0=*\left(\delta^{\nabla} \mathcal{W}^{+}\right)=-*\left(* d^{\nabla} *\left(\mathcal{W}^{+}\right)\right)=d^{\nabla} \mathcal{W}^{+},$$
which implies that $\Delta_{H} \mathcal{W}^{+} \equiv 0$, where $\Delta_{H}=d^{\nabla} \delta^{\nabla}+\delta^{\nabla} d^{\nabla}$ is the Hodge Laplacian. Thus, by exploiting the classical Weitzenböck formula for tracefree, symmetric bundle endomorphisms (see e.g. [10, Proposition 4.2]), we obtain the well-known

Lemma 2.5. Let $(M, g)$ be an oriented Riemannian four-manifold, and let $f$ be a positive smooth function such that
$$\delta_{g}\left(f W_{g}^{+}\right)=0 \quad \text { on } M .$$
Then
$$0=\nabla^{*} \nabla\left(f W_{g}^{+}\right)+\frac{s_{g}}{2} f W_{g}^{+}-6 f W_{g}^{+} \circ W_{g}^{+}+2 f\left|W_{g}^{+}\right|^{2} I,$$
where $I$ denotes the identity endomorphism of $\Lambda^{+}$.

\section*{3. Proof of Theorem 1.2 and Corollary 1.3}

Proof of Theorem 1.2. By the discussion at the beginning of Section 2, we know that the subbundle $L \subset \Lambda^{+}$defined by the eigenspace of $\alpha_{h}$ is smooth
and, after passing, if necessary, to a double cover of $M$, we may assume that $L$ is trivial. As before, we set
$$g=\alpha_{h}^{2 / 3} h .$$
From now on, unless specified otherwise, all geometric quantities are computed with respect to $g$; hence we write
$$\Lambda^{+}=\Lambda_{g}^{+}, \quad \alpha=\alpha_{g}, \quad W^{+}=W_{g}^{+}, \quad s=s_{g} .$$
Furthermore, we recall that, for every $\eta_{1}, \eta_{2} \in \Lambda^{+}$,
$$\left\langle W^{+}\left(\eta_{1}\right), \eta_{2}\right\rangle=W^{+}\left(\eta_{1}, \eta_{2}\right)=\left\langle W^{+}, \eta_{1} \otimes \eta_{2}\right\rangle .$$
Choose a globally defined smooth section $\omega_{1}$ of $L$ such that
$$W^{+}\left(\omega_{1}\right)=\alpha \omega_{1}, \quad\left|\omega_{1}\right|^{2}=2 ;$$
our first step is to derive a pointwise identity, also appearing implicitly in [36] (see also [35]), using the weighted Weitzenböck formula (2.9).

Lemma 3.1. At every point of $M$, we have
$$\begin{aligned}
0= & \frac{1}{2}\left|\nabla \omega_{1}\right|^{2}-\frac{2}{\alpha} W^{+}\left(\nabla_{e} \omega_{1}, \nabla^{e} \omega_{1}\right) \\
& +\frac{3}{2}\left\langle\omega_{1},\left(d+d^{*}\right)^{2} \omega_{1}\right\rangle+2\left(\frac{2\left|W^{+}\right|^{2}}{\alpha}-3 \alpha\right) .
\end{aligned}$$
Proof. We claim that, at every $p \in M$,
$$\left\langle\nabla^{*} \nabla\left(f W^{+}\right), \omega_{1} \otimes \omega_{1}\right\rangle=2\left\langle\omega_{1}, \nabla^{*} \nabla \omega_{1}\right\rangle-\frac{2}{\alpha} W^{+}\left(\nabla_{e} \omega_{1}, \nabla^{e} \omega_{1}\right) .$$
We observe that, since $\left|\omega_{1}\right|$ is constant and $f W^{+}\left(\omega_{1}\right)=\omega_{1}$,
$$\nabla\left(f W^{+}\left(\omega_{1}, \omega_{1}\right)\right)=\nabla\left(\left\langle f W^{+}\left(\omega_{1}\right), \omega_{1}\right\rangle\right)=\nabla\left\langle f \alpha \omega_{1}, \omega_{1}\right\rangle=\nabla\left|\omega_{1}\right|^{2}=0 ;$$
now, recalling that $\nabla^{*} \nabla=-\nabla_{e} \nabla^{e}$, we use the standard formula for covariant derivatives, together with the fact that $f W^{+}$and $\nabla\left(f W^{+}\right)$are self-adjoint, to obtain
$$\begin{aligned}
\left\langle\nabla^{*} \nabla\left(f W^{+}\right), \omega_{1} \otimes \omega_{1}\right\rangle & =4\left\langle\nabla_{e}\left(f W^{+}\right)\left(\omega_{1}\right), \nabla^{e} \omega_{1}\right\rangle \\
& +2\left\langle f W^{+}\left(\nabla_{e} \omega_{1}\right), \nabla^{e} \omega_{1}\right\rangle-2\left\langle\omega_{1}, \nabla^{*} \nabla \omega_{1}\right\rangle .
\end{aligned}$$
We use again the fact that $f W^{+}\left(\omega_{1}\right)=\omega_{1}$ : if we differentiate this equation, we obtain
$$\nabla_{e} \omega_{1}=\nabla_{e}\left(f W^{+}\left(\omega_{1}\right)\right)=\nabla_{e}\left(f W^{+}\right)\left(\omega_{1}\right)+f W^{+}\left(\nabla_{e} \omega_{1}\right)$$
and, if we contract the previous identity with $\nabla^{e} \omega_{1}$, we get
$$\left\langle\nabla_{e}\left(f W^{+}\right)\left(\omega_{1}\right), \nabla^{e} \omega_{1}\right\rangle=\left|\nabla \omega_{1}\right|^{2}-\left\langle f W^{+}\left(\nabla_{e} \omega_{1}\right), \nabla^{e} \omega_{1}\right\rangle .$$
Furthermore, by the usual Bochner formula for smooth tensors,
$$0=\nabla^{*} \nabla\left|\omega_{1}\right|^{2}=2\left\langle\omega_{1}, \nabla^{*} \nabla \omega_{1}\right\rangle-2\left|\nabla \omega_{1}\right|^{2} \Longrightarrow\left|\nabla \omega_{1}\right|^{2}=\left\langle\omega_{1}, \nabla^{*} \nabla \omega_{1}\right\rangle .$$

Substituting these identities into (3.3) and using $f \alpha=1$ proves the claim. Contracting (2.9) with $\omega_{1} \otimes \omega_{1}$ and using again $f \alpha=1,\left|\omega_{1}\right|^{2}=2$, and (3.2), we obtain
$$\begin{aligned}
0 & =2\left\langle\omega_{1}, \nabla^{*} \nabla \omega_{1}\right\rangle-\frac{2}{\alpha} W^{+}\left(\nabla_{e} \omega_{1}, \nabla^{e} \omega_{1}\right)+s-12 \alpha+\frac{4}{\alpha}\left|W^{+}\right|^{2} \\
& =\frac{1}{2}\left|\nabla \omega_{1}\right|^{2}+\frac{3}{2}\left\langle\omega_{1}, \nabla^{*} \nabla \omega_{1}\right\rangle-\frac{2}{\alpha} W^{+}\left(\nabla_{e} \omega_{1}, \nabla^{e} \omega_{1}\right)+s-12 \alpha+\frac{4}{\alpha}\left|W^{+}\right|^{2} .
\end{aligned}$$
Finally, by the well-known Weitzenböck formula for self-dual two-forms (see e.g. [36, Equation (7)])
$$\left(d+d^{*}\right)^{2} \omega_{1}=\nabla^{*} \nabla \omega_{1}-2 W^{+}\left(\omega_{1}\right)+\frac{s}{3} \omega_{1},$$
substitution gives (3.1). \(\square\)

We now integrate (3.1) over $M$ : first, we point out that, since $* \omega_{1}=\omega_{1}$ and $d^{*} \omega_{1}=-* d * \omega_{1}$, using the properties of the Hodge operator we obtain
$$\int_{M}\left\langle\omega_{1},\left(d+d^{*}\right)^{2} \omega_{1}\right\rangle d \mu_{g}=2 \int_{M}\left|d \omega_{1}\right|^{2} d \mu_{g} .$$
Then, setting again
$$\rho=\frac{\beta}{\alpha}=\frac{\beta_{h}}{\alpha_{h}}$$
and using (3.1) and (3.4), together with the fact that $\left|W^{+}\right|^{2}=2 \alpha^{2}\left(1+\rho+\rho^{2}\right)$, we get the equality
$$\int_{M}\left[\mathcal{P}+8 \alpha\left(\rho+\frac{1}{2}\right)^{2}\right] d \mu_{g}=0$$
where
$$\mathcal{P}:=3\left|d \omega_{1}\right|^{2}+\frac{1}{2}\left|\nabla \omega_{1}\right|^{2}-\frac{2}{\alpha} W^{+}\left(\nabla_{e} \omega_{1}, \nabla^{e} \omega_{1}\right) .$$
The crucial new point is that the weighted Derdziński relation in Proposition 2.3 allows us to evaluate the indefinite gradient term $\mathcal{P}$ exactly, rather than estimate it. Let $M_{W} \subset M$ be the regular spectral set for $W^{+}$, equivalently for $\mathcal{W}^{+}=f W^{+}$. Since $\alpha>\beta$ and $\alpha>0$ by hypothesis, the discussion in Section 2 implies that $M_{W}$ is an open dense subset of $M$ and that Proposition 2.3 holds locally on the whole $M_{W}$.

Indeed, we can complete $\omega_{1}$ to the oriented orthogonal frame $\left\{\omega_{1}, \omega_{2}, \omega_{3}\right\}$ of $\Lambda^{+}$defined in (2.2) locally on $M_{W}$ : the covariant derivatives of the forms $\omega_{i}$ are then given by (2.3), which immediately implies that
$$\left|\nabla \omega_{1}\right|^{2}=2\left(|a|^{2}+|c|^{2}\right)$$
on $M_{W}$. A direct computation gives
$$\begin{aligned}
d \omega_{1} & =a \wedge \omega_{2}-c \wedge \omega_{3} \\
& =-\left(a_{2}+c_{1}\right) e^{123}+\left(-a_{1}+c_{2}\right) e^{124}+\left(a_{4}+c_{3}\right) e^{134}+\left(a_{3}-c_{4}\right) e^{234}
\end{aligned}$$
where $e^{i j k}=e^{i} \wedge e^{j} \wedge e^{k}$, which implies that
$$\left|d \omega_{1}\right|^{2}=\left(a_{1}-c_{2}\right)^{2}+\left(a_{2}+c_{1}\right)^{2}+\left(a_{3}-c_{4}\right)^{2}+\left(a_{4}+c_{3}\right)^{2} .$$
Finally, using the first equation in (2.3) again, we can compute
$$W^{+}\left(\nabla_{e} \omega_{1}, \nabla^{e} \omega_{1}\right)=2\left(\beta|a|^{2}+\gamma|c|^{2}\right) ;$$
by (2.5), locally on $M_{W}$ we have
$$\left\{\begin{array}{l}
\left|d \omega_{1}\right|^{2}=(1-k)^{2}|a|^{2}, \\
\left|\nabla \omega_{1}\right|^{2}=2\left(1+k^{2}\right)|a|^{2}, \\
W^{+}\left(\nabla_{e} \omega_{1}, \nabla^{e} \omega_{1}\right)=2 \alpha\left(\rho-(1+\rho) k^{2}\right)|a|^{2},
\end{array}\right.$$
where
$$k=\frac{1-\rho}{2+\rho} .$$
Now, we can express $\mathcal{P}$ using (3.7) as
$$\begin{aligned}
\mathcal{P} & =\left[3(1-k)^{2}+\left(1+k^{2}\right)-4\left(\rho-(1+\rho) k^{2}\right)\right]|a|^{2} \\
& =\left[4(1-\rho)-6 k+4(2+\rho) k^{2}\right]|a|^{2} \\
& =\frac{6(1-\rho)}{2+\rho}|a|^{2}
\end{aligned}$$
Moreover, (3.7) gives
$$\left|\nabla \omega_{1}\right|^{2}=2\left(1+k^{2}\right)|a|^{2}=\frac{2\left(2 \rho^{2}+2 \rho+5\right)}{(2+\rho)^{2}}|a|^{2},$$
and hence
$$\mathcal{P}=\mathcal{Q}_{\rho}\left|\nabla \omega_{1}\right|^{2}, \quad \mathcal{Q}_{\rho}:=\frac{3(1-\rho)(2+\rho)}{2 \rho^{2}+2 \rho+5} .$$
This identity holds on $M_{W}$.
By (3.6), $\mathcal{P}$ is smooth on $M$, since $\omega_{1}$ is a globally defined smooth eigenform. Moreover, $\rho$ is continuous on $M$, so $\mathcal{Q}_{\rho}\left|\nabla \omega_{1}\right|^{2}$ is globally defined and continuous. These two functions coincide on the open dense set $M_{W}$; therefore,
$$\mathcal{P}=\mathcal{Q}_{\rho}\left|\nabla \omega_{1}\right|^{2} \quad \text { on } M .$$
Consequently, (3.5) becomes
$$\int_{M}\left[\frac{3(1-\rho)(2+\rho)}{2 \rho^{2}+2 \rho+5}\left|\nabla \omega_{1}\right|^{2}+8 \alpha\left(\rho+\frac{1}{2}\right)^{2}\right] d \mu_{g}=0$$
Since $-\frac{1}{2} \leq \rho<1$, both terms in the integrand are nonnegative and hence vanish identically. Since $\alpha>0$ and $\rho<1$ on $M$, we conclude that
$$\nabla \omega_{1}=0, \quad \rho=-\frac{1}{2} \quad \text { on } M,$$
which means that $g$ is a Kähler metric on $M$ [16, Proposition 5], whose Kähler form is $\omega_{1}$ and whose self-dual Weyl operator $W^{+}$has eigenvalues given by (see [16, Proposition 2])
$$\alpha=\frac{s}{6}, \quad \beta=\gamma=-\frac{s}{12} .$$
Furthermore, since $\alpha>0$ on $M$, by (3.10) we obtain that $g$ is a Kähler metric with positive scalar curvature on $M$.

Conversely, let $(M, g, J)$ be a Kähler surface with $s_{g}>0$ and set $h=s_{g}^{-2} g$. By [16, Proposition 2], $s_{g}^{-1} W_{g}^{+}$is parallel, and hence $\delta_{g}\left(s_{g}^{-1} W_{g}^{+}\right)=0$. Then, (2.1) implies $\delta_{h} W_{h}^{+}=0$, while (3.10) gives $\alpha_{h}>0$ and $\alpha_{h}>\beta_{h}$. This concludes the proof of Theorem 1.2. \(\square\)

Proof of Corollary 1.3. The strict inequality rules out zeros of $W_{h}^{+}$. Hence $W_{h}^{+}$is nowhere zero and $\alpha_{h}>0,-1 / 2 \leq \rho \leq 1$, and $\gamma_{h}=-(1+\rho) \alpha_{h}$. Hence, we immediately obtain
$$\left|W_{h}^{+}\right|^{2}=2 \alpha_{h}^{2}\left(1+\rho+\rho^{2}\right), \quad \operatorname{det}\left(W_{h}^{+}\right)=-\rho(1+\rho) \alpha_{h}^{3},$$
which imply that
$$\frac{\operatorname{det}\left(W_{h}^{+}\right)}{\left|W_{h}^{+}\right|^{3}}=\mathcal{F}(\rho),$$
where
$$\mathcal{F}(\rho):=-\frac{\rho(1+\rho)}{2^{3 / 2}\left(1+\rho+\rho^{2}\right)^{3 / 2}} .$$
A direct computation gives
$$\mathcal{F}^{\prime}(\rho)=\frac{(\rho-1)(\rho+2)\left(\rho+\frac{1}{2}\right)}{2^{3 / 2}\left(1+\rho+\rho^{2}\right)^{5 / 2}} \leq 0 .$$
Thus, $\mathcal{F}$ is non-increasing on [-1/2, 1], and its minimum is attained at $\rho=1$, where
$$\mathcal{F}(1)=-\frac{1}{3 \sqrt{6}} .$$
Since $\mathcal{F}(\rho)>\mathcal{F}(1)$ by assumption, we have $\rho<1$ on $M$, and the conclusion follows from Theorem 1.2. \(\square\)

\section*{4. Compact Einstein manifolds}

The main aim of this section is to show how the method used to prove Theorem 1.2 can be adapted to Einstein four-manifolds, without the nonvanishing assumption on $W_{h}^{+}$. We prove that, if $W_{h}^{+}$is not identically zero and its eigenvalues satisfy
$$\beta_{h} \leq \rho_{0} \alpha_{h} \quad \text { on } M, \quad \rho_{0}<1,$$
then $W_{h}^{+} \neq 0$ at every point of $M$. The idea is to work on the set
$$X:=M \backslash N, \quad N:=\left\{W_{h}^{+}=0\right\}$$
and, by constructing suitable cutoff functions satisfying a zero-capacity condition, to prove that $g=\alpha_{h}^{2 / 3} h$ is Kähler on $X$. We then use Derdziński's rigidity result for the zero set of $W_{h}^{+}$on Einstein four-manifolds [16, Proposition 5(iv)].

We first work under the weaker assumption $\delta_{h} W_{h}^{+}=0$ : by (4.1), on $X$ we have that $\alpha_{h}>\beta_{h}$ and, therefore, $\alpha_{h}>0$, which means that, using again Proposition 2.3, we can do the same algebraic computations we performed at the end of the previous section in order to obtain that (3.1) and (3.8) hold on $X \cap M_{W}$ and, therefore, on $X$ (recall that $X \cap M_{W}$ is an open dense subset of $X$ ). Since $X$ is not a closed set, we have to modify our argument in order to use integration and obtain an analogue of (3.9). We begin with a general result for manifolds with harmonic self-dual Weyl curvature.

Proposition 4.1. Let $(M, h)$ be an oriented four-manifold, not necessarily complete, such that $\delta_{h} W_{h}^{+}=0$ and let
$$N=\left\{W_{h}^{+}=0\right\}, \quad X=M \backslash N .$$
Assume that $W_{h}^{+} \not \equiv 0$ and that, on $X$,
$$\beta_{h} \leq \rho_{0} \alpha_{h}, \quad \rho_{0}<1 .$$
Let $g=\alpha_{h}^{2 / 3} h$. Suppose that there exist cutoff functions $\chi_{j} \in \operatorname{Lip}_{c}(X)$, $0 \leq \chi_{j} \leq 1$, such that $\chi_{j} \rightarrow 1$ locally uniformly on $X$ and
$$\int_{X}\left|d \chi_{j}\right|_{g}^{2} d \mu_{g} \longrightarrow 0$$
Then, after at worst passing to a double cover of $X$, there exists a smooth eigenform $\omega_{1}$, normalized by $\left|\omega_{1}\right|_{g}^{2}=2$, such that
$$\nabla^{g} \omega_{1}=0, \quad \beta_{h}=\gamma_{h}=-\frac{1}{2} \alpha_{h} \quad \text { on } X$$
and $g$ is Kähler with positive scalar curvature on $X$.
Proof. Since $\delta_{h} W_{h}^{+}=0$, by (2.1) we have $\delta_{g}\left(\alpha_{h}^{-1 / 3} W_{g}^{+}\right)=0$ : hence, since $\rho$ is continuous on $X$, (3.1) and (3.8) hold on $X$. Let $\left.L \subset \Lambda^{+}\right|_{X}$ be the line subbundle associated with the eigenspace of $\alpha_{h}$. If $L$ is not orientable, we pass to its standard double cover; the capacity condition is unchanged up to the degree of the cover. Hence we may assume that $L$ is orientable and choose a smooth eigenform $\omega_{1}$ associated to $\alpha_{h}$ normalized by $\left|\omega_{1}\right|_{g}^{2}=2$. If the line subbundle $L$ associated to the eigenspace of $\alpha_{h}$ is not orientable, We recall that, since $\omega_{1}$ is self-dual,
$$d^{*}\left(\chi_{j}^{2} \omega_{1}\right)=-* d\left(\chi_{j}^{2} \omega_{1}\right)=\chi_{j}^{2} d^{*} \omega_{1}-2 \chi_{j} *\left(d \chi_{j} \wedge \omega_{1}\right)$$
almost everywhere on $X$. Hence, since $\left|d^{*} \omega_{1}\right|=\left|d \omega_{1}\right|$ and $\left|\omega_{1}\right|^{2}=2$, multiplying (3.1) by $\chi_{j}^{2}$ and integrating by parts we obtain
$$\begin{aligned}
\int_{X} \chi_{j}^{2}\left\langle\omega_{1},\left(d+d^{*}\right)^{2} \omega_{1}\right\rangle d \mu_{g}= & 2 \int_{X} \chi_{j}^{2}\left|d \omega_{1}\right|^{2} d \mu_{g} \\
& +4 \int_{X} \chi_{j}\left\langle d \chi_{j} \wedge \omega_{1}, d \omega_{1}\right\rangle d \mu_{g}
\end{aligned}$$
Using again $\left|\omega_{1}\right|^{2}=2$ and $\left|d \omega_{1}\right| \leq C\left|\nabla \omega_{1}\right|$, the Cauchy-Schwarz and Young inequalities give
$$\begin{aligned}
\left|\int_{X} \chi_{j}\left\langle d \chi_{j} \wedge \omega_{1}, d \omega_{1}\right\rangle d \mu_{g}\right| & \leq C \int_{X}\left|\chi_{j}\right|\left|d \chi_{j}\right|\left|\nabla \omega_{1}\right| d \mu_{g} \\
& \leq \varepsilon \int_{X} \chi_{j}^{2}\left|\nabla \omega_{1}\right|^{2} d \mu_{g}+C_{\varepsilon} \int_{X}\left|d \chi_{j}\right|^{2} d \mu_{g}
\end{aligned}$$
for every $\varepsilon>0$ and some $C_{\varepsilon}>0$.
Combining (3.1), (3.8), and (4.3), we obtain
$$0=\int_{X} \chi_{j}^{2}\left[\mathcal{Q}_{\rho}\left|\nabla \omega_{1}\right|^{2}+8 \alpha\left(\rho+\frac{1}{2}\right)^{2}\right] d \mu_{g}+6 \int_{X} \chi_{j}\left\langle d \chi_{j} \wedge \omega_{1}, d \omega_{1}\right\rangle d \mu_{g}$$
where $\mathcal{Q}_{\rho}$ is defined in (3.8): observe that, by the pinching assumption, since $\mathcal{Q}_{\rho}$ is continuous and positive on $\left[-1 / 2, \rho_{0}\right]$, there exists a constant $q_{0}>0$, depending only on $\rho_{0}$, such that
$$\mathcal{Q}_{\rho} \geq q_{0}>0 \quad \text { on } X .$$
Set
$$I_{j}:=\int_{X} \chi_{j}^{2}\left[\mathcal{Q}_{\rho}\left|\nabla \omega_{1}\right|^{2}+8 \alpha\left(\rho+\frac{1}{2}\right)^{2}\right] d \mu_{g} .$$
Using (4.4), (4.5) and (4.6), we get
$$I_{j} \leq 6 \varepsilon \int_{X} \chi_{j}^{2}\left|\nabla \omega_{1}\right|^{2} d \mu_{g}+6 C_{\varepsilon} \int_{X}\left|d \chi_{j}\right|^{2} d \mu_{g} \leq \frac{6 \varepsilon}{q_{0}} I_{j}+6 C_{\varepsilon} \int_{X}\left|d \chi_{j}\right|^{2} d \mu_{g}$$
Now, taking $\varepsilon>0$ small enough such that $6 \varepsilon / q_{0}<1$, we obtain
$$0 \leq I_{j} \leq C \int_{X}\left|d \chi_{j}\right|^{2} d \mu_{g}$$
for some $C>0$. By (4.2), $I_{j} \rightarrow 0$ and, since $\chi_{j} \rightarrow 1$ locally uniformly on $X$ and the integrand of $I_{j}$ is nonnegative, Fatou's lemma yields
$$0=\int_{X}\left[\mathcal{Q}_{\rho}\left|\nabla \omega_{1}\right|^{2}+8 \alpha\left(\rho+\frac{1}{2}\right)^{2}\right] d \mu_{g}$$
As in (3.9), both terms in the integrand vanish identically. Hence
$$\nabla^{g} \omega_{1}=0, \quad \beta_{h}=\gamma_{h}=-\frac{1}{2} \alpha_{h} \quad \text { on } X .$$
Thus $g$ is Kähler on $X$ with $s_{g}>0$, which concludes the proof. \(\square\)

Now, we are ready to prove our main result on compact Einstein fourmanifolds.

Proof of Theorem 1.4. We need to construct cutoff functions that satisfy the capacity hypothesis in Proposition 4.1 for the zero set of $W_{h}^{+}$.

If $N=\varnothing$, Proposition 4.1 applies with $\chi_{j} \equiv 1$ and shows that, after possibly passing to a double cover of $M, g=\alpha_{h}^{2 / 3} h$ is Kähler with positive scalar curvature.

Henceforth suppose that $N \neq \varnothing$. The construction of the cutoff functions relies on the fact that, under our hypotheses, the zero set of $W_{h}^{+}$cannot be too large. Since $(M, h)$ is Einstein, $W_{h}^{+}$satisfies the second Bianchi identity and it is divergence-free: in particular, since we are assuming that $W_{h}^{+} \not \equiv 0$, $W_{h}^{+}$is a non-trivial solution of the first-order elliptic system (see e.g. [49])
$$\mathcal{D} W_{h}^{+}=0,$$
where $\mathcal{D}:=d^{\nabla}+\delta^{\nabla}$ is the Hodge-Dirac operator on $\Lambda^{+}$-valued 2-forms (see also the discussion before Lemma 2.5). Thus, we can apply a result by Bär [4, Corollary 1] and conclude that $N$ is countably 2-rectifiable and has finite $\mathcal{H}_{h}^{2}$-measure: in particular, $N$ has codimension at least 2.

We now exploit the following consequence of the definition of Hausdorff measure. By compactness of $N$, for every $\delta>0$, there are finitely many geodesic balls $B_{h}\left(p_{i}, r_{i}\right), p_{i} \in N$, and $0<r_{i}<\delta$ such that
$$N \subset \bigcup_{i} B_{h}\left(p_{i}, r_{i}\right), \quad \sum_{i} r_{i}^{2} \leq C_{N},$$
where $C_{N}$ is independent of $\delta$. Indeed, finite Hausdorff measure implies uniformly bounded Hausdorff $\delta$-content for every $\delta>0$; see, for instance, [19, Section 2.1]. Since $W_{h}^{+}$is smooth and vanishes on $N, \alpha_{h}$ is a Lipschitz function in a neighborhood of $N$ : hence, for $x$ sufficiently close to $N$,
$$\alpha_{h}(x) \leq C d_{h}(x, N)$$
for some uniform constant $C>0$. In particular, choosing $\delta$ sufficiently small, on each ball $B_{h}\left(p_{i}, 2 r_{i}\right)$ we have
$$\alpha_{h} \leq C r_{i} .$$
For every Lipschitz function $\varphi$, one has
$$|d \varphi|_{g}^{2} d \mu_{g}=\alpha_{h}^{2 / 3}|d \varphi|_{h}^{2} d \mu_{h}$$
almost everywhere on $X$. We want to construct suitable cutoff functions, adapted to the chosen cover of $N$, in order to apply Proposition 4.1. We choose $0<\delta<\operatorname{inj}_{h}(M) / 2$ and, for every $i$, we can define $\theta_{i} \in C^{\infty}(M)$ such that
$$0 \leq \theta_{i} \leq 1, \quad \theta_{i}=0 \quad \text { on } B_{h}\left(p_{i}, r_{i}\right), \quad \theta_{i}=1 \quad \text { on } M \backslash B_{h}\left(p_{i}, 2 r_{i}\right),$$
with
$$\left|d \theta_{i}\right|_{h}^{2} \leq C r_{i}^{-2},$$
where $C$ is a constant independent of $\delta$. Since the functions $\theta_{i}$ are smooth, the function
$$\chi_{\delta}:=\min _{i} \theta_{i}$$
is Lipschitz on $M$. It vanishes on an open neighborhood of $N$, so its restriction belongs to $\operatorname{Lip}_{c}(X)$. Moreover,
$$0 \leq \chi_{\delta} \leq 1, \quad \chi_{\delta}=0 \quad \text { on } \bigcup_{i} B_{h}\left(p_{i}, r_{i}\right), \quad \chi_{\delta}=1 \quad \text { on } M \backslash \bigcup_{i} B_{h}\left(p_{i}, 2 r_{i}\right),$$
and
$$\left|d \chi_{\delta}\right|_{h}^{2} \leq C \sum_{i} r_{i}^{-2} \mathbf{1}_{B_{h}\left(p_{i}, 2 r_{i}\right)}$$
almost everywhere on $X$. Let $K \Subset X$. Since $\bigcup_{i} B_{h}\left(p_{i}, 2 r_{i}\right) \subset\left\{x: d_{h}(x, N)<\right.$ $2 \delta\}$, the set $K$ is disjoint from this union for all sufficiently small $\delta$. Therefore $\chi_{\delta} \rightarrow 1$ uniformly on $K$. Finally, we need to verify that
$$\int_{X}\left|d \chi_{\delta}\right|_{g}^{2} d \mu_{g} \longrightarrow 0 \quad \text { as } \delta \downarrow 0$$
After possibly decreasing $\delta$, we use the standard volume bound for small geodesic balls
$$\operatorname{Vol}_{h} B_{h}\left(p_{i}, 2 r_{i}\right) \leq C r_{i}^{4} ;$$
using (4.8), (4.9) and (4.10), we obtain
$$\begin{aligned}
\int_{X}\left|d \chi_{\delta}\right|_{g}^{2} d \mu_{g} & =\int_{X} \alpha_{h}^{2 / 3}\left|d \chi_{\delta}\right|_{h}^{2} d \mu_{h} \\
& \leq C \sum_{i} r_{i}^{2 / 3} r_{i}^{-2} \operatorname{Vol}_{h} B_{h}\left(p_{i}, 2 r_{i}\right) \leq C \sum_{i} r_{i}^{8 / 3} \\
& \leq C \delta^{2 / 3} \sum_{i} r_{i}^{2} \leq C \delta^{2 / 3}
\end{aligned}$$
which proves (4.11). Therefore, the cutoffs $\chi_{\delta}$ satisfy the capacity condition (4.2) and Proposition 4.1 applies. Thus, after at worst passing to a double cover of $X$,
$$\nabla^{g} \omega_{1}=0, \quad \beta_{h}=\gamma_{h}=-\frac{1}{2} \alpha_{h} \quad \text { on } X$$
and $g=\alpha_{h}^{2 / 3} h$ is a Kähler metric on $X$. Since $W_{h}^{+} \neq 0$ on $X$, the eigenvalues of $W_{g}^{+}$are
$$\alpha=\frac{s_{g}}{6}, \quad \beta=\gamma=-\frac{s_{g}}{12} .$$
Since $\alpha>0$ on $X$, it follows that $s_{g}>0$ on $X$. Now, since $W_{h}^{+}=0$ on $N$ and $\beta_{h}=\gamma_{h}$ on $X$, we have that $\# \operatorname{spec}\left(W_{h}^{+}\right)$, i.e. the number of distinct eigenvalues of $W_{h}^{+}$, is at most 2 on $M$. Therefore, by [16, Proposition 5(iv)] and the fact that $W_{h}^{+} \not \equiv 0$, we conclude that $W_{h}^{+}$is nowhere zero, contrary to $N \neq \varnothing$. Hence $N=\varnothing$, and, after at worst passing to a double cover of
$M, g$ is Kähler with positive scalar curvature on $M$. Since $h=\alpha_{h}^{-2 / 3} g$, the conformal transformation law for the scalar curvature gives
$$\operatorname{Vol}_{h}(M) s_{h}=\int_{M} s_{h} d \mu_{h}=\int_{M}\left(\frac{2}{3} \alpha_{h}^{-8 / 3}\left|\nabla \alpha_{h}\right|_{g}^{2}+s_{g} \alpha_{h}^{-2 / 3}\right) d \mu_{g}>0 .$$
Since $h$ is Einstein, $s_{h}$ is constant, and hence positive: thus $h$ is a Hermitian Einstein metric with positive scalar curvature, which concludes the proof. \(\square\)

Proof of Corollary 1.5. We follow the notation in the proof of Corollary 1.3. By assumption and the continuity and strict monotonicity of $\mathcal{F}$ on the relevant interval, there is a unique $\rho_{0}<1$ such that
$$\mathcal{F}(\rho) \geq-c=\mathcal{F}\left(\rho_{0}\right)$$
at every point where $W_{h}^{+} \neq 0$, where $c<\frac{1}{3 \sqrt{6}}$. Hence, by the monotonicity of $\mathcal{F}(\rho)$,
$$\rho \leq \rho_{0},$$
i.e.
$$\beta_{h} \leq \rho_{0} \alpha_{h}$$
on the set $\left\{W_{h}^{+} \neq 0\right\}$. Since, on the zero set of $W_{h}^{+}$, the same inequality is automatically true, the conclusion follows from Theorem 1.4. \(\square\)

Proof of Corollary 1.7. Suppose that
$$\sup _{\left\{W_{h}^{+} \neq 0\right\}} \frac{\beta_{h}}{\alpha_{h}}=\rho_{0}<1 .$$
Then $\beta_{h} \leq \rho_{0} \alpha_{h}$ on $\left\{W_{h}^{+} \neq 0\right\}$, and the same inequality holds trivially on the zero set. Since $W_{h}^{+} \not \equiv 0$, Theorem 1.4 implies that $h$ has positive scalar curvature, contradicting the hypothesis. \(\square\)

\section*{5. Kähler-Einstein surfaces}

We are now ready to prove Theorem 1.8. Let $(M, h, J)$ be a Kähler-Einstein surface with the orientation induced by $J$. At each $p \in M$, denote by $H$ the holomorphic sectional curvature, defined by
$$H(v)=h(R(v, J v) J v, v)$$
for every unit vector $v \in T_{p} M$. We denote its pointwise maximum and minimum by $H_{\text {max }}$ and $H_{\text {min }}$, respectively, and its Fubini-Study average over $\mathbb{C P}^{1}$ by $H_{\mathrm{av}}$. Following the notation of Siu and Yang [51], when $H_{\text {max }}>H_{\text {min }}$, we define the pinching ratio
$$\Theta=\frac{H_{\mathrm{av}}-H_{\min }}{H_{\max }-H_{\min }} .$$

It is well known that, with respect to the complex orientation, the tensor $W_{h}^{-}$of a Kähler-Einstein surface is precisely the Bochner tensor $B$; see, for instance, [9, 53, 55]. As in the previous sections, let
$$\alpha_{-} \geq \beta_{-} \geq \gamma_{-}$$
denote the eigenvalues of $W_{h}^{-}$, and define
$$\rho_{-}:=\frac{\beta_{-}}{\alpha_{-}}$$
at every point where $W_{h}^{-} \neq 0$. Let $\omega$ be the Kähler form, normalized by $|\omega|_{h}^{2}=2$. For every unit vector $v \in T_{p} M$, set
$$\sigma_{v}:=v^{b} \wedge(J v)^{b}, \quad \varphi_{v}:=\sqrt{2}\left(\sigma_{v}-\frac{1}{2} \omega\right) \in \Lambda_{p}^{-} .$$
Then $\left|\varphi_{v}\right|_{h}=1$, and the curvature-operator decomposition of the Kähler-Einstein metric $h$ gives
$$H(v)=\left\langle\mathcal{R}_{h}\left(\sigma_{v}\right), \sigma_{v}\right\rangle_{h}=\frac{s_{h}}{6}+\frac{1}{2}\left\langle W_{h}^{-}\left(\varphi_{v}\right), \varphi_{v}\right\rangle_{h} .$$
As $v$ varies over the unit tangent sphere, $\varphi_{v}$ ranges over the unit sphere in $\Lambda_{p}^{-}$. Consequently,
$$H_{\max }=\frac{s_{h}}{6}+\frac{\alpha_{-}}{2}, \quad H_{\min }=\frac{s_{h}}{6}+\frac{\gamma_{-}}{2} .$$
Furthermore, a well-known result due to Berger [5] implies that
$$H_{\mathrm{av}}=\frac{s_{h}}{6} .$$
Putting everything together, we can rewrite the pinching ratio $\Theta$ as
$$\Theta=\frac{-\gamma_{-}}{\alpha_{-}-\gamma_{-}}=\frac{1+\rho_{-}}{2+\rho_{-}} .$$
Since $-1 / 2 \leq \rho_{-} \leq 1$ and
$$\frac{d \Theta}{d \rho_{-}}=\frac{1}{\left(2+\rho_{-}\right)^{2}}>0,$$
we have
$$\frac{1}{3} \leq \Theta \leq \frac{2}{3} .$$
Moreover,
$$\Theta=\frac{2}{3} \quad \Longleftrightarrow \quad \rho_{-}=1 \quad \Longleftrightarrow \quad \alpha_{-}=\beta_{-} .$$
Proof of Theorem 1.8. Assume first that $W_{h}^{-} \not \equiv 0$ : since $\Theta \geq 1 / 3$, we immediately see that $1 / 3 \leq \theta<2 / 3$. Then, using the pinching hypothesis $\Theta \leq \theta$ together with (5.2), we obtain the uniform spectral gap
$$\frac{\beta_{-}}{\alpha_{-}} \leq \rho_{0}<1$$
on $\left\{W_{h}^{-} \neq 0\right\}$, where $\rho_{0}=(2 \theta-1) /(1-\theta)$. After reversing the orientation, $W_{h}^{-}$becomes $W_{h}^{+}$. The uniform bound above then contradicts Corollary 1.7 unless $W_{h}^{-}$vanishes identically in the original complex orientation. Hence $W_{h}^{-} \equiv 0$. If $h$ is Ricci-flat, it is therefore flat, and the Bieberbach theorem implies that $M$ is finitely covered by a flat complex torus. We may thus assume that $s_{h}<0$. For a Kähler-Einstein surface, $W_{h}^{-}=0$ is equivalent
to the vanishing of the Bochner tensor. A constant-scalar-curvature Kähler metric with vanishing Bochner tensor has constant holomorphic sectional curvature [43]. Consequently, the universal cover is the complex hyperbolic plane [30, Chapter IX], and $M$ is a compact quotient of the complex ball. \(\square\)

\section*{6. Noncompact Ricci-flat manifolds}

In this section, we show how to extend our results to noncompact Ricci-flat manifolds: in particular, under suitable volume growth and curvature decay assumptions, we show how to adapt the argument of Proposition 4.1.

Proof of Theorem 1.9. Again, we set
$$N=\left\{W_{h}^{+}=0\right\}, \quad X=M \backslash N .$$
As we observed in Section 4, the condition (1.2) implies that $\alpha_{h}>0$ and that it is simple on $X$ : hence, we need to verify the capacity condition in Proposition 4.1 for $g=\alpha_{h}^{2 / 3} h$. The restriction of the zero set of $W_{h}^{+}$to each ball $\overline{B_{h}\left(p_{0}, 2 R\right)}$ has finite $\mathcal{H}_{h}^{2}$-measure by Bär's Theorem [4]: hence, we can apply the same argument used in the proof of Theorem 1.4 in order to construct cutoff functions $\eta_{\delta, R}, 0 \leq \eta_{\delta, R} \leq 1$, which vanish near $N \cap \overline{B_{h}\left(p_{0}, 2 R\right)}$, are equal to 1 away from the zero set and satisfy
$$\int_{X}\left|d \eta_{\delta, R}\right|_{g}^{2} d \mu_{g} \leq C_{R} \delta^{2 / 3}$$
where $C_{R}$ is a constant independent of $\delta$. Moreover, for fixed $R, \eta_{\delta, R} \rightarrow 1$ locally uniformly on $B_{h}\left(p_{0}, 2 R\right) \cap X$ as $\delta \rightarrow 0$. Let $\psi_{R}$ be a Lipschitz radial cutoff function such that $\psi_{R}=1$ on $B_{h}\left(p_{0}, R\right), \psi_{R}=0$ on $M \backslash B_{h}\left(p_{0}, 2 R\right)$ and $\left|d \psi_{R}\right|_{h} \leq C R^{-1}$ almost everywhere. Since $h$ is Ricci-flat, $\mathrm{Rm}_{h}=W_{h}$, which implies that $\alpha_{h} \leq C\left|\operatorname{Rm}_{h}\right|$ : hence, we obtain
$$\begin{aligned}
\int_{X}\left|d \psi_{R}\right|_{g}^{2} d \mu_{g} & =\int_{B_{h}\left(p_{0}, 2 R\right) \backslash B_{h}\left(p_{0}, R\right)} \alpha_{h}^{2 / 3}\left|d \psi_{R}\right|_{h}^{2} d \mu_{h} \\
& \leq C R^{-2-2 q / 3} \operatorname{Vol}_{h}\left(B_{h}\left(p_{0}, 2 R\right)\right) \\
& \leq C R^{\nu-2-2 q / 3}=o(1)
\end{aligned}$$
as $R \rightarrow \infty$. We now define $\chi_{\delta, R}:=\eta_{\delta, R} \psi_{R}$ : by (6.1) and (6.2), we obtain
$$\int_{X}\left|d \chi_{\delta, R}\right|_{g}^{2} d \mu_{g} \leq C_{R} \delta^{2 / 3}+o_{R}(1)$$
where $o_{R}(1)$ denotes a quantity that goes to 0 as $R \rightarrow+\infty$. We choose a sequence of radii $R_{j}$ such that $R_{j} \rightarrow+\infty$ as $j \rightarrow+\infty$. Furthermore, we can find a sequence $\left\{\delta_{j}\right\}$ such that $\delta_{j}>0$ and
$$\delta_{j}<\frac{1}{R_{j}}, \quad C_{R_{j}} \delta_{j}^{2 / 3}<\frac{1}{R_{j}}$$
for every $j$. Setting $\chi_{j}:=\chi_{\delta_{j}, R_{j}} \in \operatorname{Lip}_{c}(X)$, we immediately see that $\chi_{j} \rightarrow 1$ locally uniformly in $X$ and
$$\int_{X}\left|d \chi_{j}\right|_{g}^{2} d \mu_{g} \longrightarrow 0$$
Therefore, Proposition 4.1 applies, and we can conclude that $g=\alpha_{h}^{2 / 3} h$ is a Kähler metric with positive scalar curvature on $X$. Thus, as in the proof of Theorem 1.4, we can use our assumption and [16, Proposition 5 (iv)] to deduce that $N=\varnothing$ : hence, after passing, if necessary, to the double cover, $g$ is a Kähler metric with positive scalar curvature on $M$. This implies that $h$ is a Ricci-flat Hermitian metric; however, $h$ is not a Kähler metric, since otherwise $W_{h}^{+}$would vanish identically [16, Proposition 2], and this concludes the proof. \(\square\)

Now, we want to adapt these results to the case of gravitational instantons: following [39], a gravitational instanton is a complete, connected, oriented, noncompact Ricci-flat four-manifold with quadratic curvature decay. Equivalently,
$$\int_{M}\left|\operatorname{Rm}_{h}\right|^{2} d \mu_{h}<\infty ;$$
see [39, Remark 2.3], where the equivalence is deduced using the $\varepsilon$-regularity theorem of Cheeger and Tian [12]. In our setting, we recall the three types of gravitational instantons, which can be distinguished by the spectral properties of $W_{h}^{+}$. Namely, we say that an oriented gravitational instanton is of
\begin{itemize}
\item[-] Type $I$ if $W_{h}^{+}=0$ (in this case, ( $M, h$ ) is locally hyperkähler);
\item[-] Type II if $W_{h}^{+}$has two distinct eigenvalues at every point;
\item[-] Type III if $W_{h}^{+}$has three distinct eigenvalues generically.
\end{itemize}

Every nonflat gravitational instanton has exactly one end: indeed, if it had at least two ends, the Cheeger-Gromoll splitting theorem would give an isometric product $\mathbb{R} \times N^{3}$, with $N$ compact, and Ricci-flatness would then force $N$ (and, therefore, $M$ ) to be flat.

If $(M, h)$ is globally hyperkähler and simply connected, the asymptotic classification theorem of Sun and Zhang [52] implies that its end is of ALE, ALF, ALG, ALH, ALG*, or ALH* type (see [39, Section 4] and [7, 13, 22, 23, 44]); the ALE cases were classified by Kronheimer [31, 32]. Under a noncollapsing volume assumption, Theorem 1.9 gives the following characterization of the Type II case.

Corollary 6.1. Let $(M, h)$ be an oriented gravitational instanton with Euclidean volume growth, i.e. such that, for some $v>0$ and some $p_{0} \in M$,
$$\operatorname{Vol}_{h}\left(B_{h}\left(p_{0}, R\right)\right) \geq v R^{4} \quad \text { for all } R \gg 1 .$$
Assume that $W_{h}^{+} \not \equiv 0$ and that, for some $\rho_{0}<1$,
$$\beta_{h} \leq \rho_{0} \alpha_{h} \quad \text { on } M .$$

Then $M$ has one ALE end, and, after at worst passing to a double cover of $M, h$ is conformal to a Kähler metric with positive scalar curvature. In particular, $h$ is a Hermitian Ricci-flat and non-Kähler gravitational instanton of Type II.

Proof. By the classical Bishop-Gromov volume estimate, we obtain that (1.3) holds with $\nu=4$. Since $h$ is Ricci-flat and $\left|\mathrm{Rm}_{h}\right| \in L^{2}$, the non-collapsing volume assumption allows us to apply the theorem of Bando, Kasue and Nakajima, which implies that the end has an ALE structure of order 4 [3]; in particular $\left|\mathrm{Rm}_{h}\right|=O\left(R^{-6}\right)$ on $M \backslash B_{h}\left(p_{0}, R\right)$. Thus (1.3) holds, and the conclusion follows from Theorem 1.9: the fact that $(M, h)$ is of Type II is an immediate consequence of (3.10). \(\square\)

Remark 6.2. In the noncollapsed ALE case, Corollary 6.1 can be combined with known classification results. If $W_{h}^{+}=0$, then, up to a quotient, $(M, h)$ is one of Kronheimer's Type I gravitational instantons [31, 32]. If $W_{h}^{+} \not \equiv 0$ and the group at infinity satisfies $\Gamma \subset \operatorname{SU}(2)$ in the chosen orientation, Li's classification [37, 38] implies that, up to homothety and isometry, $h$ is the Eguchi-Hanson metric on $T^{*} \mathbb{S}^{2}$ with the opposite orientation [18].

Li [37, 38] proved that collapsed Hermitian non-Kähler gravitational instantons are toric and of ALF or AF type. Combined with the classification of Biquard and Gauduchon [7], this gives the following list (see [39, Section 5] for a complete description):
\begin{itemize}
\item[-] Kerr metrics on $\mathbb{S}^{2} \times \mathbb{R}^{2}$, with respect to both orientations [21];
\item[-] Chen-Teo metrics on $\left(\mathbb{S}^{2} \times \mathbb{R}^{2}\right) \# \overline{\mathbb{C} \mathbb{P}^{2}}$, where $\overline{\mathbb{C} \mathbb{P}^{2}}$ is the complex projective space with the opposite orientation [15];
\item[-] Taub-bolt and anti-Taub-bolt metrics [46];
\item[-] Taub-NUT metric on $\mathbb{R}^{4}$ with the opposite orientation, called anti-Taub-NUT metric.
\end{itemize}
We recall that, with respect to the standard orientation of $\mathbb{R}^{4}$, the Taub-NUT metric is hyperkähler and hence is a Type I gravitational instanton. We now prove the following result.

Theorem 6.3. Let $(M, h)$ be an oriented gravitational instanton with at most cubic volume growth, i.e.
$$\operatorname{Vol}_{h}\left(B_{h}\left(p_{0}, R\right)\right)=O\left(R^{3}\right) .$$
Assume that $W_{h}^{+} \not \equiv 0$ and that, for some $\rho_{0}<1$,
$$\beta_{h} \leq \rho_{0} \alpha_{h} \quad \text { on } M .$$
Then, after at worst passing to a double cover of $M, h$ is conformal to a Kähler metric with positive scalar curvature. In particular, $h$ is a Hermitian Ricci-flat and non-Kähler gravitational instanton of Type II and belongs to one of the following families:
\begin{itemize}
\item[-] a Kerr metric, with either orientation;
\item[-] a Chen-Teo metric, with its Type II orientation;
\end{itemize}
\begin{itemize}
\item[-] the Taub-bolt metric, with either orientation (Taub-bolt or anti-Taubbolt);
\item[-] the reversed Taub-NUT metric.
\end{itemize}
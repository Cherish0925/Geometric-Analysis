---
retention_scope: session
part: 1
total_parts: 2
---

[Part 1/2 of: Connected sum construction for $σ_k$-Yamabe metrics]

---
source_file: 0910_5353.pdf
converter: mathpix
format: mmd
---

\title{
Connected sum construction for $\sigma_{k}$-Yamabe metrics
}

\author{
Giovanni CATINO ${ }^{a}$ and Lorenzo MAZZIERI ${ }^{a, b}$ \\ ${ }^{a}$ SISSA - International School for Advanced Studies \\ Via Beirut 2-4, I-34014 Trieste - Italy \\ ${ }^{b}$ Max-Planck-Institut für Gravitationsphysik, Albert-Einstein-Institut \\ Am Mühlenberg 1, D-14476 Golm - Germany
}

\begin{abstract}
In this paper we produce families of Riemannian metrics with positive constant $\sigma_{k}$-curvature equal to $2^{-k}\binom{n}{k}$ by performing the connected sum of two given compact non degenerate $n$-dimensional solutions $\left(M_{1}, g_{1}\right)$ and $\left(M_{2}, g_{2}\right)$ of the (positive) $\sigma_{k}$-Yamabe problem, provided $2 \leq 2 k<n$. The problem is equivalent to solve a second order fully nonlinear elliptic equation.
\end{abstract}

Key Words: $\sigma_{k}$-curvature, fully nonlinear elliptic equations, conformal geometry, connected sum
AMS subject classification: 53C24, 53C20, 53C21, 53C25

\section*{1 Introduction and statement of the result}

In recent years much attention has been given to the study of the Yamabe problem for $\sigma_{k}$-curvature, briefly the $\sigma_{k}$-Yamabe problem. To introduce the analytical formulation, we first recall some background materials from Riemmanian geometry. Given $(M, g)$, a compact Riemannian manifold of dimension $n \geq 3$, we denote respectively by Ric $_{g}, R_{g}$ the Ricci tensor and the scalar curvature of $(M, g)$. The Schouten tensor of $(M, g)$ is defined as follows
$$A_{g}:=\frac{1}{n-2}\left(\text { Ric }_{g}-\frac{1}{2(n-1)} R_{g} g\right) .$$
If we denote by $\lambda_{1}, \ldots, \lambda_{n}$ the eigenvalues of the symmetric endomorphism $g^{-1} A_{g}$, then the $\sigma_{k}$-curvature of $(M, g)$ is defined as the $k$-th symmetric elementary function of $\lambda_{1}, \ldots, \lambda_{n}$, namely
$$\sigma_{k}\left(g^{-1} A_{g}\right):=\sum_{i_{1}<\ldots<i_{k}} \lambda_{i_{i}} \cdot \ldots \cdot \lambda_{i_{k}} \quad \text { for } 1 \leq k \leq n \quad \text { and } \quad \sigma_{0}\left(g^{-1} A_{g}\right):=1 .$$
The $\sigma_{k}$-Yamabe problem on $(M, g)$ consists in finding metrics with constant $\sigma_{k}$-curvature in the same conformal class of $g$. The case $k=1$ is the well known Yamabe problem, whose progressive resolution is due to Yamabe [31], Trudinger [30], Aubin [1] and Schoen [26]. Before presenting the historical overview of the existence results for $k \geq 2$, we need to recall the following notions: a metric $g$ on $M$ is said to be $k$-admissible if it belongs to the $k$-th positive cone $\Gamma_{k}^{+}$, where
$$g \in \Gamma_{k}^{+} \quad \Longleftrightarrow \quad \sigma_{j}\left(g^{-1} A_{g}\right)>0 \quad \text { for } \quad j=1, \ldots, k .$$

\footnotetext{
${ }^{1}$ E-mail addresses: catino@sissa.it, mazzieri@sissa.it
}

Under the assumption that $g$ is $k$-admissible the $\sigma_{k}$-Yamabe problem has been solved in the case $k=2$, $n=4$ by Chang, Gursky and Yang [4] [5], for locally conformally flat manifolds by Li and Li [18] (see also Guan and Wang [10]), and for $2 k>n$ by Gursky and Viaclovsky [12]. For $2 \leq 2 k \leq n$ the problem has been solved by Sheng, Trudinger and Wang [29] under the extra-hypothesis that the operator is variational. We point out that for $k=1,2$ this hypothesis is always fulfilled, whereas for $k \geq 3$ it has been shown in [2] that this extra assumption is equivalent to the locally conformally flatness. Hence, the (positive) $\sigma_{k}$-Yamabe problem still remain open for $3 \leq k \leq n / 2$ with $(M, g)$ non locally conformally flat. In this optic, our result may eventually be used to produce families of new solutions to this problem showing that it is topologically unobstructed also in the remaining cases. At the end of this section we will give a simple example which will show how to use the connected sum construction to produce a metric in $\Gamma_{3}^{+}$with constant $\sigma_{3}$-curvature on $\left(\mathbb{S}^{6} \times \mathbb{T}^{2}\right) \sharp\left(\mathbb{S}^{6} \times \mathbb{T}^{2}\right)$, which is non locally conformally flat.

To put in perspective our work we briefly recall some results which can be found in literature for connected sum and generalized connected sum of positive scalar curvature metrics, metrics with constant scalar curvature and metrics in the positive cone $\Gamma_{k}^{+}$. To fix the notations we recall that the connected sum of two $n$-dimensional Riemannian manifolds $\left(M_{1}, g_{1}\right)$ and $\left(M_{2}, g_{2}\right)$ is the topological operation which consists in removing an open ball from both $M_{1}$ and $M_{2}$ and identifying the leftover boundaries, obtaining a new manifold with possibly different topology. Formally, if $p_{i} \in M_{i}$ and for a small enough $\varepsilon>0$ we excise the ball $B\left(p_{i}, \varepsilon\right)$ from $M_{i}, i=1,2$, the (pointwise) connected sum $M_{\varepsilon}$ of $M_{1}$ and $M_{2}$ along $p_{1}$ and $p_{2}$ with necksize $\varepsilon$ is the topological manifold defined as
$$M_{\varepsilon}:=M_{1} \sharp_{\varepsilon} M_{2}=\left[M_{1} \backslash B\left(p_{1}, \varepsilon\right) \cup M_{2} \backslash B\left(p_{2}, \varepsilon\right)\right] / \sim,$$
where ~ denotes the identification of the two boundaries $\partial B\left(p_{i}, \varepsilon\right), i=1,2$. Of course the new manifold $M_{\varepsilon}$ can be endowed with both a differentiable structure and a metric structure, as it will be explicitly done in Section 3. Even though from a topological point of view the value of the necksize is forgettable, it will be important to keep track of it when we will deal with the metric structure. The generalized connected sum (or fiber sum) is the same operation where instead of removing tubular neighborhoods of points (i.e., balls), one excises the tubular neighborhood of a submanifold which is embedded in both $M_{1}$ and $M_{2}$.

The first issue concerning the interaction between generalized connected sum and the scalar curvature is due to Gromov and Lawson [7] and Schoen and Yau [28]. They proved that the generalized connected sum of manifolds with positive scalar curvature metrics performed along submanifolds of codimension at least 3 can be endowed with a new metric whose scalar curvature is still positive. Later this construction has been extended to the pointwise connected sum of manifolds carrying $k$-admissible metrics by Guan-Lin-Wang [8], under the assumption $2 \leq 2 k<n$. As a byproduct of our construction we will be able to reproduce this result, with the additional properties that our metrics have constant $\sigma_{k}$-curvature and can be chosen as close as desired to the initial metrics $g_{1}$ and $g_{2}$. In this sense they may represent a canonical choice among all the possible $k$-admissible metrics on the connected sum manifold.

Concerning the solvability of the Yamabe equation $(k=1)$ on the pointwise connected sum of manifolds with constant scalar curvature, we mention the results of Joyce [14] for the compact case and Mazzeo, Pollack and Uhlenbeck [21] for the non compact case. The generalized connected sum has been treated by the second author in [22] and [23]. Most part of the geometric features of these issues are common to our construction. The main differences come from the analytical nature of the problem. In fact for $k=1$ the equation of interest is a second order semilinear elliptic equation, whereas for $k \geq 2$ the equation becomes fully nonlinear and in general it is not elliptic. To guarantee the ellipticity one has to assume that the (background) metric lies either in the $k$-th positive or in the $k$-th negative cone (for a definition of the $k$-th negative cone $\Gamma_{k}^{-}$see for example [11]). Here we just focus on the positive cone case, which for several reasons seems to be the most natural one. In fact the general treatment of the $\sigma_{k}$-Yamabe problem seems still far to be understood in the negative cone.

Before giving the precise statement of our result, we set up the problem and briefly describe the strategy of the proof. Since the aim of our work is to produce metrics with constant positive $\sigma_{k}$-curvature, it is
natural to normalize the constant to be the same as the one of the standard sphere, which is $2^{-k}\binom{n}{k}$. Hence, we will end up with a family of metrics $\left\{\widetilde{g}_{\varepsilon}\right\}_{\varepsilon}$ parametrized in terms of the necksize which satisfy
$$\sigma_{k}\left(\widetilde{g}_{\varepsilon}^{-1} A_{\widetilde{g}_{\varepsilon}}\right)=2^{-k}\binom{n}{k} .$$
To show the existence of these solutions we start by writing down (see Section 3) an explicit family of approximate solution metrics $\left\{g_{\varepsilon}\right\}_{\varepsilon}$ (still parametrized by the necksize) on $M_{\varepsilon}$. This metrics coincide with $g_{i}$ on $M_{i} \backslash B\left(p_{i}, \varepsilon\right), i=1,2$, and are close to a model metric on the remaining piece of the connected sum manifold, which in the following will be referred as neck region. The metric which we are going to use as a model in the neck region is described in Section 2. Since it is a complete metric on $\mathbb{R} \times \mathbb{S}^{n-1}$ with zero $\sigma_{k}$-curvature, it yields a natural generalization of the scalar flat Schwarzschild metric. For these reasons we have decided to label it as $\sigma_{k}$-Schwarzschild metric. The heuristic motivation for choosing this model comes from the fact that for $k=1$ it has been successfully employed in the analogous connected sum constructions for consant scalar curvature metrics, and on the other hand it represents the intrinsic counterpart of the catenoidal neck used in the famous gluing constructions of Kapouleas for constant mean curvature surfaces [15] [16].

The next step in our strategy amounts to look for a suitable correction of the approximate solutions to the desired exact solutions. This will be done by means of a conformal perturbation. At the end it will turn out that for sufficiently small values of the parameter $\varepsilon$ such a correction can actually be found together with a very precise control on its size and this will ensure the smooth convergence of the new solutions $\tilde{g}_{\varepsilon}$ to the former metrics $g_{i}$ on the compact subsets of $M_{i} \backslash\left\{p_{i}\right\}, i=1,2$.

Having this picture in mind, we pass now to fix the notations that will be used throughout this paper in order to exploit the conformal perturbative program mentioned above and explained in details in the last part of Section 3. Let $(M, \bar{g})$ be a compact smooth $n$-dimensional Riemannian manifold without boundary an let $2 \leq 2 k<n$. Taking advantage of this second assumption, we introduce the following formalism for the conformal change
$$\bar{g}_{u}:=u^{\frac{4 k}{n-2 k}} \bar{g},$$
where the conformal factor $u>0$ is a positive smooth function. In this context $\bar{g}$ will be referred as the background metric. At a first time the $\sigma_{k}$-equation for the conformal factor $u$ can be formulated as
$$\sigma_{k}\left(\bar{g}_{u}^{-1} A_{\bar{g}_{u}}\right)=2^{-k}\binom{n}{k} .$$
We recall that the Schouten tensor of $\bar{g}_{u}$ is related to the one of $A_{\bar{g}}$ by the conformal transformation law
$$A_{\bar{g}_{u}}=A_{\bar{g}}-\frac{2 k}{n-2 k} u^{-1} \nabla^{2} u+\frac{2 k n}{(n-2 k)^{2}} u^{-2} d u \otimes d u-\frac{2 k^{2}}{(n-2 k)^{2}} u^{-2}|d u|^{2} \bar{g},$$
where $\nabla^{2}$ and $|\cdot|$ are computed with respect to the background metric $\bar{g}$. For technical reasons, it is convenient to set
$$B_{\bar{g}_{u}}:=\frac{n-2 k}{2 k} u^{\frac{2 n}{n-2 k}} \bar{g}_{u}^{-1} \cdot A_{\bar{g}_{u}}$$
and to reformulate the $\sigma_{k}$-equation as
$$\mathcal{N}_{\bar{g}}(u):=\sigma_{k}\left(B_{\bar{g}_{u}}\right)-\binom{n}{k}\left(\frac{n-2 k}{4 k}\right)^{k} u^{\frac{2 k n}{n-2 k}}=0 .$$
We notice that if two metrics $\bar{g}$ and $g$ are related by $\bar{g}=(v / u)^{4 k /(n-2 k)} g$, then the nonlinear operator enjoys the following conformal equivariance property
$$\mathcal{N}_{\bar{g}}(u)=(v / u)^{-\frac{2 k n}{n-2 k}} \mathcal{N}_{g}(v) .$$
The linearized operator of $\mathcal{N}_{\bar{g}}$ about $u$ is defined as
$$\mathbb{L}_{\bar{g}}(u)[w]:=\left.\frac{d}{d s}\right|_{s=0} \mathcal{N}_{\bar{g}}(u+s w) .$$

This last quantity will play a crucial role in our approach. In fact, as explained in Sections 3 and 4, most part of the analysis in this paper is concerned with the study of the mapping properties of the linearized operator about the approximate solutions $g_{\varepsilon}$ 's, that we will write in the form $u_{\varepsilon}^{4 k /(n-2 k)} \bar{g}$. Here the key point is to provide the linearized operator $\mathbb{L}_{\bar{g}}\left(u_{\varepsilon}\right)[\cdot]$ with invertibility and a priori estimates which are uniform with respect to the parameter $\varepsilon$. In fact, if we have this and if the error term $\mathcal{N}_{\bar{g}}\left(u_{\varepsilon}\right)$ (which measures the failure of the approximate solutions to be exact solutions) becomes smaller and smaller as $\varepsilon \rightarrow 0$, we will be in the position to perform a Newton iteration scheme based on the implicit function theorem, which will finally provide us with a correction $w$ satisfying $\mathcal{N}_{\bar{g}}\left(u_{\varepsilon}+w\right)=0$. The exact solutions will then be recovered as $\widetilde{g}_{\varepsilon}=\left(u_{\varepsilon}+w\right)^{4 k /(n-2 k)} \bar{g}$. In order to be able to exploit the linear program (invertibility, a priori estimates, etc.), it is natural to ask the linearized operators about the initial metrics to be somehow non degenerate. The concept of non degeneracy that we need is made precise in the following

Definition 1.1. Let $2 \leq 2 k<n$ and suppose that the Riemannan manifold $(M, g)$ is a compact $n$ -dimensional and $k$-admissible solution to the (positive) $\sigma_{k}$-Yamabe problem, in the sense that
$$g \in \Gamma_{k}^{+} \quad \text { and } \quad \mathcal{N}_{g}(1)=0 \quad \text { in } M .$$
Then $(M, g)$ (as well as the metric $g$ ) is said to be non degenerate if
$$\mathbb{L}_{g}(1)[w]=0 \quad \text { in } \quad M \quad \Longrightarrow \quad w \equiv 0,$$
where $\mathbb{L}_{g}(1)[\cdot]$ is the linearized operator about the metric $g$.
Our main result reads:
Theorem 1. Let $\left(M_{1}, g_{1}\right)$ and $\left(M_{2}, g_{2}\right)$ be two compact $n$-dimensional $k$-admissible non degenerate solutions to the positive $\sigma_{k}$-Yamabe problem, with $2 \leq 2 k<n$. Then there exists a positive real number $\varepsilon_{0}>0$ only depending on $n, k$, and the $C^{2}$-norm of the coefficients of $g_{1}$ and $g_{2}$ such that, for every $\varepsilon \in\left(0, \varepsilon_{0}\right]$, the connected sum $M_{\varepsilon}=M_{1} \sharp_{\varepsilon} M_{2}$ can be endowed with a $k$-admissible non degenerate metric $\widetilde{g}_{\varepsilon}$ with constant $\sigma_{k}$-curvature equal to $2^{-k}\binom{n}{k}$. Moreover $\left\|\widetilde{g}_{\varepsilon}-g_{i}\right\|_{C^{r}\left(K_{i}\right)} \rightarrow 0$ for any $r>0$ and any compact set $K_{i} \subset M_{i} \backslash\left\{p_{i}\right\}$, the $p_{i}$ 's, $i=1,2$, being the points about which the connect sum is performed.

We want to point out that the restriction on $k$ in terms of the dimension $n$ perfectly agrees with the hypothesis needed by Guan, Lin and Wang [8] to prove their gluing result for $k$-admissible metrics. Moreover, the condition $2 \leq 2 k<n$ turns out to be optimal. In fact we will show in Section 6 that $\mathbb{R P}^{3}$ and $\mathbb{R P}^{4}$ with their standard metrics are non degenerate and 2-admissible but both the connected sums $\mathbb{R} \mathbb{P}^{3} \sharp \mathbb{R} \mathbb{P}^{3}$ and $\mathbb{R} \mathbb{P}^{4} \sharp \mathbb{R} \mathbb{P}^{4}$ do not admit any 2-admissible metric.

Some comments are due concerning the non degeneracy condition introduced in Definition 1.1. On one hand this kind of hypothesis is common to all the gluing results based on the implicit function theorem and the perturbative approach (such as the previously mentioned works [14], [21], [22] and [23]) for the reasons explained above. On the other hand it must be pointed out that this condition is not fulfilled by the standard sphere $\mathbb{S}^{n}$, since its linearized operator is given by
$$\mathbb{L}_{\mathbb{S}^{n}}(1)[\cdot]=-\binom{n-1}{k-1}\left(\frac{n-2 k}{4 k}\right)^{k-1}\left[\Delta_{\mathbb{S}^{n}}+n\right][\cdot] .$$
This fact will prevent us from using Theorem 1 to attach a sphere to another given solution of the $\sigma_{k}-$Yamabe problem. However, it is clear that this gluing is not relevant from a topological point of view. A more interesting observation is that, for $k=1$, sequences of spheres can actually be glued together via Schwarzschild-type necks, in order to obtain complete non compact (briefly singular) solutions to the Yamabe problem with isolated singularities on $\mathbb{S}^{n}$, as it has been done in [27]. For $2 \leq 2 k<n$ the second author proved in a joint work with Ndiaye [24] the existence of complete non compact and conformal metrics with constant $\sigma_{k}$-curvature on $\mathbb{S}^{n} \backslash \Lambda$ where $\Lambda$ is given by a finite number of points with a symmetric disposition. In this case (as well as in [20] which is an alternative construction in the case $k=1$ ) the metrics on the complete ends of the manifold are perturbations of $\sigma_{k}$-Delaunay metrics
(for a definition see [24]). The $\sigma_{k}$-Delaunay metrics, on the other hand, are periodic metrics on the cylinder $\mathbb{R} \times \mathbb{S}^{n-1}$ with positive constant $\sigma_{k}$-curvature, which in an appropriate limit become closer and closer to a sequence of standard $n$-dimensional spheres joined together by means of (infinitely many) $\sigma_{k}$-Schwarzschild necks. In this sense all the mentioned constructions for the singular problem ([27], [20] and [24]) are consistent. To conclude this remark about the non compact situation, we recall that for $k=1$ another construction is available and it is the one performed in [21]. The solutions provided in this work are the so called dipole metrics, which in other words are connected sum of cylinders $\mathbb{R} \times \mathbb{S}^{n-1}$ endowed with $\sigma_{1}$-Delunay metrics. In a forthcoming paper [3] we extend this result to $2 \leq 2 k<n$ by taking advantage of the connected sum techniques developed in this article.

Before proceeding with the rest of the paper, we would like to illustrate with an easy example how Theorem 1 may provide the existence of a nontrivial $k$-admissible metric with constant $\sigma_{k}$-curvature in one of the cases not covered by the present literature.

Example: $n=8, k=3$. Let $\left(M_{i}, g_{i}\right)=\left(\mathbb{S}^{6} \times \mathbb{T}^{2}, g:=g_{\mathbb{S}^{6}}+g_{\mathbb{T}^{2}}\right), i=1,2$. Clearly this metric is not locally conformally flat and belongs to the 3 positive cone $\Gamma_{3}^{+}$, since
$$\sigma_{1}\left(g^{-1} A_{g}\right)=\left(\frac{5}{42}\right) 18, \quad \sigma_{2}\left(g^{-1} A_{g}\right)=\left(\frac{5}{42}\right)^{2} 105, \quad \sigma_{3}\left(g^{-1} A_{g}\right)=\left(\frac{5}{42}\right)^{3} 56 .$$
We verify now that $\left(\mathbb{S}^{6} \times \mathbb{T}^{2}, g\right)$ is non degenearate in the sense of Definition 1.1. Let us assume that $v$ satisfies $\mathbb{L}_{g}(1)[v]=0$. A direct computation shows that this is equivalent to
$$\left[-\Delta_{\mathbb{T}^{2}}-\frac{7}{24} \Delta_{\mathbb{S}^{6}}-\frac{25}{126}\right] v=0 .$$
Using separation of variables, we have the following expansion for $v$
$$v=\sum_{j=0}^{+\infty} v^{j}(x) \phi_{j}(\theta),$$
where $x \in \mathbb{T}^{2}, \theta \in \mathbb{S}^{6}$ and $\phi_{j}$ are the eigenfunctions of $\Delta_{\mathbb{S}^{6}}$ satisfying $-\Delta_{\mathbb{S}_{6}} \phi_{j}=\lambda_{j} \phi_{j}$ for every $j \in \mathbb{N}$. Hence, we have
$$-\Delta_{\mathbb{T}^{2}} v^{j}=\left[\frac{25}{126}-\frac{7}{24} \lambda_{j}\right] v^{j}, \quad j \in \mathbb{N} .$$
Recalling that $\operatorname{spec}\left(\mathbb{S}^{6}\right)=\{i(i+5): i \in \mathbb{N}\}$, we have $\lambda_{j} \geq 6$ for $j \geq 1$, which clearly implies $v^{j} \equiv 0$ for $j \geq 1$. On the other hand, for $j=0$ we have
$$-\Delta_{\mathbb{T}^{2}} v^{0}=\frac{25}{126} v^{0},$$
but it is well known that the spectrum of the standard flat torus $\mathbb{T}^{2}$ is given by $\operatorname{spec}\left(\mathbb{T}^{2}\right)=\left\{4 \pi^{2} i: i \in \mathbb{N}\right\}$. This implies $v^{0} \equiv 0$ and thus the non degeneracy of $\left(\mathbb{S}^{6} \times \mathbb{T}^{2}, g\right)$ is proven. Theorem 1 can now by applied to produce on $\left(\mathbb{S}^{6} \times \mathbb{T}^{2}\right) \sharp\left(\mathbb{S}^{6} \times \mathbb{T}^{2}\right)$ a family of constant $\sigma_{3}$-curvature metrics lying in $\Gamma_{3}^{+}$. Moreover, since these metrics are obtained via conformal perturbation of approximate solutions which agree with $g_{i}$ on $M_{i} \backslash B\left(p_{i}, 1\right)$, we conclude that the $\sigma_{3}$-Yamabe metrics produced on $\left(\mathbb{S}^{6} \times \mathbb{T}^{2}\right) \sharp\left(\mathbb{S}^{6} \times \mathbb{T}^{2}\right)$ are not locally conformally flat.

The plan of the paper is the following: in Section 2 we define the $\sigma_{k}$-Schwarzschild metric. In Section 3 we construct the approximate solution metrics $\left\{g_{\varepsilon}\right\}_{\varepsilon}$ on the connected sum $M_{\varepsilon}$. In Section 4 we provide existence, uniqueness and $\varepsilon-a$ priori estimates for solutions to the linearized problem. In Section 5 we deal with the nonlinear analysis and we will conclude the proof of Theorem 1 by means of a Newton iteration scheme. Finally, in Section 6 we will illustrate with two counterexamples the geometric obstruction which prevent the extension of our gluing theorem to the case $2 k \geq n$.

Acknowledgments. This project started when the second author was a post-doc at the Max-Planck-Institut für Gravitationsphysik. The authors are partially supported by the Italian project FIRB-IDEAS "Analysis and Beyond".

\section*{$2 \sigma_{k}$-Schwarzschild metric on $\mathbb{R} \times \mathbb{S}^{n-1}$}

As anticipated in the introduction, the first step in our strategy amounts to build approximate solutions on the connected sum of $\left(M_{1}, g_{1}\right)$ and $\left(M_{2}, g_{2}\right)$. To do that we need to change the metric in a neighborhood of the points that we are going to excise, obtaining a new metric in the so called neck region. In the scalar curvature case a clever choice turns out to be the Schwarzschild metric. This is a complete scalar flat metric conformal to the cylindrical metric $g_{\text {cyl }}$ on $\mathbb{R} \times \mathbb{S}^{n-1}$. The explicit formula is given by
$$g:=\cosh \left(\frac{n-2}{2} t\right)^{\frac{4}{n-2}} g_{\text {cyl }} .$$
In a similar way, it is easy to construct a complete conformal metric on $\mathbb{R} \times \mathbb{S}^{n-1}$ with zero $\sigma_{k}$-curvature, for all $2 \leq 2 k<n$. Namely
Proposition 2.1. Let $g_{v}$ be a metric on $\mathbb{R} \times \mathbb{S}^{n-1}$ defined by $g_{v}=v^{4 k /(n-2 k)} g_{\text {cyl }}, v$ being a positive smooth function depending only on $t \in \mathbb{R}$. Let us define the quantity
$$h(t):=v^{2}(t)-\left(\frac{2 k}{n-2 k}\right)^{2} \dot{v}^{2}(t) .$$
Then, if $h_{0}:=h(0)>0$, the family of positive solutions $v=v(t)$ to the equation
$$\sigma_{k}\left(B_{g_{v}}\right)=0 \quad \text { in } \mathbb{R} \times \mathbb{S}^{n-1}$$
is given by $v(t)=\sqrt{h_{0}} \cosh \left(\frac{n-2 k}{2 k} t-c\right), c \in \mathbb{R}$.
Remark 2.2. We will refer to the metric defined by
$$g_{\Sigma}:=v_{\Sigma}^{\frac{4 k}{n-2 k}} g_{c y l},$$
with $v_{\Sigma}:=\cosh \left(\frac{n-2 k}{2 k} t\right)$, as the $\sigma_{k}$-Schwarzschild metric.
Remark 2.3. We notice that the family of solutions $v^{4 k /(n-2 k)} g_{\text {cyl }}$ on $\mathbb{R} \times \mathbb{S}^{n-1}$ obtained in the proposition above give rise to a family of complete conformal radial metrics $u(|x|)^{4 k /(n-2 k)} g_{\mathbb{R}^{n}}$ on $\mathbb{R}^{n} \backslash\{0\}$ with zero $\sigma_{k}$-curvature via the correspondence $u(|x|)=|x|^{-(n-2 k) / 2 k} v(-\log |x|)$.
Proof. For convenience the cylindrical metric $g_{\text {cyl }}$ will also be denoted by $d t^{2}+d \theta^{2}$, where $d \theta^{2}$ is the standard metric on $\mathbb{S}^{n-1}$. Moreover let us denote by $A_{\text {cyl }}$ the Schouten tensor of the cylindrical metric. We have for $A_{g_{v}}$.
$$A_{g_{v}}=A_{c y l}-\frac{2 k}{n-2 k} v^{-1} \nabla^{2} v+\frac{2 k n}{(n-2 k)^{2}} v^{-2} d v \otimes d v-\frac{2 k^{2}}{(n-2 k)^{2}} v^{-2}|d v|^{2} g_{c y l},$$
where $\nabla^{2}$ and $|\cdot|$ are computed with respect to $g_{\text {cyl }}$. Since the Schouten tensor of the cylindrical metric is explicitly given by
$$A_{\text {cyl }}=-\frac{1}{2} d t^{2}+\frac{1}{2} d \theta^{2} .$$
From (1.2) we get
$$\begin{aligned}
\left(B_{g_{v}}\right)_{t}^{t} & =-\frac{n-2 k}{4 k} v^{2}-v \ddot{v}+\frac{n-k}{n-2 k} \dot{v}^{2}=-\frac{n-2 k}{4 k}\left(\frac{n-k}{k}\right) h+v\left[\left(\frac{n-2 k}{2 k}\right)^{2} v-\ddot{v}\right] \\
\left(B_{g_{v}}\right)_{j}^{i} & =\left(\frac{n-2 k}{4 k} v^{2}-\frac{k}{n-2 k} \dot{v}^{2}\right) \delta_{j}^{i}=\frac{n-2 k}{4 k} h \delta_{j}^{i} \\
\left(B_{g_{v}}\right)_{j}^{t} & =0=\left(B_{g_{v}}\right)_{t}^{i},
\end{aligned}$$
for $1 \leq i, j \leq n-1$. A straightforward computation yields
$$\sigma_{k}\left(B_{g_{v}}\right)=\binom{n-1}{k-1}\left(\frac{n-2 k}{4 k} h\right)^{k-1} v\left[\left(\frac{n-2 k}{2 k}\right)^{2} v-\ddot{v}\right] .$$
Since $h_{0}:=h(0)>0$ and $v>0$, by continuity, the zero $\sigma_{k}$-curvature equation is equivalent to
$$\ddot{v}(t)=\left(\frac{n-2 k}{2 k}\right)^{2} v(t) \quad \text { in } \mathbb{R}$$
and $h(t)=h_{0}$ for all $t \in \mathbb{R}$. The statement follows at once. \(\square\)

Since in the following we will need to study the mapping properties of the linearized operator about (a (scaled version of) the $\sigma_{k}$-Schwarzschild metric, we consider the conformal perturbation,
$$s \longmapsto g_{s}:=\left(v_{\Sigma}+s w\right)^{\frac{4 k}{n-2 k}} g_{c y l},$$
for $s \in \mathbb{R}$ and $w \in \mathcal{C}^{\infty}\left(\mathbb{R} \times \mathbb{S}^{n-1}\right)$. Obviously $g_{0}=g_{\Sigma}$. Let now $A_{s}$ be the Schouten tensor of the metric $g_{s}$, and let $B_{s}$ be the symmetric $(1,1)$-tensor defined by
$$B_{s}:=\frac{n-2 k}{2 k}\left(v_{\Sigma}+s w\right)^{\frac{2 n}{n-2 k}} g_{s}^{-1} \cdot A_{s} .$$
Notice that $A_{0}=A_{g_{\Sigma}}$ and $B_{0}=B_{g_{\Sigma}}$.
Even thought our main purpose is to solve the equation (1.3), it will be useful to understand the features of the linear operator given by
$$\mathbb{L}_{c y l}^{0}\left(v_{\Sigma}\right)[w]:=\left.\frac{d}{d s}\right|_{s=0} \sigma_{k}\left(B_{s}\right) .$$
To calculate the derivative of $\sigma_{k}\left(B_{s}\right)$, we use the formula
$$\frac{d}{d s} \sigma_{k}\left(B_{s}\right)=\operatorname{tr} T_{k-1}\left(B_{s}\right) \cdot \frac{d B_{s}}{d s},$$
where, for an integer $0 \leq m \leq n, T_{m}\left(B_{s}\right)$ is defined as
$$T_{m}\left(B_{s}\right):=\sum_{j=0}^{m}(-1)^{j} \sigma_{m-j}\left(B_{s}\right) B_{s}^{j}$$
and it is known as the $m$-th Newton transform of $B_{s}$ (in the formula above we use the conventions: $B^{0}=\mathbb{I}_{n}$ and $\sigma_{0}\left(B_{s}\right)=1$ ). As a consequence we get:
$$\left.\frac{d}{d s}\right|_{s=0} \sigma_{k}\left(B_{s}\right)=\left.\sum_{j=0}^{k-1}(-1)^{j} \sigma_{k-1-j}\left(B_{0}\right) \operatorname{tr} B_{0}^{j} \cdot \frac{d B_{s}}{d s}\right|_{s=0} .$$
To make the expression above more explicit, we need to compute the coefficients of $B_{s}$ and their derivatives at $s=0$. For the coefficients of $B_{0}$, from formulae (2.2), we obtain
$$\left(B_{0}\right)_{t}^{t}=\frac{n-2 k}{4 k} \frac{k-n}{k} h_{\Sigma} \quad \text { and } \quad\left(B_{0}\right)_{j}^{i}=\frac{n-2 k}{4 k} h_{\Sigma} \delta_{j}^{i} .$$
Replacing $v$ by $v_{\Sigma}+s w$ in the identity (2.1), one can easily obtain the expression for $A_{s}$. Using (2.3) again, it is straightforward to see that:
$$\begin{aligned}
\left.\frac{d\left(B_{s}\right)_{t}^{t}}{d s}\right|_{s=0} & =-v_{\Sigma} \partial_{t}^{2} w+\frac{2(n-k)}{n-2 k} \dot{v_{\Sigma}} \partial_{t} w-\left(\frac{n-2 k}{2 k} v_{\Sigma}+\ddot{v_{\Sigma}}\right) w \\
\left.\frac{d\left(B_{s}\right)_{j}^{i}}{d s}\right|_{s=0} & =-v_{\Sigma} g_{\theta}^{i l}\left(\nabla_{\theta}^{2} w\right)_{l j}-\frac{2 k}{n-2 k} \dot{v_{\Sigma}} \delta_{j}^{i} \partial_{t} w+\frac{n-2 k}{2 k} v_{\Sigma} \delta_{j}^{i} w \\
\left.\frac{d\left(B_{s}\right)_{j}^{t}}{d s}\right|_{s=0} & =-v_{\Sigma} \partial_{t} \partial_{j} w+\frac{n}{n-2 k} \dot{v_{\Sigma}} \partial_{j} w \\
\left.\frac{d\left(B_{s}\right)_{t}^{i}}{d s}\right|_{s=0} & =g_{\theta}^{i l}\left(-v_{\Sigma} \partial_{t} \partial_{l} w+\frac{n}{n-2 k} \dot{v_{\Sigma}} \partial_{l} w\right)
\end{aligned}$$
This implies, for $1 \leq j \leq k-1$,
$$\begin{aligned}
\left.\operatorname{tr} B_{0}^{j} \cdot \frac{d B_{s}}{d s}\right|_{s=0}=\left(\frac{n-2 k}{4 k}\right)^{j} h_{\Sigma}^{j} v_{\Sigma}\left\{\left(\frac{k-n}{k}\right)^{j}\right. & {\left[-\partial_{t}^{2} w+\frac{2(n-k)}{n-2 k} \frac{\dot{v_{\Sigma}}}{v_{\Sigma}} \partial_{t} w-\left(\frac{n-2 k}{2 k}+\frac{\ddot{v_{\Sigma}}}{v_{\Sigma}}\right) w\right] } \\
+ & {\left.\left[-\Delta_{\theta} w-\frac{2 k(n-1)}{n-2 k} \frac{\dot{v_{\Sigma}}}{v_{\Sigma}} \partial_{t} w+\frac{(n-2 k)(n-1)}{2 k} w\right]\right\} }
\end{aligned}$$
and
$$\sigma_{k-1-j}\left(B_{0}\right)=\left(\frac{n-2 k}{4 k}\right)^{k-1-j} h_{\Sigma}^{k-1-j} \frac{1+j}{k}\binom{n}{k-1-j} .$$
Using these in the formal expression of the derivative of $\sigma_{k}\left(B_{s}\right)$ and using a similar computation as in [24], we obtain
$$\mathbb{L}_{c y l}^{0}\left(v_{\Sigma}\right)[w]=-C_{n, k} v_{\Sigma} h_{\Sigma}^{k-1}\left[\partial_{t}^{2}+\frac{n-k}{k(n-1)} \Delta_{\theta}-\left(\frac{n-2 k}{2 k}\right)^{2}\right] w,$$
where $C_{n, k}=\binom{n-1}{k-1}\left(\frac{n-2 k}{4 k}\right)^{k-1}$ and $h_{\Sigma} \equiv 1$.
Notice that from (2.7) one has immediately that the $\sigma_{k}$-Schwarzschild metric $g_{\Sigma}$ belongs to $\bar{\Gamma}_{k}^{+} \cap \Gamma_{k-1}^{+}$, for $2 \leq 2 k<n$.

\section*{3 Approximate solutions and perturbative approach}

In this section we construct the connected sum $M_{\varepsilon}:=M_{1} \sharp_{\varepsilon} M_{2}$ of the two manifolds $\left(M_{1}, g_{1}\right),\left(M_{2}, g_{2}\right)$ obtained by excising two geodesic balls of radius $\varepsilon \in(0,1)$ centered at $p_{1} \in M_{1}$ and $p_{2} \in M_{2}$ and identifying the two left over boundaries. At the same time we will define on $M_{\varepsilon}$ a new metric $g_{\varepsilon}$ which agrees with the old ones outside the balls of radius one and which is modeled on (a scaled version of) the $\sigma_{k}$-Schwarzschild metric in the neck region.

To describe the construction we consider the diffeomorphisms given by the exponential maps
$$\exp _{p_{i}}: B\left(O_{p_{i}}, 1\right) \subset T_{p_{i}} M_{i} \longrightarrow B\left(p_{i}, 1\right) \subset M_{i}, \quad i=1,2 .$$
Next, to fix the notation, we identify the tangent spaces $T_{p_{i}} M_{i}$ with $\mathbb{R}^{n}$. It is well known that this identification yields normal coordinates centered at the points $p_{i}$, namely
$$x: B\left(p_{1}, 1\right) \longrightarrow \mathbb{R}^{n} \quad \text { and } \quad y: B\left(p_{2}, 1\right) \longrightarrow \mathbb{R}^{n} .$$
We introduce now asymptotic cylindrical coordinates on the punctured ball $B^{*}(0,1)=x\left(B^{*}\left(p_{1}, 1\right)\right)$ setting $t:=\log \varepsilon-\log |x|$ and $\theta:=x /|x|$. In this way we have the diffeomorphism $B^{*}(0,1) \simeq(\log \varepsilon,+\infty) \times$ $\mathbb{S}^{n-1}$. Analogously, we consider the diffeomorphism $y\left(B^{*}\left(p_{2}, 1\right)\right)=B^{*}(0,1) \simeq(-\infty,-\log \varepsilon) \times \mathbb{S}^{n-1}$, this time setting $t:=-\log \varepsilon+\log |y|$ and $\theta:=y /|y|$.

In order to define the differential structure of $M_{\varepsilon}$, we excise a geodesic ball $B\left(p_{i}, \varepsilon\right)$ from $M_{i}$, obtaining an annular region $A\left(p_{i}, 1, \varepsilon\right):=B\left(p_{i}, 1\right) \backslash B\left(p_{i}, \varepsilon\right), i=1,2$. The asymptotic cylindrical coordinates introduced above can be used to define a natural coordinate system on the neck region
$$(t, \theta):\left[A\left(p_{1}, 1, \varepsilon\right) \sqcup A\left(p_{2}, 1, \varepsilon\right)\right] / \sim \longrightarrow(\log \varepsilon,-\log \varepsilon) \times \mathbb{S}^{n-1}=: T_{\varepsilon},$$
where $\sim$ denotes the equivalence which identifies the boundaries of $B\left(p_{1}, \varepsilon\right)$ and $B\left(p_{2}, \varepsilon\right)$, namely
$$q_{1} \sim q_{2} \Longleftrightarrow x /|x|\left(q_{1}\right)=y /|y|\left(q_{2}\right) \quad \text { and } \quad|x|\left(q_{1}\right)=\varepsilon=|y|\left(q_{2}\right) .$$
Clearly, in this coordinates, the two identified boundaries correspond now to the set $\{0\} \times \mathbb{S}^{n-1}$. To complete the definition of the differential structure of the connected sum $M_{\varepsilon}$ it is sufficient to consider the old coordinate charts on $M_{i} \backslash B\left(p_{i}, 1\right), i=1,2$.

We are now ready to define on $M_{\varepsilon}$ the approximate solution metric $g_{\varepsilon}$. First of all we define $g_{\varepsilon}$ to be equal to the $g_{i}$ on $M_{i} \backslash B\left(p_{i}, 1\right), i=1,2$. To define $g_{\varepsilon}$ in the neck region, we start by observing that the
choice of the normal coordinate system allows us to expand the two metric $g_{1}$ and $g_{2}$ around $p_{1}$ and $p_{2}$ respectively as
$$g_{1}=\left[\delta_{\alpha \beta}+\mathcal{O}\left(|x|^{2}\right)\right] d x^{\alpha} \otimes d x^{\beta} \quad \text { and } \quad g_{2}=\left[\delta_{\alpha \beta}+\mathcal{O}\left(|y|^{2}\right)\right] d y^{\alpha} \otimes d y^{\beta} .$$
In terms of the $(t, \theta)$-coordinates we get, for $i=1,2$,
$$g_{i}=u_{i}^{\frac{4 k}{n-2 k}}\left[\left(1+a_{t t}^{(i)}\right) d t \otimes d t+\left(g_{j l}^{\theta}+a_{j l}^{(i)}\right) d \theta^{j} \otimes d \theta^{l}+a_{t j}^{(i)}\left(d t \otimes d \theta^{j}+d \theta^{j} \otimes d t\right)\right],$$
where, as usual, $g_{j l}^{\theta}$ are the coefficients of the round metric on $\mathbb{S}^{n-1}$, the conformal factors $u_{i}$ are given by
$$u_{1}:=\varepsilon^{\frac{n-2 k}{2 k}} e^{-\frac{n-2 k}{2 k} t} \quad \text { and } \quad u_{2}:=\varepsilon^{\frac{n-2 k}{2 k}} e^{\frac{n-2 k}{2 k} t}$$
and, finally, the remainders $a^{(i)}$.. verify
$$a_{\cdots}^{(1)}=\mathcal{O}\left(\varepsilon^{2} e^{-2 t}\right) \quad \text { and } \quad a_{\cdots}^{(2)}=\mathcal{O}\left(\varepsilon^{2} e^{2 t}\right) .$$
We choose a cut-off functions $\eta:(\log \varepsilon,-\log \varepsilon) \rightarrow[0,1]$ to be a non increasing smooth function which is identically equal to 1 in $(\log \varepsilon,-1]$ and 0 in $[1,-\log \varepsilon)$, and we choose another cut-off function $\chi:(\log \varepsilon,-\log \varepsilon) \rightarrow[0,1]$ to be a non increasing smooth function which is identically equal to 1 in $(\log \varepsilon,-\log \varepsilon-1]$ and which satisfies $\lim _{t \rightarrow-\log \varepsilon} \chi=0$. Using these two cut-off functions, we can define a new conformal factor $u_{\varepsilon}$ by
$$u_{\varepsilon}:=\chi(t) u_{1}+\chi(-t) u_{2}$$
and the metric $g_{\varepsilon}$ by
$$g_{\varepsilon}=u_{\varepsilon}^{\frac{4 k}{n-2 k}}\left[\left(1+a_{t t}\right) d t \otimes d t+\left(g_{j l}^{\theta}+a_{j l}\right) d \theta^{j} \otimes d \theta^{l}+a_{t j}\left(d t \otimes d \theta^{j}+d \theta^{j} \otimes d t\right)\right],$$
where the remeinder $a \ldots$ verifes
$$a \ldots=\eta a_{\ldots}^{(1)}+(1-\eta) a_{\ldots}^{(2)}=\mathcal{O}\left(\varepsilon^{2} \cosh (2 t)\right) .$$
We want to point out that the conformal factor $u_{\varepsilon}$ in $(\log \varepsilon+1,-\log \varepsilon-1) \times \mathbb{S}^{n-1}$ is a scaled version of the conformal factor $v_{\Sigma}$ of the $\sigma_{k}$-Schwarzschild metric, namely
$$u_{\varepsilon}(t)=\varepsilon^{\frac{n-2 k}{2 k}} \cosh \left(\frac{n-2 k}{2 k} t\right)$$
in $(\log \varepsilon+1,-\log \varepsilon-1) \times \mathbb{S}^{n-1}$. In force of this, the approximate solution metric $g_{\varepsilon}$ can be viewed as a perturbation of a scaled version of $g_{\Sigma}=v_{\Sigma}^{4 k /(n-2 k)} g_{\text {cyl }}$, namely
$$g_{\varepsilon}=\left(2 \varepsilon^{\frac{n-2 k}{2 k}}\right)^{\frac{4 k}{n-2 k}} g_{\Sigma}+A^{\varepsilon},$$
where
$$A^{\varepsilon}=u_{\varepsilon}^{\frac{4 k}{n-2 k}}\left[a_{t t} d t \otimes d t+a_{j l} d \theta^{j} \otimes d \theta^{l}+a_{t j}\left(d t \otimes d \theta^{j}+d \theta^{j} \otimes d t\right)\right],$$
and the coefficients verify $A_{\ldots}^{\varepsilon}=u_{\varepsilon}^{\frac{4 k}{n-2 k}} a_{\ldots}=\mathcal{O}\left(\varepsilon^{\frac{n+2 k}{2 k}} \cosh \left(\frac{n+2 k}{2 k} t\right)\right)$.
To simplify all the computations in the analysis we will make the following assumption

Assumption 3.1. The metric $g_{i}$ is conformally flat in $B\left(p_{i}, 1\right), i=1,2$.

Later we will show that this assumption can be removed. Now we are going to describe how the expression of $g_{\varepsilon}$ simplifies under the conformally flatness of the metric around the gluing locus. First of all, we observe that for $i=1,2$ the metric $g_{i}$ can now be expanded around $p_{i}$ as
$$g_{i}=u_{i}^{\frac{4 k}{n-2 k}}\left(1+c_{i}\right) g_{c y l},$$
with $c_{1}=\mathcal{O}\left(\varepsilon^{2} e^{-2 t}\right)$ and $c_{2}=\mathcal{O}\left(\varepsilon^{2} e^{2 t}\right)$. Thus, it is natural to define the approximate solution metric $g_{\varepsilon}$ as
$$g_{\varepsilon}=u_{\varepsilon}^{\frac{4 k}{n-2 k}}(1+c) g_{c y l},$$
where $c:=\eta c_{1}+(1-\eta) c_{2}=\mathcal{O}\left(\varepsilon^{2} \cosh (2 t)\right)$. Notice that this definition perfectly agrees with (3.1) with
$$c_{i}=a_{t t}^{(i)}, \quad a_{j l}^{(i)}=c_{i} g_{j l}^{\theta} \quad \text { and } \quad a_{t j}^{(i)}=0, \quad i=1,2 .$$
To summarize, we fix a background metric $\bar{g}$ defined by
$$\bar{g}:= \begin{cases}g_{i} & \text { on } M_{i} \backslash B\left(p_{i}, 1\right) \\ u_{\varepsilon}^{-\frac{4 k}{n-2 k}} g_{\varepsilon} & \text { on } \left.A\left(p_{1}, 1, \varepsilon\right) \sqcup A\left(p_{2}, 1, \varepsilon\right)\right] / \sim\end{cases}$$
In particular we notice that $\bar{g}=(1+c) g_{\text {cyl }}$ on $A\left(p_{1}, 1, \varepsilon\right) \sqcup A\left(p_{2}, 1, \varepsilon\right)$ under the Assumption 3.1. In order to write the approximate solution $g_{\varepsilon}$ as a conformal deformation of the background metric $\bar{g}$, it is sufficient to extend the definition of $u_{\varepsilon}$ setting $u_{\varepsilon} \equiv 1$ on $M_{\varepsilon} \backslash T_{\varepsilon}$. It is clear that
$$g_{\varepsilon}=u_{\varepsilon}^{\frac{4 k}{n-2 k}} \bar{g} .$$
To conclude the description of the approximate solutions we observe that from our definition it follows immediately that $g_{\varepsilon} \rightarrow g_{i}$ with respect to the $C^{m}$-topology on the compact subsets of $M_{i} \backslash\left\{p_{i}\right\}$, for $i=1,2$ and every $m \in \mathbb{N}$. A consequence of this fact is the following

Lemma 3.2. Let $g_{1}$ and $g_{2}$ be two $(k-1)$-admissible metrics on $M_{1}$ and $M_{2}$, respectively. Then there exists a positive real number $\varepsilon_{0}>0$ only depending on $n, k$ and the $C^{2}$-norm of the coefficients of the metrics $g_{1}$ and $g_{2}$ such that, for every $\varepsilon \in\left(0, \varepsilon_{0}\right]$, the approximate solution $g_{\varepsilon}$ lies in $\Gamma_{k-1}^{+}$.

Proof. We argue by contradiction. We fix an index $j \in\{1, \ldots, k-1\}$ and we suppose that there exists a sequence of parameters $\left\{\varepsilon_{i}\right\}_{i \in \mathbb{N}}$ and a corresponding sequence of points $q_{i} \in M_{\varepsilon_{i}}, i \in \mathbb{N}$ such that
\begin{itemize}
\item[-] $\varepsilon_{i} \rightarrow 0$, as $i \rightarrow+\infty$,
\item[-] $\sigma_{j}\left(g_{\varepsilon_{i}}^{-1} A_{g_{\varepsilon_{i}}}\right)\left(q_{i}\right) \leq 0, \quad i \in \mathbb{N}$.
\end{itemize}
Without loss of generality we can suppose, up to pass to a subsequence, that for every $i \in \mathbb{N}$ the point $q_{i}$ belongs to $M_{1} \backslash B\left(p_{1}, \varepsilon_{i}\right)$. Depending on the behavior of the $q_{i}$ 's, we have to distinguish three possible cases.

Case 1: There exists a subsequence of $q_{i}$ 's such that
$$q_{i} \longrightarrow q_{\infty} \in M_{1} \backslash\left\{p_{1}\right\} .$$
Since by construction the metrics $g_{\varepsilon_{i}}$ 's converge to $g_{1}$ on the compact sets of $M_{1} \backslash\left\{p_{1}\right\}$ with respect to the $C^{2}$-norm, we deduce that $\sigma_{j}\left(g_{1}^{-1} A_{g_{1}}\right)\left(q_{\infty}\right) \leq 0$, which is a contradiction.

Case 2: There exists a subsequence of $q_{i}$ 's such that
$$\operatorname{dist}_{g_{1}}\left(q_{i}, p_{1}\right)=\mathcal{O}\left(\varepsilon_{i}\right), \quad \text { as } \quad i \rightarrow+\infty .$$
Since $q_{i} \rightarrow p_{1}$, the sequence of points $q_{i}$ will stay definitely in the annulus $A\left(p_{1}, 1, \varepsilon_{i}\right)$, which is mapped to $\left(\log \varepsilon_{i}, 0\right) \times \mathbb{S}^{n-1}$ via the asymptotic cylindrical coordinates $(t, \theta)$. Setting $t_{i}:=t\left(q_{i}\right)$, we have that, for
large enough $i$ 's, $\left(t_{i}, \theta\right) \in[-C, 0] \times \mathbb{S}^{n-1}$, for some fixed positive constant $C>0$. In this compact region we have that the Schouten tensors $A_{g_{\varepsilon_{i}}}$ 's of the approximate solutions $g_{\varepsilon_{i}}$ 's converge uniformly to the Schouten tensor $A_{g_{\Sigma}}$ of the $\sigma_{k}$-Schwarzschild metric $g_{\Sigma}$, according to the conformal transformation law (2.1). The contradiction follows from (2.7).

Case 3: There exists a subsequence of $q_{i}$ 's such that
$$\operatorname{dist}_{g_{1}}\left(q_{i}, p_{1}\right)=o\left(\varepsilon_{i}\right) \quad \text { as } \quad i \rightarrow+\infty .$$
It is convenient to set $\alpha_{i}:=\operatorname{dist}_{g_{1}}\left(q_{i}, p_{1}\right)$. Again, since $q_{i} \rightarrow p_{1}$, the sequence of points $q_{i}$ will stay definitely in the annulus $A\left(p_{1}, 1, \varepsilon_{i}\right)$, which is mapped to $N_{1, \varepsilon_{i}}=\left(\log \varepsilon_{i}, 0\right) \times \mathbb{S}^{n-1}$ via the asymptotic cylindrical coordinates $(t, \theta)$. In this case we have that $t_{i}=t\left(q_{i}\right) \rightarrow-\infty$, as $i \rightarrow+\infty$. To investigate the behavior of the Schouten tensors $A_{g_{\varepsilon_{i}}}$ 's about the points $q_{i}$ 's, it is preferable to translate and rescale all of our quantities by setting
$$\hat{g}_{\varepsilon_{i}}(t, \theta):=\alpha_{i}^{-\frac{4 k}{n-2 k}} g_{\varepsilon_{i}}\left(t+t_{i}, \theta\right)=\left[\alpha_{i}^{-1} u_{\varepsilon_{i}}\left(t+t_{i}\right)\right]^{\frac{4 k}{n-2 k}}\left(1+c\left(t+t_{i}, \theta\right)\right) g_{c y l}$$
In terms of these new objects, we have by assumption that $\sigma_{j}\left(g_{\text {cyl }}^{-1} A_{\hat{g}_{\varepsilon}}\right)(0, \theta) \leq 0$. For any fixed positive constant $C>0$ we have now that on the compact subsets of the form $[-C, C] \times \mathbb{S}^{n-1}$ the functions $\alpha_{i}^{-1} u_{\varepsilon_{i}}\left(\cdot+t_{i}\right)$ converge to 1 in $C^{2}$-norm, we deduce that the Schouten tensors $A_{\hat{g}_{\varepsilon_{i}}}$ 's converge uniformly to $A_{\text {cyl }}$. A straightforward computation yields
$$\sigma_{j}\left(g_{\text {cyl }}^{-1} A_{\text {cyl }}\right)=2^{-j}\binom{n}{j}\left(\frac{n-2 j}{n}\right)>0,$$
which is a contradiction. \(\square\)

To introduce the analysis which follows, we recall that our ultimate goal is to show that, up to choose the parameters $\varepsilon$ in a suitable range, it is possible to find a smooth perturbation $w$ of the conformal factor $u_{\varepsilon}$ such that
$$\mathcal{N}_{\bar{g}}\left(u_{\varepsilon}+w\right)=0,$$
where the nonlinear operator is defined as in (1.3).
As mentioned in the introduction, we want to solve the fully nonlinear equation (3.6) by means of a fixed point argument. To do that, we consider the Taylor expansion:
$$\mathcal{N}_{\bar{g}}\left(u_{\varepsilon}+w\right):=\mathcal{N}_{\bar{g}}\left(u_{\varepsilon}\right)+\mathbb{L}_{\bar{g}}\left(u_{\varepsilon}\right)[w]+\mathcal{Q}_{\bar{g}}\left(u_{\varepsilon}\right)(w),$$
where according to (1.5)
$$\mathbb{L}_{\bar{g}}\left(u_{\varepsilon}\right)[w]:=\left.\frac{d}{d s}\right|_{s=0} \mathcal{N}_{\bar{g}}\left(u_{\varepsilon}+s w\right)$$
represents the linearized operator of $\mathcal{N}_{\bar{g}}$ around the approximate solution $u_{\varepsilon}$ and
$$\mathcal{Q}_{\bar{g}}\left(u_{\varepsilon}\right)(w):=-\int_{0}^{1}\left[\mathbb{L}_{\bar{g}}\left(u_{\varepsilon}\right)-\mathbb{L}_{\bar{g}}\left(u_{\varepsilon}+s w\right)\right][w] d s$$
is the quadratic remainder.
Now, we are ready to study the mapping properties of $\mathbb{L}_{\bar{g}}\left(u_{\varepsilon}\right)$. In particular we will find the functional setting where the equation
$$\mathbb{L}_{\bar{g}}\left(u_{\varepsilon}\right)[w]=f \quad \operatorname{in} M_{\varepsilon}$$
can be solved with $\varepsilon$-uniform a priori estimates. Combining this with the estimates of the error term
$$\mathcal{E}_{\bar{g}}\left(u_{\varepsilon}\right)(w):=-\mathcal{N}_{\bar{g}}\left(u_{\varepsilon}\right)-\mathcal{Q}_{\bar{g}}\left(u_{\varepsilon}\right)(w),$$
we will be able to solve the fixed point problem
$$w=\mathbb{L}_{\bar{g}}\left(u_{\varepsilon}\right)^{-1} \circ \mathcal{E}_{\bar{g}}\left(u_{\varepsilon}\right)(w) .$$
To solve (3.9) we split our domain, namely the connected sum manifold $M_{\varepsilon}$, into the regions $\Omega_{i, \varepsilon}:=$ $M_{i} \backslash B\left(p_{i}, \varepsilon\right), i=1,2$. Notice that $\partial \Omega_{1, \varepsilon}=\partial \Omega_{2, \varepsilon}$ by construction.
As a first step we will produce solutions $w_{i}$ to the Dirichlet problem
$$\left\{\begin{aligned}
\mathbb{L}_{\bar{g}}\left(u_{\varepsilon}\right)\left[w_{i}\right] & =f & & \Omega_{i, \varepsilon} \\
w_{i} & =0 & & \partial \Omega_{i, \varepsilon}
\end{aligned}\right.$$
Clearly $w_{1}$ and $w_{2}$ have a $C^{0}$-matching on the common boundary $\{0\} \times \mathbb{S}^{n-1}$, but to produce a (weak) global solution on $M_{\varepsilon}$, one needs to improve this matching to be at least $C^{1}$. For this purpose we set
$$w:= \begin{cases}w_{1}+\bar{w}_{1} & \Omega_{1, \varepsilon} \\ w_{2}+\bar{w}_{2} & \Omega_{2, \varepsilon}\end{cases}$$
where $\bar{w}_{i}$ are two corrections which verify the homogenous problem
$$\left\{\begin{aligned}
\mathbb{L}_{\bar{g}}\left(u_{\varepsilon}\right)\left[\bar{w}_{i}\right] & =0 & \Omega_{i, \varepsilon} \\
\bar{w}_{i} & =\psi & \partial \Omega_{i, \varepsilon}
\end{aligned}\right.$$
with the same Dirichlet boundary data $\psi$ and the $C^{1}$-matching condition
$$\partial_{\nu}\left(w_{1}+\bar{w}_{1}\right)=-\partial_{\nu}\left(w_{2}+\bar{w}_{2}\right),$$
where $\nu$ denotes the outward normal to $\Omega_{1, \varepsilon}$. We want to point out that in the second part of this program, the datum will be the gap $\partial_{\nu}\left(w_{1}+w_{2}\right)$ between the normal derivatives of $w_{1}$ and $w_{2}$ and the unknown will be represented by the Dirichlet boundary data $\psi$. The existence of such a function $\psi$ will be deduced from the invertibility of (the difference of) Dirichlet to Neumann maps (for a precise definition see Section 4.3).

\section*{4 Linear analysis}

The aim of this section is to provide existence, uniqueness and a priori estimates for solutions to the linear problem
$$\mathbb{L}_{\bar{g}}\left(u_{\varepsilon}\right)[w]=f \quad M_{\varepsilon} .$$
As anticipated in last part of the previous section, we start by dividing the connected sum manifold $M_{\varepsilon}$ into the subdomains $\Omega_{1, \varepsilon}$ and $\Omega_{2, \varepsilon}$ and since the situation is symmetric we will focus for most part of the time on the domain $\Omega_{1, \varepsilon}$ and we will study the problem
$$\left\{\begin{aligned}
\mathbb{L}_{\bar{g}}\left(u_{\varepsilon}\right)[w] & =f & & \Omega_{1, \varepsilon} \\
w & =0 & & \partial \Omega_{1, \varepsilon}
\end{aligned}\right.$$
Most part of the work here will amount to establish uniform a priori estimates for solutions to this problem which do not depend on the necksize parameter $\varepsilon$. To do that we will employ a blow-up technique which,
in the limit, will lead us to analyze some model situations, depending on where the blow-up points are going to concentrate. As it will be made clear in the proof of Propsition 4.4, in two of the three possible cases, when the blow-up points concentrate on the neck region, we will take advantage of our geometric construction, whereas in the remaining one, when the blow-up points stay away from the gluing locus, we will exclude the blow-up phenomenon thanks to the non degeneracy condition 1.1 and Corollary 4.3, which is the main issue of the following subsection.

\subsection*{4.1 A removable singularities lemma}

This subsection, whose content is somehow independent of the rest of the paper, is concerned with the proof of a removable singularities result for the linearized $\sigma_{k}$-Yamabe equation on the puctured unit ball endowed with a conformally flat metric, see Corollary 4.3.

To begin, let $u=u(s, \theta),(s, \theta) \in(0,+\infty) \times \mathbb{S}^{n-1}$, be a smooth solution to the equation
$$\mathcal{N}_{c y l}(u):=\sigma_{k}\left(B_{g_{u}}\right)-\binom{n}{k}\left(\frac{n-2 k}{4 k}\right)^{k} u^{\frac{2 k n}{n-2 k}}=0,$$
on $(0,+\infty) \times \mathbb{S}^{n-1}$. We recall that $g_{u}=u^{\frac{4 k}{n-2 k}} g_{\text {cyl }}$ and
$$B_{g_{u}}=\frac{n-2 k}{2 k} g_{c y l}^{-1}\left[u^{2} A_{c y l}-\frac{2 k}{n-2 k} u \nabla^{2} u+\frac{2 k n}{(n-2 k)^{2}} d u \otimes d u-\frac{2 k^{2}}{(n-2 k)^{2}}|d u|^{2} g_{c y l}\right] .$$
Suppose to have the expansion
$$u(s, \theta)=e^{-\frac{n-2 k}{2 k} s}\left(1+b_{0}(s, \theta)\right),$$
where $b_{0}(s, \theta)=\mathcal{O}\left(e^{-2 s}\right)$. Passing from cylindrical to the flat background metric on the punctured ball, this corresponds to the usual expansion of $g_{u}$ in normal coordinates centered at the removed point.

Lemma 4.1. Under this hypothesis, if $4 \leq 2 k<n$, then the solution $u$ verifies
$$u(s, \theta)=v(s)(1+b(s, \theta)),$$
where $v(s)=\cosh ^{-\frac{n-2 k}{2 k}}\left(s-s_{0}\right)(1+c(s))$, for some $s_{0} \in \mathbb{R}, c(s)=\mathcal{O}\left(e^{-2 s}\right)$ and $b(s, \theta)=\mathcal{O}\left(e^{-2 k s}\right)$.
Proof. First we observe that
$$\begin{aligned}
d u & =\partial_{s} u d s+u\left(1+b_{0}\right)^{-1} \partial_{j} b_{0} d \theta^{j}=\partial_{s} u d s+u\left(1+b_{0}\right)^{-1} d_{\theta} b_{0}, \\
\nabla_{c y l}^{2} u & =\partial_{s}^{2} u d s \otimes d s+\partial_{s j}^{2} u\left(d s \otimes d \theta^{j}+d \theta^{j} \otimes d s\right)+\nabla_{\theta}^{2} u,
\end{aligned}$$
where $d_{\theta}$ and $\nabla_{\theta}^{2}$ denote the exterior differential and the Hessian computed with respect to the standard differential structure and standard metric of $\mathbb{S}^{n-1}$. Hence, the components of $B_{g_{u}}$ can be written as
$$\begin{aligned}
\frac{2 k}{n-2 k}\left(g_{c y l} B_{g_{u}}\right)_{s s} & =-\frac{1}{2} u^{2}-\frac{2 k}{n-2 k} u \partial_{s}^{2} u+\frac{2 k(n-k)}{(n-2 k)^{2}}\left|\partial_{s} u\right|^{2}-\frac{2 k^{2}}{(n-2 k)^{2}} u^{2}\left(1+b_{0}\right)^{-2}\left|d_{\theta} b_{0}\right|^{2} \\
& =-\frac{1}{2} u^{2}-\frac{2 k}{n-2 k} u \partial_{s}^{2} u+\frac{2 k(n-k)}{(n-2 k)^{2}}\left|\partial_{s} u\right|^{2}+\mathcal{O}\left(u^{2} e^{-4 s}\right),
\end{aligned}$$
$$\begin{aligned}
\frac{2 k}{n-2 k}\left(g_{c y l} B_{g_{u}}\right)_{s j} & =\left(\frac{2 k}{n-2 k}\right)^{2} u \partial_{s} u\left(1+b_{0}\right)^{-1} \partial_{j} b_{0}+\frac{2 k}{n-2 k} u^{2}\left(1+b_{0}\right)^{-2} \partial_{j} b_{0} \partial_{s} b_{0}-\frac{2 k}{n-2 k} u^{2}\left(1+b_{0}\right)^{-1} \partial_{s j}^{2} b_{0} \\
& =\left(\frac{2 k}{n-2 k}\right)^{2} u \partial_{s} u \partial_{j} b_{0}-\frac{2 k}{n-2 k} u^{2} \partial_{s j}^{2} b_{0}+\mathcal{O}\left(u^{2} e^{-4 s}\right),
\end{aligned}$$
$$\begin{aligned}
\frac{2 k}{n-2 k}\left(g_{c y l} B_{g_{u}}\right)_{i j}= & \frac{1}{2} u^{2} g_{i j}^{\theta}-\frac{2 k}{n-2 k} u^{2}\left(1+b_{0}\right)^{-1}\left(\nabla_{\theta}^{2} b_{0}\right)_{i j}+\frac{2 k n}{(n-2 k)^{2}} u^{2}\left(1+b_{0}\right)^{-2}\left(d_{\theta} b_{0} \otimes d_{\theta} b_{0}\right)_{i j} \\
& -\frac{2 k^{2}}{(n-2 k)^{2}}\left|\partial_{s} u\right|^{2} g_{i j}^{\theta}-\frac{2 k^{2}}{(n-2 k)^{2}} u^{2}\left(1+b_{0}\right)^{-2}\left|d_{\theta} b_{0}\right|^{2} g_{i j}^{\theta} \\
= & \frac{1}{2}\left(u^{2}-\left(\frac{2 k}{n-2 k}\right)^{2}\left|\partial_{s} u\right|^{2}\right) g_{i j}^{\theta}-\frac{2 k}{n-2 k} u^{2}\left(\nabla_{\theta}^{2} b_{0}\right)_{i j}+\mathcal{O}\left(u^{2} e^{-4 s}\right)
\end{aligned}$$

For algebraic reasons $\sigma_{k}\left(B_{g_{u}}\right)$ can be written as
$$\sigma_{k}\left(B_{g_{u}}\right)=\sum_{\alpha l+\beta m=k} C_{\alpha \beta}^{l m}\left[\operatorname{tr}\left(B_{g_{u}}^{l}\right)\right]^{\alpha}\left[\operatorname{tr}\left(B_{g_{u} u}^{m}\right)\right]^{\beta},$$
where $C_{\alpha \beta}^{l m}$ are constant coefficients and we assume that $\alpha, \beta, l, m \in \mathbb{N}$, with $0 \leq m, l \leq k$. A direct computation shows that for every $0 \leq l \leq k$
$$\operatorname{tr}\left(B_{g_{u}}^{l}\right)=\left[\left(B_{g_{u}}\right)_{s}^{s}\right]^{l}+\sum_{i=1}^{n-1}\left(B_{g_{u}}^{l}\right)_{i}^{i}+\mathcal{O}\left(u^{2 l} e^{-4 s}\right) .$$
Moreover, if we set
$$h=h(u):=u^{2}-\left(\frac{2 k}{n-2 k}\right)^{2}\left|\partial_{s} u\right|^{2},$$
we have
$$\begin{aligned}
2^{l} \sum_{i=1}^{n-1}\left(B_{g_{u}}^{l}\right)_{i}^{i} & =h^{l} \operatorname{tr}\left(\mathbb{I}_{n-1}-\frac{4 k}{n-2 k} u^{2} h^{-1} \nabla_{\theta}^{2} b_{0}+\mathcal{O}\left(u^{2} h^{-1} e^{-4 s}\right)\right)^{l} \\
& =h^{l} \operatorname{tr}\left(\mathbb{I}_{n-1}-\frac{4 k l}{n-2 k} u^{2} h^{-1} \nabla_{\theta}^{2} b_{0}+\mathcal{O}\left(u^{2} h^{-1} e^{-4 s}\right)\right) \\
& =h^{l}\left((n-1)-\frac{4 k l}{n-2 k} u^{2} h^{-1} \Delta_{\theta} b_{0}\right)+\mathcal{O}\left(u^{2 l} e^{-4 s}\right) .
\end{aligned}$$
In force of this considerations we obtain that
$$\begin{aligned}
0=N_{c y l}(u) & =\sigma_{k}\left(B_{g_{u}}\right)-\binom{n}{k}\left(\frac{n-2 k}{4 k}\right)^{k} u^{\frac{2 k n}{n-2 k}} \\
& =\left[A_{n, k} u\left(\partial_{s} u\right)^{-1}\right] \cdot \partial_{s}\left(h^{k}-u^{\frac{2 k n}{n-2 k}}\right)+\left[P_{2 k}\left(u, \partial_{s} u\right)\right] \cdot \Delta_{\theta} b_{0}+Q\left(u, \partial u, \partial^{2} u\right),
\end{aligned}$$
where $A_{n, k}$ is a constant only depending on $n$ and $k, P_{2 k}(\cdot, \cdot \cdot)$ is an homogeneous polynomial of degree $2 k$ and the reminder $Q\left(u, \partial u, \partial^{2} u\right)$ verifies the estimate $Q\left(u, \partial u, \partial^{2} u\right)=\mathcal{O}\left(u^{2 k} e^{-4 s}\right)$. The gain $e^{-4 s}$ is due to the presence of (at least) quadratic terms in $b_{0}$ and its derivatives. Using the eigenfunctions decomposition, we write
$$b_{0}(s, \theta)=b_{0}^{0}(s)+\sum_{j=1}^{+\infty} b_{0}^{j}(s) \phi_{j}(\theta) \quad \text { and } \quad \Delta_{\theta} b_{0}(s, \theta)=-\sum_{j=1}^{+\infty} \lambda_{j} b_{0}^{j}(s) \phi_{j}(\theta),$$
where $-\Delta_{\theta} \phi_{j}=\lambda_{j} \phi_{j}, j \in \mathbb{N}$. Since we have
$$h^{k}=\mathcal{O}\left(e^{-n s}\right) \quad \text { and } \quad u^{\frac{2 k n}{n-2 k}}=\mathcal{O}\left(e^{-n s}\right),$$
$k \geq 2$ and $n \geq 5$, we infer from the equation above that
$$b_{0}^{j}(s)=\mathcal{O}\left(e^{-4 s}\right), \quad j \geq 1 .$$
So we have found that $u$ expands as
$$u(s, \theta)=v(s)(1+b(s, \theta)),$$
where
$$v(s):=e^{-\frac{n-2 k}{2 k} s}\left(1+b_{0}^{0}(s)\right) \quad \text { and } \quad b(s, \theta):=\left(1+b_{0}^{0}(s)\right)^{-1} \sum_{j=1}^{+\infty} b_{0}^{j}(s) \phi_{j}(\theta)=\mathcal{O}\left(e^{-4 s}\right) .$$
We have
$$\begin{aligned}
u\left(\partial_{s} u\right)^{-1} & =-\frac{2 k}{n-2 k}\left(1+\mathcal{O}\left(\partial_{s} b_{0}^{0}\right)\right), \\
h^{k}-u^{\frac{2 k n}{n-2 k}} & =h_{v}^{k}-v^{\frac{2 k n}{n-2 k}}+\mathcal{O}\left(v^{2 k}\left(\partial_{s} b_{0}^{0}\right)^{k-1}\left(\partial_{s} b\right)\right)+\mathcal{O}\left(v_{1}^{\frac{2 k n}{n-2 k}} b\right), \\
\Delta_{\theta} b_{0} & =\left(\Delta_{\theta} b\right)\left(1+b_{0}^{0}\right),
\end{aligned}$$
where
$$h_{v}:=v^{2}-\left(\frac{2 k}{n-2 k}\right)^{2} \dot{v}^{2} .$$

Combining the new expression for $u$ with the same formal computation used to give a first expansion for the coefficients of $B_{g_{u}}$, we obtain
$$-\left[A_{n, k}\left(\frac{2 k}{n-2 k}\right)\right] \cdot \partial_{s}\left(h_{v}^{k}-v^{\frac{2 k n}{n-2 k}}\right)+\left[P_{2 k}\left(v, \partial_{s} v\right)\right] \cdot \Delta_{\theta} b+R+S=0,$$
where
$$R=\mathcal{O}\left(e^{-(n+2) s}\right) \quad \text { and } \quad S=\mathcal{O}\left(\left(\Delta_{\theta} b\right) e^{-(n-2 k+2) s}\right) .$$
This comes from the fact that the leading term of the reminders $R$ and $S$ are given by $\partial_{s} b_{0}^{0} \partial_{s}\left(h_{v}^{k}-v^{\frac{2 k n}{n-2 k}}\right)$ and $v^{2 k} b_{0}^{0} \Delta_{\theta} b$ respectively. At this level, we know that $\Delta_{\theta} b=\mathcal{O}\left(e^{-4 s}\right)$, so that $S=\mathcal{O}\left(e^{-(n-2 k+6)}\right)$. If $k=2$, then $R$ and $S$ decay with the same velocity, namely $\mathcal{O}\left(e^{-(n+2)}\right)$. For $k>2$, we have $n-2 k+6<$ $n+2$. Using again the eigenfunction decomposition, since the first term of the left hand side is radial, we obtain that
$$b(s, \theta)=\mathcal{O}\left(e^{-6 s}\right) .$$
Hence we have obtained an improvement of the expansion for the function $b$ which will improve the estimate of the reminder $S$. Iterating this argument, we will have that, after a finite number of steps, the decay rate of $S$ will be comparable with the one of $R$, which remains fixed during the bootstrap. At the end, both in the cases $k=2$ and $k>2$, we obtain
$$b(s, \theta)=\mathcal{O}\left(e^{-2 k s}\right) .$$
Moreover, projecting (4.3), we obtain
$$-\left[A_{n, k}\left(\frac{2 k}{n-2 k}\right)\right] \cdot \partial_{s}\left(h_{v}^{k}-v^{\frac{2 k n}{n-2 k}}\right)+R^{0}+S^{0}=0,$$
where $R^{0}$ and $S^{0}$ are given by
$$R^{0}(s):=\int_{\mathbb{S}^{n-1}} R \phi_{0} d V_{\mathbb{S}^{n-1}} \quad \text { and } \quad S^{0}(s):=\int_{\mathbb{S}^{n-1}} S \phi_{0} d V_{\mathbb{S}^{n-1}},$$
and both of them are $\mathcal{O}\left(e^{-(n+2) s}\right)$. It is now easy to see from equation (4.4) that $v(s) \simeq \cosh ^{-\frac{n-2 k}{2 k}}\left(s-s_{0}\right)$ for some $s_{0} \in \mathbb{R}$. Plugging the ansatz $v(s)=\cosh ^{-\frac{n-2 k}{2 k}}\left(s-s_{0}\right)(1+c(s))$ into the equation (4.4) we have that the reminder $c(s)$ is estimated as a $\mathcal{O}\left(e^{-2 s}\right)$. \(\square\)

We consider now a conformal perturbation of the metric $g_{u}$, namely, for $r \in \mathbb{R}$ and $w \in \mathcal{C}^{2}\left(\mathbb{R} \times \mathbb{S}^{n-1}\right)$, we consider the assignment
$$r \mapsto g_{r}:=(u+r w)^{\frac{4 k}{n-2 k}} \cdot d t^{2} \otimes d \theta^{2} .$$
Obviously $g_{0}=g_{r}$. Let now $A_{r}$ be the Schouten tensor of the metric $g_{r}$, and let $B_{r}$ be the symmetric (1,1)-tensor defined by
$$B_{r}:=\frac{n-2 k}{2 k}(u+r w)^{\frac{2 n}{n-2 k}} g_{r}^{-1} \cdot A_{r} .$$
Again $A_{0}=A_{g_{u}}$ and $B_{0}=B_{g_{u}}$. We compute
$$\mathbb{L}_{c y l}(u)[w]:=\left.\frac{d}{d r}\right|_{r=0} \mathcal{N}_{c y l}(u+r w)=\left.\frac{d}{d r}\right|_{r=0} \sigma_{k}\left(B_{r}\right)-\left.\binom{n}{k}\left(\frac{n-2 k}{4 k}\right)^{k} \frac{d}{d r}\right|_{r=0}(u+r w)^{\frac{2 n k}{n-2 k}}$$
To calculate the derivative of $\sigma_{k}\left(B_{r}\right)$, we use the formula
$$\frac{d}{d r} \sigma_{k}\left(B_{r}\right)=\operatorname{tr} T_{k-1}\left(B_{r}\right) \cdot \frac{d B_{r}}{d r},$$
where, for an integer $0 \leq h \leq n, T_{h}\left(B_{r}\right)$ is defined as
$$T_{h}\left(B_{r}\right):=\sum_{j=0}^{h}(-1)^{j} \sigma_{h-j}\left(B_{r}\right) B_{r}^{j}$$
and it is known as the $h$-th Newton transform of $B_{r}$ (in the formula above we use the conventions: $B^{0}=\mathbb{I}_{n}$ and $\sigma_{0}\left(B_{r}\right)=1$ ). As a consequence we get:
$$\left.\frac{d}{d r}\right|_{r=0} \sigma_{k}\left(B_{r}\right)=\left.\sum_{j=0}^{k-1}(-1)^{j} \sigma_{k-1-j}\left(B_{0}\right) \operatorname{tr} B_{0}^{j} \cdot \frac{d B_{r}}{d r}\right|_{r=0} .$$
From the previous lemma we know that
$$u(s, \theta)=v(s)(1+b(s, \theta)),$$
where $v(s)=\cosh ^{-\frac{n-2 k}{2 k}}\left(s-s_{0}\right)(1+c(s))$, for some $s_{0} \in \mathbb{R}, c(s)=\mathcal{O}\left(e^{-2 s}\right)$ and $b(s, \theta)=\mathcal{O}\left(e^{-2 k s}\right)$. Hence, the components of $B_{g_{u}}$ can be written as
$$\begin{aligned}
\frac{2 k}{n-2 k}\left(g_{c y l} B_{0}\right)_{s s}= & -\frac{1}{2} u^{2}-\frac{2 k}{n-2 k} u \partial_{s}^{2} u+\frac{2 k(n-k)}{(n-2 k)^{2}}\left|\partial_{s} u\right|^{2}-\frac{2 k^{2}}{(n-2 k)^{2}} u^{2}(1+b)^{-2}\left|d_{\theta} b\right|^{2} \\
= & -\frac{1}{2} v^{2}-\frac{2 k}{n-2 k} v \ddot{v}+\frac{2 k(n-k)}{(n-2 k)^{2}}|\dot{v}|^{2}+\mathcal{O}\left(v^{2} e^{-2 k s}\right), \\
\frac{2 k}{n-2 k}\left(g_{c y l} B_{0}\right)_{s j}= & \left(\frac{2 k}{n-2 k}\right)^{2} u \partial_{s} u(1+b)^{-1} \partial_{j} b+\frac{2 k}{n-2 k} u^{2}(1+b)^{-2} \partial_{j} b \partial_{s} b-\frac{2 k}{n-2 k} u^{2}(1+b)^{-1} \partial_{s j}^{2} b \\
= & \mathcal{O}\left(v^{2} e^{-2 k s}\right), \\
\frac{2 k}{n-2 k}\left(g_{c y l} B_{0}\right)_{i j}= & \frac{1}{2} u^{2} g_{i j}^{\theta}-\frac{2 k}{n-2 k} u^{2}(1+b)^{-1}\left(\nabla_{\theta}^{2} b\right)_{i j}+\frac{2 k n}{(n-2 k)^{2}} u^{2}(1+b)^{-2}\left(d_{\theta} b \otimes d_{\theta} b\right)_{i j} \\
& -\frac{2 k^{2}}{(n-2 k)^{2}}\left|\partial_{s} u\right|^{2} g_{i j}^{\theta}-\frac{2 k^{2}}{(n-2 k)^{2}} u^{2}(1+b)^{-2}\left|d_{\theta} b\right|^{2} g_{i j}^{\theta} \\
= & \frac{1}{2}\left(v^{2}-\left(\frac{2 k}{n-2 k}\right)^{2}|\dot{v}|^{2}\right) g_{i j}^{\theta}+\mathcal{O}\left(v^{2} e^{-2 k s}\right)=\frac{1}{2} h_{v} g_{i j}^{\theta}+\mathcal{O}\left(v^{2} e^{-2 k s}\right)
\end{aligned}$$
It is easy to see that:
$$\begin{aligned}
& \left.\frac{d\left(B_{r}\right)_{s}^{s}}{d r}\right|_{r=0}=-v \partial_{s}^{2} w+\frac{2(n-k)}{n-2 k} \dot{v} \partial_{s} w-\left(\frac{n-2 k}{2 k} v+\ddot{v}\right) w+A_{s}^{s}[w] \\
& \left.\frac{d\left(B_{r}\right)_{j}^{i}}{d r}\right|_{r=0}=-v g_{\theta}^{i l}\left(\nabla_{\theta}^{2} w\right)_{l j}-\frac{2 k}{n-2 k} \dot{v} \delta_{j}^{i} \partial_{s} w+\frac{n-2 k}{2 k} v \delta_{j}^{i} w+A_{j}^{i}[w] \\
& \left.\frac{d\left(B_{r}\right)_{j}^{s}}{d r}\right|_{r=0}=-v \partial_{s} \partial_{j} w+\frac{n}{n-2 k} \dot{v}+\partial_{j} w+A_{j}^{s}[w] \\
& \left.\frac{d\left(B_{r}\right)_{s}^{i}}{d r}\right|_{r=0}=g_{\theta}^{i l}\left(-v \partial_{s} \partial_{l} w+\frac{n}{n-2 k} \dot{v} \partial_{l} w\right)+A_{s}^{i}[w],
\end{aligned}$$
where $A_{s}^{s}, A_{j}^{i}, A_{j}^{s}, A_{s}^{i}, i, j=1, \ldots, n-1$, are second order linear operators whose coefficients depend on $v, b$ and their derivatives up to order two and can be estimated as $\mathcal{O}\left(v e^{-2 k s}\right)$. Hence, from (4.6), we obtain that the linearized operator (4.5) splits in
$$\mathbb{L}_{\text {cyl }}(u)[w]=\mathbb{L}_{\text {cyl }}(v)[w]+\mathbb{P}\left(v, \dot{v}, \ddot{v}, b, \partial b, \partial^{2} b\right)[w],$$
where $\mathbb{P}$ is a second order linear operators with coefficients estimated by $\mathcal{O}\left(v^{2 k-1} e^{-2 k s}\right)$. Now, we recall that from Lemma 4.1 we have
$$v(s)=\bar{v}(s)(1+c(s)),$$
where $\bar{v}(s):=\cosh ^{-\frac{n-2 k}{2 k}}\left(s-s_{0}\right)$ for some $s_{0} \in \mathbb{R}$ and $c(s)=\mathcal{O}\left(e^{-2 s}\right)$. Hence we can split $\mathbb{L}_{\text {cyl }}(v)$ as
$$\mathbb{L}_{\text {cyl }}(v)[w]=\mathbb{L}_{\text {cyl }}(\bar{v})[w]+\mathbb{M}(v, \dot{v}, \ddot{v})[w],$$
where $\mathbb{M}$ is a second order linear operator with coefficients estimated by $\mathcal{O}\left(e^{-\frac{2 k n-n-2 k}{2 k} s} e^{-2 s}\right)$ and $\mathbb{L}_{\text {cyl }}(\bar{v})$ is given by
$$\mathbb{L}_{c y l}(\bar{v})[w]=-C_{n, k} \bar{v}^{\frac{k(n-2)}{n-2 k}}\left(\partial_{s}^{2}+\Delta_{\mathbb{S}^{n-1}}-\left(\frac{n-2}{2}\right)^{2}+\frac{n(n+2)}{4} \bar{v}^{\frac{4 k}{n-2 k}}\right)\left[\bar{v}^{\frac{n(k-1)}{n-2 k}} w\right],$$
where $C_{n, k}=\binom{n-1}{k-1}\left(\frac{n-2 k}{4 k}\right)^{k-1}$. Hence it is easy to see that the coefficients of $\mathbb{L}_{\text {cyl }}(\bar{v})$ can be estimated by $\mathcal{O}\left(e^{-\frac{2 k n-n-2 k}{2 k} s}\right)$. As a consequence we have that, for $s \sim+\infty$, the relevant part of the linearized operator $\mathbb{L}_{\text {cyl }}(u)$ is given by $\mathbb{L}_{\text {cyl }}(\bar{v})$.

In force of these observations we are in the position to prove the following
Lemma 4.2. Suppose that $u \in C^{2}\left((0,+\infty) \times \mathbb{S}^{n-1}\right)$ verifies
$$\mathcal{N}_{c y l}(u)=0 \quad \text { on } \quad(0,+\infty) \times \mathbb{S}^{n-1}$$
as well as the expansion $u(s, \theta)=e^{-\frac{n-2 k}{2 k} s}\left(1+b_{0}(s, \theta)\right)$ with $b_{0}(s, \theta)=\mathcal{O}\left(e^{-2 s}\right)$.
Let $w \in C^{2}\left((0,+\infty) \times \mathbb{S}^{n-1}\right)$ be such that
$$\left\{\begin{aligned}
\mathbb{L}_{c y l}(u)[w] & =0 \quad \text { on } \quad(0,+\infty) \times \mathbb{S}^{n-1} \\
(\cosh s)^{-\frac{n(k-1)}{2 k}}|w(s, \theta)| & \leq C e^{\delta s},
\end{aligned}\right.$$
for some positive constant $C>0$ and some weight $-\frac{n-2}{2}<\delta<\frac{n-2}{2}$. Then
$$(\cosh s)^{-\frac{n(k-1)}{2 k}}|w(s, \theta)| \leq C e^{-\frac{n-2}{2} s} .$$
Proof. First of all we notice that the case $k=1$ is well known (see for example [17]). As we have already seen, for $k \geq 2$, the relevant part of the operator $\mathbb{L}_{\text {cyl }}(u)$ at $s \sim+\infty$ is given by $\mathbb{L}_{\text {cyl }}(\bar{v})$, defined as above. Hence, the asymptotic behavior of $w$ coincides with the one of a function $\bar{w}$ which satisfies
$$\mathbb{L}_{c y l}(\bar{v})[\bar{w}]=0 \quad \text { on } \quad(0,+\infty) \times \mathbb{S}^{n-1}$$
and $(\cosh s)^{-\frac{n(k-1)}{2 k}}|\bar{w}(s, \theta)| \leq C e^{\delta s}$, with $C$ and $\delta$ as above. From (4.8) we have that $z:=(\cosh s)^{-\frac{n(k-1)}{2 k}} \bar{w}$ satisfies
$$\left(\partial_{s}^{2}+\Delta_{\mathbb{S}^{n-1}}-\left(\frac{n-2}{2}\right)^{2}+\frac{n(n+2)}{4} \cosh ^{-2}\left(s-s_{0}\right)\right)[z]=0 \quad \text { on } \quad(0,+\infty) \times \mathbb{S}^{n-1}$$
and $|z(s, \theta)| \leq C e^{\delta s}$. Projecting along the eigenfunctions of $\Delta_{\mathbb{S}^{n-1}}$ and using standard ODE's arguments we obtain that
$$|z(s, \theta)| \leq C e^{-\frac{n-2}{2} s} .$$
The statement follows at once. \(\square\)

Thanks to Lemma 4.2 we are now able to prove the following removable singularities result
Corollary 4.3. Let $g=\left(1+b_{0}\right)^{\frac{4 k}{n-2 k}} g_{\mathbb{R}^{n}}$ be a conformally flat metric defined on a geodesic ball $B(p, 1)$ verifying the equation
$$\sigma_{k}\left(g^{-1} A_{g}\right)=2^{-k}\binom{n}{k} .$$
Suppose $\bar{w}$ satisfies in the sense of distributions
$$\mathbb{L}_{\mathbb{R}^{n}}\left(1+b_{0}\right)[\bar{w}]=0 \quad \text { on } \quad B^{*}(p, 1)$$
with $|\bar{w}(q)| \leq C\left|\operatorname{dist}_{g}(q, p)\right|^{-\mu}$ for any $q \in B^{*}(p, 1)$ for some positive constant $C>0$ and for some weight parameter $0<\mu<n-2$. Then $\bar{w}$ is a bounded smooth function on $B(p, 1)$ and satisfies the equation above on the entire ball.

Proof. First of all we observe that, using normal coordinates centered at $p$, we have $b_{0}(q)=\mathcal{O}\left(\left|\operatorname{dist}_{g}(q, p)\right|^{2}\right)$. Passing to cylindrical coordinates and using the conformal equivariance property (1.4) in order to recover the cylindrical background metric, we have that the equation satisfied by $\bar{w}$ becomes
$$\mathbb{L}_{\text {cyl }}\left(e^{-\frac{n-2 k}{2 k} s}\left(1+b_{0}(s, \theta)\right)\right)\left[e^{-\frac{n-2 k}{2 k} s} \bar{w}(s, \theta)\right]=0 \quad \text { on } \quad(0,+\infty) \times \mathbb{S}^{n-1} .$$
Letting $w(s, \theta):=e^{-\frac{n-2 k}{2 k} s} \bar{w}(s, \theta)$, we deduce from the decay assumption on $\bar{w}$ that
$$|w(s, \theta)| \leq C e^{\mu s} e^{-\frac{n-2 k}{2 k} s} .$$
If we define $\delta:=\mu-\frac{n-2}{2}$, we have that $-\frac{n-2}{2}<\delta<\frac{n-2}{2}$ and
$$|w(s, \theta)| \leq C e^{\delta s} e^{\frac{n(k-1)}{2 k} s} .$$
We are now in the position to apply Lemma 4.2 obtaining $|w(s, \theta)| \leq C e^{-\frac{n-2 k}{2 k} s}$. From this we get
$$|\bar{w}| \leq C \quad \text { on } \quad B^{*}(p, 1) .$$
The standard elliptic theory is now sufficient to conclude that $\bar{w}$ can be extended through the point $p$ to a smooth solution on $B(p, 1)$. \(\square\)

\subsection*{4.2 Uniform a priori estimates on $\Omega_{1, \varepsilon}$ and $\Omega_{2, \varepsilon}$}
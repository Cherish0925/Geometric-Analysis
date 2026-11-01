---
retention_scope: session
part: 1
total_parts: 1
---

---
source_file: 2401_07186v1.pdf
converter: mathpix
format: mmd
---

\title{
POSITIVE MASS THEOREM FOR ASYMPTOTICALLY FLAT MANIFOLDS WITH ISOLATED CONICAL SINGULARITIES
}

\author{
XIANZHE DAI, YUKAI SUN, AND CHANGLIANG WANG
}

\begin{abstract}
We prove the positive mass theorem for asymptotical flat (AF for short) manifolds with finitely many isolated conical singularities. We do not impose the spin condition. Instead we use the conformal blow up technique which dates back to Schoen's final resolution of the Yamabe conjecture.
\end{abstract}

\section*{Contents}
1. Introduction ..... 1
2. AF manifolds with isolated conical singularities ..... 5
3. Analysis on AF manifolds with isolated conical singularities ..... 7
3.1. Weighted Sobolev spaces ..... 7
3.2. Elliptic estimate for the Laplace operator ..... 7
3.3. Fredholm property of Laplace operator ..... 9
3.4. Solving the Laplace equation ..... 9
4. Nonnegativity of mass ..... 11
5. Rigidity ..... 15
References ..... 21

\section*{1. Introduction}

The famous Positive Mass Theorem states that an asymptotically flat (AF for short; also called asymptotically Euclidean) smooth manifold with nonnegative scalar curvature must have nonnegative ADM mass, and the mass is zero iff the manifold is the Euclidean space. This result was first proven by R. Schoen and S.-T. Yau [25] for manifolds of dimension between 3 and 7 using minimal surface method (for the recent progress of Schoen and Yau's argument in higher dimension, see [26]). E. Witten [28] proved the Positive Mass Theorem for spin manifolds of arbitrary dimension by using the Dirac operator.

It is a natural problem to generalize the Positive Mass Theorem to singular Riemannian manifolds (smooth manifolds endowed with non-smooth metrics), partially motived by the

\footnotetext{
Key words and phrases. Positive mass theorem, Conical singularity, Conformal change, Blow up.
}
investigation of weak notions of nonnegative scalar curvature, and the study of stability aspect of positive mass theorem. There has been a lot of interesting works in this problem, see e.g. [7, 11, 13, 14, 17, 19, 20, 27]. These deal with metric singularities occurring on smooth manifolds, and are usually assumed to be continuous and have $W^{1, p}$-regularity for $p \geq n$.

It was observed in [3, Section 4.2] (see also Proposition 2.3 in [27]) that the negative mass Schwarzchild metric can be viewed as an AF metric with a $r^{\frac{2}{3}}$-horn singularity, which is scalar flat but has negative mass. A model $r^{b}$-horn metric is given as
$$\bar{g}_{b}:=d r^{2}+r^{2 b} g^{N}, \text { for some } b>0,$$
on a product manifold $(0,1) \times N$, where $g^{N}$ is a Riemannian metric on closed manifold $N$, and near a $r^{b}$-horn singularity the metric is asymptotic to the model $r^{b}$-horn metric as $r \rightarrow 0$. In particular, for $b=1$, it is a conical singularity. These singular metrics are not continuous at the singular point, which is not even a topological manifold point if the cross section $N$ is not a sphere. In contrast to the negative mass Schwarzchild metric, the authors in [5] proved Positive Mass Theorem for AF spin manifolds with isolated $r^{b}$ -horn singularities for $b \geq 1$, and in particular for AF spin manifolds with isolated conical singularities. In [17], Li and Mantoulidis proved Positive Mass Theorem for metrics with conical singularities along a codimension two submanifold (aka edge metrics) on smooth AF manifolds. In [12], Ju and Viaclovsky proved a positive mass theorem for AF manifolds with isolated orbifold singularities.

Conical singularities also occur naturally in the study of the near horizon geometry of black holes. Motivated from this consideration, a positive mass theorem for conical singularity under the nonnegative Ricci curvature is established in [18] (modulo some analytic details).

In this paper, we prove Positive Mass Theorem for general AF manifolds with isolated conical singularity, i.e., without imposing the spin condition.

Theorem 1.1. Let $\left(M^{n}, g\right)$ be an $A F$ manifold with finitely many isolated conical sin-gularity and $n \geq 3$. If the scalar curvature is nonnegative on the smooth part, then the ADM mass $m(g)$ is nonnegative. Furthermore, the mass $m(g)=0$ if and only if $\left(M^{n}, g\right)$ is isometric to $\left(\mathbb{R}^{n}, g_{\mathbb{R}^{n}}\right)$.

Our result also holds for multiple AF ends, as we indicate later. In 3-dimension, by estimating capacity and Willmore functional of the cross sections, as an application of mass-capacity inequalities in [22], Miao [21] obtained the nonnegativity of the mass of an AF manifold with $r^{b}$-horn singularity with $b>\frac{2}{3}$, provided that the relative homology group $H_{2}\left(M \backslash B_{r_{0}}(o), \partial B_{r_{0}}(o)\right)=0$, here $o$ is the singular point and $B_{r_{0}}(o)$ is the geodesic ball centered at $o$ with radius $r_{0}$.

The precise definition of AF manifold with conical singularity is given in Section 2. These singular manifolds are not complete. This is one of main differences from the classical Positive Mass Theorem on complete AF manifolds. Some positive mass theorems
on incomplete AF manifolds have been established in [15, 16], provided that the scalar curvature on the AF end is nonnegative and satisfies some quantitative positive lower bound on a bounded domain near the AF infinity.

The non-negativity of the mass in Theorem 1.1 is proved in Section 4. The basic strategy is to construct an AF manifold with boundary, and then apply the results about the positive mass theorem for manifolds with boundary, e.g. in [8, 9, 10, 22] and others. A straightforward way to construct an AF manifold with boundary is to remove a conical neighborhood of the singular point from an AF manifold with a conical singularity. This idea works well for $r^{b}$-horn singularity with $b>1$, as we have done in [5]. However, in the case of $b<1$, the mean curvature of the boundary with respect to the normal pointing to AF end would be too large (relative to a certain negative power of the area of the boundary) to apply positive mass theorems for manifolds with boundary. As mentioned above, the negative mass Schwarzchild metric $\left(b=\frac{2}{3}\right)$ gives a counter-example to the positive mass theorem with $r^{b}$-horn singularity for $b<1$. In the case of conical singularity $(b=1)$, this simple construction may not give desired AF manifold with boundary either, since the required upper bound for the mean curvature seems not easy to be estimated.

Instead, in the case of conical singularity, before cutting off a part of the manifold, we first apply a conformal blow up technique to the AF metric with a conical singularity, following Ju and Viaclovsky's approach for orbifold singularity in [12]. More precisely, we first conformally deform the AF metric with conical singularity by using a harmonic function, which has asymptotic order like Green's function (i.e. $r^{2-n}$ ) near the conical singularity, and is asymptotic to 1 near the AF infinity. One may think the harmonic function as the Green function with its pole at the conical singularity. This conformal deformation flips over a cone, converting the conical singularity to the infinite end of the cone, and keeps the AF end up to a higher order perturbation. Then we remove the conical end, and obtain an AF manifold with boundary whose mean curvature is negative, and so we can apply Hirsch and Miao's results about positive mass theorem with boundary [10] to prove the non-negativity of the mass.

Note that by conformally blowing up the conical singularity, we obtain a Riemannian manifold with two ends, one is an AF end, and another is an asymptotically conical end, i.e. this manifold is an AF manifold with an additional complete end. Therefore, we can also apply results about the positive mass theorems on AF manifolds with arbitrary ends in [16, 29] (for dimensions between 3 and 7) and [4] (for spin manifolds) to prove the nonnegativity of the mass in Theorem 1.1.

In a related work [1], K. Akutagawa and B. Botvinnik studied the Yamabe problem for cylindrical manifolds, and obtained positive mass theorem for certain AF manifold with two specific conical singularities, which is constructed by a conformal blow up of a cylinder. The conformal blow up technique dates back to Schoen's solution of Yamabe problem [24], and has been a very useful and powerful tool in the study of various problems related to scalar curvature. The Schwarzschild metric $g=\left(1+\frac{m}{r^{n-2}}\right)^{\frac{4}{n-2}} g_{\mathbb{R}^{n}}$ on $\mathbb{R}^{n} \backslash\{0\}$,
for $m>0$, can be viewed as the conformal blowup of the origin by the Green's function $1+\frac{m}{r^{n-2}}$, which is asymptotic to 1 as $r \rightarrow \infty$ and has the asymptotical order $r^{2-n}$ as $r \rightarrow 0$.

The key in our argument is to find a suitable harmonic function. In contrast to the case of orbifold singularity, we need to solve for a harmonic function with certain prescribed asymptotic behavior on the AF manifold with conical singularity, which may not be lifted to a smooth manifold. To deal with the conical singularity, we employ weighted Sobolev spaces introduced in [5], which have two weights, one for the conical singularity and the other for the AF infinity.

The rigidity result in Theorem 1.1 is proved in Section 5. We first prove that the mass $m(g)=0$ and $\mathrm{Sc}_{g} \geq 0$ imply the AF metric with conical singularity must be Ricci flat, by deforming the metric in a compact domain away from conical singularity, and following a conformal change. In the case of orbifold singularity, as shown in [12], by applying the Bishop-Gromov's volume inequality for orbifolds, the Euclidean volume growth at AF infinity then implies that the metric has to be flat. It is more delicate and involved in the case of conical singularity, since the Bishop-Gromov's volume inequality may not hold for AF manifolds with conical singularity. We need to get the rigidity for the cross section of the cone so that we can get more information about the regularity of the metric. For that, we solve harmonic coordinates on AF manifolds with conical singularity, and study its asymptotic behavior near the conical singularity, which can be linked to the first nonzero eigenvalue on the cross section. Then we could apply Obata's rigidity theorem to obtain that the cross section must be isometric to the standard sphere. This then implies that the metric is continuous and has $W^{1, n}$-regularity, and so the rigidity result in [11] can be applied.

The paper is organized as follows. In Section 2, we introduce asymptotically flat (AF) manifolds with isolated conical singularities and their ADM mass and collect some basic facts on cones. Section 3 is devoted to the analysis on AF manifolds with isolated conical singularities. We review the weighted Sobolev spaces introduced in [5] and discuss the corresponding elliptic estimates for the Laplace operators, their Fredholm properties, and surjectivity. This is used in Section 4 and 5 to obtain asymptotically harmonic function with certain prescribed asymptotic behavior at the conical singularity or AF infinity. In Section 4 and 5 we prove the positive mass theorem for conical singularity (Theorem 1.1).

Acknowledgement: The authors are grateful to Jeff Viaclovsky for suggesting that something like this could work. Xianzhe Dai is partially supported by the Simons Foundation. Yukai Sun is partially funded by the National Key R\&D Program of China Grant 2020YFA0712800. Changliang Wang is partially supported by the Fundamental Research Funds for the Central Universities and Shanghai Pilot Program for Basic Research.

\section*{2. AF manifolds with isolated conical singularities}

In this section, we give the precise definition of what we call asymptotically flat (AF for short) manifolds with finitely many isolated conical singularities, and the definition of the mass (at infinity) for these singular manifolds.

Definition 2.1. We say $\left(M_{0}^{n}, g, d, o\right)$ is a compact Riemannian manifold with smooth boundary and a single conical singularity at $o \in M_{0} \backslash \partial M_{0}$, if
\begin{itemize}
\item[(i)] $d$ is a metric on $M_{0}$ and $\left(M_{0}, d\right)$ is a compact metric space with smooth boundary,
\item[(ii)] $g$ is a smooth Riemannian metric on the regular part $M_{0} \backslash\{o\}, d$ is the induced metric by the Riemannian metric $g$ on $M_{0} \backslash\{o\}$,
\item[(iii)] there exists a neighborhood $U_{o}$ of $o$ in $M \backslash \partial M$, such that $U_{o} \backslash\{o\} \simeq(0,1) \times N$ for a smooth compact manifold $N$, and on $U_{o} \backslash\{o\}$ the metric $g=\bar{g}+h$, where
$$\bar{g}=d r^{2}+r^{2} g^{N},$$
$g^{N}$ is a smooth Riemannian metric on $N, r$ is a coordinate on $(0,1), r=0$ corresponding the singular point $o$, and $h$ satisfies
\end{itemize}
$$\left|\bar{\nabla}^{k} h\right|_{\bar{g}}=O\left(r^{\alpha-k}\right), \quad \text { as } \quad r \rightarrow 0,$$
for some $\alpha>0$ and $k=0,1$ and 2, where $\bar{\nabla}$ is the Levi-Civita connection of $\bar{g}$.
Definition 2.2. We say $\left(M^{n}, g, o\right)$ is an asymptotically flat manifold with a single isolated conical singularity at $o$, if $M^{n}=M_{0} \cup M_{\infty}$ satisfies
\begin{itemize}
\item[(i)] $\left(M_{0},\left.g\right|_{M_{0} \backslash\{o\}}, o\right)$ is a compact Riemannian manifold with smooth boundary and a single conical singularity at $o$ defined as in Definition 2.1,
\item[(ii)] $M_{\infty}$ is diffeomorphic to $\mathbb{R}^{n} \backslash B_{R}(0)$ for some $R>0$, and under this diffeomorphism the smooth Riemannian metric $g$ on $M_{\infty}$ satisfies
$$g=g_{\mathbb{R}^{n}}+O\left(\rho^{-\tau}\right), \quad\left|\left(\nabla^{g_{\mathbb{R}^{n}}}\right)^{i} g\right|_{g_{\mathbb{R}^{n}}}=O\left(\rho^{-\tau-i}\right), \quad \text { as } \quad \rho \rightarrow+\infty,$$
for $i=1,2$ and 3, where $\tau>\frac{n-2}{2}$ is the asymptotical order, $\nabla^{g_{\mathbb{R}^{n}}}$ is the Levi-Civita connection of the Euclidean metric $g_{\mathbb{R}^{n}}$, and $\rho$ is the Euclidean distance to a base point.
\end{itemize}

Remark 2.3. For the sake of simplicity of notations, in Definition 2.2 we only defined AF manifolds with a single conical singularity and one AF end, and we will only focus on this case in this paper. AF manifolds with finitely many isolated conical singularities and finitely many AF ends can be defined similarly, and all results in this paper can be easily extended to the case of finitely many isolated conical singularities and finitely many AF ends.

Now we give the definition of the ADM mass of such Riemannian manifold.

Definition 2.4. Let $\left(M^{n}, g, o\right)$ be an asymptotically flat manifold with a single isolated conical singularity at $o$. The mass $m(g)$ is defined as:
$$m(g)=\lim _{R \rightarrow \infty} \frac{1}{\omega_{n}} \int_{S_{R}}\left(\partial_{i} g_{j i}-\partial_{j} g_{i i}\right) * d x^{j}$$
where $\left\{\frac{\partial}{\partial x^{i}}\right\}$ is an orthonormal basis of $g_{\mathbb{R}^{n}}$ and the $*$ operator is the Hodge star operator on the Euclidean space, the indices $i, j$ run over $M^{n}$ and $S_{R}$ is the sphere of radius $R$ on $\mathbb{R}^{n}$ and $\omega_{n}$ is the volume of the unit sphere in $\mathbb{R}^{n}$.

Finally we collect some basic facts for our model cone. Let $\left(N^{n-1}, g^{N}\right)$ be a compact Riemannian manifold, and $(C(N), \bar{g})=\left(\mathbb{R}_{+} \times N, d r^{2}+r^{2} g^{N}\right)$ be the Riemannian cone over $\left(N^{n-1}, g^{N}\right)$, where $r$ is the coordinate on $\mathbb{R}_{+}$. We call $\left(N, g^{N}\right)$ the cross section of the cone. Let $\left\{e_{1}, \cdots, e_{n-1}\right\}$ be a local orthonormal frame of $T N$ with respect to $g^{N}, \bar{e}_{i}=\frac{1}{r} e_{i}$ for all $i=1, \cdots, n-1$, and $\partial_{r}=\frac{\partial}{\partial r}$. Then $\left\{\bar{e}_{1}, \cdots, \bar{e}_{n-1}, \partial_{r}\right\}$ is a local orthonormal frame of $T C(N)$ with respect to $\bar{g}$. Let $\bar{\nabla}$ denote the Levi-Civita connection of $\bar{g}$. By Koszul's formula, one easily obtains
$$\left\{\begin{array}{l}
\bar{\nabla}_{\bar{e}_{i}} \partial_{r}=\frac{1}{r} \bar{e}_{i}, \\
\bar{\nabla}_{\partial_{r}} \bar{e}_{i}=\left[\partial_{r}, \bar{e}_{i}\right]+\bar{\nabla}_{\bar{e}_{i}} \partial_{r}=-\frac{1}{r} \bar{e}_{i}+\frac{1}{r} \bar{e}_{i}=0, \quad \forall 1 \leq i, j \leq n-1 . \\
\bar{\nabla}_{\partial_{r}} \partial_{r}=0, \\
\bar{\nabla}_{\bar{e}_{i}} \bar{e}_{j}=\nabla_{\bar{e}_{i}}^{g^{N}} \bar{e}_{j}-\frac{1}{r} \delta_{i j} \partial_{r},
\end{array}\right.$$
Let $\bar{R}$ denote the Riemann curvature tensor of $\bar{g}$, and $R^{N}$ denote the Riemann curvature tensor of $g^{N}$ on $N$. In the local frame $\left\{\bar{e}_{1}, \cdots, \bar{e}_{n-1}, \partial_{r}\right\}$, the only non-vanishing components of $\bar{R}$ are
$$\bar{R}_{i j k l}=r^{2}\left(R_{i j k l}^{N}+g_{i k}^{N} g_{j l}^{N}-g_{i l}^{N} g_{j k}^{N}\right), \quad 1 \leq i, j, k, l \leq n-1 .$$
In particular,
$$\bar{R}\left(\partial_{r}, X, Y, Z\right)=0, \quad \forall X, Y, Z \in \Gamma(T C(N)),$$
and so
$$\begin{aligned}
\operatorname{Ric}_{\bar{g}}(X, Y) & =\operatorname{Ric}_{g^{N}}(X, Y)-(n-2) g^{N}(X, Y), \quad \forall X, Y \in \Gamma(T N) ; \\
\operatorname{Ric}_{\bar{g}}\left(\partial_{r}, \cdot\right) & =0,
\end{aligned}$$
and
$$\mathrm{Sc}_{\bar{g}}=\frac{\mathrm{Sc}_{g^{N}}-(n-1)(n-2)}{r^{2}} .$$
The Laplace operator $\Delta_{\bar{g}}$ on $(C(N), \bar{g})$ is given by
$$\Delta_{\bar{g}}=\partial_{r}^{2}+\frac{n-1}{r} \partial_{r}+\frac{1}{r^{2}} \Delta_{g^{N}},$$
where $\Delta_{g^{N}}$ is Laplace operator on the cross section $\left(N, g^{N}\right)$.

\section*{3. Analysis on AF manifolds with isolated conical singularities}
3.1. Weighted Sobolev spaces. Let ( $M^{n}, g, o$ ) be a AF manifold with a single conical singularity at $o$ as defined in Definition 2.2. Choose three cut-off functions $0 \leq \chi_{1}, \chi_{2}, \chi_{3} \leq$ 1 satisfying:
$$\begin{aligned}
& \chi_{1}(x)= \begin{cases}1, & \operatorname{dist}(x, o)<\epsilon, \\
0, & \operatorname{dist}(x, o)>2 \epsilon,\end{cases} \\
& \chi_{2}(x)= \begin{cases}1, & \operatorname{dist}(x, o)>2 R, \\
0, & \operatorname{dist}(x, o)<R,\end{cases}
\end{aligned}$$
and
$$\chi_{3}=1-\chi_{1}-\chi_{2},$$
where $\epsilon>0$ is chosen sufficiently small such that the ball $B_{2 \epsilon}(o)$, centered at singular point $o$ with radius $2 \epsilon$, is contained in the asymptotically conical neighborhood $U_{o}$ in Definition 2.1, and $R>0$ is chosen sufficiently large such that $M \backslash B_{R}(o) \subset M_{\infty}$.

For each $1 \leq p<+\infty, k \in \mathbb{N}$ and $\delta, \beta \in \mathbb{R}$, the weighted Sobolev space $W_{\delta, \beta}^{k, p}(M)$ is defined to be the completion of $C_{0}^{\infty}(M \backslash\{o\})$ with respect to the weighted Sobolev norm given by
$$\|u\|_{W_{\delta, \beta}^{k, p}(M)}^{p}:=\int_{M} \sum_{i=0}^{k}\left(r^{-p(\delta-i)-n}\left|\nabla^{i} u\right|^{p} \chi_{1}+\rho^{-p(\beta-i)-n}\left|\nabla^{i} u\right|^{p} \chi_{2}+\left|\nabla^{i} u\right|^{p} \chi_{3}\right) d \operatorname{vol}_{g},$$
where $r$ is the radial coordinate on the conical neighborhood $U_{o}$ in Definition 2.1 and $\rho$ is the Euclidean distance function to a base point on $M_{\infty}$ in Definition 2.2, and $\left|\nabla^{i} u\right|$ is the norm of $i^{\text {th }}$ covariant derivative of $u$ with respect to $g$.

Note that by the definition of the weighted Sobolev norms, we clearly have
$$\left\{\begin{array}{l}
\delta^{\prime} \geq \delta, \\
\beta^{\prime} \leq \beta,
\end{array} \quad \Rightarrow \quad W_{\delta^{\prime}, \beta^{\prime}}^{k, p} \subset W_{\delta, \beta}^{k, p},\right.$$
and
$$r^{\nu} \chi_{1} \in W_{\delta, \beta}^{k, p}(M) \Longleftrightarrow \nu>\delta, \quad \rho^{\mu} \chi_{2} \in W_{\delta, \beta}^{k, p}(M) \Longleftrightarrow \mu<\beta .$$
3.2. Elliptic estimate for the Laplace operator. Throughout the paper, we always use $\lambda_{j}$ to denote the eigenvalues of the Laplace operator $\Delta_{g^{N}}$ on the cross section of the model cone $(C(N), \bar{g})$, and $E_{j}$ to denote the space of the corresponding eigenfunctions. We set
$$\nu_{j}^{ \pm}:=\frac{-(n-2) \pm \sqrt{(n-2)^{2}+4 \lambda_{j}}}{2} .$$

Definition 3.1. We say $\delta \in \mathbb{R}$ is critical at conical point if $\delta=\nu_{j}^{+}$or $\delta=\nu_{j}^{-}$for some $j \in \mathbb{Z}_{\geq 0}$, where $\nu_{j}^{ \pm}$is defined as in (3.7).

We view the Euclidean space $\left(\mathbb{R}^{n}, g_{\mathbb{R}^{n}}\right)$ as a cone over the round sphere $\mathbb{S}^{n-1}$ with constant sectional curvature 1, whose Laplace operator has eigenvalues: $j(n-2+j)$, $j \in \mathbb{N}$. Replacing $\lambda_{j}$ by these eigenvalues on round sphere, we make following definition.

Definition 3.2. We say $\beta \in \mathbb{R}$ is critical at infinity if $\beta=k$ or $\beta=2-n-k$ for some $k \in \mathbb{Z}_{\geq 0}$.

Definition 3.3. We say $(\delta, \beta) \in \mathbb{R}^{2}$ is critical if $\delta$ is critical at conical point or $\beta$ is critical at infinity.

By using scaling technique, the usual interior elliptic estimates, and the asymptotic control of metric $g$ near conical point in Definition 2.1 and near infinity in Definition 2.2, one can obtain the following weighted elliptic estimate. This is treated in detail in [5] for the Dirac operator and carries over except minor modifications.

Proposition 3.4. Let $\left(M^{n}, g, o\right)$ be an $A F$ manifold with a single conical singularity at $o$. For any $1 \leq p<+\infty$, and $\delta, \beta \in \mathbb{R}$, if $u \in L_{\delta, \beta}^{p}(M)$, and $\Delta u \in L_{\delta-2, \beta-2}^{p}(M)$, then
$$\|u\|_{W_{\delta, \beta}^{2, p}(M)} \leq C\left(\|\Delta u\|_{L_{\delta-2, \beta-2}^{p}(M)}+\|u\|_{L_{\delta, \beta}^{p}(M)}\right)$$
holds for some constant $C=C(g, n, p)$ independent of $u$.
To obtain Fredholm property for the Laplace operator, the following refined weighted elliptic estimate is crucial.

Proposition 3.5. Let $\left(M^{n}, g, o\right)$ be an $A F$ manifold with a single conical singularity at $o$. If $(\delta, \beta) \in \mathbb{R}^{2}$ is not critical as in Definition 3.3, there exists a constant $C=C(g, n)$ and a compact set $B \subset M \backslash\{o\}$ such that for any $u \in L_{\delta, \beta}^{2}(M)$ with $\Delta u \in L_{\delta-2, \beta-2}^{2}(M)$,
$$\|u\|_{W_{\delta, \beta}^{2,2}(M)} \leq C\left(\|\Delta u\|_{L_{\delta-2, \beta-2}^{2}(M)}+\|u\|_{L^{2}(B)}\right) .$$

Proposition 3.5 is an immediate consequence of Proposition 3.4 and the following Lemma:

Lemma 3.6. Let $\left(M^{n}, g, o\right)$ be an $A F$ manifold with a single conical singularity at $o$. If $(\delta, \beta) \in \mathbb{R}^{2}$ is not critical as in Definition 3.3, there exists a constant $C$ and a compact set $B \subset M \backslash\{o\}$ such that for any $u \in L_{\delta, \beta}^{2}(M)$ with $\Delta u \in L_{\delta-2, \beta-2}^{2}(M)$,
$$\|u\|_{L_{\delta, \beta}^{2}(M)} \leq C\left(\|\Delta u\|_{L_{\delta-2, \beta-2}^{2}(M)}+\|u\|_{L^{2}(B)}\right) .$$

To prove Lemma 3.6, it is suffices to deal with model cone metric $\bar{g}$ on the conical neighborhood of the singular point $o$ and $g_{\mathbb{R}^{n}}$ near the AF infinity. The estimate near the AF infinity has been done in [23], by doing a spectral decomposition with respect to
$\Delta_{g_{\mathrm{S} n-1}}$, and reducing the problem to estimating coefficient functions, which satisfy certain second order ODEs. The Euclidean metric $g_{\mathbb{R}^{n}}$ can be viewed as a model cone metric with standard sphere as the cross section. The proof in [23] can be adapted to that near the tip of a cone, and then the estimate near the conical singularity follows. In [5], we have derived in detail the analogous estimate for the Dirac operator. So we omit the details of the proof, and refer to [23] and [5].
3.3. Fredholm property of Laplace operator. We consider the unbounded operator
$$\begin{aligned}
\Delta_{\delta, \beta}: \operatorname{Dom}\left(\Delta_{\delta, \beta}\right) & \rightarrow L_{\delta-2, \beta-2}^{2}(M) \\
\varphi & \mapsto \Delta \varphi,
\end{aligned}$$
whose domain $\operatorname{Dom}\left(\Delta_{\delta, \beta}\right)$ is dense subset of $L_{\delta, \beta}^{2}(M)$ consisting of function $u$ such that $\Delta u \in L_{\delta-2, \beta-2}^{2}(M)$ in the sense of distributions.

As Lemma 4.8 in [5], we have:
Lemma 3.7. The unbounded operator $\Delta_{\delta, \beta}$ is closed.
The usual $L^{2}$ pairing $(\cdot, \cdot)_{L^{2}(M)}$ identifies the topological dual space of $L_{\delta, \beta}^{2}$ with $L_{-\delta-n,-\beta-n}^{2}$. By this identification, the adjoint operator $\left(\Delta_{\delta, \beta}\right)^{*}$ of $\Delta_{\delta, \beta}$ is given as
$$\begin{aligned}
\left(\Delta_{\delta, \beta}\right)^{*}: \operatorname{Dom}\left(\left(\Delta_{\delta, \beta}\right)^{*}\right) & \rightarrow L_{-\delta-n,-\beta-n}^{2} \\
u & \mapsto \Delta u,
\end{aligned}$$
where the domain: $\operatorname{Dom}\left(\left(\Delta_{\delta, \beta}\right)^{*}\right)$ is the dense subset of $L_{-\delta+2-n,-\beta+2-n}^{2}$ consisting of functions $u$ such that $\Delta u \in L_{-\delta-n,-\beta-n}^{2}$ in the distributional sense.

By applying the refined weighted elliptic estimate in Proposition 3.5, as Proposition 4.9 in [5], we have the following Fredholm property.

Proposition 3.8. If $(\delta, \beta) \in \mathbb{R}^{2}$ is not critical as in Definition 3.3, then the operator $\Delta_{\delta, \beta}$ is Fredholm, namely,
\begin{itemize}
\item[(1)] $\operatorname{Ran}\left(\Delta_{\delta, \beta}\right)$ is closed,
\item[(2)] $\operatorname{dim}\left(\operatorname{Ker}\left(\Delta_{\delta, \beta}\right)\right)<+\infty$,
\item[(3)] $\operatorname{dim}\left(\operatorname{Ker}\left(\left(\Delta_{\delta, \beta}\right)^{*}\right)\right)<+\infty$.
\end{itemize}

For the proof one can see that of Proposition 4.9 in [5].
3.4. Solving the Laplace equation. Let $\left(M^{n}, g, o\right)$ be an AF manifold with a single conical singularity at $o$ as defined in 2.2. The equation $\Delta u=f$ has been solved near infinity in [23]. Here we similarly solve it near the conical point $o$. The strategy is similar as solving the Dirac equation near the cone point in [5], and so we omit proofs of some results in this section and refer to the analogous results for Dirac operator in Section 4 in [5].

We use $B_{r}$ to denote the ball with radius $r$ centered at the conical singularity $o$. In the notion of weighted Sobolev norms and spaces over $B_{r}$, the subscript $\beta$ will be neglected,
and they will be written as $\|\cdot\|_{W_{\delta}^{2,2}\left(B_{r}\right)}$ and $W_{\delta}^{2,2}\left(B_{r}\right)$, since there is no asymptotic control near infinity need to be concerned over the finite ball $B_{r}$.

For the model cone metric $\bar{g}=d r^{2}+r^{2} g^{N}$, by solving the Dirichlet problem for the equation $\Delta_{\bar{g}} u=f$ on a compact exhaustion of $B_{2 r_{0}} \backslash\{o\}$, and using refined weighted elliptic estimate in Lemma 3.6, one can solve $\Delta_{\bar{g}} u=f$ on $B_{2 r_{0}}$ and prove the following:

Lemma 3.9. For $\delta \in \mathbb{R}$, which is noncritical at conical point, and a small number $r_{0}>0$, there is a bounded operator
$$G_{\bar{g}}: L_{\delta-2}^{2}\left(B_{2 r_{0}}\right) \rightarrow W_{\delta}^{2,2}\left(B_{2 r_{0}}\right)$$
such that $\Delta_{\bar{g}} \circ G_{\bar{g}}=i d$.
A perturbation argument extends this result to a more general setting, namely, for an asymptotically conical metric $g=\bar{g}+h$ where $h$ satisfies (2.1), and we have the following:

Proposition 3.10. For $\delta \in \mathbb{R}$, which is noncritical at cone point as in Definition 3.1, and a small number $r_{0}$, there is a bounded operator $G_{g}: L_{\delta-2}^{2}\left(B_{2 r_{0}}\right) \mapsto W_{\delta}^{2,2}\left(B_{2 r_{0}}\right)$ such that $\Delta_{g} \circ G_{g}=i d$.

As an application of Proposition 3.10, one can solve harmonic functions near the conical point, which are asymptotic to harmonic functions, $r^{\nu_{j}^{ \pm}} \phi_{j}$, with respect to the model cone metric $\bar{g}$.

Corollary 3.11. Given $j \in \mathbb{N}$ and $\phi \in E_{j}$, there are functions $\mathcal{H}_{j, \phi}^{ \pm}$that are harmonic near the conical point and can be written as
$$\mathcal{H}_{j, \phi}^{ \pm}=r^{\nu_{j}^{ \pm}} \phi+v_{ \pm}$$
with $v_{+}$in $W_{\eta}^{2,2}$ for any $\eta<\nu_{j}^{+}+\alpha$ and $v_{-}$in $W_{\eta}^{2,2}$ for any $\eta<\nu_{j}^{-}+\alpha$.
The solution of the equation $\Delta u=f$ may not be unique, and the difference of two solutions is a harmonic function. For the model cone metric $\bar{g}=d r^{2}+r^{2} g^{N}$, the Laplace operator $\Delta_{\bar{g}}$ is given in (2.6), and the harmonic functions are linear combinations of $r^{\nu_{j}^{ \pm}} \phi_{j}$, where $\nu_{j}^{ \pm}$are given in (3.7) and $\phi_{j} \in E_{j}$, i.e. $\Delta_{g^{N}} \phi_{j}=\lambda_{j} \phi_{j}$. Based on this observation, by using (3.6) and Lemma 3.9, one can prove the following:

Lemma 3.12. Suppose $\Delta_{\bar{g}} u=f$ with $u$ in $L_{\delta}^{2}\left(B_{2 r_{0}}\right)$ and $f$ in $L_{\delta^{\prime}-2}^{2}\left(B_{2 r_{0}}\right)$ for non-critical exponents $\delta<\delta^{\prime}$ and a small number $r_{0}$. Then there is an element $v$ of $L_{\delta^{\prime}}^{2}\left(B_{2 r_{0}}\right)$ such that $u-v$ is a linear combination of functions: $r^{\nu_{j}^{ \pm}} \phi_{j}$ with $\phi_{j} \in E_{j}$ and $\delta<\nu_{j}^{ \pm}<\delta^{\prime}$;

By using Corollary 3.11, the property for model cone metrics in Lemma 3.12 can be extended to asymptotically conical metrics $g$ as following:

Proposition 3.13. Suppose $\Delta_{g} u=f$ with $u$ in $L_{\delta}^{2}\left(B_{2 r_{0}}\right)$ and $f$ in $L_{\delta^{\prime}-2}^{2}\left(B_{2 r_{0}}\right)$ for noncritical exponents $\delta<\delta^{\prime}$. Then, up to making $B_{2 r_{0}}$ smaller, there is an element $v$ of $L_{\delta^{\prime}}^{2}\left(B_{2 r_{0}}\right)$ such that $u-v$ is a linear combination of the following functions: $\mathcal{H}_{j, \phi_{j}}^{ \pm}$with $\phi_{j}$
in $E_{j}$ and $\delta<\nu_{j}^{ \pm}<\delta^{\prime}$, where $\mathcal{H}_{j, \phi_{j}}^{ \pm}$are functions, harmonic near the conical singularity, obtained in Corollary 3.11.

Now we are ready to prove the surjectivity of $\Delta_{\delta, \beta}$ for certain noncritical indices $(\delta, \beta)$, which enables us to solve the equation $\Delta_{g} u=f$.

First, by using Fredholm property in Proposition 3.8, we can prove the following surjectivity. For the proof, we refer to proofs of Corollary 2 in [23] and Proposition 4.15 in [5].

Proposition 3.14. Let $\left(M^{n}, g, o\right)$ be an $A F$ manifold with a single conical singularity at $o$. For any noncritical $(\delta, \beta)$ satisfying $\delta \leq \frac{2-n}{2}$ and $\beta \geq \frac{2-n}{2}$, the map
$$\Delta_{\delta, \beta}: \operatorname{Dom}\left(\Delta_{\delta, \beta}\right) \rightarrow L_{\delta-2, \beta-2}^{2}(M)$$
is surjective.
Moreover, the map
$$\Delta_{\frac{2-n}{2}, \frac{2-n}{2}}: \operatorname{Dom}\left(\Delta_{\frac{2-n}{2}, \frac{2-n}{2}}\right) \rightarrow L_{-\frac{n+2}{2},-\frac{n+2}{2}}^{2}(M)$$
is an isomorphism.
Then by applying Propositions 3.13 and 3.14, we can extend the region of indices $(\delta, \beta)$ for which $\Delta_{\delta, \beta}$ is surjective, and obtain the following:

Proposition 3.15. Let $\left(M^{n}, g, o\right)$ be an $A F$ manifold with a single conical singularity at o. We have that
$$\Delta_{\delta, \beta}: \operatorname{Dom}\left(\Delta_{\delta, \beta}\right) \rightarrow L_{\delta-2, \beta-2}^{2}(M)$$
is surjective for noncritical $\delta<0$ and $\beta>2-n$.
Proof. By Proposition 3.14, it suffices to show that $\Delta_{\delta, \beta}$ is surjective for $\frac{2-n}{2}<\delta<0$ and $2-n<\beta<\frac{2-n}{2}$.

For arbitrary noncritical $\delta^{\prime} \in\left(\frac{2-n}{2}, 0\right)$ and $\beta^{\prime} \in\left(2-n, \frac{2-n}{2}\right)$, we take an arbitrary function $f \in L_{\delta^{\prime}-2, \beta^{\prime}-2}^{2}(M) \subset L_{\frac{2-n}{2}-2, \frac{2-n}{2}-2}^{2}(M)$. Proposition 3.14 then implies that there exists $u \in L_{\frac{2-n}{2}, \frac{2-n}{2}}^{2}(M)$ such that $\Delta u=f$. Proposition 3.13 then implies that $u \in L_{\delta^{\prime}, \beta^{\prime}}^{2}$, since there is no critical index at conical point in $\left(\delta^{\prime}, 0\right)$ and no critical index at infinity in $\left(\beta^{\prime}, \frac{2-n}{2}\right)$. Therefore, $\Delta_{\delta^{\prime}, \beta^{\prime}}$ is surjective, and this completes the proof. \(\square\)

\section*{4. Nonnegativity of mass}

In this section, we prove the non-negativity of the ADM mass for AF manifolds with a single conical singularity with nonnegative scalar curvature on the regular part, by following the approach of Ju and Viaclovsky in the case of orbifold singularity in [12]. For that, we first solve a harmonic function as following:

Lemma 4.1. Let $\left(M^{n}, g, o\right)$ be a $n$-dimensional $A F$ manifold with a single conical singularity at $o$. There exists a harmonic function $u$ on $M$ which satisfies $u>1$ and admits the expansion
$$u= \begin{cases}r^{2-n}+o\left(r^{2-n+\alpha^{\prime}}\right), & \text { as } r \rightarrow 0, \\ 1+A \rho^{2-n}+o\left(\rho^{2-n-\epsilon}\right), & \text { as } \rho \rightarrow \infty,\end{cases}$$
for $0<\alpha^{\prime}<\min \{1, \alpha\}$ and $0<\epsilon<\min \{1, \tau\}$, and some constant $A>0$. Here $\alpha$ and $\tau$ are asymptotic orders of the metric $g$ in Definitions 2.1 and 2.2.

Proof. Choose a cut-off function $\phi$ satisfying
$$\phi= \begin{cases}1, & \text { on } B_{\frac{1}{2}}(o), \\ 0, & \text { on } M \backslash B_{1}(o) .\end{cases}$$
Let $u_{0}=\phi r^{2-n}$, which is a smooth function supported in a neighborhood of the conically singular point $o$. Then because $\Delta_{\bar{g}} r^{2-n}=0$, by the asymptotic control of $g$ near conically singular point $o$, we have
$$\Delta_{g} u_{0}= \begin{cases}O\left(r^{-n+\alpha}\right), & \text { as } r \rightarrow 0, \\ 0, & \text { on } M \backslash B_{1}(o) .\end{cases}$$
By (3.6), this implies that
$$\Delta_{g} u_{0} \in L_{\delta-2, \beta-2}^{2}(M), \quad \forall \delta<2-n+\alpha, \quad \beta>2-n .$$
Then by applying Proposition 3.15, we obtain $v \in L_{\delta, \beta}^{2}$ such that
$$\Delta_{g} v=\Delta_{g} u_{0} .$$
So by setting $u_{1}=u_{0}-v$, we have $\Delta_{g} u_{1}=0$.
Now we derive the asymptotic behavior of $v$ near conically singular point and AF infinity. Near the singular point $o, u_{1}=r^{2-n}-v$, and so $\Delta_{g} u_{1}=0$ implies
$$\Delta_{g} v=\Delta_{g} r^{2-n}=\left(\Delta_{g}-\Delta_{\bar{g}}\right) r^{2-n}=O\left(r^{-n+\alpha}\right) \in L_{\delta-2}^{p}\left(B_{\frac{1}{2}}(o)\right), \quad \forall \delta<2-n+\alpha \text { and } \forall p>1,$$
by (3.6). Then the weighted elliptic estimate in Proposition 3.4 implies that $v \in W_{\delta}^{2,2}\left(B_{\frac{1}{2}}(o)\right)$ for $\delta<2-n+\alpha$. Consequently, the weighted Sobolev inequality in Proposition 3.4 in [6] implies that $v \in L_{\delta}^{\frac{2 n}{n-2}}\left(B_{\frac{1}{2}}(o)\right)$, and by applying weighed elliptic estimate in Proposition 3.4 (with $p=\frac{2 n}{n-2}$ ) again, we obtain $v \in W_{\delta}^{2, \frac{2 n}{n-2}}\left(B_{\frac{1}{2}}(o)\right)$ for $\delta<2-n+\alpha$. By repeating this process, we can obtain that $v \in W_{\delta}^{2, p}\left(B_{\frac{1}{2}}(o)\right)$ for all $p>1$ and $\delta<2-n+\alpha$, and so, by Proposition 3.4 in [6], we have
$$v=o\left(r^{2-n+\alpha^{\prime}}\right), \quad \text { as } \quad r \rightarrow 0,$$
for $0<\alpha^{\prime}<\alpha$.

Near the AF infinity, $u_{1}=v \in L_{\beta}^{2}\left(M_{\infty}\right)$ for $\beta>2-n$, and $\Delta_{g} v=\Delta_{g} u_{1}=0 \in L_{\beta^{\prime}}^{2}\left(M_{\infty}\right)$ for $1-n<\beta^{\prime}<2-n$. Thus, Proposition 4 in [23] implies that
$$v=A \rho^{2-n}+v^{\prime}, \quad v^{\prime} \in L_{\beta^{\prime}}^{2}\left(M_{\infty}\right),$$
for $1-n<\beta^{\prime}<2-n$, and some constant $A$. Moreover,
$$\Delta_{g} v^{\prime}=-\Delta_{g}\left(A \rho^{2-n}\right)=\left(\Delta_{g_{\mathbb{R}^{n}}}-\Delta_{g}\right)\left(A \rho^{2-n}\right)=O\left(\rho^{-n-\tau}\right) \in L_{\beta^{\prime}-2}^{p}\left(M_{\infty}\right),$$
for $(2-n-\tau<) 1-n<\beta^{\prime}<2-n$, and all $p>1$. Then the weighted elliptic estimate in Proposition 3.4 implies $v^{\prime} \in W_{\beta^{\prime}}^{2,2}\left(M_{\infty}\right)$. Then by a similar weighted elliptic bootstrapping argument as above, we can obtain $v^{\prime} \in W_{\beta^{\prime}}^{2, p}\left(M_{\infty}\right)$ for all $p>1$ and $1-n<\beta^{\prime}<2-n$, and so
$$v^{\prime}=o\left(\rho^{2-n-\epsilon}\right), \quad \text { as } \quad \rho \rightarrow \infty,$$
for $0<\epsilon<1$.
In summary, we obtain a harmonic function $u_{1}$ admitting the asymptotic behavior:
$$u_{1}= \begin{cases}r^{2-n}+o\left(r^{2-n+\alpha^{\prime}}\right), & \text { as } \quad r \rightarrow 0, \\ A \rho^{2-n}+o\left(\rho^{2-n-\epsilon}\right), & \text { as } \quad \rho \rightarrow \infty,\end{cases}$$
for $0<\alpha^{\prime}<\alpha$ and $0<\epsilon<\min \{1, \tau\}$.
We let $u:=1+u_{1}$. Then $u$ is a harmonic function satisfying the asymptotic control in (4.1). Finally, by using the strong maximum principle and the asymptotic behavior in (4.1), we obtain $u \geq 1$, and in particular, $A>0$. Then by applying the strong maximum principle again, we can obtain $u>1$. \(\square\)

Now we are ready to prove the following:
Theorem 4.2. Let $\left(M^{n}, g, o\right), n \geq 3$, be a $n$-dimensional $A F$ manifold with a single conical singularity at $o$. If the scalar curvature $\mathrm{Sc}_{g} \geq 0$, then the ADM mass $m(g) \geq 0$.

Proof. For the harmonic function obtained in Lemma 4.1, and any $\delta>0$, we define
$$u_{\delta}=\delta u+(1-\delta),$$
which satisfies $\Delta_{g} u_{\delta}=0, u_{\delta}>1$, and admits the asymptotic expansion
$$u_{\delta}= \begin{cases}\delta r^{2-n}+o\left(r^{2-n+\alpha^{\prime}}\right), & \text { as } \quad r \rightarrow 0, \\ 1+\delta A r^{2-n}+o\left(\rho^{2-n-\epsilon}\right), & \text { as } \quad \rho \rightarrow \infty,\end{cases}$$
for $0<\alpha^{\prime}<\alpha$ and $0<\epsilon<1$. Here the constant $A>0$.
Then we do a conformal change for the metric $g$, and let
$$g_{\delta}:=\left(u_{\delta}\right)^{\frac{4}{n-2}} g \text { on } M .$$

By the asymptotic expansion of $u_{\delta}$ at infinity as in (4.6), $g_{\delta}$ is asymptotically flat of order $\min \{\tau, n-2\}$. Near the conically singular point $o$, the metric $g$ is given as
$$g=d r^{2}+r^{2} g^{N}+h,$$
where $h$ satisfies (2.1), and so
$$g_{\delta}=\left(u_{\delta}\right)^{\frac{4}{n-2}} g=\delta^{\frac{4}{n-2}} r^{-4}\left(1+o\left(r^{\alpha^{\prime}}\right)\right)\left(d r^{2}+r^{2} g^{N}+h\right), \quad \text { as } \quad r \rightarrow 0 .$$
Now we do a change of variable, by letting $s=\delta^{\frac{2}{n-2}} \frac{1}{r}$, and rewrite $g_{\delta}$ as
$$g_{\delta}=\left(1+o\left(s^{-\alpha^{\prime}}\right)\right)\left(d s^{2}+s^{2} g^{N}+\tilde{h}\right),$$
where $|\tilde{h}|_{d_{s^{2}+s^{2} g^{N}}}=O\left(s^{-\alpha}\right)$ as $s \rightarrow \infty$. Therefore,
$$g_{\delta}=d s^{2}+s^{2} g^{N}+o\left(s^{-\alpha^{\prime}}\right), \quad \text { as } \quad s \rightarrow \infty,$$
since $0<\alpha^{\prime}<\alpha$. Note that the metric $g_{\delta}$ is asymptotically conical, and it tends to the infinity end of a cone, as $s \rightarrow \infty$ (i.e. $r \rightarrow 0$ ). Moreover, the scalar curvature of $g_{\delta}$ is given by
$$\mathrm{Sc}_{g_{\delta}}=\frac{4(n-1)}{n-2}\left(u_{\delta}\right)^{-\frac{n+2}{n-2}}\left(-\Delta_{g} u_{\delta}+\frac{n-2}{4(n-1)} \mathrm{Sc}_{g} u_{\delta}\right)=\left(u_{\delta}\right)^{-\frac{4}{n-2}} \mathrm{Sc}_{g} \geq 0 .$$
For any fixed $\delta>0$, we can choose a hypersurface $\Sigma_{\delta, s_{0}}:=\left\{s=s_{0}\right\}$ for some sufficiently large $s_{0}$ such that $\Sigma_{\delta, s_{0}}$ is strictly mean concave with respect to the normal pointing to the AF end of $\left(M, g_{\delta}\right)$. Let $M_{\delta}=M \backslash\left\{s \geq s_{0}\right\}$ be a AF manifold with strictly mean concave boundary. By applying Theorem in [10], we obtain
$$m\left(M_{\delta}, g_{\delta}\right) \geq 0 .$$
On the other hand,
$$m\left(M_{\delta}, g_{\delta}\right)=m(M, g)+4(n-2) \delta A .$$
Because this is true for any constant $\delta>0$, and $A$ is a fixed constant, we must have
$$m(M, g) \geq 0 .$$ \(\square\)

Remark 4.3. Note that $\left(M, g_{\delta}\right)$ is a complete Riemannian manifolds with two ends, one is an AF end and another is an asymptotically conical end. In the case of the dimension $3 \leq n \leq 7$, the results of the positive mass theorems on manifold with arbitrary ends in [16, 29] imply the mass $m\left(M, g_{\delta}\right) \geq 0$. Then our conclusion follows as well.

\section*{5. Rigidity}

In this section, we prove that when the mass is zero, then $M$ is isometric to $\mathbb{R}^{n}$. We first prove that $M$ is Ricci flat, then show that it must be the Euclidean space.

First of all, we state the following Sobolev inequality on AF manifold with a single conical singularity, which can be obtained by combining the Sobolev inequality on cone (see, Lemma 3.2 in [6]) and that on the Euclidean space. It will be used in the proof of Lemma 5.2.

Lemma 5.1. Let $\left(M^{n}, g, o\right)$ be a $n$-dimensional $A F$ conical singularity at $o$. There is a Sobolev constant $C>0$ such that
$$\left(\int_{M}|f|^{\frac{2 n}{n-2}} d \mathrm{vol}_{g}\right)^{\frac{n-2}{2 n}} \leq C\left(\int_{M}|\nabla f|^{2} d \mathrm{vol}_{g}\right)^{\frac{1}{2}}$$
holds for all $f \in C_{0}^{\infty}(\AA)$.
Then as analysis preparations for proving the rigidity result in Theorem 1.1 (stated in Theorem 5.4 below), we solve Schrödinger equation with compactly supported potential function on AF manifolds with a conical singularity in Lemma 5.2; and solve harmonic functions, which are asymptotic to Euclidean coordinate near the AF infinity in Lemma 5.3. We also study their asymptotic behaviors near the conical singularity, which are critical in the proof of Theorem 5.4.

Lemma 5.2. Let $\left(M^{n}, g, o\right)$ be an $A F$ manifold with a conical singularity at $o$. There exists a constant $\epsilon_{0}=\epsilon(g)$, such that if $f$ is a smooth function with compact support in $\stackrel{\circ}{M}$ and $\left\|f_{-}\right\|_{L^{\frac{n}{2}}(M)}<\epsilon_{0}$, then the equation
$$\left\{\begin{array}{l}
-\Delta_{g} u+f u=0, \\
u \rightarrow 1 \text { as } x \rightarrow \infty,
\end{array}\right.$$
has a positive solution admitting the asymptotic as:
$$u= \begin{cases}1+\frac{A}{\rho^{n-2}}+u_{1} & \text { as } \rho \rightarrow \infty, \\ B+a(y) r^{\nu_{1}}+u_{2} & \text { as } r \rightarrow 0,\end{cases}$$
where $A$ and $B$ are constants, and $B \geq 1$,
$$\nu_{1}:=\frac{2-n+\sqrt{(n-2)^{2}+4 \lambda_{1}}}{2},$$
here $\lambda_{1}$ is the first non-zero eigenvalue of the Laplacian $\Delta_{g^{N}}$ and $a(y)$ is a corresponding eigenfunction, i.e. $\Delta_{g^{N}} a(y)=-\lambda_{1} a(y)$, and $u_{1}$ and $u_{2}$ have asymptotic as
$$\left|\nabla^{i} u_{1}\right|=o\left(\rho^{\beta-i}\right), \quad \text { as } \quad \rho \rightarrow+\infty, \quad \text { for } \quad 2-n-\tau<\beta<2-n, \quad i=0,1,$$
and
$$\left|\nabla^{i} u_{2}\right|=o\left(r^{\delta-i}\right), \quad \text { as } \quad r \rightarrow 0, \quad \text { for } \quad \nu_{1}<\delta<\nu_{1}+\alpha, \quad i=0,1 .$$
Proof. Existence of a positive solution: Let $v=1-u$. Then equation (5.2) becomes
$$\Delta_{g} v-f v=-f .$$
On a compact subset $A_{r, \rho}:=B_{\rho}(o) \backslash B_{r}(o)$, consider the Dirichlet problem
$$\begin{cases}\Delta_{g} v_{r, \rho}-f v_{r, \rho}=-f, & \text { in } A_{r, \rho}, \\ v_{r, \rho}=0, & \text { on } \partial A_{r, \rho} .\end{cases}$$
By Fredholm alternative, if the homogeneous equation
$$\begin{cases}\Delta_{g} v_{r, \rho}-f v_{r, \rho}=0, & \text { in } A_{r, \rho} \\ v_{r, \rho}=0, & \text { on } \partial A_{r, \rho}\end{cases}$$
has only zero solution, then equation (5.8) has a unique solution. Suppose $\omega$ is a solution of equation (5.9). Multiplying $\omega$ to both sides of the equation in (5.9) and integrating by parts, by the Hölder inequality with $p=\frac{n}{2}, q=\frac{n}{n-2}$ and the Sobolev inequality in Lemma 5.1, we have
$$\begin{aligned}
\int_{A_{r, \rho}}|\nabla \omega|^{2} d \operatorname{vol}_{g} & =-\int_{A_{r, \rho}} f \omega^{2} d \operatorname{vol}_{g} \leq \int_{A_{r, \rho}} f_{-} \omega^{2} d \operatorname{vol}_{g} \\
& \leq\left(\int_{A_{r, \rho}} f_{-}^{\frac{n}{2}} d \operatorname{vol}_{g}\right)^{\frac{2}{n}}\left(\int_{A_{r, \rho}} \omega^{\frac{2 n}{n-2}} d \operatorname{vol}_{g}\right)^{\frac{n-2}{n}} \\
& \leq c_{1}\left(\int_{A_{r, \rho}} f_{-}^{\frac{n}{2}} d \operatorname{vol}_{g}\right)^{\frac{2}{n}}\left(\int_{A_{r, \rho}}|\nabla \omega|^{2} d \operatorname{vol}_{g}\right)
\end{aligned}$$
Thus if $\left\|f_{-}\right\|_{L^{\frac{n}{2}}(M)}<\frac{1}{c_{1}}$, then $\omega=0$. Therefore, equation (5.8) has a unique solution $v_{r, \rho}$. Multiplying $v_{r, \rho}$ to both sides of (5.8), using Hölder inequality and Sobolev inequality again,
$$\begin{aligned}
\int_{A_{r, \rho}}\left|\nabla v_{r, \rho}\right|^{2} d \mathrm{vol}_{g} \leq & \int_{A_{r, \rho}} f_{-} v_{r, \rho}^{2} d \mathrm{vol}_{g}+\int_{A_{r, \rho}} f v_{r, \rho} d \mathrm{vol}_{g} \\
\leq & c_{1}\left(\int_{A_{r, \rho}} f_{-}^{\frac{n}{2}} d \mathrm{vol}_{g}\right)^{\frac{2}{n}}\left(\int_{A_{r, \rho}}\left|\nabla v_{r, \rho}\right|^{2} d \mathrm{vol}_{g}\right) \\
& +\left(\int_{A_{r, \rho}}|f|^{\frac{2 n}{n+2}} d \mathrm{vol}_{g}\right)^{\frac{n+2}{2 n}}\left(\int_{A_{r, \rho}} v_{r, \rho}^{\frac{2 n}{n-2}} d \mathrm{vol}_{g}\right)^{\frac{n-2}{2 n}}
\end{aligned}$$
$$\begin{aligned}
\leq & c_{1}\left(\int_{A_{r, \rho}} f_{-}^{\frac{n}{2}} d \mathrm{vol}_{g}\right)^{\frac{2}{n}}\left(\int_{A_{r, \rho}}\left|\nabla v_{r, \rho}\right|^{2} d \mathrm{vol}_{g}\right) \\
& +c_{1}\left(\int_{A_{r, \rho}}|f|^{\frac{2 n}{n+2}} d \mathrm{vol}_{g}\right)^{\frac{n+2}{2 n}}\left(\int_{A_{r, \rho}}\left|\nabla v_{r, \rho}\right|^{2} d \mathrm{vol}_{g}\right)^{\frac{1}{2}}
\end{aligned}$$
As a consequence, there is a constant $c_{2}$ depending on $(M, g, f)$ such that $\left\|v_{r, \rho}\right\|_{L^{\frac{2 n}{n-2}}}<c_{2}$ and $\left\|\nabla v_{r, \rho}\right\|_{L^{2}}<c_{2}$. The standard theory of elliptic equations concludes that $v_{r, \rho}$ have uniformly bounded $C^{2, \alpha}$ norms. By Arzela-Ascoli theorem we may pass to a limit and conclude that equation (5.7) has a solution $v$. Then $u:=1+v$ is a solution of (5.2).

We claim that $u$ is a positive solution. First, we show that $u$ is nonnegative. Otherwise, $\Omega_{-}:=\{x \in M \mid u(x)<0\}$ is nonempty open set, and its boundary $\partial \Omega_{-}=u^{-1}(0)$ is a $(n-1)$-dimensional manifold, except on a closed set of lower dimension. We consider the Dirichlet boundary problem:
$$\begin{cases}\Delta_{g} u-f u=0, & \text { in } \Omega_{-}, \\ u=0, & \text { on } \partial \Omega_{-} .\end{cases}$$
Similarly as showing that (5.9) has only zero solution, we can show that (5.10) has also only zero solution, i.e. $u=0$ in $\Omega_{-}$. This contradicts with the construction of $\Omega_{-}$. Thus, $u$ must be nonnegative. Then by applying the strong maximum principle, one can see that $u$ must be positive everywhere.

Asymptotics of the solution: Because $f$ has compact support away from the singular point $o$, there exits sufficiently small $r_{0}>0$ such that $\Delta_{g} v_{r, \rho}=0$ on $A_{r, r_{0}}=B_{r_{0}}(o) \backslash B_{r}(o)$ for all $0<r<r_{0}$. For a small $\epsilon>0$, there exists a sufficient large constant $C_{0}>0$ such that $\left|v_{r, \rho}\right| \leq \frac{C_{0}}{r^{n-2-\epsilon}}$ on $\partial B_{r_{0}}(o)$ for all $r>0$, since $v_{r, \rho}$ have uniformly bounded $C^{2, \alpha}$-norm. Note that $C_{0}$ only depends on $r_{0}$ and $\epsilon$. Moreover,
$$\begin{aligned}
\Delta_{g}\left(C_{0} r^{2-n+\epsilon}\right) & =\Delta_{\bar{g}}\left(C_{0} r^{2-n+\epsilon}\right)+\left(\Delta_{g}-\Delta_{\bar{g}}\right)\left(r^{2-n+\epsilon}\right) \\
& =\epsilon(2-n+\epsilon) C_{0} r^{-n+\epsilon}+O\left(r^{-n+\epsilon+\alpha}\right),
\end{aligned}$$
and so we can choose $r_{0}$ sufficiently small so that $\Delta_{g}\left(C r^{2-n+\epsilon}\right) \leq 0$ on $B_{r_{0}}(o)$. Thus, we have
$$\begin{cases}\Delta_{g}\left(C_{0} r^{2-n+\epsilon} \pm v_{r, \rho}\right) \leq 0, & \text { in } A_{r, r_{0}} \\ C_{0} r^{2-n+\epsilon} \pm v_{r, \rho} \geq 0, & \text { on } \partial A_{r, r_{0}} .\end{cases}$$
Then maximum principle implies
$$C_{0} r^{2-n+\epsilon} \pm v_{r, \rho} \geq 0, \quad \text { on } \quad A_{r, r_{0}}, \quad \forall 0<r<r_{0} .$$
In other words, $\left|v_{r, r_{0}}\right| \leq C_{0} r^{2-n+\epsilon}$ on $A_{r, r_{0}}$ for all $0<r<r_{0}$. By taking limit, we conclude that a solution $v$ of (5.7) satisfies
$$|v| \leq C_{0} r^{2-n+\epsilon} \text { on } B_{r_{0}}(o) \text {. }$$

Similarly, we can show that for sufficiently large $\rho_{0}>0$ and $C_{1}>0$, the solution $v$ of (5.7) satisfies
$$|v| \leq C_{1} \rho^{2-n+\epsilon} \text { on } M \backslash B_{\rho_{0}}(o) .$$

Consequently, we obtain that $v \in L_{\delta, \beta}^{2}$ for $2-n<\delta<2-n+\epsilon<0$ and $2-n+\epsilon<\beta<0$, by (3.6). Note that
$$\Delta_{g} v=f v-f \in L_{\delta^{\prime}-2, \beta^{\prime}-2}^{2}, \quad \text { for } \quad \delta^{\prime}>0 \quad \text { and } \quad \beta^{\prime}<2-n,$$
since $f$ vanishes near the conically singular point and near the AF infinity. Then because there is no critical index between $2-n$ and 0 at either cone point or infinity, by applying Proposition 3.13 and the maximal principle, there are constants $A_{1}$ and $B_{1}$ such that
$$v= \begin{cases}\frac{A_{1}}{\rho^{n-2}}+u_{1}, & \text { as } \rho \rightarrow \infty, \\ B_{1}+a(y) r^{\nu_{1}}+u_{2}, & \text { as } r \rightarrow 0,\end{cases}$$
where
$$\nu_{1}:=\frac{2-n+\sqrt{(n-2)^{2}+4 \lambda_{1}}}{2},$$
here $\lambda_{1}$ is the first non-zero eigenvalue of the Laplacian $\Delta_{g^{N}}$ and $a(y)$ is a corresponding eigenfunction, i.e. $\Delta_{g^{N}} a(y)=-\lambda_{1} a(y), u_{1} \in L_{\beta^{\prime}}^{2}$ for some $\beta^{\prime}<2-n$, and $u_{2} \in L_{\delta^{\prime}}^{2}$ for some $\delta^{\prime}>\nu_{1}$. Note that $B_{1} \geq 0$, since $v$ is a nonnegative function on $M \backslash\{o\}$.

Moreover, because $\Delta_{g} v=0$ on $B_{r_{0}}(o)$, we have:
$$\Delta_{g} u_{2}=-\Delta_{g}\left(B_{1}+a(y) r^{\nu_{1}}\right)=-\left(\Delta_{g}-\Delta_{\bar{g}}\right)\left(a(y) r^{\nu_{1}}\right)=O\left(r^{\nu_{1}-2+\alpha}\right) \in L_{\delta-2}^{p}\left(B_{r_{0}}(o)\right),$$
for all $p>1$ and $\nu_{1}<\delta<\nu_{1}+\alpha$ by (3.6). Then by applying the weighted elliptic estimate in Proposition 3.4 (with $p=2$ ), we obtain $u_{2} \in W_{\delta}^{2,2}\left(B_{r_{0}}(o)\right)$ for $\nu_{1}<\delta<\nu_{1}+\alpha$. The weighted Sobolev embedding further implies $u_{2} \in L_{\delta}^{\frac{2 n}{n-2}}\left(B_{r_{0}}(o)\right)$ for $\nu_{1}<\delta<\nu_{1}+\alpha$. Applying Proposition 3.4 (with $p=\frac{2 n}{n-2}$ ) again gives $u_{2} \in W_{\delta}^{2, \frac{2 n}{n-2}}\left(B_{r_{0}}(o)\right)$. By repeating this process, we can obtain that $u_{2} \in W_{\delta}^{2, p}\left(B_{r_{0}}(o)\right)$ for all $p>1$ and $\nu_{1}<\delta<\nu_{1}+\alpha$. Then weighted Sobolev embedding implies
$$\left|\nabla^{i} u_{2}\right|=o\left(r^{\delta-i}\right), \quad \text { as } \quad r \rightarrow 0,$$
for $\nu_{1}<\delta<\nu_{1}+\alpha$ and $i=0,1$.
Similarly, we can obtain that $u_{1}$ has the asymptotic at infinity as in (5.5).
Thus,
$$u=1+v= \begin{cases}1+\frac{A}{\rho^{n-2}}+u_{1} & \text { as } \rho \rightarrow \infty, \\ B+a(y) r^{\nu_{1}}+u_{2} & \text { as } r \rightarrow 0,\end{cases}$$
where $u_{1}$ and $u_{2}$ have asymptotic as in (5.5) and (5.6) respectively, and $B=1+B_{1} \geq 1$. This completes the proof of the lemma. \(\square\)

Lemma 5.3. Let $\left(M^{n}, g, o\right)$ be a $A F$ manifold with a single conical singularity at $o$, and $\left\{x_{i}\right\}_{i=1}^{n}$ is the Euclidean coordinate on $M_{\infty}$ given by the diffeomorphism in Definition 2.2. There exist harmonic functions $y_{i}, 1 \leq i \leq n$, on $M$ admitting the following asymptotic:
$$y_{i}= \begin{cases}c+r \frac{2-n+\sqrt{(n-2)^{2}+4 \lambda_{1}}}{2} \phi_{i}+O\left(r^{\nu^{\prime}}\right), & \text { near the conical point } o, \\ x_{i}-u_{i}, & \text { near the } A F \text { infinity },\end{cases}$$
where $\lambda_{1}$ is the first nonzero eigenvalue of the Laplacian $\Delta_{g^{N}}$ on the cross section $\left(N, g^{N}\right)$ and $\phi_{i}$ is a corresponding eigenfunction, i.e. $\Delta_{g^{N}} \phi_{i}=-\lambda_{1} \phi_{i}$, and
$$\nu^{\prime}>\frac{2-n+\sqrt{(n-2)^{2}+4 \lambda_{1}}}{2}>0,$$
and $c \in \mathbb{R}$ is a constant. Moreover, $u_{i}$ satisfy
$$\left|u_{i}\right|+\rho\left|\partial u_{i}\right|+\rho^{2}\left|\partial^{2} u_{i}\right|=o\left(\rho^{1-\tau^{\prime}}\right), \quad \text { as } \quad \rho \rightarrow+\infty,$$
with $\tau^{\prime}=\tau-\epsilon>\frac{2-n}{2}$ for sufficiently small $\epsilon>0$.
Proof. Let $\chi$ be a cut-off function supported in $M_{\infty}$ and $\chi=1$ outside of a compact subset of $M_{\infty}$. Then
$$\Delta\left(\chi x_{i}\right)= \begin{cases}O\left(\rho^{-\tau-1}\right), & \text { as } \rho \rightarrow+\infty \\ 0, & \text { near the conical point } o,\end{cases}$$
and so by (3.6)
$$\Delta\left(\chi x_{i}\right) \in L_{\delta-2, \beta-2}^{2}(M), \text { for } 2-n<\delta<0, \beta>-\tau+1>2-n .$$
Therefore, Proposition 3.15 implies that there exists $u_{i} \in L_{\delta, \beta}^{2}(M)$ for $2-n<\delta<0, \beta>$ $-\tau+1>2-n$ such that
$$\Delta u_{i}=\Delta\left(\chi x_{i}\right) .$$
By letting $y_{i}=\chi x_{i}-u_{i}$, we obtain harmonic functions $y_{i}$, for $1 \leq i \leq n$.
Then note that near the conical point $o, y_{i}=-u_{i}$, and similarly as in the proof of Lemma 5.2 in [5], applying Proposition 3.13 gives the asymptotic of $y_{i}$ near the conical point as in (5.22). In addition, similarly as in the proof of Lemma 5.1 in [5], applying a Nash-Moser iteration argument gives the asymptotic of $u_{i}$ near infinity as in (5.23). \(\square\)

Now we are ready to prove the rigidity result in Theorem 1.1 as following.
Theorem 5.4. Let $\left(M^{n}, g, o\right)$ be an $A F$ manifold with a single conical singularity at $o$. If the scalar curvature $\mathrm{Sc}_{g} \geq 0$ and the ADM mass $m(g)=0$, then $\left(M^{n}, g\right)$ is isometric to the Euclidean space $\left(\mathbb{R}^{n}, g_{\mathbb{R}^{n}}\right)$.

Proof. First we show that if $\mathrm{Sc}_{g} \geq 0$ and $m(g)=0$ then $g$ is Ricci flat. For that, we take a variation $g_{t}=g+$ th of the metric $g$, where $h$ is an arbitrary compactly supported

2-tensor on $\stackrel{\circ}{M}$. Note that for each $t$ such that $|t|$ is sufficiently small, $g_{t}$ is still an AF manifold with a single conical singularity at $o$. Then we consider the following equation:
$$\begin{cases}-\Delta_{g_{t}} u+\frac{n-2}{4(n-1)}\left(\mathrm{Sc}_{g_{t}}-\mathrm{Sc}_{g}\right) u=0, & \text { on } \stackrel{\circ}{M}, \\ u \rightarrow 1, & \text { as } x \rightarrow \infty .\end{cases}$$
For each $t$ such that $|t|$ is sufficiently small, by Lemma 5.2, the equation (5.24) has a positive solution $u_{t}$, since $h$ is compactly supported and so is $\mathrm{Sc}_{g_{t}}-\mathrm{Sc}_{g}$, and $\left\|\left(\mathrm{Sc}_{g_{t}}-\mathrm{Sc}_{g}\right)\right\|_{L^{\frac{n}{2}}(M)}$ can be arbitrary small as $|t|$ sufficiently small. Therefore, for each $t$ such that $|t|$ is sufficiently small, by the asymptotic of $u_{t}$ as in (5.3), $\tilde{g}_{t}:=u_{t}^{\frac{4}{n-2}} g_{t}$ is a AF metric with a conically singular point at $o$ as in Definition 2.2. Because $u_{t}$ is a solution of (5.24), we have
$$\operatorname{Sc}_{\tilde{g}_{t}}=\frac{4(n-1)}{n-2}\left(u_{t}\right)^{-\frac{n+2}{n-2}}\left(-\Delta_{g_{t}} u_{t}+\frac{n-2}{4(n-1)} \operatorname{Sc}_{g_{t}} u_{t}\right)=\left(u_{t}\right)^{-\frac{4}{n-2}} \operatorname{Sc}_{g} \geq 0 .$$
Thus, Theorem 4.2 implies that the mass $m\left(\tilde{g}_{t}\right) \geq 0$, and so $t=0$ is a interior minimum point of the function $m\left(\tilde{g}_{t}\right)$, since $u_{0} \equiv 1, g_{0}=g$ and $m(g)=0$. As a result,
$$0=\left.\frac{d m\left(\tilde{g}_{t}\right)}{d t}\right|_{t=0}=\int_{M} h^{j k} \operatorname{Ric}_{j k} d \operatorname{vol}_{g}$$
which implies that $g$ is Ricci flat, since $h$ is arbitrary.
Now we prove that the cross section $\left(N, g^{N}\right)$ of the conical neighborhood of the singular point is the standard sphere. The idea is to compute the mass, $m(g)$, using the harmonic coordinate, $y_{i}$, obtained in Lemma 5.3, with the help of Ricci-flatness of $g$ that we have already obtained. As a consequence, $m(g)=0$ then implies that $d y_{i}$ are parallel 1-forms, and this then enables us to apply Obata's rigidity theorem for $\left(N, g^{N}\right)$.

Note that for an asymptotically conical metric, $g$, as in Definition 2.1, its Ricci tensor, $\operatorname{Ric}_{g}$, satisfies
$$\operatorname{Ric}_{g}(X, Y)=\operatorname{Ric}_{g^{N}}(X, Y)-(n-2) g^{N}(X, Y)+O\left(r^{\alpha}\right), \quad \text { as } \quad r \rightarrow 0,$$
for all $X, Y$ tangent to the cross section $N$. Recall that the decay order $\alpha>0$. Thus, $\operatorname{Ric}_{g}=0$, implies $\operatorname{Ric}_{g^{N}}=(n-2) g^{N}$ on the cross section. As a result, the Lichnerowicz eigenvalue estimate implies that the first nonzero eigenvalue of $\Delta_{g^{N}}, \lambda_{1} \geq n-1$.

Let $y_{i}, 1 \leq i \leq n$, be harmonic functions obtained in Lemma 5.3. By the asymptotic of $y_{i}$ at infinity as in (5.23), the argument as in the proof of Theorem 4.4 in [2] implies that we can compute the mass, $m(g)$, using $y_{i}$ as coordinate on $M_{\infty}$. In addition, by Bochner formula, recall that $g$ is Ricci flat, we have
$$\Delta_{g}\left(\frac{1}{2}\left|d y_{i}\right|^{2}\right)=\left|\nabla d y_{i}\right|^{2} .$$

Then by integrating by part, we have
$$\begin{aligned}
\omega_{n} m(g) & =\lim _{\rho \rightarrow \infty}\left[\sum_{i=1}^{n} \int_{\partial B_{\rho}} \partial_{\nu_{\rho}}\left(\frac{1}{2}\left|d y_{i}\right|^{2}\right)\right] \\
& =\lim _{r \rightarrow 0}\left[\sum_{i=1}^{n} \int_{\partial B_{r}} \partial_{\nu_{r}}\left(\frac{1}{2}\left|d y_{i}\right|^{2}\right)\right]+\lim _{r \rightarrow 0, \rho \rightarrow \infty}\left[\sum_{i=1}^{n} \int_{A_{r, \rho}}\left(\left|\nabla d y_{i}\right|^{2}\right)\right] \\
& =\sum_{i=1}^{n} \int_{M}\left(\left|\nabla d y_{i}\right|^{2}\right)
\end{aligned}$$
where $\nu_{\rho}$ and $\nu_{r}$ are the outer normal vector of $\partial B_{\rho}$ and $\partial B_{r}$ respectively, and $\omega_{n}$ is the volume of the unit sphere in $\mathbb{R}^{n}$. Here in the last step, we use that the asymptotic behavior of $y_{i}$ near the conical point as in (5.22) and the fact $\lambda_{1} \geq n-1$. As a result, $m(g)=0$ implies that $\nabla d y_{i}=0$, i.e. $d y_{i}$ is parallel. Then $\left|d y^{i}\right|=1$, since $d u_{i}=O\left(\rho^{-\tau}\right)$. Thus, by considering the asymptotic behavior of $d y_{i}$ near the conical point, the exponent in (5.22):
$$\frac{2-n+\sqrt{(n-2)^{2}+4 \lambda_{1}}}{2}=1,$$
because otherwise $\left|d y_{i}\right|$ will tend to either zero or infinity as $r \rightarrow 0$, i.e. as approaching to the conical point. Therefore, by solving (5.26), we obtain that $\lambda_{1}=n-1$ is an eigenvalue of $\Delta_{g^{N}}$. Then we apply the Obata's rigidity theorem to conclude that $\left(N, g^{N}\right)$ must be the standard sphere, since we have shown that $\operatorname{Ric}_{g^{N}}=(n-2) g^{N}$. As a consequence, the conically singular point $o$ is actually a manifold point, and our metric $g$ is continuous and has $W^{1, n}$-regularity near the conical singularity point, and so it satisfies the regularity assumption in [11]. By Theorem 1.1 in [11], we conclude that $\left(M^{n}, g\right) \cong\left(\mathbb{R}^{n}, g_{\mathbb{R}^{n}}\right)$. \(\square\)

Remark 5.5. In [5], for the proof of rigidity, after we get the manifold is Ricci flat, then we can construct the harmonic coordinate to conclude that the manifold is the Euclidean space as we do in the above.

\section*{References}
\begin{itemize}
\item[] [1] K. Akutagawa and B. Botvinnik. Yamabe metrics on cylindrical manifolds. Geom. Funct. Anal., 13(2):259-333, 2003.
\item[] [2] Robert Bartnik. The mass of an asymptotically flat manifold. Comm. Pure Appl. Math., 39(5):661-693, 1986.
\item[] [3] Hubert L. Bray and Jeffery L. Jauregui. A geometric theory of zero area singularities in general relativity. Asian J. Math., 17(3):525-560, 2013.
\item[] [4] Simone Cecchini and Rudolf Zeidler. The positive mass theorem and distance estimates in the spin setting. arXiv:2108.11972, 2021.
\item[] [5] Xianzhe Dai, Yukai Sun, and Changliang Wang. Positive mass theorem for asymptotically flat spin manifolds with isolated conical singularities. arXiv:2310.13285, 2023.
\end{itemize}
\begin{itemize}
\item[] [6] Xianzhe Dai and Changliang Wang. Perelman's W-functional on manifolds with conical singularities. Math. Res. Lett., 27(3):665-685, 2020.
\item[] [7] James D.E. Grant and Nathalie Tassotti. A positive mass theorem for low-regularity riemannian metrics. arXiv:1408.6425, pages 1-21, 2014.
\item[] [8] Marc Herzlich. A Penrose-like inequality for the mass of Riemannian asymptotically flat manifolds. Comm. Math. Phys., 188(1):121-133, 1997.
\item[] [9] Marc Herzlich. Minimal surfaces, the Dirac operator and the Penrose inequality. Séminaire de Théorie Spectrale et Géométrie, Univ. Grenoble I, Saint-Martin-d'Hères, 20:9-16, 2002.
\item[] [10] Sven Hirsch and Pengzi Miao. A positive mass theorem for manifolds with boundary. Pac. J. Math, 306(1):185-201, 2020.
\item[] [11] Wenshuai Jiang, Weimin Sheng, and Huaiyu Zhang. Removable singularity of positive mass theorem with continuous metrics. Math. Z., 302(2):839-874, 2022.
\item[] [12] Tao Ju and Jeff Viaclovsky. Conformally prescribed scalar curvature on orbifolds. Comm. Math. Phys., 398(2):877-923, 2023.
\item[] [13] Dan Lee. A positive mass theorem for Lipschitz metrics with small singular sets. Proc. Am. Math. Soc., 14:3997-4004, 2013.
\item[] [14] Dan A. Lee and Philippe G. LeFloch. The positive mass theorem for manifolds with distributional curvature. Comm. Math. Phys., 339(1):99-120, 2015.
\item[] [15] Dan A. Lee, Martin Lesourd, and Ryan Unger. Density and positive mass theorems for incomplete manifolds. Calc. Var. Partial Differential Equations, 62(7):Paper No. 194, 23, 2023.
\item[] [16] Martin Lesourd, Ryan Unger, and Shing-Tung Yau. The positive mass theorem with arbitrary ends. To appear in J. Differential Geometry, 2021.
\item[] [17] Chao Li and Christos Mantoulidis. Positive scalar curvature with skeleton singularities. Math. Ann., 374:99-131, 2019.
\item[] [18] James Lucietti. All higher-dimensional Majumdar-Papapetrou black holes. Ann. Henri Poincaré, 22(7):2437-2450, 2021.
\item[] [19] Donovan McFeron and Gábor Székelyhidi. On the positive mass theorem for manifolds with corners. Comm. Math. Phys., 313(2):425-443, 2012.
\item[] [20] Pengzi Miao. Positive mass theorem on manifolds admitting corners along a hypersurface. Adv. Theor. Math. Phys., 6(6):1163-1182, 2002.
\item[] [21] Pengzi Miao. Implications of some mass-capacity inequalities. arXiv:2307.06428v2, 2023.
\item[] [22] Pengzi Miao. Mass, capacitary functions, and the mass-to-capacity ratio. Peking Mathematical Journal, 2023.
\item[] [23] Vincent Minerbe. A mass for ALF manifolds. Comm. Math. Phys., 289(3):925-955, 2009.
\item[] [24] Richard Schoen. Conformal deformation of a Riemannian metric to constant scalar curvature. J. Differential Geometry, 20:479-495, 1984.
\item[] [25] Richard Schoen and Shing Tung Yau. On the proof of the positive mass conjecture in general relativity. Comm. Math. Phys., 65:45-76, 1979.
\item[] [26] Richard Schoen and Shing Tung Yau. Positive scalar curvature and minimal hypersurface singularities. Surveys in Differential Geometry, XXIV:441-480, 2021.
\item[] [27] Yuguang Shi and Luen-Fai Tam. Scalar curvature and singular metrics. Pacific J. Math., 293(2):427-470, 2018.
\item[] [28] Edward Witten. A new proof of the positive energy theorem. Comm. Math. Phys., 80:381-402, 1981.
\item[] [29] Jintian Zhu. Positive mass theorem with arbitrary ends and its application. Int. Math. Res. Not. IMRN, (11):9880-9900, 2023.
\end{itemize}

Department of Mathematics, University of Californai, Santa Barbara CA93106, USA
Email address: dai@math.ucsb.edu
Key Laboratory of Pure and Applied Mathematics, School of Mathematical Sciences, Peking University, Beijing, 100871, P. R. China
Email address: sunyukai@math.pku.edu.cn
School of Mathematical Sciences and Institute for Advanced Study, Tongji University, Shanghai 200092, China
Email address: wangchl@tongji.edu.cn
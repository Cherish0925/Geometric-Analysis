---
retention_scope: session
part: 1
total_parts: 2
---

[Part 1/2 of: Deformation theory of scalar-flat Kähler ALE surfaces]

---
source_file: 1605_05267.pdf
converter: mathpix
format: mmd
---

\title{
DEFORMATION THEORY OF SCALAR-FLAT KÄHLER ALE SURFACES
}

\author{
JIYUAN HAN AND JEFF A. VIACLOVSKY
}

\begin{abstract}
We prove a Kuranishi-type theorem for deformations of complex structures on ALE Kähler surfaces. This is used to prove that for any scalar-flat Kähler ALE surface, all small deformations of complex structure also admit scalar-flat Kähler ALE metrics. A local moduli space of scalar-flat Kähler ALE metrics is then constructed, which is shown to be universal up to small diffeomorphisms (that is, diffeomorphisms which are close to the identity in a suitable sense). A formula for the dimension of the local moduli space is proved in the case of a scalar-flat Kähler ALE surface which deforms to a minimal resolution of $\mathbb{C}^{2} / \Gamma$, where $\Gamma$ is a finite subgroup of U(2) without complex reflections.
\end{abstract}

\section*{1. Introduction}

This article is concerned with the following class of metrics:
Definition 1.1. An ALE Kähler surface $(X, g, J)$ is a Kähler manifold of complex dimension 2 with the following property. There exists a compact subset $K \subset X$ and a diffeomorphism $\psi: X \backslash K \rightarrow\left(\mathbb{R}^{4} \backslash \bar{B}\right) / \Gamma$, such that for each multi-index $\mathcal{I}$ of order $|\mathcal{I}|$
$$\partial^{\mathcal{I}}\left(\psi_{*}(g)-g_{E u c}\right)=O\left(r^{-\mu-|\mathcal{I}|}\right),$$
as $r \rightarrow \infty$, where $\Gamma$ is a finite subgroup of U(2) containing no complex reflections, $B$ denotes a ball centered at the origin, and $g_{\text {Euc }}$ denotes the Euclidean metric. The real number $\mu$ is called the order of $g$.

Remark 1.2. In this paper, henceforth $\Gamma$ will always be a finite subgroup of $\mathrm{U}(2)$ containing no complex reflections.

We are interested in the class of scalar-flat Kähler ALE metrics. These are interesting since they are extremal in the sense of Calabi [Cal85], and they arise as "bubbles" in gluing constructions for extremal Kähler metrics [ALM15, ALM16, AP06, APS11, BR15, RS05, [RS09]. In the case of scalar-flat Kähler ALE metrics, it is known that there exists an ALE coordinate system for which the order of such a metric is at least 2 [LM08].

We note that for an ALE Kähler metric of order $\mu$, there exist ALE coordinates for which
$$\partial^{\mathcal{I}}\left(J-J_{E u c}\right)=O\left(r^{-\mu-|\mathcal{I}|}\right),$$
for any multi-index $\mathcal{I}$ as $r \rightarrow \infty$, where $J_{\text {Euc }}$ is the standard complex structure on Euclidean space [HL16].

There are many known examples of scalar-flat Kähler ALE metrics. In the case that $\Gamma \subset \operatorname{SU}(2)$, Kronheimer constructed and classified the hyperkähler ALE metrics Kro89a, Kro89b]. Calderbank-Singer constructed a family of scalar-flat Kähler ALE metrics on the

\footnotetext{
The authors were partially supported by NSF Grant DMS-1405725. This paper was completed while the authors were in residence at Mathematical Sciences Research Institute in Berkeley, California. The authors would like to thank MSRI for their support, and for providing such an excellent working environment.
}
minimal resolution of any cyclic quotient singularity [CS04]. For the remaining subgroups of U(2), the existence of scalar-flat Kähler metrics on the minimal resolution of $\mathbb{C}^{2} / \Gamma$, was shown by Lock-Viaclovsky [LV14].

The question we address in this paper is whether the scalar-flat Kähler property is preserved under small deformations of complex structure. In the cases where $\Gamma \subset \operatorname{SU}(2)$, the hyperkähler quotient construction produces hyperkähler metrics for the minimal resolution complex structure as well as for all small deformations of the minimal resolution complex structure. In the case of the LeBrun negative mass metrics, using arguments from twistor theory, Honda has shown that all small deformations of the complex structure on $\mathcal{O}(-n)$ also admit scalar-flat Kähler metrics [Hon13, Hon14]. For the case of general $\Gamma$, in [LV14], employing Honda's result, it was shown that some of small deformations of complex structure admit scalar-flat Kähler ALE metrics.

Our main result in this paper shows that for any scalar-flat Kähler ALE surface, all small deformations of complex structure admit scalar-flat Kähler ALE metrics. Our proof is analytic in nature, and in particular, gives a new analytic proof of Honda's result on $\mathcal{O}(-n)$ mentioned above.

To state our result precisely, we next recall some basic facts regarding deformations of complex structures. For a complex manifold $(X, J)$, let $\Lambda^{p, q}$ denote the bundle of $(p, q)$-forms, and let $\Theta$ denote the holomorphic tangent bundle. The deformation complex corresponds to a real complex as shown in the commutative diagram
![](https://cdn.mathpix.com/cropped/3315e6a0-8cb3-4716-9517-4535b74fdcda-02.jpg?height=223&width=1358&top_left_y=1289&top_left_x=425)
where $\mathfrak{L}_{Z} J$ is the Lie derivative of $J$,
$$\operatorname{End}_{a}(T X)=\{I \in \operatorname{End}(T X): I J=-J I\},$$
and $N_{J}^{\prime}$ is the linearization of Nijenhuis tensor
$$N(X, Y)=2\{[J X, J Y]-[X, Y]-J[X, J Y]-J[J X, Y]\}$$
at $J$. Each isomorphism $R e$ is simply taking the real part of a section. If $g$ is a Hermitian metric compatible with $J$, then let □ denote the $\bar{\partial}$-Laplacian
$$\square \equiv \bar{\partial}^{*} \bar{\partial}+\bar{\partial} \bar{\partial}^{*},$$
where $\bar{\partial}^{*}$ denotes the formal $L^{2}$-adjoint. Each complex bundle in the diagram (1.3) admits a □-Laplacian, and these correspond to real Laplacians on each real bundle in (1.3). We will use the same □ -notation for these real Laplacians.

To state our most general result, we need the following definition. This is necessary because there is a gauge freedom of Euclidean motions in the definition of ALE coordinates.

Definition 1.3. Let $(X, g, J)$ be a Kähler ALE surface. For any bundle $E$ in the diagram (1.3), and $\tau \in \mathbb{R}$, define
$$\mathcal{H}_{\tau}(X, E)=\left\{\theta \in \Gamma(X, E): \square \theta=0, \theta=O\left(r^{\tau}\right) \text { as } r \rightarrow \infty\right\} .$$

Define
$$\mathbb{W}=\left\{Z \in \mathcal{H}_{1}(X, T X) \mid \mathfrak{L}_{Z} g=O\left(r^{-1}\right), \mathfrak{L}_{Z} J=O\left(r^{-3}\right), \text { as } r \rightarrow \infty\right\} .$$
Finally, define the real subspace
$$\mathcal{H}_{e s s}\left(X, \operatorname{End}_{a}(T X)\right) \subset \mathcal{H}_{-3}\left(X, \operatorname{End}_{a}(X)\right)$$
(ess is short for essential) to be the $L^{2}$-orthogonal complement in $\mathcal{H}_{-3}\left(X, \operatorname{End}_{a}(X)\right)$ of the subspace
$$\mathbb{V}=\left\{\theta \in \mathcal{H}_{-3}\left(X, \operatorname{End}_{a}(T X)\right) \mid \theta=J \circ \mathfrak{L}_{Z} J, Z \in \mathbb{W}\right\} .$$

Our main result is the following.
Theorem 1.4. Let $(X, g, J)$ be a scalar-flat Kähler ALE surface. Let $-2<\delta<-1$, $0<\alpha<1$, and $k$ an integer with $k \geq 4$ be fixed constants. Let $B_{\epsilon_{1}}^{1}$ denote an $\epsilon_{1}$-ball in $\mathcal{H}_{\text {ess }}\left(X, \operatorname{End}_{a}(T X)\right), B_{\epsilon_{2}}^{2}$ denote an $\epsilon_{2}$-ball in $\mathcal{H}_{-3}\left(X, \Lambda^{1,1}\right)$ (both using the $L^{2}$-norm). Then there exists $\epsilon_{1}>0$ and $\epsilon_{2}>0$ and a family $\mathfrak{F}$ of scalar-flat Kähler metrics near $g$, parametrized by $B_{\epsilon_{1}}^{1} \times B_{\epsilon_{2}}^{2}$, that is, there is a differentiable mapping
$$F: B_{\epsilon_{1}}^{1} \times B_{\epsilon_{2}}^{2} \rightarrow \operatorname{Met}(X),$$
into the space of smooth Riemannian metrics on $X$, with $\mathfrak{F}=F\left(B_{\epsilon_{1}}^{1} \times B_{\epsilon_{2}}^{2}\right)$ satisfying the following "versal" property: there exists a constant $\epsilon_{3}>0$ such that for any scalar-flat Kähler metric $\tilde{g} \in B_{\epsilon_{3}}(g)$, there exists a diffeomorphism $\Phi: X \rightarrow X, \Phi \in C_{\text {loc }}^{k+1, \alpha}$, such that $\Phi^{*} \tilde{g} \in \mathfrak{F}$, where
$$B_{\epsilon_{3}}(g)=\left\{g^{\prime} \in C_{l o c}^{k, \alpha}\left(S^{2}\left(T^{*} X\right)\right) \mid\left\|g-g^{\prime}\right\|_{C_{\delta}^{k, \alpha}\left(S^{2}\left(T^{*} X\right)\right)}<\epsilon_{3}\right\} .$$

Remark 1.5. The norm in (1.12) is a certain weighted Hölder norm, see Section 2 for the precise definition. For a more precise description of the diffeomorphism $\Phi$, see Theorem 9.2 below.

In order to state our next result, we must recall some facts about vector fields and diffeomorphisms. If $(X, g)$ is an ALE metric, and $Y$ is a vector field on $X$, the Riemannian exponential mapping $\exp _{p}: T_{p} X \rightarrow X$ induces a mapping
$$\Phi_{Y}: X \rightarrow X$$
by
$$\Phi_{Y}(p)=\exp _{p}(Y) .$$
If $Y \in C_{s}^{k, \alpha}(T X)$ has sufficiently small norm, ( $s<0$ and $k$ will be determined in specific cases) then $\Phi_{Y}$ is a diffeomorphism. We will use the correspondence $Y \mapsto \Phi_{Y}$ to parametrize a neighborhood of the identity, analogous to [Biq06].

Definition 1.6. We say that $\Phi: X \rightarrow X$ is a small diffeomorphism if $\Phi$ is of the form $\Phi=\Phi_{Y}$ for some vector field $Y$ satisfying
$$\|Y\|_{C_{\delta+1}^{k+1, \alpha}}<\epsilon_{4}$$
for some $\epsilon_{4}>0$ sufficiently small which depends on $\epsilon_{3}$.

The family $\mathfrak{F}$ is not necessarily "universal", because some elements in $\mathfrak{F}$ might be isometric. However, the following theorem shows that after taking a quotient by an action of the holomorphic isometries of the central fiber $(X, g, J)$, the family $\mathfrak{F}$ is in fact universal (up to small diffeomorphisms).
Theorem 1.7. Let $(X, g, J)$ be as in Theorem 1.4, and let $\mathfrak{G}$ denote the group of holomorphic isometries of $(X, g, J)$. Then there is an action of $\mathfrak{G}$ on $\mathfrak{F}$ with the following properties.
\begin{itemize}
\item[-] Two metrics in $\mathfrak{F}$ are isometric if they are in the same orbit of $\mathfrak{G}$.
\item[-] If two metrics in $\mathfrak{F}$ are isometric by a small diffeomorphism then they must be the same.
\end{itemize}

Since each orbit represents a unique isometry class of metric (up to small diffeomorphism), we will refer to the quotient $\mathfrak{M}=\mathfrak{F} / \mathfrak{G}$ as the "local moduli space of scalar-flat Kähler ALE metrics near $g$." The local moduli space $\mathfrak{M}$ is not a manifold in general, but its dimension is in fact well-defined, and we define
$$m=\operatorname{dim}(\mathfrak{M}) .$$

Remark 1.8. We should point out that our local moduli space of metrics contains small rescalings, i.e, $g \mapsto \frac{1}{c^{2}} g(c \cdot, c \cdot)$ for $c$ close to 1. If one considers scaled metrics as equivalent (which we do not), then the dimension would decrease by 1.
1.1. Deformations of the minimal resolution. As mentioned above, there are families of examples of scalar-flat Kähler ALE metrics on minimal resolutions of isolated quotient singularities. For convenience, we next recall the definition of a minimal resolution.

Definition 1.9. Let $\Gamma \subset \mathrm{U}(2)$ be as above. Then, a smooth complex surface $X$ is called a minimal resolution of $\mathbb{C}^{2} / \Gamma$ if there is a mapping $\pi: X \rightarrow \mathbb{C}^{2} / \Gamma$ such that the restriction $\pi: X \backslash \pi^{-1}(0) \rightarrow \mathbb{C}^{2} / \Gamma \backslash\{0\}$ is a biholomorphism, and $\pi^{-1}(0)$ is a divisor in $X$ containing no -1 curves. The divisor $\pi^{-1}(0)$ is called the exceptional divisor.

In the cyclic case, the exceptional divisor is a string of rational curves with normal crossing singularities. In the case that $\Gamma$ is non-cyclic, it was shown by Brieskorn, see [Bri68], that the exceptional divisor is a tree of rational curves with normal crossing singularities. There are three Hirzebruch-Jung strings attached to a single curve, called the central rational curve. The self-intersection number of this curve will be denoted $-b_{\Gamma}$, and the total number of rational curves will be denoted by $k_{\Gamma}$.

A specialized version of Theorem 1.4 is the following.
Theorem 1.10. Let $(X, g, J)$ be any scalar-flat Kähler ALE metric on the minimal resolution of $\mathbb{C}^{2} / \Gamma$, where $\Gamma \subset \mathrm{U}(2)$ is as above. Define
$$j_{\Gamma}=2 \sum_{i=1}^{k_{\Gamma}}\left(e_{i}-1\right),$$
where $-e_{i}$ is the self-intersection number of the ith rational curve, and $k_{\Gamma}$ is the number of rational curves in the exceptional divisor, and let
$$d_{\Gamma}=j_{\Gamma}+k_{\Gamma} .$$
Then there is a family, $\mathfrak{F}$, parametrized by a ball in $\mathbb{R}^{d_{\Gamma}}$, of scalar-flat Kähler metrics near $g$ with the "versal" property stated in Theorem 1.4.

We let $m_{\Gamma}$ denote the dimension of the moduli space near the minimal resolution of $\mathbb{C}^{2} / \Gamma$, where the dimension is defined in (1.16). Note $m_{\Gamma}<d_{\Gamma}$ due to the action of the automorphism group, and $m_{\Gamma}$ can be explicitly computed for all groups $\Gamma$, but those computations will not be done here.

Remark 1.11. The dimension of the moduli space of hyperkähler metrics is known to be $3 k-3$ in the $A_{k}, D_{k}$ and $E_{k}$ cases for $k \geq 2$, and equal to 1 in the $A_{1}$ case [Kro86]. Our method of parametrizing by complex structures and Kähler classes overcounts in this case (i.e., $F$ is not injective), since a hyperkähler metric is Kähler with respect to a 2-sphere of complex structures.

Our final result applies to a generic deformation of the minimal resolution.
Theorem 1.12. Let $(X, g, J)$ be any scalar-flat Kähler ALE surface which deforms to the minimal resolution of $\mathbb{C}^{2} / \Gamma$ through a path $\left(X, g_{t}, J_{t}\right)(0 \leq t \leq 1)$, where $g_{1}=g, g_{0}$ is the minimal resolution, and $\left\|g_{t}-g_{s}\right\|_{C_{\delta}^{k, \alpha}\left(g_{0}\right)} \leq C \cdot|s-t|$ with $C>0$ a uniform constant for any $0 \leq s, t \leq 1, k \geq 4,-2<\delta<-1$. If $\mathfrak{G}(g)=\{e\}$ then the local moduli space $\mathfrak{F}$ is smooth near $g$ and is a manifold of dimension $m=m_{\Gamma}$.

Remark 1.13. It was recently shown that Kähler ALE surface with group $\Gamma \subset \mathrm{U}(2)$ is birational to a deformation of $\mathbb{C}^{2} / \Gamma$ [HRŞ16]. There are several possible components of the deformation of such a cone, here we consider surfaces in the "Artin component" of deformations of $\mathbb{C}^{2} / \Gamma$. We note however that there are some known examples of scalar-flat Kähler metrics on non-Artin components, which are free quotients of hyperkähler metrics of $A_{k}$-type, see for example [Suv12].

We end the introduction with an outline of the paper. In Section 2, we begin with the definitions of the weighted Hölder spaces which will be used throughout the paper. Then, in Section 3 we give some analysis of the complex analytic compactifications, due to Hein-LeBrun-Maskit [HL16, LM08], of Kähler ALE spaces. In Section 4, we study the deformation of complex structures using an adaptation of Kuranishi's theory to ALE spaces. The main point is that since the manifold is non-compact, the sheaf cohomology group $H^{1}(X, \Theta)$ should be replaced by an appropriate space of decaying harmonic forms. In Section 5, several key results about gauging and diffeomorphisms are proved, which are used to prove "versality" of the family constructed in Section 4. In Section 6, a refined gauging procedure is carried out, to construct the Kuranishi family of "essential" deformations. In Section 7, we generalize Kodaira-Spencer's stability theorem for Kähler structures to the ALE setting, using some arguments of Biquard-Rollin [BR15]. In Section 8, we adapt the LeBrun-Singer-Simanca theory of deformations of extremal Kähler metrics to the ALE setting [LS93, LS94]. In Section 9, we prove the versal property of the family $\mathfrak{F}$, using a local slicing theorem, and prove Theorem 1.7. In Section 10, we restrict attention to the minimal resolution, and prove Theorems 1.10 and 1.12.
1.2. Acknowledgements. The authors would like to thank Olivier Biquard, Ronan Conlon, Akira Fujiki, Ryushi Goto, Hans-Joachim Hein, Nobuhiro Honda, and Claude LeBrun, for numerous helpful discussions on deformations of complex structures. Olivier Biquard, Joel Fine, and Jason Lotay provided crucial assistance with the slicing arguments. We would also like to thank Michael Lock for valuable discussions on properties of subgroups of U(2).

Finally, the authors would like to thank to the anonymous referee for detailed helpful remarks, and for suggesting numerous improvements to the paper.

\section*{2. Notation}

We begin with the definition of weighted Hölder spaces, which will be used throughout the paper.

Definition 2.1. Let $E$ be a tensor bundle on $X$, with Hermitian metric $\|\cdot\|_{h}$. Let $\varphi$ be a smooth section of $E$. We fix a point $p_{0} \in X$, and define $r(p)$ to be the distance between $p_{0}$ and $p$. Then define
$$\begin{aligned}
\|\varphi\|_{C_{\delta}^{0}} & :=\sup _{p \in X}\left\{\|\varphi(p)\|_{h} \cdot(1+r(p))^{-\delta}\right\} \\
\|\varphi\|_{C_{\delta}^{k}} & :=\sum_{|\mathcal{I}| \leq k} \sup _{p \in X}\left\{\left\|\nabla^{\mathcal{I}} \varphi(p)\right\|_{h} \cdot(1+r(p))^{-\delta+|\mathcal{I}|}\right\},
\end{aligned}$$
where $\mathcal{I}=\left(i_{1}, \ldots, i_{n}\right),|\mathcal{I}|=\sum_{j=1}^{n} i_{j}$. Next, define
$$[\varphi]_{C_{\delta-\alpha}^{\alpha}}:=\sup _{0<d(x, y)<\rho_{i n j}}\left\{\min \{r(x), r(y)\}^{-\delta+\alpha} \frac{\|\varphi(x)-\varphi(y)\|_{h}}{d(x, y)^{\alpha}}\right\},$$
where $0<\alpha<1, \rho_{i n j}$ is the injectivity radius, and $d(x, y)$ is the distance between $x$ and $y$. The meaning of the tensor norm is to use parallel transport along the unique minimal geodesic from $y$ to $x$, and then take the norm of the difference at $x$. The weighted Hölder norm is defined by
$$\|\varphi\|_{C_{\delta}^{k, \alpha}}:=\|\varphi\|_{C_{\delta}^{k}}+\sum_{|\mathcal{I}|=k}\left[\nabla^{\mathcal{I}} \varphi\right]_{C_{\delta-k-\alpha}^{\alpha}},$$
and the space $C_{\delta}^{k, \alpha}(X, E)$ is the closure of $\left\{\varphi \in C^{\infty}(X, E):\|\varphi\|_{C_{\delta}^{k, \alpha}}<\infty\right\}$.
Remark 2.2. The dual space of Hölder space is not a Hölder space, but for the purpose of computing the dimension of cokernel of a Fredholm operator of order $o$,
$$H: C_{\delta}^{k, \alpha} \rightarrow C_{\delta-o}^{k-o, \alpha}$$
we consider the adjoint operator as mapping between Hölder spaces
$$H^{*}: C_{-4-\delta+o}^{k, \alpha} \rightarrow C_{-4-\delta}^{k-o, \alpha},$$
since the adjoint weight to weight $\delta$ is $-4-\delta$, and using elliptic regularity.

\section*{3. ALE Kähler surfaces}

In this section, we will prove several results about ALE Kähler surfaces which will be needed later. We note that the results in this section do not use the scalar-flat assumption.

In [LM08, HL16], LeBrun-Maskit and Hein-LeBrun analyzed the asymptotic behavior of the metric and complex structure near infinity of ALE Kähler surfaces. The next proposition gives a summary of their results. (See also [Li14] for other related results on complex analytic compactifications).

Proposition 3.1 (Hein-LeBrun-Maskit). Let $X_{\infty}$ be an end of an ALE Kähler surface $(X, g, J)$ with metric $g$ asymptotic to Euclidean metric at rate
$$\left.\mid \nabla_{E u c}^{\mathcal{I}}\left(g_{j, k}-\delta_{j, k}\right)\right) \mid=O\left(\rho^{-|\mathcal{I}|-1-\epsilon}\right)$$
for $|\mathcal{I}|=0,1$ if $\epsilon>1 / 2$ or for $|\mathcal{I}|=0, \ldots, 4$ if $\epsilon \in(0,1 / 2]$; here $\nabla_{\text {Euc }}$ denotes the Euclidean derivative. Then there is a surface $S$ containing an embedded holomorphic curve $C \simeq \mathbb{C P}^{1}$ with self-intersection 1, such that the universal cover $\tilde{X}_{\infty}$ of $X_{\infty}$ is biholomorphic to $S \backslash C$.

Let $(X, g, J)$ be a Kähler ALE surface, then $X$ has one end and can be analytically compactified to a smooth compact surface $\hat{X}$ by adding a tree of rational curves $E_{\infty}$. The surface $\hat{X}$ is a rational surface or a ruled surface. Also, $X$ can be compactified to an orbifold surface $\hat{X}_{\text {orb }}$ by adding a single rational curve at $\infty$.

Furthermore, if the order of $g$ satisfies $1<\mu<3$, then there exists an $A L E$ coordinate, under which $\left|J-J_{\text {Euc }}\right|=O\left(r^{-3}\right),\left|g-g_{\text {Euc }}\right|=O\left(r^{-\mu}\right)$.

Remark 3.2. The orbifold compactification $\hat{X}_{\text {orb }}$ has cyclic singularities on the rational curve at $\infty$. The smooth compactification $\hat{X}$ is obtained from $\hat{X}_{\text {orb }}$ by resolving these singularities.

Consider the space of holomorphic vector fields on $X$ with at most growth of order $\tau$
$$\mathcal{Z}_{\tau}(X, \Theta)=\left\{Z \in \Gamma(X, \Theta) \mid \bar{\partial} Z=0, Z=O\left(r^{\tau}\right) \text { as } r \rightarrow \infty\right\} .$$
The first vanishing result we need is the following.
Proposition 3.3. Let $(X, g, J)$ be an ALE Kähler surface. If $\tau<0$ then
$$\operatorname{dim} \mathcal{Z}_{\tau}(X, \Theta)=0 .$$
Proof. Let $X_{\infty}=X \backslash \overline{B(R)}$. Let $R$ be sufficiently large, then by Proposition 3.1, the universal cover $\tilde{X}_{\infty}$ can be analytically compactified by adding a rational curve $C$ at infinity, where $C$ has self-intersection +1. By [HL16], there exists a smooth map $\left[\xi_{1}, \xi_{2}, f\right]$ that maps $S=\tilde{X}_{\infty} \cup C$ to $\mathbb{C P}^{2}$, which maps $C$ holomorphically to $\{f=0\}$ as a curve $\mathbb{C P}^{1} \subset \mathbb{C P}^{2}$, where
$$\xi_{j}=\{\text { holomorphic part }\}+O\left(|f|^{3}\right),$$
as $f \rightarrow 0$. Let
$$z_{j}=x_{j}+\sqrt{-1} y_{j}=\frac{\xi_{j}}{f},(j=1,2)$$
where $\left\{x_{1}, y_{1}, x_{2}, y_{2}\right\}$ gives an ALE coordinate on $\tilde{X}_{\infty}$, and $\left|J-J_{\text {Euc }}\right|=O\left(|z|^{-3}\right)$ as $z \rightarrow \infty$. Let
$$(v, w)=\left(\frac{1}{z_{1}}, \frac{z_{2}}{z_{1}}\right)$$
where $\{v=0\}$ represents the complement of one point in $C$.
First, let $\sigma$ be a decaying holomorphic vector field on $X$, which can be lifted to $\tilde{\sigma}$ on $\tilde{X}_{\infty}$. Note that $\tilde{\sigma}$ can be extended to $\mathbb{C}^{2}$ smoothly by using a cut-off function. Since $\bar{\partial}-\bar{\partial}_{E u c}=O\left(|z|^{-3}\right)$ and $\bar{\partial} \tilde{\sigma}=0$ on $\tilde{X}_{\infty}$,
$$\bar{\partial}_{E u c} \tilde{\sigma}=\sum_{i, j} h_{i, j} d \bar{z}_{i} \otimes \frac{\partial}{\partial z_{j}}=O\left(|z|^{-3}|\sigma|\right),$$
as $z \rightarrow \infty$. By using the $\bar{\partial}_{E u c}$-Poincaré lemma, there exist
$$p_{j}=O\left(|z|^{-2} \sigma\right) \in C^{\infty}\left(\mathbb{C}^{2}\right), \bar{\partial}_{E u c} p_{j}=\sum_{i} h_{i, j} d \bar{z}_{i}$$
The formula for $p_{j}$ can be written out explicitly as follows. Let
$$\begin{aligned}
& q_{j}=\frac{1}{2 \pi \sqrt{-1}} \int_{\mathbb{C}} h_{2, j}\left(z_{1}, \zeta_{2}\right) \frac{d \zeta_{2} \wedge d \bar{\zeta}_{2}}{\zeta_{2}-z_{2}} \\
& q_{j}^{\prime}=\frac{1}{2 \pi \sqrt{-1}} \int_{\mathbb{C}}\left(h_{1, j}-\bar{\partial}_{1} q_{j}\right)\left(\zeta_{1}, z_{2}\right) \frac{d \zeta_{1} \wedge d \bar{\zeta}_{1}}{\zeta_{1}-z_{1}}
\end{aligned}$$
where the integral formula is valid since $h_{i, j}=o\left(|z|^{-3}\right)$. Then $p_{j}=q_{j}+q_{j}^{\prime}$. Then we have $\tilde{\sigma}-\sum_{j} p_{j} \frac{\partial}{\partial z_{j}}$ is a decaying $\bar{\partial}_{E u c}$-holomorphic vector field on $\mathbb{C}^{2}$, which must vanish identically. The growth rate of $\sigma$ can be dropped by 2 iteratively by this argument, so we can assume that $\sigma$ decays at any rate in the coordinates $\left\{z_{1}, z_{2}\right\}$.

On $\tilde{X}_{\infty}$, there exists a holomorphic (2, 0)-form $\Omega=d z_{1} \wedge d z_{2}+O\left(|z|^{-2+\epsilon}\right)$ as $|z| \rightarrow \infty$. Let $\tilde{\sigma}^{*} \in \Gamma\left(\tilde{X}_{\infty}, \Omega^{1}\right)$ denote the contraction of $\tilde{\sigma}$ with $\Omega$. The section $\tilde{\sigma}^{*}$ is also holomorphic and we have $\tilde{\sigma}^{*}=O\left(|z|^{-10}\right)$ as $z \rightarrow \infty$ since we can assume $\tilde{\sigma}$ decays to any order. The coordinate change gives: $d z_{1}=\frac{-1}{v^{2}} d v, d z_{2}=\frac{1}{v} d w-\frac{w}{v^{2}} d v,|z|^{2}=\frac{1}{|v|^{2}}\left(1+|w|^{2}\right)$. Then $\tilde{\sigma}^{*}=O\left(|v|^{8}\right)$ near $C$ and can be extended to $C$ with $\tilde{\sigma}^{*}=0$ on $C$. Consider the exact sequence
$$\left.0 \rightarrow N_{C}^{*} \rightarrow \Omega^{1}\right|_{C} \rightarrow \Omega^{1}(C) \rightarrow 0,$$
where $\left.\Omega^{1}\right|_{C}$ is the restriction of the bundle $\Omega^{1}$ on $C, \Omega^{1}(C)$ is the cotangent bundle of $C$ and $N_{C}$ is the normal bundle of $C$ in $S$. Then we have $\left.\Omega^{1}\right|_{C}=\mathcal{O}(-2) \oplus \mathcal{O}(-1)$. This implies $\tilde{\sigma}^{*}$ vanishes on any rational curve with self-intersection +1 on $S$. Since $C$ has self-intersection $+1, H^{1}\left(C, N_{C}^{*} \otimes \Theta(C)\right)=0$, so $C$ is rigid in $S$. Then there is an open neighborhood $U \subset S$ of $C$, such that $\tilde{\sigma}^{*}$ vanishes identically over $U$. Then $\sigma$ vanishes on an open subset of $X$, which implies that $\sigma$ vanishes identically on $X$. \(\square\)

Next, we consider harmonic (0, 2)-forms with values in the holomorphic tangent bundle.
Proposition 3.4. Let $X$ be a Kähler ALE surface. If $\delta<0$, then $\mathcal{H}_{\delta}\left(X, \Lambda^{0,2} \otimes \Theta\right)=0$.
Proof. The proposition follows an argument in [LM08, Theorem 4.2], with minor modifications. For completeness, we give a proof here following their idea. Let $\sigma \in \mathcal{H}_{\delta}\left(X, \Lambda^{0,2} \otimes \Theta\right)$. Recall that the conjugated Hodge star operator $\bar{*}$ maps $\sigma$ to a □ -harmonic form $\sigma^{*} \in$ $\mathcal{H}_{\delta}\left(X, \Lambda^{2,0} \otimes \Omega^{1}\right)$. Let $\tilde{\sigma}^{*}$ be its lifting on $\tilde{X}_{\infty}$. Following the same notion as in the proof of Proposition 3.3, we have
$$\tilde{\sigma}^{*}=\sum_{j} a_{j} d z_{1} \wedge d z_{2} \otimes d z_{j}+O\left(|z|^{-3}\left|\tilde{\sigma}^{*}\right|\right)$$
where $a_{j}$ are $\bar{\partial}_{E u c}$-holomorphic functions and $a_{j}=O\left(|z|^{\delta}\right)$ as $z \rightarrow \infty$. As shown in the proof of Proposition 3.3, $a_{j}=0$, so $\tilde{\sigma}^{*}=O\left(|z|^{\delta-3}\right)$ as $z \rightarrow \infty$. Since the growth rate of $\tilde{\sigma}^{*}$ can be dropped by 3 iteratively, $\tilde{\sigma}^{*}$ can decay to any order under the coordinate of $\left\{z_{1}, z_{2}\right\}$, then $\tilde{\sigma}^{*}$ can be extended to $C$ with $\tilde{\sigma}^{*}=0$ on $C$. Since
$$\left.\Omega^{2,0} \otimes \Omega^{1}\right|_{C}=\left(\Omega^{1}(C) \oplus N_{C}^{*}\right) \otimes\left(\Omega^{2,0}(C) \otimes N_{C}^{*}\right),$$
we have
$$\left.\Omega^{2,0} \otimes \Omega^{1}\right|_{C}=(\mathcal{O}(-2) \oplus \mathcal{O}(-1)) \otimes(\mathcal{O}(-2) \otimes \mathcal{O}(-1))=\mathcal{O}(-5) \oplus \mathcal{O}(-4) .$$
This implies that $\tilde{\sigma}^{*}$ vanishes on any rational curve with self-intersection +1 on $\tilde{X}_{\infty}$. By the same argument as in Proposition 3.3, there is an open neighborhood $U \subset S$ of $C$, such that $\tilde{\sigma}^{*}$ vanishes identically over $U$. Then $\sigma$ vanishes on an open subset of $X$, which implies that $\sigma$ vanishes identically on $X$. \(\square\)

The next proposition shows that $\mathcal{H}_{\delta}\left(X, \Lambda^{0,1} \otimes \Theta\right)$ automatically has a faster decaying rate.
Proposition 3.5. Let $X$ be an ALE Kähler surface, and $\hat{X}$ be its analytic compactification. Then for any $-3<\tau<0$ we have
$$\mathcal{H}_{\tau}\left(X, \Lambda^{0,1} \otimes \Theta\right)=\mathcal{H}_{-3}\left(X, \Lambda^{0,1} \otimes \Theta\right),$$
and if $\Gamma$ is not cyclic or $\Gamma=\mathbb{Z} / 2 \mathbb{Z}$, then
$$\mathcal{H}_{\tau}\left(X, \Lambda^{0,1} \otimes \Theta\right)=\mathcal{H}_{-4}\left(X, \Lambda^{0,1} \otimes \Theta\right) .$$
Proof. First, we will show that any decaying harmonic element $\phi \in H^{0}\left(X, \Lambda^{0,1} \otimes \Theta\right)$ has a decay rate of at least $O\left(r^{-3}\right)$ at infinity. Since $X$ is Kähler, by [Mor07, Part 5], the operator □ admits an expansion near infinity of the form
$$\square=\frac{1}{2} \nabla^{*} \nabla+\Re$$
on $\Lambda^{0,1} \otimes \Theta$, where ∇ is the covariant derivative on $\Lambda^{0,1} \otimes \Theta$, and $\Re$ is an operator given by curvature forms acting on the same bundle. The leading term of $\nabla^{*} \nabla$ is the Euclidean Laplacian $\Delta_{E u c}$, so we have
$$\square=\frac{-1}{2} \Delta_{E u c}+Q,$$
where $Q=A(\nabla \phi)+\operatorname{Ric}(\phi)$ denotes higher order terms. The element $\phi$ admits an expansion of the form
$$\phi=f+O\left(r^{-3+\epsilon}\right),$$
as $r \rightarrow \infty$, where $f$ is of the form
$$f=\sum_{i, j} \frac{f_{i, j}}{r^{2}} d \bar{z}_{i} \otimes \frac{\partial}{\partial z_{j}},$$
and $f_{i, j}$ are constants. Since $\phi$ is □ -harmonic, both $\bar{\partial} f=0$ and $\bar{\partial}^{*} f=0$. It is easy to see that this implies that each $f_{i, j}=0$. Consequently, $\phi=O\left(r^{-3+\epsilon}\right)$ as $r \rightarrow \infty$. Since $\phi$ admits an expansion with harmonic leading term, we must have $\phi=O\left(r^{-3}\right)$.

Furthermore, if $\Gamma$ is not cyclic or $\Gamma=\mathbb{Z} / 2 \mathbb{Z}$, then $\Gamma$ contains the element -1. The leading term of $\phi$ is of the form
$$f=\sum_{k, l} \frac{A_{k l}}{r^{4}} d \bar{z}_{k} \otimes \frac{\partial}{\partial z_{l}},$$
where $A_{k l}$ is a linear combination of $z_{1}, \bar{z}_{1}, z_{2}, \bar{z}_{2}$. Since any such nonzero $f$ is not invariant under the action of -1, we must have $f=0$, and then $\phi=O\left(r^{-4}\right)$. This finishes the proof of (3.14) and (3.15). \(\square\)

The following Proposition will be used in Section 7.
Proposition 3.6. Let $(X, g, J)$ be an ALE Kähler surface. Then
$$b_{1}(X)=0,$$
where $b_{1}(X)$ denotes the first Betti number of $X$. Furthermore, for $\tau<0$,
$$\operatorname{dim}\left(\mathcal{H}_{\tau}\left(X, \Lambda^{0,2}\right)\right)=\operatorname{dim}\left(\mathcal{H}_{\tau}\left(X, \Lambda^{2,0}\right)\right)=0 .$$
Proof. Let $U$ be a tubular neighborhood of $E_{\infty}, \hat{X}=X \cup E_{\infty}$ be the analytic compactification of $X$. By Proposition 3.1, $\hat{X}$ is either a rational surface or a ruled surface, then $b^{1}(\hat{X})=0$. Since $E_{\infty}$ is a tree of rational curves, $b^{1}(U)=0$ and $b^{1}(X \cap U)=0$. Then by the Mayer-Vietoris theorem, $b^{1}(X)=0$.

Since $\operatorname{dim}\left(\mathcal{H}_{\tau}\left(X, \Lambda^{0,2}\right)\right)=\operatorname{dim}\left(\mathcal{H}_{\tau}\left(X, \Lambda^{2,0}\right)\right)$, we just need to show the latter one equals to zero. The proof is similar to the proof of Proposition 3.4, so we will skip some details. For any $\sigma \in \mathcal{H}_{\tau}\left(X, \Lambda^{2,0}\right)$, let $\tilde{\sigma}$ be its lifting on $\tilde{X}_{\infty}$. Then
$$\tilde{\sigma}=a \cdot d z_{1} \wedge d z_{2}+O\left(|z|^{-3} \tilde{\sigma}\right)$$
where $a=O\left(|z|^{\tau}\right)$ as $r \rightarrow \infty$ is a $\bar{\partial}_{E u c}$-holomorphic function. Then $a=0$, and $\tilde{\sigma}=$ $O\left(|z|^{-3+\tau}\right)$, which implies that $\tilde{\sigma}$ can decay to any order in the ALE coordinates $\left\{z_{1}, z_{2}\right\}$. Consequently, $\tilde{\sigma}$ can be extended to $C$. Furthermore,
$$\left.\Omega^{2,0}\right|_{C}=\Omega^{2,0}(C) \otimes N_{C}^{*}=\mathcal{O}(-3) .$$
This implies that $\tilde{\sigma}$ vanishes on an open neighborhood of $C$, so $\sigma$ vanishes identically on $X$. \(\square\)

\section*{4. Small deformations of complex structure}

First we need a fixed point theorem for operators on Banach spaces (see, for example [BR15]).

Lemma 4.1. Let $F: \mathcal{B}_{1} \rightarrow \mathcal{B}_{2}$ be a bounded differentiable operator between Banach spaces. In a small neighborhood of $0 \in \mathcal{B}_{1}, F(x)=F(0)+F^{\prime}(0) x+Q(x)$, where
$$\left\|Q(x)-Q\left(x^{\prime}\right)\right\|_{\mathcal{B}_{2}} \leq C_{0} \cdot\left(\|x\|_{\mathcal{B}_{1}}+\left\|x^{\prime}\right\|_{\mathcal{B}_{1}}\right) \cdot\left\|x-x^{\prime}\right\|_{\mathcal{B}_{1}} .$$
Assume that $\|F(0)\|_{\mathcal{B}_{2}} \ll 1$. Then
(i) If $F^{\prime}(0)$ is an isomorphism with right inverse $G$ bounded by $C_{1}$, then there exists a ball $B(0, s) \subset \mathcal{B}_{1}$ such that there exists a unique $x \in B(0, s)$ with $F(x)=0$.
(ii) If $F^{\prime}(0)$ is Fredholm and surjective, with right inverse bounded by $C_{1}$, then there is an $s>0$, so that $F^{-1}(0) \cap B(0, s)$ is isomorphic to $U \subset \operatorname{ker}\left(F^{\prime}(0)\right)$, where $U$ is a small neighborhood of the origin.

The following lemma gives the properties of the linearized operator we will need in order to invoke Lemma 4.1.

Lemma 4.2. Let $(X, g, J)$ be a Kähler ALE surface. The linear operator
$$P: C_{\delta-1}^{k, \alpha}\left(X, \Lambda^{0,1} \otimes \Theta\right) \xrightarrow{\left(\bar{\partial}^{*}, \bar{\partial}\right)} C_{\delta-2}^{k-1, \alpha}(X, \Theta) \oplus C_{\delta-2}^{k-1, \alpha}\left(X, \Lambda^{0,2} \otimes \Theta\right)$$
is surjective and Fredholm, for some $k \geq 3$ and $\delta \in(-2,-1)$.
Proof. It is not hard to see that $P$ is an elliptic operator, and that the indicial roots of $P$ are integral. Consequently, by standard weighted space theory, $P$ is Fredholm since $\delta$ is non-integral [LM85].

The cokernel is given by
$$\operatorname{ker}\left(P^{*}\right)=\left\{\left(\sigma_{1}, \sigma_{2}\right) \in C_{-2-\delta}^{k-1, \alpha}(\Theta) \oplus C_{-2-\delta}^{k-1, \alpha}\left(\Lambda^{0,2} \otimes \Theta\right): \bar{\partial}^{*} \sigma_{2}=\bar{\partial} \sigma_{1}\right\} .$$
Let $\left(\sigma_{1}, \sigma_{2}\right) \in \operatorname{ker}\left(P^{*}\right)$, then
$$\bar{\partial}^{*} \sigma_{1}=0, \bar{\partial}^{*} \bar{\partial} \sigma_{1}=\bar{\partial}^{*} \bar{\partial}^{*} \sigma_{2}=0$$
which implies that $\sigma_{1}$ is □ -harmonic. From Proposition 3.3, $\sigma_{1}=0$. Then
$$\bar{\partial} \sigma_{2}=0, \bar{\partial}^{*} \sigma_{2}=0,$$
and the vanishing of $\sigma_{2}$ follows from Proposition 3.4. Since $\operatorname{ker}\left(P^{*}\right)=0$, and $P$ is Fredholm, $P$ is surjective. \(\square\)

For a fixed complex structure $J$, there is a nonlinear correspondence between sufficiently small sections of $\Gamma\left(X, \operatorname{End}_{a}(T X)\right)$ and almost complex structures near $J$ given by
$$\begin{aligned}
E_{J} & : \Gamma\left(X, \operatorname{End}_{a}(T X)\right) \rightarrow \mathcal{A} \\
E_{J}(I) & =\left(J+\frac{1}{2} I\right) J\left(J+\frac{1}{2} I\right)^{-1}
\end{aligned}$$
where $\mathcal{A}$ is the space of almost complex structures on $X$. If $\phi \in \Gamma\left(\Lambda^{0,1} \otimes \Theta\right)$ has sufficiently small norm, then the corresponding almost complex structure will be denoted by $J(\phi)=$ $E_{J}(R e(\phi))$. Note that there is an expansion:
$$J(\phi)=J+\operatorname{Re}(\phi)+Q$$
where $|Q|=O\left(|\phi|^{2}\right)$, as $|\phi| \rightarrow 0$.
Next we prove a weighted version of Kuranishi's theorem.
Theorem 4.3. Let $\left(X, J_{0}, g_{0}\right)$ be a Kähler ALE surface, and let $B_{\epsilon_{1}}$ be an $\epsilon_{1}$-ball around 0 in $\mathcal{H}_{-3}\left(X, \Lambda^{0,1} \otimes \Theta\right)$. Then for $\epsilon_{1}>0$ sufficiently small, there is a differentiable family of complex structures $J_{t}$ for $t \in B_{\epsilon_{1}}$ such that
$$J_{t}=J(\phi(t)), \phi(t) \in C_{\delta-1}^{k, \alpha}\left(X, \Lambda^{0,1} \otimes \Theta\right), \delta \in(-2,-1), k \geq 3,$$
where $\phi(t)$ satisfies $\phi(t)=t+\phi(t)^{\perp}$, with $\phi(t)^{\perp}$ is $L^{2}$-orthogonal to $\mathcal{H}_{-3}\left(X, \Lambda^{0,1} \otimes \Theta\right)$, and $\bar{\partial}^{*}(\phi(t))=0$. Furthermore, there exists an $\epsilon^{\prime}>0$, such that if $J=J_{0}(\phi)$ is any integrable complex structure satisfying
$$\|\phi\|_{C_{\delta}^{k, \alpha}}<\epsilon^{\prime}, \quad \text { and } \quad \bar{\partial}^{*}(\phi)=0,$$
then $\phi$ is in the family $J_{t}$. Finally, for any $t \in B_{\epsilon_{1}}$, there exists a constant $C$ such that $\|\phi(t)\|_{C_{-3}^{k, \alpha}} \leq C \cdot \epsilon_{1}$.

Proof. Define the operator
$$\begin{aligned}
F: C_{\delta-1}^{k, \alpha}\left(X, \Lambda^{0,1} \otimes \Theta\right) & \rightarrow C_{\delta-2}^{k-1, \alpha}(X, \Theta) \oplus C_{\delta-2}^{k-1, \alpha}\left(X, \Lambda^{0,2} \otimes \Theta\right) \\
\phi & \mapsto\left(\bar{\partial}^{*} \phi, \bar{\partial} \phi+[\phi, \phi]\right),
\end{aligned}$$
where $[\phi, \phi]$ is a globally defined operator, which can be expressed locally as
$$\begin{aligned}
{[\phi, \phi] } & =\frac{1}{2}\left[\sum_{i, j} \phi_{i, j} d \bar{z}_{i} \otimes \frac{\partial}{\partial z_{j}}, \sum_{k, l} \phi_{k, l} d \bar{z}_{k} \otimes \frac{\partial}{\partial z_{l}}\right] \\
& =\sum_{i, j, k, l} \phi_{i, j} \frac{\partial \phi_{k, l}}{\partial z_{j}} d \bar{z}_{i} \wedge d \bar{z}_{k} \otimes \frac{\partial}{\partial z_{l}}
\end{aligned}$$
Formally, $[\phi, \phi]$ can be written as $\phi * \nabla \phi$, where $*$ means a linear combination of quadratic terms, each involving some contraction of $\phi$ with $\nabla \phi$.

Clearly, $F$ is a bounded differentiable mapping, and $F^{\prime}(0)=\left(\bar{\partial}^{*}, \bar{\partial}\right)$. Obviously, in a small neighborhood of 0 in $C_{\delta-1}^{k, \alpha}\left(X, \Lambda^{0,1} \otimes \Theta\right), F$ admits an expansion $F=F(0)+F^{\prime}(0)+Q$. We next prove the estimate (4.1). Let $r$ denote the radius. For any two elements $\phi, \phi^{\prime} \in C_{\delta-1}^{k, \alpha}\left(\Lambda^{0,1} \otimes \Theta\right)$, we have
$$\begin{aligned}
r^{2-\delta}\left|[\phi, \phi]-\left[\phi^{\prime}, \phi^{\prime}\right]\right| & =r^{2-\delta}\left|[\phi * \nabla \phi]-\left[\phi^{\prime} * \nabla \phi^{\prime}\right]\right| \\
& =r^{2-\delta}\left|\phi *\left(\nabla \phi-\nabla \phi^{\prime}\right)-\left(\phi-\phi^{\prime}\right) * \nabla \phi^{\prime}\right| \\
& \leq C r^{\delta-1}\left\{r^{1-\delta}|\phi| r^{2-\delta}\left|\nabla \phi-\nabla \phi^{\prime}\right|+r^{1-\delta}\left|\phi-\phi^{\prime}\right| r^{2-\delta}\left|\nabla \phi^{\prime}\right|\right\} \\
& \leq C\left(r^{1-\delta}|\phi|\right)\left(r^{2-\delta}\left|\nabla\left(\phi-\phi^{\prime}\right)\right|\right)+\left(r^{2-\delta}\left|\nabla \phi^{\prime}\right|\right)\left(r^{1-\delta}\left|\phi-\phi^{\prime}\right|\right) .
\end{aligned}$$
Next, let $x \neq y \in X$, with $r(x)<r(y)$. Similarly, we have
$$\begin{aligned}
& r(x)^{2-\delta} \frac{\left|\left([\phi, \phi]-\left[\phi^{\prime}, \phi^{\prime}\right]\right)(x)-\left([\phi, \phi]-\left[\phi^{\prime}, \phi^{\prime}\right]\right)(y)\right|}{d(x, y)^{\alpha}} \\
& \leq r(x)^{\delta-1}\left\{r(x)^{1-\delta} \frac{|\phi(x)-\phi(y)|}{d(x, y)^{\alpha}}\left|\nabla \phi(x)-\nabla \phi^{\prime}(x)\right| r(x)^{2-\delta}\right\}+ \\
& r(y)^{\delta-1}\left\{r(x)^{2-\delta} \frac{\left|\left(\nabla \phi(x)-\nabla \phi^{\prime}(x)\right)-\left(\nabla \phi(y)-\nabla \phi^{\prime}(y)\right)\right|}{d(x, y)^{\alpha}}|\phi(y)| r(y)^{1-\delta}\right\}+ \\
& r(x)^{\delta-1}\left\{r(x)^{1-\delta} \frac{\left|\left(\phi(x)-\phi^{\prime}(x)\right)-\left(\phi(y)-\phi^{\prime}(y)\right)\right|}{d(x, y)^{\alpha}}\left|\nabla \phi^{\prime}(x)\right| r(x)^{2-\delta}\right\}+ \\
& r(y)^{\delta-1}\left\{r(x)^{2-\delta} \frac{\left|\nabla \phi^{\prime}(x)-\nabla \phi^{\prime}(y)\right|}{d(x, y)^{\alpha}}\left|\phi(y)-\phi^{\prime}(y)\right| r(y)^{1-\delta}\right\} .
\end{aligned}$$
This shows that
$$\left\|[\phi, \phi]-\left[\phi^{\prime}, \phi^{\prime}\right]\right\|_{C_{\delta-2}^{0, \alpha}} \leq C_{0}\left(\|\phi\|_{C_{\delta-1}^{1, \alpha}}+\left\|\phi^{\prime}\right\|_{C_{\delta-1}^{1, \alpha}}\right)\left\|\phi-\phi^{\prime}\right\|_{C_{\delta-1}^{1, \alpha}} .$$
The higher derivative terms can be handled similarly, to prove
$$\left\|[\phi, \phi]-\left[\phi^{\prime}, \phi^{\prime}\right]\right\|_{C_{\delta-2}^{j-1, \alpha}} \leq C_{j}\left(\|\phi\|_{C_{\delta-1}^{j, \alpha}}+\left\|\phi^{\prime}\right\|_{C_{\delta-1}^{j, \alpha}}\right)\left\|\phi-\phi^{\prime}\right\|_{C_{\delta-1}^{j, \alpha}}, 1 \leq j \leq k$$
which shows that $Q$ satisfies (4.1).
By Lemma 4.2, we know $P=F^{\prime}(0)$ is Fredholm. We can choose a right inverse operator $G$ such that the image of $G$ is $L^{2}$-orthogonal to $\mathcal{H}_{-3}\left(X, \Lambda^{0,1} \otimes \Theta\right)$. By Lemma 4.1 there
exists $s=\epsilon_{1}>0$, such that $F^{-1}(0)$ is locally isomorphic to an $\epsilon_{1}$-neighborhood of 0 in $\mathcal{H}_{\delta-1}\left(X, \Lambda^{0,1} \otimes \Theta\right)$, with the property that for each $t \in B_{\epsilon_{1}}$, there is a $\phi(t)=t+\phi(t)^{\perp} \in$ $F^{-1}(0)$, where $\phi(t)^{\perp}$ is $L^{2}$-orthogonal to $\mathcal{H}_{-3}\left(X, \Lambda^{0,1} \otimes \Theta\right)$, and $J_{0}(\phi(t))$ is the corresponding complex structure. It is a straightforward consequence of the implicit function theorem that the mapping $\psi: t \mapsto \phi(t)$ is differentiable. This finishes the proof of the existence of the family of complex structures.

By the fixed point Lemma 4.1, near 0, the zero set of $\left(\bar{\partial}^{*}, \bar{\partial}+[],\right)$ is locally bijective to the kernel of $\left(\bar{\partial}^{*}, \bar{\partial}\right)$, which is $\mathcal{H}_{-3}\left(X, \Lambda^{0,1} \otimes \Theta\right)$. Thus there exists an $\epsilon^{\prime \prime}>0$ such that for any $\|\phi\|_{C_{\delta-1}^{k, \alpha}}<\epsilon^{\prime \prime}, \bar{\partial}^{*} \phi=0, \bar{\partial} \phi+[\phi, \phi]=0$, then $J=J_{0}(\phi)$ is in the family we just constructed.

Next we will show that $\phi(t) \in C_{-3}^{k, \alpha}\left(X, \Lambda^{0,1} \otimes \Theta\right)$ for $t \in B_{\epsilon_{1}}$. In fact, we will show that for any $\phi \in C_{\delta}^{k, \alpha}\left(X, \Lambda^{0,1} \otimes \Theta\right)$ that satisfies the system
$$\bar{\partial} \phi=-[\phi, \phi], \bar{\partial}^{*} \phi=0,$$
then $\phi \in C_{-3}^{k, \alpha}\left(X, \Lambda^{0,1} \otimes \Theta\right)$. To see this, (4.17) implies that
$$\|\square \phi\|_{C_{2 \delta-2}^{k-2, \alpha}}=\left\|-\bar{\partial}^{*}[\phi, \phi]\right\|_{C_{2 \delta-2}^{k-2, \alpha}} \leq C \cdot\|\phi\|_{C_{\delta}^{k, \alpha}}^{2}$$
Then outside of a compact subset,
$$\frac{1}{2} \Delta_{E u c} \phi=-\square \phi+\left(\frac{1}{2} \Delta_{E u c}+\square\right) \phi=O\left(r^{2 \delta-2}\right),$$
which implies that
$$\phi=\sum_{i, j} \frac{a_{i, j}}{r^{2}} d \bar{z}_{i} \otimes \frac{\partial}{\partial z_{j}}+O\left(r^{-3+\epsilon}\right)$$
where $a_{i, j}$ are constants and $\frac{a_{i, j}}{r^{2}}$ is $\Delta_{E u c}$-harmonic. By the same argument as in the proof of (3.14), we have $a_{i, j}=0$. Then a similar argument shows that $\phi \in C_{-3}^{k, \alpha}\left(X, \Lambda^{0,1} \otimes \Theta\right)$.

Next we will show that, if $\phi \in C_{\delta}^{k, \alpha}\left(X, \Lambda^{0,1} \otimes \Theta\right),\|\phi\|_{C_{\delta}^{k, \alpha}}<\epsilon^{\prime}$, and satisfies the system (4.17), then $\|\phi\|_{C_{\delta-1}^{k, \alpha}} \leq C \cdot \epsilon^{\prime}$ for some constant $C>0$. By the argument above, $\phi \in$ $C_{-3}^{k, \alpha}\left(X, \Lambda^{0,1} \otimes \Theta\right)$, and $\phi=\phi^{h}+\phi^{\perp}$, where $\phi^{h} \in \mathcal{H}_{-3}\left(X, \Lambda^{0,1} \otimes \Theta\right)$, and $\phi^{h}$ is $L^{2}$-orthognal to $\phi^{\perp}$. By an argument similar to Corollary 1.16 in [Bar86], $\left\|\phi^{\perp}\right\|_{C_{\delta-1}^{k, \alpha}} \leq C \cdot\|\square \phi\|_{C_{\delta-3}^{k-2, \alpha}}$. Since $\phi^{h}$ is in a finite dimensional space, combined with the estimate (4.18), we can make $\epsilon^{\prime}$ small enough such that $\|\phi\|_{C_{\delta-1}^{k, \alpha}}<\epsilon^{\prime \prime}$, and then $\phi$ is in the family $J_{t}$ as shown above. The estimate of $\|\phi\|_{C_{-3}^{k, \alpha}}$ follows from finite-dimensionality of the kernel. \(\square\)

\section*{5. Versality of Kuranishi family}

The next result shows that any nearby complex structure can be brought into the family $J_{t}$ by a suitable diffeomorphism. Of course, the implicit function theorem requires a mapping between Banach spaces to be differentiable. The following lemma, inspired by [Biq06], will be used below to this end.

Lemma 5.1. Let $\left(X, g_{0}, J_{0}\right)$ be a Kähler ALE surface with $g_{0}, J_{0} \in C^{\infty}$. Then for $\delta^{\prime}<-1$, for $g_{0}, J_{0}$ with ALE asymptotic rate $O\left(r^{\delta^{\prime}}\right)$, there exists an $\epsilon_{1}>0$, such that for an $\epsilon_{1}$-ball
$B_{\epsilon_{1}} \subset C_{\delta^{\prime}+1}^{k+1, \alpha}(T X)$, the maps
$$\begin{aligned}
& B_{\epsilon_{1}} \rightarrow C_{\delta^{\prime}}^{k, \alpha}\left(S^{2}\left(T^{*} X\right)\right), Y \mapsto \Phi_{Y *} g_{0}-g_{0} \\
& B_{\epsilon_{1}} \rightarrow C_{\delta^{\prime}}^{k, \alpha}(\operatorname{End}(T X)), Y \mapsto \Phi_{Y *} J_{0}-J_{0}
\end{aligned}$$
are smooth.
Proof. Let $U \subset X$ be a normal coordinate chart with respect to $g_{0}$, and let $U^{\prime}, U^{\prime \prime}$ be smaller charts, such that the $\epsilon_{1}$-neighborhood of $U^{\prime}$ is in $U$, and the $\epsilon_{1}$-neighborhood of $U^{\prime \prime}$ is in $U^{\prime}$. The tangent bundle $T U$ is isomorphic to $U \times \mathbb{R}^{4}$, with coordinate functions $(x, v)=\left(x_{1}, \ldots, x_{4}, v_{1}, \ldots v_{4}\right)$. On $U^{\prime}$, we have the Riemannian exponential map:
$$\begin{aligned}
\operatorname{Exp}: U^{\prime} \times B_{\epsilon_{1}} \subset T U^{\prime} & \rightarrow U \\
(x, v) & \rightarrow \gamma(x, v)
\end{aligned}$$
where $\gamma(x, v)$ is a geodesic with initial position and derivative ( $x, v$ ). The $j^{\text {th }}$-coordinate function of $\operatorname{Exp}(1 \leq j \leq 4)$ is a smooth function over $(x, v)$, and has an expansion
$$\operatorname{Exp}_{j}(x, v)=x_{j}+\sum_{k=1}^{4} f_{k}(x) v_{k}+Q(x, v)$$
where $|Q(x, v)| \leq C\left(U, g_{0}\right) \cdot|v|^{2}$. Let $\xi \in C^{k+1, \alpha}(T U)$, and $\|\xi\|_{C^{k+1, \alpha}}<\epsilon_{1}$. The geodesic flow $\Phi_{\xi}$ is defined as
$$\begin{aligned}
\Phi_{\xi}: U^{\prime} & \rightarrow U \\
x & \rightarrow \operatorname{Exp}(x, \xi(x))
\end{aligned}$$
Then $\Phi_{\xi}(x)=\operatorname{Exp}(x, \xi(x))$ is $C^{k+1, \alpha}$ over $x$, since $\operatorname{Exp}$ is smooth and $\xi(x)$ is $C^{k+1, \alpha}$. Let $\xi^{\prime}$ be another vector field on $U$ with $\left\|\xi^{\prime}\right\|_{C^{k+1, \alpha}}<\epsilon_{1}$. Then by the expansion above, for each $1 \leq j \leq 4$, we have:
$$\left\|\left(\Phi_{\xi}\right)_{j}-\left(\Phi_{\xi^{\prime}}\right)_{j}-\sum_{k=1}^{4} f_{k} \cdot\left(\xi_{k}-\xi_{k}^{\prime}\right)\right\|_{C^{k+1, \alpha}\left(U^{\prime \prime}\right)} \leq C \cdot\left\|\xi-\xi^{\prime}\right\|_{C^{k+1, \alpha}(U)}^{2}$$
This implies that each coordinate function of $\Phi$ is Fréchet differentiable as a map from $B_{\epsilon_{1}} \subset C^{k+1, \alpha}(T U)$ to $C^{k+1, \alpha}\left(U^{\prime \prime}\right)$.

Since $\Phi_{\xi_{*}} g_{0}$ is defined as $\left(\Phi_{\xi}^{-1}\right)^{*} g_{0}$, without the loss of generality, we will do the analysis on $\Phi_{\xi}^{*} g_{0}-g_{0}$. On the chart $U^{\prime \prime}$, we have $\Phi_{\xi}^{*} g_{0}(x)\left(\partial_{i}, \partial_{j}\right)=g_{0}\left(\Phi_{\xi}(x)\right)\left(\Phi_{\xi_{*}} \partial_{i}, \Phi_{\xi_{*}} \partial_{j}\right)$. Since $g_{0}$ is smooth over $x$, and $\Phi_{\xi_{*}} \partial_{j}=\partial_{j} \Phi_{\xi}$ is $C^{k, \alpha}$ over $x$, by using the argument above, we can see that $\Phi^{*} g_{0}-g_{0}: B_{\epsilon_{1}} \subset C^{k+1, \alpha}(T U) \rightarrow C^{k, \alpha}\left(S^{2}\left(T^{*} U^{\prime \prime}\right)\right)$ is Fréchet differentiable.

For some large $R>0$, denote $A_{R, 2 R}$ as an annulus in the ALE space $X$. By covering $A_{R, 2 R}$ with finite many normal coordinate charts, using the argument above for each chart, we have the map $\Phi^{*} g_{0}: B_{\epsilon_{1}} \subset C^{k+1, \alpha}\left(T A_{R, 2 R}\right) \rightarrow C^{k, \alpha}\left(S^{2}\left(T^{*} A_{R-\epsilon_{1}, 2 R-2 \epsilon_{1}}\right)\right)$ is Fréchet differentiable. By a standard dilation argument, which dilates $A_{R, 2 R}$ to $A_{2^{k} R, 2^{k+1} R}$, we have $\Phi^{*} g_{0}-g_{0}$ : $B_{\epsilon_{1}} \subset C_{\delta^{\prime}+1}^{k+1, \alpha}\left(T A_{2^{k} R, 2^{k+1} R}\right) \rightarrow C_{\delta^{\prime}}^{k, \alpha}\left(S^{2}\left(T^{*} A_{2^{k}\left(R-\epsilon_{1}\right), 2^{k+1}\left(R-\epsilon_{1}\right)}\right)\right)$ is Fréchet differentiable. The constant $C\left(U, g_{0}\right)$ in each chart $U$ can be chosen uniformly bounded on $X$. This implies that $\Phi^{*} g_{0}-g_{0}: B_{\epsilon_{1}} \subset C_{\delta^{\prime}+1}^{k+1, \alpha}(T X) \rightarrow C_{\delta^{\prime}}^{k, \alpha}\left(S^{2}\left(T^{*} X\right)\right)$ is Fréchet differentiable. Furthermore, it
follows that for $Y, Y^{\prime} \in B_{\epsilon_{1}}$, there exists a constant $C$,
$$\left\|\Phi_{Y}^{*} g_{0}-\Phi_{Y^{\prime}}^{*} g_{0}-\mathfrak{L}_{Y-Y^{\prime}} g_{0}\right\|_{C_{\delta^{\prime}}^{k, \alpha}} \leq C \cdot\left\|Y-Y^{\prime}\right\|_{C_{\delta^{\prime}+1}^{k+1, \alpha}} \cdot\left(\|Y\|_{C_{\delta^{\prime}+1}^{k+1, \alpha}}+\left\|Y^{\prime}\right\|_{C_{\delta^{\prime}+1}^{k+1, \alpha}}^{k+1}\right) .$$
By using higher order expansions similar to (5.4), we can furthermore show that $\Phi^{*} g_{0}-g_{0}$ is indeed a smooth map. The proof for $J_{0}$ can proceed in a similar fashion. Specifically we have
$$\left\|\Phi_{Y}^{*} J_{0}-\Phi_{Y^{\prime}}^{*} J_{0}-\mathfrak{L}_{Y-Y^{\prime}} J_{0}\right\|_{C_{\delta^{\prime}}^{k, \alpha}} \leq C \cdot\left\|Y-Y^{\prime}\right\|_{C_{\delta^{\prime}+1}^{k+1, \alpha}} \cdot\left(\|Y\|_{C_{\delta^{\prime}+1}^{k+1, \alpha}}+\left\|Y^{\prime}\right\|_{C_{\delta^{\prime}+1}^{k+1, \alpha}}\right) .$$ \(\square\)

Let $\nabla^{*}: \Gamma\left(\operatorname{End}_{a}(T X)\right) \rightarrow \Gamma(T X)$ be the adjoint operator of $\frac{-1}{2} J \circ \mathfrak{L}_{*} J$, which is defined as:
$$\left(\nabla^{*} A\right)^{k}=-\sum_{l, j} g^{l j} \nabla_{l} A_{j}^{k}$$
Note that under the identification of $\operatorname{End}_{a}(T X)$ with $\operatorname{Re}\left(\Lambda^{0,1} \otimes \Theta\right)$ and $T X$ with $\operatorname{Re}(\Theta)$, this corresponds to the operator $\bar{\partial}^{*}$. In the following proofs, for the convenience of the notation, we will denote each element in $\Gamma\left(\operatorname{End}_{a}(T X)\right)$ as $\operatorname{Re}(\phi)$, where $\phi \in \Gamma\left(\Lambda^{0,1} \otimes \Theta\right)$.

Lemma 5.2. Let $\left(X, J_{0}, g_{0}\right)$ be a Kähler ALE surface with $J_{0}, g_{0} \in C^{\infty}$. Let $\delta^{\prime}<-1, k \geq$ $3,0<\alpha<1$. Then the following map $\mathfrak{P}$ is smooth in an open neighborhood of (0, 0, 0)
$$\begin{aligned}
\mathfrak{P}: C_{\delta^{\prime}}^{k, \alpha}\left(S^{2}(T X)\right) \times C_{\delta^{\prime}}^{k, \alpha}(\operatorname{End}(T X)) \times C_{\delta^{\prime}}^{k, \alpha}\left(E n d_{a}(T X)\right) & \rightarrow C_{\delta^{\prime}-1}^{k-1, \alpha}(T X) \\
(h, w, \operatorname{Re}(\phi)) & \mapsto \nabla_{g_{0}+h}^{*}\left(E_{J_{0}+w}^{-1}\left(J_{0}(\phi)\right)\right)
\end{aligned}$$
Proof. The divergence operator has the expansion formula
$$\nabla_{g_{0}+h}=\nabla_{g_{0}}+\left(g_{0}+h\right)^{-1} * \nabla_{g_{0}} h,$$
[GV16, Formula 3.39], where $*$ means a linear combination of tensor contractions, and $\left(g_{0}+\right.$ $h)^{-1}$ is analytic for smooth $h$. By the expansions (4.7),
$$E_{J_{0}+w}^{-1}\left(J_{0}(\phi)\right)=-w+\operatorname{Re}(\phi)+Q^{\prime}$$
where $Q^{\prime}$ represents the higher order terms, which is analytic for small $w$. Note that $\mathfrak{P}(0,0,0)=0$. For $(h, w, \operatorname{Re}(\phi)),\left(h^{\prime}, w^{\prime}, \operatorname{Re}\left(\phi^{\prime}\right)\right)$ of sufficiently small norm, by the expansion above, there exists a constant $C$ so that
$$\begin{array}{r}
\left\|\mathfrak{P}(h, w, \operatorname{Re}(\phi))-\mathfrak{P}\left(h^{\prime}, w^{\prime}, \operatorname{Re}\left(\phi^{\prime}\right)\right)+\nabla_{g_{0}}^{*}\left(w-w^{\prime}\right)-\nabla_{g_{0}}^{*} \operatorname{Re}\left(\phi-\phi^{\prime}\right)\right\|_{C_{\delta^{\prime}}^{k-1, \alpha}}^{k-1} \leq \\
C \cdot\left(\|h\|_{C_{\delta^{\prime}}^{k, \alpha}}+\left\|h^{\prime}\right\|_{C_{\delta^{\prime}}^{k, \alpha}}+\|w\|_{C_{\delta^{\prime}}^{k, \alpha}}+\left\|w^{\prime}\right\|_{C_{\delta^{\prime}}^{k, \alpha}}+\|\operatorname{Re}(\phi)\|_{C_{\delta^{\prime}}^{k, \alpha}}^{2}+\left\|\operatorname{Re}\left(\phi^{\prime}\right)\right\|_{C_{\delta^{\prime}}^{k, \alpha}}^{2}\right) \\
\cdot\left(\left\|h-h^{\prime}\right\|_{C_{\delta^{\prime}}^{k, \alpha}}+\left\|w-w^{\prime}\right\|_{C_{\delta^{\prime}}^{k, \alpha}}+\left\|\operatorname{Re}\left(\phi-\phi^{\prime}\right)\right\|_{C_{\delta^{\prime}}^{k, \alpha}}^{2}\right)
\end{array}$$
This implies $\mathfrak{P}$ is differentiable, and satisfies the condition of Lemma 4.1. By higher order expansions of $\mathfrak{P}$ over $(h, w, \operatorname{Re}(\phi))$, we can furthermore show that $\mathfrak{P}$ is smooth. \(\square\)

Lemma 5.3. Let $\left(X, J_{0}, g_{0}\right)$ be a Kähler ALE surface with $J_{0}, g_{0} \in C^{\infty}$. There exists an $\epsilon_{1}^{\prime}>0$ such that for any complex structure $\left\|J_{1}-J_{0}\right\|_{C_{\delta}^{k, \alpha}}<\epsilon_{1}^{\prime}$, where $k \geq 3, \alpha \in(0,1), \delta \in$ $(-2,-1)$, there exists a unique diffeomorphism $\Phi$, of the form $\Phi_{Y}$ for $Y \in C_{\delta+1}^{k+1, \alpha}(T X)$ such that $\Phi^{*}\left(J_{1}\right)$ is in the family $J_{t}$ from Theorem 4.3.

Proof. Let $J_{1}=J_{0}(\phi)$, where $\|\phi\|_{C_{\delta}^{k, \alpha}}<\epsilon_{1}^{\prime}$ for some small $\epsilon_{1}^{\prime}$ to be determined later, and $\bar{\partial} \phi+[\phi, \phi]=0$. Define $\phi_{Y} \in \Gamma\left(\Lambda^{0,1} \otimes \Theta\right)$ by $\Phi_{Y}^{*} J_{0}(\phi)=E_{J_{0}}\left(R e\left(\phi_{Y}\right)\right)$. Define the operator $\mathfrak{N}$ by choosing the first parameter of $\mathfrak{P}$ to be $\left(\Phi_{Y}\right)_{*} g_{0}-g_{0}$, choosing the second parameter to be $\left(\Phi_{Y}\right)_{*} J_{0}-J_{0}$, and letting $\delta^{\prime}=\delta$ as the following
$$\begin{aligned}
C_{\delta+1}^{k+1, \alpha}(T X) \times C_{\delta}^{k, \alpha}\left(X, E n d_{a}(T X)\right) & \rightarrow C_{\delta-1}^{k-1, \alpha}(T X) \\
(Y, \operatorname{Re}(\phi)) & \mapsto \nabla_{\Phi_{Y *} g_{0}}^{*}\left(E_{\Phi_{Y *} J_{0}}^{-1}\left(J_{0}(\phi)\right)\right),
\end{aligned}$$
where $\Phi_{Y}$ is defined in (1.14), and $\nabla_{\Phi_{Y *} g_{0}}^{*}$ is the divergence operator associated to metric $\Phi_{Y *} g_{0}$. Note that
$$\left.\nabla_{\Phi_{Y *} g_{0}}^{*}\left(E_{\Phi_{Y *} J_{0}}^{-1}\left(J_{0}(\phi)\right)\right)=0 \Leftrightarrow \nabla_{g_{0}}^{*} E_{J_{0}}^{-1}\left(\Phi_{Y}^{*}\left(J_{0}(\phi)\right)\right)\right)=0 \Leftrightarrow \nabla_{g_{0}}^{*} \operatorname{Re}\left(\phi_{Y}\right)=0,$$
so a zero of $\mathcal{N}$ satisfies the desired gauge condition. (The latter map has a regularity issue which is why we consider the former, see [Biq06].) Since $\mathfrak{P}$ is smooth by Lemma 5.2, and since the mappings $Y \mapsto\left(\Phi_{Y}\right)_{*} g_{0}-g_{0}$, and $Y \mapsto\left(\Phi_{Y}\right)_{*} J_{0}-J_{0}$ are smooth by Lemma 5.1. the composition $\mathfrak{N}$ is smooth in an open neighborhood of $(0,0)$.

Consequently, at $(0,0)$, the linearization of $\mathfrak{N}$ restricted to the tangent space of the first variable is
$$\begin{aligned}
& D \mathfrak{N}_{0}: C_{\delta+1}^{k+1, \alpha}(T X) \rightarrow C_{\delta-1}^{k-1, \alpha}(T X) \\
& Y \mapsto \nabla_{g_{0}}^{*} \circ \frac{-1}{2} J \circ \mathfrak{L}_{Y} J_{0}=\square_{g_{0}} Y,
\end{aligned}$$
where the adjoint operator of $D \mathfrak{N}_{0}$ is:
$$\begin{aligned}
\left(D \mathfrak{N}_{0}\right)^{*}: C_{-3-\delta}^{k+1, \alpha}(T X) & \rightarrow C_{-5-\delta}^{k-1, \alpha}(T X) \\
\eta & \mapsto \square_{g_{0}} \eta,
\end{aligned}$$
The kernel of $\left(D \mathfrak{N}_{0}\right)^{*}$ consists of those $\eta \in C_{-3-\delta}^{k+1, \alpha}(T X)$ such that $\square_{g_{0}} \eta=0$, which implies that $\eta$ is the real part of a holomorphic vector field. From Proposition 3.3, $\eta=0$. Since the cokernel of $D \mathfrak{N}_{0}$ is trivial, $D \mathfrak{N}_{0}$ is surjective. Note also that the kernel of $D \mathfrak{N}_{0}$ is trivial.

Of course, in a small neighborhood of $(0,0)$ in $C_{\delta+1}^{k+1, \alpha}(T X) \times C_{\delta}^{k, \alpha}\left(X, \operatorname{End}_{a}(T X)\right), D \mathfrak{N}$ is surjective. Since $\mathfrak{N}$ is smooth, condition (4.1) is satisfied, so by Lemma 4.1, there exists a unique diffeomorphism $\Phi_{Y}$ such that $\operatorname{Re}\left(\phi_{Y}\right)$ is divergence-free. Since $\phi_{Y}$ satisfies (4.9), by Theorem 4.3, $\Phi_{Y}^{*}\left(J_{1}\right)$ is in the family $J_{t}$. \(\square\)

\section*{6. Essential deformations of complex structure}

The arguments in this section are inspired by [CT94, Theorem 3.1], with some appropriate modifications for the smoothness arguments. Recall that the space $\mathbb{W}$ is defined as
$$\mathbb{W}=\left\{Z \in \mathcal{H}_{1}(X, T X) \mid \mathfrak{L}_{Z} g_{0}=O\left(r^{-1}\right), \mathfrak{L}_{Z} J_{0}=O\left(r^{-3}\right), \text { as } r \rightarrow \infty\right\} .$$
Clearly, $\mathbb{W}$ is finite-dimensional. For $Z \in \mathbb{W}$, we define $\Upsilon_{Z}: X \rightarrow X$ to be time-one flow for the one-parameter group of diffeomorphisms generated by $Z$. Note that since $\mathbb{W}$ is finitedimensional the use of the one-parameter group here will not have the loss-of-regularity problem as in infinite dimensions. Furthermore, the time-one flow for vector fields in $\mathbb{W}$ has the following nice property.

Lemma 6.1. Fix an ALE coordinate under which $\left|J_{0}-J_{\text {Euc }}\right|=O\left(r^{-3}\right)$. For $Z \in \mathbb{W}$ sufficiently small, the time-one flow for the one-parameter group of diffeomorphisms generated by $Z$ exists. Furthermore, there exist a matrix $A \in \mathrm{U}(2)$ and vector $\hat{\epsilon}_{0} \in \mathbb{C}^{2}$, such that in ALE coordinates of order $\mu$ with $-2<-\mu<-1$,
$$d\left(\Upsilon_{Z}(x), A x+\hat{\epsilon}_{0}\right)=O\left(r^{-\mu}\right),$$
as $r \rightarrow \infty$, for any $\epsilon>0$.
Proof. First, note that $Z \in \mathbb{W}$ admits an expansion
$$Z=Z_{1}+Z_{0}+Z_{\mu},$$
for any $\epsilon>0$, where $Z_{1}$ is in the Lie algebra of U(2), $Z_{0}$ is vector field with constant coefficients, and $Z_{\mu}=O\left(r^{-\mu}\right)$ as $r \rightarrow \infty$. To see this, by standard harmonic expansion for kernel elements of $\square_{g_{0}}$, we have that any $Z \in \mathbb{W}$ satisfies
$$Z=Z_{1}+Z_{0}+O\left(r^{-\mu}\right)$$
where $Z_{1}$ is any vector field which is homogeneous of degree one, and $Z_{0}$ is a vector field with constant coefficients. The conditions that $\mathfrak{L}_{Z} g_{0}=O\left(r^{-1}\right)$ and $\mathfrak{L}_{Z} J_{0}=O\left(r^{-3}\right)$ as $r \rightarrow \infty$ imply that $\mathfrak{L}_{Z_{1}} g_{E u c}=0$ and $\mathfrak{L}_{Z_{1}} J_{E u c}=0$, that is, $Z_{1}$ is in the Lie algebra of U(2). Next,
$$\mathfrak{L}_{Z_{1}+Z_{0}} J_{0}=\mathfrak{L}_{Z_{1}+Z_{0}}\left(J_{0}-J_{E u c}\right)=\mathfrak{L}_{Z_{1}+Z_{0}}\left(O\left(r^{-3}\right)\right),$$
which implies that
$$\mathfrak{L}_{Z_{0}+Z_{1}} J_{0}=O\left(r^{-3}\right),$$
as $r \rightarrow \infty$. Consequently,
$$\square_{0}\left(Z-Z_{1}-Z_{0}\right)=O\left(r^{-4}\right) .$$
Since there is no harmonic term of degree -1, the claimed expansion (6.3) follows.
Clearly for $Z$ sufficiently small in norm, the one-parameter group of diffeomorphisms which is defined by
$$x^{\prime}(t)=Z(x(t)), x(0)=x,$$
exists by the standard short-time existence theorem for ODEs. By the expansion (6.3), $x(t)$ will be given by a family of rotations in U(2) , and translations plus decaying terms. \(\square\)

Remark 6.2. Lemma 6.1 has assumed an ALE coordinate with inverse cubic complex structure asymptotic rate. In the following, note that the statements Lemma 6.3 and Theorem 6.4 are independent of the ALE coordinate in the sense that, if they are true under the ALE coordinate $\left(x^{1}, x^{2}, x^{3}, x^{4}\right)$, then they are also true under the ALE coordinate $\left(x^{\prime 1}, x^{\prime 2}, x^{\prime 3}, x^{\prime 4}\right)$, as long as the two coordinates are comparable, i.e, $\frac{1}{C}|x|<\left|x^{\prime}\right|<C|x|$ for some constant $C>0$. Thus, in their proofs, we are free to choose an ALE coordinate such that $\left|J_{0}-J_{E u c}\right|=O\left(r^{-3}\right)$ by Proposition 3.1.

The next lemma states some useful properties of $\mathbb{W}$, which will be needed in the proof of the subsequent gauging theorem. For the simplicity of the statement of the theorem, define the norm $\|Z\|_{k+1, \alpha}$ for $Z \in \mathbb{W}$ as $\|Z\|_{k+1, \alpha}=\|Z\|_{C_{1}^{k+1, \alpha}}$ if $\lim _{r \rightarrow \infty}\left|r^{-1} \cdot Z\right| \neq 0$, $\|Z\|_{k+1, \alpha}=\|Z\|_{C^{k+1, \alpha}}$ if $\lim _{r \rightarrow \infty}\left|r^{-1} \cdot Z\right|=0$. Note that if $Z \in \mathbb{W}$ is decaying, then, $Z \equiv 0$.

Lemma 6.3. Let ( $X, J_{0}, g_{0}$ ) be a Kähler ALE surface, the space $\mathbb{W}$ satisfies the following properties:
\begin{itemize}
\item[-] There exists a small neighborhood $U \subset \mathbb{W}$ of 0 , and an $\epsilon^{\prime}>0$ such that if $g_{1}$ is any metric satisyfing $\left\|g_{1}-g_{0}\right\|_{C_{\delta}^{k, \alpha}}<\epsilon^{\prime}$, then there exists a constant $C$, such that for any $Z \in U$,
\end{itemize}
$$\left\|\Upsilon_{Z}^{*} g_{1}-g_{0}\right\|_{C_{\delta}^{k, \alpha}} \leq C\left(\|Z\|_{k+1, \alpha}+\epsilon^{\prime}\right) .$$
\begin{itemize}
\item[-] Given $\epsilon>0$ sufficiently small, for any complex structure $J_{1}=J_{0}(\phi)$ such that $\|\phi\|_{C_{-3+\epsilon}^{k, \alpha}}<\epsilon^{\prime}$ in the family constructed in Theorem 4.3 for some sufficiently small $\epsilon^{\prime}$, there exists a small neighborhood $U \subset \mathbb{W}$ of 0 , and a constant $C$, such that for any $Z, Z^{\prime} \in U$,
\end{itemize}
$$\left\|\Upsilon_{Z}^{*} J_{1}-\Upsilon_{Z^{\prime}}^{*} J_{1}-\mathfrak{L}_{Z-Z^{\prime}} J_{1}\right\|_{C_{-3+\epsilon}^{k, \alpha}} \leq C \cdot\left\|Z-Z^{\prime}\right\|_{k+1, \alpha} \cdot\left(\|Z\|_{k+1, \alpha}+\left\|Z^{\prime}\right\|_{k+1, \alpha}\right) .$$
Furthermore, the following map
$$\begin{aligned}
\Upsilon^{*}: \mathcal{H}_{-3}\left(X, \operatorname{End}_{a}(T X)\right) \times \mathbb{W} & \rightarrow C_{-3+\epsilon}^{k, \alpha}\left(X, \operatorname{End}_{a}(T X)\right) \\
(\operatorname{Re}(t), Z) & \mapsto E_{J_{0}}^{-1}\left(\Upsilon_{Z}^{*} J_{0}(\phi(t))\right) \equiv \phi_{Z}(t)
\end{aligned}$$
is smooth in an open neighborhood of $(0,0)$.
Proof. Fix an ALE coordinate under which $\left|J_{0}-J_{\text {Euc }}\right|=O\left(r^{-3}\right)$. Under such a coordinate, we have the decomposition of $Z$ as stated in Lemma 6.1. For simplicity, we assume $Z_{1} \neq 0$ in the following, and $\|Z\|_{k+1, \alpha}=\|Z\|_{C_{1}^{k+1, \alpha}}$. (The proof for the case $Z_{1}=0$ is similar.)

First, we address the estimate (6.9). Let $\Upsilon_{A, \hat{\epsilon}_{0}}$ denote the mapping $x \mapsto A x+\hat{\epsilon}_{0}$. Using Lemma 6.1,
$$\begin{aligned}
\left|\Upsilon_{Z}^{*} g_{1}-g_{0}\right| & =\left|\Upsilon_{Z}^{*} g_{1}-g_{1}+g_{1}-g_{0}\right| \leq\left|\Upsilon_{Z}^{*} g_{1}-g_{1}\right|+\left|g_{1}-g_{0}\right| \\
& \leq\left|\left(\Upsilon_{A, \hat{\epsilon}_{0}}+O\left(r^{-2+\epsilon}\right)\right)^{*}\left(\delta_{i j}+O\left(r^{\delta}\right)\right)-\left(\delta_{i j}+O\left(r^{\delta}\right)\right)\right|+\epsilon^{\prime} r^{\delta} \\
& \leq C\|Z\|_{C_{1}^{k+1, \alpha}} r^{\delta}+\epsilon^{\prime} r^{\delta}+o\left(r^{\delta}\right) \\
& \leq C r^{\delta}\left(\|Z\|_{C_{1}^{k+1, \alpha}}+\epsilon^{\prime}\right)
\end{aligned}$$
as $r \rightarrow \infty$. Since $\Upsilon_{Z}$ is the time one flow of $Z \in \mathbb{W}$, and $\mathbb{W}$ is finite-dimensional, a similar estimate holds on any compact subset of $X$, so the $C_{\delta}^{0}$ part of the norm is bounded by the right hand side of (6.9). Higher regularity estimates are similar, and are omitted.

Next we will discuss (6.10). As in the first part, since $\mathbb{W}$ is finite-dimensional, we only need to make estimates outside of a compact set $\overline{B_{R}\left(p_{0}\right)}$, where a global coordinate exists. Let $\gamma:[0,1] \rightarrow X$ be the path $\gamma(t)=\Upsilon_{t Z}(x)$. First, we estimate
$$\begin{aligned}
r(x)^{3-\epsilon}\left|\Upsilon_{Z}^{*} J_{0}-J_{0}-\mathfrak{L}_{Z} J_{0}\right|(x) & \leq C r^{3-\epsilon} \int_{0}^{1}\left|\Upsilon_{t Z}^{*}\left(\mathfrak{L}_{Z} J_{0}\right)(\gamma(0))-\mathfrak{L}_{Z} J_{0}(\gamma(0))\right| d t \\
& \leq C r^{3-\epsilon} \int_{0}^{1} \int_{0}^{t}\left|\mathfrak{L}_{Z}\left(\mathfrak{L}_{Z} J_{0}\right)(\gamma(s))\right| d s d t
\end{aligned}$$
By the expansion (6.3), given $c>0$, the estimates
$$(1-c) r(\gamma(s)) \leq r(x)=r(\gamma(0)) \leq(1+c) r(\gamma(s))$$
are satisfied for all $Z$ sufficiently small in norm. Note that since $Z_{1}$ is a vector field corresponding to a rotation in $\mathfrak{u}(2),\left|Z_{1}\right| \geq C \cdot r$ for some constant $C$. Also, since $\mathbb{W}$ is finite dimensional, $\left|\nabla^{\mathcal{I}} Z\right| \leq C(|\mathcal{I}|) \cdot r^{-|\mathcal{I}|} \cdot(|Z|+1)$ for some constant $C(|\mathcal{I}|)>0$. Then
$$\left|\mathfrak{L}_{Z}\left(\mathfrak{L}_{Z} J_{0}\right)\right|(\gamma(s)) \leq C r(\gamma(s))^{-5}(|Z(\gamma(s))|+1)^{2},$$
so we have
$$\begin{aligned}
r(x)^{3-\epsilon}\left|\Upsilon_{Z}^{*} J_{0}-J_{0}-\mathfrak{L}_{Z} J_{0}\right|(x) & \leq C \int_{0}^{1} \int_{0}^{t} r(\gamma(s))^{3-\epsilon} r(\gamma(s))^{-5}(|Z|+1)^{2}(\gamma(s)) d s d t \\
& \leq C \int_{0}^{1} \int_{0}^{t} r(\gamma(s))^{-2-\epsilon}(|Z|+1)^{2}(\gamma(s)) d s d t \leq C\|Z\|_{C_{1}^{k+1, \alpha}}^{2}
\end{aligned}$$
Next, we estimate
$$\begin{aligned}
r(x)^{3-\epsilon}\left|\Upsilon_{Z}^{*} \phi-\phi-\mathfrak{L}_{Z} \phi\right|(x) & \leq C r^{3-\epsilon} \int_{0}^{1}\left|\Upsilon_{t Z}^{*}\left(\mathfrak{L}_{Z} \phi\right)(\gamma(0))-\mathfrak{L}_{Z} \phi(\gamma(0))\right| d t \\
& \leq C r^{3-\epsilon} \int_{0}^{1} \int_{0}^{t}\left|\mathfrak{L}_{Z}\left(\mathfrak{L}_{Z} \phi\right)(\gamma(s))\right| d s d t
\end{aligned}$$
Since $\left|\mathfrak{L}_{Z}\left(\mathfrak{L}_{Z} \phi\right)\right|(\gamma(s)) \leq C r(\gamma(s))^{-5+\epsilon}(|Z|+1)^{2}(\gamma(s))$, similarly, we have the estimate
$$\begin{aligned}
r(x)^{3-\epsilon}\left|\Upsilon_{Z}^{*} \phi-\phi-\mathfrak{L}_{Z} \phi\right|(x) & \leq C \int_{0}^{1} \int_{0}^{t} r(\gamma(s))^{3-\epsilon}\left(r(\gamma(s))^{-5+\epsilon}(|Z|+1)^{2}(\gamma(s))\right) d s d t \\
& \leq C \int_{0}^{1} \int_{0}^{t} r(\gamma(s))^{-2}(|Z|+1)^{2}(\gamma(s)) d s d t \leq C\|Z\|_{C_{1}^{k+1, \alpha}}^{2}
\end{aligned}$$
By a similar calculation, for the higher order term $Q$ in (4.7) we also have
$$r(x)^{3-\epsilon}\left|\Upsilon_{Z}^{*} Q-Q-\mathfrak{L}_{Z} Q\right|(x) \leq C\|Z\|_{C_{1}^{k+1, \alpha}}^{2}$$
It follows that
$$\begin{aligned}
r(x)^{3-\epsilon}\left|\Upsilon_{Z}^{*} J_{1}-J_{1}-\mathfrak{L}_{Z} J_{1}\right|(x) & \leq r(x)^{3-\epsilon}\left\{\left|\Upsilon_{Z}^{*} J_{0}-J_{0}-\mathfrak{L}_{Z} J_{0}\right|(x)+\right. \\
& \left.\left.\left|\Upsilon_{Z}^{*} \phi-\phi-\mathfrak{L}_{Z} \phi\right|(x)\right\}+\left|\Upsilon_{Z}^{*} Q-Q-\mathfrak{L}_{Z} Q\right|(x)\right\} \\
& \leq C\|Z\|_{C_{1}^{k+1, \alpha}}^{2}
\end{aligned}$$
where $C$ is uniform for all $Z \in \mathbb{W}$ of sufficiently small norm. And similarly, for any $Z, Z^{\prime}$ in a small neighborhood of 0,
$$\begin{aligned}
\Upsilon_{Z}^{*} J_{1}-\Upsilon_{Z^{\prime}}^{*} J_{1} & =\Upsilon_{Z^{\prime}}^{*}\left(\left(\Upsilon_{Z^{\prime}}^{*}\right)^{-1} \circ \Upsilon_{Z}^{*} J_{1}-J_{1}\right) \\
& =\Upsilon_{Z^{\prime}}^{*}\left(\left(I d-\mathfrak{L}_{Z^{\prime}}+R^{\prime}\right) \circ\left(I d+\mathfrak{L}_{Z}+R\right) J_{1}-J_{1}\right)
\end{aligned}$$
where $R, R^{\prime}$ represents the corresponding higher order terms, and has estimate as in (6.19). Then we have
$$r^{3-\epsilon}\left|\Upsilon_{Z}^{*} J_{1}-\Upsilon_{Z^{\prime}}^{*} J_{1}-\mathfrak{L}_{Z-Z^{\prime}} J_{1}\right| \leq C \cdot\left\|Z-Z^{\prime}\right\|_{C_{1}^{k+1, \alpha}} \cdot\left(\|Z\|_{C_{1}^{k+1, \alpha}}+\left\|Z^{\prime}\right\|_{C_{1}^{k+1, \alpha}}\right)$$
Higher order derivative estimates are similar, and are omitted, and (6.10) follows. Then by (5.12) and (6.10) we can see that $\Upsilon^{*}$ is differentiable, and satisfies the condition of

Lemma 4.1. A similar estimate of higher order expansions of $\Upsilon^{*}$ shows that it is a smooth map near $(0,0)$. \(\square\)

Recall that
$$\mathbb{V}=\left\{\theta \in \mathcal{H}_{-3}\left(X, \operatorname{End}_{a}(T X)\right) \mid \theta=\mathfrak{L}_{Z} J, Z \in \mathbb{W}\right\} .$$
The deformations of complex structure arising from elements of $\mathbb{V}$ become trivial if one takes into account changes of coordinates at infinity, as the following theorem shows.

Theorem 6.4. Let ( $X, J_{0}, g_{0}$ ) be a Kähler ALE surface with $J_{0} \in C^{\infty}$ and $g_{0} \in C^{\infty}$. There exists an $\epsilon_{1}^{\prime}>0$ such that for any complex structure $\left\|J_{1}-J_{0}\right\|_{C_{\delta}^{k, \alpha}}<\epsilon_{1}^{\prime}$, where $k \geq 3, \alpha \in$ $(0,1), \delta \in(-2,-1)$, there exists a diffeomorphism $\Phi$, of the form $\Phi_{Y_{1}} \circ \Upsilon_{Z} \circ \Phi_{Y_{2}}$ for $Y_{1}, Y_{2} \in$ $C_{\delta+1}^{k+1, \alpha}(T X)$ and $Z \in \mathbb{W}$, such that $\nabla_{g_{0}}^{*}\left(E_{J_{0}}^{-1}\left(\Phi^{*}\left(J_{1}\right)\right)\right)=0$, and such that $E_{J_{0}}^{-1}\left(\Phi^{*}\left(J_{1}\right)\right)$ is $L^{2}$-orthogonal to $\mathbb{V}$. Furthermore, there exists a constant $C$ so that
$$\left\|E_{J_{0}}^{-1}\left(\Phi^{*} J_{1}\right)\right\|_{C_{-3}^{k, \alpha}}<C \epsilon_{1}^{\prime} .$$
Proof. Let $J_{1}=J_{0}(\phi)$, where $\phi \in C_{\delta}^{k, \alpha}\left(X, \Lambda^{0,1} \otimes \Theta\right)$, and $\bar{\partial} \phi+[\phi, \phi]=0$. By Lemma 5.3 and Theorem 4.3, without loss of generality, we may assume that $\phi=\phi(t) \in C_{-3}^{k, \alpha}\left(X, \Lambda^{0,1} \otimes \Theta\right)$, where $t \in B_{\epsilon_{1}} \subset \mathcal{H}_{-3}\left(X, \Lambda^{0,1} \otimes \Theta\right)$. In the following of the proof, we will fixed the ALE coordinate as in Lemma 6.1, and again for simplicity, we will assume that $Z_{1} \neq 0$.
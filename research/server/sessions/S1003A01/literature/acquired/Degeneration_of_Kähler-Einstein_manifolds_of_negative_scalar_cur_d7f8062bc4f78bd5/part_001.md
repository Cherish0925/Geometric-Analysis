---
retention_scope: session
part: 1
total_parts: 2
---

[Part 1/2 of: Degeneration of Kähler-Einstein manifolds of negative scalar curvature]

---
source_file: 1706_01518v1.pdf
converter: mathpix
format: mmd
---

\title{
DEGENERATION OF KÄHLER-EINSTEIN MANIFOLDS OF NEGATIVE SCALAR CURVATURE
}

\author{
JIAN SONG
}

\begin{abstract}
Let $\pi: \mathcal{X}^{*} \rightarrow B^{*}$ be an algebraic family of compact Kähler manifolds of complex dimension $n$ with negative first Chern class over a punctured disc $B^{*} \in \mathbb{C}$. Let $g_{t}$ be the unique Kähler-Einstein metric on $\mathcal{X}_{t}=\pi^{-1}(t)$. We show that as $t \rightarrow 0$, $\left(\mathcal{X}_{t}, g_{t}\right)$ converges in pointed Gromov-Hausdorff topology to a unique finite disjoint union of complete metric length spaces $\coprod_{\alpha=1}^{\mathcal{A}}\left(Y_{\alpha}, d_{\alpha}\right)$ with $\sum_{\alpha=1}^{\mathcal{A}} \operatorname{Vol}\left(Y_{\alpha}, d_{\alpha}\right)=\operatorname{Vol}\left(\mathcal{X}_{t}, g_{t}\right)$. Each $\left(Y_{\alpha}, d_{\alpha}\right)$ is a smooth open Kähler-Einstein manifold of complex dimension $n$ outside its closed singular set of Hausdorff dimension no greater than $2 n-4$. Furthermore, $\coprod_{\alpha=1}^{\mathcal{A}} Y_{\alpha}$ is a quasi-projective variety isomorphic to $\mathcal{X}_{0} \backslash \operatorname{LCS}\left(\mathcal{X}_{0}\right)$, where $\mathcal{X}_{0}$ is a projective semilog canonical model and $\operatorname{LCS}\left(\mathcal{X}_{0}\right)$ is the non-log terminal locus of $\mathcal{X}_{0}$. This is the first step of our approach toward compactification of the analytic geometric moduli space of Kähler-Einstein manifolds of negative scalar curvature.
\end{abstract}

\section*{Contents}
\begin{itemize}
\item[1.] Introduction 1
\item[2.] Semi-log canonical models and stable families of canonical models 6
\item[3.] Kähler-Einstein currents on semi-log canonical models
\item[4.] Analytic estimates for stable families of smooth canonical models
\item[5.] Gromov-Hausdorff convergence and partial $C^{0}$-estimates
\item[6.] Distance estimates
\item[7.] Proof of Theorem 1.2
\end{itemize}

References

\section*{1. Introduction}

The geometric and algebraic moduli space of compact Einstein manifolds is a fundamental problem in both differential geometry and algebraic geometry. Any compact Riemann surface is equipped with a unique metric of constant curvature in its conformal class. Fixing a Riemann surface $M$ with genus greater than one, the moduli space of complex structures on $M$ admits a unique Deligne-Mumford compactification [17] by adding Riemann surfaces with possible nodes on the boundary of the moduli. In particular, such Riemann surfaces admit a unique constant curvature metric with complete ends at the nodal points. In higher dimensions, one considers the Einstein manifolds $(M, g)$ with
$$\operatorname{Ric}(g)=\lambda g, \lambda=1,0,-1$$
instead of spaces of constant curvature.
In dimension 4, there are many deep results on the compactness of Einstein manifolds. In fact, it is proved in [30, 2, 45, 3] that any sequence of $\left(M_{i}, g_{i}\right)$ with uniform volume

\footnotetext{
Research supported in part by National Science Foundation grants DMS-1406124.
}
lower bound, diameter upper bound and $L^{2}$-curvature bound will converge to a compact Einstein orbifold, after passing to a subsequence. In the Kähler case, the compactness result holds when $\lambda=0$ with uniform volume upper and lower bounds, and when $\lambda=1$ without any assumption.

In higher dimension, very little is known about the compactness of the moduli of general Einstein manifolds. In the case of compact Kähler-Einstein manifolds, there have been many exciting breakthroughs. The partial $C^{0}$-estimates, proposed by Tian and established in [45, 18], are the fundamental tool to study analytic and geometric degeneration of Kähler-Einstein metrics. Any sequence of Kähler-Einstein manifolds $\left(M_{i}, g_{i}\right)$ with $\operatorname{Ric}\left(g_{i}\right)=\lambda g_{i}$ and $\lambda=1$ must converge in Gromov-Hausdorff topology, after passing to a subsequence, to a singular Kahelr-Einstein metric space homeomorphic to a projective variety with log terminal singularities ([18]). Such Kähler-Einstein manifolds of positive scalar curvature, the volume must be an integer and the diameter must uniformly bounded above. Therefore, one immediately obtains uniform non-collapsing conditions for all $\left(M_{i}, g_{i}\right)$ at each point, from the volume comparison theorem. The partial $C^{0}$-estimate can be then applied to understand the algebraic structures of the limiting Kähler-Einstein metric spaces by developing a connection between the analytic and geometric Kähler-Einstein metrics and the algebraic Bergman metrics. This approach is also used to prove the fundamental relationship between existence of Kähler-Einstein metrics and K-stablity on Fano manifolds (c.f. [11, 12, 13, 47] ).

However, when $\lambda=-1$, as one sees in the case of Riemann surfaces of high genus, the Einstein metrics can collapse at the complete ends. Such complete ends correspond to the nodes from algebraic degeneration of high genus Riemann surfaces. The major result in real dimension 4 is due to Cheeger-Tian [10], much later than the case of positive scalar curvature. They apply the chopping techniques [9] in the collapsing theory and a refined $\epsilon$ -regularity theorem for 4-folds to establish a non-collapsing result for Einstein 4-manifolds with uniformly bounded $L^{2}$-curvature. In particular, let $\left(M, J_{i}, g_{i}\right)$ be a sequence of Kähler-Einstein surfaces on a smooth manifold $M$ of real dimension 4, complex structure $J_{i}$ and $\operatorname{Ric}\left(g_{i}\right)=-g_{i}$. Then it is proved in [10] that $\left(M, J_{i}, g_{i}\right)$ converge in pointed Gromov-Hausdorff topology, after passing to a subsequence, to a finite disjoint union of complete orbifold Kähler-Einstein surfaces without loss of total volume.

In this paper, we aim to establish the first step towards the compactness of the space of Kähler-Einstein manifolds of negative scalar in all dimensions. We will consider any algebraic family
$$\pi: \mathcal{X}^{*} \rightarrow B^{*}$$
over a punctured disc $B^{*}=B \backslash\{0\}$ in $\mathbb{C}$ such that $\mathcal{X}_{t}=\pi^{-1}(t)$ is an $n$-dimensional Kähler manifold with $c_{1}\left(\mathcal{X}_{t}\right)<0$. Since $c_{1}\left(\mathcal{X}_{t}\right)<0$, or equivalently, the canonical bundle of $\mathcal{X}_{t}$ is ample, there exists a unique Kähler-Einstein metric $g_{t}$ on $\mathcal{X}_{t}$ satisfying
$$\operatorname{Ric}\left(g_{t}\right)=-g_{t} .$$
A natural question is how $\left(\mathcal{X}_{t}, g_{t}\right)$ behaves as $t \rightarrow 0$.
The first result was achieved in [44], where Tian considers a very special family $\pi$ : $\mathcal{X} \rightarrow B$ over a disc $B$ in $\mathbb{C}$ satisfying the following
\begin{itemize}
\item[(1)] $\mathcal{X}_{t}$ is an $n$-dimensional Kähler manifold with $c_{1}\left(\mathcal{X}_{t}\right)<0$ for each $t \in B^{*}$.
\item[(2)] The total space $\mathcal{X}$ is smooth.
\end{itemize}
\begin{itemize}
\item[(3)] The central fibre $\mathcal{X}_{0}=\cup_{\alpha=1}^{\mathcal{A}} X_{\alpha}$ is reduced and has only normal crossing singularities. In particular, each irreducible component $X_{\alpha}$ of $\mathcal{X}_{0}$ is a smooth Kähler manifold.
\item[(4)] Any three of the components of $\mathcal{X}_{0}$ have empty intersection.
\end{itemize}

It is shown in [44] that $\left(\mathcal{X}_{t}, g_{t}\right)$ must converge smoothly to a disjoint union of complete Kähler-Einstein manifolds $\coprod_{\alpha=1}^{\mathcal{A}}\left(Y_{\alpha}, g_{\alpha}\right)$ as $t \rightarrow 0$. In particular, $Y_{\alpha}=X_{\alpha} \backslash \mathcal{S}$, where $\mathcal{S}$ is the locus of the normal crossing singularities of $\mathcal{X}_{0}$. Tian's result was generalized slightly in [28, 32, 33], in particular, condition (4) is removed. However, the assumptions (2) and (3) are too strong. The recent development in algebraic moduli spaces of canonical models shows that in general, the total space has canonical singularities and the central fibre $\mathcal{X}_{0}$ has semi-log canonical singularities.

Therefore, we will consider the following degeneration of Kähler manifolds of negative first Chern class, i.e., smooth canonical models, in the language of birational geometry.

Definition 1.1. A holomorphic degeneration family $\pi: \mathcal{X} \rightarrow B$ over a disc $B \subset \mathbb{C}$ is said to be a stable degeneration if the following hold.
\begin{itemize}
\item[(1)] The total space $\mathcal{X}$ has canonical singularities.
\item[(2)] $\pi$ is a flat projective morphism.
\item[(3)] the fibre $\mathcal{X}_{t}$ is a smooth canonical model with $\operatorname{dim}_{\mathbb{C}} \mathcal{X}_{t}=n$ for each $t \in B^{*}$, i.e., $c_{1}\left(\mathcal{X}_{t}\right)<0$.
\item[(4)] The relative canonical sheaf $K_{\mathcal{X} / B}$ is a $\pi$-ample $\mathbb{Q}$-line bundle.
\item[(5)] The central fibre $\mathcal{X}_{0}$ is a semi-log canonical model.
\end{itemize}

The definition of a semi-log canonical models of general type and its non-log terminal locus LCS is given in Section 2 (c.f. Definition 2.2 ). Roughly speaking, a semi-log canonical model of general type is a projective variety whose codimensional one singularities are ordinary nodes, and its canonical divisor is an ample $\mathbb{Q}$-Cartier divisor. The non-log terminal locus is where the adapted volume measure is not locally integrable.

Before we state the compactness for $\left(\mathcal{X}_{t}, g_{t}\right)$ as $t \rightarrow 0$ of a stable degeneration of smooth canonical models of general type, we first construct a canonical Kähler-Einstein current on any semi-log canonical models of general type.

Theorem 1.1. Let $X$ be a semi-log canonical model with $\operatorname{dim}_{\mathbb{C}} X=n$. There exists a unique Kähler current $\omega_{K E} \in-c_{1}(X)$ such that
\begin{itemize}
\item[(1)] $\omega_{K E}$ is smooth on $\mathcal{R}_{X}$, the nonsingular part of $X$, and it satisfies the Kähler-Einstein equation on $\mathcal{R}_{X}$
$$\operatorname{Ric}\left(\omega_{K E}\right)=-\omega_{K E} .$$
\item[(2)] $\omega_{K E}$ has bounded local potentials on the quasi-projective variety $X \backslash \operatorname{LCS}(X)$, where $\operatorname{LCS}(X)$ is the non-log terminal locus of $X$. More precisely, let
$$\Phi: X \rightarrow \mathbb{C} \mathbb{P}^{N}$$
be a projective embedding of $X$ by a pluricanonical system $H^{0}\left(X, m K_{X}\right)$ for some $m \in \mathbb{Z}^{+}$and let $\chi=\left.\frac{1}{m} \omega_{F S}\right|_{X}$, where $\omega_{F S}$ is the Fubini-Study metric on $\mathbb{C P}^{N}$.
\end{itemize}
\begin{itemize}
\item[] Then $\omega_{K E}=\chi+\sqrt{-1} \partial \bar{\partial} \varphi_{K E}$ for some $\varphi_{K E} \in P S H(X, \chi)$ such that $\varphi \in L_{l o c}^{\infty}(X \backslash \operatorname{LCS}(X)), \varphi \rightarrow-\infty$ near $\operatorname{LCS}(X)$.
\item[(3)] The Monge-Ampère mass $\omega_{K E}^{n}$ does not charge mass on the singularities of $X$ and
$$\int_{X} \omega_{K E}^{n}=\left[K_{X}\right]^{n} .$$
\end{itemize}

The Kähler-Einstein currents on semi-log canonical models are first constructed in [5] using a variational method and they coincide with the Kähler-Einstein currents constructed in Theorem 1.1 by the uniqueness. The estimates on local boundedness of the Kähler-Einstein potentials in [5] are not sufficient to study the Riemannian geometric degeneration for a stable degeneration of smooth canonical models. Our approach is to combine the fundamental results [26, 20, 50] and the maximum principle with suitable barrier functions. This helps us to obtain local $L^{\infty}$-estimates of local potentials away from the non-log terminal locus of $X$. In fact, it is shown in Section 3 that $\varphi_{K E}$ is milder than any log poles.

We are now ready to state the following holomorphic compactness for the space of Kähler-Einstein manifolds with negative scalar curvature.

Theorem 1.2. Let $\pi: \mathcal{X} \rightarrow B$ be a stable degeneration of smooth canonical models of complex dimension $n$ over a disc $B \subset \mathbb{C}$. Suppose the central fibre $\pi^{-1}(0)$ is given by $\mathcal{X}_{0}=\bigcup_{\alpha=1}^{\mathcal{A}} X_{\alpha}$, where $\left\{X_{\alpha}\right\}_{\alpha}$ are the irreducible components of $\mathcal{X}_{0}$. Let $g_{t}$ be the unique Kähler-Einstein metric on $\mathcal{X}_{t}$ for $t \in B^{*}$ with
$$\operatorname{Ric}\left(g_{t}\right)=-g_{t} .$$
Then the following conclusions hold as $t \rightarrow 0$.
\begin{itemize}
\item[(1)] There exist points $\left(p_{t}^{1}, p_{t}^{2}, \ldots, p_{t}^{\mathcal{A}}\right) \in \mathcal{X}_{t} \times \mathcal{X}_{t} \times \ldots \times \mathcal{X}_{t}$ such that $\left(\mathcal{X}_{t}, g_{t}, p_{t}^{1}, \ldots, p_{t}^{\mathcal{A}}\right)$ converge in pointed Gromov-Hausdoff topology to a finite disjoint union of complete Kähler-Einstein metric spaces
$$\mathbf{Y}=\coprod_{\alpha=1}^{\mathcal{A}}\left(Y_{\alpha}, d_{\alpha}, y_{\alpha}\right) .$$
\item[(2)] Let $\mathcal{R}_{Y_{\alpha}}$ be the regular part of the metric space $\left(Y_{\alpha}, d_{\alpha}\right)$ for each $\alpha$. Then $\left(\mathcal{R}_{Y_{\alpha}}, d_{\alpha}\right)$ is a smooth Kähler-Einstein manifold of complex dimension $n$ and the singular set $\mathcal{S}_{\alpha}=Y_{\alpha} \backslash \mathcal{R}_{Y_{\alpha}}$ is closed and has Hausdorff dimension no greater than $2 n-4$.
\item[(3)] $\coprod_{\alpha=1}^{\mathcal{A}} Y_{\alpha}$ is homeomophic to $\mathcal{X}_{0} \backslash \operatorname{LCS}\left(\mathcal{X}_{0}\right)$, where $\operatorname{LCS}\left(\mathcal{X}_{0}\right)$ is the non-log terminal locus of $\mathcal{X}_{0} . \coprod_{\alpha=1}^{\mathcal{A}} \mathcal{R}_{Y_{\alpha}}$ is biholomorphic to the nonsingular part of $\mathcal{X}_{0}$.
\item[(4)] $\sum_{\alpha=1}^{\mathcal{A}} \operatorname{Vol}\left(Y_{\alpha}, d_{\alpha}\right)=\operatorname{Vol}\left(\mathcal{X}_{t}, g_{t}\right)$ for all $t \in B^{*}$, where $\operatorname{Vol}\left(Y_{\alpha}, d_{\alpha}\right)$ is the Hausdorff measure of $\left(Y_{\alpha}, d_{\alpha}\right)$.
\end{itemize}
In particular, the Kähler-Einstein metric induced by $d_{\mathbf{Y}}$ on $\bigcup_{\alpha=1}^{\mathcal{A}} \mathcal{R}_{Y_{\alpha}}$ coincides with the unique Kähler-Einstein current on $\mathcal{X}_{0}$ in Theorem 1.1.

Let us say a few words about the proof. In order to prove Theorem 1.2, we first have to achieve a uniform non-collapsing condition for $\left(\mathcal{X}_{t}, g_{t}\right)$, more precisely, we want to show that there exists $c>0$ and $p_{t} \in \mathcal{X}_{t}$ for all $t \in B^{*}$ such that
$$\operatorname{Vol}_{g_{t}}\left(B_{g_{t}}\left(p_{t}, 1\right)>c, \text { for all } t \in B^{*} .\right.$$
Without such a condition, the Cheeger-Colding theory cannot be applied. Such a non-collapsing condition is achieved by uniform analytic estimates using the algebraic semistable reduction. With the noncollapsing condition, the partial $C^{0}$-estimates will naturally hold by the fundamental work in [45, 18] (also [46] with an alternative approach). One of the difficult issues in the stable degeneration is that, the diameter will in general tend to $\infty$ and there must be collapsing at the complete ends in the limiting metric space. We will have to estimate the distance near the singular locus of $\mathcal{X}_{0}$. It turns out that the general principle for geometric Kähler currents applies, i.e., boundedness of the local potential is equivalent to boundedness of distance to a fixed regular base point. Such a principle is achieved by building a local Schwarz lemma with suitable auxiliary Kähler-Einstein currents and the $L^{\infty}$-estimates for degenerate complex Monge-Ampère equations from the capacity theory [26, 20, 50].

The recent progress in birational geometry enables the KSBA compatification of canonical models, where the boundary points are semi-log canonical models. Then Theorem 1.2 also shows that the Kähler-Einstein current on smoothable semi-log canonical models, or boundary points of the moduli of smooth canonical models, are indeed Riemannian geometric with good behaviors near singularities. The work of Hacon-Xu [23] shows that given any algebraic family of smooth canonical models $\mathcal{X}^{*}$ over a punctured disc $B^{*} \subset \mathbb{C}$, after a base change for $B^{*}$, one can uniquely fill in a central fibre $\mathcal{X}_{0}$ such that $\mathcal{X}_{0}$ is a semi-log canonical model and the total space $\mathcal{X}$ has only canonical singularities. Therefore, by assuming the results in birational geometry, we can remove the assumption on the stable degeneration in Theorem 1.2 and obtain a general holomorphic compactness result for Kähler-Einstein manifolds of negative scalar curvature.

Theorem 1.3. Let $\pi: \mathcal{X}^{*} \rightarrow B^{*}$ be an algebraic family of compact Kähler manifolds of complex dimension $n$ over a punctured disc $B^{*} \subset \mathbb{C}$. Suppose $c_{1}\left(\mathcal{X}_{t}\right)<0$ for each $\mathcal{X}_{t}=\pi^{-1}(t), t \in B^{*}$. Let $g_{t}$ be the unique Kähler-Einstein metric on $\mathcal{X}_{t}$ with
$$\operatorname{Ric}\left(g_{t}\right)=-g_{t} .$$
Then the following holds as $t \rightarrow 0$.
\begin{itemize}
\item[(1)] $\left(\mathcal{X}_{t}, g_{t}\right)$ converges in pointed Gromov-Hausdoff topology to a finite disjoint union of complete Kähler-Einstein metric spaces
$$\mathbf{Y}=\coprod_{\alpha=1}^{\mathcal{A}}\left(Y_{\alpha}, d_{\alpha}\right) .$$
\item[(2)] Let $\mathcal{R}_{Y_{\alpha}}$ be the regular part of $\left(Y_{\alpha}, d_{\alpha}\right)$ for each $\alpha$. Then $\left(R_{Y_{\alpha}}, d_{\alpha}\right)$ is a smooth Kähler-Einstein manifold of complex dimension $n$ and the singular set $\mathcal{S}_{\alpha}=Y_{\alpha} \backslash$ $\mathcal{R}_{Y_{\alpha}}$ is closed and has Hausdorff dimension no greater than $2 n-4$.
\item[(3)] There exists a unique projective variety $\mathcal{X}_{0}$ with semi-log canonical singularities and an ample $\mathbb{Q}$-Cartier canonical divisor $K_{\mathcal{X}_{0}}$ such that $\coprod_{\alpha=1}^{\mathcal{A}} Y_{\alpha}$ is homeomophic
\end{itemize}
to $\mathcal{X}_{0} \backslash \operatorname{LCS}\left(\mathcal{X}_{0}\right)$, where $\operatorname{LCS}\left(\mathcal{X}_{0}\right)$ is the non-log terminal locus of $\mathcal{X}_{0}$. In particular, $\coprod_{\alpha=1}^{\mathcal{A}} \mathcal{R}_{Y_{\alpha}}$ is biholomorphic to the nonsingular part of $\mathcal{X}_{0}$.
$$\sum_{\alpha=1}^{\mathcal{A}} \operatorname{Vol}\left(Y_{\alpha}, d_{\alpha}\right)=\operatorname{Vol}\left(\mathcal{X}_{t}, g_{t}\right) \text { for each } t \in B^{*} .$$

We believe that Theorem 1.3 will be crucial to establish a general compactness for the space of Kähler-Einstein manifolds with negative scalar curvature. Certainly, at this moment, we will have to assume the algebraic KSBA compatification of the moduli space of canonical models and turn the weak semi-stable reduction over higher dimensional base into suitable analytic and geometric estimates. It is also possible one can directly prove Theorem 1.3 without using the algebraic results of [23]. If so, one might use the compactness for holomorphic families of Kähler-Einstein manifolds to construct algebraic fill-in and use such an analytic approach to study the algebraic moduli problems.

There have been many results for the study of canonical Kähler metrics on projective varieties of non-negative Kodaira dimension using the Kähler-Ricci flow or deformation of Kähler metrics of Einstein type [37, 38, 35, 21]. Such deformation with both analytic and geometric estimates can also have applications in algebraic geometry, for example, an analytic proof of Kawamata's base point free theorem for minimal models of general type is obtained in [36]. More generally, the Kähler-Ricci flow is closely related to the minimal model program and the formation of finite time singularities is an analytic geometric transition of solitons for birational flips. A detailed program is laid out in [39] with partial geometric results obtained in [41, 42, 43, 34].

Theorem 1.2 is a major improvement of Theorem 1.5 in [35]. This paper will be incorporated and replace Section 5 in [35].

The organization of this article is as follows. A quick review is given in Section 2 for algebraic singularities and degenerations of canonical models. In Section 3, we prove Theorem 1.1 by establishing the existence and uniqueness of canonical Kähler-Einstein currents on semi-log canonical models with effective analytic estimates. In Section 4, we derive various analytic estimates for the family of Kähler-Einstein metrics with a stable degeneration. In particular, we prove a uniform noncollapsing result. In Section 5, we will apply the Cheeger-Colding theory for the Riemannian degeneration of Kähler-Einstein manifolds and establish local partial $C^{0}$-estimates. In Section 5, we prove the distance estimates and establish the principle that bounded local potential is equivalent to bounded local distance. In Section 6, we combine all the previous results and prove Theorem 1.2.

\section*{2. Semi-log canonical models and stable families of canonical models}

In this section, we will have a quick review of semi-log canonical models and the algebraic degeneration of canonical models of general type. First, let us recall the definition for log canonical singularities of a projective variety.

Definition 2.1. Let $X$ be a normal projective variety such that $K_{X}$ is a $\mathbb{Q}$-Cartier divisor. Let $\pi: Y \rightarrow X$ be a log resolution and $\left\{E_{i}\right\}_{i=1}^{p}$ the irreducible components of the exceptional locus $\operatorname{Exc}(\pi)$ of $\pi$. There there exists a unique collection $a_{i} \in \mathbb{Q}$ such that
$$K_{Y}=\pi^{*} K_{X}+\sum_{i=1}^{p} a_{i} E_{i} .$$

Then $X$ is said to have
\begin{itemize}
\item[-] terminal singularities if $a_{i}>0$, for all $i$.
\item[-] canonical singularities if $a_{i} \geq 0$, for all $i$.
\item[-] log terminal singularities if $a_{i}>-1$, for all $i$.
\item[-] log canonical singularities if $a_{i} \geq-1$, for all $i$.
\end{itemize}
A projective normal variety $X$ is said to be a canonical model of general type if $X$ has canonical singularities and $K_{X}$ is ample.

Smooth canonical models are simply Kähler manifolds of negative first Chern class. There always exists a unique Kähler-Einstein metric on smooth canonical models [4, 48]. The notion of semi-log canonical models is crucial in the degeneration of smooth canonical models (c.f. [25, 27]).

Definition 2.2. A reduced projective variety $X$ is said to be a semi-log canonical model if
\begin{itemize}
\item[(1)] $K_{X}$ is an ample $\mathbb{Q}$-Cartier divisor,
\item[(2)] $X$ has only ordinary nodes in codimension 1,
\item[(3)] For any log resolution $\pi: Y \rightarrow X$,
$$K_{Y}=\pi^{*} K_{X}+\sum_{i=1}^{I} a_{i} E_{i}-\sum_{j=1}^{J} F_{j},$$
where $E_{i}$ and $F_{j}$, the irreducible components of exceptional divisors, are smooth divisors of normal crossings with $a_{i}>-1$.
\end{itemize}

We denote the algebraic closed set $\mathrm{LCS}(X)=$ Supp $\left(\pi\left(\bigcup_{j=1}^{J} F_{j}\right)\right)$ in $X$ to be the locus of non-log terminal singularities of $X$. We also let $\mathcal{R}_{X}$ be the nonsingular part of $X$ and $\mathcal{S}_{X}$ the singular set of $X$.

We always require $X$ is $\mathbb{Q}$-Gorenstein and satisfies Serre's $S_{2}$ condition. We refer such algebraic notions to [27]. The non-log terminal locus is the set of singular points of $X$ with their discrepancy equal to -1. Analytically, such locus is the set of points near which the adapted volume measure is locally not integrable.

In general, $X$ is not normal. We first let $\nu: X^{\nu} \rightarrow X$ be the normalization of $X$ and
$$K_{X^{\nu}}=\nu^{*} K_{X}-\operatorname{cond}(\nu),$$
where $\operatorname{cond}(\nu)$ is a reduced effective divisor and is called the conductor. In fact, $\operatorname{cond}(\nu)$ is the inverse image of codimensional 1 ordinary nodes. $K_{X^{\nu}}+\operatorname{cond}(\nu)$ is a big and semiample divisor on $X^{\nu}$ and so the pair ( $X^{\nu}, K_{X^{\nu}}+\operatorname{cond}(\nu)$ ) has log canonical singularities. Let $\pi^{\nu}: Y \rightarrow X^{\nu}$ be a log resolution. Then $\pi=\nu \circ \pi^{\nu}: Y \rightarrow X$ is also a log resolution and
$$K_{Y}=\pi^{*} K_{X}+\sum a_{i} E_{i}-\sum F_{j}, a_{i}>-1,$$
where $E_{i}, F_{j}$ are the exceptional prime divisors of $\pi$. In other words, the normalization $\left(X^{\nu}\right)$ of $X$ gives rise to a log canonical pair $\left(X^{\nu}, \operatorname{cond}(\nu)\right)$. In particular, if one aims to construct a Kähler-Einstien metric $g_{K E}$ on $X, g_{K E}$ can be pull backed to a suitable Kähler current on $X^{\nu}$ in the class of $K_{X^{\nu}}+\operatorname{cond}(\nu)$.

We now consider the following algebraic degeneration of Kähler manifolds with negative first Chern class.

Definition 2.3. A flat projective morphism $\pi: \mathcal{X} \rightarrow B$ over a smooth Riemann surface $B$ is called a stable degeneration of smooth canonical models if it satisfies the following conditions.
\begin{itemize}
\item[(1)] $\mathcal{X}$ is a normal projective variety with canonical singularities,
\item[(2)] $K_{\mathcal{X}}$ is an $\pi$-ample $\mathbb{Q}$-Cartier divisor,
\item[(3)] $\mathcal{X}_{t}=\pi^{-1}(t)$ is a smooth canonical model of complex dimension $n$, for $t \neq 0$,
\item[(4)] $\mathcal{X}_{0}=\pi^{-1}(0)$ is a semi-log canonical model.
\end{itemize}

The analysis for Kähler-Einstien metrics on singular varieties is usually carried out on the nonsingular model, for example, the log resolution of the original variety. Therefore we would like to have a good nonsingular model for the stable degeneration $\pi: \mathcal{X} \rightarrow B$ so that $\mathcal{X}$ will be nonsingular and the central fibre is a reduced divisor of smooth components with normal crossings. The following resolution of singularities for families over a Riemann surface is called the semi-stable reduction, proved in [24].

Theorem 2.1. Let $\pi: \mathcal{X} \rightarrow B$ be a morphism from $\mathcal{X}$ onto a Riemann surface $B$. Suppose $0 \in B$ and $\pi: \mathcal{X} \backslash \pi^{-1}(0) \rightarrow B \backslash\{0\}$ is smooth. Then there exists a finite base change $f: B^{\prime} \rightarrow B$ and a blow-up morphism $\Psi: \mathcal{X}^{\prime} \rightarrow \mathcal{X} \times_{B} B^{\prime}$
![](https://cdn.mathpix.com/cropped/214fb33d-20fb-4355-9113-beb4c2d7f8f9-08.jpg?height=312&width=548&top_left_y=1246&top_left_x=796)
such that the induced morphism $\pi^{\prime}: \mathcal{X}^{\prime} \rightarrow B^{\prime}$ is semi-stable, i.e.,
\begin{itemize}
\item[(1)] $\mathcal{X}^{\prime}$ is nonsingular,
\item[(2)] $\left(\pi^{\prime}\right)^{-1}(0)$ is a reduced divisor with nonsingular components of normal crossings.
\end{itemize}

In this paper, we will always assume $B$ is a unit disc in $\mathbb{C}$ and let $t$ be the Euclidean holomorphic coordinate on $B$. The special fibre is given by $\pi^{-1}(0)$. We can calculate the relations of the canonical divisors in the case that $\pi: \mathcal{X} \rightarrow B$ is a stable degeneration of smooth canonical models. We assume that the base change $f$ is given by $t=f\left(t^{\prime}\right)=\left(t^{\prime}\right)^{d}$ for some $d \in \mathbb{Z}^{+}$.

Let $\Psi^{\prime}: \mathcal{X}^{\prime} \rightarrow \mathcal{X}$ be the morphism of the semi-stable reduction induced by $\Psi$ and $f$. Since $\mathcal{X}$ has canonical singularities, $\mathcal{X}^{\prime}$ also has canonical singularities. The base change has ramification along the central fibre of degree $d-1$ and so we have
$$K_{\mathcal{X} \times_{B} B^{\prime}}=\left(f^{\prime}\right)^{*} K_{\mathcal{X}}+(d-1) X_{0}^{\prime},$$
where $X_{0}^{\prime}$ is the strict transform of $\mathcal{X}_{0}$. Therefore
$$K_{\mathcal{X}^{\prime}}=\left(\Psi^{\prime}\right)^{*} K_{\mathcal{X}}+(d-1) \mathcal{X}_{0}^{\prime}+\sum a_{j} E_{j}$$
where $\mathcal{X}_{0}^{\prime}=\left(\pi^{\prime}\right)^{-1}(0)$ and $E_{j}$ are nonsingular components of the exceptional divisor with $a_{j} \geq 0$.

The following adapted volume measure is introduced in [20] to study the complex Monge-Ampère equations on singular projective varieties.

Definition 2.4. Let $Y$ be a projective variety of normal singularities with a $\mathbb{Q}$-Cartier canonical divisor $K_{Y} . \Omega$ is said to be an adapted measure on $Y$ if for any $z \in Y$, there exists an open neighborhood $U$ of $z$ such that
$$\Omega=f_{U}(\alpha \wedge \bar{\alpha})^{\frac{1}{m}},$$
where $f_{U}$ is the restriction of a smooth positive function on the ambient space of a projective embedding $U$ and $\alpha$ is a local generator of the Cartier divisor $m K_{Y}$ on $U$ for some $m \in \mathbb{Z}^{+}$.

The adapted volume measure can also be defined for semi-log canonical models via pluricanonical embeddings. However, such volume measures are not locally integrable near the non-log terminal locus.

Lemma 2.1. Let $\pi: \mathcal{X} \rightarrow B$ be a stable degeneration of smooth canonical models and $\pi^{\prime}: \mathcal{X}^{\prime} \rightarrow B^{\prime}$ be a semi-stable reduction as in Theorem 2.1. If $\sigma$ is a holomorphic section of $m K_{\mathcal{X} / B}$ for some $m \in \mathbb{Z}^{+}$and $t^{\prime}$ is holomorphic coordinate of $B^{\prime}$, then $d t^{\prime} \wedge d \overline{t^{\prime}} \wedge$ $\left(\Psi^{\prime}\right)^{*}\left((\sigma \wedge \bar{\sigma})^{1 / m}\right)$ is a smooth nonnegative real ( $2 n+2$ )-form on $\mathcal{X}^{\prime}$.

Proof. By definition of relative canonical bundle, $d t \wedge d \bar{t} \wedge(\sigma \wedge \bar{\sigma})^{1 / m}$ defines a smooth volume form on the regular part $\mathcal{R}_{\mathcal{X}}$ of $\mathcal{X}$, and for any adapted volume form $\Omega$ on $\mathcal{X}$
$$\sup _{\mathcal{R}_{X}} \frac{d t \wedge d \bar{t} \wedge(\sigma \wedge \bar{\sigma})^{1 / m}}{\Omega}<\infty .$$
We consider the pullback of the relative volume form $\left.\left(\Psi^{\prime}\right)^{*}(\sigma \wedge \bar{\sigma})^{1 / m}\right)$. Let $\Omega^{\prime}$ be a smooth volume form on $\mathcal{X}^{\prime}$. Then we have
$$\frac{d t^{\prime} \wedge d \bar{t}^{\prime} \wedge\left(\Psi^{\prime}\right)^{*}\left((\sigma \wedge \bar{\sigma})^{1 / m}\right)}{\Omega^{\prime}}=\left(\frac{\left(\Psi^{\prime}\right)^{*} \Omega}{d^{2}\left|t^{\prime}\right|^{2(d-1)} \Omega^{\prime}}\right)\left(\Psi^{\prime}\right)^{*}\left(\frac{d t \wedge d \bar{t} \wedge(\sigma \wedge \bar{\sigma})^{1 / m}}{\Omega}\right) .$$
Since the volume measure $\left(\Psi^{\prime}\right)^{*} \Omega$ on $\mathcal{X}^{\prime}$ vanishes along $\mathcal{X}_{0}^{\prime}$ of order at least $2(d-1)$, therefore $d t \wedge d \overline{t^{\prime}} \wedge\left(\Psi^{\prime}\right)^{*}\left((\sigma \wedge \bar{\sigma})^{1 / m}\right)$ is a smooth nonnegative real $2 n+2$-form on $\mathcal{X}^{\prime}$. \(\square\)

The following theorem is due to Hacon and Xu [23]. It establishes the unique compactification of an algebraic family of smooth canonical models over a punctured disc $B^{*}$ in $\mathbb{C}$. In the particular, the unique fill-in for the central fibre, possibly after a base change, is a semi-log canonical model.

Theorem 2.2. Let $\pi: \mathcal{X}^{*} \rightarrow B^{*}$ be an algebraic family of smooth canonical models over a punctured dicc $B^{*}=B \backslash\{0\} \subset \mathbb{C}$. Then after a possible base change $f: B^{\prime} \rightarrow B$, there exists a unique $\pi^{\prime}: \mathcal{X}^{\prime} \rightarrow B^{\prime}$ as an extension of $\mathcal{X}^{*} \times_{B^{*}}\left(B^{\prime}\right)^{*} \rightarrow\left(B^{\prime}\right)^{*}$ such that $\mathcal{X}^{\prime}$ has canonical singularities and the central fibre $\mathcal{X}_{0}^{\prime}=\left(\pi^{\prime}\right)^{-1}(0)$ is a semi-log canonical model.

Theorem 1.3 will immediately follow from Theorem 1.2 if we apply the algebraic result of Theorem 2.2.

\section*{3. Kähler-Einstein currents on semi-log canonical models}

In this section, we will construct unique Kähler-Einstein currents on semi-log canonical models. Such canonical currents are already constructed in [5] by a variational method. We give a different approach by combining the work of [26, 20, 50] and the maximum principle to establish $L^{\infty}$-estimate for the local potentials of such Kähler-Einstein currents away from LCS, the non-log terminal locus. Such estimates are particularly important to study the geometric degeneration of smooth canonical models and to establish Riemannian geometric properties of such analytically constructed Kähler-Einstein currents.

Let $X$ be a semi-log canonical model of with $\operatorname{dim}_{\mathbb{C}} X=n$. We follow the standard scheme for the construction of Kähler-Einstein currents by reducing the Kähler-Einstein equation on $X$ to a complex Monge-Ampère equation on the nonsingular model of $X$.

The first technical preparation is to construct good barrier functions for estimates of local potentials. Such construction relies on a suitable choice of complex hypersurfaces in $X$.

Lemma 3.1. For any point $p \in X \backslash \operatorname{LCS}(X)$, there exists an effective $\mathbb{Q}$-divisor $G_{p}$ such that $G_{p}$ is numerically equivalent to $K_{X}$ and
$$p \notin G_{p}, \operatorname{LCS}(X) \subset G_{p} .$$
Proof. Since $X$ is projective, we can choose an effective ample $\mathbb{Q}$-divisor $G_{1}$ such that $p \notin G_{1}$. We let $\sigma_{1}$ be the defining section of $m_{1} G_{1}$ for some $m_{1} \in \mathbb{Z}^{+}$so that $m_{1} G_{1}$ is Cartier. Since $G_{1}$ is ample, $X_{1}=X \backslash G_{1}$ is an affine variety in $\mathbb{C}^{N}$ for some large $N$. Hence we can pick a polynomial $f$ on $\mathbb{C}^{N}$ such that $f(p) \neq 0$ and $f$ vanishes on the affine variety $\operatorname{LCS}(X) \cap X_{1}$. The restriction of $f$ to $X$ is a meromorphic function with poles along $G_{1}$. By choosing sufficiently large $k \in \mathbb{Z}^{+}, \sigma_{2}=f \sigma_{1}^{k}$ is a holomorphic section of a line bundle associated to the Cartier divisor $G_{2}=k m_{1} G_{1}$ over $X$ such that $\sigma_{2}$ vanishes on $\operatorname{LCS}(X)$ and $\sigma_{2}(p) \neq 0$. For sufficiently large $m_{2} \in \mathbb{Z}^{+}, m_{2} K_{X}-G_{2}$ is an ample Cartier divisor. So there exist $m_{3} \in \mathbb{Z}^{+}$and a holomorphic section $\sigma_{3} \in H^{0}\left(X, m_{3}\left(m_{2} K_{X}-G_{2}\right)\right)$ such that $\sigma_{3}(p) \neq 0$. Finally we let $m G_{p}$ be the divisor of zeros of $\sigma_{2}^{m_{3}} \sigma_{3}$ and the lemma is proved. \(\square\)

For any $q \in \operatorname{LCS}(X)$, we can also find $G_{p_{1}}, \ldots, G_{p_{k}}$, by the construction of $G_{p}$ in Lemma 3.1, such that the common zeros of $G_{p_{1}}, \ldots, G_{p_{k}}$ in an open neighborhood $U$ of $q$ coincide with $\mathrm{LCS}(X) \cap U$. Without loss of generality, we can consider the projective embedding $\Phi: X \rightarrow \mathbb{C P}^{N}$ by the pluricanonical system $H^{0}\left(X, m K_{X}\right)$ for some sufficiently large $m$ defined by $\Phi(x)=\left[\eta_{0}(x), \ldots, \eta_{N}(x)\right] \in \mathbb{C P}^{N}$ for a basis $\left\{\eta_{j}\right\}_{j=0}^{N}$ of $H^{0}\left(X, m K_{X}\right)$. We then choose the adapted volume measure $\Omega$ on $X$ by
$$\Omega=\left(\sum_{j=0}^{N} \eta_{j} \overline{\eta_{j}}\right)^{1 / m} .$$
We also define the curvature of $\Omega$ by
$$\chi=\sqrt{-1} \partial \bar{\partial} \log \Omega .$$
In fact, we can define $h_{\Omega}=\left(\sum_{j=0}^{N} \eta_{j} \wedge \overline{\eta_{j}}\right)^{-1 / m}$ as a hermtian metric on $K_{X}$. Obviously, $m \chi$ is the restriction of the Fubini-Study metric of $\mathbb{C P}^{N}$ to $X$.

The complex Monge-Ampère equation of our interest in relation to the Kähler-Einstein equation on $X$ is given by
$$(\chi+\sqrt{-1} \partial \bar{\partial} \varphi)^{n}=e^{\varphi} \Omega .$$
We have to prescribe singularities of the solution $\varphi$ to obtain a canonical and unique Kähler-Einstein current on $X$. To do so, we lift all the data to a log resolution $\pi: Y \rightarrow X$. By definition of semi-log canonical singularities,
$$K_{Y}=\pi^{*} K_{X}+\sum_{i} a_{i} E_{i}-\sum_{j} b_{j} F_{j}, a_{i} \geq 0,0<b_{j} \leq 1 .$$

We approximate equation (3.3) in the following way. We pull back all the data from $X$ to $Y$. Let $\sigma_{E}$ be the defining section for $E=\sum_{i=1}^{I} a_{i} E_{i}$ and $\sigma_{F}$ be the defining section for $F=\sum_{j=1}^{J} b_{j} F_{j}$ (possibly multivalued). We equip the line bundles associated to $E$ and $F$ with smooth hermitian metric $h_{E}, h_{F}$ on $Y$. Let $\Omega_{Y}$ be a smooth strictly positive volume form on $Y$ defined by
$$\Omega_{Y}=\left(\left|\sigma_{E}\right|_{h_{E}}^{2}\right)^{-1}\left|\sigma_{F}\right|_{h_{F}}^{2} \Omega .$$

Let $\theta$ be a fixed smooth Kähler form on $Y$ and we consider the following family of complex Monge-Ampère equations on $Y$ for $s \in(0,1)$,
$$\left(\chi+s \theta+\sqrt{-1} \partial \bar{\partial} \psi_{s}\right)^{n}=e^{\psi_{s}}\left(\left|\sigma_{E}\right|_{h_{E}}^{2}+s\right)\left(\left|\sigma_{F}\right|_{h_{F}}^{2}+s\right)^{-1} \Omega_{Y} .$$
For each $0<s<1$, by the result of [4, 48], there exists a unique smooth solution $\psi_{s}$ solving equation (3.4). When $s=0$, equation (3.4) coincides with equation (3.3).

We introduce two more parameter $\delta$ and $\epsilon$ in order to apply the maximum principle and consider the following family of complex Monge-Ampère equations
$$\left((1+\delta) \chi+s \theta+\sqrt{-1} \partial \bar{\partial} \psi_{p, s, \delta, \epsilon}\right)^{n}=\frac{e^{\psi_{p, s, \delta, \epsilon}}\left(\left|\sigma_{G_{p}}\right|_{h_{\Omega}}^{2 \epsilon}+s\right)\left(\left|\sigma_{E}\right|_{h_{E}}^{2}+s\right)}{\left(\left|\sigma_{F}\right|_{h_{F}}^{2}+s\right)} \Omega_{Y} .$$
Here both $\delta$ and $\epsilon$ are sufficiently small and we require $\epsilon>0$.
Lemma 3.2. For any $p \in X \backslash \operatorname{LCS}(X)$ and any $\epsilon_{0}>0$, there exist $\delta_{0}>0, C>0$ and $C^{\prime}=C^{\prime}\left(p, \epsilon_{0}\right)>0$ such that for any $-\delta_{0} \leq \delta \leq \delta_{0}, 0<s<1$, and $0<\epsilon<\epsilon_{0} / 2$, the solution $\psi_{p, s, \delta, \epsilon}$ of equation (3.5) satisfies the following estimate on $Y$,
$$\epsilon_{0} \log \left|\sigma_{G_{p}}\right|_{h_{\Omega}}^{2}-C^{\prime} \leq \psi_{p, s, \delta, \epsilon} \leq C .$$
Proof. We will pick an effective $\mathbb{Q}$-Cartier divisor $G_{p}$ from Lemma 3.1. Since $G_{p}$ is a $\mathbb{Q}$-Cartier divisor numerically equivalent to the ample divisor $K_{X}$, we will choose $h_{\Omega}$ as the hermitian metric for $G_{p}$ and we let $\sigma_{G_{p}}$ be the defining section of $G_{p}$. We first fix a sufficiently small $\delta_{0} \geq 3 \epsilon_{0}>0$ and consider the following family of equations on $Y$
$$\left((1+\delta) \chi+s \theta+\sqrt{-1} \partial \bar{\partial} \psi_{p, s, \delta, \epsilon_{0}}\right)^{n}=\frac{e^{\psi_{p, s, \delta, \epsilon_{0}}}\left(\left|\sigma_{G_{p}}\right|_{h_{\Omega}}^{2 \epsilon_{0}}+s\right)\left(\left|\sigma_{E}\right|_{h_{E}}^{2}+s\right)}{\left|\sigma_{F}\right|_{h_{F}}^{2}+s} \Omega_{Y},$$
where $-\delta_{0} \leq \delta \leq \delta_{0}$.

Since $G_{p}$ vanishes along $F$, there exist $\eta=\eta\left(\epsilon_{0}\right)>0$ and $K=K\left(\epsilon_{0}, \delta_{0}\right)>0$ such that for all $0<s<1$, we have
$$\left\|\frac{\left(\left|\sigma_{G_{p}}\right|_{h_{\Omega}}^{2 \epsilon_{0}}+s\right)\left(\left|\sigma_{E}\right|_{h_{E}}^{2}+s\right)}{\left|\sigma_{F}\right|_{h_{F}}^{2}+s}\right\|_{L^{1+\eta}\left(Y, \Omega_{Y}\right)} \leq K .$$
Then the results of [26, 20, 50] imply that there exists $C_{1}=C_{1}\left(p, \delta_{0}, \epsilon_{0}\right)>0$ such that for all $3|\delta| \leq \delta_{0}, 0<s<1$,
$$\left\|\psi_{p, s, \delta, \epsilon_{0}}\right\|_{L^{\infty}(Y)} \leq C_{1} .$$

Now we will compare $\psi_{p, s, \delta, \epsilon}$ to $\psi_{p, s, \delta^{\prime}, \epsilon_{0}}$ by applying the maximum principle. Let
$$\phi=\psi_{p, s, \delta, \epsilon}-\psi_{p, s, \delta^{\prime}, \epsilon_{0}}-\epsilon_{0} \log \left|\sigma_{G_{p}}\right|_{h_{\Omega}}^{2} .$$
Then $\phi$ satisfies the following equation
$$\frac{\left(\left(1+\delta^{\prime}\right) \chi+s \theta+\sqrt{-1} \partial \bar{\partial} \psi_{p, s, \delta^{\prime}, \epsilon_{0}}+\left(\delta-\delta^{\prime}-\epsilon_{0}\right) \chi+\sqrt{-1} \partial \bar{\partial} \phi\right)^{n}}{\left(\left(1+\delta^{\prime}\right) \chi+s \theta+\sqrt{-1} \partial \bar{\partial} \psi_{p, s, \delta^{\prime}, \epsilon_{0}}\right)^{n}}=e^{\phi}\left(\frac{\left|\sigma_{G_{p}}\right|_{h_{\Omega}}^{2 \epsilon}+s}{1+s\left|\sigma_{G_{p}}\right|_{h_{\Omega}}^{-2 \epsilon_{0}}}\right) .$$

We choose $\delta^{\prime}=-\delta_{0}$ and require $0<\epsilon<\epsilon_{0}$. Since $\phi$ is smooth away from the zeros of $G_{p}$ and $\phi$ tends to $\infty$ near zeros of $G_{p}$, we are able to apply the maximum principle to the minimum of $\phi$ and there exists $C_{2}>0$ such that
$$\inf _{\widetilde{X}} \phi \geq-C_{2},$$
Since $\psi_{p, s, \delta^{\prime}, \epsilon_{0}}$ is bounded, there exists $C_{3}>0$ such that for all $3 \delta \in\left(-\delta_{0}, \delta_{0}\right), 0<s<1$ and $\epsilon \in\left(0, \epsilon_{0} / 2\right)$,
$$\psi_{p, s, \delta, \epsilon} \geq-C_{3}+\epsilon_{0} \log \left|\sigma_{G_{p}}\right|_{h_{\Omega}}^{2} .$$

It is easier to obtain the upper bound of $\psi_{p, s, \delta, \epsilon}$. We consider the quantity
$$\phi^{\prime}=\psi_{p, s, \delta, \epsilon}-\psi_{p, s, \delta^{\prime}, \epsilon_{0}}$$
and use similar argument by choosing $\delta^{\prime}=\delta_{0}$. \(\square\)

Next, we will prove second order estimates with bounds from suitable barrier functions. There exists an effective Cartier divisor $D$ on $Y$ such that for any sufficiently small $s>0$,
$$\pi^{*} K_{X}-s D$$
is ample. In particular, we can assume that the support of $D$ coincides with the support of the exceptional divisor because $K_{X}$ is ample on $X$. We let $\sigma_{D}$ be the defining section of $D$ and choose a smooth hermitian metric $h_{D}$ on the line bundle associated to $D$ such that for any sufficiently small $s>0$,
$$\chi-\operatorname{sRic}\left(h_{D}\right)>0 .$$

Lemma 3.3. For any $p \in X \backslash \operatorname{LCS}(X)$, there exist $\lambda, \delta_{1}, \epsilon_{1}>0$ and $C=C\left(\delta_{1}, \epsilon_{1}\right)>0$ such that for all $-\delta_{1}<\delta<\delta_{1}, 0<\epsilon<\epsilon_{1}$ and $0<s<1$,
$$\left.\sup _{Y}\left(|\sigma|_{h_{D}}^{2}\left|\sigma_{G_{p}}\right|_{h_{\Omega}}^{2}\right)\right)^{2 \lambda}\left(\Delta_{\theta} \psi_{p, s, \delta, \epsilon}\right) \leq C,$$
where $\Delta_{\theta}$ is the Laplace operator with respect to the Kähler metric $\theta$.

Proof. Let $\omega=(1+\delta) \chi+s \theta+\sqrt{-1} \partial \bar{\partial} \psi_{p, s, \delta, \epsilon}$. Then we consider the quantity
$$H=\log \operatorname{tr}_{\theta}(\omega)-A^{3} \psi_{p, s, \delta, \epsilon}+A^{2} \log |\sigma|_{h_{D}}^{2}+A \log \left|\sigma_{G_{p}}\right|_{h_{\Omega}}^{2}$$
for some sufficiently large $A>0$ to be determined. Straightforward calculations show that there exists $C>0$ such that for all $\delta \in\left(-\delta_{1}, \delta_{1}\right), \epsilon \in\left(0, \epsilon_{1}\right)$ and $0<s<1$,
$$\begin{aligned}
\Delta_{\omega} H & \geq \operatorname{tr}_{\omega}\left(\left(A^{3}(1+\delta)-A\right) \chi-A^{2} \operatorname{Ric}\left(h_{D}\right)-\left(C-A^{3} s\right) \theta-n A^{3}\right. \\
& \geq \operatorname{Atr}_{\omega}(\theta)-n A^{3} .
\end{aligned}$$
We remark that we view $\chi$ as the pullback of the Fubini-Study metric from the projective embedding of $X$ and so the curvature of $\chi$ is uniformly bounded on the projective space. Applying the maximum principle, at the minimal point $x_{\text {min }}$ of $H$,
$$\operatorname{tr}_{\omega}(\theta) \leq n A^{2} .$$
Using the geometric mean value inequality combined with the Monge-Ampère equation (3.5), there exists $C=C(A)>0$ such that
$$H\left(x_{\min }\right) \leq C-A^{3}\left(\psi_{p, s, \delta, \epsilon}-A^{-1} \log \left|\sigma_{G_{p}}\right|_{h_{\Omega}}^{2}\right)\left(x_{\min }\right) .$$
for sufficiently large $A>0$. By Lemma 3.2, $\psi_{p, s, \delta, \epsilon}-A^{-1} \log \left|\sigma_{G_{p}}\right|_{h_{\Omega}}^{2}$ is bounded below for all sufficiently small $\delta$ and $0<\epsilon \ll A^{-1}$. Therefore for all sufficiently small $\epsilon>0$ and $\delta$, there exists $C>0$ such that on $Y$, we have
$$\left.\operatorname{tr}_{\theta}(\omega) \leq C\left(|\sigma|_{h_{D}}^{2}\left|\sigma_{G_{p}}\right|_{h_{\Omega}}^{2}\right)\right)^{-2 \lambda} .$$
This proves the lemma. \(\square\)

The following lemma on local high regularity of $\psi_{p, s, \delta, \epsilon}$ is established by the standard linear elliptic theory after applying Lemma 3.3 and linearizing the complex Monge-Ampère equation (3.7).

Lemma 3.4. For any $p \in X \backslash \operatorname{LCS}(X), k \geq 0$ and any compact $K \subset \subset \mathcal{R}_{X} \backslash G_{p}$, there exist $\delta_{2}>0, \epsilon_{2}>0$ and $C=C\left(p, k, K, \delta_{2}, \epsilon_{2}\right)>0$ such that for any $-\delta_{2} \leq \delta \leq \delta_{2}$, $0<\epsilon \leq \epsilon_{2}$ and $0<s<1$
$$\left\|\psi_{p, s, \delta, \epsilon}\right\|_{C^{k}(K)} \leq C .$$

Before we take $\delta, \epsilon, s \rightarrow 0$, we derive a uniform estimate with respect to variations by the parameters $\delta, \epsilon$, and $t$.

Lemma 3.5. For any $p \in X \backslash \operatorname{LCS}(X), k \geq 0$, any compact $K \subset \subset \mathcal{R}_{X} \backslash G_{p}$, there exist $\delta_{3}>0, \epsilon_{3}>0$ and $C=C\left(p, K, \delta_{3}, \epsilon_{3}\right)>0$ such that for any $-\delta_{3} \leq \delta \leq \delta_{3}, 0<\epsilon \leq \epsilon_{3}$ and $0<s<1$, we have
$$\left|\frac{\partial \psi_{p, s, \delta, \epsilon}}{\partial \delta}\right|_{L^{\infty}(K)}+\left|\frac{\partial \psi_{p, s, \delta, \epsilon}}{\partial \epsilon}\right|_{L^{\infty}(K)}+\left|\frac{\partial \psi_{p, s, \delta, \epsilon}}{\partial s}\right|_{L^{\infty}(K)} \leq C .$$
Proof. By the implicit function theorem, the solutions of (3.7) must be smooth with respect to the parameters $\delta, \epsilon$ and $s$. Let $f=\frac{\partial \psi_{p, s, \delta, \epsilon}}{\partial \delta}$. Then $f \in C^{\infty}(Y)$ and
$$\Delta_{p, s, \delta, \epsilon} f=-t r_{\omega_{p, s, \delta, \epsilon}}(\chi)+f,$$
where $\Delta_{p, s, \delta, \epsilon}$ is the Laplace operator associated to the metric
$$\omega=(1+\delta) \chi+s \theta+\sqrt{-1} \partial \bar{\partial} \varphi_{p, s, \delta, \epsilon} .$$

The function $H=f-10 \psi_{p, s, \delta, \epsilon}+\log \left|\sigma_{G_{p}}\right|_{h_{\Omega}}^{2}$ satisfies the following equation
$$\Delta_{p, s, \delta, \epsilon} H \geq f-10 n=H+10 \psi_{p, s, \delta, \epsilon}-\log \left|\sigma_{G_{p}}\right|_{h_{\Omega}}^{2}-10 n .$$
Then for all sufficiently small $\delta$ and $\epsilon>0, H$ is uniformly bounded above and so $f$ is uniformly bounded above on any compact subset in $X \backslash G_{p}$. Estimates for $\left|\frac{\partial \psi_{p, s, \delta, \epsilon}}{\partial \epsilon}\right|$ and $\left|\frac{\partial \psi_{p, s, \delta, \epsilon}}{\partial s}\right|$ can be achieved similarly. \(\square\)

Now we are able to solve equation (3.3).
Lemma 3.6. For any $p \in X \backslash \operatorname{LCS}(X)$, there exists $\varphi \in P S H(X, \chi)$ satisfying the following conditions.
\begin{itemize}
\item[(1)] $\varphi \in L_{\text {loc }}^{\infty}\left(X \backslash G_{p}\right) \cap C^{\infty}\left(\mathcal{R}_{X} \backslash G_{p}\right)$ and $\varphi$ solves equation (3.3), where $G_{p}$ is defined in Lemma 3.1.
\item[(2)] For any $\epsilon>0$ and $p \in X \backslash \operatorname{LCS}(X)$, there exists $C_{p, \epsilon}>0$ such that
$$\varphi \geq \epsilon \log \left|\sigma_{G_{p}}\right|_{h_{\Omega}}^{2}-C_{p, \epsilon} .$$
\item[(3)] Let $\omega_{K E}=\chi+\sqrt{-1} \partial \bar{\partial} \varphi$. Then $\operatorname{Ric}\left(\omega_{K E}\right)=-\omega_{K E}$ on $\mathcal{R}_{X}$ and extends to the Kähler-Einstein equation as currents to $X$.
\item[(4)] $\varphi=-\infty$ on $\operatorname{LCS}(X)$.
\item[(5)] $\int_{\mathcal{R}_{X} \backslash G_{p}}\left(\omega_{K E}\right)^{n}=\left[K_{X}\right]^{n}$.
\item[(6)] $\varphi=\lim _{s, \delta, \epsilon \rightarrow 0} \psi_{p, s, \delta, \epsilon}$.
\end{itemize}
Proof. Since for any $p \in X \backslash \operatorname{LCS}(X)$ and any sufficiently small $\delta$ and $\epsilon$, we have uniform estimates for $\psi_{p, s, \delta, \epsilon}$ away from $G_{p}$, for any sequence $s_{j}, \delta_{j}, \epsilon_{j} \rightarrow 0$, we can assume $\psi_{p, s_{j}, \delta_{j}, \epsilon_{j}}$ converges, after passing to a subsequence, to some
$$\varphi \in P S H(Y, \chi) \cap C^{\infty}\left(Y \backslash G_{p}\right) .$$
In particular, there exists $C>0$ and for any $\epsilon>0$, there exists $C_{\epsilon}>0$ such that
$$\epsilon \log \left|\sigma_{G_{p}}\right|_{h_{\Omega}}^{2}-C_{\epsilon} \leq \varphi \leq C .$$
(1), (2) and (3) can be proved from the above conclusion by passing the estimates of $\psi_{p, s, \delta, \epsilon}$ to the limit $\varphi$. Furthermore, $\varphi$ solves equation (3.3) on $\mathcal{R}_{X}$.
(4) can be reduced to the following statement: Suppose $\phi$ is a plurisubharmonic function on the unit ball $B \subset \mathbb{C}^{n}$ such that
$$\int_{B}\left|z_{1}\right|^{-2} e^{\phi}(\sqrt{-1})^{n} d z_{1} \wedge d \overline{z_{1}} \wedge \ldots \wedge d z_{n} \wedge d \overline{z_{n}}<\infty,$$
then $\phi$ tends to $-\infty$ near $B \cap\left\{z_{1}=0\right\}$. Such a statement is proved by Berndtsson (c.f. Lemma 2.7 in [5]). $\varphi$ is locally bounded and the fibre of $\pi$ over the log terminal locus is connected. On the other hand, $\varphi$ tends to $-\infty$ near $\pi^{-1}(\operatorname{LCS}(X))$ in $Y$. Otherwise there exists a curve $C$ in exceptional divisor and $C$ intersects at least one exceptional divisor with discrepancy -1, and so $\varphi$ must be constant on $C$ since it is pluriharmonic with singularities better than any log poles. This leads to contradiction and so $\varphi$ must tend to $-\infty$ near $\pi^{-1}(\operatorname{LCS}(X))$. Therefore the function $\varphi$ can uniquely descend to $X \backslash \operatorname{LCS}(X)$.
(5) follows because $\varphi$ is better than log poles along $G_{p}$ and thus $\sqrt{-1} \partial \bar{\partial} \varphi$ does not charge any mass along the singularities of $X$. More precisely, we let
$$v_{\epsilon, K}=\epsilon \log \left|\sigma_{G_{p}}\right|_{h_{\Omega}}^{2}+K, E_{\epsilon, K}=\left\{\varphi<v_{\epsilon, K}\right\} .$$
Then $\chi+\sqrt{-1} \partial \bar{\partial} v_{\epsilon, K}=(1-\epsilon) \chi \geq 0$ on $X \backslash G_{p}$. For any compact set $U \subset \subset X \backslash G_{p}$ and $\epsilon>0$, one can choose sufficiently large $K$ such that $U \subset E_{\epsilon, K} \subset \subset X \backslash G_{p}$. By comparison principle,
$$\int_{\mathcal{R}_{X}}\left(\omega_{K E}\right)^{n}>\int_{E_{\epsilon, K}}(\chi+\sqrt{-1} \partial \bar{\partial} \varphi)^{n} \geq \int_{E_{\epsilon, K}}\left(\chi+\sqrt{-1} \partial \bar{\partial} v_{\epsilon, K}\right)^{n} \geq(1-\epsilon) \int_{U} \chi^{n} .$$
By letting $K \rightarrow \infty$ and then $\epsilon \rightarrow 0$, we show that
$$\int_{\mathcal{R}_{X} \backslash G_{p}}\left(\omega_{K E}\right)^{n} \geq\left[K_{X}\right]^{n} .$$
Similarly, by comparing $\varphi$ to $u_{\epsilon, K}=-\epsilon \log \left|\sigma_{G_{p}}\right|_{h_{\Omega}}^{2}$, we can also show that
$$\int_{\mathcal{R}_{X} \backslash G_{p}}\left(\omega_{K E}\right)^{n} \leq\left[K_{X}\right]^{n} .$$
(6) can be proved as follows. Suppose $\varphi^{\prime} \in P S H(Y, \chi) \cap C^{\infty}\left(Y \backslash G_{p}\right)$ is a sequential limit of another sequence $\psi_{p, s_{j}, \delta_{j}, \epsilon_{j}}$. Then by the estimates in Lemma 3.5, on any compact set $K \subset \subset X \backslash G_{p}$, there exists $C>0$ such that for sufficiently large $j>0$,
$$\sup _{K}\left|\psi_{p, s_{j}, \delta_{j}, \epsilon_{j}}-\psi_{p, s_{j}^{\prime}, \delta_{j}^{\prime}, \epsilon_{j}^{\prime}}\right| \leq C\left(\left|\delta_{j}-\delta_{j}^{\prime}\right|+\left|\epsilon_{j}-\epsilon_{j}^{\prime}\right|+\left|s_{j}-s_{j}^{\prime}\right|\right) .$$
This implies that
$$\left.\varphi\right|_{K}=\left.\varphi^{\prime}\right|_{K}$$
and so $\varphi=\varphi^{\prime}$ on $Y$ after unique extensions over $G_{p}$ since both lie in $\operatorname{PSH}(Y, \chi)$. The above argument implies that as $s, \delta, \epsilon \rightarrow 0$, the solution $\psi_{p, s, \delta, \epsilon}$ converges to the unique limit $\varphi$. For different $p^{\prime} \in X \backslash \operatorname{LCS}(X)$, we can let $\epsilon \rightarrow 0$ for equation (3.5) with $\epsilon=0$ because Lemma 3.5 still holds when $\epsilon=0$. \(\square\)

The solution constructed in Lemma 3.6 coincides with the Kähler-Einstein current in [5], however, the key difference is that we obtain local boundedness for $\varphi$ near the log terminal singular locus of $X$. We will also prove a uniqueness result, which is different from the uniqueness theorem in [5] and will be crucial in Section 4.

Lemma 3.7. There exists a unique solution $\varphi \in L_{\text {loc }}^{\infty}(X \backslash \operatorname{LCS}(X)) \cap C^{\infty}\left(\mathcal{R}_{X}\right)$ satisfying
\begin{itemize}
\item[(1)] $(\chi+\sqrt{-1} \partial \bar{\partial} \varphi)^{n}=e^{\varphi} \Omega$ on $\mathcal{R}_{X}$,
\item[(2)] there exists $p \in X \backslash \operatorname{LCS}(X)$ such that for any $\epsilon>0$, there exist $C>0$ and $C_{p, \epsilon}>0$ with the following estimate
$$\epsilon \log \left|\sigma_{G_{p}}\right|_{h_{\Omega}}^{2}-C_{p, \epsilon} \leq \varphi \leq C,$$
where $G_{p}$ is an effective divisor as defined in Lemma 3.1.
\end{itemize}
In particular, $\varphi \in P S H(X, \chi)$ satisfies all the conditions in Lemma 3.6.

Proof. We first prove the uniqueness. Let $\varphi$ be the Kähler-Einstein potential constructed in Lemma 3.6 as the limit of $\psi_{p, s, \delta, \epsilon}(s, \delta, \epsilon \rightarrow 0)$ for a given $p \in X \backslash \operatorname{LCS}(X)$. Suppose there exists another $\varphi^{\prime}$ satisfying the conditions in the lemma and for any $\epsilon>0$, there exist $C_{1}>0$ and $C_{2}=C_{2}(\epsilon)>0$ such that
$$\epsilon \log \left|G_{p^{\prime}}\right|_{h_{\Omega}}^{2}-C_{2} \leq \varphi^{\prime} \leq C_{1},$$
for some $p^{\prime} \in X \backslash \operatorname{LCS}(X)$. We would like to show that $\varphi^{\prime}=\varphi$.
We let
$$G_{p, p^{\prime}}=\frac{1}{2} G_{p}+G_{p^{\prime}},$$
Then obviously there exist $C_{3}>0$ and $C_{4}=C_{4}(\epsilon)>0$ such that
$$\epsilon \log \left|G_{p, p^{\prime}}\right|_{h_{\Omega}}^{2}-C_{4} \leq \varphi \leq C_{3}, \epsilon \log \left|G_{p, p^{\prime}}\right|_{h_{\Omega}}^{2}-C_{4} \leq \varphi^{\prime} \leq C_{3} .$$

We consider the quantity
$$\phi=\psi_{p, s,-\delta, \epsilon}-\varphi^{\prime}+\delta^{2} \log \left|G_{p, p^{\prime}}\right|_{h_{\Omega}}^{2}+\delta^{3} \log \left|\sigma_{D}\right|_{h_{D}}^{2},$$
where $\sigma_{D}$ and $h_{D}$ are defined in (3.9) and (3.10). Then $\phi$ satisfies the following equation on the log resolution $Y$,
$$\frac{\left(\chi+\sqrt{-1} \partial \bar{\partial} \varphi^{\prime}+s \theta-\delta(1-\delta) \chi+\delta^{3} \operatorname{Ric}\left(h_{D}\right)+\sqrt{-1} \partial \bar{\partial} \phi\right)^{n}}{\left(\chi+\sqrt{-1} \partial \bar{\partial} \varphi^{\prime}\right)^{n}}=e^{\phi} \frac{\left|G_{p^{\prime}}\right|_{h_{\Omega}}^{2 \epsilon}+s}{\left|G_{p, p^{\prime}}^{2}\right|_{h_{\Omega}}^{2}\left|\sigma_{D}\right|_{h_{D}}^{2 \delta^{3}}} .$$
We pick $s \ll \delta \ll 1, \epsilon \ll \delta^{2}$ and apply the maximum principle to $\phi$. There exists $C>0$ such that for all $s \ll \delta \ll 1, \epsilon \ll \delta^{2}$,
$$\sup _{X} \phi \leq C .$$
Let $s, \delta, \epsilon \rightarrow 0$. We have
$$\varphi \leq \varphi^{\prime} .$$
Similarly, we can prove $\varphi \geq \varphi^{\prime}$ by applying the maximum principle to
$$\phi^{\prime}=\psi_{p^{\prime}, s, \delta, \epsilon}-\varphi^{\prime}-\delta \log \left|\sigma_{G_{p}}\right|_{h_{\Omega}}^{2} .$$
Therefore $\varphi=\varphi^{\prime}$ on $X \backslash G_{p, p^{\prime}}$ and $\varphi^{\prime}$ extends uniquely in $P S H(X, \chi)$ since $\varphi \in P S H(X, \chi)$.
For the existence part, we only need to verify that $\varphi \in L_{l o c}^{\infty}(X \backslash \operatorname{LCS}(X))$. By the uniqueness result we proved above, $\psi_{p, s, \delta, \epsilon}$ converges to the same $\varphi$ and such $\varphi$ satisfies the estimate (2) in Lemma 3.6 for all $p \in X \circ$. Then (2) in the lemma is proved. \(\square\)

Lemma 3.7 completes the proof of Theorem 1.1. We also remark that the uniqueness result of Lemma 3.7 does not require $\varphi \in P S H(X, \chi)$. We can also generalize Lemma 3.7 by adding a weight on the righthand side equation.

Lemma 3.8. For any open set $U \subset \subset X \backslash \operatorname{LCS}(X)$ and fixed $\alpha>1, K_{1}, K_{2}>0$, if $f$ is a real valued function on $X$ satisfying
$$\left\|e^{f}\right\|_{L^{\infty}(X \backslash U)} \leq K_{1}, \int_{U} e^{\alpha f} \Omega \leq K_{2},$$
then there exists a unique solution $\varphi$ solving
$$(\chi+\sqrt{-1} \partial \bar{\partial} \varphi)^{n}=e^{\varphi+f} \Omega$$
satisfying
\begin{itemize}
\item[(1)] $\|\varphi\|_{L^{\infty}(U)} \leq C_{1}=C_{1}\left(X, U, \Omega, \alpha, K_{1}, K_{2}\right)$.
\item[(2)] For any $p \in X \backslash \operatorname{LCS}(X)$ and $\epsilon>0$, there exist $C_{2}=C_{2}\left(X, U, \Omega, \alpha, K_{1}, K_{2}\right)>0$ and $C_{3}=C_{3}\left(X, U, \Omega, \alpha, K_{1}, K_{2}, \epsilon, p\right)>0$ such that
$$-C_{3}+\epsilon \log \left|G_{p}\right|_{h_{\Omega}}^{2} \leq \varphi \leq C_{2} .$$
\end{itemize}
In particular, if the pullback of $f$ on the log resolution $Y$ of $X$ is smooth, $\varphi \in C^{\infty}\left(\mathcal{R}_{X}\right)$.
The proof of Lemma 3.8 is almost identical to the proof of Lemma 3.6 and Lemma 3.7. It suffices to lift the equation onto the nonsingular model $Y$ of $X$ and approximate $f$ by smooth functions with the same bounds for $f$. Lemma 3.8 is a key ingredient to derive distance estimates in Section 6.

\section*{4. Analytic estimates for stable families of smooth canonical models}

In this section, we will derive uniform estimates for Kähler-Einstein metrics in a stable degeneration of smooth canonical models.

We will use the notations in Section 2. Let $\pi: \mathcal{X} \rightarrow B$ be a stable degeneration of smooth canonical models over a disc $B \subset \mathbb{C}$. Suppose $\mathcal{X}_{t}=\pi^{-1}(t)$ is a smooth canonical model of complex dimension $n$ for $t \in B^{*}$ and the central fibre $\mathcal{X}_{0}$ is a semi-log canonical model, where $t$ is the Euclidean holomorphic coordinate on $B$. After embedding $\mathcal{X}$ into $\mathbb{C P}^{N}$ by pluricanonical sections $\eta_{0}, \ldots, \eta_{N}$ in $\left|m K_{\mathcal{X} / B}\right|$ for some sufficiently large $m \in \mathbb{Z}^{+}$, we let $\chi \in-c_{1}\left(K_{\mathcal{X} / B}\right)$ be a smooth Kähler form on $\mathcal{X}$ induced from the projecting embedding, i.e.,
$$\chi=\frac{1}{m} \sqrt{-1} \partial \bar{\partial} \log \left(\sum_{j=0}^{N}\left|\eta_{j}\right|^{2}\right) .$$
Then $\chi_{t}=\left.\chi\right|_{\mathcal{X}_{t}} \in-c_{1}\left(\mathcal{X}_{t}\right)$ is a smooth Kähler form on $\mathcal{X}_{t}$ for $t \in B^{*} . \chi_{0}=\left.\chi\right|_{\mathcal{X}_{0}}$ is a Kähler current on $\mathcal{X}_{0}$ with bounded local potential and it is smooth on $\mathcal{R}_{\mathcal{X}_{0}}$, the nonsingular part of $\mathcal{X}_{0}$. We can define a real valued $(n, n)$-form measure $\Omega$ on $\mathcal{X}$ by
$$\Omega=\left(\sum_{j=0}^{N} \eta_{j} \wedge \bar{\eta}_{j}\right)^{1 / m} .$$

The restriction $\Omega_{t}=\left.\Omega\right|_{\mathcal{X}_{t}}$ on each general fibre is a smooth non-degenerate volume form on $\mathcal{X}_{t}$ for all $t \in B^{*} . \Omega_{0}=\left.\Omega\right|_{\mathcal{X}_{0}}$ is an adapted volume measure on $\mathcal{X}_{0}$. In particular,
$$\sqrt{-1} \partial \bar{\partial} \log \Omega_{t}=\chi_{t} .$$
We now consider the following family of complex Monge-Ampère equations on $\mathcal{X}_{t}$ for each $t \in B^{*}$
$$\left(\chi_{t}+\sqrt{-1} \partial \bar{\partial} \varphi_{t}\right)^{n}=e^{\varphi_{t}} \Omega_{t} .$$
Equation (4.13) admits a unique smooth solution $\varphi_{t}$ for all $t \in B^{*}$ and $\omega_{t}=\chi_{t}+\sqrt{-1} \partial \bar{\partial} \varphi_{t}$ is the unique smooth Kähler-Einstein metric on $\mathcal{X}_{t}$. We let $g_{t}$ be the Kähler-Einstein metric associated with $\omega_{t}$.

We will first compare $\chi^{n}$ and $\Omega$ on each $\mathcal{X}_{t}$.

Lemma 4.1. There exists $C>0$ such that
$$\sup _{\mathcal{X}} \frac{d t \wedge d \bar{t} \wedge \chi^{n}}{d t \wedge d \bar{t} \wedge \Omega} \leq C .$$
Proof. We use a trick similarly in [20]. By the choice of $\left\{\eta_{j}\right\}_{j=0}^{N}$,
$$\sqrt{-1} d t \wedge d \bar{t} \wedge \Omega$$
is an adapted volume measure on $\mathcal{X}$. For any point $p \in \mathcal{X}$, we can embed an open neighborhood $U$ of $p$ in $\mathcal{X}$ into $\mathbb{C}^{N}$ by $i: U \rightarrow \mathbb{C}^{N}$ (for example, we can localize the embedding by $\left[\eta_{0}, \ldots, \eta_{N}\right]$ ). Then $\left.\chi\right|_{U}$ extends to a smooth Kähler metric on $\mathbb{C}^{N}$ and is quasi-equivalent to the Euclidean metric $\hat{\omega}=\sqrt{-1} \sum_{i=1}^{N} d z_{i} \wedge d \bar{z}_{i}$. Hence there exists $C_{1}>0$ such that near $i(p)$
$$\left(C_{1}\right)^{-1} \chi^{n+1} \leq \sum_{1 \leq i_{1}<i_{2}<\ldots<i_{n+1} \leq N}(\sqrt{-1})^{n+1} \prod_{k=1}^{n+1} d z_{i_{k}} \wedge d \bar{z}_{i_{k}} \leq C_{1} \chi^{n+1} .$$
Since $\sqrt{-1} d t \wedge d \bar{t} \wedge \Omega$ is an adapted volume measure on $\mathcal{X}$, for any $1 \leq i_{1} \leq i_{2} \leq \ldots \leq$ $i_{n+1} \leq N$, there exist smooth nonnegative functions $f_{i_{1}, \ldots, i_{n+1}}$ in $U$ such that
$$i^{*}\left((\sqrt{-1})^{n+1} \prod_{k=1}^{n+1} d z_{i_{k}} \wedge d \bar{z}_{i_{k}}\right)=\sqrt{-1} f_{i_{1}, \ldots, i_{n+1}} d t \wedge d \bar{t} \wedge \Omega$$
This implies that there exists $C_{2}>0$ such that
$$\chi^{n+1} \leq C_{2} \sqrt{-1} d t \wedge d \bar{t} \wedge \Omega .$$
The lemma is proved since $\sqrt{-1} d t \wedge d \bar{t}$ is bounded above by a multiple of $\chi$. \(\square\)

We immediately can achieve the following uniform upper bound for the potential $\varphi_{t}$.
Corollary 4.1. There exists $C>0$ such that for all $t \in B^{*}$,
$$\sup _{\mathcal{X}_{t}} \varphi_{t} \leq C .$$
Proof. We apply the maximum principle to equation (4.13) on $\mathcal{X}_{t}$ at the maximal point of $\varphi_{t}$ and obtain
$$\sup _{\mathcal{X}_{t}} \varphi_{t} \leq \sup _{\mathcal{X}_{t}} \log \left(\frac{\chi_{t}^{n}}{\Omega_{t}}\right)=\sup _{\mathcal{X}_{t}} \log \left(\frac{\sqrt{-1} d t \wedge d \bar{t} \wedge \chi_{t}^{n}}{\sqrt{-1} d t \wedge d \bar{t} \wedge \Omega_{t}}\right) \leq \sup _{\mathcal{X}} \log \left(\frac{\sqrt{-1} d t \wedge d \bar{t} \wedge \chi^{n}}{\sqrt{-1} d t \wedge d \bar{t} \wedge \Omega}\right) .$$
The corollary easily follows from Lemma 4.1. \(\square\)

The main goal of this section is to achieve a local $L^{\infty}$-estimate for $\varphi_{t}$. We will apply the semi-stable reduction for $\pi: \mathcal{X} \rightarrow B$ with following diagram
![](https://cdn.mathpix.com/cropped/214fb33d-20fb-4355-9113-beb4c2d7f8f9-19.jpg?height=311&width=546&top_left_y=391&top_left_x=796)
such that $\mathcal{X}^{\prime}$ is smooth and $\mathcal{X}_{0}^{\prime}=\left(\pi^{\prime}\right)^{-1}(0)$ is a reduced divisor of smooth components with normal crossings. Let $t^{\prime}$ be the holomorphic coordinate on $B^{\prime}$ such that $t=\left(t^{\prime}\right)^{d}$.

The central fibre $\mathcal{X}_{0}^{\prime}=\widetilde{\mathcal{X}_{0}} \cup \mathcal{E}$, where $\widetilde{\mathcal{X}_{0}}$ is the strict transform of $\mathcal{X}_{0}$ and $\mathcal{E}$ is the exceptional divisor.

For simplicity, we will use $\chi$ for $\left(\Psi^{\prime}\right)^{*} \chi$ on $\mathcal{X}^{\prime}$, where
$$\Psi^{\prime}=f^{\prime} \circ \Psi .$$
By Kodaira's lemma, there exist an effective $\mathbb{Q}$-Cartier divisor $\mathcal{D}$ whose support coincides with the support of $\mathcal{E}$ and a smooth hermitian metric $h_{\mathcal{D}}$ equipped on the line bundle associated to $\mathcal{D}$ such that $\chi_{\epsilon}=\chi-\epsilon \operatorname{Ric}\left(h_{\mathcal{D}}\right)$ is a Kähler form on $\mathcal{X}^{\prime}$ for all sufficiently small $\epsilon>0$. Let $\sigma_{\mathcal{D}}$ be the defining section of $\mathcal{D}$.

By discussion in Section 2, we have
$$K_{\mathcal{X}^{\prime}}=\left(\Psi^{\prime}\right)^{*} K_{\mathcal{X}}+(d-1) \widetilde{\mathcal{X}_{0}}+\sum_{i=1}^{K} c_{i} D_{i},$$
with $c_{i} \geq 0$, where $D_{i}$ are components of the exceptional divisor $\mathcal{D}$. Also Let $\widetilde{\mathcal{X}_{0}}=$ $\cup_{\alpha=1}^{\mathcal{A}} \widetilde{X_{\alpha}}$, where $\widetilde{X_{\alpha}}$ is the irreducible component of $\mathcal{X}_{0}^{\prime}$.

We pick arbitrary $\alpha$ and let
$$\widetilde{X}=\widetilde{X}_{\alpha}, \widetilde{\mathcal{X}}_{0}=\widetilde{X} \cup \widetilde{X}^{\prime}$$
and work on $\widetilde{X}$ instead of $\widetilde{\mathcal{X}_{0}}$ unless $\widetilde{\mathcal{X}_{0}}$ is already irreducible. In particular, there exists a component $X$ in $\mathcal{X}_{0}$ such that
$$X=\Phi^{\prime}(\widetilde{X}) .$$
We can write
$$\widetilde{\mathcal{X}_{0}^{\prime}}=\widetilde{X} \cup \widetilde{X}^{\prime} \cup_{i=1}^{I} E_{i} \cup_{j=1}^{J} F_{j}$$
from the bundle formula
$$K_{\widetilde{X}}=\left(\Psi^{\prime}\right)^{*} K_{X}+\left.\sum a_{i} E_{i}\right|_{\widetilde{X}}-\left.\sum_{j} b_{j} F_{j}\right|_{\widetilde{X}},$$
where $a_{i} \geq 0,0<b_{j} \leq 1, E_{i}$ and $F_{j}$ are smooth irreducible components in $\left(\mathcal{D} \cup \widetilde{X}^{\prime}\right)$. Let $\sigma_{E_{i}}, \sigma_{F_{j}}$ and $\sigma_{\widetilde{X}^{\prime}}$ be the defining sections for $E_{i}, F_{j}$ and $\widetilde{X}^{\prime}$ respectively and we equip the corresponding line bundles with smooth hermitian metrics $h_{E_{i}}, h_{F_{j}}$ and $h_{\widetilde{X}^{\prime}}$.

We will now estimate the lower bound of $\varphi_{t}$. Equation (4.13) can be lifted to $\mathcal{X}_{t^{\prime}}^{\prime}=$ $\left(\Psi^{\prime}\right)^{-1}\left(t^{\prime}\right)$ for $t^{\prime} \in\left(B^{\prime}\right)^{*}$, given by
$$\left(\chi_{t^{\prime}}+\sqrt{-1} \partial \bar{\partial} \varphi_{t^{\prime}}\right)^{n}=e^{\varphi_{t^{\prime}}} \Omega_{t^{\prime}},$$
where $\chi_{t^{\prime}}, \Omega_{t^{\prime}}$ and $\varphi_{t^{\prime}}$ are pullback of $\chi_{t}, \Omega_{t}$ and $\varphi_{t}$ by $\Psi^{\prime}$.
Lemma 4.2. For any $\epsilon>0$, there exists $C_{\epsilon}>0$ such that for all $t^{\prime} \in\left(B^{\prime}\right)^{*}$, we have
$$\varphi_{t^{\prime}} \geq \epsilon \log \left(\prod_{i=1, j=1}^{I, J}\left|\sigma_{E_{i}}\right|_{h_{E_{i}}}^{2}\left|\sigma_{F_{j}}\right|_{h_{F_{j}}}^{2}\left|\sigma_{\widetilde{X}^{\prime}}\right|_{h_{\widetilde{X}^{\prime}}}^{2}\right)-C_{\epsilon}$$
on $\mathcal{X}_{t}$.
Proof. We define the following smooth closed (1, 1)-form
$$\begin{aligned}
\chi_{t^{\prime}, \epsilon}= & \chi_{t^{\prime}}-\epsilon_{1} \sqrt{-1} \partial \bar{\partial} \log \operatorname{Ric}\left(h_{\mathcal{D}}\right)-\epsilon_{2} \sqrt{-1} \partial \bar{\partial} \sum_{k} \log \left(\left|\sigma_{\widetilde{X}^{\prime}}\right|_{h_{\widetilde{X}^{\prime}}}^{2}\right) \\
& +\epsilon_{3} \sqrt{-1} \partial \bar{\partial}\left(\sum_{i=1}^{I}\left|\sigma_{E_{i}}\right|_{h_{E_{i}}}^{2 \epsilon_{4}}+\sum_{j=1}^{J}\left|\sigma_{F_{j}}\right|_{h_{F_{j}}}^{2 \epsilon_{\epsilon_{4}}}+\left|\sigma_{\widetilde{X}}\right|_{h_{\widetilde{X}}}^{2 \epsilon_{4}}\right),
\end{aligned}$$
where $\epsilon=\left(\epsilon_{1}, \epsilon_{2}, \epsilon_{3}, \epsilon_{4}\right)$.
For any sufficiently small $\epsilon_{1}>0$ and $\epsilon_{4}>0$, we can choose $0<\epsilon_{3} \ll \epsilon_{2} \ll \epsilon_{1}$ such that $\chi_{t^{\prime}, \epsilon}$ is a Kähler metric with conical singularities along smooth divisors $E_{i}, F_{j}$ and $\widetilde{X}^{\prime}$ with normal crossings of the same cone angle $2 \pi \epsilon_{4}$.

Let
$$\varphi_{t^{\prime}, \epsilon}=\varphi_{t^{\prime}}-f_{\epsilon},$$
where
$$f_{\epsilon}=\epsilon_{1} \log \left|\sigma_{\mathcal{D}}\right|_{h_{\mathcal{D}}}^{2}+\epsilon_{2} \log \left|\sigma_{\widetilde{X}^{\prime}}\right|_{h_{\widetilde{X}^{\prime}}}^{2}+\epsilon_{3}\left(\sum_{i=1}^{I}\left|\sigma_{E_{i}}\right|_{h_{E_{i}}}^{2 \epsilon_{4}}+\sum_{j=1}^{J}\left|\sigma_{F_{j}}\right|_{h_{F_{j}}}^{2 \epsilon_{4}}+\left|\sigma_{\widetilde{X}^{\prime}}\right|_{h_{\widetilde{X}^{\prime}}}^{2 \epsilon_{4}}\right) .$$
Then we have on $\mathcal{X}_{t^{\prime}}^{\prime}$ for $t^{\prime} \in\left(B^{\prime}\right)^{*}$,
$$\left(\chi_{t^{\prime}, \epsilon}+\sqrt{-1} \partial \bar{\partial} \varphi_{t^{\prime}, \epsilon}\right)^{n}=e^{\varphi_{t^{\prime}, \epsilon}+f_{\epsilon}} \Omega_{t^{\prime}} .$$
We can now apply the maximum principle to $\varphi_{t^{\prime}, \epsilon}$ on each $\mathcal{X}_{t^{\prime}}^{\prime}$. Suppose $\varphi_{t^{\prime}, \epsilon}$ achieves its minimum at $p_{t^{\prime}, \epsilon}$ in $\mathcal{X}_{t^{\prime}}^{\prime}$ for any given $t^{\prime} \in\left(B^{\prime}\right)^{*}$. Then
$$\begin{aligned}
\inf _{\mathcal{X}_{t^{\prime}}^{\prime}} \varphi_{t^{\prime}, \epsilon} & \geq \inf _{\mathcal{X}_{t^{\prime}}^{\prime}} \log \left(\frac{\left(\chi_{t^{\prime}, \epsilon}\right)^{n}}{e^{f_{\epsilon} \Omega_{t^{\prime}}}}\right) \\
& =\inf _{\mathcal{X}_{t^{\prime}}^{\prime}} \log \left(\frac{d t^{\prime} \wedge d \overline{t^{\prime}} \wedge\left(\chi_{t^{\prime}, \epsilon}\right)^{n}}{e^{f_{\epsilon}} d t^{\prime} \wedge d \overline{t^{\prime}} \wedge \Omega_{t^{\prime}}}\right) \\
& \geq \inf _{\mathcal{X}^{\prime}} \log \left(\frac{d t^{\prime} \wedge d \overline{t^{\prime}} \wedge\left(\chi_{t^{\prime}, \epsilon}\right)^{n}}{e^{f_{\epsilon}} d t^{\prime} \wedge d \overline{t^{\prime}} \wedge \Omega_{t^{\prime}}}\right)
\end{aligned}$$
By the normal crossings of the smooth components in $\mathcal{X}_{0}^{\prime}$ from the semi-stable reduction, we can cover $\mathcal{X}_{0}^{\prime}$ by finitely many small coordinate charts $\left\{U_{\beta}\right\}_{\beta=1}^{\mathcal{B}}$ in $\mathcal{X}^{\prime}$. We can assume in $U_{\beta}$,
$$t^{\prime}=x z_{1} z_{2} \ldots z_{m}, \text { for some } m \leq n,$$
where $x, z_{1}, \ldots, z_{n}$ are local holomorphic coordinates.
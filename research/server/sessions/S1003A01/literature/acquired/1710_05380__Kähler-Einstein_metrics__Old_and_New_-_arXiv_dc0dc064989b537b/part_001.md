---
retention_scope: session
part: 1
total_parts: 3
---

[Part 1/3 of: [1710.05380] Kähler-Einstein metrics: Old and New - arXiv]

---
source_file: 1710_05380.pdf
converter: mathpix
format: mmd
---

\title{
KÄHLER-EINSTEIN METRICS: OLD AND NEW
}

\author{
DANIELE ANGELLA AND CRISTIANO SPOTTI
}

\begin{abstract}
We present classical and recent results on Kähler-Einstein metrics on compact complex manifolds, focusing on existence, obstructions and relations to algebraic geometric notions of stability (K-stability). These are the notes for the SMI course "Kähler-Einstein metrics" given by C.S. in Cortona (Italy), May 2017. The material is not intended to be original.
\end{abstract}

\section*{Introduction}

Let us begin by presenting our main actors. The most "geometric" way to introduce them is as follow. Connected $2 n$-dimensional Riemannian manifolds ( $M^{2 n}, g$ ) are called Kähler-Einstein (KE) if, as the name suggests, they are:

Kähler: the holonomy $\operatorname{Hol}\left(M^{2 n}, g\right)$ is contained in the unitary group $\mathrm{U}(n)$;
Einstein: the Ricci curvature satisfies $\operatorname{Ric}(g)=\lambda g$ for $\lambda \in \mathbb{R}$.
In these lectures we are going to focus on compact KE manifolds. There are several possible motivations for the study such spaces:
\begin{itemize}
\item[(1)] For $n=1$, KE metrics are precisely metrics with constant Gauss curvature on compact oriented surfaces. By the classical Uniformization Theorem, a jewel of XIX century mathematics due to works of Riemann, Poincaré and Koebe, three cases occur:
\begin{itemize}
\item[-] if $\lambda>0$, then the manifold is the round sphere $\left(\mathbb{S}^{2}, g_{\text {round }}\right)$;
\item[-] if $\lambda=0$, then the manifold is a flat torus $\left(\mathbb{T}^{2}, g_{\text {flat }}\right)$;
\item[-] if $\lambda<0$, then the manifold is a compact hyperbolic surface $C_{g} \simeq \mathbb{H}^{2} / \Gamma$ where $\Gamma \subseteq$ $\operatorname{PSL}(2 ; \mathbb{R})$ is a discrete subgroup that acts freely on $\mathbb{H}^{2}$.
\end{itemize}
\end{itemize}

It is important to remark that, despite the local isometry class of such metrics depends only on the value of the constant Gauss curvature, there are, up to scalings, a real 2-dimensional continuous family of distinct (i.e., non globally isometric) flat tori, and a $6 g-6$ family (the famous Riemann's moduli parameters) of distinct hyperbolic metrics on a surface of genus $g \geq 2$. KE manifolds are the most natural higher dimensional generalizations of such important geometric spaces.
\begin{itemize}
\item[(2)] In a curvature hierarchy, Einstein metrics lie between the better understood cases of full constant curvature and constant scalar curvature (such metrics exist in any conformal class, by the solution of the Yamabe problem). In real dimension bigger than three, Einstein metrics no longer have a unique local isometry model but they still form finite dimensional moduli spaces. They are also good candidates for being "canonical" metrics on a space
\end{itemize}

\footnotetext{
Date: December 14, 2017.
2010 Mathematics Subject Classification. 53C55.
Key words and phrases. Kähler-Einstein, Fano, K-stability, Yau-Tian-Donaldson conjecture, moduli of KählerEinstein.
D.A. is supported by the Project SIR2014 AnHyC "Analytic aspects in complex and hypercomplex geometry" (code RBSI14DYEB), by Projecti PRIN2015 "Varietà reali e complesse: geometria, topologia e analisi armonica", and by GNSAGA of INdAM.
C.S. is supported by AUFF Starting Grant 24285.
}
\begin{itemize}
\item[] and they are critical points of the natural Einstein-Hilbert functional $g \mapsto \int \mathrm{Sc}_{g} d V_{g}$, over $\int d V_{g}=1$. Thus KE metrics provide an important example of such quite mysterious class of Einstein spaces to study.
\item[(3)] The Kähler condition corresponds to the holonomy group $\mathrm{U}(n)$ in the Berger's classification of reduced holonomy group of irreducible non-locally symmetric spaces. The other are the "generic" $\operatorname{SO}(2 n)$, the Calabi-Yau $\operatorname{SU}(n)$, the hyper-Kähler $\operatorname{Sp}(n)$, the quaternionic-Kähler $\operatorname{Sp}(1) \operatorname{Sp}(n)$ and the special groups $\mathrm{G}_{2}$ and Spin(7). Except than $\operatorname{SO}(2 n)$ and $\mathrm{U}(n)$, the other cases are Einstein. Thus it is natural to look what happens when we combine the relatively soft $\mathrm{U}(n)$ holonomy condition with the Einstein property: as we will see, such holonomy condition actually provides a great simplification in studying the Einstein equation.
\end{itemize}

The Kähler condition implies that there is a natural structure of complex manifold $X^{n}\left(\cong M^{2 n}\right)$ which is compatible with the metric. The Kähler-Einstein property implies even more:
\begin{itemize}
\item[-] if $\lambda>0$, then $c_{1}(X)>0$; that is $X^{n}$ is Fano;
\item[-] if $\lambda=0$, then $c_{1}(X)=0$; that is $X^{n}$ is Calabi-Yau;
\item[-] if $\lambda<0$, then $c_{1}(X)<0$; that is $X^{n}$ is with ample canonical bundle, in particular, it is of general type.
\end{itemize}

These mutually exclusive conditions are very strong and most of the complex manifolds are not of the above types (anyway, such special manifolds are, in a certain sense, supposed to be fundamental "building blocks" for complex (Kähler) manifolds).

In analogy with the uniformization of surfaces/complex curves mentioned above (note that in such case $c_{1}=2-2 g$ ), it is very natural to ask if all compact complex manifolds whose first Chern class "has a sign" can be equipped with KE metrics. This and a related question was posed by Calabi in the '50s (the famous Calabi's conjectures, [Cal54, Cal57]). However, it was immediately realized that some issues occur: Matsushima [Mat57] found an obstruction for the case $\lambda>0$ in terms of reductivity of the Lie algebra of holomorphic vector fields. In particular, very simple Fano manifolds, such as the blow-up in a point of the projective plane, cannot admit KE metric.

However, for non-positive first Chern class, the situation turned out to much nicer. Actually, the best it could be:

Theorem 0.1 (Aubin [Aub76, Aub78], Yau [Yau77, Yau78]). Let $X^{n}$ be a compact complex manifold. If $c_{1}(X)<0$, then there exists up to scaling a unique Kähler-Einstein metric on $X^{n}$.

Theorem 0.2 (Yau [Yau77, Yau78]). Let $X^{n}$ be a compact complex Kähler manifold. If $c_{1}(X)=0$, then there exists a unique Kähler-Einstein metric in any Kähler class on $X^{n}$.

In the Fano case, the situation remained unclear. Starting from the '80s there have been several discoveries of new obstructions: Futaki's invariant [Fut83], Tian's examples of a smooth Fano 3fold with no non-trivial holomorphic vector fields with not KE metric [Tia97] based on obstructions coming from algebro-geometric notions of stability conditions (see also, e.g. [Don05]). Furthermore, some existence criteria and non-trivial examples were found in the last 30 years: $\alpha$-invariant existence criterion [Tian87], study of highly symmetric cases (e.g. toric varieties [WZ04]), and a complete understanding in dimension two [Tia90a].

Motivated by the above important results and in analogy with Hitchin-Kobayashi correspondence for holomorphic vector bundles [Don87, UY86, LY87, LT95], it was conjectured, e.g. [Tia97, Don02b]), that the relations of the existence problem with some (to be understood) algebrogeometric notion of stability is indeed the crucial aspect to completely characterize, in purely algebro-geometric terms, the existence of KE metrics on Fano manifolds (and, even more generally, for constant scalar curvature Kähler metrics). Such conjecture is known as Yau-Tian-Donaldson (YTD) conjecture. By refining the Futaki's invariant, the notion of $K$-stability has been introduced
by Tian [Tia94, Tia97], and refined by Donaldson [Don02b]. This notion turned out to be the correct one:

Theorem 0.3 (Yau-Tian-Donaldson conjecture for the Fano case; "if" Chen-Donaldson-Sun [CDS14, CDS15], "only if" Berman [Ber16]). A Fano manifold $X^{n}$ admits a Kähler-Einstein metric if and only if $X$ is $K$-polystable.

The "only if" direction has been studied by Tian [Tia97], Donaldson [Don05], Mabuchi [Mab08], Stoppa [Sto09], and in full generality by Berman [Ber16]. The "if" direction is the celebrated breakthrough result obtained in 2012 by Chen-Donaldson-Sun [CDS14, CDS15].

In these six lectures we are going to describe some aspects of the above outlined "KE story". Due to the vastness of the subject, there is going to be plenty of omission of fundamental results. We apologize in advance. The first lectures are supposed to be more elementary and more detailed. In approaching the final lecture the "hand waving" is going to become more and more dominant. In any case, we hope that we at least succeed in describing some of the ideas behind the proofs of important results in the field, and that such "road map" can be of some use for the ones that would like to proceed further in the study by reading the original papers.

This is a more detailed description of the actual content of the lectures.
\begin{itemize}
\item[-] Lecture 1. Review of basic Kähler geometry with emphasis on curvature formulas.
\item[-] Lecture 2. Calabi's conjectures: preliminaries, their proofs and some consequences.
\item[-] Lecture 3. Obstructions to the existence of KE metrics on Fanos: Matsushima's theorem and Futaki's invariant. Mabuchi's energy and geodesics: the "fake" proof of uniqueness.
\item[-] Lecture 4. First results on existence of KE metric on Fanos: energy functionals, properness and the $\alpha$-invariant criterion.
\item[-] Lecture 5. Towards K-stability: review of moment maps and GIT, Donaldson-Fujiki's infinite dimensional picture, definition of K-stability.
\item[-] Lecture 6. YTD conjecture for Fanos: descriptions of Berman and Chen-Donaldson-Sun proofs. Compact Moduli spaces of KE Fanos.
\end{itemize}

Acknowledgments. This note resumes the contents of the SMI school "Kaehler-Einstein metrics" given by C.S. in Cortona on April 30th-May 06th, 2017, see https://gecogedi.dimai.unifi.it/event/404/. The event has been organized by the two authors together with Simone Calamai, Graziano Gentili and Nicoletta Tardini, with the support by SMI Scuola Matematica Interuniversitaria, Dipartimento di Matematica e Informatica "Ulisse Dini" of Università di Firenze, SIR2014 AnHyC "Analytic aspects in complex and hypercomplex geometry" (code RBSI14DYEB), GNSAGA of INdAM. The authors warmly thank all the participants for the wonderful environment they contributed to, and the secretaries for their fundamental assistance during the organization. In particular, thanks to Gao Chen, Paul Gauduchon, Long Li, Alexandra Otiman, Chengjian Yao and Kai Zheng for accepting the invitation to give seminar lectures. Many thanks also to the anonymous Reviewer, whose suggestions improved the presentation of the paper.

\section*{1. Curvature formulas on Kähler manifolds}

In this preliminary section, we recall some basic facts concerning differential complex geometry and curvature of Kähler metrics; references are e.g. [Szé14, Tia00, Mor07, Dem12, Voi07, Gau15, Huy05, MK71, GH78, Kod86, Wel08, Bal06, KN2].
1.1. Basic complex geometry. Let $X^{n}$ be a complex manifold, i.e. a smooth manifold with an atlas whose transition functions are holomorphic. Examples include $\mathbb{C P}^{n}$, hypersurfaces in $\mathbb{C P}^{n}$ namely zero-set of a homogeneous polynomial, tori $\mathbb{C}^{n} / \Gamma$ where $\Gamma$ is a discrete subgroup of maximal rank. We denote by $M^{2 n}$ the underlying smooth manifold, and we use local holomorphic
coordinates $\left(z_{j}=x_{j}+\sqrt{-1} y_{j}\right)_{j}$, so $\left(x_{j}, y_{j}\right)_{j}$ are local differential coordinates and $\left(\partial_{x_{j}}, \partial_{y_{j}}\right)_{j}$ denotes the corresponding local frame for the tangent bundle.

Multiplication by $\sqrt{-1}$ defines a tensor $J \in \operatorname{End}\left(T M^{2 n}\right)$ as $J \partial_{x_{j}}=\partial_{y_{j}}$ and $J \partial_{y_{j}}=-\partial_{x_{j}}$, which is globally defined and with the property that $J^{2}=-\mathrm{id}$. Moreover, if we define the Nijenhuis tensor of such an endomorphism $J$ as
$$N_{J}(Y, T):=\frac{1}{4}([J Y, J T]-J[J Y, T]-J[Y, J T]-[Y, T]),$$
for $Y, T \in T M^{2 n}$, then clearly we have $N_{J}=0$. Conversely, by the Newlander and Nirenberg theorem [NN57], if $M^{2 n}$ is a smooth manifold and $J \in \operatorname{End}\left(M^{2 n}\right)$ is such that $J^{2}=-\operatorname{id}$ (say that $J$ is an almost-complex structure), then $J$ is integrable (i.e. it is induced by a holomorphic atlas) if and only if $N_{J}=0$.

Consider the eigenspaces splitting
$$T M \otimes \mathbb{C}=T M^{(1,0)} \oplus T M^{(0,1)}=\left\langle\partial_{z_{1}}, \ldots, \partial_{z_{n}}\right\rangle \oplus\left\langle\partial_{\bar{z}_{1}}, \ldots, \partial_{\bar{z}_{n}}\right\rangle,$$
where
$$\partial_{z_{j}}=\frac{1}{2}\left(\partial_{x_{j}}-\sqrt{-1} \partial_{y_{j}}\right), \quad \partial_{\bar{z}_{j}}=\frac{1}{2}\left(\partial_{x_{j}}+\sqrt{-1} \partial_{y_{j}}\right) .$$
Then we can identify
$$(T M, J) \stackrel{\simeq}{\rightarrow}\left(T M^{(1,0)}, \sqrt{-1}\right)$$
by means of the maps
$$Y \mapsto Y^{(1,0)}:=\frac{1}{2}(Y-\sqrt{-1} J Y), \quad 2 \operatorname{Re} v=v+\bar{v} \leftarrow v .$$
A holomorphic vector field is a holomorphic section of $T M^{(1,0)}$; locally, it is given by $v \stackrel{\text { loc }}{=} \sum v_{j} \partial_{z_{j}}$ where $v_{j}$ are holomorphic function, i.e. smooth functions such that $\partial_{\bar{z}_{k}} v_{j}=0$ for any $k$. We see easily that a smooth vector field $v \in T M^{(1,0)}$ is holomorphic if and only if $\mathcal{L}_{\operatorname{Re} v} J=0$ (i.e. $\operatorname{Re} v$ is real holomorphic); see e.g. [Gau15, page 23].

Similarly, one can consider the splitting at the level of differential forms:
$$T M^{\vee} \otimes \mathbb{C}=\wedge^{1,0} M \oplus \wedge^{0,1} M=\left\langle d z_{1}, \ldots, d z_{n}\right\rangle \oplus\left\langle d \bar{z}_{1}, \ldots, d \bar{z}_{n}\right\rangle$$
where
$$d z_{j}=d x_{j}+\sqrt{-1} d y_{j}, \quad d \bar{z}_{j}=d x_{j}-\sqrt{-1} d y_{j} .$$
Then
$$\wedge^{j} T M^{\vee} \otimes \mathbb{C}=\bigoplus_{p+q=j} \wedge^{p, q} M,$$
that is, locally, a $(p, q)$-form can be expressed as $\eta \stackrel{\text { loc }}{=} \sum f_{I \bar{J}} d z_{i_{1}} \wedge \cdots \wedge d z_{i_{p}} \wedge d \bar{z}_{j_{1}} \wedge \cdots \wedge d \bar{z}_{j_{q}}$, where $f_{I \bar{J}}=f_{i_{1}, \ldots, i_{p}, \bar{j}_{1}, \ldots, \bar{j}_{q}}$ are smooth functions. We have $d f=\partial f+\bar{\partial} f$ on functions, and this extends to forms. By $d^{2}=0$, we get $\partial^{2}=\bar{\partial}^{2}=\partial \bar{\partial}+\bar{\partial} \partial=0$.

The Dolbeault cohomology is defined as
$$H_{\bar{\partial}}^{p, q}(X)=\frac{\operatorname{ker}\left(\bar{\partial}: \wedge^{p, q} X \rightarrow \wedge^{p, q+1} X\right)}{\operatorname{im}\left(\bar{\partial}: \wedge^{p, q-1} X \rightarrow \wedge^{p, q} X\right)} .$$
When $X$ is compact, $h^{p, q}:=\operatorname{dim}_{\mathbb{C}} H^{p, q}(X)<+\infty$ are called the Hodge numbers. Note that $h^{p, 0}$ is just the dimension of the space of holomorphic $p$-forms ( $e . g ., h^{1,0}=g$ for compact complex curves of genus $g$ ). More generally, for people who know a bit of sheaf theory, if we denote by $\mathcal{A}_{X}^{p, q}$ the sheaf of germs of smooth $(p, q)$-forms, and define the sheaf of germs of holomorphic $p$-forms as
$\Omega_{X}^{p}:=\operatorname{ker}\left(\bar{\partial}: \mathcal{A}_{X}^{p, 0} \rightarrow \mathcal{A}_{X}^{p, 1}\right)$, then it is a standard result that $H^{p, q}(X) \cong H^{q}\left(X, \Omega_{X}^{p}\right)$, where the last denotes sheaf cohomology [Dol53], see e.g. [Voi07].
1.2. Kähler manifolds. A Hermitian metric $h$ on $X^{n}$ is a smoothly varying family of Hermitian products on $T X=T M^{(1,0)}$. Namely, for any $p \in X$, it holds $h_{p}(v, v)>0$ for any $v \neq 0$ and $h_{p}(v, w)=\overline{h_{p}(w, v)}$; locally, $h \stackrel{\text { loc }}{=} \sqrt{-1} \sum h_{j \bar{k}} d z^{j} \otimes d \bar{z}^{k}$ where $\left(h_{j \bar{k}}\right)$ is a positive-definite Hermitian matrix of functions.

A Hermitian manifold is called Kähler if the associated (1,1)-form $\omega: \stackrel{\text { loc }}{=} \sqrt{-1} \sum h_{j \bar{k}} d z_{j} \wedge d \bar{z}_{k}$ is closed:
$$d \omega=0$$
that is, $\omega$ is symplectic. Equivalently if the following PDE is satisfied:
$$\frac{\partial h_{j \bar{k}}}{\partial z_{\ell}}=\frac{\partial h_{\ell \bar{k}}}{\partial z_{j}}, \quad \frac{\partial h_{j \bar{k}}}{\partial \bar{z}_{\ell}}=\frac{\partial h_{j \bar{\ell}}}{\partial \bar{z}_{k}} .$$
Examples include:
\begin{itemize}
\item[-] $\left(\mathbb{C}^{n}, \omega_{\text {flat }}\right)$ with $\omega_{\text {flat }}=\sum \frac{\sqrt{-1}}{2} d z_{j} \wedge d \bar{z}_{j}$ for $\left(z_{j}\right)$ standard coordinates; and $\mathbb{C}^{n} / \Gamma$ flat tori.
\item[-] $\left(\mathbb{C P}^{n}, \omega_{F S}\right)$ where the Fubini-Study metric is
$$\omega_{F S} \stackrel{\operatorname{loc}}{=} \sqrt{-1} \partial \bar{\partial} \log \left(1+\sum \frac{\left|Z_{j}\right|^{2}}{\left|Z_{0}\right|^{2}}\right)$$
away from $\left\{Z_{0}=0\right\}$, where $\left(Z_{j}\right)$ are homogeneous coordinates on $\mathbb{C P}^{n}$. For example, for $\mathbb{C P}^{1}$, we get the round metric $\omega=\sqrt{-1} \partial \bar{\partial} \log \left(1+|\xi|^{2}\right)=\frac{\sqrt{-1}}{\left(1+|\xi|^{2}\right)^{2}} d \xi \wedge d \bar{\xi}>0$. We remark here that, more generally, $\left(\mathbb{C P}^{n}, \omega_{F S}\right)$ has constant holomorphic sectional curvature, that is, the sectional curvature is constant on complex lines in $T X$. See later for definitions.
\item[-] $\left(\mathbb{B}, \omega_{\mathbb{B}}\right)$ where $\mathbb{B} \subset \mathbb{C}^{n}$ is the unit ball and $\omega_{\mathbb{B}}=\sqrt{-1} \partial \bar{\partial} \log \left(1-\sum\left|z_{j}\right|^{2}\right)$ for $\left(z_{j}\right)$ standard coordinates.
\item[-] Submanifolds of Kähler manifolds are naturally Kähler. In particular, algebraic manifolds (here meaning zeros of homogeneus polynomial in $\mathbb{C P}^{n}$ ) are Kähler. Note that submanifolds of $\mathbb{C P}^{n}$ with restricted $\omega_{F S}$ are almost never Kähler-Einstein for the induced metric.
\end{itemize}

We compare the real and the complex viewpoints. Starting from $\left(X^{n}, h\right)$ Hermitian, we can define a Riemannian metric as
$$g(Y, Z):=2 \operatorname{Re} h\left(Y^{(1,0)}, Z^{(1,0)}\right)$$
which is Hermitian in the sense that $J$ is an isometry: $g(J Y, J Z)=g(Y, Z)$. Conversely, we recover $h_{j \bar{k}}=\frac{1}{2} g^{\mathbb{C}}\left(\partial_{z_{j}}, \partial_{\bar{z}_{k}}\right)$. Moreover,
$$\omega=g\left(J_{-}, \_\right) .$$
In the following, we will confuse $h, \omega, g$ on a complex manifold $X^{n}$.
The Kähler condition $d \omega=0$ gives a Kähler class $[\omega] \in H^{2}(X ; \mathbb{R})$. Notice that, at $p$, we can always assume that $h_{j \bar{k}}(p)=\delta_{j k}$. From here, one can easily see that $d V_{g}=\frac{\omega^{n}}{n!}$. This implies that, if $\left(X^{n}, \omega\right)$ is compact Kähler, then the volume is cohomological: $\operatorname{Vol}_{\omega}=\operatorname{Vol}_{[\omega]}$, and the even Betti numbers are positive: $b_{2 k}>0$ for any $k \in\{0, \ldots, n\}$.

We give now another interpretation of the Kähler condition. Take $\left(M^{2 n}, J, g\right)$ where $g$ is a Riemannian metric and $J \in \operatorname{End}(T M)$ a compatible almost complex structure, i.e. a pointwise isometry such that $J^{2}=-\mathrm{id}$.

Proposition 1.1. Let $g$ be a Riemannian metric and $J$ be a compatible almost complex structure on $M^{2 n}$. Then $g$ is Kähler if and only if $\nabla^{L C} J=0$, for the Levi Civita connection $\nabla^{L C}$.

Geometrically, this means that in the Kähler case, complex rotation by $J$ commutes with parallel transport. That is, we immediately get:

Corollary 1.2. Let $g$ be a Riemannian metric and $J$ be a compatible almost complex structure on $M^{2 n}$. Then $g$ is Kähler if and only if $\operatorname{Hol}\left(M^{2 n}, g\right) \subseteq \mathrm{U}(n)$.

The proof of Proposition 1.1 goes as follow. For the "⇐" direction, using that $\nabla^{L C}$ is torsion free, we can rewrite the Nijenhuis tensor as $4 N_{J}(Y, T)=\left(\nabla_{J Y}^{L C} J\right)(T)-J\left(\left(\nabla_{J Y}^{L C} J\right)(T)\right)-\left(\nabla_{J T}^{L C} J\right)(Y)+$ $J\left(\left(\nabla_{T}^{L C} J\right)(Y)\right)$. Thus if $J$ is parallel, $N_{J}$ vanishes and $J$ is integrable. Moreover, by expressing the differential of the associated two form $\omega=g\left(J_{-}, \_\right)$using the covariant derivative $d \omega(Y, T, Z)=$ $\left(\nabla_{Y}^{L C} \omega\right)(T, Z)-\left(\nabla_{T}^{L C} \omega\right)(Y, Z)+\left(\nabla_{Z}^{L C} \omega\right)(Y, T)$, we see that $\omega$ must be closed since $\omega$ is parallel, being so $g$ and $J$. That is, $g$ is Kähler. Conversely, it is easy (but slightly long) to check that $2 g\left(\left(\nabla_{X}^{L C} J\right) Y, Z\right)=d \omega(X, Y, Z)-d \omega(X, J Y, J Z)-g\left(N_{J}(Y, J Z), X\right)$. Hence $J$ has to be parallel if $J$ is integrable and $\omega$ is closed.

Finally, a fundamental tool in the following section will be the:
Theorem $1.3\left(\sqrt{-1} \partial \bar{\partial}-\right.$ Lemma [DGMS75, pages 266-267]). Let $X^{n}$ be a compact Kähler manifold, and let $\eta$ be a real $(1,1)$-form such that $\eta=d \alpha$ for some 1 -form $\alpha$. Then there exists $f \in \mathcal{C}^{\infty}(X ; \mathbb{R})$ such that $\eta=\sqrt{-1} \partial \bar{\partial} f$.

Proof. We briefly review the proof. Write $\alpha=\beta+\bar{\beta}$ for $\beta \in \wedge^{1,0} X$ and note that $\partial \beta=0$. Consider $\partial^{*}$, the $L^{2}$-adjoint of $\partial$ with respect to the $L^{2}$-pairing $(\varphi, \psi)_{L^{2}}:=\int_{X} g^{p \bar{j}} g^{k \bar{q}} \varphi_{p \bar{q}} \overline{\psi_{j \bar{k}}} d V_{g}$. Here Einstein's summation convention to be understood and $g^{p \bar{j}}$ is the inverse of the Hermitian metric $g$. As for $\Delta_{d}=d d^{*}+d^{*} d$, we can analogously define the Laplacians $\Delta_{\partial}$ (and $\Delta_{\bar{\partial}}$ ). A fundamental fact is that for a Kähler metric, $\frac{1}{2} \Delta_{d}=\Delta_{\partial}=\Delta_{\bar{\partial}}$ (this is a consequence of the so-called Kähler identities, see e.g. [Voi07, Theorem 6.7], [Huy05, Proposition 3.1.12]).

Since we have $\int_{X} \partial^{*} \beta \frac{\omega^{n}}{n!}=0$, we can solve the equation
$$\frac{1}{2} \Delta_{d} \varphi=-\partial^{*} \beta$$
for $\varphi$ smooth. Thus we get $\partial^{*}(\beta+\partial \varphi)=0$ and $\partial(\beta+\partial \varphi)=0$, that is, $\beta+\partial \varphi$ is $\partial$-harmonic. Since $\Delta_{\partial}=\Delta_{\bar{\partial}}, \beta+\partial \varphi$ is also $\bar{\partial}$-harmonic; in particular, it is $\bar{\partial}$-closed: $\bar{\partial} \beta=\partial \bar{\partial} \varphi$. Finally, $\eta=d \alpha=\bar{\partial} \beta+\partial \bar{\beta}=\frac{\sqrt{-1}}{2} \partial \bar{\partial} \operatorname{Im} \varphi$. \(\square\)

This lemma allows to identify the space $\mathcal{K}_{[\omega]}$ of Kähler metrics in the Kähler class $[\omega] \in H^{2}(X ; \mathbb{R})$ on $X^{n}$ with the set
$$\left\{\omega+\sqrt{-1} \partial \bar{\partial} \varphi>0: \varphi \in \mathcal{C}^{\infty}(X ; \mathbb{R})\right\},$$
once fixed some background metric $\omega$. This is the first ingredient that explains why the Kähler-Einstein problem is easier than the general Einstein problem: in order to find a KE metric in a fixed cohomology class we need to look for a function $\varphi$ and not for a tensor. The other reason is that there is a very nice formula for the Ricci curvature of a Kähler metric, as we are going to explain.
1.3. Curvatures of Kähler metrics. Consider $\left(M^{2 n}, g\right)$. In this section, we denote by $\nabla:=\nabla_{g}^{L C}$ its Levi Civita connection, and by $\nabla^{\mathbb{C}}$ its complexification to $T M \otimes \mathbb{C}$. Note that $\nabla_{\bar{v}}^{\mathbb{C}} \bar{w}=\overline{\nabla_{v}^{\mathbb{C}} w}$. The complexified Christoffel symbols are defined as $\nabla_{\partial_{z_{i}}}^{\mathbb{C}} \partial_{z_{j}}=\sum_{k}\left(\Gamma_{i j}^{k} \partial_{z_{k}}+\Gamma_{i j}^{\bar{k}} \partial_{z_{\bar{k}}}\right)$ and similar. See e.g. [Szé14], [Tia00, Section 1.2] for more details on what follows.

Lemma 1.4. Let $g$ be a Kähler metric on $M^{2 n}$. Then the only non-zero Christoffel symbols are $\Gamma_{i j}^{k}$ and $\Gamma_{\bar{i} j}^{\bar{k}}=\overline{\Gamma_{i j}^{k}}$. Moreover, $\Gamma_{i j}^{k}=g^{k \bar{\ell}} \partial_{z_{j}} g_{i \bar{\ell}}$.

Let us check $\Gamma_{i j}^{\bar{k}}=0$, for the other is similar. Since $\nabla J=0$, then $\nabla_{\partial_{z_{i}}}^{\mathbb{C}}\left(J^{\mathbb{C}} \partial_{z_{j}}\right)=J^{\mathbb{C}}\left(\nabla_{\partial_{z_{i}}}^{\mathbb{C}}\left(\partial_{z_{j}}\right)\right)$, that is: $\sqrt{-1} \sum_{k}\left(\Gamma_{i j}^{k} \partial_{z_{k}}+\Gamma_{i j}^{\bar{k}} \partial_{z_{\bar{k}}}\right)=\sum_{k}\left(\sqrt{-1} \Gamma_{i j}^{k} \partial_{z_{k}}-\sqrt{-1} \Gamma_{i j}^{\bar{k}} \partial_{z_{\bar{k}}}\right)$. Thus, $\Gamma_{i j}^{\bar{k}}=0$. Next, using $\nabla g=0$ and the vanishing of mixed Christoffel, $\partial_{z_{k}} g_{i \bar{j}}=g\left(\nabla_{\partial_{z_{k}}} \partial_{z_{i}}, \partial_{\bar{z}_{j}}\right)=g\left(\Gamma_{k i}^{l} \partial_{z_{l}}, \partial_{\bar{z}_{j}}\right)=\Gamma_{k i}^{l} g_{l \bar{j}}$. By multiplying with the inverse the proof of the lemma is concluded.

We now consider the Riemannian curvature operator:
$$\operatorname{Rm}^{\mathbb{C}}(v, w) z:=\nabla_{v}^{\mathbb{C}} \nabla_{w}^{\mathbb{C}} z-\nabla_{w}^{\mathbb{C}} \nabla_{v}^{\mathbb{C}} z-\nabla_{[v, w]}^{\mathbb{C}} z .$$
Clearly, $\operatorname{Rm}(\bar{v}, \bar{w}) \bar{z}=\overline{\operatorname{Rm}(v, w) z}$. By using that $\nabla J=0$, we have that $\operatorname{Rm}(v, w) J z=J \operatorname{Rm}(v, w) z$. This implies that $\operatorname{Rm}(z, w)\left(T M^{1,0}\right) \subseteq T M^{1,0}$, and also $\operatorname{Rm}\left(T M^{1,0}, T M^{1,0}\right)=0$ thanks to the symmetries of Rm. This means that the only interesting coefficients of Rm are
$$R_{i \bar{j} k \bar{\ell}}:=g\left(\operatorname{Rm}\left(\partial_{z_{i}}, \partial_{\bar{z}_{j}}\right) \partial_{z_{k}}, \partial_{\bar{z}_{\ell}}\right)$$
and $R_{\bar{i} j \bar{k} \ell}=\overline{R_{i \bar{j} k \bar{\ell}}}$. We have a nice expression for these coefficients:
Proposition 1.5. Let $g$ be a Kähler metric on $M^{2 n}$. Then $R_{i \bar{j} k \bar{\ell}}=-g_{i \bar{j}, k \bar{\ell}}+g^{m \bar{n}} g_{i \bar{n}, k} g_{m \bar{j}, \bar{\ell}}$.
We have denoted with $g_{i \bar{j}, k \bar{\ell}}:=\partial_{z_{k} \bar{z}_{\ell}}^{2} g_{i \bar{j}}$ (and similar) for short. Here the proof:
$$R_{i \bar{j} k \bar{\ell}}=-g\left(\nabla_{\bar{j}}\left(\nabla_{i} \partial_{k}\right), \partial_{\bar{\ell}}\right)=-g\left(\nabla_{\bar{j}}\left(\Gamma_{i k}^{m} \partial_{m}\right), \partial_{\bar{\ell}}\right) \stackrel{\text { Leibniz }}{=}-g\left(\Gamma_{i k, \bar{j}}^{m} \partial_{m}, \partial_{\bar{\ell}}\right)=\Gamma_{i k, \bar{j}}^{m} g_{m \bar{\ell}} .$$
But $\Gamma_{i k, \bar{j}}^{m}=-\partial_{\bar{j}}\left(g^{m \bar{q}} g_{i \bar{q}, k}\right)=g^{m \bar{q}}{ }_{, \bar{j}} g_{i \bar{q}, k}+g^{m \bar{q}} g_{i \bar{q}, k \bar{l}}$. Since $g^{i \bar{j}}{ }_{, \bar{k}}=-g^{i \bar{m}} g^{l \bar{j}} g_{l \bar{m}, \bar{k}}$, we get
$$R_{i \bar{j} k \bar{\ell}}=-g_{m \bar{\ell}}\left(-g^{m \bar{r}} g^{s \bar{q}} g_{s \bar{r}, \bar{j}} g_{i \bar{q}, k}+g^{m \bar{q}} g_{i \bar{q}, n \bar{j}}\right)=-g_{i \bar{j}, k \bar{\ell}}+g^{m \bar{n}} g_{i \bar{n}, k} g_{m \bar{j}, \bar{\ell}}$$
where for the last step we have used the Kähler property and renamed the variables.
Define now the Ricci tensor
$$\operatorname{Ric}_{i \bar{j}}:=g^{k \bar{\ell}} R_{i \bar{j} k \bar{\ell}},$$
and the scalar curvature
$$\mathrm{Sc}:=g^{i \bar{j}} \operatorname{Ric}_{i \bar{j}} .$$

For Kähler metrics, we have the following nice expression:
Proposition 1.6. Let $g$ be a Kähler metric on $M^{2 n}$. Then $\operatorname{Ric}_{i \bar{j}}=-\partial_{i \bar{j}}^{2} \log \operatorname{det}\left(g_{k \bar{\ell}}\right)$.
The proof follows by recalling the formula $\partial(\log \operatorname{det} A)=\operatorname{tr}\left(A^{-1} \partial A\right)$, and plugging in the above formula for the curvature: $-\partial_{i \bar{j}}^{2} \log \operatorname{det}\left(g_{k \bar{\ell}}\right)=-\partial_{i}\left(g^{k \bar{\ell}} g_{k \bar{\ell}, j}\right)=\operatorname{Ric}_{i \bar{j}}$.

Here we remark that clearly in such Kähler case the above are essentially the only non-vanishing terms of the (complexified) Riemannian Ricci tensor.

The expression for Ric in Proposition 1.6 is local, but it actually yields a global real (1, 1)-form: define the Ricci form as
$$\operatorname{Ric}(\omega):=\sqrt{-1} \operatorname{Ric}_{j \bar{k}} d z_{j} \wedge d \bar{z}_{k} \stackrel{\operatorname{loc}}{=}-\sqrt{-1} \partial \bar{\partial} \log \omega^{n} .$$
Here, $\log \omega^{n}$ is short version for $\log \operatorname{det}\left(g_{k \bar{\ell}}\right)$. Thus, we can say that in the Kähler case the Ricci curvature is simply given by the complex Hessian of the logarithm of the volume form! This beautiful expression will have important consequences in the next section, especially in combination with the above $\sqrt{-1} \partial \bar{\partial}$-lemma.

Thus the Kähler-Einstein (KE) condition can be phrased in term of (1,1)-forms by saying that
$$\operatorname{Ric}(\omega)=\lambda \omega,$$
for some "cosmological constant" $\lambda \in \mathbb{R}$. Note that, when $n \geq 2$ (the case $n=1$ being described by the Uniformization Theorem), even taking $\lambda \in \mathcal{C}^{\infty}(X ; \mathbb{R})$, the cosmological factor is in fact
constant, since $0=d \operatorname{Ric}(\omega)=d \lambda \wedge \omega \Rightarrow \lambda=$ constant . This is a short Kähler version of the Riemannian Schur lemma, see e.g. [Bes87, Theorem 1.97]. More generally, if only the scalar curvature is constant we say that $\omega$ is $\csc K$.

Finally, let us note that if $\omega^{\prime}$ is another Kähler metric, then one has
$$\operatorname{Ric}\left(\omega^{\prime}\right)-\operatorname{Ric}(\omega)=\sqrt{-1} \partial \bar{\partial} \log \frac{\omega^{n}}{\omega^{\prime n}}$$
where now $\log \frac{\omega^{n}}{\omega^{\prime n}}$ is a global function on $M^{2 n}$. Being the Ricci form clearly closed, this means that any Kähler metric defines a unique class
$$[\operatorname{Ric}(\omega)]=: 2 \pi c_{1}(X) \in H^{2}(X ; \mathbb{R}) \cap H^{1,1}(X),$$
and we call $c_{1}(X)$ the first Chern class of the complex manifold $X^{n}$ (that is, of the holomorphic tangent bundle, which is the same as the first Chern class of the anti-canonical line bundle $K_{X}^{-1}:=$ $\bigwedge^{n} T X$, i.e. the dual of the canonical bundle; of course, the definition will agree with any other definition of first Chern class you may have seen before).

\section*{2. Calabi's conjectures}
2.1. Statement of Calabi's conjectures and basic Kähler-Einstein. We have seen that, for any compact Kähler manifold ( $X^{n}, \omega$ ), we have $\operatorname{Ric}(\omega) \in 2 \pi c_{1}(X)$; then it is natural to ask what about the converse statement:

Theorem 2.1 (first Calabi conjecture, proven by Yau [Yau77, Yau78]). Let $\left(X^{n}, \omega\right)$ be a compact Kähler manifold, and let $\rho \in 2 \pi c_{1}(X) \in H^{2}(X ; \mathbb{R}) \cap H^{1,1}(X)$. Then there exists a unique metric $\omega^{\prime} \in[\omega]$ such that $\operatorname{Ric}\left(\omega^{\prime}\right)=\rho$.

In particular, when $c_{1}(X)=0$ (that is, when $X$ is Calabi-Yau), the above theorem gives Kähler metric $\omega^{\prime}$ with $\operatorname{Ric}\left(\omega^{\prime}\right)=0$. Historically, these were the first non-flat examples of compact Ricci flat manifolds to have been found. More precisely, Yau's result implies:

Theorem 2.2 (Yau [Yau77, Yau78]). Let $X^{n}$ be a compact Kähler Calabi-Yau manifold, i.e. $c_{1}(X)=0$. Then in any Kähler class there is a unique Kähler-Einstein metric with cosmological constant $\lambda=0$.

As regards the other Kähler-Einstein metrics, we first observe the following important fact:
Proposition 2.3 (after [Kod54]). Let $\left(X^{n}, \omega\right)$ be a compact Kähler-Einstein manifold with cosmological constant $\lambda \neq 0$. Then $X$ is projective algebraic (actually of a very special type, see next), i.e. it has an embedding $X \hookrightarrow \mathbb{C P}^{N}$.

Remark 2.4. - This is not true for $\lambda=0$ (e.g. the generic flat complex torus in dimension bigger than one).
\begin{itemize}
\item[-] The KE metric are not given by the restriction of Fubini-Study metric.
\end{itemize}

The proof requires a little, but important, digression. First, we recall that for any holomorphic Hermitian line bundle $(L, h)$ on a complex manifold $X^{n}$ (obvious definitions), there exists a unique connection $\nabla_{h}^{C h}$ on $L$ being compatible with the Hermitian structure and such that $\nabla^{0,1}=\bar{\partial}$ : it is called the Chern connection, see e.g. [Szé14, Section 1.6], [Gau15, Section 1.7], [Dem12, Section V.12]. More precisely, let $s$ be a local non-vanishing holomorphic section of $L$, and write $h(s)=|s|^{2}$, then the connection 1-form is $\alpha=\frac{\partial h}{h}$. Thus its curvature is $\sqrt{-1} F_{\nabla^{C h}}=-\sqrt{-1} d \alpha=$ $-\sqrt{-1} \partial \bar{\partial} \log h$, and it represents, by definition, the class $2 \pi c_{1}(L)$ where $c_{1}(L) \in H^{2}(X ; \mathbb{R}) \cap H^{1,1}(X)$ is the first Chern class of L.

Second, we say that the Hermitian line bundle ( $L, h$ ) over $X^{n}$ is positive if $\sqrt{-1} F_{\nabla^{C h}}$ is a Kähler metric on $X^{n}$. Note that this is equivalent to ask that there exists a Kähler metric $\omega \in 2 \pi c_{1}(L)(a$ priori a weaker requirement). Indeed, take any Hermitian structure $\tilde{h}$ on $L$, then by the $\sqrt{-1} \partial \bar{\partial}$ -Lemma there exists $\varphi$ such that $\omega-\sqrt{-1} F_{\nabla_{\tilde{h}}^{C h}}=\sqrt{-1} \partial \bar{\partial} \varphi$, and then $\omega=\sqrt{-1} F_{\nabla_{h}^{C h}}$ for $h:=$ $\exp (-\varphi) \tilde{h}$. By the way, this argument precisely says that we can always solve the Hermitian-Einstein equation for line bundles!

We also introduce another notion: a holomorphic line bundle $L$ over $X$ is called ample if there exists a holomorphic embedding $f: X \hookrightarrow \mathbb{C P}^{N}$ such that $L^{\otimes k} \simeq f^{*} \mathcal{O}_{\mathbb{C P}^{N}}(1)$ for some $k$. Here, $\mathcal{O}_{\mathbb{C} \mathbb{P}^{N}}(1)$ is the dual of the tautological line bundle $\mathcal{O}_{\mathbb{C} \mathbb{P}^{N}}(-1)$ of $\mathbb{C} \mathbb{P}^{N}$ (the one that takes the line $\ell \in \mathbb{C}^{n+1}$ over the point $[\ell] \in \mathbb{C P}^{n}$ ).

Next we recall the following very deep theorem by Kodaira that relates the two notions, see e.g. [Voi07, Theorem 7.11], [Dem12, Corollary VII.13.3]:

Theorem 2.5 (Kodaira [Kod54]). A holomorphic line bundle over a compact complex manifold admits a positive Hermitian structure if and only if it is ample.

Of course one direction is trivial: just take the restriction of Fubini-Study metric. The other requires considerably more work. We will describe some of the idea of the proof in subsequent sections using the "pick sections technique".

Proof of Proposition 2.3. If we have a KE metric with positive cosmological section $\operatorname{Ric}(\omega)=\lambda \omega>$ 0, hence, by the discussion at the end of the last lecture the anticanonical bundle is positive. Thus, by Kodaira's theorem, $X$ can be embedded in some projective space (hence it is algebraic, i.e. it is cut by homogeneous polynomial by Chow's theorem, e.g. [GH78]). The case of negative cosmological constant goes along the same lines. \(\square\)

We say that a compact complex manifold is Fano if $c_{1}(X)>0$, i.e. if the first Chern class can be represented by a Kähler form. This is equivalent to say that the anticanonical line bundle is ample, and it is thus a "trivial" necessary condition for a complex manifold to admit KE metric of positive scalar curvature. Note that as an immediate consequence of the first Calabi conjecture, Fano manifolds are precisely the compact complex manifolds admitting Kähler metrics of positive (non necessary costant!) Ricci curvature. If $c_{1}(X)<0$ (equivalenty, the canonical bundle is ample) the manifold is, in particular, of general type (i.e. of top Kodaira dimension, see e.g. [Voi07]). Again this condition is necessary for KE metrics with negative cosmological constant.

Fano manifolds are definitely fewer that manifolds with negative first Chern class. In particular, there are only finitely many diffeomorphism classes of Fano manifolds for fixed dimension [KMM92], see e.g. [Kol96]. The next proposition provides some simple examples Fanos, Calabi-Yaus, and algebraic manifolds with ample canonical bundle.

Proposition 2.6. Let $X_{d}=\left\{F_{d}=0\right\} \subseteq \mathbb{C P}^{n}$ be a smooth hypersurface of degree $d$. Then:
\begin{itemize}
\item[-] if $d<n+1$, then $X_{d}$ is Fano;
\item[-] if $d=n+1$, then $X_{d}$ is Calabi-Yau;
\item[-] if $d>n+1$, then $X_{d}$ is with ample canonical bundle.
\end{itemize}

Proof. We sketch here some ideas for the proof. See e.g. [GH78] for more details on the definitions.
For $Y \subseteq X$ a complex submanifold of codimension 1, we have the short exact sequence of holomorphic vector bundles
$$0 \rightarrow T Y \rightarrow T X\left\lfloor_{Y} \rightarrow N_{Y} \rightarrow 0,\right.$$
and its dual, whence the adjunction formula
$$K_{Y}^{-1}=K_{X}^{-1} \downharpoonright_{Y} \otimes N_{Y},$$
where $N_{Y}^{\vee}=\mathcal{O}(Y)\left\lfloor_{Y}\right.$. Here, given locally $Y \cap U_{\alpha}=\left\{f_{\alpha}=0\right\}$, then $\mathcal{O}(Y)$ is the line bundle with transition functions $g_{\alpha \beta}:=\frac{f_{\alpha}}{f_{\beta}}$. Since $d f_{\alpha}=g_{\alpha \beta} d f_{\beta}$, we have a non-vanishing global section of $N_{Y}^{\vee} \otimes \mathcal{O}(Y)$, that is, $N_{Y}^{\vee} \otimes \mathcal{O}(Y) \simeq \mathcal{O}$ the trivial line bundle.

In our case, we recall that the space of isomorphisms classes of holomorphic line bundles on $\mathbb{C P}^{n}$ is $\operatorname{Pic}\left(\mathbb{C P}^{n}\right)=\langle\mathcal{O}(1)\rangle \simeq \mathbb{Z}$. We have $K_{\mathbb{C P}^{n}} \simeq \mathcal{O}(-1)^{\otimes(n+1)}$ (e.g. since the standard holomorphic volume form on $\mathbb{C}^{n}$ has a pole of order $n+1$ at infinity). Since an hypersurface of degree $d$ is given by a section of $\mathcal{O}(d)$,
$$K_{X_{d}}^{-1} \simeq \mathcal{O}(n+1-d)\left\lfloor X_{d} .\right.$$
The statement follows. \(\square\)

It is worth noting that by choosing different homogeneous polynomials in the above proposition we have different (non-biholomorphic) complex manifolds. For fixed degree $d$ they are all diffeomorphic. The rough "count" of the number of complex moduli parameters considering the $\operatorname{PGL}(n)$ reparametrization is equal to $\binom{n+d}{d}-(n+1)^{2}$. Clearly, from the point of view of studying existence of KE metrics on them, such complex manifolds are all to be considered different.

In our search for KE metrics, the next theorem is crucial:
Theorem 2.7 (second Calabi conjecture, proven by Aubin [Aub76, Aub78], Yau [Yau77, Yau78]). Let $X^{n}$ be a compact complex manifold with ample canonical bundle. Then there exists a unique Kähler metric $\omega \in 2 \pi c_{1}(X)$ such that $\operatorname{Ric}(\omega)=-\omega$.

Thus, thanks to Theorems 2.1 and 2.7, Proposition 2.6 gives many examples of (Kähler)-Einstein metrics: any hypersurface of degree $d \geq n+1$ in $\mathbb{C P}^{n}$ is Kähler-Einstein.

By the way, as regards hypersurfaces in the Fano case, the problem is still open! It is conjectured they all do.

Remark 2.8. It is known that KE metrics exists on hypersurfaces of Fermat type $\sum_{i} z_{i}^{d}=0$ (e.g. [Tia00]). The case of hypersurfaces for $n=3, d=3$ was proved in [Tia90a]. Donaldson (also Odaka independently) showed that the set of Kähler-Einstein manifolds in the space of Fano manifolds is Zariski open under the assumption that the group of holomorphic automorphisms of each manifold is discrete (e.g. [Don15]), hypothesis which holds for hypersurfaces. Fujita recently proved existence of KE metrics on all smooth hypersurfaces of degree $d=n$ in $\mathbb{C P}^{n}$ [Fuj16b]. For $n=4$ the conjecture follows by (very recent!) works [SS17, LX17]. Thus for $3 \leq d \leq n-1$ and $n \geq 5$ the existence problem of KE metrics on all smooth hypersurfaces is open.
2.2. Reduction of Calabi's conjectures to certain PDE's. In this section, we reduce first and second Calabi's conjectures, Theorems 2.1 and 2.7, to a PDE, whose solutions are going to be studied in the following sections.

Consider the first Calabi's conjecture, Theorem 2.1, that is, the problem of representing a chosen form $\rho$ in $2 \pi c_{1}(X)$ as the Ricci form of a metric in $[\omega]$, where $\omega$ is the fixed background metric. Thanks to the $\sqrt{-1} \partial \bar{\partial}$-Lemma, we are reduced to look for $\varphi \in \mathcal{C}^{\infty}(X ; \mathbb{R})$ such that $\omega_{\varphi}:=\omega+$ $\sqrt{-1} \partial \bar{\partial} \varphi>0$ has $\operatorname{Ric}\left(\omega_{\varphi}\right)=\rho$. Again by the $\sqrt{-1} \partial \bar{\partial}$-Lemma, we have $f \in \mathcal{C}^{\infty}(X ; \mathbb{R})$ such that $\operatorname{Ric}(\omega)-\rho=\sqrt{-1} \partial \bar{\partial} f$; we can normalize the Ricci potential $f$ in such a way that $\int_{X} \exp f \omega^{n}=$ $\int_{X} \omega^{n}$. By the expression for the Ricci form of a Kähler metric, Proposition 1.6, we are reduced to solve $\sqrt{-1} \partial \bar{\partial} \log \frac{\omega_{\varphi}^{n}}{\omega^{n}}=\sqrt{-1} \partial \bar{\partial} f$. When $X$ is compact, this reduces to
$$\omega_{\varphi}^{n}=\exp f \omega^{n}$$
In other words, we are prescribing the volume form. In coordinates, this can be written as
$$\operatorname{det}\left(g_{i \bar{j}}+\partial_{z_{i} \bar{z}_{j}}^{2} \varphi\right)=\exp f \operatorname{det} g_{i \bar{j}}$$
which is a complex Monge-Ampère equation a very much studied second oreder non-linear PDE.
Remark 2.9. As regards deep study of complex Monge-Ampère equations, see e.g. [Aub98, LNM2038, GZ17]). As regards real Monge-Ampère equations, see e.g. [GT98, CC95, Fig17] and the references therein.

Similarly, the problem of finding Kähler-Einstein metrics with cosmological constant $\lambda \in \mathbb{R}$ reduces to the equation
$$\omega_{\varphi}^{n}=\exp (f-\lambda \varphi) \omega^{n}$$
In particular, the second Calabi's conjecture, Theorem 2.7, corresponds to $\lambda=-1$, up to homothety:
$$\omega_{\varphi}^{n}=\exp (f+\varphi) \omega^{n} .$$
2.3. Uniqueness of solutions for Calabi's conjectures. In this section, we prove uniqueness of solutions for equations (1) and (3).

Consider first the equation (3) for the second Calabi's conjecture. In this case the proof of uniqueness follows easily by the maximum principle. Assume that $\omega$ and $\omega_{\varphi}$ are two different Kähler-Einstein metrics. We can assume $f=0$ in (3), so we have $\omega_{\varphi}^{n}=\exp \varphi \omega^{n}$. Let $p_{\text {max }}$ be a maximum point for $\varphi$. Then $\partial_{z_{i} \bar{z}_{j}}^{2} \varphi\left(p_{\text {max }}\right) \leq 0$. By using $\omega_{\varphi}^{n}=\exp \varphi \omega^{n}$, we get that $\exp \varphi\left(p_{\text {max }}\right) \leq 1$, then $\varphi(x) \leq \varphi\left(p_{\max }\right) \leq 0$ for any $x$. The same argument for a minimum point $q_{\min }$ gives $\varphi(x) \geq 0$ for any $x$. Thus $\varphi=0$.

Uniqueness, up to additive constants, of solutions for first Calabi's conjecture (1) has been proven by Calabi [Cal57]. The proof now is more subtle, and it needs some non-pointwise estimates. Assume that $\omega_{\varphi}=\omega+\sqrt{-1} \partial \bar{\partial} \varphi$ and $\omega_{\psi}=\omega+\sqrt{-1} \partial \bar{\partial} \psi$ are two different metrics in the same Kähler class $[\omega]$ with the same volume form $\omega_{\varphi}^{n}=\omega^{n}=\omega_{\psi}^{n}$. Consider the Aubin functional [Aub84] as a generalization of the classical Dirichlet energy (see also e.g. [Gau15, Section 4.2]) and [Tia00, page 46]):
$$I_{\omega}(\varphi):=\frac{1}{n!\operatorname{Vol}_{\omega}} \int_{X} \varphi\left(\omega^{n}-\omega_{\varphi}^{n}\right) .$$
We have:
$$\begin{aligned}
0 & \int_{X}(\varphi-\psi)\left(\omega_{\psi}^{n}-\omega_{\varphi}^{n}\right)=-\sqrt{-1} \int_{X}(\varphi-\psi) \partial \bar{\partial}(\varphi-\psi) \wedge \sum_{k=0}^{n-1} \omega_{\varphi}^{k} \wedge \omega_{\psi}^{n-k-1} \\
= & \sqrt{-1} \int_{X} \partial(\varphi-\psi) \wedge \bar{\partial}(\varphi-\psi) \wedge \omega_{\varphi}^{n-1} \\
& +\sqrt{-1} \sum_{k=0}^{n-2} \int_{X} \partial(\varphi-\psi) \wedge \bar{\partial}(\varphi-\psi) \wedge \omega_{\varphi}^{k} \wedge \omega_{\psi}^{n-k} \\
\geq & \sqrt{-1} \int_{X} \partial(\varphi-\psi) \wedge \bar{\partial}(\varphi-\psi) \wedge \omega_{\varphi}^{n-1} \\
= & \frac{1}{n} \int_{X}|\partial(\varphi-\psi)|_{\omega_{\varphi}}^{2} \omega_{\varphi}^{n} \geq 0
\end{aligned}$$
yielding $\partial(\varphi-\psi)=0$. Since $\varphi-\psi$ is real, this gives that $\varphi-\psi$ is constant and so $\omega_{\varphi}=\omega_{\psi}$.
As a consequence, we get:
Proposition 2.10. Let $X^{n}$ be a compact complex manifold with ample canonical bundle. Then any $F \in \operatorname{Aut}(X)$ is an isometry for the Kähler-Einstein metric.

That is, Kähler-Einstein metrics are canonical: namely, the symmetries for the metric are the holomorphic symmetries. Recall that, in such a case, the group of isometries is finite, by Bochner formula, see e.g. [Bes87, Theorem 1.84] and discussions in the next section.
2.4. Existence of solutions for second Calabi's conjecture. We prove existence of a smooth solution for equation (3) by applying the continuity method. We consider the family of equations
$$\omega_{\varphi}^{n}=\exp (t f+\varphi) \omega^{n}$$
varying $t \in[0,1]$. Set
$$E:=\left\{t \in[0,1]: \text { there exists } \varphi_{s} \in \mathcal{C}^{\infty}(X ; \mathbb{R}) \text { solution of }\left(\star_{t}\right) \text { for all } 0 \leq s \leq t\right\} .$$
We prove that:
\begin{itemize}
\item[-] $E \neq \varnothing$ (this is straightforward because $\varphi=0$ is a solution for $\left(\star_{t}\right)$ when $t=0$ );
\item[-] $E$ is open (this will follow by an implicit function argument);
\item[-] $E$ is closed (this will follow by a priori estimates on the solutions).
\end{itemize}
In this case, since $[0,1]$ is connected, we get $E=[0,1]$, and in particular $1 \in E$, assuring that we have a solution for $\left(\star_{t}\right)$ for $t=1$, which is exactly (3).

We prove openness. We can define the Hölder spaces $\mathcal{C}^{k, \alpha}(X)$ (on a compact manifold just take the usual definition in charts; one can also use a fixed background metric and compute the Hölder differences via parallel transport. All these possible constructions give the same spaces with equivalent norms). Consider
$$\mathcal{E}: \mathcal{C}^{k, \alpha}(X) \times[0,1] \rightarrow \mathcal{C}^{k-2, \alpha}(X), \quad(\varphi, t) \mapsto \log \frac{\omega_{\varphi}^{n}}{\omega^{n}}-\varphi-t f,$$
We can then rewrite: $\varphi$ is a solution of $\left(\star_{t}\right)$ if and only if $\mathcal{E}(\varphi, t)=0$. We compute
$$\begin{aligned}
D_{\varphi} \mathcal{E}(\varphi, t)(\psi) & :=\frac{d}{d s} L_{s=0} \mathcal{E}(\varphi+s \psi, t) \\
& =\operatorname{tr}_{\omega_{\varphi}} \sqrt{-1} \partial \bar{\partial} \psi-\psi=-\Delta_{\bar{\partial}} \psi-\psi .
\end{aligned}$$
Since $-\Delta_{\bar{\partial}}$ has non-positive eigenvalues, then the kernel of $D_{\varphi} \mathcal{E}(\varphi, t)$ is zero. Being self-adjoint,, the set of $\mathcal{C}_{\omega}^{k, \alpha}$-solutions is open by implicit function theorem. To prove smoothness of the solution, we can start from $k=2$ using the Evans-Krylov theory [Eva82, Kry82], or from $k=3$ using the Schauder theory (see e.g. [GT98, Chapter 6]). The idea of the Schauder theory is the following. Consider $\varphi_{t}$ a $\mathcal{C}^{3, \alpha}$-regular solution of $\log \operatorname{det}\left(g_{j \bar{k}}+\partial_{z_{j} \bar{z}_{k}}^{2} \varphi_{t}\right)_{j, k}-\log \operatorname{det}\left(g_{j \bar{k}}\right)_{j, k}-\varphi_{t}-t f=0$. By differentiating the equation in $z_{\rho}$, we get
$$g_{\varphi_{t}}^{j \bar{k}}\left(\partial_{z_{\rho}} g_{j \bar{k}}+\partial_{z_{\rho} z_{j} \bar{z}_{k}}^{3} \varphi_{t}\right)-\partial_{z_{\rho}} \log \operatorname{det}\left(g_{j \bar{k}}\right)_{j, k}-\partial_{z_{\rho}} \varphi_{t}-t \partial_{z_{\rho}} f=0 .$$
So locally $\partial_{z_{\rho}} \varphi_{t}$ is a $\mathcal{C}^{2}$-regular solution of
$$L \partial_{z_{\rho}} \varphi_{t}=h$$
where $L:=\Delta_{\omega_{\varphi_{t}}}-1$ (here and later $\Delta_{\omega}:=-\frac{1}{2} \Delta_{d}$, as analyst would prefer) is a second-order linear elliptic operator with $\mathcal{C}^{1, \alpha}$-regular coefficients, and $h:=-g_{\varphi_{t}}^{j \bar{k}} \partial_{z_{\rho}} g_{j \bar{k}}+\partial_{z_{\rho}} \log \operatorname{det}\left(g_{j \bar{k}}\right)_{j, k}+t \partial_{z_{\rho}} f$ is $\mathcal{C}^{1, \alpha}$-regular. By Schauder estimates, see e.g. [GT98, Theorem 6.19], $d \varphi$ is $\mathcal{C}^{3, \alpha}$-regular, then $\varphi$ is $\mathcal{C}^{4, \alpha}$-regular. By bootstrap, we get that $\varphi$ is $\mathcal{C}^{k, \alpha}$-regular for any $k$ and $\alpha$, so $\varphi$ is smooth.

We prove now closedness. (See also e.g. [Tia00, Chapter 5], [Szé14, Chapter 3].) More precisely, let $\left(\varphi_{t_{j}}\right)_{j}$ be a sequence where $\varphi_{t_{j}}$ is a solution of $\left(\star_{t}\right)$ for $t=t_{j}$. We want to prove that $\varphi_{t_{j}} \rightarrow \varphi_{\bar{t}}$ as $t_{j} \rightarrow \bar{t}$, and that $\varphi_{\bar{t}}$ is a solution of $\left(\star_{t}\right)$ for $t=\bar{t}$. This will follow by the following a priori estimates on the solutions of $\left(\star_{t}\right)$ :
\begin{itemize}
\item[(i)] uniform $\mathcal{C}^{0}$-estimate;
\item[(ii)] uniform Laplacian estimate;
\item[(iii)] uniform higher-order estimate.
\end{itemize}

Indeed, if we have $\left\|\varphi_{t_{j}}\right\|_{\mathcal{C}^{3, \alpha} \omega(X)}<C$, then by the Ascoli-Arzelà theorem, see e.g. [Aub98, 3.15], we get that $\varphi_{t_{j}} \rightarrow \varphi_{\bar{t}} \in \mathcal{C}^{3, \alpha^{\prime}}(X)$ for some $0<\alpha^{\prime}<\alpha$, and $\varphi_{\bar{t}}$ is still a solution of $\left(\star_{t}\right)$ for $t=\bar{t}$. Moreover, by the estimate in (ii), we will also get $g_{\varphi}>0$.

Notice that (ii) and (iii), as well as the argument in the paragraph above, hold also for equation (1) and for equation (2). So the difficulty to solve the first Calabi's conjecture essentially arises in adapting the $\mathcal{C}^{0}$-estimate.

The $\mathcal{C}^{0}$-estimate is very easy. This follows directly by applying the maximum principle to $\left(\star_{t}\right)$ as we did in the proof of uniqueness. We get $\left\|\varphi_{t}\right\|_{L^{\infty}} \leq C\|f\|_{L^{\infty}}$ for some constant $C=C\left(X^{n}, \omega\right)$.

We prove the Laplacian estimate. Roughly, we look for an estimate of the type
$$0<n+\Delta_{g} \varphi \leq C\left(\|\varphi\|_{L^{\infty}}\right),$$
where $C$ is a function (exponential) so that together with the $L^{\infty}$ bound give the control on the Laplacian. The crucial estimate is the following: denote $g_{\varphi}=g+\partial^{2} \varphi$, so $\operatorname{tr}_{g} g_{\varphi}=n+\Delta_{g} \varphi$; we prove that there exists a constant $B=B\left(X^{n}, g\right)$ such that
$$\Delta_{g_{\varphi}} \log \operatorname{tr}_{g} g_{\varphi} \geq-B \operatorname{tr}_{g_{\varphi}} g-\frac{\operatorname{tr}_{g} \operatorname{Ric}\left(g_{\varphi}\right)}{\operatorname{tr}_{g} g_{\varphi}}$$
We prove (4). At a point $p_{0}$, we can assume that $g\left(p_{0}\right)=\mathrm{id}$ and $g_{\varphi}\left(p_{0}\right)$ is diagonal. We use also the Kähler condition so at the point $p_{0}$ we can further assume that we have complex normal coordinates, i.e. the first derivatives of the metric $g$ at $p_{0}$ vanish. This can be done for any Kähler metric [GH78]. Then
$$\operatorname{tr}_{g} g_{\varphi}\left(p_{0}\right)=\sum_{i}\left(g_{\varphi}\right)_{i \bar{i}}\left(p_{0}\right), \quad \operatorname{tr}_{g_{\varphi}} g\left(p_{0}\right)=\sum_{j} g_{\varphi}^{j \bar{j}}\left(p_{0}\right)=\sum_{j}\left(g_{\varphi}\right)_{j \bar{j}}\left(p_{0}\right)^{-1} .$$
At $p_{0}$, we compute:
$$\begin{aligned}
\Delta_{g_{\varphi}} \operatorname{tr}_{g} g_{\varphi}\left(p_{0}\right) & =g_{\varphi}^{p \bar{q}} \partial_{z_{p} \bar{z}_{q}}^{2}\left(g^{j \bar{k}}\left(g_{\varphi}\right)_{j \bar{k}}\right) \\
& =g_{\varphi}^{p \bar{q}} \partial_{z_{p} \bar{z}_{q}}^{2} g^{j \bar{k}}\left(g_{\varphi}\right)_{j \bar{k}}+g_{\varphi}^{p \bar{q}} g^{j \bar{k}} \partial_{z_{p} \bar{z}_{q}}^{2}\left(g_{\varphi}\right)_{j \bar{k}} \\
& =g_{\varphi}^{p \bar{q}} \partial_{z_{p} \bar{z}_{q}}^{2} g^{j \bar{k}}\left(g_{\varphi}\right)_{j \bar{k}}-g_{\varphi}^{p \bar{q}} g^{j \bar{k}}\left(\mathrm{R}_{\varphi}\right)_{j \bar{k} p \bar{q}}+g_{\varphi}^{a \bar{b}} g_{\varphi}^{p \bar{q}} g^{j \bar{k}}\left(\partial_{z_{j}}\left(g_{\varphi}\right)_{p \bar{b}}\right)\left(\partial_{\bar{z}_{k}}\left(g_{\varphi}\right)_{a \bar{q}}\right) \\
& =g_{\varphi}^{p \bar{q}} \partial_{z_{p} \bar{z}_{q}}^{2} g^{j \bar{k}}\left(g_{\varphi}\right)_{j \bar{k}}-g^{j \bar{k}}\left(\operatorname{Ric}\left(\omega_{\varphi}\right)\right)_{j \bar{k}}+g_{\varphi}^{a \bar{b}} g_{\varphi}^{p \bar{q}} g^{j \bar{k}}\left(\partial_{z_{j}}\left(g_{\varphi}\right)_{p \bar{b}}\right)\left(\partial_{\bar{z}_{k}}\left(g_{\varphi}\right)_{a \bar{q}}\right) \\
& =g_{\varphi}^{p \bar{p}} \partial_{z_{p} \bar{z}_{p}}^{2} g^{j \bar{j}}\left(g_{\varphi}\right)_{j \bar{j}}-g^{j \bar{k}}\left(\operatorname{Ric}\left(\omega_{\varphi}\right)\right)_{j \bar{k}}+g_{\varphi}^{a \bar{b}} g_{\varphi}^{p \bar{q}} g^{j \bar{k}}\left(\partial_{z_{j}}\left(g_{\varphi}\right)_{p \bar{b}}\right)\left(\partial_{\bar{z}_{k}}\left(g_{\varphi}\right)_{a \bar{q}}\right) \\
& \geq-B g_{\varphi}^{p \bar{p}}\left(g_{\varphi}\right)_{j \bar{j}}-g^{j \bar{k}}\left(\operatorname{Ric}\left(\omega_{\varphi}\right)\right)_{j \bar{k}}+g_{\varphi}^{a \bar{b}} g_{\varphi}^{p \bar{q}} g^{j \bar{k}}\left(\partial_{z_{j}}\left(g_{\varphi}\right)_{p \bar{b}}\right)\left(\partial_{\bar{z}_{k}}\left(g_{\varphi}\right)_{a \bar{q}}\right) \\
& =-B \operatorname{tr}_{g} g_{\varphi} \operatorname{tr}_{g_{\varphi}} g-g^{j \bar{k}}\left(\operatorname{Ric}\left(\omega_{\varphi}\right)\right)_{j \bar{k}}+g_{\varphi}^{a \bar{b}} g_{\varphi}^{p \bar{q}} g^{j \bar{k}}\left(\partial_{z_{j}}\left(g_{\varphi}\right)_{p \bar{b}}\right)\left(\partial_{\bar{z}_{k}}\left(g_{\varphi}\right)_{a \bar{q}}\right) \\
& =-B \operatorname{tr}_{g} g_{\varphi} \operatorname{tr}_{g_{\varphi}} g-g^{j \bar{k}}\left(\operatorname{Ric}\left(\omega_{\varphi}\right)\right)_{j \bar{k}}+\sum_{j} g_{\varphi}^{a \bar{a}} g_{\varphi}^{p \bar{p}}\left|\partial_{z_{j}}\left(g_{\varphi}\right)_{p \bar{a}}\right|_{g}
\end{aligned}$$
where $-B=-B\left(X^{n}, g\right)$ is a lower bound for the holomorphic bisectional curvature of $g$ at $p_{0}$ (which is finite since $X$ is compact). We now compute, at $p_{0}$ :
$$\Delta_{g_{\varphi}} \log \operatorname{tr}_{g} g_{\varphi}\left(p_{0}\right)=\frac{\Delta_{g_{\varphi}} \operatorname{tr}_{g} g_{\varphi}}{\operatorname{tr}_{g} g_{\varphi}}-\frac{g_{\varphi}^{p \bar{q}} \partial_{p}\left(\operatorname{tr}_{g} g_{\varphi}\right) \partial_{\bar{q}}\left(\operatorname{tr}_{g} g_{\varphi}\right)}{\left(\operatorname{tr}_{g} g_{\varphi}\right)^{2}}$$
$$\begin{aligned}
\geq & -B \operatorname{tr}_{g_{\varphi}} g-\frac{g^{j \bar{k}}\left(\operatorname{Ric}\left(\omega_{\varphi}\right)\right)_{j \bar{k}}}{\operatorname{tr}_{g} g_{\varphi}}+\frac{1}{\operatorname{tr}_{g} g_{\varphi}} \sum_{j} g_{\varphi}^{a \bar{a}} g_{\varphi}^{p \bar{p}}\left|\partial_{z_{j}}\left(g_{\varphi}\right)_{p \bar{a}}\right|_{g} \\
& -\frac{1}{\left(\operatorname{tr}_{g} g_{\varphi}\right)^{2}} g_{\varphi}^{p \bar{p}} \partial_{p}\left(g_{\varphi}\right)_{a \bar{a}} \partial_{\bar{p}}\left(g_{\varphi}\right)_{b \bar{b}} .
\end{aligned}$$
We estimate the last term by the Cauchy-Schwarz inequality twice:
$$\begin{aligned}
g_{\varphi}^{p \bar{p}} \partial_{p}\left(g_{\varphi}\right)_{a \bar{a}} \partial_{\bar{p}}\left(g_{\varphi}\right)_{b \bar{b}} & =\left(g_{\varphi}^{p \bar{p}}\right)^{\frac{1}{2}}\left(\partial_{p}\left(g_{\varphi}\right)_{a \bar{a}}\right)\left(g_{\varphi}^{p \bar{p}}\right)^{\frac{1}{2}}\left(\partial_{p}\left(g_{\varphi}\right)_{b \bar{b}}\right) \\
& \leq \sum_{a, b}\left(\sum_{p} g_{\varphi}^{p \bar{p}}\left|\partial_{p}\left(g_{\varphi}\right)_{a \bar{a}}\right|^{2}\right)^{\frac{1}{2}}\left(\sum_{p} g_{\varphi}^{p \bar{p}}\left|\partial_{q}\left(g_{\varphi}\right)_{b \bar{b}}\right|^{2}\right)^{\frac{1}{2}} \\
& =\sum_{a} \sum_{p} g_{\varphi}^{p \bar{p}}\left|\partial_{p}\left(g_{\varphi}\right)_{a \bar{a}}\right|^{2} \\
& =\left(\sum_{a}\left(\left(g_{\varphi}\right)_{a \bar{a}}\right)^{\frac{1}{2}}\left(\sum_{p} g_{\varphi}^{p \bar{p}} g_{\varphi}^{a \bar{a}}\left|\partial_{p}\left(g_{\varphi}\right)_{a \bar{a}}\right|^{2}\right)^{\frac{1}{2}}\right)^{2} \\
& \leq\left(\sum_{a}\left(g_{\varphi}\right)_{a \bar{a}}\right)\left(\sum_{b} \sum_{p} g_{\varphi}^{p \bar{p}} g_{\varphi}^{b \bar{b}}\left|\partial_{p}\left(g_{\varphi}\right)_{b \bar{b}}\right|^{2}\right) .
\end{aligned}$$
Thus we get
$$\begin{aligned}
\Delta_{g_{\varphi}} \log \operatorname{tr}_{g} g_{\varphi}\left(p_{0}\right) \geq & -B \operatorname{tr}_{g_{\varphi}} g-\frac{g^{j \bar{k}}\left(\operatorname{Ric}\left(\omega_{\varphi}\right)\right)_{j \bar{k}}}{\operatorname{tr}_{g} g_{\varphi}}+\frac{1}{\operatorname{tr}_{g} g_{\varphi}} \sum_{j} g_{\varphi}^{a \bar{a}} g_{\varphi}^{p \bar{p}}\left|\partial_{z_{j}}\left(g_{\varphi}\right)_{p \bar{a}}\right|_{g} \\
& -\frac{1}{\left(\operatorname{tr}_{g} g_{\varphi}\right)^{2}} g_{\varphi}^{p \bar{p}} \partial_{p}\left(g_{\varphi}\right)_{a \bar{a}} \partial_{\bar{p}}\left(g_{\varphi}\right)_{b \bar{b}} \\
\geq & -B \operatorname{tr}_{g_{\varphi}} g-\frac{g^{j \bar{k}}\left(\operatorname{Ric}\left(\omega_{\varphi}\right)\right)_{j \bar{k}}}{\operatorname{tr}_{g} g_{\varphi}}+\frac{1}{\operatorname{tr}_{g} g_{\varphi}} \sum_{j} g_{\varphi}^{a \bar{a}} g_{\varphi}^{p \bar{p}}\left|\partial_{z_{j}}\left(g_{\varphi}\right)_{p \bar{a}}\right|_{g} \\
& -\frac{1}{\operatorname{tr}_{g} g_{\varphi}} g_{\varphi}^{p \bar{p}} g_{\varphi}^{a \bar{a}}\left|\partial_{p}\left(g_{\varphi}\right)_{a \bar{a}}\right|^{2} \\
\geq & -B \operatorname{tr}_{g_{\varphi}} g-\frac{g^{j \bar{k}}\left(\operatorname{Ric}\left(\omega_{\varphi}\right)\right)_{j \bar{k}}}{\operatorname{tr}_{g} g_{\varphi}}+\frac{1}{\operatorname{tr}_{g} g_{\varphi}} \sum_{j} g_{\varphi}^{a \bar{a}} g_{\varphi}^{p \bar{p}}\left|\partial_{z_{j}}\left(g_{\varphi}\right)_{p \bar{a}}\right|_{g} \\
& -\frac{1}{\operatorname{tr}_{g} g_{\varphi}} \sum_{j} g_{\varphi}^{p \bar{p}} g_{\varphi}^{a \bar{a}}\left|\partial_{p}\left(g_{\varphi}\right)_{j \bar{a}}\right|^{2} \\
\geq & -B \operatorname{tr}_{g_{\varphi}} g-\frac{g^{j \bar{k}}\left(\operatorname{Ric}\left(\omega_{\varphi}\right)\right)_{j \bar{k}}}{\operatorname{tr}_{g} g_{\varphi}}
\end{aligned}$$
where we used the Kähler condition. This proves (4). We prove now the uniform equivalence between the metrics $g$ and $g_{\varphi}$, that will yield to the Laplacian and to partial $\mathcal{C}^{2}$-estimates. More precisely, we prove that there exists a constant $C=C\left(X^{n}, \omega,\|f\|_{L^{\infty}}, \inf \Delta_{\omega} f,\|\varphi\|_{L^{\infty}}\right)>0$ such that
$$C^{-1} g_{j \bar{k}} \leq\left(g_{\varphi}\right)_{j \bar{k}} \leq C g_{j \bar{k}},$$
by using the maximum principle. We plug-in $\left(\star_{t}\right)$ in the estimate (4) to get:
$$\Delta_{g_{\varphi}} \log \operatorname{tr}_{g} g_{\varphi} \geq-B \operatorname{tr}_{g_{\varphi}} g+\frac{\Delta f+\operatorname{tr}_{g} g_{\varphi}-n-\operatorname{Sc}_{\omega}}{\operatorname{tr}_{g} g_{\varphi}} .$$

By the Cauchy-Schwarz inequality, we have
$$\operatorname{tr}_{g} g_{\varphi} \cdot \operatorname{tr}_{g_{\varphi}} g \geq n^{2}$$
Then, under the normalization for $f$, we have a constant $C$ such that
$$\Delta_{\varphi} \log \operatorname{tr}_{g} g_{\varphi} \geq-C \operatorname{tr}_{g_{\varphi}} g .$$
Since $\Delta_{g_{\varphi}} \varphi=n-\operatorname{tr}_{g_{\varphi}} g$, then for $A \gg 1$ :
$$\Delta_{g_{\varphi}}\left(\log \operatorname{tr}_{g} g_{\varphi}-A \varphi\right) \geq \operatorname{tr}_{g_{\varphi}} g-n A .$$
By the maximum principle, at a maximum point $p_{\text {max }}$, we get
$$\operatorname{tr}_{g_{\varphi}} g\left(p_{\max }\right) \leq A .$$
On the other side, by the equation, we get, in suitable coordinates at $p_{\text {max }}$, that $\prod g_{\varphi, i \bar{i}}\left(p_{\text {max }}\right)=$ $\exp \left(f\left(p_{\text {max }}\right)+\varphi\left(p_{\text {max }}\right)\right) \leq C$ for some constant $C$, then
$$\operatorname{tr}_{g} g_{\varphi}\left(p_{\max }\right) \leq C .$$
Then, at any point,
$$\log \operatorname{tr}_{g} g_{\varphi}-A \varphi \leq C-A \varphi\left(p_{\max }\right),$$
whence
$$\sup \log \operatorname{tr}_{g} g_{\varphi} \leq C .$$

We now shortly discuss higher-order estimates. For the $\mathcal{C}^{3}$ estimates, after Phong-Sesum-Sturm [PSS07], it is convenient to look at estimates of the Christoffel symbols: this will suffice because $g_{\varphi}$ and $g$ are equivalent. Set
$$S(\varphi)_{j k}^{i}:=\Gamma(g)_{j k}^{i}-\Gamma\left(g_{\varphi}\right)_{j k}^{i} .$$
A long computation as before yields,
$$\|S\|_{L^{\infty}} \leq C .$$
By the above $\mathcal{C}^{0}$-estimate, we have that $g_{\varphi}$ is equivalent to $g$, then we get $\left|\partial_{z_{j} z_{k} \bar{z}_{\ell}}^{3} \varphi\right| \leq C$. This gives $\partial_{z_{j} \bar{z}_{k}} \varphi \in \mathcal{C}_{\omega}^{0, \alpha}(X)$, for any $j, k$. By Schauder as before, we get $\partial_{z_{j}} \varphi \in \mathcal{C}_{\omega}^{2, \alpha}(X)$, whence finally $\partial^{3} \varphi \in \mathcal{C}_{\omega}^{0, \alpha}(X)$.
2.5. Existence of solutions for first Calabi's conjecture. We consider now the first Calabi conjecture. Essentially, the only difference is the $\mathcal{C}^{0}$-estimate: the Laplacian and higher-order estimates, as well as the general argument, can be repeated with very small variations, see [Tia00].

Under the suitable normalization $\sup _{X} \varphi=-1$, we prove the Moser iteration:
$$\|\varphi\|_{L^{\infty}} \leq C\left(\|\varphi\|_{L_{\omega}^{2}}+1\right) .$$
By Poincaré inequality, we prove:
$$\|\varphi\|_{L_{\omega}^{2}} \leq C\left(\|\varphi\|_{L_{\omega}^{1}}+1\right) .$$
Finally, by Green function argument, we prove:
$$\|\varphi\|_{L_{\omega}^{1}} \leq C .$$

The essential steps in the Moser iteration are the following. Set $\varphi_{-}:=-\varphi \geq 1$. Consider the equation
$$\begin{aligned}
(\exp f-1) \omega^{n} & =\omega_{\varphi}^{n}-\omega^{n} \\
& =-\sqrt{-1} \partial \bar{\partial} \varphi_{-} \wedge\left(\omega_{\varphi}^{n-1}+\omega_{\varphi}^{n-2} \wedge \omega+\cdots+\omega_{\varphi} \wedge \omega^{n-2}+\omega^{n-1}\right) ;
\end{aligned}$$
now muplitply by $\varphi_{-}^{p}$ and integrate as before:
$$\begin{aligned}
f_{X} \varphi_{-}^{p}(\exp f-1) \omega^{n} & \geq p \cdot f_{X} \varphi_{-}^{p-1} \sqrt{-1} \partial \varphi_{-} \wedge \bar{\partial} \varphi_{-} \wedge \omega^{n-1} \\
& =\frac{4 p}{n(p+1)^{2}} f_{X}\left(\left|\nabla\left(\varphi_{-}^{\frac{p+1}{2}}\right)\right|^{2} \omega^{n},\right.
\end{aligned}$$
(where, hereafter, we use the notation $f_{X} f \omega^{n}=\frac{1}{\operatorname{Vol}_{\omega}} \int_{X} f \omega^{n}$,) and on the other side clearly
$$\operatorname{Cf} f_{X}\left(\varphi_{-}\right)^{p+1} \omega^{n} \geq f_{X} \varphi_{-}^{p}(\exp f-1) \omega^{n} .$$
We use the Sobolev embedding, see e.g. [Aub98, Theorem 2.21], [GT98, Theorem 7.10]:
$$W_{\omega}^{1, q} \hookrightarrow L_{\omega}^{\frac{q \cdot 2 n}{2 n-q}} .$$
Then, for $q=2$ :
$$f_{X}\left(\varphi_{-}\right)^{p+1} \omega^{n} \geq C_{1} \frac{p}{(p+1)^{2}}\left(f_{X}\left|\left(\varphi_{-}\right)^{\frac{p+1}{2}}\right|^{\frac{2 n}{n-1}}\right)^{\frac{n-1}{2 n}}-C_{2} f_{X}\left(|\varphi|^{\frac{p+1}{2}}\right)^{2},$$
which yields
$$\left\|\varphi_{-}\right\|_{L_{\omega}^{(p+1) \frac{n}{n-1}}} \leq(C(p+1))^{\frac{1}{p+1}}\left\|\varphi_{-}\right\|_{L_{\omega}^{p+1}}$$
We iterate (observing that the constant in the above estimate stay under control) to get:
$$\|\varphi\|_{L^{\infty}} \leq \tilde{C}\|\varphi\|_{L_{\omega}^{2}} .$$

We now prove the reduction from $L^{2}$-control to $L^{1}$-control thanks to the Poincaré inequality, see e.g. [Aub98, Corollary 4.3], [GT98, page 164]:
$$\begin{aligned}
C f_{X}|\varphi| \omega^{n} & \geq f_{X} \varphi(1-\exp f) \omega^{n} \\
& \geq \frac{1}{n} f_{X}|\nabla \varphi|^{2} \omega^{n} \\
& \geq \frac{\lambda_{j}(\omega)}{n}\left(f_{X}|\varphi|^{2} \omega^{n}-\left(f_{X} \varphi \omega^{n}\right)^{2}\right),
\end{aligned}$$
using the normalization: $\varphi \leq-1$.
We finally prove the $L^{2}$-control. By consider the Green function $G_{\omega}$, see e.g. [Aub98, Theorem 4.13]: let $p_{\text {max }}$ a maximum point, then
$$-1=\varphi\left(p_{\max }\right)=-f_{X}|\varphi| \omega^{n}-f_{X} \Delta_{\omega} \varphi G_{\omega}\left(p, \_\right) \omega^{n} .$$
Then, using that $\Delta_{\omega} \varphi>-n$, we get:
$$-1+\int_{X}|\varphi| \leq n \int_{X} G_{\omega}\left(p, \_\right) \omega^{n} \leq C .$$
This completes the $\mathcal{C}^{0}$ estimate for the first Calabi conjecture.
2.6. Consequences of Calabi's conjectures. We give here some applications of the Calabi conjecture.

Theorem 2.11 (Kobayashi [Kob74], Yau [Yau77]). A Fano manifold is simply-connected.
Proof. Consider $\pi: \tilde{X} \rightarrow X$ the universal cover. By assumption, $X$ is Fano, that is, there exists a Kähler form $\omega \in 2 \pi c_{1}(X)>0$. By the first Calabi conjecture, Theorem 1, there exists a Kähler form
$\omega^{\prime}$ on $X$ such that $\operatorname{Ric}\left(\omega^{\prime}\right)=\omega$. Consider the Kähler metric $\pi^{*} \omega^{\prime}$ on $\tilde{X}$. It has $\operatorname{Ric}\left(\pi^{*} \omega^{\prime}\right)=\pi^{*} \omega>0$ bounded below away from zero. Then, by the Myers theorem in Riemannian geometry, see e.g. [Bes87, Theorem 6.51], $\tilde{X}$ is compact, and so it is Fano too. By using that $X$ is Fano, that is the anticanonical bundle is ample whence positive, and thanks to the Kodaira vanishing theorem, see e.g. [Voi07, Theorem 7.13], we have $h^{0, j}(X)=\operatorname{dim} H^{j}\left(X ; \mathcal{O}_{X}\right)=\operatorname{dim} H^{j}\left(X ; K_{X} \otimes K_{X}^{-1}\right)=0$ for $j>0$; it follows that the Euler characteristic for the structure sheaf $\mathcal{O}_{X}$ is $\chi\left(\mathcal{O}_{X}\right):=\sum_{j}(-1)^{j} h^{0, j}(X)=1$. For the same reasons, also $\chi(\tilde{X})=1$. On the other side, the Euler characteristic is additive on a cover, for example, as a consequence of the Hirzebruch-Riemann-Roch theorem. Then $X=\tilde{X}$. \(\square\)

As innocent as it seems, the above statement is kind of deep:
Remark 2.12. • The Calabi's conjecture is crucially used to prove that the universal cover is compact. All the other arguments would work the same for arbitrary finite covers, giving the weaker statement that $X$ has trivial pro-finite completion of the fundamental group.
\begin{itemize}
\item[-] There exists a fully algebraic prove that makes use of rationally connectivity of Fanos (hence also very deep results in algebraic geometry based on Mori's Bend-and-Break, which uses reduction in finite characteristic $p$ (e.g. [Mor79, KM98, Deb01]).
\end{itemize}

The next consequence is a very famous inequality between Chern numbers.
Theorem 2.13 (Bogomolov-Miyaoka-Yau inequality [VdV66, Bog78, Miy77, Yau77, Yau78]). Let $X^{n}$ be a compact Kähler manifold.
\begin{itemize}
\item[-] If $X^{n}$ is Fano Kähler-Einstein, then
$$n c_{1}^{n}(X) \leq 2(n+1) c_{1}^{n-2}(X) c_{2}(X),$$
with equality if and only if $X=\mathbb{C} \mathbb{P}^{n}$.
\item[-] If $X^{n}$ is with ample canonical bundle, and then Kähler-Einstein by Theorem 3, then
$$n(-1)^{n-2} c_{1}^{n}(X) \leq 2(n+1)(-1)^{n-2} c_{1}^{n-2}(X) c_{2}(X),$$
with equality if and only if $X^{n}=\mathbb{B}^{n} / \Gamma$.
\end{itemize}

Proof. For more details see e.g. [Tos17]. First of all, we fix $\omega$ Kähler-Einstein, with cosmological constant $\lambda$, and we notice that we can rewrite the two inequalities that we want to prove as
$$\left(\frac{2(n+1)}{n} c_{2}-c_{1}^{2}\right)[\omega]^{n-2} \geq 0,$$
and we also want to prove that equality holds if and only if $X$ has constant holomorphic sectional curvature. Indeed, recall that simply-connected Kähler manifolds with constant holomorphic sectional curvature are holomorphically isometric to either $\mathbb{C}^{n}$, or $\mathbb{B}^{n}$, or $\mathbb{C P}^{n}$, up to homothety, see e.g. [KN2, Theorems IX.7.8, IX.7.9] (the proof is very similar to the corresponding result in the real case). Recall that the holomorphic sectional curvature is $H(X):=K(X \wedge J X):=R(X, J X, J X, X)$ for $|X|=1$. Then $H$ is constant if and only if the traceless part $R^{0}$ of $R$ vanishes, where:
$$R_{i \bar{j} k \bar{\ell}}^{0}=R_{i \bar{j} k \bar{\ell}}-\frac{\lambda}{n+1}\left(g_{i \bar{j}} g_{k \bar{\ell}}+g_{i \bar{\ell}} g_{k \bar{j}}\right) .$$
Using the KE condition, we immediately see that
$$\left|R^{0}\right|^{2}=|R|^{2}-\frac{2 \lambda^{2} n}{n+1}$$
Let $\Omega_{i}^{j}=\sqrt{-1} \sum R_{i}{ }^{j}{ }_{k \bar{l}} d z_{k} \wedge d \bar{z}_{l}$ be the curvature seen as a form valued endomorphism of the tangent bundle. By Chern-Weil theory we can represent the first Pontryagin class (if you want,
this a possible definition of such class) as:
$$\left(2 \pi^{2}\right)^{-1} \operatorname{tr}(\Omega \wedge \Omega):=\left(2 \pi^{2}\right)^{-1} \sum_{i, k} \Omega_{i}^{k} \wedge \Omega_{k}^{i} \in p_{1}(X)=c_{1}^{2}(X)-2 c_{2}(X) .$$
Then, using the KE condition again, we compute:
$$n(n-1) \operatorname{tr}(\Omega \wedge \Omega) \wedge \omega^{n-2}=\left(\lambda^{2} n-|R|^{2}\right) \omega^{n}$$

Finally, integrating (5) and (6) on $X$,
$$\frac{1}{n(n-1) 4 \pi^{2}} \int_{X}\left|R^{0}\right|^{2} \omega^{n}=\left(2 c_{2}(X)-\frac{n}{n+1} c_{1}^{2}(X)\right)[\omega]^{n-2},$$
whence we get the statement. \(\square\)

Remark 2.14. We would like to make some observations on the Bogomolov-Miyaoka-Yau (BMY) inequality.
\begin{itemize}
\item[-] For compact complex surfaces, the BMY inequalities reduce to
$$c_{1}^{2} \leq 3 c_{2}$$
where $c_{2}=e(X)$ is the topological Euler characteristic and $c_{1}^{2}=2 e(X)+3 \tau(X)$ with $\tau(X)$ the signature of the intersection form on the second cohomology. Hence it is purely topological. Surfaces which realize the equality are hard to construct (e.g. Mumford Fake projective spaces [Mum79]).
\item[-] For Fano KE threefolds, the BMY inequality reduces to
$$c_{1}^{3}(X) \leq 64=c_{1}^{3}\left(\mathbb{C P}^{3}\right)$$
thanks to the fact that $c_{1}(X) c_{2}(X)=24 \int_{X} \operatorname{td}(X)=\chi\left(\mathcal{O}_{X}\right)=1$. In dimension $n \geq 4$, it is proven that for KE Fano manifolds [Fuj15]
$$c_{1}^{n}(X) \leq(n+1)^{n}=c_{1}^{n}\left(\mathbb{C P}^{n}\right)$$
continues to hold (not as a consequence of BMY, but using K- stability considerations). We should remark that there are Fano manifolds whose volume is bigger than $c_{1}^{n}\left(\mathbb{C P}^{n}\right)$ : e.g. certain $\mathbb{C P}^{1}$-bundles over $\mathbb{C P}^{3}$.
\end{itemize}
---
retention_scope: session
part: 1
total_parts: 3
---

[Part 1/3 of: Degenerating conic Kähler–Einstein metrics to the normal cone]

---
source_file: Degenerating_conic_Kähler_Einstein_metrics_to_the_normal_cone_2d8b110a398c.pdf
converter: mathpix
format: mmd
---

\title{
DEGENERATING CONIC KÄHLER-EINSTEIN METRICS TO THE NORMAL CONE
}

\author{
OLIVIER BIQUARD AND HENRI GUENANCIA
}

\begin{abstract}
Let $X$ be a Fano manifold of dimension at least 2 and $D$ be a smooth divisor in a multiple of the anticanonical class, $\frac{1}{\alpha}\left(-K_{X}\right)$ with $\alpha>1$. It is well-known that Kähler-Einstein metrics on $X$ with conic singularities along $D$ may exist only if the angle $2 \pi \beta$ is bigger than some positive limit value $2 \pi \beta_{*}$. Under the hypothesis that the automorphisms of $D$ are induced by the automorphisms of the pair $(X, D)$, we prove that for $\beta>\beta_{*}$ close enough to $\beta_{*}$, such Kähler-Einstein metrics do exist. We identify the limits at various scales when $\beta \rightarrow \beta_{*}$ and, in particular, we exhibit the appearance of the Tian-Yau metric of $X \backslash D$.
\end{abstract}

\section*{Contents}
1. Introduction ..... 1
2. Geometric setup ..... 8
3. Conic Calabi Ansatz: construction and asymptotics ..... 11
4. Automorphisms and related objects ..... 29
5. The tubular neighbourhood of $D$ ..... 31
6. The Tian-Yau metric and its formal perturbation ..... 37
7. Gluing and linear analysis ..... 43
8. Estimating the error and the obstruction ..... 54
9. Resolution of the Monge-Ampère equation ..... 64
10. Examples ..... 68
References ..... 69

\section*{1. Introduction}
1.1. Kähler-Einstein metrics with cone singularities along a divisor. Let $X$ be a compact Kähler manifold of dimension $n$ and let $D$ be a smooth divisor on $X$. Given $\beta \in(0,1)$, we say that a Kähler metric $\omega$ on $X \backslash D$ is a Kähler-Einstein metric with cone angle $2 \pi \beta$ along $D$ ( $\mathrm{KE}_{\beta}$ for short) if
\begin{itemize}
\item[-] Ric $\omega=\mu \omega$ on $X \backslash D$, for some $\mu \in \mathbb{R}$,
\item[-] $\omega$ has cone singularities with cone angle $2 \pi \beta$ along $D$.
\end{itemize}

In this paper, we will only focus on the case $\mu>0$, so that a $\mathrm{KE}_{\beta}$ metric will be assumed to have positive scalar curvature unless stated otherwise.

The second item in the definition above means that if $\left(z_{1}, \ldots, z_{n}\right)$ is any holomorphic system of coordinates on a neighborhood $U$ of a point in $D$ such that $D=\left(z_{1}=0\right)$, then $\left.\omega\right|_{U \backslash D}$ is quasi-isometric to the model flat cone metric
$$\frac{i d z_{1} \wedge d \bar{z}_{1}}{\left|z_{1}\right|^{2(1-\beta)}}+\sum_{j \geqslant 2} i d z_{j} \wedge d \bar{z}_{j} .$$
In particular, $\omega$ extends canonically to a Kähler current on $X$ in the cohomology class $-\mu^{-1} c_{1}\left(K_{X}+(1-\beta) D\right)$ which satisfies
$$\operatorname{Ric} \omega=\omega+(1-\beta)[D] .$$
A natural and important question is, given a pair $(X, D)$, to determine the set $I:=\left\{\beta \in(0,1) ; \exists \mathrm{KE}_{\beta}\right.$ metric $\left.\omega_{\beta}\right\}$ and understand what happens to $\omega_{\beta}$ when $\beta$ approached a critical value $\beta_{*} \in \partial I$.

A necessary condition for the existence of a $\mathrm{KE}_{\beta}$ metric is that $-\left(K_{X}+(1-\right.$ $\beta) D)$ be ample, but just as when $D=0$, this condition is not sufficient in general. We refer to [CDS14, $\mathrm{BBE}^{+}$19, DR17, BBJ21, Li22] and the references therein for an account of the problem.

Determining the admissible cone angles and understanding degeneration of conic Kähler-Einstein metrics has drawn a lot of attention in the last decade, see e.g. [Szé13, LS14, Gue20, BG22, RZ22, Del24].
1.2. Statement of the main theorem. Let us start by introducing the objects involved in the main theorem below.
1.2.1. Varieties. Let $X$ be a Fano manifold of dimension $n \geqslant 2$ such that $-K_{X} \sim_{\mathrm{Q}}$ $\alpha D$ for some positive rational number $\alpha \in \mathbb{Q}$ satisfying $\alpha>1$. Note that the case $\alpha=1$ has already been fully treated in [BG22]. The case $\alpha \in(0,1)$ is quite different and involves the incomplete Ricci flat cone metrics constructed in [Bre13, GP16, JMR16], but we will not discuss it further here.

From the assumptions above, $D$ is a connected Fano manifold and we will further assume that it admits a Kähler-Einstein metric $\omega_{D}$, i.e. Ric $\omega_{D}=\omega_{D}$. Let $L:=\left.N_{D} \simeq \mathcal{O}_{X}(D)\right|_{D}$ be the normal bundle of $D$ and set $v$ to be the fiber coordinate so that $L=\left\{(x, v) ; x \in D, v \in L_{x}\right\}$. We consider the hermitian metric $h$ on $L$ (unique up to a multiplicative constant) such that $i \Theta(L, h)=\frac{1}{\alpha-1} \omega_{D}$.

Next let $\bar{L}=L \sqcup\left\{x_{\infty}\right\}$ be the one-point compactification of $L$; it can be endowed with a structure of normal projective variety. Moreover, $\bar{L} \backslash D$ is an affine cone over $D$ with apex $x_{\infty}$, cf section 2 below.

Small neighborhoods $\mathcal{U}_{L} \subset X$ of $D$ (resp. $\Delta_{L} \subset L$ of the zero section $O_{L} \simeq$ $D \subset L$ ), which are in general non isomorphic, are pseudoconcave and carry a multivalued meromorphic $n$-form $\Omega$ (resp. $\Omega_{L}$ ) with a pole of order $\alpha$ along $D$; it is unique up to constant scaling by pseudoconcavity. One can define
$$j_{0} \in \mathbb{N}_{>0} \cup\{+\infty\}$$
to be the largest integer such that there exists a diffeomorphism Y : $\Delta_{L} \rightarrow \mathcal{U}_{L}$ such that $\mathrm{Y}^{*} \Omega$ and $\Omega_{L}$ coincide up to order $j_{0}-1$, cf Proposition 5.3. Observe that since the $n$-form determines the complex structure, $j_{0}$ coincides with the largest integer such that the formal neighborhoods of $D \subset X$ (resp. $D \subset L$ ) of order $j_{0}-1$ are isomorphic. By definition, this means that $j_{0}$ is the largest integer such that the ringed spaces $\left(D, \mathcal{O}_{X} / \mathcal{I}_{D}^{j_{0}}\right)$ and $\left(D, \mathcal{O}_{L} / \mathcal{I}_{D}^{j_{0}}\right)$ are isomorphic.
1.2.2. Metrics. An important numerical factor in the following is the positive number
$$\beta_{*}:=\frac{\alpha-1}{n} .$$
Let us recall that one can always assume that $\alpha<n+1$ (cf section 2). That is, we have $\beta_{*} \in(0,1)$.

The Calabi Ansatz enables one to construct on $\bar{L} \backslash D$ two canonical Kähler-Einstein metrics (of positive and zero curvature, respectively) having a conical singularity at the point $x_{\infty}=\bar{L} \backslash L$.
\begin{itemize}
\item[-] The Ricci flat Tian-Yau cone metric $\omega_{\mathrm{TY}, L}:=d d^{c}|v|_{h}^{-2 \beta *}$ which is complete near $D \subset L$.
\item[-] The $\mathrm{KE}_{\beta_{*}}$ metric $\omega_{\beta_{*}, L}:=d d^{c} \log \left(1+|v|_{h}^{-2 \beta_{*}}\right)$. It satisfies Ric $\omega_{\beta_{*}, L}=$ $\omega_{\beta_{*}, L}$ on $L \backslash D$, has cone singularities of angle $2 \pi \beta_{*}$ along $D \subset L$ and it is asymptotic to $\omega_{\mathrm{TY}, L}$ near the conical point.
\end{itemize}

We will explain in section 2.3 that the Calabi Ansatz metric $\omega_{\beta_{*}, L}$ is rigid in the sense that it is the only Kähler-Einstein metric on $\bar{L}$ with cone singularities along $D$.

Finally, Tian and Yau [TY91] proved that under our assumptions, there exists
\begin{itemize}
\item[-] A complete Ricci flat Kähler metric $\omega_{\mathrm{TY}}$ on $X \backslash D$ which is asymptotic to $\omega_{\mathrm{TY}, L}$ at infinity,
\end{itemize}
and we refer to section 6 for more details.
1.2.3. Results. For $\beta \in(0,1)$, we consider the Kähler-Einstein equation
$$\operatorname{Ric} \omega_{\beta}=\mu \omega_{\beta}+(1-\beta)[D]$$
where $\mu=\mu(\beta)>0$ is given by $\mu \alpha=\alpha+\beta-1$, so that $\omega_{\beta} \in c_{1}(X)=\alpha c_{1}(D)$ is fixed, independent of $\beta$. Since $\mu\left(\beta_{*}\right)>0$ the difference between normalizing the Einstein constant to be 1 or $\mu_{\beta}$ is geometrically irrelevant. Consider the interval
$$I:=\left\{\beta \in(0,1] ; \exists \omega_{\beta} \text { solution of }\left(\mathrm{KE}_{\beta}\right)\right\} .$$
It is known that $I$ is either empty or of the form $\left(\beta_{*}, \beta^{*}\right)$ (or $\left(\beta_{*}, \beta^{*}\right]$ ) where $\beta_{*}$ is defined in (1.2), cf Proposition 2.1. The identification of $\beta^{*}$ is a complicated problem in general and depends very much on the geometry of the pair $(X, D)$, cf [Szé13]. However, $I$ is never empty (i.e. $\beta^{*}>\beta_{*}$ ) as a byproduct of our main result below.

Main Theorem. Let $X$ be a Fano manifold of dimension $n \geqslant 2$ and let $D$ be a smooth divisor such that $-K_{X} \sim_{\mathrm{Q}} \alpha D$ for some $\alpha \in \mathbb{Q}_{>1}$. Assume that $D$ is Kähler-Einstein and that the restriction map $\operatorname{Aut}^{\circ}(X, D) \rightarrow \operatorname{Aut}^{\circ}(D)$ is onto. Then there exists $\delta>0$ such that
\begin{itemize}
\item[1.] For any $\beta \in\left(\beta_{*}, \beta_{*}+\delta\right)$, there exists a $\mathrm{KE}_{\beta}$ metric $\omega_{\beta}$.
\item[2.] There is convergence
$$\left(X, \omega_{\beta}\right) \underset{\beta \rightarrow \beta_{*}}{\longrightarrow}\left(\bar{L}, \omega_{\beta_{*}, L}\right)$$
in the Gromov-Hausdorff topology.
\item[3.] We have
$$\varepsilon_{\beta}^{-1} \omega_{\beta} \underset{\beta \rightarrow \beta_{*}}{\longrightarrow} \omega_{\mathrm{TY}} \quad \text { in } \quad C_{\mathrm{loc}}^{\infty}(X \backslash D),$$
where $\varepsilon_{\beta}$ is defined by
$$\varepsilon_{\beta}= \begin{cases}\left(\beta-\beta_{*}\right)^{\frac{\alpha-1}{n j_{0}}} & \text { if } j_{0}<\alpha-1 \\ \left(\frac{\beta-\beta_{*}}{-\log \left(\beta-\beta_{*}\right)}\right)^{\frac{1}{n}} & \text { if } j_{0}=\alpha-1 \\ \left(\beta-\beta_{*}\right)^{\frac{1}{n}} & \text { if } j_{0}>\alpha-1\end{cases}$$
where $j_{0}$ is defined in (1.1).
\end{itemize}

Remark 1.1. Let us first make a few remarks
\begin{itemize}
\item[(1)] As a corollary and under the assumption that $\mathrm{Aut}^{\circ}(X, D) \rightarrow \mathrm{Aut}^{\circ}(D)$ is onto, we get that the Tian-Yau metric $\omega_{\mathrm{TY}}$ is canonically attached to the pair $(X, D)$, modulo the obvious scaling and the action of $\operatorname{Aut}^{\circ}(X, D)$.
\item[(2)] The condition that $\operatorname{Aut}^{\circ}(X, D) \rightarrow \operatorname{Aut}^{\circ}(D)$ is onto is satisfied automatically if $X$ is toric, cf Lemma 4.2. We are not aware of pairs $(X, D)$ as in our setup for which there are holomorphic vector fields on $D$ which do not lift to $X$. If $X$ is allowed to be singular, such examples can be constructed, cf Example 4.3.
\item[(3)] In section 10 we provide examples where the three possible values for $\varepsilon_{\beta}$ are achieved.
\item[(4)] Thanks to [Ber15], any two $\mathrm{KE}_{\beta}$ metrics are related by an element in Aut $^{\circ}(X, D)$. In particular the isometry class of the metric space $\left(X, \omega_{\beta}\right)$ does not depend on the particular $\mathrm{KE}_{\beta}$ metric.
\end{itemize}

In the case of $\left(\mathbb{P}^{2}, Q\right)$ where $Q$ is the smooth quadric, the result above was conjectured by Li and Sun [LS14] and shortly after numerical evidence to that conjecture was provided by Li [Li15]. Recently, Delcroix [Del24] settled the conjecture in full - he actually considers the more general situation of a rank one horosymmetric Fano manifold with the divisor being a codimension one orbit.
1.3. Strategy of proof. The proof involves several steps.
1.3.1. Construction of the model metric near $D$. We work on the normal bundle $L$ and solve the conic Calabi Ansatz to construct a semi-explicit Kähler-Einstein metric $\omega_{\beta, L}=d d^{c} \phi_{\beta, L}$ on $L$ with cone singularities of angle $2 \pi \beta$ along the zero section $D \subset L$; we refer to section 3 for details relative to the conic Calabi Ansatz in this setting. The Ansatz can be used for every angle $\beta \in(0,1)$ but the angle $\beta_{*}$ is critical in the following sense.

For $\beta<\beta_{*}, \omega_{\beta, L}$ acquires a cone singularity along the divisor at infinity $D_{\infty}=\mathbb{P}\left(0 \oplus \mathcal{O}_{D}\right)$ in the smooth compactification $\mathbb{P}\left(L \oplus \mathcal{O}_{D}\right)$ of $L$.

At $\beta=\beta_{*}, D_{\infty}$ is contracted, and $\omega_{\beta_{*}, L}$ has a conical singularity at the singular point at infinity of the compactification $\bar{L}$ of $L$.

Finally, for $\beta>\beta_{*}, \omega_{\beta, L}$ is only defined away from some euclidean neighborhood $D_{\infty}$ (or, equivalently, $x_{\infty}$ ). More precisely, the domain of definition of $\omega_{\beta, L}$ is larger and larger as $\beta \searrow \beta_{*}$ and one can identify a zone (escaping to infinity in $L$ ) where the potential has the asymptotics
$$\phi_{\beta, L}=\phi_{\beta_{*}, L}+\frac{\beta-\beta_{*}}{r^{2 n-2}}+\text { l.o.t. }$$
where $r$ is the radius for the Ricci flat cone metric $g_{L}$ on $L$ (to which $\omega_{\beta_{*}, L}$ is asymptotic near the conical point).
1.3.2. Gluing with the Tian-Yau metric. Fix two parameters $\varepsilon>0$ and $\beta>\beta_{*}$. It can be useful to think of $\varepsilon$ as the (modulus of the) base parameter in the deformation $\pi: \mathcal{X} \rightarrow \mathbb{C}$ of $X$ to the normal cone of $D$. The ultimate goal is to produce for each $\varepsilon>0$ small enough an angle $\beta=\beta(\varepsilon)$ and a $\mathrm{KE}_{\beta}$ metric $\omega_{\mathrm{KE}, \beta(\varepsilon)}$ on $X$ (thought of as $X_{\varepsilon}=\pi^{-1}(\varepsilon)$ ). Moreover one wants $\beta(\varepsilon) \rightarrow \beta_{*}$ as $\varepsilon \rightarrow 0$.

Using a diffeomorphism identifying a neighborhood of $D \subset X$ with a neighborhood of $D \subset L$, one can cook up a Kähler metric $\omega_{\beta, \varepsilon}$ on $X$ obtained by gluing $\omega_{\beta, L}$ and $\varepsilon \omega_{\mathrm{TY}}$ closer and closer to $D$ as $\varepsilon \rightarrow 0$. Constructing a $\mathrm{KE}_{\beta}$ metric $\omega_{\beta, \varepsilon}+d d^{c} f$ amounts to solving a Monge-Ampère equation
$$P_{\beta, \varepsilon}(f)=0 .$$
The relevant properties of $P_{\beta, \varepsilon}$ are as follows.
\begin{itemize}
\item[-] $P_{\beta, \varepsilon}(0)$ measures the "Kähler-Einstein" defect of $\omega_{\beta, \varepsilon}$. It arises from three factors: the difference between the complex structures of $X$ and $L$, the cut-offs performed to glue the two model metrics, the fact that $\omega_{\mathrm{TY}}$ is Ricci-flat rather than having positive Einstein constant.
\item[-] $d P_{\beta, \varepsilon}(0)=\Delta_{\omega_{\beta, \varepsilon}}+\mu_{\beta}=: L_{\beta, \varepsilon}$ where $\mu_{\beta}$ is our choice of Einstein constant (it depends linearly on $\beta$ with $\mu_{\beta_{*}}>0$, so one can think of it as being constant). Small eigenvalues of $L_{\beta, \varepsilon}$ represent the obstructions to deform $\omega_{\beta, \varepsilon}$ to a $\mathrm{KE}_{\beta}$ metric.
\end{itemize}
1.3.3. Resolution modulo the obstruction. The obstructions arise at least conceptually from three sources: harmonic functions on $\left(X \backslash D, g_{\mathrm{TY}}\right)$, harmonic functions on the cone $\left(L, g_{L}\right)$ and functions on $L$ in the kernel of $\Delta_{\omega_{\beta_{*}, L}}+\mu_{\beta_{*}}$. One can relatively easily kill the first two using suitable weighted Hölder spaces, hence we are left to dealing with the third kind of obstruction.

Since $\omega_{\beta_{*}, L}$ is Kähler-Einstein, there is a one-to-one correspondence between $\operatorname{ker}\left(\Delta_{\omega_{\beta_{*}, L}}+\mu_{\beta_{*}}\right)$ and $H^{0}\left(L, T_{L}\right) \simeq H^{0}\left(D, T_{D}\right) \oplus \mathbb{C} \xi$ where $\xi$ is the radial vector field generating the $\mathbb{C}^{*}$ action. The assumption that vector fields on $D$ lift to $X$ combined with the fact that Aut ${ }^{\circ}(D)=G^{\mathbb{C}}$ is reductive (since $D$ is KE) allows us to work equivariantly with respect to a compact group $G \subset \operatorname{Aut}{ }^{\circ}(X, D)$ and kill the obstruction induced by $H^{0}\left(D, T_{D}\right)$.

One can find an explicit function $\tau_{\beta}$ solving $i_{\xi} \omega_{\beta, L}=\bar{\partial} \tau_{\beta}$ which we then transplant to a function $\tau_{\beta, \varepsilon}$ on the whole $X$ satisfying $\left|L_{\beta, \varepsilon} \tau_{\beta, \varepsilon}\right| \ll 1$. Therefore $\tau_{\beta, \varepsilon}$ is asymptotically in the cokernel of $L_{\beta, \varepsilon}$ and represents the one obstruction remaining in order to solve $P_{\beta, \varepsilon}(f)=0$. In particular, one can solve modulo obstruction, i.e. one can find a (unique) function $f=f_{\beta, \varepsilon}$ such that
$$P_{\beta, \varepsilon}\left(f_{\beta, \varepsilon}\right)^{\perp}=0$$
i.e. $P_{\beta, \varepsilon}\left(f_{\beta, \varepsilon}\right)=a\left(f_{\beta, \varepsilon}\right) \cdot \tau_{\beta, \varepsilon}$ for a constant $a\left(f_{\beta, \varepsilon}\right) \in \mathbb{R}$. Actually, even that equation cannot be solved readily because $P_{\beta, \varepsilon}(0)$ is not small enough to apply the implicit function theorem, cf Remark 9.2. This has to do with the fact that the Tian-Yau metric does not provide a good enough approximation of the solution (e.g. since it is Ricci flat). So it is necessary to construct a formal perturbation of $\omega_{\mathrm{TY}}$ at a large order and use that metric instead of $\omega_{\mathrm{TY}}$ in the gluing.
1.3.4. Deforming the cone angle to kill the obstruction. We have two parameters $\varepsilon, \beta$ and one obstruction $a(\beta, \varepsilon):=a\left(f_{\beta, \varepsilon}\right)$ to kill. A signification fraction of the present paper is devoted to showing that the obstruction has an expansion which looks like
$$a(\beta, \varepsilon)=F(\varepsilon)-\left(\beta-\beta_{*}\right)+\text { l.o.t. }$$
where $F(\varepsilon)$ is a positive quantity which has either the form $F(\varepsilon)=\varepsilon^{v}$ (for some $1 \leqslant v \leqslant n$ ) or $F(\varepsilon)=\varepsilon^{n} \log \frac{1}{\varepsilon}$ depending on the convergence rate of $J_{X}$ to $J_{L}$ near $D$. The dominant positive contribution to the obstruction, that is $F(\varepsilon)$, comes from either the complex structure change (between $X$ and $L$ ), or cutting off the $\omega_{\mathrm{TY}}$, or both. The dominant negative contribution to the obstruction, that is $-\left(\beta-\beta_{*}\right)$, comes from cutting off $\omega_{\beta, L}$ and its particular shape is due to the "Green's function like" term $\frac{\beta-\beta_{*}}{r^{2 n-2}}$ in the expansion of $\phi_{\beta, L}$.

Ensuring that $F(\varepsilon)$ is positive is absolutely crucial since it allows us to fix $\varepsilon$ and deform the cone angle as $\beta=\beta_{*}+F(\varepsilon)+\gamma$ where l.o.t. $\ll|\gamma| \ll F(\varepsilon)$ will vary to ensure that $a(\beta, \varepsilon)$ takes positive and negative values hence vanishes for some value $\beta=\beta(\varepsilon)$. For technical reasons, we will actually fix $\beta$ and vary $\varepsilon$ to the same effect, in order to circumvent the troubles due to the functional spaces changing as $\beta$ varies.

The computation of $F(\varepsilon)$ relies on two things : (i) the (delicate) construction of a tubular neighborhood of $D$ where the difference between the holomorphic volume forms on $L$ and $X$ has a sign and (ii) the computation of the sub-leading term and its sign in the asymptotic expansion of the Tian-Yau potential. This result (Theorem 6.1) may be of independent interest.
1.4. Comparison with [BG22]. In the paper [BG22], we had previously treated the case where $\alpha=1$ and we would like to briefly single out the main differences between the techniques involved in that paper and in the present one.

In [BG22], the main difficulties stemmed from the collapsing of the $\mathrm{KE}_{\beta}$ metrics at stake coupled with the fact that the cone angle $\beta$ goes to zero; that made the Schauder estimates extremely delicate to establish. The MA equation was obstructed as well (again because of the radial vector field in the normal
bundle) but killing the obstruction with the cone angle turned out to be rather easy.

In our present situation, there is no collapsing and $\beta$ remains bounded away from 0 and 1. However, the Calabi Ansatz is much trickier to analyse since we cannot use a scaling argument anymore. More importantly, it is much harder to kill the obstruction as it relies on a very fine understanding of the geometry of the pair $(X, D)$ and its associated canonical KE metrics, as we have explained in the previous paragraph.

Acknowledgements. The authors are grateful to Hajo Hein for the many enlightening conversations about this problem, and to Thibaut Delcroix for insightful discussions and explaining Example 4.3 to us. We would also like to thank the referee for helping improve the exposition of the article. H.G. is partially supported by the French Agence Nationale de la Recherche (ANR) under reference ANR-21-CE40-0010 (KARMAPOLIS).

\section*{2. Geometric setup}

Let $X$ be a Fano manifold of dimension $n \geqslant 2$, and let $D$ be a smooth divisor such that
\begin{itemize}
\item[-] $-K_{X} \sim_{Q} \alpha D$ for some rational number $\alpha>1$.
\item[-] $D$ admits a Kähler-Einstein metrics $\omega_{D}$; i.e. Ric $\omega_{D}=\omega_{D}$.
\end{itemize}

Recall that the identify $-K_{X} \sim_{\mathbb{Q}} \alpha D$ means that there exists an integer $m \geqslant 1$ such that $m \alpha \in \mathbb{N}$ and that the line bundles $K_{X}^{\otimes m}$ and $\mathcal{O}_{X}(-m \alpha D)$ are isomorphic.

Let us observe that $\alpha \leqslant n+1$. Indeed, by Mori's bend and break, there is always a (rational) curve $C$ such that $\left(-K_{X} \cdot C\right) \leqslant n+1$. In particular, this implies that $\alpha \leqslant \frac{n+1}{(D \cdot C)} \leqslant n+1$. By Kobayashi-Ochiai, equality occurs if and only if $X=\mathbb{P}^{n}$ and $D$ is an hyperplane. The latter case is irrelevant for our purposes, so we will assume that $\alpha<n+1$ in the following.
2.1. Deformation to the normal cone $\bar{L}$. Let $L:=N_{D}$ be the normal bundle of $D$, which is an ample divisor and set $v$ to be the fiber coordinate so that $L=$ $\left\{(x, v) ; x \in D, v \in L_{x}\right\}$. We consider the hermitian metric $h$ on $L$ (unique up to a multiplicative constant) such that $i \Theta(L, h)=\frac{1}{\alpha-1} \omega_{D}$.

Next let $\bar{L}$ be the one-point compactification of $L$; it can be endowed with a structure of normal projective variety in two equivalent ways. First, one can consider the affine cone $C\left(D, L^{-1}\right)$ obtained e.g. as the contraction of the zero section in the total space of the negative bundle $L^{-1}$ and define $\bar{L}$ to be the projectivization of $C\left(D, L^{-1}\right)$. Or we can view $\bar{L}$ as the blow-down of $\mathbb{P}\left(N_{D}\right) \subset$
$\mathbb{P}\left(N_{D} \oplus \mathcal{O}_{D}\right)$. It is a classical fact that $\bar{L}$ can be achieved as the central fiber of a $\mathbb{C}^{*}$ degeneration of $X$ using the so-called degeneration to the normal cone. We recall the construction below.

Consider the family $\mathfrak{X}:=\mathrm{Bl}_{D \times\{0\}}(X \times \mathbb{C}) \rightarrow \mathbb{C}$. The fibers $\mathfrak{X}_{t}$ for $t \neq 0$ are isomorphic to $X$ while $\mathfrak{X}_{0}=\mathrm{Bl}_{D} X \cup \mathbb{P}\left(N_{D} \oplus \mathcal{O}_{D}\right) \simeq X \cup \mathbb{P}\left(N_{D} \oplus \mathcal{O}_{D}\right)$ and the two $n$-dimensional varieties meet along $D$ and $\mathbb{P}\left(N_{D} \oplus 0\right) \simeq \mathbb{P}\left(N_{D}\right)$, the section at infinity. One can contract $\mathrm{Bl}_{D} X \subset \mathfrak{X}$ via a map $\mathfrak{X} \rightarrow \mathcal{X}$; the resulting map is called $\pi: \mathcal{X} \rightarrow \mathbb{C}$. Its fibers outside the origin are isomorphic to $X$ and identified via a $\mathbb{C}^{*}$ action that lifts from $\mathbb{C}$, while the central fiber is the projective cone $\mathbb{P}\left(N_{D} \oplus \mathcal{O}_{D}\right)$ with the section at infinity contracted to a point, or said otherwise it is the one-point compactification $\bar{L}$ of $N_{D}$ mentioned above, cf e.g. [Li20, § 4.1] combined with the fact that for $m \geqslant 0$, one has $H^{1}(X, m D)=$ $H^{1}\left(X, K_{X}+\left(-K_{X}+m D\right)\right)=0$ by Kodaira vanishing since $-K_{X}+m D$ is ample.

On the singular cone $\bar{L}$, the Calabi-Ansatz enables to construct a $\mathrm{KE}_{\beta_{*}}$ metric
$$\omega_{\beta_{*}, L}:=d d^{c} \log \left(1+|v|_{h}^{-2 \beta_{*}}\right),$$
cf (3.24). The metric is smooth and satisfies Ric $\omega_{\beta_{*}, L}=\omega_{\beta_{*}, L}$ on $L \backslash D$, has cone singularities of angle $2 \pi \beta_{*}$ along $D \subset L$ and it is asymptotic to the Tian-Yau cone metric $\omega_{\mathrm{TY}, L}=d d^{c}|v|^{-2 \beta_{*}}$ near the conical point. The existence of $\omega_{\beta_{*}, L}$ has important consequences as we now explain.
2.2. Smallest possible cone angle. For a given value $\beta \in(0,1)$, we consider the Kähler-Einstein equation
$$\operatorname{Ric} \omega_{\beta}=\mu \omega_{\beta}+(1-\beta)[D]$$
where $\mu=\mu(\beta)>0$ is given by $\mu \alpha=\alpha+\beta-1$, so that $\omega_{\beta} \in c_{1}(X)=\alpha c_{1}(D)$ is fixed, independent of $\beta$. Consider the interval
$$I:=\left\{\beta \in(0,1] ; \exists \omega_{\beta} \text { solution of }\left(\mathrm{KE}_{\beta}\right)\right\} .$$
Recall that if $\operatorname{Aut}^{\circ}(X, D)=\{1\}$, then $I$ is open by [Don12]. Actually, much more can be said even without the assumption on holomorphic vector fields.
Proposition 2.1 ([LS14]). There exists $\beta^{*} \in(0,1]$ such that
$$I=\varnothing,\left(\beta_{*}, \beta^{*}\right) \text { or }\left(\beta_{*}, \beta^{*}\right]$$
where $\beta_{*}$ is defined in (1.2).

Sketch of proof. There are three main steps which we sketch below.
Step 1.
The existence of the $\mathrm{KE}_{\beta}$ metric $\omega_{\beta_{*}, L}$ on the central fiber of a non-trivial test configuration shows that $\beta_{*} \notin I$. Actually, one can show $I \subset\left(\beta_{*}, 1\right)$. One way to do is it to directly compute the Futaki invariant of $(X,(1-\beta) D)$ associated to that test configuration [LS14] and show that when $\beta \leqslant \beta_{*}$, it has the "wrong" sign. Alternatively, one can use Fujita valuative criterion [Fuj16] with respect to the prime divisor $D$, and polarization $L=-\left(K_{X}+(1-\beta) D\right)=-\mu K_{X}$ with $\mu=\frac{1}{\alpha}(\alpha-1+\beta)$. Then, one has $A_{(X,(1-\beta) D)}(D):=1+\operatorname{ord}_{D}\left(K_{X}-\left(K_{X}+(1-\right.\right.$ $\beta) D))=\beta$ and $\operatorname{vol}(L-x D)=\left(\mu-\frac{x}{\alpha}\right)^{n}\left(-K_{X}^{n}\right)$, hence the $\beta$ invariant
$$\beta(D)=A_{(X,(1-\beta) D)}(D) \cdot\left(L^{n}\right)-\int_{0}^{+\infty} \operatorname{vol}(L-x D) d x$$
satisfies $\beta(D)=\mu^{n}\left(-K_{X}^{n}\right)\left[\beta-\frac{\mu \alpha}{n+1}\right]=\frac{n}{n+1} \mu^{n}\left(-K_{X}^{n}\right)\left[\beta-\beta_{*}\right]$. In particular, $\beta(D) \geqslant 0$ if and only if $\beta \geqslant \beta_{*}$.

Step 2.
The Ding functional $F_{\beta}$ for $(X,(1-\beta) D)$ is bounded below for $\beta=\beta_{*}$ by a classical argument relying on convexity of Mabuchi along (weak) geodesics [LS14].

Step 3.
The functional $F_{\beta}$ is affine in $\beta$ and existence of a $\mathrm{KE}_{\beta}$ metric is equivalent to a suitable notion of properness by [DR17]. Hence the existence of a $\mathrm{KE}_{\beta_{0}}$ metric implies properness for all $\beta \in\left(\beta_{*}, \beta_{0}\right]$, hence the existence of a $\mathrm{KE}_{\beta}$ metric for each of these angles. That is, $I$ is connected and $\inf I \in\left\{\beta_{*},+\infty\right\}$. \(\square\)
2.3. Rigidity of $\omega_{\beta_{*}, L}$. The aim of this short paragraph is to explain that the cone angle $2 \pi \beta_{*}$ is the only one for which $(\bar{L}, D)$ admits a Kähler-Einstein cone metric. The rigidity is related to the existence of holomorphic vector field tangent to $D$ (namely, the radial vector field induced by the $\mathbb{C}^{*}$ action), since in the absence of such vector fields, the set of possible cone angles is open [Don12]. Such a rigidity phenomenon had already been observed for surfaces in [CR18, Example 2.8].

Proposition 2.2. The pair $(\bar{L}, D)$ admits a $\mathrm{KE}_{\beta}$ metric if, and only if $\beta=\beta_{*}$.
We provide below only a rough sketch of proof based on the computation of the log Futaki invariant associated to the radial vector field $\xi$. Note that Proposition 2.2 is also a direct consequence of the main theorem (i.e. the existence of $\mathrm{KE}_{\beta}$ metrics on $(X, D)$ for $\beta \in\left(\beta_{*}, \beta_{*}+\delta\right)$ ) and the non-existence of $\mathrm{KE}_{\beta}$ metrics on ( $X, D$ ) for $\beta \leqslant \beta_{*}$, cf Proposition 2.1.

Proof. We claim that there exists on $L$ a Kähler metric $\omega:=d d^{c} \varphi(u)$ with $u=$ $\log |v|_{h}^{2}$ such that the following properties are met
\begin{itemize}
\item[(i)] $\varphi$ is nonincreasing, convex and coincides with $-u+e^{u}$ near $-\infty$ and $e^{-u}$ near $+\infty$.
\item[(ii)] $\varphi^{\prime}$ is a potential for $\xi$, i.e. $i_{\xi} \omega=\bar{\partial} \varphi^{\prime}$.
\end{itemize}
Indeed, with the help of a drawing one can easily convince oneself that such a function $\varphi$ exists. It induces a Kähler metric on $L$ thanks to the Calabi Ansatz, cf (3.4) below, and the metric actually extends smoothly to a Kähler metric on the singular cone $\bar{L}$. The second item is also a direct consequence of (3.4) and the identity $\bar{\partial} \varphi^{\prime}=\varphi^{\prime \prime} \bar{\partial} u$.

The two properties above imply that $f:=-\varphi^{\prime} \geqslant 0$ is identically 1 on $D$ and decreases with $u$. Moreover, we have $\omega=\varphi^{\prime \prime}(u) d u \wedge d^{c} u+\left.p^{*} \omega\right|_{D}$ hence we deduce
$$\begin{aligned}
\frac{1}{\operatorname{vol}(\bar{L}, \omega)} \int_{\bar{L}} f \frac{\omega^{n}}{n!} & =\frac{1}{\operatorname{vol}(\bar{L}, \omega)} \int_{-\infty}^{+\infty} f(u) \varphi^{\prime \prime}(u) d u \wedge d^{c} u \int_{D} \frac{\omega^{n-1}}{(n-1)!} \\
& <\frac{1}{\operatorname{vol}(\bar{L}, \omega)} \int_{-\infty}^{+\infty} \varphi^{\prime \prime}(u) d u \wedge d^{c} u \int_{D} \frac{\omega^{n-1}}{(n-1)!} \\
& =1 \\
& =\frac{1}{\operatorname{vol}(D, \omega)} \int_{D} f \frac{\omega^{n-1}}{(n-1)!}
\end{aligned}$$
Thanks to (the singular version of) [Has19], the log Futaki invariant associated to $(\bar{L}, D, \beta,-\xi, f)$ satisfies
$$\operatorname{Fut}_{\xi, \beta}([\omega])=\operatorname{Fut}_{\xi, 1}([\omega])-a(1-\beta)$$
for some constant $a>0$. In particular, there is at most one value of $\beta$ such that the Futaki invariant vanishes, i.e. $\operatorname{Fut}_{\xi, \beta}([\omega])=0$. Of course, this is none other than $\beta=\beta_{*}$. The proposition follows. \(\square\)

\section*{3. Conic Calabi Ansatz: construction and asymptotics}

In this section, we rely on the Calabi Ansatz to construct (possibly incomplete) $\mathrm{KE}_{\beta}$ metrics $\omega_{\beta, L}$ on the normal bundle $L$ (with cone singularities along the zero section $D \subset L$ ) for each angle $\beta \in(0,1)$ - the value $\beta=\beta_{*}$ being critical. We then analyze their asymptotic behavior as $\beta \searrow \beta_{*}$.
3.1. Reduction to an ODE. Let us record notations that will be used throughout the section

\begin{tabular}[t]{|l|l|l|}
\hline $$\begin{aligned}
& \beta_{*}=\frac{\alpha-1}{n} \\
& \mu=\frac{1}{\alpha}(\alpha+\beta-1) \\
& \lambda=\frac{\alpha-1}{\mu}
\end{aligned}$$ & $$\begin{aligned}
& a=\frac{\mu}{n+1} \\
& b=\beta_{*}=\frac{\alpha-1}{n} \\
& \psi=-\phi-\lambda u
\end{aligned}$$ & $C_{\beta}=\frac{\alpha^{n}}{n+1}\left(\beta-\beta_{*}\right)$ \\
\hline
\end{tabular}

The the last constant $C_{\beta}$ is recorded here for clarity but it will only be determined a few lines below.

On $L=N_{D}$, we want to solve
$$\operatorname{Ric} \omega_{\beta}=\mu \omega_{\beta}+(1-\beta)[D]$$
with
\begin{itemize}
\item[(i)] $\omega_{\beta}=d d^{c} \phi(u)$ where $u=\log |v|_{h}^{2}$, and $h$ is a smooth hermitian metric on $L$ such that $i \Theta(L, h)=\frac{1}{\alpha-1} \omega_{D}$.
\item[(ii)] $\omega_{\beta}$ has conic singularities with cone angle $2 \pi \beta$ along $D$.
\item[(iii)] $\phi(u) \sim-\alpha u$ when $u \rightarrow-\infty$.
\end{itemize}

The last condition just means that the current $\left.\omega_{\beta}\right|_{D}$ belongs to $\left.\alpha c_{1}(D)\right|_{D}$. It is an arbitrary normalization that imposes the value of the Einstein constant to satisfy
$$\mu \alpha=\alpha+\beta-1 .$$
The fact that $\omega_{\beta}$ is a metric is equivalent to having
$$-\phi^{\prime}>0, \quad \phi^{\prime \prime}>0 .$$
It is easy to check that
$$\Xi:=e^{-(\alpha-1) u} d u \wedge d^{c} u \wedge \omega_{D}^{n-1}$$
defines a Ricci flat volume form on $L$ with a pole of order $\alpha$ along the zero section. The metric
$$\omega_{\beta}=d d^{c} \phi(u)=\phi^{\prime \prime}(u) d u \wedge d^{c} u-\frac{2}{\alpha-1} \phi^{\prime}(u) \omega_{D}$$
satisfies
$$\omega_{\beta}^{n}=a_{n, \alpha} \phi^{\prime \prime}(u)\left(-\phi^{\prime}(u)\right)^{n-1} d u \wedge d^{c} u \wedge \omega_{D}^{n-1}, \quad a_{n, \alpha}=\frac{2^{n-1} n}{(\alpha-1)^{n-1}} .$$

Therefore $\omega_{\beta}$ is a solution of
$$\omega_{\beta}^{n}=a_{n, \alpha} e^{-\mu \phi}{ }_{\Xi},$$
and therefore a solution of (3.1), if $\phi$ solves
$$\left(-\phi^{\prime}\right)^{n-1} \phi^{\prime \prime}=e^{-\mu \phi-(\alpha-1) u} .$$
Multiplying each side by $-\mu \phi^{\prime}-(\alpha-1)$ and integrating, we get
$$\left(-\phi^{\prime}\right)^{n}\left(b+a \phi^{\prime}\right)=e^{-\mu(\phi+\lambda u)}-C_{\beta}$$
for some constant $C_{\beta}$ to determine.
By setting $\psi:=-\phi-\lambda u$, we get the equivalent autonomous equation
$$\left(\psi^{\prime}+\lambda\right)^{n}\left(b-a\left(\psi^{\prime}+\lambda\right)\right)=e^{\mu \psi}-C_{\beta}$$

In order to choose the right constant $C_{\beta}$, let us remember that when $u \rightarrow$ $-\infty$, we want our solution $\psi$ to satisfy $\psi(u) \sim(\alpha-\lambda) u=\frac{\beta}{\mu} u$, so that $\psi^{\prime}+\lambda \sim \alpha$. Therefore we want the constant $C_{\beta}$ to satisfy
$$\alpha^{n}(b-a \alpha)=\frac{\alpha^{n}}{n+1}\left(\frac{\alpha-1}{n}-\beta\right)=-C_{\beta} .$$
From now on, we impose the constant $C_{\beta}$ from (3.9) to be given by the equation (3.10) above, i.e.
$$C_{\beta}=\frac{\alpha^{n}}{n+1} \cdot\left(\beta-\beta_{*}\right) .$$
Observe that
$$C_{\beta_{*}=0} \quad \text { and } C_{\beta}>0 \text { for } \beta>\beta_{*} .$$
In the sections that follow, we investigate the existence and the behavior of solutions of (3.9).

From now on, we will assume that $\beta>\beta_{*}$ until the end of section 3 with the exception of section 3.5.
3.2. Construction of $\psi$ near $-\infty$. In order for the problem to be well posed, we fix the initial value $\psi\left(\hat{u}_{0}\right)=\hat{\psi}_{0}$ for some couple $\left(\hat{u}_{0}, \hat{\psi}_{0}\right)$ that will be determined later.

Let $F(t)=t^{n}(b-a t)$, defined on $[0, \alpha]$.
![](https://cdn.mathpix.com/cropped/ba0b4a59-2b1b-4998-859c-b58cf6bb6861-14.jpg?height=267&width=705&top_left_y=578&top_left_x=680)
We have $F(0)=0, F(\alpha) \leqslant 0$ with equality if and only if $\beta=\beta_{*}$. $F$ is increasing up until $t=\lambda$, and then decreasing. The value
$$F(\lambda)=\frac{\beta_{*} \lambda^{n}}{n+1}>0$$
is explicit but does not play any role. $F$ admits two inverses
$$G_{1}:[0, F(\lambda)] \rightarrow[0, \lambda] \quad \text { and } \quad G_{2}:\left[F(\alpha)=-C_{\beta}, F(\lambda)\right] \rightarrow[\lambda, \alpha] .$$
The equation (3.9) can be reformulated as
$$F\left(\psi^{\prime}+\lambda\right)=e^{\mu \psi}-C_{\beta}$$
which can be expressed as $\psi^{\prime}=G_{i}\left(e^{\mu \psi}-C_{\beta}\right)-\lambda$, i.e.
$$\frac{d \psi}{G_{i}\left(e^{\mu \psi}-C_{\beta}\right)-\lambda}=d u$$
for either $i=1,2$. Note that neither function $G_{i}$ is differentiable at the nexus point $F(\lambda)$.

The equation
$$\int_{\hat{\psi}_{0}}^{\psi} \frac{d x}{G_{2}\left(e^{\mu x}-C_{\beta}\right)-\lambda}=u-\hat{u}_{0}$$
uniquely defines a function $\psi=\psi(u)$ on a neighborhood of $u=\hat{u}_{0}$ solving (3.12). Here, we need $\hat{\psi}_{0} \ll 0$ to make sure that $e^{\mu \hat{\psi}_{0}} \in(F(\alpha), F(\lambda))$ so that $G_{2}\left(e^{\mu x}-C_{\beta}\right)$ is well-defined near $x=\hat{\psi}_{0}$. Let us define
$$\psi_{0}:=\frac{1}{\mu} \log \left(F(\lambda)+C_{\beta}\right), \quad \text { i.e. } \quad e^{\mu \psi_{0}}-C_{\beta}=F(\lambda) .$$

Since $G_{2} \geqslant \lambda, \psi$ is non-decreasing. Clearly, $\psi$ reaches any value less than $\psi_{0}$. Moreover, we claim that $\psi(u)$ is defined for any negative values of $u$. This follows from the fact that the integral
$$\int_{\hat{\psi}_{0}}^{-\infty} \frac{d x}{G_{2}\left(e^{\mu x}-C_{\beta}\right)-\lambda}=-\infty$$
diverges. Indeed, $G_{2}\left(e^{\mu x}-C_{\beta}\right) \underset{x \rightarrow-\infty}{\sim} \alpha$ and $\alpha>\lambda$. In particular, one has $\psi(u) \rightarrow$ $-\infty$ when $u \rightarrow-\infty$. One can actually say more. Indeed, $G_{2}\left(-C_{\beta}+s\right)=\alpha+$ $\frac{s}{F^{\prime}(\alpha)}+O\left(s^{2}\right)$ when $s \rightarrow 0^{+}$. Equivalently, one finds $G_{2}\left(e^{\mu x}-C_{\beta}\right)-\lambda=(\alpha-$ $\lambda)+\frac{e^{\mu x}}{F^{\prime}(\alpha)}+O\left(e^{2 \mu x}\right)$ when $x \rightarrow-\infty$. Expanding the integral defining $\psi$, one finds near $u=-\infty$ :
$$\psi(u)=(\alpha-\lambda)\left(u-\hat{u}_{0}\right)+\hat{\psi}_{0}+\frac{\alpha-\lambda}{F^{\prime}(\alpha)} e^{\mu \psi}+O\left(e^{2 \mu \psi}\right) .$$
Writing $\alpha-\lambda=\frac{\beta}{\mu}$, one infers that
$$\phi(u)=-\alpha u+u_{\infty}-\frac{\beta}{\mu F^{\prime}(\alpha)} e^{\beta u}+O\left(e^{2 \beta u}\right)$$
when $u \rightarrow-\infty$, for some $u_{\infty} \in \mathbb{R}$. Since $F^{\prime}(\alpha)=-\beta \alpha^{n-1}<0, \phi$ satisfies the requirements (3.2) at least near $-\infty$ and $d d^{c} \phi(u)$ has indeed a cone singularity of angle $2 \pi \beta$ along $D=(u=-\infty)$. Moreover, thanks to (3.8), we obtain the following expansions for $\phi^{\prime}$ and $\phi^{\prime \prime}$ :
$$\phi^{\prime}(u)=-\alpha+c_{1} e^{\beta u}+O\left(e^{2 \beta u}\right), \quad \phi^{\prime \prime}(u)=c_{2} e^{\beta u}+O\left(e^{2 \beta u}\right),$$
where $c_{1}=-\frac{\beta^{2}}{\mu F^{\prime}(\alpha)}$ and $c_{2}=\beta c_{1}$.
3.3. Extension of $\psi$ past $\psi_{0}$. We are going to show that $\psi$ can be smoothly extended past the value $\psi_{0}$ defined in (3.15). First, we claim that the integral
$$\int_{\hat{\psi}_{0}}^{\psi_{0}} \frac{d x}{G_{2}\left(e^{\mu x}-C_{\beta}\right)-\lambda}$$
is convergent. Indeed, perform the change of variable $s:=e^{\mu x}-C_{\beta}$ and set $\hat{s}_{0}:=e^{\mu \hat{\psi}_{0}}-C_{\beta}$ so that our integral becomes
$$\frac{1}{\mu} \int_{\hat{s}_{0}}^{F(\lambda)} \frac{d s}{\left(G_{2}(s)-\lambda\right)\left(s+C_{\beta}\right)}=\frac{1}{\mu} \int_{\lambda}^{G\left(\hat{s}_{0}\right)} \frac{-F^{\prime}(t) d t}{(t-\lambda)\left(F(t)+C_{\beta}\right)}$$
where we have used another change of variable $t=G(s)$ to obtain the RHS. Now an easy computation shows that $F^{\prime}(t)=\mu t^{n-1}(\lambda-t)$ and the integral becomes $\int_{\lambda}^{G\left(\hat{s}_{0}\right)} \frac{t^{n-1} d t}{F(t)+C_{\beta}}$ which is obviously convergent. Now, the identity
$$\int_{\psi_{0}}^{\psi} \frac{d x}{G_{2}\left(e^{\mu x}-C_{\beta}\right)-\lambda}=u-u_{0}$$
shows that $\psi$ is defined on $\left(-\infty, u_{0}\right)$ and satisfies $\psi(u) \rightarrow \psi_{0}$ when $u \rightarrow u_{0}$. We set
$$u_{0}:=\hat{u}_{0}+\int_{\hat{\psi}_{0}}^{\psi_{0}} \frac{d x}{G_{2}\left(e^{\mu x}-C_{\beta}\right)-\lambda}=\hat{u}_{0}+\int_{\lambda}^{G\left(\hat{s}_{0}\right)} \frac{t^{n-1} d t}{F(t)+C_{\beta}} .$$
By the same arguments, one see that the integral
$$\int_{\psi_{0}}^{\psi} \frac{d x}{G_{1}\left(e^{\mu x}-C_{\beta}\right)-\lambda}$$
is convergent, hence
$$\int_{\psi_{0}}^{\psi} \frac{d x}{G_{1}\left(e^{\mu x}-C_{\beta}\right)-\lambda}=u-u_{0}$$
defines an extension of $\psi$ for $u>u_{0}$ close enough to $u_{0}$ which is continuous across $u_{0}$ and satisfies
$$\psi(u) \underset{u \rightarrow u_{0}}{\longrightarrow} \psi_{0}, \quad \psi^{\prime}(u) \underset{u \rightarrow u_{0}}{\longrightarrow} 0 .$$
Let us now show that $\psi$ is smooth at $u_{0}$. Differentiating (3.12) we get $\psi^{\prime \prime} F^{\prime}\left(\psi^{\prime}+\right.$ $\lambda)=\mu \psi^{\prime} e^{\mu \psi}$ away from $u_{0}$. Since $F^{\prime}(t)=-\mu t^{n-1}(t-\lambda)$, this implies that
$$\psi^{\prime \prime}=-\frac{e^{\mu \psi}}{\left(\psi^{\prime}+\lambda\right)^{n-1}}$$
which converges to the value $\frac{e^{\mu \psi_{0}}}{\lambda^{n-1}}$ when $u \rightarrow u_{0}$. In particular, $\psi$ is $C^{2}$ near $u_{0}$. We get smoothness iteratively thanks to (3.20).

Finally, since $G_{1} \leqslant \lambda, \psi$ is non-increasing after $u_{0}$. The expression (3.19) yields a function $\psi$ satisfying $\psi \geqslant \psi_{\beta}$ for $\psi_{\beta} \in \mathbb{R}$ which is a solution of
$$e^{\mu \psi_{\beta}}=C_{\beta} .$$

We refer to Figure 3.1 below for the qualitative behavior of $\psi$.
We can actually provide an integral expression (or relation) for $\psi$ which does not involve $u_{0}$. Indeed, from (3.18), one get
$$\begin{aligned}
\lambda\left(u_{0}-\hat{u}_{0}\right) & =\hat{\psi}_{0}-\psi_{0}+\int_{\hat{\psi}_{0}}^{\psi_{0}} \frac{G_{2}\left(e^{\mu x}-C_{\beta}\right) d x}{G_{2}\left(e^{\mu x}-C_{\beta}\right)-\lambda} \\
& =\hat{\psi}_{0}-\psi_{0}+\int_{\lambda}^{G_{2}\left(\hat{s}_{0}\right)} \frac{t^{n} d t}{F(t)+C_{\beta}}
\end{aligned}$$
and similarly, one gets from (3.19)
$$\lambda\left(u-u_{0}\right)=\psi_{0}-\psi+\int_{G_{1}(s(\psi))}^{\lambda} \frac{t^{n} d t}{F(t)+C_{\beta}} .$$
Adding the latter identities, we get
$$\phi\left(\hat{u}_{0}\right)-\phi(u)=\int_{G_{1}(s(\psi))}^{G_{2}\left(\hat{s}_{0}\right)} \frac{t^{n} d t}{F(t)+C_{\beta}}$$
where $s(\psi)=e^{\mu \psi}-C_{\beta}$. Recall that by construction, we have $\phi\left(\hat{u}_{0}\right)=-\hat{\psi}_{0}-\lambda \hat{u}_{0}$, and that $\hat{\psi}_{0}$ is constrained to $\hat{s}_{0}=s\left(\hat{\psi}_{0}\right) \in(F(\alpha), F(\lambda))$ where $s(x)=e^{\mu \hat{x}}-C_{\beta}$. We fix such a $\hat{\psi}_{0}$ once and for all. At this point, $\hat{u}_{0}$ is arbitrary, but from now on we will choose $\hat{u}_{0}$ so that
$$\hat{\psi}_{0}+\lambda \hat{u}_{0}+\int_{0}^{G_{2}\left(\hat{s}_{0}\right)} \frac{t^{n} d t}{F(t)+C_{\beta}}=0$$
As a result, we obtain from (3.21) the relation
$$\phi(u)=\int_{0}^{G_{1}(s(\psi))} \frac{t^{n} d t}{F(t)+C_{\beta}} .$$
3.4. Long time existence of $\psi$. There are two cases to consider depending on the sign of $C_{\beta}$.
\begin{itemize}
\item[-] If $C_{\beta}>0$ (i.e. $\beta>\beta_{*}$ ), the integral
$$\int_{\psi_{0}}^{\psi_{\beta}} \frac{d x}{G_{1}\left(e^{\mu x}-C_{\beta}\right)-\lambda}=\int_{0}^{\lambda} \frac{t^{n-1} d t}{F(t)+C_{\beta}}$$
\end{itemize}
is convergent. In other words, there exists a finite time $u_{\beta}$ such that $\psi\left(u_{\beta}\right)=\psi_{\beta}$. In particular, $d d^{c} \phi$ cannot be extended as a metric past $u_{\beta}$. Moreover, the previous integral goes to $+\infty$ as $\beta \rightarrow \beta_{*}$ which shows that $u_{\beta} \rightarrow+\infty$ when $\beta \rightarrow \beta_{*}$.
- If $C_{\beta}=0$ (i.e. $\beta=\beta_{*}$ ), then $\psi$ is defined for all times and $\psi(u) \xrightarrow[u \rightarrow+\infty]{ }-\infty$ since
$$\int_{\psi_{0}}^{-\infty} \frac{d x}{G_{1}\left(e^{\mu x}\right)-\lambda}=\int_{0}^{\lambda} \frac{d t}{t(b-a t)}=+\infty$$
is divergent and $\int_{\psi_{0}}^{\psi_{2}} \frac{d x}{G_{1}\left(e^{\mu x}\right)-\lambda}<+\infty$ is finite for any finite $\psi_{2}<\psi_{0}$. One can easily get from (3.21) the successive asymptotics $\psi(u)=-\lambda u+C_{1}+o(1)$ and then $\psi(u)=-\lambda u+C_{1}-C_{2} e^{-\frac{\lambda \mu}{n} u}+O\left(e^{-\frac{2 \lambda \mu}{n} u}\right)$ when $u \rightarrow+\infty$, for some $C_{2}>0$. In terms of $\phi$, we get
$$\phi(u)=-C_{1}+C_{2} e^{-\beta_{*} u}+O\left(e^{-2 \beta_{*} u}\right),$$
where we have used that $\frac{\lambda \mu}{n}=\beta_{*}$.
One can actually recover the qualitative behavior of $\phi_{\beta_{*}}$ from an explicit formula. Indeed, $\phi:=\phi_{\beta_{*}}$ is a solution of $\phi^{\prime \prime}=-\phi^{\prime}\left(1+\frac{\phi^{\prime}}{\alpha}\right) \beta_{*}$ which can be integrated in
$$\begin{aligned}
\phi_{\beta_{*}}(u) & =c_{0}-\alpha u+\frac{\alpha}{\beta_{*}} \log \left(1+c_{1} e^{\beta_{*} u}\right) \\
& =c_{2}+\frac{\alpha}{\beta_{*}} \log \left(1+c_{1}^{-1} e^{-\beta_{*} u}\right)
\end{aligned}$$
where $c_{0}, c_{2} \in \mathbb{R}$ and $c_{1}>0$ are constant.
3.5. Analysis of the case $\beta<\beta_{*}$. Again, we fix the initial values ( $\hat{u}_{0}, \hat{\psi}_{0}$ ) such that $e^{\mu \hat{\psi}_{0}} \in(F(\alpha), F(\lambda))$. Under the assumption that $\beta<\beta_{*}$, we have $C_{\beta}<0$ hence the graph of $F$ has the shape below.
![](https://cdn.mathpix.com/cropped/ba0b4a59-2b1b-4998-859c-b58cf6bb6861-18.jpg?height=270&width=719&top_left_y=1820&top_left_x=673)
Here we have set $\gamma:=G_{1}(F(\alpha))=G_{1}\left(-C_{\beta}\right)$. We can construct a solution $\psi$ near $u_{0}$ solving $\psi\left(\hat{u}_{0}\right)=\hat{\psi}_{0}$.
Claim 3.1. The solution $\psi=\psi(u)$ is defined for all $u \in(-\infty,+\infty)$.

Proof. The existence of $\psi(u)$ for $u$ near $-\infty$ is justified by the divergence of the integral $\int_{-\infty}^{\hat{\psi}_{0}} \frac{d x}{G_{2}\left(e^{\mu x}-C_{\beta}\right)-\lambda}$ which is clear since $G_{2}\left(e^{\mu x}-C_{\beta}\right) \rightarrow \alpha$ when $x \rightarrow-\infty$. As in the case $\beta>\beta_{0}$, one see that there is a value $u_{0}$ such that $\psi(u) \rightarrow \psi_{0}$ when $u \nearrow u_{0}$ where $e^{\mu \psi_{0}}-C_{\beta}=F(\lambda)$, and that $\psi$ can be extended smoothly past $u_{0}$. The existence of $\psi(u)$ for $u$ near $+\infty$ is justified by the divergence of the integral $\int_{-\infty}^{\psi_{0}} \frac{d x}{G_{1}\left(e^{\mu x}-C_{\beta}\right)-\lambda}$ which in turn is a consequence of $G_{1}\left(e^{\mu x}-C_{\beta}\right) \rightarrow \gamma \in(0, \lambda)$ when $x \rightarrow-\infty$. \(\square\)

Claim 3.2. The KE metric $\omega_{\beta}=d d^{c} \phi_{\beta}$ extends to a metric on the compactification $\mathbb{P}\left(L \oplus \mathcal{O}_{D}\right)$ with cone singularities along both $D$ and $D_{\infty}$. The cone angle along $D$ is $2 \pi \beta$ and the cone angle along $D_{\infty}$ is $2 \pi \mu(\lambda-\gamma)$ which ranges in $(0,2 \pi(\alpha-1))$ as $\beta$ ranges in ( $0, \beta_{*}$ ).

Proof. Let us start with the behavior near $u=-\infty$. One writes $G_{2}\left(e^{\mu x}-C_{\beta}\right)=$ $\alpha-c e^{\mu x}+O\left(e^{2 \mu x}\right)$ with $c>0$. Plugging that in the identity $\int_{\psi_{0}}^{\psi} \frac{d x}{G_{2}\left(e^{\mu x}-C_{\beta}\right)-\lambda}=$ $u-u_{0}$, we infer iteratively $\psi-\psi_{0} \approx(\alpha-\lambda)\left(u-u_{0}\right)$ and then $\psi-\psi_{0}=(\alpha-$ $\lambda)\left(u-u_{0}\right)-c^{\prime} e^{\beta\left(u-u_{0}\right)}+O\left(e^{2 \beta u}\right)$ when $u \rightarrow-\infty$, where we have used $\alpha-\lambda=$ $\frac{\beta}{\mu}$. This shows that $\phi(u)-\phi\left(u_{0}\right)=-\alpha\left(u-u_{0}\right)+c^{\prime \prime} e^{\beta u}+O\left(e^{2 \beta u}\right)$ with $c^{\prime \prime}>0$, which holds for the derivatives of $\phi$ as well thanks to the MA equation that the latter solves.

Near $u=+\infty$, the analysis is similar but we use instead $G_{1}\left(e^{\mu x}-C_{\beta}\right)=$ $\gamma+c e^{\mu x}+O\left(e^{2 \mu x}\right)$ for some other $c>0$. Then $\psi-\psi_{0} \simeq(\gamma-\lambda)\left(u-u_{0}\right)$ and $\phi(u)-\phi\left(u_{0}\right)=-\gamma\left(u-u_{0}\right)+c^{\prime \prime} e^{-\mu(\lambda-\gamma) u}+O\left(e^{-2 \mu(\lambda-\gamma) u}\right)$ hence the result. \(\square\)

Degenerating $\beta$ to zero. In the remaining part of this section, we will explain how $\omega_{\beta}$ degenerates when $\beta \rightarrow 0$.

We fix $\hat{u}_{0}=0$ and choose any $\hat{\psi}_{0}<\psi_{0}$, which yields a value of $u_{0}$ by (3.18). Replacing $\psi$ by $\psi\left(\cdot+u_{0}\right)$, one can assume wlog that $u_{0}=0$. Since $\alpha-\lambda=\frac{\beta}{\mu} \rightarrow 0$, the values $\gamma$ and $\lambda$ converge to $\alpha$. Moreover, one can check that
$$e^{\mu \psi_{0}}=F(\lambda)+C_{\beta} \sim \frac{\alpha^{n}}{2(\alpha-1)} \cdot \beta^{2} .$$
When coupled with the identity $F(t)=F(\lambda)+\frac{(\lambda-t)^{2}}{2} \cdot F^{\prime \prime}(\lambda)+O\left((\lambda-t)^{3}\right)$ evaluated at $t=\gamma$, we obtain
$$\lambda-\gamma \sim \frac{\alpha}{\alpha-1} \cdot \beta$$
since $F^{\prime \prime}(\lambda)=-\mu \lambda^{n-1} \approx-\mu \alpha^{n-1}$.
- Behavior near D. Let us first focus on what happens near D. For $t \in(\lambda, \alpha)$, one writes $F(t)-F(\alpha)=\alpha^{n-1}(\alpha-t)\left(\beta-\frac{\mu}{2}(\alpha-t)+O\left(\beta^{2}\right)\right)$. Neglecting the $O\left(\beta^{2}\right)$ term, one can solve for $t$ and find $t-\lambda=\frac{\beta}{\mu} \sqrt{1-\frac{2 \mu}{\alpha^{n-1}} \frac{F(t)-F(\alpha)}{\beta^{2}}}$. Setting $t:=$ $G_{2}\left(e^{\mu x}-C_{\beta}\right)$ and using (3.25) this yields $G_{2}\left(e^{\mu x}-C_{\beta}\right)-\lambda \approx \frac{\beta}{\mu} \sqrt{1-e^{\mu\left(x-\psi_{0}\right)}}$ hence
$$\begin{aligned}
-\frac{\beta}{\mu} u & =\int_{\psi-\psi_{0}}^{0} \frac{d x}{\sqrt{1-e^{\mu x}}} \\
& =-\left(\psi-\psi_{0}\right)+c-\frac{1}{2 \mu} e^{\mu\left(\psi-\psi_{0}\right)}+O\left(e^{2 \mu\left(\psi-\psi_{0}\right)}\right)
\end{aligned}$$
where $c>0$ is a positive harmless constant (it might depend on $\beta$ but does not blow up when $\beta \rightarrow 0$ ). In terms of $\phi$, we have
$$\phi_{\beta}(u)=-\psi_{0}-c-\alpha u+\frac{1}{2 \mu} e^{\beta u}+O\left(e^{2 \beta u}\right) .$$
In particular, if one sets $r:=\sqrt{\frac{2}{\mu}} e^{\frac{1}{2} \beta u} \in\left(0, \sqrt{2 \mu^{-1}}\right)$, one sees that near $D$, the Riemannian metric $g_{\beta}$ associated to $\omega_{\beta}$ is asymptotic (uniformly in $\beta$ ) to the Riemannian metric $d r^{2}+\beta^{2} \eta^{2}+\frac{2 \alpha}{\alpha-1} g_{D}$ which collapses the circles. Here, $g_{D}$ is the Riemannian metric associated to $\omega_{D}$.
- Behavior near $D_{\infty}$. Let us now discuss what happens near $D_{\infty}$. Since $F^{\prime}(t)=$ $-\mu t^{n-1}(t-\lambda)$, we derive from (3.26) that $F^{\prime}(\gamma) \sim \frac{\mu \alpha^{n}}{\alpha-1} \beta$ and $F^{\prime \prime}(\gamma) \approx-\mu \alpha^{n-1}$. So for $t \in(\gamma, \lambda)$, one has $F(t)-F(\gamma)=\mu \alpha^{n-1}(t-\gamma)\left(\frac{\alpha}{\alpha-1} \beta-\frac{1}{2}(t-\gamma)+O\left(\beta^{2}\right)\right)$. Neglecting the $O\left(\beta^{2}\right)$ term, one can complete the square and find the relation $t-\lambda=-\frac{\alpha}{\alpha-1} \beta \sqrt{1-\frac{2(\alpha-1)^{2}}{\mu \alpha^{n+1} \beta^{2}} e^{\mu x}}$. Setting $t=G_{1}\left(e^{\mu x}-C_{\beta}\right)$ and using (3.25), this yields $G_{1}\left(e^{\mu x}-C_{\beta}\right)-\lambda \approx-\frac{\alpha}{\alpha-1} \beta \sqrt{1-e^{\mu\left(x-\psi_{0}\right)}}$ hence
$$\begin{aligned}
\frac{\alpha \beta}{\alpha-1} u & =\int_{\psi-\psi_{0}}^{0} \frac{d x}{\sqrt{1-e^{\mu x}}} \\
& =-\left(\psi-\psi_{0}\right)+c-\frac{1}{2 \mu} e^{\mu\left(\psi-\psi_{0}\right)}+O\left(e^{2 \mu\left(\psi-\psi_{0}\right)}\right)
\end{aligned}$$
hence
$$\phi_{\beta}(u)=-\psi_{0}-c-\gamma u+\frac{1}{2 \mu} e^{-\frac{\mu \alpha}{\alpha-1} \beta u}+O\left(e^{-2 \frac{\mu \alpha}{\alpha-1} \beta u}\right)$$
and we conclude similarly to earlier for the case of $D$. The actual expansion has additionnal corrective terms, e.g. the cone singularity has angle $2 \pi \mu(\lambda-\gamma)$ which differs from $2 \pi \mu \frac{\alpha}{\alpha-1} \beta$ by a $O\left(\beta^{2}\right)$.

From the analysis above, one sees that $\omega_{\beta}$ collapses to $\frac{2 \alpha}{\alpha-1} \omega_{D}$ on the interior of $L \backslash D=\mathbb{P}\left(L \oplus \mathcal{O}_{D}\right) \backslash\left(D \cup D_{\infty}\right)$. In conclusion the Gromov-Hausdorff limit of $\left(\mathbb{P}\left(L \oplus \mathcal{O}_{D}\right), g_{\beta}\right)$ is the union of two copies of $\left([0,1] \times D, \frac{2 \alpha}{\alpha-1}\left(d r^{2}+g_{D}\right)\right)$ glued along $(r=1) \simeq D$ or, equivalently, $\left([0,2] \times D, \frac{2 \alpha}{\alpha-1}\left(d r^{2}+g_{D}\right)\right)$.
3.6. Asymptotic expansion of $\phi$ near $+\infty$. Now we want to investigate the behavior of $\phi(u)=\phi_{\beta}(u)$ both as $\beta$ decreases to $\beta_{*}$ and when $u \rightarrow+\infty$.

First, we know that $\psi \rightarrow-\infty$ so that $s(\psi) \rightarrow 0$. Since $F(t) \sim b t^{n}$ when $t \rightarrow$ 0 and $\frac{1}{F(t)+C_{\beta}} \leqslant \frac{1}{F(t)}$, (3.22) tells us that $0 \leqslant \phi(u) \leqslant G_{1}(s(\psi))\left(b^{-1}+o(1)\right)$ which tends to zero. Recall that $G(s) \sim b^{-\frac{1}{n}} s^{\frac{1}{n}}$ and $s(\psi) \leqslant e^{\mu \psi}=e^{-n \beta_{*} u-\mu \phi} \leqslant e^{-n \beta_{*} u}$ since $\phi$ is non-negative. In short, we get
$$\phi(u)=O\left(e^{-\beta_{*} u}\right),$$
where the $O(\cdot)$ is uniform in $\beta$, when $u \rightarrow+\infty$.
Since $\psi(u)=-\lambda u-\phi(u)$, the estimate (3.27) above is already enough to see that the extinction time $u_{\beta}$ of $\psi_{\beta}$ (i.e. when the latter reaches the value $\frac{1}{\mu} \log C_{\beta}$ ) happens when $u_{\beta} \simeq-\frac{1}{\lambda \mu} \log C_{\beta}$, or more precisely
$$u_{\beta}=-\frac{1}{n \beta_{*}} \log C_{\beta}+O\left(C_{\beta}^{\frac{1}{n}}\right) .$$
Therefore we have the following picture
To refine (3.27), we need to further analyze the integral $\phi=\int_{0}^{G_{1}(s(\psi))} \frac{t^{n} d t}{F(t)+C_{\beta}}$ as $s(\psi) \rightarrow 0$. Despite its simple form, it is actually slightly simpler to reverse the change of variable and work with the expression
$$\phi=\frac{1}{\lambda \mu} \int_{0}^{s(\psi)} \frac{G(s) d s}{\left(1-\lambda^{-1} G(s)\right)\left(s+C_{\beta}\right)} .$$

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/ba0b4a59-2b1b-4998-859c-b58cf6bb6861-22.jpg?height=372&width=647&top_left_y=390&top_left_x=677}
\captionsetup{labelformat=empty}
\caption{Figure 3.1. Graph of $\psi$}
\end{figure}

First, we claim that the function $G(s)$ has a polynomial expansion in $s^{\frac{1}{n}}$ at any (finite) order. We prove this by induction, given that this is clear at order one. Set $\gamma(s)=G\left(s^{n}\right)$, which satisfies
$$\gamma(s)^{n}(b-a \gamma(s))=s^{n} .$$
Fix an integer $N \geqslant 0$, and assume that one can write $\gamma(s)=b^{-\frac{1}{n}} s+s^{2}\left(P_{N}(s)+\right.$ $\left.R_{N}(s)\right)$ where $P_{N}$ is a polynomial of degree at most $N$ while $R_{N}(s)=O\left(s^{N+1}\right)$. By (3.30), we get
$$\begin{aligned}
b-a\left(P_{N}+R_{N}\right)=\left(\frac{s}{\gamma(s)}\right)^{n} & =b^{\frac{1}{n}}\left(1+\sum_{k=1}^{N+1}(-1)^{k} b^{\frac{k}{n}} s^{k}\left(P_{N}+R_{N}\right)^{k}\right)+O\left(s^{N+2}\right) \\
& =b^{\frac{1}{n}}\left(1+\sum_{k=1}^{N+1}(-1)^{k} b^{\frac{k}{n}} s^{k} P_{N}^{k}\right)+O\left(s^{N+2}\right)
\end{aligned}$$
from which one deduces that $R_{N}(s)=c_{N+1} s^{N+1}+O\left(s^{N+2}\right)$, as desired.
The expansion of $G(s)$ induces an expansion of $\frac{G(s)}{1-\lambda^{-1} G(s)}$, which we can combine with $\frac{1}{s+C_{\beta}}=s^{-1}\left(1-\frac{C_{\beta}}{s}+O\left(\left(\frac{C_{\beta}}{s}\right)^{2}\right)\right)$ and (3.29) to obtain
$$\phi=P_{N}\left(s^{\frac{1}{n}}\right)+O\left(s^{\frac{N+1}{n}}\right)+\frac{C_{\beta}}{s^{1-\frac{1}{n}}}\left(c_{0}+O\left(s^{\frac{1}{n}}\right)+O\left(\frac{C_{\beta}}{s}\right)\right)$$
where $P_{N}$ is a polynomial of degree at most $N$ vanishing at 0 , $c_{0}=\frac{1}{(n-1) b^{1+\frac{1}{n}}}$ while
$$s:=s(\psi)=e^{\mu \psi}-C_{\beta} .$$

This asymptotic expansion is valid in the zone $C_{\beta} \ll s \ll 1$ or, equivalently by (3.27), in
$$\left(\beta-\beta_{*}\right)^{\frac{1}{n}} \ll e^{-\beta_{*} u} \ll 1 .$$
It will be convenient to introduce the variables
$$\varrho:=e^{-\frac{1}{2} \beta_{*} u} \quad \text { and } \quad r=2 \varrho$$
( $r$ will correspond to a Riemannian radius but $\varrho$ is more convenient to write expansions). We expand $\phi_{\beta}$ in powers of $\varrho^{2}$ and $\delta:=\frac{C_{\beta}}{\varrho^{2 n}}$ (the latter is a $o(1)$ from (3.33)). Therefore, we need to expand $s$ in powers of $\varrho$ and $\varepsilon$.

First, one infers from (3.27)
$$e^{\mu \psi}=\varrho^{2 n}\left(1+O\left(\varrho^{2 n}\right)\right) .$$
In particular, we find
$$s=e^{\mu \psi}\left(1-C_{\beta} e^{-\mu \psi}\right)=\varrho^{2 n}\left(1+O\left(\varrho^{2 n}\right)+\delta\left(-1+O\left(\varrho^{2 n}\right)\right)\right)$$

We claim that we can improve (3.36) as follows. Given any order $N \geqslant 0$, one can find a polynomial $Q_{N}$ or degree at most $N$ such that
$$s^{\frac{1}{n}}=h \varrho^{2}, \quad \text { with } \quad h(\varrho)=Q_{N}(\varrho)+O\left(\varrho^{N+1}\right)+\delta\left(c_{1}+O\left(\varrho^{2}\right)+O(\delta)\right),$$
for some (negative) constant $c_{1}$. From (3.36), we have $Q_{N}(0)=1$. Let us now prove the claim (3.37). In what follows $g_{\bullet}$ will denote a function of the form cst $+O\left(\varrho^{2}\right)+O(\delta)$. Note that this class of functions is stable under addition and multiplication. We assume that the claim is known at some level $N \geqslant 1$ and we write $h(\varrho)=Q_{N}(\varrho)+R_{N}+\delta g_{N}$. We need to show that $R_{N}=c_{N+1} \varrho^{N+1}+$ $O\left(\varrho^{N+2}\right)$.

An easy computation shows that for any $k \in \mathbb{N}$, we have
$$h(\varrho)^{k}=\text { polynomial }+k C_{0}^{\frac{k-1}{n}} R_{N}(\varrho)+\delta g_{h, k} .$$
In particular, we have $P_{N}\left(h \varrho^{2}\right)=$ polynomial $+\delta g_{N}+O\left(\varrho^{N+3}\right)$, hence for any $k \in \mathbb{N}$, we have
$$\left(P_{N}\left(h \varrho^{2}\right)+O\left(\left(h \varrho^{2}\right)^{N+1}\right)\right)^{k}=\text { polynomial }+\delta g_{N, k}+O\left(\varrho^{N+3}\right) .$$

Next, we have $\frac{C_{\beta}}{s^{1-\frac{1}{n}}}=\delta \varrho^{2} h^{1-n}=\delta g_{0}$ so that for any $k \geqslant 1$, (3.31) and (3.39) yield $\phi_{\beta}(\varrho)^{k}=$ polynomial $+\delta g_{\phi, k}+O\left(\varrho^{N+3}\right)$. Therefore, we find
$$\begin{aligned}
h(\varrho)^{n} & =e^{-\mu \phi}-\delta \\
& =e^{-\mu a_{0}}\left(1+\sum_{k=1}^{N} \frac{\left(-\mu^{k}\right)}{k!} \phi^{k}\right)+O\left(\varrho^{2 N+2}\right)-\delta \\
& =\text { polynomial }+\delta g_{h, n}+O\left(\varrho^{N+3}\right)
\end{aligned}$$
and (3.38) with $k=n$ yields the expected result (3.37) (we actually get the improved result that $Q_{N}$ is even). It is now straightforward to infer the expansion of $\phi_{\beta}$ below
$$\begin{aligned}
\phi_{\beta}(\varrho)= & \sum_{k=0}^{N} a_{k} \varrho^{2 k}+O\left(\varrho^{2 N+2}\right) \\
& +a_{L} \frac{\beta-\beta_{*}}{\varrho^{2 n-2}} \cdot\left(1+O\left(\varrho^{2}\right)+O\left(\frac{\beta-\beta_{*}}{\varrho^{2 n}}\right)\right) .
\end{aligned}$$
Moreover, one can check that coefficients $a_{i}=a_{i}(\beta)$ are smooth in $\beta$ and the first ones are given by $a_{0}=0, a_{1}=\frac{1}{b^{1+\frac{1}{n}}}, a_{2}=\frac{1}{2 \lambda b^{1+\frac{2}{n}}} \cdot\left(1+\frac{1}{n+1}\right)$, and $a_{L}=$ $\frac{\alpha^{n}}{(n-1) n(n+1) b^{1+\frac{1}{n}}}$. At this point, it is convenient to (slightly) rescale $L$, replacing $u$ by $u+\left(1+\frac{1}{n}\right) \frac{\log b}{b}$. We therefore consider $\tilde{\phi}(u)=\phi\left(u-\left(1+\frac{1}{N}\right) \frac{\log b}{b}\right)$ : this changes the equations (3.7) and (3.6) to
$$\begin{gathered}
\tilde{\phi}^{\prime \prime}\left(-\tilde{\phi}^{\prime}\right)^{n-1}=b^{n+1} e^{-\mu \tilde{\phi}-(\alpha-1) u} \\
\omega^{n}=e^{-\mu \tilde{\phi}} b_{n, \alpha} \Xi
\end{gathered}$$
where now
$$b_{n, \alpha}=\beta_{*}^{n+1} a_{n, \alpha} .$$
As a result, the expansion (3.40) of $\tilde{\phi}$ has $a_{1}=1$.
We now consider that we have done the rescaling and we replace the previous $\phi$ by $\tilde{\phi}$, so $\phi$ is a solution of (3.41). In this way, $\phi_{\beta}$ coincides up to order 2 in $\varrho$ with the unique potential $\phi_{\beta_{*}}$ defined in (3.24) with $c_{1}=1, c_{2}=0$, i.e.
$$\phi_{\beta_{*}}(\varrho)=\log \left(1+\varrho^{2}\right)=\log \left(1+\frac{r^{2}}{4}\right)=\frac{r^{2}}{4}-\frac{r^{4}}{32}+\cdots$$

Since the $a_{i}(\beta)$ are differentiable in $\beta$, the polynomial expansion of $\phi_{\beta}$ (i.e. the first line in the expansion above) differs from that of $\phi_{\beta_{*}}$ by a factor $O((\beta-$ $\left.\beta_{*}\right) r^{4}$ ). Therefore, we have
Theorem 3.3. Given any $N>0$, the potential $\phi_{\beta}$ admits the following expansion, valid in the zone $\left(\beta-\beta_{*}\right)^{\frac{1}{n}} \ll r^{2} \ll 1$ :
$$\phi_{\beta}(r)=\phi_{\beta_{*}}(r)+a_{L} \frac{\beta-\beta_{*}}{r^{2 n-2}} \cdot\left(1+O\left(r^{2}\right)+O\left(\frac{\beta-\beta_{*}}{r^{2 n}}\right)\right)+O\left(r^{2 N}\right),$$
where $\phi_{\beta_{*}}$ is given by (3.44) and $a_{L}>0$ is a positive constant.
In the remaining part of this section, let us now explain how to get expansions similar to (3.40) for $\phi_{\beta}^{\prime}$ and $\phi_{\beta}^{\prime \prime}$. Since $\varrho=e^{-\frac{1}{2} \beta_{*} u}$, one has $\partial_{u}=-\frac{\beta_{*}}{2} \varrho \partial_{\varrho}$ hence one can rewrite (3.7) as $F\left(-\frac{\beta_{*}}{2} \varrho \partial_{\varrho} \phi\right)=\varrho^{2 n} e^{-\mu \phi}-C_{\beta}$. Recall that we introduced the function $\delta=\frac{C_{\beta}}{\varrho^{2 n}}$ which goes to zero but at a rate which is "independent" of $\varrho$. The above identity becomes
$$\varrho \partial_{\varrho} \phi=-\frac{2}{\beta_{*}} G\left(\varrho^{2 n}\left(e^{-\mu \phi}-\delta\right)\right) .$$
Since $G(s)$ has finite expansions in powers of $s^{\frac{1}{n}}$ near 0 (cf paragraph around (3.30)), any expansion of $\phi$ in powers of $\varrho$ and $\delta$ will yield an expansion of $\varrho \partial_{\varrho} \phi$. Moreover, the coefficients in the expansion are formally determined by the equation above. More precisely, if one combines the expansion of $G$ and the following expansion induced by (3.40)
$$\begin{aligned}
\varrho^{2}\left(e^{-\mu \phi}-\delta\right)^{\frac{1}{n}} & =\left(\sum_{k=1}^{N} * \varrho^{2 k}+O\left(\varrho^{2 N+2}\right)\right) \cdot\left(1-\frac{1}{n} \delta e^{\mu b_{0}}+O\left(\delta \varrho^{2}\right)+O\left(\delta^{2}\right)\right) \\
& =\sum_{k=1}^{N} * \varrho^{2 k}+O\left(\varrho^{2 N+2}\right)+\delta \varrho^{2}\left(*+O\left(\varrho^{2}\right)+O(\delta)\right)
\end{aligned}$$
we get an expansion $\varrho \partial_{\varrho} \phi=\sum_{k=1}^{N} * \varrho^{2 k}+O\left(\varrho^{2 N+2}\right)+\delta \varrho^{2}\left(*+O\left(\varrho^{2}\right)+O(\delta)\right)$ and we recover the coefficients from (3.40) by integration, i.e.
$$\begin{aligned}
\varrho \partial_{\varrho} \phi_{\beta}(r)= & \sum_{k=1}^{N} 2 k a_{k} \varrho^{2 k}+O\left(\varrho^{2 N+2}\right)+ \\
& +(2 n-2) a_{L} \frac{\beta-\beta_{*}}{\varrho^{2 n-2}} \cdot\left(1+O\left(\varrho^{2}\right)+O\left(\frac{\beta-\beta_{*}}{\varrho^{2 n}}\right)\right) .
\end{aligned}$$

Feeding this into (3.7), we obtain next
$$\begin{aligned}
\left(\varrho \partial_{\varrho}\right)^{2} \phi_{\beta}(\varrho)= & \sum_{k=1}^{N}(2 k)^{2} a_{k} \varrho^{2 k}+O\left(\varrho^{2 N+2}\right)+ \\
& +(2 n-2)^{2} a_{L} \frac{\beta-\beta_{*}}{\varrho^{2 n-2}} \cdot\left(1+O\left(\varrho^{2}\right)+O\left(\frac{\beta-\beta_{*}}{\varrho^{2 n}}\right)\right) .
\end{aligned}$$
Combining (3.45) and (3.47) and coming back to the variable $r$, this leads to
$$\omega_{\beta}=\omega_{\beta_{*}}+\left(O\left(\frac{\beta-\beta_{*}}{r^{2 n}}\right)+O\left(r^{2 N-2}\right)\right) \omega_{\beta} .$$
3.7. Asymptotics of $g_{\beta}$. In order to analyse the Riemannian metric $g_{\beta}$ associated to $\omega_{\beta}$, we introduce the variable $s:=-\phi^{\prime}$ which decreases from $\alpha$ (on $D$, i.e. at $u=-\infty)$ to 0 (at the extinction time $u=u_{\beta}$ of the solution) corresponding to the moment map of the $S^{1}$ action on $L$ and write $g_{\beta}$ as
$$\begin{aligned}
g_{\beta} & =\phi^{\prime \prime}\left(d u^{2}+4 \eta^{2}\right)+\frac{2 s}{\alpha-1} g_{D} \\
& =\frac{d s^{2}}{\phi^{\prime \prime}}+4 \phi^{\prime \prime} \eta^{2}+\frac{2 s}{\alpha-1} g_{D}
\end{aligned}$$
where $\eta$ is the connection 1-form, satisfying $d \eta=-\frac{1}{\alpha-1} \omega_{D}$. Using (3.9)-(3.8), we see that
$$\phi^{\prime \prime}=\frac{1}{s^{n-1}}\left(s^{n}(b-a s)+C_{\beta}\right) .$$
Given (3.10), we have $\phi^{\prime \prime}(\alpha)=0$; after factorizing, we get $\phi^{\prime \prime}(s)=s(\alpha-s)(a-$ $(b-a \alpha) \frac{\alpha^{n}-s^{n}}{s^{n}(\alpha-s)}$ ). Using $\alpha a=\beta_{*}+\frac{1}{n+1}\left(\beta-\beta_{*}\right)$ and $b-a \alpha=\frac{1}{n+1}\left(\beta-\beta_{*}\right)$, we eventually find
$$\phi^{\prime \prime}=s\left(1-\frac{s}{\alpha}\right) \beta_{*}\left(1+\frac{1}{(n+1) \beta_{*}}\left(\beta-\beta_{*}\right) \cdot \frac{\alpha^{n+1}-s^{n+1}}{s^{n}(\alpha-s)}\right) .$$
Setting $V_{\beta}(s)=\phi^{\prime \prime}$, we can rewrite $g_{\beta}$ as
$$g_{\beta}=\frac{d s^{2}}{V_{\beta}(s)}+V_{\beta}(s) 4 \eta^{2}+\frac{2 s}{\alpha-1} g_{D} .$$
Using (3.49), we find:
\begin{itemize}
\item[-] When $s \rightarrow \alpha, V_{\beta}(s) \simeq(\alpha-s) \beta$. Setting $r:=2 \sqrt{\frac{\alpha-s}{\beta}}$, we see that $g_{\beta} \simeq$ $d r^{2}+\beta^{2} r^{2} \eta^{2}+\frac{2 s}{\alpha-1} g_{D}$, i.e. $g_{\beta}$ has a cone singularity of angle $2 \pi \beta$ along $D$.
\end{itemize}
\begin{itemize}
\item[-] When $s \rightarrow 0$, we have either
$$V_{\beta}(s) \simeq\left\{\begin{array}{ll}
\frac{\alpha^{n}}{n+1}\left(\beta-\beta_{*}\right) \frac{1}{s^{n-1}} & \text { if } \beta>\beta_{*} \\
s \beta_{*} & \text { if } \beta=\beta_{*}
\end{array} .\right.$$
In the case where $\beta>\beta_{*}, g_{\beta}$ is an incomplete metric where the circles blow up and the divisor gets contracted. In the case where $\beta=\beta_{*}, g_{\beta_{*}}$ is incomplete again and contracts the divisor at infinity $D_{\infty}$ in $L$; i.e. $D_{\infty}=$ $\mathbb{P}(L) \subset \mathbb{P}\left(L \oplus \mathcal{O}_{D}\right)$. The metric $g_{\beta_{*}}$ is equivalent near zero to the cone metric
$$\begin{aligned}
g_{\text {cone }} & =\frac{d s^{2}}{s \beta_{*}}+4 s \beta_{*} \eta^{2}+\frac{2 s}{\alpha-1} g_{D} \\
& =d r^{2}+r^{2} \beta_{*}^{2} \eta^{2}+\frac{\beta_{*} r^{2}}{2(\alpha-1)} g_{D}
\end{aligned}$$
with $r:=2 \sqrt{\frac{S}{\beta_{*}}}$, which is the asymptotic cone of the Tian-Yau metric.
\end{itemize}

Let us now obtain an expansion in $\beta-\beta_{*}$ of the metric $g_{\beta}$, which we will be mostly interested in near $s=0$ where we will glue it to the Tian-Yau metric. So we set
$$\begin{aligned}
g_{\beta_{*}} & :=\frac{1}{s\left(1-\frac{s}{\alpha}\right) \beta_{*}} d s^{2}+4 s\left(1-\frac{s}{\alpha}\right) \beta_{*} \eta^{2}+\frac{2 s}{\alpha-1} g_{D} \\
& =g_{\text {cone }}+\frac{s}{\alpha}\left(\frac{d s^{2}}{s \beta_{*}}-4 s \beta_{*} \eta^{2}\right)+O\left(s^{2}\right) \\
& =g_{\text {cone }}+\frac{\beta_{*}}{4 \alpha} r^{2} d r^{2}+O\left(r^{4}\right) .
\end{aligned}$$
The expansion of $g_{\beta}$ is given by
$$g_{\beta}=g_{\beta_{*}}+\left(\beta-\beta_{*}\right) g_{1}+O\left(\left(\beta-\beta_{*}\right)^{2}\right)$$
where
$$g_{1}=\frac{\alpha^{n+1}-s^{n+1}}{s^{n}(\alpha-s)} \cdot \frac{1}{(n+1) \beta_{*}}\left(\frac{-d s^{2}}{s\left(1-\frac{s}{\alpha}\right) \beta_{*}}+4 s\left(1-\frac{s}{\alpha}\right) \beta_{*} \eta^{2}\right) .$$
3.8. Finding the scaling factor and the gluing region. In order to perform a gluing construction, we need to ensure that most of the domain of the potential $\phi_{\beta}$ be included in an infinitesimally small (i.e. as $\beta \rightarrow \beta_{*}$ ) neighborhood of the zero section. This is certainly not the case as such but it can be achieved by using the radial automorphisms of $L$. More precisely, we use the scaling $\mathbb{C}^{*}$ action on $L$ by $t \cdot(x, v)=(x, t v)$ to get a new potential $\phi_{\beta}^{t}(v)=\phi_{\beta}(t v)$. In terms of the function $u$, we have $\phi_{\beta}^{t}(u)=\phi_{\beta}\left(u-\log |t|^{2}\right)$.

From now on we use a diffeomorphism of a small neighborhood of fixed euclidean size of $D \subset X$ with a small neighborhood of the zero section in $L$ to identify both sets. If we glue near $u$, we have to make sure that the size of $D$ measured with $\omega_{\beta}$ and $\varepsilon \omega_{\mathrm{TY}}$ is the same (here $\varepsilon=\varepsilon_{\beta}$ ), which yields the equation
$$\left(-\phi_{\beta}^{t}\right)^{\prime}(u) \approx \varepsilon e^{-\beta_{*} u},$$
where $\approx$ means that the log of the quotient is bounded. Given (3.40), we find that in the zone $\left(\beta-\beta_{*}\right)^{\frac{1}{n}} \ll e^{-\beta_{*} u} \ll 1$ we have $\phi_{\beta}^{\prime}(u) \approx e^{-\beta_{*} u}$ hence the equation (3.52) is satisfied provided
$$\varepsilon \approx|t|^{2 \beta_{*}}, \quad \text { i.e. } \log |t|^{2}=\frac{1}{\beta_{*}} \log \varepsilon+O(1)$$
holds. It will be convenient to introduce the scaling (shrinking) map $\lambda_{\varepsilon}: L \rightarrow L$ defined by
$$\lambda_{\varepsilon}(v)=\varepsilon^{\frac{1}{2 \beta *}} v .$$
From now on we set
$$\widehat{u}_{\beta}:=-\frac{1}{n \beta_{*}} \log \left(\beta-\beta_{*}\right)$$
Finally, we set
$$\psi_{\beta}:=\phi_{\beta}\left(\cdot-\frac{1}{\beta_{*}} \log \varepsilon\right)=\left(\lambda_{\varepsilon}\right)_{*} \phi_{\beta}$$
which is defined on ( $u \leqslant \widehat{u}_{\beta}+\frac{1}{\beta_{*}} \log \varepsilon$ ). The asymptotics of $\phi_{\beta}(v)$ match those of the conic Tian-Yau potential in the region where $1 \ll v \ll-\frac{1}{n \beta_{*}} \log \left(\beta-\beta_{*}\right)$, cf (3.40). Therefore we need to glue $d d^{c} \psi_{\beta}(u)$ to $\varepsilon_{\beta} \omega_{\text {TY }}$ near $u=u_{\beta}$ (i.e. in a zone like $\left.\left|u-u_{\beta}\right| \leqslant 1\right)$ satisfying
$$\frac{1}{\beta_{*}} \log \varepsilon_{\beta} \ll u_{\beta} \ll \frac{1}{\beta_{*}} \log \frac{\varepsilon}{\left(\beta-\beta_{*}\right)^{\frac{1}{n}}}$$

In term of the Tian-Yau radius $R=2|v|^{-\beta_{*}}$, this means
$$\left(\beta-\beta_{*}\right)^{\frac{1}{n}} \ll \varepsilon R^{2} \ll 1 .$$
In the gluing zone, (3.27) guarantees that $s(u)=-\phi^{\prime}\left(u-\frac{1}{\beta_{*}} \log \varepsilon\right) \simeq \varepsilon R^{2}$ hence $s^{n} \gg \beta-\beta_{*}$ by (3.54). Combined with (3.49), this shows that
$$g_{\beta} \approx g_{\text {cone }}=\frac{d s^{2}}{s \beta^{*}}+4 s \beta_{*} \eta^{2}+\frac{2 s}{\alpha-1} g_{D}$$
# Degenerating Kähler–Einstein cones, locally symmetric cusps, and the Tian-Yau metric

- Category: papers
- Identity: doi:10.1007/s00222-022-01138-5
- Content status: fulltext_ok

---

---
source_file: 2108_13318.pdf
converter: mathpix
format: mmd
---

\title{
DEGENERATING KÄHLER-EINSTEIN CONES, LOCALLY SYMMETRIC CUSPS, AND THE TIAN-YAU METRIC
}

\author{
OLIVIER BIQUARD AND HENRI GUENANCIA
}

\begin{abstract}
Let $X$ be a complex projective manifold and let $D \subset X$ be a smooth divisor. In this article, we are interested in studying limits when $\beta \rightarrow 0$ of Kähler-Einstein metrics $\omega_{\beta}$ with a cone singularity of angle $2 \pi \beta$ along $D$. In our first result, we assume that $X \backslash D$ is a locally symmetric space and we show that $\omega_{\beta}$ converges to the locally symmetric metric and further give asymptotics of $\omega_{\beta}$ when $X \backslash D$ is a ball quotient. Our second result deals with the case when $X$ is Fano and $D$ is anticanonical. We prove a folklore conjecture asserting that a rescaled limit of $\omega_{\beta}$ is the complete, Ricci flat Tian-Yau metric on $X \backslash D$. Furthermore, we prove that $\left(X, \omega_{\beta}\right)$ converges to an interval in the Gromov-Hausdorff sense.
\end{abstract}

\section*{Contents}
Introduction ..... 1
1. Closing the cusps of locally symmetric spaces ..... 5
2. The Calabi ansatz ..... 10
3. Curvature calculations ..... 14
4. Asymptotics of the conical KE metrics on ball quotients ..... 16
5. Gluing with the Tian-Yau metric ..... 21
6. Uniform Schauder estimate for cones ..... 27
7. Schauder estimate for collapsed metrics ..... 37
8. Convergence in the positive case: proof of Theorem B ..... 45
References ..... 49

\section*{Introduction}

Let $X$ be a complex projective manifold and let $D \subset X$ be a smooth divisor. In many geometrically meaningful situations, one is able to construct Kähler-Einstein metrics $\omega$ on the complement $X^{\circ}:=X \backslash D$ of the divisor $D$. Unless one imposes some growth condition near $D$, such a metric $\omega$ may not be unique - one can typically find complete and incomplete KE metrics on the same $X^{\circ}$, possibly with the same Einstein constant too.

The focus of the present paper is to investigate the relationship between these different metrics in the specific setting of Kähler-Einstein metrics with cone singularities along $D$. Recall that if $\beta \in(0,1)$, a Kähler metric $\omega$ on $X^{\circ}$ is said to have cone singularities along $D$ with cone angle $2 \pi \beta$ if it is locally
quasi-isometric to the model cone metric
$$\omega_{\beta, \text { mod }}:=\frac{i d z_{1} \wedge d \bar{z}_{1}}{\left|z_{1}\right|^{2(1-\beta)}}+\sum_{j \geqslant 2} i d z_{j} \wedge d \bar{z}_{j}$$
on each coordinate chart $\left(U,\left(z_{i}\right)\right)$ where $U \cap D=\left(z_{1}=0\right)$. Such a metric is incomplete, has finite volume and automatically extends to a closed, positive (1,1)-current on X. There is an analogue of the Aubin-Yau (resp. Yau) theorem guaranteeing the existence and uniqueness of a negatively curved (resp. Ricci-flat) Kähler-Einstein metric $\omega_{\beta}$ with cone angle $2 \pi \beta$ along $D$ under the condition that the adjoint $\mathbb{R}$-line bundle $K_{X}+(1-\beta) D$ is ample (resp. numerically trivial), cf e.g. [Bre13, CGP13, GP16, JMR16]. The positive curvature case is more complicated, in analogy with the absolute case $D=\varnothing$ and it involves the properness of some suitable analogue of the Mabuchi or Ding functional.

Let us now shift our focus to the small angle regime, that is when $0<\beta \ll 1$. We raise the following broad and somewhat vague question, which is closely related to [CR15, Conjecture 1.11] and [Oda20, Conjecture 1.4] in the positive curvature case.

Question. Let $X$ be a complex projective manifold and let $D \subset X$ be a smooth divisor. Assume that for any $0<\beta \ll 1$, there exists a unique Kähler-Einstein metric $\omega_{\beta}$ with cone angle $2 \pi \beta$ along $D$, i.e.
$$\operatorname{Ric} \omega_{\beta}=\sigma \omega_{\beta}+(1-\beta)[D]$$
for some $\sigma= \pm 1$. Do the metrics $\omega_{\beta}$ converge when $\beta \rightarrow 0$ to some canonical metric on $X^{\circ}$, possibly after rescaling?

The aim of this paper is to provide an answer to the above question in two different geometric situations, one for each sign of the curvature.

The negative case.
As recalled above, the existence of a KE metric solving (0.1) with $\sigma=-1$ is equivalent to $K_{X}+(1-\beta) D$ being ample. For instance, if one assumes that $K_{X}+D$ is ample, then the same will hold true for $K_{X}+(1-\beta) D$ as long as $\beta$ is small enough. In that situation, it was proved in [Gue20] that when $\beta \rightarrow 0$, the KE metric $\omega_{\beta}$ converges to the complete KE metric with Poincaré growth constructed by R. Kobayashi [Kob84] and Tian-Yau [TY87].

Another interesting example is provided by toroidal compactifications of ball quotients $X^{\circ}=\Gamma \backslash \mathbb{B}^{n}$, where $\Gamma \subset \operatorname{Aut}\left(\mathbb{B}^{n}\right)$ is a torsion-free, discrete subgroup. It is well-known that one can embed $X^{\circ} \hookrightarrow X$ as a Zariski-open subset of a projective orbifold $X$ such that $D:=X \backslash X^{\circ}$ is a disjoint union of abelian varieties, cf § 1.1 for references and more details. Note that the Bergman metric on $\mathbb{B}^{n}$ descends to the complex (complete) hyperbolic metric $\omega_{\text {hyp }}$ on $X^{\circ}$, which we normalize to have $\operatorname{Ric} \omega_{\text {hyp }}=-\omega_{\text {hyp }}$. Moreover, $K_{X}+$ $(1-\beta) D$ is ample for $0<\beta \ll 1$ (but certainly not for $\beta=0$ unless $D=\varnothing$ ) and therefore $X^{\circ}$ also comes equipped with KE metrics $\omega_{\beta}$ with cone angle
$2 \pi \beta$ along $D$ whenever $\beta>0$ is small enough. The relationship between these metrics is provided by the following
Theorem A. Let $(X, D)$ be a toroidal compactification of a ball quotient $X^{\circ}=$ $\Gamma \backslash \mathbb{B}^{n}$, and let $\omega_{\beta}$ be the KE metric solving (0.1) for small $\beta$, with $\sigma=-1$. Then, we have convergence
$$\omega_{\beta} \underset{\beta \rightarrow 0}{\longrightarrow} \omega_{\text {hyp }}$$
both in $C_{\text {loc }}^{\infty}\left(X^{\circ}\right)$ and weakly as currents on $X$. Moreover, we have precise asymptotics of $\omega_{\beta}$ near $D$ when $\beta \rightarrow 0$.

A few remarks are in order here.
\begin{itemize}
\item[(i)] The asymptotics of $\omega_{\beta}$ in $C^{0}$ are given in Theorem 4.5. They are obtained by constructing a model metric on the normal bundle of $D$ using the Calabi Ansatz, cf § 2.
\item[(ii)] The first half of the statement (i.e. the convergence part) remains true in the more general setting of quotients of bounded symmetric domains, cf Theorem 1.1. In that case, $D$ needs not be smooth anymore but has simple normal crossings up to a finite cover.
\item[(iii)] Assume that the lattice $\Gamma$ is arithmetic. By choosing the angles carefully along each torus at the boundary, one can find a sequence $\omega_{\beta_{m}}$ of orbifold KE metrics that can be globally desingularized so that $\left(X^{\circ}, \omega_{\text {hyp }}\right)$ is the limit of smooth, compact KE spaces up to the action of a larger and larger group of isometries, cf § 4.3. In a nutshell, one can "close the complex hyperbolic cusp". This gives the closest analog to the Dehn filling of real hyperbolic cusps by Einstein manifolds, due to Thurston in dimension 3 and Anderson [And06] in higher dimension: in the complex case, one cannot fill the cusp, but this is possible up to some larger and larger covering. This answers a question of Misha Kapovich to the first author several years ago.
\end{itemize}

The positive case.
In general, it is not so easy to characterize the existence of a metric $\omega_{\beta}$ solving (0.1) with $\sigma=1$, for small values of $\beta$. However, a result of Berman [Ber13] (later generalized by Song-Wang [SW16]) asserts that if $X$ is a Fano manifold (that is, $-K_{X}$ is ample) and $D \in\left|-K_{X}\right|$ is smooth, then there exists $\beta_{0}>0$ such that for any $0<\beta<\beta_{0}$, there exists a unique Kähler metric $\omega_{\beta}$ on $X^{\circ}$ such that $\operatorname{Ric} \omega_{\beta}=\omega_{\beta}$ and $\omega_{\beta}$ has cone singularities with cone angle $2 \pi \beta$ along $D$, i.e. $\omega_{\beta}$ solves (0.1).

The existence of such a metric had been conjectured by Donaldson [Don12, § 6] in relation with his program to prove that a $K$-stable Fano manifold admits a Kähler-Einstein metric by using the continuity path Ric $\omega_{t}=t \omega_{t}+(1-t)[D]$ involving metrics with cone singularities. He also predicted that the (conjectural then) $\omega_{\beta}$ would actually converge to the Ricci flat complete Kähler metric $\omega_{\mathrm{TY}}$ constructed by Tian and Yau in [TY90].

If $n=1$, then the metrics $\omega_{\beta}$ on $\mathbb{P}^{1} \backslash\{0, \infty\}$ are completely explicit, given by the expression $\omega_{\beta}=\frac{\beta^{2} i d z \wedge d \bar{z}}{|z|^{2(1-\beta)}\left(1+|z|^{2 \beta}\right)^{2}}$ and one sees immediately that $\beta^{-2} \omega_{\beta}$
converges locally smoothly to the cylinder $\omega_{\text {cyl }}=\frac{i d z \wedge d \bar{z}}{4|z|^{2}}$ while $\left(\mathbb{P}^{1}, \omega_{\beta}\right)$ converges in the Gromov-Hausdorff sense to the interval $\left(\left[0, \frac{\pi}{2}\right], d t^{2}\right)$ (set $r=|z|^{\beta}$ to that $g_{\beta}=\frac{d r^{2}+\beta^{2} r^{2} d \theta^{2}}{\left(1+r^{2}\right)^{2}}$ and reparametrize by $\left.t=\tan ^{-1}(r)\right)$, cf also [RZ20]. Our second main result establishes the conjecture in full generality.
Theorem B. Let $X$ be a Fano manifold of dimension $n$ and let $D \in\left|-K_{X}\right|$ be a smooth anticanonical divisor. Then up to a rescaling factor, the conic KE metrics $\omega_{\beta}$ solving (0.1) with $\sigma=1$ for small $\beta$ converge to the Tian-Yau metric:
$$\beta^{-1-\frac{1}{n}} \omega_{\beta} \underset{\beta \rightarrow 0}{\longrightarrow} \omega_{\mathrm{TY}}$$
in $C_{\text {loc }}^{\infty}(X \backslash D)$. Moreover, we have precise asymptotics of $\omega_{\beta}$ near $D$ when $\beta \rightarrow 0$.
Finally fix a point $p \in D$, denote $g_{\beta}$ the Riemannian metric associated to the Kähler form $\omega_{\beta}$ and consider the renormalized volume forms $v_{\beta}=\frac{d \operatorname{vol}_{g_{\beta}}}{\operatorname{vol}_{g_{\beta}}(X)}$. Then the spaces $\left(X, g_{\beta}, p, v_{\beta}\right)$ converge in the measured Gromov-Hausdorff sense to the interval
$$\left(\left[0, \frac{\pi}{2}\right], g_{\infty}=\frac{2}{n+1} d s^{2}, 0, v_{\infty}=d\left(-\cos ^{\frac{2 n}{n+1}} s\right)\right) .$$

As before, a few remarks:
\begin{itemize}
\item[(i)] The fibers of the collapsing to an interval are the normal circle bundle of the divisor $D$. The two endpoints of the interval correspond respectively to the conical divisor $D$ itself and to the Tian-Yau metric. Over interior points of the interval, the fibres have two speeds of collapsing: speed $\beta$ for the circle directions and $\sqrt{\beta}$ for the divisor directions. See section 5.3 for a detailed discussion, a relevant picture, as well as the computation of the other possible nontrivial Gromov-Hausdorff limits of the rescaled metrics $g_{\beta}$ : we obtain $\mathbb{R}_{+}, \mathbb{R}_{+} \times D$ and $\mathbb{R}_{+} \times \mathbb{C}^{n-1}$ at $s=0$, and at $s=\frac{\pi}{2}$ the previous Tian-Yau metric on $X \backslash D$ and $\mathbb{R}_{+}$.
\item[(ii)] Several recent papers study cases of collapsing of Ricci flat Kähler metrics to an interval, for K3 surfaces [HSVZ22] or in higher dimension [SZ19]. Our theorem probably gives the first general example of collapsing of Kähler-Einstein metrics with positive Ricci: of course this is made possible by the presence of a cone angle going to zero.
\item[(iii)] In the process of the proof, we construct the Kähler-Einstein metrics $\omega_{\beta}$ for small $\beta$, therefore recovering Berman's result.
\end{itemize}

\section*{Strategy of the proof.}

Although Theorem A and Theorem B have a quite different flavor, their proofs share a common approach. Indeed, in both proofs, we rely on the existence of a model metric living in the neighborhood of the zero section in the normal bundle of $D$. That metric is provided by the Calabi Ansatz, cf § 2, and its curvature is computed in the following section, § 3.

The proof of Theorem A goes as follows. We use pluripotential methods, especially the comparison principle (quite suited in negative curvature), in order to estimate the potential of $\omega_{\beta}$ with enough precision to establish the weak convergence. The local smooth convergence away from $D$ follows from a suitable use of Chern-Lu formula. In order to further compute the asymptotics of
$\omega_{\beta}$ (at order zero), we show that $\omega_{\beta}$ is asymptotically close to the Calabi metric constructed and analyzed in § 2. This relies on the previous step as well as the application of the maximum principle and Chern-Lu formula, which in turn uses crucially that the curvature of the Calabi metric is bounded, cf § 3.

The proof of Theorem B, technicallly more involved than the previous one, relies on gluing methods. The general idea is to construct a model cone metric $\tilde{\omega}_{\beta}$ by gluing the Calabi metric $\omega_{\beta, L}$ near $D$ and the Tian-Yau metric $\omega_{T Y}$ away from $D$. For $\beta \ll 1$, the implicit function theorem allows us to find the Kähler-Einstein metric $\omega_{\beta}=\tilde{\omega}_{\beta}+d d^{c} \varphi_{\beta}$ with a control on $\varphi_{\beta}$ and its covariant derivatives that is sufficiently precise that one can derive the desired smooth convergence $\beta^{-1-\frac{1}{n}} \omega_{\beta} \rightarrow \omega_{T Y}$ away from $D$ as well as the global GromovHausdorff convergence of ( $X, \omega_{\beta}$ ) to an interval.

Some of the main technical steps include: estimating the curvature of the Calabi metric; finely gluing the Calabi metric which lives on the normal bundle $L$ of $D$ onto a neighborhood of $D$ in $X$ using a fibration in extremal disks; establishing a Schauder estimate for the model cone metric on $\mathbb{C}^{*} \times \mathbb{C}^{n-1}$ with cone angle $2 \pi \beta$ which is uniform in $\beta$; establishing a uniform Schauder estimate in suitable weighted Hölder spaces for the family of collapsing cone metrics $\tilde{\omega}_{\beta}$ mentioned above. This is similar in spirit to other gluing problems, especially the papers [HSVZ22, SZ19] mentioned above, but our techniques are different.

Applying the techniques used for Theorem B to Theorem A would probably enhance our $C^{0}$ estimates for the metrics to estimates on all derivatives, at the expense of a much more technical proof. On the other hand, the pluripotential techniques seem to fall short in the context of Theorem B.

Acknowledgements. O.B. would like to thank Misha Kapovich for discussions a long time ago about closing complex hyperbolic cusps. H.G. would like to thank Benoît Cadorel for the many insightful discussions about toroidal compactifications of quotients of bounded symmetric domains. The authors would like to thank the referee for reading the manuscript carefully and for the several suggestions that helped us improve the paper.
H.G has benefited from the support of the ANR project GRACK as well as from the state aid managed by the ANR under the "PIA" program bearing the reference ANR-11-LABX-0040, in connection with the research project HER-METIC.

\section*{1. Closing the cusps of locally symmetric spaces}
1.1. Setup. Let $X=\Gamma \backslash \Omega$ be an $n$-dimensional quotient of a bounded symmetric domain $\Omega$ by a torsion-free lattice $\Gamma \subset \operatorname{Aut}(\Omega)^{\circ}$. It is well-known that $X$ is a quasi-projective variety that can be compactified in several meaningful ways.

The Satake-Baily-Borel compactification $X \hookrightarrow \bar{X}_{\text {min }}$ is a singular, minimal compactification in the sense that given any normal compactification $X \hookrightarrow \bar{X}^{\prime}$, the identity morphism on $X$ extends to a holomorphic map $\bar{X}^{\prime} \rightarrow \bar{X}_{\text {min }}$. The
variety $\bar{X}_{\text {min }}$ is normal, has log canonical singularities and $K_{\bar{X}_{\text {min }}}$ is ample. In a modern terminology, $\bar{X}_{\text {min }}$ is a (normal) stable variety.

The Ash-Mumford-Rapoport-Tai [AMRT10] toroidal compactification $X \hookrightarrow$ $\bar{X}$ is a compactification with finite quotient singularities such that $\bar{X} \backslash X$ is a (reduced) divisor with simple normal crossings that we denote by $D=\sum_{\lambda=1}^{N} D_{\lambda}$. Moreover, the birational morphism $\pi: \bar{X} \rightarrow \bar{X}_{\min }$ satisfies
$$K_{\bar{X}}+D=\pi^{*} K_{\bar{X}_{\min }} .$$

If $\Gamma$ is neat, the toroidal compactification $\bar{X}$ is actually smooth. Moreover, any torsion-free lattice $\operatorname{Aut}(\Omega)$ admits a finite index subgroup which is neat. As a result, one can find $\Gamma^{\prime}<\Gamma$ with finite index such that $Y=\Gamma^{\prime} \backslash \Omega$ admits a smooth toroidal compactification $\left(\bar{Y}, D^{\prime}\right)$. Moreover, the finite étale morphism $f: Y \rightarrow X$ extends uniquely to a finite cover $f: \bar{Y} \rightarrow \bar{X}$ and one has $K_{\bar{Y}}+D^{\prime}=$ $f^{*}\left(K_{\bar{X}}+D\right)$.

In the case where $\Omega=\mathbb{B}^{n}$ is the euclidean unit ball in $\mathbb{C}^{n}, \bar{X}_{\text {min }} \backslash X$ consist of finitely many singular points $\left\{x_{1}, \ldots, x_{N}\right\}$ and $D=\sqcup_{\lambda=1}^{N} D_{\lambda}$ is a disjoint union of abelian varieties $D_{\lambda}$ with negative normal bundle, which are contracted onto those singular points by $\pi$.
1.2. The Kähler-Einstein metric. The Bergman metric $\omega_{\text {Berg }}$ on $\Omega$ is invariant under the action of $\operatorname{Aut}(\Omega)$ hence it descends to a Kähler-Einstein metric $\omega_{\mathrm{KE}}$ on $X$. Moreover, one can prove that $\omega_{\mathrm{KE}}$ extends to a closed, positive current $\omega_{\mathrm{KE}} \in c_{1}\left(K_{\bar{X}}+D\right)$ and
$$\int_{X} \omega_{\mathrm{KE}}^{n}=c_{1}\left(K_{\bar{X}}+D\right)^{n} .$$
In particular, $\omega_{\mathrm{KE}}=\pi^{*} \omega_{\text {min }}$ for some closed, positive current $\omega_{\text {min }} \in c_{1}\left(K_{\bar{X}_{\text {min }}}\right)$ which coincides with the singular Kähler-Einstein metric constructed in [BG14].

If $\Gamma^{\prime}<\Gamma$ has finite index, then the Kähler-Einstein metric of $Y=\Gamma^{\prime} \backslash \Omega$ is simply $f^{*} \omega_{\mathrm{KE}}$ where $f: Y \rightarrow X$ is the finite étale cover induced by the lattice inclusion.

In the case where $\Omega=\mathbb{B}^{n}$ and $\Gamma$ is neat, one has a very precise description of $\omega_{\mathrm{KE}}$ near $D$, cf. e.g. [Mok12, Eq. (8)]. In particular, if $\left(z_{1}, \ldots, z_{n}\right)$ is a system of holomorphic coordinates on some open set $U \subset \bar{X}$ such that $D \cap U=\left(z_{1}=0\right)$, then $\left.\omega\right|_{U}$ is quasi-isometric to
$$\frac{i d z_{1} \wedge d \bar{z}_{1}}{\left|z_{1}\right|^{2}\left(-\log \left|z_{1}\right|\right)^{2}}+\frac{1}{\left(-\log \left|z_{1}\right|\right)} \sum_{k=2}^{n} i d z_{k} \wedge d \bar{z}_{k} .$$
One can actually say much more and exhibit an exact formula for $\omega_{\mathrm{KE}}$ on a small enough neighborhood $U$ of $D$ after identifying $U$ with a neighborhood of the zero section in the normal bundle $N_{D / X} \rightarrow D$ of $D$, cf (4.5).
1.3. Monge-Ampère equation. One can write down the Monge-Ampère equation satisfied by $\omega_{\mathrm{KE}}$. In order to do so, we pick:
- A Kähler metric $\omega_{\bar{X}_{\text {min }}} \in c_{1}\left(K_{\bar{X}_{\text {min }}}\right)$ and set $\chi:=\pi^{*} \omega_{\bar{X}_{\text {min }}}$. It is a smooth, semipositive form on $\bar{X}$. Recall that a Kähler metric on a singular complex
space $Y$ is defined to be a Kähler metric on the regular locus $Y_{\text {reg }}$ which is locally the restriction of an ambient Kähler form under local embeddings $Y \stackrel{\hookrightarrow}{\text { loc }}$ $\mathbb{C}^{N}$. In particular, its bisectional curvature is bounded above locally near any point.
- Holomorphic sections $s_{\lambda} \in H^{0}\left(\bar{X}, \mathcal{O}_{\bar{X}}\left(D_{\lambda}\right)\right)$ such that $D_{\lambda}=\left(s_{\lambda}=0\right)$ and smooth hermitian metrics $h_{\lambda}$ on $\mathcal{O}_{\bar{X}}\left(D_{\lambda}\right)$. with Chern curvature form $\theta_{\lambda}:=$ $i \Theta_{h_{\lambda}}\left(D_{\lambda}\right)$. We set $s=\otimes s_{\lambda},|s|:=\prod_{k}\left|s_{\lambda}\right|_{h_{\lambda}}, \theta=\sum_{k} \theta_{\lambda}$. Up to scaling $h_{\lambda}$, one can assume that $\left|s_{\lambda}\right|_{h_{\lambda}}<e^{-1}$.
- A smooth volume form $d V$ on $\bar{X}$ satisfying $-\operatorname{Ric}(d V)+\theta=\chi$. Then one can write the Kähler-Einstein metric $\omega_{\mathrm{KE}}$ on $\bar{X}$ as $\omega_{\mathrm{KE}}=\chi+d d^{c} \widehat{\varphi}$ for the unique $\chi$-psh function $\widehat{\varphi}$ solution of the (non-pluripolar) Monge-Ampère equation
$$\omega_{\mathrm{KE}}^{n}=\left(\chi+d d^{c} \widehat{\varphi}\right)^{n}=\frac{e^{\widehat{\varphi}} d V}{|s|^{2}} .$$
One knows that for any $\varepsilon>0$, there exists a constant $C_{\varepsilon}$ such that the following set of inequalities
$$C_{1} \geqslant \widehat{\varphi} \geqslant-(n+1+\varepsilon) \log (-\log |s|)-C_{\varepsilon}$$
hold on $\bar{X}$, cf. [DGG20, Prop. D].
1.4. Conic approximation. As $\pi$ can be obtained as a sequence of blow ups of smooth centers, there exist coefficients $a_{\lambda} \in \mathrm{Q}_{+}$such that $-\sum a_{\lambda} D_{\lambda}$ is $\pi$ ample. In particular, for $\beta>0$ small enough, the Q -line bundle $K_{X}+\sum_{\lambda}(1-$ $\left.\beta a_{\lambda}\right) D_{\lambda}$ is ample. Moreover, up to scaling down the $a_{\lambda}$ (by the same factor), one can assume that $\chi-\widetilde{\theta}$ is a Kähler form, where $\widetilde{\theta}:=\sum a_{\lambda} \theta_{\lambda}$. The Monge-Ampère equation
$$\left(\chi-\beta \widetilde{\theta}+d d^{c} \widehat{\varphi}_{\beta}\right)^{n}=\frac{e^{\widehat{\varphi}_{\beta}} d V}{\prod_{\lambda}\left|s_{\lambda}\right|_{h_{\lambda}}^{2\left(1-\beta a_{\lambda}\right)}}$$
has a unique solution $\widehat{\varphi}_{\beta} \in L^{\infty}(\bar{X}) \cap \operatorname{PSH}(\bar{X}, \chi-\beta \widetilde{\theta})$ by [Koł98]. Moreover, it is well-known that
$$\widehat{\omega}_{\beta}:=\chi-\beta \widetilde{\theta}+d d^{c} \widehat{\varphi}_{\beta}$$
is smooth outside $D$, has conic singularities along each $D_{\lambda}$ with cone angle $2 \pi \beta a_{\lambda}$ (say if $\bar{X}$ is smooth, otherwise this will be true only after a finite cover) and one has $\operatorname{Ric} \widehat{\omega}_{\beta}=-\widehat{\omega}_{\beta}$ on $X=\bar{X} \backslash D$, cf e.g. [GP16]. In particular, we have as currents
$$\operatorname{Ric} \widehat{\omega}_{\beta}=-\widehat{\omega}_{\beta}+\sum_{\lambda=1}^{N}\left(1-\beta a_{\lambda}\right)\left[D_{\lambda}\right] .$$
1.5. Main result. The aim of this section is to prove the following result.

Theorem 1.1. The conic Kähler-Einstein metrics $\widehat{\omega}_{\beta}$ solution of (1.5) converge to $\omega_{\mathrm{KE}}$ when $\beta \rightarrow 0$, both weakly as currents on $\bar{X}$ and locally smoothly on $X$.

Proof. We divide the proof in three steps. In the first two steps, we assume that $\Gamma$ is neat so that $\bar{X}$ is a smooth manifold. In the last step, we will explain how to work with the finite quotient singularities that $\bar{X}$ has in general.

Step 1. Weak convergence.
Let $\beta \in\left[0, \frac{1}{2}\right]$ and let $\tau_{\beta} \in(0,1]$ be a number to be determined later. We set
$$\widehat{\psi}_{\beta}:=\frac{1}{1-\beta} \cdot\left(\widehat{\varphi}_{\beta}+\tau_{\beta}\right)$$
this is a $\frac{1}{1-\beta} \cdot(\chi-\beta \widetilde{\theta})$-psh function with finite energy (even bounded if $\beta>0$ ) satisfying the Monge-Ampère equation
$$\left(\frac{1}{1-\beta} \cdot(\chi-\beta \widetilde{\theta})+d d^{c} \widehat{\psi}_{\beta}\right)^{n}=e^{(1-\beta) \widehat{\psi}_{\beta}+F_{\beta}} \cdot \frac{d V}{|s|_{h}^{2}}$$
where $F_{\beta}=\beta \sum_{\lambda} a_{\lambda} \log \left|s_{\lambda}\right|_{h_{\lambda}}^{2}-n \log (1-\beta)-\tau_{\beta}$. We claim that for any $\beta^{\prime}>\beta$ small enough, one has
$$\frac{1}{1-\beta^{\prime}} \cdot\left(\chi-\beta^{\prime} \tilde{\theta}\right)+d d^{c} \widehat{\psi}_{\beta} \geqslant 0 .$$
This follows from the identity
$$\frac{1-\beta}{1-\beta^{\prime}} \cdot\left(\chi-\beta^{\prime} \widetilde{\theta}\right)=(\chi-\beta \widetilde{\theta})+\frac{\beta^{\prime}-\beta}{1-\beta^{\prime}} \cdot \underbrace{(\chi-\widetilde{\theta})}_{>0} .$$
More precisely, we get
$$\begin{aligned}
\left(\frac{1}{1-\beta^{\prime}} \cdot\left(\chi-\beta^{\prime} \widetilde{\theta}\right)+d d^{c} \widehat{\psi}_{\beta}\right)^{n} & \geqslant(1-\beta)^{-n}\left(\frac{1-\beta}{1-\beta^{\prime}} \cdot\left(\chi-\beta^{\prime} \widetilde{\theta}\right)+d d^{c} \widehat{\varphi}_{\beta}\right)^{n} \\
& \geqslant(1-\beta)^{-n}\left(\chi-\beta \widetilde{\theta}+d d^{c} \widehat{\varphi}_{\beta}\right)^{n} \\
& =e^{\left(1-\beta^{\prime}\right) \widehat{\psi}_{\beta}+F_{\beta^{\prime}}+H_{\beta^{\prime}, \beta}} \cdot \frac{d V}{|s|_{h}^{2}}
\end{aligned}$$
where $H_{\beta^{\prime}, \beta}=\left(\beta^{\prime}-\beta\right)\left(\widehat{\psi}_{\beta}-\log |s|^{2}\right)-n \log \left(\frac{1-\beta}{1-\beta^{\prime}}\right)-\tau_{\beta}+\tau_{\beta^{\prime}}$.
If we first choose $\beta=0, \tau_{\beta^{\prime}}=C \beta^{\prime}-n \log \left(1-\beta^{\prime}\right)$ where $C>0$ is a constant such that $\varphi \geqslant \log |s|_{h}^{2}-C$, whose existence is guaranteed by (1.3), then we see that $H_{\beta^{\prime}, 0} \geqslant 0$ so that $\widehat{\varphi}=\widehat{\psi}_{0}$ is a subsolution of (1.6), hence the comparison principle yields
$$\frac{1}{1-\beta} \cdot \widehat{\varphi}_{\beta}+\frac{C \beta-n \log (1-\beta)}{1-\beta} \geqslant \widehat{\varphi}$$
Using the inequality above, we conclude that there is a constant $C^{\prime}>0$ such that $\widehat{\psi}_{\beta} \geqslant \log |s|^{2}-C^{\prime}$ for any $\beta$. Then we set $\tau_{\beta}:=C^{\prime} \beta-n \log (1-\beta)$ and it follows that $H_{\beta^{\prime}, \beta} \geqslant 0$. In other words, $\widehat{\psi}_{\beta}$ is a subsolution of the Monge-Ampère equation satisfied by $\hat{\psi}_{\beta^{\prime}}$, hence
$$\widehat{\psi}_{\beta^{\prime}} \geqslant \widehat{\psi}_{\beta} .$$

The family $\left(\widehat{\psi}_{\beta}\right)_{\beta>0}$ is a decreasing family of quasi-psh functions with complex Hessian uniformly bounded from below. It follows that they converge when $\beta$ approaches zero to a $\chi$-psh function $\widetilde{\varphi}$. It follows from (1.9) that $\widetilde{\varphi}$ has finite energy, is locally bounded on $X$ has satisfies
$$\left(\chi+d d^{c} \widetilde{\varphi}\right)^{n}=\frac{e^{\widetilde{\varphi}} d V}{|s|^{2}}$$
on $X$ by Bedford-Taylor theory, hence also globally on $\bar{X}$. By uniqueness of such a solution (cf e.g. [BG14, Prop. 4.1]), we get $\widetilde{\varphi}=\widehat{\varphi}$, which proves the first part of the proposition.

Step 2. Smooth convergence locally on $X$.
We apply Chern-Lu inequality to the identity map from $\left(X, \widehat{\omega}_{\beta}\right)$ to $(X, \chi)$, cf e.g. [Rub14, Proposition 7.1]. As Ric $\widehat{\omega}_{\beta}=-\widehat{\omega}_{\beta}$ and the bisectional curvature of $(X, \chi)$ is bounded from above, there is a constant $A>0$ such that
$$\Delta_{\widehat{\omega}_{\beta}} \log \operatorname{tr}_{\widehat{\omega}_{\beta}} \chi \geqslant-A\left(1+\operatorname{tr}_{\widehat{\omega}_{\beta}} \chi\right) .$$
Next, we have
$$\begin{aligned}
\Delta_{\widehat{\omega}_{\beta}}\left(-\widehat{\varphi}_{\beta}\right) & =\operatorname{tr}_{\widehat{\omega}_{\beta}} \chi-n-\varepsilon \operatorname{tr}_{\widehat{\omega}_{\beta}} \widetilde{\theta} \\
& =\operatorname{tr}_{\widehat{\omega}_{\beta}} \chi-n+\varepsilon\left[\operatorname{tr}_{\widehat{\omega}_{\beta}}(\chi-\widetilde{\theta})-\operatorname{tr}_{\widehat{\omega}_{\beta}} \chi\right] \\
& \geqslant(1-\beta) \operatorname{tr}_{\widehat{\omega}_{\beta}} \chi-n
\end{aligned}$$
and, if $|\widetilde{s}|^{2}:=\prod\left|s_{\lambda}\right|_{h_{\lambda}}^{2 a_{\lambda}}$,
$$\begin{aligned}
\Delta_{\widehat{\omega}_{\beta}} \log |\widetilde{s}|^{2} & =\operatorname{tr}_{\widehat{\omega}_{\beta}}(-\widetilde{\theta}) \\
& =\operatorname{tr}_{\widehat{\omega}_{\beta}}(\chi-\widetilde{\theta})-\operatorname{tr}_{\widehat{\omega}_{\beta}} \chi \\
& \geqslant-\operatorname{tr}_{\widehat{\omega}_{\beta}} \chi
\end{aligned}$$
Fix some number $\delta \in\left(0, \frac{1}{4}\right)$; it follows from the previous inequalities that the following holds on $X$
$$\Delta_{\widehat{\omega}_{\beta}}\left[\log \operatorname{tr}_{\widehat{\omega}_{\beta}} \chi-(A+1) \widehat{\varphi}_{\beta}+\delta \log |\widetilde{s}|^{2}\right] \geqslant(1-(A+1) \beta-\delta) \operatorname{tr}_{\widehat{\omega}_{\beta}} \chi-B$$
where $B=(n+1) A+n$. Up to decreasing $\beta$, one can assume without loss of generality that $(A+1) \beta \leqslant 1 / 2$ so that $(1-(A+1) \beta-\delta) \geqslant \frac{1}{4}$. Set $H_{\beta, \delta}:=$ $\log \operatorname{tr}_{\widehat{\omega}_{\beta}} \chi-(A+1) \widehat{\varphi}_{\beta}+\delta \log |\widetilde{s}|^{2}$; it is a smooth function on $X$ which tends to $-\infty$ near $D$ thanks to (1.3)-(1.9). At its maximum $x_{\beta, \delta} \in X \backslash D$, one has $\operatorname{tr}_{\widehat{\omega}_{\beta}} \chi\left(x_{\beta, \delta}\right) \leqslant 4 B$. Therefore, one has, for any $x \in X$
$$\begin{aligned}
\log \operatorname{tr}_{\widehat{\omega}_{\beta}} \chi(x) & =H_{\beta, \delta}(x)+(A+1) \widehat{\varphi}_{\beta}(x)-\delta \log |\widetilde{s}|^{2}(x) \\
& \leqslant H_{\beta, \delta}\left(x_{\delta, \beta}\right)+(A+1) \widehat{\varphi}_{\beta}(x)-\delta \log |\widetilde{s}|^{2}(x) \\
& \leqslant \log 4 B+\left[\delta \log |\widetilde{s}|^{2}-(A+1) \widehat{\varphi}_{\beta}\right]\left(x_{\beta, \delta}\right)+(A+1) \widehat{\varphi}_{\beta}(x)-\delta \log |\widetilde{s}|^{2}(x) \\
& \leqslant C_{\delta}-\delta \log |\widetilde{s}|^{2}(x)
\end{aligned}$$
where we used the fact that $\widehat{\varphi}_{\beta}$ is uniformly bounded above (e.g. (1.10)) and $\widehat{\varphi}_{\beta} \geqslant-(n+2) \log (-\log |s|)+O(1)$ by (1.9). As a result, we get
$$\chi \leqslant \frac{C_{\delta}}{|\widetilde{s}|^{2 \delta}} \cdot \widehat{\omega}_{\beta}$$
uniformly on $X$, for any $\delta \in(0,1 / 4)$. From the Monge-Ampère equation satisfied by $\widehat{\omega}_{\beta}$ and the fact that $\chi$ is a smooth Kähler form on $X$, we deduce that given any compact subset $V \Subset X$, there is a constant $C_{V}$ independent of $\beta$ such that
$$\sup _{V}\left|\Delta_{\chi} \widehat{\varphi}_{\beta}\right| \leqslant C_{V} .$$
Using standard bootstrapping arguments, we get uniform bounds on the higher derivatives of $\varphi_{\beta}$ on compact subsets of $X$, which ends the proof of the theorem in the case where $\Gamma$ is neat.

Step 3. General case when $\Gamma$ is not neat.
Let $\Gamma^{\prime}<\Gamma$ be a neat, finite index sub-lattice. The quotient $Y=\Gamma^{\prime} \backslash \Omega$ admits a smooth toroidal compactification $\left(\bar{Y}, D^{\prime}\right)$, and let $f: \bar{Y} \rightarrow \bar{X}$ be the associated finite cover. Set $m_{\lambda}$ to be the ramification order of $f$ along $D_{\lambda}$, and set $D_{\lambda}^{\prime}=$ $f^{-1}\left(D_{\lambda}\right)$. In summary, one has
$$K_{\bar{Y}}+\sum_{\lambda}\left(1-\beta a_{\lambda} m_{\lambda}\right) D_{\lambda}^{\prime}=f^{*}\left(K_{\bar{X}}+\sum_{\lambda}\left(1-\beta a_{\lambda}\right) D_{\lambda}\right) .$$
The Kähler-Einstein metrics $\widehat{\omega}_{\beta}^{\prime}:=f^{*} \widehat{\omega}_{\beta}$ have cone singularities along $D^{\prime}$ with cone angle $2 \pi\left(1-\beta a_{\lambda} m_{\lambda}\right)$ along $D_{\lambda}^{\prime}$. That is, they satisfy Ric $\widehat{\omega}_{\beta}^{\prime}=-\widehat{\omega}_{\beta}^{\prime}+$ $\sum_{\lambda}\left(1-\beta a_{\lambda} m_{\lambda}\right)\left[D_{\lambda}^{\prime}\right]$. Thanks to Steps 1-2 above, $\widehat{\omega}_{\beta}^{\prime}$ converge globally weakly on $\bar{Y}$ and locally smoothly on $Y$ towards the hyperbolic metric $Y$. Of course, one needs to perform a harmless adjustment by replacing $\chi$ with $f^{*} \chi$. Since the hyperbolic metric on $Y$ is nothing but $f^{*} \omega_{\mathrm{KE}}, \mathrm{cf}$. § 1.2, the theorem follows immediately. \(\square\)

\section*{2. The Calabi ansatz}

We now construct some explicit model Kähler metrics in the total space of a holomorphic line bundle $L$ over $D$. This technique goes back to Calabi [Cal79].

Model Setup. Let $D$ be a compact Kähler manifold equipped with a Kähler form $\theta_{D}$ and let ( $L, h$ ) be a Hermitian holomorphic line bundle over $D$. We make the following assumptions:
\begin{itemize}
\item[(i)] $\operatorname{Ric}\left(\theta_{D}\right)=0$.
\item[(ii)] $i \Theta(L, h)=\sigma \theta_{D}, \quad \sigma= \pm 1$.
\end{itemize}

We think of $L$ as the normal bundle of $D$ which will be a divisor in a compact complex manifold $X$. The case $\sigma=-1$ corresponds to a quotient of a ball: in that case $D$ will be a torus. The case $\sigma=1$ corresponds to that of an anticanonical divisor in a Fano manifold $X$.

We consider the function $t=\log \|v\|_{h}^{2}$ defined on $L \backslash D$, the complement of the zero section in the total space of $L$. We also have on $L \backslash D$ a connection

1-form $\eta$ which coincides on each fibre of $L$ with the angular form $d \theta$, and satisfies
$$d \eta=-i p^{*} \Theta(L, h)=-\sigma p^{*} \theta_{D},$$
where $p$ is the projection $p: L \rightarrow D$. Then $\xi=\frac{1}{2} d t+i \eta$ is a (1,0)-form on $L \backslash D$, coinciding with $\frac{d z}{z}$ in each fibre. In particular, $d t \wedge \eta=i \xi \wedge \bar{\xi}$ coincides with $\frac{i d z \wedge d \bar{z}}{|z|^{2}}$ in each fiber. In the following, one will identify $p^{*} \theta_{D}$ with $\theta_{D}$ and view the latter as a (1,1)-form on the total space $L$.

We are looking for a Kähler metric $\omega=i \partial \bar{\partial} \varphi$ on $L \backslash D$ whose Kähler potential $\varphi=\varphi(t)$ only depends on $t$ and such that
$$\operatorname{Ric}(\omega)=\sigma \omega .$$

One can compute the coefficients of the metric in the frame introduced above as follows. First, $d^{c} \varphi=\frac{1}{i}(\partial-\bar{\partial}) \varphi=2 \varphi^{\prime}(t) \eta$ and, then the associated Kähler form is
$$\omega=i \partial \bar{\partial} \varphi=\frac{1}{2} d d^{c} \varphi=\varphi^{\prime \prime} d t \wedge \eta-\sigma \varphi^{\prime} \theta_{D} .$$
In particular, we have as necessary conditions
$$\varphi^{\prime \prime}>0 \quad \text { and } \quad-\sigma \varphi^{\prime}>0 .$$
Let $\omega$ be a (maybe local) parallel ( $n-1,0$ ) form on $D$, then $\Omega=\xi \wedge \omega$ satisfies $d \Omega=i d \eta \wedge \omega=0$, so $\Omega$ is holomorphic. Moreover, up to some positive constant, $|\Omega|^{-2}=\left(-\sigma \varphi^{\prime}\right)^{n-1} \varphi^{\prime \prime}$. As Ric $\omega=i \partial \bar{\partial} \log |\Omega|^{2}$, in order for $\omega$ to be a solution of (2.1), it is enough to see that $\varphi$ is a solution of the following equation
$$\left(-\sigma \varphi^{\prime}\right)^{n-1} \varphi^{\prime \prime}=c e^{-\sigma \varphi}$$
for some constant $c>0$. This can be integrated into
$$\left(-\sigma \varphi^{\prime}\right)^{n+1}=a-b \sigma e^{-\sigma \varphi}$$
for constants $a \in \mathbb{R}$ and $b=(n+1) c>0$.
As we shall see, the solutions $\varphi(t)$ will be defined on intervals of the form $\left(-\infty, t_{0}\right)$ for some arbitrary constant $t_{0} \in \mathbb{R}$, and they will satisfy $\sigma \varphi(t) \rightarrow \infty$ when $t \rightarrow-\infty$, that is when we go to the divisor $D$. It follows that $a \geq 0$ and actually $\varphi(t) \sim-\sigma a^{\frac{1}{n+1}} t$ when $t \rightarrow-\infty$, which says that $\omega$ extends over $D$ with $\left.\omega\right|_{D}=a^{\frac{1}{n+1}} \theta_{D}$. Coming back to the equation (2.4) we obtain the first terms of the expansion of $\varphi$ when $t \rightarrow-\infty$, for some constant $\varphi_{0}$ :
$$\varphi(t) \sim-\sigma a^{\frac{1}{n+1} t}+\varphi_{0}+\frac{b}{(n+1) a} e^{-\sigma \varphi_{0}+a^{\frac{1}{n+1} t}}+\cdots$$
which shows that $\omega$ has actually a conical singularity around $D$ with angle $2 \pi a^{\frac{1}{n+1}}$, so the angle goes to zero when $a \rightarrow 0$, this is the limit we want to study.

Observe that if we have a solution $\varphi_{1}(t)$ of equation (2.4) with $a=b=1$, then $\varphi_{1}(\beta t)+\varphi_{0}$ is still a solution with $a=\beta^{n+1}$ and $b=\beta^{n+1} e^{\sigma \varphi_{0}}$. We use this remark to produce our model families ( $\varphi_{\beta}(t)$ ) with angle $2 \pi \beta$ degenerating to
zero:
Negative case.
(i) The potential $\varphi_{1}$.
This is when $\sigma=-1$. The function $\varphi_{1}$ satisfies $\left(\varphi_{1}^{\prime}\right)^{n+1}=1+e^{\varphi_{1}}$ so we can take as solution $\varphi_{1}(t)=F_{-}^{-1}(t):(-\infty, 0) \rightarrow \mathbb{R}$ with $F_{-}: \mathbb{R} \rightarrow(-\infty, 0)$ defined by
$$F_{-}(x)=-\int_{x}^{+\infty} \frac{d x}{\left(1+e^{x}\right)^{\frac{1}{n+1}}}$$
One can check that the precise behavior of $\varphi_{1}$ at $t=-\infty$ is given by
$$\varphi_{1}(t)=t+I_{n}+\frac{e^{I_{n}}}{n+1} \cdot e^{t}+O\left(e^{2 t}\right) \quad \text { when } t \rightarrow-\infty,$$
where the constant $I_{n}$ is defined by
$$I_{n}:=\int_{0}^{+\infty} \frac{d u}{\left(e^{u}+1\right)^{\frac{1}{n+1}}}-\int_{-\infty}^{0} \frac{\left(e^{u}+1\right)^{\frac{1}{n+1}}-1}{\left(e^{u}+1\right)^{\frac{1}{n+1}}} d u$$
while at $t=0^{-}$, one has
$$\varphi_{1}(t)=-(n+1) \log \left(\frac{-t}{n+1}\right)+\frac{1}{n+2} \cdot\left(\frac{-t}{n+1}\right)^{n+1}+O\left(t^{2(n+1)}\right) \quad \text { when } t \rightarrow 0^{-} .$$
(ii) Degeneration.
We choose to fix $b=1$ by taking
$$\varphi_{\beta}(t)=\varphi_{1}(\beta t)+(n+1) \log \beta .$$
When $\beta \rightarrow 0$, (2.8) implies that $\varphi_{\beta}(t) \rightarrow-(n+1) \log \left(\frac{-t}{n+1}\right)$ which is the Kähler potential of the hyperbolic cusp.

Positive case.
(i) The potential $\varphi_{1}$.
In the positive case, $\sigma=1$. The function $\varphi_{1}$ satisfies $\left(-\varphi_{1}^{\prime}\right)^{n+1}=1-e^{-\varphi_{1}}$ and we take $\varphi_{1}(t)=F_{+}^{-1}(-t):(-\infty, 0) \rightarrow \mathbb{R}_{+}$with $F_{+}: \mathbb{R}_{+} \rightarrow \mathbb{R}_{+}$by
$$F_{+}(x)=\int_{0}^{x} \frac{d x}{\left(1-e^{-x}\right)^{\frac{1}{n+1}}}$$
Again, one can obtain the precise behavior of $\varphi_{1}$ at $t=-\infty$ as
$$\varphi_{1}(t)=-t-J_{n}+\frac{e^{J_{n}}}{n+1} \cdot e^{t}+O\left(e^{2 t}\right) \quad \text { when } t \rightarrow-\infty,$$
where the constant $J_{n}$ is defined by
$$I_{n}:=\int_{0}^{+\infty} \frac{1-\left(1-e^{-u}\right)^{\frac{1}{n+1}}}{\left(1-e^{-u}\right)^{\frac{1}{n+1}}} d u$$
while at $t=0^{-}$, one has
$$\varphi_{1}(t)=c_{n}(-t)^{1+\frac{1}{n}}\left(1+O\left((-t)^{1+\frac{1}{n}}\right) \quad \text { when } t \rightarrow 0^{-},\right.$$
where $c_{n}=\left(\frac{n}{n+1}\right)^{\frac{n+1}{n}}$.
(ii) Degeneration.
We now choose the degeneration
$$\varphi_{\beta}(t)=\varphi_{1}(\beta t) .$$
Here the limit when $\beta \rightarrow 0$ is just 0 . More precisely, the asymptotics (2.11) imply that when $\beta \rightarrow 0$ one has
$$\varphi_{\beta}(t) \sim\left(\frac{-n \beta t}{n+1}\right)^{1+\frac{1}{n}} .$$
Therefore the rescaling $\beta^{-1-\frac{1}{n}} \varphi_{\beta}$ converges to $\left(-\frac{n t}{n+1}\right)^{1+\frac{1}{n}}$ which is the Kähler potential of a Ricci flat metric on $L \backslash D$, the Tian-Yau metric: it gives the asymptotic behaviour of the Tian-Yau metric of $X \backslash D$ near $D$.

We have seen a limit of $\varphi_{\beta}(t)$ when $\beta \rightarrow 0$ on each compact set in $t$. To understand the global geometry of our models, we write from (2.2)
$$\omega_{\beta}=i \partial \bar{\partial} \varphi_{\beta}=\beta^{2} \varphi_{1}^{\prime \prime}(\beta t) d t \wedge \eta-\beta \sigma \varphi_{1}^{\prime}(\beta t) \theta_{D} .$$
The geometry is clear when one writes the associated Riemannian metric $g_{\beta}$, after the change of variable $u=\beta t \in(-\infty, 0)$ :
$$g_{\beta}=2 \varphi_{1}^{\prime \prime}(u)\left(\frac{1}{4} d u^{2}+\beta^{2} \eta^{2}\right)-\beta \sigma \varphi_{1}^{\prime}(u) g_{D} .$$
The geometry collapses at speed $\sqrt{\beta}$ in the directions of $D$, and $\beta$ in the circle directions. Observe that, up to a multiplicative constant, we have when $u \rightarrow 0$ the asymptotics $\varphi_{1}^{\prime \prime}(u) \sim u^{-2}$ in the negative case, and $u^{-1+\frac{1}{n}}$ in the positive case, from which it follows that the diameter is infinite in the negative case and bounded in the positive case (as it should by Myers's theorem). More precisely, we have at $u=0$ the following asymptotics
$$\varphi_{1}^{\prime}(u)=-c_{n}^{\prime}(-u)^{\frac{1}{n}}+O\left((-u)^{1+\frac{2}{n}}\right), \quad \varphi_{1}^{\prime \prime}(u)=\frac{c_{n}^{\prime}}{n}(-u)^{-1+\frac{1}{n}}+O\left((-u)^{\frac{2}{n}}\right) .$$
with $c_{n}^{\prime}=\left(\frac{n}{n+1}\right)^{\frac{1}{n}}$.
To see the behaviour of the metric near the divisor $D$, we consider the expansion at $u=-\infty$ given as in (2.5) by
$$\varphi_{1}^{\prime}(u)=-\sigma+\frac{1}{n+1} e^{u}+O\left(e^{2 u}\right)$$
from which follows, taking $r=e^{\frac{u}{2}} \in(0,1)$,
$$\begin{aligned}
g_{\beta} & =\frac{2}{n+1} e^{u}\left(\frac{1}{4} d u^{2}+\beta^{2} \eta^{2}\right)+\beta g_{D}+O\left(e^{u}\right) \\
& =\frac{2}{n+1}\left(d r^{2}+\beta^{2} r^{2} \eta^{2}\right)+\beta g_{D}+O\left(r^{2}\right),
\end{aligned}$$
where the $O\left(r^{2}\right)$ is with respect to $g_{\beta}$ and is uniform with respect to $\beta$.

\section*{3. Curvature calculations}

We now calculate the curvature of our model metrics $\omega_{\beta}$ on $L \backslash D$. This gives a control of the local geometry and will be also used in the Laplacian estimate.

The Kähler metric $\omega=i \partial \bar{\partial} \varphi$ induces a hermitian metric $h$ on the bundle $\Omega^{1,0}$ of $(1,0)$-forms on $L \backslash D$, and it will be convenient to compute its Chern curvature tensor $F^{\Omega^{1,0}}$. At this point, we take an arbitrary Kähler potential $\varphi=\varphi(t)$. We will use the $\mathcal{C}^{\infty}$ orthogonal splitting
$$\Omega^{1,0}=\mathbb{C} \xi \oplus p^{*} \Omega_{D}^{1,0}$$
From (2.2) we see that the Hermitian metric preserves this decomposition, and is equal to
$$h=\left(\begin{array}{cc}
\left(\varphi^{\prime \prime}\right)^{-1} & \\
& \left(-\sigma \varphi^{\prime}\right)^{-1} h^{\Omega_{D}^{1,0}}
\end{array}\right) .$$
where $h^{\Omega_{D}^{1,0}}$ is the hermitian metric induced on $\Omega_{D}^{1,0}$ by the Kähler metric $\theta_{D}$. From $d \xi=i d \eta=-i \sigma \theta_{D}$ we deduce the $\bar{\partial}$ and $\partial$ operators of $\Omega^{1,0}$ in this splitting:
$$\bar{\partial}=\left(\begin{array}{cc}
\bar{\partial} & 0 \\
a & \bar{\partial}_{D}^{1,0}
\end{array}\right), \quad \partial=\left(\begin{array}{cc}
\partial-\partial \log \varphi^{\prime \prime} & -\frac{\varphi^{\prime \prime}}{-\sigma \varphi^{\prime}} a^{*} \\
0 & \partial^{\Omega_{D}^{1,0}}-\partial \log \left(-\sigma \varphi^{\prime}\right)
\end{array}\right)$$
Here $a$ is the ( 0,1 )-form with values in $\operatorname{Hom}\left(\mathbb{C}, \Omega_{D}^{1,0}\right)=\Omega_{D}^{1,0}$ defined by $a_{X}=$ $X\lrcorner d \xi=-i \sigma X\lrcorner \theta_{D}$, and $a^{*}$ its adjoint $\left.a_{X}^{*} \alpha=-i \sigma \Lambda(\alpha \wedge(X\lrcorner \theta)\right)$. The familiar form for the curvature is then
$$F^{\Omega^{1,0}}=\left(\begin{array}{cc}
\partial \bar{\partial} \log \varphi^{\prime \prime}-\frac{\varphi^{\prime \prime}}{-\sigma \varphi^{\prime}} a^{*} \wedge a & -\bar{\partial}\left(\frac{\varphi^{\prime \prime}}{-\sigma \varphi^{\prime}} a^{*}\right) \\
\partial^{h} a & \partial \bar{\partial} \log \varphi^{\prime}+F^{\Omega_{D}^{1,0}}-\frac{\varphi^{\prime \prime}}{-\sigma \varphi^{\prime}} a \wedge a^{*}
\end{array}\right)$$
so that $i F^{\Omega^{1,0}}$ is given by
$$\left(\begin{array}{cc}
\left(\log \varphi^{\prime \prime}\right)^{\prime \prime} i \xi \wedge \bar{\xi}-\sigma\left(\log \frac{\varphi^{\prime \prime}}{-\sigma \varphi}\right)^{\prime} \theta_{D} & -i\left(\frac{\varphi^{\prime \prime}}{-\sigma \varphi}\right)^{\prime} \bar{\xi} \wedge a^{*} \\
i \log \left(\frac{\varphi^{\prime \prime}}{-\sigma \varphi^{\prime}}\right)^{\prime} \xi \wedge a & \log \left(-\sigma \varphi^{\prime}\right)^{\prime \prime} i \xi \wedge \bar{\xi}-\sigma \log \left(-\sigma \varphi^{\prime}\right)^{\prime}\left(\theta_{D}+\Theta_{D}\right)+i F^{\Omega_{D}^{1,0}}
\end{array}\right)$$
where the last $\Theta_{D}$ is the 2-form with values in the endomorphisms of $\Omega_{D}^{1,0}$ defined by $\left.\left.\left(\Theta_{D}\right)_{X, Y}(\alpha)=-(X\lrcorner \alpha\right)(Y\lrcorner \theta_{D}\right)$ for $X \in T^{1,0}$ and $Y \in T^{0,1}$.

Lemma 3.1. One has the following bounds for the curvature of the model Kähler metric $\omega_{\beta}$ defined in (2.14):
\begin{itemize}
\item[-] in the negative case $(\sigma=-1)$, if $D$ is flat, then the curvature is bounded;
\item[-] in the positive case $(\sigma=1)$, the curvature is bounded by
$$\operatorname{cst} .\left(\frac{1}{1-e^{-\varphi_{\beta}}}+\frac{1}{\beta\left(1-e^{-\varphi_{\beta}}\right)^{\frac{1}{n+1}}}\right) .$$
\end{itemize}
Proof. For now, $\omega=i \partial \bar{\partial} \varphi$ is still arbitrary, and only at the end we will choose $\varphi:=\varphi_{\beta}$ to be the potential constructed by the Calabi Ansatz above. Let $X=$
$\lambda \xi^{*}+v$ with $\lambda \in \mathbb{C}, v \in T_{D}^{1,0}$ and $Y=\mu \xi+\alpha$ with $\mu \in \mathbb{C}, \alpha \in \Omega_{D}^{1,0}$. We assume that $\|\xi\|_{\omega}=\|Y\|_{h}=1$, so that
$$|\lambda|^{2} \leqslant \frac{1}{\varphi^{\prime \prime}},\|v\|_{\theta_{D}}^{2} \leqslant \frac{1}{-\sigma \varphi^{\prime}}, \quad \text { and } \quad|\mu|^{2} \leqslant \varphi^{\prime \prime},\|\alpha\|_{h_{D}}^{2} \leqslant-\sigma \varphi^{\prime}$$
where $h_{D}$ is the metric on $\Omega_{D}^{1,0}$ induced by $\theta_{D}$. The hermitian matrix $h \cdot i F_{X, \bar{X}}^{\Omega^{1,0}}$ is equal to
$$\left(\begin{array}{cc}
|\lambda|^{2} \frac{\left(\log \phi^{\prime \prime}\right)^{\prime \prime}}{\varphi^{\prime \prime}}-\frac{\sigma\|v\|_{\theta_{D}}}{\varphi^{\prime \prime}} \log \left(\frac{\varphi^{\prime \prime}}{-\sigma \varphi^{\prime}}\right)^{\prime} & -i \bar{\lambda} a_{v}^{*}-\frac{1}{-\sigma \varphi} \log \left(\frac{\varphi^{\prime \prime}}{-\sigma \varphi \varphi^{\prime}}\right)^{\prime} \\
i \lambda a_{\bar{v}} \frac{1}{-\sigma \varphi^{\prime}} \log \left(\frac{\varphi^{\prime \prime}}{-\sigma \varphi}\right)^{\prime} & \frac{\log \left(-\sigma \varphi^{\prime}\right)^{\prime \prime}}{-\sigma \varphi^{\prime}}|\lambda|^{2}+\frac{\log (-\sigma \varphi)^{\prime}}{\varphi^{\prime}}\left(\theta_{D}+\Theta_{D}\right)_{v, \bar{v}}+\frac{i}{-\sigma \varphi^{\prime}} \Gamma_{v, \bar{v}}^{1,0}
\end{array}\right)$$
As a result, the expansion of $\left\langle i F_{X, \bar{X}}^{\Omega^{1,0}} \Upsilon, Y\right\rangle_{h}$ involves the following terms
$$\begin{gathered}
|\lambda \mu|^{2} \frac{\left(\log \varphi^{\prime \prime}\right)^{\prime \prime}}{\varphi^{\prime \prime}},|\mu|^{2} \frac{\|v\|_{\theta_{D}}^{2}}{\varphi^{\prime \prime}}\left(\log \left(\frac{\varphi^{\prime \prime}}{-\sigma \varphi^{\prime}}\right)^{\prime}, \lambda \bar{\mu}\left\langle a_{\bar{v}}, \alpha\right\rangle_{h_{D}} \log \left(\frac{\varphi^{\prime \prime}}{-\sigma \varphi^{\prime}}\right)^{\prime}\right. \\
|\lambda|^{2}\|\alpha\|_{h_{D}}^{2} \frac{\log \left(-\sigma \varphi^{\prime}\right)^{\prime \prime}}{-\sigma \varphi^{\prime}},\|\alpha\|_{h_{D}}^{2} \frac{\log \left(-\sigma \varphi^{\prime}\right)^{\prime}}{\varphi^{\prime}}\left(\theta_{D}+\Theta_{D}\right)_{v, \bar{v}}, \frac{1}{\varphi^{\prime}}\left\langle i F_{v, \bar{v}}^{\Omega_{D}^{1,0}} \alpha, \alpha\right\rangle_{h_{D}} .
\end{gathered}$$
Given the bounds (3.2), we see that we need to bound the quantities
$$\frac{\left(\log \varphi^{\prime \prime}\right)^{\prime \prime}}{\varphi^{\prime \prime}}, \quad \frac{\log \left(-\sigma \varphi^{\prime}\right)^{\prime \prime}}{\varphi^{\prime \prime}}, \quad \frac{\left(\log \varphi^{\prime \prime}\right)^{\prime}}{\varphi^{\prime}}, \quad \frac{\log \left(-\sigma \varphi^{\prime}\right)^{\prime}}{\varphi^{\prime}},$$
while the term $F^{\Omega_{D}^{1,0}}$ (present only in the positive case) is bounded by $\frac{\text { cst. }}{-\sigma \varphi^{\prime}}$.
Up to an additive constant, we have $\varphi_{\beta}(t)=\varphi_{1}(\beta t)$, so we see that the factors $\beta$ in (3.3) cancel and it is enough to bound these quantities for $\varphi_{1}$, while the term involving the curvature of $D$ is bounded by $\frac{\text { cst. }}{-\beta \varphi_{1}^{\prime}(\beta t)}$. We now use the equation satisfied by $\varphi_{1}$, that is
$$-\sigma \varphi_{1}^{\prime}=\left(1-\sigma e^{-\sigma \varphi_{1}}\right)^{\frac{1}{n+1}}$$
Taking $x=e^{-\sigma \varphi_{1}}$ we obtain $x^{\prime}=x(1-\sigma x)^{\frac{1}{n+1}}$. It is then convenient to write all the quantities in terms of $x$. We have $-\sigma \varphi_{1}^{\prime}=(1-\sigma x)^{\frac{1}{n+1}}$, therefore $-\sigma \varphi_{1}^{\prime \prime}=$ $\frac{1}{n+1} x(1-\sigma x)^{-\frac{n-1}{n+1}}$. Then one calculates all quantities in (3.3):
$$\begin{array}{ll}
\frac{\log \left(-\sigma \varphi_{1}^{\prime}\right)^{\prime}}{\varphi_{1}^{\prime}}=\frac{x}{1-\sigma x}, & \frac{\log \left(-\sigma \varphi_{1}^{\prime}\right)^{\prime \prime}}{\varphi_{1}^{\prime \prime}}=\frac{n+1-\sigma x}{(n+1)(1-\sigma x)}, \\
\frac{\log \left(-\sigma \varphi_{1}^{\prime \prime}\right)^{\prime}}{\varphi_{1}^{\prime}}=\frac{n+1-2 \sigma x}{(n+1)(1-\sigma x)}, & \frac{\log \left(-\sigma \varphi_{1}^{\prime \prime}\right)^{\prime \prime}}{\varphi_{1}^{\prime \prime}}=\frac{-n^{2}+n+2-2 \sigma x}{(n+1)(1-\sigma x)} .
\end{array}$$
If $\sigma=-1$ then $1-\sigma x=1+e^{\varphi} \geq 1$ therefore all these quantities are bounded. If $\sigma=1$ then $1-\sigma x=1-e^{-\varphi}$ and we obtain the bounds in the statement of the lemma. \(\square\)

In the positive case, the divisor $D$ corresponds to $\varphi \rightarrow+\infty$ so the curvature is $O\left(\beta^{-1}\right)$ in all sets of the form $u<-A<0$. At $u=0$ the metric $g_{\beta}$ from (2.15) degenerates, but this part will be cut out since we will glue with the rest of $X$.

\section*{4. Asymptotics of the conical KE metrics on ball quotients}
4.1. Set-up. In this section, we borrow the setup and notation of § 1.1 and we assume additionally that $\Omega=\mathbb{B}^{n}$ is the complex hyperbolic space of dimension $n$. In this section, we assume that $\Gamma$ is neat, so that $X=\Gamma \backslash{ }^{\mathbb{B}}$ can be compactified smoothly by adding finitely many disjoint tori $D_{1}, \ldots, D_{N}$ of dimension $n-1$. In general, this is only true up to the action of a finite group (locally in the neighborhood of each torus). The Kähler-Einstein metric $\omega_{\mathrm{KE}}$ is, up to a normalizing constant, the hyperbolic metric on $X$, described locally near $D$ by (1.1).

It will be important in the following to allow cone angles along $D_{\lambda}$ that are not necessarily of the form $2 \pi \beta a_{\lambda}$ for some given $a_{\lambda}>0$ and a single parameter $\beta>0$ going to zero. For that reason and from now on, we denote by $\beta:=\left(\beta_{1}, \ldots, \beta_{N}\right)$ a $N$-tuple of positive numbers. Since the components $D_{1}, \ldots, D_{N}$ of the boundary divisor $D$ are disjoint, the divisor $-\sum_{\lambda} a_{\lambda} D_{\lambda}$ is relatively ample for any $a_{\lambda}>0$. In particular, up to changing $h_{\lambda}$ one can find $\delta_{0}>0$ such that $\chi-\delta \theta_{\lambda}$ is semi-positive globally on $\bar{X}$ and Kähler on $X \backslash \sqcup_{\mu \neq \lambda} D_{\mu}$, for any $\delta \leqslant 2 \delta_{0} N$. As a result, $\chi-\sum_{\lambda} a_{\lambda} \theta_{\lambda}$ is globally Kähler on $\bar{X}$ for any $a_{\lambda} \in\left(0,2 \delta_{0}\right]$. In the following, one will assume that $\beta_{\lambda} \leqslant \delta_{0} / 2 N$ for any $\lambda$.

The Kähler-Einstein metric $\widehat{\omega}_{\beta}=\chi-\sum_{\lambda=1}^{N} \beta_{\lambda} \theta_{\lambda}+d d^{c} \widehat{\varphi}_{\beta}$ solution of
$$\operatorname{Ric} \widehat{\omega}_{\beta}=-\widehat{\omega}_{\beta}+\sum_{\lambda=1}^{N}\left(1-\beta_{\lambda}\right)\left[D_{\lambda}\right]$$
for $\|\beta\|$ small enough solves the following Monge-Ampère equation
$$\left(\chi-\sum_{\lambda=1}^{N} \beta_{\lambda} \theta_{\lambda}+d d^{c} \widehat{\varphi}_{\beta}\right)^{n}=\frac{e^{\widehat{\varphi}_{\beta}} d V}{\prod_{\lambda}\left|s_{\lambda}\right|_{h_{\lambda}}^{2\left(1-\beta_{\lambda}\right)}}$$
where $d V$ is a smooth volume form such that $-\operatorname{Ric}(d V)+\sum_{\lambda=1}^{N} \theta_{\lambda}=\chi$.
One can reproduce the arguments in the proof of Theorem 1.1 verbatim to show that $\widehat{\phi}_{\beta}$ almost decreases to $\widehat{\phi}$ when $\beta$ goes to zero. More precisely, one can find a sequence of real numbers $\tau_{\beta} \rightarrow 0$ such that $\frac{1}{1-\delta_{0}^{-1} \sum_{\lambda} \beta_{\lambda}}\left(\widehat{\phi}_{\beta}+\tau_{\beta}\right)$ decreases to $\widehat{\phi}$ when $\beta \searrow 0$ component-wise. The main point is that if $\beta^{\prime}>\beta$ component-wise and if we set $B=\sum \beta_{\lambda}$ (resp. $B^{\prime}=\sum \beta_{\lambda}^{\prime}$ ), we have
$$\begin{aligned}
\frac{1-\delta_{0}^{-1} B}{1-\delta_{0}^{-1} B^{\prime}} \cdot\left(\chi-\sum \beta_{\lambda}^{\prime} \theta_{\lambda}\right)= & \left(\chi-\sum \beta_{\lambda} \theta_{\lambda}\right) \\
& +\frac{B^{\prime}-B}{\delta_{0}-B^{\prime}} \cdot[\chi-\sum_{\lambda} \underbrace{\left(\delta_{0} \beta_{\lambda}+\frac{\delta_{0}-B}{B^{\prime}-B} \cdot\left(\beta_{\lambda}^{\prime}-\beta_{\lambda}\right)\right)}_{\in\left(0,2 \delta_{0}\right)} \cdot \theta_{\lambda}] .
\end{aligned}$$
which replaces the identity (1.8).

Moreover, the Laplacian estimate from the proof of Theorem 1.1 carries over with no significant change, and therefore
$$\widehat{\omega}_{\beta} \underset{\beta \rightarrow 0}{\longrightarrow} \omega_{\mathrm{KE}} \quad \text { in } \quad \mathcal{C}_{\text {loc }}^{\infty}\left(U^{*}\right)$$
4.2. Comparison to the model metric. We now aim to compare the global Kähler-Einstein metric $\widehat{\omega}_{\beta}$ to the model $\omega_{\beta}$ constructed via the Calabi Ansatz in § 2. One

Given any torus $D \in\left\{D_{1}, \ldots, D_{N}\right\}$, one can identify an open neighborhood $U$ of $D$ in $\bar{X}$ to a neighborhood of the zero section in the total space of the normal bundle $L:=N_{D / \bar{X}} \rightarrow D$. Moreover, $L$ comes naturally equipped with a smooth hermitian metric $h$ such that $\theta_{D}:=\pi \cdot i \Theta\left(L^{-1}, h^{-1}\right)$ is a flat Kähler metric on $D$. We let $p: U \rightarrow D$ be the projection induced by the identification of $U$ to an open subset of the total space of $L$. Under this identification and given a point $(x, v) \in U$ (i.e. $x \in D, v \in L_{x}$ ), we can consider the quantity $\|v\|_{h}^{2}$ and assume that $\|v\|_{h}^{2}<e^{-1}$ on $U$. On $U^{*}:=U \backslash D$, the smooth function $t=\log \|v\|_{h}^{2}: U^{*} \rightarrow(-\infty,-1)$ satisfies
$$i \partial \bar{\partial} t=p^{*} \theta_{D} .$$
Moreover, the Kähler-Einstein metric $\omega_{\mathrm{KE}}$ on $X$ has an exact expression in restriction to $U^{*}$; namely
$$\begin{aligned}
\left.\omega_{\mathrm{KE}}\right|_{U^{*}} & =i \partial \bar{\partial}[-(n+1) \log (-t)] . \\
& =(n+1)\left[\frac{\xi \wedge \bar{\xi}}{(-t)^{2}}+\frac{p^{*} \theta_{D}}{-t}\right]
\end{aligned}$$
where $\xi=\frac{1}{2} d t+i \eta$ has been defined in § 2. We have observed in ibid. that the potential $\varphi(t)=-(n+1) \log (-t)$ of $\omega_{\mathrm{KE}}$ is the limit of the potentials
$$\psi_{\beta}:=\varphi_{\beta}(t)+(n+1) \log (n+1)$$
of $\omega_{\beta}$ (cf. (2.9)) when $\beta \rightarrow 0$ and that the convergence is smooth on the compact subsets of $\bar{U} \backslash D$. In particular, we get
$$\omega_{\beta} \underset{\beta \rightarrow 0}{\longrightarrow} \omega_{\mathrm{KE}} \quad \text { in } \quad \mathcal{C}_{\text {loc }}^{\infty}\left(U^{*}\right) .$$

Let $\Omega=\xi \wedge \omega$ be the holomorphic $n$-form with logarithmic poles along $D$ constructed on $U$ in the previous section.The Monge-Ampère equation solved by $\psi_{\beta}$ reads
$$\left(i \partial \bar{\partial} \psi_{\beta}\right)^{n}=e^{\psi_{\beta}} i^{n^{2}} \Omega \wedge \bar{\Omega} .$$
The Monge-Ampère equation solved by $\widehat{\omega}_{\beta}$ has a similar form. Indeed, let $\psi_{\chi}$ be a smooth potential for $\chi$ on $U$ and let us set $\widehat{\psi}_{\beta}:=\psi_{\chi}-\beta t+\widehat{\varphi}_{\beta}$ which is well-defined on $U^{*}$. Recall that $\widehat{\varphi}_{\beta} \in L^{\infty}\left(U^{*}\right)$ so that $\widehat{\psi}_{\beta}-\varphi_{\beta}$ is globally bounded on $U^{*}$ (only qualitatively at this point). Moreover, we have
$$\left(i \partial \bar{\partial} \widehat{\psi}_{\beta}\right)^{n}=e^{\widehat{\psi}_{\beta}+F_{\beta}} i^{n^{2}} \Omega \wedge \bar{\Omega}$$
where $F_{\beta}$ is a smooth function on $U^{*}$, globally bounded independently of $\beta$, i.e. $\left\|F_{\beta}\right\|_{L^{\infty}\left(U^{*}\right)} \leqslant C_{1}$.

Lemma 4.1. The following bound holds
$$\left\|\widehat{\psi}_{\beta}-\psi_{\beta}\right\|_{L^{\infty}(U)} \leqslant C_{1} .$$
Proof. This is a simple application of the maximum principle. Indeed, let $\delta>0$ arbitrarily small and let $H=H_{\beta, \delta}:=\widehat{\psi}_{\beta}-\varphi_{\beta}+\delta t$. Since $H_{\beta, \delta}$ goes to $-\infty$ along $D$, its maximum is attained at a point $x=x_{\beta, \delta} \in \bar{U} \backslash D$ at which the complex Hessian of $H$ is non-positive. In particular, we get $i \partial \bar{\partial} \widehat{\psi}_{\beta} \leqslant i \partial \bar{\partial} \psi_{\beta}-$ $\delta \theta_{D} \leqslant i \partial \bar{\partial} \psi_{\beta}$ at $x$. Taking the top wedge product and using the Monge-Ampère equations above, we find $H(x) \leqslant-F_{\beta}(x)+\delta t(x) \leqslant C_{1}$. In particular, $H \leqslant C_{1}$ everywhere on $U^{*}$ and passing to the limit when $\delta \rightarrow 0$, we get the first half of (4.7). The other half is obtained in a similar way. \(\square\)

Remark 4.2. In the lemma above, we could have use Bedford-Taylor's comparison principle instead of the maximum principle (with the tweak by $\delta t$ ), see e.g. [CKZ11, Lemma 3.4].

Next, we claim that $\widehat{\omega}_{\beta}$ and $\omega_{\beta}$ are uniformly quasi-isometric on $U^{*}$.
Lemma 4.3. There exists $C_{2}>0$ independent of $\beta$ such that
$$C_{2}^{-1} \omega_{\beta} \leqslant \widehat{\omega}_{\beta} \leqslant C_{2} \omega_{\beta} .$$
Proof. Consider the smooth function
$$H_{\beta}:=\log \operatorname{tr}_{\widehat{\omega}_{\beta}} \omega_{\beta} \quad \text { on } U^{*} .$$
Since Ric $\widehat{\omega}_{\beta}=-\widehat{\omega}_{\beta}$ and the holomorphic bisectional curvature of $\omega_{\beta}$ is bounded above independently of $\beta$ by Lemma 3.1, an application of Chern-Lu formula (see e.g. [Rub14, Proposition 7.1]) yields a constant $B>0$ independent of $\beta$ such that
$$\Delta_{\widehat{\omega}_{\beta}} H_{\beta} \geqslant-1-B e^{H_{\beta}} \quad \text { on } U^{*} .$$
Thanks to (4.3)- (4.6), we have
$$H_{\beta} \leqslant(n+1) \text { on } \partial U$$
for $\beta$ small enough.
Since $\Delta_{\widehat{\omega}_{\beta}}\left(\psi_{\beta}-\widehat{\psi}_{\beta}\right)=e^{H_{\beta}}-n$ and $i \partial \bar{\partial} t \geqslant 0$, we get for any $\delta>0$
$$\Delta_{\omega_{\varepsilon}}\left(H_{\beta}-(B+1) \cdot\left(\psi_{\beta}-\widehat{\psi}_{\beta}\right)+\delta t\right)=e^{H_{\beta}}-n(B+1)-1 .$$
The maximum of the function inside the Laplacian is attained at $x \in \bar{U} \backslash D$. If $x \in \partial U$, then (4.7)-(4.10) and the inequality $t \leqslant 0$ imply that $H_{\beta} \leqslant(n+1)+$ $2(B+1) C_{1}-\delta t$ on $U^{*}$. If $x \in U$, then the maximum principle implies that $H_{\beta} \leqslant(B+1)\left(n+2 C_{1}\right)+1-\delta t$ on $U^{*}$. Passing to the limit when $\delta \rightarrow 0$, one finds $H_{\beta} \leqslant C_{2}$ on $U^{*}$. The result follows (up to enlarging $C_{2}$ ) since the Monge-Ampère of $\omega_{\beta}$ and $\widehat{\omega}_{\beta}$ are commensurable - which itself relies on the estimate (4.7). \(\square\)

Since we know that $\omega_{\beta}$ and $\widehat{\omega}_{\beta}$ are asymptotically close at any order away from $D$, one can improve Lemma 4.3 as follows.

Lemma 4.4. There exists a sequence of numbers $\varepsilon_{\beta} \searrow 0$ such that
$$\left(1-\varepsilon_{\beta}\right) \omega_{\beta} \leqslant \widehat{\omega}_{\beta} \leqslant\left(1+\varepsilon_{\beta}\right) \omega_{\beta} \quad \text { on } U^{*} \text {. }$$
Proof. We introduce for any $\delta>0$ the quantities
$$F_{\beta}:=\log \left(\frac{\widehat{\omega}_{\beta}^{n}}{\omega_{\beta}^{n}}\right) \quad \text { and } \quad F_{\beta, \delta}:=F_{\beta}+\delta t .$$
The function $F_{\beta}$ is bounded on $U$ and smooth away from $D$. If we can show that $F_{\beta}$ converges uniformly to 0 on $U$, then we will be done since we know that $\widehat{\omega}_{\beta}$ and $\omega_{\beta}$ are uniformly quasi-isometric thanks to Lemma 4.3. First, we observe that
$$\lim _{\beta \rightarrow 0}\left\|F_{\beta}\right\|_{L^{\infty}(\partial U)}=0$$
thanks to (4.3)- (4.6). Let $x \in U$ be a point where $F_{\beta, \delta}$ attains its maximum. If $x \in \partial U$, we have $F_{\beta, \delta} \leqslant\left\|F_{\beta}\right\|_{L^{\infty}(\partial U)}$ which goes to zero by (4.12). Otherwise, $x \in U^{*}$ and we have $d d^{c} F_{\beta, \delta}(x) \leqslant 0$. Since both metrics are Kähler-Einstein with the same constant, we have $d d^{c} F_{\beta}=\widehat{\omega}_{\beta}-\omega_{\beta}$. In particular, we get at the point $x$ the following inequality
$$\widehat{\omega}_{\beta}(x) \leqslant \omega_{\beta}(x)-\delta d d^{c} t \leqslant \omega_{\beta}(x)$$
It follows that $F_{\beta}(x) \leqslant 0$, hence $F_{\varepsilon, \delta} \leqslant 0$. Passing to the limit when $\delta \rightarrow 0$, we obtain that in any case, $\sup _{U} F_{\beta} \leqslant o(1)$ when $\beta \rightarrow 0$.

One can proceed similarly with $G_{\beta, \delta}=\log \left(\frac{\omega_{\beta}^{n}}{\hat{\omega}_{\beta}^{n}}\right)+\delta t$ to see that $\inf _{U} F_{\beta} \geqslant$ $o(1)$ when $\beta \rightarrow 0$. The lemma is proved. \(\square\)

To finish this section, we put together the Laplacian estimate (4.11) with the asymptotics (2.6)-(2.8), which yields

Theorem 4.5. The conical Kähler-Einstein metric $\widehat{\omega}_{\beta}$ has the following behavior on $U$ as $\beta$ approaches zero:
\begin{itemize}
\item[-] On $\{\beta t \rightarrow 0\}$, it is quasi-isometric to
$$\omega_{\mathrm{KE}}=(n+1)\left[\frac{i \xi \wedge \bar{\xi}}{(-t)^{2}}+\frac{\theta_{D}}{-t}\right]$$
with quasi-isometry constant converging to 1 as $\beta t \rightarrow 0$.
\item[-] On $\{\beta t \rightarrow-\infty\}$, it is quasi-isometric to
$$a_{n} \beta^{2} \cdot e^{\beta t} i \xi \wedge \bar{\xi}+\beta \theta_{D}$$
with quasi-isometry constant converging to 1 as $\beta t \rightarrow-\infty$ and $\beta \rightarrow 0$ and where $a_{n}=\frac{e^{I_{n}}}{n+1}, I_{n}$ being defined in (2.7).
\end{itemize}
\begin{itemize}
\item[-] Elsewhere, i.e. on $\left\{-C \leqslant \beta t \leqslant C^{-1}\right\}$; it is quasi-isometric to
$$\beta^{2} \cdot e^{\beta t} i \xi \wedge \bar{\xi}+\beta \theta_{D}$$
with quasi-isometry constant uniformly bounded as $\beta \rightarrow 0$.
\end{itemize}

The picture below illustrates the result.
![](https://cdn.mathpix.com/cropped/f774122a-1d15-4317-9d31-f69a2c77c0d9-20.jpg?height=434&width=838&top_left_y=627&top_left_x=642)
4.3. Ramified covers. In Set-up 4.1, assume additionally that $\Gamma$ is arithmetic, so that $\Gamma$ can be realized as the integral points $G(\mathbb{Z})$ of an algebraic group $G$ defined over $\mathbb{Z}$. Given an integer $m \geqslant 1$, the congruence subgroup $\Gamma(m)=$ $\operatorname{Ker}[G(\mathbb{Z}) \rightarrow G(\mathbb{Z} / m \mathbb{Z})]$ induces an étale cover
$$\pi_{m}: \Gamma(m) \backslash \mathbb{B} \rightarrow \Gamma \backslash \mathbb{B} .$$
Let $X_{m}:=\Gamma(m) \backslash \mathbb{B}$ and let $\bar{X}_{m}$ be a log smooth compactification of $X_{m}$. The étale cover $\pi_{m}: X_{m} \rightarrow X$ can be uniquely extended to a cover $\bar{\pi}_{m}: \bar{X}_{m} \rightarrow \bar{X}$. Up to taking a further cover, one can assume that $\bar{\pi}_{m}$ is Galois, with group $\Lambda_{m}$. Moreover, Mumford shows in [Mum77, p270-271] that $\bar{\pi}_{m}$ is highly ramified along $D$ in the following sense. Let $v_{m, \lambda}$ be the ramification order of $\bar{\pi}_{m}$ along $D_{\lambda}$. Then, given any integer $\ell \geqslant 1$, there exists $m=m(\ell)$ such that $\ell \mid v_{m, \lambda}$ for any $\lambda=1, \ldots, N$.

Pick $\ell$ arbitrary large and consider the ramified cover $\bar{\pi}_{m}: \bar{X}_{m} \rightarrow \bar{X}$ for $m=m(\ell)$ as above. Set $\beta_{m}:=\left(\frac{1}{v_{m, 1}}, \ldots, \frac{1}{v_{m, N}}\right)$ and consider the conical Kähler-Einstein metric $\omega_{\beta_{m}}$ with cone angles $2 \pi\left(\beta_{m}\right)_{\lambda}$ along $D_{\lambda}$. By the choice of $\beta_{m}$, $\omega_{\beta_{m}}$ is an orbifold Kähler metric for the pair $\left(X, \sum_{\lambda}\left(1-\frac{1}{v_{m, \lambda}}\right) D_{\lambda}\right)$, hence $\omega_{m}:=$ $\bar{\pi}_{m}^{*} \omega_{\beta_{m}}$ is a genuine Kähler-Einstein metric on the compact Kähler manifold $\bar{X}_{m}$, i.e.
$$\operatorname{Ric} \omega_{m}=-\omega_{m} \quad \text { on } \bar{X}_{m} .$$

As $\ell \rightarrow+\infty$, so does $m$ and $\beta_{m}$ converges to 0, so that $\omega_{\beta_{m}}$ converges to the hyperbolic (Bergman) metric on $X$ by the previous results. Schematically, one can summarize the situation as below
$$\left(\bar{X}_{m}, \omega_{m}\right) / \Lambda_{m} \underset{m \rightarrow+\infty}{\longrightarrow}\left(\Gamma \backslash \mathbb{B}, \omega_{\text {Berg }}\right) .$$

\section*{5. Gluing with the Tian-Yau metric}

We now pass to the setting of a compact Fano manifold $X$ of dimension $n \geqslant 2$ endowed with a smooth anticanonical divisor $D \subset X$. Note that $D$ is connected by the Lefschetz hyperplane theorem. We denote by $L$ the normal bundle of $D$. The objects on $L$ constructed in section 2 will now carry an index $L\left(h_{L}, \Omega_{L}, \varphi_{\beta, L}, \omega_{\beta, L}\right.$, etc.) to distinguish them from the objects constructed on $X$.
5.1. The Tian-Yau metric. The Tian-Yau metric was obtained in [TY90] and precise asymptotics are derived in [Hei12]. A nice summary is written in [HSVZ22, § 3], and the asymptotics written below are taken from this reference.

We choose the holomorphic $(n-1)$-form $\omega$ on $D$ of section 2 so that $\frac{i^{(n-1)^{2}}}{n} \omega \wedge$ $\bar{\omega}=\omega_{D}^{n-1}$. We have a global holomorphic $n$-form $\Omega$ on $X$ with a simple pole along $D$, normalized by $\omega=\operatorname{Res}_{D} \Omega$, so that the form induced by $\Omega$ on $L$ is $\Omega_{L}=\xi \wedge p^{*} \omega$.

The normal bundle $L$ gives the infinitesimal neighbourhood of $D$ in $X$. One can identify a neighbourhood of $D$ in $X$ with a disc bundle in $L$ : one method uses the Riemannian exponential of a Hermitian metric on $X$, but we prefer a more intrinsic identification using the theory of extremal discs, which produces a (non-holomorphic) fibration in holomorphic discs. The theory was especially used by Lempert [Lem92] to study fillings of 3-dimensional CauchyRiemann manifolds, both on the pseudoconvex and pseudoconcave sides, and also by Bland-Duchamp [BD91]. We will use the following proposition, whose proof is similar to that for 3-dimensional pseudoconcave domains [Lem92, Theorem 10.1]; it can also be extracted from the general statement in [Biq02, Theorem 4.1], which is valid for any signature of the (non degenerate) Levi form.

Proposition 5.1. There exists a diffeomorphism $\Phi: \Delta_{L} \rightarrow U_{L} \subset X$ from the disc bundle $\Delta_{L} \subset L$ to a neighbourhood $U_{L} \subset X$ of $D$, such that $\phi:=\Phi^{*} J_{X}-J_{L} \in$ $\Omega^{0,1}\left(T^{1,0}\right)$ satisfies $\left.\phi\right|_{D}=0, \phi$ is a section of $\left(p^{*} \Omega_{D}^{0,1}\right) \otimes \operatorname{ker} \eta^{1,0}$ (that is, $\phi$ is purely horizontal), and $\phi$ is holomorphic along the discs of $\Delta_{L}$.

Moreover $\Phi^{*} \Omega=v(1-\phi)^{*} \Omega_{L}$, where $v$ is a function on $\Delta_{L}$ such that $\left.v\right|_{D}=1$ and $v$ is holomorphic along the discs.

The advantage of this canonical diffeomorphism is to simplify a number of estimates or calculations, for example in Lemma 5.2, for a potential $\varphi$ depending only of the distance in the normal bundle, we will see that the Kähler form $i \partial \bar{\partial} \varphi$ is the same when calculated with respect to $J_{L}$ or $J_{X}$.

We still denote $t=\log \|v\|_{h_{L}}^{2}$, which via the diffeomorphism $\Phi$ we can also see as a function on $U_{L}$. We modify the function $t$ on $\{-2 \leq t \leq-1\}$ to get a smooth function $\tilde{t}$ on $X \backslash D$ such that
$$\tilde{t}= \begin{cases}t & \text { on } t \leq-2 \\ -1 & \text { on } t \geq-1 \text { and } X \backslash U_{L} .\end{cases}$$

We denote $\omega_{T Y, L}=\left(\frac{n}{n+1}\right)^{1+\frac{1}{n}} i \partial \bar{\partial}(-t)^{1+\frac{1}{n}}$ the Tian-Yau metric defined on $\{t<0\} \subset L$, and $g_{T Y, L}$ the corresponding Riemannian metric. From (2.2) it is given by the formula
$$\omega_{T Y, L}=\left(\frac{n}{n+1}\right)^{\frac{1}{n}}\left(\frac{1}{n}(-t)^{-1+\frac{1}{n}} d t \wedge \eta+(-t)^{\frac{1}{n}} \theta_{D}\right) .$$

Take some Hermitian metric $h$ on $K_{X}^{-1}$ such that $\left.h\right|_{D}=h_{L}$, and with positive curvature on $X$. In order to construct such a metric, we can first extend $h_{L}$ to a positively curved metric $\tilde{h}$ on a neighborhood of $D$ using a distance function (cf e.g. [DP04, Proposition 3.3(i)]). Then, extend $\tilde{h}$ arbitrarily to $X$, and consider $h:=\tilde{h} e^{-A|s|^{2}}$ where $s$ is a section of $\mathcal{O}_{X}(D)$ cutting out $D,|\cdot|$ is a hermitian metric on the latter bundle with positive curvature and $A>0$ is a large enough constant.

Note that $\left.h\right|_{D}$ is only well-defined up to a constant, which will be fixed later in order to have (5.7). Then, the asymptotics of $\omega_{T Y, L}$ coincide with those of the metric
$$\omega_{0}=i \partial \bar{\partial}\left(-\frac{n}{n+1} \log \left|\Omega^{-1}\right|_{h}^{2}\right)^{1+\frac{1}{n}}$$
on $X \backslash D$, with the corresponding Riemannian metric $g_{0}$. More precisely, for any $\varepsilon>0$ :
$$\begin{aligned}
\left|\nabla_{g_{T Y Y, L}}^{j}\left(\Phi^{*} \Omega-\Omega_{L}\right)\right|_{g_{T Y Y, L}} & =O\left(e^{\left(\frac{1}{2}-\varepsilon\right) t}\right) \\
\left|\nabla_{g_{T Y, L}}^{j}\left(\Phi^{*} g_{0}-g_{T Y, L}\right)\right|_{g_{T Y, L}} & =O\left(e^{\left(\frac{1}{2}-\varepsilon\right) t}\right) .
\end{aligned}$$
This comes from the fact that the objects on $L$ and on $X \backslash D$ coincide near $D$ up to order $O(z)=O\left(e^{\frac{t}{2}}\right)$, but then the form of the metric (5.2) introduces powers of $t$ in the estimates for the differences and their derivatives, so we simply write $O\left(e^{\left(\frac{1}{2}-\varepsilon\right) t}\right)$ which will be enough for us.

The Tian-Yau metric on $X \backslash D$ is a Kähler metric $\omega_{T Y}=i \partial \bar{\partial} \varphi_{T Y}$ satisfying
$$\omega_{T Y}^{n}=\frac{i^{n^{2}}}{n+1} \Omega \wedge \bar{\Omega}$$
and asymptotic to our Tian-Yau metric $\omega_{T Y, L}$ near $D$. Of course (5.6) implies that it is Ricci flat. For a suitable (unique) normalization of $h$, we have the asymptotics
$$\varphi_{T Y}=\left(-\frac{n}{n+1} \log \left|\Omega^{-1}\right|_{h}^{2}\right)^{1+\frac{1}{n}}+\psi, \quad\left|\nabla_{g_{T Y, L}}^{j} \psi\right|_{g_{T Y, L}}=O\left(e^{-\varepsilon \sqrt{-t}}\right)$$
for all $j \geq 0$ and for some $\varepsilon>0$. Compared to [HSVZ22], we have a different normalization of the constants in order to match our models of section 2. The rate $e^{-\varepsilon \sqrt{-t}}$ comes from the fact that harmonic functions which go to zero in the metric $g_{0}$ have exponential decay in $\sqrt{-t}$.
5.2. The gluing. We now define Kähler metrics $\omega_{\beta}$ on $X$, with a cone singularity of angle $2 \pi \beta$ around $D$, which are close to be Kähler-Einstein with constant 1, by gluing the metrics $\omega_{\beta, L}$ of section 2 with the Tian-Yau metric $\omega_{T Y}$. This is done by gluing the corresponding Kähler potentials around $t_{\beta}=-\beta^{-1+\mu}$ for some $\mu \in(0,1)$, which will be fixed in the final argument in section 8.2.

We define on $X \backslash D$
$$\varphi_{\beta}= \begin{cases}\chi\left(\frac{t}{t_{\beta}}\right) \Phi_{*} \varphi_{\beta, L}+\left(1-\chi\left(\frac{t}{t_{\beta}}\right)\right) \beta^{1+\frac{1}{n}} \varphi_{T Y} & \text { on } U_{L} \\ \beta^{1+\frac{1}{n}} \varphi_{T Y} & \text { on } X \backslash U_{L}\end{cases}$$
where $\chi: \mathbb{R}_{+} \rightarrow \mathbb{R}_{+}$is a nondecreasing function such that $\chi(u)=1$ for $u \geq 2$ and $\chi(u)=0$ for $u \leq \frac{1}{2}$. We denote $\omega_{\beta}=i \partial \bar{\partial} \varphi_{\beta}$ and $g_{\beta}$ the corresponding Kähler form and Riemannian metric.

This metric is very close to our model $\omega_{\beta, L}$ for $t<t_{\beta} / 2$ :
Lemma 5.2. For any $\varepsilon>0$, one has for $\beta$ small enough, uniformly with respect to $\beta$ :
$$\left|\nabla_{g_{\beta, L}}^{j}\left(g_{\beta}-g_{\beta, L}\right)\right|_{g_{\beta, L}}= \begin{cases}O\left(e^{\left(\frac{1}{2}-\varepsilon\right) t}\right) & \text { for } t \leq 2 t_{\beta}, \\ O\left((-\beta t)^{\left(1-\frac{j}{2}\right)\left(1+\frac{1}{n}\right)}\right) & \text { for } 2 t_{\beta} \leq t \leq \frac{1}{2} t_{\beta} .\end{cases}$$
Proof. The main point here is the uniformity with respect to $\beta$. For $t \leq 2 t_{\beta}$, we have the same potential $\varphi_{\beta, L}$ but with respect to two different complex structures, that of $L$ and of $X$, that we shall denote $J_{L}$ and $J_{X}$. It follows from Proposition 5.1 that $J_{X}-J_{L}$ vanishes on the vertical directions of $L$, and reduces to an endomorphism of $\operatorname{ker} \eta$. Since on $t \leq 2 t_{\beta}$ both Kähler forms have potential $\varphi_{\beta, L}(t)$, and $J_{L} d t=J_{X} d t=2 \eta$, it follows that actually $\omega_{\beta, L}=\frac{1}{2} d J_{L} d \varphi_{\beta, L}$ coincides with $\omega_{\beta}=\frac{1}{2} d J_{X} d \varphi_{\beta, L}$ on $t \leq 2 t_{\beta}$. Therefore $g_{\beta}-g_{\beta, L}=\omega_{\beta, L}\left(\cdot,\left(J_{X}-\right.\right.$ $\left.\left.J_{L}\right) \cdot\right)$, so estimating $g_{\beta}-g_{\beta, L}$ on this region is the same as estimating $J_{X}-J_{L}$.

Since $J_{X}-J_{L}$ vanishes on $D$, it follows from formula (2.14) that
$$\left|J_{X}-J_{L}\right|_{g_{\beta, L}}=O\left(e^{\frac{t}{2}}\right)$$
uniformly in $\beta$, since the factor $-\beta \varphi_{1}^{\prime}(\beta t)$ in front of $\theta_{D}$ does not change the norm of the endomorphisms. The covariant derivatives include terms $\frac{1}{\beta \sqrt{\varphi_{1}^{\prime \prime}(\beta t)}} \frac{\partial}{\partial t}$ and $\frac{1}{\sqrt{-\beta \varphi_{1}^{\prime}(\beta t)}} \frac{\partial}{\partial x}$ (for $x$ coordinate on $D$ ). From the behaviour of $\varphi_{1}$ given in (2.10) it follows that the worst coefficient introduced by a covariant derivative is $\beta^{-1} e^{-\beta \frac{t}{2}}$. As a result, for any $\varepsilon>0$, we have for $\beta$ small enough and $t \leq 2 t_{\beta}=2 \beta^{-1+\mu}$, uniformly in $\beta$,
$$\left|\nabla_{g_{\beta, L}}^{j}\left(J_{X}-J_{L}\right)\right|_{g_{\beta, L}}=O\left(e^{\left(\frac{1}{2}-\varepsilon\right) t}\right) .$$

Now pass to the region $2 t_{\beta} \leq t \leq \frac{1}{2} t_{\beta}$. Here we have
$$\varphi_{\beta}=\beta^{1+\frac{1}{n}} \varphi_{T Y}(t)+\chi\left(\frac{t}{t_{\beta}}\right)\left(\varphi_{\beta, L}(t)-\beta^{1+\frac{1}{n}} \varphi_{T Y}(t)\right),$$
with
$$\begin{aligned}
& \varphi_{T Y}(t)=\left(\frac{-n t}{n+1}\right)^{1+\frac{1}{n}}+\psi, \quad \psi=O\left(e^{-\varepsilon \sqrt{-t}}\right), \\
& \varphi_{\beta, L}(t)=\left(\frac{-\beta n t}{n+1}\right)^{1+\frac{1}{n}}+O\left((-\beta t)^{2\left(1+\frac{1}{n}\right)}\right) .
\end{aligned}$$
(The second line is actually a complete expansion in powers of $(-\beta t)^{1+\frac{1}{n}}$ ). Since $t_{\beta}=-\beta^{-1+\mu}$ goes to $-\infty$, the term coming from $\psi$ is negligible and we obtain
$$\beta^{1+\frac{1}{n}} \varphi_{T Y}(t)-\varphi_{\beta, L}(t)=O\left((-\beta t)^{2\left(1+\frac{1}{n}\right)}\right) .$$

The Kähler form $\omega_{\beta, L}$ is asymptotic to the Tian-Yau form
$$\beta^{1+\frac{1}{n}} \omega_{T Y, L}=\beta^{1+\frac{1}{n}}\left(\frac{n}{n+1}\right)^{\frac{1}{n}}\left(\frac{1}{n}(-t)^{-1+\frac{1}{n}} d t \wedge \eta+(-t)^{\frac{1}{n}} \theta_{D}\right) .$$
Therefore we have
$$\left|\nabla^{j}\left(\beta^{1+\frac{1}{n}} \varphi_{T Y}(t)-\varphi_{\beta, L}(t)\right)\right|_{\beta^{1+\frac{1}{n}} g_{T Y, L}}=O\left((-\beta t)^{\left(2-\frac{j}{2}\right)\left(1+\frac{1}{n}\right)}\right) .$$
On the other hand, $\left|\partial_{t}^{j}\left(\chi\left(\frac{t}{t_{\beta}}\right)\right)\right|=O\left(t_{\beta}^{-j}\right)=O\left(t^{-j}\right)$ so we have the same estimate on the derivatives of $\chi\left(\frac{t}{t_{\beta}}\right)$ :
$$\left|\nabla^{j}\left(\chi\left(\frac{t}{t_{\beta}}\right)\right)\right|_{\beta^{1+\frac{1}{n}} g_{T Y, L}}=O\left((-\beta t)^{-\frac{j}{2}\left(1+\frac{1}{n}\right)}\right) .$$
Since $\varphi_{\beta}-\varphi_{\beta, L}=\left(1-\chi\left(\dot{\overline{t_{\beta}}}\right)\right)\left[\beta^{1+\frac{1}{n}} \varphi_{T Y}-\varphi_{\beta, L}\right]$ we eventually obtain
$$\left|\nabla^{j}\left(\varphi_{\beta}(t)-\varphi_{\beta, L}(t)\right)\right|_{\beta^{1+\frac{1}{n}} g_{T Y, L}}=O\left((-\beta t)^{\left(2-\frac{j}{2}\right)\left(1+\frac{1}{n}\right)}\right) .$$
Since the difference $J_{X}-J_{L}$ is exponentially small, differentiating the estimate (5.12) gives the lemma. \(\square\)

We will solve the Kähler-Einstein equation $\operatorname{Ric}\left(\omega_{\beta}+i \partial \bar{\partial} \varphi\right)=\omega_{\beta}+i \partial \bar{\partial} \varphi$ under the form
$$P_{\beta}(\varphi):=\log \frac{\left(\omega_{\beta}+i \partial \bar{\partial} \varphi\right)^{n}}{i^{n^{2}} \Omega \wedge \bar{\Omega}}+\left(\varphi_{\beta}+\varphi\right)-C_{\beta}=0$$
where the constant $C_{\beta}$ is the constant obtained for the model Calabi metric $g_{\beta, L}$, that is $C_{\beta}=C_{1}+(n+1) \log \beta$. One can calculate $C_{1}=-\log (n+1)$, in accordance with (5.6) when one checks that the Tian-Yau metric must be the limit of $\frac{\omega_{\beta}}{\beta^{1+\frac{1}{n}}}$ when $\beta \rightarrow 0$. We can now estimate the initial error term:

Lemma 5.3. For any $\varepsilon>0$, one has for $\beta$ small enough, uniformly with respect to $\beta$ :
$$\left|\nabla_{g_{\beta}}^{j} P_{\beta}(0)\right|_{g_{\beta}}= \begin{cases}O\left(e^{\left(\frac{1}{2}-\varepsilon\right) t}\right) & t \leq 2 t_{\beta}, \\ O\left((-\beta \tilde{t})^{\left(1-\frac{j}{2}\right)\left(1+\frac{1}{n}\right)}\right) & \tilde{t} \geq 2 t_{\beta} .\end{cases}$$

Proof. This follows from the estimates in Lemma 5.2:
\begin{itemize}
\item[-] The form $\omega_{\beta, L}$ solves $\omega_{\beta, L}^{n}=C_{\beta} e^{\varphi_{\beta, L}} i^{n^{2}} \Omega_{L} \wedge \bar{\Omega}_{L}$, therefore on $t \leq 2 t_{\beta}$, since $\omega_{\beta}$ and $\Omega$ differ from $\omega_{\beta, L}$ and $\Omega_{L}$ respectively by an exponentially decreasing term, we obtain the estimate of the lemma.
\item[-] On $\tilde{t} \geq \frac{1}{2} t_{\beta}$ the Tian-Yau form $\omega_{T Y}$ is Ricci flat and solves (5.6), so the error term in (5.14) is $\varphi_{\beta}=O\left((-\beta \tilde{t})^{1+\frac{1}{n}}\right)$ (and the corresponding estimates for the derivatives).
\item[-] On the gluing region $2 t_{\beta} \leq t \leq \frac{1}{2} t_{\beta}$, the estimates from lemma 5.2 are still sufficient to prove (5.14).
\end{itemize} \(\square\)
5.3. Convergence of $\left(X, g_{\beta}\right)$ and its rescalings. In this section, we determine all possible Gromov-Hausdorff limits of our model space $\left(X, \varepsilon_{\beta}^{-1} g_{\beta}, p\right)$ where $p$ is a fixed point and $\left(\varepsilon_{\beta}\right)_{\beta}$ is non-decreasing family of positive numbers. At the very end of the paper, we will see that the results of this section continue to hold for the Kähler-Einstein metric $\hat{g}_{\beta}$, cf Lemma 8.4.

Case $A$. Convergence of $\left(X, g_{\beta}, p\right)$ and limit renormalized measure. In the following, we will use the variable $u=\beta t$, so that the gluing region is $-2 \beta^{\mu} \leq u \leq-\frac{1}{2} \beta^{\mu}$; we set $u_{\beta}:=-\beta^{\mu}$. For later purposes, we extend the variable $u$ to the whole $X$ by setting $\tilde{u}=\beta \tilde{t}$, so that $\tilde{u}=\beta$ in $X \backslash U_{L}$. We have the form (2.15) for the metric, which we rewrite here:
$$g_{\beta, L}=2 \varphi_{1}^{\prime \prime}(u)\left(\frac{1}{4} d u^{2}+\beta^{2} \eta^{2}\right)-\beta \varphi_{1}^{\prime}(u) g_{D} .$$
Next, we have by Lemma 5.2 the following estimates
$$g_{\beta}= \begin{cases}g_{\beta, L}+O\left(e^{-\beta^{\mu-1}}\right) & \text { if } \quad u \leqslant 2 u_{\beta} \\ g_{\beta, L}+O\left(\beta^{\mu\left(1+\frac{1}{n}\right)}\right) & \text { if } \quad 2 u_{\beta} \leqslant u \leqslant \frac{1}{2} u_{\beta}, \\ \beta^{1+\frac{1}{n}} g_{\mathrm{TY}} & \text { if } \quad u \geqslant \frac{1}{2} u_{\beta} .\end{cases}$$
At this point, we can already see that the size of ( $u \geqslant 2 u_{\beta}$ ) with respect to $g_{\beta}$ goes to zero, hence that zone does not contribute to the limit.

To go further, it is convenient to introduce the moment map $x=-\varphi_{1}^{\prime}(u) \in$ $(0,1)$ and then set $\cos (s)=x^{\frac{n+1}{2}}$ for $s \in\left(0, \frac{\pi}{2}\right)$. Relying on the identities $x^{n+1}=1-e^{x}$ and $\varphi_{1}^{\prime \prime}=\frac{1}{n+1} \frac{1-x^{n+1}}{x^{n-1}}$, we get
$$g_{\beta, L}=\frac{2}{n+1} d s^{2}+\frac{2}{n+1} \frac{\sin ^{2} s}{\cos (s)^{2 \frac{n-1}{n+1}}} \beta^{2} \eta^{2}+\beta \cos (s)^{\frac{2}{n+1}} g_{D}$$
Given (5.9), we easily see that $\left(X, g_{\beta}, p\right)$ converges to
$$\left(X_{\infty}, g_{\infty}, p_{\infty}\right)= \begin{cases}\left(\left[0, \frac{\pi}{2}\right], \frac{2}{n+1} d s^{2}, 0\right) & \text { if } p \in D \\ \left(\left[0, \frac{\pi}{2}\right], \frac{2}{n+1} d s^{2}, 1\right) & \text { otherwise }\end{cases}$$
Moreover, the normalized measures $v_{\beta}=\frac{\mathrm{dvol}_{g_{\beta}}}{\operatorname{vol}_{g_{\beta}}(X)}$ converge to the measure $v_{\infty}=c \sin s \cos (s)^{\frac{n-1}{n+1}} d s$ for some $c>0$. In other words,
$$v_{\infty}=d\left(-\cos ^{\frac{2 n}{n+1}} s\right) .$$
The asymptotic behavior of $\left(X, g_{\beta}\right)$ is summarized by the picture below.
![](https://cdn.mathpix.com/cropped/f774122a-1d15-4317-9d31-f69a2c77c0d9-26.jpg?height=625&width=821&top_left_y=318&top_left_x=653)
Case B. Convergence of $\left(X, \varepsilon_{\beta}^{-1} g_{\beta}, p\right)$ with $\varepsilon_{\beta} \rightarrow 0$. First we consider the case $p \in D$. In other words, we work near $s=0$. Clearly, the zone $\left(u \geqslant 2 u_{\beta}\right)$ does not contribute to the limit since it escapes any ball centered at $p$ of fixed radius. From (5.15)-(5.16) we get
$$g_{\beta} \simeq \frac{2}{n+1}\left(d s^{2}+s^{2} \beta^{2} \eta^{2}\right)+\beta g_{D}$$
and the limit of $\left(X, \varepsilon_{\beta}^{-1} g_{\beta}, p\right)$ when $p \in D$ is
$$\begin{cases}\left(\mathbb{R}_{+}, d t^{2}, 0\right) & \text { if } \quad \beta \ll \varepsilon_{\beta} \ll 1 \\ \left(\mathbb{R}_{+} \times D, d t^{2}+g_{D},(0, p)\right) & \text { if } \quad \varepsilon_{\beta}=\beta \\ \left(\mathbb{R}_{+} \times \mathbb{C}^{n-1}, d t^{2}+g_{\left.\mathbb{C}^{n-1},(0,0)\right)}\right. & \text { if } \quad \varepsilon_{\beta} \ll \beta .\end{cases}$$
where the $\mathbb{R}_{+}$factor comes from the rescaling $t=\varepsilon_{\beta}^{-1 / 2} s$.
Second we consider the case when $p \in X \backslash D$. In other words, we work near $s=\frac{\pi}{2}$. It is convenient to set $\sigma=\frac{\pi}{2}-s$.

Let us first consider the case where $\varepsilon_{\beta} \leqslant \beta^{1+\frac{1}{n}}$. In that case, the "Tian-Yau" zone ( $u \geqslant \frac{1}{2} u_{\beta}$ ) has size of order $\varepsilon_{\beta}^{-\frac{1}{2}} \beta^{\frac{\mu}{2}\left(1+\frac{1}{n}\right)} \rightarrow+\infty$ with respect to $\varepsilon_{\beta}^{-1} g_{\beta}$ hence the limit is that of $\left(X \backslash D, \varepsilon_{\beta}^{-1} \beta^{1+\frac{1}{n}} g_{\mathrm{TY},} p\right)$.

From now on, one can assume that $\varepsilon_{\beta} \gg \beta^{1+\frac{1}{n}}$. Therefore, the compact part is contracted and everything is concentrated near the zone where $u \sim 0$, where the asymptotics (2.16) hold for $g_{\beta, L}$ as well as for $\beta^{1+\frac{1}{n}} g_{\mathrm{TY}}$. Given (5.15), we get in terms of the variable $\sigma \simeq(-u)^{\frac{n+1}{2 n}}$
$$g_{\beta} \simeq \frac{2}{n+1}\left(d \sigma^{2}+\frac{\beta^{2}}{\sigma^{2 \frac{n-1}{n+1}}} \eta^{2}\right)+\beta \sigma^{\frac{2}{n+1}} g_{D} .$$

In a ball centered at $p$ of fixed radius for $\varepsilon_{\beta}^{-1} g_{\beta}$, we have $\varepsilon^{-\frac{1}{2}} \sigma \lessapprox 1$ (since $\varepsilon_{\beta}^{-1 / 2} \sigma(p) \ll 1$ ), so that
$$\varepsilon_{\beta}^{-1} \beta \sigma^{\frac{2}{n+1}} \lessapprox\left(\varepsilon_{\beta}^{-1} \beta^{1+\frac{1}{n}}\right)^{\frac{n}{n+1}} \ll 1 .$$
Moreover, we have $\sigma \gtrapprox \beta^{\frac{n+1}{2 n}}$ (since $u \leqslant-\beta$ ), hence
$$\varepsilon_{\beta}^{-1} \frac{\beta^{2}}{\sigma^{2 \frac{n-1}{n+1}}} \lessapprox \varepsilon_{\beta}^{-1} \beta^{1+\frac{1}{n}} \ll 1 .$$
From (5.17), we can deduce that in this case the limit is just a ray.
In summary, if $p \in X \backslash D$ the limit of $\left(X, \varepsilon_{\beta}^{-1} g_{\beta}, p\right)$ is
$$\left\{\begin{array}{lll}
\left(\mathbb{R}_{+}, d t^{2}, 0\right) & \text { if } & \beta^{1+\frac{1}{n}} \ll \varepsilon_{\beta} \ll 1 \\
\left(X \backslash D, g_{\mathrm{TY}}, p\right) & \text { if } & \varepsilon_{\beta}=\beta^{1+\frac{1}{n}}
\end{array}\right.$$
and for $\varepsilon_{\beta} \ll \beta^{1+\frac{1}{n}}$ we only have the trivial bubble $\mathbb{C}^{n}$.

\section*{6. Uniform Schauder estimate for cones}
6.1. Preliminaries. In this section, we consider the flat Kähler metric on $\mathbb{C}^{*} \times$ $\mathbb{C}^{n-1}$ with cone angle $2 \pi \beta$ along $D:=\left(z_{1}=0\right)$, that is
$$d d^{c}\left(\left|z_{1}\right|^{2 \beta}+\left\|z^{\prime}\right\|^{2}\right)=\beta^{2}\left|z_{1}\right|^{2(\beta-1)} i d z_{1} \wedge d \bar{z}_{1}+\sum_{j=2}^{n} i d z_{j} \wedge d \bar{z}_{j}$$
where $z^{\prime}=\left(z_{2}, \ldots, z_{n}\right)$. Using the real coordinates $r:=\left|z_{1}\right|^{\beta}, \theta:=\arg \left(z_{1}\right)$, the Riemannian metric associated that Kähler metric is
$$\bar{g}_{\beta}:=\left(d r^{2}+\beta^{2} r^{2} d \theta^{2}\right)+g_{\mathbb{C}^{n-1}} .$$
It will be convenient to introduce the notation
$$\widehat{g}_{\beta}:=d r^{2}+\beta^{2} r^{2} d \theta^{2}$$
for the one-dimensional complex cone with cone angle $2 \pi \beta$ at $0 \in \mathbb{C}$.
On balls.
We are interested in the behavior of $\bar{g}_{\beta}$ near the divisor when $\beta$ approaches 0. When $n=1$, the zone $\left\{C \geqslant\left|z_{1}\right| \geqslant 1 / C\right\}$ is collapsed onto a point which is at distance exactly one of the origin. This means that the asymptotic geometry is concentrated extremely close to the divisor. In the following, we will only consider with points $p$ at distance at most $\frac{1}{2}$ from the origin with respect to $\bar{g}_{\beta}$; in particular, $\left|z_{1}(p)\right| \leqslant 2^{-1 / \beta}$ converges exponentially fast to zero.

If $p \in \mathbb{C}^{n}$ and $\rho>0$, we denote by $B_{p}(\rho)$ the geodesic ball of radius $\rho$ centered at $p$, with respect to $\bar{g}_{\beta}$. If $p \in D$, then $B_{p}(\rho)=\left\{q=\left(r_{q}, \theta_{q}, z^{\prime}\right) ; r_{q}^{2}+\right.$ $\left.\left\|z^{\prime}-z^{\prime}(p)\right\|^{2}<\rho^{2}\right\}$.

In the following, we set $B_{\beta}:=B_{0}\left(\frac{1}{2}\right)$ for the ball centered at the origin with radius 1/2 with respect to $\bar{g}_{\beta}$. It will be convenient to also set $B_{\beta}^{\prime}:=B_{0}\left(\frac{1}{4}\right)$. As
explained above, we will exclusively focus on the behavior of $\bar{g}_{\beta}$ on $B_{\beta}$. Punctured balls $B^{*}$ are defined as $B \backslash D$.

We decompose the gradient of $\bar{g}_{\beta}$ as $\nabla^{\bar{g}_{\beta}}=\left(D^{\prime}, D^{\prime \prime}\right)$ where $D^{\prime}=\left(D_{1}, D_{2}\right)$ with $D_{1}=\partial_{r}, D_{2}=\frac{1}{\beta r} \partial_{\theta}$ and $D^{\prime \prime}=\left(D_{3}, \ldots, D_{2 n}\right)$ where $D_{2 j-1}=\partial_{x_{j}}, D_{2 j}=\partial_{y_{j}}$ if $z_{j}=x_{j}+i y_{j}$. The laplacian is
$$\Delta_{\bar{g}_{\beta}}=\underbrace{\partial_{r}^{2}+\frac{1}{r} \partial_{r}+\frac{1}{\beta^{2} r^{2}} \partial_{\theta}^{2}}_{=\Delta_{\widehat{z}_{\beta}}}+\Delta_{\mathbb{C}^{n-1}} .$$
In complex coordinates, the first order derivatives are given by
$$\partial_{r}=\frac{1}{\beta\left|z_{1}\right|^{\beta}}\left(z_{1} \partial_{z_{1}}+\bar{z}_{1} \partial_{\bar{z}_{1}}\right), \quad \text { and } \quad \frac{1}{\beta r} \partial_{\theta}=\frac{i}{\beta\left|z_{1}\right|^{\beta}}\left(z_{1} \partial_{z_{1}}-\bar{z}_{1} \partial_{\bar{z}_{1}}\right)$$
while the second order derivatives are
$$\partial_{r}^{2}=\frac{1}{\beta^{2}\left|z_{1}\right|^{2 \beta}}\left(2\left|z_{1}\right|^{2} \partial_{z_{1} \bar{z}_{1}}^{2}+(1-\beta)\left(z_{1} \partial_{z_{1}}+\bar{z}_{1} \partial_{\bar{z}_{1}}\right)+\left(z_{1}^{2} \partial_{z_{1}}+\bar{z}_{1}^{2} \partial_{\bar{z}_{1}}\right)\right)$$
and
$$\frac{1}{\beta^{2} r^{2}} \partial_{\theta}^{2}=\frac{-1}{\beta^{2}\left|z_{1}\right|^{2 \beta}}\left(z_{1}^{2} \partial_{z_{1}}^{2}+z_{1} \partial_{z_{1}}-2\left|z_{1}\right|^{2} \partial_{z_{1} \bar{z}_{1}}^{2}+\bar{z}_{1} \partial_{\bar{z}_{1}}+\bar{z}_{1}^{2} \partial_{\bar{z}_{1}}\right) .$$

For any real number $\alpha \in(0,1)$, we define the $\mathcal{C}^{\alpha}$ norm with respect to $\bar{g}_{\beta}$ in the classical way. That is, if $p \in B_{\beta}$ i.e. if $f \in \mathcal{C}^{0}\left(B_{\beta}\right)$, then
$$\|f\|_{\alpha}=\sup _{x, y \in B_{\beta}} \frac{|f(x)-f(y)|}{d_{\bar{g}_{\beta}}(x, y)^{\alpha}} .$$
We defined the $\mathcal{C}^{2, \alpha}$ norm of a function $f$ on $B_{\beta}$ as
$$\|f\|_{\alpha}=\|f\|_{0}+\left\|\nabla^{\bar{g}_{\beta}} f\right\|_{0}+\sum_{i=1}^{2 n} \sum_{j=3}^{2 n}\left\|D_{i} D_{j} f\right\|_{\alpha}+\left\|\Delta_{\widehat{g}_{\beta}} f\right\|_{\alpha} .$$
This means that we do not require a control on the derivatives $D_{1}^{2} f, D_{2}^{2} f$, $D_{1} D_{2} f, D_{2} D_{1} f$, following Donaldson [Don12].

The main result of this section is the following
Theorem 6.1 (Weak Schauder estimate). Let $u \in L^{\infty}\left(B_{\beta}\right)$ solve $\Delta_{\bar{g}_{\beta}} u=f$ for some $f \in \mathcal{C}^{\alpha}\left(B_{\beta}\right)$. Then $u \in \mathcal{C}^{2, \alpha}\left(B_{\beta}\right)$ and there exists a constant $C=C(n, \alpha, \delta)$ such that for all $\beta \in(0,1-\delta]$ one has
$$\|u\|_{\mathcal{C}^{2, \alpha}\left(B_{\beta}^{\prime}\right)} \leqslant C\left(\|f\|_{\mathcal{C}^{\alpha}\left(B_{\beta}\right)}+\|u\|_{\mathcal{C}^{0}\left(B_{\beta}\right)}\right) .$$

The novelty of the result above relies on the uniformity of the "Schauder constant" $C$ above with respect to $\beta$ (say when $\beta \rightarrow 0$ ), since the result for fixed $\beta$ has been known for a while. It is initially due to Donaldson [Don12] and was later reproved and generalized via many different methods, cf [GS21, GY21, DE21].

We will follow the approach of Bin Guo and Jian Song [GS21], itself based on an original and quite direct proof of the usual Schauder estimate by Xu-Jia Wang [Wan06].

In what follows, we will systematically assume that $\beta<\frac{1}{2}$.
6.2. Gradient estimates. In this section, we provide two types of gradient estimates for the metric $\bar{g}_{\beta}$ that will be useful later.

Lemma 6.2. Assume that $n=1$. Let $u \in L^{\infty}\left(B_{0}(\rho)\right)$, smooth outside 0 solving $\Delta_{\widehat{g}_{\beta}} u=f$. Then there exists a constant $C>0$ such that for any $r \leqslant \frac{\rho}{2^{\beta}}$, one has
$$\left|\nabla^{\widehat{\delta_{\beta}}} u\right|(r, \theta) \leqslant C\left[\frac{1}{\beta}\left(\frac{r}{\rho}\right)^{\frac{1}{\beta}} \cdot \frac{1}{r} \sup _{B_{0}(\rho)}|u|+r \sup _{B_{0}(\rho)}|f| .\right]$$
Remark 6.3. A trivial but crucial observation is that when $r \leqslant \rho / 2$, we have $\frac{1}{\beta}\left(\frac{r}{\rho}\right)^{\frac{1}{\beta}} \rightarrow 0$ when $\beta \rightarrow 0$. In particular, and this is all we will use in the following, the latter quantity is bounded when $\beta$ approaches zero.

Proof. The function $v(z):=u\left(\rho^{1 / \beta} z\right)$ is defined for $|z| \leqslant 1$ and satisfies $\Delta_{\text {eucl }} v(z)=$ $\rho^{2} \frac{\beta^{2}}{|z|^{2(1-\beta)}} f\left(\rho^{1 / \beta} z\right)$. Classically, we have
$$v(z)=h(z)+\underbrace{\rho^{2} \int_{|w|<1} \frac{\beta^{2}}{|w|^{2(1-\beta)}} f\left(\rho^{1 / \beta} w\right) \log \left|\frac{z-w}{1-\bar{w} z}\right||d w|^{2}}_{=: I(z)},$$
where $h$ is the harmonic function on the unit disk $\mathbb{D} \subset \mathbb{C}$ whose boundary values are $\left.v\right|_{\partial \mathbb{D}}$. In particular, there exists a universal constant $C_{1}$ such that
$$\sup _{|z| \leqslant \frac{1}{2}}\left|\nabla^{\text {eucl }} h(z)\right| \leqslant C_{1} \sup _{|z|=1}|v(z)|=C_{1} \sup _{B_{0}(\rho)}|u| .$$
In particular, we get for $\left|\rho^{-1 / \beta} z\right| \leqslant 1 / 2$ (or, equivalently, $r \leqslant 2^{-\beta} \rho$ ):
$$\left|\nabla^{\widehat{s}_{\beta}} h\left(\rho^{-1 / \beta} z\right)\right| \leqslant \frac{C_{1}}{\beta}\left(\frac{r}{\rho}\right)^{\frac{1}{\beta}} \cdot \frac{1}{r} \sup _{B_{0}(\rho)}|u|,$$
which takes care of the first part in the RHS of (6.3). To take care of the integral summand $I(z)$, we assume that $|z| \leqslant 1 / 2$ so that $\nabla^{\text {eucl }} I(z)$ is controlled by $\rho^{2} \beta^{2} \sup |f| \cdot \int_{|w|<1} \frac{|d w|^{2}}{|w|^{2(1-\beta)} \cdot|z-w|}$. Performing the change of variable $x:=w / z$ in the integral, we get $|z|^{2 \beta-1} \int_{|x|<1 /|z|} \frac{|d x|^{2}}{|x|^{2(1-\beta)} .|x-1|}$. There are three zones: around $x=0$ the integral is equivalent to $1 / \beta$, around $x=1$ we have uniform integrability while around $|x|=1 /|z|$ it is equivalent to $|z|^{1-2 \beta}$ hence it is uniformly integrable too. All in all, we find that $\left|\nabla^{\text {eucl }} I(z)\right| \lesssim \beta \rho^{2}|z|^{2 \beta-1} \cdot \sup |f|$. In terms of $\bar{g}_{\beta}$-gradient, this means that
$$\left|\nabla^{\widehat{\gamma_{\beta}}} I\left(\rho^{-1 / \beta} z\right)\right| \lesssim \frac{1}{\beta} r^{\frac{1}{\beta}-1} \rho^{-1 / \beta} \cdot \beta \rho^{2}\left|\rho^{-1 / \beta} z\right|^{2 \beta-1} \cdot \sup |f|=r \cdot \sup |f| .$$
Combined with (6.4), this yields the desired gradient estimate for $u$. \(\square\)

We will also need the following gradient estimate in any dimension for harmonic functions:

Lemma 6.4. Let $u \in L^{\infty}\left(B_{p}(\rho)\right)$ be a harmonic function, i.e. $\Delta_{\bar{g}_{\beta}} u=0$. Assume that either $p=0$ or $\rho<r(p)$. Then there exists a universal constant $C=C(n)>0$ such that
$$\sup _{B_{p}(\rho / 2)}\left|\nabla^{\bar{g}_{\beta}} u\right| \leqslant \frac{C}{\rho} \sup _{B_{p}(\rho)}|u| .$$
In particular, for any integer $\ell>0$ that
$$\sup _{B_{p}(\rho / 2)}\left|\left(D^{\prime \prime}\right)^{\ell} u\right| \leqslant \frac{C(n, \ell)}{\rho^{\ell}} \sup _{B_{p}(\rho)}|u| ; \quad \sup _{B_{p}(\rho / 2)}\left|\left(D^{\prime \prime}\right)^{\ell} D^{\prime} u\right| \leqslant \frac{C(n, \ell)}{\rho^{\ell+1}} \sup _{B_{0}(\rho)}|u|$$
as well as, if $p$ is not on the divisor
$$\left|\nabla^{\bar{g}_{\beta}}\left[\partial_{r}\left(D^{\prime \prime}\right)^{\ell} u\right](z)\right|+\left|\nabla^{\bar{g}_{\beta}}\left[\frac{1}{\beta r} \partial_{\theta}\left(D^{\prime \prime}\right)^{\ell} u\right](z)\right| \leqslant C\left(1+\frac{r(p)}{r}\right) \cdot \frac{\|u\|_{L^{\infty}\left(B_{p}(\rho)\right)}}{\rho^{\ell+2}} .$$
Proof. Following [GS21, Lemma 2.4 \& Proposition 2.2], one can approximate $\bar{g}_{\beta}$ by smooth metrics $\bar{g}_{\beta, \varepsilon}$ with non-negative Ricci curvature and use Cheng-Yau's gradient estimate [CY75] to get the first two sets of inequalities. For the last estimate, set $v:=\left(D^{\prime \prime}\right)^{\ell} u$ and observe that $\frac{1}{\beta} \partial_{\theta} v$ is harmonic on $B_{p}(\rho)$ and therefore
$$\left|\frac{1}{\beta} \partial_{\theta} v\right| \leqslant C \frac{r\|u\|_{L^{\infty}\left(B_{p}(\rho)\right)}}{\rho^{\ell+1}} \text { on } B_{p}(\rho / 2)$$
thanks to the previous gradient estimate. Here, $C=C(n, \ell)$ and may change from line to line. Iterating that argument, we get
$$\left|\nabla^{\bar{g}_{\beta}} \frac{1}{\beta} \partial_{\theta} v\right| \leqslant C \frac{r(p)\|u\|_{L^{\infty}\left(B_{p}(\rho)\right)}}{\rho^{\ell+2}} \quad \text { on } B_{p}(\rho / 2) .$$
Since $\left|\nabla^{\bar{g}_{\beta}} \frac{1}{\beta r} \partial_{\theta} v\right| \leqslant \frac{1}{r^{2}}\left|\frac{1}{\beta} \partial_{\theta} v\right|+\frac{2}{r}\left|\nabla^{\bar{g}_{\beta}} \frac{1}{\beta} \partial_{\theta} v\right|$, we get
$$\left|\nabla^{\bar{g}_{\beta}} \frac{1}{\beta r} \partial_{\theta} v\right| \leqslant C\left(\frac{\rho}{r}+\frac{r(p)}{r}\right) \cdot \frac{\|u\|_{L^{\infty}\left(B_{p}(\rho)\right)}}{\rho^{\ell+2}}$$
which provides half of the desired inequality. For the second half, observe that $\nabla^{\bar{g} \beta} \partial_{r} v$ involves the following terms: $\partial_{r}^{2} v, \frac{1}{r} \partial_{r}\left(\frac{1}{\beta} \partial_{\theta} v\right)$ and $\nabla^{\prime \prime} \partial_{r} v$. The last term is controlled by the gradient estimate already established for the harmonic function $D^{\prime \prime} v$ and the second one is controlled by (6.6). Finally, the first one can be written $\partial_{r}^{2} v=\underbrace{\Delta_{\bar{g}_{\beta}} v}_{=0}-\frac{1}{r} \partial_{r} v-\frac{1}{\beta^{2} r^{2}} \partial_{\theta}^{2} v-\Delta_{\mathbb{C}^{n-1}} v$ and the estimate follows from the previous ones. \(\square\)

In Lemma 6.4 above, one can adapt the proof of the estimate (6.5) in the case where $p=0$ is centered on the divisor, and the RHS becomes $C \frac{\|u\|_{L^{\infty}(B p(\rho))}}{r \rho^{\ell+1}}$, which turns out to be too coarse for our later purposes. Instead, we will use the input of Lemma 6.2 to obtain the following estimate, valid for balls centered on the divisor.

Lemma 6.5. Let $u \in L^{\infty}\left(B_{0}(\rho)\right)$ be a harmonic function, i.e. $\Delta_{\bar{g}_{\beta}} u=0$. There exists $C=C(n, \ell)$ such that for all $z=\left(r, \theta, z^{\prime}\right)$ in $B_{0}(\rho / 4)$, one has
$$\left|\nabla^{\widehat{8_{\beta}}}\left[\left(D^{\prime \prime}\right)^{\ell} u\right](z)\right|+\left|\nabla^{\widehat{8_{\beta}}}\left[\frac{1}{\beta} \partial_{\theta}\left(D^{\prime \prime}\right)^{\ell} u\right](z)\right| \leqslant C \frac{\|u\|_{L^{\infty}\left(B_{0}(\rho)\right)}}{\rho^{\ell+1}} \cdot\left(\frac{1}{\beta}\left(\frac{r}{\rho}\right)^{\frac{1}{\beta}-1}+\frac{r}{\rho}\right)$$
as tas
$$\left|\nabla^{\widehat{\beta}_{\beta}}\left[\partial_{r}\left(D^{\prime \prime}\right)^{\ell} u\right](z)\right| \leqslant C \frac{\|u\|_{L^{\infty}\left(B_{0}(\rho)\right)}}{\rho^{\ell+2}} \cdot\left(\frac{1}{\beta}\left(\frac{r}{\rho}\right)^{\frac{1}{\beta}-2}+1\right) .$$
Proof. The two important points are that $\Delta_{\bar{g}_{\beta}}$ commutes with both $D^{\prime \prime}$ and $\partial_{\theta}$ and that for any $\bar{g}_{\beta}$-harmonic function $w$, one has $\Delta_{\widehat{g}_{\beta}} w=-\Delta_{\mathbb{C}^{n-1}} w$. Set $v:=$ $\left(D^{\prime \prime}\right)^{\ell} u$. By Lemma 6.4,
$$\sup _{B_{0}(\rho / 2)}\left[|v|+\left|\frac{1}{\beta} \partial_{\theta} v\right|\right] \leqslant C \frac{\|u\|_{L^{\infty}\left(B_{0}(\rho)\right)}}{\rho^{\ell+1}}$$
so that the first inequality now easily follows from Lemma 6.2.
The second inequality requires a bit more work. We start by decomposing
$$\nabla^{\bar{s}_{\beta}} \partial_{r} v=\left(\partial_{r}^{2} v, \frac{1}{\beta r} \partial_{r \theta}^{2} v, D^{\prime \prime} \partial_{r} v\right)$$
and observing that the last two components are controlled on $B_{0}(\rho / 4)$ by
$$\left.\sup _{B_{0}(\rho / 2)}\left[\left|\nabla^{\widehat{\delta}_{\beta}} D^{\prime \prime} v\right|+\frac{1}{r}\left|\nabla^{\widehat{\delta}_{\beta}} \frac{1}{\beta} \partial_{\theta} v\right|\right]\right],$$
which in turn is controlled by $M:=\frac{\|u\|_{L^{\infty}\left(B_{0}(\rho)\right)}}{\rho^{\ell+2}} \cdot\left(\frac{1}{\beta}\left(\frac{r}{\rho}\right)^{\frac{1}{\beta}-2}+1\right)$ thanks to the first inequality. We are left to estimating $\partial_{r}^{2} v$. We write
$$\begin{aligned}
\partial_{r}^{2} v & =\Delta_{\widehat{g}_{\beta}}(v)-\frac{1}{r} \partial_{r} v-\frac{1}{\beta^{2} r^{2}} \partial_{\theta}^{2} v \\
& =-\Delta_{\mathbb{C}^{n-1}}(v)-\frac{1}{r} \partial_{r} v-\frac{1}{\beta^{2} r^{2}} \partial_{\theta}^{2} v
\end{aligned}$$
and observe that each summand is controlled by
$$\sup _{B_{0}(\rho / 2)}\left[\left|\left(D^{\prime \prime}\right)^{2} v\right|+\frac{1}{r}\left[\left|\nabla^{\widehat{\beta}_{\beta}} v\right|+\left|\nabla^{\widehat{\beta}_{\beta}} \frac{1}{\beta} \partial_{\theta} v\right|\right]\right] \leqslant C M$$
thanks to the first inequality again. The lemma is proved. \(\square\)
6.3. Strategy of the proof of Theorem 6.1. The main idea is to consider, for a given point $p \in B_{\beta}$ a sequence of functions $\left(u_{\kappa}\right)$ defined on neighborhoods $U_{\kappa}$ of $p$ getting smaller and smaller when $\kappa$ increases and such that
$$\begin{cases}\Delta_{\bar{g}_{\beta}} u_{\kappa}=f(p) & \text { on } U_{\kappa} \\ \left.u_{\kappa}\right|_{\partial U_{\kappa}}=\left.u\right|_{\partial U_{\kappa}} & \end{cases}$$
More precisely, let us set $\lambda:=\frac{1}{2}, r(p):=d(p, D)$ and choose $U_{\kappa}=B_{p}\left(\lambda^{\kappa}\right)$ if $r(p)>\lambda^{\kappa}$ and $U_{\kappa}:=B_{\tilde{p}}\left(2 \lambda^{\kappa}\right)$ otherwise, where $\tilde{p}$ is the projection of $p$ onto
$D$ under the natural map $\mathbb{C}^{n} \rightarrow \mathbb{C}^{n-1},\left(z_{1}, \ldots, z_{n}\right) \rightarrow\left(z_{2}, \ldots, z_{n}\right)$. Note that if $\sin (\beta \pi) r(p)<\rho<r(p)$, then the geodesic ball $B_{p}(\rho)$ is essentially an annulus (times an euclidean ball).

Since $u_{\kappa}-\frac{1}{n-1}\left\|z^{\prime}\right\|^{2}$ is harmonic, $u_{\kappa}$ enjoys all the regularity properties shared by harmonic functions.

The strategy is, given two indices $i, j$ and two points $p, q \in B_{\beta}$, to estimate $D_{i} D_{j} u(p)-D_{i} D_{j} u(q)$ by the analogous quantity for $u_{\kappa}$, for some $\kappa=\kappa(p, q)$ chosen carefully. More precisely, the choice of $\kappa$ with be such that $\lambda^{\kappa} \simeq 8 d$ where $d=d(p, q)$. In particular, $U_{\kappa}$ will contain $B_{p}(2 d)$ and thus the geodesic joining $p$ to $q$.
6.4. $\mathcal{C}^{2}$ estimates. It is convenient to write $\omega(r)$ for the modulus of continuity of $f$. By assumption, one has $\omega(r)=O\left(r^{\alpha}\right)$. By considering $u-u_{\kappa} \pm \omega\left(\lambda^{\kappa}\right)$. $\left[(r-r(p))^{2}+\left\|z^{\prime}-z^{\prime}(p)\right\|^{2}\right]$, one easily deduces from the maximum principle that
$$\left\|u-u_{\kappa}\right\|_{L^{\infty}\left(U_{\kappa}\right)} \leqslant C(n) \lambda^{2 \kappa} \omega\left(\lambda^{\kappa}\right) .$$
By the triangle inequality, these inequality extend to quantify the harmonic functions
$$h_{\kappa}:=u_{\kappa+1}-u_{\kappa}$$
on $U_{\kappa+1}$ along with their derivatives thanks to Lemma 6.4
$$\left\|D^{\prime \prime} h_{\kappa}\right\|_{L^{\infty}\left(U_{\kappa+2}\right)} \leqslant C(n) \lambda^{\kappa} \omega\left(\lambda^{\kappa}\right) ; \quad\left\|\left(D^{\prime \prime}\right)^{2} h_{\kappa}\right\|_{L^{\infty}\left(U_{\kappa+2}\right)} \leqslant C(n) \omega\left(\lambda^{\kappa}\right) .$$
For $\kappa \gg 1$, one can define on $U_{\kappa}$ a single-valued branch $w=z_{1}^{\beta}$ realizing an isomorphic biholomorphism between $\left(U_{\kappa}, \bar{g}_{\beta}\right)$ and a euclidean ball $\left(B_{\text {eucl }}\left(\lambda^{\kappa}\right), g_{\text {eucl }}\right)$. Using this, one gets that whenever $p \notin D$,
$$\lim _{\kappa \rightarrow+\infty} D^{\prime \prime} u_{\kappa}(p)=D^{\prime \prime} u(p) ; \quad \lim _{\kappa \rightarrow+\infty}\left(D^{\prime \prime}\right)^{2} u_{\kappa}(p)=\left(D^{\prime \prime}\right)^{2} u(p),$$
cf [GS21, Lemma 2.8]. Write $\left(D^{\prime \prime}\right)^{2} u_{\kappa}=\left(D^{\prime \prime}\right)^{2} u_{1}+\sum_{j=1}^{\kappa-1}\left(D^{\prime \prime}\right)^{2}\left(u_{j+1}-u_{j}\right)$ on $U_{\kappa}$ and then combine (6.10), (6.9) and Lemma 6.4 to obtain
$$\left\|\left(D^{\prime \prime}\right)^{2} u\right\|_{L^{\infty}\left(B_{\beta}^{\prime}\right)} \leqslant C(n, \alpha)\left[\|u\|_{L^{\infty}\left(B_{\beta}\right)}+\|f\|_{\mathcal{C}^{\alpha}\left(B_{\beta}\right)}\right] .$$
Since $\Delta_{\widehat{g}_{\beta}} u=f-\sum_{j=3}^{2 n} D_{j}^{2} u$, (6.11) provides a bound for $\left\|\Delta_{\widehat{g}_{\beta}} u\right\|_{L^{\infty}\left(B_{\beta}^{\prime}\right)}$ in terms of $\|u\|_{L^{\infty}\left(B_{\beta}\right)}$ and $\|f\|_{L^{\infty}\left(B_{\beta}\right)}$.
6.5. $\mathcal{C}^{\alpha}$ estimates for the tangential derivatives. Let $p, q \in B_{\beta}^{\prime}{ }^{*}$ and let $d=$ $d_{\bar{g}_{\beta}}(p, q)$. By [GS21, Proposition 2.3], we have
$$\left|\left(D^{\prime \prime}\right)^{2} u(p)-\left(D^{\prime \prime}\right)^{2} u(q)\right| \leqslant C(n, \alpha)\left[d\|u\|_{L^{\infty}\left(B_{\beta}\right)}+d^{\alpha}\|f\|_{\mathcal{C}^{\alpha}\left(B_{\beta}\right)}\right] .$$
For the reader's convenience, we recall the main steps. We introduce the functions $v_{\kappa}$ playing the role of $u_{\kappa}$ but for the point $q$ instead of $p$. Choose $\kappa$ such
that $d \simeq \lambda^{\kappa+3}$ and assume $r(p)=\min (r(p), r(q)) \leqslant 2 d$ for simplicity. We have essentially three terms to treat
$$\underbrace{\left(D^{\prime \prime}\right)^{2} u(p)-\left(D^{\prime \prime}\right)^{2} u_{\kappa}(p)}_{=:(\mathrm{I})} ; \underbrace{\left(D^{\prime \prime}\right)^{2} u_{\kappa}(p)-\left(D^{\prime \prime}\right)^{2} u_{\kappa}(q)}_{=:(\text {II })} ; \underbrace{\left(D^{\prime \prime}\right)^{2} u_{\kappa}(q)-\left(D^{\prime \prime}\right)^{2} v_{\kappa}(q)}_{=:(\text {III })} .$$
The first term is easy to handle:
$$|(\mathrm{I})|=\lim _{N \rightarrow+\infty}\left|\sum_{j=\kappa}^{N}\left(D^{\prime \prime}\right)^{2} h_{j}(p)\right| \leqslant C(n) \sum_{j=\kappa}^{+\infty} \omega\left(\lambda^{j}\right) \leqslant C(n, \alpha) d^{\alpha}\|f\|_{\mathcal{C}^{\alpha}\left(B_{\beta}\right)} .$$
For the second term, we use the gradient estimate (6.4) for the harmonic function $\left(D^{\prime \prime}\right)^{2} h_{j}(2 \leqslant j \leqslant \kappa-1)$ :
$$\sup _{B_{\tilde{p}}\left(\lambda^{j}\right)}\left|\nabla^{\bar{g}_{\beta}}\left(D^{\prime \prime}\right)^{2} h_{j}\right| \leqslant C(n) \lambda^{-j} \omega\left(\lambda^{j}\right)$$
and after integration along the geodesic joining $p$ ang $q$ (which lies in $B_{\tilde{p}}\left(\lambda^{k}\right)^{*}$ )
$$\left|\left(D^{\prime \prime}\right)^{2} u_{j+1}(p)-\left(D^{\prime \prime}\right)^{2} u_{j+1}(q)\right| \leqslant\left|\left(D^{\prime \prime}\right)^{2} u_{j}(p)-\left(D^{\prime \prime}\right)^{2} u_{j}(q)\right|+C(n) d \lambda^{-j} \omega\left(\lambda^{j}\right)$$
and by iterating
$$|(\mathrm{II})| \leqslant\left|\left(D^{\prime \prime}\right)^{2} u_{2}(p)-\left(D^{\prime \prime}\right)^{2} u_{2}(q)\right|+C(n) d^{\alpha}\|f\|_{\mathcal{C}^{\alpha}\left(B_{\beta}\right)} .$$
The first term in the RHS is almost harmonic on a ball of definite size, so by using the gradient estimate (6.4), on can dominate it by $C(n) d\|u\|_{L^{\infty}\left(B_{\beta}\right)}$. As for the third term, the function $u_{\kappa}-v_{\kappa}$ is well-defined on $B_{\tilde{q}}\left(\lambda^{\kappa}\right)$, it is almost harmonic and its sup-norm on that ball is of order $\lambda^{2 \kappa} \omega\left(\lambda^{\kappa}\right)$ by (6.8). The gradient estimate for harmonic functions (Lemma 6.4) then provides the desired estimate.
6.6. $\mathcal{C}^{\alpha}$ estimates for the normal-tangential derivatives. In this paragraph, we explain the following estimate, cf [GS21, Propositions 2.4\&2.5]. The argument is somehow simplified here because we can choose an angle $2 \pi \beta<\pi$; this will simplify the application of Lemma 6.5. Let $p, q \in B_{\beta}^{\prime *}$ and let $d=$ $d_{\bar{g}_{\beta}}(p, q)$; then
$$\sum_{i=1}^{2} \sum_{j=3}^{2 n}\left|D_{i} D_{j} u(p)-D_{i} D_{j} u(q)\right| \leqslant C(n, \alpha)\left[d\|u\|_{L^{\infty}\left(B_{\beta}\right)}+d^{\alpha}\|f\|_{\mathcal{C}^{\alpha}\left(B_{\beta}\right)}\right] .$$
Again, we will only highlight the main steps, and focus on the $i=1$ case; i.e. we estimate the Hölder constant of $\partial_{r} D_{j} u$ for any $j \geqslant 3$. The case $i=2$, i.e. estimating $\frac{1}{\beta r} \partial_{\theta} D_{j} u$ is very similar. Borrowing the notation from § 6.5, Lemma 6.4 shows that the harmonic function $h_{\kappa}$ satisfies
$$\sup _{U_{\kappa+2}}\left|\nabla^{\bar{g} \beta} D^{\prime \prime} h_{\kappa}\right| \leqslant C(n) \omega\left(\lambda^{\kappa}\right) .$$
Similarly to (6.10), we have
$$\lim _{\kappa \rightarrow+\infty} \partial_{r} u_{\kappa}(p)=\partial_{r} u(p) ; \quad \lim _{\kappa \rightarrow+\infty} \partial_{r} D^{\prime \prime} u_{\kappa}(p)=\partial_{r} D^{\prime \prime} u(p),$$
cf [GS21, Lemma 2.10]. To estimate $\partial_{r} D^{\prime \prime} u(p)-\partial_{r} D^{\prime \prime} u(q)$, we fix the integer $\kappa$ so that $d \simeq \lambda^{\kappa+3}$ and we need to analyze the analogous terms (I)' $:=$ $\partial_{r} D^{\prime \prime} u(p)-\partial_{r} D^{\prime \prime} u_{\kappa}(p)$,
$$\text { (II)' }:=\partial_{r} D^{\prime \prime} u_{\kappa}(p)-\partial_{r} D^{\prime \prime} u_{\kappa}(q),$$
and (III)' $:=\partial_{r} D^{\prime \prime} u_{\kappa}(q)-\partial_{r} D^{\prime \prime} v_{\kappa}(q)$. The first term is dealt with just as in § 6.5 and the third one relies on the same arguments as before along with (6.14)-(6.15), cf [GS21, Lemma 2.11]. In the following, we thus focus on (II)'. As for its analog (II), the key point is to estimate
$$\text { (II)" }:=\partial_{r} D^{\prime \prime} h_{j}(p)-\partial_{r} D^{\prime \prime} h_{j}(q),$$
for any $2 \leqslant j \leqslant \kappa-1$ since $u_{2}$ is almost harmonic on $B_{\tilde{p}}(\lambda)$ and Lemma 6.5 shows that the $\bar{g}_{\beta}$-gradient of $\partial_{r} D^{\prime \prime} u_{2}$ is bounded on that ball. Set $w_{j}:=\partial_{r} D^{\prime \prime} h_{j}$, defined on $U_{j+1}$. We distinguish two cases.
- Case 1. $U_{\kappa}$ is centered on the divisor.
In particular, any $U_{j}(2 \leqslant j \leqslant \kappa-1)$ is centered on the divisor as well. The estimate (6.7) in Lemma 6.5 shows that for $\beta$ small enough ( $\beta<\frac{1}{2}$ would suffice), $\nabla^{\bar{g}_{\beta}} w_{j}$ is bounded on $B_{\tilde{p}}\left(\frac{3}{2} \lambda^{j}\right) \supset B_{p}(2 d)$ by $C(n) \lambda^{-j} \omega\left(\lambda^{j}\right)$.
- Case 2. $U_{\kappa}$ is centered at $p$.
Necessarily, we have $r(p) \geqslant \lambda^{\kappa} \simeq 8 d$. Along a geodesic $\gamma(t)$ joining $p$ to $q$, we have the inequality $r(\gamma(t)) \geqslant \frac{r(p)}{2}$ since the distance from $p$ to a point $p^{\prime}$ with $r\left(p^{\prime}\right) \leqslant r(p) / 2$ is at least $r(p) / 2 \geqslant 2 d$. The geodesic $\gamma$ lies in $B_{p}\left(\lambda^{\kappa}\right)$ hence equation (6.5) in Lemma 6.4 shows that for any $j, \nabla^{\bar{z}} \beta w_{j}$ is bounded by $C(n) \lambda^{-j} \omega\left(\lambda^{j}\right)$ along $\gamma$.

The case by case analysis above has therefore shown that $\left|w_{j}(p)-w_{j}(q)\right| \leqslant$ $C(n) \lambda^{-j} \omega\left(\lambda^{j}\right) \cdot d$ and we can conclude as in § 6.5.
6.7. Strong Schauder estimate. In this section, we intend to improve Theorem 6.1 by controlling the $\mathcal{C}^{\alpha}$ norm of the non-mixed derivatives of order two of a solution $u$ of the equation $\Delta_{\bar{g}_{\beta}} u=f$, that is to get an estimate of $\left\|\nabla_{\bar{g}_{\beta}}^{2} u\right\|_{\mathcal{C}^{\alpha}}$. As we will later see, it all comes down to the following one-dimensional problem.

Proposition 6.6. Assume that $n=1$. Let $u \in L^{\infty}\left(B_{\beta}\right)$ solve $\Delta_{\bar{g}_{\beta}} u=f$ for some $f \in \mathcal{C}^{\alpha}\left(B_{\beta}\right)$. Then $u \in \mathcal{C}^{2, \alpha}\left(B_{\beta}\right)$ and there exists a constant $C=C(n, \alpha)$ such that for all $\beta \in\left(0, \frac{1}{4}\right]$ one has
$$\|u\|_{\mathcal{C}^{2, \alpha}\left(B_{\beta}^{\prime}\right)} \leqslant C\left(\|f\|_{\mathcal{C}^{\alpha}\left(B_{\beta}\right)}+\|u\|_{\mathcal{C}^{0}\left(B_{\beta}\right)}\right) .$$

Corollary 6.7 (Strong Schauder estimate). The full Schauder estimate (6.16) holds in any dimension.

Here, the $\mathcal{C}^{2, \alpha}$ norm $D \subset B_{\beta}$ is defined by
$$\|u\|_{C^{2, \alpha}}=\sup _{B_{\beta}} \sum_{0 \leq j \leq 2}\left|\nabla^{j} u\right|_{\bar{g}_{\beta}}+\left[\nabla^{2} u\right]_{\alpha}$$
where
$$[v]_{\alpha}=\sup _{x, y \in B_{\beta} ;|r(x)-r(y)|<\frac{r(x)}{2}} \frac{|v(x)-v(y)|}{d_{\bar{g}_{\beta}}(x, y)^{\alpha}} .$$

This Hölder semi-norm is quite convenient to manipulate as we will see later, and it is well-known that it is equivalent to the usual Hölder semi-norm $\|v\|_{\alpha}:=\sup _{x, y} \frac{|v(x)-v(y)|}{d_{\tilde{g}_{\beta}}(x, y)^{\alpha}}$.

Remark 6.8. By classical arguments (see e.g. [Don12, § 4.2], [GS18, § 3.5]), the result of Corollary 6.7 for the flat cone metric extends to perturbations $\Delta_{\bar{g}_{\beta}}+$ $a_{\beta} \cdot \nabla^{2}+b_{\beta} \cdot \nabla$, provided the tensors $a_{\beta}$ and $b_{\beta}$ are small enough in $C^{\alpha}$ norm. It is easy to check that the uniformity with respect to $\beta$ is preserved provided $a_{\beta}$ and $b_{\beta}$ are uniformly small, more precisely for some $\varepsilon=\varepsilon(n, \alpha)>0$ small enough, one has for all $\beta \in\left(0, \frac{1}{4}\right]$
$$\left\|a_{\beta}\right\|_{C^{\alpha}\left(\bar{g}_{\beta}\right)}+\left\|b_{\beta}\right\|_{C^{\alpha}\left(\bar{g}_{\beta}\right)}<\varepsilon .$$
Proof of Proposition 6.6. The proof of Proposition 6.6 consists in three steps. First, we show that is is enough to prove the estimate for functions $u$ which vanish on $\partial B_{\beta}$ and whose integral on every circle $\{r=\mathrm{cst}\}$ is zero. Next, we show that for such functions $u$, the norm $\left\|u / r^{2+\alpha}\right\|_{\mathcal{C}^{0}}$ is controlled by $\|u\|_{\mathcal{C}^{0}}+\|f\|_{\mathcal{C}^{\alpha}}$. Finally, we combine the previous results and Schauder's estimate for the cylindrical metric to conclude.
- Step 1. The reduction step. First, we decompose $u=h+v$ where $h$ is harmonic on $B_{\beta}$ with $\left.h\right|_{\partial B_{\beta}}=\left.u\right|_{\partial B_{\beta}}$ and $v$ solving $\Delta_{\bar{g}_{\beta}} v=f,\left.v\right|_{\partial B_{\beta}} \equiv 0$. All the usual derivatives of $h$ are controlled by it sup norm, itself controlled by its boundary value, hence by $\|u\|_{\mathcal{C}^{0}}$. Moreover, the formulas (6.1)-(6.2) show that $\left\|\nabla_{\bar{g}_{\beta}}^{3} h\right\|_{\mathcal{C}^{0}}$ is controlled by $\beta^{-3} r^{1 / \beta-3}\left\|\nabla_{\text {eucl }}^{3} h\right\|_{\mathcal{C}^{0}}$. Therefore, Schauder's estimate for $v$ implies that for $u$.

Next, we write $\mathbb{C}^{*}=\mathbb{R}_{+}^{*} \times S^{1}$ and we expand $v$ in Fourier series $v=v_{0}(r)+$ $\tilde{v}$ where $\tilde{v}=\sum_{n \geqslant 1} v_{n}(r) e^{i n \theta}$. The function $\tilde{v}$ has integral zero on each circle, hence $\left.\tilde{v}\right|_{\partial B_{\beta}} \equiv 0$. As $v_{0}(r)=\frac{1}{2 \pi r} \int_{|z|=r} v$, both $\left\|v_{0}\right\|_{\mathcal{C}^{0}}$ and $\|\tilde{v}\|_{\mathcal{C}^{0}}$ are controlled by $\|v\|_{\mathcal{C}^{0}}$. Since $\Delta_{\bar{g}_{\beta}}$ respects the decomposition, the Fourier series expansion of $f=f_{0}(r)+\tilde{f}$ is given by $\Delta_{\bar{g}_{\beta}} v_{0}+\Delta_{\bar{g}_{\beta}} \tilde{v}$. It is easy to check that $\left\|f_{0}\right\|_{\mathcal{C}^{\alpha}} \leqslant$ $\|f\|_{\mathcal{C}^{\alpha}}$. From this one infers two things: first, $\left\|v_{0}\right\|_{\mathcal{C}^{2, \alpha}}$ is under control (e.g. by explicitly solving the ODE $\left.\left(\partial_{r}^{2}+r^{-1} \partial_{r}\right) v_{0}=f_{0}\right)$ and next, $\tilde{f}$ is $\mathcal{C}^{\alpha}$ and $\|\tilde{f}\|_{\mathcal{C}^{\alpha}}$ is under control as well.

Therefore, Schauder's estimate for $\tilde{v}$ implies Schauder's estimate for $v$, hence for $u$ as well. This shows that it is enough to restrict ourselves to functions $u$ which vanish on $\partial B_{\beta}$ and whose integral on each circle $\{|z|=r\}$ is zero.
- Step 2. The improved uniform estimate. In this step, we show that for $u$ satisfying $\left.u\right|_{\partial B_{\beta}} \equiv 0$ and $\int_{|z|=r} u=0$ for any $r$, then there exists a constant
$C>0$ independent of $\beta$ such that
$$\left\|u / r^{2+\alpha}\right\|_{\mathcal{C}^{0}\left(B_{\beta}^{\prime}\right)} \leqslant C\|f\|_{\mathcal{C}^{\alpha}\left(B_{\beta}\right)} .$$
Set $\rho:=\frac{1}{2}$. From (6.3), we have
$$u(z)=\rho^{2} \int_{|w|<1} \frac{\beta^{2}}{|w|^{2(1-\beta)}} f\left(\rho^{1 / \beta} w\right) \log \left|\frac{\rho^{-1 / \beta_{z}} z-w}{1-\rho^{-1 / \beta} \bar{z}}\right||d w|^{2}$$
The integral of $u$ along any circle $\{|w|=s\}$ is zero, so the same is true for $f$. This implies that
$$\begin{aligned}
u(z) & =\rho^{2} \int_{|w|<1} \frac{\beta^{2}}{|w|^{2(1-\beta)}} f\left(\rho^{1 / \beta} w\right) \log \left|\frac{\rho^{-1 / \beta} z / w-1}{1-\rho^{-1 / \beta} \bar{z} \bar{w}}\right||d w|^{2} \\
& =\beta^{2}|z|^{2 \beta} \int_{|t|>\rho^{-1 / \beta}|z|} f\left(\rho^{1 / \beta} w\right) \log \left|\frac{t-1}{1-\rho^{-2 / \beta}|z|^{2} / t}\right| \frac{|d t|^{2}}{|t|^{2+2 \beta}}
\end{aligned}$$
after performing the change of variables $t:=\rho^{-1 / \beta} z / w$. Since $f(0)=0$, we have $|f| \leqslant C_{\alpha}\|f\|_{\mathcal{C}^{\alpha}} \cdot r^{\alpha}$ and therefore
$$\left|\frac{u(z)}{r^{2+\alpha}}\right| \leqslant C_{\alpha}\|f\|_{\mathcal{C}^{\alpha}} \cdot \underbrace{\beta^{2} \int_{|t|>\rho^{-1 / \beta}|z|} \log \left|\frac{t-1}{1-\rho^{-2 / \beta}|z|^{2} / t}\right| \frac{|d t|^{2}}{|t|^{2+2 \beta}}}_{=: I(z)} .$$
We are left to bounding the integral $I(z)$ uniformly for all $\beta$ and all $z \in B_{\beta}^{\prime}$. When $|t|$ is very small, say $|t| \leqslant \varepsilon$, then $\rho^{-1 / \beta}|z|<\varepsilon$ and the log term is a $O(t)+O\left(\rho^{-1 / \beta}|z|\right)=O(t)$ hence this portion of the integral is dominated by $\beta^{2} \int_{s=0}^{\varepsilon} \frac{d s}{s^{2 \beta}}=O(1)$. For the rest of the integral, we first observe that for $z \in B_{\beta^{\prime}}^{\prime}$ we have $\left.\left|\rho^{-2 / \beta}\right| z\right|^{2} / t \mid \leqslant \rho^{1 / \beta}$ hence
$$\beta^{2} \int_{|t|>\varepsilon}-\left.\log \left|1-\rho^{-2 / \beta}\right| z\right|^{2} / t \left\lvert\, \frac{|d t|^{2}}{|t|^{2+2 \beta}} \leqslant \beta^{2} \int_{s=\varepsilon}^{+\infty} \frac{d s}{s^{1+2 \beta}}=O(1) .\right.$$
We are left to estimating $\beta^{2} \int_{|t|>\varepsilon} \log |t-1| \frac{|d t|^{2}}{|t|^{2+2 \beta}}$. The region $\varepsilon \leqslant|t| \leqslant 2$ is trivially dealt with, while the remaining region is estimated by
$$\int_{s=2}^{+\infty} \frac{\log s}{s^{1+2 \beta}} d s=\frac{1}{\gamma \beta}\left[s^{-\gamma \beta}\left(\log s-\frac{1}{\gamma \beta}\right)\right]_{2}^{+\infty}=O\left(\beta^{-2}\right)$$
where $\gamma=(2+\alpha)$. The estimate (6.18) is now proved.
- Step 3. Schauder estimates for the cylinder. Set $t:=\log r$ so that $\bar{g}_{\beta}=r^{2} g_{c}$ where $g_{c}:=d t^{2}+\beta^{2} d \theta^{2}$ to be the cylindrical metric on $\mathbb{R} \times S^{1}$, where the circle has length $2 \pi \beta$. It is complete with bounded curvature hence it satisfies uniform Schauder estimates independent of $\beta$ and the chosen ball of a given radius (small balls may not be simply connected but one can pass to the universal cover).

Let us pick an arbitrary point $x_{0} \in B_{\beta}^{\prime}$ and set $r_{0}:=r\left(x_{0}\right)$. We define the regions $D:=\left\{\left|t-t_{0}\right|<2\right\}$ and $D^{\prime}:=\left\{\left|t-t_{0}\right|<1\right\}$; these depend on the base point $x_{0}$. On $D$, the function $\frac{r}{r_{0}}=e^{t-t_{0}}$ has bounded $g_{c}$-derivatives at every
order (and the same holds for its inverse), and these bounds are independent of $x_{0}$. On $D$, we have $\left\|\nabla_{g_{c}}^{j} u\right\|_{\mathcal{C}^{0}} \sim r_{0}^{j}\left\|\nabla_{\bar{g}_{\beta}}^{j} u\right\|_{\mathcal{C}^{0}}$ and $\|v\|_{\mathcal{C}_{g c}^{\alpha}(D)} \sim r_{0}^{\alpha}\|v\|_{\mathcal{C}_{\bar{g} \beta}^{\alpha}(D)}$ by the definition of the Hölder norm for $\bar{g}_{\beta}$, cf (6.17). By the same token, $\left\|r^{2} f\right\|_{\mathcal{C}_{g c}^{\alpha}(D)} \sim$ $r_{0}^{2+\alpha}\|f\|_{\mathcal{C}_{\bar{\delta}_{\beta}}^{\alpha}(D)}$.

This implies that
$$\begin{aligned}
\|u\|_{\mathcal{C}_{\tilde{\mathcal{Z}}_{\beta}}^{2, \alpha}\left(D^{\prime}\right)} & \lesssim r_{0}^{-2-\alpha}\|u\|_{\mathcal{C}_{g c}^{2, \alpha}\left(D^{\prime}\right)} \\
& \leqslant C\left(\left\|u / r_{0}^{2+\alpha}\right\|_{\mathcal{C}^{0}(D)}+\|f\|_{\mathcal{C}_{\hat{\delta}_{\beta}}^{\alpha}(D)}\right)
\end{aligned}$$
where the last inequality follows from Schauder estimates for the cylindrical metric, since $\Delta_{g_{c}} u=r^{2} f$. Putting (6.18) and (6.20) together, we conclude that $\|u\|_{\mathcal{C}_{\tilde{g}_{\beta}}^{2, \alpha}\left(D^{\prime}\right)} \leqslant C\|f\|_{\mathcal{C}_{\tilde{g}_{\beta}}^{\alpha}(D)}$ for some constant $C$ independent of $\beta$ and $x_{0}$. By varying the point $x_{0}$ across $B_{\beta}^{\prime}$ and using the first reduction step, we obtain the proposition. \(\square\)

Proof of Corollary 6.7. We are left to showing that the $\mathcal{C}^{\alpha}$ norms of $\partial_{r}^{2} u$ and $\frac{1}{\beta r^{2}} \partial_{\theta}^{2} u$ are controlled by $\|u\|_{\mathcal{C}^{0}}+\|f\|_{\mathcal{C}^{\alpha}}$. We will treat the term $v:=\partial_{r}^{2} u$, the other one being entirely similar. Let $x, y \in B_{\beta}^{\prime}$ which we write $\left(z_{1}, z_{1}^{\prime}\right)$ and $\left(z_{2}, z_{2}^{\prime}\right)$ where $z_{i}^{\prime} \in \mathbb{C}^{n-1}$ for $i=1,2$. We set $t=\left(z_{2}, z_{1}^{\prime}\right)$ and decompose the difference $v(x)-v(y)=(v(x)-v(t))+(v(t)-v(y))$. On the slice $S_{z_{1}^{\prime}}:=\mathbb{C}^{*} \times\left\{z_{1}^{\prime}\right\}$, the function $u$ satisfies $\Delta_{\hat{g}_{\beta}} u=f-\Delta_{\mathbb{C}^{n-1}} u$ and the $\mathcal{C}^{\alpha}$ norm of the RHS is controlled by Theorem 6.1. By Proposition 6.6, we get that
$$|v(x)-v(t)| \leqslant C d_{\hat{g}_{\beta}}\left(z_{1}, z_{2}\right)^{\alpha} \leqslant C d_{\bar{g}_{\beta}}(x, y)^{\alpha}$$
where $C$ is some uniform multiple of $\|u\|_{\mathcal{C}^{0}}+\|f\|_{\mathcal{C}^{\alpha}}$.
We now have to take care of $v(t)-v(y)$. The geodesic from $t$ to $y$ lies in the "euclidean slice" $\tilde{S}_{z_{2}}=\left\{z_{2}\right\} \times \mathbb{C}^{n-1}$ so we only have to estimate $D^{\prime \prime} v=$ $\partial_{r}^{2} D^{\prime \prime} u$ along $\tilde{S}_{z_{2}}$. But this is entirely similar to what has been done in § 6.6 by using almost harmonic approximations and relying on (6.5)-(6.7) depending on whether $d_{\bar{g}_{\beta}}(t, y)=d_{\text {eucl }}\left(z_{1}^{\prime}, z_{2}^{\prime}\right)$ dominates or not $r(t)=r(y)=\left|z_{2}\right|^{\beta}$. \(\square\)

\section*{7. Schauder estimate for collapsed metrics}

In this section we establish the uniform Schauder estimates which are at the heart of our argument. The important point here is the existence of different scales at which we can look at the geometry, since the metrics $g_{\beta, L}$ (hence $g_{\beta}$ ) collapse much quicker in the circle direction of the bundle $L$ over $D$ (scale $\beta$ ) than in the directions of $D$ (scale $\sqrt{\beta}$ ). Since we have here two different speeds for the collapsing, we call this geometry '2-collapsed'. We will also need to consider an intermediate '1-collapsed' geometry, more precisely:
\begin{itemize}
\item[-] 1-collapsed geometry: this is a scale at which the circle collapses but the divisor does not collapse; this roughly amounts to consider the metrics $\frac{1}{\beta} g_{\beta}$, which turn out to have controled curvature so that we can
\end{itemize}
\begin{itemize}
\item[] obtain Schauder estimates from standard arguments far from the divisor $D$, and near the divisor $D$ with the conical singularities from the estimates developed in section 6; this is done in section 7.2;
\item[-] 2-collapsed geometry: this is the scale of $g_{\beta, L}$, and it turns out that in our problem we need estimates at this scale, on balls of fixed radius, say $\varrho$, for $g_{\beta, L}$; this corresponds to balls of larger and larger radius $\frac{\varrho}{\sqrt{\beta}}$ in the 1-collapsed geometry of $\frac{1}{\beta} g_{\beta, L}$; we obtain these estimates in section 7.3 from a global estimate on some limit of $\frac{1}{\beta} g_{\beta, L}$.
\end{itemize}

Notation. Since we have a lot of constants appearing in our estimates, from now we simplify the notation by introducing the relations
$$A \lessapprox B \quad \text { resp. } \quad A \approx B$$
defined by the fact that there is some constant $\mathfrak{C}_{n}$ depending only on the dimension $n$ (and certainly not on $\beta$ ) such that
$$A \leq \mathfrak{C}_{n} B \quad \text { resp. } \quad \mathfrak{C}_{n}^{-1} B \leq A \leq \mathfrak{C}_{n} B .$$
7.1. Functional spaces. We now define the functional spaces in which we will solve the equation. These are weighted Hölder spaces.

With the notation of section 5.3, we define a weight on $X$ by
$$w_{\beta}=\chi(-\tilde{u})-(1-\chi(-\tilde{u})) \tilde{u}$$
so that $w_{\beta}=1$ for $u \leq-2$ and $w_{\beta}=\tilde{u}$ for $u \geq-\frac{1}{2}$.
Fix a real number $\delta$. For any section $f$ of a tensor bundle, we define the weighted norm (which depends on $\beta$ ):
$$\|f\|_{C_{\delta}^{\ell, \alpha}}=\sup \sum_{0 \leq j \leq \ell} w_{\beta}^{\delta+\frac{j}{2}\left(1+\frac{1}{n}\right)}\left|\nabla^{j} f\right|_{g_{\beta}}+\left[w_{\beta}^{\delta+\frac{\ell}{2}\left(1+\frac{1}{n}\right)} \nabla^{\ell} f\right]_{\alpha}$$
where the semi-norm $[f]_{\alpha}$ is also weighted:
$$[f]_{\alpha}=\sup _{d_{g_{\beta}}(x, y)<\rho\left(\beta w_{\beta}^{\frac{1}{n}}(x)\right)^{\frac{1}{2}}}\left(\beta w_{\beta}^{\frac{1}{n}}\right)^{\frac{\alpha}{2}} \frac{|f(x)-f(y)|}{d_{g_{\beta}}(x, y)^{\alpha}} .$$
One can be surprised by these definitions, since (7.2) and (7.3) do not correspond to the same weight: roughly speaking the norm $\|f\|_{C^{0}}+[f]_{\alpha}$ is a $C^{\alpha}$ norm with respect to the metric $\beta^{-1} w^{-\frac{1}{n}} g_{\beta}$, a metric which looks like:
\begin{itemize}
\item[-] $\beta^{-1} g_{\beta}$ on $u \leq-1$ : this has bounded curvature by Lemma 3.1;
\item[-] $\beta^{-1-\frac{1}{n}} g_{\beta}$, that is $g_{T Y}$ on the compact part of $X \backslash U_{L}$;
\end{itemize}
in both cases the point is that the geometry is controlled so that there are uniform Schauder estimates.

On the other hand, the $C^{\ell}$ norm defined by (7.2) has a different weight, motivated by the fact that $\left|\nabla^{j} w_{\beta}^{\bullet}\right|_{g_{\beta}}=O\left(w_{\beta}^{\bullet-\frac{j}{2}\left(1+\frac{1}{n}\right)}\right)$, so it is well-adapted to functions depending on $u$ only: we will see that these are the functions on which we have the worst estimates, because the other directions collapse.

Remark 7.1. Despite the presence of the weight, one still has the usual estimate for products in Hölder spaces: $\|f g\|_{C^{\alpha}} \leq\|f\|_{C^{\alpha}}\|g\|_{C^{\alpha}}$. This is because for the standard Hölder norms one has actually $[f g]_{\alpha} \leq\|f\|_{C^{0}}[g]_{\alpha}+[f]_{\alpha}\|g\|_{C^{0}}$, so adding our weight $\beta w_{\beta}^{\frac{1}{n}}$ does not change the estimate.
7.2. 1-collapsed Schauder estimate. From Lemma 3.1 we have the following bound for the curvature of $g_{\beta, L}$ :
$$\left|K\left(g_{\beta, L}\right)\right| \lessapprox\left(\frac{1}{\left(-\varphi_{1}^{\prime}(u)\right)^{n+1}}+\frac{1}{-\beta \varphi_{1}^{\prime}(u)}\right) .$$
Since $\varphi_{1}^{\prime}(u) \sim c_{n}(-u)^{\frac{1}{n}}$ when $u \rightarrow 0$, then for $u<-\frac{\beta}{A}$ for some $A>0$ which will be fixed below, we have for $B=\operatorname{cst} .(1+A)$,
$$\left|K\left(g_{\beta, L}\right)\right| \leq \frac{B}{-\beta \varphi_{1}^{\prime}(u)} .$$
Since $u=\beta t$, the region $u<-\frac{\beta}{A}$ corresponds to the region $t<-\frac{1}{A}$ in the Tian-Yau space, that is the exterior of a compact region. We choose that compact region large enough, that is $A>0$ small enough, so that the asymptotics of the Tian-Yau metric written in section 5.1 are valid. From the estimate (5.9) on the difference $g_{\beta}-g_{\beta, L}$ we see that (7.5) remains true for $g_{\beta}$. For simplicity we write the sequel for $g_{\beta, L}$ but these bounds imply that our estimates will remain true for the small perturbation $g_{\beta}$.

Since $\varphi_{1}^{\prime \prime}(u) \approx e^{u}$ by (2.17), the distance $r_{D}$ from the divisor is of order $r_{D} \approx$ $e^{\frac{u}{2}}$. Therefore a region $r_{D}>\varepsilon$ corresponds to $u>2 \log \varepsilon+\mathrm{cst}$.

We will also use the function $r_{0}(u)$ which is the distance to the point $u=0$, so that when $u \rightarrow 0$ one has
$$r_{0}(u) \approx|u|^{\frac{1}{2}+\frac{1}{2 n}} .$$

Note $\rho$ the injectivity radius of the metric $g_{D}$, and fix a finite number of balls of radius $\rho$ covering $D$. Near some $u_{0}<-\frac{\beta}{A}$ we can consider the rescaled metric $h=\frac{g_{\beta, L}}{-\beta \varphi_{1}^{\prime}\left(u_{0}\right)}$. This is the metric where only the $S^{1}$ fibres are collapsed, at speed $\sqrt{\beta}$ ('1-collapse'). For $u \approx u_{0}$ the curvature of $h$ is uniformly bounded and $h \simeq \frac{\varphi_{1}^{\prime \prime}(u)}{-4 \beta \varphi_{1}^{\prime}\left(u_{0}\right)}\left(2 d u^{2}+\beta^{2} \eta^{2}\right)+g_{D}$. Because of the $S^{1}$-bundle over $D$, small balls of radius $\rho$ for $h$ are not simply connected but we can use Schauder estimates in local universal coverings. We define the domain
$$D_{u_{0}}(\tau)=\left\{\left|r_{0}(u)-r_{0}\left(u_{0}\right)\right| \leq \tau \sqrt{\beta w_{\beta}\left(u_{0}\right)^{\frac{1}{n}}}\right\}$$
and we assume the extra condition $r_{D}\left(u_{0}\right)>\varepsilon \sqrt{\beta}$, that is $u_{0}>\log \beta+2 \log \varepsilon+$ cst. Said otherwise, we only look at points at a fixed, positive distance to the divisor $D$ with respect to $h$. We can then check that $D_{u_{0}}(\rho) \subset B_{h}\left(u_{0}, C \rho\right)$ and that on $D_{u_{0}}(\rho)$, we have $\frac{u_{0}}{u} \lessapprox 1$ (this can be done easily by treating each case $u_{0} \approx-\infty,-1,0$ separately and using the assumption $r_{D}\left(u_{0}\right)>\varepsilon \sqrt{\beta}$.) These considerations lead to the following Schauder estimate for the metric $h$ outside
the divisor:
$$\|f\|_{C_{h}^{2, \alpha}\left(D_{u_{0}}\left(\frac{1}{2} \rho\right)\right)} \lessapprox\left(\|f\|_{C^{0}\left(D_{u_{0}}(\rho)\right)}+\left\|\Delta_{h} f\right\|_{C_{h}^{\alpha}\left(D_{u_{0}}(\rho)\right)}\right)$$
which we rewrite in terms of $g_{\beta}$ using the weighted norm (7.3):
$$\left\|\nabla^{2} f\right\|_{C_{0}^{\alpha}\left(D_{u_{0}}\left(\frac{1}{2} \rho\right)\right)} \lessapprox \frac{1}{\beta w_{\beta}\left(u_{0}\right)^{\frac{1}{n}}}\|f\|_{C^{0}\left(D_{u_{0}}(\rho)\right)}+\left\|\Delta_{g_{\beta}} f\right\|_{C_{0}^{\alpha}\left(D_{u_{0}}(\rho)\right)} .$$
Note that this estimate extends everywhere:
\begin{itemize}
\item[-] Near the divisor we have the same by taking balls centered on the divisor and applying the uniform Schauder estimate established in section 6 to the metric $h=\frac{g_{\beta}}{\beta}$. More precisely, if $u_{0}=-\infty$ and $\rho>0$ is small enough one has $D_{-\infty}(\rho)=\{r<\rho \sqrt{\beta}\}$ which is topologically a disk in $\mathbb{C}$ times $D$. The change of variable $R=r / \sqrt{\beta}$ in (2.19) gives
$$h=\frac{g_{\beta}}{\beta}=\frac{2}{n+1}\left(d R^{2}+\beta^{2} R^{2} \eta^{2}\right)+g_{D}+O\left(\beta R^{2}\right) .$$
Maybe up to scaling again by a large constant, we see that we have locally a uniformly small (in the sense of Remark 6.8) perturbation of the product of the cone metric $d R^{2}+\beta^{2} R^{2} d \theta^{2}$ with the flat metric, and therefore we can apply Corollary 6.7 to get
$$\|f\|_{C_{h}^{2, \alpha}\left(D_{-\infty}\left(\frac{1}{2} \rho\right)\right)} \lessapprox\left(\|f\|_{C^{0}\left(D_{-\infty}(\rho)\right)}+\left\|\Delta_{h} f\right\|_{C_{h}^{\alpha}\left(D_{-\infty}(\rho)\right)}\right)$$
and the corresponding inequality (7.7) in terms of $g_{\beta}$ (with the weighted norm - in this region we have $w_{\beta} \equiv 1$ ) is also valid for $D_{-\infty}(\rho)$. Therefore, it holds any $u_{0}<-\frac{\beta}{A}$.
\item[-] On the Tian-Yau part $X \backslash U_{L}$, this is the standard Schauder estimate, since the scaling factor with the Tian-Yau metric is $\beta w_{\beta}\left(u_{0}\right)^{\frac{1}{n}}=\beta^{1+\frac{1}{n}}$.
\end{itemize}
7.3. 2-collapsed Schauder estimate. Our aim now is to give an estimate more suitable for the scale of $g_{\beta}$, where the the divisor $D$ is also collapsed at speed $\sqrt{\beta}$, and the circle at speed $\beta$ ('2-collapse'). More precisely, we want to replace by a better coefficient the factor $\frac{1}{\beta w_{\beta}\left(u_{0}\right)^{\frac{1}{n}}}$ in (7.7). For $u_{0}$ bounded away from zero, this is just the scaling factor $\frac{1}{\beta}$. We do this in two steps: decomposing in Fourier series along the circle, a direct application of the maximum principle gives the required estimates on nonzero modes. For zero modes, the argument is more complicated: instead of estimates on balls of radius $\frac{1}{\sqrt{\beta}}$ as above, we would like estimates on balls of fixed radius, say $\rho$ if $u$ is far from 0 or $-\infty$. In the rescaled metric $\frac{1}{\beta} g_{\beta, L}$ this corresponds to a cylinder of length approximately $\frac{\rho}{\sqrt{\beta}}$, converging to an infinite cylinder. The estimates on this limit will provide the estimates we need.

For small values of $\varepsilon$ and $u_{0}$ away from the divisor, we define the region
$$E_{u_{0}}(\varepsilon)=\left\{\left|r_{0}(u)-r_{0}\left(u_{0}\right)\right| \leq \varepsilon r_{0}\left(u_{0}\right)\right\} .$$

If $u_{0}=-\infty$ that is we consider the divisor $D$, we use
$$E_{-\infty}(\varepsilon)=\left\{\left|r_{D}(u)\right| \leq \varepsilon\right\} .$$
Notice that for $\varepsilon>0$ and $u_{0}$ small, $\varphi_{1}^{\prime}(u)$ and $\varphi_{1}^{\prime \prime}(u)$ do not vary much in $E_{u_{0}}(\varepsilon)$, that is remain comparable to their value at $u_{0}$.

The regions $E_{u_{0}}$ correspond to the scale of the geometry of $g_{\beta}$, and are therefore very large for the geometry of the previously used $h=\frac{g_{\beta, L}}{-\beta \varphi_{1}^{\prime}\left(u_{0}\right)}$. We then obtain the better estimate:

Proposition 7.2.
$$\left\|\nabla^{2} f\right\|_{C_{0}^{\alpha}\left(E_{u_{0}}\left(\frac{1}{2} \varepsilon\right)\right)} \lessapprox\left\|\Delta_{g_{\beta}} f\right\|_{C_{0}^{\alpha}\left(E_{u_{0}}(\varepsilon)\right)}+w_{\beta}\left(u_{0}\right)^{-1-\frac{1}{n}}\|f\|_{C^{0}\left(E_{u_{0}}(\varepsilon)\right)} .$$

Remark that on the Tian-Yau part $X \backslash U_{L}$ the function $w_{\beta}$ takes the value $\beta$ so this is the same estimate as in (7.7). But the important point is that on $\{u \leqslant-1\}$ the factor $w_{\beta}$ does not depend on $\beta$, contrarily to the initial estimate (7.7). We deduce the following corollary:

Corollary 7.3. One has the following uniform estimate, for all functions $f$ on $X$ :
$$\|f\|_{C_{\delta}^{2, \alpha}} \lessapprox\|f\|_{C_{\delta}^{0}}+\left\|\Delta_{g_{\beta}} f\right\|_{C_{\delta+1+\frac{1}{n}}^{\alpha}} .$$ \(\square\)

Remark 7.4. The estimate $\|f\|_{C_{\delta}^{2, \alpha}} \lessapprox\|f\|_{C_{\delta}^{0}}+\left\|L_{\beta} f\right\|_{C_{\delta+1+\frac{1}{n}}^{\alpha}}$ follows for any operator of the shape say $L_{\beta}=\Delta_{g_{\beta}}+c$ where $c$ is a constant, as one sees immediately using the interpolation estimate $\|f\|_{C^{\alpha}} \lessapprox \varepsilon^{-\alpha}\|f\|_{C^{0}}+\varepsilon^{\alpha}\|f\|_{C^{1}}$ for any fixed $0<\varepsilon \ll 1$.

The rest of this section is devoted to the proof of the estimate (7.10). Again from the bounds on $g_{\beta}-g_{\beta, L}$ it is sufficient to prove the estimate on $g_{\beta, L}$.

First step. We first decompose along each circle into Fourier series $f=\sum_{\mathbb{Z}} f_{\ell}$ and control nonconstant modes. Here, more precisely, we see $L$ as a $S^{1}$ bundle over $\mathbb{R}_{-} \times D$, and $f_{\ell}$ is induced from a section $F_{\ell}$ of $p^{*} L^{-\ell}$ over $\mathbb{R}_{-} \times D$ by the formula $f_{\ell}(x)=\left\langle F_{\ell}(p(x)), x^{\otimes \ell}\right\rangle$. On $p^{*} L^{-\ell}$ over $D$ we have the rough Laplacian $-\Delta_{D}:=\nabla^{*} \nabla$ constructed from the given connection on $L$ and the metric $g_{D}$.

The Laplacian of the metric $g_{\beta, L}$ preserves the Fourier decomposition and acts on $F_{\ell}$ by
$$\begin{aligned}
\Delta_{g_{\beta, L}} F_{\ell} & =\frac{2}{\varphi_{1}^{\prime \prime}(u)}\left(\partial_{u}^{2} F_{\ell}-\frac{\ell^{2}}{4 \beta^{2}} F_{\ell}\right)+\frac{2(n-1)}{\varphi_{1}^{\prime}(u)} \partial_{u} F_{\ell}+\frac{1}{-\beta \varphi_{1}^{\prime}(u)} \Delta_{D} F_{\ell} \\
& =\Delta_{\mathbb{R}_{-} \times D} F_{\ell}-\frac{\ell^{2}}{2 \varphi_{1}^{\prime \prime}(u) \beta^{2}} F_{\ell}
\end{aligned}$$

Lemma 7.5. Fix $\varepsilon>0$ small enough and $\ell \neq 0$. We have the estimate
$$\sup _{E_{u_{0}\left(\frac{1}{2} \varepsilon\right)}}\left|f_{\ell}\right| \lessapprox \frac{\beta}{\ell^{2}} \sup _{E_{u_{0}}(\varepsilon)}\left(w_{\beta}\left(u_{0}\right)^{\frac{1}{n}}\left|\Delta f_{\ell}\right|+w_{\beta}\left(u_{0}\right)^{-1}\left|f_{\ell}\right|\right) .$$

It follows that
$$\sup _{E_{u_{0}}\left(\frac{1}{2} \varepsilon\right)}\left|f-f_{0}\right| \lessapprox \beta \sup _{E_{u_{0}}(\varepsilon)}\left(w_{\beta}\left(u_{0}\right)^{\frac{1}{n}}\left|\Delta\left(f-f_{0}\right)\right|+w_{\beta}\left(u_{0}\right)^{-1}\left|f-f_{0}\right|\right) .$$
Proof. Let us first explain how to derive (7.13) from (7.12). Set $g:=f-f_{0}$. The function $F_{\ell}$ can be recovered as an integral of $g e^{-i \ell \cdot}$ along each circle. Hence for $\ell \neq 0$, we have $\sup \left|f_{\ell}\right| \leqslant \sup |g|$ and similarly $\sup \left|\Delta f_{\ell}\right| \leqslant \sup |\Delta g|$. Now we can just sum all the estimates (7.12) for $\ell \in \mathbb{Z}^{*}$ and get (7.13).

We now get to proving (7.12). We use the inequality
$$\frac{1}{2} \Delta_{\mathbb{R}_{-} \times D}\left|F_{\ell}\right|^{2} \geq\left\langle\Delta_{\mathbb{R}_{-} \times D} F_{\ell}, F_{\ell}\right\rangle=\left\langle\Delta F_{\ell}, F_{\ell}\right\rangle+\frac{\ell^{2}}{2 \varphi_{1}^{\prime \prime}(u) \beta^{2}}\left|F_{\ell}\right|^{2}$$
twice.
First, if $f_{\ell}$ vanishes at $\partial E_{u_{0}}(\varepsilon)$, then from the maximum principle and the fact that $\varphi_{1}^{\prime \prime}(u) \lessapprox \varphi_{1}^{\prime \prime}\left(u_{0}\right)$ on $E_{u_{0}}(\varepsilon)$ we have
$$\sup _{E_{u_{0}}(\varepsilon)}\left|F_{\ell}\right| \lessapprox \frac{\beta^{2} \varphi_{1}^{\prime \prime}\left(u_{0}\right)}{\ell^{2}} \sup _{E_{u_{0}}(\varepsilon)}\left|\Delta F_{\ell}\right|$$
and the result follows since $\frac{\beta}{\left|u_{0}\right|} \leq A$ and $\varphi_{1}^{\prime \prime}(u) \approx u^{-1+\frac{1}{n}}$ when $u \rightarrow 0$.
Therefore it is sufficient to consider the case where $\Delta f_{\ell}=0$. Indeed, let $h_{\ell}$ be the harmonic function on $E_{u_{0}}(\varepsilon)$ with same boundary values as $f_{\ell}$ and let $g_{\ell}:=f_{\ell}-h_{\ell}$. By what was said above, we have
$$\sup _{E_{u_{0}}(\varepsilon)}\left|g_{\ell}\right| \lessapprox \frac{\beta}{\ell^{2}} \sup _{E_{u_{0}}(\varepsilon)} w_{\beta}\left(u_{0}\right)^{\frac{1}{n}}\left|\Delta f_{\ell}\right|$$
hence
$$\sup _{E_{u_{0}}\left(\frac{1}{2} \varepsilon\right)}\left|f_{\ell}\right| \lessapprox \frac{\beta}{\ell^{2}} \sup _{E_{u_{0}}(\varepsilon)} w_{\beta}\left(u_{0}\right)^{\frac{1}{n}}\left|\Delta f_{\ell}\right|+\sup _{E_{u_{0}}\left(\frac{1}{2} \varepsilon\right)}\left|h_{\ell}\right| .$$
Recall that $\sup _{E_{u_{0}(\varepsilon)}}\left|h_{\ell}\right|=\sup _{E_{u_{0}}(\varepsilon)}\left|f_{\ell}\right|$. So, if we assume that $\sup _{E_{u_{0}\left(\frac{1}{2} \varepsilon\right)}}\left|h_{\ell}\right| \lessapprox$ $\frac{\beta}{\ell^{2}} w_{\beta}\left(u_{0}\right)^{-1} \sup _{E_{u_{0}}(\varepsilon)}\left|h_{\ell}\right|$, we are done.

Let us consider the comparison function $g(u)=a \cosh \left(b\left(u-u_{0}\right)\right)$. Then
$$\begin{aligned}
\frac{1}{2} \Delta g=\frac{\partial_{u}^{2} g}{\varphi_{1}^{\prime \prime}(u)}+(n-1) \frac{\partial_{u} g}{\varphi_{1}^{\prime}(u)} & \leq\left(\frac{b^{2}}{\varphi_{1}^{\prime \prime}(u)}-\frac{(n-1) b}{\varphi_{1}^{\prime}(u)}\right) g \\
& \leq \frac{\ell^{2}}{2 \beta^{2} \varphi_{1}^{\prime \prime}(u)} g
\end{aligned}$$
if we take $b=\gamma \frac{\ell}{\beta}$ for some small constant $\gamma>0$, thanks to the condition $u \leqslant-\frac{\beta}{A}$ for $A$ small enough. Combining with (7.14) we obtain
$$\Delta\left(\left|F_{\ell}\right|^{2}-g\right) \geq \frac{\ell^{2}}{\varphi_{1}^{\prime \prime}(u) \beta^{2}}\left(\left|F_{\ell}\right|^{2}-g\right) .$$

Choose $a$ large enough so that $\left|F_{\ell}\right|^{2} \leq g$ at $\partial E_{u_{0}}(\varepsilon)$, then it follows from (7.15) that $\left|F_{\ell}\right|^{2} \leq g$ on $E_{u_{0}}(\varepsilon)$, which in particular on $E_{u_{0}}\left(\frac{\varepsilon}{2}\right)$ we obtain
$$\sup _{E_{u_{0}}\left(\frac{\varepsilon}{2}\right)}\left|F_{\ell}\right|^{2} \lessapprox \frac{\cosh \left(\frac{1}{2} \varepsilon \gamma \frac{\ell}{\beta} u_{0}\right)}{\cosh \left(\varepsilon \gamma \frac{\ell}{\beta} u_{0}\right)} \sup _{E_{u_{0}}(\varepsilon)}\left|F_{\ell}\right|^{2} .$$
Since $x:=\frac{\left|u_{0}\right|}{\beta} \geq \frac{1}{A}$, we certainly have
$$\frac{\cosh \left(\frac{1}{2} \varepsilon \gamma \frac{\ell}{\beta} u_{0}\right)}{\cosh \left(\varepsilon \gamma \frac{\ell}{\beta} u_{0}\right)} \lessapprox \frac{1}{(x \ell)^{4}} \leq \frac{A^{2}}{\left(x \ell^{2}\right)^{2}}$$
which gives (7.12).
The case where $u_{0}=-\infty$ (that is centered on the divisor) is similar, so we only highlight the modifications to perform. To obtain the inequality
$$\sup _{E_{-\infty}(\varepsilon)}\left|F_{\ell}\right| \lessapprox \frac{\beta^{2}}{\ell^{2}} \sup _{E_{-\infty}(\varepsilon)}\left|\Delta F_{\ell}\right|$$
we can modify $E_{-\infty}(\varepsilon)$ and assume that its boundary is $\{u=2 \log \varepsilon\}$. Let us set $u_{\varepsilon}:=u-2 \log \varepsilon$ so that $\Delta u_{\varepsilon}=\frac{2(n-1)}{\varphi_{1}^{\prime}(u)}=O(1)$ and fix $\delta>0$. Then, we apply the maximum principle to $\left|F_{\ell}\right|^{2}+\delta u_{\varepsilon}$ to obtain, for any fixed $x$ :
$$\left|F_{\ell}(x)\right|^{2} \leqslant \frac{\beta^{2}}{\ell^{2}} \sup _{E_{-\infty}(\varepsilon)}\left|\Delta F_{\ell}\right| \cdot \sup _{E_{-\infty}(\varepsilon)}\left|F_{\ell}\right|-\delta u_{\varepsilon}(x)+O(\delta)$$
and we get (7.16) by taking $\delta \rightarrow 0$ and passing to the supremum over $x \in$ $E_{-\infty}(\varepsilon)$. The next step is very similar to the case $u_{0} \neq-\infty$ but one chooses instead $g(u)=a e^{\frac{\ell u}{\beta}}$, satisfying $\Delta g \leqslant \frac{2 \ell^{2}}{\beta^{2} \varphi_{1}^{\prime \prime}(u)} g$. Then we apply the maximum principle using the same barrier function as before, to obtain $\sup _{E_{-\infty}\left(\frac{\varepsilon}{2}\right)}\left|F_{\ell}\right| \leqslant$ $e^{-\frac{\ell}{\beta} \log 2} \sup _{E_{-\infty}(\varepsilon)}\left|F_{\ell}\right|$. The conclusion follows from the inequality $e^{-\frac{\ell}{\beta} \log 2} \lessapprox$ $\frac{\beta^{2}}{\ell^{2}}$. \(\square\)

Combining (7.13) with the local Schauder estimate (7.7) for $g=f-f_{0}$, we obtain
$$\left\|\nabla^{2} g\right\|_{C_{0}^{\alpha}\left(E_{u_{0}}\left(\frac{1}{2} \varepsilon\right)\right)} \lessapprox\left\|\Delta_{g_{\beta, L}} g\right\|_{C_{0}^{\alpha}\left(E_{u_{0}}(\varepsilon)\right)}+w_{\beta}\left(u_{0}\right)^{-1-\frac{1}{n}}\|g\|_{C^{0}\left(E_{u_{0}}(\varepsilon)\right),}$$
which is the estimate stated in Proposition 7.2.
Second step. We can now restrict the proof of Proposition 7.2 to the case when $f$ is circle invariant. In that case (7.11) reduces to
$$\begin{aligned}
\Delta_{g_{\beta, L}} f & =2 \frac{\partial_{u}^{2} f_{\ell}}{\varphi_{1}^{\prime \prime}(u)}+2(n-1) \frac{\partial_{u} f}{\varphi_{1}^{\prime}(u)}+\frac{1}{-\beta \varphi_{1}^{\prime}(u)} \Delta_{D} f \\
& =\frac{1}{-\beta \varphi_{1}^{\prime}(u)}\left(\partial_{v}^{2} f+\Delta_{D} f\right)
\end{aligned}$$
where $d v^{2}=\frac{\varphi_{1}^{\prime \prime}(u)}{-2 \beta \varphi_{1}^{\prime}(u)} d u^{2}$ and we choose $v\left(u_{0}\right)=0$. We now restrict to the case where for every $u$ one has
$$\int_{\{u\} \times D} f=0 .$$
We also suppose that we are not close to the divisor $D$, that is $r_{D}\left(u_{0}\right)>\varepsilon$. On each slice $\{u\} \times D$ the function $f$ is therefore orthogonal to the kernel of $\Delta_{D}$, which corresponds to erasing the critical weight 0 of the cylindrical Laplacien $\partial_{v}^{2}+\Delta_{D}$. It follows that this Laplacian is an isomorphism $C^{2, \alpha}(\mathbb{R} \times D) \rightarrow$ $C^{\alpha}(\mathbb{R} \times D)$, see for example [LM85, formula (2.3)]. In particular we have, still under condition (7.18),
$$\sup _{\mathbb{R} \times D}|f| \lessapprox \sup _{\mathbb{R} \times D}\left|\left(\partial_{\mathcal{V}}^{2}+\Delta_{D}\right) f\right| .$$
A quick elementary derivation of (7.19) is as follows: suppose $\left(\partial_{v}^{2}+\Delta_{D}\right) f=$ $g$, note $E(a)=\int_{[-a, a] \times D}|d f|^{2}$ and $F(a)=\int_{[-a, a] \times D}|g|^{2}$. The hypothesis on $f$ implies that for each $v$ we have $\int_{\{v\} \times D}\left|d_{D} f\right|^{2} \geq \lambda_{1}^{2} \int_{\{v\} \times D}|f|^{2}$, where $\lambda_{1}^{2}$ is the first nonzero eigenvalue of $\Delta_{D}$. By elliptic regularity and translation invariance, it is enough to prove that $E(1) \lessapprox \sup |g|^{2}$. By integration by parts we have
$$E(a)=-\int_{[-a, a] \times D} f g+\left(\int_{v=a}-\int_{v=-a}\right) f \partial_{v} f .$$
But $\left|\int_{v=a} f \partial_{v} f\right| \leq \frac{1}{2} \int_{v=a} \frac{1}{\lambda_{1}}\left|\partial_{v} f\right|^{2}+\lambda_{1}|f|^{2} \leq \frac{1}{2 \lambda_{1}} \int_{v=a}|d f|^{2}$. Since $E^{\prime}(a)=$ $\left(\int_{v=a}+\int_{v=-a}\right)|d f|^{2}$, it follows from (7.20) that $\lambda_{1} E(a)-E^{\prime}(a) \leq \frac{F(a)}{\lambda_{1}}$, and after integration $E(1) \leq \int_{1}^{+\infty} \frac{e^{-\lambda_{1}(a-1)}}{\lambda_{1}} F(a) d a \leq\left(\sup |g|^{2}\right) \frac{2}{\lambda_{1}} \int_{1}^{+\infty} a e^{-\lambda_{1}(a-1)} d a$.

The region $E_{u_{0}}(\varepsilon)$ gives only a bounded region in $\mathbb{R} \times D$, of diameter $2 d$ with respect to the variable $v$. Using a cut-off function for $\frac{d}{2} \leq|v| \leq d$, we deduce from (7.19) combined with the interpolation inequality $\left\|\partial_{v} f\right\|_{\infty}^{2} \lessapprox\left\|\partial_{v}^{2} f\right\|_{\infty}$. $\|f\|_{\infty}$ the following estimate
$$\sup _{\left[-\frac{d}{2}, \frac{d}{2}\right] \times D}|f| \lessapprox \sup _{[-d, d] \times D}\left[\left|\left(\partial_{v}^{2}+\Delta_{D}\right) f\right|+\frac{1}{d^{2}}|f|\right] .$$
Now we come back to the variable $u$ : we have $d^{2} \approx \frac{\varphi_{1}^{\prime \prime}\left(u_{0}\right)}{-\beta \varphi_{1}^{\prime}\left(u_{0}\right)} w_{\beta}\left(u_{0}\right)^{2}$, so we obtain (remember $-\varphi_{1}^{\prime}\left(u_{0}\right) \approx w_{\beta}\left(u_{0}\right)^{\frac{1}{n}}$ ):
$$\sup _{E_{u_{0}}\left(\frac{\varepsilon}{2}\right)}|f| \lessapprox \beta w_{\beta}\left(u_{0}\right)^{\frac{1}{n}} \sup _{E_{u_{0}}(\varepsilon)}\left|\Delta_{g_{\beta, L}} f\right|+\frac{1}{\varphi_{1}^{\prime \prime}\left(u_{0}\right) w_{\beta}\left(u_{0}\right)^{2}}|f| .$$
Combining with (7.7) we finally get
$$\left\|\nabla^{2} f\right\|_{C_{0}^{\alpha}\left(E_{u_{0}}\left(\frac{1}{2} \varepsilon\right)\right)} \lessapprox\left\|\Delta_{g_{\beta}} f\right\|_{C_{0}^{\alpha}\left(E_{u_{0}}(\varepsilon)\right)}+\frac{1}{\varphi_{1}^{\prime \prime}\left(u_{0}\right) w_{\beta}\left(u_{0}\right)^{2}}\|f\|_{C^{0}\left(E_{u_{0}}(\varepsilon)\right)} .$$
Since $\varphi_{1}^{\prime \prime}(u) \approx w_{\beta}(u)^{-1+\frac{1}{n}}$ if $r_{D}(u)>\varepsilon$, the estimate (7.10) follows in that case.

For the case where $u_{0}=-\infty$, that is $E_{u_{0}}(\varepsilon)$ is centered on the divisor $D$, we proceed similarly, except that the limit after rescaling is a half-cylinder instead of a cylinder. The same estimate (7.10) follows.

Third step. There remains only the case of a function $f(u)$ of the variable $u$ alone. But it is then almost obvious that the weight $w_{\beta}(u)^{1+\frac{1}{n}}$, which equals $|u|^{1+\frac{1}{n}}$ for $u$ small enough, is the correct weight for the operator $\Delta_{g_{\beta, L}}$.

\section*{8. Convergence in the positive case: proof of Theorem B}
8.1. Bound on the inverse of the linearisation. We first give a bound on the inverse of the linearisation $L_{\beta}=\frac{1}{2} \Delta_{g_{\beta}}+1$ of the operator $P_{\beta}$ defined in (5.13). We first prove:

Proposition 8.1. Fix $\delta \in(0,1)$. There exists a constant $c$ such that for any function $f$ on $X$ such that $\int_{X} f d \operatorname{vol}_{g_{\beta}}=0$ one has
$$\|f\|_{\mathcal{C}_{\delta}^{2, \alpha}} \leq c\left\|L_{\beta} f\right\|_{C_{\delta+1+\frac{1}{n}}^{\alpha}} .$$

We deduce:
Corollary 8.2. Fix $\delta \in(0,1)$. The operator $L_{\beta}: C_{\delta}^{2, \alpha} \rightarrow C_{\delta+1+\frac{1}{n}}^{\alpha}$ satisfies
$$\left\|L_{\beta}^{-1}\right\| \lessapprox \beta^{-\frac{1}{n}-\delta} .$$
Proof of Corollary 8.2. The constant function 1 satisfies $\|1\|_{C_{\delta}}=1$ as soon as $\delta \geq 0$. Since $L_{\beta}(1)=1$, the estimate (8.1) is also satisfied on constants.

Set $\delta^{\prime}:=\delta+1+\frac{1}{n}$. Given $f \in C_{\delta^{\prime}}^{\alpha}$ we decompose $f=\bar{f}+f_{1}$ with $\bar{f}$ constant and $\int_{X} f_{1} d \operatorname{vol}_{g_{\beta}}=0$. We have $L_{\beta}^{-1} f=L_{\beta}^{-1} f_{1}+\bar{f}$ so by (8.1), we have $\left\|L_{\beta}^{-1} f\right\|_{C_{\delta}^{\alpha}} \lessapprox\|f\|_{C_{\delta^{\prime}}^{\alpha}}+|\bar{f}|$ and we are reduced to showing that
$$|\bar{f}| \lessapprox \beta^{-\frac{1}{n}-\delta}\|f\|_{C_{\delta^{\prime}}^{0}} .$$
Now it follows from (5.9) that on $\left\{u \leqslant-\beta^{\mu} / 2\right\}$, we have $d \operatorname{vol}_{g_{\beta}} \approx \beta^{n} d \operatorname{vol}_{g_{X}}$ for some fixed Riemannian metric $g_{X}$ on $X$ while on $\left\{\tilde{u} \geqslant-\beta^{\mu} / 2\right\}$, we have $g_{\beta}=\beta^{1+\frac{1}{n}} g_{T Y}$ and, in particular, $\int_{\left\{\tilde{u} \geqslant-\beta^{\mu} / 2\right\}} d \operatorname{vol}_{g_{\beta}}=O\left(\beta^{n+1-\mu}\right)$. It follows that $\operatorname{Vol}\left(g_{\beta}\right) \approx \beta^{n}$.

Now, since $|f| \leq\|f\|_{C_{\delta^{\prime}}^{0}} w_{\beta}^{-\delta^{\prime}}$ we have,
$$\begin{aligned}
|\bar{f}| & \leq \frac{1}{\operatorname{Vol}\left(g_{\beta}\right)} \int_{x}|f| d \operatorname{vol}_{g_{\beta}} \\
& \lessapprox \frac{\|f\|_{C_{\delta^{\prime}}^{0}}}{\beta^{n}} \int_{X} w_{\beta}^{-\delta^{\prime}} d \operatorname{vol}_{g_{\beta}} .
\end{aligned}$$
One checks that since $\delta^{\prime}>1$, the main contribution of the last integral is on the Tian-Yau part $X \backslash U_{L}$, and is of order $\beta^{n+1-\delta^{\prime}}$. We therefore get $|\bar{f}| \lessapprox$ $\beta^{1-\delta^{\prime}}\|f\|_{C_{\delta^{\prime}}^{0}}$ and (8.3) is proved. This ends the proof of the corollary. \(\square\)

The rest of this section is devoted to the proof of Proposition 8.1.
Suppose (8.1) is not true. By Corollary 7.3 and Remark 7.4 there exist functions $f_{\beta}$ such that $\int_{X} f_{\beta} d \mathrm{vol}_{g_{\beta}}=0$ and
$$\left\|f_{\beta}\right\|_{C_{\delta}^{0}}=1, \quad\left\|L_{\beta} f_{\beta}\right\|_{C_{\delta+1+\frac{1}{n}}^{\alpha}} \rightarrow 0,$$
while $\left\|f_{\beta}\right\|_{C_{\delta}^{2, \alpha}}$ is bounded. Fix $x_{\beta} \in X$ such that $w_{\beta}\left(x_{\beta}\right)^{\delta}\left|f_{\beta}\left(x_{\beta}\right)\right|=1$. We then analyze the various cases depending on the limit of $x_{\beta}$.

First case. The $x_{\beta}$ 's converge to $D$ and $u\left(x_{\beta}\right)<\eta<0$.
For now, we restrict the functions $f_{\beta}$ on $U_{L}$ and see them as functions on a fixed neighborhood $U=\left\{\|v\|_{h}^{2}<e^{-1}\right\}$ of the zero section in $L$. In this proof only, we emphasize the dependence of $u$ in $\beta$ and denote it $u_{\beta}$. We use the diffeomorphism $\Phi_{\beta}: L \backslash D \rightarrow L \backslash D, v \mapsto\|v\|^{\frac{1}{\beta}-1} \cdot v$, so that $\Phi_{\beta}^{*} u_{\beta}=u: v \mapsto$ $\log \|v\|_{h}^{2}$ and $U_{\beta}:=\Phi_{\beta}^{-1}(U)=\left\{\|v\|_{h}^{2}<e^{-\beta}\right\}$ is essentially independent of $\beta$. Of course, $\Phi_{\beta}^{*} g_{\beta}$ is still given by (2.15), but there is no more hidden dependence on $\beta$ in that expression. Set $F_{\beta}=\Phi_{\beta}^{*} f_{\beta}$. Since $\left\|f_{\beta}\right\|_{\mathcal{C}_{\delta}^{2, \alpha}}$ remains bounded, we can extract a limit $F_{\beta} \rightarrow f$. It turns out that $f$ depends on $u$ only because the norm $\left\|d f_{\beta}\right\|_{C_{\delta+1}^{0}}$ involves a factor $\beta^{-1}$ in the circle direction or $\beta^{-1 / 2}$ in the divisor $D$ direction. It is possible that $y_{\beta}:=\Phi_{\beta}^{-1}\left(x_{\beta}\right)$ satisfies $u\left(y_{\beta}\right) \rightarrow-\infty$ but the $C^{1}$ bound on $F_{\beta}$ ensures that one can find another point $z_{\beta}$ with $\eta \geqslant u\left(z_{\beta}\right) \geqslant-C$ and $\left|F_{\beta}\left(z_{\beta}\right)\right| \geqslant \frac{1}{2}$ for some $C>0$.

Therefore we have a non-zero limit $f(u)$ for $u \in(-\infty, 0)$ which satisfies
$$\begin{gathered}
\sup |w|^{\delta}|f|=1, \\
\frac{f^{\prime \prime}(u)}{\varphi_{1}^{\prime \prime}(u)}+(n-1) \frac{f^{\prime}(u)}{\varphi_{1}^{\prime}(u)}+f(u)=0,
\end{gathered}$$
where $w(u)=1$ if $u \leqslant-2$ and $w(u)=u$ if $u \geqslant-1 / 2$. Note that the limit Laplacian
$$\Delta_{v_{\infty}}:=\frac{1}{2}\left(\frac{1}{\varphi_{1}^{\prime \prime}(u)} \partial_{u}^{2}+\frac{n-1}{\varphi_{1}^{\prime}(u)} \partial_{u}\right)$$
is the Bakry-Emery Laplacian of $\left(g_{\infty}, v_{\infty}\right)$, a general fact in measured Gromov-Hausdorff convergence.

Moreover
$$\frac{1}{\beta^{n}}\left|\int_{\tilde{u} \geq-\beta} f_{\beta} d \operatorname{vol}_{g_{\beta}}\right| \leq \beta^{1-\delta}\left\|f_{\beta}\right\|_{C_{\delta}^{0}}$$
so if $\delta<1$ we have that
$$\frac{1}{\beta^{n}} \int_{X} f_{\beta} d \operatorname{vol}_{g_{\beta}} \rightarrow c \int_{-\infty}^{0} f(u) \varphi_{1}^{\prime \prime}(u) \varphi_{1}^{\prime}(u)^{n-1} d u$$
for some constant $c$, so the limit $f(u)$ satisfies
$$\int_{-\infty}^{0} f(u) \varphi_{1}^{\prime \prime}(u) \varphi_{1}^{\prime}(u)^{n-1} d u=0$$

The function $\varphi_{1}^{\prime}(u)$ is an obvious solution of (8.5), it corresponds to the dilation vector field in the bundle $L$. It satisfies $\varphi_{1}^{\prime}(u) \rightarrow-1$ when $u \rightarrow-\infty$, while the other solution is $f=g \varphi_{1}^{\prime}$ with $g=\int \frac{d u}{\left(1-e^{-\varphi_{1}}\right)}$. By (2.10), $f(u) \approx u$ near $-\infty$ (it corresponds to the Green function near $D$ ). But this is ruled out by (8.4). Therefore we see that up to a constant we must have $f(u)=\varphi_{1}^{\prime}(u)$, which gives a contradiction with (8.7).

Second case. The $x_{\beta}$ 's still converge to $D$ but we can extract a limit only in the intermediate region between the normal bundle $L$ and the Tian-Yau metric on $X \backslash D$ : this is the case where $u\left(x_{\beta}\right) \rightarrow 0$ but $\frac{1}{\beta} u\left(x_{\beta}\right) \rightarrow-\infty$. It is similar to the previous one; set $\varepsilon_{\beta}:=-u\left(x_{\beta}\right), v:=\frac{u}{\varepsilon_{\beta}}$ and consider the rescaled functions $h_{\beta}:=\varepsilon_{\beta}^{\delta} f_{\beta}$. It satisfies $h_{\beta} \leqslant|v|^{-\delta}$ while on the compact sets of $v \in\left(-\infty, \frac{\beta}{\varepsilon_{\beta}}\right]$, the metric $g_{\beta}$ is asymptotically close to
$$\varepsilon_{\beta}^{1+\frac{1}{n}}\left(\frac{1}{n}|v|^{-1+\frac{1}{n}}\left(\frac{1}{2} d v^{2}+2\left(\frac{\beta}{\varepsilon_{\beta}}\right)^{2} \eta^{2}\right)+\frac{\beta}{\varepsilon_{\beta}} \cdot|v|^{\frac{1}{n}} g_{D}\right)$$
by (2.16), with $\frac{\beta}{\varepsilon_{\beta}} \rightarrow 0$.
Geometrically this amounts to saying that we have the following convergence in the measured Gromov-Hausdorff sense: for some constant $C>0$,
$$\left(X, \varepsilon_{\beta}^{-1-\frac{1}{n}} g_{\beta}, x_{\beta}, \frac{d \operatorname{vol}_{g_{\beta}}}{\operatorname{vol}_{g_{\beta}}\left(B\left(x_{\beta}, 1\right)\right)}\right) \longrightarrow\left((-\infty, 0), \frac{1}{2 n}|v|^{-1+\frac{1}{n}} d v^{2},-1, C d v\right) .$$

Our Hölder estimates imply similarly to the previous case that $h_{\beta}$ has a non-zero limit $h$ which is a function of $v$ only. Since $L_{\beta}=\frac{1}{2}\left(\Delta_{g_{\beta}}+1\right)=$ $\varepsilon_{\beta}^{-1-\frac{1}{n}}\left(\frac{1}{2} \Delta_{\varepsilon_{\beta}^{-1-\frac{1}{n}} g_{\beta}}+\varepsilon_{\beta}^{1+\frac{1}{n}}\right)$, the constant term in $L_{\beta}$ disappears in the limit, so the limit function $h$ is harmonic with respect to the limit Bakry-Emery Laplacian, which is now given by equation (8.6) with $\varphi^{\prime}(u)=(-u)^{\frac{1}{n}}$. Finally this gives the equation
$$n(-v)^{1-\frac{1}{n}} \partial_{v}^{2} h-(n-1)(-v)^{-\frac{1}{n}} \partial_{v} h=0 .$$
Hence $h$ is a linear combination of the harmonic functions 1 and $|v|^{\frac{1}{n}}$, but it also satisfies $h \leqslant|v|^{-\delta}$. We derive a contradiction when $v \rightarrow-\infty$.

Third case. The $x_{\beta}$ 's converge in the Tian-Yau part: $u\left(x_{\beta}\right)=O(\beta)$. This is similar: after rescaling, we get a nonzero limit $f$ which is a nonzero harmonic function on the Tian-Yau space $X \backslash D$ with $|f| \leq|\tilde{t}|^{-\delta}$. This implies $f=0$, which is a contradiction.
8.2. Resolution of the Kähler-Einstein equation. We first control the quadratic terms of the equation:

Lemma 8.3. For $\delta \geq 0$ and any function $\varphi$ we have
$$\left\|(\partial \bar{\partial} \varphi)^{2}\right\|_{C_{\delta}^{\alpha}} \lessapprox \beta^{-\delta}\|\partial \bar{\partial} \varphi\|_{C_{\delta}^{\alpha}}^{2}$$

Proof. From Remark 7.1 we see that for $\delta=0$ we have the estimate. The weight $w_{\beta}^{\delta}$ introduces a coefficient $w_{\beta}^{-\delta}$ in the estimates, which is maximal when the weight $w_{\beta}$ is minimal, that is on the Tian-Yau part where the value of $w_{\beta}$ is $\beta$. The lemma follows. \(\square\)

End of the proof of Theorem B. Decompose $P_{\beta}$ into an affine part and a higher order term part:
$$P_{\beta}(\varphi)=P_{\beta}(0)+L_{\beta}(\varphi)+Q_{\beta}(\varphi) .$$
It follows from the lemma that if $\|\partial \bar{\partial} \varphi\|_{C_{\delta+1+\frac{1}{n}}^{\alpha}}<\varepsilon \beta^{1+\frac{1}{n}+\delta}$ for a small enough $\varepsilon>0$, then
$$\left\|Q_{\beta}(\varphi)-Q_{\beta}(\psi)\right\|_{C_{\delta+1+\frac{1}{n}}^{\alpha}} \lessapprox \beta^{-1-\frac{1}{n}-\delta}\|\varphi-\psi\|_{C_{\delta}^{2, \alpha}}\left(\|\varphi\|_{C_{\delta}^{2, \alpha}}+\|\psi\|_{C_{\delta}^{2, \alpha}}\right) .$$

On the other hand from (5.14) we have $\left|P_{\beta}(0)\right| \lessapprox \tilde{u}^{1+\frac{1}{n}}$ for $u \geq-2 \beta^{\mu}$, and $\left|P_{\beta}(0)\right| \lessapprox e^{\left(\frac{1}{2}-\varepsilon\right) \frac{u}{\beta}}$ for $u \leq-2 \beta^{\mu}$. These bounds give the worst control of $\sup \left|w_{\beta}^{\delta+1+\frac{1}{n}} P_{\beta}(0)\right|$ around $u=-\beta^{\mu}$ and it follows that $\left\|P_{\beta}(0)\right\|_{C_{\delta+1+\frac{1}{n}}^{0}} \lessapprox$ $\beta^{\mu\left(2\left(1+\frac{1}{n}\right)+\delta\right)}$. Adding the seminorm $[\cdot]_{\alpha}$ does not change the bound and we get
$$\left\|P_{\beta}(0)\right\|_{C_{\delta+1+\frac{1}{n}}^{\alpha}} \lessapprox \beta^{\mu\left(2\left(1+\frac{1}{n}\right)+\delta\right)}$$

Fix $\delta$ small enough (the precise bound will be fixed below). Given the bound (8.2), together with (8.9) and (8.10), standard fixed point arguments (see for example [BM11, Lemma 1.3]) now imply that if
$$\beta^{\mu\left(2\left(1+\frac{1}{n}\right)+\delta\right)} \ll \beta^{1+\frac{3}{n}+3 \delta}$$
then the equation $P_{\beta}(\varphi)=0$ has a unique solution $\varphi(\beta)$ in a ball of radius $\varepsilon \beta^{1+\frac{2}{n}+2 \delta}$ in $C_{\delta}^{2, \alpha}$, and this solution actually satisfies
$$\|\varphi(\beta)\|_{C_{\delta}^{2, \alpha}} \lessapprox \beta^{\mu\left(2\left(1+\frac{1}{n}\right)+\delta\right)-\frac{1}{n}-\delta} .$$
Observe that for $\mu=1$ the inequality (8.11) is satisfied if $2 \delta<1-\frac{1}{n}$. Now fix $\delta<\frac{1}{2}\left(1-\frac{1}{n}\right)$. We use the flexibility of fixing $\mu \in(0,1)$ as close to 1 as we want, which geometrically corresponds to gluing more near the Tian-Yau part (then the error is smaller since the Calabi ansatz gives an exact solution up to exponentially small terms). So we fix $\mu<1$ so that (8.11) is satisfied, and these values of $\delta$ and $\mu$ enable us to solve the problem. Moreover for any $\epsilon>0$ we can find values of $(\mu, \delta)$ close to $(1,0)$ so that (8.12) gives the following bound on the solution $\varphi(\beta)$ :
$$\|\varphi(\beta)\|_{C_{\delta}^{2, \alpha}} \lessapprox \beta^{2+\frac{1}{n}-\epsilon} .$$

By [Ber15, Theorem 7.3], the Kähler-Einstein metric $\widehat{\omega}_{\beta}:=\omega_{\beta}+i \partial \bar{\partial} \varphi(\beta)$ is the unique Kähler-Einstein metric with cone angle $2 \pi \beta$ along $D$, i.e. satisfying Ric $\widehat{\omega}_{\beta}=\widehat{\omega}_{\beta}+(1-\beta)[D]$. Given any compact set $M \Subset X \backslash D$, we have for $\beta \ll 1$ :
$$\left.w_{\beta}\right|_{M} \equiv \beta,\left.\quad \omega_{\beta}\right|_{M}=\beta^{1+\frac{1}{n}} \omega_{T Y}, \quad\left\|\beta^{-1-\frac{1}{n}} \partial \bar{\partial} \varphi(\beta)\right\|_{\omega_{T Y}} \lessapprox \beta^{1-\epsilon-\delta}$$
where the last estimate follows by (8.13). In particular, $\left\|\beta^{-1-\frac{1}{n}} \widehat{\omega}_{\beta}-\omega_{T Y}\right\|_{\omega_{T Y}}=$ $O\left(\beta^{1-\epsilon-\delta}\right)$ on $M$, and we are done with the first part of Theorem B, since higher estimates are obtained as usual by bootstrapping.

At this point of the proof, we are essentially done but for exposition purposes, we collect the remaining statements in Theorem B and the remarks following it in:

Lemma 8.4. Given $p \in X$ and a non-decreasing family $\left(\varepsilon_{\beta}\right)$ of positive numbers, the pointed Gromov-Hausdorff limits of the rescaled Kähler-Einstein metric $\left(X, \varepsilon_{\beta}^{-1} \hat{g}_{\beta}, p\right)$ coincide with that of the model space $\left(X, \varepsilon_{\beta}^{-1} g_{\beta}, p\right)$ given in section 5.3.

Proof of Lemma 8.4. The estimate (8.13) shows that $\|\partial \bar{\partial} \varphi(\beta)\|_{g_{\beta}} \lessapprox \beta^{1-\delta-\varepsilon}$, so that, in particular, $\left|\hat{g}_{\beta}-g_{\beta}\right|_{g_{\beta}} \lessapprox \sqrt{\beta}$, or equivalently
$$\left|\varepsilon_{\beta}^{-1} \hat{g}_{\beta}-\varepsilon_{\beta}^{-1} g_{\beta}\right|_{\varepsilon_{\beta}^{-1} g_{\beta}} \lessapprox \sqrt{\beta},$$
and the lemma follows immediately from the definition of pointed GromovHausdorff convergence. \(\square\)

The proof of Theorem B is now complete. \(\square\)

\section*{References}
\begin{itemize}
\item[] [AMRT10] Avner Ash, David Mumford, Michael Rapoport, and Yung-Sheng Tai. Smooth compactifications of locally symmetric varieties. Cambridge Mathematical Library. Cambridge University Press, Cambridge, second edition, 2010. With the collaboration of Peter Scholze.
\item[] [And06] Michael T. Anderson. Dehn filling and Einstein metrics in higher dimensions. J. Differ. Geom., 73(2):219-261, 2006.
\item[] [BD91] J. Bland and T. Duchamp. Moduli for pointed convex domains. Invent. Math., 104(1):61-112, 1991.
\item[] [Ber13] Robert J. Berman. A thermodynamical formalism for Monge-Ampère equations, Moser-Trudinger inequalities and Kähler-Einstein metrics. Adv. Math., 248:1254-1297, 2013.
\item[] [Ber15] Bo Berndtsson. A Brunn-Minkowski type inequality for Fano manifolds and some uniqueness theorems in Kähler geometry. Invent. Math., 200(1):149-200, 2015.
\item[] [BG14] Robert J. Berman and Henri Guenancia. Kähler-Einstein metrics on stable varieties and log canonical pairs. Geometric and Function Analysis, 24(6):1683-1730, 2014.
\item[] [Biq02] Olivier Biquard. Métriques autoduales sur la boule. Invent. math., 148(3):545-607, 2002.
\item[] [BM11] Olivier Biquard and Vincent Minerbe. A Kummer construction for gravitational instantons. Commun. Math. Phys., 308(3):773-794, 2011.
\item[] [Bre13] S. Brendle. Ricci flat Kähler metrics with edge singularities . International Mathematics Research Notices, 24:5727-5766, 2013.
\item[] [Cal79] E. Calabi. Métriques kählériennes et fibrés holomorphes. Ann. Sci. École Norm. Sup. (4), 12(2):269-294, 1979.
\item[] [CGP13] Frédéric Campana, Henri Guenancia, and Mihai Păun. Metrics with cone singularities along normal crossing divisors and holomorphic tensor fields. Ann. Sci. Éc. Norm. Supér. (4), 46(6):879-916, 2013.
\item[] [CKZ11] U. Cegrell, S. Kołodziej, and A. Zeriahi. Maximal subextensions of plurisubharmonic functions. Ann. Fac. Sci. Toulouse Math. (6), 20(Fascicule Spécial):101-122, 2011.
\end{itemize}
[CR15] Ivan A. Cheltsov and Yanir A. Rubinstein. Asymptotically log Fano varieties. Adv. Math., 285:1241-1300, 2015.
[CY75] S. Y. Cheng and S. T. Yau. Differential equations on Riemannian manifolds and their geometric applications. Comm. Pure Appl. Math., 28(3):333-354, 1975.
[DE21] Martin De Borbon and Gregory Edwards. Schauder estimates on products of cones. Comment. Math. Helv., 96(1):113-148, 2021.
[DGG20] Eleonora DiNezza, Vincent Guedj, and Henri Guenancia. Families of singular Kähler-Einstein metrics. Preprint arXiv:2003.08178, to appear in J. Eur. Math. Soc., 2020.
[Don12] Simon Donaldson. Kähler metrics with cone singularities along a divisor. In Essays in mathematics and its applications, pages 49-79. Springer, Heidelberg, 2012.
[DP04] Jean-Pierre Demailly and Mihai Păun. Numerical characterization of the Kähler cone of a compact Kähler manifold. Ann. of Math. (2), 159(3):1247-1274, 2004.
[GP16] Henri Guenancia and Mihai Păun. Conic singularities metrics with prescribed Ricci curvature: the case of general cone angles along normal crossing divisors. J. Differential Geom., 103(1):15-57, 2016.
[GS18] Bin Guo and Jian Song. Schauder estimates for equations with cone metrics, II. Preprint arXiv:1809.03116, 2018.
[GS21] Bin Guo and Jian Song. Schauder estimates for equations with cone metrics. I. Indiana Univ. Math. J., 70(5):1639-1676, 2021.
[Gue20] Henri Guenancia. Kähler-Einstein metrics: From cones to cusps. J. Reine Angew. Math., 759:1-27, 2020.
[GY21] Yaoting Gui and Hao Yin. Schauder estimates on smooth and singular spaces. Ann. Global Anal. Geom., 59(4):457-481, 2021.
[Hei12] Hans-Joachim Hein. Gravitational instantons from rational elliptic surfaces. J. Am. Math. Soc., 25(2):355-393, 2012.
[HSVZ22] Hans-Joachim Hein, Song Sun, Jeff Viaclovsky, and Ruobing Zhang. Nilpotent structures and collapsing Ricci-flat metrics on the K3 surface. J. Am. Math. Soc., 35(1):123-209, 2022.
[JMR16] Thalia Jeffres, Rafe Mazzeo, and Yanir A. Rubinstein. Kähler-Einstein metrics with edge singularities. Ann. of Math. (2), 183(1):95-176, 2016. with an Appendix by C. Li and Y. Rubinstein.
[Kob84] R. Kobayashi. Kähler-Einstein metric on an open algebraic manifolds. Osaka 1. Math., 21:399-418, 1984.
[Koł98] Sławomir Kołodziej. The complex Monge-Ampère operator. Acta Math., 180(1):69-117, 1998.
[Lem92] László Lempert. On three-dimensional Cauchy-Riemann manifolds. J. Amer. Math. Soc., 5(4):923-969, 1992.
[LM85] Robert B. Lockhart and Robert C. McOwen. Elliptic differential operators on noncompact manifolds. Ann. Scuola Norm. Sup. Pisa Cl. Sci. (4), 12(3):409-447, 1985.
[Mok12] Ngaiming Mok. Projective algebraicity of minimal compactifications of complexhyperbolic space forms of finite volume. In Perspectives in analysis, geometry, and topology, volume 296 of Progr. Math., pages 331-354. Birkhäuser/Springer, New York, 2012.
[Mum77] D. Mumford. Hirzebruch's proportionality theorem in the non-compact case. Invent. Math., 42:239-272, 1977.
[Oda20] Yuji Odaka. Polystable log Calabi-Yau varieties and gravitational instantons. Preprint arXiv:2009.13876, 2020.
[Rub14] Yanir A. Rubinstein. Smooth and singular Kähler-Einstein metrics. In Geometric and spectral analysis, volume 630 of Contemp. Math., pages 45-138. Amer. Math. Soc., Providence, RI, 2014.
[RZ20] Yanir A. Rubinstein and Kewei Zhang. Small angle limits of Hamilton's footballs. Bull. Lond. Math. Soc., 52(1):189-199, 2020.
[SW16] Jian Song and Xiaowei Wang. The greatest Ricci lower bound, conical Einstein metrics and Chern number inequality. Geom. Topol., 20(1):49-102, 2016.
[SZ19] Song Sun and Ruobing Zhang. Complex structure degenerations and collapsing of Calabi-Yau metrics. Preprint arXiv:1906.03368, 2019.
[TY87] Gang Tian and Shing-Tung Yau. Existence of Kähler-Einstein metrics on complete Kähler manifolds and their applications to algebraic geometry. Adv. Ser. Math. Phys. 1, 1:574-628, 1987. Mathematical aspects of string theory (San Diego, Calif., 1986).
[TY90] Gang Tian and Shing-Tung Yau. Complete Kähler manifolds with zero Ricci curvature. I. J. Amer. Math. Soc., 3(3):579-609, 1990.
[Wan06] Xu-Jia Wang. Schauder estimates for elliptic and parabolic equations. Chinese Ann. Math. Ser. B, 27(6):637-642, 2006.

Sorbonne Université and Université de Paris, CNRS, IMJ-PRG, F-75005 Paris, France
Email address: olivier.biquard@sorbonne-universite.fr
Institut de Mathématiques de Toulouse; UMR 5219, Université de Toulouse; CNRS, UPS, 118 route de Narbonne, F-31062 Toulouse Cedex 9, France
Email address: henri.guenancia@math.cnrs.fr

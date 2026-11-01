---
retention_scope: session
part: 1
total_parts: 2
---

[Part 1/2 of: Eguchi--Hanson metrics arising from Kahler--Einstein edge metrics]

---
source_file: 2111_00652.pdf
converter: mathpix
format: mmd
---

\title{
Eguchi-Hanson metrics arising from Kähler-Einstein edge metrics
}

\author{
Yuxiang Ji, Yanir A. Rubinstein, Kewei Zhang
}

14 December 2023

Dedicated to Scott Wolpert on the occassion of his retirement

\begin{abstract}
Calabi-Hirzebruch manifolds are higher-dimensional generalizations of both the football and Hirzebruch surfaces. We construct a family of Kähler-Einstein edge metrics singular along two disjoint divisors on the Calabi-Hirzebruch manifolds and study their Gromov-Hausdorff limits when either cone angle tends to its extreme value. As a very special case, we show that the celebrated Eguchi-Hanson metric arises in this way naturally as a Gromov-Hausdorff limit. We also completely describe all other (possibly rescaled) Gromov-Hausdorff limits which exhibit a wide range of behaviors, resolving in this setting a conjecture of Cheltsov-Rubinstein. This gives a new interpretation of both the Eguchi-Hanson space and Calabi's Ricci flat spaces as limits of compact singular Einstein spaces.
\end{abstract}

\section*{Contents}
1 Motivation ..... 2
2 Results ..... 2
2.1 Large angle limits ..... 4
2.2 Small angle limits ..... 5
2.3 Organization ..... 6
3 Model metrics ..... 6
3.1 Non-compact case: model metrics on $-k H_{\mathbb{P}^{n-1}}$ ..... 7
3.2 Compact case: model metrics on $\mathbb{P}^{n}(1, \ldots, 1, k)$ ..... 8
4 Constructions of Kähler-Einstein edge metrics ..... 10
4.1 Constructions of $\eta_{\beta_{1}}$ on $\mathbb{F}_{n, k}$ ..... 10
4.2 Constructions of $\xi_{\beta_{2}}$ on $\mathbb{F}_{n, k}$ ..... 13
5 Angle asymptotics ..... 14
6 Large angle limits ..... 18
7 Small angle limits and fiberwise rescaling ..... 21
A A brief review on Eguchi-Hanson metrics ..... 25
B Eguchi-Hanson metrics as Gromov-Hausdorff limits of Kähler-Einstein edge metrics ..... 28
C Examples of limit of Kähler-Einstein edge metrics ..... 32
C. 1 Calculations in terms of $\beta_{2}$ ..... 33

\section*{1 Motivation}

The main motivation for this work is a program of Cheltsov-Rubinstein concerning the small angle deformation of Kähler-Einstein edge (KEE) metrics, which in particular makes the following prediction [6, Conjecture 1.11]:

Conjecture 1.1. Suppose that $(X, D)$ is strongly asymptotically log Fano manifold with $D$ smooth and irreducible. Suppose that $\kappa:=\inf \left\{\mathbb{N} \ni k \leq \operatorname{dim} X:\left(K_{X}+D\right)^{k}=0\right\} \leq \operatorname{dim} X$, and that there exist KEE metrics $\omega_{\beta}, \beta \in(0, \epsilon)$ on $(X, D)$ for some $\epsilon>0$. Then, $\left(X, D, \omega_{\beta}\right)$ converges in an appropriate sense as $\beta$ tends to zero to a generalized $K E$ metric $\omega_{\infty}$ that is Calabi-Yau along its generic ( $\operatorname{dim} X+1-\kappa$ )-dimensional fibers.

In this article we actually treat a slightly more general situation where $D$ is allowed to have two disjoint smooth components $D=D_{1}+D_{2}$, but the setting is essentially identical to that of Conjecture 1.1 since the angle $2 \pi \beta_{1}$ along $D_{1}$ of the KEE metric $\omega_{\beta_{1}, \beta_{2}}$ actually determines the angle $2 \pi \beta_{2}$ along $D_{2}$ and, importantly, vice versa.

A second motivation for this article is given by a prediction posed by two of the present authors in a previous work concerning the large angle limit of a family of Kähler-Einstein edge metrics constructed on the second Hirzebruch surface $\mathbb{F}_{2}$. On that surface let $D_{1}:=Z_{-2}$ denote the -2-curve and $D_{2}:=Z_{2}$ the smooth infinity section, a 2-curve satisfying $Z_{-2} \cap Z_{2}=\emptyset$. According to [14, Theorem 1.2] there exist for each $\beta_{1} \in(0,1)$ a unique Kähler-Einstein edge metric $\omega_{\beta_{1}, \beta_{2}}$ with angle $2 \pi \beta_{1}$ along $Z_{-2}$ and angle $2 \pi \beta_{2}=2 \pi\left(2 \beta_{1}-3+\sqrt{9+12 \beta_{1}-12 \beta_{1}^{2}}\right) / 4$ along $Z_{2}$ and cohomologous to $\frac{1+\beta_{2}}{1-\beta_{1}}\left[Z_{2}\right]-\left[Z_{-2}\right]$. The following prediction was made [14, Remark 5.1]:

Conjecture 1.2. As $\beta_{1}$ tends to 1 , an appropriate limit of $\left(\mathbb{F}_{2}, \omega_{\beta_{1}, \beta_{2}}\right)$ converges to the Eguchi-Hanson metric.

The virtue of Conjecture 1.2 is that it proposes a remarkable new interpretation of the Eguchi-Hanson space from mathematical physics as an angle deformation limit of compact singular Einstein spaces with edge singularities.

The goal of the present article is to treat both conjectures and a bit more. We solve Conjecture 1.1 in the setting of Calabi-Hirzebruch manifolds as well as solve Conjecture 1.2. In fact we solve a generalized version of Conjecture 1.2 that interprets Calabi's Ricci flat spaces as limits of compact KEE spaces. Moreover, due to the existence of two disjoint divisors there are also interesting limits to study that are not part of the above conjectures: these limits are studied in Theorems 2.4 and 2.8 below.

\section*{2 Results}

Let $M$ be a compact Kähler manifold and $D=D_{1}+\cdots D_{r}$ a simple normal crossing divisor in $M$. A Kähler metric $\omega$ is said to have edge singularity along $D$ if $\omega$ is smooth on $M \backslash D$ and asymptotically equivalent to the model edge metric along $D$ [12, Definition 3.1]. The study of

Kähler-Einstein edge metrics dates back to Tian [15] where he considered applications of such metrics to algebraic geometry. Cheltsov-Rubinstein [6] initiated the program of studying small angle limits of Kähler-Einstein edge metrics. In previous works, two of us treated the Riemann surface footballs case and Hirzebruch surfaces case by first constructing Kähler-Einstein edge metrics on the manifolds using Calabi ansatz and then studying their limiting behaviors when the cone angles tend to 0 [14, 13]. In this paper, we consider a more general setting, Calabi-Hirzebruch manifolds. To construct these KEE metrics we use the standard Calabi ansatz in Section 4, generalizing [14]. The angle at either divisor $D_{1}:=Z_{n, k}$ or $D_{2}:=Z_{n,-k}$ then determines the angle on the other divisor which leads to two families of KEE metrics $\eta_{\beta_{1}}$ and $\xi_{\beta_{2}}$ on $\mathbb{F}_{n, k}$.
Remark 2.1. Very recently, Biquard-Guenancia completely solved the folklore case $\kappa=1$ of Conjecture 1.1 [3] (that case of the conjecture seems to have been already conjectured by Tian and Mazzeo in the 90's and then explicitly stated around 2009 by Donaldson [11, 10, 7]), and interestingly the Calabi ansatz makes an appearance in their proof as well. It would be interesting to explore whether some of the rather elementary ideas here can be combined with some of their deep estimates to attack the general case of Conjecture 1.1.
Remark 2.2. It is interesting to note that Abreu [1, §5] and subsequently Atiyah-LeBrun [2, (5.5)-(5.6)] also studied a family of Einstein metrics with orbifold/cone-edge singularities converging (roughly) to the Eguchi-Hanson metric. There are, however, important differences between their construction and ours: (i) their metrics are not Kähler, (ii) they work on the space $\mathbb{P}^{2}$ while we work on the second Hirzebruch surface $\mathbb{F}_{2}$ (which generalizes to $\mathbb{F}_{n, k}$ in higher-dimensions), (iii) the metrics they construct in the sequence are singular along a single $\mathbb{P}^{1}$ divisor instead of two $\mathbb{P}^{1}$ divisors, as in our construction, (iv) their limit metric is not precisely the Eguchi-Hanson metric, but rather its double cover (they obtain an angle of $4 \pi$ along a $\mathbb{P}^{1}$ divisor). While our metrics are constructed directly from the Calabi ansatz as Kähler-Einstein edge metrics, Abreu constructs extremal (non-Einstein) Kähler metrics using toric formalism and then uses Derdzinki's theorem to conclude that a conformal rescaling (dividing by the scalar curvature squared) will be Einstein (but not Kähler). LeBrun obtains the same family of metrics using a completely different method specific to dimension 4. One could take the double cover of our construction. That would have the effect of, roughly speaking, the curve being pushed out to infinity becoming smooth in the limit as the angle there would tend to $2 \pi$ (instead of $\pi$ ), while the other angle tends to $4 \pi$. But even then it is not clear how to relate our metrics that are Kähler-Einstein edge (and in particular Kähler) to the Abreu-Atiyah-LeBrun metrics, that are not Kähler.

Motivated by the previous remark, we pose:
Problem 2.3. Relate the Abreu-Atiyah-LeBrun metrics to ours.
A common feature for footballs, Hirzebruch surfaces, and Calabi-Hirzebruch manifolds is that there are two smooth disjoint divisors and hence two angle parameters $\beta_{1}, \beta_{2}$. In Section 3, we review the construction of Calabi-Hirzebruch manifolds [5, 9], denoted by $\mathbb{F}_{n, k}$ for $\mathbb{N} \ni n \geq 2$ and $k \in \mathbb{N}$, and define two (families of) model metrics. The first are Ricci-flat edge metrics on the total space of the (non-compact) line bundle $-k H_{\mathbb{P}^{n-1}}$,
$$\omega_{\mathrm{eh}, n, k},$$
and an edge singularity of the angle $2 \pi n / k$ along $Z_{n, k}$. The second are compact Kähler-Einstein edge spaces with positive Ricci curvature $(n+1) / k$ and an edge singularity of angle $2 \pi / k$,
$$\omega_{\text {orb, } n, k},$$
on the weighted projective space $\mathbb{P}^{n}(1, \ldots, 1, k)$. These two model spaces turn out to be the different Gromov-Hausdorff limits of large-angle limits of the KEE metrics we construct on the Calabi-Hirzebruch manifolds.

\subsection*{2.1 Large angle limits}

The following result describes precisely the different large-angle limits that arise from these KEE metrics by either using different pointed limits or else parametrizing the angles in different ways. Note that $\beta_{1}$ ranges in ( $0, n / k$ ) and $\beta_{2}$ ranges in ( $0,1 / k$ ).

Theorem 2.4. Fix a base point $p$ on the zero section of $\mathbb{F}_{n, k}$ and $q$ on the infinity section. The pointed metric space $\left(\mathbb{F}_{n, k}, \eta_{\beta_{1}}, p\right)$ converges in the pointed Gromov-Hausdorff sense to $\left(-k H_{\mathbb{P}^{n-1}}, \omega_{\mathrm{eh}, n, k}, p\right)$ as $\beta_{1}$ tends to $n / k$. On the other hand, $\left(\mathbb{F}_{n, k}, \xi_{\beta_{2}}, q\right)$ converges in the pointed Gromov-Hausdorff sense to $\left(\mathbb{P}^{n}(1, \ldots, 1, k), \omega_{\text {orb }, n, k}, q\right)$ as $\beta_{2} \rightarrow 1 / k$.

In particular, when $n=k=2$, Theorem 2.4 resolves Conjecture 1.2. Theorem 2.4 amounts to saying that the famous Eguchi-Hanson metric from mathematical physics is the Gromov-Hausdorff limit of compact Kähler-Einstein edge metrics that we construct on the second Hirze-bruch surface (see Remark 6.3 for more details or see Appendix B for another proof). More generally, when $n=k$, Theorem 2.4 recovers a family of Ricci-flat metrics on the total space of canonical bundle of $\mathbb{P}^{n-1}$ that was constructed by Calabi [4], once again as a limit of compact Einstein spaces.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/59facd2c-e2e3-4682-b142-baa3b5352b01-04.jpg?height=864&width=928&top_left_y=1229&top_left_x=593}
\captionsetup{labelformat=empty}
\caption{Figure 1: The upper part shows the Kähler edge structure on the Calabi-Hirzebruch manifold $\mathbb{F}_{n, k}$. When $n=2, \mathbb{F}_{2, k}$ is the $k$-th Hirzebruch surface and $Z_{2, \pm k}$ is a $\mp k$-curve. The lower part shows the different limits described in Theorem 2.4. Note that on the left, we get a non-compact limit, with $q$ (together with all of $Z_{n,-k}$ ) pushed-out to infinity. On the right we get a compact limit, with $p$ limiting (together with all of $Z_{n, k}$ ) to an isolated orbifold point.}
\end{figure}

Remark 2.5. It would be interesting to find physical interpretations of Theorem 2.4 in the case $n=k=2$ of the Eguchi-Hanson metric.

The elementary proof of Theorem 2.4 is divided into two parts. In section 5, we study asymptotic behaviors of Kähler-Einstein edge metrics $\eta_{\beta_{1}}$ and $\xi_{\beta_{2}}$ when $\beta_{1}$, or respectively $\beta_{2}$, is close to $n / k$ or $1 / k$. In section 6, we prove the convergence results by studying a family of ODEs that arises from the construction of $\eta_{\beta_{1}}$ and $\xi_{\beta_{2}}$.
Remark 2.6. The two families of Kähler-Einstein edge metrics $\eta_{\beta_{1}}$ and $\xi_{\beta_{2}}$ are related via a simple, but important, rescaling. In Theorem 2.4, we see that different limits airse for those two family of metrics. The normalization factor can be obtained by studying the asymptotic behavior of $\xi_{\beta_{2}}$ : see Proposition 5.5 for details.
Remark 2.7. As noted before Theorem 2.4, $\beta_{1}$ ranges in $(0, n / k)$ and $\beta_{2}$ ranges in $(0,1 / k)$. In proving Theorem 2.4 for the family $\eta_{\beta_{1}}$ one obtains the asymptotic dependence of $\beta_{2}$ on $\beta_{1}$ in terms of a parameter that controls the length of the fibers in the Hirzebruch fibration-see (5.9). This shows that as $\beta_{1}$ tends to its maximal value $n / k, \beta_{2}$ tends to its maximal value as well, $1 / k$, and the divisor $Z_{n, k}$ gets pushed-off to infinity. It thus comes a bit as a surprise that when we consider the family $\xi_{\beta_{2}}$ parametrized in terms of $\beta_{2}$, and we let $\beta_{2}$ tend towards $1 / k$, while the parameter $\beta_{1}$ still tends towards its maximal value $n / k$ we get a completely different limiting behavior: instead of a non-compact limit we get a compact limit via a metric degeneration along $Z_{n, k}$. Thus, studying the two families is an essential feature of the setting and leads to two completely different Gromov-Hausdorff limits as in Theorem 2.4. It would be interesting to generalize this phenomenon to other settings.

\subsection*{2.2 Small angle limits}

Next, we resolve Conjecture 1.1 in the setting of $\mathbb{F}_{n, k}$. Denote by $\widetilde{\eta_{\beta_{1}}}$ and $\widetilde{\xi_{\beta_{2}}}$ fiber-wise rescalings of $\eta_{\beta_{1}}, \xi_{\beta_{2}}$, respectively (see (7.7) and §7).

Theorem 2.8. Both $\left(\mathbb{F}_{n, k}, \eta_{\beta_{1}}\right)$ and $\left(\mathbb{F}_{n, k}, \xi_{\beta_{2}}\right)$ converge in the Gromov-Hausdorff sense to $\left(\mathbb{P}^{n-1}, k \omega_{\mathrm{FS}}\right)$ as $\beta_{1}$ or $\beta_{2}$ tends to 0 . Moreover, as $\beta_{1} \searrow 0,\left(\mathbb{F}_{n, k}, \widetilde{\eta_{\beta_{1}}}, p\right)$ converges in the pointed Gromov-Hausdorff sense to $\left(\mathbb{P}^{n-1} \times \mathbb{C}^{*}, \frac{k}{n}\left(n \pi_{1}^{*} \omega_{\mathrm{FS}}+\pi_{2}^{*} \omega_{\mathrm{Cyl}}\right), p\right)$ and similarly for $\left(\mathbb{F}_{n, k}, \widetilde{\xi_{\beta_{2}}}, q\right)$, where $p, q \in \mathbb{F}_{n, k}$ are as in Theorem 2.4.

A compendium of the limit theorems in [13, 14] and the present work is shown in Table 1.

\begin{table}
\begin{tabular}[t]{|l|l|l|l|l|l|l|}
\hline $n$ & $k$ & $\beta_{1}$ & $\beta_{2}$ & Sequence & Limit & Reference \\
\hline 1 & $k$ & $\beta_{1} \searrow 0$ & $\beta_{2}\left(\beta_{1}\right) \equiv \beta_{1}$ & football metrics & $\left(\mathbb{C}^{*}, \omega_{\text {Cyl }}\right)$ & folklore, [13, Thm 1.3] \\
\hline 1 & $k$ & $\beta_{1} \nearrow 1$ & $\beta_{2}\left(\beta_{1}\right) \equiv \beta_{1}$ & football metrics & $\left(\mathbb{P}^{1}, \omega_{\mathrm{FS}}\right)$ & folklore, [13, Thm 1.2] \\
\hline 2 & $k$ & $\beta_{1} \searrow 0$ & $\beta_{2}\left(\beta_{1}\right)=\beta_{1}+O\left(\beta_{1}^{2}\right)$ & KEE metrics & $\left(\mathbb{P}^{1}, k \omega_{\mathrm{FS}}\right)$ & [14, Thm 1.2] \\
\hline 2 & $k$ & $\beta_{1} \searrow 0$ & $\beta_{2}\left(\beta_{1}\right)=\beta_{1}+O\left(\beta_{1}^{2}\right)$ & rescaled KEE metrics & $\left(\mathbb{P}^{1} \times \mathbb{C}^{*}, k \pi_{1}^{*} \omega_{\mathrm{FS}}+k \pi_{2}^{*} \omega_{\mathrm{Cyl}}\right)$ & [14, Thm 1.2] \\
\hline 2 & 1 & $\beta_{1} \rightarrow 1$ & $\beta_{2}\left(\beta_{1}\right) \rightarrow \sqrt{3}-1$ & KEE metrics & KEE metric on $\left(\mathbb{F}_{1}, Z_{-1}\right)$ & [14, Cor 1.5] \\
\hline 2 & 1 & $\beta_{1} \nearrow 2$ & $\beta_{2}\left(\beta_{1}\right) \nearrow 1$ & KEE metrics & Ricci-flat metric on $\left(-H_{\mathbb{P}^{1}}, Z_{1}\right)$ & Thm C. 3 \\
\hline 2 & 1 & the metric degenerates on $Z_{1}$ & $\beta_{2} \nearrow 1$ & KEE metrics & $\left(\mathbb{P}^{2}, \omega_{\mathrm{FS}}\right)$ & Thm C.5. \\
\hline 2 & 1 & $\beta_{1}\left(\beta_{2}\right) \nearrow 2$ & $\beta_{2} \nearrow 1$ & rescaled KEE metrics & Ricci-flat metric on $\left(-H_{\mathbb{P}^{1}}, Z_{1}\right)$ & Thm C. 7 \\
\hline 2 & 2 & $\beta_{1} \nearrow 1$ & $\beta_{2}\left(\beta_{1}\right) \nearrow 2$ & KEE metrics & Eguchi-Hanson metric $(\epsilon=1)$ & Thm 6.1 \\
\hline 2 & $k$ & the metric degenerates on $Z_{2, k}$ & $\beta_{2}\left(\beta_{1}\right) \nearrow 1 / k$ & KEE metrics & $\left(\mathbb{P}^{2}(1,1, k), \omega_{\text {orb }, 2, k}\right)$ & Thm 6.4 \\
\hline $n$ & 1 & the metric degenerates on $Z_{n, 1}$ & $\beta_{2}\left(\beta_{1}\right) \nearrow 1$ & KEE metrics & $\left(\mathbb{P}^{n}, \omega_{\mathrm{FS}}\right)$ & Thm 6.4 \\
\hline $n$ & $k$ & $\beta_{1} \nearrow n / k$ & $\beta_{2}\left(\beta_{1}\right) \nearrow 1 / k$ & KEE metrics & $\left(-k H_{\mathbb{P}^{n-1}}, \omega_{\mathrm{eh}, n, k}\right)$ & Thm 6.1 \\
\hline $n$ & $k$ & $\beta_{1} \searrow 0$ & $\beta_{2}\left(\beta_{1}\right)=\beta_{1}+O\left(\beta_{1}^{2}\right)$ & rescaled KEE metrics & $\left(\mathbb{P}^{n-1} \times \mathbb{C}^{*}, \frac{k}{n}\left(n \pi_{1}^{*} \omega_{\mathrm{FS}}+\pi_{2}^{*} \omega_{\mathrm{Cyl}}\right)\right)$ & Thm 7.6 \\
\hline $n$ & $k$ & the metric degenerates on $Z_{n, k}$ & $\beta_{2} \nearrow 1 / k$ & KEE metrics & $\left(\mathbb{P}^{n}(1, \ldots, 1, k), \omega_{\text {orb }, n, k}\right)$ & Thm 6.4 \\
\hline $n$ & $k$ & $\beta_{1}\left(\beta_{2}\right) \nearrow n / k$ & $\beta_{2} \nearrow 1 / k$ & rescaled KEE metrics & $\left(-k H_{\mathbb{P}^{n-1}}, \omega_{\mathrm{eh}, n, k}\right)$ & Cor 6.5 \\
\hline $n$ & $k$ & $\beta_{1}\left(\beta_{2}\right)=\beta_{2}+O\left(\beta_{2}^{2}\right)$ & $\beta_{2} \searrow 0$ & rescaled KEE metrics & $\left(\mathbb{P}^{n-1} \times \mathbb{C}^{*}, \frac{k}{n}\left(n \pi_{1}^{*} \omega_{\mathrm{FS}}+\pi_{2}^{*} \omega_{\mathrm{Cyl}}\right)\right)$ & Thm 7.11 \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 1: Limits of Kähler-Einstein edge metrics on $\mathbb{F}_{n, k}$, the $k$-th Calabi-Hirzebruch manifold of dimension $n$.}
\end{table}

\subsection*{2.3 Organization}

In Section 3, we first review the construction of Calabi-Hirzebruch manifolds and then define two families of model metrics respectively on the total space of line bundles $-k H_{\mathbb{P}^{n-1}}$ and the Calabi-Hirzebruch manifolds. In Section 4, we construct Kähler-Einstein edge metrics on the Calabi-Hirzebruch manifolds following Calabi ansatz. In Section 5, we study the asymptotic behaviors of Kähler-Einstein edge metrics by reducing it to the study of some ODEs. In Section 6, we consider the Gromov-Hausdorff limits of the Kähler-Einstein edge metrics on the Calabi-Hirzebruch manifolds and find out the model metrics in the limit. Theorem 2.4 is then proved in two parts: Theorem 6.1 and Theorem 6.4. The first statement of Theorem 2.8 about the non-rescaled limits is proved in Theorems 7.1 and 7.10. The second statement of Theorem 2.8 concerning rescaled limits and pointed limits is contained in Theorems 7.6 and 7.11. We also discuss the relation between Theorem 6.1 and Theorem 6.4 as mentioned in Remark 2.6 in Corollary 6.5.

Finally, we end with several appendices whose main purpose is to bridge the mathematical, or "Calabi's" formalism, and the physics, or "Eguchi-Hanson" setting. These should make the article accessible to the physics audience, as well as introduce some of the physics motivation for the article to the mathematical audience. Appendices A and B provide a brief review on basic properties of Eguchi-Hanson metrics and explain how to understand Eguchi-Hanson metrics as Gromov-Hausdorff limits of Kähler-Einstein edge metrics. In Appendix C, we provide more examples of Kähler-Einstein edge metrics and their Gromov-Hausdorff limit metrics.

Acknowledgments. Research supported by NSF grant 1906370, NSFC grant 12101052, the Fundamental Research Funds 2021NTST10 for the Central Universities, and a Brin Graduate Fellowship at the University of Maryland. YAR thanks C. LeBrun for informing him of [1, 2]. The authors are grateful to the referees for their careful reading and comments.

This article is dedicated to Scott Wolpert that aside from his seminal mathematical contributions to complex geometry has been instrumental in forging the University of Maryland as a leader in that field, and has positively impacted the careers of all three authors as either graduate students or faculty in the department (and, in particular, in all likelihood this article would not have appeared had it not been for his constant support).

\section*{3 Model metrics}

We first review the construction of Calabi-Hirzebruch manifolds [5, 9].
Definition 3.1. The Calabi-Hirzebruch manifold, denoted by $\mathbb{F}_{n, k}$, where $n, k \in \mathbb{N}$, is defined as follows:
$$\mathbb{F}_{n, k}:=\mathbb{P}\left(-k H_{\mathbb{P}^{n-1}} \oplus \mathbb{C}_{\mathbb{P}^{n-1}}\right), \quad n, k \in \mathbb{N},$$
where $H_{\mathbb{P}^{n-1}}$ is the hyperplane bundle over $\mathbb{P}^{n-1}$ and $\mathbb{C}_{\mathbb{P}^{n-1}}$ is the trivial one.
An alternative way to define $\mathbb{F}_{n, k}$ is by adding an infinity section to the blow up of $\mathbb{C}^{n} / \mathbb{Z}_{k}$ at the origin [14, Lemma 2.1].

In this section, we introduce two model metrics $\omega_{\text {eh }, n, k}$ and $\omega_{\text {orb }, n, k}$, that are defined on the total space of line bundle $-k H_{\mathbb{P}^{n-1}}$ and on the weighted projective space $\mathbb{P}^{n}(1, \ldots, 1, k)$, respectively. They will serve as the candidates of limit metrics in the latter sections.

Denote by $\left[Z_{1}: \cdots: Z_{n}\right]$ the homogeneous coordinates on $\mathbb{P}^{n-1}$. Working on the chart $\left\{Z_{i} \neq 0\right\}$, we shall use the nonhomogeneous coordinates $z_{j}:=Z_{j} / Z_{i}$ for all $j \neq i$. Denote
by $w$ the coordinate along each fiber on $-k H_{\mathbb{P}^{n-1}}$ or $\mathbb{F}_{n, k}$. Then $w \in \mathbb{C}$ for $-k H_{\mathbb{P}^{n-1}}$ and $w \in \mathbb{C} \cup\{\infty\}$ for $\mathbb{F}_{n, k}$. In particular, we have two divisors on $\mathbb{F}_{n, k}$ : the zero section
$$Z_{n, k}:=\{w=0\}$$
and the infinity section
$$Z_{n,-k}:=\{w=\infty\} .$$
Consider the Hermitian norm on $-k H_{\mathbb{P}^{n-1}}$ (and also $\mathbb{F}_{n, k}$ )
$$\left\|\left(z_{1}, \ldots, \hat{z}_{i}, \ldots, z_{n}, w\right)\right\|:=|w|^{2}\left(1+\sum_{j \neq i}^{n}\left|z_{j}\right|^{2}\right)^{k},$$
on the chart $\left\{Z_{i} \neq 0\right\}$. Let $s$ be the logarithm of this fiberwise norm, i.e.,
$$s:=\log |w|^{2}+k \log \left(1+\sum_{j \neq i}\left|z_{j}\right|^{2}\right) .$$
Next, we define model metrics that depend only on $s$ on $-k H_{\mathbb{P}^{n-1}}$ and $\mathbb{P}^{n}(1, \ldots, 1, k)$.

\subsection*{3.1 Non-compact case: model metrics on $-k H_{\mathbb{P}^{n-1}}$}

The first model metric, $\omega_{\mathrm{eh}, n, k}$, is a Ricci-flat edge metric with edge singularity of angle $2 n \pi / k$ along the zero section $Z_{n, k}$ of $-k H_{\mathbb{P}^{n-1}}$. In particular, when $n=k$, this metric is smooth. Indeed, when $n=k, \omega_{\mathrm{eh}, n, k}$ coincides with the Ricci-flat metric on the canonical bundle of $\mathbb{P}^{n-1}$ that was constructed by Calabi [4].

Definition 3.2. Let $s$ be defined in (3.1). To define $\omega_{\mathrm{eh}, n, k}$, introduce another coordinate $\lambda \in(1,+\infty)$ such that
$$\lambda=\left(e^{\frac{n}{k} s}+1\right)^{\frac{1}{n}} .$$
Thus $\{\lambda=1\}$ corresponds to the zero section $Z_{n, k}=\{w=0\}$ on $-k H_{\mathbb{P}^{n-1}}$. We define $\omega_{\mathrm{eh}, n, k}$ by giving its potential function as follows:
$$f(\lambda):=k \lambda+k \int \frac{1}{\lambda^{n}-1} \mathrm{~d} \lambda,$$
where the last term denotes an indefinite integral, and
$$\omega_{\mathrm{eh}, n, k}:=\sqrt{-1} \partial \bar{\partial} f(s) .$$
The metric $\omega_{\mathrm{eh}, n, k}$ is a Ricci-flat metric on $-k H_{\mathbb{P}^{n-1}}$ with edge singularity of angle $2 n \pi / k$ along the zero section (See Theorem 6.1 for details). It can be seen as a generalization of Eguchi-Hanson metrics to higher dimensional manifolds (See Remark 3.3 for details). More precisely, in local coordinates,
$$\begin{aligned}
& \omega_{\mathrm{eh}, n, k}=k\left(e^{\frac{n}{k} s}+1\right)^{\frac{1}{n}} \pi_{1}^{*} \omega_{\mathrm{FS}}+\frac{e^{\frac{n}{k} s}}{k\left(e^{\frac{n}{k} s}+1\right)^{\frac{n-1}{n}}}\left(\frac{\sqrt{-1} \mathrm{~d} w \wedge \mathrm{~d} \bar{w}}{|w|^{2}}+\sqrt{-1} \alpha \wedge \bar{\alpha}+\right. \\
&\left.\sqrt{-1} \alpha \wedge \frac{\mathrm{~d} \bar{w}}{\bar{w}}+\sqrt{-1} \frac{\mathrm{~d} w}{w} \wedge \bar{\alpha}\right)
\end{aligned}$$
where
$$\alpha=k \frac{\sum_{i \neq j} \bar{z}_{i} \mathrm{~d} z_{i}}{1+\sum_{i \neq j}\left|z_{i}\right|^{2}}, \quad \text { on the chart }\left\{z_{j} \neq 0\right\},$$
and
$$\pi_{1}\left(\left[Z_{1}: \cdots: Z_{n}\right], w\right)=\left[Z_{1}: \cdots: Z_{n}\right]$$
is the projection map from the total space $-k H_{\mathbb{P}^{n-1}}$ to the base space $\mathbb{P}^{n-1}$.
Remark 3.3. Fixing $n=k=2$ in (3.2) and (3.3), we obtain that on $-2 H_{\mathbb{P}^{1}}$ the model metric $\omega_{\mathrm{eh}, n, k}$ has the expression
$$\sqrt{-1} \partial \bar{\partial}(2 \lambda+\log (\lambda-1)-\log (\lambda+1)), \quad \lambda>1 .$$
Set
$$r:=e^{\frac{1}{4} s}, \quad r>0 .$$
Plugging (3.2) and (3.5) in (3.4), one finds $\omega_{\mathrm{eh}, n, k}$ has the following expression on $-2 H_{\mathbb{P}^{1}}$ :
$$\sqrt{-1} \partial \bar{\partial}\left[\sqrt{r^{4}+1}+\log r^{2}-\log \left(\sqrt{r^{4}+1}+1\right)\right] .$$
(3.6) coincides with (A.11) in the Appendix where we put $\epsilon=1$. In other words, when $n=k=2, \omega_{\mathrm{eh}, n, k}$ recovers the famous Eguchi-Hanson metric [8] that is constructed on the total space of $-2 H_{\mathbb{P}^{1}}$.

It is recalled in Proposition A. 1 that the Eguchi-Hanson metric is Ricci-flat. The metric $\omega_{\mathrm{eh}, n, k}$, which is also Ricci-flat but with edge singularities along $Z_{n, k}$ when $n \neq k$, can be seen as a generalization of Eguchi-Hanson metrics to the total space of $-k H_{\mathbb{P}^{n-1}}$ for arbitrary $n, k \in \mathbb{N}_{>0}$.

\subsection*{3.2 Compact case: model metrics on $\mathbb{P}^{n}(1, \ldots, 1, k)$}

In this section, we introduce another model metric $\omega_{\text {orb, } n, k}$ that is defined on the weighted projective space $\mathbb{P}^{n}(1, \ldots, 1, k)$. We first recall the construction of the weighted projective space and its orbifold structure.

Definition 3.4. For $k \in \mathbb{N}$, consider the group action of $\mathbb{C}^{*}$ on $\mathbb{C}^{n+1} \backslash\{0\}$ given by
$$\lambda \cdot\left(z_{0}, \ldots, z_{n-1}, z_{n}\right)=\left(\lambda z_{0}, \ldots, \lambda z_{n-1}, \lambda^{k} z_{n}\right), \quad \lambda \in \mathbb{C}^{*},\left(z_{0}, \ldots, z_{n-1}, z_{n}\right) \in \mathbb{C}^{n+1} \backslash\{0\} .$$
Then the weighted projective space $\mathbb{P}^{n}(1, \ldots, 1, k)$ is defined as the quotient of this group action:
$$\mathbb{P}^{n}(1, \ldots, 1, k):=\left(\mathbb{C}^{n+1} \backslash\{0\}\right) / \mathbb{C}^{*} .$$
We use homogeneous coordinates on $\mathbb{P}^{n}(1, \ldots, 1, k)$. A point $\left[x_{0}: \cdots: x_{n-1}: x_{n}\right] \in$ $\mathbb{P}^{n}(1, \ldots, 1, k)$ corresponds to an equivalence class in $\mathbb{C}^{n+1} \backslash\{0\}$. More precisely,
$$\left[x_{0}: \cdots: x_{n-1}: x_{n}\right]:=\left\{\lambda x_{0}, \ldots, \lambda x_{n-1}, \lambda^{k} x_{n}: \lambda \in \mathbb{C}^{*}\right\} .$$

Consider the $\mathbb{Z}_{k}$ action on $\mathbb{C}^{n}$ such that the $\mathbb{Z}_{k}$ orbit of a point $\left(z_{1}, \ldots, z_{n}\right) \in \mathbb{C}^{n}$ is
$$\left\{e^{\frac{2 \pi \sqrt{-1} \ell}{k}} z_{1}, \ldots, e^{\frac{2 \pi \sqrt{-1} \ell}{k}} z_{n}: \ell=0, \ldots, k-1\right\} .$$

Then near the point $[0: 0 \cdots: 0: 1] \in \mathbb{P}^{n}(1, \ldots, 1, k)$ the local structure is $\mathbb{C}^{n} / \mathbb{Z}_{k}$. The next lemma shows the relation between $\mathbb{P}^{n}(1, \ldots, 1, k)$ and $\mathbb{F}_{n, k}$.

Lemma 3.5. The total space of the line bundle $k H_{\mathbb{P}^{n-1}}$ can be embedded in the weighted projective space $\mathbb{P}^{n}(1, \ldots, 1, k)$ and the complement is a single point $p=[0: \cdots: 0: 1] \in$ $\mathbb{P}^{n}(1, \ldots, 1, k)$. Moreover, $\mathbb{F}_{n, k}$ is the blow up of $\mathbb{P}^{n}(1, \ldots, 1, k)$ at $p$.

Proof. Since for any vector bundle $A$ and line bundle $L$ we have $\mathbb{P}(A \otimes L)=\mathbb{P}(A)$, it follows that $\mathbb{F}_{n,-k}$ is biholomorphic to $\mathbb{F}_{n, k}$ by taking $L=2 k H_{\mathbb{P}^{n-1}}$ in Definition 3.1 with the biholomorphism exchanging the zero and the infinity sections $Z_{n, k}$ and $Z_{n,-k}$. Thus, we identify $\mathbb{F}_{n, k}$ as
$$\mathbb{F}_{n, k}=\mathbb{P}\left(k H_{\mathbb{P}^{n-1}} \oplus \mathbb{C}_{\mathbb{P}^{n-1}}\right) .$$
We first show the total space of $k H_{\mathbb{P}^{n-1}}$ can be naturally embedded in $\mathbb{P}^{n}(1, \ldots, 1, k)$.
Consider $\mathbb{P}^{n}(1, \ldots, 1, k)$ with homogeneous coordinate $\left[x_{0}: \cdots, x_{n}\right]$ and embed $\mathbb{P}^{n-1}$ in $\mathbb{P}^{n}$ as $\left\{x_{n}=0\right\}$. Recall the transition function at a point $\left[x_{0}: \cdots: x_{n-1}\right] \in \mathbb{P}^{n-1}$ of the line bundle $k H_{\mathbb{P}^{n-1}}$ is given by
$$g_{i j}\left(\left[x_{0}: \cdots: x_{n-1}\right]\right)=\left(\frac{x_{j}}{x_{i}}\right)^{k} .$$
Then the fiber of $k H_{\mathbb{P}^{n-1}}$ at an arbitrary point $\left[x_{0}: \cdots, x_{n-1}: 0\right] \in \mathbb{P}^{n}(1, \ldots, 1, k)$ can be identified as the set of all $\left[x_{0}: \cdots: x_{n-1}: \lambda\right]$ for $\lambda \in \mathbb{C}$, where $\left[x_{0}: \cdots: x_{n-1}: \lambda\right]$ is defined in (3.7). By definition of the weighted projective space and (3.9), this is well-defined. Thus, $k H_{\mathbb{P}^{n-1}}$ can be naturally embedded in $\mathbb{P}^{n}(1, \ldots, 1, k)$ and the complement is the point $[0: \cdots: 0: 1]$. We have mentioned that the local structure of $\mathbb{P}^{n}(1, \ldots, 1, k)$ near this point is $\mathbb{C}^{n} / \mathbb{Z}_{k}$.

Next, we blow up $\mathbb{P}^{n}(1, \ldots, 1, k)$ at $[0: \cdots: 0: 1]$. The exceptional divisor can be identified as adding an infinity section that is biholomorphic to $\mathbb{P}^{n-1}$ to the total space $k H_{\mathbb{P}^{n-1}}$. Combining this observation with (3.8), one realizes the manifold upstairs is the Calabi-Hirzebruch manifold $\mathbb{F}_{n, k}$. We henceforth denote by $\pi$ the blow down map. \(\square\)

Now we are ready to define $\omega_{\text {orb }, n, k}$. To do so, we first define another family of model metrics $\tilde{\omega}_{\text {orb, } n, k}$ on $\mathbb{F}_{n, k}$. The metric $\tilde{\omega}_{\text {orb, } n, k}$ is a Kähler-Einstein edge metric with Ricci curvature $(n+1) / k$ and an edge singularity of angle $2 \pi / k$ along $Z_{n,-k}$ that degenerates on $Z_{n, k}$. In particular, this metric is smooth along $Z_{n,-k}$ when $k=1$ and collapses along $Z_{n, k}$. Indeed, when $k=1$ this metric coincides with the Fubini-Study metric on $\mathbb{P}^{n}$. We will then define $\omega_{\text {orb }, n, k}$ as the pull-back of the metric $\tilde{\omega}_{\text {orb, } n, k}$ under the blow up map.

Definition 3.6. Let $s$ be defined in (3.1). To define $\tilde{\omega}_{\text {orb, } n, k}$, introduce another coordinate $\nu \in(0,1)$ such that
$$\nu=1-\left(e^{\frac{s}{k}}+1\right)^{-1} .$$
Note that $\{\nu=0\}$ and $\{\nu=1\}$ correspond to the zero section $Z_{n, k}$ and the infinity section $Z_{n,-k}$ respectively. We define $\tilde{\omega}_{\text {orb, } n, k}$ by giving its potential function as follows:
$$g(\nu):=-k \log (1-\nu), \quad \nu \in(0,1),$$
and
$$\tilde{\omega}_{\text {orb }, n, k}:=\sqrt{-1} \partial \bar{\partial} g(s) .$$
Note that $\tilde{\omega}_{\text {orb, } n, k}$ is a degenerate Kähler-Einstein edge metric on $\mathbb{F}_{n, k}$ with Ricci curvature $(n+1) / k$ and an edge singularity of the angle $2 \pi / k$ along $Z_{n,-k}$, while $\tilde{\omega}_{\text {orb }, n, k}$ collapses along
$Z_{n, k}$ (See Theorem 6.4 for details). More precisely, in local coordinates,
$$\begin{aligned}
& \tilde{\omega}_{\text {orb }, n, k}=\frac{k e^{\frac{s}{k}}}{e^{\frac{s}{k}}+1} \pi_{1}^{*} \omega_{\mathrm{FS}}+\frac{e^{\frac{s}{k}}}{k\left(e^{\frac{s}{k}}+1\right)}\left(\frac{\sqrt{-1} \mathrm{~d} w \wedge \mathrm{~d} \bar{w}}{|w|^{2}}+\sqrt{-1} \alpha \wedge \bar{\alpha}+\right. \\
&\left.\sqrt{-1} \alpha \wedge \frac{\mathrm{~d} \bar{w}}{\bar{w}}+\sqrt{-1} \frac{\mathrm{~d} w}{w} \wedge \bar{\alpha}\right),
\end{aligned}$$
where
$$\alpha=k \frac{\sum_{i \neq j} \bar{z}_{i} \mathrm{~d} z_{i}}{1+\sum_{i \neq j}\left|z_{i}\right|^{2}}, \quad \text { on the chart }\left\{z_{j} \neq 0\right\},$$
and
$$\pi_{1}\left(\left[Z_{1}: \cdots: Z_{n}\right], w\right)=\left[Z_{1}: \cdots: Z_{n}\right]$$
is the projection map from $\mathbb{F}_{n, k}$ to the zero section $Z_{n, k}$ identified as $\mathbb{P}^{n-1}$.
Definition 3.7. For $k>1$, the model metric $\omega_{\text {orb }, n, k}$ on $\mathbb{P}^{n}(1, \ldots, 1, k)$ is defined away from $[0: \cdots: 0: 1]$ as the pull-back of the metric $\tilde{\omega}_{\text {orb }, n, k}$ on $\mathbb{F}_{n, k} \backslash\left\{Z_{n, k}\right\}$ under the inverse of the blow up map. For $k=1$, we define $\omega_{\text {orb }, n, 1}$ as the Fubini-Study metric on $\mathbb{P}^{n}(1, \ldots, 1,1)=\mathbb{P}^{n}$.

\section*{4 Constructions of Kähler-Einstein edge metrics}

In this section, we aim to construct Kähler-Einstein edge metrics defined on the Calabi-Hirzebruch manifold $\mathbb{F}_{n, k}$ with edge singularities along the zero section $Z_{n, k}$ and the infinity section $Z_{n,-k}$ using Calabi ansatz. By Kähler-Einstein edge metrics we mean Kähler edge currents that satisfy the Kähler-Einstein equation on smooth locus. The reader may refer to [12] for detailed exposition of Kähler edge metrics.

\subsection*{4.1 Constructions of $\eta_{\beta_{1}}$ on $\mathbb{F}_{n, k}$}

Recall, the coordinate $s$ is defined in (3.1), where $w$ and $z_{j}, j \neq i$ are coordinates we use when working on the chart $\left\{Z_{i} \neq 0\right\} \subset \mathbb{F}_{n, k}$. We seek a Kähler-Einstein edge metric
$$\eta:=\sqrt{-1} \partial \bar{\partial} f(s)$$
for some smooth function $f$ on $\mathbb{F}_{n, k}$. Define
$$\begin{aligned}
& \tau(s):=f^{\prime}(s), \quad s \in(-\infty,+\infty) \\
& \varphi(s):=f^{\prime \prime}(s)=\tau^{\prime}(s), \quad s \in(-\infty,+\infty) .
\end{aligned}$$

Let $\pi_{1}$ and $\pi_{2}$ be projections from $\mathbb{F}_{n, k}$ to the zero section $Z_{n, k}$ and each fiber respectively, i.e.,
$$\begin{aligned}
& \pi_{1}\left(\left[Z_{1}: \cdots: Z_{n}\right], w\right)=\left[Z_{1}: \cdots: Z_{n}\right], \\
& \pi_{2}\left(\left[Z_{1}: \cdots: Z_{n}\right], w\right)=w .
\end{aligned}$$
Denote by $\omega_{\mathrm{FS}}$ the Fubini-Study metric on $\mathbb{P}^{n-1}$ and define
$$\begin{aligned}
\omega_{\mathrm{Cyl}} & :=\frac{\sqrt{-1} \mathrm{~d} w \wedge \mathrm{~d} \bar{w}}{|w|^{2}} \\
\alpha & :=\frac{k \sum_{j \neq i} \bar{z}_{j} \mathrm{~d} z_{j}}{1+\sum_{j \neq i}\left|z_{j}\right|^{2}}, \quad \text { on the chart }\left\{Z_{i} \neq 0\right\} .
\end{aligned}$$

Then direct calculation (cf. [14, Section 3.3] for detailed computations in dimension $n=2$ ) yields
$$\begin{aligned}
\eta=k \tau \pi_{1}^{*} \omega_{\mathrm{FS}}+\varphi & \left(\pi_{2}^{*} \omega_{\mathrm{Cyl}}+\sqrt{-1} \alpha \wedge \bar{\alpha}+\right. \\
& \left.\sqrt{-1} \alpha \wedge \frac{\mathrm{~d} \bar{w}}{\bar{w}}+\sqrt{-1} \frac{\mathrm{~d} w}{w} \wedge \bar{\alpha}\right) .
\end{aligned}$$

Positive definiteness of $\eta$ then implies $f^{\prime} \geq 0$ and $f^{\prime \prime} \geq 0$ for $s \in(-\infty,+\infty)$.
Proposition 4.1. Assume $Z_{n, k}$ is non-collapsed, then $\inf _{s \in \mathbb{R}} \tau(s)>0$. Moreover, $\sup _{s \in \mathbb{R}} \tau(s)<+\infty$.

Proof. Assume by contradiction that $\inf _{s \in \mathbb{R}} \tau(s)=0$. Then by (4.2), $\eta$ is identically zero when restricted to $Z_{n, k}$. However, we assume $Z_{n, k}$ is non-collapsed. Thus we must have $\inf _{s \in \mathbb{R}} \tau(s)>0$. To see $\sup _{s \in \mathbb{R}} \tau(s)<+\infty$, we follow the arguments in [14, Lemma 3.2]. Indeed, restricting $\eta$ to the fiber $\left\{Z_{j}=0, \forall j \neq i\right\}$, in (4.2) we get
$$\begin{aligned}
\eta & =\varphi \cdot \pi_{2}^{*} \omega_{\mathrm{Cyl}} \\
& =\varphi \frac{\sqrt{-1} \mathrm{~d} w \wedge \mathrm{~d} \bar{w}}{|w|^{2}},
\end{aligned}$$
and also in this case $s=\log |w|^{2}$. Then we use the coordinate $w=e^{s / 2+\sqrt{-1} \theta}$ on this fiber, and by (4.3) $\eta$ restricted on the fiber gives a metric
$$g_{\eta}=\frac{1}{2 \varphi(\tau)} \mathrm{d} \tau^{2}+2 \varphi(\tau) \mathrm{d} \theta^{2} .$$
Thus, the volume form on the fiber is $\mathrm{d} \tau \wedge \mathrm{d} \theta$, and the volume of the fiber is $2 \pi\left(\sup _{s \in \mathbb{R}} \tau(s)-\right.$ $\inf _{s \in \mathbb{R}} \tau(s)$ ). Since for any Kähler edge metric the volume of a complex submanifold is finite, we conclude $\sup _{s \in \mathbb{R}} \tau(s)<\infty$. \(\square\)

By Proposition 4.1, we may rescale $f$ by a positive constant such that $\inf \tau=1$ and $\sup \tau=T<\infty$. Thus, we henceforth assume that $\tau$ ranges from $[1, T]$.

Proposition 4.2. If $\eta$ is a Kähler edge metric with conic singularities along $Z_{n, k}$ and $Z_{n,-k}$, then
$$\begin{array}{ll}
\varphi(1)=0, & \frac{d \varphi}{d \tau}(1)=\beta_{1}, \\
\varphi(T)=0, & \frac{d \varphi}{d \tau}(T)=-\beta_{2},
\end{array}$$
if we denote by $2 \pi \beta_{1}$ and $2 \pi \beta_{2}$ respectively the angles of $\eta$ along $Z_{n, k}$ and $Z_{n,-k}$.
Proof. Recall we assume $\tau$ ranges from $[1, T]$. In particular, this implies that
$$\lim _{s \rightarrow \pm \infty} \frac{\mathrm{d} \tau}{\mathrm{~d} s}=0,$$
which combines with (4.1) show that
$$\varphi(1)=\varphi(T)=0 .$$
Next, we follow the arguments in the proof of [14, Proposition 3.3]. Indeed, it follows from [10, Theorem 1, proposition 4.4] that the potential function $f$ of $\eta$ has complete asymptotic
expansions near both $w=0$ and $w=\infty$. Near $w=0$, the leading term in the expansion is $|w|^{2 \beta_{1}}$. More precisely, by (3.1),
$$\begin{aligned}
\varphi & \sim C_{1}+C_{2}|w|^{2 \beta_{1}}+\left(C_{3} \sin \theta+C_{4} \cos \theta\right)|w|^{2}+O\left(|w|^{2+\epsilon}\right) \\
& =C_{1}+C_{2} e^{\beta_{1} s}+\left(C_{3} \sin \theta+C_{4} \cos \theta\right) e^{s}+O\left(e^{(1+\epsilon) s}\right) .
\end{aligned}$$
We first find $C_{1}=0$ by the fact that $\varphi(1)=\varphi(T)=0$ in (4.5). Moreover, the expansion can be differentiated term-by-term as $|w| \rightarrow 0$ or $s \rightarrow-\infty$. As $\varphi^{\prime}(\tau)=\frac{\partial \varphi}{\partial s} \frac{\mathrm{~d} s}{\mathrm{~d} \tau}=\frac{\partial \varphi}{\partial s} / \varphi$, we obtain
$$\varphi^{\prime}(1)=\beta_{1} .$$
The same arguments imply that
$$\varphi^{\prime}(T)=-\beta_{2},$$
where the minus sign comes from the fact that the leading term in this expansion is $|w|^{-2 \beta_{2}}=$ $e^{-\beta_{2} s}$. \(\square\)

Definition 4.3. A Kähler-Einstein edge metric $\omega$ is a Kähler edge metric that has constant Ricci curvature away from the singular locus.

By Definition 4.3, $\eta$ is a Kähler-Einstein edge metric if and only if it satisfies the following Kähler-Einstein edge equation:
$$\operatorname{Ric} \eta=\lambda \eta+\left(1-\beta_{1}\right)\left[Z_{n, k}\right]+\left(1-\beta_{2}\right)\left[Z_{n,-k}\right],$$
where by $\lambda$ we denote the Ricci curvature.
The next proposition shows that (4.6) is equivalent to an ODE satisfied by $\tau$ and $\varphi$ with boundary conditions given in (4.5).

Proposition 4.4. The Kähler edge metric $\eta$ given in (4.2) satisfies the Kähler-Einstein edge equation (4.6) if and only if
$$\begin{aligned}
& \lambda=\frac{n}{k}-\beta_{1}, \quad \beta_{1} \in\left(0, \frac{n}{k}\right), \\
& \varphi(\tau)=\frac{1}{k} \frac{\tau^{n}-1}{\tau^{n-1}}+\frac{1}{n+1}\left(\beta_{1}-\frac{n}{k}\right) \frac{\tau^{n+1}-1}{\tau^{n-1}}, \quad \tau \geq 1 .
\end{aligned}$$
Moreover, $\beta_{2}$ and $T$ are determined by $\beta_{1}$ such that $T>1$ and $\beta_{2}>0$.
Proof. By (4.2), we calculate Ric $\eta$ :
$$\begin{aligned}
\operatorname{Ric} \eta & =-\sqrt{-1} \partial \bar{\partial} \log \eta^{n} \\
& =-\sqrt{-1} \partial \bar{\partial} \log \left(k^{n-1} \tau^{n-1} \varphi\left(\pi_{1}^{*} \omega_{\mathrm{FS}}\right)^{n-1} \wedge \pi_{2}^{*} \omega_{\mathrm{Cyl}}\right) \\
& =\left(1-\beta_{1}\right)\left[Z_{n, k}\right]+\left(1-\beta_{2}\right)\left[Z_{n,-k}\right]+\left(n-k(n-1) \frac{\varphi}{\tau}-k \frac{\mathrm{~d} \varphi}{\mathrm{~d} \tau}\right) \pi_{1}^{*} \omega_{\mathrm{FS}} \\
& -\varphi \frac{\mathrm{d}}{\mathrm{~d} \tau}\left((n-1) \frac{\varphi}{\tau}+\frac{\mathrm{d} \varphi}{\mathrm{~d} \tau}\right)\left(\pi_{2}^{*} \omega_{\mathrm{Cyl}}+\sqrt{-1} \alpha \wedge \bar{\alpha}+\right. \\
& \left.\sqrt{-1} \alpha \wedge \frac{\mathrm{~d} \bar{w}}{\bar{w}}+\sqrt{-1} \frac{\mathrm{~d} w}{w} \wedge \bar{\alpha}\right) .
\end{aligned}$$

Plugging (4.2) and (4.9) in (4.6), (4.6) is equivalent to
$$\begin{aligned}
n-k(n-1) \frac{\varphi}{\tau}-k \frac{\mathrm{~d} \varphi}{\mathrm{~d} \tau} & =\lambda k \tau, \\
-\varphi \frac{\mathrm{d}}{\mathrm{~d} \tau}\left((n-1) \frac{\varphi}{\tau}+\frac{\mathrm{d} \varphi}{\mathrm{~d} \tau}\right) & =\lambda \varphi .
\end{aligned}$$
Now we first observe that (4.10) and (4.11) are equivalent since taking derivative of (4.10) with respect to $\tau$ gives (4.11). Thus we conclude (4.6) is equivalent to the ODE (4.10) together with boundary conditions (4.5). Solving this ODE with boundary conditions gives (4.7) and (4.8). We need the assumption $\beta_{1} \in(0, n / k)$ to ensure the existence of $T$ and $\beta_{2}$ that satisfy (4.5). Indeed, $\beta_{2}$ and $T$ are determined by $\beta_{1}$ due to (4.5) and (4.8). More precisely, $T$ should be a root of the polynomial that appears in the right hand side of (4.8) and $-\beta_{2}$ should be determined by the derivative $\mathrm{d} \varphi / \mathrm{d} \tau$ at $T$. Writing (4.8) as $\varphi(\tau)=P(\tau) / \tau^{n-1}$, we factor $P(\tau)$ as
$$\begin{aligned}
P(\tau) & =(\tau-1)\left[\frac{1}{k}\left(\tau^{n-1}+\cdots+1\right)+\frac{1}{n+1}\left(\beta_{1}-\frac{n}{k}\right)\left(\tau^{n}+\cdots+1\right)\right] \\
& =\frac{(\tau-1)}{n+1}\left[\left(\beta_{1}-\frac{n}{k}\right) \tau^{n}+\left(\frac{1}{k}+\beta_{1}\right)\left(\tau^{n-1}+\cdots+1\right)\right] .
\end{aligned}$$
Under the assumption $\beta_{1} \in(0, n / k)$, one finds $P(\tau)>0$ for $1<\tau \ll 2$ and $P(\tau)<0$ for $\tau \rightarrow \infty$. Thus, $P(\tau)$ has at least one real root that is greater than 1. Denote by $T$ the first root of $P$ after 1. In particular, $\mathrm{d} \varphi / \mathrm{d} \tau(T)<0$. By (4.5), this implies that $\beta_{2}>0$ as claimed. \(\square\)

By (4.1), there holds
$$\frac{\mathrm{d} s}{\mathrm{~d} \tau}=\frac{1}{\varphi(\tau)} .$$
Combining (4.2), (4.13) and Proposition 4.4 altogether, we realize that given $\beta_{1} \in(0, n / k)$ we can construct a Kähler-Einstein edge metric $\eta$ on $\mathbb{F}_{n, k}$ using coordinates $\tau$ and $\varphi$. This Kähler-Einstein edge metric has Ricci curvature $\lambda=n / k-\beta_{1}$, and has edge singularities of angle $2 \pi \beta_{1}$ along $Z_{n, k}$ and angle $2 \pi \beta_{2}$ along $Z_{n,-k}$. Note that $\beta_{2}$ is determined by $\beta_{1}$. In other words, we can construct a family of Kähler-Einstein edge metrics on $\mathbb{F}_{n, k}$ parametrized by $\beta_{1} \in(0, n / k)$. In Section 5, we study the asymptotic behavior of this family of metrics when $\beta_{1}$ approaches the two extremes: $n / k$ or 0.

Recall, in the construction of $\eta$ we rescale the metric such that $\tau$ ranges from $[1, T]$. Note that $T$ is determined by $\beta_{1}$. By Proposition 4.1, we may also rescale the metric such that $\tau$ ranges from $[t, 1]$ for some $0<t<1$. In such a way, we construct another family of Kähler-Einstein edge metrics on $\mathbb{F}_{n, k}$ parametrized by $\beta_{2}$ in the remainder of this section. Such metrics can be seen as obtained after renormalizing metrics in the family that is parametrized by $\beta_{1}$. However, when studying their asymptotic behaviors they give rise to different limit metric.

\subsection*{4.2 Constructions of $\xi_{\beta_{2}}$ on $\mathbb{F}_{n, k}$}

Now consider a change of coordinate $u:=1 / w$. Then (3.1) can be written as
$$s=-\log |u|^{2}+k \log \left(1+\sum_{j \neq i}^{n}\left|z_{j}\right|^{2}\right) .$$

We still denote by $f(s)$ a smooth function on $\mathbb{F}_{n, k}$ and seek Kähler-Einstein edge metrics that have the form $\sqrt{-1} \partial \bar{\partial} f(s)$. Recall $\tau(s)$ and $\varphi(s)$ are defined in (4.1). Let
$$\begin{aligned}
\xi: & =\sqrt{-1} \partial \bar{\partial} f(s) \\
& =k \tau \pi_{1}^{*} \omega_{\mathrm{FS}}+\varphi\left(\pi_{2}^{*} \omega_{\mathrm{Cyl}}+\sqrt{-1} \alpha \wedge \bar{\alpha}-\right. \\
& \left.\sqrt{-1} \alpha \wedge \frac{\mathrm{~d} \bar{u}}{\bar{u}}-\sqrt{-1} \frac{\mathrm{~d} u}{u} \wedge \bar{\alpha}\right),
\end{aligned}$$
where $\pi_{1}, \pi_{2}$ and $\alpha$ are the same as those in (4.2). Recall by Proposition 4.1,
$$0<\inf _{s \in \mathbb{R}} \tau(s)<\sup _{s \in \mathbb{R}} \tau(s)<+\infty .$$
We rescale the potential function $f$ such that for some $t>0$,
$$\sup _{s \in \mathbb{R}} \tau(s)=1, \quad \inf _{s \in \mathbb{R}} \tau(s)=t .$$
Assume $\xi$ is a Kähler edge metric on $\mathbb{F}_{n, k}$. Then, under the renormalization given by (4.15), Proposition 4.2 and Proposition 4.4, which respectively describe the boundary conditions for $\varphi$ and the ODE satisfied by $\varphi$, translate to the following two Propositions.

Proposition 4.5. Assume $\xi$ has edge singularities of angle $2 \pi \beta_{1}$ and $2 \pi \beta_{2}$ respectively along $Z_{n, k}$ and $Z_{n,-k}$. Recall $\varphi$ in (4.14). Then,
$$\begin{array}{ll}
\varphi(t)=0, & \frac{d \varphi}{d \tau}(t)=\beta_{1}, \\
\varphi(1)=0, & \frac{d \varphi}{d \tau}(1)=-\beta_{2} .
\end{array}$$

Proposition 4.6. Under the same assumptions in Proposition 4.5, the Kähler edge metric $\xi$ satisfies the Kähler-Einstein edge equation if and only if
$$\begin{aligned}
& \mu=\frac{n}{k}+\beta_{2}, \quad \beta_{2} \in\left(0, \frac{1}{k}\right), \\
& \varphi(\tau)=\frac{1}{k} \frac{\tau^{n}-1}{\tau^{n-1}}-\frac{1}{n+1}\left(\frac{n}{k}+\beta_{2}\right) \frac{\tau^{n+1}-1}{\tau^{n-1}}, \quad \tau \in(t, 1),
\end{aligned}$$
where by $\mu$ we denote the Ricci curvature of $\xi$. Moreover, $\beta_{1}$ and $t$ are determined by $\beta_{2}$.
By Propositions 4.5 and 4.6, we realize that given $\beta_{2}$ we can construct a family of Kähler-Einstein edge metrics on $\mathbb{F}_{n, k}$ parametrized by $\beta_{2}$ such that $\beta_{1}$ and $t$ are determined by $\beta_{2}$. This family of metrics can be obtained by renormalizing the family of metrics parametrized by $\beta_{1}$.

\section*{5 Angle asymptotics}

In this section, we study the asymptotic behaviors of Kähler-Einstein edge metrics $\eta$ in (4.2) (respectively, $\xi$ in (4.14)) as $\beta_{1}$ (respectively, $\beta_{2}$ ) approaches either of its extremes.

We first study the limit behavior of $\eta$ when $\beta_{1} \nearrow n / k$. It is enough to study the limiting behavior of $\varphi$ and $\tau$ thanks to Proposition 4.4.

Proposition 5.1. When $\beta_{1}$ is close to $n / k$, we have $T>1$ and $T \rightarrow \infty$ as $\beta_{1} \nearrow n / k$.

Proof. Recall by (4.5), 1 and $T$ are both roots of $\varphi(\tau)$. By Proposition 4.4, $T>1$. To prove $T \rightarrow \infty$ as $\beta_{1} \nearrow n / k$, we write (4.8) as
$$\varphi(\tau)=\frac{1}{\tau^{n-1}} \cdot \frac{1}{n+1}\left(\beta_{1}-\frac{n}{k}\right)(\tau-1)\left(\tau-\alpha_{1}\right) \cdots\left(\tau-\alpha_{n-1}\right)(\tau-T),$$
where $\alpha_{1}, \ldots, \alpha_{n-1} \in \mathbb{C}$. Comparing (4.8) to (5.1), we have
$$\left(\tau-\alpha_{1}\right) \cdots\left(\tau-\alpha_{n-1}\right)(\tau-T)=\tau^{n}+\frac{1+k \beta_{1}}{k \beta_{1}-n}\left(\tau^{n-1}+\cdots+1\right) .$$
By Vieta's formulas,
$$\begin{aligned}
(-1)^{n} \alpha_{1} \cdots \alpha_{n-1} \cdot T & =\frac{1+k \beta_{1}}{k \beta_{1}-n}, \\
\alpha_{1}+\cdots+\alpha_{n-1}+T & =\frac{1+k \beta_{1}}{n-k \beta_{1}} .
\end{aligned}$$

By (4.8), $\varphi(\tau)$ has $n+1$ (possibly complex) roots. Since
$$\varphi(\tau) \rightarrow \frac{1}{k} \frac{\tau^{n}-1}{\tau^{n-1}}, \quad \text { as } \beta_{1} \nearrow n / k,$$
we conclude that the $n$ roots of $\varphi$ except $T$ converge to the $n$th root of unity as $\beta_{1} \nearrow n / k$. In particular, $\left|\alpha_{1}\right|, \ldots,\left|\alpha_{n-1}\right|$ converge to 1 as $\beta_{1} \nearrow n / k$. However, by (5.2) we see
$$\left|\alpha_{1}\right| \cdots\left|\alpha_{n-1}\right||T| \rightarrow+\infty, \quad \text { as } \beta_{1} \nearrow n / k .$$
Thus we must have $T \rightarrow+\infty$ as $\beta_{1} \nearrow n / k$. \(\square\)

Proposition 5.2. As $\beta_{1} \nearrow n / k$, the length of the path on each fiber between the intersection point of the fiber with $Z_{n, k}$ and that of the fiber with $Z_{n,-k}$ tends to infinity. In other words, $Z_{n,-k}$ gets pushed-off to infinity as $\beta_{1} \nearrow n / k$ if we fix a base point on $Z_{n, k}$.

Proof. Restricted to each fiber, by (4.4), $\eta=\varphi \sqrt{-1} \mathrm{~d} w \wedge \mathrm{~d} \bar{w} /|w|^{2}$ gives a metric
$$g=\frac{1}{2 \varphi(\tau)} \mathrm{d} \tau^{2}+2 \varphi(\tau) \mathrm{d} \theta^{2} .$$
Up to some constant, the distance between $\{\tau=1\}$ and $\{\tau=T\}$ is given by
$$\begin{aligned}
& \int_{1}^{T} \frac{1}{\sqrt{\varphi(\tau)}} \mathrm{d} \tau= \\
& \int_{1}^{T} \frac{\tau^{\frac{n-1}{2}}}{\sqrt{\frac{n / k-\beta_{1}}{n+1}} \cdot \sqrt{(\tau-1)\left(\tau-\alpha_{1}\right) \cdots\left(\tau-\alpha_{n-1}\right)(T-\tau)}} \mathrm{d} \tau .
\end{aligned}$$
Recall in the proof of Proposition 5.1, we have shown
$$T \sim \frac{1+k \beta_{1}}{n-k \beta_{1}} \sim \frac{1+n}{k} \cdot \frac{1}{n / k-\beta_{1}}, \quad \text { as } \beta_{1} \nearrow n / k .$$
For any fixed $\epsilon>0$, consider
$$\int_{T-\epsilon}^{T} \frac{\tau^{\frac{n-1}{2}}}{\sqrt{\frac{n / k-\beta_{1}}{n+1}} \cdot \sqrt{(\tau-1)\left(\tau-\alpha_{1}\right) \cdots\left(\tau-\alpha_{n-1}\right)(T-\tau)}} \mathrm{d} \tau .$$

We can find $\beta_{1}$ close to $n / k$ such that
$$T-\epsilon>\frac{1}{2} T .$$
Then in $[T-\epsilon, T]$, we have
$$\begin{aligned}
& \tau^{\frac{n-1}{2}}>(T-\epsilon)^{\frac{n-1}{2}}>\left(\frac{1}{2} T\right)^{\frac{n-1}{2}}, \\
& \sqrt{(\tau-1)\left(\tau-\alpha_{1}\right) \cdots\left(\tau-\alpha_{n-1}\right)}<\sqrt{2\left(\tau^{n}-1\right)}<\sqrt{2 T^{n}} .
\end{aligned}$$
By (5.5) and (5.6), there exists a constant $C>0$ that is independent of $\epsilon$ such that
$$\begin{aligned}
& \int_{T-\epsilon}^{T} \frac{\tau^{\frac{n-1}{2}}}{\sqrt{\frac{n / k-\beta_{1}}{n+1}} \cdot \sqrt{(\tau-1)\left(\tau-\alpha_{1}\right) \cdots\left(\tau-\alpha_{n-1}\right)(T-\tau)}} \mathrm{d} \tau \\
& >C \cdot \frac{T^{\frac{n-1}{2}}}{\sqrt{n / k-\beta_{1}} \cdot T^{\frac{n}{2}}} \int_{T-\epsilon}^{T} \frac{1}{\sqrt{T-\tau}} \mathrm{d} \tau \\
& >C \epsilon .
\end{aligned}$$
Since $\epsilon$ is arbitrarily chosen, the integral in (5.4) diverges as $\beta_{1} \nearrow n / k$. Thus, we have shown $Z_{n,-k}$ gets pushed-off to infinity as $\beta_{1} \nearrow n / k$ if we choose a base point on $Z_{n, k}$. \(\square\)

Proposition 5.3. $\lim _{\beta_{1} \nearrow \frac{n}{k}} \beta_{2}\left(\beta_{1}\right)=\frac{1}{k}$.
Proof. We calculate
$$\frac{\mathrm{d} \varphi}{\mathrm{~d} \tau}=\frac{1}{k} \frac{\tau^{n-2}}{\left(\tau^{n-1}\right)^{2}}\left(n+\tau^{n}-1\right)+\frac{1}{n+1}\left(\beta_{1}-\frac{n}{k}\right) \frac{\tau^{n-2}}{\left(\tau^{n-1}\right)^{2}}\left(2 \tau^{n+1}+n-1\right) .$$
By $\varphi_{\tau}(T)=-\beta_{2}$ we have
$$\frac{1}{k T^{n}}\left(n+T^{n}-1\right)+\frac{1}{n+1}\left(\beta_{1}-\frac{n}{k}\right) \frac{1}{T^{n}}\left(2 T^{n+1}+n-1\right)=-\beta_{2} .$$
Recall $\varphi(T)=0$, then we have
$$\frac{T^{n}-1}{k}+\frac{1}{n+1}\left(\beta_{1}-\frac{n}{k}\right)\left(T^{n+1}-1\right)=0 .$$
Combining (5.7) and (5.8),
$$\left(\frac{1}{k}-\beta_{2}\right) T^{n}=\beta_{1}+\frac{1}{k} .$$
Since $T \rightarrow \infty$ as $\beta_{1} \nearrow n / k$, there holds $\beta_{2} \rightarrow 1 / k$ as $\beta_{1} \nearrow n / k$. \(\square\)

In Section 6, we use asymptotic behaviors discussed above to study the limit metric of $\eta$ as $\beta_{1}$ approaches $n / k$ or 0 . In the remainder of this section, we focus on the family of metrics $\xi$ that is parametrized by $\beta_{2}$. Inspired by Proposition 5.3, we study the asymptotic behaviors of $\xi$ as $\beta_{2} \nearrow 1 / k$.

Proposition 5.4. When $\beta_{2} \nearrow \frac{1}{k}$, as an analogue of (5.9), there holds
$$\left(\frac{1}{k}+\beta_{1}\right) t^{n}=\frac{1}{k}-\beta_{2} .$$
Proof. Let $\varphi(\tau)$ and $t$ be as in (4.16) and (4.17). We calculate
$$\frac{\mathrm{d} \varphi}{\mathrm{~d} \tau}=\frac{1}{k} \frac{\tau^{n-2}}{\left(\tau^{n-1}\right)^{2}}\left(\tau^{n}+n-1\right)-\frac{1}{n+1}\left(\frac{n}{k}+\beta_{2}\right) \frac{\tau^{n-2}}{\left(\tau^{n-1}\right)^{2}}\left(2 \tau^{n+1}+n-1\right) .$$
By the fact that $\mathrm{d} \varphi / \mathrm{d} \tau(t)=\beta_{1}$,
$$\beta_{1}=\frac{1}{k t^{n}}\left(n+t^{n}-1\right)-\frac{1}{n+1}\left(\frac{n}{k}+\beta_{2}\right) \frac{1}{t^{n}}\left(2 t^{n+1}+n-1\right) .$$
Combining this with the fact that $\varphi(t)=0$, there holds
$$\begin{aligned}
\beta_{1} t^{n} & =\frac{1}{k}\left(n+t^{n}-1\right)-\frac{2\left(t^{n}-1\right)}{k}-\frac{n}{k}-\beta_{2} \\
& =-\frac{1}{k} t^{n}+\frac{1}{k}-\beta_{2},
\end{aligned}$$
which implies
$$\left(\beta_{1}+\frac{1}{k}\right) t^{n}=\frac{1}{k}-\beta_{2}$$
as claimed. \(\square\)

Proposition 5.5. As $\beta_{2} \nearrow \frac{1}{k}, t=O\left(\left(\frac{k}{n+1}\right)^{\frac{1}{n}}\left(\frac{1}{k}-\beta_{2}\right)^{\frac{1}{n}}\right)$. In particular, $t$ tends to 0 when $\beta_{2} \nearrow 1 / k$. Moreover, the length of the path on each fiber between the intersection point of the fiber with $Z_{n, k}$ and that of the fiber with $Z_{n,-k}$ converges to a finite number as $\beta_{2} \nearrow 1 / k$.

Proof. Recall $t$ is a root of
$$\varphi(\tau)=\frac{1}{k} \frac{\tau^{n}-1}{\tau^{n-1}}-\frac{1}{n+1}\left(\frac{n}{k}+\beta_{2}\right) \frac{\tau^{n+1}-1}{\tau^{n-1}}=0 .$$
Direct calculations yield
$$\frac{\varphi(\tau)}{\tau-1}=\frac{1}{\tau^{n-1}}\left(-\frac{1}{n+1}\left(\frac{n}{k}+\beta_{2}\right) \tau^{n}+\frac{1 / k-\beta_{2}}{n+1}\left(\tau^{n-1}+\cdots+\tau+1\right)\right) .$$
Then it is easy to see that every root of $\varphi(\tau)$ except for $\tau=1$, denoted by $\alpha$, satisfies that $|\alpha|=O\left((k /(n+1))^{1 / n}\left(1 / k-\beta_{2}\right)^{1 / n}\right)$ when $\beta_{2} \nearrow 1 / k$. In particular, as $\beta_{2} \nearrow 1 / k$, all roots of $\varphi(\tau)=0$ except for $\tau=1$ converge to 0 . We conclude that $t \rightarrow 0$. To see that the length between $Z_{n, k}$ and $Z_{n,-k}$ converges to a finite number in the limit, one follows the arguments in the proof of Proposition 5.2 and Proposition C.4. \(\square\)

\section*{6 Large angle limits}

In this section, we first study the Gromov-Hausdorff limit of the family of metrics $\eta$ when the parameter $\beta_{1}$ approaches $n / k$.

Theorem 6.1. Fix an arbitrary base point $p$ on $Z_{n, k}$. As $\beta_{1} \nearrow n / k$, the Kähler-Einstein edge metric $\left(\mathbb{F}_{n, k}, \eta_{\beta_{1}}, p\right)$ converges in the pointed Gromov-Hausdorff sense to a Ricci-flat Kähler edge metric $\left(-k H_{\mathbb{P}^{n-1}}, \eta_{\infty}, p\right)$ described in (6.5). Moreover, away from $Z_{n, k}$, one has $\eta_{\beta_{1}} \xrightarrow{C_{\text {loc }}^{k}}$ $\eta_{\infty}$ for any $k \geq 0$ on the total space of $-k H_{\mathbb{P}^{n-1}}$ (seen as an open subset in $\mathbb{F}_{n, k}$ ), and the limit metric $\eta_{\infty}$ coincides with the model metric $\omega_{\mathrm{eh}, n, k}$ defined in Section 3.

Proof. We use notation $\eta_{\beta_{1}}, \tau\left(\beta_{1}\right)$ and $\varphi\left(\beta_{1}\right)$ to emphasize the dependence of metrics and coordinates on $\beta_{1}$. Combining (4.1) and (4.8), we have
$$\frac{\mathrm{d} s}{\mathrm{~d} \tau\left(\beta_{1}\right)}=\frac{1}{\varphi\left(\beta_{1}\right)}=\frac{\tau\left(\beta_{1}\right)^{n-1}}{\frac{1}{k}\left(\tau\left(\beta_{1}\right)^{n}-1\right)+\frac{\beta_{1}-n / k}{n+1}\left(\tau\left(\beta_{1}\right)^{n+1}-1\right)} .$$

Claim 6.2. The pointwise limits of functions
$$\begin{array}{ll}
\tau_{\infty}(s):= & \lim _{\beta_{1} \nearrow n / k} \tau\left(\beta_{1}, s\right), \\
\varphi_{\infty}(s):= & \lim _{\beta_{1} \nearrow n / k} \varphi\left(\beta_{1}, s\right), \\
& s \in(-\infty,+\infty),
\end{array}$$
exist. Moreover, $\tau_{\infty}(s)$ and $\varphi_{\infty}(s)$ are smooth in $s$.
Proof of the Claim. By the continuous dependence of ODEs in (6.1) on the parameter $\beta_{1}$, the pointwise limit function $\tau_{\infty}$ exists. Since $\tau\left(\beta_{1}, s\right)$ is smooth in $s$ for each $\beta_{1}, \tau_{\infty}(s)$ is smooth in $s$. By (4.8) and the existence of $\tau_{\infty}(s), \varphi_{\infty}(s)$ also exists. Moreover, $\varphi_{\infty}(s)$ is smooth in $s$ due to the smoothness of $\tau_{\infty}(s)$. \(\square\)

Thanks to Claim 6.2, $\tau_{\infty}$ and $\varphi_{\infty}$ satisfy
$$\begin{aligned}
\frac{\mathrm{d} s}{\mathrm{~d} \tau_{\infty}} & =\frac{\tau_{\infty}^{n-1}}{\frac{1}{k}\left(\tau_{\infty}^{n}-1\right)}, \\
\varphi_{\infty}\left(\tau_{\infty}\right) & =\frac{1}{k} \frac{\tau_{\infty}^{n}-1}{\tau_{\infty}^{n-1}} .
\end{aligned}$$
Solving the first equation in (6.2), we get
$$\tau_{\infty}(s)=\left(1+e^{(s-C) \frac{n}{k}}\right)^{1 / n}, \quad \text { for some constant } C .$$
By considering a change of coordinate $w^{\prime}=C^{\prime} w$ for some appropriate $C^{\prime}$ in (3.1), we may choose $C$ in (6.3) to be 0 . Plugging (6.3) into the second equation in (6.2), one finds
$$\varphi_{\infty}(s)=\frac{1}{k} \cdot \frac{e^{s \cdot \frac{n}{k}}}{\left(e^{s \cdot \frac{n}{k}}+1\right)^{\frac{n-1}{n}}} .$$

Plugging (6.3) and (6.4) into (4.2), we obtain the convergence of Kähler-Einstein edge metric $\eta_{\beta_{1}}$ on any compact subsets of $\mathbb{F}_{n, k}$ in every $C^{k}$-norm to the following metric:
$$\begin{aligned}
\eta_{\infty}: & =\lim _{\beta_{1} \nearrow n / k} \eta_{\beta_{1}} \\
& =k\left(1+e^{s \cdot \frac{n}{k}}\right)^{1 / n} \pi_{1}^{*} \omega_{\mathrm{FS}}+\frac{1}{k} \cdot \frac{e^{s \cdot \frac{n}{k}}}{\left(e^{s \cdot \frac{n}{k}}+1\right)^{\frac{n-1}{n}}}\left(\pi_{2}^{*} \omega_{\mathrm{Cyl}}+\sqrt{-1} \alpha \wedge \bar{\alpha}\right. \\
& \left.+\sqrt{-1} \alpha \wedge \frac{\mathrm{~d} \bar{w}}{\bar{w}}+\sqrt{-1} \frac{\mathrm{~d} w}{w} \wedge \bar{\alpha}\right) .
\end{aligned}$$
Recall by (4.7), the Ricci curvature of $\eta_{\beta_{1}}$ is given by $\lambda_{\beta_{1}}=n / k-\beta_{1}$, which converges to 0 as $\beta_{1} \nearrow n / k$. Thus, $\eta_{\infty}$ is a Ricci-flat Kähler edge metric on $-k H_{\mathbb{P}^{n-1}} . \eta_{\infty}$ has edge singularity of angle $2 n \pi / k$ along $Z_{n, k} \subset-k H_{\mathbb{P}^{n-1}}$. Indeed, $\eta_{\infty}$ coincides with the model metric $\omega_{\mathrm{eh}, n, k}$ defined in Section 3. To obtain the convergence in the pointed Gromov-Hausdorff sense, we first recall by Proposition 5.2 the distance between $Z_{n,-k}$ and $Z_{n, k}$ tends to infinity as $\beta_{1} \nearrow n / k$. Once we choose a base point on $Z_{n, k}$. Since $\eta_{\beta_{1}}$ converges to $\eta_{\infty}$ on any compact geodesic balls centered at the base point, we conclude that $\eta_{\beta_{1}}$ converges in the pointed Gromov-Hausdorff sense to $\eta_{\infty}$ on $-k H_{\mathbb{P}^{n-1}}$. \(\square\)

Remark 6.3. If we let $n=k=2$ in Theorem 6.1, then by Remark 3.3 we obtain in the limit the Eguchi-Hanson metric with parameter $\epsilon$ set as 1 (see (A.11)). In other words, the Eguchi-Hanson metric arises as the pointed Gromov-Hausdorff limit of Kähler-Einstein edge metrics $\eta_{\beta_{1}}$ when $\beta_{1} \nearrow 1$. This interesting observation has been conjectured in our previous work [14, Remark 5.1] and provided some of the motivation for the present article.

Next, we fix a base point on the infinity section $Z_{n,-k}$ to study the Gromov-Hausdorff limit of the family of Kähler-Einstein edge metrics $\xi$ on $\mathbb{F}_{n, k}$. In the limit, we obtain an orbifold Kähler-Einstein edge metric instead of the Ricci-flat edge metric obtained in Theorem 6.1.

From now on, we use $\xi_{\beta_{2}}, \tau\left(\beta_{2}\right)$ and $\varphi\left(\beta_{2}\right)$ to emphasize the dependence of metrics and coordinates on $\beta_{2}$. We consider the case $\beta_{2} \nearrow 1 / k$.

Theorem 6.4. Fix an arbitrary base point $p$ on the infinity section $Z_{n,-k}$. As $\beta_{2} \nearrow 1 / k$, the Kähler-Einstein edge metric $\left(\mathbb{F}_{n, k}, \xi_{\beta_{2}}, p\right)$ on $\mathbb{F}_{n, k}$ converges in the pointed Gromov-Hausdorff sense to an orbifold Kähler-Einstein edge metric $\left(\mathbb{P}^{n}(1, \ldots, 1, k), \xi_{\infty}, p\right)$ on the weighted projective space $\mathbb{P}^{n}(1, \ldots, 1, k)$ with an edge singularity of angle $2 \pi / k$ along $Z_{n,-k}$. This limit metric coincides with the model metric $\omega_{\text {orb }, n, k}$ defined in Definition 3.7.

Proof. By similar notation and calculations as in the proof of Theorem 6.1, we have
$$\frac{\mathrm{d} s}{\mathrm{~d} \tau\left(\beta_{2}\right)}=\frac{1}{\varphi\left(\beta_{2}\right)}=\frac{\tau\left(\beta_{2}\right)^{n-1}}{\frac{1}{k}\left(\tau\left(\beta_{2}\right)^{n}-1\right)-\frac{n / k+\beta_{2}}{n+1}\left(\tau\left(\beta_{2}\right)^{n+1}-1\right)} .$$
As $\beta_{2} \nearrow 1 / k$, we have
$$\begin{aligned}
\frac{\mathrm{d} s}{\mathrm{~d} \tau_{\infty}} & =\frac{k}{\tau_{\infty}-\tau_{\infty}^{2}}, \\
\varphi_{\infty}\left(\tau_{\infty}\right) & =\frac{1}{k}\left(\tau_{\infty}-\tau_{\infty}^{2}\right) .
\end{aligned}$$

Solving (6.6) and considering a change of coordinate $u^{\prime}=C^{\prime} u$ for some appropriate $C$, we have
$$\begin{aligned}
\tau_{\infty}(s) & =1-\frac{1}{e^{\frac{s}{k}}+1}, \quad s \in(-\infty,+\infty), \\
\varphi_{\infty}(s) & =\frac{1}{k} \frac{e^{s / k}}{\left(e^{s / k}+1\right)^{2}}, \quad s \in(-\infty,+\infty) .
\end{aligned}$$
Thus, the limit metric on $\mathbb{F}_{n, k}$ is as follows:
$$\begin{aligned}
\tilde{\xi}_{\infty} & =k \frac{e^{s / k}}{e^{s / k}+1} \pi_{1}^{*} \omega_{\mathrm{FS}}+\frac{1}{k} \frac{e^{s / k}}{\left(e^{s / k}+1\right)^{2}}\left(\pi_{2}^{*} \omega_{\mathrm{Cyl}}+\sqrt{-1} \alpha \wedge \bar{\alpha}\right. \\
& \left.+\sqrt{-1} \alpha \wedge \frac{\mathrm{~d} \bar{w}}{\bar{w}}+\sqrt{-1} \frac{\mathrm{~d} w}{w} \wedge \bar{\alpha}\right) .
\end{aligned}$$
Recall the Ricci curvature $\mu_{\beta_{2}}$ is given in (4.17) by $n / k+\beta_{2}$ and converges to $(n+1) / k$ in the limit. Thus $\tilde{\xi}_{\infty}$ has Ricci curvature $(n+1) / k$. Moreover, $\tilde{\xi}_{\infty}$ has an edge singularity of angle $2 \pi / k$ along $Z_{n,-k}$. It degenerates on $Z_{n, k}$ since $\tau \equiv 0$ on $Z_{n, k}$. Indeed, $\tilde{\xi}_{\infty}$ coincides with the model metrics defined in Definition 3.6. Then by Definition 3.7, we denote by $\xi_{\infty}$ the model metric on $\mathbb{P}^{n}(1, \ldots, 1, k)$ that is the pull-back of $\tilde{\xi}_{\infty}$ under the blow up map.

We have shown that $\tilde{\xi}_{\infty}$ is the limit of $\xi_{\beta_{2}}$ as tensors in the pointwise smooth sense. Next, fix an arbitrary base point on $Z_{n,-k}$. By Proposition 5.5 and the local smooth convergence result, we conclude that $\left(\mathbb{P}^{n}(1, \ldots, 1, k), \xi_{\infty}\right)$ is the limit of $\left(\mathbb{F}_{n, k}, \xi_{\beta_{2}}\right)$ in the pointed Gromov-Hausdorff sense when $\beta_{2} \nearrow 1 / k$. Moreover, the limit metric coincides with the model metric $\omega_{\text {orb, } n, k}$ defined in Section 3. \(\square\)

As we pointed out in Section 5, the family of metrics $\xi_{\beta_{2}}$ can be obtained by renormalizing the family of metrics $\eta_{\beta_{1}}$. Comparing Theorem 6.1 to Theorem 6.4, we obtain different limit metrics for those two family of metrics. However, we show that after a proper normalization of $\xi_{\beta_{2}}$, we obtain the same limit metric for both $\xi_{\beta_{2}}$ and $\eta_{\beta_{1}}$. The normalization factor is actually given by Proposition 5.5.
Corollary 6.5. Rescale the Kähler-Einstein edge metric $\xi_{\beta_{2}}$ by $((n+1) / k)^{1 / n} /\left(1 / k-\beta_{2}\right)^{1 / n}$, then the normalized metric converges in the pointed Gromov-Hausdorff sense to a Ricci-flat metric on $-k H_{\mathbb{P}^{n-1}}$ when $\beta_{2} \nearrow 1 / k$, where the base point is chosen from $Z_{n, k}$. See the proof for a more precise explanation. Moreover, this Ricci-flat metric coincides with the one obtained in Theorem 6.1, i.e., the model metric $\omega_{\mathrm{eh}, n, k}$.

Proof. Consider a change of coordinate
$$y\left(\beta_{2}\right):=\left(\frac{n+1}{k}\right)^{\frac{1}{n}} \cdot \frac{\tau\left(\beta_{2}\right)}{\left(\frac{1}{k}-\beta_{2}\right)^{\frac{1}{n}}} .$$
By Proposition 5.5, the interval of definition of $y\left(\beta_{2}\right)$ converges to $[1,+\infty]$ as $\beta_{2} \nearrow 1 / k$. The rescaled metric reads
$$\begin{aligned}
& \left(\frac{n+1}{k}\right)^{\frac{1}{n}} \cdot \frac{\xi_{\beta_{2}}}{\left(\frac{1}{k}-\beta_{2}\right)^{\frac{1}{n}}} \\
& =k y \pi_{1}^{*} \omega_{\mathrm{FS}}+\left(\frac{n+1}{k}\right)^{\frac{1}{n}} \cdot \frac{\varphi\left(\beta_{2}\right)}{\left(\frac{1}{k}-\beta_{2}\right)^{\frac{1}{n}}}\left(\pi_{2}^{*} \omega_{\mathrm{Cyl}}+\sqrt{-1} \alpha \wedge \bar{\alpha}-\right. \\
& \left.\sqrt{-1} \alpha \wedge \frac{\mathrm{~d} \bar{u}}{\bar{u}}-\sqrt{-1} \frac{\mathrm{~d} u}{u} \wedge \bar{\alpha}\right) .
\end{aligned}$$

Recall
$$\begin{aligned}
& \left(\frac{n+1}{k}\right)^{\frac{1}{n}} \cdot \frac{\varphi\left(\beta_{2}\right)}{\left(\frac{1}{k}-\beta_{2}\right)^{\frac{1}{n}}}= \\
& \left(\frac{n+1}{k}\right)^{\frac{1}{n}} \cdot \frac{\frac{1}{k}\left(\tau\left(\beta_{2}\right)^{n}-1\right)-\frac{1}{n+1}\left(\frac{n}{k}+\beta_{2}\right)\left(\tau\left(\beta_{2}\right)^{n+1}-1\right)}{\left(\tau\left(\beta_{2}\right)^{n-1}\right)\left(\frac{1}{k}-\beta_{2}\right)^{\frac{1}{n}}} .
\end{aligned}$$
Denote by $y$ the coordinate in the limit. Letting $\beta_{2} \nearrow 1 / k$, the right hand side of (6.7) converges to
$$\frac{y^{n}-1}{k y^{n-1}}, \quad y \in[1,+\infty] .$$
Solving
$$\frac{\mathrm{d} s}{\mathrm{~d} \tau_{\beta_{2}}}=\frac{1}{\varphi_{\beta_{2}}\left(\tau_{\beta_{2}}\right)} \Rightarrow \frac{\mathrm{d} s}{\mathrm{~d} y_{\beta_{2}}} \frac{1}{\left(\frac{1}{k}-\beta_{2}\right)^{\frac{1}{n}}} \cdot\left(\frac{n+1}{k}\right)^{\frac{1}{n}}=\frac{1}{\varphi_{\beta_{2}}\left(y_{\beta_{2}}\right)},$$
we obtain in the limit
$$s=\frac{k}{n} \log \left(y^{n}-1\right), \quad y \in(1,+\infty) .$$
Thus the limit metric is given by
$$\begin{aligned}
\tilde{\xi}_{\infty}=k y \pi_{1}^{*} \omega_{\mathrm{FS}}+\frac{y^{n}-1}{k y^{n-1}}( & \pi_{2}^{*} \omega_{\mathrm{Cyl}}+\sqrt{-1} \alpha \wedge \bar{\alpha}- \\
& \left.\sqrt{-1} \alpha \wedge \frac{\mathrm{~d} \bar{u}}{\bar{u}}-\sqrt{-1} \frac{\mathrm{~d} u}{u} \wedge \bar{\alpha}\right),
\end{aligned}$$
where $y$ and $s$ satisfy (6.8). This limit metric is Ricci-flat. And it coincides with the limit metric in Theorem 6.1, i.e., the model metric $\omega_{\mathrm{eh}, n, k}$ defined in Section 3. Fix an arbitrary base point on $Z_{n, k}$. By Proposition 5.5, the distance between $Z_{n, k}$ and $Z_{n,-k}$ tends to $+\infty$ in the limit under the renormalized metric. Thus, $Z_{n,-k}$ gets pushed-off to infinity in the limit. We obtain the pointed Gromov-Hausdorff convergence of $\left(\mathbb{F}_{n, k},((n+1) / k)^{1 / n} \xi_{\beta_{2}} /\left(\frac{1}{k}-\beta_{2}\right)^{1 / n}\right)$ to $-k H_{\mathbb{P}^{n-1}}$ with the metric obtained in (6.9). \(\square\)

\section*{7 Small angle limits and fiberwise rescaling}

In this section we first consider the $\beta_{1} \searrow 0$ case for $\eta_{\beta_{1}}$.
Theorem 7.1. As $\beta_{1}$ tends to $0,\left(\mathbb{F}_{n, k}, \eta_{\beta_{1}}\right)$ converges in the Gromov-Hausdorff sense to $\left(\mathbb{P}^{n-1}, k \omega_{\mathrm{FS}}\right)$.

Proof. As $\beta_{1} \searrow 0$, by (4.8) we have
$$\begin{aligned}
\varphi_{0}:=\lim _{\beta_{1} \searrow 0} \varphi_{\beta_{1}} & =\frac{1}{\tau^{n-1}}\left(\frac{1}{k}\left(\tau^{n}-1\right)-\frac{n}{k(n+1)}\left(\tau^{n+1}-1\right)\right) \\
& =\frac{1}{k(n+1)} \cdot \frac{1}{\tau^{n-1}}\left(-n \tau^{n+1}+(n+1) \tau^{n}-1\right) .
\end{aligned}$$
Then we observe $\varphi_{0}$ does not have any root greater than 1. Indeed, notice that
$$\begin{aligned}
-n \tau^{n+1}+(n+1) \tau^{n}-1 & =(\tau-1)\left(1+\cdots+\tau^{n-1}-n \tau^{n}\right) \\
& =(\tau-1)\left(1-\tau^{n}+\tau-\tau^{n}+\cdots+\tau^{n-1}-\tau^{n}\right) .
\end{aligned}$$

Thus $\varphi_{0}$ is always positive when $\tau>1$. However, combining this fact with (5.1), we conclude that
$$\lim _{\beta_{1} \searrow 0} T=1 .$$
Since $\varphi(1)=\varphi(T)=0$, we have $\varphi\left(\beta_{1}\right) \rightarrow 0$ as $\beta_{1} \searrow 0$. Since $\tau$ ranges from 1 to $T$, by (4.2) we conclude that as $\beta_{1} \searrow 0, \eta_{\beta_{1}}$ converges to $k \pi_{1}^{*} \omega_{\mathrm{FS}}$. Thus we have shown $\left(\mathbb{F}_{n, k}, \eta_{\beta_{1}}\right)$ converges in the Gromov-Hausdorff sense to $\left(\mathbb{P}^{n-1}, k \omega_{\mathrm{FS}}\right)$ when $\beta_{1} \searrow 0$. \(\square\)

Roughly speaking, Theorem 7.1 says that as $\beta_{1} \searrow 0$, the fibers collapse to the zero section. This motivates us to rescale the metric $\eta_{\beta_{1}}$ along the fiber so that we can obtain a non-collapsed metric in the limit. We first need the following lemma.
---
retention_scope: session
part: 1
total_parts: 1
---

---
source_file: 1308_4307v1.pdf
converter: mathpix
format: mmd
---

\title{
EXISTENCE OF WEAK CONICAL KÄHLER-EINSTEIN METRICS ALONG SMOOTH HYPERSURFACES
}

\author{
CHENGJIAN YAO
}

\begin{abstract}
The existence of weak conical Kähler-Einstein metrics along smooth hypersurfaces with angle between 0 and $2 \pi$ is obtained by studying a smooth continuity method and a local Moser's iteration technique. In the case of negative and zero Ricci curvature, the $C^{0}$ estimate is unobstructed; while in the case of positive Ricci curvature, the $C^{0}$ estimate obstructed by the properness of the twisted K-Energy. As soon as the $C^{0}$ estimate is achieved, the local Moser iteration could improve the rough bound on the approximations to a uniform $C^{2}$ bound , thus produce a weak conical Kähler-Einstein metric. The method used here do not depend on the bound of any background conical Kähler metrics.
\end{abstract}

\section*{1. Introduction}

The existence of smooth Kähler-Einstein metrics with negative Ricci curvature is solved independently by Aubin and Yau, and Ricci-flat case by Yau in his celebrated work on the Calabi's conjecture. In the last part of the paper of Yau [15], complex Monge-Ampère equation with degenerate and meromorphic right hand side was also considered. For the conical Kähler-Einstein metrics, the Riemann surfaces situation was well studied by Troyanov [14] and McOwen [10]. The high dimensional was considered by Tian in [13]. And in recent years, partly motivated by Donaldson's project of using conical Käher-Einstein metrics as a continuity method of solving smooth Kähler-Einstein problem on Fano manifolds, lots of results along this line have been achieved, see [2], [7], and [8]. Quite recently, Chen, Donaldson and Sun [3],[4],[5] proved the smooth Yau-Tian-Donaldson conjecture in Fano case, where conical Kähler-Einstein metrics are used as a main ingredient. The existence of conical Kähler-Einstein metrics still has its own interest in studying more general compact Kähler manifolds.

The aim of this paper is to study the existence of weak conical Kähler-Einstein metrics with conical singularities along smooth hypersurfaces. By saying a weak conical Kähler-Einstein metric $\omega$ on $X$ with cone angle $2 \pi \beta$ along a smooth hypersurface $D$, we mean that $\omega$ is smooth Kähler-Einstein on $X \backslash D$, and near each point $p \in D$, there exists coordinate neighborhood $\left(z, z_{2}, \cdots, z_{n}\right) \in U$ such that locally $D$ is defined by $\{z=0\}$, and $\omega$ is quasi-isometric to a local model metric $\omega_{\beta}=\sqrt{-1}\left\{|z|^{2 \beta-2} \mathrm{~d} z \wedge \mathrm{~d} \bar{z}+\sum_{i=2}^{n} \mathrm{~d} z_{i} \wedge \mathrm{~d} \bar{z}_{i}\right\}$ on $U$.

\footnotetext{
Date: Aug 19 ,2013.
}

By studying the smoothing continuity path and proving uniform $C^{2}$ estimate in terms of local model conical metric along the hypersurface, we could get weak conical Kähler-Einstein metrics. Let $X$ be a compact Kähler manifold, $\omega_{0}$ be a smooth Kähler metric on $X$, and $D$ be a smooth hypersurface, $\beta \in(0,1)$, suppose the cohomological condition $c_{1}(X)=\mu\left[\omega_{0}\right]+(1-\beta) c_{1}\left(L_{D}\right)$ is satisfied. By studying a smoothing of the current equation $\operatorname{Ric}\left(\omega_{\phi}\right)=\mu \omega_{\phi}+(1-\beta) \chi$, we get the main theorem of this paper

Theorem 1. There are three situations:
1.For $\mu<0$, there exists weak conical Kähler-Einstein metric with Ricci curvature $\mu$;
2.For $\mu=0$, there exists weak conical Kähler-Einstein metric with zero Ricci curvature;
3.For $\mu>0$, under the assumption that $c_{1}\left(L_{D}\right)$ is nonnegative and the twisted K-Energy is proper, there exists weak conical Kähler-Einstein metric with Ricci curvature $\mu$.

Brendle proved the existence of Ricc-flat Kähler metrics with conical singularity along a smooth hypersurface under the assumption that the cone angle $\beta<\frac{1}{2}$. A group of authors Campana, Guenancia and Păun [2] dealt with the general situation where the divisor $D$ is allowed to have simple normal crossing, under the assumption that $\beta \leq \frac{1}{2}$. Around the same time, another group of authors Jeffres, Mazzeo and Rubinstein obtained the existence of conical Kähler-Einstein metrics with conical singularities along a smooth hypersurface by studying the classical continuity path of conical singular metrics for general angle $\beta \in(0,1)$.

The method adopted here differs from the work of Brendle [1] and Jeffres, Mazzeo and Rubinstein[8] in the sense that by smoothing the delta distribution $\chi$ in the equation, we avoided dealing with continuity path of singular metrics.

In Section 2 we primarily set up the problem of solving conical Kähler-Einstein metric with positive Ricci curvature on a Fano manifold, and we also outline how uniform $C^{0}$ estimate is obtained for the Smooth Continuity Path. Then following the idea of using Chern-Lu inequality as in Chen, Donaldson and Sun [3], a rough $C^{2}$ bound is derived. Section 3 explains how to go from this rough $C^{2}$ bound to a finer $C^{2}$ bound $C^{-1} \omega_{\beta, \epsilon} \leq \omega_{\phi_{\epsilon}} \leq C \omega_{\beta, \epsilon}$ by using a local Moser iteration. In section 4, it is illustrated how this idea could be applied to the general case of the current equation in the main theorem. The last section discusses some questions about the regularity problem of the weak conical Kähler-Einstein metric.

I was motivated to use a smooth Continuity method after reading the series of papers [3],[4],[5] by Chen, Donaldson and Sun and the hope that the angle assumption $\beta \leq \frac{1}{2}$ in Campana, Guenancia and Păun [7] could be removed by doing Yau's estimate locally. While preparing this note, I noticed the beautiful paper of Guenancia and Păun where they removed the assumption on $\beta$ and proved the existence of weak conical Kähler-Einstein metrics for the more general case of simple normal crossing divisors. However, the method used here, the local Moser iteration, which could deal with the situation of smooth hypersurfaces, is different from their work and hopefully this is still of some interest.

Acknowledgement: I would like to express great thanks to Professor Xiuxiong Chen, who gave me constantly encouragement and showed great patience during working on this problem. I would also like to thank Dr. Song Sun, Dr. Haozhao Li and Dr. Yuanqi Wang for helpful discussion and providing useful notes at some points. The discussion with Yu Zeng and Long Li also helped me clarify several things which were not clear to me before.

\section*{2. Setting Up for Fano Case}

Suppose $X$ is a smooth Fano manifold and $D$ is a smooth anti-canonical divisor, following [7], we define a weak conical Kähler-Einstein metric with conical angle $2 \pi \beta$ to be a metric which is smooth Kähler-Einstein on $X \backslash D$ and quasi-isometric to a local model metric $\sqrt{-1}\left\{\beta^{2}|z|^{2 \beta-2} \mathrm{~d} z \wedge \mathrm{~d} \bar{z}+\sum_{i=2}^{n} \mathrm{~d} z_{i} \wedge \mathrm{~d} \bar{z}_{i}\right\}$ near the divisor $D$ where $z=0$ is local defining function of $D$.

Under the assumption the Twisted K-Energy (see [3] or [9]) is proper,the existence of weak Kähler-Einstein metric with conical angle $2 \pi \beta$ for $\beta \in(0,1)$ is established by a slightly different way from [8] in the sense that we are solving smooth continuity method with uniform $C^{2}$ bound instead of dealing with the continuity path for the conical singular metrics directly.

Take $\omega_{0}$ to be a fixed smooth background Kähler metric in $c_{1}(X)$ and take a Hermitian metric $h$ on $L_{D}$ with curvature form $\omega_{0}$, then we could consider the Continuity Path:
$$\operatorname{Ric} \omega_{\phi_{\epsilon}(t)}=t \omega_{\phi_{\epsilon}(t)}+(\beta-t) \omega_{0}+(1-\beta) \chi_{\epsilon}$$
where the starting point is $\omega_{\phi_{\epsilon}(0)}=\omega_{\varphi_{\epsilon}}$ satisfying Ric $\omega_{\varphi_{\epsilon}}=\beta \omega_{0}+(1-\beta) \chi_{\epsilon}$, and $\chi_{\epsilon}=\omega_{0}+\sqrt{-1} \partial \bar{\partial} \log \left(|S|_{h}^{2}+\epsilon\right)$ is smooth positive closed $(1,1)$ form in $c_{1}(X)$ approaching the Delta Distribution $\chi$ along $D$. This could be done following the Calabi's Volume form Conjecture solved by Yau.

Solve the smooth Kähler-Einstein problem is well-known to be obstructed by some Stability Condition (See the recent work relating K-Stability and Kähler-Einstein metrics on Fano case by [3], [4] and [5]) algebraically and Properness of K-Energy [13] analytically).

Similarly, in the case of conical Kähler-Einstein situation, analytically we also need the properness of some functional, namely the Twisted K-Energy. Let's recall the definitions:
$$\begin{gathered}
E(\phi)=-n \int_{0}^{1} \mathrm{~d} t \int_{X} \dot{\phi}_{t}\left(\operatorname{Ric}\left(\omega_{\phi_{t}}\right)-\omega_{\phi_{t}}\right) \wedge \omega_{\phi_{t}}^{n-1} \\
E_{(1-\beta) D}(\phi)=E(\phi)+(1-\beta) J_{\chi}(\phi) \\
E_{\epsilon,(1-\beta) D}(\phi)=E(\phi)+(1-\beta) J_{\chi_{\epsilon}}(\phi) \\
J_{\chi}(\phi)=n \int_{0}^{1} \mathrm{~d} t \int_{X} \dot{\phi}_{t}\left(\chi-\omega_{\phi_{t}}\right) \wedge \omega_{\phi_{t}}^{n-1}
\end{gathered}$$
$$J_{\chi_{\epsilon}}(\phi)=n \int_{0}^{1} \mathrm{~d} t \int_{X} \dot{\phi}_{t}\left(\chi_{\epsilon}-\omega_{\phi_{t}}\right) \wedge \omega_{\phi_{t}}^{n-1}$$
for any path of smooth potential $\phi_{t}$ connecting $\omega_{0}$ and $\omega_{\phi}$. And by saying Proper, we mean that there exists constant $C_{1}$ and $C_{2}$ s.t. $E_{(1-\beta) D}(\phi) \geq C_{1}(I-J)(\phi)-C_{2}$, where $I, J$ are the classical functionals used in the reference, for instance [9].

Proposition 1. If $E_{(1-\beta) D}$ is proper, then the above continuity path is solvable up to $t=\beta$ for any $\epsilon \in(0,1]$.

Proof. We assume $\omega_{0}$ has volume 1. Along the continuity path, the Twisted K-Energy is decreasing by a direct computation as soon as $t<\beta$. Since the initial metric satisfies the Monge-Ampère equation $\omega_{\varphi_{\epsilon}}^{n}=e^{h_{\omega_{0}}+C_{\epsilon}} \frac{\omega_{0}^{n}}{\left(|S|_{h}^{2}+\epsilon\right)^{1-\beta}}$, where $C_{\epsilon}$ is chosen constant (bounded above and below) so that $\int_{X} e^{h_{\omega_{0}}+C_{\epsilon}} \frac{\omega_{0}^{n}}{\left(|S|_{h}^{2}+\epsilon\right)^{1-\beta}}=\int_{X} \omega_{0}^{n}=1$, for $1<p<\frac{1}{1-\beta}$,
$$\begin{aligned}
\int_{X}\left(\frac{e^{h_{\omega_{0}}+C_{\epsilon}}}{\left(|S|_{h}^{2}+\epsilon\right)^{1-\beta}}\right)^{p} \omega_{0}^{n} & =\int_{X}\left(\frac{e^{h_{\omega_{0}}}}{\left(|S|_{h}^{2}+\epsilon\right)^{1-\beta}}\right)^{p} \omega_{0}^{n} /\left(\int_{X} \frac{e^{h_{\omega_{0}}}}{\left(|S|_{h}^{2}+\epsilon\right)^{1-\beta}} \omega_{0}^{n}\right)^{p} \\
& \leq C \int_{X}\left(\frac{e^{h_{\omega_{0}}}}{\left(|S|_{h}^{2}+\epsilon\right)^{1-\beta}}\right)^{p} \omega_{0}^{n} \\
& \leq C
\end{aligned}$$
Kolodziej's theorem tells us that $\varphi_{\epsilon}$ has uniform $C^{\alpha}$ bound since the right hand side of the equation is uniform in $L^{p}$ for some $p>1$.

By an explicit formula(see [9]) of the Twisted $K$-Energy:
$$E_{\epsilon,(1-\beta) D}(\phi)=\int_{X} \log \frac{\omega_{\phi}^{n}}{\omega_{0}^{n}} \omega_{\phi}^{n}-\beta(I-J)(\phi)+\int_{X}\left\{h_{\omega_{0}}-(1-\beta) \log \left(|S|_{h}^{2}+\epsilon\right)\right\}\left(\omega_{0}^{n}-\omega_{\phi}^{n}\right) .$$

For the initial Kähler metrics $\omega_{\varphi_{\epsilon}}$,
$$\begin{aligned}
E_{\epsilon,(1-\beta) D}\left(\varphi_{\epsilon}\right) & =\int_{X} \log \frac{\omega_{\varphi_{\epsilon}}^{n}}{\omega_{0}^{n}} \omega_{\varphi_{\epsilon}}^{n}-\beta(I-J)\left(\varphi_{\epsilon}\right)+\int_{X}\left\{h_{\omega_{0}}-(1-\beta) \log \left(|S|_{h}^{2}+\epsilon\right)\right\}\left(\omega_{0}^{n}-\omega_{\varphi_{\epsilon}}^{n}\right) \\
& =\int_{X} C_{\epsilon} \omega_{\phi_{\epsilon}}^{n}+\int_{X}\left\{h_{\omega_{0}}-(1-\beta) \log \left(|S|_{h}^{2}+\epsilon\right)\right\} \omega_{0}^{n}-\beta(I-J)\left(\varphi_{\epsilon}\right) \\
& \leq C
\end{aligned}$$
where the last inequality holds since the other classical functionals $I, J$ are bounded as soon the potential has $C^{0}$ bound. By the assumption that $E_{(1-\beta) D}$ is proper, we know that $E_{\epsilon,(1-\beta) D}(\phi) \geq E_{(1-\beta) D}(\phi)-C \geq C_{1}(I-J)(\phi)-C_{2}$, then similarly as the proof on Page 12 in [3], we could solve the continuity path up to $t=\beta$ with uniform $C^{0}$ bound on $\phi_{\epsilon}(\beta)=\phi_{\epsilon}$. \(\square\)

The solution at the endpoint of the continuity method $\omega_{\phi_{\epsilon}(\beta)}=\omega_{\phi_{\epsilon}}$ satisfy Monge-Ampère equation for suitable normalization on $\phi_{\epsilon}$ :
$$\omega_{\phi_{\epsilon}}=e^{-\beta \phi_{\epsilon}+h_{\omega_{0}}} \frac{\omega_{0}^{n}}{\left(|S|_{h}^{2}+\epsilon\right)^{1-\beta}}$$

With $C^{0}$ bound in hand, by using global Chern-Lu inequality, a rough bound could be derived, see [3] for example. For the reader's convenience, we outline the proof here. Keep in mind that from now on, all the constant $C$ 's are constant varying from line to line, which are independent of $\epsilon$.

Lemma 1. (Chern-Lu Inequality) Suppose $\omega$ and $\eta$ are two Kähler metrics on a compact Kähler manifold, if $\operatorname{Ric}(\omega) \geq C_{1} \omega-C_{2} \eta$ and the holomorphic bisectional curvature $R_{i \bar{j} k \bar{l}}^{\eta} \leq$ $C_{3}\left(h_{i \bar{j}} h_{k \bar{l}}+h_{i \bar{l}} h_{k \bar{j}}\right)$, then
$$\Delta_{\omega} \log t r_{\omega} \eta \geq C_{1}-\left(C_{2}+2 C_{3}\right) t r_{\omega} \eta .$$

Proposition 2. (3) $\exists C$, s.t. $C^{-1} \omega_{0} \leq \omega_{\phi_{\epsilon}} \leq \frac{C}{\left(|S|^{2}+\epsilon\right)^{1-\beta}} \omega_{0}$.
Proof. Since on $X \backslash D$,
$$\begin{aligned}
\chi_{\epsilon}=\omega_{0}+\sqrt{-1} \partial \bar{\partial} \log \left(|S|_{h}^{2}+\epsilon\right) & =\omega_{0}+\sqrt{-1} \partial \frac{|S|_{h}^{2} \bar{\partial} \log |S|_{h}^{2}}{|S|_{h}^{2}+\epsilon} \\
& =\omega_{0}+\frac{|S|_{h}^{2}}{|S|_{h}^{2}+\epsilon} \sqrt{-1} \partial \bar{\partial} \log |S|_{h}^{2}+\sqrt{-1} \frac{\epsilon}{|S|_{h}^{2}\left(|S|_{h}^{2}+\epsilon\right)^{2}} \partial|S|_{h}^{2} \wedge \bar{\partial}|S|_{h}^{2} \\
& \geq \omega_{0}+\frac{|S|_{h}^{2}}{|S|_{h}^{2}+\epsilon}\left(-\omega_{0}\right) \\
& \geq 0
\end{aligned}$$
the smooth $(1,1)$ form $\chi_{\epsilon} \geq 0$
Because $\operatorname{Ric}\left(\omega_{\phi_{\epsilon}}\right)=\beta \omega_{\phi_{\epsilon}}+(1-\beta) \chi_{\epsilon} \geq \beta \omega_{\phi_{\epsilon}}$ and the bisectional curvature of $\omega_{0}$ is bounded above by $\Lambda$, the Chern-Lu inequality in the above lemma tells
$$\Delta_{\omega_{\phi_{\epsilon}}} \log \operatorname{tr}_{\omega_{\phi_{\epsilon}}} \omega_{0} \geq \beta-2 \Lambda \operatorname{tr}_{\omega_{\phi_{\epsilon}}} \omega_{0} .$$

And by using the fact that $\Delta_{\omega_{\phi_{\epsilon}}} \phi=\operatorname{tr}_{\omega_{\phi_{\epsilon}}}\left(\omega_{\phi_{\epsilon}}-\omega_{0}\right)=n-\operatorname{tr}_{\omega_{\phi_{\epsilon}}} \omega_{0}$, we get the inequality
$$\Delta_{\omega_{\phi_{\epsilon}}}\left\{\log \operatorname{tr}_{\omega_{\phi_{\epsilon}}} \omega_{0}-(2 \Lambda+1) \phi_{\epsilon}\right\} \geq \operatorname{tr}_{\omega_{\phi_{\epsilon}}} \omega_{0}+\beta-n(2 \Lambda+1) .$$
The maximum principle on this compact manifold tells us $\operatorname{tr}_{\omega_{\phi_{\epsilon}}} \omega_{0} \leq\{n(2 \Lambda+1)-\beta\} e^{(2 \Lambda+1) \operatorname{Osc} \phi_{\epsilon}}$, thus $\omega_{0} \leq C \omega_{\phi_{\epsilon}}$ and the bound in the other direction follows from this bound together with the Monge-Ampère equation. \(\square\)

The upper bound in this control is satisfactory in the perpendicular direction while it is still far away from the correct control in the tangential direction. In the next section, we are going to apply local Moser iteration to improve the upper bound of $\omega_{\phi_{\epsilon}}$.

\section*{3. Uniform Laplacian Estimate}
3.1. A local smooth approximate metric. Since we are willing to get a comparison between the metric $\omega_{\phi_{\epsilon}}$ and the local model conic metric $\omega_{\beta, \epsilon}=\sqrt{-1}\left\{\left(|z|^{2}+\epsilon\right)^{\beta-1} \mathrm{~d} z \wedge \mathrm{~d} \bar{z}+\right.$ $\left.\sum_{i=2}^{n} \mathrm{~d} z_{i} \wedge \mathrm{~d} \bar{z}_{i}\right\}$ only in a local sense, to try to apply some kind of local maximum principle is not so easy. Instead of getting the upper bound from maximum principle, we apply local Moser iteration to overcome this difficulty.

We want to compare the Kähler metric $\omega_{\phi_{\epsilon}}$ with the regularized metric $\omega_{\beta, \epsilon}$ above locally on a coordinate balls near the divisor. The rough bound $C^{-1} \omega_{E u c} \leq \omega_{\phi_{\epsilon}} \leq \frac{C}{\left(|S|^{2}+\epsilon\right)^{1-\beta}} \omega_{E u c}$ implies a rough geometry.

Lemma 2. There is Hölder control for the distance function $\omega_{\phi_{\epsilon}}$ :
\begin{itemize}
\item[1.] For any $R>0, B_{\phi_{\epsilon}}(p, R) \subset B_{\text {Euc }}(p, \sqrt{C} R)$;
\item[2.] For any $R>0, \exists \delta=\delta(R)\left(=\tilde{C} R^{\frac{1}{\beta}}\right)>0, \epsilon(R)>0$, s.t. $\forall \epsilon<\epsilon(R), B_{E u c}(p, \delta) \subset$ $B_{\phi_{\epsilon}}(p, R)$, where $\tilde{C}=\left\{\left(\frac{2}{\beta}+2\right) \sqrt{C}\right\}^{-\frac{1}{\beta}}$.
\end{itemize}

Proof. The first part is just a direct consequence of the bound $\omega_{E u c} \leq C \omega_{\phi_{\epsilon}}$, any curve initiating from $p$ measuring under the metric $\omega_{\phi_{\epsilon}}$ with length less than $R$ will have length less than $\sqrt{C} R$ when measured using the Euclidean metric.

The second part of the containing relationship is also not so difficult. On an Euclidean ball $B_{\text {Euc }}(p, \delta)=\left\{\left(z, z_{2}, \cdots, z_{n}\right)| | z\left|\leq \delta,\left|z_{i}\right| \leq \delta\right\}\right.$ centered at $p$, pick any point $q$, then $q$ is joined with $p$ by detouring line segments $\overline{q q^{\prime}}, \overline{q^{\prime} p^{\prime}}, \overline{p^{\prime} p}$, where $q^{\prime}$ is the point on the boundary of the Euclidean ball with the same $z_{2}, \cdots, z_{n}$ coordinates as $q$ and $z$ coordinate just the radial projection of the $z$ coordinate of $q$ to the boundary, and $p^{\prime}$ is just the projection of $q^{\prime}$ to the complex line $z_{2}=0, \cdots, z_{n}=0$. When measured under the metric $\omega_{\phi_{\epsilon}},\left|\overline{q q^{\prime}}\right| \leq \int_{r=0}^{\delta} \sqrt{C}\left(r^{2}+\epsilon\right)^{\frac{\beta-1}{2}} \mathrm{~d} r \leq \sqrt{C} \frac{1}{\beta} \delta^{\beta}$ and similarly $\left|\overline{p p^{\prime}}\right| \leq \sqrt{C} \frac{1}{\beta} \delta^{\beta}$ and $\left|\overline{q^{\prime} p^{\prime}}\right| \leq$ $\int_{z^{\prime} \in \overline{q^{\prime} p^{\prime}}} \sqrt{C}\left(\delta^{2}+\epsilon\right)^{\frac{\beta-1}{2}}\left|\mathrm{~d} z^{\prime}\right| \leq \sqrt{C}\left(\delta^{2}+\epsilon\right)^{\frac{\beta-1}{2}} \delta \leq \sqrt{C}\left(\delta^{2}+\epsilon\right)^{\frac{\beta}{2}}$. Therefore, if we choose $\delta$ so that $\left(\frac{2}{\beta}+2\right) \sqrt{C} \delta^{\beta}<R$ and choose $\epsilon(R)=\delta^{2}$, then the distance of $q$ and $p$ under the metric $\omega_{\phi_{\epsilon}}$ will be no bigger than $R$. \(\square\)

Also, as is proved in [3], the rough bound $C^{-1} \omega_{0} \leq \omega_{\phi_{\epsilon}} \leq \frac{C}{\left(|S|_{h}^{2}+\epsilon\right)^{1-\beta}} \omega_{0}$ gives the bound on diameter.

Lemma 3. The diameter of $\left(X, \omega_{\phi_{\epsilon}}\right)$ is bounded above.
From this rough geometry, a finite collection of covering on $D$ which Moser Iteration will be applied could be chosen. Firstly, around each point $p_{\alpha} \in D$, there exists coordinate ball $\mathcal{U}_{\alpha}\left(p_{\alpha}\right)=\tau_{\alpha}\left(B_{\alpha}\left(0, r_{\alpha}\right)\right)$ where $B_{\alpha}\left(0, r_{\alpha}\right)=\left\{\left(z^{\alpha}=z_{1}^{\alpha}, z_{2}^{\alpha}, \cdots, z_{n}^{\alpha}\right)| | z^{\alpha}\left|,\left|z_{2}^{\alpha}\right|, \cdots,\left|z_{n}^{\alpha}\right|<\right.\right.$ $\left.r_{\alpha}\right\} \subset \mathbb{C}^{n}$, such that $\mathcal{U}_{\alpha} \cap D$ corresponds to $\left\{z^{\alpha}=0\right\}$, the first item of Lemma 2 tells that $\mathcal{U}_{\alpha}$ contains $\omega_{\phi_{\epsilon}}$-metric ball $U_{\alpha}=B_{\phi_{\epsilon}}\left(p_{\alpha}, \frac{r_{\alpha}}{\sqrt{C}}\right)$, and the second item of Lemma 2 tells this metric ball contains Euclidean ball $B_{E u c}\left(p_{\alpha}, \delta\left(\frac{r_{\alpha}}{\sqrt{C}}\right)\right)$ and again this contains $\omega_{\phi_{\epsilon}}-$ metric ball $V_{\alpha}=B_{\phi_{\epsilon}}\left(p_{\alpha}, \frac{1}{\sqrt{C}} \delta\left(\frac{r_{\alpha}}{\sqrt{C}}\right)\right), V_{\alpha}$ contains coordinate ball $\mathcal{V}_{\alpha}\left(p_{\alpha}\right)=B_{E u c}\left(p_{\alpha}, s_{\alpha}\right)$,
for $s_{\alpha}=\delta\left(\frac{1}{\sqrt{C}} \delta\left(\frac{r_{\alpha}}{\sqrt{C}}\right)\right)$. Since $D$ is compact, we could cover it by finitely many $\mathcal{V}_{\alpha}\left(p_{\alpha}\right)$ 's, and the weight for the Hermitian metric $e^{-h_{\alpha}}$ satisfies $\left|h_{\alpha}\right| \leq C_{\alpha},\left|\frac{\partial h_{\alpha}}{\partial z_{i}^{\alpha}}\right| \leq C_{\alpha},\left|\frac{\partial^{2} h_{\alpha}}{\partial z_{i}^{\alpha} \partial \bar{z}_{i}^{\alpha}}\right| \leq C_{\alpha}$.

Then on each $\mathcal{U}_{\alpha}$, take the smooth Kähler metrics $\omega_{\beta, \epsilon}^{\alpha}=\sqrt{-1}\left\{\beta^{2}\left(\left|z^{\alpha}\right|^{2}+\epsilon\right)^{\beta-1} \mathrm{~d} z^{\alpha} \wedge\right.$ $\left.\mathrm{d} \bar{z}^{\alpha}+\sum_{j=2}^{n} \mathrm{~d} z_{j}^{\alpha} \wedge \mathrm{d} \bar{z}_{j}^{\alpha}\right\}$ as the approximating metrics to the standard flat conical metric. From now on, for simplicity the notations will forget about $\alpha$. For those local metrics, $R_{1 \overline{1} 1 \overline{1}}=\epsilon(1-\beta)\left(|z|^{2}+\epsilon\right)^{\beta-3}$, and $R_{i \bar{j} k \bar{l}}=0$ if one of $i, j, k, l \neq 1$, therefore the holomorphic bisectional curvature $R(\xi, \bar{\xi}, \eta, \bar{\eta})=\left|\xi^{1}\right|^{2}\left|\eta^{1}\right|^{2} R_{1 \overline{1} 1 \overline{1}} \geq 0$ for any pair of ( 1,0 )-vector fields $\xi=\xi^{1} \frac{\partial}{\partial z}+\sum_{i} \xi^{i} \frac{\partial}{\partial z^{i}}$, and $\eta=\eta^{1} \frac{\partial}{\partial z}+\sum_{i} \eta^{i} \frac{\partial}{\partial z^{i}}$.
3.2. Differential Inequality. The goal of this section is to derive a local differential inequality on $\tilde{U}_{\alpha}$. Let $\sigma_{\epsilon, \beta}=\operatorname{tr}_{\omega_{\beta, \epsilon}} \omega_{\phi_{\epsilon}}$, then

Proposition 3.
$$\Delta_{\omega_{\phi_{\epsilon}}} \log \sigma_{\epsilon, \beta} \geq-C\left(|z|^{2}+\epsilon\right)^{-\beta}-C$$

To prove this inequality we need a lemma.
Lemma 4.
$$\Delta_{\omega_{\phi_{\epsilon}}} \sigma_{\epsilon, \beta} \geq-C \sigma_{\epsilon, \beta}-C+\sum_{i, j, k} \frac{1}{1+\phi_{i \bar{i}}} \frac{1}{1+\phi_{j \bar{j}}}\left|\phi_{i \bar{j} k}\right|^{2}-C\left(|z|^{2}+\epsilon\right)^{-\beta}$$
Proof. (Proof of Lemma 2) First, on $\mathcal{U}_{\alpha}$, suppose $\omega_{\beta, \epsilon}=\omega_{0}+\sqrt{-1} \partial \bar{\partial} \psi_{\epsilon}$ with suitable normalization on the potential $\psi_{\epsilon}$ such that $\left\|\psi_{\epsilon}\right\|_{C^{0}} \leq C$, rewrite the equation (2),
$$\left(\omega_{\beta, \epsilon}+\sqrt{-1} \partial \bar{\partial} \tilde{\phi}_{\epsilon}\right)^{n}=e^{F_{\epsilon, \beta}} \omega_{\beta, \epsilon}^{n}$$
where $F_{\epsilon, \beta}=-\beta \phi_{\epsilon}+h_{\omega_{0}}+(1-\beta) h+(1-\beta) \log \frac{|z|^{2}+\epsilon}{|z|^{2}+\epsilon e^{h}}+\log \frac{\omega_{o}^{n}}{\omega_{E u c}^{n}}$.
Following Yau's calculation on the $C^{2}$ estimate, use $g_{i \bar{j}}$ to denote the background metric $\omega_{\beta, \epsilon}$ and $g_{i \bar{j}}^{\prime}$ to denote $\omega_{\phi_{\epsilon}}$, then under the local normal coordinate for which $g_{i \bar{j}}=\delta_{i \bar{j}}, g_{i \bar{j}}^{\prime}=$ $\left(1+\phi_{i \bar{j}}\right) \delta_{i \bar{j}}$,
$$\begin{aligned}
\Delta_{\omega_{\phi_{\epsilon}}} \sigma_{\epsilon, \beta} & =\Delta_{\omega_{\beta, \epsilon}} F_{\epsilon, \beta}+\sum_{i, j, k, l, n} g^{\prime k \bar{j}} g^{\prime}{ }^{i n} \phi_{k \bar{n} \bar{l}} \phi_{i \bar{j} l}+\sum_{k, l} R_{k \bar{k} l \bar{l}} \frac{\left(\phi_{k \bar{k}}-\phi_{l \bar{l}}\right)^{2}}{\left(1+\phi_{k \bar{k}}\right)\left(1+\phi_{l \bar{l}}\right)} \\
& \geq \Delta_{\omega_{\beta, \epsilon}} F_{\epsilon, \beta}+\sum_{i, j, k} \frac{1}{1+\phi_{i \bar{i}}} \frac{1}{1+\phi_{j \bar{j}}}\left|\phi_{i \bar{j} k}\right|^{2}
\end{aligned}$$

Since $h_{\omega_{0}}, h$ and $\log \frac{\omega_{0}^{n}}{\omega_{E u c}^{n}}$ are smooth functions, and $\Delta_{\omega_{\beta, \epsilon}} \phi_{\epsilon}=\operatorname{tr} \omega_{\omega_{\beta, \epsilon}}\left(\omega_{\phi_{\epsilon}}-\omega_{0}\right) \leq \sigma_{\epsilon, \beta}$, our primarily care should be the lower bound on $\Delta_{\omega_{\beta, \epsilon}} \log \frac{\left(|z|^{2}+\epsilon\right)}{\left(|z|^{2}+\epsilon e^{h}\right)}$.
$$\begin{aligned}
\sqrt{-1} \partial \bar{\partial} \log \left(|z|^{2}+\epsilon\right)= & \sqrt{-1} \frac{\epsilon \mathrm{~d} z \wedge \mathrm{~d} \bar{z}}{\left(|z|^{2}+\epsilon\right)^{2}} \\
\sqrt{-1} \partial \bar{\partial} \log \left(|z|^{2}+\epsilon e^{h}\right)= & \sqrt{-1}\left\{\frac{\epsilon e^{h}+\epsilon e^{h}|z|^{2} \frac{\partial^{2} h}{\partial z \partial \bar{z}}+\epsilon^{2} e^{2 h} \frac{\partial^{2} h}{\partial z \partial \bar{z}}+\epsilon e^{h}|z|^{2}\left|\frac{\partial h}{\partial z}\right|^{2}-\epsilon e^{h}\left(\bar{z} \frac{\partial h}{\partial \bar{z}}+z \frac{\partial h}{\partial z}\right)}{\left(|z|^{2}+\epsilon e^{h}\right)^{2}} \mathrm{~d} z \wedge \mathrm{~d} \bar{z}\right. \\
& \left.+\sum_{i=2}^{n} \frac{\epsilon e^{h}|z|^{2} \frac{\partial^{2} h}{\partial \bar{z}_{i} \partial z_{i}}+\epsilon^{2} e^{2 h} \frac{\partial^{2} h}{\partial \bar{z}_{i} \partial z_{i}}+\epsilon e^{h}|z|^{2} \frac{\partial h}{\partial \bar{z}_{i}} \frac{\partial h}{\partial z_{i}}}{\left(|z|^{2}+\epsilon e^{h}\right)^{2}} \mathrm{~d} z_{i} \wedge \mathrm{~d} \bar{z}_{i}\right\} \\
& + \text { mixed terms } \\
& \leq C \sqrt{-1}\left\{\frac{\epsilon}{\left(|z|^{2}+\epsilon\right)^{2}} \mathrm{~d} z \wedge \mathrm{~d} \bar{z}+\sum_{i=2}^{n} \mathrm{~d} z_{i} \wedge \mathrm{~d} \bar{z}_{i}\right\}+\text { mixed terms } \\
& \leq C \sqrt{-1}\left\{\frac{1}{|z|^{2}+\epsilon} \mathrm{d} z \wedge \mathrm{~d} \bar{z}+\sum_{i=2}^{n} \mathrm{~d} z_{i} \wedge \mathrm{~d} \bar{z}_{i}\right\}+\text { mixed terms }
\end{aligned}$$

Because $\omega_{\beta, \epsilon}$ is diagonal metric, the mixed terms do not contribute when take the trace, thus we get $\Delta_{\omega_{\beta, \epsilon}} \log \frac{|z|^{2}+\epsilon}{|z|^{2}+\epsilon e^{h}} \geq-C\left\{\left(|z|^{2}+\epsilon\right)^{1-\beta}\left(|z|^{2}+\epsilon\right)^{-1}+\left(|z|^{2}+\epsilon\right)^{1-\beta}\right\} \geq-C\left(|z|^{2}+\right.$ $\epsilon)^{-\beta}-C$, and the Lemma follows. \(\square\)

Proof. (Proof of Proposition 3)
$$\begin{aligned}
\left|\nabla \sigma_{\epsilon, \beta}\right|_{\omega_{\phi_{\epsilon}}}^{2} & =\sum_{i, j, k, l, p, q} g^{\prime i \bar{j}} g^{k \bar{l}} \phi_{k \bar{l} i} g^{p \bar{q}} \phi_{p \bar{q} \bar{j}} \\
& =\sum_{i} \frac{1}{1+\phi_{i \bar{i}}}\left|\sum_{k} \phi_{k \bar{k} i}\right|^{2} \\
& =\sum_{i} \frac{1}{1+\phi_{i \bar{i}}}\left|\sum_{k} \frac{\phi_{k \bar{k} i}}{\left(1+\phi_{k \bar{k}}\right)^{1 / 2}}\left(1+\phi_{k \bar{k}}\right)^{1 / 2}\right|^{2} \\
& \leq \sum_{i} \frac{1}{1+\phi_{i \bar{i}}} \sum_{k} \frac{\left|\phi_{k \bar{k} i}\right|^{2}}{1+\phi_{k \bar{k}}} \sum_{l}\left(1+\phi_{l \bar{l}}\right) \\
& =\sigma_{\epsilon, \beta} \sum_{i, k} \frac{1}{1+\phi_{i \bar{i}}} \frac{1}{1+\phi_{k \bar{k}}}\left|\phi_{k \bar{k} i}\right|^{2} \\
& \leq \sigma_{\epsilon, \beta} \sum_{i, j, k} \frac{1}{1+\phi_{i \bar{i}}} \frac{1}{1+\phi_{j \bar{j}}}\left|\phi_{i \bar{j} k}\right|^{2}
\end{aligned}$$

By the formula $\Delta_{\omega_{\phi_{\epsilon}}} \log \sigma_{\epsilon, \beta}=\frac{\Delta_{\omega_{\phi_{\epsilon}}} \sigma_{\epsilon, \beta}}{\sigma_{\epsilon, \beta}}-\frac{\left|\nabla \sigma_{\epsilon, \beta}\right|^{2}}{\sigma_{\epsilon, \beta}^{2}}$, together with the lower bound on $\sigma_{\epsilon, \beta}=\operatorname{tr}_{\omega_{\beta, \epsilon}} \omega_{\phi_{\epsilon}} \geq(n-1) C$ (here, we assume $n \geq 2$; for $n=1$ case, the $C^{2}$ bound is straightforward), we could deduce the inequality
$$\begin{aligned}
\Delta_{\omega_{\phi}} \log \sigma_{\epsilon, \beta} & \geq \frac{-C \sigma_{\epsilon, \beta}-C}{\sigma_{\epsilon, \beta}}+\frac{1}{\sigma_{\epsilon, \beta}} \sum_{i, j, k} \frac{1}{1+\phi_{i \bar{i}}} \frac{1}{1+\phi_{j \bar{j}}}\left|\phi_{i \bar{j} k}\right|^{2}-\frac{\left|\nabla \sigma_{\epsilon, \beta}\right|^{2}}{\sigma_{\epsilon, \beta}^{2}}-C \frac{\left(|z|^{2}+\epsilon\right)^{-\beta}}{\sigma_{\epsilon, \beta}} \\
& \geq-C-\frac{C}{\sigma_{\epsilon, \beta}}-\frac{\left(|z|^{2}+\epsilon\right)^{-\beta}}{\sigma_{\epsilon, \beta}} \\
& \geq-C-C\left(|z|^{2}+\epsilon\right)^{-\beta}
\end{aligned}$$ \(\square\)

The rough bound $C^{-1} \omega_{0} \leq \omega_{\phi_{\epsilon}} \leq C \frac{\omega_{0}}{\left(|z|^{2}+\epsilon\right)^{1-\beta}}$ is not enough for our application. We may first use the rougher lower bound $\omega_{\phi_{\epsilon}} \leq C \frac{\omega_{0}}{\left(|z|^{2}+\epsilon\right)^{1-\beta^{\prime}}}$ by decreasing the angle a little bit to get a better control on the tangential direction and then conclude the correct upper bound on the direction perpendicular to the divisor.

\subsection*{3.3. Decreasing the angle a little. Let's rewrite the equation}
$$\omega_{\phi_{\epsilon}}^{n}=e^{F_{\epsilon, \beta^{\prime}}} \omega_{\beta^{\prime}, \epsilon}^{n}$$
where $\beta^{\prime}$ is a number a little bit smaller than $\beta$, and $F_{\epsilon, \beta^{\prime}}=F_{\epsilon, \beta}+\left(\beta-\beta^{\prime}\right) \log \left(|z|^{2}+\epsilon\right)$. Then we have a similar inequality as in the above section:

\section*{Proposition 4.}
$$\Delta_{\omega_{\phi_{\epsilon}}} \log \sigma_{\epsilon, \beta^{\prime}} \geq-C\left(|z|^{2}+\epsilon\right)^{-\beta^{\prime}}-C$$

Proof. (Proof of Proposition 4) Since $\sqrt{-1} \partial \bar{\partial} F_{\epsilon, \beta^{\prime}}=\sqrt{-1} \partial \bar{\partial} F_{\epsilon, \beta}+\sqrt{-1} \partial \bar{\partial} \log \left(|z|^{2}+\epsilon\right) \geq$ $\sqrt{-1} \partial \bar{\partial} F_{\epsilon, \beta} \geq-\sqrt{-1} C\left\{\frac{1}{|z|^{2}+\epsilon} \mathrm{d} z \wedge \mathrm{~d} \bar{z}+\sum_{i} \mathrm{~d} z_{i} \wedge \mathrm{~d} \bar{z}_{i}\right\}+$ mixed terms, we have $\Delta_{\omega_{\beta^{\prime}}, \epsilon} F_{\epsilon, \beta^{\prime}}=$ $\operatorname{tr}_{\omega_{\beta^{\prime}, \epsilon}} \sqrt{-1} \partial \bar{\partial} F_{\epsilon, \beta^{\prime}} \geq-C-C\left(|z|^{2}+\epsilon\right)^{1-\beta^{\prime}}\left(|z|^{2}+\epsilon\right)^{-1}=-C-C\left(|z|^{2}+\epsilon\right)^{-\beta^{\prime}}$. \(\square\)

Now modify the differential inequality by adding an auxiliary function $C\left(\beta-\beta^{\prime}\right)^{-2}\left(|z|^{2}+\right.$ $\epsilon)^{\beta-\beta^{\prime}}$, and use the rough bound $\omega_{\phi_{\epsilon}} \leq C \frac{\omega_{0}}{\left(|z|^{2}+\epsilon\right)^{1-\beta}}$, we get the inequality:
$$\begin{aligned}
\Delta_{\omega_{\phi_{\epsilon}}} & \left\{\log \sigma_{\epsilon, \beta^{\prime}}+C\left(\beta-\beta^{\prime}\right)^{-2}\left(|z|^{2}+\epsilon\right)^{\beta-\beta^{\prime}}\right\} \\
& \geq C\left(|z|^{2}+\epsilon\right)^{-\beta^{\prime}}-C\left(|z|^{2}+\epsilon\right)^{-\beta^{\prime}}-C \\
& \geq-C
\end{aligned}$$
Since $\Delta_{\omega_{\phi_{\epsilon}}}\left\{C \beta^{-2}\left(|z|^{2}+\epsilon\right)^{\beta}\right\} \geq C$, the final inequality will be the following proposition:

\section*{Proposition 5.}
$$\Delta_{\omega_{\phi_{\epsilon}}}\left\{\log \sigma_{\epsilon, \beta^{\prime}}+C\left(\beta-\beta^{\prime}\right)^{-2}\left(|z|^{2}+\epsilon\right)^{\beta-\beta^{\prime}}+C \beta^{-2}\left(|z|^{2}+\epsilon\right)^{\beta}\right\} \geq 0$$
3.4. Moser's Iteration. We are going to apply the local Moser Iteration to the function $f=\log \sigma_{\epsilon, \beta^{\prime}}+C\left(\beta-\beta^{\prime}\right)^{-2}\left(|z|^{2}+\epsilon\right)^{\beta-\beta^{\prime}}+C \beta^{-2}\left(|z|^{2}+\epsilon\right)^{\beta}$, notice that since $\sigma_{\epsilon, \beta^{\prime}}=$ $\operatorname{tr}_{\omega_{\beta^{\prime}, \epsilon}} \omega_{\phi_{\epsilon}} \geq \operatorname{tr}_{\omega_{\beta^{\prime}, \epsilon}} C^{-1} \omega_{0} \geq(n-1) C^{-1}$, we could add a constant to $f$ to make it positive.

Now a local inequality is settled up:
$$\Delta_{\omega_{\phi_{\epsilon}}} f \geq 0$$

We are going to do Moser Iteration on the pair of $\omega_{\phi_{\epsilon}}$-metric balls $V_{\alpha}$ and $U_{\alpha}$, since there are only finitely many, there is no loss of generality to assume $V_{\alpha}$ is radius 1 and $U_{\alpha}$ is radius 2. The $L^{\infty}$ norm of $f$ on metric 1-ball will be bounded by the $L^{2}$ bound of $f$ on metric 2-ball, and it is carried out out below, which ignores $\epsilon$ for simplicity:
$$\begin{aligned}
\frac{4 p}{(p+1)^{2}} \int_{X} \eta^{2}\left|\nabla f^{\frac{p+1}{2}}\right|^{2} \omega_{\phi}^{n} & =p \int_{X} \eta^{2} f^{p-1}|\nabla f|^{2} \omega_{\phi}^{n} \\
& =\int_{X}\left\{\nabla\left(\eta^{2} f^{p} \nabla f\right)-2 \eta f^{p} \nabla \eta \cdot \nabla f-\eta^{2} f^{p} \Delta_{\omega_{\phi}} f\right\} \omega_{\phi}^{n} \\
& \leq \int_{X}-2 \eta f^{p} \nabla \eta \cdot \nabla f \omega_{\phi}^{n} \\
& =\int_{X}-\frac{4}{p+1} f^{\frac{p+1}{2}} \nabla \eta \cdot \eta \nabla f^{\frac{p+1}{2}} \omega_{\phi}^{n} \\
& \leq \int_{X} \frac{2}{p+1}\left\{\delta \eta^{2}\left|\nabla f^{\frac{p+1}{2}}\right|^{2}+\delta^{-1} f^{p+1}|\nabla \eta|^{2}\right\} \omega_{\phi}^{n}
\end{aligned}$$

Then by taking $\delta=\frac{p}{p+1}$, we would end with the control
$$\int_{X} \eta^{2}\left|\nabla f^{\frac{p+1}{2}}\right|^{2} \omega_{\phi}^{n} \leq\left(\frac{p+1}{p}\right)^{2} \int_{X} f^{p+1}|\nabla \eta|^{2} \omega_{\phi}^{n} \leq 4 \int_{X} f^{p+1}|\nabla \eta|^{2} \omega_{\phi}^{n}$$

Since our manifold $\left(M, \omega_{\phi_{\epsilon}}\right)$ has a uniform positive lower bound on the Ricci curvature and uniform constant volume, we have a uniform Sobolev constant, which means:
$$\begin{aligned}
\left\{\int_{X}\left|\eta f^{\frac{p+1}{2}}\right|^{\frac{2 n}{n-1}} \omega_{\phi}^{n}\right\}^{\frac{n-1}{n}} & \leq C_{S} \int_{X}\left\{\eta^{2} f^{p+1}+\left|f^{\frac{p+1}{2}} \nabla \eta+\eta \nabla f^{\frac{p+1}{2}}\right|^{2}\right\} \omega_{\phi}^{n} \\
& \leq C_{S} \int_{X}\left\{\eta^{2} f^{p+1}+2\left(\eta^{2}\left|\nabla f^{\frac{p+1}{2}}\right|^{2}+f^{p+1}|\nabla \eta|^{2}\right)\right\} \omega_{\phi}^{n} \\
& \leq 10 C_{S} \int_{X}\left(\eta^{2}+|\nabla \eta|^{2}\right) f^{p+1} \omega_{\phi}^{n}
\end{aligned}$$

Now by taking a suitable cut-off function on the real line $\eta$ and compositing with the distance function on the manifold we get a cut-off function which satisfies $\eta \equiv 0$ outside the metric ball $B_{\phi}(R)$ and $\eta \equiv 1$ inside the metric ball $B_{\phi}(S)$ and $|\nabla \eta| \leq \frac{C}{R-S}$, plug in this cut-off function to the above inequality we get:
$$\|f\|_{L^{(p+1) \frac{n}{n-1}}\left(B_{\phi}\left(r_{1}\right)\right)} \leq\left(10 C_{S}\right)^{\frac{1}{p+1}}\left\{1+\frac{C}{(R-S)^{2}}\right\}^{\frac{1}{p+1}}\|f\|_{L^{p+1}\left(B_{\phi}\left(r_{2}\right)\right)}$$

The Moser Iteration technique uses $\gamma_{m}$ to replace $p+1$ in the above inequality and use the pair of radius $r_{m}=1+2^{-m}$ and $r_{m+1}$ to replace $R$ and $S$ on the $m$-th step, and eventually will end up with
$$\|f\|_{L^{\infty}\left(B_{\phi}(1)\right)} \leq C\|f\|_{L^{2}\left(B_{\phi}(2)\right)}$$

Since $\sigma_{\epsilon, \beta^{\prime}} \leq C\left(1+\left(|z|^{2}+\epsilon\right)^{\beta-1}\right) \leq C\left(|z|^{2}+\epsilon\right)^{\beta-1}$, the $L^{2}$ bound of $f$ on the unit $\omega_{\phi_{\epsilon}}$-metric ball is bounded by the following Lemma:

Lemma 5.
$$\begin{gathered}
\int_{B_{\phi_{\epsilon}}(p, 2)}\left|\log \sigma_{\epsilon, \beta^{\prime}}\right|^{2} \omega_{\phi_{\epsilon}}^{n} \leq C \int_{|z| \leq 2 \sqrt{C}}\left|\log \left(|z|^{2}+\epsilon\right)\right|^{2}\left(|z|^{2}+\epsilon\right)^{\beta-1} \sqrt{-1} \mathrm{~d} z \wedge \mathrm{~d} \bar{z} \leq C \\
\int_{B_{\phi_{\epsilon}}(p, 2)}\left|\log \sigma_{\epsilon, \beta^{\prime}}\right|\left(|z|^{2}+\epsilon\right)^{\beta-\beta^{\prime}} \omega_{\phi_{\epsilon}}^{n} \leq C \int_{|z| \leq 2 \sqrt{C}}\left|\log \left(|z|^{2}+\epsilon\right)\right|\left(|z|^{2}+\epsilon\right)^{2 \beta-\beta^{\prime}-1} \sqrt{-1} \mathrm{~d} z \wedge \mathrm{~d} \bar{z} \leq C \\
\int_{B_{\phi_{\epsilon}}(p, 2)}\left|\log \sigma_{\epsilon, \beta^{\prime}}\right|\left(|z|^{2}+\epsilon\right)^{\beta} \omega_{\phi_{\epsilon}}^{n} \leq C \int_{|z| \leq 2 \sqrt{C}}\left|\log \left(|z|^{2}+\epsilon\right)\right|\left(|z|^{2}+\epsilon\right)^{2 \beta-1} \sqrt{-1} \mathrm{~d} z \wedge \mathrm{~d} \bar{z} \leq C
\end{gathered}$$

Since $D$ is covered by finitely many coordinate balls $\mathcal{V}_{\alpha}$, and on each of those balls $t r_{\omega_{\beta^{\prime}, \epsilon}} \omega_{\phi_{\epsilon}} \leq C$. Comparing with the rough bound $C^{-1} \omega_{0} \leq \omega_{\phi_{\epsilon}} \leq C \frac{\omega_{0}}{\left(|z|^{2}+\epsilon\right)^{1-\beta}}$ achieved in Proposition 2, this yields us a finer control about the metric $\omega_{\phi_{\epsilon}}$ on the tangential direction. $\operatorname{tr}_{\omega_{\beta^{\prime}, \epsilon}} \omega_{\phi_{\epsilon}} \leq C$ implies that $\omega_{\phi_{\epsilon}} \leq C \omega_{\beta^{\prime}, \epsilon}$, thus we have uniform bound on the divisor direction $\lambda_{2}, \cdots, \lambda_{n} \leq C$. Combined with the previous rough bound $\lambda_{2}, \cdots, \lambda_{n} \geq C^{-1}$ and the asymptotic behavior of the volume form $\lambda_{1} \lambda_{2} \cdots \lambda_{n} \sim \frac{1}{\left(|z|^{2}+\epsilon\right)^{1-\beta}}$, we conclude that $\lambda_{1} \sim \frac{1}{\left(|z|^{2}+\epsilon\right)^{1-\beta}}$. Finally we get the desired uniform control about the metric $\omega_{\phi_{\epsilon}}$.

Theorem 2. For a uniform constant $C$, we have control $C^{-1} \omega_{\beta, \epsilon}^{\alpha} \leq \omega_{\phi_{\epsilon}} \leq C \omega_{\beta, \epsilon}^{\alpha}$ on $\mathcal{V}_{\alpha}$.
The standard Evans-Krylov theory outside $D$ gives us high order estimate of $\omega_{\phi_{\epsilon}}$ which will yield a smooth limit Kähler-Einstein metric on $X \backslash D$. By letting $\epsilon \rightarrow 0$ in the above theorem, we get the theorem:

Theorem 3. On a Fano manifold $X$, let $D$ is a smooth anti-canonical divisor, $\beta \in(0,1)$, if the twisted $K$-energy $E_{(1-\beta) D}$ is proper, then there exists a weak conical Kähler-Einstein metric in $c_{1}(X)$ with angle $2 \pi \beta$ along $D$.

\section*{4. General Current Equation}

On a quite general situation of compact Kähler manifolds, we could set up similar problem of prescribing Kähler-Einstein metrics on $X$ with conical singularities along a smooth hypersurface $D$. Pick a smooth background Kähler metric $\omega_{0}$ in a fixed cohomology class $\mathfrak{W}$, and suppose $\mathfrak{A}=c_{1}\left(L_{D}\right)$ satisfies the cohomological condition:
$$c_{1}(X)=\mu \mathfrak{W}+(1-\beta) \mathfrak{A}$$

Let
$$\operatorname{Ric}\left(\omega_{0}\right)=\mu \omega_{0}+(1-\beta) \alpha_{0}$$
where $\alpha_{0}$ is a smooth $(1,1)$ form in $\mathfrak{A}$ and it is the curvature form of some Hermitian metric $h$ on $L_{D}$. Let $S$ be holomorphic section of $L_{D}$ which defines $D$, and in $\mathfrak{A}$ we define a family of smooth $(1,1)$ form $\chi_{\epsilon}=\alpha_{0}+\sqrt{-1} \partial \bar{\partial} \log \left(|S|_{h}^{2}+\epsilon\right)$, notice that $\chi_{\epsilon}$ approaches the delta distribution $\chi$ along $D$ in the current sense as $\epsilon \rightarrow 0$. Moreover, as a $(1,1)$ form, $\chi_{\epsilon}$ has lower bound:
$$\begin{aligned}
\chi_{\epsilon}=\alpha_{0}+\sqrt{-1} \partial \bar{\partial} \log \left(|S|_{h}^{2}+\epsilon\right) & =\alpha_{0}+\sqrt{-1} \partial \frac{|S|_{h}^{2} \bar{\partial} \log |S|_{h}^{2}}{|S|_{h}^{2}+\epsilon} \\
& =\alpha_{0}+\frac{|S|_{h}^{2}}{|S|_{h}^{2}+\epsilon} \sqrt{-1} \partial \bar{\partial} \log |S|_{h}^{2}+\sqrt{-1} \frac{\epsilon}{|S|_{h}^{2}\left(|S|_{h}^{2}+\epsilon\right)^{2}} \partial|S|_{h}^{2} \wedge \bar{\partial}|S|_{h}^{2} \\
& \geq \alpha_{0}+\frac{|S|_{h}^{2}}{|S|_{h}^{2}+\epsilon}\left(-\alpha_{0}\right) \\
& =\frac{\epsilon}{|S|_{h}^{2}+\epsilon} \alpha_{0}
\end{aligned}$$
In order to solve the singular equation
$$\operatorname{Ric}(\omega)=\mu \omega+(1-\beta) \chi,$$
we first solve the smoothing equation instead,
$$\operatorname{Ric}\left(\omega_{\phi_{\epsilon}}\right)=\mu \omega_{\phi_{\epsilon}}+(1-\beta) \chi_{\epsilon}$$
and then consider the limit metric as $\epsilon \rightarrow 0$.
For any $\epsilon>0$, we could set up the Continuity Path $\star_{\epsilon}$ :
$$\operatorname{Ric}\left(\omega_{\phi_{\epsilon}(t)}\right)=(1-t)\left\{\mu \omega_{0}+(1-\beta) \alpha_{0}\right\}+t\left\{\mu \omega_{\phi_{\epsilon}(t)}+(1-\beta) \chi_{\epsilon}\right\}$$

The solvability of $\star_{\epsilon}$ is different for the cases $\mu<0, \mu=0$ and $\mu>0$ and the below section distincts them, and will be treated differently.

Case 1: $\mu<0$. By standard argument of Continuity Method, $\star_{\epsilon}$ could be solved up to $t=1$.

The openness part follows from the injectivity of the operator $\Delta_{\omega_{\phi_{\epsilon}(t)}}+t \mu$ since $\mu<0$.
The $C^{0}$ bound is by combining Maximum Principle to the equation
$$\omega_{\phi_{\epsilon}(t)}^{n}=e^{-t \mu \phi_{\epsilon}(t)+C_{\epsilon, t}} \frac{\omega_{0}^{n}}{\left(|S|_{h}^{2}+\epsilon\right)^{(1-\beta) t}}$$
and Kolodziej's $L^{p}$ estimate. Concretely speaking, first solve the equation for $t \in\left[0, \delta_{0}\right]$ by openness and then by considering the maximum point of $\phi_{\epsilon}(t)$ we know that
$$\sup e^{-t \mu \phi_{\epsilon}(t)+C_{\epsilon, t}} \leq \sup \left(|S|_{h}^{2}+\epsilon\right)^{(1-\beta) t} \leq M .$$

The right hand of the equation is uniform in $L^{p}$ therefore we could apply $L^{p}$ estimate to achive $C^{0}$ estimate for the potential $\phi_{\epsilon}(t)$. Eventually, we could solve the equation up to $t=1$ with uniform $C^{0}$ bound on $\phi_{\epsilon}$. And the higher order bound (depending on $\epsilon$ ) is obtained by Aubin.

Case 2: $\mu=0$. We use the smooth Calabi's conjecture instead of continuity method.
Theorem 4. Suppose $D$ is a smooth hypersurface in the Kähler manifold $X$, and $c_{1}(X)=$ $(1-\beta) c_{1}\left(L_{D}\right)$, then we have a weak Ricci flat Kähler metric with conical singularities of angle $2 \pi \beta$ in any Kähler class.

Proof. The equation $\omega_{\phi_{\epsilon}}^{n}=e^{h_{\omega_{0}}+C_{\epsilon}} \frac{\omega_{0}^{n}}{\left(|S|_{h}^{2}+\epsilon\right)^{1-\beta}}$, where $C_{\epsilon}$ is a normalization constant such that $\int_{X} \frac{e^{h_{\omega_{0}+C_{\epsilon}}}}{\left(|S|_{h}^{2}+\epsilon\right)^{1-\beta}} \omega_{0}^{n}=\int_{X} \omega_{0}^{n}=1$, could be solved by Yau's solution on the Calabi's Conjecture. The right hand side has uniform $L^{p}$ bound for $p<\frac{1}{1-\beta}$. Using Kolodziej's local estimate, we could get a uniform $C^{0}$ bound on the whole manifold.

From $C^{0}$ estimate to $C^{2}$ estimate the above technique could be used. $\operatorname{Ric}\left(\omega_{\phi_{\epsilon}}\right)=$ $(1-\beta) \alpha_{0}+(1-\beta) \sqrt{-1} \partial \bar{\partial} \log \left(|S|_{h}^{2}+\epsilon\right) \geq C(1-\beta) \omega_{0}$, then the Chern-Lu inequality (the version that $\operatorname{Ric}\left(\omega_{\phi}\right) \geq-C_{1} \omega_{\phi}-C_{2} \omega_{0}$, see Lemma 1) gives the rough estimate first. From this, the Ricci curvature is bounded form below since the rough bound $\omega_{\phi_{\epsilon}} \geq C^{-1} \omega_{0}$ tells that $\operatorname{tr}_{\omega_{\phi_{\epsilon}}} \omega_{0} \leq C$. At the same time, since the rough bound also gives the uniform diameter upper bound, we have uniform Sobolev constant. Then the technique used above could be applied to prove uniform $C^{2}$ estimate. \(\square\)

Remark 1. Ricci flat Kähler metric with conic singularities was first considered by Brendle under restrictions of the cone angle $\beta \in\left(0, \frac{1}{2}\right)$, see [1]. The above theorem removes the assumption on the cone angle while getting a Ricci flat Kähler metrics with conical singularities with weaker regularities than the result of Brendle [1], see Section 3 for discussions.

Case 3: $\mu>0$ is obstructed as before, the solvability need the Properness of the twisted K-Energy $E_{(1-\beta) \chi}$. In this situation, the smooth continuity method could also be solved up to $t=1$ with uniform $C^{0}$ estimate by the same reasoning explained in section 2 above.
Remark 2. The $C^{0}$ bound for the case $\mu<0$ and $\mu=0$ do not depend on positivity of D, which implies the rough estimate from which we could get the lower bound on the Ricci curvature therefore the uniform upper bound on the Sobolev constant. However, for $\mu>0$, from bound on $I-J$ to $C^{0}$ bound, we need the uniform Sobolev constant. That's why in the Main Theorem $c_{1}\left(L_{D}\right) \geq 0$ is assumed.

As soon as we have uniform $C^{0}$ bound on $\phi_{\epsilon}$ for equation (8), we are ready to prove the uniform $C^{2}$ estimate. Since $\chi_{\epsilon} \geq \frac{\epsilon}{|S|_{h}^{2}+\epsilon} \alpha_{0} \geq-C \omega_{0}, \operatorname{Ric}\left(\omega_{\phi_{\epsilon}}\right)=\mu \omega_{\phi_{\epsilon}}+(1-\beta) \chi_{\epsilon} \geq$ $\mu \omega_{\phi_{\epsilon}}-C(1-\beta) \omega_{0}$, the Chern-Lu inequality (See Lemma 1 above) gives the rough estimate. Afterwards, we could prove the differential inequality , since the essential part is the calculation of the lower bound of $\Delta_{\omega_{\beta, \epsilon}} \log \frac{|z|^{2}+\epsilon}{|z|^{2}+\epsilon e^{h}}$. And because $\sqrt{-1} \partial \bar{\partial} h=\alpha_{0}$ is a fixed smooth $(1,1)$ form, $h_{z \bar{z}}$ and $h_{z}$ is uniformly bounded, a similar argument tells us this quantity is bounded below by $-\frac{C}{|z|^{2}+\epsilon} \mathrm{d} z \wedge \mathrm{~d} \bar{z}-C \sum_{i} \mathrm{~d} z_{i} \wedge \mathrm{~d} \bar{z}_{i}$.

Another piece of information is the uniform Sobolev constants. The Ricci curvature is bounded below by $\mu-C(1-\beta)$ since $\operatorname{tr}_{\omega_{\phi_{\epsilon}}} \omega_{0} \leq C$ by the rough bound $\omega_{0} \leq C \omega_{\phi_{\epsilon}}$. The lower bound on the Ricci curvature together with the diameter upper bound (Lemma 3) and the constant volume gives us the uniform Sobolev constant, thus the a priori estimate on second derivative by local Moser Iteration goes through.

\section*{5. Regularity}

By studying Calabi's third order estimate, Brendle showed the regularity of Ricci-flat Kähler metrics he obtained under the assumption $\beta \in\left(0, \frac{1}{2}\right)$. In [8], the group of authors studied the a priori $C^{2, \alpha}$ estimate along the continuity path of conical singular Kähler metrics with edge and wedge calculus. And in [6], Calamai and Zheng adapted Evans-Krylov theory to the conical setting to prove the a priori $C^{2, \alpha}$ estimate for the continuity path of Kähler-Einstein metrics with conical singularities under a technical assumption that $\beta<\frac{2}{3}$. It is still interesting to know how to get the general regularity directly from the quasi-isometry condition, i.e. whether we could get some uniform Hölder estimate of $\omega_{\phi_{\epsilon}}$ with respect to the local model metric $\omega_{\beta, \epsilon}$ or third order estimate.

When $\beta=1$, the weak Kähler-Einstein metric is actually smooth as shown in the appendix of [5], the natural question is that whether it is smooth with respect to the background conical Kähler metric for the general conical angle $2 \pi \beta$, i.e. whether it is $C^{\alpha}$ in the singular coordinate around $D$ ?

\section*{References}
\begin{itemize}
\item[] [1] Simon Brendle, Ricci flat Kähler metrics with Edge Singularities. arXiv:1103.5454
\item[] [2] Frédéric Campana, Henri Guenancia and Mihai Păun, Metrics with cone singularities along normal crossing divisors and holomorphic tensor fields
\item[] [3] Xiuxiong Chen, Simon Donaldson and Song Sun, Kähler-Einstein metrics on Fano Manifolds, I: approximation of metrics with cone singularities.arXiv 1211.4566
\item[] [4] Xiuxiong Chen, Simon Donaldson and Song Sun, Kähler-Einstein metrics on Fano Manifolds, II: limits with cone angle less than $2 \pi$. arXiv 1212.4714.
\item[] [5] Xiuxiong Chen, Simon Donaldson and Song Sun, Kähler-Einstein metrics on Fano Manifolds, III: limits as cone angle approaches $2 \pi$ and completion of the main proof. arXiv:1302.0282.
\item[] [6] Simone Calamai, Kai Zheng,Geodesics in the Space of Kähler Cone Metrics. arXiv:1205.0056.
\item[] [7] Henri Guenancia, Mihai Păun, Conic singularities metrics with Prescribed Ricci curvature: The case of General cone angles along normal crossing divisors. arXiv:1307.6375.
\item[] [8] T.D. Jeffres, R. Mazzeo and Y. Rubinstein, Kähler-Einstein metrics with Edge singularities. arXiv:1105.5216.
\item[] [9] Chi Li and Song Sun, Conical Kähler Einstein metrics revisited, arXiv:1207.5011
\item[] [10] R.C. McOwen, Point Singularities and Conformal metrics on Riemann surfaces. Proc. Amer. Math. Soc.(103)1988, 224-204.
\item[] [11] Gábor Székelyhidi, Greatest lower bound on the Ricci curvature of Fano manifolds. Compos. Math. 147(2011), No. 1, 319-331.
\item[] [12] Gang Tian, Canonical Metrics on Kähler Manifolds, Birkhauser,1999.
\item[] [13] Gang Tian, Kähler-Einstein metrics on Algebraic Manifolds, in: Transcendental Method in Algebraic Geometry (Cetraro 1994) Lecture Notes in Math. 1644. pp. 143-185.
\item[] [14] M. Troyanov, Prescribing curvature on compact surfaces with conic singularities. Trans. Amer. Math. Soc. 324(1991), 793-821.
\item[] [15] Shing-Tung Yau: On the Ricci curvature of a compact Kähler manifold and the complex Monge-Ampère equation, $I^{*}$, Comm. Pure Appl. Math. 31 (1978) 339-441.
\end{itemize}
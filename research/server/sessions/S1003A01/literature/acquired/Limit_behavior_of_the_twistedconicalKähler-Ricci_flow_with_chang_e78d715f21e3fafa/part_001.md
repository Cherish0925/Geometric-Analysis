---
retention_scope: session
part: 1
total_parts: 2
---

[Part 1/2 of: Limit behavior of the twistedconicalKähler-Ricci flow with change in...]

---
source_file: 2406_04590.pdf
converter: mathpix
format: mmd
---

\title{
Limit behavior of the twisted conical Kähler-Ricci FLOW WITH CHANGE IN THE CONE ANGLE
}

\author{
Jiawei Liu and Xi Zhang
}

\begin{abstract}
In this paper, we study the limit behavior of the conical Kähler-Ricci flow as its cone angle tends to zero. More precisely, we prove that as the cone angle tends to zero, the conical Kähler-Ricci flow converges to a unique Kähler-Ricci flow, which is smooth outside the divisor and admits cusp singularity along the divisor.
\end{abstract}

\section*{Contents}
1. Introduction ..... 1
2. Preliminaries ..... 5
3. Uniform estimates on metric potentials ..... 12
4. High order uniform estimates ..... 19
5. Existence ..... 22
6. Uniqueness ..... 29
References ..... 33

\section*{1. Introduction}

Ricci flow was first introduced by Hamilton [25] in 1980s, which has many applications in differential geometry and topology. For example, Perelman [51, 52] gave a solution to the Poincaré conjecture, and Brendle-Schoen [5] proved the differentiable sphere theorem via Ricci flow. Then Cao [6] introduced Ricci flow to the Kähler manifold, which was called Kähler-Ricci flow, to give a parabolic proof of the Calabi-Yau theorem. The general existence of Kähler-Ricci flow was given by Tsuji [71] and Tian-Zhang [67]. Later, Lott-Zhang [43, 44] showed that the Kähler-Ricci flows can come from some singular metrics on quasi-projective manifold and that the flows keep the singularities of the initial metrics. Song-Tian [57] proved that the Kähler-Ricci flow can come from a weak metric whose potential is only continuous and then immediately smoothes it. Székelyhidi-Tosatti [60] generalized this result to a more general kind of complex Monge-Ampère flow, and as an application they gave the regularity result on the corresponding complex Monge-Ampère equation. Moreover, Phong-Sturm [49], Phong-Sesum-Sturm [46], Tian-Zhu [68, 69], Phong-Song-Sturm-Weinkove [47, 48], Székelyhidi [59], Tosatti [70], Tian-Zhang-Zhang-Zhu [65], Song-Tian

\footnotetext{
2020 Mathematics Subject Classification. 53E30, 35K96, 35K67.
Key words and phrases. Kähler-Ricci flow, conical singularity, cusp singularity.
X. Zhang is supported by National Key R and D Program of China 2020YFA0713100, NSFC (Grant Nos. 12141104 and 11721101). J.W. Liu is supported by NSFC (Grant No.12371059), Jiangsu Specially-Appointed Professor Program, Fundamental Research Funds for the Central Universities, and partially supported by Special Priority Program SPP 2026 "Geometry at Infinity" from the German Research Foundation (DFG).
}
[57], Berman-Boucksom-Eyssidieux-Guedj-Zeriahi [3], Dervan-Székelyhidi [18] and Jian-Song-Tian [27]etc. contributed many important results on the convergence of Kähler-Ricci flow. In recent years, the most significant work is the solution of Hamilton-Tian's conjecture [62], which has been proved by Tian-Zhang [66], Bamler [1], Chen-Wang [12] and Wang-Zhu [72].

As a generalization of the Kähler-Ricci flow, the twisted Kähler-Ricci flow which adds a smooth twisted form in Kähler-Ricci flow was first studied by Collins-Székelyhidi [16] and the first author [34]. By using some new arguments, Guedj-Zeriahi [23] and Di Nezza-Lu [19] gave the best regularity and uniqueness results of this flow starting from weak metric which only admits zero Lelong number. Recently, Zhang [74] proved Tian's partial $C^{0}$-estimate along this flow, and the authors [41] showed the relation between the convergence of these flows and the greatest Ricci lower bound.

When adding a non-smooth twisted form in Kähler-Ricci flow, more precisely, the twisted form is only a current of the integration along a divisor with positive coefficient less than 1, such flow was called conical Kähler-Ricci flow which was first introduced by Jeffres-Mazzeo-Rubinstein [26]. Then Chen-Wang [13, 14], the authors [37], Wang [73] and Shen [56] studied its existence when is comes from a class of conical Kähler metrics or a specific one. Later, the authors [38] and the first author and Zhang [36] extended the initial metic to the weak one as in [57, 60], and Li-Shen-Zheng [32] extended this result to the weak initial metric which only admits $L^{\infty}$-potential on $\log$ canonical pairs. Recently, the authors and Zhang [42] studied this flow coming from the weakest initial metric whose Lelong number is zero, which generalized the results on smooth Kähler-Ricci flow proved by Guedj-Zeriahi [23] and Di Nezza-Lu [19] to the conical case. For the convergence and geometric properties along this flow, see [21, 22, 50, 55, 75, 76, 40] for more details.

The conical Kähler-Ricci flow was introduced to study the conical Kähler-Einstein metric which plays an important role in the solution of Yau-Tian-Donaldson conjecture. Such metrics exist for all small cone angles, which was conjectured by Donaldson [20] and proved by Berman [2] and Li-Sun [33] (see also [35, 40]). So how large the cone angle can be, and what the limit behavior of this metric should be as its cone angle tends to the critical value are important and interesting problems. On the first question, if it can be related to some geometric invariant, Song-Wang [58] did important work is this subject. And from the proof of Yau-Tian-Donaldson conjecture [63, 9, 10, 11], if the Fano manifold is $K$-stable, then the conical Kähler-Einstein metric converges to the smooth Kähler-Einstein metric as its cone angle tends to $2 \pi$. On the other hand, Tian [61] anticipated that the complete Tian-Yau Kähler-Einstein metric on the complement of a divisor should be the limit of the conical Kähler-Einstein metric as cone angle tend to zero, and Cheltsov-Rubinstein [8] gave a more general conjecture. Guenancia [24] and Rubinstein-Zhang [53, 54] contributed many important work in this research. Especially, by introducing new ideas and techniques, Biquard-Guenancia [4] creatively solved Tian's conjecture in Fano and some twisted canonical line bundles being ample cases.

For the conical Kähler-Ricci flow itself, it exits for all cone angles belonging to 0 to $2 \pi$, and it converges to the smooth Kähler-Ricci flow as its cone angle tends to $2 \pi$ because there is a positive lower bound on the cone angel in this case and so the uniform estimates can be obtained directly (see [37, 73, 56]). A natural question is what the limit behavior of the conical Kähler-Ricci flow should be as its cone angle tends to zero. As we know, only the authors [39] proved that the conical Kähler-Ricci flow with a specific initial metric admitting conical singularity converges to a cusp Kähler-Ricci flow with a cusp Kähler metric as its initial metric as the cone angle tends to zero if the twisted canonical line bundle $K_{X}+L_{D}$ is ample. The key point is that the authors observe that the singularity term can be combined with the metric potential to be viewed as a whole, which can be controlled uniformly when they choose a specific initial metric. But unfortunately, this method does not work in general case.

In this paper, we study the limit behavior of the twisted conical Kähler-Ricci flow as its cone angle tends to zero in general case. Let $(X, \omega)$ be a compact Kähler manifold with complex
dimension $n$ and $D$ be a smooth divisor. Assume that $\hat{\omega} \in[\omega]$ is a positive closed current with potential $\varphi_{0} \in L^{\infty}(X) \cap \operatorname{PSH}(\mathrm{X}, \omega)$ and that $\eta$ is a smooth closed (1,1)-form. The twisted conical Kähler-Ricci flow with initial metric $\hat{\omega}$ is given as
$$\left\{\begin{array}{l}
\frac{\partial \omega_{\gamma}(t)}{\partial t}=-\operatorname{Ric}\left(\omega_{\gamma}(t)\right)+(1-\gamma)[D]+\eta \\
\left.\omega_{\gamma}(t)\right|_{t=0}=\hat{\omega}
\end{array},\right.$$
where $[D]$ is the current of integration along $D$. Denote
$$T_{\gamma, \max }^{\eta}=\sup \left\{t \geqslant 0 \mid[\omega]+t\left(-c_{1}(X)+(1-\gamma) c_{1}\left(L_{D}\right)+[\eta]\right) \geqslant 0\right\},$$
where $L_{D}$ is the line bundle associated with divisor $D$. From Li-Shen-Zheng's [32] result (see the authors' [42] result for more general case), we see that there exists a unique solution to the twisted Kähler-Ricci flow $\left(C K R F_{\gamma}^{\eta}\right)$ on $\left[0, T_{\gamma, \max }^{\eta}\right) \times X$ in the sense of Definition 2.4.

By introducing some new ideas, here we give the following characterization of the limit behavior of the twisted conical Kähler-Ricci flow as its cone angle tends to zero.

Theorem 1.1. As the cone angle tends to 0, the twisted conical Kähler-Ricci flow $\left(C K R F_{\gamma}^{\eta}\right)$ converges locally in the smooth sense outside the divisor and globally in the sense of currents to a Kähler-Ricci flow
$$\left\{\begin{array}{l}
\frac{\partial \omega(t)}{\partial t}=-\operatorname{Ric}(\omega(t))+[D]+\eta \\
\left.\omega(t)\right|_{t=0}=\hat{\omega}
\end{array},\right.$$
which exists on $\left[0, T_{\text {max }}^{\eta}\right) \times X$ in the following sense.
\begin{itemize}
\item[-] For any $0<T<T_{\text {max }}^{\eta}$, there exists a constant $C$ such that for any $t \in(0, T)$,
$$e^{-\frac{C}{t^{2}}} \omega_{o} \leqslant \omega(t) \leqslant e^{\frac{C}{t^{2}}} \omega_{o} \quad \text { in } \quad X \backslash D ;$$
\item[-] In $\left(0, T_{\text {max }}^{\eta}\right) \times(X \backslash D), \omega(t)$ satisfies the smooth twisted Kähler-Ricci flow
$$\frac{\partial \omega(t)}{\partial t}=-\operatorname{Ric}(\omega(t))+\eta ;$$
\item[-] On $\left(0, T_{\max }^{\eta}\right) \times X, \omega(t)$ satisfies Kähler-Ricci flow $\left(C K R F_{0}^{\eta}\right)$ in the sense of currents;
\item[-] There exists a metric potential $\varphi(t) \in \mathcal{C}^{\infty}\left(\left(0, T_{\max }^{\eta}\right) \times(X \backslash D)\right)$ with respect to $\omega_{t}$ such that $\omega(t)=\omega_{t}+\sqrt{-1} \partial \bar{\partial} \varphi(t)$,
$$\lim _{t \rightarrow 0^{+}}\left\|\varphi(t)-\varphi_{0}\right\|_{L^{1}(X)}=0 \quad \text { and } \quad \lim _{t \rightarrow 0^{+}} \varphi(t)=\varphi_{0} \quad \text { in } \quad X \backslash D ;$$
\item[-] $O n\left[0, T_{\text {max }}^{\eta}\right),\left\|\varphi(t)-t \psi_{o}\right\|_{L^{\infty}(X)} \leqslant C$;
\item[-] For any $0<T<T_{\text {max }}^{\eta}$, there exist constants a and $C$ such that for any $t \in(0, T)$,
$$-C+a \log t \leqslant \dot{\varphi}(t)-\psi_{o} \leqslant \frac{C}{t} ;$$
\end{itemize}
where $\omega_{o}$ and $\psi_{o}$ are a cusp Kähler metric and its metric potential coming from (2.30) and (2.31) respectively, $\omega_{t}$ comes from (2.10), and
$$T_{\max }^{\eta}=\sup \left\{t \geqslant 0 \mid[\omega]+t\left(-c_{1}(X)+c_{1}\left(L_{D}\right)+[\eta]\right) \geqslant 0\right\} .$$

As is well known, the key steps in showing the limit behavior of the twisted conical Kähler-Ricci flow $\left(C K R F_{\gamma}^{\eta}\right)$ as cone angle tends to zero are to derive uniform estimates which do not depend on $\gamma$ on this flow. But it seems not to be easy. A conical Kähler metric with cone angle $2 \pi \gamma$ along
divisor is $L^{p_{\gamma}}$-integrable with $p_{\gamma} \in\left(1, \frac{1}{1-\gamma}\right)$, so for any fix $\gamma>0$, we can use the classical results in partial differential equations, such as Kołodziej's $L^{p}$-estimate and stability theorem [29, 30] etc, to derive the estimates on the twisted conical Kähler-Ricci flow $\left(C K R F_{\gamma}^{\eta}\right)$ and its smooth approximation sequence (see [37, 38, 73, 56] for more details). But all above estimates depend on $\gamma$ and will converge to $\infty$ as $\gamma$ tends to zero. In addition, since there is no available theory for complex Monge-Ampère equation with $L^{1}$ right hand side, and also $\omega_{\gamma}(t)$ may converge to a non-integrable current, there is no direct results that can be applied to derive the uniform estimates (independent of $\gamma$ ) on the twisted conical Kähler-Ricci flow $\left(C K R F_{\gamma}^{\eta}\right)$ with sufficiently small positive $\gamma$. Therefore, we need some new arguments to prove the uniform estimates on the twisted conical Kähler-Ricci flow when we consider its limit behavior .

In order to overcome above difficulties, we introduce some new ideas to derive the uniform estimates on the twisted conical Kähler-Ricci flow $\left(C K R F_{\gamma}^{\eta}\right)$ with sufficiently small positive $\gamma$. In this process, a special function (see (2.23)), thanks to Guenancia [24], which is a metric potential for conical Kähler metric and converges to the potential of a cusp Kähler metric, plays an important role. More precisely, by using Guenancia's function, we construct a special super-solution to derive a uniform upper bound on the potential of $\omega_{\gamma}(t)$. Then we obtain the uniform lower bound on the potential in a short time by writing the parabolic Monge-Ampère equation as an elliptic one and by proving a uniform upper bound on the time derivative of potential. At last, by constructing a new auxiliary function, we successively obtain the uniform lower bound on the time derivative of potential, which implies a uniform lower bound on the potential for any time. Combining all these estimates together, we prove the uniform Laplacian $\mathcal{C}^{2}$-estimate by introducing a new auxiliary function again, and then we show the convergence of the twisted conical Kähler-Ricci flow in the subsequence sense as the cone angle tends to zero. Moreover, since the limit behavior of the twisted conical Kähler-Ricci flow near the initial time depends on $\gamma$, we can not let $\gamma$ tends to zero directly when we consider the limit behavior of the limit flow near the initial time. Our method of studying this is to construct sub-solution and super-solution and then study the limit behavior of these solutions. Furthermore, by drawing inspiration from Di Nezza-Lu's [19] uniqueness theorem on smooth Kähler-Ricci flow with weak initial metric (see also the author's work [42] for the conical case), we prove a uniqueness theorem for the Kähler-Ricci flow with cusp singularity along the divisor $D$, which implies that the limit flow of above convergence is unique.

As a corollary of Theorem 1.1, we give the following existence and uniqueness result.
Corollary 1.2. There exists a unique weak solution to the twisted cusp Kähler-Ricci flow on $\left[0, T_{\text {max }}^{\eta}\right) \times X$ in the sense of Theorem 1.1.

The smooth Kähler-Ricci flow with singularity along a divisor in quasi-projective manifold $X \backslash D$ was first studied by Lott-Zhang [43, 44]. They thoroughly studied the existence and convergence of Kähler-Ricci flow whose initial metric is finite volume Kähler metric with "superstandard spatial asymptotics" (Definition 8.10 in [43]), and they gave some interesting examples. Their flow keeps "superstandard spatial asymptotics" and this type of metrics contain cusp Kähler metrics. Then the authors [39] studied the Kähler-Ricci flow with cusp singularity along a divisor on $X$ globally by approximating a sequence of conical Kähler-Ricci flows as their cone angles tend to zero in the case that the twisted canonical line bundle $K_{X}+L_{D}$ is ample, and later Chau-Li-Shen [7] generalized Lott-Zhang's [43] results to more general initial metric, which means that the smooth Kähler-Ricci flow with cusp singularity along a divisor in $X \backslash D$ can start from a metric without cusp singularity. Recently, Li-Shen-Zheng [32] constructed a maximal solution (in the sense of potential) to the Kähler-Ricci flow $\left(C K R F_{0}^{\eta}\right)$ on $\left[0, T_{\text {max }}^{\eta}\right) \times X$ in the sense of Definition 5.7. However it is not clear whether their maximal solution is the unique one to the Kähler-Ricci flow $\left(C K R F_{0}^{\eta}\right)$. Here we prove that the solution is indeed unique.

The paper is organized as follows. We first give the definition and some known results of the twisted conical Kähler-Ricci flow, and we prove some maximum principles in section 2. Then we prove the uniform estimates including the $\mathcal{C}^{0}$-estimates on metric potentials and its time derivative in section 3. In section 4, we prove the uniform Laplacian $\mathcal{C}^{2}$ and high order estimates. We then show the limit behavior of the conical Kähler-Ricci flow as the cone angle tends to zero, and we give the existence of the limit flow in section 5. At the last section, we prove a uniqueness theorem for the Kähler-Ricci flow with cusp singularity along the divisor.

\section*{2. Preliminaries}

In this section, we recall some definitions and results on the twisted conical Kähler-Ricci flow, and then we prove some maximum principles for the equations with conical singularity.

Let $(X, \omega)$ be a compact Kähler manifold with complex dimension $n$ and $D$ be a smooth divisor with definition section $s$, that is, $D=\{s=0\}$. Assume that $\hat{\omega} \in[\omega]$ is a positive closed current with potential $\varphi_{0} \in L^{\infty}(X) \cap \operatorname{PSH}(\mathrm{X}, \omega)$, that is,
$$\hat{\omega}=\omega+\sqrt{-1} \partial \bar{\partial} \varphi_{0} .$$
The twisted conical Kähler-Ricci flow with twisted form $\eta$ which is a smooth closed (1,1)-form is as follows
$$\left\{\begin{array}{l}
\frac{\partial \omega_{\gamma}(t)}{\partial t}=-\operatorname{Ric}\left(\omega_{\gamma}(t)\right)+(1-\gamma)[D]+\eta \\
\left.\omega_{\gamma}(t)\right|_{t=0}=\hat{\omega}
\end{array} .\right.$$
Denote
$$T_{\max }^{\eta}=\sup \left\{t \geqslant 0 \mid[\omega]+t\left(-c_{1}(X)+c_{1}\left(L_{D}\right)+[\eta]\right) \geqslant 0\right\},$$
where $L_{D}$ is the line bundle associated with divisor $D$.
For any $T<T_{\text {max }}^{\eta}$, there exists a smooth volume form $\Omega$ such that
$$\omega_{t}=\omega+t(-\operatorname{Ric}(\Omega)+\theta+\eta)>0$$
for all $t \in[0, T]$, where $\theta$ is the curvature of a smooth Hermitian metric $h$ on $L_{D}$. In fact, since
$$[\omega]+T\left(-c_{1}(X)+c_{1}\left(L_{D}\right)+[\eta]\right)>0,$$
there exists a smooth positive closed (1, 1)-form
$$\kappa \in[\omega]+T\left(-c_{1}(X)+c_{1}\left(L_{D}\right)+[\eta]\right) .$$
For any $t \in[0, T]$, we denote
$$\omega_{t}=\omega+\frac{t}{T}(\kappa-\omega)=\left(1-\frac{t}{T}\right) \omega+\frac{t}{T} \kappa .$$
It is obvious that $\omega_{t}$ is positive and
$$\omega_{t} \in[\omega]+t\left(-c_{1}(X)+c_{1}\left(L_{D}\right)+[\eta]\right) .$$

On the other hand, since
$$-\frac{1}{T}(\kappa-\omega)+\theta+\eta \in c_{1}(X)$$
is a smooth closed (1,1)-form, by Calabi-Yau theorem, there exists a smooth volume form $\Omega$ such that
$$\operatorname{Ric}(\Omega)=-\frac{1}{\mathrm{~T}}(\kappa-\omega)+\theta+\eta,$$
which implies that for any $t \in[0, T]$,
$$\omega_{t}=\omega+t(-\operatorname{Ric}(\Omega)+\theta+\eta) .$$

It is obvious that there is a constant $C>1$ depending only on $T, \theta, \eta$ and $\omega$ such that
$$\frac{1}{C} \omega \leqslant \omega_{t} \leqslant C \omega$$
for all $t \in[0, T]$. We denote
$$\Omega=e^{-h} \omega^{n} \quad \text { and } \quad \omega_{t}=\omega+t \nu,$$
where
$$\nu=-\operatorname{Ric}(\Omega)+\theta+\eta .$$
Then we can write the flow $\left(C K R F_{0}^{\eta}\right)$ as the following parabolic Monge-Ampère equation
$$\left\{\begin{array}{l}
\frac{\partial \varphi(t)}{\partial t}=\log \frac{\left(\omega_{t}+\sqrt{-1} \partial \bar{\partial} \varphi(t)\right)^{n}}{\omega^{n}}+h+\log |s|_{h}^{2} \\
\left.\varphi(t)\right|_{t=0}=\varphi_{0}
\end{array} .\right.$$
We denote
$$T_{\gamma, \max }^{\eta}=\sup \left\{t \geqslant 0 \mid[\omega]+t\left(-c_{1}(X)+(1-\gamma) c_{1}\left(L_{D}\right)+[\eta]\right) \geqslant 0\right\} .$$
For any $T<T_{\text {max }}^{\eta}$, there holds $T<T_{\gamma, \text { max }}^{\eta}$ and
$$\omega_{\gamma t}:=\omega_{t}-\gamma t \theta=\omega+t(-\operatorname{Ric}(\Omega)+(1-\gamma) \theta+\eta)>0$$
for all $t \in[0, T]$ and $0<\gamma \ll 1$ sufficiently small. From (2.11), there also exists a large constant $C>1$ depending only on $\omega, T, \theta$ and $\eta$ such that
$$\frac{1}{C} \omega \leqslant \omega_{\gamma t} \leqslant C \omega$$
for all $t \in[0, T]$ and $0<\gamma \ll 1$. If we denote
$$\nu_{\gamma}=-\operatorname{Ric}(\Omega)+(1-\gamma) \theta+\eta=\nu-\gamma \theta,$$
then
$$\omega_{\gamma t}=\omega+t \nu_{\gamma},$$
and the twisted conical Kähler-Ricci flow $\left(C K R F_{\gamma}^{\eta}\right)$ can be written as equation
$$\left\{\begin{array}{l}
\frac{\partial \varphi_{\gamma}(t)}{\partial t}=\log \frac{\left(\omega_{\gamma t}+\sqrt{-1} \partial \bar{\partial} \varphi_{\gamma}(t)\right)^{n}}{\omega^{n}}+h+(1-\gamma) \log |s|_{h}^{2} \\
\left.\varphi_{\gamma}(t)\right|_{t=0}=\varphi_{0}
\end{array} .\right.$$

Definition 2.1. By saying a closed positive (1,1)-current $\omega$ with locally bounded potential is a conical Kähler metric with cone angle $2 \pi \gamma(0<\gamma \leqslant 1)$ along $D$, we mean that $\omega$ is a smooth Kähler metric in $M \backslash D$. And near each point $p \in D$, there exists a local holomorphic coordinate $\left(z_{1}, \cdots, z_{n}\right)$ in a neighborhood $U$ of $p$ such that $D=\left\{z_{n}=0\right\}$ and that $\omega$ is asymptotically equivalent to the model conical metric
$$\sum_{j=1}^{n-1} \sqrt{-1} d z_{j} \wedge d \bar{z}_{j}+\frac{\sqrt{-1} d z_{n} \wedge d \bar{z}_{n}}{\left|z_{n}\right|^{2(1-\gamma)}} \quad \text { on } \quad U$$

In this paper, we always choose Guenancia's metric (Lemma 3.1 in [24])
$$\begin{aligned}
\omega_{\gamma} & =\omega+\sqrt{-1} \partial \bar{\partial} \psi_{\gamma} \\
& =\omega+\frac{\gamma^{2}\left\langle D^{\prime} s, D^{\prime} s\right\rangle}{|s|_{h}^{2(1-\gamma)}\left(1-|s|_{h}^{2 \gamma}\right)^{2}}-\frac{\gamma|s|_{h}^{2 \gamma}}{1-|s|_{h}^{2 \gamma}} \theta
\end{aligned}$$
as the model conical Kähler metric, where
$$\psi_{\gamma}=-\log \left(\frac{1-|s|_{h}^{2 \gamma}}{\gamma}\right)^{2}$$
and $D^{\prime}$ is the $(1,0)$ part of the Chern connection of the line bundle $L_{D}$ with Hermitian metric $h$. Since function $f(t)=\frac{\gamma t^{\gamma}}{1-t^{\gamma}}$ increases with respect to $t \in[0,1)$, after rescaling $h$ such that $|s|_{h}^{2}<\delta$, we have
$$0 \leqslant \frac{\gamma|s|_{h}^{2 \gamma}}{1-|s|_{h}^{2 \gamma}} \leqslant \frac{\gamma \delta^{\gamma}}{1-\delta^{\gamma}} \rightarrow-\frac{1}{\log \delta} \quad \text { as } \gamma \rightarrow 0,$$
which implies that
$$0 \leqslant \frac{\gamma|s|_{h}^{2 \gamma}}{1-|s|_{h}^{2 \gamma}} \leqslant-\frac{2}{\log \delta} \quad \text { for } \quad 0<\gamma \ll 1,$$
and so
$$\sqrt{-1} \partial \bar{\partial} \psi_{\gamma}=\frac{\gamma^{2}\left\langle D^{\prime} s, D^{\prime} s\right\rangle}{|s|_{h}^{2(1-\gamma)}\left(1-|s|_{h}^{2 \gamma}\right)^{2}}-\frac{\gamma|s|_{h}^{2 \gamma}}{1-|s|_{h}^{2 \gamma}} \theta \geqslant-\frac{\gamma|s|_{h}^{2 \gamma}}{1-|s|_{h}^{2 \gamma}} \theta \geqslant \frac{2 C}{\log \delta} \omega$$
for $0<\gamma \ll 1$, where $C$ is a positive constant satisfying $\theta \leqslant C \omega$. Therefore, if we choose $0<\delta \ll 1$ such that
$$\sqrt{-1} \partial \bar{\partial} \psi_{\gamma} \geqslant-\frac{1}{8(C-1)} \omega,$$
where $C$ comes from (2.17), then there holds
$$\omega_{\gamma}=\omega+\sqrt{-1} \partial \bar{\partial} \psi_{\gamma} \geqslant\left(1-\frac{1}{8(C-1)}\right) \omega \geqslant \frac{1}{2} \omega$$
for $0<\gamma \ll 1$. From Guenancia's arguments in [24], we know that there exists a uniform constant $C$ independent of $\gamma$ such that
$$\left.\left.\left|\log \frac{\omega_{\gamma}^{n}}{\omega^{n}}+(1-\gamma) \log \right| s\right|_{h} ^{2}-\psi_{\gamma} \right\rvert\, \leqslant C .$$
Moreover, from the authors' observation (Proposition 2.8 in [39]), $\psi_{\gamma}$ is monotone decreasing to $\psi_{o}$ as $\gamma \searrow 0^{+}$. Hence $\omega_{\gamma}$ converges in $\mathcal{C}_{\text {loc }}^{\infty}$-topology in $X \backslash D$ to a Kähler metric
$$\begin{aligned}
\omega_{o} & =\omega+\sqrt{-1} \partial \bar{\partial} \psi_{o} \\
& =\omega+\frac{\left\langle D^{\prime} s, D^{\prime} s\right\rangle}{|s|_{h}^{2} \log ^{2}|s|_{h}^{2}}+\frac{1}{\log |s|_{h}^{2}} \theta
\end{aligned}$$
as $\gamma$ tends to 0, and
$$-\log \log ^{2}|s|_{h}^{2}=\psi_{o} \leqslant \psi_{\gamma} \leqslant \psi_{1}=-\log \left(1-|s|_{h}^{2}\right)^{2} .$$
So there exists a uniform constant $C$ depending only on $\omega, \theta$ and $T$ such that
$$\psi_{\gamma} \leqslant C \quad \text { on } \quad X .$$

Remark 2.2. In fact, $\omega_{o}$ is a cusp Kähler metric in the following sense.
Definition 2.3. By saying a closed positive (1, 1)-current $\omega$ is a cusp Kähler metric along $D$, we mean that $\omega$ is a smooth Kähler metric in $M \backslash D$. And near each point $p \in D$, there exists a local holomorphic coordinate $\left(z_{1}, \cdots, z_{n}\right)$ in a neighborhood $U$ of $p$ such that $D=\left\{z_{n}=0\right\}$ and that $\omega$ is asymptotically equivalent to the model cusp metric
$$\sqrt{-1} \sum_{j=1}^{n-1} d z_{j} \wedge d \bar{z}_{j}+\frac{\sqrt{-1} d z_{n} \wedge d \bar{z}_{n}}{\left|z_{n}\right|^{2} \log ^{2}\left|z_{n}\right|^{2}} \quad \text { on } \quad U .$$

Combining (2.27), (2.28) with (2.17), we also have
$$\omega_{\gamma t}+\sqrt{-1} \partial \bar{\partial} \psi_{\gamma} \leqslant C \omega+\sqrt{-1} \partial \bar{\partial} \psi_{\gamma}=(C-1) \omega+\omega_{\gamma} \leqslant(2 C-1) \omega_{\gamma}$$
and
$$\begin{aligned}
\omega_{\gamma t}+\sqrt{-1} \partial \bar{\partial} \psi_{\gamma} & \geqslant \frac{1}{C} \omega+\sqrt{-1} \partial \bar{\partial} \psi_{\gamma}=\frac{1}{C} \omega_{\gamma}+\left(1-\frac{1}{C}\right) \sqrt{-1} \partial \bar{\partial} \psi_{\gamma} \\
& \geqslant \frac{1}{2 C} \omega_{\gamma}+\frac{1}{4 C} \omega+\left(1-\frac{1}{C}\right) \sqrt{-1} \partial \bar{\partial} \psi_{\gamma} \\
& \geqslant \frac{1}{2 C} \omega_{\gamma}+\frac{1}{4 C} \omega-\left(1-\frac{1}{C}\right) \frac{1}{8(C-1)} \omega \\
& =\frac{1}{2 C} \omega_{\gamma}+\frac{1}{8 C} \omega .
\end{aligned}$$
Therefore, there exists a uniform constant $C$ depending only on $\omega, \theta, \eta$ and $T$ such that for any $0<\gamma \ll 1$, we have
$$\frac{1}{C} \omega_{\gamma} \leqslant \omega_{\gamma t}+\sqrt{-1} \partial \bar{\partial} \psi_{\gamma} \leqslant C \omega_{\gamma} \quad \text { in } \quad X \backslash D .$$

Definition 2.4. Assume that $\hat{\omega} \in[\omega]$ is a positive closed current with potential $\varphi_{0} \in L^{\infty}(X)$ (or more general, $\hat{\omega} \in[\omega]$ is a positive closed current with zero Lelong number). By saying $\omega_{\gamma}(t)$ is a weak solution to the twisted conical Kähler-Ricci flow $\left(C K R F_{\gamma}^{\eta}\right)$ with initial metric $\hat{\omega}$ on $\left(0, T^{\prime}\right) \times X$, we mean that it satisfies the following conditions.
\begin{itemize}
\item[-] For any $0<\delta<T<T^{\prime}$, there exists a constant $C$ such that for any $t \in(\delta, T)$,
$$C^{-1} \omega_{\gamma} \leqslant \omega_{\gamma}(t) \leqslant C \omega_{\gamma} \quad \text { in } \quad X \backslash D ;$$
\item[-] In $\left(0, T^{\prime}\right) \times(X \backslash D), \omega_{\gamma}(t)$ satisfies the smooth twisted Kähler-Ricci flow
$$\frac{\partial \omega_{\gamma}(t)}{\partial t}=-\operatorname{Ric}\left(\omega_{\gamma}(t)\right)+\eta ;$$
\item[-] On $\left(0, T^{\prime}\right) \times X, \omega_{\gamma}(t)$ satisfies equation $\left(C K R F_{\gamma}^{\eta}\right)$ in the sense of currents;
\item[-] There exists a metric potential $\varphi_{\gamma}(t) \in \mathcal{C}^{2, \alpha, \gamma}(X) \cap \mathcal{C}^{\infty}(X \backslash D)$ such that $\omega_{\gamma}(t)=\omega_{\gamma t}+$ $\sqrt{-1} \partial \bar{\partial} \varphi_{\gamma}(t)$,
$$\lim _{t \rightarrow 0^{+}}\left\|\varphi_{\gamma}(t)-\varphi_{0}\right\|_{L^{1}(X)}=0 \quad \text { and } \quad \lim _{t \rightarrow 0^{+}} \varphi_{\gamma}(t)=\varphi_{0} \quad \text { in } \quad X \backslash D .$$
\end{itemize}

Remark 2.5. By saying a function $\phi \in \mathcal{C}^{2, \alpha, \gamma}(X)$, we mean that $\phi$ is a $\mathcal{C}^{2, \alpha}$-function with respect to $\omega_{\gamma}$.

Definition 2.6. We call $\phi(t) \in \mathcal{C}^{2, \alpha, \gamma}(X) \cap \mathcal{C}^{\infty}(X \backslash D)$ a weak solution to equation (2.20) with initial value $\phi_{0} \in L^{\infty}(X) \cap \operatorname{PSH}(X, \omega)$ on $\left(0, T^{\prime}\right) \times X$ if $\phi(t)$ satisfies the following conditions.
\begin{itemize}
\item[-] For $0<\delta<T<T^{\prime}$, there exists a constant $C$ such that for any $t \in(\delta, T)$,
$$C^{-1} \omega_{\gamma} \leqslant \omega_{\gamma t}+\sqrt{-1} \partial \bar{\partial} \phi(t) \leqslant C \omega_{\gamma} \quad \text { in } \quad X \backslash D ;$$
\item[-] In $\left(0, T^{\prime}\right) \times(X \backslash D), \phi(t)$ satisfies equation
$$\frac{\partial \phi(t)}{\partial t}=\log \frac{\left(\omega_{\gamma t}+\sqrt{-1} \partial \bar{\partial} \phi(t)\right)^{n}}{\omega^{n}}+h+(1-\gamma) \log |s|_{h}^{2} ;$$
\item[-] $\lim _{t \rightarrow 0^{+}}\left\|\phi(t)-\phi_{0}\right\|_{L^{1}(X)}=0$ and $\lim _{t \rightarrow 0^{+}} \phi(t)=\phi_{0}$ in $X \backslash D$.
\end{itemize}

Since there are two singular terms in the twisted conical Kähler-Ricci flow $\left(C K R F_{\gamma}^{\eta}\right)$, which are the initial metic $\hat{\omega}$ and current term $[D]$. By Demailly's regularization result [17], the authors [42] choose the sequence $\omega_{j}$ approximating to $\hat{\omega}$, that is, there exists a sequence of smooth strictly $\omega$-psh functions $\varphi_{j}$ decreasing to $\varphi_{0}$ as $j \nearrow \infty$, and
$$\omega_{j}=\omega+\sqrt{-1} \partial \bar{\partial} \varphi_{j} .$$
For the current term $[D]$, as in [37], we approximate it by $\theta_{\varepsilon}=\theta+\sqrt{-1} \partial \bar{\partial} \log \left(\varepsilon^{2}+|s|_{h}^{2}\right)$ as $\varepsilon \searrow 0$. Then the flow $\left(C K R F_{\gamma}^{\eta}\right)$ is approximated by the smooth twisted Kähler-Ricci flow
$$\left\{\begin{array}{l}
\frac{\partial \omega_{\gamma \varepsilon j}(t)}{\partial t}=-\operatorname{Ric}\left(\omega_{\gamma \varepsilon j}(t)\right)+(1-\gamma) \theta_{\varepsilon}+\eta \\
\left.\omega_{\gamma \varepsilon j}(t)\right|_{t=0}=\omega_{j}
\end{array} \quad\left(T K R F_{\gamma \varepsilon j}^{\eta}\right)\right.$$
which is equivalent to the following complex Monge-Ampère equation
$$\left\{\begin{array}{l}
\frac{\partial \varphi_{\gamma \varepsilon j}(t)}{\partial t}=\log \frac{\left(\omega_{\gamma t}+\sqrt{-1} \partial \bar{\partial} \varphi_{\gamma \varepsilon j}(t)\right)^{n}}{\omega^{n}}+h+(1-\gamma) \log \left(\varepsilon^{2}+|s|_{h}^{2}\right) \\
\left.\varphi_{\gamma \varepsilon j}(t)\right|_{t=0}=\varphi_{j}
\end{array} .\right.$$
In [42], by using smooth approximation and the ideas of Guedj-Zeriahi [23] and Di Nezza-Lu's [19] regularizing properties for the smooth twisted Kähler-Ricci flow coming from a positive current with zero Lelong number, the authors and Zhang proved the following result.

Theorem 2.7. Let $\hat{\omega} \in[\omega]$ be a closed positive current with zero Lelong number. For any $\gamma \in(0,1]$ and smooth closed (1, 1)-form $\eta$, there exists a unique weak solution to the twisted conical Kähler-Ricci flow $\left(C K R F_{\gamma}^{\eta}\right)$ on $\left(0, T_{\gamma, \max }^{\eta}\right) \times X$ in the sense of Definition 2.4.

Remark 2.8. From Definition 2.6, if $\phi(t)$ is a weak solution to equation (2.20) with initial value $\phi_{0} \in L^{\infty}(X) \cap \operatorname{PSH}(X, \omega)$ on $\left(0, T^{\prime}\right) \times X$, for any $0<\delta<T<T^{\prime}$, there exists a constant $C$ such that
$$C^{-1} \omega_{\gamma} \leqslant \omega_{\gamma t}+\sqrt{-1} \partial \bar{\partial} \phi(t) \leqslant C \omega_{\gamma} .$$
Hence for fix $\gamma \in(0,1)$,
$$\frac{\partial \phi(t)}{\partial t}=\log \frac{\left(\omega_{\gamma t}+\sqrt{-1} \partial \bar{\partial} \phi(t)\right)^{n}}{\omega^{n}}+h+(1-\gamma) \log |s|_{h}^{2}$$
is bounded in $[\delta, T] \times(X \backslash D)$, which implies that $\phi(t)$ is Hölder continuous on $X$ for any $t \in[\delta, T]$ by Kotodziej's $L^{p}$-estimates and that
$$\|\phi(t)-\phi(s)\|_{L^{\infty}(X)} \leqslant C|t-s| \quad \text { for all } t, s \in[\delta, T] .$$
Therefore, for any $t>0, \phi(t)$ is continuous on $X$, and there holds
$$\lim _{s \rightarrow t^{+}}\|\phi(s)-\phi(t)\|_{L^{\infty}(X)}=0 .$$

If the metric potential of the initial metric is continuous, the only difference is that the solution of (2.20) converges to the initial one in $L^{\infty}$-sense, which is stronger than the last condition in Definition 2.4. In [38], the authors gave the following existence and uniqueness theorem.

Theorem 2.9 (Theorem 1.2 and Remark 1.3 in [39]). Assume that $\tilde{\omega}$ is a closed positive current with continuous metric potential $\tilde{\varphi}_{0}$ with respect to $\omega$. Then there exists a unique solution to the
twisted conical Kähler-Ricci flow
$$\left\{\begin{array}{l}
\frac{\partial \omega_{\gamma}(t)}{\partial t}=-\operatorname{Ric}\left(\omega_{\gamma}(t)\right)+(1-\gamma)[D]+\eta \\
\left.\omega_{\gamma}(t)\right|_{t=0}=\tilde{\omega}
\end{array}\right.$$
on $\left(0, T_{\gamma, \max }^{\eta}\right) \times X$ in the following sense
\begin{itemize}
\item[-] For any $0<\delta<T<T_{\gamma, \max }^{\eta}$, there exists a constant $C$ such that for any $t \in(\delta, T)$,
$$C^{-1} \omega_{\gamma} \leqslant \omega_{\gamma}(t) \leqslant C \omega_{\gamma} \quad \text { in } \quad X \backslash D ;$$
\item[-] In $\left(0, T_{\gamma, \max }^{\eta}\right) \times(X \backslash D), \omega_{\gamma}(t)$ satisfies the smooth twisted Kähler-Ricci flow
$$\frac{\partial \omega_{\gamma}(t)}{\partial t}=-\operatorname{Ric}\left(\omega_{\gamma}(t)\right)+\eta ;$$
\item[-] On $\left(0, T_{\gamma, \max }^{\eta}\right) \times X, \omega_{\gamma}(t)$ satisfies equation (2.48) in the sense of currents;
\item[-] There exists a metric potential $\varphi_{\gamma}(t) \in \mathcal{C}^{2, \alpha, \gamma}(X) \cap \mathcal{C}^{\infty}(X \backslash D)$ such that $\omega_{\gamma}(t)=\omega_{\gamma t}+$ $\sqrt{-1} \partial \bar{\partial} \varphi_{\gamma}(t)$ and $\lim _{t \rightarrow 0^{+}}\left\|\varphi_{\gamma}(t)-\tilde{\varphi}\right\|_{L^{\infty}(X)}=0$;
\end{itemize}

Definition 2.10. Let $u_{0} \in \mathcal{C}^{0}(X)$ be a $\omega$-psh function. By saying $u(t) \in \mathcal{C}^{2, \alpha, \gamma}(X) \cap \mathcal{C}^{\infty}(X \backslash D)$ is a sub-solution to equation (2.20) with initial value $u_{0}$ on $\left(0, T^{\prime}\right) \times X$, we mean that $u(t)$ satisfies the following conditions.
\begin{itemize}
\item[-] For $0<\delta<T<T^{\prime}$, there exists a constant $C$ such that for any $t \in(\delta, T)$,
$$C^{-1} \omega_{\gamma} \leqslant \omega_{\gamma t}+\sqrt{-1} \partial \bar{\partial} u(t) \leqslant C \omega_{\gamma} \quad \text { in } \quad X \backslash D ;$$
\item[-] In $\left(0, T^{\prime}\right) \times(X \backslash D), u(t)$ satisfies equation
$$\frac{\partial u(t)}{\partial t} \leqslant \log \frac{\left(\omega_{\gamma t}+\sqrt{-1} \partial \bar{\partial} u(t)\right)^{n}}{\omega^{n}}+h+(1-\gamma) \log |s|_{h}^{2} ;$$
\item[-] $\lim _{t \rightarrow 0^{+}}\left\|u(t)-u_{0}\right\|_{L^{\infty}(X)}=0$.
\end{itemize}

Definition 2.11. Let $v_{0} \in \mathcal{C}^{0}(X)$ be a $\omega$-psh function. By saying $v(t) \in \mathcal{C}^{2, \alpha, \gamma}(X) \cap \mathcal{C}^{\infty}(X \backslash D)$ is a super-solution to equation (2.20) with initial value $v_{0}$ on $\left(0, T^{\prime}\right) \times X$, we mean that $v(t)$ satisfies the following conditions.
\begin{itemize}
\item[-] For $0<\delta<T<T^{\prime}$, there exists a constant $C$ such that for any $t \in(\delta, T)$,
$$C^{-1} \omega_{\gamma} \leqslant \omega_{\gamma t}+\sqrt{-1} \partial \bar{\partial} v(t) \leqslant C \omega_{\gamma} \quad \text { in } \quad X \backslash D ;$$
\item[-] In $\left(0, T^{\prime}\right) \times(X \backslash D), v(t)$ satisfies equation
$$\frac{\partial v(t)}{\partial t} \geqslant \log \frac{\left(\omega_{\gamma t}+\sqrt{-1} \partial \bar{\partial} v(t)\right)^{n}}{\omega^{n}}+h+(1-\gamma) \log |s|_{h}^{2} ;$$
\item[-] $\lim _{t \rightarrow 0^{+}}\left\|v(t)-v_{0}\right\|_{L^{\infty}(X)}=0$.
\end{itemize}

Definition 2.12. Let $\phi_{0} \in \mathcal{C}^{0}(X)$ be a $\omega$-psh function. By saying $\phi(t) \in \mathcal{C}^{2, \alpha, \gamma}(X) \cap \mathcal{C}^{\infty}(X \backslash D)$ is a solution to equation (2.20) with initial value $\phi_{0}$ on $\left(0, T^{\prime}\right) \times X$, we mean that $\phi(t)$ is both a sub-solution and a super-solution.
Remark 2.13. From Definitions 2.6 and 2.12 and Remark 2.8, we see that a weak solution $\phi(t)$ to equation (2.20) with initial value $\phi_{0} \in L^{\infty}(X) \cap \operatorname{PSH}(X, \omega)$ on $\left(0, T^{\prime}\right) \times X$ is a solution to equation (2.20) with initial value $\phi\left(t_{0}\right) \in \mathcal{C}^{0}(X) \cap \operatorname{PSH}\left(X, \omega_{\gamma t_{0}}\right)$ on $\left(t_{0}, T^{\prime}\right) \times X$.

Next, we prove some maximum principles, which are important in proving the uniqueness theorem of the limit flow.

Proposition 2.14. If $u(t)$ is a sub-solution to equation (2.20) with initial value $u_{0} \in \mathcal{C}^{0}(X) \cap$ $\operatorname{PSH}(X, \omega)$ on $\left(0, T^{\prime}\right) \times X$, and $v(t)$ is a super-solution to equation (2.20) with initial value $v_{0} \in$ $\mathcal{C}^{0}(X) \cap \operatorname{PSH}(X, \omega)$ on $\left(0, T^{\prime}\right) \times X$. Then
$$u(t)-v(t) \leqslant \sup _{X}\left(u_{0}-v_{0}\right) \quad \text { on } \quad\left[0, T^{\prime}\right) \times X .$$
Proof. For any $0<t_{1}<T<T^{\prime}$ and $a>0$. We consider $\Psi(t)=u(t)-v(t)+a \log |s|_{h}^{2}$ on $\left[t_{1}, T\right] \times X$. If we denote
$$\hat{\Delta}=\int_{0}^{1} g_{s}^{i \bar{j}} \frac{\partial^{2}}{\partial z^{i} \partial \bar{z}^{j}} d s$$
where $g_{s}$ is the metric corresponding to $\omega_{s}=\omega_{\gamma t}+s \sqrt{-1} \partial \bar{\partial} u(t)+(1-s) \sqrt{-1} \partial \bar{\partial} v(t)$. Then $\Psi(t)$ evolves along the following equation
$$\frac{\partial \Psi(t)}{\partial t} \leqslant \hat{\Delta} \Psi(t)-a \hat{\Delta} \log |s|_{h}^{2} .$$
Since $\omega_{u(t)}$ and $\omega_{v(t)}$ are bounded from below by $c_{0} \omega_{\gamma}$ and (2.28), we obtain
$$\omega_{s} \geqslant c \omega$$
for some constants $c_{0}$ and $c$ depending on $t_{1}$ and $T$. Combining this with $-\sqrt{-1} \partial \bar{\partial} \log |s|_{h}^{2}=\theta$, we conclude that there exists a constant $C\left(t_{1}, T\right)$ depending on $t_{1}$ and $T$ such that
$$-\hat{\Delta} \log |s|_{h}^{2}=\int_{0}^{1} \operatorname{tr}_{\omega_{s}} \theta d s \leq C\left(t_{1}, T\right)$$
in $X \backslash D$. Then
$$\frac{\partial \Psi(t)}{\partial t} \leqslant \hat{\Delta} \Psi(t)+a C\left(t_{1}, T\right) .$$

Let $\tilde{\Psi}=\Psi-a C\left(t_{1}, T\right)\left(t-t_{1}\right)-\epsilon\left(t-t_{1}\right)$. It is obvious that the space maximum of $\Psi(t)$ on $\left[t_{1}, T\right] \times X$ is attained away from $D$. Let $\left(t_{0}, x_{0}\right)$ be the maximum point. If $t_{0}>t_{1}$, by the maximum principle, at $\left(t_{0}, x_{0}\right)$, we have
$$0 \leqslant\left(\frac{\partial}{\partial t}-\hat{\Delta}\right) \tilde{\Psi}(t) \leqslant-\epsilon,$$
which is impossible and so $t_{0}=t_{1}$. Then for $(t, x) \in\left[t_{1}, T\right] \times(X \backslash D)$, we obtain
$$u(t)-v(t) \leqslant \sup _{X}\left(u\left(t_{1}\right)-v\left(t_{1}\right)\right)+a T C\left(t_{1}, T\right)+\epsilon T-a \log |s|_{h}^{2} .$$
We let $\epsilon \rightarrow 0$ and then $a \rightarrow 0$, there holds
$$u(t)-v(t) \leqslant \sup _{X}\left(u\left(t_{1}\right)-v\left(t_{1}\right)\right) .$$
Then we prove (2.55) after we let $t_{1} \rightarrow 0^{+}$since $\lim _{t \rightarrow 0^{+}}\left\|u(t)-u_{0}\right\|_{L^{\infty}(X)}=0$ and $\lim _{t \rightarrow 0^{+}} \| v(t)-$ $v_{0} \|_{L^{\infty}(X)}=0$ \(\square\)

Proposition 2.15. Assume that $\phi(t)$ is a super-solution to equation (2.20) with initial value $\phi_{0} \in$ $\mathcal{C}^{0}(X) \cap \operatorname{PSH}(X, \omega)$ and that $\psi(t)$ is a weak solution to equation (2.20) with initial value $\psi_{0} \in$ $L^{\infty}(X) \cap \operatorname{PSH}(X, \omega)$ on $\left(0, T^{\prime}\right) \times X$. Then
$$\psi(t)-\phi(t) \leqslant \sup _{X}\left(\psi_{0}-\phi_{0}\right) \quad \text { on } \quad\left[0, T^{\prime}\right) \times X .$$
Proof. For any $0<t_{1}<T<T^{\prime}$, since $\psi(t)$ is a weak solution to equation (2.20), by Remark 2.13, $\psi(t)$ is a solution to equation (2.20) with initial value $\psi\left(t_{1}\right)$. By using Proposition 2.14, on $\left[t_{1}, T^{\prime}\right) \times X$, we have
$$\psi(t)-\phi(t) \leqslant \sup _{X}\left(\psi\left(t_{1}\right)-\phi\left(t_{1}\right)\right) .$$

Since $\psi\left(t_{1}\right)$ converges to $\psi_{0}$ in $L^{1}$-sense and $\phi\left(t_{1}\right)$ converges to $\phi_{0}$ in $L^{\infty}$-sense, it then follows form Hartogs' Lemma that
$$\psi(t)-\phi(t) \leqslant \sup _{X}\left(\psi_{0}-\phi_{0}\right)$$
on $\left[0, T^{\prime}\right) \times X$ after we let $t_{1} \rightarrow 0$. \(\square\)

\section*{3. Uniform estimates on metric potentials}

In this section, we prove some uniform estimates on potential $\varphi_{\gamma}(t)$ and its time derivative $\dot{\varphi}_{\gamma}(t)$.
For any $0<T<T_{\text {max }}^{\eta}, T<T_{\gamma, \text { max }}^{\eta}$ also holds for $0<\gamma \ll 1$ sufficiently small. If $T>1$, we further assume that $\delta$ in (2.26) is sufficiently small such that
$$\sqrt{-1} \partial \bar{\partial} \psi_{\gamma} \geqslant-\frac{1}{8 T(C-1)} \omega>-\frac{1}{8(C-1)} \omega,$$
where $C$ comes from (2.17). Combining (2.27) with (2.28), we also have
$$\omega_{\gamma}=\omega+\sqrt{-1} \partial \bar{\partial} \psi_{\gamma} \geqslant \frac{1}{2} \omega .$$

Due to the singularity of the equation (2.20), we are unable to derive an effective uniform estimate on $\varphi_{\gamma}(t)$ by using the maximum principle. But fortunately, by constructing new auxiliary functions and introducing new arguments, we can prove a uniform estimate on $\varphi_{\gamma}(t)-t \psi_{\gamma}$ and its time derivative, which enables us to derive the high order uniform estimates along the twisted conical Kähler-Ricci flow. Now we first construct a super-solution to derive a uniform upper bound.

Proposition 3.1. There exists a uniform constant $C$ depending only on $\omega, \theta, \eta$ and $T$ such that
$$\varphi_{\gamma}(t) \leqslant \sup _{X} \varphi_{0}+t \psi_{\gamma}+C t \quad \text { on } \quad X$$
for all $t \in[0, T]$ and $0<\gamma \ll 1$.
Proof. Denote
$$\psi_{\gamma}(t)=\sup _{X} \varphi_{0}+t \psi_{\gamma}+C t .$$
By using (2.17) and (3.1), for any $t \in[0, T]$, we have
$$\omega_{\gamma t}+\sqrt{-1} \partial \bar{\partial} \psi_{\gamma}(t)=\omega_{\gamma t}+t \sqrt{-1} \partial \bar{\partial} \psi_{\gamma} \geqslant \frac{1}{C} \omega-\frac{t}{8 T(C-1)} \omega \geqslant\left(\frac{1}{C}-\frac{1}{8(C-1)}\right) \omega>0,$$
which implies that $\psi_{\gamma}(t)$ is a continuous $\omega_{\gamma t}$-psh function.
On the other hand, from (2.17), (2.34) and (3.2), there exists a uniform constant $C$ depending only on $\omega, \theta, \eta$ and $T$ such that
$$\omega_{\gamma t}+\sqrt{-1} \partial \bar{\partial} \psi_{\gamma}(t)=t\left(\omega_{\gamma t}+\sqrt{-1} \partial \bar{\partial} \psi_{\gamma}\right)+(1-t) \omega_{\gamma t} \leqslant C \omega_{\gamma} .$$
Hence
$$\begin{aligned}
& \log \frac{\left(\omega_{\gamma t}+\sqrt{-1} \partial \bar{\partial} \psi_{\gamma}(t)\right)^{n}}{\omega^{n}}+h+(1-\gamma) \log |s|_{h}^{2} \\
\leqslant & \log C+\log \frac{\omega_{\gamma}^{n}}{\omega^{n}}+h+(1-\gamma) \log |s|_{h}^{2} \\
\leqslant & \log C+\log \frac{\omega_{\gamma}^{n}}{\omega^{n}}+h+(1-\gamma) \log |s|_{h}^{2}-\psi_{\gamma}+\psi_{\gamma} \\
\leqslant & C+\psi_{\gamma}=\frac{\partial \psi_{\gamma}(t)}{\partial t},
\end{aligned}$$
where we use (2.29) in the last inequality. Combining the fact that
$$\lim _{t \rightarrow 0^{+}}\left\|\psi_{\gamma}(t)-\sup _{X} \varphi_{0}\right\|_{L^{\infty}(X)}=0,$$
we show that $\psi_{\gamma}(t)$ is a super-solution to equation with initial value $\sup _{X} \varphi_{0}$. By the maximum principle Proposition 2.15, we conclude that
$$\varphi_{\gamma}(t) \leqslant \psi_{\gamma}(t)=\sup _{X} \varphi_{0}+t \psi_{\gamma}+C t \quad \text { on } \quad X$$
for all $t \in[0, T]$ and $0<\gamma \ll 1$. \(\square\)

Proposition 3.2. For any $t \in(0, T]$ and $0<\gamma \ll 1$, there holds
$$\dot{\varphi}_{\gamma}(t) \leqslant \frac{\varphi_{\gamma}(t)-\varphi_{0}}{t}+n \quad \text { in } \quad X \backslash D .$$
Furthermore, there exists a uniform constant $C$ depending only on $n, \omega, \theta, \eta$ and $T$ such that
$$\dot{\varphi}_{\gamma}(t) \leqslant \frac{\operatorname{osc} \varphi_{0}}{t}+\psi_{\gamma}+C \quad \text { in } \quad X \backslash D$$
for all $t \in[0, T]$ and $0<\gamma \ll 1$.
Proof. We consider the smooth complex Monge-Ampère equation (2.43). Let
$$H_{\gamma \varepsilon j}(t)=t \dot{\varphi}_{\gamma \varepsilon j}(t)-\left(\varphi_{\gamma \varepsilon j}(t)-\varphi_{j}\right)-n t .$$
Direct computations show that
$$\frac{\partial}{\partial t} \dot{\varphi}_{\gamma \varepsilon j}(t)=\operatorname{tr}_{\omega_{\gamma \varepsilon j}(t)}\left(v_{\gamma}+\sqrt{-1} \partial \bar{\partial} \dot{\varphi}_{\gamma \varepsilon j}(t)\right),$$
and hence
$$\frac{\partial H_{\gamma \varepsilon j}}{\partial t}=t \ddot{\varphi}_{\gamma \varepsilon j}(t)-n=t\left(\operatorname{tr}_{\omega_{\gamma \varepsilon j}(t)} \nu_{\gamma}+\Delta_{\omega_{\gamma \varepsilon j}(t)} \dot{\varphi}_{\gamma \varepsilon j}(t)\right)-n .$$
On the other hand, we have
$$\begin{aligned}
\Delta_{\omega_{\gamma \varepsilon j}(t)} H_{\gamma \varepsilon j} & =t \Delta_{\omega_{\gamma \varepsilon j}(t)} \dot{\varphi}_{\gamma \varepsilon j}(t)-\Delta_{\omega_{\gamma \varepsilon j}(t)} \varphi_{\gamma \varepsilon j}(t)+\Delta_{\omega_{\gamma \varepsilon j}(t)} \varphi_{j} \\
& =t \Delta_{\omega_{\gamma \varepsilon j}(t)} \dot{\varphi}_{\gamma \varepsilon j}(t)-n+\operatorname{tr}_{\omega_{\gamma \varepsilon j}(t)} \omega_{\gamma t}+\Delta_{\omega_{\gamma \varepsilon j}(t)} \varphi_{j} \\
& =t\left(\operatorname{tr}_{\omega_{\gamma \varepsilon j}(t)} \nu_{\gamma}+\Delta_{\omega_{\gamma \varepsilon j}(t)} \dot{\varphi}_{\gamma \varepsilon j}(t)\right)-n+\operatorname{tr}_{\omega_{\gamma \varepsilon j}(t)} \omega_{j} .
\end{aligned}$$
Then
$$\left(\frac{\partial}{\partial t}-\Delta_{\omega_{\gamma \varepsilon j}(t)}\right) H_{\gamma \varepsilon j}=-\operatorname{tr}_{\omega_{\gamma \varepsilon j}(t)} \omega_{j} \leqslant 0 .$$
By the maximum principle, we have $H_{\gamma \varepsilon j}(t) \leqslant \sup _{X} H_{\gamma \varepsilon j}(0)=0$. Therefore,
$$\dot{\varphi}_{\gamma \varepsilon j}(t) \leqslant \frac{\varphi_{\gamma \varepsilon j}(t)-\varphi_{j}}{t}+n$$
for all $j \geqslant 1, \varepsilon \in(0,1)$ and $t \in(0, T]$. Letting $j \rightarrow \infty$ and then $\varepsilon \rightarrow 0$, we obtain
$$\dot{\varphi}_{\gamma}(t) \leqslant \frac{\varphi_{\gamma}(t)-\varphi_{0}}{t}+n \quad \text { in } \quad X \backslash D .$$
Inequality (3.11) follows from (3.18) and Proposition 3.1. \(\square\)

Corollary 3.3. For any $0<T<T_{\text {max }}^{\eta}$, there exists a uniform constant $C$ depending only on $n$, $\omega, \theta, \eta$ and $T$ such that for any $t \in[0, T]$ and $0<\gamma \ll 1$,
$$t\left(\dot{\varphi}_{\gamma}(t)-\psi_{\gamma}\right) \leqslant \underset{X}{\operatorname{osc}} \varphi_{0}+C t \quad \text { in } \quad X \backslash D .$$

Corollary 3.4. For any $0<\delta<T<T_{\text {max }}^{\eta}$, there exists a uniform constant $C$ depending only on $\left\|\varphi_{0}\right\|_{L^{\infty}(X)}, n, \omega, \theta, \eta, \delta$ and $T$ such that for any $t \in[\delta, T]$ and $0<\gamma \ll 1$,
$$\dot{\varphi}_{\gamma}(t) \leqslant \psi_{\gamma}+C \quad \text { in } \quad X \backslash D .$$

Then by using Propositions 3.1 and 3.2, we give some new arguments to prove a uniform lower bound on the potential in a short time.

Proposition 3.5. There exists a uniform constant $C$ depending only on $n, \omega, \theta, \eta$ and $T$ such that
$$\varphi_{\gamma}(t) \geqslant \inf _{X} \varphi_{0}+t \psi_{\gamma}-C \quad \text { on } \quad X$$
for all $t \in[0,1]$ and $0<\gamma \ll 1$.
Proof. We only consider the case $t \in(0,1]$. By using Proposition 3.2, we have
$$\begin{aligned}
\left(\omega_{\gamma t}+\sqrt{-1} \partial \bar{\partial} \varphi_{\gamma}(t)\right)^{n} & =e^{\dot{\varphi}_{\gamma}(t)-h} \frac{\omega^{n}}{|s|_{h}^{2(1-\gamma)}} \\
& \leqslant e^{\frac{\varphi_{\gamma}(t)-\varphi_{0}}{t}+C-(1-\gamma) \log |s|_{h}^{2}+\log \frac{\omega^{n}}{\omega_{\gamma}^{n}}} \omega_{\gamma}^{n} \\
& \leqslant e^{\frac{\varphi_{\gamma}(t)-t \psi_{\gamma}}{t}+\psi_{\gamma}-\frac{1}{t} \inf _{X} \varphi_{0}+C-(1-\gamma) \log |s|_{h}^{2}+\log \frac{\omega^{n}}{\omega_{\gamma}^{n}}} \omega_{\gamma}^{n} \\
& \leqslant e^{\frac{\varphi_{\gamma}(t)-t \psi_{\gamma}}{t}+\frac{1}{t}\left(C-\inf _{X} \varphi_{0}\right)} \omega_{\gamma}^{n},
\end{aligned}$$
where we use inequality (2.29) in the last inequality.
For $0<\epsilon \ll 1$, we denote
$$\phi_{\gamma}(t)=\varphi_{\gamma}(t)-t \psi_{\gamma} \quad \text { and } \quad \chi_{\gamma \epsilon}(t)=\phi_{\gamma}(t)-\epsilon \log |s|_{h}^{2} .$$
For any $0<t_{0} \leqslant 1$, we let $x_{0}$ be the minimum point of $\chi_{\gamma \epsilon}\left(t_{0}\right)$. Since $\phi_{\gamma}\left(t_{0}\right)$ is continuous on $X$, $x_{0}$ must be attained in $X \backslash D$. At $\left(t_{0}, x_{0}\right)$, by the maximum principle and (2.36), there holds
$$\begin{aligned}
\left(\omega_{\gamma t_{0}}+\sqrt{-1} \partial \bar{\partial} \varphi_{\gamma}\left(t_{0}\right)\right)^{n} & =\left(\omega_{\gamma t_{0}}+t_{0} \sqrt{-1} \partial \bar{\partial} \psi_{\gamma}+\sqrt{-1} \partial \bar{\partial} \phi_{\gamma}\left(t_{0}\right)\right)^{n} \\
& =\left(\omega_{\gamma t_{0}}+t_{0} \sqrt{-1} \partial \bar{\partial} \psi_{\gamma}-\epsilon \theta+\sqrt{-1} \partial \bar{\partial} \chi_{\gamma \epsilon}\left(t_{0}\right)\right)^{n} \\
& \geqslant\left(\omega_{\gamma t_{0}}+t_{0} \sqrt{-1} \partial \bar{\partial} \psi_{\gamma}-\epsilon \theta\right)^{n} \\
& =\left(t_{0}\left(\omega_{\gamma t_{0}}+\sqrt{-1} \partial \bar{\partial} \psi_{\gamma}\right)+\left(1-t_{0}\right) \omega_{\gamma t_{0}}-\epsilon \theta\right)^{n} \\
& \geqslant\left(\frac{t_{0}}{2}\right)^{n}\left(\omega_{\gamma t_{0}}+\sqrt{-1} \partial \bar{\partial} \psi_{\gamma}\right)^{n} \\
& \geqslant \frac{t_{0}^{n}}{C} \omega_{\gamma}^{n}
\end{aligned}$$
for all $0<\gamma, \epsilon \ll 1$. Therefore, by using (3.22), at ( $t_{0}, x_{0}$ ), we have
$$\frac{1}{t_{0}} \phi_{\gamma}\left(t_{0}, x_{0}\right)+\frac{1}{t_{0}}\left(C-\inf _{X} \varphi_{0}\right) \geqslant n \log t_{0}-C,$$
that is,
$$\phi_{\gamma}\left(t_{0}, x_{0}\right) \geqslant \inf _{X} \varphi_{0}+n t_{0} \log t_{0}-C \geqslant \inf _{X} \varphi_{0}-C .$$
Hence
$$\chi_{\gamma \epsilon}\left(t_{0}\right) \geqslant \phi_{\gamma}\left(t_{0}, x_{0}\right) \geqslant \inf _{X} \varphi_{0}-C,$$
and then
$$\varphi_{\gamma}\left(t_{0}\right) \geqslant t_{0} \psi_{\gamma}+\epsilon \log |s|_{h}^{2}+\inf _{X} \varphi_{0}-C .$$

Let $\epsilon \rightarrow 0$, there holds
$$\varphi_{\gamma}\left(t_{0}\right) \geqslant \inf _{X} \varphi_{0}+t_{0} \psi_{\gamma}-C \quad \text { on } \quad X$$
for some uniform constant $C$ depending only on $n, \omega, \theta, \eta$ and $T$. Since $t_{0}$ is arbitrary, we complete the proof. \(\square\)

Remark 3.6. In fact, by using similar arguments as in the proof of Proposition 3.1, we can also give a uniform low bound as follows. There exists a uniform constant $C$ depending only on $n, \omega$, $\theta, \eta$ and $T$ such that
$$\varphi_{\gamma}(t) \geqslant \inf _{X} \varphi_{0}+t \psi_{\gamma}+n(t \log t-t)-C t \quad \text { on } \quad X$$
for all $t \in[0,1]$ and $0<\gamma \ll 1$.
In Proposition 5.4, we will show a better uniform lower bound which improves the terms $\inf _{X} \varphi_{0}$ in (3.21) and (3.30) to be $\varphi_{0}$. It is very important in showing the limit behavior of the limit flow near $t=0$.

On the foundation of above uniform estimates, we prove a uniform lower bound on $\dot{\varphi}_{\gamma}(t)$ in a uniform short time. In this proof, the originality of the auxiliary function lies in the coefficient $t+\sigma$ of the term $\left(\dot{\varphi}_{\gamma}(t)-\psi_{\gamma}\right)$ for some uniform small positive constant $\sigma$, which is only $t$ in previous literature, such as [57, 23, 38, 39, 32] etc. The main reason is that in this proof, we need to derive a term $\sigma \operatorname{tr}_{\omega_{\gamma}(t)} \omega_{\gamma}$ with uniform coefficient $\sigma>0$ for all $t>0$ and $0<\gamma \ll 1$ to control the term $\log \frac{\omega_{\gamma}^{n}(t)}{\omega_{\gamma}^{n}}$ coming from $\dot{\varphi}_{\gamma}(t)$ by the mean value inequality. But the background metric considered here is $\omega_{\gamma t}+t \sqrt{-1} \partial \bar{\partial} \psi_{\gamma}$, due to the coefficient of $\sqrt{-1} \partial \bar{\partial} \psi_{\gamma}$ is $t$, we can only derive the term $t \operatorname{tr}_{\omega_{\gamma}(t)} \omega_{\gamma}$, which can not imply a uniform lower bound for all $t>0$. So we choose the coefficient $t+\sigma$ in the new auxiliary function.

Proposition 3.7. There exist uniform positive constants $\sigma$ and $\kappa$ depending only on $\eta, \theta$ and $\omega$, and a uniform constant $C$ depending only on $n, \omega, \theta, \eta$ and $T$ such that
$$\sigma\left(\dot{\varphi}_{\gamma}(t)-\psi_{\gamma}\right) \geqslant-2 \underset{X}{\operatorname{cosc}} \varphi_{0}+n \log t-C \quad \text { in } \quad X \backslash D$$
for all $t \in(0, \kappa]$ and $0<\gamma \ll 1$.
Proof. For any $0<\sigma \ll 1$ and $\epsilon>0$, we define function
$$G_{\gamma}(t)=(t+\sigma)\left(\dot{\varphi}_{\gamma}(t)-\psi_{\gamma}\right)+\left(\varphi_{\gamma}(t)-t \psi_{\gamma}\right)-n \log t-\epsilon \log |s|_{h}^{2} .$$
For any fix $\gamma$, from the author results (Proposition 3.9 in [42], see also Lemma 3.7 in [32]), $(t+$ $\sigma) \dot{\varphi}_{\gamma}(t)$ is bounded from below by $n \sigma \log t$ near $t=0$. And since $\varphi_{\gamma}(t)$ and $\psi_{\gamma}$ are continuous on $X$, and $n \sigma \log t-n \log t$ tends to $+\infty$ as $t \rightarrow 0, G_{\gamma}(t)$ tends to $+\infty$ as $t \rightarrow 0$ or $x \rightarrow D$ and so the minimum point of $G_{\gamma}(t)$ must be away from both $t=0$ and the divisor $D$, where $G_{\gamma}(t)$ is smooth.

In $X \backslash D$, direct computations show that
$$\begin{aligned}
\left(\frac{\partial}{\partial t}-\Delta_{\omega_{\gamma}(t)}\right) G_{\gamma}(t)= & \dot{\varphi}_{\gamma}(t)-\psi_{\gamma}+(t+\sigma)\left(\ddot{\varphi}_{\gamma}(t)-\Delta_{\omega_{\gamma}(t)} \dot{\varphi}_{\gamma}(t)\right)+(t+\sigma) \Delta_{\omega_{\gamma}(t)} \psi_{\gamma} \\
& +\dot{\varphi}_{\gamma}(t)-\Delta_{\omega_{\gamma}(t)} \varphi_{\gamma}(t)-\psi_{\gamma}+t \Delta_{\omega_{\gamma}(t)} \psi_{\gamma}-\frac{n}{t}-\epsilon \operatorname{tr}_{\omega_{\gamma}(t)} \theta \\
= & 2 \dot{\varphi}_{\gamma}(t)-2 \psi_{\gamma}+(t+\sigma) \operatorname{tr}_{\omega_{\gamma}(t)} \nu_{\gamma}-\Delta_{\omega_{\gamma}(t)} \varphi_{\gamma}(t)-\frac{n}{t}-\epsilon \operatorname{tr}_{\omega_{\gamma}(t)} \theta \\
& +(2 t+\sigma) \Delta_{\omega_{\gamma}(t)} \psi_{\gamma} \\
= & 2\left(\dot{\varphi}_{\gamma}(t)-\psi_{\gamma}\right)-n+\operatorname{tr}_{\omega_{\gamma}(t)}\left(\omega+(2 t+\sigma) \nu_{\gamma}+(2 t+\sigma) \sqrt{-1} \partial \bar{\partial} \psi_{\gamma}-\epsilon \theta\right)-\frac{n}{t} \\
= & \operatorname{tr}_{\omega_{\gamma}(t)}\left(\sigma\left(\omega+\sqrt{-1} \partial \bar{\partial} \psi_{\gamma}\right)+\left((1-\sigma) \omega+(2 t+\sigma) \nu_{\gamma}+2 t \sqrt{-1} \partial \bar{\partial} \psi_{\gamma}\right)-\epsilon \theta\right)
\end{aligned}$$
$$+2\left(\dot{\varphi}_{\gamma}(t)-\psi_{\gamma}\right)-n-\frac{n}{t} .$$
By using (2.29), we have
$$\begin{aligned}
\dot{\varphi}_{\gamma}(t)-\psi_{\gamma} & =\log \frac{\left(\omega_{\gamma t}+\sqrt{-1} \partial \bar{\partial} \varphi_{\gamma}(t)\right)^{n}}{\omega^{n}}+h+(1-\gamma) \log |s|_{h}^{2}-\psi_{\gamma} \\
& =\log \frac{\left(\omega_{\gamma t}+\sqrt{-1} \partial \bar{\partial} \varphi_{\gamma}(t)\right)^{n}}{\omega_{\gamma}^{n}}+\log \frac{\omega_{\gamma}^{n}}{\omega^{n}}+h+(1-\gamma) \log |s|_{h}^{2}-\psi_{\gamma} \\
& \geqslant \log \frac{\left(\omega_{\gamma t}+\sqrt{-1} \partial \bar{\partial} \varphi_{\gamma}(t)\right)^{n}}{\omega_{\gamma}^{n}}-C .
\end{aligned}$$
On the other hand, if $\nu_{\gamma} \geqslant-C \omega$ and $\theta \leqslant C \omega$ with some uniform large constant $C>2$, by using (3.1), for $0<\sigma<\frac{1}{2(C+1)}, 0<t<\frac{1}{8 C}:=\kappa<\frac{1}{2}$ and $0<\epsilon<\frac{C-2}{4 C(C-1)}$, we have
$$\begin{aligned}
& (1-\sigma) \omega+(2 t+\sigma) \nu_{\gamma}+2 t \sqrt{-1} \partial \bar{\partial} \psi_{\gamma}-\epsilon \theta \\
\geqslant & \left(1-\sigma-(2 t+\sigma) C-\frac{1}{4(C-1)}-C \epsilon\right) \omega \\
\geqslant & 0 .
\end{aligned}$$
Therefore, there exists a uniform constant $C$ depending only on $n, \omega, \theta, \eta$ and $T$ such that
$$\begin{aligned}
\left(\frac{\partial}{\partial t}-\Delta_{\omega_{\gamma}(t)}\right) G_{\gamma}(t) & \geqslant 2 \log \frac{\left(\omega_{\gamma t}+\sqrt{-1} \partial \bar{\partial} \varphi_{\gamma}(t)\right)^{n}}{\omega_{\gamma}^{n}}+\sigma \operatorname{tr}_{\omega_{\gamma}(t)} \omega_{\gamma}-\frac{C}{t} \\
& \geqslant 2 \log \frac{\left(\omega_{\gamma t}+\sqrt{-1} \partial \bar{\partial} \varphi_{\gamma}(t)\right)^{n}}{\omega_{\gamma}^{n}}+\sigma n\left(\frac{\omega_{\gamma}^{n}}{\omega_{\gamma}^{n}(t)}\right)^{\frac{1}{n}}-\frac{C}{t},
\end{aligned}$$
where we use the mean value inequality in the last inequality.
Consider function
$$f(s)=\frac{n \sigma}{2} s^{\frac{1}{n}}-2 \log s .$$
There exists a constant $S$ depending only on $\sigma, l$ and $n$ such that $f(s) \geqslant 0$ when $s \geqslant S$ or $0<s \leqslant 1$.
Assume that $\left(t_{0}, x_{0}\right)$ is the minimum point of $G_{\gamma}(t)$ in $(0, \kappa] \times(X \backslash D)$. If $\frac{\omega_{\gamma}^{n}}{\omega_{\gamma}^{n}(t)} \geqslant S$ at $\left(t_{0}, x_{0}\right)$, then
$$\left(\frac{\partial}{\partial t}-\Delta_{\omega_{\gamma}(t)}\right) G_{\gamma}(t) \geqslant \frac{n \sigma}{2}\left(\frac{\omega_{\gamma}^{n}}{\omega_{\gamma}^{n}(t)}\right)^{\frac{1}{n}}-\frac{C}{t} .$$
The maximum principle implies that at $\left(t_{0}, x_{0}\right)$,
$$\left(\frac{\omega_{\gamma}^{n}}{\omega_{\gamma}^{n}(t)}\right) \leqslant\left(\frac{2 C}{\sigma n t_{0}}\right)^{n}$$
and then
$$\log \frac{\omega_{\gamma}^{n}(t)}{\omega_{\gamma}^{n}} \geqslant n \log t_{0}-C .$$

If $\frac{\omega_{\gamma}^{n}}{\omega_{\gamma}^{n}(t)}<S$ at $\left(t_{0}, x_{0}\right)$, then
$$\log \frac{\omega_{\gamma}^{n}(t)}{\omega_{\gamma}^{n}} \geqslant-\log S .$$

Combining above arguments with (2.29) and Proposition 3.5, we have
$$\begin{aligned}
& (t+\sigma)\left(\dot{\varphi}_{\gamma}(t)-\psi_{\gamma}\right)+\left(\varphi_{\gamma}(t)-t \psi_{\gamma}\right)-n \log t-\epsilon \log |s|_{h}^{2} \\
\geqslant & \left(t_{0}+\sigma\right)\left(\dot{\varphi}_{\gamma}\left(t_{0}, x_{0}\right)-\psi_{\gamma}\left(x_{0}\right)\right)+\left(\varphi_{\gamma}\left(t_{0}, x_{0}\right)-t_{0} \psi_{\gamma}\left(x_{0}\right)\right)-n \log t_{0} \\
\geqslant & \left(t_{0}+\sigma\right)\left(\log \frac{\left(\omega_{\gamma t}+\sqrt{-1} \partial \bar{\partial} \varphi_{\gamma}(t)\right)^{n}}{\omega^{n}}+h+(1-\gamma) \log |s|_{h}^{2}-\psi_{\gamma}\right)\left(t_{0}, x_{0}\right) \\
& +\inf _{X} \varphi_{0}-C-n \log t_{0} \\
= & \left(t_{0}+\sigma\right)\left(\log \frac{\left(\omega_{\gamma t}+\sqrt{-1} \partial \bar{\partial} \varphi_{\gamma}(t)\right)^{n}}{\omega_{\gamma}^{n}}+\log \frac{\omega_{\gamma}^{n}}{\omega^{n}}+h+(1-\gamma) \log |s|_{h}^{2}-\psi_{\gamma}\right)\left(t_{0}, x_{0}\right) \\
& +\inf _{X} \varphi_{0}-C-n \log t_{0} \\
\geqslant & \left(t_{0}+\sigma\right)\left(n \log t_{0}-C\right)+\inf _{X} \varphi_{0}-C-n \log t_{0} \\
= & -\left(1-t_{0}-\sigma\right) n \log t_{0}+\inf _{X} \varphi_{0}-C \\
\geqslant & \inf _{X} \varphi_{0}-C,
\end{aligned}$$
where we use $t_{0}+\sigma<1$ uniformly. After letting $\epsilon \rightarrow 0$ and using Proposition 3.1, we obtain
$$(t+\sigma)\left(\dot{\varphi}_{\gamma}(t)-\psi_{\gamma}\right) \geqslant-\operatorname{osc}_{X} \varphi_{0}+n \log t-C .$$
Then by using Corollary 3.3, we complete the proof . \(\square\)

Remark 3.8. In fact, the constant $C$ in (3.31) also depends on $\sigma$. Since $\sigma$ depends only on $\eta, \theta$ and $\omega$, we will no longer mention that the constant depends on it after we fix one $\sigma$ in the following arguments.

Next, we extend above uniform estimates in short time to all time in $(0, T]$.
Proposition 3.9. For any $T \in\left(\kappa, T_{\text {max }}^{\eta}\right)$, where $\kappa$ comes from Proposition 3.7, there exists a uniform constant $C$ depending only on $\left\|\varphi_{0}\right\|_{L^{\infty}(X)}, n, \omega, \theta, \eta$ and $T$ such that
$$(T-t)\left(\dot{\varphi}_{\gamma}(t)-\psi_{\gamma}\right) \geqslant-C \quad \text { in } \quad X \backslash D$$
for all $t \in[\kappa, T]$ and $0<\gamma \ll 1$.
Furthermore, for any $T^{\prime} \in(\kappa, T)$, there exists a uniform constant $C$ depending only on $\left\|\varphi_{0}\right\|_{L^{\infty}(X)}$, $n, \omega, \theta, \eta, T^{\prime}$ and $T$ such that
$$\dot{\varphi}_{\gamma}(t) \geqslant \psi_{\gamma}-C \quad \text { in } \quad X \backslash D$$
for all $t \in\left[\kappa, T^{\prime}\right]$ and $0<\gamma \ll 1$.
Proof. Define
$$K_{\gamma \varepsilon j}(t)=(T-t)\left(\dot{\varphi}_{\gamma \varepsilon j}(t)-\psi_{\gamma}\right)+\left(\varphi_{\gamma \varepsilon j}(t)-t \psi_{\gamma}\right)+n t-\epsilon \log |s|_{h}^{2} .$$
Direct computations show that in $X \backslash D$,
$$\begin{aligned}
\left(\frac{\partial}{\partial t}-\Delta_{\omega_{\gamma e j}(t)}\right) K_{\gamma \varepsilon j}(t) & =(T-t) \operatorname{tr}_{\omega_{\gamma \varepsilon j}(t)} \nu_{\gamma}+\operatorname{tr}_{\omega_{\gamma \varepsilon j}(t)}\left(\omega_{\gamma t}-\epsilon \theta\right)+T \Delta_{\omega_{\gamma \varepsilon j}(t)} \psi_{\gamma} \\
& =\operatorname{tr}_{\omega_{\gamma \varepsilon j}(t)}\left(\omega+T \nu_{\gamma}+T \sqrt{-1} \partial \bar{\partial} \psi_{\gamma}-\epsilon \theta\right) .
\end{aligned}$$
By using (2.17) and (3.1), we have
$$\omega+T \nu_{\gamma}+T \sqrt{-1} \partial \bar{\partial} \psi_{\gamma}-\epsilon \theta \geqslant\left(\frac{1}{C}-\frac{1}{8(C-1)}-C \epsilon\right) \omega \geqslant 0$$
if we choose $\epsilon$ sufficiently small. Hence
$$\left(\frac{\partial}{\partial t}-\Delta_{\omega_{\gamma \varepsilon j}(t)}\right) K_{\gamma \varepsilon j}(t) \geqslant 0 .$$
Since $K_{\gamma \varepsilon j}(t)$ tends to $+\infty$ as $x \rightarrow D$, the minimum point of $K_{\gamma \varepsilon j}(t)$ on $\left[t_{0}, T\right] \times X$ with $t_{0} \geqslant 0$ must be outside $D$. The maximum principle shows that
$$\begin{aligned}
& (T-t)\left(\dot{\varphi}_{\gamma \varepsilon j}(t)-\psi_{\gamma}\right)+\left(\varphi_{\gamma \varepsilon j}(t)-t \psi_{\gamma}\right)+n t-\epsilon \log |s|_{h}^{2} \\
\geqslant & \inf _{X}\left(\left(T-t_{0}\right)\left(\dot{\varphi}_{\gamma \varepsilon j}\left(t_{0}\right)-\psi_{\gamma}\right)+\left(\varphi_{\gamma \varepsilon j}\left(t_{0}\right)-t_{0} \psi_{\gamma}\right)\right) .
\end{aligned}$$
Let $\epsilon \rightarrow 0$, and then $j \rightarrow+\infty$ and $\varepsilon \rightarrow 0$, there holds
$$\begin{aligned}
& (T-t)\left(\dot{\varphi}_{\gamma}(t)-\psi_{\gamma}\right)+\left(\varphi_{\gamma}(t)-t \psi_{\gamma}\right)+n t \\
\geqslant & \inf _{X}\left(\left(T-t_{0}\right)\left(\dot{\varphi}_{\gamma}\left(t_{0}\right)-\psi_{\gamma}\right)+\left(\varphi_{\gamma}\left(t_{0}\right)-t_{0} \psi_{\gamma}\right)\right) .
\end{aligned}$$
If we choose $t_{0}=\kappa$, by using Propositions 3.1, 3.5 and 3.7, we have
$$(T-t)\left(\dot{\varphi}_{\gamma}(t)-\psi_{\gamma}\right) \geqslant-C \quad \text { in } \quad X \backslash D$$
for all $t \in[\kappa, T]$ and $0<\gamma \ll 1$, where constant $C$ depends only on $\left\|\varphi_{0}\right\|_{L^{\infty}(X)}, n, \omega, \theta, \eta$ and $T$. Then it implies for any $T^{\prime} \in(\kappa, T)$, there exists a uniform constant $C$ depending only on $\left\|\varphi_{0}\right\|_{L^{\infty}(X)}, n, \omega, \theta, \eta, T^{\prime}$ and $T$ such that
$$\dot{\varphi}_{\gamma}(t) \geqslant \psi_{\gamma}-C \quad \text { in } \quad X \backslash D$$
for all $t \in\left[\kappa, T^{\prime}\right]$ and $0<\gamma \ll 1$. \(\square\)

Remark 3.10. In fact, the constant $C$ in (3.44) also depends on $\kappa$. Since $\kappa$ depends only on $\eta, \theta$ and $\omega$, we will no longer mention that the constant depends on it in the following arguments.

Combining Proposition 3.7 with Proposition 3.9, we have the following uniform estimates.
Corollary 3.11. There exist uniform constants $\sigma$, and a uniform constant $C$ depending only on $\left\|\varphi_{0}\right\|_{L^{\infty}(X)}, n, \omega, \theta, \eta$ and $T$ such that
$$\sigma\left(\dot{\varphi}_{\gamma}(t)-\psi_{\gamma}\right) \geqslant n \log t-C \quad \text { in } \quad X \backslash D$$
for all $t \in(0, T]$ and $0<\gamma \ll 1$.
Proposition 3.12. For any $0<T<T_{\text {max }}^{\eta}$, there exists a uniform constant $C$ depending only on $\left\|\varphi_{0}\right\|_{L^{\infty}(X)}, n, \omega, \theta, \eta$ and $T$ such that for any $t \in[0, T]$ and $0<\gamma \ll 1$,
$$\varphi_{\gamma}(t) \geqslant t \psi_{\gamma}-C \quad \text { on } \quad X .$$
Proof. From Proposition 3.5, we need only consider the case $t \geqslant 1$. In this case, Corollary 3.11 implies that there exists a uniform constant $C$ depending only on $\left\|\varphi_{0}\right\|_{L^{\infty}(X)}, n, \omega, \theta, \eta$ and $T$ such that
$$\dot{\varphi}_{\gamma}(t)-\psi_{\gamma} \geqslant-C \quad \text { in } \quad X \backslash D$$
for all $t \in[1, T]$ and $0<\gamma \ll 1$.
Integrating (3.56) from 1 to $t$ on both sides, we have
$$\varphi_{\gamma}(t)-\varphi_{\gamma}(1) \geqslant(t-1) \psi_{\gamma}-C(t-1) \quad \text { on } \quad X,$$
which implies that
$$\varphi_{\gamma}(t) \geqslant t \psi_{\gamma}+\varphi_{\gamma}(1)-\psi_{\gamma}-C(t-1) \quad \text { on } \quad X .$$
Then inequality (3.55) follows from Proposition 3.5. \(\square\)

\section*{4. High order uniform estimates}

In this section, we show the high order uniform estimates along the twisted conical Kähler-Ricci flow. The most important one is the uniform Laplacian $C^{2}$-estimate, where the key step is to compare $\omega_{\gamma}(t)$ with the conical Kähler metric $\omega_{\gamma}$. Since we only obtain the uniform estimates on the metric potential with respect to the metric $\omega_{\gamma t}+t \sqrt{-1} \partial \bar{\partial} \psi_{\gamma}$ which is a conical Kähler metric depending on $t$, there is on uniform lower bound on $\omega_{\gamma t}+t \sqrt{-1} \partial \bar{\partial} \psi_{\gamma}$ for all $t>0$ and so we need some new arguments. First, we recall the following uniform estimates on the holomorphic bisectional curvature of $\omega_{\gamma}$, which was proved by Guenancia [24].

Lemma 4.1 (Theorem 3.2 in [24]). There exists a constant $C$ depending only on $X$ such that for all $\gamma \in\left(0, \frac{1}{2}\right]$, the holomorphic bisectional curvature of $\omega_{\gamma}$ is bounded by $C$.

Next, we prove the uniform Laplacian $C^{2}$-estimate by constructing a new auxiliary function whose originality lies in the new terms $(t-\tau)\left(\dot{\varphi}_{\gamma}(t)-\psi_{\gamma}\right)$ (with uniform small positive constant $\tau)$ and $\log (t-\delta)$ added. The main reason for adding the first term is that in this proof, we need to derive a negative term $-\tau \operatorname{tr}_{\omega_{\gamma}(t)} \omega_{\gamma}$ with uniform coefficient $\tau>0$ for all $0<t<T$ and $0<\gamma \ll 1$ to cancel the term $\operatorname{tr}_{\omega_{\gamma}(t)} \omega_{\gamma}$ coming from the evolution equation of $\log \operatorname{tr}_{\omega_{\gamma}(t)} \omega_{\gamma}$. But the background metric considered here is $\omega_{\gamma t}+t \sqrt{-1} \partial \bar{\partial} \psi_{\gamma}$, which can only contribute the term $-t \operatorname{tr}_{\omega_{\gamma}(t)} \omega_{\gamma}$ and so there is no uniform bound for all $t>0$. So we add the term $A(t-\tau)\left(\dot{\varphi}_{\gamma}(t)-\psi_{\gamma}\right)$ in the new auxiliary function. Moreover, the second new term $\log (t-\delta)$ ensures the maximum point of the auxiliary function can not be attained at the time $t=\delta$.
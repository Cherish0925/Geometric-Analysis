---
retention_scope: session
part: 1
total_parts: 2
---

[Part 1/2 of: Ricci Flow Singularity for Triaxial Bianchi IX Metric]

---
source_file: 1911_09797.pdf
converter: mathpix
format: mmd
---

\title{
RICCI FLOW SINGULARITY FOR TRIAXIAL BIANCHI IX METRIC
}

\author{
M. SYAFIQ JOHAR
}

\begin{abstract}
In this work, we are going to find sufficient conditions on the initial triaxial Bianchi IX metric on some 4-dimensional manifolds foliated by homogeneous $S^{3}$ for a Type I singularity to occur when it is flowed under the Ricci flow. This work generalises the study on rotationally symmetric manifolds done by Angenent and Isenberg [3] as well as the work of Isenberg, Knopf, and Šešum [6], in which they introduced some ansatz for the problem setup.
\end{abstract}

Contents
\begin{itemize}
\item[1.] Introduction
\end{itemize}
[1]
\begin{itemize}
\item[2.] Previous Work
\end{itemize}

2
\begin{itemize}
\item[3.] Proof of Theorem 1.1
\end{itemize}

4
\begin{itemize}
\item[4.] Proof of Theorem 1.2
\end{itemize}

5
Appendix A. Computation of the Ricci Flow Equations
16
Appendix B. Maximum Principles
24
References
26

\section*{1. Introduction}

The Ricci flow is an evolution equation of the metric on a Riemannian manifold $(M, g(t))$ introduced by Richard Hamilton in 1982 for the study of the famous Poincaré conjecture. This metric evolution equation is given by:
$$\begin{aligned}
\frac{\partial}{\partial t} g(t) & =-2 \operatorname{Ric}(g(t)), \\
g(0) & =g_{0},
\end{aligned}$$
where Ric is the Ricci curvature of the metric $g(t)$ at time $t \geq 0$.
This geometric flow has been important in the study of topological properties of manifolds. In particular, it was instrumental in the proof of the Poincaré Conjecture and the Thurston Geometrisation Conjecture by Perelman in early 2000s.

Due to the non-linear nature of the Ricci flow, we can only guarantee the short time existence of the solution to this flow from any initial data. As a result, the flow might run into a singularity at some finite time. The finite-time singularities of the Ricci flow can be classified into two types, which are called the Type I and Type II singularities, depending on the curvature asymptotics.

A Type I singularity occurs in a Ricci flow if the singularity occurs at a finite time $T<\infty$ such that we have the following curvature asymptotics:
$$\sup _{M \times[0, T)}(T-t)|\operatorname{Rm}(\cdot, t)|_{g}<\infty,$$
and by dichotomy, Type II singularity occurs if we have the following curvature asymptotics:
$$\sup _{M \times[0, T)}(T-t)|\operatorname{Rm}(\cdot, t)|_{g}=\infty,$$
where Rm is the Riemann curvature tensor and $|\cdot|_{g}$ is the norm on 4-tensors induced from the metric $g$.

Studying the singularities of the Ricci flow has been a long-standing subject of research in differential geometry. There has been an interest in constructing explicit initial data which develop singularities and modelling these singularities with self-similar Ricci flow solutions, which are called the Ricci solitons.

In this work, we are going to give some sufficient conditions for a Type I singularity to develop for the triaxial Bianchi IX metric. The theorems that we are going to prove here are:

Theorem 1.1. Suppose that we run a Ricci flow on the manifold $\left(S^{1} \times S^{3}, g_{0}\right)$ where the initial metric $g_{0}$ is of the form:
$$g_{0}=\phi(z)^{2} d z^{2}+a(z)^{2} \omega^{1} \otimes \omega^{1}+b(z)^{2} \omega^{2} \otimes \omega^{2}+c(z)^{2} \omega^{3} \otimes \omega^{3},$$
for $z \in S^{1}=[0,2 \pi)$ and $0 \leq a(z) \leq b(z) \leq c(z)$. Then the Ricci flow preserves the form of the metric, the ordering of the metric components, and there exist constants $\tilde{C}_{0}, \bar{C}_{0}>0$ depending on the data on the initial data such that for all $(z, t) \in S_{T}^{1}=S^{1} \times[0, T)$, we have:
$$\begin{aligned}
& |b(z, t)-c(z, t)| \leq \tilde{C}_{0} \min (b(z, t), c(z, t)), \\
& |a(z, t)-c(z, t)| \leq \bar{C}_{0} \min (a(z, t), c(z, t)) .
\end{aligned}$$ \(\square\)

Theorem 1.2. There exist open sets of warped metrics on $S^{1} \times S^{3}$ of the form:
$$g=\phi(z)^{2} d z^{2}+a(z)^{2} \omega^{1} \otimes \omega^{1}+b(z)^{2} \omega^{2} \otimes \omega^{2}+c(z)^{2} \omega^{3} \otimes \omega^{3},$$
for $z \in S^{1}=[0,2 \pi)$, satisfying:
\begin{itemize}
\item[(1)] $0<a \leq b \leq c<2 a$ at $t=0$,
\item[(2)] $\min _{s, t=0}(\mathrm{~S}) \geq 0$ at $t=0$,
\item[(3)] there exists a $T<\infty$ such that $\limsup _{t \rightarrow T} \max _{s}|\operatorname{Ric}(s, t)|=\infty$,
\end{itemize}
such that all solutions of the Ricci flow originating in these sets develop local neckpinch singularities at some $T<\infty$. Each such solution has the properties that:
\begin{itemize}
\item[(1)] the ordering $a \leq b \leq c$ is preserved,
\item[(2)] the singularity is of Type I with $|\mathrm{Rm}| \leq \frac{C}{\min _{s}\left(a^{2}\right)}$ and $D \sqrt{T-t} \leq \min _{s}(a) \leq C \sqrt{T-t}$ for some constants $C, D>0$. \(\square\)
\end{itemize}

\section*{2. Previous Work}

The first non-trivial concrete example for an initial metric which leads to the Type I singularity has been constructed by Angenent and Knopf in 2004 [3]. In the paper, they constructed this metric by considering a warped product metric on $S^{3}$ of the form:
$$g_{0}=d s^{2}+\psi(s)^{2} \hat{g}_{S^{2}},$$
where $\hat{g}_{S^{2}}$ is the canonical metric on the unit 2-sphere and $\psi(s)$ is a function on the interval $I=\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$. The function $\psi(s)$ describes the radius of the $S^{2}$ spheres which foliate the $S^{3}$ manifold over the interval $I$ such that $\psi$ vanishes at the boundaries of the interval $I$ and $\psi^{\prime}(s) \rightarrow \pm 1$ as $s \rightarrow \mp \frac{\pi}{2}$. This way, they reduced the Ricci flow equation to a one-dimensional parabolic PDE, which simplifies the problem considerably.

This family of explicit examples was generalised further by Isenberg, Knopf, and Šešum [6]. Instead of considering the warped product metric on $S^{3}$ of the form (2.1), they considered a warped product metric on $S^{1} \times S^{3}$. The base of the foliation $S^{1}$ simplifies the analysis in [3] considerably by doing away the technical analysis at the poles of the manifold, which are special orbits of the symmetry. Furthermore, the fibre manifold $S^{3}$ is parallelisable, which means that there exists a global vector field frame $\left\{E_{1}, E_{2}, E_{3}\right\}$ on this manifold. Therefore, a more general form for the metric on the fibre is given by:
$$g=a^{2} \omega^{1} \otimes \omega^{1}+b^{2} \omega^{2} \otimes \omega^{2}+c^{2} \omega^{3} \otimes \omega^{3},$$
for some positive constants $a, b$, and $c$ such that $\left\{\omega^{1}, \omega^{2}, \omega^{3}\right\}$ are dual frames to the vector fields $\left\{E_{1}, E_{2}, E_{3}\right\}$. Instead of this general form, they studied the biaxial case for simplicity; that is, they set $b \equiv c$. In short, they studied the Ricci flow of metrics on $S^{1} \times S^{3}$ of the form:
$$g=\phi(z)^{2} d s^{2}+a(z)^{2} \omega^{1} \otimes \omega^{1}+c(z)^{2}\left(\omega^{2} \otimes \omega^{2}+\omega^{3} \otimes \omega^{3}\right),$$
where $a(z)$ and $c(z)$ are $2 \pi$-periodic positive functions of $z$. Metrics of this form are also known as the biaxial Bianchi IX metric or the warped Berger metric.

Under assumptions on the initial ordering of the metric components $a$ and $c$ as well as curvature assumptions, they managed to find sufficiency conditions for a Type I singularity to occur. Furthermore, with additional conditions, they proved that the singularity resembles a shrinking cylinder after scaling, which is similar to what was done by Angenent and Knopf for the $S^{3}$ case. More specifically, they proved:

Theorem 2.1. [6] The eccentricity of every warped Berger solution of Ricci flow is uniformly bounded: there exists a constant $C_{0}>0$ depending only on the initial data such that the estimate:
$$|a-c| \leq C_{0} \min (a, c),$$
holds pointwise for as long as the solution exists. \(\square\)

Theorem 2.2. [6] There exist open sets of warped Berger metrics satisfying:
\begin{itemize}
\item[(1)] $0<a \leq c$ at $t=0$,
\item[(2)] $\min _{s, t=0}(\mathrm{~S}) \cdot \max _{s, t=0}\left(c^{2}\right)>-3$ at $t=0$,
\item[(3)] there exists $T<\infty$ such that $\limsup _{t \rightarrow T} \max _{s}|\operatorname{Ric}(s, t)|$,
\end{itemize}
such that all solutions originating in these sets develop local neckpinch singularities at some $T<\infty$. Each such solution has the properties that:
\begin{itemize}
\item[(1)] the ordering $a \leq c$ is preserved,
\item[(2)] the singularity is Type I with $|\operatorname{Ric}| \leq \frac{C}{\min _{s}\left(a^{2}\right)}$ and $\frac{\sqrt{T-t}}{C} \leq \min _{s}(a) \leq C \sqrt{T-t}$,
\item[(3)] the diameter of $(M, g)$ is bounded as $t \rightarrow T$.
\end{itemize} \(\square\)

Theorems 1.1 and 1.2 are generalisations of Theorems 2.1 and 2.2, which were proven in [6]. In our case, we assume that the metric quantity $b$ is not identically equal to $c$. The main difficulty in proving our theorems is that we have to control three quantities instead of just two. In some of the equations that we are going to study, these quantities and their derivatives might be coupled. These will be dealt by utilising Young's inequality to separate the various terms. Furthermore, in order to deal with the resulting inequalities, we have to impose the extra condition such that $a \leq c<2 a$ at initial time, which was not present in Theorem 2.2.

\section*{3. Proof of Theorem 1.1}

From Appendix A and the work done by Isenberg, Knopf, and Šešum, we know that the Ricci flow equation from the metrics on $S^{1} \times S^{3}$ with initial metric of the form (1.5) would preserve the symmetry and form of the metric. This is true since the metric quantities evolve according to the semilinear parabolic system of equations:
$$\begin{aligned}
& \partial_{t} a=a^{\prime \prime}+a^{\prime}\left(\frac{b^{\prime}}{b}+\frac{c^{\prime}}{c}\right)-2 a\left(\frac{a^{4}-\left(b^{2}-c^{2}\right)^{2}}{(a b c)^{2}}\right), \\
& \partial_{t} b=b^{\prime \prime}+b^{\prime}\left(\frac{a^{\prime}}{a}+\frac{c^{\prime}}{c}\right)-2 b\left(\frac{b^{4}-\left(a^{2}-c^{2}\right)^{2}}{(a b c)^{2}}\right), \\
& \partial_{t} c=c^{\prime \prime}+c^{\prime}\left(\frac{a^{\prime}}{a}+\frac{b^{\prime}}{b}\right)-2 c\left(\frac{c^{4}-\left(a^{2}-b^{2}\right)^{2}}{(a b c)^{2}}\right),
\end{aligned}$$
along with the commutator relation $\left[\partial_{t}, \partial_{s}\right]=-\left(\frac{a^{\prime \prime}}{a}+\frac{b^{\prime \prime}}{b}+\frac{c^{\prime \prime}}{c}\right) \partial_{s}$. We now prove that the initial ordering of the metric components is also preserved under the Ricci flow.

Lemma 3.1. [6] If $0<a(z, 0) \leq b(z, 0) \leq c(z, 0)$, then under the Ricci flow this ordering is preserved for all $t>0$ for which the flow exists. \(\square\)

Proof. Consider the parabolic PDEs satisfied by the quantities $\frac{\xi}{a}=\frac{a-b}{a}$ and $\frac{\zeta}{b}=\frac{b-c}{b}$. They evolve according to the equations (A.15) and (A.17). Thus, the maximum principles hold here where the parabolic boundary $\mathscr{P} S_{T}^{1}=S^{1} \times\{0\}$ is simply the base $S^{1}$ at initial time. Note that $a \leq b \leq c$ initially. By applying Theorem B. 4 to the equation for $\frac{\xi}{a}$ and Theorem B. 2 to the equation for $\frac{\zeta}{b}$, we deduce that $\frac{\xi}{a} \leq 0$ and $\frac{\zeta}{b} \leq 0$ in $S_{T}^{1}$ and hence we have $0<a \leq b \leq c$ for all $(z, t) \in S_{T}^{1}$. \(\square\)

Furthermore, by using Theorem B. 2 on equations (A.17)-(A.20), in the same vein as the proof by Isenberg, Knopf, and Šešum, we can deduce the eccentricity result in Theorem 1.1.

Proof of Theorem 1.1. We consider equations (A.17) and (A.18). Since $0<a \leq c$ for all time $t \in[0, T)$, we can deduce the following inequalities:
$$\begin{aligned}
& -4\left(\frac{1}{a^{2}}-\frac{1}{c^{2}}+\frac{b^{2}}{a^{2} c^{2}}+\frac{b^{2}+c^{2}-a^{2}}{a^{2} b c}\right)=-4\left(b^{2}+c^{2}-a^{2}\right)\left(\frac{1}{a^{2} c^{2}}+\frac{1}{a^{2} b c}\right) \leq 0, \\
& -4\left(\frac{1}{a^{2}}-\frac{1}{b^{2}}+\frac{c^{2}}{a^{2} b^{2}}+\frac{b^{2}+c^{2}-a^{2}}{a^{2} b c}\right)=-4\left(b^{2}+c^{2}-a^{2}\right)\left(\frac{1}{a^{2} b^{2}}+\frac{1}{a^{2} b c}\right) \leq 0 .
\end{aligned}$$

By applying Theorem B.2, there exist some constants $C_{1}, C_{2}>0$ which depend only on the data on $\mathscr{P} S_{T}^{1}$ such that $\left|\frac{\zeta}{c}\right| \leq C_{1}$ and $\left|\frac{\zeta}{b}\right| \leq C_{2}$. If we choose $\tilde{C}_{0}=\max \left(C_{1}, C_{2}\right)$, then $|b-c| \leq \tilde{C} \min (b, c)$ for all $(z, t) \in S_{T}^{1}$. Similarly, by applying Theorem B. 2 to equations (A.19) and (A.20) as well as noting that $c \geq b$, there exists a constant $\hat{C}_{0}>0$ such that $|a-c| \leq \hat{C}_{0} \min (a, c)$ for all $(z, t) \in S_{T}^{1}$. \(\square\)

In fact, these equations tell us more:
Lemma 3.2. Suppose that at time $t=0$ we have $0<a$ and $1 \leq \max _{s}\left(\frac{c}{a}\right) \leq \lambda$ for some constant $\lambda \geq 1$. Then $1 \leq \frac{c}{a} \leq \lambda$ for all $(z, t) \in S_{T}^{1}$. \(\square\)

Proof. Since $\frac{\chi}{a}=\frac{a-c}{a}=1-\frac{c}{a}$, the evolution equation for $\frac{c}{a}$ is obtained from equation (A.19) as:
$$\begin{aligned}
\partial_{t}\left(\frac{c}{a}\right)=-\partial_{t}\left(\frac{\chi}{a}\right) & =-\left(\frac{\chi}{a}\right)^{\prime \prime}-\left(2 \frac{a^{\prime}}{a}+\frac{b^{\prime}}{b}\right)\left(\frac{\chi}{a}\right)^{\prime}+4\left(a^{2}+c^{2}-b^{2}\right)\left(\frac{1}{a^{2} b^{2}}+\frac{1}{a b^{2} c}\right)\left(\frac{\chi}{a}\right) \\
& =\left(\frac{c}{a}\right)^{\prime \prime}+\left(2 \frac{a^{\prime}}{a}+\frac{c^{\prime}}{c}\right)\left(\frac{c}{a}\right)^{\prime}+4\left(a^{2}+c^{2}-b^{2}\right)\left(\frac{1}{a^{2} b^{2}}+\frac{1}{a b^{2} c}\right)\left(1-\frac{c}{a}\right) \\
& \leq\left(\frac{c}{a}\right)^{\prime \prime}+\left(2 \frac{a^{\prime}}{a}+\frac{c^{\prime}}{c}\right)\left(\frac{c}{a}\right)^{\prime},
\end{aligned}$$
since $1-\frac{c}{a} \leq 0$. By applying Theorem B.2, we conclude that $\frac{c}{a} \leq \max _{s, t=0}\left(\frac{c}{a}\right)=\lambda$. \(\square\)

\section*{4. Proof of Theorem 1.2}

In this section, we now aim to prove Theorem 1.2. The strategy to prove Theorem 1.2 is to prove several lemmas which bound the metric quantities and trace the spatial minimum of the smallest metric quantity as time progresses. We then show that this spatial minima of the smallest metric quantity can be bounded from above and below by linear functions. Finally, by computing the norm of the Riemann curvature tensor explicitly and using the bound obtained above, we conclude that the singularity that develops during the flow is of Type I.

Since we have the ordering $a(z, t) \leq b(z, t) \leq c(z, t)$ at all points $(z, t) \in S_{T}^{1}$, we wish to study the behaviour of the minima of the function $a$. Intuitively, one can think of the quantity $a$ as the smallest "radius" of the SU(2) fibre at $z$. We define the quantity $\check{a}$ that will be used in our study for the neckpinching of the manifold by:
$$\check{a}(t)=\min _{s}(a(s, t)) .$$

Necessarily, we have $\check{a}(t)>0$ as long as the Ricci flow exists and at this point, $a^{\prime}(s, t)=0$ and $a^{\prime \prime}(s, t) \geq 0$. By picturing a neckpinch, we expect the quantity $a$ would vanish at the singular time; that is, $\check{a}(T)=0$. Furthermore, the spatial global minima, denoted by $\check{a}(t)$, is a Lipschitz continuous function of time [5].

Lemma 4.1. If there exists a $T<\infty$ such that $\check{a}(T)=0$, then $\check{a}(t)^{2} \leq 4(T-t)$. \(\square\)

Proof. We use the original coordinate $z \in[0,2 \pi)$. Since the global spatial minima of the quantity $a$ is a Lipschitz continuous function of time, we may define the derivative $\frac{d}{d t} \check{a}(t)$ in the sense of forward difference quotients as described in [5]. Defining $z(t)$ to be a position of the global spatial minima of $a$ at time $t$, we have:
$$\begin{aligned}
\frac{d}{d t} \check{a}(t) & =\partial_{t} a(z(t), t)=a^{\prime \prime}+a^{\prime}\left(\frac{b^{\prime}}{b}+\frac{c^{\prime}}{c}\right)-2 a\left(\frac{a^{4}-\left(b^{2}-c^{2}\right)^{2}}{(a b c)^{2}}\right) \\
& \geq-2 a\left(\frac{a^{4}-\left(b^{2}-c^{2}\right)^{2}}{(a b c)^{2}}\right) \geq-\frac{2 a^{3}}{b^{2} c^{2}}=-\frac{2}{a} \frac{a^{2}}{b^{2}} \frac{a^{2}}{c^{2}} .
\end{aligned}$$

Next, by the ordering $a \leq b \leq c$ we have $\frac{a^{2}}{b^{2}} \frac{a^{2}}{c^{2}} \leq 1$. Along with the inequality (4.1), we deduce:
$$\frac{d}{d t} \check{a} \geq-\frac{2}{\check{a}} \quad \Rightarrow \quad \frac{d}{d t}\left(\check{a}^{2}\right) \geq-4 .$$

By integrating the differential inequality from $t$ to $T$ and using the fact that $\check{a}(T)=0$, we have $\check{a}(t)^{2} \leq 4(T-t)$ for almost every $t \in[0, T)$. \(\square\)

The lemma above gives us a corollary:

Corollary 4.2. The singular time $T$ for the Ricci flow is bounded below by $T \geq \frac{\breve{a}(0)^{2}}{4}$. \(\square\)

Apart from the upper bound for $\check{a}(t)$, we can also find a similar bound for $\hat{c}(t)=$ $\max (c(s, t))$. Similar as before, this quantity is a Lipschitz continuous function of time [5]. From equation (A.12), along the path for the maximum of $c$ we have:
$$\frac{d}{d t} \hat{c} \leq-2 c\left(\frac{c^{4}-\left(a^{2}-b^{2}\right)^{2}}{(a b c)^{2}}\right)=-\frac{2}{c}\left(\frac{\left(c^{4}-b^{4}\right)+a^{2}\left(2 b^{2}-a^{2}\right)}{(a b)^{2}}\right) \leq 0,$$
which implies that the maximum of $c$ over $S^{1}$ decreases over time. In fact, we have the following estimate:

Lemma 4.3. The maximum of $c$ over $S^{1}$ is bounded above by $\hat{c}(t)^{2} \leq-4 t+\hat{c}(0)^{2}$. \(\square\)

Proof. From inequality 4.2), we study the function $P(x, y)=2+\frac{1}{x^{2} y^{2}}-\frac{x^{2}}{y^{2}}-\frac{y^{2}}{x^{2}}$ since the left hand side of (4.2) is $-\frac{2}{c} P\left(\frac{a}{c}, \frac{b}{c}\right)$. Let $c \leq \lambda a$ at the initial time. Thus, by Lemmas 3.1 and 3.2, we have the ordering $a \leq b \leq c \leq \lambda a$ at all time. Thus, it is sufficient to restrict the domain of the function $P(x, y)$ to $x \in\left[\lambda^{-1}, y\right]$ and $y \in[x, 1]$. We call this domain $\Pi_{\lambda} \subset \mathbb{R}^{2}$.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/b362cabb-c683-448d-a634-831fcb80044e-06.jpg?height=488&width=442&top_left_y=1110&top_left_x=807}
\captionsetup{labelformat=empty}
\caption{Figure 1. Domain $\Pi_{\lambda}$ of the function $P(x, y)$.
The arrows indicate the direction $P(x, y)$ increases.}
\end{figure}

Our aim now is to minimise the function $P$ over the domain $\Pi_{\lambda}$. Since $\operatorname{grad}(P)=$ $\frac{2}{x^{2} y^{2}}\left(\frac{y^{4}-x^{4}-1}{x}, \frac{x^{2}-y^{2}-1}{y}\right)$, we conclude that the there are no global critical points of $P$ over $\mathbb{R}^{2}$. Necessarily, the minimum of $P(x, y)$ on $\Pi_{\lambda}$ lies on $\partial \Pi_{\lambda}$. Along the boundary of $\Pi_{\lambda}$ we have:
$$\begin{aligned}
P(x, x) & =\frac{1}{x^{4}}, \\
P(x, 1) & =2-x^{2}, \\
P\left(\lambda^{-1}, y\right) & =\frac{\lambda^{2}}{y^{2}}-\frac{1}{\lambda^{2} y^{2}}-\lambda^{2} y^{2}+2 .
\end{aligned}$$

We note that the functions $P(x, x)$ and $P(x, 1)$ are strictly decreasing as $x$ increases from $\lambda^{-1}$ to 1. Furthermore, since $\lambda \geq 1, \partial_{y} P\left(\lambda^{-1}, y\right)=\frac{2}{\lambda^{2} y^{3}}\left(1-\lambda^{4} y^{4}-\lambda^{4}\right)<0$ for any $y \in\left[\lambda^{-1}, 1\right]$. So $P\left(\lambda^{-1}, y\right)$ is a decreasing function of $y$. Thus, the minimum of $P(x, y)$ on $\Pi_{\lambda}$ is at the point $(1,1)$ which gives us $P(x, y) \geq P(1,1)=1$. By using this in inequality (4.2), we get:
$$\frac{d}{d t} \hat{c} \leq-\frac{2}{\hat{c}} \quad \Rightarrow \quad \frac{d}{d t}\left(\hat{c}^{2}\right) \leq-4,$$
for all but a finite number of $t \in[0, T)$. By integrating the differential inequality from 0 to $t$, we have $\hat{c}(t)^{2}-\hat{c}(0)^{2} \leq-4 t$ for almost every $t \in[0, T)$, hence the result. \(\square\)

This inequality is sharp and is attained when $a=b=c$; that is, it is attained by the shrinking sphere. The lemma above gives us another corollary:

Corollary 4.4. The singular time $T$ for the Ricci flow is bounded above by $T \leq \frac{\hat{c}(0)^{2}}{4}$. \(\square\)

A consequence of the lemma above is a refinement of Lemma 3.2 using Maximum Principle II in Theorem B.3.

Lemma 4.5. Suppose that at time $t=0$ we have $1 \leq \max _{s}\left(\frac{c}{a}\right) \leq \lambda$ for some constant $\lambda \geq 1$. Then for all $(z, t) \in S_{T}^{1}$ we have the following estimate:
$$1 \leq \frac{c^{2}}{a^{2}} \leq e^{\left(\lambda^{2}-1\right)}\left(\lambda^{2}-1\right)\left(1-\frac{4 t}{\hat{c}(0)^{2}}\right)^{2}+1 .$$ \(\square\)
Proof. Consider the evolution equation for $\frac{c}{a}$ from equation (A.19):
$$\partial_{t}\left(\frac{c}{a}\right)=\left(\frac{c}{a}\right)^{\prime \prime}+\left(2 \frac{a^{\prime}}{a}+\frac{c^{\prime}}{c}\right)\left(\frac{c}{a}\right)^{\prime}+4\left(a^{2}+c^{2}-b^{2}\right)\left(\frac{1}{a^{2} b^{2}}+\frac{1}{a b^{2} c}\right)\left(1-\frac{c}{a}\right) .$$

By defining $u:=\frac{c}{a}$, the equation above can be rewritten as:
$$\partial_{t} u=u^{\prime \prime}+\left(2 \frac{a^{\prime}}{a}+\frac{c^{\prime}}{c}\right) u^{\prime}+\frac{4}{a^{2}}\left(\frac{a^{2}}{b^{2}}-1+\frac{c^{2}}{b^{2}}+\frac{a^{3}}{b^{2} c}+\frac{a c}{b^{2}}-\frac{a}{c}\right)(1-u) .$$
Since $1-u<0$, we want to minimise the coefficient of $1-u$ in the equation above. Using the ordering $a \leq b \leq c$ we have:
$$\begin{aligned}
\partial_{t} u & \leq u^{\prime \prime}+\left(2 \frac{a^{\prime}}{a}+\frac{c^{\prime}}{c}\right) u^{\prime}+\frac{4}{a^{2}}\left(\frac{u+1}{u^{3}}\right)(1-u) \\
& \leq u^{\prime \prime}+\left(2 \frac{a^{\prime}}{a}+\frac{c^{\prime}}{c}\right) u^{\prime}+\frac{4}{c^{2}}\left(\frac{u+1}{u^{3}}\right)(1-u) \\
& \leq u^{\prime \prime}+\left(2 \frac{a^{\prime}}{a}+\frac{c^{\prime}}{c}\right) u^{\prime}+\frac{4}{\hat{c}^{2}}\left(\frac{u+1}{u^{3}}\right)(1-u) \\
& \leq u^{\prime \prime}+\left(2 \frac{a^{\prime}}{a}+\frac{c^{\prime}}{c}\right) u^{\prime}+\frac{4}{\hat{c}(0)^{2}-4 t}\left(\frac{u+1}{u^{3}}\right)(1-u),
\end{aligned}$$
where we used Lemma 4.3 in the last line. We now appeal to Maximum Principle II by solving the following associated ODE:
$$\begin{aligned}
\frac{d v}{d t} & =\frac{4}{\hat{c}(0)^{2}-4 t}\left(\frac{1-v^{2}}{v^{3}}\right), \\
v(0) & =\lambda .
\end{aligned}$$

This is a separable ODE, which we can solve to get:
$$v^{2}-\lambda^{2}+\log \left(\frac{v^{2}-1}{\lambda^{2}-1}\right)=2 \log \left(1-\frac{4 t}{\hat{c}(0)^{2}}\right) \quad \Rightarrow \quad e^{v^{2}-\lambda^{2}}\left(\frac{v^{2}-1}{\lambda^{2}-1}\right)=\left(1-\frac{4 t}{\hat{c}(0)^{2}}\right)^{2} .$$

Maximum Principle II states that $u$ is bounded above by the function $v$ that satisfies equation (4.3). We can solve equation (4.3) for $v$ using the Lambert-W function but this is not expressible in terms of elementary functions. For an explicit bound, since $1 \leq u \leq v$, we have:
$$e^{1-\lambda^{2}}\left(\frac{v^{2}-1}{\lambda^{2}-1}\right) \leq e^{v^{2}-\lambda^{2}}\left(\frac{v^{2}-1}{\lambda^{2}-1}\right)=\left(1-\frac{4 t}{\hat{c}(0)^{2}}\right)^{2},$$
from which we can conclude the result $u^{2} \leq v^{2} \leq e^{\left(\lambda^{2}-1\right)}\left(\lambda^{2}-1\right)\left(1-\frac{4 t}{\hat{c}(0)^{2}}\right)^{2}+1$. \(\square\)
\begin{itemize}
\begin{itemize}
\item[] ![](https://cdn.mathpix.com/cropped/b362cabb-c683-448d-a634-831fcb80044e-08.jpg?height=593&width=1242&top_left_y=323&top_left_x=290)
\end{itemize}
\item[(A)] Evolution of $\check{a}^{2}$ for initial data $\phi_{0}=1, a_{0}=\cos (z)+1.5, b_{0}=\cos (z)+2.5$, and $c_{0}=\cos (z)+3.5$.
![](https://cdn.mathpix.com/cropped/b362cabb-c683-448d-a634-831fcb80044e-08.jpg?height=601&width=1160&top_left_y=1037&top_left_x=372)
\begin{itemize}
\item[(B)] Evolution of $\check{a}^{2}$ for initial data $\phi_{0}=1, a_{0}=\cos (2 z)+1.5, b_{0}=\sin (z)+4$, and $c_{0}=6$.
![](https://cdn.mathpix.com/cropped/b362cabb-c683-448d-a634-831fcb80044e-08.jpg?height=591&width=986&top_left_y=1767&top_left_x=545)
\end{itemize}
\item[(C)] Evolution of $\check{a}^{2}$ for initial data $\phi_{0}=1, a_{0}=\frac{1}{2} \cos (z)+1, b_{0}=\cos (z)+2$, and $c_{0}=2 \cos (z)+4$.
\end{itemize}

Figure 2. Numerical plots for the evolution of $\check{a}(t)^{2}$ for some initial metric.

Now we want to find a lower bound for the quantity $\check{a}(t)$. Numerical simulations in [8] provide some evidence that the function $\check{a}(t)^{2}$ is concave. Some of the plots from [8] can be seen in Figure 2. If one can prove that the function $\check{a}(t)^{2}$ is a concave function of time, then since $\check{a}(0)^{2}>0$ and $\check{a}(T)^{2}=0$, we can bound the function $\check{a}(t)^{2}$ from above and below by non-negative linear functions with strictly negative gradients such that:
$$D(T-t) \leq \check{a}(t)^{2} \leq C(T-t),$$
for some positive constants $C, D>0$.
However, demonstrating the concavity of $\check{a}(t)^{2}$ by considering its second derivative would be complicated in our setting since the first and second derivatives of the other metric quantities along the minima of $a^{2}$ would appear in the analysis and we have no control over the sign of these quantities. One way of proceeding with this is to consider the definition of concavity from first principles; that is, by showing that the following inequality holds for any $t_{1}, t_{2} \in[0, T)$ and $p \in[0,1]$ :
$$\check{a}\left(p t_{1}+(1-p) t_{2}\right)^{2} \geq p \check{a}\left(t_{1}\right)^{2}+(1-p) \check{a}\left(t_{2}\right)^{2} .$$

This is still out of reach of our analysis. However, following the work in [6], by setting an assumption on the initial scalar curvature of the manifold as well as the ratio $\frac{c}{a}$, we can prove the following proposition:

Proposition 4.6. Suppose that at time $t=0$ we have $1 \leq \frac{c}{a}<2$ and the scalar curvature S at initial time is non-negative; that is, $\min _{s, t=0}(\mathrm{~S}) \geq 0$. If there exists a finite time $T>0$ such that $\check{a}(T)=0$, then there exists a uniform constant $D>0$ such that $\check{a}(t)^{2} \geq D(T-t)$. \(\square\)

Proof. Consider the quantity $\log (a b c)$. This quantity evolves according to the PDE:
$$\begin{aligned}
\partial_{t} \log (a b c) & =\frac{\partial_{t} a}{a}+\frac{\partial_{t} b}{b}+\frac{\partial_{t} c}{c} \\
& =\frac{a^{\prime \prime}}{a}+\frac{b^{\prime \prime}}{b}+\frac{c^{\prime \prime}}{c}+2\left(\frac{a^{\prime} b^{\prime}}{a b}+\frac{a^{\prime} c^{\prime}}{a c}+\frac{b^{\prime} c^{\prime}}{b c}\right)-2\left(\hat{K}_{12}+\hat{K}_{13}+\hat{K}_{23}\right) \\
& =\frac{a^{\prime \prime}}{a}+\frac{b^{\prime \prime}}{b}+\frac{c^{\prime \prime}}{c}+2\left(\frac{a^{\prime} b^{\prime}}{a b}+\frac{a^{\prime} c^{\prime}}{a c}+\frac{b^{\prime} c^{\prime}}{b c}\right)-2\left(\frac{2 a^{2} b^{2}+2 a^{2} c^{2}+2 b^{2} c^{2}-a^{4}-b^{4}-c^{4}}{a^{2} b^{2} c^{2}}\right) .
\end{aligned}$$

Since the scalar curvature S satisfies $\partial_{t} \mathrm{~S}=\Delta \mathrm{S}+\frac{n}{2} \mathrm{~S}^{2} \geq \Delta \mathrm{S}$ from equation (A.14), we have $\mathrm{S} \geq 0$ by minimum principle of parabolic equations. From this and the expression for the scalar curvature S, we deduce:
$$\begin{array}{ll} 
& 0 \leq-\left(\frac{a^{\prime \prime}}{a}+\frac{b^{\prime \prime}}{b}+\frac{c^{\prime \prime}}{c}+\frac{a^{\prime} b^{\prime}}{a b}+\frac{a^{\prime} c^{\prime}}{a c}+\frac{b^{\prime} c^{\prime}}{b c}-\frac{2 a^{2} b^{2}+2 a^{2} c^{2}+2 b^{2} c^{2}-a^{4}-b^{4}-c^{4}}{a^{2} b^{2} c^{2}}\right) \\
\Rightarrow & \frac{a^{\prime \prime}}{a}+\frac{b^{\prime \prime}}{b}+\frac{c^{\prime \prime}}{c} \leq-\left(\frac{a^{\prime} b^{\prime}}{a b}+\frac{a^{\prime} c^{\prime}}{a c}+\frac{b^{\prime} c^{\prime}}{b c}\right)+\frac{2 a^{2} b^{2}+2 a^{2} c^{2}+2 b^{2} c^{2}-a^{4}-b^{4}-c^{4}}{a^{2} b^{2} c^{2}} .
\end{array}$$

Thus, we have:
$$\partial_{t} \log (a b c) \leq \frac{a^{\prime} b^{\prime}}{a b}+\frac{a^{\prime} c^{\prime}}{a c}+\frac{b^{\prime} c^{\prime}}{b c}+\frac{a^{2}}{b^{2} c^{2}}+\frac{b^{2}}{a^{2} c^{2}}+\frac{c^{2}}{a^{2} b^{2}}-\frac{2}{a^{2}}-\frac{2}{b^{2}}-\frac{2}{c^{2}} .$$

Furthermore, we have:
$$\begin{aligned}
\frac{a^{\prime} b^{\prime}}{a b}+\frac{a^{\prime} c^{\prime}}{a c}+\frac{b^{\prime} c^{\prime}}{b c} & =\frac{1}{2}(\log (a b c))^{\prime}\left(\frac{a^{\prime}}{a}+\frac{b^{\prime}}{b}+\frac{c^{\prime}}{c}\right)-\frac{1}{2}\left(\left(\frac{a^{\prime}}{a}\right)^{2}+\left(\frac{b^{\prime}}{b}\right)^{2}+\left(\frac{c^{\prime}}{c}\right)^{2}\right) \\
& \leq \frac{1}{2}(\log (a b c))^{\prime}\left(\frac{a^{\prime}}{a}+\frac{b^{\prime}}{b}+\frac{c^{\prime}}{c}\right) .
\end{aligned}$$

So, we acquire the inequality:
$$\begin{aligned}
\partial_{t} \log (a b c) & \leq \frac{1}{2}(\log (a b c))^{\prime}\left(\frac{a^{\prime}}{a}+\frac{b^{\prime}}{b}+\frac{c^{\prime}}{c}\right)+\frac{a^{2}}{b^{2} c^{2}}+\frac{b^{2}}{a^{2} c^{2}}+\frac{c^{2}}{a^{2} b^{2}}-\frac{2}{a^{2}}-\frac{2}{b^{2}}-\frac{2}{c^{2}} \\
\Leftrightarrow \quad \partial_{t}(a b c) & \leq\left(\frac{(a b c)^{\prime}}{2 a b c}\left(\frac{a^{\prime}}{a}+\frac{b^{\prime}}{b}+\frac{c^{\prime}}{c}\right)+\frac{a^{2}}{b^{2} c^{2}}+\frac{b^{2}}{a^{2} c^{2}}+\frac{c^{2}}{a^{2} b^{2}}-\frac{2}{a^{2}}-\frac{2}{b^{2}}-\frac{2}{c^{2}}\right) a b c .
\end{aligned}$$

Since $S^{1}$ is compact, necessarily the global minima of $a b c$ over $s$ satisfies $(a b c)^{\prime}=0$. By using the same argument as in Lemma 4.1, along the path $(z(t), t)$ for the global minima of $a b c$ over $S^{1}$, we have:
$$\frac{d}{d t} a b c \leq\left(\frac{(a b c)^{\prime}}{2 a b c}\left(\frac{a^{\prime}}{a}+\frac{b^{\prime}}{b}+\frac{c^{\prime}}{c}\right)+\frac{a^{2}}{b^{2} c^{2}}+\frac{b^{2}}{a^{2} c^{2}}+\frac{c^{2}}{a^{2} b^{2}}-\frac{2}{a^{2}}-\frac{2}{b^{2}}-\frac{2}{c^{2}}\right) a b c,$$
for all but a finite number of $t \in[0, T)$.
Following the proof by Isenberg, Knopf, and Šešum [6], we wish to bound the term $\frac{a^{2}}{b^{2} c^{2}}+\frac{b^{2}}{a^{2} c^{2}}+\frac{c^{2}}{a^{2} b^{2}}-\frac{2}{a^{2}}-\frac{2}{b^{2}}-\frac{2}{c^{2}}$ by a negative multiple of $\frac{1}{c^{2}}$; that is, for some $\mathfrak{C}>0$, we want:
$$\frac{a^{2}}{b^{2} c^{2}}\left(1+\left(\frac{b^{2}}{a^{2}}-\frac{c^{2}}{a^{2}}\right)^{2}-2 \frac{b^{2}}{a^{2}}-2 \frac{c^{2}}{a^{2}}\right) \leq-\frac{\mathfrak{C}}{c^{2}} .$$

This motivates us to study the polynomial $P(x, y)=1+\left(x^{2}-y^{2}\right)^{2}-2 x^{2}-2 y^{2}=x^{4}+y^{4}-$ $2 x^{2} y^{2}-2 x^{2}-2 y^{2}+1$ since the left hand side of (4.5) is a positive multiple of $P\left(\frac{b}{a}, \frac{c}{a}\right)$. As a result of the ordering $a \leq b \leq c \leq \lambda a$, we restrict the domain of the polynomial $P(x, y)$ to $x \in[1, y]$ and $y \in[x, \lambda]$. We call this domain $\Omega_{\lambda} \subset \mathbb{R}^{2}$.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/b362cabb-c683-448d-a634-831fcb80044e-10.jpg?height=476&width=443&top_left_y=1567&top_left_x=806}
\captionsetup{labelformat=empty}
\caption{Figure 3. Domain $\Omega_{\lambda}$ of the function $P(x, y)$.
The arrows indicate the direction where $P(x, y)$ increases.}
\end{figure}

By examining $\operatorname{grad}(P)=4\left(x\left(x^{2}-y^{2}-1\right),-y\left(x^{2}-y^{2}+1\right)\right)$, we conclude that the critical points of $P$ are (0, 0), (0, ±1), and (±1, 0), all of which lie outside of $\Omega_{\lambda}$. Thus, the maximum of $P(x, y)$ on $\Omega_{\lambda}$ lies on $\partial \Omega_{\lambda}$. Along the boundary of $\Omega_{\lambda}$ we have:
$$\begin{aligned}
& P(x, x)=1-4 x^{2}, \\
& P(1, y)=y^{4}-4 y^{2}, \\
& P(x, \lambda)=1+x^{4}+\lambda^{4}-2 \lambda^{2} x^{2}-2 x^{2}-2 \lambda^{2} .
\end{aligned}$$
$$P(1, y)=y^{4}-4 y^{2}$$

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/b362cabb-c683-448d-a634-831fcb80044e-11.jpg?height=404&width=463&top_left_y=348&top_left_x=824}
\captionsetup{labelformat=empty}
\caption{Figure 4. Plot of $P(1, y)=y^{4}-4 y^{2}$.}
\end{figure}

For any $\lambda>1$, the polynomials $P(x, x)$ and $P(x, \lambda)$ are strictly decreasing as $x$ increases from 1 to $\lambda$. Thus, necessarily, the maximum of $P(x, y)$ on $\Omega_{\lambda}$ lies on the line segment connecting $(1,1)$ to $(1, \lambda)$. From the plot in Figure 4, we note that the maximum of $P(1, y)$ for $y \in[1, \lambda]$ is negative if $\lambda<2$. Thus, a sufficient and necessary condition for the maximum of $P(x, y)$ to be negative in $\Omega_{\lambda}$ is $\lambda<2$. Furthermore, $\max _{\Omega_{\lambda}}(P(x, y))=\max \left(-3, \lambda^{4}-4 \lambda^{2}\right):=$ $-\lambda_{0}$ for some $\lambda_{0}>0$.

Hence, if we have $\frac{c}{a}<2$ at time $t=0$, by compactness of $S^{1}$, there exists a $1<\lambda<2$ such that $\frac{c}{a} \leq \lambda$ at time $t=0$. By virtue of Lemma 3.2, we have $\frac{c}{a} \leq \lambda$ for all $S_{T}^{1}$ and thus:
$$\begin{aligned}
1+\left(\frac{b^{2}}{a^{2}}-\frac{c^{2}}{a^{2}}\right)^{2}-2 \frac{b^{2}}{a^{2}}-2 \frac{c^{2}}{a^{2}}=P\left(\frac{b}{a}, \frac{c}{a}\right) & \leq-\lambda_{0} . \\
\Rightarrow \quad \frac{a^{2}}{b^{2} c^{2}}\left(1+\left(\frac{b^{2}}{a^{2}}-\frac{c^{2}}{a^{2}}\right)^{2}-2 \frac{b^{2}}{a^{2}}-2 \frac{c^{2}}{a^{2}}\right) & \leq-\lambda_{0} \frac{a^{2}}{b^{2} c^{2}}<-\frac{\lambda_{0}}{\lambda^{2} c^{2}},
\end{aligned}$$
since the ordering $a \leq b \leq c \leq \lambda a<2 a$ is preserved under the Ricci flow. From inequality (4.4), along the minimum of $a b c$ we have:
$$\frac{d}{d t} a b c \leq\left(-\frac{\lambda_{0}}{\lambda^{2} c^{2}}\right) a b c=-\frac{\lambda_{0}}{\lambda^{2}} \frac{a b}{c} \leq-\frac{\lambda_{0}}{\lambda^{\frac{10}{3}}}(a b c)^{\frac{1}{3}},$$
where we used the fact that $a \leq b \leq c \leq \lambda a$ and Lemma 3.2 for the last inequality.
By setting $m(t)=a b c(z(t), t)$, for all but a finite number of $t \in[0, T)$ we have:
$$\frac{d}{d t} m(z(t), t) \leq-D_{1} m^{\frac{1}{3}}$$
where $D_{1}=\frac{\lambda_{0}}{\lambda^{\frac{10}{3}}}>0$ is some constant. Integrating this inequality from an arbitrary $t<T$ to $T$ and noting that $m(T)=0$ since $\check{a}(T)=0$, we have $m(t)^{\frac{2}{3}} \geq \frac{2 D_{1}}{3}(T-t)$. Furthermore, by using Lemma 3.2 we obtain the inequality:
$$\check{a}(t)^{3} \geq \frac{1}{\lambda^{2}} a b c(z(t), t)=\frac{1}{\lambda^{2}} m(t) \geq \frac{2 \sqrt{6} D_{1}^{\frac{3}{2}}}{9 \lambda^{2}}(T-t)^{\frac{3}{2}},$$
and thus $\check{a}(t)^{2} \geq D(T-t)$ for the constant $D=\frac{2}{3} \frac{\lambda_{0}}{\lambda^{\frac{14}{3}}}>0$ where $\lambda_{0}=\min \left(3,4 \lambda^{2}-\lambda^{4}\right)$. \(\square\)

The next step is to find the bounds for the first and second derivatives of the metric components. This is required since they appear in the curvature quantities of the metric $g$. We prove:

Lemma 4.7. Suppose that $a \leq b \leq c \leq \lambda a$ for some $1<\lambda<2$ at time $t=0$. Then for all $(s, t) \in S_{T}^{1}$ there exist constants $C_{1}(\lambda), C_{2}(\lambda), C_{3}(\lambda)>0$ such that:
$$\begin{aligned}
& \left|a^{\prime}(s, t)\right| \leq C_{1}(\lambda) \leq \max \left(\frac{280 \sqrt{3}}{9}, \max _{s}\left(\left|a^{\prime}(s, 0)\right|\right)\right), \\
& \left|b^{\prime}(s, t)\right| \leq C_{2}(\lambda) \leq \max \left(\frac{4 \sqrt{57}}{3}, \max _{s}\left(\left|b^{\prime}(s, 0)\right|\right)\right), \\
& \left|c^{\prime}(s, t)\right| \leq C_{3}(\lambda) \leq \max \left(\frac{10 \sqrt{93}}{9}, \max _{s}\left(\left|c^{\prime}(s, 0)\right|\right)\right) .
\end{aligned}$$ \(\square\)
Proof. We recall the evolution equation for $a^{\prime}$ in (A.21):
$$\begin{aligned}
\partial_{t}\left(a^{\prime}\right)= & a^{\prime \prime \prime}+a^{\prime \prime}\left(\frac{b^{\prime}}{b}+\frac{c^{\prime}}{c}-\frac{a^{\prime}}{a}\right)-a^{\prime}\left(\frac{\left(b^{\prime}\right)^{2}}{b^{2}}+\frac{\left(c^{\prime}\right)^{2}}{c^{2}}+\frac{6 a^{4}+2\left(b^{2}-c^{2}\right)^{2}}{(a b c)^{2}}\right) \\
& +4\left(\frac{a^{3} b^{\prime}}{b^{3} c^{2}}+\frac{a^{3} c^{\prime}}{b^{2} c^{3}}-\frac{c^{2} b^{\prime}}{a b^{3}}-\frac{b^{2} c^{\prime}}{a c^{3}}+\frac{c c^{\prime}}{a b^{2}}+\frac{b b^{\prime}}{a c^{2}}\right) .
\end{aligned}$$

We denote $\tilde{a}^{\prime}=\max _{s}\left(a^{\prime}(s, t)\right)$. By using the same method as in Lemma 4.1, we have $\tilde{a}^{\prime \prime} \leq 0$ and $\tilde{a}^{\prime}=0$ along the path $(z(t), t)$ for the maximum value of $a^{\prime}$. We substitute this in (4.6):
$$\begin{aligned}
\frac{d}{d t} \tilde{a}^{\prime} \leq & -\tilde{a}^{\prime}\left(\frac{\left(b^{\prime}\right)^{2}}{b^{2}}+\frac{\left(c^{\prime}\right)^{2}}{c^{2}}+\frac{6 a^{4}+2\left(b^{2}-c^{2}\right)^{2}}{(a b c)^{2}}\right)+4\left(\frac{a^{3} b^{\prime}}{b^{3} c^{2}}+\frac{a^{3} c^{\prime}}{b^{2} c^{3}}-\frac{c^{2} b^{\prime}}{a b^{3}}-\frac{b^{2} c^{\prime}}{a c^{3}}+\frac{c c^{\prime}}{a b^{2}}+\frac{b b^{\prime}}{a c^{2}}\right) \\
= & -\tilde{a}^{\prime}\left(\frac{\left(b^{\prime}\right)^{2}}{b^{2}}+\frac{\left(c^{\prime}\right)^{2}}{c^{2}}+\frac{6 a^{2}}{b^{2} c^{2}}+\frac{2 b^{2}}{a^{2} c^{2}}+\frac{2 c^{2}}{a^{2} b^{2}}\right)+\frac{4 \tilde{a}^{\prime}}{a^{2}} \\
& +4\left(\frac{a^{3} b^{\prime}}{b^{3} c^{2}}+\frac{a^{3} c^{\prime}}{b^{2} c^{3}}-\frac{c^{2} b^{\prime}}{a b^{3}}-\frac{b^{2} c^{\prime}}{a c^{3}}+\frac{c c^{\prime}}{a b^{2}}+\frac{b b^{\prime}}{a c^{2}}\right) .
\end{aligned}$$

To deal with the terms in the second bracket on the right hand side of the inequality (4.7) we use Young's inequality on each of them. So, for any $\varepsilon_{i}>0$ for $i=1,2,3,4,5,6$, we have:
$$\begin{aligned}
\frac{a^{3} b^{\prime}}{b^{3} c^{2}} & \leq \frac{\varepsilon_{1}}{2} \frac{\left(b^{\prime}\right)^{2}}{b^{2}}+\frac{1}{2 \varepsilon_{1}} \frac{a^{6}}{b^{4} c^{4}} \leq \frac{\varepsilon_{1}}{2} \frac{\left(b^{\prime}\right)^{2}}{b^{2}}+\frac{1}{2 \varepsilon_{1}} \frac{a^{2}}{b^{2} c^{2}}, \\
\frac{a^{3} c^{\prime}}{b^{2} c^{3}} & \leq \frac{\varepsilon_{2}}{2} \frac{\left(c^{\prime}\right)^{2}}{c^{2}}+\frac{1}{2 \varepsilon_{2}} \frac{a^{6}}{b^{4} c^{4}} \leq \frac{\varepsilon_{2}}{2} \frac{\left(c^{\prime}\right)^{2}}{c^{2}}+\frac{1}{2 \varepsilon_{2}} \frac{a^{2}}{b^{2} c^{2}}, \\
-\frac{c^{2} b^{\prime}}{a b^{3}} & \leq \frac{\varepsilon_{3}}{2} \frac{\left(b^{\prime}\right)^{2}}{b^{2}}+\frac{1}{2 \varepsilon_{3}} \frac{c^{4}}{a^{2} b^{4}} \leq \frac{\varepsilon_{3}}{2} \frac{\left(b^{\prime}\right)^{2}}{b^{2}}+\frac{1}{2 \varepsilon_{3}} \frac{\lambda^{2} c^{2}}{a^{2} b^{2}}, \\
-\frac{b^{2} c^{\prime}}{a c^{3}} & \leq \frac{\varepsilon_{4}}{2} \frac{\left(c^{\prime}\right)^{2}}{c^{2}}+\frac{1}{2 \varepsilon_{4}} \frac{b^{4}}{a^{2} c^{4}} \leq \frac{\varepsilon_{4}}{2} \frac{\left(c^{\prime}\right)^{2}}{c^{2}}+\frac{1}{2 \varepsilon_{4}} \frac{b^{2}}{a^{2} c^{2}}, \\
\frac{b b^{\prime}}{a c^{2}} & \leq \frac{\varepsilon_{5}}{2} \frac{\left(b^{\prime}\right)^{2}}{b^{2}}+\frac{1}{2 \varepsilon_{5}} \frac{b^{4}}{a^{2} c^{4}} \leq \frac{\varepsilon_{5}}{2} \frac{\left(b^{\prime}\right)^{2}}{b^{2}}+\frac{1}{2 \varepsilon_{5}} \frac{b^{2}}{a^{2} c^{2}}, \\
\frac{c c^{\prime}}{a b^{2}} & \leq \frac{\varepsilon_{6}}{2} \frac{\left(c^{\prime}\right)^{2}}{c^{2}}+\frac{1}{2 \varepsilon_{6}} \frac{c^{4}}{a^{2} b^{4}} \leq \frac{\varepsilon_{6}}{2} \frac{\left(c^{\prime}\right)^{2}}{c^{2}}+\frac{1}{2 \varepsilon_{6}} \frac{\lambda^{2} c^{2}}{a^{2} b^{2}},
\end{aligned}$$
where we used the fact that the ordering $a \leq b \leq c \leq \lambda a$ is preserved for all $t>0$. For a crude bound, we set $\varepsilon_{1}=\varepsilon_{2}, \varepsilon_{3}=\varepsilon_{6}$, and $\varepsilon_{4}=\varepsilon_{5}$. Therefore, we deduce:
$$\begin{gathered}
4\left(\frac{a^{3} b^{\prime}}{b^{3} c^{2}}+\frac{a^{3} c^{\prime}}{b^{2} c^{3}}-\frac{c^{2} b^{\prime}}{a b^{3}}-\frac{b^{2} c^{\prime}}{a c^{3}}+\frac{c c^{\prime}}{a b^{2}}+\frac{b b^{\prime}}{a c^{2}}\right) \leq 2\left(\varepsilon_{1}+\varepsilon_{3}+\varepsilon_{5}\right)\left(\frac{\left(b^{\prime}\right)^{2}}{b^{2}}+\frac{\left(c^{\prime}\right)^{2}}{c^{2}}\right)+\frac{1}{\varepsilon_{1}} \frac{4 a^{2}}{b^{2} c^{2}} \\
+\frac{1}{\varepsilon_{5}} \frac{4 b^{2}}{a^{2} c^{2}}+\frac{1}{\varepsilon_{3}} \frac{4 \lambda^{2} c^{2}}{a^{2} b^{2}} .
\end{gathered}$$

We want the right hand side of inequality (4.8) to be a positive multiple of the first bracket in the inequality (4.7). In order to choose the constants $\varepsilon_{1}, \varepsilon_{3}, \varepsilon_{5}>0$, we solve the following simultaneous equations for some constant $\mathfrak{C}>0$ :
$$2\left(\varepsilon_{1}+\varepsilon_{3}+\varepsilon_{5}\right)=\mathfrak{C}, \quad 4=6 \mathfrak{C} \varepsilon_{1}, \quad 4=2 \mathfrak{C} \varepsilon_{5}, \quad \text { and } \quad 4 \lambda^{2}=2 \mathfrak{C} \varepsilon_{3} .$$

The system above has a solution $\mathfrak{C}=\sqrt{\frac{16}{3}+4 \lambda^{2}}$ for some $\varepsilon_{1}, \varepsilon_{3}, \varepsilon_{5}>0$. Thus, we obtain:
$$\frac{d}{d t} \tilde{a}^{\prime} \leq\left(\mathfrak{C}-\tilde{a}^{\prime}\right)\left(\frac{\left(b^{\prime}\right)^{2}}{b^{2}}+\frac{\left(c^{\prime}\right)^{2}}{c^{2}}+\frac{6 a^{2}}{b^{2} c^{2}}+\frac{2 b^{2}}{a^{2} c^{2}}+\frac{2 c^{2}}{a^{2} b^{2}}\right)+\frac{4 \tilde{a}^{\prime}}{a^{2}} .$$

Whenever $\tilde{a}^{\prime} \geq \mathfrak{C}$, the first term would be negative whereas the second term will be positive. We want the right hand side to be negative, so we now aim to get rid of the positive term $\frac{4 \tilde{a}^{\prime}}{a^{2}}$ by adding a large enough negative term to it. By assuming $\tilde{a}^{\prime} \geq \mathfrak{C}$, we have:
$$\begin{aligned}
\frac{d}{d t} \tilde{a}^{\prime} & \leq\left(\mathfrak{C}-\tilde{a}^{\prime}\right)\left(\frac{\left(b^{\prime}\right)^{2}}{b^{2}}+\frac{\left(c^{\prime}\right)^{2}}{c^{2}}\right)+\left(\mathfrak{C}-\tilde{a}^{\prime}\right)\left(\frac{6 a^{2}}{b^{2} c^{2}}+\frac{2 b^{2}}{a^{2} c^{2}}+\frac{2 c^{2}}{a^{2} b^{2}}\right)+\frac{4 \tilde{a}^{\prime}}{a^{2}} \\
& =\left(\mathfrak{C}-\tilde{a}^{\prime}\right)\left(\frac{\left(b^{\prime}\right)^{2}}{b^{2}}+\frac{\left(c^{\prime}\right)^{2}}{c^{2}}\right)+\frac{4}{a^{2}}\left(\left(\mathfrak{C}-\tilde{a}^{\prime}\right)\left(\frac{3 a^{4}}{2 b^{2} c^{2}}+\frac{b^{2}}{2 c^{2}}+\frac{c^{2}}{2 b^{2}}\right)+\tilde{a}^{\prime}\right) .
\end{aligned}$$

We now look at the function of two variables $P(x, y)=\frac{3}{2 x^{2} y^{2}}+\frac{x^{2}}{2 y^{2}}+\frac{y^{2}}{2 x^{2}}$ and determine its minimum value in the region $\Omega_{\lambda}$ as in Figure 3 in the proof for Proposition 4.6. Upon calculations, we note that the minimum of $P(x, y)$ in $\Omega_{\lambda}$ occurs at $(x, y)=(\lambda, \lambda)$, which gives us $\min _{\Omega_{\lambda}} P(x, y)=1+\frac{3}{2 \lambda^{4}}$. Hence:
$$\begin{aligned}
\frac{d}{d t} \tilde{a}^{\prime} & \leq\left(\mathfrak{C}-\tilde{a}^{\prime}\right)\left(\frac{\left(b^{\prime}\right)^{2}}{b^{2}}+\frac{\left(c^{\prime}\right)^{2}}{c^{2}}\right)+\frac{4}{a^{2}}\left(\left(\mathfrak{C}-\tilde{a}^{\prime}\right)\left(1+\frac{3}{2 \lambda^{4}}\right)+\tilde{a}^{\prime}\right), \\
& =\left(\mathfrak{C}-\tilde{a}^{\prime}\right)\left(\frac{\left(b^{\prime}\right)^{2}}{b^{2}}+\frac{\left(c^{\prime}\right)^{2}}{c^{2}}\right)+\frac{4}{a^{2}}\left(\left(1+\frac{3}{2 \lambda^{4}}\right) \mathfrak{C}-\frac{3}{2 \lambda^{4}} \tilde{a}^{\prime}\right) .
\end{aligned}$$

Thus, we conclude that $\max _{s}\left(a^{\prime}(s, t)\right)$ cannot exceed $\mathfrak{C}\left(1+\frac{2 \lambda^{4}}{3}\right) \leq \frac{280 \sqrt{3}}{9}$ and $\max _{s}\left(a^{\prime}(s, 0)\right)$. By running a similar argument on the negative of $a$, we obtain the lower bound $\min _{s}\left(a^{\prime}(s, t)\right) \geq$ $-\max \left(\frac{280 \sqrt{3}}{9}, \max _{s}\left(\left|a^{\prime}(s, 0)\right|\right)\right)$, which gives us the desired bound for $a^{\prime}$.

Using arguments identical to the above and noting that the minimum of $P(x, y)$ on the triangles $\left\{(x, y): \frac{1}{2} \leq x \leq 1,1 \leq y \leq 2 x\right\}$ and $\left\{(x, y): \frac{1}{2} \leq x \leq 1, x \leq y \leq 1\right\}$ are $P(1, \sqrt{2})=2$ and $P(1,1)=\frac{5}{2}$ respectively, similar bounds for $b^{\prime}$ and $c^{\prime}$ can be obtained. \(\square\)

By the work of Šešum in [10], we note that a finite time singularity occurs at $T<\infty$ only if:
$$\limsup _{t \nearrow T} \max _{p \in M}|\operatorname{Ric}(p, t)|_{g}=\infty .$$

Furthermore, this singularity is of Type I if we have:
$$\sup _{t \in[0, T)} \max _{p \in M}(T-t)|\operatorname{Rm}(p, t)|_{g} \leq C<\infty,$$
for some constant $C>0$. Thus, we now want to investigate the behaviour of the norm of the Riemann curvature tensor, which is given by:
$$|\operatorname{Rm}|_{g}^{2}=2\left(K_{01}^{2}+K_{02}^{2}+K_{03}^{2}+K_{12}^{2}+K_{13}^{2}+K_{23}^{2}\right) .$$

Lemma 4.8. If $1 \leq \frac{c}{a} \leq \lambda$ for some $\lambda<2$ at $t=0$, then for all $p \in M$ we have:
$$\left|K_{12}(p, t)\right|+\left|K_{13}(p, t)\right|+\left|K_{23}(p, t)\right| \leq \frac{C(\lambda)}{a(\pi(p), t)^{2}},$$
where $\pi: S^{1} \times S^{3} \rightarrow S^{1}$ is the projection map from the manifold $S^{1} \times S^{3}$ to the $S^{1}$ base of the foliation. \(\square\)

Proof. The sectional curvatures $K_{12}, K_{13}$, and $K_{23}$ are given by:
$$\begin{aligned}
& K_{12}=-\frac{a^{\prime} b^{\prime}}{a b}+\frac{\left(a^{2}-b^{2}\right)^{2}-3 c^{4}}{(a b c)^{2}}+\frac{2}{a^{2}}+\frac{2}{b^{2}}, \\
& K_{13}=-\frac{a^{\prime} c^{\prime}}{a c}+\frac{\left(a^{2}-c^{2}\right)^{2}-3 b^{4}}{(a b c)^{2}}+\frac{2}{a^{2}}+\frac{2}{c^{2}}, \\
& K_{23}=-\frac{b^{\prime} c^{\prime}}{b c}+\frac{\left(b^{2}-c^{2}\right)^{2}-3 a^{4}}{(a b c)^{2}}+\frac{2}{b^{2}}+\frac{2}{c^{2}} .
\end{aligned}$$

Thus, by Lemma 4.7 and the fact that $a \leq b \leq c \leq \lambda a$ for all $t \geq 0$, we obtain the bound:
$$\begin{aligned}
\left|K_{12}\right|+\left|K_{13}\right|+\left|K_{23}\right| & \leq \frac{\left|a^{\prime}\right|\left|b^{\prime}\right|}{a b}+\frac{\left|a^{\prime}\right|\left|c^{\prime}\right|}{a c}+\frac{\left|b^{\prime}\right|\left|c^{\prime}\right|}{b c}+\frac{a^{2}}{b^{2} c^{2}}+\frac{b^{2}}{a^{2} c^{2}}+\frac{c^{2}}{a^{2} b^{2}}+\frac{2}{a^{2}}+\frac{2}{b^{2}}+\frac{2}{c^{2}} \\
& \leq \tilde{C}(\lambda)\left(\frac{1}{a b}+\frac{1}{a c}+\frac{1}{b c}\right)+\frac{1}{c^{2}}+\frac{1}{a^{2}}+\frac{1}{\lambda^{2} b^{2}}+\frac{6}{a^{2}} \leq \frac{C(\lambda)^{2}}{a^{2}},
\end{aligned}$$
for some constant $C(\lambda)>0$. \(\square\)

We now want to bound the sectional curvatures $K_{01}, K_{02}$, and $K_{03}$. These curvatures involve the second order derivatives of the quantities $a, b$, and $c$. A similar bound as in Lemma 4.8 may be obtained, but this requires a bit more work.

Lemma 4.9. If $1 \leq \frac{c}{a} \leq \lambda$ for some $\lambda<2$ at $t=0$, then for all $p \in M$ we have:
$$\left|K_{01}(p, t)\right|+\left|K_{02}(p, t)\right|+\left|K_{03}(p, t)\right| \leq \frac{C(\lambda)}{\check{a}(t)^{2}} .$$ \(\square\)
Proof. First we recall the evolution equation for $K_{01}$ computed in (A.27):
$$\begin{aligned}
\partial_{t} K_{01}=\Delta_{g} & K_{01}+2 K_{01}^{2}-2 K_{01}\left(\frac{\left(b^{\prime}\right)^{2}}{b^{2}}+\frac{\left(c^{\prime}\right)^{2}}{c^{2}}+\frac{2 a^{4}+2\left(b^{2}-c^{2}\right)^{2}}{(a b c)^{2}}\right) \\
& +2 K_{02}\left(\frac{2 a^{2}}{b^{2} c^{2}}+\frac{2 b^{2}}{a^{2} c^{2}}-\frac{2 c^{2}}{a^{2} b^{2}}-\frac{a^{\prime} b^{\prime}}{a b}\right)+2 K_{03}\left(\frac{2 a^{2}}{b^{2} c^{2}}+\frac{2 c^{2}}{a^{2} b^{2}}-\frac{2 b^{2}}{a^{2} c^{2}}-\frac{a^{\prime} c^{\prime}}{a c}\right) \\
& +2 \frac{a^{\prime}}{a}\left(-\frac{\left(b^{\prime}\right)^{3}}{b^{3}}-\frac{\left(c^{\prime}\right)^{3}}{c^{3}}+\frac{6 a a^{\prime}}{b^{2} c^{2}}+\frac{4 b b^{\prime}}{a^{2} c^{2}}+\frac{4 c c^{\prime}}{a^{2} b^{2}}-\frac{2 a^{\prime} c^{2}}{a^{3} b^{2}}-\frac{2 a^{\prime} b^{2}}{a^{3} c^{2}}+\frac{4 a^{\prime}}{a^{3}}\right. \\
& \left.-\frac{12 a^{2} b^{\prime}}{b^{3} c^{2}}-\frac{12 a^{2} c^{\prime}}{b^{2} c^{3}}-\frac{4 b^{2} c^{\prime}}{a^{2} c^{3}}-\frac{4 c^{2} b^{\prime}}{a^{2} b^{3}}\right)+4 a^{2}\left(\frac{3\left(b^{\prime}\right)^{2}}{b^{4} c^{2}}+\frac{4 b^{\prime} c^{\prime}}{b^{3} c^{3}}+\frac{3\left(c^{\prime}\right)^{2}}{b^{2} c^{4}}\right) \\
& -\frac{4}{a}\left(\frac{\left(c^{\prime}\right)^{2}}{a b^{2}}+\frac{\left(b^{\prime}\right)^{2}}{a c^{2}}+\frac{3\left(b^{\prime}\right)^{2} c^{2}}{a b^{4}}+\frac{3 b^{2}\left(c^{\prime}\right)^{2}}{a c^{4}}-\frac{4 c c^{\prime} b^{\prime}}{a b^{3}}-\frac{4 b b^{\prime} c^{\prime}}{a c^{3}}\right) .
\end{aligned}$$

We can bound this quantity by using Lemma 4.7 and the fact that $a \leq b \leq c<2 a$ for all $t \geq 0$. Thus, for some positive constants $D_{1}, D_{2}, D_{3}, D_{4}>0$ depending only on $\lambda>0$, we have:
$$\begin{aligned}
\partial_{t} K_{01} & \leq \Delta_{g} K_{01}+2 K_{01}^{2}+D_{1} \frac{K_{01}}{a^{2}}+D_{2} \frac{K_{02}}{a^{2}}+D_{3} \frac{K_{03}}{a^{2}}+\frac{D_{4}}{a^{4}} \\
& \leq \Delta_{g} K_{01}+3 K_{01}^{2}+K_{02}^{2}+K_{03}^{2}+\frac{D_{0}}{a^{4}}
\end{aligned}$$
where we applied the Cauchy-Schwarz inequality to get $D_{0}:=D_{1}^{2}+D_{2}^{2}+D_{3}^{2}+D_{4}$. Furthermore, by using the same estimates and using Young's inequality for the last term in the evolution equation for the quantity $\frac{\left(a^{\prime}\right)^{2}}{a^{2}}$ obtained from (A.24), we obtain:
$$\begin{aligned}
\partial_{t}\left(\frac{\left(a^{\prime}\right)^{2}}{a^{2}}\right)= & \Delta_{g}\left(\frac{\left(a^{\prime}\right)^{2}}{a^{2}}\right)-2 \frac{\left(a^{\prime}\right)^{2}}{a^{2}}\left(2 \frac{\left(a^{\prime}\right)^{2}}{a^{2}}+\frac{\left(b^{\prime}\right)^{2}}{b^{2}}+\frac{\left(c^{\prime}\right)^{2}}{c^{2}}+\frac{4\left(a^{4}+\left(b^{2}-c^{2}\right)^{2}\right)}{a^{2} b^{2} c^{2}}\right) \\
& +8 \frac{a^{\prime}}{a^{2}}\left(\frac{a^{3} b^{\prime}}{b^{3} c^{2}}+\frac{a^{3} c^{\prime}}{b^{2} c^{3}}-\frac{c^{2} b^{\prime}}{a b^{3}}-\frac{b^{2} c^{\prime}}{a c^{3}}+\frac{c c^{\prime}}{a b^{2}}+\frac{b b^{\prime}}{a c^{2}}\right)-2 K_{01}^{2}-4 \frac{\left(a^{\prime}\right)^{2}}{a^{2}} K_{01}, \\
\leq & \Delta_{g}\left(\frac{\left(a^{\prime}\right)^{2}}{a^{2}}\right)+\frac{D_{5}}{a^{4}}-K_{01}^{2},
\end{aligned}$$
where $D_{5}>0$ is a positive constant. By repeating this for the evolution equations of the quantities $\frac{\left(b^{\prime}\right)^{2}}{b^{2}}$ and $\frac{\left(c^{\prime}\right)^{2}}{c^{2}}$ in A.25 and A.26 respectively, for some positive constants $D_{6}, D_{7}>0$ we have the inequalities:
$$\begin{aligned}
& \partial_{t}\left(\frac{\left(b^{\prime}\right)^{2}}{b^{2}}\right) \leq \Delta_{g}\left(\frac{\left(b^{\prime}\right)^{2}}{b^{2}}\right)+\frac{D_{6}}{a^{4}}-K_{02}^{2}, \\
& \partial_{t}\left(\frac{\left(c^{\prime}\right)^{2}}{c^{2}}\right) \leq \Delta_{g}\left(\frac{\left(c^{\prime}\right)^{2}}{c^{2}}\right)+\frac{D_{7}}{a^{4}}-K_{03}^{2} .
\end{aligned}$$

Let us define $P_{+}=K_{01}+3 \frac{\left(a^{\prime}\right)^{2}}{a^{2}}+\frac{\left(b^{\prime}\right)^{2}}{b^{2}}+\frac{\left(c^{\prime}\right)^{2}}{c^{2}} \geq K_{01}$. By linearity, the evolution of the quantity $P_{+}$is governed by the inequality:
$$\partial_{t} P_{+} \leq \Delta_{g} P_{+}+\frac{D}{a^{4}},$$
where $D:=D_{0}+3 D_{5}+D_{6}+D_{7}>0$ is some positive constant. By tracking $\hat{P}_{+}=\max _{s}\left(P_{+}(s, t)\right)$ using the same argument as in Lemma 4.1, we have:
$$\left.\frac{d}{d t} P_{+}(z(t), t)\right) \leq \frac{D}{a^{4}} \leq \frac{D}{\check{a}^{4}},$$
which implies that $P_{+}$, and hence $K_{01}$, cannot blow up to $+\infty$ as long as the metric component $a$ is bounded away from 0.

To bound the sectional curvature $K_{01}$ from below, by using Lemma 4.7 and the fact that $a \leq b \leq c<2 a$ for all $t \geq 0$, we note that there exists a constant $C_{0}>0$ such that:
$$\partial_{t} K_{01} \geq \Delta_{g} K_{01}-3 K_{01}^{2}-K_{02}^{2}-K_{03}^{2}-\frac{C_{0}}{a^{4}} .$$

We now define $P_{-}=K_{01}-3 \frac{\left(a^{\prime}\right)^{2}}{a^{2}}-\frac{\left(b^{\prime}\right)^{2}}{b^{2}}-\frac{\left(c^{\prime}\right)^{2}}{c^{2}} \leq K_{01}$. This quantity satisfies:
$$\partial_{t} P_{-} \geq \Delta_{g} P_{-}-\frac{C}{a^{4}},$$
for some constant $C:=D+3 D_{5}+D_{6}+D_{7}>0$. Tracking the minimum of $P_{-}$, we obtain:
$$\frac{d}{d t} P_{-}(z(t), t) \geq-\frac{C}{a^{4}} \geq-\frac{C}{\check{a}^{4}} .$$

By a similar argument as before, this implies that $P_{-}$, and hence $K_{01}$, cannot approach $-\infty$ as long as the metric quantity $a$ is bounded away from 0 . Both of these arguments imply that the sectional curvature $K_{01}$ is bounded on the manifold for times $[0, T)$ where $T$ is the singular time when the quantity $a$ reaches 0 somewhere.

Since we have shown that $D(T-t) \leq \check{a}(t)^{2} \leq C(T-t)$ for some constants $C, D>0$, by substituting the lower bound for $\check{a}$ in (4.10) and (4.11), we get the inequalities:
$$\begin{aligned}
& \frac{d}{d t} \hat{P}_{+} \leq \frac{D}{(T-t)^{2}}, \\
& \frac{d}{d t} \check{P}_{-} \geq-\frac{C}{(T-t)^{2}},
\end{aligned}$$
for some constants $C, D>0$.
By integrating both of these, for some constants $\tilde{C}, \tilde{D}>0$, we acquire:
$$\left|K_{01}\right| \leq \frac{\tilde{C}}{(T-t)}+\tilde{D} \leq \frac{\tilde{C}+T \tilde{D}}{(T-t)},$$
for all but a finite number of $t \in[0, T)$.
If we substitute the upper bound for $\check{a}^{2}$ in the inequality above, we get the required bound for $\left|K_{01}\right|$. A similar procedure can be used to bound $\left|K_{02}\right|$ and $\left|K_{03}\right|$ using equations (A.28) and (A.29). This proves the lemma. \(\square\)

By putting all of these together, we have:
$$|\operatorname{Rm}|_{g}^{2}=2\left(K_{01}^{2}+K_{02}^{2}+K_{03}^{2}+K_{12}^{2}+K_{13}^{2}+K_{23}^{2}\right) \leq \frac{3 D^{2}}{\check{a}^{4}}+\frac{3 C^{2}}{a^{4}} \leq \frac{\tilde{C}}{\check{a}^{4}},$$
for some finite constant $0<\tilde{C}$. The lower bound for $\check{a}$ in Proposition 4.6 implies the bound $(T-t)^{2}|\operatorname{Rm}|_{g}^{2} \leq C$ for some finite constant $C>0$. If we take the the supremum over $S^{1} \times S^{3}$ and $t \in[0, T)$ on the left hand side, we can show that the curvature asymptotics satisfy the Type I condition as in (1.3).

Finally, we note that the metric constructed by Isenberg, Knopf, and Šešum [6] also satisfies the conditions required for Proposition 4.6, so the set of metrics satisfying the sufficient conditions in Theorem 1.2 is non-empty. Thus, this proves Theorem 1.2.

\section*{Appendix A. Computation of the Ricci Flow Equations}

We can endow the manifold $N=S^{1} \times S^{3}$ with a metric of the form:
$$g=\phi(z)^{2} d z^{2}+a(z)^{2} \omega^{1} \otimes \omega^{1}+b(z)^{2} \omega^{2} \otimes \omega^{2}+c(z)^{2} \omega^{3} \otimes \omega^{3},$$
where $\phi, a, b$, and $c$ are positive $2 \pi$-periodic functions on the base manifold $S^{1}$. Now we wish to calculate the curvature tensors of the metric $g$ in the frame $\left\{\partial_{z}=E_{0}, E_{1}, E_{2}, E_{3}\right\}$ for $N=S^{1} \times S^{3}$. The first thing we have to consider is the derivatives of the frame vector fields. We write the derivatives of the frame vector fields using the symbols $\Sigma_{\alpha \beta}^{\gamma}$ for $\alpha, \beta, \gamma \in$ \{0, 1, 2, 3\} by:
$$\nabla_{E_{\alpha}} E_{\beta}=\Sigma_{\alpha \beta}^{\gamma} E_{\gamma} .$$

Recall that the Christoffel symbols $\Gamma_{i j}^{k}$ are defined via local coordinates. Thus, the symbols $\Sigma_{\alpha \beta}^{\gamma}$ are not the same as Christoffel symbols because the vector fields $\left\{E_{0}, E_{1}, E_{2}, E_{3}\right\}$ on $N$ are not coordinate vector fields. We call $\Sigma_{\alpha \beta}^{\gamma}$ the frame symbols. Using the Koszul formula, we calculate each of the frame symbols. We have that:
$$\begin{aligned}
2 g\left(E_{\gamma}, E_{\gamma}\right) \Sigma_{\alpha \beta}^{\gamma}= & 2 g\left(\nabla_{E_{\alpha}} E_{\beta}, E_{\gamma}\right) \\
= & E_{\alpha} g\left(E_{\beta}, E_{\gamma}\right)+E_{\beta} g\left(E_{\gamma}, E_{\alpha}\right)-E_{\gamma} g\left(E_{\alpha}, E_{\beta}\right) \\
& \quad-g\left(E_{\alpha},\left[E_{\beta}, E_{\gamma}\right]\right)+g\left(E_{\beta},\left[E_{\gamma}, E_{\alpha}\right]\right)+g\left(E_{\gamma},\left[E_{\alpha}, E_{\beta}\right]\right) .
\end{aligned}$$

Remark A.1. Note that the frame symbols $\Sigma_{\alpha \beta}^{\gamma}$ may not be symmetric in the $\alpha$ and $\beta$ indices since the (possibly non-zero) quantity $\left[E_{\alpha}, E_{\beta}\right]$ in the last term is anti-symmetric. This shows us that the frame symbols are not the same as the Christoffel symbols. \(\square\)

Proposition A.2. Let $i, j, k \in\{1,2,3\}$. The frame symbols for the tangent bundle frame $\left\{\partial_{z}=E_{0}, E_{1}, E_{2}, E_{3}\right\}$ on $(M, g)$ are given by:
\begin{itemize}
\item[(1)] $\Sigma_{00}^{0}=\frac{1}{2} g^{00} \partial_{z} g_{00}$,
\item[(2)] $\Sigma_{0 i}^{0}=\Sigma_{i 0}^{0}=\Sigma_{00}^{i}=0$,
\item[(3)] $\Sigma_{j 0}^{i}=\Sigma_{0 j}^{i}=\frac{1}{2} g^{i i} \partial_{z}\left(\delta_{i}^{j} g_{i j}\right)$,
\item[(4)] $\Sigma_{i j}^{0}=-\frac{1}{2} g^{00} \partial_{z}\left(\delta_{i}^{j} g_{i j}\right)$,
\item[(5)] $\Sigma_{i j}^{k}=\hat{\Sigma}_{i j}^{k}=\epsilon_{i j k} g^{k k}\left(g_{i i}-g_{j j}-g_{k k}\right)$ where $\hat{\Sigma}_{i j}^{k}$ is the frame symbol for the fibre metric $\hat{g}_{z}=a(z)^{2} w^{1} \otimes w^{1}+b(z)^{2} w^{2} \otimes w^{2}+c(z)^{2} w^{3} \otimes w^{3}$. \(\square\)
\end{itemize}

Proof. Equation (A.2) can be simplified for certain combinations of $i, j$, and $k$. Note that $E_{1}, E_{2}, E_{3} \in \mathscr{L}\left(T S^{3}\right)$ while $E_{0} \in \mathscr{L}(T B)$, where $\mathscr{L}$ denotes the lift of the respective vector fields to $\Gamma(T M)$. Since $E_{0}$ and $E_{i}$ are in the horizontal and vertical lifts of the tangent bundle of product manifold, we have that $\left[E_{0}, E_{i}\right]=0$ for $i=1,2,3$. Furthermore, the frame is chosen to be orthogonal and $g\left(E_{0}, E_{0}\right)=\phi(z)^{2}=g_{00}$. Thus, if all three indices are 0, then $2 g_{00} \Sigma_{00}^{0}=\partial_{z} g_{00}$. If exactly two of the indices in the frame symbol $\Sigma_{\alpha \beta}^{\gamma}$ are 0, then the frame symbol vanishes identically.

If exactly one of the indices $\alpha, \beta$, or $\gamma$ is 0 , we have $\Sigma_{\alpha \beta}^{\gamma}=\Sigma_{\beta \alpha}^{\gamma}$ since the anti-symmetric term $g\left(E_{\gamma},\left[E_{\alpha}, E_{\beta}\right]\right)$ in (A.2) vanishes. By symmetry, there are two cases: $\Sigma_{j 0}^{i}$ or $\Sigma_{i j}^{0}$. In both cases, the last three terms of A.2 vanish since $\left\{E_{1}, E_{2}, E_{3}\right\}$ is chosen so that $\left[E_{i}, E_{j}\right]=-2 \epsilon_{i j k} E_{k}$. Furthermore, since $E_{0} \perp E_{i}$ for any $i=1,2,3$, only one of the remaining terms survives for both of these symbols. Respectively, we compute $2 g_{i i} \Sigma_{j 0}^{i}=\partial_{z}\left(\delta_{i}^{j} g_{i j}\right)$ and $2 \Sigma_{i j}^{0}=-\partial_{z}\left(\delta_{i}^{j} g_{i j}\right)$, which gives us the result.

Finally, for non-zero indices, if all three indices are the same, then clearly the frame symbols vanish. If exactly two of them are the same, there are three cases: $\Sigma_{i i}^{j}, \Sigma_{j i}^{i}$ or $\Sigma_{i j}^{i}$. In all cases, the first three terms of (A.2) vanish since $a(z), b(z)$, and $c(z)$ are constant in the fibres of each $z \in B$. This implies that the frame symbol $\Sigma_{i j}^{k}$ is the same as the frame symbol $\hat{\Sigma}_{i j}^{k}$ on the fibre $\left(S^{3}, \hat{g}_{z}\right)$. Furthermore, the last three terms also vanish since $\left[E_{i}, E_{i}\right]=0$ and $\left[E_{i}, E_{j}\right]=-2 \epsilon_{i j k} E_{k} \perp E_{i}$.

Thus, the only (possibly) non-vanishing frame symbol of this form is when $i, j$, and $k$ are distinct. Substituting in all the Lie brackets of vector fields, we get $2 g^{k k} \Sigma_{i j}^{k}=2\left(\epsilon_{j k i} g_{i i}-\right.$ $\left.\epsilon_{k i j} g_{j j}-\epsilon_{i j k} g_{k k}\right)$. By permuting the indices of the Levi-Civita symbol, we deduce the desired result. \(\square\)

With these explicitly defined, we can calculate the Riemann curvature tensor components. Note here that we are calculating the tensor with respect to the frame $\left\{\partial_{z}=E_{0}, E_{1}, E_{2}, E_{3}\right\}$ instead of coordinate vector fields, so we denote $\operatorname{Rm}_{\alpha \beta \gamma \delta}=g\left(\operatorname{Rm}\left(E_{\alpha}, E_{\beta}\right) E_{\gamma}, E_{\delta}\right)$ for the indices $\alpha, \beta, \gamma, \delta \in\{0,1,2,3\}$.

Proposition A.3. Let $i, j, k \in\{1,2,3\}$ be distinct indices. The Riemann curvature tensor components in the frame $\left\{\partial_{z}=E_{0}, E_{1}, E_{2}, E_{3}\right\}$ on $(M, g)$ are given by:
\begin{itemize}
\item[(1)] $\mathrm{Rm}_{000 i}=\mathrm{Rm}_{0000}=0$,
\item[(2)] $\operatorname{Rm}_{i 00 j}=0$ and $\operatorname{Rm}_{i 00 i}=\operatorname{Rm}_{0 i i 0}=\frac{1}{4}\left(g^{00} g^{i i} \partial_{z} g_{00} \partial_{z} g_{i i}+g^{i i}\left(\partial_{z} g_{i i}\right)^{2}-2 \partial_{z z} g_{i i}\right)$,
\item[(3)] $\mathrm{Rm}_{i j j k}=\mathrm{Rm}_{i j j 0}=0$ and $\mathrm{Rm}_{i j j i}=-\frac{1}{4} g^{00} \partial_{z} g_{j j} \partial_{z} g_{i i}+\hat{\mathrm{Rm}_{i j j i}}$ where $\hat{\mathrm{Rm}_{i j j i}}=-g^{k k}\left(g_{k k}^{2}-\right.$ $\left.\left(g_{i i}-g_{j j}\right)^{2}\right)-2\left(g_{k k}-g_{j j}-g_{i i}\right)$ is the Riemann curvature tensor of the fibre metric $\hat{g}_{z}$. \(\square\)
\end{itemize}

Proof. From the previous proposition, we note that the frame symbols are only dependent on the variable $z$. The first identity is clear. For the second, we compute:
$$\begin{aligned}
\nabla^{2} E_{0}\left(E_{i}, E_{0}\right)-\nabla^{2} E_{0}\left(E_{0}, E_{i}\right) & =\nabla_{E_{i}} \nabla_{E_{0}} E_{0}-\nabla_{E_{0}} \nabla_{E_{i}} E_{0}-\nabla_{\left[E_{i}, E_{0}\right]} E_{0} \\
& =\nabla_{E_{i}}\left(\Sigma_{00}^{0} E_{0}\right)-\nabla_{E_{0}}\left(\Sigma_{i 0}^{i} E_{i}\right) \\
& =\Sigma_{00}^{0} \Sigma_{i 0}^{i} E_{i}-\partial_{z} \Sigma_{i 0}^{i} E_{i}-\Sigma_{i 0}^{i} \nabla_{E_{0}} E_{i} \\
& =\Sigma_{00}^{0} \Sigma_{i 0}^{i} E_{i}-\partial_{z} \Sigma_{i 0}^{i} E_{i}-\Sigma_{i 0}^{i} \Sigma_{0 i}^{i} E_{i} \\
& =\frac{1}{4} g^{00} g^{i i} \partial_{z} g_{00} \partial_{z} g_{i i} E_{i}-\frac{1}{2} \partial_{z}\left(g^{i i} \partial_{z} g_{i i}\right) E_{i}-\frac{1}{4}\left(g^{i i} \partial_{z} g_{i i}\right)^{2} E_{i} .
\end{aligned}$$

By using the fact that $0=\partial_{s}\left(g^{i i} g_{i i}\right)=g_{i i} \partial_{s} g^{i i}+g^{i i} \partial_{s} g_{i i}$, we can simplify this to:
$$\nabla^{2} E_{0}\left(E_{i}, E_{0}\right)-\nabla^{2} E_{0}\left(E_{0}, E_{i}\right)=\left(\frac{1}{4} g^{00} g^{i i} \partial_{z} g_{00} \partial_{z} g_{i i}+\frac{1}{4}\left(g^{i i} \partial_{z} g_{i i}\right)^{2}-\frac{1}{2} g^{i i} \partial_{z z} g_{i i}\right) E_{i} .$$

By taking the inner product of this quantity with $E_{i}$ and $E_{j}$ and using the symmetries of the Riemann curvature tensor, we obtain the second relation. For the third, we calculate:
$$\begin{aligned}
\nabla^{2} & E_{j}\left(E_{i}, E_{j}\right)-\nabla^{2} E_{j}\left(E_{j}, E_{i}\right) \\
= & \nabla_{E_{i}} \nabla_{E_{j}} E_{j}-\nabla_{E_{j}} \nabla_{E_{i}} E_{j}-\nabla_{\left[E_{i}, E_{j}\right]} E_{j} \\
= & \nabla_{E_{i}}\left(\Sigma_{j j}^{0} E_{0}\right)-\nabla_{E_{j}}\left(\Sigma_{i j}^{k} E_{k}\right)+2 \epsilon_{i j k} \nabla_{E_{k}} E_{j} \\
= & \Sigma_{j j}^{0} \Sigma_{i 0}^{i} E_{i}-\Sigma_{i j}^{k} \Sigma_{j k}^{i} E_{i}+\epsilon_{i j k} \Sigma_{k j}^{i} E_{i} \\
= & -\frac{1}{4} g^{00} g^{i i} \partial_{z} g_{i i} \partial_{z} g_{j j} E_{i}-\epsilon_{i j k} \epsilon_{j k i} g^{i i} g^{k k}\left(g_{i i}-g_{j j}-g_{k k}\right)\left(g_{j j}-g_{k k}-g_{i i}\right) E_{i} \\
& \quad+2 \epsilon_{i j k} \epsilon_{k j i} g^{i i}\left(g_{k k}-g_{j j}-g_{i i}\right) E_{i} \\
= & \left(-\frac{1}{4} g^{00} g^{i i} \partial_{z} g_{j j} \partial_{z} g_{i i}-g^{i i} g^{k k}\left(g_{k k}^{2}-\left(g_{i i}-g_{j j}\right)^{2}\right)-2 g^{i i}\left(g_{k k}-g_{j j}-g_{i i}\right)\right) E_{i} .
\end{aligned}$$

Again, by taking the inner product with $E_{0}, E_{i}$, and $E_{k}$, and using the symmetries of the Riemann curvature tensor, we extract the results. Note that throughout the calculation above, the last two terms do not involve the vector $E_{0}$ at all, hence they are the same as the Riemann curvature tensor $\hat{\mathrm{Rm}}_{i j j k}$ of the fibre metric $\hat{g}_{z}$. \(\square\)

We can also calculate the Ricci tensor components and the sectional curvatures by taking the appropriate traces of the Riemann curvature tensor from above.

Proposition A.4. We have the following Ricci tensor components:
\begin{itemize}
\item[(1)] $\operatorname{Ric}_{\alpha \beta}=0$ for $\alpha \neq \beta$,
\item[(2)] $\left.\operatorname{Ric}_{00}=\frac{1}{4} \sum_{i=1}^{3}\left(g^{00}\left(g^{i i}\right)^{2} \partial_{z} g_{00} \partial_{z} g_{i i}+\left(g^{i i} \partial_{z} g_{i i}\right)^{2}-2 g^{i i} \partial_{z z} g_{i i}\right)\right)$,
\item[(3)] $\operatorname{Ric}_{i i}=\frac{1}{4}\left(g^{00}\left(g^{00} g^{i i} \partial_{z} g_{00} \partial_{z} g_{i i}+g^{i i}\left(\partial_{z} g_{i i}\right)^{2}-2 \partial_{z z} g_{i i}\right)-\sum_{\substack{j=1 \\ j \neq i \\ j \neq k}}^{3} g^{j j}\left(g^{00} \partial_{z} g_{j j} \partial_{z} g_{i i}+4 g^{k k}\left(g_{k k}^{2}-\right.\right.\right.$
$$\left.\left.\left.\left(g_{i i}-g_{j j}\right)^{2}\right)+8\left(g_{k k}-g_{j j}-g_{i i}\right)\right)\right) \text {. }$$ \(\square\)
\end{itemize}

Proposition A.5. For $i, j \in\{1,2,3\}$, the sectional curvatures of the metric $g$ are given by:
\begin{itemize}
\item[(1)] $K_{0 i}=\frac{1}{4} g^{00} g^{i i}\left(g^{00} g^{i i} \partial_{z} g_{00} \partial_{z} g_{i i}+g^{i i}\left(\partial_{z} g_{i i}\right)^{2}-2 \partial_{z z} g_{i i}\right)$,
\item[(2)] $K_{i j}=-\frac{1}{4} g^{00} g^{i i} g^{j j} \partial_{z} g_{i i} \partial_{z} g_{j j}+\hat{K}_{i j}$ where $\hat{K}_{i j}=-g^{i i} g^{j j}\left(g^{k k}\left(g_{k k}^{2}-\left(g_{i i}-g_{j j}\right)^{2}\right)+\left(g_{k k}-\right.\right.$ $\left.g_{j j}-g_{i i}\right)$ ) for $k \neq i, j$ is the sectional curvature of the fibre metric $\hat{g}_{z}$ spanned by $E_{i}$ and $E_{j}$. \(\square\)
\end{itemize}

Recall that we have defined an arclength coordinate in the cylinder-to-sphere rule. The arclength element $d s$ is induced from $\phi(z)$ by defining the arclength coordinate $s(z)=$ $\int_{0}^{z} \phi(w) d w$ and using this coordinate in place of $z$. In fact, this is a more natural geometric quantity as the formulation for the Ricci flow equation written in this coordinate, as we shall see later, is strongly parabolic. Therefore, we would not have to resort to DeTurck's Trick to formulate a system of parabolic PDEs.

If we choose to calculate the symbols in the arclength coordinate frame (that is, $\left\{\partial_{s}=\right.$ $\left.E_{0}, E_{1}, E_{2}, E_{3}\right\}$ ), we simply substitute $g^{00}=1$ in Propositions A.2 A. 5 to get:

Corollary A.6. In the arclength coordinate frame, the Christoffel symbols can be written explicitly as:
\begin{itemize}
\item[(1)] $\Sigma_{00}^{0}=\Sigma_{0 i}^{0}=\Sigma_{i 0}^{0}=\Sigma_{00}^{i}=0$,
\item[(2)] $\Sigma_{j 0}^{i}=\Sigma_{0 j}^{i}=\frac{1}{2} g^{i i} \partial_{s}\left(\delta_{i}^{j} g_{i j}\right)$,
\item[(3)] $\Sigma_{i j}^{0}=-\frac{1}{2} \partial_{s}\left(\delta_{i}^{j} g_{i j}\right)$,
\item[(4)] $\Sigma_{i j}^{k}=\hat{\Sigma}_{i j}^{k}=\epsilon_{i j k} g^{k k}\left(g_{i i}-g_{j j}-g_{k k}\right)$ where $\hat{\Sigma}_{i j}^{k}$ is the frame symbol for the fibre metric $\hat{g}_{s}=a(s)^{2} \omega^{1} \otimes \omega^{1}+b(s)^{2} \omega^{2} \otimes \omega^{2}+c(s)^{2} \omega^{3} \otimes \omega^{3}$. \(\square\)
\end{itemize}

Corollary A.7. In the arclength coordinate frame, the Riemmann curvature tensor components for distinct indices $i, j, k \in\{1,2,3\}$ can be written explicitly as:
\begin{itemize}
\item[(1)] $\mathrm{Rm}_{000 i}=\mathrm{Rm}_{0000}=0$,
\item[(2)] $\operatorname{Rm}_{i 00 j}=0$ and $\operatorname{Rm}_{i 00 i}=\operatorname{Rm}_{0 i i 0}=\frac{1}{4}\left(g^{i i}\left(\partial_{s} g_{i i}\right)^{2}-2 \partial_{s s} g_{i i}\right)$,
\item[(3)] $\mathrm{Rm}_{i j j k}=\mathrm{Rm}_{i j j 0}=0$ and $\mathrm{Rm}_{i j j i}=-\frac{1}{4} \partial_{s} g_{j j} \partial_{s} g_{i i}+\hat{\mathrm{Rm}_{i j j i}}$ where $\hat{\mathrm{Rm}_{i j j i}}=-g^{k k}\left(g_{k k}^{2}-\right.$ $\left.\left(g_{i i}-g_{j j}\right)^{2}\right)-2\left(g_{k k}-g_{j j}-g_{i i}\right)$ is the Riemann curvature tensor of the fibre metric $\hat{g}_{s}$. \(\square\)
\end{itemize}

Corollary A.8. In the arclength coordinate frame, the Ricci curvature tensor components can be written explicitly as:
\begin{itemize}
\item[(1)] $\operatorname{Ric}_{\alpha \beta}=0$ for $\alpha \neq \beta$,
\item[(2)] $\left.\operatorname{Ric}_{00}=\frac{1}{4} \sum_{i=1}^{3}\left(\left(g^{i i} \partial_{s} g_{i i}\right)^{2}-2 g^{i i} \partial_{s s} g_{i i}\right)\right)$,
\item[(3)] $\operatorname{Ric}_{i i}=\frac{1}{4}\left(g^{i i}\left(\partial_{z} g_{i i}\right)^{2}-2 \partial_{z z} g_{i i}-\sum_{\substack{j=1 \\ j \neq i \\ j \neq k}}^{3} g^{j j}\left(\partial_{z} g_{j j} \partial_{z} g_{i i}+4 g^{k k}\left(g_{k k}^{2}-\left(g_{i i}-g_{j j}\right)^{2}\right)+8\left(g_{k k}-\right.\right.\right.$
$$\left.\left.\left.g_{j j}-g_{i i}\right)\right)\right) .$$ \(\square\)
\end{itemize}

Corollary A.9. In the arclength coordinate frame, the sectional curvatures can be written explicitly as:
\begin{itemize}
\item[(1)] $K_{0 i}=\frac{1}{4}\left(\left(g^{i i} \partial_{s} g_{i i}\right)^{2}-2 g^{i i} \partial_{s s} g_{i i}\right)$,
\item[(2)] $K_{i j}=-\frac{1}{4} g^{i i} g^{j j} \partial_{s} g_{i i} \partial_{s} g_{j j}+\hat{K}_{i j}$ where $\hat{K}_{i j}=-g^{i i} g^{j j}\left(g^{k k}\left(g_{k k}^{2}-\left(g_{i i}-g_{j j}\right)^{2}\right)+\left(g_{k k}-g_{j j}-\right.\right.$ $\left.g_{i i}\right)$ ) for $k \neq i, j$ is the sectional curvature of the fibre metric $\hat{g}_{s}$ spanned by $E_{i}$ and $E_{j}$. \(\square\)
\end{itemize}

Explicitly, in the arclength coordinate frame $\left\{\partial_{s}=E_{0}, E_{1}, E_{2}, E_{3}\right\}$, we can calculate the Ricci tensor components of the metric in (A.1) to get:
$$\begin{aligned}
& \operatorname{Ric}_{00}=-\left(\frac{a^{\prime \prime}}{a}+\frac{b^{\prime \prime}}{b}+\frac{c^{\prime \prime}}{c}\right), \\
& \operatorname{Ric}_{11}=-a a^{\prime \prime}-a a^{\prime}\left(\frac{b^{\prime}}{b}+\frac{c^{\prime}}{c}\right)+a^{2}\left(\hat{K}_{12}+\hat{K}_{13}\right), \\
& \operatorname{Ric}_{22}=-b b^{\prime \prime}-b b^{\prime}\left(\frac{a^{\prime}}{a}+\frac{c^{\prime}}{c}\right)+b^{2}\left(\hat{K}_{12}+\hat{K}_{23}\right), \\
& \operatorname{Ric}_{33}=-c c^{\prime \prime}-c c^{\prime}\left(\frac{a^{\prime}}{a}+\frac{b^{\prime}}{b}\right)+c^{2}\left(\hat{K}_{13}+\hat{K}_{23}\right), \\
& \operatorname{Ric}_{\alpha \beta}=0 \quad \text { for } \quad \alpha \neq \beta,
\end{aligned}$$
where:
$$\begin{aligned}
& \hat{K}_{12}=\frac{\left(a^{2}-b^{2}\right)^{2}-3 c^{4}}{(a b c)^{2}}+\frac{2}{a^{2}}+\frac{2}{b^{2}}, \\
& \hat{K}_{13}=\frac{\left(a^{2}-c^{2}\right)^{2}-3 b^{4}}{(a b c)^{2}}+\frac{2}{a^{2}}+\frac{2}{c^{2}}, \\
& \hat{K}_{23}=\frac{\left(b^{2}-c^{2}\right)^{2}-3 a^{4}}{(a b c)^{2}}+\frac{2}{b^{2}}+\frac{2}{c^{2}},
\end{aligned}$$
are the sectional curvature of the SU(2) fibres. These were calculated in Proposition A.5.
The . . .' denotes derivative with respect to the arclength variable $s(z, t)$ via the change of variable $d s=\phi(z, t) d z$. From now on, we denote derivatives with respect to the original variable $z$ and the new gauge $s(z, t)$ by ... and ...' respectively.
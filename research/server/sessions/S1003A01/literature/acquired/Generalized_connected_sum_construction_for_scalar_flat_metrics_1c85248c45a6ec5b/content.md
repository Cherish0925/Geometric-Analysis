---
retention_scope: session
part: 1
total_parts: 1
---

---
source_file: math_0611778.pdf
converter: mathpix
format: mmd
---

\title{
Generalized connected sum construction for scalar flat metrics
}

\author{
L. Mazzieri *
}

June 25, 2018

\section*{1 Introduction and statement of the result}

In this paper we will show that the generalized connected sum construction for constant scalar curvature metrics can be extended to the zero scalar curvature case. In particular we want to construct solutions to the Yamabe equation on the generalized connected sum $M=M_{1} \sharp_{K} M_{2}$ of two compact Riemannian manifolds $\left(M_{1}, g_{1}\right)$ and $\left(M_{2}, g_{2}\right)$ with zero constant scalar curvature along a common (isometrically embedded) submanifold $\left(K, g_{K}\right)$ of codimension $\geq 3$.

We present here two kinds of construction. The first one is the basic model and it works for every couple of scalar flat manifolds, but it has a drawback. In fact following this method we are not allowed to choose a scalar flat metric on the generalized connected sum, although the error can be chosen as small as we want. The second construction is an adjustment of the first one which enable us to get a zero scalar curvature metric on the final manifold, but it require the hypothesis that the starting Riemannian manifolds are non Ricci flat.

In section 2-5 we present the first method. As in the nonzero scalar curvature case, our strategy lies in writing down a family of approximate solution metrics $\left(g_{\varepsilon}\right)_{\varepsilon \in(0,1)}$ (where the parameter $\varepsilon$ represents the size of the tubular neighborhood we excise from each manifold in order to perform the generalized connected sum) and then in finding out a conformal factor $u_{\varepsilon}$ such that for sufficiently small $\varepsilon>0$ the metrics $\tilde{g}_{\varepsilon}=u_{\varepsilon}^{\frac{4}{m-2}} g_{\varepsilon}, \varepsilon \in(0,1)$, are "small" constant scalar curvature metrics. As we claimed before, notice that by this method it is impossible to ensure that the scalar curvature $S=S_{\tilde{g}_{\varepsilon}}$ of the metrics we obtain is exactly zero. Anyway we will show that $S=\mathcal{O}\left(\varepsilon^{n-2}\right)$. Notice also that in order to achieve our goal we will need to scale up or down the initial manifolds by means of suitable homotheties, in other words we need to multiply the initial metrics $g_{1}$ and $g_{2}$ by suitable positive constants; hence, what the submanifold $\left(K, g_{K}\right)$ is actually required to do is to be homothetically embedded

\footnotetext{
*Scuola Normale Superiore di Pisa and Laboratoire d'Analyse et de Mathématiques Appliquées, Université Paris 12. E-mail : l.mazzieri@sns.it
}
in both the initial manifolds, it is to say isometrically embedded modulo homotheties in $M_{1}$ and $M_{2}$. Let us now describe this result more precisely.

Let $\left(M_{1}, g_{1}\right)$ and $\left(M_{2}, g_{2}\right)$ be two $m$-dimensional compact Riemannian manifolds with zero constant scalar curvature, and suppose that there exists a $k$-dimensional Riemannian manifold $\left(K, g_{K}\right)$ which is isometrically embedded in each $\left(M_{i}, g_{i}\right)$, for $i=1,2, m \geq 3, m-k \geq 3$. We also assume that the normal bundles of $K$ in $\left(M_{i}, g_{i}\right)$ can be diffeomorphically identified.

Let $M^{R, Q}=M_{1} \sharp_{K} M_{2}$ be the generalized connected sum of $\left(M_{1}, R g_{1}\right)$ and $\left(M_{2}, Q g_{2}\right)$ along $K$ which is obtained by removing an $\varepsilon$-tubular neighborhood of $K$ from each $M_{i}$ and identifying the two boundaries.

Our main result reads :
Theorem 1.1. Under the above assumptions, for $\varepsilon \in\left(0, \varepsilon_{0}\right)$ and suitable constants $R, Q>0$, it is possible to endow $M^{R, Q}$ with a family of constant scalar curvature metrics $\left(\tilde{g}_{\varepsilon}\right)$, whose scalar curvature $S_{\tilde{g}_{\varepsilon}}$ is a $\mathcal{O}\left(\varepsilon^{n-2}\right)$. In addition the metric $\tilde{g}_{\varepsilon}$ is conformal to the metrics $g_{i}$ away from a fixed (small) tubular neighborhood of $K$ in $M_{i}, i=1,2$ for a conformal factor $u_{\varepsilon}$ which can be chosen so that
$$\left\|u_{\varepsilon}-1\right\|_{L^{\infty}(M)} \leq C r_{\varepsilon}$$
where $r_{\varepsilon}=\mathcal{O}\left(\varepsilon^{1-\gamma}\right), \gamma \in(0,1)$, for $n=3$ and $r_{\varepsilon}=\mathcal{O}(\varepsilon)$ for $n \geq 4$.
Section 6 is devoted to the description of a special device, which works in the non Ricci flat case. In this case we will be able to achieve a scalar flat metric on the final manifold. The strategy lies in making a slight modification of the approximate solution metrics away from the polyneck. If the starting manifolds are non Ricci flat, this construction provide us two correction terms which will be employed in the non-linear analysis in place of the non zero constant scalar curvature and in place of the homotheties in order to get a solution of the Yamabe equation with prescribed zero scalar curvature.

The statement of the theorem is the following
Theorem 1.2. Let $M$ be the generalized connected sum of two Riemannian scalar flat non Ricci flat manifolds $\left(M_{1}, g_{1}\right)$ and $\left(M_{2}, g_{2}\right)$ of dimension $m \geq 3$ along a common isometrically embedded submanifold $\left(K, g_{K}\right)$ of codimension at least 3 . Under these assumptions it is possible to endow $M$ with a family of scalar flat metrics

\section*{2 Geometric construction}

The geometric construction we use here is essentially the same we used in [11], but in order to fix the notation it is useful to transfer it, paying attention in making the appropriate adjustments. Here we describe the construction in the case where $R=Q=1$, but it still holds in the general case. Of course the isometries become
isometries modulo homotheties.

Let $\left(K, g_{K}\right)$ be a $k$-dimensional Riemannian manifold isometrically embedded in both the $n$-dimensional Riemannian manifolds $\left(M_{1}, g_{1}\right)$ and $\left(M_{2}, g_{2}\right)$,
$$\iota_{i}: K \hookrightarrow M_{i}$$
We assume that the isometric map $\iota_{1}^{-1} \circ \iota_{2}: \iota_{1}(K) \rightarrow \iota_{2}(K)$ extends to a diffeomorphism between the normal bundles of $\iota_{i}(K)$ in $\left(M_{i}, g_{i}\right), i=1,2$. We further assume that both the metrics $g_{1}$ and $g_{2}$ have zero constant scalar curvature. In this section our aim is to perform a generalized connected sum of $\left(M_{1}, g_{1}\right)$ and $\left(M_{2}, g_{2}\right)$ along $\left(K, g_{K}\right)$ and to construct on the new manifold $M=M_{1} \sharp_{K} M_{2}$ a family of metrics $\left(g_{\varepsilon}\right)_{\varepsilon \in(0,1)}$, whose scalar curvature is close to zero in a suitable sense.

For a fixed $\varepsilon \in(0,1)$, we describe the generalized connected sum construction and the definition of the metric $g_{\varepsilon}$ in local coordinates, the fact that this construction yields a globally defined metric will follow at once.

Let $U^{k}$ be an open set of $\mathbb{R}^{k}, B^{m-k}$ the $(m-k)$-dimensional open ball $(m-k \geq 3)$. For $i=1,2, F_{i}: U^{k} \times B^{m-k} \rightarrow W_{i} \subset M_{i}$ given by
$$F_{i}(z, x):=\exp _{z}^{M_{i}}(x)$$
defines local Fermi coordinates near the coordinate patches $F_{i}(\cdot, 0)(U) \subset \iota_{i}(K) \subset M_{i}$. In these coordinates, the metric $g_{i}$ can be decomposed as
$$g_{i}(z, x)=g_{j_{1} j_{2}}^{(i)} d z^{j_{1}} \otimes d z^{j_{2}}+g_{\alpha \beta}^{(i)} d x^{\alpha} \otimes d x^{\beta}+g_{j \alpha}^{(i)} d z^{j} \otimes d x^{\alpha}$$
and it is well known that in this coordinate system
$$g_{\alpha \beta}^{(i)}=\delta_{\alpha \beta}+\mathcal{O}\left(|x|^{2}\right) \quad \text { and } \quad g_{j \alpha}^{(i)}=\mathcal{O}(|x|)$$

In order to perform the identification between $W_{1}$ and $W_{2}$ and in order to glue the metrics together and define $g_{\varepsilon}$, we partially change the coordinate system, by setting
$$x=\varepsilon \mathrm{e}^{-t} \theta$$
on $F_{1}^{-1}\left(W_{1}\right)$ and
$$x=\varepsilon \mathrm{e}^{t} \theta$$
on $F_{2}^{-1}\left(W_{2}\right)$, for $\varepsilon \in(0,1), \log \varepsilon<t<-\log \varepsilon, \theta \in S^{m-k-1}$.
Using these changes of coordinates the expressions of the two metrics $g_{1}$ and $g_{2}$ on $U^{k} \times A_{\varepsilon^{2}}^{1}$, where $A_{\varepsilon^{2}}^{1}$ is the annulus $\left\{\varepsilon^{2}<|x|<1\right\}$ become respectively
$$\begin{aligned}
g_{1}(z, t, \theta) & =g_{i j}^{(1)} d z^{i} \otimes d z^{j} \\
& +u_{\varepsilon}^{(1)} \frac{4}{n-2}\left[\left(d t \otimes d t+g_{\lambda \mu}^{(1)} d \theta^{\lambda} \otimes d \theta^{\mu}\right)+g_{t \theta}^{(1)} d t \ltimes d \theta\right] \\
& +g_{i t}^{(1)} d z^{i} \otimes d t+g_{i \lambda}^{(1)} d z^{i} \otimes d \theta^{\lambda}
\end{aligned}$$
and
$$\begin{aligned}
g_{2}(z, t, \theta) & =g_{i j}^{(2)} d z^{i} \otimes d z^{j} \\
& +u_{\varepsilon}^{(2)} \frac{4}{n-2}\left[\left(d t \otimes d t+g_{\lambda \mu}^{(2)} d \theta^{\lambda} \otimes d \theta^{\mu}\right)+g_{t \theta}^{(2)} d t \ltimes d \theta\right] \\
& +g_{i t}^{(2)} d z^{i} \otimes d t+g_{i \lambda}^{(2)} d z^{i} \otimes d \theta^{\lambda}
\end{aligned}$$
where by the compact notation $g_{t \theta} d t \ltimes d \theta$ we indicate the general component of the normal metric tensor (that is, it involves $d t \otimes d t, d \theta^{\lambda} \otimes d \theta^{\mu}$ and $d t \otimes d \theta^{\lambda}$ components).

Remark that for $j=1,2$ we have
$$\begin{array}{ll}
g_{\lambda \mu}^{(j)}=\mathcal{O}(1) & g_{t \theta}^{(j)}=\mathcal{O}\left(|x|^{2}\right) \\
g_{i t}^{(j)}=\mathcal{O}\left(|x|^{2}\right) & g_{i \lambda}^{(j)}=\mathcal{O}\left(|x|^{2}\right)
\end{array}$$
and
$$u_{\varepsilon}^{(1)}(t)=\varepsilon^{\frac{n-2}{2}} \mathrm{e}^{-\frac{n-2}{2} t} \quad \text { and } \quad u_{\varepsilon}^{(2)}(t)=\varepsilon^{\frac{n-2}{2}} \mathrm{e}^{\frac{n-2}{2} t}$$

We choose a cut-off function $\zeta:(\log \varepsilon,-\log \varepsilon) \rightarrow[0,1]$ to be a non increasing smooth function which is identically equal to 1 in $(\log \varepsilon,-1]$ and 0 in $[1,-\log \varepsilon)$ and we choose another cut-off function $\eta:(\log \varepsilon,-\log \varepsilon) \rightarrow[0,1]$ to be a non increasing smooth function which is identically equal to 1 in $(\log \varepsilon,-\log \varepsilon-1]$ and which satisfies $\lim _{t \rightarrow-\log \varepsilon} \eta=0$. Using these two cut-off functions, we can define a new normal conformal factor $u_{\varepsilon}$ by
$$u_{\varepsilon}(t):=\eta(t) u_{\varepsilon}^{(1)}(t)+\eta(-t) u_{\varepsilon}^{(2)}(t)$$
and the metric $g_{\varepsilon}$ by
$$\begin{aligned}
g_{\varepsilon}(z, t, \theta) & :=\left(\zeta g_{i j}^{(1)}+(1-\zeta) g_{i j}^{(2)}\right) d z^{i} \otimes d z^{j} \\
& +u_{\varepsilon}^{\frac{4}{n-2}}\left[d t \otimes d t+\left(\zeta g_{\lambda \mu}^{(1)}+(1-\zeta) g_{\lambda \mu}^{(2)}\right) d \theta^{\lambda} \otimes d \theta^{\mu}\right. \\
& \left.\quad+\left(\zeta g_{t \theta}^{(1)}+(1-\zeta) g_{t \theta}^{(2)}\right) d t \times d \theta\right] \\
& +\left(\zeta g_{i t}^{(1)}+(1-\zeta) g_{i t}^{(2)}\right) d z^{i} \otimes d t \\
& +\left(\zeta g_{i \lambda}^{(1)}+(1-\zeta) g_{i \lambda}^{(2)}\right) d z^{i} \otimes d \theta^{\lambda}
\end{aligned}$$

Closer inspection of this expression shows that the metric $g_{\varepsilon}$ - whose definition can be obviously completed by setting $g_{\varepsilon} \equiv g_{1}$ and $g_{\varepsilon} \equiv g_{2}$ out of the "polyneck" - is a Riemannian metric which is globally defined on the manifold $M$.

Following [11] it is immediate to obtain the estimate for the scalar curvature of the approximate solution metric.

Proposition 2.1. There exists a constant $C>0$ independent of $\varepsilon \in(0,1)$ such that
$$\left|S_{g_{\varepsilon}}\right| \leq C \varepsilon^{-1}(\operatorname{ch} t)^{1-n}$$
for $|t| \leq|\log \varepsilon|-1$.
Of course, when we consider $R g_{1}$ and $Q g_{2}$ as initial metrics the estimate 2 still remains true, but the constant $C$ depends now on the factors $P$ and $Q$.

Another useful tool we can obtain from [11] is the expression for the $g_{\varepsilon}$-laplacian on the polyneck
$$\Delta_{g_{\varepsilon}}=u_{\varepsilon}^{-\frac{4}{n-2}}\left[\partial_{t}^{2}+(n-2) \operatorname{th}\left(\frac{n-2}{2} t\right) \partial_{t}+\Delta_{S^{n-1}}^{(\theta)}+u_{\varepsilon}^{\frac{4}{n-2}} \Delta_{K}^{(z)}+\mathcal{O}(|x|) \Phi\left(\nabla, \nabla^{2}\right)\right]$$
where $\Phi\left(\nabla, \nabla^{2}\right)$ is a nonlinear differential operator involving first order and second order partial derivatives with respect to $t, \theta^{\lambda}$ and $z^{j}$ and whose coefficients are bounded uniformly on the "polyneck", as $\varepsilon \in(0,1)$.

\section*{3 Analysis of a linear operator}

Our aim is now to solve the Yamabe equation
$$\Delta_{g_{\varepsilon}} u+c_{m} S_{g_{\varepsilon}} u=c_{m} S u^{\frac{m+2}{m-2}}$$
where $c_{m}=-(m-2) / 4(m-1)$ and $S=S(\varepsilon)$ is a suitable constant.

Since we want to preserve the structure of the two initial metrics far away from the gluing locus, we are looking for a conformal factor $u$ as close to 1 as we want. For these reasons it is natural to consider the change $u=1+v$ and consequently the equation
$$\begin{aligned}
\Delta_{g_{\varepsilon}} v & =c_{m}\left(S-S_{g_{\varepsilon}}\right)+c_{m}\left(S-S_{g_{\varepsilon}}\right) v+c_{m} \frac{4}{m-2} S v+c_{m} S f(v) \\
& =: F_{\varepsilon}(v)
\end{aligned}$$
where $f(v)=\left((1+v)^{\frac{m+2}{m-2}}-1-\frac{m+2}{m-2} v\right)$.
Since the first eigenvalue $\mu_{\varepsilon}$ of the operator $\Delta_{g_{\varepsilon}}$ is a $\mathcal{O}\left(\varepsilon^{n-2}\right)$, it is not easy to provide a good estimate for the inverse of the laplacian dealing directly with the equation above. It is better, on the other hand, to consider the following problem
$$\Delta_{g_{\varepsilon}} v=F_{\varepsilon}(v)-\lambda(\varepsilon, v) \beta_{\varepsilon}$$
where $\beta_{\varepsilon}=c_{1} \chi_{1}-c_{2} \chi_{2}$, with $c_{1}, c_{2}>0$ and $\chi_{1}, \chi_{2}$ smooth monotone cut-off defined by
$$\chi_{1}= \begin{cases}1 & \text { on } M_{1} \backslash T_{0}^{\varepsilon} \\ 1 & \text { on }\{\log \varepsilon<t<\log \varepsilon+\alpha\} \\ 0 & \text { on }\{\log \varepsilon+\alpha+1<t<0\} \\ 0 & \text { otherwise }\end{cases}$$
$$\chi_{2}= \begin{cases}1 & \begin{array}{l}
\text { on } M_{2} \backslash T_{0}^{\varepsilon} \\
1 \\
\text { on }\{-\log \varepsilon+\alpha<t<-\log \varepsilon\} \\
0
\end{array} \\
\begin{array}{ll}
\text { on }\{0<t<-\log \varepsilon-\alpha-1\} \\
0 & \text { otherwise }
\end{array}\end{cases}$$
is such that $\int_{M} \beta_{\varepsilon} \mathrm{d} \operatorname{vol}_{g_{\varepsilon}}=0$ and $\int_{M} \beta_{\varepsilon}{ }^{2} \mathrm{~d} \operatorname{vol}_{g_{\varepsilon}}$ and we can think of it as an approximation of the first eigenvector of $\Delta_{g_{\varepsilon}}$. In this problem we are looking for a function $v$ and an approximate first eigenvalue $\lambda(\varepsilon, v)$ such that the equation 5 is verified.

Once this problem will be solved, we will show that, by scaling the initial metrics $g_{1}$ and $g_{2}$, the constant $\lambda(\varepsilon, v)$ can be chosen to be zero, providing a solution of the equation 4.

By linearizing the equation 5 we are induced to consider the linear problem
$$\Delta_{g_{\varepsilon}} u=f-\lambda \beta_{\varepsilon}$$
where $f$ is an assigned function such that $\int_{M} f \mathrm{~d} v o l_{g_{\varepsilon}}=0$ and we are looking for a suitable constant $\lambda$ and a solution $u$ which, up to a constant, can be chosen such that $\int_{M} u \mathrm{~d} v o l_{g_{\varepsilon}}=0$.

In order to choose a good functional setting for this linear problem, let us recall the following result from [11]

Proposition 3.1. Given $\gamma \in(0, n-2)$, there exist a real number $\alpha=\alpha(n, \gamma)>0$ and a constant $C_{n, \gamma} \geq 0$ such that for all $\varepsilon \in\left(0, \mathrm{e}^{-\alpha}\right)$ and all $v, f \in \mathcal{C}^{0}\left(T_{\alpha}^{\varepsilon}\right)$ satisfying $\Delta_{g_{\varepsilon}} v=f$, the following estimate holds
$$\sup _{T_{\alpha}^{\varepsilon}}\left|\psi_{\varepsilon}^{\gamma} v\right| \leq C_{n, \gamma}\left(\sup _{T_{\alpha}^{\varepsilon}}\left|\psi_{\varepsilon}^{\gamma+2} f\right|+\sup _{\partial T_{\alpha}^{\varepsilon}}\left|\psi_{\varepsilon}^{\gamma} v\right|\right)$$
where $T_{\rho}^{\varepsilon}:=\{\log \varepsilon+\rho \leq t \leq-\log \varepsilon-\rho\}$, for $\rho>0$ and the weight $\psi_{\varepsilon}$ interpolate smoothly between these definitions in $T_{0}^{\varepsilon} \backslash T_{\alpha}^{\varepsilon}$
$$\psi_{\varepsilon}:= \begin{cases}\varepsilon \operatorname{ch} t & \text { in } T_{\alpha}^{\varepsilon} \\ 1 & \text { in } M \backslash T_{0}^{\varepsilon}\end{cases}$$

Having this result it becomes quite natural to consider functions $f \in \mathcal{C}^{0}(M)$ such that $\|f\|_{\mathcal{C}_{\gamma+2}^{0}(M)}=\sup _{M}\left|\psi_{\varepsilon}^{\gamma+2} f\right|<+\infty$ and looking for solutions $u \in \mathcal{C}^{0}(M)$ such that $\|u\|_{\mathcal{C}_{\gamma}^{0}(M)}=\sup _{M}\left|\psi_{\varepsilon}^{\gamma} u\right|<+\infty$.

As a first step towards the solution of the problem 6 we will proof the following
Lemma 3.2. Given a function $f \in \mathcal{C}^{0}(M)$ such that $\int_{M} f \mathrm{~d} \operatorname{vol}_{g_{\varepsilon}}=0$ and $\|f\|_{\mathcal{C}_{\gamma+2}^{0}(M)}<$ $+\infty$ it is possible to find a real number $\lambda$, an approximate solution $u \in \mathcal{C}^{0}(M)$ such that $\int_{M} u \mathrm{~d} \operatorname{vol}_{g_{\varepsilon}}=0$ and $\|u\|_{\mathcal{C}_{\gamma}^{0}(M)}<+\infty$ and an error term $R \in \mathcal{C}^{0}(M)$ such that $\int_{M} R \mathrm{~d} \operatorname{vol}_{g_{\varepsilon}}=0$ and $\|R\|_{\mathcal{C}_{\gamma+2}^{0}(M)}<+\infty$ that verify
$$\Delta_{g_{\varepsilon}} u=f-\lambda \beta_{\varepsilon}+R$$

Moreover there exist positive constants $A, B, C>0$ such that the following estimates yield for every $\gamma \in(0, n-2)$
$$\begin{aligned}
\|R\|_{\mathcal{C}_{\gamma+2}^{0}(M)} & \leq A \mathrm{e}^{(n-2) \alpha} \varepsilon^{n-2}\|f\|_{\mathcal{C}_{\gamma+2}^{0}(M)} \\
\|u\|_{\mathcal{C}_{\gamma}^{0}(M)} & \leq B\|f\|_{\mathcal{C}_{\gamma+2}^{0}(M)}^{0} \\
|\lambda| & \leq C\|f\|_{\mathcal{C}_{\gamma+2}^{0}(M)}^{0}
\end{aligned}$$

The proof of the lemma consists in building an approximate solution $u$ and in estimating the error term. In order to do that let us consider a non negative smooth function $\chi_{P}$ such that the triple $\left\{\chi_{1}, \chi_{P}, \chi_{2}\right\}$ is a partition of the unity. We can write
$$f=f \chi_{1}+f \chi_{P}+f \chi_{2}=f_{1}+f_{P}+f_{2}$$
As a first step we want to build a good approximate solution on the polyneck. It is well known that the problem
$$\begin{cases}\Delta_{g_{\varepsilon}} v=f_{P} & \text { on } T_{\alpha}^{\varepsilon} \\ v=0 & \text { on } \partial T_{\alpha}^{\varepsilon}\end{cases}$$
admits a solution and we call it $\tilde{u}_{P}$. Moreover, if $f_{P}$ is continuous, so does $\tilde{u}_{P}$ and thanks to the Lemma 3.1, if we choose $\alpha$ large enough, we have that the following estimate yields
$$\left\|\tilde{u}_{P}\right\|_{\mathcal{C}_{\gamma}^{0}\left(T_{\alpha}^{\varepsilon}\right)} \leq C_{P}\left\|f_{P}\right\|_{\mathcal{C}_{\gamma+2}^{0}\left(T_{\alpha}^{\varepsilon}\right)}$$
for some positive constant $C_{P}>0$. Notice that the boundary condition allows us to drop out the term $\left\|\tilde{u}_{P}\right\|_{\mathcal{C}_{\gamma}^{0}\left(\partial T_{\alpha}^{\varepsilon}\right)}$ in the above estimate.

Let us define $u_{P}:=\chi_{P} \tilde{u}_{P}$, as a consequence we have that
$$\begin{aligned}
\Delta_{g_{\varepsilon}} u_{p} & =\Delta_{g_{\varepsilon}} \tilde{u}_{P}-\Delta_{g_{\varepsilon}}\left(1-\chi_{P}\right) \tilde{u}_{P} \\
& =f_{P}-\Delta_{g_{\varepsilon}}\left(\chi_{1} \tilde{u}_{P}\right)-\Delta_{g_{\varepsilon}}\left(\chi_{2} \tilde{u}_{P}\right) \\
& =f_{P}-q_{1}-q_{2}
\end{aligned}$$
where $q_{i}=\Delta_{g_{\varepsilon}}\left(\chi_{i} \tilde{u}_{P}\right), i=1,2$.
Let us call $\tilde{f}_{i}:=f_{i}+q_{i}, i=1,2$ and $\tilde{f}:=\tilde{f}_{1}+\tilde{f}_{2}$. Since $\int_{M} f \mathrm{~d} \operatorname{vol}_{g_{\varepsilon}}=0$, it is easy to check that also $\int_{M} \tilde{f} \mathrm{~d}$ vol $_{g_{\varepsilon}}=0$. Hence $\int_{M} \tilde{f}_{1} \mathrm{~d} \operatorname{vol}_{g_{\varepsilon}}=-\int_{M} \tilde{f}_{2} \mathrm{~d} v o l_{g_{\varepsilon}}$.

Let us define $h_{i}:=\tilde{f}_{i}+(-1)^{i} \lambda c_{i} \chi_{i}$ for $i=1,2$ and $h:=h_{1}+h_{2}=\tilde{f}-\lambda \beta_{\varepsilon}$. Obviously we have that $\int_{M} h \mathrm{~d} v o l_{g_{\varepsilon}}=0$ and $\int_{M} h_{1} \mathrm{~d} v o l_{g_{\varepsilon}}=-\int_{M} h_{2} \mathrm{~d} v o l_{g_{\varepsilon}}$.

Moreover
$$\int_{M} h_{1} \mathrm{~d} v o l_{g_{\varepsilon}}-\int_{M} h_{2} \mathrm{~d} v o l_{g_{\varepsilon}}=\int_{M} \tilde{f}_{1}-\tilde{f}_{2} \mathrm{~d} v o l_{g_{\varepsilon}}-\lambda \int_{M} c_{1} \chi_{1}+c_{2} \chi_{2} \mathrm{~d} v o l_{g_{\varepsilon}}$$

Hence, by setting
$$\lambda:=\frac{\int_{M} \tilde{f}_{1}-\tilde{f}_{2} \mathrm{~d} \operatorname{vol}_{g_{\varepsilon}}}{\int_{M} c_{1} \chi_{1}+c_{2} \chi_{2} \mathrm{~d} v o l_{g_{\varepsilon}}}$$
it follows at once that $\int_{M} h_{i} \mathrm{~d} v o l_{g_{\varepsilon}}=0, i=1,2$.
As a second step we want now to construct approximate solutions on the pieces of $M$ coming from $M_{1}$ and $M_{2}$. For this purpose, let us consider, for $i=1,2$, the functions $\tilde{u}_{i}$ verifying
$$\Delta_{g_{i}} \tilde{u}_{i}=h_{i}-b_{i} \delta_{K}$$
where $b_{i}=C_{n, K} \int_{M} h_{i} \mathrm{dvol}_{g_{i}}$ and $C_{n, K}$ is a suitable constant.
It is rather simple to describe how this functions approximately look like, in fact we can write (notice that the following remarks still hold for $i=2$ )
$$\Delta_{g_{1}} \tilde{u}_{1}=h_{1}+\frac{1}{V_{1}} \int_{M} h_{1} \mathrm{~d} v o l_{g_{1}}-\frac{1}{V_{1}} \int_{M} h_{1} \mathrm{~d} v o l_{g_{1}}-b_{1} \delta_{K}$$
we can now consider the split $\tilde{u}_{1}=\bar{u}_{1}+\hat{u}_{1}$ where
$$\left\{\begin{array}{l}
\Delta_{g_{1}} \bar{u}_{1}=h_{1}-\frac{1}{V_{1}} \int_{M} h_{1} \mathrm{~d} v o l_{g_{1}} \\
\Delta_{g_{1}} \hat{u}_{1}=\frac{1}{V_{1}} \int_{M} h_{1} \mathrm{~d} v o l_{g_{1}}-b_{1} \delta_{K}
\end{array}\right.$$
we can think of $\bar{u}_{1}$ as the "finite part" and of $\hat{u}_{1}$ as the "pure Green function part" of $\tilde{u}_{1}$. In particular $\hat{u}_{1}$ has the following shape:
$$\begin{aligned}
\hat{u}_{1} & =\Omega_{n, K} \int_{M} h_{1} \mathrm{~d} v o l_{g_{1}}\left(|x|^{2-n}+\mathcal{O}\left(|x|^{1-n}\right)\right) \\
& =\Omega_{n, K} \int_{M} h_{1}\left(\mathrm{~d} v o l_{g_{1}}-\mathrm{d} v o l_{g_{\varepsilon}}\right)\left(|x|^{2-n}+\mathcal{O}\left(|x|^{1-n}\right)\right)
\end{aligned}$$
since $\int_{M} h_{1} \mathrm{~d} \operatorname{vol}_{g_{\varepsilon}}=0$. For the gradient $\nabla \hat{u}_{1}$ the expression is
$$\nabla \hat{u}_{1}=\Omega_{n, K} \int_{M} h_{1}\left(\mathrm{~d} \operatorname{vol}_{g_{1}}-\mathrm{d} \operatorname{vol}_{g_{\varepsilon}}\right)\left((n-2)|x|^{2-n}+\mathcal{O}\left(|x|^{1-n}\right)\right)$$
because $\nabla|x|^{2-n}=\nabla\left(\varepsilon^{2-n} \mathrm{e}^{(n-2) t}\right)=\varepsilon^{2-n}(n-2) \mathrm{e}^{(n-2) t}=(n-2)|x|^{2-n}$.

In order to glue together $\tilde{u}_{1}$ and $\tilde{u}_{2}$, we will use the following smooth and monotone cut-off functions
$$\phi_{1}= \begin{cases}1 & \text { on } M_{1} \backslash T_{0}^{\varepsilon} \\ 1 & \text { on }\{\log \varepsilon<t<\log \varepsilon+\alpha+1\} \\ 0 & \text { on }\{\log \varepsilon+\alpha+2<t<0\} \\ 0 & \text { otherwise }\end{cases}$$
$$\phi_{2}= \begin{cases}1 & \begin{array}{l}
\text { on } M_{2} \backslash T_{0}^{\varepsilon} \\
1 \\
0
\end{array} \\
\text { on }\{-\log \varepsilon-\alpha-1<t<-\log \varepsilon\} \\
0 & \text { on }\{0<t<-\log \varepsilon-\alpha-2\} \\
\text { otherwise }\end{cases}$$
Now we can define the approximate solution $u$ as
$$u=u_{P}+\phi_{1} \tilde{u}_{1}+\phi_{2} \tilde{u}_{2}$$
and we can calculate
$$\begin{aligned}
\Delta_{g_{\varepsilon}} u & =\Delta_{g_{\varepsilon}} u_{P}+\Delta_{g_{\varepsilon}}\left(\phi_{1} \tilde{u}_{1}\right)+\Delta_{g_{\varepsilon}}\left(\phi_{2} \tilde{u}_{2}\right) \\
& =f_{P}-q_{1}-q_{2} \\
& +\phi_{1}\left(h_{1}-b_{1} \delta_{K}\right)+\left(\Delta_{g_{\varepsilon}} \phi_{1}\right) \tilde{u}_{1}+g_{\varepsilon}\left(\nabla \phi_{1}, \nabla \tilde{u}_{1}\right) \\
& +\phi_{2}\left(h_{2}-b_{2} \delta_{K}\right)+\left(\Delta_{g_{\varepsilon}} \phi_{2}\right) \tilde{u}_{2}+g_{\varepsilon}\left(\nabla \phi_{2}, \nabla \tilde{u}_{2}\right) \\
& =f-\lambda \beta_{\varepsilon} \\
& +\left(\Delta_{g_{\varepsilon}} \phi_{1}\right) \tilde{u}_{1}+g_{\varepsilon}\left(\nabla \phi_{1}, \nabla \tilde{u}_{1}\right) \\
& +\left(\Delta_{g_{\varepsilon}} \phi_{2}\right) \tilde{u}_{2}+g_{\varepsilon}\left(\nabla \phi_{2}, \nabla \tilde{u}_{2}\right)
\end{aligned}$$
At this point it is quite natural to define $E_{i}:=\left(\Delta_{g_{\varepsilon}} \phi_{i}\right) \tilde{u}_{i}+g_{\varepsilon}\left(\nabla \phi_{i}, \nabla \tilde{u}_{i}\right), i=1,2$ and $R:=E_{1}+E_{2}$, so that
$$\Delta_{g_{\varepsilon}} u=f-\lambda \beta_{\varepsilon}+R$$
We can now proceed with the estimate of $R$. Without loss of generality, let us look for example at the error term $E_{1}$. Since $\operatorname{supp}\left(\Delta_{g_{\varepsilon}} \phi_{1}\right)$ and $\operatorname{supp}\left(\nabla \phi_{1}\right)$ are both included in $[\log \varepsilon+\alpha+1, \log \varepsilon+\alpha+2]$, the term $E_{1}$ is supported here as well.

It follows from a straightforward computation that
$$\left|\int_{M} h_{1}\left(\mathrm{~d} v o l_{g_{\varepsilon}}-\mathrm{d} v o l_{g_{1}}\right)\right| \leq C^{(0)} \mathrm{e}^{\alpha \gamma} \varepsilon^{n-2}\|f\|_{\mathcal{C}_{\gamma+2}^{0}(M)}$$
for some constant $C^{(0)}>0$.

According to the splitting of $\tilde{u}_{1}$ we have that
$$\tilde{u}_{1}=\bar{u}_{1}+\hat{u}_{1} \quad \nabla \tilde{u}_{1}=\nabla \bar{u}_{1}+\nabla \hat{u}_{1}$$
and by remembering the expressions found for $\hat{u}_{1}$ and $\nabla \hat{u}_{1}$ it is easy to see that both these terms are $\mathcal{O}\left(\mathrm{e}^{(n-2+\gamma) \alpha}\right)$ on the support of $E_{1}$, hence, for sufficiently large $\alpha>0$ it is clear that $\left|\tilde{u}_{1}\right|<A^{(0)}\left|\hat{u}_{1}\right|$ and $\left|\nabla \tilde{u}_{1}\right|<A^{(1)}\left|\nabla \hat{u}_{1}\right|$, for suitable constants $A^{(0)}, A^{(1)}>0$.

Now we are ready to estimate on the interval $[\log \varepsilon+\alpha+1, \log \varepsilon+\alpha+2]$ the term
$$\begin{aligned}
\left|\psi_{\varepsilon}^{\gamma+2}\left(\Delta_{g_{\varepsilon}} \phi_{1}\right) \tilde{u}_{1}\right| & \leq A^{(0)}\left|\psi_{\varepsilon}^{\gamma+2}\left(\Delta_{g_{\varepsilon}} \phi_{1}\right) \hat{u}_{1}\right| \\
& \leq A^{(2)}|x|^{\gamma+2}|x|^{-2}\left|\Omega_{n, K}\right|\left|\int_{M} h_{1}\left(\mathrm{~d} v o l_{g_{\varepsilon}}-\mathrm{d} v o l_{g_{1}}\right)\right||x|^{2-n} \\
& \leq A^{(3)}|x|^{-(n-2-\gamma)} \mathrm{e}^{\alpha \gamma} \varepsilon^{n-2}\|f\|_{\mathcal{C}_{\gamma+2}^{0}(M)} \\
& \leq A^{(4)} \mathrm{e}^{(n-2) \alpha} \varepsilon^{n-2}\|f\|_{\mathcal{C}_{\gamma+2}^{0}(M)}
\end{aligned}$$

Analogously
$$\left|\psi_{\varepsilon}^{\gamma+2} g_{\varepsilon}\left(\nabla \phi_{1}, \nabla \tilde{u}_{1}\right)\right| \leq A^{(5)} \mathrm{e}^{(n-2) \alpha} \varepsilon^{n-2}\|f\|_{\mathcal{C}_{\gamma+2}^{0}(M)}$$

Hence
$$\left\|E_{1}\right\|_{\mathcal{C}_{\gamma+2}^{0}(M)} \leq A^{(6)} \mathrm{e}^{(n-2) \alpha} \varepsilon^{n-2}\|f\|_{\mathcal{C}_{\gamma+2}^{0}(M)}^{0}$$
Since the same estimate holds for $E_{2}$, we conclude that, for a suitable constant $A>0$
$$\|R\|_{\mathcal{C}_{\gamma+2}^{0}(M)}^{0} \leq A \mathrm{e}^{(n-2) \alpha} \varepsilon^{n-2}\|f\|_{\mathcal{C}_{\gamma+2}^{0}(M)}$$

In order to obtain the estimate 9, let us recall that $u=u_{P}+\phi_{1} \tilde{u}_{1}+\phi_{2} \tilde{u}_{2}$ and that, for $\alpha>0$ large enough, $\left\|u_{p}\right\|_{\mathcal{C}_{\gamma}^{0}\left(T_{\alpha}^{\varepsilon}\right)}=\left\|\chi_{P} \tilde{u}_{P}\right\|_{\mathcal{C}_{\gamma}^{0}\left(T_{\alpha}^{\varepsilon}\right)} \leq B^{(0)}\left\|f_{p}\right\|_{\mathcal{C}_{\gamma+2}^{0}\left(T_{\alpha}^{\varepsilon}\right)}$.

On the other hand, on the support of $\phi_{1}$ we have that
$$\begin{aligned}
\left|\psi_{\varepsilon}^{\gamma} \phi_{1} \tilde{u}_{1}\right| & \leq B^{(1)}|x|^{\gamma}\left|\Omega_{n, K}\right|\left|\int_{M} h_{1} \mathrm{~d} v o l_{g_{\varepsilon}}\right||x|^{2-n} \\
& \leq B^{(2)} \mathrm{e}^{\alpha \gamma} \varepsilon^{n-2}\|f\|_{\mathcal{C}_{\gamma+2}^{0}(M)}|x|^{2-n+\gamma} \\
& \leq B^{(3)} \mathrm{e}^{(n-2) \alpha} \varepsilon^{\gamma}\|f\|_{\mathcal{C}_{\gamma+2}^{0}(M)}
\end{aligned}$$

Hence, it is clear that there exists a constant $B>0$ such that:
$$\|u\|_{\mathcal{C}_{\gamma}^{0}(M)} \leq B\|f\|_{\mathcal{C}_{\gamma+2}^{0}(M)}$$

Finally, by remembering the expression for $\lambda$ it follows from a straightforward computation that, for large enough $C>0$,
$$|\lambda| \leq C\|f\|_{\mathcal{C}_{\gamma+2}^{0}(M)}$$
and the lemma 3.2 is proved.

The idea is to solve the equation 6 by means of a sequence method. We start by setting $f^{(0)}:=f$ and thanks to the lemma 3.2 we obtain a triple $\left(\lambda^{(0)}, u^{(0)}, R^{(0)}\right)$ verifying the equation
$$\Delta_{g_{\varepsilon}} u^{(0)}=f^{(0)}-\lambda^{(0)} \beta_{\varepsilon}+R^{(0)}$$
and the estimates 8, 9, 10. Now we set $f^{(1)}:=-R^{(0)}$ and we find another triple $\left(\lambda^{(1)}, u^{(1)}, R^{(1)}\right)$ with the same properties of the first one and so on. In general, for
every $j \in \mathbb{N}$, we have $f^{(j)}:=-R^{(j-1)}$ and a triple $\left(\lambda^{(j)}, u^{(j)}, R^{(j)}\right)$ verifying the equation
$$\Delta_{g_{\varepsilon}} u^{(j)}=f^{(j)}-\lambda^{(j)} \beta_{\varepsilon}+R^{(j)}$$
and the estimates 8, 9, 10,

By taking the sum of the equations 11 we have that, for every $N \in \mathbb{N}$
$$\begin{aligned}
\Delta_{g_{\varepsilon}}\left(\sum_{j=0}^{N} u^{(j)}\right) & =\sum_{j=0}^{N} f^{(j)}-\left(\sum_{j=0}^{N} \lambda^{(j)}\right) \beta_{\varepsilon}+\sum_{j=0}^{N} R^{(j)} \\
& =f-\left(\sum_{j=0}^{N} \lambda^{(j)}\right) \beta_{\varepsilon}+R^{(N)}
\end{aligned}$$

In other words
$$\Delta_{g_{\varepsilon}} v^{(N)}=f-\mu^{(N)} \beta_{\varepsilon}+R^{(N)}$$
where $v^{(N)}:=\sum_{j=0}^{N} u^{(j)}$ and $\mu^{(N)}:=\sum_{j=0}^{N} \lambda^{(j)}$.
Notice that from the estimate of the lemma 3.2 it follows easily that
$$\begin{aligned}
\left\|f^{(j)}\right\|_{\mathcal{C}_{\gamma+2}^{0}(M)}=\left\|R^{(j-1)}\right\|_{\mathcal{C}_{\gamma+2}^{0}(M)}^{0} & \leq A \mathrm{e}^{(n-2) \alpha} \varepsilon^{n-2}\left\|f^{(j-1)}\right\|_{\mathcal{C}_{\gamma+2}^{0}(M)} \\
& \leq\left(A \mathrm{e}^{(n-2) \alpha} \varepsilon^{n-2}\right)^{j}\|f\|_{\mathcal{C}_{\gamma+2}^{0}(M)} \\
\left\|u^{(j)}\right\|_{\mathcal{C}_{\gamma}^{0}(M)} & \leq B\left\|f^{(j)}\right\|_{\mathcal{C}_{\gamma+2}^{0}(M)} \\
& \leq B\left(A \mathrm{e}^{(n-2) \alpha} \varepsilon^{n-2}\right)^{j}\|f\|_{\mathcal{C}_{\gamma+2}^{0}(M)} \\
\left|\lambda^{(j)}\right| & \leq C\left\|f^{(j)}\right\|_{\mathcal{C}_{\gamma+2}^{0}(M)} \\
& \leq C\left(A \mathrm{e}^{(n-2) \alpha} \varepsilon^{n-2}\right)^{j}\|f\|_{\mathcal{C}_{\gamma+2}^{0}(M)}
\end{aligned}$$

Now it is clear that, for sufficiently small $\varepsilon>0$, there exist $\lambda \in \mathbb{R}$ and a continuous function $u$ such that
$$\begin{aligned}
& R^{(N)} \xrightarrow{\|\cdot\|_{\mathcal{C}_{\gamma+2}^{0}}} 0 \\
& v^{(N)} \xrightarrow{\|\cdot\|_{\mathcal{C}_{\gamma}^{0}}} u \\
& \mu^{(N)} \xrightarrow{ } \lambda
\end{aligned}$$
Moreover there exist positive constants $B^{\prime}, C^{\prime}>0$ such that
$$\|u\|_{\mathcal{C}_{\gamma}^{0}(M)} \leq B^{\prime}\|f\|_{\mathcal{C}_{\gamma+2}^{0}(M)} \quad|\lambda| \leq C^{\prime}\|f\|_{\mathcal{C}_{\gamma+2}^{0}(M)}$$

Hence
$$\left\{\begin{array}{l}
\Delta_{g_{\varepsilon}} v^{(N)} \xrightarrow{\|\cdot\|_{\mathcal{C}_{\gamma}^{0}+2}^{0}} f-\lambda \beta_{\varepsilon} \\
v^{(N)} \xrightarrow{\|\cdot\|_{C_{\gamma}^{0}}} u
\end{array}\right.$$
On the other hand we have that, for every $N \in \mathbb{N}$ and for every $\phi \in \mathcal{C}^{\infty}(M)$
$$\int_{M} v^{(N)} \Delta_{g_{\varepsilon}} \phi \mathrm{d} v o l_{g_{\varepsilon}}=\int_{M}\left(f-\mu^{(N)} \beta_{\varepsilon}+R^{(N)}\right) \phi \mathrm{d} v o l_{g_{\varepsilon}}$$
Hence, by taking the limit for $N \rightarrow+\infty$ we find the expression
$$\int_{M} u \Delta_{g_{\varepsilon}} \phi \mathrm{d} v o l_{g_{\varepsilon}}=\int_{M}\left(f-\lambda \beta_{\varepsilon}\right) \phi \mathrm{d} v o l_{g_{\varepsilon}}$$
for every $\phi \in \mathcal{C}^{\infty}(M)$. It is to say that $\Delta_{g_{\varepsilon}} u=f-\lambda \beta_{\varepsilon}$ in the sense of the distributions.

Thanks to the elliptic regularity (see for example [2], [4]) if we suppose that $f \in \mathcal{C}^{\infty}(M)$, then so does $u$ and the expression above is a pointwise identity.

To conclude this section we summarize our results in the following
Proposition 3.3. Given a function $f \in \mathcal{C}^{0}(M)$ such that $\int_{M} f \mathrm{~d}$ vol $_{g_{\varepsilon}}=0$ and $\|f\|_{\mathcal{C}_{\gamma+2}^{0}(M)}<+\infty$, it is possible to find a real number $\lambda$ and a function $u \in \mathcal{C}^{0}(M)$ with $\int_{M} u \mathrm{~d} \operatorname{vol}_{g_{\varepsilon}}=0$ and $\|u\|_{\mathcal{C}_{\gamma}^{0}(M)}<+\infty$ verifying
$$\Delta_{g_{\varepsilon}} u=f-\lambda \beta_{\varepsilon}$$
in the sense of the distributions and the following estimates
$$\begin{aligned}
\|u\|_{\mathcal{C}_{\gamma}^{0}(M)} & \leq B^{\prime}\|f\|_{\mathcal{C}_{\gamma+2}^{0}(M)} \\
|\lambda| & \leq C^{\prime}\|f\|_{\mathcal{C}_{\gamma+2}^{0}(M)}^{0}
\end{aligned}$$
for suitable constants $B^{\prime}, C^{\prime}>0$.

Moreover, if $f \in \mathcal{C}^{\infty}(M)$, then $u \in \mathcal{C}^{\infty}(M)$ and the identity above holds pointwise.

\section*{4 Fixed point argument}

The aim of this section is to solve the problem 5
$$\Delta_{g_{\varepsilon}} v=F_{\varepsilon}(v)-\lambda(\varepsilon, v) \beta_{\varepsilon}$$
We will be able to do that by means of the results of the previous section and of a contracting mapping argument.

Before starting, let us remark that in the expression for $F_{\varepsilon}(v)$ (see equation 4) it is always possible to choose $S=S(\varepsilon, v)$ in such a way that $\int_{M} F_{\varepsilon} \mathrm{d} v o l_{g_{\varepsilon}}=0$. Moreover,
by using the scalar curvature estimate $S_{g_{\varepsilon}}=\mathcal{O}\left(\varepsilon^{n-2}|x|^{1-n}\right)$ found in [11] it will be easy to see that $S=\mathcal{O}\left(\varepsilon^{n-2}\right)$.

Now, for every $\sigma>0$ let us define the space
$$\mathcal{C}_{\sigma}^{0}(M):=\left\{h \in \mathcal{C}^{0}(M): \int_{M} h \mathrm{~d} v o l_{g_{\varepsilon}}=0 \quad \text { and } \quad\|h\|_{\mathcal{L}_{\sigma}^{0}(M)}<+\infty\right\}$$
where $\|h\|_{\mathcal{C}_{\sigma}^{0}(M)}:=\sup _{M}\left|\psi_{\varepsilon}^{\sigma} h\right|$.
Let us define also the maps
$$\begin{aligned}
H_{\varepsilon}: \mathcal{C}_{\gamma}^{0}(M) & \longrightarrow \mathcal{C}_{\gamma+2}^{0}(M) \\
v & \longmapsto F_{\varepsilon}(v)-\lambda(\varepsilon, v) \beta_{\varepsilon}
\end{aligned}$$
$$\begin{aligned}
\Delta_{g_{\varepsilon}}^{-1}: \mathcal{C}_{\gamma+2}^{0}(M) & \longrightarrow \mathcal{C}_{\gamma}^{0}(M) \\
w & \longmapsto \Delta_{g_{\varepsilon}}^{-1} w
\end{aligned}$$
$$\begin{aligned}
P_{\varepsilon}: \mathcal{C}_{\gamma}^{0}(M) & \longrightarrow \mathcal{C}_{\gamma}^{0}(M) \\
v & \longmapsto \Delta_{g_{\varepsilon}}^{-1} \circ H_{\varepsilon}(v)
\end{aligned}$$

Let us start with the following lemma
Lemma 4.1. For $\gamma \in(0,1)$ and for sufficiently small $\varepsilon>0$ there exists a radius $r_{\varepsilon}>0$ such that $P_{\varepsilon}\left(B_{r_{\varepsilon}}^{\gamma}\right) \subset B_{r_{\varepsilon}}^{\gamma}$, where $B_{r_{\varepsilon}}^{\gamma}:=\left\{u \in \mathcal{C}_{\gamma}^{0}(M):\|u\|_{\mathcal{C}_{\gamma}^{0}(M)} \leq r_{\varepsilon}\right\}$. In other words:
$$\|v\|_{\mathcal{C}_{\gamma}^{0}(M)} \leq r_{\varepsilon} \quad \Longrightarrow \quad\left\|P_{\varepsilon}(v)\right\|_{\mathcal{C}_{\gamma}^{0}(M)} \leq r_{\varepsilon}$$

In order to prove the statement we observe that from the estimate 12 of the proposition 3.3 we obtain immediately the inequality
$$\left\|P_{\varepsilon}(v)\right\|_{\mathcal{C}_{\gamma}^{0}(M)} \leq D\left\|F_{\varepsilon}(v)\right\|_{\mathcal{C}_{\gamma+2}^{0}(M)}$$
for large enough $D>0$.

Now we have to estimate the term
$$\begin{aligned}
\left|F_{\varepsilon}(v) \psi_{\varepsilon}^{\gamma+2}\right| & \leq c_{m}|S| \psi_{\varepsilon}^{\gamma+2}+c_{m}\left|S_{g_{\varepsilon}}\right| \psi_{\varepsilon}^{\gamma} \\
& +c_{m}|S| \psi_{\varepsilon}^{\gamma+2}|v|+c_{m}\left|S_{g_{\varepsilon}}\right| \psi_{\varepsilon}^{\gamma}|v|+\frac{|S|}{m-1} \psi_{\varepsilon}^{\gamma}|v| \\
& +c_{m}|S||f(v)| \psi_{\varepsilon}^{\gamma} \\
& \leq D_{(1)} \varepsilon^{n-2}+D_{(2)}\left[\varepsilon^{n-2}+\varepsilon^{1+\gamma}\right] \\
& +D_{(3)} \varepsilon^{n-2} r_{\varepsilon}+D_{(4)}\left[\varepsilon^{n-2}+\varepsilon\right] r_{\varepsilon}+D_{(5)} \varepsilon^{n-2} r_{\varepsilon} \\
& +D_{(6)} \varepsilon^{n-2} r_{\varepsilon}^{2} \\
& \leq D_{(7)} \varepsilon^{n-2}+D_{(8)} \varepsilon^{1+\gamma} \\
& +D_{(9)} \varepsilon^{n-2} r_{\varepsilon}+D_{(10)} \varepsilon r_{\varepsilon} \\
& +D_{(11)} \varepsilon^{n-2} r_{\varepsilon}^{2}
\end{aligned}$$
for suitable constants $D_{(j)}$.
If $n=3$, then $\varepsilon^{n-2}=\varepsilon \gg \varepsilon^{1+\gamma}$, when $\varepsilon>0$ is small. Hence $D_{(7)} \varepsilon^{n-2}+$ $D_{(8)} \varepsilon^{1+\gamma} \leq D_{(12)} \varepsilon$, so if we define $r_{\varepsilon}:=2 D D_{(12)} \varepsilon$ we obtain $D_{(9)} \varepsilon^{n-2}+D_{(10)} \varepsilon+$ $D_{(11)} \varepsilon^{n-2} r_{\varepsilon} \leq D_{(13)} \varepsilon+D_{(11)} \varepsilon 2 D D_{(12)} \varepsilon \leq 1 / 2 D$, for small enough $\varepsilon>0$ and that guarantees $D\left\|F_{\varepsilon}(v)\right\|_{\mathcal{C}_{\gamma+2}^{0}(M)} \leq r_{\varepsilon}$.

If $n \geq 4$, then $\varepsilon^{n-2} \ll \varepsilon^{1+\gamma}$ (since $\gamma \in(0,1)$ ), when $\varepsilon>0$ is small. Hence $D_{(7)} \varepsilon^{n-2}+D_{(8)} \varepsilon^{1+\gamma} \leq D_{(12)} \varepsilon^{1+\gamma}$, so if we define $r_{\varepsilon}:=2 D D_{(14)} \varepsilon^{1+\gamma}$ we obtain $D_{(9)} \varepsilon^{n-2}+D_{(10)} \varepsilon+D_{(11)} \varepsilon^{n-2} r_{\varepsilon} \leq D_{(15)} \varepsilon+D_{(11)} \varepsilon 2 D D_{(14)} \varepsilon^{1+\gamma} \leq 1 / 2 D$, for small enough $\varepsilon>0$ and that still guarantees $D\left\|F_{\varepsilon}(v)\right\|_{\mathcal{C}_{\gamma+2}^{0}(M)} \leq r_{\varepsilon}$.

In both the cases the lemma is proved.

At this point our purpose is to prove the convergence of the sequence $v^{j}:=P_{\varepsilon}^{j}(0)$ with respect to the norm $\|\cdot\|_{\mathcal{C}_{\gamma}^{0}(M)}$. Towards this aim we need to provide an estimate of $\left\|P_{\varepsilon}(u)-P_{\varepsilon}(v)\right\|_{\mathcal{C}_{\gamma}^{0}(M)}$ in terms of $\|u-v\|_{\mathcal{C}_{\gamma}^{0}(M)}$, where $u, v \in B_{r_{\varepsilon}}^{\gamma}$; in fact, since $0 \in B_{r_{\varepsilon}}^{\gamma}$, all the terms of the sequence lie in $B_{r_{\varepsilon}}^{\gamma}$, because of the lemma 4.1.

Since $\Delta_{g_{\varepsilon}}\left(P_{\varepsilon}(u)-P_{\varepsilon}(v)\right)=H_{\varepsilon}(u)-H_{\varepsilon}(v)$ we have immediately that
$$\begin{aligned}
\left\|P_{\varepsilon}(u)-P_{\varepsilon}(v)\right\|_{\mathcal{C}_{\gamma}^{0}(M)} & \leq C^{\prime}\left\|H_{\varepsilon}(u)-H_{\varepsilon}(v)\right\|_{\mathcal{C}_{\gamma+2}^{0}(M)} \\
& =C^{\prime}\left\|F_{\varepsilon}(u)-F_{\varepsilon}(v)-(\lambda(\varepsilon, u)-\lambda(\varepsilon, v)) \beta_{\varepsilon}\right\|_{\mathcal{C}_{\gamma+2}^{0}(M)}
\end{aligned}$$

On the other hand it is easy to check that the mapping $f \longmapsto \lambda_{f}$, where $f$ and $\lambda=\lambda_{f}$ are those of the proposition 3.3, is a linear mapping, therefore
$$\lambda(\varepsilon, u)-\lambda(\varepsilon, v)=: \lambda_{F_{\varepsilon}(u)}-\lambda_{F_{\varepsilon}(v)}=\lambda_{F_{\varepsilon}(u)-F_{\varepsilon}(v)}$$
Hence, thanks to the estimate 10, we obtain
$$\left\|P_{\varepsilon}(u)-P_{\varepsilon}(v)\right\|_{\mathcal{C}_{\gamma}^{0}(M)} \leq C^{\prime \prime}\left\|F_{\varepsilon}(u)-F_{\varepsilon}(v)\right\|_{\mathcal{C}_{\gamma+2}^{0}(M)}$$

Since the function $f$ that appears in the definition of $F_{\varepsilon}(v)$ verifies the following inequality
$$|f(u)-f(v)| \leq\left[A(|u|+|v|)+B\left(|u|^{\frac{4}{m-2}}-|v|^{\frac{4}{m-2}}\right)\right]|u-v|$$
for suitable constants $A, B>0$, we can proceed to the estimate of the term $F_{\varepsilon}(u)-$ $F_{\varepsilon}(v): \gamma \in(0,1 / 2)$ is a sufficient condition to ensure that
$$\begin{aligned}
\psi_{\varepsilon}^{\gamma+2}\left|F_{\varepsilon}(u)-F_{\varepsilon}(v)\right| & \leq \psi_{\varepsilon}^{\gamma+2}\left[c_{m}|S||u-v|+c_{m}\left|S_{g_{\varepsilon}}\right||u-v|+\frac{|S|}{m-1}|u-v|\right] \\
& +\psi_{\varepsilon}^{\gamma+2} c_{m}|S|\left[A(|u|+|v|)+B\left(|u|^{\frac{4}{m-2}}-|v|^{\frac{4}{m-2}}\right)\right]|u-v| \\
& \leq C^{\prime \prime \prime} \varepsilon\|u-v\|_{\mathcal{C}_{\gamma}^{0}(M)} \\
& +C^{\prime \prime \prime \prime} \varepsilon^{n-2}\left(\|u\|_{\mathcal{C}_{\gamma}^{0}(M)}+\|v\|_{\mathcal{C}_{\gamma}^{0}(M)}\right)\|u-v\|_{\mathcal{C}_{\gamma}^{0}(M)} \\
& +C^{\prime \prime \prime \prime \prime} \varepsilon^{n-2}\left(\|u\|_{\mathcal{C}_{\gamma}^{0}(M)}^{\frac{4}{m-2}}+\|v\|_{\mathcal{C}_{\gamma}^{0}(M)}^{\frac{4}{m-2}}\right)\|u-v\|_{\mathcal{C}_{\gamma}^{0}(M)}
\end{aligned}$$

Hence, for $u, v \in B_{r_{\varepsilon}}^{\gamma}$ and small enough $\varepsilon>0$ we get the inequality
$$\left\|P_{\varepsilon}(u)-P_{\varepsilon}(v)\right\|_{\mathcal{C}_{\gamma}^{0}(M)} \leq C \varepsilon\|u-v\|_{\mathcal{C}_{\gamma}^{0}(M)}$$
Now, for integers $p \leq q$ we have that
$$\begin{aligned}
\left\|v^{q}-v^{p}\right\|_{\mathcal{C}_{\gamma}^{0}(M)} & \leq \sum_{1}^{p-q}\left\|v^{p+j}-v^{p+j-1}\right\|_{\mathcal{C}_{\gamma}^{0}(M)} \\
& \leq(C \varepsilon)^{p} \sum_{0}^{+\infty}(C \varepsilon)^{j}\left\|v^{1}-v^{0}\right\|_{\mathcal{C}_{\gamma}^{0}(M)}
\end{aligned}$$

Hence the sequence $\left(v^{j}\right)$ is a Cauchy sequence and it must converge to a continuous function $v_{\varepsilon} \in B_{r_{\varepsilon}}^{\gamma}$ which is the fixed point we were looking for i. e.
$$P_{\varepsilon}\left(v_{\varepsilon}\right)=v_{\varepsilon}$$
In other words
$$\Delta_{g_{\varepsilon}} v_{\varepsilon}=F_{\varepsilon}\left(v_{\varepsilon}\right)-\lambda_{F_{\varepsilon}\left(v_{\varepsilon}\right)} \beta_{\varepsilon}$$

By means of a classical boot strap argument it is easy to see that $v_{\varepsilon}$ is actually a smooth function.

\section*{5 The approximate eigenvalue $\lambda_{F_{\varepsilon}\left(v_{\varepsilon}\right)}$}

In this section we want to study the sign of the approximate eigenvalue $\lambda_{F_{\varepsilon}\left(v_{\varepsilon}\right)}$. In particular our purpose is to show that by moving the initial metrics (more precisely by scaling up or down $g_{1}$ and $g_{2}$ ) the approximate eigenvalue becomes positive or negative, hence there exist suitable constants $R, Q>0$ such that the construction starting by $R g_{1}$ and $Q g_{2}$ as initial metrics has zero approximate eigenvalue. Therefore, in this case, $v_{\varepsilon}$ is a solution of the problem 4.

Since an explicit expression of $\lambda_{F_{\varepsilon}\left(v_{\varepsilon}\right)}$ in terms of the initial metrics is not available, we have to handle with its approximations, taking care in estimating the errors. Thanks to the proposition 3.3 we can think of $\lambda_{F_{\varepsilon}\left(v_{\varepsilon}\right)}$ as obtained by a sequence method, exactly like the real number $\lambda$ of the mentioned proposition. Therefore it is possible to find a sequence $\lambda_{F_{\varepsilon}\left(v_{\varepsilon}\right)}^{(j)}$ such that
$$\lambda_{F_{\varepsilon}\left(v_{\varepsilon}\right)}=\sum_{j=0}^{\infty} \lambda_{F_{\varepsilon}\left(v_{\varepsilon}\right)}^{(j)}$$
and such that the following estimate holds:
$$\left|\lambda_{F_{\varepsilon}\left(v_{\varepsilon}\right)}^{(j)}\right| \leq C\left(A \mathrm{e}^{(n-2) \alpha} \varepsilon^{n-2}\right)^{j}\left\|F_{\varepsilon}\left(v_{\varepsilon}\right)\right\|_{\mathcal{C}_{\gamma+2}^{0}(M)}$$
for suitable constants $A, C>0$.

Now, for sufficiently small $\varepsilon>0$ it is quite easy to estimate the difference
$$\begin{aligned}
\left|\lambda_{F_{\varepsilon}\left(v_{\varepsilon}\right)}-\lambda_{F_{\varepsilon}\left(v_{\varepsilon}\right)}^{(0)}\right| & \leq \sum_{j=1}^{+\infty}\left|\lambda_{F_{\varepsilon}\left(v_{\varepsilon}\right)}^{(j)}\right| \\
& \leq C\left[\sum_{j=1}^{+\infty}\left(A \mathrm{e}^{(n-2) \alpha} \varepsilon^{n-2}\right)^{j}\right]\left\|F_{\varepsilon}\left(v_{\varepsilon}\right)\right\|_{\mathcal{C}_{\gamma+2}^{0}(M)} \\
& \leq \frac{A \mathrm{e}^{(n-2) \alpha} \varepsilon^{n-2}}{1-A \mathrm{e}^{(n-2) \alpha} \varepsilon^{n-2}} C\left\|F_{\varepsilon}\left(v_{\varepsilon}\right)\right\|_{\mathcal{C}_{\gamma+2}^{0}(M)} \\
& \leq B \mathrm{e}^{(n-2) \alpha} \varepsilon^{n-2}\left\|F_{\varepsilon}\left(v_{\varepsilon}\right)\right\|_{\mathcal{C}_{\gamma+2}^{0}(M)}
\end{aligned}$$
where $B>0$ is a suitable constant.

At the moment we have obtained that
$$\left|\lambda_{F_{\varepsilon}\left(v_{\varepsilon}\right)}\right| \leq\left|\lambda_{F_{\varepsilon}\left(v_{\varepsilon}\right)}^{(0)}\right|-B \mathrm{e}^{(n-2) \alpha} \varepsilon^{n-2}\left\|F_{\varepsilon}\left(v_{\varepsilon}\right)\right\|_{\mathcal{C}_{\gamma+2}^{0}(M)}$$

Following the proof of the proposition 3.3, we can write down the expression for $\left|\lambda_{F_{\varepsilon}\left(v_{\varepsilon}\right)}^{(0)}\right|$, it is to say:
$$\lambda_{F_{\varepsilon}\left(v_{\varepsilon}\right)}^{(0)}=\frac{\int_{M} \widetilde{F_{\varepsilon}\left(v_{\varepsilon}\right)_{1}}-\widetilde{F_{\varepsilon}\left(v_{\varepsilon}\right)_{2}} \mathrm{~d} v o l_{g_{\varepsilon}}}{\int_{M} c_{1} \chi_{1}+c_{2} \chi_{2} \mathrm{~d} \operatorname{vol}_{g_{\varepsilon}}}$$
where $\widetilde{F_{\varepsilon}\left(v_{\varepsilon}\right)_{i}}=\chi_{i} F_{\varepsilon}\left(v_{\varepsilon}\right)+\Delta_{g_{\varepsilon}}\left(\chi_{i} \tilde{u}_{P}^{\varepsilon}\right)$, for $i=1,2$ and where $\tilde{u}_{P}^{\varepsilon}$ is the solution of the problem
$$\begin{cases}\Delta_{g_{\varepsilon}} \tilde{u}_{P}^{\varepsilon}=\chi_{P} F_{\varepsilon}\left(v_{\varepsilon}\right) & \text { on } T_{\alpha}^{\varepsilon} \\ \tilde{u}_{P}^{\varepsilon}=0 & \text { on } \partial T_{\alpha}^{\varepsilon}\end{cases}$$

It is convenient to write
$$\begin{aligned}
\lambda_{F_{\varepsilon}\left(v_{\varepsilon}\right)}^{(0)} & =\frac{1}{\int_{M} c_{1} \chi_{1}+c_{2} \chi_{2} \mathrm{~d} v o l_{g_{\varepsilon}}} \int_{M} F_{\varepsilon}\left(v_{\varepsilon}\right) \chi_{1}-F_{\varepsilon}\left(v_{\varepsilon}\right) \chi_{2} \mathrm{~d} v o l_{g_{\varepsilon}} \\
& +\frac{1}{\int_{M} c_{1} \chi_{1}+c_{2} \chi_{2} \mathrm{~d} v o l_{g_{\varepsilon}}} \int_{M} \Delta_{g_{\varepsilon}}\left(\chi_{1} \tilde{u}_{P}^{\varepsilon}\right)-\Delta_{g_{\varepsilon}}\left(\chi_{2} \tilde{u}_{P}^{\varepsilon}\right) \mathrm{d} v o l_{g_{\varepsilon}}
\end{aligned}$$

Concerning the first summand, it is sufficient to remember the estimate of the scalar curvature contained in the proposition 2.1 to conclude that
$$\int_{M} F_{\varepsilon}\left(v_{\varepsilon}\right) \chi_{1}-F_{\varepsilon}\left(v_{\varepsilon}\right) \chi_{2} \mathrm{~d} v o l_{g_{\varepsilon}}=\mathcal{O}\left(\varepsilon^{n-2}\right)$$

Concerning the second summand, it is useful to consider, for $i=1,2$ the split $\Delta_{g_{\varepsilon}}\left(\chi_{i} \tilde{u}_{P}^{\varepsilon}\right)=\chi_{i}\left(\Delta_{g_{\varepsilon}} \tilde{u}_{P}^{\varepsilon}\right)+g_{\varepsilon}\left(\nabla \chi_{i}, \nabla \tilde{u}_{P}^{\varepsilon}\right)+\tilde{u}_{P}^{\varepsilon}\left(\Delta_{g_{\varepsilon}} \chi_{i}\right)$. Obviously, we have that:
$$\begin{aligned}
\int_{M} \chi_{i}\left(\Delta_{g_{\varepsilon}} \tilde{u}_{P}^{\varepsilon}\right) \mathrm{d} v o l_{g_{\varepsilon}} & =\int_{\{\log \varepsilon+\alpha \leq t \leq \log \varepsilon+\alpha+1\}} \chi_{1} \chi_{P} F_{\varepsilon}\left(v_{\varepsilon}\right) \mathrm{d} v o l_{g_{\varepsilon}} \\
& =\mathcal{O}\left(\mathrm{e}^{-\alpha} \varepsilon^{n-2}\right)
\end{aligned}$$
and, using the Green formula, we can get now
$$\begin{aligned}
\int_{M} \tilde{u}_{P}^{\varepsilon}\left(\Delta_{g_{\varepsilon}} \chi_{i}\right) \mathrm{d} v o l_{g_{\varepsilon}}+\int_{M} g_{\varepsilon}\left(\nabla \chi_{i}, \nabla \tilde{u}_{P}^{\varepsilon}\right) \mathrm{d} v o l_{g_{\varepsilon}} & =\int_{T_{\alpha}^{\varepsilon}} \tilde{u}_{P}^{\varepsilon}\left(\Delta_{g_{\varepsilon}} \chi_{i}\right) \mathrm{d} v o l_{g_{\varepsilon}} \\
& +\int_{T_{\alpha}^{\varepsilon}} \nabla \chi_{i}\left(\tilde{u}_{P}^{\varepsilon}\right) \mathrm{d} v o l_{g_{\varepsilon}} \\
& =\int_{\partial T_{\alpha}^{\varepsilon}} \tilde{u}_{P}^{\varepsilon} \partial_{t}\left(\chi_{i}\right) \mathrm{d} v o l_{\iota^{*} g_{\varepsilon}} \\
& =0
\end{aligned}$$
where $\iota: \partial T_{\alpha}^{\varepsilon} \rightarrow M$ is the natural embedding.
Hence the second summand in 17 is a $\mathcal{O}\left(\mathrm{e}^{-\alpha} \varepsilon^{n-2}\right)$.
Now, by performing the right choice of $\alpha=\alpha(\varepsilon)$ we will be able to show that the sign of the approximate eigenvalue is determined by the sign of $\lambda_{F_{\varepsilon}\left(v_{\varepsilon}\right)}^{(0)}$ and, in particular, by the term
$$\frac{1}{\int_{M} c_{1} \chi_{1}+c_{2} \chi_{2} \mathrm{~d} v o l_{g_{\varepsilon}}} \int_{M} F_{\varepsilon}\left(v_{\varepsilon}\right) \chi_{1}-F_{\varepsilon}\left(v_{\varepsilon}\right) \chi_{2} \mathrm{~d} v o l_{g_{\varepsilon}}$$
If we set, for example $\alpha=-\log \varepsilon / 2(n-2)$, we get immediately
$$\begin{aligned}
\mathrm{e}^{(n-2) \alpha} \varepsilon^{n-2}\left\|F_{\varepsilon}\left(v_{\varepsilon}\right)\right\|_{\mathcal{C}_{\gamma+2}^{0}(M)} & =\mathcal{O}\left(\varepsilon^{n-3 / 2}\right) \\
\frac{1}{\int_{M} c_{1} \chi_{1}+c_{2} \chi_{2} \mathrm{~d} v o l_{g_{\varepsilon}}} \int_{M} \Delta_{g_{\varepsilon}}\left(\chi_{1} \tilde{u}_{P}^{\varepsilon}\right)-\Delta_{g_{\varepsilon}}\left(\chi_{2} \tilde{u}_{P}^{\varepsilon}\right) \mathrm{d} v o l_{g_{\varepsilon}} & =\mathcal{O}\left(\varepsilon^{n-2+1 / 2(n-2)}\right)
\end{aligned}$$
Hence, for small $\varepsilon>0$ the leading term is the one we wished.

More precisely, if we look at the expression for $F_{\varepsilon}\left(v_{\varepsilon}\right)$, it is clear that, when $\varepsilon$ is close to zero, the sign of the approximate eigenvalue is determined by the term
$$\int_{M}\left(S-S_{g_{\varepsilon}}\right) \chi_{1} \mathrm{~d} v o l_{g_{\varepsilon}}-\int_{M}\left(S-S_{g_{\varepsilon}}\right) \chi_{2} \mathrm{~d} v o l_{g_{\varepsilon}}$$

At this moment we want to replace for instance the initial metric $g_{1}$ by its homothetic $R g_{1}$ and to show that for sufficiently large $R>0$ the sign of the expression above is determined.

If we indicate by $(\cdot)^{R}$ the geometric quantities obtained in this case, we find the expansions
$$\begin{aligned}
\chi_{1} \mathrm{~d} v o l_{g_{\varepsilon}}^{R} & =R^{\frac{m}{2}} \mathrm{~d} v o l_{g_{1}}+R^{\frac{k}{2}+\frac{n+2}{4}} \mathcal{O}\left(\varepsilon^{n} \mathrm{e}^{-2 t}\right) \mathrm{d} t \mathrm{~d} \theta^{1} \ldots \mathrm{~d} \theta^{n-1} \mathrm{~d} z^{1} \ldots \mathrm{~d} z^{k} \\
\chi_{2} \mathrm{~d} v o l_{g_{\varepsilon}}^{R} & =\mathrm{d} v o l_{g_{2}}+R^{\frac{n-2}{4}} \mathcal{O}\left(\varepsilon^{n} \mathrm{e}^{2 t}\right) \mathrm{d} t \mathrm{~d} \theta^{1} \ldots \mathrm{~d} \theta^{n-1} \mathrm{~d} z^{1} \ldots \mathrm{~d} z^{k} \\
\chi_{1} S_{g_{\varepsilon}}^{R} & =R^{-\frac{n-2}{4}} \mathcal{O}\left(\varepsilon^{-1} \mathrm{e}^{(n-1) t}\right) \\
\chi_{2} S_{g_{\varepsilon}}^{R} & =R^{\frac{n-2}{4}} \mathcal{O}\left(\varepsilon^{-1} \mathrm{e}^{-(n-1) t}\right)
\end{aligned}$$

Moreover, by imposing that $\int_{M} F_{\varepsilon}^{R}\left(v_{\varepsilon}^{R}\right) \mathrm{d} v o l_{g_{\varepsilon}}^{R}=0$ we have that
$$\begin{aligned}
S^{R} & =\frac{1}{\int_{M} 1+\left(1+\frac{1}{c_{n}(n-1)}\right) v_{\varepsilon}^{R}+f\left(v_{\varepsilon}^{R}\right) \mathrm{d} v o l_{g_{\varepsilon}}^{R}} \int_{M} S_{g_{\varepsilon}}^{R}\left(1+v_{\varepsilon}^{R}\right) \mathrm{d} v o l_{g_{\varepsilon}}^{R} \\
& =\frac{1}{\operatorname{vol}_{g_{\varepsilon}(M)}^{R}} \int_{M} S_{g_{\varepsilon}}^{R} \mathrm{~d} v o l_{g_{\varepsilon}}^{R}+\sigma\left(\varepsilon^{n-2}\right) \\
& =R^{-\frac{n-2}{4}} \mathcal{O}\left(\varepsilon^{n-2}\right)
\end{aligned}$$
Therefore, for suitable constants $C_{1}, C_{2}$
$$\int_{M}\left(S^{R}-S_{g_{\varepsilon}}^{R}\right) \chi_{1} \mathrm{~d} v o l_{g_{\varepsilon}}^{R}=C_{1} R^{\frac{m}{2}-\frac{n-2}{4}} \mathcal{O}\left(\varepsilon^{n-2}\right)$$
and
$$\int_{M}\left(S^{R}-S_{g_{\varepsilon}}^{R}\right) \chi_{2} \mathrm{~d} v o l_{g_{\varepsilon}}^{R}=C_{2} R^{\frac{n-2}{4}} \mathcal{O}\left(\varepsilon^{n-2}\right)$$
Notice that $C_{1}$ and $C_{2}$ have the same sign, it is to say the sign of both the terms $\int_{M}\left(S-S_{g_{\varepsilon}}\right) \chi_{1} \mathrm{~d} \operatorname{vol}_{g_{\varepsilon}}$ and $\int_{M}\left(S-S_{g_{\varepsilon}}\right) \chi_{2} \mathrm{~d} \operatorname{vol}_{g_{\varepsilon}}$. Hence, for large enough $R>0$ the sign of the approximate eigenvalue is determined.

Obviously, if we make the same computation for the metric $Q g_{2}$ instead of $g_{2}$, we have that, for large enough $Q>0$, the sign of the approximate eigenvalue is the opposite of the one we found by scaling the metric $g_{1}$.

Hence, if we look at the approximate eigenvalue as a continuous function $\lambda_{F_{\varepsilon}\left(v_{\varepsilon}\right)}=$ $\lambda_{F_{\varepsilon}\left(v_{\varepsilon}\right)}(P, Q)$ depending on the positive factors $P$ and $Q$, we have seen that there exist $\bar{P}$ and $\bar{Q}$ such that $\lambda_{F_{\varepsilon}\left(v_{\varepsilon}\right)}(\bar{P}, 1)$ and $\lambda_{F_{\varepsilon}\left(v_{\varepsilon}\right)}(1, \bar{Q})$ have opposite sign.

At this point we can deduce that there exist positive real numbers $P_{0}$ and $Q_{0}$ such that $\lambda_{F_{\varepsilon}\left(v_{\varepsilon}\right)}\left(P_{0}, Q_{0}\right)=0$ and this is what we wished.

\section*{6 The non Ricci-flat case}

As we claimed in section 1, when both the initial metrics are scalar flat but non Ricci flat it is possible to construct a zero scalar curvature metric on the generalized connected sum. The idea consists in doing a slight modification of the approximate solution metric $g_{\varepsilon}$ away from the gluing locus. By means of this modification it is possible to obtain the vanishing of the term $\int_{M} F_{\varepsilon}(v) \mathrm{d} v o l_{g_{\varepsilon}}$ without using the nonzero constant scalar curvature $S=S(\varepsilon, v)$ and it is also possible to show that up to carefully choose the size of the adjustment, the approximate eigenvalue $\lambda_{F_{\varepsilon}\left(v_{\varepsilon}\right)}$ is zero.

Let us describe the construction. Instead of the metric $g_{\varepsilon}$ let us consider the new approximate solution metric $\overline{g_{\varepsilon}}(r, s)=g_{\varepsilon}+r h_{1}+s h_{2}$, where $h_{1}$ and $h_{2}$ are positive definite symmetric tensors supported respectively on the manifolds $M_{1}$ and $M_{2}$ away
from the polyneck, and $r$ and $s$ are real numbers. Hence the equation we are induced to solve is the following
$$\Delta_{\overline{g_{\varepsilon}}} v=\overline{F_{\varepsilon}}(v, r, s)-\lambda_{\overline{F_{\varepsilon}}(v, r, s)} \beta_{\varepsilon}$$
where $\overline{F_{\varepsilon}}(v)=-c_{n} S_{\overline{g_{\varepsilon}}}(1+v)$. Notice that by defining $\overline{F_{\varepsilon}}$ that way we have automatically imposed that the final scalar curvature which we are going to achieve is zero.

As in the previous case, we will obtain the solution of the problem by means of a fixed point argument lying on a sequence method. Concerning the linear analysis, notice that the construction above allows us to use all the results we have already obtained, hence let us focus on the nonlinear analysis.

Since the condition $\int_{M} \overline{F_{\varepsilon}}(v, r, s) \mathrm{d} v o l_{g_{\varepsilon}}=0$ has to be verified, we have that $r, s=\mathcal{O}\left(\varepsilon^{n-2}\right)$ and so it is easy to obtain a result analogous to the lemma 4.1 for the map $\overline{P_{\varepsilon}}$ (with obvious notation), with the same estimate for the radius $r_{\varepsilon}$.

It is also immediate to prove that for sufficiently small $\varepsilon>0$ the map $\overline{P_{\varepsilon}}$ is a contraction and more precisely
$$\left\|\overline{P_{\varepsilon}}(u)-\overline{P_{\varepsilon}}(v)\right\|_{\mathcal{C}_{\gamma}^{0}(M)} \leq C \varepsilon\|u-v\|_{\mathcal{C}_{\gamma}^{0}(M)}$$
for a suitable constant $C>0$. In particular the sequence defined by $v_{j}:=\overline{P_{\varepsilon}^{j}(0)}$ converges with respect to the norm $\|\cdot\|_{\mathcal{C}_{\gamma}^{0}(M)}$ to a function $v_{\varepsilon}$.

It remains to check that the operator $\overline{P_{\varepsilon}}$ is actually well defined. In particular we require that $\int_{M} \overline{F_{\varepsilon}}(v, r, s) \mathrm{d} v o l_{g_{\varepsilon}}=0$.

Before starting the calculation let us make some remarks concerning the scalar curvature of the metric $\overline{g_{\varepsilon}}$, in order to get more information about $\overline{F_{\varepsilon}}$. Since the supports of $S_{g_{\varepsilon}}, h_{1}, h_{2}$ are disjoint, we can write
$$\begin{aligned}
S_{\overline{g_{\varepsilon}}} & =S_{g_{\varepsilon}}+S_{g_{1}+r h_{1}}+S_{g_{2}+s h_{2}} \\
& =S_{g_{\varepsilon}} \\
& +S_{g_{1}}+r K_{1}+\mathcal{O}\left(r^{2}\right) \\
& +S_{g_{2}}+s K_{2}+\mathcal{O}\left(s^{2}\right) \\
& =S_{g_{\varepsilon}}+r K_{1}+\mathcal{O}\left(r^{2}\right)+s K_{2}+\mathcal{O}\left(s^{2}\right)
\end{aligned}$$
where, following [3]
$$K_{i}=\Delta_{g_{i}}\left(\operatorname{tr}_{g_{i}} h_{i}\right)+\delta_{g_{i}}\left(\delta_{g_{i}} h_{i}\right)+g_{i}\left(\operatorname{Ric}_{g_{i}}, h_{i}\right)$$
for $i=1,2$. In the notation above $\delta_{g_{i}}$ indicate the divergence of a symmetric tensor with respect to the metric $g_{i}$, and $\operatorname{Ric}_{g_{i}}$ is the Ricci tensor of the metric $g_{i}$.

When we integrate we obtain
$$\begin{aligned}
\int_{M} K_{i} \mathrm{~d} v o l_{g_{\varepsilon}} & =\int_{M_{i}} K_{i} \mathrm{~d} v o l_{g_{i}} \\
& =\int_{M_{i}} g_{i}\left(\operatorname{Ric}_{g_{i}}, h_{i}\right) \mathrm{d} v o l_{g_{i}}
\end{aligned}$$
because of the divergence theorem. Notice that in the Ricci flat case the integral above is zero and there is no chance to correct the term $\int_{M} S_{g_{\varepsilon}}(1+v) \mathrm{d} v o l_{g_{\varepsilon}}$ in order to get the condition $\int_{M} \overline{F_{\varepsilon}(v, r, s)} \mathrm{d} v o l_{g_{\varepsilon}}=0$.

Let us define the map $G_{\varepsilon, j}(r, s)$ as follows:
$$\begin{aligned}
G_{\varepsilon, j} & :=\int_{M} S_{g_{\varepsilon}}\left(1+v_{j}\right) \mathrm{d} v o l_{g_{\varepsilon}} \\
& +\int_{M_{1}} S_{g_{1}+r h_{1}}\left(1+v_{j}\right) \mathrm{d} v o l_{g_{1}} \\
& +\int_{M_{2}} S_{g_{2}+s h_{2}}\left(1+v_{j}\right) \mathrm{d} v o l_{g_{2}} \\
& =\int_{M} S_{g_{\varepsilon}} \mathrm{d} v o l_{g_{\varepsilon}}+r \int_{M_{1}} K_{1} \mathrm{~d} v o l_{g_{1}}+s \int_{M_{2}} K_{2} \mathrm{~d} v o l_{g_{2}} \\
& +E_{1}^{(j)}(r, s)+E_{2}^{(j)}(r, s)
\end{aligned}$$
where
$$\begin{aligned}
E_{1}^{(j)} & =\int_{M} S_{g_{\varepsilon}} v_{j} \mathrm{~d} v o l_{g_{\varepsilon}}+r \int_{M_{1}} K_{1} v_{j} \mathrm{~d} v o l_{g_{1}}+s \int_{M_{2}} K_{2} v_{j} \mathrm{~d} v o l_{g_{2}} \\
E_{2}^{(j)} & =\int_{M_{1}} S_{g_{1}+r h_{1}}\left(1+v_{j}\right) \mathrm{d} v o l_{g_{1}}-r \int_{M_{1}} K_{1}\left(1+v_{j}\right) \mathrm{d} v o l_{g_{1}} \\
& +\int_{M_{2}} S_{g_{2}+s h_{2}}\left(1+v_{j}\right) \mathrm{d} v o l_{g_{2}}-s \int_{M_{2}} K_{2}\left(1+v_{j}\right) \mathrm{d} v o l_{g_{2}}
\end{aligned}$$
at this point our purpose is to describe the set where $G_{\varepsilon, j}(r, s)$ is zero.
Towards this aim let us consider the map $H_{\varepsilon}(r, s):=G_{\varepsilon, j}(r, s)-E_{1}^{(j)}(r, s)-$ $E_{2}^{(j)}(r, s)$. In order to simplify the calculus we can suppose that the symmetric tensors $h_{1}$ and $h_{2}$ are so chosen that $\int_{M_{1}} K_{1} \mathrm{~d} v o l_{g_{1}}=\int_{M_{2}} K_{2} \mathrm{~d} v o l_{g_{2}}=1$. We can also assume $\int_{M} S_{g_{\varepsilon}} \mathrm{d}$ vol $_{g_{\varepsilon}}<0$ (if it is not the case, we can conclude by means of obvious modifications) and since $\int_{M} S_{g_{\varepsilon}} \mathrm{d} v o l_{g_{\varepsilon}}=\mathcal{O}\left(\varepsilon^{n-2}\right)$ we can set, up to normalize, $\int_{M} S_{g_{\varepsilon}} \mathrm{d} \operatorname{vol}_{g_{\varepsilon}}=-\varepsilon^{n-2}$. The expression for $H_{\varepsilon}$ becomes then the following
$$H_{\varepsilon}(r, s)=-\varepsilon^{n-2}+r+s$$
The set where $H_{\varepsilon}$ vanishes is given by $\left\{(r, s) \in \mathbb{R}^{2} \mid r+s=\varepsilon^{n-2}\right\}$. We will show that the set where $G_{\varepsilon, j}$ vanishes is uniformly close to the set $\left\{H_{\varepsilon}=0\right\}$ with respect to $j$.

As we have already seen, there exists positive constant $A>0$ such that for every $j \in \mathbb{N}$
$$\begin{aligned}
& \left|v_{j}\right| \leq A \varepsilon^{(n-2)+1} \quad \text { when } \quad n=3 \\
& \left|v_{j}\right| \leq A \varepsilon^{(n-2)+(1+\gamma)} \quad \text { when } \quad n \geq 4
\end{aligned}$$
Moreover, since $r, s=\mathcal{O}\left(\varepsilon^{n-2}\right)$ it is easy to see that there exist positive constants $B_{1}, B_{2}$ such that for every $j \in \mathbb{N}$
$$\begin{aligned}
& \left|E_{1}^{(j)}\right| \leq B_{1} \varepsilon^{(n-2)+1} \quad \text { when } n=3 \\
& \left|E_{1}^{(j)}\right| \leq B_{1} \varepsilon^{(n-2)+(1+\gamma)} \quad \text { when } \quad n \geq 4 \\
& \left|E_{2}^{(j)}\right| \leq B_{2} \varepsilon^{2(n-2)}
\end{aligned}$$
In particular, for an arbitrarily small fixed constant $c>0$ and sufficiently small $\varepsilon>0$ we have that
$$\begin{aligned}
& \left|E_{1}^{(j)}\right| \leq(c / 2) \varepsilon^{n-2} \\
& \left|E_{2}^{(j)}\right| \leq(c / 2) \varepsilon^{n-2}
\end{aligned}$$
At this point it is immediate to see that for every $j \in \mathbb{N}$
$$\begin{aligned}
\left\{G_{\varepsilon, j}(r, s)=0\right\} & =\left\{(r, s) \in \mathbb{R}^{2} \quad \mid \quad r+s=\varepsilon^{n-2}-E_{1}^{(j)}(r, s)-E_{2}^{(j)}(r, s)\right\} \\
& \subseteq\left\{(r, s) \in \mathbb{R}^{2} \quad \mid \quad(1-c) \varepsilon^{n-2} \leq r+s \leq(1+c) \varepsilon^{n-2}\right\} \\
& =: Z_{\varepsilon}
\end{aligned}$$

If we set now $r_{0}^{(j)}:=\varepsilon^{n-2} / 2$ for every $j \in \mathbb{N}$, it must exists a real number $s_{0}^{(j)}$ such that $\left(\varepsilon^{n-2}, s_{0}^{(j)}\right) \in Z_{\varepsilon}$ and $G_{\varepsilon, j}\left(\varepsilon^{n-2} / 2, s_{0}^{(j)}\right)=0$.

Obviously $G_{\varepsilon, j}$ are smooth functions with respect to the variables $r$ and $s$ and in particular it is quite easy to get the following uniform estimate for the first and the second partial derivatives at the origin.
$$\begin{aligned}
\left|\frac{\partial G_{\varepsilon, j}}{\partial r}(0,0)\right| & \leq \int_{M_{1}}\left|\frac{\partial S\left(g_{1}+r h_{1}\right)}{\partial r}(0,0) \cdot\left(1+v_{j}\right)\right| \mathrm{d} v o l_{g_{1}} \\
& \leq\left\|1+v_{j}\right\|_{\mathcal{C}^{0}(M)} \int_{M_{1}}\left|\frac{\partial S\left(g_{1}+r h_{1}\right)}{\partial r}(0,0)\right| \mathrm{d} v o l_{g_{1}} \\
& \leq 2 \int_{M_{1}}\left|\frac{\partial S\left(g_{1}+r h_{1}\right)}{\partial r}(0,0)\right| \mathrm{d} v o l_{g_{1}}
\end{aligned}$$
$$\begin{aligned}
\left|\frac{\partial^{2} G_{\varepsilon, j}}{\partial r^{2}}(0,0)\right| & \leq \int_{M_{1}}\left|\frac{\partial^{2} S\left(g_{1}+r h_{1}\right)}{\partial r^{2}}(0,0) \cdot\left(1+v_{j}\right)\right| \mathrm{d} v o l_{g_{1}} \\
& \leq 2 \int_{M_{1}}\left|\frac{\partial^{2} S\left(g_{1}+r h_{1}\right)}{\partial r^{2}}(0,0)\right| \mathrm{d} v o l_{g_{1}}
\end{aligned}$$
for every $j \in \mathbb{N}$. Notice that the same estimates hold for the partial derivatives in $s$ and that the terms $\frac{\partial^{2} G_{\varepsilon, j}}{\partial s \partial r}(0,0)$ and $\frac{\partial^{2} G_{\varepsilon, j}}{\partial r \partial s}(0,0)$ are zero.

Concerning the modulus of the first partial derivative at the origin, we are also able to provide a uniform lower bound, in fact
$$\begin{aligned}
\left|\frac{\partial G_{\varepsilon, j}}{\partial r}(0,0)\right| & =\left|\int_{M_{1}} K_{1} \cdot\left(1+v_{j}\right) \mathrm{d} v o l_{g_{1}}\right| \\
& \geq\left|\int_{M_{1}} K_{1} \mathrm{~d} v o l_{g_{1}}\right|-\int_{M_{1}}\left|K_{1}\right|\left|v_{j}\right| \mathrm{d} v o l_{g_{1}} \\
& \geq\left|\int_{M_{1}} K_{1} \mathrm{~d} v o l_{g_{1}}\right|-\left\|v_{j}\right\|_{\mathcal{C}^{0}(M)} \int_{M_{1}}\left|K_{1}\right| \mathrm{d} v o l_{g_{1}} \\
& \geq \frac{1}{2}\left|\int_{M_{1}} K_{1} \mathrm{~d} v o l_{g_{1}}\right| \\
& >0 \text { for sufficiently small } \varepsilon>0
\end{aligned}$$
for every $j \in \mathbb{N}$. Of course, the same is true for $\frac{\partial G_{\varepsilon, j}}{\partial s}(0,0)$.
Now, arguing by contradiction and using these estimate it is possible to deduce that there exists a positive constant $C>0$ and a positive real number $R>0$ such that both the first partial derivatives $\left|\frac{\partial G_{\varepsilon, j}}{\partial r}\right|$ and $\left|\frac{\partial G_{\varepsilon, j}}{\partial r}\right|$ are greater than $C$ in $B_{R}((0,0))$, for every $j \in \mathbb{N}$.

Up to choose $\varepsilon$ sufficiently small, we have that the set $Z_{\varepsilon} \cap\{r, s \geq 0\}$ lies in the ball of radius $R$ centered at the origin, hence it is possible to apply the implicit function theorem to the functions $G_{\varepsilon, j}$ around the points $\left(\varepsilon^{n-2} / 2, s_{0}^{(j)}\right)$, so that we obtain, for every $j$, an open neighborhood $U^{(j)}$ of $r_{0}^{(j)}$, an open neighborhood $V^{(j)}$ of $s_{0}^{(j)}$ and a smooth function $f_{j}: U^{(j)} \longrightarrow V^{(j)}$ such that $G_{\varepsilon, j}\left(r, f_{j}(r)\right)=0$ for every $r \in U^{(j)}$.

Since it is possible to extend each implicit function $f_{j}$ to the interval ( $0,(1-$ $c) \varepsilon^{n-2}$ ), we can suppose that there exists an open neighborhood $U$ of $\varepsilon^{n-2} / 2$ and an open neighborhood $V$ of every $s_{0}^{(j)}$ such that it is possible to choose $U^{(j)}=U$ and $V^{(j)}=V$ for every $j \in \mathbb{N}$.

Let us fucus now on the family of functions $\left\{f_{j}\right\}_{j \in \mathbb{N}}$. Since each $f_{j}$ is a uniformly continuous function, we can extend them to the compact set $\bar{U}$, so that we have to handle now a family of functions $f_{j}: \bar{U} \longrightarrow \bar{V}$ defined on a compact set and all bounded by the same constant $(1+c) \varepsilon^{n-2}$.

At this point our aim is to show that the $f_{j}$ 's admit the same Lipschitz's constant. First remember that
$$f_{j}(r)=\int_{M} S_{g_{\varepsilon}} \mathrm{d} v o l_{g_{\varepsilon}}-r+E_{1}^{(j)}(r)+E_{2}^{(j)}(r)$$
and consequently, for $r, r^{\prime} \in U$
$$\begin{aligned}
\left|f_{j}(r)-f_{j}\left(r^{\prime}\right)\right| & \leq\left|r-r^{\prime}\right| \\
& +\left|E_{1}^{(j)}(r)-E_{1}^{(j)}\left(r^{\prime}\right)\right| \\
& +\left|E_{2}^{(j)}(r)-E_{2}^{(j)}\left(r^{\prime}\right)\right| \\
& \leq\left|r-r^{\prime}\right| \\
& +\int_{M_{1}}\left|K_{1}\right| \mathrm{d} v o l_{g_{1}}\left\|v_{j}\right\|_{\mathcal{C}^{0}(M)}\left|r-r^{\prime}\right| \\
& +\int_{M_{2}}\left|K_{2}\right| \mathrm{d} v o l_{g_{2}}\left\|v_{j}\right\|_{\mathcal{C}^{0}(M)}\left|f_{j}(r)-f_{j}\left(r^{\prime}\right)\right| \\
& +C_{1} \varepsilon^{n-2}\left|r-r^{\prime}\right|+C_{2} \varepsilon^{n-2}\left|f_{j}(r)-f_{j}\left(r^{\prime}\right)\right|
\end{aligned}$$
for suitable $C_{1}, C_{2}>0$. Now, for $n=3$, we have that $\left\|v_{j}\right\|_{\mathcal{C}^{0}(M)} \leq \tilde{D} \varepsilon^{1-\gamma}$, whereas, for $n \geq 4,\left\|v_{j}\right\|_{\mathcal{C}^{0}(M)} \leq \tilde{D} \varepsilon$, so it is easy to deduce that
$$\left|f_{j}(r)-f_{j}\left(r^{\prime}\right)\right| \leq \frac{1+D_{1} \varepsilon^{1-\gamma}+C_{1} \varepsilon^{n-2}}{1-D_{2} \varepsilon^{1-\gamma}-C_{2} \varepsilon^{n-2}}\left|r-r^{\prime}\right|$$
when $n=3$, and
$$\left|f_{j}(r)-f_{j}\left(r^{\prime}\right)\right| \leq \frac{1+D_{1} \varepsilon+C_{1} \varepsilon^{n-2}}{1-D_{2} \varepsilon-C_{2} \varepsilon^{n-2}}\left|r-r^{\prime}\right|$$
when $n \geq 4$, where $D_{i}=\tilde{D} \int_{M_{i}}\left|K_{i}\right| \mathrm{d} v o l_{g_{i}}, i=1,2$.
Thanks to the Ascoli - Arzelá theorem and up to consider subsequence, the $f_{j}$ 's converges with respect to the norm $\|\cdot\|_{\mathcal{C}^{0}(U)}$ to a continuous function $f$.

Notice that in order to get a solution for the equation 18 we could have picked a point $\bar{r} \in \bar{U}$ and deduced immediately the convergence, up to subsequences, of the $f_{j}(\bar{r})$ 's to a point $\bar{s}$, but in the following we want to use the parameter $r$ to kill the term $\lambda_{\overline{F_{\varepsilon}}\left(v_{\varepsilon}, r, f(r)\right)}$ and the continuity of $f$ will be crucial.

We are now ready to discuss the sign of the term $\lambda_{\overline{F_{\varepsilon}}\left(v_{\varepsilon}, r, f(r)\right)}$ which appears in the identity
$$\Delta_{\overline{g_{\varepsilon}}} v_{\varepsilon}=\overline{F_{\varepsilon}}\left(v_{\varepsilon}, r, f(r)\right)-\lambda_{\overline{F_{\varepsilon}}\left(v_{\varepsilon}, r, f(r)\right)} \beta_{\varepsilon}$$
As we have already seen, the sign of the approximate eigenvalue for small $\varepsilon>0$ is determined by the sign of its part of order $\varepsilon^{n-2}$, it is to say that if this one is strictly positive or negative, so does $\lambda_{\overline{F_{\varepsilon}}\left(v_{\varepsilon}, r, f(r)\right)}$. Hence our task is to show that the sign of
$$\int_{M} S_{g_{\varepsilon}} \chi_{1} \mathrm{~d} v o l_{g_{\varepsilon}}-\int_{M} S_{g_{\varepsilon}} \chi_{2} \mathrm{~d} v o l_{g_{\varepsilon}}+r \int_{M_{1}} K_{1} \mathrm{~d} v o l_{g_{1}}-f(r) \int_{M_{2}} K_{2} \mathrm{~d} v o l_{g_{2}}$$
becomes positive or negative if we move $r \in \bar{U}$. Then, thanks to the continuity of $f$ we deduce the existence of a real number $\bar{r}$ in correspondence of which the approximate
eigenvalue vanishes.

Since there exists a constant $C>0$ such that
$$\left|\int_{M} S_{g_{\varepsilon}} \chi_{1} \mathrm{~d} v o l_{g_{\varepsilon}}-\int_{M} S_{g_{\varepsilon}} \chi_{2} \mathrm{~d} v o l_{g_{\varepsilon}}\right| \leq C \varepsilon^{n-2}$$
and since it is always possible to choose $r$ either in a region of $U$ where $f(r)>r$ or in a region where $f(r)<r$, it is clear that our goal is achieved if we impose that
$$\left|\int_{M_{1}} K_{1} \mathrm{~d} v o l_{g_{1}}\right|=\left|\int_{M_{2}} K_{2} \mathrm{~d} v o l_{g_{2}}\right|>\frac{C \varepsilon^{n-2}}{|f(r)-r|}$$
and we are always allowed to do that.

\section*{References}
\begin{itemize}
\item[] [1] M. Anderson, Dehn filling and Einstein metrics in higher dimensions, arxiv:math.DG/0303260 (2003).
\item[] [2] T. Aubin, Some nonlinear Problems in Riemannian Geometry, Springer Monographs in Mathematics, Springer, (1998).
\item[] [3] A.L. Besse, Einstein Manifolds, Spinger, (1987).
\item[] [4] D. Gilbarg, N. Trudinger, Elliptic Partial Differential Equation of Second Order, Springer, (1983).
\item[] [5] D. Joyce Constant scalar curvature metrics on connected sums. Int. J. Math. Math. Sci. (2003), no. 7, 405-450.
\item[] [6] J.M. Lee, T.H. Parker, The Yamabe Problem, Bull. A.M.S. 17 (1987), 37-91.
\item[] [7] R. Mazzeo, F. Pacard, Constant scalar curvature metrics with isolated singularities, Duke Math. Journal 99 No. 3 (1999) 353-418.
\item[] [8] R. Mazzeo, F. Pacard, Constant mean curvature surfaces with Delaunay ends, Comm. Anal. Geom. 9 No. 1 (2001) 169-237.
\item[] [9] R. Mazzeo, F. Pacard, D. Pollack, Connected sums of constant mean curvature surfaces in Euclidean 3 space, J. Reine Angew. Math. 536 (2001), 115-165.
\item[] [10] R. Mazzeo, D. Pollack e K. Uhlenbeck, Connected sums constructions for constant scalar curvature metrics, Topological Method in Nonlinear Analysis 6 (1995), 207-233.
\item[] [11] L. Mazzieri Generalized connected sum construction for constant scalar curvature metrics to appear in Communication on Partial Differential Equations.
\item[] [12] Gromov, M. and Lawson, H. B. The classification of simply connected manifolds of positive scalar curvature. Ann. of Math. (2) 111 (1980), no. 3, 423-434.
\item[] [13] Schoen, R. and Yau, S. T. On the structure of manifolds with positive scalar curvature. Manuscripta Math. 28 (1979), no. 1-3, 159-183
\end{itemize}
---
retention_scope: session
part: 1
total_parts: 1
---

---
source_file: 1409_4004v3.pdf
converter: mathpix
format: mmd
---

\title{
SCALAR CURVATURE FUNCTIONS OF ALMOST-KÄHLER METRICS
}

\author{
JONGSU KIM AND CHANYOUNG SUNG
}

\begin{abstract}
For a closed smooth manifold $M$ admitting a symplectic structure, we define a smooth topological invariant $Z(M)$ using almost-Kähler metrics, i.e. Riemannian metrics compatible with symplectic structures. We also introduce $Z(M,[[\omega]])$ depending on symplectic deformation equivalence class $[[\omega]]$. We first prove that there exists a 6-dimensional smooth manifold $M$ with more than one deformation equivalence classes with different signs of $Z(M,[[\omega]])$. Using $Z$ invariants, we set up a Kazdan-Warner type problem of classifying symplectic manifolds into three categories.

We finally prove that on every closed symplectic manifold $(M, \omega)$ of dimension $\geq 4$, any smooth function which is somewhere negative and somewhere zero can be the scalar curvature of an almost-Kähler metric compatible with a symplectic form which is deformation equivalent to $\omega$.
\end{abstract}

\section*{1. Introduction}

In Riemannian geometry, scalar curvature encodes certain information of the differential topology of a smooth closed manifold. There has been much progress on topological conditions for the existence of a metric of positive scalar curvature, and more generally which functions on a given manifold can be the scalar curvature of a Riemannian metric.

The latter problem is known as the Kazdan-Warner problem. They proved [9] that the necessary and sufficient condition for a smooth function $f$ on a closed manifold $M$ of dimension $\geq 3$ to be the scalar curvature of some metric is
\begin{itemize}
\item[-] $f$ is arbitrary, in case $Y(M)>0$,
\item[-] $f$ is identically zero or somewhere negative, in case $Y(M)=0$ and $M$ admits a scalar-flat metric,
\item[-] $f$ is negative somewhere, in the remaining case,
\end{itemize}

\footnotetext{
Date: July 17, 2018.
2010 Mathematics Subject Classification. 53D05,53D35,53C15,53C21.
Key words and phrases. almost-Kähler, scalar curvature, symplectic manifold.
The first author was supported by the National Research Foundation of Korea(NRF) grant funded by the Korea government(MOE) (No.NRF-2010-0011704).
}
where $Y(M)$ denotes the Yamabe invariant of $M$. For the Yamabe invariant, the readers are referred to [13].

As an extension of the Kazdan-Warner problem, it is natural to pursue a similar classification in some restricted class of Riemannian metrics.

Let $M$ be a smooth manifold with a symplectic form $\omega$. An almost-complex structure $J$ is called $\omega$-compatible, if $\omega(J \cdot, J \cdot)=\omega(\cdot, \cdot)$, and $\omega(\cdot, J \cdot)$ is positive-definite. Thus a smooth $\omega$-compatible $J$ defines a smooth $J$ -invariant Riemannian metric $g(\cdot, \cdot):=\omega(\cdot, J \cdot)$, which is called an $\omega$-almost-Kähler metric. It is Kähler iff $J$ is integrable.

Due to the lack of a Yamabe-type theorem ([15]) which would produce metrics of constant scalar curvature, a Kazdan-Warner type result for symplectic manifolds is left open even without any conjectures. A general existence result so far is in [10] stating that every symplectic manifold of dimension $\geq 4$ admits a complete compatible almost-Kähler metric of negative scalar curvature.

In [12, 11], we studied a symplectic version of the Kazdan-Warner problem and in particular we characterized the scalar curvature functions of some symplectic tori and nil-manifolds. Here we shall refine this version of Kazdan-Warner problem.

Let us recall that two symplectic forms $\omega_{0}$ and $\omega_{1}$ on $M$ are called deformation equivalent, if there exists a diffeomorphism $\psi$ of $M$ such that $\psi^{*} \omega_{1}$ and $\omega_{0}$ can be joined by a smooth homotopy of sympelctic forms, [17]. There are a number of smooth manifolds which admit more than one deformation equivalence classes: see [22] or references therein. For a symplectic form $\omega$, its deformation equivalence class shall be denoted by $[[\omega]]$. By abuse of notation, we say that a metric $g$ is in $[[\omega]]$ when $g$ is compatible with a symplectic form $\omega$ in $[[\omega]]$.

Definition 1. Let $M$ be a smooth closed manifold of dimension $2 n \geq 4$ which admits a symplectic structure. Define
$$Z(M,[[\omega]])=\sup _{g \in[[\omega]]} \frac{\int_{M} s_{g} d v o l_{g}}{\left(\operatorname{Vol}_{g}\right)^{\frac{n-1}{n}}},$$
where $s_{g}$ is the scalar curvature of $g$, and define
$$Z(M)=\sup _{[[\omega]]} Z(M,[[\omega]]) .$$

The denominator in $\frac{\int_{M} s_{g} d \mathrm{vol}_{g}}{\left(\operatorname{Vol}_{g}\right)^{\frac{n-1}{n}}}$ was put for the invariance under a scale change $\omega \rightarrow c \cdot \omega$ with $c>0$, and one can get the following inequality from
the formulas (2.2) and (6.15) below;
$$Z(M,[[\omega]]) \leq \sup _{\omega \in[[\omega]]} \frac{4 \pi c_{1}(\omega) \cdot \frac{[\omega]^{n-1}}{(n-1)!}}{\left(\frac{[\omega]^{n}}{n!}\right)^{\frac{n-1}{n}}},$$
where $c_{1}(\omega)$ is the first Chern class of $\omega$.
These $Z$ numbers may take the value of $\infty$ and are different in nature from the Yamabe invariant which is bounded above in each dimension. Obviously $Z(M)$ is a smooth topological invariant of $M$. Although the quantity in the right hand side of (1.1) may serve usefully for many purposes, the $Z$ value reflects almost-Kähler geometry better, so seems more relevant to our purpose. Of course, it would be very interesting to know if the equality in (1.1) always holds or not.

To explain why possible scalar curvature functions may depend on $[[\omega]]$, we shall demonstrate a smooth manifold which admits two symplectic deformation equivalence classes with distinct signs of $Z(M,[[\omega]])$.

Theorem 1.1. There exists a smooth closed 6-dimensional manifold with distinct symplectic deformation equivalence classes $\left[\left[\omega_{i}\right]\right], i=1,2$ such that $Z\left(M,\left[\left[\omega_{1}\right]\right]\right)=\infty$ and $Z\left(M,\left[\left[\omega_{2}\right]\right]\right)<0$.

Next, we use the method of [10, 11] to prove our main theorem;
Theorem 1.2. Let $(M,[[\omega]])$ be a smooth closed manifold of dimension $2 n \geq$ 4 with a deformation equivalence class of symplectic forms. Then any smooth function on $M$ which is somewhere negative and somewhere zero is the scalar curvature of some smooth almost-Kähler metric in $[[\omega]]$.

We speculate that any smooth somewhere-negative function on a closed manifold $M$ with $[[\omega]]$ might be the scalar curvature of some smooth almost-Kähler metric in $[[\omega]]$. A key step to prove it should be to show that every $(M,[[\omega]])$ has an almost-Kähler metric of negative constant scalar curvature in $[[\omega]]$.

With $Z$ ready, one can see that Theorem 1.2 contributes to answering the following question;

Question 1.3. Let $M$ be a smooth closed manifold of dimension $2 n \geq 4$ admitting a symplectic structure.

Is the (necessary and sufficient) condition for a smooth function $f$ on $M$ to be the scalar curvature of some smooth almost-Kähler metric as follows?
(a) $f$ is arbitrary, if $0<Z(M) \leq \infty$,
(b) $f$ is identically zero or somewhere negative, if $Z(M)=0$ and $M$ admits a scalar-flat almost-Kähler metric,
(c) $f$ is negative somewhere, if otherwise.

Also, is the condition for a smooth function $f$ on $M$ to be the scalar curvature of some smooth almost-Kähler metric in $[[\omega]]$ as follows?
\begin{itemize}
\item[] ( $a^{\prime}$ ) $f$ is arbitrary, if $0<Z(M,[[\omega]]) \leq \infty$,
\item[] $\left(b^{\prime}\right) f$ is identically zero or somewhere negative, if $Z(M,[[\omega]])=0$ and $M$ admits a scalar-flat almost-Kähler metric in $[[\omega]]$,
\item[] $\left(c^{\prime}\right) f$ is negative somewhere, if otherwise.
\end{itemize}

This paper is organized as follows. In section 2, some computations of $Z(M)$ are explained. Theorem 1.1 is proved in section 3. In section 4, Kazdan-Warner type argument in almost Kähler setting is explained. Theorem 1.2 is proved in section 5 and 6.

\section*{2. Some computations of $Z(M)$}

In this section we explain some basic properties and computations of $Z$ invariant in relatively simple cases.

Lemma 2.1. Let $M$ be a smooth closed manifold of dimension $\geq 4$ admitting a symplectic structure. If $Y(M) \leq 0$, then $Z(M) \leq 0$.

Proof. Suppose not. Then there exists an almost Kähler metric $g$ on $M$ such that $\int_{M} s_{g} d v o l_{g}>0$. Then by the Yamabe problem [15], a conformal change of $g$ gives a metric of positive constant scalar curvature. This implies that $Y(M)>0$, thereby yielding a contradiction. \(\square\)

Lemma 2.2. Any compact minimal Kähler surface $M$ of Kodaira dimension 0 has $Z(M)=0$, and it is attained by a Ricci-flat Kähler metric.

Proof. By the Kodaira-Enriques classification [3], such $M$ is K3 or $T^{4}$ or their finite quotients, and hence it admits a Ricci-flat Kähler metric. Thus $Z(M) \geq 0$. Since $M$ cannot admit a metric of positive scalar curvature, (in fact, $Y(M)=0$ ), the above lemma forces $Z(M)=0$. \(\square\)

By using Lemma 2.1, one can show that if $Y(M)=0$, and $M$ admits a "collapsing" sequence of almost-Käher metrics with bounded scalar curvature, then $Z(M)=0$. For example, we consider the Kodaira-Thurston manifold $M_{K T}$; see Section 4.

Lemma 2.3. For the Kodaira-Thurston manifold $M_{K T}, Z\left(M_{K T}\right)=0$, and it is obtained as the limit by a collpasing sequence of almost-Kähler metrics of negative constant scalar curvature.

Proof. $M_{K T}$ never admits a metric of positive scalar curvature; one can use Seiberg-Witten theory, see [18]. So, $Y\left(M_{K T}\right) \leq 0$. Thus $Z\left(M_{K T}\right) \leq 0$ by Lemma 2.1.

We let $\mathbb{R}^{4}=\{(x, y, z, t)\}$ endowed with the metric $d x^{2}+d y^{2}+(d z-$ $x d y)^{2}+d t^{2}$. Then $M_{K T}$ with an almost-Kähler metric is obtained as the quotient of $\mathbb{R}^{4}$ by the group generated by isometric actions,
$$\begin{array}{cc}
\gamma_{1}(x, y, z, t)=(x+1, y, y+z, t), & \gamma_{2}(x, y, z, t)=(x, y+1, z, t), \\
\gamma_{3}(x, y, z, t)=(x, y, z+1, t), & \gamma_{4}(x, y, z, t)=(x, y, z, t+d),
\end{array}$$
where $d$ is any positive constant.
For any $d>0$, the scalar curvature is $-\frac{1}{2}$. (See the curvature computations in Lemma 6.2.) But by taking $d>0$ sufficiently small, we can get an almost-Kähler metric $g$ on $M_{K T}$ such that $\int_{M_{K T}} s_{g} d \operatorname{vol}_{g} /\left(\operatorname{Vol}_{g}\right)^{\frac{1}{2}}$ is arbitrarily close to 0 . Therefore $Z\left(M_{K T}\right)=0$. \(\square\)

Now $M_{K T}$, with $Z\left(M_{K T}\right)=0$, never admits a scalar-flat almost-Kähler metric, because such a metric has to be a Kähler metric, which is not allowed on $M_{K T}$ with $b_{1}\left(M_{K T}\right)=3$. Therefore one can expect that $M_{K T}$ belongs to the category (c) in the classification of Question 1.3. Indeed this was already proved in [11]. Note that $M_{K T}$ is a nilmanifold. One may expect to find more examples of symplectic solvmanifolds with vanishing $Z$ value and prove them to be in the category (c).

Now let us give an example of $Z(M)>0$.
Lemma 2.4. For the complex projective plane $\mathbb{C} P^{2}, Z\left(\mathbb{C} P^{2}\right)=12 \sqrt{2} \pi$, and it is attained by a Kähler Einstein metric.

Proof. First we claim that $\mathbb{C} P^{2}$ with the reversed orientation does not support any almost complex structure. Suppose it does. Recall that any closed almost complex 4-manifold satisfy
$$c_{1}^{2}=2 \chi+3 \tau,$$
where $\chi$ and $\tau$ respectively denote Euler characteristic and signature. Then this formula gives $c_{1}^{2}=3$, which is impossible because of the fact that $c_{1} \in$ $H^{2}\left(\mathbb{C} P^{2} ; \mathbb{Z}\right)$. Thus $c_{1}^{2}$ must be 9 so that $c_{1}$ is $3[H]$ or $-3[H]$, where $[H]$ is the hyperplane class.

For any symplectic form $\omega$ on $\mathbb{C} P^{2},[\omega]$ must be a nonzero multiple of $[H]$. We apply the Blair formula (6.15) to get
$$\begin{aligned}
\frac{\int_{\mathbb{C} P^{2}} s_{g} d v o l_{g}}{\left(\operatorname{Vol}_{g}\right)^{\frac{1}{2}}} & \leq \frac{\int_{\mathbb{C} P^{2}} \frac{1}{2}\left(s_{g}+s_{g}^{*}\right) d v o l_{g}}{\left(\operatorname{Vol}_{g}\right)^{\frac{1}{2}}} \\
& =\frac{4 \pi c_{1}(\omega) \cdot[\omega]}{\left(\frac{[\omega] \cdot[\omega]}{2}\right)^{\frac{1}{2}}} \\
& = \pm 12 \sqrt{2} \pi,
\end{aligned}$$
for any $\omega$-almost-Kähler metric $g$ on $\mathbb{C} P^{2}$. In the above inequality, we used a relation between $s$ and the star-scalar curvature $s^{*}$ [2];
$$s^{*}-s=\frac{1}{2}|\nabla J|^{2} \geq 0 .$$

Therefore $Z\left(\mathbb{C} P^{2},[[\omega]]\right) \leq 12 \sqrt{2} \pi$. In fact the Fubini-Study metric with $\omega_{F S}$ saturates this upper bound, so we finally get
$$Z\left(\mathbb{C} P^{2}\right)=Z\left(\mathbb{C} P^{2},\left[\left[\omega_{F S}\right]\right]\right)=12 \sqrt{2} \pi .$$ \(\square\)

Remark 2.5. In the above we only treated a few simple examples. However, we expect that $Z$ invariant is fairly computable under some symplectic surgeries. For instance, one can see that $Z\left(\hat{T}^{4}\right)=0$, where $\hat{T}^{4}$ is the blowup at one point of the Kähler 4-torus. In fact, one only needs to check that LeBrun's argument in the proof of theorem 3 of [14] still works in almost Kähler context. This gives $Z\left(\hat{T}^{4}\right) \geq 0$. Together with Seiberg-Witten theory one gets $Z\left(\hat{T}^{4}\right)=0$. A similar argument, albeit in Kähler case, may be found in [23].

\section*{3. Symplectic deformation classes on a manifold with distinct signs of $Z(\cdot,[[\omega]])$}

In this section we shall prove Theorem 1.1.
We use one of the examples in [21]. Let $W$ be a complex Barlow surface, which is a minimal complex surface of general type homeomorphic, but not diffeomorphic, to $R_{8}$, the blown-up complex surface at 8 points in general position in the complex projective plane. By a small deformation of complex structure we may assume that $W$ has ample canonical line bundle [5]. Then by Yau's solution of Calabi conjecture, $W$ and $R_{8}$ admit a Kähler Einstein metric of negative (and positive, respectively) scalar curvature. Ruan showed that for a compact Riemann surface $\Sigma, R_{8} \times \Sigma$ and $W \times \Sigma$ are diffeomorphic but their natural symplectic structures are not deformation equivalent.

We prove;
Proposition 3.1. Let $W$ be a Barlow surface with ample canonical line bundle and $\Sigma$ be a Riemann surface of genus 2. Consider a Kähler Einstein metric of negative scalar curvature on $W$ with Kähler form $\omega_{W}$ on $W$ and a Kähler form $\omega_{\Sigma}$ on $\Sigma$ with constant negative scalar curvature.

Then $Z\left(W \times \Sigma,\left[\left[\omega_{W}+\omega_{\Sigma}\right]\right]\right)=-12 \pi$, and it is attained by a Kähler Einstein metric.

Proof. We recall a few results about $W$ from [21, Section 4]; there is a homeomorphism of $W$ onto $R_{8}$ which preserves the Chern class $c_{1}$ and there is a diffeomorphism of $W \times \Sigma$ onto $R_{8} \times \Sigma$ which preserves $c_{1}$.

Then, the first Chern class of $W$ can be written as $c_{1}(W)=3 E_{0}-$ $\sum_{i=1}^{8} E_{i} \in H^{2}(W, \mathbb{R}) \cong \mathbb{R}^{9}$, where $E_{i}, i=0, \cdots 8$, is the Poincare dual of a homology class $\tilde{E}_{i}, i=0, \cdots 8$ so that $\tilde{E}_{i}, i=0, \cdots 8$, form a basis of $H_{2}(W, \mathbb{Z}) \cong \mathbb{Z}^{9}$ and their intersections satisfy $\tilde{E}_{i} \cdot \tilde{E}_{j}=\epsilon_{i} \delta_{i j}$, where $\epsilon_{0}=1$ and $\epsilon_{i}=-1$ for $i \geq 1$. So, in this basis the intersection form becomes
$$I=\left[\begin{array}{ccccc}
1 & 0 & \cdot & \cdot & 0 \\
0 & -1 & \cdot & \cdot & 0 \\
\cdot & \cdot & \cdot & \cdot & 0 \\
\cdot & \cdot & \cdot & \cdot & 0 \\
0 & 0 & 0 & -1
\end{array}\right] .$$

We have the orientation of $W$ induced by the complex structure and the fundamental class $[W] \in H_{4}(W, \mathbb{Z}) \cong \mathbb{Z}$. As $\omega_{W}$ is Kähler Einstein of negative scalar curvature, we may get $\left[\omega_{W}\right]=-3 E_{0}+\sum_{i=1}^{8} E_{i}$ by scaling if necessary.

Now a compact Riemann surface $\Sigma$ of genus 2 has its fundamental class $[\Sigma] \in H_{2}(\Sigma, \mathbb{Z}) \cong \mathbb{Z}$. Let $c$ be the generator of $H^{2}(\Sigma, \mathbb{Z}) \cong \mathbb{Z}$ such that the pairing $\langle c,[\Sigma]\rangle=1$. Then $c_{1}(\Sigma)=-2 c$. We consider a Kähler form $\omega_{h}$ with constant negative scalar curvature such that $\left[\omega_{h}\right]=c \in H^{2}(\Sigma, \mathbb{R}) \cong \mathbb{R}$.

Set $M=W \times \Sigma$. By Künneth theorem, $H^{2}(M, \mathbb{R}) \cong \pi_{1}^{*} H^{2}(W) \oplus$ $\pi_{2}^{*} H^{2}(\Sigma) \cong \mathbb{R}^{9} \oplus \mathbb{R}$, where $\pi_{i}$ are the projection of $M$ onto the i-th factor. Then,
$$c_{1}(M)=\pi_{1}^{*} c_{1}(W)+\pi_{2}^{*} c_{1}(\Sigma)=\pi_{1}^{*}\left(3 E_{0}-\sum_{i=1}^{8} E_{i}\right)-2 \pi_{2}^{*} c \in H^{2}(M, \mathbb{R}) .$$
Consider any smooth path of symplectic forms $\omega_{t}, 0 \leq t \leq \delta$, on $M$ such that $\omega_{0}=\omega_{W}+\omega_{h}$. We may write
$$\left[\omega_{t}\right]=n_{0}(t) \pi_{1}^{*} E_{0}+\sum_{i=1}^{8} n_{i}(t) \pi_{1}^{*} E_{i}+l(t) \pi_{2}^{*} c \in H^{2}(M, \mathbb{R})$$
for some smooth functions $n_{i}(t), l(t), i=0, \cdots, 8$. As they are connected, their first Chern class $c_{1}\left(\omega_{t}\right)=c_{1}(M)$. We have;
$$\begin{aligned}
{\left[\omega_{t}\right]^{3}([W \times \Sigma]) } & =\left[n_{0}(t) \pi_{1}^{*} E_{0}+\sum_{i=1}^{8} n_{i}(t) \pi_{1}^{*} E_{i}+l(t) \pi_{2}^{*} c\right]^{3}([W \times \Sigma]) \\
& =3\left\{n_{0}^{2}(t)-\sum_{i=1}^{8} n_{i}^{2}(t)\right\} l(t)>0 .
\end{aligned}$$
As $l(0)=1>0, l(t)>0$. So, $n_{0}^{2}(t)>\sum_{i=1}^{8} n_{i}^{2}(t)$. From above, we know that $n_{0}(0)=-3<0$. As $n_{0}^{2}(t)>0$, we get $n_{0}(t)<0$.
$$c_{1} \cdot\left[\omega_{t}\right]^{2}([W \times \Sigma])=-2\left\{n_{0}^{2}(t)-\sum_{i=1}^{8} n_{i}^{2}(t)\right\}+2 l(t)\left\{3 n_{0}(t)+\sum_{i=1}^{8} n_{i}(t)\right\} .$$

Since $n_{0}^{2}(t)>\sum_{i=1}^{8} n_{i}^{2}(t)$ and $\left|\sum_{i=1}^{8} n_{i}(t)\right| \leq \sqrt{8} \sqrt{\sum_{i=1}^{8} n_{i}^{2}}$, we get
$$\begin{aligned}
3 n_{0}(t)+\sum_{i=1}^{8} n_{i}(t) & \leq 3 n_{0}(t)+2 \sqrt{2} \sqrt{\sum_{i=1}^{8} n_{i}^{2}(t)} \\
& <3 n_{0}(t)+2 \sqrt{2} \sqrt{n_{0}^{2}(t)}=(3-2 \sqrt{2}) n_{0}(t)<0 .
\end{aligned}$$

So, $c_{1} \cdot\left[\omega_{t}\right]^{2}([W \times \Sigma])<0$. Putting $A=n_{0}^{2}(t)-\sum_{i=1}^{8} n_{i}^{2}(t)$ and $B=$ $3 n_{0}(t)+\sum_{i=1}^{8} n_{i}(t)$, we have
$$\frac{c_{1}\left[\omega_{t}\right]^{2}}{\left[\omega_{t}^{3}\right]^{2 / 3}}=\frac{2}{3^{2 / 3}}\left\{\frac{-A+l(t) B}{A^{2 / 3} l(t)^{2 / 3}}\right\}=\frac{2}{3^{2 / 3}}\left\{\frac{-A^{1 / 3}}{l(t)^{2 / 3}}+\frac{l(t)^{1 / 3} B}{A^{2 / 3}}\right\} .$$

For $a, b<0$ and $x>0$, set $h(x):=\frac{2}{3^{2 / 3}}\left(\frac{a}{x^{2}}+\frac{x}{b}\right)$. Since $h^{\prime}(x)=$ $\frac{2}{3^{2 / 3}}\left(\frac{x^{3}-2 a b}{x^{3} b}\right), h(x)$ has maximum when $x=(2 a b)^{1 / 3}$. So we get $h(x) \leq\left(\frac{6 a}{b^{2}}\right)^{\frac{1}{3}}$. With $a=-A^{1 / 3}, b=\frac{A^{2 / 3}}{B}$ and $x=l(t)^{1 / 3}$, this gives
$$\frac{c_{1}\left[\omega_{t}\right]^{2}}{\left[\omega_{t}^{3}\right]^{2 / 3}} \leq-6^{\frac{1}{3}}\left(\frac{B^{2}}{A}\right)^{\frac{1}{3}},$$
and from (3.5)
$$\frac{B^{2}}{A} \geq \frac{\left\{3 n_{0}(t)+2 \sqrt{2} \sqrt{\sum_{i=1}^{8} n_{i}^{2}(t)}\right\}^{2}}{n_{0}^{2}(t)-\sum_{i=1}^{8} n_{i}^{2}(t)}=\frac{(3-2 \sqrt{2} \sqrt{y})^{2}}{1-y}$$
where $y=\sum_{i=1}^{8} \frac{n_{i}^{2}(t)}{n_{0}^{2}(t)}$. By calculus, $\frac{(3-2 \sqrt{2} \sqrt{y})^{2}}{1-y} \geq 1$ for $y \in[0,1)$ with equality at $y=\frac{8}{9}$.

We have $\frac{c_{1}\left[\omega_{t}\right]^{2}}{\left[\omega_{t}^{3}\right]^{2 / 3}} \leq-6^{\frac{1}{3}}$; the equality is achieved exactly when $n_{0}(t)=-3$, $n_{i}(t)=1, i=1, \cdots, 8$ and $l(t)=2$ modulo scaling, i.e. when $\left[\omega_{t}\right]$ is a positive multiple of $-c_{1}(M)$. The Kähler form of a product Kähler Einstein metric on $M=W \times \Sigma$ belongs to this class.

As the expression $\frac{4 \pi c_{1}(\omega) \cdot \frac{[\omega]^{n-1}}{(n-1)!}}{\left(\frac{[\omega]^{n}}{n!}\right)^{\frac{n-1}{n}}}$ is invariant under a change $\omega \mapsto \phi^{*}(\omega)$ by a diffeomorphism $\phi$, so from (1.1),
$$Z\left(M,\left[\left[\omega_{0}\right]\right]\right) \leq \sup _{\omega \in\left[\left[\omega_{0}\right]\right]} 2 \pi \cdot 6^{2 / 3} \frac{c_{1}[\omega]^{2}}{\left[\omega^{3}\right]^{2 / 3}} \leq-12 \pi .$$
As the equality is attained by a Kähler Einstein metric, $Z\left(M,\left[\left[\omega_{0}\right]\right]\right)=-12 \pi$. \(\square\)

The next corollary yields Theorem 1.1.

Corollary 3.2. There exists a smooth closed 6-d manifold with distinct symplectic deformation equivalence classes $\left[\left[\omega_{1}\right]\right]$ and $\left[\left[\omega_{2}\right]\right]$ such that $Z\left(M,\left[\left[\omega_{1}\right]\right]\right)=$ $\infty$ which is obtained by a sequence of Kähler metrics of positive constant scalar curvature, and $Z\left(M,\left[\left[\omega_{2}\right]\right]\right)<0$.

Proof. Consider $V \times \Sigma$ and $W \times \Sigma$ where $V=R_{8}, W$ and $\Sigma$ are as in Proposition 3.1. They are diffeomorphic but their natural symplectic structures are not deformation equivalent. Let $\omega_{1}$ be the Kähler form of a product Kähler Einstein metric on $V \times \Sigma$. One can easily get $Z\left(M,\left[\left[\omega_{1}\right]\right]\right)=\infty$ by scaling on one factor of the product. Let $\omega_{2}$ be the $\omega_{W}+\omega_{\Sigma}$ in Proposition 3.1 \(\square\)

Remark 3.3. Theorem 1.1 and its proof hint that much more examples may be obtained in a similar way. Just for another instance, considering the example $M=R_{8} \times R_{8}$ of Catanese and LeBrun in [5], we could check that the smooth 8-dimensional manifold $M$ admits distinct symplectic deformation equivalence classes $\left[\left[\omega_{i}\right]\right], i=1,2$ such that $Z\left(M,\left[\left[\omega_{1}\right]\right]\right)=\infty$ and $Z\left(M,\left[\left[\omega_{2}\right]\right]\right)<0$.

\section*{4. Kazdan-Warner method adapted to almost Kähler metrics}

Our method to prove Theorem 1.2 is an adaptation of ordinary scalar curvature theory to an almost-Kähler setting, and recall and modify the material explained in [12, 11].

Let $\mathfrak{M}$ denote the space of Riemannian metrics on a given smooth manifold $M$ of real dimension $2 n$, and we regard $\mathfrak{M}$ as the completion of smooth metrics with respect to $L_{2}^{p}$-norm for $p>2 n$. Given a symplectic form $\omega$ on $M$, let $\Omega_{\omega}$ be the subspace of $\omega$-almost-Kähler metrics on $M$. The space $\Omega_{\omega}$ is a smooth Banach manifold with the above norm, and its tangent space $T_{g} \Omega_{\omega}$ at $g:=\omega(\cdot, J \cdot)$ consists of symmetric $(0,2)$ tensors $h$ which are $J$-antiinvariant, i.e.
$$h^{+}(X, Y):=\frac{1}{2}(h(X, Y)+h(J X, J Y))=0$$
for all $X, Y \in T M$.
The space $\Omega_{\omega}$ admits a natural parametrization by the exponential map; for $g \in \Omega_{\omega}$, define $\mathcal{E}_{g}: T_{g} \Omega_{\omega} \rightarrow \Omega_{\omega}$ by $\mathcal{E}_{g}(h)=g \cdot e^{h}$ with
$$g \cdot e^{h}(X, Y)=g\left(X, e^{\hat{h}}(Y)\right)=g\left(X, Y+\sum_{k=1}^{\infty} \frac{1}{k!} \hat{h}^{k} Y\right),$$
where $X, Y \in T M$, and $\hat{h}$ is the (1,1)-tensor field lifted from $h$ with respect to $g$. Clearly we have
$$\left.\frac{d\left\{g \cdot e^{t h}\right\}}{d t}\right|_{t=0}=h .$$

Given $g \in \Omega_{\omega}$ with corresponding $J$, any other metric $\tilde{g}$ in $\Omega_{\omega}$ can be expressed as
$$\tilde{g}=g \cdot e^{h},$$
where $h$ is a $J$-anti-invariant symmetric (0, 2)-tensor field uniquely determined.

For the scalar curvature functional $S_{\omega}: \Omega_{\omega} \rightarrow L^{p}(M)$, the derivative at $g$ is given by
$$D_{g} S_{\omega}(h)=\delta_{g} \delta_{g}(h)-g\left(r_{g}, h\right)$$
for $h \in T_{g} \Omega_{\omega}$, where $r_{g}$ is the Ricci curvature of $g$, and its formal adjoint is given by
$$\left(D_{g} S_{\omega}\right)^{*}(\psi)=(\nabla d \psi)^{-}-r_{g}^{-} \psi,$$
where $A^{-}$for a symmetric $(0,2)$ tensor $A$ denotes the $J$-anti-invariant part $\frac{1}{2}(A(\cdot, \cdot)-A(J \cdot, J \cdot))$.

The followings are key facts for the Kazdan-Warner type problem in the almost-Kähler setting.

Lemma 4.1. [12], [11, Lemma 1] If $D_{g} S_{\omega}$ is surjective for a smooth $g \in \Omega_{\omega}$, then $S_{\omega}$ is locally surjective at $g$, i.e. there exists an $\epsilon>0$ such that for any $f \in L^{p}(M)$ with $\left\|f-S_{\omega}(g)\right\|<\epsilon$ there is an $L_{2}^{p}$ almost-Kähler metric $\tilde{g} \in \Omega_{\omega}$ satisfying $f=S_{\omega}(\tilde{g})$. Furthermore if $f$ is $C^{\infty}$, so is $\tilde{g}$.

Recall that a diffeomorphism $\phi$ is said to be isotopic to the identity map if there is a homotopy of diffeomorphisms $\phi_{t}, 0 \leq t \leq 1$, such that $\phi_{0}=i d$ and $\phi_{1}=\phi$. The following lemma was proved in [8, Theorem 2.1] without the isotopy clause. Here we add a few arguments in their argument to verify the isotopy part.

Lemma 4.2. Suppose $\operatorname{dim} M \geq 2$ and $f \in C^{0}(M)$. Then an $L^{p}$ function $f_{1}$ on $M$ belongs to the $L^{p}$ closure of
$\{f \circ \phi \mid \phi$ is a diffeomorphism of $M$, isotopic to the identity map $\}$ if and only if $\inf f \leq f_{1} \leq \sup f$ almost everywhere.

Proof. Let $\varepsilon>0$ be given. As $C^{0}(M)$ is dense in $L^{p}(M)$, we may assume $f_{1} \in C^{0}(M)$. We triangulate $M$ into n-simplexes $\Delta_{i}$ so that $M=\cup \Delta_{i}$ and that $\max _{x, y \in \Delta_{i}}\left|f_{1}(x)-f_{1}(y)\right|<\delta$ with $2 \delta=\frac{\varepsilon}{(2 \operatorname{vol} M)^{\frac{1}{p}}}$. Choose $b_{i}$ in the interior of $\Delta_{i}$.

There exist disjoint open balls $V_{i} \subset M$ such that $\left|f(y)-f_{1}\left(b_{i}\right)\right|<\delta$ for $y \in V_{i}$ and for each $i$. One chooses a neighborhood $\Omega$ of the $(n-1)$ - skeleton $M^{(n-1)}$ of $M$, disjoint from the $b_{i}$, so small that
$$\left(\max _{M}|f|+\max _{M}\left|f_{1}\right|\right)^{p} \operatorname{Vol}(\Omega)<\frac{\varepsilon^{p}}{2} .$$

For each $i$, let $U_{i}$ be a small ball neighborhood of $b_{i}$, disjoint from $\Omega$, and choose open sets $O_{1}$ and $O_{2}$, so that
$$M-\Omega \subset O_{1} \subset \overline{O_{1}} \subset O_{2} \subset \overline{O_{2}} \subset M-M^{(n-1)} .$$

There is a homotopy of diffeomorphisms $\phi_{t}, 0 \leq t \leq 1$, such that $\phi_{0}=i d$ and $\phi_{1}\left(U_{i}\right) \subset V_{i}$, for each $i$. And there is a homotopy of diffeomorphisms $\psi_{t}, 0 \leq t \leq 1$, with $\psi_{0}=i d$ such that $\psi_{1}$ satisfies $\psi_{1} \mid M-O_{2}=i d$ and that $\psi_{1}\left(O_{1} \cap \Delta_{i}\right) \subset U_{i}$, for each $i$. Let $\Phi_{t}=\phi_{t} \circ \psi_{t}$. Then, we get
$$\begin{aligned}
\left\|f \circ \Phi_{1}-f_{1}\right\|_{p}^{p} & =\left(\int_{\Omega}+\int_{M-\Omega}\right)\left(\left|f \circ \Phi_{1}-f_{1}\right|^{p} d v o l\right) \\
& <\frac{\varepsilon^{p}}{2}+\sum_{i} \int_{O_{1} \cap \Delta_{i}}\left|f \circ \Phi_{1}(y)-f_{1}\left(b_{i}\right)+f_{1}\left(b_{i}\right)-f_{1}(y)\right|^{p} d v o l \\
& <\frac{\varepsilon^{p}}{2}+\sum_{i} 2^{p} \delta^{p} \operatorname{Vol}\left(\Delta_{i}\right)=\varepsilon^{p} .
\end{aligned}$$
This proves if part, and only if part should be clear. \(\square\)

Proposition 4.3. If $D_{g} S_{\omega}$ is surjective for a smooth $g \in \Omega_{\omega}$, then any smooth function $f$ with $\inf f \leq S_{\omega}(g) \leq \sup f$ is the scalar curvature of a smooth almost-Kähler metric compatible with $\phi^{*} \omega$ for a diffeomorphism $\phi$ of $M$ isotopic to the identity.

Proof. By the above two lemmas, there exists a diffeomorphism $\tilde{\phi}$ isotopic to the identity such that $f \circ \tilde{\phi}=S_{\omega}(\tilde{g})$ for a smooth $\omega$-almost-Kähler metric $\tilde{g}$. Thus $f=S_{\left(\tilde{\phi}^{-1}\right)^{*} \omega}\left(\left(\tilde{\phi}^{-1}\right)^{*} \tilde{g}\right)$. \(\square\)

Lemma 4.4. The principal part of the fourth-order linear partial differential operator $\left(D_{g} S_{\omega}\right) \circ\left(D_{g} S_{\omega}\right)^{*}: C^{\infty}(M) \rightarrow C^{\infty}(M)$ is equal to that of $\frac{1}{2} \Delta_{g} \circ \Delta_{g}$, where $\Delta_{g}$ is the $g$-Laplacian.

Proof. Let $e_{1}, J e_{1}, \cdots, e_{n}, J e_{n}$ be a local orthonormal frame satisfying $J e_{2 i-1}=$ $e_{2 i}$ for $i=1, \cdots, n$. The fourth order differentiation only occurs at $\delta_{g} \delta_{g}(\nabla d \psi)^{-}$.

A direct computation shows that
$$\begin{aligned}
\delta_{g} \delta_{g}(2 \nabla d \psi)^{-}(\psi) & =\sum_{i=1}^{2 n} \sum_{j=1}^{2 n} e_{i}\left(e_{j}\left(\nabla d \psi\left(e_{i}, e_{j}\right)-\nabla d \psi\left(J\left(e_{i}\right), J\left(e_{j}\right)\right)\right)\right)+\text { l.o.t. } \\
& =\sum_{i=1}^{2 n} \sum_{j=1}^{2 n}\left\{e_{i}\left(e_{j}\left(e_{i}\left(e_{j} \psi\right)\right)\right)-e_{i}\left(e_{j}\left(J e_{i}\left(J e_{j} \psi\right)\right)\right)\right\}+\text { l.o.t. } \\
& =\sum_{i=1}^{2 n} \sum_{j=1}^{2 n}\left\{e_{i}\left(e_{i}\left(e_{j}\left(e_{j} \psi\right)\right)\right)-e_{i}\left(J e_{i}\left(e_{j}\left(J e_{j} \psi\right)\right)\right)+\right.\text { l.o.t. } \\
& =\Delta^{2} \psi-\left\{\sum_{i=1}^{n}\left(e_{2 i-1} J e_{2 i-1}+e_{2 i} J e_{2 i}\right)\left(\sum_{j=1}^{2 n} e_{j}\left(J e_{j} \psi\right)\right)\right\}+\text { l.o.t. } \\
& =\Delta_{g}^{2} \psi-\left\{\sum_{i=1}^{n}\left(e_{2 i-1} e_{2 i}-e_{2 i} e_{2 i-1}\right)\left(\sum_{j=1}^{2 n} e_{j}\left(J e_{j} \psi\right)\right)\right\}+\text { l.o.t. } \\
& =\Delta_{g}^{2} \psi+\text { l.o.t., }
\end{aligned}$$
where l.o.t denotes the terms of differentiations up to the 3rd order and $\Delta$ is the Euclidean Laplacian. \(\square\)

\section*{5. Almost-Kähler Surgery and deformation}

Here we consider a left-invariant almost-Kähler metric on the 4-dimensional Kodaira-Thurston nil-manifold [1]. The metric can be written on $\mathbb{R}^{4}=$ $\{(x, y, z, t) \mid x, y, z, t \in \mathbb{R}\}$ as
$$g_{K T}=d x^{2}+d y^{2}+(d z-x d y)^{2}+d t^{2}$$
and the left-invariant symplectic form is $\omega_{K T}=d t \wedge d x+d y \wedge d z$. The almost complex structure $J$ is then given by $J\left(e_{4}\right)=e_{1}, J\left(e_{1}\right)=-e_{4}, J\left(e_{2}\right)=e_{3}$, $J\left(e_{3}\right)=-e_{2}$, where $e_{1}=\frac{\partial}{\partial x}, e_{2}=\frac{\partial}{\partial y}+x \frac{\partial}{\partial z}, e_{3}=\frac{\partial}{\partial z}, e_{4}=\frac{\partial}{\partial t}$ which form an orthonormal frame for the metric.

Now we consider a metric $g_{n}$ on the product manifold $\mathbb{R}^{4} \times \mathbb{R}^{2 n-4}, n \geq 2$ defined by $g_{n}=g_{K T}+g_{E u c}$, where $g_{E u c}$ is the Euclidean metric on $\mathbb{R}^{2 n-4}$. This manifold has the symplectic form $\tilde{\omega}=\omega_{K T}+\omega_{0}$, where $\omega_{0}$ is the standard symplectic structure on $\mathbb{R}^{2 n-4}$ and $g_{n}$ is $\tilde{\omega}$-almost-Kähler .

Given any symplectic manifold $(M, \omega)$ with an almost-Kähler metric $g$ and the corresponding almost complex structure $J_{g}$, we pick a point $p$. There exists a Darboux coordinate neighborhood $\left(U, x_{i}\right)$ of $p$ with $x(p)=0$ so that $\omega=\sum_{i=1}^{n} d x_{2 i-1} \wedge d x_{2 i}$. Assume that $U$ contains a ball $B_{\delta}^{g}(p)$ of $g$-radius $\delta$ with center at $p$. By considering the (coordinates-rearranging) local diffeomorphism $\phi\left(x_{1}, \cdots, x_{2 n}\right)=\left(x_{2}, x_{3}, x_{4}, x_{1}, x_{5} \cdots, x_{2 n}\right), \phi: U \rightarrow$
$\mathbb{R}^{4} \times \mathbb{R}^{2 n-4}$, i.e. identifying $x_{2}=x, x_{3}=y, x_{4}=z, x_{1}=t \cdots$, we can get the pulled-back metric of $g_{n}$ via $\phi$, which we still denote by $g_{n}$. Note that $\phi^{*} \tilde{\omega}=\omega$. We may express $g_{n}=g \cdot e^{h}$ on $U$ for a unique smooth symmetric $J_{g}$-anti-invariant tensor $h$ from (4.6), because $g$ and $g_{n}$ are both $\omega$-almost-kähler. Let $\eta(r)$ be a smooth cutoff function in $C^{\infty}\left(\mathbb{R}^{>0},[0,1]\right)$ s.t. $\eta \equiv 0$ for $r<\frac{\delta}{3}$ and $\eta \equiv 1$ on the set $r \geq \frac{2 \delta}{3}$.

We define a new $\omega$-almost-Kähler metric $h$ on $M$ by
$$h:= \begin{cases}g & \text { on } \quad \mathrm{M} \backslash \mathrm{~B}_{\frac{2 \delta}{3}}^{\mathrm{g}}(\mathrm{p}), \\ g_{n} \cdot e^{\eta\left(r_{g}\right) h} & \text { on } \quad \mathrm{B}_{\frac{2 \delta}{3}}^{\mathrm{g}}(\mathrm{p}) \backslash \mathrm{B}_{\frac{\delta}{3}}^{\mathrm{g}}(\mathrm{p}) \\ g_{n} & \text { on } \quad \mathrm{B}_{\frac{\delta}{3}}^{\mathrm{g}}(\mathrm{p})\end{cases}$$
where $r_{g}$ is the distance function of $g$ from $p$.
In [10], using a Lohkamp type argument [16] adapted to symplectic manifolds, the first author proved on any closed symplectic manifold of dimension $\geq$ 4 the existence of an almost-Kähler metric of negative scalar curvature which equals a prescribed negative scalar-curved metric on an open subset;

Proposition 5.1. [10, Theorem 3] Let $S$ be a closed subset in a smooth closed symplectic manifold $(M, \omega)$ of dimension $2 n \geq 4$, and $U \supset S$ be an open neigborhood. Then for any smooth $\omega$-almost-Kähler metric $g_{0}$ on $U$ with $s\left(g_{0}\right)<0$, there exists a smooth $\omega$-almost-Kähler metric $g$ on $M$ such that $g=g_{0}$ on $S$ and $s(g)<0$ on $M$.

We now apply proposition 5.1 to the metric $h$ of (5.7) with $U=B_{\frac{\delta}{3}}^{g}(p)$ and $S=B_{\frac{\delta}{6}}^{g}(p)$. We get;

Corollary 5.2. On any smooth closed symplectic manifold $(M, \omega)$ of dimension $2 n \geq 4$, there exists a smooth $\omega$-almost-Kähler metric $g$ with negative scalar curvature such that $g$ is isometric to the product metric of $g_{K H}$ and the Euclidean metric on an open subset $B_{\epsilon}$ of $M$.

\section*{6. Proof of Theorem 1.2}

Theorem 6.1. Let $(M, \omega)$ be a smooth closed symplectic manifold of dimension $2 n \geq 4$. Then any smooth function on $M$ which is somewhere negative and somewhere zero is the scalar curvature of some smooth almost-Kähler metric associated to $c \varphi^{*} \omega$, where $c>0$ is a constant and $\varphi$ is a diffeomorphism of $M$, isotopic to the identity.

Proof. On $(M, \omega)$, let's take the $\omega$-almost-Kähler metric $g$ constructed in Corollary 5.2. By Lemma 6.2 below, we have that $D_{g} S_{\omega}$ is surjective. If $f \in$
$C^{\infty}(M)$ is somewhere negative and somewhere zero, then for a sufficiently large constant $c>0$,
$$\inf c f \leq S_{\omega}(g) \leq \sup c f .$$
Then by Proposition 4.3, $c f$ is the scalar curvature of an almost-Kähler metric $G$ compatible with $\phi^{*} \omega$ for some diffeomorphism $\phi$ of $M$ isotopic to the identity, and hence $f$ is the scalar curvature of the almost-Kähler metric $c \cdot G$ compatible with $c \phi^{*} \omega$. \(\square\)

Theorem 1.2 follows from the above theorem 6.1, since $c \phi^{*} \omega$ is deformation equivalent to $\omega$ for any constant $c>0$.

Lemma 6.2. For the metric $g$ constructed in Corollary 5.2, the kernel of $\left(D_{g} S_{\omega}\right)^{*}$ is $\{0\}$.

Proof. We look into the computations in [11, Section 4], where any global solution on Kodaira-Thurston compact manifold was shown to be zero, whereas we shall now improve to show any local solution on it is zero.

Let's first compute the curvature of $g$ on $B_{\epsilon}$. Since it is the product of the Kodaira-Thurston metric and the Euclidean metric, we will only list components for $i=1, \cdots, 4$. (Recall the frame $e_{1}, e_{2}, e_{3}, e_{4}$ in Section 5.) From the formula
$$2\left\langle\nabla_{X} Y, Z\right\rangle=X\langle Y, Z\rangle+Y\langle X, Z\rangle-Z\langle X, Y\rangle-\langle X,[Y, Z]\rangle-\langle Y,[X, Z]\rangle+\langle Z,[X, Y]\rangle,$$
one can compute
$$\begin{gathered}
\nabla_{e_{1}} e_{2}=-\nabla_{e_{2}} e_{1}=\frac{1}{2} e_{3}, \quad \nabla_{e_{1}} e_{3}=\nabla_{e_{3}} e_{1}=-\frac{1}{2} e_{2}, \\
\nabla_{e_{2}} e_{3}=\nabla_{e_{3}} e_{2}=\frac{1}{2} e_{1}, \quad \nabla_{e_{i}} e_{i}=\nabla_{e_{4}} e_{i}=\nabla_{e_{i}} e_{4}=0 .
\end{gathered}$$
Thus letting
$$\nabla e_{i}=\sum_{j} \omega_{i j} e_{j},$$
we have
$$\omega_{i j}=\frac{1}{2}\left(\begin{array}{cccc}
0 & d z-x d y & d y & 0 \\
-d z+x d y & 0 & -d x & 0 \\
-d y & d x & 0 & 0 \\
0 & 0 & 0 & 0
\end{array}\right),$$
and the Cartan structure equation gives
$$\begin{aligned}
\Omega_{i j} & =d \omega_{i j}+\sum_{k} \omega_{i k} \wedge \omega_{k j} \\
& =\frac{1}{4}\left(\begin{array}{cccc}
0 & -3 d x \wedge d y & d x \wedge(d z-x d y) & 0 \\
3 d x \wedge d y & 0 & d y \wedge d z & 0 \\
(d z-x d y) \wedge d x & -d y \wedge d z & 0 & 0 \\
0 & 0 & 0 & 0
\end{array}\right) .
\end{aligned}$$
Denoting the sectional curvature of the plane spanned by $e_{i}$ and $e_{j}$ by $K_{i j}$, we have
$$K_{12}=-\frac{3}{4}, K_{13}=\frac{1}{4}, K_{23}=\frac{1}{4}, K_{i 4}=0$$
for any $i$. Then the Ricci tensor $\left(r_{i j}\right)$ is given by
$$r_{11}=-\frac{1}{2}, r_{22}=-\frac{1}{2}, r_{33}=\frac{1}{2}, r_{44}=0, r_{i j}=0 \text { for } i \neq j$$
so that
$$r_{11}^{-}=-\frac{1}{4}, r_{22}^{-}=-\frac{1}{2}, r_{33}^{-}=\frac{1}{2}, r_{44}^{-}=\frac{1}{4}, r_{i j}^{-}=0 \text { for } i \neq j .$$

Denoting $(\nabla d \psi)\left(e_{i}, e_{j}\right)=e_{i}\left(e_{j} \psi\right)-\left(\nabla_{e_{i}} e_{j}\right) \psi$ for $\psi \in C^{\infty}\left(B_{\epsilon}\right)$ by $\nabla d \psi_{i j}$, one can easily get
$$\begin{array}{rlrl}
\nabla d \psi_{11} & =\psi_{x x}, \nabla d \psi_{22}=\psi_{y y}+2 x \psi_{y z}+x^{2} \psi_{z z}, \nabla d \psi_{33}=\psi_{z z}, & \nabla d \psi_{44}=\psi_{t t}, \\
\nabla d \psi_{12} & =\psi_{x y}+x \psi_{y z}+\frac{1}{2} \psi_{z}, & \nabla d \psi_{13}=\psi_{x z}+\frac{1}{2} \psi_{y}+\frac{x}{2} \psi_{z}, & \nabla d \psi_{14} \\
\nabla d \psi_{23} & =\psi_{x t}, \\
\nabla \psi_{y z}+x \psi_{z z}-\frac{1}{2} \psi_{x}, & \nabla d \psi_{24}=\psi_{y t}+x \psi_{z t}, & \nabla d \psi_{34} & =\psi_{z t} .
\end{array}$$
We list only $\nabla d \psi_{i j}$ for $i, j=1, \cdots, 4$, because that's enough for our purpose.
Also denoting $(\nabla d \psi)^{-}\left(e_{i}, e_{j}\right)=\frac{1}{2}\left(\nabla d \psi\left(e_{i}, e_{j}\right)-\nabla d \psi\left(J e_{i}, J e_{j}\right)\right)$ simply by $\nabla^{-} d \psi_{i j}$, one can get
$$\begin{gathered}
2 \nabla^{-} d \psi_{11}=\psi_{x x}-\psi_{t t}, \quad 2 \nabla^{-} d \psi_{22}=\psi_{y y}+2 x \psi_{y z}+\left(x^{2}-1\right) \psi_{z z}, \\
2 \nabla^{-} d \psi_{12}=\psi_{x y}+x \psi_{x z}+\frac{1}{2} \psi_{z}+\psi_{z t}, 2 \nabla^{-} d \psi_{13}=\psi_{x z}+\frac{1}{2} \psi_{y}+\frac{1}{2} x \psi_{z}-\psi_{y t}-x \psi_{z t}, \\
2 \nabla^{-} d \psi_{23}=2\left(\psi_{y z}+x \psi_{z z}-\frac{1}{2} \psi_{x}\right), \quad 2 \nabla^{-} d \psi_{14}=2 \psi_{x t} .
\end{gathered}$$

Now suppose $\psi \in \operatorname{ker}\left(D_{g} S_{\omega}\right)^{*}$, i.e.
$$\nabla^{-} d \psi-\psi r^{-}=0 .$$
Then from the above, we get the following 6 equations of $\psi$ on $B_{\epsilon}$ :
$$\psi_{x x}-\psi_{t t}=-\frac{1}{2} \psi,$$
$$\begin{gathered}
\psi_{y y}+2 x \psi_{y z}+\left(x^{2}-1\right) \psi_{z z}=-\psi \\
\psi_{x y}+x \psi_{x z}+\frac{1}{2} \psi_{z}+\psi_{z t}=0 \\
\psi_{x z}+\frac{1}{2} \psi_{y}+\frac{1}{2} x \psi_{z}-\psi_{y t}-x \psi_{z t}=0 \\
\psi_{y z}+x \psi_{z z}-\frac{1}{2} \psi_{x}=0 \\
\psi_{x t}=0
\end{gathered}$$

In order to deduce $\psi=0$ on $B_{\epsilon}$ out of these 6 equations, let's write the local coordinate $\left(x, y, z, t, x_{5}, \cdots, x_{2 n}\right)$ on $B_{\epsilon}$ as $(x, y, z, t) \times w$ so that $w=\left(x_{5}, \cdots, x_{2 n}\right)$. We will first show $\psi_{t}=0$ and then $\psi_{x}=0$, which together imply $\psi=0$ by (6.9).

From (6.14), $\psi(x, y, z, t, w)$ can be written as $a(x, y, z, w)+b(y, z, t, w)$. Substituting it into (6.9) gives
$$a_{x x}-b_{t t}=-\frac{1}{2}(a+b) .$$
Then the LHS of $a_{x x}+\frac{1}{2} a=b_{t t}-\frac{1}{2} b$ is a function of $x, y, z, w$, whereas its RHS is a function of $y, z, t, w$. Thus both sides are functions of y,z, and w only. Differentiating the RHS with respect to $t$ gives
$$b_{t t t}-\frac{1}{2} b_{t}=0 .$$
Solving this ODE, we get
$$b_{t}=b_{1}(y, z, w) e^{\frac{t}{\sqrt{2}}}+b_{2}(y, z, w) e^{-\frac{t}{\sqrt{2}}}$$
so that
$$b=\sqrt{2} b_{1}(y, z, w) e^{\frac{t}{\sqrt{2}}}-\sqrt{2} b_{2}(y, z, w) e^{-\frac{t}{\sqrt{2}}}+b_{3}(y, z, w) .$$
Now plugging $a+b$ into (6.11), and picking up only $t$ terms, we get
$$\frac{1}{2}\left(\sqrt{2} \frac{\partial b_{1}}{\partial z} e^{\frac{t}{\sqrt{2}}}-\sqrt{2} \frac{\partial b_{2}}{\partial z} e^{-\frac{t}{\sqrt{2}}}\right)+\frac{\partial b_{1}}{\partial z} e^{\frac{t}{\sqrt{2}}}+\frac{\partial b_{2}}{\partial z} e^{-\frac{t}{\sqrt{2}}}=0$$
so that $\frac{\partial b_{1}}{\partial z}=\frac{\partial b_{2}}{\partial z}=0$, and hence we can conclude that $b_{1}$ and $b_{2}$ are functions of $y$ and $w$ only.

Plugging new $a+b$ into (6.12), and picking up only $t$ terms, we get
$$\frac{1}{2}\left(\sqrt{2} \frac{\partial b_{1}}{\partial y} e^{\frac{t}{\sqrt{2}}}-\sqrt{2} \frac{\partial b_{2}}{\partial y} e^{-\frac{t}{\sqrt{2}}}\right)-\left(\frac{\partial b_{1}}{\partial y} e^{\frac{t}{\sqrt{2}}}+\frac{\partial b_{2}}{\partial y} e^{-\frac{t}{\sqrt{2}}}\right)=0,$$
which implies that $\frac{\partial b_{1}}{\partial y}=\frac{\partial b_{2}}{\partial y}=0$, and hence $b_{1}$ and $b_{2}$ are functions of $w$ only.

Again plugging this new $a+b$ into (6.10), and picking up only $t$ terms, we get
$$0=-\left(\sqrt{2} b_{1} e^{\frac{t}{\sqrt{2}}}-\sqrt{2} b_{2} e^{-\frac{t}{\sqrt{2}}}\right),$$
which finally implies that $b_{1}=b_{2}=0$ and hence $\psi_{t}=0$.
Taking $\frac{\partial}{\partial x}$ to (6.11) produces
$$\psi_{x x y}+x \psi_{x x z}+\frac{3}{2} \psi_{x z}=0 .$$
Applying $\psi_{x x}=-\frac{1}{2} \psi$ from (6.9), this becomes
$$-\frac{1}{2} \psi_{y}-\frac{1}{2} x \psi_{z}+\frac{3}{2} \psi_{x z}=0 .$$
Comparing it with $\psi_{x z}+\frac{1}{2} \psi_{y}+\frac{1}{2} x \psi_{z}=0$ from (6.12) gives
$$\psi_{y}+x \psi_{z}=0$$
so that
$$\psi_{y z}+x \psi_{z z}=0 .$$
Combing it with (6.13), we get desired $\psi_{x}=0$.
Finally we have $\psi=0$ on $B_{\epsilon} . \psi$ is a solution of a linear elliptic equation $\left(D_{g} S_{\omega}\right) \circ\left(D_{g} S_{\omega}\right)^{*} \psi=0$ whose principal part is bi-Laplacian from Lemma 4.4. So we get $\psi=0$ on $M$ by the unique continuation principle for a bi-Laplace type operator ${ }^{1}$, finishing the proof. \(\square\)

Remark 6.3. In our argument, a particular metric $g_{K T}$ on Kodaira-Thurston manifold is used, as it guarantees the surjectivity of the derivative of scalar curvature map at the constructed metric. One may guess, reasonably, that a generic almost Kähler metric satisfies this surjectivity, as in the Riemannian case [4, 4.37]. However, the equation (6.8) is not readily understood. For this matter, the article [6, Theorem 7.4] on local deformation of scalar curvature is interesting; generic (local) surjectivity of scalar curvature was shown by some method. In that argument a crucial part was the existence of one real analytic metric without local KIDs, i.e. with (locally) surjective derivative of scalar curvature functional.

Here we did not try to prove such generic surjectivity. Rather we bypassed it; we found one almost Kähler metric without local KIDs, and then we imbedded it onto any symplectic manifold, obtaining a no-global-KID metric. We hope to address this generic surjectivity issue in near future.

\footnotetext{
${ }^{1}$ For example, one can apply Protter's theorem [20] which states that if a realvalued function $u$ defined in a domain $D \subset \mathbb{R}^{m}$ containing 0 satisfies that $\left|\Delta^{n} u\right| \leq$ $f\left(x, u, D u, \cdots, D^{k} u\right)$ for Lipschitzian $f$ and $k \leq\left[\frac{3 n}{2}\right]$, and $e^{2 r^{-\beta}} u \rightarrow 0$ as $r:=$ $\sqrt{x_{1}^{2}+\cdots+x_{m}^{2}} \rightarrow 0$ for any constant $\beta>0$, then $u$ vanishes identically in $D$.
}

Remark 6.4. For an almost Kähler version of Kazdan-Warner theory, one may try the Hermitian scalar curvature $\frac{1}{2}\left(s+s^{*}\right)$ [2] rather than the usual scalar curvature, where $s^{*}$ is the star scalar curvature. However, although the Hermitian scalar curvature is natural in almost Kähler geometry, Kazdan-Warner theory goes better with usual one. To see this, recall the Blair's formula [7] for $g \in \Omega_{\omega}$ :
$$\int \frac{1}{2}\left(s_{g}+s_{g}^{*}\right) \frac{\omega^{n}}{n!}=4 \pi c_{1}(\omega) \cdot \frac{[\omega]^{n-1}}{(n-1)!} .$$

Since $c_{1}$ of any symplectic structure on the 4-d torus is zero by Taubes' result [24], no negative function can be the Hermitian scalar curvature of an almost Kähler metric on 4-d torus.

\section*{References}
\begin{itemize}
\item[] [1] E. Abbena, An example of an almost Kähler manifold which is not Kählerian, Boll. Un. Mat. Ital. A (6) 3 (1984), 383-392.
\item[] [2] V. Apostolov and T. Drăghici, The curvature and the integrability of Almost Kähler manifolds: A Survey, Fields Inst. Communications Series 35 AMS (2003), 25-53. http://arxiv.org/pdf/math/0302152v1.pdf
\item[] [3] W. Barth, C. Peters, and A. Van de Ven, Compact Complex Surfaces, Springer-Verlag, 1984.
\item[] [4] A. L. Besse, Einstein manifolds, Ergebnisse der Mathematik, 3 Folge Band 10, Springer-Verlag, 1987.
\item[] [5] F. Catanese and C. LeBrun, On the scalar curvature of Einstein manifolds, Math. Research Letters 4, (1997), 843-854
\item[] [6] R. Beig, P. T. Chruściel, and R. Schoen, KIDs are non-generic, Ann. Henri Poincare, 6 (2005), no. 1, 155-194.
\item[] [7] D. Blair, The 'Total Scalar Curvature' as a symplectic invariant, and related results, Proceedings of the 3rd Congress of Geometry (Thessaloniki, 1991), Aristotle Univ. Thessaloniki, 1992, 79-83.
\item[] [8] J.L. Kazdan and F.W. Warner, Existence and conformal deformation of metrics with prescribed gaussian and scalar curvatures, Ann. of Math. (2) 101 (1975), 317-331.
\item[] [9] J.L. Kazdan and F.W. Warner, A direct approach to the determination of Gaussian and scalar curvature functions, Invent. Math. 28 (1975), 227-230.
\item[] [10] J. Kim, Almost Kähler metrics of negative scalar curvature on symplectic manifolds, Math. Z. 262 (2009), 381-388.
\item[] [11] J. Kim, A note on scalar curvature functions of almost-Kähler metrics, J. Korean Soc. Math. Educ. Ser. B : Pure Appl. Math., 20 (2013), 199-206.
\item[] [12] J. Kim and C. Sung, Deformations of almost-Kähler metrics with constant scalar curvature on compact Kähler manifolds, Ann. of Global Anal. and Geom. 22 (2002), 49-73.
\item[] [13] O. Kobayashi, Scalar curvature of a metric with unit volume, Math. Ann. 279 (1987), 253-265.
\item[] [14] C. LeBrun, Kodaira dimension and the Yamabe problem, Comm. Anal. Geom. 7 (1999), 133-156.
\item[] [15] J.M. Lee and T.H. Parker, The Yambe problem, Bull. Amer. Math. Soc. 17 (1987), 37-91.
\end{itemize}
[16] J. Lohkamp, Metrics of negative Ricci curvature, Ann. of Math. (2) 140 (1994), 655-683.
[17] D. McDuff and D. Salamon, Introduction to symplectic topology, Oxford University Press, New York (1998).
[18] H. Ohta and K. Ono, Notes on symplectic 4-manifolds with $b_{2}^{+}=1$, II , International Journal of Mathematics, 07 (1996), 755-770.
[19] J. Petean, The Yamabe invariant of simply connected manifolds, Jour. fur die reine und angew. Math. v. 2000, 523 (2006), 225-231.
[20] M.H. Protter, Unique continuation for elliptic equations, Trans. Amer. Math. Soc. 95 (1960), 81-91.
[21] Y. Ruan, Symplectic topology on algebraic 3 -folds, J. Differential Geom. 39 (1994), 215-227.
[22] D. Salamon, Uniqueness of symplectic structures, Acta Math. Vietnam. 38 (2013), 123-144.
[23] S.R. Simanca and L.D. Stelling, The dynamics of the energy of a Kähler class, Comm. Math. Phys. 255 (2005), 363-389.
[24] C.H. Taubes, The Seiberg-Witten invariants and symplectic forms, Math. Res. Lett. 1 (1994), 809-822.

Dept. of Mathematics, Sogang University, Seoul, Korea
E-mail address: jskim@sogang.ac.kr
Dept. of mathematics education, Korea National University of Education
E-mail address: cysung@knue.ac.kr
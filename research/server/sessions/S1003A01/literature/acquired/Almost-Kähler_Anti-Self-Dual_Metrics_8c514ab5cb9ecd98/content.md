---
retention_scope: session
part: 1
total_parts: 1
---

---
source_file: 1511_07656v1.pdf
converter: mathpix
format: mmd
---

\title{
ALMOST-KÄHLER ANTI-SELF-DUAL METRICS
}

\author{
INYOUNG KIM
}

\begin{abstract}
We show the existence of strictly almost-Kähler anti-self-dual metrics on certain 4-manifolds by deforming scalar-flat Kähler metrics. On the other hand, we prove the non-existence of such metrics on certain other 4-manifolds by means of Seiberg-Witten theory. In the process, we provide a simple new proof of the fact that any almost-Kähler anti-self-dual 4-manifold must have a non-trivial Seiberg-Witten invariant.
\end{abstract}

\section*{1. Introduction}

On a smooth, oriented riemannian 4-manifold, the bundle of 2-forms $\Lambda^{2}$ decomposes as self-dual and anti-self-dual 2-forms
$$\Lambda^{2}=\Lambda^{+} \oplus \Lambda^{-},$$
where $\Lambda^{ \pm}$are (±1)- eigenspaces of the Hodge-star operator. In terms of this decomposition, the riemannian curvature operator $R: \Lambda^{2} \rightarrow \Lambda^{2}$ takes the form,
$$R=\left(\begin{array}{c|c}
W_{+}+\frac{s}{12} & \stackrel{\circ}{r} \\
\hline \stackrel{\circ}{r} & W_{-}+\frac{s}{12}
\end{array}\right) .$$
If $W_{+}=0$, the the riemannian metric is said anti-self-dual (ASD). Anti-self-dual metrics are hard to construct, but most generally, Taubes showed that $M \# n \overline{\mathbb{C P}^{2}}$ admits such a metric for all sufficiently large $n$, where $M$ is any smooth compact, oriented 4-manifold [26].

On the other hand, when a 4-manifold admits an additional structure such as a complex structure or a symplectic structure, it is natural to think of compatible metrics. More precisely, let $(M, \omega)$ be a symplectic 4-manifold. The symplectic form $\omega$ is a closed and nondegenerate 2-form. By this, we mean $d \omega=0$, and for each $x \in M$ and nonzero $v \in T_{x} M$, there exists $w \in T_{x} M$ such that $\omega(v, w) \neq 0$. A smooth fiber-wise linear map $J: T M \rightarrow T M$ on $M$ is called an almost-complex structure when $J$ satisfies $J^{2}=-1$. We say $\omega$ is compatible with $J$ if
$$\omega\left(J v_{1}, J v_{2}\right)=\omega\left(v_{1}, v_{2}\right)$$
for each $x \in M$ and $v_{1}, v_{2} \in T_{x} M$ and $\omega(v, J v)>0$ for all nonzero $v \in T_{x} M$. It is known that the space of almost-complex structures which are compatible with $\omega$ is nonempty and

\footnotetext{
The research of the author was supported in part by SRC-GAIA, the Grant 2011-0030044 from The Ministry of Education, The Republic of Korea.
}
contractible [19]. Given such a compatible $J$, we define the associated metric by
$$g(v, w)=\omega(v, J w) .$$
Then $g$ is a positive symmetric bilinear form and $J$ is compatible with $g$, that is, $g(v, w)=$ $g(J v, J w)$. When such a $g$ is anti-self-dual, we call $g$ an almost-Kähler anti-self-dual metric.

When $J$ is integrable, $(g, \omega, J)$ is said to be a Kähler structure. A Kähler metric on complex surfaces is scalar-flat if and only if it is anti-self-dual [17]. Thus, scalar-flat Kähler metrics provides one of the important examples of ASD metrics.

The main topic of this article is to study an almost-Kähler anti-self-dual metric on a smooth, compact 4-manifold. We call $g$ a strictly almost-Kähler ASD metric when it is not scalar-flat Kähler. We show the existence of strictly almost-Kähler ASD metrics by deforming scalar-flat Kähler metrics. Many examples of scalar-flat Kähler metrics have been constructed by Kim, LeBrun, Pontecorvo [10], [13] and Rollin, Singer [24]. The deformation theory of such metrics has been studied [17]. Fortunately, twistor theory provides a transparent interpretation of deformation of ASD metrics in terms of Kodaira-Spencer theory of deformations of complex structure.

Conversely, we will give a complete classification (up to diffeomorphism) of the smooth, compact oriented 4-manifolds which admit both almost-Kähler anti-self-dual metrics and metrics of positive scalar curvature. The main tool is the Seiberg-Witten invariant. In particular, we show that an almost-Kähler anti-self-dual 4-manifold has a unique solution of the Seiberg-Witten equation for an explicit perturbation form. Taubes already showed that the existence of the solution of the Seiberg-Witten equation for an almost-Kähler metric with large perturbation form [27]. We show that this equation becomes more explicit when we use an almost-Kähler anti-self-dual metric. In particular, we get an explicit bound of the perturbation form. Combining with Liu's theorem [18], we get useful topological information when we also assume $M$ admits a positive scalar curvature metric. In particular, we show that $\mathbb{C P}^{2} \# n \overline{\mathbb{C P}^{2}}$ admits an almost-Kähler anti-self-dual metric if and only if $n \geq 10$. We state our main results below.

Theorem 1. Suppose a smooth, compact 4-manifold $M$ admits an almost Kähler ASD metric. If $M$ also admits a metric of positive scalar curvature, then it is diffeomorphic to one of the following:
\begin{itemize}
\item[-] $\mathbb{C P}^{2} \# n \overline{\mathbb{C P}^{2}}$ for $n \geq 10$;
\item[-] $S^{2} \times \Sigma_{\mathbf{g}}$ and non-trivial $S^{2}$-bundle over $\Sigma_{\mathbf{g}}$, where $\Sigma_{\mathbf{g}}$ is a Riemann surface with genus $\mathbf{g} \geq 2$;
\item[-] $\left(S^{2} \times \Sigma_{\mathrm{g}}\right) \# n \overline{\mathbb{C P}^{2}}$ for $n \geq 1$; or
\item[-] $\left(S^{2} \times T^{2}\right) \# n \overline{\mathbb{C P}^{2}}$ for $n \geq 1$.
\end{itemize}

Conversely, each of the following differentiable manifolds admits an almost-Kähler antiself-dual metric:
\begin{itemize}
\item[-] $\mathbb{C P}^{2} \# n \overline{\mathbb{C P}^{2}}$ for $n \geq 10$;
\item[-] $S^{2} \times \Sigma_{\mathbf{g}}$ and non-trivial $S^{2}$-bundle over $\Sigma_{\mathbf{g}}$, where $\Sigma_{\mathbf{g}}$ is a Riemann surface with genus $\mathbf{g} \geq 2$;
\end{itemize}
\begin{itemize}
\item[-] $\left(S^{2} \times \Sigma_{\mathrm{g}}\right) \# n \overline{\mathbb{C P}^{2}}$ for $n \geq 1$; or
\item[-] $\left(S^{2} \times T^{2}\right) \# n \overline{\mathbb{C P}^{2}}$ for $n \geq 4$.
\end{itemize}

Except $\mathbb{C P}^{2} \# 10 \overline{\mathbb{C P}^{2}}$ and $S^{2} \times \Sigma_{\mathbf{g}}$, each of those admits a strictly almost-Kähler anti-self-dual metric.

Acknowledgement. This article is based on the author's Ph.D. Thesis. The author would like to thank Prof. Claude LeBrun for suggesting the problem, as well as for his constant help and encouragement.

\section*{2. Geometry of almost-Kähler anti-self-dual metrics}

We begin by discussing the basic property of almost-Kähler anti-self-dual metrics. Throughout this section, we assume $M$ is a smooth, compact, oriented 4-manifold.

Lemma 1. Let $(M, g, \omega, J)$ be an almost-Kähler structure. Then $\omega$ is a self-dual harmonic 2-form $\omega$ with $|\omega|=\sqrt{2}$.

Proof. The easiest way to see this is to use an orthonormal basis. Since $J$ is orthogonal with respect to $g$, there exists an orthonormal basis of the form $\left\{e_{1}, e_{2}=J\left(e_{1}\right), e_{3}, e_{4}=J\left(e_{3}\right)\right\}$. Then the corresponding 2-form $\omega$ is
$$e_{1} \wedge e_{2}+e_{3} \wedge e_{e_{2}} .$$
This is self-dual and $|\omega|=\sqrt{2}$. Since $\omega$ is closed and self-dual, we get
$$d^{*} \omega=-* d * \omega=-* d \omega=0,$$
and therefore,
$$\Delta \omega=\left(d d^{*}+d^{*} d\right) \omega=0 .$$ \(\square\)

Lemma 2. The scalar curvature of almost-Kähler anti-self-dual metric is nonpositive. Moreover, the scalar curvature is identically zero if and only if the metric is Kähler.

Proof. On an oriented, smooth, compact riemannian 4-manifold, there is well-known Weitzenböck formula [3] for self-dual 2-forms
$$\Delta \omega=\nabla^{*} \nabla \omega-2 W_{+}(\omega, \cdot)+\frac{s}{3} \omega .$$

If we take an inner product with $\omega$ in (2), we get
$$<\Delta \omega, \omega>=<\nabla^{*} \nabla \omega, \omega>-2 W_{+}(\omega, \omega)+\frac{s}{3}|\omega|^{2} .$$
If $g$ is an almost-Kähler, then the corresponding symplectic 2-form $\omega$ is harmonic and $|\omega|=\sqrt{2}$. Thus, we get
$$\begin{gathered}
0=\frac{1}{2} \Delta|\omega|^{2}+|\nabla \omega|^{2}-2 W_{+}(\omega, \omega)+\frac{s}{3}|\omega|^{2} \\
0=|\nabla \omega|^{2}-2 W_{+}(\omega, \omega)+\frac{2 s}{3}
\end{gathered}$$

Since $g$ is anti-self-dual, we get
$$0=|\nabla \omega|^{2}+\frac{2 s}{3} .$$ \(\square\)

Note that an anti-self-dual metric is real analytic in suitable coordinates. Thus, $\nabla \omega$ is also real analytic and therefore, it does not vanish on an open set. Moreover, it can only vanishes on the union of real analytic subvarieties. Thus, if $g$ is a strictly almost-Kähler anti-self-dual metric, then $s \neq 0$ on an open dense subset.

When there is an almost-complex structure $J$ on $M$, the complexified tangent vector bundle decomposes as
$$T M \otimes \mathbb{C}=T^{1,0} \oplus T^{0,1},$$
where
$$\begin{aligned}
T^{1,0} & =\left\{Z=X-i J(X) \in T^{\mathbb{C}} \mid X \in T M\right\} \\
T^{0,1} & =\left\{Z=X+i J(X) \in T^{\mathbb{C}} \mid X \in T M\right\} .
\end{aligned}$$

When we evaluate 2-forms on complexified vectors, we extend it complex linearly on both factors. Accordingly, we define extended metric on $T^{\mathbb{C}}$ by
$$\begin{aligned}
g_{\mathbb{C}}(i X, Y) & =i g_{\mathbb{C}}(X, Y) \\
g_{\mathbb{C}}(X, i Y) & =i g_{\mathbb{C}}(X, Y),
\end{aligned}$$
where $X, Y \in T M$. In this convention, we have
$$g_{\mathbb{C}}\left(T^{1,0}, T^{1,0}\right)=0 .$$
Recall $\omega$ is related to $g$ by $\omega(X, Y)=g(J X, Y)$. This can be extended complex bilinearly on both factors and therefore, we can think of $\omega$ as an element of $\Lambda_{\mathbb{C}}^{2}$. Then $\omega$ associated with metric $g_{\mathbb{C}}$ is an element of $\Lambda^{1,1}$.

Following the outline given in [25], we show that when $d \omega=0$, the zero set of Nijenhuis tensor $N$ is equal to the zero set of $\nabla \omega$.

Proposition 1. Let $(M, g, J, \omega)$ be an almost-Kähler structure. Then the zero set of the Nijenhuis tensor $N$ is equal to the zero set of $\nabla \omega$.

Proof. We can check that
$$\left(\nabla_{X} \omega\right)(Y, Z)=2 i g\left(\nabla_{X} Y, Z\right),$$
for $Y, Z \in T^{1,0}$ and $X \in T^{\mathbb{C}}$. And for $Y, Z \in T^{0,1}$, we have
$$\left(\nabla_{X} \omega\right)(Y, Z)=-2 i g\left(\nabla_{X} Y, Z\right) .$$
Using this fact and the torsion-free property of the Levi-Civita connection, we have
$$\begin{aligned}
& g([X, Y], Z)=g\left(\nabla_{X} Y, Z\right)-g\left(\nabla_{Y} X, Z\right) \\
& =-\frac{1}{2 i}\left(\nabla_{X} \omega\right)(Y, Z)+\frac{1}{2 i}\left(\nabla_{Y} \omega\right)(X, Z)
\end{aligned}$$
for $X, Y, Z \in T^{0,1}$. If the Nijenhuis tensor vanishes, then $[X, Y] \in T^{0,1}$ and therefore, we have $g([X, Y], Z)=0$. Thus, we get
$$\left(\nabla_{X} \omega\right)(Y, Z)-\left(\nabla_{Y} \omega\right)(X, Z)=0$$
On the other hand, by definition we have
$$d \omega(X, Y, Z)=\left(\nabla_{X} \omega\right)(Y, Z)-\left(\nabla_{Y} \omega\right)(X, Z)+\left(\nabla_{Z} \omega\right)(X, Y) .$$
Thus, if $d \omega=0$ and $N$ vanishes, then
$$\left(\nabla_{Z} \omega\right)(X, Y)=0$$
for $X, Y, Z \in T^{0,1}$. Also we have $\left(\nabla_{X} \omega\right)(Y, Z)=0$ and $\left(\nabla_{Y} \omega\right)(X, Z)=0$ for $X, Y \in T^{0,1}$ and $Z \in T^{1,0}$. Then from $d \omega=0$, we get
$$\left(\nabla_{Z} \omega\right)(X, Y)=0,$$
for $X, Y \in T^{0,1}$ and $Z \in T^{1,0}$. Combining these two, we get $\left(\nabla_{Z} \omega\right)(X, Y)=0$ for $Z \in T^{\mathbb{C}}$ and $X, Y \in T^{0,1}$.

When $N=0$, we also have $\left[T^{1,0}, T^{1,0}\right] \in T^{1,0}$ and therefore $g([X, Y], Z)=0$ holds for $X, Y, Z \in T^{1,0}$. In the same way, we can show $\left(\nabla_{Z} \omega\right)(X, Y)=0$ for $Z \in T^{\mathbb{C}}$ and $X, Y \in T^{1,0}$. Since $\left(\nabla_{X} \omega\right)(Y, Z)=0$ for $X \in T^{\mathbb{C}}$ and $Y \in T^{1,0}, Z \in T^{0,1}$, we can conclude when $d \omega=0$ holds, the zero set of $N$ is equal to the zero set of $\nabla \omega$. \(\square\)

Armstrong found certain topological obstruction when the Nijenhuis tensor is nowhere vanishing [1].

Theorem 2. (Armstrong) Let $(M, J)$ be a compact smooth 4-manifold with an almost-complex structure $J$. If the Nijenhuis tensor $N$ is nowhere vanishing, then $5 \chi+6 \tau=0$.

Corollary 1. Suppose $M$ admits an almost-Kähler ASD metric $g$. If $5 \chi+6 \tau \neq 0$, then the scalar curvature $s$ vanishes somewhere.

Proof. By Armstrong's theorem, the Nijenhuis tensor should vanish somewhere. Since $d \omega=0, \nabla \omega=0$ vanish somewhere by Proposition 1. Since the zero set of the scalar curvature is equal to the zero set of $\nabla \omega, s$ vanish somewhere and if $g$ is not Kähler, $s$ is negative somewhere. \(\square\)

Example 1. In the next section, we show that the following examples admit almost-Kähler anti-self-dual metrics for certain values $n$.
1) $\mathbb{C P}^{2} \# n \overline{\mathbb{C P}^{2}}$.

In this case, $\chi=3+n$ and $\tau=1-n$. Using this, we have
$$5 \chi+6 \tau=5(3+n)+6(1-n)=21-n$$
Thus, except $n=21$, the scalar curvature of an almost-Kähler ASD metric should vanish somewhere.
2) $S^{2} \times T^{2} \# n \overline{\mathbb{C P}^{2}}$.

In this case, we have $\chi=n$ and $\tau=-n$. Thus, we have
$$5 \chi+6 \tau=5 n-6 n=-n$$

Thus, for $n \geq 1$, the scalar curvature should vanish somewhere.
3) $S^{2} \times \Sigma_{\mathbf{g}} \# n \overline{\mathbb{C P}^{2}}$.

In this case, we have $\chi=-4(\mathbf{g}-1)+n$ and $\tau=-n$. Thus, we have
$$5 \chi+6 \tau=-20 \mathbf{g}+5 n+20-6 n=-20 \mathbf{g}-n+20$$
Thus $5 \chi+6 \tau$ is always negative for $n \geq 0$ and $\mathbf{g} \geq 2$.
Suppose a smooth 4-manifold $M$ admits an almost-complex structure $J$ and a compatible metric $g$. Then the complex-valued 2-forms decompose as
$$\Lambda^{2} T_{\mathbb{C}}^{*}=\left(\Lambda^{2.0} \oplus \Lambda^{0,2}\right) \oplus \Lambda^{1,1} .$$
On the other hand, on an oriented, smooth 4-manifold, we have the following decomposition
$$\Lambda^{2} T_{\mathbb{C}}^{*}=\Lambda_{\mathbb{C}}^{+} \oplus \Lambda_{\mathbb{C}}^{-} .$$
As before, we define an associated 2-form $\omega$ by $\omega(v, w)=g(J v, w)$. When it is not required $d \omega=0,(M, g, \omega, J)$ is called an almost-Hermitian manifold. In this case, two decompositions are compatible in the following way.

Lemma 3. Let $(M, g, \omega, J)$ be an almost-Hermitian 4-manifold. Then we have
$$\begin{gathered}
\Lambda_{\mathbb{C}}^{+}=\mathbb{C} \omega \oplus \Lambda^{2.0} \oplus \Lambda^{0,2}, \\
\Lambda_{\mathbb{C}}^{-}=\Lambda_{0}^{1,1},
\end{gathered}$$
where $\Lambda_{0}^{1,1}$ is the orthogonal complement of $\omega$ in the space of $\Lambda^{1,1}$.

\section*{3. Deformation of scalar-flat Kähler metrics}

In this section, we show the existence of strictly almost-Kähler anti-self-dual metrics by deforming the scalar-flat Káhler metrics. Many examples of scalar-flat Kähler metrics are known [10], [13], [24] and their deformation theory has been studied [17]. Deformation theory of ASD metrics has been known in a purely differential geometric point of a view on a smooth, compact, oriented 4-manifold $M$ using the Atiyah-Singer Index theorem. We study them together at the twistor level using short exact sequences of sheaves. This part mainly depends on [17]. The important well-known result in this context is the following [17].

Proposition 2. Let $g$ be a Kähler metric on a complex surface. Then $g$ is anti-self-dual if and only if its scalar curvature $s=0$.

Let us consider the geometry of scalar-flat Kähler metrics briefly. This will be useful later when they are compared with almost-Kähler ASD metrics. We define the Ricci form $\rho$ by
$$\rho(X, Y)=\operatorname{Ric}(J X, Y) .$$
Then $\rho$ is a closed, real $(1,1)$ form. The important theorem on a Kähler manifold is that the first Chern class of the manifold is represented by $\frac{1}{2 \pi} \rho$
$$c_{1}(M):=c_{1}\left(K^{-1}\right)=\left[\frac{\rho}{2 \pi}\right] .$$

By Lemma 3, we can decompose a $(1,1)$ form $\varphi$, by $\varphi=\frac{1}{2}(\Lambda \varphi) \omega+\varphi_{0}$, where $\Lambda \varphi=\langle\varphi, \omega\rangle$ and $\varphi_{0} \in \wedge_{0}^{1,1}$. From this, we can write the Ricci from $\rho$ as $\rho=\frac{1}{4} s \omega+\rho_{0}$. Using the fact $[\rho]=2 \pi c_{1}$ and $d \mu=\frac{[\omega]^{2}}{2}$, we get
$$2 \pi c_{1} \cdot[\omega]=[\rho] \cdot[\omega]=\frac{1}{4}[s \omega] \cdot[\omega]=\int_{M} \frac{1}{2} s d \mu .$$

Proposition 3. Let $(M, \omega, g)$ be a Kähler surface with the scalar curvature $s$. Then the following identity holds,
$$\int_{M} s d \mu=4 \pi c_{1} \cdot[\omega] .$$

The theorem below tells us which complex surfaces can admit a scalar-flat Kähler metric.
Theorem 3. (Yau) [28], [17] Let $(M, J)$ be a complex surface which admits a Kahler metric $\omega$ such that $c_{1} \cdot[\omega]=0$. If $c_{1} \neq 0$, that is, if $M$ is not covered by a complex torus or K3 surface, then $M$ is a ruled surface.

Remark 1. For a scalar-flat Kähler metric, we have $c_{1} \cdot[\omega]=0$ by Proposition 3. Therefore, by Yau's theorem, a scalar-flat Kähler surface is either covered by K3 or $T^{4}$ or it is a ruled surface. Suppose $c_{1} \neq 0$. Since $\omega$ is a self-dual harmonic 2-form, we can conclude $c_{1}$ belongs to $H^{-}$. Thus, $c_{1}^{2}<0$. Let us consider $\mathbb{C P}^{2} \# n \overline{\mathbb{C P}^{2}}$. Then we have $\chi=3+n$ and $\tau=1-n$. Thus, we have
$$c_{1}^{2}=2 \chi+3 \tau=2(3+n)+3(1-n)=9-n .$$
Thus, $\mathbb{C P}^{2} \# n \overline{\mathbb{C P}^{2}}$ with $n \leq 9$ does not admit scalar-flat Kähler metrics.
For the existence part, LeBrun constructed explicit scalar-flat Kähler metrics on a ruled surface and its blown up, $S^{2} \times \Sigma_{\mathbf{g}} \# n \overline{\mathbb{C P}^{2}}$ for $n \geq 2$ and $\mathbf{g} \geq 2$ [13] and Kim, Pontercorvo extended this result for $n \geq 1$ [11]. Kim, LeBrun and Pontecorvo constructed scalar-flat Kähler metrics on $\mathbb{C P}^{2} \# 14 \overline{\mathbb{C P}^{2}}$ and $S^{2} \times T^{2} \# n \overline{\mathbb{C P}^{2}}$ for $n=6$ [10] using the result of Donaldson-Friedman [6]. And Rollin and Singer improved this result on $\mathbb{C P}^{2} \# 10 \overline{\mathbb{C P}^{2}}$ and $S^{2} \times T^{2} \# n \overline{\mathbb{C P}^{2}}$ for $n=4$ [24]. Note that from the above remark 1, 10 is the minimum number for which scalar-flat Kähler metrics can exist on $\mathbb{C P}^{2} \# n \overline{\mathbb{C P}^{2}}$. Also Kim, Pontercorvo proved one-point blow up of a non-minimal scalar-flat Kähler surface also admits a scalar-flat Kähler metric [11]. Therefore, we get the following.

Theorem 4. [10], [11], [24] Let $M$ be diffeomorphic to one of $\mathbb{C P}^{2} \# n \overline{\mathbb{C P}^{2}}$ for $n \geq 10$. Then $M$ admits a scalar-flat Kähler metric.

We study deformation theory of a scalar-flat Kähler metric. We deform this metric in two different categories, namely in scalar-flat Kähler metrics and ASD metrics. The obstruction for a deformation as ASD metrics lies in
$$\mathrm{CokerDW}_{+} \cong H^{2}\left(Z, \Theta_{Z}\right),$$
where $Z$ is the twistor space of $M$. For a scalar-flat Kähler metric, Pontecorvo's result [23] gives us an additional structure on the twistor space. Before stating this result, we explain about the twistor space briefly.

An oriented, 4-dimensional riemannian manifold $M$ with an ASD metric has its companion complex 3-dimensional manifold $Z$. This $Z$ is the total space of the sphere bundle of the vector bundle of self-dual 2-forms on $M$ and so we have a bundle map $\pi: Z \rightarrow M$. The Levi-Civita connection on $M$ induces the connection on $T Z$. Using this connection, we can split $T Z \cong \mathcal{H} \oplus \mathcal{V}$, where $\mathcal{H}$ is the horizontal part which is isomorphic to $\pi^{*}(T M)$ and $\mathcal{V}$ is the vertical part. Since fibers are 2-spheres, $\mathcal{V}$ has a natural almost-complex structure. Given a metric $g$ on $M$, self-dual 2-forms and $g$-orthogonal almost-complex structures on $T_{x} M$ correspond via the map $\omega(v, w)=g(J v, w)$. Thus, we can think of the fiber over $x$ as the set of all linear maps $J_{x}: T M_{x} \rightarrow T M_{x}$ such that $J_{x}^{2}=-1$. Suppose $z \in Z$ and $\pi(z)=x$. Then $\mathcal{H}_{z}=\pi^{*}\left(T M_{x}\right)$ and since $z$ itself represent a $J_{x}$ in $T M_{x}$, we can assign this $J_{x}$ on $\mathcal{H}_{z}$. Thus, $T Z$ admits an almost-complex structure. The remarkable fact is that when $g$ is ASD, this almost-complex structure on $Z$ is integrable and therefore, the twistor space $Z$ becomes a complex manifold [2]. In addition to this, there is a fiberwise antipodal map
$$\omega \rightarrow-\omega$$
and this gives us a fixed-point free anti-holomorphic involution $\sigma$ on the total space $Z$.
Suppose $M$ admits a scalar-flat Kähler metric $g$. In this case, we have the following Pontecorvo's result [23]. An almost-complex structure $J$ and its conjugate $-J$ give us embeddings of $M$ into $Z$ as complex hypersurfaces and we denote them by $\Sigma$ and $\bar{\Sigma}$ and their sum by $D=\Sigma+\bar{\Sigma}$. Then the anti-holomorphic involution $\sigma$ interchanges $\Sigma$ and $\bar{\Sigma}$ and so we have
$$\sigma(\Sigma+\bar{\Sigma})=\bar{\Sigma}+\Sigma .$$
Thus, we get a real bundle $D=[\Sigma+\bar{\Sigma}]$. Then the result in [23] gives
$$[D] \cong K_{Z}^{-\frac{1}{2}} .$$
Conversely, let $Z \rightarrow M$ be a twistor fibration and suppose we have a complex hypersurface $\Sigma \subset Z$ which meets every fiber at one point. Then $\Sigma$ is diffeomorphic to $M$ and we can think of $M$ as a complex surface induced from $\Sigma$. Suppose $[D] \cong K_{Z}^{-\frac{1}{2}}$, where $D=\Sigma+\Sigma$. Then there is a metric $g$ in the conformal class $[g]$ such that $(M, g, J)$ is scalar-flat Kähler.

Using this result, we have the following, which is originally discovered by Boyer [5] in a different way.

Theorem 5. [5], [23] Let $M$ be an oriented, compact, smooth 4-manifold with an ASD metric $g$ and assume the first Betti number $b_{1}(M)$ is even. Suppose there is a complex structure $J$ such that $g(v, w)=g(J v, J w)$. Then the conformal class of $g$ contains a unique scalar-flat Kähler metric.

From this theorem, we can conclude that deforming scalar-flat Kähler metrics is equivalent to deforming ASD hermitian conformal structures. The latter correspond to the deformation of the pair $(Z, D)$ preserving the real structure. Therefore, when obstruction
vanishes, the moduli space of the ASD hermitian conformal structures is the real slice of $H^{1}\left(Z, \Theta_{Z, D}\right)$. Details can be found in [17]. From Theorem 5, we can conclude the following.

Lemma 4. When obstruction vanishes, the deformation of scalar-flat Kähler metrics corresponds to the real slice of $H^{1}\left(Z, \Theta_{Z, D}\right)$, where $\Theta_{Z, D}$ is the sheaf of holomorphic vector fields on $Z$ which are tangent to $D$. And its obstruction lies in $H^{2}\left(Z, \Theta_{Z, D}\right)$.

Remark 2. Note that deformation of scalar-flat Kähler metrics with a fixed complex structure corresponds to the sheaf $\Theta_{Z} \otimes \mathcal{I}_{D}$.

Here we denote the ideal sheaf of $D$ by $\mathcal{I}_{D}$. LeBrun and Singer identifies $H^{i}\left(Z, \Theta \otimes \mathcal{I}_{D}\right)$ using the Penrose transform [17]. In particular, if there is no holomorphic vector field or the complex surface is non-minimal, it is shown that the obstruction vanishes [10], [17]. Below is the result by LeBrun and Singer [17].

Proposition 4. [17] Let $(M, \omega)$ be a compact scalar-flat Kähler surface and let $Z$ be its twistor space. Suppose $c_{1} \neq 0$. If $H^{2}\left(Z, \Theta \otimes \mathcal{I}_{D}\right)=0$, then $H^{2}\left(Z, \Theta_{Z, D}\right)=H^{2}\left(Z, \Theta_{Z}\right)=0$.

This proposition is proved by considering the following short exact sequences of sheaves and showing that $H^{2}\left(D, \Theta_{D}\right)=0$ and $H^{2}\left(D, N_{D}\right)=0$.
$$\begin{gathered}
0 \longrightarrow \Theta_{Z, D} \longrightarrow \Theta_{Z} \longrightarrow N_{D} \longrightarrow 0, \\
0 \longrightarrow \Theta_{Z} \otimes \mathcal{I}_{D} \longrightarrow \Theta_{Z, D} \longrightarrow \Theta_{D} \longrightarrow 0 .
\end{gathered}$$
From (6), we get the following long exact sequence,
$$\cdots \longrightarrow H^{2}\left(Z, \Theta_{Z} \otimes \mathcal{I}_{D}\right) \longrightarrow H^{2}\left(Z, \Theta_{Z, D}\right) \longrightarrow H^{2}\left(D, \Theta_{D}\right) \longrightarrow \cdots$$
Thus, if $H^{2}\left(Z, \Theta_{Z} \otimes \mathcal{I}_{D}\right)=0$, then
$$H^{2}\left(Z, \Theta_{Z, D}\right)=0 .$$
Similarly, from (5), we get
$$\cdots \longrightarrow H^{2}\left(Z, \Theta_{Z, D}\right) \longrightarrow H^{2}\left(Z, \Theta_{Z}\right) \longrightarrow H^{2}\left(D, N_{D}\right) \longrightarrow \cdots$$
Thus, when $H^{2}\left(Z, \Theta_{Z, D}\right)=0$, we have $H^{2}\left(Z, \Theta_{Z}\right)=0$.
Thus, when $H^{2}\left(Z, \Theta \otimes \mathcal{I}_{D}\right)=0$, obstructions of deformation of scalar-flat Kähler metrics and ASD metrics vanish. In particular, if there is no holomorphic vector field, then $H^{2}\left(Z, \Theta_{Z} \otimes \mathcal{I}_{D}\right)=0$ by [17]. When $M$ is a scalar-flat Kähler surface but not Ricci-flat, it is shown in [23]
$$H^{0}\left(M, \Theta_{M}\right)=H^{0}\left(Z, \Theta_{Z}\right) .$$
Thus, when there is no holomorphic vector field on $M$, there is no holomorphic vector field on $Z$. In particular, $H^{0}\left(Z, \Theta_{Z}\right)=H^{0}\left(Z, \Theta_{Z, D}\right)=0$. Therefore, under this assumption, we get a smooth moduli space of scalar flat Kähler metrics and ASD metrics and their dimensions can be calculated by the index theorem.

Theorem 6. Let $(M, g, J, \omega)$ be a complex surface with a scalar-flat Kähler metric. Suppose $c_{1} \neq 0$ and assume $(M, J)$ admits no holomorphic vector fields. Then on these surfaces, we have $-9 \chi \geq 13 \tau$ and if the inequality is strict, there exist deformations which are strictly almost-Kähler.

Proof. Consider the short exact sequence (6). Since $D \cong \Sigma+\bar{\Sigma}$, we have
$$\chi\left(Z, \Theta_{Z, D}\right)=\chi\left(Z, \Theta_{Z} \otimes \mathcal{I}_{D}\right)+2 \chi\left(M, \Theta_{M}\right) .$$
When obstruction vanishes, we can think of $-\chi$ as the dimension of the moduli space. It is shown in [17] that
$$\chi\left(Z, \Theta_{Z} \otimes I_{D}\right)=\tau .$$
Thus, the dimension the moduli space of scalar-flat Kähler metrics is given by
$$-\chi\left(Z, \Theta_{Z, D}\right)=-\tau-2 \chi\left(M, \Theta_{M}\right) .$$
By the index theorem, $\chi\left(M, \Theta_{M}\right)$ is given by
$$\begin{gathered}
\chi\left(M, \Theta_{M}\right)=\int_{M}\left(1+\frac{c_{1}}{2}+\frac{c_{1}^{2}+c_{2}}{12}\right)\left(2+c_{1}+\frac{c_{1}^{2}-2 c_{2}}{2}\right) \\
=\left(\frac{c_{1}^{2}+c_{2}}{6}+\frac{c_{1}^{2}}{2}+\frac{c_{1}^{2}}{2}-c_{2}\right)(M)=\left(\frac{7}{6} c_{1}^{2}-\frac{5}{6} c_{2}\right)(M) \\
=\frac{7(2 \chi+3 \tau)-5 \chi}{6}=\frac{9 \chi+21 \tau}{6}=\frac{3 \chi}{2}+\frac{7 \tau}{2} .
\end{gathered}$$
Therefore, the expected dimension of the moduli space of scalar-flat Kähler metrics is
$$-\chi\left(Z, \Theta_{Z, D}\right)=-\tau-2 \chi\left(M, \Theta_{M}\right)=-\tau-(3 \chi+7 \tau)=-3 \chi-8 \tau .$$

Consider another short exact sequence (5). By Pontecorvo's result [23], we have $N_{D}=$ $K_{D}^{-1}$. From this, we get
$$\chi\left(Z, \Theta_{Z}\right)=\chi\left(Z, \Theta_{Z, D}\right)+2 \chi\left(M, K_{M}^{-1}\right) .$$
$\chi\left(M, K_{M}^{-1}\right)$ is given by the Riemann-Roch formula,
$$\chi(L)=\chi\left(\mathcal{O}_{M}\right)+\int_{M} \frac{c_{1}(L)\left(c_{1}(L)+c_{1}\left(K^{-1}\right)\right)}{2},$$
where $L$ is any holomorphic line bundle on $M$. If $L=K^{-1}$, we get
$$\chi\left(K^{-1}\right)=\chi\left(\mathcal{O}_{M}\right)+c_{1}\left(K^{-1}\right) \cdot c_{1}\left(K^{-1}\right)=\chi\left(\mathcal{O}_{M}\right)+c_{1}^{2}(M) .$$
Since $\chi\left(\mathcal{O}_{M}\right)=\frac{c_{1}^{2}+c_{2}}{12}$, we have
$$\chi\left(K^{-1}\right)=\frac{c_{1}^{2}+c_{2}}{12}+c_{1}^{2} .$$
Using $c_{1}^{2}(M)=2 \chi+3 \tau$ and $c_{2}(M)=\chi$, we get
$$\chi\left(M, K_{M}^{-1}\right)=\frac{2 \chi+3 \tau+\chi}{12}+2 \chi+3 \tau$$
$$=\frac{1}{4} \chi+\frac{1}{4} \tau+2 \chi+3 \tau .$$
Then we have
$$\begin{gathered}
\chi\left(Z, \Theta_{Z}\right)=\chi\left(Z, \Theta_{Z, D}\right)+2 \chi\left(M, K_{M}^{-1}\right) \\
=3 \chi+8 \tau+\frac{1}{2} \chi+\frac{1}{2} \tau+4 \chi+6 \tau \\
=\frac{1}{2}(15 \chi+29 \tau) .
\end{gathered}$$
Thus, when obstruction vanishes, we can conclude the dimension of the moduli space of ASD metrics is given by
$$-\frac{1}{2}(15 \chi+29 \tau) .$$
Using Lemma 5 below, if
$$-\frac{1}{2}(15 \chi+29 \tau)>-(3 \chi+8 \tau),$$
that is, if $-9 \chi>13 \tau$, then there exist strictly almost-Kähler anti-self-dual metrics. In the examples below, we can easily check all scalar-flat Kähler surfaces with $c_{1} \neq 0$ satisfy $-9 \chi \geq 13 \tau$. \(\square\)

Remark 3. The dimension of the moduli of ASD metrics, $-\frac{1}{2}(15 \chi+29 \tau)$, is given first by I. M. Singer using the Atiyah-Singer Index theorem [8]. Also the dimension of the moduli of scalar-flat Kähler metrics, $-(3 \chi+8 \tau)$, has been known to experts, for example in another version of [11], but it seems it has not been written down in detail.

In the following lemma, we show that there is a unique almost-Kähler ASD metric in each conformal class which is close to the one containing a scalar-flat Kähler metric.

Lemma 5. Let $M$ be a compact, smooth 4-dimensional manifold which admits a scalar-flat Kähler metric. Assume $M$ does not admit a holomorphic vector field. Suppose $g^{\prime}$ be a small deformation of $g$. Then there is a unique almost-Kähler anti-self-dual metric in the conformal class of $\left[g^{\prime}\right]$.

Proof. Since $g^{\prime}$ is close to the Kähler metric, there is a self-dual harmonic 2-form $\omega_{g}^{\prime}$ is nondegenerate. Then by conformal rescaling, we can find a metric $\tilde{g}$ in the conformal class of $g^{\prime}$ such that $\left|\omega_{\tilde{g}}\right|=\sqrt{2}$. Then in terms of an orthonormal basis $\left\{e_{1}, e_{2}, e_{3}, e_{4}\right\}$, $\omega_{\tilde{g}}=e_{1} \wedge e_{2}+e_{3} \wedge e_{4}$. Define $J e_{1}=e_{2}, J e_{2}=-e_{1}, J e_{3}=e_{4}, J e_{4}=-e_{3}$. Then, $\omega(X, Y)=$ $\tilde{g}(J X, Y)$ and $J$ is $\omega$ and $\tilde{g}$-compatible. \(\square\)

Example 2. Let us consider $\mathbb{C P}^{2} \# n \overline{\mathbb{C P}^{2}}$. When there is no holomorphic vector field, the dimension the moduli space of scalar-flat Kähler metrics is given by
$$\begin{aligned}
& -3 \chi-8 \tau=-3(3+n)+8(n-1) \\
& =-9-3 n+8 n-8=-17+5 n .
\end{aligned}$$

On the other hand, the dimension of the moduli space of ASD metrics is given by
$$\begin{aligned}
& -\frac{(15 \chi+29 \tau)}{2}=-\frac{(15(3+n)+29(1-n))}{2} \\
& \quad=-\frac{(45+15 n+29-29 n)}{2}=7 n-37 .
\end{aligned}$$
Therefore, we have
$$7 n-37-(-17+5 n) \geq 0 \Longleftrightarrow n \geq 10$$
and equality holds if and only if $n=10$. This observation with Lemma 5 tells us that for $\mathbb{C P}^{2} \# n \overline{\mathbb{C P}^{2}}$, the dimension of the moduli space of almost-Kähler ASD metrics is greater than or equal to the dimension of the moduli of scalar-flat Kähler metrics if and only if $n \geq 10$ and they are equal when $n=10$. Thus, when $n>10$, there exists a strictly almost-Kähler ASD metric.
Example 3. Let us consider $S^{2} \times T^{2} \# n \overline{\mathbb{C P}^{2}}$. Using the fact that $\chi\left(S^{2} \times T^{2}\right)=\chi\left(S^{2}\right) \chi\left(T^{2}\right)=$ 0 and $\chi\left(\mathbb{C P}^{2}\right)=3$, we get
$$\chi\left(S^{2} \times T^{2} \# n \overline{\mathbb{C P}^{2}}\right)=\chi\left(S^{2} \times T^{2}\right)+n\left(\chi\left(\overline{\mathbb{C P}^{2}}\right)-2\right)=n$$
Since $\tau=-n$, the dimension of the moduli space of scalar-flat Kähler metrics is given by
$$-3 \chi-8 \tau=-3 n+8 n=5 n$$
and the dimension the moduli space of ASD metrics is equal to
$$-\frac{(15 \chi+29 \tau)}{2}=-\frac{(15(n)+29(-n))}{2}=7 n$$
Thus, when $n \geq 1$, we have a strictly almost-Kähler ASD metric. Note that we only know that scalar-flat Kähler metric exist on $S^{2} \times T^{2} \# n \overline{\mathbb{C P}^{2}}$ for $n \geq 4$ [24].

By a similar calculation, we can show that the dimension of the moduli space of almost-Kähler ASD metrics is greater than the one of scalar-flat Kähler metrics in case of $S^{2} \times$ $\Sigma_{\mathbf{g}} \# n \overline{\mathbb{C P}^{2}}$ for $\mathbf{g} \geq 2$. And note that LeBrun showed the existence of scalar-flat Kähler metric explicitly when $n \geq 2$ [13] and Kim, Pontecorvo showed the existence of such a metric for $n \geq 1$ [11].

Example 4. Let us consider a minimal ruled surface $\mathbb{V}$ over $\Sigma_{\mathbf{g}}$., where $\mathbf{g} \geq 2$ and $\mathbb{V}$ is a holomorphic rank 2 bundle.

When $S^{2} \times \Sigma_{\mathbf{g}}$ admits a standard product Kähler metric, there is a holomorphic vector field. Let us consider projectivization of a rank 2 holomorphic vector bundle $\mathbb{V}$ over $\Sigma_{\mathbf{g}}$. When $\mathbb{V}$ is a stable vector bundle over $\Sigma_{\mathbf{g}}$, it can be shown that there is no holomorphic vector field on the ruled surface $P(\mathbb{V}) \rightarrow \Sigma_{\mathbf{g}}$ [7]. By Narasimhan-Seshadri theorem [21], there is a flat connection on $P(\mathbb{V})$ and therefore, universal cover of $P(\mathbb{V})$ is $S^{2} \times \mathcal{H}^{2}$. Then locally, $P(\mathbb{V})$ is $S^{2} \times \Sigma_{\mathbf{g}}$, where the standard Kähler metric is given. Therefore, $P(\mathbb{V})$ admits a scalar-flat Kähler metric.

On the other hand, suppose $P(\mathbb{V})$ admits a scalar-flat Kähler metric. It is shown in [4], [12] that $P(\mathbb{V})$ is locally riemannian product $S^{2} \times \Sigma_{\mathbf{g}}$ with the standard metric. We
briefly discuss the proof. Note that in this case, $\tau=0$, and therefore, we have $b_{+}=b_{-}$ and $W_{+}=W_{-}$. Thus, there is a self-dual harmonic 2-form $\omega$ and also an anti-self-dual harmonic 2-form $\varphi$. From the equation (2), we can conclude $\nabla \omega=0$. For an anti-self-dual harmonic form $\rho$, we have
$$0=<\nabla^{*} \nabla \varphi, \varphi>-2 W_{-}(\varphi, \varphi)+\frac{s}{3}|\varphi|^{2}$$
Thus, we can conclude $\nabla \varphi=0$. Since there are two parallel 2-forms, the holonomy is a subgroup of $S O(2) \times S O(2)$ and thus we get the conclusion.

In sum, we can conclude scalar-flat Kähler metrics on $P(\mathbb{V})$ correspond to the following representation up to conjugation.
$$\rho: \pi_{1}(M) \rightarrow S O(3) \times S O(2,1) .$$
Note that $\pi_{1}(M)$ has 2g generators and has 1 relation. Fundamental group $\pi_{1}(M)$ is expressed by
$$\pi_{1}(M)=<a_{1} . b_{1}, \ldots a_{\mathbf{g}}, b_{\mathbf{g}} \mid a_{1} b_{1} a_{1}^{-1} b_{1}^{-1} \ldots a_{\mathbf{g}} b_{\mathbf{g}} a_{\mathbf{g}}^{-1} b_{\mathbf{g}}^{-1}=1>.$$
Thus, the dimension of this representation is
$$6(2 \mathbf{g}-2)=12 \mathbf{g}-12 .$$

We can also count the dimension of the moduli space of scalar-flat Kähler metrics from $-3 \chi-8 \tau$. When the vector bundle is stable, there is no holomorphic vector field, and thus we can deform the scalar-flat Kähler metric on it. In this case, $\tau=0$, and therefore, the dimension of the moduli space is $-3 \chi$. Since $\chi=-4(\mathbf{g}-1)$, we have
$$-3 \chi=3 \times 4(\mathbf{g}-1)=12 \mathbf{g}-12 .$$

The dimension of the moduli space of ASD metrics is given by
$$-\frac{1}{2}(15 \chi+29 \tau) .$$
Again, since $\tau=0$, it's equal to
$$-\frac{1}{2} 15 \chi=\frac{1}{2} 15 \times 4(\mathbf{g}-1)=30(\mathbf{g}-1) .$$

This also can be calculated by considering the corresponding representation. ASD metrics on $P(\mathbb{V})$, over $\Sigma_{\mathbf{g}}$ is conformally flat since $\tau=0$. The conformal group acts on the universal covering space, $S^{4}-S^{1}$. Then the dimension of ASD metric is the same with the dimension of the following representation space up to conjugation.
$$\rho: \pi_{1}(M) \rightarrow S O(5,1) .$$
Since $\operatorname{dim} S O(5,1)=15$, the dimension of the moduli of ASD metrics which comes from this representation is given by 15(2g - 2), which is the same as before.

\section*{4. Seiberg-Witten invariants}

In this section, we show the Seiberg-Witten invariant can give us useful topological information for manifolds which admit a strictly almost-Kähler ASD metric and also a metric of positive scalar curvature.

We begin by explaining the Seiberg-Witten invariant briefly. Suppose a smooth, compact riemannian 4-manifold $(M, g)$ admits an almost-complex structure. Its homotopy class $c$ contains an almost-complex structure $J$ which is compatible with g [14]. Then the complexified tangent bundle $T M \otimes \mathbb{C}$ decomposes as $T^{1,0} \oplus T^{0,1}$. We define positive and negative spinor bundles by
$$\begin{gathered}
\mathbb{V}_{+}=\Lambda^{0,0} \oplus \Lambda^{0,2} \\
\mathbb{V}_{-}=\Lambda^{0,1} .
\end{gathered}$$
These spinor bundles inherits a hermitian inner product from $g$ on $M$. Also this bundles have Clifford action of $\Lambda^{p, q}$ given by
$$v \cdot\left(w^{1} \wedge \cdots \wedge w^{k}\right)=\sqrt{2} v^{0,1} \wedge w^{1} \wedge \cdots \wedge w^{k}-\sqrt{2} \sum_{i=1}^{k}\left\langle w^{i}, \overline{v^{1,0}}\right\rangle w^{1} \wedge \cdots \hat{w^{i}} \cdots \wedge w^{k},$$
where $\langle$,$\rangle is the hermitian inner product which is complex linear on the first variable and$ anti-linear on the second variable.

These bundles depend only on the homotopy class of J, which we denote by $c=[J]$. This means on a contractible open set $U \in M, \mathbb{V}_{ \pm}$can be identified with $\mathbb{S}_{ \pm} \otimes\left(K^{-1}\right)^{\frac{1}{2}}$, where $\mathbb{S}_{ \pm}$ are spin-bundles and they have spin connections induced from the Levi-Civita connection [14]. Thus, a connection $A$ on $K^{-1}$ which is compatible with $g$-induced inner product and Spin connection on $\mathbb{S}_{ \pm}$determines a connection on $\mathbb{V}_{ \pm}$. Then using this connection on $\mathbb{V}_{ \pm}$, we define the Dirac operator
$$D_{A}: C^{\infty}\left(\mathbb{V}_{+}\right) \rightarrow C^{\infty}\left(\mathbb{V}_{-}\right),$$
where $D_{A}$ is given by
$$D_{A}: C^{\infty}\left(\mathbb{V}_{+}\right) \xrightarrow{\nabla A} C^{\infty}\left(T^{*} M \otimes \mathbb{V}_{+}\right) \xrightarrow{c l} C^{\infty}\left(\mathbb{V}_{-}\right) .$$
Using an orthonormal basis, it is given by $D_{A}(\Phi)=\Sigma e_{i} \cdot\left(\nabla_{A} \Phi\right)\left(e_{i}\right)$.
The perturbed Seiberg-Witten equation is defined by
$$\left\{\begin{array}{l}
F_{A}^{+}=\sigma(\Phi)+i \epsilon \\
D_{A}(\Phi)=0 .
\end{array}\right.$$
Here $\Phi$ is a section of $C^{\infty}\left(\mathbb{V}_{+}\right)$and $F_{A}^{+}$is the self-dual part of the curvature form of the connection $A$ on $K^{-1}$ and $\epsilon$ is a perturbation self-dual 2-form. Since the Lie algebra of $U(1)$ is $i \mathbb{R}, F_{A}^{+} \in \Lambda^{2} \otimes i \mathbb{R}$ is a purely imaginary self-dual 2-form.

The Seiberg-Witten equation is invariant under the action of the gauge group, $\operatorname{Map}\left(M, S^{1}\right)$. In order to get a well-defined invariant, we need to consider the gauge group action. We call ( $A, \Phi$ ) a reducible solution if $\Phi \equiv 0$. Otherwise, we call ( $A, \Phi$ ) an irreducible solution.

The gauge group does not act freely on reducible solutions, and therefore, we only consider irreducible solutions.

Let us fix a unitary connection $A_{0}$ on $K^{-1}$. Then for any given unitary connection $A$ on $K^{-1}$, there is a gauge transformation so that after the gauge transformation on $A$, we have $A=A_{0}+\theta$ and $d^{*} \theta=0$. Thus, the moduli space
$$\mathcal{M}_{g}^{*}=\left\{(A, \Phi) \in L_{k}^{p}\left(\Lambda^{1}\right) \times L_{k}^{p}\left(\mathbb{V}^{+}\right) \mid D_{A} \Phi=0, F_{A}^{+}=\sigma(\Phi)+i \epsilon, \Phi \neq 0\right\} / \operatorname{Map}\left(M, S^{1}\right)$$
can be rewritten as follows,
$$\mathcal{M}_{g}^{*}=\left\{(A, \Phi) \mid D_{A} \Phi=0, F_{A}^{+}=\sigma(\Phi)+i \epsilon, d^{*}\left(A-A_{0}\right)=0, \Phi \neq 0\right\} / U^{1} \rtimes H^{1}(M, \mathbb{Z}),$$
where $U^{1} \rtimes H^{1}(M, \mathbb{Z})$ is a 1-dimensional group. In order to define a well-defined map, we choose the space $L_{k}^{p}$, where $p>4$ and $k \geq 1$. Here $L_{k}^{p}$ denote the Sobolev space
$$L_{k}^{p}(\Omega)=\left\{u \in L^{p}(\Omega)\left|D^{\alpha} u \in L^{p}(\Omega), \forall\right| \alpha \mid \leq k\right\} .$$
Then for generic $\epsilon, \mathcal{M}_{g}^{*}$ is a smooth manifold of dimension 0 . We refer to [20] for proofs in detail.

Using the gauge-fixing Lemma, and the bound of a spinor field $\Phi$ which comes from the Seiberg-Witten equation intrinsically, we get compactness of $\mathcal{M}^{*}$ and we recover regularity from the elliptic bootstrapping. Since the dimension of the moduli space is zero and the moduli space is compact, it consists of finite points.

If $(A, \Phi)$ is reducible, then $F_{A}^{+}=i \epsilon$. Denote by $c_{1}^{+}$the image of $c_{1} \in H^{2}(M, \mathbb{R})$ in $H^{+}(g)$ of deRham classes of self-dual harmonic 2-forms which depends on the metric $g$. If the orthogonal projection of $\epsilon$ onto the self dual harmonic 2-forms is not equal to $-2 \pi c_{1}^{+}$, then there is no such a solution. However, this is a closed condition, and therefore, for a generic 2-form, there is no reducible solution.

Definition 1. [14] Let $g$ be a riemannian metric on a compact, smooth 4-dimensional manifold $M$ which admits an almost-complex structure $J$ and let $\epsilon \in L_{k-1}^{p}\left(\Lambda^{+}\right)$. If $\left[\epsilon_{H}\right] \neq$ $-2 \pi c_{1}^{+}$, then $(g, \epsilon)$ is called a good pair. Here, $\epsilon_{H}$ is a harmonic part of $\epsilon$ and $c_{1}^{+}$means its projection onto self-dual part.

The path component of good pairs is called a chamber. If $b_{+}>1$, there is only one chamber and if $b_{+}=1$, there are exactly two chambers [14].

Definition 2. [14] We call $(g, \epsilon)$ an excellent pair if $(g, \epsilon)$ is a good pair and if i $\epsilon$ is a regular value for the map $\wp$, where $\wp: \mathcal{M}_{g}^{*} \rightarrow F_{A}^{+}-\sigma(\Phi)$.
Definition 3. Let $(M, c)$ be a smooth, compact 4-manifold with a homotopy class $c=[J]$ of almost-complex structures. Then we define by $n_{c}(M, g, \epsilon)$ for an excellent pair $(g, \epsilon)$ the number of solutions of (7) mod 2.

As proven in [14], if two excellent pairs $\left(g^{\prime}, \epsilon^{\prime}\right)$ and $(g, \epsilon)$ are in the same chamber, then
$$n_{c}\left(M, g^{\prime}, \epsilon^{\prime}\right)=n_{c}(M, g, \epsilon) .$$

Thus, when $b_{+}>1$, we define
$$n_{c}(M)=n_{c}(M, g, \epsilon)$$
for any excellent pair $(g, \epsilon)$.
When $b_{+}=1$, the Seiberg-Witten invariant depends on the chamber. However, if $c_{1} \neq 0$, and $c_{1}^{2} \geq 0$, then $(g, 0)$ is a good pair for any metric $g$ and therefore, all the pairs $(g, 0)$ belongs to the same path component [14].

We show that there is a non-trivial solution of the Seiberg-Witten equation for the pair $(g, \epsilon)$, where $g$ is an almost-Kähler anti-self-dual metric and $\epsilon$ is an explicit perturbation form. Using an almost-Kähler metric, Taubes proved there is only one solution for a large perturbation form [27]. And this unique solution consists of special connection $A_{0}$ on the anti canonical bundle $K^{-1}$, which was discovered independently by Blair and Taubes, and a simple positive spinor $\Phi_{0}=(r, 0) \in \mathbb{V}^{+}$. LeBrun found the curvature form of this connection [16]. Below we only need the self-dual part of $i F_{A_{0}}$.

Proposition 5. [16] Let $M$ be an almost-Kähler 4-manifold. Then the self-dual part of the curvature form of the Blair-Taubes connection $A_{0}$ is given by
$$i F_{A_{0}}^{+}=\eta+\frac{s+s^{*}}{8} \omega,$$
where $s$ is the scalar curvature and $s^{*}$ is the star-scalar curvature and $\eta=W^{+}(\omega)^{\perp} \in$ $\Lambda^{2,0} \oplus \Lambda^{0,2}$ is orthogonal to $\omega$.

When $W^{+}=0$, we have
$$i F_{A_{0}}^{+}=\frac{s+s^{*}}{8} \omega .$$
By definition,
$$s^{*}=2 R(\omega, \omega) .$$
Since $\omega \in \Lambda^{+}$, from the decomposition of the curvature operator, we get
$$R(\omega, \omega)=W^{+}(\omega, \omega)+\frac{s}{12}|\omega|^{2} .$$
Thus, for an ASD metric, we get
$$s^{*}=2 R(\omega, \omega)=\frac{s}{3} .$$
In sum, for an almost-Kähler ASD metric, we have
$$i F_{A_{0}}^{+}=\frac{s+s^{*}}{8} \omega=\frac{s+\frac{s}{3}}{8} \omega=\frac{s}{6} \omega .$$
In the Kähler case, we saw that the following identity (4) holds
$$\int_{M} s d \mu=4 \pi c_{1} \cdot[\omega] .$$
In the symplectic case, there is a corresponding formula which is discovered by Blair. In this paper, we can prove this identity using the curvature formula of the Blair-Taubes connection.

Lemma 6. [16] Let $(M, g, \omega)$ be a compact, 4-dimensional almost-Kähler manifold. Then,
$$\int_{M} \frac{s+s^{*}}{2} d \mu=4 \pi c_{1} \cdot[\omega] .$$
Proof. By Proposition 5, we have
$$i F_{A_{0}}^{+}=\eta+\frac{s+s^{*}}{8} \omega$$
Since
$$i F_{A_{0}}^{+}=2 \pi c_{1}^{+}\left(K^{-1}\right),$$
we get
$$4 \pi c_{1} \cdot \omega=2 i F_{A_{0}} \wedge \omega=\int_{M} \frac{s+s^{*}}{4} \omega \wedge \omega=\int_{M} \frac{s+s^{*}}{2} d \mu$$ \(\square\)

If the metric is almost-Kähler anti-self-dual, then $s^{*}$ is equal to $\frac{s}{3}$. Therefore, we get
$$4 \pi c_{1} \cdot[\omega]=\int_{M} \frac{s+s^{*}}{2} d \mu=\int_{M} \frac{s+\frac{s}{3}}{2} d \mu=\int_{M} \frac{2}{3} s d \mu$$
On the other hand, by the Weitzenböck formula (3) for a self dual 2-form, we have
$$0=|\nabla \omega|^{2}+\frac{2}{3} s .$$
Thus, the scalar curvature $s$ is non-positive and moreover, $s=0$ if and only if $\nabla \omega=0$. Therefore, for a strictly almost-Kähler anti-self-dual metric, we have
$$4 \pi c_{1} \cdot[\omega]=\int_{M} \frac{2}{3} s d \mu<0$$

Lemma 7. Let $g$ be an almost-Kähler ASD metric on a compact 4-manifold. If $g$ is a strictly almost Kähler ASD metric, then $c_{1} \cdot \omega<0$.

Corollary 2. Let $M$ be a smooth, compact, 4-manifold with an almost-Kähler anti-self-dual metric $g$. Suppose $c_{1}=0$. Then $g$ is hyperKähler.

Proof. For an almost-Kähler anti-self-dual metric, we have $s \leq 0$. From (10), if $c_{1}=0$, then $s=0$. This implies that $g$ is Kähler. On the other hand, we have
$$c_{1}^{2}=2 \chi+3 \tau=\frac{1}{4 \pi^{2}} \int_{M}\left(\frac{|s|^{2}}{24}+2\left|W^{+}\right|^{2}-\left|r i c_{0}\right|^{2}\right) d \mu$$
Since $g$ is scalar-flat anti-self-dual, we get $r i c_{0}=0$. Thus, $g$ is Ricci-flat Kähler. \(\square\)

Using an almost-Kähler metric, Taubes showed that the constant section $u_{0}$ of $\Lambda^{0,0}$ with unit length satisfies the Dirac equation. The connection $A_{0}$ on $K^{-1}$ induces a covariant derivative $\nabla_{A_{0}}$ on $\mathbb{V}_{+}$and $\nabla_{A_{0}} u_{0} \in \mathbb{V}_{+} \otimes T_{\mathbb{C}}^{*}$. As it is shown by Taubes [27], $A_{0}$ can be chosen so that the following holds
$$\left.\nabla_{A_{0}} u_{0}\right|_{\Lambda^{0,0}}=0 .$$

Then by [27] we note that $d \omega=0$ if and only if $D_{A_{0}} u_{0}=0$, where $D_{A_{0}}$ is the Dirac operator on $\mathbb{V}_{+}$.

Given $\Phi \in \mathbb{V}_{+}$, we define $\sigma(\Phi) \in \operatorname{End}\left(\mathbb{V}_{+}\right)$[22] by
$$\sigma(\Phi): \rho \rightarrow\langle\rho, \Phi\rangle \Phi-\frac{1}{2}|\Phi|^{2} \rho .$$

On the other hand, $\Lambda_{+}^{2} \otimes \mathbb{C}$ induces an endomorphism of $\mathbb{V}_{+}$by Clifford multiplication. Let us write $\Phi=(\alpha, \beta)$, where $\alpha \in \Lambda^{0,0}$ and $\beta \in \Lambda^{0,2}$. Then we claim the following self-dual 2-form induces $\sigma(\Phi)$,
$$\frac{i}{4}\left(|\alpha|^{2}-|\beta|^{2}\right) \omega+\frac{1}{2}(\bar{\alpha} \beta-\alpha \bar{\beta}) .$$
This can be checked directly. Here we use that $e_{i} \wedge e_{j}, i<j$ as an orthonormal basis and $\left|d z_{i}\right|=\left|\overline{d z_{i}}\right|=\sqrt{2}$. Also note that the above 2-form is a purely imaginary self-dual 2-form. Thus, the Seiberg-Witten equation can be written as
$$\left\{\begin{array}{l}
F_{A}^{+}=\frac{i}{4}\left(|\alpha|^{2}-|\beta|^{2}\right) \omega+\frac{1}{2}(\bar{\alpha} \beta-\alpha \bar{\beta})+i \epsilon \\
D_{A} \Phi=0 .
\end{array}\right.$$
Recall we have the following self-dual part of the curvature formula (9) for $A_{0}$
$$i F_{A_{0}}^{+}=\frac{s+s^{*}}{8} \omega=\frac{s+\frac{s}{3}}{8} \omega=\frac{s}{6} \omega .$$
For the spinor solution $\Phi_{0}=(r, 0)$, the corresponding self-dual 2-form is given by
$$\sigma\left(\Phi_{0}\right)=\frac{i r^{2} \omega}{4} .$$
Therefore, the $\epsilon$ corresponding to $\left(A_{0}, \Phi_{0}\right)$ on the Seiberg-Witten equation becomes
$$\epsilon=-\left(\frac{s}{6}+\frac{r^{2}}{4}\right) \omega .$$
In the following, we show that the Blair-Taubes connection $A_{0}$ and the positive spinor $\Phi_{0}=(r, 0)$ is a unique solution with respect to the almost-Kähler ASD metric $g$ and $\epsilon$.

Theorem 7. Let $M$ be a smooth, compact 4-manifold with an almost-Kähler ASD metric $g$. Then there is a unique non-trivial solution of the Seiberg-Witten equation for the pair $(g, \epsilon)$, where
$$\epsilon=-\left(\frac{s}{6}+\frac{r^{2}}{4}\right) \omega$$
and $r \geq \sqrt{\frac{4|s|}{3}}$.
Proof. Let us consider following perturbed Seiberg-Witten equation
$$\left\{\begin{array}{l}
D_{A} \Phi=0 \\
F_{A}^{+}=\sigma(\Phi)+i \epsilon
\end{array}\right.$$

A section $\Phi \in \mathbb{V}_{+}=\Lambda^{0,0} \oplus \Lambda^{0,2}$ can be written as
$$\Phi=(\alpha, \beta) .$$
The Weitzenböck formula for $D_{A}^{*} D_{A}$ is given by
$$D_{A}^{*} D_{A} \Phi=\nabla_{A}^{*} \nabla_{A} \Phi+\frac{s}{4} \Phi+\frac{F_{A}}{2} \cdot \Phi,$$
where • is Clifford multiplication. Since $\Phi \in \mathbb{V}^{+}$, we have $\frac{F_{A}}{2} \cdot \Phi=\frac{F_{A}^{+}}{2} \cdot \Phi$. From the Seiberg Witten equation, we get
$$0=\left\langle\nabla_{A}^{*} \nabla_{A} \Phi, \Phi\right\rangle+\frac{s}{4}|\Phi|^{2}+\frac{|\Phi|^{4}}{4}-\left(\frac{s}{6}+\frac{r^{2}}{4}\right)\left(|\alpha|^{2}-|\beta|^{2}\right) .$$
If we put $\phi=\sigma(\Phi)$, then $\phi$ is a self-dual 2-form. Moreover, $\phi$ and $\Phi$ are related in the following way [15],
$$\begin{gathered}
|\phi|^{2}=\frac{1}{8}|\Phi|^{4}, \\
|\nabla \phi|^{2} \leq \frac{1}{2}|\Phi|^{2}|\nabla \Phi|^{2} .
\end{gathered}$$
Using the Weitzenböck formula for self-dual 2-form (2), we have
$$\int_{M}\left(|\nabla \phi|^{2}+\frac{s}{3}|\phi|^{2}\right) d \mu \geq 0$$
In terms of $\Phi$, this means
$$\int_{M}\left(|\Phi|^{2}|\nabla \Phi|^{2}+\frac{s}{12}|\Phi|^{4}\right) d \mu \geq 0$$
By multiplying $|\Phi|^{2}$ in (11) and using $\left\langle\nabla_{A}^{*} \nabla_{A} \Phi, \Phi\right\rangle=\left|\nabla_{A} \Phi\right|^{2}+\frac{1}{2} \Delta|\Phi|^{2}$ and $\int_{M}|\Phi|^{2} \Delta|\Phi|^{2} d \mu \geq$ 0, it follows
$$\int_{M}|\Phi|^{2}\left(\frac{s}{6}|\Phi|^{2}+\frac{|\Phi|^{4}}{4}-\left(\frac{s}{6}+\frac{r^{2}}{4}\right)\left(|\alpha|^{2}-|\beta|^{2}\right)\right) d \mu \leq 0 .$$
By expanding terms and subtracting some positive terms, we have
$$\int_{M}|\Phi|^{2}\left(\frac{s}{3}|\beta|^{2}+\frac{r^{2}\left(|\alpha|^{2}-r^{2}\right)}{4}+\frac{r^{2}}{4}|\beta|^{2}\right) d \mu \leq 0 .$$
If we choose $r$ so that
$$r \geq \sqrt{\frac{4|s|}{3}},$$
then we get
$$\int_{M}|\Phi|^{2}|\alpha|^{2} d \mu \leq r^{2} \int_{M}|\Phi|^{2} d \mu .$$
Using the fact $|\Phi|^{2}=|\alpha|^{2}+|\beta|^{2}$, we have
$$\int_{M}|\alpha|^{2}|\alpha|^{2} d \mu \leq \int_{M}|\Phi|^{2}|\alpha|^{2} d \mu \leq r^{2} \int_{M}\left(|\alpha|^{2}+|\beta|^{2}\right) d \mu .$$

Thus, we get
$$\int_{M}\left(|\alpha|^{2}|\alpha|^{2}-r^{2}|\alpha|^{2}\right) d \mu \leq r^{2} \int_{M}|\beta|^{2} d \mu .$$
Using $F_{A}^{+}=\sigma(\Phi)+i \epsilon$ and $\langle\sigma(\Phi), \omega\rangle=i\left(\frac{|\alpha|^{2}-|\beta|^{2}}{2}\right)$, we have
$$|\alpha|^{2}-|\beta|^{2}=-2 i\left\langle F_{A}, \omega\right\rangle+4\left(\frac{s}{6}+\frac{r^{2}}{4}\right) .$$

Since $c_{1}$ is represented by $\left[\frac{i F_{A}}{2 \pi}\right]$ for any connection $A$, we have $i F_{A}=i F_{A_{0}}+d \gamma$ for the Blair-Taubes connection $A_{0}$ and for some 1-form $\gamma$. By (9), we get
$$|\alpha|^{2}-|\beta|^{2}=-\frac{4 s}{6}-2\langle d \gamma, \omega\rangle+4\left(\frac{s}{6}+\frac{r^{2}}{4}\right) .$$
Thus, we have
$$|\alpha|^{2}-|\beta|^{2}-r^{2}=-2\langle d \gamma, \omega\rangle .$$
Since $\omega$ is a self-dual harmonic 2-form, by integrating, we have
$$\int_{M}\left(|\alpha|^{2}-r^{2}\right) d \mu=\int_{M}\left(|\beta|^{2}-2\left\langle\gamma, d^{*} \omega\right\rangle\right) d \mu=\int_{M}|\beta|^{2} d \mu$$
Using this equality and $\int_{M}\left(|\alpha|^{2}|\alpha|^{2}-r^{2}|\alpha|^{2}\right) d \mu \leq r^{2} \int_{M}|\beta|^{2} d \mu$, we have
$$\int_{M}\left(|\alpha|^{4}-r^{2}|\alpha|^{2}\right) d \mu \leq r^{2} \int_{M}\left(|\alpha|^{2}-r^{2}\right) d \mu .$$
This implies
$$\int_{M}\left(|\alpha|^{2}-r^{2}\right)^{2} d \mu=\int_{M}\left(|\alpha|^{4}-r^{2}|\alpha|^{2}-r^{2}|\alpha|^{2}+r^{4}\right) d \mu \leq 0$$
Thus $|\alpha|^{2}=r^{2}$ and from the equality $\int_{M}\left(|\alpha|^{2}-r^{2}\right) d \mu=\int_{M}|\beta|^{2} d \mu$, it follows that $\beta=0$. Then up to gauge equivalence $\alpha=r$. Since the Dirac equation is invariant under the gauge transformation, we have
$$D_{A} \Phi_{0}=0,$$
where $\Phi_{0}=(r, 0)$. Since $D_{A} \Phi_{0}=D_{A_{0}} \Phi_{0}+\frac{1}{2} \theta \cdot \Phi_{0}$, where • is Clifford multiplication, we get
$$\theta \cdot \Phi_{0}=0 .$$
This implies that $\theta^{0,1}=0$. On the other hand, since $\theta$ is a purely-imaginary 1-form, we can conclude $\theta=0$. Thus, up to gauge transformation, we get the standard solution $\left(A_{0}, \Phi_{0}\right)$. \(\square\)

Lemma 8. Let $g$ be an almost-Kähler ASD metric and let $\epsilon$ be given by
$$\epsilon=-\left(\frac{s}{6}+\frac{r^{2}}{4}\right) \omega .$$
Then, $(g, \epsilon)$ is an excellent pair.

Proof. By theorem 7, there is a unique solution $\left(A_{0}, \Phi_{0}\right)$ up to gauge equivalence. We show that this solution is nondegenerate. This is equivalent to showing the map $\wp$ is surjective, where $\wp: \mathcal{M}_{g}^{*} \rightarrow F^{+}-\sigma(\Phi)$. Let us consider the linearization of the following equations at $\left(\left(A_{0}, \Phi_{0}\right),-\left(\frac{s}{6}+\frac{r^{2}}{4}\right) \omega\right.$,
$$d^{*}\left(A-A_{0}\right)=0, D_{A} \Phi=0, F_{A}^{+}=\sigma(\Phi)+i \epsilon .$$
Considering (8), the linearization $D_{\wp}$ is onto if and only if the dimension of the kernel of (12) is 1. Suppose $(\theta,(u, \psi))$ belong to the kernel of (12). We saw that any solution $\Phi=(\alpha, \beta)$ of the equations $D_{A} \Phi=0$ and $F_{A}^{+}=\sigma(\Phi)+i \epsilon$ must be $|\alpha|^{2}=r^{2}, \beta=0$. Thus $(u, \psi)$ satisfies the linearization of the pair of the equations $|\alpha|^{2}=r^{2}$ and $\beta=0$. The linearization of these equations evaluated at $\Phi_{0}=(r, 0)$ are
$$r(u+\bar{u})=0, \quad \psi=0 .$$
Note that $u+\bar{u}=0$ implies that the real part of $u$ is zero. Thus, $u$ is purely imaginary. Also note that from the linearization of the Dirac equation, we get
$$D_{A_{0}}(u)=-\frac{1}{2} \theta \cdot(r, 0) .$$
Since $D_{A_{0}}(u)=\sqrt{2} \bar{\partial} u$, we get
$$\bar{\partial} u=C \theta^{0,1},$$
where $C$ is an explicit constant. This implies that $d u=\theta$. Since $d^{*} \theta=0$, we get $d^{*} d u=0$. By taking an $L^{2}$ inner product with $u$, we can conclude $d u=0$, and therefore, $u$ is constant and $\theta=0$. Since $u$ is purely imaginary and constant, we get the dimension of the kernel of (12) is equal to 1. \(\square\)

Lemma 9. Let $M$ be a smooth, compact 4-manifold with $b_{+}=1$ and assume $M$ admits a strictly almost-Kähler anti-self-dual metric $g$. Then $(g, 0)$ and $(g, \epsilon)$, where $\epsilon=-\left(\frac{s}{6}+\frac{r^{2}}{4}\right) \omega$ are good pairs respectively and they can be path connected through good pairs, and therefore, they belong to the same path component.

Proof. We use the Blair-Taubes connection $A_{0}$ in order to get $2 \pi c_{1}^{+}$. Since $b_{+}=1$, we can think of $\frac{\omega}{\sqrt{2}}$ as a basis for $\mathcal{H}^{+}$. Thus, the harmonic part of $i F_{A_{0}}^{+}$is
$$\left(\int_{M}\left\langle\frac{s \omega}{6}, \frac{\omega}{\sqrt{2}}\right\rangle d \mu\right) \frac{\omega}{\sqrt{2}}=\frac{s_{0}}{6} \omega,$$
where $s_{0}=\int s d \mu$. Since $g$ is a strictly almost-Kähler ASD metric, we have $s_{0}<0$. In particular, this means $2 \pi c_{1}^{+} \neq 0$. Thus, $(g, 0)$ is a good pair. We claim, for $t \in(0,1),(g, t \epsilon)$ is a good pair. Suppose not. Then there is $t_{0} \in[0,1]$ such that
$$\frac{s_{0}}{6} \omega=t_{0}\left(\frac{s_{0}}{6}+\frac{r^{2}}{4}\right) \omega .$$
Then we rewrite this as
$$\left(1-t_{0}\right) \frac{s_{0}}{6} \omega=\frac{t_{0} r^{2}}{4} \omega .$$

Since $s_{0}<0$, we get a contradiction. \(\square\)

From this, it follows that $(g, 0)$ and $(g, \epsilon)$ belong to the same path component. Therefore, for the chamber which contains $(g, 0)$, where $g$ is a strictly almost-Kähler ASD metric, the SW invariant is non-zero.

Lemma 10. [14] Let $M$ be a compact, 4-dimensional manifold. Suppose $M$ admit an almost-complex structure and $b_{+}>0$ and assume $M$ admits a positive scalar curvature metric $\tilde{g}$. Then for the chamber whose closure contains $(\tilde{g}, 0), n_{c}=0$.

Liu's theorem [18] tells us about symplectic manifolds which admits a positive scalar curvature metric.

Theorem 8. (Liu) Let $M$ be a smooth, compact, symplectic 4-manifold. If $M$ admits a positive scalar curvature metric, then $M$ is diffeomorphic to either a rational or ruled surfaces.

Theorem 9. Suppose a smooth, compact 4-manifold $M$ admits an almost Kähler ASD metric. If $M$ also admits a metric of positive scalar curvature, then it is diffeomorphic to one of the following:
\begin{itemize}
\item[-] $\mathbb{C P}^{2} \# n \overline{\mathbb{C P}^{2}}$ for $n \geq 10$;
\item[-] $S^{2} \times \Sigma_{\mathbf{g}}$ and non-trivial $S^{2}$-bundle over $\Sigma_{\mathbf{g}}$, where $\Sigma_{\mathbf{g}}$ is a Riemann surface with genus $\mathbf{g} \geq 2$;
\item[-] $\left(S^{2} \times \Sigma_{\mathrm{g}}\right) \# n \overline{\mathbb{C P}^{2}}$ for $n \geq 1$; or
\item[-] $\left(S^{2} \times T^{2}\right) \# n \overline{\mathbb{C P}^{2}}$ for $n \geq 1$.
\end{itemize}

Proof. By Liu's theorem, $M$ is diffeomorphic to a rational or ruled surfaces. Suppose $g$ be a strictly almost-Kähler ASD metric. Then the scalar curvature $s$ is negative somewhere. Then $c_{1} \neq 0$ and $b_{+}=1$. We show $c_{1}^{2}<0$. If $c_{1}^{2} \geq 0$, then all pairs $(g, 0)$ is a good pair and belong to the same chamber. However, by Lemma 10, for the chamber which contains $\tilde{g}$, a metric of positive scalar curvature, $n_{c}=0$. On the other hand, for the chamber which contains $(g, 0)$, where $g$ is a strictly almost-Kähler ASD metric, $n_{c}=1$. Thus, we get a contradiction and therefore, $c_{1}^{2} \geq 0$. Thus, we get the conclusion in this case. Note that by Gromov-Lawson [9], all of these examples admit a metric of positive scalar curvature.

Suppose $g$ be a scalar-flat Kähler metric. Then by Yau's theorem, $M$ has either $c_{1}=0$, or it is a ruled surface. Suppose $c_{1} \neq 0$. Then, from Remark 1, we get the conclusion in this case.

Suppose $M$ admits a scalar-flat Kähler metric and $c_{1}=0$. Then, universal cover of $M$ is to either $T^{4}$ or $K 3$. However, these do not belong to the list of Liu's theorem. Thus, $c_{1} \neq 0$. \(\square\)

Theorem 10. Suppose $\mathbb{C P}^{2} \# n \overline{\mathbb{C P}^{2}}$ admits an almost-Kähler ASD metric. Then $n \geq 10$.
Proof. In this case, $c_{1} \neq 0$. If $n \leq 9$, then $c_{1}^{2} \geq 0$ and therefore, all the pairs $(g, 0)$ belong to the same chamber. Since these manifolds admit a positive scalar curvature metric, it follows that any almost-Kähler anti-self-dual metric is scalar-flat Kähler. Then, we have $c_{1}^{2}<0$,
which is a contradiction. Thus, $\mathbb{C P}^{2} \# n \overline{\mathbb{C P}^{2}}$ for $n \leq 9$ does not admit an almost-Kähler anti-self-dual metric. \(\square\)

\section*{Bibliography}
\begin{itemize}
\item[] [1] J. Armstrong, On four-dimensional almost-Kähler manifolds, Quart. J. Math. Oxford Ser.(2), 48(1997), pp. 405-415.
\item[] [2] M. F. Atiyah, N. J .Hitchin, and I. M .Singer, Self-duality in four-dimensional Riemannian geometry, Proc. Roy. Soc. London Ser. A, 362(1978), pp. 425-461.
\item[] [3] J. -P. Bourguignon, Les variétés de dimension 4 à signature non nulle dont la courbure est harmonique sont d'Einstein, Invent. Math. 63 (1981), pp. 263-286.
\item[] [4] D. Burns and P. de Bartolomeis, stability of vector bundles and extremal metrics, Inv. Math. 92 (1998) 403-407
\item[] [5] C. Boyer, Conformal duality and compact complex surfaces, Math. Ann. 274 (1986), pp. 517-526.
\item[] [6] S. Donaldson and R. Friedman, Connected sums of self-dual manifolds and deformations of singular spaces, 1989 Nonlinearity, 2 (1989), pp. 197-239.
\item[] [7] M. G. Eastwood and M. A. Singer, The Fröhlicher spectral sequence on a twistor space, J. Differential Geom. Volume 38, Number 3 (1993), 653-669.
\item[] [8] T. Eguchi, P. B. Gilkey, A. J. Hanson, Gravitation, gauge theories and differential geometry, Phys. Rep. 66 (1980), no. 6, 213-393.
\item[] [9] M. Gromov and H. B. Lawson, Jr., The classification of simply connected manifolds of positive scalar curvature, Ann.of Math.(2) 111(1980), no.3, 423-434.
\item[] [10] J. -S. Kim, C. LeBrun and M. Pontecorvo, Scalar-fat Kähler surfaces of all genera, J.reine angew. math 486(1997), 69-95.
\item[] [11] J. -S. Kim and M. Pontecorvo, A new method of constructing scalar-flat Kähler surfaces, J. Differential Geom. Volume 41, Number 2 (1995), 449-477.
\item[] [12] C. LeBrun, On the topology of self-dual 4-manifolds, Proc. Am. Math. Soc. 98(1986), 637-640.
\item[] [13] C. LeBrun, Scalar-flat Kähler metrics on blown-up ruled surfaces, J. Reine Angew Math. 420(1991), 161-177.
\item[] [14] C. LeBrun, On the scalar curvature of complex surfaces, Geom. Func. An. 5 (1995), 619-628.
\item[] [15] C. LeBrun, Ricci curvature, Minimal volumes, and Seiberg-Witten theory, Invent. Math. 145 (2001), 279-316
\item[] [16] C. LeBrun, Einstein Metrics, symplectic minimality, and pseudo-holomophic curves, Ann. Glob. An. Geom. 28 (2005), 157-177.
\item[] [17] C. LeBrun and M. A. Singer, Existence and deformation theory for scalar-flat kahler metrics on compact complex surfaces, Inv. Math. 112(1993), pp. 273-313.
\item[] [18] A-K. Liu, Some new applications of general wall-crossing formula, Gompf's conjecture and its applications, Math. Res. Lett, 3(1996), pp.569-585.
\item[] [19] D. McDuff and D. Salamon, Introduction to symplectic topology, Oxford University Press, 1995
\item[] [20] J. W. Morgan, The Seiberg-Witten equations and applications to the topology of smooth four-manifolds, Mathematical notes vol. 44, Princeton University Press.
\item[] [21] M. S. Narasimhan and C. S. Seshadri, Stable and unitary vector bundles on a compact Riemann surface, Ann. of Math. 82 (1965), pp. 540-567.
\item[] [22] L. Nicolaescu, Notes on Seiberg-Witten theory, Graduate Studies in Mathematics 28, American Mathematical Society, 2000.
\item[] [23] M. Pontecorvo, On twistor spaces of anti-self-dual hermitian surfaces, Trans. Amer. Math. Soc. 331(1992), no.2, 653-661.
\item[] [24] Y. Rollin and M. A. Singer, Non-minimal scalar-flat Kähler surfaces and parabolic stability, Inv. math. 162 (2005), no. 2, 235-270.
\item[] [25] S. Salamon, Geometry seminar, "Luigi Bianchi", 1982, Springer
\item[] [26] C. H. Taubes, The existence of anti-self-dual conformal structures, J. Differential Geometry. 36(1992) 163-253.
\item[] [27] C. H. Taubes, The Seiberg-Witten invariants and symplectic forms, Math. Res. Lett. 1 (1994), 809-822.
\item[] [28] S.-T. Yau, On the curvature of compact hermitian manifolds, Inv. Math. 25 (1974), 213-239.
\end{itemize}

The Center for Geometry and its Applications, Pohang University of Science and Technology, Pohang city, 790-784, South Korea

E-mail address: kiysd@postech.ac.kr
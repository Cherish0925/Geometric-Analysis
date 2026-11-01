---
retention_scope: session
part: 1
total_parts: 1
---

---
source_file: 1612_01866.pdf
converter: mathpix
format: mmd
---

\title{
KÄHLER METRICS WITH CONE SINGULARITIES ALONG A DIVISOR OF BOUNDED RICCI CURVATURE
}

\author{
MARTIN DE BORBON
}

\begin{abstract}
Let $D$ be a smooth divisor in a compact complex manifold $X$ and let $\beta \in(0,1)$. We use the liner theory developed by Donaldson [5] to show that in any positive co-homology class on $X$ there is a Kähler metric with cone angle $2 \pi \beta$ along $D$ which has bounded Ricci curvature. We use this result together with the Aubin-Yau continuity method to give an alternative proof of a well-known existence theorem for Kahler-Einstein metrics with cone singularities.
\end{abstract}

\section*{1. Introduction}

Let $X$ be a compact complex manifold, $D \subset X$ a smooth divisor and $\beta \in(0,1)$. Let $\omega$ be a $C^{\alpha}$ Kähler metric on $X$ with cone angle $2 \pi \beta$ along $D$-see Section 2 for the definitions-; $\alpha \in(0,1)$ is the Hölder exponent, we also require that $\alpha \leq(1 / \beta)-1$. Let $0<\alpha^{\prime}<\alpha$ and $\epsilon>0$.

Theorem 1. There is $\phi \in C^{2, \alpha^{\prime}}(X)$ with $\|\phi\|_{2, \alpha^{\prime}}<\epsilon$ such that the Ricci form of $\omega_{\phi}=\omega+i \partial \bar{\partial} \phi$ extends to $X$ as a 2-form, smooth with respect to the complex coordinates. In particular $\omega_{\phi}$ has bounded Ricci curvature.

We take $\alpha^{\prime}<\alpha$ in order to approximate as much as we like the relevant $C^{\alpha}$ function ('Ricci potential' of $\omega)$ by smooth functions. Theorem 1 follows by performing a suitable and small change in the volume form of $\omega$, this is done via the Implicit Function Theorem and uses the linear theory developed in [5].

In a different direction; it is conjectured that the existence of Kahler metrics with cone singularities of bounded sectional curvature imposes strong restrictions on the complex geometry of the pair $(X, D)$-see [1]-. More precisely, if we denote the normal bundle of $D$ as $\nu_{D}$ and the tangent bundles as $T X$ and $T D$; then it is expected a holomorphic splitting $\left.T X\right|_{D}=T D \oplus \nu_{D}$. Theorem 1 says that there are no such restrictions for the case of Ricci curvature.

As an application of Theorem 1 we give an alternative proof of a well-established existence result for Kähler-Einstein metrics with cone singularities (KEcs). These are metrics with cone angle $2 \pi \beta$ along $D$ which satisfy $\operatorname{Ric}(g)=\lambda g$ in the complement of $D$ for some constant $\lambda$.

Theorem 2. (1) If $c_{1}(X)-(1-\beta) c_{1}(D)<0$; then there is a unique KEcs with $\lambda=-1$.
(2) If $c_{1}(X)=(1-\beta) c_{1}(D)$; then there is a unique KEcs with $\lambda=0$ in each Kähler class.

We prove Theorem 2 by means of the classical Aubin-Yau continuity path, starting with a metric of bounded Ricci curvature. The openness follows from [5] and the closedness from standard a priori estimates. The $C^{0}$ estimate uses the maximum principle when $\lambda=-1$ (see [8]) and Moser iteration when $\lambda=0$ (see [2]). The $C^{2}$ estimate follows from the maximum principle applied to the Chern-Lu inequality, together with the fact that there is a reference metric with bisectional curvature bounded above (see [7]). Finally, the $C^{2, \alpha}$ estimate follows from the interior Schauder estimates in [3].

The proof of Theorem 2 presents -in this simpler compact setting- the arguments in [4] used to establish an existence theorem for asymptotically conical Ricci-flat Kähler metrics with cone singularities. In that context, the method we use to show Theorem 1 serves to produce asymptotically conical metrics which are Ricci-flat outside a compact set -see Proposition 6 in [4]-.

Acknowledgments. This article contains material from the author's PhD Thesis at Imperial College, founded by the European Research Council Grant 247331 and defended in December 2015. I wish to thank my supervisor, Simon Donaldson, for his encouragement and support.

\footnotetext{
Date: DECEMBER, 2016.
}

\section*{2. Background}
2.1. Linear Theory. Fix $0<\beta<1$. We work on $\mathbb{C}^{n}$ with complex coordinates $z_{1}, \ldots, z_{n}$. Consider the model metric
$$g_{(\beta)}=\beta^{2}\left|z_{1}\right|^{2 \beta-2}\left|d z_{1}\right|^{2}+\sum_{j=2}^{n}\left|d z_{j}\right|^{2},$$
which has cone singularities of total angle $2 \pi \beta$ along $\left\{z_{1}=0\right\}$. It induces a distance $d_{\beta}$ and therefore, for each $\alpha \in(0,1)$, a Hölder semi-norm
$$[u]_{\alpha}=\sup _{x, y} \frac{|u(x)-u(y)|}{d_{\beta}(x, y)^{\alpha}}$$
on continuous functions defined on domains of $\mathbb{C}^{n}$. If we write $z_{1}=r^{1 / \beta} e^{i \theta}$, then $g_{(\beta)}=d r^{2}+\beta^{2} r^{2} d \theta^{2}+$ $\sum_{j=2}^{n}\left|d z_{j}\right|^{2}$. In these cone coordinates, $\left(r e^{i \theta}, z_{2}, \ldots, z_{n}\right), g_{(\beta)}$ is quasi-isometric to the Euclidean metric -indeed $\beta^{2} g_{E u c} \leq g_{(\beta)} \leq g_{E u c^{-}}$; therefore 2.2 becomes equivalent to the standard Hölder semi-norm with respect to the Euclidean distance.

We want to define Hölder continuous 1-forms. Set $\epsilon=d r+i \beta r d \theta$. A $(1,0)$ form $\eta$ is called $C^{\alpha}$ if $\eta=u_{1} \epsilon+\sum_{j=2}^{n} u_{j} d z_{j}$ with $u_{1}, u_{j} C^{\alpha}$ functions in the usual sense in the cone coordinates; it is also required that $u_{1}=0$ on the singular set $\left\{z_{1}=0\right\}$. Note that if we change $\epsilon$ with $\tilde{\epsilon}=e^{i \theta} \epsilon=\beta\left|z_{1}\right|^{\beta-1} d z_{1}$, say, in the definition then the vanishing condition implies that we get the same space. We move on and consider a 2-form $\eta$ of type (1, 1), we use the basis $\left\{\epsilon \bar{\epsilon}, \epsilon d \overline{z_{j}}, d z_{j} \bar{\epsilon}, d z_{j} d \overline{z_{k}}\right\}$ for $j, k=2, \ldots, n$. We say that $\eta$ is $C^{\alpha}$ if its components are $C^{\alpha}$ functions; we also require the components corresponding to $\epsilon d \overline{z_{j}}, d z_{j} \bar{\epsilon}$ to vanish on $\left\{z_{1}=0\right\}$. Finally, we set $C^{2, \alpha}$ to be the space of $C^{\alpha}$ (real) functions $u$ such that $\partial u, i \partial \bar{\partial} u$ are $C^{\alpha}$. It is straightforward to introduce norms; we define the $C^{\alpha}$ norm of a function $\|u\|_{\alpha}$ as the sum of its $C^{0}$ norm $\|u\|_{0}$ and its $C^{\alpha}$ semi-norm $[u]_{\alpha}$. The $C^{2, \alpha}$ norm of a function $u$, denoted by $\|u\|_{2, \alpha}$, is the sum of $\|u\|_{\alpha}$, the $C^{\alpha}$ norm of the components of $\partial u$ in and the $C^{\alpha}$ norm of the components of $i \partial \bar{\partial} u$.

Let $X$ be a compact complex manifold, $D \subset X$ a smooth divisor and $g$ a smooth Kähler metric on the complement of $D$.

Definition 1. We say that $g$ is a $C^{\alpha}$ metric with cone angle $2 \pi \beta$ along $D$, if for every $p \in D$ we can find complex coordinates $\left(z_{1}, \ldots, z_{n}\right)$ centred at $p$ in which
\begin{itemize}
\item[-] $D=\left\{z_{1}=0\right\}$.
\item[-] $(1 / C) g_{(\beta)} \leq g \leq C g_{(\beta)}$ for some $C>0$.
\item[-] There is a local Kähler potential for $g$ which belongs to $C^{2, \alpha}$.
\end{itemize}

It is easy to show that if $g$ satisfies Definition 1, then its tangent cone at points of $D$ is $g_{(\beta)}$. It is also straightforward to see that its Kähler form $\omega$ defines a closed current on $X$-with zero Lelong numbers at points of $D$ - and therefore there is a positive de Rham co-homology class $[\omega]$. Nevertheless, we won't make use of these facts.

Set $\left\{v_{1}, \ldots, v_{n}\right\}$ to be the vectors
$$v_{1}=\left|z_{1}\right|^{1-\beta} \frac{\partial}{\partial z_{1}}, \quad v_{j}=\frac{\partial}{\partial z_{j}} \text { for } j=2, \ldots n .$$
Note that, with respect to $g_{(\beta)}$, these vectors are orthogonal and their length is constant. In the complement of $D$ we have smooth functions $g_{i \bar{j}}=g\left(v_{i}, \bar{v}_{j}\right)$ which admit a Hölder continuous extension to $D$. The matrix $\left(g_{i \bar{j}}(p)\right)$ is positive definite and $g_{1 \bar{j}}=0$ when $j \geq 2$ and $z_{1}=0$. It is interesting to note that Definition 1 is independent of the complex coordinates $z_{1}, \ldots, z_{n}$ only if we add the restriction that $\alpha \leq \beta^{-1}-1$. Indeed, assume for simplicity that $g$ is a metric in a domain of $\mathbb{C}^{2}$, with standard complex coordinates $\left(\tilde{z}_{1}, \tilde{z}_{2}\right)$, of cone angle $2 \pi \beta$ along $D=\left\{\tilde{z}_{1}=0\right\}$. We get smooth functions $\tilde{g}_{i \bar{j}}$ on the complement of $D$ which extend Hölder continuously to $D$. Set $\tilde{z}_{1}=z_{1}$ and $\tilde{z}_{2}=z_{1}+z_{2}$, so that
$$\frac{\partial}{\partial z_{1}}=\frac{\partial}{\partial \tilde{z}_{1}}+\frac{\partial}{\partial \tilde{z}_{2}}, \quad \frac{\partial}{\partial z_{2}}=\frac{\partial}{\partial \tilde{z}_{2}} .$$

In the coordinates $\left(z_{1}, z_{2}\right)$,
$$g_{1 \overline{1}}=\tilde{g}_{1 \overline{1}}+\left|z_{1}\right|^{1-\beta}\left(\tilde{g}_{1 \overline{2}}+\tilde{g}_{2 \overline{1}}\right)+\left|z_{1}\right|^{2-2 \beta} \tilde{g}_{2 \overline{2}}, \quad g_{1 \overline{2}}=\tilde{g}_{1 \overline{2}}+\left|z_{1}\right|^{1-\beta} \tilde{g}_{2 \overline{2}}, \quad g_{2 \overline{2}}=\tilde{g}_{2 \overline{2}} .$$
However, the function $\left|z_{1}\right|^{1-\beta}$ belongs to $C^{\alpha}$ only if $\alpha \leq \beta^{-1}-1$.
There are two types of coordinates we can consider around $D$. The first is given by holomorphic coordinates $z_{1}, \ldots, z_{n}$ in which $D=\left\{z_{1}=0\right\}$. In the second we replace $z_{1}$ with $r e^{i \theta}$, by means of $z_{1}=r^{1 / \beta} e^{i \theta}$, and leave $z_{2}, \ldots, z_{n}$ unchanged; we refer to the last as cone coordinates. In other words, there are two relevant differential structures on $X$ in our situation. One is given by the complex manifold structure we started with, the other is given by declaring the cone coordinates to be smooth. The two structures are clearly equivalent by a map modelled on
$$\left(r e^{i \theta}, z_{2}, \ldots, z_{n}\right) \rightarrow\left(r^{1 / \beta} e^{i \theta}, z_{2}, \ldots, z_{n}\right)$$
in a neighborhood of $D$. The notion of a function being Hölder continuous (without specifying the exponent) is independent of the coordinates we take, however the value of its exponent does depend. We set $C^{\alpha}(X)$ to be the space of Hölder continuous functions of exponent $\alpha$ with respect to the cone coordinates -this agrees with the space of $C^{\alpha \beta}$ functions with respect to the complex coordinates-. Taking a finite covering of $X$ by complex coordinate charts, it is straightforward to define the space $C^{2, \alpha}(X)$ and endow it with a norm which makes it into a Banach space. The main result we want to recall is the following

Theorem 3. Assume that $\alpha<(1 / \beta)-1$; then $\Delta_{g}: C^{2, \alpha}(X) \rightarrow C^{\alpha}(X)$ is a Fredholm operator of index 0.
Theorem 3 is proved in [5]. In this article $\Delta_{g}$ denotes the negative or 'analyst' Laplacian of $g$.
2.2. Standard reference metric. Let $\Lambda$ be the complex line bundle associated to $D, h$ a smooth Hermitian metric on it and $s$ a holomorphic section of $\Lambda$ with $s^{-1}(0)=D$. Let $\Omega$ be a smooth Kähler metric on $X$; for $\delta>0$ set
$$\omega=\Omega+\delta i \partial \bar{\partial}|s|_{h}^{2 \beta} .$$
We have the following
Proposition 1. If $\delta$ is sufficiently small, then $\omega$ is $C^{\alpha}$ according to Definition 1 with $\alpha=(1 / \beta)-1$. Moreover, its sectional curvature is uniformly bounded above.

Proof. By compactness, it is enough to work locally. Let $F$ be a smooth positive function and let $\Omega$ be a smooth Kähler form, both defined on a domain in $\mathbb{C}^{n}$ which contains the origin. Consider the $(1,1)$ form
$$\omega=\Omega+i \partial \bar{\partial}\left(F\left|z_{1}\right|^{2 \beta}\right) .$$
Straightforward calculation gives us that
$$i \partial \bar{\partial}\left(F\left|z_{1}\right|^{2 \beta}\right)=\left|z_{1}\right|^{2 \beta} i \partial \bar{\partial} F+\beta\left|z_{1}\right|^{2 \beta-2}\left(\bar{z}_{1} i d z_{1} \wedge \bar{\partial} F+z_{1} i \partial F \wedge d \bar{z}_{1}\right)+\beta^{2}\left|z_{1}\right|^{2 \beta-2} F i d z_{1} \wedge d \bar{z}_{1} .$$
Let $I$ be the complex structure of $\mathbb{C}^{n}$ and $g=\omega(., I$.$) . Let v_{1}, \ldots, v_{n}$ be as in 2.3. We want to compute $g_{i \bar{j}}=g\left(v_{i}, \bar{v}_{j}\right)$. Write $\Omega=\sum_{i, j=1}^{n} \Omega_{i \bar{j}} i d z_{i} \wedge d \bar{z}_{j}$. Note that the coefficients $\Omega_{i \bar{j}}$ are given by the contraction of $\Omega$ with the standard coordinate vectors $\partial / \partial z_{i}, \partial / \partial \bar{z}_{j}$, while to obtain $g_{i \bar{j}}$ we must contract $g$ with $v_{i}, \bar{v}_{j}$. It is easy to check that
$$\begin{gathered}
g_{1 \overline{1}}=\left|z_{1}\right|^{2-2 \beta} \Omega_{1 \overline{1}}+\left|z_{1}\right|^{2} \frac{\partial^{2} F}{\partial z_{1} \partial \bar{z}_{1}}+\beta\left(z_{1} \frac{\partial F}{\partial z_{1}}+\bar{z}_{1} \frac{\partial F}{\partial \bar{z}_{1}}\right)+\beta^{2} F ; \\
g_{1 \bar{j}}=\left|z_{1}\right|^{1-\beta} \Omega_{1 \bar{j}}+\left|z_{1}\right|^{1+\beta} \frac{\partial^{2} F}{\partial z_{1} \partial \bar{z}_{j}}+\beta\left|z_{1}\right|^{\beta-1}\left(z_{1} \frac{\partial F}{\partial z_{j}}+\bar{z}_{1} \frac{\partial F}{\partial \bar{z}_{j}}\right) \quad \text { for } j \geq 2 ; \\
g_{j \bar{k}}=\Omega_{j \bar{k}}+\left|z_{1}\right|^{2 \beta} \frac{\partial^{2} F}{\partial z_{j} \partial \bar{z}_{k}} \quad \text { for } j, k \geq 2 .
\end{gathered}$$
It is then clear that if $\left|z_{1}\right|$ is sufficiently small, then $g$ defines a $C^{\alpha}$ Kähler metric with $\alpha=\beta^{-1}-1$.
There is a useful way of thinking of $g$, due to J. Sturm -see [9], Lemma 3.14- : On $\mathbb{C}^{n+1}$ with standard complex coordinates $\left(z_{1}, \ldots, z_{n+1}\right)$ consider the $(1,1)$ form
$$\Gamma=\Omega+i \partial \bar{\partial}\left(F\left|z_{n+1}\right|^{2}\right) .$$

This form defines a smooth Kähler metric on $\mathbb{C}^{n+1}$ in a neighbourhood of 0. Let us delete a ray in the complex plane corresponding to the $z_{1}$ variable and define
$$\Phi\left(z_{1}, \ldots, z_{n}\right)=\left(z_{1}, \ldots, z_{n}, z_{1}^{\beta}\right),$$
so that $\omega=\Phi^{*} \Gamma$. The pull-back of $\Gamma$ by $\Phi$ is independent of the branch of $z_{1}^{\beta}$ that we take and we can think of the metric $g$ in the complement of $D$ as the restriction of the smooth metric defined by $\Gamma$ to a smooth complex hyper-surface in $\mathbb{C}^{n+1}$. A well-known principle says that the holomorphic sectional curvature of a complex submanifold of a Kähler manifold is less or equal than that of the ambient manifold, see Section 0.5 in Griffiths-Harris [6]. We conclude that we can restrict $g$ to a smaller neighbourhood of 0 if necessary so that its sectional curvature is uniformly bounded above. \(\square\)

It is easy to check that $[\omega]=[\Omega]$ as de Rham co-homology classes. We refer to $\omega$ as the 'standard reference metric'. It follows from the computations in the appendix of [7] that the sectional curvature of $\omega$ is unbounded below at $D$; it then follows that the same holds for its Ricci curvature. We remark that this negative curvature phenomena is not inherent to the cone singularities, it is a consequence of the particular definition of $\omega$. A good example to have in mind is the following: Let $a$ be a real number with $|a|<1$. Consider the metric defined in the unit disc of the complex numbers,
$$g_{a}=\left(a+\left|z_{1}\right|^{2 \beta-2}\right)\left|d z_{1}\right|^{2} .$$
Its Gaussian curvature is given by
$$K_{a}=-4(\beta-1)^{2} a \frac{\left|z_{1}\right|^{2-4 \beta}}{\left(1+\left|z_{1}\right|^{2-2 \beta} a\right)^{3}} .$$
If $1 / 2<\beta<1$, then $K_{a}$ is unbounded below when $a>0$ and unbounded above if $a<0$. In higher dimensions we can take the product of $g_{a}$ with a flat euclidean factor $\mathbb{C}^{n-1}$.

For reference in the future; we recall that on a Kähler manifold there are the notions of sectional curvature, holomorphic sectional curvature and bisectional curvature. A uniform (upper or lower) bound in any of these three implies a uniform (upper or lower) bound on the other two.

\section*{3. Proof of Theorem 1}

Consider the functional $H$ given by
$$H(\phi)=\log \frac{\omega_{\phi}^{n}}{\omega^{n}},$$
where $\omega_{\phi}=\omega+i \partial \bar{\partial} \phi$; it is defined in a suitable neighbourhood of 0 in $C^{2, \alpha^{\prime}}(X)$ and takes values in $C^{\alpha^{\prime}}(X)$. Let $v=\int_{X} \omega^{n}$ and $M=\left\{h \in C^{\alpha^{\prime}}(X)\right.$ s.t. $\left.\int_{X} e^{h} \omega^{n}=v\right\}$; integration by parts shows that $\int_{X} \omega_{\phi}^{n}=\int_{X} \omega^{n}$ and therefore $H(\phi) \in M$ for any $\phi$. Clearly $H(0)=0$; standard computations show that $H$ is $C^{1}$ and that its derivative at 0 agrees with $\Delta_{g}$. Write $T_{0} M=\left\{\psi \in C^{\alpha^{\prime}}(X)\right.$ s.t. $\left.\int_{X} \psi \omega^{n}=0\right\}$ for the tangent space of $M$ at 0; and let $L=\left\{\phi \in C^{2, \alpha^{\prime}}(X)\right.$ s.t. $\left.\int_{X} \phi \omega^{n}=0\right\}$. It follows from Theorem 3 and the Implicit Function Theorem that $H$ defines a diffeomorphism between small neighborhoods of 0 , say $U \subset L$ and $V \subset M$. We can assume that $U \subset B(0, \epsilon)$, the ball centred at the origin of radius $\epsilon$; and that $B(0,2 \mu) \cap M \subset V$ for some $\mu>0$.

On the other hand, a standard formula in Kähler geometry tells us that, in the complement of $D$
$$\operatorname{Ric}\left(\omega_{\phi}\right)-\operatorname{Ric}(\omega)=-i \partial \bar{\partial} H(\phi) ;$$
and
$$\operatorname{Ric}(\omega)-\operatorname{Ric}(\Omega)=i \partial \bar{\partial} \log \frac{\Omega^{n}}{\omega^{n}}=i \partial \bar{\partial} \log \frac{|s|_{h}^{2 \beta-2} \Omega^{n}}{\omega^{n}}+(1-\beta) i \partial \bar{\partial} \log |s|_{h}^{2}$$
Since $\omega$ is a $C^{\alpha}$ metric, the function
$$F=\log \frac{|s|_{h}^{2 \beta-2} \Omega^{n}}{\omega^{n}}$$
belongs to $C^{\alpha}(X)$. Since $\alpha^{\prime}<\alpha$, there is $\tilde{h} \in B(0, \mu) \subset C^{\alpha^{\prime}}(X)$ such that $F-\tilde{h}$ is a smooth function on $X$ with respect to the complex coordinates. Note that $e^{-\mu} v \leq \int_{X} e^{\tilde{h}} \omega^{n} \leq e^{\mu} v$, so we can add a constant to $\tilde{h}$ to get $h \in V$ such that $F-h$ is smooth. Write $h=H(\phi)$ with $\phi \in U ; 3.2$ together with 3.3 give us
$$\operatorname{Ric}\left(\omega_{\phi}\right)=\operatorname{Ric}(\Omega)+(1-\beta) i \partial \bar{\partial} \log |s|_{h}^{2}+i \partial \bar{\partial}(F-H(\phi)) .$$
Note that $i \partial \bar{\partial} \log |s|_{h}^{2}$ extends as a smooth 2-form on $X$, indeed it is the standard representative for $-2 \pi c_{1}(\Lambda)$. Theorem 1 then follows from 3.4

For the sake of clarity we remark that in the proof we use standard derivatives in the complement of $D$. If we were using currents and working globally on $X$; then we would have to include the term $2 \pi(1-\beta)[D]$ on the right hand sides of equations 3.3 and 3.4, with $[D]$ the current of integration along $D$.

\section*{4. Proof of Theorem 2}

We prove the case of negative Ricci, the case of Ricci-flat metrics goes along the same lines; the major difference is in the $C^{0}$ estimate, in which Moser iteration is used instead of the maximum principle. There are no difficulties in extending the Moser iteration technique to the setting of metrics with cone singularities, for the details we refer to [2]. We concentrate on the existence part; the uniqueness follows from the maximum principle -see [8]-.

The hypothesis that $c_{1}(X)-(1-\beta) c_{1}([D])<0$ implies that there is a smooth Kähler form $\Omega$ such that $-(2 \pi)^{-1}[\Omega]=c_{1}(X)-(1-\beta) c_{1}([D])$. Take $s$ to be a holomorphic section of $\Lambda$ such that $s^{-1}(0)=D$ and let $h$ be a smooth Hermitian metric on $\Lambda$. Fix $\delta>0$ so that we have the reference metric $\omega=\Omega+\delta i \partial \bar{\partial}|s|_{h}^{2 \beta}$ of Proposition 1.

Claim 1. There is a $C^{\alpha}$ function $f$ on $X$, smooth in the complement of $D$, such that $\operatorname{Ric}(\omega)=-\omega+i \partial \bar{\partial} f$. We refer to $f$ as the Ricci potential of $\omega$.

Proof. The co-homology condition on $\Omega$ implies that there is a smooth function $F$ on $X$ with $i \partial \bar{\partial} F=$ $\Omega+\operatorname{Ric}(\Omega)+(1-\beta) i \partial \bar{\partial} \log |s|_{h}^{2}$. We use that $\operatorname{Ric}(\omega)-\operatorname{Ric}(\Omega)=i \partial \bar{\partial} \log \left(\Omega^{n} / \omega^{n}\right)$ to obtain
$$\operatorname{Ric}(\omega)=\operatorname{Ric}(\Omega)+i \partial \bar{\partial} \log \left(\frac{\Omega^{n}}{\omega^{n}}\right)=i \partial \bar{\partial} F-\Omega-i \partial \bar{\partial} \log \left(\frac{|s|_{h}^{2-2 \beta} \omega^{n}}{\Omega^{n}}\right)=-\omega+i \partial \bar{\partial} f ;$$
where
$$f=F+\delta|s|_{h}^{2 \beta}-\log \left(\frac{|s|_{h}^{2-2 \beta} \omega^{n}}{\Omega^{n}}\right) .$$
Since $\omega$ is $C^{\alpha}$, we see that $f$ is a smooth function in the complement of $D$ which extends as a $C^{\alpha}$ function to $X$ with $\alpha=(1 / \beta)-1$. \(\square\)

We want to find $u \in C^{2, \alpha}$ a solution of
$$(\omega+i \partial \bar{\partial} u)^{n}=e^{f+u} \omega^{n} .$$
It is easy to argue that if we set $\omega_{K E}=\omega+i \partial \bar{\partial} u$, then $\omega_{K E}$ defines a Kähler metric with cone angle $2 \pi \beta$ along $D$ and $\operatorname{Ric}\left(\omega_{K E}\right)=-\omega_{K E}$ in the complement of $D$. In order to solve 4.1 we use the Aubin-Yau continuity method. A novel feature is that the path we use doesn't start at the reference metric $\omega$.

We start the continuity path with a metric whose Ricci potential is a smooth function rather than $C^{\alpha}$, to obtain the initial metric we proceed as in the proof of Theorem 1. From now on we fix $\alpha<(1 / \beta)-1$. Consider the functional $\mathcal{F}: U \rightarrow C^{\alpha}$, where $U$ is a neighbourhood of 0 in $C^{2, \alpha}$ and $\mathcal{F}(\phi)=\log \left(\omega_{\phi}^{n} / \omega^{n}\right)-\phi$. It is clear that $\mathcal{F}(0)=0$ and that the derivative at 0 is given by $D_{0} \mathcal{F}(\phi)=\triangle_{g} \phi-\phi$. Integration by parts shows that $D_{0} \mathcal{F}$ has no kernel, so that the Implicit Function Theorem together with Theorem 3 imply that there is $\epsilon>0$ such that for every $h \in C^{\alpha}$ with $\|h\|_{\alpha}<\epsilon$ there is $\phi \in C^{2, \alpha}$ with $\mathcal{F}(\phi)=h$. There is a function $f_{0}$, smooth in the complex coordinates, such that $\left\|f-f_{0}\right\|_{\alpha}<\epsilon$. We let $h=f-f_{0}$ and take $\phi \in C^{2, \alpha}$ with $\mathcal{F}(\phi)=h$, so that $\omega_{\phi}$ satisfies $\omega_{\phi}^{n}=e^{h+\phi} \omega^{n}$; hence $\operatorname{Ric}\left(\omega_{\phi}\right)=-\omega_{\phi}+i \partial \bar{\partial} f_{0}$.

Set $\omega_{0}=\omega_{\phi}$. To solve equation 4.1 it is enough to find $u_{1} \in C^{2, \alpha}$ such that $\left(\omega_{0}+i \partial \bar{\partial} u_{1}\right)^{n}=e^{f_{0}+u_{1}} \omega_{0}^{n}$; so then $u=\phi+u_{1}$ is the solution of 4.1. We use the path
$$\left(\omega_{0}+i \partial \bar{\partial} u_{t}\right)^{n}=e^{t f_{0}+u_{t}} \omega_{0}^{n}$$
and consider the set
$$T=\left\{t \in[0,1] \text { such that there is } u_{t} \in C^{2, \alpha}\right. \text { solving 4.2 }$$
We start at $t=0$ with $u_{0}=0$. The goal is to show that $T$ is open and closed.
Theorem 3 implies that $T$ is open. The fact that $T$ is closed, and hence Theorem 2, follows from the following a priori estimate:

Proposition 2. There is a constant $C$, independent of $t \in T$, such that $\left\|u_{t}\right\|_{2, \alpha} \leq C$.
The proof of Proposition 2 is divided into three steps:
Step 1. $C^{0}$-estimate This is an application of the maximum principle. If $u_{t}$ attains its maximum at $p \in X \backslash D$ then 4.2 implies that $t f_{0}(p)+u_{t}(p) \leq 0$, so that $\sup u_{t} \leq \max \left\{-\inf f_{0}, 0\right\}$. If the maximum is attained at $p \in D$ then one considers $\tilde{u}_{t}=u_{t}+\delta|s|_{h}^{\epsilon}$ for a suitable choice of $\delta$ and $\epsilon$ positive and small. The function $\tilde{u}_{t}$ attains its maximum outside $D$, one gets a uniform upper bound on the supreme of $\tilde{u}_{t}$-see [8]-which indeed implies a uniform upper bound on $\sup u_{t}$. Similarly one gets a uniform lower bound on inf $u_{t}$. As a result $\left\|u_{t}\right\|_{0} \leq C$.

Step 2. $C^{2}$-estimate Write $\omega_{t}=\omega_{0}+i \partial \bar{\partial} u_{t}$, then 4.2 implies that $\operatorname{Ric}\left(\omega_{t}\right)=-\omega_{t}+(1-t) i \partial \bar{\partial} f_{0}$. Since $f_{0}$ is smooth, there is a constant $C_{2}>0$ such that $i \partial \bar{\partial} f_{0} \geq-C_{2} \omega$. Set $C_{1}=1$ so that $\operatorname{Ric}\left(\omega_{t}\right) \geq-C_{1} \omega_{t}-C_{2} \omega$. On the other hand, the reference metric $\omega$ has bisectional curvature bounded above, so there is $C_{3}>0$ such that $\operatorname{Bisec}(\omega) \leq C_{3}$.

Write $\tilde{u}_{t}=\phi+u_{t}$, so that $\omega_{t}=\omega+i \partial \bar{\partial} \tilde{u}_{t}$. Let $A=C_{2}+2 C_{3}+1$; the Chern-Lu inequality -see [7]- tells us that
$$\triangle_{\omega_{t}}\left(\operatorname{tr}_{\omega_{t}} \omega-A \tilde{u}_{t}\right) \geq-C_{1}-A n+\operatorname{tr}_{\omega_{t}} \omega .$$
We already have a uniform bound on $\left\|\tilde{u}_{t}\right\|_{0}$. We use 4.3 and the maximum principle (as in the previous step), together with the estimate on $\left\|\tilde{u}_{t}\right\|_{0}$, to get the uniform bound $\operatorname{tr}_{\omega_{t}} \omega \leq C$. This bound together with 4.2 imply that $C^{-1} \omega \leq \omega_{t} \leq C \omega$.

Step 3. $C^{2, \alpha}$-estimate This is a local result. We appeal to the 'interior Schauder estimates for the complex Monge-Ampere operator'. In the case that $\beta=1$ (no cone singularities) there is a large literature on this topic; we mention, among others, the work of Caffarelli and Safanov for the real Monge-Ampere operator. More recently, Chen-Wang - [3]- gave a new proof of these estimates by means of a 'blow-up' argument, similar in spirit to Leon Simon's proof of the Schauder estimates for the Laplace operator [10]. This technique works in the setting of metrics with cone singularities. Our previous $C^{2}$ estimate together with Theorem 1.7 in [3] gives us that $\|u\|_{2, \alpha} \leq C$. Alternatively; we can refer to Evans-Krillov theory and its analogue for metrics with cone singularities, see [7].

\section*{References}
\begin{itemize}
\item[] [1] Alberto Arezzo, Claudio; Della Vedova and Gabriele La Nave. On the curvature of conic Kahler-Einstein metrics. preprint.
\item[] [2] Simon Brendle. Ricci flat Kähler metrics with edge singularities. Int. Math. Res. Not. IMRN, (24):5727-5766, 2013.
\item[] [3] Xiuxiong Chen and Yuanqi Wang. $c^{2, \alpha}$-estimate for Monge-Ampère equations with Hölder-continuous right hand side. Annals of Global Analysis and Geometry, 49(2):195-204, 2016.
\item[] [4] Martin de Borbon. Asymptotically conical Ricci-flat Kähler metrics with cone singularities. PhD thesis, Imperial College, London, UK, 2015.
\item[] [5] S. K. Donaldson. Kähler metrics with cone singularities along a divisor. In Essays in mathematics and its applications, pages 49-79. Springer, Heidelberg, 2012.
\item[] [6] Phillip Griffiths and Joseph Harris. Principles of algebraic geometry. John Wiley \& Sons, 2014.
\item[] [7] Thalia Jeffres, Rafe Mazzeo, and Yanir A. Rubinstein. Kähler-Einstein metrics with edge singularities. Ann. of Math. (2), 183(1):95-176, 2016.
\item[] [8] Thalia D Jeffres. Uniqueness of Kähler-Einstein cone metrics. Publicacions matematiques, pages 437-448, 2000.
\item[] [9] Yanir A Rubinstein. Smooth and singular Kähler-Einstein metrics. Geometric and Spectral Analysis (P. Albin et al., eds.), Contemp. Math, 630:45-138, 2014.
\item[] [10] Leon Simon. Schauder estimates by scaling. Calculus of Variations and Partial Differential Equations, 5(5):391-407, 1997.
\end{itemize}
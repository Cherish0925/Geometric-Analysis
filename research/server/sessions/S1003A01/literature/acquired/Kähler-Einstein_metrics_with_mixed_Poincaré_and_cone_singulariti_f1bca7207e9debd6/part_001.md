---
retention_scope: session
part: 1
total_parts: 2
---

[Part 1/2 of: Kähler-Einstein metrics with mixed Poincaré and cone singularities along a normal crossing divisor]

---
source_file: 1201_0952.pdf
converter: mathpix
format: mmd
---

\title{
KÄHLER-EINSTEIN METRICS WITH MIXED POINCARÉ AND CONE SINGULARITIES ALONG A NORMAL CROSSING DIVISOR
}
by

\author{
Henri Guenancia
}

\begin{abstract}
Let $X$ be a Kähler manifold and $\Delta$ be a $\mathbb{R}$-divisor with simple normal crossing support and coefficients between 1/2 and 1. Assuming that $K_{X}+\Delta$ is ample, we prove the existence and uniqueness of a negatively curved Kahler-Einstein metric on $X \backslash \operatorname{Supp}(\Delta)$ having mixed Poincaré and cone singularities according to the coefficients of $\Delta$. As an application we prove a vanishing theorem for certain holomorphic tensor fields attached to the pair $(X, \Delta)$.
\end{abstract}

\section*{Contents}
Introduction ..... 2
Acknowledgments ..... 4
1. Preliminaries ..... 4
1.1. Notations and definitions ..... 4
1.2. Kähler-Einstein metrics for pairs ..... 5
1.3. The logarithmic case ..... 6
1.4. A priori estimates ..... 8
2. Uniqueness of the Kähler-Einstein metric ..... 9
2.1. Energy classes for quasi-psh functions ..... 9
2.2. From Kähler-Einstein metrics to Monge-Ampère equations ..... 10
3. Statement of the main result ..... 12
4. Proof of the main result ..... 13
4.1. The approximation process ..... 13
4.2. Establishing estimates for $\varphi_{\varepsilon}$ ..... 14
4.2.1. A precise expression of the metric ..... 14
4.2.2. Bounding the curvature from below ..... 16
4.2.3. Bounding the $\omega_{\varepsilon}$-Laplacian of $F_{\varepsilon}$ ..... 19
4.3. End of the proof ..... 21
4.4. Remarks ..... 22
5. A vanishing theorem for holomorphic tensor fields ..... 22
References ..... 29

\section*{Introduction}

Let $X$ be a compact Kähler manifold of dimension $n$, and $\Delta=\sum a_{i} \Delta_{i}$ an effective $\mathbb{R}$-divisor with simple normal crossing support such that the $a_{i}$ 's satisfy the following inequality: $0<a_{i} \leqslant 1$. We write $X_{0}=X \backslash \operatorname{Supp}(\Delta)$.

Our local model is given by the product $X_{\text {mod }}=\left(\mathbb{D}^{*}\right)^{r} \times\left(\mathbb{D}^{*}\right)^{s} \times \mathbb{D}^{n-(s+r)}$ where $\mathbb{D}$ (resp. $\mathbb{D}^{*}$ ) is the disc (resp. punctured disc) of radius $1 / 4$ in $\mathbb{C}$, the divisor being $D_{\text {mod }}=d_{1}\left[z_{1}=\right.$ $0]+\cdots+d_{r}\left[z_{r}=0\right]+\left[z_{r+1}=0\right]+\cdots+\left[z_{r+s}=0\right]$, with $d_{i}<1$. We will say that a metric $\omega$ on $X_{\text {mod }}$ has mixed Poincaré and cone growth (or singularities) along the divisor $D_{\text {mod }}$ if there exists $C>0$ such that
$$C^{-1} \omega_{\bmod } \leqslant \omega \leqslant C \omega_{\bmod }$$
where
$$\omega_{\text {mod }}:=\sum_{j=1}^{r} \frac{i d z_{j} \wedge d \bar{z}_{j}}{\left|z_{j}\right|^{2 d_{j}}}+\sum_{j=r+1}^{s} \frac{i d z_{j} \wedge d \bar{z}_{j}}{\left|z_{j}\right|^{2} \log ^{2}\left|z_{j}\right|^{2}}+\sum_{j=r+s+1}^{n} i d z_{j} \wedge d \bar{z}_{j}$$
is simply the product metric of the standard cone metric on $\left(\mathbb{D}^{*}\right)^{r}$, the Poincaré metric on $\left(\mathbb{D}^{*}\right)^{s}$, and the euclidian metric on $\mathbb{D}^{n-(s+r)}$.

This notion makes sense for global (Kähler) metrics $\omega$ on the manifold $X_{0}$; indeed, we can require that on each trivializing chart of $X$ where the pair $(X, \Delta)$ becomes $\left(X_{\text {mod }}, D_{\text {mod }}\right)$ (those charts cover $X$ ), $\omega$ is equivalent to $\omega_{\text {mod }}$ just like above, and this does not depend on the chosen chart.

Our goal will then be to find, whenever this is possible, Kähler metrics on $X_{0}$ having constant Ricci curvature and mixed Poincaré and cone growth along $\Delta$. Those metrics will naturally be called Kähler-Einstein metrics. For reasons which will appear in section 1.2 and more precisely in Remark 1.3, we will restrict ourselves to looking for Kähler-Einstein metrics with negative curvature.

The existence of Kähler-Einstein metrics (in the previously specified sense) has already been studied in various contexts and for multiple motivations. The logarithmic case (all coefficients of $\Delta$ are equal to 1) has been solved when $K_{X}+\Delta$ is assumed to be ample by R. Kobayashi [Kob84] and G.Tian-S.T.Yau [TY87], the latter considering also orbifold coefficients for the fractional part $\Delta_{k l t}=\sum_{\left\{a_{i}<1\right\}} a_{i} \Delta_{i}$ of $\Delta$, that is of the form $1-\frac{1}{m}$ for some integers $m>1$. Our main result extends this when the coefficients of $\Delta_{k l t}$ are no longer orbifold coefficients, but are any real numbers $a_{i} \geqslant 1 / 2$ (condition which is realized if $a_{i}$ is of orbifold type):

Theorem A. - Let $X$ be a compact Kähler manifold and $\Delta=\sum a_{i} \Delta_{i}$ a $\mathbb{R}$-divisor with simple normal crossing support such that $K_{X}+\Delta$ is ample. We assume furthermore that the coefficients of $\Delta$ satisfy the following inequalities:
$$1 / 2 \leqslant a_{i} \leqslant 1 .$$
Then $X \backslash \operatorname{Supp}(\Delta)$ carries a unique Kähler-Einstein metric $\omega_{K E}$ with curvature -1 having mixed Poincaré and cone singularities along $\Delta$.

The conic case, ie when the coefficients of $\Delta$ are stricly less than 1), under the assumption that $K_{X}+\Delta$ is positive or zero, has been studied by R. Mazzeo [Maz99], T. Jeffres [Jef00] and recently resolved independently by S. Brendle [Bre11] and R. Mazzeo, T. Jeffres, Y. Rubinstein [JMR11] in the case of an (irreducible) smooth divisor, and by [CGP11] in the general case of a simple normal crossing divisor (having though all its coefficients greater than $\frac{1}{2}$ ). In the
conic case where $K_{X}+\Delta<0$, some interesting existence results were obtained by R. Berman in [Ber11] and T. Jeffres, R. Mazzeo and Y. Rubinstein in [JMR11]. Let us finally mention that in [JMR11], it is proved that the potential of the Kähler-Einstein metric has polyhomogeneous expansion, which is much stronger than the assertion on the cone singularities of this metric.

Let us now give a sketch of the proof by detailing the organization of the paper.
The first step is, as usual, to relate the existence of Kähler-Einstein metrics to some particular Monge-Ampère equations. We explain this link in Proposition 2.5. The idea is that any negatively curved normalized Kähler-Einstein metric on $X_{0}$ with appropriate boundary conditions extends to a Kähler current of finite energy in $c_{1}\left(K_{X}+\Delta\right)$ satisfying on $X$ a Monge-Ampère equation of the type $\omega_{\varphi}^{n}=e^{\varphi-\varphi \Delta} \omega^{n}$ where $\omega$ is a Kähler form on $X$, and $\varphi_{\Delta}=\sum a_{i} \log \left|s_{i}\right|^{2}+$ (smooth terms). One may observe that as soon as some $a_{i}$ equals 1, the measure $e^{-\varphi \Delta} \omega^{n}$ has infinite mass.

The uniqueness of the solution metric will then follow from the so-called comparison principle established by V.Guedj and A.Zeriahi for this special class of finite energy currents.

We are then reduced to solving some singular Monge-Ampère equation. The strategy consists in working on the open manifold $X_{l c}:=X \backslash \Delta_{l c}$, and we are led to the following equation: $\omega_{\varphi}^{n}=e^{\varphi-\varphi \Delta_{k l t}} \omega^{n}$ where this time $\omega$ is a Kähler form on $X_{l c}$ with Poincaré singularities along $\Delta_{l c}$, and $\varphi_{\Delta_{k l t}}=\sum_{\left\{a_{i}<1\right\}} a_{i} \log \left|s_{i}\right|^{2}+$ (smooth terms). If $\varphi_{\Delta_{k l t}}$ were smooth, one could simply apply the results of Kobayashi and Tian-Yau. As it is not the case, we adapt the strategy of Campana-Guenancia-Păun to this setting:

We start in section 4.1 by regularizing $\varphi_{\Delta_{k l t}}$ into a smooth function (on $X_{l c}$ ) $\varphi_{\Delta_{k l t}, \varepsilon}$ and introducing smooth approximations $\omega_{\varepsilon}$ of the cone metric on $X_{l c}$ having Poincaré singularities along $\Delta_{l c}$. Then we consider the regularized equation $\omega_{\varphi_{\varepsilon}}^{n}=e^{\varphi_{\varepsilon}-\varphi_{\Delta_{k l t}, e}} \omega_{\varepsilon}^{n}$ which we can solve for every $\varepsilon>0$ (we are in the logarithmic case). The point is to construct our desired solution $\varphi$ as the limit of $\left(\varphi_{\varepsilon}\right)_{\varepsilon}$; this is made possible by controlling (among other things) the curvature of $\omega_{\varepsilon}$, and applying appropriate a priori laplacian estimates which we briefly explain in section 1.4. The final step is standard: it consists in invoking Evans-Krylov $\mathscr{C}^{2, \alpha}$ interior estimates, and concluding that $\varphi$ is smooth on $X_{0}$ using Schauder estimates.

In the last part of the paper, and as in [CGP11], we try to use the Kähler-Einstein metric constructed in the previous sections to obtain the vanishing of some particular holomorphic tensors attached to a pair $(X, \Delta), \Delta$ being still a $\mathbb{R}$-divisor with simple normal crossing support and having coefficients in [0, 1]. This specific class consists in the holomorphic tensors which are the global sections of the locally free sheaf $T_{s}^{r}(X \mid \Delta)$ introduced by Campana in [Cam10]: they are holomorphic tensors with prescribed zeros or poles along $\Delta$. Thanks to their realization as bounded tensors with respect to some (or equivalently, any) twisted metric $g$ with mixed cone and Poincaré singularities along $\Delta$, given in Proposition 5.3 we can use Theorem A to prove the following:

Theorem B. - Let $(X, \Delta)$ be a pair satisfying the assumptions of Theorem $A$. Then, there is no non-zero holomorphic tensor of type ( $r, s$ ) whenever $r \geqslant s+1$ :
$$H^{0}\left(X, T_{s}^{r}(X \mid \Delta)\right)=0 .$$

The proof of this results follows closely the one of its analogue in [CGP11]: we use a Bochner formula applied to the truncated holomorphic tensors, and the key point is to control the error
term. However, a new difficulty pops up here, namely we have to deal with an additional term coming from the curvature of the line bundle $\mathcal{O}_{X}(\lfloor\Delta\rfloor)$; fortunately, it has the right sign.

\section*{Acknowledgments}

I am very grateful to Sébastien Boucksom for his patient and careful reading of the preliminary versions, and his several highly valuable comments and suggestions to improve both the organization and the content of this paper.
I would like to also thank warmly Mihai Păun for the precious help he gave me to elaborate the last section of this article.

\section*{1. Preliminaries}

In this first section devoted to the preliminaries, we intend to fix the notations and the scope of this paper. We also recall some useful objects introduced in [Kob84] and [TY87] within the framework of the logarithmic case; finally, we explain briefly some a priori estimates which are going to be some of our main tools in the proof of the main theorem.
1.1. Notations and definitions. - All along this work, $X$ will be a compact Kähler manifold of complex dimension $n$. We will consider effective $\mathbb{R}$-divisors $\Delta=\sum a_{i} \Delta_{i}$ with simple normal crossing support, and such that their coefficients $a_{i}$ belong to [0, 1].
It will be practical to separate the hypersurfaces $\Delta_{i}$ appearing with coefficient 1 in $\Delta$ from the other ones. For this, we write:
$$\begin{aligned}
\Delta & =\sum_{\left\{a_{i}<1\right\}} a_{i} \Delta_{i}+\sum_{\left\{a_{i}=1\right\}} \Delta_{i} \\
& =\Delta_{k l t}+\Delta_{l c}
\end{aligned}$$
These notations come from the framework of the pairs in birational geometry; klt stands for Kawamata log-terminal whereas lc means log-canonical. In this language, $(X, \Delta)$ is called a logsmooth lc pair, and $\left(X, \Delta_{k l t}\right)$ is a log-smooth klt pair. Apart from these practical notations, we will not use this terminology.

We will denote by $s_{i}$ a section of $\mathcal{O}_{X}\left(\Delta_{i}\right)$ whose zero locus is the (smooth) hypersurface $\Delta_{i}$, and, omitting the dependance in the metric, we write $\Theta\left(\Delta_{i}\right)$ the curvature form of $\left(\mathcal{O}_{X}\left(\Delta_{i}\right), h_{i}\right)$ for some hermitian metric on $\mathcal{O}_{X}\left(\Delta_{i}\right)$. Up to scaling the $h_{i}$ 's, one can assume that $\left|s_{i}\right| \leqslant e^{-1}$, and we will make this assumption all along the paper. Finally, we set $X_{0}:=X \backslash \operatorname{Supp}(\Delta)$ and $X_{l c}:=X \backslash \operatorname{Supp}\left(\Delta_{l c}\right)$.

In the introduction, we introduced a natural class of growth of Kähler metrics near the divisor $\Delta$ which we called metrics with mixed Poincaré and cone singularities along $\Delta$. They are the Kähler metrics locally equivalent to the model metric $\omega_{\text {mod }}=\sum_{j=1}^{r} \frac{i d z_{j} \wedge d \bar{z}_{j}}{\left|z_{j}\right|^{2 d_{j}}}+\sum_{j=r+1}^{s} \frac{i d z_{j} \wedge d \bar{z}_{j}}{\left|z_{j}\right|^{2} \log ^{2}\left|z_{j}\right|^{2}}+$ $\sum_{j=r+s+1}^{n} i d z_{j} \wedge d \bar{z}_{j}$ whenever the pair $(X, \Delta)$ is locally isomorphic to $\left(X_{\text {mod }}, D_{\text {mod }}\right)$ with $X_{\text {mod }}=$ $\left(\mathbb{D}^{*}\right)^{r} \times\left(\mathbb{D}^{*}\right)^{s} \times \mathbb{D}^{n-(s+r)}$ and $D_{\text {mod }}=d_{1}\left[z_{1}=0\right]+\cdots+d_{r}\left[z_{r}=0\right]+\left[z_{r+1}=0\right]+\cdots+\left[z_{r+s}=0\right]$, with $d_{i}<1$.
The following elementary lemma ensures that given a pair $(X, \Delta)$ as above, Kähler metrics with mixed Poincaré and cone singularities along $\Delta$ always exist:

Lemma 1.1. - The following (1, 1)-form
$$\omega_{\Delta}:=\omega_{0}+\sum_{\left\{a_{i}<1\right\}} d d^{c}\left|s_{i}\right|^{2\left(1-a_{i}\right)}-\sum_{\left\{a_{i}=1\right\}} d d^{c} \log \log \frac{1}{\left|s_{i}\right|^{2}}$$
defines a Kähler form on $X_{0}$ as soon as $\omega_{0}$ is a sufficiently positive Kähler metric on $X$. Moreover, it has mixed Poincaré and cone singularities along $\Delta$.

Proof. - This can be seen by a simple computation: combine e.g. [Cla08, Proposition 2.1] with [CG72, Proposition 2.1] or [Gri76, Proposition 2.17]. \(\square\)

Before we end this paragraph, we would like to emphasize the different role played by the $\Delta_{i}$ 's whether they appear in $\Delta$ with coefficient 1 or stricly less than 1. Here is some explanation: let $0<\alpha<1$ be a real number, and $\omega_{\alpha}=\frac{(1-\alpha)^{2} i d z \wedge d \bar{z}}{|z|^{2 \alpha}\left(1-|z|^{2(1-\alpha)}\right)^{2}}$; its curvature is constant equal to -1 on the punctured disc $\mathbb{D}^{*}$, and it has a cone singularity along the divisor $\alpha[0]$. Then, when $\alpha$ goes to $1, \omega_{\alpha}$ converges pointwise to the Poincaré metric $\omega_{P}=\frac{i d z \wedge d \bar{z}}{|z|^{2} \log ^{2}|z|^{2}}$.

In the following, any pair $(X, \Delta)$ will be implicitely assumed to be composed of a compact Kähler manifold $X$ and a $\mathbb{R}$-divisor $\Delta$ on $X$ having simple normal crossing support and coefficients belonging to [0, 1].
1.2. Kähler-Einstein metrics for pairs. - As explained in the introduction, the goal of this paper is to find a Kähler metric on $X_{0}$ with constant Ricci curvature, and having mixed Poincaré and cone singularities along the given divisor $\Delta$. The second condition is essential and as important as the first one; the proof of the vanishing theorem for holomorphic tensors in the last section will render an account of this and shall surely convince the reader. Let us state properly the definition:

Definition 1.2. - A Kähler-Einstein metric for a pair $(X, \Delta)$ is defined to be a Kähler metric $\omega$ on $X_{0}$ satisfying the following properties:
\begin{itemize}
\item[-] Ric $\omega=\mu \omega$ for some real number $\mu$;
\item[-] $\omega$ has mixed Poincaré and cone singularities along $\Delta$.
\end{itemize}

Remark 1.3. - Unlike cone singularities, Poincaré singularities are intrinsically related to negative curvature geometry:
\begin{itemize}
\item[-] The Bonnet-Myers Theorem tells us that in the case where $\Delta_{k l t}=0$ (so that we work with complete metrics), there cannot exist Kähler-Einstein metrics in the previous sense with $\mu>0$. However, if $\Delta_{l c}=0$, there may exist Kähler-Einstein metrics with positive curvature, and the question of their existence is often a difficult question (see e.g. [BBE ${ }^{+}$] or [Ber11]).
\item[-] As for the Ricci-flat case $(\mu=0)$, it also has to be excluded. Indeed, there cannot be any Ricci-flat metric on the punctured disc $\mathbb{D}^{*}$ with Poincaré singularity at 0 ; to see this, we write $\omega=\frac{i}{2} e^{2 u} d z \wedge d \bar{z}$ such a metric, and then $u$ has to satisfy the following properties: $u$ is harmonic on $\mathbb{D}^{*}$ and $e^{2 u}$ behaves like $\frac{1}{|z|^{2} \log ^{2}|z|^{2}}$ near 0, up to constants. But it is well-known that any harmonic function $u$ on $\Delta^{*}$ can be written $u=\operatorname{Re}(f)+c \log |z|$ for some holomorphic function $f$ on $\mathbb{D}^{*}$ and some constant $c \in \mathbb{R}$. Clearly, $f$ cannot have an essential singularity at 0; moreover, because of the logarithmic term in the Poincaré metric, $f$ can neither be bounded, nor have a pole at 0 . This ends to show that in general (and
\end{itemize}
for local reasons), there does not exist Ricci-flat Kähler-Einstein metric in the sense of the previous definition (whenever $\Delta_{l c} \neq 0$ ).
For these reasons, we will focus in the following on the case of negative curvature, which we will normalize in $\mu=-1$.
1.3. The logarithmic case. - For the sake of completeness, we will briefly recall in this section the proof of the main result (Theorem 3.1) in the logarithmic case, namely when $\Delta=\Delta_{l c}$, ie when $\Delta_{k l t}=0$. As we already explained, this was achieved by Kobayashi [Kob84] and Tian-Yau [TY87] in a very similar way. In this section, we will assume that $(X, \Delta)$ is logarithmic, so that $X_{0}=X_{l c}$.

We will use the following terminology which is convenient for the following:
Definition 1.4. - We say that a Kähler metric $\omega$ on $X_{0}$ is of Carlson-Griffiths type if there exists a Kähler form $\omega_{0}$ on $X$ such that $\omega=\omega_{0}-\sum_{K} d d^{c} \log \log \frac{1}{\left|s_{k}\right|^{2}}$.

As observed in Lemma 1.1, such a metric always exists, and it has Poincaré singularities along $\Delta$. In [CG72], Carlson and Griffiths introduced such a metric for some $\omega_{0} \in c_{1}\left(K_{X}+\Delta\right)$. The reason why we exhibit this particular class of Kähler metric on $X_{0}$ having Poincaré singularities along $\Delta$ is that we have an exact knowledge on its behaviour along $\Delta$, much more precise that its membership of the previously cited class. For example, Lemma 1.6 mirrors this fact.

We start from a compact Kähler manifold $X$ with a simple normal crossing divisor $\Delta=\sum \Delta_{k}$ such that $K_{X}+\Delta$ is ample. We want to find a Kähler metric $\omega_{\mathrm{KE}}$ on $X_{0}=X \backslash \Delta$ with - Ric $\omega_{\mathrm{KE}}=\omega_{\mathrm{KE}}$, and having Poincaré singularities along $\Delta$. If we temporarily forget the boundary condition, the problem amounts to solve the following Monge-Ampère equation on $X_{0}$ :
$$\left(\omega+d d^{c} \varphi\right)^{n}=e^{\varphi+F} \omega^{n}$$
where $\omega$ is a Kähler metric on $X_{0}$ of Carlson-Griffiths type (cf. Definition 1.4), and $F=$ $-\log \left(\prod\left|s_{k}\right|^{2} \log ^{2}\left|s_{k}\right|^{2} \cdot \omega^{n} / \omega_{0}^{n}\right)+$ (smooth terms on $X$ ) for some Kähler metric $\omega_{0}$ on $X$.

The key point is that $\left(X_{0}, \omega\right)$ has bounded geometry at any order. Let us get a bit more into the details. To simplify the notations, we will assume that $\Delta$ is irreducible, so that locally near a point of $\Delta, X_{0}$ is biholomorphic to $\mathbb{D}^{*} \times \mathbb{D}^{n-1}$, where $\mathbb{D}$ (resp. $\mathbb{D}^{*}$ ) is the unit disc (resp. punctured disc) of $\mathbb{C}$. We want to show that, roughly speaking, the components of $\omega$ in some appropriate coordinates have bounded derivatives at any order. The right way to formalize it consists in introducing quasi-coordinates: they are maps from an open subset $V \subset \mathbb{C}^{n}$ to $X_{0}$ having maximal rank everywhere. So they are just locally invertible, but these maps are not injective in general.
To construct such quasi-coordinates on $X_{0}$, we start from the univeral covering map $\pi: \mathbb{D} \rightarrow \mathbb{D}^{*}$, given by $\pi(w)=e^{\frac{w+1}{w-1}}$. Formally, it sends 1 to 0. The idea is to restrict $\pi$ to some fixed ball $B(0, R)$ with $1 / 2<R<1$, and compose it (at the source) with a biholomorphism $\Phi_{\eta}$ of $\mathbb{D}$ sending 0 to $\eta$, where $\eta$ is a real parameter which we will take close to 1 . If want to write a formula, we set $\Phi_{\eta}(w)=\frac{w+\eta}{1+\eta w}$, so that the quasi-coordinate maps are given by $\Psi_{\eta}=\pi \circ \Phi_{\eta} \times \operatorname{Id}_{\mathbb{D}^{n-1}}: V=B(0, R) \times \mathbb{D}^{n-1} \rightarrow \mathbb{D}^{*}$, with $\Psi_{\eta}\left(v, v_{2}, \ldots, v_{n}\right)=\left(e^{\frac{1+\eta}{1-\eta} \frac{v+1}{v-1}}, v_{2}, \ldots, v_{n}\right)$. Once we have said this, it is easy to see that $X_{0}$ is covered by the images $\Psi_{\eta}(V)$ when $\eta$ goes to 1, and for all the trivializing charts for $X$, which are in finite number. Now, an easy computation shows that the derivatives of the components of $\omega$ with respect to the $v_{i}$ 's are bounded uniformly in $\eta$. This can be thought as a consequence of the fact that the Poincaré metric is invariant by
any biholomorphism of the disc.
At this point, it is natural to introduce the Hölder space of $\mathscr{C}_{q c}^{k, \alpha}$-functions on $X_{0}$ using the previously introduced quasi-coordinates:

Definition 1.5. - For a non-negative integer $k$, a real number $\alpha \in] 0.1[$, we define:
$$\mathscr{C}_{q c}^{k, \alpha}\left(X_{0}\right)=\left\{u \in \mathscr{C}^{k}\left(X_{0}\right) ; \sup _{V, \eta}\left\|u \circ \Psi_{\eta}\right\|_{k, \alpha}<+\infty\right\}$$
where the supremum is taken over all our quasi-coordinate maps $V$ (which cover $X_{0}$ ). Here $\|\cdot\|_{k, \alpha}$ denotes the standard $\mathscr{C}_{q c}^{k, \alpha}$-norm for functions defined on a open subset of $\mathbb{C}^{n}$.

The following fact, though easy, is very important for our matter:
Lemma 1.6. - Let $\omega$ be a Carlson-Griffiths type metric on $X_{0}$, and $\omega_{0}$ some Kähler metric on $X$. Then
$$F_{0}:=\log \left(\prod\left|s_{k}\right|^{2} \log ^{2}\left|s_{k}\right|^{2} \cdot \omega^{n} / \omega_{0}^{n}\right)$$
belongs to the space $\mathscr{C}_{q c}^{k, \alpha}\left(X_{0}\right)$ for every $k$ and $\alpha$.
Proof. - The first remark is that $F_{0}$ is bounded (cf. [Kob84, Lemma 1.(ii)] or the beginning of section 4.2.3), and $F_{0} \in \mathscr{C}_{q c}^{k, \alpha}\left(X_{0}\right)$ if and only if $e^{F_{0}} \in \mathscr{C}_{q c}^{k, \alpha}\left(X_{0}\right)$. So in the following, we will deal with $e^{F_{0}}$.
Then, as the (elementary) computations of Lemma 4.3 show, it is enough to check that the functions on $\mathbb{D}^{*}$ (say with radius 1/2) defined by $z \mapsto \frac{1}{\log |z|^{2}}, z \mapsto|z|^{2} \log |z|^{2}$ and $z \mapsto|z|^{2} \log ^{2}|z|^{2}$ are in $\mathscr{C}_{q c}^{k, \alpha}\left(\mathbb{D}^{*}\right)$. But in the quasi-coordinates given by $\Phi_{\eta}, \frac{1}{\log |z|^{2}}=\frac{1}{2} \cdot \frac{1-\eta}{1+\eta} \frac{|v|^{2}-1}{|v-1|^{2}}$ and $|z|^{2} \log ^{\alpha}|z|^{2}=$ $\left(\frac{1}{2} \cdot \frac{1+\eta}{1-\eta} \frac{|v-1|^{2}}{|v|^{2}-1}\right)^{\alpha} e^{2 \cdot \frac{1+\eta}{1-\eta} \frac{|v|^{2}-1}{|v-1|^{2}}}$, for $v \in B(0, R)$ with $R<1$, and where $\alpha \in \mathbb{R}$. Now there is no difficulty in seeing that these two functions of $v$ are bounded when $\eta$ goes to 1 (actually this property does not depend on the chosen coordinates), and so are their derivatives (still with respect to $v$ ); this is obvious for the first function, and for the second one, it relies on the fact that $x^{m} e^{-x}$ goes to 0 as $x \rightarrow+\infty$, for all $m \in \mathbb{Z}$. \(\square\)

The end of the proof consists in showing that the Monge-Ampère equation $\left(\omega+d d^{c} \varphi\right)^{n}=$ $e^{\varphi+f} \omega^{n}$ has a unique solution $\varphi \in \mathscr{C}_{q c}^{k, \alpha}\left(X_{0}\right)$ for all functions $f \in \mathscr{C}_{q c}^{k, \alpha}\left(X_{0}\right)$ with $k \geqslant 3$. This can be done using the continuity method in the quasi-coordinates. In particular, applying this to $f=F$ (cf beginning of the section), which the previous lemma allows to do, this will prove the existence of a negatively curved Kähler-Einstein metric, which is equivalent to $\omega$ (in the strong sense: $\varphi \in \mathscr{C}_{q c}^{k, \alpha}\left(X_{0}\right)$ for all $k, \alpha$ ).

To summarize, the theorem of Kobayashi and Tian-Yau is the following:
Theorem 1.7. - Let $(X, \Delta)$ be a logarithmic pair, $\omega$ a Kähler form of Carlson-Griffiths type on $X_{0}$, and $F \in \mathscr{C}_{q c}^{k, \alpha}\left(X_{0}\right)$ for some $k \geqslant 3$. Then there exists $\varphi \in \mathscr{C}_{q c}^{k, \alpha}\left(X_{0}\right)$ solution to the following equation:
$$\left(\omega+d d^{c} \varphi\right)^{n}=e^{\varphi+F} \omega^{n}$$
In particular if $K_{X}+\Delta$ is ample, then there exists a (unique) Kähler-Einstein metric of curvature -1 equivalent to $\omega$.
1.4. A priori estimates. - In this section, we recall the classical estimates valid for a large class of complete Kähler manifolds; they are derived from the classical estimates over compact manifolds using the generalized maximum principle of Yau [Yau78]. We will use them in an essential manner in the course of the proof of our main theorem. Indeed, our proof is based upon a regularization process, and in order to guarantee the existence of the limiting object, we need to have a control on the $\mathscr{C}^{k}$ norms.

Theorem 1.8. - Let $X$ be a complete Riemannian manifold with Ricci curvature bounded from below. Let $f$ be a $\mathscr{C}^{2}$ function which is bounded from below on $M$. Then for every $\varepsilon>0$, there exists $x \in X$ such that at $x$,
$$|\nabla f|<\varepsilon, \quad \Delta f>-\varepsilon, \quad f(x)<\inf _{X} f+\varepsilon .$$
From this, we easily deduce the following result, stated in [CY80, Proposition 4.1].
Proposition 1.9. - Let $(X, \omega)$ be a $n$-dimensional complete Kähler manifold, and $F \in \mathscr{C}^{2}(X)$ a bounded function. We assume that we are given $u \in \mathscr{C}^{2}(X)$ satisfying $\omega+d d^{c} u>0$ and
$$\left(\omega+d d^{c} u\right)^{n}=e^{u+F} \omega^{n}$$
Suppose that the bisectional curvature of $(X, \omega)$ is bounded below by some constant, and that $u$ is a bounded function. Then
$$\sup _{X}|u| \leqslant \sup _{X}|F| .$$

We emphasize the fact that the previous estimate does not depend on the lower bound for the bisectional curvature of $(X, \omega)$.
As for the Laplacian estimate, we have the following (we could also have used [CY80, Proposition 4.2]):

Proposition 1.10. - Suppose that the bisectional curvature of $(X, \omega)$ is bounded below by some constant $-B, B>0$, and that $u$ as well as its Laplacian $\Delta u$ are bounded functions on $X$. If $\omega+d d^{c} u$ defines a complete Kähler metric on $X$ with Ricci curvature bounded from below, then
$$\sup _{X}(n+\Delta u) \leqslant C$$
where $C>0$ only depends on $\sup |F|, \inf \Delta F, B$ and $n$.
Sketch of the proof. - We set $\omega^{\prime}=\omega+d d^{c} u$, and $\Delta^{\prime}$ is defined to be the Laplacian with respect to $\omega^{\prime}$.
Using [CGP11, Lemma 2.2], we obtain $\Delta^{\prime}\left(\operatorname{tr}_{\omega} \omega^{\prime}\right) \geqslant \frac{\Delta F}{\operatorname{tr}_{\omega^{\prime}} \omega}-B \operatorname{tr}_{\omega^{\prime}} \omega$, and from this we may deduce that
$$\Delta^{\prime}\left(\operatorname{tr}_{\omega} \omega^{\prime}-\left(C_{1}+1\right) u\right) \geqslant \operatorname{tr}_{\omega^{\prime}} \omega-C_{2}$$
where $C_{1}, C_{2}$ are constant depending only $B, \inf \Delta F$ and $n$. The assumptions allow us to use the generalized maximum principle stated as Theorem 1.8 to show that sup $\operatorname{tr}_{\omega^{\prime}} \omega \leqslant C_{3}$. As $\omega^{\prime}=e^{F+u} \omega$, and as we have at our disposal uniform estimates on sup $|u|$ thanks to 1.9, the usual arguments work here to give a uniform bound $\sup (n+\Delta u) \leqslant C$. We refer e.g. to [CGP11, section 2] for more details. \(\square\)

\section*{2. Uniqueness of the Kähler-Einstein metric}

In this section, we begin to investigate the questions raised in the introduction concerning the existence of Kähler-Einstein metrics for pairs $(X, \Delta)$. The first thing to do is, as usual, to relate the existence of theses metrics to the existence of solutions for some Monge-Ampère equations. We will be in a singular case, so we have to specify the class of $\omega$-psh functions to which we are going to apply the Monge-Ampère operators. This is the aim of the few following lines, where we will recall some recent (but relatively basic) results of pluripotential theory. We refer to [GZ07] or [BEGZ] for a detailed treatment.
2.1. Energy classes for quasi-psh functions. - Let $\omega$ be a Kähler metric on $X$; the class $\mathcal{E}(X, \omega)$ is defined to be composed of $\omega$-psh functions $\varphi$ such that their non-pluripolar Monge-Ampère $\left(\omega+d d^{c} \varphi\right)^{n}$ has full mass $\int_{X} \omega^{n}$ (cf. [GZ07], [BEGZ]). An alternate way to apprehend those functions is to see them as the largest class where one can define $\left(\omega+d d^{c} \varphi\right)^{n}$ as a measure which does not charge pluripolar sets. Those functions satisfy the so-called comparison principle, which we are going to use in an essential manner for the uniqueness of our Kähler-Einstein metric:

Proposition 2.1 (Comparison Principle, [GZ07]). - Let $\varphi, \psi \in \mathcal{E}(X, \omega)$. Then we have:
$$\int_{\{\varphi<\psi\}}\left(\omega+d d^{c} \psi\right)^{n} \leqslant \int_{\{\varphi<\psi\}}\left(\omega+d d^{c} \varphi\right)^{n} .$$

An important subset of $\mathcal{E}(X, \omega)$ is the class $\mathcal{E}^{1}(X, \omega)$ of functions in the class $\mathcal{E}(X, \omega)$ having finite $\mathcal{E}^{1}$-energy, namely $\mathcal{E}^{1}(\varphi):=\int_{X}|\varphi|\left(\omega+d d^{c} \varphi\right)^{n}<+\infty$. Every smooth (or even bounded) $\omega$-psh function belongs to this class.
In order to state an useful result for us, we recall the notion of capacity attached to a compact Kähler manifold $(X, \omega)$, as introduced in [GZ05], generalizing the usual capacity of Bedford-Taylor ([BT82]): for every Borel subset $K$ of $X$, we set:
$$\operatorname{Cap}_{\omega}(K):=\sup \left\{\int_{K} \omega_{\varphi}^{n} ; \varphi \in \operatorname{PSH}(X, \omega), 0 \leqslant \varphi \leqslant 1\right\}$$
There is an useful criteria to show that some $\omega$-psh function belongs to the class $\mathcal{E}^{1}(X, \omega)$ without checking that it has full Monge-Ampère mass, but only using the capacity decay of the sublevel sets. It appears in different papers, among which [GZ07, Lemma 5.1], [BGZ08, Proposition 2.2], [BBGZ09, Lemma 2.9]:

Lemma 2.2. - Let $\varphi \in \operatorname{PSH}(X, \omega)$. If
$$\int_{t=0}^{+\infty} t^{n} \operatorname{Cap}_{\omega}\{\varphi<-t\} d t<+\infty$$
then $\varphi \in \mathcal{E}^{1}(X, \omega)$.
Now we have enough background about these objects to state and prove the result we will use in the next section. Let us first fix the notations.
Let $\left(X, \omega_{0}\right)$ be a Kähler manifold, and $\Delta=\sum_{k \in K} \Delta_{k}$ a simple normal crossing divisor. We choose sections $s_{k}$ of $\mathcal{O}_{X}\left(\Delta_{k}\right)$ whose divisor is precisely $\Delta_{k}$, and we fix some smooth hermitian metrics on those line bundles. We can assume that $\left|s_{k}\right| \leqslant e^{-1}$, and we know that, up to scaling the metrics, one may assume that $\omega_{0}-\sum_{k} d d^{c} \log \log \frac{1}{\left|s_{k}\right|^{2}}$ is positive on $X_{0}$, and defines a Kähler current on $X$.

Proposition 2.3. - The function
$$\varphi_{0}=-\sum_{k \in K} \log \log \frac{1}{\left|s_{k}\right|^{2}}$$
belongs to the class $\mathcal{E}^{1}\left(X, \omega_{0}\right)$.
Proof. - We want to apply Lemma 2.2. To compute the global capacity as defined above, or at least know the capacity decay of the sublevel sets, it is convenient to use the Bedford-Taylor capacity. But a result due to Kołodziej [Koł01] (see also [GZ05, Proposition 2.10]), states that up to universal multiplicative constants, the capacity can be computed by the local Bedford-Taylor capacities on the trivializing charts of $X$.

Therefore, we are led to bound from above $\operatorname{Cap}_{B T}\{u<-t\}$ in the unit polydisc of $\mathbb{C}^{n}$, where $u=\sum_{i=1}^{p}-\log \left(-\log \left|z_{i}\right|^{2}\right)$ for some $p \leqslant n$. As
$$\{u<-t\} \subset \bigcup_{i=1}^{p}\left\{-\log \left(-\log \left|z_{i}\right|^{2}\right)<-\frac{t}{p}\right\}$$
one can now assume that $p=1$. But $\operatorname{Cap}_{B T}\left\{\log |z|^{2}<-t\right)=2 / t$ (see e.g [Dem, Example 13.10]), whence $\operatorname{Cap}_{B T}\left\{-\log \left(-\log \left|z_{i}\right|^{2}\right)<-t\right)=2 e^{-t}$. The result follows. \(\square\)

Remark 2.4. - An alternate way to proceed is to show that the smooth approximations $\varphi_{\varepsilon}:=$ - $\sum_{k \in K} \log \log \frac{1}{\left|s_{k}\right|^{2}+\varepsilon^{2}}$ of $\varphi_{0}$ have (uniformly) bounded $\mathcal{E}^{1}$-energy, which also allows to conclude that $\varphi_{0} \in \mathcal{E}^{1}\left(X, \omega_{0}\right)$ thanks to [BEGZ, Proposition 2.10 \& 2.11].
2.2. From Kähler-Einstein metrics to Monge-Ampère equations. - The following proposition explains how to relate Kähler-Einstein metrics for a pair $(X, \Delta)$ and some Monge-Ampère equations, the difficulty being here that we have to deal with singular weights/potentials for which the definitions and properties of the Monge-Ampère operators are more complicated than in the smooth case. Note that this result generalizes [Ber11, Proposition 5.1]:

Proposition 2.5. - Let $X$ be a compact Kähler manifold, and $\Delta=\sum a_{j} \Delta_{j}$ an effective $\mathbb{R}$ -divisor with simple normal crossing support, such that $a_{j} \leqslant 1$ for all $j$. We assume that $K_{X}+\Delta$ is ample, and we choose a Kähler metric $\omega_{0} \in c_{1}\left(K_{X}+\Delta\right)$. Then any Kähler metric $\omega$ on $X_{0}$ satisfying:
\begin{itemize}
\item[-] $-\operatorname{Ric} \omega=\omega$ on $X_{0}$;
\item[-] There exists $C>0$ such that:
$$C^{-1} \omega^{n} \leqslant \frac{\omega_{0}^{n}}{\prod_{\left\{a_{i}<1\right\}}\left|s_{i}\right|^{2 a_{i}} \prod_{\left\{a_{i}=1\right\}}\left|s_{i}\right|^{2} \log ^{2}\left|s_{i}\right|^{2}} \leqslant C \omega^{n}$$
extends to a Kähler current $\omega=\omega_{0}+d d^{c} \varphi$ on $X$ where $\varphi \in \mathcal{E}^{1}\left(X, \omega_{0}\right)$ is a solution of
$$\left(\omega_{0}+d d^{c} \varphi\right)^{n}=e^{\varphi-\varphi \Delta} \omega_{0}^{n}$$
and $\varphi_{\Delta}=\sum_{r \in J \cup K} a_{r} \log \left|s_{r}\right|^{2}+f$ for some $f \in \mathscr{C}^{\infty}(X)$. Furthermore there exists at most one such metric $\omega$ on $X_{0}$.
\end{itemize}

Remark 2.6. - One can observe that although $e^{\varphi-\varphi \Delta} \omega_{0}^{n}$ has finite mass, $e^{-\varphi \Delta} \omega_{0}^{n}$ does not (as soon as $\Delta_{l c} \neq 0$ ).

Proof. - We recall that $\Theta\left(\Delta_{i}\right)$ denotes the curvature of $\left(\mathcal{O}_{X}\left(\Delta_{i}\right), h_{i}\right)$, and we write $\Theta\left(\Delta_{k l t}\right)=$ $\sum_{\left\{a_{i}<1\right\}} a_{i} \Theta\left(\Delta_{i}\right), \Theta\left(\Delta_{l c}\right)=\sum_{\left\{a_{i}=1\right\}} \Theta\left(\Delta_{i}\right)$ and $\Theta(\Delta)=\Theta\left(\Delta_{k l t}\right)+\Theta\left(\Delta_{l c}\right)$. All those forms are smooth on $X$.
Let us define a smooth function $\psi$ on $X_{0}$ by:
$$\psi_{0}:=\log \left(\frac{\prod_{j \in J}\left|s_{j}\right|^{2 a_{j}} \prod_{k \in K}\left|s_{k}\right|^{2} \log ^{2}\left|s_{k}\right|^{2} \omega^{n}}{\omega_{0}^{n}}\right)$$
By assumption, $\psi_{0}$ is bounded on $X_{0}$, so that $\psi:=\psi_{0}-\sum_{k} \log \log ^{2} \frac{1}{\left|s_{k}\right|^{2}}$ is bounded above on $X_{0}$. On this set, we have
$$d d^{c} \psi=\omega+\operatorname{Ric} \omega_{0}^{n}+\Theta(\Delta)$$
so that $\psi$ is $M \omega_{0}$-psh for some $M>0$ big enough. As it is bounded above, it extends to a (unique) $M \omega_{0}$-psh function on the whole $X$, which we will also denote by $\psi$. Let now $f$ be a smooth potential on $X$ of $\operatorname{Ric} \omega_{0}^{n}+\omega_{0}-\Theta(\Delta)$. It is easily shown that $\varphi:=\psi-f$ satisfies $\omega_{0}+d d^{c} \varphi=\omega$ on $X_{0}$.

From the definition of $\varphi$, we see that $\varphi=2 \varphi_{0}+\mathcal{O}(1)$, where $\varphi_{0}=-\sum_{k \in K} \log \log \frac{1}{\left|s_{k}\right|^{2}}$. Therefore, Proposition 2.3 ensures that $\varphi \in \mathcal{E}^{1}\left(X, \omega_{0}\right)$, so that its non-pluripolar Monge-Ampère $\left(\omega_{0}+\right.$ $\left.d d^{c} \varphi\right)^{n}$ satisfies the equation
$$\begin{aligned}
\left(\omega_{0}+d d^{c} \varphi\right)^{n} & =\frac{e^{\varphi-f} \omega_{0}^{n}}{\prod_{r \in J \cup K}\left|s_{r}\right|^{2 a_{r}}} \\
& =e^{\varphi-\varphi \Delta} \omega_{0}^{n}
\end{aligned}$$
on the whole $X$, with the notations of the statement. By the comparison principle (Proposition 2.1), if the previous equation had two solutions $\varphi, \psi \in \mathcal{E}^{1}\left(X, \omega_{0}\right)$, then on the set $A=\{\varphi<\psi\}$, we would have
$$\int_{A} e^{\psi-\varphi \Delta} \omega_{0}^{n} \leqslant \int_{A} e^{\varphi-\varphi \Delta} \omega_{0}^{n}$$
but on $A, e^{\psi}>e^{\varphi}$ so that $A$ has zero measure with repect to the measure $e^{-\varphi \Delta} \omega_{0}^{n}$, so it has zero measure with respect to $\omega_{0}^{n}$. We can do the same for $B=\{\psi<\varphi\}$, so that $\{\varphi=\psi\}$ has full measure with respect to $\omega_{0}^{n}$. As $\varphi, \psi$ are $\omega_{0}$-psh, they are determined by their data almost everywhere, so they are equal on $X$. This finishes to conclude that our $\varphi$ is unique, so that the proposition is proved. \(\square\)

Remark 2.7. - In the logarithmic case $\left(\Delta=\Delta_{l c}\right)$, the metrics at stake are complete, so that their uniqueness follow from the generalized maximum principle of Yau (cf. [Kob84], [TY87] e.g). In the conic case, Kołodziej's theorem [Ko198] ensures that the potentials we are dealing with are continuous, and the unicity follows from the classical comparison principle established in [BT82, Theorem 4.1].

As Kähler metrics with mixed Poincaré and cone singularities clearly satisfy the second condition of the proposition, we deduce that any negatively curved normalized Kähler-Einstein metric must be obtained by solving the global equation $\left(\omega_{0}+d d^{c} \varphi\right)^{n}=e^{\varphi-\varphi \Delta} \omega_{0}^{n}$ on $X$, for $\varphi \in \mathcal{E}^{1}\left(X, \omega_{0}\right)$, and $\varphi_{\Delta}=\sum_{r \in J \cup K} a_{r} \log \left|s_{r}\right|^{2}+f$ for some $f \in \mathscr{C}^{\infty}(X)$. We will now show how to solve the previous equation, and derive from this the existence of negatively curved Kähler-Einstein metrics and their zero-th order asymptotic along $\Delta$.

\section*{3. Statement of the main result}

Here is a result which encompasses the previous results of [CGP11], Kobayashi ([Kob84]) and Tian-Yau ([TY87]). This provides a (positive) partial answer to a question raised in [CGP11, section 10].

Theorem 3.1. - Let $X$ be a compact Kähler manifold, and $\Delta=\sum a_{i} \Delta_{i}$ an effective $\mathbb{R}$-divisor with simple normal crossing support such that its coefficients satisfy the inequalities:
$$1 / 2 \leqslant a_{i} \leqslant 1 .$$
Then for any Kähler form $\omega$ on $X_{l c}$ of Carlson-Griffiths type and any function $f \in \mathscr{C}_{q c}^{k, \alpha}\left(X_{l c}\right)$ with $k \geqslant 3$, there exists a Kähler metric $\omega_{\infty}=\omega+d d^{c} \varphi$ on $X_{0}$ solution to the following equation:
$$\left(\omega+d d^{c} \varphi\right)^{n}=\frac{e^{\varphi+f}}{\prod_{\left\{a_{i}<1\right\}}\left|s_{i}\right|^{2 a_{i}}} \omega^{n}$$
such that $\omega_{\infty}$ has mixed Poincaré and cone singularities along $\Delta$.
We refer to section 1.3 and more precisely to Definition 1.5 for the definition of the space $\mathscr{C}_{q c}^{k, \alpha}\left(X_{l c}\right)$; one important class of functions belonging to $\mathscr{C}_{q c}^{k, \alpha}\left(X_{l c}\right)$ is pointed out in Lemma 1.6, and we will use it for proving the following result.

Corollary 3.2. - Let $(X, \Delta)$ be a pair such that $\Delta=\sum a_{i} \Delta_{i}$ is a divisor with simple normal crossing support whose coefficients satisfy the inequalities
$$1 / 2 \leqslant a_{i} \leqslant 1 .$$
If $K_{X}+\Delta$ is ample, then $X_{0}$ carries a unique Kähler-Einstein metric $\omega_{K E}$ of curvature -1 having mixed Poincaré and cone singularities along $\Delta$.

Here, by ample, we mean that $c_{1}\left(K_{X}+\Delta\right)$ contains a Kähler metric, or equivalently that $K_{X}+\Delta$ is a positive combination of ample $\mathbb{Q}$-divisors.

Proof. - We choose $\left(h_{i}\right)$ and $h_{K_{X}}$ some smooth hermitian metrics on the line bundles $\mathcal{O}_{X}\left(\Delta_{i}\right)$ and $\mathcal{O}_{X}\left(K_{X}\right)$ respectively such that the product metric $h$ on $K_{X}+\Delta$ has positive curvature $\omega_{0}$, and up to renormalizing the metrics $h_{k}$, one can assume that $\omega:=\omega_{0}-\sum_{\left\{a_{k}=1\right\}} d d^{c} \log \log \frac{1}{\left|s_{k}\right|^{2}}$ defines a Kähler metric on $X_{l c}$ with Poincaré singularities along $\Delta_{l c}$; more precisely it is of Carlson-Griffiths type.
Lemma 1.6 shows that one can write
$$\omega^{n}=\frac{e^{-B} \Psi}{\prod\left|s_{k}\right|^{2} \log ^{2}\left|s_{k}\right|^{2}}$$
with $\Psi$ the smooth volume form on $X$ attached to $h_{K_{X}}$ (in particular $-\operatorname{Ric} \Psi=\Theta_{h_{K_{X}}}\left(K_{X}\right)$, the curvature of $\left(\mathcal{O}_{X}\left(K_{X}\right), h_{K_{X}}\right)$ ), and $B \in \mathscr{C}_{q c}^{k, \alpha}\left(X \backslash \Delta_{l c}\right)$ for all $k$ and $\alpha$.
Now we use Theorem 3.1 with $f=B$, and $\omega$ as reference metric. We then get a Kähler metric $\omega_{\mathrm{KE}}:=\omega+d d^{c} \varphi$ on $X \backslash \operatorname{Supp}(\Delta)$ with mixed Poincaré and cone singularities along $\Delta$ satisfying
$$\left(\omega+d d^{c} \varphi\right)^{n}=\frac{e^{\varphi+B}}{\prod_{j \in J}\left|s_{j}\right|^{2 a_{j}}} \omega^{n} .$$

Therefore,
$$\begin{aligned}
-\operatorname{Ric}\left(\omega_{\mathrm{KE}}\right)= & d d^{c}(\varphi+B)-d d^{c} B+\Theta_{h_{K_{X}}}\left(K_{X}\right)-\sum_{k \in K}\left(d d^{c} \log \left|s_{k}\right|^{2}-d d^{c} \log \log \frac{1}{\left|s_{k}\right|^{2}}\right) \\
& -\sum_{j \in J} d d^{c} \log \left|s_{j}\right|^{2 a_{j}} \\
= & d d^{c} \varphi+\Theta\left(K_{X}\right)+\Theta\left(\Delta_{l c}\right)+\Theta\left(\Delta_{k l t}\right)-\sum_{k \in K} d d^{c} \log \log \frac{1}{\left|s_{k}\right|^{2}} \\
= & \omega_{\mathrm{KE}} .
\end{aligned}$$
Moreover, $\omega_{\mathrm{KE}}$ has mixed Poincaré and cone singularities along $\Delta$, so it is a Kähler-Einstein metric for the pair $(X, \Delta)$.
As for the uniqueness of $\omega_{\mathrm{KE}}$, it follows directly from Proposition 2.5. \(\square\)

\section*{4. Proof of the main result}

As we explained in the introduction, the natural strategy is to combine the approaches of [CGP11] and Kobayashi ([Kob84]). More precisely we will produce a sequence of Kähler metrics $\left(\omega_{\varepsilon}\right)_{\varepsilon}$ on $X \backslash \Delta_{l c}$ having Poincaré singularities along $\Delta_{l c}$ and acquiring cone singularities along $\Delta_{k l t}$ at the end of the process when $\varepsilon=0$.
4.1. The approximation process. - We keep the notation of Theorem 3.1, so that $\omega$ is a Kähler form on $X_{l c}$ of Carlson-Griffiths type; in particular it has Poincaré singularities along $\Delta_{l c}$.
We define, for any sufficiently small $\varepsilon>0$, a Kähler form $\omega_{\varepsilon}$ on $X_{l c}$ by
$$\omega_{\varepsilon}:=\omega+d d^{c} \psi_{\varepsilon}$$
where $\psi_{\varepsilon}=\frac{1}{N} \sum_{\left\{a_{j}<1\right\}} \chi_{j, \varepsilon}\left(\varepsilon^{2}+\left|s_{j}\right|^{2}\right)$ for $\chi_{j, \varepsilon}$ functions defined by:
$$\chi_{j, \varepsilon}\left(\varepsilon^{2}+t\right)=\frac{1}{\tau_{j}} \int_{0}^{t} \frac{\left(\varepsilon^{2}+r\right)^{\tau_{j}}-\varepsilon^{2 \tau_{j}}}{r} d r$$
for any $t \geqslant 0$. The important facts to remember about this construction are the following ones, extracted from [CGP11, section 3]:
\begin{itemize}
\item[-] For $N$ big enough, $\omega_{\varepsilon}$ dominates (as a current) a Kähler form on $X$ because $\omega$ already does;
\item[-] $\psi_{\varepsilon}$ is uniformly bounded (on $X$ ) in $\varepsilon$;
\item[-] When $\varepsilon$ goes to $0, \omega_{\varepsilon}$ converges on $X_{l c}$ to $\omega_{\Delta}$ having mixed Poincaré and cone singularities along $\Delta$.
\end{itemize}

As $\omega_{\varepsilon}$ is a Kähler metric on $X_{l c}$ with Poincaré singularities along $\Delta_{l c}$, the case $J=\emptyset$ treated by Kobayashi ([Kob84]) and Tian-Yau ([TY87]), cf section 1.3, Theorem 1.7, enables us to find a smooth $\omega_{\varepsilon}$-psh function $\varphi_{\varepsilon}$ on $X_{l c}$ satisfying:
$$\left(\omega_{\varepsilon}+d d^{c} \varphi_{\varepsilon}\right)^{n}=e^{\varphi_{\varepsilon}+F_{\varepsilon}} \omega_{\varepsilon}^{n}$$
where
$$F_{\varepsilon}=f+\psi_{\varepsilon}+\log \left(\frac{\omega^{n}}{\prod_{j \in J}\left(\left|s_{j}\right|^{2}+\varepsilon^{2}\right)^{a_{j}} \omega_{\varepsilon}^{n}}\right)$$
belongs to $\mathscr{C}_{q c}^{k, \alpha}\left(X_{l c}\right)$ thanks to Lemma 1.6 and the assumptions on $f$. We may insist on the fact that the relation $F_{\varepsilon} \in \mathscr{C}_{q c}^{k, \alpha}\left(X_{l c}\right)$ is only qualitative in the sense that we a priori don't have uniform estimates on $\left\|F_{\varepsilon}\right\|_{k, \alpha}$.
Besides, $\varphi_{\varepsilon} \in \mathscr{C}_{q c}^{k, \alpha}\left(X_{l c}\right)$ (cf. [Kob84, section 3]) so that in particular, it is bounded on $X_{l c}$, $\omega_{\varepsilon}+d d^{c} \varphi_{\varepsilon}$ defines a complete Kähler metric on $X_{l c}$, and the Ricci curvature of $\omega_{\varepsilon}+d d^{c} \varphi_{\varepsilon}$ bounded (from below) if and only if the one of $\omega_{\varepsilon}$ is bounded (from below). Note that the bounds may a priori not be uniform in $\varepsilon$ - however we will show that this is the case.
Once observed that $\omega_{\varepsilon}$ converges to a Kähler metric with mixed Poincaré and cone singularities along $\Delta$, and that equation (1) is equivalent to
$$\left(\omega+d d^{c}\left(\varphi_{\varepsilon}+\psi_{\varepsilon}\right)\right)^{n}=\frac{e^{f+\left(\varphi_{\varepsilon}+\psi_{\varepsilon}\right)}}{\prod_{j \in J}\left(\left|s_{j}\right|^{2}+\varepsilon^{2}\right)^{a_{j}}} \omega^{n}$$
the proof of our theorem boils down to showing that one can extract a subsequence of $\left(\varphi_{\varepsilon}\right)_{\varepsilon}$ converging to $\varphi$, smooth outside $\Delta$, and such that $\omega+d d^{c} \varphi$ has the expected singularities along $\Delta$.
4.2. Establishing estimates for $\varphi_{\varepsilon}$. - In view of the a priori estimates of section 1.4, we first need to find a bound $\sup \left|\varphi_{\varepsilon}\right| \leqslant C$. We will see at the beginning of section 4.2.3 that $\sup _{\varepsilon} \sup _{X}\left|F_{\varepsilon}\right|$ is finite. Therefore, using 1.9 with $\omega_{\varepsilon}$ as reference metric, we have the desired $\mathscr{C}^{0}$ estimate: $\sup \left|\varphi_{\varepsilon}\right| \leqslant \sup _{\varepsilon} \sup _{X}\left|F_{\varepsilon}\right|$. So it remains to check that (here uniformly means "uniformly in $\varepsilon$ "):
\begin{itemize}
\item[(i)] The bisectional curvature of $\left(X_{l c}, \omega_{\varepsilon}\right)$ is uniformly bounded from below;
\item[(ii)] $F_{\varepsilon}$ is uniformly bounded;
\item[(iii)] The Laplacian of $F_{\varepsilon}$ with respect to $\omega_{\varepsilon}, \Delta_{\omega_{\varepsilon}} F_{\varepsilon}$, is uniformly bounded.
\end{itemize}

Once we will have shown that conditions $(i)-(i i i)$ hold, we will get the existence of $C>0$ such that for all $\varepsilon>0, \operatorname{tr}_{\omega_{\varepsilon}}\left(\omega_{\varepsilon}+d d^{c} \varphi_{\varepsilon}\right) \leqslant C$ (by the remarks above, $\omega_{\varepsilon}+d d^{c} \varphi_{\varepsilon}$ is complete and will have Ricci curvature bounded from below so that the assumptions of Proposition 1.10 are fulfilled). Therefore, we will have $\omega_{\varepsilon}+d d^{c} \varphi_{\varepsilon} \leqslant C \omega_{\varepsilon}$. Furthermore, as $\varphi_{\varepsilon}$ and $F_{\varepsilon}$ will be bounded, the identity $\left(\omega_{\varepsilon}+d d^{c} \varphi_{\varepsilon}\right)^{n}=e^{\varphi_{\varepsilon}+F_{\varepsilon}} \omega_{\varepsilon}^{n}$ joint with the basic inequality $\operatorname{det}_{\omega_{\varepsilon}}\left(\omega_{\varepsilon}+d d^{c} \varphi_{\varepsilon}\right)$. $\operatorname{tr}_{\omega_{\varepsilon}+d d^{c} \varphi_{\varepsilon}}\left(\omega_{\varepsilon}\right) \leqslant\left(\operatorname{tr}_{\omega_{\varepsilon}}\left(\omega_{\varepsilon}+d d^{c} \varphi_{\varepsilon}\right)\right)^{n-1}$ (which amounts to saying that $\sum_{|I|=n-1} \prod_{i \in I} \lambda_{i} \leqslant$ $\left(\sum_{i=1}^{n} \lambda_{i}\right)^{n-1}$ ) will imply that, up to increasing $C, \operatorname{tr}_{\omega_{\varepsilon}+d d^{c} \varphi_{\varepsilon}}\left(\omega_{\varepsilon}\right) \leqslant C$. Therefore,
$$C^{-1} \omega_{\varepsilon} \leqslant \omega_{\varepsilon}+d d^{c} \varphi_{\varepsilon} \leqslant C \omega_{\varepsilon}$$
and passing to the limit (after choosing a subsequence so that $\left(\varphi_{\varepsilon}\right)_{\varepsilon}$ converges to $\varphi$ smooth outside $\operatorname{Supp}(\Delta)$ - we skip some important details here, cf. section 4.3) our solution $\omega_{o}+d d^{c} \varphi$ will have mixed Poincaré and cone singularities along $\Delta$.
4.2.1. A precise expression of the metric. - Before we go any further, we have to give the explicit local expresssions of $\omega_{\varepsilon}$. We recall that $\Delta=\sum_{j \in J} a_{j} \Delta_{j}+\sum_{k \in K} \Delta_{k}$ for some disjoints sets $J, K \subset \mathbb{N}$, such that for all $j \in J, a_{j}<1$. In the following, an index $j$ (resp. $k$ ) will always be assumed to belong to $J$ (resp. $K$ ).
First of all, pick some point $p_{0} \in X$ sitting on $\operatorname{Supp}(\Delta)$. We choose a neighborhood $U$ of $p_{0}$ trivializing $X$ and such that $\operatorname{Supp}(\Delta) \cap U=\left\{\prod_{J_{U}} z_{j} \cdot \prod_{K_{U}} z_{k}=0\right\}$ for some $J_{U} \subset J$ and $K_{U} \subset K$. Then if $i \notin J_{U} \cup K_{U}, \Delta_{i}$ does not meet $U$. To simplify the notations, one may suppose that $J_{U}=\{1, \ldots, r\}$ and $K_{U}=\{r+1, \ldots, d\}$. Finally, we stress the point that although $p_{0} \in \operatorname{Supp}(\Delta)$, all our computations will be done on $U \cap X_{l c}=U \backslash \operatorname{Supp}\left(\Delta_{l c}\right)$.

So as to simplify the computations, we will use the following (more or less basic) lemma, extracted from [CGP11, Lemma 4.1]:

Lemma 4.1. - Let $\left(L_{1}, h_{1}\right), \ldots,\left(L_{d}, h_{d}\right)$ be a set of hermitian line bundles on a compact Kähler manifold $X$, and for each index $j=1, \ldots, d$, let $s_{j}$ be a section of $L_{j}$; we assume that the hypersurfaces
$$Y_{j}:=\left(s_{j}=0\right)$$
are smooth, and that they have strictly normal intersections. Let $p_{0} \in \bigcap Y_{j}$; then there exist a constant $C>0$ and an open set $V \subset X$ centered at $p_{0}$, such that for any point $p \in V$ there exists a coordinate system $z=\left(z_{1}, \ldots, z_{n}\right)$ at $p$ and a trivialization $\theta_{j}$ for $L_{j}$ such that:
\begin{itemize}
\item[(i)] For $j=1, \ldots, d$, we have $Y_{j} \cap V=\left(z_{j}=0\right)$;
\item[(ii)] With respect to the trivialization $\theta_{j}$, the metric $h_{j}$ has the weight $\varphi_{j}$, such that
$$\varphi_{j}(p)=0, \quad d \varphi_{j}(p)=0, \quad\left|\frac{\partial^{|\alpha|+|\beta|} \varphi_{j}}{\partial z_{\alpha} \partial \bar{z}_{\beta}}(p)\right| \leqslant C_{\alpha, \beta}$$
for all multi indexes $\alpha, \beta$.
\end{itemize}

Up to shrinking the neighborhood $V$, we may assume that each coordinate system $\left(z_{1}, \ldots, z_{n}\right)$ for $V$, as given in Lemma 4.1, satisfies $\sum_{i}\left|z_{i}\right|^{2} \leqslant 1 / 2$. Moreover, in order to make the notations clearer, we define, for $i \in\{1, \ldots, n\}$, a non-negative function on $V$ (depending on $\varepsilon$ ) by
$$A(i)= \begin{cases}\left(\left|z_{i}\right|^{2}+\varepsilon^{2}\right)^{a_{i} / 2} & \text { if } i \in\{1, \ldots, r\} ; \\ \left|z_{i}\right| \log \frac{1}{\left|z_{i}\right|^{2}} & \text { if } i \in\{r+1, \ldots, d\} ; \\ 1 & \text { if } i<d .\end{cases}$$
Now, for $i, j, k, l \in\{1, \ldots, n\}$, we simply set $A(i, j, k, l):=A(i) A(j) A(k) A(l)$.
We first want to check that the holomorphic bisectional curvature of $\omega_{\varepsilon}$ is bounded from below, that is
$$\Theta_{\omega_{\varepsilon}}\left(T_{X}\right) \geqslant-C \omega_{\varepsilon} \otimes \operatorname{Id}_{T_{X}}$$
for some $C>0$ independent of $\varepsilon$, and where $\Theta_{\omega_{\varepsilon}}\left(T_{X}\right)$ denotes the curvature tensor of the holomorphic tangent bundle of $\left(X_{l c}, \omega_{\varepsilon}\right)$. It is useful for the following to reformulate the (intrinsic) condition (2) in terms of local coordinates. Namely, the inequality in (2) amounts to saying that the following inequality holds:
$$\sum_{p, q, r, s} R_{p \bar{q} r \bar{s}}(z) v_{p} \overline{v_{q}} w_{r} \overline{w_{s}} \geqslant-C|v|_{\omega_{\varepsilon}}^{2}|w|_{\omega_{\varepsilon}}^{2}$$
for any vector fields $v=\sum_{p} v_{p} \frac{\partial}{\partial z_{p}}$ and $w=\sum_{r} w_{r} \frac{\partial}{\partial z_{r}}$.
The notation in the above relations is as follows: in local coordinates, we write
$$\omega_{\varepsilon}=\frac{i}{2} \sum_{p, q} g_{p \bar{q}} d z_{p} \wedge d \bar{z}_{q} ;$$
(so that the $g_{p \bar{q}}$ 's actually depend on $\varepsilon$, but we choose not to let it appear in the notations so as to make them a bit lighter) and the corresponding components of the curvature tensor are
$$R_{p \bar{q} r \bar{s}}:=-\frac{\partial^{2} g_{p \bar{q}}}{\partial z_{r} \partial \bar{z}_{s}}+\sum_{k, l} g^{k \bar{l}} \frac{\partial g_{p \bar{k}}}{\partial z_{r}} \frac{\partial g_{l \bar{q}}}{\partial \bar{z}_{s}} .$$

Looking at the local expression of $\omega_{\varepsilon}$ makes it clear that there exists $C>0$ independent of $\varepsilon$ such that on $V, C^{-1} \omega_{\Delta, \varepsilon} \leqslant \omega_{\varepsilon} \leqslant C \omega_{\Delta, \varepsilon}$, where
$$\omega_{\Delta, \varepsilon}:=\sum_{j=1}^{r} \frac{i d z_{j} \wedge d \bar{z}_{j}}{\left(\left|z_{j}\right|^{2}+\varepsilon^{2}\right)^{a_{j}}}+\sum_{k=r+1}^{d} \frac{i d z_{k} \wedge d \bar{z}_{k}}{\left|z_{k}\right|^{2} \log ^{2}\left|z_{k}\right|^{2}}+\sum_{l=d}^{n} i d z_{l} \wedge d \bar{z}_{l}$$
Therefore, if $v=\sum_{p} v_{p} \frac{\partial}{\partial z_{p}}$ satisfies $|v|_{\omega_{\varepsilon}}=1$, then for each $p,\left|v_{p}\right| \leqslant A(p)$. We are now going to show the following two facts, which will ensure that the holomorphic bisectional curvature of $\omega_{\varepsilon}$ is bounded from below:
\begin{itemize}
\item[(i)] For every four-tuple $(p, q, r, s)$ with $\#\{p, q, r, s\} \geqslant 2$, we have $A(p, q, r, s)\left|R_{p \bar{q} r \bar{s}}(z)\right| \leqslant C$;
\item[(ii)] For every $p$, and every $\omega_{\varepsilon}$-unitary vector fields $v, w,\left|v_{p}\right|_{\omega_{\varepsilon}}^{2}\left|w_{p}\right|_{\omega_{\varepsilon}}^{2} R_{p \bar{p} p \bar{p}} \geqslant-C$.
\end{itemize}

In order to prove $(i)-(i i)$, we have to give a precise expression of the metric $\omega_{\varepsilon}$ in some coordinate chart. We will use the coordinates given by Lemma 4.1, which will simplify the computations a lot. We remind that $\omega_{\varepsilon}=\omega+d d^{c} \psi_{\varepsilon}$, and according to [CGP11, equation (21)] and Definition 1.4 (or [Gri76, pp. 50-51]), the components $g_{p \bar{q}}$ of $\omega_{\varepsilon}$ are given by:
$$\begin{aligned}
g_{p \bar{q}} & =u_{p \bar{q}}+\frac{\delta_{p q, J} e^{-\varphi_{p}}}{\left(\left|z_{p}\right|^{2} e^{-\varphi_{p}}+\varepsilon^{2}\right)^{a_{p}}}+\delta_{p, J} e^{-\varphi_{p}} \frac{\bar{z}_{p} \overline{\alpha_{q p}}}{\left(\left|z_{p}\right|^{2} e^{-\varphi_{p}}+\varepsilon^{2}\right)^{a_{p}}}+\delta_{q, J} e^{-\varphi_{q}} \frac{z_{q} \alpha_{q p}}{\left(\left|z_{q}\right|^{2} e^{-\varphi_{q}}+\varepsilon^{2}\right)^{a_{q}}} \\
4) & +\sum_{j \in J} \frac{\left|z_{j}\right|^{2} \beta_{j p q}}{\left(\left|z_{j}\right|^{2} e^{-\varphi_{j}}+\varepsilon^{2}\right)^{a_{j}}}\left(\left(\left|z_{j}\right|^{2} e^{-\varphi_{j}}+\varepsilon^{2}\right)^{1-a_{j}}-\varepsilon^{2\left(1-a_{j}\right)}\right) \frac{\partial^{2} \varphi_{j}}{\partial z_{p} \partial \bar{z}_{q}} \\
& +\delta_{p q, K} \frac{i d z_{p} \wedge d \bar{z}_{p}}{\left|z_{p}\right|^{2} \log ^{2}\left|z_{p}\right|^{2}}+\frac{\delta_{p, K} \lambda_{p}}{z_{p} \log ^{2}\left|z_{p}\right|^{2}}+\frac{\delta_{q, K} \mu_{q}}{\bar{z}_{q} \log ^{2}\left|z_{q}\right|^{2}}+\sum_{k=r+1}^{d} \frac{\nu_{k}}{\log \left|z_{k}\right|^{2}}
\end{aligned}$$
where $u_{p q}, \alpha_{p q}, \beta_{j p q}, \lambda_{p}, \mu_{q}, \nu_{k}$ are smooth functions on $X$ (more precisely on the whole neighborhood $V$ of $p$ in $X$ given by Lemma 4.1). Moreover, $\alpha, \lambda, \mu$ (resp. $\beta$ ) are functions of the partial derivatives of the $\varphi_{i}$ 's; in particular, they vanish at the given point $p$ at order at least 1 (resp. 2). Finally, we use the notation $\delta_{p, J}=\delta_{p \in J}$ and $\delta_{p q, J}=\delta_{p q} \delta_{p \in J}$ (idem for $K$ instead of $J$ ).
4.2.2. Bounding the curvature from below. - First of all, using (4), and remembering that $\alpha, \beta, \lambda, \mu$, vanish at $p$, on can give a precise 0-order estimate on the metric (more precisely on the inverse matrix of the metric), which is a straightforward generalization of [CGP11, Lemma 4.2]:

Lemma 4.2. - In our setting, and for $|z|^{2}+\varepsilon^{2}$ sufficiently small, we have at the previously chosen point $p$ :
\begin{itemize}
\item[(i)] For all $i \in\{1, \ldots, n\}, \quad g^{i \bar{i}}=A(i)^{2}\left(1+\mathcal{O}\left(A(i)^{2}\right)\right)$;
\item[(ii)] For all $j, k \in\{1, \ldots, n\}$ such that $j \neq k, \quad g^{j \bar{k}}=\mathcal{O}\left(A(j, k)^{2}\right)$.
\end{itemize}

We insist on the fact that the $\mathcal{O}$ symbol refers to the expression $|z|^{2}+\varepsilon^{2}=\left|z_{1}\right|^{2}+\cdots+\left|z_{n}\right|^{2}+\varepsilon^{2}$ going to zero.

To bound the curvature, we will essentially have to deal with the Poincaré part of $\omega_{\varepsilon}$, the other cone part being almost already treated in [CGP11]. We could use the fact that $\left(X_{l c}, \omega\right)$ has bounded geometry at any order (cf section 1.3), but as mixed terms involving the (regularized) cone metric will appear - which is not known to be of bounded geometry-, we prefer to give the explicit computations for more clarity.

For $\lambda$ and $\mu$ any smooth functions on $V$, there exist smooth functions $\lambda_{1}, \lambda_{2}, \ldots$ and $\mu_{1}, \mu_{2}, \ldots$ such that for any $k \in K$ :
$$\begin{aligned}
\frac{\partial}{\partial z_{k}}\left(\frac{\lambda}{z_{k} \log ^{2}\left|z_{k}\right|^{2}}\right) & =\frac{\lambda_{1}}{z_{k} \log ^{2}\left|z_{k}\right|^{2}}+\frac{\lambda_{2}}{z_{k}^{2} \log ^{2}\left|z_{k}\right|^{2}}+\frac{\lambda_{3}}{z_{k}^{2} \log ^{3}\left|z_{k}\right|^{2}}=\mathcal{O}\left(\frac{1}{\left|z_{k}\right|^{2} \log ^{2}\left|z_{k}\right|^{2}}\right) \\
\frac{\partial}{\partial \bar{z}_{k}}\left(\frac{\lambda}{z_{k} \log ^{2}\left|z_{k}\right|^{2}}\right) & =\frac{\lambda_{4}}{z_{k} \log ^{2}\left|z_{k}\right|^{2}}+\frac{\lambda_{5}}{\left|z_{k}\right|^{2} \log ^{3}\left|z_{k}\right|^{2}}=\mathcal{O}\left(\frac{1}{\left|z_{k}\right|^{2} \log ^{3}\left|z_{k}\right|^{2}}\right) \\
\frac{\partial^{2}}{\partial z_{k} \partial \bar{z}_{k}}\left(\frac{\lambda}{z_{k} \log ^{2}\left|z_{k}\right|^{2}}\right) & =\frac{\lambda_{6}}{z_{k} \log ^{2}\left|z_{k}\right|^{2}}+\frac{\lambda_{7}}{\left|z_{k}\right|^{2} \log ^{3}\left|z_{k}\right|^{2}}+\frac{\lambda_{8}}{z_{k}^{2} \log ^{2}\left|z_{k}\right|^{2}}+ \\
& +\frac{\lambda_{9}}{z_{k}\left|z_{k}\right|^{2} \log ^{3}\left|z_{k}\right|^{2}}+\frac{\lambda_{10}}{z_{k}^{2} \log ^{3}\left|z_{k}\right|^{2}}+\frac{\lambda_{11}}{z_{k}\left|z_{k}\right|^{2} \log ^{4}\left|z_{k}\right|^{2}} \\
& =\mathcal{O}\left(\frac{1}{\left|z_{k}\right|^{3} \log ^{3}\left|z_{k}\right|^{2}}\right) \\
\frac{\partial}{\partial z_{k}}\left(\frac{\mu}{\log \left|z_{k}\right|^{2}}\right) & =\frac{\mu_{1}}{\log \left|z_{k}\right|^{2}}+\frac{\mu_{2}}{z_{k} \log ^{2}\left|z_{k}\right|^{2}}=\mathcal{O}\left(\frac{\mu}{\left.\left|\log ^{2}\right| z_{k}\right|^{2}}\right) \\
& =\frac{\mu_{3}}{\left.\left|\log ^{2}\right| z_{k}\right|^{2}}+\frac{\mu_{4}}{\bar{z}_{k} \log ^{2}\left|z_{k}\right|^{2}}=\mathcal{O}\left(\frac{1}{\left|z_{k}\right| \log ^{2}\left|z_{k}\right|^{2}}\right) \\
& =\frac{\mu_{5}}{\log ^{2}\left|z_{k}\right|^{2}}+\frac{\mu_{6}}{\bar{z}_{k} \log ^{2}\left|z_{k}\right|^{2}}+\frac{\mu_{7}}{z_{k} \log ^{2}\left|z_{k}\right|^{2}}+\frac{\mu_{8}}{\left|z_{k}\right|^{2} \log ^{3}\left|z_{k}\right|^{2}} \\
\frac{\partial}{\partial z_{k}}\left(\frac{1}{\left|z_{k}\right|^{2} \log ^{2}\left|z_{k}\right|^{2}}\right) & =\frac{1}{z_{k}\left|z_{k}\right|^{2} \log ^{2}\left|z_{k}\right|^{2}}+\frac{-2}{z_{k}\left|z_{k}\right|^{2} \log ^{3}\left|z_{k}\right|^{2}}=\mathcal{O}\left(\frac{1}{\left|z_{k}\right|^{3} \log ^{2}\left|z_{k}\right|^{2}}\right) \\
\frac{\partial^{2}}{\partial z_{k} \partial \bar{z}_{k}}\left(\frac{1}{\left|z_{k}\right|^{2} \log ^{2}\left|z_{k}\right|^{2}}\right) & =\frac{1}{\left|z_{k}\right|^{4} \log ^{2}\left|z_{k}\right|^{2}}+\frac{4}{\left|z_{k}\right|^{4} \log ^{3}\left|z_{k}\right|^{2}}+\frac{6}{\left|z_{k}\right|^{4} \log ^{4}\left|z_{k}\right|^{2}}
\end{aligned}$$

As we are mostly interested in the Poincaré part of the metric $g$, we will write $g=g^{(P)}+g^{(C)}$ its decomposition into the Poincaré and the cone part (cf. the expression (4)). Moreover, we write $g^{(P)}=\gamma^{0}+\gamma$ where $\gamma^{0}=\sum_{k \in K} \frac{i d z_{k} \wedge d \bar{z}_{k}}{\left|z_{k}\right|^{2} \log ^{2}\left|z_{k}\right|^{2}}$. Therefore, if $k \neq l, g_{k \bar{l}}^{(P)}=\gamma_{k \bar{l}}$, and the computations above lead to (for every $k, l, r, s \in K$ ):
$$\begin{array}{rlr}
\frac{\partial g_{k \bar{l}}^{(P)}}{\partial z_{k}}=\mathcal{O}\left(\frac{1}{A(k)^{2} A(l)}\right) & \text { if } k \neq l \\
\frac{\partial^{2} g_{k \bar{l}}^{(P)}}{\partial z_{k} \partial \bar{z}_{r}}=\mathcal{O}\left(\frac{1}{A(k)^{2} A(r, l)}\right) & \text { if } k \neq l \\
\frac{\partial \gamma_{k \bar{l}}}{\partial z_{r}}=\mathcal{O}\left(\frac{1}{A(k, l, r)}\right) & \\
\frac{\partial^{2} \gamma_{k \bar{l}}}{\partial z_{r} \partial \bar{z}_{s}}=\mathcal{O}\left(\frac{1}{A(k, l, r, s)}\right) &
\end{array}$$
Furthermore, we may note that if $\{p, q, r, s\} \cap J=\emptyset$, then we can see from the expression (4) that $\frac{\partial g_{p \bar{q}}}{\partial z_{r}}=\frac{\partial g_{p \bar{q}}^{(P)}}{\partial z_{r}}+\mathcal{O}(1)$ as well as $\frac{\partial^{2} g_{p \bar{q}}}{\partial z_{r} \partial \bar{z}_{s}}=\frac{\partial g_{p \bar{q}}^{(P)}}{\partial z_{r} \partial \bar{z}_{s}}+\mathcal{O}(1)$. From this, (5)-(6) and Lemma 4.2, we deduce that for every $p, q, r, s \in K$ such that $p \neq q$, the expression $A(p, q, r, s) R_{p \bar{q} r \bar{s}}(z)$ is
uniformly bounded in $z \in V \cap X_{l c}$.
So it remains to study the terms of the form $R_{p \bar{p} r \bar{s}}$ for $p, r, s \in K$. And as mentionned in the last paragraph, the terms in the curvature tensor coming from the cone part (or the smooth part) do not play any role here, so we have:
$$\begin{aligned}
R_{p \bar{p} r \bar{s}} & =-\frac{\partial^{2} g_{p \bar{p}}}{\partial z_{r} \partial \bar{z}_{s}}+\sum_{1 \leqslant k, l \leqslant n} g^{k \bar{l}} \frac{\partial g_{p \bar{l}}}{\partial z_{r}} \frac{\partial g_{k \bar{p}}}{\partial \bar{z}_{s}} \\
& =-\frac{\partial^{2}}{\partial z_{r} \partial \bar{z}_{s}}\left(\frac{1}{\left|z_{p}\right|^{2} \log ^{2}\left|z_{p}\right|^{2}}\right)-\frac{\partial^{2} \gamma_{p \bar{p}}}{\partial z_{r} \partial \bar{z}_{s}}+\sum_{1 \leqslant k, l \leqslant n} g^{k \bar{l}} \frac{\partial g_{p \bar{l}}^{(P)}}{\partial z_{r}} \frac{\partial g_{k \bar{p}}^{(P)}}{\partial \bar{z}_{s}}+\mathcal{O}(1)
\end{aligned}$$
Using (5)-(8) and Lemma 4.2, we see that the only possibly unbounded terms (when multiplied by $A(p)^{2} A(r, s)$ ) appearing in the expansion of $R_{p \bar{p} r \bar{s}}$ are coming from $\gamma_{0}$. More precisely, these are the following ones, appearing in $R_{p \bar{p} \bar{p} \bar{p}}$ only:
$$-\frac{\partial^{2}}{\partial z_{p} \partial \bar{z}_{p}}\left(\frac{1}{\left|z_{p}\right|^{2} \log ^{2}\left|z_{p}\right|^{2}}\right)+\sum_{p \in\{k, l\}} g^{k \bar{l}} \frac{\partial g_{p \bar{l}}^{(P)}}{\partial z_{p}} \frac{\partial g_{k \bar{p}}^{(P)}}{\partial \bar{z}_{p}}$$

Let us now expand the terms under the sum:
$$\begin{aligned}
\frac{\partial g_{k \bar{p}}^{(P)}}{\partial z_{p}} & =\mathcal{O}\left(\frac{1}{\left|z_{p}\right|^{2} \log ^{3}\left|z_{p}\right|^{2}}\right) \quad \text { if } k \neq p \\
\frac{\partial g_{p \bar{p}}^{(P)}}{\partial z_{p}} & =\frac{-1}{z_{p}\left|z_{p}\right|^{2} \log ^{2}\left|z_{p}\right|^{2}}+\frac{-2}{z_{p}\left|z_{p}\right|^{2} \log ^{3}\left|z_{p}\right|^{2}}+\mathcal{O}\left(\frac{1}{\left|z_{k}\right|^{2} \log ^{3}\left|z_{k}\right|^{2}}\right) \\
\left|\frac{\partial g_{p \bar{p}}^{(P)}}{\partial z_{p}}\right|^{2} & =\frac{1}{\left|z_{p}\right|^{6} \log ^{4}\left|z_{p}\right|^{2}}\left(1+\frac{4}{\log ^{2}\left|z_{k}\right|^{2}}+\frac{4}{\log ^{2}\left|z_{k}\right|^{2}}+\mathcal{O}\left(\left|z_{k}\right|\right)\right)
\end{aligned}$$
Now, if we combine Lemma 4.2 with (10)-(11), we see that the remaining possibly unbounded terms (after multiplying by $A(p)^{4}$ ) appearing in (9) are
$$-\frac{\partial^{2}}{\partial z_{p} \partial \bar{z}_{p}}\left(\frac{1}{\left|z_{p}\right|^{2} \log ^{2}\left|z_{p}\right|^{2}}\right)+g^{p \bar{p}} \frac{\partial g_{p \bar{p}}^{(P)}}{\partial z_{p}} \frac{\partial g_{p \bar{p}}^{(P)}}{\partial \bar{z}_{p}}$$
which, thanks to point (i) of Lemma 4.2 and (12), happens to be a $\mathcal{O}\left(\frac{1}{\left|z_{p}\right|^{4} \log ^{4}\left|z_{p}\right|^{2}}\right)$, which finishes to prove that for every $p, q, r, s \in K$, the expression $A(p, q, r, s) R_{p \bar{q} r \bar{s}}(z)$ is uniformly bounded in $z \in V \cap X_{l c}$.

Now we may look at the terms $R_{p \bar{q} r \bar{s}}$ where $p, q \in K$ but $r, s \notin K$. If $r, s \notin J$, then $A(p, q, r, s) R_{p \bar{q} r \bar{s}}(z)=A(p, q) R_{p \bar{q} r \bar{s}}(z)$ is uniformly bounded in $z \in V \cap X_{l c}$ as we can see by looking at the expression of the metric (4). So now we may suppose that $r$ or $s$ belongs to $J$. The only term in the metric which may cause trouble is $\sum_{j \in J} \frac{\left|z_{j}\right|^{2} \beta_{j p q}}{\left(\left|z_{j}\right|^{2} e^{-\varphi_{j}}+\varepsilon^{2}\right)^{a_{j}}}+$ $\left(\left(\left|z_{j}\right|^{2} e^{-\varphi_{j}}+\varepsilon^{2}\right)^{1-a_{j}}-\varepsilon^{2\left(1-a_{j}\right)}\right) \frac{\partial^{2} \varphi_{j}}{\partial z_{p} \partial \bar{z}_{q}}$. But Lemma 4.2 enables us to use the computations of [CGP11, section 4.3] word for word, so as to show that $A(p, q, r, s) R_{p \bar{q} r \bar{s}}(z)$ is uniformly bounded in $z \in V \cap X_{l c}$.

The next step in bounding the curvature of $\omega_{\varepsilon}$ from below consists now in looking at the terms $R_{p \bar{q} r \bar{s}}$ for $p, q \in J$. Then the terms in $g_{p \bar{q}}$ coming from the Poincaré part are of the form $\sum_{k} \frac{\nu_{k}}{\log \left|z_{k}\right|^{2}}$ as (4) shows. These terms are uniformly bounded in $V \cap X_{l c}$, as well as their derivatives with respect to the variables $z_{r}, \bar{z}_{s}$ as long as $r, s \notin K$; in that that case [CGP11, sections 4.3-4.4] gives us the expected lower bound for $A(p, q, r, s) R_{p \bar{q} r \bar{s}}$. If now $r \in K$, then we saw earlier that $A(r) \frac{\partial}{\partial z_{r}}\left(\frac{\nu_{r}}{\log \left|z_{r}\right|^{2}}\right), A(s) \frac{\partial}{\partial \bar{z}_{s}}\left(\frac{\nu_{s}}{\log \left|z_{k}\right|^{2}}\right), A(r)^{2} \frac{\partial^{2}}{\partial z_{r} \partial \bar{z}_{r}}\left(\frac{\nu_{r}}{\log \left|z_{r}\right|^{2}}\right)$ are bounded functions in $V \cap X_{l c}$, so that, using Lemma 4.2, the boundedness of $A(p, q, r, s) R_{p \bar{q} r \bar{s}}$ is equivalent to the one of $A(p, q, r, s) R_{p \bar{q} r \bar{s}}^{g^{(C)}}$ whenever $p, q \in J$. And by [CGP11, section 4.3], we know the existence of this bound (which is an upper and lower bound, as $\#\{p, q, r, s\} \geqslant 2$ ).
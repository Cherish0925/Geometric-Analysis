---
retention_scope: session
part: 2
total_parts: 3
---

[Part 2/3 of: Kähler–Einstein Metrics on Stable Varieties and log Canonical Pairs]

Remark 3.4. - The proof of the preceding lemma yields actually a stronger result. If $\sum a_{i} \operatorname{div}\left(s_{i}\right)$ is an effective divisor with snc support meeting $D$ transversally and such that $a_{i}<1$ for all $i$, then the function $u$ obtained above satisfies $e^{u} / \prod\left|s_{i}\right|^{2 a_{i}}\left|s_{0}\right|^{2} \in L^{1}(d V)$, and more generally this is still true for $e^{\varepsilon u}$ for all $\varepsilon>0$ (use the inequality $\varepsilon x^{\alpha} \geqslant(n+1) \log x-C$ for $x=-\frac{1}{m} \log |s|_{h_{0}}^{2}$ this time).
3.4. Stability under perturbations. - Let now $L$ be a semipositive and big line bundle, and consider the perturbed ample lind bundles $L_{j}:=L+\varepsilon_{j} A$, for $\varepsilon_{j}$ a sequence of positive numbers tending to 0 and $A$ a fixed ample line bundle. Fixing also a Kähler form $\omega_{A} \in c_{1}(A)$ and a smooth semipositive form $\omega \in c_{1}(L)$, we write $\omega_{j}:=\omega+\varepsilon_{j} \omega_{A}$. Let $\mu_{j}$ be the sequence of measures on $X$ given by
$$\mu_{j}=\prod_{\alpha}\left(\left|s_{\alpha}\right|^{2}+\varepsilon_{j}\right)^{e_{\alpha}} \frac{d V}{\prod_{\beta}\left|s_{\beta}\right|^{2}}$$
where $e_{\alpha}>-1$ for all $\alpha$, and the divisor $\sum_{\alpha} \operatorname{div}\left(s_{\alpha}\right)+\sum_{\beta} \operatorname{div}\left(s_{\beta}\right)$ is a reduced normal crossing divisor. This is precisely the sequence of approximations we are going to use to solve our Kähler-Einstein equation.
Consider now the following Monge-Ampère equations for $u_{j} \in \mathcal{E}\left(X, \omega_{j}\right)$ (and supnormalized):
$$\omega_{u_{j}}^{n} / V=\frac{e^{u_{j}} \mu_{j}}{\int_{X} e^{u_{j}} \mu_{j}}$$
and similarly
$$\omega_{u}^{n} / V=\frac{e^{u} \mu}{\int_{X} e^{u} \mu}$$
for $u \in \mathcal{E}(X, \omega)$.
Theorem 3.5. - The unique sup-normalized solution $u_{j}$ of the first equation above converges, in the $L^{1}(X)$-topology, to the unique sup-normalized solution $u$ to the the latter equation. Equivalently, the solutions $v_{j}$ of the corresponding non-normalized equations converge in $L^{1}(X)$ to $v$ solving the corresponding limiting non-normalized equation.

Proof. - We denote by $\mathcal{G}_{j}$ (resp. $\mathcal{L}_{j}$ ) the functional determined by the pair $\left(\omega_{j}, \mu_{j}\right)$ (resp. $\mu_{j}$ ), and by $u_{j}$ the sup-normalized maximizer of $\mathcal{G}_{j}$. We also denote by $u_{0}$ the sup-normalized fixed $\omega$-psh function given by Lemma 3.3. Let us add that in the course of the proof, the precise value of the constant $C$ may, as usual, change from line to line. We split the proof into four steps.

Step 1. We first show that
$$-C \leqslant \mathcal{G}_{j}\left(u_{j}\right) \leqslant C$$
As $u_{0}$ is $\omega$-psh, it is also $\omega_{j}$-psh. Moreover, the capacity computation of Lemma 3.3 shows that the energy of $u_{0}$ with respect to $\omega_{j}$ is finite, and as $\mathcal{E}_{\omega_{j}}\left(u_{0}\right)$ increases with $j$, we obtain
$$\mathcal{E}_{\omega_{j}}\left(u_{0}\right) \geqslant-C$$
Besides, by dominated convergence, we have $\lim _{j \rightarrow+\infty} \mathcal{L}_{j}\left(u_{0}\right)=\mathcal{L}\left(u_{0}\right)$ and therefore we get $L_{j}\left(u_{0}\right) \geqslant-C$. Consequently, $\mathcal{G}_{j}\left(u_{j}\right) \geqslant \mathcal{G}_{j}\left(u_{0}\right) \geqslant-C$ which gives a first bound (recall that $u_{j}$ maximize $\mathcal{G}_{j}$ by Theorem 3.2 and the translation invariance of $\mathcal{G}_{j}$ ).

Choose now a probability measure $\mu_{0}$ satisying $\mu_{j} \geqslant e^{-C} \mu_{0}$ for all $j$ (its existence is clear given the precise form of $\mu_{j}$ ). Then Jensen's inequality gives
$$\mathcal{L}_{j}\left(u_{j}\right) \leqslant-\int_{X} u_{j} d \mu_{0}-C$$
but the compactness properties of quasi-psh functions (all $u_{j}$ 's are $C \omega_{A}$-psh) also gives the inequality
$$\sup u_{j}=0 \leqslant \int_{X} u_{j} d \mu_{0}+C$$
Combining the two previous inequalities, we get
$$\mathcal{G}_{j}\left(u_{j}\right) \leqslant \mathcal{E}_{\omega_{j}}\left(u_{j}\right)+C$$
which gives both the uniform upper bound for $\mathcal{G}_{j}\left(u_{j}\right)$ (as $\mathcal{E}_{\omega_{j}}$ is always non-positive) and a uniform lower bound $\mathcal{E}_{\omega_{j}}\left(u_{j}\right) \geqslant-C$.

Let $u$ be an $L^{1}$-limit point in $P S H(X, \omega)$ of the sequence $\left(u_{j}\right)$.

Step 2. We next show that
$$\mathcal{G}(u) \geqslant \lim \sup \mathcal{G}_{j}\left(u_{j}\right)$$
First by Fatou's lemma, we have
$$\mathcal{L}(u) \geqslant \lim \sup \mathcal{L}_{j}\left(u_{j}\right)$$
Moreoverm
$$\mathcal{E}(u) \geqslant \lim \sup \mathcal{E}_{\omega_{j}}\left(u_{j}\right)$$
as follows from Lemma 3.6 below. Putting these two inequalities together gives the desired bound.

Step 3. $u$ is a sup-normalized maximizer of $\mathcal{G}$.

For any given sup-normalized $\omega$-psh function $v$, we need to show that
$$\mathcal{G}(u) \geqslant \mathcal{G}(v)$$

Of course, on can assume that $\mathcal{G}(v)$ is finite. Thanks to step 2, it is enough to show that $\limsup \mathcal{G}_{j}(v) \geqslant G(v)$. But this inequality is far from clear as we cannot directly apply the dominated convergence theorem here. Indeed, for the energy part, it could happen that $\mathcal{E}_{\omega}(v)$ is finite though $\mathcal{E}_{\omega_{j}}(v)=-\infty$ for all $j$. As for the other part, despite $e^{v} \in L^{1}(\mu)$, it is not obvious that $e^{v} \in L^{1}\left(\mu_{j}\right)$ (because of the "zeroes" of $\mu$ which do not appear in $\mu_{j}$ ).

To bypass these difficulties we will use a regularization/perturbation argument. More precisely, we pick a family of smooth $\omega$-psh functions $\left(v_{\delta}\right)_{\delta>0}$ which decreases to $v$, and we set for all positive $\delta, \varepsilon$ :
$$v_{\delta, \varepsilon}:=(1-\varepsilon) v_{\delta}+\varepsilon u_{0}$$
where we recall that $u_{0}$ denotes the particular (sup-normalized) $\omega$-psh function constructed in Lemma 3.3.

As $v_{\delta}$ is smooth and $u_{0} \in \mathcal{E}^{1}\left(X, \omega_{j}\right)$ for all $j, v_{\delta, \varepsilon}$ has finite $\omega_{j}$-energy, the dominated convergence theorem shows that
$$\lim _{j \rightarrow+\infty} \mathcal{E}_{\omega_{j}}\left(v_{\delta, \varepsilon}\right)=\mathcal{E}_{\omega}\left(v_{\delta, \varepsilon}\right)$$
Moreover, as we observed in remark 3.4, the function $e^{\varepsilon u_{0}}$ is in $L^{1}(\mu)$ for all $\varepsilon>0$, and $e^{v_{\delta, \varepsilon}} \leqslant e^{\varepsilon u_{0}}$. Therefore, by dominated convergence, we get
$$\lim _{j \rightarrow+\infty} \mathcal{L}_{j}\left(v_{\delta, \varepsilon}\right)=\mathcal{L}\left(v_{\delta, \varepsilon}\right)$$
Combining (3.8) with (3.10) and (3.11), we get $\mathcal{G}(u) \geqslant \mathcal{G}\left(v_{\delta, \varepsilon}\right)$ for all $\delta, \varepsilon>0$. Set $v_{\varepsilon}:=(1-\varepsilon) v+\varepsilon u_{0}$. By monotonicity of $\mathcal{E}_{\omega}$, we have $\mathcal{E}_{\omega}\left(v_{\delta, \varepsilon}\right) \geqslant \mathcal{E}_{\omega}\left(v_{\varepsilon}\right)$. Using the dominated convergence theorem, we also see that $\mathcal{L}\left(v_{\delta, \varepsilon}\right) \rightarrow \mathcal{L}\left(v_{\varepsilon}\right)$. Therefore, we have $\mathcal{G}(u) \geqslant \mathcal{G}\left(v_{\varepsilon}\right)$. Finally, using the concavity of $\mathcal{G}$, we get $\mathcal{G}(u) \geqslant(1-\varepsilon) \mathcal{G}(v)+\varepsilon \mathcal{G}\left(u_{0}\right)$, and we get (3.9) by letting $\varepsilon$ go to zero.

Step 4. Back to the non-normalized equation. We have $v_{j}=u_{j}+\mathcal{L}_{j}\left(u_{j}\right)$ and as shown above in $(3.7), \mathcal{G}_{j}\left(u_{j}\right)$ is a bounded sequence (more precisely, it converges to the maximal value $S$ of $\mathcal{G}$ ) and $0 \leqslant-\mathcal{E}\left(u_{j}\right) \leqslant C$, which implies that $\mathcal{L}_{j}\left(u_{j}\right)$ is also a bounded sequence. After passing to a subsequence we may thus assume that $\mathcal{L}_{j}\left(u_{j}\right) \rightarrow l \in \mathbb{R}$ so that $v_{j} \rightarrow v:=u+l$, solving the desired equation (and $v \in \mathcal{E}^{1}(X, \omega)$ ). By the uniqueness of solutions of the latter equation this means that the whole sequence $u_{j}$ converges to $v$, which concludes the proof. \(\square\)

Let us now give the proof of the following result which was essential for step 2:
Lemma 3.6. - Let $\left[\omega_{j}\right]$ and $[\omega]$ be semi-positive big classes such that $\omega_{j} \rightarrow \omega$ in the $\mathcal{C}^{\infty}$-topology of smooth (semipositive) forms. If $u_{j} \in \mathcal{E}\left(X, \omega_{j}\right)$ (and $u \in \mathcal{E}(X, \omega)$ ) such that $u_{j} \rightarrow u$ in $L^{1}(X)$, then
$$\mathcal{E}_{\omega}(u) \geqslant \limsup _{j} \mathcal{E}_{\omega_{j}}\left(u_{j}\right)$$

Proof. - When $\omega_{j}=\omega$ the lemma amounts to the well-known fact that $\mathcal{E}_{\omega}$ is usc. We may as well assume that $\sup u_{j}=\sup u=0$.
First of all, we modify the sequence $\left(u_{j}\right)$ to make it non-increasing. More precisely, we set $\tilde{u}_{j}:=\left(\sup _{k \geqslant j} u_{k}\right)^{*}$, which defines an $\omega_{j}$-psh function. Then $\tilde{u}_{j} \geqslant u_{j}$ and the sequence $\left(\tilde{u}_{j}\right)_{j}$ is non-increasing. Given $v$ an $\omega$-psh function and $c \in \mathbb{R}$, we will write $v^{c}:=\max \{v, c\}$. By construction $\tilde{u}_{j}^{c}$ decreases to $u^{c}$, and all these functions are $\omega_{0}$-psh. By the local convergence result of Bedford-Taylor for mixed Monge-Ampère expressions and the smooth convergence of $\omega_{j}$ to $\omega$, we see that
$$\mathcal{E}_{\omega}\left(u^{c}\right)=\lim _{j \rightarrow+\infty} \mathcal{E}_{\omega_{j}}\left(\tilde{u}_{j}^{c}\right)$$
As $u_{j} \leqslant \tilde{u}_{j} \leqslant \tilde{u}_{j}^{c}$, the monotonicity of $\mathcal{E}_{\omega}$ ensures that
$$\mathcal{E}_{\omega}\left(u^{c}\right)=\limsup _{j \rightarrow+\infty} \mathcal{E}_{\omega_{j}}\left(u_{j}\right)$$
Taking the infimum over all $c$ and using the definition of the functional $\mathcal{E}_{\omega}$, we obtain the desired inequality. \(\square\)

Corollary 3.7. - Let $(X, D)$ be a log smooth log canonical pair (in particular, the coefficients of $D$ are in $]-\infty, 1]$ ) and assume that $L:=K_{X}+D$ is semi-positive and big. Fixing an ample line bundle $A$ set $L_{j}:=L+A / j$. Let $\psi_{j}$ be a decreasing sequence of smooth metrics on on the klt part $D_{k l t}$ of $D$ such that $\psi_{j} \rightarrow \phi_{k l t}\left(\right.$ where $\left.d d^{c} \phi_{k l t}=\left[D_{k l t}\right]\right)$ and consider the Monge-Ampère equations
$$\left(d d^{c} \phi_{j}\right)^{n}=e^{\phi_{j}-\psi_{j}-\phi_{D}}$$
for a metric $\phi_{j} \in \mathcal{E}\left(X, L_{j}\right)$. The equations admit unique solutions $\phi_{j}$ and moreover $\phi_{j} \rightarrow$ $\phi_{K E}$ in $L^{1}$ where $\phi_{K E}$ is the unique solution of equation (3.4).

\section*{4. Smoothness of the Kähler-Einstein metric}

Before we go into the details of the proof of the regularity theorem, we would like to give an overview of previous related results and underline the main differences that will appear in our specific case, namely the case of general $\log$ canonical pairs. As we will rely on the so called logarithmic case (i.e. ( $X, D$ ) is log smooth, $D$ is reduced, and $K_{X}+D$ is ample), the next section will be devoted to recall some of the main tools appearing in this setting. Then, we will give the proof of the main regularity theorem, which will constitute the core of this section.
4.1. Special features in the log canonical case. - We should first mention the case of varieties with log terminal singularities, or more generally klt pairs, which correspond to the pairs where the discrepancies $a_{i}$ defined earlier satisfy the strict inequalities $a_{i}>-1$. Then the situation is relatively well understood: In the non-positively curved case, we know that the Kähler-Einstein metric exists, is unique, has bounded potential, and induces on the regular locus a genuine Kähler-Einstein metric (see e.g. [BEGZ10, EGZ08, EGZ09, DP10]). As for the case of positive curvature, or log Fano manifolds, then there exist criteria (like the properness of the Mabuchi functional) to guarantee the existence and uniqueness
(modulo automorphisms of $X$ ) of a Kähler-Einstein metric [BBE ${ }^{+}$11]; this metric is also known to have bounded potential and to be smooth on the regular locus of $X$ (see again [BBE ${ }^{+}$11, Pău08]).

However, the behavior of the Kähler-Einstein metric near the singularities of $X$ is mostly unknown (except if the singularities are orbifold). In the case of a klt pair, we know that the metric will not be smooth along the divisor, but its singularities can sometimes be understood outside of the singular part of $(X, D)$. For example, a recent result in this direction states that the Kähler-Einstein metric has cone singularities near each point where $(X, D)$ is log smooth, i.e. $X$ is smooth and $D$ has simple normal crossing support (cf [Gue13, GP16]).

When $(X, D)$ is now a log smooth pair, the situation gets easier because there is no more loss of positivity coming from the resolution of singularities. For example, if the coefficients of $D$ are in $[0,1)$ (the pair is then klt), the Kähler-Einstein metric is known to have cone singularities along $D$, as it was proved by [GP16] in full generality, and by [Bre13, CGP13, JMR16] under some assumptions on $D$.

When now every coefficient of $D$ is equal to 1 , and $K_{X}+D$ is ample, then we know from the work of Kobayashi [Kob84] and Tian-Yau [TY87] that there exists a unique complete Kähler-Einstein metric having Poincaré singularities along $D$. The situation where the coefficients of $D$ are in ]0, 1] behaves like a product of cone and Poincaré geometries and was studied in [Gue14, GP16].

In a slightly different direction, Tsuji [Tsu88a] has considered the case of a singular variety with ample canonical line bundle such that only one divisor appears in its resolution, with discrepancy equal to -1. Finally, Wu [Wu08, Wu09] has worked out the case of a quasi-projective manifold compactified by a snc divisor $\sum D_{i}$ such that $K_{X}+\sum a_{i} D_{i}$ is ample for some coefficients $a_{i} \geqslant-1$. In our case however, such a strong positivity assumption will never happen as soon as we have to perform a non-trivial resolution.

As one can already observe in the log smooth case studied by Kobayashi and Tian-Yau, the log canonical case is very different from the klt case. Let us mention some striking divergences: first of all, the potentials are no more bounded even in the ample case so that the solution does not have minimal singularities. Moreover, the Kähler-Einstein equation in this setting is closely related to a negative curvature geometry. Indeed, if we first consider the Ricci-flat case, then it is impossible to write the equation on the whole $X$. Indeed, the current solution obtained on $X_{\text {reg }}$ will not have finite mass near the singularities, and hence it will not extend as a global positive current on $X$. This phenomenon already happens in [TY90]. Finally, it has been proven in $\left[\mathrm{BBE}^{+} 11\right.$, Proposition 3.8] that any pair $(X, D)$ with $X$ normal and $-\left(K_{X}+D\right)$ ample admitting a Kähler metric $\omega$ on $X_{\text {reg }}$ with continuous potentials solution of $\operatorname{Ric} \omega=\omega+[D]$ is necessarily klt. Therefore it is pointless to look for positively curved Kähler-Einstein metric in the general setting of log canonical pairs instead
of klt pairs.

To finish this discussion, let us stress the fact that the class of varieties with semi-log canonical singularities can be realized as a subclass of log canonical pairs (cf definition 2.8). This is the largest "reasonable" class to look for Kähler-Einstein metrics: for example, if $X$ is a smooth Fano manifold carrying a smooth divisor $D \in\left|-K_{X}\right|$, then for any $\varepsilon>0$, one has $K_{X}+(1+\varepsilon) D>0$; however, there is no smooth Kähler-Einstein metric with negative scalar curvature on $X \backslash D$. Indeed, its existence would contradict the Yau-Schwarz lemma applied with the complete Ricci-flat Kähler metric constructed in [TY90].

Moreover, we will see that the existence of a negatively curved Kähler-Einstein metric on the regular part of a normal projective variety with maximal volume forces the singularities to be at worst log canonical, cf. Proposition 5.1.
4.2. The logarithmic case. - In this section, we will briefly recall the Theorem of Kobayashi and Tian-Yau constructing negatively-curved Kähler-Einstein metrics on quasiprojective varieties $X \backslash D$ where $D$ is a reduced divisor with simple normal crossings, and $K_{X}+D$ is ample. In the course of the proof of Theorem 4.6, we will use in an essential manner the functional spaces introduced by these authors, namely the "quasi-coordinates" version of the usual Hölder spaces $\mathscr{C}^{k, \alpha}$. For now, $X_{0}$ will denote $X \backslash D$.

Definition 4.1. - We say that a Kähler metric $\omega$ on $X_{0}$ is of Carlson-Griffiths type if there exists a Kähler form $\omega_{0}$ on $X$ such that $\omega=\omega_{0}-\sum_{K} d d^{c} \log \log \frac{1}{\left|s_{k}\right|^{2}}$.

In [CG72], Carlson and Griffiths introduced such a metric for some $\omega_{0} \in c_{1}\left(K_{X}+D\right)$, but one can easily see that such a metric always exists on a Kähler manifold without assumptions on the bundle $K_{X}+D$. One can also observe that the existence of such a metric $\omega$ forces the cohomology class $\{\omega\}$ to be Kähler by Demailly's regularization theorem [Dem82, Dem92].

The reason why we exhibit this particular class of Kähler metrics on $X_{0}$ having Poincaré singularities along $D$ is that we have an exact knowledge on its behaviour along $D$, which is much more precise that knowing its membership in the aforementioned class. This is precisely the class in which one will look for a Kähler-Einstein metric, so that one needs to define the appropriate analogue of the usual Hölder spaces $\mathscr{C}^{k, \alpha}$. And to do so, one may (almost) boil down to the usual euclidian situation.

The key point is that $\left(X_{0}, \omega\right)$ has bounded geometry at any order. Let us get a bit more into the details. To simplify the notations, we will assume that $D$ is irreducible, so that locally near a point of $D, X_{0}$ is biholomorphic to $\mathbb{D}^{*} \times \mathbb{D}^{n-1}$, where $\mathbb{D}$ (resp. $\mathbb{D}^{*}$ ) is the unit disc (resp. punctured disc) of $\mathbb{C}$. We want to show that, roughly speaking, the components of $\omega$ in some appropriate coordinates have bounded derivatives at any order. The right way to formalize it consists in introducing quasi-coordinates: they are maps from an open subset $V \subset \mathbb{C}^{n}$ to $X_{0}$ having maximal rank everywhere. So they are just locally invertible, but these maps are not injective in general.

To construct such quasi-coordinates on $X_{0}$, we start from the univeral covering map $\pi: \mathbb{D} \rightarrow \mathbb{D}^{*}$, given by $\pi(w)=e^{\frac{w+1}{w-1}}$. Formally, it sends 1 to 0 . The idea is to restrict $\pi$ to some fixed ball $B(0, R)$ with $1 / 2<R<1$, and compose it (at the source) with a biholomorphism $\Phi_{\eta}$ of $\mathbb{D}$ sending 0 to $\eta$, where $\eta$ is a real parameter which we will take close to 1 . If one wants to write a formula, we set $\Phi_{\eta}(w)=\frac{w+\eta}{1+\eta w}$, so that the quasi-coordinate maps are given by $\Psi_{\eta}=\pi \circ \Phi_{\eta} \times \operatorname{Id}_{\mathbb{D}^{n-1}}: V=B(0, R) \times \mathbb{D}^{n-1} \rightarrow \mathbb{D}^{*}$, with $\Psi_{\eta}\left(v, v_{2}, \ldots, v_{n}\right)=\left(e^{\frac{1+\eta}{1-\eta} \frac{v+1}{v-1}}, v_{2}, \ldots, v_{n}\right)$.
Once we have said this, it is easy to see that $X_{0}$ is covered by the images $\Psi_{\eta}(V)$ when $\eta$ goes to 1 , and for all the trivializing charts for $X$, which are in finite number. Now, an easy computation shows that the derivatives of the components of $\omega$ with respect to the $v_{i}$ 's are bounded uniformly in $\eta$. This can be thought as a consequence of the fact that the Poincaré metric is invariant by any biholomorphism of the disc.

At this point, it is natural to introduce the Hölder space of $\mathscr{C}_{q c}^{k, \alpha}$-functions on $X_{0}$ using the previously introduced quasi-coordinates:

Definition 4.2. - For a non-negative integer $k$, a real number $\alpha \in] 0.1[$, we define:
$$\mathscr{C}_{q c}^{k, \alpha}\left(X_{0}\right)=\left\{u \in \mathscr{C}^{k}\left(X_{0}\right) ; \sup _{V, \eta}\left\|u \circ \Psi_{\eta}\right\|_{k, \alpha}<+\infty\right\}$$
where the supremum is taken over all our quasi-coordinate maps $V$ (which cover $X_{0}$ ). Here $\|\cdot\|_{k, \alpha}$ denotes the standard $\mathscr{C}_{q c}^{k, \alpha}$-norm for functions defined on a open subset of $\mathbb{C}^{n}$.

The following fact, though easy, is very important (see e.g [Kob84] or [Gue14, Lemma 1.6] for a detailed proof) :

Lemma 4.3. - Let $\omega$ be a Carlson-Griffiths type metric on $X_{0}$, and $\omega_{0}$ some Kähler metric on $X$. Then
$$F_{0}:=\log \left(\prod\left|s_{k}\right|^{2} \log ^{2}\left|s_{k}\right|^{2} \cdot \omega^{n} / \omega_{0}^{n}\right)$$
belongs to the space $\mathscr{C}_{q c}^{k, \alpha}\left(X_{0}\right)$ for every $k$ and $\alpha$.
Finding the Kähler-Einstein metric consists then in showing that the Monge-Ampère equation $\left(\omega+d d^{c} \varphi\right)^{n}=e^{\varphi+f} \omega^{n}$ has a unique solution $\varphi \in \mathscr{C}_{q c}^{k, \alpha}\left(X_{0}\right)$ for all functions $f \in \mathscr{C}_{q c}^{k, \alpha}\left(X_{0}\right)$ with $k \geqslant 3$. This can be done using the continuity method in the quasicoordinates. In particular, applying this to $f=F:=-\log \left(\prod\left|s_{k}\right|^{2} \log ^{2}\left|s_{k}\right|^{2} \cdot \omega^{n} / \omega_{0}^{n}\right)+$ (smooth terms on $X$ ), which the previous lemma allows to do, this will prove the existence of a negatively curved Kähler-Einstein metric, which is equivalent to $\omega$ (in the strong sense: $\varphi \in \mathscr{C}_{q c}^{k, \alpha}\left(X_{0}\right)$ for all $k, \alpha$ ).

In this continuity method, one needs to obtain first uniform estimates; they follow from a consequence of Yau's maximum principle for complete manifolds which we recall here (see [CY80, Proposition 4.1]):

Proposition 4.4. - Let $(X, \omega)$ be a $n$-dimensional complete Kähler manifold, and $F \in$ $\mathscr{C}^{2}(X)$ bounded from above. We assume that we are given $u \in \mathscr{C}^{2}(X)$ satisfying $\omega+d d^{c} u>0$ and
$$\left(\omega+d d^{c} u\right)^{n}=e^{u+F} \omega^{n}$$
Suppose that the bisectional curvature of $(X, \omega)$ is bounded below by some constant, and that $u$ is bounded from below. Then
$$\inf _{X} u \geqslant-\sup _{X} F \quad \text { and } \quad \sup _{X} u \leqslant-\inf _{X} F$$

There are similar results for the Laplacian estimates, but as we will not use them directly, we do not state them here. To summarize the discussion, one obtains:

Theorem 4.5 (Kobayashi [Kob84], Tian-Yau [TY87]). - Let $X$ be a compact Kähler manifold, $D$ a reduced divisor with simple normal crossings, $\omega$ a Kähler form of Carlson-Griffiths type on $X \backslash D$, and $F \in \mathscr{C}_{q c}^{k, \alpha}(X \backslash D)$ for some $k \geqslant 3$. Then there exists $\varphi \in$ $\mathscr{C}_{q c}^{k, \alpha}(X \backslash D)$ solution to the following equation:
$$\left(\omega+d d^{c} \varphi\right)^{n}=e^{\varphi+F} \omega^{n}$$
In particular if $K_{X}+D$ is ample, then there exists a (unique) Kähler-Einstein metric of curvature -1 equivalent to $\omega$.
4.3. Statement of the regularity theorem. - In this section, we prove that the Kähler-Einstein metric attached to a log canonical pair $(X, D)$ (satisfying $K_{X}+D$ ample) by Theorem 3.2 is smooth on $X_{0}=X_{\text {reg }} \backslash \operatorname{Supp}(D)$. As usual, we will work on a log resolution $\pi: X^{\prime} \rightarrow X$, where:
$$K_{X^{\prime}}=\pi^{*}\left(K_{X}+D\right)+\sum a_{i} E_{i}$$
$E_{i}$ being either an exceptional divisor or a component of the strict transform of $D$, and the coefficients $a_{i}$ (called discrepencies) satisfy the inequality $a_{i} \geqslant-1$.

The Kähler-Einstein metric is given on $X^{\prime}$ by a (singular) psh weight $\phi$ on $\pi^{*}\left(K_{X}+D\right)$ satisfying
$$\left(d d^{c} \phi\right)^{n}=e^{\phi+\sum a_{i} \phi_{E_{i}}}$$
where $\phi_{E_{i}}$ is a psh weight on $\mathcal{O}_{X^{\prime}}\left(E_{i}\right)$ such that $d d^{c} \phi_{E_{i}}=\left[E_{i}\right]$. So if in local coordinates, $E_{i}$ is given by $\left\{z_{n}=0\right\}$, then $\phi_{E_{i}}=\log \left|z_{n}\right|^{2}$.

Our aim is to obtain regularity properties for the solutions of degenerate Monge-Ampère equations like the previous one; this is the content of the following theorem:

Theorem 4.6. - Let $X$ be a compact Kähler manifold of dimension $n$, $d V$ some volume form, $D=\sum a_{i} D_{i}$ a $\mathbb{R}$-divisor with coefficients in $(-\infty, 1]$ and defining sections $s_{i}, E=$ $\sum c_{\alpha} E_{\alpha}$ an effective $\mathbb{R}$-divisor such that $D_{\text {red }}+E$ has snc support, and $\theta$ a semipositive
form with $\int_{X} \theta^{n}>0$ such that $\{\theta\}-c_{1}(E)$ is a Kähler class. Then the $\theta$-psh function $\varphi$ with full Monge-Ampère mass, which is a solution of
$$\left\langle\left(\theta+d d^{c} \phi\right)^{n}\right\rangle=\frac{e^{\varphi} d V}{\prod_{i}\left|s_{i}\right|^{2 a_{j}}}$$
is smooth outside of $\operatorname{Supp}(D) \cup \operatorname{Supp}(E)$.
Note that although $\varphi$ has full Monge-Ampère mass, it is in general far from having minimal singularities as soon as some coefficient $a_{i}$ of $D$ equals 1 . Think for example of the logarithmic case (a log smooth pair $(X, D)$ where $K_{X}+D$ is ample; then the potential of the Kähler-Einstein metric is not bounded whereas the class is ample.

Let us go back to the general Kähler-Einstein case. We would like to apply the previous results with $E$ being some positive combination of the $E_{i}$ 's. The problem is that there might be no such divisors; for example if $\pi$ happens to be a small resolution, its exceptional locus has codimension at least 2. Therefore we need to perform another modification.

On $X^{\prime}, \pi^{*}\left(K_{X}+D\right)$ is no more ample, and by [BBP13, Proposition 1.5], its augmented base locus is $\mathbb{B}_{+}\left(\pi^{*}\left(K_{X}+D\right)\right)=\pi^{-1}\left(\mathbb{B}_{+}\left(K_{X}+D\right)\right) \cup \operatorname{Exc}(\pi)=\operatorname{Exc}(\pi)$, and lies above $X_{\text {sing }} \cup \operatorname{Supp}(D)$. It is well-known that one can find a log resolution $\mu: X^{\prime \prime} \rightarrow X^{\prime}$ of $\left(X^{\prime}, \mathbb{B}_{+}\left(\pi^{*}\left(K_{X}+D\right)\right)\right)$, and an effective $\mathbb{Q}$-divisor $F$ with snc support lying above $\mathbb{B}_{+}\left(\pi^{*}\left(K_{X}+D\right)\right)$ and such that $\mu^{*} \pi^{*}\left(K_{X}+D\right)-F$ is ample. Moreover one can also assume that $F+\sum E_{i}^{\prime}$ has snc support, where $E_{i}^{\prime}$ denotes the strict transform of $E_{i}$ by $\mu$.

Let us recall the argument. We start by resolving the singularities of a Kähler current $T \geqslant \omega$ ( $\omega$ a Kähler form on $X^{\prime}$ ) in $\pi^{*}\left(K_{X}+D\right)$ computing $\mathbb{B}_{+}\left(\pi^{*}\left(K_{X}+D\right)\right.$ ), then we write Siu's decomposition $\mu^{*} T=\theta+[D]$ with $\theta$ semi-positive dominating $\mu^{*} \omega$, and $D$ lying above $\mathbb{B}_{+}\left(\pi^{*}\left(K_{X}+D\right)\right)$. Finally, we choose a $\mu$-exceptional $\mathbb{Q}$-divisor $G$ such that $-G$ is $\mu$-ample; it exists because $\mu$ is a finite composition of blow-ups with smooth centers. Then it becomes clear that for $\varepsilon>0$ small enough, $\left\{\mu^{*} \theta\right\}-\varepsilon G$ is a Kähler class, and we have $\mu^{*} \pi^{*}\left(K_{X}+D\right)=\left(\left\{\mu^{*} \theta\right\}-\varepsilon G\right)+(\varepsilon G+D)$, with $\varepsilon G+D$ lying above $\mathbb{B}_{+}\left(\pi^{*}\left(K_{X}+D\right)\right)$ and having simple normal crossing support. If one had chosen a log resolution of the ideal sheaf generated by the augmented base locus of $\pi^{*}\left(K_{X}+D\right)$ and the $\mathcal{O}_{X}^{\prime}\left(E_{i}\right)$, we would have obtained the refined result that $F+E^{\prime}$ has snc support.

Set $\nu:=\pi \circ \mu: X^{\prime \prime} \rightarrow X$, and write $K_{X^{\prime \prime}}=\nu^{*}\left(K_{X}+D\right)+E_{\nu}$. We know that $E_{\nu}$ is a divisor with snc support and coefficients $\geqslant-1$, and by the construction above, there exists a snc divisor $F$ on $X^{\prime \prime}$ lying above $X_{\text {sing }} \cup \operatorname{Supp}(D)$ such that $F+\left(E_{\nu}\right)_{\text {red }}$ has snc support and $\nu^{*}\left(K_{X}+D\right)-F$ is ample. Applying Theorem 4.6, we get:

Corollary 4.7. - Let $(X, D)$ be a log canonical pair such that $K_{X}+D$ is ample. Then the Kähler-Einstein metric $\omega_{\mathrm{KE}}$ on $(X, D)$ is smooth on $X_{\mathrm{reg}} \backslash \operatorname{Supp}(D)$.

As we shall see in the course of the proof (cf §4.5.2), we do not obtain very precise estimates on the potential of the solution, even at order zero. However, it is tempting to believe that the potential $\phi_{\mathrm{KE}}$ of the Kähler-Einstein metric should be locally bounded outside of the non-klt locus of $(X, D)$ defined as the support of the sheaf $\mathcal{O}_{X} / \mathscr{I}(X, D)$ where $\mathscr{I}(X, D)$ is the multiplier ideal sheaf of $(X, D)$ (cf. e.g. [Laz04]). However, as this locus cannot be read easily on some log resolution, it does not seem obvious how one should tackle this question.
4.4. Preliminaries: the regularized equation. - We now borrow the notations of Theorem 4.6, and we let $\omega_{0}$ be a Kähler form on $X$; it will be our reference metric in the following. Recall that we want to solve the equation
$$\operatorname{MA}(\varphi)=\frac{e^{\varphi} d V}{\prod_{i}\left|s_{i}\right|^{2 a_{i}}}$$
where the unknown function is $\varphi$ a $\theta$-psh function, $s_{i}$ are non-zero sections of $\mathcal{O}_{X}\left(D_{i}\right),|\cdot|_{i}$ are smooth hermitian metrics on $\mathcal{O}_{X}\left(D_{i}\right), f \in \mathscr{C}^{\infty}(X)$ and $d V$ is a smooth volume form on $X$. Moreover, the expression $\operatorname{MA}(\varphi)$ has to be understood as the non-pluripolar Mongeampère operator. It will be convenient for the following to differentiate the "klt part" of $D$ from its "lc part", so we introduce the following notation:
$$D=\underbrace{\sum_{a_{j}<1} a_{j} D_{j}}_{D_{k l t}}+\underbrace{\sum_{a_{k}=1} D_{k}}_{D_{l c}}$$

By Theorem 3.5, we know that the solution is the limit of any sequence of solutions of some appropriate regularized equations. The regularization process we are going to use concerns both the a priori non-Kähler class $\{\theta\}$ and the "klt part" in the volume form: $\prod_{a_{j}<1}\left|s_{i}\right|^{-2 a_{j}}$. More concretely, we will be studying the following equation:
$$\left\langle\left(\theta+t \omega_{0}+d d^{c} \varphi_{t, \varepsilon}\right)^{n}\right\rangle=\frac{e^{\varphi_{t, \varepsilon}+f} d V}{\prod_{a_{j}<1}\left(\left|s_{i}\right|^{2}+\varepsilon^{2}\right)^{a_{i}} \prod_{a_{k}=1}\left|s_{k}\right|^{2}}$$
Smoothness of the regularized solution. - At this point, it is still not completely clear that the solution $\varphi_{t, \varepsilon}$ of equation (4.1) is smooth on $X \backslash D_{l c}$. So we translate our equation into the logarithmic setting : we set
$$\omega_{t, l c}:=\theta+t \omega_{0}-\sum_{a_{k}=1} d d^{c} \log \left(\log \left|s_{k}\right|^{2}\right)^{2}$$
We may choose the hermitian metrics $|\cdot|_{k}$ such that $\left|s_{k}\right|<1$ and such that $\omega_{t, l c}$ defines a Kähler metric on $X \backslash D_{l c}$ (cf [CG72, Gri76] e.g.). Of course this rescaling will depend on $t$, but we will explain how to bypass this problem later.

So using this new reference metric, one may rewrite equation (4.1) in the following form:
$$\left(\omega_{t, l c}+d d^{c} \psi_{t, \varepsilon}\right)^{n}=\frac{e^{\psi_{t, \varepsilon}+f_{t}} \omega_{t, l c}^{n}}{\prod_{a_{j}<1}\left(\left|s_{j}\right|^{2}+\varepsilon^{2}\right)^{a_{j}}}$$
where $\psi_{t, \varepsilon}=\varphi_{t, \varepsilon}+\sum_{a_{k}=1} \log \left(\log \left|s_{k}\right|^{2}\right)^{2}$ and $f_{t}=-\log \left(\frac{\prod_{k}\left|s_{k}\right|^{2} \log ^{2}\left|s_{k}\right|^{2} \omega_{t, l c}^{n}}{d V}\right)$. Clearly, $f_{t}$ is bounded (but only the lower bound is uniform in $t$ ) and smooth on $X \backslash D_{l c}$, but we know by Lemma 4.3 that $f_{t}$ is smooth when read in the quasi-coordinates adapted to the pair $\left(X, D_{l c}\right)$. Therefore, using the Theorem of Kobayashi and Tian-Yau (see Theorem 4.5), we know that the solution $\psi_{t, \varepsilon}$ is bounded on $X \backslash D_{l c}$ : there exists $C_{t, \varepsilon}>0$ such that
$$-C_{t, \varepsilon}-\sum_{a_{k}=1} \log \left(\log \left|s_{k}\right|^{2}\right)^{2} \leqslant \varphi_{t, \varepsilon} \leqslant C_{t, \varepsilon}-\sum_{a_{k}=1} \log \left(\log \left|s_{k}\right|^{2}\right)^{2}$$

Moreover, $\psi_{t, \varepsilon}$ is smooth in the quasi-coordinates. In particular, $\omega_{t, l c}+d d^{c} \psi_{t, \varepsilon}$ is a Kähler metric with bounded geometry on $X \backslash D_{l c}$ and with Poincaré type growth along $D_{l c}$. Therefore it is complete and has a bounded curvature tensor. To prove the regularity theorem, we will thus have to obtain on each compact subset of $X_{0}$ estimates on the potential $\varphi_{\varepsilon}$ at any order.

A first attempt at the uniform estimate. - The previous observation allows us to apply Yau's maximum principle (cf Proposition 4.4), and obtain that
$$\sup _{X \backslash D_{l c}} \psi_{t, \varepsilon} \leqslant \sup _{X \backslash D_{l c}}\left(\sum a_{i} \log \left(\left|s_{i}\right|^{2}+\varepsilon^{2}\right)-f_{t}\right)$$
and similarly $\inf _{X \backslash D_{l c}} \psi_{t, \varepsilon} \leqslant \inf _{X \backslash D_{l c}}\left(\sum a_{i} \log \left(\left|s_{i}\right|^{2}+\varepsilon^{2}\right)-f_{t}\right)$. If some coefficient $a_{i}$ is negative, then we cannot obtain a bound for $\sup \psi_{t, \varepsilon}$. As for the lower bound, $-f_{t}$ is not uniformly bounded from below because $\omega_{t, l c}$ degenerates at $t=0$ (and if some $a_{i}$ is positive, $a_{i} \log \left(\left|s_{i}\right|^{2}+\varepsilon^{2}\right)$ is not uniformly bounded below neither), so we cannot expect to find a lower bound for $\psi_{t, \varepsilon}$ using this strategy. Therefore we need another method to obtain a zero-order estimate on the potential of the solution. In fact, we will need to add some barrier function to gain positivity, in the spirit of Tsuji's trick [Tsu88b] for the Laplacian estimate of a degenerate class; the novelty in our situation is that this is also needed for the zero-order estimates (as opposed to the klt case).
4.5. Uniform estimate. - Before going any further, let us fix some notations.
4.5.1. A new framework. - We will denote by $s_{i}, i \in I$ (non-zero) sections of the (reduced) components of the divisor $D_{\text {red }}+E$, and by $s_{\alpha}, \alpha \in A$ (non-zero) sections of the (reduced) components of $E$; we endow all these line bundles with suitable smooth hermitian metrics (se below). Finally, we set $X_{0}:=X \backslash(\operatorname{Supp}(D) \cup \operatorname{Supp}(E))$, and define $F:=\left(D_{\text {red }}+E\right)_{\text {red }}$ as the reduced divisor $X \backslash X_{0}$.

The idea is to work on $X_{0}$. Of course, if we endow the last space with the Kähler metric $\omega_{t, l c}$, it will not be complete (near $D_{k l t}$ e.g.), so we won't be able to use Yau's maximum principle. Instead, we will rather use the following metric:
$$\omega_{\chi}:=\theta+t \omega_{0}-\sum_{i \in I} d d^{c} \log \left(\log \left|s_{i}\right|^{2}\right)^{2}+d d^{c} \chi$$
where $\chi:=\sum_{\alpha} c_{\alpha} \log \left|s_{\alpha}\right|^{2}$ (recall that the $c_{\alpha}$ 's are the coefficients of $E$ ).

We do here a slight abuse of notation because $\omega_{\chi}$ depends on $t$. However, the following lemma shows that the dependence is harmless:

Lemma 4.8. - Up to changing the previously chosen hermitian metrics, the (1,1)-form $\omega_{\chi}$ defines on $X_{0}$ a smooth Kähler metric with Poincaré growth along $F$ having bounded geometry, all of those properties being satisfied uniformly in $t$.

What we mean by this statement is that there exists a Poincaré-type metric $\omega_{P}$ on $X_{0}$ and a constant $C>0$ independent of $t$ such that $C^{-1} \omega_{P} \leqslant \omega_{\chi} \leqslant C \omega_{P}$, and that in the appropriate quasi-coordinates attached to the pair $(X, F)$, the coefficients $g_{i \bar{j}}$ of $\omega_{\chi}$ satisfy $\left|\frac{\partial^{|\alpha|+|\beta|} g_{i \bar{j}}}{\partial z^{\alpha} \partial \bar{z}^{\beta}}\right| \leqslant C_{\alpha, \beta}$ for some constants $C_{\alpha, \beta}>0$ independant of $t$. In particular, $\omega_{\chi}$ has a uniformly (in $t$ ) bounded curvature tensor.

Proof of Lemma 4.8. - We know that $\{\theta\}-c_{1}(E)$ is ample. Therefore, up to changing the hermitian metrics $h_{\alpha}$ on $\mathcal{O}_{X}\left(E_{\alpha}\right)$, we may suppose that $\eta:=\theta-\sum c_{\alpha} \Theta_{h_{\alpha}}\left(E_{\alpha}\right)$ defines a smooth Kähler form on $X$ (we designated by $\Theta_{h_{\alpha}}\left(E_{\alpha}\right)$ the curvature form of the hermitian line bundle $\left(E_{\alpha}, h_{\alpha}\right)$ ). Therefore, on $X_{0}$, we have:
$$\omega_{\chi}=\eta+t \omega_{0}-\sum_{i \in I} d d^{c} \log \left(\log \left|s_{i}\right|^{2}\right)^{2}$$
and the statement follows easily from the computations of [CG72, Proposition 2.1] and [Kob84, Lemma 2] or [TY87]. \(\square\)
4.5.2. Getting the lower bound. - First of all, we will use the crucial information that $\varphi_{t, \varepsilon}$ converges (in the weak sense of distributions) to some $\theta$-psh function (cf first paragraph). By the elementary properties of psh (or quasi-psh) functions, we know that $\left(\varphi_{t, \varepsilon}\right)$ is uniformly bounded above on the compact set $X$ (see e.g. [Hör94, Theorem 3.2.13]). Therefore, we obtain some uniform constant $C$ such that
$$\varphi_{t, \varepsilon} \leqslant C$$

Now, recall that we chose $\omega_{\chi}$ to be the new reference metric, so our equation becomes
$$\left(\omega_{\chi}+d d^{c} u_{t, \varepsilon}\right)^{n}=e^{u_{t, \varepsilon}+G_{\varepsilon}} \omega_{\chi}^{n}$$
where
$$u_{t, \varepsilon}:=\varphi_{t, \varepsilon}+\sum_{i \in I} \log \left(\log \left|s_{i}\right|^{2}\right)^{2}-\chi$$
and
$$G_{\varepsilon}:=\chi+f+\sum_{a_{j}<1} \log \left(\frac{\left|s_{j}\right|^{2}}{\left(\left|s_{j}\right|^{2}+\varepsilon^{2}\right)^{a_{j}}}\right)-\log \left(\frac{\prod_{i \in I}\left|s_{i}\right|^{2} \log ^{2}\left|s_{i}\right|^{2} \omega_{\chi}^{n}}{d V}\right)$$

Here again we should mention that $G_{\varepsilon}$ also depends on $t$ through the last term involving $\omega_{\chi}$. For our purpose, we can ignore this dependence in order to simplify the notations.

We can see from (4.3) and Lemma 4.8 that $G_{\varepsilon}$ has a uniform (in $t$ and $\varepsilon$ ) upper bound on $X_{0}$ :
$$\sup _{X_{0}} G_{\varepsilon} \leqslant C$$

Moreover, we know from (4.2) that $\varphi_{t, \varepsilon}+\sum_{a_{k}=1} \log \left(\log \left|s_{k}\right|^{2}\right)^{2}$ is bounded. Therefore, it follows immediately that $u_{t, \varepsilon}$ is bounded from below (but a priori non uniformly). Applying Yau's maximum principle (cf. Proposition 4.4) to the smooth function $u_{t, \varepsilon}$ on the complete Kähler manifold $\left(X_{0}, \omega_{\chi}\right)$ ensures that $\inf _{X_{0}} u_{t, \varepsilon} \geqslant-\sup _{X_{0}} G_{\varepsilon} \geqslant-C$. In terms of $\varphi_{t, \varepsilon}$, and recalling inequality (4.3) we get:
$$C \geqslant \varphi_{t, \varepsilon} \geqslant \chi-C-\sum_{i \in I} \log \left(\log \left|s_{i}\right|^{2}\right)^{2}$$
4.6. Laplacian estimate. - For the Laplacian estimate, we still work on the open manifold $X_{0}$. We endow it with the complete Kähler metric $\omega_{\chi}$, and we recall from Lemma 4.8 that $\omega_{\chi}$ has uniformly bounded (bisectional) curvature.

As usual when one wants to compare to Kähler metrics $\omega$ and $\omega^{\prime}$, the strategy is to use an inequality of the form $\Delta F \geqslant G$, where $F, G$ involve terms like $\operatorname{tr}_{\omega} \omega^{\prime}, \operatorname{tr}_{\omega^{\prime}} \omega$ or the local potentials of $\omega^{\prime}-\omega$. There exist several variants of such inequalities, due e.g. to Chen-Lu, Yau, Siu, etc. involving different assumptions on the curvature of the metrics involved. In our case, as we have a control on the bisectional curvature of the reference metric $\omega_{\chi}$, on the Ricci curvature of the "unknown metric" $\omega_{\chi}+d d^{c} u_{t, \varepsilon}$, and on the laplacian $\Delta_{\omega_{\chi}} G_{\varepsilon}$, we could use any of these formulas.

We have chosen to use a variant of Siu's inequality [Siu87, p.99], which can be found in [CGP13, Proposition 2.1] (see also [Pău08, $\mathbf{B B E}^{+} \mathbf{1 1}$ ]); notice the important feature allowing the factor $e^{-F_{-}}$for $F_{-}$quasi-psh which is crucial for us since the RHS of our Monge-Ampère equation has poles:

Proposition 4.9. - Let $X$ be a Kähler manifold of dimension $n, \omega, \omega^{\prime}$ two cohomologous Kähler metrics on $X$. We assume that $\omega^{\prime}=\omega+d d^{c} u$ with $\omega^{\prime n}=e^{u+F_{+}-F_{-}} \omega^{n}$. and that we have a constant $C>0$ satisfying:
\begin{itemize}
\item[(i)] $d d^{c} F_{ \pm} \geqslant-C \omega$,
\item[(ii)] $\Theta_{\omega}\left(T_{X}\right) \geqslant-C \omega \otimes \operatorname{Id}_{T_{X}}$.
\end{itemize}
Then there exist some constant $A>0$ depending only on $n$ and $C$ such that
$$\Delta_{\omega^{\prime}}\left(\log \operatorname{tr}_{\omega} \omega^{\prime}-A u+F_{-}\right) \geqslant \operatorname{tr}_{\omega^{\prime}} \omega-n A .$$
Moreover, if one assumes that $\sup F_{+} \leqslant C, u \geqslant-C$ and that $\log \operatorname{tr}_{\omega} \omega^{\prime}-A u+F_{-}$attains its maximum on $X$, then there exists $M>0$ depending on $n$ and $C$ only such that:
$$\omega^{\prime} \leqslant M e^{A u-F_{-}} \omega .$$

Here $\Delta$ (resp. $\Delta^{\prime}$ ) is the laplacian with respect to $\omega$ (resp. $\omega^{\prime}$ ), and $\Theta_{\omega}\left(T_{X}\right)$ is the Chern curvature tensor of the hermitian holomorphic vector bundle $\left(T_{X}, \omega\right)$ (which may be identified with the tensor of holomorphic bisectional curvatures, usually denoted by the letter R).

Sketch of proof. - Siu's inequality applied to $\omega=\sum g_{i \bar{j}} d z_{i} \wedge d \bar{z}_{k}$ and $\omega^{\prime}=\sum g_{i \bar{j}}^{\prime} d z_{i} \wedge d \bar{z}_{k}$ yields:
$$\Delta^{\prime}\left(\log \operatorname{tr}_{\omega} \omega^{\prime}\right) \geqslant \frac{1}{\operatorname{tr}_{\omega} \omega^{\prime}}\left(-g^{j \bar{i}} R_{j \bar{i}}+\Delta\left(u+F_{+}-F_{-}\right)+g^{\prime k \bar{l}} R_{k \bar{l}}^{j \bar{i}} g_{j \bar{i}}^{\prime}\right)$$

Recollecting terms coming (with different signs) from the scalar and the Ricci curvature, we will obtain a similar inequality involving only a lower bound for the holomorphic bisectional curvature, namely
$$\Delta^{\prime} \log \operatorname{tr}_{\omega} \omega^{\prime} \geqslant \frac{\Delta\left(u+F_{+}-F_{-}\right)}{\operatorname{tr}_{\omega}\left(\omega^{\prime}\right)}-B \operatorname{tr}_{\omega^{\prime}} \omega$$
where $B$ is a lower bound for the bisectional curvature of $\omega$ : this is the content of [CGP13, Lemma 2.2].
Clearly, $\Delta u=\operatorname{tr}_{\omega} \omega^{\prime}-n$ so that $\Delta\left(u+F_{+}\right) \geqslant-n(C+1)$. As $\operatorname{tr}_{\omega} \omega^{\prime} \operatorname{tr}_{\omega^{\prime}} \omega \geqslant n$, we get
$$\frac{\Delta\left(u+F_{+}\right)}{\operatorname{tr}_{\omega} \omega^{\prime}} \geqslant-(1+C) \operatorname{tr}_{\omega^{\prime}} \omega$$
As for the second laplacian, we write
$$0 \leqslant C \omega+d d^{c} F_{-} \leqslant \operatorname{tr}_{\omega^{\prime}}\left(C \omega+d d^{c} F_{-}\right) \omega^{\prime}$$
and we take the trace with respect to $\omega$ :
$$\frac{n C+\Delta_{\omega} F_{-}}{\operatorname{tr}_{\omega} \omega^{\prime}} \leqslant C \operatorname{tr}_{\omega^{\prime}} \omega+\Delta_{\omega^{\prime}} F_{-}$$
so that
$$\Delta_{\omega^{\prime}} F_{-} \geqslant \frac{\Delta_{\omega} F_{-}}{\operatorname{tr}_{\omega} \omega^{\prime}}-C \operatorname{tr}_{\omega^{\prime}} \omega$$
Plugging (4.6) and (4.7) into (4.5), we get:
$$\Delta^{\prime}\left(\log \operatorname{tr}_{\omega} \omega^{\prime}+F_{-}\right) \geqslant-C_{1} \operatorname{tr}_{\omega^{\prime}} \omega$$
for $C_{1}=1+B+2 C$. Finally, using $\Delta^{\prime} u=n-\operatorname{tr}_{\omega^{\prime}} \omega$, we see that
$$\Delta^{\prime}\left(\log \operatorname{tr}_{\omega} \omega^{\prime}-\left(C_{1}+1\right) u+F_{-}\right) \geqslant \operatorname{tr}_{\omega^{\prime}} \omega-n\left(C_{1}+1\right)$$
which shows the first assertion by chosing $A:=1+C_{1}$.

As for the second part, if we denote by $p$ the point where the maximum is attained, then one has $\left(\operatorname{tr}_{\omega^{\prime}} \omega\right)(p) \leqslant C_{2}$. Using the basic inequality $\operatorname{tr}_{\omega} \omega^{\prime} \leqslant e^{u+F_{+}-F_{-}}\left(\operatorname{tr}_{\omega^{\prime}} \omega\right)^{n-1}$, one gets
$$\begin{aligned}
\log \left(\operatorname{tr}_{\omega} \omega^{\prime}\right) & =\left(\log \operatorname{tr}_{\omega} \omega^{\prime}-A u+F_{-}\right)+A u-F_{-} \\
& \leqslant\left(u(p)+F_{+}(p)-F_{-}(p)\right)+(n-1) \log (n A)-A u(p)+F_{-}(p)+A u-F_{-} \\
& \leqslant C_{2}+A u-F_{-}
\end{aligned}$$
where $C_{2}=\sup F_{+}+(n-1) \log (n A)-(A-1) \inf u$ (recall that $A$ can be chosen to be positive). This concludes the proof of the proposition. \(\square\)

Recall that we are interested in equation (4.4) given by
$$\left(\omega_{\chi}+d d^{c} u_{t, \varepsilon}\right)^{n}=e^{u_{t, \varepsilon}+G_{\varepsilon}} \omega_{\chi}^{n}$$
We obtained the zero-order estimate on $u_{t, \varepsilon}$ in the last section, and now we want a Laplacian estimate. In order too use the previous proposition we first have to decompose $G_{\varepsilon}$ as a difference of $C \omega_{\chi}$-psh functions in order to use the result above. Recall that
$$G_{\varepsilon}:=\chi+f+\sum_{a_{j}<1} \log \left(\frac{\left|s_{j}\right|^{2}}{\left(\left|s_{j}\right|^{2}+\varepsilon^{2}\right)^{a_{j}}}\right)-\log \left(\frac{\prod_{i \in I}\left|s_{i}\right|^{2} \log ^{2}\left|s_{i}\right|^{2} \omega_{\chi}^{n}}{d V}\right)$$
By [Kob84] or [Gue14, Lemma 1.6], the last term is already known to be smooth in the quasi-coordinates (and it depends neither on $t$ nor on $\varepsilon$ ).
We claim that
$$G_{\varepsilon}=\underbrace{\left[\chi+f+\sum_{a_{j}<1} \log \left|s_{j}\right|^{2}+\sum_{a_{j}<0} \log \left(\left|s_{j}\right|^{2}+\varepsilon^{2}\right)^{-a_{j}}\right]}_{F_{+}}-\underbrace{\left[\sum_{0<a_{j}<1} \log \left(\left|s_{j}\right|^{2}+\varepsilon^{2}\right)^{a_{j}}\right]}_{F_{-}}$$
gives the desired decomposition $G_{\varepsilon}=F_{+}-F_{-}$in the notations of Proposition 4.9. Indeed, $\chi, f, \log \left|s_{i}\right|^{2}$ are quasi-psh, thus $C \omega_{\chi}$-psh for some uniform $C>0$ as $\omega_{\chi}$ dominates some fixed Kähler form, cf Lemma 4.8. Moreover, a simple computation leads to the identity:
$$d d^{c} \log \left(|s|^{2}+\varepsilon^{2}\right)=\frac{\varepsilon^{2}}{\left(|s|^{2}+\varepsilon^{2}\right)^{2}} \cdot\left\langle D^{\prime} s, D^{\prime} s\right\rangle-\frac{|s|^{2}}{|s|^{2}+\varepsilon^{2}} \cdot \Theta_{h}$$
where $\Theta_{h}$ is the curvature of the hermitian metric $h$ implicit in the term $|s|^{2}$, and $D^{\prime} s$ is the $(1,0)$-part of $D s$ where $D$ is the Chern connection attached to $\left(\mathcal{O}_{X}(\operatorname{div}(s)), h\right)$. If follows that $F_{ \pm}$are $C \omega_{\chi}$-psh for some uniform $C>0$.

We can now apply Proposition 4.9 to the setting: $\omega=\omega_{\chi}, \omega^{\prime}=\omega_{\chi}+d d^{c} u_{t, \varepsilon}, F_{+}-F_{-}=G_{\varepsilon}$. Indeed, it is clear that $F_{+}$is uniformly upper bounded, we just saw that $F_{ \pm}$are $C \omega_{\chi}$-psh, and we know from the previous section that $u_{t, \varepsilon}$ has a uniform lower bound. Furthermore, $\log \operatorname{tr}_{\omega} \omega^{\prime}-A u+F_{-}$attains its maximum on $X_{0}$ : indeed, $-A u$ tends to $-\infty$ near the boundary of $X_{0}, F_{-}$is bounded (it is even smooth), and $\operatorname{tr}_{\omega} \omega^{\prime}=\Delta_{\omega_{\chi}}\left(\varphi_{t, \varepsilon}+\sum_{i \in I} \log \left(\log \left|s_{i}\right|^{2}\right)^{2}-\chi\right)$ is bounded on $X_{0}$ (we know it for the term $\Delta_{\omega_{\chi}}\left(\varphi_{t, \varepsilon}-\chi\right)$ and it is an elementary computation for the other term).

In conclusion, we may use Proposition 4.9 to obtain the following estimate:
$$\theta+t \omega_{0}+d d^{c} \varphi_{t, \varepsilon} \leqslant M\left(\prod_{i \in I} \log ^{2}\left|s_{i}\right|^{2}\right)^{C} \cdot \prod_{\alpha \in A}\left|s_{\alpha}\right|^{-c_{\alpha} \cdot C} \prod_{a_{j}>0}\left|s_{j}\right|^{-2 a_{j}} \omega_{\chi}$$

For the "reverse inequality", we use the identity
$$\left(\omega_{\chi}+d d^{c} u_{t, \varepsilon}\right)^{n}=e^{u_{t, \varepsilon}+G_{\varepsilon}} \omega_{\chi}^{n}$$
which leads to the inequality
$$\operatorname{tr}_{\omega_{\chi}+d d^{c} u_{t, \varepsilon}} \omega_{\chi} \leqslant e^{-\left(u_{t, \varepsilon}+G_{\varepsilon}\right)}\left(\operatorname{tr}_{\omega_{\chi}}\left(\omega_{\chi}+d d^{c} u_{t, \varepsilon}\right)\right)^{n-1}$$
and therefore
$$\theta+t \omega_{0}+d d^{c} \varphi_{t, \varepsilon} \geqslant M^{-1} \prod_{a_{j}<1} \frac{\left|s_{j}\right|^{2}}{\left(\left|s_{j}\right|^{2}+\varepsilon^{2}\right)^{a_{j}}} \cdot\left(\prod_{i \in I} \log ^{2}\left|s_{i}\right|^{2}\right)^{-C} \cdot \prod_{\alpha \in A}\left|s_{\alpha}\right|^{c_{\alpha} \cdot C} \prod_{a_{j}>0}\left|s_{j}\right|^{2 a_{j}} \omega_{\chi}$$
for some uniform $C, M>0$ (different from the previous ones).

In particular, for any compact set $K \Subset X_{0}$, there exists a constant $C_{K}>0$ satisfying
$$C_{K}^{-1} \omega_{0} \leqslant \theta+t \omega_{0}+d d^{c} \varphi_{t, \varepsilon} \leqslant C_{K} \omega_{0}$$
Using Evans-Krylov theorem and the classical elliptic theory shows that the potential $\varphi_{t, \varepsilon}$ satisfies uniform $\mathscr{C}^{k, \alpha}$ estimates on any $\Omega \subseteq K$ for each $k, \alpha$. Thus the theorem is proved.

Remark 4.10. - One can easily obtain somewhat more precise estimates. Indeed, if $\alpha$ is a nef and big class and $E$ an effective $\mathbb{R}$-divisor such that $\alpha-E$ is ample, then we have in fact that for every $\delta>0, \alpha-\delta E$ is ample (write $\alpha-\delta E=(1-\delta) \alpha+\delta(\alpha-E)$ ). Applying this observation to Theorem 4.6, we see that for every $\delta>0$, there exists $C_{\delta}>0$ such that:
$$\varphi_{\mathrm{KE}} \geqslant \delta \sum c_{\alpha} \log \left|s_{\alpha}\right|^{2}-\sum_{i \in I} \log \left(\log \left|s_{i}\right|^{2}\right)^{2}-C_{\delta}$$
for every $\delta>0$. One could apply the same argument to the Laplacian estimates.
About uniqueness of the Kähler-Einstein metrics. - First of all, in the case where $X$ is smooth and $K_{X}$ is ample, then uniqueness of the Kähler-Einstein metric constructed by Aubin and Yau is a straightforward consequence of the maximum principle. Generalizing this principle to some complete Kähler manifolds in [Yau75], Yau could prove that on a Kähler manifold, there can be only one complete Kähler metric $\omega$ satisfying Ric $\omega=-\omega$. In particular, this result has been applied by Kobayashi and Tian-Yau to show the uniqueness of the Kähler-Einstein metric for a log smooth pair $(X, D)$ satisfying $K_{X}+D$ ample, cf [Kob84, TY87]. Using Yau-Schwarz lemma in a more subtle way (through the notion of almost complete metric), they also show uniqueness when $K_{X}+D$ is only assumed nef, big and ample modulo $D$, which means that $K_{X}+D$ intersects positively every curve not contained in $D$. For example, if $(X, D)$ is a log resolution of some canonically polarized singular variety, these assumptions are not satisfied.

In our situation we proceed in a different manner: we first use the volume assumption (as a replacement for completeness) to show that the Kähler-Einstein metric, originally defined on the (log) regular locus , extends to define a a positive current on X whose local potentials glue to define a solution with full Monge-Amère mass of a global Monge-Ampère equation to which we can apply the comparison principle to finally deduce the uniqueness.

\section*{5. Applications}
5.1. Yau-Tian-Donaldson conjecture for singular varieties. - Let us start with the following converse of Theorem A stated in the introduction.

Proposition 5.1. - Let $X$ be projective variety satisfying the conditions $G_{1}$ and $S_{2}$, and such that $K_{X}$ is $\mathbb{Q}$-ample. If $X$ admits a Kähler-Einstein metric $\omega$ in the following sense: $\omega$ is a $K-E$ metric on $X_{\mathrm{reg}}$ and its total volume there is equal to $K_{X}^{n}$, then $X$ has semi-log canonical singularities.

Proof. - We begin with the case where $X$ is normal.
Let us first show that $\phi:=\log \omega^{n}$ on $X_{\text {reg }}$ extends to an element in $\mathcal{E}\left(X, K_{X}\right)$. By the K-E equation $d d^{c} \phi:=-$ Ric $\omega=\omega \geqslant 0$ and hence, since $X$ is normal, $\phi$ extends to a positively curved singular metric on $K_{X}$ over all of $X$. Thus, writing $\omega=d d^{c} \psi$ for some other such metric $\psi$ the compactness of $X$ forces the K-E equation $\mathrm{MA}(\phi)=e^{\phi}$ (up to shifting $\phi$ by a constant) globally on $X$ (since the non-pluripolar MA does not charge the singular locus of $X$ ). Moreover, by the volume assumption we have that $\int_{X} \mathrm{MA}(\phi)=K_{X}^{n}$ and hence $\phi \in \mathcal{E}\left(X, K_{X}\right)$, as desired.

Next, fix a resolution $\pi: X^{\prime} \rightarrow X$ and assume, to a get a contradiction, that $p^{*} K_{X}=$ $K_{X^{\prime}}+D$ where $D$ is a snc $\mathbb{Q}$-divisor such that $D=D^{\prime}+(1+\delta) E$ for some $\delta>0$, where $D^{\prime}$ is a $\mathbb{Q}$-divisor and $E$ is a smooth irreducible divisor transversal to the support of $D^{\prime}$. Since $\phi$ has maximal MA-mass it follows, as shown in $\left[\mathbf{B B E}^{+} \mathbf{1 1}\right]$ using an Izumi type estimate, that $\pi^{*} \phi$ has no Lelong numbers. In particular, it follows from the characterization of Lelong numbers that there exists a neigbourhood $U$ of $E$ such that $\pi^{*} \phi \geqslant \frac{1}{2} \delta \log \left|s_{E}\right|^{2}-C$ in local trivializations. Moreover, we may take $U$ such that $D$ does not intersect $U$. But then it follows from the K-E equation that
$$K_{X}^{n} \geqslant C^{\prime} \int_{U} e^{\pi^{*} \phi-(1+\delta) \log \left|s_{E}\right|^{2}} \geqslant C^{\prime \prime} \int_{U} e^{-(1+\delta / 2) \log \left|s_{E}\right|^{2}}=\infty,$$
which gives the desired contradiction.

We move on to the general case when $X$ is only assumed to be $G_{1}$ and $S_{2}$. As we observed in §2.3, the result of Proposition 2.6 holds actually in the general $G_{1}$ and $S_{2}$ case (we did not use at all that the singularities were slc); however we should be careful and work instead on a log-resolution of ( $X^{\nu}, C_{X^{\nu}}$ ) because the formula $\nu^{*} K_{X}=K_{X^{\nu}}+C_{X^{\nu}}$ could not be meaningful anymore if $C_{X^{\nu}}$ is not Cartier, cf §2.3 and the remarks following the identity (2.1). So the first conclusion is that the weight $\phi:=\log \omega^{n}$ on $X_{\text {reg }}$ extends on the normalization $X^{\nu}$ to a psh weight in $\mathcal{E}\left(X^{\nu}, \nu^{*} K_{X}\right)$. Then we take a log-resolution $\pi: X^{\prime} \rightarrow X^{\nu}$ of the pair $\left(X^{\nu}, C_{X^{\nu}}\right)$ where $C_{X^{\nu}}$ is the conductor of the normalization; a priori, this is just an effective divisor, possibly non-reduced. We write $\left(X^{\prime}, D^{\prime}\right)$ for the new pair that we obtain on $X^{\prime}$. Then same arguments as earlier show that $D^{\prime}$ has coefficients less than or equal to 1 , which amounts to saying that ( $X^{\nu}, C_{X^{\nu}}$ ) is log canonical, or equivalently that $X$ has semi-log canonical singularities. \(\square\)

To relate this to $K$-stability we recall that Odaka [Oda13] has shown that, if $X$ is $K$ semistable, then $X$ has semi-log canonical singularities (recall that we assume that $X$ is $G_{1}$ and $S_{2}$ and that $K_{X}>0$ ). Conversely, if $X$ is semi-log canonical, then $X$ is $K$-stable [Oda12]. Hence, combining our results with Odaka's results gives the following confirmation of the Yau-Tian-Donaldson conjecture for varieties being $G_{1}$ and $S_{2}$, with $K_{X}$ ample:

Theorem 5.2. - Let $X$ be a $G_{1}$ and $S_{2}$ projective variety such that $K_{X}$ is ample. Then $X$ admits a Kähler-Einstein metric iff $X$ is $K$-stable.

It would be interesting to have a direct analytical proof of the implication "KählerEinstein implies $K$-stable" as shown in [Ber16] the (log) Fano case (where $K$-stability has to be replaced by $K$-polystability in the presence of holomorphic vector fields).
5.2. Automorphism groups of canonically polarized varieties. - The existence and uniqueness of Kähler-Einstein metrics established in Theorem A allows us to give an analytical proof of the following result shown in [BHPS13] (where two proofs were given, one cohomological and one geometric)

Theorem 5.3. - Let $X$ be a stable variety. Then $\operatorname{Aut}(X)$ is finite.
Proof. - First observe that the normalization map $\nu: X^{\nu} \rightarrow X$ induces a morphism $\operatorname{Aut}(X) \rightarrow \operatorname{Aut}\left(X^{\nu}\right)$ which is clearly injective. So we only need to treat the case of a normal stable variety $X$. As $X$ is canonically polarized and every automorphism of $X$ preserves $K_{X}$, the automorphism group of $X$ can be realized the automorphism group of a polarized variety, hence it is an algebraic subgroup of $\operatorname{PGL}(N, \mathbb{C})$ for some $N$, and therefore it has finitely many connected components. It is thus enough to show that this group has dimension 0.

By general results on automorphism groups of normal varieties (see [BBE ${ }^{+}$11, Lemma 5.2] and references therein) it is equivalent to show that any holomorphic vector field $V$ on $X_{\text {reg }}$ vanishes identically. To prove this vanishing we first observe that, by normality, $V$ is the infinitisimal generator of a complex one-parameter family of automorphism $F$ of $X$ and in particular of $X_{\text {reg }}$. Fix a Kähler-Einstein current $\omega$ on $X$. By the naturality of the KE-equation it follows that $F^{*} \omega$ is also a KE-current and hence by uniqueness $F^{*} \omega=\omega$ on $X_{\text {reg }}$. Let us denote by $V_{r}$ and $V_{i}$ the real and imagnary parts of $V$, which are infinitisimal generators of real one parameter families of automorphisms that we will denote by $F_{r}$ and $F_{i}$ respectively, which, by the previous argument, also preserve $\omega$. Next, note that any automorphism automatically lifts to the line bundle $K_{X}$ over $X_{\text {reg }}$ and thus it follows from general principles that the real part $V_{r}$ of $V$ is a Hamiltonian vector field, i.e. $i_{V_{r}} \omega=d h$ for some smooth function $h$ on $X_{\text {reg }}$. But then, by Cartan's formula, the Lie deriviative $L_{V_{i}} \omega$ is given by $d\left(i_{W_{r}} \omega\right)=d J i_{V_{r}} \omega=d J d h=d d^{c} h$. Since the flow $F_{i}$ defined by $V_{i}$ also preserves $\omega$ it thus follows that $d d^{c} h=0$. But by normality it follows that $h=0$ (indeed, by normality $h$ is bounded and we can thus apply the maximum principle on a resolution). Hence $i_{V_{r}} \omega=0$ on $X_{\text {reg }}$, which forces $V_{r}=0$ on $X_{\text {reg }}$, since $\omega$ is Kähler there and in particular pointwise
non-degenerate. Finally, by the same argument $V_{i}=0$ (for example replacing $V$ with $J V$ ) and hence $V=0$ as desired. \(\square\)

Remark 5.4. - In the case when $X$ is smooth there is a simple cohomological proof of the previous proposition: by Serre duality $H^{0}(X, T X)$ is isomorphic to $H^{n-1}\left(X,-K_{X}\right)$, which is trivial by Kodaira vanishing (since $K_{X}$ is ample). In the case when $X$ is log canonical a similar cohomological argument can be used [BHPS13], relying on the Bogomolov-Sommese vanishing result for log canonical singularities, established in [GKKP11, Theorem 7.2]. Indeed, if $V$ does not vanish identically then contracting with $V$ on $X_{\text {reg }}$ maps $K_{X}$ to a rank one reflexive sheaf in $\operatorname{Hom}\left(K_{X}, \Omega_{X}^{[n-1]}\right)$, where $\Omega_{X}^{[n-1]}$ is the sheaf of reflexive $(n-1)$-forms on $X$ and hence by the Bogomolov-Sommese vanishing result in [GKKP11] the Kodaira dimension of $K_{X}$ is at most $n-1$, which contradict the ampleness of $K_{X}$.

\section*{6. Outlook}
6.1. Towards Miyaoka-Yau type inequalities. - For simplicity we will only consider the case $n=2$ (but a similar discussion applies in the general case). We set $E:=\Omega_{X}^{1}$, the cotangent bundle of $X$. The classical case is when $X$ is smooth with $K_{X}$ ample, where the Miyaoka-Yau inequality says
$$c_{1}(E)^{2} \leqslant 3 c_{2}(E) .$$
Let us briefly recall Yau's differential-geometric proof. We equip $E$ with the Hermitian metric induced by $\omega$ and denote by $(E, \omega)$ the corresponding Hermitian vector bundle. Then, if $\omega$ is Kähler-Einstein a direct local calculation gives the point-wise inequality
$$c_{1}(E, \omega)^{2} \leqslant 3 c_{2}(E, \omega)$$
formulated in terms of the Chern-Weil representatives $c_{i}(E, \omega)$ of the corresponding Chern classes. Hence, integrating immediately gives the Miyaoka-Yau inequality. Repeating this argument in the singular case when $X$ a stable surface and using Theorem A gives the following

Proposition 6.1. — The following inequality holds for a stable surface equipped with the canonical Kähler-Einstein metric $\omega$ on its regular part:
$$c_{1}\left(K_{X}\right)^{2} \leqslant 3 \int_{X_{\text {reg }}} c_{2}(E, \omega)$$
with equality iff $\omega$ has constant holomorphic sectional curvature, i.e. $\left(X_{\mathrm{reg}}, \omega\right)$ is locally isometric to a ball.

Proof. - Since the point-wise inequality above still holds, by the KE-condition, we can simply integrate it over $X_{\text {reg }}$ and use that, by Theorem A, $c_{1}\left(K_{X}\right)^{2}=\int_{X_{\text {reg }}} c_{1}(E, \omega)^{2}$. The conditions for equality are well-known in the point-wise inequality. \(\square\)

Since $\omega$ is canonically attached to $X$ one could simply define the rhs appearing in the inequality above as the "analytical second Chern number" $c_{2, \text { an }}(X)$ of $X$. However, it should be stressed that it is not even a priori clear that $c_{2, \text { an }}(X)$ is finite, even though we expect that this is the case. More precisely, we expect that $c_{2, \mathrm{an}}(X)$ can be identified with (or at least bounded from above) by a suitable algebraically defined second Chern class number $c_{2}(X)$. Various definitions of such Chern numbers have been proposed in the litterature and we refer the reader to the paper of Langer [Lan03] where very general algebraic Miyaoka-Yau type inequalities are obtained, which in particular apply to stable surfaces. More generally, as before, our arguments apply to log canonical pairs.
6.2. The Weil-Petersson geometry of the moduli space of stable varieties. - In this section we will briefly explain how the finite energy property of the Kähler-Einstien metric on a stable variety naturally appears in the geometric study of the moduli space $\mathcal{M}$ of all stable varieties. In a nut shell, the Kähler-Einstein metrics on stable varieties induces a metric on the $\mathbb{Q}$-line bundle $\mathcal{L} \rightarrow \mathcal{M}$ over the moduli space defined by the top Deligne pairing of $K_{X}$ and the finite energy condition is precisely the condition which makes sure that the metric is point-wise finite. The relation to Weil-Petterson geometry comes from the well-known fact that the curvature form of the corresponding metric over the moduli space $\mathcal{M}_{0}$ of all smooth stable varieties (i.e. all canonically polarized $n$-dimensional manifolds, with a fixed oriented smooth structure) coincides with the Weil-Petersson metric $\Omega_{W P}$ on $\mathcal{M}_{0}$ [FS90, Sch12].

To be a bit more precise we first recall that given a line bundle $L \rightarrow X$ over a (complex) $n$-dimensional algebraic variety $X$ its top Deligne pairing i.e. the $(n+1)$-fold Deligne pairing of $L$ with itself is a complex line that we will denote by $\langle L\rangle$ [Elk89, Elk90]. Equipping $\langle L\rangle$ with an Hermitian metric $\phi$ (using additive notation as before) induces a Hermitian metric $\langle\phi\rangle$ on $\langle L\rangle$, satisfying the change of metric formula: $\langle\phi\rangle-\langle\psi\rangle=(\mathcal{E}(\phi)-\mathcal{E}(\psi))$ (up to a multiplicative normalization constant), where $\mathcal{E}$ is the energy functional appearing in §3 (compare [PS04]). Fixing a smooth reference metric $\phi_{0}$ on $L$ one can use the latter transformation formula to define the metric $\langle\phi\rangle$ as long as $\phi$ has finite energy. The resulting metric $\langle\phi\rangle$ is then independent of the choice of reference metric $\phi_{0}$. More generally, in the relative case of a flat morphism $\mathcal{X} \rightarrow B$ between integral schemes of relative dimension $n$ and an Hermitian line bundle $L \rightarrow \mathcal{X}$ this construction produces an Hermitian line bundle $\langle L\rangle \rightarrow B$ over the base $B$.

In particular, taking $X$ to be an $n$-dimensional stable variety $L:=K_{X}$ one obtains a canonical metric on the complex line $\left\langle K_{X}\right\rangle$, induced by the finite energy metric on $K_{X}$ determined by the volume form of the Kähler-Einstein metric on the regular locus of $X$.

Let now $\mathcal{M}$ denote the moduli space of all n-dimensional stable varieties with a fixed Hilbert polynomial [Kol13, Kol]. Using the existence of a universal stable family $\mathcal{X}$ (in the sense of Kollar) over a finite cover of each irreducible component of the moduli space one obtains a $\mathbb{Q}$ - line bundle $\mathcal{L}$ over $\mathcal{M}$, induced by the fiber-wise top Deligne pairings $\left\langle K_{X}\right\rangle$. We conjecture that the metric on $\mathcal{L}$ induced by the fiber-wise Kähler-Einstein metrics is
continuous (as in the case of stable curves [Fre12]). Confirming this conjecture would require a more detailed analysis of the dependence of the Kähler-Einstein metric on the complex structure that we leave for the future.

As is well-known the curvature of the corresponding metric over $\mathcal{M}_{0}$ coincides (up to a numerical factor) with the Weil-Petersson metric $\Omega_{W P}$. In particular, it is stricly positive as a form (in the orbifold sense). Under the validity of the previous conjecture one thus obtains a canonical extension of the induced Weil-Petersson metric on $\mathcal{M}_{0}$ to its compactification in $\mathcal{M}$ as a positive current with continuous potentials. It would also be very interesting to know under which assumptions the extension is strictly positive in a suitable sense, for example if it is, locally, the restriction of a Kähler metric? These problems are (e.g. by Grauert's generalization of Kodaira's embedding theorem to singular varities) closely related to the problem of showing that the correponding line bundle $\mathcal{L}$ over the moduli space $\mathcal{M}$ is ample (on each irreducible component) and it should be compared with the recent work of Schumacher [Sch12], where an analytic proof of the quasi-projectivity of $\mathcal{M}_{0}$ is given. As shown by Schumacher the Weil-Petersson metric $\Omega_{W P}$ on $\mathcal{M}_{0}$ admits a (non-canonical) extension as a positive current with analytic singularities to Artin's Moishezon compactifaction of $\mathcal{M}_{0}$. But the conjecture above is closely related to the problem of obtaining a canonical extension of $\Omega_{W P}$ to $\mathcal{M}$ as a positive current with continuous potentials.

Finally, it should be pointed out that the top Deligne pairing used above essentially coincides with Tian's CM-line bundle in this setting (by the Knudson-Mumford expansion and Zhang's isomorphism realizing the Chow divisor as a top Deligne pairing). The ampleness of the induced CM-line bundle over general moduli spaces of $K$-stable polarized varieties was recently speculated on by Odaka [Oda15].
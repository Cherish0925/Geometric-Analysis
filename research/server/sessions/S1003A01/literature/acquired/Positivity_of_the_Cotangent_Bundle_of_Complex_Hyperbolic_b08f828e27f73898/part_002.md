---
retention_scope: session
part: 2
total_parts: 2
---

[Part 2/2 of: Positivity of the Cotangent Bundle of Complex Hyperbolic ...]

Lemma 5.4. For a positive real number $u_{i}$ and sufficiently small $\epsilon>0$, there exists a $C^{2}$ function $\rho_{i}: \mathbb{R}_{>0} \rightarrow \mathbb{R}$ and a constant number $c$ satisfying the following properties:
\begin{itemize}
\item[(1)] $\rho_{i}(u)=-\log (u)+c$ on $\left(0, u_{i}+\epsilon^{\prime}\right]$, where $\epsilon^{\prime}$ is a positive number depending on $\epsilon$.
\item[(2)] $i \partial \bar{\partial} \rho_{i} \geq 0$
\end{itemize}

Let $u=-\frac{t_{i}}{2 \pi} \cdot \log |q|-|\zeta|^{2}$, where $t_{i} \in \mathbb{R}^{+}$, and $(\zeta, q) \in \mathbb{C}^{n-1} \times \mathbb{C}$.
\begin{itemize}
\item[(3)] When $(\zeta, q)$ varies on a compact set with non-empty intersection with $q=0$,
$$\lim _{q \rightarrow 0} \frac{\rho_{i}(u)}{\log |q|}=\frac{1}{2 \pi}\left(d_{i}-\epsilon\right),$$
where $d_{i}=\frac{t_{i}}{u_{i}}$.
\item[(4)] The forms $\bar{\partial}\left(\rho(u)-\frac{1}{2 \pi}\left(d_{i}-\epsilon\right) \log |q|\right)$ and $\partial \bar{\partial}(\rho(u))$ are locally integrable on the set $\left\{(\zeta, q) \in \mathbb{C}^{n-1} \times \mathbb{C} \mid u>u_{0}+\epsilon^{\prime}\right\}$.
\end{itemize}

Proof. Let $\epsilon>0$ be small enough such that there exists $\epsilon^{\prime} \in\left(0, \frac{t_{i}}{4 \pi}\right)$ satisfying $\frac{t_{i}}{u_{i}}-\frac{t_{i}}{u_{i}+2 \epsilon^{\prime}}=\epsilon$ and define $\rho_{i}: \mathbb{R}_{>0} \rightarrow \mathbb{R}$ be the function given by
$$\rho_{i}(u)= \begin{cases}-\log (u)+c_{0} & 0<u<u_{i}+\epsilon^{\prime}, \\ \frac{-u}{u_{i}+2 \epsilon^{\prime}}+c_{1} e^{-a\left(u-u_{i}-\epsilon^{\prime}\right)} & u \geq u_{i}+\epsilon^{\prime},\end{cases}$$
where $a=\frac{1}{\epsilon^{\prime}}+\frac{1}{u_{i}+\epsilon^{\prime}}, c_{1}=\left(\frac{\epsilon^{\prime}}{u_{i}+2 \epsilon^{\prime}}\right)^{2}$, and $c_{0}=-\log \left(u_{i}+\epsilon^{\prime}\right)-c_{1}-\frac{u_{i}+\epsilon^{\prime}}{u_{i}+2 \epsilon^{\prime}}$. Since $a \cdot c_{1}=$ $\frac{\epsilon^{\prime}}{\left(u_{i}+\epsilon^{\prime}\right)\left(u_{i}+2 \epsilon^{\prime}\right)}$, and $a^{2} c_{1}=\frac{1}{\left(u_{i}+\epsilon^{\prime}\right)^{2}}$ its straightforward to see that the function $\rho_{i}$ is $C^{2}$.

As $-u$ is a plurisubharmonic function, and $c_{1}$ and $a$ are positive, $-\log (u)+c_{0}, \frac{-u}{u_{i}+2 \epsilon^{\prime}}+$ $c_{1} e^{-\left(u-u_{i}-\epsilon^{\prime}\right)}$ are plurisubharmonic because the function $-\log (-x)$ when $x<0$ and the function $e^{b x}$ for every $b>0$ are monotonically increasing and convex. Hence, $\rho_{i}(u)$ satisfies the second properties.
$\rho_{i}(u)$ satisfies the third condition since
$$\lim _{q \rightarrow 0} \frac{\rho_{i}(u)}{\log |q|}=\frac{1}{2 \pi} \frac{t_{i}}{u_{i}+2 \epsilon^{\prime}}=\frac{1}{2 \pi}\left(\frac{t_{i}}{u_{i}}-\epsilon\right)=\frac{1}{2 \pi}\left(d_{i}-\epsilon\right) .$$

To check the forth condition note that
$$e^{-a\left(u-u_{i}-\epsilon^{\prime}\right)}=c^{\prime} \cdot e^{-a|\zeta|^{2}} \cdot|q|^{l},$$
where $l=\frac{a \cdot t_{i}}{2 \pi}$ and $c^{\prime}$ is a constant. The inequality $a>\frac{1}{\epsilon^{\prime}}>\frac{4 \pi}{t_{i}}$ gives that $l>2$, the function $|q|^{l}$, and the forms $\bar{\partial}\left(|q|^{l}\right), \partial\left(|q|^{l}\right)$ and $\partial \bar{\partial}\left(|q|^{l}\right)$ are locally integrable and therefore letting $c^{\prime \prime}=\frac{1}{u_{0}+2 \epsilon^{\prime}}$,
$$\partial \bar{\partial}\left(\rho_{i}(u)\right)=\partial \bar{\partial}\left(c^{\prime \prime} \cdot|\zeta|^{2}\right)+\partial \bar{\partial}\left(c^{\prime} e^{-a|\zeta|^{2}}|q|^{l}\right)$$
is a locally integrable form. On the other hand, $\frac{-u}{u_{i}+2 \epsilon^{\prime}}=\left(d_{i}-\epsilon\right) \log |q|+\frac{|\zeta|^{2}}{u_{i}+2 \epsilon^{\prime}}$, in other words,
$$\bar{\partial}\left(\frac{-u}{u_{i}+2 \epsilon^{\prime}}-(d-\epsilon) \log |q|\right)=\bar{\partial}\left(c^{\prime \prime} \cdot|\zeta|^{2}\right),$$
which is a locally integrable form. Hence, $\bar{\partial}\left(\rho(u)-\left(d_{i}-\epsilon\right) \log |q|\right)$ is locally integrable on $\left\{(\zeta, q) \in \mathbb{C}^{n-1} \times \mathbb{C} \mid u>u_{0}+\epsilon^{\prime}\right\}$ as desired. \(\square\)

The main difficulty to prove Theorem A is to prove the following proposition. In the proof, we construct a singular hermitian metric by Preposition 3.3 and Lemma 5.4:

Proposition 5.5. For a sufficiently small $\epsilon>0$, with $r=(d-\epsilon) / 4 \pi$ being rational, the $\mathbb{Q}$-vector bundle
$$\Omega \frac{1}{\bar{X}}(\log (D))\langle-r D\rangle$$
is ample.
Proof. Denote $\Omega_{\bar{X}}^{1}(\log (D))$ by $F$. Suppose $\widetilde{D}$ is the pullback of $D$ by the natural projection
$$\pi: \mathbb{P}(F) \longrightarrow \bar{X} .$$

The goal is to show that the $\mathbb{Q}$-line bundle $O_{\mathbb{P}(F)}(1)-r \widetilde{D}$ is ample, i.e., it intersects positively with every subvariety of $\mathbb{P}(F)$. Since $-r=-(d-\epsilon)<0$ for a sufficiently small $\epsilon>0$, by Proposition 5.3, it is enough to show that $O_{\mathbb{P}(F)}(1)-r \widetilde{D}$ intersects positively with every subvariety of $\mathbb{P}(F)$ that is not contained in $\widetilde{D}$ but possibly intersects with $\widetilde{D}$. Let $V$ be such a subvariety.

Let $a$ and $b$ be positive integer such that $a / b=r$. We show that the line bundle $L=$ $O_{\mathbb{P}(F)}(b) \otimes O_{\mathbb{P}(F)}(-a \widetilde{D})$ intersects positively with $V$ by constructing a singular hermitian metric $\bar{h}$ on $L$ such that $c_{1}(L, \bar{h})^{\operatorname{dim}(V)} \cdot V>0$.

Suppose $D_{i}$ is the component of $D$ compactifing the cusp $c_{i}$ and $D_{i}$ is given by $q_{i}=0$ on the horoball $H_{i}\left(u_{i}\right)$, where $u_{i}=t_{i} / d$. Let $\widetilde{D}_{i}=\pi^{*}\left(D_{i}\right)$ and $\widetilde{H}_{i}\left(u_{i}\right)=\pi^{-1}\left(H_{i}\left(u_{i}\right)\right)$. By Shimuzu's lemma the horoballs are disjoint and therefore $L_{\mid \widetilde{H}_{i}\left(u_{i}\right)}$ naturally isomorphic to $O_{\mathbb{P}(F)}(b) \otimes O_{\mathbb{P}(F)}\left(-a \widetilde{D}_{i}\right)$.

Substituting $u_{i}$ and $\epsilon$ to Lemma 5.4, we obtain a function $\rho_{i}(u)$ and a constant $c$ satisfying the properties in Lemma 5.4. Now, we define a singular hermitian metric
$$\bar{h}\left(s^{b} \otimes \beta\right):=\exp \left(b \cdot\left(-\rho_{i}(u)-\log (u)-c\right)\right) \hat{h}(s)^{b}$$
on $O_{\mathbb{P}(F)}(b) \otimes O_{\mathbb{P}(F)}\left(-a \widetilde{D}_{i}\right)$, where $s^{b}$ is a section of $O_{\mathbb{P}(F)}(b)$ and $\beta$ is the canonical rational section of $-a \widetilde{D}_{i}$ corresponding to 1. As horoballs are disjoint, Lemma 5.4 implies that $\bar{h}$ is
a well-defined metric on $L$ and on the complements of horoballs it equals to $\hat{h}^{b}$. Evaluating $\bar{h}$ at a local generator of $L$ on $\widetilde{H}_{i}\left(u_{i}\right)$ gives
$$\bar{h}\left(s^{b} \otimes \beta q_{i}^{a}\right)=\exp \left(b \cdot\left(-\rho_{i}(u)+2 r \log \left|q_{i}\right|-\log (u)-c\right)\right) \hat{h}(s) .$$

Now, we can compute the curvature current on the horoball $\widetilde{H}_{i}\left(u_{i}\right)$ :
$$\begin{aligned}
{\left[c_{1}(L, \bar{h})\right]=\frac{i}{2 \pi}( } & {\left[\partial \bar{\partial}\left(\rho_{i}(u)-2 r \log \left|q_{i}\right|\right)\right] } \\
& +[\partial \bar{\partial} \log (u)]-[\partial \bar{\partial} \log (\hat{h}(s))])
\end{aligned}$$
By Proposition 3.4, the current $[\partial \bar{\partial} \log (\hat{h}(s))]$ is represented by the form $\partial \bar{\partial} \log (\hat{h}(s))$. Applying Proposition 3.3 to $\Phi_{1}\left(\zeta,\left|q_{i}\right|\right)=\exp \left(\rho_{i}(u)-2 r \log \left|q_{i}\right|\right)$ and $\Phi_{2}\left(\zeta,\left|q_{i}\right|\right)=\exp (-\log (u))$ gives that
$$\left.\left[\partial \bar{\partial}\left(\rho_{i}(u)-2 r \log \left|q_{i}\right|\right)\right)\right]+[\partial \bar{\partial} \log (u)]$$
is represented by the form $\partial \bar{\partial}\left(\rho_{i}(u)-2 r \log \left|q_{i}\right|\right)+\partial \bar{\partial} \log (u)$. By Proposition 3.2, we observe that $\partial \bar{\partial} \log (u)-\partial \bar{\partial} \log (\hat{h}(s))$ is a semi-positive form. On the other hand, Lemma 5.4 gives that the form $\partial \bar{\partial}\left(\rho_{i}(u)-2 r \log \left|q_{i}\right|\right)=i \partial \bar{\partial} \rho_{i}(u)$ is semi-positive. Putting these together, we obtain that $\left[c_{1}(L, \bar{h})\right]$ is represented by a semi-positive form on $\widetilde{H}_{i}\left(u_{i}\right)$.

Note that by Lemma 5.4 we killed the Lelong number of the current $\left[\partial \bar{\partial}\left(\rho_{i}(u)-2 r \log \left|q_{i}\right|\right)\right]$ on $q_{i}=0$, and the currents $[\partial \bar{\partial} \log (u)]$ and $[\partial \bar{\partial} \log (\hat{h}(s))]$ also have 0 Lelong number on $q_{i}=0$ (see the last part of the proof of Proposition 3.4). Therefore, we can apply [Dem92, Corollary 7.6.] and obtain that
$$\int_{V}\left[c_{1}(L, \bar{h})\right]^{\operatorname{dim}(V)} \geq \int_{V_{\mid \pi^{-1}(X)}}\left(\partial \bar{\partial}\left(\rho_{i}(u)+\log (u)-\log (\hat{h}(s))\right)^{\operatorname{dim}(V)} \geq 0 .\right.$$

As $V \cap X \neq \varnothing$, by Proposition 3.2, $V$ has a positive intersection with $L_{\mid \pi^{-1}(X)}$. Since $\bar{h}$ does not depend on $V$, we can conclude that every subvariety $V \subset \mathbb{P}(E)$ that is not entirely contained in $\widetilde{D}$ intersects positively with $L$. \(\square\)

Using Proposition 5.3 together with Proposition 5.5, we can prove Theorem A:
Theorem 5.6. (Theorem A) For every rational $r \in(0, d / 4 \pi)$, the $\mathbb{Q}$-vector bundle
$$\Omega \frac{1}{\bar{X}}(\log (D))\langle-r D\rangle$$
is ample.
Proof. Fix $r=a / b \in(0, d / 4 \pi)$, and choose $\epsilon>0$ such that $r<(d-\epsilon) / 4 \pi$. Putting Proposition 5.5 and Lemma 4.11 together, we get that $\Omega \frac{1}{X}(\log (D))\langle-r D\rangle$ is ample module $D$, i.e. the vector bundle $S^{b} \Omega \frac{1}{\bar{X}}(\log (D)) \otimes O_{\bar{X}}(-a D)$ is ample modulo $D$. Moreover, it follows from Proposition 5.3 that the restricted $\mathbb{Q}$-vector bundle $\Omega \frac{1}{\bar{X}}(\log (D))_{\mid D}\left\langle-r D_{\mid D}\right\rangle$ is ample and therefore by Lemma 4.7 we can conclude that the vector bundle $S^{b} \Omega \frac{1}{\bar{X}}(\log (D)) \otimes O_{\bar{X}}(-a D)$ is ample. \(\square\)

Theorem 5.6 implies that $\Omega \frac{1}{X}(\log (D))$ is a limit of ample $\mathbb{Q}$-vector bundles. Moreover, we show in Corollary 5.7 that $\Omega_{\bar{X}}^{1}(\log (D))$ is ample modulo $D$ and nef. It is previously proved by Cadorél that $\Omega_{\bar{X}}^{1}(\log (D))$ is big and nef ([Cad21b, Theorem 3]).

Corollary 5.7. (Corollary G) The logarithmic cotangent bundle $\Omega \frac{1}{X}(\log (D))$ is ample modulo $D$ and nef.

Proof. Denote $\Omega \frac{1}{X}(\log (D))$ by $F$. Putting Proposition 5.5 and Lemma 4.11 together, we get that $\Omega_{\bar{X}}^{1}(\log (D))$ is ample module $D$.

It is easy to conclude from Theorem 5.6 that $F$ is nef. If $F$ were not nef, then there would be a curve $C \subset \mathbb{P}(F)$ such that the intersection $I:=C \cdot O_{\mathbb{P}(F)}(1)$ is negative. Let $\widetilde{D}=\pi^{*} D$. Choose a small enough $r>0$ such that $I-r(C \cdot \widetilde{D})<0$ and therefore
$$C \cdot\left(O_{\mathbb{P}(F)}(1)-r \widetilde{D}\right)<0,$$
which contradicts the ampleness of $F\langle-r D\rangle$. \(\square\)

\section*{6. Positivity of $\Omega \frac{1}{\bar{X}}$}

Throughout this section, we denote a complex hyperbolic manifold with cusps by $X$, and its smooth toroidal compactification by $\bar{X}$. Additionally, we assume that $\bar{X}$ does not have any orbifold point.

The goal of this section is to prove the results on the positivity of the cotangent bundle, namely Theorem B and Theorem D. Further, we conclude that if the canonical depth of cusps is sufficiently large, then the symmetric differentials on $\bar{X}$ is finitely generated $\mathbb{C}$-algebra.

To pass from positivity on the log-cotangent bundle in the previous section to positivity of the cotangent bundle in this section we consider the following exact sequence of coherent sheaves over $\bar{X}$ :
$$0 \longrightarrow \Omega_{\bar{X}}^{1}(\log (D)) \otimes O_{\bar{X}}(-D) \xrightarrow{\phi} \Omega_{\bar{X}}^{1} \longrightarrow i_{*} \Omega_{D}^{1} \rightarrow 0,$$
where $\phi$ sends $\left(\sum_{i=1}^{n} f_{i} d \zeta_{i}+g \frac{d q}{q}\right) \otimes q$ to $\sum_{i=1}^{n} q f_{i} d \zeta_{i}+g d q$ on an open set $U$ on which the local coordinate of $D$ is given by $q=0$.

Theorem 6.1. (Theorem D) Suppose that the uniform depth of cusps $d$ is greater than $4 \pi$. Then,
$$\Omega_{\bar{X}}^{1}\langle-r D\rangle$$
is ample for all rational $r \in(0,-1+d / 4 \pi)$.
Proof. Let $r=a / b$ with a positive $b$ be a rational number in $(0,-1+d / 4 \pi)$. Since $d>4 \pi$, Theorem 5.6 gives that the $\mathbb{Q}$-vector bundle $\Omega \frac{1}{\bar{X}}(\log (D))\langle(-1-r) D\rangle$ is ample. In particular, $\Omega_{\bar{X}}^{1}(\log (D))\langle(-1-r) D\rangle$ is ample modulo $D$. Note that the exact sequence 20 gives that the vector bundle $\Omega_{\bar{X}}^{1}(\log (D)) \otimes O_{\bar{X}}(-D)$ is a subbundle of $\Omega_{\bar{X}}^{1}$. Therefore, the $\mathbb{Q}$-vector bundle $\Omega_{\bar{X}}^{1}(\log (D))\langle(-1-r) D\rangle$ is a $\mathbb{Q}$-subsheaf of $\Omega_{\bar{X}}^{1}\langle-r D\rangle$. It follows from Lemma 4.10 that $\Omega_{\bar{X}}^{1}\langle-r D\rangle$ is ample modulo $D$, that is, the vector bundle $S^{b} \Omega_{\bar{X}}^{1} \otimes O_{\bar{X}}(-a D)$ is ample modulo
$D$. On the other hand, the restricted bundle $\Omega_{\bar{X} \mid D}^{1}\left\langle-r D_{\mid D}\right\rangle$ is ample thanks to Proposition 5.2. This means that $\left(S^{b} \Omega \frac{1}{\bar{X}} \otimes O_{\bar{X}}(-a D)\right)_{\mid D}$ is ample. Hence, it follows from Lemma 4.7 that $\Omega_{\bar{X}}^{1}\langle-r D\rangle$ is ample. \(\square\)

Theorem 6.2. (Theorem B) Suppose that the uniform depth of cusps $d$ is greater than $4 \pi$. Then, $\Omega \frac{1}{X}$ is ample modulo $D$ and semi-ample.
Proof. Set $E=\Omega \frac{1}{X}$. Since the uniform depth of all cusps is greater then $4 \pi$, Theorem 5.6 implies that $\Omega \frac{1}{\bar{X}}(\log (D)) \otimes O_{\bar{X}}(-D)$ is ample. It therefore follows from 20 and Lemma 4.10 that $E$ is ample modulo $D$.

Let $Y=\mathbb{P}(E), \pi: \mathbb{P}(E) \rightarrow \bar{X}$ be the natural projection and $\widetilde{D}=\pi^{*}(D)$. Given that $E$ is ample modulo $D$ and $E_{\mid D}$ is semi-ample by Proposition 5.2, to show that $E$ is semi-ample, we only need to show that there is a large enough $n$ such that setting $L=O_{Y}(n)$
$$H^{0}(Y, L) \xrightarrow{\phi} H^{0}\left(\widetilde{D}, L_{\mid \widetilde{D}}\right)$$
is surjective. Choose $r \in(0,-1+d / 4 \pi)$. By Theorem 6.1, $\Omega_{\bar{X}}^{1}\langle-r D\rangle$ is ample, i.e., $O_{Y}(1)-$ $r \widetilde{D}$ is ample. We can choose $n$ large enough so that $H^{1}(Y, L-\tilde{n} \widetilde{D})=0$, where $\tilde{n}=n r \in \mathbb{Z}$. Therefore, denoting the restriction of $L$ to the $\tilde{n}$ th order thickening of $\widetilde{D}$ by $L_{\mid \tilde{n} \tilde{D}}$, we obtain
$$H^{0}(Y, L) \xrightarrow{\psi} H^{0}\left(Y, L_{\mid \tilde{n} \tilde{D}}\right)$$
is surjective. Considering the commutative diagram
![](https://cdn.mathpix.com/cropped/8f1b60e9-fac0-4df7-853e-1120a3401e08-25.jpg?height=257&width=515&top_left_y=1413&top_left_x=804)
to conclude that $\phi$ is surjective, it is enough to show that $\eta$ is surjective. To this end, consider the following exact sequence on $\widetilde{D}$ :
$$0 \longrightarrow L(-m \widetilde{D})_{\mid \widetilde{D}} \longrightarrow L_{\mid(m+1) \widetilde{D}} \longrightarrow L_{\mid m \tilde{D}} \longrightarrow 0,$$
where $m$ is a positive integer. We prove that for every $m>0$,
$$H^{0}\left(\widetilde{D}, L_{\mid(m+1) \widetilde{D}}\right) \longrightarrow H^{0}\left(\widetilde{D}, L_{\mid m \tilde{D}}\right)$$
is surjective by showing that $H^{1}\left(\widetilde{D}, L(-m \widetilde{D})_{\mid \widetilde{D}}\right)=0$. This implies that $\eta$ is surjective and therefore $\phi$ is surjective which finishes the proof.

Let $\varphi: D \longrightarrow \operatorname{Spec}(\mathbb{C})$. Applying the exact sequence of low degrees to the composition of the push-forward functor
$$\pi_{*}: S h(\widetilde{D}) \longrightarrow S h(D)$$
and the global section functor $\varphi_{*}$ yields
$$0 \longrightarrow H^{1}\left(D, \pi_{*}\left(L(-m \widetilde{D})_{\mid \widetilde{D}}\right)\right) \longrightarrow R^{1}(\varphi \circ \pi)_{*}\left(L(-m \widetilde{D})_{\mid \widetilde{D}}\right) \longrightarrow H^{0}\left(D, R^{1} \pi_{*}\left(L(-m \widetilde{D})_{\mid \widetilde{D}}\right)\right) .$$

Note that $(\varphi \circ \pi)_{*}$ is the global section functor $H^{0}(\widetilde{D},-)$ and therefore
$$R^{1}(\varphi \circ \pi)_{*}\left(L(-m \widetilde{D})_{\mid \widetilde{D}}\right)=H^{1}\left(\widetilde{D}, L(-m \widetilde{D})_{\mid \widetilde{D}}\right) .$$
Hence, it is sufficient to prove that
$$H^{1}\left(D, \pi_{*}\left(L(-m \widetilde{D})_{\mid \widetilde{D}}\right)\right)=H^{0}\left(D, R^{1} \pi_{*}\left(L(-m \widetilde{D})_{\mid \widetilde{D}}\right)\right)=0 .$$

To prove $H^{0}\left(D, R^{1} \pi_{*}\left(L(-m \widetilde{D})_{\mid \widetilde{D}}\right)\right)=0$, note that $\pi$ is a flat morphism because the fibers of $\pi$ are projective spaces of the same dimension. Since for every $x \in D$, the dimension $h^{1}\left(x, \pi_{*}(L-m \widetilde{D})_{x}\right)=h^{1}\left(\pi^{-1}(x), O_{\mathbb{P}^{n-1}}(n)\right)$ is constant, Grauert's theorem ([Har13, Corollary 12.9]) gives the isomorphism
$$R^{1} \pi_{*}\left(L(-m \widetilde{D})_{\mid \widetilde{D}}\right) \cong H^{1}\left(\mathbb{P}^{n-1}, O_{\mathbb{P}^{n-1}}(n)\right)=0 .$$
Hence $H^{0}\left(D, R^{1} \pi_{*}\left(L(-m \widetilde{D})_{\mid \widetilde{D}}\right)\right)=0$.
To prove $H^{1}\left(D, \pi_{*}\left(L(-m \widetilde{D})_{\mid \widetilde{D}}\right)\right)=0$, note that $\pi_{*}\left(L\left(\begin{array}{ll}-m & \widetilde{D}\end{array}\right)_{\mid \widetilde{D}}\right)=S^{n} \Omega_{\bar{X} \mid D}^{1}\left(-m D_{\mid D}\right)$. Consider the filtration of $S^{n} \Omega_{\bar{X} \mid D}^{1}$ obtained by the exact sequence 18:
$$S^{n} \Omega_{\bar{X} \mid D}^{1}=F^{0} \supseteq F^{1} \supseteq \ldots \supseteq F^{m} \supseteq F^{m+1},$$
with quotients
$$F^{i} / F^{i+1} \cong S^{m-i} \Omega_{D}^{1}\left(-i D_{\mid D}\right)$$
for each $i$. Tensoring the filtration by $-m D_{\mid D}$, we get a filtration for $S^{n} \Omega_{\bar{X} \mid D}^{1}\left(-m D_{\mid D}\right)$ whose successive quotients are $S^{m-i} \Omega_{D}^{1}\left(-j D_{\mid D}\right)$ for some $j>0$. As $D$ is an étale quotient of abelian variety, there exists a finite étale map $f: D^{\prime} \rightarrow D$, where $D^{\prime}$ is an abelian variety. Since $f^{*} \Omega_{D}^{1} \cong \Omega_{D^{\prime}}^{1}$, and $\Omega_{D^{\prime}}^{1}$ is trivial, we get that $f^{*} S^{m-i} \Omega_{D}^{1}\left(-j D_{\mid D}\right)$ is a power of $f^{*}\left(-j D_{\mid D}\right)$. Since the canonical bundle $K_{D^{\prime}}$ is trivial, $f$ is finite and $-D_{\mid D}$ is ample, Kodaira vanishing theorem gives that $H^{1}\left(D^{\prime}, f^{*}\left(-j D_{\mid D}\right)\right)=0$ for every positive integer $j$.

It follows that the successive quotients of the filtration of $S^{n} \Omega_{\bar{X} \mid D}^{1}\left(-m D_{\mid D}\right)$ have vanishing first cohomology. Hence, $H^{1}\left(D, S^{n} \Omega_{\bar{X} \mid D}^{1}\left(-m D_{\mid D}\right)\right)=0$, i.e.,
$$H^{1}\left(D, \pi_{*}\left(L(-m \widetilde{D})_{|\widetilde{D}|}\right)\right)=0 .$$ \(\square\)

Applying [Laz17, Example 2.1.29] to Theorem 6.2, we get that symmetric differentials over $\bar{X}$ forms a finitely generated $\mathbb{C}$-algebra provided that the uniform depth is sufficiently large. More precisely, we get:

Corollary 6.3. (Corollary C) With the same assumption as Theorem 6.2, the graded ring
$$\bigoplus_{n>0} H^{0}\left(\bar{X}, S^{n} \Omega \frac{1}{\bar{X}}\right)$$
is finitely generated $\mathbb{C}$-algebra.

\section*{7. Application to Hyperbolicity of subvarieties}

We follow the same notations as previous section and denote a ball quotient $\Gamma \backslash \mathbb{B}^{n}$ with a torsion-free lattice $\Gamma$ by $X$, the boundary divisor $\bar{X} \backslash X$ by $D$, the toroidal compactification of $X$ by $\bar{X}$ and the uniform depth of cusps by $d$. In addition, we assume that $\bar{X}$ does not have any orbifold point. Let $V$ be an irreducible subvariety of $\bar{X}$ intersecting $X$.

The purpose of this section is to prove the result related to hyperbolicity of $V$. We first prove Corollary E and Corollary F. Further, we prove Corollary H which tells us that the hyperbolicity increases in towers of normal covering in the sense that the minimum volume of subvarieties of $\bar{X}$ intersecting both $X$ and $D$ tends to infinity. Note that, as the components of $D$ are étale quotient of abelian varieties, we can not expect that the hyperbolic volume of a variety entirely contained in $D$ tends to infinity.

Corollary 7.1. (Corollary E) Suppose $V$ is smooth with dimension $m>0$. Then, $\mathbb{Q}$-line bundle
$$K_{V}-(r-1) D_{\mid V}$$
is ample for all rational $r \in\left(0, \frac{m d}{4 \pi}\right)$. Moreover, if $d>4 \pi$ or $m>6$, then $K_{V}$ is ample.
Proof. Let $a$ and $b$ be positive integers such that $a / b<d / 4 \pi$ and let $D^{\prime}$ be $D_{\mid V}$. Since the vector bundle $S^{b} \Omega_{V}^{1}\left(\log \left(D^{\prime}\right)\right) \otimes O_{V}\left(-a D^{\prime}\right)$ is a quotient of
$$\left(S^{b} \Omega_{\bar{X}}^{1}(\log (D)) \otimes O_{\bar{X}}(-a D)\right)_{\mid V},$$
Theorem 5.6 gives that $S^{a} \Omega_{V}^{1}\left(\log \left(D^{\prime}\right)\right) \otimes O_{V}\left(-b D^{\prime}\right)$ is ample and therefore its determinant
$$\frac{b}{m}\binom{m+b-1}{b}\left(K_{V}\left(D^{\prime}\right)\right)-\binom{m+b-1}{b} a D^{\prime}$$
is ample. Scaling yields the first part of the claimed result. The rest follows from the fact that the uniform depth of cusps $d$ is at least 2. \(\square\)

Corollary 7.2. (Corollary F) All subvarieties of $X$ are of general type provided that the uniform depth of cusps is greater than $4 \pi$.

Proof. Let $V_{0}$ be an $m$-dimensional (possibly non-smooth) subvariety of $\bar{X}$ not entirely contained in $D$ and let $\mu: V^{\prime} \rightarrow V_{0}$ be a resolution of singularities. There is a generically surjective homomorphism $\mu^{*} \Omega \frac{m}{\bar{X}} \rightarrow \Omega_{V^{\prime}}^{m}=K_{V^{\prime}}$. Thanks to Theorem 6.2, $\Omega \frac{m}{\bar{X}}$ is ample modulo $D$ and therefore, the pull back $\mu^{*} \Omega_{\bar{X}}^{m}$ is ample modulo $\mu^{*} D$. This implies that $K_{V^{\prime}}$ is in particular big, i.e., $V_{0}$ is of general type. \(\square\)

The volume of a line bundle is a birational invariant and it is positive if and only if the line bundle is big. It turns out that if $L$ is nef, then $\operatorname{vol}(L)=L^{n}$.

In the setting of the compactification of a locally symmetric domain, a natural quantity reflecting the hyperbolicity behaviour is the volume of the log-canonical bundle. In particular, $\operatorname{vol}_{V}\left(K_{V}+D_{\mid V}\right)>0$ if and only if $V$ is of log-general type. In the case of ball quotients, Corollary 5.7 in particular implies $\Omega_{V}^{1}\left(\log D_{\mid V}\right)$ is nef and therefore $K_{V}+D_{\mid V}$ is nef on $V$. Hence,
$$\operatorname{vol}_{V}\left(K_{V}+D_{\mid V}\right)=\left(K_{V}+D_{\mid V}\right)^{m} .$$

We show that the minimum volume of log-canonical bundle of subvarieties of $\bar{X}$ is controlled by the uniform depth of cusps:

Corollary 7.3. Suppose $V$ is a $m$-dimensional smooth subvariety of $\bar{X}$ not entirely contained in $D$. If $l$ is the number of component of $D$ intersecting with $V$, then
$$\operatorname{vol}_{V}\left(K_{V}+D_{\mid V}\right)>m^{m}\left(\frac{d}{4 \pi}\right)^{m} l(m-1)!.$$
Proof. Let $r=\frac{d}{4 \pi}$ and $D^{\prime}$ be $D_{\mid V}$. Since $D$ is a union of étale quotient of abelian varieties with ample conormal bundle $O_{D}(-D)$, we get
$$l \leq \frac{D^{\prime} \cdot\left(-D^{\prime}\right)^{m-1}}{(m-1)!}=\frac{-\left(-D^{\prime}\right)^{m}}{(m-1)!} .$$
On the other hand, Corollary 7.1 implies that $K_{V}-(m r-1) D^{\prime}$ is in particular big and nef. Thus, $\left(K_{V}-(m r-1) D^{\prime}\right)^{m}>0$. On the other hand, $\left(K_{V}+D^{\prime}\right)_{\mid D^{\prime}}$ is nef and $-D_{\mid D^{\prime}}^{\prime}$ is ample. Consequently, for every $0<i<m$,
$$\left(K_{V}+D^{\prime}\right)^{m-i}\left(-D^{\prime}\right)^{i}=-\left(\left(K_{V}+D^{\prime}\right)_{\mid D^{\prime}}\right)^{m-i}\left(-D_{\mid D^{\prime}}^{\prime}\right)^{i-1}$$
is non-positive. Hence, $\left(K_{V}-(m r-1) D^{\prime}\right)^{m}>0$ yields that
$$\left(K_{V}+D^{\prime}\right)^{m}>-(r m)^{m}\left(-D^{\prime}\right)^{m} .$$
Combining this with the inequality 21 gives the desired inequality. \(\square\)

Remark 7.4. Parker's generalization of Shimizu's lemma [Par98, Proposition 2.4.] gives that the uniform depth of cusps is at least 2. Plugging in this result to Corollary 7.3 gives that if $V$ intersects $D$, then $V$ is of log general type. This can be concluded from the recent result of Guenancia [Gue22, Theorem B] as well.

We also get a uniform lower bound for the volume of the canonical bundles of subvarieties:
Corollary 7.5. If the canonical depth of cusps $d$ is greater than $4 \pi$, then
$$\operatorname{vol}_{V}\left(K_{V}\right) \geq\left(\frac{m d}{4 \pi}-1\right)^{m} l(m-1)!$$
Proof. Since $d>4 \pi$, by Corollary 7.1 we get that $K_{V}$ is ample and therefore $\operatorname{vol}_{V}\left(K_{V}\right)=K_{V}^{m}$. Let $r=\frac{d}{4 \pi}$ and $D^{\prime}$ be $D_{\mid V}$. As sated in the proof of Corollary 7.3, $\left(K_{V}-(m r-1) D^{\prime}\right)^{m}>0$. Since $K_{V \mid D^{\prime}}$ and $-D_{D^{\prime}}^{\prime}$ are ample, for every $0<i<m$,
$$K_{V}^{m-i} \cdot\left(-D^{\prime}\right)^{i} \cong-\left(K_{V \mid D^{\prime}}\right)^{m-i} \cdot\left(-D_{\mid D^{\prime}}^{\prime}\right)^{i-1}$$
is negative. Hence, $\left(K_{V}-(m r-1) D^{\prime}\right)^{m}>0$ together with the inequality 21 yields that
$$K_{V}^{m} \geq-(r m-1)^{m}\left(-D^{\prime}\right)^{m} \geq(r m-1)^{m} l(m-1)!$$ \(\square\)

As a generalization of Brunebarbe's work [Bru20a], for towers of ball quotients we show that:

Corollary 7.6. (Corollary H) Let $\left\{X_{i}\right\}_{i=1}^{\infty}$ be a tower of $X=X_{1}$. Suppose that toroidal compactification of $X_{i}$ does not have any orbifold points. Then, given a positive number $v$, for all but finitely many $i$, every subvariety $V$ of $X_{i}$ containing a cusp of $X_{i}$ have $\operatorname{vol}\left(K_{V}\right)>v$.

Proof. Combining Lemma 2.6 and Corollary 7.5 gives the result. \(\square\)

\section*{References}
\begin{itemize}
\item[] [ADT22] Kenneth Ascher, Kristin DeVleming, and Amos Turchet. Hyperbolicity and uniformity of varieties of log general type. Int. Math. Res. Not. IMRN, (4):2532-2581, 2022.
\item[] [AMRT10] Avner Ash, David Mumford, Michael Rapoport, and Yung-Sheng Tai. Smooth compactifications of locally symmetric varieties. Cambridge Mathematical Library. Cambridge University Press, Cambridge, second edition, 2010. With the collaboration of Peter Scholze.
\item[] [AV65] Aldo Andreotti and Edoardo Vesentini. Carleman estimates for the laplace-beltrami equation on complex manifolds. Publications Mathématiques de l'IHÉS, 25:81-130, 1965.
\item[] [BB66] Walter L Baily and Armand Borel. Compactification of arithmetic quotients of bounded symmetric domains. Annals of mathematics, pages 442-528, 1966.
\item[] [BD18] Damian Brotbek and Ya Deng. On the positivity of the logarithmic cotangent bundle. Ann. Inst. Fourier (Grenoble), 68(7):3001-3051, 2018.
\item[] $\left[\mathrm{BKK}^{+} 15\right]$ Thomas Bauer, Sándor J Kovács, Alex Küronya, Ernesto C Mistretta, Tomasz Szemberg, and Stefano Urbinati. On positivity and base loci of vector bundles. European Journal of Mathematics, 1(2):229-249, 2015.
\item[] [Bou02] Sébastien Boucksom. On the volume of a line bundle. International Journal of Mathematics, 13(10):1043-1063, 2002.
\item[] [Bru18] Yohan Brunebarbe. Symmetric differentials and variations of hodge structures. Journal für die reine und angewandte Mathematik (Crelles Journal), 2018(743):133-161, 2018.
\item[] [Bru20a] Yohan Brunebarbe. Increasing hyperbolicity of varieties supporting a variation of hodge structures with level structures. arXiv preprint arXiv:2007.12965, 2020.
\item[] [Bru20b] Yohan Brunebarbe. A strong hyperbolicity property of locally symmetric varieties. Ann. Sci. Éc. Norm. Supér. (4), 53(6):1545-1560, 2020.
\item[] [BT18a] Benjamin Bakker and Jacob Tsimerman. The geometric torsion conjecture for abelian varieties with real multiplication. Journal of Differential Geometry, 109(3):379-409, 2018.
\item[] [BT18b] Benjamin Bakker and Jacob Tsimerman. The kodaira dimension of complex hyperbolic manifolds with cusps. Compositio Mathematica, 154(3):549-564, 2018.
\item[] [Cad21a] Benoit Cadorel. Subvarieties of quotients of bounded symmetric domains. Mathematische Annalen, pages 1-38, 2021.
\item[] [Cad21b] Benoît Cadorel. Symmetric differentials on complex hyperbolic manifolds with cusps. J. Differential Geom., 118(3):373-398, 2021.
\item[] [CP15] Frédéric Campana and Mihai Păun. Orbifold generic semi-positivity: an application to families of canonically polarized manifolds. In Annales de l'Institut Fourier, volume 65, pages 835-861, 2015.
\item[] [DCDC15] Gabriele Di Cerbo and Luca F Di Cerbo. Effective results for complex hyperbolic manifolds. Journal of the London Mathematical Society, 91(1):89-104, 2015.
\item[] [Dem92] Jean-Pierre Demailly. Regularization of closed positive currents and intersection theory. J. Algebraic Geom, 1(3):361-409, 1992.
\item[] [ES14] Vincent Emery and Matthew Stover. Covolumes of nonuniform lattices in pu (n, 1). American Journal of Mathematics, 136(1):143-164, 2014.
\item[] [Fuj83] Takao Fujita. Semipositive line bundles. J. Fac. Sci. Univ. Tokyo Sect. IA Math., 30(2):353-378, 1983.
\item[] [GK73] Phillip Griffiths and James King. Nevanlinna theory and holomorphic mappings between algebraic varieties. 1973.
\end{itemize}
\begin{itemize}
\item[] [Gue22] Henri Guenancia. Quasiprojective manifolds with negative holomorphic sectional curvature. Duke Mathematical Journal, 171(2):417-442, 2022.
\item[] [Hö5] Lars Hörmander. $L^{2}$ estimates and existence theorems for the $\bar{\partial}$ operator. Acta Math., 113:89-152, 1965.
\item[] [Har13] Robin Hartshorne. Algebraic geometry, volume 52. Springer Science \& Business Media, 2013.
\item[] [Hir84] Friedrich Hirzebruch. Chern numbers of algebraic surfaces. Mathematische Annalen, 266(3):351-356, 1984.
\item[] [HT06] Jun-Muk Hwang and Wing-Keung To. Uniform boundedness of level structures on abelian varieties over complex function fields. Mathematische Annalen, 335(2):363-377, 2006.
\item[] [Hum98] Christoph Hummel. Rank one lattices whose parabolic isometries have no rotational part. Proceedings of the American Mathematical Society, pages 2453-2458, 1998.
\item[] [Kol85] János Kollár. Subadditivity of the kodaira dimension: fibers of general type. Algebraic geometry, Sendai, 10:361-398, 1985.
\item[] [Laz04] Robert Lazarsfeld. Positivity in algebraic geometry. II, volume 49 of Ergebnisse der Mathematik und ihrer Grenzgebiete. 3. Folge. A Series of Modern Surveys in Mathematics [Results in Mathematics and Related Areas. 3rd Series. A Series of Modern Surveys in Mathematics]. Springer-Verlag, Berlin, 2004. Positivity for vector bundles, and multiplier ideals.
\item[] [Laz17] Robert K Lazarsfeld. Positivity in algebraic geometry I: Classical setting: line bundles and linear series, volume 48. Springer, 2017.
\item[] [Mem23] Soheil Memarian. Volumes of subvarieties of complex ball quotients and sparsity of rational points. arXiv preprint arXiv:2310.08060, 2023.
\item[] [MG78] Barry Mazur and Dorian Goldfeld. Rational isogenies of prime degree. Inventiones mathematicae, 44:129-162, 1978.
\item[] [Mok12] Ngaiming Mok. Projective algebraicity of minimal compactifications of complex-hyperbolic space forms of finite volume. In Perspectives in analysis, geometry, and topology, volume 296 of Progr. Math., pages 331-354. Birkhäuser/Springer, New York, 2012.
\item[] [Mum77] David Bryant Mumford. Hirzebruch's proportionality theorem in the non-compact case. Inventiones mathematicae, 1977.
\item[] [Nad89] Alan Michael Nadel. The nonexistence of certain level structures on abelian varieties over complex function fields. Annals of Mathematics, 129(1):161-178, 1989.
\item[] [Par98] John R Parker. On the volumes of cusped, complex hyperbolic manifolds and orbifolds. Duke mathematical journal, 94(3):433-464, 1998.
\item[] [SB05] Nicholas I Shepherd-Barron. Perfect forms and the moduli space of abelian varieties. arXiv preprint math/0502362, 2005.
\item[] [Shi71] Gorō Shimura. Introduction to the arithmetic theory of automorphic functions, volume 1. Princeton university press, 1971.
\item[] [SY16] Yum-Tong Siu and Shing-Tung Yau. Compactification of negatively curved complete kahler manifolds of finite volume. In Seminar on Differential Geometry.(AM-102), Volume 102, pages 363-380. Princeton University Press, 2016.
\item[] [Wil95] Andrew Wiles. Modular elliptic curves and fermat's last theorem. Annals of mathematics, 141(3):443-551, 1995.
\item[] [Won18] Kwok-Kin Wong. On effective existence of symmetric differentials of complex hyperbolic space forms. Math. Z., 290(3-4):711-733, 2018.
\item[] [Yeu94] Sai Kee Yeung. Betti numbers on a tower of coverings. Duke Mathematical Journal, 73(1):201-226, 1994.
\end{itemize}

Dept. of Mathematics, University of Toronto, Toronto, Canada.
Email address: soheil.memarian@mail.utoronto.ca
---
retention_scope: session
part: 3
total_parts: 4
---

[Part 3/4 of: Families of singular Kähler–Einstein metrics]

We fix $\Theta$ a closed differential (1,1)-form on $\mathcal{X}$ which represents $c_{1}\left(K_{\mathcal{X} / \mathbb{D}}\right) \in H_{\partial \bar{\partial}}^{1,1}(\mathcal{X})$ and set $\theta_{t}=\Theta_{\mid X_{t}}$. Shrinking D if necessary and rescaling, we can assume without loss of generality that
$$-\omega \leqslant \Theta \leqslant \omega .$$

Lemma 5.2. - In the Setting 5.1, the quantity $\operatorname{vol}\left(K_{X_{t}}\right)$ is independent of $t \in \mathbb{D}$.
Proof. - We work in two steps. First, we assume that the family $\pi: \mathcal{X} \rightarrow \mathbb{D}$ is projective, i.e. there exists a positive line bundle $L$ over $\mathcal{X}$. In that case, we know that the invariance of plurigenera holds [Siu98, Pău07] in that the function $t \mapsto h^{0}\left(X_{t}, m K_{X_{t}}\right)$ is constant on $\mathbb{D}$, without even assuming that $X_{t}$ is of general type for all $t$. In particular, it would even be enough to assume that only $X_{0}$ is of general type from which it results that $X_{t}$ is of general type for all $t$ and that the volume $\operatorname{vol}\left(K_{X_{t}}\right)$ is independent of $t$.

Coming back to the general case, we know that $K_{\mathcal{X} / \mathbb{D}}$ is big. Thanks to Demailly's regularization theorem, there exists a Kähler current $T \in c_{1}\left(K_{\mathcal{X} / \mathbb{D}}\right)$ with analytic singularities along $V(\mathcal{I})$ for some ideal sheaf $\mathcal{I} \subset \mathcal{O}_{\mathcal{X}}$. Let $f: \mathcal{X}^{\prime} \rightarrow \mathcal{X}$ be a log resolution of $(\mathcal{X}, \mathcal{I})$. By Hironaka's theorem, we know that one can construct such a morphism $f$ by a sequence of blow-ups along smooth centers only. We write $f^{*} T=T^{\prime}+[F]$ for some smooth semipositive form $T^{\prime}$ on $\mathcal{X}^{\prime}$ and some effective divisor $F$. Remark that this sequence may be infinite; however, the centers project onto a locally finite family of subsets of $\mathcal{X}$. Up to co-restricting $f$ to $\pi^{-1}(K)$ for some compact subset $K \in \mathbb{D}$, one can assume that $f$ is a finite composition of blow-ups and that $T^{\prime} \geqslant \delta \pi^{*} \omega$ for some $\delta>0$ small enough.

Let $E$ be the exceptional divisor of $f$, with irreducible components $E=\sum_{k=1}^{N} E_{k}$. A classical argument (cf e.g. [DP04, Lem. 3.5]) allows one to find smooth (1,1)-forms $\theta_{E_{k}} \in c_{1}\left(E_{k}\right)$ with support in an arbitrarily small neighborhood of $E_{k}$ along with positive numbers $\left(a_{k}\right)$ such that the sum $\theta=\sum_{k} a_{k} \theta_{k}$ defines a (1,1)-form on $\mathcal{X}^{\prime}$ which is negative definite along the fibers of $f$. It follows that for $\varepsilon>0$ small enough, the smooth form $\pi^{*} \omega-\varepsilon \theta_{E}$ is Kähler. In particular, $T^{\prime}-\delta \varepsilon \theta$ is a Kähler form whose cohomology class belongs to $\mathrm{NS}_{\mathbb{R}}\left(\mathcal{X}^{\prime}\right)$. This implies that the Kähler cone of $\mathcal{X}^{\prime}$ meets $\mathrm{NS}_{\mathbb{Z}}\left(\mathcal{X}^{\prime}\right)$, i.e. $\pi \circ f$ is projective.

Let $X_{t}^{\prime}:=f^{-1}\left(X_{t}\right)$ and let $K^{\circ} \subset K$ be the set of regular value of $\pi \circ f$. For any $t \in K^{\circ}$, the map $\left.f\right|_{X_{t}^{\prime}}: X_{t}^{\prime} \rightarrow X_{t}$ is birational hence $\operatorname{vol}\left(K_{X_{t}^{\prime}}\right)=\operatorname{vol}\left(K_{X_{t}}\right)$. By the first step, the volume $\operatorname{vol}\left(K_{X_{t}^{\prime}}\right)$ is independent of $t \in K^{\circ}$, hence the same holds for $\operatorname{vol}\left(K_{X_{t}}\right)$. The set $K \backslash K^{\circ}$ is finite and without loss of generality, one can assume that it consists of the single element $\{0\}$. The fiber $X_{0}^{\prime}$ can be decomposed as $X_{0}^{\prime}=Y_{0}+\sum E_{i}$ where $\left.f\right|_{Y_{0}}: Y_{0} \rightarrow X_{0}$ is birational and $E_{i}$ is contracted by $\left.f\right|_{X_{0}^{\prime}}$. Let $Y_{0}^{\prime} \rightarrow Y_{0}$ be a resolution of singularities. By [Tak07, Thm. 1.2], we have $\operatorname{vol}\left(K_{Y_{0}^{\prime}}\right) \leqslant \operatorname{vol}\left(K_{X_{t}^{\prime}}\right)$ for $t \neq 0$. As $X_{0}$ and
$Y_{0}^{\prime}$ are smooth and birational, we have $\operatorname{vol}\left(K_{X_{0}}\right)=\operatorname{vol}\left(K_{Y_{0}^{\prime}}\right) \leqslant \operatorname{vol}\left(K_{X_{t}}\right)$. Finally, as the function $t \mapsto \operatorname{vol}\left(K_{X_{t}}\right)$ is upper semi-continous, we have $\operatorname{vol}\left(K_{X_{0}}\right)=\operatorname{vol}\left(K_{X_{t}}\right)$ for any $t \in K$. The lemma is proved. \(\square\)

Remark 5.3. - In the last step of the proof of Lemma 5.2, we could also use the existence of relative minimal models, provided $\mathbb{D}$ is replaced by a quasi-projective smooth curve $C$. The general fiber of the projective morphism $\mathcal{X}^{\prime} \rightarrow C$ is a projective variety of general type, hence it admits a good minimal model over $\mathbb{C}$ by [BCHM10]. By [Fuj16, Thm. 3.3] and [Tak19, Cor. 1.2], it follows that $\mathcal{X}^{\prime} \rightarrow C$ admits a birational model $\phi: \mathcal{X}^{\prime} \rightarrow \mathcal{X}^{\prime \prime}$ over $C$ such that: $\phi^{-1}$ does not contract any divisor, every fiber $X_{t}^{\prime \prime}$ of $\mathcal{X}^{\prime \prime} \rightarrow C$ has canonical singularities and satisfies that $K_{\mathcal{X}_{t}^{\prime \prime}}$ is semiample and big. For any $t \in C$, one has $\operatorname{vol}\left(K_{X_{t}^{\prime \prime}}\right)=\left(K_{X_{t}^{\prime \prime}}^{n}\right)$. By flatness, this quantity does not depend on $t$. Finally, we claim that $X_{0}^{\prime \prime}$ is birational to $X_{0}$. This is a combination of the following two facts. First, the variety $X_{0}^{\prime \prime}$ has canonical singularities and $K_{X_{0}^{\prime \prime}}$ is big hence it is of general type and, in particular, it is not uniruled. Next, $X_{0}^{\prime \prime}$ is birational to a component of $X_{0}^{\prime}$ and all of them but the strict transform of $X_{0}$ by $f$ are covered by rational curves as $f$ is a composition of blow-ups of smooth centers from a smooth manifold.

The positive $(n, n)$-forms $\left(\omega_{t}^{n}\right)_{t \in \mathbb{D}}$ induce a smooth hermitian metric on $-K_{\mathcal{X} / \mathbb{D}}$. Since $[\Theta]=c_{1}\left(K_{\mathcal{X} / \mathbb{D}}\right) \in H_{\partial \bar{\partial}}^{1,1}(\mathcal{X})$; there exists a smooth function $\widetilde{h}$ on $\mathcal{X}$ such that
$$-d d_{\mathcal{X}}^{c} \log \omega_{t}^{n}=-\Theta+d d_{\mathcal{X}}^{c} \widetilde{h}$$
We will denote by $\widetilde{h}_{t}:=\left.\widetilde{h}\right|_{X_{t}}$ the restriction to the fiber $X_{t}$. The function $\widetilde{h}$ becomes unique (and remains smooth) after one imposes the following normalization
$$\int_{X_{t}} \widetilde{h}_{t} \omega_{t}^{n}=0 .$$
We define a function $h$ on $\mathcal{X}$ by imposing that $h_{t}:=\left.h\right|_{X_{t}}$ satisfies
$$h_{t}=\widetilde{h}_{t}-\log \left(\frac{1}{V_{t}} \int_{X_{t}} e^{\widetilde{h}_{t}} \omega_{t}^{n}\right) .$$
In particular, one has
$$\int_{X_{t}} e^{h_{t}} \omega_{t}^{n}=V_{t}:=\operatorname{vol}\left(K_{X_{t}}\right)$$
As $\widetilde{h}$ is smooth on $\mathcal{X}$, one has the following obvious consequence.
Lemma 5.4. - Given any compact subset $K \Subset \mathbb{D}$, one has
$$\sup _{t \in K}\left\|h_{t}\right\|_{L^{\infty}\left(X_{t}\right)}<+\infty .$$

It follows from [BEGZ10], a generalization of the Aubin-Yau theorem [Aub78, Yau78], that there exists a unique Kähler-Einstein current on $X_{t}$. This is a positive closed current $T_{t}$ in $c_{1}\left(K_{X_{t}}\right)$ which, by [EGZ09, BCHM10], is a smooth Kähler form in the ample locus $\operatorname{Amp}\left(K_{X_{t}}\right)$, where it satisfies the Kähler-Einstein equation
$$\operatorname{Ric}\left(T_{t}\right)=-T_{t} .$$

It can be written $T_{t}=\theta_{t}+d d^{c} \varphi_{t}$, where $\varphi_{t}$ is the unique $\theta_{t}$-psh function with minimal singularities that satisfies the complex Monge-Ampère equation
$$\left(\theta_{t}+d d^{c} \varphi_{t}\right)^{n}=e^{\varphi_{t}+h_{t}} \omega_{t}^{n} \quad \text { on } \operatorname{Amp}\left(K_{X_{t}}\right) .$$
The minimal singularity assertion is equivalent to the following uniform bound: for all $x \in X_{t}$,
$$-M_{t} \leqslant\left(\varphi_{t}(x)-\sup _{X_{t}} \varphi_{t}\right)-V_{\theta_{t}}(x) \leqslant 0,$$
where
$$V_{\theta_{t}}(x)=\sup \left\{u_{t}(x) ; u_{t} \in \operatorname{PSH}\left(X_{t}, \theta_{t}\right) \text { and } u_{t} \leqslant 0\right\} .$$
We can choose $M_{t}$ independent of $t$ by using Theorem 1.9:
Theorem 5.5. - In Setting 5.1, let $K \Subset \mathbb{D}$ be a compact subset. There exists a constant $M_{K}$ such that for all $x \in \pi^{-1}(K)$, one has
$$-M_{K} \leqslant \varphi_{t}(x)-V_{\theta_{t}}(x) \leqslant M_{K}$$
where $t=\pi(x)$.
Proof. - From Lemma 5.2, it follows that the volume $V_{t}$ of $K_{X_{t}}$ is independent of $t$. We denote it by $V$.
Set $\mu_{t}=e^{h_{t}} \omega_{t}^{n} / V$ and recall that this is a probability measure, by our choice of normalization. We first observe that
$$0 \leqslant \sup _{X_{t}} \varphi_{t} \leqslant-\inf _{\pi^{-1}(K)} h \leqslant C_{K} .$$

Let us first prove the left-hand side inequality. As the measures
$$\frac{1}{V}\left(\theta_{t}+d d^{c} \varphi_{t}\right)^{n}=e^{\varphi_{t}} \mu_{t}$$
have mass one, one has
$$1 \leqslant \int_{X_{t}} e^{\sup _{X_{t}} \varphi_{t}} d \mu_{t}=e^{\sup _{X_{t}} \varphi_{t}}$$
and therefore, $\sup _{X_{t}} \varphi_{t} \geqslant 0$.
To prove the inequality in the middle in (5.2), we observe that, since $\theta_{t} \leqslant \omega_{t}, \varphi_{t}$ is a subsolution of the equation
$$\left(\omega_{t}+d d^{c} \varphi_{t}\right)^{n} \geqslant\left(\theta_{t}+d d^{c} \varphi_{t}\right)^{n}=e^{\varphi_{t}+h_{t}} \omega_{t}^{n},$$
while the constant function $u_{t}(x)=-\inf _{\pi^{-1}(K)} h$ is a supersolution of the same equation,
$$\left(\omega_{t}+d d^{c} u_{t}\right)^{n}=\omega_{t}^{n} \leqslant e^{u_{t}+h_{t}} \omega_{t}^{n} .$$
It follows from the comparison principle [GZ17, Prop. 10.6] that $\varphi_{t} \leqslant-\inf _{\pi^{-1}(K)} h$. The rightmost inequality in (5.2) follows from Lemma 5.4 above.

We can thus rewrite the complex Monge-Ampère equation as
$$\frac{1}{V}\left(\theta_{t}+d d^{c} \psi_{t}\right)^{n}=e^{\psi_{t}+\sup _{X_{t}} \phi_{t}} \mu_{t}=f_{t} \mu_{t},$$
where $\psi_{t}=\varphi_{t}-\sup _{X_{t}} \varphi_{t}$ and $f_{t}=\exp \left(\psi_{t}+\sup _{X_{t}} \varphi_{t}\right)$. Combining the inequalities $\psi_{t} \leqslant 0$ and (5.2), it follows that the densities $f_{t}$ are uniformly bounded.

Recall that $\pi$ is smooth so, in particular, it is locally trivial. Therefore, Theorem 3.4 applies and we can now appeal to Theorem 1.9 with $p=+\infty$ and $0<\alpha<\alpha(\Theta, \mathcal{X})$ and obtain
$$-M_{K} \leqslant \psi_{t}-V_{\theta_{t}} \leqslant 0 .$$
Note that one used here that the volumes $V_{t}$ stay away from zero. The conclusion follows since $\psi_{t}-\varphi_{t}$ is uniformly bounded by (5.2). \(\square\)

Remark 5.6. - Set
$$V_{\Theta}(x)=V_{\theta_{\pi(x)}}(x) .$$
and
$$\phi(x):=\varphi_{\pi(x)}(x) .$$
It is tempting to compare $\phi$ to
$$\hat{V}_{\Theta}=\sup \{u \in \operatorname{PSH}(\mathcal{X}, \Theta) ; u \leqslant 0\} .$$
Clearly $\hat{V}_{\Theta} \leqslant V_{\Theta}$ hence $\hat{V}_{\Theta}-M_{K} \leqslant \phi$. It follows from [CGP21, Thm. A] that $\phi$ is $\Theta$-psh on $\mathcal{X}$, thus $\phi-\sup _{\pi^{-1}(K)} \phi \leqslant \hat{V}_{\Theta}$ and
$$-M_{K} \leqslant \phi-\hat{V}_{\Theta} \leqslant M_{K} .$$

Remark 5.7. - The same results can be proved if the family $\pi: \mathcal{X} \rightarrow \mathbb{D}$ is replaced by a smooth family $\pi:(\mathcal{X}, B) \rightarrow \mathbb{D}$ of pairs $\left(X_{t}, B_{t}\right)$ of log general type, i.e. such that $\left(X_{t}, B_{t}\right)$ is klt and $K_{X_{t}}+B_{t}$ is big for all $t \in \mathbb{D}$.
5.2. Stable varieties. - A stable variety is a projective variety $X$ such that
\begin{itemize}
\item[1.] $X$ has semi-log-canonical singularities.
\item[2.] The Q-line bundle $K_{X}$ is ample.
\end{itemize}
We refer to [KSB88, Ale96, Kar00, Kov13, Kol] for a detailed account of these varieties and their connection to moduli theory.

In [BG14], it was proved that a stable variety admits a unique Kähler-Einstein metric $\omega$. There are several equivalent definitions for such an object, but the simplest is probably the following:

Definition 5.8. - A Kähler-Einstein metric $\omega$ on a stable variety is a smooth Kähler metric on $X_{\text {reg }}$ such that
$$\operatorname{Ric}(\omega)=-\omega \quad \text { and } \quad \int_{X_{\text {reg }}} \omega^{n}=\left(K_{X}^{n}\right)$$
if $n=\operatorname{dim}_{\mathbb{C}} X$.
It is proved in loc. cit. that $\omega$ extends canonically across $X_{\text {sing }}$ to a closed, positive current in the class $c_{1}\left(K_{X}\right)$. It is desirable to understand the singularities of $\omega$ near $X_{\text {sing }}$. In [GW16, Thm. B], it is proved that $\omega$ has cusp singularities near the double crossings of $X$. Moreover, it is proved in [Son17] that the potential $\varphi$ of $\omega$ with respect to a given Kähler form $\omega_{X} \in c_{1}\left(K_{X}\right)$, i.e. $\omega=\omega_{X}+d d^{c} \varphi$, is locally bounded on the klt locus of $X$. More precisely, given any divisor $D=(s=0) \sim_{\mathrm{Q}} K_{X}$ containing the non-klt locus of $X$ and given any $\varepsilon>0$, there exists a constant $C_{\varepsilon}>0$ such that
$$\varphi \geqslant \varepsilon \log |s|^{2}-C_{\varepsilon},$$
where $|\cdot|$ is some smooth hermitian metric on $\mathcal{O}_{X}(D)$. We wish to refine that estimate and obtain a version for families of canonically polarized manifolds degenerating to a stable variety. For that purpose, we introduce the following definition.

Given a log resolution of singularities $f: Y \rightarrow X$ write $K_{Y}=f^{*} K_{X}+\sum_{i \in I} a_{i} E_{i}$ where $E=\sum_{i \in I} E_{i}$ is a divisor with simple normal crossings whose components are either exceptional or sit above the divisorial components of $\operatorname{Sing}(X)$. We set $J:=\left\{i \in I ; a_{i}=\right.$ $-1\}$ which we assume to be non-empty and define the non-klt locus of $X$ by $\operatorname{Nklt}(X)=$ $\cup_{j \in J} f\left(E_{j}\right)$; it is independent of $f$. Given $K \subset I$, we set $E_{K}=\cap_{i \in K} E_{i}$ and introduce the invariants
$$v(f):=\max \left\{|K| ; K \subset J, E_{K} \neq \varnothing\right\}, \quad \text { and } \quad v:=\inf _{f}\{v(f)\}$$
where the infimum is taken over all the log resolutions of $X$. We have $v \in\{1, \ldots, n\}$.
Proposition 5.9. - Let $X$ be a stable variety of dimension $n$ and let $\omega_{X} \in c_{1}\left(K_{X}\right)$ be a Kähler metric. Next, let $\omega=\omega_{X}+d d^{c} \varphi$ be the Kähler-Einstein metric of $X$. Let $D=(s=0)$ be a divisor containing the non-klt locus of $X$ and let $|\cdot|$ be some smooth hermitian metric on $\mathcal{O}_{X}(D)$. For any $\varepsilon>0$, there is a constant $C_{\varepsilon}$ such that
$$\varphi \geqslant-(n+v+\varepsilon) \log (-\log |s|)-C_{\varepsilon},$$
where $v$ is defined in (5.4).
Remark 5.10. - The estimate (5.5) is an important refinement of (5.3), as it insures that $\varphi$ belongs to the finite energy class $\mathcal{E}^{1}\left(X, \omega_{X}\right)$, cf [GZ07] or [BEGZ10, Sect. 2] for the definitions and main properties of these classes.

This estimate is almost optimal as the following two examples show.
Example 5.11. - Let $X={\overline{\mathrm{B}^{n} / \Gamma}}^{\text {BBS }}$ be the Baily-Borel-Satake compactification of a ball quotient, where $\Gamma \subset \operatorname{PU}(n, 1)$ is a discrete group acting freely with finite covolume. It is a normal stable variety and it admits a resolution $f: \bar{X} \rightarrow X$ which is a toroidal compactification of $\mathbb{B}^{n} / \Gamma$ obtained by adding disjoint abelian varieties $D_{i}$. That is, $v=$ $v(f)=1$. If one sets $D=\sum D_{i}$, the potential $\varphi$ of the Kähler-Einstein metric on ( $\bar{X}, D$ ) with respect to a smooth form in $c_{1}\left(K_{\bar{X}}+D\right)$ satisfies
$$\varphi=-(n+1) \log \left(-\log \left|s_{D}\right|\right)+O(1)$$
if $\left(s_{D}=0\right)=D$.
Example 5.12. - Let $X={\overline{\Delta^{2} / \Gamma}}^{\text {BBS }}$ be Baily-Borel-Satake compactification of a Hilbert modular surface, where $\Gamma \subset \operatorname{PSL}(2, \mathbb{R})$ is a discrete group whose diagonal action on the bi-disk $\Delta^{2}$ is free with finite covolume. It is a normal stable surface and the exceptional divisor $D$ of its minimal resolution $f: \bar{X} \rightarrow X$ consist of cycles of $\mathbb{P}^{1 \prime}$ s. In particular, we have $v=v(f)=2$. Moreover, it is known that the potential $\varphi$ of the Kähler-Einstein metric on $(\bar{X}, D)$ with respect to a smooth form in $c_{1}\left(K_{\bar{X}}+D\right)$ satisfies
$$\varphi=-4 \log \left(-\log \left|s_{D}\right|\right)+O(1)$$
if $\left(s_{D}=0\right)=D$, cf [Kob84, p. 57-58].

Proof. - Let $f: Y \rightarrow X$ be a resolution of singularities of $X$ such that $f$ induces an isomorphism over $X_{\text {reg }}$ and achieves $v=v(f)$. The complex Monge-Ampère equation satisfied by $\varphi$ pulls back to $Y$ and reads
$$\left(f^{*} \omega_{X}+d d^{c} f^{*} \varphi\right)^{n}=e^{f^{*} \varphi} d \mu_{Y}$$
where $d \mu_{Y}:=\prod_{i=1}^{r}\left|t_{i}\right|^{2 a_{i}} \omega_{Y}^{n}$ is a positive measure with possibly infinite mass. Here, $\omega_{Y}$ is a Kähler form on $Y$, and $\left(t_{i}=0\right)$ are divisors sitting over $X_{\text {sing }}$ (they need not be exceptional though, as $X$ may have singularities in codimension one). Finally, one has $a_{i} \geqslant-1$ for all $i$, and any divisor $\left(t_{i}=0\right)$ such that $a_{i}=-1$ sits above the non-klt locus of $X$.

Now, let $F$ be an effective divisor on $X$ and let $\sigma_{X} \in H^{0}\left(X, \mathcal{O}_{X}(F)\right)$ be a section cutting out $F$. Let $h$ be a smooth hermitian metric on $\mathcal{O}_{X}(F)$; there exists a constant $C_{F}$ such that $\Theta_{h}(F) \leqslant C_{F} \omega_{X}$. One can scale $h$ such that $\left|\sigma_{X}\right|_{h}^{2}<e^{-2(n+2) C_{F}}$ on $X$. Finally, let $\sigma_{Y}:=f^{*} \sigma_{X}$ and and let $\psi:=-\log \left(-\log \left|\sigma_{Y}\right|^{2}\right)$. We have
$$d d^{c} \psi=\frac{\left\langle D \sigma_{Y}, D \sigma_{Y}\right\rangle}{\left|\sigma_{Y}\right|^{2}\left(-\log \left|\sigma_{Y}\right|^{2}\right)}-\frac{1}{\left(-\log \left|\sigma_{Y}\right|^{2}\right)} \cdot f^{*} \Theta_{h}(F) .$$
By our choice of scaling, the function $A \psi$ is $f^{*} \omega_{X}$-psh for any $0 \leqslant A \leqslant 2(n+2)$. Moreover, it belongs to the class $\mathcal{E}\left(Y, f^{*} \omega_{X}\right)$ thanks to e.g. [Gue14, Prop. 2.3] and [DDNL18, Thm. 1.1(ii)].

We apply this construction to $F$ some (very ample, say) divisor containing the nonklt locus of $X$. This yields a section $\sigma_{Y}$ of $f^{*} F$ that vanishes at order at least one along the $\left(t_{i}=0\right)$ for which $a_{i}=-1$. As a result, the measure
$$e^{(n+v+2 \varepsilon) \psi} d \mu_{Y} \lesssim \frac{1}{\prod_{a_{i}=-1}\left|t_{i}\right|^{2}\left(-\log \prod_{a_{i}=-1}\left|t_{i}\right|^{2}\right)^{n+v+2 \varepsilon}} \prod_{a_{i}>-1}\left|t_{i}\right|^{2 a_{i}} \cdot \omega_{Y}^{n}$$
has a density $g_{\varepsilon}$ with respect to $\omega_{Y}^{n}$ that satisfies
$$\int_{Y} g_{\varepsilon}\left|\log g_{\varepsilon}\right|^{n+\varepsilon} \omega_{Y}^{n}<+\infty$$
for any $\varepsilon>0$ as we observed in the proof of Claim 4.5, cf (4.12) and the discussion below. By Theorem 1.5, this implies that the unique solution $u_{\varepsilon} \in \mathcal{E}\left(Y, \frac{1}{2} f^{*} \omega_{X}\right)$ of the Monge-Ampère equation
$$\left(\frac{1}{2} f^{*} \omega_{X}+d d^{c} u_{\varepsilon}\right)^{n}=e^{u_{\varepsilon}+(n+v+2 \varepsilon) \psi} d \mu_{Y}$$
is bounded, i.e. there exists a constant $C_{\varepsilon}>0$ such that
$$\left\|u_{\varepsilon}\right\|_{L^{\infty}(Y)} \leqslant C_{\varepsilon} .$$
Now, the function $v_{\varepsilon}:=u_{\varepsilon}+(n+v+2 \varepsilon) \psi \in \mathcal{E}\left(Y, f^{*} \omega_{X}\right)$ satisfies the inequality
$$\begin{aligned}
\left(f^{*} \omega_{X}+d d^{c} v_{\varepsilon}\right)^{n} & \geqslant\left(\frac{1}{2} f^{*} \omega_{X}+d d^{c} u_{\varepsilon}\right)^{n} \\
& =e^{v_{\varepsilon}} d \mu_{Y},
\end{aligned}$$
i.e. $v_{\varepsilon}$ is a subsolution of (5.6). By the comparison principle, we obtain that $f^{*} \varphi \geqslant v_{\varepsilon}$ and it follows from (5.7) that
$$f^{*} \varphi \geqslant(n+v+2 \varepsilon) \psi-C_{\varepsilon},$$
from which the conclusion follows. \(\square\)
5.3. Stable families. - Now one can establish a family version of the previous estimate, i.e. Proposition 5.9. In Setting 4.1, let us assume additionally that $K_{\mathcal{X} / \mathbb{D}}$ is ample. We let $h$ be a smooth hermitian metric on $K_{\mathcal{X} / \mathbb{D}}$ whose curvature is a Kähler form $\omega_{\mathcal{X}}:=\Theta_{h}\left(K_{\mathcal{X} / \mathbb{D}}\right)$; we set $\omega_{X_{t}}:=\left.\omega_{\mathcal{X}}\right|_{X_{t}}$. If $\Omega$ is a local trivialization of $m K_{\mathcal{X} / \mathbb{D}}$, then the quantity
$$\mu_{\mathcal{X} / \mathbb{D}, h}:=\frac{i^{n^{2}}(\Omega \wedge \bar{\Omega})^{1 / m}}{|\Omega|_{h}^{2 / m}}$$
is independent of $\Omega$ or $m$ (yet it depends on $h$ ) and for any $t \in \mathbb{D}$, it restricts to $X_{t}^{\text {reg }}$ as a positive measure
$$\mu_{X_{t}, h}:=\left.\mu_{\mathcal{X} / \mathbb{D}}\right|_{X_{t}^{\mathrm{reg}}}$$
which we extend by zero across $X_{t}^{\text {sing }}$. For each $t \in \mathbb{D}$, there exists a unique Kähler-Einstein metric $\omega_{\mathrm{KE}, t} \in c_{1}\left(K_{X_{t}}\right)$ which solves the Monge-Ampère equation
$$\left(\omega_{X_{t}}+d d^{c} \varphi_{t}\right)^{n}=e^{\varphi_{t}} \mu_{X_{t}, h}$$
on $X_{t}$. This is due to [Aub78, Yau78] when $X_{t}$ is smooth and to [BG14] in general.
Theorem 5.13. — In Setting 4.1, assume that
\begin{itemize}
\item[-] The relative canonical bundle $K_{\mathcal{X} / \mathbb{D}}$ is ample.
\item[-] The central fiber $X_{0}$ is irreducible.
\end{itemize}
Let $\omega_{X_{t}}+d d^{c} \varphi_{t}$ be the Kähler-Einstein metric of $X_{t}$, solution of (5.8) and let $D=(s=0) \subset \mathcal{X}$ be a divisor which contains $\operatorname{Nklt}\left(\mathcal{X}, X_{0}\right)$, cf (4.4). Fix | | | a some smooth hermitian metric on $\mathcal{O}_{\mathcal{X}}(D)$. Up to shrinking D , then for any $\varepsilon>0$, there exists $C_{\varepsilon}>0$ such that the inequality
$$\varphi_{t} \geqslant-(n+v+\varepsilon) \log (-\log |s|)-C_{\varepsilon}$$
holds on $X_{t}$ for any $t \in \mathbb{D}$, where $v$ is defined in (4.5).
This estimate improves an interesting control obtained previously by J.Song (see [Son17, Lem. 4.2]).

Proof. - Let $f: \mathcal{X}^{\prime} \rightarrow \mathcal{X}$ be a semi-stable model as in (4.2), achieving $v(f)=v$. The first observation is that the behavior of $f^{*}\left(\Omega_{t} \wedge \bar{\Omega}_{t}\right)^{1 / m}$ and $f^{*} \mu_{X_{t}, h}$ on $X_{t}$ is the same, uniformly in $t$, because there exists a constant $C>0$ such that for any trivializing open set, one has $C \geqslant|\Omega|_{h}^{2} \geqslant C^{-1}$, where $\Omega$ ranges among the finitely many trivializations of $m K_{\mathcal{X} / \mathbb{D}}$. This follows from the fact $h$ is a smooth hermitian metric on $m K_{\mathcal{X} / \mathbb{D}}$.

We set $\psi:=f^{*}\left(-\log \left(-\log |s|^{2}\right)\right)$; it is a quasi-psh function on $\mathcal{X}^{\prime}$ satisfying
$$\psi \leqslant \psi_{F}+O(1)$$
where $\psi_{F}$ is defined in (4.10).
By scaling the metric $|\cdot|$ on $\mathcal{O}_{\mathcal{X}}(D)$, one can assume that $A \psi$ is $f^{*} \omega_{X}$-psh for any $0 \leqslant A \leqslant 2(n+2)$. For any $t \in \mathbb{D}^{*}$, the function $\psi_{t}:=\left.\psi\right|_{X_{t}^{\prime}}$ belongs to $\mathcal{E}\left(X_{t}^{\prime}, f^{*} \omega_{X_{t}}\right)$ by the same argument as in the proof of Proposition 5.9.

Let $u_{\varepsilon, t} \in \mathcal{E}\left(X_{t}^{\prime}, \frac{1}{2} f^{*} \omega_{X_{t}}\right)$ be the unique solution of the Monge-Ampère equation
$$\left(\frac{1}{2} f^{*} \omega_{X_{t}}+d d^{c} u_{\varepsilon, t}\right)^{n}=e^{u_{\varepsilon, t}+(n+v+2 \varepsilon) \psi_{t}} f^{*} \mu_{X_{t}, h} .$$

One can write $e^{(n+v+2 \varepsilon) \psi_{t}} f^{*} \mu_{X_{t}, h}=e^{\rho_{t}} f^{*} \omega_{X_{t}}^{n}$ where $\rho_{t}$ is the restriction to $X_{t}^{\prime}$ of the difference of quasi-psh functions on $\mathcal{X}^{\prime}$ with uniformly bounded $L^{1}$ norm on $X_{t}^{\prime}$. Set $V:=\int_{X_{t}} \omega_{X_{t}}^{n}$. Integrating both sides of (5.10) and using Jensen inequality we have
$$\begin{aligned}
\frac{V}{2^{n}} & =\int_{X_{t}^{\prime}} e^{u_{\varepsilon, t}+(n+v+2 \varepsilon) \psi_{t}} f^{*} \mu_{X_{t}, h} \\
& =V \int_{X_{t}^{\prime}} e^{u_{\varepsilon, t}+\rho_{t}} \frac{f^{*} \omega_{X_{t}}^{n}}{V} \\
& \geqslant V \cdot e^{\frac{1}{V} \int_{X_{t}^{\prime}}\left(u_{\varepsilon, t}+\rho_{t}\right) f^{*} \omega_{X_{t}}^{n}}
\end{aligned}$$
Since $\int_{X_{t}^{\prime}}\left|\rho_{t}\right| f^{*} \omega_{X_{t}}^{n}$ is uniformly bounded, we get that $\int_{X_{t}^{\prime}} u_{\varepsilon, t} f^{*} \omega_{X_{t}}^{n} \leqslant C$ for some $C>0$ independent of $\varepsilon$, $t$. Since $u_{\varepsilon, t}$ is $f^{*}\left(\frac{1}{2} \omega_{X_{t}}\right)$-psh, it is the pull-back of a $\frac{1}{2} \omega_{X_{t}}$-psh function on $X_{t}$ to which one can apply Proposition 3.3 since $\pi$ is projective. To summarize, we get an upper bound
$$u_{\varepsilon, t} \leqslant C .$$

Next, we wish to apply Theorem 1.5; in order to do so, one has to check that hypotheses (H1) and (H2') are satisfied in our situation. For (H1), it is a consequence of Theorem 3.4 - recall that up to shrinking $\mathbb{D}$, all fibers $X_{t}$ are irreducible since so is $X_{0}$. As for (H2'), it follows from Lemma 4.6 that we pull back via $f$ to the smooth Kähler manifold $X_{t}^{\prime}$. All in all, we can find $C_{\varepsilon}>0$ independent of $t \in \mathbb{D}$ such that
$$\left\|u_{\varepsilon, t}\right\|_{L^{\infty}\left(X_{t}^{\prime}\right)} \leqslant C_{\varepsilon} .$$
Now, the function $v_{\varepsilon, t}:=u_{\varepsilon, t}+(n+v+2 \varepsilon) \psi_{t} \in \mathcal{E}\left(X_{t}^{\prime}, f^{*} \omega_{X_{t}}\right)$ satisfies the inequality
$$\begin{aligned}
\left(f^{*} \omega_{X_{t}}+d d^{c} v_{\varepsilon, t}\right)^{n} & \geqslant\left(\frac{1}{2} f^{*} \omega_{X_{t}}+d d^{c} u_{\varepsilon, t}\right)^{n} \\
& =e^{v_{\varepsilon, t}} f^{*} \mu_{X_{t}, h},
\end{aligned}$$
i.e. $v_{\varepsilon, t}$ is a subsolution of (5.8). By the comparison principle, we obtain that $f^{*} \varphi_{t} \geqslant v_{\varepsilon, t}$ and it follows from (5.12) that
$$f^{*} \varphi_{t} \geqslant(n+v+2 \varepsilon) \psi_{t}-C_{\varepsilon},$$
from which the conclusion follows. \(\square\)

\section*{6. Log Calabi-Yau families}
6.1. Families of Calabi-Yau varieties. - In Setting 4.1, let us assume additionally that $K_{\mathcal{X} / \mathbb{D}}$ is relatively trivial and that $X_{0}$ has canonical singularities. For $t$ small enough, $X_{t}$ has canonical singularities as well and $K_{X_{t}}$ is linearly trivial.

Let $\alpha$ be a relative Kähler cohomology class on $\mathcal{X}$ represented by a relative Kähler form $\omega$. We set $\alpha_{t}:=\left.\alpha\right|_{X_{t}}, \omega_{X_{t}}:=\left.\omega\right|_{X_{t}}$ and $V:=\int_{X_{t}} \omega_{t}^{n}$; it does not depend on $t$, cf Lemma 2.2. Let $\Omega$ be a trivialization of $K_{\mathcal{X} / \mathbb{D}}$, so that the quantity
$$\mu_{\mathcal{X} / \mathbb{D}}:=i^{n^{2}} \Omega \wedge \bar{\Omega}$$
restricts to $X_{t}^{\text {reg }}$ as a positive measure
$$\mu_{X_{t}}:=\left.\mu_{\mathcal{X} / \mathbb{D}}\right|_{X_{t}^{\text {reg }}}$$
which we extend by zero across $X_{t}^{\text {sing }}$. We set $c_{t}:=\log \int_{X_{t}} d \mu_{X_{t}}$. For each $t \in \mathbb{D}$, there exists a unique Kähler-Einstein metric $\omega_{\mathrm{KE}, t}=\omega_{t}+d d^{c} \varphi_{t} \in \alpha_{t}$ which solves the Monge-Ampère equation
$$\frac{1}{V}\left(\omega_{t}+d d^{c} \varphi_{t}\right)^{n}=e^{-c_{t}} \mu_{X_{t}}$$
on $X_{t}$ and that we normalize by $\sup _{X_{t}} \varphi_{t}=0$. This is due to [Yau78] when $X_{t}$ is smooth and to [EGZ09] in general.

Theorem 6.1. - In Setting 4.1, assume that
\begin{itemize}
\item[-] The relative canonical bundle $K_{\mathcal{X} / \mathbb{D}}$ is trivial.
\item[-] The central fiber $X_{0}$ has canonical singularities.
\item[-] Assumption 3.2 is satisfied.
\end{itemize}
Let $\omega_{t}+d d^{c} \varphi_{t}$ be the Kähler-Einstein metric of $X_{t}$, solution of (6.1). Up to shrinking $\mathbb{D}$, there exists $C>0$ such that one has
$$\operatorname{osc}_{X_{t}} \varphi_{t} \leqslant C$$
for any $t \in \mathbb{D}$, where $\operatorname{osc}_{X_{t}}\left(\varphi_{t}\right)=\sup _{X_{t}} \varphi_{t}-\inf _{X_{t}} \varphi_{t}$.
A particular case of this result has been obtained previously by Rong-Zhang (see [RZ11a, Lemma 3.1]) by using Moser iteration process.

Remark 6.2. - One can replace the first two assumptions in Theorem 6.1 above by the following weaker ones: $\mathcal{X}$ is normal, Q-Gorenstein, $K_{\mathcal{X} / \mathbb{D}}$ is trivial and $X_{0}$ has canonical singularities. Indeed, it follows from the inversion of adjunction [Kol18, Thm. 2.3] that $\left(X, X_{t}\right)$ is lc for $t$ close enough to 0. Moreover, an easy computation relying on the adjunction formula shows that $X_{t}$ has canonical singularities for $t$ close to 0.

Proof of Theorem 6.1. - A first observation is that the quantities $c_{t}$ remain bounded when $t$ varies thanks to Lemma 4.2. The result now follows from Theorem 1.1. Indeed, (H1) is satisfied thanks to Theorem 3.4 while (H2) holds thanks to Lemma 4.4 that we pull back to $X_{t}^{\prime}$ via $f$, with the notation of the Lemma. \(\square\)
6.2. The log Calabi-Yau setting. - In the sequel we use the following setting.

Setting 6.3. - Let $X$ be an $n$-dimensional compact Kähler space and let $B=\sum b_{i} B_{i}$ be an effective $\mathbb{R}$-divisor such that the pair $(X, B)$ has klt singularities. We assume furthermore that the log Kodaira dimension of the pair $(X, B)$ vanishes, i.e.
$$\kappa\left(K_{X}+B\right)=0 .$$

In what follows, we denote by $E$ the (unique) effective $\mathbb{R}$-divisor in $c_{1}\left(K_{X}+B\right)$. Thanks to log abundance in numerical dimension zero (see [CGP23, Cor. 1.18]), a particular instance of such pairs is provided by klt pairs $(X, B)$ with rational boundary such that the Chern class $c_{1}\left(K_{X}+B\right) \in H^{2}(X, \mathbb{Q})$ vanishes.

Definition 6.4. - In Setting 6.3, given a cohomology class $\alpha \in H^{1,1}(X, \mathbb{R})$ that is nef and big, it follows from [BEGZ10] that there exists a unique singular Ricci flat current $T \in \alpha$, i.e. a closed, positive current of bidegree $(1,1)$ representing $\alpha$, with the following properties:
\begin{itemize}
\item[(i)] $T$ has minimal singularities in $\alpha$;
\item[(ii)] $T$ is a Kähler form on the analytic open set $\Omega_{\alpha}:=\left(X_{\text {reg }} \backslash \operatorname{Supp}(B+E)\right) \cap \operatorname{Amp}(\alpha)$;
\item[(iii)] $\operatorname{Ric}(T)=[B]-[E]$ on $X_{\text {reg }}$.
\end{itemize}

The current $T$ can be found by solving the Monge-Ampère equation
$$\operatorname{vol}(\alpha)^{-1}\left(\theta+d d^{c} \varphi\right)^{n}=\mu_{(X, B)}$$
where $\theta \in \alpha$ is a smooth representative, $\varphi \in \operatorname{PSH}(X, \theta)$ is the unknown function and
$$\mu_{(X, B)}=(s \wedge \bar{s})^{\frac{1}{m}} e^{-\phi_{B}} .$$
Here, $s \in H^{0}\left(X, m\left(K_{X}+B\right)\right)$ is any non-zero section (for some $m \geqslant 1$ ) and $\phi_{B}$ is the unique singular psh weight on $\mathcal{O}_{X}(B)$ solving $d d^{c} \phi_{B}=[B]$ and normalized by
$$\int_{X}(s \wedge \bar{s})^{\frac{1}{m}} e^{-\phi_{B}}=1 .$$

We let $\mathcal{K}_{X}$ denote the Kähler cone, i.e. the set of cohomology classes $\alpha \in H^{1,1}(X, \mathbb{R})$ which can be represented by a Kähler form. We fix $\left(\alpha_{t}\right)_{0<t \leqslant 1} \subset \mathcal{K}_{X}$ a path of Kähler classes and assume that $\alpha_{t} \rightarrow \partial \mathcal{K}_{X}$ as $t \rightarrow 0$.

When $X$ is smooth and $B=0$, the existence of a unique Ricci flat Kähler metric $\omega_{t}$ in $\alpha_{t}$ for each $0<t \leqslant 1$ dates back to the celebrated work of Yau [Yau78]. A basic problem is to understand the asymptotic behavior of the $\omega_{t}{ }^{\prime}$ s as $t \rightarrow 0$. This problem has a long history, we refer the reader to [GTZ13] for references.

Despite motivations coming from mirror symmetry, not much is known when the norm of $\alpha_{t}$ converges to $+\infty$ (this case is expected to be the mirror of a large complex structure limit, see [KS01] or the recent survey [Tos20]). We thus only consider the case when $\alpha_{t} \rightarrow \alpha_{0} \in \partial \mathcal{K}_{X}$. There are two rather different settings, depending on whether $\alpha_{0}$ is big $\left(\operatorname{vol}\left(\alpha_{0}\right)>0\right)$, or merely nef with $\operatorname{vol}\left(\alpha_{0}\right)=0$.
6.3. The non-collapsing case. - We first consider the case when the volumes of the $\alpha_{t}$ 's are non-collapsing, i.e. $\operatorname{vol}\left(\alpha_{0}\right)>0$. Then, we have the following result, generalizing theorems of Tosatti [Tos09] and Collins-Tosatti [CT15].

Theorem 6.5. - Let $(X, B)$ be a pair as in Setting 6.3 and let $\left(\alpha_{t}\right)_{0<t \leqslant 1} \subset \mathcal{K}_{X}$ be a smooth path of Kähler classes such that $\alpha_{t} \rightarrow \alpha_{0} \in \partial \mathcal{K}_{X}$ as $t \rightarrow 0$, with $\operatorname{vol}\left(\alpha_{0}\right)>0$.
Then, the singular Ricci-flat currents $T_{t} \in \alpha_{t}$ converge to $T_{0}$ as $t \rightarrow 0$ weakly on $X$, and locally smoothly on $\Omega_{\alpha}$.

Proof. - One can work in a desingularization $p: Y \rightarrow X$ of $X$. The path $\alpha_{t}$ induces a path $\beta_{t}=p^{*} \alpha_{t}$ of semi-positive and big classes. The currents $T_{t}$ can be decomposed as $T_{t}=\theta_{t}+d d^{c} \varphi_{t}$ where $\theta_{t} \in \beta_{t}$ is a smooth representative and $\varphi_{t}$ are normalized by $\sup _{X_{t}} \varphi_{t}=0$ and solve the complex Monge-Ampère equation
$$\frac{1}{V_{t}}\left(\theta_{t}+d d^{c} \varphi_{t}\right)^{n}=\mu_{Y}=f d V_{Y},$$
where the volumes $V_{t}=\alpha_{t}^{n}$ are bounded away from zero and infinity, $C^{-1} \leqslant V_{t} \leqslant C$, and $\mu_{Y}=f d V_{Y}$ is a fixed volume form, with $f \in L^{p}(Y)$ for some $p>1$ (because $(X, B)$ has klt singularities, see [EGZ09, Lem. 6.4]).

The hypothesis of Theorem 1.1 (H2) is thus trivially satisfied, while (H1) follows if we initially bound from above $\alpha_{t} \leqslant \gamma_{X}$ by a fixed Kähler class. The most delicate $\mathcal{C}^{0}$-estimate follows thus here from Theorem 1.9. When $X$ is smooth, the $\mathcal{C}^{0}$-estimate in [Tos09] is obtained by using a Moser iteration argument as in Yau's celebrated paper [Yau78], but this argument can no longer be applied in the present more singular setting.
The rest of the proof is then roughly the same as in the case of smooth manifolds. It consists in adapting Yau's Laplacian estimate by using Tsuji's trick (first used in [Tsu88]), the remaining higher order estimates being local ones. \(\square\)
6.4. The collapsing case. - We now consider the case when the volumes of the $\alpha_{t}$ 's are collapsing, i.e. $\operatorname{vol}\left(\alpha_{0}\right)=0$. This case is more involved and only special cases are fully understood.

Suppose there is a surjective, holomorphic map with connected fibers $f: X \rightarrow Z$, where $Z$ is a compact, normal Kähler space of positive dimension $m$. We denote by $k:=n-m=\operatorname{dim} X-\operatorname{dim} Z$ the relative dimension of the fiber space $f$. We let $S_{Z}$ denote the smallest proper analytic subset $\Sigma \subset Z$ such that
\begin{itemize}
\item[-] $\Sigma$ contains the singular locus $Z_{\text {sing }}$ of $Z$,
\item[-] The map $f$ is smooth on $f^{-1}(Z \backslash \Sigma)$,
\item[-] For any $z \in Z \backslash \Sigma, \operatorname{Supp}(B)$ intersects $X_{z}$ transversally,
\end{itemize}
and we set $S_{X}=f^{-1}\left(S_{Z}\right)$. Finally, we set $Z^{\circ}:=Z \backslash S_{Z}$ and $X^{\circ}:=X \backslash S_{X}=f^{-1}\left(Z^{\circ}\right)$. By the last item, each component of $\left.B\right|_{X^{\circ}}$ dominates $Z^{\circ}$.

A general fiber $X_{z}$ satisfies $\kappa\left(K_{X_{z}}+B_{z}\right) \geqslant 0$, but the inequality may be strict. If $c_{1}\left(K_{X}+B\right)=0$, then log abundance implies that $K_{X_{z}}+B_{z} \sim_{\mathrm{Q}} \mathcal{O}_{X_{z}}$ for $z$ general. Moreover, Iitaka's conjecture predicts that $\kappa\left(K_{X_{z}}+B_{z}\right)$ vanishes as soon as $\kappa(Z) \geqslant 0$, which in turn should be equivalent to $Z$ not being uniruled.

Fix $\omega_{Z}$ a Kähler form on $Z$. For simplicity, we assume that $\int_{Z} \omega_{Z}^{m}=1$. The form $f^{*} \omega_{Z}$ is a semi-positive form such that $f^{*} \omega_{Z}^{p}=0$ for any $p>m$. We also choose a Kähler form $\omega_{X}$ on $X$. The quantity $\int_{X_{z}} \omega_{X}^{k}=f_{*} \omega_{X}^{k}$ is constant in $z \in Z$; up to renormalizing $\omega_{X}$, we may assume that the constant is 1.

We assume that our path $\left(\alpha_{t}\right)_{t \geqslant 0}$ in $H^{1,1}(X, \mathbb{R})$ is given by $\alpha_{0}=\left\{f^{*} \omega_{Z}\right\}$ and $\alpha_{t}=$ $\alpha_{0}+t\left\{\omega_{X}\right\}$. As a result, one has
$$V_{t}:=\operatorname{vol}\left(\alpha_{t}\right)=\binom{n}{k} t^{k} \int_{X} f^{*} \omega_{Z}^{m} \wedge \omega_{X}^{k}+o\left(t^{k}\right)=\binom{n}{k} t^{k}+o\left(t^{k}\right) .$$
We set $\omega_{t}:=f^{*} \omega_{Z}+t \omega_{X}$ and let $\omega_{\varphi_{t}}:=\omega_{t}+d d^{c} \varphi_{t}$ denote the singular Ricci-flat current in $\alpha_{t}$, normalized by $\int_{X} \varphi_{t} \omega_{X}^{n}=0$. It satisfies
$$\omega_{\varphi_{t}}^{n}=V_{t} \cdot \mu_{(X, B)},$$
cf Eq. (6.3). The probability measure $f_{*} \mu_{(X, B)}$ has $L^{1+\varepsilon}$-density with respect to $\omega_{Z}^{m}$ thanks to [EGZ18, Lem. 2.3]. Therefore, there exists a unique positive current $\omega_{\infty} \in\left\{\omega_{Z}\right\}$ with
bounded potentials, solution of the Monge-Ampère equation
$$\omega_{\infty}^{m}=f_{*} \mu_{(X, B)},$$
cf [EGZ09]. In the case where $X$ is smooth, $B=0$ and $c_{1}(X)=0$, the Ricci curvature of $f_{*} \mu_{X}$ (or, equivalently, $\omega_{\infty}$ ) coincides with the Weil-Petersson form of the fibration $f$ of Calabi-Yau manifolds. We propose the following problem.

Problem 1. - Let $f: X \rightarrow Z$ be a surjective holomorphic map with connected fibers between compact, normal Kähler spaces. Assume that there exists an effective divisor $B$ on $X$ such that $(X, B)$ is klt and $\kappa\left(K_{X}+B\right)=0$. Let $\omega_{X}$ (resp. $\omega_{Z}$ ) be a Kähler form on $X$ (resp. $Z$ ) and let $\omega_{\varphi_{t}}$ be the unique singular Ricci-flat current in $\left\{f^{*} \omega_{Z}+t \omega_{X}\right\}$ for $t>0$.
Then, the currents $\omega_{\varphi_{t}}$ converge weakly to $f^{*} \omega_{\infty}$ when $t \rightarrow 0$, where $\omega_{\infty} \in\left\{\omega_{Z}\right\}$ solves $\omega_{\infty}^{\operatorname{dim} Z}=f_{*} \mu_{(X, B)}$.

The Problem above is motivated by a string of papers (cf below) where the expected result is proved along with some additional information on the convergence.

Theorem 6.6. - [Tos10, GTZ13, TWY18, HT20] Assume that $X$ is smooth, $B=0$ and $c_{1}\left(K_{X}\right)=0$. Then, the metrics $\omega_{\varphi_{t}}$ converge to $f^{*} \omega_{\infty}$ in the $\mathcal{C}_{\text {loc }}^{\alpha}$-sense on $X \backslash S_{X}$, for some $\alpha>0$.

In this section, we aim at providing a positive answer to Problem 1 whenever $X$ is smooth, $B$ has simple normal crossings support and $c_{1}\left(K_{X}+B\right)=0$. We will follow the strategy of Tosatti [Tos10] rather closely. However, some adjustments need to be made, requiring the use of conical metrics and the results of the present paper.

Theorem 6.7. - In the Setting of Problem 1, assume furthermore that $X$ is smooth, $B$ has snc support and $c_{1}\left(K_{X}+B\right)=0$. Then, $\omega_{\varphi_{t}} \rightarrow f^{*} \omega_{\infty}$ as currents on $X$, when $t$ goes to 0 .

Proof. - We will proceed in several steps, similarly to [Tos10]. In order to simplify some computations to follow, one will assume that $S_{Z}$ is contained in a divisor $D_{Z}$, cut out by a section $\sigma_{Z} \in H^{0}\left(Z, \mathcal{O}_{Z}\left(D_{Z}\right)\right)$. If $Z$ is projective, this is not a restriction. The general case requires to follow Tosatti's computations more closely but does not present significant additional difficulties.

Step 1. Choice of some suitable conical metrics
We list in the Proposition below the properties of the conical metric that will be important for the following. It is mostly a recollection of well-known results, cf e.g. [GP16]. By abuse of notation, we will not distinguish between $B$ and $\operatorname{Supp}(B)$.

Proposition 6.8. - There exists a Kähler current $\omega_{B} \in\left\{\omega_{X}\right\}$ on $X$ such that
\begin{itemize}
\item[1.] $\omega_{B}$ is a smooth Kähler form on $X \backslash B$ and has conical singularities along $B$.
\item[2.] There exists a constant $C>0$ and a quasi-psh function $\Psi \in \mathcal{C}^{\infty}(X \backslash B) \cap L^{\infty}(X)$ such that the following inequalities of tensors hold in the sense of Griffiths on $X \backslash B$
$$-\left(C \omega_{B}+d d^{c} \Psi\right) \otimes \operatorname{Id}_{T_{X}} \leqslant \Theta_{\omega_{B}}\left(T_{X}\right) \leqslant C \omega_{B} \otimes \operatorname{Id}_{T_{X}} .$$
\item[3.] Let $h:=\omega_{B}^{n} / \omega_{X}^{n}$. There exists $p>1$ such that for any $K \Subset Z^{\circ}$, one has
$$\sup _{z \in K}\left\|\left.h\right|_{X_{z}}\right\|_{L^{p}\left(\omega_{X_{z}}^{k}\right)}<+\infty .$$
\end{itemize}

Sketch of proof of Proposition 6.8. - To construct such a metric $\omega_{B}$, one first chooses smooth metrics $h_{i}$ on $B_{i}$, sections $s_{i} \in H^{0}\left(X, \mathcal{O}_{X}\left(B_{i}\right)\right)$ cutting out $B_{i}$, and one sets $\omega_{B}:=\omega_{X}+d d^{c} \sum_{i}\left|s_{i}\right|^{2\left(1-b_{i}\right)}$. Up to scaling down the metrics $h_{i}$, one can easily achieve the first condition. The third condition also follows easily.

The left-hand side inequality of 2 ("lower bound" on the holomorphic bisectional curvature) follows from [GP16, (4.3)] with $\varepsilon=0$. As for the right-hand side inequality (upper bound on the holomorphic bisectional curvature), a proof has been given in [JMR16, App. A] in the case where $B$ is smooth but a very simple argument has been found by Sturm, cf [Rub14, Lem. 3.14]. \(\square\)

Step 2. Estimates
We list in the Proposition below various estimates on $\omega_{\varphi_{t}}$ that will be useful for the last step. First, we define for $z \in Z^{\circ}$ the quantity $\underline{\varphi_{t}}(z):=\int_{X_{z}} \varphi_{t} \omega_{X_{z}}^{k}$. In the following, we will not distinguish between $\underline{\varphi_{t}}$ and $f^{*} \underline{\varphi_{t}}$.

Proposition 6.9. - There exist a constant $C>0$ as well as a positive function $g \in \mathcal{C}^{\infty}\left(X^{\circ}\right)$, both independent of $t$, such that
\begin{itemize}
\item[1.] $\left\|\varphi_{t}\right\|_{L^{\infty}(X)} \leqslant C$.
\item[2.] $\omega_{\varphi_{t}} \geqslant C^{-1} f^{*} \omega_{Z}$.
\item[3.] $\left|\varphi_{t}-\varphi_{t}\right| \leqslant g \cdot t$.
\item[4.] $g^{-1} t \cdot \omega_{B} \leqslant \omega_{\varphi_{t}} \leqslant g \cdot \omega_{B}$.
\item[5.] $g^{-1} t \cdot \omega_{B_{z}} \leqslant\left.\omega_{\varphi_{t}}\right|_{X_{z}} \leqslant g t \cdot \omega_{B_{z}} \quad$ for all $z \in Z^{\circ}$.
\end{itemize}
Proof of Proposition 6.9. - In this proof, $C$ will denote a constant that may change from line to line but is independent of $t$. In the same way, $g$ will be a smooth, positive function on $X^{\circ}$ that should be thought as blowing up to $+\infty$ near $S_{X}$; it can be assumed to come from $Z^{\circ}$ via $f$.
\begin{itemize}
\item[1.] This is a consequence of [EGZ08, Thm. A] or [DP10, p. 401].
\item[2.] Let us consider the holomorphic map $f:\left(X \backslash B, \omega_{\varphi_{t}}\right) \rightarrow\left(Z, \omega_{Z}\right)$. Given that $\operatorname{Ric}\left(\omega_{\varphi_{t}}\right)=0$ and that $\omega_{Z}$ is a smooth Kähler metric on the compact space $Z$, Chern-Lu's formula [Che68, Lu68] provides a constant $C>0$ such that the non-negative function $u=\operatorname{tr}_{\omega_{\varphi_{t}}} f^{*} \omega_{Z}$ satisfies
$$\Delta_{\omega_{\varphi_{t}}} \log u \geqslant-C(1+u)$$
on $X \backslash B$. Now,
$$\Delta_{\omega_{\varphi_{t}}}\left(-\varphi_{t}\right)=\operatorname{tr}_{\omega_{\varphi_{t}}}\left(-\omega_{\varphi_{t}}+f^{*} \omega_{Z}+t \omega_{X}\right) \geqslant u-n$$
so that setting $A=C+1$, one finds
$$\Delta_{\omega_{\varphi_{t}}}\left(\log u-A \varphi_{t}\right) \geqslant u-C .$$
\end{itemize}
Let $\tau$ be a section of $\mathcal{O}_{X}(\lceil B\rceil)$ cutting out $B$ and let $h_{B}$ be a smooth hermitian metric on that line bundle. We set $\chi:=\log |\tau|_{h_{B}}^{2}$. As $\omega_{\varphi_{t}}$ is a Kähler current and $\chi$ is quasi-psh,
there exists a constant $C_{t}>0$ such that $d d^{c} \chi \geqslant-C_{t} \omega_{\varphi_{t}}$. Therefore, for any $\delta \in\left(0, C_{t}^{-1}\right)$, one has an inequality
$$\Delta_{\omega_{\varphi_{t}}}\left(\log u-A \varphi_{t}+\delta \chi\right) \geqslant u-C .$$
As $\omega_{\varphi_{t}}$ is a conical metric for $t>0$, the function $u$ is bounded above on $X \backslash B$ and therefore, $H_{t, \delta}:=\log u-A \varphi_{t}+\delta \chi$ attains its maximum at a point $x_{t, \delta} \in X \backslash B$ such that $u\left(x_{t, \delta}\right) \leqslant C$. As a result, the estimate obtained in 1. allows one to show that for any $x \in X \backslash B$, one has
$$\begin{aligned}
\log u(x) & =H_{t, \delta}(x)+A \varphi_{t}(x)-\delta \chi(x) \\
& \leqslant H_{t, \delta}\left(x_{t, \delta}\right)+C-\delta \chi(x) \\
& \leqslant C-\delta \chi .
\end{aligned}$$
As this holds for any $\delta>0$ small enough, we can pass to the limit and conclude that $u \leqslant e^{C}$ on $X \backslash B$, hence everywhere.
3. The equation solved by $\varphi_{t}$ can be rewritten as
$$\left(f^{*} \omega_{Z}+t \omega_{X}+d d^{c} \varphi_{t}\right)^{n}=t^{k} e^{F_{t}} \omega_{B}^{n}$$
where $F_{t}$ is uniformly bounded independently of $t$. Next, one has on $X_{z}\left(z \in Z^{\circ}\right)$
$$\frac{\left(\left.\omega_{\varphi_{t}}\right|_{X_{z}}\right)^{k}}{\omega_{X_{z}}^{k}}=\frac{\omega_{\varphi_{t}}^{k} \wedge f^{*} \omega_{Z}^{m}}{\omega_{X}^{k} \wedge f^{*} \omega_{Z}^{m}} \leqslant C g \cdot \frac{\omega_{\varphi_{t}}^{n}}{\omega_{X}^{n}}$$
thanks to 2. Observing that $\left.\omega_{\varphi_{t}}\right|_{X_{z}}=\left.\left(\omega_{\varphi_{t}}-d d^{c} \underline{\varphi_{t}}\right)\right|_{X_{z}}$, one sees from Eq. (6.5) that $\left.\left(\varphi_{t}-\underline{\varphi_{t}}\right)\right|_{X_{z}}$ satisfies
$$\left(\omega_{X_{z}}+d d^{c}\left(\left.\frac{1}{t}\left(\varphi_{t}-\underline{\varphi_{t}}\right)\right|_{X_{z}}\right)\right)^{k} \leqslant\left. g h\right|_{X_{z}} \cdot \omega_{X_{z}}^{k}$$
where $h=\omega_{B}^{n} / \omega_{X}^{n}$. Thanks to the third item of Proposition 6.8, Theorem 3.4 and Theorem 1.1, we can derive 3. Actually, we used a version of Theorem 3.4 for higher-dimensional bases, but only for smooth morphisms, in which case the proofs in the one-dimensional case go through without any change.
4.a We first prove the right-hand side inequality. Let us start by writing $\omega_{B}=\omega_{X}+$ $d d^{c} \psi_{B}$ where $\psi_{B} \in L^{\infty}(X) \cap \mathcal{C}^{\infty}(X \backslash B)$. From the second item of Proposition 6.8 and Siu's Laplacian inequality (cf [GP16, (2.2)]), one concludes that
$$\Delta_{\omega_{\varphi_{t}}}\left(\log \operatorname{tr}_{\omega_{B}} \omega_{\varphi_{t}}+\Psi\right) \geqslant-C\left(1+\operatorname{tr}_{\omega_{\varphi_{t}}} \omega_{B}\right) .$$
Next, one has
$$\Delta_{\omega_{\varphi_{t}}}\left(-\varphi_{t}+t \psi_{B}\right)=\operatorname{tr}_{\omega_{\varphi_{t}}}\left(-\omega_{\varphi_{t}}+f^{*} \omega_{Z}+t \omega_{B}\right) \geqslant t \operatorname{tr}_{\omega_{\varphi_{t}}} \omega_{B}-n$$
so that
$$\Delta_{\omega_{\varphi_{t}}}\left(\log \operatorname{tr}_{\omega_{B}} \omega_{\varphi_{t}}+\Psi-\frac{A}{t} \varphi_{t}+A \psi_{B}\right) \geqslant \operatorname{tr}_{\omega_{\varphi_{t}}} \omega_{B}-\frac{C}{t} .$$

We want to bound from below the term $d d^{c} \underline{\varphi_{t}}$. In order to achieve this, one writes
$$\begin{aligned}
d d^{c} \underline{\varphi}_{t} & =d d^{c} f_{*}\left(\varphi_{t} \omega_{X}^{k}\right)=f_{*}\left(d d^{c} \varphi_{t} \wedge \omega_{X}^{k}\right) \\
& \geqslant-f_{*}\left(f^{*} \omega_{Z} \wedge \omega_{X}^{k}+t \omega_{X}^{k+1}\right) \\
& \geqslant-\omega_{Z}-t f_{*} \omega_{X}^{k+1} \geqslant-g \cdot \omega_{Z}
\end{aligned}$$
given that $f_{*} \omega_{X}^{k}=1$. In particular, one has
$$\Delta_{\omega_{\varphi_{t}}} \underline{\varphi_{t}} \geqslant-g$$
thanks to 2. Combining that estimate with (6.8), one finds
$$\Delta_{\omega_{\varphi_{t}}}\left(\log \operatorname{tr}_{\omega_{B}} \omega_{\varphi_{t}}+\Psi-\frac{A}{t}\left(\varphi_{t}-\underline{\varphi_{t}}\right)+A \psi_{B}\right) \geqslant \operatorname{tr}_{\omega_{\varphi_{t}}} \omega_{B}-\frac{g}{t} .$$
We now set $F:=\Psi-\frac{A}{t}\left(\varphi_{t}-\underline{\varphi_{t}}\right)+A \psi_{B}$; it is a bounded function on $X$, smooth on $X^{\circ} \backslash B$ such that
$$|F| \leqslant g$$
thanks to 3. Next, we set $\rho:=\chi+f^{*} \log \left|\sigma_{Z}\right|_{h_{D_{Z}}}^{2}$ where $\chi$ is defined in the proof of 2 and $h_{D_{Z}}$ is a smooth hermitian metric on the divisor $D_{Z}$ (containing $S_{Z}$ ). As $\rho$ is quasi-psh on $X$, there exists $C_{t}>0$ such that
$$d d^{c} \rho \geqslant-C_{t} \omega_{\varphi_{t}} .$$
In particular, one has
$$\Delta_{\omega_{\varphi_{t}}}\left(\log \operatorname{tr}_{\omega_{B}} \omega_{\varphi_{t}}+F+\delta \rho\right) \geqslant \operatorname{tr}_{\omega_{\varphi_{t}}} \omega_{B}-\frac{g}{t} .$$
as soon as $\delta \in\left(0, C_{t}^{-1}\right)$. We choose such a $\delta$ for the following. As the quantity $\log \operatorname{tr}_{\omega_{B}} \omega_{\varphi_{t}}+F$ is globally bounded on $X$ and smooth on $X^{\circ} \backslash B$, the function $\log \operatorname{tr}_{\omega_{B}} \omega_{\varphi_{t}}+F+\delta \rho$ attains it maximum at a point $y_{t, \delta} \in X^{\circ} \backslash B$ such that
$$\operatorname{tr}_{\omega_{\varphi_{t}}} \omega_{B}\left(y_{t, \delta}\right) \leqslant \frac{g}{t}$$
thanks to the maximum principle. Combining this with 2, one finds
$$\operatorname{tr}_{\omega_{\varphi_{t}}}\left(f^{*} \omega_{Z}+t \omega_{B}\right)\left(y_{t, \delta}\right) \leqslant g$$
Using the standard inequality
$$\operatorname{tr}_{\omega^{\prime}} \omega \leqslant \frac{\omega^{n}}{\omega^{\prime n}}\left(\operatorname{tr}_{\omega} \omega^{\prime}\right)^{n-1}$$
valid for any two positive (1,1)-forms, one gets from (6.15)
$$\operatorname{tr}_{f^{*} \omega_{Z}+t \omega_{B}}\left(\omega_{\varphi_{t}}\right)\left(y_{t, \delta}\right) \leqslant g$$
since $\omega_{\varphi_{t}}^{n} \simeq t^{k} \omega_{B}^{n}$ is uniformly comparable to $\left(f^{*} \omega_{Z}+t \omega_{B}\right)^{n}$ by Claim 6.10 below. As $\omega_{B}$ dominates $f^{*} \omega_{Z}+t \omega_{B}$, we infer from the inequality above the following
$$\operatorname{tr}_{\omega_{B}} \omega_{\varphi_{t}}\left(y_{t, \delta}\right) \leqslant g .$$

Given the definition of $y_{t, \delta}$, the boundedness of $F$ and that $\delta>0$ is arbitrary, we find as in the proof of 2. above that (6.16) actually implies
$$\operatorname{tr}_{\omega_{B}} \omega_{\varphi_{t}} \leqslant g \quad \text { on } X^{\circ} \backslash B$$
hence on the whole $X^{\circ}$.
To conclude the proof of the RHS inequality in 4., it remains to prove the following
Claim 6.10. - We have
$$g^{-1} t^{k} \cdot \omega_{B}^{n} \leqslant\left(f^{*} \omega_{Z}+t \omega_{B}\right)^{n} \leqslant g t^{k} \cdot \omega_{B}^{n}$$
Proof of Claim 6.10. - The statement is local, so one can assume that $f: \mathbb{C}^{n} \rightarrow \mathbb{C}^{m}$ is given by the projection onto the last $m$ factors and that $B=\sum_{i=1}^{r} b_{i}\left(z_{i}=0\right)$ for some $r \leqslant k$. As the inequality is invariant under quasi-isometry, one can choose $\omega_{Z}=$ $\sum_{j=k+1}^{n} i d z_{j} \wedge d \bar{z}_{j}$ to be the euclidean metric on $\mathbb{C}^{m}$ while
$$\omega_{B}=\sum_{j=1}^{r} \frac{i d z_{j} \wedge d \bar{z}_{j}}{\left|z_{j}\right|^{2 b_{j}}}+\sum_{j=r+1}^{n} i d z_{j} \wedge d \bar{z}_{j}$$
is the standard cone metric. Setting $K:=\prod_{j=1}^{r}\left|z_{j}\right|^{-2 b_{j}}$ and $\omega_{\mathbb{C}^{n}}:=\sum_{j=1}^{n} i d z_{j} \wedge d \bar{z}_{j}$, one finds
$$\omega_{B}^{n}=K \cdot \omega_{\mathbb{C}^{n}}^{n} \quad \text { and } \quad\left(f^{*} \omega_{Z}+t \omega_{B}\right)^{n}=t^{k}(1+t)^{m} K \cdot \omega_{\mathbb{C}^{n}}^{n}$$
which gives the expected result. \(\square\)
4.b We now move on to the LHS inequality in 4. Let us set $v:=\operatorname{tr}_{\omega_{\varphi_{t}}}\left(t \omega_{B}\right)$. Remember from Proposition 6.8 2. that $\omega_{B}$ has holomorphic bisectional curvature bounded from above on $X \backslash B$. By Chern-Lu's inequality, we get on $X \backslash B$
$$\Delta_{\omega_{\varphi_{t}}} \log v \geqslant-C t^{-1} v .$$
Combining that inequality with (6.7)-(6.10) and (6.13), one finds, for $A=C+1$
$$\Delta_{\omega_{\varphi_{t}}}\left(\log v-\frac{A}{t}\left(\varphi_{t}-\underline{\varphi_{t}}\right)+A \psi_{B}+\delta \rho\right) \geqslant \frac{1}{t}(v-g) .$$
Applying the maximum principle and arguing as before, we eventually find $v \leqslant g$ on $X^{\circ} \backslash B$, hence on $X^{\circ}$.
5. The LHS inequality is a direct consequence of 4, by restriction. As for the RHS, it follows easily from the LHS since
$$\begin{aligned}
\left.\operatorname{tr}_{\omega_{B_{z}}} \omega_{\varphi_{t}}\right|_{X_{z}} & \leqslant \frac{\left(\left.\omega_{\varphi_{t}}\right|_{X_{z}}\right)^{k}}{\omega_{B_{z}}^{k}} \cdot\left(\operatorname{tr}_{\left.\omega_{\varphi_{t}}\right|_{X_{z}}} \omega_{B_{z}}\right)^{k-1} \\
& \leqslant g t^{k-(k-1)}
\end{aligned}$$
thanks to (6.6). This ends the proof of Proposition 6.9. \(\square\)

\section*{Step 3. Convergence}

Thanks to Proposition 6.9 1., the family $\left(\varphi_{t}\right)_{0<t \leqslant 1}$ is relatively compact for the $L^{1}$ -topology. All we have to do is showing that all its clusters values coincide. Let $\varphi_{\infty}$ be such a cluster value; it is an $f^{*} \omega_{Z}$-psh function but $f$ has connected fibers so that $\varphi_{\infty}$ is necessarily constant on the fibers. Equivalently, one has $\varphi_{\infty}=f^{*} \varphi_{\infty}$ for the (unique) $\omega_{Z}$-psh function $\underline{\varphi_{\infty}}$ satisfying $\underline{\varphi_{\infty}}(z):=\int_{X_{z}} \varphi_{\infty} \omega_{X}^{k}$ for $z \in Z^{\circ}$. We want to show that the following equality of measures
$$\left(\omega_{Z}+d d^{c} \underline{\varphi_{\infty}}\right)^{m}=f_{*} \mu_{(X, B)}$$
holds on $Z$. Given that Eq. 6.18 has a unique normalized bounded solution, this will prove the Theorem. As $\varphi_{\infty}$ is globally bounded on $X$ thanks to Proposition 6.9 1. and $f_{*} \mu_{(X, B)}$ does not charge any pluripolar set, it is actually enough to show that the equality of measures (6.18) holds on $Z^{\circ}$. In order to prove (6.18) on $Z^{\circ}$, given that $f_{*} \omega_{X}^{k}=1$, it is enough to prove instead that for any function $u \in \mathcal{C}_{0}^{\infty}\left(Z^{\circ}\right)$, one has
$$\int_{X} f^{*} u \cdot\left(f^{*} \omega_{Z}+d d^{c} \varphi_{\infty}\right)^{m} \wedge \omega_{X}^{k}=\int_{X} f^{*} u \cdot d \mu_{(X, B)} .$$

We start from the identity
$$\omega_{\varphi_{t}}^{n}=\left(f^{*} \omega_{Z}+t \omega_{X}+d d^{c} \varphi_{t}\right)^{n}=V_{t} \cdot \mu_{(X, B)}$$
where $V_{t}=\binom{n}{k} t^{k}+o\left(t^{k}\right)$ when $t \rightarrow 0$, cf (6.4). Set $\psi_{t}:=\varphi_{t}-\underline{\varphi_{t}}$ and decompose $\omega_{\varphi_{t}}$ as
$$\omega_{\varphi_{t}}=f^{*}\left(\omega_{Z}+d d^{c} \underline{\varphi_{t}}\right)+\left(t \omega_{X}+d d^{c} \psi_{t}\right) .$$
By expanding, one obtains
$$\omega_{\varphi_{t}}^{n}=\sum_{i=0}^{m}\binom{n}{i} \underbrace{f^{*}\left(\omega_{Z}+d d^{c} \underline{\varphi_{t}}\right)^{i} \wedge\left(t \omega_{X}+d d^{c} \psi_{t}\right)^{n-i}}_{=: \alpha_{i}} .$$
- Case $i=m$.

We expand again
$$\alpha_{m}=\sum_{j=0}^{k-1}\binom{k}{j} t^{j} \underbrace{f^{*}\left(\omega_{Z}+d d^{c} \underline{\varphi_{t}}\right)^{m} \wedge \omega_{X}^{j} \wedge\left(d d^{c} \psi_{t}\right)^{k-j}}_{=: \beta_{j}}+t^{k} f^{*}\left(\omega_{Z}+d d^{c} \underline{\varphi_{t}}\right)^{m} \wedge \omega_{X}^{k} .$$
Performing an integration by parts, one gets
$$\int_{X} f^{*} u \cdot \beta_{j}=\int_{X} \psi_{t} \cdot f^{*} \underbrace{\left(d d^{c} u \wedge\left(\omega_{Z}+d d^{c} \underline{\varphi_{t}}\right)^{m}\right)}_{=0} \wedge \omega_{X}^{j} \wedge\left(d d^{c} \psi_{t}\right)^{k-j-1}=0$$
for degree reasons.
By dominated convergence theorem, we have that $\underline{\varphi_{t}} \rightarrow \underline{\varphi_{\infty}}$ in the $L_{\text {loc }}^{1}\left(Z^{\circ}\right)$ topology. Moreover, as $B$ intersects the fibers of $f$ tranversally over $Z^{\circ}$, an easy argument relying on partition of unity shows that $f_{*}\left(\omega_{B} \wedge \omega_{X}^{k}\right)$ is a smooth (1,1)-form on $Z^{\circ}$. Combining
this with Proposition 6.9 4., we find $d d^{c} \underline{\varphi_{t}}=f_{*}\left(d d^{c} \varphi_{t} \wedge \omega_{X}^{k}\right) \leqslant f_{*}\left(g \omega_{B} \wedge \omega_{X}^{k}\right) \leqslant\left(f_{*} g\right)$. $\omega_{Z}$. Together with (6.9), this implies
$$\pm d d^{c} \underline{\varphi_{t}} \leqslant\left(f_{*} g\right) \cdot \omega_{Z} .$$
By standard result, this shows that $\underline{\varphi_{t}} \rightarrow \underline{\varphi_{\infty}}$ in $C_{\text {loc }}^{1, \alpha}\left(Z^{\circ}\right)$ for any $\alpha<1$. In particular, the quasi-psh functions $\underline{\varphi_{t}}$ converge uniformly on $\operatorname{Supp}(u)$. By Bedford-Taylor theory, one deduces that
$$\int_{X} f^{*} u \cdot f^{*}\left(\omega_{Z}+d d^{c} \underline{\varphi_{t}}\right)^{m} \wedge \omega_{X}^{k} \rightarrow \int_{X} f^{*} u \cdot f^{*}\left(\omega_{Z}+d d^{c} \underline{\varphi_{\infty}}\right)^{m} \wedge \omega_{X}^{k} .$$
In the end, one has showed that
$$\frac{\binom{n}{m}}{V_{t}} \int_{X} f^{*} u \cdot \alpha_{m} \rightarrow \int_{X} f^{*} u \cdot f^{*}\left(\omega_{Z}+d d^{c} \underline{\varphi_{\infty}}\right)^{m} \wedge \omega_{X}^{k} .$$
since $V_{t} \sim\binom{n}{m} t^{k}$.
- Case $i<m$.

We expand
$$\alpha_{i}=\sum_{j=0}^{n-i-1}\binom{n-i}{j} t^{j} \underbrace{f^{*}\left(\omega_{Z}+d d^{c} \underline{\varphi_{t}}\right)^{i} \wedge \omega_{X}^{j} \wedge\left(d d^{c} \psi_{t}\right)^{n-i-j}}_{=: \gamma_{i j}}+t^{n-i} f^{*}\left(\omega_{Z}+d d^{c} \underline{\varphi_{t}}\right)^{i} \wedge \omega_{X}^{n-i} .$$
From (6.21), we find
$$\frac{t^{n-i}}{V_{t}} \int_{X} f^{*} u \cdot f^{*}\left(\omega_{Z}+d d^{c} \underline{\varphi_{t}}\right)^{i} \wedge \omega_{X}^{n-i}=O\left(t^{m-i}\right)=o(1)$$
For the remaining terms, an integration by parts yields
$$\int_{X} f^{*} u \cdot \gamma_{i j}=\int_{X} \psi_{t} \cdot f^{*}\left(d d^{c} u \wedge\left(\omega_{Z}+d d^{c} \underline{\varphi_{t}}\right)^{i}\right) \wedge \omega_{X}^{j} \wedge\left(d d^{c} \psi_{t}\right)^{n-i-j-1}$$
From Proposition 6.9 3., one has $\left|\psi_{t}\right| \leqslant g t$. Moreover, among the ( $n-i-j-1$ ) eigenvalues of $d d^{c} \psi_{t}$ involved in the integral, at least $(n-i-j-1)-(m-(i+1))=k-j$ must come from the fiber. Given Proposition $6.94-5$., the integrand is a $O\left(t^{1+k-j}\right)$. As a result,
$$\frac{t^{j}}{V_{t}} \int_{X} f^{*} u \cdot \gamma_{i j}=O(t) .$$
Combining that result with (6.23), we see that for any $i>m$, one has
$$\lim _{t \rightarrow 0} \frac{1}{V_{t}} \int_{X} f^{*} u \cdot \alpha_{i}=0 .$$

Putting together (6.20), (6.22) and (6.24), we obtain
$$\begin{aligned}
\int_{X} f^{*} u \cdot d \mu_{(X, B)} & =\frac{1}{V_{t}} \int_{X} f^{*} u \cdot \omega_{\varphi_{t}}^{n} \\
& =\lim _{t \rightarrow 0} \sum_{i=0}^{m}\binom{n}{i} \frac{1}{V_{t}} \int_{X} f^{*} u \cdot \alpha_{i} \\
& =\lim _{t \rightarrow 0} \frac{\binom{n}{m}}{V_{t}} \int_{X} f^{*} u \cdot \alpha_{m} \\
& =\int_{X} f^{*} u \cdot f^{*}\left(\omega_{Z}+d d^{c} \underline{\varphi_{\infty}}\right)^{m} \wedge \omega_{X}^{k} .
\end{aligned}$$
In summary, (6.19) is proved, which concludes the proof of the Theorem. \(\square\)
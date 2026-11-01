---
retention_scope: session
part: 2
total_parts: 5
---

[Part 2/5 of: [PDF] On tamed almost complex four manifolds]

In terms of (3.23) and (3.24), there exists a $f_{\phi} \in L_{2}^{2}(M)_{0}$ such that $h_{\phi}=\varphi+\widetilde{\mathcal{D}}_{J}^{+}\left(f_{\phi}\right)$ and
$$\int_{M} \phi \wedge h_{\phi}=c$$
since $\mathcal{H}_{\varphi}$ is a closed space. Since $h \in \mathcal{H}_{\varphi}$, it follows that $h-h_{\phi}$ is in the image of $\widetilde{\mathcal{D}}_{J}^{+}$. Hence,
$$\int_{M} \phi \wedge\left(h-h_{\phi}\right) \leq 0, \quad \int_{M} \phi \wedge\left(h_{\phi}-h\right) \geq 0 .$$
It follows immediately that $\phi$ is weakly $\widetilde{\mathcal{D}}_{J}^{+}$-closed, that is,
$$\int_{M} \phi \wedge \widetilde{\mathcal{D}}_{J}^{+}(f)=0$$
for any $f \in L_{2}^{2}(M)_{0}$. By Lemma 3.11, $\phi \in\left(\Lambda_{\mathbb{R}}^{1,1} \otimes L^{2}(M)\right)_{w}^{0}$ since $h_{J}^{-}=b^{+}-1$.
Let
$$\phi_{0}:=\phi-c F \in\left(\Lambda_{\mathbb{R}}^{1,1} \otimes L^{2}(M)\right)_{w}^{0},$$
then by (3.21) and (3.24), we have
$$\int_{M} \phi_{0} \wedge \varphi \leq c-c=0$$
and
$$\int_{M} \phi_{0} \wedge p_{0}>0$$
for any $p_{0} \in \mathcal{P}$. So $\phi_{0}$ is strictly positive almost everywhere. Hence
$$\int_{M} \phi_{0}^{2}>0 \text { and } \int_{M} \phi_{0} \wedge F>0 .$$
It follows from Corollary 3.10 that
$$\int_{M} \phi_{0} \wedge \varphi>0$$
giving a contradiction (see (3.26)). Therefore $\mathcal{P}_{\varepsilon} \cap \mathcal{H}_{\varphi}$ can not be empty proving the existence of $p_{\varepsilon}$ and $f_{\varepsilon}$. The last statement of the lemma follows from denseness of the smooth positive (1, 1)-forms in the $L^{2}$-positive (1, 1)-forms and of the smooth functions in $L_{2}^{2}(M)_{0}$. This completes the proof of Lemma 3.12. \(\square\)

In next section, we will devote to proving main theorem, i.e. Theorem 1.1. The proof of Theorem 1.1 follows mainly Buchdahl's unified proof of the Kodaira conjecture.

\section*{4 The tamed almost complex 4-manifolds with $h_{J}^{-}=b^{+}-1$}

This section is devoted to proving Theorem 1.1 which follows mainly Buchdahl's unified proof of Kodaira conjecture.. Throughout this section, we assume that $(M, J)$ is a closed tamed almost complex 4-manifold with $h_{J}^{-}=b^{+}-1$. Without loss of generality, we may assume that $J$ is tamed by a symplectic form $\omega_{1}=F+d_{J}^{-}(v+\bar{v})$, where $F$ is a fundamental 2-form,
$$F^{2}>0, \quad \int_{M} F^{2}=2, \quad \int_{M} d_{J}^{-}(v+\bar{v}) \wedge d_{J}^{-}(v+\bar{v})=2 a>0, \quad v \in \Omega_{J}^{0,1} .$$
Set $g(\cdot, \cdot)=F(\cdot, J \cdot)$ that is an almost Hermitian metric on $(M, J)$. Denote by $d \mu_{g}$ the volume form defined by $g$. Set $\widetilde{\omega}_{1}=\omega_{1}-d(v+\bar{v})=F-d_{J}^{+}(v+\bar{v}) \in \mathcal{Z}_{J}^{+}$,
$$\int_{M} \omega_{1}^{2}=2(1+a)=\int_{M} \widetilde{\omega}_{1}^{2} .$$
It is easy to see that
$$\begin{gathered}
\int_{M} d_{J}^{+}(v+\bar{v}) \wedge d_{J}^{+}(v+\bar{v})=-2 a \\
\int_{M} F \wedge d_{J}^{+}(v+\bar{v})=-2 a
\end{gathered}$$
From Section 3, we know that $\widetilde{\omega}_{1}$ is in $\mathcal{Z}_{J}^{+}$and cohomologous to $\omega_{1}$ satisfying
$$\int_{M} \widetilde{\omega}_{1}^{2}=2(1+a), \quad \int_{M} \widetilde{\omega}_{1} \wedge F=2(1+a) .$$
By Lemma 3.11, since $h_{J}^{-}=b^{+}-1$, we have that $\widetilde{\omega}_{1} \in\left(\Lambda_{\mathbb{R}}^{1,1} \otimes L^{2}(M)\right)_{w}^{0}$. Let $\phi=$ $\widetilde{\omega}_{1}-(1+a) F$, it is easy to see that
$$\int_{M} P_{g}^{+}(\phi) \wedge \omega_{1}=\int_{M} \phi \wedge \omega_{1}=0 .$$
Hence $P_{g}^{+}(\phi)$ is orthogonal to $\mathcal{H}_{g}^{+}(M)$ with respect to the integration since $h_{J}^{-}=b^{+}-1$. Moreover, note that both $F$ and $\widetilde{\omega}_{1}$ are weakly $\widetilde{\mathcal{D}}_{J}^{+}$-closed, so $\phi$ is weakly $\widetilde{\mathcal{D}}_{J}^{+}$-closed.

For
$$0<t_{0}=1+a-\sqrt{(1+a)^{2}-(1+a)}=\left(1+\sqrt{\frac{a}{1+a}}\right)^{-1}<1,$$
the smooth (1, 1)-form
$$\varphi=\widetilde{\omega}_{1}-t_{0} F=(\sqrt{a(1+a)}-a) F-d_{J}^{+}(v+\bar{v})$$
is still in $\left(\Lambda_{\mathbb{R}}^{1,1} \otimes L^{2}(M)\right)_{w}^{0}$.
$$\begin{aligned}
\int_{M} \varphi^{2} & =2(\sqrt{a(1+a)}-a)^{2}+4(\sqrt{a(1+a)}-a) a-2 a \\
& =2 a(1+a)-4 a \sqrt{a(1+a)}+2 a^{2}+4 a \sqrt{a(1+a)}-4 a^{2}-2 a \\
& =0,
\end{aligned}$$
$$\begin{aligned}
\int_{M} F \wedge \varphi & =2(\sqrt{a(1+a)}-a)+2 a \\
& =2 \sqrt{a(1+a)}>0 .
\end{aligned}$$
By Lemma 3.12, for each $m \in \mathbb{N}$ there is a smooth positive (1,1)-form $p_{m}$ and a smooth function $f_{m} \in C^{\infty}(M)_{0}$ such that
$$\left\|\varphi+\widetilde{\mathcal{D}}_{J}^{+}\left(f_{m}\right)-p_{m}\right\|_{L^{2}}<\frac{1}{m} .$$
Since
$$\begin{aligned}
\int_{M} p_{m} \wedge F & =-\int_{M}\left(\varphi+\widetilde{\mathcal{D}}_{J}^{+}\left(f_{m}\right)-p_{m}\right) \wedge F+\int_{M}\left(\varphi+\widetilde{\mathcal{D}}_{J}^{+}\left(f_{m}\right)\right) \wedge F \\
& =-\int_{M}\left(\varphi+\widetilde{\mathcal{D}}_{J}^{+}\left(f_{m}\right)-p_{m}\right) \wedge F+\int_{M} \varphi \wedge F \\
& =-\int_{M}\left(\varphi+\widetilde{\mathcal{D}}_{J}^{+}\left(f_{m}\right)-p_{m}\right) \wedge F+2 \sqrt{a(1+a)}
\end{aligned}$$
and
$$\left|-\int_{M}\left(\varphi+\widetilde{\mathcal{D}}_{J}^{+}\left(f_{m}\right)-p_{m}\right) \wedge F\right| \leq\left\|\varphi+\widetilde{\mathcal{D}}_{J}^{+}\left(f_{m}\right)-p_{m}\right\|_{L^{2}}\|F\|_{L^{2}}<\frac{\sqrt{2}}{m},$$
the integral
$$\int_{M} p_{m} \wedge F$$
is converging to $2 \sqrt{a(1+a)}>0$ and by Lemma 2.9 and Lemma 3.1, the positive functions $\left(\wedge p_{m}\right)^{\frac{1}{2}}$ are uniformly bounded in $L^{2}$, where $\wedge: \Omega_{\mathbb{R}}^{1,1} \longrightarrow \Omega_{\mathbb{R}}^{0}$ is an algebraic operator in Lefschetz decomposition (cf. [31]). So a subsequence can be found converging weakly in $L^{2}$. The forms $p_{m} /\left(\wedge p_{m}\right)$ are bounded in $L^{\infty}$, so subsequence of these forms can also be found converging weakly in $L^{4}$. The sequence $\left\{\widetilde{\mathcal{D}}_{J}^{+}\left(f_{m}\right)\right\}=\left\{d \widetilde{\mathcal{W}}\left(f_{m}\right)\right\}$ is uniformly bounded in $L^{1}$. The uniform $L^{1}$ bound on $\widetilde{\mathcal{D}}_{J}^{+}\left(f_{m}\right)$ does not imply an $L^{2}$ bound on $f_{m}$, it really needed to find a subsequence converge in the sense of currents. Hence, we have the following claim.

Claim 4.1. Given any $s<\frac{4}{3}$ and $t<2$, there is a subsequence of $\left\{f_{m}\right\}$ that converges weakly in $L_{1}^{s}$, and strongly in $L^{t}$ to a limiting function $f_{0}$.

Proof. If $J$ is integrable, $\mathcal{D}_{J}^{+}=\sqrt{-1} \partial_{J} \bar{\partial}_{J}$. Xiaowei Xu [81] pointed out that the uniform $L^{1}$ bound on $\sqrt{-1} \partial_{J} \bar{\partial}_{J}\left(f_{m}\right)$ does not imply an $L^{2}$ bound on $f_{m}$. It means that in Buchdahl [7, p.296] there exists a gap. Buchdahl gave a new argument (cf. X. Xu [81]). In the follows,
we will give a proof of the above claim which follows the argument of N. Buchdahl (cf. X. Xu [81]).

Since $h_{J}^{-}=b^{+}-1, J$ is tamed by $\omega_{1}=F+d_{J}^{-}(v+\bar{v})$, by Proposition 2.7,
$$\widetilde{\mathcal{D}}_{J}^{+}\left(f_{m}\right)=d \widetilde{\mathcal{W}}\left(f_{m}\right)=2 d d^{*} \mathbb{G}\left(f_{m}^{\prime} F\right)=2 d \mathbb{G} d^{*}\left(f_{m}^{\prime} F\right)$$
and
$$P_{g}^{+} \widetilde{\mathcal{D}}_{J}^{+}\left(f_{m}\right)=2 P_{g}^{+} d d^{*} \mathbb{G}\left(f_{m}^{\prime} F\right)=\Delta_{g} \mathbb{G}\left(f_{m}^{\prime} F\right)=f_{m}^{\prime} F,$$
where $f_{m}^{\prime} \in L^{2}(M)_{0}$ and $\mathbb{G}$ is the Green operator associated to $\Delta_{g}$ (cf. [49]). First, take any real number $t^{\prime}>2$ and let $h$ be any function in $L^{t^{\prime}}(M)_{0}$, that is,
$$\int_{M} h d \mu_{g}=0$$
and $h \in L^{t^{\prime}}(M)$, so
$$h F^{2}=2 P_{g}^{+} d d^{*} \mathbb{G}\left(f_{m}^{\prime} F\right) \wedge F=\Delta_{g} \mathbb{G}\left(f_{m}^{\prime} F\right) \wedge F$$
and $\mathbb{G}(h F) \in L_{2}^{t^{\prime}}$. This is standard linear elliptic theory. By the Sobolev embedding theorem, the fact $t^{\prime}>2$ implies that $L_{2}^{t^{\prime}}$ is compactly embedded in $C^{0}$, so there is a uniform $C^{0}$ bound on $\mathbb{G}(h F)$ in terms of its $L_{2}^{t^{\prime}}$ norm, and that in turn is uniformly bounded by a constant times the $L^{t^{\prime}}$ norm of $2 d d^{*} \mathbb{G}(h F)$ by ellipticity and the fact that $h F$ has been chosen to orthogonal to the kernal in $L^{2}$. So the sup norm of $\mathbb{G}(h F)$ is bounded by a fixed constant times the $L^{t^{\prime}}$ norm of $h$. Then
$$\begin{aligned}
\int_{M} f_{m}^{\prime} h F^{2} & =\int_{M} f_{m}^{\prime} F \wedge h F \\
& =\int_{M} f_{m}^{\prime} F \wedge \Delta_{g} \mathbb{G}(h F) \\
& =\int_{M} \Delta_{g} \mathbb{G}\left(f_{m}^{\prime} F\right) \wedge h F \\
& =\int_{M} 2 d \mathbb{G} d^{*}\left(f_{m}^{\prime} F\right) \wedge h F \\
& =\int_{M} \widetilde{\mathcal{D}}_{J}^{+}\left(f_{m}\right) \wedge h F .
\end{aligned}$$
Since $p_{m}$ is uniformly bounded in $L^{1}$ and $\varphi+\widetilde{\mathcal{D}}_{J}^{+}\left(f_{m}\right)-p_{m}$ is converging to 0 in $L^{2}$, it follows that $\widetilde{\mathcal{D}}_{J}^{+}\left(f_{m}\right)$ is uniformly bounded in $L^{1}$. Therefore
$$\left|\int_{M} f_{m}^{\prime} h F^{2}\right| \leq C o n s t .\|h\|_{L^{t^{\prime}}},$$
which shows that the sequence $\left\{f_{m}^{\prime}\right\}$ (resp. $\left\{f_{m}\right\}$ ) is weakly bounded in $L^{t}$, where $\frac{1}{t}+\frac{1}{t^{\prime}}=$ 1. Since it is weakly bounded, it is bounded, and therefore we can find a subsequence converging weakly in $L^{t}$. We now have to do the same thing with the first derivatives. Recall that
$$\widetilde{\mathcal{W}}(h)=2 \mathbb{G} d^{*}(h F), \widetilde{\mathcal{D}}_{J}^{+}(h)=d \widetilde{\mathcal{W}}(h)=2 d \mathbb{G} d^{*}(h F) .$$

Since
$$\begin{aligned}
\int_{M} \widetilde{\mathcal{D}}_{J}^{+}(h) \wedge f_{m} \omega_{1} & =\int_{M} d \widetilde{\mathcal{W}}(h) \wedge f_{m} \omega_{1} \\
& =-\int_{M} \widetilde{\mathcal{W}}(h) \wedge d f_{m} \wedge \omega_{1} .
\end{aligned}$$
As done in Lemma 3.2, we can prove that $\widetilde{\mathcal{W}}(h)$ has closed range. This time we take any $\widetilde{\mathcal{W}}(h)$ that lies in $L^{s^{\prime}}$ where $s^{\prime}>4$. Then, following the same reason as above, we get $\left\{d f_{m}\right\}$ uniformly bounded in $L^{s}$ for $\frac{1}{s}+\frac{1}{s^{\prime}}=1$ and therefore $\left\{d f_{m}\right\}$ strongly bounded in $L^{s}$. We can then use the compactness part of the Sobolev embedding theorem to pick out a subsequence that converges strongly in $L^{q}$, where $q<2$. This completes the proof of the claim. \(\square\)

By Claim 4.1, the subsequence of positive (1, 1)-forms $\left\{p_{m}\right\}$ in the sense of currents to define a positive (1,1)- current $p=\varphi+\widetilde{\mathcal{D}}_{J}^{+}\left(f_{0}\right), f_{0} \in L_{2}^{q}(M)_{0}$ for some fixed $q \in(1,2)$. Note that since $\wedge p \in L^{1}$ and $p /(\wedge p) \in \Lambda_{\mathbb{R}}^{1,1} \otimes L^{\infty}$, the current
$$P=p+t_{0} F=\widetilde{\omega}_{1}+\widetilde{\mathcal{D}}_{J}^{+}\left(f_{0}\right)$$
is a closed ( 1,1 )-current which lies in $L^{1}$ satisfying $P \geq t_{0} F$. Thus, $P$ is called an almost Kähler current (cf. [12, 35-37, 59, 63, 64, 71, 76]). In summary, we have the following proposition:

Proposition 4.2. (see Theorem 11 in [7] and Lemma 1.7 in [71]) Suppose that ( $M, J$ ) is a closed almost complex 4-manifold with $h_{J}^{-}=b^{+}-1$ which is tamed by a symplectic form $\omega_{1}$. As defined the above,
$$P=p+t_{0} F=\widetilde{\omega}_{1}+\widetilde{\mathcal{D}}_{J}^{+}\left(f_{0}\right)$$
is a closed positive almost complex (1,1)-current in $L^{1}$ (almost Kähler current) and satisfies $P \geq t_{0} F$, where $f_{0} \in L_{2}^{q}(M)_{0}$ for some fixed $q \in(1,2)$ and
$$0<t_{0}=\left(1+\sqrt{\frac{a}{1+a}}\right)^{-1}<1 .$$
$P$ is homologous to $\widetilde{\omega}_{1}$ in the sense of current.
Remark 4.3. (1)If $J$ is integrable, which is tamed by $\omega_{1}$, then $h_{J}^{-}=b^{+}-1$ since $\omega_{1} \in$ $\mathcal{H}_{g}^{+}(M)$. By the Dolbeault decomposition (cf. Remark 2.2, or 3, 18]), it is easy to see that $b^{1}=$ even . On the other hand, for any compact complex surface, if $b^{1}=$ even, then there exists a symplectic from $\omega$ by which the integrable complex structure $J$ is tamed. Therefore, for any compact complex surface, $b^{1}=$ even if and only if there exists a symplectic form $\omega$ by which the integrable complex structure $J$ is tamed. Hence Theorem 1.1 is an affirmative answer to the Kodiria conjecture. The key ingredients in the unified proof of the Kodaira conjecture by N. Buchdahl in [7] are Theorem 11 in [7] (i.e., Proposition 4.2), Y.-T. Siu's theorem [70] on the analyticity of the sets associated with the Lelong numbers of closed positive currents, and J.-P. Demailly's result [12] on the smoothing of closed positive (1,1)-currents.
(2) Taubes studies Donaldson's "tamed to compatible" question in [76]. He constructs an almost Kähler form in the class $[\omega]$ for a generic almost complex structure tamed by a symplectic form $\omega$ on a 4-manifold $M$ with $b^{+}=1$. To construct the almost Kähler form, Taubes' strategy is first to construct a closed positive $(1,1)$ current $\Phi_{\mathcal{K}}$ in class $[\omega]$ by irreducible $J$-holomorphic subvarieties. This special current satisfies
$$\mathcal{K}^{-1} t^{4}<\Phi_{\mathcal{K}}\left(\sqrt{-1} f_{B} \sigma \wedge \bar{\sigma}\right)<\mathcal{K} t^{4},$$
where $\mathcal{K}>1$ is a constant, $B$ is a ball of radius $t, \sigma$ denotes a unit length section of $\left.\Lambda^{1,0} M\right|_{B}$ and $f_{B}$ denotes the characteristic function of $B$ (cf. Proposition 1.3 in [76]). To obtain a genuine almost Kähler form, Taubes smooths currents by a compact supported, closed 4-form on TM which represents the Thom class in the compactly supported cohomology of TM (cf. §1.6 of [4]).
M. Lejmi [54] shows that any almost complex manifold $(M, J)$ of dimension 4 has the local symplectic property, i.e. $\forall p \in M$, there is a local symplectic form $\omega_{p}=d \tau_{p}$ compatible with $J$ on a neighborhood, $U_{p}$, of $p$, where $\left.\tau_{p} \in \Omega_{\mathbb{R}}^{1}\right|_{U_{p}}$. Note that as a trivial example, any complex manifold has the local symplectic property, hence almost complex manifolds with the local symplectic property can be regarded as a generalization of complex manifold. On the other hand, R. Bryant, M. Lejmi [5,6,54] showed that the almost complex structure underlying a non-Kähler, nearly Kähler 6-manifold ( in particular, the standard almost complex structure of $S^{6}$ ) can not be compatible with any symplectic form, even locally. Recall that for any closed positive (1,1)-current on an analytic variety, one can define Lelong number (cf. [13, 31, 45]). By using locally symplectic form $\omega_{p}$, we will define Lelong number for any closed positive almost complex (1,1)-current on an almost Hermitian 4-manifold $(M, g, J, F)$ in Appendix B. 1 (cf. [15,24,35-37,59,64,83]).

In the remainder of this section, we will devote to proving our main theorem (Theorem 1.1). To prove Theorem 1.1, we will study strictly $J$-plurisubharmonic functions, closed strictly positive $(1,1)$-current $\widetilde{\mathcal{D}}_{J}^{+}(f)$, Lelong numbers, the decomposition theorem and the regularization of almost Kähler currents in appendices A, B, C. With the results in appendices, we now prove Theorem 1.1 by the similar method in [7], in particular, by using Proposition 4.2.

Proof of Theorem 1.1: By Proposition 4.2, we have a positive $d$-closed almost complex (1, 1)-current
$$P=p+t_{0} F=\widetilde{\omega}_{1}+\widetilde{\mathcal{D}}_{J}^{+}\left(f_{0}\right) \geq t_{0} F$$
on $(M, g, J, F)$ which is tamed by the symplectic form $\omega_{1}$, it follows that $P$ is an almost Kähler current and $\operatorname{Supp} P=M$. To complete the proof of Theorem 1.1, by using the almost Kähler current $P$ we will construct an almost Kähler form. Let $\nu_{1}(x, P)$ denote the Lelong number of $P$ at $x$ defined as follows: If $x \in \operatorname{supp} P$, we define
$$\nu_{1}\left(x, \omega_{1}, r, P\right)=\int_{B(x, r)} P \wedge \omega_{1},$$
where $B(x, r):=\left\{y \in M \mid \rho_{g}(x, y) \leq r\right\}, \rho_{g}(x, y)$ is the geodesic distance of points $x, y$ with
respect to the almost Kähler metric $g$. And
$$\nu_{1}(x, P)=\lim _{r \rightarrow 0} r^{-2} \nu_{1}\left(x, \omega_{1}, r, P\right) .$$
For more details, see Definition B. 13 in Appendix B.1. For $c>0$, the upperlevel set
$$E_{c}(P):=\left\{x \in M \mid \nu_{1}(x, P) \geq c\right\}$$
is a $J$-analytic subset (cf. Appendix B. 1 or [24, Definition 2] for the definition) of $M$ of dimension (complex) $\leq 1$ by the decomposition theorem (will be proven in Appendix B.2, see Theorem B. 21 and Remark B.22) which is analogous to Siu's Decomposition Formula [70].

By F. Elkhadhra's result (see Theorem 2 in [24] or Lemma B. 9 in Appendix B.1), if $D$ is an irreducible $J$-holomorphic curve in $E_{c}(P)$,
$$\nu_{0}:=\inf \left\{\nu_{1}(x, P) \mid x \in D\right\}, \quad \nu_{1}(x, P)=\nu_{0}$$
for almost all $x \in D$. If $D_{1}, \cdots, D_{n}$ are the irreducible $J$-holomorphic curves in $E_{c}(P)$ and
$$\nu_{i}:=\inf \left\{\nu_{1}(x, P) \mid x \in D_{i}\right\},$$
the $d$-closed (1,1)-current
$$T=P-\Sigma \nu_{i} T_{D_{i}}$$
is positive and the $c$-upperlevel set $E_{c}(T)$ of this current are isolated singular points by Theorem B. 21 and Remark B. 22 in Appendix B. 2 as in classical complex analysis. Here $T_{D_{i}}$ are the currents of integration on $D_{i}$.

As done in [7], it is always possible to approximate the closed positive current $T$ by smooth real currents admitting a small negative part and that this negative part can be estimated in terms of the Lelong numbers of $T$ and the geometry of $(M, g, J, F)$ (cf. Theorem C. 12 and Remark C. 13 in Appendix C.4). Fix a number $K \geq 0$ such that the $(1,1)$ curvature form, $R^{\nabla^{1}}$, of the second canonical connection $\nabla^{1}$ with respect to the metric $g$ (cf. [28]) on $T M$ satisfies $R^{\nabla^{1}} \geq-K F \otimes I d_{T M}$ and let $c>0$ be such that $t_{0}-c K>0$, where $R^{\nabla^{1}}=R_{i k \bar{l}}^{j} \theta^{k} \wedge \bar{\theta}^{l}, 1 \leq i, j, k, l \leq 2$, and $\left\{\theta^{1}, \theta^{2}\right\}$ is a coframe for $\Lambda_{J}^{1,0}$ (see [77] or Appendix C.1). Since the approximation theorem is locally proved, we can consider $J$-pseudoconvex domain. Notice that $(M, g, J, F)$ is a closed $\omega_{1}$-tamed almost Hermitian 4-manifold which has the local symplectic property [54], hence for $\forall x \in M$, there is a neighborhood $U_{x}$ of $x$ and a $J$-compatible symplectic form $\omega_{x}$ on $U_{x}$ such that
$$\left.\omega_{x}\right|_{x}=\left.F\right|_{x},\left.F\right|_{U_{x}}=\left.f_{x} \omega_{x}\right|_{U_{x}},$$
where $f_{x} \in C^{\infty}\left(U_{x}\right), f_{x}(x)=1$. Fix a point $y \in U_{x}$. We may assume that $r$ is small enough such that $B(y, r) \subset U_{x}$. On symplectic 4-manifold $\left(U_{x}, \omega_{x}\right)$, we can define Lelong number for closed positive (1, 1)-current on $\left(U_{x}, \omega_{x}\right)$
$$\nu_{2}\left(y, \omega_{x}, r, T\right)=\frac{2}{r^{2}} \int_{B(y, r)} T \wedge \omega_{x}$$
and
$$\nu_{2}(y, x, T)=\lim _{r \rightarrow 0} \nu_{2}\left(y, \omega_{x}, r, T\right) .$$
Also we may assumed that $U_{x}$ is very samll and a strictly $J$-pseudoconvex domain, hence we can solve $\widetilde{\mathcal{W}}, d_{J}^{-}$-problem on $U_{x}$ (similar to $\bar{\partial}$-problem in classical complex analysis [40]). More details, see Appendix A.3. Thus, there exists a strictly $J$-plurisubharmonic function $f_{0}^{\prime}$ on $U_{x}$ such that
$$\widetilde{\mathcal{D}}_{J}^{+}\left(f_{0}\right)=\widetilde{\mathcal{D}}_{J}^{+}\left(f_{0}^{\prime}\right),$$
where $\widetilde{\mathcal{D}}_{J}^{+}\left(f_{0}\right)$ is defined in the equality (4.5), the solution $f_{0}^{\prime}$ satisfies the above equation with respect to the metric $g_{x}(\cdot, \cdot)=\omega_{x}(\cdot, J \cdot)$. By Remark 2.6, $\widetilde{\mathcal{D}}_{J}^{+}\left(f_{0}^{\prime}\right)=\mathcal{D}_{J}^{+}\left(f_{0}^{\prime}\right)$ since $\left(U_{x}, g_{x}, J, \omega_{x}\right)$ is an almost Kähler 4-manifold. By Theorem B. 15 in Appendix B.1, $\nu_{1}(y, T)=f_{x}(y) \nu_{2}(y, x, T), \forall y \in \sup T \cap U_{x}$.

As done in classical complex analysis, using the regularization of almost Kähler currents (For more details, we refer to Appendix C.3, C.4. Notice that Theorem C. 12 in Appendix C. 4 still holds for $\widetilde{\mathcal{D}}_{J}^{+}\left(f_{0}\right)$ since the approximation theorem is locally proved, see Remark C. 13 in Appendix C.4), there is a 1-parameter family $T_{c, \varepsilon}$ of $d$-closed positive (1,1)-currents in the same homology class as $T=P-\Sigma \nu_{i} T_{D_{i}}$ in the sense of currents which weakly converges to $T$ as $\varepsilon \rightarrow 0^{+}$, with $T_{c, \varepsilon}$ smooth off $E_{c}(T)$
$$T_{c, \varepsilon} \geq\left(t_{0}-\min \left\{\lambda_{\varepsilon}, c\right\} K-\delta_{\varepsilon}\right) F$$
for some continuous functions $\lambda_{\varepsilon}$ on $M$ and constants $\delta_{\varepsilon}$ satisfying $\lambda_{\varepsilon}(x) \searrow \nu_{1}(x, T)$ for each $x \in M$ and $\delta_{\varepsilon} \searrow 0$ (see Buchdahl [7, P.296] or Appendix C). Moreover, $\nu_{1}\left(x, T_{c, \varepsilon}\right)=$ $\left(\nu_{1}(x, T)-c\right)_{+}$at each point $x$. For $\varepsilon$ sufficiently small therefore, $T_{c, \varepsilon} \geq t_{1} F$ for some $t_{1}>0$, where $t_{1}$ can be chosen arbitrarily close to $t_{0}$ if $c$ and $\varepsilon$ are small enough (see Buchdahl [7, P.296] or Appendix C).

The current $T_{c, \varepsilon}$ is smooth off the zero-dimensional singular set $E_{c}(T)$, that is, off a finite set of points since $M$ is compact. More details, see Appendix B. Without loss of generality, we may assume that $E_{c}(T)=\left\{p_{0}\right\}$. There is a neighbourhood, $U_{p_{0}}$, of $p_{0}$ and a locally symplectic form $\omega_{p_{0}}=d \tau_{p_{0}}$ on $U_{p_{0}}$ that is compatible with $\left.J\right|_{U_{p_{0}}}$, where $\left.\tau_{p_{0}} \in \Omega_{\mathbb{R}}^{1}\right|_{U_{p_{0}}}$. Without loss of generality, we may assume that $U_{p_{0}}$ is $\omega_{p_{0}}$-convex which is also called $J$-pseudoconvex (for the definition of $J$-pseudoconvex we refer to Appendix A.1, and for more details, please see [22, 33, 63]). Moreover, we assume that $U_{p_{0}}$ is a strictly $J$-pseudoconvex domain in the almost complex 4-manifold $\left(\mathbb{R}^{4}, J\right)$ (also see Appendix A.3). By Lemma A. 11 (which solves $\widetilde{\mathcal{W}}, d_{J}^{-}$-problem), there exists a strictly $J$-plurisubharmonic function $f$ such that $T_{c, \varepsilon}=d \widetilde{\mathcal{W}}(f)=\widetilde{\mathcal{D}}_{J}^{+}(f)$ since $\left.T_{c, \varepsilon}\right|_{U_{p_{0}}}$ is a closed positive (1,1)-current. Also we have the following estimate (see Theorem A. 31 in Appendix A.3):
$$\|f\|_{L^{2}\left(U_{p_{0}}, \varphi\right)} \leq \frac{1}{\sqrt{c}}\|\widetilde{\mathcal{W}}(f)\|_{L^{2}\left(U_{p_{0}}, \varphi\right)},$$
where $\varphi$ is a strictly $J$-plurisubharmonic function satisfying
$$\sum_{i, j}\left(\partial_{J_{i}} \bar{\partial}_{J_{j}} \varphi\right) \xi^{i} \bar{\xi}^{j} \geq c \sum_{i}\left|\xi^{i}\right|^{2}$$
$\xi \in \mathbb{C}^{2}$. Note that when $U_{p_{0}}$ is very small, we can choose $\varphi=|z|^{2}=\left|z_{1}\right|^{2}+\left|z_{2}\right|^{2}$, $\left(z_{1}, z_{2}\right) \in \mathbb{C}^{2}$ which is the Darboux coordinate chart on $\left(U_{p_{0}}, \omega_{p_{0}}\right)$ (see Proposition 6.4 in [37]). Using a standard modifying function as in [30, p.147], $f$ can be smoothed in a neighbourhood of $p_{0}$ to a family $f_{t}$ of smooth strictly $J$-plurisubharmonic functions converging to $f$.

Recently, F.R. Harvey, H.B. Lawson JR. and S. Pliś got a result in [38] (see Theorem 4.1 in [38] or Proposition A.10): Suppose $(X, J)$ is an almost complex manifold which is $J$-pseudoconvex, and let $f$ be a $J$-plurisubharmonic function on $(X, J)$. Then there exists a decreasing sequence $f_{j}$ of smooth strictly $J$-plurisubharmonic functions point-wise decreasing down to $f$.

On an annular region surrounding $p_{0}$ the convergence of this sequence is uniform in $C^{k}$ for any $k$ with respect to the almost Kähler metric $g_{J}^{\prime}(\cdot, \cdot):=\omega_{p_{0}}(\cdot, J \cdot)$. (by Lemma 4.1 and the accompanying discussing in [30]). Choose two small neighbourhoods, $U_{p_{0}}^{\prime}$ and $U_{p_{0}}^{\prime \prime}$ of $p_{0}$ satisfying $p_{0} \in U_{p_{0}}^{\prime} \subset \subset U_{p_{0}}^{\prime \prime} \subset \subset U_{p_{0}}$. Construct a cut-off function:
$$\rho(x)= \begin{cases}1 & x \in M \backslash U_{p_{0}}^{\prime \prime}, \\ 0 & x \in \bar{U}_{p_{0}}^{\prime} .\end{cases}$$
It is clear that $\rho f+(1-\rho) f_{t}$ is a smooth strictly $J$-plurisubharmonic function for $t$ sufficiently small which agrees with $f$ outside the annulus. Construct a smooth closed strictly positive $(1,1)$ form $\tau_{c, \varepsilon}$ for $\varepsilon>0$ as follows:
$$\tau_{c, \varepsilon}= \begin{cases}T_{c, \varepsilon} & \text { on } M \backslash U_{p_{0}}, \\ d \overline{\mathcal{W}}\left(\rho f+(1-\rho) f_{t}\right) & \text { on } \bar{U}_{p_{0}} .\end{cases}$$
Hence the current $T_{c, \varepsilon}$ is $\widetilde{\mathcal{D}}_{J}^{+}$-homologous to the smooth closed strictly positive (1,1)-form $\tau_{c, \varepsilon}$. Moreover, for $0<t_{1}<t_{0}$, there is some $c$ and $\varepsilon$ such that $\tau_{c, \varepsilon} \geq t_{1} F$ (see Buchdahl [7, P.296]). Thus, $\tau_{c, \varepsilon}$ is a smooth almost Kähler form on $(M, J)$. This completes the proof of Theorem 1.1. \(\square\)

In the following three appendixes, we will discuss $J$-plurisubharmonic functions as in classical complex analysis, minimal principle for $J$-plurisubharmonic functions, Lelong numbers of closed positive (1, 1)-currents on almost complex 4-manifold, Siu's decomposition theorem for closed positive (1, 1)-currents on tamed almost complex 4-manifold and Demailly's regularization theorem for closed positive (1, 1)-currents on tamed almost complex 4-manifold. These notations and results extend various foundational notations and results from pluripotential theory, used in the main argument in Section 4, to the almost-complex case.

\section*{Appendices}

\section*{Appendix A Elementary pluripotential theory}

This appendix is devoted to discussing $J$-plurisubharmonic functions, minimal principle for $J$-plurisubharmonic functions, $\widetilde{\mathcal{W}}, d_{J}^{-}$-problem on tamed almost complex 4-manifolds,
and the singularities of $J$-plurisubharmonic functions.

\section*{A. $1 J$-plurisubharmonic functions on almost complex manifolds}

In this subsection, we will discuss $J$-plurisubharmonic functions on almost complex manifolds as done in classical complex analysis. We will adopt classical notations from geometric measure theory [14, 23, 24, 35-37, 41, 63, 65, 66].

Let $(M, J)$ be an almost complex manifold of real dimension $2 n$. We let $\mathcal{D}^{p, q}(M)$ denote the space of $C^{\infty}(p, q)$-forms on $M$ with compact support and let $\mathcal{D}^{\prime p, q}(M)=\mathcal{D}^{n-p, n-q}(M)^{\prime}$ be the space $(p, q)$-currents on $(M, J)$. We also let $\mathcal{E}^{p, q}(M)$ be the space of $C^{\infty}(p, q)$-forms on $(M, J)$ and $\mathcal{E}^{\prime p, q}(M)=\mathcal{E}^{n-p, n-q}(M)^{\prime}$ denote the space of compactly supported $(p, q)$ -currents on $(M, J)$. Suppose $T \in \mathcal{D}^{\prime p, q}(M)$. We let Singsupp $T$ denote the smallest closed subset $A$ of $M$ such that $T$ is a smooth current on $M \backslash A$. For $\varphi \in \mathcal{D}^{n-p, n-q}(M)$, we let $(T, \varphi)=T(\varphi)$ denote the pairing of $T$ and $\varphi$. We note that if $M$ is a closed manifold and $T, \varphi$ is closed, then $(T, \varphi)=(T \cdot \varphi)$, where $(T \cdot \varphi)$ is the intersection number given by the cup-product (cf. [4, 31, 35-37, 63]).

Definition A.1. (cf. [24, 42]) (1) A real ( $p, p$ )-form on ( $M, J$ ) is strictly positive (positive) if it is strictly positive (positive) at each point. A real $(p, p)$-current $T$ on $M$ is positive if $(T, \varphi)$ is positive for all test strictly positive $(n-p, n-p)$-forms $\varphi$ on $(M, J)$.
(2) A real $(p, p)$-current $T$ on $(M, J)$ is strictly positive if there is a strictly positive (1, 1)-form $F$ on $(M, J)$ such that $T-F^{p}$ is positive; $T$ is said to be strictly positive at a point $x \in M$ if there is a neighborhood $U$ of $x$ such that $\left.T\right|_{U}$ is a strictly positive current on $U$.

Note that $T$ is strictly positive on $(M, J)$ if and only if $T$ is strictly positive at each point of $M$. By the definition above, a smooth form is strictly positive (positive) as a form if and only if it is strictly positive (positive) as a current. If a $(p, p)$-current $T$ is strictly positive (positive), we write $T>0(T \geq 0)$. We also write $S>T(S \geq T)$ if $S-T>0(S-T \geq 0)$, for $(p, p)$-currents $S, T$. A strictly positive (1,1)-current on an almost complex manifold is called an almost Kähler current [76, 83] (Since a strictly positive $(1,1)$-current on a complex manifold $(M, J)$ is called Kähler current [13,31].).

In fact, for any real-valued $C^{\infty}$-function $u$ we have $\partial_{J} \bar{\partial}_{J} u=-\bar{\partial}_{J} \partial_{J} u$ (see (2.9)). We can define the complex Hessian operator (cf. Harvey-Lawson [37])
$$\mathcal{H}: C^{\infty}(M) \rightarrow \Gamma\left(M, \Lambda_{J}^{1,1}\right)$$
by $\mathcal{H}(u)(X, Y):=\left(\partial_{J} \bar{\partial}_{J} u\right)(X, \bar{Y})$ for $X, Y \in T M^{1,0}$. The real form $H(u)$ of the complex Hessian $\mathcal{H}$ is given by the polarization of the real quadratic form
$$H(u)(X, Y):=\operatorname{Re} \mathcal{H}(u)(X-\sqrt{-1} J X, Y-\sqrt{-1} J Y),$$
where $X, Y \in T M$. Of course, it is enough to define the quadratic form
$$H(u)(X, X):=\operatorname{Re} \mathcal{H}(u)(X-\sqrt{-1} J X, X-\sqrt{-1} J X)$$
for all real vector fields $X$ and it is a real-valued form. By a simple calculation ( [37, Lemma 4.1]), we can obtain that $H(u)$ is given by
$$H(u)(X, X)=\{X X+(J X)(J X)+J([X, J X])\} u$$
defined for all $X \in T M$ (see [37, Lemma 4.1]).
Definition A.2. (cf. Harvey-Lawson [37]) A smooth function $u$ on $(M, J)$ is called $J$ -plurisubharmonic if $H_{x}(u) \geq 0$ for each $x \in M$.

This notion extends directly to the space of distributions by requiring $\sqrt{-1} \partial_{J} \bar{\partial}_{J} u$ to be positive. The definition of $J$-plurisubharmonic function could be broadened to the space of upper semi-continuous functions on $M$ takinng values in $[-\infty, \infty)$. Denote by USC(M) the space of upper semi-continuous functions on $M$. A function $\varphi$ which is $C^{2}$ in a neighborhood of $x \in M$ is called a test function for $u \in \operatorname{USC}(\mathrm{M})$ at $x$ if $u-\varphi \leq 0$ near $x$ and $u=\varphi$ at $x$. A function $u \in \operatorname{USC}(\mathrm{M})$ is called $J$-plurisubharmonic on $M$ if for each $x \in M$ and each test function $\varphi$ for $u$ at $x$ we have $H_{x}(\varphi) \geq 0$. On the other hand, an upper semi-continuous function $u$ on $(M, J)$ is said to be $J$-plurisubharmonic in the standard sense if its restriction to each $J$-holomorphic curve in $(M, J)$ is subharmonic (for detials, see [37,63]). If the function $u$ is of class $C^{2}$, there is a simple characterization. For any tangent vector field $X \in T M$ one must have
$$d d_{J}^{c} u(X, J X) \geq 0,$$
where the twisted exterior differential $d_{J}^{c}=(-1)^{p} J d J$ acting on $p$-forms, in particular $d_{J}^{c} u(X)=-d u(J X)$. We say that a function $u$ of class $C^{2}$ is strictly $J$-plurisubharmonic if $d d_{J}^{c} u(X, J X)>0$. The manifold $(M, J)$ is said to be (strictly) $J$-pseudoconvex if it admits a smooth exhaustion function $\phi: M \rightarrow \mathbb{R}$ which is (strictly) $J$-plurisubharmonic. If $J=J_{s t}$ is the standard complex structure on $\mathbb{C}^{n}, d_{J_{s t}}^{c}=d^{c}$. Moreover, we have the following integration by parts formula.

Proposition A.3. (cf. Demailly [13, Formula 3.1 in Chapter 3]) Let $(M, J)$ be a closed almost complex $2 n$-manifold and let $\alpha, \beta$ be smooth forms of pure bidegrees $(p, p)$ and $(q, q)$ with $p+q=n-1$. Then
$$\int_{M} \alpha \wedge d d_{J}^{c} \beta-d d_{J}^{c} \alpha \wedge \beta=0$$

Proof. Note that
$$d\left(\alpha \wedge d_{J}^{c} \beta-d_{J}^{c} \alpha \wedge \beta\right)=\alpha \wedge d d_{J}^{c} \beta-d d_{J}^{c} \alpha \wedge \beta+\left(d \alpha \wedge d_{J}^{c} \beta+d_{J}^{c} \alpha \wedge d \beta\right) .$$

Hence, by Stokes' theorem, we get
$$\int_{M} \alpha \wedge d d_{J}^{c} \beta-d d_{J}^{c} \alpha \wedge \beta=-\int_{M} d \alpha \wedge d_{J}^{c} \beta+d_{J}^{c} \alpha \wedge d \beta .$$
As all forms of total degree $2 n$ and bidegree $\neq(n, n)$ are zero, we have
$$d \alpha \wedge d_{J}^{c} \beta=-\sqrt{-1} \cdot\left(\partial_{J} \alpha \wedge \bar{\partial}_{J} \beta-\bar{\partial}_{J} \alpha \wedge \partial_{J} \beta+A_{J} \alpha \wedge \bar{A}_{J} \beta-\bar{A}_{J} \alpha \wedge A_{J} \beta\right)$$
and
$$d_{J}^{c} \alpha \wedge d \beta=\sqrt{-1} \cdot\left(\partial_{J} \alpha \wedge \bar{\partial}_{J} \beta-\bar{\partial}_{J} \alpha \wedge \partial_{J} \beta+A_{J} \alpha \wedge \bar{A}_{J} \beta-\bar{A}_{J} \alpha \wedge A_{J} \beta\right),$$
where $A_{J}$ and $\bar{A}_{J}$ are defined in Section 2 (cf. (2.4)). Therefore, $d \alpha \wedge d_{J}^{c} \beta=-d_{J}^{c} \alpha \wedge d \beta$. \(\square\)

By a simple calculation, we get
$$d d_{J}^{c} u=2 \sqrt{-1} \partial_{J} \bar{\partial}_{J} u+\sqrt{-1}\left(\bar{A}_{J} \bar{\partial}_{J} u-\partial_{J}^{2} u\right)+\sqrt{-1}\left(\bar{\partial}_{J}^{2} u-A_{J} \partial_{J} u\right)$$
and
$$d_{J}^{c} d u=-2 \sqrt{-1} \partial_{J} \bar{\partial}_{J} u+\sqrt{-1}\left(\bar{A}_{J} \bar{\partial}_{J} u-\partial_{J}^{2} u\right)+\sqrt{-1}\left(\bar{\partial}_{J}^{2} u-A_{J} \partial_{J} u\right) .$$
Hence, a $C^{2}$ function $u$ is $J$-plurisubharmonic if and only if the $(1,1)$ part of $d d_{J}^{c} u$ is positive. Harvey and Lawson have proven that the notion of $J$-plurisubharmonic is equivalent to the $J$-plurisubharmonic in the standard sense (cf. Harvey-Lawson [37, Theorem 6.2]). Harvey and Lawson also introduce the notion of Hermitian plurisubharmonic on an almost Hermitian manifold $(M, g, J)$. Denote the Riemannian Hessian operator by
$$(\operatorname{Hess} u)(X, Y):=X Y u-\left(\nabla_{X} Y\right) u$$
for $X, Y \in T M$, where ∇ is the Levi-Civita connection. A function $u \in C^{\infty}(M)$ is then defined to be Hermitian plurisubharmonic if $\operatorname{Hess}^{\mathrm{C}} u \geq 0$, where
$$\left(\operatorname{Hess}^{\mathrm{C}} u\right)(X, Y):=(\operatorname{Hess} u)(X, Y)+(\operatorname{Hess} u)(J X, J Y) .$$
In general, Hermitian plurisubharmonic does not agree with the standard $J$-plurisubharmonic (cf. Harvey-Lawson [37, Section 9]). But we have the following proposition proved by Harvey and Lawson:

Proposition A.4. (cf. Harvey-Lawson [37, Theorem 9.1]) Let $(M, g, J)$ be an almost Hermitian manifold. If the associated Kähler form $\omega(\cdot, \cdot)=g(J \cdot, \cdot)$ is closed, that is, $(M, g, J, \omega)$ is almost Kähler, then the notion of Hermitian plurisubharmonic coincides with the notion of $J$-plurisubharmonic.

Let $(M, g, J, \omega)$ be an almost Kähler manifold of (complex) dimension $n$. For any $p \in M$, assume $T_{p} M \cong \mathbb{C}^{n}$. Let
$$B_{1}\left(p, \varepsilon_{1}\right):=\left\{\xi \in T_{p} M| | \xi \mid \leq \varepsilon_{1}\right\}$$
and
$$S_{1}\left(p, \varepsilon_{1}\right):=\left\{\xi \in T_{p} M| | \xi \mid=\varepsilon_{1}\right\} .$$
Suppose that $\rho_{g}(p, q)$ is the geodesic distance of points $p, q$ with respect to $g$ (for details, see Chavel [9]). Denote by
$$B\left(p, \varepsilon_{1}\right):=\left\{q \in M \mid \rho_{g}(p, q) \leq \varepsilon_{1}\right\}$$
and
$$S\left(p, \varepsilon_{1}\right):=\left\{q \in M \mid \rho_{g}(p, q)=\varepsilon_{1}\right\} .$$

It is well known that for each $p \in M$, there exists $\varepsilon_{2}>0$ and a neighborhood $U$ of $p$ in $M$ such that for each $q \in U, \exp _{q}$ maps $B_{1}\left(p, \varepsilon_{2}\right)$ diffeomorphically onto an open set in $M$. Hence, for $\varepsilon_{1}<\varepsilon_{2}$, we have
$$B\left(p, \varepsilon_{1}\right)=\exp B_{1}\left(p, \varepsilon_{1}\right)$$
and
$$S\left(p, \varepsilon_{1}\right)=\exp S_{1}\left(p, \varepsilon_{1}\right) .$$
Let $i n j M$ be the injectivity radius of $M$ (for the detailed definition, we refer to Chavel [9, Chapter III]).

Proposition A.5. (cf. Chavel [9, Theorem IX.6.1]) Let $(M, g, J, \omega)$ be an almost Kähler manifold. Assume that the sectional curvature $K \leq \delta$ on $M$. Set $r=\min \left\{\frac{i n j M}{2}, \frac{\pi}{2 \sqrt{\delta}}\right\}$, then $B(p, r)$ is strictly convex.

Therefore, on an almost Kähler manifold with bounded geometry (cf. [9]), a small geodesic ball is strictly convex. It is well known that one of the fundamental results of classical complex analysis establishes the equivalence between the holomorphic disc convexity of a domain in an affine complex space, the Levi convexity of its boundary and existence of a strictly plurisubharmonic exhaustion function. On the other hand, in the works of K. Diederich-A. Sukhov, Y. Eliashberg-M. Gromov, F.R. Harvey-H.B. Lawson, Jr [14, 22, 35, 36] and other authors, the convexity properties of strictly $J$-pseudoconvex domains in almost complex manifolds are substantially used give rise to many interesting results. Concerning symplectic structure, K. Diederich and A. Sukhov [14, Theorem 5.4] obtained a characterization of $J$-pseudoconvex domain in almost complex manifolds similar to the classical results of complex analysis. Hence fix a point $p, \rho_{g}(p, q)$ is a strictly subharmonic function on $\left\{q \mid \rho_{g}(p, q)<r\right\}$.

Claim A.6. Let $(M, g, J, \omega)$ be an almost Kähler manifold of (complex) dimension $n$. For any $p \in M, \log \rho_{g}(p, q)$ is $J$-plurisubharmonic if $\rho_{g}(p, q)$ is small enough.

We will prove the above claim later. Note that when we identify $\mathbb{R}^{2 n}$ with $\mathbb{C}^{n}$. Chirka (unpublished) observed that if the almost complex structure $J$ defined in a neighborhood of 0 coincides with the standard complex structure at 0, then for $A>0$ large enough the function $z \rightarrow \log |z|+A|z|$ is $J$-plurisubharmonic near 0, with $z=\left(z_{1}, \cdots, z_{n}\right)$ and $|z|=\left(\left|z_{1}\right|^{2}+\cdots+\left|z_{n}\right|^{2}\right)^{\frac{1}{2}}$. One should of course not expect the function $\log |z|$ to be $J$-plurisubharmonic, since it is not strictly plurisubharmonic for the standard complex structure, and hence even a small change of complex structure will not preserve plurisubharmonicity. The term $A|z|$ is a needed correction term. The computation is made in detail in Ivashkovich-Rosay [41, Lemma 1.4]. Note that $J$-holomorphic curves are $-\infty$ sets of $J$-plurisubharmonic functions, with a singularity of log log type (cf. Rosay [65]), but it is shown that in general they are not $-\infty$ set of $J$-plurisubharmonic functions with logarithmic singularity (cf. Rosay [66]).

Suppose that $(M, g, J)$ is an almost Hermitian $2 n$-manifold. Let $\nabla^{1}$ be the second canonical connection satisfying $\nabla^{1} g=0$ and $\nabla^{1} J=0$ [28]. There exists a unique second canonical connection on almost Hermitian manifold $(M, g, J)$ whose torsion has everywhere
vanishing $(1,1)$ part (cf. [28,77]). This connection was first introduced by Ehresmann and Libermann (cf. [21]). It is also sometimes referred to as the Chern connection, since when $J$ is integrable it coincides with the connection defined in [10]. Choose a local unitary frame $\left\{e_{1}, \cdots, e_{n}\right\}$ for $T M^{1,0}$ with respect to the Hermitian inner product $h=g-\sqrt{-1} \omega$, where $\omega(\cdot, \cdot)=g(J \cdot, \cdot)$, and let $\left\{\theta^{1}, \cdots, \theta^{n}\right\}$ be a dual coframe. The metric $h$ can be written as
$$h=\theta^{i} \otimes \overline{\theta^{i}}+\overline{\theta^{i}} \otimes \theta^{i} .$$
Let $\Theta$ be the torsion of the canonical almost Hermitian connection $\nabla^{1}$. Define functions $N_{\bar{j} \bar{k}}^{i}$ and $T_{j k}^{i}$ (cf. [77]) by
$$\begin{aligned}
\left(\Theta^{i}\right)^{(0,2)} & =N_{\bar{j} \bar{k}}^{i} \overline{\theta^{j}} \wedge \overline{\theta^{k}}, \\
\left(\Theta^{i}\right)^{(2,0)} & =T_{j k}^{i} \theta^{j} \wedge \theta^{k}
\end{aligned}$$
with $N_{\bar{j} \bar{k}}^{i}=-N_{\bar{k} j}^{i}$ and $T_{j k}^{i}=-T_{k j}^{i}$.
It is not hard to obtain the following lemma:
Lemma A.7. (cf. [27, 77, 79]) The $(0,2)$ part of the torsion is independent of the choice of metric.

Consider the real $(1,1)$ form $\omega(\cdot, \cdot)=g(J \cdot, \cdot)$,
$$\omega=\sqrt{-1} \sum_{i=1}^{n} \theta^{i} \wedge \overline{\theta^{i}} .$$
We say that $(M, J, g, \omega)$ is almost Kähler if $d \omega=0$, and it is quasi Kähler if $(d \omega)^{(1,2)}=0$. An almost Kähler or quasi Kähler manifold with $J$ integrable is a Kähler manifold.

Lemma A.8. (cf. [27,77]) An almost Hermitian manifold ( $M, g, J, \omega$ ) is almost Kähler if and only if
$$T_{k j}^{i}=0$$
and
$$N_{\bar{i} \bar{j} \bar{k}}+N_{\bar{j} \bar{k} \bar{i}}+N_{\bar{k} i \bar{j}}=0,$$
where $N_{\bar{i} \bar{j} \bar{k}}=N_{\bar{j} \bar{k}}^{i} .(M, g, J, \omega)$ is quasi Kähler if and only if
$$T_{k j}^{i}=0 .$$

Notice that if $(M, g, J, \omega)$ is almost Kähler, then $(M, g, J, \omega)$ is quasi Kähler.
Let $f$ be a smooth function on $M$. We define the canonical Laplacian $\Delta^{1}$ of $f$ by
$$\Delta^{1} f=\sum_{i}\left(\nabla^{1} \nabla^{1} f\left(e_{i}, \bar{e}_{i}\right)+\nabla^{1} \nabla^{1} f\left(\bar{e}_{i}, e_{i}\right)\right) .$$
This expression is independent of the choice of unitary frame. By Lemma 2.5 in [77],
$$\Delta^{1} f=\sqrt{-1} \sum_{i}\left(d d_{J}^{c} f\right)^{(1,1)}\left(e_{i}, \bar{e}_{i}\right) .$$

Lemma A.9. (cf. [27,[77]) If the metric $g$ is quasi-Kähler then the canonical Laplacian $\Delta^{1}$ is equal to the usual Laplacian, $\Delta_{g}$, of the Levi-Civita connection of $g$.

Let us return to the proof of the above claim.
Proof of Claim A. 6 To verity that $\log \rho_{g}(p, q)$ is $J$-plurisubharmonic on almost Kähler manifold $(M, g, J, \omega)$, we introduce geodesic spherical coordinates about $p$ by defining
$$V:[0, \varepsilon) \times T_{p} M \longrightarrow M$$
by $V(s, X)=\exp s X$. For any $\xi \in S_{p}=S_{1}(p, 1)$, denote by
$$\xi^{\perp}:=\left\{\eta \in T_{p} M \mid\langle\eta, \xi\rangle=0\right\} .$$
Then the map $\eta \mapsto s F \eta$ is an isomorphism of $\xi^{\perp}$ onto $S_{1}(p, s)_{s \xi}$, where $F: T_{p} M \rightarrow\left(T_{p} M\right)_{s \xi}$ is the canonical isomorphism. Hence for any point $q^{\prime}$ which lies in a small neighborhood of $p, q^{\prime}$ could be written as
$$q^{\prime}=\exp s\left(\xi+\sum_{i=1}^{2 n-1} \theta_{i} e_{i}\right),$$
where $e_{1}, \cdots, e_{2 n-1}, \xi=e_{2 n} \in T_{p} M$ is a local unitary orthogonal frame, and $J e_{2 i-1}=e_{2 i}$, $1 \leq i \leq n$. Therefore,
$$\rho_{g}\left(p, q^{\prime}\right)=\sqrt{s^{2}\left(1+\sum_{i=1}^{2 n-1} \theta_{i}^{2}\right)} .$$
Hence, when $s=t, \theta_{i}=0, i=1,2, \cdots, 2 n-1$
$$\begin{aligned}
\left.\Delta_{g} \log \rho_{g}\left(p, q^{\prime}\right)\right|_{q} & =\left.\frac{1}{2}\left(\frac{\partial^{2}}{\partial s^{2}}+\frac{1}{t^{2}} \sum_{i=1}^{2 n-1} \frac{\partial^{2}}{\partial \theta_{i}^{2}}\right) \log s^{2}\left(1+\sum_{i=1}^{2 n-1} \theta_{i}^{2}\right)\right|_{s=t, \theta_{i}=0} \\
& =-\frac{1}{t^{2}}+\sum_{i=1}^{2 n-1} \frac{1}{t^{2}}=\frac{2 n-2}{t^{2}} .
\end{aligned}$$
Since we mainly consider it on almost Kähler $2 n$-manifold, especially, on almost Kähler 4 -manifold, $\Delta_{g} \log \rho_{g}(p, q) \geq 0$. By Lemma A.9, notice that an almost Kähler manifold is a quasi Kähler manifold, we have
$$\Delta^{1} \log \rho_{g}(p, q)=\Delta_{g} \log \rho_{g}(p, q) \geq 0 .$$
Define $l_{j}$ to be the $J$-holomorphic curves spanned by $\left\{e_{2 j-1}, J e_{2 j-1}\right\}, 1 \leq j \leq n$. Then, we have
$$\begin{aligned}
\left.\left.\Delta_{g}\right|_{l_{n}} \log \rho_{g}\left(p, q^{\prime}\right)\right|_{q}= & \left.\frac{-1}{s^{2}\left(1+\sum_{i=1}^{2 n-1} \theta_{i}^{2}\right)}\right|_{s=t, \theta_{i}=0} \\
& +\left.\left[\frac{1}{s^{2}\left(1+\sum_{i=1}^{2 n-1} \theta_{i}^{2}\right)}+\frac{-2 \theta_{2 n-1}^{2}}{s^{2}\left(1+\sum_{i=1}^{2 n-1} \theta_{i}^{2}\right)^{2}}\right]\right|_{s=t, \theta_{i}=0} \\
= & -\frac{1}{t^{2}}+\frac{1}{t^{2}}=0
\end{aligned}$$
and
$$\begin{aligned}
\Delta_{g}\left|l_{j} \log \rho_{g}\left(p, q^{\prime}\right)\right|_{q}= & \left.\frac{\left(1+\sum_{i=1}^{2 n-1} \theta_{i}^{2}\right)-2 \theta_{2 j-1}^{2}}{\left(1+\sum_{i=1}^{2 n-1} \theta_{i}^{2}\right)^{2}}\right|_{s=t, \theta_{i}=0} \\
& +\left.\frac{\left(1+\sum_{i=1}^{2 n-1} \theta_{i}^{2}\right)-2 \theta_{2 j}^{2}}{\left(1+\sum_{i=1}^{2 n-1} \theta_{i}^{2}\right)^{2}}\right|_{s=t, \theta_{i}=0} \\
= & \frac{1}{t^{2}}+\frac{1}{t^{2}}=\frac{2}{t^{2}},
\end{aligned}$$
where $1 \leq j \leq n-1$. Hence, for any $J$-holomorphic curve $l=\sum_{j=1}^{n} a_{j} l_{j}$ spanned by $\{X, J X\}$,
$$\begin{aligned}
\left.d d_{J}^{c} \log \rho_{g}\left(p, q^{\prime}\right)(X, J X)\right|_{q} & =\left.\left.\sum_{j=1}^{n} a_{j}^{2} \Delta_{g}\right|_{l_{j}} \log \rho_{g}\left(p, q^{\prime}\right)\right|_{q} \\
& =\frac{2}{t^{2}} \sum_{j=1}^{n-1} a_{j}^{2} \geq 0
\end{aligned}$$
which means that $\log \rho_{g}(p, q)$ is $J$-plurisubharmonic if $\rho_{g}(p, q)<\varepsilon$. This completes the proof of the claim. \(\square\)

In the remainder of this subsection, we will discuss the basic properties of $J$-plurisubharmonic functions on almost Kähler manifolds. In fact, a number of the results established in complex analysis via plurisubharmonic functions have been extended to almost complex manifolds (cf. [35-38, 72]). Let $(M, J)$ be an almost complex manifold and $\operatorname{PSH}(M, J)$ the set of $J$-plurisubharmonic functions on $(M, J)$. We have the following facts (cf. [35-38, 72]):

\section*{Proposition A.10.}
1) Suppose $(M, J)$ is an almost complex manifold which is $J$-pseudoconvex, and let $u \in \operatorname{PSH}(M, J)$ be a $J$-plurisubharmonic function. Then there exists a decreasing sequence $\left\{u_{j}\right\} \subset C^{\infty}(M)$ of smooth strictly $J$-plurisubharmonic functions such that $u_{j}(x) \downarrow u(x)$ at each $x \in M$.
2) (Maximum property) If $u, v \in \operatorname{PSH}(M, J)$, then $w=\max \{u, v\} \in \operatorname{PSH}(M, J)$.
3) (Coherence property) If $u \in \operatorname{PSH}(M, J)$ is twice differentiable at $x \in M$, then Hess ${ }_{x} u$ is positive.
4) Let $u_{1}$ and $u_{2}$ be smooth strictly $J$-plurisubharmonic functions on $(M, J)$. Then for every $\varepsilon>0$ and every relatively compact domain $\Omega \subset M$ there exists a smooth and strictly $J$-plurisubharmonic function $u$ in $\Omega$ such that $\max \left\{u_{1}, u_{2}\right\} \leq u \leq \max \left\{u_{1}, u_{2}\right\}+\varepsilon$ on $\Omega$.
5) If $\psi$ is convex non-decreasing function, then $\psi \circ u \in \operatorname{PSH}(M, J)$ for each $u \in$ $\operatorname{PSH}(M, J)$.
6) (Decreasing sequence property) If $\left\{u_{j}\right\}$ is a decreasing $\left(u_{j} \geq u_{j+1}\right)$ sequence of functions with all $u_{j} \in \operatorname{PSH}(M, J)$, then the limit $u=\lim _{j \rightarrow \infty} u_{j} \in \operatorname{PSH}(M, J)$.
7) (Uniform limit property) Suppose $\left\{u_{j}\right\} \subset \operatorname{PSH}(M, J)$ is a sequence which converges to $u$ uniformly on compact subsets on $M$, then $u \in \operatorname{PSH}(M, J)$.
8) (Families locally bounded above) Suppose $\mathcal{F} \subset \operatorname{PSH}(M, J)$ is a family of functions which are locally uniformly bounded above. Then the upper envelope $v=\sup _{f \in \mathcal{F}} f$ has
upper semi-continuous regularization $v^{*} \in \operatorname{PSH}(M, J)$ and $v^{*}=v$ a.e.. Moreover, there exists a sequence $\left\{u_{j}\right\} \subset \mathcal{F}$ with $v^{j}=\max \left\{u_{1}, \cdots, u_{j}\right\}$ converging to $v^{*}$ in $L_{\text {loc }}^{1}(M)$.

For an almost Kähler 4-manifold, we use Theorem A. 31 for $\widetilde{\mathcal{W}}, d_{J}^{-}$-problem in Appendix A. 3 to establish the following result:

Lemma A.11. Let $(M, g, J, \omega)$ be an almost Kähler 4-manifold, and let $T$ be a strictly positive closed (1, 1)-current on $M$ with $L^{q}$ coefficients for some fixed $q \in(1,2)$. Then, $T$ can be written as $T=d \widetilde{\mathcal{W}}\left(f_{T}\right)$ locally, where $f_{T}$ is in $L_{2}^{q}(M)$ and strictly $J$-plurisubharmonic.

Proof. It is often convenient to work with smooth forms and then prove statements about currents by using an approximation of a given current by smooth forms (cf. [31, 69]). For any point $p \in M$, we choose a neighborhood $U_{p}$ of $p$. We may assume without loss of generality that $U_{p}$ is a star shaped strictly $J$-pseudoconvex open set, by Poincaré Lemma, $T=d A$ on $U_{p}$ since $\left.T\right|_{U_{p}}$ is a strictly positive closed (1, 1)-current. Note that $T$ is $(1,1)$ type, so $d_{J}^{-}(A)=0$. Then applying Theorem A. 31 in Appendix A. 3 ( $\widetilde{\mathcal{W}}, d_{J}^{-}$-problem), there exists a smooth function $f_{T}$ such that $T=d \widetilde{\mathcal{W}}\left(f_{T}\right)$ on $U_{p}$. Since $(M, g, J, \omega)$ is an almost Kähler 4-manifold, $\widetilde{\mathcal{W}}\left(f_{T}\right)=\mathcal{W}\left(f_{T}\right)$ (see Section 2), hence $T=d \mathcal{W}\left(f_{T}\right)$ locally. When $U_{p}$ is very small, on $U_{p}$ there exists Darboux coordinate chart $\left(z_{1}, z_{2}\right)$ (cf. [2,60]) with standard complex structure $J_{0}=J(p)$. Since $d \mathcal{W}\left(f_{T}\right)=\mathcal{D}_{J}^{+}\left(f_{T}\right)$ is smooth and strictly positive (1,1)-form, $\mathcal{D}_{J}^{+}\left(f_{T}\right)$ can be regarded as a local symplectic form on $U_{p}$. Hence, the complex coordinate $\left(z_{1}, z_{2}\right)$ is also Darboux coordinate on $U_{p}$ for $\mathcal{D}_{J}^{+}\left(f_{T}\right)$, that is, $\mathcal{D}_{J}^{+}\left(f_{T}\right)$ are $J$ and $J_{0}(=J(p))$ compatible. Hence $\mathcal{D}_{J}^{+}\left(f_{T}\right)=2 \sqrt{-1} \partial_{J(p)} \bar{\partial}_{J(p)} f_{T}$, i.e., $f_{T}=\left|z_{1}\right|^{2}+\left|z_{2}\right|^{2}$. It is easy to see that $\sqrt{-1} \partial_{J} \bar{\partial}_{J} f_{T}>0$ on $U_{p}$. Therefore $f_{T}$ is also strictly $J$-plurisubharmonic. By Proposition A.10, when $f_{T} \in L_{2}^{q}\left(U_{p}\right)$ for some fixed $q \in(1,2)$, the above conclusion also holds since there exists a sequence $\left\{f_{T, k}\right\}$ of smooth $J$-plurisubharmonic functions on $U_{p}$ such that $f_{T, k}$ converges to $f_{T}$ in norm $L_{2}^{q}$. This completes the proof of Lemma A.11. \(\square\)

In classical complex analysis case, we have Poincaré-Lelong equation ( [31]). If the holomorphic function $f$ has divisor the analytic hypersurface $Z$, then the equation of currents
$$\frac{\sqrt{-1}}{2 \pi} \partial \bar{\partial} \log |f|^{2}=T_{Z}$$
is valid. In [24], Elkhadhra extended Poincaré-Lelong equation to the almost complex category. Let $\Omega$ be an open set of $\mathbb{R}^{2 n}$ equipped with an almost complex structure $J$. Given a submanifold $Z$ of $\Omega$ of codimension $2 p$ if $J(T Z)=T Z$, that is, $T Z$ is $J$-invariant, then $J$ is also an almost complex structure on $T Z$, it means that $Z$ is an almost complex submanifold of dimension $2 n-2 p$. Let $U$ be an open subset of $\Omega$ such that $Z$ is defined on $U$ by $f_{i}=0,1 \leq i \leq p$, where the $f_{i}$ are of smooth functions on $U, \bar{\partial}_{J} f_{i}=0$ on $Z \cap U$ and $\partial_{J} f_{1} \wedge \cdots \wedge \partial_{J} f_{p} \neq 0$ on $U$. With these notations, Elkhadhra obtained a generalized Poincaré-Lelong formula:
$$\left(\frac{\sqrt{-1}}{2 \pi} \partial_{J} \bar{\partial}_{J} \log |f|^{2}\right)^{p}=T_{Z}+R_{J}(f),$$
where $f=\left(f_{i}\right)_{1 \leq i \leq p},|f|^{2}=\sum_{i=1}^{p}\left|f_{i}\right|^{2}$ and $R_{J}(f)$ is a $(p, p)$-current which has $L_{\text {loc }}^{\alpha}$ integrable as coefficients, $\alpha<1+\frac{1}{2 p-1}$. Moreover, $R_{J}(f)=0$ when the structure $J$ is integrable. Our Lemma A. 11 can be viewed as a generalized Poincaré-Lelong equation of closed positive (1, 1)-currents on almost Kähler 4-manifold.

\section*{A. 2 Kiselman's minimal principle for $J$-plurisubharmonic functions}

This subsection is devoted to studying Kiselman's minimal principle for $J$-plurisubharmonic functions. A linear image of a convex set is convex, but in spite of far reaching analogy between convexity and pseudoconvexity the corresponding result is not true in the complex domain, the projection in $\mathbb{C}^{2}$ of a pseudoconvex set in $\mathbb{C}^{3}$ may fail to be pseudoconvex. C. O. Kiselman [46] exhibited, in classical complex analysis, a class of pseudoconvex sets which admit pseudoconvex projections and studied an associated functional transformation, the partial Legendre transformation. This transformation can be used to study the local behavior of plurisubharmonic functions in classical complex analysis. In this subsection, we use this method to study the local behavior of $J$-plurisubharmonic functions.

Let $\left(\mathbb{R}^{2 n}, \omega_{0}\right)$ be the standard symplectic vector space, where $\omega_{0}=\sum_{i=1}^{n} d x_{i} \wedge d y_{i}$. Here $\left(x_{1}, y_{1}, \cdots, x_{n}, y_{n}\right)$ is the global coordinate of $\mathbb{R}^{2 n}$. As in classical complex analysis [43], we have the following definition.

Definition A.12. (cf. Jarnicki-Pflug [43, Definition 1.1.1]) A pair ( $X, \pi$ ) is called a symplectic Riemann region over the symplectic vector space $\left(\mathbb{R}^{2 n}, \omega_{0}\right)$ if:
\begin{itemize}
\item[(1)] $X$ is a topological Hausdorff space;
\item[(2)] $\pi: X \longrightarrow\left(\mathbb{R}^{2 n}, \omega_{0}\right)$ is a local homeomorphism.
\end{itemize}

Moreover, if $X$ is connected, then we say that $(X, \pi)$ is a symplectic Riemann domain over $\left(\mathbb{R}^{2 n}, \omega_{0}\right)$. The mapping $\pi$ is called the projection. $\forall z \in \pi(X), \pi^{-1}(z)$ is called the stalk over $z$. A subset $A \subset X$ is said to be univalent if $\left.\pi\right|_{A}: A \rightarrow \pi(A)$ is homeomorphic.

Remark A.13. (cf. Jarnicki-Pflug [43]) (1) If we replace $\left(\mathbb{R}^{2 n}, \omega_{0}\right)$ in the above definition by a (connected) $2 n$-dim symplectic manifold $(M, \omega)$, then we get the notion of a Riemann region (domain) over $(M, \omega)$.
(2) $\omega_{0}$ can be pulled back to $X$ so that $\left(X, \omega=\pi^{*} \omega_{0}\right)$ is a symplectic manifold. It is well known that there exists an $\omega$-compatible almost complex structure $J$ on $X$, that is, $\omega(J \cdot, J \cdot)=\omega(\cdot, \cdot)$. Let $g(\cdot, \cdot):=\omega(\cdot, J \cdot)$ be an almost Kähler metric on $X$. Then $(X, g, J, \omega)$ is an almost Kähler manifold (cf. [60]). Let $J_{0}:=J_{s t}$ be the standard complex structure on $\mathbb{R}^{2 n}, g_{0}(\cdot, \cdot):=\omega_{0}\left(\cdot, J_{0} \cdot\right)$, then $\left(\mathbb{R}^{2 n}, g_{0}, J_{0}, \omega_{0}\right)=\mathbb{C}^{n}$.
(3) If $\Omega \subset\left(\mathbb{R}^{2 n}, g_{0}, J_{0}, \omega_{0}\right)$ is a domain, then $\left(\Omega, \omega_{0}\right)$ is a (symplectic) Riemann domain over $\mathbb{C}^{n}$.
(4) If $(X, \pi, \omega)$ is a symplectic Riemann domain over $\left(\mathbb{R}^{2 n}, \omega_{0}\right)$, then $\pi$ is an open mapping. Hence, $\pi(X)$ is a domain over $\left(\mathbb{R}^{2 n}, \omega_{0}\right)$ and the stalk $\pi^{-1}(p)$ is discrete for all $p \in \pi(X)$.
(5) Let $(X, \pi, \omega)$ be a symplectic Riemann domain over $\left(\mathbb{R}^{2 n}, \omega_{0}\right)$, and let $Y$ be a univalent subset such that $\pi(Y)=\pi(X)$, then $Y=X$.
(6) Evidently, not all connected symplectic $2 n$-dimensional manifolds are symplectic Riemann domains, e.g., a compact symplectic manifold cannot be a symplectic Riemann
domain. In the category of non-compact connected symplectc manifolds the situation is as follows: If $n=1$, then any complex (symplectic 2-dimensional) manifold is a symplectic Riemann domain over $\mathbb{C}\left(\left(\mathbb{R}^{2}, \omega_{0}\right)\right)$ with suitable projection $\pi$; If $n \geq 2$, then there exist very regular non-compact connected symplectic manifolds which are not symplectic Riemann domains over $\left(\mathbb{R}^{2 n}, \omega_{0}\right)$.
(7) If $(X, \pi, \omega)$ is a symplectic Riemann domain over $\left(\mathbb{R}^{2}, \omega_{0}\right)$, then $\left(Y,\left.\pi\right|_{Y},\left.\omega\right|_{Y}\right)$ is a symplectic Riemann domain over $\left(\mathbb{R}^{2}, \omega_{0}\right)$ for any domain $Y \subset X$.
(8) If $\left(X, \pi^{1}, \omega^{1}\right)$ and $\left(Y, \pi^{2}, \omega^{2}\right)$ are symplectic Riemann domains over $\left(\mathbb{R}^{2 n}, \omega_{0}^{1}\right)$ and $\left(\mathbb{R}^{2 m}, \omega_{0}^{2}\right)$, respectively, then $\left(X \times Y, \pi^{1} \times \pi^{2}, \omega^{1} \oplus \omega^{2}\right)$ is a symplectic Riemann domain over $\left(\mathbb{R}^{2 n} \times \mathbb{R}^{2 m}, \omega_{0}^{1} \oplus \omega_{0}^{2}\right)$.

Example A.14. (1) Let $\left(\mathbb{R}^{2 n}, \pi=i d_{\mathbb{R}^{2 n}}, \omega_{0}^{1}\right)$ be a symplectic vector space, where
$$\mathbb{R}^{2 n}:=\left\{\left(x_{1}, \cdots, x_{2 n}\right) \mid x_{i} \in \mathbb{R}, 1 \leq i \leq 2 n\right\},$$
$\omega_{0}^{1}=d x_{1} \wedge d x_{2}+\cdots+d x_{2 n-1} \wedge d x_{2 n}$. Suppose $J$ is an $\omega_{0}^{1}$-compatible almost complex structure on $\mathbb{R}^{2 n}$. Let $g_{J}(\cdot, \cdot)=\omega_{0}^{1}(\cdot, J \cdot)$, then $E:=\left(\mathbb{R}^{2 n}, g_{J}, J, \omega_{0}^{1}\right)$ is an almost Kähler manifold and also a topological vector space.
(2) Let $\left(\mathbb{R}^{2 m}, \pi=i d_{\mathbb{R}^{2 m}}, \omega_{0}^{2}\right)$ be a symplectic vector space, where
$$\mathbb{R}^{2 m}=\left\{\left(y_{1}, \cdots, y_{2 m}\right) \mid y_{i} \in \mathbb{R}, 1 \leq i \leq 2 m\right\},$$
$\omega_{0}^{2}=d y_{1} \wedge d y_{2}+\cdots+d y_{2 m-1} \wedge d y_{2 m}$. Let $J_{0}$ be the standard complex structure on $\mathbb{R}^{2 m}$. It is easy to see that $J_{0}$ is $\omega_{0}^{2}$-compatible. Then $\left(\mathbb{R}^{2 m}, J_{0}, \omega_{0}^{2}\right)=\mathbb{C}^{m}=\mathbb{R}^{m}+\sqrt{-1} \mathbb{R}^{m}$.

Definition A.15. A domain $\Omega \subset \mathbb{C}^{n}$ is called a tube domain if $\Omega=\Omega+\sqrt{-1} \mathbb{R}^{n}$.
In classical complex analysis, one has the following theorem (cf. [13, 40, 47]):
Theorem A.16. (1) Let $\Omega \subset \mathbb{C}^{n}$ be a domain, $u$ a $\left(J_{0}\right)$-plurisubharmonic function which is locally indenpendent of the imaginary part of z, i.e., for any $z \in \Omega, u\left(z^{\prime}\right)=u(z)$ if $z^{\prime}$ is sufficientlly close to $z$ and $\operatorname{Re} z^{\prime}=\operatorname{Re} z$. Then $u$ is locally convex in $\Omega$ (thus convex if $\Omega$ is convex).
(2) Any ( $J_{0}$ )-pseudoconvex tube domain $\Omega \subset \mathbb{C}^{n}$ is of the form $\Omega=\Omega_{1}+\sqrt{-1} \mathbb{R}^{n}$, where $\Omega_{1}$ is a convex subdomain of $\mathbb{R}^{n}$.

The main goal of this subsection is to prove a minimum principle for $J$-plurisubharmonic function as in classical complex analysis (cf. Kiselman [46]).

Theorem A.17. (minimal principle for $J$-plurisubharmonic functions)
Let $E=\left(\mathbb{R}^{2 n-2 k}, g_{J}, J, \omega_{0}^{1}\right)$ be an almost Kähler manifold which is also a topological vector space with the induced topology from the metric $g_{J}$. Let $J_{1}:=J \oplus J_{0}$ be an $\omega_{0}^{1} \oplus \omega_{0}^{2}$ - compatible almost complex structure on $\left(\mathbb{R}^{2 n-2 k}, \omega_{0}^{1}\right) \times\left(\mathbb{R}^{2 k}, \omega_{0}^{2}\right)$. Suppose that $\Omega$ is a $J_{1}$-pseudoconvex subdomain of $E \times \mathbb{C}^{k}$ such that for each $x \in E$, the fiber
$$\Omega_{x}:=\left\{z \in \mathbb{C}^{k} \mid(x, z) \in \Omega\right\}$$
is a non-empty connected tube domain. Let $u$ be a $J_{1}$-plurisubharmonic function on $\Omega$. Then the function
$$\begin{aligned}
& f: \pi(\Omega) \rightarrow[-\infty,+\infty), \quad \pi: E \times \mathbb{C}^{k} \rightarrow E \\
& f(x):=\inf \left\{u(x, z) \mid z \in \Omega_{x}\right\}, \quad x \in \pi(\Omega)
\end{aligned}$$
is $J$-plurisubharmonic.
Remark A.18. (1) $\pi(\Omega) \subset E$ is $J$-pseudoconvex (cf. Kiselman [46]).
(2) If the fibres are tubular but not necessarily connected (they must consist of convex components), then the function $f$ is not defined on $E$ but on a symplectic Riemann domain over $\left(\mathbb{R}^{2 n-2 k}, \omega_{0}^{1}\right)$. For more details see [46, Proposition 2.1].

The similar proof as in classical complex analysis we will present here is taken from Kiselman [47] and Jarnicki-Pflug [43]. We need the following technical lemmas:

Lemma A.19. Let $L$ be a positive semidefinite Hermitian $(n \times n)$-matrix. Then there exists a Hermitian $(n \times n)$-matrix $M$ with $L M L=L$.

Proof. There exists $P \in U(n)$ such that
$$P L \bar{P}^{T}=\left(\begin{array}{ccccc}
\lambda_{1} & & & & \\
& \ldots & & & \\
& & \lambda_{m} & & \\
& & & 0 & \\
& & & \ldots & \\
& & & & 0
\end{array}\right)=: \Lambda, m \leq n,$$
since $L$ is a positive semidefinite Hermitian $(n \times n)$-matrix. Let
$$\Lambda^{-}:=\left(\begin{array}{cccccc}
\frac{1}{\lambda_{1}} & & & & & \\
& \cdots & & & & \\
& & \frac{1}{\lambda_{m}} & & & \\
& & & 0 & & \\
& & & & \cdots & \\
& & & & & 0
\end{array}\right),$$
and take $M=\bar{P}^{T} \Lambda^{-} P$, then $L M L=\left(\bar{P}^{T} \Lambda P\right)\left(\bar{P}^{T} \Lambda^{-} P\right)\left(\bar{P}^{T} \Lambda P\right)=L$. \(\square\)

Such matrix $M$ is called a Hermitian quasi-inverse of $L$.
Lemma A.20. Let $F: \mathbb{C}^{n} \rightarrow \mathbb{R}$,
$$F(z):=\sum_{i, j=1}^{n} L_{i j} z_{i} \overline{z_{j}}+2 \operatorname{Re}\left(\sum_{j=1}^{n} b_{j} z_{j}\right)$$
be bounded from below, where $L=\left(L_{i j}\right)_{n \times n}$ is a positive semidefinite Hermitian matrix and $b=\left(b_{1}, \cdots, b_{n}\right) \in \mathbb{C}^{n}$. If $M$ is a Hermitian quasi-inverse of $L$, then $L M b^{T}=b^{T}$ and
$$F(z) \geq-\bar{b} M b^{T}=F\left(-\left(\bar{M} \bar{b}^{T}\right)^{T}\right), z \in \mathbb{C}^{n} .$$

Proof. For a detailed proof of this lemma, we refer to [43, Lemma 2.3.6]. \(\square\)

By using Lemma A.19, A.20, we can prove the following lemma.
Lemma A.21. Let $\Omega$ be a domain in $\mathbb{C}_{z} \times \mathbb{C}_{w}^{n}$ and let $u \in P S H(\Omega) \cap C^{2}(\Omega)$. Moreover, let $M(z, w)$ denote a quasi-inverse of
$$L(z, w)=\left(\frac{\partial^{2} u}{\partial w_{i} \partial \bar{w}_{j}}(z, w)\right)_{1 \leq i, j \leq n},(z, w) \in \Omega .$$
Then $u_{z \bar{z}} \geq \bar{b} M b^{T}$ on $\Omega$, where $b=\left(b_{1}, \cdots, b_{n}\right)=\left(\frac{\partial^{2} u}{\partial \bar{z} \partial w_{1}}, \cdots, \frac{\partial^{2} u}{\partial \bar{z} \partial w_{n}}\right): \Omega \rightarrow \mathbb{C}^{n}$.
Proof. For a detailed proof of this lemma, we refer to [43, Lemma 2.3.7]. \(\square\)

Let $U \subset \mathbb{C}$ be an open set, and let $y: U \rightarrow \mathbb{C}^{n}$ be a $C^{1}$-function such that
$$(z, y(z)) \in \Omega, \quad \frac{\partial u}{\partial w_{j}}(z, y(z))=0, \quad 1 \leq j \leq n, \quad z \in U,$$
where $u$ and $\Omega$ are the same as in the above lemma. Define $g: U \rightarrow \mathbb{R}, g(z):=u(z, y(z))$. Differentiation of $g$ with respect to $z$ and $\bar{z}$ leads to
$$g_{z \bar{z}}(z)=u_{z \bar{z}}(z, y(z))+\sum_{j=1}^{n} u_{z w_{j}}(z, y(z)) y_{j \bar{z}}(z)+\sum_{j=1}^{n} u_{z \bar{w}_{j}}(z, y(z)) \bar{y}_{j \bar{z}}(z) .$$
Since $u_{w_{k}}(z, y(z))=0, k=1, \cdots, n$, we differentiate the equations with respect to $z$ and $\bar{z}$, then
$$0=a_{k}(z, y(z))+\sum_{j=1}^{n} H_{k j}(z) \alpha_{j}(z)+\sum_{j=1}^{n} L_{k j}(z) \bar{\beta}_{j}(z), \quad 1 \leq k \leq n,$$
and
$$0=b_{k}(z, y(z))+\sum_{j=1}^{n} H_{k j}(z) \beta_{j}(z)+\sum_{j=1}^{n} L_{k j}(z) \bar{\alpha}_{j}(z), \quad 1 \leq k \leq n,$$
where
$$\begin{gathered}
\alpha=\left(y_{1 z}, \cdots, y_{n z}\right), \quad \beta=\left(y_{1 \bar{z}}, \cdots, y_{n \bar{z}}\right), \\
a=\left(a_{1}, \cdots, a_{n}\right)=\left(u_{z w_{1}}, \cdots, u_{z w_{n}}\right), \quad b=\left(b_{1}, \cdots, b_{n}\right)=\left(u_{\bar{z} \bar{w}_{1}}, \cdots, u_{\bar{z} \bar{w}_{n}}\right), \\
H(z)=\left(H_{k j}(z)\right)=\left(\frac{\partial^{2} u}{\partial w_{k} \partial w_{j}}(z, y(z)), \quad L(z)=\left(L_{k j}(z)\right)=\left(\frac{\partial^{2} u}{\partial w_{k} \partial \bar{w}_{j}}(z, y(z)), \quad z \in U .\right.\right.
\end{gathered}$$
Summarizing, the following identities hold for $z \in U$ :
$$\begin{aligned}
& a(z, y(z))=-\alpha(z) H(z)-\bar{\beta}(z) L^{T}(z), \\
& b(z, y(z))=-\beta(z) H(z)-\bar{\alpha}(z) L^{T}(z) .
\end{aligned}$$

Proposition A.22. Let $M$ be a matrix-valued function on $U$ such that for all $z \in U$ the matrix $M(z)$ is a Hermitian quasi-inverse of $L(z)$. Then
$$g_{z \bar{z}}(z) \geq\left(\beta\left(H M^{T} \bar{H}-L\right) \bar{\beta}^{T}\right)(z), \quad z \in U .$$
In particular, $g$ is subharmonic on $U$, if the right-hand side of this inequality is never negative on $U$.

Proof. Lemma A. 21 shows $\forall z \in U, u_{z \bar{z}}(z, y(z)) \geq\left(\bar{b} M b^{T}\right)(z, y(z))$ and using $L M b^{T}=b^{T}$,
$$\begin{aligned}
g_{z \bar{z}}(z)= & u_{z \bar{z}}(z, y(z))+a(z, y(z)) \beta(z)+\overline{b(z, y(z)) \alpha(z)} \\
\geq & \bar{b} M b^{T}+a \beta^{T}+\bar{b} \bar{\alpha}^{T} \\
= & \bar{\beta} \bar{H} M H \beta^{T}+\bar{\beta} \bar{H} M L \bar{\alpha}^{T}+\alpha H^{T} \beta^{T}+\alpha H^{T} \beta^{T} \\
& +\alpha L \bar{\alpha}^{T}-\alpha H \beta^{T}-\bar{\beta} L^{T} \beta^{T}-\bar{\beta} \bar{H} \bar{\alpha}^{T}-\alpha \bar{L}^{T} \bar{\alpha}^{T} \\
= & \bar{\beta}\left(\bar{H} M H-L^{T}\right) \beta^{T}+\bar{\beta} \bar{H}\left(M L-I_{n}\right) \bar{\alpha}^{T} \\
= & \beta\left(H M^{T} \bar{H}-L\right) \bar{\beta}^{T}+\left(-\bar{b}-\alpha \bar{L}^{T}\right)\left(M L-I_{n}\right) \bar{\alpha}^{T} \\
= & \beta\left(H M^{T} \bar{H}-L\right) \bar{\beta}^{T} .
\end{aligned}$$ \(\square\)

Corollary A.23. Under the assumptions of the above proposition, moreover, assume that the following properties are fulfilled: if $z \in U$ and $t \in \mathbb{R}^{n}$, then $(z, w+\sqrt{-1} t) \in U$ and $u(z, w)=u(z, w+\sqrt{-1} t)$. Then $g: U \rightarrow \mathbb{R}$ is subharmonic on $U$.

By the above lemmas, proposition and corollary, we return to prove Theorem A.17. Proof of Theorem A.17: Suppose that
$$\left(\mathbb{R}^{2 n-2 k}, g_{J}, J, \omega_{0}^{1}\right) \times\left(\mathbb{R}^{2 k}, g_{J_{0}}, J_{0}, \omega_{0}^{2}\right)=\left(\mathbb{R}^{2 n-2 k}, g_{J}, J, \omega_{0}^{1}\right) \times \mathbb{C}^{k}$$
is an almost Kähler manifold, where $J$ is an $\omega_{0}^{1}$-compatible almost complex structure on $\mathbb{R}^{2 n-2 k}, g_{J}(\cdot, \cdot):=\omega_{0}^{1}(\cdot, J \cdot), J_{0}=J_{s t}$ is the standard complex structure on $\left(\mathbb{R}^{2 k}, \omega_{0}^{2}\right) \cong \mathbb{C}^{k}$, $g_{J_{0}}(\cdot, \cdot):=\omega_{0}^{2}\left(\cdot, J_{0} \cdot\right)$. Let
$$\Omega \subset\left(\mathbb{R}^{2 n-2 k}, g_{J}, J, \omega_{0}^{1}\right) \times \mathbb{C}^{k}$$
be a $J_{1}$-pseudoconvex domain, where $J_{1}:=J \oplus J_{0}$ is an $\omega_{0}^{1} \oplus \omega_{0}^{2}$-compatible almost complex structure on $\mathbb{R}^{2 n-2 k} \times \mathbb{R}^{2 k}$. Suppose that $u(x, w)$ is a $J_{1}$-plurisubharmonic function on $\Omega$, where
$$(x, w) \in \Omega \subset\left(\mathbb{R}^{2 n-2 k}, g_{J}, J, \omega_{0}^{1}\right) \times \mathbb{C}^{k} .$$
Let
$$\pi:\left(\mathbb{R}^{2 n-2 k}, g_{J}, J, \omega_{0}^{1}\right) \times \mathbb{C}^{k} \rightarrow\left(\mathbb{R}^{2 n-2 k}, g_{J}, J, \omega_{0}^{1}\right), \pi(x, w)=x \in\left(\mathbb{R}^{2 n-2 k}, g_{J}, J, \omega_{0}^{1}\right) .$$
Define a function on $\pi(\Omega)$ as follows: Let
$$\Omega_{x}:=\left\{w \in \mathbb{C}^{k} \mid(x, w) \in \Omega\right\}, g(x):=\inf \left\{u(x, w) \mid w \in \Omega_{x}\right\}, x \in \pi(\Omega) .$$

To complete the proof of Theorem A.17, we must prove that $g: \pi(\Omega) \rightarrow[-\infty,+\infty)$ is a $J$-plurisubharmonic function on $\pi(\Omega)$. It is well know that a $J$-plurisubharmonic function is $J$-plurisubharmonic in the standard sense (cf. [37]), that is, its restriction to each $J$ -holomorphic curve $\Sigma$ in $(\pi(\Omega), J)$ is subharmonic. Hence, without loss of generality, we may assume $k=n-1$, that is,$\Omega \subset\left(\mathbb{R}^{2}, g_{J}, J, \omega_{0}^{1}\right) \times \mathbb{C}^{n-1}$. Note that $\left(\mathbb{R}^{2}, g_{J}, J, \omega_{0}^{1}\right)$ is a Riemann surface (cf. [31]) since $J$ on $\mathbb{R}^{2}$ is integrable. Hence $\Omega \subset\left(\mathbb{R}^{2}, g_{J}, J, \omega_{0}^{1}\right) \times \mathbb{C}^{n-1}$ is a Kähler manifold which is also a Riemann domain over $\mathbb{C}^{n}$ in classical complex analysis. By using Theorem A. 16 and Corollary A.23, similar to the proof of Theorem 2.3.2 in [43], we can prove that $g(x): \pi(\Omega) \rightarrow[-\infty,+\infty)$ is a subharmonic function on $\pi(\Omega)$. For details, we refer to [43, proof of Theorem 2.3.2]. This completes the proof of Theorem A.17, □

\section*{A. 3 Hörmander's $L^{2}$ estimates on tamed almost complex 4-manifolds}

In this subsection, we devote to considering $\widetilde{\mathcal{W}}, d_{J}^{-}$-problem (as $\bar{\partial}$-problem in classical complex analysis, cf. Hörmander [39, 40]). In Stein manifold, the $L^{2}$-method for the $\bar{\partial}$ operator has many applications, for example, using $L^{2}$-method we can prove the theorem of Siu [70] on the Lelong numbers of plurisubharmonic functions (cf. [13]). In this subsection, we extend Hörmander's $L^{2}$ estimates [39, 40] to tamed almost complex 4-manifold.
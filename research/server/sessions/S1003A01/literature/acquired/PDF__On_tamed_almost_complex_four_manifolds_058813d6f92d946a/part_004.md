---
retention_scope: session
part: 4
total_parts: 5
---

[Part 4/5 of: [PDF] On tamed almost complex four manifolds]

Definition B.14. If $p \in \operatorname{Supp} T, T$ is a closed positive $(1,1)$-current on a closed almost complex 4-manifold, we define
$$\nu_{2}\left(q, \omega_{p}, r, T\right)=\frac{2}{r^{2}} \int_{B(q, r)} T \wedge \omega_{p},$$
and
$$\nu_{2}(q, p, T)=\lim _{r \rightarrow 0} \nu_{2}\left(q, \omega_{p}, r, T\right) .$$

Note that
$$\nu_{1}\left(q, \omega_{1}, r, T\right)=\frac{2}{r^{2}} \int_{B(q, r)} T \wedge \omega_{1}=\frac{2}{r^{2}} \int_{B(q, r)} T \wedge F=\frac{2}{r^{2}} \int_{B(q, r)} f_{p} T \wedge \omega_{p},$$
we will get the following comparison theorem:
Theorem B.15. Let $T$ be a closed positive $(1,1)$-current on a closed almost complex 4-manifold tamed by symplectic form $\omega_{1}$. If $p \in$ Supp $T$, then $\nu_{1}(q, T)=f_{p}(q) \nu_{2}(q, p, T)$ for any $q$ which is very close to $p$. Moreover, there exists a constant $c>1$ depending on $\omega_{1}$ such that $c^{-1} \nu_{2}(q, p, T) \leq \nu_{1}(q, T) \leq c \nu_{2}(q, p, T), \forall q \in S u p p T \cap U_{p} \subseteq M$.

Proof. Since $f_{p}$ is smooth on $U_{p}, f_{p}$ can achieve the maximum and minimum values on $\overline{B(q, r)}$. Assume that $M_{r}$ and $m_{r}$ are the maximum and minimum values of $f_{p}$ on $\overline{B(q, r)}$, respectively. Thus,
$$m_{r} \frac{2}{r^{2}} \int_{B(q, r)} T \wedge \omega_{p} \leq \nu_{1}\left(q, \omega_{1}, r, T\right)=\frac{2}{r^{2}} \int_{B(q, r)} f_{p} T \wedge \omega_{p} \leq M_{r} \frac{2}{r^{2}} \int_{B(q, r)} T \wedge \omega_{p} .$$
It is easy to see that $\lim _{r \rightarrow 0} M_{r}=\lim _{r \rightarrow 0} m_{r}=f_{p}(q)$. Taking the limit of both sides of the above inequality, for $q \in \operatorname{Supp} T \cap U_{p}$, we can get
$$f_{p}(q) \nu_{2}(q, p, T) \leq \nu_{1}(q, T) \leq f_{p}(q) \nu_{2}(q, p, T) .$$
Hence, we obtain $\nu_{1}(q, T)=f_{p}(q) \nu_{2}(q, p, T)$, in particular $\nu_{1}(p, T)=\nu_{2}(p, p, T)$, since $f_{p}(p)=1$. Note that $M$ is a closed almost complex 4-manifold which has local symplectic property, so we can find a finite open symplectic covering $\left\{\left(U_{p_{1}}, \omega_{p_{1}}\right), \cdots,\left(U_{p_{k}}, \omega_{p_{k}}\right)\right\}$ of $M$. \(\square\)

Remark B.16. (1) Let $T$ be a closed positive $(n-1, n-1)$-current on a closed almost complex $2 n$-manifold tamed by a symplectic form $\omega$. If $p \in S u p p T$, we define
$$\nu_{1}(p, \omega, r, T)=\frac{2}{r^{2}} \int_{B(p, r)} T \wedge \omega,$$
and $\nu_{1}(p, T)=\lim _{r \rightarrow 0} \nu_{1}(p, \omega, r, T)$.
(2) Let $T$ be a closed positive $(p, p)$-current on a closed almost Kähler $2 n$-manifold $(M, g, J, \omega)$. If $q \in$ Supp $T$, we define
$$\nu(q, \omega, r, T)=\frac{2}{r^{2 n-2 p}} \int_{B(q, r)} T \wedge \omega^{n-p}$$
and $\nu(q, T)=\lim _{r \rightarrow 0} \nu(q, \omega, r, T)$.

\section*{B. 2 Siu's decomposition formula of closed positive (1,1)-currents on tamed almost complex 4-manifolds}
T. Rivière and G. Tian [64] have obtained a very important result on the singular set of $(1,1)$ integral currents on almost complex manifolds with the local symplectic property. The regularity question for almost complex cycles is embedded into the problem of calibrated current and hence the theory of area-minimizing rectifiable 2-cycles. Their result appears to be a consequence of the "Big Regularity Paper" of F. Almgren [1] combined with the Ph.D thesis of his student S. Chang [8]. This subsection is devoted to considering regularity of closed (1, 1)-currents on tamed closed almost complex 4-manifolds. It is natural to generalize Siu's semicontinuity theorem [70] of closed positive (1,1)-currents on almost complex manifolds with local symplectic property. Note that any almost complex 4-manifold $(M, J)$ has the local symplectic property [54] and the concepts we are gonging to study mostly concern the behaviour of currents or $J$-plurisubharmonic function in a neighbordhood of a point on an almost complex 4-manifold $(M, J)$, we may assume that $(M, g, J, \omega)$ is an almost Kähler 4-manifold throughout this section. Moreover, without loss of generality, we may assume that $M$ is an open subset of $\mathbb{C}^{2}$. Suppose that $\nu_{1}(p, T)$ is the Lelong number defined on the closed almost Hermitian 4-manifold $\left(M, g_{J}, J, F\right)$ tamed by a symplectic form $\omega_{1}=F+d_{J}^{-}(v+\bar{v})$, where $v \in \Omega_{J}^{1,0}$. Since Lelong number is locally defined, we first consider properties of Lelong number on an open almost Kähler 4-manifold.

Lemma B.17. (cf. Demailly [13, The first and second steps of the proof of Theorem 8.4 in Chapter 3]) If $T$ is a closed positive current of bidimension $(1,1)$ on an open almost Kähler 4-manifold $(M, g, J, \omega)$, the upperlevel sets
$$E_{c}(T)=\{p \in M \mid \nu(p, T) \geq c\}$$
of the usual Lelong number are complete $J$-pluripolar subsets of $M$.
Proof. Suppose $(M, g, J, \omega)$ is an open almost Kähler 4-manifold, where $M \subset \subset \mathbb{C}^{2}$. Let $\varphi(x, y)=\log \rho_{g}(x, y): M \times M \rightarrow[-\infty,+\infty)$ be a continuous $J$-plurisubharmonic function (see Claim A.6), where $\rho_{g}(x, y)$ is the geodesic distance of points $x, y$ with respect to $g$. Let $\chi \in C^{\infty}(\mathbb{R}, \mathbb{R})$ be an increasing function such that $\chi(t)=t$ for $t \leq-1$ and $\chi(t)=0$ for $t \geq 0$. We consider the half-plane $H=\{z \in \mathbb{C} \mid \operatorname{Re} z<-1\}$ and associate with $T$ the potential function $V$ on $M \times H$ defined by
$$V(y, z)=-\int_{\operatorname{Re} z}^{0} \nu\left(\varphi_{y}, t, T\right) \chi^{\prime}(t) d t$$

For every $t>\operatorname{Re} z$, Stokes' formula gives
$$\nu\left(\varphi_{y}, t, T\right)=\int_{\varphi(x, y)<t} T(x) \wedge d d_{J, x}^{c} \tilde{\varphi}(x, y, z)$$
with
$$\tilde{\varphi}(x, y, z):=\max \{\varphi(x, y) \mid \operatorname{Re} z\} .$$
By Fubini theorem, we obtain
$$\begin{aligned}
V(y, z) & =-\int_{x \in M, \varphi(x, y)<t, \operatorname{Re} z<t<0} T(x) \wedge\left(d d_{J, x}^{c} \tilde{\varphi}(x, y, z)\right) \chi^{\prime}(t) d t \\
& =\int_{x \in M} T(x) \wedge \chi(\tilde{\varphi}(x, y, z)) d d_{J, x}^{c} \tilde{\varphi}(x, y, z)
\end{aligned}$$
where $d d_{J, x}^{c} \tilde{\varphi}(x, y, z)=d J(x) d \tilde{\varphi}(x, y, z)$. For any smooth (2, 2)-form $\alpha$ with compact support in $M \times H$, by Proposition A.3, we get
$$\begin{aligned}
<d d_{J}^{c} V, \alpha> & =<V, d_{J}^{c} d \alpha> \\
& =\int_{M \times M \times H} T(x) \wedge \chi(\tilde{\varphi}(x, y, z)) d d_{J}^{c} \tilde{\varphi}(x, y, z) \wedge d_{J}^{c} d \alpha(y, z) \\
& =-\int_{M \times M \times H} T(x) \wedge \chi(\tilde{\varphi}(x, y, z)) d d_{J}^{c} \tilde{\varphi}(x, y, z) \wedge d d_{J}^{c} \alpha(y, z) \\
& =-\int_{M \times M \times H} d d_{J}^{c}\left[T(x) \wedge \chi(\tilde{\varphi}(x, y, z)) \wedge d d_{J}^{c} \tilde{\varphi}(x, y, z)\right] \wedge \alpha(y, z) \\
& =\int_{M \times M \times H} T(x) \wedge d d_{J}^{c} \chi(\tilde{\varphi}(x, y, z)) \wedge d d_{J}^{c} \tilde{\varphi}(x, y, z) \wedge \alpha(y, z) .
\end{aligned}$$
Observe that the replacement of $d d_{J, x}^{c}$ by the total differentiation $d d_{J}^{c}$ does not modify the integrand, because the terms in $d x, d \bar{x}$ must have total bidegree. On $\{-1 \leq \varphi(x, y) \leq 0\}$ we have $\tilde{\varphi}(x, y, z)=\varphi(x, y)$, whereas for $\varphi(x, y)<-1$ we get $\tilde{\varphi}<-1$ and $\chi(\tilde{\varphi})=\tilde{\varphi}$. We see that $d d_{J}^{c} V(y, z)$ is the sum of (1,1)-form
$$\int_{\{x \in M \mid-1 \leq \varphi(x, y) \leq 0\}} T \wedge d d_{J}^{c}(\chi \circ \varphi) \wedge\left(d d_{J}^{c} \varphi\right),$$
and
$$\int_{\{x \in M \mid \varphi(x, y)<-1\}} T \wedge\left(d d_{J}^{c} \tilde{\varphi}\right)^{2} .$$
As $\varphi$ is smooth outside $\varphi^{-1}(-\infty)$, this form (B.6) has locally bounded coefficients. Hence $d d_{J}^{c} V(y, z) \geq 0$ except perhaps for locally bounded terms. In addition, $V$ is continuous on $M \times H$ because $T \wedge\left(d d_{J}^{c} \tilde{\varphi}\right)^{2}$ is weakly continuous in the variables $(y, z)$ by Corollary 3.6 in [13]. Therefore, there exists a positive $J$-plurisubharmonic function $\rho \in C^{\infty}(M)$ such that $\rho(y)+V(y, z)$ is $J$-plurisubharmonic on $M \times H$. If we let $\operatorname{Re} z$ tend to $-\infty$, we see that the function
$$U_{0}(y)=\rho(y)+V(y,-\infty)=\rho(y)-\int_{-\infty}^{0} \nu\left(\varphi_{y}, t, T\right) \chi^{\prime}(t) d t$$
is locally $J$-plurisubharmonic or identically $-\infty$ on $M$. Moreover, it is clear that $U_{0}(y)=$ $-\infty$ at every point $y$ such that $\nu\left(\varphi_{y}, T\right)>0$. If $M$ is connected and $U_{0} \not \equiv-\infty$, we already conclude that the density set $\cup_{c>0} E_{c}$ is pluripolar in $M$.

Let $a \geq 0$ be arbitrary. The function $\rho(y)+V(y, z)-a \operatorname{Re} z$ is $J$-plurisubharmonic and independent of $\operatorname{Im} z$. By Kiselman's minimal principle [46] which also holds on almost Kähler manifolds (see Theorem A. 17 in Appendix A.2), the partial Legendre transform
$$U_{a}(y):=\inf _{r<-1}\{\rho(y)+V(y, r)-a r\}$$
is locally $J$-plurisubharmonic or $\equiv-\infty$ on $M$. Let $y_{0} \in M$ be a given point. We claim that:
\begin{itemize}
\item[(a)] If $a>\nu\left(\varphi_{y_{0}}, T\right)$, then $U_{a}$ is bounded below on a neighborhood of $y_{0}$.
\item[(b)] If $a<\nu\left(\varphi_{y_{0}}, T\right)$, then $U_{a}\left(y_{0}\right)=-\infty$.
\end{itemize}

By the definition of $V$ we have
$$V(y, r) \leq-\nu\left(\varphi_{y}, r, T\right) \int_{r}^{0} \chi^{\prime}(t) d t=r \nu\left(\varphi_{y}, r, T\right) \leq r \nu\left(\varphi_{y}, T\right)$$
Then clearly $U_{a}\left(y_{0}\right)=-\infty$ if $a<\nu\left(\varphi_{y_{0}}, T\right)$. On the other hand, if $a>\nu\left(\varphi_{y_{0}}, T\right)$, there exists $t_{0}<0$ such that $\nu\left(\varphi_{y_{0}}, t_{0}, T\right)<a$. Fix $r_{0}<t_{0}$. The semi-continuity property (Demailly [13, Proposition 5.13]) shows that there exists a neighborhood $\varpi$ of $y_{0}$ such that $\sup _{y \in \varpi} \nu\left(\varphi_{y}, r_{0}, T\right)<a$. For all $y \in \varpi$, we get
$$V(y, r) \geq-C-a \int_{r}^{0} \chi^{\prime}(t) d t=-C+a\left(r-r_{0}\right),$$
and this implies $U_{a}(y) \geq-C-a r_{0}$. We complete the proof of the claim above.
Now return to the proof of Lemma B.17. Note that the family $\left\{U_{a}\right\}$ is increasing in $a$, that $U_{a}=-\infty$ on $E_{c}$ for all $a<c$ and that $\sup _{a<c} U_{a}(y)>-\infty$ if $y \in M \backslash E_{c}$ (apply the above claim). For any integer $k \geq 1$, let $f_{k} \in C^{\infty}(M)$ be a $J$-plurisubharmonic regularization of $U_{c-\frac{1}{k}}$ such that $f_{k} \geq U_{c-\frac{1}{k}}$ on $M$ and $f_{k} \leq-2^{k}$ on $E_{c} \cap M_{k}$ where
$$M_{k}=\left\{y \in M \left\lvert\, d_{g_{J}}(y, \partial M) \geq \frac{1}{k}\right.\right\} .$$
Then the above claim shows that the family $\left(f_{k}\right)$ is uniformly bounded below on every compact subset of $M \backslash E_{c}$. We can also choose $\left(f_{k}\right)$ uniformly bounded above on every compact subset of $M$ because $U_{c-\frac{1}{k}} \leq U_{c}$. The function
$$f=\sum_{k=1}^{+\infty} 2^{-k} f_{k}$$
is a continuous $J$-plurisubharmonic function $f: M \rightarrow[-\infty,+\infty)$ such that
$$E_{c}=f^{-1}(-\infty) .$$
Hence $E_{c}$ is a complete $J$-pluripolar subset of $M$ and has zero Lebesgue measure. \(\square\)

To prove the $J$-analyticity of $E_{c}$, we need the following estimation
Lemma B.18. (cf. Demailly [13, The third step of the proof of Theorem 8.4 in Chapter 3]) Let $y_{0} \in M$ be a given point, $L$ a compact neighborhood of $y_{0}, K \subset M$ a compact subset and $r_{0}$ a real number < -1 such that
$$\left\{(x, y) \in M \times L \mid \varphi(x, y) \leq r_{0}\right\} \subset K \times L,$$
where
$$\varphi(x, y)=\log \rho_{g}(x, y): M \times M \rightarrow[-\infty,+\infty)$$
is a continuous $J$-plurisubharmonic function. Assume that $e^{\varphi(x, y)}$ is locally Hölder continuous in $y$ and that
$$\left|e^{\varphi\left(x, y_{1}\right)}-e^{\varphi\left(x, y_{2}\right)}\right| \leq C \rho_{g}\left(y_{1}, y_{2}\right)^{\gamma}$$
for all $\left(x, y_{1}, y_{2}\right) \in K \times L \times L$. Then for all $\varepsilon \in(0,1)$, there exists a real number $\eta(\varepsilon)>0$ such that all $y \in M$ with $\rho_{g}\left(y, y_{0}\right)<\eta(\varepsilon)$ satisfy
$$U_{a}(y) \leq \rho(y)+\left((1-\varepsilon) \nu\left(\varphi_{y_{0}}, T\right)-a\right)\left(\gamma \log \rho_{g}\left(y, y_{0}\right)+\log \frac{2 e C}{\varepsilon}\right) .$$
Proof. For a detailed proof of this lemma, we refer to Demailly [13, The third step of the proof of Theorem 8.4 in Chapter 3]. \(\square\)

By Lemma B.18, B.17, as in classical complex analysis, we have the following theorem:
Theorem B.19. (cf. Demailly [13, Theorem 8.4 and Corollary 8.5 in Chapter 3]) If $T$ is a closed positive current of bidimension $(1,1)$ on an almost Kähler 4-manifold $(M, g, J, \omega)$, the upperlevel sets
$$E_{c}(T)=\{p \in M \mid \nu(p, T) \geq c\}$$
of the usual Lelong number are $J$-analytic subsets of dimension $\leq 1$.
Proof. For $a, b>0$, we let $Z_{a, b}$ be the set of points in a neighborhood of which $e^{-U_{a} / b}$ is not integrable. Then $Z_{a, b}$ is $J$-analytic by Theorem A. 33 in Appendix A. 4 , and as the family $\left\{U_{a}\right\}$ is increasing in $a$, we have $Z_{a^{\prime}, b^{\prime}} \supset Z_{a^{\prime \prime}, b^{\prime \prime}}$ if $a^{\prime} \leq a^{\prime \prime}, b^{\prime} \leq b^{\prime \prime}$.

Let $y_{0} \in M$ be a given point. If $y_{0} \notin E_{c}$, then $\nu\left(\varphi_{y_{0}}, T\right)<c$ by definition of $E_{c}$. Choose $a$ such that $\nu\left(\varphi_{y_{0}}, T\right)<a<c$. The claim (a) in Lemma B. 17 implies that $U_{a}$ is bounded below in a neighborhood of $y_{0}$, thus $e^{-U_{a} / b}$ is integrable and $y_{0} \notin Z_{a, b}$ for $b>0$.

On the other hand, if $y_{0} \in E_{c}$ and if $a<c$, then Lemma B. 18 implies for all $\varepsilon>0$ that
$$U_{a}(y) \leq(1-\varepsilon)(c-a) \gamma \log \rho_{g}\left(y, y_{0}\right)+C(\varepsilon)$$
on a neighborhood of $y_{0}$. Hence $e^{-U_{a} / b}$ is non integrable at $y_{0}$ as soon as $b<(c-a) \gamma / 4$. We obtain therefore
$$E_{c}=\bigcap_{a<c, b<(c-a) \gamma / 4} Z_{a, b} .$$
This proves that $E_{c}$ is a $J$-analytic subset of $M$. \(\square\)

Remark B.20. 1) For an almost complex 4-manifold ( $M, J$ ), it has the local symplectic property [55]. For any $p \in M$, there exists a locally symplectic form $\omega_{p}$ on small neighborhood $U_{p}$. Hence on $U_{p}$ we can define Lelong number $\nu_{2}(q, p, T)$, see Definition B. 14 in Appendix B.1. Thus, we have Theorem B. 19 in B. 2 for $\left(U_{p}, g_{p}, J, \omega_{p}\right), g_{p}(\cdot, \cdot)=\omega_{p}(\cdot, J \cdot)$. By Theorem B. 15 in Appendix B.1, it is also true for Lelong number $\nu_{1}(p, T)$ (see Definition B. 13 in Appendix B.1) defined on tamed almost complex 4-manifold, that is, the upper level sets
$$E_{c}(T)=\left\{p \in M \mid \nu_{1}(p, T) \geq c\right\}$$
are $J$-analytic subsets of complex dimension $\leq 1$ on a closed almost complex 4-manifold $(M, J)$ which is tamed by a symplectic form $\omega_{1}$.
2) It is natural to ask that for bidegree $(1,1)$ or bidegree $(n-1, n-1)$ closed positive currents on the higher dimensional almost Kähler manifolds, could one extend the above theorem?

As in classical complex analysis, we have Siu's decomposition formula of closed positive $(1,1)$ currents on almost Kähler 4-manifolds.

Theorem B.21. If $T$ is a closed positive almost complex $(1,1)$-current on an almost Kähler 4-manifold ( $M, g, J, \omega$ ), there is a unique decomposition of $T$ as a (possibly finite) weakly convergent series
$$T=\Sigma_{j \geq 1} \lambda_{j} T_{\Sigma_{j}}+R, \quad \lambda_{j}>0,$$
where $T_{\Sigma_{j}}$ is the current of integration over an irreducible 1-dimensional $J$-analytic set $\Sigma_{j} \subset M$ and where $R$ is a closed positive almost complex $(1,1)$-current with the property that $\operatorname{dim}_{\mathbb{C}} E_{c}(R)<1$ for every $c>0$.

Proof. Uniqueness. If $T$ has such a decomposition, the 1-dimensional components of $E_{c}(T)$ are $\left(\Sigma_{j}\right)_{\lambda_{j}>c}$, for
$$\nu(p, T)=\Sigma_{j \geq 1} \lambda_{j} \nu\left(p, T_{\Sigma_{j}}\right)+\nu(p, R)$$
is non zero only on $\bigcup \Sigma_{j} \cup \bigcup E_{c}(R)$, and is equal to $\lambda_{j}$ generically on $\Sigma_{j}$ (more precisely, $\nu(p, T)=\lambda_{j}$ at every regular point of $\Sigma_{j}$ which does not belong to any intersection $\Sigma_{j} \cap \Sigma_{k}$, $k \neq j$ or to $\left.\bigcup E_{c}(R)\right)$. In particular $\Sigma_{j}$ and $\lambda_{j}$ are unique.

Existence. By Theorem B.19, $E_{c}(T)$ is a $J$-analytic subset of dimension $\leq 1$. For any $p \in M$, by Theorem A.33, there are 1-dimensional components $\left(\Sigma_{j}\right)_{\lambda_{j}>c}$ of $E_{c}(T)$ passing through $p$. Let $\left(\Sigma_{j}\right)_{j \geq 1}$ be the countable collection of 1-dimensional components occurring in one of the sets $E_{c}(T), c \in \mathbb{Q}_{+}^{*}$, and let $\lambda_{j}>0$ be the generic Lelong number of $T$ along $\Sigma_{j}$. Then Proposition B. 11 shows by induction on $N$ that
$$R_{N}=T-\sum_{1 \leq j \leq N} \lambda_{j} T_{\Sigma_{j}}$$
is positive. As $R_{N}$ is a decreasing sequence, there must be a limit $R=\lim _{N \rightarrow+\infty} R_{N}$ in the weak topology. Thus we have the asserted decomposition. By construction, $R$ has zero generic Lelong number along $\Sigma_{j}$, so $\operatorname{dim}_{\mathbb{C}} E_{c}(R)<1$ for every $c>0$. \(\square\)

Remark B.22. Similarly, by Theorem B.15, it is also true for closed positive almost complex $(1,1)$-current $T$ on a closed almost complex 4 -manifold $(M, J)$ which is tamed by a symplectic form $\omega_{1}$.

\section*{Appendix C Demailly's approximation theorem on tamed almost complex 4-manifolds}

Let $(M, J)$ be a closed almost complex 4-manifold and let $T$ be a closed positive current of bidegree $(1,1)$ on $(M, J)$. In general $T$ can not be approximated by smooth closed positive currents. However, as done in classical complex analysis, we shall see that it is always possible to approximate a closed positive current $T$ of type $(1,1)$ by smooth closed real currents admitting a small negative part and that this negative part can be estimated in terms of the Lelong numbers of $T$ and the geometry (for complex analysis, see Demailly [11,12]).

In this appendix, we will give a Demailly's approximation theorem on tamed almost complex 4-manifolds. Our approach is along the lines used by Demailly to give a proof of Theorem 1.1 in [12].

\section*{C. 1 Exponential map associated to the second canonical connection}

In this subsection, we study exponential map associated to the second canonical connection on almost Hermitian manifolds. Suppose $\left(M, g_{J}, J, F\right)$ is an almost Hermitian $2 n$-manifold. Choose a complex coordinate $\left\{z_{i}=x_{i}+\sqrt{-1} y_{i}\right\}_{i=1}^{n}$ around $p \in M$ such that $\left\{\left.\frac{\partial}{\partial z_{i}}\right|_{p}\right\}_{i=1}^{n} \subseteq$ $T_{p}^{1,0} M$ is orthonormal at $p$ with respect to the almost Hermitian metric $h=g_{J}-\sqrt{-1} F$. Let $\left\{e_{i}\right\}_{i=1}^{n}$ be a unitary frame around $p$ such that $e_{i}(p)=\left.\frac{\partial}{\partial z_{i}}\right|_{p}$. Let $\nabla^{1}$ be the second canonical connection satisfying $\nabla^{1} g_{J}=0$ and $\nabla^{1} J=0$, hence $\nabla^{1} F=0$ and $\nabla^{1} h=0$ (P. Gauduchon [28]). In particular, note that if $J$ is integrable, that is, $(M, J)$ is a complex manifold, $\nabla^{1}$ is Chern connection; if $\left(M, g_{J}, J, F\right)$ is a Kähler manifold, $\nabla^{1}$ is Levi-Civita connection (P. Gauduchon [29]). Then locally there exists a matrix of valued 1 -forms $\left\{\theta_{i}^{j}\right\}$, called the connection 1-forms, such that
$$\nabla^{1} e_{i}=\theta_{i}^{j} e_{j}, \quad \theta_{i}^{j}(p)=0 .$$
Let $\left\{\theta^{1}, \cdots, \theta^{n}\right\}$ be the dual coframe of $\left\{e_{1}, \cdots, e_{n}\right\}$. Then we have $\theta^{i}(p)=d z_{i}(p)$ by the choice of $\left\{z_{i}\right\}_{i=1}^{n}$. There holds the following Maurer-Cartan equations [9, 29]:
$$\left\{\begin{aligned}
d \theta^{i} & =-\theta_{j}^{i} \wedge \theta^{j}+\Theta^{i} \\
d \theta_{j}^{i} & =-\theta_{k}^{i} \wedge \theta_{j}^{k}+\Psi_{j}^{i},
\end{aligned}\right.$$
where
$$\Theta^{i}=\left(\Theta^{i}\right)^{(2,0)}+\left(\Theta^{i}\right)^{(0,2)}=T_{j k}^{i} \theta^{j} \wedge \theta^{k}+N \bar{j}_{\bar{k}}^{i} \bar{\theta}^{j} \wedge \bar{\theta}^{k}$$
is the torsion form with vanishing $(1,1)$ part and $\Psi_{j}^{i}$ is the curvature form (see Tosatti-Weinkove-Yau [77]). Take exterior derivative of (C.2) to get
$$0=-d \theta_{j}^{i} \wedge \theta^{j}+\theta_{j}^{i} \wedge d \theta^{j}+d \Theta^{i}$$
$$\begin{aligned}
& =-d \theta_{j}^{i} \wedge \theta^{j}-\theta_{j}^{i} \wedge \theta_{k}^{j} \wedge \theta^{k}+d \Theta^{i}+\theta_{j}^{i} \wedge \Theta^{j} \\
& =-\left(d \theta_{j}^{i}+\theta_{k}^{i} \wedge \theta_{j}^{k}\right) \wedge \theta^{j}+d \Theta^{i}+\theta_{j}^{i} \wedge \Theta^{j} \\
& =-\Psi_{j}^{i} \wedge \theta^{j}+d \Theta^{i}+\theta_{j}^{i} \wedge \Theta^{j} .
\end{aligned}$$
Hence $d \Theta^{i}=\Psi_{j}^{i} \wedge \theta^{j}-\theta_{j}^{i} \wedge \Theta^{j}$. Define $R_{i k \bar{l}}^{j}, K_{j k l}^{i}$ and $K_{j \bar{k} \bar{l}}^{i}$ (see Tosatti-Weinkove-Yau [77]) by
$$\begin{aligned}
& \left(\Psi_{i}^{j}\right)^{(1,1)}=R_{i k \bar{l}}^{j} \theta^{k} \wedge \bar{\theta}^{l}, \\
& \left(\Psi_{i}^{j}\right)^{(2,0)}=K_{j k l}^{i} \theta^{k} \wedge \theta^{l}, \\
& \left(\Psi_{i}^{j}\right)^{(0,2)}=K_{j \bar{k} l}^{i} \bar{\theta}^{k} \wedge \bar{\theta}^{l},
\end{aligned}$$
with $K_{j k l}^{i}=-K_{j l k}^{i}, K_{j \bar{k} \bar{l}}^{i}=-K_{j \overline{l k}}^{i}, K_{j k l}^{i}=\overline{K_{i \bar{l} k}^{j}}, \delta^{s \bar{j}} \delta_{t \bar{i}} R_{s k \bar{l}}^{t}=\overline{R_{i l \bar{k}}^{j}}$, where
$$K_{j \bar{k} \bar{l}}^{i}=2 T_{p j}^{i} N_{\bar{j} \bar{l}}^{p}+N_{\bar{k} \bar{l}, j}^{i}, K_{j k l}^{i}=\overline{K_{i \bar{k}}^{j}},$$
and $\delta^{s \bar{j}}$ is the Kronecker delta and $\delta_{t \bar{i}}$ is its inverse.
For a local complex frame
$$\left\{\frac{\partial}{\partial z_{1}}, \frac{\partial}{\partial z_{2}}, \cdots, \frac{\partial}{\partial z_{n}}\right\} \subseteq T^{1,0} M, \quad\left\{\frac{\partial}{\partial \bar{z}_{1}}, \frac{\partial}{\partial \bar{z}_{2}}, \cdots, \frac{\partial}{\partial \bar{z}_{n}}\right\} \subseteq T^{0,1} M .$$
Denote by $\frac{\partial}{\partial z_{\bar{i}}}=\frac{\partial}{\partial \bar{z}_{i}}$, and define $\Gamma_{A B}^{C}$ as
$$\nabla_{\frac{\partial}{\partial z_{A}}}^{1} \frac{\partial}{\partial z_{B}}=\Gamma_{A B}^{C} \frac{\partial}{\partial z_{C}}, A, B, C \in\{1,2, \cdots, n, \overline{1}, \overline{2}, \cdots, \bar{n}\} .$$
Hence, $\overline{\Gamma_{A B}^{C}}=\Gamma_{\bar{A} \bar{B}}^{\bar{C}}, \Gamma_{A B}^{C}=\Gamma_{B A}^{C}$. Let $h:=g_{J}-\sqrt{-1} F=\sum_{i} \theta^{i} \otimes \bar{\theta}^{i}$, then $h_{i j}=$ $h\left(\partial / \partial z_{i}, \partial / \partial z_{j}\right)$.

Lemma C.1. The only non-vanishing Christoffel symbols are $\Gamma_{i j}^{k}, \Gamma_{\bar{i} \bar{j}}^{\bar{k}}$, where
$$\Gamma_{i j}^{k}=\sum_{l=1}^{n} h^{k \bar{l}} \frac{\partial h_{j \bar{l}}}{\partial z_{i}} .$$

Proof. There hold
$$\nabla_{\frac{\partial}{\partial z_{i}}}^{1} \frac{\partial}{\partial z_{j}}=\sum_{k} \Gamma_{i j}^{k} \frac{\partial}{\partial z_{k}}+\sum_{k} \Gamma_{i j}^{\bar{k}} \frac{\partial}{\partial \bar{z}_{k}},$$
and
$$\nabla_{\frac{\partial}{\partial \bar{z}_{i}}}^{1} \frac{\partial}{\partial z_{j}}=\sum_{k} \Gamma_{i \bar{j}}^{k} \frac{\partial}{\partial z_{k}}+\sum_{k} \Gamma_{i \bar{j}}^{\bar{k}} \frac{\partial}{\partial \bar{z}_{k}} .$$
Since $\nabla^{1} J=0$, and $J$ acts on $T^{1,0} M$ being by multiplying $\sqrt{-1}$ and acts on $T^{0,1} M$ by $-\sqrt{-1}$, we have
$$\sqrt{-1} \nabla_{\frac{\partial}{\partial z_{i}}}^{1} \frac{\partial}{\partial z_{j}}=\nabla_{\frac{\partial}{\partial z_{i}}}^{1}\left(J \frac{\partial}{\partial z_{j}}\right)=J\left(\nabla_{\frac{\partial}{\partial z_{i}}}^{1} \frac{\partial}{\partial z_{j}}\right) .$$

Then
$$\sqrt{-1}\left(\sum_{k} \Gamma_{i j}^{k} \frac{\partial}{\partial z_{k}}+\sqrt{-1} \sum_{k} \Gamma_{i j}^{\bar{k}} \frac{\partial}{\partial \bar{z}_{k}}\right)=\sqrt{-1}\left(\sum_{k} \Gamma_{i j}^{k} \frac{\partial}{\partial z_{k}}-\sqrt{-1} \sum_{k} \Gamma_{i j}^{\bar{k}} \frac{\partial}{\partial \bar{z}_{k}}\right),$$
which implies that $\Gamma_{i j}^{\bar{k}}=0$. Similarly, $\Gamma_{i \bar{j}}^{\bar{k}}, \Gamma_{i \bar{j}}^{k}$ vanish. Nonzero ones are only $\Gamma_{i j}^{k}, \Gamma_{\bar{i} \bar{j}}^{\bar{k}}$. Moreover,
$$\frac{\partial}{\partial z_{i}} h\left(\frac{\partial}{\partial z_{j}}, \frac{\partial}{\partial \bar{z}_{j}}\right)=h\left(\sum_{l} \Gamma_{i j}^{l} \frac{\partial}{\partial z_{l}}, \frac{\partial}{\partial \bar{z}_{k}}\right)=\sum_{l} \Gamma_{i j}^{l} h_{l \bar{k}} .$$
Hence, $\Gamma_{i j}^{k}=\sum_{l=1}^{n} h^{k \bar{l}} \frac{\partial h_{j \bar{l}}}{\partial z_{i}}$. \(\square\)

By (C.1) and Lemma C.1, we have
$$\begin{aligned}
e_{i} & =e_{i}(p)+\frac{1}{2}\left(\nabla^{1}\right)^{2} e_{i}+O\left(|z|^{3}\right) \\
& =\left.\frac{\partial}{\partial z_{i}}\right|_{p}+\sum_{j, l, m}\left(b_{j i l m}^{\prime \prime} z_{l} z_{m}+\bar{b}_{j i l m}^{\prime \prime} \bar{z}_{l} \bar{z}_{m}+c_{j i l m}^{\prime \prime} z_{l} \bar{z}_{m}\right) \frac{\partial}{\partial z_{j}}+O\left(|z|^{3}\right) .
\end{aligned}$$
Without loss of generality, we may assume that $b_{j i l m}^{\prime \prime}=b_{j i m l}^{\prime \prime}$, otherwise, if $b_{j i l m}^{\prime \prime}=-b_{j i m l}^{\prime \prime}$ then $\sum_{l, m} b_{j i l m}^{\prime \prime} z_{l} z_{m}=0$. Also, by (C.4), the skew symmetric part of $\left(\nabla^{1}\right)^{2} e_{i}$ is $\left(\Psi_{j}^{i}\right)^{(1,1)}=$ $R_{j l \bar{m}}^{i} \theta^{l} \wedge \bar{\theta}^{m}$. Hence
$$c_{j i l m}^{\prime \prime}=\frac{1}{2} R_{j l \bar{m}}^{i} .$$
By (C.3), the skew symmetric part is $\Theta^{i}=T_{j k}^{i} \theta^{j} \wedge \theta^{k}+N_{\bar{j} \bar{k}}^{i} \bar{\theta}^{j} \wedge \bar{\theta}^{k}$. Hence,
$$\begin{aligned}
\theta^{i} & =\theta^{i}(p)+\nabla^{1} \theta^{i}+O\left(|z|^{2}\right) \\
& =\sum_{j} \delta_{i j} d z^{j}+\sum_{j, l}\left(a_{j i l}^{\prime} z_{l} d z_{j}+\bar{a}_{j i l}^{\prime \prime} \bar{z}_{l} d \bar{z}_{j}\right)+O\left(|z|^{2}\right) .
\end{aligned}$$
By (C.7) and (C.9), we can expand $h_{i j}(z)=h\left(\frac{\partial}{\partial z_{i}}, \frac{\partial}{\partial z_{j}}\right)$ as follows:
$$\begin{aligned}
h_{i j}(z)= & \delta_{i j}+\sum_{l}\left(a_{j i l} z_{l}+\bar{a}_{j i l} \bar{z}_{l}\right)+\sum_{l, m}\left(b_{j i l m}^{\prime} z_{l} z_{m}+\bar{b}_{j i l m}^{\prime} \bar{z}_{l} \bar{z}_{m}\right) \\
& +\sum_{l, m} c_{j i l m}^{\prime} z_{l} \bar{z}_{m}+O\left(|z|^{3}\right),
\end{aligned}$$
where $a_{j i l}=a_{j i l}^{\prime}+a_{j i l}^{\prime \prime}, b_{j i l m}^{\prime}=b_{j i m l}^{\prime}$. We may always arrange that skew symmetry relation $a_{j i l}=-a_{l i j}$ holds; otherwise the change of variables $z_{i}=z_{i}^{\prime}-\frac{1}{4} \sum_{j, l}\left(a_{j i l}+a_{l i j}\right) z_{j}^{\prime} z_{l}^{\prime}$ yields coordinates $\left(z_{l}^{\prime}\right)$ with this property. By the definition of $a_{j i l}$ and
$$\left.\nabla^{1} \theta^{i}\right|_{p}=\left.d \theta^{i}\right|_{p}=\left.\left(-\theta_{j}^{i} \wedge \theta^{j}+\Theta^{i}\right)\right|_{p}=T_{j l}^{i} \theta^{j} \wedge \theta^{l}+N_{\bar{j} l}^{i} \bar{\theta}^{j} \wedge \bar{\theta}^{l},$$
it is easy to see that $a_{j i l}^{\prime}=T_{j l}^{i}, \bar{a}_{j i l}^{\prime \prime}=\overline{N_{\bar{j} \bar{l}}^{i}}$. If $h$ is Kähler, then $a_{j i l}=0$; in that case $b_{j i l m}^{\prime}$ is also symmetric in $j, l, m$ and a new change of variables $z_{i}=z_{i}^{\prime}-\frac{1}{3} \sum_{j, l, m} b_{j i l m}^{\prime} z_{j}^{\prime} z_{l}^{\prime} z_{m}^{\prime}$ gives $b_{j i l m}^{\prime}=0$ likewise.

The complex frame of $T_{p}^{1,0} M$ defined by
$$\tilde{e}_{s}=\partial / \partial z_{s}-\sum_{j}\left(a_{j s k} z_{j}+\sum_{m} b_{j s k m}^{\prime} z_{j} z_{m}\right) \partial / \partial z_{k}$$
satisfies
$$\begin{gathered}
<\tilde{e}_{s}, \tilde{e}_{t}>_{h}=\delta_{s t}-\sum_{j, k} c_{t s j k} z_{j} \bar{z}_{k}+O\left(|z|^{3}\right) \\
\partial / \partial z_{s}=\tilde{e}_{s}+\sum_{l}\left(\sum_{j} a_{j s l} z_{j}+\sum_{j, k} b_{j s l k} z_{j} z_{k}+O\left(z^{3}\right)\right) \tilde{e}_{l}
\end{gathered}$$
with $c_{t s j k}=-c_{t s j k}^{\prime}-\sum a_{j s l} \bar{a}_{k t l}$ and $b_{j s k l}=b_{j s k l}^{\prime}+\sum a_{l s m} a_{j m k}$. Hence, in the Kähler case, $a_{j s l}=0$ and $b_{j s l k}=0$. The formula $\partial_{\frac{\partial}{\partial z_{j}}}<\tilde{e}_{s}, \tilde{e}_{t}>_{h}=<\nabla_{\frac{\partial}{\partial z_{j}}}^{1} \tilde{e}_{s}, \tilde{e}_{t}>_{h}$ with respect to $J(p)$ easily gives the following
$$\begin{aligned}
& \nabla^{1} \tilde{e}_{s}=-\sum_{t, j, k} c_{t s j k} \bar{z}_{k} d z_{j} \otimes \tilde{e}_{t}+O\left(|z|^{2}\right) \\
& \left.(\tilde{\Psi})^{(1,1)}\right|_{p}=\sum_{s, t, j, k} c_{t s j k} d z_{j} \wedge d \bar{z}_{k} \otimes \tilde{\theta}^{s} \otimes \tilde{e}_{t},
\end{aligned}$$
where $\tilde{\theta}^{s}$ is the dual frame of $\tilde{e}_{s}$. Hence $c_{t s j k}=R_{t j k}^{s}$.
Remark C.2. If $M$ is a complex manifold, then $N_{\bar{j} \bar{k}}^{i}=0$. By (C.5), $K_{j \bar{k} \bar{l}}^{i}=0$, thus $\left(\tilde{\Psi}_{j}^{i}\right)^{(1,1)}=\tilde{\Psi}_{j}^{i}$.

Given a vector field $\zeta=\sum_{l} \zeta_{l} \partial / \partial z_{l}$ in $T^{1,0} M$, we denote by $\left(\xi_{m}\right)$ the components of $\zeta$ with respect to the basis $\left(\tilde{e}_{m}\right)$, thus $\zeta=\sum_{m} \xi_{m} \tilde{e}_{m}$ in $T^{1,0} M$. By (C.11), we have
$$\xi_{m}=\zeta_{m}+\sum_{j, l} a_{j m l} z_{j} \zeta_{l}+\sum_{j, k, l} b_{j m l k} z_{j} z_{k} \zeta_{l}$$
By a direct calculation, we have
$$\begin{aligned}
\nabla^{1}\left(\partial / \partial z_{l}\right)= & -\sum_{j, k, m} c_{m l j k} \bar{z}_{k} d z_{j} \otimes \tilde{e}_{m}+\sum_{j, m} a_{m l j} d z_{j} \otimes \tilde{e}_{m} \\
& +2 \sum_{j, k, m} b_{m l j k} z_{k} d z_{j} \otimes \tilde{e}_{m}+O\left(|z|^{2}\right) d z \\
= & -\sum_{j, k, m}\left(c_{m l j k} \bar{z}_{k}-2 b_{m l j k} z_{k}\right) d z_{j} \otimes \frac{\partial}{\partial z_{m}} \\
& +\sum_{j, m}\left(a_{m l j}-\sum_{k, i} a_{i l j} a_{i m k} z_{k}\right) d z_{j} \otimes \frac{\partial}{\partial z_{m}}+O\left(|z|^{2}\right) d z .
\end{aligned}$$
Hence, as in classical complex analysis (cf. (2.5) in Demailly [12]), we have
$$\begin{aligned}
\nabla^{1} \zeta= & \sum_{m} d \zeta_{m} \otimes \frac{\partial}{\partial z_{m}}-\sum_{j, k, l, m}\left(c_{l m j k} \bar{z}_{k}-2 b_{l m j k} z_{k}\right) \zeta_{m} d z_{j} \otimes \frac{\partial}{\partial z_{l}} \\
& +\sum_{j, l, m}\left(a_{l m j}-\sum_{k, i} a_{l i j} a_{i m k} z_{k}\right) \zeta_{m} d z_{j} \otimes \frac{\partial}{\partial z_{l}}+O\left(|z|^{2}\right) \zeta d z
\end{aligned}$$

Consider a curve $t \rightarrow u(t)$. By a substitution of variables $z_{j}=u_{j}(t), \zeta_{l}=\frac{d u_{l}}{d t}$ in formula (C.14), the equation $\nabla^{1}\left(\frac{d u}{d t}\right)=0$ becomes
$$\frac{d^{2} u_{s}}{d t^{2}}=\sum_{j, k, l}\left(c_{l s j k} \bar{u}_{k}(t)-2 b_{l s j k} u_{k}(t)\right) \frac{d u_{j}}{d t} \frac{d u_{l}}{d t}+O\left(|u(t)|^{2}\right)\left(\frac{d u}{d t}\right)^{2} .$$
Notice that the contribution of the terms $\sum a_{j \bullet l} \zeta_{l} d z_{j}$ is zero by the skew symmetry relation. The initial condition $u(0)=z, u^{\prime}(0)=\zeta$ gives $u_{s}(t)=z_{s}+t \zeta_{s}+O\left(t^{2}|\zeta|^{2}\right)$. Hence,
$$\begin{aligned}
u_{s}(t)= & z_{s}+t \zeta_{s}+\sum_{i, j, k} c_{i s j k}\left(\frac{t^{2}}{2} \bar{z}_{k}+\frac{t^{3}}{6} \bar{\zeta}_{k}\right) \zeta_{i} \zeta_{j} \\
& -2 b_{i s j k}\left(\frac{t^{2}}{2} z_{k}+\frac{t^{3}}{6} \zeta_{k}\right) \zeta_{i} \zeta_{j}+O\left(t^{2}|\zeta|^{2}(|z|+|\zeta|)^{2}\right) .
\end{aligned}$$
An iteration of this procedure (substitution in (C.15) followed by an integration) easily shows that all terms but the first two in the Taylor expansion of $u_{s}(t)$ contain $\mathbb{C}$-quadratic factors of the form $\zeta_{j} \zeta_{l}$. Let us substitute $\zeta_{j}$ by its expression in terms of $z, \xi$ deduced from (C.13). We find that $\exp _{z}(\zeta)=u(1)$ has a third order expansion
$$\begin{aligned}
\exp _{z}(\zeta)_{s}= & K_{p, s}(z, \xi) \\
& +\sum_{j, k, l} c_{l s j k}\left(\frac{1}{2} \bar{z}_{k}+\frac{1}{6} \bar{\xi}_{k}\right) \xi_{j} \xi_{l}+O\left(|\xi|^{2}(|z|+|\xi|)^{2}\right),
\end{aligned}$$
where
$$\begin{aligned}
K_{p, s}(z, \xi)= & z_{s}+\xi_{s}-\sum_{j, l} a_{j s l} z_{j} \xi_{l}+\sum_{i, j, k, l} a_{j i l} a_{k s i} z_{j} z_{k} \xi_{l} \\
& -\sum_{j, k, l} b_{l s j k}\left(z_{j} z_{k} \xi_{l}+z_{k} \xi_{j} \xi_{l}+\frac{1}{3} \xi_{j} \xi_{k} \xi_{l}\right)
\end{aligned}$$
is a holomorphic polynomial of degree 3 in $z, \xi$ with respect to complex structure $J(p)$. In the Kähler case we simply have $\xi_{l}=\zeta_{l}$ and $K_{p, s}(z, \xi)=z_{s}+\xi_{s}$.

Remark C.3. 1 When $M$ is a complex manifold,
$$N_{\bar{i} j}^{\underline{s}}=0, a_{i s j}=T_{i j}^{s}, c_{l s i j}=\left(\Psi_{l}^{s}\right)^{(1,1)}=R_{l i \bar{j}}^{s} .$$

2 When $M$ is a quasi-Kähler (or almost Kähler) manifold,
$$T_{i j}^{s}=0, a_{i s j}=\overline{N_{i \bar{j}}^{s}}, c_{l s i j}=\left(\Psi_{l}^{s}\right)^{(1,1)}=R_{l i \bar{j}}^{s} .$$
3 When $M$ is a Kähler manifold,
$$a_{i s j}=0, b_{l s i j}=0, c_{l s i j}=\left(\Psi_{l}^{s}\right)^{(1,1)}=R_{l i \bar{j}}^{s} .$$

The exponential map is unfortunately non-holomorphic for $z$ fixed with respect to $J(p) \cong J_{s t}$. However, as done in classical complex analysis, we make it quasi-holomorphic with respect to $\zeta \in T_{z}^{1,0} M$ as follows: for $z, J(p)$ fixed, we consider the formal power series obtained by eliminating all monomials in the Taylor expansion of $\zeta \mapsto \exp _{z}(\zeta)$ at the origin which are not holomorphic with respect to $\zeta$. This defines in a unique way a jet of infinite order along the zero section of $T_{z}^{1,0} M$. There is a smooth map
$$T_{z}^{1,0} M \rightarrow M, \quad(z, \zeta) \mapsto \operatorname{exph}_{z}(\zeta),$$
such that its jet at $\zeta=0$ coincides with the " $J(p)\left(\cong J_{s t}\right)$-holomorphic" part of $\zeta \mapsto \exp _{z}(\zeta)$. Moreover, (C.16) and (C.17) imply that
$$\operatorname{exph}_{z}(\zeta)_{s}=K_{p, s}(z, \xi)+\frac{1}{2} \sum_{i, j, k} c_{j s i k} \bar{z}_{k} \xi_{i} \xi_{j}+O\left(|\xi|^{2}(|z|+|\xi|)^{2}\right) .$$
By including in $K_{p, s}$ all holomorphic monomials of partial degree at most 2 in $z$ and $N$ in $\xi\left(N \geq 2\right.$ being a given integer), we get holomorphic polynomials $L_{p, s}(z, \xi)$ of linear part $z_{s}+\xi_{s}$ and total degree $N+2$, such that
$$\operatorname{exph}_{z}(\zeta)_{s}=K_{p, s}(z, \xi)+O\left(\bar{z}, z \bar{z}, \bar{z} \bar{z},|z|^{3}, \xi^{N-1}\right) \xi^{2} .$$
Here a notation as $O\left(\bar{z}, z \bar{z}, \bar{z} \bar{z},|z|^{3}, \xi^{N-1}\right) \xi^{2}$ indicates an arbitrary function in the ideal of $C^{\infty}$ functions generated by monomials of the form $\bar{z}_{k} \xi_{l} \xi_{m}, z_{i} \bar{z}_{j} \xi_{l} \xi_{m}, \bar{z}_{i} \bar{z}_{j} \xi_{l} \xi_{m}, z^{\alpha} \bar{z}^{\beta} \xi_{l} \xi_{m}$ and $\xi^{\gamma}$, for all multi-indices $|\alpha|+|\beta|=3$ and $|\gamma|=N+1$. By the implicit function theorem applied to the mapping $L_{p}=\left(L_{p, m}\right)_{1 \leq m \leq n}$ we thus get (cf. Proposition 2.9 in Demailly [12])

Proposition C.4. Suppose $\left(M, g_{J}, J, F\right)$ is an almost Hermitian manifold. Let $h=g_{J}-$ $\sqrt{-1} F$ be an almost Hermitian metric on $T^{1,0} M$. There exists a $C^{\infty}$ map
$$T_{p}^{1,0} M \rightarrow M, \quad(p, \zeta) \mapsto \operatorname{exph}_{p}(\zeta)$$
with the following properties:
\begin{itemize}
\item[(1)] . For every $p \in M \operatorname{exph}_{p}(0)=p$ and $d_{\zeta} \operatorname{exph}_{p}(0)=I d_{T_{p}^{1,0} M}$.
\item[(2)] . For every $p \in M$, the map $\zeta \rightarrow \operatorname{exph}_{p}(\zeta)$ has a quasi-holomorphic Taylor expansion at $\zeta=0$ with respect to fixed almost complex structure $J(p)$ on small neighborhood. Moreover, with respect to an almost Hermitian structure $\left(g_{J}, J, F\right)$, there are local normal complex coordinates $\left(z_{1}, z_{2}, \cdots, z_{n}\right)$ on $M$ centered at $p, z_{i}(p)=0, i=1,2, \cdots, n$, and holomorphic normal complex coordinates $\left(\zeta_{j}\right)$ on the fibers of $T^{1,0} M$ near $p$ with respect to the fixed complex structure $J(p)$ such that
$$\operatorname{exph}_{z}(\xi)=L_{p}\left(z, \rho_{p}(z, \xi)\right),$$
\end{itemize}
where $L_{p}(z, \xi)$ is a holomorphic polynomial map of degree 2 in $z$ and of degree $N$ in $\xi$, and where $\rho_{p}: \mathbb{C}^{n} \times \mathbb{C}^{n} \rightarrow \mathbb{C}^{n}$ is a smooth map such that
$$\begin{aligned}
L_{p, m}(z, \xi)= & z_{m}+\xi_{m}-\sum_{j, l} a_{j m l} z_{j} \xi_{l}+\sum_{i, j, k, l} a_{l m i} a_{j i k} z_{j} z_{k} \xi_{l} \\
& -\sum_{j, k, l} b_{l m j k}\left(z_{j} z_{k} \xi_{l}+z_{k} \xi_{j} \xi_{l}+\frac{1}{3} \xi_{j} \xi_{k} \xi_{l}\right)+O\left((|z|+|\xi|)^{4}\right),
\end{aligned}$$
$$\begin{aligned}
\rho_{p, m}(z, \xi)= & \xi_{m}+\sum_{2 \leq|\alpha| \leq N}\left(\sum_{k} d_{\alpha m k} \xi^{\alpha} \bar{z}_{k}+\sum_{i, k} e_{\alpha m i k} \xi^{\alpha} z_{i} \bar{z}_{k}\right) \\
& +O\left(\bar{z}^{2},|z|^{3}, \xi^{N-1}\right) \xi^{2} .
\end{aligned}$$
(3). For $\alpha=\left(0, \cdots, 1_{l}, \cdots, 1_{j}, \cdots, 0\right)$ of degree 2, we have
$$d_{\alpha m k}=\frac{1}{2} c_{l m j k}, e_{\alpha m i k}=\frac{1}{2} \sum_{s} a_{l m s} c_{j s i k} z_{s},$$
where $c_{l m j k}$ is the curvature tensor $R_{l j \bar{k}}^{m}, a_{l m j}=T_{l j}^{m}+\overline{N_{\bar{l} j}^{m}}$.
Proof. The argument is similar to the proof of Proposition 2.9 in Demailly [12]. \(\square\)

Remark C.5. Suppose that $\left(M, g_{J}, J, F\right)$ is an almost Hermitian 4-manifold. For any $p \in M$, there exists a $J$-compatible local symplectic form $\omega_{p}$ on a small neighborhood $U_{p}$ such that $F=f_{p} \omega_{p}$, where $f_{p}>0$ on $U_{p}$ and $f_{p}(p)=1$ (cf. Lejmi [55]). On $U_{p}$, by Darboux's theorem (cf. McDuff-Salamon [60]), there is a coordinate chart $\left(V_{p}, \phi_{p}\right)$, where $V_{p} \subseteq U_{p}$ is a neighborhood of $p, \phi_{p}: V_{p} \rightarrow \phi_{p}\left(V_{p}\right) \subset \mathbb{R}^{4}$ is a homeomorphism such that $\phi^{*} \omega_{0}=\omega_{p}$, and
$$\omega_{0}=\sum_{i=1}^{2} d x_{i} \wedge d y_{i}$$
is the standard symplectic form on $\mathbb{R}^{4}$. Let $J_{\text {st }}$ be the standard complex structure on $\mathbb{C}^{2} \cong \mathbb{R}^{4}$ with complex coordinates $z_{i}=x_{i}+\sqrt{-1} y_{i}, i=1,2$, and $J_{p}=\phi^{*} J_{s t}$ the induced complex structure on $V_{p}$. Set $g_{p}(\cdot, \cdot)=F(\cdot, J \cdot)$. So we can get $g_{J}=g_{p} e^{D}$ on $V_{p}$, where $D$ is a symplectic $J$-anti-invariant $(2,0)$ tensor (for details, see Tan-Wang-Zhou [74]). Therefore, for the almost Hermitian 4-manifold $\left(M, g_{J}, J, F\right)$, any $p \in M$, there exists a small neighborhood $V_{p}$ such that on $V_{p}$ there is $F$-compatible complex structure $J_{p}$, that is, any almost complex 4-manifold has locally complex structure. Let $g_{J_{s t}}(\cdot, \cdot)=F\left(\cdot, J_{s t} \cdot\right)$ on $V_{p}$, then $g_{J_{s t}}(p)=g_{J}(p), g_{J_{s t}}$ is a Hermitian metric on $V_{p}$.

\section*{C. 2 Regularization of quasi-J-plurisubharmonic functions on tamed almost Hermitian 4-manifolds}

In this subsection, we consider regularization of quasi-J-plurisubharmonic functions on almost Hermitian $2 n$-manifolds. Let $\left(M, g_{J}, J, F\right)$ be an almost Hermitian $2 n$-manifold. Suppose $\phi$ is a quasi-J-plurisubharmonic function, that is, a function which is locally the sum of $\phi_{1}$ and $\phi_{2}$ where $\phi_{1}$ is a smooth function and $\phi_{2}$ is a $J$-plurisubharmonic function. In this section, as done in Section 3 of Demailly's article [12], we consider regularization of quasi-J-plurisubharmonic functions in almost Hermitian $2 n$-manifolds tamed by $\omega_{1}=F+d_{J}^{-}(v+\bar{v})$.

For any $p \in\left(M, g_{J}, J, F\right)$, choose a complex coordinate
$$U_{p}=\left\{z_{i}=x_{i}+\sqrt{-1} y_{i}, i=1, \cdots, n\right\}$$
around $p$ such that $\left\{\left.\frac{\partial}{\partial z_{i}}\right|_{p}\right\}_{i=1,2, \cdots, n} \subset T_{p}^{1,0} M$ is orthonormal at $p$ with respect to almost Hermitian metric $h=g_{J}-\sqrt{-1} F$. Consider the exponential map:
$$T_{z}^{1,0} M \rightarrow M,(z, \zeta) \mapsto \exp _{z}(\zeta), z \in U_{p}, \quad(z, \zeta) \in T_{z}^{1,0} M .$$

By (C.16), we have Taylor expansion of exponential map,
$$\begin{aligned}
\exp _{z}(\zeta)_{s}= & K_{p, s}(z, \xi)+\sum_{1 \leq i, j, k \leq n} c_{j s i k}\left(\frac{1}{2} \bar{z}_{k}+\frac{1}{6} \bar{\xi}_{k}\right) \xi_{i} \xi_{j} \\
& +O\left(|\xi|^{2}(|z|+|\xi|)^{2}\right),
\end{aligned}$$
where
$$\begin{aligned}
K_{p, s}(z, \xi)= & z_{s}+\xi_{s}-\sum_{1 \leq i, j \leq n} a_{i s j} z_{i} \xi_{j}+\sum_{1 \leq i, j, k, l \leq n} a_{k s l} a_{i l j} z_{i} z_{j} \xi_{k} \\
& -\sum_{1 \leq i, j, k \leq n} b_{j s k i}\left(z_{i} z_{j} \xi_{k}+z_{i} \xi_{j} \xi_{k}+\frac{1}{3} \xi_{i} \xi_{j} \xi_{k}\right)
\end{aligned}$$
Here $a_{i j s}, b_{i k s j}$ and $c_{i j k s}$ are given in Appendix C.1. However, we make this map quasiholomorphic as follows:
$$\operatorname{exph}_{z}(\zeta)_{s}=K_{p, s}(z, \xi)+\frac{1}{2} \sum_{1 \leq i, j, k \leq n} c_{j s i k} \bar{z}_{k} \xi_{i} \xi_{j}+O\left(|\xi|^{2}(|z|+|\xi|)^{2}\right) .$$
Here, for fixed $z \in M, \operatorname{exph}_{z}(\zeta)$ is holomorphic for $\zeta \in T_{z}^{1,0} M$
For a fixed point $p \in M$ and use the coordinate $\left(p, e_{1}, \cdots, e_{n}\right)$ for $T_{p}^{1,0} M$, where $\left(e_{1}, \cdots, e_{n}\right)$ is orthernormal. Suppose $\left(\theta^{1}, \cdots, \theta^{n}\right)$ is the dual coframe of $\left(e_{1}, \cdots, e_{n}\right)$. As in Appendix C.1, $\zeta \in T_{z}^{1,0}(M), \zeta=\sum \zeta_{i} \frac{\partial}{\partial z_{i}}=\sum \xi_{i} \tilde{e}_{i}$,
$$|\zeta|^{2}=\sum_{m}\left|\xi_{m}\right|^{2}-\sum_{j, k, l, m} c_{l m j k} z_{j} \bar{z}_{k} \xi_{l} \bar{\xi}_{m}+O\left(|z|^{3}\right)|\xi|^{2} .$$
The volume form
$$\begin{aligned}
\mathrm{d} \lambda(\zeta) & =\frac{1}{2^{n} n!}\left(\sqrt{-1} \partial_{J(p)} \bar{\partial}_{J(p)}|\zeta|^{2}\right)^{n} \\
& =\left(1-\sum_{j, k, l} c_{l l j k} z_{j} \bar{z}_{k}+O\left(|z|^{3}\right)\right) \frac{\sqrt{-1}}{2} d \xi_{1} \wedge d \bar{\xi}_{1} \wedge \cdots \wedge \frac{\sqrt{-1}}{2} d \xi_{n} \wedge d \bar{\xi}_{n}
\end{aligned}$$

Choose a smooth cut-off function $\chi: \mathbb{R} \rightarrow \mathbb{R}$ satisfying
$$\chi(t)\left\{\begin{array}{l}
>0, t<1 \\
=0, t \geq 1,
\end{array} \quad \int_{v \in \mathbb{C}^{n}} \chi\left(|v|^{2}\right) \mathrm{d} \lambda(v)=1 .\right.$$

Set
$$\begin{aligned}
& \phi_{\varepsilon}(z)=\frac{1}{\varepsilon^{2 n}} \int_{\zeta \in T_{z}^{1,0} M} \phi\left(\operatorname{exph}_{z}(\zeta)\right) \cdot \chi\left(\frac{|\zeta|^{2}}{\varepsilon^{2}}\right) \mathrm{d} \lambda(\zeta), \quad \varepsilon>0 \\
& \quad \Phi(z, w)=\int_{\zeta \in T_{z}^{1,0} M} \phi\left(\operatorname{exph}_{z}(w \zeta)\right) \cdot \chi\left(|\zeta|^{2}\right) \mathrm{d} \lambda(\zeta)
\end{aligned}$$
which is smooth on $M \times\left\{w \in \mathbb{C}\left|0<|w|<\varepsilon_{0}\right\}\right.$ for some $\varepsilon_{0}>0$. Then for $w \in \mathbb{C}$ with $|w|=\varepsilon$, we have $\phi_{\varepsilon}(z)=\Phi(z, w)$. In the following, we need to compute $(d J d \Phi)^{(1,1)}$ over the set $M \times\left\{0<|w|<\varepsilon_{0}\right\}$ and estimate the negative part when $|w|$ is small.

In (C.27), we make the change of variables $s=w^{-1} \rho(p, w \zeta)$, hence we can write $\operatorname{exph}_{\mathrm{p}}(\mathrm{w} \zeta)=\mathrm{L}_{\mathrm{p}}(\mathrm{z}, \mathrm{ws})$. By (C.20) and (C.21), we get
$$\begin{aligned}
s_{m}= & \xi_{m}+\sum_{2 \leq|\alpha| \leq N}\left(\sum_{k} d_{\alpha m k} w^{|\alpha|-1} \xi^{\alpha} \bar{z}_{k}+\sum_{j, k} e_{\alpha m j k} w^{|\alpha|-1} \xi^{\alpha} z_{j} \bar{z}_{k}\right) \\
& +O\left(\bar{z}^{2},|z|^{3}, w^{N-1} \xi^{N-1}\right) w \xi^{2} .
\end{aligned}$$
Hence,
$$\begin{aligned}
\xi_{m}= & s_{m}-\sum_{2 \leq|\alpha| \leq N}\left(\sum_{k} d_{\alpha m k} w^{|\alpha|-1} s^{\alpha} \bar{z}_{k}+\sum_{j, k} e_{\alpha j k m} w^{|\alpha|-1} s^{\alpha} z_{j} \bar{z}_{k}\right) \\
& +O\left(\bar{z}^{2},|z|^{3}, w^{N-1} s^{N-1}\right) w s^{2}
\end{aligned}$$
and $\xi=s+O\left(w^{N} s^{N+1}\right)$ for $z=0$. Plugging into (C.27), we get
$$\Phi(z, w)=\int_{\mathbb{C}^{n}} \phi\left(L_{p}(z, w s)\right) \chi(A(z, w, s)) B(z, w, s) d \lambda(s) .$$
where
$$\begin{aligned}
& { }^{A(z, w, s)} \\
= & \sum_{1 \leq m \leq n}\left|s_{m}\right|^{2}-\sum_{1 \leq j, k, l, m \leq n} c_{l m j k} z_{j} \bar{z}_{k} s_{l} \bar{s}_{m} \\
& -2 R e \sum_{\alpha, k, m} d_{\alpha m k} w^{|\alpha|-1} s^{\alpha} \bar{s}_{m} \bar{z}_{k}-2 R e \sum_{\alpha, j, k, m} e_{\alpha m j k} w^{|\alpha|-1} s^{\alpha} \bar{s}_{m} z_{j} \bar{z}_{k} \\
& +\sum_{\alpha, \beta, j, k, m} d_{\alpha m k} \overline{d_{\beta m j}} w^{|\alpha|-1} w^{|\beta|-1} s^{\alpha} \bar{s}^{\beta} z_{j} \bar{z}_{k} \\
& +O\left(z^{2}, \bar{z}^{2},|z|^{3},|w|^{N-1}|s|^{N-1}\right)|w||s|^{3},
\end{aligned}$$
$$\begin{aligned}
& B(z, w, s) \\
= & 1-\sum_{1 \leq j, k, l \leq n} c_{l l j k} z_{j} \bar{z}_{k} \\
& -2 R e \sum_{\alpha, k, m} d_{\alpha m k} w^{|\alpha|-1} \alpha_{m} s^{\alpha-1_{m}} \bar{z}_{k} \\
& -2 R e \sum_{\alpha, j, k, m} e_{\alpha m j k} w^{|\alpha|-1} \alpha_{m} s^{\alpha-1_{m}} z_{j} \bar{z}_{k} \\
& +\sum_{\alpha, \beta, j, k, l, m} d_{\alpha m k} \bar{d}_{\beta l j} w^{|\beta|-1} \alpha_{m} \beta_{l} s^{\alpha-1_{m}} \bar{s}^{\beta-1_{l}} z_{j} \bar{z}_{k} \\
& +O\left(z^{2}, \bar{z}^{2},|z|^{3},|w|^{N-1}|s|^{N-1}\right)|w||s|
\end{aligned}$$
here $\left(1_{m}\right)_{1 \leq m \leq n}$ denotes the standard basis of $\mathbb{Z}^{n}$, hence $s^{1_{m}}=s_{m}$.
Let $\left(M, g_{J}, J, F\right)$ be a $2 n$-dimensional almost Hermitian manifold. We have the following lemma (cf. Wang-Zhu [79])

Lemma C.6. Suppose $f$ is a smooth function on $M$, then
$$\begin{aligned}
d J d f & =(d J d f)^{(1,1)}+(d J d f)^{(2,0)+(0,2)} \\
& =2 \sqrt{-1} f_{i \bar{j}} \theta^{i} \wedge \bar{\theta}^{j}-2 \sqrt{-1}\left(\overline{N_{\bar{i} \bar{j}}^{k}} \bar{f}_{k} \theta^{i} \wedge \theta^{j}+N_{\bar{i} \bar{j}}^{k} f_{k} \bar{\theta}^{i} \wedge \bar{\theta}^{j}\right),
\end{aligned}$$
where $\partial_{J} f=\sum f_{k} \theta^{k}, \bar{\partial}_{J} f=\sum \bar{f}_{k} \bar{\theta}^{k}, N \frac{k}{i j}$ is the Nijenhuis tensor $J$ which is independent of the choice of a metric.

By Lemma 2.1 of Diederich-Sukhov [14], for any $p \in M$, there exists a neighborhood $U$ of $p$ and a coordinate map $z: U \rightarrow \mathbb{B}$ such that $z(p)=0$ and $d z(p) \circ J(p) \circ d z^{-1}(0)=J_{s t}$. Moreover, $z_{*}(J):=d z \circ J \circ d z^{-1}$ satisfies $\left\|z_{*}(J)-J_{s t}\right\|_{C^{\alpha}(\overline{\mathbb{B}})} \leq \lambda_{0}$ for every $\alpha \geq 0$ and $\lambda_{0}>0$, where $\mathbb{B}$ is the unit ball in $\mathbb{C}^{n}$. It is easy to see that
$$\left.\partial_{J} f\right|_{p}=\left.\partial_{J_{s t}} f\right|_{p},\left.\bar{\partial}_{J} f\right|_{p}=\left.\bar{\partial}_{J_{s t}} f\right|_{p},$$
and
$$\left.d J d f\right|_{p}=\left.2 \sqrt{-1} \partial_{J} \bar{\partial}_{J} f\right|_{p}=\left.2 \sqrt{-1} \partial_{J_{s t}} \bar{\partial}_{J_{s t}} f\right|_{p} .$$
For more details, please see Diederich-Sukhov [14]. Fix a point $p \in M$, choose a complex coordinate chart $U_{p}=\left\{\left(z_{1}, \cdots, z_{n}\right) \in \mathbb{C}^{n}\right\}$ around $p$. Define two almost complex structures on $U_{p} \times \mathbb{C}$ as follows:
$$\tilde{J}(z)=J(z) \oplus J_{s t}, \quad \tilde{J}_{0}=\tilde{J}(0)=J(0) \oplus J_{s t} .$$
It is easy to see that $\tilde{J}_{0}$ is integrable. Return to (C.27),
$$\Phi(z, w)=\int_{\zeta \in T_{z}^{1,0} M} \phi\left(\operatorname{exph}_{z}(w \zeta)\right) \cdot \chi\left(|\zeta|^{2}\right) \mathrm{d} \lambda(\zeta) .$$
The change of variable $y=\operatorname{exph}_{z}(w \zeta)$ expresses $w \zeta$ as a smooth function of $y, z$ in neighborhood of the diagonal in $M \times M$. Hence $\Phi$ is a smooth over $M \times\left\{0<|w|<\varepsilon_{0}\right\}$ for some $\varepsilon_{0}>0$. By (C.30), we are going to compute $\partial_{\tilde{J}} \Phi, \bar{\partial}_{\tilde{J}} \Phi$ and $\partial_{\tilde{J}} \bar{\partial}_{\tilde{J}} \Phi$. Note that
$$\left.\left.(d \tilde{J} d \Phi(z, w))^{(1,1)}\right|_{(0, w)}=\left.\left(d \tilde{J}_{0} d \Phi(z, w)\right)^{(1,1)}\right|_{(0, w)}=2 \sqrt{-1} \partial_{\tilde{J}_{0}} \tilde{\partial}_{\tilde{J}_{0}} \Phi(z, w)\right)\left.\right|_{(0, w)},$$
and
$$\begin{aligned}
\left.(d \tilde{J} d \Phi(z, w))^{(2,0)+(0,2)}\right|_{(0, w)}= & -2 \sqrt{-1}\left(\left.\overline{N_{\overline{i j}}^{k}} \frac{\partial}{\partial \bar{z}_{k}} \Phi(z, w)\right|_{(0, w)} d z_{i} \wedge d z_{j}\right. \\
& \left.+\left.N \frac{k}{i \bar{j}} \frac{\partial}{\partial z_{k}} \Phi(z, w)\right|_{(0, w)} d \bar{z}_{i} \wedge d \bar{z}_{j}\right) .
\end{aligned}$$
By Lemma C.6, we have
$$\begin{aligned}
d \tilde{J} d \Phi(z, w))\left.^{(1,1)}\right|_{(0, w)}= & \left.d \tilde{J}_{0} d \Phi(z, w)\right)\left.^{(1,1)}\right|_{(0, w)} \\
= & \left.2 \sqrt{-1} \partial_{\tilde{J}_{0}} \tilde{\partial}_{\tilde{J}_{0}} \Phi(z, w)\right)\left.\right|_{(0, w)} \\
= & 2 \sqrt{-1}\left(\left.\frac{\partial^{2}}{\partial z_{i} \partial \bar{z}_{j}} \Phi(z, w)\right|_{(0, w)} d z_{i} \wedge d \bar{z}_{j}\right. \\
& +\left.\frac{\partial^{2}}{\partial z_{i} \partial \bar{w}} \Phi(z, w)\right|_{(0, w)} d z_{i} \wedge d \bar{w} \\
& +\left.\frac{\partial^{2}}{\partial w \partial \bar{z}_{j}} \Phi(z, w)\right|_{(0, w)} d w \wedge d \bar{z}_{j} \\
& +\left.\frac{\partial^{2}}{\partial w \partial \bar{w}} \Phi(z, w)\right|_{(0, w)} d w \wedge d \bar{w},
\end{aligned}$$
and
$$\begin{aligned}
\left.(d \tilde{J} d \Phi(z, w))^{(2,0)+(0,2)}\right|_{(0, w)}= & \left.\left(d \tilde{J}_{0} d \Phi(z, w)\right)^{(2,0)+(0,2)}\right|_{(0, w)} \\
= & \left.(d J(p) d \Phi(z, w))^{(2,0)+(0,2)}\right|_{(0, w)} \\
= & -2 \sqrt{-1}\left(\left.\overline{N_{\overline{i j}}^{k}} \frac{\partial}{\partial \bar{z}_{k}} \Phi(z, w)\right|_{(0, w)} d z_{i} \wedge d z_{j}\right. \\
& \left.+\left.N \frac{k}{i j} \frac{\partial}{\partial z_{k}} \Phi(z, w)\right|_{(0, w)} d \bar{z}_{i} \wedge d \bar{z}_{j}\right) .
\end{aligned}$$
By the above observation, Proposition 3.8 of Demailly [12] can be generalized to almost Hermitian $2 n$-manifolds as follows

Proposition C.7. For any integer $N \geq 2$ and any $(\varrho, \eta) \in T_{z}^{1,0} U_{p} \times \mathbb{C}$, at $(z, w) \in U_{p} \times \mathbb{C}$ we have the following estimates
$$\partial_{\tilde{J}_{0}} \Phi_{(p, w)} \cdot(\varrho, \eta)=\int_{\zeta \in T_{p}^{1,0} M} \partial_{\tilde{J}_{0}} \phi_{\left(\operatorname{exph}_{z}(\mathrm{w} \zeta)\right)} \cdot \tau \chi\left(|\zeta|^{2}\right) d \lambda(\zeta)+O\left(|w|^{N}\right)(\varrho, \eta)$$
$$\begin{aligned}
\partial_{\tilde{J}} \bar{\partial}_{\tilde{J}} \Phi_{(p, w)}(\varrho \wedge \bar{\varrho}, \eta \wedge \bar{\eta})= & \partial_{\tilde{J}_{0}} \bar{\partial}_{\tilde{J}_{0}} \Phi_{(p, w)}(\varrho \wedge \bar{\varrho}, \eta \wedge \bar{\eta}) \\
= & \int_{\zeta \in T_{p}^{1,0} M} \partial_{\tilde{J}_{0}} \bar{\partial}_{\tilde{J}_{0}} \phi \cdot\left(\tau \wedge \bar{\tau}+|w|^{2} V\right)_{\operatorname{exph}_{p}(w \zeta)} \chi\left(|\zeta|^{2}\right) d \lambda(\zeta) \\
& +O\left(|w|^{N-1}\right)(\varrho \wedge \bar{\varrho}, \eta \wedge \bar{\eta}),
\end{aligned}$$
where $\tau$ is a vector field over $T M^{1,0}, V$ is a $(1,1)$-vector field, both depending smoothly on the parameters $p, w$ and linearly or quadratically on $\varrho, \eta$. The vector fields $\tau, V$ are given at $y=\operatorname{exph}_{p}(w \zeta)$ by
$$\begin{aligned}
& \tau_{y}=\partial_{J(p)} \operatorname{exph}_{(p, w \zeta)}\left(\varrho^{h}+\eta \zeta^{v}+|w|^{2} \Xi_{y}^{v}\right), \\
& V_{y}=\partial_{J(p)} \operatorname{exph}_{(p, w \zeta)}\left(U^{v}-|w|^{2} \Xi^{v} \wedge \overline{\Xi^{v}}\right)_{y},
\end{aligned}$$
where $\varrho^{h}, \zeta^{v} \in T(T M)_{(p, w \zeta)}$ are respectively the horizontal lifting of $\varrho$ with respect to the Chern connection ∇ with respect to $h$ and $J(p)$, and the vertical vector associated to $\zeta$, and where $\epsilon$ can be arbitrarily small. Here, $\Xi, U$ is defined by
$$\begin{aligned}
& \Xi_{y}(\zeta)=\sum_{\alpha, j, l, m} \frac{1}{\chi\left(|\zeta|^{2}\right)} \frac{\partial}{\partial \bar{\zeta}_{l}}\left(\chi_{1}\left(|\zeta|^{2}\right) \bar{\zeta}^{\alpha-1_{m}}\right) \overline{d_{\alpha l j}} \frac{\alpha_{m}}{|\alpha|} \bar{w}^{|\alpha|-2} \varrho_{j} \frac{\partial}{\partial z_{m}}, \\
& U_{y}(\zeta)=\sum_{l, m} \frac{1}{2}\left(U_{m, l}(\zeta)+\overline{U_{l, m}}(\zeta)\right) \frac{\partial}{\partial z_{m}} \wedge \frac{\partial}{\partial \bar{z}_{l}}, \\
& U_{m, l}(\zeta)=-\frac{\chi_{1}\left(|\zeta|^{2}\right)}{\chi\left(|\zeta|^{2}\right)}\left\{\sum_{j, k} c_{l m j k} \varrho_{j} \bar{\varrho}_{k}+2 \sum_{\alpha, j, k} e_{\alpha m j k} w^{|\alpha|-1} \frac{\alpha_{l}}{|\alpha|} \zeta^{\alpha-1_{t}} \varrho_{j} \bar{\varrho}_{k}\right. \\
& \left.+2 \sum_{\alpha, k} d_{\alpha m k}(|\alpha|-1) w^{|\alpha|-2} \frac{\alpha_{l}}{|\alpha|} \zeta^{\alpha-1_{t}} \eta \bar{\varrho}_{k}+\sum_{\alpha, \beta, j, k} d_{\alpha m k} \overline{d_{\beta l j}} w^{|\alpha|-2} \bar{w}^{|\beta|-2} \zeta^{\alpha} \bar{\zeta}^{\beta} \varrho_{j} \bar{\varrho}_{k}\right\} .
\end{aligned}$$

Here,
$$\chi_{1}(t)=\int_{+\infty}^{t} \chi(u) d u$$
and $c_{l m j k}, d_{\beta l j}, e_{\alpha m j k}$ are defined in Appendix C.1. Moreover, $\alpha, \beta \in \mathbb{N}^{n}$ run over all multi-indices such that $2 \leq|\alpha|,|\beta| \leq N$.

Proof. Our approach is similar to the proof of Proposition 3.8 in Demailly [12]. A brute force differentiation of (C.30) gives
$$\begin{aligned}
\partial_{\tilde{J}_{0}} \Phi_{(p, w)} \cdot(\varrho, \eta)= & \int_{\mathbb{C}^{n}} \partial_{\tilde{J}_{0}}\left(\phi \circ L_{p}\right)_{(0, w s)} \cdot(\varrho, \eta) \chi(A(0, w, s)) B(0, w, s) d \lambda(s) \\
& -\int_{\mathbb{C}^{n}}\left(\phi \circ L_{p}\right)_{(0, w s)} E_{(w, s)} \cdot(\varrho, \eta) d \lambda(s),
\end{aligned}$$
where
$$E_{(w, s)}=-\partial_{\tilde{J}_{0}}(\chi(A(z, w, s)) B(z, w, s))_{(z, w)} .$$
We find
$$\begin{aligned}
E_{(w, s)} \cdot(\varrho, \eta)= & \sum_{l, m} \frac{\partial^{2}}{\partial \bar{s}_{l} \partial s_{m}}\left(\chi\left(|s|^{2}\right) \sum_{\alpha, j} \overline{d_{\alpha l j}} \bar{w}^{|\alpha|-1} \frac{\alpha_{m}}{|\alpha|} \bar{s}^{\alpha-1_{m}} \varrho_{j}\right) \\
& +O\left(|w|^{N-1}|s|^{N}\right) \cdot(\varrho, \eta),
\end{aligned}$$
$$\begin{aligned}
\partial_{\tilde{J}_{0}} \bar{\partial}_{\tilde{J}_{0}} \Phi_{(p, w)} \cdot(\varrho \wedge \bar{\varrho}, \eta \wedge \bar{\eta})= & \int_{\mathbb{C}^{n}} \partial_{\tilde{J}_{0}} \bar{\partial}_{\tilde{J}_{0}}\left(\phi \circ L_{p}\right)_{(0, w s)} \cdot(\varrho \wedge \bar{\varrho}, \eta s \wedge \overline{\eta s}) \\
& \cdot \chi(A(0, w, s)) B(0, w, s) d \lambda(s) \\
& -\int_{\mathbb{C}^{n}} \bar{\partial}_{\tilde{J}_{0}}\left(\phi \circ L_{p}\right)_{(0, w s)} \cdot(\bar{\varrho}, \overline{\eta s}) \cdot E_{(w, s)} \cdot(\varrho, \eta s) d \lambda(s) \\
& -\int_{\mathbb{C}^{n}} \partial_{\tilde{J}_{0}}\left(\phi \circ L_{p}\right)_{(0, w s)} \cdot(\varrho, \eta s) \cdot \overline{E_{(w, s)}} \cdot(\bar{\varrho}, \overline{\eta s}) d \lambda(s) \\
& -\int_{\mathbb{C}^{n}}\left(\phi \circ L_{p}\right)_{(0, w s)} \cdot F_{(w, s)} \cdot(\varrho \wedge \bar{\varrho}, \eta s \wedge \overline{\eta s}) d \lambda(s),
\end{aligned}$$
where
$$F_{(w, s)}=-\partial_{\tilde{J}_{0}} \bar{\partial}_{\tilde{J}_{0}}(\chi(A(z, w, s)) B(z, w, s))_{(z, w)} .$$
We find
$$\begin{aligned}
& F_{(w, s)} \cdot(\varrho \wedge \bar{\varrho}, \eta s \wedge \overline{\eta s}) \\
& \quad=\sum_{l, m} \frac{\partial^{2}}{\partial \bar{s}_{l} \partial s_{m}}\left(\chi_{1}\left(|s|^{2}\right) \sum_{j, k} c_{l m j k} \varrho_{j} \bar{\varrho}_{k}\right) \\
& \quad+2 \operatorname{Re}\left\{\sum_{l, m} \frac{\partial^{2}}{\partial \bar{s}_{l} \partial s_{m}}\left(\chi_{1}\left(|s|^{2}\right) \sum_{\alpha, j, k} e_{\alpha m j k} w^{|\alpha|-1} \frac{\alpha_{l}}{|\alpha|} s^{\alpha-1_{l}} \varrho_{j} \bar{\varrho}_{k}\right)\right. \\
& \left.\quad+\sum_{l, m} \frac{\partial^{2}}{\partial s_{l} \partial \bar{s}_{m}}\left(\chi_{1}\left(|s|^{2}\right) \sum_{\alpha, k} d_{\alpha m k}(|\alpha|-1) w^{|\alpha|-2} \frac{\alpha_{l}}{|\alpha|} \bar{s}^{\alpha-1_{l}} \eta \bar{\varrho}_{k}\right)\right\}
\end{aligned}$$
$$\begin{aligned}
& -\sum_{l, m} \frac{\partial^{2}}{\partial \bar{s}_{l} \partial s_{m}}\left(\chi_{1}\left(|s|^{2}\right) \sum_{\alpha, k} d_{\alpha m k} \overline{d_{\beta l j}} w^{|\alpha|-1} \bar{w}^{|\beta|-1} s^{\alpha} \bar{s}^{\beta} \varrho_{j} \bar{\varrho}_{k}\right) \\
& +O\left(|w|^{N-2}|s|^{N}\right)(\varrho \wedge \bar{\varrho}, \eta s \wedge \overline{\eta s}) .
\end{aligned}$$
In all these expansions, the remainder terms $O(\cdot)$ involve uniform constants when the origin x of coordinates belongs to a compact subset of a coordinate patch. When $U_{p}$ is very small, without loss of generality, we may assume that $\phi$ is strictly $J$-convex (and $J(p)$ -convex). By the mean value properties of plurisubharmonic functions (cf. L. Simon [69]), we have
$$\int_{|s|<1}|\phi(p+w s)| d \lambda(s) \leq C(1+\log |w|)$$
locally uniformly in $p$. An integration by parts with compact supports yields
$$\int_{|s|<1} \partial_{\tilde{J}_{0}}\left(\phi \circ L_{p}\right)_{(0, w s)} O(|w|) d \lambda(s)=\int_{|s|<1} \phi \circ L_{p}(0, w s) d \lambda(s)=O(\log |w|) .$$
Hence, the remainder term $O\left(|w|^{N-1}\right)$ in $E_{(w, s)}$ gives contributions of order at most $O\left(|w|^{N-1} \log |w|\right)$ in $\partial_{\tilde{J}_{0}} \Phi$ as $|w|$ tends to 0; the remainder terms $O\left(|w|^{N-1}\right)$ in $E_{(w, s)}$ and $O\left(|w|^{N-2}\right)$ in $F_{(w, s)}$ give contributions of order at most $O\left(|w|^{N-2} \log |w|\right)$ in $\partial_{\tilde{J}_{0}} \bar{\partial}_{\tilde{J}_{0}} \Phi$ as $|w|$ tends to 0.

By (C.34), an integration by parts in (C.33) gives
$$\begin{aligned}
\partial_{\tilde{J}_{0}} \Phi_{(p, w)} \cdot(\varrho, \eta)= & \int_{\mathbb{C}^{n}} \partial_{J(p)}\left(\phi \circ L_{p}\right)\left\{(\varrho, \eta s)+|w|^{2}(0, \Xi)\right\} \\
& \chi(A(0, w, s)) B(0, w, s) d \lambda(s) \\
& +O\left(|w|^{N-1} \log |w|\right) \cdot(\varrho, \eta),
\end{aligned}$$
with
$$\Xi(\zeta)=\sum_{\alpha, j, l, m} \frac{1}{\chi\left(|s|^{2}\right)} \frac{\partial}{\partial \bar{s}_{l}}\left(\chi_{1}\left(|s|^{2}\right) \bar{s}^{\alpha-1_{m}}\right) \overline{d_{\alpha l j}} \frac{\alpha_{m}}{|\alpha|} \bar{w}^{|\alpha|-2} \varrho_{j} \frac{\partial}{\partial z_{m}} .$$
The choice $\chi(t)=\frac{C}{(1-t)^{2}} \exp \left(\frac{1}{t-1}\right)$ for $t<1$ gives $\chi_{1}(t)=-C \exp \left(\frac{1}{t-1}\right)$, so
$$\chi_{1}(t) / \chi(t)=(1-t)^{2}$$
is smooth and bounded, and our vector field $\Xi(\zeta)$ is smooth. We can write
$$\tau=d L_{p}(0, w s)\left(\varrho, \eta s+|w|^{2} \Xi(\zeta)\right) .$$
Since
$$\operatorname{exph}_{z}(\zeta)=L_{p}\left(z, \rho_{p}(z, \xi)\right), \quad \rho_{p}(0, \xi)=\xi+O\left(\xi^{N+1}\right),$$
and
$$\partial_{J(p)} \rho_{p}(0, \xi)=d \xi+O\left(\xi^{N}\right) d \xi$$
by Proposition C.4, we infer that the $(1,0)$-differential of exph at $(p, \zeta) \in T^{1,0} M$ is
$$\partial_{J(p)} \operatorname{exph}_{(\mathrm{p}, \zeta)}=\mathrm{dL}_{\mathrm{p}}(0, \xi)+\mathrm{O}\left(\xi^{\mathrm{N}}\right) \mathrm{d} \xi$$
modulo the identification of the tangent spaces $T\left(T^{1,0} M\right)_{(p, \xi)}$ and $T\left(T \mathbb{C}^{n}\right)_{(0, \xi)}$ given by the coordinates $(z, \xi)$ on $T^{1,0} M$. However, these coordinates are precisely those which realize the splitting
$$T\left(T^{1,0} M\right)_{(p, \xi)}=\left(T_{p}^{1,0} M\right)^{h} \oplus\left(T_{p}^{1,0} M\right)^{v}$$
with respect to the Chern connection on $U_{p}$. Since $s=\xi+O\left(w^{N} \xi^{N+1}\right)$ and $\xi=\zeta$ at $z=0$, we get
$$\tau=\partial_{J(p)} \operatorname{exph}_{(p, w \zeta)}\left(\varrho^{h}+\eta \zeta^{v}+|w|^{2} \Xi(\zeta)^{v}\right)+O\left(|w|^{N}|\zeta|^{N}\right) .$$
We can drop the terms $O\left(|w|^{N}\right)$ in $\tau$ because
$$\begin{aligned}
\int_{|\zeta|<1} \partial_{J(p)} \phi\left(\operatorname{exph}_{p}(w \zeta)\right) d \lambda(\zeta) & =\frac{1}{|w|^{2 n}} \int_{|\zeta|<|w|} \partial_{J(p)} \phi\left(\operatorname{exph}_{p}(\zeta)\right) d \lambda(\zeta) \\
& =O\left(|w|^{-1}\right)
\end{aligned}$$
By (C.34) and (C.37), an integration by parts in (C.35) gives
$$\begin{aligned}
\partial_{\tilde{J}_{0}} \bar{\partial}_{\tilde{J}_{0}} \Phi_{(p, w)}(\varrho, \eta) \wedge \overline{(\varrho, \eta)}= & \int_{\mathbb{C}^{n}} \partial_{\tilde{J}_{0}} \bar{\partial}_{\tilde{J}_{0}}\left(\phi \circ L_{p}\right)_{(0, w s)} \cdot\{(\varrho, \eta s) \wedge \overline{(\varrho, \eta s)} \\
& +|w|^{2}(0, \Xi(\zeta)) \wedge \overline{(\varrho, \eta s)}+|w|^{2}(\varrho, \eta s) \wedge \overline{(0, \Xi(\zeta))} \\
& +|w|(0, U)\} \chi(A(0, w, s)) B(0, w, s) d \lambda(s) \\
& +O\left(|w|^{N-2} \log |w|\right)(\varrho, \eta) \wedge \overline{(\varrho, \eta)},
\end{aligned}$$
where
$$U(\zeta)=\sum_{l, m} \frac{1}{2}\left(U_{m, l}+\overline{U_{l, m}}\right) \frac{\partial}{\partial z_{m}} \wedge \frac{\partial}{\partial z_{l}}$$
is smooth,
$$\begin{aligned}
U_{m, l}(\zeta)= & -\frac{\chi_{1}\left(|s|^{2}\right)}{\chi\left(|s|^{2}\right)} \cdot\left\{\sum_{j, k} c_{l m j k} \varrho_{j} \bar{\varrho}_{k}+2 \sum_{\alpha, j, k} e_{\alpha m j k} w^{|\alpha|-1} \frac{\alpha_{l}}{|\alpha|} s^{\alpha-1_{l}} \varrho_{j} \bar{\varrho}_{k}\right. \\
& \left.+2 \sum_{\alpha, k} d_{\alpha m k}(|\alpha|-1) w^{|\alpha|-2} \frac{\alpha_{l}}{|\alpha|} s^{\alpha-1_{l}} \eta \bar{\varrho}_{k}\right\} \\
& +\sum_{\alpha, \beta, j, k} d_{\alpha m k} \bar{d}_{\beta l j} w^{|\alpha|-1} \bar{w}^{|\beta|-1} s^{\alpha} \bar{s}^{\beta} \varrho_{j} \bar{\varrho}_{k} .
\end{aligned}$$
We can write
$$\begin{aligned}
& (\varrho, \eta s) \wedge \overline{(\varrho, \eta s)}+|w|^{2}(0, \Xi(\zeta)) \wedge \overline{(\varrho, \eta s)}+|w|^{2}(\varrho, \eta s) \wedge \overline{(0, \Xi(\zeta))}+|w|(0, U) \\
= & \left(\varrho, \eta s+|w|^{2} \Xi(\zeta) \wedge \overline{\left(\varrho, \eta s+|w|^{2} \Xi(\zeta)\right)}+\left(0, U-|w|^{2} \Xi(\zeta) \wedge \overline{\Xi(\zeta)}\right)\right) .
\end{aligned}$$
Therefore (C.41) implies the formula in Proposition C. 7 with
$$V=d L_{p(0, w s)}\left(0, U-|w|^{2} \Xi \wedge \bar{\Xi}\right) .$$
Finally, we get
$$V=\partial_{\tilde{J}_{0}} \operatorname{exph}_{(p, w \zeta)}\left(U^{v}-|w|^{2} \Xi^{v} \wedge \overline{\Xi^{v}}\right)+O\left(|w|^{N}|\zeta|^{N}\right) .$$

Also, we can get
$$\begin{aligned}
\int_{|\zeta|<1} \partial_{\tilde{J}_{0}} \bar{\partial}_{\tilde{J}_{0}} \operatorname{exph}_{p}(w \zeta) d \lambda(\zeta) & =\frac{1}{|w|^{2 n}} \int_{|\zeta|<|w|} \partial_{\tilde{J}_{0}} \bar{\partial}_{\tilde{J}_{0}} \operatorname{exph}_{p}(\zeta) d \lambda(\zeta) \\
& =O\left(|w|^{-2}\right) .
\end{aligned}$$
After substituting $\zeta$ to $s$ in the formal expression of $\Xi$ and $U$, we get precisely the formula given in Proposition C.7. As done in the proof of Proposition 3.8 in [12], the remainder term $O\left(|w|^{N-1} \log |w|\right)$ in (C.38) (resp. $O\left(|w|^{N-2} \log |w|\right)$ in (C.41) ) is in fact of the type $O\left(|w|^{N}\right)$ (resp. $O\left(|w|^{N-1}\right)$ ). To see this, we increase $N$ by two units and estimate the additional terms in the expansions, due to the contribution of all multi-indices $\alpha$ with $|\alpha|=N+1$ or $N+2$. It is easily seen that the additional terms in $\Xi$ and $U$ are $O\left(|w|^{N-1}\right)$, so they are $O\left(|w|^{N+1}\right)$ in $\tau$ and $|w|^{2} V$. The contribution of these terms to $\partial_{J(p)} \Phi_{(p, w)}$ and $\partial_{J(p)} \bar{\partial}_{J(p)} \Phi_{(p, w)}$ are thus of the forms
$$\begin{gathered}
\int_{|\zeta|<1} \partial_{J(p)} \phi\left(\operatorname{exph}_{p}(w \zeta)\right) O\left(|w|^{N+1}\right) d \lambda(\zeta)=O\left(|w|^{N}\right) \\
\int_{|\zeta|<1} \partial_{J(p)} \bar{\partial}_{J(p)} \phi\left(\operatorname{exph}_{p}(w \zeta)\right) O\left(|w|^{N+1}\right) d \lambda(\zeta)=O\left(|w|^{N-1}\right)
\end{gathered}$$
This completes the proof of Proposition C. 7. \(\square\)

By Lemma C.6, (C.38) and (C.39), we have
Corollary C.8. Let $N=2$, we have
$$\begin{aligned}
\left(\frac{1}{2} d \tilde{J} d \Phi(z, w)_{(0, w)}\right)^{(0,2)}(\bar{\varrho}, 0) \wedge(\bar{\varrho}, 0)= & \sqrt{-1} \int_{\zeta \in T_{p}^{1,0} M}-\sum_{k} \frac{\partial}{\partial z_{k}}\left(\phi \circ L_{p}(z, w)\right) N^{k}(p) \\
& \left\{\left[(\bar{\varrho}, 0)+|w|^{2}(0, \bar{\Xi})\right] \wedge\left[(\bar{\varrho}, 0)+|w|^{2}(0, \bar{\Xi})\right]\right\}_{(0, w)} \\
& +O\left(|w|^{2}\right) \\
= & \sqrt{-1} \int_{\zeta \in T_{p}^{1,0} M}-\sum_{k, i, j} \frac{\partial}{\partial z_{k}}\left(\phi \circ L_{p}(z, w)\right) N_{\bar{i} j}^{k} \bar{\varrho}_{i} \wedge \bar{\varrho}_{j} \\
& +O(|w|) .
\end{aligned}$$

\section*{C. 3 Regularization of closed positive (1, 1)-currents on tamed almost complex 4-manifolds}

In this subsection, we devote to studying regularization of closed positive $(1,1)$ currents on tamed almost complex 4-manifolds. It is similar to J.-P. Demailly's result [11, 12] that we will see that it is always possible to approximate a closed positive almost complex $(1,1)$ current $T$ on almost Hermitian 4-manifold $\left(M, g_{J}, J, F\right)$ by smooth closed real currents admitting a small negative part, and that this negative part can be estimated in terms of the Lelong numbers of $T$ and geometry of $M$. Let $\left(M, g_{J}, J, F\right)$ be an almost Hermitian 4-manifold tamed by a symplectic form $\omega_{1}=F+d_{J}^{-}(v+\bar{v})$. In general, $\partial_{J} \bar{\partial}_{J} f$ is not $d$-closed since $J$ is not integrable. In Section 2, we have defined an operator
$$\mathcal{D}_{J}^{+}: C^{\infty}(M) \longrightarrow \Omega_{J}^{+}(M) .$$

For any $f \in C^{\infty}(M), \mathcal{D}_{J}^{+}(f) \in \Omega_{J}^{+}(M)$ is $d$-closed. Let $T$ be a closed strictly positive current of bidegree $(1,1)$ on $\left(M, g_{J}, J, F\right)$ tamed by $\omega_{1}$. Let $\widetilde{\omega}$ be a smooth closed (1, 1)-form representing the same $\mathcal{D}_{J}^{+}$-cohomology class as $T$ and let $\psi=\mathcal{D}_{J}^{+}(f)$ be a quasi- $J$-positive (1, 1)-current (that is, a (1, 1)-form which is locally the sum of a positive (1, 1)-current and a smooth ( 1,1 )-form) such that $T=\widetilde{\omega}+\mathcal{D}_{J}^{+}(f)$. Such a function $f$, is called a quasi-$J$-plurisubharmonic function. Such a decomposition exists since we can always find an open covering $\left(\Omega_{k}\right)$ where $\Omega_{k}$ are $J$-pseudoconvex domains such that $T=\mathcal{D}_{J}^{+}\left(f_{k}\right)$ over $\Omega_{k}$ (see Lemma A. 11 or Theorem A. 31 in Appendix A), and costruct a global $f=\sum \varsigma_{k} f_{k}$ by means of a partion of unity $\left(\varsigma_{k}\right)$ (note that $f-f_{k}$ is smooth on $\Omega_{k}$ ). Notice that for any $p \in M$, there exists a $J$-compatible symplectic form $\omega_{p}$ on a small neighborhood $U_{p}$ which is $J$-pseudoconvex. By the construction of $\omega_{p}$ (cf. Lejmi [54]), there exists real 1-form $\alpha$ on $U_{p}$ such that $\omega_{p}=d \alpha$. Hence, by Lemma A. 11 (that is Theorem A. 31 in Appendix A.3), there is a real function $f_{p}$ on $U_{p}$ which is strictly $J$-plurisubharmonic such that $\omega_{p}=\widetilde{\mathcal{D}}_{J}^{+}\left(f_{p}\right)=d \widetilde{\mathcal{W}}\left(f_{p}\right)$ with respect to metric $g_{p}(\cdot, \cdot)=\omega_{p}(\cdot, J \cdot)$. Since $\left(U_{p}, \omega_{p}\right)$ is a symplectic 4-manifold, thus $\widetilde{\mathcal{W}}\left(f_{p}\right)=\mathcal{W}\left(f_{p}\right)$ (see Section 2),
$$\omega_{p}=d \mathcal{W}\left(f_{p}\right)=\mathcal{D}_{J}^{+}\left(f_{p}\right) .$$
Therefore, we have the following lemma,
Lemma C.9. Suppose that $(M, J)$ is an almost complex 4-manifold. For any $p \in M$, there exist a small neighborhood $U_{p}$ and a smooth strictly $J$-plurisubharmonic function $f_{p}$ on $U_{p}$ such that $\mathcal{D}_{J}^{+}\left(f_{p}\right)$ is a strictly positive closed $(1,1)$-form on $U_{p}$.
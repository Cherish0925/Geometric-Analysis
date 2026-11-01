---
retention_scope: session
part: 2
total_parts: 4
---

[Part 2/4 of: Families of singular Kähler–Einstein metrics]

Applying Lemma 2.11 to $X=X_{t}, u=\psi_{t}, v=w=G_{x}$ (recall that $\left.G_{x}\right|_{\partial \mathbb{B}} \equiv 0$ ), we get
$$\int_{\mathbb{B} \cap X_{t}} \psi_{t}\left(d d^{c} G_{x}\right)^{n}=\underbrace{\int_{\mathbb{B} \cap X_{t}} G_{x} d d^{c} \psi_{t} \wedge\left(d d^{c} G_{x}\right)^{n-1}}_{=: I_{t}}+\underbrace{\int_{\partial \mathbb{B} \cap X_{t}} \psi_{t} d^{c} G_{x} \wedge\left(d d^{c} G_{x}\right)^{n-1}}_{=: J_{t}}$$
By Lemma 2.12, in order to get a lower bound for $J_{t}$, it is enough to bound from above the quantity $\int_{\partial \mathbb{B} \cap X_{t}}\left(-\psi_{t}\right) d^{c}\|z\|^{2} \wedge\left(d d^{c}\|z\|^{2}\right)^{n-1}$. Applying (2.9) to $u=-\psi_{t}, v=w=$ $\|z\|^{2}-1$, we find
$$\begin{aligned}
\int_{\partial \mathbb{B} \cap X_{t}}\left(-\psi_{t}\right) d^{c}\|z\|^{2} \wedge\left(d d^{c}\|z\|^{2}\right)^{n-1}= & \int_{\mathbb{B} \cap X_{t}}\left(-\psi_{t}\right)\left(d d^{c}\|z\|^{2}\right)^{n}+ \\
& \int_{\mathbb{B} \cap X_{t}}\left(\|z\|^{2}-1\right) d d^{c} \psi_{t} \wedge\left(d d^{c}\|z\|^{2}\right)^{n-1} \\
\leqslant & \int_{\mathbb{B} \cap X_{t}}\left(-\psi_{t}\right)\left(d d^{c}\|z\|^{2}\right)^{n} \\
\leqslant & C_{1}^{n}\left[\int_{X_{t}}\left(-\varphi_{t}\right) \omega_{t}^{n}+C_{\tau} \cdot V\right],
\end{aligned}$$
where $C_{1}$ is such that $d d^{c}\|z\|^{2} \leqslant C_{1} \omega$ on $\mathbb{B}$ and $C_{\tau}$ is given in (2.5).
We now take care of the most singular term $I_{t}$. Set
$$\gamma_{t}(x):=\int_{\mathbb{B}} d d^{c} \psi_{t} \wedge\left(d d^{c} G_{x}\right)^{n-1} \wedge\left[X_{t}\right]$$
so that $\mu:=\gamma_{t}^{-1} d d^{c} \psi_{t} \wedge\left(d d^{c} G_{x}\right)^{n-1} \wedge\left[X_{t}\right]$ is a probability measure on $\mathbb{B}$ (depending on $x$ ). We claim that for any $x \in \mathbb{B}$ there exists a constant $v>0$ independent of $t$ and $x$ such that $1 \leqslant \gamma_{t}<v$. The uniform upper bound follows from the same computations in the proof of Proposition 2.3. By (2.7) we can infer that
$$\begin{aligned}
\int_{\mathbb{B}} d d^{c} \psi_{t} \wedge\left(d d^{c} G_{x}\right)^{n-1} \wedge\left[X_{t}\right] & \geqslant \int_{\mathbb{B}} d d^{c}\|z\|^{2} \wedge\left(d d^{c} G_{x}\right)^{n-1} \wedge\left[X_{t}\right] \\
& \geqslant v\left(\left(d d^{c} G_{x}\right)^{n-1} \wedge\left[X_{t}\right], x\right) \\
& \geqslant v\left(\left[X_{t}\right], x\right)=m\left(X_{t}, x\right) \geqslant 1
\end{aligned}$$
In the second inequality we used the fact that $r \rightarrow \frac{1}{r^{2}} \int_{\mathbb{B}_{r}} d d^{c}\|z\|^{2} \wedge T$ is decreasing to $v(T, x)$ when $r \downarrow 0$ (see (2.2)). The first equality follows from (2.3) while the second one comes from Thie's theorem. Recall that the origin of $\mathbb{B}$ is identified with the point $x$.

We now use Jensen's formula and (2.8) to obtain
$$\begin{aligned}
\exp \left(-\alpha I_{t}(x)\right) & =\exp \left(\int_{z \in \mathbb{B}}-\alpha \gamma_{t} G_{x} d \mu\right) \\
& \leqslant \frac{1}{\gamma_{t}} \int_{z \in \mathbb{B}} e^{-\alpha \gamma_{t} G_{x}} d d^{c} \psi_{t} \wedge\left(d d^{c} G_{x}\right)^{n-1} \wedge\left[X_{t}\right] \\
& =\frac{1}{\gamma_{t}} \int_{z \in \mathbb{B}} \frac{d d^{c} \psi_{t} \wedge\left(d d^{c} G_{x}\right)^{n-1} \wedge\left[X_{t}\right]}{\left\|\Phi_{x}(z)\right\|^{\alpha \gamma_{t}}} \\
& \leqslant C_{0} \int_{z \in \mathbb{B}} \frac{d d^{c} \psi_{t} \wedge\left(d d^{c}\|z\|^{2}\right)^{n-1} \wedge\left[X_{t}\right]}{\left\|\Phi_{x}(z)\right\|^{\alpha v+2 n-2}},
\end{aligned}$$
where we can assume w.l.o.g. that $\alpha v<2$. By Fubini's theorem, we have
$$\begin{aligned}
\int_{x \in \mathbb{B}_{1 / 2}} e^{-\alpha \psi_{t}} \omega^{n} \wedge\left[X_{t}\right] & \leqslant \int_{x \in \mathbb{B}_{1 / 2}} e^{-\alpha\left(I_{t}+J_{t}\right)} \omega^{n} \wedge\left[X_{t}\right] \\
& \leqslant K \cdot \int_{x \in \mathbb{B}_{1 / 2}} e^{-\alpha I_{t}} \omega^{n} \wedge\left[X_{t}\right] \\
& \leqslant C_{0} \cdot K \cdot \int_{x \in \mathbb{B}_{1 / 2}}\left(\int_{z \in \mathbb{B}} \frac{d d^{c} \psi_{t} \wedge\left(d d^{c}\|z\|^{2}\right)^{n-1} \wedge\left[X_{t}\right]}{\left\|\Phi_{x}(z)\right\|^{\alpha v+2 n-2}}\right) \omega^{n} \wedge\left[X_{t}\right] \\
& \leqslant C_{0} \cdot K \cdot \int_{z \in \mathbb{B}}\left(\int_{x \in \mathbb{B}_{1 / 2}} \frac{\left(d d^{c}\|x\|^{2}\right)^{n} \wedge\left[X_{t}\right]}{\left\|\Phi_{x}(z)\right\|^{\alpha v+2 n-2}}\right) d d^{c} \psi_{t} \wedge\left(d d^{c}\|z\|^{2}\right)^{n-1} \wedge\left[X_{t}\right]
\end{aligned}$$
where $K:=\exp \left\{-\alpha C_{1}^{n} \int_{X_{t}} \psi_{t} \omega_{t}^{n}\right\}$.
Moreover, using the same computation as in the proof of Lemma 2.13 below, one can check that if $\beta:=\frac{2-\alpha v}{2 n}>0$, there exists a constant $C_{\beta}>0$ such that the inequality of $(n, n)$-currents below holds on $\mathbb{B}$
$$C_{\beta}^{-1}\left(d d_{x}^{c}\left\|\Phi_{x}(z)\right\|^{2 \beta}\right)^{n} \leqslant \frac{1}{\left\|\Phi_{x}(z)\right\|^{\alpha v+2 n-2}}\left(d d^{c}\|x\|^{2}\right)^{n} \leqslant C_{\beta}\left(d d_{x}^{c}\left\|\Phi_{x}(z)\right\|^{2 \beta}\right)^{n}$$
Fix $z \in \mathbb{B}$ and for any $x \in \mathbb{B}$ let $f_{x}(z):=\left\|\Phi_{x}(z)\right\|$. We define an extension of $f_{x}$ to $\mathcal{X}$ by
$$F_{x}(z):= \begin{cases}\chi \cdot f_{x}(z) & \text { if } x \in \mathbb{B} \\ 0 & \text { else. }\end{cases}$$
Here, $\chi$ is a smooth cut-off function such that $\operatorname{Supp}(\chi) \subset \mathbb{B}$ and $\chi \equiv 1$ on $\mathbb{B}_{1 / 2}$. It is easy to check that $F_{x}$ is an $A \omega$-psh function on $\mathcal{X}$ for some $A=A_{\tau}$ big enough (that a priori depends on $U_{\tau}$ but can be chosen independently of $x \in \mathbb{B}_{1 / 2}$ ). Thus
$$\begin{aligned}
\int_{x \in \mathbb{B}_{1 / 2}} \frac{1}{\left\|\Phi_{x}(z)\right\|^{\alpha v+2 n-2}}\left(d d^{c}\|x\|^{2}\right)^{n} \wedge\left[X_{t}\right] & \leqslant C_{\beta} \int_{x \in \mathbb{B}_{1 / 2}}\left(d d_{x}^{c}\left\|\Phi_{x}(z)\right\|^{2 \beta}\right)^{n} \wedge\left[X_{t}\right] \\
& \leqslant C_{\beta} \int_{x \in \mathcal{X}}\left(A \omega+d d_{x}^{c} F_{x}(z)^{2 \beta}\right)^{n} \wedge\left[X_{t}\right] \\
& \leqslant C_{\beta} \cdot A^{n} \cdot V:=C_{2} .
\end{aligned}$$
It then follows that
$$\int_{x \in \mathbb{B}_{1 / 2}} e^{-\alpha \psi_{t}} \omega^{n} \wedge\left[X_{t}\right] \leqslant C_{0} \cdot C_{2} \cdot K \cdot \int_{z \in \mathbb{B}} d d^{c} \psi_{t} \wedge\left(d d^{c}\|z\|^{2}\right)^{n-1} \wedge\left[X_{t}\right] \leqslant C_{3} \cdot K,$$
where $C_{3}:=C_{0} C_{2} C_{\Theta} C_{1}^{n-1} \cdot V$. The last inequality follows from the fact that on $\mathbb{B}_{t}$, we have $d d^{c} \psi_{t} \wedge\left(d d^{c}\|z\|^{2}\right)^{n-1} \leqslant\left(\theta_{t}+d d^{c} \varphi_{t}\right) \wedge\left(C_{1} \omega\right)^{n-1}$, and one can dominate the integral of the right-hand side on $\mathbb{B}_{t}$ by its integral on $X_{t}$ and use (2.1). This is the conclusion. \(\square\)

Lemma 2.12. — With the notations introduced at the beginning of the proof of Theorem 2.9, there exists a constant $C=C(n)>0$ such that for all $x \in \mathbb{B}_{1 / 2} \subset \mathbb{C}^{N}$ and $z \in X_{t} \cap \mathrm{~S}^{2 N-1}$,
$$\frac{1}{C} d^{c}\|z\|^{2} \wedge\left(d d^{c}\|z\|^{2}\right)^{n-1} \leqslant d^{c} G_{x} \wedge\left(d d^{c} G_{x}\right)^{n-1} \leqslant C d^{c}\|z\|^{2} \wedge\left(d d^{c}\|z\|^{2}\right)^{n-1}$$
Proof. - One knows that there exists a neighborhood $U$ of $\mathbb{S}^{2 N-1} \subset \mathbb{C}^{N}$ not containing $x$ such that $d d^{c}\left\|\Phi_{x}\right\|^{2}$ defines a Kähler form $\omega_{x}$ on $U$. This follows for instance from the fact that $\Phi_{x}$ can be extended as an holomorphic map to an open neighborhood of the closed ball - and that neighborhood can be chosen to be independent of $x \in \mathbb{B}_{1 / 2}$. On $U, \omega_{x}$ is comparable to the euclidean metric on $\mathbb{C}^{N}$ and therefore, $\omega_{x}$ and $\omega_{\text {eucl }}$ induce uniformly equivalent Riemannian metrics $g_{x}$ and $g_{\text {eucl }}$ on $U \cap X_{t}$ first, and then as well on the real hypersurface $X_{t} \cap \mathrm{~S}^{2 N-1}$; we denote them by $g_{x}^{\prime}$ and $g_{\text {eucl }}^{\prime}$ respectively. In particular their volume forms $d V_{g_{x}^{\prime}}, d V_{g_{\text {eucl }}^{\prime}}$ are equivalent too. One has $d V_{g_{\text {eucl }}^{\prime}}=\iota_{v} d V_{g_{\text {eucl }}}$ where $v$ is the restriction to $X_{t}$ of the unit outward radial vector
$$\sum_{j=1}^{n+k}\left(z_{j} \frac{\partial}{\partial z_{j}}+\bar{z}_{j} \frac{\partial}{\partial \bar{z}_{j}}\right) .$$
Hence, on $X_{t} \cap \mathbb{S}^{2 N-1}$ one has
$$d V_{g_{\text {eucl }}^{\prime}}=\iota_{v}\left(d d^{c}\|z\|^{2}\right)^{n}=2\left(\frac{i}{\pi}\right)^{n-1} d^{c}\|z\|^{2} \wedge\left(d d^{c}\|z\|^{2}\right)^{n-1} .$$

In the same way, $d V_{g_{x}^{\prime}}=\iota_{v_{x}} d V_{g_{x}}$ where $v_{x}$ is the restriction to $X_{t}$ of the unit outward vector with respect to $d d^{c}\left\|\Phi_{x}\right\|^{2}$, hence $v_{x}=\Phi_{x}^{*} v$. Therefore one has on $X_{t} \cap \mathrm{~S}^{2 N-1}$,
$$\begin{aligned}
d V_{g_{x}^{\prime}}=\iota_{v_{x}}\left(d d^{c}\left\|\Phi_{x}\right\|^{2}\right)^{n}=\Phi_{x}^{*}\left(\iota_{v}\left(d d^{c}\|z\|^{2}\right)^{n}\right) & =2\left(\frac{i}{\pi}\right)^{n-1} d^{c}\left\|\Phi_{x}\right\|^{2} \wedge\left(d d^{c}\left\|\Phi_{x}\right\|^{2}\right)^{n-1} \\
& =2^{n+1}\left(\frac{i}{\pi}\right)^{n-1} d^{c} G_{x} \wedge\left(d d^{c} G_{x}\right)^{n-1} .
\end{aligned}$$
given that $G_{x}=\frac{1}{2} \log \left\|\Phi_{x}\right\|^{2}$ vanishes on the sphere and that $d^{c} \log u \wedge\left(d d^{c} \log u\right)^{n-1}=$ $\frac{1}{u^{n}} d^{c} u \wedge\left(d d^{c} u\right)^{n-1}$ for any smooth function $u$. This shows that the above two volume forms on $X_{t} \cap \mathrm{~S}^{2 N-1}$ are uniformly equivalent on $X_{t} \cap \mathrm{~S}^{2 N-1}$ hence it ends the proof. \(\square\)

Lemma 2.13. - Let $\beta>0$ and $\mathbb{B} \subset \mathbb{C}^{n}$ be the unit ball. Then $\|z\|^{2 \beta}$ is psh on $\mathbb{B}$ and there exists a constant $C_{\beta}>0$ (that depends only on $\beta$ ) such that
$$\frac{C_{\beta}^{-1}}{\|z\|^{2(1-\beta)}} \cdot d d^{c}\|z\|^{2} \leqslant d d^{c}\|z\|^{2 \beta} \leqslant \frac{C_{\beta}}{\|z\|^{2(1-\beta)}} \cdot d d^{c}\|z\|^{2} .$$
Proof. - Let $\chi: \mathbb{R}^{+} \rightarrow \mathbb{R}^{+}$be defined as $\chi(t):=t^{\beta}$ and $u:=\|z\|^{2}$. One has
$$d d^{c} \chi \circ u=\beta u^{\beta-1}\left(d d^{c} u-(1-\beta) u^{-1} d u \wedge d^{c} u\right) .$$

Note that $\min \{1, \beta\} \cdot d d^{c} u \leqslant d d^{c} u-(1-\beta) u^{-1} d u \wedge d^{c} u \leqslant \max \{1, \beta\} \cdot d d^{c} u$. Observe that he hermitian matrix associated to the (1,1)-form $d u \wedge d^{c} u$ is $\left(\bar{z}_{i} z_{j}\right)_{i j}$. The latter has rank one and its non-zero eigenvalue coincides with its trace, i.e. $u$. Therefore the eigenvalues of the hermitian matrix $A:=\mathrm{I}_{n}-(1-\beta) u^{-1}\left(\bar{z}_{i} z_{j}\right)_{i \bar{j}}$ are 1 (with multiplicity $n-1$ ) and $\beta$ (multiplicity 1). This ends the proof. \(\square\)

\section*{3. Normalization in families}

Previous section allows us to check hypothesis (H1), as soon as the mean value of sup-normalized $\theta_{t}$-psh functions is uniformly controlled. It is classical that one can compare the supremum and the mean value of $\theta$-psh functions on a fixed compact Kähler variety (see [GZ17, Prop. 8.5]). We conjecture that the following results holds

Conjecture 3.1. — In the Setting 2.1, there exists a constant $C>0$ such that: the inequality
$$\sup _{X_{t}} \varphi_{t}-C \leqslant \frac{1}{V} \int_{X_{t}} \varphi_{t} \omega_{t}^{n} \leqslant \sup _{X_{t}} \varphi_{t}$$
holds for all $t \in \overline{\mathbb{D}}_{1 / 2}$ and for every function $\varphi_{t} \in \operatorname{PSH}\left(X_{t}, \theta_{t}\right)$.
In a preprint version of this paper, we claimed a proof of the conjecture above but a referee, whom we thank, pointed out a gap. In this section, we propose a large class of families for which the conjecture holds. More precisely, let us consider the following

Assumption 3.2. — In Setting 2.1, we assume additionnally that one of the following conditions is satisfied by the family $\pi: \mathcal{X} \rightarrow \mathbb{D}$.
\begin{itemize}
\item[1.] The map $\pi$ is projective.
\item[2.] The map $\pi$ is locally trivial.
\item[3.] The fibers $X_{t}$ are smooth for $t \neq 0$.
\item[4.] The fibers $X_{t}$ have isolated singularities for every $t \in \mathbb{D}$.
\end{itemize}

Recall that $\pi$ is said to be
\begin{itemize}
\item[-] projective if we have a commutative diagram as below
![](https://cdn.mathpix.com/cropped/a36c2a22-d4f8-428d-a076-7702e51fb997-26.jpg?height=174&width=468&top_left_y=2014&top_left_x=861)
\item[-] locally trivial if, up to shrinking $\mathbb{D}$, there exists a euclidean open cover $\left(U_{\alpha}\right)_{\alpha}$ of $\mathcal{X}$ and a collection of isomorphisms
$$F_{\alpha}:\left.\mathcal{X}\right|_{U_{\alpha}} \xrightarrow{\simeq}\left(U_{\alpha} \cap X_{0}\right) \times \mathbb{D}$$
\end{itemize}
such that the following diagram is commutative
![](https://cdn.mathpix.com/cropped/a36c2a22-d4f8-428d-a076-7702e51fb997-27.jpg?height=194&width=628&top_left_y=425&top_left_x=657)
For instance, if $\mathcal{X}$ is smooth and if the map $\pi$ is a holomorphic submersion, then $\pi$ is automatically locally trivial.
The main result in this section is the following
Proposition 3.3. - In the Setting 2.1 and if Assumption 3.2 is satisfied, then Conjecture 3.1 holds. That is, there exists a constant $C>0$ such that: the inequality
$$\sup _{X_{t}} \varphi_{t}-C \leqslant \frac{1}{V} \int_{X_{t}} \varphi_{t} \omega_{t}^{n} \leqslant \sup _{X_{t}} \varphi_{t}$$
holds for all $t \in \overline{\mathbb{D}}_{1 / 2}$ and for every function $\varphi_{t} \in \operatorname{PSH}\left(X_{t}, \theta_{t}\right)$.
We will prove Proposition 3.3 in several independent steps.
\begin{itemize}
\item[-] In § 3.2, we prove the locally trivial case.
\item[-] In § 3.3, we treat the case of isolated singularities.
\item[-] In §3.4-3.5-3.6 we introduce the material (Sobolev and Poincaré inequalities, heat kernels and Green's functions) that we will use in the final section.
\item[-] In § 3.7, we establish at the same time the projective case and the case of a smoothing, thereby completing the proof of Proposition 3.3.
\end{itemize}

By combining the above result with Theorem 2.9, we get the following
Theorem 3.4. - In Setting 2.1, let us choose a positive number $\alpha \in(0, \alpha(\Theta))$, which is possible thanks to Corollary 2.4. If Assumption 3.2 is satisfied, there exists a constant $C_{\alpha}>0$ such that for all $t \in \overline{\mathbb{D}}_{1 / 2}$ and for all $\varphi_{t} \in \operatorname{PSH}\left(X_{t}, \theta_{t}\right)$, we have
$$\int_{X_{t}} e^{-\alpha\left(\varphi_{t}-\sup _{X_{t}} \varphi_{t}\right)} \omega_{t}^{n} \leqslant C_{\alpha} .$$
3.1. Irreducibility of the fibers. - The irreducibility of all the fibers is a necessary assumption for the left-hand-side inequality in Conjecture 3.1 to hold as the following example shows:

Example 3.5. - Consider $\mathcal{X} \subset \mathbb{P}^{2} \times \mathbb{C}$ where
$$\mathcal{X}:=\left\{([x: y: z], t) ; x y-t z^{2}=0\right\} .$$
The variety $\mathcal{X}$ is smooth and comes equipped with the proper morphism $\pi: \mathcal{X} \rightarrow \mathbb{C}$ induced by the second projection $\mathbb{P}^{2} \times \mathbb{C} \rightarrow \mathbb{C}$. Set $X_{t}=\left\{[x: y: z] \in \mathbb{P}^{2}: x y=t z^{2}\right\}$. Note that $X_{t}$ is a smooth conic for $t \neq 0$ while $X_{0}=\left\{[x: y: z] \in \mathbb{P}^{2}: x y=0\right\}$ is the union of two lines. The quasi-psh function $\varphi$ on $\mathbb{P}^{2}$ defined by
$$\varphi([x: y: z])=\frac{1}{4}\left(\log \left(|x|^{2}+|z|^{2}\right)+\log |y|^{2}\right)-\frac{1}{2} \log \left(|x|^{2}+|y|^{2}+|z|^{2}\right)+\frac{\log 2}{2}$$
clearly induces a $\omega$-psh function $\Phi$ on $\mathcal{X}$, where $\omega=\omega_{\mathrm{FS}}+d d^{c}|t|^{2}$,
$$\Phi([x: y: z], t)=\varphi([x: y: z]) .$$
We set $\varphi_{t}:=\left.\Phi\right|_{X_{t}}$ and $\omega_{t}:=\left.\omega\right|_{X_{t}}$. A simple computation shows that $\sup _{\mathcal{X}} \Phi=0$ and it is attained at points ( $[x: y: z], t)$ such that $|y|^{2}=|x|^{2}+|z|^{2}$. We also find that $\sup _{X_{t}} \varphi_{t}=0$ and the supremum is attained on the set
$$S_{t}:=\left\{[x: 1: z]:|x|=\frac{1}{2|t|} \cdot\left(\sqrt{4|t|^{2}+1}-1\right), z^{2}=x t^{-1}\right\} .$$
As $t \rightarrow 0, S_{t}$ becomes the circle $\mathcal{C}:=\left\{\left[0: 1: e^{i \theta}\right] ; \theta \in \mathbb{R}\right\} \subset X_{0}$. Note also that $X_{0}=\ell \cup \ell^{\prime}$, where $\ell:=\{[0: y: z]\}$ and $\ell^{\prime}:=\{[x: 0: z]\}$ and $\mathcal{C} \subset \ell$. The open annulus $U_{t}:=\left\{\left[z^{2}: t: z\right] ; 1<|z|^{2}<2\right\} \subset X_{t}$ satisfies
$$\int_{U_{t}} \omega_{t} \geqslant \delta$$
for some $\delta>0$ independent of $t$ as well as
$$\left.\varphi_{t}\right|_{U_{t}} \leqslant \frac{1}{2}(\log |t|+1)$$
from which it follows that
$$\lim _{t \rightarrow 0} \int_{X_{t}} \varphi_{t} \omega_{t}=-\infty .$$
3.2. The locally trivial case. - In this section, we prove Proposition 3.3 under the assumption that $\pi$ is locally trivial; we borrow the notations from Diagram (3.1).

One can reduce the problem to showing that there exists a constant $C>0$ depending only on $\pi$ such that given any sequence of complex numbers $t_{k} \rightarrow 0$ and any functions $\varphi_{k} \in \operatorname{PSH}\left(X_{t_{k}}, \theta_{t_{k}}\right)$ such that $\sup _{X_{t_{k}}} \varphi_{k}=0$, one has
$$\int_{X_{t_{k}}} \varphi_{k} \omega_{t_{k}}^{n} \geqslant-C .$$

By compactness of $\pi^{-1}\left(\overline{\mathbb{D}}_{1 / 2}\right)$, one can assume that $\alpha$ ranges among the finite set $\{1, \ldots, r\}$ and without loss of generality, one can assume that $U_{\alpha+1} \cap U_{\alpha} \neq \varnothing$, for any $\alpha \in\{1, \ldots, r-1\}$. Up to splitting the sequence $\left(\varphi_{k}\right)$ into (at most) $r$ subsequences, we can assume that for every $k, \varphi_{k}$ attains its maximum in the same set $U_{\alpha_{0}}$ for some fixed $\alpha_{0} \in\{1, \ldots, r\}$. By simplicity, we assume that $\alpha_{0}=1$.

Let $G_{\alpha, k}: U_{\alpha} \cap X_{0} \rightarrow U_{\alpha} \cap X_{t_{k}}$ be the biholomorphism defined as the inverse of the restriction of $F_{\alpha}$ to $U_{\alpha} \cap X_{t_{k}}$ and let us analyze the sequence of functions $\psi_{\alpha, k}:=G_{\alpha, k}^{*} \varphi_{k}$. As $F_{\alpha}^{*}\left(\omega_{0}+i d t \wedge d \bar{t}\right)$ is commensurable to $\omega$, there exists $C>0$ depending only on $\pi$ such that
$$C^{-1} \omega_{0} \leqslant G_{\alpha, k}^{*} \omega_{t_{k}} \leqslant C \omega_{0} .$$
In particular, up to increasing $C$, one can assume that $G_{\alpha, k}^{*} \theta_{t_{k}} \leqslant C \omega_{0}$. As a result, one has $\psi_{\alpha, k} \in \operatorname{PSH}\left(U_{\alpha} \cap X_{0}, C \omega_{0}\right)$.

The family $\left(\psi_{1, k}\right)_{k}$ is a family of non-positive $C \omega_{0}$-psh functions on the complex space $U_{1} \cap X_{0}$ attaining the value zero there, so it is relatively compact for the $L_{\text {loc }}^{1}$ topology,
cf e.g. [GZ17, Proposition 8.5]. In particular, given any compact subset $U_{1}^{\prime} \Subset U_{1}$, the integral $\int_{U_{1}^{\prime}} \psi_{1, k} \omega_{0}^{n}$ admits a lower bound depending only on $U_{1}^{\prime}$ but not on $k$.

Next, the family $\left(\psi_{2, k}\right)_{k}$ is a family of non-positive $C \omega_{0}$-psh functions on $U_{2} \cap X_{0}$. Therefore, either it converges locally uniformly to $-\infty$ or it is relatively compact on each compact subset. From (3.2), it follows that the family of automorphisms $H_{k}:=$ $\left.\left.\left(G_{2, k}^{-1}\right)\right|_{U_{1} \cap U_{2} \cap X_{t_{k}}} \circ G_{1}\right|_{U_{1} \cap U_{2} \cap X_{0}}$ of $U_{1} \cap U_{2} \cap X_{0}$ satisfies
$$C^{-1} \omega_{0} \leqslant H_{k}^{*} \omega_{0} \leqslant C \omega_{0} \quad \text { and } \quad \psi_{2, k}=H_{k}^{*} \psi_{1, k} .$$
One deduces then easily that for any compact subset $U_{12}^{\prime} \Subset U_{1} \cap U_{2}$, the integral $\int_{U_{12}^{\prime}} \psi_{2, k} \omega_{0}^{n}$ admits a lower bound independent of $k$. In turn, this implies that $\left(\psi_{2, k}\right)_{k}$ is relatively compact for the $L_{\text {loc }}^{1}$ topology on the whole $U_{2} \cap X_{0}$.

By iterating the argument, one finds that for any $\alpha$, the family $\left(\psi_{\alpha, k}\right)_{k}$ is relatively compact for the $L_{\text {loc }}^{1}\left(U_{\alpha} \cap X_{0}\right)$ topology and using the estimate (3.2) as above, one concludes easily that $\int_{X_{t_{k}}} \varphi_{k} \omega_{t_{k}}^{n}$ admits a uniform lower bound as claimed.

This shows that Proposition 3.3 holds whenever $\pi$ is locally trivial. An easy consequence is the following

Corollary 3.6. — In Setting 2.1, there exists a discrete set $Z \subset \mathbb{D}$ such that for every compact subset $K \Subset \mathbb{D} \backslash Z$, there exists a constant $C_{K}$ such that
$$\int_{X_{t}} \varphi_{t} \omega_{t}^{n} \geqslant-C_{K}$$
for any collection of functions $\varphi_{t} \in \operatorname{PSH}\left(X_{t}, \theta_{t}\right)$ such that $\sup _{X_{t}} \varphi_{t}=0$.
Moreover, one can take $Z=\varnothing$ provided that the family $\pi: \mathcal{X} \rightarrow \mathbb{D}$ admits a simultaneous resolution of singularities, i.e. a proper, surjective holomorphic map $f: \mathcal{Y} \rightarrow \mathcal{X}$ from a Kähler manifold $\mathcal{Y}$ such that for any $t \in \mathbb{D}$, the induced morphism $\left.f\right|_{Y_{t}}: Y_{t} \rightarrow X_{t}$ is a resolution of singularities, where $Y_{t}:=f^{-1}\left(X_{t}\right)$.

Proof. - Let $f: \mathcal{Y} \rightarrow \mathcal{X}$ be a resolution of singularities of $\mathcal{X}$. One can assume that $\mathcal{Y}$ is a Kähler manifold; let us pick $\omega_{Y}$ a Kähler form on $\mathcal{Y}$. The induced map $\rho:=\pi \circ f:$ $\mathcal{Y} \rightarrow \mathbb{D}$ is surjective, hence by generic smoothness, it is smooth over the complement of a proper analytic subset $Z$ of $\mathbb{D}$. In particular, $Z$ is discrete. Note that over $Z$, the fibers of $\rho$ may have several irreducible components.

We denote by $f_{t}$ the restriction $\left.f\right|_{Y_{t}}: Y_{t} \rightarrow X_{t}$ of $f$ to the fiber $Y_{t}$, where $Y_{t}:=\rho^{-1}(t)$. For any $t \in \mathbb{D} \backslash Z$, the map $f_{t}$ is bimeromorphic, i.e. it is a resolution of singularities of $X_{t}$. Let us choose $K \Subset \mathbb{D}$ a compact subset. There exists a constant $C_{K}$ such that $f^{*} \omega \leqslant C_{K} \omega_{Y}$ on $\rho^{-1}(K)$. In particular, for any $t \in K$, one has $f_{t}^{*} \varphi_{t} \in \operatorname{PSH}\left(Y_{t}, C_{K} C_{\Theta} \omega_{Y}\right)$ and $\sup _{Y_{t}} f_{t}^{*} \varphi_{t}=0$. Now, if we additionally assume that $K \Subset \mathbb{D} \backslash Z$, we can apply the result above to the smooth family $\left.\rho\right|_{\rho^{-1}(K)}: \rho^{-1}(K) \rightarrow K$ to find another constant $C_{K}^{\prime}>0$ satisfying
$$\int_{Y_{t}}\left(f_{t}^{*} \varphi_{t}\right) \omega_{Y}^{n} \geqslant-C_{K}^{\prime}$$
for any $t \in K$. As $\omega_{Y}^{n} \geqslant C_{K}^{-n} f_{t}^{*} \omega_{t}^{n}$, we deduce that
$$\int_{X_{t}} \varphi_{t} \omega_{t}^{n} \geqslant-C_{K}^{\prime} \cdot C_{K}^{n}$$
which concludes the first part of the proof. The second statement is an immediate consequence of the proof of the first one. Indeed, if $Y_{t}$ is smooth (as an analytic space), then $\pi \circ f$ is smooth in a neighborhood of $Y_{t}$ and the argument above can be run over a neighborhood of $t$. \(\square\)
3.3. The case of isolated singularities. - In this section, we prove Proposition 3.3 in the case where all fibers $X_{t}, t \in \mathbb{D}$, have isolated singularities.

Remark 3.7. - We would like to start with two observations.
\begin{itemize}
\item[-] This case includes the case where $n=\operatorname{dim} X_{t}=1$.
\item[-] If one only assumes that $X_{0}$ has isolated singularities, then it is easy to check that there exists $\varepsilon>0$ such that $X_{t}$ has isolated singularities for any $t$ satisfying $|t|<\varepsilon$. This is because the locus $Z \subset \mathcal{X}$ where $\pi$ is not smooth is an analytic set such that $\operatorname{dim}\left(Z \cap X_{0}\right)=0$ and by upper semi-continuity, $Z$ has relative dimension 0 over a neighborhood of $0 \in \mathbb{D}$.
\end{itemize}

We now proceed to proving Proposition 3.3 in several steps.
Step 1. Localization of the problem at $t=0$.
Let $f: \mathcal{Y} \rightarrow \mathcal{X}$ be a resolution of singularities $\mathcal{X}$. The induced family $\pi \circ f: \mathcal{Y} \rightarrow \mathbb{D}$ is generically smooth over $\mathbb{D}$ so for $r>0$ small enough, the restriction of $\pi \circ f$ to the inverse image of $\mathbb{D}_{r}$ has a most one singular fiber, corresponding to $t=0$. In particular, the family $\mathcal{Y} \rightarrow \mathbb{D}_{r}$ is locally trivial away from $Y_{0}$. Applying the result in the locally trivial case (cf. § 3.2) to the collection of $f^{*} \theta_{t}$-psh functions $f^{*} \varphi_{t}$, we see that for every compact subset $K \Subset \mathbb{D}_{r}^{*}$, there exists a constant $C_{K}$ independent of the chosen family such that
$$\sup _{t \in K} \int_{X_{t}}\left(-\varphi_{t}\right) \omega_{t}^{n} \leqslant C_{K},$$
cf also Corollary 3.6. This shows that it is enough to prove that for any sequence $t_{k} \rightarrow 0$ and any collection of sup-normalized $\theta_{t_{k}}$-psh functions $\varphi_{t_{k}}$, one has
$$\sup _{k \geqslant 1} \int_{X_{t_{k}}}\left(-\varphi_{t_{k}}\right) \omega_{t_{k}}^{n}<+\infty .$$

Step 2. Choice of a good covering.
As the fibers are reduced, it follows from the jacobian criterion for smoothness that the smooth locus of $\pi$ coincides with the union of the smooth loci of $X_{t}$ when $t$ ranges in $\mathbb{D}$. Recall that $Z$, the singular locus of $\pi$, is an analytic space of relative dimension at most zero. It has finitely many irreducible components (say when restricted to $\pi^{-1}\left(\mathbb{D}_{1 / 2}\right)$ ) and we can assume without loss of generality that this number is equal to the cardinality of $Z \cap X_{0}$. Let $\left(V_{\alpha}\right)_{\alpha}$ be a finite collection of (small) open balls in $\mathcal{X}$ centered at the (finitely many) singular points of $X_{0}$. Up to adding a finite amount of balls to the collection, one can assume that
\begin{itemize}
\item[(i)] The reunion $V:=\cup_{\alpha} V_{\alpha}$ is an open neighborhood of $X_{0} \subset \mathcal{X}$.
\item[(ii)] Each point of $Z \cap X_{0}$ belongs to exactly one element $V_{\alpha}$ of the covering.
\item[(iii)] For all $\alpha$, there exists $\rho_{\alpha} \in \mathcal{C}^{\infty}\left(V_{\alpha}, \mathbb{R}\right)$ such that $\left.\omega\right|_{V_{\alpha}}=d d^{c} \rho_{\alpha}$.
\end{itemize}
\begin{itemize}
\item[(iv)] There exists $r>0$ such that for all $\alpha$, one has
$$\mathrm{Z} \cap \partial V_{\alpha} \cap \pi^{-1}\left(\mathbb{D}_{r}\right)=\varnothing .$$
\end{itemize}

Up to substracting a constant to $\rho_{\alpha}$, one can assume that $\rho_{\alpha}$ is non-negative. Moreover, there exists a constant $C_{1}>0$ such that $\rho_{\alpha} \leqslant C_{1}$ on $V_{\alpha}$, for any $\alpha$. Let $\left(\chi_{\alpha}\right)_{\alpha}$ be a partition of unity associated to the covering $\left(V_{\alpha}\right)_{\alpha}$. That means that $\sum_{\alpha} \chi_{\alpha} \equiv 1$ and $\operatorname{Supp}\left(\chi_{\alpha}\right) \subset V_{\alpha}$. Finally, let $\rho:=\sum \chi_{\alpha} \rho_{\alpha}$. If follows from (ii) that one has $\omega=d d^{c} \rho$ in some neighborhood $W_{\alpha}^{\prime}$ of each point of $Z \cap X_{0}$. We pick a relatively compact open subset $W_{\alpha} \Subset W_{\alpha}^{\prime}$ and set $W:=\cup W_{\alpha}$. Up to decreasing $r$ a little, one can assume that $Z \cap \partial W \cap \pi^{-1}\left(\overline{\mathbb{D}}_{r}\right)=\varnothing$. In particular, there exists $\delta>0$ such that for any $t \in \overline{\mathbb{D}}_{r}$, one has $d_{\omega}\left(\partial W \cap X_{t}, Z\right) \geqslant \delta$. In summary
$$0 \leqslant \rho \leqslant C_{1}, \quad \omega=d d^{c} \rho \text { on } W, \quad d_{\omega}\left(\partial W \cap X_{t}, Z\right) \geqslant \delta \text { for all } t \in \overline{\mathbb{D}}_{r} .$$

Step 3. Weak compactness locally outside $Z$.
Let $t_{k}$ be a sequence of numbers converging to zero, and let $\varphi_{t_{k}} \in \operatorname{PSH}\left(X_{t_{k}}, \theta_{t_{k}}\right)$ such that $\sup _{X_{t_{k}}} \varphi_{t_{k}}=0$. We claim that there exists a sequence of points $x_{k} \in X_{t_{k}}$ and a constant $C_{2}>0$ such that
\begin{itemize}
\item[(i)] $\varphi_{t_{k}}\left(x_{k}\right) \geqslant-C_{2}$.
\item[(ii)] $d_{\omega}\left(x_{k}, Z\right) \geqslant \delta / 2$.
\end{itemize}
Indeed, let $y_{k} \in X_{t_{k}}$ be such that $\varphi_{t_{k}}\left(y_{k}\right)=0$. If $d_{\omega}\left(y_{k}, Z\right) \geqslant \delta / 2$, then we are done. Otherwise, it means that we have $y_{k} \in W$ by the third item of (3.3). Now, the function $C_{\Theta} \rho+\varphi_{t_{k}}$ is psh on $\bar{W}$ so by the maximum principle, there exists $x_{k} \in \partial W$ such that $\left(C_{\Theta} \rho+\varphi_{t_{k}}\right)\left(x_{k}\right) \geqslant\left(C_{\Theta} \rho+\varphi_{t_{k}}\right)\left(y_{k}\right) \geqslant 0$. By the first item of (3.3), we deduce $\varphi_{t_{k}}\left(x_{k}\right) \geqslant-C_{2}$ where we set $C_{2}:=C_{1} C_{\Theta}$.

Let $U:=\left\{x \in \pi^{-1}\left(\mathbb{D}_{r}\right) ; d(x, Z)>\delta / 2\right\}$. The map $\pi$ is smooth on $U$ and one can cover $U$ by finitely many open subsets $\left(U_{j}\right)_{1 \leqslant j \leqslant p}$ isomorphic to $\left(U_{j} \cap X_{0}\right) \times \mathbb{D}_{r}$ over $\mathbb{D}_{r}$. Because of (i), we can argue as in the locally trivial case (cf. § 3.2) by exporting the functions $\left.\varphi_{t_{k}}\right|_{U_{j} \cap X_{t_{k}}}$ to the fixed space $U_{j} \cap X_{0}$ and get relative compactness there. In particular, one can find a constant $C_{3}>0$ independent of $k$ such that
$$\int_{U \cap X_{t_{k}}}\left(-\varphi_{t_{k}}\right) \omega_{t_{k}}^{n} \leqslant C_{3} .$$

Step 4. The integral bound.
On $W$, one has $\omega=d d^{c} \rho$. This implies that $\omega^{n}=\left(d d^{c} \rho\right)^{n}+T$ for some smooth, closed $(n, n)$-form $T$ on $\pi^{-1}\left(\mathbb{D}_{r}\right)$ such that $\left.T\right|_{W} \equiv 0$. Let us introduce constants $C_{4}, C_{5}$ such that $-C_{4} \omega^{n-1} \leqslant\left(d d^{c} \rho\right)^{n-1} \leqslant C_{4} \omega^{n-1}$ and $T \leqslant C_{5} \omega^{n}$. As the complement of $W$ in $\pi^{-1}\left(\mathbb{D}_{r}\right)$ is included in $U$, it follows from (3.4) that
$$\int_{X_{t_{k}}}\left(-\varphi_{t_{k}}\right) T \leqslant C_{5} C_{3} .$$

Moreover, one has
$$\begin{aligned}
\int_{X_{t_{k}}}\left(-\varphi_{t_{k}}\right)\left(d d^{c} \rho\right)^{n} & =\int_{X_{t_{k}}}-\rho d d^{c} \varphi_{t_{k}} \wedge\left(d d^{c} \rho\right)^{n-1} \\
& =-\int_{X_{t_{k}}} \rho\left(\theta_{t_{k}}+d d^{c} \varphi_{t_{k}}\right) \wedge\left(d d^{c} \rho\right)^{n-1}+\int_{X_{t_{k}}} \rho \theta_{t_{k}} \wedge\left(d d^{c} \rho\right)^{n-1} \\
& \leqslant C_{4} C_{1} \int_{X_{t_{k}}}\left(\theta_{t_{k}}+d d^{c} \varphi_{t_{k}}\right) \wedge \omega^{n-1}+C_{\Theta} C_{4} C_{1} \cdot V \\
& \leqslant 2 C_{1} C_{4} C_{\Theta} \cdot V
\end{aligned}$$
All in all, one finds
$$\int_{X_{t_{k}}}\left(-\varphi_{t_{k}}\right) \omega_{t_{k}}^{n} \leqslant C_{6}$$
where $C_{6}=C_{3} C_{5}+2 C_{1} C_{4} C_{\Theta} \cdot V$.
3.4. Sobolev and Poincaré inequalities. - In this section, we work in the Setting 2.1 above and we assume from now on that the relative dimension $n=\operatorname{dim}_{\mathbb{C}} X_{t}$ satisfies $n>1$, since the case $n=1$ has already been dealt with in § 3.3, cf. Remark 3.7.

For $t \in \mathbb{D}$, we set $X_{t}:=\pi^{-1}(t)$ and denote by $X_{t}^{\text {reg }}$ the regular locus of $X_{t}$. We fix a Kähler form $\omega$ on $\mathcal{X}$ and set
$$\omega_{t}:=\omega_{\mid X_{t}} .$$

Proposition 3.8. - Let $K \Subset \mathbb{D}$. There exists $C_{S}=C_{S}(K)$ such that
$$\forall t \in K, \forall f \in \mathcal{C}_{0}^{\infty}\left(X_{t}^{\mathrm{reg}}\right), \quad\left(\int_{X_{t}}|f|^{\frac{2 n}{n-1}} \omega_{t}^{n}\right)^{\frac{n-1}{n}} \leqslant C_{S} \int_{X_{t}}\left(|f|^{2}+|d f|_{\omega_{t}}^{2}\right) \omega_{t}^{n} .$$

Remark 3.9. - The inequality above extends immediately to the functions $f \in$ $W^{1,2}\left(X_{t}^{\text {reg }}\right)$, i.e. such that $f, d f \in L^{2}\left(X_{t}^{\text {reg }}, \omega_{t}\right)$.

Proof. - Because of the existence of partition of unity, the statement above is local. That means that it is enough to show the above inequality for any $t \in K$ and any $f \in \mathcal{C}_{0}^{\infty}\left(U_{i} \cap X_{t}^{\text {reg }}\right)$ where $U_{i} \subset \mathcal{X}$ are open sets such that $\cup U_{i}=\mathcal{X}$.

We fix such an open set $U_{i}$ and we drop the index $i$ in what follows. Without loss of generality, one can assume that there exists an embedding $U_{i} \hookrightarrow \mathbb{C}^{N}$ and that $\left.\omega\right|_{U}$ and $\left.\omega_{\mathbb{C}^{N}}\right|_{U}$ are quasi-isometric. Because Sobolev inequality is essentially insensitive to quasi-isometry, it is enough to show the inequality replacing $\omega_{t}$ by $\left.\omega_{\mathbb{C}^{N}}\right|_{U_{t}}$ where $U_{t}:=U \cap X_{t}$.

Now, the isometric embeddings $\left(U_{t}^{\text {reg }},\left.\omega_{\mathbb{C}^{N}}\right|_{U_{t}}\right) \hookrightarrow\left(\mathbb{C}^{N}, \omega_{\mathbb{C}^{N}}\right)$ provide a family of minimal submanifolds (i.e. with zero mean curvature vector) of the euclidean space by virtue of Wirtinger inequality. The expected inequality is now a direct application of Michael-Simon's Sobolev inequality [MS73, Thm. 2.1]. \(\square\)

Proposition 3.10. - Let $K \in \mathbb{D}$. There exists $C_{P}=C_{P}(K)$ such that
$$\forall t \in K, \forall f \in \mathcal{W}_{0}^{1,2}\left(X_{t}^{\mathrm{reg}}\right), \quad \int_{X_{t}}|f|^{2} \omega_{t}^{n} \leqslant C_{P} \int_{X_{t}}|d f|_{\omega_{t}}^{2} \omega_{t}^{n} .$$

In the statement above, the space $W_{0}^{1,2}\left(X_{t}^{\text {reg }}\right)$ is defined as the space of functions $f$ on $X_{t}^{\text {reg }}$ such that $f, d f \in L^{2}\left(X_{t}^{\text {reg }}, \omega_{t}\right)$ and $\int_{X_{t}} f \omega_{t}^{n}=0$.

Proof. - First, we claim that for each $t \in \mathbb{D}$, there exists such a Poincaré constant $C_{P, t}$. Indeed, thanks to [Bei19, Thm. 0.2], the Laplacian $\Delta_{\omega_{t}}$ is positive, self-adjoint and its spectrum is discrete. It remains to show that its kernel is one-dimensional. Now, if $f \in W^{1,2}\left(X_{t}^{\text {reg }}\right)$ is such that $\Delta_{t} f=0$, it means that for every $u \in W^{1,2}\left(X_{t}^{\text {reg }}\right)$, we have $\langle\nabla u, \nabla f\rangle=0$. In particular, taking $u=f$ shows that $f$ is locally constant on $X_{t}^{\text {reg }}$. As $X_{t}$ is irreducible, $X_{t}^{\text {reg }}$ is connected and the result follows.

Given the absolute case explained above, the family version of Poincaré inequality follows from Proposition 3.8 and the irreducibility of the fibers: we refer the reader to [RZ11b, Prop. 3.2] for a detailed argument (the projectivity assumption made by Ruan-Zhang being unnecessary for this part of the argument). \(\square\)
3.5. Heat kernels and Green's functions. - In this section as well as in the following section 3.6, we go back to the absolute case and consider an irreducible and reduced Kähler space ( $X, \omega$ ) of dimension $n=\operatorname{dim}_{\mathbb{C}} X$ satisfying $n>1$.

When $X$ is smooth, it is well-known (cf e.g. [Cha84, § VI]) that there exists a smooth, positive function $H: X \times X \times(0,+\infty)$, symmetric in its space variable and such that if $\Delta:=\operatorname{tr}_{\omega} d d^{c}$, one has
\begin{itemize}
\item[-] $\left(-\Delta_{y}+\partial_{t}\right) H(x, y, t)=0$.
\item[-] For every $x \in X$, one has weak convergence $H(x, \cdot, t) \omega^{n} \xrightarrow[t \rightarrow 0]{ } \delta_{x}$.
\end{itemize}
In the general case where $X$ may have singularities, one can introduce $X_{\varepsilon}=X \backslash V_{\varepsilon}$ where $V_{\varepsilon}$ is a closed $\varepsilon$-neighborhood of $X_{\text {sing }}$ with smooth boundary. Then, there exists a unique smooth, positive function $H_{\varepsilon}$ on $X_{\varepsilon} \times X_{\varepsilon} \times(0,+\infty)$ such that
\begin{itemize}
\item[-] $\left(-\Delta_{y}+\partial_{t}\right) H_{\varepsilon}(x, y, t)=0$.
\item[-] $H_{\varepsilon}(x, y, t) \rightarrow 0$ whenever $x$ or $y$ approaches $\partial X_{\varepsilon}$.
\item[-] For every $x \in X_{\varepsilon}$, one has weak convergence $H_{\varepsilon}(x, \cdot, t) \omega^{n} \xrightarrow[t \rightarrow 0]{ } \delta_{x}$.
\end{itemize}

Moreover, given $(x, y, t) \in X_{\varepsilon_{0}} \times X_{\varepsilon_{0}} \times(0,+\infty)$, the function $\left(0, \varepsilon_{0}\right) \ni \varepsilon \mapsto H_{\varepsilon}(x, y, t)$ is decreasing. Using [Cha84, VIII. 2 Thm. 4] and its proof, we additionally see that the limit $H:=\lim _{\varepsilon} H_{\varepsilon}$ is everywhere finite and satisfies
\begin{itemize}
\item[-] $H$ is positive and smooth on $X_{\text {reg }} \times X_{\text {reg }} \times(0,+\infty)$.
\item[-] $\left(-\Delta_{y}+\partial_{t}\right) H(x, y, t)=0$.
\item[-] For all $x, y \in X_{\text {reg }}$ and $t, s>0$, one has
\end{itemize}
$$H(x, y, t+s)=\int_{X} H(x, \cdot, t) H(\cdot, y, s) \omega^{n} .$$
\begin{itemize}
\item[-] For any $x \in X_{\text {reg }}$, one has $H(x, \cdot, t) \omega^{n} \xrightarrow[t \rightarrow 0]{ } \delta_{x}$ weakly.
\end{itemize}

When $X \subset \mathbb{P}^{N}$ is projective and $\omega=\left.\omega_{\mathrm{FS}}\right|_{X}$, Li and Tian have showed in [LT95] that there is an absolute inequality
$$H(x, y, t) \leqslant H_{\mathbb{P}^{n}}\left(d_{\mathbb{P}^{N}}(x, y), t\right)$$
for any $x, y \in X_{\text {reg }}$ and $t \in(0,+\infty)$, where $H_{\mathbb{P}^{n}}$ is the heat kernel of $\left(\mathbb{P}^{n}, \omega_{\mathrm{FS}}\right)$, whose dependence in the space variables $x, y$ is known to reduce to a single real variable, namely the distance between those two points.

In particular, $H(x, \cdot, t)$ is bounded on $X_{\text {reg }}$ for any $x \in X_{\text {reg }}$ and $t>0$. Since $X_{\text {sing }}$ has real codimension at least two, it admits cut-off functions whose gradient converges to zero in $L^{2}$, and this allows one to perform integration by parts as in the compact case for bounded functions in $W^{1,2}$. We refer to [LT95, Lem 3.1] for more details; we will also rely on the latter result which states that $H(x, \cdot, t) \in W^{1,2}$ and that is satisfies the conservation property
$$\forall t>0, \int_{X} H(x, \cdot, t) \omega^{n}=1 .$$

Below are a few more properties that will be useful later, which are certainly standard in the smooth case. For this purpose, one introduces the function
$$G(x, y, t):=H(x, y, t)-\frac{1}{V}$$
where $V:=\int_{X} \omega^{n}$. The key information for us will be given by the fourth item, for which the arguments are borrowed from [CL81], see also [Siu87, App. A].

Lemma 3.11. - Assume either that $X$ is smooth or that $X \subset \mathbb{P}^{N}$ is projective and $\omega=\left.\omega_{\mathrm{FS}}\right|_{X}$. Let $x, y \in X_{\text {reg }}$. We have
\begin{itemize}
\item[1.] $G(x, y, t)>-\frac{1}{V}, \int_{X} G(x, \cdot, t) \omega^{n}=0$ and $\int_{X}|G(x, \cdot, t)| \omega^{n} \leqslant 2$.
\item[2.] $|G(x, y, t)|^{2} \leqslant G(x, x, t) G(y, y, t)$.
\item[3.] $H(x, x, t) \rightarrow+\infty$ when $t \rightarrow 0$.
\item[4.] There exists a constant $C_{0}$ depending only on the Sobolev and Poincaré constant of $\left(X_{\text {reg }}, \omega\right)$ such that
$$|G(x, y, t)| \leqslant C_{0} t^{-n}$$
for any $x, y \in X_{\text {reg }}$ and any $t>0$.
\end{itemize}

Proof. - Under the assumptions on $X$, we know that $H(x, \cdot, t)$ is bounded on $X_{\text {reg }}$, in $W^{1,2}$ and satisfies the conservation property. We will only rely on these non-quantitative properties to establish the items below, and not on the more precise inequality (3.7) which certainly does not hold if $X$ is not projective.
\begin{itemize}
\item[(1)] a trivial consequence of the positivity of $H$ and the fact that $\int_{X} H(x, \cdot, t) \omega^{n}=1$.
\item[(2)] is classical when $X$ is smooth, so we assume for the time being that $X$ is projective.
\end{itemize} Let $K_{\varepsilon}$ be the Neumann heat kernel on $X_{\varepsilon}$, let $V_{\varepsilon}:=\int_{X_{\varepsilon}} \omega^{n}$ and let $\widetilde{G}_{\varepsilon}:=K_{\varepsilon}-\frac{1}{V_{\varepsilon}}$. Then we have
$$K_{\varepsilon}(x, y, t)=\sum_{i \geqslant 0} e^{-\lambda_{i, \varepsilon} t} \phi_{i, \varepsilon}(x) \phi_{i, \varepsilon}(y)$$
where $\left(\phi_{i, \varepsilon}\right)$ is an orthonormal basis of $L^{2}\left(X_{\varepsilon}\right)$ consisting of Neumann eigenfunctions of $-\Delta$ with eigenvalues $\lambda_{i, \varepsilon}$. Note that $\phi_{0, \varepsilon}=\frac{1}{\sqrt{V_{\varepsilon}}}$. By Cauchy-Schwarz, we find that $\left|\widetilde{G}_{\varepsilon}(x, y, t)\right|^{2} \leqslant \widetilde{G}_{\varepsilon}(x, x, t) \cdot \widetilde{G}_{\varepsilon}(y, y, t)$. Thanks to [LT95, Lemma 3.2], $K_{\varepsilon}$ converges to $H$ locally smoothly on $X_{\text {reg }}^{2} \times(0,+\infty)$ when $\varepsilon \rightarrow 0$, hence $\widetilde{G}_{\varepsilon} \rightarrow G$ in the same way and we get the second item.
(3) Since $H \geqslant H_{\varepsilon}$, It is enough to show the third claim for $H_{\varepsilon}$. We consider a Sturm-Liouville decomposition as before
$$H_{\varepsilon}(x, y, t)=\sum_{i \geqslant 0} e^{-\mu_{i, \varepsilon} t} \psi_{i, \varepsilon}(x) \psi_{i, \varepsilon}(y)$$
but now, $\left(\psi_{i, \varepsilon}\right)$ is an orthonormal basis of $L^{2}\left(X_{\varepsilon}\right)$ consisting of Dirichlet eigenfunctions of $-\Delta$ with eigenvalues $\mu_{i, \varepsilon}$, cf [Cha84, VII (31)]. The sought property now follows since $\sum \psi_{i, \varepsilon}(x)^{2}$ is the norm of the unbounded functional $L^{2} \cap \mathcal{C}^{\infty}\left(X_{\varepsilon}\right) \ni f \mapsto f(x)$.
(4) We start from the identity (3.6), which holds for $G$ as well as one checks easily. Taking $y=x$ and differentiating with respect to $s$ and eventually setting $s:=t$, one finds
$$-G^{\prime}(x, x, 2 t)=\|d G(x, \cdot, t)\|_{L^{2}}^{2} \geqslant\left(C_{S}\left(C_{P}+1\right)\right)^{-1}\|G(x, \cdot, t)\|_{L^{\frac{2 n}{n-1}}}^{2}$$
since integration by parts is legitimate as we explained above and $\int_{X} G(x, \cdot, t) \omega^{n}=0$. Moreover, the interpolation inequality gives
$$G(x, x, 2 t)=\|G(x, \cdot, t)\|_{L^{2}}^{2} \leqslant\|G(x, \cdot, t)\|_{L^{1}}^{\frac{2}{n+1}} \cdot\|G(x, \cdot, t)\|_{L^{\frac{2 n}{n-1}}}^{\frac{2 n}{n+1}}$$
hence
$$\|G(x, \cdot, t)\|_{L^{\frac{2 n}{n-1}}}^{2} \geqslant 2^{-\frac{2}{n}} G(x, x, 2 t)^{\frac{n+1}{n}}$$
and
$$-\frac{1}{n} G^{\prime}(x, x, t) G(x, x, t)^{-1-\frac{1}{n}} \geqslant C^{-1}$$
for $C=n 4^{\frac{1}{n}} \cdot C_{S}\left(C_{P}+1\right)$. Integrating this inequality w.r.t. $t$ and using the second item, we get the fourth item - recall that $G(x, x, t)>0$ for any $x \in X_{\text {reg }}$ given its expansion as power series, cf (2). \(\square\)

Under the assumptions of Lemma 3.11 above, the integral
$$G(x, y):=\int_{0}^{+\infty} G(x, y, t) d t$$
is convergent whenever $x \neq y$ and defines a function $G$ on $X_{\text {reg }} \times X_{\text {reg }}$ such that $G(x, \cdot) \in L^{1}\left(X_{\text {reg }}\right)$. Moreover, since $\left(-\Delta+\partial_{t}\right) G(x, \cdot, t)=0, G(x, \cdot, t) \underset{t \rightarrow+\infty}{\rightarrow} 0$ and $G(x, \cdot, t) \omega^{n} \underset{t \rightarrow 0}{\rightarrow} \delta_{x}-\frac{1}{V}$, we have
$$d d^{c} G(x, \cdot) \wedge \omega^{n}=\frac{\omega^{n}}{V}-\delta_{x},$$
i.e. for all $f \in C_{0}^{\infty}\left(X_{\text {reg }}\right)$, we have
$$\int_{X} \Delta f \cdot G(x, \cdot) \omega^{n}=\frac{1}{V} \int_{X} f \omega^{n}-f(x) .$$

Finally, the first and fourth item of Lemma 3.11 enable us to find a lower bound of the Green function as follows
$$\begin{aligned}
G(x, y) & =\int_{0}^{1} G(x, y, t) d t+\int_{1}^{+\infty} G(x, y, t) d t \\
& \geqslant-\frac{1}{V}-\frac{C}{n-1}
\end{aligned}$$
where $C$ only depends on the Sobolev and Poincaré constants of $\left(X_{\text {reg }}, \omega\right)$.
3.6. Green's inequality for general psh functions. - In this section, we assume that the assumptions of Lemma 3.11 are satisfied.

Let us first generalize Formula (3.8) to some functions $f \in \mathcal{C}^{\infty}\left(X_{\text {reg }}\right)$ that are not necessarily compactly supported. For that purpose, let $p: Y \rightarrow X$ a log resolution of singularities, let $D$ be the exceptional divisor of $p$ and let $Y^{\circ}:=p^{-1}\left(X_{\text {reg }}\right)=Y \backslash D$. We claim that for any $f \in \mathcal{C}^{\infty}\left(X_{\text {reg }}\right)$ such that $p^{*} f$ extends smoothly across $D$, the formula
$$\int_{X_{\mathrm{reg}}} \Delta f \cdot G(x, \cdot) \omega^{n}=\frac{1}{V} \int_{X_{\mathrm{reg}}} f \omega^{n}-f(x)$$
holds. First observe that all the terms are well-defined as one sees by pulling back by $p$, which is an isomorphism over $X_{\text {reg }}$. Indeed, recall that $x \in X_{\text {reg }}$ and that $G(x, \cdot)$ is locally bounded near $X_{\text {sing }}$ so that $p^{*} G(x, \cdot)$ is in $L^{1}\left(Y^{\circ}, \omega_{Y}\right)$ for any Kähler form $\omega_{Y}$ on $Y$.

Next, we choose a family $\left(\chi_{\delta}\right)_{\delta}$ of cut-off functions for $D$. As they are identically 0 on $D$, they come from $X$ under $p$ and one can see them either as functions on $X$ or $Y$ interchangeably. It is classical (cf e.g. [CGP13, Sect. 9]) that one can choose $\chi_{\delta}$ such that both $d \chi_{\delta} \wedge d^{c} \chi_{\delta}$ and $\pm d d^{c} \chi_{\delta}$ are dominated by some fixed Poincaré metric $\omega_{P}$ (independently of $\delta$ ). In particular, using Cauchy-Schwarz and the dominated convergence theorem, one finds
$$\lim _{\delta \rightarrow 0} \int_{X_{\mathrm{reg}}} G(x, \cdot)\left[f d d^{c} \chi_{\delta}+d f \wedge d^{c} \chi_{\delta}+d \chi_{\delta} \wedge d^{c} f\right] \wedge \omega^{n-1}=0$$
by the dominated convergence theorem. Formula (3.10) is now a direct application of (3.8).

The next result is the key for the proof of Proposition 3.3.
Claim 3.12. - Under the assumptions of Lemma 3.11, let $\varphi \in \operatorname{PSH}(X, \omega), V=\int_{X} \omega^{n}$ and let $x \in X_{\text {reg }}$. Then, one has
$$\frac{1}{V} \int_{X} \varphi \omega^{n}-\varphi(x) \geqslant n V \cdot \inf _{X_{\mathrm{reg}}} G(x, \cdot) .$$
Proof. - Replacing $\varphi$ by $\max (\varphi,-j)$ and letting $j \rightarrow+\infty$, one sees that it is enough to prove the claim for bounded functions $\varphi$. Next, thanks to Demailly's regularization theorem, one can write $p^{*} \varphi$ as a pointwise decreasing limit of smooth function $\psi_{\varepsilon}$ satisfying $p^{*} \omega+\varepsilon \omega_{Y}+d d^{c} \psi_{\varepsilon} \geqslant 0$ for some fixed Kähler metric $\omega_{Y}$ on $Y$. Using (3.10) and setting $G_{x}:=G(x, \cdot)$, one finds
$$\frac{1}{V} \int_{X} \varphi \omega^{n}-\varphi(x)=\lim _{\varepsilon \rightarrow 0} \int_{Y^{\circ}} n p^{*} G_{x} d d^{c} \psi_{\varepsilon} \wedge p^{*} \omega^{n-1}$$

Moreover, as $G_{x}$ have zero mean value, one has
$$\begin{aligned}
\int_{Y^{\circ}} p^{*} G_{x} d d^{c} \psi_{\varepsilon} \wedge p^{*} \omega^{n-1}= & \int_{Y^{\circ}}\left(p^{*} G_{x}-\inf _{X_{\mathrm{reg}}} G_{x}\right) d d^{c} \psi_{\varepsilon} \wedge p^{*} \omega^{n-1} \\
= & \int_{Y^{\circ}}\left(p^{*} G_{x}-\inf _{X_{\mathrm{reg}}} G_{x}\right)\left(p^{*} \omega+\varepsilon \omega_{Y}+d d^{c} \psi_{\varepsilon}\right) \wedge p^{*} \omega^{n-1} \\
& -\int_{Y^{\circ}} p^{*} G_{x} \wedge\left(p^{*} \omega+\varepsilon \omega_{Y}\right) \wedge p^{*} \omega^{n-1} \\
& +\inf _{X_{\mathrm{reg}}} G_{x} \cdot\left(V+\varepsilon \int_{Y} \omega_{Y} \wedge p^{*} \omega^{n-1}\right) \\
\geqslant & \inf _{X_{\mathrm{reg}}} G_{x} \cdot V+\varepsilon \cdot\left(\inf _{X_{\mathrm{reg}}} G_{x} \cdot \int_{Y} \omega_{Y} \wedge p^{*} \omega^{n-1}-\int_{Y^{\circ}} p^{*} G_{x} \omega_{Y} \wedge p^{*} \omega^{n-1}\right)
\end{aligned}$$
Taking the limit as $\varepsilon \rightarrow 0$, we get the expected result. \(\square\)
3.7. Proof of Proposition 3.3. — We can now finish the proof of Proposition 3.3. We are left to treating the cases where $\pi$ is projective or $X_{t}$ is smooth for $t \neq 0$. Moreover, we can assume that $n=\operatorname{dim} X_{t} \geqslant 2$ since otherwise, $X_{t}$ would have at most isolated singularities and we could then appeal to § 3.3, cf. Remark 3.7.

Moreover, the content of Proposition 3.3 is insensitive to replacing $\omega$ by another Kähler metric on $\mathcal{X}$. In the case where $\pi$ is projective, i.e. if we have $\mathcal{X} \subset \mathbb{P}^{N} \times \mathbb{D}$ such that $\pi$ commutes with the second projection, then we will assume that $\omega=\left.\omega_{\mathrm{FS}}\right|_{\mathcal{X}}$.

Finally, in the case where $X_{t}$ is smooth for $t \neq 0$, it is sufficient to prove Proposition 3.3 for $t \neq 0$ since it is already well-known that the $L^{1}$-sup comparison holds on the fixed irreducible complex space $X_{0}$.

We know from § 3.4 that the Kähler manifolds $\left(X_{t}^{\text {reg }}, \omega_{t}\right)$ admit uniform Poincaré and Sobolev constants. As the volume $V$ of $\left(X_{t}, \omega_{t}\right)$ is constant, it follows from (3.9) that there exists $C_{G}>0$ independent of $t$ such that
$$\forall x, y \in X_{t}^{\mathrm{reg}}, G_{t}(x, y) \geqslant-C_{G},$$
where $G_{t}(\cdot, \cdot)$ is the Green function of $\left(X_{t}, \omega_{t}\right)$. As $\varphi_{t}$ is sup-normalized and upper semi-continuous, there exists $x_{t} \in X_{t}^{\text {reg }}$ such that $\varphi_{t}\left(x_{t}\right) \geqslant-1$. Applying Claim 3.12 to $\varphi:=\varphi_{t}$ and $x:=x_{t}$, we find
$$\frac{1}{V} \int_{X_{t}}\left(-\varphi_{t}\right) \omega_{t}^{n} \leqslant n V C_{G}+1 .$$
The Proposition is proved.

\section*{4. Densities along a log canonical map}

We now pay attention to hypotheses (H2) and (H2'). We focus in this section on the integrability properties of some canonical densities.

\subsection*{4.1. Semi-stable model. -}

Setting 4.1. - Let $\pi: \mathcal{X} \rightarrow \mathbb{D}$ be a proper, holomorphic surjective map from a Kähler space $\mathcal{X}$ with connected fibers to the unit disk of relative dimension $n$. We make the following assumption
$$\text { For each } t \in \mathbb{D} \text {, the pair }\left(\mathcal{X}, X_{t}\right) \text { has log canonical singularities }$$
where $X_{t}=\pi^{-1}(t)$ is the schematic fiber at $t \in \mathbb{D}$, cf [KM98, Def. 7.1].
About the singularities. In Setting 4.1, the following properties hold
\begin{itemize}
\item[1.] Every fiber is reduced, $K_{\mathcal{X} / \mathbb{D}}$ is Q-Cartier and $\mathcal{X}$ has log canonical singularities.
\item[2.] The space $\mathcal{X}$ has canonical singularities if and only if the general fiber $X_{t}$ has canonical singularities, cf [KM98, Lem. 7.2].
\item[3.] The condition (4.1) is preserved by finite base change from a smooth curve, cf [KM98, Lem. 7.6].
\item[4.] If $\left(\mathcal{X}, X_{0}\right)$ has lc singularities, then $\left(\mathcal{X}, X_{t}\right)$ has lc singularities for $|t| \ll 1$, see [Kol13, Cor. 4.10 (2)] and [Kol18, Thm. 2.3].
\item[5.] By loc. cit., the condition (4.1) is equivalent to asking $\mathcal{X}$ to be normal, Q -Gorenstein, and that each fiber $X_{t}$ has semi- log canonical singularities.
\end{itemize}

By [KKMSD73], one can find a semi-stable model of $\pi^{(1)}$. More precisely, up to shrinking $\mathbb{D}$, there exists a finite cover $\varphi: t \mapsto t^{k}$ of the disk for some integer $k \geqslant 1$ and a proper, surjective birational morphism $f: \mathcal{X}^{\prime} \rightarrow \mathcal{X} \times_{\varphi} \mathbb{D}$
![](https://cdn.mathpix.com/cropped/a36c2a22-d4f8-428d-a076-7702e51fb997-38.jpg?height=199&width=492&top_left_y=1362&top_left_x=854)
such that $\mathcal{X}^{\prime}$ is smooth, $f$ is isomorphic over the smooth locus of $\pi$ and such that around any point $x^{\prime} \in X_{0}^{\prime}$, there exists an integer $p \leqslant n+1$ and a system of coordinates $\left(z_{0}, \ldots, z_{n}\right)$ centered at $x^{\prime}$ and such that $\pi^{\prime}\left(z_{0}, \ldots, z_{n}\right)=z_{0} \cdots z_{p}$.

Additional assumption. Up to shrinking $\mathbb{D}$, one will assume that $\pi^{\prime}$ is smooth away from 0 so that for any $t \neq 0$, the induced morphism $\left.(g \circ f)\right|_{X_{t}^{\prime}}: X_{t}^{\prime} \rightarrow X_{t}$ is a resolution of singularities. Note that $X_{t}^{\prime}$ need not be connected.

Let $m \geqslant 1$ be an integer such that $m K_{\mathcal{X} / \mathbb{D}}$ is a Cartier divisor. We can cover $\mathcal{X}$ with open sets $U_{i}$ such that $U_{i} \cap \mathcal{X}^{\text {reg }}$ admits a nowhere vanishing section $\Omega_{U_{i}} \in H^{0}\left(U_{i} \cap \mathcal{X}^{\text {reg }}, m K_{\mathcal{X} / \mathbb{D}}\right)$. For any $t \in \mathbb{D}$, the restriction $\left.\Omega_{U_{i}}\right|_{X_{t}^{\text {reg }}}$ defines a nowhere vanishing section $\left.\Omega_{U_{i}}\right|_{X_{t}^{\text {reg }}} \in H^{0}\left(U_{i} \cap X_{t}^{\text {reg }}, m K_{X_{t}}\right)$. In particular, $m K_{X_{t}}$ is a Cartier divisor for all $t$. We want to understand the behavior of the volume forms $\left.\left(\Omega_{U_{i}} \wedge \overline{\Omega_{U_{i}}}\right)\right|_{X_{t}^{\text {reg }}} ^{\frac{1}{m}}$ when $t \rightarrow 0$. In order to do so, it is enough to work on $\mathcal{X} \times_{\varphi} \mathbb{D}$

\footnotetext{
${ }^{(1)}$ The reference [KKMSD73] deals with the case of a proper morphism between algebraic varieties but the construction extends to the analytic case mutatis mutandis, as stated in e.g. [KM98, Thm. 7.17]
}
directly as explained below.
Reduction step. The finite map $g$ induces an isomorphism of Q-line bundles $K_{\mathcal{X} \times_{\varphi} \mathbb{D} / \mathbb{D}} \simeq g^{*} K_{\mathcal{X} / \mathbb{D}}$. In particular, one can replace $\mathcal{X}$ by $\mathcal{X} \times_{\varphi} \mathbb{D}$ in the following, or equivalently assume that $\varphi=\mathrm{Id}_{\mathbb{D}}$; i.e $k=1$. By what was said above, the "new" family still satisfies the condition (4.1).
4.2. Analytic expression of the densities in a semi-stable model. - Let us start with some notation. Once and for all, we fix an open set $U:=U_{i_{0}}$ for some $i_{0}$. We set $\Omega:=$ $\Omega_{U}$ and $\Omega_{t}:=\left.\Omega\right|_{X_{t}^{\text {reg }}}$. One can cover $f^{-1}(U)$ by a finite number of open subsets $V_{j} \subset \mathcal{X}^{\prime}$ isomorphic to the unit polydisk of $\mathbb{C}^{n+1}$ and endowed with a system of coordinates as above. We let $V:=V_{j_{0}}$ be one of them. The goal is to understand $f^{*} \Omega$ when restricted to $V$, using our preferred set of coordinates. Finally, we set $U_{t}:=U \cap X_{t}$ and $V_{t}:=V \cap X_{t}^{\prime}$.

Next, we write
$$K_{\mathcal{X}^{\prime}}+Y_{0}=f^{*}\left(K_{\mathcal{X}}+X_{0}\right)+\sum_{i \in I} a_{i} E_{i}$$
where the $E_{i}$ 's are $f$-exceptional divisors with $a_{i} \geqslant-1$ for all $i \in I$ and $Y_{0}$ is the strict transform of $X_{0}$. Note that some of the divisors $E_{i}$ 's may be irreducible components of $X_{0}^{\prime}$. The others surject onto $\mathbb{D}$ thanks to the additional assumption made in the previous section. The divisor $E:=\sum_{i \in I} E_{i}$ is the exceptional locus of $f$ and $E+Y_{0}$ has simple normal crossing support. We set $J:=\left\{i \in I ; a_{i}=-1\right\}$ which we assume to be non-empty and define the non-klt locus of $\left(\mathcal{X}, X_{0}\right)$ by
$$\operatorname{Nklt}\left(\mathcal{X}, X_{0}\right):=f\left(\bigcup_{j \in J} E_{j}\right)$$
One can check that $\operatorname{Nklt}\left(\mathcal{X}, X_{0}\right)$ does indeed not depend on the particular choice of $f$, hence the notation. Under our assumptions, the above analytic set contains the non-klt locus of every fiber $X_{t}, t \in \mathbb{D}$. This is an easy consequence of the adjunction formula, at least when the $X_{t}$ 's are normal. Given $K \subset I$, we set $E_{K}=\cap_{i \in K} E_{i}$ and introduce the invariants
$$v(f):=\max \left\{|K| ; K \subset J, E_{K} \neq \varnothing\right\}, \quad \text { and } \quad v:=\inf _{f}\{v(f)\}$$
where the infimum is taken over all the semistable models of $\mathcal{X} \rightarrow \mathbb{D}$.
We now let $x^{\prime} \in Y_{0}$ and we assume that the coordinates mentioned above are chosen such that $Y_{0}=\left(z_{0} \cdots z_{r}=0\right)$ locally for $0 \leqslant r \leqslant p$ being the number of irreducible components of $Y_{0}$ minus one on that chosen open set.

On $V_{t}, t \neq 0$, the functions $\left(z_{1}, \ldots, z_{n}\right)$ induce a system of coordinates and the form $f^{*} \Omega$ on $V$ can be seen as a collection of $m$-th powers of holomorphic $n$-forms
$$f^{*} \Omega_{t}=g_{t}\left(z_{1}, \ldots, z_{n}\right)\left(d z_{1} \wedge \cdots \wedge d z_{n}\right)^{\otimes m}$$
for some holomorphic function $g_{t}$ on $V_{t} \backslash E$, with poles of order at most $\left(-m a_{i}\right)_{+}$along $E_{i} \cap X_{t}$. The form $\Omega \wedge \pi^{*}\left(\frac{d t}{t}\right)^{\otimes m}$ is trivialisation of $m\left(K_{\mathcal{X}}+X_{0}\right)$ over $U^{\text {reg }}$. The pullback $f^{*}\left(\Omega \wedge \pi^{*}\left(\frac{d t}{t}\right)^{\otimes m}\right)$ is a well-defined $m$-th power of a $(n+1)$-form on $f^{-1}\left(U^{\text {reg }}\right)$ with logarithmic poles along $Y_{0}$ that extends meromorphically to $f^{-1}(U)$ with poles of order at most $\left(-m a_{i}\right)_{+}$along $E_{i}$. As
$$f^{*} \pi^{*}\left(\frac{d t}{t}\right)=\left(\pi^{\prime}\right)^{*}\left(\frac{d t}{t}\right)=\sum_{i=0}^{p} \frac{d z_{i}}{z_{i}}$$
on $V$, the form $f^{*}\left(\Omega \wedge \pi^{*}\left(\frac{d t}{t}\right)^{\otimes m}\right)$ is equal on that set to
$$(-1)^{m n}\left(z_{1} \cdots z_{r}\right)^{m} g_{\pi^{\prime}(z)}\left(z_{1}, \ldots, z_{n}\right)\left(\frac{d z_{0}}{z_{0}} \wedge \frac{d z_{1}}{z_{1}} \wedge \cdots \wedge \frac{d z_{r}}{z_{r}} \wedge d z_{r+1} \wedge \cdots \wedge d z_{n}\right)^{\otimes m}$$
so that the function $\left(V \backslash E \cup Y_{0}\right) \ni z \mapsto(-1)^{n m}\left(z_{1} \cdots z_{r}\right)^{m} g_{\pi^{\prime}(z)}\left(z_{1}, \ldots, z_{n}\right)$ extends to a meromorphic function $h$ on $V$, holomorphic along $Y_{0}$ and with poles of order at most $\left(-m a_{i}\right)_{+}$along $E_{i}$ and satisfying
$$f^{*} \Omega_{t}=(-1)^{m n} \frac{h(z)}{\left(z_{1} \cdots z_{r}\right)^{m}}\left(d z_{1} \wedge \cdots \wedge d z_{n}\right)^{\otimes m}$$
on $V_{t}$, for $t \neq 0$. When $t=0$, one can also obtain a formula as above for $f^{*} \Omega_{0}$ but it requires to first choose a component $Y_{0}^{(k)}$ of $Y_{0}$. Let $0 \leqslant i \leqslant r$ such that $Y_{0}^{(k)} \cap V_{0}=\left(z_{i}=\right.$ 0 ). On that set (say after removing $E$ ), one has
$$f^{*} \Omega_{0}=(-1)^{i+m n} \frac{h(z)}{\left(z_{1} \cdots \widehat{z}_{i} \cdots z_{r}\right)^{m}}\left(d z_{0} \wedge \cdots \wedge \widehat{d z_{i}} \wedge \cdots \wedge d z_{n}\right)^{\otimes m} .$$
Note that if $X_{0}$ (or equivalenty, $Y_{0}$ ) is irreducible, then $r=0$ in the formula above.
Claim 4.2. - If $X_{0}$ has canonical singularities, then $r=0$ and the meromorphic function $V \ni z \mapsto h(z)$ is holomorphic on $V$.

Proof. - As $X_{0}$ is normal, it is irreducible, hence $Y_{0}$ is smooth and irreducible. In particular, the map $\left.f\right|_{Y_{0}}: Y_{0} \rightarrow X_{0}$ induces a resolution of singularities.

As $X_{0}$ has canonical singularities, the pull-back $f^{*} \Omega_{0}$ of the form $\Omega_{0}$ on $X_{0}^{\text {reg }} \cap U$ extends holomorphically across $\Upsilon_{0} \cap E$. Given (4.7), it means that $h \mid V \cap Y_{0}$ extends holomorphically along each $E_{i} \cap Y_{0}$. As $h$ is holomorphic on $V$ and does not vanish outside $V_{0}$, its divisor is an $n$-dimensional variety supported on $V \cap E$, therefore $\operatorname{div}(h)=\sum b_{i} E_{i}$ for some integers $b_{i}$. As $E+Y_{0}$ is snc, the decomposition $\operatorname{div}\left(\left.h\right|_{Y_{0}}\right)=\sum b_{i}\left(E_{i} \cap Y_{0}\right)$ is the decomposition into irreducible components. As $\left.h\right|_{Y_{0}}$ is holomorphic along the nonempty set $Y_{0} \cap E_{i}$, we have necessarily $b_{i} \geqslant 0$ for any $i$. The claim is proved. \(\square\)

\subsection*{4.3. Integrability properties of the canonical densities. -}

Definition 4.3. - In Setting 4.1, let $\omega$ be a Kähler form on $\mathcal{X}$. We define the function $\gamma$ on $U \cap \mathcal{X}_{\text {reg }}$ by
$$(\Omega \wedge \bar{\Omega})^{\frac{1}{m}}=e^{-\gamma} \omega^{n} .$$

We want to analyze the integrability properties of $e^{-\gamma}$. Arguing as in the proof of [RZ11a, Thm. B.1(i)] (see also [EGZ09, Lem. 6.4]), it is easy to infer from the normality of $\mathcal{X}$ that given any small open set $U^{\prime} \subset U$, there exist bounded holomorphic functions $\left(f_{1}, \cdots, f_{\ell}\right)$ on $U^{\prime}$ such that $V\left(f_{1}, \ldots, f_{\ell}\right) \subset U_{\text {sing }}^{\prime}$ and
$$\left.\gamma\right|_{U_{\mathrm{reg}}^{\prime}}=\frac{1}{m} \log \sum_{i}\left|f_{i}\right|^{2} .$$
Let us pick a section $s_{E} \in H^{0}\left(\mathcal{X}^{\prime}, \mathcal{O}_{\mathcal{X}^{\prime}}(E)\right)$ cutting out the exceptional divisor $E$ and let us choose $|\cdot|$ a smooth hermitian metric on $\mathcal{O}_{\mathcal{X}^{\prime}}(E)$. Given (4.8), there exists a constant $A>0$ such that
$$f^{*} \gamma \geqslant A \log \left|s_{E}\right|^{2} .$$
We have the following
Lemma 4.4. - Assume that $X_{0}$ has canonical singularities and set $\omega_{t}:=\left.\omega\right|_{X_{t}}$. Then up to shrinking $\mathbb{D}$, there exists $p>1$ and a constant $C>0$ such that for any $t \in \mathbb{D}$, one has
$$\int_{U_{t}} e^{-p \gamma} \omega_{t}^{n} \leqslant C .$$
Proof. - We set $p:=1+\delta$ for some $\delta>0$ small enough to be chose later. Given (4.9), we have
$$\int_{U_{t}} e^{-p \gamma} \omega_{t}^{n}=\int_{f^{-1}\left(U_{t}\right)} e^{-\delta f^{*} \gamma} f^{*}\left(\Omega_{t} \wedge \bar{\Omega}_{t}\right)^{\frac{1}{m}} \leqslant \int_{f^{-1}\left(U_{t}\right)}\left|s_{E}\right|^{-2 \delta A} f^{*}\left(\Omega_{t} \wedge \bar{\Omega}_{t}\right)^{\frac{1}{m}} .$$
Now, one can cover $f^{-1}\left(U_{t}\right)$ by finitely many open sets $V_{t}=V \cap X_{t}^{\prime}$ as above. On $V$, the system of coordinates $\left(z_{0}, \ldots, z_{n}\right)$ induces a system of coordinates $\left(z_{1}, \ldots, z_{n}\right)$ such that we have
$$\left|s_{E}\right|^{-2 \delta A} f^{*}\left(\Omega_{t} \wedge \bar{\Omega}_{t}\right)^{\frac{1}{m}} \leqslant C \prod_{i=1}^{p}\left|z_{i}\right|^{-2 \delta A} i d z_{1} \wedge d \bar{z}_{1} \wedge \cdots \wedge i d z_{n} \wedge d \bar{z}_{n}$$
for some uniform constant $C$ thanks to (4.6) and Claim 4.2. Recall that $V=\prod_{i=0}^{n}\left\{\left|z_{i}\right|<\right.$ $1\} \subset \mathbb{C}^{n+1}$ and
$$V_{t}=V \cap\left\{z_{0} \cdots z_{p}=t\right\} \hookrightarrow\left\{\left(z_{1}, \ldots, z_{n}\right) \in \mathbb{C}^{n} ; t \leqslant\left|z_{i}\right|<1\right\} \subset \mathbb{D}^{n} .$$
where the injective map is given by $\left.\operatorname{pr}_{z_{1}, \ldots, z_{n}}\right|_{V_{t}}$, i.e. the restriction to $V_{t}$ of the projection map onto the last $n$ coordinates in $\mathbb{C}^{n+1}$. For $\delta$ small enough, the function $\mathbb{D} \ni z \mapsto$ $|z|^{-\delta A}$ is integrable with respect to the area measure; this concludes the proof. \(\square\)

For the next lemma, we come back to the general case. We start by choosing a component $Y_{0}^{\left(k_{0}\right)}$ of $Y_{0}$, and we denote by $X_{0}^{\left(k_{0}\right)}$ the irreducible component of $X_{0}$ birational to $Y_{0}^{\left(k_{0}\right)}$ via $f$. Next, we consider the reduced divisor $F$ on $\mathcal{X}^{\prime}$ whose support consists of the union of the other components $Y_{0}^{(k)}, k \neq k_{0}$, along with the divisors $E_{i}$ whose discrepancy $a_{i}$ is equal to -1 , cf (4.3).

Let $h_{F}$ be a smooth hermitian metric on $\mathcal{O}_{\mathcal{X}^{\prime}}(F)$ and let $s_{F} \in H^{0}\left(\mathcal{X}^{\prime}, \mathcal{O}_{\mathcal{X}^{\prime}}(F)\right)$ such that $\operatorname{div}\left(s_{F}\right)=F$. We let
$$\psi_{F}:=-\log \left(-\log \left|s_{F}\right|_{h_{F}}^{2}\right) .$$

Similarly, let $F_{\text {klt }}:=E-F \cap E$, and let $\psi_{\text {klt }}:=\log \left|s_{F_{\text {klt }}}\right|^{2}$.
Claim 4.5. - There exists $\delta>0$ small enough such that for any $\varepsilon>0$, there exists a constant $C_{\varepsilon}$ such that for any $t \in \mathbb{D}$,
$$\int_{f^{-1}\left(U_{t}\right)} e^{(v(f)+\varepsilon) \psi_{F}-\delta \psi_{\mathrm{klt}}} f^{*}\left(\Omega_{t} \wedge \bar{\Omega}_{t}\right)^{\frac{1}{m}} \leqslant C_{\varepsilon},$$
where $v(f)$ is defined in (4.5).
Proof. - The statement is local on $\mathcal{X}^{\prime}$, so it is enough to control the integrals over $V_{t}$. Up to relabelling, one can assume that $Y_{0}^{\left(k_{0}\right)} \cap V=\left(z_{0}=0\right), F \cap V=\left(z_{1} \cdots z_{s}=0\right)$ so that for $s+1 \leqslant i \leqslant p, f^{*} \Omega_{t}$ has a pole of order at most $m-1$ along $\left(z_{i}=0\right)$. Given the definition of $v(f)$, we have
$$v(f) \geqslant s .$$
We implicitly assumed that $V$ meets $Y_{0}^{\left(k_{0}\right)}$; it actually does not matter much for the computation which is insensitive to whether that condition is fulfilled or not. Using (4.6), our integral is bounded by the following one
$$\int_{V_{t}} \frac{1}{\prod_{i=1}^{s}\left|z_{i}\right|^{2}} \cdot \frac{1}{\left(-\log \prod_{i=1}^{s}\left|z_{i}\right|\right)^{v(f)+\varepsilon}} \cdot \prod_{i=s+1}^{p} \frac{1}{\left|z_{i}\right|^{2\left(\delta-a_{i}\right)}} \cdot d \lambda_{\mathbb{C}^{n}}$$
where $-1<a_{i}<0$ and $V=\prod_{i=0}^{n}\left\{\left|z_{i}\right|<1\right\} \subset \mathbb{C}^{n+1}$ and $V_{t}=V \cap\left\{z_{0} \cdots z_{p}=t\right\}$. By Fubini theorem, one can reduce the integral to $V_{t}^{p}:=V_{t} \cap \mathbb{C}^{p+1}$ (i.e. fixing $z_{p+1}, \ldots, z_{n}$ ). There is no harm in assuming that $\delta<\min _{i} \frac{1+a_{i}}{2}$ so that the integral is bounded by
$$\int_{V_{t}^{p}} \frac{1}{\prod_{i=1}^{s}\left|z_{i}\right|^{2}} \cdot \frac{1}{\left(-\log \prod_{i=1}^{s}\left|z_{i}\right|\right)^{v(f)+\varepsilon}} \cdot \prod_{i=s+1}^{p} \frac{1}{\left|z_{i}\right|^{2(1-\delta / 2)}} \cdot d \lambda_{\mathbb{C}^{p}}$$
Using polar coordinates, one can assume that $t$ is real (in $(0,1)$ ) and the integral becomes over $W_{t}:=\left\{\left(r_{i}\right)_{1 \leqslant i \leqslant p} \in[0,1 / 2]^{p} ; r_{1} \ldots r_{p} \geqslant t\right\}$
$$\int_{W_{t}} \frac{1}{\prod_{i=1}^{s} r_{i} \cdot\left(-\log \prod_{i=1}^{s} r_{i}\right)^{v(f)+\varepsilon}} \cdot \prod_{i=s+1}^{p} \frac{1}{r_{i}^{1-\delta}} \cdot d \lambda_{\mathbb{R}^{p}} .$$
As $W_{t} \subset \prod_{i=1}^{p}\left\{t \leqslant r_{i} \leqslant 1 / 2\right\}$ and the function $r \mapsto \frac{1}{r^{1-\delta}}$ is integrable on [0, 1/2], one can appeal to Fubini's theorem to reduce the problem to showing convergence of the integral
$$\int_{[0,1]^{s}} \frac{d r_{1} \ldots d r_{s}}{\prod_{i=1}^{s} r_{i} \cdot\left(-\log \prod_{i=1}^{s} r_{i}\right)^{v(f)+\varepsilon}}$$
Now, we inductively use the formula for $\alpha>1$ :
$$\int_{[0,1]^{2}} \frac{d x d y}{x y(-\log x y)^{\alpha}}=\frac{1}{\alpha-1} \int_{0}^{1} \frac{d x}{x(-\log x)^{\alpha-1}}$$
to see that the integral $\int_{[0,1]^{s}} \frac{d x_{1} \ldots d x_{s}}{x_{1} \ldots x_{s}\left(-\log x_{1} \ldots x_{s}\right)^{\alpha}}$ converges if and only if $\alpha>s$. The conclusion now follows from the observation above and the inequality (4.11). \(\square\)

The result above allows us to generalize Lemma 4.4 when no assumption on the central fiber is made. To do so, we first need some notation. The function $\psi_{F}$ is well defined on $\mathcal{X}^{\prime}$ but it does not necessarily come from $\mathcal{X}$. Given that $\operatorname{Nklt}\left(\mathcal{X}, X_{0}\right)$ is an analytic set in $\mathcal{X}$ and up to shrinking D a little, one can construct a function $\rho$ such that
\begin{itemize}
\item[-] $\rho \leqslant-1$ on $\mathcal{X}$.
\item[-] $\rho$ is quasi-psh and has analytic singularities along $\operatorname{Nklt}\left(\mathcal{X}, X_{0}\right)$; in particular, it is identically $-\infty$ on that set.
\end{itemize}
We set
$$\psi:=-\log (-\rho) \quad \text { on } \mathcal{X} .$$
Up to scaling $\rho$, one can assume that
$$f^{*} \psi \leqslant \psi_{F} .$$
Next, we introduce for $\varepsilon>0$ the function $\gamma_{\varepsilon}:=\gamma-(n+v(f)+2 \varepsilon) \psi$ defined on $U$. In other words, one has
$$e^{(n+v(f)+2 \varepsilon) \psi}(\Omega \wedge \bar{\Omega})^{\frac{1}{m}}=e^{-\gamma_{\varepsilon}} \omega^{n} .$$

Lemma 4.6. — With the notation above, there exists a constant $\widetilde{\mathrm{C}}_{\varepsilon}$ such that
$$\int_{U_{t}}\left|\gamma_{\varepsilon}\right|^{n+\varepsilon} e^{-\gamma_{\varepsilon}} \omega_{t}^{n} \leqslant \widetilde{C}_{\varepsilon}$$
for any $t \in \mathbb{D}$.
Proof. - In order to compute the integral, we pull it back by $f$ and work on $V_{t}$. We have successively
$$\begin{aligned}
\left|f^{*} \gamma_{\varepsilon}\right| & \lesssim-\log \left|s_{E}\right|+\log \left(-\log \left|s_{F}\right|\right) \\
& \lesssim-\log \left|s_{F}\right|-\log \left|s_{F_{\mathrm{klt}}}\right| .
\end{aligned}$$
The first inequality is a combination of (4.9) and (4.13). To obtain the second inequality, we use the fact that $E=F \cup F_{\text {klt }}$ to split the term $\log \left|s_{E}\right|$ while $\log \left(-\log \left|s_{F}\right|\right)$ can be absorbed by the more singular $-\log \left|s_{F}\right|$. The integral to bound becomes
$$\int_{V_{t}}\left[\left(-\log \left|s_{F}\right|\right)^{n+\varepsilon}+\left(-\log \left|s_{F_{\mathrm{klt}}}\right|\right)^{n+\varepsilon}\right] e^{(n+v(f)+2 \varepsilon) \psi_{F}} f^{*}\left(\Omega_{t} \wedge \bar{\Omega}_{t}\right)^{\frac{1}{m}}$$
which itself is controled by
$$\int_{V_{t}} e^{(v(f)+\varepsilon) \psi_{F}} f^{*}\left(\Omega_{t} \wedge \bar{\Omega}_{t}\right)^{\frac{1}{m}}+\int_{V_{t}} e^{(n+1) \psi_{F}-\delta \psi_{\mathrm{klt}}} f^{*}\left(\Omega_{t} \wedge \bar{\Omega}_{t}\right)^{\frac{1}{m}}$$
for any given $\delta>0$. The lemma now follows from Claim 4.5. \(\square\)

\section*{5. Negative curvature}

In this section we apply our previous results to the study of families of varieties with "negative canonical bundle": we consider families of manifolds of general type, as well as families of "stable varieties".

\subsection*{5.1. Families of manifolds of general type. -}

Setting 5.1. - Let $\mathcal{X}$ be an irreducible and reduced complex space endowed with a Kähler form $\omega$ and a proper, holomorphic map $\pi: \mathcal{X} \rightarrow \mathbb{D}$. We assume that for each $t \in \mathbb{D}$, the (schematic) fiber $X_{t}$ is a $n$-dimensional Kähler manifold $X_{t}$ of general type, i.e. such that its canonical bundle $K_{X_{t}}$ is big. In particular, $\mathcal{X}$ is automatically non-singular and the map $\pi$ is smooth. One can view the fibers $X_{t}$ as deformations of $X_{0}$.
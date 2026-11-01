---
retention_scope: session
part: 3
total_parts: 4
---

[Part 3/4 of: Monopoles over 4-manifolds containing long necks, I]

In the following lemma, Sobolev norms of sections of the spinor bundle $\mathbb{S}_{Y}$ over $Y$ will be taken with respect to $B_{0}$ and some fixed connection in the tangent bundle $T Y$. This means that the same constant $\epsilon$ will work if $\alpha$ is replaced with some monopole gauge equivalent to $\alpha$.

Lemma 6.2 In the above situation there exists an $\epsilon>0$ such that if $S$ is any smooth monopole over the band $(-1,1) \times Y$ satisfying $\left\|S_{0}-\alpha\right\|_{L_{1}^{2}(Y)} \leq \epsilon$ then
$$\pm 2 \lambda^{ \pm}\left(\vartheta\left(S_{0}\right)-\vartheta(\alpha)\right) \leq-\left.\partial_{t}\right|_{0} \vartheta\left(S_{t}\right) .$$

Proof Choose a smooth $u:(-1,1) \times Y \rightarrow \mathrm{U}(1)$ such that $u(S)$ is in temporal gauge. Then
$$\partial_{t} \vartheta\left(S_{t}\right)=\partial_{t} \vartheta\left(u_{t}\left(S_{t}\right)\right)=-\left\|\nabla \vartheta\left(u_{t}\left(S_{t}\right)\right)\right\|_{2}^{2}=-\left\|\nabla \vartheta\left(S_{t}\right)\right\|_{2}^{2} .$$
If $\epsilon>0$ is sufficiently small then by the local slice theorem we can find a smooth $v: Y \rightarrow \mathrm{U}(1)$ which is $L_{2}^{2}$ close to 1 and such that $\mathcal{I}_{\alpha}^{*}\left(v\left(S_{0}\right)-\alpha\right)=0$. We now apply Lemma 6.1 with $E$ the kernel of $\mathcal{I}_{\alpha}^{*}$ in $L_{1}^{2}, E^{\prime}$ the kernel of $\mathcal{I}_{\alpha}^{*}$ in $L^{2}$, and $f(x)= \pm(\vartheta(\alpha+x)-\vartheta(\alpha))$. The assumption that $\alpha$ be non-degenerate means that $H=\widetilde{H}_{\alpha}: E \rightarrow E^{\prime}$ is an isomorphism, so the lemma follows. \(\square\)
6.2 Estimates over $[0, T] \times Y$

Let $\alpha$ be a non-degenerate critical point of $\vartheta$ and $\underline{\alpha}=(B, \Psi)$ the monopole over $\mathbb{R} \times Y$ that $\alpha$ defines. Throughout this subsection, the same convention for Sobolev norms of sections of $\mathbb{S}_{Y}$ will apply as in Lemma 6.2. For Sobolev norms of sections of the spinor bundles over (open subsets of) $\mathbb{R} \times Y$ we will use the connection $B$.

Throughout this subsection $S=(A, \Phi)$ will be a monopole over a band $\mathbf{B}=$ $[0, T] \times Y$ where $T \geq 1$. Set $s=(a, \phi)=S-\underline{\alpha}$ and
$$\begin{gathered}
\delta=\|s\|_{L_{2}^{2}(\mathbf{B})}^{2}, \\
\nu^{2}=\left\|\nabla \vartheta_{S}\right\|_{L^{2}(\mathbf{B})}^{2}=\vartheta\left(S_{0}\right)-\vartheta\left(S_{T}\right) .
\end{gathered}$$
The main result of this subsection is Proposition 6.1, which asserts in particular that if $\delta$ is sufficiently small then $S$ is gauge equivalent to a configuration $\widetilde{S}$ which is in Coulomb gauge with respect to $\underline{\alpha}$ and satisfies $\|\widetilde{S}-\underline{\alpha}\|_{L_{1}^{2}(\mathbf{B})} \leq$ const $\cdot \nu$.

We will assume $\delta \leq 1$. Let $a^{\prime}$ denote the contraction of $a$ with the vector field $\partial_{1}=\frac{\partial}{\partial t}$. Quantities referred to as constants or denoted "const" may depend on $Y, \eta,[\alpha], T$ but not on $S$. Note that
$$\nu \leq \text { const } \cdot\left(\|s\|_{1,2}+\|s\|_{1,2}^{2}\right) \leq \text { const },$$
the last inequality because $\delta \leq 1$.
For real numbers $t$ set
$$i_{t}: Y \rightarrow \mathbb{R} \times Y, \quad y \mapsto(t, y) .$$
If $\omega$ is any differential form over B set $\omega_{t}=i_{t}^{*} \omega, 0 \leq t \leq T$. Similar notation will be used for connections and spinors over B.

Lemma 6.3 There is a constant $C_{0}>0$ such that
$$\left\|\partial_{1} \phi\right\|_{2} \leq C_{0}\left(\nu+\left\|a^{\prime}\right\|_{3}\right) .$$

Proof We have
$$\partial_{1} \phi=\partial_{1} \Phi=\nabla_{1}^{A} \Phi-a^{\prime} \Phi,$$
where $\nabla_{1}^{A}$ is the covariant derivative with respect to $A$ in the direction of the vector field $\partial_{1}=\frac{\partial}{\partial t}$. Now $\left|\nabla_{1}^{A} \Phi\right|$ depends only on the gauge equivalence class of $S=(A, \Phi)$, and if $A$ is in temporal gauge (ie if $a^{\prime}=0$ ) then $\left(\nabla_{1}^{A} \Phi\right)_{t}=\partial_{A_{t}} \Phi_{t}$. The lemma now follows because $\delta \leq 1$. \(\square\)

Lemma 6.4 There is a constant $C_{1}>0$ such that if $\delta$ is sufficiently small then the following hold:
\begin{itemize}
\item[(i)] $\|\phi\|_{1,2} \leq C_{1}\left(\left\|\mathcal{I}_{\underline{\alpha}}^{*} s\right\|_{2}+\left\|a^{\prime}\right\|_{1,2}+\nu\right)$,
\item[(ii)] There is a smooth $\check{f}: \mathbf{B} \rightarrow i \mathbb{R}$ such that $\check{s}=(\check{a}, \check{\phi})=\exp (\check{f})(S)-\underline{\alpha}$ satisfies
$$\left\|\check{s}_{t}\right\|_{1,2} \leq C_{1}\left\|\nabla \vartheta_{S_{t}}\right\|_{2}, \quad 0 \leq t \leq T,$$
\item[(iii)] $\|d a\|_{2} \leq C_{1} \nu$,
\end{itemize}
where in (i) and (iii) all norms are taken over B.

Proof The proof will use an elliptic inequality over $Y$, the local slice theorem for $Y$, and the gradient flow description of the Seiberg-Witten equations over $\mathbb{R} \times Y$.
(i) Since $\alpha$ is non-degenerate we have
$$\|z\|_{1,2} \leq \mathrm{const} \cdot\left\|\left(\mathcal{I}_{\alpha}^{*}+H_{\alpha}\right) z\right\|_{2}$$
for $L_{1}^{2}$ sections $z$ of $(i \Lambda \oplus \mathbb{S})_{Y}$. Recall that
$$\nabla \vartheta_{\alpha+z}=H_{\alpha} z+z \otimes z$$
where $z \otimes z$ represents a pointwise quadratic function of $z$. Furthermore, $\| z \otimes$ $z \|_{2} \leq$ const $\cdot\|z\|_{1,2}^{2}$. If $\|z\|_{1,2}$ is sufficiently small then we can rearrange to get
$$\|z\|_{1,2} \leq \text { const } \cdot\left(\left\|\mathcal{I}_{\alpha}^{*} z\right\|_{2}+\left\|\nabla \vartheta_{\alpha+z}\right\|_{2}\right) .$$
By the Sobolev embedding theorem we have
$$\left\|s_{t}\right\|_{L_{1}^{2}(Y)} \leq \text { const } \cdot\|s\|_{L_{2}^{2}(\mathbf{B})}, \quad t \in[0, T],$$
for some constant independent of $t$, so we can apply inequality (33) with $z=s_{t}$ when $\delta$ is sufficiently small. Because
$$\left(\mathcal{I}_{\underline{\alpha}}^{*} s-\partial_{1} a^{\prime}\right)_{t}=\mathcal{I}_{\alpha}^{*} s_{t}$$
we then obtain
$$\int_{0}^{T}\left\|s_{t}\right\|_{L_{1}^{2}(Y)}^{2} d t \leq \mathrm{const} \cdot\left(\left\|\mathcal{I}_{\underline{x}}^{*} s\right\|_{L^{2}(\mathbf{B})}^{2}+\left\|\partial_{1} a^{\prime}\right\|_{L^{2}(\mathbf{B})}^{2}+\nu^{2}\right) .$$
This together with Lemma 6.3 establishes (i).
(ii) Choose a base-point $y_{0} \in Y$. By the local slice theorem there is a constant $C$ such that if $\delta$ is sufficiently small then for each $t \in[0, T]$ there is a unique smooth $\check{f}_{t}: Y \rightarrow i \mathbb{R}$ such that
\begin{itemize}
\item[-] $\left\|\check{f}_{t}\right\|_{2,2} \leq C \delta$,
\item[-] $\check{f}_{t}\left(y_{0}\right)=0$ if $\alpha$ is reducible,
\item[-] $\check{s}_{t}=\exp \left(\check{f}_{t}\right)\left(S_{t}\right)-\alpha$ satisfies $\mathcal{I}_{\alpha}^{*} \check{s}_{t}=0$.
\end{itemize}
It is not hard to see that the function $\check{f}: \mathbf{B} \rightarrow i \mathbb{R}$ given by $\check{f}(t, y)=\check{f}_{t}(y)$ is smooth. Moreover, $\left\|\check{s}_{t}\right\|_{1,2} \leq$ const $\cdot\left\|s_{t}\right\|_{1,2}$. Part (ii) then follows by taking $z=\check{s}_{t}$ in (33).
(iii) Choose a smooth $u: \mathbf{B} \rightarrow \mathrm{U}(1)$ such that $u(S)$ is in temporal gauge, and set $(\underline{a}, \underline{\phi})=u(S)-\underline{\alpha}$. Then
$$d a=d \underline{a}=d t \wedge \partial_{1} \underline{a}+d_{Y} \underline{a}=-d t \wedge \nabla_{1} \vartheta_{S_{t}}+d_{Y} \check{a}_{t},$$
where $\nabla_{1} \vartheta$ is the first component of $\nabla \vartheta$. This yields the desired estimate on da. \(\square\)

Lemma 6.5 Let $\left\{v_{1}, \ldots, v_{b_{1}(Y)}\right\}$ be a family of closed 2-forms on $Y$ which represents a basis for $H^{2}(Y ; \mathbb{R})$. Then there is a constant $C$ such that
$$\|b\|_{L_{1}^{2}(\mathbf{B})} \leq C\left(\left\|\left(d^{*}+d\right) b\right\|_{L^{2}(\mathbf{B})}+\left\|\left.(* b)\right|_{\partial \mathbf{B}}\right\|_{L_{1 / 2}^{2}(\partial \mathbf{B})}+\sum_{j}\left|\int_{\mathbf{B}} d t \wedge \pi^{*} v_{j} \wedge b\right|\right)$$
for all $L_{1}^{2} 1$-forms $b$ on $\mathbf{B}$, where $\pi: \mathbf{B} \rightarrow Y$ is the projection.
Proof Let $K$ denote the kernel of the operator
$$\Omega_{\mathbf{B}}^{1} \rightarrow \Omega_{\mathbf{B}}^{0} \oplus \Omega_{\mathbf{B}}^{2} \oplus \Omega_{\partial \mathbf{B}}^{0}, \quad b \mapsto\left(d^{*} b, d b,\left.* b\right|_{\partial \mathbf{B}}\right) .$$
Then we have an isomorphism
$$\rho: K \stackrel{\approx}{\rightarrow} H^{1}(Y ; \mathbb{R}), \quad b \mapsto\left[b_{0}\right] .$$
For on the one hand, an application of Stokes' theorem shows that $\rho$ is injective. On the other hand, any $c \in H^{1}(Y ; \mathbb{R})$ can be represented by an harmonic 1-form $\omega$, and $\pi^{*} \omega$ lies in $K$, hence $\rho$ is surjective.
It follows that every element of $K$ is of the form $\pi^{*}(\omega)$. Now apply Proposition 4.1 and Lemma 5.1 \(\square\)

Lemma 6.6 There is a smooth map $\hat{f}: \mathbf{B} \rightarrow i \mathbb{R}$, unique up to an additive constant, such that $\hat{a}=a-d \hat{f}$ satisfies
$$d^{*} \hat{a}=0,\left.\quad(* \hat{a})\right|_{\partial \mathbf{B}}=0 .$$
Given any such $\hat{f}$, if we set $\hat{s}=(\hat{a}, \hat{\phi})=\exp (\hat{f})(S)-\underline{\alpha}$ then
$$\|\hat{a}\|_{L_{1}^{2}(\mathbf{B})} \leq C_{2} \nu, \quad\|\hat{s}\|_{L_{2}^{2}(\mathbf{B})} \leq C_{2} \delta$$
for some constant $C_{2}>0$.

Proof The first sentence of the lemma is just the solution to the Neumann problem. If we fix $x_{0} \in \mathbf{B}$ then there is a unique $\hat{f}$ as in the lemma such that $\hat{f}\left(x_{0}\right)=0$, and we have $\|\hat{f}\|_{3,2} \leq$ const $\cdot\|a\|_{2,2}$. Writing
$$\hat{\phi}=\exp (\hat{f}) \Phi-\Psi=(\exp (\hat{f})-1) \Phi+\phi$$
and recalling that, for functions on B, multiplication is a continuous map $L_{3}^{2} \times$ $L_{k}^{2} \rightarrow L_{k}^{2}$ for $0 \leq k \leq 3$, we get
$$\begin{aligned}
\|\hat{\phi}\|_{2,2} & \leq C\|\exp (\hat{f})-1\|_{3,2}\|\Phi\|_{2,2}+\|\phi\|_{2,2} \\
& \leq C^{\prime}\|\hat{f}\|_{3,2} \exp \left(C^{\prime \prime}\|\hat{f}\|_{3,2}\right)+\|\phi\|_{2,2} \\
& \leq C^{\prime \prime \prime}\left\|_{s}\right\|_{2,2}
\end{aligned}$$
for some constants $C, \ldots, C^{\prime \prime \prime}$, since we assume $\delta \leq 1$. There is clearly a similar $L_{2}^{2}$ bound on $\hat{a}$, so this establishes the $L_{2}^{2}$ bound on $\hat{s}$.

We now turn to the $L_{1}^{2}$ bound on $\hat{a}$. Let $\check{a}$ be as in Lemma 6.4 Since $\hat{a}-\check{a}$ is exact we have
$$\left|\int_{Y} v \wedge \hat{a}_{t}\right|=\left|\int_{Y} v \wedge \check{a}_{t}\right| \leq \text { const } \cdot\|v\|_{2}\left\|\check{a}_{t}\right\|_{2}$$
for any closed $v \in \Omega_{Y}^{2}$. Now take $b=\hat{a}$ in Lemma 6.5 and use Lemma 6.4. remembering that $d \hat{a}=d a$. \(\square\)

Definition 6.1 For any smooth $h: Y \rightarrow i \mathbb{R}$ define $\underline{h}, P(h): \mathbf{B} \rightarrow i \mathbb{R}$ by $\underline{h}(t, y)=h(y)$ and
$$P(h)=\Delta \underline{h}+i\langle i \Psi, \exp (\underline{h}) \Phi\rangle,$$
where $\Delta=d^{*} d$ is the Laplacian over $\mathbb{R} \times Y$. Let $P_{t}(h)$ be the restriction of $P(h)$ to $\{t\} \times Y$.

Note that
$$\mathcal{I}_{\underline{\alpha}}^{*}(\exp (\underline{h})(S)-\underline{\alpha})=-d^{*} a+P(h) .$$

Lemma 6.7 If $\alpha$ is irreducible then the following hold:
\begin{itemize}
\item[(i)] There is a $C_{3}>0$ such that if $\delta$ is sufficiently small then there exists a unique smooth $h: Y \rightarrow i \mathbb{R}$ satisfying $\|h\|_{3,2} \leq C_{3} \delta$ and $P_{0}(h)=0$.
\item[(ii)] If $h: Y \rightarrow i \mathbb{R}$ is any smooth function satisfying $P_{0}(h)=0$ then
$$\|P(h)\|_{L^{2}(\mathbf{B})} \leq \mathrm{const} \cdot\left(\nu+\left\|a^{\prime}\right\|_{L^{3}(\mathbf{B})}\right) .$$
\end{itemize}

Proof (i) We will apply Proposition B. 1 (ie the inverse function theorem) to the smooth map
$$P_{0}: L_{3}^{2} \rightarrow L_{1}^{2}, \quad h \mapsto \Delta_{Y} h+i\left\langle i \Psi_{0}, \exp (h) \Phi_{0}\right\rangle .$$
The first two derivatives of this map are
$$\begin{aligned}
D P_{0}(h) k & =\Delta_{Y} k+k\left\langle\Psi_{0}, \exp (h) \Phi_{0}\right\rangle, \\
D^{2} P_{0}(h)(k, \ell) & =i k \ell\left\langle i \Psi_{0}, \exp (h) \Phi_{0}\right\rangle .
\end{aligned}$$
The assumption $\delta \leq 1$ gives
$$\left\|D^{2} P_{0}(h)\right\| \leq \text { const } \cdot\left(1+\|\nabla h\|_{3}\right) .$$
Set $L=D P_{0}(0)$. Then
$$\left(L-\Delta_{Y}-\left|\Psi_{0}\right|^{2}\right) k=k\left\langle\Psi_{0}, \phi_{0}\right\rangle,$$
hence
$$\left\|L-\Delta_{Y}-\left|\Psi_{0}\right|^{2}\right\| \leq \text { const } \cdot \delta .$$
Thus if $\delta$ is sufficiently small then $L$ is invertible and
$$\left\|L^{-1}\right\| \leq\left\|\left(\Delta_{Y}+\left|\Psi_{0}\right|^{2}\right)^{-1}\right\|+1 .$$
Furthermore, we have $P_{0}(0)=i\left\langle i \Psi_{0}, \phi_{0}\right\rangle$, so
$$\left\|P_{0}(0)\right\|_{1,2} \leq \text { const } \cdot \delta .$$
By Proposition B. 1 (i) there exists a constant $C>0$ such that if $\delta$ is sufficiently small then there is a unique $h \in L_{3}^{2}$ such that $\|h\|_{3,2} \leq C$ and $P_{0}(h)=0$ (which implies that $h$ is smooth). Proposition B. 1 (ii) then yields
$$\|h\|_{3,2} \leq \text { const } \cdot\left\|P_{0}(0)\right\|_{1,2} \leq \text { const } \cdot \delta .$$
(ii) Setting $Q=P(h)$ we have, for $0 \leq t \leq T$,
$$\int_{Y}|Q(t, y)|^{2} d y=\int_{Y}\left|\int_{0}^{t} \partial_{1} Q(s, y) d s\right|^{2} d y \leq \text { const } \cdot \int_{\mathbf{B}}\left|\partial_{1} Q\right|^{2} .$$
Now, $\partial_{1} Q=i\left\langle i \Psi, \exp (\underline{h}) \partial_{1} \Phi\right\rangle$, hence
$$\left\|\partial_{1} Q\right\|_{2} \leq \text { const } \cdot\left\|\partial_{1} \Phi\right\|_{2} \leq \text { const } \cdot\left(\nu+\left\|a^{\prime}\right\|_{3}\right)$$
by Lemma 6.3 \(\square\)

Proposition 6.1 There is a constant $C_{4}$ such that if $\delta$ is sufficiently small then there exists a smooth $\widetilde{f}:$ B $\rightarrow i \mathbb{R}$ such that $\widetilde{s}=(\widetilde{a}, \widetilde{\phi})=\exp (\widetilde{f})(S)-\underline{\alpha}$ satisfies
$$\mathcal{I}_{\underline{\alpha}}^{*} \widetilde{s}=0,\left.\quad(* \widetilde{a})\right|_{\partial \mathbf{B}}=0, \quad\|\widetilde{s}\|_{L_{1}^{2}(\mathbf{B})} \leq C_{4} \nu, \quad\|\widetilde{s}\|_{L_{2}^{2}(\mathbf{B})} \leq C_{4} \delta,$$
where $\delta, \nu$ are as in (31).

This is analogous to Uhlenbeck's theorem [32, Theorem 1.3] (with $\mathrm{p}=2$ ), except that we assume a bound on $\delta$ rather than on $\nu$.

Proof To simplify notation we will write $\mathcal{I}=\mathcal{I}_{\underline{\alpha}}$ in this proof.
Case 1: $\alpha$ reducible In that case the operator $\mathcal{I}^{*}$ is given by $\mathcal{I}^{*}(b, \psi)=$ $-d^{*} b$. Let $\widetilde{f}$ be the $\hat{f}$ provided by Lemma 6.6. Then apply Lemma 6.4 (ii), taking the $S$ of that lemma to be the present $\exp (\widetilde{f})(S)$.
Case 2: $\alpha$ irreducible Let $\hat{f}, \hat{S}$ etc be as in Lemma 6.6. Choose $h: Y \rightarrow i \mathbb{R}$ such that the conclusions of Lemma 6.7 (i) holds with the $S$ of that lemma taken to be the present $\hat{S}$. Set $\underline{S}=(\hat{A}, \underline{\Phi})=\exp (\underline{h})(\hat{S})$ and $\dot{s}=(\dot{a}, \dot{\phi})=\dot{S}-\underline{\alpha}$. By Lemmas 6.7 and 6.4 (ii) we have
$$\left\|\mathcal{I}^{*} \hat{s}\right\|_{2} \leq \text { const } \cdot \nu, \quad\left\|\hat{s}^{\prime}\right\|_{2,2} \leq \text { const } \cdot \delta, \quad\|\hat{\phi}\|_{1,2} \leq \text { const } \cdot \nu .$$
Since $-d^{*} a=\mathcal{I}^{*} \dot{s}-i\langle i \Psi, \dot{\phi}\rangle$ we also get
$$\left\|d^{*} \hat{a}\right\|_{2} \leq \text { const } \cdot \nu \text {. }$$
Applying Lemma 6.5 as in the proof of Lemma 6.6 we see that
$$\|a ́\|_{1,2} \leq \text { const } \cdot \nu \text {. }$$
It now only remains to make a small perturbation to $\dot{S}$ so as to fulfil the Coulomb gauge condition. To this end we invoke the local slice theorem for B. This says that there is a $C>0$ such that if $\delta$ is sufficiently small then there exists a unique smooth $f: \mathbf{B} \rightarrow i \mathbb{R}$ such that setting $\widetilde{s}=(\widetilde{a}, \widetilde{\phi})=\exp (f)\left({ }^{\dot{S}}\right)-\underline{\alpha}$ one has
$$\|f\|_{3,2} \leq C \delta, \quad \mathcal{I}^{*} \widetilde{s}=0,\left.\quad * \widetilde{a}\right|_{\partial \mathbf{B}}=0 .$$
We will now estimate first $\|f\|_{2,2}$, then $\|\widetilde{s}\|_{1,2}$ in terms of $\nu$. First note that $\left.* a ́\right|_{\partial \mathbf{B}}=\left.* \hat{a}\right|_{\partial \mathbf{B}}=0$, and
$$\widetilde{a}=\dot{a}-d f, \quad \widetilde{\phi}=\exp (f) \dot{\Phi}-\Psi$$
by definition. Write the imaginary part of $\exp (f)$ as $f+f^{3} u$. Then $f$ satisfies the equations $\left.\left(\partial_{t} f\right)\right|_{\partial \mathbf{B}}=0$ and
$$\begin{aligned}
0 & =-d^{*} \widetilde{a}+i\langle i \Psi, \widetilde{\phi}\rangle_{\mathbb{R}} \\
& =\Delta f-d^{*} \dot{a}+i\langle i \Psi, \exp (f)(\dot{\phi}+\Psi)\rangle_{\mathbb{R}} \\
& =\Delta f+|\Psi|^{2} f-d^{*} \dot{a}+i\left\langle i \Psi, \exp (f) \dot{\phi}+f^{3} u \Psi\right\rangle_{\mathbb{R}} .
\end{aligned}$$
By the Sobolev embedding theorem we have
$$\|f\|_{\infty} \leq \text { const } \cdot\|f\|_{3,2} \leq \text { const } \cdot \delta,$$
and we assume $\delta \leq 1$, so $\|u\|_{\infty} \leq$ const. Therefore,
$$\begin{aligned}
\|f\|_{2,2} & \leq \text { const } \cdot\left\|\Delta f+|\Psi|^{2} f\right\|_{2} \\
& \leq \nu+\text { const } \cdot\left\|f^{3}\right\|_{2} \\
& \leq \nu+\text { const } \cdot\|f\|_{2,2}^{3},
\end{aligned}$$
cf Subsection 2.5 for the first inequality. If $\delta$ is sufficiently small then we can rearrange to get $\|f\|_{2,2} \leq$ const $\cdot \nu$. Consequently, $\|\widetilde{a}\|_{1,2} \leq$ const $\cdot \nu$. To estimate $\|\widetilde{\phi}\|_{1,2}$ we write
$$\widetilde{\phi}=g \Psi+\exp (f) \dot{\phi},$$
where $g=\exp (f)-1$. Then $|d g|=|d f|$ and $|g| \leq$ const $\cdot|f|$. Now
$$\begin{aligned}
\|\widetilde{\phi}\|_{2} & \leq \text { const } \cdot\|f\|_{2}+\|\dot{\phi}\|_{2} \leq \text { const } \cdot \nu, \\
\|\nabla \widetilde{\phi}\|_{2} & \leq \text { const } \cdot\left(\|g\|_{1,2}+\|d f \otimes \dot{\phi}\|_{2}+\|\nabla \hat{\phi}\|_{2}\right) \\
& \leq \text { const } \cdot\left(\nu+\|d f\|_{4}\|\dot{\phi}\|_{4}\right) \\
& \leq \text { const } \cdot\left(\nu+\|f\|_{2,2}\|\dot{\phi}\|_{1,2}\right) \\
& \leq \operatorname{const} \cdot\left(\nu+\nu^{2}\right) \\
& \leq \operatorname{const} \cdot \nu
\end{aligned}$$
by (32). Therefore, $\|\widetilde{\phi}\|_{1,2} \leq$ const $\cdot \nu$. Thus, the proposition holds with
$$\widetilde{f}=\hat{f}+\underline{h}+f .$$ \(\square\)

Proposition 6.2 Let $k$ be a positive integer and $V \Subset \operatorname{int}(\mathbf{B})$ an open subset. Then there are constants $\epsilon_{k}, C_{k, V}$, where $\epsilon_{k}$ is independent of $V$, such that if
$$\mathcal{I}_{\underline{\alpha}}^{*} s=0, \quad\|s\|_{L_{1}^{2}(\mathbf{B})} \leq \epsilon_{k}$$
then
$$\|s\|_{L_{k}^{2}(V)} \leq C_{k, V}\|s\|_{L_{1}^{2}(\mathbf{B})} .$$

Proof The argument in [11, pages 62-63] carries over, if one replaces the operator $d^{*}+d^{+}$with $\mathcal{I}_{\underline{\alpha}}^{*}+D \Theta_{\underline{\alpha}}$, where $D \Theta_{\underline{\alpha}}$ is the linearization of the monopole map at $\underline{\alpha}$. Note that $\mathcal{I}_{\underline{\alpha}}^{*}+D \Theta_{\underline{\alpha}}$ is injective over $S^{1} \times Y$ because $\alpha$ is non-degenerate, so if $\gamma: \mathbf{B} \rightarrow \mathbb{R}$ is a smooth function supported in $\operatorname{int}(\mathbf{B})$ then
$$\|\gamma s\|_{k, 2} \leq C_{k}^{\prime}\left\|\left(\mathcal{I}_{\underline{\alpha}}^{*}+D \Theta_{\underline{\alpha}}\right)(\gamma s)\right\|_{k-1,2}$$
for some constant $C_{k}^{\prime}$. \(\square\)

\subsection*{6.3 Decay of monopoles}

The two theorems in this subsection are analogues of Propositions 4.3 and 4.4 in [10], respectively.

Let $\beta$ be a non-degenerate monopole over $Y$, and $U \subset \mathcal{B}_{Y}$ an $L^{2}$-closed subset which contains no monopoles except perhaps $[\beta]$. Choose $\lambda^{ \pm}>0$ such that $\widetilde{H}_{\beta}$ has no eigenvalue in the interval $\left[-\lambda^{-}, \lambda^{+}\right]$, and set $\lambda=\min \left(\lambda^{-}, \lambda^{+}\right)$. Define
$$\mathbf{B}_{t}=[t-1, t+1] \times Y .$$

Theorem 6.1 For any $C>0$ there are constants $\epsilon, C_{0}, C_{1}, \ldots$ such that the following holds. Let $S=(A, \Phi)$ be any monopole in temporal gauge over $(-2, \infty) \times Y$ such that $\left[S_{t}\right] \in U$ for some $t \geq 0$. Set
$$\bar{\nu}=\left\|\nabla \vartheta_{S}\right\|_{L^{2}((-2, \infty) \times Y)}, \quad \nu(t)=\left\|\nabla \vartheta_{S}\right\|_{L^{2}\left(\mathbf{B}_{t}\right)} .$$
If $\|\Phi\|_{\infty} \leq C$ and $\bar{\nu} \leq \epsilon$ then there is a smooth monopole $\alpha$ over $Y$, gauge equivalent to $\beta$, such that if $B$ is the connection part of $\underline{\alpha}$ then for every $t \geq 1$ and non-negative integer $k$ one has
$$\sup _{y \in Y}\left|\nabla_{B}^{k}(S-\underline{\alpha})\right|_{(t, y)} \leq C_{k} \sqrt{\nu(0)} e^{-\lambda^{+} t} .$$

Proof It follows from the local slice theorem that $\widetilde{\mathcal{B}}_{Y} \rightarrow \mathcal{B}_{Y}$ is a (topological) principal $H^{1}(Y ; \mathbb{Z})$-bundle. Choose a small open neighbourhood $V$ of $[\beta] \in \mathcal{B}_{Y}$ which is the image of a convex set in $\mathcal{C}_{Y}$. We define a continuous function $\bar{f}: V \rightarrow \mathbb{R}$ by
$$\bar{f}(x)=\vartheta(\sigma(x))-\vartheta(\sigma([\beta]))$$
where $\sigma: V \rightarrow \widetilde{\mathcal{B}}_{Y}$ is any continuous cross-section. It is clear that $\bar{f}$ is independent of $\sigma$.

Given $C>0$, let $S=(A, \Phi)$ be any monopole over $(-2, \infty) \times Y$ such that $\|\Phi\|_{\infty} \leq C$ and $\left[S_{t}\right] \in U$ for some $t \geq 0$. If $\delta>0$, and $k$ is any non-negative integer, then provided $\bar{\nu}$ is sufficiently small, our local compactness results (Lemmas 4.2 and 4.1) imply that for every $t \geq 0$ we can find a smooth $u: \mathbf{B}_{0} \rightarrow \mathrm{U}(1)$ such that
$$\left\|u\left(\left.S\right|_{\mathbf{B}_{t}}\right)-\underline{\beta}\right\|_{C^{k}\left(\mathbf{B}_{0}\right)}<\delta .$$
In particular, if $\bar{\nu}$ is sufficiently small then
$$f: \overline{\mathbb{R}}_{+} \rightarrow \mathbb{R}, \quad t \mapsto \bar{f}\left(\left[S_{t}\right]\right)$$
is a well-defined smooth function. Since $f(t)-\vartheta\left(S_{t}\right)$ is locally constant, and $f(t) \rightarrow 0$ as $t \rightarrow \infty$, we have
$$f(t)=\vartheta\left(S_{t}\right)-L,$$
where $L=\lim _{t \rightarrow \infty} \vartheta\left(S_{t}\right)$. If $\bar{\nu}$ is sufficiently small then Lemma 6.2 gives $2 \lambda^{+} f \leq-f^{\prime}$, hence
$$0 \leq f(t) \leq e^{-2 \lambda^{+} t} f(0), \quad t \geq 0 .$$
This yields
$$\nu(t)^{2}=f(t-1)-f(t+1) \leq \text { const } \cdot e^{-2 \lambda^{+} t} f(0), \quad t \geq 1 .$$
If $\bar{\nu}$ is sufficiently small then by Propositions 6.1 and 6.2 we have
$$f(t) \leq \text { const } \cdot \nu(t), \quad \sup _{y \in Y}\left|\nabla_{A}^{k}\left(\nabla \vartheta_{S}\right)\right|_{(t, y)} \leq C_{k}^{\prime} \nu(t)$$
for every $t \geq 0$ and non-negative integer $k$, where $C_{k}^{\prime}$ is some constant. Here we are using the simple fact that if $E, E^{\prime}$ are Banach spaces, $W \subset E$ an open neighbourhood of 0 , and $h: W \rightarrow E^{\prime}$ a differentiable map with $h(0)=0$ then $\|h(x)\| \leq(\|D h(0)\|+1)\|x\|$ in some neighbourhood of 0. For instance, to deduce the second inequality in (36) we can apply this to the map
$$h: L_{k+j+1}^{2} \rightarrow L_{j}^{2}, \quad s=(a, \phi) \mapsto \nabla_{B^{\prime}+a}^{k}\left(\nabla \vartheta_{\underline{\beta}+s}\right)$$
where $j \geq 3$, say, and $B^{\prime}$ is the connection part of $\underline{\beta}$.
Putting the inequalities above together we get
$$\sup _{y \in Y}\left|\nabla_{A}^{k}\left(\nabla \vartheta_{S}\right)\right|_{(t, y)} \leq C_{k}^{\prime \prime} \sqrt{\nu(0)} e^{-\lambda^{+} t}, \quad t \geq 1$$
for some constants $C_{k}^{\prime \prime}$. If $S$ is in temporal gauge we deduce, by taking $k=0$, that $S_{t}$ converges uniformly to some continuous configuration $\alpha$. One can now prove by induction on $k$ that $\alpha$ is of class $C^{k}$ and that (35) holds. \(\square\)

Theorem 6.2 For any $C>0$ there are constants $\epsilon, C_{0}, C_{1} \ldots$ such that the following holds for every $T>1$. Let $S=(A, \Phi)$ be any smooth monopole in temporal gauge over the band $[-T-2, T+2] \times Y$, and suppose $\left[S_{t}\right] \in U$ for some $t \in[-T, T]$. Set
$$\bar{\nu}=\left\|\nabla \vartheta_{S}\right\|_{L^{2}((-T-2, T+2) \times Y)}, \quad \nu(t)=\left\|\nabla \vartheta_{S}\right\|_{L^{2}\left(\mathbf{B}_{t}\right)} .$$
If $\|\Phi\|_{\infty} \leq C$ and $\bar{\nu} \leq \epsilon$ then there is a smooth monopole $\alpha$ over $Y$, gauge equivalent to $\beta$, such that if $B$ is the connection part of $\underline{\alpha}$ then for $|t| \leq T-1$ and every non-negative integer $k$ one has
$$\sup _{y \in Y}\left|\nabla_{B}^{k}(S-\underline{\alpha})\right|_{(t, y)} \leq C_{k}(\nu(-T)+\nu(T))^{1 / 2} e^{-\lambda(T-|t|)} .$$

Proof Given $C>0$, let $S=(A, \Phi)$ be any monopole over $[-T-2, T+2] \times Y$ such that $\|\Phi\|_{\infty} \leq C$ and $\left[S_{t}\right] \in U$ for some $t \in[-T, T]$. If $\bar{\nu}$ is sufficiently small then we can define the function $f(t)$ for $|t| \leq T$ as in the proof of Theorem 6.1, and (36) will hold with $f(t)$ replaced by $|f(t)|$, for $|t| \leq T$. Again, $f(t)=\vartheta\left(S_{t}\right)-L$ for some constant $L$. Lemma 6.2 now gives
$$e^{-2 \lambda_{-}(T-t)} f(T) \leq f(t) \leq e^{-2 \lambda_{+}(T+t)} f(-T), \quad|t| \leq T,$$
which implies
$$\begin{aligned}
|f(t)| \leq(|f(-T)|+|f(T)|) e^{-2 \lambda(T-|t|)}, & |t| \leq T, \\
\nu(t)^{2} \leq \text { const } \cdot(\nu(-T)+\nu(T)) e^{-2 \lambda(T-|t|)}, & |t| \leq T-1 .
\end{aligned}$$
By Propositions 6.1 and 6.2 there is a critical point $\alpha$ gauge equivalent to $\beta$ such that
$$\left\|\nabla_{B}^{k}\left(S_{0}-\alpha\right)\right\|_{L^{\infty}(Y)} \leq C_{k}^{\prime \prime \prime} \nu(0)$$
for some constants $C_{k}^{\prime \prime \prime}$. It is now easy to complete the proof by induction on $k$. \(\square\)

\subsection*{6.4 Global convergence}

The main result of this subsection is Proposition 6.3, which relates local and global convergence of monopoles over a half-cylinder. First some lemmas.

Lemma 6.8 Let $Z$ be a compact Riemannian $n$-manifold (perhaps with boundary), $m$ a non-negative integer, and $q \geq n / 2$. Then there is a real polynomial $P_{m, q}(x)$ of degree $m+1$ satisfying $P_{m, q}(0)=0$, such that for any smooth $u: Z \rightarrow U(1)$ one has
$$\|d u\|_{m, q} \leq P_{m, q}\left(\left\|u^{-1} d u\right\|_{m, q}\right) .$$

Proof Argue by induction on $m$ and use the Sobolev embedding $L_{k}^{r}(Z) \subset$ $L_{k-1}^{2 r}(Z)$ for $k \geq 1, r \geq n / 2$. \(\square\)

Lemma 6.9 Let $Z$ be a compact, connected Riemannian $n$-manifold (perhaps with boundary), $z \in Z, m$ a positive integer, and $q \geq 1$. Then there is a $C>0$ such that for any smooth $f: Z \rightarrow \mathbb{C}$ one has
\begin{itemize}
\item[(i)] $\left\|f-f_{a v}\right\|_{m, q} \leq C\|d f\|_{m-1, q}$,
\item[(ii)] $\|f\|_{m, q} \leq C\left(\|d f\|_{m-1, q}+|f(z)|\right)$,
\end{itemize}
where $f_{a v}=\operatorname{Vol}(Z)^{-1} \int_{Z} f$ is the average of $f$.

Proof Exercise. \(\square\)

Lemma 6.10 Let $Z$ be a compact Riemannian $n$-manifold (perhaps with boundary), $m$ a positive integer, and $q$ a real number such that $m q>n$. Let $\Phi$ be a smooth section of some Hermitian vector bundle $E \rightarrow Z, \Phi \not \equiv 0$. Then there exists a $C>0$ with the following significance. Let $\phi_{1}$ be a smooth section of $E$ satisfying $\left\|\phi_{1}\right\|_{q} \leq C^{-1}$ and $w: Z \rightarrow \mathbb{C}$ a smooth map. Define another section $\phi_{2}$ by
$$w\left(\Phi+\phi_{1}\right)=\Phi+\phi_{2} .$$
Then
$$\|w-1\|_{m, q} \leq C\left(\|d w\|_{m-1, q}+\left\|\phi_{2}-\phi_{1}\right\|_{q}\right) .$$

Proof The equation
$$(w-1) \Phi=\phi_{2}-\phi_{1}-(w-1) \phi_{1}$$
gives
$$\begin{aligned}
\|w-1\|_{m, q} & \leq \text { const } \cdot\left(\|d w\|_{m-1, q}+\|(w-1) \Phi\|_{q}\right) \\
& \leq \text { const } \cdot\left(\|d w\|_{m-1, q}+\left\|\phi_{2}-\phi_{1}\right\|_{q}+\|w-1\|_{m, q}\left\|\phi_{1}\right\|_{q}\right) .
\end{aligned}$$
Here the first inequality is analogous to Lemma 6.9 (ii). If $\left\|\phi_{1}\right\|_{q}$ is sufficiently small then we can rearrange to get the desired estimate on $\|w-1\|_{m, q}$. \(\square\)

Now let $\alpha$ be a non-degenerate critical point of $\vartheta$. Note that if $S=(A, \Phi)$ is any finite energy monopole in temporal gauge over $\mathbb{R}_{+} \times Y$ such that $\|\Phi\|_{\infty}<\infty$ and
$$\liminf _{t \rightarrow \infty} \int_{[t, t+1] \times Y}|S-\underline{\alpha}|^{r}=0$$
for some $r>1$ then by the results of Section 4 we have $\left[S_{t}\right] \rightarrow[\alpha]$ in $\mathcal{B}_{Y}$, hence $S-\underline{\alpha}$ decays exponentially by Theorem 6.1. In this situation we will simply say that $S$ is asymptotic to $\alpha$.
(Here we used the fact that for any $p>2$ and $1<r \leq 2 p$, say, the $L^{r}$ metric on the $L_{1}^{p}$ configuration space $\mathcal{B}([0,1] \times Y)$ is well-defined.)

Lemma 6.11 If $S=(A, \Phi)$ is any smooth monopole over $\mathbb{R}_{+} \times Y$ such that $\|\Phi\|_{\infty}<\infty$ and $S-\underline{\alpha} \in L_{1}^{p}$ for some $p>2$ then there exists a null-homotopic smooth $u: \mathbb{R}_{+} \times Y \rightarrow U(1)$ such that $u(S)$ is in temporal gauge and asymptotic to $\alpha$.

Proof By Theorem 6.1 there exists a smooth $u: \mathbb{R}_{+} \times Y \rightarrow \mathrm{U}(1)$ such that $u(S)$ is in temporal gauge and asymptotic to $\alpha$. Lemma 6.8, Lemma 6.9 (i), and the assumption $S-\underline{\alpha} \in L_{1}^{p}$ then gives
$$\left\|u-u_{\mathrm{av}}\right\|_{L^{\infty}([t, t+1] \times Y)} \rightarrow 0 \text { as } t \rightarrow \infty,$$
hence $u$ is null-homotopic. \(\square\)

It follows that all elements of the moduli spaces defined in Subsection 3.4 have smooth representatives that are in temporal gauge over the ends.

Proposition 6.3 Let $\delta>0$ and suppose $\vartheta: \widetilde{\mathcal{B}}_{Y} \rightarrow \mathbb{R}$ has no critical value in the half-open interval $(\vartheta(\alpha), \vartheta(\alpha)+\delta]$ (this implies Condition $(O 1)$ ). For $n=1,2, \ldots$ let $S_{n}=\left(A_{n}, \Phi_{n}\right)$ be a smooth monopole over $\overline{\mathbb{R}}_{+} \times Y$ such that
$$S_{n}-\underline{\alpha} \in L_{1}^{p}, \quad \sup _{n}\left\|\Phi_{n}\right\|_{\infty}<\infty, \quad \vartheta\left(S_{n}(0)\right) \leq \vartheta(\alpha)+\delta,$$
for some $p>2$. Let $v_{n}: \overline{\mathbb{R}}_{+} \times Y \rightarrow U(1)$ be a smooth map such that the sequence $v_{n}\left(S_{n}\right)$ converges in $C^{\infty}$ over compact subsets of $\overline{\mathbb{R}}_{+} \times Y$ to a configuration $S$ in temporal gauge. Then the following hold:
\begin{itemize}
\item[(i)] $S$ is asymptotic to a critical point $\alpha^{\prime}$ gauge equivalent to $\alpha$,
\item[(ii)] If $\alpha=\alpha^{\prime}$ then $v_{n}$ is null-homotopic for all sufficiently large $n$, and there exist smooth $u_{n}: \overline{\mathbb{R}}_{+} \times Y \rightarrow U(1)$ with the following significance: For every $t \geq 0$ one has $u_{n}=1$ on $[0, t] \times Y$ for all sufficiently large $n$. Moreover, for any $\sigma<\lambda^{+}, q \geq 1$ and non-negative integer $m$ one has
$$\left\|u_{n} v_{n}\left(S_{n}\right)-S\right\|_{L_{m}^{q, \sigma}} \rightarrow 0 \text { as } n \rightarrow \infty .$$
\end{itemize}
Here $\lambda^{+}$is as in Subsection 6.1

Proof It clearly suffices to prove the proposition when $q \geq 2$ and $m q>4$, which we assume from now on.

By Lemma 4.5 we have
$$\int_{\mathbb{R}_{+} \times Y}\left|\nabla \vartheta_{S_{n}}\right|^{2}=\vartheta\left(S_{n}(0)\right)-\vartheta(\alpha) \leq \delta$$
for each $n$, hence $\int_{\mathbb{R}_{+} \times Y}\left|\nabla \vartheta_{S}\right|^{2} \leq \delta$. Part (i) of the proposition is now a consequence of Theorem 6.1 and the following

Claim $6.1[S(t)]$ converges in $\mathcal{B}_{Y}$ to $[\alpha]$ as $t \rightarrow \infty$.

Proof of claim For $r>0$ let $B_{r} \subset \mathcal{B}_{Y}$ denote the open $r$-ball around $[\alpha]$ in the $L^{2}$ metric, and let $\bar{B}_{r}$ be the corresponding closed ball. Choose $r>0$ such that $\bar{B}_{2 r}$ contains no monopole other than $[\alpha]$. Assuming the claim does not hold then by Lemma 4.1 one can find a sequence $t_{j}^{\prime}$ such that $t_{j}^{\prime} \rightarrow \infty$ as $j \rightarrow \infty$ and $\left[S\left(t_{j}^{\prime}\right)\right] \notin \bar{B}_{2 r}$ for each $j$. Because of the convergence of $v_{n}\left(S_{n}\right)$ it follows by a continuity argument that there are sequences $n_{j}, t_{j}$ with $t_{j}, n_{j} \rightarrow \infty$ as $j \rightarrow \infty$, such that
$$\left[S_{n_{j}}\left(t_{j}\right)\right] \in \bar{B}_{2 r} \backslash B_{r}$$
for all $j$. For $s \in \mathbb{R}$ let $\mathcal{T}_{s}: \mathbb{R} \times Y \rightarrow \mathbb{R} \times Y$ be translation by $s$ :
$$\mathcal{T}_{s}(t, y)=(t+s, y) .$$
Again by Lemma 4.1 there are smooth $\omega_{j}: \overline{\mathbb{R}}_{+} \times Y \rightarrow \mathrm{U}(1)$ such that a subsequence of $\left(\mathcal{T}_{t_{j}}\right)^{*}\left(\omega_{j}\left(S_{n_{j}}\right)\right)$ converges in $C^{\infty}$ over compact subsets of $\mathbb{R} \times Y$ to some finite energy monopole $S^{\prime}$ whose spinor field is pointwise bounded. Moreover, it is clear that $\vartheta \circ \omega_{j}(0)-\vartheta \in \mathbb{R}$ must be bounded as $j \rightarrow \infty$, so by passing to a subsequence and replacing $\omega_{j}$ by $\omega_{j} \omega_{j_{0}}^{-1}$ for some fixed $j_{0}$ we may arrange that $\vartheta \circ \omega_{j}(0)=\vartheta$ for all $n$. Then $\ell=\lim _{t \rightarrow-\infty} \vartheta\left(S^{\prime}(t)\right)$ must be a critical value of $\vartheta$. Since
$$\left[S^{\prime}(0)\right] \in \bar{B}_{2 r} \backslash B_{r},$$
$S^{\prime}(0)$ is not a critical point, whence $\left.\partial_{t}\right|_{0} \vartheta\left(S^{\prime}(t)\right)<0$. Therefore,
$$\vartheta(\alpha)+\delta \geq \ell>\vartheta\left(S^{\prime}(0)\right)>\vartheta(\alpha),$$
contradicting our assumptions. This proves the claim. \(\square\)

We will now prove Part (ii). For $\tau \geq 0$ let
$$B_{\tau}^{-}=[0, \tau] \times Y, \quad B_{\tau}^{+}=[\tau, \infty) \times Y, \quad \mathcal{O}_{\tau}=[\tau, \tau+1] \times Y .$$
By Lemma 6.11 there is, for every $n$, a null-homotopic, smooth $\widetilde{v}_{n}: \overline{\mathbb{R}}_{+} \times Y \rightarrow$ U(1) such that $S_{n}^{\prime \prime}=\widetilde{v}_{n}\left(S_{n}\right)$ is in temporal gauge and asymptotic to $\alpha$.
Note that
$$\lim _{t \rightarrow \infty} \limsup _{n \rightarrow \infty} \vartheta\left(S_{n}(t)\right)=\vartheta(\alpha) .$$
For otherwise we could find an $\epsilon>0$ and for every natural number $j$ a pair $t_{j}, n_{j} \geq j$ such that
$$\vartheta\left(S_{n_{j}}\left(t_{j}\right)\right) \geq \vartheta(\alpha)+\epsilon,$$
and we could then argue as in the proof of Claim 6.1 to produce a critical value of $\vartheta$ in the interval $(\alpha, \alpha+\delta]$. Since $\left|\nabla \vartheta_{S_{n}}\right|=\left|\nabla \vartheta_{S_{n}^{\prime \prime}}\right|$ it follows from (37) and Theorem 6.1 that there exists a $t_{1} \geq 0$ such that if $\tau \geq t_{1}$ then
$$\limsup _{n \rightarrow \infty}\left\|S_{n}^{\prime \prime}-\underline{\alpha}\right\|_{L_{m}^{q, \sigma}\left(B_{\tau}^{+}\right)} \leq \operatorname{const} \cdot e^{\left(\sigma-\lambda^{+}\right) \tau}$$
where the constant is independent of $\tau$. Then we also have
$$\limsup _{n \rightarrow \infty}\left\|S_{n}^{\prime \prime}-S\right\|_{L_{m}^{q, \sigma}\left(B_{\tau}^{+}\right)} \leq \text {const } \cdot e^{\left(\sigma-\lambda^{+}\right) \tau} .$$
Set $S_{n}^{\prime}=v_{n}\left(S_{n}\right)$ and $w_{n}=\widetilde{v}_{n} v_{n}^{-1}$. Then we get
$$\limsup _{n \rightarrow \infty}\left\|S_{n}^{\prime \prime}-S_{n}^{\prime}\right\|_{L_{m}^{q}\left(\mathcal{O}_{\tau}\right)} \leq \mathrm{const} \cdot e^{-\lambda^{+} \tau},$$
which gives
$$\limsup _{n \rightarrow \infty}\left\|d w_{n}\right\|_{L_{m}^{q}\left(\mathcal{O}_{\tau}\right)} \leq \mathrm{const} \cdot e^{-\lambda^{+} \tau}$$
by Lemma 6.8 In particular, $w_{n}$ is null-homotopic for all sufficiently large $n$.
Fix $y_{0} \in Y$ and set $x_{\tau}=\left(\tau, y_{0}\right)$. Choose a sequence $\tau_{n}$ such that $\tau_{n} \rightarrow \infty$ as $n \rightarrow \infty$ and
$$\begin{aligned}
& \left\|S_{n}^{\prime}-S\right\|_{L_{m}^{q, \sigma}\left(B_{\tau_{n}+1}^{-}\right)}^{-} \rightarrow 0, \\
& \left\|S_{n}^{\prime \prime}-S\right\|_{L_{m}^{q, \sigma}\left(B_{\tau_{n}}^{+}\right)} \rightarrow 0
\end{aligned}$$
as $n \rightarrow \infty$. If $\alpha$ is reducible then by multiplying each $\widetilde{v}_{n}$ by a constant and redefining $w_{n}, S_{n}^{\prime \prime}$ accordingly we may arrange that $w_{n}\left(x_{\tau_{n}}\right)=1$ for all $n$. (If $\alpha$ is irreducible we keep $\widetilde{v}_{n}$ as before.) Then (38) still holds. Applying Lemma 6.8 together with Lemma 6.9 (ii) (if $\alpha$ is reducible) or Lemma 6.10 (if $\alpha$ is irreducible) we see that
$$e^{\sigma \tau_{n}}\left\|w_{n}-1\right\|_{L_{m+1}^{q}\left(\mathcal{O}_{\tau_{n}}\right)} \rightarrow 0$$
as $n \rightarrow \infty$.
Let $\beta: \mathbb{R} \rightarrow \mathbb{R}$ be a smooth function such that $\beta(t)=0$ for $t \leq \frac{1}{3}$ and $\beta(t)=1$ for $t \geq \frac{2}{3}$. Set $\beta_{\tau}(t)=\beta(t-\tau)$. Given any function $w: \mathcal{O}_{\tau} \rightarrow \mathbb{C} \backslash(-\infty, 0]$ define
$$\mathcal{U}_{w, \tau}=\exp \left(\beta_{\tau} \log w\right)$$
where $\log (\exp (z))=z$ for complex numbers $z$ with $|\operatorname{Im}(z)|<\pi$. Let $m^{\prime}$ be any integer such that $m^{\prime} q>4$. If $\|w-1\|_{m^{\prime}, q}$ is sufficiently small then
$$\begin{aligned}
& \left\|\mathcal{U}_{w, \tau}-1\right\|_{m^{\prime}, q} \leq \text { const } \cdot\|w-1\|_{m^{\prime}, q}, \\
& \left\|w^{-1} d w\right\|_{m^{\prime}-1, q} \leq \text { const } \cdot\|w-1\|_{m^{\prime}, q} .
\end{aligned}$$
To see this recall that for functions on $\mathbb{R}^{4}$, multiplication defines a continuous map $L_{m^{\prime}}^{q} \times L_{k}^{q} \rightarrow L_{k}^{q}$ for $0 \leq k \leq m^{\prime}$. Therefore, if $V$ is the set of all functions in $L_{m^{\prime}}^{q}\left(\mathcal{O}_{\tau}, \mathbb{C}\right)$ that map into some fixed small open ball about $1 \in \mathbb{C}$ then $w \mapsto \mathcal{U}_{w, \tau}$ defines a $C^{\infty}$ map $V \rightarrow L_{m^{\prime}}^{q}$. This yields the first inequality in (39), and the proof of the second inequality is similar.

Combining (38) and (39) we conclude that Part (ii) of the proposition holds with
$$u_{n}= \begin{cases}1 & \text { in } B_{\tau_{n}}^{-}, \\ \mathcal{U}_{w_{n}, \tau_{n}} & \text { in } \mathcal{O}_{\tau_{n}}, \\ w_{n} & \text { in } B_{\tau_{n}+1}^{+} .\end{cases}$$
This completes the proof of Proposition 6.3. \(\square\)

\section*{7 Global compactness}

In this section we will prove Theorems 1.3 and 1.4. Given the results of Sections 4 and 5, what remains to be understood is convergence over ends and necks. We will use the following terminology:
$$\text { c-convergence }=C^{\infty} \text { convergence over compact subsets. }$$

\subsection*{7.1 Chain-convergence}

We first define the notion of chain-convergence. For simplicity we only consider two model cases: first the case of one end and no necks, then the case of one neck and no ends. It should be clear how to extend the notion to the case of multiple ends and/or necks.

Definition 7.1 Let $X$ be a spin ${ }^{c}$ Riemannian 4-manifold with one tubular end $\mathbb{R}_{+} \times Y$, where $Y$ is connected. Let $\alpha_{1}, \alpha_{2}, \ldots$ and $\beta_{0}, \ldots, \beta_{k}$ be elements of $\widetilde{\mathcal{R}}_{Y}$, where $k \geq 0$ and $\vartheta\left(\beta_{j-1}\right)>\vartheta\left(\beta_{j}\right)$ for $j=1, \ldots, k$. Let $\omega \in M\left(X ; \beta_{0}\right)$ and $\vec{v}=\left(v_{1}, \ldots, v_{k}\right)$, where $v_{j} \in \check{M}\left(\beta_{j-1}, \beta_{j}\right)$. We say a sequence $\left[S_{n}\right] \in M\left(X ; \alpha_{n}\right)$ chain-converges to $(\omega, \vec{v})$ if there exist, for each $n$,
\begin{itemize}
\item[-] a smooth map $u_{n}: X \rightarrow \mathrm{U}(1)$,
\item[-] for $j=1, \ldots, k$ a smooth map $u_{n, j}: \mathbb{R} \times Y \rightarrow \mathrm{U}(1)$,
\item[-] a sequence $0=t_{n, 0}<t_{n, 1}<\cdots<t_{n, k}$,
\end{itemize}
such that
\begin{itemize}
\item[(i)] $u_{n}\left(S_{n}\right)$ c-converges over $X$ to a representative of $\omega$ (in the sense of Subsection 2.4),
\item[(ii)] $t_{n, j}-t_{n, j-1} \rightarrow \infty$ as $n \rightarrow \infty$,
\item[(iii)] $u_{n, j}\left(\mathcal{T}_{t_{n, j}}^{*} S_{n}\right)$ c-converges over $\mathbb{R} \times Y$ to a representative of $v_{j}$,
\end{itemize}
\begin{itemize}
\item[(iv)] $\limsup _{n \rightarrow \infty}\left[\vartheta\left(S_{n}\left(t_{n, j-1}+\tau\right)\right)-\vartheta\left(S_{n}\left(t_{n, j}-\tau\right)\right)\right] \rightarrow 0$ as $\tau \rightarrow \infty$,
\item[(v)] $\limsup _{n \rightarrow \infty}\left[\vartheta\left(S_{n}\left(t_{n, k}+\tau\right)\right)-\vartheta\left(\alpha_{n}\right)\right] \rightarrow 0$ as $\tau \rightarrow \infty$,
\end{itemize}
where (ii), (iii) and (iv) should hold for $j=1, \ldots, k$.
Conditions (iv) and (v) mean, in familiar language, that "no energy is lost in the limit". As before, $\mathcal{T}_{s}$ denotes translation by $s$, ie $\mathcal{T}_{s}(t, y)=(t+s, y)$.

We now turn to the case of one neck and no ends.
Definition 7.2 In the situation of Subsection 1.4, suppose $r=1$ and $r^{\prime}=0$. Let $\beta_{0}, \ldots, \beta_{k} \in \widetilde{\mathcal{R}}_{Y}$, where $k \geq 0$ and $\vartheta\left(\beta_{j-1}\right)>\vartheta\left(\beta_{j}\right), j=1, \ldots, k$. Let $\omega \in$ $M\left(X ; \beta_{0}, \beta_{k}\right)$ and $\vec{v}=\left(v_{1}, \ldots, v_{k}\right)$, where $v_{j} \in \check{M}\left(\beta_{j-1}, \beta_{j}\right)$. Let $T(n) \rightarrow \infty$ as $n \rightarrow \infty$. We say a sequence $\left[S_{n}\right] \in M\left(X^{(T(n))}\right)$ chain-converges to $(\omega, \vec{v})$ if there exist, for every $n$,
\begin{itemize}
\item[-] a smooth map $u_{n}: X^{(T(n))} \rightarrow \mathrm{U}(1)$,
\item[-] for $j=1, \ldots, k$ a smooth map $u_{n, j}: \mathbb{R} \times Y \rightarrow \mathrm{U}(1)$,
\item[-] a sequence $-T(n)=t_{n, 0}<t_{n, 1}<\cdots<t_{n, k+1}=T(n)$,
\end{itemize}
such that (i)-(iv) of Definition 7.1 hold for the values of $j$ for which they are defined (in other words, (ii) and (iv) should hold for $1 \leq j \leq k+1$ and (iii) for $1 \leq j \leq k$ ).

In the notation of Subsection 1.2 if $J \subset \mathbb{R}$ is an interval with non-empty interior then a smooth configuration $S$ over $J \times Y$ is called regular (with respect to $\vartheta)$ if either $\partial_{t} \vartheta\left(S_{t}\right)<0$ for every $t \in J$, or $S$ is gauge equivalent to the translationary invariant configuration $\underline{\alpha}$ determined by some critical point $\alpha$ of $\vartheta$. Proposition 4.3 guarantees the regularity of certain $(\mathfrak{p}, \mathfrak{q})$-monopoles when $\mathfrak{p}$ is sufficiently small. In particular, genuine monopoles are always regular.

Consider now the situation of Subsection 1.4 (without assuming (B1) or (B2)), and let the 2 -form $\mu$ on $X$ be fixed.

Definition 7.3 A set of perturbation parameters $\overrightarrow{\mathfrak{p}}, \overrightarrow{\mathfrak{p}}^{\prime}$ is admissible for a vector $\vec{a}^{\prime}$ of critical points if for some $t_{0} \geq 1$ the following holds. Let $\mathcal{M}$ be the disjoint union of all moduli spaces $M\left(X^{(T)} ; \vec{\alpha}^{\prime} ; \overrightarrow{\mathfrak{p}} ; \overrightarrow{\mathfrak{p}}^{\prime}\right)$ with $\min _{j} T_{j} \geq t_{0}$. Then we require, for all $j, k$, that
\begin{itemize}
\item[(i)] If $\widetilde{S}$ is any configuration over $[-1,1] \times Y_{j}$ which is a $C^{\infty}$ limit of configurations of the form $\left.S\right|_{[t-1, t+1] \times Y_{j}}$ with $S \in \mathcal{M}$ and $|t| \leq T_{j}-1$, then $\widetilde{S}$ is regular.
\end{itemize}
\begin{itemize}
\item[(ii)] If $\widetilde{S}$ is any configuration over $[-1,1] \times Y_{k}^{\prime}$ which is a $C^{\infty}$ limit of configurations of the form $\left.S\right|_{[t-1, t+1] \times Y_{k}^{\prime}}$ with $S \in \mathcal{M}$ and $t \geq 1$, then $\widetilde{S}$ is regular.
\end{itemize}

In particular, the zero perturbation parameters are always admissible.
The next two propositions describe some properties of chain-convergence.

Proposition 7.1 In the notation of Theorem 1.3, suppose $\omega_{n}$ chain-converges to $\left(\omega, \vec{v}_{1}, \ldots, \vec{v}_{r}\right)$, where $\vec{\alpha}_{n}=\vec{\beta}$ for all $n$, each $\vec{v}_{j}$ is empty, and $\overrightarrow{\mathfrak{p}}$ is admissible for $\vec{\beta}$. Then $\omega_{n} \rightarrow \omega$ in $M(X ; \vec{\beta})$ with its usual topology.

Proof This follows from Proposition 6.3. \(\square\)

In other words, if a sequence $\omega_{n}$ in a moduli space $M$ chain-converges to an element $\omega \in M$, then $\omega_{n} \rightarrow \omega$ in $M$ provided the perturbations are admissible.

Proposition 7.2 In the notation of Theorem 1.4, suppose that the sequence $\omega_{n} \in M\left(X^{(T(n))} ; \vec{\alpha}_{n}^{\prime}\right)$ chain-converges to $\mathbb{V}=\left(\omega, \vec{v}_{1}, \ldots, \vec{v}_{r}, \vec{v}_{1}^{\prime}, \ldots, \vec{v}_{r^{\prime}}^{\prime}\right)$, where $\min _{j} T_{j}(n) \rightarrow \infty$. Suppose also that the perturbation parameters $\overrightarrow{\mathfrak{p}}, \overrightarrow{\mathfrak{p}}^{\prime}$ are admissible for each $\vec{\alpha}_{n}^{\prime}$. Then the following hold:
\begin{itemize}
\item[(i)] For sufficiently large $n$ there is a smooth map $u_{n}: X^{(T(n))} \rightarrow U(1)$ such that $v_{n, j}=\left.u_{n}\right|_{\{0\} \times Y_{j}^{\prime}}$ satisfies $v_{n, j}\left(\alpha_{n, j}^{\prime}\right)=\gamma_{j}^{\prime}, j=1, \ldots, r^{\prime}$.
\item[(ii)] The chain limit is unique up to gauge equivalence, ie if $\mathbb{V}, \mathbb{V}^{\prime}$ are two chain limits of $\omega_{n}$ then there exists a smooth $u: X^{\#} \rightarrow U(1)$ which is translationary invariant over the ends of $X^{\#}$, and such that $u(\mathbb{V})=\mathbb{V}^{\prime}$.
\end{itemize}

In (i), recall that moduli spaces are labelled by critical points modulo null-homotopic gauge transformations. Note that we can arrange that the maps $u_{n}$ are translationary invariant over the ends. This allows us to identify the moduli spaces $M\left(X ; \vec{\alpha}_{n}^{\prime}\right)$ and $M\left(X ; \vec{\gamma}^{\prime}\right)$, so that we obtain a sequence $u_{n}\left(\omega_{n}\right), n \gg 0$ in a fixed moduli space.

In (ii) we define $u(\mathbb{V})$ as follows. Let $w_{j}: \mathbb{R} \times Y_{j} \rightarrow \mathrm{U}(1)$ and $w_{j}^{\prime}: \mathbb{R} \times Y_{j}^{\prime} \rightarrow \mathrm{U}(1)$ be the translationary invariant maps which agree with $u$ on $\{0\} \times Y_{j}$ and $\mathbb{R}_{+} \times Y_{j}^{\prime}$, respectively. Let $w: X \rightarrow \mathrm{U}(1)$ be the map which is translationary invariant over each end and agrees with $u$ on $X_{: 1}$. Then $u(\mathbb{V})$ is the result of applying the appropriate maps $w, w_{j}, w_{j}^{\prime}$ to the various components of $u(\mathbb{V})$.

Proof (i) For simplicity we only discuss the case of one end and no necks, ie the situation of Definition 7.1. The proof in the general case is similar.

Using Condition (v) of Definition 7.1 and a simple compactness argument it is easy to see that $\alpha_{n}$ is gauge equivalent to $\beta_{k}$ for all sufficiently large $n$. Moreover, Conditions (iv) and (v) of Definition 7.1 ensure that there exist $\tau, n^{\prime}>0$ such that if $n>n^{\prime}$ then $\omega_{n}$ restricts to a genuine monopole on $\left(t_{n, k}+\tau, \infty\right) \times Y$ and on $\left(t_{n, j-1}+\tau, t_{n, j}-\tau\right) \times Y$ for $j=1, \ldots, k$. It then follows from Proposition 6.3 that $v_{n}=\left.u_{n, k}\right|_{\{0\} \times Y}$ satisfies $v_{n}\left(\alpha_{n}\right)=\beta_{k}$ for $n \gg$ 0 . (Recall again that $\alpha_{n}, \beta_{k} \in \widetilde{\mathcal{R}}_{Y}$ are critical points modulo null-homotopic gauge transformations, so $v_{n}\left(\alpha_{n}\right)$ depends only on the homotopy class of $v_{n}$.) Similarly, it follows from Theorems 6.1, 6.2 that $\left.u_{n, j-1}\right|_{\{0\} \times Y}$ is homotopic to $\left.u_{n, j}\right|_{\{0\} \times Y}$ for $j=1, \ldots, r$ and $n \gg 0$, where $u_{n, 0}=u_{n}$. Therefore, $v_{n}$ extends over $X_{: 0}$.
(ii) This is a simple exercise. \(\square\)

\subsection*{7.2 Proof of Theorem 1.3}

By Propositions 3.115.6, and 4.3, if each $\mathfrak{p}_{j}$ has sufficiently small $C^{1}$ norm then $\overrightarrow{\mathfrak{p}}$ will be admissible for all $\vec{\alpha}$. Choose $\overrightarrow{\mathfrak{p}}$ so that this is the case. Set
$$C_{0}=-\inf _{n} \sum_{j} \lambda_{j} \vartheta\left(\alpha_{n, j}\right)<\infty .$$
Let $S_{n}$ be a smooth representative for $\omega_{n}$. The energy assumption on the asymptotic limits of $S_{n}$ is unaffected if we replace $S_{n}$ by $u_{n}\left(S_{n}\right)$ for some smooth $u_{n}: X \rightarrow \mathrm{U}(1)$ which is translationary invariant on $\left(t_{n}, \infty\right) \times Y$ for some $t_{n}>0$. After passing to a subsequence we can therefore, by Proposition 5.3. assume that $S_{n}$ c-converges over $X$ to some monopole $S^{\prime}$ which is in temporal gauge over the ends. Because $\overrightarrow{\mathfrak{p}}$ is admissible we have that
$$\partial_{t} \vartheta\left(\left.S_{n}\right|_{\{t\} \times Y_{j}}\right) \leq 0$$
for all $j, n$ and $t \geq 0$. From the energy bound (30) we then see that $S^{\prime}$ must have finite energy. Let $\gamma_{j}$ denote the asymptotic limit of $S^{\prime}$ over the end $\mathbb{R}_{+} \times Y_{j}$ as guaranteed by Proposition 4.4. Then
$$\limsup _{n} \vartheta\left(\alpha_{n, j}\right) \leq \vartheta\left(\gamma_{j}\right)$$
for each $j$. Hence there is a constant $C_{2}<\infty$ such that for $h=1, \ldots, r$ and all $n$ one has
$$C_{2}+\lambda_{h} \vartheta\left(\alpha_{n, h}\right) \geq \sum_{j} \lambda_{j} \vartheta\left(\alpha_{n, j}\right) \geq-C_{0} .$$

Consequently,
$$\sup _{n, j}\left|\vartheta\left(\alpha_{n, j}\right)\right|<\infty .$$
For the remainder of this proof we fix $j$ and focus on one end $\mathbb{R} \times Y_{j}$. For simplicity we drop $j$ from notation and write $Y, \alpha_{n}$ instead of $Y_{j}, \alpha_{n, j}$ etc.
After passing to a subsequence we may arrange that $\vartheta\left(\alpha_{n}\right)$ has the same value $L$ for all $n$ (here we use Condition (O1)). If $\vartheta(\gamma)=L$ then we set $k=0$ and the proof is complete. Now suppose $\vartheta(\gamma)>L$. Then there is an $n^{\prime}$ such that $\partial_{t} \vartheta\left(S_{n}(t)\right)<0$ for all $n \geq n^{\prime}, t \geq 0$. Set
$$\delta=\frac{1}{2} \min \left\{|x-y|: x, y \text { are distinct critical values of } \vartheta: \widetilde{\mathcal{B}}_{Y} \rightarrow \mathbb{R}\right\} .$$
The minimum exists by (O1). For sufficiently large $n$ we define $t_{n, 1} \gg 0$ implicitly by
$$\vartheta\left(S_{n}\left(t_{n, 1}\right)\right)=\vartheta(\gamma)-\delta .$$
It is clear that $t_{n, 1} \rightarrow \infty$ as $n \rightarrow \infty$. Moreover, Definition 7.1 (iv) must hold for $j=1$. For otherwise we can find $\epsilon>0$ and sequences $\tau_{\ell}, n_{\ell}$ with $\tau_{\ell}, n_{\ell} \rightarrow \infty$ as $\ell \rightarrow \infty$, such that
$$\vartheta\left(S_{n_{\ell}}\left(\tau_{\ell}\right)\right)-\vartheta\left(S_{n_{\ell}}\left(t_{n_{\ell}, 1}-\tau_{\ell}\right)\right)>\epsilon$$
for every $\ell$. As in the proof of Claim 6.1 there are smooth $\widetilde{u}_{\ell}: \mathbb{R} \times Y \rightarrow \mathrm{U}(1)$ satisfying $\vartheta \circ \widetilde{u}_{\ell}(0)=\vartheta$ such that a subsequence of $\widetilde{u}_{\ell}\left(\mathcal{T}_{t_{n_{\ell}}, 1}^{*} S_{n_{\ell}}\right)$ c-converges over $\mathbb{R} \times Y$ to a finite energy monopole $\widetilde{S}$ in temporal gauge. The asymptotic limit $\widetilde{\gamma}$ of $\widetilde{S}$ at $-\infty$ must satisfy
$$\epsilon \leq \vartheta(\gamma)-\vartheta(\widetilde{\gamma})<\delta,$$
where the first inequality follows from (40). This contradicts the choice of $\delta$. Therefore, Definition 7.1 (iv) holds for $j=1$ as claimed.
After passing to a subsequence we can find $u_{n, 1}: \mathbb{R} \times Y \rightarrow \mathrm{U}(1)$ such that $u_{n, 1}\left(\mathcal{T}_{t_{n, 1}}^{*} S_{n}\right)$ c-converges over $\mathbb{R} \times Y$ to some finite energy monopole $S_{1}^{\prime}$ in temporal gauge. Let $\beta_{1}^{ \pm}$denote the limit of $S_{1}^{\prime}$ at $\pm \infty$. A simple compactness argument shows that $\gamma$ and $\beta_{1}^{-}$are gauge equivalent, so we can arrange that $\gamma=\beta_{1}^{-}$by modifying the $u_{n, 1}$ by a fixed gauge transformation $\mathbb{R} \times Y \rightarrow \mathrm{U}(1)$. As in the proof of Proposition 7.2 (i) we see that $u_{n, 1}$ must be null-homotopic for all sufficiently large $n$. Hence $\vartheta\left(\beta_{1}^{+}\right) \geq L$. If $\vartheta\left(\beta_{1}^{+}\right)=L$ then we set $k=1$ and the proof is finished. If on the other hand $\vartheta\left(\beta_{1}^{+}\right)>L$ then we continue the above process. The process ends when, after passing successively to subsequences and choosing $u_{n, j}, t_{n, j}, \beta_{j}^{ \pm}$for $j=1, \ldots, k$ (where $\beta_{j-1}^{+}=\beta_{j}^{-}$, and $u_{n, j}$ is null-homotopic for $n \gg 0$ ) we have $\vartheta\left(\beta_{k}^{+}\right)=L$. This must occur after finitely many steps; in fact $k \leq(2 \delta)^{-1}(\vartheta(\gamma)-L)$. \(\square\)

\subsection*{7.3 Proof of Theorem 1.4}

For simplicity we first consider the case when there is exactly one neck (ie $r=1$ ), and we write $Y=Y_{1}$ etc. We will make repeated use of the local compactness results proved earlier.

Let $S_{n}$ be a smooth representative of $\omega_{n}$. After passing to a subsequence we can find smooth maps
$$u_{n}: X^{(T(n))} \backslash(\{0\} \times Y) \rightarrow \mathrm{U}(1)$$
such that $\widetilde{S}_{n}=u_{n}\left(S_{n}\right)$ c-converges over $X$ to some finite energy monopole $S^{\prime}$ which is in temporal gauge over the ends. Introduce the temporary notation $S_{n}(t)=\left.S_{n}\right|_{\{t\} \times Y}$, and similarly for $\widetilde{S}_{n}$ and $u_{n}$. For $0 \leq \tau<T(n)$ set
$$\Theta_{\tau, n}=\vartheta\left(S_{n}(-T(n)+\tau)\right)-\vartheta\left(S_{n}(T(n)-\tau)\right) .$$
Let $u_{n}^{ \pm}=u_{n}( \pm T(n))$ and
$$I_{n}^{ \pm}=2 \pi \int_{Y} \widetilde{\eta}_{j} \wedge\left[u_{n}^{ \pm}\right],$$
cf Equation (1). Since $\Theta_{0, n}$ is bounded as $n \rightarrow \infty$, it follows that $I_{n}^{+}-I_{n}^{-}$ is bounded as $n \rightarrow \infty$. By Condition (O1) there is a $q>0$ such that $q I_{n}^{ \pm}$is integral for all $n$. Hence we can arrange, by passing to a subsequence, that $I_{n}^{+}-I_{n}^{-}$is constant. In particular,
$$I_{n}^{+}-I_{1}^{+}=I_{n}^{-}-I_{1}^{-} .$$
Choose a smooth map $w: X \rightarrow \mathrm{U}(1)$ which is translationary invariant over the ends, and homotopic to $u_{1}^{-1}$ over $X_{: 0}$. After replacing $u_{n}$ by $w u_{n}$ for every $n$ we then obtain $I_{n}^{+}=I_{n}^{-}$. Set $I_{n}=I_{n}^{ \pm}$. We now have
$$\Theta_{\tau, n}=\vartheta\left(\widetilde{S}_{n}(-T(n))\right)-\vartheta\left(\widetilde{S}_{n}(T(n))\right) .$$
Let $\beta_{0}, \beta^{\prime}$ denote the asymptotic limits of $S^{\prime}$ over the ends $\iota^{+}\left(\mathbb{R}_{+} \times Y\right)$ and $\iota^{-}\left(\mathbb{R}_{+} \times Y\right)$, respectively. Set
$$L=\lim _{\tau \rightarrow \infty} \lim _{n \rightarrow \infty} \Theta_{\tau, n}=\vartheta\left(\beta_{0}\right)-\vartheta\left(\beta^{\prime}\right) .$$
Since $\Theta_{\tau, n} \geq 0$ for $\tau \geq 0$ we have $L \geq 0$.
Suppose $L=0$. Then a simple compactness argument shows that there is a smooth $v: Y \rightarrow \mathrm{U}(1)$ such that $v\left(\beta_{0}\right)=\beta^{\prime}$. Moreover, there is an $n_{0}$ such that $v u_{n}^{-} \sim u_{n}^{+}$for $n \geq n_{0}$, where ~ means 'homotopic'. Therefore, we can find a smooth $z: X \rightarrow \mathrm{U}(1)$ which is translationary invariant over the ends and homotopic to $u_{n_{0}}^{-1}$ over $X_{: 0}$, such that after replacing $u_{n}$ by $z u_{n}$ for every
$n$ we have that $\beta_{0}=\beta^{\prime}$ and $u_{n}^{+} \sim u_{n}^{-}$. In that case we can in fact assume that $u_{n}$ is a smooth map $X^{(T(n))} \rightarrow \mathrm{U}(1)$. The remainder of the proof when $L=0$ (dealing with convergence over the ends) is now a repetition of the proof of Theorem 1.3.
We now turn to the case $L>0$. For large $n$ we must then have $\partial_{t} S_{n}(t)<0$ for $|t| \leq T(n)$. Let $\delta$ be as in the proof of Theorem 1.3. We define $t_{n, 1} \in$ $(-T(n), T(n))$ implicitly for large $n$ by
$$\vartheta\left(\beta_{0}\right)=\vartheta\left(S_{n}\left(t_{n, 1}\right)\right)+I_{n}+\delta .$$
Then $\left|t_{n, 1} \pm T(n)\right| \rightarrow \infty$ as $n \rightarrow \infty$. As in the proof of Theorem 1.3 one sees that
$$\limsup _{n \rightarrow \infty}\left[\vartheta\left(S_{n}(-T(n)+\tau)\right)-\vartheta\left(S_{n}\left(t_{n, 1}-\tau\right)\right)\right] \rightarrow 0$$
as $\tau \rightarrow \infty$, and after passing to a subsequence we can find smooth $u_{n, 1}: \mathbb{R} \times$ $Y \rightarrow \mathrm{U}(1)$ such that $u_{n, 1}\left(\mathcal{T}_{t_{n, 1}}^{*} S_{n}\right)$ c-converges over $\mathbb{R} \times Y$ to a finite energy monopole $S_{1}^{\prime}$ in temporal gauge whose asymptotic limit at $-\infty$ is $\beta_{0}$. Let $\beta_{1}$ denote the asymptotic limit of $S_{1}^{\prime}$ at $\infty$. We now repeat the above process. The process ends when, after passing successively to subsequences and choosing $u_{n, j}, t_{n, j}, \beta_{j}$ for $j=1, \ldots, k$ one has that
$$\limsup _{n \rightarrow \infty}\left[\vartheta\left(S_{n}\left(t_{n, k}+\tau\right)\right)-\vartheta\left(S_{n}(T(n)-\tau)\right)\right] \rightarrow 0$$
as $\tau \rightarrow \infty$. As in the case $L=0$ one sees that $\beta_{k}, \beta^{\prime}$ must be gauge equivalent, and after modifying $u_{n}, u_{n, j}$ one can arrange that $\beta_{k}=\beta^{\prime}$. This establishes chain-convergence over the neck. As in the case $L=0$ we can in fact assume that $u_{n}$ is a smooth map $X^{(T(n))} \rightarrow \mathrm{U}(1)$, and the rest of the proof when $L>0$ is again a repetition of the proof of Theorem 1.3
In the case of multiple necks one applies the above argument successively to each neck. In this case, too, after passing to a subsequence one ends up with smooth maps $u_{n}: X^{(T(n))} \rightarrow \mathrm{U}(1)$ such that $u_{n}\left(S_{n}\right)$ c-converges over $X$. One can then deal with convergence over the ends as before. \(\square\)

\section*{8 Transversality}

We will address two kinds of transversality problems: non-degeneracy of critical points of the Chern-Simons-Dirac functional, and regularity of moduli spaces over 4-manifolds.

In this section we do not assume Condition (O1).
Recall that a subset of a topological space $Z$ is called residual if it contains a countable intersection of dense open subsets of $Z$.

\subsection*{8.1 Non-degeneracy of critical points}

Lemma 8.1 Let $Y$ be a closed, connected, Riemannian spin ${ }^{c}$ 3-manifold and $\eta$ any closed (smooth) 2-form on $Y$. Let $G^{*}$ be the set of all $\nu \in \Omega^{1}(Y)$ such that all irreducible critical points of $\vartheta_{\eta+d \nu}$ are non-degenerate. Then $G^{*} \subset \Omega^{1}(Y)$ is residual, hence dense (with respect to the $C^{\infty}$ topology).

Proof The proof is a slight modification of the argument in [15]. For $2 \leq k \leq$ $\infty$ and $\delta>0$ let $W_{k, \delta}$ be the space of all 1-forms $\nu$ on $Y$ of class $C^{k}$ which satisfy $\|d \nu\|_{C^{1}}<\delta$. Let $W_{k, \delta}$ have the $C^{k}$ topology. For $1 \leq k<\infty$ we define a $\mathcal{G}$-equivariant smooth map
$$\begin{aligned}
\Upsilon_{k}: \mathcal{C}^{*} \times L_{1}^{2}(Y ; i \mathbb{R}) \times W_{k, \delta} & \rightarrow L^{2}\left(Y ; i \Lambda^{1} \oplus \mathbb{S}\right), \\
(B, \Psi, \xi, \nu) & \mapsto \mathcal{I}_{\Psi} \xi+\nabla \vartheta_{\eta+d \nu}(B, \Psi),
\end{aligned}$$
where $\mathcal{G}$ acts trivially on forms, and by multiplication on spinors. Now if $\Upsilon_{k}(B, \Psi, \xi, \nu)=0$ then
$$\left\|\mathcal{I}_{\Psi} \xi\right\|_{2}^{2}=-\int_{Y}\left\langle\nabla \vartheta_{\eta+d \nu}(B, \Psi), \mathcal{I}_{\Psi} \xi\right\rangle=0$$
by (12), which implies $\xi=0$ since $\Psi \neq 0$. The derivative of $\Upsilon_{k}$ at a point $x=(B, \Psi, 0, \nu)$ is
$$D \Upsilon_{k}(x)(b, \psi, f, v)=H_{(B, \Psi)}(b, \psi)+\mathcal{I}_{\Psi} f+(i * d v, 0) .$$
Let $(B, \Psi)$ be any irreducible critical point of $\vartheta_{\eta}$. We will show that $P=$ $D \Upsilon_{k}(B, \Psi, 0,0)$ is surjective. Note that altering $(B, \Psi)$ by an $L_{2}^{2}$ gauge transformation $u$ has the effect of replacing $P$ by $u P u^{-1}$. We may therefore assume that $(B, \Psi)$ is smooth. Since $P_{1}=\mathcal{I}_{\Psi}+H_{(B, \Psi)}$ has surjective symbol, the image of the induced operator $L_{1}^{2} \rightarrow L^{2}$ is closed and has finite codimension. The same must then hold for $\operatorname{im}(P)$. Suppose $(b, \psi) \in L^{2}$ is orthogonal to $\operatorname{im}(P)$, ie $d b=0$ and $P_{1}^{*}(b, \psi)=0$. The second equation implies that $b$ and $\psi$ are smooth, by elliptic regularity. Writing out the equations we find as in [15] that on the complement of $\Psi^{-1}(0)$ we have $-b=i d r$ for some smooth function $r: Y \backslash \Psi^{-1}(0) \rightarrow \mathbb{R}$. We now invoke a result of Bär [4] which says that, because $B$ is smooth and $\Psi \not \equiv 0$, the equation $\partial_{B} \Psi=0$ implies that the zero-set of $\Psi$ is contained in a countable union of smooth 1-dimensional submanifolds of $Y$. In particular, any smooth loop in $Y$ can be deformed slightly so that it misses $\Psi^{-1}(0)$. Hence $b$ is exact. From Bär's theorem (or unique continuation for $\partial_{B}$, which holds when $B$ is of class $C^{1}$, see [19]) we also deduce that the complement of $\Psi^{-1}(0)$ is dense and connected. Therefore, $f$ has a smooth extension to all of $Y$, and as in [15] this gives $(b, \psi)=0$. Hence $P$ is surjective.

Consider now the vector bundle
$$E=\left(\mathcal{C}^{*} \underset{\mathcal{G}}{\times} L^{2}\left(Y ; i \Lambda^{1} \oplus \mathbb{S}\right)\right) \times L_{1}^{2}(Y ; i \mathbb{R}) \rightarrow \mathcal{B}^{*} \times L_{1}^{2}(Y ; i \mathbb{R}) .$$
For $1 \leq k<\infty$ the map $\Upsilon_{k}$ defines a smooth section $\sigma_{k, \delta}$ of the bundle
$$E \times W_{k, \delta} \rightarrow \mathcal{B}^{*} \times L_{1}^{2}(Y ; i \mathbb{R}) \times W_{k, \delta} .$$
By the local slice theorem, a zero of $\Upsilon_{k}$ is a regular point of $\Upsilon_{k}$ if and only if the corresponding zero of $\sigma_{k, \delta}$ is regular. Since surjectivity is an open property for bounded operators between Banach spaces, a simple compactness argument shows that the zero-set of $\sigma_{2, \delta}$ is regular when $\delta>0$ is sufficiently small. Fix such a $\delta$. Observe that the question of whether the operator (41) is surjective for a given $x$ is independent of $k$. Therefore, the zero-set $M_{k, \delta}$ of $\sigma_{k, \delta}$ is regular for $2 \leq k<\infty$. In the remainder of the proof assume $k \geq 2$.

For any $\rho>0$ let $\mathcal{B}_{\rho}$ be the set of elements $[B, \Psi] \in \mathcal{B}$ satisfying
$$\int_{Y}|\Psi| \geq \rho .$$
Define $M_{k, \delta, \rho} \subset M_{k, \delta}$ similarly. For any given $\nu$, the formula for $\Upsilon_{k}$ defines a Fredholm section of $E$ which we denote by $\sigma_{\nu}$. Let $G_{k, \delta, \rho}$ be the set of those $\nu \in W_{k, \delta}$ such that $\sigma_{\nu}$ has only regular zeros in $\mathcal{B}_{\rho} \times\{0\}$. For $k<\infty$ let
$$\pi: M_{k, \delta} \rightarrow W_{k, \delta}$$
be the projection, and $\Sigma \subset M_{k, \delta}$ the closed subset consisting of all singular points of $\pi$. A compactness argument shows that $\pi$ restricts to a closed map on $M_{k, \delta, \rho}$, hence
$$G_{k, \delta, \rho}=W_{k, \delta} \backslash \pi\left(M_{k, \delta, \rho} \cap \Sigma\right)$$
is open in $W_{k, \delta}$. On the other hand, applying the Sard-Smale theorem as in [11, Section 4.3] we see that $G_{k, \delta, \rho}$ is residual (hence dense) in $W_{k, \delta}$. Because $W_{\infty, \delta}$ is dense in $W_{k, \delta}$, we deduce that $G_{\infty, \delta, \rho}$ is open and dense in $W_{\infty, \delta}$. But then
$$\bigcap_{n \in \mathbb{N}} G_{\infty, \delta, \frac{1}{n}}$$
is residual in $W_{\infty, \delta}$, and this is the set of all $\nu \in W_{\infty, \delta}$ such that $\sigma_{\nu}$ has only regular zeros.

An irreducible critical point of $\vartheta_{\eta+d \nu}$ is non-degenerate if and only if the corresponding zero of $\sigma_{\nu}$ is regular. Thus we have proved that among all smooth 1-forms $\nu$ with $\|d \nu\|_{C^{1}}<\delta$, those $\nu$ for which all irreducible critical points of $\vartheta_{\eta+d \nu}$ are non-degenerate make up a residual subset in the $C^{\infty}$ topology. The
same must hold if $\eta$ is replaced with $\eta+d \nu$ for any $\nu \in \Omega^{1}(Y)$, so we conclude that $G^{*}$ is locally residual in $\Omega^{1}(Y)$, ie any point in $G^{*}$ has a neighbourhood $V$ such that $G^{*} \cap V$ is residual in $V$. Hence $G^{*}$ is residual in $\Omega^{1}(Y)$. (This last implication holds if $\Omega^{1}(Y)$ is replaced with any second countable, regular space.) \(\square\)

Proposition 8.1 Let $Y$ be a closed, connected, Riemannian spin ${ }^{c}$ 3-manifold and $\eta$ any closed 2 -form on $Y$ such that either $b_{1}(Y)=0$ or $\widetilde{\eta} \neq 0$. Let $G$ be the set of all $\nu \in \Omega^{1}(Y)$ such that all critical points of $\vartheta_{\eta+d \nu}$ are non-degenerate. Then $G$ is open and dense in $\Omega^{1}(Y)$ with respect to the $C^{\infty}$ topology.

Proof A compactness argument shows that $G$ is open. If $b_{1}(Y)>0$ then $\vartheta_{\eta+d \nu}$ has no reducible critical points and the result follows from Lemma 8.1
Now suppose $b_{1}(Y)=0$. Then we may assume $\eta=0$. For $0 \leq k \leq \infty$ let $W_{k}$ be the space of 1 -forms on $Y$ of class $C^{k}$, with the $C^{k}$ topology. If $\nu \in W_{1}$ then $\vartheta_{d \nu}$ has up to gauge equivalence a unique reducible critical point, represented by $(B-i \nu, 0)$ for any smooth spin connection $B$ over $Y$ with $\check{B}$ flat. This critical point is non-degenerate precisely when
$$\operatorname{ker}\left(\partial_{B-i \nu}\right)=0 \quad \text { in } L_{1}^{2} .$$
Let $G_{k}^{\prime}$ be the set of all $\nu \in W_{k}$ such that (42) holds. This is clearly an open subset of $W_{k}$. The last part of the proof of [15, Proposition 3] shows that $G_{k}^{\prime}$ is residual (hence dense) in $W_{k}$ for $2 \leq k<\infty$. Hence $G_{\infty}^{\prime}$ is open and dense in $\Omega^{1}(Y)=W_{\infty}$. Now apply Lemma 8.1 \(\square\)

Marcolli [25] proved a weaker result in the case $b_{1}(Y)>0$, allowing $\eta$ to vary freely among the closed 2-forms.

\subsection*{8.2 Regularity of moduli spaces}

The following lemma will provide us with suitable Banach spaces of perturbation forms.

Lemma 8.2 Let $X$ be a smooth $n$-manifold, $K \subset X$ a compact, codimension 0 submanifold, and $E \rightarrow X$ a vector bundle. Then there exists a separable Banach space $W$ consisting of smooth sections of $E$ supported in $K$, such that the following hold:
\begin{itemize}
\item[(i)] The natural map $W \rightarrow \Gamma\left(\left.E\right|_{K}\right)$ is continuous with respect to the $C^{\infty}$ topology on $\Gamma\left(\left.E\right|_{K}\right)$.
\end{itemize}
\begin{itemize}
\item[(ii)] For every point $x \in \operatorname{int}(K)$ and every $v \in E_{x}$ there exists a section $s \in \Gamma(E)$ with $s(x)=v$ and a smooth embedding $g: \mathbb{R}^{n} \rightarrow X$ with $g(0)=x$ such that for arbitrarily small $\epsilon>0$ there are elements of $W$ of the form $f s$ where $f: X \rightarrow[0,1]$ is a smooth function which vanishes outside $g\left(\mathbb{R}^{n}\right)$ and satisfies
$$f(g(z))= \begin{cases}0, & |z| \geq 2 \epsilon \\ 1, & |z| \leq \epsilon\end{cases}$$
\end{itemize}

Proof Fix connections in $E$ and $T X$, and a Euclidean metric on $E$. For any sequence $a=\left(a_{0}, a_{1}, \ldots\right)$ of positive real numbers and any $s \in \Gamma(E)$ set
$$\|s\|_{a}=\sum_{k=0}^{\infty} a_{k}\left\|\nabla^{k} s\right\|_{\infty}$$
and
$$W_{a}=\left\{s \in \Gamma(E): \operatorname{supp}(s) \subset K,\|s\|_{a}<\infty\right\} .$$
Then $W=W_{a}$, equipped with the norm $\|\cdot\|_{a}$, clearly satisfies (i) for any $a$. We claim that one can choose $a$ such that (ii) also holds. To see this, first observe that there is a finite dimensional subspace $V \subset \Gamma(E)$ such that
$$V \rightarrow E_{x}, \quad s \mapsto s(x)$$
is surjective for every $x \in K$. Fix a smooth function $b: \mathbb{R} \rightarrow[0,1]$ satisfying
$$b(t)= \begin{cases}1, & t \leq 1, \\ 0, & t \geq 4 .\end{cases}$$
We use functions $f$ that in local coordinates have the form
$$f_{r}(z)=b\left(r|z|^{2}\right),$$
where $r \gg 0$. Note that for each $k$ there is a bound $\left\|f_{r}\right\|_{C^{k}} \leq$ const $\cdot r^{k}$ where the constant is independent of $r \geq 1$. It is now easy to see that a suitable sequence $a$ can be found. \(\square\)

In the next two propositions, $X, \vec{\alpha}, \mu$ will be as in Subsection 1.3. Let $K \subset X$ be any non-empty compact codimension 0 submanifold. Let $W$ be a Banach space of smooth self-dual 2 -forms on $X$ supported in $K$, as provided by Lemma 8.2. The following proposition will be used in the proof of Theorem 1.2

Proposition 8.2 In the above situation, let $G$ be set of all $\nu \in W$ such that all irreducible points of the moduli space $M(X ; \vec{\alpha} ; \mu+\nu ; 0)$ are regular (here $\mathfrak{p}_{j}=0$ for each $j$ ). Then $G \subset W$ is residual, hence dense.

There is another version of this proposition where $W$ is replaced with the Fréchet space of all smooth self-dual 2-forms on $X$ supported in $K$, at least if one assumes that (O1) holds for each pair $Y_{j}, \eta_{j}$ and that (A) holds for $X, \widetilde{\eta}_{j}, \lambda_{j}$. The reason for the extra assumptions is that the proof then seems to require global compactness results (cf the proof of Lemma 8.1).
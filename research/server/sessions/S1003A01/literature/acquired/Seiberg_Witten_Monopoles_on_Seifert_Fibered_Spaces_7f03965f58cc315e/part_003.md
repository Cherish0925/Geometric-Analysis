---
retention_scope: session
part: 3
total_parts: 4
---

[Part 3/4 of: Seiberg–Witten Monopoles on Seifert Fibered Spaces]

Let $C:(0,1) \rightarrow(0, \infty)$ be any function satisfying
$$\lim _{\epsilon \mapsto 0} C(\epsilon) \epsilon=0$$
and
$$\lim _{\epsilon \mapsto 0} \frac{C(\epsilon)}{\log (\epsilon)}=-\infty$$
(for example, $C(\epsilon)=-\frac{\log (\epsilon)}{\sqrt{\epsilon}}$ ).
Letting
$$T(\epsilon)=\frac{2 \log \left(\frac{2 \kappa}{\epsilon \xi}\right)}{\gamma}+\frac{1}{\xi},$$
fix $\epsilon>0$ small enough that it satisfies each of the following inequalities:
$$T(\epsilon)>2+\frac{1}{\xi}$$
$$\log \left(\frac{3}{2}\right)>\epsilon$$
$$C(\epsilon)>\log (\sqrt{8})$$
$$\xi>\epsilon,$$
$$\frac{\gamma}{2}>\epsilon,$$
$$\frac{1}{3 \sup _{Y}|f|}>\epsilon,$$
$$\frac{m}{4 \xi}>\epsilon,$$
$$\frac{C(\epsilon)}{2 T(\epsilon)}>\kappa+\sup _{[1,2] \times Y}\left|\epsilon \Delta_{c y l} \lambda f e^{\epsilon t}\right|+\sup _{[0,1]}\left|\Delta_{c y l} \lambda e^{\epsilon t}\right|,$$
$$\frac{m}{8}>\left(\frac{4}{3} C(\epsilon)+1\right)\left(\epsilon^{2}+\xi \epsilon\right)+C(\epsilon) \epsilon\left|\sup \Delta_{c y l} f\right|$$
(Conditions 8.18 and 8.17 are satisfied for any $\epsilon$ sufficiently small, thanks to Equations 8.7 and 8.8 respectively.) Let $C=C(\epsilon), T=T(\epsilon)$ for the chosen value of $\epsilon$, let $\psi_{1}$ be the function provided by Construction 8.14, with $M=C / 2 T$, and let $\psi_{2}$ be the function provided by Construction 8.15. We will now verify that the function
$$u_{-}(t, x)=-\lambda(t) e^{-\epsilon t}-C \epsilon f(x) e^{\epsilon(t+T)} \lambda(T-t)+\left\{\begin{array}{cc}
\psi_{1}\left(t-T-\frac{1}{\xi}\right) & t \geq 0 \\
\psi_{2}(t+T) & t \leq 0
\end{array}\right.$$
satisfies
$$\mathcal{N}\left(u_{-}\right) \leq-\kappa e^{-\gamma|t|} .$$
We divide the problem into four cases, corresponding to four regions which cover $R^{o}$.
\begin{itemize}
\item[1.] On the set where $h \geq \frac{m}{2}$ and $t \leq-T$, we have that
$$\begin{aligned}
\mathcal{N}\left(u_{-}\right) \leq & \Delta_{\text {cyl }}\left(-(C+1+\epsilon C f) e^{\epsilon(t+T)}\right)+C \epsilon \Delta_{\text {cyl }} f e^{\epsilon(t+T)} \\
& +\frac{m}{2}\left(e^{-C(1+\epsilon f) e^{\epsilon t}}-1\right) \\
\leq & \left(\left(\frac{4}{3} C+1\right)\left(\epsilon^{2}+\xi \epsilon\right)+C \epsilon\left|\sup \Delta_{\text {cyl }} f\right|\right) e^{\epsilon(t+T)} \\
& +\frac{m}{2}\left(e^{-\frac{2 C}{3} e^{\epsilon(t+T)}}-1\right) \\
\leq & \frac{m}{8} e^{\epsilon(t+T)}+\frac{m}{2}\left(e^{-\frac{2 C}{3} e^{\epsilon(t+T)}}-1\right) .
\end{aligned}$$
(The first step follows from the assumption that $h \geq \frac{m}{2}$, together with the properties of Construction 8.15; the second step involves Inequality 8.15 and Inequality 8.18.) The above quantity is in turn bounded by $-\frac{m}{8} e^{\epsilon(t+T)}$, since the function
$$x \mapsto \frac{x}{2}+\left(e^{-\frac{2 C}{3} x}-1\right)$$
is negative on $x \in[0,1]$, thanks to Inequality 8.12. In turn, combining the above inequalities with Inequalities 8.16, 8.14, and 8.6, we have that
$$\mathcal{N}\left(u_{-}\right) \leq-\frac{m}{8} e^{\epsilon(t+T)}<-\frac{m}{8} e^{\epsilon t}<-\frac{\epsilon \xi}{2} e^{\epsilon t} .$$
The desired inequality over this region then follows from the above, together with the observation that for $|t|<T-\frac{1}{\xi}$,
$$-\frac{\epsilon \xi}{2} e^{-\epsilon|t|}<-\kappa e^{-\gamma|t|} .$$
This is true because for $t$ in this range, Inequality 8.14 and 8.9 give
$$e^{(\gamma-\epsilon)|t|} \geq e^{\frac{\gamma}{2} t} \geq e^{\frac{\gamma}{2}\left(T-\frac{1}{\xi}\right)}=\frac{\epsilon \xi}{2 \kappa} .$$
\item[2.] When $t \leq-T$ and $h \leq \frac{m}{2}$, we have that $\Delta_{\text {cyl }} f \geq 5 \xi$, due to our choice of $f$ and Inequality 8.5. Combining Inequalities 8.15 and 8.13, we have
$$\left(\epsilon^{2}+2 \xi \epsilon\right)(1+\epsilon f)<4 \xi \epsilon .$$
Combining this with Inequality 8.14, we get that over this region,
$$\begin{aligned}
\mathcal{N}\left(u_{-}\right) & \leq C\left(\left(\epsilon^{2}+2 \epsilon \xi\right)(1+\epsilon f)-\epsilon \Delta_{c y l} f\right) e^{\epsilon(t+T)} \\
& \leq-C \xi \epsilon e^{\epsilon(t+T)} \\
& <-\xi \epsilon e^{\epsilon t} .
\end{aligned}$$
\end{itemize}
\begin{itemize}
\item[] (The last step follows from the fact that $T \geq 0$ and $C \geq 1$, which are of course weaker than Inequalities 8.10 and 8.12.) Once again, the desired inequality then follows from Inequality 8.19.
\item[3.] Over the region $\left[-T, T-\frac{1}{\xi}\right] \times Y, u_{-}$is a pointwise non-positive function. This is clear over $\left[-T+1, T-\frac{1}{\xi}\right]$, since each term in the definition for $u_{-}$is non-positive. For $t \in[-T,-T+1]$,we use Inequality 8.15 to get
$$\left|C \epsilon \lambda f e^{\epsilon(t+T)}\right| \leq \frac{C e^{\epsilon}}{3} \leq \frac{C}{2} .$$
On the other hand, $\psi_{2}$ in the region $[-T, 0]$ is a linear function with slope $M$ and value $-C$ at $-T$, so in this region,
$$\psi_{2}(t) \leq-\frac{C}{2} ;$$
i.e. over all of $\left[-T, T-\frac{1}{\xi}\right] \times Y$,
$$u_{-} \leq 0,$$
and therefore
$$\mathcal{N}\left(u_{-}\right) \leq \Delta_{\text {cyl }}\left(u_{-}\right) .$$
Now, the function which is $\psi_{1}(t-T)$ for $t \geq 0$ and $\psi_{2}(t+T)$ for $t \leq 0$ is a linear function with slope $M$, so
$$\begin{aligned}
\mathcal{N}\left(u_{-}\right) \leq \Delta_{\text {cyl }}\left(u_{-}\right) & <-M+\sup \left(\Delta_{\text {cyl }}\left(\epsilon \lambda f e^{t \epsilon}\right)\right)+\sup \left(\Delta_{\text {cyl }} \lambda\right) \\
& <-\kappa,
\end{aligned}$$
which is exactly Inequality 8.17.
\item[4.] For all $t>T-\frac{1}{\xi}$, we have that $u_{-}=-e^{-\epsilon t}-\frac{M}{\xi} e^{-\xi(t-T)}$, so that
$$\begin{aligned}
\mathcal{N}\left(u_{-}\right) & \leq\left(\epsilon^{2}-2 \xi \epsilon\right) e^{-\epsilon t} \\
& \leq-\xi \epsilon e^{-\epsilon t} \\
& <-\kappa e^{-\gamma t}
\end{aligned}$$
(The first step follows from the fact that $u_{-}$is non-positive, the second follows from Inequality 8.13. and the third by Inequality 8.19.)
\end{itemize}

Verification that $u_{+}=-u_{-}$is an upper solution, i.e.
$$\mathcal{N}\left(u_{+}\right) \geq \kappa e^{\gamma|t|},$$
mirrors the above. The only conceptual difference occurs in Region 1, where we must verify an inequality of the form
$$-\frac{x}{2}+\left(e^{\frac{2 C}{3} x}-1\right) \geq 0$$
for $x \in[0,1]$. This is satisfied provided that $C \geq \frac{3}{4}$ (the condition which takes the place of Inequality 8.12). \(\square\)

\section*{9. Deformation Theory on the Cylinder.}

Section 7 and Section 8 together set up an identification, on the level of topological spaces, between the moduli space of flows on $R^{o}$ and holomorphic curves in $R$. Now, we would like to compare the corresponding deformation theories. But before we can consider this problem, we embark on a digression about exponentially decaying cohomology for complex manifolds with cylindrical ends.

\subsection*{9.1. Dolbeault Cohomology of Cylinders.}

Let $\widehat{E}$ be a Hermitian line bundle over $R$, and let $\widehat{A}$ be a compatible connection on $\widehat{E}$ whose associated $\bar{\partial}$-operator is integrable. Denote the sheaf of $\bar{\partial}_{A}$-holomorphic sections of $\widehat{E}$ by $\mathcal{E}$. Given a real number $\delta$, consider the presheaf over $R^{o}$ of $(p, q)$-forms with values in $E=\left.\widehat{E}\right|_{R^{o}}$, whose coefficients lie in
$$L_{\infty, \delta}^{2}:=\bigcap_{k=1}^{\infty} L_{k, \delta}^{2} .$$
This can be pushed forward to $R$ and sheafified to form a sheaf over $R$ denoted by $A_{\delta}^{p, q}(E)$. Explicitly, a section of $A_{\delta}^{p, q}(U, E)$ for $U \subset R$ is a form $\omega \in \Omega^{p, q}\left(U-U \cap \Sigma_{*}, E\right)$ such that there is a covering $\left\{U_{i}\right\}$ of $U$ for which $\left.\omega\right|_{U_{i}-U_{i} \cap \Sigma_{*}}$ has coefficients in $L_{\infty, \delta}^{2}$.

Remark 9.1. Of course, the sheaf $A_{\delta}^{p, q}$ is a subsheaf of the sheaf of $\mathcal{C}_{\delta / 2}^{\infty}$ forms, but the containment is proper: the function $e^{\frac{\delta \tau}{2}}$ is in $\mathcal{C}_{\delta / 2}^{\infty}$, but it is not a section of $A_{\delta}^{0,0}$.

Let
$$\left(E_{ \pm}, A_{ \pm}\right)=\left.(\widehat{E}, \widehat{A})\right|_{\Sigma_{ \pm}} .$$
We can define another subsheaf of the sheaf of continuous $p, q$ forms $A_{\delta, \Sigma_{*}}^{p, q}(E)$ generated by sections of $A_{\delta}^{p, q}(E)$, (smooth sections of) $\pi^{*}\left(\Omega^{p, q}\left(\Sigma_{+}\right)\right.$), and $\pi^{*}\left(\Omega^{p, q}\left(\Sigma_{-}\right)\right)$. A section of $A_{\delta, \Sigma_{*}}^{p, q}(E)$ is a form $\omega \in \Omega^{p, q}\left(U-U \cap \Sigma_{*}, E\right)$ such that there is a covering $\left\{U_{i}\right\}$ of $U$ such that for each $i, U_{i}$ hits only one of the curves $\Sigma_{-}, \Sigma_{+}$, and, if $U_{i} \cap \Sigma_{\mp}=\emptyset$, then
$$\omega=\omega_{\delta}+\pi^{*}\left(\omega_{ \pm}\right),$$
where $\omega_{\delta} \in A_{\delta}^{p, q}(E)$, and $\omega_{ \pm} \in \Omega^{p, q}\left(U \cap \Sigma_{ \pm}, E_{ \pm}\right)$is a (smooth orbïfold) form.
Recall ([14]) that a sheaf $\mathcal{F}$ over a topological space $X$ is called fine if it admits partitions of unity. In this case, the sheaf cohomology groups $H^{i}(X ; \mathcal{F})=0$ for all $i>0$. Moreover, if
$$0 \longrightarrow \mathcal{E} \longrightarrow \mathcal{F}^{0} \xrightarrow{d^{0}} \mathcal{F}^{1} \xrightarrow{d^{1}} \ldots$$
is a resolution of a sheaf $\mathcal{E}$ by fine sheaves, then there is a natural isomorphism between the sheaf cohomology of $\mathcal{E}$ with the cohomology of the chain complex of sections of $\mathcal{F}^{i}$,
$$H^{i}(X ; \mathcal{E}) \cong H^{i}\left(\Gamma\left(X, \mathcal{F}^{*}\right), d^{*}\right) .$$

Proposition 9.2. Let $\mathcal{E} \otimes \mathcal{I}_{\Sigma_{*}}$ denote the kernel of the restriction map
$$\left.\mathcal{E} \rightarrow \mathcal{E}\right|_{\Sigma_{*}} .$$
For any $\delta$ with $0<\delta<2$, the complex $\left(A_{\delta}^{0, p}(E), \bar{\partial}_{A}\right)$ forms a fine resolution of the sheaf $\mathcal{E} \otimes \mathcal{I}_{\Sigma_{*}}$. Thus,
$$H^{i}\left(\Omega_{\delta}^{0, *}\left(R^{o}, E\right), \bar{\partial}_{A}\right) \cong H^{i}\left(R, \mathcal{E} \otimes \mathcal{I}_{\Sigma_{*}}\right) .$$

Remark 9.3. Caution: $\mathcal{E} \otimes \mathcal{I}_{\Sigma_{*}}$ is not the tensor product of coherent sheaves over $R$; rather, it is a tensor product of orbifold sheaves. More precisely, if
$$\phi: \widetilde{U} \rightarrow R$$
is an orbifold coordinate chart with an action of $\mathbb{Z} / p \mathbb{Z}$ such that the orbifold sections of $\mathcal{E}$ correspond to the $\mathbb{Z} / p \mathbb{Z}$-invariant sections of $\widetilde{\mathcal{E}}$, then sections of $\mathcal{E} \otimes \mathcal{I}_{\Sigma_{*}}$ correspond to the $\mathbb{Z} / p \mathbb{Z}$-invariant sections of
$$\tilde{\mathcal{E}} \otimes_{\mathcal{O}_{\tilde{U}}} \mathcal{I}_{\phi^{-1}\left(\Sigma_{*}\right)},$$
where $\mathcal{I}_{\phi^{-1}\left(\Sigma_{*}\right)}$ is the ideal sheaf in $\mathcal{O}_{\tilde{U}}$ of the pre-image of $\Sigma_{*}$.

Corollary 9.4. For sufficiently $0<\delta<2$, the complex $\left(A_{\delta, \Sigma_{*}}^{0, *}, \bar{\partial}_{A}\right)$ forms a fine resolution of the sheaf $\mathcal{E}$, so that
$$H^{i}\left(A_{\delta, \Sigma_{*}}^{0, *}, \bar{\partial}_{A}\right) \cong H^{i}(R, \mathcal{E}) .$$

Proof. The pair $\left(A_{\delta, \Sigma_{*}}^{0, *}(E), \bar{\partial}_{A}\right)$ is a clearly a complex of fine sheaves. Moreover, it naturally fits into a short exact sequence of sheaves
$$0 \longrightarrow A_{\delta}^{0, *}(E) \longrightarrow A_{\delta, \Sigma_{*}}^{0, *}(E) \longrightarrow A^{0, *}\left(\Sigma_{*}, \mathcal{E} \mid \Sigma_{*}\right) \longrightarrow 0 .$$
Since both $A_{\delta}^{0, *}(E)$ and $A^{0, *}\left(\Sigma_{*},\left.E\right|_{\Sigma_{*}}\right)$ are acyclic complexes of sheaves (Proposition 9.2), so is $A_{\delta, \Sigma_{*}}^{0, *}(E)$.

It remains therefore to identify the kernel $K$ of
$$\bar{\partial}: A_{\delta, \Sigma_{*}}^{0,0}(E) \rightarrow A_{\delta, \Sigma_{*}}^{0,1}(E) .$$
Restricting holomorphic sections of $\mathcal{E}$ from $R$ to $R^{o} \subset R$ induces a sheaf map
$$\mathcal{E} \rightarrow K,$$
since $\mathcal{E}$ is generated by the subsheaves of holomorphic functions which vanish along $\Sigma_{*}, \mathcal{E} \otimes \mathcal{I}_{\Sigma_{*}}$, and the sheaf of holomorphic functions which are pullbacks of holomorphic functions defined over $\Sigma_{*}$. It follows then that $K \cong \mathcal{E}$, from the short exact sequence above and the proposition. \(\square\)

The proof of Proposition 9.2 is tantamount to showing a version of the $\bar{\partial}$ -Poincaré lemma, which we build to in the following sequence of lemmas. But first, some notation. Let $D_{r}$ denote the disk of radius $r$ in the complex plane, and $C_{T}=[T, \infty) \times S^{1}$ be the cylinder with its natural complex structure.

Given $T \in \mathbb{R}$, let $\mathcal{H}_{\delta}\left(D_{r} \times C_{T}\right)$ denote the space of holomorphic functions which lie in $L_{\infty, \delta}^{2}$ (i.e. functions in $L_{\infty, \delta}^{2}\left(D_{r} \times C_{T}\right)$ which can be holomorphically extended to $D_{r^{\prime}} \times C_{T^{\prime}}$ for some $r^{\prime}>r, T^{\prime}<T$ ). By elliptic regularity, a holomorphic function lies in this space if and only if it lies in $L_{0, \delta}^{2}$. Let
$$c: D_{r} \times C_{T} \rightarrow D_{r} \times D_{e^{-T}}$$
given by
$$(w, z) \mapsto\left(w, e^{-z}\right) .$$

Lemma 9.5. The space $\mathcal{H}_{\delta}\left(D_{r} \times C_{T}\right)$ is identified via precomposition with $c$ with the space of holomorphic functions on $D_{r} \times D_{e^{-T}}$ which vanish to order greater than $\delta / 2$ along the subspace $D_{r} \times\{0\}$.

Proof. Suppose $f \in \mathcal{H}_{\delta}\left(D_{r} \times C_{T}\right)$. Then, by the Rellich lemma,
$$\lim _{t \mapsto+\infty}|f| e^{t \delta / 2}=0,$$
so the function $\widetilde{f}$ we get by extending $c^{*} f$ by zero over $D_{r} \times\{0\}$ is continuous over $D_{r} \times D_{e^{-T}}$ and holomorphic away from $D_{r} \times\{0\}$. By the removable singularities theorem of complex analysis, it follows then that $\widetilde{f}$ is holomorphic over all of $D_{r} \times D_{e^{-T}}$. In fact, the same argument says that if $n \leq \frac{\delta}{2}$, then $\widetilde{f}(z) / z^{n}$ extends over all of $D_{r} \times D_{e^{-T}}$ as a function which vanishes at along $D_{r} \times\{0\}$.

Conversely, by Taylor's theorem, if $f$ is a holomorphic function defined over $D_{r} \times D_{e^{-T}}$ which vanishes to order greater than $\delta / 2$ along $D_{r} \times\{0\}$, we can write $f=z^{n} g$ for $n>\delta / 2$ and $g$ a holomorphic function over $D_{r} \times C_{T}$. It follows then that
$$\|f\|_{L_{\delta}^{2}} \leq \pi r^{2}\|g\|_{L^{\infty}}\left(\int_{0}^{\infty} e^{-2 n+\delta} d t\right)<\infty .$$ \(\square\)

Definition 9.6. Given a smooth function
$$g: D_{r} \times C_{T} \rightarrow \mathbb{C},$$
let
$$Q_{z} g: D_{r} \times C_{T} \rightarrow \mathbb{C}$$
denote the function given by
$$Q_{z} g(w, z)=\frac{1}{2 \pi i} \int_{C_{T}} \frac{f(w, \eta) d \eta \wedge d \bar{\eta}}{1-e^{z-\eta}},$$
whenever the above integral makes sense.
Lemma 9.7. If $\frac{\delta}{2} \notin \mathbb{Z}$, then $Q_{z}$ induces a bounded map
$$Q_{z}: L_{\infty, \delta}^{2}\left(D_{r} \times C_{T}\right) \rightarrow L_{\infty, \delta}^{2}\left(D_{r} \times C_{T}\right)$$
with the property that
$$\frac{\partial}{\partial \bar{z}} Q_{z} f(w, z)=f(w, z) .$$

Proof. For $f: C_{T} \rightarrow \mathbb{C}$, define
$$Q f(z)=\frac{1}{2 \pi i} \int_{C_{T}} \frac{f(\eta) d \eta \wedge d \bar{\eta}}{1-e^{z-\eta}}$$
Write the Fourier expansion for a function $f$ as
$$f(t+i \theta)=\sum_{n \in \mathbb{Z}} \widehat{f}_{n}(t) e^{2 \pi i n \theta} .$$
Using Cauchy's integral formula, we have for any $a \in \mathbb{C}$ with $|a| \neq 1$ that
$$\frac{1}{2 \pi} \int \frac{e^{-i n \theta} d \theta}{1-a e^{i \theta}}=\left\{\begin{aligned}
a^{n} & \text { if }|a|<1 \text { and } n \geq 0 \\
-a^{n} & \text { if }|a|>1 \text { and } n \leq 0 \\
0 & \text { otherwise }
\end{aligned}\right.$$
so that, writing $\eta=s+i \varphi$
$$\begin{aligned}
\widehat{Q f}_{n}(t) & =\frac{1}{2 \pi} \int e^{-i n \theta} d \theta\left(\frac{1}{2 \pi i} \int_{C_{T}} \frac{f(\eta) d \eta \wedge d \bar{\eta}}{1-e^{z-\eta}}\right) \\
& =\frac{1}{2 \pi i} \int_{C_{T}} f(\eta) d \eta \wedge d \bar{\eta}\left(\frac{1}{2 \pi} \int \frac{e^{-i n \theta} d \theta}{e^{t+i \theta-\eta}-1}\right) \\
& =\frac{1}{2 \pi i} \int_{C_{T}} f(s+i \varphi)(-2 i d s \wedge d \varphi)\left\{\begin{array}{c}
e^{n(t-s-i \varphi)} \chi_{(t, \infty)}(s) \\
-e^{n(t-s-i \varphi)} \chi_{(T, t)}(s)
\end{array} \text { if } n \geq 0\right. \\
& =2\left\{\begin{aligned}
-\int_{t}^{\infty} \widehat{f}_{n}(s) e^{n(t-s)} d s & \text { if } n \geq 0 \\
\int_{T}^{t} \widehat{f}_{n}(s) e^{n(t-s)} d s & \text { if } n<0
\end{aligned}\right.
\end{aligned}$$
Using the obvious isometry for each $k \in \mathbb{Z}$
$$\phi_{\delta}: L_{k, \delta}^{2} \cong L_{k}^{2}$$
given by
$$\phi_{\delta}(f)=f e^{\frac{t \delta}{2}},$$
we see that $Q$ corresponds to the parametrix for $\phi_{\delta} \frac{\partial}{\partial \bar{z}} \phi_{\delta}^{-1}$ acting on the cylinder $C_{T}$ with APS boundary conditions constructed in Proposition 2.5 of [1]. It follows from this proposition, then, that $Q$ induces a bounded map $Q: L_{k, \delta}^{2}\left(C_{T}\right) \rightarrow L_{k+1, \delta}^{2}\left(C_{T}\right)$ whenever $\frac{\delta}{2} \notin \mathbb{Z}$.

Since
$$\int \mu_{D_{r}}(w) \int \mu_{C_{T}^{\prime}}(z)\left|Q_{z} f(w, z)\right|^{2} e^{t \delta} \leq C \int \mu_{D_{r}}(w) \int \mu_{C_{T}^{\prime}}(z)|f(w, z)|^{2} e^{t \delta},$$
we have by Fubini's theorem that $Q_{z}$ maps $L_{0, \delta}^{2}\left(D_{r} \times C_{T}\right)$ to $L_{0, \delta}^{2}\left(D_{r} \times C_{T}^{\prime}\right)$. Similarly, since $Q_{z}$ commutes with differentiation, we have that $Q$ extends to a map from $L_{k, \delta}^{2}$ to itself for each $k$, and hence a map from $L_{\infty, \delta}^{2}$ to itself. \(\square\)

We now prove Proposition 9.2
Proof. Clearly, $A_{\delta}^{0, p}$ is a fine sheaf. We must show that given $U \subset R$, $\omega \in \Omega_{\infty, \delta}^{0, p}\left(U,\left.E\right|_{U}\right)$ with $\bar{\partial}_{A} \omega=0$, and $x \in U$, there is an open neighborhood $V \subset U$ of $x$ and a form $\eta_{V} \in \Omega_{\infty, \delta}^{0, p-1}\left(V ;\left.E\right|_{V}\right)$ such that
$$\bar{\partial}_{A} \eta=\left.\omega\right|_{V} .$$

When $x \notin \Sigma_{*}$, this follows from the $\bar{\partial}$-Poincaré lemma. When $x \in \Sigma_{*}$, we imitate the usual proof of the this lemma.

Suppose that $x \in \Sigma_{*}$, but $x$ is not a singular point. Then, there is a neighborhood of $x \in R$ of the form $D_{r} \times D_{e^{-T}}$ with respect to which $x$ corresponds to the origin, $\Sigma_{*}$ corresponds to $D_{r} \times\{0\}$, holomorphic sections of $E$ correspond to holomorphic functions (under a holomorphic trivialization of $\left.\mathcal{E}\right|_{D_{r} \times C_{T}}$ ), and $\left.\omega\right|_{D_{r} \times D_{e^{-T}-0}}$ corresponds to a form in $L_{\infty, \delta}^{2}\left(D_{r} \times C_{T} ; \Lambda^{0, p}\right)$ satisfying $\bar{\partial} \omega=0$. We would like to find a form $\eta \in L_{\infty, \delta}^{2}\left(D_{r} \times C_{T}\right)$ with $\bar{\partial} \eta=\omega$.

When $p=2$, write $\omega=f d \bar{w} \wedge d \bar{z}$, and let $\eta=-Q z f d \bar{w}$. The fact that $\eta$ lies in the requisite Sobolev spaces and satisfies $\bar{\partial} \eta=\omega$ follows from Lemma 9.7.

When $p=1$, write $\omega=g d \bar{w}+h d \bar{z}$. We reduce to the case where $h=0$ by subtracting $\bar{\partial} Q_{z} h$.

When $p=1$, and $\omega$ is of the form
$$\omega=g d \bar{w},$$
let
$$Q_{w} g(w, z)=\frac{1}{2 \pi i} \int_{D_{r}} \frac{g(\xi, z)}{\xi-w} d \xi \wedge d \bar{\xi}$$
By Cauchy's integral formula, $Q_{w} g$ is a smooth function with $\frac{\partial}{\partial \bar{w}} Q_{w} g=$ $g$. The condition that $\bar{\partial} \omega=0$ is equivalent to the condition that $g$ is holomorphic in the $z$ variable, a property which is clearly preserved by the operator $Q_{w}$; thus, $\bar{\partial} Q_{w} g=\omega$.

To verify the integrability condition on $Q_{w} g$, recall Young's convolution inequality
$$\|f * g\|_{L^{2}} \leq\|f\|_{L^{1}}\|g\|_{L^{2}},$$
which gives us that
$$\int_{D_{r}}\left|Q_{w} g(w, z)\right|^{2} d w \wedge d \bar{w} \leq 2 r^{2} \int_{D_{r}}|g(w, z)|^{2} d w \wedge d \bar{w}$$
Thus, by Fubini's theorem, $Q_{w} g \in L_{0, \delta}^{2}$. Using elliptic regularity for $\bar{\partial}$ gives us then that $\eta \in L_{\infty, \delta}^{2}\left(D_{r^{\prime}} \times C_{T}\right)$, for any $r^{\prime}<r$.

Thus, we have verified the exactness of the sequence of sheaves
$$A_{\delta}^{0,0}(E) \xrightarrow{\bar{\partial}_{A}} A_{\delta}^{0,1}(E) \xrightarrow{\bar{\partial}_{A}} A_{\delta}^{0,2}(E) \longrightarrow 0$$
over the smooth locus of $R$.
When $x$ is a singular point, we can identify a neighborhood $U$ of $x$ with the quotient of $D_{r} \times D_{e^{-T}}$ by the $\mathbb{Z} / p \mathbb{Z}$ action
$$\zeta \times(w, z)=\left(\zeta w, \zeta^{p} z\right) .$$
For each $j=0, \ldots, p-1$, we can identify
$$L_{\infty, \delta}^{2}\left(U-\Sigma_{*} \cap U,\left.E\right|_{U-\Sigma_{*} \cap U}\right) \cong L_{\infty, \delta}^{2}\left(\frac{D_{r} \times C_{T}}{\mathbb{Z} / p \mathbb{Z}}, \mathcal{O}_{j}\right)$$
with the space of $\mathbb{Z} / p \mathbb{Z}$-equivariant sections of
$$L_{\infty, \delta}^{2}\left(D_{r} \times C_{T}\right),$$
i.e. those functions which satisfy
$$\zeta^{j} f(w, z)=f(\zeta w, z-q \log \zeta) .$$
This is true because the $\mathbb{Z} / p \mathbb{Z}$ acts by isometries which do not change the $t$ coordinate. Letting $\zeta^{*}$ denote pull-back (of forms) under the map which defines the $\mathbb{Z} / p \mathbb{Z}$ action, and letting $w, z$ denote the $D_{r}$ and $C_{T}$ coordinates on $D_{r} \times C_{T}$ respectively, note that
$$\zeta^{*} d \bar{w}=\zeta^{-1} d \bar{w}$$
and
$$\zeta^{*} d \bar{z}=d \bar{z}$$
Exactness of the Diagram 9.1 then follows once we have demonstrated that the parametrices $Q_{w}$ and $Q_{z}$ constructed earlier commute with the $\mathbb{Z} / p \mathbb{Z}$
action:
$$\begin{aligned}
\zeta^{*} Q_{w}(f d \bar{w})(w, z) & =\frac{1}{2 \pi i} \int_{D_{r}} \frac{f(\xi, z-q \log (\zeta)) d \xi \wedge d \bar{\xi}}{\zeta w-\xi} \\
& =\frac{1}{2 \pi i \zeta} \int_{D_{r}} \frac{f(\zeta \xi, z-q \log (\zeta)) d \xi \wedge d \bar{\xi}}{w-\xi} \\
& =\left(Q_{w} \zeta^{*} f\right) \zeta^{*}(d \bar{w}) \\
\zeta^{*} Q_{z}(f d \bar{z})(w, z) & =\frac{1}{2 \pi i} \int_{C_{T}} \frac{f(\zeta w, \eta-q \log (\zeta)) d \eta \wedge d \bar{\eta}}{1-e^{z-\eta}} \\
& =\left(Q_{z} \zeta^{*} f\right) \zeta^{*}(d \bar{z})
\end{aligned}$$

The fact that Sequence 9.1 is a resolution of the sheaf $\mathcal{E} \otimes \mathcal{I}_{\Sigma_{*}}$ when $0<\frac{\delta}{2}<1$ is an immediate consequence of Lemma 9.5. \(\square\)

Remark 9.8. More generally, for $\frac{\delta}{2} \notin \mathbb{Z}$, the above sequence provides a resolution of $\mathcal{E} \otimes \mathcal{I}_{\Sigma_{*}}^{\left[\frac{\delta}{2}\right]}$, the subsheaf of $\mathcal{E}$ generated by sections which vanish to order $\left\lceil\frac{\delta}{2}\right\rceil$ along $\mathcal{I}_{\Sigma_{*}}$.

Remark 9.9. Of course, the arguments given above generalize in an obvious way to any dimension, replacing the curve $\Sigma_{*}$ by a (complex) codimension-one sub-orbifold.

Example 9.10. If $X$ is a compact, complex curve, and $P \subset X$ is a finite collection of points, then we can give $X-P$ a complete metric with finitely many cylindrical ends. The above shows that the $L_{\delta}^{2}$-index of the $\bar{\partial}$ operator acting on $\mathcal{O}_{X-P}$ is the holomorphic Euler characteristic $\chi\left(X, \mathcal{I}_{P}\right)$, which is easily computed via the short exact sequence
$$0 \longrightarrow \mathcal{I}_{P} \longrightarrow \mathcal{O}_{X} \longrightarrow \oplus_{p \in P} \mathbb{C}_{p} \longrightarrow 0$$
to be $1-g-|P|$. This agrees with the computation appearing in [1] of the extended $L^{2}$-index of the $\bar{\partial}$ operator.

In Section 10, we need a version of Proposition 9.2 in the case where $\left(E, \bar{\partial}_{A}\right)$ does not quite extend over $R$. Assume rather that we are given $(E, A)$, a Hermitian line bundle with connection over $R^{o}$, which naturally extends over $R-\Sigma_{+}$, together with an isomorphism
$$j:\left.\left.\pi^{*}\left(E_{+}\right)\right|_{R^{o}} \rightarrow E\right|_{R^{o}}$$
such that
$$j^{*}(A)=A_{+}+i \delta_{0} \eta,$$
where $\delta_{0} \in(0,1), E_{+}$is an orbifold bundle over $\Sigma$, and $A_{+}$is a connection which extends over $R-\Sigma_{-}$. Then, we can form the line bundle $\mathcal{E}_{0}$ over $R$ given by patching $A$ to $A_{+}$using the complex gauge transformation $t \mapsto$ $e^{-\delta_{0} t}$; i.e. the $\bar{\partial}_{A_{+}}$-holomorphic section $\Phi$ of $\pi^{*}\left(E_{+}\right)$is identified with the $\bar{\partial}_{A}$-holomorphic section $e^{-t \delta_{0}} j^{*}(\Phi)$ of $\left.E\right|_{[T, \infty)}$.

Corollary 9.11. For any real $\delta \in\left(0, \delta_{0}\right)$, the complex $\left(A_{\delta}^{0, p}(E), \bar{\partial}_{A}\right)$ forms a fine resolution of the sheaf $\mathcal{E}_{0} \otimes \mathcal{I}_{\Sigma_{-}}$.

Proof. We must prove the following analogue of Lemma 9.5: Consider the complex structure $\bar{\partial}_{A}$ on the trivial bundle $D_{r} \times C_{T}$ induced by the connection $d-i \delta_{0} d \theta$. Then, for any real $\delta \in\left(0, \delta_{0}\right)$, the map which takes a function $\phi$ over $D_{r} \times D_{e^{-T}}$ to the function on $D_{r} \times C_{T}$ defined by
$$(w, z) \mapsto e^{-t \delta_{0}} \phi\left(w, e^{-z}\right)$$
induces an identification between the space of holomorphic functions on $D_{r} \times D_{e^{-T}}$ and the space of $\bar{\partial}_{A^{-}}$-holomorphic function on $D_{r} \times C_{T}$ which lie in $L_{\delta}^{2}$. This implies that the complex $\left(A_{\delta}^{0, *}(E), \bar{\partial}_{A}\right)$, which was shown to be a resolution, resolves $\mathcal{E}_{0} \otimes \mathcal{I}_{\Sigma_{-}}$. \(\square\)

\subsection*{9.2. Comparison of Deformation Theories.}

With this background in place, we turn to the identification of the deformation theories.

Definition 9.12. Let $U_{1}, U_{2} \subset \mathcal{C}^{\infty}(Y)$ be a pair of subsets, $\delta \in \mathbb{R}, k \in$ $\mathbb{Z} \cup \infty, k \geq 2$. The space of $U_{1}, U_{2}$-extended $L_{k, \delta}^{2}$ functions, denoted $L_{k, \delta, U_{1}, U_{2}}^{2}$, is the space of functions which can be written as
$$f_{0}+f_{1}+f_{2},$$
where $f_{0} \in L_{k, \delta}^{2}, f_{1}(t, y)=\lambda(t) g_{1}(y), f_{2}(t, y)=\lambda(-t) g_{2}(y)$, for $g_{i} \in U_{i}$, and $\lambda$ a cut-off function with $\lambda \equiv 0$ for $t \leq 0, \lambda \equiv 1$ for $t \geq 1$.

Example 9.13. The global sections of $A_{\delta, \Sigma_{*}}^{p, q}(E)$ are the $L_{\infty, \delta}^{2}$ sections of the bundle $\Lambda^{p, q}$ extended by the smooth forms in $\pi^{*}\left(\Omega^{p, q}\left(E_{-}\right)\right), \pi^{*}\left(\Omega^{p, q}\left(E_{+}\right)\right)$.

Let $\mathcal{C}_{1}$ and $\mathcal{C}_{2}$ be a pair of non-degenerate, irreducible critical manifolds (Definition 5.21) for cs and let $[A, \Phi] \in \mathcal{M}\left(\mathcal{C}_{1}, \mathcal{C}_{2}\right)$ correspond to a gradient flow line between them; i.e.
$$\left.\lim _{t \mapsto \pm \infty}[A, \Phi]\right|_{\{t\} \times Y}=\left[B_{ \pm}, \Psi_{ \pm}\right]$$
with $\left[B_{-}, \Psi_{-}\right] \in \mathcal{C}_{1},\left[B_{+}, \Psi_{+}\right] \in \mathcal{C}_{2}$ (we return to the case of flows to the trivial connection in Subsection 10.1). A neighborhood of $[A, \Phi]$ in $\mathcal{M}\left(\mathcal{C}_{1}, \mathcal{C}_{2}\right)$ can be described as follows. Choose spaces $U_{1}, U_{2}$ of $\left(B_{+}, \Psi_{+}\right)\left(B_{-}, \Psi_{-}\right)$ in $\mathcal{C}(Y)$ which project to open neighborhoods of $\left[B_{+}, \Psi_{+}\right],\left[B_{-}, \Psi_{-}\right]$in $\mathcal{C}_{1}, \mathcal{C}_{2} \subset \mathcal{B}(Y)$ respectively, and consider the configuration space $\mathcal{B}$ of $L_{k, \delta, U_{1}, U_{2}}^{2}$ perturbations of $(A, \Phi)$, modulo the action of the gauge group $L_{k+1, \delta}^{2}$-gauge transformations which are 1 at infinity. The Seiberg-Witten equations, viewed as a section of a bundle over $\mathcal{B}$, cut out a neighborhood of $[A, \Phi] \in \mathcal{M}\left(\mathcal{C}_{1}, \mathcal{C}_{2}\right)$. The tangent space of $\mathcal{B}$ is the quotient of the space of $T_{\left(B_{-}, \psi_{-}\right)} U_{1}, T_{\left(B_{-}, \psi_{-}\right)} U_{2}$-extended $L_{k, \delta}^{2}$ sections of $\Lambda^{1}(i \mathbb{R}) \times W$ by the image of $L_{k+1, \delta}^{2}$ under the derivative of the gauge group action. The linearization
$$D_{[A, \Phi]^{\mathrm{SW}}}: \mathrm{T}_{[\mathrm{A}, \Phi]} \mathcal{B} \rightarrow \Omega^{+}\left(R^{o}, i \mathbb{R}\right) \oplus \Gamma\left(R^{o}, \mathrm{~W}^{-}\right),$$
given by
$$(a, \phi) \mapsto\left(d^{+}+\widehat{\sigma}(\phi, \Phi), \mathbf{D}_{A} \phi+a \cdot \Phi\right),$$
where the range is given the $L_{k-1, \delta}^{2}$ topology, is Fredholm for all sufficiently small $\delta>0$ (and even when $\delta=0$, if the two critical manifolds are non-degenerate, isolated points). Here, $\widehat{\sigma}$ denotes the bilinear form corresponding to the quadratic function $\sigma$ appearing in the four-dimensional Seiberg-Witten Equaitons (Equation 4.7). Thus, the deformation complex, $\left(C_{s w}^{*}, d_{s w}^{*}\right)$, for $\mathcal{M}\left(\mathcal{C}_{1}, \mathcal{C}_{2}\right)$ is
$$\Omega^{0}\left(R^{o}, i \mathbb{R}\right) \longrightarrow \Omega^{1}\left(R^{o}, i \mathbb{R}\right) \oplus \Gamma_{\delta}\left(R^{o}, W^{+}\right) \longrightarrow \Omega^{+}\left(R^{o}, i \mathbb{R}\right) \oplus \Gamma_{\delta}\left(R^{o}, W^{-}\right),$$
This complex is graded so that the middle term in the above sequence has degree zero. The terms in degree $i \neq 0$ are required to lie in the Sobolev space $L_{\delta, k-i}^{2}$, while the term in degree zero lies in $L_{\delta, k}^{2}$ extended by $T_{\left(B_{1}, \psi_{1}\right)} U_{1} \oplus$ $T_{\left(B_{2}, \psi_{2}\right)} U_{1}$.

The Morse theory of [27] adapted to the Seiberg-Witten context reads as follows:

Theorem 9.14. Let $\mathcal{C}_{1}, \mathcal{C}_{2}$ be a pair of non-degenerate critical manifolds for cs. Given any $(A, \Phi) \in \mathcal{M}\left(C_{1}, C_{2}\right)$, with
$$\lim _{t \mapsto \pm \infty}[A, \Phi]_{\{t\} \times Y}=\pi^{*}\left[B_{ \pm}, \Psi_{ \pm}\right],$$
there is a Kuranishi map
$$\psi: H^{0}\left(C_{s w}^{*}, d_{s w}^{*}\right) \rightarrow H^{1}\left(C_{s w}^{*}, d_{s w}^{*}\right)$$
describing a neighborhood of $[A, \Phi]$ in $\mathcal{M}\left(\mathcal{C}_{1}, \mathcal{C}_{2}\right)$.
Definition 9.15. Let $\mathcal{C}_{1}, \mathcal{C}_{2}$ be a pair of non-degenerate critical manifolds for cs. The formal dimension of the space of flows from $\mathcal{C}_{1}$ to $\mathcal{C}_{2}$, written $\mathrm{e}-\operatorname{dim}\left(\mathcal{M}\left(\mathcal{C}_{1}, \mathcal{C}_{2}\right)\right)$ is the quantity defined by the formula:
$$\mathrm{e}-\operatorname{dim}\left(\mathcal{M}\left(\mathcal{C}_{1}, \mathcal{C}_{2}\right)\right):=\chi\left(H^{*}\left(C_{s w}^{*}, d_{s w}^{*}\right)\right) .$$

When $\mathcal{C}_{i} i=1,2$ are both non-degenerate, isolated points, the above quantity is the relative degree appearing in the Floer complex (see Section 13).

We have given an identification between the space of flows
$$\mathcal{M}\left(\mathcal{C}^{+}\left(E_{1}\right), \mathcal{C}^{+}\left(E_{2}\right)\right)$$
and an open subset of the space of divisors $\mathcal{D}\left(E_{1}, E_{2}\right)$ interpolating between $E_{1}$ and $E_{2}$. In this section, we compare Kuranishi descriptions of these spaces.

Theorem 9.16. Suppose that $E_{i} i=1,2$ correspond to irreducible critical manifolds $\mathcal{C}^{+}\left(E_{i}\right)$. Then, like the moduli space of divisors, the moduli space $\mathcal{M}\left(\mathcal{C}^{+}\left(E_{1}\right), \mathcal{C}^{+}\left(E_{2}\right)\right)$ is locally modeled about any point $(A, \Phi) \in$ $\mathcal{M}\left(\mathcal{C}^{+}\left(E_{1}\right), \mathcal{C}^{+}\left(E_{2}\right)\right)$ on the zeros of a map
$$H^{0}\left(D,\left.\mathcal{E}\right|_{D}\right) \rightarrow H^{1}\left(D,\left.\mathcal{E}\right|_{D}\right),$$
where $\mathcal{E}$ is the holomorphic structure induced by $(A, \Phi)$ on the line bundle interpolating $E_{1}$ and $E_{2}$, and $D=\alpha^{-1}(0)$ is the zero locus of the associated section. In particular,
$$\mathrm{e}-\operatorname{dim} \mathcal{M}\left(\mathcal{C}^{+}\left(E_{1}\right), \mathcal{C}^{+}\left(E_{2}\right)\right)=\mathrm{e}-\operatorname{dim} \mathcal{D}\left(E_{1}, E_{2}\right) .$$

Remark 9.17. Given a section $\alpha$ over an orbifold line bundle $\mathcal{E}$, the sheaf $\mathcal{E} / \alpha \mathcal{O}_{R}$ is supported along $D=\alpha^{-1}(0)$. Indeed, the pair $\left(D, \mathcal{E} / \alpha \mathcal{O}_{R}\right)$ is naturally a (possibly singular) orbifold curve equipped with an orbifold line bundle, which we write as $\left(D,\left.\mathcal{E}\right|_{D}\right)$.

Using the identifications of Isomorphism 6.1, together with the identifications ([6])
![](https://cdn.mathpix.com/cropped/42f1b57f-f433-4175-9f9c-9eca23c647ec-076.jpg?height=229&width=554&top_left_y=444&top_left_x=593)
we get a natural map of complexes from the Seiberg-Witten deformation complex (Diagram 9.2) to the complex $\left(C_{r}^{*}, d_{r}^{*}\right)$ defined by:
$$\Omega^{0,0} \longrightarrow \Omega^{0,1} \oplus\left(\Omega^{0,0} \oplus \Omega^{0,2}\right)(E) \longrightarrow \Omega^{0,2} \oplus \Omega^{0,1}(E),$$
where once again, the terms in degree $i \neq 0$ lie in $L_{k-i, \delta}^{2}$, while the term in degree 0 lies in $L_{k-i, \delta}^{2}$ is extended by $T_{\left(B_{1}, \psi_{1}\right)} U_{1} \oplus T_{\left(B_{1}, \psi_{1}\right)} U_{1}$.

To identify the cohomology groups of ( $C_{r}^{*}, d_{r}^{*}$ ) and ( $C_{s w}^{*}, d_{s w}^{*}$ ), we appeal to the following standard fact from homological algebra.

Lemma 9.18. Let $\left(C^{*}, d^{*}\right)$ be a cochain complex, $i \in \mathbb{Z}$, and $A, B$ be Abelian groups together with maps
$$f: A \rightarrow C^{i} \quad \text { and } \quad g: C^{i} \rightarrow B$$
with the properties that
$$d^{i} \circ f=g \circ d^{i-1}=0$$
and
$$f \circ g: A \rightarrow B$$
is an isomorphism. Then the natural map of chain complexes
![](https://cdn.mathpix.com/cropped/42f1b57f-f433-4175-9f9c-9eca23c647ec-076.jpg?height=222&width=1035&top_left_y=1747&top_left_x=350)
induces an isomorphism in cohomology.
Lemma 9.19. The natural map from the Seiberg-Witten deformation complex $\left(C_{s w}^{*}, d_{s w}^{*}\right)$ to the complex $\left(C_{r}^{*}, d_{r}^{*}\right)$ induces an isomorphism in cohomology.

Proof. We appeal to Lemma 9.18, with $A=\operatorname{Re} L_{k+1}^{2} \Omega_{\delta}^{0,0}$ and $B=$ $L_{k-1, \delta}^{2} \Omega^{0} \omega \subset \Omega_{\delta}^{+}\left(R^{o}, i \mathbb{R}\right)$. We must verify that the map induced from $A$ to $B$ by $\Lambda d_{s w}^{1} \circ d_{r}^{0}$ is an isomorphism. But
$$\begin{aligned}
\Lambda d_{s w}^{1} d_{r}^{0} f & =\Lambda d_{s w}^{1}(2 \bar{\partial} f, f \otimes \Phi) \\
& =2\left(i \operatorname{Im} \Lambda \partial \bar{\partial}+|\Phi|^{2}\right) f,
\end{aligned}$$
which is (half) the differential of the operator $\mathcal{N}$ encountered in Section 8. This was shown to be an isomorphism in Lemma 8.13. \(\square\)

Lemma 9.20. The natural map from the complex appearing in Diagram 9.4 to the complex $\left(C_{\mathbb{C}}^{*}, d_{\mathbb{C}}^{*}\right)$ given by
$$\Omega^{0,0} \longrightarrow \Omega^{0,1} \oplus \Omega^{0,0}(E) \longrightarrow \Omega^{0,2} \oplus \Omega^{0,1}(E) \longrightarrow \Omega^{0,2}(E),$$
with the conventions for Sobolev completion the same as for the complex $\left(C_{s w}^{*}, d_{s w}^{*}\right)$, induces an isomorphism in cohomology.

Proof of Theorem 9.16. Once again, we appeal to Lemma 9.18, this time with $A=L_{k}^{2} \Omega_{\delta}^{0,2}(E)$ and $B=L_{k-2}^{2} \Omega_{\delta}^{0,2}(E)$. Note that
$$\left.d_{\mathbb{C}}^{2} \circ d_{r}^{1}\right|_{A}=d_{\mathbb{C}}^{2} \circ\left(d_{\mathbb{C}}^{2}\right)^{*}: L_{k, \delta}^{2} \Omega^{0,2}(E) \rightarrow L_{k, \delta}^{2} \Omega^{0,2}(E),$$
where
$$\left(d_{\mathbb{C}}^{2}\right)^{*}: L_{k, \delta}^{2} \Omega^{0,2}(E) \rightarrow C_{\mathbb{C}}^{1}$$
denotes the formal $\left(L^{2}\right)$ adjoint of the differential operator defining $d_{\mathbb{C}}^{2}$.
To see injectivity of $d_{\mathbb{C}}^{2} \circ\left(d_{\mathbb{C}}^{2}\right)^{*}$, use integration by parts to identify its kernel with
$$\operatorname{Ker}\left(d_{\mathbb{C}}^{2}\right)^{*}=\left.\operatorname{Ker} D_{[A, \Phi]^{\mathrm{sw}}}\right|_{S^{-}} ;$$
but we have shown in Section 6 that the $S^{-}$-component of any element in the kernel of $D_{[A, \Phi]^{\mathrm{SW}}}$ vanishes, when $\Phi$ is a non-vanishing section of $S^{+}$. To see surjectivity, note that as a map from $L_{k, 0}^{2}$ to $L_{k-2,0}^{2}, d_{\mathbb{C}}^{2} \circ\left(d_{\mathbb{C}}^{2}\right)^{*}$ is Fredholm, as it asymptotically approaches
$$\left.\left(-\frac{d^{2}}{d t^{2}}+\left(D_{\left(B_{ \pm}, \Psi_{ \pm}\right)} \mathrm{sw}_{3}\right)^{2}\right)\right|_{S^{-}}$$
(where $\left(B_{ \pm}, \Psi_{ \pm}\right)$are the limiting values at $\pm \infty$ of the pair $(A, \Phi)$ ) and the operator $D_{\left(B_{ \pm}, \Psi_{ \pm}\right)} \mathrm{Sw}_{3}$ has no kernel in $S^{-}$, since $\Psi_{ \pm}$are nonvanishing sections of $S^{+}$. Moreover, when $\delta=0, d_{\mathbb{C}}^{2} \circ\left(d_{\mathbb{C}}^{2}\right)^{*}$ is formally self-adjoint, hence
it has index zero. Thus, for small $\delta>0$, the operator remains Fredholm of index zero. \(\square\)

Proof. A subcomplex of a complex is said to carry the cohomology if the inclusion map induces an isomorphism in cohomology. Consider the subcomplex $\left(C_{\delta}^{*}, d_{\delta}^{*}\right)=\left(C_{\mathbb{C}}^{*}, d_{\mathbb{C}}^{*}\right) \cap L_{\delta}^{2}$, the subcomplex consisting of un-extended Sobolev sections. For small $\delta$, this is a Fredholm complex, so its cohomology is carried by harmonic representatives. In particular, elliptic regularity tells us that the cohomology is carried by the subcomplex of sections which lie in $L_{\infty, \delta}^{2}$. Moreover, we have a short exact sequence of complexes
$$\begin{aligned}
0 \longrightarrow\left(C_{\delta}^{*}, d_{\delta}^{*}\right) & \longrightarrow \begin{array}{c}
\left(C_{\mathbb{C}}^{*}, d_{\mathbb{C}}^{*}\right) \\
\end{array} \longrightarrow T_{\left(B_{-}, \psi_{-}\right)} U_{1} \oplus T_{\left(B_{+}, \psi_{+}\right)} U_{2} \longrightarrow 0,
\end{aligned}$$
where the tangent space above is to be thought of as a complex concentrated in degree zero. Thus, by an easy application of the five-lemma, the cohomology of the complex $\left(C_{\mathbb{C}}^{*}, d_{\mathbb{C}}^{*}\right)$ is carried by $L_{\infty, \delta}^{2}$ forms (appropriately extended in degree zero). We have seen (Subsection 5.6 together with Subsection 5.7) that the tangent space to the critical manifolds carries the cohomology of the deformation complex for divisors in $\Sigma_{*},\left(C_{\Sigma}^{*}, d_{\Sigma}^{*}\right)$ :
$$\Omega^{0,0}\left(\Sigma_{*}\right) \longrightarrow \Omega^{0,1}\left(\Sigma_{*}\right) \oplus \Omega^{0,1}\left(\Sigma_{*}, E_{*}\right) \longrightarrow \Omega^{0,1}\left(\Sigma_{*}, E_{*}\right) .$$
This tells us that the extended $L_{\infty, \delta}^{2}$ subcomplex of $\left(C_{s w}^{*}, d_{s w}^{*}\right)$, thought of as a subcomplex of
$$\Omega^{0,0} \longrightarrow \Omega^{0,1} \oplus \Omega^{0,0}(E) \longrightarrow \Omega^{0,2} \oplus \Omega^{0,1}(E) \longrightarrow \Omega^{0,2}(E),$$
consisting of all $\Omega^{0, *}\left(\Sigma_{*}\right)$-extended $L_{\infty, \delta}^{2}$ forms, carries the cohomology of this complex.

But this latter complex is the mapping cone for the map
$$\underline{\Phi}: \Omega^{0, *} \rightarrow \Omega^{0, *}(E)$$
induced by
$$\omega \mapsto \omega \otimes \Phi,$$
viewed as a map between complexes of $\Omega^{0, *}\left(\Sigma_{*}\right)$-extended $L_{\infty, \delta}^{2}$ forms. Thus, by the isomorphisms in Lemmas 9.19 and 9.20, together with Corollary 9.4, we have that
$$H^{*}\left(C_{s w}^{*}, d_{s w}^{*}\right) \cong H^{*}\left(C_{\mathbb{C}}^{*}, d_{\mathbb{C}}^{*}\right) \cong H^{*}\left(\frac{\Omega^{0, *}(E)}{\Phi \Omega^{0, *}}\right) \cong H^{*}\left(\mathcal{E} / \alpha \mathcal{O}_{R}\right) . \square$$

\section*{10. Flows to the Reducible Locus.}

In this section, we will investigate the analogue of Theorem 7.6 for flows to the reducible locus.

Throughout this section we make the following assumptions. Let $Y=$ $S(N)$ be the unit sphere bundle over an orbifold bundle over $\Sigma$ with
$$\operatorname{deg}(N)<0 .$$
Fix a line bundle $E$ over $Y$ which is the pull-back of an orbifold line bundle over $\Sigma$, i.e. $c_{1}(E)$ is a torsion class. Moreover, assume that the reducible locus $\mathfrak{J}(E)$ in the corresponding $\operatorname{Spin}_{\mathrm{c}}(3)$ structure is non-degenerate. (See Proposition 5.16 and Corollary 5.17.)

Definition 10.1. Let $\left\lfloor\frac{K}{2}\right\rfloor$ be the orbifold line bundle over $\Sigma$ of maximal degree among all orbifold line bundles whose degree is less than $\frac{1}{2} \operatorname{deg}\left(K_{\Sigma}\right)$ and whose pull-back is isomorphic to $E$.

Moreover, let
$$\delta_{0}=\frac{\operatorname{deg}\left(\left\lfloor\frac{K}{2}\right\rfloor\right)-\frac{1}{2} \operatorname{deg}\left(K_{\Sigma}\right)}{\operatorname{deg}(N)} .$$

Remark 10.2. Given $E \cong \pi^{*}\left(E_{0}\right)$ for some orbifold line bundle $E_{0}$ over $\Sigma$, there is a unique line bundle $\left\lfloor\frac{K}{2}\right\rfloor$ which satisfies the above properties. This is clear, since the set of all orbifold line bundles over $\Sigma$ whose pull-back is isomorphic to $E$ is the set of all bundles of the form $E_{0} \otimes N^{k}$, for $k \in \mathbb{Z}$; and
$$\operatorname{deg}\left(E_{0} \otimes N^{k}\right)=\operatorname{deg}\left(E_{0}\right)+k \operatorname{deg}(N) .$$
Note that the definition of $\left\lfloor\frac{K}{2}\right\rfloor$ depends on the choice of $E$.
Fix an orbifold line bundle $E_{0}$ with $\pi^{*}\left(E_{0}\right) \cong E$, and $\operatorname{deg}\left(E_{0}\right)<$ $\frac{1}{2} \operatorname{deg}\left(K_{\Sigma}\right)$. In fact, fix isomorphisms
$$j_{-}: \pi^{*}\left(E_{0}\right) \rightarrow E$$
and
$$j_{+}: \pi^{*}\left(\left\lfloor\frac{K}{2}\right\rfloor\right) \rightarrow E .$$
Throughout this section, $\widehat{E}$ will denote the bundle over $R$ obtained by gluing $\pi^{*}\left(E_{0}\right)$ to $\pi^{*}\left(\left\lfloor\frac{K}{2}\right\rfloor\right)$ (viewed as bundles over $R-\Sigma_{+}$and $R-\Sigma_{-}$respectively) using the transition function $e^{\delta_{0} t} j_{+}^{-1} \circ j_{-}$over the overlap $R^{o} \subset R$. Note that by construction the restrictions $\left.\widehat{E}\right|_{\Sigma_{-}}$and $\left.\widehat{E}\right|_{\Sigma_{+}}$are canonically identified with the bundles $E_{0}$ and $\left\lfloor\frac{K}{2}\right\rfloor$ respectively.

Definition 10.3. Consider the space of generalized vortex pairs ( $A, \alpha$ ) which connect vortices in $E_{0}$ with reducibles in $\pi^{*}\left(\left\lfloor\frac{K}{2}\right\rfloor\right)$ via the given isomorphisms $j_{ \pm}$. The moduli space of generalized vortices which connect $E_{0}$ to $\mathfrak{J}(E)$, denoted $\mathcal{M}\left(E_{0}, \mathfrak{J}(E)\right)$, is the quotient of this space of pairs by the gauge automorphisms whose derivatives exponentially decay to zero. Dividing the space of generalized vortex pairs by the smaller goup of gauge transformations which exponentially decay to 1 , we obtain a larger space, the based moduli space, which is denoted $\mathcal{M}^{\circ}\left(E_{0}, \mathfrak{J}(E)\right)$. This space is a circle bundle over the (unbased) moduli space.

There is a corresponding notion for the moduli space of divisors.
Definition 10.4. Pick a reference point $x \in R$. The based moduli space of divisors connecting $E_{0}$ to $\left\lfloor\frac{K}{2}\right\rfloor$, denoted $\mathcal{D}^{\circ}\left(E_{0},\left\lfloor\frac{K}{2}\right\rfloor\right)$, is the quotient of the space of holomorphic pairs in $\widehat{E}$ by the subgroup of the complex gauge group which fixes the fiber $\left.\widehat{E}\right|_{x}$. The $\mathbb{C}^{*}$ action on this fiber induces a $\mathbb{C}^{*}$ action on $\mathcal{D}^{\circ}\left(E_{0},\left\lfloor\frac{K}{2}\right\rfloor\right)$, whose quotient is $\mathcal{D}\left(E_{0},\left\lfloor\frac{K}{2}\right\rfloor\right)$. Over the points represented by sections which do not vanish identically, the $\mathbb{C}^{*}$ action on $\mathcal{D}^{\circ}\left(E_{0},\left\lfloor\frac{K}{2}\right\rfloor\right)$ is free.

Remark 10.5. The space $\mathcal{D}^{\circ}\left(E_{0},\left\lfloor\frac{K}{2}\right\rfloor\right)$ inherits a deformation theory from $\mathcal{D}\left(E_{0},\left\lfloor\frac{K}{2}\right\rfloor\right)$ (see Remark 7.4).

A gradient flow line in the based moduli space from the critical manifold corresponding to $E_{0}, \mathcal{C}^{+}\left(E_{0}\right)$, to the reducible locus $\mathfrak{J}(E)$ induces, as in Section 7, a holomorphic pair over $\left.\widehat{E}\right|_{R-\Sigma_{+}}$. Indeed, the following analogue of Theorem 7.6 tells us that this data naturally extends over all of $\widehat{E}$ over $R$ :

Theorem 10.6. If $\mathcal{C}^{+}\left(E_{0}\right)$ is a critical manifold in the $\operatorname{Spin}_{\mathrm{c}}(3)$ structure determined by $E$, whose reducible critical manifold $\mathfrak{J}(E)$ is non-degenerate, then there is a natural identification between the based moduli space of flows connecting $\mathcal{C}^{+}\left(E_{0}\right)$ to $\mathfrak{J}(E)$ with the open subset of based divisors in $\mathcal{D}^{\circ}\left(E_{0},\left\lfloor\frac{K}{2}\right\rfloor\right)$ which do not contain $\Sigma_{-}$.

Remark 10.7. In particular, it is an easy consequence of this theorem that this space of flows is non-empty. Given a divisor $D_{0} \subset \Sigma$ corresponding to a critical point in $\mathcal{C}^{+}\left(E_{0}\right)$, the divisor
$$\pi^{*}\left(D_{0}\right)+\left(\operatorname{deg}\left(D_{0}\right)-\operatorname{deg}\left(\left\lfloor\frac{K}{2}\right\rfloor\right)\right)\left[\Sigma_{+}\right]$$
corresponds to a divisor in $\mathcal{D}\left(E_{0},\left\lfloor\frac{K}{2}\right\rfloor\right)$.

Remark 10.8. The space of flows from $\mathfrak{J}(E)$ to $\mathcal{C}^{+}\left(E_{0}\right)$ is empty, while all flows from $\mathfrak{J}(E)$ to $\mathfrak{J}(E)$ are stationary. This statement follows easily from Proposition 5.23.

The proof of this theorem follows the same lines as Theorem 7.6 and has two parts corresponding to the discussions in Sections 7 and 8 respectively.

To exhibit a map from the $\mathcal{M}^{\circ}$ to $\mathcal{D}^{\circ}$ we will use an alternative description of $\mathcal{D}^{\circ}$. Fix a vortex $\left(A_{-}, \alpha_{-}\right)$in $E_{0}$ and a constant curvature connection $B_{0}$ in $\left\lfloor\frac{K}{2}\right\rfloor$. Consider the space $\mathcal{S}$ of holomorphic pairs $(\widehat{A}, \widehat{\alpha})$ in $\widehat{E}$ so that:
\begin{itemize}
\item[-] $\left.(\widehat{A}, \widehat{\alpha})\right|_{\Sigma_{-}}=\left(A_{-}, \alpha_{-}\right)$
\item[-] $\left.\widehat{A}\right|_{\Sigma_{+}}=B_{0}$.
\end{itemize}

The quotient, $\mathcal{Q}$, of this space by the action of the group of complex gauge transformations which are the identity over $\Sigma_{ \pm}$is naturally identified with the based moduli space of divisors with $\left.[\widehat{A}, \widehat{\alpha}]\right|_{\Sigma_{-}}=\left[A_{-}, \alpha_{-}\right]$and $\left.[\widehat{A}]\right|_{\Sigma_{+}}=\left[B_{0}\right]$ (as complex gauge equivalence classes). We will now obtain an element of $\mathcal{Q}$ from a based flow line connecting the critical point in $\mathcal{C}^{+}\left(E_{0}\right)$ corresponding to $\left[A_{-}, \alpha_{-}\right]$to the reducible corresponding to $\pi^{*}\left(B_{0}\right)$.

Lemma 10.9. The real number $\delta_{0} \geq 0$ defined above is the smallest eigenvalue of the operator $i \nabla_{\frac{\partial}{\partial \varphi}}^{B}$ acting on $\Gamma\left(Y, S^{+}\right)$. Let $\delta_{1}$ be the smallest non-negative eigenvalue of $\mathbf{D}_{B}$ belonging to any eigenvector in $\Gamma\left(Y, S^{+}\right) \subset$ $\Gamma(Y, W)$, then $\delta_{0} \leq \delta_{1}$.

Proof. Given $\delta \in \mathbb{R}$, the $\delta$-eigenspace of $i \nabla_{\frac{\partial}{\partial \varphi}}$ for the is the kernel of $i \nabla_{\frac{\partial}{\partial \varphi}}^{B+i \delta \eta}$. Thus, pushing $B+i \delta \eta$ forward (according to Proposition 5.3), we identify the $\delta$-eigenspace of $i \nabla_{\frac{\partial}{\partial \varphi}}^{B}$ with sections of a bundle over $\Sigma$ whose curvature form is
$$F_{B}+\delta F_{N} .$$

This proves the first claim. The second follows from the fact that $i \nabla_{\frac{\partial}{\partial \varphi}}^{B}$ is the $S^{+}$-component of the Dirac operator, acting on $S^{+}$. \(\square\)

Proposition 10.10. Let $(A, \alpha)$ be a flow on $\mathbb{R} \times Y$ which converges exponentially to a reducible solution $[B, 0]$ as $t \mapsto+\infty$, then the pair
$$\left(e^{t \delta_{0}} \bar{\partial}_{A} e^{-t \delta_{0}}, e^{t \delta_{0}} \alpha\right)$$
converges exponentially to a the pull-back of a holomorphic pair $\left(B_{0}, \alpha_{0}\right)$ in $\left\lfloor\frac{K}{2}\right\rfloor$, where $B_{0}$ has constant curvature.

Proof. There are constants $\mu_{1}>0, \delta_{2}>\delta_{1}>0$ such that for any gradient flow line $(A, \alpha)$ as above, there is an asymptotic expansion (for $t \gg 0$ ) of the form
$$(A, \alpha)=\left(B+O\left(e^{-\mu_{1} t}\right), e^{-\delta_{1} t} \alpha_{1}+O\left(e^{-\delta_{2} t}\right)\right) .$$
Here, $\delta_{1}$ is the constant from Lemma 10.9, so that $\delta_{0} \leq \delta_{1}$. If $\delta_{0}<\delta_{1}$, let $\alpha_{0}=0$, otherwise, let $\alpha_{0}=\alpha_{1}$. In either case, we see that $e^{t \delta_{0}} c$ converges exponentially to $\alpha_{0}$.

The section $e^{t \delta_{0}} \alpha$ is harmonic for the Dirac operator
$$e^{t \delta_{0}} \mathbf{D}_{A} e^{-t \delta_{0}}=\mathbf{D}_{A}-\delta_{0} \rho(d t),$$
which is the same as $\mathbf{D}_{A+i \delta_{0} \eta}$, when restricted to $S^{+}$. Moreover, the connection $A+i \delta_{0} \eta$ converges as $t \mapsto+\infty$ to $B+i \delta_{0} \eta=\pi^{*}\left(B_{0}\right)$, so we see that $\alpha_{0}$ corresponds to a holomorphic section of $\left\lfloor\frac{K}{2}\right\rfloor$. \(\square\)

As an immediate consequence, we see that the sections $e^{t \delta_{0}} \alpha$ over $\pi^{*}\left(E_{0}\right)$, and $\alpha_{0}$ over $\Sigma_{+}$glue together to give a continuous section $\widehat{\alpha}$ of $\widehat{E}$. We can apply Theorem 7.7 to extend the holomorphic structure $\bar{\partial}_{A+i \delta_{0}}$ over $\pi^{*}\left(\left\lfloor\frac{K}{2}\right\rfloor\right)$, giving us a holomorphic structure on all of $\widehat{E}$ with respect to which $\widehat{\alpha}$ is holomorphic. Indeed the complex gauge transformation obtained in Theorem 7.7 is the idenity over $\Sigma_{ \pm}$and hence we obtain an element of $\mathcal{Q}$.

Thus, we have constructed a map from the moduli space of flows to the space of divisors. To invert this map, as before (Section 8), we have to solve a Kazdan-Warner equation for a complex gauge transformation. First, we solve the problem "at infinity":

Lemma 10.11. Let $\widehat{E}$ be the line bundle over $R$ defined as above. Suppose that $(\widehat{A}, \widehat{\alpha})$ is a holomorphic pair in $\mathcal{S}$. Then, there is a complex gauge transformation $e^{u}$ on $E$ which takes the restriction of $\left.(\widehat{A}, \widehat{\alpha})\right|_{R^{\circ}}$ to a pair $(A, \alpha)$ such that
\begin{itemize}
\item[1.] $(A, \alpha)$ converges exponentially as $t \mapsto-\infty$ to the vortex in $E_{0}$ with section $\left.\widehat{\alpha}\right|_{\Sigma_{-}}$, and
\item[2.] $(A, \alpha)$ converges exponentially as $t \mapsto+\infty$ to a reducible solution $[B, 0]$.
\end{itemize}

Proof. The hypothesis that $(\widehat{A}, \widehat{\alpha}) \in \mathcal{S}$ gives us that
$$\left.\left(2 \Lambda F_{\widehat{A}}-\Lambda F_{K_{\Sigma}}-i|\widehat{\alpha}|^{2}\right)\right|_{\Sigma_{-}} \equiv 0$$
and
$$\left.\left(i\left(2 \Lambda F_{\widehat{A}}-\Lambda F_{K_{\Sigma}}\right)-\frac{2 \pi\left(2 \operatorname{deg}\left(\left\lfloor\frac{K}{2}\right\rfloor\right)-\operatorname{deg}\left(K_{\Sigma}\right)\right)}{\operatorname{Vol}(\Sigma)}\right)\right|_{\Sigma_{+}} \equiv 0 .$$

Suppose that $\operatorname{deg}\left(\left\lfloor\frac{K}{2}\right\rfloor\right)=\frac{1}{2} \operatorname{deg}\left(K_{\Sigma}\right)$, then $\left.\alpha\right|_{\Sigma_{+}}$is a holomorphic section of an orbifold bundle whose degree is $\frac{1}{2} \operatorname{deg}\left(K_{\Sigma}\right)$ and whose pull-back to $Y$ is $E$. Thus, $\left.\alpha\right|_{\Sigma_{+}}=0$, by our assumption that $\mathfrak{J}(E)$ is non-degenerate (see Proposition 5.16). Now, the restriction $(A, \alpha)$ of $(\widehat{A}, \widehat{\alpha})$ to $R^{o}$ satisfies the requirements (by Lemma 8.2).

Suppose that $\operatorname{deg}\left(\left\lfloor\frac{K}{2}\right\rfloor\right) \neq \frac{1}{2} \operatorname{deg}\left(K_{\Sigma}\right)$, so that $\delta_{0}>0$. Recall that a complex gauge transformation $e^{u}$ acting on a connection $A$ on $E$ over $\mathbb{R} \times Y$ (i.e. the transformation which takes sections $\alpha \in \Gamma\left(E, R^{o}\right)$ to $e^{u} \alpha$ ) transforms the curvature according to
$$i \Lambda F_{e^{u} A} \mapsto 2 i \Lambda \bar{\partial} \partial u+i \Lambda F_{A}=-e^{-2 \xi t} \frac{\partial}{\partial t} e^{2 \xi t} \frac{\partial}{\partial t} u+\Delta_{Y} u+i \Lambda F_{A},$$
following Lemma 8.7. Thus, if $e^{u}$ is a complex gauge transformation with
$$u(t)=\left\{\begin{array}{ll}
0 & \text { if } t \ll 0 \\
-\delta_{0} t & \text { if } t \gg 0
\end{array},\right.$$
this complex gauge transformation takes the restriction of $(\widehat{A}, \widehat{\alpha})$ to a pair $(A, \alpha)$ which exponentially decays as $t \mapsto-\infty$ a vortex in $E_{0}$, and as $t \mapsto \infty$, it decays to a reducible solution [B, 0]. \(\square\)

Thanks to this lemma, finding a flow-line then becomes equivalent to solving the Kazdan-Warner equation
$$\Delta_{c y l}(u)+h\left(e^{u}-1\right)=k$$
for an exponentially decaying function $u$, where $h=|\alpha|^{2}$ satisfies
\begin{itemize}
\item[1.] $h \geq 0$,
\item[2.] $\lim _{t \mapsto-\infty} h=h_{-}$exponentially, for some function $h_{-} \not \equiv 0$
\item[3.] $\lim _{t \mapsto+\infty} h=0$ exponentially.
\end{itemize}

Under these hypotheses, Equation 10.1 has a unique exponentially decaying solution $u$, according to Proposition 8.3.

Suppose that $(\widehat{A}, \widehat{\alpha})$ is a holomorphic pair as in Lemma 10.11. Then, a gauge transformation over $R$ which is the identity over $\Sigma_{ \pm}$carries the pair $(A, \alpha)$ provided by that lemma to another pair which is equivalent to $(A, \alpha)$ by a gauge transformation which exponentially converges to 1. Thus, thanks to the uniqueness statement in Proposition 8.3, our construction maps $\mathcal{Q}$ to $\mathcal{M}^{\circ}\left(E_{0}, \mathfrak{J}(E)\right)$ as promised.

\subsection*{10.1. Deformation Theory of Flows to the Reducible Locus.}

We can slightly modify the discussion in Section 9 to obtain the following analogue of Theorem 9.16:

Theorem 10.12. Let $E, E_{0}$ be as in Theorem 10.6. Then, the based moduli space of flows to the reducible locus $\mathcal{M}^{\circ}\left(E_{0}, \mathfrak{J}(E)\right)$ is locally modeled about any point $(A, \Phi) \in \mathcal{M}^{\circ}\left(E_{0}, \mathfrak{J}(E)\right)$ on the zeros of a map
$$\mathbb{C} \oplus H^{0}\left(D,\left.\mathcal{E}\right|_{D}\right) \rightarrow H^{1}\left(D,\left.\mathcal{E}\right|_{D}\right),$$
where $\mathcal{E}$ is the holomorphic structure induced by ( $A, \Phi$ ) on the line bundle interpolating $E_{0}$ and $\left\lfloor\frac{K}{2}\right\rfloor$ from Theorem 10.6, and $D=\alpha^{-1}(0)$ is the zeroset of the associated section. In particular,
$$\mathrm{e}-\operatorname{dim} \mathcal{M}\left(\mathcal{C}^{+}\left(E_{0}\right), \mathfrak{J}(E)\right)=\mathrm{e}-\operatorname{dim}\left(\mathcal{D}\left(E_{0},\left\lfloor\frac{K}{2}\right\rfloor\right)\right)+1 .$$
Proof. Recall that the tangent space to the reducible locus is given by
$$T_{\left[B_{+}, 0\right]} U_{2}=\operatorname{Coker}\left(\bar{\partial}: \Omega^{0,0}\left(\Sigma_{+}\right) \rightarrow \Omega^{0,1}\left(\Sigma_{+}\right)\right) .$$
Bearing this in mind, the proof of Theorem 9.16 shows that the cohomology groups of the deformation complex are isomorphic to a mapping cone for
$$\underline{\Phi}: \Omega^{0, *} \rightarrow \Omega^{0, *}(E),$$
where forms in $\Omega^{0, *}$ are extended by $\pi^{*}\left(\Omega^{0, *}\left(\Sigma_{-}\right)\right)$at $-\infty$ but only by $T_{\left[B_{+}, 0\right]} U_{2}$ at $+\infty$; while forms in $\Omega^{0, *}(E)$ are extended by $\pi^{*}\left(\Omega^{0, *}\left(\Sigma_{-}, E_{0}\right)\right)$ at $-\infty$ and by nothing at $+\infty$.

With the above conventions on $\Omega^{0, *}$, the cohomology groups
$$H^{*}\left(\Omega^{0, *}, \bar{\partial}\right) \cong\left\{\begin{array}{rl}
0 & \text { if } *=0 \\
H^{*}\left(R, \mathcal{O}_{R}\right) & \text { otherwise }
\end{array},\right.$$
which we can see by mapping this complex to the corresponding complex of $L_{\infty, \delta}^{2}$ forms which are extended by all smooth forms pulling back from $\Sigma_{ \pm}$ at the ends $\pm \infty$, noting that the quotient complex is merely a $\mathbb{C}$ in degree zero, and then applying Corollary 9.4.

We wish now to identify the cohomology groups of $\left(\Omega^{0, *}(E), \bar{\partial}_{A}\right)$, given the above decay conventions, with the sheaf cohomology groups $H^{*}(R, \mathcal{E})$. There are two cases. When $\delta_{0} \neq 0$, the connection $A$ used over $R^{o}$ does not extend over $\Sigma_{+}$, but rather it satisfies the hypotheses of Corollary 9.11, so this corollary provides the requisite identification. When $\delta=0, \Omega^{0, *}(E)$ maps to the complex extended by $\Omega^{0, *}\left(\Sigma_{-}, E_{0}\right), \Omega^{0, *}\left(\Sigma_{+},\left\lfloor\frac{K}{2}\right\rfloor\right)$, with quotient the complex
$$\Omega^{0,0}\left(\Sigma_{+},\left\lfloor\frac{K}{2}\right\rfloor\right) \xrightarrow{\bar{\partial}_{B}} \Omega^{0,1}\left(\Sigma_{+},\left\lfloor\frac{K}{2}\right\rfloor\right) .$$
But the cohomology groups of this complex must vanish by the non-degeneracy hypothesis on $\mathfrak{J}(E)$ (see Proposition 5.16).

Putting together the above facts, we see that in either case, the cohomology groups
$$H^{*}\left(C_{s w}^{*}, d_{s w}^{*}\right) \cong\left\{\begin{array}{cl}
\mathbb{C} \oplus H^{0}\left(\mathcal{E} / \alpha \mathcal{O}_{R}\right) & *=0 \\
H^{1}\left(\mathcal{E} / \alpha \mathcal{O}_{R}\right) & *=1 \\
0 & \text { otherwise }
\end{array}\right.$$
The theorem then follows. \(\square\)

\section*{11. Resolving Sheaves over Orbifold Singularities.}

Given any two relatively prime integers with $0<q<p$, let $a \in \mathbb{Z} / p \mathbb{Z}$ act on $\mathbb{C}^{2}$ by
$$a \times(w, z)=\left(\zeta^{a} w, \zeta^{q a} z\right),$$
where $\zeta$ is a primitive $p^{\text {th }}$ root of unity. Topologically, the quotient
$$C_{p, q}=\mathbb{C}^{2} /(\mathbb{Z} / p \mathbb{Z})$$
is a cone on a Lens space of type ( $p, q$ ).
This quotient has the structure of a complex two-dimensional orbifold. Its (algebraic) coordinate ring $\mathbb{A}\left[C_{p, q}\right]$ is given by the subring
$$\mathbb{C}[w, z]^{\mathbb{Z} / p \mathbb{Z}} \subset \mathbb{C}[w, z]$$
of algebraic functions on $\mathbb{C}^{2}$ which are invariant under the action of $\mathbb{Z} / p \mathbb{Z}$; i.e. those functions $f(w, z)$ for which
$$f(w, z)=f\left(\zeta w, \zeta^{q} z\right) .$$
The variety $C_{p, q}$ inherits $p$ distinct orbifold sheaves $\left\{\mathcal{O}_{j}\right\}_{j=0}^{p-1}$, consisting of those functions $f(w, z)$ on $\mathbb{C}^{2}$ for which
$$f\left(\zeta w, \zeta^{q} z\right)=\zeta^{j} f(w, z) .$$
Equivalently, the representations $\left\{\rho_{j}\right\}_{j=0}^{p-1}$ of $\mathbb{Z} / p \mathbb{Z}$ on the one-dimensional complex vector space $\mathbb{C}$ given by
$$\rho_{j}(a)(v)=\zeta^{a j} v,$$
along with the above action of $\mathbb{Z} / p \mathbb{Z}$ on $\mathbb{C}^{2}$, give us $p$ distinct $\mathbb{Z} / p \mathbb{Z}$ -equivariant line bundles over $\mathbb{C}^{2}$, which we will denote by $\left\{\mathcal{L}_{j}\right\}_{j=0}^{p-1}$. Now, the sections of $\mathcal{O}_{j}$ can be thought of as the $\mathbb{Z} / p \mathbb{Z}$-equivariant sections of the line bundle $\mathcal{L}_{j}$.

Since the action of $\mathbb{Z} / p \mathbb{Z}$ on $\mathbb{C}^{2}$ is free away from the origin, the equivariant line bundle $\mathcal{L}_{j}$ descends to give an honest line bundle on $C_{p, q}-[0,0]$ so that the sheaves $\left.\mathcal{O}_{j}\right|_{C_{p, q}-[0,0]}$ are all locally free. Indeed, these $p$ line bundles are all distinct topological bundles over $C_{p, q}-[0,0]$, representing the $p$ elements in
$$H^{2}\left(C_{p, q}-[0,0], \mathbb{Z}\right) \cong H^{2}\left(L_{p, q}, \mathbb{Z}\right) \cong \mathbb{Z} / p \mathbb{Z} .$$
The sheaves $\mathcal{O}_{j}$ (for $j \neq 0$ ) do not extend over [0, 0] as locally free sheaves (as their first Chern classes do not extend). However, there is a canonical way to extend these sheaves over the resolution $\widehat{C}_{p, q}$. Describing this procedure is the goal of this section.

First, recall that the minimal resolution
$$r: \widehat{C}_{p, q} \rightarrow C_{p, q}$$
is the map which contracts the chain of two-spheres in $\widehat{C}_{p, q}$, labeled $\left\{S_{i}\right\}_{i=1}^{m}$. Here, $m$ is the number of terms in the Hirzebruch-Jung continued fraction expansion of $p / q$ :
$$\frac{p}{q}=a_{1}-\frac{1}{a_{2}-\frac{1}{\ddots-\frac{1}{a_{m}}}}=\left\langle a_{1}, \ldots, a_{m}\right\rangle$$
and $S_{i}$ has self-intersection number $-a_{i}$ (see Section 3). Pulling back the orbifold sheaf $\mathcal{O}_{j}$ via $r$ (as a coherent sheaf), we obtain a coherent sheaf $r^{*}\left(\mathcal{O}_{j}\right)$ over $\widehat{C}_{p, q}$.

In order to give a more concrete description of this sheaf, one which is useful in calculations, we must first introduce some terminology. Suppose $\mathbf{w}$ is in a monoid generated by elements $\mathbf{v}_{1}, \ldots, \mathbf{v}_{m}$. Then the $m$-tuple of non-negative integers $\left(x_{1}, \ldots, x_{m}\right)$ is called a maximal decomposition of $\mathbf{w}$ in terms of $\left(\mathbf{v}_{1}, \ldots, \mathbf{v}_{m}\right)$ if it is maximal, in the dictionary ordering, among all $m$-tuples $\left(y_{1}, \ldots, y_{m}\right)$ of non-negative integers which satisfy
$$\mathbf{w}=\sum_{i} y_{i} \mathbf{v}_{i} .$$
In particular, if $\left(d_{1}, \ldots, d_{m}\right)$ is an ordered $m$-tuple of natural numbers, and $j$ is a non-negative integer, then the minimal decomposition of $j$ with respect to $\left(d_{1}, \ldots, d_{m}\right)$ (if it exists) can be found inductively by a Euclidean algorithm letting
$$x_{1}=\left\lfloor\frac{j}{d_{1}}\right\rfloor,$$
and $\left(x_{2}, \ldots, x_{m}\right)$ be the maximal decomposition of $j-x_{1} d_{1}$ in terms of $\left(d_{2}, \ldots, d_{m}\right)$.

Proposition 11.1. For each $j=0, \ldots, p-1$, the sheaf $r^{*}\left(\mathcal{O}_{j}\right)$ is an invertible sheaf over $\widehat{C}_{p, q}$ for which the natural map
$$\mathcal{O}_{j} \rightarrow r_{*} r^{*}\left(\mathcal{O}_{j}\right) .$$
is an isomorphism. Let $\left(x_{1}, \ldots, x_{m}\right)$ be a maximal decomposition of $j$ in terms of $\left(d_{1}, \ldots, d_{m}\right)$, where $d_{i}$ is the the denominator of the Hirzebruch-Jung continued fraction $\left\langle a_{i}, a_{i+1}, \ldots, a_{m}\right\rangle$. Then, the first Chern class of the line bundle corresponding to $r^{*}\left(\mathcal{O}_{j}\right)$ is determined by
$$\left\langle c_{1}\left(r^{*}\left(\mathcal{O}_{j}\right)\right),\left[S_{i}\right]\right\rangle=x_{i},$$
where $\left[S_{i}\right]$ is the homology class of the $i^{\text {th }}$ sphere in $\widehat{C}_{p, q}$.
Thus, this proposition gives a natural correspondence between orbifold sections of the sheaf $\mathcal{O}_{j}$ over $C_{p, q}$ and sections of a line bundle (depending on $j$ ) over $\widehat{C}_{p, q}$. The result should be compared with the following theorem of Gonzalez-Sprinberg and Verdier [13] (see also [21]):

Theorem 6 (Gonzalez-Sprinberg, Verdier). Let $G$ be a finite subgroup of $S U(2)$. The resolution $\mathbb{C}^{2} / G$ is obtained by inserting a configuration of 2-spheres which are in a one-to-one correspondence with the non-trivial irreducible representations of $G$. Given a representation
$$\rho: G \rightarrow G L(V),$$
letting $\mathcal{O}_{\rho}$ denote the sheaf of orbifold sections of of the orbifold bundle
$$\mathbb{C}^{2} \times_{\{G, \rho\}} V$$
over $\mathbb{C}^{2} / G$, we can form
$$r\left(\mathcal{O}_{\rho}\right)=r^{*}\left(\mathcal{O}_{\rho}\right) / \text { Tors },$$
the quotient of the pull-back sheaf by its nilpotent elements. Then, $r\left(\mathcal{O}_{\rho}\right)$ is a locally free sheaf for which the natural map
$$\mathcal{O}_{\rho} \rightarrow r_{*}\left(r\left(\mathcal{O}_{\rho}\right)\right)$$
is an isomorphism and
$$\left\langle c_{1}(r(\rho)),\left[S_{\sigma}\right]\right\rangle=\left\{\begin{array}{ll}
1 & \text { if } \sigma=\rho \\
0 & \text { otherwise }
\end{array},\right.$$
where $S_{\sigma}$ denotes the sphere corresponding to the representation $\sigma$.
The hypotheses of our Proposition are consistent with the hypotheses of the Gonzalez-Sprinberg and Verdier theorem exactly when $q=p-1$, i.e. when $G \cong \mathbb{Z} / p \mathbb{Z}$ is given by matrices of the form
$$\left(\begin{array}{cc}
\zeta^{a} & 0 \\
0 & \zeta^{-a}
\end{array}\right)$$
with $a \in \mathbb{Z} / p \mathbb{Z}$. There are $p-1$ terms in the continued fraction expansion of $p / p-1$, and the denominators are $(p-1, p-2, \ldots, 1)$, so that the maximal expansion of any $0<j<p$ is given by coefficients $x_{i}=\delta_{i, p-j}$ (Kronecker delta). Thus, in this special case, both Theorem 6 and Proposition 11.1 are in agreement.

The proof of Proposition 11.1 requires a concrete description of $\widehat{C}_{p, q}$, which is based on elements of the theory of toric varieties (see [10]). We set up the notation presently.

The map
$$\chi: \mathbb{Z}^{2} \mapsto \mathbb{C}\left[w, z, w^{-1}, z^{-1}\right]$$
from the standard lattice to the Laurent polynomials
$$\chi(i, j)=w^{i} z^{j}$$
sets up a correspondence between additive sub-monoids of $\mathbb{Z}^{2}$ and subrings of $\mathbb{C}\left[w, z, w^{-1}, z^{-1}\right]$. Under this correspondence, the lattice $\Lambda \subset \mathbb{Z}^{2}$ given by
$$i+q j \equiv 0 \quad(\bmod p)$$
corresponds to the subring of $\mathbb{Z} / p \mathbb{Z}$-invariant Laurent polynomials. Moreover, the upper right quadrant of $\Lambda$,
$$\Lambda_{+}=\left\{v \in \Lambda \mid \Pi_{1}(v) \geq 0, \Pi_{2}(v) \geq 0\right\},$$
corresponds to the coordinate ring $\mathbb{A}\left[C_{p, q}\right]$. In the above expression,
$$\Pi_{\alpha}: \mathbb{Z}^{2} \rightarrow \mathbb{Z}$$
denotes the projection onto the $\alpha^{\text {th }}$ coordinate.
As in [10], the monoid $\Lambda_{-}$
$$\Lambda_{-}=\left\{v \in \Lambda \mid \Pi_{1}(v) \leq 0, \Pi_{2}(v) \geq 0\right\}$$
has a canonical generating set $\left(\mathbf{v}_{0}, \ldots, \mathbf{v}_{m+1}\right)$, arranged so that
$$-p=\Pi_{1} \mathbf{v}_{0}<\Pi_{1} \mathbf{v}_{1}<\ldots<\Pi_{1} \mathbf{v}_{m}<\Pi_{1} \mathbf{v}_{m+1}=0 .$$
Consecutive pairs of vectors $\mathbf{v}_{i}, \mathbf{v}_{i+1}$ generate the monoid of lattice points in the sector of $\Lambda$ lying between those vectors. The vectors $\mathbf{v}_{0}=(-p, 0)$, $\mathbf{v}_{m+1}=(0, p)$, and the vectors $\left\{\mathbf{v}_{1}, \ldots, \mathbf{v}_{m}\right\}$ are the lattice points appearing on the boundary of the convex hull of the set $\Lambda_{-}-\{(0,0)\}$, off the coordinate axes. This convexity forces
$$0=\Pi_{2} \mathbf{v}_{0}<\Pi_{2} \mathbf{v}_{1}<\ldots<\Pi_{2} \mathbf{v}_{m}<\Pi_{2} \mathbf{v}_{m+1}=p .$$
These vectors satisfy the relations
$$\mathbf{v}_{i-1}+\mathbf{v}_{i+1}=a_{i} \mathbf{v}_{i},$$
where the $a_{i}$ appear in the continued fraction expansion in Equation 11.1. Moreover,
$$\Pi_{1} \mathbf{v}_{i}=-d_{i},$$
where the $d_{0}=p, d_{m+1}=0$, and $d_{i}$ for $i=1, \ldots, m$ are as in the statement of the Proposition 11.1. (Similarly, for $i=1, \ldots, m, \Pi_{2} \mathbf{v}_{i}$ is the denominator of the Hirzebruch-Jung continued fraction expansion of $\left\langle a_{i}, \ldots, a_{1}\right\rangle$.) Equations 11.4, and 11.1 (along with the statement about $\Pi_{2} \mathbf{v}_{i}$ ) are neatly summarized by the statement that, for each $i=1, \ldots, m$, there is a matrix $A_{i} \in \operatorname{Sl}_{2}(\mathbf{Z})$ with $A_{i} \mathbf{v}_{i-1}=\mathbf{v}_{i}$, and $A_{i} \mathbf{v}_{i}=\mathbf{v}_{i+1}$.

The ordering properties expressed in Inequalities 11.2 and 11.3 give us a constructive technique for giving the maximal decomposition of a vector $\mathbf{w} \in \Lambda_{-}$.

Lemma 11.2. Suppose $\mathrm{w} \in \Lambda_{-}$, and $\left(x_{0}, \ldots, x_{m}\right)$ is the maximal decomposition of $\Pi_{1} \mathbf{w}$ with respect to $\left(d_{0}, \ldots, d_{m}\right)$. Then, letting
$$x_{m+1}=\frac{\Pi_{2}\left(\mathrm{w}-\sum_{i=0}^{m} x_{i} \mathrm{v}_{i}\right)}{p},$$
the $\left(x_{0}, \ldots, x_{m+1}\right)$ form the maximal decomposition of the $\mathbf{w}$ with respect to the generators $\left(\mathbf{v}_{0}, \ldots, \mathbf{v}_{m+1}\right)$. In particular, we have for the maximal decomposition
$$\mathbf{v}=\sum_{i} x_{i} \mathbf{v}_{i}$$
that
$$d_{i}>\sum_{j>i} x_{j} d_{j} .$$

Proof. Letting $\mathbf{u}=\sum_{i=0}^{m} x_{i} \mathbf{v}_{i}, \mathbf{u} \in \Lambda_{-}$has $\Pi_{1} \mathbf{u}=\Pi_{1} \mathbf{w}$ by Equation 11.5. The maximality of the $x_{i}$, combined with the ordering property in Inequality 11.3 ensure that u has minimal $\Pi_{2}$ among all vectors in $\Lambda \cap \Pi_{1}{ }^{-1} \Pi_{1} \mathbf{w}$. This implies the first statement.

The inequality 11.6 follows immediately from the construction of maximal decompositions of natural numbers. \(\square\)

If $\mathbf{v}, \mathbf{w} \in \Lambda_{-}$, we say that $\mathbf{v}$ precedes $\mathbf{w}$, denoted $\mathbf{v} \prec \mathbf{w}$, if the maximal decomposition of $\mathbf{v}$ with respect to the generators $\left(\mathbf{v}_{0}, \ldots, \mathbf{v}_{m}\right)$ precedes that of $\mathbf{w}$ in the dictionary ordering.

Corollary 11.3. If $\mathbf{v}, \mathbf{w} \in \Lambda_{-}$and $\Pi_{1} \mathbf{w}<\Pi_{1} \mathbf{v}$ then there is a $\lambda \in \Lambda_{+}$and $\mathbf{u} \in \Lambda_{-}$with $\mathbf{u} \preceq \mathbf{w}$ such that
$$\mathbf{v}=\mathbf{u}+\lambda .$$

Proof. Let $\mathbf{v}=\sum b_{i} \mathbf{v}_{i}, \mathbf{w}=\sum c_{i} \mathbf{v}_{i}$ be the maximal decompositions. We might as well assume $\mathbf{v} \npreceq \mathbf{w}$ (otherwise the conclusion is satisfied for $\lambda=0$ ). Thus, there must be an integer $k$ with $b_{k}>c_{k}$. Let $\ell$ be the integer with the property that for all $j<\ell, b_{j}=c_{j}$, and $b_{\ell} \neq c_{\ell}$.
---
retention_scope: session
part: 2
total_parts: 3
---

[Part 2/3 of: Surface group representations with maximal Toledo invariant]

Given now $(a, b) \in \check{S}^{(2)}$, let as in [14, § 5.1]
$$\mathcal{O}_{a, b} \subset \mathbf{G} / \mathbf{Q}$$
be the Zariski open subset on which the map
$$\begin{aligned}
p_{a, b}: \mathcal{O}_{a, b} & \rightarrow \mathbb{C}^{\times} \mathbb{1} \backslash A^{\times} \\
x & \mapsto\langle\langle a, b, x\rangle\rangle_{\mathbb{C}}
\end{aligned}$$
is defined. We have then (see [14, Lemma 5.1]) that if for some $m \in$ $\mathbb{Z} \backslash\{0\}$ the map
$$\begin{aligned}
\mathcal{O}_{a, b} & \rightarrow \mathbb{C}^{\times} \mathbb{1} \backslash A^{\times} \\
x & \mapsto p_{a, b}(x)^{m}
\end{aligned}$$
is constant, then $\mathcal{X}$ is of tube type. Now we apply (4.2) in Corollary 4.4 to get that if $\rho: \Gamma \rightarrow G=\mathbf{G}(\mathbb{R})^{\circ}$ is maximal, then
$$\beta_{\check{S}}(\varphi(x), \varphi(y), \varphi(z))= \pm \frac{\mathrm{r}_{\mathcal{X}}}{2}$$
for almost every $(x, y, z)$, which implies that
$$\langle\langle\varphi(x), \varphi(y), \varphi(z)\rangle\rangle^{2} \equiv 1 \quad \bmod \mathbb{R}^{\times} .$$
In particular, fix $x, y$ such that $(\varphi(x), \varphi(y)) \in \check{S}^{(2)}$ and such that (4.5) holds for almost all $z \in \partial \mathbb{D}$ : letting $E \subset \partial \mathbb{D}$ be this set of full measure, we may assume that $E$ is $\Gamma$-invariant and $\varphi(E) \subset \mathcal{O}_{a, b}$ where $a=\varphi(x)$ and $b=\varphi(y)$. But $\varphi(E)$ being $\rho(\Gamma)$-invariant is Zariski dense in G/Q and hence Zariski dense in the open set $\mathcal{O}_{a, b}$; since the map $x \mapsto p_{a, b}(x)^{2}$ is constant on $\varphi(E)$ it is so on $\mathcal{O}_{a, b}$, which implies that $\mathcal{X}$ is of tube type.
4.3. The image of $\rho$ is discrete. Under the hypothesis of Theorem 4.1, we know now that $\mathcal{X}$ is of tube type. Then the generalized Maslov cocycle $\beta_{\check{S}}$ takes on $\check{S}{ }^{(3)}$ exactly $\mathrm{r}_{\mathcal{X}}+1$ values, namely
$$\left\{-\frac{\mathrm{r}_{\mathcal{X}}}{2},-\frac{\mathrm{r}_{\mathcal{X}}}{2}+1, \ldots, \frac{\mathrm{r}_{\mathcal{X}}}{2}-1, \frac{\mathrm{r}_{\mathcal{X}}}{2}\right\}$$
so that
$$\check{S}^{(3)}=\cup_{i=0}^{\mathrm{r}_{\mathcal{X}}} \mathcal{O}_{-\mathrm{r}_{\mathcal{X}}+2 i},$$
where $\mathcal{O}_{-\mathrm{r}_{\mathcal{X}}+2 i}$ is the preimage via $\beta_{\check{S}}$ of $\frac{\mathrm{r} \mathcal{X}}{2}+i$, which incidentally is open since $\beta_{\check{S}}$ is continuous on $\check{S}^{(3)}$ (see [14, Corollary 3.7]). With the
above notations, it follows from (4.2) in Corollary 4.4 that
$$(\varphi(x), \varphi(y), \varphi(z)) \in \mathcal{O}_{-\mathrm{r}_{\mathcal{X}}} \cup \mathcal{O}_{\mathrm{r}_{\mathcal{X}}}$$
for almost all $(x, y, z) \in(\partial \mathbb{D})^{3}$. Let us now denote by $\operatorname{Ess} \operatorname{Im} \varphi \subset \check{S}$ the essential image of $\varphi$, that is the support of the pushforward $\varphi_{*}(\lambda)$ of the round measure $\lambda$ on $\partial \mathbb{D}$. Then $\operatorname{Ess} \operatorname{Im} \varphi$ is closed and $\rho(\Gamma)$-invariant. It follows then from (4.7) that
$$(\operatorname{Ess} \operatorname{Im} \varphi)^{3} \subset \overline{\mathcal{O}_{-\mathrm{r}_{\mathcal{X}}}} \cup \overline{\mathcal{O}_{\mathrm{r}_{\mathcal{X}}}},$$
where the closure on the right hand side is taken in $\check{S}^{3}$. There are now two cases. Either $\mathrm{r}_{\mathcal{X}}=1, \mathcal{X}=\mathbb{D}, G=\mathrm{PU}(1,1)$, which is the case treated in [11]; or $\mathrm{r}_{\mathcal{X}} \geq 2$, and then $\overline{\mathcal{O}_{-\mathrm{r}_{\mathcal{X}}}} \cup \overline{\mathcal{O}_{\mathrm{r}_{\mathcal{X}}}}$ is not the whole of $\check{S}^{(3)}$, since its complement contains at least $\mathcal{O}_{-\mathrm{r}_{\mathcal{X}}+2}$; thus $(\operatorname{Ess} \operatorname{Im} \varphi)^{3} \neq \check{S}^{3}$ and, since $(\operatorname{Ess} \operatorname{Im} \varphi)^{3}$ is $\rho(\Gamma)^{3}$-invariant closed and $\check{S}$ is $G$-homogeneous, this implies that $\rho(\Gamma)$ is not dense in $G$. Since a Zariski dense subgroup of $G$ is either discrete or dense, we have that $\rho(\Gamma)$ is discrete.
4.4. The representation $\rho$ is injective. Assume that
$$\operatorname{ker}(\rho) \nless \mathcal{Z}(\Gamma) .$$
Then it is easy to see that there is $\gamma \in \operatorname{ker} \rho$ of infinite order, so that we may choose a nonempty open interval $I \subset \partial \mathbb{D}$ such that $I, \gamma I, \gamma^{2} I$ are pairwise disjoint and positively oriented, that is $\beta_{\mathbb{D}}(x, y, z)=\frac{1}{2}$ for all $(x, y, z) \in I \times \gamma I \times \gamma^{2} I$. Now choose three open nonvoid intervals $I_{1}, I_{2}, I_{3}$ in $I$ which are pairwise disjoint and positively oriented. Then it follows from (4.2) in Corollary 4.4 that
$$E_{1}:=\left\{(x, y, z) \in I_{3} \times \gamma I_{2} \times \gamma^{2} I_{1}: \beta_{\check{S}}(\varphi(x), \varphi(y), \varphi(z))=\frac{\mathrm{r}_{\mathcal{X}}}{2}\right\}$$
is of full measure in $I_{3} \times \gamma I_{2} \times \gamma^{2} I_{1}$, while
$$E_{2}:=\left\{(x, y, z) \in I_{3} \times I_{2} \times I_{1}: \beta_{\check{S}}(\varphi(x), \varphi(y), \varphi(z))=-\frac{\mathrm{r}_{\mathcal{X}}}{2}\right\}$$
is of full measure in $I_{3} \times I_{2} \times I_{1}$. Thus
$$E_{1}^{\prime}:=\left\{(x, y, z) \in E_{1}:\left(x, \gamma^{-1} y, \gamma^{-2} z\right) \in E_{2}\right\}$$
is of full measure; using the almost everywhere equivariance of $\varphi$ and the assumption that $\rho(\gamma)=\mathrm{Id}$, we conclude that for almost every $(x, y, z) \in E_{1}^{\prime}$
$$\frac{\mathrm{r}_{\mathcal{X}}}{2}=\beta_{\check{S}}(\varphi(x), \varphi(y), \varphi(z))=\beta_{\check{S}}\left(\varphi(x), \varphi\left(\gamma^{-1} y\right), \varphi\left(\gamma^{-2} z\right)\right)=-\frac{\mathrm{r}_{\mathcal{X}}}{2},$$
which is a contradiction. This shows that $\operatorname{ker} \rho \subset \mathcal{Z}(\Gamma)$ and completes the proof of Theorem 4.1.

\section*{5. Regularity properties of the boundary map: the Zariski dense case}

In this section we generalize a technique from [7] to study the boundary map $\varphi: \partial \mathbb{D} \rightarrow \check{S}$ associated to a maximal representation $\rho: \Gamma \rightarrow$ $G=\mathbf{G}(\mathbb{R})^{\circ}$ with Zariski dense image and establish the existence of strictly equivariant maps with additional regularity properties. This relies in an essential way on the fact established in Theorem 4.1 asserting that, in the situation described above, the symmetric space $\mathcal{X}$ associated to $G$ is irreducible and of tube type.

Theorem 5.1. Let $\Gamma$ be a lattice in a finite connected covering of $\operatorname{PU}(1,1)$ and let $\rho: \Gamma \rightarrow G$ a maximal representation with Zariski dense image. Then there are two Borel maps
$$\varphi_{ \pm}: \partial \mathbb{D} \rightarrow \check{S}$$
with the following properties:
\begin{itemize}
\item[(1)] $\varphi_{+}$and $\varphi_{-}$are strictly $\rho$-equivariant;
\item[(2)] $\varphi_{-}$is left continuous and $\varphi_{+}$is right continuous;
\item[(3)] for every $x \neq y, \varphi_{\epsilon}(x)$ is transverse to $\varphi_{\delta}(y)$ for all $\epsilon, \delta \in\{+,-\}$;
\item[(4)] for all $x, y, z \in \partial \mathbb{D}$,
$$\beta_{\check{S}}\left(\varphi_{\epsilon}(x), \varphi_{\delta}(y), \varphi_{\eta}(z)\right)=\mathrm{r}_{\mathcal{X}} \beta_{\partial \mathbb{D}}(x, y, z),$$
for all $\epsilon, \delta, \eta \in\{+,-\}$.
\end{itemize}
Moreover $\varphi_{+}$and $\varphi_{-}$are the unique maps satisfying (1) and (2).
5.1. General properties of boundary maps. Let $\Gamma<L$ be a lattice in a connected finite covering $L$ of $\operatorname{PU}(1,1)$ as above, $\mathbf{G}$ a connected semisimple group, P a parabolic subgroup, both defined over $\mathbb{R}, G=$ $\mathbf{G}(\mathbb{R}), P=\mathbf{P}(\mathbb{R}), \rho: \Gamma \rightarrow G$ a homomorphism and $\lambda$ the round measure on $\partial \mathbb{D}$. If $\varphi: \partial \mathbb{D} \rightarrow G / P$ is a $\rho$-equivariant measurable map and $\rho$ has Zariski dense image, one sees immediately that the image of $\varphi$ cannot be contained in a proper algebraic subset. The following proposition is a strengthening of this statement, showing that from the point of view of the round measure, the essential image of $\varphi$ meets any proper algebraic subset in a set of measure zero. Namely:

Proposition 5.2. If $\mathbf{V} \subset \mathbf{G} / \mathbf{P}$ is any proper Zariski closed subset defined over $\mathbb{R}$, then
$$\lambda\left(\varphi^{-1}(\mathbf{V}(\mathbb{R}))\right)=0 .$$

This will follow from the following two lemmas.
Lemma 5.3. [36] If $A \subset \partial \mathbb{D}$ is a set of positive measure, then there exists a sequence $\left\{\gamma_{n}\right\}_{n=1}^{\infty}$ in $\Gamma$ such that $\lim _{n \rightarrow \infty} \lambda\left(\gamma_{n} A\right)=1$.

Lemma 5.4. Let $\mathbf{V} \subset \mathbf{G} / \mathbf{P}$ be a proper Zariski closed subset defined over $\mathbb{R}$ and $\left\{g_{n}\right\}_{n=1}^{\infty}$ a sequence in $G$. Then there exists a proper Zariski closed subset $\mathbf{W} \subset \mathbf{G} / \mathbf{P}$ defined over $\mathbb{R}$ and a subsequence $\left\{g_{n_{k}}\right\}_{k=1}^{\infty}$ such that for every $\epsilon>0$ there exists $K>0$ such that for all $k \geq K$
$$g_{n_{k}} \mathbf{V}(\mathbb{R}) \subset \mathcal{N}_{\epsilon}(\mathbf{W}(\mathbb{R})),$$
where $\mathcal{N}_{\epsilon}$ denotes the $\epsilon$-neighborhood for some fixed distance on $G / P$.
Proof. Passing to a subsequence $\left\{g_{n_{k}}\right\}$ we may assume that, if $V:=$ $\mathbf{V}(\mathbb{R}), g_{n_{k}} V$ converges to a compact set $F \subset G / P$ in the Gromov-Hausdorff topology. It suffices then to show that $F$ is not Zariski dense in $\mathbf{G} / \mathbf{P}$. To this end, let $I(\mathbf{V}) \subset \mathbb{C}[\mathbf{G} / \mathbf{P}]$ be the defining ideal and pick $d \geq 1$ such that the homogeneous component $I(\mathbf{V})_{d}(\mathbb{R}) \subset \mathbb{C}[\mathbf{G} / \mathbf{P}]_{d}(\mathbb{R})$ is nonzero. Let $\ell:=\operatorname{dim} I(\mathbf{V})_{d}(\mathbb{R})$; then we may assume that the sequence $g_{n_{k}} I(\mathbf{V})_{d}(\mathbb{R})$ converges to a point $E$ in the Grassmannian $\operatorname{Gr}_{\ell}\left(\mathbb{C}[\mathbf{G} / \mathbf{P}]_{d}(\mathbb{R})\right)$. In particular, given $p \in E, p \neq 0$, there exists $p_{n} \in g_{n_{k}} I(\mathbf{V})_{d}(\mathbb{R})$ with $p_{n} \rightarrow p$. It is then not difficult to show that $p$ vanishes on $F$ and one can take $\mathbf{W} \subset \mathbf{G} / \mathbf{P}$ to be the Zariski closure of $F$. \(\square\)

Proof of Proposition 5.2. Let $V:=\mathbf{V}(\mathbb{R})$ and $A:=\{x \in \partial \mathbb{D}: \varphi(x) \in$ $V\}$. Assume that $\lambda(A)>0$ and pick a sequence $\left\{\gamma_{n}\right\}_{n=1}^{\infty}$ in $\Gamma$ as in Lemma 5.3 such that
$$\lambda\left(\gamma_{n} A\right) \rightarrow 1 .$$
Passing to a subsequence, let $\mathbf{W} \subset \mathbf{G} / \mathbf{P}$ be the proper Zariski closed subset given by Lemma 5.4. For every $m \geq 1$, let $N(m)$ be such that for all $n \geq N(m)$
$$\rho\left(\gamma_{n}\right) V \subset \mathcal{N}_{1 / m}(W),$$
where $W:=\mathbf{W}(\mathbb{R})$. Setting $E_{N}:=\cup_{n=N}^{\infty} \gamma_{n} A$, we have thus
$$\varphi\left(E_{N(m)}\right) \subset \mathcal{N}_{1 / m}(W) .$$
But now $E_{N(m)} \subset \partial \mathbb{D}$ is a set of full measure and so is $E:=\cap_{m \geq 1} E_{N(m)}$, which, by (5.1), implies now that $\varphi(E) \subset W$. This implies that
$$\operatorname{Ess} \operatorname{Im}(\varphi) \subset W \subset \mathbf{W} \subset \mathbf{G} / \mathbf{P}$$
and contradicts the Zariski density of $\rho(\Gamma)$ since $\operatorname{Ess} \operatorname{Im}(\varphi)$ is $\rho(\Gamma)$ -invariant. \(\square\)
5.2. Exploiting maximality. Let now $\rho: \Gamma \rightarrow G$ be a maximal representation with Zariski dense image and $\varphi: \partial \mathbb{D} \rightarrow \check{S}$ be the $\rho$ -equivariant measurable map given by Theorem 4.2. Having introduced the essential image $\operatorname{Ess} \operatorname{Im}(\varphi) \subset \check{S}$, we will now study the essential graph $\operatorname{Ess} \operatorname{Gr}(\varphi) \subset \partial \mathbb{D} \times \check{S}$ of $\varphi$ defined as the support of the pushforward of the round measure $\lambda$ on $\partial \mathbb{D}$ under the map
$$\begin{aligned}
\partial \mathbb{D} & \rightarrow \partial \mathbb{D} \times \check{S} \\
x & \mapsto(x, \varphi(x)) .
\end{aligned}$$
For this we will use (4.2) in Corollary 4.4 in an essential way. The following properties of the generalized Maslov cocycle $\beta_{\check{S}}$ follow from [16, 21, 19]:

Lemma 5.5. (1) $\beta_{\check{S}}: \check{S}^{3} \rightarrow\left\{-\frac{\mathrm{r} \mathcal{X}}{2}\right\}+\mathbb{Z}$ is a $G$-invariant cocycle;
\begin{itemize}
\item[(2)] $\left|\beta_{\check{S}}(x, y, z)\right| \leq \frac{\mathrm{r}_{\mathcal{X}}}{2}$;
\item[(3)] if $\beta_{\check{S}}(x, y, z)=\frac{\mathrm{r}_{\mathcal{X}}}{2}$ then $x, y, z$ are pairwise transverse;
\item[(4)] $\check{S}^{(3)}=\sqcup_{i=0}^{\mathrm{r}_{\mathcal{X}}} \mathcal{O}_{-\mathrm{r}_{\mathcal{X}}+2 i}$, where $\mathcal{O}_{-\mathrm{r}_{\mathcal{X}}+2 i}$ is open in $\check{S}^{3}$ and $\beta_{\check{S}}$ takes on the value $-\frac{\mathrm{r}_{\mathcal{X}}}{2}+i$ on $\mathcal{O}_{-\mathrm{r}_{\mathcal{X}}+2 i}$;
\item[(5)] if $x,\left\{x_{n}\right\},\left\{x_{n}^{\prime}\right\} \in \check{S}, \lim _{n \rightarrow \infty} x_{n}=x$ and $\beta_{\check{S}}\left(x, x_{n}^{\prime}, x_{n}\right)=\frac{\mathrm{r}_{\mathcal{X}}}{2}$, then $\lim _{n \rightarrow \infty} x_{n}^{\prime}=x$.
\end{itemize}

Finally, for $x \in \check{S}=G / Q \subset \mathbf{G} / \mathbf{Q}$, let $\mathbf{V}_{x} \subset \mathbf{G} / \mathbf{Q}$ be the proper Zariski closed $\mathbb{R}$-subset of all points $y \in \mathbf{G} / \mathbf{Q}$ which are not transverse to $x$, so that $V_{x}:=\mathbf{V}_{x}(\mathbb{R})$ is the set of points in $\check{S}$ which are not transverse to $x$.

Lemma 5.6. Let $\left(x_{1}, f_{1}\right),\left(x_{2}, f_{2}\right),\left(x_{3}, f_{3}\right)$ be points in $\operatorname{Ess} \operatorname{Gr}(\varphi)$ so that $x_{1}, x_{2}, x_{3}$ are pairwise distinct and $f_{1}, f_{2}, f_{3}$ are pairwise transverse. Then
$$\beta_{\check{S}}\left(f_{1}, f_{2}, f_{3}\right)=\mathrm{r}_{\mathcal{X}} \beta_{\partial \mathbb{D}}\left(x_{1}, x_{2}, x_{3}\right) .$$
Proof. Let $I_{i}, i=1,2,3$ be pairwise disjoint open intervals containing $x_{i}$ such that for all $y_{i} \in I_{i}$
$$\beta_{\partial \mathbb{D}}\left(y_{1}, y_{2}, y_{3}\right)=\beta_{\partial \mathbb{D}}\left(x_{1}, x_{2}, x_{3}\right) .$$
Let $U_{i}, i=1,2,3$ be neighborhoods of $f_{i}$ such that $U_{1} \times U_{2} \times U_{3} \subset \check{S}^{(3)}$. Then
$$A_{i}=\left\{x \in I_{i}: \varphi(x) \in U_{i}\right\}$$
is of positive measure and hence it follows from (4.2) in Corollary 4.4 that for almost every $\left(y_{1}, y_{2}, y_{3}\right) \in A_{1} \times A_{2} \times A_{3}$,
$$\beta_{\check{S}}\left(\varphi\left(y_{1}\right), \varphi\left(y_{2}\right), \varphi\left(y_{3}\right)\right)=\mathrm{r}_{\mathcal{X}} \beta_{\partial \mathbb{D}}\left(y_{1}, y_{2}, y_{3}\right)=\mathrm{r}_{\mathcal{X}} \beta_{\partial \mathbb{D}}\left(x_{1}, x_{2}, x_{3}\right) .$$

Thus setting $\varepsilon=2 \beta_{\partial \mathbb{D}}\left(x_{1}, x_{2}, x_{3}\right) \in\{ \pm 1\}$, we have for almost every $\left(y_{1}, y_{2}, y_{3}\right) \in A_{1} \times A_{2} \times A_{3}$, that
$$\left(\varphi\left(y_{1}\right), \varphi\left(y_{2}\right), \varphi\left(y_{3}\right)\right) \in\left(U_{1} \times U_{2} \times U_{3}\right) \cap \mathcal{O}_{\varepsilon \mathrm{r}_{\mathcal{X}}},$$
which implies, since the neighborhood $U_{i}$ can be chosen arbitrarily small, that $\left(f_{1}, f_{2}, f_{3}\right) \in \overline{\mathcal{O}_{\varepsilon \mathrm{r}_{\mathcal{X}}}}$. But
$$\overline{\mathcal{O}_{\varepsilon \mathrm{r}_{\mathcal{X}}}} \cap \check{S}^{(3)}=\overline{\mathcal{O}_{\varepsilon \mathrm{r}_{\mathcal{X}}}} \cap\left(\cup_{i=0}^{\mathrm{r}_{\mathcal{X}}} \mathcal{O}_{-\mathrm{r}_{\mathcal{X}}+2 i}\right)=\mathcal{O}_{\varepsilon \mathrm{r}_{\mathcal{X}}}$$
which, together with the assumption that $\left(f_{1}, f_{2}, f_{3}\right) \in \check{S}^{(3)}$, implies that $\left(f_{1}, f_{2}, f_{3}\right) \in \mathcal{O}_{\varepsilon \mathrm{r}_{\mathcal{X}}}$ and hence proves the lemma. \(\square\)

Lemma 5.7. Let $\left(x_{1}, f_{2}\right),\left(x_{2}, f_{2}\right) \in \operatorname{Ess} \operatorname{Gr}(\varphi)$ with $x_{1} \neq x_{2}$. Then $f_{1}$ is transverse to $f_{2}$.

Proof. For $x, y \in \partial \mathbb{D}$, let
$$((x, y)):=\left\{z \in \partial \mathbb{D}: \beta_{\partial \mathbb{D}}(x, z, y)=\frac{1}{2}\right\} .$$
We will use the obvious fact that for almost every $x \in \partial \mathbb{D},(x, \varphi(x)) \in$ Ess $\operatorname{Gr}(\varphi)$. Using Proposition 5.2, we can find $a \in\left(\left(x_{1}, x_{2}\right)\right)$ such that $(a, \varphi(a)) \in \operatorname{Ess~} \operatorname{Gr}(\varphi)$ and $\varphi(a) \notin V_{f_{1}} \cup V_{f_{2}}$, that is $\varphi(a)$ is transverse to $f_{1}$ and $f_{2}$. Then by the same argument, we can find $b \in\left(\left(x_{2}, x_{1}\right)\right)$ such that $(b, \varphi(b)) \in \operatorname{Ess} \operatorname{Gr}(\varphi)$, and $\varphi(b)$ is transverse to $f_{1}, f_{2}$ and $\varphi(a)$. Applying the cocycle property of $\beta_{\check{S}}$ and Lemma 5.6, we obtain
$$\begin{aligned}
0= & \beta_{\check{S}}\left(\varphi(a), f_{2}, \varphi(b)\right)-\beta_{\check{S}}\left(f_{1}, f_{2}, \varphi(b)\right) \\
& +\beta_{\check{S}}\left(f_{1}, \varphi(a), \varphi(b)\right)-\beta_{\check{S}}\left(f_{1}, \varphi(a), f_{2}\right) \\
= & \frac{\mathrm{r}_{\mathcal{X}}}{2}-\beta_{\check{S}}\left(f_{1}, f_{2}, \varphi(b)\right)+\frac{\mathrm{r}_{\mathcal{X}}}{2}-\beta_{\check{S}}\left(f_{1}, \varphi(a), f_{2}\right),
\end{aligned}$$
which, together with Lemma 5.5(2) implies that $\beta_{\check{S}}\left(f_{1}, f_{2}, \varphi(b)\right)=\frac{\mathrm{r}_{\mathcal{X}}}{2}$; using Lemma 5.5(3) we conclude that $f_{1}$ and $f_{2}$ are transverse. \(\square\)

For a subset $A \subset \partial \mathbb{D}$, let $F_{A}=\{f \in \check{S}$ : there exists $x \in A$ such that $(x, f) \in \operatorname{Ess} \operatorname{Gr}(\varphi)\}$, and set
$$((x, y]]:=((x, y)) \cup\{y\} .$$
Lemma 5.8. Let $x \neq y$ in $\partial \mathbb{D}$. Then $\overline{F_{((x, y)]}} \cap F_{x}$ and $\overline{F_{[[y, x)]}} \cap F_{x}$ consist each of one point.

Proof. We start with two observations: first, if $A \cap B=\emptyset$, it follows from Lemma 5.7 that $F_{A} \cap F_{B}=\emptyset$; moreover, if $A$ is closed then $F_{A}$ is also closed. We prove now that $\overline{F_{((x, y)]}} \cap F_{x}$ consists of one point, the other statement can be proved analogously.

Let $f, f^{\prime} \in \overline{F_{((x, y)]}} \cap F_{x}$ and let $\left(x_{n}, f_{n}\right) \in \operatorname{Ess} \operatorname{Gr}(\varphi)$ be a sequence such that
$$x_{n} \in((x, y]], \quad \lim x_{n}=x, \text { and } \lim f_{n}=f .$$
Observe now that if $z \in((x, y]]$, writing $F_{((x, y)]}=F_{((x, z))} \cup F_{[[z, y]]}$ and taking into account that $F_{[[z, y]]}$ is closed and disjoint from $F_{x}$, we get that
$$\overline{F_{((x, y)]}} \cap F_{x}=\overline{F_{((x, z))}} \cap F_{x},$$
and hence also
$$\overline{F_{((x, y)]}} \cap F_{x}=\overline{F_{((x, z)]}} \cap F_{x}$$
for all $z \in((x, y))$. Using (5.2), we may find another sequence $\left(y_{n}, f_{n}^{\prime}\right) \in$ Ess $\operatorname{Gr}(\varphi)$ such that
$$y_{n} \in\left(\left(x, x_{n}\right)\right), \quad \lim y_{n}=x, \text { and } \lim f_{n}^{\prime}=f^{\prime} .$$
Then it follows from Lemma 5.6 and Lemma 5.7 that
$$\beta_{\check{S}}\left(f, f_{n}^{\prime}, f_{n}\right)=\mathrm{r}_{\mathcal{X}} \beta_{\partial \mathbb{D}}\left(x, y_{n}, x_{n}\right)=\frac{\mathrm{r}_{\mathcal{X}}}{2} .$$
Since $\lim f_{n}=f$, by Lemma 5.5(5), this however implies that $\lim f_{n}^{\prime}=$ $f$ and hence $f=f^{\prime}$. \(\square\)

Here is an interesting corollary about the structure of $\operatorname{Ess} \operatorname{Gr}(\varphi)$ which spells out precisely to which extent $\operatorname{Ess} \operatorname{Gr}(\varphi)$ is in general not the graph of a map.

Corollary 5.9. For every $x \in \partial \mathbb{D}, F_{x}$ consists of one or two points.
Proof. Pick $y_{-}, x, y_{+}$positively oriented in $\partial \mathbb{D}$ and $f \in F_{x}$. For every neighborhood $U$ of $f$, one of the sets
$$\begin{aligned}
& \left\{z \in\left[\left[y_{-}, x\right)\right): \varphi(z) \in U\right\} \\
& \left\{z \in\left(\left(x, y_{+}\right]\right]: \varphi(z) \in U\right\}
\end{aligned}$$
is of positive measure. This implies that
$$F_{x} \subset \overline{F_{[[y-, x)}} \cup \overline{F_{\left(\left(x, y_{+}\right]\right]}}$$
and thus
$$F_{x}=\left(\overline{F_{\left[\left[y_{-}, x\right)\right.}} \cap F_{x}\right) \cup\left(\overline{F_{\left(\left(x, y_{+}\right]\right]}} \cap F_{x}\right),$$
which, together with Lemma 5.8 proves the assertion. \(\square\)

Proof of Theorem 5.1. We use Lemma 5.8 in order to define for every $x \in \partial \mathbb{D}$
$$\begin{aligned}
& \varphi_{-}(x)=\overline{F_{\left(\left(x, y_{+}\right)\right]}} \cap F_{x} \\
& \varphi_{+}(x)=\overline{F_{\left[\left[y_{-}, x\right)\right.}} \cap F_{x}
\end{aligned}$$
where $y_{+} \neq x$ and $y_{-} \neq x$ are arbitrary. Then $\varphi_{+}$and $\varphi_{-}$are clearly respectively right and left continuous. The strict $\rho$-equivariance of $\varphi_{+}$ and $\varphi_{-}$follows from the invariance of $\operatorname{Ess} \operatorname{Gr}(\varphi) \subset \partial \mathbb{D} \times \check{S}$ under the diagonal $\Gamma$-action together with (5.3) and the fact that $\Gamma$ acts in an orientation preserving way on $\partial \mathbb{D}$.

Properties (3) and (4) are immediate consequences of Lemmas 5.6 and 5.7.

Concerning the uniqueness of $\varphi_{+}$for example, let $\psi$ be a right continuous $\rho$-equivariant map. Since the $\rho(\Gamma)$-action on $\check{S}$ is proximal, we have $\psi(x)=\varphi_{+}(x)$ for almost every $x \in \partial \mathbb{D}$ [24]. Fix $x \in \partial \mathbb{D}$ : then pick a sequence $y_{n} \in((x, y))$ such that
$$\lim y_{n}=x \text { and } \psi\left(y_{n}\right)=\varphi_{+}\left(y_{n}\right) .$$
This implies, since $\psi$ and $\varphi_{+}$are both right continuous, that $\psi(x)=$ $\varphi_{+}(x)$. \(\square\)

\section*{6. Structure of maximal representations and boundary MAPS: THE GENERAL CASE}

In this section we present the proofs of Theorem 5 and Theorem 8 in the introduction; this relies on the results obtained in §§ 4 and 5 and on the relation between maximal representations and tight homomorphisms, which were introduced in [12].

Let $G$ be a group of type (RH). We briefly recall the structure of $\mathrm{H}_{\mathrm{cb}}^{2}(G, \mathbb{R})$ in terms of simple components and the explicit form of the Gromov norm. Let $\mathcal{X}$ be the symmetric space associated to $G$; setting $G_{\mathcal{X}}:=\operatorname{Iso}(\mathcal{X})^{\circ}$ we have a canonical projection $q: G \rightarrow G_{\mathcal{X}}$ which by hypotheses has compact kernel. Let $\mathcal{X}=\mathcal{X}_{1} \times \cdots \times \mathcal{X}_{n}$ be the decomposition into irreducible factors and $p_{i}: G_{\mathcal{X}} \rightarrow G_{\mathcal{X}_{i}}$ the canonical projections. We have then the following isometric isomorphisms:
(1) $q^{*}: \mathrm{H}_{\mathrm{cb}}^{2}\left(G_{\mathcal{X}}, \mathbb{R}\right) \rightarrow \mathrm{H}_{\mathrm{cb}}^{2}(G, \mathbb{R})$;
(2) $\prod \mathrm{H}_{\mathrm{cb}}^{2}\left(G_{\mathcal{X}_{i}}, \mathbb{R}\right) \rightarrow \mathrm{H}_{\mathrm{cb}}^{2}\left(G_{\mathcal{X}}, \mathbb{R}\right),\left(\alpha_{i}\right) \mapsto \sum_{i=1}^{n} p_{i}^{*}\left(\alpha_{i}\right)$.
Defining for ease of notation $\kappa_{\mathcal{X}}^{\mathrm{b}}$ to be the bounded Kähler class of $G_{\mathcal{X}}$, let
$$\kappa_{\mathcal{X}, i}^{\mathrm{b}}:=p_{i}^{*}\left(\kappa_{\mathcal{X}_{i}}^{\mathrm{b}}\right) \quad \text { and } \quad \kappa_{G, i}^{\mathrm{b}}:=q^{*}\left(\kappa_{\mathcal{X}, i}^{\mathrm{b}}\right) .$$

Then
$$\left\{\kappa_{G, i}^{\mathrm{b}}: 1 \leq i \leq n\right\}$$
is a basis of $\mathrm{H}_{\mathrm{cb}}^{2}(G, \mathbb{R})$ and the norm of an element
$$\kappa=\sum_{i=1}^{n} \lambda_{i} \kappa_{G, i}^{\mathrm{b}}$$
equals (see [12, (2.15)]
$$\|\kappa\|=\sum_{i=1}^{n}\left|\lambda_{i}\right| \frac{\mathrm{r}_{\mathcal{X}_{i}}}{2} .$$
In the rest of this section $L$ will always denote a finite connected covering of $\mathrm{PU}(1,1)$ and $\Gamma<L$ a lattice. The following lemma is a routine verification using the Definition 3.5 of maximality and the Milnor-Wood type bounds in Corollary 3.4.

Lemma 6.1. Let $\rho: \Gamma \rightarrow G$ be a homomorpism.
\begin{itemize}
\item[(1)] If $\Gamma_{0}<\Gamma$ is a subgroup of finite index, then $\rho$ is maximal if and only if $\left.\rho\right|_{\Gamma_{0}}$ is maximal;
\item[(2)] $\rho$ is maximal if and only if $q \circ \rho: \Gamma \rightarrow G_{\mathcal{X}}$ is maximal;
\item[(3)] $\rho$ is maximal if and only if $p_{i} \circ q \circ \rho: \Gamma \rightarrow G_{\mathcal{X}_{i}}$ is maximal for every $i=1, \ldots, n$.
\end{itemize}

Recall now from [12, Definition 2.11.] that if $H$ is a locally compact group, a continuous homomorphism $\rho: H \rightarrow G$ is tight if
$$\left\|\rho^{*}\left(\kappa_{G}^{\mathrm{b}}\right)\right\|=\left\|\kappa_{G}^{\mathrm{b}}\right\| .$$
Lemma 6.2. If $\rho: \Gamma \rightarrow G$ is maximal, then it is tight.
Proof. Using that
$$\mathrm{T}_{\mathrm{b}}\left(\rho^{*}\left(\kappa_{G}^{\mathrm{b}}\right)\right)=\mathrm{t}_{\mathrm{b}}(\rho) \kappa_{L}^{\mathrm{b}}$$
and that, because of maximality,
$$\mathrm{t}_{\mathrm{b}}(\rho)=\mathrm{r}_{\mathcal{X}}=2\left\|\kappa_{G}^{\mathrm{b}}\right\|$$
we get that
$$\mathrm{T}_{\mathrm{b}}\left(\rho^{*}\left(\kappa_{G}^{\mathrm{b}}\right)\right)=2\left\|\kappa_{G}^{\mathrm{b}}\right\| \kappa_{L}^{\mathrm{b}}$$
which, together with $\left|\mathrm{T}_{\mathrm{b}}\left(\rho^{*}\left(\kappa_{G}^{\mathrm{b}}\right)\right)\right| \leq\left\|\rho^{*}\left(\kappa_{G}^{\mathrm{b}}\right)\right\|$ and $\left\|\kappa_{L}^{\mathrm{b}}\right\|=1 / 2$ implies that
$$\left\|\kappa_{G}^{\mathrm{b}}\right\| \leq\left\|\rho^{*}\left(\kappa_{G}^{\mathrm{b}}\right)\right\| .$$
Since the reverse inequality holds always true, we have proved the lemma. \(\square\)

Let $H$ be of type (RH), $\mathcal{Y}$ the associated symmetric space, $\mathcal{Y}=$ $\mathcal{Y}_{1} \times, \ldots, \times \mathcal{Y}_{m}$ the decomposition into irreducible factors and $\left\{\kappa_{H, i}^{\mathrm{b}}:\right.$ $1 \leq i \leq m\}$ the basis of $\mathrm{H}_{\mathrm{cb}}^{2}(H, \mathbb{R})$ obtained as above. Given a continuous homomorphisms $\sigma: H \rightarrow G$ and writing
$$\sigma^{*}\left(\kappa_{G}^{\mathrm{b}}\right)=\sum_{i=1}^{m} \lambda_{i} \kappa_{H, i}^{\mathrm{b}} .$$
It follows from (6.1) and (2.1) that $\sigma$ is tight if and only if
$$\sum_{i=1}^{m}\left|\lambda_{i}\right| \mathrm{r}_{y_{i}}=\mathrm{r}_{\mathcal{X}} .$$
Finally we recall that a continuous homomorphism $\sigma: H \rightarrow G$ is positive if $\lambda_{i} \geq 0$ for $1 \leq i \leq m$.

Lemma 6.3. Let $\rho: \Gamma \rightarrow H$ and $\sigma: H \rightarrow G$ be homomorphisms, where $\sigma$ is continuous and $H, G$ are of type ( $R H$ ).
\begin{itemize}
\item[(1)] If $\sigma \circ \rho$ is maximal then $\sigma$ is tight;
\item[(2)] if $\sigma \circ \rho$ is maximal and $\sigma$ is positive then $\rho$ is maximal;
\item[(3)] if $\rho$ is maximal and $\sigma$ is tight and positive, then $\sigma \circ \rho$ is maximal.
\end{itemize}
Proof. With the notation introduced above, let
$$\sigma^{*}\left(\kappa_{G}^{\mathrm{b}}\right)=\sum_{i=1}^{m} \lambda_{i} \kappa_{H, i}^{\mathrm{b}} .$$
Thus
Thus if $\sigma \circ \rho$ is maximal, the equality (6.3.a) combined with (6.3,b) and (6.3.c) implies that we have equality in (6.3.c) and hence $\sigma$ is tight.

If $\sigma$ is positive, that is $\lambda_{i} \geq 0$ for $1 \leq i \leq m$, and $\sigma \circ \rho$ is maximal, we get from (6.3.a), (6.3.b) and (6.3.c) that
$$\mathrm{t}_{\mathrm{b}}\left(\rho, \kappa_{H, i}^{\mathrm{b}}\right)=\mathrm{r}_{\mathcal{Y}_{i}}$$
which, together with Lemma 6.1(3) implies that $\rho$ is maximal.
Finally, if $\rho$ is maximal we get from Lemma 6.1(3) that $\mathrm{t}_{\mathrm{b}}\left(\rho, \kappa_{H, i}^{\mathrm{b}}\right)=$ $\mathrm{r}_{\mathcal{Y}_{i}}$ for $1 \leq i \leq m$, and if $\sigma$ is tight and positive then
$$\mathrm{t}_{\mathrm{b}}(\sigma \circ \rho)=\sum_{i=1}^{m} \lambda_{i} \mathrm{t}_{\mathrm{b}}\left(\rho, \kappa_{H, i}^{\mathrm{b}}\right)=\sum_{i=1}^{m} \lambda_{i} \mathrm{r}_{y_{i}}=\mathrm{r}_{\mathcal{X}}$$
and hence $\sigma \circ \rho$ is maximal. \(\square\)

Proofs of Theorems 5 and 8. In order to prove these results we place ourselves, as we may, in the slightly more general context in which $\Gamma$ is a lattice in a finite covering of $\mathrm{PU}(1,1)$. Let now G and $G=\mathbf{G}(\mathbb{R})^{\circ}$ be as in the statement of Theorem 5, that is $\mathbf{G}$ is a connected semisimple algebraic group defined over $\mathbb{R}$ such that $G=\mathbf{G}(\mathbb{R})^{\circ}$ is of Hermitian type, and let $\rho: \Gamma \rightarrow G$ be a maximal representation. Set $\mathbf{H}:=$ $\overline{\rho(\Gamma)}^{Z}$. Since $\rho$ is maximal, it is in particular a tight homomorphism (Lemma 6.2) and hence [12, Theorem 4] applies. In particular, $\mathbf{H}$ is reductive, $H:=\mathbf{H}(\mathbb{R})^{\circ}$ has compact centralizer in $G$ and is of type (RH); furthermore if $\mathcal{Y}$ denotes the symmetric space associated to $H$ then there is a unique $H$-invariant complex structure on $\mathcal{Y}$ such that the inclusion $i: H \rightarrow G$ is tight and positive.

Setting $\Gamma_{0}=\rho^{-1}(\Gamma \cap H)$ and $\rho_{0}:=\left.\rho\right|_{\Gamma_{0}}: \Gamma_{0} \rightarrow H$, we have from Lemma 6.1(1) that $i \circ \rho_{0}: \Gamma_{0} \rightarrow H$ is maximal and, since $i$ is tight and positive, from Lemma 6.3(2) that $\rho_{0}: \Gamma_{0} \rightarrow H$ is maximal as well. Composing $\rho_{0}$ with $p_{i} \circ q: H \rightarrow H_{\mathcal{Y}} \rightarrow H_{\mathcal{Y}_{i}}$, where $\mathcal{Y}_{i}, 1 \leq i \leq m$ are the irreducible factors of $\mathcal{Y}$, the resulting homomorphisms $\rho_{0, i}: \Gamma_{0} \rightarrow H_{\mathcal{Y}_{i}}$ are maximal with Zariski dense image. Theorem 4.1 then implies that $\mathcal{Y}_{i}$ is of tube type and $\rho_{0, i}$ is injective, modulo the center of $\Gamma_{0}$, and with discrete image. This implies that $\rho: \Gamma \rightarrow G$ is injective (modulo the center) and with discrete image. Since $\mathcal{Y}$ is of tube type and $i: H \rightarrow G$ is tight, there is a unique maximal subdomain $\mathcal{T} \subset \mathcal{X}$ of tube type with $i(\mathcal{Y}) \subset \mathcal{T}$ (see [12, Theorem 10(1)]); it is moreover $H$-invariant and hence (by uniqueness) $\mathbf{H}(\mathbb{R})$-invariant and thus $\rho(\Gamma)$-invariant. This completes the proof of Theorem 5.

Applying Theorem 5.1 to every irreducible factor of $\mathcal{Y}$, we get, say, a left continuous strictly $\rho_{0}$-equivariant map $\varphi: \partial \mathbb{D} \rightarrow \check{S}_{\mathcal{Y}}=\check{S}_{\mathcal{Y}_{1}} \times \cdots \times$ $\check{S}_{\mathcal{Y}_{m}}$. Since $i: H \rightarrow G$ is tight, we have also a canonical $i$-equivariant map $\hat{i}: \check{S}_{\mathcal{Y}} \rightarrow \check{S}_{\mathcal{X}}$; applying judiciously the uniqueness property in [12, Theorem 4.1.], we deduce that $\hat{i} \circ \varphi: \partial \mathbb{D} \rightarrow \check{S}_{\mathcal{X}}$ is $\rho$-equivariant. Finally, writing
$$i^{*}\left(\kappa_{\mathcal{X}}^{\mathrm{b}}\right)=\sum_{i=1}^{m} \lambda_{i} \kappa_{\mathcal{Y}, i}^{\mathrm{b}},$$
for $\lambda_{i} \geq 0$, we have (see [12, Lemma 5.9.])
$$\beta_{\check{S}_{\mathcal{X}}}(\hat{i}(x), \hat{i}(y), \hat{i}(z))=\sum_{j=1}^{m} \lambda_{j} \beta_{\check{S}_{y_{j}}}\left(x_{j}, y_{j}, z_{j}\right),$$
where $x=\left(x_{1}, \cdots, x_{m}\right), y=\left(y_{1}, \cdots, y_{m}\right), z=\left(z_{1}, \cdots, z_{m}\right) \in \check{S}_{\mathcal{Y}}$. This, together with (4.2) in Corollary 4.4, implies
$$\beta_{\check{S}_{\mathcal{X}}}(\hat{i} \varphi(a), \hat{i} \varphi(b), \hat{i} \varphi(c))=\left(\sum_{i=1}^{m} \lambda_{i} \mathrm{r}_{\mathcal{Y}_{i}}\right) \beta_{\partial \mathbb{D}}(a, b, c)$$
and concludes the proof since $i$ is tight and positive. \(\square\)

\section*{7. Rotation numbers and applications to groups of Hermitian type}

In this section we introduce and study rotation numbers on locally compact groups and compute them for groups of Hermitian type. The results are of independent interest. Here they are used in an essential way in the computation of the Toledo invariant in the case of surfaces with boundary.
7.1. Basic definitions and properties. Let $G$ be a locally compact group and $\kappa \in \widehat{\mathrm{H}}_{\mathrm{cb}}^{2}(G, \mathbb{Z})$ a bounded integer valued Borel class. Let $B<G$ be a closed subgroup and consider the first few terms of the long exact sequence
$$0 \longrightarrow \operatorname{Hom}_{\mathrm{c}}(B, \mathbb{R} / \mathbb{Z}) \stackrel{\delta}{\longrightarrow} \widehat{\mathrm{H}}_{\mathrm{cb}}^{2}(B, \mathbb{Z}) \longrightarrow \mathrm{H}_{\mathrm{cb}}^{2}(B, \mathbb{R}) \longrightarrow \ldots$$
coming from the coefficient sequence (2.4); denote by $\kappa_{\mathbb{R}}$ the image in $\mathrm{H}_{\mathrm{cb}}^{2}(G, \mathbb{R})$ of an element $\kappa \in \widehat{\mathrm{H}}_{\mathrm{cb}}^{2}(G, \mathbb{Z})$. Then if $\left.\kappa_{\mathbb{R}}\right|_{B}=0$, we let $f_{B}: B \rightarrow \mathbb{R} / \mathbb{Z}$ denote the unique continuous homomorphism with $\delta\left(f_{B}\right)=\left.\kappa\right|_{B}$. In particular this applies to $B=\overline{\langle g\rangle}$ for any $g \in G$ and we define

Definition 7.1. The rotation number of $g \in G$ with respect to $\kappa \in$ $\widehat{\mathrm{H}}_{\mathrm{cb}}^{2}(G, \mathbb{Z})$ is
$$\operatorname{Rot}_{\kappa}(g):=f_{\overline{\langle g\rangle}}(g) .$$

Using that the exact sequence in (7.1) is natural with respect to group homomorphisms, one verifies easily the following properties

Lemma 7.2. (1) $\operatorname{Rot}_{\kappa}: G \rightarrow \mathbb{R} / \mathbb{Z}$ is invariant under conjugation;
\begin{itemize}
\item[(2)] if $\left.\kappa_{\mathbb{R}}\right|_{B}=0$, then $\left.\operatorname{Rot}_{\kappa}\right|_{B}$ is a continuous homomorphism and $\delta\left(\left.\operatorname{Rot}_{\kappa}\right|_{B}\right)=\left.\kappa\right|_{B} ;$
\item[(3)] if $\sigma: G_{1} \rightarrow G_{2}$ is a continuous homomorphism and $\kappa_{1}=\sigma^{*}\left(\kappa_{2}\right)$, then
$$\operatorname{Rot}_{\kappa_{1}}\left(g_{1}\right)=\operatorname{Rot}_{\kappa_{2}}\left(\sigma\left(g_{1}\right)\right)$$
\end{itemize}
for all $g_{1} \in G_{1}$.
In the study of rotation numbers $\operatorname{Rot}_{\kappa}$, quasimorphisms play an important role. We quickly review the basic definitions. If $A=\mathbb{Z}, \mathbb{R}$, a function $f: G \rightarrow A$ is a quasimorphism if the function $d f: G \rightarrow A$
$$d f(x, y)=f(x y)-f(x)-f(y)$$
is bounded. When $A=\mathbb{R}$, a quasimorphism is homogeneous if
$$f\left(g^{n}\right)=n f(g)$$
for $n \in \mathbb{Z}$ and $g \in G$. Any quasimorphism $f: G \rightarrow A$ can be made homogeneous by setting
$$H f(x):=\lim _{n \rightarrow \infty} \frac{f\left(x^{n}\right)}{n} \in \mathbb{R}$$
and it is a standard fact that $f-H f$ is bounded.
Lemma 7.3. Assume that $\kappa$ vanishes when considered as an ordinary class in $\widehat{\mathrm{H}}_{\mathrm{c}}^{2}(G, \mathbb{Z})$. Let $f: G \rightarrow \mathbb{Z}$ be a Borel map such that $d f$ is bounded and represents $\kappa$ seen as a bounded class. Then $f$ is a quasimorphism and
$$\operatorname{Rot}_{\kappa}(g) \equiv H f(g) \quad \bmod \mathbb{Z}$$
where $H f$ is the homogenization of $f$.
Proof. By Lemma 7.2(3), it suffices to show the assertion for $G=\mathbb{Z}$. Let $p: \mathbb{R} \rightarrow \mathbb{R} / \mathbb{Z}$ be the canonical projection; then $p \circ H f: \mathbb{Z} \rightarrow \mathbb{R} / \mathbb{Z}$ is a homomorphism since $H f$ is homogeneous, and we claim that $\kappa=$ $\delta(p \circ H f)$. Indeed let $\sigma: \mathbb{R} / \mathbb{Z} \rightarrow \mathbb{R}$ be the Borel section of $p$ with values in $[0,1)$; then we have
$$\delta(p \circ H F)=-\mathrm{d}(\sigma \circ p \circ H f)=d f-d((f-H f+\sigma \circ p \circ H f)$$
where we have used in the last equality that $d H f=0$. The claim then follows from the fact that $f$ and $H f-\sigma \circ p \circ H f$ take integral values and both $f-H f$ and $\sigma \circ p \circ H f$ are bounded. From the claim we the get that
$$\operatorname{Rot}_{\kappa}(g)=p \circ H f(g)$$
for all $g \in \mathbb{Z}$, which is the assertion that needed to be proved. \(\square\)

Next we have:
Lemma 7.4. Let $f: G \rightarrow \mathbb{R}$ be a homogeneous Borel quasimorphism. Then $f$ is continuous.

Proof. We show first that $f$ is locally bounded. Let $C:=\sup _{x, y}|d f(x, y)|$ and $E_{N}=\{x \in G:|f(x)| \leq N\}$. Then $E_{N}=E_{N}^{-1}$ and for $N$ large enough is of positive Haar measure. For such $N$ we deduce that $E_{N} \cdot E_{N}$ is a neighborhood of $e \in G$; since $f$ is a quasimorphism we have that $E_{N} \cdot E_{N} \subset E_{N+2 C}$ which implies that $f$ is bounded in a neighborhood of $e$ and hence, by the quasimorphism property, locally bounded. Fix now $\varphi: G \rightarrow[0, \infty)$ continuous with compact support and of total integral one. Since $f$ is locally bounded, we have that for every $n \in \mathbb{N}$
$$F_{n}(x)=\frac{1}{n} \int_{G}\left(f\left(x^{n} y\right)-f(y)\right) \varphi(y) d y$$
is defined and continuous. Since $f$ is homogeneous we have
$$\begin{aligned}
\left|f(x)-F_{n}(x)\right| & =\left|\frac{1}{n} f\left(x^{n}\right)-F_{n}(x)\right| \\
& =\left|\frac{1}{n} \int_{G}\left(f\left(x^{n}\right)+f(y)-f\left(x^{n} y\right)\right) \varphi(y) d y\right| \leq \frac{C}{n}
\end{aligned}$$
which implies that $f$ is the uniform limit of a sequence of continuous functions and therefore continuous. \(\square\)

Now we come to the main goal of this subsection, which is the continuity of $\operatorname{Rot}_{\kappa}$; this is shown by exhibiting a direct relationship with a certain quasimorphism on a central extension of $G$. More precisely let as before $\kappa \in \widehat{\mathrm{H}}_{\mathrm{cb}}^{2}(G, \mathbb{Z})$; then $\kappa$ can be seen as a class in $\mathrm{H}_{\mathrm{c}}^{2}(G, \mathbb{Z})$ and hence gives rise by [44] to a topological central extension
$$0 \longrightarrow \mathbb{Z} \xrightarrow{i} G_{\kappa} \xrightarrow{p} G \longrightarrow e$$
that is $G_{\kappa}$ is a locally compact group, $i$ and $p$ are continuous, $i(\mathbb{Z})$ is a closed central subgroup of $G_{\kappa}$ and $G_{\kappa} / i(\mathbb{Z})$ is topologically isomorphic to $G$.

Proposition 7.5. There exists a continuous homogeneous quasimorphism $f: G_{\kappa} \rightarrow \mathbb{R}$ such that
\begin{itemize}
\item[(1)] $f(i(n) g)=n+f(g)$, for $n \in \mathbb{Z}, g \in G_{\kappa}$;
\item[(2)] $\operatorname{Rot}_{\kappa}(p(g)) \equiv f(g) \bmod \mathbb{Z}$.
\end{itemize}

Corollary 7.6. Let $\kappa \in \widehat{\mathrm{H}}_{\mathrm{cb}}^{2}(G, \mathbb{Z})$. Then $\operatorname{Rot}_{\kappa}: G \rightarrow \mathbb{R} / \mathbb{Z}$ is continuous.

Proof of Proposition 7.5. Let $c: G^{2} \rightarrow \mathbb{Z}$ be a bounded Borel cocycle which represents $\kappa \in \widehat{\mathrm{H}}_{\mathrm{cb}}^{2}(G, \mathbb{Z})$ and which we assume to be normalized.

Then $G_{\kappa}$ is a Borel group isomorphic to the Borel space $G \times \mathbb{Z}$ with multiplication given by
$$\left(g_{1}, n_{1}\right)\left(g_{2}, n_{2}\right)=\left(g_{1} g_{2}, n_{1}+n_{2}+c\left(g_{1}, g_{2}\right)\right) .$$
Define $f_{1}: G_{\kappa} \rightarrow \mathbb{Z}$ by $f_{1}(g, m):=m$. Then $f_{1}$ is a Borel function and $d f_{1}$ is a bounded Borel cocycle representing $p^{*}(\kappa) \in \widehat{\mathrm{H}}_{\mathrm{cb}}^{2}\left(G_{\kappa}, \mathbb{Z}\right)$. let $f: G_{\kappa} \rightarrow \mathbb{R}$ be the homogenization of $f_{1}$. Then Lemma 7.3 implies that
$$\operatorname{Rot}_{\kappa}(p(g))=\operatorname{Rot}_{p^{*}(\kappa)}(g) \equiv f(g) \quad \bmod \mathbb{Z}$$
and Lemma 7.4 that $f$ is continuous. Finally $f$ satisfies (1) because $f_{1}$ does and $i(\mathbb{Z})$ is central. \(\square\)
7.2. Rotation numbers on groups of Hermitian type. We begin first by determining $\widehat{\mathrm{H}}_{\mathrm{cb}}^{2}(G, \mathbb{Z})$ for $G$ of Hermitian type. The main points are summarized in the following

Proposition 7.7. Let $G$ be a group of Hermitian type and $K<G$ a maximal compact subgroup.
\begin{itemize}
\item[(1)] The comparison map $\widehat{\mathrm{H}}_{\mathrm{cb}}^{2}(G, \mathbb{Z}) \rightarrow \widehat{\mathrm{H}}_{\mathrm{c}}^{2}(G, \mathbb{Z})$ is an isomorphism;
\item[(2)] the map
$$\begin{aligned}
\widehat{\mathrm{H}}_{\mathrm{cb}}^{2}(G, \mathbb{Z}) & \rightarrow \operatorname{Hom}_{\mathrm{c}}(K, \mathbb{R} / \mathbb{Z}) \\
\kappa & \mapsto \operatorname{Rot}_{\left.\kappa\right|_{K}}
\end{aligned}$$
is an isomorphism;
\item[(3)] the change of coefficient map
$$\widehat{\mathrm{H}}_{\mathrm{cb}}^{2}(G, \mathbb{Z}) \rightarrow \mathrm{H}_{\mathrm{cb}}^{2}(G, \mathbb{R})$$
is injective and its image is a lattice.
\end{itemize}

Proof. (1) follows from the commutativity of the diagram
![](https://cdn.mathpix.com/cropped/4c2b5273-bae1-4a9e-bc17-559dcbfd0d15-40.jpg?height=223&width=917&top_left_y=1851&top_left_x=567)
and the fact that with real coefficients the comparison map is an isomorphism.
(2) follows from (1) and the fact that in ordinary Borel cohomology the restriction
$$\widehat{\mathrm{H}}_{\mathrm{c}}^{2}(G, \mathbb{Z}) \rightarrow \widehat{\mathrm{H}}_{\mathrm{c}}^{2}(K, \mathbb{Z})$$
is an isomorphism [52].
(3) follows from (1) and the corresponding statement in ordinary cohomology. \(\square\)

In view of the preceding proposition we can refer for every $u \in$ $\operatorname{Hom}_{\mathrm{c}}(K, \mathbb{R} / \mathbb{Z})$ to the class $\kappa$ associated to $u$, and conversely.

We turn now to the explicit computation of the rotation number function. let $G=K A N$ be an Iwasawa decomposition; recall the refined Jordan decomposition, namely that every $g \in G$ is a product $g=g_{e} g_{h} g_{n}$, where $g_{e}$ is contained in a compact subgroup, $g_{h}$ and $g_{n}$ are conjugated to an element respectively in $A$ and $N$; moreover the elements $g_{e}, g_{h}$ and $g_{n}$ commute pairwise. Then we have:
Proposition 7.8. Let $\kappa \in \widehat{\mathrm{H}}_{\mathrm{cb}}^{2}(G, \mathbb{Z})$ and $u \in \operatorname{Hom}_{\mathrm{c}}(K, \mathbb{R} / \mathbb{Z})$ be the corresponding homomorphism.
\begin{itemize}
\item[(1)] $\left.\operatorname{Rot}_{\kappa}\right|_{A N}$ is the trivial homomorphism;
\item[(2)] for $g \in G$, let $g_{e}$ be the elliptic component in the refined Jordan decomposition of $g$ and $k \in C\left(g_{e}\right) \cap K$, where $C\left(g_{e}\right)$ denotes the $G$-conjugacy class of $g_{e}$. Then $\operatorname{Rot}_{\kappa}(g)=u(k)$.
\end{itemize}

Proof. (1) Since $B=A N$ is amenable, $\left.\kappa_{\mathbb{R}}\right|_{B}=0$ and thus Lemma 7.2(2) implies that $\left.\operatorname{Rot}_{\kappa}\right|_{A N}$ is a continuous homomorphism and hence differentiable. Since $[B, B]=N$, then $\operatorname{Rot}_{\kappa}(N)=0$. The restriction $\left.\operatorname{Rot}_{\kappa}\right|_{A}$ is invariant under the Weyl group $\mathcal{N}_{K}(A) / \mathcal{Z}_{K}(A)$ and hence its differential
$$\left.D_{e} \operatorname{Rot}_{\kappa}\right|_{A}: \mathfrak{a} \rightarrow \mathbb{R}$$
is a linear form invariant under the Weyl group; it must therefore vanish since $G$ is semisimple and thus $\left.\operatorname{Rot}_{\kappa}\right|_{A}$ is trivial as well.
(2) Let $g=g_{e} g_{h} g_{n}$ be the refined Jordan decomposition of $g$. Since the subgroup $C$ generated by $g_{e}, g_{h}$ and $g_{n}$ is Abelian, $\left.\operatorname{Rot}_{\kappa}\right|_{C}$ is a homomorphism, hence
$$\operatorname{Rot}_{\kappa}(g)=\operatorname{Rot}_{\kappa}\left(g_{e}\right)+\operatorname{Rot}_{\kappa}\left(g_{h}\right)+\operatorname{Rot}_{\kappa}\left(g_{n}\right) .$$
Taking into account (1) and the fact that $g_{h}$ and $g_{n}$ are conjugate respectively to elements in $A$ and $N$, we get that
$$\operatorname{Rot}_{\kappa}(g)=\operatorname{Rot}_{\kappa}\left(g_{e}\right)=\operatorname{Rot}_{\kappa}(k)=u(k)$$
which concludes the proof. \(\square\)

For the next result, if $u \in \operatorname{Hom}_{\mathrm{c}}(K, \mathbb{R} / \mathbb{Z})$, let us denote by $u_{*}$ : $\pi_{1}(G) \rightarrow \mathbb{Z}$ the homomorphism induced by $u$ on the level of fundamental groups, where we have identified $\pi_{1}(K)$ with $\pi_{1}(G)$.
Theorem 7.9. Let $u: K \rightarrow \mathbb{R} / \mathbb{Z}$ be a continuous homomorphism and $\kappa \in \widehat{\mathrm{H}}_{\mathrm{cb}}^{2}(G, \mathbb{Z})$ the associated class.
\begin{itemize}
\item[(1)] $\operatorname{Rot}_{\kappa}$ is continuous;
\item[(2)] the unique continuous lift $\widetilde{\operatorname{Rot}_{\kappa}}: \widetilde{G} \rightarrow \mathbb{R}$ such that $\widetilde{\operatorname{Rot}_{\kappa}}(e)=0$ is a continuous homogeneous quasimorphism and satisfies
$$\widetilde{\operatorname{Rot}_{\kappa}}(z g)=u_{*}(z)+\widetilde{\operatorname{Rot}_{\kappa}}(g)$$
for all $z \in \pi_{1}(G)$ and for all $g \in \widetilde{G}$.
\end{itemize}

As a consequence we obtain a description of the space $\mathcal{Q}(\widetilde{G})_{\mathbb{Z}}$ of continuous homogeneous quasimorphism $f: \widetilde{G} \rightarrow \mathbb{R}$ such that $f\left(\pi_{1}(G)\right) \subset$ $\mathbb{Z}$.

Corollary 7.10. The maps
$$\begin{aligned}
\operatorname{Hom}_{\mathrm{c}}(K, \mathbb{R} / \mathbb{Z}) & \rightarrow \mathcal{Q}(\widetilde{G})_{\mathbb{Z}} \rightarrow \operatorname{Hom}\left(\pi_{1}(G), \mathbb{Z}\right) \\
u & \left.\mapsto \widetilde{\operatorname{Rot}}_{\kappa} \mapsto \widetilde{\operatorname{Rot}}_{\kappa}\right|_{\pi_{1}(G)}=u_{*}
\end{aligned}$$
are group isomorphisms.
Proof of Theorem 7.9. The first assertion is a special case of Corollary 7.6. Let then $p: G_{\kappa} \rightarrow G$ be the Lie group central extension determined by $\kappa$ and $\pi: \widetilde{G} \rightarrow\left(G_{\kappa}\right)^{\circ}$ the canonical projection. If $f: G_{\kappa} \rightarrow \mathbb{R}$ is the continuous homogeneous quasimorphism given by Proposition 7.5, then it follow from Proposition 7.5(2) that $\left.f\right|_{G_{\kappa}} \circ \pi$ : $\widetilde{G} \rightarrow \mathbb{R}$ is a continuous lift of $\operatorname{Rot}_{\kappa}$ to $\widetilde{G}$ which moreover vanishes at $e$. Hence $\widetilde{\operatorname{Rot}_{\kappa}}=\left.f\right|_{\left(G_{\kappa}\right)^{\circ}} \circ \pi$, which implies the remaining assertion in the theorem. \(\square\)

Proof of Corollary 7.10. Since the composition of the two arrows is the isomorphism
$$\begin{array}{ccc}
\operatorname{Hom}_{\mathrm{c}}(K, \mathbb{R} / \mathbb{Z}) & \rightarrow \operatorname{Hom}\left(\pi_{1}(G), \mathbb{Z}\right) \\
u & \mapsto & u_{*}
\end{array}$$
it suffices to show that the second morphism is injective. If $f_{1}, f_{2}$ : $\widetilde{G} \rightarrow \mathbb{R}$ are homogeneous continuous quasimorphisms which induce the same homomorphism $h: \pi_{1}(G) \rightarrow \mathbb{Z}$ then their difference $f_{1}-f_{2}$ is $\pi_{1}(G)$-invariant and hence descends to a homogeneous quasimorphism $G \rightarrow \mathbb{R}$ which therefore vanishes since $G$ is connected semisimple with finite center. Thus $f_{1}=f_{2}$, which completes the proof. \(\square\)

Remark 7.11. For special classes $\kappa \in \widehat{\mathrm{H}}_{\mathrm{cb}}^{2}(G, \mathbb{Z})$ the rotation number $\operatorname{Rot}_{\kappa}$ coincides with previously known constructions:
\begin{itemize}
\item[(1)] If $G=\operatorname{Homeo}_{+}\left(S^{1}\right)$ is the group of orientation preserving homeomorphisms of the circle (viewed as an abstract group) and $e^{\mathrm{b}} \in \mathrm{H}_{\mathrm{b}}^{2}(G, \mathbb{Z})$ is the bounded Euler class, Ghys [25] observed
\end{itemize}
\begin{itemize}
\item[] that $\operatorname{Rot}_{e^{\mathrm{b}}}(\varphi)$ is the classical rotation number of the homeomorphism $\varphi$.
\item[(2)] To obtain the symplectic rotation number defined by Barge and Ghys [1] for $G=\operatorname{Sp}(2 n, \mathbb{R})$, we have to consider the class $\kappa$ which corresponds to the homomorphism $u: K=\mathrm{U}(n) \rightarrow \mathbb{T}$ defined by $u(k)=(\operatorname{det} k)^{2}$.
\item[(3)] If $\mathcal{D}$ is an irreducible symmetric domain of tube type, $G=$ $\operatorname{Aut}(\mathcal{D})^{\circ}$ and $K$ is the stabilizer of $0 \in \mathcal{D}$, Clerc and Koufany construct a homomorphism $\chi: K \rightarrow \mathbb{T}$ using the Jordan algebra determinant. The rotation number function and the quasimorphism constructed in their paper [18, Theorem 10.3 and Proposition 10.4], coincide then respectively with $\operatorname{Rot}_{\kappa}$ and $\widehat{\operatorname{Rot}}_{\kappa}$, where $\kappa$ is the class corresponding to $\chi$.
We observe moreover that if $u: K \rightarrow \mathbb{T}$ is the complex Jacobian at 0 , then for every $k \in K$ we have that
$$\chi(k)^{p_{\mathcal{X}}}=u(k)^{2},$$
which incidentally shows that $\kappa_{G}^{\mathrm{b}}$ is in the image of $\widehat{\mathrm{H}}_{\mathrm{cb}}^{2}(G, \mathbb{Z})$.
\end{itemize}

\section*{8. Toledo numbers: formula and applications to representation varieties}
8.1. The formula. Let $\Sigma$ be a connected oriented surface and $G$ a group of Hermitian type. In this subsection we establish a formula for the Toledo invariant $\mathrm{T}_{\kappa}(\Sigma, \rho)$ where $\kappa$ is a bounded integral class, and we concentrate on the case in which $\partial \Sigma \neq \emptyset$; we mention at the end the formula in the case in which $\partial \Sigma=\emptyset$.

The boundary of $\Sigma$ is the union $\partial \Sigma=\bigsqcup_{j=1}^{n} C_{j}$ of oriented circles and we fix a presentation
$$\pi_{1}(\Sigma)=\left\langle a_{1}, b_{1}, \ldots, a_{g}, b_{g}, c_{1}, \ldots, c_{n}: \prod_{i=1}^{g}\left[a_{i}, b_{i}\right] \prod_{j=1}^{n} c_{j}=e\right\rangle$$
where $g$ is the genus of $\Sigma$ and $c_{j}$ is freely homotopic to $C_{j}$ with positive orientation. Combining now the long exact sequence in bounded cohomology associated to the pair of spaces $(\Sigma, \partial \Sigma)$ and the one associated
to the usual coefficient sequence in (2.4), we obtain
![](https://cdn.mathpix.com/cropped/4c2b5273-bae1-4a9e-bc17-559dcbfd0d15-44.jpg?height=509&width=997&top_left_y=482&top_left_x=529)
where we have used that $\mathrm{H}_{\mathrm{b}}^{i}(\partial \Sigma, \mathbb{R})=0, i \geq 1$. We have then the following congruence relation:

Lemma 8.1. Let $\alpha \in \mathrm{H}_{\mathrm{b}}^{2}(\Sigma, \mathbb{Z})$ and denote by $\alpha_{\mathbb{R}}$ its image in $\mathrm{H}_{\mathrm{b}}^{2}(\Sigma, \mathbb{R})$.
$$\begin{aligned}
\left\langle j_{\partial \Sigma}^{-1}\left(\alpha_{\mathbb{R}}\right),[\Sigma, \partial \Sigma]\right\rangle & \equiv-\left\langle\delta^{-1}\left(\left.\alpha\right|_{\partial \Sigma}\right),[\partial \Sigma]\right\rangle \quad \bmod \mathbb{Z} \\
& =-\sum_{j=1}^{n}\left\langle\left.\delta^{-1} \alpha\right|_{C_{j}},\left[C_{j}\right]\right\rangle,
\end{aligned}$$
where we view $j_{\partial \Sigma}^{-1}\left(\alpha_{\mathbb{R}}\right)$ as ordinary relative singular cohomology class.
Proof. Let $c \in \mathcal{Z}_{\mathrm{b}}^{2}(\Sigma, \mathbb{Z})$ be a $\mathbb{Z}$-valued bounded cocycle representing $\alpha \in \mathrm{H}_{\mathrm{b}}^{2}(\Sigma, \mathbb{Z})$, and let $\left.c\right|_{\partial \Sigma} \in \mathcal{Z}_{\mathrm{b}}^{2}(\partial \Sigma, \mathbb{Z})$ be its restriction to the boundary $\partial \Sigma$. Since the fundamental groups of the components of $\partial \Sigma$ are amenable, there exists a bounded $\mathbb{R}$-valued 1 -cochain $c^{\prime} \in F_{\mathrm{b}}^{1}(\partial \Sigma, \mathbb{R})$ such that $d c^{\prime}=\left.c\right|_{\partial \Sigma}$. Let $c^{\prime \prime} \in F_{\mathrm{b}}^{1}(\partial \Sigma, \mathbb{R} / \mathbb{Z})$ be the corresponding $\mathbb{R} / \mathbb{Z}$-valued 1-cochain on $\partial \Sigma$ : for any 1-simplex $t \in S_{1}(\partial \Sigma)$ we have that
$$\left\langle c^{\prime}, t\right\rangle \equiv\left\langle c^{\prime \prime}, t\right\rangle \quad \bmod \mathbb{Z}$$
and moreover, since $\left.c\right|_{\partial \Sigma}$ is $\mathbb{Z}$-valued, $c^{\prime \prime}$ is a 1-cocycle which represents the class $\delta^{-1}\left(\left.\alpha\right|_{\partial \Sigma}\right) \in \mathrm{H}^{1}(\partial \Sigma, \mathbb{R} / \mathbb{Z})$.

On the other hand, we can extend $c^{\prime}$ to a 1-cochain $\widetilde{c^{\prime}}$ on $\Sigma$ by setting
$$\widetilde{c^{\prime}}(\sigma)=\left\{\begin{array}{cl}
c^{\prime}(\sigma) & \text { if } \sigma \in S_{1}(\partial \Sigma) \\
0 & \text { otherwise },
\end{array}\right.$$
so that $c-d \widetilde{c^{\prime}} \in \mathcal{Z}_{\mathrm{b}}^{2}(\Sigma, \partial \Sigma, \mathbb{R})$ is a cocycle which represents $j_{\partial \Sigma}^{-1}\left(\alpha_{\mathbb{R}}\right)$.
Let now $s$ be a two-chain which represents the relative fundamental class $[\Sigma, \partial \Sigma]$, so that $\partial s$ represents the fundamental class $[\partial \Sigma]$. From
the definition of $\widetilde{c^{\prime}}$, from (8.2) and the fact that $\langle c, s\rangle \in \mathbb{Z}$, it follows that
$$\left\langle c-d \widetilde{c^{\prime}}, s\right\rangle=\langle c, s\rangle-\left\langle\widetilde{c^{\prime}}, s\right\rangle \equiv-\left\langle c^{\prime \prime}, \partial s\right\rangle \quad \bmod \mathbb{Z},$$
thus completing the proof. \(\square\)

We apply the above general lemma to the situation at hand and show the following
$$\mathrm{T}_{\kappa}(\Sigma, \rho) \equiv-\sum_{j=1}^{n} \operatorname{Rot}_{\kappa}\left(\rho\left(c_{j}\right)\right) \quad \bmod \mathbb{Z}$$
Proof. Consider the commutative diagram

\begin{figure}
\captionsetup{labelformat=empty}
\caption{Lemma 8.2. Let $\kappa \in \widehat{\mathrm{H}}_{\mathrm{cb}}^{2}(G, \mathbb{Z})$ and $\rho: \pi_{1}(\Sigma) \rightarrow G$ a homomorphism. Then}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/4c2b5273-bae1-4a9e-bc17-559dcbfd0d15-45.jpg?height=381&width=629&top_left_y=1137&top_left_x=712}
\end{figure}
where the horizontal arrows are isomorphisms, the vertical arrows between first and second row are restriction maps and those between third and second are connecting homomorphisms. The commutativity implies the first equality
$$\left\langle\delta^{-1}\left(\left.\left[g_{\Sigma} \rho^{*}(\kappa)\right]\right|_{C_{j}}\right),\left[C_{j}\right]\right\rangle=\delta^{-1}\left(\left.\rho^{*}(\kappa)\right|_{\pi_{1}\left(C_{j}\right)}\right)\left(c_{j}\right)=\operatorname{Rot}_{\kappa}\left(\rho\left(c_{j}\right)\right),$$
while the second is the definition of $\operatorname{Rot}_{\kappa}$ (see Definition 7.1). This, together with Lemma 8.1 applied to $\alpha=g_{\Sigma}\left(\rho^{*}(\kappa)\right)$ implies the result. \(\square\)

Now we come to the formula for the Toledo invariant. Observe first that when $\partial \Sigma \neq \emptyset, \pi_{1}(\Sigma)$ is a free group and thus any homomorphism $\rho: \pi_{1}(\Sigma) \rightarrow G$ admits a lift $\widetilde{\rho}: \pi_{1}(\Sigma) \rightarrow \widetilde{G}$.

Proof of Theorem 12. Using the equivariance property of $\widetilde{\mathrm{Rot}_{\kappa}}$ in Theorem 7.9(2), one checks that
$$\mathrm{R}(\rho):=-\sum_{j=1}^{n} \widetilde{\mathrm{Rot}_{\kappa}}\left(\widetilde{\rho}\left(c_{j}\right)\right)$$
does not depend on the choice of the lift $\widetilde{\rho}$. Thus the map
$$\begin{aligned}
\operatorname{Hom}\left(\pi_{1}(\Sigma), G\right) & \rightarrow \mathbb{R} \\
\rho & \mapsto \mathrm{R}(\rho)
\end{aligned}$$
is well defined and continuous since $\widetilde{\operatorname{Rot}_{\kappa}}$ is continuous and $\widetilde{G} \rightarrow G$ is a covering. This implies with Proposition 3.10 that the map
$$\rho \mapsto \mathrm{T}_{\kappa}(\Sigma, \rho)-\mathrm{R}(\rho)$$
is continuous; on the other hand (from Lemma 8.2) we know that this map is $\mathbb{Z}$-valued and hence, since $\operatorname{Hom}\left(\pi_{1}(\Sigma), G\right)$ is connected, that (8.3) is constant: evaluation at the trivial homomorphism implies that this constant is zero thus showing the theorem. \(\square\)

Finally, we indicate briefly the formula when $\partial \Sigma=\emptyset$. Let
$$[\cdot, \cdot]^{\sim}: G \times G \rightarrow \widetilde{G}$$
denote the $\widetilde{G}$-valued commutator map. Recall that when $\partial \Sigma=\emptyset$ the consideration of ordinary cohomology suffices.
Theorem 8.3. Let $\kappa \in \widehat{\mathrm{H}}_{\mathrm{c}}^{2}(G, \mathbb{Z})$ and $u \in \operatorname{Hom}_{\mathrm{c}}(K, \mathbb{R} / \mathbb{Z})$ the associated homomorphism. If $\rho: \pi_{1}(\Sigma) \rightarrow G$ is a representation, we have
$$\mathrm{T}_{\kappa}(\Sigma, \rho)=-u_{*}\left(\prod_{j=1}^{g}\left[\rho\left(a_{i}\right), \rho\left(b_{i}\right)\right]^{\sim}\right)$$
where, as usual, $u_{*}: \pi_{1}(K)=\pi_{1}(G) \rightarrow \mathbb{Z}$ is the homomorphism induced by $u$.

Remark 8.4. One may prove the formula in Theorem 8.3 by cutting $\Sigma$ along the separating curve $\left[a_{1}, b_{1}\right]$ and combine the formula in Theorem 8.3 applied to each component together with the additivity property in Proposition 3.2(1).

Remark 8.5. The formula in Theorem 8.3 generalizes Milnor's classical formula for the Euler number of a representation into $\mathrm{GL}^{+}(2)$ [45].
8.2. The bounded fundamental class and generalized $w_{1}$-classes. The group $\operatorname{PU}(1,1)$ acts effectively on the circle $\partial \mathbb{D}$ and we have seen that if $\rho_{1}$ and $\rho_{2}$ are maximal representations of $\pi_{1}(\Sigma)$ into $\operatorname{PU}(1,1)$ then the resulting actions on $\partial \mathbb{D}$ are semiconjugate in the sense of Ghys [25]. If $e^{\mathrm{b}} \in \mathrm{H}_{\mathrm{b}}^{2}(\mathrm{PU}(1,1), \mathbb{Z})$ denotes the bounded Euler class, or more precisely the restriction to $\operatorname{PU}(1,1)$ of the bounded Euler class of the group of orientation preserving homeomorphisms of $\partial \mathbb{D}$, then $\rho_{1}^{*}\left(e^{\mathrm{b}}\right)=\rho_{2}^{*}\left(e^{\mathrm{b}}\right)$ [25]. Thus we obtain a canonical class
$$\kappa_{\Sigma, \mathbb{Z}}^{\mathrm{b}} \in \mathrm{H}_{\mathrm{b}}^{2}\left(\pi_{1}(\Sigma), \mathbb{Z}\right)$$
associated to the oriented surface $\Sigma$ and which plays the role of the classical fundamental class when $\partial \Sigma \neq \emptyset$. We propose to call it the bounded fundamental class of $\Sigma$; observe that even when $\partial \Sigma=\emptyset$, this class contains more information than the usual fundamental class since
$$\mathrm{H}_{\mathrm{b}}^{2}\left(\pi_{1}(\Sigma), \mathbb{Z}\right) \rightarrow \mathrm{H}^{2}\left(\pi_{1}(\Sigma), \mathbb{Z}\right)$$
is never injective. Thus we obtain that for a representation $\rho: \pi_{1}(\Sigma) \rightarrow$ $\operatorname{PU}(1,1)$ the following are equivalent
\begin{itemize}
\item[(1)] $\rho$ is maximal;
\item[(2)] $\rho$ comes from a complete hyperbolic structure on $\Sigma^{\circ}$;
\item[(3)] $\rho^{*}\left(e^{\mathrm{b}}\right)=\kappa_{\Sigma, \mathbb{Z}}^{\mathrm{b}}$.
\end{itemize}
For general groups $G$ of Hermitian type, an analogue of the equivalence of (1) and (3) holds for real coefficients; the extent to which it does not hold for integral coefficients will lead to nontrivial invariants for maximal representations.

Let now $G$ be of Hermitian type and, as usual, let $\left\{\kappa_{G, i}^{\mathrm{b}}: 1 \leq i \leq\right.$ $n\}$ be the basis of $\mathrm{H}_{\mathrm{cb}}^{2}(G, \mathbb{R})$ determined by the decomposition of the associated symmetric space $\mathcal{X}=\mathcal{X}_{1} \times \ldots \mathcal{X}_{n}$ into irreducible factors. We define a linear form $\lambda_{G}$ on $\mathrm{H}_{\mathrm{cb}}^{2}(G, \mathbb{R})$ by
$$\lambda_{G}\left(\kappa_{G, i}^{\mathrm{b}}\right)=\mathrm{r}_{\mathcal{X}_{i}} .$$
Let $\kappa_{\Sigma}^{\mathrm{b}} \in \mathrm{H}_{\mathrm{b}}^{2}\left(\pi_{1}(\Sigma), \mathbb{R}\right)$ denote the real class which is the image of $\kappa_{\Sigma, \mathbb{Z}}^{\mathrm{b}}$ by change of coefficients. Then it follows from our results obtained so far that:

Corollary 8.6. For a homomorphism $\rho: \pi_{1}(\Sigma) \rightarrow G$ the following are equivalent:
\begin{itemize}
\item[(1)] $\rho$ is maximal:
\item[(2)] $\rho^{*}(\kappa)=\lambda_{G}(\kappa) \kappa_{\Sigma}^{\mathrm{b}}$ for all $\kappa \in \mathrm{H}_{\mathrm{cb}}^{2}(G, \mathbb{R})$.
\end{itemize}

Let now $\mathcal{D}$ be the bounded symmetric domain associated to $G, \check{S}$ its Shilov boundary and $Q$ the stabilizer of some point in $\check{S}$; let $e_{G}$ be the exponent of the finite group $Q / Q^{\circ}$. We will furthermore denote by $\operatorname{Hom}_{\text {max }}\left(\pi_{1}(\Sigma), G\right)$ the set of maximal representations of $\pi_{1}(\Sigma)$ into $G$.

Let $\kappa \in \widehat{\mathrm{H}}_{\mathrm{cb}}^{2}(G, \mathbb{Z})$ and $\rho_{0}: \pi_{1}(\Sigma) \rightarrow G$ a maximal representation then Theorem 13 states that for every maximal representation $\rho: \pi_{1}(\Sigma) \rightarrow G$ the map
$$\begin{aligned}
\mathrm{R}_{\kappa}^{\rho_{0}}(\rho): \pi_{1}(\Sigma) & \rightarrow \mathbb{R} / \mathbb{Z} \\
\gamma & \mapsto \operatorname{Rot}_{\kappa}(\rho(\gamma))-\operatorname{Rot}_{\kappa}\left(\rho_{0}(\gamma)\right)
\end{aligned}$$
is a homomorphism, which takes values in $e_{G}^{-1} \mathbb{Z} / \mathbb{Z}$ if $\mathcal{D}$ is of tube type.

Before we turn now to the proof of Theorem 13 we give an example and state a few preliminary lemmas.

Example 8.7. Let $V$ be a real symplectic vector space of dimension $2 n$. Let $K=\mathrm{U}(V, J)$ be the maximal compact subgroup of $\operatorname{Sp}(V)$ given by the choice of a compatible complex structure $J$ on $V$, $\operatorname{det}: K \rightarrow \mathbb{T}$ the complex determinant and let $\kappa \in \widehat{\mathrm{H}}_{\mathrm{cb}}^{2}(\operatorname{Sp}(V), \mathbb{Z})$ be the bounded integer class associated to the homomorphism $u: K \rightarrow \mathbb{R} / \mathbb{Z}$, where $e^{2 \pi i u}=\operatorname{det}$.

When $n=1$, the associated rotation number $\operatorname{Rot}_{\kappa}(\rho): \pi_{1}(\Sigma) \rightarrow$ $\mathbb{Z} / 2 \mathbb{Z}, \gamma \mapsto \operatorname{Rot}_{\kappa}(\rho(\gamma))$ associates to an element $\gamma \in \pi_{1}(\Sigma)$ the sign of the eigenvalue of $\rho(\gamma) \in \operatorname{Sp}(V) \cong \operatorname{SL}(2, \mathbb{R})$. In particular, $\operatorname{Rot}_{\kappa}(\rho)$ itself is not a homomorphism.

On the other hand, when $n$ is even, let $\Delta: \operatorname{SL}(2, \mathbb{R}) \rightarrow \operatorname{Sp}(V)$ be the homomorphism corresponding to a diagonal disk $\mathbb{D} \rightarrow \mathcal{X}$, and choose a hyperbolization $h: \pi_{1}(\Sigma) \rightarrow \operatorname{SL}(2, \mathbb{R})$. Setting $\rho_{0}=\Delta \circ h$, we have that $\operatorname{Rot}_{\kappa}\left(\rho_{0}\right)=0$ and hence $\operatorname{Rot}_{\kappa}(\rho)=\mathrm{R}_{\kappa}^{\rho_{0}}(\rho)$ is therefore a homomorphism. This homomorphism is related to the first Stiefel-Whitney class of the following bundle. Let $\mathcal{L}(V)$ the Grassmannian of Lagrangian subspaces in $V$ and $\mathcal{L} \rightarrow \mathcal{L}(V)$ the tautological bundle. In [7] we have shown that if $S=\Gamma \backslash \mathbb{D}$ is a closed hyperbolic surface and $\rho: \Gamma \rightarrow \operatorname{Sp}(V)$ is a maximal representation, the equivariant map
$$\varphi: \partial \mathbb{D} \rightarrow \mathcal{L}(V)$$
in Theorem 8 is continuous. Composing $\varphi$ with the visual map $T_{1} \mathbb{D} \rightarrow$ $\partial \mathbb{D}$ and pulling back the bundle $\mathcal{L}$, we get a vector bundle $\mathcal{L}_{\rho} \rightarrow T_{1} S$ with base the unit tangent bundle of $S$. Then the first Stiefel-Whitney class $w_{1}\left(\mathcal{L}_{\rho}\right) \in \mathrm{H}^{1}\left(T_{1} S, \mathbb{Z} / 2 \mathbb{Z}\right)$ is given by the composition of the projection $\pi_{1}\left(T_{1} S\right) \rightarrow \Gamma$ and $\operatorname{Rot}_{\kappa}(\rho): \Gamma \rightarrow \mathbb{Z} / 2 \mathbb{Z}$.

This example shows that in some cases already $\operatorname{Rot}_{\kappa}(\rho)$ is a homomorphism, whereas in general only the difference $\mathrm{R}_{\kappa}^{\rho_{0}}(\rho)$ for a fixed maximal representation $\rho_{0}$ is a homomorphism, which generalizes the first Stiefel-Whitney class; in fact when $\partial \Sigma \neq \emptyset$, the map $\varphi$ is in general not continuous as the case of $\operatorname{PU}(1,1)$ already shows, and there is no (continuous) bundle in sight.

Lemma 8.8. Let $\rho: \pi_{1}(\Sigma) \rightarrow G$ be a maximal representation. Then for every $\gamma \in \pi_{1}(\Sigma), \rho(\gamma)$ has at least one fixed point in $\check{S}$.

Proof. This follows at once from Theorem 8, more specifically from the strict equivariance of the left continuous map $\varphi: \partial \mathbb{D} \rightarrow \check{S}$. \(\square\)

Lemma 8.9. The restriction map $\mathrm{H}_{\mathrm{cb}}^{2}(G, \mathbb{R}) \rightarrow \mathrm{H}_{\mathrm{cb}}^{2}(Q, \mathbb{R})$ is the zero тар.

Proof. Let $\mathcal{X}=\mathcal{X}_{1} \times \cdots \times \mathcal{X}_{n}$ be a decomposition of the symmetric space associated to $G$ into irreducible factors. Then $\check{S}=\check{S}_{1} \times \cdots \times \check{S}_{n}$, where $\check{S}_{i}$ is the Shilov boundary of $\mathcal{X}_{i}$. Let $p_{i}: \overleftrightarrow{S} \rightarrow \check{S}_{i}$ be the projection onto the $i$-th factor and set $\beta_{\check{S}, i}=p_{i}{ }^{*} \beta_{\check{S}_{i}}$, where $\beta_{\check{S}_{i}}$ is the generalized Maslov cocycle of $\check{S}_{i}$.

Let $\kappa=\sum_{i=1}^{n} \lambda_{i} \kappa_{G, i}^{\mathrm{b}}$, where $\left\{\kappa_{G, i}^{\mathrm{b}}: 1 \leq i \leq n\right\}$ is the basis of $\mathrm{H}_{\mathrm{cb}}^{2}(G, \mathbb{R})$. Applying [9, Corollary 2.3], we have for any $Q$-invariant Borel set $Z \subset \check{S}$ a commutative diagram
![](https://cdn.mathpix.com/cropped/4c2b5273-bae1-4a9e-bc17-559dcbfd0d15-49.jpg?height=221&width=540&top_left_y=829&top_left_x=757)
where the class $\left[\beta:=\sum_{i=1}^{n} \lambda_{i} \beta_{\check{S}, i}\right] \in \mathrm{H}^{2}\left(\mathcal{B}_{\text {alt }}^{\infty}\left(\check{S}^{\bullet}\right)^{Q}\right)$ goes to $\left.\kappa\right|_{Q}$ (see § 2.1.3); taking now $Z$ to be the $Q$-fixed point in $\check{S}$ and observing that $\left.\beta\right|_{Z^{3}}=0$, we get that $\left.\kappa\right|_{Q}=0$. \(\square\)

Lemma 8.10. $\left.\operatorname{Rot}_{\kappa}\right|_{Q}: Q \rightarrow \mathbb{R} / \mathbb{Z}$ is a homomorphism and if $\mathcal{D}$ is of tube type $\operatorname{Rot}_{\kappa}$ is trivial on $Q^{\circ}$, and hence $\operatorname{Rot}_{\kappa}(Q) \subset e_{G}^{-1} \mathbb{Z} / \mathbb{Z}$.

Proof. The first assertion follows from the fact that $\left.\kappa_{\mathbb{R}}\right|_{Q}=0$ (see Lemma 8.9) and from Lemma 7.2(2).

Let $Q=M A_{Q} N_{Q}$ be the Langlands decomposition of $Q$; then $\operatorname{Rot}_{\kappa}$ is trivial on $A_{Q} N_{Q}$ (see Proposition 7.8(1)). Now $M^{\circ}$ is reductive with compact center and we may assume that $\mathcal{Z}\left(M^{\circ}\right) \subset K \cap Q$. If then $\mathcal{D}$ is of tube type, the Lie algebra of $K \cap Q$ is contained in the Lie algebra of $[K, K]$ [37, Theorem 4.11] and since $\left.\operatorname{Rot}_{\kappa}\right|_{K}$ is a homomorphism, it is therefore trivial on $[K, K]$ and hence on $\mathcal{Z}\left(M^{\circ}\right)^{\circ}$. Since $\operatorname{Rot}_{\kappa}$ is also trivial on every connected almost simple factor of $M^{\circ}$, we obtain finally that it is trivial on $Q^{\circ}$. \(\square\)

Proof of Theorem 13. Let $\kappa \in \widehat{\mathrm{H}}_{\mathrm{cb}}^{2}(G, \mathbb{Z})$ and $\rho, \rho_{0}: \pi_{1}(\Sigma) \rightarrow G$ be maximal representations. Corollary 8.6 implies that the real class in $\mathrm{H}_{\mathrm{b}}^{2}\left(\pi_{1}(\Sigma), \mathbb{R}\right)$ which corresponds to $\rho^{*}(\kappa)-\rho(\kappa) \in \mathrm{H}_{\mathrm{b}}^{2}\left(\pi_{1}(\Sigma), \mathbb{Z}\right)$ vanishes and hence
$$\rho^{*}(\kappa)-\rho_{0}^{*}(\kappa)=\delta(h)$$
for a unique homomorphism $h: \pi_{1}(\Sigma) \rightarrow \mathbb{R} / \mathbb{Z}$. Restricting the equality (8.4) to cyclic subgroups, we get
$$\mathrm{R}_{\kappa}^{\rho_{0}}(\rho)=\operatorname{Rot}_{\kappa}(\rho(\gamma))-\operatorname{Rot}_{\kappa}\left(\rho_{0}(\gamma)\right)=h(\gamma)$$
for all $\gamma \in \pi_{1}(\Sigma)$.

Now from Lemma 8.8 we know that every $\rho(\gamma)$ and $\rho_{0}(\gamma)$ is conjugate to an element of $Q$ and thus if $\mathcal{D}$ is of tube type we have from Lemma 8.10 that $\mathrm{R}_{\kappa}^{\rho_{0}}(\rho) \in e_{G}^{-1} \mathbb{Z} / \mathbb{Z}$. The last assertion follows then from the fact that $\operatorname{Rot}_{\kappa}$ is continuous and $\operatorname{Hom}\left(\pi_{1}(\Sigma), e_{G}^{-1} \mathbb{Z} / \mathbb{Z}\right)$ is finite. \(\square\)
8.3. Applications to representation varieties. Let $G$ be a group of Hermitian type. If $\partial \Sigma=\emptyset$, it is well known that $\operatorname{Hom}_{\max }\left(\pi_{1}(\Sigma), G\right)$ is a union of components of Hom $\left(\pi_{1}(\Sigma), G\right)$ and hence if $G$ is real algebraic, the set of maximal representations is a real semialgebraic set. In the case in which $\partial \Sigma \neq \emptyset$, $\operatorname{Hom}\left(\pi_{1}(\Sigma), G\right)$ is connected; it is then necessary to study certain naturally defined subsets of the representation variety.

We assume $\partial \Sigma \neq \emptyset$ and use the presentation in (1.1). Let $\mathcal{C}=$ $\left(\mathcal{C}_{1}, \ldots, \mathcal{C}_{n}\right)$ be a set of conjugacy classes in $G$. Then
$$\operatorname{Hom}^{\mathcal{C}}\left(\pi_{1}(\Sigma), G\right):=\left\{\rho \in \operatorname{Hom}\left(\pi_{1}(\Sigma), G\right): \rho\left(c_{i}\right) \in \mathcal{C}_{i}, 1 \leq i \leq n\right\}$$
is a real semialgebraic set and
Corollary 8.11. For any $\kappa \in \mathrm{H}_{\mathrm{cb}}^{2}(G, \mathbb{R})$ the map $\rho \mapsto \mathrm{T}_{\kappa}(\Sigma, \rho)$ is constant on connected components of $\operatorname{Hom}^{\mathcal{C}}\left(\pi_{1}(\Sigma), G\right)$.
Proof. Since $\mathrm{H}_{\mathrm{cb}}^{2}(G, \mathbb{R})$ is spanned by integral classes (see Proposition 7.7(3)), we may assume that $\kappa$ is integral in which case $\mathrm{T}_{\kappa}(\Sigma, \rho)$ is congruent $\bmod \mathbb{Z}$ to $-\sum_{i=1}^{n} \operatorname{Rot}_{\kappa}\left(\rho\left(\mathrm{c}_{i}\right)\right)$; the latter is then constant for $\rho \in \operatorname{Hom}^{\mathcal{C}}\left(\pi_{1}(\Sigma), G\right)$. Thus, since $\rho \mapsto \mathrm{T}_{\kappa}(\Sigma, \rho)$ is continuous, it is locally constant which proves the corollary. \(\square\)
---
retention_scope: session
part: 4
total_parts: 5
---

[Part 4/5 of: THE FAMILY SEIBERG-WITTEN INVARIANT AND NON-SYMPLECTIC LOOPS OF DIFFEOMORPHISMS]

We first recall the plumbing construction as follows: Let $D^{2} \hookrightarrow V \rightarrow S$ and $D^{2} \hookrightarrow$ $V^{\prime} \rightarrow S^{\prime}$ be two disk bundles over surfaces $S, S^{\prime}$. Take points $x \in S$ and $x^{\prime} \in S^{\prime}$. Let $B$ (resp. $B^{\prime}$ ) be a small neighborhood of $x$ (resp. $x^{\prime}$ ) in $S$ (resp. $S^{\prime}$ ). Fix trivializations
$$\left.V\right|_{B} \cong D^{2} \times B,\left.\quad V\right|_{B^{\prime}} \cong D^{2} \times B^{\prime} .$$
The plumbing of $V, V^{\prime}$ along $x, x^{\prime}$ is defined by gluing $V$ and $V^{\prime}$ together by identifying $\left.V\right|_{B}$ with $\left.V_{i}\right|_{B_{i}}$ in a way that switches the fiber and base directions. We use the notation $(V, x) \sim\left(V^{\prime}, x^{\prime}\right)$ to denote this procedure.

Recall that $p^{-1}(0) \in \widetilde{\mathbb{C}^{2} / \Gamma}$ is a union of -2-spheres $S_{1}, \cdots, S_{n}$ that intersects each other transversely. Let $V_{i}$ be the normal disk bundle of $S_{i}$ in $\widetilde{\mathbb{C}^{2} / \Gamma}$. Since the action (72) preserve $S_{i}$ as a set, it induces an action
$$r_{i}: S^{1} \times V_{i} \rightarrow V_{i} .$$
There is a homeomorphism from $M_{1}$ to the plumbing of $\left\{V_{i}\right\}_{1 \leqslant i \leqslant n}$ (along the intersection points $\left\{S_{i} \cap S_{j}\right\}_{1 \leqslant i<j \leqslant n}$ ). Furthermore, under this homeomorphism, the circle action (72) is obtained by plumbing together $\left\{r_{i}\right\}_{1 \leqslant i \leqslant n}$.

To give an explicit description of $r_{i}$, we fix a complex analytic diffeomorphism
$$l_{i}: \mathbb{C} \cup\{\infty\}=\mathbb{C P}^{1} \cong S_{i}$$
for each $i$. These diffeomorphisms are chosen in a way such that the following conditions hold:
\begin{itemize}
\item[-] For a type-A singularity, we have $l_{i}(\infty)=l_{i+1}(0)$ for $1 \leqslant i \leqslant n-1$. In other words, $S_{i}$ and $S_{i+1}$ intersects each other at a single point $l_{i}(\infty)=l_{i+1}(0)$.
\item[-] For a type-D singularity, we have $l_{i}(\infty)=l_{i+1}(0)$ for $1 \leqslant i \leqslant n-2$ and $l_{n-2}(1)=$ $l_{n}(0)$.
\item[-] For a type-E singularity, we have $l_{i}(\infty)=l_{i+1}(0)$ for $1 \leqslant i \leqslant n-2$ and $l_{n-3}(1)=$ $l_{n}(0)$.
\item[-] For any $i$, both $l_{i}(0)$ and $l_{i}(\infty)$ are fixed under the action $r_{i}$. Since $r_{i}$ must fix points in $S_{i} \cap S_{j}$ (for $j \neq i$ ), this condition is redundant unless the vertex in the Dynkin diagram that corresponds to $S_{i}$ is 1-valent.
\end{itemize}
Using $l_{i}$, we can identify $V_{i}$ with the unit disk bundle associated to $\mathcal{O}(-2)$. There are two natural circle actions. The action
$$r_{(0,1)}^{i}: S^{1} \times V_{i} \rightarrow V_{i}$$
is given by the scalar multiplication on the fibers. And the action
$$r_{(1,-1)}^{i}: S^{1} \times V_{i} \rightarrow V_{i}$$
is induced by the standard circle action on $\mathbb{C P}^{1}=\mathbb{C} \cup \infty$ (Here we identify $\mathcal{O}(-2)$ with $T \mathbb{C P}^{1}$ via an isomorphism that reverses the fiber orientation). Both actions have $0 \in \mathbb{C P}^{1}$ as a fixed point, and the weights are $(0,1)$ and (1, -1) respectively. (Here the first and second component denote weights in the base and the fiber direction respectively.) For any $a, b \in \mathbb{Z}$, we can consider the composition
$$r_{(a, b)}^{i}: S^{1} \times V_{i} \rightarrow V_{i}$$
defined by
$$r_{(a, b)}^{i}(z, x):=r_{(0,1)}^{i}\left(z^{a+b}, r_{(1,-1)}^{i}\left(z^{a}, x\right)\right), \quad \text { for } z \in S^{1}, x \in V .$$
This is a circle action that has 0 as a fix point of weight $(a, b)$. Note that for any $z \in S^{1}$, $r_{i}(z,-): V_{i} \rightarrow V_{i}$ is a bundle automorphism that covers an analytical map $S_{i} \rightarrow S_{i}$ which fixes both 0 and $\infty$. Such action is completely determined by the weights at 0 in the fiber and base direction. Therefore, $r_{i}=r_{\left(a_{i}, b_{i}\right)}^{i}$ for some $a_{i}, b_{i} \in \mathbb{Z}$. In other words, the circle action $\phi$ on $M_{1}$ is obtained by plumbing the circle actions $\left\{r_{\left(a_{i}, b_{i}\right)}^{i}\right\}$ together for some $a_{i}, b_{i}$. Our next task is to find the exact values of them.

Lemma 6.3. (1) The weight of $r_{(a, b)}$ at $\infty$ is $(-a, 2 a+b)$. Again, we put the base direction in the first component and the fiber direction in the second component
(2) Suppose $V_{i}$ and $V_{j}$ are plumbed together along $l_{i}(0) \in S_{i}$ and $l_{j}(\infty) \in S_{j}$. Then we have $\left(a_{j}, b_{j}\right)=\left(2 a_{i}+b_{i},-a_{i}\right)$.
(3) Suppose $V_{i}$ and $V_{j}$ are plumbed together along $l_{i}(1) \in S_{i}$ and $l_{j}(0) \in S_{j}$. Then $\left(a_{i}, b_{i}\right)=$ $(0, k)$ an $\left(a_{j}, b_{j}\right)=(k, 0)$ for some integer $k$.

Proof. (1) From the geometric description of $r_{(0,1)}^{i}$ and $r_{(1,-1)}^{i}$, we see that their weights at $\infty$ are $(0,1)$ and (-1, 1) respectively. So the weight of $r_{(a, b)}$ at $\infty$ is $(-a, 2 a+b)$.
(2) Since the plumbing construction switches the base and the fiber direction, we must have $\left(b^{\prime}, a^{\prime}\right)=(2 a+b,-a)$ if $r_{(a, b)}$ and $r_{\left(a^{\prime}, b^{\prime}\right)}$ can be plumbed together.
(3) Since $r_{\left(a_{i}, b_{i}\right)}^{i}$ fixes $l(0), l(1)$ and $l(\infty)$, it must be trivial when restricted to $S_{i}$. This implies that $\left(a_{i}, b_{i}\right)=(0, k)$ and $\left(a_{j}, b_{j}\right)=(k, 0)$ for some $k$. \(\square\)

Proposition 6.4. The values of $\left\{\left(a_{i}, b_{i}\right)\right\}_{1 \leqslant i \leqslant n}$ are given as follows:
\begin{itemize}
\item[(1)] For an $A_{n}$-singularity, we have $\left(a_{i}, b_{i}\right)=(-n+2 i-1, n-2 i+3)$ for $1 \leqslant i \leqslant n$.
\item[(2)] For a $D_{n}$-singularity, we have $\left(a_{i}, b_{i}\right)=(-2 n+2 i+4,2 n-2 i-2)$ for $1 \leqslant i \leqslant n-1$ and $\left(a_{n}, b_{n}\right)=(2,0)$.
\item[(3)] For an $E_{n}$-singularity, we have $\left(a_{i}, b_{i}\right)=(-2 n+2 i+6,2 n-2 i-4)$ for $1 \leqslant i \leqslant n-1$ and $\left(a_{n}, b_{n}\right)=(2,0)$.
\end{itemize}

Proof. Since $\overline{p^{-1}\left(D\left(\mathbb{C}^{2}\right) \backslash\{0\}\right)}=M_{1}$, the action $\phi$ is determined by its restriction to $p^{-1}\left(D\left(\mathbb{C}^{2}\right) \backslash\{0\}\right)$. Furthermore, suppose we identify $p^{-1}\left(D\left(\mathbb{C}^{2}\right) \backslash\{0\}\right)$ with $\partial M_{1} \times(0,1]$ by sending $p^{-1}(t x)$ to $(x, t)$. Then $\phi$ is trivial on the second component. Therefore, to understand $\phi$, it suffices to understand its restriction to $\partial M_{1}$, which is just the circle action
$$\phi^{\prime}: S^{1} \times\left(S\left(\mathbb{C}^{2}\right) / \Gamma\right) \rightarrow\left(S\left(\mathbb{C}^{2}\right) / \Gamma\right)$$
defined by
$$\phi^{\prime}\left(e^{\mathrm{i} \theta},\left[\left(z_{1}, z_{2}\right)\right]\right)=\left[\left(e^{\mathrm{i} \theta} z_{1}, e^{\mathrm{i} \theta} z_{2}\right)\right] .$$
This circle action gives $S\left(\mathbb{C}^{2}\right) / \Gamma$ the structure of a Seifert fibered space. Each fiber (regular or singular) is an orbit by itself. The isotropy group for a regular fiber is the group $\Gamma \cap\left\{\left(\begin{array}{cc}e^{\mathrm{i} \theta} & 0 \\ 0 & e^{\mathrm{i} \theta}\end{array}\right)\right\}$. This group is trivial for an $A_{n}$-singularity with $n$ even and is $\mathbb{Z} / 2$ otherwise.

For a $D_{n}$ singularity, $v_{n-2}$ is the unique 3-valent vertex in the Dynkin diagram. Take a fiber of the corresponding disk bundle $V_{n-2}$. Then the boundary of this fiber is a regular fiber of $S\left(\mathbb{C}^{2}\right) / \Gamma$. Since any regular fiber is an orbit with isotropy group $\mathbb{Z} / 2$, we see that $\left(a_{n-2}, b_{n-2}\right)=(0,2)$. (We don't have (0, -2) here because we are using the complex orientation to orient the fibers.) The value of $\left(a_{i}, b_{i}\right)$ for $i \neq n-2$ is determined by Lemma 6.3. This finishes the proof of (2). The proof of (3) is completely analogues. And $v_{n-3}$ is the unique 3-valent vertex in this case.

Now we prove (1). For an $A_{n}$-singularity, we have
$$\Gamma=\left\{\left(\begin{array}{cc}
e^{\frac{2 k \pi \mathrm{i}}{n+1}} & 0 \\
0 & \left.e^{-\frac{2 k \pi \mathrm{i}}{n+1}}\right)
\end{array}\right\}_{k \in \mathbb{Z}},\right.$$
and $\partial M_{1}=S\left(\mathbb{C}^{2}\right) / \Gamma$ is the lens space $L(n+1,-1)$. Suppose $n=1$. Then there are no singular fibers. Same argument as before shows that $\left(a_{1}, b_{1}\right)=(0,2)$. Now suppose $n \geqslant 2$, then there are two singular fibers $\left\{\left[\left(e^{\mathrm{i} \theta}, 0\right)\right]\right\}_{\theta}$ and $\left\{\left[\left(0, e^{\mathrm{i} \theta}\right)\right]\right\}_{\theta}$. For points on these two fibers, the isotropy group is $\mathbb{Z} /(n+1)$, which is strictly larger than the isotropy group of points on regular fibers, which is either trivial or $\mathbb{Z} / 2$. Now we consider the fiber of $V_{1}$ over $l_{1}(0)$ and the fiber of $V_{n}$ over $l_{n}(\infty)$. Denote their boundaries by $F_{1}$ and $F_{n}$. By our assumption that $l_{1}(0)$ and $l_{1}(\infty)$ are fixed points of $r, F_{1}$ and $F_{n}$ are orbits of the circle action on $\partial M_{1}$. Furthermore, from the plumbing description of $\phi$, we see that they are the only orbits whose isotropy group can possibly be larger then orbits near by. (Boundaries of the fibers over $l_{i}(0)$ with $i>1$ or $l_{i}(\infty)$ with $i<n$ also have this property, but they are
contained in the interior of $M_{1}$.) Therefore, we see that $F_{0}, F_{1}$ are exactly the two singular fibers and points on them have isotropy group $\mathbb{Z} /(n+1)$. In particular, this implies that the weights of $\phi$ at $l_{1}(0)$ and $l_{n}(\infty)$ are $(c, n+1)$ and $\left(c^{\prime}, n+1\right)$ for some $c, c^{\prime} \in \mathbb{Z}$. By Lemma 6.3 (1), this implies
$$b_{1}=2 a_{n}+b_{n}=n+1 .$$
Putting this equation with the equations
$$\left(a_{i+1}, b_{i+1}\right)=\left(2 a_{i}+b_{i},-a_{i}\right) \text { for } 1 \leqslant i \leqslant n-1$$
provided by Lemma 6.3 (2), one can solve that $\left(a_{i}, b_{i}\right)=(-n+2 i-1, n-2 i+3)$. This finishes the proof. \(\square\)

Since the circle action $\phi$ fixes $S_{i}$ as a subset, we obtain a 4-dimensional submanifold $\widetilde{S}_{i}$ of $\widetilde{M}_{1}$ by putting together $S_{i}$ in all fibers. A simple application of the Serre spectral sequence shows that $H_{4}\left(\widetilde{M}_{1} ; \mathbb{Z}\right)$ is a free abelian group generated by $\left\{\left[\widetilde{S}_{i}\right]\right\}_{1 \leqslant i \leqslant n}$.

Lemma 6.5. (1) The triple self-intersection number $\widetilde{S}_{i} \cdot \widetilde{S}_{i} \cdot \widetilde{S}_{i}=8$ for any $i$. (2) Suppose $S_{i}$ and $S_{j}$ intersects each other at $x \in S_{i}$. And suppose the weight of the circle $\phi$ action on $T_{x} S_{i}$ equals $k$. Then $\widetilde{S}_{i} \cdot \widetilde{S}_{j} \cdot \widetilde{S}_{j}=-k$. (3) We have $\left\langle p_{1}\left(T \widetilde{M}_{1} / \mathcal{Q}\right),\left[\widetilde{S}_{i}\right]\right\rangle=8$.

Proof. We have a fiber bundle $S_{i} \hookrightarrow \widetilde{S}_{i} \rightarrow S^{2}$ and the clutching function is the restriction of $\phi$. A fixed point $p$ of $\phi$ gives a section of the bundle $\widetilde{S}_{i}$. The image of this section, denoted by $\Sigma_{p}$, is a 2-dimensional submanifold of $\widetilde{S}_{i}$. The normal bundle of $\Sigma_{p}$ in $\widetilde{S}_{i}$, denoted by $N_{\Sigma_{p}} \widetilde{S}_{i}$, has Euler number $-k$, where $k$ is the weight of $\phi$ on $T_{p} S_{i}$. (See Remark 9.)

To prove (1), we set $p=l_{i}(0)$. Since the weight of $\phi$ on $T_{p} S_{i}$ equals $a_{i}$, we have
$$\widetilde{S}_{i} \cong\left\{\begin{array}{ll}
S^{2} \times S^{2} & \text { if } a_{i} \text { is even } \\
\mathbb{C P}^{2} \# \overline{\mathbb{C P}} \mathbb{P}^{2} & \text { if } a_{i} \text { is odd }
\end{array} .\right.$$
In any case, $\left\{\left[S_{i}\right],\left[\Sigma_{p}\right]\right\}$ is a basis of $H_{2}\left(\widetilde{S}_{i} ; \mathbb{Q}\right)$. Their intersection numbers in $\widetilde{S}_{i}$ are given by
$$S_{i} \cdot S_{i}=0, \quad \Sigma_{p} \cdot \Sigma_{p}=-a_{i}, \quad S_{i} \cdot \Sigma_{p}=1 .$$
Let $N$ be the normal bundle of $\widetilde{S}_{i}$ in $\widetilde{M}_{1}$. Then $\left.N\right|_{S_{i}}$ has Euler number -2 (because $S_{i}$ is a -2 sphere) and $\left.N\right|_{\Sigma_{p}}$ has Euler number $-b_{i}$. By (75), we get
$$e(N)=\operatorname{PD}\left(-2\left[\Sigma_{p}\right]-\left(2 a_{i}+b_{i}\right)\left[S_{i}\right]\right) .$$
Therefore, we get
$$\widetilde{S}_{i} \cdot \widetilde{S}_{i} \cdot \widetilde{S}_{i}=\left\langle e(N)^{2},\left[\widetilde{S}_{i}\right]\right\rangle=4\left(a_{i}+b_{i}\right)=8 .$$

To prove (2), we set $p=x$. Note that $\widetilde{S}_{i}$ and $\widetilde{S}_{j}$ intersect each other transversely at $\Sigma_{p}$. So $\widetilde{S}_{i} \cdot \widetilde{S}_{j} \cdot \widetilde{S}_{j}$ equals the self-intersection of $\Sigma_{p}$ in $\widetilde{S}_{i}$, which is $-k$.

Now we prove (3). We have a decomposition
$$\left.\left(T \widetilde{M}_{1} / \mathcal{Q}\right)\right|_{\widetilde{S}_{i}}=\left(T \widetilde{S}_{i} / \mathcal{Q}\right) \oplus N_{\widetilde{S}_{i}} \widetilde{M}_{1} .$$

Here $T \widetilde{S}_{i} / \mathcal{Q}$ denotes the vertical tangle bundle of the fiber bundle $S_{i} \hookrightarrow \widetilde{S}_{i} \rightarrow \mathcal{Q}$. This implies that
$$p_{1}\left(\left.\left(T \widetilde{M}_{1} / \mathcal{Q}\right)\right|_{\widetilde{S}_{i}}\right)=e\left(N_{\widetilde{S}_{i}} \widetilde{M}_{1}\right)^{2}+e\left(T \widetilde{S}_{i} / \mathcal{Q}\right)^{2} .$$

Set $p=l_{i}(0)$. Then we have $\chi\left(\left.\left(T \widetilde{S}_{i} / \mathcal{Q}\right)\right|_{S_{i}}\right)=\chi\left(T S_{i}\right)=2$ and $\chi\left(\left.T \widetilde{S}_{i}\right|_{\Sigma_{p}}\right)=-a_{i}$. By the same argument as (2), we see that
$$e\left(T \widetilde{S}_{i} / \mathcal{Q}\right)=\operatorname{PD}\left(2\left[\Sigma_{p}\right]+a_{i}\left[S_{i}\right]\right) .$$

This implies
$$\left\langle e\left(T \widetilde{S}_{i} / \mathcal{Q}\right)^{2},\left[\widetilde{S}_{i}\right]\right\rangle=0 .$$
Hence we have
$$\left\langle p_{1}\left(T \widetilde{M}_{1} / \mathcal{Q}\right),\left[\widetilde{S}_{i}\right]\right\rangle=\left\langle e\left(N_{\widetilde{S}_{i}} \widetilde{M}_{1}\right)^{2},\left[\widetilde{S}_{i}\right]\right\rangle=\widetilde{S}_{i} \cdot \widetilde{S}_{i} \cdot \widetilde{S}_{i}=8 .$$ \(\square\)

Remark 10. The ADE family $\widetilde{M} / Q$ is always topologically nontrivial because the total space $\widetilde{M}$ is not homotopy equivalent to $M \times \mathcal{Q}$. To see this, we note that for any $\alpha \in$ $H_{4}(M \times \mathcal{Q} ; \mathbb{Z})$, the triple self-intersection number $\alpha \cdot \alpha \cdot \alpha$ is always divisible by 3 (this can be seen using the Künneth formula). However, this condition is not satisfied for $\widetilde{M}$ because $\widetilde{S}_{i} \cdot \widetilde{S}_{i} \cdot \widetilde{S}_{i}=8$. Similarly, one can show that the blown-up family is also topologically nontrivial. (See Lemma 7.1.)

Given any $r=\left(t_{1}, \cdots, t_{n}\right) \in \mathbb{Z}^{n}$, we let $S_{r}$ be the formal linear combination $t_{1} S_{1}+\cdots+$ $t_{n} S_{n}$. Similarly, we let $\widetilde{S}_{r}=t_{1} \widetilde{S}_{1}+\cdots+t_{n} \widetilde{S}_{n}$.
Proposition 6.6. Let $\widetilde{M}=\widetilde{M}_{1} \cup\left(\mathcal{Q} \times M_{2}\right)$ be an ADE family with fiber $M=M_{1} \cup M_{2}$. Let $\widetilde{\mathfrak{s}}$ be a family spin ${ }^{c}$ structure on $\widetilde{M}$ that satisfies
$$\operatorname{PD}\left(c_{1}\left(\left.\widetilde{\mathfrak{s}}\right|_{\widetilde{M}_{1}}\right)\right)=2\left[\widetilde{S}_{r}\right] \in H_{4}\left(\widetilde{M}_{1}, \partial \widetilde{M}_{1} ; \mathbb{Z}\right)$$
for some root $r$. Then
$$\left\langle c_{1}\left(\operatorname{Ind}\left(\not D^{+}(\widetilde{M}, \widetilde{\mathfrak{s}})\right)\right),[\mathcal{Q}]\right\rangle= \pm 1 .$$
Proof. By the family Atiyah-Singer index theorem, one has
$$\begin{aligned}
\left\langle c_{1}\left(\operatorname{Ind}\left(\not D^{+}(\widetilde{M}, \widetilde{\mathfrak{s}})\right)\right),[\mathcal{Q}]\right\rangle & =\left\langle e^{\frac{c_{1}(\mathfrak{s})}{2}} \cdot \hat{A}(T \widetilde{M} / \mathcal{Q}),[\widetilde{M}]\right\rangle \\
& =\left\langle\left(1+\frac{c_{1}(\widetilde{\mathfrak{s}})}{2}+\frac{c_{1}(\widetilde{\mathfrak{s}})^{2}}{8}+\frac{c_{1}(\widetilde{\mathfrak{s}})^{3}}{48}\right) \cup\left(1-\frac{p_{1}(T \widetilde{M} / \mathcal{Q})}{24}\right),[\widetilde{M}]\right\rangle \\
& =\frac{\left\langle c_{1}(\widetilde{\mathfrak{s}})^{3}-p_{1}(T \widetilde{M} / \mathcal{Q}) c_{1}(\widetilde{\mathfrak{s}}),[\widetilde{M}]\right\rangle}{48} .
\end{aligned}$$
By (76), we have $c_{1}(\widetilde{\mathfrak{s}})=\operatorname{PD}\left(2\left[\widetilde{S}_{r}\right]+\widetilde{\beta}\right)$, where $\widetilde{\beta}$ the image of $\beta \times[\mathcal{Q}]$ under the map $H_{4}\left(M_{2} ; \mathbb{Z}\right) \rightarrow H_{4}(M ; \mathbb{Z})$ for some $\beta \in H_{2}(M ; \mathbb{Z})$. As a result, we get
$$\left\langle c_{1}\left(\operatorname{Ind}\left(\not D^{+}(\widetilde{M}, \widetilde{\mathfrak{s}})\right)\right),[\mathcal{Q}]\right\rangle=\frac{4\left[\widetilde{S}_{r}\right] \cdot\left[\widetilde{S}_{r}\right] \cdot\left[\widetilde{S}_{r}\right]-\left\langle p_{1}(T \widetilde{M} / \mathcal{Q}),\left[\widetilde{S}_{r}\right]\right\rangle}{24}$$

We consider the function
$$f\left(t_{1}, \cdots, t_{n}\right):=\sum_{1 \leqslant i \leqslant n} 8\left(4 t_{i}^{3}-t_{i}\right)-\sum_{\{\{i, j\}\} \mid i \leftrightarrow j\}} 12 t_{i} t_{j}\left(t_{i} w_{j, i}+t_{j} w_{i, j}\right) .$$
Here we use the $i \leftrightarrow j$ to denote the condition that there is an edge in the Dynkin diagram that connects the vertices $v_{i}$ and $v_{j}$, and we use $w_{i, j}$ denotes the weight of the circle action on the tangent space $T_{S_{i} \cap S_{j}} S_{i}$.

Suppose $r=\left(t_{1}, \cdots, t_{n}\right)$. Then by Lemma 6.5, we have
$$4\left[\widetilde{S}_{r}\right] \cdot\left[\widetilde{S}_{r}\right] \cdot\left[\widetilde{S}_{r}\right]-\left\langle p_{1}(T \widetilde{M} / \mathcal{Q}),\left[\widetilde{S}_{r}\right]\right\rangle=f\left(t_{1}, \cdots, t_{n}\right)$$
So it suffices to show that
$$f\left(t_{1}, \cdots, t_{n}\right)= \pm 24$$
for any root $r=\left(t_{1}, \cdots t_{n}\right)$.
By changing the sign of $r$, we may assume that it is a positive root (i.e. $t_{i} \geqslant 0$ for all i.) It is obvious that $f(0, \cdots, 0,1,0, \cdots, 0)=24$. So (78) holds for simple roots. Since the Hasse diagram for ADE Dynkin diagram is connected (see, for example, [36]), for any positive root $r$, there exists a sequence $r_{1}, \cdots r_{m}$ of positive roots such that $r_{1}=r, r_{m}$ is simple, and
$$r_{i}-r_{i+1}= \pm(0, \cdots, 1, \cdots, 0) .$$
Therefore, the proof is finished by the following lemma. \(\square\)

Lemma 6.7. Suppose $r=\left(t_{1}, \cdots, t_{k}, \cdots, t_{n}\right)$ and $r^{\prime}=\left(t_{1}, \cdots, t_{k}+1, \cdots, t_{n}\right)$ are both roots. Then $f(r)=f\left(r^{\prime}\right)$.

Proof. Note that we always have
$$w_{i, j}+w_{j, i}=a_{i}+b_{i}=2 .$$
Also note that since $r \cdot r=r^{\prime} \cdot r^{\prime}$, we have
$$2 t_{k}^{2}-\sum_{\{j \mid j \leftrightarrow k\}} 2 t_{k} t_{j}=2\left(t_{k}+1\right)^{2}-\sum_{\{j \mid j \leftrightarrow k\}} 2\left(t_{k}+1\right) t_{j},$$
which implies
$$2 t_{k}+1=\sum_{\{j \mid j \leftrightarrow k\}} t_{j} .$$

It is straightforward to compute that
$$f\left(r^{\prime}\right)-f(r)=24\left(2 t_{k}+1\right)^{2}-\sum_{\{j \mid j \leftrightarrow k\}} 12\left(t_{j} w_{j, k}\left(2 t_{k}+1\right)+t_{j}^{2} w_{k, j}\right) .$$
Suppose the vertex $v_{k}$ is 3 -valent. Then there are three vertices that are connected to $v_{k}$, and for each of them, we have $w_{k, j}=0$ and $w_{j, k}=2$. Therefore, we get
$$f\left(r^{\prime}\right)-f(r)=24\left(2 t_{k}+1\right)^{2}-\sum_{\{j \mid j \leftrightarrow k\}} 24 t_{j}\left(2 t_{k}+1\right)=24\left(2 t_{k}+1\right)\left(2 t_{k}+1-\sum_{\{j \mid j \leftrightarrow k\}} t_{j}\right)=0 .$$
Suppose the vertex $v_{k}$ is 2-valent and connected to $v_{j}$ and $v_{j^{\prime}}$. Then by Lemma 6.3, we have
$$w_{k, j}+w_{k, j^{\prime}}=a_{i}+\left(-a_{i}\right)=0 .$$

Let $w=w_{k, j}$. Then $w_{j, k}=2-w$ and $w_{j^{\prime}, k}=2+w$ and we have
$$\begin{aligned}
f\left(r^{\prime}\right)-f(r) & =24\left(2 t_{k}+1\right)^{2}-12\left(t_{j}(2-w)\left(2 t_{k}+1\right)+t_{j}^{2} w+t_{j^{\prime}}(2+w)\left(2 t_{k}+1\right)-t_{j^{\prime}}^{2} w\right) \\
& =24\left(2 t_{k}+1\right)^{2}-12\left(2\left(t_{j}+t_{j^{\prime}}\right)\left(2 t_{k}+1\right)-w\left(2 t_{k}+1\right)\left(t_{j}-t_{j^{\prime}}\right)+w\left(t_{j}^{2}-t_{j^{\prime}}^{2}\right)\right) \\
& =24\left(2 t_{k}+1\right)^{2}-12\left(2\left(2 t_{k}+1\right)\left(2 t_{k}+1\right)-w\left(t_{j}+t_{j^{\prime}}\right)\left(t_{j}-t_{j^{\prime}}\right)+w\left(t_{j}^{2}-t_{j^{\prime}}^{2}\right)\right) \\
& =0 .
\end{aligned}$$
Suppose $v_{k}$ is 1-valent and connected to $v_{j}$. Then $t_{j}=2 t_{k}+1$ and we have
$$f\left(r^{\prime}\right)-f(r)=24\left(2 t_{k}+1\right)^{2}-12\left(2 t_{k}+1\right)^{2}\left(w_{k, j}+w_{j, k}\right)=0 .$$ \(\square\)

\section*{7. The blown-up family}

Let $M \hookrightarrow \widetilde{M} \rightarrow \mathcal{Q}$ be a blown-up family as defined in Section 1, with fiber $M=$ $M^{\prime} \# \overline{\mathbb{C P}^{2}}$. Then we have a decomposition
$$\widetilde{M}=\widetilde{M}_{1} \cup \widetilde{M}_{2}$$
where $\widetilde{M}_{1}$ is a nontrivial family with fiber $M_{1}=\overline{\mathbb{C P} \mathbb{P}^{2}} \backslash D^{4}$ and $\widetilde{M}_{2}$ is the trivial family with fiber $M_{2}=M^{\prime}-\stackrel{\circ}{D}^{4}$. We use $S$ to denote the exceptional divisor in the fiber $M$ and use $\widetilde{S}$ to denote submanifold of $\widetilde{M}$ formed by the union of the exceptional divisors on all fibers.
Lemma 7.1. (1) The triple self-intersection $\widetilde{S} \cdot \widetilde{S} \cdot \widetilde{S}=2$.
(2) We have $\left\langle p_{1}(T \widetilde{M} / \mathcal{Q}),[\widetilde{S}]\right\rangle=2$.

Proof. (1) By the same argument as Lemma 6.1, we can choose the clutching function for $\widetilde{M}$ so that in a tubular neighborhood of $S$, it is a circle action that fixes $S$ pointwisely and has weight 1 on its normal bundle in $M$. Therefore, $\widetilde{S}$ is diffeomorphic to $S \times \mathcal{Q}$ and its second homology is generated by $S$ and $\Sigma:=* \times \mathcal{Q}$. By Remark 9, we have
$$\chi\left(\left.N_{\widetilde{S}} \widetilde{M}\right|_{\Sigma}\right)=-1$$
and we also have
$$\chi\left(\left.\left(N_{\widetilde{S}} \widetilde{M}\right)\right|_{S}\right)=\chi\left(N_{S} M\right)=S \cdot S=-1 .$$
This implies that $e\left(N_{\widetilde{S}} \widetilde{M}\right)=-\operatorname{PD}([S]+[\Sigma])$ and that
$$\widetilde{S} \cdot \widetilde{S} \cdot \widetilde{S}=\left\langle e\left(N_{\widetilde{S}} \widetilde{M}\right)^{2},[\widetilde{S}]\right\rangle=2 .$$
(2) We have
$$p_{1}\left(T \widetilde{M} /\left.\mathcal{Q}\right|_{\widetilde{S}}\right)=e\left(N_{\widetilde{S}} \widetilde{M}\right)^{2}+e(T \widetilde{S} / \mathcal{Q})^{2} .$$
where $T \widetilde{S} / \mathcal{Q}$ denotes the vertical tangent bundle of $S \rightarrow \widetilde{S} \rightarrow \mathcal{Q}$. Since this bundle is trivial, we have $e(T \widetilde{S} / \mathcal{Q})^{2}=0$. This implies
$$\left\langle p_{1}\left(T \widetilde{M} /\left.\mathcal{Q}\right|_{\widetilde{S}}\right),[\widetilde{S}]\right\rangle=\left\langle e\left(N_{\widetilde{S}} \widetilde{M}\right)^{2},[\widetilde{S}]\right\rangle=2 .$$ \(\square\)

Proposition 7.2. Let $\widetilde{\mathfrak{s}}$ be a family $\operatorname{spin}^{c}$ structure on $\widetilde{M}$ such that $c_{1}\left(\left.\widetilde{\mathfrak{s}}\right|_{\widetilde{M_{1}}}\right)=-3 \operatorname{PD}[\widetilde{S}]$. Then
$$\left\langle c_{1}\left(\operatorname{Ind}\left(\not D^{+}(\widetilde{M}, \widetilde{\mathfrak{s}})\right)\right),[\mathcal{Q}]\right\rangle=-1 .$$

Proof. The proof is similar to Proposition 6.6. By the Atiyah-Singer index theorem, one has
$$\begin{aligned}
\left\langle c_{1}\left(\operatorname{Ind}\left(\not D^{+}(\widetilde{M}, \widetilde{\mathfrak{s}})\right)\right),[\mathcal{Q}]\right\rangle & =\left\langle e^{\frac{c_{1}(\widetilde{\mathfrak{s l}})}{2}} \cdot \hat{A}(T \widetilde{M} / \mathcal{Q}),[\widetilde{M}]\right\rangle \\
& =\left\langle\left(1+\frac{c_{1}(\widetilde{\mathfrak{s}})}{2}+\frac{c_{1}(\widetilde{\mathfrak{s}})^{2}}{8}+\frac{c_{1}(\widetilde{\mathfrak{s}})^{3}}{48}\right) \cup\left(1-\frac{p_{1}(T \widetilde{M} / \mathcal{Q})}{24}\right),[\widetilde{M}]\right\rangle \\
& =\frac{-27 \widetilde{S} \cdot \widetilde{S} \cdot \widetilde{S}+3\left\langle p_{1}(T \widetilde{M} / \mathcal{Q}),[\widetilde{S}]\right\rangle}{48}=-1 .
\end{aligned}$$ \(\square\)

\section*{8. Symplectic structures on the ADE family and the blown-up family}

In this section, we study the existence of fiberwise symplectic structures on the ADE families and the blown-up families through the calculations we did the previous two sections. The following lemma is an improvement of Lemma 2.9 without the assumption that $b_{1}(M)=0$.
Lemma 8.1. Let $\widetilde{M} / \mathcal{Q}$ be an ADE family or a blown-up family. Then any $\operatorname{spin}^{c}$ structure on the fiber $M$ can be extended to a family $\operatorname{spin}^{c}$ structure on $\widetilde{M} / \mathcal{Q}$. Furthermore, any two such extensions are related to each other by a twist of a complex line bundle $L$ pulled back from $\mathcal{Q}$
Proof. Consider the cohomology Serre spectral sequence for $\widetilde{M} / \mathcal{Q}$ and the differential,
$$d_{2}^{0,2}: H^{0}\left(\mathcal{Q} ; H^{2}(M ; \mathbb{Z})\right) \rightarrow H^{2}\left(\mathcal{Q} ; H^{1}(M ; \mathbb{Z})\right) .$$
Because $H^{1}(M ; \mathbb{Z}) \rightarrow H^{1}\left(M_{2} ; \mathbb{Z}\right)$ is injective and the corresponding differential for the trivial bundle $\widetilde{M}_{2} / \mathcal{Q}$ is trivial. This gives the short exact sequence
$$0 \rightarrow H^{2}(\mathcal{Q} ; \mathbb{Z}) \xrightarrow{p^{*}} H^{2}(\widetilde{M} ; \mathbb{Z}) \xrightarrow{i^{*}} H^{2}(M ; \mathbb{Z}) \rightarrow 0 .$$
A similar argument implies the short exact sequence
$$0 \rightarrow H^{2}(\mathcal{Q} ; \mathbb{Z} / 2) \xrightarrow{p^{*}} H^{2}(\widetilde{M} ; \mathbb{Z} / 2) \xrightarrow{i^{*}} H^{2}(M ; \mathbb{Z} / 2) \rightarrow 0 .$$
We first prove that $\widetilde{M} / \mathcal{Q}$ does have a family $\operatorname{spin}^{c}$ structure. Let $\widetilde{w}_{2}(\widetilde{M} / \mathcal{Q})$ be the second Stiefel-Whitney class of the vertical tangent bundle $T \widetilde{M} / \mathcal{Q}$. Since any 4-manifold has a $\operatorname{spin}^{c}$ structure, $i^{*}\left(\widetilde{w}_{2}(\widetilde{M} / \mathcal{Q})\right)=\omega_{2}(M)$ is the reduction of a class $c \in H^{2}(M ; \mathbb{Z})$. By (81), there exists $\widetilde{c} \in H^{2}(\widetilde{M} ; \mathbb{Z})$ such that $i^{*}(\widetilde{c})=c$. Let $\widetilde{w}$ be the mod-2 reduction of $\widetilde{c}$. Then $i^{*}(\widetilde{w})=i^{*}\left(\widetilde{w}_{2}(\widetilde{M} / \mathcal{Q})\right)$. By (82), $\widetilde{w}=\widetilde{w}_{2}(\widetilde{M} / \mathcal{Q})+p^{*}\left(w^{\prime}\right)$ for some $w^{\prime} \in H^{2}(\mathcal{Q} ; \mathbb{Z} / 2)$. Let $c^{\prime}$ be an element in $H^{2}(\mathcal{Q} ; \mathbb{Z})$ which reduces to $w^{\prime}$. Then the mod-2 reduction of $\widetilde{c}-p^{*}\left(c^{\prime}\right)$ is exactly $\widetilde{w}_{2}(\widetilde{M} / \mathcal{Q})$. Therefore, the family $\widetilde{M} / \mathcal{Q}$ has a $\operatorname{spin}^{c}$ structure.

Let $\mathfrak{s}$ be a spin ${ }^{c}$ structure on the fiber $M$. Take any family spin ${ }^{c}$ structure $\widetilde{\mathfrak{s}}$. Let $\beta=\left.\widetilde{\mathfrak{s}}\right|_{M}-\mathfrak{s} \in H^{2}(M ; \mathbb{Z})$. By (81), there exists $\widetilde{\beta} \in H^{2}(\widetilde{M} ; \mathbb{Z})$ such that $i^{*}(\widetilde{\beta})=\beta$. Then $\widetilde{\mathfrak{s}}+\tilde{\beta}$ is an extension of $\mathfrak{s}$.

Suppose $\mathfrak{s}_{\widetilde{M}}^{1}$ and $\mathfrak{s}_{\widetilde{M}}^{2}$ are two extensions of $\widetilde{\mathfrak{s}}$. Then $i^{*}\left(\mathfrak{s}_{\widetilde{M}}^{1}-\mathfrak{s}_{\widetilde{M}}^{2}\right)=0$. By (81), there exists some complex line bundle $L$ over $\mathcal{Q}$ such that $\mathfrak{s}_{\widetilde{M}}^{1}$ and $\mathfrak{s}_{\widetilde{M}}^{2}$ are related by a twist with $p^{*}(L)$. \(\square\)

Proposition 8.2. Let $\widetilde{M} / \mathcal{Q}$ be an ADE family. Let $\mathfrak{s}$ be a $\operatorname{spin}^{c}$ structure on the fiber $M$ that satisfies $d(\mathfrak{s}, M)=0$ and $c_{1}\left(\left.\mathfrak{s}\right|_{M_{1}}\right)=0$. Let $\widetilde{\mathfrak{s}}$ be any family spin ${ }^{c}$ structure on $\widetilde{M} / \mathcal{Q}$ such that $d(\widetilde{\mathfrak{s}}, \widetilde{M})=0$ and $\left.\widetilde{\mathfrak{s}}\right|_{M_{2}}=\left.\mathfrak{s}\right|_{M_{2}}$. Then we have
$$\operatorname{FSW}(\widetilde{M} / \mathcal{Q}, \widetilde{\mathfrak{s}})= \pm \operatorname{SW}(M, \mathfrak{s})$$
when $b_{2}^{+}(M)>1$ and we have
$$\operatorname{FSW}_{+}(\widetilde{M} / \mathcal{Q}, \widetilde{\mathfrak{s}})= \pm \operatorname{SW}(M, \mathfrak{s}), \quad \operatorname{FSW}_{-}(\widetilde{M} / \mathcal{Q}, \widetilde{\mathfrak{s}})= \pm \operatorname{SW}_{-}(M, \mathfrak{s})$$
when $b_{2}^{+}(M)=1$.
Proof. We use $\mathfrak{s}_{M}^{\prime}$ to denote $\left.\widetilde{\mathfrak{s}}\right|_{M}$. Since $\left.\mathfrak{s}_{M}^{\prime}\right|_{M_{2}}=\left.\mathfrak{s}\right|_{M_{2}}$, we have $\mathfrak{s}_{M}^{\prime}=\mathfrak{s}+\operatorname{PD}\left[S_{r}\right]$ for some $r \in \mathbb{Z}^{n}$. This implies that
$$c_{1}\left(\left.\widetilde{\mathfrak{s}}\right|_{\widetilde{M}_{1}}\right)=2 \operatorname{PD}\left[\widetilde{S}_{r}\right]+p^{*}(\alpha)$$
for some $\alpha \in H^{2}(\mathcal{Q} ; \mathbb{Z})$. Furthermore, we have
$$\left[S_{r}\right] \cdot\left[S_{r}\right]=\left[S_{r}\right] \cdot\left[S_{r}\right]+\left\langle c_{1}(\mathfrak{s}),\left[S_{r}\right]\right\rangle=d\left(\mathfrak{s}_{M}^{\prime}, M\right)-d(\mathfrak{s}, M)=-2 .$$
So $r$ is a root.
By twisting $\widetilde{\mathfrak{s}}$ with a line bundle pulled back from $\mathcal{Q}$ (which doesn't change the family Seiberg-Witten invariant according to Lemma 2.7), we may assume that $\left.\widetilde{\mathfrak{s}}\right|_{\widetilde{M_{2}}}$ is a pull back of $\left.\mathfrak{s}\right|_{M_{2}}$. This implies $\alpha=0$ and
$$c_{1}\left(\left.\widetilde{\mathfrak{s}}\right|_{\widetilde{M}_{1}}\right)=2 \operatorname{PD}\left[\widetilde{S}_{r}\right] .$$
Suppose $b_{2}^{+}(M)>1$, then by Theorem 5.3, we have
$$\operatorname{FSW}\left(\widetilde{M}, \widetilde{\mathfrak{s}}_{\widetilde{M}}\right)=-\left\langle c_{1}\left(\operatorname{Ind} \not D^{+}(\widetilde{M}, \widetilde{\mathfrak{s}})\right),[\mathcal{Q}]\right\rangle \cdot \operatorname{SW}(M, \mathfrak{s}) .$$
By Proposition 6.6, we have $\left\langle c_{1}\left(\operatorname{Ind} \not D^{+}(\widetilde{M}, \widetilde{\mathfrak{s}})\right),[\mathcal{Q}]\right\rangle= \pm 1$. This finishes the proof when $b_{2}^{+}(M)>1$. The argument when $b_{2}^{+}(M)=1$ is the same. \(\square\)

Proposition 8.3. Let $\widetilde{M} / \mathcal{Q}$ be a blown-up family. Let $\mathfrak{s}$ be a $\operatorname{spin}^{c}$ structure on the fiber $M$ that satisfies $d(\mathfrak{s}, M)=0$ and $\left\langle c_{1}(\mathfrak{s}),[S]\right\rangle=1$. Let $\widetilde{\mathfrak{s}}$ be any family spin ${ }^{c}$ structure such that $d(\widetilde{\mathfrak{s}}, \widetilde{M})=0$ and $\left.\widetilde{\mathfrak{s}}\right|_{M_{2}}=\left.\mathfrak{s}\right|_{M_{2}}$. Then we have
$$\operatorname{FSW}(\widetilde{M} / \mathcal{Q}, \widetilde{\mathfrak{s}})=\operatorname{SW}(M, \mathfrak{s})$$
when $b_{2}^{+}(M)>1$ and we have
$$\operatorname{FSW}_{ \pm}(\widetilde{M} / \mathcal{Q}, \widetilde{\mathfrak{s}})=\operatorname{SW}_{ \pm}(M, \mathfrak{s}) .$$
when $b_{2}^{+}(M)=1$.

Proof. The proof is identical to Proposition 8.2, except that we use Proposition 7.2 instead of Lemma 6.6. \(\square\)

Now we suppose the fiber $M$ has a symplectic structure $\omega$ with the canonical class $K \in H^{2}(M ; \mathbb{Z})$ and the canonical spin ${ }^{c}$ structure $\mathfrak{s}_{J}$. By Lemma 8.1, there exists a unique family spin ${ }^{c}$ structure that restricts to $\mathfrak{s}_{J}$ on the fiber $M$ and restricts to a pull-back of $\left.\mathfrak{s}_{J}\right|_{M_{2}}$ on the product piece $\widetilde{M}_{2}=\mathcal{Q} \times M_{2}$. We denote this family spin ${ }^{c}$ stucture by $\widetilde{\mathfrak{s}}_{J}$.

Proof of Theorem J. Suppose (1) is not true and such $a$ exists. Then $a=\left[S_{r}\right]$ for some root $r$. By replacing $r$ with $-r$, we may assume that
$$\left\langle\left[\omega_{b}\right],\left[S_{r}\right]\right\rangle \leqslant 0, \quad \forall b \in \mathcal{Q} .$$
Consider the family spin ${ }^{c}$ structure $\widetilde{\mathfrak{s}}=\widetilde{\mathfrak{s}}_{J}+\operatorname{PD}\left[\widetilde{S}_{r}\right]$. Then By Theorem 2.14, we must have
$$\operatorname{FSW}_{\xi_{\omega}}(\widetilde{M}, \widetilde{\mathfrak{s}})=0 .$$
However, Proposition 8.2 and Theorem 2.13 together imply that
$$\operatorname{FSW}_{\xi_{c}}(\widetilde{M}, \widetilde{\mathfrak{s}})= \pm \operatorname{SW}\left(M, \mathfrak{s}_{J}\right)= \pm 1 .$$
So the only possibility is that $\xi_{\omega} \neq \xi_{c}$. This can only happen when $b_{2}^{+}(M)=3$. By (11), $\xi_{\omega}$ must be the winding chamber. That implies the map (4) has degree $\pm 1$. Since $M$ is minimal, by a result of Taubes [45, Theorem 0.2], we have $K \cdot K \geqslant 0$ and $\left[\omega_{b}\right] \cdot K \geqslant 0$ for any $b \in \mathcal{Q}$. By Lemma 2.4(ii), $K$ must be torsion. \(\square\)

Proof of Theorem H. By Theorem 2.16 and Theorem 2.17, we have $\left\langle\left[\omega_{b}\right],[S]\right\rangle>0$ for any $b \in \mathcal{Q}$. Consider the family spin ${ }^{c}$ structure
$$\widetilde{\mathfrak{s}}=\widetilde{\mathfrak{s}}_{J}-\operatorname{PD}[\widetilde{S}],$$
Then by Proposition 2.14, we have
$$\operatorname{FSW}_{\xi_{\omega}}(\widetilde{M} / \mathcal{Q}, \widetilde{\mathfrak{s}})=0 .$$
Again, we compare this with Theorem 2.13 and Proposition 8.3. We see that the only possibility is that $b_{2}^{+}(M)=3$ and the map (4) has mapping degree ±1. \(\square\)

We end this section by the following proposition, which used in Section 9 to show linearly independence of generalized Dehn twists.

Proposition 8.4. Let $M$ be a smooth 4-manifold with two smoothly embedded spheres $S_{0}$ and $S_{1}$ of self-intersection -1 or -2. Let $\mathfrak{s}$ be a spin ${ }^{c}$ structure with $d(\mathfrak{s}, M)=0$ such that the adjunction formula
$$\left\langle c_{1}(\mathfrak{s}),\left[S_{i}\right]\right\rangle=S_{i} \cdot S_{i}+2$$
holds for $i=1,2$. When $S_{0} \cdot S_{0}=-1$ (resp. $S_{0} \cdot S_{0}=-2$ ), we let $\widetilde{M} / \mathcal{Q}$ be the blown-up family (resp. the $A_{1}$-family) associated to $S_{0}$. Let $\widetilde{\mathfrak{s}}_{1}$ be a family spin ${ }^{c}$ structure on $\widetilde{M} / \mathcal{Q}$ that restricts to $\mathfrak{s}-\operatorname{PD}\left(S_{1}\right)$ on the fiber. Then the following conclusion holds.
\begin{itemize}
\item[(1)] Suppose $b_{2}^{+}(M)>1$ and assume
$$\operatorname{SW}\left(M, \mathfrak{s}-\operatorname{PD}\left(S_{1}\right)-\operatorname{PD}\left(S_{0}\right)\right)=\operatorname{SW}\left(M, \mathfrak{s}-\operatorname{PD}\left(S_{1}\right)+\operatorname{PD}\left(S_{0}\right)\right)=0 .$$
Then we have
$$\operatorname{FSW}\left(\widetilde{M} / \mathcal{Q}, \widetilde{\mathfrak{s}}_{1}\right)=0 .$$
\item[(2)] Suppose $b_{2}^{+}(M)=1$ and assume
$$\mathrm{SW}_{-}\left(M, \mathfrak{s}-\mathrm{PD}\left(S_{1}\right)-\mathrm{PD}\left(S_{0}\right)\right)=\mathrm{SW}_{-}\left(M, \mathfrak{s}-\mathrm{PD}\left(S_{1}\right)+\operatorname{PD}\left(S_{0}\right)\right)=0 .$$
Then we have
$$\operatorname{FSW}_{-}\left(\widetilde{M} / \mathcal{Q}, \widetilde{\mathfrak{s}}_{1}\right)=0 .$$
Same result holds for $\mathrm{SW}_{+}$and $\mathrm{FSW}_{+}$.
\end{itemize}

Lemma 8.5. Let $M, \widetilde{M}, S_{0}, S_{1}, \widetilde{\mathfrak{s}}_{1}$ be as in Proposition 8.4. Let $k=S_{0} \cdot S_{0}$ and let $n=k+2-2 S_{0} \cdot S_{1}$. Suppose $\left.\widetilde{\mathfrak{s}}_{1}\right|_{\widetilde{M}_{2}}$ is pull-back from $M_{2}$. Then we have
$$\left\langle c_{1}\left(\operatorname{Ind}\left(\not D^{+}\left(\widetilde{M}, \widetilde{\mathfrak{s}}_{1}\right)\right)\right),[\mathcal{Q}]\right\rangle=\frac{n(n-k)(n+k)}{24 k} .$$
Proof. We first assume $k=-2$. By the Atiyah-Singer index theorem, we have
$$\left\langle c_{1}\left(\operatorname{Ind}\left(\not D^{+}\left(\widetilde{M}, \widetilde{\mathfrak{s}}_{1}\right)\right)\right),[\mathcal{Q}]\right\rangle=\frac{\left\langle c_{1}\left(\widetilde{\mathfrak{s}}_{1}\right)^{3}-p_{1}(T \widetilde{M} / \mathcal{Q}) \cdot c_{1}\left(\widetilde{\mathfrak{s}}_{1},[\widetilde{M}]\right\rangle\right.}{48} .$$
Consider $c_{1}\left(\left.\widetilde{\mathfrak{s}}_{1}\right|_{\widetilde{M}_{1}}\right) \in H^{2}\left(\widetilde{M}_{1} ; \mathbb{R}\right)$. Since $\left.\widetilde{\mathfrak{s}}_{1}\right|_{\widetilde{M}_{1}}$ is pulled back from $\partial \widetilde{M}_{1}$ and $H^{2}\left(\partial \widetilde{M}_{1} ; \mathbb{R}\right)=$ 0 , there exists $\widetilde{x}_{1} \in H^{2}\left(\widetilde{M}_{1}, \partial \widetilde{M}_{1} ; \mathbb{R}\right)$ that is sent to $c_{1}\left(\left.\widetilde{\mathfrak{s}}_{1}\right|_{\widetilde{M}_{1}}\right)$. Smilarly, there exists $x_{2} \in H^{2}\left(M_{2}, \partial M_{2} ; \mathbb{R}\right)$ that is sent to $c_{1}\left(\left.\widetilde{\mathfrak{s}}_{1}\right|_{\widetilde{M}_{2}}\right) \in H^{2}\left(M_{2} ; \mathbb{R}\right)$. We let $\widetilde{x}_{2} \in H^{2}\left(\widetilde{M}_{2}, \partial \widetilde{M}_{2} ; \mathbb{R}\right)$ be the pull-back of $x_{2}$ under the projection map $\widetilde{M}_{2} \rightarrow M_{2}$. Then we have
$$\begin{aligned}
\left\langle c_{1}\left(\operatorname{Ind}\left(\not D^{+}\left(\widetilde{M}, \widetilde{\mathfrak{s}}_{1}\right)\right)\right),[\mathcal{Q}]\right\rangle & =\frac{\left\langle\widetilde{x}_{1}^{3}-p_{1}\left(T \widetilde{M}_{1} / \mathcal{Q}\right) \cdot \widetilde{x}_{1},\left[\widetilde{M}_{1}\right]\right\rangle}{48}+\frac{\left\langle\widetilde{x}_{2}^{3}-p_{1}\left(T \widetilde{M}_{2} / \mathcal{Q}\right) \cdot \widetilde{x}_{2},\left[\widetilde{M}_{2}\right]\right\rangle}{48} \\
& =\frac{\left.\left\langle\widetilde{x}_{1}^{3}-p_{1}\left(T \widetilde{M}_{1}\right) / \mathcal{Q} \cdot \widetilde{x}_{1}\right),\left[\widetilde{M}_{1}\right]\right\rangle}{48}
\end{aligned}$$
where the second equality follows from the observation that both $\widetilde{x}_{2}$ and $p_{1}\left(T \widetilde{M}_{2} / \mathcal{Q}\right)$ are pulled back from $M_{2}$. Since $H_{4}\left(\widetilde{M}_{1} ; \mathbb{R}\right)$ is generated by $\widetilde{S}_{0}$, we can have
$$\widetilde{x}_{1}=a \cdot \operatorname{PD}\left(\widetilde{S}_{0}\right)$$
for some $a \in \mathbb{R}$. Then by Lemma 6.5, we have
$$\frac{\left\langle\widetilde{x}_{1}^{3}-p_{1}\left(T \widetilde{M}_{1} / \mathcal{Q}\right) \cdot \widetilde{x}_{1},\left[\widetilde{M}_{1}\right]\right\rangle}{48}=\frac{a^{3}-a}{6} .$$
Because $\widetilde{S}_{0} \cdot S_{0}=-2$ and $\left\langle c_{1}\left(\widetilde{\mathfrak{s}}_{1}\right),\left[S_{0}\right]\right\rangle=n$, we get $a=\frac{n}{2}$. This finishes the proof when $k=-2$. The case $k=-1$ is similar. \(\square\)

Proof of Proposition 8.4. We first assume $b^{+}(M)>1$. By twisting $\widetilde{\mathfrak{s}}_{1}$ with a line bundle $L$ pulled back from $\mathcal{Q}$, we may assume that $\left.\widetilde{\mathfrak{s}}_{1}\right|_{\mathcal{Q} \times M_{2}}$ is pulled back from $M_{2}$. We may further assume that
$$\frac{n(n-k)(n+k)}{24 k} \neq 0$$
because otherwise Lemma 8.5, Theorem L and Theorem 4.32 will directly imply (85).
As the next step, we apply the switching formula (63) to conclude that
$$\operatorname{FSW}\left(\widetilde{M}_{0} / \mathcal{Q}, \widetilde{\mathfrak{s}}_{1}\right)=-\frac{n(n-k)(n+k)}{24 k} \cdot \operatorname{SW}\left(M, \mathfrak{s}-\operatorname{PD}\left(S_{1}\right)+l \operatorname{PD}\left(S_{0}\right)\right)$$
for any integer $l$ that satisfies
$$d\left(\mathfrak{s}-\operatorname{PD}\left(S_{1}\right)+l \operatorname{PD}\left(S_{0}\right), M\right) \geqslant 0 .$$
We denote this expected dimension by $d(l)$ and compute it as follows:
$$\begin{aligned}
d(l) & =d(\mathfrak{s}, M)+\left(l \operatorname{PD}\left(S_{0}\right)-\operatorname{PD}\left(S_{1}\right)\right)^{2}+c_{1}(\mathfrak{s}) \cdot\left(l \operatorname{PD}\left(S_{0}\right)-\operatorname{PD}\left(S_{1}\right)\right) \\
& =l^{2} S_{0} \cdot S_{0}+S_{1} \cdot S_{1}-2 l S_{0} \cdot S_{1}+l\left\langle c_{1}(\mathfrak{s}),\left[S_{0}\right]\right\rangle-\left\langle c_{1}(\mathfrak{s}),\left[S_{1}\right]\right\rangle \\
& =k l^{2}+n l-2 .
\end{aligned}$$
To finish the proof, we consider four possible cases. Note that $k, n$ have the same parity.
\begin{itemize}
\item[(i)] $k=-1$ and $|n|>1$ : We let $l=1$ if $n>0$ and let $l=-1$ if $n<0$. Then
$$d(l)=|n|-3 \geqslant 0 .$$
By our assumption, we have
$$\operatorname{SW}\left(M, \mathfrak{s}-\operatorname{PD}\left(S_{1}\right) \pm \operatorname{PD}\left(S_{0}\right)\right)=0$$
and (85) follows from (88).
\item[(ii)] $k=-1$ and $n= \pm 1$ : This is ruled out by (87).
\item[(iii)] $k=-2$ and $|n| \geqslant 4$ : We let $l=1$ if $n>0$ and let $l=-1$ if $n<0$. Then $d(l)=|n|-4 \geqslant 0$ and the argument is the same as (i).
\item[(iv)] $k=-2$ and $n=0, \pm 2$ : This is ruled out by (87).
\end{itemize}
This finishes the proof when $b_{2}^{+}(M)>1$. The proof when $b_{2}^{+}(M)=1$ is completely analogous. \(\square\)

\section*{9. Linearly independence of the generalized Dehn twists}

In this section, we prove Theorem A. Theorem E and various corollaries of them. The ideas in these proofs are similar: To show a loop in $\operatorname{Diff}(M)$ is noncontractible, we use the loop as a clutching function and show that the corresponding family over $S^{2}$ has nontrivial family Seiberg-Witten invariants. To show that this loop is not homotopic to a loop in $\operatorname{Symp}(X)$, we use our results in previous sections to conclude that this family do not support a fiberwise symplectic structure (in a fixed cohomology class).
9.1. The symplectic case. Let $(M, \omega)$ be a symplectic 4-manifold with canonical class $K$. We fix a compatible almost complex structure $J$.

We assume that the set $R_{X}$ (as defined in (2)) is nonempty. For each $\alpha \in R_{X}$, we pick an embedded sphere $S_{\alpha}$ representing the corresponding homology class.

Lemma 9.1. One can choose a suitable orientation on $S_{\alpha}$ so that
$$\int_{S_{\alpha}} \omega \geqslant 0, \quad-\left\langle K,\left[S_{\alpha}\right]\right\rangle=2+S_{\alpha} \cdot S_{\alpha} .$$
Proof. By the definition of $R_{M}$, the self-intersection $S_{\alpha} \cdot S_{\alpha}$ can be -1 or -2.
When $S_{\alpha} \cdot S_{\alpha}=-1$, we orient $S_{\alpha}$ so that $\left\langle K,\left[S_{\alpha}\right]\right\rangle=-1$. Then by Theorem 2.16 and Theorem 2.17, $S_{\alpha}$ is homologous to an embedded holnomorphic curve $C$. Therefore, (89) is satisfied.

When $S_{\alpha} \cdot S_{\alpha}=-2$, we have $\left\langle K,\left[S_{\alpha}\right]\right\rangle=0$ so the equality $-\left\langle K,\left[S_{\alpha}\right]\right\rangle=2+S_{\alpha} \cdot S_{\alpha}$ holds for both orientations. By choosing a suitable orientation, we may assume $\int_{S_{\alpha}} \omega \geqslant 0$ \(\square\)

From now on, we assume that (89) is satisfied for all $S_{\alpha}$. For each $\alpha \in R_{M}$, we use the generalized Dehn twist $\gamma_{S_{\alpha}}$ as the clutching function and form a family $\widetilde{M}_{\alpha} / \mathcal{Q}$ over $\mathcal{Q}=S^{2}$. When $S_{\alpha} \cdot S_{\alpha}=-1, \widetilde{M}_{\alpha} / \mathcal{Q}$ is a blown-up family. When $S_{\alpha} \cdot S_{\alpha}=-2, \widetilde{M}_{\alpha} / \mathcal{Q}$ is an $A_{1}$ family. For any formal linear combination $\vec{\alpha}=\sum_{i=1}^{n} a_{i} \alpha_{i} \in \mathbb{Z}^{R_{M}}$, we consider the loop
$$\gamma_{\vec{\alpha}}:=\gamma_{S_{\alpha_{1}}}^{a_{1}} \cdots \gamma_{S_{\alpha_{n}}}^{a_{n}}$$
in $\operatorname{Diff}(M)$ and we use it as the clutching function to define the family $\widetilde{M}_{\vec{\alpha}} / \mathcal{Q}$.
Theorem 9.2. Consider a closed, oriented surface $\mathcal{Q}^{\prime}$ and a smooth map $f: \mathcal{Q}^{\prime} \rightarrow \mathcal{Q}$ of nonzero degree. Let $\widetilde{M}_{\vec{\alpha}}^{\prime} / \mathcal{Q}^{\prime}$ be the smooth family obtained by pulling back $\widetilde{M}_{\vec{\alpha}} / \mathcal{Q}$ via $f$. Suppose $\vec{\alpha} \neq \overrightarrow{0}$. Then $\widetilde{M}_{\vec{\alpha}}^{\prime} / \mathcal{Q}^{\prime}$ does not carry a fiberwise symplectic structure $\left\{\omega_{b}\right\}$ in the fixed cohomology class $[\omega]$. In particular, $\widetilde{M}_{\vec{\alpha}} / \mathcal{Q}$ itself doesn't carry a fiberwise symplectic structure in the fixed cohomology class $[\omega]$.

Proof. We first assume $b^{+}(M)>1$. Let $\vec{\alpha}=a_{1} \alpha_{1}+\cdots+a_{n} \alpha_{n}$. Without loss of generality, we may assume that
$$\int_{S_{\alpha_{1}}} \omega \geqslant \int_{S_{\alpha_{2}}} \omega, \cdots, \int_{S_{\alpha_{n}}} \omega \geqslant 0 .$$
Then by Taubes' theorem Theorem 2.13, we have
$$\operatorname{SW}\left(M, \mathfrak{s}_{J}-\operatorname{PD}\left(S_{\alpha_{1}}\right) \pm \operatorname{PD}\left(S_{\alpha_{i}}\right)\right)=0 \quad \text { for any } 2 \leqslant i \leqslant n .$$
Next, we consider a family spin ${ }^{c}$ structure $\mathfrak{s}_{\widetilde{M}_{\vec{\alpha}}}$ such that
$$\left.\mathfrak{s}_{\widetilde{M}_{\vec{\alpha}}}\right|_{M}=\mathfrak{s}_{J}-\mathrm{PD}\left(S_{\alpha_{1}}\right) .$$
By the additivity of the family Seiberg-Witten invariant, we have
$$\operatorname{FSW}\left(\widetilde{M}_{\vec{\alpha}} / \mathcal{Q}, \mathfrak{s}_{\widetilde{M}_{\vec{\alpha}}}\right)=\sum_{i=1}^{n} a_{i} \cdot \operatorname{FSW}\left(\widetilde{M}_{\alpha_{i}} / \mathcal{Q}, \mathfrak{s}_{\widetilde{M}_{\alpha_{i}}}\right),$$
where $\mathfrak{s}_{\widetilde{M}_{\alpha_{i}}}$ is a family $\operatorname{spin}^{c}$ structure on $\widetilde{M}_{\alpha_{i}} / \mathcal{Q}$ that restricts to $\mathfrak{s}_{J}-\operatorname{PD}\left(S_{\alpha_{1}}\right)$ on the fiber $M$. By Proposition 8.4, we have
$$\operatorname{FSW}\left(\widetilde{M}_{\alpha_{i}} / \mathcal{Q}, \mathfrak{s}_{\widetilde{M}_{\alpha_{i}}}\right)=0, \text { for any } i \geqslant 2 .$$
By Proposition 8.2 and Proposition 8.3, we have
$$\operatorname{FSW}\left(\widetilde{M}_{\alpha_{1}} / \mathcal{Q}, \mathfrak{s}_{\widetilde{M}_{\alpha_{1}}}\right)= \pm 1 .$$
Therefore, we get
$$\operatorname{FSW}\left(\widetilde{M}_{\vec{\alpha}} / \mathcal{Q}, \mathfrak{s}_{\widetilde{M}_{\vec{\alpha}}}\right)= \pm a_{1} .$$

Now we consider the family Seiberg-Witten invariant of $\widetilde{M}_{\vec{\alpha}}^{\prime} / \mathcal{Q}^{\prime}$. Since $\widetilde{M}_{\vec{\alpha}}^{\prime} / \mathcal{Q}^{\prime}$ is pulled back from the homology product $\widetilde{M}_{\alpha} / \mathcal{Q}$, itself is also a homology product. Let $\mathfrak{s}_{\widetilde{M}_{\dot{\alpha}}^{\prime}}$ be the pull-back of $\mathfrak{s}_{\widetilde{M}_{\vec{\alpha}}}$. Then by Lemma 2.8, we have
$$\operatorname{FSW}\left(\widetilde{M}_{\vec{\alpha}}^{\prime} / \mathcal{Q}^{\prime}, \mathfrak{s}_{\widetilde{M}_{\vec{\alpha}}^{\prime}}\right)=\operatorname{deg}(f) \cdot \operatorname{FSW}\left(\widetilde{M}_{\vec{\alpha}} / \mathcal{Q}, \mathfrak{s}_{\widetilde{M}_{\vec{\alpha}}}\right)=\operatorname{deg}(f) \cdot a_{1} \neq 0$$

Now suppose $\widetilde{M}_{\vec{\alpha}}^{\prime} / \mathcal{Q}^{\prime}$ support a fiberwise symplectic structure $\left\{\omega_{b}\right\}$ in the cohomology class $[\omega]$. By Theorem 2.13, the canonical class of $\omega_{b}$ equals $K$. Therefore, Proposition 2.14 tells us that $\operatorname{FSW}\left(\widetilde{M}_{\vec{\alpha}}^{\prime} / \mathcal{Q}^{\prime}, \mathfrak{s}_{\widetilde{M}_{\vec{\alpha}}^{\prime}}\right)=0$. This leads to the contradiction.

The case $b^{+}(M)=1$ is completely analogous. One can show that
$$\operatorname{FSW}_{-}\left(\widetilde{M}_{\vec{\alpha}}^{\prime} / \mathcal{Q}, \mathfrak{s}_{\widetilde{M}_{\vec{\alpha}}^{\prime}}\right)=\operatorname{deg}(f) \cdot a_{1} \neq 0 .$$
and then apply Proposition 2.14. \(\square\)

Proof of Theorem E. By Theorem 9.2, the structure group of $\widetilde{M}_{\vec{\alpha}} / \mathcal{Q}$ can not be reduced to $\operatorname{Symp}(M)$. Hence its clutching function $\gamma_{\vec{\alpha}}$ is not homotopic to a loop in $\operatorname{Symp}(M)$. \(\square\)

Proof of Corollary F. Suppose $M$ is minimal. Then $S \cdot S=-2$. By Lemma 2.18, we have $-\langle K,[S]\rangle=0$ and $[S] \in R_{M}$. Suppose $M$ is nonminimal. Then the exceptional curve represents an element in $R_{M}$. In both cases, the set $R_{M}$ is nonempty so the result follows from Theorem E. \(\square\)

Proof of Corollary G. (1) For any $\vec{\alpha} \in \mathbb{Z}^{R_{M}} \backslash\{\overrightarrow{0}\}$, we consider the loop of symplectic structures $\widetilde{\omega}_{\vec{\alpha}}=\left\{\omega_{\vec{\alpha}}(t)\right\}_{t \in S^{1}}$ defined by $\widetilde{\omega}_{\vec{\alpha}}(t):=\gamma_{\alpha}(t)^{*}(\omega)$. We will show that $\widetilde{\omega}_{\vec{\alpha}}$ is not null-homologous in the space $\mathbb{S}_{[\omega]}(M)$. Suppose this is not the case. Then there exists a smooth family of cohomologous symplectic forms $\widetilde{\omega}_{1}:=\left\{\omega_{b}\right\}_{b \in F}$ on $M$ that is parameterized by an oriented surface $F$ and restricts to $\widetilde{\omega}_{\vec{\alpha}}$ on $\partial F$. We also consider the constant family of symplectic forms $\widetilde{\omega}_{2}:=\left\{\omega_{b}\right\}_{b \in D^{2}}$ with $\omega_{b}=\omega$ for any $b \in D^{2}$. Let $\mathcal{Q}^{\prime}=F \cup_{S^{1}} D^{2}$. Consider the smooth family $\widetilde{M}_{\vec{\alpha}}^{\prime} / \mathcal{Q}^{\prime}$ defined by
$$\widetilde{M}_{\vec{\alpha}}^{\prime}=\left((F \times X) \sqcup\left(D^{2} \times X\right)\right) / \sim,$$
where ~ is generated by $(t, x) \sim\left(t, \gamma_{\alpha}(t)(x)\right)$ for $t \in \partial D^{2}=\partial F$. By gluing together $\widetilde{\omega}_{1}$ and $\widetilde{\omega}_{2}$, we obtain a fiberwise symplectic structure on $\widetilde{M}_{\vec{\alpha}}^{\prime} / \mathcal{Q}^{\prime}$ in the cohomology class $[\omega]$.

However, $\widetilde{M}_{\vec{\alpha}}^{\prime} / \mathcal{Q}^{\prime}$ can also be obtained by pulling back $\widetilde{M}_{\vec{\alpha}} / \mathcal{Q}$ via a degree-1 map from $\mathcal{Q}^{\prime}$ to $\mathcal{Q}$. So Theorem 9.2 implies that such a fiberwise symplectic structure does not exist. This leads to the contradiction.
(2) Now we assume $\vec{\alpha} \in \mathbb{Z}_{M}^{R_{M}^{2}} \backslash\{\overrightarrow{0}\}$ and prove that $\widetilde{\omega}_{\vec{\alpha}}$ is indeed null-homotopic (and hence null-homologous) in $\mathcal{S}(M)$ (the space of almost symplectic forms). By linearity, it suffices to focus on the case $\vec{\alpha}=\alpha$ for some $\alpha \in R_{M}^{2}$. By Lemma 6.2, the family $\widetilde{M}_{\vec{\alpha}} / \mathcal{Q}$ admits a fiberwise almost complex structure $\widetilde{J}=\left\{J_{b}\right\}_{b \in \mathcal{Q}}$ such that $J_{b_{0}}=J$. By choosing compatible matrices on the fibers, $\widetilde{J}$ induces a smooth family of almost symplectic forms $\widetilde{\omega}_{4}=\left\{\omega_{b}\right\}_{b \in \mathcal{Q}}$ such that $\omega_{b_{0}}=\omega$. By pulling back $\widetilde{\omega}_{4}$ via the quotient map
$$D^{2} \rightarrow D^{2} / \partial D^{2} \cong \mathcal{Q},$$
we obtain a smooth family $\widetilde{\omega}_{5}$ of almost symplectic forms that is parametrzied by $D^{2}$ and restricts to $\widetilde{\omega}_{\vec{\alpha}}$ on $\partial D^{2}$. So $\widetilde{\omega}_{\vec{\alpha}}$ is null-homotopic in $\mathcal{S}(M)$ when $\vec{\alpha}=\alpha$.
(3) We first assume $b_{2}^{+}(M)>1$. Consider a nontrivial linear combination $\vec{\alpha}=\sum_{i=1}^{n} a_{i} \alpha_{i}$ of elements $\alpha_{i} \in R_{M}^{1}$. We may assume
$$\int_{S_{\alpha_{1}}} \omega \geqslant \int_{S_{\alpha_{2}}} \omega, \cdots, \int_{S_{\alpha_{n}}} \omega \geqslant 0 .$$
Suppose the loop $\widetilde{\omega}_{\vec{\alpha}}$ is null-homologous in $\mathbb{S}(M)$. Then smilar to (1), one can construct a smooth family $\widetilde{M}_{\vec{\alpha}}^{\prime} / \mathcal{Q}^{\prime}$, parametrized by a surface $\mathcal{Q}^{\prime}$, such that it admits a fiberwise symplectic structure $\left\{\omega_{b}\right\}$ with $\omega_{b_{0}}=\omega$ and that
$$\operatorname{FSW}\left(\widetilde{M}_{\vec{\alpha}}^{\prime} / \mathcal{Q}^{\prime}, \mathfrak{s}_{\widetilde{M}_{\vec{\alpha}}^{\prime}}\right) \neq 0 .$$
for some family spin ${ }^{c}$-structure $\mathfrak{s}_{\widetilde{M}_{\vec{\alpha}}^{\prime}}$ that restricts to $\mathfrak{s}_{J}-\operatorname{PD}\left(S_{\alpha_{1}}\right)$ on the fibers. By Theorem 2.16 and Theorem 2.17, we have $\left\langle\left[\omega_{b}\right],\left[S_{\alpha}\right]\right\rangle>0$ for any $b \in \mathcal{Q}^{\prime}$. So Proposition 2.14 tells us that
$$\operatorname{FSW}_{\xi_{\omega}}\left(\widetilde{M}_{\vec{\alpha}}^{\prime} / \mathcal{Q}^{\prime}, \mathfrak{s}_{\widetilde{M}_{\vec{\alpha}}^{\prime}}\right)=0 .$$
Since $b^{+}(M) \neq 2,3$. Every map from $\mathcal{Q}^{\prime}$ to $V^{+}(M) \simeq S^{b^{+}}(M)-1$ is null-homotopic. So the symplectic chamber $\xi_{\omega}$ is just the canonical chamber. This leads to the contradiction.

When $b^{+}(M)=1$, we use FSW_ instead of FSW and then repeat the argument.
(4) The proof is the same as (3), except that we can set $\mathcal{Q}^{\prime}=\mathcal{Q}$ in this case. So every map $\mathcal{Q}^{\prime}$ to $V^{+}(M) \simeq S^{b^{+}(M)-1}$ is null-homotopic as long as $b^{+}(M) \neq 3$. \(\square\)
9.2. The smooth case. From now on, we assume that $M$ is a smooth (but not necessarily symplectic) 4-manifold with $b_{1}(M)=0$.

Lemma 9.3. Suppose $b_{2}^{+}(M)>1$. Consider the set
$$\mathcal{A}_{M}:=\{\mathfrak{s} \mid \operatorname{SW}(M, \mathfrak{s}) \neq 0\}$$
of Seiberg-Witten basic classes. Then for any smoothly embedded -2-sphere $S$ and any $\mathfrak{s} \in \mathcal{A}_{M}$, we have
$$\mathfrak{s}+\frac{\left\langle c_{1}(\mathfrak{s}),[S]\right\rangle}{2_{68}} \cdot S \in \mathcal{A}_{M}$$

Proof. Given any such $S$, we consider the relfection diffeomorphism $r: M \rightarrow M$. (See the proof of Lemma 2.18 for an explicit description.) Since $r$ is supported near $S$, we have
$$r_{*}(\mathfrak{s})=\mathfrak{s}+k \operatorname{PD}(S)$$
for some $k$. To compute $k$, we note that the induced action
$$r^{*}: H^{2}(M ; \mathbb{Z}) \rightarrow H^{2}(M ; \mathbb{Z})$$
is the relation along $\operatorname{PD}(S)$. In particular, one has
$$\left\langle c_{1}\left(r^{*}(\mathfrak{s})\right),[S]\right\rangle=-\left\langle c_{1}(\mathfrak{s}),[S]\right\rangle$$
This implies $k=\frac{\left\langle c_{1}(\mathfrak{s}),[S]\right\rangle}{2}$. Since $\mathcal{A}_{M}$ is preserved by any orientation preserving diffeomorphism, we have proved (90). \(\square\)

Now we are ready to prove Theorem A, restated as follows.
Theorem 9.4. Let $M$ be a smooth closed 4-manifold that contains an infinite collection of smoothly embedded (-2)-spheres $\left\{S_{i}\right\}_{i \in \mathbb{N}}$, representing different homology classes. Suppose $b_{1}(M)=0$ and assume one of the following conditions holds:
\begin{itemize}
\item[(1)] $b_{2}^{+}(M)>1$ and $\operatorname{SW}\left(M, \mathfrak{s}_{M}\right) \neq 0$ for some spin ${ }^{c}$-structure $\mathfrak{s}$ with $d(\mathfrak{s}, M)=0$.
\item[(2)] $b_{2}^{+}(M)=1$ and there exists a spin ${ }^{c}$ structure $\mathfrak{s}$ such that $d(\mathfrak{s}, M)=0$ and that $\left\langle c_{1}(\mathfrak{s}),\left[S_{i}\right]\right\rangle=0$ for any $i$. (We don't impose any constraint on the Seiberg-Witten invariant in this case.)
\end{itemize}
Then $\pi_{1}(\operatorname{Diff}(M))$ contains a $\mathbb{Z}^{\infty}$-summand, generated by generalized Dehn twists along a subcollection $\left\{S_{n_{i}}\right\}_{i \in \mathbb{N}}$.

Proof. (1) Since $\mathcal{A}_{M}$ is a finite set, after passing to an infinite subcollection, we may assume that for any $\mathfrak{s} \in \mathcal{A}_{M}$, any $i \neq j$ and any $k \neq 0$, we have
$$\mathfrak{s}+k \operatorname{PD}\left(S_{i}\right) \notin \mathcal{A}_{M}$$
and
$$\mathfrak{s}-\operatorname{PD}\left(S_{i}\right) \pm \operatorname{PD}\left(S_{j}\right) \notin \mathcal{A}_{M} .$$

By (91) and Lemma 9.3, we have $\left\langle c_{1}(\mathfrak{s}),\left[S_{i}\right]\right\rangle=0$ for any $i \in \mathbb{N}$. Denote $\mathfrak{s}-\operatorname{PD}\left(S_{i}\right)$ by $\mathfrak{s}_{i}$. Then $d\left(\mathfrak{s}_{i}, M\right)=-2$. By Proposition 2.10, we have a group homomorphism
$$\bigoplus_{i \in \mathbb{N}} \operatorname{SW}\left(-, \mathfrak{s}_{i}\right): \pi_{1}(\operatorname{Diff}(M)) \rightarrow \mathbb{Z}^{\infty} .$$
It suffices to show that this homomorphism is surjective. To see this, we consider the generalized Dehn twist $\gamma_{S_{i}}$ around $S_{i}$. Then Proposition 8.2, Proposition 8.4 and (92) together imply that
$$\operatorname{SW}\left(\gamma_{S_{i}}, \mathfrak{s}_{j}\right)= \begin{cases} \pm \operatorname{SW}(M, \mathfrak{s}) \neq 0 & \text { if } i=j \\ 0 & \text { if } i \neq j\end{cases}$$
This finishes the proof.
(2) We pick $H \in H^{2}(M ; \mathbb{Z})$ with $H \cdot H>0$ and use it to fix a homology orientation on $M$. Let
$$\mathcal{A}_{M}:=\left\{\mathfrak{s} \mid \operatorname{SW}_{H}(M, \mathfrak{s}) \neq 0\right\},$$
where $\operatorname{SW}_{H}(M, \mathfrak{s})$ is the small perturbation Seiberg-Witten invariant defined as
$$\mathrm{SW}_{H}(M, \mathfrak{s}):=\left\{\begin{array}{ll}
\mathrm{SW}_{+}(M, \mathfrak{s}) & \text { if } c_{1}(\mathfrak{s}) \cdot H \geqslant 0 \\
\mathrm{SW}_{-}(M, \mathfrak{s}) & \text { if } c_{1}(\mathfrak{s}) \cdot H<0
\end{array} .\right.$$
Then compactness of the Seiberg-Witten moduli space implies that $\mathcal{A}_{M}$ is a finite set. Since $\operatorname{SW}_{+}(M, \mathfrak{s})$ and $\operatorname{SW}_{-}(M, \mathfrak{s})$ differ by ±1, at least one of them is nonzero. By changing the sign of $H$ if necessary, we may assume $\operatorname{SW}_{-}(M, \mathfrak{s}) \neq 0$.

Since $S_{i}$ all represent distinct homology classes of self-intersection -2, it's straightforward to see that
$$\lim _{i \rightarrow+\infty}\left|\operatorname{PD}\left(S_{i}\right) \cdot H\right|=+\infty .$$
Therefore, by passing to an infinite subcollection and choosing suitable orientations on $S_{i}$, we may assume that the following conditions all hold.
\begin{itemize}
\item[-] For any $i \in \mathbb{N}$, we have $c_{1}\left(\mathfrak{s}-\operatorname{PD}\left(S_{i}\right)\right) \cdot H<0$..
\item[-] For any $j>i$, we have
$$c_{1}\left(\mathfrak{s}-\mathrm{PD}\left(S_{j}\right) \pm \mathrm{PD}\left(S_{i}\right)\right) \cdot H<0 .$$
\item[-] For any $j>i$, we have
$$\mathfrak{s}-\operatorname{PD}\left(S_{j}\right) \pm \operatorname{PD}\left(S_{i}\right) \notin \mathcal{A}_{M} .$$
\end{itemize}
We let $\mathfrak{s}_{i}=\mathfrak{s}-\mathrm{PD}\left(S_{i}\right)$. By Proposition 2.12, we have a group homomorphism
$$\bigoplus_{i \in \mathbb{N}} \operatorname{SW}_{H}\left(-, \mathfrak{s}_{i}\right): \pi_{1}(\operatorname{Diff}(M)) \rightarrow \mathbb{Z}^{\infty} .$$

To show that this homomorphism is surjective, we again consider the generalized Dehn twist $\gamma_{S_{i}}$ around $S_{i}$. By Proposition 8.2, we have
$$\mathrm{SW}_{H}\left(\gamma_{S_{i}}, \mathfrak{s}_{i}\right)=\mathrm{SW}_{-}(M, \mathfrak{s}) \neq 0 .$$
While for any $i<j$, we apply Proposition 8.4, (91) and (92) to conclude that
$$\mathrm{SW}_{H}\left(\gamma_{S_{i}}, \mathfrak{s}_{j}\right)=0 .$$
Therefore, the homomorphism (95) is surjective. \(\square\)

Proof of Corollary C. (1) We start with the case $M=E(1)$, obtained by blowing up $\mathbb{C P}^{2}$ along the nine intersection points of two generic cubical curves. We set $\mathfrak{s}$ to be the canonical spin ${ }^{c}$-structure $\mathfrak{s}_{J}$. Then
$$c_{1}(\mathfrak{s})=-K=\operatorname{PD}\left(3[H]-\sum_{i=1}^{9}\left[C_{i}\right]\right)=\operatorname{PD}\left[F_{\infty}\right] .$$
Here $H$ is a hyperplane in $\mathbb{C P}^{2}, C_{i}$ is the $i$-th exceptional divisor and $F_{\infty}$ is a regular fiber. We consider the map
$$\rho: H_{2}\left(M \backslash F_{\infty} ; \mathbb{Z}\right) \rightarrow H_{2}(M ; \mathbb{Z}) .$$
Then the $\operatorname{Image}(\rho)$ equals
$$K^{\perp}:=\{\alpha \in H(M ; \mathbb{Z}) \mid\langle K, \alpha\rangle=0\} .$$

Take an infinite collection of classes in $K^{\perp}$ with square -2. For example, we can set
$$\alpha_{i}=\left[C_{1}\right]-\left[C_{2}\right]+i\left[F_{\infty}\right] \text { for } i \in \mathbb{N} .$$
Then by [10, Theorem 5.1], $\alpha_{i}$ can be represented by an embedded sphere in $S_{i} \hookrightarrow M \backslash F_{\infty}$. This finishes the proof when $M=E(1)$.

For a generic elliptic surface $M$ with $b_{1}(M)=0$, it can be obtained from $E(1)$ by taking logarithmic transformations and taking fiber sums with additional copies of $E(1)$. We apply these constructions along regular fibers near $F_{\infty}$. Then $S_{i}$ is still embedded in $M$. Note that
$$\left[S_{i}\right]-\left[S_{j}\right]=(i-j)\left[F_{\infty}\right] \neq 0 \in H_{2}(M ; \mathbb{Z}) .$$
So $\left\{S_{i}\right\}_{i \in \mathbb{N}}$ still represent different homology classes in $M$.
(2) Now we suppose $M$ is a hypersurface or complete intersection with $b^{+}(M)>1$. By the Lefschetz hyperplane theorem, $M$ is simply-connected. We again set $\mathfrak{s}$ to be the canonical spin ${ }^{c}$ structure. Let $V=K^{\perp} \otimes \mathbb{R}$. In [10, Page 406], the authors found a subset $\Delta \subset V$ such that any element in $\Delta$ can be represented by an embedded (-2)-sphere. Moreover, let $\Gamma_{\Delta} \subset \operatorname{Aut}(V)$ be the group generated by reflections along elements in $\Delta$. Then it is proved that $\Gamma_{\Delta} \cdot \Delta$ is Zariski dense in $V$. In particular, $\Gamma_{\Delta} \cdot \Delta$ is an infinite set. Since any element in $\Gamma_{\Delta}$ can be realized by a diffeomorphism on $M$ (i.e. a composition of reflections along those -2-spheres), we see that any class in $\Gamma_{\Delta} \cdot \Delta$ can be presented by an embedded -2-sphere.
(3) Let $M=M^{\prime} \#_{T^{2}} E$. Using the Mayer-Vietoris sequence, it can be shown that $b_{1}(M)=0$ and $b^{+}(M)>1$. Since $S W\left(M^{\prime}, \mathfrak{s}\right) \neq 0$, by the adjuntion inequality, we have $\left\langle c_{1}(\mathfrak{s}),[F]\right\rangle=0$. By the gluing formula for the Seiberg-Witten invariants along $T^{3}$ (see [19, formula (38.4)]), we can suitable glue $\mathfrak{s}$ and the canonical spin ${ }^{c}$ structure $\mathfrak{s}_{J}$ on $E$ together and form a $\operatorname{spin}^{c}$ structure $\mathfrak{s}$ such that $S W(M, \mathfrak{s}) \neq 0, d(\mathfrak{s})=0$. Let $\left\{S_{i}\right\}$ be the -2-spheres embedded in $E \backslash F_{\infty} \subset M$ established in (1). Similar to (1), the homology classes of $S_{i}$ differ from each other by nonzero multiples of $F$. So $\left\{S_{i}\right\}_{i \in \mathbb{N}}$ represent distinct homology classes (up to sign) in $M$. This finishes the proof.
(4) For $i=0,1$, consider the reflection $r_{i}: M \rightarrow M$ along $S_{i}$ and their induced action $r_{i, *}$ on the subgroup $V \subset H_{2}(M ; \mathbb{Z})$ generated by $\left[S_{0}\right]$ and $\left[S_{1}\right]$. Suppose $S_{0} \cdot S_{1}=k$. Then $r_{0, *}, r_{1, *}: V \rightarrow V$ are given by the matrices
$$\left(\begin{array}{cc}
1 & -k \\
0 & -1
\end{array}\right), \quad\left(\begin{array}{cc}
-1 & 0 \\
-k & 1
\end{array}\right)$$
respectively. Let $r=r_{1} \circ r_{2}$. Then $r_{*}: V \rightarrow V$ is given by the matrix
$$\left(\begin{array}{cc}
k^{2}-1 & -k \\
k & -1
\end{array}\right) .$$
When $|k| \geqslant 3$, this matrix does not have an eigenvalue with norm 1. As a result, the (-2)-sphere $\left\{r^{i}\left(S_{0}\right)\right\}_{i \in \mathbb{N}}$ all represent different homology classes.
(5) This follows directly from the blow up formula for the Seiberg-Witten invariants. \(\square\)

Proof of Corollary D. (1) By [20, Proposition 5.20], $\pi_{1}\left(\right.$ haut $\left.^{\mathrm{id}}(M)\right)$ is a finitely generated abelian group. Therefore, kernel of the map $\pi_{1}(\operatorname{Diff}(M)) \rightarrow \pi_{1}\left(\right.$ haut $\left.^{\text {id }}(M)\right)$ contains a $\mathbb{Z}^{\infty}$ subgroup.
(2) We first consider the simplical group $\widehat{\operatorname{Homeo}}(M)$ of block homeomorphisms. It is proved in [20, Proposition 5.22] that $\pi_{1}(\widetilde{\operatorname{Homeo}}(M))$ is a finitely generated abelian group. So kernel of the map
$$\pi_{1}(\operatorname{Diff}(M)) \rightarrow \pi_{1}(\widetilde{\operatorname{Homeo}}(M))$$
contains a $\mathbb{Z}^{\infty}$ subgroup. Any element in this kernel can be represented by a loop of diffeomorphisms $\gamma: S^{1} \rightarrow \operatorname{Diff}(M)$ such that the diffeomorphism
$$\widetilde{\gamma}: S^{1} \times M \rightarrow S^{1} \times M \text { defined by }(t, x) \mapsto(t, \gamma(t) \cdot x)$$
can be extended to a homeomorphism on $\widehat{\gamma}: D^{2} \times M \rightarrow D^{2} \times M$. By classical smoothing theory (see [15]), the unique obstruction class of isotoping $\widehat{\gamma}$ (relative to $S^{1} \times X$ ) to a diffeomorphism on $D^{2} \times M$ belongs to
$$H^{3}\left(D^{2} \times M, S^{1} \times M ; \pi_{3}(\operatorname{Top} / \mathrm{O})\right) \cong H^{3}\left(D^{2} \times M, S^{1} \times M ; \mathbb{Z} / 2\right) \cong H^{1}(M ; \mathbb{Z} / 2) .$$
Here Top denotes the direct limit of homeomorphism on $\mathbb{R}^{n}$ that preservers the origin and O denotes the direct limit of $O(n)$. Since $M$ is simply-connected, $H^{1}(M ; \mathbb{Z} / 2)=0$. So $\widehat{\gamma}$ is isotopic (relative to boundary) to a diffeomorphism on $D^{2} \times M$. We have proved that the kernel of the map
$$\pi_{1}(\operatorname{Diff}(M)) \rightarrow \pi_{1}(\widetilde{\operatorname{Diff}}(M))$$
actually coincides with the kernel of (96) so it contains a $\mathbb{Z}^{\infty}$ subgroup too.
(3) For any $\gamma: S^{1} \rightarrow \operatorname{Diff}(M)$ that gives an element in the kernel of (97), we use $\gamma$ as the clutching function and form the bundle $\widetilde{M}_{1} / S^{2}$. Then we have a diffeomorphism from $\widetilde{M}_{1}$ to $S^{2} \times M$ obtained by gluing together $\widehat{\gamma}$ and $\operatorname{Id}_{D^{2} \times M^{2}}$.

We assume $b^{+}(M)>1$ for now. By the proof of Theorem 9.2, we may pick $\gamma$ such that
$$a:=\operatorname{FSW}\left(\widetilde{M}_{1} / S^{2}, \widetilde{\mathfrak{s}}_{1}\right) \neq 0$$
for some family spin ${ }^{c}$ structure $\widetilde{\mathfrak{s}}_{1}$. For any $n \in \mathbb{N}$, we use a degree- $n$ map $S^{2} \rightarrow S^{2}$ to pull back $\left(\widetilde{M}_{1} / S^{2}, \widetilde{\mathfrak{s}}_{1}\right)$. We denote the result by $\left(\widetilde{M}_{n} / S^{2}, \widetilde{\mathfrak{s}}_{n}\right)$. Then by By Lemma 2.8, we have
$$\operatorname{FSW}\left(\widetilde{M}_{n} / S^{2}, \widetilde{\mathfrak{s}}_{n}\right)=n a .$$
Now consider another family spin ${ }^{c}$ structure $\widetilde{\mathfrak{s}}$ on $\widetilde{M}_{n} / \mathcal{Q}$ with $d(\widetilde{\mathfrak{s}}, \widetilde{M})=0$. By Lemma 2.9, there exists a family spin ${ }^{c}$ structure on $\widetilde{M}_{1} / \mathcal{Q}$ such that $\left.\widetilde{\mathfrak{s}}^{\prime}\right|_{M}=\left.\widetilde{\mathfrak{s}}\right|_{M}$. Then by Lemma 2.8 and Lemma 2.7, we have
$$\operatorname{FSW}\left(\widetilde{M}_{n} / S^{2}, \widetilde{\mathfrak{s}}\right)=n \operatorname{FSW}\left(\widetilde{M}_{1} / S^{2}, \widetilde{\mathfrak{s}}^{\prime}\right) .$$
In particular, this implies
$$n \mid \operatorname{FSW}\left(\widetilde{M}_{n} / S^{2}, \widetilde{\mathfrak{s}}\right) \text { for any } \widetilde{\mathfrak{s}} .$$
Equation (99) and (100) together imply that $\widetilde{M}_{n} / S^{2}$ is not isomorphic to $\widetilde{M}_{m} / S^{2}$ whenever $m>n|a|$. Therefore, the set $\left\{\widetilde{M}_{n} / S^{2}\right\}_{n \in \mathbb{N}}$ contains infinitely many isomorphism classes of smooth bundles over $S^{2}$. This finishes the proof when $b^{+}(M)>1$. When $b^{+}(M)=1$, we fix a choice of $H \in H^{2}(M ; \mathbb{Z})$ with $H \cdot H>0$ and repeat the same argument to $\mathrm{FSW}_{H}$. \(\square\)
---
retention_scope: session
part: 1
total_parts: 1
---

---
source_file: 0809_4891.pdf
converter: mathpix
format: mmd
---

\title{
ON THE NONEXISTENCE OF EINSTEIN METRIC ON 4-MANIFOLDS
}

\author{
CHANYOUNG SUNG
}

\begin{abstract}
By using the gluing formulae of the Seiberg-Witten invariant, we show the nonexistence of Einstein metric on manifolds obtained from a 4-manifold with nontrivial Seiberg-Witten invariant by performing sufficiently many connected sums or appropriate surgeries along circles or homologically trivial 2-spheres with closed oriented 4-manifolds with negative definite intersection form.
\end{abstract}

\section*{1. Introduction}

A smooth Riemannian manifold ( $M, g$ ) is called Einstein if it satisfies
$$\operatorname{Ric}_{g}=c g,$$
where $R i c_{g}$ denotes the Ricci curvature of $g$, and $c$ is a constant. When the dimension of $M$ is less than 4, any Einstein manifold is a space form whose classification is well-known. In higher dimensions, it is in general difficult to decide whether a manifold admits an Einstein metric. Unlike the dimension greater than 4 where no topological obstruction is known, any closed orientable 4-manifold $M$ admitting an Einstein metric must satisfy the Hitchin-Thorpe inequality [5, 8, 17]
$$2 \chi(M) \geq 3|\tau(M)|$$
with equality held only by a quotient of $K 3$ surface or 4-torus, where $\chi(M)$ and $\tau(M)$ respectively denote the Euler characteristic and the signature of $M$. This well-known inequality is the consequence of the 4-dimensional Chern-Gauss-Bonnet formula.

Since the 4-dimensional geometry is complicated by the possible existence of many smooth structures, the condition for the existence of Einstein metric on 4-manifolds inevitably involve the underlying smooth structure. It was the Seiberg-Witten theory that has brought a remarkable improvement of the

\footnotetext{
Date: November 2, 2018.
2000 Mathematics Subject Classification. 53C25,57R57, 57M50.
Key words and phrases. Einstein metric, Seiberg-Witten theory.
This work was supported by the National Research Foundation(KRF) grant funded by the Korea government(MEST). (No. 2009-0074404).
}

Hitchin-Thorpe condition. LeBrun exploited the curvature estimate coming from the Seiberg-Witten theory to derive that any closed oriented Einstein 4-manifold $M$ with a monopole class satisfies
$$\chi(M) \geq 3 \tau(M)$$
with equality held only by a compact complex hyperbolic 2-space or a flat 4-manifold ([10]), and
Theorem 1.1 (LeBrun [12]). Let $M$ be a smooth closed oriented 4-manifold with a nontrivial Seiberg-Witten invariant. Then $M \# k \overline{\mathbb{C} P^{2}} \# l\left(S^{1} \times S^{3}\right)$ does not admit Einstein metric if $k+4 l>0$ and $k+4 l \geq \frac{1}{3}(2 \chi(M)+3 \tau(M))$.

In this article, we generalize this theorem to :
Theorem 1.2. Let $M$ be a smooth closed oriented 4-manifold with a nontrivial Seiberg-Witten invariant and $N$ be a smooth closed oriented 4-manifold with $b_{2}^{+}(N)=0$. Then $M \# N$ does not admit Einstein metric if
$$b_{2}(N)+4 b_{1}(N)>0$$
and
$$b_{2}(N)+4 b_{1}(N) \geq \frac{1}{3}(2 \chi(M)+3 \tau(M)) .$$

Definition 1. Let $M_{1}$ and $M_{2}$ be smooth $n$-manifolds and suppose that $k$ spheres $c_{1}$ and $c_{2}$ are embedded into $M_{1}$ and $M_{2}$ respectively with trivial normal bundle. A surgery of $M_{1}$ and $M_{2}$ along $c_{i}$ 's are defined as the result of deleting tubular neighborhood of each $c_{i}$ and gluing the remainders by identifying two boundaries $S^{k} \times S^{n-k-1}$ using a diffeomorphism of $S^{k}$ and the reflection map of $S^{n-k-1}$.

Note that the surgery on $M$ with $\left(S^{1} \times S^{3}\right) \# N$ along a null-homotopic circle in $M$ and a circle representing $\left[S^{1}\right] \times\{\mathrm{pt}\} \in H_{1}\left(S^{1} \times S^{3}, \mathbb{Z}\right)$ gives $M \# N$. More generally, we will prove :
Theorem 1.3. Let $M$ be a smooth closed oriented 4-manifold with a nontrivial Seiberg-Witten invariant and $N_{i}$ be a smooth closed oriented 4-manifold with $b_{2}^{+}\left(N_{i}\right)=0$ and $b_{1}\left(N_{i}\right) \geq 1$ for $i=1, \cdots, m$. Suppose that $c_{i} \subset N_{i}$ is an embedded circle nontrivial in $H_{1}\left(N_{i}, \mathbb{R}\right)$ for $i=1, \cdots, m$, and $\tilde{M}$ is a manifold obtained from $M$ by performing a surgery with $\cup_{i=1}^{m} N_{i}$ along $\cup_{i=1}^{m} c_{i}$.

Then $\tilde{M}$ does not admit Einstein metric if
$$\sum_{i=1}^{m}\left(b_{2}\left(N_{i}\right)+4\left(b_{1}\left(N_{i}\right)-1\right)\right)>0$$
and
$$\sum_{i=1}^{m}\left(b_{2}\left(N_{i}\right)+4\left(b_{1}\left(N_{i}\right)-1\right)\right) \geq \frac{1}{3}(2 \chi(M)+3 \tau(M)) .$$

Most generally, we can also allow surgeries along homologically trivial 2-spheres to give :

Theorem 1.4. Let $M$ be a smooth closed oriented 4-manifold with a nontrivial Seiberg-Witten invariant, and $N_{i}, \bar{N}_{j}$ for $i=1, \cdots, m$ and $j=1, \cdots, n$ be smooth closed oriented 4-manifolds such that $b_{2}^{+}\left(N_{i}\right)=b_{2}^{+}\left(\bar{N}_{j}\right)=0$ and $b_{1}\left(N_{i}\right) \geq 1$. Suppose that $c_{i} \subset N_{i}$ for $i=1, \cdots, m$ is an embedded circle nontrivial in $H_{1}\left(N_{i}, \mathbb{R}\right)$, and $F_{j} \subset M$ and $\bar{F}_{j} \subset \bar{N}_{j}$ for $j=1, \cdots, n$ are embedded 2-spheres trivial in $H_{2}(M, \mathbb{R})$ and $H_{2}\left(\bar{N}_{j}, \mathbb{R}\right)$ respectively.

If $\tilde{M}$ is a manifold obtained from $M$ by performing a surgery with $\cup_{i=1}^{m} N_{i}$ along $\cup_{i=1}^{m} c_{i}$, and with $\cup_{j=1}^{n} \bar{N}_{j}$ along $\cup_{j=1}^{n} F_{j}$ and $\cup_{j=1}^{n} \bar{F}_{j}$, then $\tilde{M}$ does not admit Einstein metric if
$$\sum_{i=1}^{m}\left(b_{2}\left(N_{i}\right)+4\left(b_{1}\left(N_{i}\right)-1\right)\right)+\sum_{j=1}^{n}\left(b_{2}\left(\bar{N}_{j}\right)+4\left(b_{1}\left(\bar{N}_{j}\right)+1\right)\right) \geq \frac{1}{3}(2 \chi(M)+3 \tau(M)) .$$
The same conclusion also holds when $m=0$, i.e. $\cup_{i=1}^{m} N_{i}=\emptyset$.

\section*{2. Computation of Seiberg-Witten invariant}

We will give a brief definition of the Seiberg-Witten invariant. Let $M$ be a smooth oriented Riemannian 4 -manifold and $\mathfrak{s}$ be a Spin ${ }^{c}$ structure on it. We assume that $M$ is closed or noncompact with a cylindrical-end metric. Let $\mathbb{A}(M)$ be the graded algebra over $\mathbb{Z}$ defined by
$$\mathbb{Z}\left[H_{0}(M ; \mathbb{Z})\right] \otimes \wedge^{*} H_{1}(M ; \mathbb{Z})$$
with $H_{0}(M ; \mathbb{Z})$ grading two and $H_{1}(M ; \mathbb{Z})$ grading one. An element in $\mathbb{A}(M)$ cannonically gives a cocycle of the Seiberg-Witten moduli space, i.e. the solution space modulo gauge transformations of the Seiberg-Witten equations of $(M, \mathfrak{s})$. Thus the evaluation on the fundamental cycle of the moduli space is the Seiberg-Witten invariant as a function
$$S W_{M, \mathfrak{s}}: \mathbb{A}(M) \rightarrow \mathbb{Z} .$$
When $b_{2}^{+}(M)>1$, this is independent of a Riemannian metric and a perturbation term, thus giving a topological invariant. (If $b_{2}^{+}(M)=1$, it may depend on the chamber.) The first Chern class of a Spin ${ }^{c}$ structure on $M$ whose Seiberg-Witten invariant is nontrivial is called a basic class of $M$. For more details on the Seiberg-Witten invariant, the readers are referred to [13, 14, 16].

We will need the following gluing formulae of the Seiberg-Witten invariant.
Lemma 2.1. Let N be a closed oriented smooth 4-manifold with negativedefinite intersection form $Q$. Then there exists a Spinc structure $\mathfrak{s}^{\prime}$ on $N$ satisfying $c_{1}^{2}\left(\mathfrak{s}^{\prime}\right)=-b_{2}(N)$.

Proof. By the Donaldson's theorem, $Q$ is diagonalizable. (The original Donaldson's theorem [6] is stated for the simply-connected case, but a simple application of the Mayer-Vietoris argument gives this generalization.) Let $\left\{\alpha_{1}, \cdots, \alpha_{b_{2}(N)}\right\}$ be a basis of $H^{2}(N, \mathbb{Z}) \otimes \mathbb{Q}$ diagonalizing $Q$.

We have to show that there exists an element $x \in H^{2}(N, \mathbb{Z})$ such that $Q(x, x)=-b_{2}(N)$, and $x$ is characteristic, i.e. $Q(x, \alpha) \equiv Q(\alpha, \alpha) \bmod 2$ for any $\alpha \in H^{2}(N, \mathbb{Z})$. This is done by taking $x=\sum_{i=1}^{b_{2}(N)} \pm \alpha_{i}$. \(\square\)

Theorem 2.2. Let $M$ and $N$ be smooth closed oriented 4 -manifolds such that $b_{2}^{+}(M)>0, b_{2}^{+}(N)=0$, and $b_{1}(N) \geq 1$. Let $c \subset N$ be an embedded circle nontrivial in $H_{1}(N, \mathbb{R})$ and $\tilde{M}$ be the manifold obtained by performing a surgery on $M$ with $N$ along $c$.

If $\tilde{\mathfrak{s}}$ is the Spin ${ }^{c}$ structure on $\tilde{M}$ obtained by gluing a Spin ${ }^{c}$ structure $\mathfrak{s}$ on $M$ and a Spin ${ }^{c}$ structure $\mathfrak{s}^{\prime}$ on $N$ satisfying $c_{1}^{2}\left(\mathfrak{s}^{\prime}\right)=-b_{2}(N)$, then
$$S W_{\tilde{M}, \tilde{\mathfrak{s}}}\left(a \cdot\left[d_{1}\right] \cdots\left[d_{b_{1}(N)-1}\right]\right)= \pm S W_{M, \mathfrak{s}}(a)$$
for $a \in \mathbb{A}(M)$, where $\left[d_{1}\right], \cdots,\left[d_{b_{1}(N)-1}\right]$ along with $r[c]$ for some $r \in \mathbb{Q}$ form a basis for the non-torsion part of $H_{1}(N, \mathbb{Z})$.

Proof. See [16]. \(\square\)

Theorem 2.3 (Ozsváth and Szabó [14]). Let $M$ be a smooth closed oriented 4-manifold with $b_{2}^{+}(M)>0$. Suppose that $F \subset M$ is an embedded 2-sphere trivial in $H_{2}(M, \mathbb{R})$, and $\tilde{M}$ is the manifold obtained by performing a surgery on $M$ with $S^{4}$ along $F$.

Then for each Spin ${ }^{c}$ structure $\mathfrak{s}$ on $M$, the induced Spin ${ }^{c}$ structure $\tilde{\mathfrak{s}}$ on $\tilde{M}$ satisfies
$$S W_{\tilde{M}, \tilde{\mathfrak{s}}}(a \cdot[\gamma])= \pm S W_{M, \mathfrak{s}}(a)$$
for $a \in \mathbb{A}(M)$, where $\gamma$ is the core of surgery, i.e. a circle $\{p t\} \times D^{2}$ in a small tubular neighborhood $F \times D^{2}$ of $F$.

Generalizing this, we prove :
Theorem 2.4. Let $M$ and $N$ be smooth closed oriented 4 -manifolds such that $b_{2}^{+}(M)>0$, and $b_{2}^{+}(N)=0$. Suppose that $F \subset M$ and $\bar{F} \subset N$ are embedded 2-spheres trivial in $H_{2}(M, \mathbb{R})$ and $H_{2}(N, \mathbb{R})$ respectively, and $\tilde{M}$ is the manifold obtained by performing a surgery on $M$ with $N$ along $F$ and $\bar{F}$.

If $\tilde{\mathfrak{s}}$ is the Spin ${ }^{c}$ structure on $\tilde{M}$ obtained by gluing a Spin ${ }^{c}$ structure $\mathfrak{s}$ on $M$ and a Spin ${ }^{c}$ structure $\mathfrak{s}^{\prime}$ on $N$ satisfying $c_{1}^{2}\left(\mathfrak{s}^{\prime}\right)=-b_{2}(N)$, then
$$S W_{\tilde{M}, \tilde{\mathfrak{s}}}\left(a \cdot[\gamma] \cdot\left[d_{1}\right] \cdots\left[d_{b_{1}(N)}\right]\right)= \pm S W_{M, \mathfrak{s}}(a)$$
for $a \in \mathbb{A}(M)$, where $\gamma$ is a circle $\{p t\} \times D^{2}$ in a small tubular neighborhood $F \times D^{2}$ of $F$, and $\left[d_{1}\right], \cdots,\left[d_{b_{1}(N)}\right]$ form a basis for the non-torsion part of $H_{1}(N, \mathbb{Z})$.

Proof. Perform a surgery on $M$ with $S^{4}$ along $F$ to obtain $M^{\prime}$. In the same way, we get $N^{\prime}$. The surgery on $M^{\prime}$ with $N^{\prime}$ along the circle $\gamma$ gives $\tilde{M}$.
Lemma 2.5. Let $\hat{M}$ be the manifold obtained from $M$ by deleting a small tubular neighborhood of $F$. Then
$$H_{1}\left(M^{\prime}, \mathbb{R}\right) \simeq H_{1}(\hat{M}, \mathbb{R}) \simeq H_{1}(M, \mathbb{R}) \oplus \mathbb{R},$$
and
$$H_{2}\left(M^{\prime}, \mathbb{R}\right) \simeq H_{2}(\hat{M}, \mathbb{R}) \simeq H_{2}(M, \mathbb{R}),$$
where the additional $\mathbb{R}$-factor is generated by $[\gamma]$, and the isomorphisms are induced by the obvious inclusions. Likewise for $N^{\prime}$.

Proof. Obviously $H_{1}\left(M^{\prime}, \mathbb{R}\right) \simeq H_{1}(\hat{M}, \mathbb{R})$, because $\pi_{1}\left(M^{\prime}\right) \simeq \pi_{1}(\hat{M})$ by the Seifert-Van Kampen theorem. To see $H_{1}(\hat{M}, \mathbb{R}) \simeq H_{1}(M, \mathbb{R}) \oplus \mathbb{R}$, it is enough to show that $i_{*}$ in the following commutative diagram of exact sequences is injective.
![](https://cdn.mathpix.com/cropped/55502cba-7d75-4d7c-a6af-f84e8a1ac6e9-05.jpg?height=223&width=771&top_left_y=1259&top_left_x=679)
Suppose not. Then $i^{*}$ in the above diagram is surjective. This means that there exists a nonzero element in $H^{2}(M)$, which is dual to $[F]$, yielding a contradiction. This also means that $[F]$ is zero in $H_{2}(\hat{M}, \mathbb{R})$, which will be used just below.

The fact $H_{2}(\hat{M}, \mathbb{R}) \simeq H_{2}(M, \mathbb{R})$ follows from the exact sequence
$$H_{2}(\partial \hat{M}) \xrightarrow{i_{*}} H_{2}(\hat{M}) \oplus H_{2}\left(S^{2} \times D^{2}\right) \xrightarrow{\varphi} H_{2}(M) \rightarrow 0,$$
and similarly the fact $H_{2}(\hat{M}, \mathbb{R}) \simeq H_{2}\left(M^{\prime}, \mathbb{R}\right)$ follows from the exact sequence
$$H_{2}(\partial \hat{M}) \xrightarrow{i_{*}} H_{2}(\hat{M}) \oplus H_{2}\left(D^{3} \times S^{1}\right) \xrightarrow{\varphi} H_{2}\left(M^{\prime}\right) \rightarrow 0,$$
where the sequences end with 0, because $i_{*}: H_{1}(\partial \hat{M}) \rightarrow H_{1}(\hat{M})$ is injective. \(\square\)

Note that $\mathfrak{s}$ and $\mathfrak{s}^{\prime}$ restrict to be trivial on $F$ and $\bar{F}$ respectively. Thus we abuse the notation to let $\mathfrak{s}$ and $\mathfrak{s}^{\prime}$ be the induced Spin ${ }^{c}$ structures on $M^{\prime}$ and $N^{\prime}$ respectively. By theorem 2.3,
$$S W_{M^{\prime}, \mathfrak{s}}(a \cdot[\gamma])= \pm S W_{M, \mathfrak{s}}(a)$$
for $a \in \mathbb{A}(M)$. Applying theorem 2.2,
$$S W_{M^{\prime}, \mathfrak{s}}(a \cdot[\gamma])= \pm S W_{\tilde{M}, \tilde{\mathfrak{s}}}\left(a \cdot[\gamma] \cdot\left[d_{1}\right] \cdots\left[d_{b_{1}(N)}\right]\right)$$
for $a \in \mathbb{A}(M)$. \(\square\)

\section*{3. Proof of Theorem 1.3}

We need to have a basic class on $\tilde{M}$. Let $\mathfrak{s}$ be the $\operatorname{Spin}^{c}$ structure on $M$ with a nontrivial Seiberg-Witten invariant. Applying theorem 2.2 successively, $\tilde{M}$ has nontrivial Seiberg-Witten invariant for $\tilde{\mathfrak{s}}$. Write $c_{1}(\tilde{\mathfrak{s}})$ as $c_{1}(\mathfrak{s})+E$ where $E=c_{1}\left(\mathfrak{s}^{\prime}\right)$ coming from $\cup_{i=1}^{m} N_{i}$.

Then the proof proceeds in a similar way to [12]. First,
$$\begin{aligned}
\chi(\tilde{M}) & =\chi(M)+\sum_{i=1}^{m} \chi\left(N_{i}\right) \\
& =\chi(M)+\sum_{i=1}^{m}\left(2-2 b_{1}\left(N_{i}\right)+b_{2}\left(N_{i}\right)\right),
\end{aligned}$$
and
$$H_{2}(\tilde{M}, \mathbb{Z}) \simeq H_{2}(M, \mathbb{Z}) \oplus\left(\oplus_{i=1}^{m} H_{2}\left(N_{i}, \mathbb{Z}\right)\right)$$
by a simple Mayer-Vietoris argument. (Here, we use the fact that $c_{i}$ 's are all non-torsion.) Thus
$$\begin{aligned}
2 \chi(\tilde{M})+3 \tau(\tilde{M})= & 2 \chi(M)+3 \tau(M) \\
& -\sum_{i=1}^{m}\left(b_{2}\left(N_{i}\right)+4\left(b_{1}\left(N_{i}\right)-1\right)\right) .
\end{aligned}$$

Lemma 3.1. Any Riemannian metric $g$ on $\tilde{M}$ satisfies
$$\frac{1}{4 \pi^{2}} \int_{\tilde{M}}\left(\frac{s_{g}^{2}}{24}+2\left|W_{+}\right|_{g}^{2}\right) d \mu_{g} \geq \frac{2}{3}(2 \chi(M)+3 \tau(M))$$
Proof. Since $c_{1}(\mathfrak{s})+E$ and $c_{1}(\mathfrak{s})-E$ are basic classes of $\tilde{M}$, LeBrun's estimate [12] gives
$$\frac{1}{4 \pi^{2}} \int_{\tilde{M}}\left(\frac{s_{g}^{2}}{24}+2\left|W_{+}\right|_{g}^{2}\right) d \mu_{g} \geq \frac{2}{3}\left(\left(c_{1}(\mathfrak{s}) \pm E\right)^{+}\right)^{2}$$
where $(\cdot)^{+}$denotes the self-dual harmonic part. On the other hand,
$$\begin{aligned}
\left(\left(c_{1}(\mathfrak{s}) \pm E\right)^{+}\right)^{2} & =\left(c_{1}(\mathfrak{s})^{+} \pm E^{+}\right)^{2} \\
& =\left(c_{1}(\mathfrak{s})^{+}\right)^{2} \pm 2 c_{1}(\mathfrak{s})^{+} \cdot E^{+}+\left(E^{+}\right)^{2} \\
& \geq\left(c_{1}(\mathfrak{s})^{+}\right)^{2} \pm 2 c_{1}(\mathfrak{s})^{+} \cdot E^{+} .
\end{aligned}$$

Thus at least one of $\left(\left(c_{1}(\mathfrak{s})+E\right)^{+}\right)^{2}$ and $\left(\left(c_{1}(\mathfrak{s})-E\right)^{+}\right)^{2}$ should be greater than or equal to $\left(c_{1}(\mathfrak{s})^{+}\right)^{2}$. Say $\left(\left(c_{1}(\mathfrak{s})+E\right)^{+}\right)^{2} \geq\left(c_{1}(\mathfrak{s})^{+}\right)^{2}$. Then
$$\begin{aligned}
\left(\left(c_{1}(\mathfrak{s})+E\right)^{+}\right)^{2} & \geq c_{1}^{2}(\mathfrak{s}) \\
& \geq 2 \chi(M)+3 \tau(M),
\end{aligned}$$
where we used the fact that $d(\mathfrak{s}):=\frac{1}{4}\left(c_{1}^{2}(\mathfrak{s})-(2 \chi(M)+3 \tau(M))\right)$, the dimension of the Seiberg-Witten moduli space of $(M, \mathfrak{s})$ is nonnegative. \(\square\)

Now suppose that $g$ is an Einstein metric on $\tilde{M}$. Then the Chern-Gauss-Bonnet formula gives :
$$\begin{aligned}
2 \chi(\tilde{M})+3 \tau(\tilde{M}) & =\frac{1}{4 \pi^{2}} \int_{\tilde{M}}\left(\frac{s_{g}^{2}}{24}+2\left|W_{+}\right|_{g}^{2}-\frac{|\stackrel{\circ}{r}|_{g}^{2}}{2}\right) d \mu_{g} \\
& =\frac{1}{4 \pi^{2}} \int_{\tilde{M}}\left(\frac{s_{g}^{2}}{24}+2\left|W_{+}\right|_{g}^{2}\right) d \mu_{g} \\
& \geq \frac{2}{3}(2 \chi(M)+3 \tau(M))
\end{aligned}$$
Combined with (3.1), it follows that
$$\frac{1}{3}(2 \chi(M)+3 \tau(M)) \geq \sum_{i=1}^{m}\left(b_{2}\left(N_{i}\right)+4\left(b_{1}\left(N_{i}\right)-1\right)\right) .$$

It remains to deal with the equality case in the above inequality. Suppose the equality holds. Then from the above we have
$$\left(\left(c_{1}(\mathfrak{s})+E\right)^{+}\right)^{2}=c_{1}^{2}(\mathfrak{s})=2 \chi(M)+3 \tau(M) .$$
Suppose $\sum_{i=1}^{m}\left(b_{2}\left(N_{i}\right)+4\left(b_{1}\left(N_{i}\right)-1\right)\right)>0$, which implies
$$\left(\left(c_{1}(\mathfrak{s})+E\right)^{+}\right)^{2}>0$$
by (3.3) and (3.4).
From the the equality in (3.2), LeBrun's result [12] says that $(\tilde{M}, g)$ must be almost-Kähler with almost-Kähler form a multiple of $\left(c_{1}(\mathfrak{s})+E\right)^{+}$such that the basic class $c_{1}(\mathfrak{s})+E$ being the (anti)canonical class of the associated almost-complex structure, and the almost-Kähler form is an eigenvector of $W_{+}$everywhere.

Applying Armstrong's result [2] that any closed almost-Kähler Einstein 4-manifold whose almost-Kähler form is an eigenvector of $W_{+}$everywhere is Kähler, or Apostolov-Armstrong-Drăghici's result [1] that any closed almost-Kähler 4-manifold which saturates (3.2) and whose Ricci tensor is invariant under the almost-complex structure is Kähler, we conclude that $(\tilde{M}, g)$ is Kähler.

Since $(\tilde{M}, g)$ is Kähler-Einstein, we can apply the Enriques-Kodaira classification of compact complex surfaces. Since $\tilde{M}$ has a nontrivial Seiberg-Witten invariant, its Kodaira dimension is nonnegative. Then it is minimal, because it admits a Kähler-Einstein metric.

Now the anti-canonical class is non-torsion, because $c_{1}^{2}(\mathfrak{s})>0$ from (3.4). Then the basic classes of such a minimal Kähler surface are numerically equivalent to $r c_{1}(K)$, where $|r| \leq 1$ is a rational number, and $K$ is the canonical line bundle. (See [13].) But $\pm\left(c_{1}(\mathfrak{s}) \pm E\right)$ are basic classes of $\tilde{M}$. This means that $E=0$, implying that
$$b_{2}\left(N_{i}\right)=0 \quad \forall i .$$

Finally using Wu's formula [18, 7] for a closed almost-complex 4-manifold, and (3.4),
$$\begin{aligned}
0 & =\left(c_{1}(\mathfrak{s})+E\right)^{2}-(2 \chi(\tilde{M})+3 \tau(\tilde{M})) \\
& =c_{1}(\mathfrak{s})^{2}-\sum_{i=1}^{m} b_{2}\left(N_{i}\right)-\left(2 \chi(M)+3 \tau(M)-\sum_{i=1}^{m}\left(b_{2}\left(N_{i}\right)+4\left(b_{1}\left(N_{i}\right)-1\right)\right)\right) \\
& =\sum_{i=1}^{m} 4\left(b_{1}\left(N_{i}\right)-1\right),
\end{aligned}$$
implying that
$$b_{1}\left(N_{i}\right)=1 \quad \forall i .$$
Thus $\sum_{i=1}^{m}\left(b_{2}\left(N_{i}\right)+4\left(b_{1}\left(N_{i}\right)-1\right)\right)=0$, yielding a contradiction.

\section*{4. Proof of Theorem 1.4}

By successively applying theorem 2.2 and 2.4, the Seiberg-Witten invariant of $(\tilde{M}, \tilde{\mathfrak{s}})$ is nontrivial, where $\tilde{\mathfrak{s}}$ is the $\operatorname{Spin}^{c}$ structure gotten by gluing $\mathfrak{s}$ on $M$ which has nontrivial Seiberg-Witten invariant and $\mathfrak{s}^{\prime}$ on $\left(\cup_{i=1}^{m} N_{i}\right) \cup\left(\cup_{j=1}^{m} \bar{N}_{j}\right)$ such that $c_{1}^{2}\left(\left.\mathfrak{s}^{\prime}\right|_{N_{i}}\right)=-b_{2}\left(N_{i}\right)$ and $c_{1}^{2}\left(\left.\mathfrak{s}^{\prime}\right|_{\bar{N}_{j}}\right)=-b_{2}\left(\bar{N}_{j}\right)$ for all $i, j$.

As before, we have
$$\begin{aligned}
\chi(\tilde{M}) & =\chi(M)+\sum_{i=1}^{m} \chi\left(N_{i}\right)+\sum_{j=1}^{n}\left(\chi\left(\bar{N}_{j}\right)-4\right) \\
& =\chi(M)+\sum_{i=1}^{m}\left(2-2 b_{1}\left(N_{i}\right)+b_{2}\left(N_{i}\right)\right)+\sum_{j=1}^{n}\left(-2-2 b_{1}\left(\bar{N}_{j}\right)+b_{2}\left(\bar{N}_{j}\right)\right),
\end{aligned}$$
and
$$H_{2}(\tilde{M}, \mathbb{R}) \simeq H_{2}(M, \mathbb{R}) \oplus\left(\oplus_{i=1}^{m} H_{2}\left(N_{i}, \mathbb{R}\right)\right) \oplus\left(\oplus_{j=1}^{n} H_{2}\left(\bar{N}_{j}, \mathbb{R}\right)\right)$$
by a simple Mayer-Vietoris argument. (Here, we use the fact that $c_{i}$ 's are non-torsion, and $F_{j}$ 's and $\bar{F}_{j}$ 's are all torsion.) Thus
$$\begin{aligned}
2 \chi(\tilde{M})+3 \tau(\tilde{M})= & 2 \chi(M)+3 \tau(M)-\sum_{i=1}^{m}\left(b_{2}\left(N_{i}\right)+4\left(b_{1}\left(N_{i}\right)-1\right)\right) \\
& -\sum_{j=1}^{n}\left(b_{2}\left(\bar{N}_{j}\right)+4\left(b_{1}\left(\bar{N}_{j}\right)+1\right)\right) .
\end{aligned}$$
Now proceeding in the same way as theorem 1.3, the existence of an Einstein metric on $\tilde{M}$ dictates that
$$\frac{1}{3}(2 \chi(M)+3 \tau(M)) \geq \sum_{i=1}^{m}\left(b_{2}\left(N_{i}\right)+4\left(b_{1}\left(N_{i}\right)-1\right)\right)+\sum_{j=1}^{n}\left(b_{2}\left(\bar{N}_{j}\right)+4\left(b_{1}\left(\bar{N}_{j}\right)+1\right)\right),$$
and if the equality holds, then the left hand side of the above inequality is positive, and the same argument as theorem 1.3 gives that
$$b_{2}\left(N_{i}\right)=b_{2}\left(\tilde{N}_{j}\right)=0 \quad \forall i, j,$$
and
$$\left.\sum_{i=1}^{m} 4\left(b_{1}\left(N_{i}\right)-1\right)\right)+\sum_{j=1}^{n} 4\left(b_{1}\left(\bar{N}_{j}\right)+1\right)=0$$
which is a contradiction.

\section*{5. Final Remarks}

Unlike the surgery with $N$ with $b_{2}^{+}(N)=0$, in case of a surgery with 4manifolds with $b_{2}^{+}>0$ it is difficult to decide the existence of Einstein metric, because those surgered manifolds have no basic classes and it is very difficult to show the existence of Seiberg-Witten equations for a general metric.

Ishida and LeBrun used the Bauer-Furuta invariant [3, 4] whose nonvanishing also guarantees the existence of Seiberg-Witten equations for any metric to show the nonexistence of Einstein metric on some connected sums of Kähler surfaces. As in [9], let $X_{j}$ for $j=1, \cdots, 4$ be smooth closed almost-complex 4-manifolds satisfying
$$b_{1}\left(X_{j}\right)=0, \quad b_{2}^{+}\left(X_{j}\right) \equiv 3 \bmod 4, \quad \sum_{j=1}^{4} b_{2}^{+}\left(X_{j}\right) \equiv 4 \bmod 8,$$
and $N$ be any smooth closed oriented 4-manifold with $b_{2}^{+}(N)=0$. Suppose that all $X_{i}$ 's have nonzero mod-2 Seiberg-Witten invariants. Then, for each $m=2,3,4$,
$$\left(\#_{j=1}^{m} X_{j}\right) \# N$$
does not admit Einstein metric if
$$4 m-(2 \chi(N)+3 \tau(N)) \geq \frac{1}{3} \sum_{j=1}^{m} c_{1}^{2}\left(X_{j}\right) .$$

Finally one can use the $G$-monopole invariant [15] which is roughly the "count" of $G$-invariant solutions of the Seiberg-Witten equations modulo gauge transformation to show the nonexistence of $G$-invariant Einstein metric on some 4-manifolds with a $G$-action for a compact Lie group $G$.

\section*{References}
\begin{itemize}
\item[] [1] V. Apostolov, J. Armstrong, and T. Drăghici, Local rigidity of certain classes of almost Kähler 4-manifolds, Ann. Glob. Anal. Geom. 21 (2002) 151-176.
\item[] [2] J. Armstrong, An ansatz for almost-Kähler, Einstein 4-manifolds, J. Reine Angew. Math. 542 (2002) 53-84.
\item[] [3] S. Bauer and M. Furuta, A stable cohomotopy refinement of Seiberg-Witten invariants: $I$, Invent. Math. 155 (2004), 1-19.
\item[] [4] S. Bauer, A stable cohomotopy refinement of Seiberg-Witten invariants: II, Invent. Math. 155 (2004), 21-40.
\item[] [5] A. Besse, Einstein Manifolds, Springer-Verlag (1987).
\item[] [6] S. Donaldson, An application of gauge theory to four dimensional topology, J. Diff. Geom. 18 (1983), 279-315.
\item[] [7] F. Hirzebruch and H. Hopf, Felder von Flächenelementen in 4-dimensionalen Mannigfaltigkeiten, Math. Ann. 136 (1958), 156-172.
\item[] [8] N. Hitchin, On compact four-dimensional Einstein manifolds, J. Diff. Geom. 9 (1974), 435-441.
\item[] [9] M. Ishida and C. LeBrun, Curvature, Connected Sums, and Seiberg-Witten Theory, Comm. Anal. Geom. 11 (2003) 809-836.
\item[] [10] C. LeBrun, Einstein metrics and Mostow rigidity, Math. Res. Lett. 2 (1995), 1-8.
\item[] [11] C. LeBrun, Four manifolds without Einstein metrics, Math. Res. Lett. 3 (1996), 133-147.
\item[] [12] C. LeBrun, Ricci curvature, minimal volumes, and Seiberg-Witten theory, Invent. Math. 145 (2001), 279-316.
\item[] [13] J. Morgan, The Seiberg-Witten Equations and applications to the topology of smooth four-manifolds, Princeton University Press, 1996.
\item[] [14] P. Ozsváth and Z. Szabó, Higher type adjunction inequalities in Seiberg-Witten theory, J. Diff. Geom. 55 (2000), 385-440.
\item[] [15] Y. Ruan, Virtual neighborhoods and the monopole equations, Topics in symplectic 4-manifolds, 101-116, First Int. Press Lect. Ser. I, Int. Press, Cambridge, MA, 1998.
\item[] [16] C. Sung, Surgery, Yamabe invariant, and Seiberg-Witten theory, J. Geom. Phys. 59 (2009), 246-255.
\item[] [17] J. Thorpe, Some remarks on the Gauss-Bonnet integral, J. Math. Mech. 18 (1969), 779-786.
\item[] [18] W.-T. Wu, Sur le classes caracteristique des structures fibrées sphériques, Actualités Sci. Ind. 1183 (1952), 1-89.
\end{itemize}

Dept. of Mathematics and Institute for Mathematical Sciences, Konkuk University, 1 Hwayang-dong, Gwangjin-gu, Seoul, KOREA
E-mail address: cysung@kias.re.kr
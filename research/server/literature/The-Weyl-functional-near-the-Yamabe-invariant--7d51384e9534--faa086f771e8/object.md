# The Weyl functional near the Yamabe invariant

- Category: papers
- Identity: arxiv:math/0201153
- Content status: fulltext_ok

---

---
source_file: math_0201153.pdf
converter: mathpix
format: mmd
---

\title{
The Weyl functional near the Yamabe invariant
}

\author{
Kazuo Akutagawa, Boris Botvinnik, Osamu Kobayashi, Harish Seshadri
}

\begin{abstract}
For a compact manifold $M$ of $\operatorname{dim} M=n \geq 4$, we study two conformal invariants of a conformal class $C$ on $M$. These are the Yamabe constant $Y_{C}(M)$ and the $L^{\frac{n}{2}}$ -norm $W_{C}(M)$ of the Weyl curvature. We prove that for any manifold $M$ there exists a conformal class $C$ such that the Yamabe constant $Y_{C}(M)$ is arbitrarily close to the Yamabe invariant $Y(M)$, and, at the same time, the constant $W_{C}(M)$ is arbitrarily large. We study the image of the map $\mathrm{W}: C \mapsto\left(Y_{C}(M), W_{C}(M)\right) \in \mathbf{R}^{2}$ near the line $\{(Y(M), w) \mid w \in \mathbf{R}\}$. We also apply our results to certain classes of 4-manifolds, in particular, minimal compact Kähler surfaces of Kodaira dimension 0, 1 or 2.
\end{abstract}

\section*{1 Introduction: results and examples}
T.1. The Yamabe constant/invariant. Let $M$ be a smooth compact (without boundary) manifold of $\operatorname{dim} M=n \geq 3$. We denote by $\mathcal{R} \operatorname{iem}(M)$ the space of the Riemannian metrics on $M$, and by $\mathcal{C}(M)$ the space of conformal classes of Riemannian metrics on $M$. The Einstein-Hilbert functional $I: \mathcal{R} \operatorname{iem}(M) \rightarrow \mathbf{R}$ is given as
$$I(g)=\frac{\int_{M} R_{g} d \sigma_{g}}{\operatorname{Vol}_{g}(M)^{\frac{n-2}{n}}},$$
where $R_{g}$ is the scalar curvature and $d \sigma_{g}$ is the volume form of $g$. It is well-known that the functional $I$ is not bounded from above and below for any manifold, and the set of critical points of $I$ coincides with the Einstein metrics on $M$. Let $C \in \mathcal{C}(M)$ be a conformal class. The restiction $\left.I\right|_{C}$ is always bounded from below. The constant
$$Y_{C}(M):=\inf _{g \in C} I(g)$$
is known as the Yamabe constant of the conformal class $C$. The Yamabe constant satisfies the inequality $Y_{C}(M) \leq Y_{C_{0}}\left(S^{n}\right)$, where the equality holds if and only if the manifold $(M, C)$ is conformally equivalent to the standard sphere $S^{n}$ with the standard conformal class $C_{0}$. Then the supremum
$$Y(M):=\sup _{C \in \mathcal{C}(M)} Y_{C}(M)$$
is the Yamabe invariant of $M$. The Yamabe constant $Y_{C}(M)$ is an important conformal invariant. In particular, for any conformal class $C \in \mathcal{C}(M)$, there exists a metric (Yamabe metric) $\check{g} \in C$ such that $I(\check{g})=Y_{C}(M)$. The Yamabe metric has constant scalar curvature $R_{\breve{g}}=Y_{C}(M)$ under the normalization $\operatorname{Vol}_{\breve{g}}(M)=1$.
1.2. The Weyl functional. Now let $\operatorname{dim} M \geq 4$. We denote by $W_{g}=\left(W^{i}{ }_{j k \ell}\right)$ the Weyl tensor of a metric $g \in \mathcal{R} i e m(M)$. The norm $\left|W_{g}\right|_{g}$ is defined as
$$\left|W_{g}\right|_{g}=\left(W_{j k \ell}^{i} W_{i}^{j k \ell}\right)^{1 / 2} .$$
Let $C \in \mathcal{C}(M)$, and let $g \in C$ be any metric. Then the integral
$$W_{C}(M):=\int_{M}\left|W_{g}\right|_{g}^{\frac{n}{2}} d \sigma_{g}$$
does not depend on the choice of the metric $g \in C$. The map $\mathcal{C}(M) \rightarrow \mathbf{R}, C \mapsto W_{C}(M)$, is called the Weyl functional. We shall call $W_{C}(M)$ the Weyl constant of the conformal class $C$ and the infimum
$$W(M):=\inf _{C \in \mathcal{C}(M)} W_{C}(M)$$
the Weyl invariant of $M$. Clearly the invariant $W(M)$ is a diffeomorphism invariant as well as $Y(M)$.
1.3. General results. To state our main results, we define one more numerical invariant $\omega(M)$ as follows. Firstly, for a given manifold $M$, we say that a sequence $\left\{C_{i}\right\}, C_{i} \in \mathcal{C}(M)$, of conformal classes is a Yamabe sequence if
$$\lim _{i \rightarrow \infty} Y_{C_{i}}(M)=Y(M) .$$
In particular, if there exists a class $C \in \mathcal{C}(M)$ satisfying $Y(M)=Y_{C}(M)$, the sequence $C_{i}=C$ for $i \geq 1$ is a Yamabe sequence. Secondly, we define the constant
$$\omega\left(M,\left\{C_{i}\right\}\right):=\liminf _{i \rightarrow \infty} W_{C_{i}}(M) \geq 0$$
for any Yamabe sequence $\left\{C_{i}\right\}$. Then the invariant $\omega(M)$ is defined as
$$\omega(M):=\inf \left\{\omega\left(M,\left\{C_{i}\right\}\right) \mid\left\{C_{i}\right\} \text { is a Yamabe sequence }\right\} .$$
Notice that $\omega(M) \geq W(M)$ by definition. Also it easy to show that $\omega(M)=0$ for $M=S^{n}$, $S^{1} \times S^{n-1}, T^{n}$ and their connected sums.

Theorem A. Let $M$ be a compact manifold of $\operatorname{dim} M=n \geq 4$. Then for any small $\varepsilon>0$ and any constant $\kappa>\omega(M)$ there exists a conformal class $C \in \mathcal{C}(M)$ such that
$$\left\{\begin{array}{l}
Y_{C}(M) \geq Y(M)-\varepsilon, \\
\kappa+\varepsilon \geq W_{C}(M) \geq \kappa .
\end{array}\right.$$

Remark 1.1. If $\omega(M)=+\infty$, Theorem A delivers an empty statement. It is not clear that the invariant $\omega(M)$ is finite for every compact manifold $M$. However, without the finiteness of $\omega(M)$, the following statement still holds.

Theorem A'. Let $M$ be a compact manifold of $\operatorname{dim} M=n \geq 4$. Then for any small $\varepsilon>0$ and any constant $\kappa>0$ there exists a conformal class $C \in \mathcal{C}(M)$ such that
$$\left\{\begin{array}{l}
Y_{C}(M) \geq Y(M)-\varepsilon \\
W_{C}(M) \geq \kappa
\end{array}\right.$$
We prove Theorem A in two steps. Firstly, we prove Theorem A for $M=S^{n}$ by constructing a conformal class $C \in \mathcal{C}\left(S^{n}\right)$ satisfying (1) with the understanding that $\omega\left(S^{n}\right)=0$. Secondly, we prove the general case by constructing an appropriate conformal class on the connected sum $M \# S^{n}$. Theorem A' follows immediately from our argument as well.

To proceed further, we would like to introduce some terminology.
1.4. The YW-quadrant, Yamabe corner, Sobolev and Kuiper lines. For a compact manifold $M$ we consider the map
$$\mathrm{W}: \mathcal{C}(M) \longrightarrow \mathbf{R}^{2}, \quad C \mapsto\left(Y_{C}(M), W_{C}(M)\right) .$$
We denote by $\mathbf{K}^{\mathrm{W}}(M) \subset \mathbf{R}^{2}$ the image of the map $\mathbf{W}$. By definition, the set $\mathbf{K}^{\mathbf{W}}(M)$ is a diffeomorphism invariant of $M$.
The third author observed that the set $\mathbf{K}^{\mathrm{W}}(M)$ contains certain interesting aspects of conformal geometry, and he studied some of its properties (cf. [11], [12]).
Let $(y, w)$ be the Euclidian coordinates in $\mathbf{R}^{2}$. Consider the W -quadrant of a manifold $M$ :
$$\mathbf{Q}^{\mathrm{W} \mathrm{~W}}(M):=\{(y, w) \mid y \leq Y(M), \quad w \geq W(M)\},$$
see Fig. 1.1. Clearly $\mathbf{K}^{\mathrm{W}}(M) \subset \mathbf{Q}^{\mathrm{W}}(M)$. We emphasize that there is not much known about the shape of the set $\mathbf{K}^{\mathrm{W}}(M) \subset \mathbf{Q}^{\mathrm{W}}(M)$. In this paper we study the set $\mathbf{K}^{\mathrm{W}}(M)$ near the Sobolev line defined below.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/7154e6c7-f149-4bc9-a073-5210e0e5e33d-03.jpg?height=430&width=1063&top_left_y=1597&top_left_x=706}
\captionsetup{labelformat=empty}
\caption{Fig. 1.1. The YW-quadrant of $M$. Here $Y(M)>0, W(M)>0$.}
\end{figure}
We explain the notations and terminology given in Fig. 1.1. We call the point $(Y(M), W(M))$ the Yamabe corner of $M$. Then we call the line $\{y=Y(M)\}$ the Sobolev line. This name is motivated by the following observation. Let $Y(M)>0$, and let $C$ be a positive conformal class (i.e. $Y_{C}(M)>0$ ). We denote by $\check{g} \in C$ a Yamabe metric. Then the following inequality holds (cf. [1])
$$\left(\int_{M}|f|^{\frac{2 n}{n-2}} d \sigma_{\check{g}}\right)^{\frac{n-2}{n}} \leq \frac{1}{\frac{n-2}{4(n-1)} Y_{C}(M)} \int_{M}|d f|_{\check{g}}^{2} d \sigma_{\check{g}}+\frac{1}{\operatorname{Vol}_{\check{g}}(M)^{\frac{2}{n}}} \int_{M} f^{2} d \sigma_{\check{g}}$$
for $f \in L_{\tilde{g}}^{1,2}(M)$, where $L_{\tilde{g}}^{1,2}(M)$ denotes the Sobolev space of $L^{2}$-functions with $L^{2}$ first derivatives relative to $\check{g}$. In particular, the constant $\frac{n-2}{4(n-1)} Y_{C}(M)$ is the best Sobolev constant for the Sobolev embedding $L_{\tilde{g}}^{1,2}(M) \subset L_{\tilde{g}}^{\frac{2 n}{n-2}}(M)$. Furthermore, $\frac{n-2}{4(n-1)} Y(M)$ is the supremum of those Sobolev constants. We notice that
$$\mathbf{K}^{\mathrm{WV}}\left(S^{n}\right) \cap\left\{\text { the Sobolev line of } S^{n}\right\}=\left\{\left(Y\left(S^{n}\right), 0\right)\right\}=\left\{\text { the Yamabe corner of } S^{n}\right\}$$
for all $n \geq 4$ due to the final resolution of the Yamabe problem by Schoen [23]. The case $Y(M) \leq 0$ does not have such interpretation, however, it is convenient to use this term in general case.

We call the line $\{w=W(M)\}$ the Kuiper line of $M$ (see Gursky's paper [6] for some remarkable results on the Kuiper lines of 4-manifolds). Our motivation for this name comes from the Kuiper Theorem [15]: if $W_{C}\left(S^{n}\right)=0$ for a conformal class $C \in \mathcal{C}\left(S^{n}\right)$, then $C$ is equivalent (up to a diffeomorphism) to the standard conformal class $C_{0}$. In our terms,
$$\mathbf{K}^{\mathbf{W}}\left(S^{n}\right) \cap\left\{\text { the Kuiper line of } S^{n}\right\}=\left\{\left(Y\left(S^{n}\right), 0\right)\right\}=\left\{\text { the Yamabe corner of } S^{n}\right\} .$$
In terms of the set $\mathbf{K}^{\mathrm{W}}(M)$, Theorem A implies the following.
Corollary B. Let $M$ be a compact manifold of $\operatorname{dim} M=n \geq 4$. Then
$$\overline{\mathbf{K}^{\mathrm{W}}(M)} \cap\{\text { the Sobolev line of } M\}=\{y=Y(M), w \geq \omega(M)\} .$$
Here $\overline{\mathbf{K}^{\mathrm{W}}(M)}$ is the closure of $\mathbf{K}^{\mathrm{W}}(M) \subset \mathbf{R}^{2}$.
1.5. The Einstein and the gap curves. Here we consider only 4-dimensional manifolds. For a manifold $M$ we denote by $\chi(M)$ and $\tau(M)$ the Euler characteristic and the signature of $M$ respectively. The Hirzebruch signature formula gives the following result.

Proposition 1.1. Let $M$ be an oriented, compact 4-manifold. Then for any $C \in \mathcal{C}(M)$,
$$W_{C}(M) \geq 48 \pi^{2}|\tau(M)|$$
with the equality if and only if $(M, C)$ is half conformally flat (i.e. self-dual or anti self-dual). In particular, $W(M) \geq 48 \pi^{2}|\tau(M)|$.

The Chern-Gauss-Bonnet formula leads to the following interesting result.
Theorem 1.2. ([12, Section 1-(i)]) Let $M$ be a compact 4-manifold. Then for any conformal class $C \in \mathcal{C}(M)$ the following inequality holds:
$$W_{C}(M) \geq 32 \pi^{2} \chi(M)-\frac{1}{6} Y_{C}(M)^{2}$$
with the equality if and only if the conformal class $C$ contains an Einstein metric.
We call the curve $w=32 \pi^{2} \chi(M)-\frac{1}{6} y^{2}, w \geq W(M), y \leq Y(M)$, the Einstein curve of $M$.
On the other hand, the Gap Theorems due to Gursky [7, Theorem 3.3, Proposition 3.5] and Gursky-LeBrun [9, Theorem 1] can be reformulated as follows.

Theorem 1.3. (Gap Theorem) Let $M$ be an oriented, compact 4-manifold and $C \in \mathcal{C}(M)$ a conformal class satisfying $Y_{C}(M)>0$. Assume that either
\begin{itemize}
\item[(i)] $b_{2}^{+}(M)=\operatorname{dim} H_{+}^{2}(M ; \mathbf{R})>0$, or
\item[(ii)] $C$ contains an Einstein metric and $W_{g}^{+} \not \equiv 0$ for $g \in C$.
\end{itemize}

Then the following inequality holds:
$$W_{C}(M) \geq \frac{1}{3} Y_{C}(M)^{2}-48 \pi^{2} \tau(M) .$$
Here $W_{g}^{+}$is the self-dual Weyl curvature of $g$.
We call the curve $w=\frac{1}{3} y^{2}-48 \pi^{2} \tau(M), w \geq 0, y \geq 0$, the gap curve of $M$.
1.6. Examples. 1. Let $M=S^{4}$. Then we have $W\left(S^{4}\right)=0, Y\left(S^{4}\right)=8 \pi \sqrt{6}$. The Einstein and the gap curves are $w=64 \pi^{2}-\frac{1}{6} y^{2}, w=\frac{1}{3} y^{2}$ respectively. We notice that $Y\left(S^{4}\right)=8 \pi \sqrt{6}$ coincides with the value of $y$ given by the intersection of the Einstein curve with $w=0$. We have
$$\begin{aligned}
& \mathbf{K}^{\mathbf{W}}\left(S^{4}\right) \cap\left\{\text { the Sobolev line of } S^{4}\right\}=\left\{\text { the Yamabe corner of } S^{4}\right\}, \\
& \mathbf{K}^{\mathbf{W} \mathrm{W}}\left(S^{4}\right) \cap\left\{\text { the Kuiper line of } S^{4}\right\}=\left\{\text { the Yamabe corner of } S^{4}\right\} .
\end{aligned}$$
On the other hand, Corollary B implies that
$$\overline{\mathbf{K}^{\mathfrak{W}}\left(S^{4}\right)} \cap\left\{\text { the Sobolev line of } S^{4}\right\}=\{y=8 \pi \sqrt{6}, w \geq 0\} .$$
We have the following picture for $S^{4}$ :

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/7154e6c7-f149-4bc9-a073-5210e0e5e33d-05.jpg?height=566&width=957&top_left_y=1457&top_left_x=776}
\captionsetup{labelformat=empty}
\caption{Fig. 1.2. The YW-picture of $S^{4}$.}
\end{figure}
Here and below we shade a subset of $\mathbf{Q}^{\mathrm{W}}(M)$ which still contains $\mathbf{K}^{\mathrm{W}}(M)$. We call it the "YW-picture of $M$ ".
Then Theorem 1.3 implies that the intersection $\mathbf{K}^{\mathrm{W}}\left(S^{4}\right) \cap\left\{\right.$ the Einstein curve of $\left.S^{4}\right\}$ does not contain the points with $8 \pi \sqrt{2}<y<8 \pi \sqrt{6}$. It is not known whether this intersection contains any points except the Yamabe corner.
Example 2. Let $M=\mathbf{C P}^{2}$. The Einstein curve and the gap curves are given as $w=$ $98 \pi^{2}-\frac{1}{6} y^{2}$ and $w=\frac{1}{3} y^{2}-48 \pi^{2}$ respectively.

It is known that $W\left(\mathbf{C P}^{2}\right)=48 \pi^{2}$ (it follows from Proposition 1.1) and $Y\left(\mathbf{C P}^{2}\right)=12 \pi \sqrt{2}$ (LeBrun [18], Gursky-LeBrun [8]), where $Y\left(\mathbf{C P}^{2}\right)$ is attained by the conformal class $\left[g_{F S}\right]$ of the Fubini-Study metric $g_{F S}$ on $\mathbf{C P}^{2}$. In particular, $\omega\left(\mathbf{C P}^{2}\right)=W_{\left[g_{F S}\right]}\left(\mathbf{C P}^{2}\right)=W\left(\mathbf{C P}^{2}\right)=$ $48 \pi^{2}$. The YW -picture of $\mathbf{C P}^{2}$ is shown at Fig. 1.3 below. Here the Yamabe corner coincides with the intersection of the Sobolev line, Kuiper line and the Einstein curve (and the gap curve). Moreover, it follows from Gursky-LeBrun's result [8, Theorem 7] that
$\mathbf{K}^{\mathrm{W}}\left(\mathbf{C P}^{2}\right) \cap\left\{\right.$ the Sobolev line of $\left.\mathbf{C P}^{2}\right\}=\left\{\right.$ the Yamabe corner of $\left.\mathbf{C P}^{2}\right\}=\left\{\left(12 \pi \sqrt{2}, 48 \pi^{2}\right)\right\}$.
Corollary B gives here that
$$\overline{\mathbf{K}^{\mathrm{W}}\left(\mathbf{C P}^{2}\right)} \cap\left\{\text { the Sobolev line of } \mathbf{C P}^{2}\right\}=\left\{y=12 \pi \sqrt{2}, w \geq 48 \pi^{2}\right\} .$$
In this case the gap curve does not give useful restrictions. However, it follows from [9, Theorem 2] that if a conformal class $C$ contains an Einstein metric different from $g_{F S}$, then $Y_{C}\left(\mathbf{C P}^{2}\right)<4 \pi \sqrt{6}$, see Fig 1.3.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/7154e6c7-f149-4bc9-a073-5210e0e5e33d-06.jpg?height=595&width=928&top_left_y=973&top_left_x=756}
\captionsetup{labelformat=empty}
\caption{Fig. 1.3. The YW -picture of $\mathbf{C P}^{2}$.}
\end{figure}
1.7. Results on 4-manifolds. Let $\chi(M)$ and $\tau(M)$ be as above.

Theorem C. Let $M$ be a minimal compact complex surface of general type, that is, its $\operatorname{Kodairadimension~} \operatorname{Kod}(M)=2$. Let $M^{\prime}=M \# k \overline{\mathbf{C P}^{2}} \# \ell\left(S^{1} \times S^{3}\right)(k, \ell \geq 0)$ be the connected sum of the blow-up of $M$ at $k$ points with $\ell$ copies of $S^{1} \times S^{3}$. Then
$$\omega\left(M^{\prime}\right)=\frac{16}{3} \pi^{2}\left(4 \chi\left(M^{\prime}\right)-3 \tau\left(M^{\prime}\right)+2 k+8 \ell\right), \quad \text { in particular, }$$
$\overline{\mathbf{K}^{\mathrm{W}}\left(M^{\prime}\right)} \cap\left\{\right.$ the Sobolev line of $\left.M^{\prime}\right\}=\left\{y=Y\left(M^{\prime}\right), w \geq \frac{16}{3} \pi^{2}\left(4 \chi\left(M^{\prime}\right)-3 \tau\left(M^{\prime}\right)+2 k+8 \ell\right)\right\}$.
In this case the Yamabe invariant $Y\left(M^{\prime}\right)$ is known (see LeBrun [17], [20] and Petean [22]):
$$Y\left(M^{\prime}\right)=-4 \sqrt{2} \pi \sqrt{2 \chi(M)+3 \tau(M)}<0 .$$
We have the following YW-picture for such $M$ :

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/7154e6c7-f149-4bc9-a073-5210e0e5e33d-07.jpg?height=559&width=980&top_left_y=247&top_left_x=781}
\captionsetup{labelformat=empty}
\caption{Fig. 1.4. The YW -picture of a minimal compact complex surface $M$ of general type.}
\end{figure}
In Fig. 1.4, we assume that $M$ has a negative first Chern class. We emphasize that in general, it is not clear whether $\omega(M)=W(M)$ or $\omega(M)>W(M)$ for every minimal compact complex surface of general type.

Theorem D. Let $M$ be a minimal compact Kähler-type complex surface of $\operatorname{Kod}(M)=0$ or $\operatorname{Kod}(M)=1$. Let $M^{\prime}=M \# k \overline{\mathbf{C P}^{2}} \# \ell\left(S^{1} \times S^{3}\right)(k, \ell \geq 0)$. Then
$$\begin{gathered}
\omega\left(M^{\prime}\right)=W\left(M^{\prime}\right)=-48 \pi^{2} \tau\left(M^{\prime}\right)=48 \pi^{2}(k-\tau(M)), \quad \text { in particular }, \\
\overline{\mathbf{K}^{\mathrm{W}}\left(M^{\prime}\right)} \cap\left\{\text { the Sobolev line of } M^{\prime}\right\}=\left\{y=Y\left(M^{\prime}\right), w \geq-48 \pi^{2} \tau\left(M^{\prime}\right)\right\} .
\end{gathered}$$
In this case it is also known that $Y\left(M^{\prime}\right)=0$ (see LeBrun [20] and Petean [22]).
Remark 1.2. (1) Under the assumptions of Theorem C or D, the intersection
$$\mathbf{K}^{\mathrm{W}}(M) \cap\{\text { the Sobolev line of } M\}=\{\text { one point }\} \text { or } \emptyset,$$
see [4, Proposition 5.89] or [13, Theorem 1].
(2) Theorems C and D still hold for more general 4-manifolds $M^{\prime}$, see [10, Theorems A, B and C].
T.8. More examples. Here we give examples illustrating Theorems C and D.

Example 3. Let $M$ be a $K 3$-surface. Then $M$ is a minimal Kähler surface of $\operatorname{Kod}(M)=0$. Here $\tau(M)=-16$, and Theorem D gives that $W(M)=\omega(M)=768 \pi^{2}, Y(M)=0$. Here we know also that there is no conformal class $C \in \mathcal{C}(M)$ with $Y_{C}(M)=0$ and with $W_{C}(M)>\omega(M)=W(M)=768 \pi^{2}$. Thus we have:
$$\begin{gathered}
\mathbf{K}^{\mathrm{W}}(M) \cap\{\text { the Sobolev line }\}=\left\{\left(Y(M)=0, W(M)=768 \pi^{2}\right)\right\}=\{\text { the Yamabe corner }\}, \\
\overline{\mathbf{K}^{\mathrm{W}}(M)} \cap\{\text { the Sobolev line }\}=\left\{y=0, w \geq 768 \pi^{2}\right\} \quad \text { by Corollary B. }
\end{gathered}$$
In particular, we see that a conformal class $C \in \mathcal{C}(M)$ contains an Einstein metric if and only if $Y_{C}(M)=0$ and $W_{C}(M)=768 \pi^{2}$. We have the following YW-picture:

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/7154e6c7-f149-4bc9-a073-5210e0e5e33d-08.jpg?height=554&width=898&top_left_y=219&top_left_x=781}
\captionsetup{labelformat=empty}
\caption{Fig. 1.5. The YW-picture of the K3 surface.}
\end{figure}

Example 4. Let $M=T^{2} \times \Sigma_{g}$, where $\Sigma_{g}$ is a surface with genus $g \geq 2$. Then $M$ is a minimal Kähler surface of $\operatorname{Kod}(M)=1$. Here $\tau(M)=0$ and $\chi(M)=0$.
Theorem D gives that $\omega(M)=W(M)=0$. We notice that $Y(M)=0$, however, there is no conformal class $C \in \mathcal{C}(M)$ such that $Y(M)=Y_{C}(M)=0$ (see [20, Proposition 6]). Hence we have
$$\mathbf{K}^{\mathrm{W}}(M) \cap\{\text { the Sobolev line of } M\}=\emptyset,$$
$$\overline{\mathbf{K}^{\mathfrak{Y} \mathfrak{W}}(M)} \cap\{\text { the Sobolev line of } M\}=\{y=0, w \geq 0\} \quad \text { by Corollary B. }$$

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/7154e6c7-f149-4bc9-a073-5210e0e5e33d-08.jpg?height=543&width=1102&top_left_y=1380&top_left_x=776}
\captionsetup{labelformat=empty}
\caption{Fig. 1.6. The XW -picture of $M=T^{2} \times \Sigma_{g}, g \geq 2$.}
\end{figure}

Example 5. Let $M=\Sigma_{g_{1}} \times \Sigma_{g_{2}}$ where $g_{1}, g_{2} \geq 2$. Then $M$ is a minimal Kähler surface of $\operatorname{Kod}(M)=2$. We have $\chi(M)=4\left(g_{1}-1\right)\left(g_{2}-1\right), \tau(M)=0$. Here the Yamabe invariant is attained by the canonical product Kähler-Einstein metrics. Theorem C gives that $\omega(M)=$ $\frac{256}{3} \pi^{2}\left(g_{1}-1\right)\left(g_{2}-1\right)$. Also $Y(M)=-16 \pi \sqrt{\left(g_{1}-1\right)\left(g_{2}-1\right)}$. We have
$$\begin{gathered}
\mathbf{K}^{\mathrm{W}}(M) \cap\{\text { the Sobolev line of } M\}=\{(Y(M), \omega(M))\}=\{\text { the Yamabe corner of } M\}, \\
\overline{\mathbf{K}^{\mathrm{W}}(M)} \cap\{\text { the Sobolev line of } M\}=\{y \geq Y(M), w \geq \omega(M)\} \quad \text { by Corollary B. }
\end{gathered}$$
Here it is not clear whether $\omega\left(\Sigma_{g_{1}} \times \Sigma_{g_{2}}\right)>W\left(\Sigma_{g_{1}} \times \Sigma_{g_{2}}\right)$ or they are equal.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/7154e6c7-f149-4bc9-a073-5210e0e5e33d-09.jpg?height=561&width=1127&top_left_y=247&top_left_x=643}
\captionsetup{labelformat=empty}
\caption{Fig. 1.7. The WW-picture of $M=\Sigma_{g_{1}} \times \Sigma_{g_{2}}$ with $g_{1}, g_{2} \geq 2$.}
\end{figure}

Example 6. Let $M=\mathbf{C} H^{2} / \Gamma$ be a smooth compact quotient of the complex hyperbolic space. Then $M$ is a minimal compact Kähler surface of general type. Then $\chi(M)=3 \tau(M)>$ 0 by [16, Theorem 5].
Theorem D now gives: $\omega(M)=\frac{16}{3} \pi^{2} \cdot 9 \tau(M)=48 \pi^{2} \tau(M)=16 \pi^{2} \chi(M)$. Let $g_{B}$ be the canonical Kähler-Einstein metric on $M$ (i.e. the Bergmann metric). The Yamabe invariant $Y(M)=-12 \sqrt{2} \pi \sqrt{\tau(M)}$ is attained by the metric $g_{B}$. Since $g_{B}$ is a self-dual metric, we have $W(M)=48 \pi^{2} \tau(M)$ by Proposition 1.1. Hence $\omega(M)=W(M)=48 \pi^{2} \tau(M)=16 \pi^{2} \chi(M)$. Here we have
$$\mathbf{K}^{\mathbf{W}}(M) \cap\{\text { the Sobolev line of } M\}=\{(Y(M), \omega(M))\}=\{\text { the Yamabe corner of } M\},$$
$$\overline{\mathbf{K}^{\mathfrak{Y} \mathfrak{W}}(M)} \cap\{\text { the Sobolev line of } M\}=\{y \geq Y(M), w \geq \omega(M)\} \quad \text { by Corollary B. }$$

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/7154e6c7-f149-4bc9-a073-5210e0e5e33d-09.jpg?height=559&width=898&top_left_y=1507&top_left_x=742}
\captionsetup{labelformat=empty}
\caption{Fig. 1.8. The YW -picture of $M=\mathbf{C} H^{2} / \Gamma$.}
\end{figure}
1.9. The plan of the paper. Firstly we prove Theorems C, D assuming Theorem A in Section 2. Secondly we prove Theorem A for the particular manifold $M=S^{n}$ in Section 3. Thirdly we prove the general case of Theorem A in Section 4.
1.10. Acknowledgments. The first and the third authors are very grateful to the Department of Mathematics of the University of Oregon for hospitality. The authors are grateful to Claude LeBrun for his valuable comments concerning Theorem 1.3 and Theorems C, D.

\section*{2 Proofs of Theorems C and D}
2.1. Proof of Theorem C. Let $M$ be a minimal compact complex surface of general type, and $M^{\prime}=M \# k \overline{\mathbf{C P}^{2}} \# \ell\left(S^{1} \times S^{3}\right)$. Here we use the results by LeBrun [19, Theorem 7], [20, Theorem 2], [21, Proposition 3.2, Proof of Theorem 4.3] and Petean [22, Proposition 4] to conclude that there exists a sequence of metrics $\left\{g_{j}\right\}, g_{j} \in \mathcal{R} \operatorname{iem}\left(M^{\prime}\right)$ such that
$$\left\{\begin{array}{l}
\lim _{j \rightarrow \infty} \int_{M^{\prime}}\left|W_{g_{j}}^{+}\right|_{g_{j}}^{2} d \sigma_{g_{j}}=\frac{4}{3} \pi^{2}(2 \chi(M)+3 \tau(M))>0 \\
\lim _{j \rightarrow \infty} Y_{\left[g_{j}\right]}\left(M^{\prime}\right)=Y\left(M^{\prime}\right)=-4 \sqrt{2} \pi \sqrt{2 \chi(M)+3 \tau(M)}<0 \\
\lim _{j \rightarrow \infty} \int_{M^{\prime}} R_{g_{j}}^{2} d \sigma_{g_{j}}=Y\left(M^{\prime}\right)^{2}=32 \pi^{2}(2 \chi(M)+3 \tau(M))>0
\end{array}\right.$$
Here we use the following convention: $\left|W_{g}\right|_{g}^{2}=4\left(\left|W_{g}^{+}\right|_{g}^{2}+\left|W_{g}^{-}\right|_{g}^{2}\right)$. In particular, the sequence of conformal classes $\left\{\left[g_{j}\right]\right\}$ is a Yamabe sequence. Then the Hirzebruch signature formula gives:
$$\begin{aligned}
\lim _{j \rightarrow \infty} W_{\left[g_{j}\right]}\left(M^{\prime}\right) & =8 \lim _{j \rightarrow \infty} \int_{M^{\prime}}\left|W_{g_{j}}^{+}\right|_{g_{j}}^{2} d \sigma_{g_{j}}-48 \pi^{2} \tau\left(M^{\prime}\right) \\
& =\frac{16}{3} \pi^{2}\left(4 \chi\left(M^{\prime}\right)-3 \tau\left(M^{\prime}\right)+2 k+8 \ell\right)
\end{aligned}$$
Then, by definition, we have:
$$\omega\left(M^{\prime},\left\{\left[g_{j}\right]\right\}\right)=\lim _{j \rightarrow \infty} W_{\left[g_{j}\right]}\left(M^{\prime}\right)=\frac{16}{3} \pi^{2}\left(4 \chi\left(M^{\prime}\right)-3 \tau\left(M^{\prime}\right)+2 k+8 \ell\right) .$$
From the formula (2) below, we also notice that
$$\omega\left(M^{\prime}\right) \geq \frac{16}{3} \pi^{2}\left(4 \chi\left(M^{\prime}\right)-3 \tau\left(M^{\prime}\right)+2 k+8 \ell\right) .$$
These imply Theorem C. \(\square\)

Remark 2.1. Under the same assumptions on $M$ and $M^{\prime}$ as in Theorem C, we notice the following.
\begin{itemize}
\item[(1)] There is a sharp inequality
$$\left|Y_{C}\left(M^{\prime}\right)\right|+\sqrt{6}\left(\int_{M^{\prime}}\left|W_{g}^{+}\right|_{g}^{2} d \sigma_{g}\right)^{\frac{1}{2}} \geq 6 \sqrt{2} \pi \sqrt{2 \chi(M)+3 \chi \tau(M)}>0$$
for any $C \in \mathcal{C}\left(M^{\prime}\right)$ and $g \in C$ (see [21, Formula (13)]). When either $k \geq 1$ or $\ell \geq 1$, the inequality (2) provides a further restriction on the YW-picture of $M^{\prime}$.
\item[(2)] Furthemore,
$$\begin{aligned}
& \text { \{the Sobolev line of } \left.M^{\prime}\right\} \cap\left\{\text { the Einstein curve of } M^{\prime}\right\} \\
& \qquad=\left\{\left(Y\left(M^{\prime}\right), \frac{16}{3} \pi^{2}\left(4 \chi\left(M^{\prime}\right)-3 \tau\left(M^{\prime}\right)-k-4 \ell\right)\right)\right\} .
\end{aligned}$$
Then if either $k \geq 1$ or $\ell \geq 1$, the above $w$-coordinate is strictly less than $\omega\left(M^{\prime}\right)$.
\end{itemize}
2.2. Proof of Theorem D. Let $M$ be a minimal compact Kähler-type complex surface of $\operatorname{Kodairadimension~} \operatorname{Kod}(M)=0$ or 1. Let $M^{\prime}=M \# k \overline{\mathbf{C P}^{2}} \# \ell\left(S^{1} \times S^{3}\right)$. Again we use the results due to LeBrun [19, Theorem 7], [20, Theorems 4 and 6], [21, Proposition 3.2 and Proof of Theorem 4.3] and Petean [22, Proposition 3] to conclude that there exists a sequence of metrics $\left\{g_{j}\right\}, g_{j} \in \mathcal{R} \operatorname{iem}\left(M^{\prime}\right)$ such that
$$\left\{\begin{array}{l}
\lim _{j \rightarrow \infty} \int_{M^{\prime}}\left|W_{g_{j}}^{+}\right|_{g_{j}}^{2} d \sigma_{g_{j}}=\frac{4}{3} \pi^{2}(2 \chi(M)+3 \tau(M)) \\
\lim _{j \rightarrow \infty} Y_{\left[g_{j}\right]}\left(M^{\prime}\right)=Y\left(M^{\prime}\right)=0 \\
\lim _{j \rightarrow \infty} \int_{M^{\prime}} R_{g_{j}}^{2} d \sigma_{g_{j}}=Y\left(M^{\prime}\right)^{2}=0
\end{array}\right.$$
Thus the sequence of conformal classes $\left\{\left[g_{j}\right]\right\}$ is a Yamabe sequence. Then the Hirzebruch signature formula gives:
$$\begin{aligned}
\lim _{j \rightarrow \infty} W_{\left[g_{j}\right]}\left(M^{\prime}\right) & =8 \lim _{j \rightarrow \infty} \int_{M^{\prime}}\left|W_{g_{j}}^{+}\right|_{g_{j}}^{2} d \sigma_{g_{j}}-48 \pi^{2} \tau\left(M^{\prime}\right) \\
& =\frac{16}{3} \pi^{2}(4 \chi(M)-3 \tau(M)+9 k)
\end{aligned}$$
We obtain:
$$\omega\left(M^{\prime},\left\{\left[g_{j}\right]\right\}\right)=\lim _{j \rightarrow \infty} W_{\left[g_{j}\right]}\left(M^{\prime}\right)=\frac{16}{3} \pi^{2}(4 \chi(M)-3 \tau(M)+9 k) .$$
It also follows from [20, Theorem 4 and Proposition 7] that $2 \chi(M)=-3 \tau(M) \geq 0$ and $\omega\left(M^{\prime}\right)=W\left(M^{\prime}\right)=48 \pi^{2}(k-\tau(M))=-48 \pi^{2} \tau\left(M^{\prime}\right)$. These imply Theorem D. \(\square\)

\section*{3 The sphere}
3.1. The result. Our goal here is to prove Theorem A for $M=S^{n}$, that is, the following result.

Theorem 3.1. For any small $\varepsilon>0$ and arbitrary $\kappa>0$ there exists a conformal class $C \in \mathcal{C}\left(S^{n}\right)$ such that
$$\left\{\begin{array}{l}
Y_{C}\left(S^{n}\right) \geq Y\left(S^{n}\right)-\varepsilon \\
\kappa+\varepsilon \geq W_{C}\left(S^{n}\right) \geq \kappa
\end{array}\right.$$
To give a proof of Theorem 3.1 we will construct a required conformal class $C \in \mathcal{C}\left(S^{n}\right)$ using the manifold $S^{n-1} \times \mathbf{R}$. The following definition is due to Schoen and Yau [25].
Definition 3.1. Let $(N, C)$ be a conformal manifold of $\operatorname{dim} N=n \geq 3$ (possibly noncompact) and $g \in C$ any metric. We denote
$$\begin{aligned}
E_{g}(f) & =\int_{N}\left(\alpha_{n}|d f|_{g}^{2}+R_{g} f^{2}\right) d \sigma_{g} \\
Q_{g}(f) & =\frac{E_{g}(f)}{\left(\int_{N}|f|^{\frac{2 n}{n-2}} d \sigma_{g}\right)^{\frac{n-2}{n}}}
\end{aligned}$$
where $\alpha_{n}=\frac{4(n-1)}{n-2}$. Then the Yamabe constant $Y_{C}(N)$ is defined as
$$Y_{C}(N)=\inf _{\substack{f \in C_{\mathrm{cpt}}^{\infty}(N) \\ f \neq 0}} Q_{g}(f) .$$
The Yamabe constant $Y_{C}(N)$ does not depend on the choice of the metric $g \in C$ (see [25]).
3.2. Continuity of the Yamabe constant. First we recall the following result on the continuity of the Yamabe constant, see [5], [13, Fact 1.4] (cf. [2, Lemma 4.1]).
Fact 3.1. Let $M$ be a compact manifold of $\operatorname{dim} M=n \geq 3$ and $g \in \operatorname{Riem}(M)$. Let $\left\{g_{i}\right\}$ be a sequence of Riemannian metrics such that
$$\left\{\begin{array}{l}
g_{i} \rightarrow g, \\
R_{g_{i}} \rightarrow R_{g}
\end{array} \quad \text { as } \quad i \rightarrow \infty\right.$$
in the uniform $C^{0}$-norm on $M$ with respect to $g$. Then $Y_{\left[g_{i}\right]}(M) \rightarrow Y_{[g]}(M)$ as $i \rightarrow \infty$.
In the course of proving Proposition 3.1 one has to show that $\liminf _{i \rightarrow \infty} Y_{\left[g_{i}\right]}(M) \geq Y_{[g]}(M)$. Here it is essential that the volume $\operatorname{Vol}_{g}(M)$ is finite. However, a similar continuity result still holds for noncompact manifolds under the positivity of scalar curvature.
Proposition 3.2. Let $N$ be a manifold without boundary (possibly noncompact). Assume that a metric $g \in \mathcal{R} \operatorname{iem}(N)$ satisfies the following condition
$$0<L_{0}^{-1} \leq R_{g} \leq L_{0} \text { on } N$$
for some constant $L_{0}>0$. Let $\left\{g_{i}\right\}$ be a sequence of Riemannian metrics, such that
$$\left\{\begin{array}{l}
g_{i} \rightarrow g, \\
R_{g_{i}} \rightarrow R_{g}
\end{array} \quad \text { as } \quad i \rightarrow \infty\right.$$
in the uniform $C^{0}$-norm on $N$ with respect to $g$. Then $Y_{\left[g_{i}\right]}(N) \rightarrow Y_{[g]}(N)$ as $i \rightarrow \infty$.
Proof. Given $\varepsilon>0$, there exists an integer $i(\varepsilon)>0$ such that
$$\begin{aligned}
\left|g_{i}-g\right|_{g} \leq \varepsilon, & \left|g_{i}^{-1}-g^{-1}\right|_{g} \leq \varepsilon \quad(\text { with respect to } g), \\
(1-\varepsilon) d \sigma_{g} & \leq d \sigma_{g_{i}} \leq(1+\varepsilon) d \sigma_{g}, \\
0<(1-\varepsilon) R_{g} & \leq R_{g_{i}} \leq(1+\varepsilon) R_{g}
\end{aligned}$$
for any $i \geq i(\varepsilon)$. Note that the last inequality follows from the condition (3). For any compactly supported smooth function $f \in C_{\text {cpt }}^{\infty}(N)$, we have
$$\begin{aligned}
E_{g_{i}}(f) & =\int_{N}\left(\alpha_{n}|d f|_{g_{i}}^{2}+R_{g_{i}} f^{2}\right) d \sigma_{g_{i}} \\
& \geq \int_{N}\left(\alpha_{n}(1-\varepsilon)|d f|_{g}^{2}+(1-\varepsilon) R_{g} f^{2}\right)(1-\varepsilon) d \sigma_{g} \\
& \geq(1-2 K \varepsilon) \int_{N}\left(\alpha_{n}|d f|_{g}^{2}+R_{g} f^{2}\right) d \sigma_{g} \\
& \geq(1-2 K \varepsilon) E_{g}(f)
\end{aligned}$$
for any $i \geq i(\varepsilon)$. Similarly we have
$$\begin{gathered}
E_{g_{i}}(f) \leq(1+2 K \varepsilon) E_{g}(f) \text { and } \\
\left(1-K^{\prime} \varepsilon\right)\left(\int_{N}|f|^{\frac{2 n}{n-2}} d \sigma_{g}\right)^{\frac{n-2}{n}} \leq\left(\int_{N}|f|^{\frac{2 n}{n-2}} d \sigma_{g_{i}}\right)^{\frac{n-2}{n}} \leq\left(1+K^{\prime} \varepsilon\right)\left(\int_{N}|f|^{\frac{2 n}{n-2}} d \sigma_{g}\right)^{\frac{n-2}{n}} .
\end{gathered}$$
Here $K, K^{\prime}$ are positive constants independent of $f$ and $\varepsilon$. Hence we have
$$\begin{aligned}
\frac{(1-2 K \varepsilon)}{\left(1+K^{\prime} \varepsilon\right)} Q_{g}(f) & \leq Q_{g_{i}}(f) \leq \frac{(1+2 K \varepsilon)}{\left(1-K^{\prime} \varepsilon\right)} Q_{g}(f) \text {, or } \\
\left(1-K^{\prime \prime} \varepsilon\right) Q_{g}(f) & \leq Q_{g_{i}}(f) \leq\left(1+K^{\prime \prime} \varepsilon\right) Q_{g}(f), \text { or } \\
\left(1-K^{\prime \prime} \varepsilon\right) Y_{[g]}(N) & \leq Y_{\left[g_{i}\right]}(N) \leq\left(1+K^{\prime \prime} \varepsilon\right) Y_{[g]}(N)
\end{aligned}$$
for some positive constant $K^{\prime \prime}$. This implies that $Y_{\left[g_{i}\right]}(N) \longrightarrow Y_{[g]}(N)$. \(\square\)

We recall the following well-known facts (cf. [13], [24]).
Fact 3.2. Let $g_{0}$ and $h_{0}$ denote the standard metrics on the spheres $S^{n}$ and $S^{n-1}$ respectively. Let $C_{0}=\left[g_{0}\right]$. Then
$$Y\left(S^{n}\right)=Y_{C_{0}}\left(S^{n}\right)=Y_{C_{0}}\left(S^{n} \backslash\{2 \text { points }\}\right)=Y_{\left[h_{0}+d t^{2}\right]}\left(S^{n-1} \times \mathbf{R}\right) .$$

Fact 3.3. Let $M$ be a compact manifold, $p_{1}, \ldots, p_{k} \in M$, and $C \in \mathcal{C}(M)$ a conformal class which is conformaly flat near the points $p_{1}, \ldots, p_{k}$. Then
$$Y_{C}(M)=Y_{C}\left(M \backslash\left\{p_{1}, \ldots, p_{k}\right\}\right) .$$
Let $g_{0}$ and $h_{0}$, as above, denote the standard metrics on the spheres $S^{n}$ and $S^{n-1}$ respectively. As a corollary of Proposition 3.2 we have the following result.

Corollary 3.3. Let $h(\cdot, t)$ be a smooth (with respect to $t$ ) family of Riemannian metrics on $S^{n-1}$, and let $\bar{g}(z, t)=h(z, t)+d t^{2},(z, t) \in S^{n-1} \times \mathbf{R}$, be the corresponding metric on the cylinder $S^{n-1} \times \mathbf{R}$. Then for any $\varepsilon>0$ there exists $\delta>0$ such that if the family $h(\cdot, t)$ satisfies the condition
$$\begin{cases}\left|h(\cdot, t)-h_{0}\right| h_{0}<\delta & \text { on } S^{n-1} \text { for any } t \in \mathbf{R}, \text { and } \\ \left|R_{\bar{g}(\cdot, t)}-R_{\bar{g}_{0}}\right|<\delta & \text { on } S^{n-1} \times \mathbf{R},\end{cases}$$
then $Y_{[\bar{g}]}\left(S^{n-1} \times \mathbf{R}\right) \geq Y_{\left[\bar{g}_{0}\right]}\left(S^{n-1} \times \mathbf{R}\right)-\varepsilon=Y\left(S^{n}\right)-\varepsilon$. Here $\bar{g}_{0}:=h_{0}+d t^{2}$ on $S^{n-1} \times \mathbf{R}$.
3.3. Metrics on the cylinder $N=M \times \mathbf{R}$. We consider the following general situation. Let $M$ be a compact manifold, and $N=M \times \mathbf{R}$.
First, let $g(\cdot, t) \in \mathcal{R}$ iem $(M)$ be a smooth family of metrics and $\bar{g}(z, t)=g(z, t)+d t^{2}$ the corresponding metric on $N=M \times \mathbf{R}$. First, we compare the scalar curvature functions $R_{g}$ and $R_{\bar{g}}$, where $g:=g(\cdot, t)$. We have:
$$\begin{aligned}
R_{\bar{g}} & =R_{g}+\frac{1}{4}\left(g^{i j} g^{k l} \cdot \partial_{t} g_{i j} \cdot \partial_{t} g_{k l}-\left(g^{i j} \cdot \partial_{t} g_{i j}\right)^{2}\right)-\frac{1}{2}\left(g^{i j} \cdot \partial_{t}^{2} g_{i j}+\partial_{t}\left(g^{i j} \cdot \partial_{t} g_{i j}\right)\right) \\
& =R_{g}-g^{i j} \cdot \partial_{t}^{2} g_{i j}-\frac{1}{4}\left(g^{i j} \cdot \partial_{t} g_{i j}\right)^{2}+\frac{3}{4} g^{i j} g^{k l} \cdot \partial_{t} g_{i j} \cdot \partial_{t} g_{k l}
\end{aligned}$$

Here the indices $i, j, k, \ell$ vary within the corresponding indices $1, \ldots, n-1$ of local coordinates $z=\left\{z^{1}, \ldots, z^{n-1}\right\}$ on $M$. Now we consider a particular family of metrics. Let $L>0$ be a sufficiently large constant. We choose a nonnegative function $\varphi=\varphi_{L} \in C^{\infty}(\mathbf{R})$ satisfying
$$\left|\varphi^{\prime}\right| \leq \frac{2}{L}, \quad\left|\varphi^{\prime \prime}\right| \leq \frac{4}{L^{2}}, \quad \varphi= \begin{cases}0, & \text { if } t \leq 0, \\ 1, & \text { if } t \geq L, \quad \text { (see Fig. 3.1.) }\end{cases}$$

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/7154e6c7-f149-4bc9-a073-5210e0e5e33d-14.jpg?height=276&width=1041&top_left_y=525&top_left_x=643}
\captionsetup{labelformat=empty}
\caption{Fig. 3.1. The function $\varphi=\varphi_{L}$.}
\end{figure}
Let $h, \hat{h} \in \mathcal{R} \operatorname{iem}(M)$ be two metrics on the "slice" $M$. We define the family of metrics on $M \times\{t\} \cong M$ :
$$\begin{aligned}
g(z, t) & :=\varphi(t) \cdot h(z)+(1-\varphi(t)) \cdot \hat{h}(z) \\
& =h(z)-(1-\varphi(t)) \cdot T(z)
\end{aligned}$$
where $T(z):=h(z)-\hat{h}(z)$. Let $\bar{g}(z, t):=g(z, t)+d t^{2}$ be the metric on the cylinder $M \times \mathbf{R}$. We notice that
$$\left\{\begin{aligned}
g^{\prime} & =\varphi^{\prime} \cdot T, \\
g^{\prime \prime} & =\varphi^{\prime \prime} \cdot T
\end{aligned} \quad \text { and } \quad \bar{g}= \begin{cases}\hat{h}+d t^{2} & \text { if } t \leq 0, \\
h+d t^{2} & \text { if } t \geq L .\end{cases}\right.$$
Assume that $|T|_{h} \ll 1$, so that $\frac{1}{2}\left(h_{i j}\right) \leq\left(g_{i j}\right) \leq 2\left(h_{i j}\right)$. Then we use (4) to give the estimate
$$\left|R_{\bar{g}}-R_{g}\right| \leq \frac{8}{L^{2}}|T|_{h}+\frac{4}{L^{2}}|T|_{h}^{2}+\frac{12}{L^{2}}|T|_{h}^{2} \leq \frac{K_{0}}{L^{2}}|T|_{h}$$
since $|T|_{h} \ll 1$. We denote $\theta(z, t):=-(1-\varphi(t)) T(z)$, so that $g(z, t)=h(z)+\theta(z, t)$ on $M \times\{t\} \cong M$. We also denote
$$P_{h}(\theta):=-\nabla^{j} \nabla_{i} \theta_{i}^{i}+\nabla^{i} \nabla^{j} \theta_{i j}-R_{i j} \theta^{i j},$$
where $\left(R_{i j}\right)$ is the Ricci curvature of $h$. A straightforward calculation gives the following formula for the scalar curvature (cf. [13], [14]):
$$R_{g}=R_{h}+P_{h}(\theta)+Q_{h}(\theta),$$
where the function $Q_{h}(\theta)$ is estimated by
$$\begin{gathered}
\left|Q_{h}(\theta)\right|_{h} \leq K_{n}\left\{|\nabla \theta|_{h}^{2} \cdot q^{3}+|\theta|_{h} \cdot\left|\nabla^{2} \theta\right|_{h} \cdot q^{2}+\left(|\theta|_{h} \cdot\left|\nabla^{2} \theta\right|_{h}+|\operatorname{Ric}(h)|_{h} \cdot|\theta|_{h}^{2}\right) q\right\} \quad \text { with } \\
q(z, t):=\max \left\{\left.\frac{h(X, X)}{g(X, X)} \right\rvert\, X \in T_{(z, t)} M, X \not \equiv 0\right\} .
\end{gathered}$$
Here $\nabla$, Ric $=\left(R_{i j}\right)$ and all norms are with respect to the metric $h$. Now we also assume that $|\nabla T|_{h}$ and $\left|\nabla^{2} T\right|_{h}$ are sufficiently small. Then the estimates (5) and (6) imply that
$$\left|R_{g}-R_{h}\right| \leq \Phi(h, T),$$
where the constant $\Phi(h, T) \geq 0$ (depending on $h$ and $T$ ) is small as well. We obtain
$$\left|R_{\bar{g}}-R_{h}\right| \leq \frac{K_{0}}{L^{2}}|T|_{h}+\Phi(h, T) .$$
In particular, the above argument implies the following technical result.
Lemma 3.4. Let $h_{0} \in \operatorname{Riem}\left(S^{n-1}\right)$ be the standard metric of constant curvature 1. Then for any integer $j>0$ there exist a constant $L(j) \gg 1$ and a metric $h_{j} \in \mathcal{R} \operatorname{iem}\left(S^{n-1}\right)$ such that
$$\left\{\begin{array}{l}
\left|\bar{g}_{0}-\bar{g}_{j}\right| \bar{g}_{0} \leq \frac{1}{j}, \\
\left|R_{\bar{g}_{0}}-R_{\bar{g}_{j}}\right| \leq \frac{1}{j}
\end{array} \quad \text { on } \quad S^{n-1} \times \mathbf{R} .\right.$$
Here the metrics $\bar{g}_{0}$ and $\bar{g}_{j}$ on $S^{n-1} \times \mathbf{R}$ are defined as
$$\begin{aligned}
& \bar{g}_{0}(z, t):=h_{0}(z)+d t^{2} \\
& \bar{g}_{j}(z, t):=\left(h_{0}(z)-(1-\varphi(t)) \cdot\left(h_{0}(z)-h_{j}(z)\right)\right)+d t^{2}
\end{aligned}$$
where $\varphi(t):=\varphi_{L}(t)$ for any $L \geq L(j)$.
Proof of Theorem 3.1. Let $h_{0}$ be the standard metric on $S^{n-1}$. We use Lemma 3.4 to conclude the following.
For any $\varepsilon>0$ there exist a constant $L \gg 1$ and a metric $h \in \mathcal{R i e m}\left(S^{n-1}\right)$ (where $h$ is not homothetic but $C^{2}$-close to $h_{0}$ ) such that the metric
$$\begin{aligned}
\bar{g}(z, t) & :=g(z, t)+d t^{2} \text { on } S^{n-1} \times \mathbf{R} \text { with } \\
g(z, t) & := \begin{cases}h(z) & \text { on } S^{n-1} \times[-\bar{L}, \bar{L}] \\
h_{0}(z)-\left(1-\varphi_{L}(t-\bar{L})\right) \cdot\left(h_{0}(z)-h(z)\right) & \text { on } S^{n-1} \times[\bar{L}, \bar{L}+L] \\
h_{0}(z)-\left(1-\varphi_{L}(-t-\bar{L})\right) \cdot\left(h_{0}(z)-h(z)\right) & \text { on } S^{n-1} \times[-(\bar{L}+L),-\bar{L}] \\
h_{0}(z) & \text { on } S^{n-1} \times(\mathbf{R} \backslash[-(\bar{L}+L), \bar{L}+L])\end{cases}
\end{aligned}$$
satisfies the inequalities
$$\left\{\begin{aligned}
Y_{[\bar{g}]}\left(S^{n-1} \times \mathbf{R}\right) & \geq Y\left(S^{n}\right)-\varepsilon, \\
\int_{S^{n-1} \times([-(\bar{L}+L),-\bar{L}] \cup[\bar{L}, \bar{L}+L])}\left|W_{\bar{g}}\right| \frac{n}{\bar{g}} d \sigma_{\bar{g}} & \leq \varepsilon
\end{aligned}\right.$$
for any $\bar{L}>0$ (see Fig. 3.2).

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/7154e6c7-f149-4bc9-a073-5210e0e5e33d-15.jpg?height=290&width=1106&top_left_y=2127&top_left_x=543}
\captionsetup{labelformat=empty}
\caption{Fig. 3.2. The metric $\bar{g}$ on $S^{n-1} \times \mathbf{R}$.}
\end{figure}

Notice that the restriction of the metric $\bar{g}(z, t)$ on $S^{n-1} \times[-\bar{L}, \bar{L}]$ is given as $\bar{g}(z, t)=$ $h(z)+d t^{2}$. Consider the function
$$f(\bar{L}):=\int_{S^{n-1} \times[-\bar{L}, \bar{L}]}\left|W_{\bar{g}}\right|_{\bar{g}}^{\frac{n}{2}} d \sigma_{\bar{g}} \in(0, \infty)$$
Then $f$ is continuous on $(0, \infty)$, and
$$\lim _{\bar{L} \rightarrow 0} f(\bar{L})=0, \quad \lim _{\bar{L} \rightarrow \infty} f(\bar{L})=\infty .$$
By definition of $f$, we have:
$$\int_{S^{n-1} \times \mathbf{R}}\left|W_{\bar{g}}\right|_{\bar{g}}^{\frac{n}{2}} d \sigma_{\bar{g}}=f(\bar{L})+\int_{S^{n-1} \times([-(\bar{L}+L),-\bar{L}] \cup[\bar{L}, \bar{L}+L])}\left|W_{\bar{g}}\right|_{\bar{g}}^{\frac{n}{2}} d \sigma_{\bar{g}} .$$
It follows from (7), (8) and (9) that for any $0<\varepsilon \ll 1$ and any constant $\kappa>0$ there exist constants $L>0$ and $\bar{L}>0$ such that
$$\left\{\begin{array}{l}
\bar{g}(z, t)=g(z, t)+d t^{2} \text { on } S^{n-1} \times \mathbf{R}(\text { as above }), \\
Y_{[\bar{g}]}\left(S^{n-1} \times \mathbf{R}\right) \geq Y\left(S^{n}\right)-\varepsilon, \\
\kappa+\varepsilon \geq W_{[\bar{g}]}\left(S^{n-1} \times \mathbf{R}\right) \geq \kappa,
\end{array}\right.$$
where $\bar{g}(z, t)=h_{0}(z)+d t^{2}$ on $S^{n-1} \times(\mathbf{R} \backslash[-(\bar{L}+L), \bar{L}+L])$. Thus the conformal class $[\bar{g}]$ can be extended smoothly to a conformal class $C \in \mathcal{C}\left(S^{n}\right)$ such that
$$\left\{\begin{aligned}
Y_{[\bar{g}]}\left(S^{n-1} \times \mathbf{R}\right) & =Y_{C}\left(S^{n}\right), \\
W_{[\bar{g}]}\left(S^{n-1} \times \mathbf{R}\right) & =W_{C}\left(S^{n}\right) .
\end{aligned}\right.$$
Combining (10) with (11), we complete the proof of Theorem 3.1. \(\square\)

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/7154e6c7-f149-4bc9-a073-5210e0e5e33d-16.jpg?height=285&width=572&top_left_y=1652&top_left_x=735}
\captionsetup{labelformat=empty}
\caption{Fig. 3.3. The sphere ( $S^{n}, \hat{g}$ ).}
\end{figure}

Remark 3.1. In the proof of Theorem 3.1, we let $\bar{L}$ go to the infinity. Then (in the terminology of [3]) we obtain the canonical cylindrical manifold
$$\left(S^{n-1} \times \mathbf{R}, \bar{g}:=h+d t^{2}\right),$$
where $h$ is not homothetic but $C^{2}$-close to $h_{0}$. Proposition 3.2 implies that the inequality $Y_{[\bar{g}]}\left(S^{n-1} \times \mathbf{R}\right) \geq Y\left(S^{n}\right)-\varepsilon$ still holds for a small $\varepsilon>0$. However, $W_{[\bar{g}]}\left(S^{n-1} \times \mathbf{R}\right)=+\infty$. From [3, Theorems 6.1, 6.2] there exists a function $u \in C_{+}^{\infty}\left(S^{n-1} \times \mathbf{R}\right) \cap L_{\bar{g}}^{1,2}\left(S^{n-1} \times \mathbf{R}\right)$ such
that the metric $\hat{g}=u^{\frac{4}{n-2}} \bar{g}$ is a Yamabe metric (i.e. a minimizer of the functional $Q_{\bar{g}}$, see [3] for details). Furthermore, the metric $\hat{g}$ is almost conical metric near the two ends.

Then, by adding two points $p_{-}, p_{+}$to the ends, we obtain the sphere
$$S^{n}=\left(S^{n-1} \times \mathbf{R}\right) \cup\left\{p_{-}, p_{+}\right\}$$
with the metric $\hat{g}$ (see Fig. 3.3).
Thus $\left(S^{n}, \hat{g}\right)$ is a compact Riemannian manifold with two almost conical singularities. These singularities provide the source of the phenomenon that
$$W_{[\hat{g}]}\left(S^{n}\right)=W_{[\bar{g}]}\left(S^{n-1} \times \mathbf{R}\right)=+\infty .$$

\section*{4 Proof of Theorem A}

We start with the following approximation result in [13] and [14] (see also [2]).
Proposition 4.1. Let $M$ be a compact manifold of $\operatorname{dim} M=n \geq 3$ and $o \in M$ a point. Given any conformal class $C \in \mathcal{C}(M)$ and small $\varepsilon>0$ there exists a conformal class $\tilde{C} \in \mathcal{C}(M)$ such that
$$\left\{\begin{array}{l}
\left|Y_{\tilde{C}}(M)-Y_{C}(M)\right| \leq \varepsilon, \\
\left|W_{\tilde{C}}(M)-W_{C}(M)\right| \leq \varepsilon,
\end{array}\right.$$
and $\tilde{C}$ is conformally flat near the point $o \in M$.
Proof. Let $g \in C$ be any metric. Then following the construction in [13, Section 3], we define a smooth family of approximation metrics. For a given $o \in M$, there exists a metric $\bar{g} \in \mathcal{R} i \operatorname{em}(M)$, which is conformally flat near the point $o$, such that
$$\left\{\begin{array}{l}
j_{o}^{1}(\bar{g})=j_{o}^{1}(g) \\
R_{\bar{g}}(o)=R_{g}(o)
\end{array}\right.$$
For a small $\delta>0$, there exist a positive constant $0<\varepsilon(\delta)(0<\varepsilon(\delta)<\delta)$ and a smooth cut-off function $w_{\delta}=w_{\delta}(r)(r \geq 0)$ satisfying
$$0 \leq w_{\delta} \leq 1, \quad w_{\delta}=\left\{\begin{array} { l l } 
{ 0 } & { \text { if } r \geq \delta , } \\
{ 1 } & { \text { if } 0 \leq r \leq \varepsilon ( \delta ) , }
\end{array} \quad \text { and } \quad \left\{\begin{array}{l}
\left|r \cdot \dot{w}_{\delta}\right|<\delta, \\
\left|r^{2} \cdot \ddot{w}_{\delta}\right|<\delta .
\end{array}\right.\right.$$
Then let $g_{\delta}:=g+w_{\delta}(\bar{g}-g)$. Then we have that
$$\begin{cases}g_{\delta} \rightarrow g & \text { in the } C^{1} \text {-norm on } M \text { with respect to } g, \\ R_{g_{\delta}} \rightarrow R_{g} & \text { in the } C^{0} \text {-norm on } M\end{cases}$$
as $\delta \rightarrow 0$. This implies that $Y_{\left[g_{\delta}\right]}(M) \rightarrow Y_{[g]}(M)$ as $\delta \rightarrow 0$.
To analyze the behaviour of the Weyl constant, we denote by $B_{\delta}$ the disk (with respect to $g$ ) centered at $o \in M$ of radius $\delta$. Also we denote $h=\bar{g}-g$ and $T=w_{\delta} \cdot h=O\left(r^{2}\right)$. Then
$$\left(W_{g_{\delta}}\right)^{i}{ }_{j k \ell}-\left(W_{g}\right)^{i}{ }_{j k \ell}=O\left(\left|\nabla^{2} T\right|_{g}\right)+O\left(\left(1+|T|_{g}^{2}\right)|\nabla T|_{g}^{2}\right) .$$

Here
$$\left\{\begin{aligned}
\nabla T & =\dot{w}_{\delta} \cdot h+w_{\delta} \cdot \nabla h, \\
\nabla^{2} T & =\ddot{w}_{\delta} \cdot h+2 \dot{w}_{\delta} \cdot \nabla h+w_{\delta} \cdot \nabla^{2} h .
\end{aligned}\right.$$
Notice that $\nabla h=O(r), \nabla^{2} h=O(1)$, and then
$$\left\{\begin{aligned}
|T|_{g}^{2} & \leq K_{1} \cdot \delta^{4} \\
|\nabla T|_{g}^{2} & \leq K_{2} \cdot \delta^{2} \\
\left|\nabla^{2} T\right|_{g} & \leq K_{3} \cdot \delta+K_{4}
\end{aligned}\right.$$
for some positive constants $K_{1}, K_{2}, K_{3}, K_{4}$. From (12) and (13), we obtain
$$\left|W_{g_{\delta}}\right|_{g} \leq\left|W_{g}\right|_{g}+K_{5}$$
for some $K_{5}>0$ on the disk $B_{\delta}$, and hence there exists a constant $K_{6}>0$ such that
$$\left|W_{g_{\delta}}\right|_{g}^{\frac{n}{2}} \leq K_{6}\left(\left|W_{g}\right|_{g}^{\frac{n}{2}}+1\right) .$$
This implies that
$$\begin{aligned}
\left|W_{\left[g_{\delta}\right]}(M)-W_{[g]}(M)\right| & \left.=\left.\left|\int_{B_{\delta}}\right| W_{g_{\delta}}\right|_{g_{\delta}} ^{\frac{n}{2}} d \sigma_{g_{\delta}}-\int_{B_{\delta}}\left|W_{g}\right|_{g}^{\frac{n}{2}} d \sigma_{g} \right\rvert\, \\
& \leq 2 K_{6} \cdot \int_{B_{\delta}}\left(\left|W_{g}\right|_{g}^{\frac{n}{2}}+1\right) d \sigma_{g}
\end{aligned}$$
since $d \sigma_{g_{\delta}} \leq 2 d \sigma_{g}$. We obtain that $W_{\left[g_{\delta}\right]}(M) \rightarrow W_{[g]}(M)$ as $\delta \rightarrow 0$. \(\square\)

Proof of Theorem A. First we choose small $\varepsilon>0$. Then by definition there exists a conformal class $C \in \mathcal{C}(M)$ such that
$$\left\{\begin{array}{l}
Y_{C}(M) \geq Y(M)-\frac{\varepsilon}{2} \\
\omega(M)+\frac{\varepsilon}{2} \geq W_{C}(M) \geq \omega(M) .
\end{array}\right.$$
From Proposition 4.1 we may assume that $C$ is conformally flat near some point $o \in M$.
Now consider the sphere $S^{n}$. By an argument similar to the one in the proof of Theorem 3.1, for any constant $\hat{\kappa}>0$ there exists a conformal class $\hat{C} \in \mathcal{C}\left(S^{n}\right)$, which is conformally flat near $\hat{o} \in S^{n}$, such that
$$\left\{\begin{array}{l}
Y_{\hat{C}}\left(S^{n}\right) \geq Y\left(S^{n}\right)-\frac{\varepsilon}{2}, \\
\hat{\kappa}+\frac{\varepsilon}{2} \geq W_{\hat{C}}\left(S^{n}\right) \geq \hat{\kappa} .
\end{array}\right.$$
We decompose the manifolds $M \backslash\{o\}$ and $S^{n} \backslash\{\hat{o}\}$ as follows (see Fig. 4.1):
$$\left\{\begin{array}{l}
M \backslash\{o\}=X \cup\left(S^{n-1} \times[0, \infty)\right), \\
S^{n} \backslash\{\hat{o}\}=\hat{X} \cup\left(S^{n-1} \times[0, \infty)\right) .
\end{array}\right.$$
Let $h_{0}$ be the standard metric on $S^{n-1}$. We choose metrics $g \in C$ and $\hat{g} \in \hat{C}$ satisfying
$$\left\{\begin{array}{llll}
g \in C & \text { with } & g(z, t)=h_{0}(z)+d t^{2} & \text { on } \\
\hat{g} \in \hat{C} & \text { with } & \hat{g}(z, t)=h_{0}(z)+d t^{2} & \text { on } \\
\end{array} \quad S^{n-1} \times[0, \infty),\right.$$

For each $\ell>0$ let $g_{\ell}$ be the natural gluing metric on the manifold
$$M \cong M \# S^{n} \cong\left(X \cup\left(S^{n-1} \times[0, \ell]\right)\right) \cup_{S^{n-1} \times\{\ell\}}\left(\left(S^{n-1} \times[0, \ell]\right) \cup \hat{X}\right),$$
which satisfies
$$\left.g_{\ell}\right|_{X \cup\left(S^{n-1} \times[0, \ell]\right)}=g, \quad \text { and }\left.\quad g_{\ell}\right|_{\hat{X} \cup\left(S^{n-1} \times[0, \ell]\right)}=\hat{g} .$$

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/7154e6c7-f149-4bc9-a073-5210e0e5e33d-19.jpg?height=441&width=1267&top_left_y=541&top_left_x=443}
\captionsetup{labelformat=empty}
\caption{Fig. 4.1. The manifolds $M \backslash\{o\}$ and $S^{n} \backslash\{\hat{o}\}$.}
\end{figure}
From the argument in the proof of [13, Theorem 2] (cf. [3]), there exists a large constant $\ell=\ell(\varepsilon)>0$ such that
$$\begin{aligned}
Y_{\left[g_{\ell}\right]}(M) & \geq Y_{C \sqcup \hat{C}}\left((M \backslash\{o\}) \sqcup\left(S^{n} \backslash\{\hat{o}\}\right)\right)-\frac{\varepsilon}{2} \\
& =Y_{C \sqcup \hat{C}}\left(M \sqcup S^{n}\right)-\frac{\varepsilon}{2}=\min \left\{Y_{C}(M), Y_{\hat{C}}\left(S^{n}\right)\right\}-\frac{\varepsilon}{2} \\
& =\left(Y(M)-\frac{\varepsilon}{2}\right)-\frac{\varepsilon}{2}=Y(M)-\varepsilon .
\end{aligned}$$
Recall that $g$ and $\hat{g}$ are conformally flat on $S^{n-1} \times[0, \infty)$. Hence for the Weyl constant, we have:
$$\begin{aligned}
W_{\left[g_{\ell}\right]}(M) & =\int_{X}\left|W_{g}\right|_{\hat{g}}^{\frac{n}{2}} d \sigma_{g}+\int_{\hat{X}}\left|W_{\hat{g}}\right|_{\hat{g}}^{\frac{n}{2}} d \sigma_{\hat{g}} \\
& =W_{C}(M)+W_{\hat{C}}\left(S^{n}\right)
\end{aligned}$$
This combined with (14) and (15) implies
$$\hat{\kappa}+\omega(M)+\varepsilon \geq W_{C}(M)+W_{\hat{C}}\left(S^{n}\right) \geq \hat{\kappa}+\omega(M) .$$
We take $\hat{\kappa}=\kappa-\omega(M)>0$ and then obtain the second inequality in Theorem A. This completes the proof of Theorem A. \(\square\)

\section*{References}
\begin{itemize}
\item[] [1] K. Akutagawa, Yamabe metrics of positive scalar curvature and conformally flat manifolds, Diff. Geom. Appl. 4 (1994), 239-258.
\item[] [2] K. Akutagawa, B. Botvinnik, The relative Yamabe invariant, to appear in Comm. Anal. Geom.
\end{itemize}
[3] K. Akutagawa, B. Botvinnik, Yamabe metrics on cylindrical manifolds, math.DG/0107164.
[4] T. Aubin, Some nonlinear problems in Riemannian geometry, Springer Monographs in Mathematics, Springer-Verlag, Berlin, 1998.
[5] A. Besse, Einstein manifolds, Springer, Berlin, 1987.
[6] M. Gursky, The Weyl functional, de Rham cohomology, and Kähler-Einstein metrics, Ann. of Math. 148 (1998), 315-337.
[7] M. Gursky, Four-manifolds with $\delta W^{+}=0$ and Einstein constants of the sphere, Math. Ann. 318 (2000), 417-431.
[8] M. Gursky, C. LeBrun, Yamabe invariants and spin ${ }^{c}$ structures, Geom. Funct. Anal. 8 (1998), 965-977.
[9] M. Gursky, C. LeBrun, On Einstein manifolds of positive sectional curvature, Ann. Global Anal. Geom. 17 (1999), 315-328.
[10] M. Ishida, C. LeBrun, Curvature, connected sum, and Seiberg-Witten theory, math.DG/0111228.
[11] O. Kobayashi, On a conformally invariant functional of the space of Riemannian metrics, J. Math. Soc. Japan 37 (1985), 373-389.
[12] O. Kobayashi, A Willmore type problem for $S^{2} \times S^{2}$, Differential geometry and differential equations (Shanghai, 1985), 67-72, Lecture Notes in Math. 1255, Springer-Verlag, 1987.
[13] O. Kobayashi, Scalar curvature of a metric with unit volume, Math. Ann. 279 (1987), 253-265.
[14] O. Kobayashi, On the Yamabe problem, (in Japanese) Seminar on Mathematical Sciences, 16. Keio University, Department of Mathematics, Yokohama, 1990.
[15] N. Kuiper, On conformally flat spaces in the large, Ann. of Math. 50 (1949), 916-924.
[16] C. LeBrun, Einstein metrics and Mostow rigidity, Math. Res. Lett. 2 (1995), 1-8.
[17] C. LeBrun, Four-manifolds without Einstein metrics, Math. Res. Lett. 3 (1996), 133-147.
[18] C. LeBrun, Yamabe constants and the perturbed Seiberg-Witten equations, Comm. Anal. Geom. 5 (1997), 535-553.
[19] C. LeBrun, Weyl curvature, Einstein metrics, and Seiberg-Witten theory, Math. Res. Lett. 5 (1998), 423-438.
[20] C. LeBrun, Kodaira dimension and the Yamabe problem, Comm. Anal. Geom. 7 (1999), 133-156.
[21] C. LeBrun, Ricci curvature, minimal volumes, and Seiberg-Witten theory, Invent. Math. 145 (2001), 279-316.
[22] J. Petean, Computations of the Yamabe invariant, Math. Res. Lett. 5 (1998), 703-709.
[23] R. Schoen, Conformal deformation of a Riemannian metric to constant scalar curvature, J. Diff. Geom. 20 (1984), 479-495.
[24] R. Schoen, Variational theory for the totatl scalar curvature functional for Riemannian metrics and related topics, Topics in calculus of variations (Montecatini Terme, 1987), 120-154, Lecture Notes in Math. 1365, Springer-Verlag, 1989.
[25] R. Schoen, S.-T. Yau, Conformally flat manifolds, Kleinian groups and scalar curvature, Invent. Math. 92 (1988), 47-71.

Kazuo Akutagawa, Shizuoka University, Shizuoka, Japan
e-mail: smkacta@ipc.shizuoka.ac.jp

Boris Botvinnik, University of Oregon, Eugene, USA
e-mail: botvinn@math.uoregon.edu
Osamu Kobayashi, Kumamoto University, Kumamoto, Japan
e-mail: ok@math.sci.kumamoto-u.ac.jp
Harish Seshadri, University of Oregon, Eugene, USA
e-mail: harish@darkwing.uoregon.edu

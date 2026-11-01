---
retention_scope: session
part: 1
total_parts: 1
---

---
source_file: 0906_5195v2.pdf
converter: mathpix
format: mmd
---

\title{
SURFACES OF GENERAL TYPE WITH $p_{g}=1$ AND $q=0$
}

\author{
HEESANG PARK, JONGIL PARK, AND DONGSOO SHIN
}

\begin{abstract}
In this paper we construct a new family of simply connected minimal complex surfaces of general type with $p_{g}=1, q=0$, and $K^{2}=3,4,5,6,8$ using a $\mathbb{Q}$-Gorenstein smoothing theory. We also reconstruct minimal complex surfaces of general type with $p_{g}=1, q=0$, and $K^{2}=1,2$ using the same method.
\end{abstract}

\section*{1. Introduction}

In the geography of minimal complex surfaces of general type, one of the fundamental problems is to find a new family of simply connected minimal surfaces with given topological invariants such as $p_{g}, q$, and $K^{2}$. This geography problem has been studied extensively by algebraic geometers and topologists for a long time, so that various families of surfaces of general type have been constructed ([2], Chapter VII). Nevertheless, in the case of $p_{g}=1$ and $q=0$, only a few examples are known (see below) and there were no such simply connected examples with $K^{2} \geq 3$ previously known. Note that this class of surfaces has been drawn attention because they provide counterexamples to the Torelli problems.

One the other hand, complex surfaces of general type with $p_{g}=1$ and $q=0$ also provide exotic smooth structures on the topological 4-manifolds $3 \mathbb{C P}^{2} \sharp n \overline{\mathbb{C P}}^{2}$. In fact, many examples of exotic $3 \mathbb{C P}^{2} \sharp n \overline{\mathbb{C P}}^{2}$ for $n=5$ or $7 \leq n \leq 19$ were constructed via various surgery techniques. For example, Gompf [6] constructed exotic $3 \mathbb{C P}^{2} \sharp n \overline{\mathbb{C P}}^{2}$ for $14 \leq n \leq 18$ by a symplectic sum, B.D. Park [15] constructed exotic $3 \mathbb{C P}^{2} \sharp n \overline{\mathbb{C P}}^{2}$ for $10 \leq n \leq 13$ via knot surgery and symplectic sum, and Stipsicz and Szabó [21], and the second author [17] constructed exotic $3 \mathbb{C P}^{2} \sharp 9 \overline{\mathbb{C P}}^{2}$ and $3 \mathbb{C P}^{2} \sharp 8 \overline{\mathbb{C P}}^{2}$ using rational blowdowns, respectively. However it was not known whether those exotic $3 \mathbb{C P}^{2} \sharp n \overline{\mathbb{C P}}^{2}$ 's constructed so far admit complex structures.

All known surfaces of general type with $p_{g}=1$ and $q=0$ are constructed by classical methods: Quotient and covering. Kynev [10] constructed a surface with $K^{2}=1$ as a quotient of the Fermat sextic in $\mathbb{C P}^{3}$ by a suitable action of a group of order 6. According to Catanese [3], all minimal surfaces of general type with $p_{g}=1$ and $K^{2}=1$ are diffeomorphic and simply connected. Catanese and Debarre [4] constructed surfaces with $K^{2}=2$ by double coverings of the projective plane $\mathbb{C P}^{2}$ or smooth minimal K3 surfaces. In fact, they classified such surfaces into five classes according to the degree and the image of the bicanonical map. Four of them are simply connected and the other one has a torsion $\mathbb{Z} / 2 \mathbb{Z}$. Todorov [22] also constructed non-simply connected surfaces with $2 \leq K^{2} \leq 8$ by considering

\footnotetext{
2000 Mathematics Subject Classification. Primary 14J29; Secondary 14J10, 14J17, 53D05.
Key words and phrases. $\mathbb{Q}$-Gorenstein smoothing, rational blow-down surgery, surface of general type.
}
double covers of K3 surfaces. Note that all his examples with $3 \leq K^{2} \leq 8$ have big fundamental groups.

The main result of this paper is the following.
Theorem. There are simply connected minimal complex surfaces of general type with $p_{g}=1, q=0$, and $K^{2}=1,2, \ldots, 6,8$ and a minimal complex surface of general type with $p_{g}=1, q=0, K^{2}=2$, and $H_{1}=\mathbb{Z} / 2 \mathbb{Z}$.

In order to construct such surfaces with $1 \leq K^{2} \leq 6$, we take a similar strategy in Y. Lee and J. Park [13]. We blow up an elliptic K3 surface in a suitable set of points so that we obtain a surface with a very special configuration of rational curves. Inside this configuration we find some disjoint chains which can be contracted to special quotient singularities. These singularities admit a local $\mathbb{Q}$-Gorenstein smoothing, which is a smoothing whose relative canonical class is $\mathbb{Q}$ -Cartier. And then, we prove that these local smoothings can be glued to a global $\mathbb{Q}$-Gorenstein smoothing of the whole singular surface by showing that the obstruction space of a global smoothing is zero. Finally it is not difficult to show that a general fiber of the smoothing is the desired surface. The key ingredient of the construction is to develop a new method for proving that the obstruction space is zero because the method in Y. Lee and J. Park [13] for a computation of the obstruction space cannot be applied to our cases.

For constructing a simply connected surface with $K^{2}=8$, we blow up a K3 surface $\bar{Y}$ in a suitable set of points so that we obtain a surface with some special disjoint linear chains of rational curves which can be contracted to singularities class $T$ on a singular surface $\bar{X}$ with $H^{2}\left(\mathcal{T}_{\bar{X}}\right) \neq 0$. In order to prove the existence of a global $\mathbb{Q}$-Gorenstein smoothing of $\bar{X}$, we apply the cyclic covering trick developed in Y. Lee and J. Park [12]. The cyclic covering trick says that, if a cyclic covering $\pi: V \rightarrow W$ of singular surfaces satisfies certain conditions and the base $W$ has a $\mathbb{Q}$-Gorenstein smoothing, then the cover $V$ has also a $\mathbb{Q}$-Gorenstein smoothing. The main ingredient is that we construct an unramified double covering $\bar{\pi}: \bar{X} \rightarrow X$ to a singular surface $X$ constructed in a recent paper [16] of the first author. It is a main result of H. Park [16] that the singular surface $X$ has a global $\mathbb{Q}$-Gorenstein smoothing and a general fiber $X_{t}$ of the smoothing of $X$ is a surface of general type with $p_{g}=0, K^{2}=4$, and $\pi_{1}=\mathbb{Z} / 2 \mathbb{Z}$. We show that the double covering $\bar{\pi}: \bar{X} \rightarrow X$ satisfies all the conditions of the cyclic covering trick; hence there is a global $\mathbb{Q}$-Gorenstein smoothing of $\bar{X}$. Then it is not difficult to show that a general fiber $\bar{X}_{t}$ of the smoothing of $\bar{X}$ is the desired surface.

This paper is organized as follows. In Section 2 we reconstruct complex surfaces with $p_{g}=1, q=0$ and $K^{2}=2$ : A simply connected surface and a surface with $H_{1}=\mathbb{Z} / 2 \mathbb{Z}$. We prove in Section 3 that the obstruction spaces of global smoothings of the singular surfaces constructed in Section 2 are zero. In Section 4 and Section 5. we construct various examples of simply connected surfaces with $p_{g}=1, q=0$ and $K^{2}=1,2, \ldots, 6,8$.

Acknowledgement. The authors would like to thank Professor Yongnam Lee for some valuable comments on the first draft of this article. Jongil Park was supported by Basic Science Research Program through the National Research Foundation of Korea (NRF) Grant funded by the Korean Government (2009-0093866). He also holds a joint appointment at Korea Institute for Advanced Study and at Research Institute of Mathematics in Seoul National University. Dongsoo Shin was supported
by Basic Science Research Program through the National Research Foundation of Korea (NRF) grant funded by the Korean Government (2010-0002678).

\section*{2. Surfaces with $p_{g}=1, q=0$, and $K^{2}=2$}

In this section we construct a simply connected minimal surface of general type with $p_{g}=1, q=0$, and $K^{2}=2$. We start with a special rational elliptic surface $E(1)$. Let $L_{1}, L_{2}, L_{3}$, and $A$ be lines in $\mathbb{C P}^{2}$ and let $B$ be a smooth conic in $\mathbb{C P}^{2}$ intersecting as in Figure 1(A). We consider a pencil of cubics $\left\{\lambda\left(L_{1}+L_{2}+L_{3}\right)+\right.$ $\left.\mu(A+B) \mid[\lambda: \mu] \in \mathbb{C P}^{1}\right\}$ in $\mathbb{C P}^{2}$ generated by two cubic curves $L_{1}+L_{2}+L_{3}$ and $A+B$, which has 4 base points, say, $p, q, r$ and $s$. In order to obtain an elliptic fibration over $\mathbb{C P}^{1}$ from the pencil, we blow up three times at $p$ and $r$, respectively, and twice at $s$, including infinitely near base-points at each point. We perform one further blowing-up at the base point $q$. By blowing-up totally nine times, we resolve all base points (including infinitely near base-points) of the pencil and we then get a rational elliptic surface $E(1)$ with an $I_{8}$-singular fiber, an $I_{2}$-singular fiber, two nodal singular fibers, and four sections; Figure 1(B).

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/9ee2462a-e4a3-493e-91b6-73cb6d621727-03.jpg?height=451&width=1139&top_left_y=1195&top_left_x=492}
\captionsetup{labelformat=empty}
\caption{Figure 1. A rational elliptic surface $E(1)$}
\end{figure}

Let $Y$ be a double cover of the rational elliptic surface $E(1)$ branched along two general fibers. Then the surface $Y$ is an elliptic K3 surface with two $I_{8}$-singular fibers, two $I_{2}$-singular fibers, four nodal singular fibers, and four sections; Figure 2(A). In the following construction we use only one $I_{8}$-singular fiber, one nodal singular fiber, and three sections; Figure 2(B).

Let $\tau: V \rightarrow Y$ be the blowing-up at the node of the nodal singular fiber and let $E$ be the exceptional divisor of $\tau$. Since $K_{Y}=0$, we have $K_{V}=E$. Let $D=D_{1}+\cdots+D_{6}$ be the part of the $I_{8}$-singular fiber. Let $S_{i}(i=1,2,3)$ be the sections of the fibration $V \rightarrow \mathbb{C P}^{1}$ and set $S=S_{1}+S_{2}+S_{3}$. Let $F$ be the proper transform of the nodal fiber of the K3 surface $Y$; Figure 3.

We blow up the surface $V$ three times totally at the three marked points ● and blow up twice at the marked point $\odot$. We then get a surface $Z$; Figure 4. There exist three disjoint linear chains of $\mathbb{C P}^{1}$ 's in $Z$ :
$$\stackrel{-3}{\circ}^{-6}-\stackrel{-2}{\circ}^{-3}-\stackrel{-2}{\circ}^{\circ}, \quad \circ^{-4}-\text { o }^{-2}-\stackrel{-}{\circ}^{-2}-\stackrel{-3}{\circ}^{-2}, \quad \begin{aligned}
& -4 \\
& \circ
\end{aligned} \text {. }$$

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/9ee2462a-e4a3-493e-91b6-73cb6d621727-04.jpg?height=829&width=1102&top_left_y=425&top_left_x=509}
\captionsetup{labelformat=empty}
\caption{Figure 2. An elliptic K3 surface $Y$}
\end{figure}

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/9ee2462a-e4a3-493e-91b6-73cb6d621727-04.jpg?height=357&width=417&top_left_y=1366&top_left_x=853}
\captionsetup{labelformat=empty}
\caption{Figure 3. A surface $V=Y \sharp \overline{\mathbb{C P}}^{2}$}
\end{figure}

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/9ee2462a-e4a3-493e-91b6-73cb6d621727-04.jpg?height=352&width=412&top_left_y=1852&top_left_x=855}
\captionsetup{labelformat=empty}
\caption{Figure 4. A surface $Z=Y \sharp 6 \overline{\mathbb{C P}}^{2}$}
\end{figure}

Main construction. By applying $\mathbb{Q}$-Gorenstein smoothing theory to the surface $Z$ as in Y. Lee and J. Park [13] and the authors [19, 20], we construct a complex
surface of general type with $p_{g}=1, q=0$, and $K^{2}=2$. That is, we first contract the three chains of $\mathbb{C P}^{1}$ 's from the surface $Z$ so that it produces a normal projective surface $X$ with three permissible singular points. In Section 3 we will show that the singular surface $X$ has a global $\mathbb{Q}$-Gorenstein smoothing. Let $X_{t}$ be a general fiber of the $\mathbb{Q}$-Gorenstein smoothing of $X$. Since $X$ is a (singular) surface with $p_{g}=1, q=0$, and $K^{2}=2$, by applying general results of complex surface theory and $\mathbb{Q}$-Gorenstein smoothing theory, one may conclude that a general fiber $X_{t}$ is a complex surface of general type with $p_{g}=1, q=0$, and $K^{2}=2$. Furthermore, it is not difficult to show that a general fiber $X_{t}$ is minimal and simply connected by using a similar technique in Y. Lee and J. Park [13] and the authors [19, 20].

Remark. Catanese and Debarre [4] proved that surfaces of general type with $p_{g}=1$, $q=0$, and $K^{2}=2$ are divided into five types according to the degree and the image of the bicanonical map. Four of them are simply connected and the other one has a torsion $\mathbb{Z} / 2 \mathbb{Z}$. It is an interesting problem to determine in which class the simply connected example constructed in this section is contained. We leave this question for the future research.
2.1. An example with $K^{2}=2$ and $H_{1}=\mathbb{Z} / 2 \mathbb{Z}$. We construct a minimal complex surface of general type with $p_{g}=1, q=0, K^{2}=2$, and $H_{1}=\mathbb{Z} / 2 \mathbb{Z}$. Let $A, L_{i}(i=1,2,3)$ be lines on the projective plane $\mathbb{C P}^{2}$ and $B$ a nonsingular conic on $\mathbb{C P}^{2}$ which intersect as in Figure 5(A). Consider a pencil of cubics generated by the two cubics $A+B$ and $L_{1}+L_{2}+L_{3}$. By resolving the base points of the pencil of cubics including infinitely near base-points, we obtain a rational elliptic surface $E(1)$ with an $I_{7}$-singular fiber, an $I_{2}$-singular fiber, an cusp singular fiber, a nodal singular fiber, and five sections as in Figure 5(B).

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/9ee2462a-e4a3-493e-91b6-73cb6d621727-05.jpg?height=430&width=1121&top_left_y=1512&top_left_x=501}
\captionsetup{labelformat=empty}
\caption{Figure 5. A rational elliptic surface $E(1)$ for $K^{2}=2$ and $H_{1}=\mathbb{Z} / 2 \mathbb{Z}$}
\end{figure}

Let $Y$ be a double cover of the rational elliptic surface $E(1)$ branched along two general fibers $F_{1}$ and $F_{2}$ near the cusp singular fiber. Then $Y$ is an elliptic K3 surface with two $I_{7}$-singular fibers, two $I_{2}$-singular fibers, two cusp singular fibers, two nodal singular fibers, and five sections. We use only two $I_{7}$-singular fibers, two $I_{2}$-singular fibers, and two sections; Figure 6(A). We blow up eight times totally at the eight marked points • We then get a surface $Z$; Figure 6(B). There exist six disjoint linear chains of $\mathbb{C P}^{1}$ 's in $Z$ :
$$\stackrel{-5}{\circ}^{-3}-\stackrel{-2}{\circ}^{-\circ^{-2}}, \quad \frac{\circ^{-5}}{\circ^{-3}}-\stackrel{-2}{\circ}^{-2}, \quad \stackrel{-3}{\circ}^{-2}-\stackrel{-3}{\circ}^{-3}-\stackrel{-2}{\circ}^{-3}, \quad \stackrel{-4}{\circ}, \quad \stackrel{-4}{\circ}$$

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/9ee2462a-e4a3-493e-91b6-73cb6d621727-06.jpg?height=909&width=814&top_left_y=428&top_left_x=655}
\captionsetup{labelformat=empty}
\caption{Figure 6. An example with $H_{1}=\mathbb{Z} / 2 \mathbb{Z}$}
\end{figure}

We now briefly explain how to prove that the complex surface obtained by the above configuration has $H_{1}=\mathbb{Z} / 2 \mathbb{Z}$. For proving this one may apply a similar method in Y. Lee and J. park [11] and the authors [18]. The key part of the method is finding a basis for the free abelian group $H_{2}(Z, \mathbb{Z})$ and calculating how the elements of the basis intersect with the contracted rational curves. Then the proof of being $H_{1}=\mathbb{Z} / 2 \mathbb{Z}$ follows because the configuration of the contracted rational curves are very special. A basis for $H_{2}(Z, \mathbb{Z})$ in our case can be obtained as follows: Since the K3 surface $Y$ may be regarded as a 4-manifold obtained by applying a fiber sum surgery from the rational elliptic surface $E(1)$ along two general fibers near the cusp singular fiber, the homology $H_{2}(Z, \mathbb{Z})$ are generated by 18 spheres induced from a basis for $H_{1}(E(1), \mathbb{Z})$, four new homology elements emerging during the fiber sum surgery, and the eight -1-curves induced from eight blowing-ups on $Y$; cf. [7, p. 70]. It is not difficult to calculate how the 18 spheres induced from a basis for $H_{1}(E(1), \mathbb{Z})$ intersect with the contracted rational curves because a basis for $H_{1}(E(1), \mathbb{Z})$ can be represented by linear combinations of -2-curves consisting of the $I_{7}$-singular fiber and the five sections. Furthermore the four new homology elements emerging during the fiber sum surgery do not intersect the contracted rational curves. Hence one can apply a similar method in Y. Lee and J. park [11] and the authors [18] to show that the complex surface obtained by the above configuration has $H_{1}=\mathbb{Z} / 2 \mathbb{Z}$.

\section*{3. The Existence of $\mathbb{Q}$-Gorenstein smoothings}

This section is devoted to the proof of the following theorem.

Theorem 3.1. The singular surface $X$ constructed in the main construction in Section 2 has a global $\mathbb{Q}$-Gorenstein smoothing.

For this, we first briefly review some basic facts on $\mathbb{Q}$-Gorenstein smoothing theory for normal projective surfaces with special quotient singularities (refer to Y. Lee and J. Park [13] for details).

Definition. Let $X$ be a normal projective surface with quotient singularities. Let $\mathcal{X} \rightarrow \Delta$ (or $\mathcal{X} / \Delta$ ) be a flat family of projective surfaces over a small disk $\Delta$. The one-parameter family of surfaces $\mathcal{X} \rightarrow \Delta$ is called a $\mathbb{Q}$-Gorenstein smoothing of $X$ if it satisfies the following three conditions;
\begin{itemize}
\item[(i)] the general fiber $X_{t}$ is a smooth projective surface,
\item[(ii)] the central fiber $X_{0}$ is $X$,
\item[(iii)] the canonical divisor $K_{\mathcal{X} / \Delta}$ is $\mathbb{Q}$-Cartier.
\end{itemize}

A $\mathbb{Q}$-Gorenstein smoothing for a germ of a quotient singularity $\left(X_{0}, 0\right)$ is defined similarly. A quotient singularity which admits a $\mathbb{Q}$-Gorenstein smoothing is called a singularity of class $T$.

Proposition 3.2 ([8, 14]). Let $\left(X_{0}, 0\right)$ be a germ of two dimensional quotient singularity. If $\left(X_{0}, 0\right)$ admits a $\mathbb{Q}$-Gorenstein smoothing over the disk, then $\left(X_{0}, 0\right)$ is either a rational double point or a cyclic quotient singularity of type $\frac{1}{d n^{2}}(1, d n a-1)$ for some integers $a, n, d$ with $a$ and $n$ relatively prime.

Proposition 3.3 ([8, 14]). (1) The singularities $\circ^{-4}$ and $\circ^{-3}-\circ^{-2}-\circ^{-2} \cdots \circ^{-2} \circ^{-3}$ are of class $T$.
\begin{itemize}
\item[(2)] If the singularity $\stackrel{-b_{1}}{\circ}-\cdots-\stackrel{-b_{r}}{\circ}$ is of class $T$, then so are
$$\stackrel{-2}{\circ}-\stackrel{-b_{1}}{\circ}-\cdots-\stackrel{-b_{r}-1}{\circ}-\stackrel{-b_{r}-1}{\circ} \text { and } \stackrel{-b_{1}-1}{\circ}-\stackrel{-b_{2}}{\circ}-\cdots-\stackrel{-b_{r}}{\circ}-\stackrel{-2}{\circ} \text {. }$$
\item[(3)] Every singularity of class $T$ that is not a rational double point can be obtained by starting with one of the singularities described in (1) and iterating the steps described in (2).
\end{itemize}

Let $X$ be a normal projective surface with singularities of class $T$. Due to the result of Kollár and Shepherd-Barron [8], there is a $\mathbb{Q}$-Gorenstein smoothing locally for each singularity of class $T$ on $X$. The natural question arises whether this local $\mathbb{Q}$-Gorenstein smoothing can be extended over the global surface $X$ or not. Roughly geometric interpretation is the following: Let $\cup_{\alpha} V_{\alpha}$ be an open covering of $X$ such that each $V_{\alpha}$ has at most one singularity of class $T$. By the existence of a local $\mathbb{Q}$ -Gorenstein smoothing, there is a $\mathbb{Q}$-Gorenstein smoothing $\mathcal{V}_{\alpha} / \Delta$. The question is if these families glue to a global one. The answer can be obtained by figuring out the obstruction map of the sheaves of deformation $T_{X}^{i}=\operatorname{Ext}_{X}^{i}\left(\Omega_{X}, \mathcal{O}_{X}\right)$ for $i=0,1,2$. For example, if $X$ is a smooth surface, then $T_{X}^{0}$ is the usual holomorphic tangent sheaf $T_{X}$ and $T_{X}^{1}=T_{X}^{2}=0$. By applying the standard result of deformations to a normal projective surface with quotient singularities, we get the following

Proposition 3.4 (Wahl [24, §4]). Let $X$ be a normal projective surface with quotient singularities. Then
\begin{itemize}
\item[(1)] The first order deformation space of $X$ is represented by the global Ext 1-group $\mathbb{T}_{X}^{1}=\operatorname{Ext}_{X}^{1}\left(\Omega_{X}, \mathcal{O}_{X}\right)$.
\item[(2)] The obstruction lies in the global Ext 2-group $\mathbb{T}_{X}^{2}=\operatorname{Ext}_{X}^{2}\left(\Omega_{X}, \mathcal{O}_{X}\right)$.
\end{itemize}

Furthermore, by applying the general result of local-global spectral sequence of ext sheaves to deformation theory of surfaces with quotient singularities so that $E_{2}^{p, q}=H^{p}\left(T_{X}^{q}\right) \Rightarrow \mathbb{T}_{X}^{p+q}$, and by $H^{j}\left(T_{X}^{i}\right)=0$ for $i, j \geq 1$, we also get

Proposition 3.5 (Manetti [14], Wahl [24]). Let $X$ be a normal projective surface with quotient singularities. Then
\begin{itemize}
\item[(1)] We have the exact sequence
$$0 \rightarrow H^{1}\left(T_{X}^{0}\right) \rightarrow \mathbb{T}_{X}^{1} \rightarrow \operatorname{ker}\left[H^{0}\left(T_{X}^{1}\right) \rightarrow H^{2}\left(T_{X}^{0}\right)\right] \rightarrow 0$$
where $H^{1}\left(T_{X}^{0}\right)$ represents the first order deformations of $X$ for which the singularities remain locally a product.
\item[(2)] If $H^{2}\left(T_{X}^{0}\right)=0$, every local deformation of the singularities may be globalized.
\end{itemize}

As mentioned above, there is a local $\mathbb{Q}$-Gorenstein smoothing for each singularity of $X$ due to the result of Kollár and Shepherd-Barron [8]. Hence it remains to show that every local deformation of the singularities can be globalized. Note that the following proposition tells us a sufficient condition for the existence of a global $\mathbb{Q}$-Gorenstein smoothing of $X$.

Proposition 3.6 (Y. Lee and J. Park [13]). Let $X$ be a normal projective surface with singularities of class $T$. Let $\pi: V \rightarrow X$ be the minimal resolution and let $A$ be the reduced exceptional divisor. Suppose that $H^{2}\left(T_{V}(-\log A)\right)=0$. Then $H^{2}\left(T_{X}^{0}\right)=0$ and there is a $\mathbb{Q}$-Gorenstein smoothing of $X$.

Furthermore, the proposition above can be easily generalized to any log resolution of $X$ by keeping the vanishing of cohomologies under blowing up at the points. It is obtained by the following well-known result.

Proposition 3.7 (Flenner and Zaidenberg [5, §1]). Let $V$ be a nonsingular surface and let $A$ be a simple normal crossing divisor in $V$. Let $f: V^{\prime} \rightarrow V$ be a blowing up of $V$ at a point $p$ of $A$. Set $A^{\prime}=f^{-1}(A)_{\text {red }}$. Then $h^{2}\left(T_{V^{\prime}}\left(-\log A^{\prime}\right)\right)=$ $h^{2}\left(T_{V}(-\log A)\right)$.

Therefore Theorem 3.1 follows from Proposition 3.6 and the following proposition:

Proposition 3.8. $H^{2}\left(T_{V}(-\log (D+S+F))\right)=H^{0}\left(\Omega_{V}(\log (D+S+F))(E)\right)=0$.
The idea of the proof is as follows: There is an exact sequence of sheaves
$$0 \rightarrow \Omega_{V} \rightarrow \Omega_{V}(\log (D+S+F)) \rightarrow \bigoplus_{i=1}^{6} \mathcal{O}_{D_{i}} \oplus \bigoplus_{i=1}^{3} \mathcal{O}_{S_{i}} \oplus \mathcal{O}_{F} \rightarrow 0$$
By tensoring $\mathcal{O}_{V}(E)$, we have an exact sequence
$$0 \rightarrow \Omega_{V}(E) \rightarrow \Omega_{V}(\log (D+S+F))(E) \rightarrow \bigoplus_{i=1}^{6} \mathcal{O}_{D_{i}} \oplus \bigoplus_{i=1}^{3} \mathcal{O}_{S_{i}} \oplus \mathcal{O}_{F}(E) \rightarrow 0 .$$
Since $H^{0}\left(\Omega_{V}(E)\right)=0$, the proof of Proposition 3.8 is done if we show that the connecting homomorphism
$$\bigoplus_{i=1}^{6} H^{0}\left(\mathcal{O}_{D_{i}}\right) \oplus \bigoplus_{i=1}^{3} H^{0}\left(\mathcal{O}_{S_{i}}\right) \oplus H^{0}\left(\mathcal{O}_{F}(E)\right) \rightarrow H^{1}\left(\Omega_{V}(E)\right)$$
is injective.

The proof of Proposition 3.8 begins with the following Lemma. We have a commutative diagram
![](https://cdn.mathpix.com/cropped/9ee2462a-e4a3-493e-91b6-73cb6d621727-09.jpg?height=327&width=939&top_left_y=509&top_left_x=591)

Lemma 3.9. The composition map
$$\beta_{1} \circ c_{1}: \bigoplus_{i=1}^{6} H^{0}\left(\mathcal{O}_{D_{i}}\right) \oplus \bigoplus_{i=1}^{3} H^{0}\left(\mathcal{O}_{S_{i}}\right) \oplus H^{0}\left(\mathcal{O}_{F}\right) \rightarrow H^{1}\left(\Omega_{V}(E)\right)$$
is injective.
Proof. Note that the map $c_{1}$ is the first Chern class map. Since the intersection matrix, whose entries are the intersection numbers of $D_{i}(i=1, \ldots, 6), S_{j}(j=$ $1,2,3)$, and $F$, is invertible, their images by the map $c_{1}$ are linearly independent. Therefore the map $c_{1}$ is injective.

Consider the commutative diagram
![](https://cdn.mathpix.com/cropped/9ee2462a-e4a3-493e-91b6-73cb6d621727-09.jpg?height=593&width=1033&top_left_y=1311&top_left_x=544)
where the vertical sequence is induced from the exact sequence
$$0 \rightarrow H^{0}\left(\Omega_{V} \otimes \mathcal{O}_{E}(E)\right) \xrightarrow{\delta} H^{1}\left(\Omega_{V}\right) \xrightarrow{\beta_{1}} H^{1}\left(\Omega_{V}(E)\right) \xrightarrow{\gamma} H^{1}\left(\Omega_{V} \otimes \mathcal{O}_{E}(E)\right) \rightarrow 0 .$$
Claim: The connecting homomorphism $\delta: H^{0}\left(\Omega_{V} \otimes \mathcal{O}_{E}(E)\right) \rightarrow H^{1}\left(\Omega_{V}\right)$ is the first Chern class map of $\mathcal{O}_{V}(E)$ : Since $H^{0}\left(\Omega_{E} \otimes \mathcal{O}_{E}(E)\right)=0$, we have an isomorphism
$$H^{0}\left(\mathcal{O}_{E}(-E) \otimes \mathcal{O}_{E}(E)\right) \stackrel{\cong}{\rightarrow} H^{0}\left(\Omega_{V} \otimes \mathcal{O}_{E}(E)\right) .$$
Here the above map is given by $z_{\alpha} \otimes \frac{1}{z_{\alpha}} \mapsto\left\{\frac{d z_{\alpha}}{z_{\alpha}}\right\}$, where $z_{\alpha}$ is a local equation of $E$. Therefore the connecting homomorphism $\delta: H^{0}\left(\Omega_{V} \otimes \mathcal{O}_{E}(E)\right) \rightarrow H^{1}\left(\Omega_{V}\right)$ is given by
$$\left\{\frac{d z_{\alpha}}{z_{\alpha}}\right\} \mapsto\left\{\frac{d z_{\alpha}}{z_{\alpha}}-\frac{d z_{\beta}}{z_{\beta}}\right\}=\left\{d\left(\frac{z_{\alpha}}{z_{\beta}}\right) /\left(\frac{z_{\alpha}}{z_{\beta}}\right)\right\},$$
which is the first Chern class map of $\mathcal{O}_{V}(E)$. This proves the claim.
Since $E$ is the exceptional divisor, it is independent of the other divisors in $H^{1}\left(\Omega_{V}\right)$. Therefore $\operatorname{im} c_{1} \cap \operatorname{im} \delta=0$; hence the composition map $\beta_{1} \circ c_{1}$ is injective. \(\square\)

We now concentrate on the following restriction map $d_{1}^{\prime}$ of the map $d_{1}$ in (3.1):
$$d_{1}^{\prime}: H^{0}\left(\mathcal{O}_{F}(E)\right) \rightarrow H^{1}\left(\Omega_{V}(E)\right),$$
which is also regarded as a connecting homomorphism induced from the exact sequence
$$0 \rightarrow \Omega_{V} \rightarrow \Omega_{V}(\log F) \rightarrow \mathcal{O}_{F} \rightarrow 0$$
tensored by $\mathcal{O}_{V}(E)$.
Lemma 3.10. We have $H^{0}\left(\Omega_{V}(\log F)(E)\right)=0$.
Proof. Let $C$ be a general fiber of the elliptic fibration $\phi: Y \rightarrow \mathbb{C P}^{1}$. By the projection formula we have
$$\begin{aligned}
H^{0}\left(\Omega_{V}(\log F)(E)\right) & \subseteq H^{0}\left(\Omega_{V}(F+E)\right)=H^{0}\left(\Omega_{V}\left(\tau^{*} C-E\right)\right) \\
& \subseteq H^{0}\left(\Omega_{V}\left(\tau^{*} C\right)\right)=H^{0}\left(Y, \Omega_{Y}(C)\right)
\end{aligned}$$
On the other hand it is not difficult to show that
$$H^{0}\left(Y, \Omega_{Y}(C)\right)=H^{0}\left(\mathbb{C} \mathbb{P}^{1}, \Omega_{\mathbb{C P}}(1)\right)=0$$
by a similar method in Y. Lee and J. Park [13, Lemma 2]. Therefore the assertion follows. \(\square\)

By the above lemma, we have the following commutative diagram of exact sequences:
![](https://cdn.mathpix.com/cropped/9ee2462a-e4a3-493e-91b6-73cb6d621727-10.jpg?height=662&width=1076&top_left_y=1508&top_left_x=488)

Lemma 3.11. $h^{0}\left(\Omega_{V}(\log F) \otimes \mathcal{O}_{E}(E)\right)=1$.
Proof. Let
$$\bar{r}: \Omega_{V}(\log F) \otimes \mathcal{O}_{E} \rightarrow \Omega_{E} \otimes \mathcal{O}_{E}(F)$$
be the restriction to the subsheaf $\Omega_{V}(\log F)$ of the restriction map $r \otimes \mathrm{id}:\left.\Omega_{V}\right|_{E} \otimes$ $\mathcal{O}_{E}(F) \rightarrow \Omega_{E} \otimes \mathcal{O}_{E}(F)$.

Claim. $\operatorname{ker} \bar{r}=\mathcal{O}_{E}(-E)$ : Let $z_{1}, z_{2}$ be the local equations of $F, E$, respectively. Note that the restriction map $r:\left.\Omega_{V}\right|_{E} \rightarrow \Omega_{E}$ is defined by
$$r: \bar{a} d z_{1}+\bar{b} d z_{2}=\bar{a} d \overline{z_{1}}$$
Hence the map $\bar{r}$ is defined by
$$\bar{r}\left(\bar{a} \frac{d z_{1}}{z_{1}}+\bar{b} d z_{2}\right)=\bar{a} \frac{d z_{1}}{z_{1}}$$
It follows that $\operatorname{ker} \bar{r}=\operatorname{ker} r=\mathcal{O}_{E}(-E)$.
By the claim we have
$$\operatorname{ker}\left[\bar{r} \otimes \operatorname{id}: \Omega_{V}(\log F) \otimes \mathcal{O}_{E}(E) \rightarrow \Omega_{E} \otimes \mathcal{O}_{E}(F+E)\right]=\mathcal{O}_{E}(-E) \otimes \mathcal{O}_{E}(E)=\mathcal{O}_{E} .$$
Hence we have the exact sequence
$$0 \rightarrow H^{0}\left(\mathcal{O}_{E}\right) \rightarrow H^{0}\left(\Omega_{V}(\log F) \otimes \mathcal{O}_{E}(E)\right) \rightarrow H^{0}(\operatorname{im}(\bar{r} \otimes \mathrm{id})) .$$
Since $H^{0}(\operatorname{im}(\bar{r} \otimes \mathrm{id})) \subset H^{0}\left(\Omega_{E} \otimes \mathcal{O}_{E}(F+E)\right)=0$, the result follows. \(\square\)

Lemma 3.12. The composition map
$$\gamma \circ d_{1}^{\prime}: H^{0}\left(\mathcal{O}_{F}(E)\right) \rightarrow H^{1}\left(\Omega_{V} \otimes \mathcal{O}_{E}(E)\right)$$
is surjective.
Proof. On the second column in (3.2), we have $h^{0}\left(\Omega_{V} \otimes \mathcal{O}_{E}(E)\right)=1, h^{1}\left(\Omega_{V}\right)=21$, $h^{1}\left(\Omega_{V} \otimes \mathcal{O}_{E}(E)\right)=2$. Hence $h^{1}\left(\Omega_{V}(E)\right)=22$. Since $h^{0}\left(\mathcal{O}_{F}\right)=1$ and $h^{0}\left(\mathcal{O}_{F}(E)\right)=$ 3, it follows from the first and the second columns that $h^{1}\left(\Omega_{V}(\log F)\right)=20$ and $h^{1}\left(\Omega_{V}(\log F)(E)\right)=19$. Therefore, on the third column, we have $h^{1}\left(\Omega_{V}(\log F) \otimes\right.$ $\left.\mathcal{O}_{E}(E)\right)=0$ because $h^{0}\left(\Omega_{V}(\log F) \otimes \mathcal{O}_{E}(E)\right)=1$ by Lemma 3.11. Hence $\beta_{2}$ is surjective.

Note that $H^{0}\left(\mathcal{O}_{F}\right) \subseteq \beta_{1}\left(H^{1}\left(\Omega_{V}\right)\right) \cap \operatorname{ker} \alpha_{2}$ in $H^{1}\left(\Omega_{V}(E)\right)$. On the other hand, since $\alpha_{1}$ and $\beta_{2}$ are surjective, we have
$$\left(\alpha_{2} \circ \beta_{1}\right)\left(H^{1}\left(\Omega_{V}\right)\right)=\left(\beta_{2} \circ \alpha_{1}\right)\left(H^{1}\left(\Omega_{V}\right)\right)=H^{1}\left(\Omega_{V}(\log F)(E)\right) .$$
Therefore $\operatorname{dim}\left[\beta_{1}\left(H^{1}\left(\Omega_{V}\right)\right) \cap \operatorname{ker} \alpha_{2}\right]=1$; hence $H^{0}\left(\mathcal{O}_{F}\right)=\beta_{1}\left(H^{1}\left(\Omega_{V}\right)\right) \cap \operatorname{ker} \alpha_{2}$ in $H^{1}\left(\Omega_{V}(E)\right)$. Thus
$$\operatorname{dim}\left[\beta_{1}\left(H^{1}\left(\Omega_{V}\right)\right) \cap H^{0}\left(\mathcal{O}_{F}(E)\right)\right]=1 .$$
Since $\operatorname{ker} \gamma=\operatorname{im} \beta_{1}$, we have $\operatorname{dim}\left[\operatorname{ker} \gamma \cap H^{0}\left(\mathcal{O}_{F}(E)\right)\right]=1$; hence the composition $\gamma \circ d_{1}^{\prime}$ is surjective because $h^{0}\left(\mathcal{O}_{F}(E)\right)=3$ but $h^{1}\left(\Omega_{V} \otimes \mathcal{O}_{E}(E)\right)=2$. \(\square\)

Proof of Proposition 3.8. Set $\mathbb{K}=H^{0}\left(\Omega_{V}(\log (D+S+F))(E)\right)$. We want to show that $\mathbb{K}=0$. Consider the commutative diagram
![](https://cdn.mathpix.com/cropped/9ee2462a-e4a3-493e-91b6-73cb6d621727-12.jpg?height=632&width=1055&top_left_y=509&top_left_x=535)

Let $\left\{1, v_{1}, v_{2}\right\}$ be a basis for $H^{0}\left(\mathcal{O}_{F}(E)\right)$, where 1 is a basis for $H^{0}\left(\mathcal{O}_{F}\right) \cong \mathbb{C}$. By Lemma 3.12 the images $\gamma \circ d_{1}\left(v_{1}\right)$ and $\gamma \circ d_{1}\left(v_{2}\right)$ span $H^{1}\left(\Omega_{V} \otimes \mathcal{O}_{E}(E)\right)$. Therefore they are linearly independent in $H^{1}\left(\Omega_{V}(E)\right)$ and they are not contained in the kernel of the map $\gamma$. On the other hand
$$\bigoplus_{i=1}^{6} H^{0}\left(\mathcal{O}_{D_{i}}\right) \oplus \bigoplus_{i=1}^{3} H^{0}\left(\mathcal{O}_{S_{i}}\right) \oplus H^{0}\left(\mathcal{O}_{F}\right) \subset \operatorname{ker} \gamma .$$
Therefore the map $d_{1}$ is injective; hence $\mathbb{K}=\operatorname{ker} d_{1}=0$. \(\square\)
4. Simply connected surfaces with $p_{g}=1, q=0$, and $1 \leq K^{2} \leq 6$

In this section we construct various examples of simply connected minimal surfaces of general type with $p_{g}=1, q=0$ and $1 \leq K^{2} \leq 6$. Since all the proofs are basically the same as the case of the main construction, we describe only complex surfaces $Z$ which make it possible to get singular surfaces $X$ with permissible singularities.
4.1. An example with $K^{2}=1$. Let $Y$ be the K3 surface described in Section 2. We blow up the surface $Y$ totally three times at the three marked points ●; Figure 7(A). We then get a surface $Z$; Figure 7(B). There exist two disjoint linear chains of $\mathbb{C P}^{1}$ 's in $Z$ :
$$\stackrel{-}{\circ}^{-3}-\stackrel{-}{\circ}^{-2}-\stackrel{-}{\circ}^{-2}-\stackrel{-3}{\circ}^{-2}, \quad \stackrel{-}{\circ}^{-5}-\stackrel{-3}{\circ}^{.}$$
Remark. According to Catanese [3], all minimal surfaces of general type with $p_{g}=1$ and $K^{2}=1$ are diffeomorphic and simply connected. Hence the example above is automatically simply connected. However we can prove the simply connectedness directly by using similar techniques - rational blow-down surgery, Milnor fiber theory, and Van-Kampen Theorem - in Y. Lee and J. Park [13] and the authors [19, 20 .

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/9ee2462a-e4a3-493e-91b6-73cb6d621727-13.jpg?height=404&width=782&top_left_y=425&top_left_x=670}
\captionsetup{labelformat=empty}
\caption{Figure 7. An example with $K^{2}=1$}
\end{figure}
4.2. An example with $K^{2}=3$. Let $A, L_{i}(i=1,2,3)$ be lines on the projective plane $\mathbb{C P}^{2}$ and $B$ a nonsingular conic on $\mathbb{C P}^{2}$ which intersect as in Figure 8(A). Consider a pencil of cubics generated by the two cubics $A+B$ and $L_{1}+L_{2}+L_{3}$. Blow up the five base points ● of the pencil of cubics including infinitely near base-points at each point. Then we obtain a rational elliptic surface $E(1)$ with an $I_{6}$-singular fiber, $I_{3}$-singular fiber, three nodal singular fibers, and five sections which intersect as in Figure 8(B), where we omit one nodal singular fiber and one section which are not used in the following construction.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/9ee2462a-e4a3-493e-91b6-73cb6d621727-13.jpg?height=417&width=958&top_left_y=1366&top_left_x=584}
\captionsetup{labelformat=empty}
\caption{Figure 8. A rational elliptic surface $E(1)$ for $K^{2}=3$}
\end{figure}

Let $Y$ be a double cover of the rational elliptic surface $E(1)$ branched along two general fibers. Then $Y$ is an elliptic K3 surface with two $I_{6}$-singular fibers, two $I_{3}$-singular fibers, six nodal singular fibers, and five sections. We use only two $I_{6}$ singular fibers, one $I_{3}$-singular fibers, one nodal singular fibers, and four sections; Figure 9 (A).

We blow up the surface $Y$ six times at the six marked points ● and twice at the marked point $\odot$. We then get a surface $Z$; Figure 9 (B). There exist four disjoint linear chains of $\mathbb{C P}^{1}$ 's in $Z$ :
$$\stackrel{-5}{\circ}^{-\circ^{-2}}-\stackrel{-6}{\circ}^{-2}-\stackrel{-2}{\circ}^{-2}, \quad \stackrel{-2}{\circ}^{-\circ^{-3}}, \stackrel{-4}{\circ}^{-2}, \quad \text { ० }^{-3}-\text { о }^{-4}, \quad \begin{aligned}
& -3 \\
& \circ
\end{aligned}-\text { о }^{-3} .$$
4.3. An example with $K^{2}=4$. Let $A$ and $L$ be lines on the projective plane $\mathbb{C P}^{2}$ and $B$ a nonsingular conic on $\mathbb{C P}^{2}$ which intersect as in Figure 10(A). Consider a

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/9ee2462a-e4a3-493e-91b6-73cb6d621727-14.jpg?height=812&width=866&top_left_y=428&top_left_x=629}
\captionsetup{labelformat=empty}
\caption{Figure 9. An example with $K^{2}=3$}
\end{figure}
pencil of cubics generated by the two cubics $A+B$ and $3 L$. Blow up the three base points of the pencil of cubics including infinitely near base-points at each point. Then we obtain a rational elliptic surface $E(1)$ with an $\tilde{E}_{6}$-singular fiber, an $I_{2}$-singular fiber, two nodal singular fibers, and three sections; Figure 10(B).

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/9ee2462a-e4a3-493e-91b6-73cb6d621727-14.jpg?height=400&width=836&top_left_y=1674&top_left_x=642}
\captionsetup{labelformat=empty}
\caption{Figure 10. A rational elliptic surface $E(1)$ for $K^{2}=4$}
\end{figure}

Let $Y$ be a double cover of the rational elliptic surface $E(1)$ branched along two general fibers. Then $Y$ is an elliptic K3 surface with two $\tilde{E}_{6}$-singular fibers, two $I_{2}$-singular fibers, four nodal singular fibers, and three sections. We use only two $\tilde{E}_{6}$-singular fibers, two $I_{2}$-singular fibers, one nodal singular fibers, and three sections; Figure 11(A).

We blow up the surface $Y$ totally 16 times at the marked points．We then get a surface $Z$ ；Figure 11（B）．There exist six disjoint linear chains of $\mathbb{C P}^{1}$＇s in $Z$ ：
$$\begin{gathered}
\stackrel{-2}{\circ}-\stackrel{-10}{\circ}-\stackrel{-2}{\circ}-\stackrel{-2}{\circ}^{-2}-\stackrel{-2}{\circ}-\stackrel{-2}{\circ}-\stackrel{-3}{\circ}, \quad{ }_{\circ}^{-2}-\stackrel{-8}{\circ}-\stackrel{-2}{\circ}-\stackrel{-2}{\circ}^{-2}-\stackrel{-3}{\circ}^{-3} \\
{ }^{-3}-\stackrel{-2}{\circ}^{-2}-\stackrel{-3}{\circ}^{-3}, \quad \stackrel{-2}{\circ}^{-5}-\stackrel{-3}{\circ}^{-4}, \quad{ }^{-4} .
\end{gathered}$$

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/9ee2462a-e4a3-493e-91b6-73cb6d621727-15.jpg?height=791&width=629&top_left_y=700&top_left_x=746}
\captionsetup{labelformat=empty}
\caption{Figure 11．An example with $K^{2}=4$}
\end{figure}

4．4．An example with $K^{2}=5$ ．Let $Y$ be the K3 surface used in Section 2．1．We use only two $I_{7}$－singular fibers，two $I_{2}$－singular fibers，one nodal singular fibers，and three sections；Figure 12（A）．

We blow up the surface $Y$ totally 15 times at the marked points．We then get a surface $Z$ ；Figure 12（B）．There exist seven disjoint linear chains of $\mathbb{C P}^{1}$＇s in $Z$ ：
$$\begin{gathered}
\text { o }^{-2}-\text { o }^{-3}-\text { o }^{-8}-\text { o }^{-2}-\text { o }^{-2}-\text { o }^{-3}-\text { o }^{-7}, \quad \text { o }^{-2}-\text { o }^{-2}-\text { o }^{-2} \\
\text { 一 }^{3}-\text { o }^{-5}-\text { o }^{-3}, \quad \text { 一 }^{-3}-\text { o }^{-3}, \quad \text { о }, \quad \text { 一 } 4, \quad \text { 一 } 4
\end{gathered}$$

4．5．An example with $K^{2}=6$ ．Let $Y$ be the elliptic K3 surface described in Section 2．We use only two $I_{8}$－singular fibers，two $I_{2}$－singular fibers，one nodal singular fibers，and three sections；Figure 13（A）．

We blow up the surface $Y$ totally 18 times at the marked points．We then get a surface $Z$ ；Figure 13（B）．There exist five disjoint linear chains of $\mathbb{C P}^{1}$＇s in $Z$ ：
$$\begin{aligned}
& \stackrel{-2}{\circ}^{-2} \stackrel{-}{\circ}^{-3}-\stackrel{-9}{\circ}-\stackrel{-2}{\circ}-\stackrel{-2}{\circ}^{-2}-\stackrel{-2}{\circ}-\stackrel{-3}{\circ}^{-} \stackrel{-4}{\circ}^{,} \\
& \stackrel{-2}{\circ}_{\circ}^{-3}-\stackrel{-7}{\circ}^{-2} \stackrel{-}{\circ}_{\circ}-\stackrel{-3}{\circ}-\stackrel{-3}{\circ}, \quad \circ^{7}-\circ^{-2}-\circ^{-2}-\circ^{-2}, \\
& \stackrel{-4}{\circ^{-4}} \text { - } \stackrel{-3}{\circ} \text { - } \stackrel{-2}{\circ}, \quad \stackrel{-4}{\circ} .
\end{aligned}$$

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/9ee2462a-e4a3-493e-91b6-73cb6d621727-16.jpg?height=827&width=784&top_left_y=430&top_left_x=670}
\captionsetup{labelformat=empty}
\caption{Figure 12. An example with $K^{2}=5$}
\end{figure}

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/9ee2462a-e4a3-493e-91b6-73cb6d621727-16.jpg?height=829&width=765&top_left_y=1414&top_left_x=679}
\captionsetup{labelformat=empty}
\caption{Figure 13. An example with $K^{2}=6$}
\end{figure}

\section*{5. A SIMPLY CONNECTED SURFACE WITH $p_{g}=1, q=0$, AND $K^{2}=8$}

In this section we construct a simply connected minimal complex surface of general type with $p_{g}=1, q=0$, and $K^{2}=8$.

According to Kondo [9], there is an Enriques surface $Y$ with an elliptic fibration over $\mathbb{C P}^{1}$ which has a $I_{9}$-singular fiber, a nodal singular fiber $F$, and two bisections $S_{1}$ and $S_{2}$; Figure 14. Again by Kondo [9], there is an unbranched double covering $\pi: \bar{Y} \rightarrow Y$ of $Y$ where $\bar{Y}$ is an elliptic K3 surface which has two $I_{9}$-singular fiber, two nodal singular fiber $\bar{F}_{1}$ and $\bar{F}_{2}$, and four sections $\bar{S}_{1}, \ldots, \bar{S}_{4}$ such that $\pi\left(\bar{F}_{1}\right)=\pi\left(\bar{F}_{2}\right)=F, \pi\left(\bar{S}_{1}\right)=\pi\left(\bar{S}_{3}\right)=S_{1}$, and $\pi\left(\bar{S}_{2}\right)=\pi\left(\bar{S}_{4}\right)=S_{2}$; Figure 15.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/9ee2462a-e4a3-493e-91b6-73cb6d621727-17.jpg?height=505&width=602&top_left_y=892&top_left_x=761}
\captionsetup{labelformat=empty}
\caption{Figure 14. An Enriques surface $Y$}
\end{figure}

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/9ee2462a-e4a3-493e-91b6-73cb6d621727-17.jpg?height=511&width=1152&top_left_y=1654&top_left_x=486}
\captionsetup{labelformat=empty}
\caption{Figure 15. A K3 surface $\bar{Y}$}
\end{figure}

We blow up the K3 surface $\bar{Y}$ totally 30 times at the marked points ● and ⊙. We then get a surface $\bar{Z}=\bar{Y} \sharp 30 \overline{\mathbb{C P}}^{2}$; Figure 16. There exist four disjoint linear
chains of $\mathbb{C P}^{1}$ 's in $\bar{Z}$ :
$$\begin{aligned}
& C_{19,6}: \stackrel{-2}{\circ}^{-2} \stackrel{-}{\circ}^{-9} \text { - } \stackrel{-2}{\circ} \text { - } \stackrel{-2}{\circ} \text { - } \stackrel{-2}{\circ} \text { - } \stackrel{-2}{\circ} \text { - } \stackrel{-4}{\circ} \\
& C_{19,6}: \stackrel{-2}{\circ}^{-} \stackrel{-2}{\circ}^{-9} \text { - } \stackrel{-2}{\circ} \text { - } \stackrel{-2}{\circ} \text { - } \stackrel{-2}{\circ} \text { - } \stackrel{-2}{\circ} \text { - } \stackrel{-4}{\circ} \\
& C_{73,50}: \stackrel{-2}{\circ}^{-\circ^{-2}} \text { - } \stackrel{-7}{\text { ∘ }} \text { - } \stackrel{-6}{\text { о }} \text { - } \stackrel{-2}{\text { о }} \text { - } \stackrel{-3}{\text { о }} \text { - } \stackrel{-2}{\text { о }} \text { - } \stackrel{-2}{\text { о }} \text { - } \stackrel{-2}{\text { о }} \text { - } \stackrel{-2}{\text { о }} \text { - } \stackrel{-4}{\text { о }}
\end{aligned}$$

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/9ee2462a-e4a3-493e-91b6-73cb6d621727-18.jpg?height=619&width=1255&top_left_y=791&top_left_x=434}
\captionsetup{labelformat=empty}
\caption{Figure 16. A surface $\bar{Z}=\bar{Y} \sharp 30 \overline{\mathbb{C P}}^{2}$}
\end{figure}

We contract these four chains of $\mathbb{C P}^{1}$ 's from the surface $\bar{Z}$ so that it produces a normal projective surface $\bar{X}$ with four singular points of class $T$. It is not difficult to show that $H^{2}\left(X, \mathcal{T}_{X}\right) \neq 0$.

Theorem 5.1. The singular surface $\bar{X}$ has a global $\mathbb{Q}$-Gorenstein smoothing. A general fiber $\bar{X}_{t}$ of the smoothing of $\bar{X}$ is a simply connected minimal complex surface of general type with $p_{g}=1, q=0$, and $K^{2}=8$.

In order to prove Theorem 5.1, we apply the following proposition.
Proposition 5.2 (Y. Lee and J. Park [12]). Let $V$ be a normal projective surface with singularities of class $T$. Assume that a cyclic group $G$ acts on $X$ such that
\begin{itemize}
\item[1.] $W=V / G$ is a normal projective surface with singularities of class $T$,
\item[2.] $p_{g}(W)=q(W)=0$,
\item[3.] $W$ has a $\mathbb{Q}$-Gorenstein smoothing,
\item[4.] the map $\sigma: V \rightarrow W$ induced by a cyclic covering is flat, and the branch locus $D$ (resp. the ramification locus) of the map $\sigma: V \rightarrow W$ is a nonsingular curve lying outside the singular locus of $W$ (resp. of $V$ ), and
\item[5.] $H^{1}\left(W, \mathcal{O}_{W}(D)\right)=0$.
\end{itemize}

Then there exists a $\mathbb{Q}$-Gorenstein smoothing of $V$ that is compatible with a $\mathbb{Q}$ -Gorenstein smoothing of $W$. Furthermore the cyclic covering extends to the $\mathbb{Q}$ -Gorenstein smoothing.

We now construct an unramified double covering from the singular surface $\bar{X}$ to another singular surface. We begin with the Enriques surface $Y$ in Figure 14. We blow up totally 15 times at the marked points ● and ⊙; Figure 17. We then get a surface $Z=Y \sharp 15 \overline{\mathbb{C P}}^{2}$; Figure 18. There exist two disjoint linear chains of $\mathbb{C P}^{1}$ 's in $Z$ :
$$\begin{aligned}
& C_{19,6}: \stackrel{-2}{\circ}^{-} \stackrel{-2}{\circ}^{-9}-\stackrel{-2}{\circ}^{-2}-\stackrel{\circ}{\circ}^{-2}-\stackrel{\circ}{\circ}^{-} \stackrel{-}{\circ}^{-4} \\
& C_{73,50}: \stackrel{-2}{\circ}^{-2}-\stackrel{-7}{\circ}^{-6}-\stackrel{-2}{\circ}^{-3}-\stackrel{-}{\circ}^{-2}-\stackrel{-2}{\circ}^{-2}-\stackrel{-}{\circ}_{\circ}-\stackrel{-4}{\circ}^{-4}
\end{aligned}$$

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/9ee2462a-e4a3-493e-91b6-73cb6d621727-19.jpg?height=505&width=602&top_left_y=801&top_left_x=761}
\captionsetup{labelformat=empty}
\caption{Figure 17. An Enriques surface $Y$ with marked points}
\end{figure}

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/9ee2462a-e4a3-493e-91b6-73cb6d621727-19.jpg?height=554&width=636&top_left_y=1448&top_left_x=743}
\captionsetup{labelformat=empty}
\caption{Figure 18. A surface $Z=Y \sharp 15 \overline{\mathbb{C P}}^{2}$}
\end{figure}

We contract the two chains of $\mathbb{C P}^{1}$ 's from the surface $Z$ so that it produces a normal projective surface $X$ with two singular points class $T$. It is clear that there is an unbranched double covering $\bar{\pi}: \bar{X} \rightarrow X$. The singular surface $X$ satisfies the third condition of Proposition 5.2.

Proposition 5.3 (H. Park [16]). The singular surface $X$ has a global $\mathbb{Q}$-Gorenstein smoothing. A general fiber $X_{t}$ of the smoothing of $X$ is a minimal complex surface of general type with $p_{g}=0, K^{2}=4$, and $\pi_{1}\left(X_{t}\right)=\mathbb{Z} / 2 \mathbb{Z}$.

Proof of Theorem 5.1. It is easy to show that the covering $\bar{\pi}: \bar{X} \rightarrow X$ satisfies all conditions of Proposition 5.2. Therefore the singular surface $\bar{X}$ has a global $\mathbb{Q}$-Gorenstein smoothing. Let $\bar{X}_{t}$ be a general fiber of the smoothing of $\bar{X}$. Since $p_{g}(\bar{X})=1, q(\bar{X})=0$, and $K_{\bar{X}}^{2}=8$, by applying general results of complex surface theory and $\mathbb{Q}$-Gorenstein smoothing theory, one may conclude that a general fiber $\bar{X}_{t}$ is a complex surface of general type with $p_{g}=1, q=0$, and $K^{2}=8$. Furthermore, it is not difficult to show that a general fiber $X_{t}$ is minimal by using a similar technique in Y. Lee and J. Park [13] and the authors [19, 20].

Claim. A general fiber $\bar{X}_{t}$ is simply connected: By Proposition 5.2, there is an induced unbranched double covering $\bar{X}_{t} \rightarrow X_{t}$; hence, a general fiber $\bar{X}_{t}$ is simply connected because $\pi\left(X_{t}\right)=\mathbb{Z} / 2 \mathbb{Z}$ by Proposition 5.3. \(\square\)

\section*{References}
\begin{itemize}
\item[] [1] R. Barlow, A simply connected surface of general type with $p_{g}=0$, Invent. Math. 79 (1985), no. 2, 293-301.
\item[] [2] W. Barth, K. Hulek, C. Peters, A. Van de Ven, Compact complex surfaces, 2nd ed. SpringerVerlag, Berlin, 2004.
\item[] [3] F. Catanese, Surfaces with $K^{2}=p_{g}=1$ and their period mapping, Algebraic geometry (proc. Summer Meeting, Univ. Copenhagen, Copenhagen, 1978), Lecture Notes in Math. 732 (1979), 1-29.
\item[] [4] F. Catanese and O. Debarre, Surfaces with $K^{2}=2, p_{g}=1, q=0$, J. Reine Angew. Math. 395 (1989), 1-55.
\item[] [5] H. Flenner and M. Zaidenberg, $\mathbb{Q}$-acyclic surfaces and their deformations, Contemp. Math. 162 (1994), 143-208.
\item[] [6] R. E. Gompf, A new construction of symplectic manifolds, Ann. of Math. 142 (1995), 527-595.
\item[] [7] R.E. Gompf and A. Stipsicz, 4-manifolds and Kirby calculus, Graduate Studies in Mathematics, 20. American Mathematical Society, 1999.
\item[] [8] J. Kollár and N.I. Shepherd-Barron, Threefolds and deformations of surface singularities, Invent. Math. 91 (1988), 299-338.
\item[] [9] S. Kondo, Enriques surfaces with finite automorphism groups, Japan. J. Math. (N.S.) 12 (1986), no. 2, 191-282.
\item[] [10] V. Kynev, An example of a simply connected surface of general type for which the local Torelli theorem does not hold, C. R. Acad. Bulgare Sci. 30 (1977), no. 3, 323-325.
\item[] [11] Y. Lee and J. Park, A complex surface of general type with $p_{g}=0, K^{2}=2$ and $H_{1}=\mathbb{Z} / 2 \mathbb{Z}$, Math. Res. Lett. 16 (2009), 323-330.
\item[] [12] $\_\_\_\_$, A construction of Horikawa surface via Q-Gorenstein smoothings, arXiv:0708.3319. to appear in Math. Zeit.
\item[] [13] $\_\_\_\_$, A simply connected surface of general type with $p_{g}=0$ and $K^{2}=2$, Invent. Math. 170 (2007), 483-505.
\item[] [14] M. Manetti, Normal degenerations of the complex projective plane, J. Reine Angew. Math. 419 (1991), 89-118.
\item[] [15] B. D. Park, Exotic smooth structures on $3 \mathbb{C P}^{2} \sharp n \overline{\mathbb{C P}}^{2}$, Part II, Proc. Amer. Math. Soc. 128 (2000), 3067-3073.
\item[] [16] H. Park, A complex surface of general type with $p_{g}=0, K^{2}=4$, and $\pi_{1}=\mathbb{Z} / 2 \mathbb{Z}$, arXiv:0910.3476
\item[] [17] J. Park, Exotic smooth structures on $3 \mathbb{C P}^{2} \sharp 8 \overline{\mathbb{C P}}^{2}$, Bull. London Math. Soc. 39 (2007), no. 1, 95-102.
\item[] [18] H. Park, J. Park and D. Shin, A complex surface of general type with $p_{g}=0, K^{2}=3$ and $H_{1}=\mathbb{Z} / 2 \mathbb{Z}$, Bulletin of the Korean Math. Soc. 47 (2010), 1269-1274.
\item[] [19] $\_\_\_\_$, A simply connected surface of general type with $p_{g}=0$ and $K^{2}=3$, Geom. Topol. 13 (2009), no. 2, 743-767.
\item[] [20] $\_\_\_\_$, A simply connected surface of general type with $p_{g}=0$ and $K^{2}=4$, Geom. Topol. 13 (2009), no. 3, 1483-1494.
\end{itemize}
[21] A. Stipsicz and Z. Szabó, Small exotic 4-manifolds with $b_{2}^{+}=3$, Bull. London Math. Soc. 38 (2006), 501-506.
[22] A. Todorov, A construction of surfaces with $p_{g}=1, q=0$ and $2 \leq\left(K^{2}\right) \leq 8$ : Counterexamples of the global Torelli theorem, Invent. Math. 63 (1981), no. 2, 287-304.
[23] R. Torres, On Einstein metrics, normalized Ricci flow and smooth structures on $3 \mathbb{C P}^{2} \sharp k \overline{\mathbb{C P}}^{2}$, arXiv:1009.1160
[24] J. Wahl, Smoothing of normal surface singularities, Topology 20 (1981), 219-246.
School of Mathematics, Korea Institute for Advanced Study, Seoul 130-722, Korea
E-mail address: hspark@kias.re.kr
Department of Mathematical Sciences, Seoul National University, Seoul 151-747, Korea \& Korea Institute for Advanced Study, Seoul 130-722, Korea
E-mail address: jipark@snu.ac.kr
Department of Mathematics, Chungnam National University, Daejeon 305-764, Korea
E-mail address: dsshin@cnu.ac.kr
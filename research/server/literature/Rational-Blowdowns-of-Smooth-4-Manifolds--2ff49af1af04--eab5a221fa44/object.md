# Rational Blowdowns of Smooth 4-Manifolds

- Category: papers
- Identity: arxiv:alg-geom/9505018
- Content status: fulltext_ok

---

---
source_file: alg-geom_9505018.pdf
converter: mathpix
format: mmd
---

\title{
RATIONAL BLOWDOWNS OF SMOOTH 4-MANIFOLDS
}

\author{
RONALD FINTUSHEL AND RONALD J. STERN
}

\section*{1. Introduction}

The invariants of Donaldson and of Seiberg and Witten are powerful tools for studying smooth 4-manifolds. A fundamental problem is to determine procedures which relate smooth 4-manifolds in such a fashion that their effect on both the Donaldson and Seiberg-Witten invariants can be computed. The purpose of this paper is to initiate this study by introducing a surgical procedure, called rational blowdown, and to determine how this procedure affects these two sets of invariants. The technique of rationally blowing down and its effect on the the Donaldson invariant were first announced at the 1993 Georgia International Topology Conference and represents the bulk of the mathematics in this paper. We fell upon this surgical procedure while we were investigating the behavior of the Donaldson invariant in the presence of embedded spheres and while investigating methods for producing a topological logarithmic transform. As it turns out, this rational blowdown procedure allows for the full computation of the Donaldson series (and Seiberg-Witten invariants) of all elliptic surfaces with $p_{g} \geq 1$ with the only input being the Donaldson invariants of the Kummer surface; in particular this computation shows that the Donaldson series of elliptic surfaces is that conjectured by Kronheimer and Mrowka in [KM1]:

Theorem . Let $E(n ; p, q)$ be the simply connected elliptic surface with $p_{g}=n-1$ and with multiple fibers of relatively prime orders $p, q \geq 1$. Then
$$\mathbf{D}_{E(n ; p, q)}=\exp (Q / 2) \frac{\sinh ^{n}(f)}{\sinh \left(f_{p}\right) \sinh \left(f_{q}\right)} .$$
This theorem gives another, more topological, proof of the diffeomorphism classification of elliptic surfaces ([Br, MM2, MO, Fr]). This procedure also goes further and routinely computes the Donaldson series (and Seiberg-Witten invariants) for many 4-manifolds, some of which are complex surfaces, and for most of the currently known examples which are not even homotopy equivalent to complex surfaces.

The ideas presented in this paper have led to rather easy proofs of the blowup formulas for the Donaldson invariants for arbitrary smooth 4-manifolds [FS2] and alternate proofs and generalizations [FS3] of some of the results announced by Kronheimer and Mrowka ([KM1],[KM2]). While we chose

\footnotetext{
The first author was partially supported NSF Grant DMS9401032 and the second author by NSF Grant DMS9302526.
}
to first write up these later results, another major delay in the appearance of this paper was the introduction of the Seiberg-Witten invariants.

From the beginning, Witten has conjectured how the Seiberg-Witten invariants and the Donaldson invariants determine each other (cf. [Wn]). Some progress in proving this relationship has been announced by V. Pidstrigach and A. Tyurin. Our techniques verify Witten's conjecture for elliptic surfaces and for a large class of manifolds obtained from them by rational blowdowns. (See §8.)

Here is an outline of the paper: In §2 we introduce the concept of a rational blowdown and discuss relevant topological issues. Our main analytical result, Theorem 5.1, gives a universal formula which relates the Donaldson invariants of a manifold with those of its rational blowdown. Three examples of the effect of a rational blowdown are given in §3 and these examples are used in subsequent sections to compute the universal quantities given in Theorem 5.1. In §4 we give the fundamental definitions of the Donaldson series, and §5 presents our key analytical results. Here we shall take advantage of our later results and techniques ([FS2],[FS3]) to streamline our earlier arguments. In particular, we will utilize the " pullback — pushforward " point of view introduced and developed by Cliff Taubes in [T1, T2, T3, T4] (or, alternatively the thesis of Wieczorek [Wk]) to prove our basic universal formula (Theorem 5.1). Under the assumption of simple type, this universal formula takes on a particularly simple form (Theorem 5.11). Starting with the computations of the Donaldson series for elliptic surfaces without multiple fibers given in [KM1],[FS3] and [Li], we apply Theorem 5.11 and some of the examples presented in §3 to compute the Donaldson series of the elliptic surfaces with multiple fibers in §6. Under the assumption of simple type and the additional assumption that the configuration of curves that is blown down is 'taut', Theorem 5.11 yields a very simple formula relating the basic classes of $X$ with those of its rational blowdowns (cf. Theorem 7.1). This, as well as applications to the computations of the Donaldson series of other manifolds, is discussed in §7. Theorem 5.11 has a straightforward analogue relating the Seiberg-Witten invariants of $X$ and those of its rational blowdowns. We conclude this paper with a statement and proof of this relationship in §8.

\section*{2. The Topology of Rational Blowdowns}

In this section we define what is meant by a rational blowdown. Let $C_{p}$ denote the simply-connected smooth 4-manifold obtained by plumbing the $(p-1)$ disk bundles over the 2-sphere according to the linear diagram
![](https://cdn.mathpix.com/cropped/0b688b97-8445-47da-9e28-b2fc1fdb2772-02.jpg?height=116&width=466&top_left_y=2166&top_left_x=848)
Here, each node denotes a disk bundle over $S^{2}$ with Euler class indicated by the label; an interval indicates that the endpoint disk bundles are plumbed, i.e identified fiber to base over the upper
hemisphere of each $S^{2}$. Label the homology classes represented by the spheres in $C_{p}$ by $u_{1}, \ldots, u_{p-1}$ so that the self-intersections are $u_{p-1}^{2}=-(p+2)$ and, for $j=1, \ldots, p-2, u_{j}^{2}=-2$. Further, orient the spheres so that $u_{j} \cdot u_{j+1}=+1$. Then $C_{p}$ is a 4-manifold with negative definite intersection form and with boundary the lens space $L\left(p^{2}, p-1\right)$.

Lemma 2.1. The lens space $L\left(p^{2}, p-1\right)=\partial C_{p}$ bounds a rational ball $B_{p}$ with $\pi_{1}\left(B_{p}\right)=\mathbf{Z}_{p}$ and a surjective inclusion induced homomorphism $\pi_{1}\left(L\left(p^{2}, p-1\right)=\mathbf{Z}_{p^{2}} \rightarrow \pi_{1}\left(B_{p}\right)\right.$.

Proof. There are several constructions of $B_{p}$; we present three here. The first construction is perhaps amenable to showing that if the configuration of spheres $C_{p}$ are symplectically embedded in a symplectic 4-manifold $X$, then the rational blowdown $X_{p}$ is also symplectic (cf. [G2]). For this construction let $\mathbf{F}_{p-1}, p \geq 2$, be the simply connected ruled surface whose negative section $s_{-}$has square $-(p-1)$. Let $s_{+}$be a positive section (with square $(p-1)$ ) and $f$ a fiber. Then the homology classes $s_{+}+f$ and $s_{-}$are represented by embedded 2-spheres which intersect each other once and have intersection matrix
$$\left(\begin{array}{cc}
p+1 & 1 \\
1 & -(p-1)
\end{array}\right)$$
It follows that the regular neighborhood of this pair of 2-spheres has boundary $L\left(p^{2}, p-1\right)$. Its complement in $\mathbf{F}_{p-1}$ is the rational ball $B_{p}$.

The second construction begins with the configuration of $(p-1) 2$-spheres
![](https://cdn.mathpix.com/cropped/0b688b97-8445-47da-9e28-b2fc1fdb2772-03.jpg?height=74&width=426&top_left_y=1480&top_left_x=870)
in $\#(p-1) \mathbf{C P}^{2}$ where the spheres (from left to right) represent
$$2 h_{1}-h_{2}+\cdots-h_{p-1}, h_{1}+h_{2}, h_{2}+h_{3}, \ldots, h_{p-2}+h_{p-1}$$
where $h_{i}$ is the hyperplane class in the $i$ th copy of $\mathbf{C P}^{2}$. The boundary of the regular neighborhood of the configuration is $L\left(p^{2}, p-1\right)$ and the classes of the configuration span $H_{2}\left(\mathbf{C P}{ }^{2} ; \mathbf{Q}\right)$. The complement is the rational ball $B_{p}$.

The third construction is due to Casson and Harer [CH]. It utilizes the fact that any lens space is the double cover of $S^{3}$ branched over a 2-bridge knot. The 2-bridge knot $K\left((1-p) / p^{2}\right)$ corresponding to $L\left(p^{2}, 1-p\right)$ is slice, and $B_{p}$ is the double cover of the 4-ball branched over the slice disk. \(\square\)

That all these constructions produce the same rational ball $B_{p}$ is an exercise in Kirby calculus. However, for the purposes of this paper, it is the third construction that is the most useful, since it allows us to quickly prove:

Corollary 2.2. Each diffeomorphism of $L\left(p^{2}, 1-p\right)$ extends over the rational ball $B_{p}$.

Proof. It is a theorem of Bonahon [Bo] that $\pi_{0}\left(\operatorname{Diff}\left(L\left(p^{2}, 1-p\right)\right)=\mathbf{Z}_{\mathbf{2}}\right.$, and is generated by the deck transformation $\tau$ of the double branched cover of $K\left((1-p) / p^{2}\right)$. The extension of $\tau$ to $B_{p}$ is given by the deck transformation of the double cover of $B^{4}$ branched over the slice disk. \(\square\)

Suppose that $C_{p}$ embeds in a closed smooth 4-manifold $X$. Then let $X_{p}$ be the smooth 4-manifold obtained by removing the interior of $C_{p}$ and replacing it with $B_{p}$. Corollary 2.2 implies that this construction is well-defined. We call this procedure a rational blowdown and say that $X_{p}$ is obtained by rationally blowing down $X$. Note that $b^{+}(X)=b^{+}\left(X_{p}\right)$ so that rationally blowing down increases the signature while keeping $b^{+}$fixed. An algebro-geometric analogue of rationally blowing down is discussed in [KSB].

With respect to the basis $\left\{u_{1}, \ldots, u_{p-1}\right\}$ for $H_{2}\left(C_{p}\right)$, the plumbing matrix for $C_{p}$ is given by the symmetric $(p-1) \times(p-1)$ matrix
$$P=\left(\begin{array}{ccccccc}
-2 & 1 & & & & & \\
1 & -2 & 1 & & & 0 & \\
0 & 1 & -2 & 1 & & & \\
& & & & \ddots & & \\
& 0 & & & & -2 & 1 \\
& & & & & 1 & -(p+2)
\end{array}\right)$$
with inverse given by $\left(P^{-1}\right)_{i, j}=-j+\frac{(i j)(p+1)}{p^{2}}$ for $j \leq i$.
Let $Q: H_{2}\left(C_{p}, \partial C_{p} ; \mathbf{Z}\right) \times H_{2}\left(C_{p} ; \mathbf{Z}\right) \rightarrow \mathbf{Z}$ be the (relative) intersection form of $C_{p}$ and let $\left\{\gamma_{1}, \ldots, \gamma_{p-1}\right\}$ be the basis of $H_{2}\left(C_{p}, \partial C_{p} ; \mathbf{Z}\right)$ dual to the basis $\left\{u_{1}, \ldots, u_{p-1}\right\}$ of $H_{2}\left(C_{p} ; \mathbf{Z}\right)$ with respect to $Q$. I.e. $\gamma_{k} \cdot u_{\ell}=\delta_{k \ell}$. Let $i_{*}: H_{2}\left(C_{p} ; \mathbf{Z}\right) \rightarrow H_{2}\left(C_{p}, \partial C_{p} ; \mathbf{Z}\right)$ be the inclusion induced homomorphism. Then the intersection form of $H_{2}\left(C_{p}, \partial C_{p} ; \mathbf{Q}\right)$ is defined by
$$\gamma_{k} \cdot \gamma_{\ell}=\frac{1}{p^{2}} \gamma_{k} \cdot \gamma_{\ell}^{\prime}$$
where $\gamma_{\ell}^{\prime} \in H_{2}\left(C_{p} ; \mathbf{Z}\right)$ is chosen such that $i_{*}\left(\gamma_{\ell}^{\prime}\right)=p^{2} \gamma_{\ell}$. Since $\gamma_{\ell}^{\prime}=p^{2} P^{-1}\left(\gamma_{\ell}\right)$, the intersection matrix for $H_{2}\left(C_{p}, \partial C_{p} ; \mathbf{Q}\right)$ is $\left(\gamma_{k} \cdot \gamma_{\ell}\right)=P^{-1}$. Note also that using the sequence
$$0 \rightarrow H_{2}\left(C_{p} ; \mathbf{Z}\right) \xrightarrow{P} H_{2}\left(C_{p}, \partial C_{p} ; \mathbf{Z}\right) \xrightarrow{\partial} H_{1}\left(L\left(p^{2}, 1-p ; \mathbf{Z}\right) \rightarrow 0\right.$$
we may identify $H_{1}\left(L\left(p^{2}, 1-p ; \mathbf{Z}\right)\right.$ with $\mathbf{Z}_{p^{2}}$ so that $\partial$ is given by $\partial\left(\gamma_{j}\right)=j$.
There is an alternative choice of dual bases for $H_{2}\left(C_{p} ; \mathbf{Z}\right)$ and $H_{2}\left(C_{p}, \partial C_{p} ; \mathbf{Z}\right)$ that we shall find useful because of its symmetry. Define the basis $\left\{v_{i}\right\}$ of $H_{2}\left(C_{p} ; \mathbf{Z}\right)$ by
$$v_{i}=u_{p-1}+\cdots+u_{i}, \quad u_{j}=v_{j}-v_{j+1}$$
so $v_{i}^{2}=-(p+2)$ for each $i$, and if $i \neq j$ then $v_{i} \cdot v_{j}=-(p+1)$. The dual basis $\left\{\delta_{i}\right\}$ of $H_{2}\left(C_{p}, \partial C_{p} ; \mathbf{Z}\right)$ is given in terms of $\left\{\gamma_{i}\right\}$ by
$$\begin{aligned}
\delta_{i} & =\gamma_{i}-\gamma_{i-1}, \quad i \neq 1 \\
\delta_{1} & =\gamma_{1}
\end{aligned}$$

Then
$$\begin{aligned}
\delta_{i} \cdot \delta_{j} & =\frac{(p+1)}{p^{2}}, \quad i \neq j \\
\delta_{i}^{2} & =-\frac{\left(p^{2}-p-1\right)}{p^{2}}
\end{aligned}$$
and
$$\partial\left(\sum a_{i} \delta_{i}\right)=\sum a_{i} .$$

Let the character variety of $S O(3)$ representations of $\pi_{1}\left(L\left(p^{2}, 1-p\right)\right)$ mod conjugacy be denoted by $\chi_{S O(3)}\left(L\left(p^{2}, 1-p\right)\right)$, and identify $\pi_{1}\left(L\left(p^{2}, 1-p\right)\right)$ with $\mathbf{Z}_{p^{2}}$ as above. Then we have an identification
$$\chi_{S O(3)}\left(L\left(p^{2}, 1-p\right)\right) \cong \mathbf{Z}_{p^{2}} /\{ \pm 1\} \cong H_{1}\left(L\left(p^{2}, 1-p\right) ; \mathbf{Z}\right) /\{ \pm 1\} .$$
Let $\eta$ be the generator of $\chi_{S O(3)}\left(L\left(p^{2}, 1-p\right)\right)$ satisfying
$$\eta(1)=\left(\begin{array}{ccc}
\cos \left(2 \pi i / p^{2}\right) & \sin \left(2 \pi i / p^{2}\right) & 0 \\
-\sin \left(2 \pi i / p^{2}\right) & \cos \left(2 \pi i / p^{2}\right) & 0 \\
0 & 0 & 1
\end{array}\right)$$
Let $e \in H_{2}\left(C_{p}, \partial C_{p} ; \mathbf{Z}\right)$; so $\partial e$ is some $n_{e} \in \mathbf{Z}_{p^{2}}$. Since $b^{+}\left(C_{p}\right)=0, e$ defines an anti-self-dual connection $A_{e}$ on the complex line bundle $L_{e}$ over $C_{p}$ whose first chern class is the Poincaré dual of $e$. Throughout this paper we shall identify $H_{2}\left(C_{p}, \partial C_{p} ; \mathbf{Z}\right) \equiv H^{2}\left(C_{p} ; \mathbf{Z}\right)$; so we may write $c_{1}\left(L_{e}\right)=e$. Consider $C_{p}$ with a metric which gives a collar $L\left(p^{2}, 1-p\right) \times[0, \infty)$. The connection $A_{e}$ has an asymptotic value as $t \rightarrow \infty$, and this is a flat connection on $L\left(p^{2}, 1-p\right)$. Dividing out by gauge equivalence, we obtain the element $\partial A_{e}=\eta^{n_{e}} \in \chi_{S O(3)}\left(L\left(p^{2}, 1-p\right)\right)$. For later use, we define
$$\partial^{\prime}: H_{2}\left(C_{p}, \partial C_{p} ; \mathbf{Z}\right) \rightarrow \chi_{S O(3)}\left(L\left(p^{2}, p-1\right)\right)=\mathbf{Z}_{p^{2}} /\{ \pm 1\}=\{0,1, \ldots,[p / 2]\}$$
by $\partial^{\prime}(e)=\bar{n}_{e}$, the equivalence class of $\partial e$.

\section*{3. Examples of Rational Blowdowns}

In this section we present four examples of the effect of rational blowdowns. These are essential for our later computations.

Example 1. Logarithmic transform as a rational blowdown
This first example, whose discovery motivated our interest in this procedure, shows that a logarithmic transform of order $p$ can be obtained by a sequence of $(p-1)$ blowups (i.e. connect sum with $(p-1)$ copies of $\overline{\mathbf{C P}}^{2}$ ) and one rational blowdown of a natural embedding of the configuration $C_{p}$. First, some terminology. Recall that simply connected elliptic surfaces without multiple fibers are classified up to diffeomorphism by their holomorphic Euler characteristic $n=e(X) / 12=p_{g}(X)+1$. The underlying smooth 4-manifold is denoted $E(n)$. The tubular neighborhood of a torus fiber is a copy of $T^{2} \times D^{2}=S^{1} \times\left(S^{1} \times D^{2}\right)$. By a log transform on $E(n)$ we mean the result of removing this $T^{2} \times D^{2}$ from $E(n)$ and regluing it by a diffeomorphism
$$\varphi: T^{2} \times \partial D^{2} \rightarrow T^{2} \times \partial D^{2} .$$

The order of the log transform is the absolute value of the degree of
$$\operatorname{pr}_{\partial D^{2}} \circ \varphi: \operatorname{pt} \times \partial D^{2} \rightarrow \partial D^{2} .$$
Let $E(n)_{\varphi}$ denote the result of this operation on $E(n)$. Note that multiplicity 0 is a possibility. It follows from Moishezon [Mn] that if $\varphi$ and $\varphi^{\prime}$ have the same order, there is a diffeomorphism, fixing the boundary, from $E(n)_{\varphi}$ to $E(n)_{\varphi^{\prime}}$. What is needed here is the existence of a cusp neighborhood (cf. [FS1]). Let $E(n ; p)$ denote any $E(n)_{\varphi}$ where the multiplicity of $\varphi$ is $p$.

In $E(n ; p)$ there is again a copy of the fiber $F$, but there is also a new torus fiber, the multiple fiber. Denote its homology class by $f_{p}$; so in $H_{2}(E(n ; p) ; \mathbf{Z})$ we have $f=p f_{p}$. We can continue this process on other torus fibers; to insure that the resulting manifold is simply connected we can take at most two log-transforms with orders that are pairwise relatively prime. Let the orders be $p$ and $q$ and denote the result by $E(n ; p, q)$. We sometimes write $E(n ; p, q)$ in general, letting $p$ or $q$ equal 1 if there are fewer than 2 multiple fibers. Of course one can take arbitrarily many log transforms (which we shall sometimes do) and we denote the result of taking $r \log$ transforms of orders $p_{1}, \ldots, p_{r}$ by $E\left(n ; p_{1}, \ldots, p_{r}\right)$.

The homology class $f$ of the fiber of $E(n)$ can be represented by an immersed sphere with one positive double point (a nodal fiber). Figure 1 represents a handlebody (Kirby calculus) picture for a cusp neighborhood $N$ which contains this nodal fiber. (See [K] for an explaination of such pictures and how to manipulate them.) Blow up this double point (i.e. take the proper transform of $f$ ) so that the class $f-2 e_{1}$ (where $e_{1}$ is the homology class of the exceptional divisor) is represented by an embedded sphere with square -4 (cf. Figure 2). This is just the configuration $C_{2}$. Now the exceptional divisor intersects this sphere in two positive points. Blow up one of these points, i.e. again take a proper transform. One obtains the homology classes $u_{2}=f-2 e_{1}-e_{2}$ and $u_{1}=e_{1}-e_{2}$ which form the configuration $C_{3}$. Continuing in this fashion, $C_{p}$ naturally embeds in $N \#_{p-1} \overline{\mathbf{C P}}^{2} \subset E(n) \#_{p-1} \overline{\mathbf{C P}}^{2}$ as in Figure 3. Our first important example of a rational blown down is:

Theorem 3.1. The rational blowdown of the above configuration $C_{p} \subset E(n) \#(p-1) \overline{\mathbf{C P}}^{2}$ is diffeomorphic $E(n ; p)$.

Proof. As proof, we offer a sequence of Kirby calculus moves in Figures 4 through 8. In Figure 4 we add to Figure 3 the handle (with framing -1) which has the property that when added to $\partial C_{p}$ one obtains $S^{2} \times S^{1}$ (so that when a further 3 and 4-handle are attached $B_{p}$ is obtained). Then we blow down the added handle, keeping track of the dual 2-handle (which is labelled in Figure 4 with 0-framing). In Figure 5 we blow down this added handle with framing -1 and rearrange to obtain Figure 6. Now slide $e_{1}$ over the handle with framing +1 and rearrange to obtain Figure 7. Blow down the -1 curve in Figure 7; so the -2 curve becomes a -1 curve. Continue this process $p-2$ times to obtain Figure 8. If in this final picture one replaces the handle with a dot on it by a 1-handle, there results the handlebody picture given by Gompf in [G1] for $N_{p}$, the order $p$ log-transformed cusp neighborhood. \(\square\)

For the case $p=2$, this theorem was first observed by Gompf [G2].
Here is a useful observation: To perform a log transform of order $p q$, first perform a log transform of order $p$ and then perform a log transform of order $q$ on the resulting multiple fiber $f_{p}$. This can also be obtained via a rational blowdown procedure. Figure 9 is a handlebody decomposition $N_{p} \#_{q-1} \overline{\mathbf{C P}}^{2}$ with an easily identified copy of $C_{q}$. The proof that the result of blowing down $C_{q}$ results in $E(n ; p q)$ is to again follow through the steps of the proof of Theorem 3.1.

Proposition 3.2. Let $f_{p}$ be the multiple fiber in $E(n ; p)$. Then there is an immersed (nodal) 2-sphere $S \subset E(n ; p)$ representing the homology class of $f_{q}$. Let $q$ be a positive integer relatively prime to $p$. If the process of Theorem 3.1 is applied to $S$, i.e. if $Y$ is the rational blowdown of the configuration $C_{q}$ in $E(n ; p) \#(q-1) \overline{\mathbf{C P}}^{2}$ obtained from blowing up $S$, then $Y \cong E(n ; p q)$, the result of a multiplicity $p q$ log transform on $E$.

Example 2. In $E(2)$ there is an embedded sphere with self-intersection -4 such that its blowdown is diffeomorphic to $3 \mathbf{C P}^{2} \# 18 \overline{\mathbf{C P}}^{2}$.

For this, any -4 curve suffices; however to verify that the rational blowdown decomposes requires more Kirby calculus manipulations. The Milnor fiber $M(2,3,5)$ for the Poincaré homology 3-sphere $P=\Sigma(2,3,5)$ embeds in $E(2)$ so that $E(2)=M(2,3,5) \cup W$ for some 4-manifold $W$ (cf. [FS1]). Now $\partial M(2,3,5)=P$ also bounds another negative definite 4-manifold $S$ which is the trace of -1 surgery on the left handed trefoil. It is known that $S \cup W$ is diffeomorphic to $3 \mathbf{C P}^{2} \# 11 \overline{\mathbf{C P}}^{2}$. Thus, to construct the example, it suffices find a -4 curve in $M(2,3,5)$ whose rational blowdown produces $S \# 7 \overline{\mathbf{C P}}^{2}$. Recall that $M(2,3,5)$ is just the $E_{8}$ plumbing manifold given in Figure 10. Slide the handle labeled $h$ over the handle labeled $k$ to obtain the -4 curve $h+k$ in Figure 11. Blow down this -4 curve to obtain Figure 12. Now slide the handle labeled $h^{\prime}$ over the handle labeled $k^{\prime}$ to obtain Figure 13. Now succesively blow down the -1 curves to obtain Figure 14. Cancelling the 1-handle with the 2 -handle with framing -2 yields $S \# 7 \overline{\mathbf{C P}}^{2}$.

Example 3. Given any smooth 4-manifold $X$, there is an embedding of the configuration $C_{p} \subset$ $X \#(p-1) \overline{\mathbf{C P}}^{2}=Y$ with $u_{i}=e_{p-(i+1)}-e_{p-i}$ for $i=1, \ldots, p-2$, and $u_{p-1}=-2 e_{1}-e_{2}-\cdots-e_{p-1}$ such that the rational blowdown $Y_{p}$ of $Y$ is diffeomorphic to $X \# H_{p}$ where $H_{p}$ is the homology 4-sphere with $\pi_{1}=\mathbf{Z}_{p}$ which is the double of the rational ball $B_{p}$.

In fact $C_{p} \subset \#(p-1) \overline{\mathbf{C P}}^{2}=Y$, and, from the proof of Lemma 2.1, the result of blowing down this configuration is just the double of $B_{p}$.

Note that Example 3 points out that although a smooth 4-manifold $Y$ may have a symplectic structure, it need not be the case that a rational blowdown $Y_{p}$ of $Y$ also have a symplectic structure. For in this example $X \# H_{p}$ will never have a symplectic structure since its $p$-fold cover can be written as a connected sum of two 4-manifolds with positive $b_{+}$so has vanishing Seiberg-Witten invariants and hence, by Taubes [T5], is not symplectic. Of course, in this example the configuration $C_{p}$ is not symplectically embedded. This brings up the possibility that any smooth 4-manifold can be rationally blown up to a symplectic 4-manifold.

\section*{4. The Donaldson Series}

In this section we outline the definition of the Donaldson invariant. We refer the reader to [D1] and [DK] for a more complete treatment. Given an oriented simply connected 4-manifold with a generic Riemannian metric and an $S U(2)$ or $S O(3)$ bundle $P$ over $X$, the moduli space of gauge equivalence classes of anti-self-dual connections on $P$ is a manifold $\mathcal{M}_{X}(P)$ of dimension
$$8 c_{2}(P)-3\left(1+b_{X}^{+}\right)$$
if $P$ is an $S U(2)$ bundle, and
$$-2 p_{1}(P)-3\left(1+b_{X}^{+}\right)$$
if $P$ is an $S O(3)$ bundle. It will often be convenient to treat these two cases together by identifying $\mathcal{M}_{X}(P)$ and $\mathcal{M}_{X}(\operatorname{ad}(P))$ for an $S U(2)$ bundle $P$. Over the product $\mathcal{M}_{X}(P) \times X$ there is a universal $S O(3)$ bundle P which gives rise to a homomorphism $\mu: H_{i}(X ; \mathbf{R}) \rightarrow \mathbf{H}^{4-\mathbf{i}}\left(\mathcal{M}_{\mathbf{X}}(\mathbf{P}) ; \mathbf{R}\right)$ obtained by decomposing the class $-\frac{1}{4} p_{1}(\mathbf{P}) \in H^{4}\left(\mathcal{M}_{X} \times X\right)$.

When either $w_{2}(P) \neq 0$ or when $w_{2}(P)=0, d>\frac{3}{4}\left(1+b_{X}^{+}\right)$, the Uhlenbeck compactification $\overline{\mathcal{M}}_{X}(P)$ carries a fundamental class. In practice, one is able to get around this latter restriction by blowing up $X$ and considering bundles over $X \# \overline{\mathbf{C P}}^{2}$ which are nontrivial when restricted to the exceptional divisor [MM1]. In [FM] it is shown that for $\alpha \in H_{2}(X ; \mathbf{Z})$ the classes $\mu(\alpha) \in$ $H^{2}\left(\mathcal{M}_{X}(P)\right)$ extend over $\overline{\mathcal{M}}_{X}(P)$. When $b_{X}^{+}$is odd, $\operatorname{dim} \mathcal{M}_{X}(P)$ is even, say equal to $2 d$. In fact, a class $c \in H_{2}(X ; \mathbf{Z})$ and a nonnegative integer $d \equiv-c^{2}+\frac{1}{2}\left(1+b^{+}\right)$determine an $S O(3)$ bundle $P_{c, d}$ over $X$ with $w_{2}\left(P_{c, d}\right) \equiv c(\bmod 2)$ and formal dimension $\operatorname{dim} \mathcal{M}_{X}\left(P_{c, d}\right)=2 d$. For $\bar{\alpha}=\left(\alpha_{1}, \ldots, \alpha_{d}\right) \in H_{2}(X ; \mathbf{Z})^{d}$, write $\mu(\bar{\alpha})=\mu\left(\alpha_{1}\right) \cup \cdots \cup \mu\left(\alpha_{d}\right)$. Then one has
$$\left\langle\mu(\bar{\alpha}),\left[\overline{\mathcal{M}}_{X}\left(P_{c, d}\right)\right]\right\rangle=\int_{\overline{\mathcal{M}}_{X}\left(P_{c, d}\right)} \mu(\bar{\alpha})$$
when $\mu(\bar{\alpha})$ is viewed as a $2 d$-form.
If $[1] \in H_{0}(X ; \mathbf{Z})$ is the generator, then $\nu=\mu([1])=-\frac{1}{4} p_{1}(\beta) \in H^{4}\left(\mathcal{M}_{X}(P)\right)$ where $\beta$ is the basepoint fibration $\tilde{\mathcal{M}}_{X}(P) \rightarrow \mathcal{M}_{X}(P)$ with $\tilde{\mathcal{M}}_{X}(P)$ the manifold of anti-self-dual connections on $P$ modulo based gauge transformations, i.e. those that are the identity on the fiber over a fixed basepoint. The class $\nu$ extends over the Uhlenbeck compactification $\overline{\mathcal{M}}_{X}(P)$ if $w_{2}(P) \neq 0$, and in case $P$ is an $S U(2)$ bundle, the class will extend under certain dimension restrictions. Once again, these restrictions can be done away with via the tricks mentioned above [MM1].

Consider the graded algebra
$$\mathbf{A}(X)=\operatorname{Sym}_{*}\left(H_{0}(X) \oplus H_{2}(X)\right)$$
where $H_{i}(X)$ has degree $\frac{1}{2}(4-i)$. The Donaldson invariant $D_{c}=D_{X, c}$ is then an element of the dual algebra $\mathbf{A}^{*}(X)$, i.e. a linear function
$$D_{c}: \mathbf{A}(X) \rightarrow \mathbf{R} .$$
This is a homology orientation-preserving diffeomorphism invariant for manifolds $X$ satisfying $b_{X}^{+} \geq$ 3. Throughout this paper we assume $b_{X}^{+} \geq 3$ and odd.

We let $x \in H_{0}(X)$ be the generator [1] corresponding to the orientation. In case $a+2 b=d>$ $\frac{3}{4}\left(1+b_{X}^{+}\right)$and $\alpha \in H_{2}(X)$,
$$D_{c}\left(\alpha^{a} x^{b}\right)=\left\langle\mu(\alpha)^{a} \nu^{b},\left[\overline{\mathcal{M}}_{X}\left(P_{c, d}\right)\right]\right\rangle .$$
We may extend $\mu$ over $\mathbf{A}(X)$, and write for $z \in \mathbf{A}(X)$ of degree $d, D_{c}(z)=\left\langle\mu(z),\left[\overline{\mathcal{M}}_{X}\left(P_{c, d}\right)\right]\right\rangle$. Since such moduli spaces $\mathcal{M}_{X}\left(P_{c, d}\right)$ exist only for $d \equiv-c^{2}+\frac{1}{2}\left(1+b_{X}^{+}\right)(\bmod 4)$, the Donaldson invariant $D_{c}$ is defined only on elements of $\mathbf{A}(X)$ whose total degree is congruent to $-c^{2}+\frac{1}{2}\left(1+b_{X}^{+}\right)$ $(\bmod 4)$. By definition, $D_{c}$ is 0 on all elements of other degrees. When $P$ is an $S U(2)$ bundle one simply writes $D$ or $D_{X}$.

If $Y$ is a simply connected 4-manifold with boundary, one can similarly construct relative Donaldson invariants. A good reference for this is [MMR]. When the boundary is a lens space, the theory simplifies considerably, and we get relative Donaldson invariants
$$D_{Y, c}\left[\lambda_{i}\right]: \mathbf{A}(Y) \rightarrow \mathbf{R} .$$

Following [KM1], one considers the invariant
$$\hat{D}_{X, c}: \operatorname{Sym}_{*}\left(H_{2}(X)\right) \rightarrow \mathbf{R}$$
defined by $\hat{D}_{X, c}(u)=D_{X, c}\left(\left(1+\frac{x}{2}\right) u\right)$. Whereas $D_{X, c}$ can be nonzero only in degrees congruent to $-c^{2}+\frac{1}{2}\left(1+b^{+}\right)(\bmod 4), \hat{D}_{X, c}$ can be nonzero in degrees congruent to $-c^{2}+\frac{1}{2}\left(1+b^{+}\right)(\bmod 2)$. The Donaldson series $\mathbf{D}_{c}=\mathbf{D}_{X, c}$ is defined by
$$\mathbf{D}_{X, c}(\alpha)=\hat{D}_{X, c}(\exp (\alpha))=\sum_{d=0}^{\infty} \frac{\hat{D}_{X, c}\left(\alpha^{d}\right)}{d!}$$
for all $\alpha \in H_{2}(X)$. This is a formal power series on $H_{2}(X)$.
A simply connected 4-manifold $X$ is said to have simple type if the relation $D_{X, c}\left(x^{2} z\right)=4 D_{X, c}(z)$ is satisfied by its Donaldson invariant for all $z \in \mathbf{A}(X)$ and for all $c \in H_{2}(X ; \mathbf{Z})$. This important definition is due to Kronheimer and Mrowka [KM1] and was observed to hold for many 4-manifolds [KM2, FS3]. In terms of $\hat{D}_{X, c}$, the simple type condition is that $\hat{D}_{X, c}(z x)=2 \hat{D}_{X, c}(z)$ for all $z \in \mathbf{A}(X)$ and for all $c \in H_{2}(X ; \mathbf{Z})$. The assumption of simple type assures that for each $c$, the complete Donaldson invariant $D_{X, c}$ is determined by the Donaldson series $\mathbf{D}_{X, c}$. It is still an open question whether all 4-manifolds are of simple type.

The structure theorem is:
Theorem 4.1 (Kronheimer and Mrowka [KM2, FS3]). Let $X$ be a simply connected 4-manifold of simple type. Then, there exist finitely many 'basic' classes $\kappa_{1}, \ldots, \kappa_{p} \in H_{2}(X, \mathbf{Z})$ and nonzero rational numbers $a_{1}, \ldots, a_{p}$ such that
$$\mathbf{D}_{X}=\exp (Q / 2) \sum_{s=1}^{p} a_{s} e^{\kappa_{s}}$$
as analytic functions on $H_{2}(X)$. Each of the 'basic classes' $\kappa_{s}$ is characteristic, i.e. $\kappa_{s} \cdot x \equiv x \cdot x$ (mod 2)for all $x \in H_{2}(X ; \mathbf{Z})$.

Further, suppose $c \in H_{2}(X ; \mathbf{Z})$. Then
$$\mathbf{D}_{X, c}=\exp (Q / 2) \sum_{s=1}^{p}(-1)^{\frac{c^{2}+\kappa_{s} \cdot c}{2}} a_{s} e^{\kappa_{s}}$$
Here the homology class $\kappa_{s}$ acts on an arbitrary homology class by intersection, i.e. $\kappa_{s}(u)=\kappa_{s} \cdot u$. The basic classes $\kappa_{s}$ satisfy certain inequalities analogous to the adjuction formula in a complex surface [KM2, FS3]. We shall need

Theorem 4.2 ([FS3]). Let $X$ be a simply connected 4-manifold of simple type and let $\left\{\kappa_{s}\right\}$ be the set of basic classes as above. If $u \in H_{2}(X ; \mathbf{Z})$ is represented by an immersed 2-sphere with $p \geq 1$ positive double points, then for each $s$
$$2 p-2 \geq u^{2}+\left|\kappa_{s} \cdot u\right| .$$

Theorem 4.3 ([FS3]). Let $X$ be a simply connected 4-manifold of simple type with basic classes $\left\{\kappa_{s}\right\}$ as above. If the nontrivial class $u \in H_{2}(X ; \mathbf{Z})$ is represented by an immersed 2-sphere with no positive double points, then let
$$\left\{\kappa_{s} \mid s=1, \ldots, 2 m\right\}$$
be the collection of basic classes which violate the inequality (1). Then $\kappa_{s} \cdot u= \pm u^{2}$ for each such $\kappa_{s}$. Order these classes so that $\kappa_{s} \cdot u=-u^{2}(>0)$ for $s=1, \ldots, m$. Then
$$\sum_{s=1}^{m} a_{s} e^{\kappa_{s}+u}-(-1)^{\frac{1+b_{X}^{+}}{2}} \sum_{s=1}^{m} a_{s} e^{-\kappa_{s}-u}=0 .$$

\section*{5. The Basic Computational Theorem}

Recall that for $y \in H_{2}(X)$ and $F \in \mathbf{A}(X)$, interior product
$$\iota_{u} F(v)=(\operatorname{deg}(v)+1) F(u v)$$
defines a derivation which we denote by $\partial_{u}$ and call 'partial derivation'. Our basic theorem is:
Theorem 5.1. Let $X$ be a simply connected 4-manifold of simple type containing the configuration $C_{p}$, and let $X_{p}$ be the result of rationally blowing down $C_{p}$. Then, restricted to $X^{*}=X_{p} \backslash B_{p}=X \backslash C_{p}$ :
$$\mathbf{D}_{X_{p}}=\sum_{i=1}^{m(p)} \alpha_{i}(p) \partial^{n_{i}(p)} \mathbf{D}_{X, c_{i}(p)}$$
where $\alpha_{i}(p) \in \mathbf{Q}, c_{i}(p) \in H_{2}\left(C_{p} ; \mathbf{Z}\right), \partial^{n_{i}(p)}$ is an $n_{i}$ th order partial derivative with respect to classes in $H_{2}\left(C_{p} ; \mathbf{Z}\right)$, and these quantities depend only on $p$, not on $X$.

As motivation, and for use in the next section, we begin with a 'by hand' calculation.

Lemma 5.2. Let $X$ be a simply connected 4-manifold containing an embedded 2-sphere $\Sigma$ of square -4 representing the homology class $\sigma$. Let $X_{2}$ be the result of rationally blowing down $\Sigma$. Then
$$\left.\mathbf{D}_{X_{2}}\right|_{X^{*}}=\mathbf{D}_{X}-\mathbf{D}_{X, \sigma} .$$
Proof. Here we work with $S U(2)$ connections over $X_{2}$ and $X$. The conjugacy classes of $S U(2)$ representations of $L(4,-1)$ are $\{ \pm 1, i\}$. Since a multiple of any class in $H_{2}\left(X_{2} ; \mathbf{Z}\right)$ lives in $H_{2}\left(X^{*} ; \mathbf{Z}\right)$, it suffices to evaluate $D_{X_{2}}(z)$ for $z \in \mathbf{A}\left(X^{*}\right)$. The lemma is proved by a standard counting argument obtained by stretching the neck $\partial X^{*} \times \mathbf{R}$ in $X_{2}$. Doing this with nonempty moduli spaces leads to a sequence of anti-self-dual connections (with respect to a sequence of generic metrics on $X_{2}$ ) which limit to anti-self-dual connections $A^{*}$ over $X^{*}$, and $A_{B}$ over $B_{2}$ together perhaps with instantons on $X^{*}$ and $B_{2}$. Dimension counting shows that $A^{*}$ is irreducible, $A_{B}$ is reducible (hence flat), and that no instantons occur. (The key fact is that each representation of $L(4,-1)$ has a positive dimensional isotropy group.) The flat $S U(2)$ connections on $B_{2}$ are ±1. Thus we have
$$D_{X_{2}}(z)= \pm D_{X^{*}}[1](z) \pm D_{X^{*}}[-1](z) .$$
The invariants $D_{X^{*}}[ \pm 1](z)$ are relative Donaldson invariants of $X^{*}$ with the given boundary values.
We first claim that $D_{X^{*}}[1](z)= \pm D_{X}(z)$. This is almost obvious by applying an argument like the one above. We need to know that there are no nontrivial reducible connections on the neighborhood $C_{2}$ of $\Sigma$ with boundary value 1 and in a moduli space of negative dimension. This follows simply from the fact that if $\lambda$ is the complex line bundle whose first chern class generates $H^{2}\left(C_{2} ; \mathbf{Z}\right)$, then the moduli space of anti-self-dual connections on $\lambda^{m}+\lambda^{-m}$ has dimension $4 m-3$ (see [FS3]). To compute $D_{X^{*}}[-1](z)$, note that the Poincaré dual of $\sigma$ in $H^{2}\left(X ; \mathbf{Z}_{2}\right)$ is the unique nonzero class whose restrictions to $X^{*}$ and $C_{2}$ are both 0 . When passing to structure group $\operatorname{SO}(3)$, the representation -1 becomes trivial, and thus extends over $C_{2}$ as the trivial $S O(3)$ connection. Now one can see that $D_{X^{*}}[-1](z)= \pm D_{X, \sigma}(z)$.

Finally, we need to determine signs. A key point following from our discussion is that they are independent of $X$. Recall from Example 2 that there is a sphere $\Sigma$ of square -4 in the $K 3$-surface $X$ which has a rational blowdown $X_{2}$ with $\mathbf{D}_{X_{2}}=0$. Since $\mathbf{D}_{X, \sigma}=\exp (Q / 2)=\mathbf{D}_{X}$, our formula must read
$$D_{X_{2}}(z)= \pm\left(D_{X}(z)-D_{X, \sigma}(z)\right) .$$
To compute the overall sign, we must compare the way that signs are attached to $A_{0} \# \Theta_{B_{2}}$, and $A_{0} \# \Theta_{C_{2}}$ where $A_{0}$ is an anti-self-dual connection on $X^{*}$ with boundary value 1 and $\Theta_{B_{2}}$ and $\Theta_{C_{2}}$ are the trivial connections on $B_{2}$ and $C_{2}$. This is done in a way similar to the proof of [FS2, Theorem 2.1], and the sign is easily seen to be '+'. \(\square\)

We now proceed toward the proof of Theorem 5.1. The first step is to understand reducible connections over $C_{p}$. It will be convenient here to use the symmetric dual bases $\left\{v_{i}\right\}$ and $\left\{\delta_{i}\right\}$ of §2. Using these coordinates, we express elements of $H_{2}\left(C_{p}, \partial C_{p} ; \mathbf{Z}\right)$ as
$$\beta=\sum t_{i} \delta_{i}=\left\langle t_{1}, \ldots, t_{p-1}\right\rangle .$$

Classes of the form $\langle t, \ldots, t, s, \ldots, s\rangle$ will play a special role. We shall use the abbreviation
$$\langle t, \ldots, t, s, \ldots, s\rangle=\langle t, s ; b\rangle$$
if the number of $s$ 's is $1 \leq b \leq p-1$. If $e \in H_{2}\left(C_{p}, \partial C_{p} ; \mathbf{Z}\right)$, write $\mathcal{M}_{e}$ for the $S O(3)$-moduli space of anti-self-dual connections on $C_{p}$ which contains the reducible connection in the bundle $L_{e} \oplus \mathbf{R}$ where $c_{1}\left(L_{e}\right)=e$, and which are asymptotically flat with boundary value $\partial^{\prime} e \in \chi_{S O(3)}\left(L\left(p^{2}, 1-p\right)\right)$. Note that $\partial\langle t, t+1 ; b\rangle=(p-1) t+b$.

Lemma 5.3. Let $e=\langle t, t+1 ; b\rangle$ with $0 \leq t \leq p$. Then $\operatorname{dim} \mathcal{M}_{e}=2 t-1$.
Proof. With respect to the basis $\left\{\delta_{i}\right\}$, the intersection form of $H_{2}\left(C_{p}, \partial\right)$ is
$$Q=-\frac{\left(p^{2}-p-1\right)}{p^{2}} \sum x_{i}^{2}+2 \frac{p+1}{p^{2}} \sum_{i<j} x_{i} x_{j}$$
and
$$\begin{aligned}
e^{2}=\left(b(t+1)^{2}+(p-b-1) t^{2}\right)( & \left.-\frac{\left(p^{2}-p-1\right)}{p^{2}}\right) \\
& +2\left((p-b-1) b t(t+1)+\binom{p-b-1}{2} t^{2}+\binom{b}{2}(t+1)^{2}\right) \frac{p+1}{p^{2}}
\end{aligned}$$
Hence
$$e^{2}=\frac{1}{p^{2}}\left(b^{2}+b^{2} p-b p^{2}-2 b t+t^{2}-p t^{2}\right) .$$
By hypothesis, $\partial e=(p-1) t+b \neq 0$. From [L] we have
$$\frac{\rho}{2}(\partial e)=-\frac{1}{p^{2}}\left(-2 b^{2}-2 b^{2} p-p^{2}+2 b p^{2}+4 b t-2 p^{2} t-2 t^{2}+2 p t^{2}\right)$$
and by the index theorem APS:
$$\operatorname{dim} \mathcal{M}_{e}=-2 e^{2}-\frac{3}{2}-\frac{1}{2}(h+\rho)(\partial e)=-2 e^{2}-2-\frac{\rho}{2}(\partial e)=2 t-1 .$$ \(\square\)

Lemma 5.4. Let $e=\langle t, t+1 ; b\rangle$ with $t \geq 0$ and $(p-1) t+b \leq p^{2} / 2$. Suppose also that $e^{\prime}=$ $\left\langle\alpha_{1}, \ldots, \alpha_{p-1}\right\rangle$ with $\sum \alpha_{i}=(p-1) t+b+r p^{2}, r \neq 0,-1$. Then $\operatorname{dim} \mathcal{M}_{e^{\prime}}>\operatorname{dim} \mathcal{M}_{e}$.

Proof. Using (2), it follows from symmetry that for fixed $s=\sum x_{i}$, the minimum absolute value of $Q\left\langle x_{1}, \ldots, x_{p-1}\right\rangle$ occurs at $\mu(s)=\langle s /(p+1), \ldots, s /(p+1)\rangle$, and
$$\mu(s)^{2}=-\frac{\left(p^{2}-p-1\right)}{p^{2}}(p-1) \frac{s^{2}}{(p-1)^{2}}+2 \frac{p+1}{p^{2}}\binom{p-1}{2} \frac{s^{2}}{(p-1)^{2}}=\frac{s^{2}}{p^{2}-p^{3}} .$$
On the other hand by (3), $e^{2}=\frac{1}{p^{2}}\left(b^{2}+b^{2} p-b p^{2}-2 b t+t^{2}-p t^{2}\right)$. Set $s=(p-1) t+b+r p^{2}$. Then
$$\mu(s)^{2}-e^{2}=-\frac{1}{p-1}\left(b+b^{2}+2 b r+p^{2} r^{2}+2 r t(p-1)-b p\right) .$$
Since $1 \leq b \leq p-1$, we have $b p \leq p^{2}-p \leq p^{2} r^{2}$. So
$$\mu(s)^{2}-e^{2} \leq-\frac{1}{p-1}\left(b+b^{2}+2 b r+2 r t(p-1)\right)$$
and if we assume $r \geq 1, \mu(s)^{2}<e^{2}(<0)$. By the index theorem,
$$\operatorname{dim} \mathcal{M}_{e^{\prime}}=-2 e^{\prime 2}-\frac{3}{2}-\frac{1}{2}(h+\rho)\left(\partial e^{\prime}\right) \geq-2 \mu(s)^{2}-\frac{3}{2}-\frac{1}{2}(h+\rho)(\partial e) \geq \operatorname{dim} \mathcal{M}_{e}$$
since $(h+\rho)\left(\partial e^{\prime}\right)=(h+\rho)(\partial e)$. Notice that we have not yet used the hypothesis that $(p-1) t+b \leq$ $p^{2} / 2$.

If $r<-1$, set $\bar{e}=\left\langle t^{\prime}, t^{\prime}+1 ; c\right\rangle$ with $t^{\prime}, c$ chosen such that
$$(p-1) t^{\prime}+c=p^{2}-((p-1) t+b) \geq p^{2} / 2 .$$
By Lemma 5.3, $\operatorname{dim} \mathcal{M}_{\bar{e}} \geq \operatorname{dim} \mathcal{M}_{e}$ with equality only if $t^{\prime}=t$. Note that $\operatorname{dim} \mathcal{M}_{-e^{\prime}}=\operatorname{dim} \mathcal{M}_{e^{\prime}}$, and $-\sum \alpha_{i}=(p-1) t^{\prime}+c-(r+1) p^{2}$. Since $-(r+1) \geq 1$, the case we have already handled shows that $\operatorname{dim} \mathcal{M}_{-e^{\prime}} \geq \operatorname{dim} \mathcal{M}_{\bar{e}}$. \(\square\)

Lemma 5.5. Let $e=\langle t, t+1 ; b\rangle$ with $t \geq 0$. Suppose that $e^{\prime}=\left\langle\alpha_{1}, \ldots, \alpha_{p-1}\right\rangle \neq e$ but $\sum \alpha_{i}=$ $(p-1) t+b$. Then $\operatorname{dim} \mathcal{M}_{e^{\prime}}>\operatorname{dim} \mathcal{M}_{e}$ unless $e^{\prime}$ is a permutation of $e$.

Proof. It suffices to show that $e^{\prime 2}<e^{2}$. Write $e^{\prime}=e+\nu$ where
$$\nu=\left\langle n_{1}, \ldots, n_{p-b-1}, n_{p-b}, \ldots, n_{p-1}\right\rangle .$$
Since the sum of the coordinates of $e$ and $e^{\prime}$ is the same, $\sum n_{i}=0$. Let
$$\begin{gathered}
N_{L}=\sum_{i=1}^{p-b-1} n_{i} \quad N_{R}=\sum_{i=p-b}^{p-1} n_{i} . \\
e^{\prime^{2}}=e^{2}+2\left(N_{L}((p-2) t+b)+N_{R}((p-2) t+b-1)\right)\left(\frac{p+1}{p^{2}}\right) \\
-2\left(N_{L} t+N_{R}(t+1)\right)\left(\frac{p^{2}-p-1}{p^{2}}\right)+\nu^{2} \\
=e^{2}-2 N_{R}+\nu^{2}
\end{gathered}$$
since $N_{L}+N_{R}=0$. Hence $\frac{1}{2}\left(\operatorname{dim} \mathcal{M}_{e^{\prime}}-\operatorname{dim} \mathcal{M}_{e}\right)=e^{2}-e^{\prime 2}=-\nu^{2}+2 N_{R}$. However, if $y$ is the result of adding +1 to $x_{i_{0}}$ and -1 to $x_{i_{1}}$ in $x=\left\langle x_{1}, \ldots, x_{p-1}\right\rangle$, then $y^{2}-x^{2}=2\left(x_{i_{1}}-x_{i_{0}}-1\right)$. Starting with $x=\langle 0, \ldots, 0\rangle$ and making these ±1 moves with constant sign in each coordinate until reaching $\nu$, we see that the minimum change in the square is -2. This is achieved only if each coordinate operated on is originally 0. Thus, if $N_{+}$is the sum of the positive coordinates $n_{i}$, we have $-\nu^{2} \geq 2 N_{+}$. Equality occurs only if each $n_{i}$ is ±1 or 0. In this case there are $N_{+}$such -1's. If $\left|N_{R}\right|<N_{+}$then $-\nu^{2}+2 N_{R} \geq 2\left(N_{+}-\left|N_{R}\right|\right)>0$. If $\left|N_{R}\right|=N_{+}$then each -1 occurs in a coordinate $n_{i}, i=p-b, \ldots, p-1$, and so $e^{\prime}$ is a permutation of $e$. If $-\nu^{2}>2 N_{+}$then since $\left|N_{R}\right| \leq N_{+}$, we have $-\nu^{2}+2 N_{R}>0$. \(\square\)

Proposition 5.6. Let $e=\langle t, t+1 ; b\rangle$ with $t \geq 0$ and $(p-1) t+b \leq p^{2} / 2$. If $e^{\prime}=\left\langle\alpha_{1}, \ldots, \alpha_{p-1}\right\rangle$ with $e^{\prime} \equiv e(\bmod 2)$ and $\operatorname{dim} \mathcal{M}_{e^{\prime}} \leq \operatorname{dim} \mathcal{M}_{e}$, then $\partial e^{\prime} \leq \partial e$ as elements of $\mathbf{Z}_{p^{2}}$.

Proof. Let $\bar{e}=\langle s, s+1 ; c\rangle$ with $s \geq 0$, be the unique class of this form with $0 \leq \partial \bar{e} \leq p^{2} / 2$ satisfying $\partial e^{\prime}=\partial \bar{e}$. Lemmas 5.4 and 5.5 imply that unless $-p^{2} / 2 \leq \sum a_{i}<0$, we have $\operatorname{dim} \mathcal{M}_{\bar{e}} \leq \operatorname{dim} \mathcal{M}_{e^{\prime}}$; so $s \leq t$. This holds in any case, since we can always work with $-e^{\prime}$. If $s=t$ then $\bar{e}=e$ since no class $\left\langle t, t+1 ; b^{\prime}\right\rangle$ with $b^{\prime} \neq b$ is congruent to $e(\bmod 2)$. This means that $\partial e^{\prime} \leq \partial e$. \(\square\)

Corollary 5.7. Let $e=\langle t, t+1 ; b\rangle$ with $t \geq 0$ and $(p-1) t+b \leq p^{2} / 2$. Suppose that $e^{\prime}=$ $\left\langle\alpha_{1}, \ldots, \alpha_{p-1}\right\rangle$ with $\partial^{\prime} e^{\prime}=\partial^{\prime} e \in \chi_{S O(3)}\left(L\left(p^{2}, 1-p\right)\right)$ and $e^{\prime} \equiv e(\bmod 2)$. Then $\operatorname{dim} \mathcal{M}_{e^{\prime}}=$ $\operatorname{dim} \mathcal{M}_{e}+4 k, k \geq 0$.

Proof. As above, $\operatorname{dim} \mathcal{M}_{e} \leq \operatorname{dim} \mathcal{M}_{e^{\prime}}$. But $e^{\prime} \equiv e(\bmod 2)$ implies that $e^{\prime 2}=e^{2}(\bmod 4)$; so the corollary follows from the index theorem. \(\square\)

We need one more simple fact. Let $\iota:\left(C_{p}, \emptyset\right) \rightarrow\left(C_{p}, \partial\right)$ be the inclusion.
Lemma 5.8. Let $e \in H_{2}\left(C_{p}, \partial ; \mathbf{Z}\right)$, and suppose that $\partial e \equiv 0(\bmod 2)$ in case $p$ is even. Then there is a $c \in H_{2}\left(C_{p} ; \mathbf{Z}\right)$ such that $\iota_{*}(c) \equiv e(\bmod 2)$.

Proof. This follows directly from the exact sequence
$$0 \rightarrow H_{2}\left(C_{p} ; \mathbf{Z}\right) \rightarrow H_{2}\left(C_{p}, \partial ; \mathbf{Z}\right) \rightarrow \mathbf{Z}_{p^{2}} \rightarrow 0 .$$ \(\square\)

We now proceed toward the proof of Theorem 5.1. We shall work always with structure group $S O(3)$ and identify $S U(2)$ connections with $S O(3)$ connections on $w_{2}=0$ bundles. We wish to calculate $D_{X_{p}}(z)$ for $z \in \mathbf{A}\left(X^{*}\right)$. If we blow up $X^{*}$ and evaluate $D_{X_{p} \# \overline{\mathbf{C P}}^{2},{ }_{e}}(z e)=D_{X_{p}}(z)$ where $e$ is the exceptional class [MM1], we can work under the assumption that there are no flat connections on the complement of $B_{p}$ with the same $w_{2}$ as our given bundle. Keeping this in mind, we may simplify notation without loss by making the same assumption for our given situation, $X_{p}=X^{*} \cup B_{p}$. Consider a sequence of generic metrics on $X_{p}$ which stretch a collar on $L\left(p^{2}, 1-p\right)=\partial B_{p}$ to infinite length, giving the disjoint union of $X^{*}$ and $B_{p}$ with cylindrical ends as the limit. A sequence of anti-self-dual connections $\left\{A_{n}\right\}$ with respect to these metrics, each of which also lies in the divisor $V_{z}$ corresponding to $z \in \mathbf{A}\left(X^{*}\right)$, must limit to $A_{X^{*}} \amalg A_{B_{p}}$. These are anti-self-dual connections over $X^{*}$ and $B_{p}$, and a counting argument shows that $A_{X^{*}} \in V_{z}$ and $A_{B_{p}}$ is reducible. (Our above assumption is helpful here.) Since the only reducible connections on the rational ball $B_{p}$ are flat, we get
$$D_{X_{p}}(z)=\sum_{n=0}^{[p / 2]} \pm D_{X^{*}}\left[\eta^{n p}\right](z) .$$
The notation $D_{X^{*}}\left[\eta^{n p}\right]$ stands for the relative Donaldson invariant on $X^{*}$ constructed from the moduli space of anti-self-dual connections over $X^{*}$ (with a cylindrical end) which decay exponentially to a flat connection whose gauge equivalence class corresponds to the conjugacy class of the representation $\eta^{n p}$.

We need to calculate the summands of (4). We begin with $n=0$, i.e. $D_{X^{*}}[1](z)$. Consider $D_{X}(z)$. To calculate this, we use a neck-stretching argument as above. We see that on $C_{p}$ we must get a reducible anti-self-dual connection corresponding to chern class $e$ with $\operatorname{dim} \mathcal{M}_{e}<0$ and $e \equiv 0$ $(\bmod 2)$. This last condition means that $e$ cannot have the form $\langle 0,1 ; b\rangle$ (recall $1 \leq b \leq p-1$ ); so by Lemma 5.3, $e \neq\langle t, t+1 ; b\rangle, t \geq 0$. Now Proposition 5.6 implies that $e=0$. Thus
$$D_{X}(z)= \pm D_{X^{*}}[1](z)$$
and the sign is independent of $X$.
To calculate the other terms, we must utilize techniques of Taubes [T1, T2, T3, T4] or Wieczorek [Wk] as in [FS3, §4]. We shall quickly review the methods involved and refer the reader to [FS3] and the references given there for more details. Our plan is to evaluate all the $D_{X^{*}}\left[\eta^{m}\right](z)$ inductively. (In case $p$ is even, we only need to calculate this for $m$ even.) We do this by computing $D_{X, c_{m}}\left(z w_{m}\right)$ where $c_{m} \in H_{2}(X ; \mathbf{Z})$ is supported in $C_{p}, m=(p-1) t+b$, and $w_{m} \in \operatorname{Sym}_{t}\left(H_{2}\left(C_{p} ; \mathbf{Z}\right)\right)$ depending only on $m$ and $p$. First we obtain $c_{m}$. Let $e_{m} \in H^{2}\left(C_{p} ; \mathbf{Z}\right)$ be the Poincaré dual of $\langle t, t+1 ; b\rangle$. By Lemma 5.8 we can find $c_{m} \in H_{2}\left(C_{p} ; \mathbf{Z}\right) \subset H_{2}(X ; \mathbf{Z})$ such that $\iota_{*}\left(c_{m}\right) \equiv\langle t, t+1 ; b\rangle(\bmod 2)$. Thus the Poincaré dual of $c_{m}$ in $H^{2}(X ; \mathbf{Z})$ restricts to $C_{p}$ congruent to $e_{m}(\bmod 2)$ and restricts trivially to $X^{*}$. A dimension counting argument shows that in the formalism of Taubes [T1], $D_{X, c_{m}}\left(z w_{m}\right)$ is the sum of terms of the form
$$\int_{\tilde{\mathcal{M}}_{X^{*}}\left[\eta^{j}\right] \times_{j} \tilde{\mathcal{M}}_{C_{p}, \epsilon, \ell}} \tau \wedge \tilde{\mu}(z) \wedge \tilde{\mu}\left(w_{m}\right) .$$
In this formula, $\tilde{\mathcal{M}}_{C_{p}, \epsilon, \ell}$ is the based moduli space of exponentially decaying asymptotically flat anti-self-dual connections on the $S O(3)$ bundle $E_{\epsilon, \ell}$ which is obtained from the reducible bundle $L_{\epsilon} \oplus \mathbf{R}$ by grafting in $\ell$ instanton bundles. (The euler class of $L_{\epsilon}$ is $\epsilon, \partial \epsilon=j, \epsilon \equiv e_{m}(\bmod 2)$, and $\operatorname{dim} \mathcal{M}_{\epsilon}+8 \ell \leq 2 t-1$.) The notation ' $\times_{j}$ ' in the formula denotes the fiber product with respect to the $\operatorname{SO}(3)$-equivariant boundary value maps
$$\partial_{C_{p}, \epsilon, \ell}: \tilde{\mathcal{M}}_{C_{p}, \epsilon, \ell} \rightarrow G[j], \quad \partial_{X^{*}}[j]: \tilde{\mathcal{M}}_{X^{*}}\left[\eta^{j}\right] \rightarrow G[j]$$
where $G[j] \subset \operatorname{SO}(3)$ is the conjugacy class $\eta^{j}$ of representations of $\pi_{1}\left(L\left(p^{2}, 1-p\right)\right)$ to $\operatorname{SO}(3)$. If $j \neq 0, p^{2} / 2$ then $G[j]$ is a 2-sphere, $G[0]=\{I\}$, and, in case $p$ is even, $G\left[p^{2} / 2\right] \cong \mathbf{R} \mathbf{P}^{2}$. Also, $\tau$ denotes a 3-form which integrates to 1 over the fibers of the basepoint fibration $\beta_{X^{*}, j}$ i.e. $\tilde{\mathcal{M}}_{X^{*}}\left[\eta^{j}\right] \rightarrow$ $\mathcal{M}_{X^{*}}\left[\eta^{j}\right]$. The form $\tilde{\mu}\left(w_{m}\right)$ is supported near the orbit of the reducible connection corresponding to $\epsilon$. (If $\ell>0$, this reducible connection lies in the Uhlenbeck compactification of $\mathcal{M}_{C_{p}, \epsilon, \ell}$.) The principal $S O(3)$ bundle $\beta_{X^{*}, j}$ has a reduction to a bundle with structure group $S^{1}$. As in [FS3, §4], we let $\varepsilon \in H^{2}\left(\mathcal{M}_{X^{*}}\left[\eta^{j}\right]\right)$ denote the euler class of this $S^{1}$ bundle.

The upshot of Taubes' work cited above is that there is a form $\tilde{\mu}\left(w_{m}\right)$ representing a class $\mu_{S O(3)}\left(w_{m}\right)$ in the $S O(3)$-equivariant cohomology of an enlargement of $\tilde{\mathcal{M}}_{C_{p}, \epsilon, \ell}$. The lift $\tilde{\mu}(z)$ defines an element of the equivariant cohomology $H_{S O(3)}^{2 d}\left(\tilde{\mathcal{M}}_{X^{*}}\left[\eta^{j}\right]\right)$. Furthermore, Taubes has shown that
the push-forward $\left(\partial_{C_{p}, \epsilon, \ell}\right)_{*}$ is well-defined, and
$$\int_{\tilde{\mathcal{M}}_{X^{*}}\left[\eta^{j}\right]_{\times_{j}} \tilde{\mathcal{M}}_{C_{p}, \epsilon, \ell}} \tau \wedge \tilde{\mu}(z) \wedge \tilde{\mu}\left(w_{m}\right)=\int_{\tilde{\mathcal{M}}_{X^{*}}\left[\eta^{j}\right]} \tau \wedge \tilde{\mu}(z) \wedge\left(\partial_{X^{*}}[j]\right)^{*}\left(\partial_{C_{p}, \epsilon, \ell}\right)_{*}\left(\tilde{\mu}\left(w_{m}\right)\right)$$
where $\left(\partial_{X^{*}}[j]\right)^{*}$ denotes pullback in equivariant cohomology.
For $j=0, \partial_{C_{p}, \epsilon, \ell}: \tilde{\mathcal{M}}_{C_{p}, \epsilon, \ell} \rightarrow\{1\}$, has fiber dimension equal to $\operatorname{dim} \tilde{\mathcal{M}}_{C_{p}, \epsilon, \ell}=4 k+8 \ell$ for some $k \geq$ 0 . The cohomology class of $\left(\partial_{C_{p}, \epsilon, \ell}\right)_{*}\left(\tilde{\mu}\left(w_{m}\right)\right)$ lies in $H_{S O(3)}^{2 t-4 k-8 \ell}(\{1\} ; \mathbf{R})=H^{2 t-4 k-8 \ell}(B S O(3) ; \mathbf{R})$ which is a polynomial algebra on the 4-dimensional class $\wp$, which pulls back over $\tilde{\mathcal{M}}_{X^{*}}\left[\eta^{j}\right]$ as $p_{1}\left(\beta_{X^{*}, j}\right)$. For $j \neq 0, p^{2} / 2$, let $j=t_{j}(p-1)+b_{j}$ where $1 \leq b_{j} \leq p-1$. Then $\partial_{C_{p}, \epsilon, \ell}: \tilde{\mathcal{M}}_{C_{p}, \epsilon, \ell} \rightarrow G[j]$ has fiber dimension $2 t_{j}+2+8 \ell+4 k-2$ for some $k \geq 0$; so the cohomology class of $\left(\partial_{C_{p}, \epsilon, \ell}\right) *\left(\tilde{\mu}\left(w_{m}\right)\right)$ lies in $H_{S O(3)}^{2\left(t-t_{j}\right)-8 \ell-4 k}\left(S^{2} ; \mathbf{R}\right)=H^{2\left(t-t_{j}\right)-8 \ell-4 k}\left(\mathbf{C P}^{\infty} ; \mathbf{R}\right)$. Let $v$ be the 2-dimensional generator of $H^{*}\left(\mathbf{C P}^{\infty} ; \mathbf{R}\right)$. The pullback $\left(\partial_{X^{*}}[j]\right)^{*}(v)=\varepsilon$. Using the fact that $\varepsilon^{2}=p_{1}\left(\beta_{X^{*}, j}\right)$, and arguing as in [FS3, Prop.4.5,4.6] we get
$$D_{X, c_{m}}\left(z w_{m}\right)=\sum_{t_{j} \equiv t(2)} \sum_{q} r_{m, j, q} D_{X^{*}}\left[\eta^{j}\right]\left(z x^{q}\right)+\sum_{\substack{t_{j} \not \equiv t(2) \\ j \neq 0}} \sum_{q} r_{m, j, q}^{\prime} D_{X^{*}}\left[\eta^{j}\right]\left(z x^{q} \varepsilon\right) .$$
The notation $D_{X^{*}}\left[\eta^{j}\right]\left(z x^{q} \varepsilon\right)$ is not standard, but its meaning is clear. It follows from Proposition 5.6 that the $\eta^{j}$ in (6) have $j \leq m$; so this bounds $j$ in both terms. We emphasize that in order to obtain $r_{m, j, q}$ or $r_{m, j, q}^{\prime} \neq 0$ we must have an $\epsilon \in H^{2}\left(C_{p} ; \mathbf{Z}\right)$ satisfying $\partial^{\prime} \epsilon=j, \epsilon \equiv e_{m}(\bmod 2)$, and $\operatorname{dim} \mathcal{M}_{\epsilon}+8 q \leq 2 t-1$.

Assume inductively that:
\begin{itemize}
\item[a)] For each $j<m\left(j \equiv 0(\bmod 2)\right.$ if $p$ is even) there are classes $w_{j, i} \in \operatorname{Sym}_{*}\left(H_{2}\left(C_{p} ; \mathbf{Z}\right)\right)$ and rational numbers $a_{j, i}$ satisfying
$$D_{X^{*}}\left[\eta^{j}\right](z)=\sum_{i=1}^{j} a_{j, i} D_{X, c_{i}}\left(z w_{j, i}\right)$$
\item[b)] For each $j$ with $t_{j}<t-1($ and $j \equiv 0(\bmod 2)$ if $p$ is even $)$ there are classes $w_{j, i}^{\prime} \in$ $\operatorname{Sym}_{*}\left(H_{2}\left(C_{p} ; \mathbf{Z}\right)\right)$ and rational numbers $a_{j, i}^{\prime}$ satisfying
$$D_{X^{*}}\left[\eta^{j}\right](z \varepsilon)=\sum_{i=1}^{j} a_{j, i} D_{X, c_{i}}\left(z w_{j, i}^{\prime}\right)$$
\end{itemize}
for all $z \in \mathbf{A}\left(X^{*}\right)$, and the coefficients $a_{j, i}, a_{j, i}^{\prime}$ are independent of $z$ and $X$.
Recall that we are writing $m=(t-1) p+b$ with $1 \leq b \leq p-1$, and let $e_{m}$ be the Poincaré dual of $\langle t, t+1 ; b\rangle=(t+1) \gamma_{p-1}-\gamma_{p-1-b}$. Also, we suppose that $m$ is even if $p$ is even. We set
$$w_{m}=\left(u_{p-1}-(t-1) u_{p-1-b}\right) \cdot\left(u_{p-1}\right)^{t-1} \in \mathbf{A}\left(C_{p}\right) .$$

We wish to calculate $D_{X, c_{m}}\left(z w_{m}\right)$ using (6). For $j=m$ in this formula, we need to compute $\left(\partial_{C_{p}, e_{m}, 0}\right)_{*}\left(\tilde{\mu}\left(w_{m}\right)\right) \in H_{S O(3)}^{0}(G[m] ; \mathbf{R})=\mathbf{R}$ since $t_{m}=t$. In fact,
$$\begin{aligned}
\left(\partial_{C_{p}, e_{m}, 0}\right)_{*}\left(\tilde{\mu}\left(w_{m}\right)\right) & =r_{m, m, 0} \\
& =-\frac{1}{2}\left\langle u_{p-1}-(t-1) u_{p-1-b}, e_{m}\right\rangle\left(-\frac{1}{2}\left\langle u_{p-1}, e_{m}\right\rangle\right)^{t-1}=\left(-\frac{1}{2}\right)^{t}(2 t)(t+1)^{t-1} \neq 0
\end{aligned}$$
(cf. [DK, p.187]). In (6), $r_{m, m, 0} D_{X^{*}}\left[\eta^{m}\right](z)$ is the only term which involves the boundary value $\eta^{m}$. If $j$ is the boundary value of an $\epsilon$ with $\epsilon \equiv e_{m}(\bmod 2)$, and $\operatorname{dim} \mathcal{M}_{\epsilon}+8 q \leq 2 t-1$, and if $t_{j}=t-1$, then by Corollary 5.7 and Lemma 5.5, $\epsilon$ must be a permutation of $\langle t-1, t ; p-1-b\rangle=t \gamma_{p-1}-\gamma_{b}$. In fact $\epsilon \equiv e_{m}(\bmod 2)$ implies that $\epsilon=\langle t, t-1 ; b\rangle=(t-1) \gamma_{p-1}+\gamma_{p-1-b}$. So $j=(t-1)(p-1)+(p-1-b)$. Hence $\left\langle u_{p-1}-(t-1) u_{p-1-b}, \epsilon\right\rangle=0$. Thus, no such $j$ occurs in the second sum of the expansion (6) for $D_{X, c_{m}}\left(z w_{m}\right)$. (I.e. for such $j$, necessarily $q=0$ and $r_{m, j, q}^{\prime}=0$.) Finally, if $p$ is even, then we are assuming that $m$ is also even. If $r_{m, i, q}$ or $r_{m, i, q}^{\prime} \neq 0$ then as above there is an $\epsilon$ with $\partial \epsilon=i$ and $\epsilon \equiv e_{m}(\bmod 2)$; so for
$$\partial_{2}: H_{2}\left(C_{p}, \partial ; \mathbf{Z}_{2}\right) \rightarrow H_{1}\left(L\left(p^{2}, 1-p\right) ; \mathbf{Z}_{2}\right)=\mathbf{Z}_{2}$$
$j \equiv \partial_{2}(\epsilon) \equiv \partial_{2} e_{m} \equiv m(\bmod 2)$. Accordingly, all the other terms in (6) are given inductively by (7) and (8), and the powers of $x$ can be removed using the hypothesis that $X$ has simple type. Since the coefficient of $D_{X^{*}}\left[\eta^{m}\right](z)$ is nonzero, we may solve for it, completing the induction step for (7).

For (8), we show how to compute $D_{X^{*}}\left[\eta^{m^{\prime}}\right](z \varepsilon)$ for $m^{\prime}=(t-1)(p-1)+(p-1-b)$ as required. Thus after completing the inductive step for each $t(p-1)+c, 1 \leq c \leq p-1$, we will have completed the calculation of $D_{X^{*}}\left[\eta^{j}\right](z \varepsilon)$ for all $j=(t-1) p+a, 1 \leq a \leq p-1$. So to calculate $D_{X^{*}}\left[\eta^{m^{\prime}}\right](z \varepsilon)$ and thus complete the induction, we calculate $D_{X, c_{m}}\left(z w_{m^{\prime}}^{\prime}\right)$ where $w_{m^{\prime}}^{\prime}=\left(u_{p-1}+(t+1) u_{p-1-b}\right) \cdot$ $\left(u_{p-1}+(t-1) u_{p-1-b}\right) \cdot\left(u_{p-1}\right)^{t-2}$. Using (6)
$$D_{X, c_{m}}\left(z w_{m^{\prime}}^{\prime}\right)=\sum_{t_{j} \equiv t(2)} \sum_{q} s_{m^{\prime}, j, q} D_{X^{*}}\left[\eta^{j}\right]\left(z x^{q}\right)+\sum_{\substack{t_{j} \neq t(2) \\ j \neq 0}} \sum_{q} s_{m^{\prime}, j, q}^{\prime} D_{X^{*}}\left[\eta^{j}\right]\left(z x^{q} \varepsilon\right) .$$
Computing as above, we see that $s_{m^{\prime}, m^{\prime}, 0}=0$. What we need to see is that $s_{m^{\prime}, m^{\prime}, 0}^{\prime} \neq 0$. By the argument of the above paragraph, $m^{\prime}$ is the only possible boundary value not covered by the induction step. Let $\epsilon=(t-1) \gamma_{p-1}+\gamma_{p-1-b}$. This is the only euler class that can give boundary value $m^{\prime}$ in (9). Then
$$\left(\partial_{C_{p}, \epsilon, 0}\right)_{*}\left(\tilde{\mu}\left(w_{m}^{\prime}\right)\right) \in H_{S O(3)}^{2}\left(S^{2} ; \mathbf{R}\right) \cong H_{S O(3)}^{2}\left(G\left[m^{\prime}\right] ; \mathbf{R}\right)=\mathbf{R}$$
and $\left(\partial_{C_{p}, \epsilon, 0}\right)_{*}\left(\tilde{\mu}\left(w_{m}^{\prime}\right)\right)=\left(-\frac{1}{2}\right)^{t-1} 2 t(2 t-2)(t-1)^{t-2} v$ which pulls back over $\tilde{\mathcal{M}}_{X^{*}}\left[\eta^{j}\right]$ as $\left(-\frac{1}{2}\right)^{t-3} t(t-$ $1)(t-1)^{t-2} \varepsilon$. This means that we can solve (9) for $D_{X^{*}}\left[\eta^{m^{\prime}}\right](z \varepsilon)$, completing the induction and the proof of Theorem 5.1.

The argument above shows that all of the relative invariants $D_{X^{*}}\left[\eta^{n p}\right]$ can be expressed in terms of absolute invariants of $X$. Since we are assuming that $X$ has simple type, it follows that each of the relative invariants satisfies the formula
$$D_{X^{*}}\left[\eta^{n p}\right]\left(z x^{2}\right)=4 D_{X^{*}}\left[\eta^{n p}\right](z) .$$

Hence it follows from (4) that:
Corollary 5.9. Let $X_{p}$ be the result of rationally blowing down $C_{p} \subset X$. If $X$ has simple type, then so does $X_{p}$. \(\square\)

Now we shall make stronger use of the hypothesis that $X$ has simple type. By [KM1, FS3] we can write
$$\begin{aligned}
\mathbf{D}_{X} & =\exp \left(Q_{X} / 2\right) \sum_{s=1}^{n} a_{s} e^{\kappa_{s}} \\
\mathbf{D}_{X, c} & =\exp \left(Q_{X} / 2\right) \sum_{s=1}^{n}(-1)^{\frac{1}{2}\left(c^{2}+c \cdot \kappa_{s}\right)} a_{s} e^{\kappa_{s}}
\end{aligned}$$
for nonzero rational numbers $a_{s}$ and basic classes $\kappa_{1}, \ldots, \kappa_{n} \in H_{2}(X ; \mathbf{Z})$. Here $Q_{X}$ is the intersection form of $X$. Now
$$\partial_{u}\left(\exp \left(Q_{X} / 2\right) e^{\kappa}\right)=\exp \left(Q_{X} / 2\right)(\tilde{u}+\kappa \cdot u) e^{\kappa}$$
where $\tilde{u}: H_{2}(X) \rightarrow \mathbf{R}$ is $\tilde{u}(\alpha)=u \cdot \alpha$ and $\partial_{v} \tilde{u}=v \cdot u$. Apply Theorem 5.1: since all derivatives are taken with respect to classes $u \in H_{2}\left(C_{p} ; \mathbf{Z}\right)$, after all derivatives are taken, the remaining $\tilde{u}$ 's restricted to $X^{*}$ vanish. Hence,
$$\left.\mathbf{D}_{X_{p}}\right|_{X^{*}}=\left.\exp \left(Q_{X^{*}} / 2\right) \sum_{s=1}^{n} a_{s} b_{s} e^{\kappa_{s}}\right|_{X^{*}}=\exp \left(Q_{X^{*}} / 2\right) \sum_{s=1}^{n} a_{s} b_{s} e^{\kappa_{s}^{\prime}}$$
where $\kappa_{s}^{\prime}=\left.\kappa_{s}\right|_{X^{*}}=\operatorname{PD}\left(i^{*}\left(\operatorname{PD}\left(\kappa_{s}\right)\right)\right) \in H_{2}\left(X^{*}, \partial ; \mathbf{Z}\right)$, where PD denotes Poincaré duality, $i$ is the inclusion $X^{*} \subset X$, and $b_{s}$ depends only on the intersection numbers of $\kappa_{s}$ with the generators $u_{i}$ of $H_{2}\left(C_{p} ; \mathbf{Z}\right)$.

Lemma 5.10. If $b_{s} \neq 0$ in (10) then
$$\partial \kappa_{s}^{\prime} \in p \mathbf{Z}_{p^{2}} \subset H_{1}\left(L\left(p^{2}, 1-p\right) ; \mathbf{Z}\right)=\mathbf{Z}_{p^{2}} .$$
Proof. Corollary 5.9 implies that $X_{p}$ has simple type. We thus have
$$\mathbf{D}_{X_{p}}=\exp \left(Q_{X_{p}} / 2\right) \sum_{r=1}^{m} c_{r} e^{\lambda_{r}}$$
where the basic classes of $X_{p}$ are $\lambda_{1}, \ldots, \lambda_{m}$. Restrict $\mathbf{D}_{X_{p}}$ to $X^{*}$ and compare the restrictions of $\exp \left(Q_{X_{p}} / 2\right)^{-1} \mathbf{D}_{X_{p}}$ in (10) and (11). Since for distinct $\alpha \in H_{2}\left(X^{*}, \partial ; \mathbf{Z}\right)$ the functions $e^{\alpha}:$ $H_{2}\left(X^{*}\right) \rightarrow \mathbf{R}$ are linearly independent, it follows that if $b_{s} \neq 0$, then $\kappa_{s}^{\prime}=\left.\lambda_{i}\right|_{X^{*}}$ for some $i$. Thus $\kappa_{s}^{\prime}$ extends over $B_{p}$, and hence $\partial \kappa_{s}^{\prime} \in p \mathbf{Z}_{p^{2}}$. \(\square\)

As a result, we have the following restatement of Theorem 5.1.
Theorem 5.11. Suppose that $X$ has simple type and
$$\mathbf{D}_{X}=\exp \left(Q_{X} / 2\right) \sum_{s=1}^{n} a_{s} e^{\kappa_{s}} .$$

Let $C_{p} \subset X$ and let $X_{p}$ be its rational blowdown. Let $\left\{\kappa_{t} \mid t=1, \ldots, m\right\}$ be the basic classes of $X$ which satisfy $\partial \kappa_{t}^{\prime} \in p \mathbf{Z}_{p^{2}}$, and for each $t$, let $\bar{\kappa}_{t}$ be the unique extension of $\kappa_{t}^{\prime}$. Then
$$\mathbf{D}_{X_{p}}=\exp \left(Q_{X_{p}} / 2\right) \sum_{t=1}^{m} a_{t} b_{t} e^{\bar{\kappa}_{t}}$$
where the $b_{t}$ depend only on the intersection numbers $u_{i} \cdot \kappa_{t}, i=1, \ldots, p-1$. \(\square\)

\section*{6. The Donaldson Invariant of Elliptic Surfaces}

In this section we shall compute the result on the Donaldson series of performing log transforms. The Donaldson invariants of the elliptic surfaces $E(n), n \geq 2$ without multiple fibers have been known for some time. There is a complete calculation in [FS3], for example. For $n \geq 2$ :
$$\mathbf{D}_{E(n)}=\exp (Q / 2) \sinh ^{n-2}(f)$$
where $f$ is the class of a fiber. In this notation, the $K 3$ surface is $E(2)$. As in Theorem 3.1, let $X=E(2) \#(p-1) \overline{\mathbf{C P}}^{2}$, and let $X_{p}$ be the rational blowdown of $C_{p} \subset X$, so that $X_{p} \cong E(2 ; p)$. Since $\mathbf{D}_{E(2)}=\exp (Q / 2)$, the blowup formula [FS2] yields
$$\mathbf{D}_{X}=\frac{1}{2^{p-1}} \exp (Q / 2) \sum_{J} \exp \left(\sum_{i=1}^{p-1} \epsilon_{J, i} e_{i}\right)$$
where the outer sum is taken over all $J=\left(\epsilon_{J, 1}, \ldots, \epsilon_{J, p-1}\right) \in\{ \pm 1\}^{p-1}$. The basic classes of $X$ are $\left\{\kappa_{J}=\sum \epsilon_{J, i} e_{i}\right\}$, and applying Theorem 5.11 we get
$$\mathbf{D}_{X_{p}}=\frac{1}{2^{p-1}} \exp \left(Q_{X_{p}} / 2\right) \sum_{J} b_{J} e^{\bar{\kappa}_{J}}$$
where $\bar{\kappa}_{J} \in H_{2}\left(X_{p} ; \mathbf{Z}\right)$ is the unique extension of $\left.\kappa_{J}\right|_{X^{*}}$. Recall that the spheres of the configuration $C_{p}$ represent homology classes $u_{i}=e_{p-(i+1)}-e_{p-i}$ for $1 \leq i \leq p-2$, and $u_{p-1}=f-2 e_{1}-e_{2}-$ $\cdots-e_{p-1}$. In $X_{p}$ we have the multiple fiber $f_{p}=f / p$.

Proposition 6.1. $\bar{\kappa}_{J}=|J| \cdot f_{p}$ where $|J|=\sum_{i=1}^{p-1} \epsilon_{J, i}$.

Proof. First we find a class $\zeta \in H_{2}\left(C_{p} ; \mathbf{Q}\right)$ so that $\left(\kappa_{J}+\zeta\right) \cdot u_{i}=0$ for each $i$. This means that $\kappa_{J}+\zeta \in H_{2}\left(X^{*} ; \mathbf{Q}\right)$, and as dual forms: $H_{2}\left(X^{*} ; \mathbf{Z}\right) \rightarrow \mathbf{Z},\left.\kappa_{J}\right|_{X^{*}}=\kappa_{J}+\zeta$. To find $\zeta$ we need to solve the linear system
$$\left(\kappa_{J}+\sum x_{i} u_{i}\right) \cdot u_{j}=0, \quad j=1, \ldots, p-1 .$$
We begin by rewriting these equations. Let $\left\{\omega_{i}\right\}$ be a standard basis for $\mathbf{Q}^{p-1}$, and let $A$ be the $(p-1) \times(p-1)$ matrix whose $i$ th row vector is
$$\begin{aligned}
A_{i} & =\omega_{p-(i+1)}-\omega_{p-i}, \quad i=1, \ldots, p-2 \\
A_{p-1} & =-2 \omega_{1}-\omega_{2}-\cdots-\omega_{p-1} .
\end{aligned}$$

We have $u_{i}=A^{t}\left(\omega_{i}\right) \cdot \mathbf{e}$ and $u_{p-1}=f+A^{t}\left(\omega_{p-1}\right) \cdot \mathbf{e}$, where $\mathbf{e}=\left(e_{1}, \ldots, e_{p-1}\right)$. Our linear system is equivalent to
$$P \mathbf{x}=A \boldsymbol{\epsilon}_{J}$$
where $\mathbf{x}=\left(x_{1}, \ldots, x_{p-1}\right)$ and $\boldsymbol{\epsilon}_{J}=\left(\epsilon_{J, 1}, \ldots, \epsilon_{J, p-1}\right)$. (The matrix $P$ is the plumbing matrix for $C_{p}$.) Hence $\mathbf{x}=P^{-1} A \boldsymbol{\epsilon}_{J}$.

We claim that $P\left(A^{t}\right)^{-1}=-A$. This can be checked on the basis
$$\left\{\omega_{2}-\omega_{1}, \ldots, \omega_{p-1}-\omega_{p-2}, \omega_{p-1}\right\}$$
using
$$\begin{aligned}
A\left(\omega_{i}\right) & =-\omega_{p-1}-\omega_{p-(i+1)}+\omega_{p-i}, 2 \leq i \leq p-1 \quad\left(\omega_{0}=0\right), \\
A\left(\omega_{1}\right) & =-2 \omega_{p-1}+\omega_{p-2}, \\
P\left(\omega_{i}\right) & =\omega_{i+1}-2 \omega_{i}+\omega_{i-1}, i \neq p-1, \\
P\left(\omega_{p-1}\right) & =-(p+2) \omega_{p-1}+\omega_{p-2} .
\end{aligned}$$

It follows that $A^{t} P^{-1} A=-I$. Thus
$$\kappa_{J}+\zeta=\kappa_{J}+\sum x_{i} u_{i}=\left(\epsilon_{J}+A^{t} \mathbf{x}\right) \cdot \mathbf{e}+x_{p-1} f=\left(\boldsymbol{\epsilon}_{J}-\boldsymbol{\epsilon}_{J}\right) \cdot \mathbf{e}+x_{p-1} f=x_{p-1} f .$$
To compute $x_{p-1}$ note that
$$A \boldsymbol{\epsilon}_{J}=\left(\epsilon_{J, p-2}-\epsilon_{J, p-1}, \epsilon_{J, p-3}-\epsilon_{J, p-2}, \ldots, \epsilon_{J, 1}-\epsilon_{J, 2},-2 \epsilon_{J, 1}-\epsilon_{J, 2}-\cdots-\epsilon_{J, p-1}\right)$$
so that if $\left(P^{-1}\right)_{p-1}$ denotes the bottom row of $P^{-1}$ :
$$x_{p-1}=\left(P^{-1}\right)_{p-1}\left(A \boldsymbol{\epsilon}_{J}\right)=-\frac{1}{p^{2}}(1,2, \ldots, p-1) \cdot\left(A \epsilon_{J}\right)=\frac{1}{p} \sum \epsilon_{J, i}=\frac{1}{p}|J| .$$
Thus $\left.\kappa_{J}\right|_{X^{*}}=\kappa_{J}+\zeta=\frac{1}{p}|J| f$ as forms: $H_{2}\left(X^{*} ; \mathbf{Z}\right) \rightarrow \mathbf{Z}$. The homology class $\kappa_{J}+\zeta$ is in fact an integral class $\bar{\kappa}_{J}=|J| f_{p} \in H_{2}\left(X_{p} ; \mathbf{Z}\right)$ which is the unique extension of $\left.\kappa_{J}\right|_{X^{*}}$ \(\square\)

In an arbitrary smooth 4-manifold $X$, define a nodal fiber to be an immersed 2-sphere $S$ with one singularity, a positive double point, such that the regular neighborhood of $S$ is diffeomorphic to the regular neighborhood of a nodal fiber in an elliptic surface. (There need not be any associated ambient fibration of $X$.) Given such a nodal fiber $S$, one can perform a 'log transform' of multiplicity $p$ by blowing up to get $C_{p} \subset X \#(p-1) \overline{\mathbf{C P}}^{2}$ with $u_{p-1}=S-2 e_{1}-e_{2}-\cdots-e_{p-1}$, and then blowing down $C_{p}$. We denote the result of this process by $X_{p}$.

Throughout, we use the following notation. If $X$ has simple type, and
$$\mathbf{D}_{X}=\exp (Q / 2) \sum a_{s} e^{\kappa_{s}},$$
then we write $\mathbf{K}_{X}=\sum a_{s} e^{\kappa_{s}}$.

Proposition 6.2. Let $S$ be a nodal fiber which satisfies $S \cdot \lambda_{j}=0$ for each basic class $\lambda_{j}$ of $X$. Then
$$\mathbf{D}_{X_{p}}= \begin{cases}\exp \left(Q_{X_{p}} / 2\right) \mathbf{K}_{X} \cdot\left(b_{p, 0}+\sum_{i=1}^{\frac{p-1}{2}} b_{p, 2 i}\left(e^{2 i S / p}+e^{-2 i S / p}\right)\right), & p \text { odd } \\ \exp \left(Q_{X_{p}} / 2\right) \mathbf{K}_{X} \cdot\left(\sum_{i=1}^{\frac{p}{2}} b_{p, 2 i-1}\left(e^{(2 i-1) S / p}+e^{-(2 i-1) S / p}\right)\right), & p \text { even }\end{cases}$$
where the coefficients $b_{p, j}$ depend only on $p$, not on $X$.
Proof. The Donaldson series of $X \#(p-1) \overline{\mathbf{C P}}^{2}$ is
$$\frac{1}{2^{p-1}} \mathbf{D}_{X} \cdot \exp \left(Q_{(p-1)} \overline{\mathbf{C P}}^{2} / 2\right) \sum_{J} \exp \left(\sum_{i=1}^{p-1} \epsilon_{J, i} e_{i}\right) .$$
Theorem 5.1 states that $\mathbf{D}_{X_{p}}$ is obtained from this by applying a differential operator which by hypothesis evaluates trivially on $\mathbf{D}_{X}$. The proposition now follows from (13) and Propostion 6.1 by the Leibniz rule. (That the coefficients of $e^{m p}$ and $e^{-m p}$ are equal follows from the fact that $\mathbf{D}_{E(2 ; p)}$ is an even function.) \(\square\)

Proposition 6.3. The Donaldson series of the simply connected elliptic surface $E(n ; 2)$ with $p_{g}=$ $n-1(>0)$ and one multiple fiber of multiplicity 2 is
$$\mathbf{D}_{E(n ; 2)}=\exp (Q / 2) \frac{\sinh ^{n-1}(f)}{\sinh \left(f_{2}\right)} .$$
Proof. According to Theorem 3.1, we obtain $E(n ; 2)$ from $E(n) \# \overline{\mathbf{C P}}^{2}$ by blowing down the sphere of square -4 representing $f-2 e$. We have $\mathbf{D}_{E(n) \# \overline{\mathbf{C P}}^{2}}=\exp (Q / 2) \sinh ^{n-2}(f) \cosh (e)$. Lemma 5.2 gives
$$\left.\mathbf{D}_{E(n ; 2)}\right|_{X^{*}}=\left.\left(\mathbf{D}_{E(n) \#} \overline{\mathbf{C P}}^{2}-\mathbf{D}_{E(n) \#} \overline{\mathbf{C P}}^{2}, f-2 e\right)\right|_{X^{*}}=\left.2 \exp (Q / 2) \sinh ^{n-2}(f) \cosh (e)\right|_{X^{*}}$$
(cf. [KM2], [FS3, Thm.5.13]). By Proposition 6.1
$$\mathbf{D}_{E(n ; 2)}=2 \exp (Q / 2) \sinh ^{n-2}(f) \cosh \left(f_{2}\right)=\exp (Q / 2) \frac{\sinh ^{n-1}(f)}{\sinh \left(f_{2}\right)} .$$ \(\square\)

Proposition 6.2 now implies:
Corollary 6.4. If $S$ is a nodal fiber in $X$ orthogonal to all basic classes and $X_{2}$ is the multiplicity 2 log transform of $X$ formed from $S$, then
$$\mathbf{D}_{X_{2}}=\exp \left(Q_{X_{2}} / 2\right) \mathbf{K}_{X} \cdot\left(e^{S / 2}+e^{-S / 2}\right) .$$ \(\square\)

Lemma 6.5. Let $X$ contain a nodal fiber $S$ orthogonal to all basic classes. Then the sum of the coefficients $b_{p, j}$ in the expression for $\mathbf{D}_{X_{p}}$ in Proposition 6.2 is equal to $p$.

Proof. In Example 3 we showed that there is a configuration $C_{p}^{\prime} \subset X \#(p-1) \overline{\mathbf{C P}}^{2}=Y$ where $u_{i}^{\prime}=e_{p-(i+1)}-e_{p-i}$ for $i=1, \ldots, p-2$, and $u_{p-1}^{\prime}=-2 e_{1}-e_{2}-\cdots-e_{p-1}$ such that the rational blowdown $Y_{p}=X \# H_{p}$ where $H_{p}$ is a homology 4-sphere with $\pi_{1}=\mathbf{Z}_{p}$. It follows easily that $\mathbf{D}_{Y_{p}}=p \cdot \mathbf{D}_{X}$.

As above, we let $\kappa_{J}=\sum \epsilon_{J, i} e_{i}, J \in\{ \pm 1\}^{p-1}$; so
$$\mathbf{D}_{Y}=\frac{1}{2^{p-1}} \mathbf{D}_{X} \cdot \exp \left(Q_{(p-1) \overline{\mathbf{C P}}^{2}} / 2\right) \sum_{J} e^{\kappa_{J}} .$$
All partial derivatives of $\mathbf{D}_{X}$ with respect to classes in $H_{2}\left(C_{p}^{\prime}\right)$ are trivial; so
$$p \mathbf{D}_{X}=\mathbf{D}_{Y_{p}}=\mathbf{D}_{X} \cdot \sum_{J} b_{J} e^{\bar{\kappa}_{J}} .$$
The proof of Proposition 6.1 shows that each $\bar{\kappa}_{J}=0$; so $\sum_{J} b_{J}=p$.
We can also form the configuration $C_{p} \subset Y$ whose blowdown is the $p$-log transform of the nodal fiber $S \subset X$. The configurations $C_{p}, C_{p}^{\prime}$ agree, $u_{i}=u_{i}^{\prime}$, except that $u_{p-1}=u_{p-1}^{\prime}+S$. However, since $S$ is orthogonal to all the basic classes of $X$, for all $i$, all intersections of $u_{i}$ and $u_{i}^{\prime}$ with all basic classes of $Y=X \#(p-1) \overline{\mathbf{C P}}^{2}$ agree. Thus, according to Theorem 5.11, the coefficients $b_{J}$ are the same coefficients that arise in the formula
$$\mathbf{D}_{X_{p}}=\exp \left(Q_{X_{p}} / 2\right) \mathbf{K}_{X} \sum_{J} c_{J} e^{|J| S / p} .$$
This means that the sum of the coefficients of the expression for $\mathbf{D}_{X_{p}}$ in Proposition 6.2 is $\sum_{J} b_{J}=$ $p$. \(\square\)

We next invoke Proposition 3.2 to see that if $p$ is any positive odd integer, then a multiplicity $2 p$ log transform can be obtained as the result of either a multiplicity $p \log$ transform on a nodal fiber of multiplicity 2 , or by a multiplicity 2 log transform on a nodal fiber of multiplicity $p$. Thus
$$\begin{aligned}
\mathbf{D}_{E(n ; 2 p)} & =\exp (Q / 2)\left(e^{f_{2}}+e^{-f_{2}}\right)\left(b_{p, 0}+\sum_{i=1}^{(p-1) / 2} b_{p, 2 i}\left(e^{2 i f_{2} / p}+e^{-2 i f_{2} / p}\right)\right) \\
& =\exp (Q / 2)\left(b_{p, 0}+\sum_{i=1}^{(p-1) / 2} b_{p, 2 i}\left(e^{2 i f_{p}}+e^{-2 i f_{p}}\right)\right)\left(e^{f_{p} / 2}+e^{-f_{p} / 2}\right)
\end{aligned}$$
since we already know the formula for a log transform of multiplicity 2 . We compare coefficients using $f_{2}=p f_{2 p}$ and $f_{p}=2 f_{2 p}$.

Assume for the sake of definiteness that $p \equiv 1(\bmod 4)$ and let $r=(p-1) / 4$. In the top expansion, the coefficient of $e^{ \pm p f_{2 p}}$ is $b_{p, 0}$ and $b_{p, 2 j}$ is the coefficient of $e^{ \pm(p+2 j) f_{2 p}}$ and $e^{ \pm(p-2 j) f_{2 p}}$. In the second expansion, the coefficient of $e^{ \pm f_{2 p}}$ is $b_{p, 0}$, and $b_{p, 2 j}$ is the coefficient of $e^{ \pm(4 j-1) f_{2 p}}$ and $e^{ \pm(4 j+1) f_{2 p}}$. To simplify notation, let $(m)_{1}$ be the coefficient of $e^{m f_{2 p}}$ in the top expansion and $(m)_{2}$ its coefficient
in the bottom expansion. Then,
$$\begin{aligned}
b_{p, 0}=(p)_{1} & =(p)_{2}=b_{p, 2 r}=(p-2)_{2}=(p-2)_{1}=b_{p, 2}=(p+2)_{1}=(p+2)_{2} \\
& =b_{p, 2(r+1)}=(p+4)_{2}=(p+4)_{1}=b_{p, 4}=(p-4)_{1}=(p-4)_{2} \\
& =b_{p, 2(r-1)}=(p-6)_{2}=(p-6)_{1}=b_{p, 6}=\cdots
\end{aligned}$$
and we see inductively that when $p$ is odd, all the $b_{p, 2 i}$ are equal. But by Lemma 6.5
$$b_{p, 0}+2 \sum_{i=1}^{(p-1) / 2} b_{p, 2 i}=p .$$
It follows that each $b_{p, 2 i}=1, i=0, \ldots,(p-1) / 2$.
Similarly, if $p$ is even, let $q=p-1$. Expanding $\mathbf{D}_{E(n ; p q)}$ we see that all $b_{p, 2 i-1}, i=1, \ldots, p / 2$ are equal; and so again each $b_{p, 2 i-1}=1$.

Theorem 6.6. Let $X$ be a 4-manifold of simple type and suppose that $X$ contains a nodal fiber $S$ orthogonal to all its basic classes. Then
$$\mathbf{D}_{X_{p}}=\exp \left(Q_{X_{p}} / 2\right) \mathbf{K}_{X} \cdot \frac{\sinh (S)}{\sinh (S / p)} .$$
Proof. If, e.g., $p$ is odd,
$$\begin{aligned}
\mathbf{D}_{X_{p}} & =\exp \left(Q_{X_{p}} / 2\right) \mathbf{K}_{X} \cdot(1+2 \cosh (2 S / p)+2 \cosh (4 S / p)+\cdots+2 \cosh ((p-1) S / p)) \\
& =\exp \left(Q_{X_{p}} / 2\right) \mathbf{K}_{X} \cdot \frac{\sinh (S)}{\sinh (S / p)} .
\end{aligned}$$ \(\square\)

As a result we have the calculation of the Donaldson series for all simply connected elliptic surfaces with $p_{g} \geq 1$.

Theorem 6.7. If $n \geq 2$ and $p, q \geq 1$ are relatively prime,
$$\mathbf{D}_{E(n ; p, q)}=\exp (Q / 2) \frac{\sinh ^{n}(f)}{\sinh \left(f_{p}\right) \sinh \left(f_{q}\right)} .$$ \(\square\)
This formula was originally conjectured by Kronheimer and Mrowka [KM1].
As an example of Theorem 6.6 consider $E(n)$. It follows from [GM] and [FS1] that in $E(n)$ there are 3 pairs of disjoint nodal fibers such that the nodal fibers in each pair are homologous, but give three linearly independent homology classes. Form $E\left(n ; p_{1}, q_{1} ; p_{2}, q_{2} ; p_{3}, q_{3}\right)$ by performing log transforms with each pair $\left\{p_{i}, q_{i}\right\}$ relatively prime. The resulting manifold is simply connected and,

Proposition 6.8. $\mathbf{D}_{E\left(n ; p_{1}, q_{1} ; p_{2}, q_{2} ; p_{3}, q_{3}\right)}=\exp (Q / 2) \frac{\sinh ^{n+4}(f)}{\prod_{i=1}^{3} \sinh \left(f_{p_{i}}\right) \sinh \left(f_{q_{i}}\right)}$. \(\square\)

Applying Theorem 6.7 and Proposition 6.8 to the manifolds $E\left(n ; p_{1}, q_{1} ; p_{2}, q_{2} ; p_{3}, q_{3}\right)$, we see that they do not admit complex structures with either orientation (cf.[GM],[FS1, Theorem 8.3]). The manifolds $E\left(2 ; p_{1}, q_{1} ; p_{2}, q_{2} ; p_{3}, q_{3}\right)$ are the Gompf-Mrowka fake K3-surfaces [GM].

\section*{7. Tautly Embedded Configurations}

Consider a 4-manifold $X$ of simple type containing the configuration $C_{p}$. By Theorem 4.2 for each 2-sphere $u_{i}$ in $C_{p}$ and each basic class $\kappa$ of $X$, we have
$$-2 \geq u_{i}^{2}+\left|u_{i} \cdot \kappa\right|$$
except in the special case described in Theorem 4.3 where $0 \geq u_{i}^{2}+\left|u_{i} \cdot \kappa\right|$. The only examples known where the special case arises are in blowups. This was the situation in the previous section where we studied log transforms. In this section, we assume that we are not in the special case. We say that a configuration is tautly embedded if (14) is satisfied for each $u_{i}$ of the configuration and each basic class $\kappa$ of $X$. Thus, if $C_{p}$ is tautly embedded, then for every basic class $\kappa, u_{i} \cdot \kappa=0$ for $i=1, \ldots, p-2$ and $\left|u_{p-1} \cdot \kappa\right| \leq p$.

Theorem 7.1. Suppose that $X$ is of simple type and contains the tautly embedded configuration $C_{p}$. If
$$\mathbf{D}_{X}=\exp \left(Q_{X} / 2\right) \sum a_{s} e^{\kappa_{s}}$$
then the rational blowdown $X_{p}$ satisfies
$$\mathbf{D}_{X_{p}}=\exp \left(Q_{X_{p}} / 2\right) \sum \bar{a}_{s} e^{\bar{\kappa}_{s}}$$
where
$$\bar{a}_{s}= \begin{cases}2^{p-1} a_{s}, & \left|u_{p-1} \cdot \kappa_{s}\right|=p \\ 0, & \left|u_{p-1} \cdot \kappa_{s}\right|<p\end{cases}$$
Furthermore, if $\left|u_{p-1} \cdot \kappa_{s}\right|=p$, then $\bar{\kappa}_{s}^{2}=\kappa_{s}{ }^{2}+(p-1)$.

Proof. If $\kappa_{s} \cdot u_{p-1} \neq 0, \pm p$ then $\bar{a}_{s}=0$ by Lemma 5.10. For $\kappa_{s} \cdot u_{p-1}=0, \kappa_{s} \neq 0$, note that since the $\kappa_{s}$ are characteristic, $p$ must be even. But then $\bar{\kappa}_{s}$ cannot even be characteristic in $X_{p}$, since $\bar{\kappa}_{s}^{2}=\kappa^{2}$ is not $\bmod 4$ congruent to $(3 \operatorname{sign}+2 e)\left(X_{p}\right)$. Thus, Theorem 5.11 implies that $\bar{a}_{s}=0$.

In case $\kappa_{s} \cdot u_{p-1}= \pm p$, we compare with the model for the order $p \log$ transforms of $E(2) ; C_{p}^{\prime \prime} \subset$ $Y=E(2) \#(p-1) \overline{\mathbf{C P}}^{2}$ which is blown down to obtain $Y_{p}=E(2 ; p)$. Again let $\lambda_{0}= \pm\left(e_{1}+\cdots+e_{p-1}\right)$; so by Lemma 6.1, $\pm \lambda_{0}$ are the unique basic classes of $Y_{p}$ satisfying $\pm \bar{\lambda}_{0}= \pm(p-1) f_{p} \in H_{2}\left(Y_{p} ; \mathbf{Z}\right)$. Now
$$\begin{aligned}
\mathbf{D}_{Y} & =\frac{1}{2^{p-1}} \exp (Q / 2) \sum \exp \left( \pm e_{1} \pm \cdots \pm e_{p-1}\right)=\exp (Q / 2) \sum_{J} \frac{1}{2^{p-1}} e^{\lambda_{J}} \\
\mathbf{D}_{Y_{p}} & =\exp (Q / 2) \sum_{\substack{|\ell| \leq p-1 \\
\ell \equiv p(\bmod 2)}} e^{\ell f_{p}}=\exp (Q / 2) \sum \frac{1}{2^{p-1}} b_{J} e^{\lambda_{J}}
\end{aligned}$$

Since $\pm \lambda_{0}$ are the unique $\lambda_{J}$ with $\bar{\lambda}_{0}= \pm(p-1) f_{p}$, the corresponding coefficient is $b_{0}=2^{p-1}$. We may now apply Theorem 5.11 to obtain our result since $\kappa_{s} \cdot u_{i}=\lambda_{0} \cdot u_{i}^{\prime \prime}$ for each $i$.

In order to compute $\bar{\kappa}_{s}^{2}$, we find $x_{i} \in \mathbf{Q}, i=1, \ldots, p-1$, such that
$$\kappa_{s}+\zeta=\kappa_{s}+\sum_{i=1}^{p-1} x_{i} u_{i} \in H_{2}\left(X^{*} ; \mathbf{Q}\right)$$
as in the proof of Proposition 6.1. We can solve for the $x_{i}$ using the model $C_{p}^{\prime \prime} \subset Y^{\prime \prime}$, and $\boldsymbol{\epsilon}_{J}=$ $\pm(1, \ldots, 1)$ in the proof of Proposition 6.1. Referring there, we get
$$\mathbf{x}=P^{-1} A \boldsymbol{\epsilon}_{J}=-\left(A^{t}\right)^{-1} \boldsymbol{\epsilon}_{J}= \pm \frac{1}{p}(1,2, \ldots, p-1) .$$
So $\zeta= \pm \sum \frac{i}{p} u_{i}$, and $\zeta^{2}=\mathbf{x} \cdot P \mathbf{x}=1-p$. Hence
$$\bar{\kappa}_{s}^{2}=\left(\kappa_{s}+\zeta\right)^{2}=\kappa_{s}^{2}+2 \kappa_{s} \cdot \zeta+\zeta^{2}=\kappa_{s}^{2}+(p-1) .$$ \(\square\)

Now consider the elliptic surface $E(1)$. It can be constructed by blowing up $\mathbf{C P}^{2}$ at the nine intersection points of a generic pencil of cubic curves. The fiber class of $E(1)$ is $f=3 h-e_{1}-\cdots e_{9}$ where $3 h$ is the class of the cubic in $H_{2}\left(\mathbf{C P}^{2} ; \mathbf{Z}\right)$. The nine exceptional curves are disjoint sections of the elliptic fibration. The elliptic surface $E(n)$ can be obtained as the fiber sum of $n$ copies of $E(1)$, and these sums can be made so that the sections glue together to give nine disjoint sections of $E(n)$, each of square $-n$. In particular, consider $E(4)$ with 9 disjoint sections of square -4. The basic classes of $E(4)$ are 0 and $2 f$; so we see that each of the 9 sections gives us a tautly embedded configuration $C_{2}$. Let $W_{n}$ be the rational blowdown of $n$ of these sections, $1 \leq n \leq 9$. For $n \leq 8$, $W_{n}$ is simply connected. Gompf has shown that all these manifolds admit symplectic structures, and it is not hard to see that $W_{2}$ is the 2-fold branched cover of $\mathbf{C P}^{2}$ branched over the octic curve [G2, §5.2].

Proposition 7.2. $\mathbf{D}_{W_{n}}=2^{n-1} \exp (Q / 2) \cosh \left(\kappa_{n}\right)$ where $\kappa_{n}^{2}=n$.

Proof. We have
$$\mathbf{D}_{E(4)}=\exp (Q / 2) \sinh ^{2}(f)=\exp (Q / 2)\left(\frac{1}{2} \cosh (2 f)+\frac{1}{2}\right) .$$
The basic classes $\pm 2 f$ intersect each section twice; so Theorem 7.1 implies that each $X_{n}$ has only the basic classes, $\pm \kappa_{n}$, and that each blowdown multiplies its coefficient by 2 and increases its square by 1 . (We start with coefficient $\frac{1}{2}$ and square 0.) \(\square\)

To further illustrate the utility of Theorem 7.1 we compute the Donaldson invariants of a family of Horikawa surfaces $\{H(n)\}$ with $c_{1}(H(n))^{2}=2 n-6$. To obtain $H(n)$, start with the simply connected ruled surface $\mathbf{F}_{n-3}$ whose negative section $s_{-}$has square $-(n-3)$. We have seen in the proof of Lemma 2.1 that the classes $s_{+}+f$ and $s_{-}$form a configuration in $\mathbf{F}_{n-3}$ whose regular neighborhood $D_{n-2}$ has complement the rational ball $B_{n-2}$. The Horikawa surface $H(n)$ is defined
to be the 2 -fold branched cover of $\mathbf{F}_{n-3}$ branched over a smoothing of $4\left(s_{+}+f\right)+2 s_{-}$. (Equivalently this is a smooth surface representing $(6, n+1)$ in $S^{2} \times S^{2}$.)

Lemma 7.3. For $n \geq 4$, the elliptic surface $E(n)$ contains a pair of disjoint configurations $C_{n-2}$ in which the spheres $u_{n-1}$ are sections of $E(n)$ and for $1 \leq j \leq n-2, u_{j} \cdot f=0$. Furthermore, the rational blowdown of this pair of configurations is the Horikawa surface $H(n)$.

Proof. It follows from our description of $H(n)$ that there is a decomposition
$$H(n)=B_{n-2} \cup \tilde{D}_{n-2} \cup B_{n-2}$$
where $\tilde{D}_{n-2}$ is the branched cover of $D_{n-2}$. Rationally blow up each $B_{n-2}$; this is then the 2-fold branched cover of $\mathbf{F}_{n-3}$ with $B_{n-2}$ blown up. The result is the complex surface $C_{n-2} \cup \tilde{D}_{n-2} \cup C_{n-2}$ which, by computing characteristic numbers, is just $E(n)$. \(\square\)

The first case, $n=4$, gives the example $H(4)=W_{2}$ above. The Horikawa surfaces $H(n)$ lie on the Noether line $5 c_{1}^{2}-c_{2}+36=0$, and of course the elliptic surfaces $E(n)$ lie on the line $c_{1}^{2}=0$ in the plane of coordinates $\left(c_{1}^{2}, c_{2}\right)$. Let $Y(n)$ be the simply connected 4-manifold obtained from $E(n)$ by blowing down just one of the configurations $C_{n-2}$. Then $c_{1}(Y(n))^{2}=n-3$ and $c_{2}(Y(n))=11 n+3$; so $Y(n)$ lies on the bisecting line $11 c_{1}^{2}-c_{2}+36=0$. The calculation of Donaldson invariants of $Y(n)$ and $H(n)$ follows directly from Theorem 7.1.

Proposition 7.4. The Donaldson invariants of $Y(n)$ and $H(n)$ are:
$$\begin{aligned}
\mathbf{D}_{Y(n)} & =\left\{\begin{array}{l}
\exp (Q / 2) \sinh \left(\lambda_{n}\right), \quad n \text { odd } \\
\exp (Q / 2) \cosh \left(\lambda_{n}\right), \quad n \text { even }
\end{array}\right. \\
\mathbf{D}_{H(n)} & =\left\{\begin{array}{l}
2^{n-3} \exp (Q / 2) \sinh \left(\kappa_{n}\right), \quad n \text { odd } \\
2^{n-3} \exp (Q / 2) \cosh \left(\kappa_{n}\right), \quad n \text { even }
\end{array}\right.
\end{aligned}$$
where $\lambda_{n}^{2}=n-3$ and $\kappa_{n}^{2}=2 n-6$. \(\square\)

Corollary 7.5. The simply connected 4-manifolds $Y(n)$ are not homotopy equivalent to any complex surface.

Proof. If $Y(n)$ were homeomorphic to a complex surface, this computation shows that it would have to be minimal, since the formula for $\mathbf{D}_{Y(n)}$ does not contain a factor $\cosh (e)$ where $e^{2}=-1$. Certainly the surface in question could not be elliptic since $c_{1}(Y(n))^{2} \neq 0$. Bt neither could the surface be of general type since $Y(n)$ violates the Noether inequality. Thus $Y(n)$ is not homeomorphic to any complex surface. \(\square\)
D. Gomprecht [Gt] has computed the value of the Donaldson invariant $D_{X}\left(F^{k}\right)$ for any Horikawa surface $X$ and $k$ large, where $F$ is the branched cover of the fiber $f$ of $F_{n-3}$.

\section*{8. Seiberg-Witten Invariants of Rational Blowdowns}

Suppose we are given a spin ${ }^{\mathrm{c}}$ structure on an oriented closed Riemannian 4-manifold $X$. Let $W^{+}$ and $W^{-}$be the associated spin ${ }^{\mathrm{c}}$ bundles with $L=\operatorname{det} W^{+}=\operatorname{det} W^{-}$the associated determinant line bundle. Since $c_{1}(L) \in H^{2}(X ; \mathbf{Z})$ is a characteristic cohomology class, i.e. has $\bmod 2$ reduction equal to $w_{2}(X) \in H^{2}\left(X ; \mathbf{Z}_{2}\right)$, we refer to $L$ as a characteristic line bundle. We will confuse a characteristic line bundle $L$ with its first Chern class $L \in H^{2}(X ; \mathbf{Z})$. For simplicity we assume that $H^{2}(X ; \mathbf{Z})$ has no 2-torsion so that the set $\operatorname{Spin}^{\mathrm{c}}(X)$ of spin ${ }^{\mathrm{c}}$ structures on $X$ is precisely the set of characteristic line bundles on $X$.

Clifford multiplication, $c$, maps $T^{*} X$ into the skew adjoint endomorphisms of $W^{+} \oplus W^{-}$and is determined by the requirement that $c(v)^{2}$ is multiplication by $-|v|^{2}$. Thus $c$ induces a map
$$c: T^{*} X \rightarrow \operatorname{Hom}\left(W^{+}, W^{-}\right) .$$
The 2-forms $\Lambda^{2}=\Lambda^{+} \oplus \Lambda^{-}$of $X$ then act on $W^{+}$leading to a map $\rho: \Lambda^{+} \rightarrow \operatorname{su}\left(W^{+}\right)$. A connection $A$ on $L$ together with the Levi-Civita connection on the tangent bundle of $X$ induces a connection $\nabla_{A}: \Gamma\left(W^{+}\right) \rightarrow \Gamma\left(T^{*} X \otimes W^{+}\right)$on $W^{+}$. This connection, followed by Clifford multiplication, induces the Dirac operator $D_{A}: \Gamma\left(W^{+}\right) \rightarrow \Gamma\left(W^{-}\right)$. (Thus $D_{A}$ depends both on the connection $A$ and the Riemannian metric on $X$.) Given a pair $(A, \psi) \in \mathcal{A}_{X}(L) \times \Gamma\left(W^{+}\right)$, i.e. $A$ a connection in $L$ and $\psi$ a section of $W^{+}$, the monopole equations of Seiberg and Witten [Wn] are
$$\begin{aligned}
D_{A} \psi & =0 \\
\rho\left(F_{A}^{+}\right) & =\left(\psi \otimes \psi^{*}\right)_{o}
\end{aligned}$$
where $\left(\psi \otimes \psi^{*}\right)_{o}$ is the trace-free part of the endomorphism $\psi \otimes \psi^{*}$.
The gauge group $\operatorname{Aut}(L)=\operatorname{Map}\left(X, S^{1}\right)$ acts on the space of solutions, and its orbit space is the moduli space $M_{X}(L)$ whose formal dimension is
$$\operatorname{dim} M_{X}(L)=\frac{1}{4}\left(c_{1}(L)^{2}-(3 \operatorname{sign}(X)+2 e(X)) .\right.$$
If this formal dimension is nonnegative and if $b^{+}>0$, then for a generic metric on $X$ the moduli space $M_{X}(L)$ contains no reducible solutions (solutions of the form $(A, 0)$ where $A$ is an anti-self-dual connection on $L$ ), and for a generic perturbation of the second equation of (15) by the addition of a self-dual 2-form of $X$, the moduli space $M_{X}(L)$ is a compact manifold of the given dimension ([Wn]).

The Seiberg-Witten invariant for $X$ is the function $S W_{X}: \operatorname{Spin}^{\mathrm{c}}(X) \rightarrow \mathbf{Z}$ defined as follows. Let $L$ be a characteristic line bundle. If $\operatorname{dim} M_{X}(L)<0$ or is odd, then $S W_{X}(L)$ is defined to be 0. If $\operatorname{dim} M_{X}(L)=0$, the moduli space $M_{X}(L)$ consists of a finite collection of points and $S W_{X}(L)$ is defined to be the number of these points counted with signs. These signs are determined by an orientation on $M_{X}(L)$, which in turn is determined by an orientation on the determinant line $\operatorname{det}\left(H^{0}(X ; \mathbf{R})\right) \otimes \operatorname{det}\left(H^{1}(X ; \mathbf{R})\right) \otimes \operatorname{det}\left(H_{+}^{2}(X ; \mathbf{R})\right)$. If $\operatorname{dim} M_{X}(L)>0$ then we consider the basepoint map
$$\tilde{M}_{X}(L)=\{\text { solutions }(A, \psi)\} / \text { Aut }^{0}(L) \rightarrow M_{X}(L)$$
where $\operatorname{Aut}^{0}(L)$ consists of gauge transformations which are the identity on the fiber of $L$ over a fixed basepoint in $X$. If there are no reducible solutions, the basepoint map is an $S^{1}$ fibration, and we denote its euler class by $\beta \in H^{2}\left(M_{X}(L) ; \mathbf{Z}\right)$. The moduli space $M_{X}(L)$ represents an integral cycle in the configuration space $B_{X}(L)=\left(\mathcal{A}_{X}(L) \times \Gamma\left(W^{+}\right)\right) / \operatorname{Aut}(L)$, and if $\operatorname{dim} M_{X}(L)=2 n$, the Seiberg-Witten invariant is defined to be the integer
$$S W_{X}(L)=\left\langle\beta^{n},\left[M_{X}(L)\right]\right\rangle .$$
A fundamental result is that if $b^{+}(X) \geq 2$, the map
$$S W_{X}: \operatorname{Spin}^{\mathrm{c}}(X) \rightarrow \mathbf{Z}$$
is a diffeomorphism invariant ([Wn]); i.e. $S W_{X}(L)$ does not depend on the (generic) choice of Riemannian metric on $X$ nor the choice of generic perturbation of the second equation of (15).

It is often convenient to observe that the space $\mathcal{A}_{X}(L) \times \Gamma\left(W^{+}\right)$is contractible and $\operatorname{Aut}(L) \cong$ $\operatorname{Map}\left(X, S^{1}\right)$ acts freely on $\mathcal{A}_{X}(L) \times\left(\Gamma\left(W^{+}\right) \backslash\{0\}\right)$. Since $S^{1}$ is a $K(\mathbf{Z}, 1)$, if we further assume that $H^{1}(X ; \mathbf{R})=\mathbf{0}$, then the quotient
$$B_{X}^{*}(L)=\left(\mathcal{A}_{X}(L) \times\left(\Gamma\left(W^{+}\right) \backslash\{0\}\right)\right) / S^{1}$$
of this action is homotopy equivalent to $\mathbf{C P}^{\infty}$. So if there are no reducible solutions, we may view $M_{X}(L) \subset \mathbf{C P}^{\infty}$. Under these identifications, the class $\beta$ becomes the standard generator of $H^{2}\left(\mathbf{C P}^{\infty} ; \mathbf{Z}\right)$.

Call a characteristic line bundle with nontrivial Seiberg-Witen invariant a Seiberg-Witten class. The assumption in Seiberg-Witten theory which is analogous to the assumption of simple type in Donaldson theory is
\begin{itemize}
\item[] (*) For each Seiberg-Witten class $L, \operatorname{dim} M_{L}(X)=0$.
\end{itemize}

If this condition is satisfied, $X$ is said to have Seiberg-Witten simple type.
Lemma 8.1. Let $C_{p} \subset X$ and let $X_{p}$ be its rational blowdown. Assume that $X_{p}$ is simply connected.
\begin{itemize}
\item[(a)] A line bundle $L^{*}$ on $X^{*}$ extends over $X_{p}$ if and only if $c_{1}\left(\left.L^{*}\right|_{L\left(p^{2}, 1-p\right)}\right) \in p \mathbf{Z}_{p^{2}}$.
\item[(b)] If $\bar{L}$ is a characteristic line bundle on $X_{p}$, then there is a characteristic line bundle $L$ on $X$ such that $\left.L\right|_{X^{*}}=\left.\bar{L}\right|_{X^{*}}$.
\item[(c)] If $L$ is a characteristic line bundle on $X$, then an extension $\bar{L}$ of $\left.L\right|_{X^{*}}$ is characteristic on $X^{*}$ if and only if $\left.\bar{L}\right|_{B_{p}}$ is characteristic.
\end{itemize}

Proof. (a) is obvious. For any simply connected manifold $Y=V \cup W$ where $\partial V=\partial W$ is a rational homology sphere, a class $c \in H^{2}(Y ; \mathbf{Z})$ will be characteristic provided $\langle c, \alpha\rangle \equiv \alpha \cdot \alpha(\bmod 2)$ for all $\alpha \in H^{2}(Y ; \mathbf{Z})$. Thus we need not worry about torsion classes; so a class is characteristic if and only if its restrictions to $V$ and $W$ are both characteristic. Applying this observation to $X_{p}=X^{*} \cup B_{p}$ proves (c).

To prove (b), let $\bar{L}$ be a characteristic line bundle on $X_{p}$ and let $L^{*}=\left.\bar{L}\right|_{X^{*}}$. By (a), $\delta c_{1}\left(L^{*}\right)=m p$ for some integer $m$. Suppose that $p$ is odd, then since $m p=(p+m) p \in \mathbf{Z}_{\mathbf{p}^{2}}$, we may assume that
$m$ is even. Let $L^{\prime}$ be the line bundle on $C_{p}$ such that the Poincaré dual of $c_{1}\left(L^{\prime}\right)$ is $(m+1) \gamma_{p-1}+$ $(m-p+1) \gamma_{1}$. Then $L^{\prime}$ is characteristic on $C_{p}$ and $\delta c_{1}\left(L^{\prime}\right)=\delta c_{1}\left(L^{*}\right)$. It follows that $L^{*}$ extends to a characteristic line bundle on $X$ by our observation above. If $p$ is even, we may take $c_{1}\left(L^{\prime}\right)$ to be the Poincaré dual of $m p \gamma_{1}$ and get the extension of $L^{*}$ to a global line bundle $L$ on $X$ whose restriction to both $X^{*}$ and $C_{p}$ is characteristic. \(\square\)

If $\bar{L}$ is a line bundle on $X_{p}$ and $L$ is a line bundle on $X$ satisfying $\left.L\right|_{X^{*}}=\left.\bar{L}\right|_{X^{*}}$, we say that $L$ is a lift of $\bar{L}$.

Theorem 8.2. Let $C_{p} \subset X$ and let $X_{p}$ be its rational blowdown. Let $\bar{L}$ be a characteristic line bundle on $X_{p}$ and let $L$ be any lift of $\bar{L}$ which is characteristic on $X$. Suppose that $\operatorname{dim} M_{X}(L) \equiv$ $\operatorname{dim} M_{X_{p}}(\bar{L})(\bmod 2)$. Then
$$S W_{X_{p}}(\bar{L})=S W_{X}(L) .$$
Proof. Since the rational ball $B_{p}$ embeds in the ruled surface $\mathbf{F}_{p-1}$ (see Lemma 2.1), it admits a metric of positive scalar curvature. The gluing theory for solutions of the Seiberg-Witten equations follows the same pattern as for solutions of the anti-self-duality equations. Thus we study the solutions on $X_{p}$ for $\bar{L}$ by stretching the neck between $X^{*}$ and $B_{p}$. We may assume that there are positive scalar curvature metrics on both the neck $L\left(p^{2}, 1-p\right) \times \mathbf{R}^{+}$and on $B_{p}$. This means that the only solution to the Seiberg-Witten equations on $B_{p}$ with a cylindrical end is the reducible solution ( $A^{\prime}, 0$ ), where $A^{\prime}$ is an anti-self-dual connection on $L^{\prime}=\left.\bar{L}\right|_{B_{p}}$. Possible global solutions are constructed from asymptotically reducible solutions on $X^{*}$ glued to $\left(A^{\prime}, 0\right)$. The formal dimension of $M_{B_{p}}\left(L^{\prime}\right)$ is odd and negative, and there is one gluing parameter (since the asymptotic value is reducible); so
$$\operatorname{dim} M_{X^{*}}\left(L^{*}\right)+1+\operatorname{dim} M_{B_{p}}\left(L^{\prime}\right)=\operatorname{dim} M_{X_{p}}(\bar{L})=2 d_{\bar{L}},$$
say. (If $\operatorname{dim} M_{X_{p}}(\bar{L})$ is odd, there is nothing to prove.) Thus $\operatorname{dim} M_{X^{*}}\left(L^{*}\right)=2 d_{L^{*}}$ where $d_{L^{*}} \geq d_{\bar{L}}$. This means that there is an obstruction to perturbing a glued-up $\left(A^{*}, \psi^{*}\right) \#\left(A^{\prime}, 0\right)$ to a solution. As in Donaldson theory, there is an obstruction bundle $\xi$ over $M_{X^{*}}\left(L^{*}\right)$, and it is the complex vector bundle of rank $d_{L^{*}}-d_{\bar{L}}$ associated to the basepoint fibration. The zero set of a generic section of $\xi$ is homologous to $M_{X_{p}}$ in $B_{X_{p}}(\bar{L})$. Thus
$$S W_{X_{p}}(\bar{L})=\left\langle\beta^{d_{\bar{L}}},\left[M_{X_{p}}(\bar{L})\right]\right\rangle=\left\langle\beta^{d_{\bar{L}}}, \beta^{d_{L^{*}}-d_{\bar{L}}} \cap\left[M_{X^{*}}\left(L^{*}\right)\right]\right\rangle=\left\langle\beta^{d_{L^{*}}},\left[M_{X^{*}}\left(L^{*}\right)\right]\right\rangle .$$

Let $L$ be a characteristic line bundle on $X$ which is a lift of $\bar{L}$, and let $\operatorname{dim} M_{X}(L)=2 d_{L}$. The second construction of Lemma 2.1 shows that $C_{p}$ has a metric of positive scalar curvature. So the discussion of the last paragraph applies to show that
$$S W_{X}(L)=\left\langle\beta^{d_{L^{*}}},\left[M_{X^{*}}\left(L^{*}\right)\right]\right\rangle,$$
completing the proof of the theorem. \(\square\)

Lemma 8.3. Suppose that $C_{p} \subset X$ with rational blowdown $X_{p}$. Let $L$ be a characteristic line bundle on $X$ such that $\left\langle c_{1}(L), u_{i}\right\rangle=0$ for $i=1, \ldots, p-2$ and $\left\langle c_{1}(L), u_{p-1}\right\rangle=m p$ for some $m \in \mathbf{Z}$.

Let $\bar{L}$ be a characteristic extension of $\left.L\right|_{X^{*}}$ to all of $X_{p}$. Then $m$ is odd, and $\operatorname{dim} M_{\bar{L}}\left(X_{p}\right)=$ $\operatorname{dim} M_{L}(X)+\frac{m^{2}-1}{4}(p-1)$.

Proof. The proof of Theorem 7.1 shows that $m$ must be odd if $\bar{L}$ is to be characteristic and that $c_{1}(\bar{L})^{2}=c_{1}(L)^{2}+m^{2}(p-1)$. Since $3 \operatorname{sign}\left(X_{p}\right)+2 e\left(X_{p}\right)=3 \operatorname{sign}(X)+2 e(X)+(p-1)$, the lemma follows. \(\square\)

Note that this shows that, unless $m= \pm 1$, the dimensions of the moduli spaces will increase.
We shall consider the two situations analogous to those studied in the previous sections:
\begin{itemize}
\item[(i)] $C_{p}$ is embedded in $X=Y \#(p-1) \overline{\mathbf{C P}}^{2}$ so that $X_{p}$ is the result of an order $p \log$ transform performed on a nodal fiber of $X$.
\item[(ii)] $C_{p}$ is tautly embedded in $X$ with respect to $L$, i.e. $\left\langle c_{1}(L), u_{i}\right\rangle=0$ for $i=1, \ldots, p-2$, and $\left\langle c_{1}(L), u_{p-1}\right\rangle \leq p$.
\end{itemize}

The next theorem follows directly from Theorem 8.2 and Lemma 8.3.
Theorem 8.4. Suppose that $X$ has Seiberg-Witten simple type and that $C_{p} \subset X$ with $X_{p}$ its rational blowdown. Assume that $X_{p}$ is simply connected and that $\bar{L}$ is a characteristic line bundle on $X_{p}$. Suppose further that $L$ is a characteristic lift of $\bar{L}$ and that $C_{p}$ is tautly embedded with respect to $L$. Then
$$S W_{X_{p}}(\bar{L})=S W_{X}(L)$$
and $c_{1}(\bar{L})^{2}=c_{1}(L)^{2}+(p-1)$. \(\square\)

Say that the configuration $C_{p}$ is $S W$-tautly embedded in $X$ if it is tautly embedded with respect to each Seiberg-Witten class.

Corollary 8.5. Suppose that $X$ has Seiberg-Witten simple type and contains the $S W$-tautly embedded configuration $C_{p}$. Assume that the rational blowdown $X_{p}$ is simply connected. Then the Seiberg-Witten classes of $X_{p}$ are the characteristic line bundles $\bar{L}$ which have a lift to a Seiberg-Witten class $L$ of $X$, and $S W_{X_{p}}(\bar{L})=S W_{X}(L)$. \(\square\)

In a fashion similar to the proof of Theorem 8.2, one can prove a blowup formula for Seiberg-Witten invariants. The characteristic line bundles of $X \# \overline{\mathbf{C P}}^{2}$ are those of the form $L \otimes E^{2 k+1}$ where $L$ is characteristic on $X$ and $c_{1}(E)=e$, and $\operatorname{dim} M_{L \otimes E^{2 k+1}}\left(X \# \overline{\mathbf{C P}}^{2}\right)=\operatorname{dim} M_{L}(X)-k(k+1)$. It is shown in [FS4] that $S W_{X \# \overline{\mathbf{C P}}^{2}}\left(L \otimes E^{2 k+1}\right)=S W_{X}(L)$ provided $\operatorname{dim} M_{L}(X)-k(k+1) \geq 0$. It follows that if $X$ satisfies the Seiberg-Witten simple-type condition (*), then so does $X \# \overline{\mathbf{C P}}^{2}$.

Suppose that $X$ contains the nodal fiber $S$, and $X_{p}$ is the result of performing an order $p \log$ transform on $S$. The characteristic line bundles on $X_{p}$ are obtained from characteristic bundles $L \otimes E_{1}^{2 k_{1}+1} \otimes \cdots \otimes E_{p-1}^{2 k_{p-1}+1}$ on $Y=X \#(p-1) \overline{\mathbf{C P}}^{2}$ by restricting to $Y^{*}=Y \backslash C_{p}$ and then extending over $B_{p}$. If we assume that $\left\langle c_{1}(L), S\right\rangle=0$, then for each $L \otimes E_{1}^{ \pm 1} \otimes \cdots \otimes E_{p-1}^{ \pm 1}=L\left(\boldsymbol{\epsilon}_{J}\right)$
with $c_{1}\left(L\left(\boldsymbol{\epsilon}_{J}\right)\right)=c_{1}(L)+\sum_{J} \epsilon_{J, i} e_{i}$, it follows from Proposition 6.1 that the unique extension $\bar{L}_{J}$ over $X_{p}$ has $c_{1}\left(\bar{L}_{J}\right)=c_{1}(L)+|J| \sigma_{p}$, where $\sigma_{p}$ is the Poincaré dual of $S / p$. (Note that when $p$ is even, $|J|$ must be odd; so the extension $\bar{L}_{J}$ is characteristic.) Hence
$$\operatorname{dim} M_{\bar{L}_{J}}\left(X_{p}\right)=\operatorname{dim} M_{L}(X),$$
and Theorem 8.2 implies:
Theorem 8.6. Suppose that $X$ has Seiberg-Witten simple type and contains the nodal fiber $S$. Let $L$ be a characteristic line bundle on $X$ with $\left\langle c_{1}(L), S\right\rangle=0$. Let $X_{p}$ be the result of performing an order $p$ log transform on $S$. For each $J \in\{ \pm 1\}^{p-1}$, we have $S W_{X_{p}}\left(\bar{L}_{J}\right)=S W_{X}(L)$. Suppose furthermore that $\left\langle c_{1}(L), S\right\rangle=0$ for each characteristic $L$ on $X$ with $S W_{X}(L) \neq 0$. Then $X_{p}$ also has Seiberg-Witten simple type and each line bundle $\Lambda$ on $X_{p}$ with $\operatorname{SW}_{X_{p}}(\Lambda) \neq 0$ is of the form $\Lambda=\bar{L}_{J}$. \(\square\)

By a the nodal configuration we shall mean a configuration $C_{p} \subset X \#(p-1) \overline{\mathbf{C P}}^{2}$ as above, obtained from a nodal fiber $S$ satisfying the condition $\left\langle c_{1}(L), S\right\rangle=0$ for each characteristic $L$ on $X$ with $S W_{X}(L) \neq 0$.

Witten [Wn] has conjectured that (for manifolds with $b^{+}>1$ ) the Seiberg-Witten simple type condition is equivalent to the simple type condition of Kronheimer and Mrowka for Donaldson theory. Further, under this hypothess of simple type, Witten gives a precise conjecture for relating the Seiberg-Witten invariants and the Donaldson series, namely:

Conjecture (Witten). The set of basic classes in the two theories are the same, and
$$\mathbf{D}_{X}=2^{3 \operatorname{sign}+2 e-\left(\frac{b^{+}-3}{2}\right)} \exp (Q / 2) \sum S W_{X}\left(\kappa_{s}\right) e^{\kappa_{s}} .$$

Theorem 8.7. Witten's conjecture is true for simply connected elliptic surfaces.

Proof. Witten has given a recipe for calculating $S W_{X}$ for all Kahler manifolds $X$. So one could prove this theorem simply by comparing the answer obtained with that of Theorem 6.7. Alternatively, note that Witten's recipe gives the result that the nonzero Seiberg-Witten invariants of $E(n)$ are:
$$S W_{E(n)}((n-2-2 r) f)=(-1)^{r}\binom{n-2}{r}, \quad r=0, \ldots, n-2$$
(where $f$ is the fiber class). Suppose we define
$$\mathbf{W}_{X}=2^{3 \operatorname{sign}+2 e-\left(\frac{b^{+}-3}{2}\right)} \sum S W_{X}\left(\kappa_{s}\right) e^{\kappa_{s}}, \quad \mathbf{S W}_{X}=\exp \left(Q_{X} / 2\right) \mathbf{W}_{X}$$
Then (17) shows that $\mathbf{D}_{E(n)}=\mathbf{S W}_{E(n)}$. Suppose that $X_{p}$ is the result of an order $p \log$ transform on a nodal fiber which is orthogonal to all classes in $H_{2}(X)$ with nontrivial Seiberg-Witten invariants. Then Theorem 8.6 implies that $\mathbf{W}_{X_{p}}=\mathbf{W}_{X} \cdot\left(\sinh \left(f_{p}\right) / \sinh (f)\right)$. It follows that $\mathbf{S W}_{E(n ; p, q)}=$ $\mathbf{D}_{E(n ; p, q)}$. \(\square\)

Furthermore, we have

Theorem 8.8. If $X$ satisfies the Witten conjecture, then so do all blowups and blowdowns and any rational blowdown $X_{p}$ of a nodal or taut configuration.

\section*{References}
\begin{itemize}
\item[] [APS] M. Atiyah, V. Patodi, and I. Singer, Spectral asymmetry and Riemannian geometry. I, Math. Proc. Camb. Phil. Soc. 77 (1975), 43-69.
\item[] [Br] S. Bauer, Diffeomorphism types of elliptic surfaces with $p_{g}=1, \mathrm{~J}$. Reine Angew. Math. 451 (1992), 149-180.
\item[] [Bo] F. Bonahon, Difféotopies des espaces lenticulaires, Topology 22 (1983), 305-314.
\item[] [CH] A. Casson and J. Harer, Some homology lens spaces which bound rational homology balls, Pac. J. Math. 96 (1981), 23-36.
\item[] [D1] S. Donaldson, Polynomial invariants for smooth 4-manifolds, Topology 29 (1990), 257-315.
\item[] [DK] S. Donaldson and P. Kronheimer, "The Geometry of Four-Manifolds," Oxford Mathematical Monographs, Oxford University Press, Oxford, 1990.
\item[] [FS1] R. Fintushel and R. Stern, Surgery in cusp neighborhoods and the geography of irreducible 4-manifolds, Inventiones Math., 117 (1994), 455-523.
\item[] [FS2] R. Fintushel and R. Stern, The blowup formula for Donaldson invariants, to appear in Annals of Math.
\item[] [FS3] R. Fintushel and R. Stern, Donaldson invariants of 4-manifolds with simple type, to appear in Jour. Diff. Geom.
\item[] [FS4] R. Fintushel and R. Stern, Immersed spheres in 4-manifolds and the immersed Thom conjecture, preprint.
\item[] [Fr] R. Friedman, Vector bundles and SO(3)-invariants for elliptic surfaces , Jour. Amer. Math. Soc. 8 (1995), 29-139.
\item[] [FM1] R. Friedman and J. Morgan, On the diffeomorphism types of certain algebraic surfaces I,II, Jour. Diff. Geom. 27 (1988), 297-369.
\item[] [FM] R. Friedman and J. Morgan, "Smooth Four-Manifolds and Complex Surfaces," Ergebnisse der Math. und Grenz. 3, Springer-Verlag, New York, 1994.
\item[] [G1] R. Gompf, Nuclei of elliptic surfaces, Topology 30 (1991), 479-511.
\item[] [G2] R. Gompf, A new construction of symplectic manifolds, preprint.
\item[] [GM] R. Gompf and T. Mrowka, Irreducible four manifolds need not be complex, Annals of Math. 138 (1993), 61-111.
\item[] [Gt] D. Gomprecht, Rank 2 bundles on genus 2 fibrations, preprint.
\item[] [K] R. Kirby, "The Topology of Four-Manifolds," Lecture Notes in Mathematics 1374 , Springer-Verlag, New York, 1989.
\item[] [KSB] J. Kollár and N. Shepherd-Barron Threefolds and deformations of surface singularities, Inventiones Math., 91 (1988), 299-338.
\item[] [KM1] P. Kronheimer and T. Mrowka, Recurrence relations and asymptotics for four-manifold invariants, Bull. Amer. Math. Soc. 30 (1994), 215-221.
\item[] [KM2] P. Kronheimer and T. Mrowka, Embedded surfaces and the structure of Donaldson's polynomial invariants, to appear in Jour. Diff. Geom.
\item[] [L] T. Lawson, Invariants for families of Brieskorn varieties, Proc. Amer. Math. Soc. 99 (1987), 187-192.
\item[] [Li] P. Lisca, On Donaldson polynomials of elliptic surfaces, Journal of Diff. Geometry, preprint
\item[] [Mn] B. Moishezon, "Complex Surfaces and Connected Sums of Projective Planes," Springer Notes No. 603, 1977.
\item[] [MM1] J. Morgan and T. Mrowka, A note on Donaldson's polynomial invariants, Int. Math. Research Notices 10 (1992), 223-230.
\item[] [MM2] J. Morgan and T. Mrowka On the diffeomorphism classification of regular elliptic surfaces, Int. Math. Research International Math. Research Notices 6 (1993) 183-184
\item[] [MMR] J. Morgan, T. Mrowka, and D. Ruberman, The $L^{2}$-moduli space and a vanishing theorem for Donaldson polynomial invariants, International Press, 1994.
\item[] [MO] J. Morgan and K.G. O'Grady, Differential Topology of Complex surfaces: Elliptic surfaces with $p_{g}=$ 1:Smooth Classification, Lecture Notes in Mathematics, Vol. 1545, Springer-Verlag, 1993.
\item[] [T1] C. Taubes, A simplicial model for Donaldson - Floer theory, to appear in Floer Memorial Volume, Birkhauser, 1994.
\item[] [T2] C. Taubes, The role of reducibles in Donaldson - Floer theory, to appear in Proc. 1993 Taniguchi Symposium on Low Dimensional Topology and Topological Field Theory.
\item[] [T3] C. Taubes, Floer theory for twisted circle bundles, preprint.
\item[] [T4] C. Taubes, Holonomy forms in gauge theory, in preparation.
\end{itemize}
\begin{itemize}
\item[] [T5] C. Taubes, The Seiberg-Witten invariants and symplectic forms, Mathematical Research Letters 1 (1994), 809-822.
\item[] [Wk] W. Wieczorek, The Donaldson invariant and embedded 2-spheres, Michigan State University Thesis, 1995.
\item[] [Wn] E. Witten, Monopoles and four-manifolds, Mathematical Research Letters 1 (1994), 769-796.
\end{itemize}

\section*{Figures}

Figure 5.
Figure 6.

Figure 7.
Figure 8.

Figure 13.
Figure 14.

Department of Mathematics, Michigan State University East Lansing, Michigan 48824

E-mail address: ronfint@math.msu.edu

Department of Mathematics, University of California Irvine, California 92717

E-mail address: rstern@math.uci.edu

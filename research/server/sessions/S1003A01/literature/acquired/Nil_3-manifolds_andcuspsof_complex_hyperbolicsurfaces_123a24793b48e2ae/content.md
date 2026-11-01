---
retention_scope: session
part: 1
total_parts: 1
---

---
source_file: 2411_15345.pdf
converter: mathpix
format: mmd
---

\title{
Nil 3-manifolds and cusps of complex hyperbolic surfaces
}

\author{
Julien Paupert, Connor Sell
}

November 26, 2024

\begin{abstract}
McReynolds showed that every compact Nil 3-manifold occurs as the cusp cross-section of some arithmetic complex hyperbolic 2-manifold. We classify which commensurability classes of cusped, arithmetic, complex hyperbolic 2-manifolds admit cusps with cross-section homeomorphic to a given compact Nil 3-manifold. In particular, there are some Nil 3-manifolds which occur as cusps in every such commensurability class, and some which only occur in a single commensurability class. We also show that every compact Nil 3-manifold occurs as the cusp cross-section of some non-arithmetic complex hyperbolic 2-manifold.
\end{abstract}

\section*{1 Introduction}

A classical and well-studied question in topology is whether a given $n$-manifold $M$ occurs as the boundary of an $(n+1)$-manifold $W$. For instance, Rohlin showed in [R] that every compact orientable 3-manifold bounds a compact orientable 4-manifold - in other words, the cobordism group of 3-manifolds is trivial.

One can refine the question of bounding when the manifolds are equipped with geometric structures. For example, when $M$ is a compact hyperbolic $n$-manifold, one can ask whether $M$ occurs as the totally geodesic boundary of a hyperbolic $(n+1)$-manifold-with-boundary $W$. Analogously, when $M$ is a compact flat $n$ manifold one can ask whether $M$ occurs as the cusp cross-section of a (complete, finite-volume, 1-cusped) hyperbolic manifold $W$. (Recall that the ends of a complete, finite-volume, hyperbolic manifold, called cusps, are diffeomorphic to $M \times \mathbb{R}^{+}$with $M$ a compact flat $n$-manifold, called a cusp cross-section). In either case we will say that $M$ bounds geometrically. Note that in the latter case, $M$ is diffeomorphic to the boundary of a manifold-with-boundary $W^{\prime}$ such that $W=W^{\prime} \backslash \partial W^{\prime}$ admits a complete, finite-volume hyperbolic metric. ( $W^{\prime}$ is obtained from $W$ by adding the boundary $M$ "at infinity").

The latter version of geometric bounding also makes sense for the other negatively curved locally symmetric spaces, which do not admit any totally geodesic hypersurfaces (see Proposition 2.5.1 of [CG]). These "other" locally symmetric spaces - negatively curved but not constantly curved - are quotients of the hyperbolic spaces $\mathrm{H}_{\mathbb{K}}^{n}$ with $\mathbb{K}=\mathbb{C}$ and $n \geqslant 2, \mathbb{K}=\mathbb{H}$ and $n \geqslant 2$, or $\mathbb{K}=\mathbb{O}$ and $n=2$. For these other locally symmetric spaces, the cusp cross-sections $M$ are now infra-nilmanifolds, that is, compact quotients of a simply-connected nilpotent Lie group $\mathfrak{N}$ by a discrete group of isometries. Gromov showed that the latter are exactly the compact almost flat manifolds (see [Gr]), so we will use the terms interchangeably.

More specifically, when $W$ is a cusped, negatively curved, locally symmetric space, its cusp cross-sections are quotients of 2-step nilpotent Lie groups usually called generalized Heisenberg groups (over $\mathbb{C}$ or $\mathbb{H}$, see e.g. [CG]). For example, in the case of $\mathbb{K}=\mathbb{C}$ and $n=2$, which is the most relevant for this paper, $\mathfrak{N}$ is the usual 3-dimensional Heisenberg group, which we will denote Nil, following the standard notation in 3-dimensional topology (this is one of the 8 Thurston geometries; see Sc or Section 2.1 for more details). An interesting feature of almost-flat manifolds is that, unlike the flat ones, they occur in infinite families in each dimension at least 3; the 3-dimensional ones are listed in Section 2.1 by fundamental group.

Farrell and Zdravkovska conjectured the following, Conjecture 2 of [FZ] (in both statements $M$ is assumed to be compact and connected):

Conjecture 1. (a) If $M^{n}$ is a flat Riemannian manifold, then $M^{n}=\partial W^{n+1}$, where $W \backslash \partial W$ supports a complete hyperbolic structure with finite volume.
\begin{itemize}
\item[(b)] If $M^{n}$ is an almost-flat Riemannian manifold, then $M^{n}=\partial W^{n+1}$, where $W \backslash \partial W$ supports a complete Riemannian metric with finite volume and negative sectional curvatures.
\end{itemize}

Long and Reid showed in [LR1] that (a) is false when $n=3$, providing examples of flat 3-manifolds which are not homeomorphic to any cross-section of a one-cusped (complete, finite-volume) hyperbolic 4-manifold. On the other hand, they also showed in [LR2] that for any $n \geqslant 2$, every compact, flat $n$-manifold occurs as the cusp cross-section of some hyperbolic $(n+1)$-orbifold [LR2] (possibly with several cusps). This result was later upgraded by McReynolds in [M2] to say that such a flat manifold always occurs as the cusp cross-section of a hyperbolic $(n+1)$-manifold, also possibly with several cusps.

The restriction to manifolds (or even orbifolds) with a single cusp seems difficult, to say the least. In fact, while there is an abundance of 1-cusped hyperbolic surfaces and 3-manifolds (e.g. knot complements), it was only in 2013 that Kolpakov-Martelli produced in [KM] the first example of a one-cusped hyperbolic 4-manifold. As far as we know, it is still an open question whether or not there exists a one-cusped hyperbolic $n$-manifold for $n \geqslant 5$. Analogously, it was not until very recently that Deraux ([Der]) and Deraux-Stover ([DS]) found the first examples of one-cusped complex hyperbolic 2-manifolds.

Moreover, it may well be that there do not exist any one-cusped hyperbolic or complex hyperbolic manifolds, or even orbifolds, in high enough dimensions. In the arithmetic world, Stover [St1] showed that no arithmetic hyperbolic orbifold of dimension at least 30 can have exactly one cusp, and that similar bounds exist for arithmetic complex and quaternion hyperbolic orbifolds as well. (Since finite-volume quaternion hyperbolic orbifolds of dimension at least 2 are all arithmetic, the result is in fact unconditional in that case). Stover also produced in [St1] examples of one-cusped (arithmetic) hyperbolic orbifolds in dimensions $n=10$ and 11; such orbifolds were known to exist for $n \leqslant 9$ among hyperbolic Coxeter groups.

In view of these results it seems reasonable to relax the Farrell-Zdravkovska Conjecture to ask the following (where, again, the manifolds $M$ are assumed to be compact and connected):

Question 1. (a) Given a flat $n$-manifold $M$, is $M$ diffeomorphic to a cusp cross-section of some finite-volume hyperbolic $(n+1)$-manifold $W$ ? If so, of which such manifolds $W$ ?
\begin{itemize}
\item[(b)] Given an almost-flat $n$-manifold $M$, is $M$ diffeomorphic to a cusp cross-section of some finite-volume complex, quaternion or octonion-hyperbolic manifold $W$ of real dimension $n+1$ ? If so, of which such manifolds $W$ ?
\end{itemize}

Note that the class of complex, quaternion or octonion-hyperbolic $(n+1)$-manifold $W$ appearing in part (b) is, in case $W$ has a single cusp, exactly the class of locally symmetric Riemannian manifolds $W$ such that $M=\partial W$, and $W \backslash \partial W$ supports a complete, finite-volume Riemannian metric with negative sectional curvatures, as in part (b) of the Farrell-Zdravkovska Conjecture. (Recall that a complex, quaternion or octonion-hyperbolic manifold is an isometric quotient of hyperbolic space $\mathrm{H}_{\mathbb{K}}^{n}$ for $\mathbb{K}=\mathbb{C}, \mathbb{H}$ or $\mathbb{O}$, see [CG] and Section 2.2 when $\mathbb{K}=\mathbb{C}$ for more details).

McReynolds studied in [M1] the cusps of arithmetic real, complex, and quaternion-hyperbolic orbifolds, On one hand, he showed that every compact Nil 3-manifold occurs as the cusp cross-section of some (arithmetic) complex hyperbolic 2-orbifold (see below for some more precise terminology). This gives a positive answer to the first part of Question (b) above for any (compact, connected) almost-flat 3-manifold.

On the other hand, he showed that in all other cases (that is, complex dimension at least 3 and quaternion dimension at least 2) there exist (infinite families of) almost-flat manifolds modelled on the appropriate generalized Heisenberg group which are not diffeomorphic to a cusp cross-section of any finite-arithmetic complex or quaternion-hyperbolic manifold. As above, in the quaternion case all finite-volume manifolds are arithmetic and so this provides a negative answer to Question (b) above for infinitely many almost-flat manifolds in each dimension $4 n+3$ with $n \geqslant 1$.

Kamishima showed in [K] that the cusp cross-section of any one-cusped complex hyperbolic 2-manifold must have trivial holonomy (rotational part), that is, in the terminology of Section 2.1 below, it must belong to the family (1) of Nil-tori. Moreover, by Corollary 2.2 of [DS] the Euler number (denoted $k$ in Section 2.1) of the Nil-torus must be a multiple of 4. The one-cusped complex hyperbolic 2-manifolds constructed in [DS] have as cusp cross-sections Nil-tori with Euler number $k$ any odd multiple of 12 ; so in the above terminology such Nil-tori bound geometrically.

Both [LR2] and [M1] utilized arithmetic methods (and separability arguments) to construct manifolds with a given cross-section. In both the real and complex cases, all known examples of hyperbolic manifolds in high enough dimensions are either arithmetic or use arithmetic manifolds in their constructions. (Here, high enough means dimension at least 4 in the complex case, and at least 6 in the real case).

The second author studied in [Se] the second part of Question (a) for flat 3-manifolds. More precisely, the main results of [Se] classify, given a flat 3-manifold $M$, in which commensurability classes of cusped, arithmetic hyperbolic 4-manifolds $M$ occurs as a cusp cross-section. In this paper, we study the analogous second part of Question (b) for almost-flat 3-manifolds, that is we study, given a Nil 3-manifold $M$, in which cusped, complex hyperbolic 2-manifolds $M$ can occur as a cusp cross-section.

In the arithmetic case, similarly to [Se], given a Nil 3-manifold $M$, we classify in which commensurability classes of cusped, arithmetic complex hyperbolic 2-manifolds $M$ occurs as a cusp cross-section. Such commensurability classes are enumerated by the Picard modular groups $\operatorname{PU}\left(2,1, \mathcal{O}_{d}\right)$ with $d$ a positive square-free integer and $\mathcal{O}_{d}$ the ring of integers of $\mathbb{Q}(i \sqrt{d})$ (see Section 2.3). First, we show that some Nil 3-manifolds occur in every commensurability class of cusped arithmetic complex hyperbolic 2-manifolds (see Section 2.1 for the labelling of families (1)-(7)).

Theorem 1. Let $N$ be any Nil 3-manifold in families (1), (2), (3) or (4) (Nil-tori, vertical or horizontal halftwist, or double half-twist). Then $N$ occurs as a cusp cross-section in the commensurability class of the Picard modular group $\operatorname{PU}\left(2,1, \mathcal{O}_{d}\right)$ for any squarefree $d \geqslant 1$.

Secondly, we show that some Nil 3-manifolds are obstructed from some commensurability classes. In fact, they each occur in only a single commensurability class of arithmetic complex hyperbolic 2-manifolds. Note that every Nil 3-manifold is covered by either Theorem 1 or Theorem 2.

Theorem 2. The Nil 3-manifolds in families (5), (6), and (7) (1/4-twist, 1/3-twist and 1/6-twist) each occur as cusp cross-sections in a single arithmetic commensurability class. For the 1/4-twist, this is the commensurability class of the Gauss-Picard modular group $\operatorname{PU}\left(2,1, \mathcal{O}_{1}\right)$, and for the 1/3-twist and 1/6-twist, this is the commensurability class of the Eisenstein-Picard modular group $\operatorname{PU}\left(2,1, \mathcal{O}_{3}\right)$.

In passing, we prove the following related result. This shows that certain Nil 3-manifolds $N$ can only occur as cusp cross-sections in $\mathrm{H}_{\mathbb{C}}^{2}$-manifolds which are not complex hyperbolic manifolds (see Definition 2); in other words, any embedding of $\pi_{1}(N)$ into $\operatorname{Isom}\left(\mathrm{H}_{\mathbb{C}}^{2}\right)$ must contain antiholomorphic isometries in its image (see Section 2.2).

Theorem 3. Let $N$ be any Nil 3-manifold in families (3) or (4) (horizontal half-twist or double half-twist). Then $N$ occurs as a cusp cross-section of an $\mathrm{H}_{\mathbb{C}}^{2}$-manifold, but not of any complex hyperbolic manifold or orbifold. That is, the image of any holonomy representation $\rho: \pi_{1}(N) \longrightarrow G_{\infty} \simeq \operatorname{Isom}(\mathrm{Nil})$ must contain anitholomorphic isometries.

Finally, we combine results of [M1] and [M2] with the detailed analysis of cusp groups in the known nonarithmetic complex hyperbolic orbifolds in [DPP2] to show the following:

Theorem 4. Every Nil 3-manifold occurs as the cusp cross-section of a non-arithmetic complex hyperbolic 2-manifold or $\mathrm{H}_{\mathbb{C}}^{2}$-manifold.

The paper is organized as follows. Section 2 gives background on Nil-manifolds, complex hyperbolic geometry, Picard modular groups and their cusps and non-arithmetic complex hyperbolic 2-orbifolds and their cusps. Section 3 is devoted to the results stated above and their proofs.

\section*{2 Geometric background}

\subsection*{2.1 Nil-manifolds}

The Heisenberg group Nil is a 3-dimensional Lie group which can be written as $\mathbb{C} \times \mathbb{R}$ with group law given by:
$$\left(z_{1}, t_{1}\right) \cdot\left(z_{2}, t_{2}\right)=\left(z_{1}+z_{2}, t_{1}+t_{2}+2 \operatorname{Im}\left(z_{1} \overline{z_{2}}\right)\right) .$$
It is a 2-step nilpotent group, as one can easily check that $[\mathrm{Nil}, \mathrm{Nil}]=Z(\mathrm{Nil})=\{(0, t) \mid t \in \mathbb{R}\}$, the vertical axis. This model of Nil naturally arises from the action of $\mathrm{PU}(2,1)$ on the 3-sphere $\partial_{\infty} \mathrm{H}_{\mathbb{C}}^{2}$ as we will see in the next subsection. (The most standard model of Nil is the subgroup of upper-triangular unipotent matrices in $\operatorname{SL}_{3}(\mathbb{R})$, see [Sc]).

As any Lie group, Nil admits a left-invariant Riemannian metric, unique up to scale. By construction, (left-) translations are isometries for this metric. We will describe the isometry group Isom(Nil) in more detail in the next subsection, but for now we just note that, as in the Euclidean case, isometries are affine diffeomorphisms of Nil in the sense that:
$$\operatorname{Isom}(\operatorname{Nil})=\operatorname{Nil} \rtimes C$$
for some compact Lie subgroup $C$ of $\operatorname{Aut}(\mathrm{Nil})$. In fact we will see below that $C=\mathrm{U}(1) \rtimes \mathbb{Z}_{2}$, with the U(1) factor acting on Nil by rotations about the (vertical) $t$-axis, and $\mathbb{Z}_{2}$ acting by $(z, t) \mapsto(\bar{z},-t)$.

Definition 1. A Nil-manifold is a compact Riemannian 3-manifold $N$ locally modelled on Nil (in the sense of Ehresmann-Thurston geometric structures). In other words, $N \simeq \mathrm{Nil} / \Delta$, where $\Delta \simeq \pi_{1}(N)$ is a discrete torsion-free subgroup of Isom(Nil).

Note that there are various definitions of Nil- (or nil-)manifolds in the literature, but this is the standard definition from 3-manifold topology/geometric structures. (We will quote the classification from [Dek] below, where they are called infra-nilmanifolds).

Given a Nil-manifold $N$, we will be interested in recovering the geometric structure on $N$ from representations of $\pi_{1}(N)$. To this end, recall that a representation $\rho: \pi_{1}(N) \longrightarrow$ Isom(Nil) is a holonomy representation (for the Nil-structure on $N$ ) if $\mathrm{Nil} / \rho\left(\pi_{1}(N)\right)$ is diffeomorphic to $N$. The basic theory of geometric structures (see e.g. [Go2], Corollary 8.1.4) gives us the following:

Lemma 1. Let $N$ be a Nil-manifold and $\rho: \pi_{1}(N) \longrightarrow \operatorname{Isom}(\mathrm{Nil})$ a discrete and faithful representation with $\operatorname{Nil} / \rho\left(\pi_{1}(N)\right)$ compact. Then $\operatorname{Nil} / \rho\left(\pi_{1}(N)\right)$ is diffeomorphic to $N$; that is, $\rho$ is a holonomy representation of $\pi_{1}(N)$.

As a special case of the second generalized Bieberbach theorem below, the holonomy representation of a Nil-manifold group $\rho: \pi_{1}(N) \longrightarrow \operatorname{Isom}(\mathrm{Nil})$ is unique up to conjugation by the affine group $\mathrm{Nil} \rtimes \operatorname{Aut}(\mathrm{Nil})$. The following generalized Bieberbach theorems are due to Auslander ([A]), with a corrected statement and proof for the second statement by Lee-Raymond ([LeRa], see also discussion in Section 2.2 of [Dek]).

Theorem 5. Let $N$ be a simply-connected nilpotent Lie group and $C$ a compact Lie subgroup of $\operatorname{Aut}(N)$.
\begin{itemize}
\item[1.] ([A]) Let $\Gamma$ be a discrete cocompact subgroup of $G=N \rtimes C$. Then $\Gamma \cap N$ is a cocompact lattice in $N$ and $\Gamma /(\Gamma \cap N)$ is finite.
\item[2.] (LeRa ) Let $\Gamma_{1}, \Gamma_{2}$ be discrete cocompact subgroups of $G=N \rtimes C$. If $\Gamma_{1}$ and $\Gamma_{2}$ are isomorphic (as abstract groups) then they are conjugate in the affine group $N \rtimes \operatorname{Aut}(N)$.
\end{itemize}

Note that the (first two) classical Bieberbach theorems are obtained by taking $N=\mathbb{R}^{n}$ (and $C=\mathrm{O}(n)$ ) in these statements. The third Bieberbach theorem, stating that up to conjugacy, there are only finitely many such $\Gamma$ in each dimension, is no longer true for more general nilpotent groups. There is a meaningful generalization of this third Bieberbach theorem (see Section 2.3 of Dek ), but when $N=$ Nil there is in fact an explicit classification of Nil-manifold groups, coming in seven infinite families as follows.

We give presentations for the fundamental groups of the manifolds in these seven families below; the numbering is the same as in [M1] (these are the $A B$-groups from [Dek], appearing on pp. 159-166 in families numbered $1,2,4,8,10,13,16$ respectively). We give these families more evocative names for ease of reference.
\begin{itemize}
\item[1.] (Nil-tori) $\left\langle a, b, c \mid[b, a]=c^{k},[c, a]=[c, b]=1\right\rangle$ with $k \in \mathbb{N}$
\item[2.] (Vertical half-twist) $\left\langle a, b, c, \alpha \mid[b, a]=c^{k},[c, a]=[c, b]=[c, \alpha]=1, \alpha a=a^{-1} \alpha, \alpha b=b^{-1} \alpha, \alpha^{2}=c\right\rangle$ with $k \in 2 \mathbb{N}$.
\item[3.] (Horizontal half-twist) $\left\langle a, b, c, \alpha \mid[b, a]=c^{2 k},[c, a]=[c, b]=[a, \alpha]=1, \alpha b=b^{-1} \alpha c^{-k}, \alpha c=c^{-1} \alpha, \alpha^{2}=a\right\rangle$ with $k \in \mathbb{N}$.
\item[4.] (Double half-twist) $\langle a, b, c, \alpha, \beta|[b, a]=c^{2 k},[c, a]=[c, b]=[c, \alpha]=[a, \beta]=1, \alpha a=a^{-1} \alpha c^{k}$, $\left.\alpha b=b^{-1} \alpha c^{-k}, \beta b=b^{-1} \beta c^{-k}, \beta c=c^{-1} \beta, \alpha \beta=a^{-1} b^{-1} \beta \alpha c^{-k-1}, \alpha^{2}=c, \beta^{2}=a\right\rangle$ with $k \in 2 \mathbb{N}$.
\end{itemize}
\begin{itemize}
\item[5.] (1/4-twist) $\left\langle a, b, c, \alpha \mid[b, a]=c^{k},[c, a]=[c, b]=[c, \alpha]=1, \alpha a=b \alpha, \alpha b=a^{-1} \alpha, \alpha^{4}=c^{p}\right\rangle$ with $k \in 2 \mathbb{N}$ and either $p=1$ or $k \in 4 \mathbb{N}$ and $p=3$.
\item[6.] (1/3-twist) $\left\langle a, b, c, \alpha \mid[b, a]=c^{k},[c, a]=[c, b]=[c, \alpha]=1, \alpha a=b \alpha c^{k_{1}}, \alpha b=a^{-1} b^{-1} \alpha, \alpha^{3}=c^{k_{2}}\right\rangle$ with $k>0$ and either $k \equiv 0(\bmod 3), k_{1}=0$, and $k_{2}=1$ or 2, or $k \equiv 1,2(\bmod 3), k_{1}=1$, and $k_{2}=1$.
\item[7.] (1/6-twist) $\left\langle a, b, c, \alpha \mid[b, a]=c^{k},[c, a]=[c, b]=[c, \alpha]=1, \alpha a=a b \alpha, \alpha b=a^{-1} \alpha, \alpha^{6}=c^{k_{1}}\right\rangle$ with $k>0$ and either $k \equiv 0,4(\bmod 6)$ and $k_{1}=1$, or $k \equiv 0,2(\bmod 6)$ and $k_{1}=5$.
\end{itemize}

In the geometric realization of these groups (in the holonomy representation), the generators $a, b$, and $c$ are Heisenberg translations, with $a, b$ horizontal translations and $c$ a vertical translation (see next subsection for terminology). The generators $\alpha$ and $\beta$ are ellipto-parabolic, and play a similar role to the generators of flat 3-manifolds with nontrivial rotational part.

In this way, there is a correspondence between these seven families of Nil-manifolds and the six orientable flat 3-manifolds, with families (1), (4), (5), (6), and (7) corresponding to the 3-torus, Hantzsche-Wendt manifold, 1/4-twist, 1/3-twist, and 1/6-twist, respectively. Families (2) and (3) both correspond to the half-twist, with the twist occurring along a vertical or horizontal Heisenberg translation, respectively. In fact, setting $k=0$ in these presentations (along with particular values for $p, k_{1}$, or $k_{2}$ ) yields the fundamental group of the corresponding flat manifold.

\subsection*{2.2 Complex hyperbolic geometry}

See [CG] or [Go1] for a more detailed discussion of the background material in this section.
Projective models: Consider $\mathbb{C}^{n, 1}$, the vector space $\mathbb{C}^{n+1}$ endowed with a Hermitian form $\langle\cdot, \cdot\rangle$ of signature $(n, 1)$. Let $V^{-}=\left\{Z \in \mathbb{C}^{n, 1} \mid\langle Z, Z\rangle<0\right\}$ and $\pi: \mathbb{C}^{n+1}-\{0\} \longrightarrow \mathbb{C P}^{n}$ denote projectivization. Define $\mathrm{H}_{\mathbb{C}}^{n}$ to be $\pi\left(V^{-}\right) \subset \mathbb{C P}^{n}$, endowed with the distance $d$ given by:
$$\cosh ^{2} \frac{1}{2} d(\pi(X), \pi(Y))=\frac{|\langle X, Y\rangle|^{2}}{\langle X, X\rangle\langle Y, Y\rangle}$$
This distance is in fact induced by a complete Riemannian metric (called the Bergman metric) which has negative sectional curvatures 1/4-pinched (between -1 and -1/4 in the above normalization).

Different choices of Hermitian forms of signature ( $n, 1$ ) give rise to different models of $\mathrm{H}_{\mathbb{C}}^{n}$. For our purposes we will consider the Siegel model, generalizing the Poincaré upper half-plane model of $\mathrm{H}_{\mathbb{R}}^{2}$, where the Hermitian form is given by $\langle Z, Z\rangle=2 \operatorname{Re}\left(z_{1} \overline{z_{n+1}}\right)+\left|z_{2}\right|^{2}+\cdots+\left|z_{n}\right|^{2}$. This form provides especially nice coordinates for the stabilizer of a particular point at infinity, in the form of upper-triangular matrices.

Isometries: From (2) it is clear that $\operatorname{PU}(n, 1)$ acts by isometries on $\mathrm{H}_{\mathbb{C}}^{n}$, where $\mathrm{U}(n, 1)$ denotes the subgroup of $\operatorname{GL}(n+1, \mathbb{C})$ preserving $\langle\cdot, \cdot\rangle$, and $\operatorname{PU}(n, 1)$ its image in $\operatorname{PGL}(n+1, \mathbb{C})$. In fact, $\operatorname{PU}(n, 1)$ is the group of holomorphic isometries of $\mathrm{H}_{\mathbb{C}}^{n}$, and the full group of isometries $\operatorname{Isom}\left(\mathrm{H}_{\mathbb{C}}^{n}\right)$ is $\operatorname{PU}(n, 1) \rtimes \mathbb{Z} / 2$, where the $\mathbb{Z} / 2$ factor corresponds to a real reflection, that is, an antiholomorphic involution (see below).

Definition 2. A complex hyperbolic manifold is a quotient $\mathrm{H}_{\mathbb{C}}^{n} / \Gamma$ where $\Gamma$ is a torsion-free discrete subgroup of $\operatorname{PU}(n, 1)$. More generally, a manifold modelled on $\mathrm{H}_{\mathbb{C}}^{n}$, or in short, $\mathrm{H}_{\mathbb{C}}^{n}$-manifold, is a quotient $\mathrm{H}_{\mathbb{C}}^{n} / \Gamma$ with $\Gamma$ a torsion-free discrete subgroup of $\operatorname{Isom}\left(\mathrm{H}_{\mathbb{C}}^{n}\right)$.

Note that, since $\operatorname{PU}(n, 1)$ consists of holomorphic isometries, the complex (in fact Kähler) structure of $\mathrm{H}_{\mathbb{C}}^{n}$ descends to complex hyperbolic manifolds. On the other hand, if $\Gamma$ is a torsion-free discrete subgroup of $\operatorname{Isom}\left(\mathrm{H}_{\mathbb{C}}^{n}\right)$ containing an antiholomorphic isometry then the complex structure does not descend to the quotient $\mathrm{H}_{\mathbb{C}}^{n} / \Gamma$, and this quotient in fact does not admit any complex structure.

Holomorphic isometries of $\mathrm{H}_{\mathbb{C}}^{n}$ can be of three types, depending on the number and location of their fixed points. Namely, $g \in \operatorname{PU}(n, 1)-\{\mathrm{Id}\}$ is :
\begin{itemize}
\item[-] elliptic if it has a fixed point in $\mathrm{H}_{\mathbb{C}}^{n}$
\item[-] parabolic if it has (no fixed point in $\mathrm{H}_{\mathbb{C}}^{n}$ and) exactly one fixed point in $\partial \mathrm{H}_{\mathbb{C}}^{n}$
\end{itemize}
\begin{itemize}
\item[-] loxodromic: if it has (no fixed point in $\mathrm{H}_{\mathbb{C}}^{n}$ and) exactly two fixed points in $\partial \mathrm{H}_{\mathbb{C}}^{n}$
\end{itemize}

A parabolic isometry is called unipotent (or a Heisenberg translation) if it has a unipotent lift in $\mathrm{U}(n, 1)$; if not it is called ellipto-parabolic. In dimensions $n>1$, unipotent isometries are either 2-step or 3-step, according to whether the minimal polynomial of their unipotent lift is $(X-1)^{2}$ or $(X-1)^{3}$ (see section 3.4 of [CG]). We will usually call 2-step nilpotent isometries vertical Heisenberg translations and 3-step nilpotent isometries horizontal Heisenberg translations. This terminology reflects the position of the subspaces preserved by each type of isometry in the Heisenberg group, relative to its standard contact structure. Any two horizontal (resp. vertical) Heisenberg translations are conjugate under an isometry.

Totally geodesic subspaces and related isometries: A complex $k$-plane is a projective $k$-dimensional subspace of $\mathbb{C} P^{n}$ intersecting $\pi\left(V^{-}\right)$non-trivially (so, it is an isometrically embedded copy of $\mathrm{H}_{\mathbb{C}}^{k} \subset \mathrm{H}_{\mathbb{C}}^{n}$ ). Complex 1-planes are usually called complex lines.

A real $k$-plane is the projective image of a totally real $(k+1)$-subspace $W$ of $\mathbb{C}^{n, 1}$, i. e. a $(k+1)$-dimensional real vector subspace such that $\langle v, w\rangle \in \mathbb{R}$ for all $v, w \in W$. We will usually call real 2-planes simply real planes, or $\mathbb{R}$-planes. Every real $n$-plane in $\mathrm{H}_{\mathbb{C}}^{n}$ is the fixed-point set of an antiholomorphic isometry of order 2 called a real reflection or $\mathbb{R}$-reflection. The prototype of such an isometry is the map given in affine coordinates by:
$$\sigma:\left(z_{1}, \ldots, z_{n}\right) \mapsto\left(\overline{z_{1}}, \ldots, \overline{z_{n}}\right)$$
This is an isometry provided that the Hermitian form has real coefficients.
The Siegel model in dimension 2: As mentioned in the previous section, this model corresponds to the Hermitian form given by the matrix:
$$H=\left[\begin{array}{lll}
0 & 0 & 1 \\
0 & 1 & 0 \\
1 & 0 & 0
\end{array}\right]$$
In this model, any point $p \in \mathrm{H}_{\mathbb{C}}^{2}$ admits a unique lift to $\mathbb{C}^{2,1}$ of the following form, called its standard lift:
$$\mathbf{p}=\left[\begin{array}{c}
\left(-|z|^{2}-u+i t\right) / 2 \\
z \\
1
\end{array}\right] \text { with }(z, t, u) \in \mathbb{C} \times \mathbb{R} \times(0, \infty) .$$

The coordinates $(z, t, u)$ are called horospherical coordinates of $p$. The boundary at infinity $\partial_{\infty} \mathrm{H}_{\mathbb{C}}^{2}$ is the level set $\{u=0\}$, together with the distinguished point at infinity, given by
$$q_{\infty} \sim\left[\begin{array}{l}
1 \\
0 \\
0
\end{array}\right] .$$

Level sets $\left\{u=u_{0}\right\}$ with fixed $u_{0}>0$ are called horospheres based at $q_{\infty}$. The punctured boundary at infinity $\partial_{\infty} \mathrm{H}_{\mathbb{C}}^{2} \backslash\left\{q_{\infty}\right\}$ is a copy of the Heisenberg group Nil, identified as above with $\mathbb{C} \times \mathbb{R}$ with group law given by:
$$\left(z_{1}, t_{1}\right) \cdot\left(z_{2}, t_{2}\right)=\left(z_{1}+z_{2}, t_{1}+t_{2}+2 \operatorname{Im}\left(z_{1} \overline{z_{2}}\right)\right) .$$

The stabilizer of $q_{\infty}$ in $\operatorname{PU}(2,1)$ corresponds to upper triangular matrices, and is generated by the following 3 types of isometries: Heisenberg translations $T_{(z, t)}((z, t) \in \mathbb{C} \times \mathbb{R})$, Heisenberg rotations $R_{u}(u \in \mathrm{U}(1))$ and Heisenberg dilations $D_{r}(r>0)$, where:
$$T_{(z, t)}=\left[\begin{array}{ccc}
1 & -\bar{z} & -\left(|z|^{2}-i t\right) / 2 \\
0 & 1 & z \\
0 & 0 & 1
\end{array}\right] \quad R_{u}=\left[\begin{array}{ccc}
1 & 0 & 0 \\
0 & u & 0 \\
0 & 0 & 1
\end{array}\right] \quad D_{r}=\left[\begin{array}{ccc}
r & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1 / r
\end{array}\right] .$$
In Heisenberg coordinates, these correspond to the following:
\begin{itemize}
\item[-] $T_{(z, t)}$ is left multiplication by $(z, t):(w, s) \longmapsto(z, t) \cdot(w, s)$,
\item[-] $R_{u}$ is given by $(w, s) \longmapsto(u w, s)$,
\end{itemize}
\begin{itemize}
\item[-] $D_{r}$ is the Heisenberg dilation $(w, s) \longmapsto\left(r w, r^{2} s\right)$.
\end{itemize}

Heisenberg translations and rotations preserve each horosphere based at $q_{\infty}$ whereas Heisenberg dilations permute horospheres based at $q_{\infty}$. It turns out that the subgroup of $\operatorname{Stab}_{\mathrm{PU}(2,1)}\left(q_{\infty}\right)$ preserving each horosphere based at $q_{\infty}$ is Isom ${ }^{0}$ (Nil), the identity component of isometries for the Riemannian metric on Nil discussed in the previous section. Note that $\operatorname{Isom}^{0}(\mathrm{Nil})=\left\{P_{(z, t, u)} \mid z \in \mathbb{C}, t \in \mathbb{R}, u \in \mathrm{U}(1)\right\}$, where:
$$P_{(z, t, u)}=T_{[z, t]} R_{u}=\left[\begin{array}{ccc}
1 & -u \bar{z} & -\left(|z|^{2}-i t\right) / 2 \\
0 & u & z \\
0 & 0 & 1
\end{array}\right]$$
Moreover, denoting as above $\sigma$ complex conjugation in affine coordinates of $\mathrm{H}_{\mathbb{C}}^{2}, \sigma$ acts on Nil by $(z, t) \mapsto(\bar{z},-t)$ and:
$$\operatorname{Isom}(\mathrm{Nil})=\operatorname{Isom}^{0}(\mathrm{Nil}) \cup \operatorname{Isom}^{0}(\mathrm{Nil}) \sigma$$

For notational convenience we will denote $G=\operatorname{Isom}\left(\mathrm{H}_{\mathbb{C}}^{2}\right)=\langle\mathrm{PU}(2,1), \sigma\rangle, G^{0}=\operatorname{Isom}^{0}\left(\mathrm{H}_{\mathbb{C}}^{2}\right)=\mathrm{PU}(2,1)$ the subgroup of holomorphic isometries, and $G_{\infty}, G_{\infty}^{0}$ their respective subgroups preserving ( $q_{\infty}$ and) each horosphere based at $q_{\infty}$. That is:
$$\begin{aligned}
& G_{\infty}^{0}=\operatorname{Isom}^{0}(\mathrm{Nil})=\left\{P_{(z, t, u)} \mid z \in \mathbb{C}, t \in \mathbb{R}, u \in \mathrm{U}(1)\right\} \\
& G_{\infty}=\operatorname{Isom}(\mathrm{Nil})=\left\langle G_{\infty}^{0}, \sigma\right\rangle=G_{\infty}^{0} \cup G_{\infty}^{0} \sigma .
\end{aligned}$$

For any subring $R$ of $\mathbb{C}$ we likewise denote $G^{0}(R)$ (resp. $G_{\infty}^{0}(R)$ ) the subgroup of $G^{0}$ (resp. $G_{\infty}^{0}$ ) consisting of (images in PU( 2,1 ) of) matrices with entries in $R$. In the next subsection we will consider the groups with $R=\mathcal{O}_{d}$, the ring of integers of $\mathbb{Q}(i \sqrt{d})$, giving the Picard modular groups $G^{0}\left(\mathcal{O}_{d}\right)=\mathrm{PU}\left(2,1, \mathcal{O}_{d}\right)$ and the corresponding cusp subgroup $G_{\infty}^{0}\left(\mathcal{O}_{d}\right)$. By extension we will also denote $G\left(\mathcal{O}_{d}\right)=\left\langle G^{0}\left(\mathcal{O}_{d}\right), \sigma\right\rangle$ and $G_{\infty}\left(\mathcal{O}_{d}\right)=$ $\left\langle G_{\infty}^{0}\left(\mathcal{O}_{d}\right), \sigma\right\rangle$ their index-2 extensions obtained by adding the $\mathbb{R}$-reflection $\sigma$ defined in (3).

A (holomorphic) parabolic isometry is conjugate in $\operatorname{Isom}\left(\mathrm{H}_{\mathbb{C}}^{2}\right)$ to exactly one of the following:
\begin{itemize}
\item[-] $P_{(1,0,0)}=T_{[1,0]}$ if it is a horizontal Heisenberg translation (3-step unipotent),
\item[-] $P_{(0,1,0)}$ if it is a vertical Heisenberg translation (2-step unipotent),
\item[-] $P_{(0,1, \theta)}$ for some non-zero $\theta \in \mathbb{R} / 2 \pi \mathbb{Z}$ if it is ellipto-parabolic.
\end{itemize}

Also note that Heisenberg dilations act by conjugation as: $D_{r} P_{(z, t, u)} D_{r}^{-1}=P_{\left(r z, r^{2} t, u\right)}$ (for any $z \in \mathbb{Z}, t \in \mathbb{R}, u \in$ $\mathrm{U}(1), r>0)$. Recall also from [Sc] that the exact sequence:
$$1 \longrightarrow \mathbb{R} \longrightarrow \text { Nil } \xrightarrow{\Pi} \mathbb{C} \longrightarrow 1$$
induces an exact sequence:
$$1 \longrightarrow \operatorname{Isom}(\mathbb{R}) \longrightarrow \operatorname{Isom}(\operatorname{Nil}) \xrightarrow{\Pi_{*}} \operatorname{Isom}(\mathbb{C}) \longrightarrow 1 .$$
Explicitly: $\Pi_{*}\left(P_{(z, t, \theta)}\right)=\left(\begin{array}{cc}e^{i \theta} & z \\ 0 & 1\end{array}\right)$, acting on $\mathbb{C}$ by $w \mapsto e^{i \theta} w+z$, and $\Pi_{*}(\sigma)$ is complex conjugation in $\mathbb{C}$. In practice, we will write elements of $G_{\infty}^{0}$ as triples $(z, t, u)$ and compute products in $G_{\infty}$ by the following rules, which are straightforward from the matrix form $P_{(z, t, u)}$ above.

Lemma 2. Let $z_{1}, z_{2}, z \in \mathbb{C}, t_{1}, t_{2}, t \in \mathbb{R}$ and $u_{1}, u_{2}, u \in \mathrm{U}(1)$. Then:
\begin{itemize}
\item[1.] $\left(z_{1}, t_{1}, u_{1}\right) \cdot\left(z_{2}, t_{2}, u_{2}\right)=\left(u_{1} z_{2}+z_{1}, t_{1}+t_{2}+2 \operatorname{Im}\left(\overline{u_{1}} z_{1} \overline{z_{2}}\right), u_{1} u_{2}\right)$,
\item[2.] $\sigma(z, t, u)=(\bar{z},-t, \bar{u}) \sigma$.
\end{itemize}

In some of the representations below we will consider elements whose square is a vertical Heisenberg translation $(0, t, 1)$ (for some $t \in \mathbb{R}$ ). For this it is instructive to note that for any $z \in \mathbb{C}, t \in \mathbb{R},(z, t,-1)^{2}=(0,2 t, 1)$, that is: the square of any ellipto-parabolic with rotational part -1 is a vertical Heisenberg translation. At the other extreme:

Lemma 3. No antiholomorphic isometry in $G_{\infty}$ squares to a vertical Heisenberg translation. That is, for any $(z, t, u) \in G_{\infty}^{0}$, if $((z, t, u) \sigma)^{2}=\left(0, t^{\prime}, 1\right)$ for some $t^{\prime} \in \mathbb{R}$ then $t^{\prime}=0$.

Proof. By the above lemma, $((z, t, u) \sigma)^{2}=(z, t, u) \cdot(\bar{z},-t, \bar{u})=\left(u \bar{z}+z,-2 \operatorname{Im}\left(u \bar{z}^{2}\right), 1\right)$. Now if $u \bar{z}+z=0$, $u \bar{z}^{2}=-z \bar{z}$ and so $\operatorname{Im}\left(u \bar{z}^{2}\right)=0$. \(\square\)

\subsection*{2.3 Picard modular groups and their cusps}

Although the Nil-manifolds are more complicated than the flat 3-manifolds, the commensurability classes of cusped arithmetic complex hyperbolic 2-manifolds are easier to understand than that of their real counterparts.

A group of the form $\operatorname{PU}\left(2,1, \mathcal{O}_{d}\right)$, where $d \geqslant 1$ is a squarefree integer and $\mathcal{O}_{d}$ is the ring of integers of $\mathbb{Q}(i \sqrt{d})$, is called a Picard modular group. (Here we think of PU(2, 1) as corresponding to the Siegel model, with Hermitian form given in (4). See Section 3.1 of [St2] for a more general discussion involving different forms.)

Every non-cocompact, arithmetic lattice in $\operatorname{PU}\left(2,1, \mathcal{O}_{d}\right)$ is commensurable to a Picard modular group $\operatorname{PU}\left(2,1, \mathcal{O}_{d}\right)$ for some $d$, and no two distinct $\operatorname{PU}\left(2,1, \mathcal{O}_{d}\right)$ are commensurable (see [St2]). In other words, passing to the quotient orbifolds $\mathrm{H}_{\mathbb{C}}^{2} / \mathrm{PU}\left(2,1, \mathcal{O}_{d}\right)$, the commensurability classes of arithmetic complex hyperbolic 2-manifolds are in bijective correspondence with the Picard modular groups. (Note that, as all Picard modular groups contain torsion (see below), the corresponding quotients are not manifolds.)

Cusp subgroups of Picard modular groups:
The Picard modular groups are non-cocompact lattices, hence contain parabolic elements. In fact, it is clear from the matrix form (8) that they all have the point $q_{\infty}=[1,0,0]^{T}$ as a cusp point (that is, a fixed point of a parabolic isometry in the group). We will denote by $\Gamma_{\infty}(d)$ the corresponding cusp subgroup of $\operatorname{PU}\left(2,1, \mathcal{O}_{d}\right)$, that is, the stabilizer of $q_{\infty}$ in $\operatorname{PU}\left(2,1, \mathcal{O}_{d}\right)$. (In the above notation 9, $\Gamma_{\infty}(d)=G^{0} \infty\left(\mathcal{O}_{d}\right)$ ).

These subgroups have been explicitly described in [FP] $(d=3)$, [FFP] $(d=1)$ and [PW] (all other $d)$, in terms of the exact sequence (12). We will denote by $\Gamma_{\infty}^{v}(d), \Gamma_{\infty}^{h}(d)$ the vertical and horizontal parts of $\Gamma_{\infty}(d)$, that is the kernel and image of the homomorphism $\Pi_{*}$, so that the exact sequence becomes, when restricted to $\Gamma_{\infty}(d)$ :
$$1 \longrightarrow \Gamma_{\infty}^{v}(d) \longrightarrow \Gamma_{\infty}(d) \xrightarrow{\Pi_{*}} \Gamma_{\infty}^{h}(d) \longrightarrow 1 .$$
Combining Proposition 3.1 of [FP], Proposition 2 of [FFP] and Lemma 5.2 of [PW] gives the following, where we denote $\Delta(p, q, r)$ the orientation-preserving $(p, q, r)$-triangle group in $\operatorname{Isom}(\mathbb{C})$ :

Proposition 1. (a) For all $d, \Gamma_{\infty}^{v}(d)$ is generated by the vertical Heisenberg translation $T_{(0,2 \sqrt{d})}$.
\begin{itemize}
\item[(b)] $\Gamma_{\infty}^{h}(3)=\Delta(2,3,6) ; \Gamma_{\infty}^{h}(1)$ has index 2 in $\operatorname{Isom}^{+}(\mathbb{Z}[i])=\Delta(2,4,4)$.
\item[(c)] For all other $d, \Gamma_{\infty}^{h}(d)=\operatorname{Isom}^{+}\left(\mathcal{O}_{d}\right)$ if $d \equiv 3(\bmod 4) ; \Gamma_{\infty}^{h}(d)$ has index 2 in $\operatorname{Isom}^{+}\left(\mathcal{O}_{d}\right)$ if $d \equiv 1,2(\bmod 4)$.
\end{itemize}

Remarks:
\begin{itemize}
\item[-] In part (a), Lemma 5.2 of [PW] mistakenly stated $T_{(0, \sqrt{d})}$ instead of $T_{(0,2 \sqrt{d})}$ (the former has entry $i \sqrt{d} / 2$ in the top-right corner, which is not in $\mathcal{O}_{d}$ ).
\item[-] Recall that $\mathcal{O}_{d}=\mathbb{Z}[\tau]$, where $\tau=i \sqrt{d}$ if $d \equiv 1,2(\bmod 4)$ and $\tau=\frac{1+i \sqrt{d}}{2}$ if $d \equiv 3(\bmod 4)$. In part (c), for $d \neq 1,3, \operatorname{Isom}^{+}\left(\mathcal{O}_{d}\right)$ is generated by the translations by 1 and $\tau$ and a half-turn. The corresponding half-turn is a torsion element in $\Gamma_{\infty}(d)$ for all $d$.
\end{itemize}

\subsection*{2.4 Non-arithmetic lattices in $\operatorname{PU}(2,1)$ and their cusps}

Non-arithmetic lattices in PU(2,1) were constructed by Mostow and Deligne-Mostow in the 1980's, and more recently by Deraux, Parker and the first author in [DPP1], [DPP2]. The latter paper classified the known examples up to commensurability, showing that they fall into 22 commensurability classes, 10 of which consist of cusped lattices (Table 11 of [DPP2] gives 11 such classes, but the class containing $\Gamma(3,1 / 12)$ and $\Gamma(8,7 / 24)$ is in fact cocompact, see Appendix A.9). A key geometric fact is that each of the 22 classes contains a group generated by 3 complex reflections with the same order $p \geqslant 3$.

We do not need to review details of the construction or notation; we simply collect here the information about the cusp groups for those lattices that are non-cocompact, see Section 7.2.2 of [DPP2]. These all have $p=3$, 4 or 6, and the cusp group $\Gamma_{\infty}$ is generated by two complex reflections $A, B$ of order $p$. As we did for the Picard modular groups in (13), we characterize each of these cusp groups by its horizontal part $\Gamma_{\infty}^{h}$ and vertical part $\Gamma_{\infty}^{v}$ in the exact sequence (12). In all three cases, $\Gamma_{\infty}^{h}$ is a triangle group and $\Gamma_{\infty}^{v}$ is generated by a vertical translation $T$ which is a power of $A B$. More precisely:

Lemma 4. ● When $p=3, \Gamma_{\infty}^{h}=\Delta(3,3,3)$ and $\Gamma_{\infty}^{v}=\langle T\rangle$ with $T=(A B)^{3}$.
\begin{itemize}
\item[-] When $p=4, \Gamma_{\infty}^{h}=\Delta(2,4,4)$ and $\Gamma_{\infty}^{v}=\langle T\rangle$ with $T=(A B)^{2}$.
\item[-] When $p=6, \Gamma_{\infty}^{h}=\Delta(2,3,6)$ and $\Gamma_{\infty}^{v}=\langle T\rangle$ with $T=(A B)^{3}$.
\end{itemize}

For completeness we note that all three cases above occur as a cusp group for some non-arithmetic lattice, see again Table 11 of [DPP2]. Comparing this with the description of the cusp groups $\Gamma_{\infty}(d)$ of the Picard modular groups with $d=1,3$ above, we get:

Corollary 1. The non-arithmetic complex triangle groups with $p=6$ have a cusp group isomorphic to $\Gamma_{\infty}(3)=$ $G_{\infty}^{0}\left(\mathcal{O}_{3}\right)$. The non-arithmetic complex triangle groups with $p=4$ have a cusp group containing an index-2 subgroup isomorphic to $\Gamma_{\infty}(1)=G_{\infty}^{0}\left(\mathcal{O}_{1}\right)$.

In order to realize all Nil-manifold groups as cusp groups of non-arithmetic orbifolds in Section 3.2 we will also need to use the fact that these non-arithmetic lattices are generated by $\mathbb{R}$-reflections, in the sense that they have index 2 in a group generated by $\mathbb{R}$-reflections (recall that the latter are the anitholomorphic involutions in $\operatorname{Isom}\left(H_{\mathbb{C}}^{2}\right)$ ). More specifically, it was shown in Section 2.2 of [DFP] that any symmetric complex triangle group $\Gamma(p, t)$ or $\mathcal{S}(p, \tau)$ is contained (with index 2 or 6) in a group $\widetilde{\Gamma}(p, t)$ or $\widetilde{\mathcal{S}}(p, \tau)$ generated by (three) $\mathbb{R}$-reflections. Moreover one of these three $\mathbb{R}$-reflections, $\sigma_{12}$ in the notation of [DFP], stabilizes the cusp point $q_{\infty}$. From this (using again Table 11 of [DPP2]) we record the following:

Corollary 2. • The non-arithmetic lattices $\widetilde{\Gamma}(6,1 / 6), \widetilde{\mathcal{S}}\left(6, \sigma_{1}\right)$ and $\widetilde{\mathcal{S}}\left(6, \overline{\sigma_{4}}\right)$ have a cusp group isomorphic to $G_{\infty}\left(\mathcal{O}_{3}\right)$.
\begin{itemize}
\item[-] The non-arithmetic lattices $\widetilde{\mathcal{S}}\left(4, \sigma_{1}\right), \widetilde{\mathcal{S}}\left(4, \sigma_{5}\right)$ and $\widetilde{\mathcal{S}}\left(4, \bar{\sigma}_{4}\right)$ have a cusp group isomorphic to $G_{\infty}\left(\mathcal{O}_{1}\right)$.
\end{itemize}

\section*{3 Nil-manifolds and cusp cross-sections}

In this section we prove Theorems 1 and 2. We start by recalling some relevant results from [M1] and [M2]. In the context of complex hyperbolic 2-orbifolds/manifolds and their cusp cross-sections, the main result of [M1] and [M2] is the following (Corollary 1.6 of [M2]).

Theorem 6 ([M2]). Every Nil-manifold is diffeomorphic to to a cusp cross-section of an arithmetic complex hyperbolic 2-manifold.

The proof of Theorem 6 proceeds in three main steps: (1) Given any Nil-manifold $N$, find a faithful representation $\rho: \pi_{1}(N) \longrightarrow \Gamma$ for some arithmetic lattice $\Gamma$ in PU(2, 1). Geometrically, this realizes a $\pi_{1}$-injective immersion of $N$ into a cusp cross-section of the orbifold $M=\mathrm{H}_{\mathbb{C}}^{2} / \Gamma$. Step (2) is then to show that this immersion can be promoted to an embedding in a finite cover $M^{\prime}=\mathrm{H}_{\mathbb{C}}^{2} / \Gamma^{\prime}$ of $M$ using a separability argument, so that $N$ is now embedded as the cross-section.of a cusp of $M^{\prime}$. Step (3), accomplished in [M2], is to refine the previous step to a further manifold cover $M^{\prime \prime}$, so that $N$ is a cusp cross-section of the manifold $M^{\prime \prime}$.

We now give more details about step (1) using some notation introduced earlier, as we will be extending the results from this step in the next section. Denote as above $G_{\infty}^{0}\left(\mathcal{O}_{d}\right)=G_{\infty}^{0} \cap \mathrm{PU}\left(2,1, \mathcal{O}_{d}\right)$ and $G_{\infty}\left(\mathcal{O}_{d}\right)=$ $\left\langle G_{\infty}^{0}\left(\mathcal{O}_{d}\right), \sigma\right\rangle$, with $G_{\infty}, G_{\infty}^{0}$ defined in (9). Note that, from the matrix form 8, $G_{\infty}^{0}\left(\mathcal{O}_{d}\right)=\left\{(z, t, u) \mid z,\left(-|z|^{2}+\right.\right.$ $\left.i t) / 2, u \in \mathcal{O}_{d}\right\}$.

Recall that a holonomy representation of a Nil-manifold group $\pi_{1}(N)$ is a representation $\rho: \pi_{1}(N) \longrightarrow$ $G_{\infty} \simeq \operatorname{Isom}(\mathrm{Nil})$ such that $\operatorname{Nil} / \rho\left(\pi_{1}(N)\right)$ is diffeomorphic to $N$. By Lemma 1, this is equivalent to $\rho$ being discrete, faithful and cocompact.

The first part of the following statement is Theorem 7.1 of [M1]. The second part collects case-by-case information from the explicit representations given there in the Appendix.

Theorem 7 ([M1]). For any Nil-manifold $N$, there exists a faithful (discrete, cocompact) representation $\rho$ : $\pi_{1}(N) \longrightarrow G_{\infty}\left(\mathcal{O}_{d}\right)$ with $d=1$ or 3. More precisely, when $N$ belongs to families (1), (2) or (5) (Nil-torus, vertical half-twist, or 1/4-twist) the image of $\rho$ is contained in $G_{\infty}^{0}\left(\mathcal{O}_{1}\right)$; when $N$ belongs to families (3) or (4) (horizontal half-twist or double half-twist) the image of $\rho$ is contained in $G_{\infty}\left(\mathcal{O}_{1}\right)$, and when $N$ belongs to families (6) or (7) (1/3-twist or 1/6-twist) the image of $\rho$ is contained in $G_{\infty}^{0}\left(\mathcal{O}_{3}\right)$.

\subsection*{3.1 Nil-manifolds and commensurability classes of Picard modular groups}

We are now ready to prove our main results.
Theorem 1, Let $N$ be any Nil 3-manifold in families (1), (2), (3) or (4) (Nil-tori, vertical or horizontal halftwist, or double half-twist). Then $N$ occurs as a cusp cross-section in the commensurability class of the Picard modular group $\operatorname{PU}\left(2,1, \mathcal{O}_{d}\right)$ for any squarefree $d \geqslant 1$.

In fact we show the following, which implies the conclusion of the theorem. This is a generalization of Theorem 7 for arbitrary $d$, and Steps (2) and (3) described above as in [M1] and [M2] imply that $N$ is then diffeomorphic to a cusp cross-section of a manifold in the given commensurability class.

Lemma 5. The Nil-torus and vertical half-twist groups admit a holonomy representation into $G_{\infty}^{0}\left(\mathcal{O}_{d}\right)$ for any $d$; the horizontal and double half-twist groups admit a holonomy representation into $G_{\infty}\left(\mathcal{O}_{d}\right)$ for any $d$. More precisely, with the notation of the presentations in Section 2.1, these are given by:
\begin{itemize}
\item[1.] (Nil-torus) $a \mapsto(2 k, 0,1), b \mapsto(2 k i \sqrt{d}, 0,1), c \mapsto(0,16 k \sqrt{d}, 1)$,
\item[2.] (Vertical half-twist) $a \mapsto(2 k, 0,1), b \mapsto(2 k i \sqrt{d}, 0,1), c \mapsto(0,16 k \sqrt{d}, 1), \alpha \mapsto(0,8 k \sqrt{d},-1)$,
\item[3.] (Horizontal half-twist) $a \mapsto(2 k, 0,1), b \mapsto(2 k i \sqrt{d}, 0,1), c \mapsto(0,8 k \sqrt{d}, 1), \alpha \mapsto(k, 0,1) \sigma$,
\item[4.] (Double half-twist) $a \mapsto(2 k, 0,1), b \mapsto(2 k i \sqrt{d}, 0,1), c \mapsto(0,8 k \sqrt{d}, 1), \alpha \mapsto(-k(1+i \sqrt{d}), 4 k \sqrt{d},-1)$, $\beta \mapsto(k, 0,1) \sigma$.
\end{itemize}

Proof. The fact that these formulas define representations, that is, that the images of the generators satisfy the relations of the presentation, can directly be checked using Lemma 2. We give more details below for the double half-turn family (4), in particular since the representation given in [M1] for that family is not correct (the matrix given there in the Appendix for $\alpha$ does not satisfy the relation $\alpha^{2}=c$ ).

The fact that these representations are faithful follows directly from Lemma 7.2 of [M1]. They are clearly discrete as their image belongs to the discrete subgroup $G_{\infty}\left(\mathcal{O}_{d}\right)$, and they have cocompact image in Nil as the images of $a, b, c$ already generate a lattice in Nil. Therefore, by Lemma 1 these representations are all holonomy representations of the corresponding $\pi_{1}(N)$.

We now give more details for family (4). We follow essentially the same strategy as in [M1], by first finding a representation in $G_{\infty}$, then conjugating it by a suitable dilation to have entries in $\mathcal{O}_{d}$. We do this in several steps; all computations are reasonably done by hand, using Lemma 2.
\begin{itemize}
\item[-] We first take $\rho(a)=(1,0,1)$ and $\rho(b)=(0, i \sqrt{d}, 1)$. This gives $[\rho(b), \rho(a)]=(0,4 \sqrt{d}, 1)$, so we take $\rho(c)=(0,2 \sqrt{d} / k)$ to satisfy the relation $[b, a]=c^{2 k}$.
\item[-] Next we seek $\rho(\alpha)=(z, t, u)$ satisfying the relations: $\alpha^{2}=c, \alpha a=a^{-1} \alpha c^{k}(1)$, and $\alpha b=b^{-1} \alpha c^{-k}(2)$. (The presentation also lists $[c, \alpha]=\mathrm{Id}$ but this follows from $\alpha^{2}=c$ ). The relation $\alpha^{2}=c$ implies $u= \pm 1$; we take $u=-1$ (or else $\alpha$ would commute with $c$ ). Taking $t=\sqrt{d} / k$ gives $\alpha^{2}=c$ (independently of the value of $z$ ). We then solve for $z$ using relations (1) and (2). The former gives $\operatorname{Im} z=-\sqrt{d} / 2$ and the latter $\operatorname{Re} z=-1 / 2$. Therefore, taking $z=-(1+i \sqrt{d}) / 2$ gives all the above relations. (Note: the matrix given for $\rho(\alpha)$ in the Appendix of [M1] corresponds to $(z, t, u)=(2 k(1+i), 0,-1)$, which squares to the identity, not to $\rho(c)=(0,32 k, 1)$.)
\item[-] We then seek $\rho(\beta)=(z, t, u) \sigma$ satisfying the relations: $\beta^{2}=a, \beta c=c^{-1} \beta$, and $\beta b=b^{-1} \beta c^{-k}$. (The presentation also lists $[a, \beta]=$ Id but this follows from $\beta^{2}=a$ ). We try $\beta=(x, 0,1) \sigma$ (for some $x \in \mathbb{R}$ ) as in [M1]. Taking $x=1 / 2$ gives the relation $\beta^{2}=a$. We then check that the other two relations hold.
\item[-] We then check that the last relation $\alpha \beta=a^{-1} b^{-1} \beta \alpha c^{-k-1}$ is also satisfied.
\end{itemize}
\begin{itemize}
\item[-] Finally, we conjugate by a dilation of factor $2 k$ in order for $\rho$ to have image contained in $G_{\infty}\left(\mathcal{O}_{d}\right)$, giving the formulas in the statement of the Lemma.
\end{itemize} \(\square\)

Note that in the representations above, any Nil-manifold in family (3) or (4) has a generator ( $\alpha$ or $\beta$, respectively) which maps to an isometry induced by an antiholomorphic isometry of $\mathrm{H}_{\mathbb{C}}^{2}$. Recall that a complex hyperbolic manifold is a quotient $\mathrm{H}_{\mathbb{C}}^{n} / \Gamma$ where $\Gamma$ is a torsion-free discrete subgroup of the holomorphic isometry group $\operatorname{PU}(n, 1) \simeq \operatorname{Isom}^{0}\left(\mathrm{H}_{\mathbb{C}}^{n}\right)$, and more generally an $\mathrm{H}_{\mathbb{C}}^{n}$-manifold is a quotient $\mathrm{H}_{\mathbb{C}}^{n} / \Gamma$ where $\Gamma$ is a torsion-free discrete subgroup of $\operatorname{Isom}\left(\mathrm{H}_{\mathbb{C}}^{n}\right)$. We slightly abuse terminology by calling holomorphic (resp. antiholomorphic) isometries of Nil which are induced by holomorphic (resp. antiholomorphic) isometries of $\mathrm{H}_{\mathbb{C}}^{2}$.

Theorem 3. Let $N$ be any Nil 3-manifold in families (3) or (4) (horizontal half-twist or double half-twist). Then $N$ occurs as a cusp cross-section of an $\mathrm{H}_{\mathbb{C}}^{2}$-manifold, but not of any complex hyperbolic manifold or orbifold. That is, the image of any holonomy representation $\rho: \pi_{1}(N) \longrightarrow G_{\infty} \simeq \operatorname{Isom}(\mathrm{Nil})$ must contain anitholomorphic isometries.

Proof. This follows from the second generalized Bieberbach theorem, Theorem5 (2) above. Indeed, automorphisms of Nil are induced by isometries of $\mathrm{H}_{\mathbb{C}}^{2}$ (see e.g. Section 2.4 of [M1]), hence conjugation by any element of the affine group Nil ★ Aut(Nil) preserves holomorphicity (resp. antiholomorphicity). Moreover, the holonomy representations produced above (and in [M1]) for these two families contain antiholomorphic isometries.

We now give a more pedestrian proof using computations similar to the ones above. Auslander showed (Proposition 2 of [A]) that, if $\Gamma$ is a discrete cocompact subgroup of $N \rtimes C$ (with as previously, $N$ a simplyconnected nilpotent Lie group and $C$ a compact Lie subgroup of $\operatorname{Aut}(N)$ ), then $\Gamma \cap N$ is a maximal nilpotent normal subgroup of $\Gamma$. (Dekimpe points out in [Dek] that one can remove the word "normal", with the same proof). In the notation of the presentations of Nil-manifold groups given in Section 2.1, the maximal nilpotent subgroup (called fitting subgroup in [Dek] and [M1]) is $\langle a, b, c\rangle$.

By this result, if $\rho: \pi_{1}(N) \longrightarrow G_{\infty}$ is a holonomy representation of $\pi_{1}(N)$ (that is, by Lemma 1, discrete, faithful and cocompact) then $\rho(a), \rho(b), \rho(c)$ must be Heisenberg translations. Moreover, $\rho(a)$ and $\rho(b)$ must be horizontal Heisenberg translations, or else they would commute with each other (and $\rho$ would not be faithful). That is, they are of the form $(z, t, 1)$ with $z \neq 0$ in $(z, t, u)$-coordinates on Nil $\rtimes \mathrm{U}(1)$. Now, in the horizontal half-twist family (3), the element $\alpha$ satisfies $\alpha^{2}=a$. Assuming that $\rho(\alpha)$ is a holomorphic isometry of Nil, that is of the form $(z, t, u) \in \mathrm{Nil} \rtimes \mathrm{U}(1)$, by Lemma 2 we would have $\rho(\alpha)^{2}=\left(u z+z, 2 t, u^{2}\right)$. Therefore $u^{2}=1$, that is $u= \pm 1$. But if $u=1, \rho(\alpha)$ would commute with $\rho(c)$, contradicting again faithfulness of $\rho$ (in the presentation, $\alpha$ and $c$ satisfy $\alpha c=c^{-1} \alpha$ ). Therefore $u=-1$, hence $\rho(\alpha)^{2}=(0,2 t, 1)$, a vertical Heisenberg translation, contradicting the fact that $\rho(a)$ is a horizontal Heisenberg translation. Therefore $\rho(\alpha)$ must be antiholomorphic.

For the double half-twist family (4) one argues similarly with the element $\rho(\beta)$ satisfying $\rho(\beta)^{2}=a$. \(\square\)

To complete the proof of Theorem 2, we must obstruct certain Nil-manifolds from appearing as cross-sections in all but one commensurability class (of Picard modular groups). Note that it is not enough to obstruct them from appearing as a subgroup of the "standard cusp" (represented above by the vector $(1,0,0)^{T}$ ); the standard cusp is the only cusp of $X_{d}=\mathrm{H}_{\mathbb{C}}^{2} / \mathrm{PU}\left(2,1, \mathcal{O}_{d}\right)$ exactly when the ideal class number of $\mathbb{Q}(i \sqrt{d})$ is 1 (that is, when $d=1,2,3,7,11,19,43,67$, or 163).

Theorem 2. The Nil 3-manifolds in families (5), (6), and (7) (1/4-twist, 1/3-twist and 1/6-twist) each occur as cusp cross-sections in a single arithmetic commensurability class. For the 1/4-twist, this is the commensurability class of the Gauss-Picard modular group $\mathrm{PU}\left(2,1, \mathcal{O}_{1}\right)$, and for the 1/3-twist and 1/6-twist, this is the commensurability class of the Eisenstein-Picard modular group $\operatorname{PU}\left(2,1, \mathcal{O}_{3}\right)$.

Proof. The forward direction - that the Nil-manifolds do occur in the single commensurability class given - was proven directly in [M1], providing explicit holonomy representations into the corresponding $G_{\infty}^{0}\left(\mathcal{O}_{d}\right)=$ $G_{\infty}^{0} \cap \mathrm{PU}\left(2,1, \mathcal{O}_{d}\right)$ (Section 9 of [M1]). We provide explicit representations here, because some of the ones given in [M1] had minor errors, and because they were given in a different form (as matrices in $U(2,1)$ rather than as points in Isom(Nil)). With the notation of the presentations in Section 2.1, we have:
\begin{itemize}
\item[5.] (1/4-twist) $a \mapsto(2 k, 0,1), b \mapsto(2 k i, 0,1), c \mapsto(0,16 k, 1), \alpha \mapsto(0,4 p k, i)$,
\item[6.] (1/3-twist) $a \mapsto(24 k, 0,1), b \mapsto((-12+12 \sqrt{-3}) k, 0,1), c \mapsto(0,1152 k \sqrt{3}, 1)$, $\alpha \mapsto\left(-6 k+6 k \sqrt{-3}-12 k_{1}-12 k_{1} \sqrt{-3}, 384 k k_{2} \sqrt{3}+48 k^{2} \sqrt{3}-96 k k_{1} \sqrt{3}+192 k_{1}^{2} \sqrt{3}, \frac{-1+\sqrt{-3}}{2}\right)$,
\item[7.] (1/6-twist) $a \mapsto(12 k, 0,1), b \mapsto((-6+6 \sqrt{-3}) k, 0,1), c \mapsto(0,288 k \sqrt{3}, 1)$, $\alpha \mapsto\left(6 k, 36 k^{2} \sqrt{3}+48 k k_{1} \sqrt{3}, \frac{1+\sqrt{-3}}{2}\right)$.
\end{itemize}

Now let $N$ be a Nil-manifold in family (5), (6) or (7), and let $\rho: \pi_{1}(N) \longrightarrow G_{\infty} \simeq \operatorname{Isom}($ Nil $)$ be a holonomy representation of $\pi_{1}(N)$ with image contained in a subgroup $\Gamma$ of $\operatorname{Isom}\left(\mathrm{H}_{\mathbb{C}}^{2}\right)$ commensurable to a Picard modular group $\operatorname{PU}\left(2,1, \mathcal{O}_{d}\right)$. As in the proof of the previous theorem, by the second generalized Bieberbach theorem all elements of $\rho\left(\pi_{1}(N)\right)$ must be holomorphic, since this is the case for the holonomy representations found in [M1]. Therefore we may assume that $\Gamma$ is contained in $\operatorname{PU}(2,1)$; since it is also commensurable to $\operatorname{PU}\left(2,1, \mathcal{O}_{d}\right)$, $\Gamma$ is contained in $\operatorname{PU}\left(2,1, E_{d}\right)$ where $E_{d}=\mathbb{Q}(i \sqrt{d})$ is the field of definition of the commensurability class (see Section 3.1 of [St2]).

Now let $A \in \mathrm{U}\left(2,1, E_{d}\right)$ be the matrix representative of $\rho(\alpha)$ of the form $P_{(z, t, u)}$ as in Equation 8, with $(z, t, u) \in \mathrm{Nil} \rtimes U(1)$. Again by the second generalized Bieberbach theorem, $\rho(\alpha)$ is affinely conjugate to the corresponding $P_{(z, t, u)}$ for the relevant McReynolds representation, which as noted above has $u=\zeta_{4}, \zeta_{3}, \zeta_{6}$ for the 1/4-twist, 1/3-twist and 1/6-twist families respectively. Note that the matrix $P_{(z, t, u)}$ has eigenvalues 1, 1, $u$. Since, as also noted above, automorphisms of Nil are induced by isometries of $\mathrm{H}_{\mathbb{C}}^{2}$ (which are in turn either matrices or matrices preceded by complex conjugation of coordinates), affine conjugation by an element of Nil ★ Aut(Nil) either preserves the eigenvalues of the matrix $A$, or maps them to their complex conjugates. Therefore the matrix $A$ has eigenvalues $1,1, u$ with $u=\zeta_{4}, \zeta_{3}, \zeta_{6}$ or their complex conjugates.

But the eigenvalues of $A$ must lie in a cubic extension of $E_{d}$, since $A$ is a 3 × 3 matrix with entries in $E_{d}$. However the elements $u=\zeta_{4}, \zeta_{3}, \zeta_{6}$ and their complex conjugates do not lie in any cubic extension of $E_{d}$, except $E_{4}=\mathbb{Q}(i)$ itself for $\zeta_{4}$ and its complex conjugate, and $E_{3}=\mathbb{Q}\left(\zeta_{3}\right)$ for $\zeta_{3}, \zeta_{6}$ and their complex conjugates. Therefore $d=1$ if $N$ belongs to the 1/4-twist family, and $d=3$ if $N$ belongs to the 1/3- or 1/6-twist family. □

\subsection*{3.2 Nil-manifolds and cusp cross-sections of non-arithmetic manifolds}

We finish with the following result about cusps of non-arithmetic manifolds.
Theorem 4. Every Nil 3-manifold occurs as the cusp cross-section of a non-arithmetic complex hyperbolic 2-manifold or $\mathrm{H}_{\mathbb{C}}^{2}$-manifold.

Proof. This follows the strategy of proof of Theorem 6 given in [M1] and [M2], outlined after the statement of Theorem 6. Step (1) essentially follows from Theorem 7 and Corollary 1. More precisely, by Theorem 7, for any Nil-manifold $N$ there exists a faithful (discrete, cocompact) representation $\rho_{1}: \pi_{1}(N) \longrightarrow G_{\infty}\left(\mathcal{O}_{d}\right)$ with $d=1$ or 3. But, by Corollary 2, there exist non-arithmetic lattices $\Gamma$ in $\operatorname{PU}(2,1)$ whose cusp group is exactly $G_{\infty}\left(\mathcal{O}_{d}\right)$ with $d=1$ or 3 . This provides a discrete, faithful representation $\rho_{2}: \pi_{1}(N) \longrightarrow \Gamma_{\infty}$ with $\Gamma_{\infty}$ a cusp subgroup of a non-arithmetic lattice $\Gamma$.

We want to promote this, as in steps (2) and (3) the proof of Theorem 6, to show that $N$ occurs as a cross-section of a (non-arithmetic) manifold covering the non-arithmetic orbifold $\mathrm{H}_{\mathbb{C}}^{2} / \Gamma$. Step (2) is to find a finite-index subgroup $\Gamma_{1}<\Gamma$ (possibly with torsion) such that $\pi_{1}(N)$ is the full cusp subgroup of $\Gamma_{1}$, promoting the immersion of $N$ to an embedding as in Theorem 3.12 of [M1]. Step (3) is to find a further finite-index subgroup $\Gamma_{2} \leqslant \Gamma_{1}$ which is torsion-free but still has a cusp subgroup isomorphic to $\pi_{1}(N)$, as in Corollary 1.6 of [M2].

We now give more details for these last two steps, as the relevant results of [M1] and [M2] are stated there for arithmetic lattices. For step (2) we use the following result of Bergeron ("Lemme principal" of [B], as stated in Proposition 3.8 of [M1]):

Proposition 2 ([B]). Let $H$ be an algebraic subgroup of a linear algebraic group $G$ and $\Gamma$ a finitely generated subgroup of $G$. Then $H \cap \Gamma$ is separable in $\Gamma$.

Taking $G=\operatorname{SU}(2,1), H=\operatorname{Stab}_{G}\left(q_{\infty}\right)$ and $\Gamma$ any lattice in $G$ (arithmetic or not), this gives that the cusp subgroup $\Gamma_{\infty}=\Gamma \cap H$ is separable in $\Gamma$. (Note that $H$ is an algebraic subgroup of $G$ as it consists of all uppertriangular matrices in $G$ ). The result of step (2) then follows; that is, Theorem 3.12 of [M1] holds without the arithmetic assumption, with the same proof. We now have a non-arithmetic lattice $\Gamma_{1}$ in $\operatorname{SU}(2,1)$ such that $N$ is diffeomorphic to a cusp cross-section of the orbifold $\mathrm{H}_{\mathbb{C}}^{2} / \Gamma_{1}$. In other words, we have a discrete, faithful representation $\rho_{3}: \pi_{1}(N) \longrightarrow \Gamma_{1}$ such that $\rho_{3}\left(\pi_{1}(N)\right)$ is exactly a cusp stabilizer in $\Gamma_{1}$.

For Step (3) we show that the relevant results of [M2] still apply in the non-arithmetic but integral case. We first recall the following result, Corollary 5.3 of [M2]:

Theorem 8 ([M2]). Let $\Lambda_{1}$ be a torsion-free virtually unipotent subgroup of an arithmetic lattice $\Lambda$. Then there exists a torsion-free finite-index subgroup $\Lambda_{0}$ of $\Lambda$ containing $\Lambda_{1}$.

We now recall that all known non-arithmetic lattices in SU(2,1) are integral in the following sense (see e.g. Section 3.1 of [DPP1]). For each such lattice $\Gamma_{1}$ there exists a totally real number field $k$ (in fact, the adjoint trace field $\mathbb{Q}\left[\operatorname{Tr} \operatorname{Ad} \Gamma_{1}\right]$ ) and an imaginary quadratic extension $L$ of $k$ such that $\Gamma_{1}<\operatorname{SU}\left(H, \mathcal{O}_{L}\right)$ for some Hermitian form $H$ of signature (2,1) defined over $L$. Denoting $\operatorname{Gal}(L / \mathbb{Q})=\left\{\mathrm{Id}=\sigma_{1}, \ldots, \sigma_{n}\right\}$, this provides an injective homomorphism:
$$\begin{aligned}
\varphi: \Gamma_{1} & \longrightarrow \Pi_{i=1}^{n} \operatorname{SU}\left(\sigma_{i} H, \mathcal{O}_{L}\right) \\
\gamma & \longmapsto\left({ }^{\sigma_{1}} \gamma, \ldots,{ }^{\sigma_{n}} \gamma\right)
\end{aligned}$$
where, for any $\sigma \in \operatorname{Gal}(L / \mathbb{Q})$ and $\gamma \in \Gamma_{1},{ }^{\sigma} \gamma$ denotes the matrix obtained from $\gamma$ by applying $\sigma$ to the entries of $\gamma$; likewise ${ }^{\sigma} H$ denotes the Hermitian matrix obtained from $H$ by applying $\sigma$ to the entries of $H$ (this is still a Hermitian matrix by the assumptions on $L$, as each $\sigma$ commutes with complex conjugation).

Now $\Lambda=\Pi_{i=1}^{n} \mathrm{SU}\left({ }^{\sigma_{i}} H, \mathcal{O}_{L}\right)$ is an arithmetic lattice. Indeed, by restriction of scalars (more specifically, choosing a $\mathbb{Q}$-basis for $L$ which is also a $\mathbb{Z}$-basis for $\mathcal{O}_{L}$ ), we get a linear algebraic group $G^{\prime}$ defined over $\mathbb{Q}$ such that $\Lambda \simeq G^{\prime}(\mathbb{Z})$, which is therefore an arithmetic lattice in $G^{\prime}(\mathbb{R}) \simeq \Pi_{i=1}^{n} \mathrm{SU}\left({ }^{\sigma_{i}} H\right)$ by the Borel-Harish-Chandra theorem (see e.g. Section 5.5 of [WM] for this now classical construction). Note that $\varphi\left(\Gamma_{1}\right)$ has infinite index in $\Lambda$ since $\Gamma_{1}$ is non-arithmetic.

Note also that for any $\sigma \in \operatorname{Gal}(L / \mathbb{Q})$ and $\gamma \in \Gamma_{1},{ }^{\sigma} \gamma$ is unipotent (resp. finite-order) if and only $\gamma$ is, hence $\varphi(\gamma)$ is unipotent (resp. finite-order) if and only $\gamma$ is. Therefore $\Lambda_{1}=\varphi\left(\rho_{3}\left(\pi_{1}(N)\right)\right)$ is a torsion-free, virtually unipotent subgroup of the arithmetic lattice $\Lambda$. By Theorem 8, there exists a torsion-free finite-index subgroup $\Lambda_{0}$ of $\Lambda$ containing $\Lambda_{1}$. Taking the intersection with the first factor of $\Lambda$ gives a torsion-free finite-index subgroup $\Gamma_{2}$ of $\Gamma_{1}$, containing $\rho_{3}\left(\pi_{1}(N)\right)$ as required for the conclusion of Step (3). \(\square\)

\section*{References}
\begin{itemize}
\item[] [A] L. Auslander; Bieberbach's theorems on space groups and discrete uniform subgroups of Lie groups. Ann. of Math. (2) 71 (1960), 579-590.
\item[] [B] N. Bergeron; Premier nombre de Betti et spectre du laplacien de certaines variétés hyperboliques. Enseign. Math. (2) 46 (2000), no. 1-2, 109-137.
\item[] [CG] S. Chen, L. Greenberg; Hyperbolic spaces, in Contributions to Analysis. Academic Press, New York (1974), 49-87.
\item[] [Dek] K. Dekimpe; Almost-Bieberbach groups: affine and polynomial structures. Lecture Notes in Mathematics 1639, Springer-Verlag, Berlin, 1996.
\item[] [Der] M. Deraux, On subgroups finite index in complex hyperbolic lattice triangle groups. Exp. Math. 33 (2024), no.3, 456-481.
\item[] [DFP] M. Deraux, E. Falbel, J. Paupert; New constructions of fundamental polyhedra in complex hyperbolic space. Acta Math. 194 (2005), 155-201.
\item[] [DPP1] M. Deraux, J.R. Parker, J. Paupert; New non-arithmetic complex hyperbolic lattices. Invent. Math. 203 (2016), 681-771.
\end{itemize}
[DPP2] M. Deraux, J.R. Parker, J. Paupert; New non-arithmetic complex hyperbolic lattices II. Michigan Math. J. 70 (2021), 133-205.
[DS] M. Deraux, M. Stover; One-cusped complex hyperbolic 2-manifolds. Preprint (2024). arXiv: 2409.08028
[FP] E. Falbel, J.R. Parker; The geometry of the Eisenstein-Picard modular group. Duke Math. J. 131 (2006) 249-289.
[FFP] E. Falbel, G. Francsics, J.R. Parker; The geometry of the Gauss-Picard modular group. Math. Ann. 349 (2011), no. 2, 459-508.
[FZ] F. T. Farrell, S. Zdravkovska; Do almost flat manifolds bound. Michigan J. Math. 30 (1983) 199-208.
[Go1] W.M. Goldman; Complex Hyperbolic Geometry. Oxford Mathematical Monographs. Oxford University Press (1999).
[Go2] W.M. Goldman; Geometric structures on manifolds. Graduate Studies in Mathematics 227. American Mathematical Society, Providence, RI, 2022.
[Gr] M. Gromov; Almost flat manifolds. J. Differential Geom. 13 (1978), 231-241.
[K] Y. Kamishima; Nonexistence of cusp cross-section of one-cusped complete complex hyperbolic manifolds II. Int. Math. Forum 2 (2007), no. 25-28, 1251-1258.
[KM] A. Kolpakov, B. Martelli; Hyperbolic four-manifolds with one cusp. Geom. Funct. Anal. 23 (2013), no.6, 1903-1933.
[LeRa] K.B. Lee, F. Raymond; Rigidity of almost crystallographic groups. Combinatorial methods in topology and algebraic geometry, Contemp. Math. 44, 73-78. American Mathematical Society, Providence, RI, 1985.
[LR1] D. D. Long, A. W. Reid; On the geometric boundaries of hyperbolic 4-manifolds. Geometry \& Topology 4 (2000), 171-178.
[LR2] D. D. Long, A. W. Reid; All flat manifolds are cusps of hyperbolic orbifolds. Algebraic and Geometric Topology 2 (2002), 285-296.
[M1] D. B. McReynolds; Peripheral separability and cusps of arithmetic hyperbolic orbifolds. Algebraic and Geometric Topology 4 (2004), 721-755.
[M2] D. B. McReynolds; Controlling manifold covers of orbifolds. Math. Res. Lett. 16 (2009), no.4, 651-662.
[PW] J. Paupert, P. Will; Real reflections, commutators and cross-ratios in complex hyperbolic space. Groups Geom. Dyn. 11 (2017), 311-352.
[R] V.A. Rohlin; A three-dimensional manifold is the boundary of a four-dimensional one. Doklady Akad. Nauk SSSR (N.S.) 81 (1951), 355-357.
[Sc] P. Scott; The geometries of 3-manifolds. Bull. London Math. Soc. 15 (1983), 401-487.
[Se] C. Sell; Cusps and commensurability classes of hyperbolic 4-manifolds. Algebraic and Geometric Topology 23, No. 8 (2023), 3405-3434.
[St1] M. Stover; On the number of ends of rank one locally symmetric spaces. Geometry \& Topology 17 (2013), 905-924.
[St2] M. Stover; Volumes of Picard modular surfaces. Proc. Amer. Math. Soc. 39 (2011), no. 9, 3045-3056.
[WM] D. Witte Morris; Introduction to arithmetic groups. Deductive Press, 2015. Available at: https://arxiv.org/abs/math/0106063

Julien Paupert
School of Mathematical and Statistical Sciences, Arizona State University paupert@asu.edu

Connor Sell
Département de Mathématiques, Université du Québec à Montréal sell.connor_daniel@courrier.uqam.ca
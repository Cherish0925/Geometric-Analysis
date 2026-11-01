---
retention_scope: session
part: 2
total_parts: 4
---

[Part 2/4 of: New non-arithmetic complex hyperbolic lattices]

We can also calculate the orbifold Euler characteristic $\chi$ of $\Gamma \backslash \mathbf{H}_{\mathbb{C}}^{1}$ as follows. We consider
each $\Gamma$-orbit of facets of $E$ and we weight them by the reciprocal of the order of their stabilizer:

\begin{tabular}[t]{|l|l|l|}
\hline Facet & Stabilizer & Order \\
\hline $q_{R}$ & $\langle R\rangle$ & 2 \\
\hline $q_{J}$ & $\left\langle P^{-1} R\right\rangle$ & 3 \\
\hline $r$ & $i d$ & 1 \\
\hline $E$ & $\langle P\rangle$ & 7 \\
\hline
\end{tabular}
Thus
$$\chi=\left(\frac{1}{2}+\frac{1}{3}\right)-1+\frac{1}{7}=\frac{-1}{42} .$$

We now briefly review standard techniques used to verify the hypotheses on ridge cycles. Tessellating around Giraud disks. For cycles around Giraud ridges the conditions of the Poincaré polyhedron theorem are easily checked, as we now recall.

Let $\mathscr{G}=\mathscr{G}\left(p_{0}, p_{1}, p_{2}\right)$ be a Giraud disk. Then $\mathscr{G}$ defines three regions $Y_{0}, Y_{1}$ and $Y_{2}$ given, for indices $j=0,1,2$ taken mod 3, by:
$$Y_{j}=\left\{u \in \mathbf{H}_{\mathbb{C}}^{2}: d\left(u, p_{j}\right) \leqslant d\left(u, p_{j+1}\right), d\left(u, p_{j}\right) \leqslant d\left(u, p_{j-1}\right)\right\}$$
Any point in $\mathbf{H}_{\mathbb{C}}^{2}$ is contained in (at least) one of these three regions according to the minimum of $d\left(u, p_{j}\right)$ for $j=0,1,2$. The interior $Y_{j}^{\circ}$ of $Y_{j}$ is the set of points where $d\left(u, y_{j}\right)$ is strictly smaller than $d\left(u, p_{j+1}\right)$ and $d\left(u, p_{j-1}\right)$. Clearly the interiors of these three regions are disjoint.

Lemma 3.3 Let $E$ be a polyhedron bounded by bisectors and let $\rho=s_{1} \cap s_{2}$ be a Giraud ridge of $E$ contained in the sides $s_{1}$ and $s_{2}$ of $E$. Let $S_{1}=\sigma\left(s_{1}\right)$ and $S_{2}=\sigma\left(s_{2}\right)$. Let $Y_{0}, Y_{1}$ and $Y_{2}$ be the three regions given in (9), defined by the Giraud disk containing $\rho$. Suppose the $Y_{j}$ each contain exactly one of $E, S_{1}^{-1}(E)$ and $S_{2}^{-1}(E)$ and that $S_{1}^{-1}(E) \cap S_{2}^{-1}(E)$ is contained in the third bisector containing $\rho$. Then $E, S_{1}^{-1}(E)$ and $S_{2}^{-1}(E)$ tessellate a neighborhod of the interior of $\rho$.

Proof. Without loss of generality, suppose that $E \subset Y_{0}, S_{1}^{-1}(E) \subset Y_{1}$ and $S_{2}^{-1}(E) \subset Y_{2}$. Since the $Y_{j}$ have disjoint interiors, it is clear that $E^{\circ}, S_{1}^{-1}\left(E^{\circ}\right)$ and $S_{2}^{-1}\left(E^{\circ}\right)$ are disjoint.

We must show that the three copies of $E$ cover a neighborhood of the interior of $\rho$. Suppose that $w \in \rho^{\circ}$ and $U(w)$ is a neighborhood of $w$. Then any point in $U(w)$ is in (at least) one of $Y_{0}, Y_{1}, Y_{2}$. If the point is sufficiently close to $\rho$ then it is in $E, S_{1}^{-1}(E)$ or $S_{2}^{-1}(E)$ respectively. \(\square\)

Tessellating around complex lines. Cycles around ridges contained in complex lines can be more complicated than ridges contained in Giraud disks. However, by looking at complex lines orthogonal to the intersection, tessellation is reduced to an angle condition resembling the classical version of the Poincaré polyhedron theorem for the hyperbolic plane.

Let $\mathscr{B}$ and $\mathscr{B}^{\prime}$ be two bisectors that intersect in a complex line $C$. Suppose $E$ is a polyhedron contained in the intersection of two half-spaces defined by $\mathscr{B}$ and $\mathscr{B}^{\prime}$ and that these bisectors contain sides $s$ and $s^{\prime}$ of $E$ intersecting in a simply connected ridge $\rho$ in $C$. Using Lemma 2.3 any complex line $C^{\perp}$ orthogonal to $C$ intersects $\mathscr{B}$ and $\mathscr{B}^{\prime}$ along geodesics, and $C^{\perp} \cap E$ is contained in a wedge bounded by these geodesics, as $\mathscr{B}$ and $\mathscr{B}^{\prime}$ both bound $E$. We must keep track of the angle subtended by this wedge. It is important to note that this
angle will depend on the point where $C$ and $C^{\perp}$ intersect, but that the total angle subtended over a ridge cycle will remain the same.

In particular, suppose $T$ is the cycle transformation of $\rho$. By construction, $T$ maps $C$ to itself. There are two possibilities: either $T$ fixes $C$ pointwise, and so is a complex reflection in $C$, or $T$ has a unique fixed point $o$ in $C$. In the latter case, the point $o$ must lie in $\rho$ as $T$ is a symmetry of $\rho$, which is simply connected. In either case, if $o$ is a point of $\rho$ fixed by $T$ then the complex line $C_{o}^{\perp}$ through $o$ orthogonal to $C$ is mapped to itself by $T$.

Suppose the cycle transformation is $T=P \circ S_{m} \circ \cdots \circ S_{1}$. The definition of a ridge cycle leads to ridges $\rho_{i}=s_{i} \cap s_{i-1}^{-}$where $S_{i}=\sigma\left(s_{i}\right)$. The intersection of $C_{o}^{\perp}$ with $S_{1}^{-1} \circ \cdots \circ S_{i-1}^{-1}(E)$ for $1 \leqslant i \leqslant m$ is a wedge, say with angle $\beta_{i}$, bounded by the intersection of $C_{o}^{\perp}$ with the sides $S_{1}^{-1} \circ \cdots \circ S_{i-1}^{-1}\left(s_{i}\right)$ and $S_{1}^{-1} \circ \cdots \circ S_{i-1}^{-1}\left(s_{i-1}^{-}\right)$. These wedges fit together to give a larger wedge bounded by the intersection of $C_{o}^{\perp}$ with a bisector and its image under $T$. In this larger wedge, the total angle at $o$ subtended by copies of $E$ under the cycle is $\beta_{1}+\cdots+\beta_{m}$.

Lemma 3.4 Let $E$ be a polyhedron bounded by bisectors and let $\rho$ be a ridge of $E$ contained in a complex line $C$. Let $T$ be the cycle transformation of $\rho$ and let $o$ be a fixed point of $T$ in $\rho$. Suppose that $T$ has order $\ell>0$ and that $T$ acts on $C_{o}^{\perp}$ as a rotation by angle $2 \pi / \ell$. Suppose that the total angle at $o$ in $C_{o}^{\perp}$ subtended by copies of $E$ under the cycle is $2 \pi / \ell$. Then any point $w \in \rho^{\circ}$ has an open neighborhood tessellated by images of $E$.

Proof. For simplicity, we begin by supposing the ridge cycle has length one and $T=$ $P \circ S$ where $S$ is the side-pairing map of $s$ and $P \in \Upsilon$. This means we only have to show that $E, T^{-1}(E), \ldots, T^{-(\ell-1)}(E)$ tessellate around $\rho$. (This is the only case we need in the applications in this paper.)

First consider the action of $T$ on $C_{o}^{\perp}$. Let $\mathscr{B}$ and $\mathscr{B}^{\prime}=T(\mathscr{B})$ be the bisectors containing the sides $s$ and $s^{\prime}=T(s)$ of $E$. Write $b_{o}=\mathscr{B} \cap C_{o}^{\perp}$ and $b_{o}^{\prime}=\mathscr{B}^{\prime} \cap C_{o}^{\perp}$. Since $T$ acts on $C_{o}^{\perp}$ as a rotation by $2 \pi / \ell$ then $b_{o}^{\prime}=T\left(b_{o}\right)$ and the arcs $b_{o}, b_{0}^{\prime}$ bound a wedge with angle $2 \pi / \ell$ containing $C^{\perp} \cap E$. Applying powers of $T$ we obtain $\ell$ wedges containing images of $E$ that tessellate a neighborhood of $o$ in $C_{o}^{\perp}$.

When $T$ is a complex reflection in $C$, this argument applies to all points of $\rho$ and the result follows.

We now consider the case where the fixed point $o$ of $T$ is unique. For a general point $u \in C \cap E$ consider $C_{u}^{\perp}$, the orthogonal complex line to $C$ at $u$. Since $T$ does not fix $u$, we see that $T$ sends $C_{u}^{\perp}$ to $C_{T u}^{\perp}$. However, by continuity, the intersection of $C_{u}^{\perp}$ with $E$ is contained in some wedge with apex $u$. The angle may change as $u$ varies but will always be positive since $\mathscr{B} \cap \mathscr{B}^{\prime}$ is $C$. Let $k$ (which divides $\ell$ ) be the smallest positive integer so that $T^{k}$ is the identity on $C$. Then the angles of these wedges at all the images of $C_{u}^{\perp}, T\left(C_{u}^{\perp}\right), \ldots, T^{k}\left(C_{u}^{\perp}\right)$ add up to $2 k \pi / \ell$. Since $T^{k}$ is a complex reflection in $C$ with angle $2 k \pi / \ell$ we see that the intersection of $E, T(E), \ldots, T^{\ell-1}(E)$ with $C_{u}^{\perp}$ tessellate a neighborhood of $u$ in $C_{u}^{\perp}$.

By carrying out this process for all points of $C \cap E$, we see that for any point $u$ in the (relative) interior of $C \cap E$ there is an open neighborhood of $u$ tessellated by copies of $E$.

Now consider the general case where the length of the ridge cycle is $m \geqslant 1$ and the cycle transformation is $T=P \circ S_{m} \circ \cdots \circ S_{1}$. In this case, we need to keep track of wedges in $T^{-j} \circ S_{1}^{-1} \circ \cdots \circ S_{i}^{-1}\left(C_{u}^{\perp}\right)$ for $0 \leqslant i \leqslant m-1$ and $0 \leqslant j \leqslant \ell-1$. Nevertheless, the same argument gives the result. \(\square\)

\section*{4 Construction of the fundamental polyhedron}

In section 4.1 and 4.2, we define the six groups that appear in Theorem 1.1, and establish basic notation that will be used throughout the paper.

In section 4.3, we study braiding properties of some complex reflections in our groups, which are used in an essential way in order to build our fundamental polyhedra, as explained in section 4.4. These braiding pairs of reflections are also important because they will correspond to the stabilizers of various vertices and complex ridges of our fundamental polyhedron, see section 5.3; this will allow us to compute the orbifold Euler characteristic, see section 5.5.

We define our polyhedra in section 4.5 by building the $k$-skeleton for increasing values of $k$. The general strategy for this definition is described in section 4.8, an important point for this inductive definition to make sense is that the boundary of every cell is a topological (piecewise smooth) sphere. The only difficult part of this verification is the one that concerns the boundary of the whole polyhedron. We show that the boundary of $E$ is homeomorphic to $S^{3}$ in section 4.7.

We then start from the combinatorial model of the polyhedron (this is described in section 4.6.2), and prove that the geometric realization is well-defined, and that it gives an embedding of the combinatorial model (sections 4.8.1 through 4.8.5).

\subsection*{4.1 Generators}

In this section, we give explicit matrices that generate our groups. For more details on sporadic triangle groups, see [PP09] and [DPP11].

Recall from the introduction that our groups are generated by a complex reflection $R_{1}$ and a regular elliptic element $J$ of order three. We write
$$R_{2}=J R_{1} J^{-1}, \quad R_{3}=J R_{2} J^{-1} .$$

We write $\mathbf{n}_{j}$ for polar vector to the mirror of the complex reflection $R_{j}(j=1,2,3)$. Matrix representatives for $R_{j}$ in $\operatorname{SU}(2,1)$ will have eigenvalues $a^{2}, \bar{a}, \bar{a}$ where
$$a=e^{2 \pi i / 3 p} .$$
Since $R_{j+1}=J R_{j} J^{-1}$ we see that $\mathbf{n}_{j+1}=J \mathbf{n}_{j}$ (with $j \bmod 3$ ). In the cases that interest us, $\left(\mathbf{n}_{1}, \mathbf{n}_{2}, \mathbf{n}_{3}\right)$ forms a basis for $\mathbb{C}^{3}$, which we will use throughout the paper. The matrix for $J$ in this basis is then simply the permutation matrix:
$$J=\left[\begin{array}{lll}
0 & 0 & 1 \\
1 & 0 & 0 \\
0 & 1 & 0
\end{array}\right]$$
and the Hermitian form is given by a matrix of the form
$$H=\left[\begin{array}{ccc}
\alpha & \beta & \bar{\beta} \\
\bar{\beta} & \alpha & \beta \\
\beta & \bar{\beta} & \alpha
\end{array}\right] .$$
It is convenient to choose
$$\alpha=4 \sin ^{2}(\pi / p)=2-a^{3}-\bar{a}^{3},$$

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/31f0f35c-0604-47ef-a2ef-a49ed021037c-22.jpg?height=523&width=1394&top_left_y=383&top_left_x=349}
\captionsetup{labelformat=empty}
\caption{Figure 2: Relative positions of the mirrors of $R_{1}, R_{2}, R_{3}$. For $p \geqslant 5$, the dotted lines correspond to the lines polar to $p_{j k}$, or in other words the common perpendicular between the mirrors of $R_{j}$ and $R_{k}$.}
\end{figure}
in which case the condition $\operatorname{tr}\left(R_{1} J\right)=\tau$ imposes
$$\beta=\left(\bar{a}^{2}-a\right) \tau .$$
The matrix of the reflection $R_{1}$ (adjusted to have determinant 1 , since we want to work with $\operatorname{SU}(2,1))$, is easily seen to be
$$R_{1}=\left[\begin{array}{ccc}
a^{2} & \tau & -a \bar{\tau} \\
0 & \bar{a} & 0 \\
0 & 0 & \bar{a}
\end{array}\right]$$
and $R_{2}=J R_{1} J^{-1}, R_{3}=J^{-1} R_{1} J$.
The configuration of three complex lines given by the mirrors of $R_{1}, R_{2}$ and $R_{3}$ varies with $p$. Note that the relative position of the mirrors of $R_{1}$ and $R_{2}$ is controlled by the restriction of the Hermitian form to $\operatorname{Span}\left(\mathbf{n}_{1}, \mathbf{n}_{2}\right)$, i.e by the sign of the determinant of the 2 × 2 matrix in the upper left corner of $H$. Using the specific value $\tau=-(1+i \sqrt{7}) / 2$ (in fact all we need is that $|\tau|^{2}=2$ ), we have
$$\alpha^{2}-|\beta|^{2}=8 \sin ^{2}(\pi / p)\left(2 \sin ^{2}(\pi / p)-1\right)=-8 \sin ^{2}(\pi / p) \cos (2 \pi / p) .$$
Hence the mirrors intersect inside complex hyperbolic space only for $p=3$, they intersect at infinity when $p=4$, and they are ultraparallel when $p \geqslant 5$ (see Figure 2).

For future reference, we define
$$P=R_{1} J$$
and
$$S_{1}=P^{2} R_{1} P^{-2} R_{1} P^{2}$$
which will turn out to be key isometries when constructing our fundamental domains. Since $P=R_{1} J$ has trace $\tau=-(1+i \sqrt{7}) / 2=e^{-2 \pi i / 7}+e^{-4 \pi i / 7}+e^{-8 \pi i / 7}$, we immediately see that $P$ is a regular elliptic map of order 7, with isolated fixed point
$$\mathbf{p}=\left[\begin{array}{c}
a e^{-2 \pi i / 7} \\
1 \\
\bar{a} e^{2 \pi i / 7}
\end{array}\right] .$$

For completeness we give an explicit matrix for $S_{1}$, which is also regular elliptic of order $2 p$ :
$$S_{1}=\left[\begin{array}{ccc}
-a & \bar{a} \bar{\tau} & -1 \\
0 & -a \tau+\bar{a}^{2} \bar{\tau} & a^{2} \bar{\tau}-a^{2}-\bar{a} \\
0 & -1-\bar{a}^{3}+\bar{a}^{3} \tau & a \tau-\bar{a}^{2} \bar{\tau}
\end{array}\right] .$$

\subsection*{4.2 Word notation}

We shall often use word notation and write $j$ for $R_{j}$ and $\bar{j}$ for $R_{j}^{-1}$, so that a word in $R_{1}$, $R_{2}, R_{3}$ and their inverses is described by a sequence of (possibly overlined) integers. Note that there is very little confusion possible between $R_{j}^{-1}$ and the complex conjugate matrix $\bar{R}_{j}$ (which we shall never use in this paper). For example, $23 \overline{2}$ denotes $R_{2} R_{3} R_{2}^{-1}$, and $1 \overline{3} 23 \overline{1}$ denotes $R_{1} R_{3}^{-1} R_{2} R_{3} R_{1}^{-1}$.

When an isometry given by a word $w$ in 1, 2, 3 has an isolated fixed point, we denote this point by $p_{w}$ or $q_{w}$. In particular, consider two reflections with distinct mirrors that can be expressed as words $u, v$. If $w=u v$ is conjugate in $\Gamma$ to 12 (this is a word, not a number!) then we denote by $p_{w}$ the intersection point of their mirrors of reflections (or the intersection of the extension of their mirrors to projective lines, i.e. these points may be in $\mathbf{P}_{\mathbb{C}}^{n}$ rather than $\mathbf{H}_{\mathbb{C}}^{n}$ ). Similarly, if $w=u v$ is conjugate to $123 \overline{2}$ then we denote the fixed point of $w$ by $q_{w}$. The reason for using different letters of the alphabet is that points the of the form $p_{w}$ and those of the form $q_{w}$ are in different group orbits. We will refer to vertices of our polyhedra that have the form $p_{w}$ for some word $w$ as $p_{*}$-vertices (and similarly for $q_{*}$-vertices).

Let $\mathbf{n}_{w}$ denote a lift to $\mathbb{C}^{3}$ of the corresponding point $p_{w}$. Of course, by definition, these lifts are only determined up to multiplication by a scalar; so we give some explicit formulae for future reference.
$$\begin{gathered}
\mathbf{n}_{23 \overline{2}}=R_{2} \mathbf{n}_{3}=\left[\begin{array}{c}
0 \\
\tau \\
\bar{a}
\end{array}\right], \quad \mathbf{n}_{123 \overline{1}}=a R_{1} \mathbf{n}_{23}=\left[\begin{array}{c}
a^{6}+a^{3}-a^{3} \tau+\bar{\tau} \\
a^{2} \bar{\tau}-\bar{a} \\
\bar{a}^{2} \tau-a
\end{array}\right], \\
\mathbf{n}_{123 \overline{2}}=\left[\begin{array}{c}
\bar{a}^{2}+a \tau \\
\bar{a}^{3}-a^{3}-\bar{\tau} \\
\bar{a}^{4} \bar{\tau}+\bar{a}
\end{array}\right], \quad \mathbf{n}_{1 \overline{3} 23}=\left[\begin{array}{c}
a^{2}+\overline{a \tau} \\
a^{4} \tau+a \\
a^{3}-\bar{a}^{3}-\tau
\end{array}\right], \quad \mathbf{n}_{1 \overline{3} 23 \overline{1}}=a R_{1} R_{3}^{-1} \mathbf{n}_{2}=\left[\begin{array}{c}
a^{2} \\
a \\
\bar{\tau}
\end{array}\right] .
\end{gathered}$$

We will also denote by $m_{w}$ the mirror of the complex reflection corresponding to a word $w$, so that $\mathbf{n}_{w}$ is a polar vector to $m_{w}$ (in other words, $m_{w}$ corresponds to $\mathbf{n}_{w}^{\perp}$ ). We will also extend this notation to group elements that have a complex reflection as a power, so that (when $p \geqslant 5$ ) $m_{23}$ denotes the mirror of $\left(R_{2} R_{3}\right)^{2}$, and (when $p \geqslant 8$ ) $m_{123 \overline{2}}$ denotes the mirror of $\left(R_{1} R_{2} R_{3} R_{2}^{-1}\right)^{3}$.

\subsection*{4.3 Higher braiding}

The key to the general procedure to build the fundamental domains for our groups (see section 4.4) is the following result from [PP09] (see also section 2.2 of [Mos80]).

Proposition 4.1 (Proposition 4.4 of [PP09]) Suppose that $R_{x}$ and $R_{y}$ are complex reflections in $\mathrm{SU}(2,1)$ both with eigenvalues $e^{2 i \psi / 3}, e^{-i \psi / 3}, e^{-i \psi / 3}$. Let $L_{x}$ and $L_{y}$ be the $e^{-i \psi / 3}$ eigenspaces of $R_{x}$ and $R_{y}$, respectively. Then $L_{x} \cap L_{y}$ is an $e^{-2 i \psi / 3}$ eigenspace of $R_{x} R_{y}$. Suppose $R_{x} R_{y}$ is non-loxodromic and that its other eigenvalues are $-e^{i \psi / 3 \pm i \phi}$. Then the group
$\Gamma_{x y}=\left\langle R_{x}, R_{y}\right\rangle$ acts on the orthogonal complement of $L_{x} \cap L_{y}$ as (the orientation preserving subgroup of ) a $(\psi / 2, \psi / 2, \phi)$ triangle group $\Delta_{x y}$.

Consider the action of $\left\langle R_{x}, R_{y}\right\rangle$ on the projectivization of $\left(L_{x} \cap L_{y}\right)^{\perp}$, which we denote by $m_{x y}$. The space $m_{x y}$ is a sphere, Euclidean plane or hyperbolic plane respectively, depending on whether $m_{x}$ and $m_{y}$ intersect, are asymptotic or are ultraparallel. Note that there is a close connection between the values of $\psi$ and $\phi$ and these three cases (see Figure 2). In what follows, we will suppose $\psi=2 \pi / p$ and $\phi=2 \pi / q$ (which will be the case in our examples). This means that the triangle associated to $\Delta_{x y}$ has internal angles $\pi / p, \pi / p, 2 \pi / q$. In particular, $R_{x} R_{y}$ acts on $m_{x y}$ as a rotation through angle $2 \phi=4 \pi / q$. If $q$ is even then $\Delta_{x y}$ is a $(p, p, q / 2)$ triangle group. Therefore $\left(R_{x} R_{y}\right)^{q / 2}$ acts as the identity on $m_{x y}$. On the other hand, if $q$ is odd this triangle can be divided into two $(2, p, q)$ triangles, and $\Delta_{x y}$ is a $(2, p, q)$ triangle group. In this case a simple geometric argument in $m_{x y}$ shows that $\left(R_{x} R_{y}\right)^{(q-1) / 2}\left(m_{x} \cap m_{x y}\right)=$ $\left(m_{y} \cap m_{x y}\right)$. Since $m_{x}$ and $m_{y}$ are orthogonal to $m_{x y}$ we immediately see that $R_{x}$ and $R_{y}$ satisfy a (generalized) braid relation. When $q$ is even, this braid relation is
$$\left(R_{x} R_{y}\right)^{q / 2}=\left(R_{y} R_{x}\right)^{q / 2}$$
and when $q$ is odd, it is
$$\left(R_{x} R_{y}\right)^{(q-1) / 2} R_{x}=R_{y}\left(R_{x} R_{y}\right)^{(q-1) / 2} .$$
Furthermore, by examining the eigenvalues we can see that $\left(R_{x} R_{y}\right)^{q / 2}$ (respectively $\left(R_{x} R_{y}\right)^{q}$ ) has a repeated eigenvalue. Therefore it is either is a complex reflection (in a line or a point), the angle depending on $p$ and $q$ or it is possibly parabolic. The latter case arises when $p_{x y}$ lies on $\partial \mathbf{H}_{\mathbb{C}}^{2}$. In either case, a power of $R_{x} R_{y}$ is in the center of $\left\langle R_{x}, R_{y}\right\rangle$.

The following result is clear from the analysis in [PP09], but it can also be checked by explicit computations (see also Section 9.2.1 of [DPP11], and Section 2.2 of [Mos80]). Geometrically, it corresponds to the relative positions of the mirrors of $R_{1}$ and $R_{2}$ described in Section 4.1 and illustrated in Figure 2. When we use the Poincaré polyhedron theorem in Section 5.4, we will derive these equations from the cycle relations, see Lemma 5.12.

Proposition $4.2\left(R_{1} R_{2}\right)^{2}$ is a complex reflection with angle $(p-4) \pi / p$ when $p \neq 4$, and it is parabolic when $p=4$. For $p=3,\left(R_{1} R_{2}\right)^{2}$ is a complex reflection in the point $p_{12}$ where the mirrors of $R_{1}$ and $R_{2}$ intersect. For $p \geqslant 5$, it is a complex reflection in the common perpendicular complex line $m_{12}$ to the mirrors of $R_{1}$ and $R_{2}$. Moreover, for any $p$, we have the higher braid relation
$$\left(R_{1} R_{2}\right)^{2}=\left(R_{2} R_{1}\right)^{2}$$
Note that it follows from (14) that $R_{1}$ and $R_{2}$ both commute with $\left(R_{1} R_{2}\right)^{2}$, which implies the orthogonality statement about their mirrors. More specifically, we have

Proposition 4.3 The group $\left\langle R_{1}, R_{2}\right\rangle$ is a central extension of a $(2, p, p)$ orientation preserving triangle group with center $\left\langle\left(R_{1} R_{2}\right)^{2}\right\rangle$ of order $2 p /|p-4|$ (which is infinite for $p=4$ ). In particular, $\left\langle R_{1}, R_{2}\right\rangle$ has order $8 p^{2} /(4-p)^{2}$ when $p \leqslant 3$ and infinite order when $p \geqslant 4$.

Proof. The first statement follows from the fact that $R_{1}$ and $R_{2}$ have order $p$ and $\left(R_{1} R_{2}\right)^{2}$ is central with order $2 p /|p-4|$. The second statement follows from the fact that, for $p \leqslant 3$, a $(2, p, p)$ triangle group has order $4 p /(4-p)$ and for $p \geqslant 4$ it is infinite. \(\square\)

Geometrically, when $p=3$ the spherical (2, 3, 3) triangle group acts on the sphere of complex lines through $p_{12}$; when $p=4$ the vertex $p_{12}$ is on the ideal boundary and the Euclidean (2, 4, 4) triangle group acts on the horizontal factor of the Heisenberg group based at that vertex; when $p \geqslant 5$ the hyperbolic triangle group (2, 5, 5) acts on the complex line $m_{12}$.

It is useful to have a formula for the mirror of $\left(R_{1} R_{2}\right)^{2}$ (when $p \geqslant 5$ ), which is polar to
$$\mathbf{n}_{12}=\left[\begin{array}{c}
a^{2} \bar{\tau}-\bar{a} \\
\bar{a}^{2} \tau-a \\
a^{3}+\bar{a}^{3}
\end{array}\right] .$$
The notation is set up to indicate that it is the intersection point of the mirrors of $R_{1}$ and $R_{2}$ (see also Section 4.3). When $p=3,4$ the vector $\mathbf{n}_{12}$ projects to $p_{12}$, which is in $\mathbf{H}_{\mathbb{C}}^{2}$ or on its boundary respectively. The obvious extension of this notation allows us to describe the $J$-orbit of this vector, namely
$$\mathbf{n}_{23}=J \mathbf{n}_{12}, \quad \mathbf{n}_{13}=J \mathbf{n}_{23} .$$
Note that the higher braid relation holds of course between any pair of reflections $R_{j}$ and $R_{k}$ with $j \neq k$, since $J R_{k} J^{-1}=R_{k+1}$, so that
$$\left(R_{2} R_{3}\right)^{2}=\left(R_{3} R_{2}\right)^{2}, \quad\left(R_{3} R_{1}\right)^{2}=\left(R_{1} R_{3}\right)^{2} .$$

The following observation will be useful later.
Proposition $4.4 P^{2} S_{1}$ is a complex reflection, in fact
$$P^{2} S_{1}=R_{2} R_{3}^{-1} R_{2}^{-1} .$$
Proof. Using the identity (10), we see that $P^{2} S_{1}=R_{3}^{-1} R_{2}^{-1} R_{3}^{-1} R_{2} R_{3}$, by repeatedly using $P=R_{1} J$ and $J R_{k} J^{-1}=R_{k+1}$. The equality (15) then follows from the braid relation $\left(R_{2} R_{3}\right)^{2}=\left(R_{3} R_{2}\right)^{2}$. \(\square\)

A similar analysis holds for $R_{1}$ and $R_{2} R_{3} R_{2}^{-1}$. In fact, in this case we recover the braid relation (compare with the calculations in [DFP05], or in Section 2.2 of [Mos80], in or Section 6 of [Par06]).

Proposition $4.5\left(R_{1} R_{2} R_{3} R_{2}^{-1}\right)^{3}$ is a complex reflection with angle $(p-6) \pi / p$ when $p \neq 6$, and it is parabolic when $p=6$. For $p \leqslant 5,\left(R_{1} R_{2} R_{3} R_{2}^{-1}\right)^{3}$ is a complex reflection in the point $q_{123 \overline{2}}$. For $p \geqslant 7$, it is a complex reflection in the complex line $m_{123 \overline{2}}$ perpendicular to the mirrors of $R_{1}$ and $R_{2} R_{3} R_{2}^{-1}$. Moreover, for any $p \in \mathbb{N}^{*}$, we have the braid relation
$$R_{1}\left(R_{2} R_{3} R_{2}^{-1}\right) R_{1}=\left(R_{2} R_{3} R_{2}^{-1}\right) R_{1}\left(R_{2} R_{3} R_{2}^{-1}\right) .$$

Proposition 4.6 The group $\left\langle R_{1}, R_{2} R_{3} R_{2}^{-1}\right\rangle$ is a central extension of a ( $2,3, p$ ) orientation preserving triangle group with center $\left\langle\left(R_{1} R_{2} R_{3} R_{2}^{-1}\right)^{3}\right\rangle$ of order $2 p /|p-6|$ (which is infinite for $p=6$ ). In particular, $\left\langle R_{1}, R_{2} R_{3} R_{2}^{-1}\right\rangle$ has order $24 p^{2} /(6-p)^{2}$ when $p \leqslant 5$ and infinite order when $p \geqslant 6$.

Proof. Since $R_{1}$ has order $p$ and $\left(R_{1} R_{2} R_{3} R_{2}^{-1} R_{1}\right)^{2}=\left(R_{1} R_{2} R_{3} R_{2}^{-1}\right)^{3}$ is central with order $2 p /|p-6|$, we obtain the first statement. The second statement follows since a $(2,3, p)$ triangle group has order $12 p /(6-p)$ for $p \leqslant 5$ and is infinite for $p \geqslant 6$. \(\square\)

\subsection*{4.4 General procedure for building fundamental domains}

In this section, we give a rough idea of the procedure that allowed us to produce the fundamental domains that appear in this paper.

The general context is that of triangle groups, i.e. groups generated by three complex reflections. An important example of such a group was studied in [Sch03], where Schwartz gave a fundamental domain for a group generated by complex reflections $I_{1}, I_{2}, I_{3}$ of order 2 with pairwise products of order 4 and such that $I_{1} I_{2} I_{3} I_{2}$ has order 7. The combinatorial structure of Schwartz's fundamental domain inspired several subsequent constructions, see [Par06] and [Tho10], which in turn evolved into a fairly general procedure that applies to triangle groups. We now outline that procedure and relate it to Schwartz's construction.

In Section 4.3, we discussed the fact that some pairs of complex reflections in the group satisfy the (generalized) braid relations (12) and (13). In the present paper, we consider only $q=3$ or $q=4$ (for groups with $\tau=\sigma_{1}$ or $\sigma_{5}$ in the notation of [PP09], we would need to consider $q=5$ and $q=6$ as well).

We will now outline how to go from a pair of braiding complex reflections $R_{x}$ and $R_{y}$ to (the combinatorial model of) a side in our polyhedron. We first explain the construction in the simplest case, namely when $L_{x} \cap L_{y}$ is negative for the Hermitian inner product, or equivalently, $m_{x} \cap m_{y}=p_{x y} \in \mathbf{H}_{\mathbb{C}}^{2}$.

\subsection*{4.4.1 Basic construction of pyramids using braiding}

The mirrors $m_{x}$ and $m_{y}$ of $R_{x}$ and $R_{y}$ pass through $p_{x y}$. Now consider the images of the lines $m_{x}$ and $m_{y}$ under powers of $R_{x} R_{y}$. Using subscript notation, these can be written as $m_{x}, m_{x y \bar{x}}, m_{x y x \bar{y} \bar{x}}, \ldots, m_{\bar{y} x y}, m_{y}$. It is not hard to see that there are exactly $q$ of these lines, all lying in the pencil of complex lines through $p_{x y}$. (If $q$ is odd then $m_{y}$ is the image of $m_{x}$ under $\left(R_{x} R_{y}\right)^{(q-1) / 2}$. If $q$ is even $m_{x}$ and $m_{y}$ are in distinct orbits, each orbit comprising $q / 2$ lines.) These $q$ lines form our starting point when constructing a side of the polyhedron.

Consider now a third complex reflection $R_{z}$ with mirror $m_{z}$ and angle $\psi=2 \pi / p$. For simplicity, we suppose $m_{z}$ intersects each of $m_{x}, m_{x y \bar{x}}, \ldots, m_{\bar{y} x y}, m_{y}$ in a point of $\mathbf{H}_{\mathbb{C}}^{2}$, denoted by $p_{x z}, p_{x y \bar{x} z}$, and so on. The $q$ points $p_{x z}, p_{x y \bar{x} z}, \ldots, p_{y z}$ form the vertices of a $q$-gon in the line $m_{z}$. Together with the point $p_{x y}$, they form the vertices of a pyramid with apex $p_{x z}$ and base the $q$-gon in $m_{z}$. The combinatorial model for the side is obtained by adding edges as follows. We include each of the $q$ edges of the $q$-gon in the base, together with an edge from each of the base vertices to $p_{x y}$ (see Figure 3).

In order for our polyhedron to have a well-defined side pairing, given a pyramid as above, it is natural to construct an opposite isometric pyramid. Note that the reflection $R_{z}$ fixes the base of the above pyramid pointwise. We find a second pyramid by applying $R_{z}$ to the first one. In this case $x$ is replaced with $z x \bar{z}$ and $y$ is replaced with $z y \bar{z}$ and so on.

The above procedure is illustrated in Figure 3. Part (a) shows a square pyramid with $x=2, y=3, z=1$, and part (b) shows its opposite pyramid. Part (c) shows a triangular pyramid with $x=1, y=\overline{3} 23$ and $z=23 \overline{2}$, and part (d) shows (the image under $P^{-2}$ of) its opposite pyramid; here $P^{-2} z^{-1} x z P^{2} P^{-2}(\overline{3} \overline{2} 3) 1(\overline{3} 23) P^{2}=1$, and similarly $P^{-2} z^{-1} y z P^{2}=$ $23 \overline{2}$ and $P^{-2} z P^{2}=1 \overline{3} 23 \overline{1}$.

The number of sides in these examples come from the fact that $R_{2}$ and $R_{3}$ braid with order 4 , and $R_{1}$ and $R_{\overline{3} 23}$ braid with order 3 (see section 4.3). Note also that we use relations in the group to write $\bar{y} x y z=\overline{3} \overline{2} 31 \overline{3} 2323 \overline{2}=\overline{3} \overline{2} 3123$ and $y z=\overline{3} 2323 \overline{2}=23$.

Schwartz uses a similar procedure in [Sch03]. Since his generating reflections have order $p=2$, in his case $x=\bar{x}$ and $y=\bar{y}$. Consider Fig 4.2 of [Sch03] which depicts what Schwartz calls an odd $B$ piece. This is made up of two square pyramids. In the front one, $x=1$, $y=3$ and $z=2$. The apex is $p_{x y}=[13]$ and the vertices around the base are $p_{x z}=[12]$, $p_{x y \bar{x} z}=[1312], p_{\bar{y} x y z}=[3132]$ and $p_{y z}=p_{z y}=[23]$. The rear pyramid is the image of the front one under $R_{z}=I_{2}$ and has $x=212, y=232$ and $z=2$.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/31f0f35c-0604-47ef-a2ef-a49ed021037c-27.jpg?height=386&width=1551&top_left_y=703&top_left_x=271}
\captionsetup{labelformat=empty}
\caption{Figure 3: Combinatorial structure of the faces, in the case $p=3$ or 4. Since all vertices are inside $\mathbf{H}_{\mathbb{C}}^{2}$, no truncation is needed.}
\end{figure}

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/31f0f35c-0604-47ef-a2ef-a49ed021037c-27.jpg?height=388&width=1548&top_left_y=1300&top_left_x=272}
\captionsetup{labelformat=empty}
\caption{Figure 4: Combinatorial structure of the faces, in the case $p=5$ or 6. A first truncation has occurred since the mirrors of $R_{1}, R_{2}$ and $R_{3}$ are ultraparallel.}
\end{figure}

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/31f0f35c-0604-47ef-a2ef-a49ed021037c-27.jpg?height=390&width=1551&top_left_y=1890&top_left_x=271}
\captionsetup{labelformat=empty}
\caption{Figure 5: Combinatorial structure of the faces, in the case $p=8$ or 12. Further truncation has occurred since the mirrors of $R_{1}$ and $R_{3}^{-1} R_{2} R_{3}$ are ultraparallel.}
\end{figure}

Given one pyramid as above, the ridges containing the apex are all triangles, for example the ridge determined by the three complex lines $m_{x}, m_{y}, m_{z}$ with vertices $p_{x y}, p_{x z}, p_{y z}$. We can repeat the whole of the above construction starting with a different pair of these
complex lines, for example $m_{z}$ and $m_{y}$. This will yield a new pyramid, whose base lies in $m_{x}$ and which shares a common triangular side with our initial pyramid. In order to construct a combinatorial model for our polyhedron, we repeat this process. For each side of each pyramid, there should be exactly one other pyramid with the same triangular side, and the whole collection should close up and be invariant under powers of $P$. This game should be compared with [Sch03] or [Tho10] where a similar game is played. The main difference is that Schwartz is not interested in triangles if all three vertices lie outside complex hyperbolic space.

\subsection*{4.4.2 Truncation}

It may be that some, or all, of the vertices of the pyramid lie outside complex hyperbolic space. In this case, it turns out the intersection point is the polar vector of a mirror of a complex reflection in the group (provided $p \geq 3$ ). With the notation above, suppose $m_{x}$ and $m_{y}$ are ultraparallel. As we have seen, $\left(R_{x} R_{y}\right)^{q / 2}$ or $\left(R_{x} R_{y}\right)^{q}$, for $q$ even or odd repectively, is a complex reflection and commutes with $R_{x}$ and $R_{y}$. Therefore the common orthogonal to $m_{x}$ and $m_{y}$ is the mirror $m_{x y}$ of this power of $R_{x} R_{y}$.

The simplest case of this are the even $A$ piece of Schwartz depicted in Figure 4.3 of [Sch03]. In this case $q=7$ (and he still has $p=2$ ) and he has two pyramids with a heptagonal base. For the front pyramid $x=131, y=2$ and $z=1$. Thus the apex of the pyramid is $p_{x y}=[1312]$. Of the base vertices, four are points of complex hyperbolic space, namely: $p_{x z}=[1311]=[13]$, $p_{x y \bar{x} z}=[13121311]=[131213], p_{\bar{y} x y z} p_{z \bar{y} x y}=[121312]$ and $p_{y z}=p_{z y}=[12]$. The other three base vertices lie outside complex hyperbolic space. The rear pyramid is the image of the first under $R_{z}=I_{1}$, and so has $x=3, y=121$ and $z=1$. Schwartz's picture does not illustrate the truncation arising from vertices lying outside complex hyperbolic space.

We now explain the implications of this truncation process for our polyhedra. The simplest feature is when $m_{x}$ and $m_{y}$ are ultraparallel. We denote their common orthogonal by $m_{x y}$. The $q$ lines $m_{x}, m_{x y \bar{x}}, m_{x y x \bar{y} \bar{x}}, \ldots, m_{\bar{y} x y}, m_{y}$ are all orthogonal to $m_{x y}$ and their intersection points with $m_{x y}$ (denoted $p_{x y}^{x}=m_{x} \cap m_{x y}$ etc.) now form the vertices of a $q$-gon in $m_{x y}$; compare Figure 3(a) with Figure 4(a) and Figure 5(a), where the apex $p_{23}$ has been replaced with a quadrilateral.

Next, we explain how the truncation affects base vertices. Suppose the mirrors $m_{x}$ and $m_{z}$ of $R_{x}$ and $R_{z}$ are ultraparallel. Then consider their common perpendicular line $m_{x z}$. The mirrors $m_{x}$ and $m_{z}$ intersect $m_{x z}$ in distinct points, which we label $p_{x z}^{x}$ and $p_{x z}^{z}$ respectively. The point $p_{x z}$ is then replaced with a line in $m_{x z}$ between these two points. Compare Figure 3(c) with Figure 4(c). In particular, the vertex $p_{23}$ has been replaced with an arc from $p_{23}^{\overline{3} 23}$ to $p_{23}^{23 \overline{2}}$. We can still build up a polyhedron from these truncated polyhedra, the main difference being that the sides that were formerly triangles may be quadrilaterals, pentagons or hexagons.

\subsection*{4.5 Definition of the polyhedron $E$}

In this section we define the fundamental polyhedron $E$. We will show that $E$ is a piecewise smooth polyhedron (as defined in Section 3.2), and in parallel we determine its precise combinatorics. This allows us to show that $E$ is a fundamental domain for the action of the cosets of $\Upsilon=\operatorname{Stab}_{\Gamma}(E)$ in $\Gamma$.

\subsection*{4.5.1 Bounding bisectors}

The basic fact we will use is that the pyramids constructed in section 4.4 have a natural geometric realization inside a suitable bisector. Indeed, for a given pyramid, there is a unique bisector that contains the base of the pyramid in a complex slice, and whose extended real spine contains its apex. We call this bisector the supporting bisector of the pyramid. Concretely, if the base is given by $\mathbf{m}^{\perp}$ and the apex by a, the real spine of the supporting bisector is given by the real span of a and $\mathbf{a}-\langle\mathbf{a}, \mathbf{m}\rangle \mathbf{m} /\langle\mathbf{m}, \mathbf{m}\rangle$ (a lift of the orthogonal projection of a onto the base). The following gives a geometric justification for considering such bisectors:

Proposition 4.7 The supporting bisector of a pyramid contains all real geodesic segments between its vertices.

This is obvious for edges in the base, as the base is contained in a complex slice of the supporting bisector. For edges through the apex, it follows from the fact that a bisector contains all geodesics intersecting the real spine. For edges in truncation faces, it follows from the fact that the complex line containing the truncation face is a complex slice of the supporting bisector.

The basic building blocks of $E$ will be the following four bisectors, which are the supporting bisectors of the four faces described in section 4.4.

Definition 4.8 1. $\mathscr{R}_{1}$ is the bisector whose extended real spine contains $\mathbf{n}_{1}$ and $\mathbf{n}_{23}$;
\begin{itemize}
\item[2.] $\mathscr{R}_{1}^{-}$is the image of $\mathscr{R}_{1}$ under $R_{1}$;
\item[3.] $\mathscr{S}_{1}$ is the bisector whose extended real spine contains $\mathbf{n}_{23 \overline{2}}$ and $\mathbf{n}_{1 \overline{3} 23}$;
\item[4.] $\mathscr{S}_{1}^{-}$is the image of $\mathscr{S}_{1}$ under $S_{1}$.
\end{itemize}
Recall from section 4.1 that we denote by $\mathbf{p}$ the isolated fixed point of $P$.
Definition 4.9 Let $F$ be the intersection of the 28 half-spaces containing $\mathbf{p}$ bounded by the bisectors $P^{k} \mathscr{R}_{1}^{ \pm}$and $P^{k} \mathscr{S}_{1}^{ \pm}(k=0, \pm 1, \pm 2, \pm 3)$. The region $E$ is the connected component of $F$ containing $\mathbf{p}$.

We will refer to the 28 bisectors of the form $P^{k} \mathscr{R}_{1}^{ \pm}$and $P^{k} \mathscr{S}_{1}^{ \pm}$as the bounding bisectors.
Remark 4.10 (1) The domain $E$ has much simpler combinatorics than the Dirichlet domains that were used in [DPP11] (when $p \geqslant 4$ ). As a slight drawback of not using Dirichlet domains, it is unclear whether $E$ is star-shaped with respect to p, and hence it is not convenient to use geodesic cone arguments; rather we use fundamental domains for coset decompositions.
(2) It turns out to be complicated to determine the precise combinatorics of the polyhedron $F$ bounded by the bounding bisectors; in fact it is not even obvious that $F$ is connected. This is why we define $E$ as a component of $F$. In fact one could prove that $E=F$ (which would then give a description of the combinatorial structure of $F$ ) but this is not needed in order to prove our main theorem. The main reason for working with $E$ rather than $F$ is that it significantly reduces the number of computer calculations.

It will be useful to distinguish between sides of $E$ and the bisector that contains them, so we will use the following notation:

Definition 4.11 The intersection of $E$ with a given bounding bisector is called a bounding side. The 28 bounding sides will be denoted by
$$P^{k} r_{1}^{ \pm}=E \cap P^{k} \mathscr{R}_{1}^{ \pm} ; \quad P^{k} s_{1}^{ \pm}=E \cap P^{k} \mathscr{S}_{1}^{ \pm},$$
for $k=0, \pm 1, \pm 2, \pm 3$.
The combinatorial structure of the bounding sides $P^{k} r_{1}^{ \pm}$and $P^{k} s_{1}^{ \pm}$is described in detail in Section 4.6.2. Note that for a polyhedron $E$ bounded by bisectors in $\mathbf{H}_{\mathbb{C}}^{2}$, it is by no means obvious how to determine the combinatorics of $E$ from the knowledge of its vertices, which explains the length of the sections stating and proving the combinatorics.

\subsection*{4.5.2 Symmetry}

The polyhedron $E$ is by definition $P$-invariant. Our notation for bisectors is set up so that the $P$-orbits can be conveniently read off their labels. For vertices (and mirrors of reflections), it is a bit more tedious but completely straighforward to study these orbits. For concreteness we treat a couple of examples in detail.

The basic point is that $P=R_{1} J$, and $J R_{k} J^{-1}=R_{k+1}$, i.e. conjugation by $J$ raises indices by one (mod 3). The $P$-image of the mirror of $R_{1}$, which corresponds to the complex line polar to $m_{1}$, is polar to $P m_{1}=m_{12 \overline{1}}$, since
$$P 1 P^{-1}=1 J 1 J^{-1} \overline{1}=12 \overline{1} .$$

The $P$-image of $p_{23}$ is simply $p_{13}$, since it is fixed by $P 23 P^{-1}=1 J 23 J^{-1} \overline{1}=131 \overline{1}=13$. Similarly, $P p_{13}=p_{12}$. Applying $P$ often yields slightly more complicated results, for instance the $P$-image of $p_{12}$ is given by $p_{P 12 P^{-1}}=p_{123 \overline{1}}$, since
$$P 12 P^{-1}=1 J 12 J^{-1} \overline{1}=123 \overline{1} .$$

It will be important in the sequel to observe that $E$ also has an anitholomorphic involutive symmetry, which we now explain. The antiholomorphic map
$$\iota_{23}:\left[\begin{array}{c}
z_{1} \\
z_{2} \\
z_{3}
\end{array}\right] \longmapsto\left[\begin{array}{c}
\bar{z}_{1} \\
\bar{z}_{3} \\
\bar{z}_{2}
\end{array}\right] .$$
clearly induces an isometry of $\mathbf{H}_{\mathbb{C}}^{2}$, since $\left\langle\iota_{23} \mathbf{v}, \iota_{23} \mathbf{w}\right\rangle=\overline{\langle\mathbf{v}, \mathbf{w}\rangle}$. It is easy to see that $\iota_{23}$ conjugates $J$ into $J^{-1}, R_{1}$ into $R_{1}^{-1}, R_{2}$ into $R_{3}^{-1}$ and $R_{3}$ into $R_{2}^{-1}$. From this it follows that the antiholomorphic map $\iota$ given by
$$\iota=R_{1} \iota_{23}$$
is an involution as well, and this will be useful several times throughout the paper.
Proposition 4.12 The involution $\iota$ preserves $E$, sending $r_{1}$ to $r_{1}^{-}$and $s_{1}$ to $s_{1}^{-}$.
Proof. Since $P=R_{1} J$, it follows easily that $\iota$ conjugates $R_{1}$ into $R_{1}^{-1}$, and $P$ into $P^{-1}$ (beware that $\iota_{23}$ does not conjugate $P$ into $P^{-1}$ ). In particular, $\iota$ fixes $\mathbf{p}$.

The fact that $\iota$ conjugates $S_{1}$ into $S_{1}^{-1}$ follows from the fact that $S_{1}$ can be expressed as a palindromic word in $R_{1}$ and $P$, namely $S_{1}=P^{2} R_{1} P^{-2} R_{1} P^{2}$.

Hence $\iota$ sends the half-space containing $\mathbf{p}$ bounded by $P^{k} \mathscr{R}_{1}^{ \pm}$(respectively $P^{k} \mathscr{S}_{1}^{ \pm}$) to the half-space containing $\mathbf{p}$ bounded by $P^{-k} \mathscr{R}_{1}^{\mp}$ (respectively $P^{-k} \mathscr{S}_{1}^{\mp}$ ). This show that $\iota$ preserves $F$, and this implies that it preserves $E$ (which is the connected component of $F$ containing p). \(\square\)

Note that $\iota$ conjugates an isometry given by a word $w$ (see Section 4.2) into the isometry given by the word $1 w^{\prime} \overline{1}$, where $w^{\prime}$ is obtained from $w$ by replacing each occurrence of 1,2,3 by $\overline{1}, \overline{3}, \overline{2}$ respectively. One can then read the action of $\iota$ on the vertices $p_{w}, q_{w}$ by applying this rule to the label $w$. For instance, we have
$$\begin{aligned}
& \iota\left(p_{12}\right)=p_{1 \overline{1} \overline{3} \overline{1}}=p_{\overline{3} \overline{1}}=p_{13} \\
& \iota\left(p_{23}\right)=p_{1 \overline{3} \overline{2} \overline{1}}=p_{123 \overline{1}},
\end{aligned}$$
and
$$\iota\left(q_{123 \overline{2}}\right)=q_{\overline{3} \overline{2} 3 \overline{1}}=q_{1 \overline{3} 23}$$
Observe that $P p_{13}=p_{12}$ implies $P^{3} p_{12}=P^{-3} p_{13}$. Since $p_{\overline{3} \overline{2} 3123}=R_{3}^{-1} R_{2}^{-1} R_{1}^{-1} p_{13}=P^{-3} p_{13}$ and $\iota\left(p_{\overline{3} \overline{2} 3123}\right)=R_{1}\left(p_{23 \overline{2} \overline{1} \overline{3} \overline{2}}\right)=R_{1} R_{2} R_{3} p_{12}=P^{3} p_{12}$, we get
$$\iota\left(p_{\overline{3} \overline{2} 3123}\right)=p_{\overline{3} \overline{2} 3123} .$$

\subsection*{4.5.3 Alternative descriptions}

Since the bounding bisectors $\mathscr{R}_{1}^{ \pm}, \mathscr{S}_{1}^{ \pm}$are central to the construction of the fundamental domain, it will be useful to have alternative descriptions. In Table 1 we write the bounding bisectors as equidistant from a pair of points and we also give some information that is useful for computational purposes; see also Section 4.8.3). We label vectors that appear in the table following the conventions from Section 4.2: $y_{0}$ denotes the intersection point of the complex spines of $\mathscr{R}_{1}$ and $\mathscr{S}_{1}$ (see below for explicit computation).

\begin{table}
\begin{tabular}[t]{|l|l|l|l|l|}
\hline Bisector & Equidistant & $\mathbb{R}$-spine & Polar & Reflections \\
\hline $\mathscr{R}_{1}$ & $\mathscr{B}\left(y_{0}, R_{1}^{-1} y_{0}\right)$ & $\operatorname{Span}_{\mathbb{R}}\left(\mathbf{n}_{1}, \mathbf{n}_{23}\right)$ & $\mathbf{f}_{1}=[0, \bar{\tau}, \bar{a} \tau]$ & 1, $(23)^{2}$ \\
\hline $\mathscr{R}_{1}^{-}$ & $\mathscr{B}\left(y_{0}, R_{1} y_{0}\right)$ & $\operatorname{Span}_{\mathbb{R}}\left(a^{2} \mathbf{n}_{1}, \bar{a} \mathbf{n}_{123 \overline{1}}\right)$ & $\mathbf{f}_{2}=\mathbf{f}_{1}$ & 1, $1(23)^{2} \overline{1}$ \\
\hline $\mathscr{S}_{1}$ & $\mathscr{B}\left(y_{0}, S_{1}^{-1} y_{0}\right)$ & $\operatorname{Span}_{\mathbb{R}}\left(a \mathbf{n}_{23 \overline{2}}, \mathbf{n}_{1 \overline{3} 23}\right)$ & $\mathbf{f}_{3}=\left[a^{2} \bar{\tau},-a,-\bar{\tau}\right]$ & $23 \overline{2},(1 \overline{3} 23)^{3}$ \\
\hline $\mathscr{S}_{1}^{-}$ & $\mathscr{B}\left(y_{0}, S_{1} y_{0}\right)$ & $\operatorname{Span}_{\mathbb{R}}\left(\bar{a} \mathbf{n}_{1 \overline{3} 23 \overline{1}}, \mathbf{n}_{123 \overline{2}}\right)$ & $\mathbf{f}_{4}=\left[a^{2} \bar{\tau}, a \tau, 1\right]$ & $1 \overline{3} 23 \overline{1},(123 \overline{2})^{3}$ \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 1: Descriptions of the bisectors $\mathscr{R}_{1}^{ \pm}$and $\mathscr{S}_{1}^{ \pm}$as equidistant hypersurfaces, and in terms of vectors spanning their extended real spines. We also give polar vectors for their complex spines and reflections whose mirrors are contained in each bisector (the mirror is either a complex line or a point, depending on the value of $p$ ).}
\end{table}

In the table, we list two vectors $\mathbf{w}, \mathbf{v}$ with real inner products, so that the extended real spine is obtained by taking real linear combinations of these two vectors (the real spine corresponds to such vectors with negative square norm). For convenience, we also give a polar vector to the complex spine, i.e. a nonzero vector $\mathbf{f}$ with $\langle\mathbf{w}, \mathbf{f}\rangle=\langle\mathbf{v}, \mathbf{f}\rangle=0$, as well as specific reflections whose mirrors are slices of these bisectors.

Proposition 4.13 The bisectors $\mathscr{R}_{1}, \mathscr{R}_{1}^{-}, \mathscr{S}_{1}$ and $\mathscr{S}_{1}^{-}$are all coequidistant from a point in $\mathbf{H}_{\mathbb{C}}^{2}$, which we denote by $y_{0}$. More specifically, $\mathscr{R}_{1}^{ \pm}=\mathscr{B}\left(y_{0}, R_{1}^{\mp 1} y_{0}\right)$ and $\mathscr{S}_{1}^{ \pm}=\mathscr{B}\left(y_{0}, S_{1}^{\mp} y_{0}\right)$.

Proof. From a pair of vectors w, v spanning the real spine of a bisector, one easily finds a vector orthogonal to both of them, since this amounts to finding a vector f that satisfies
$$\mathbf{w}^{*} H \mathbf{f}=\mathbf{v}^{*} H \mathbf{f}=0$$
which is a linear system in f. This allows us to get formulae for the four vectors $\mathbf{f}_{j}$. Note that $\mathscr{R}_{1}$ and $\mathscr{R}_{1}^{-}$are cospinal, i.e. they have the same complex spine.

From the $\mathbf{f}_{j}$, one can easily find the intersection between two of the complex spines, again by solving a linear system. The vector $\mathbf{y}_{0}$ can obtained in this way, being the unique intersection point of the complex spines of $\mathscr{R}_{1}$ and $\mathscr{S}_{1}$. For future reference, we give explicit coordinates:
$$\mathbf{y}_{0}=\left[\begin{array}{c}
-a^{3}\left(\bar{a}^{2} \bar{\tau}+a\right)^{2} \\
\left(a^{2} \bar{\tau}+\bar{a} \tau\right)\left(a^{2} \bar{\tau}-\bar{a}\right) \\
\left(a^{2} \bar{\tau}+\bar{a} \tau\right)\left(\bar{a}^{2} \tau-a\right)
\end{array}\right],$$
One easily checks that $\left\langle\mathbf{y}_{0}, \mathbf{f}_{j}\right\rangle=0$ for all $j=1,2,3,4$, so that all four bisectors $\mathscr{R}_{1}^{ \pm}, \mathscr{S}_{1}^{ \pm}$are equidistant from $\mathbf{y}_{0}$. A further simple check shows that $\left\langle\mathbf{y}_{0}, \mathbf{y}_{0}\right\rangle<0$ and so $\mathbf{y}_{0}$ corresponds to a point $y_{0} \in \mathbf{H}_{\mathbb{C}}^{2}$.

We now show that $\mathscr{R}_{1}=\mathscr{B}\left(y_{0}, R_{1}^{-1} y_{0}\right)$. From Table 1 we see that the spine of $\mathscr{R}_{1}$ is the real span of $\mathbf{n}_{1}$ and $\mathbf{n}_{23}$. These vectors are both fixed by the involution $\iota_{23}$ defined in (17), and so it also fixes any vector on the real spine of $\mathscr{R}_{1}$. Applying $\iota_{23}$ to $\mathbf{y}_{0}$ and simplifying, we see that $\iota_{23} \mathbf{y}_{0}=\bar{a}^{2} R_{1}^{-1} \mathbf{y}_{0}$. Therefore, if $\mathbf{s}$ is any vector in the real spine of $\mathscr{R}_{1}$ we have:
$$\left\langle\mathbf{y}_{0}, \mathbf{s}\right\rangle=\overline{\left\langle\iota_{23} \mathbf{y}_{0}, \iota_{23} \mathbf{s}\right\rangle}=a^{2} \overline{\left\langle R_{1}^{-1} \mathbf{y}_{0}, \mathbf{s}\right\rangle} .$$
Therefore, any point of $\mathscr{R}_{1}$ is equidistant from $y_{0}$ and $R_{1}^{-1} y_{0}$. Applying $R_{1}$ we see that $\mathscr{R}_{1}^{-}$ is equidistant from $R_{1} y_{0}$ and $y_{0}$.

Similarly, the involution $\overline{3} \overline{2} 3 \overline{1} \overline{3} \iota_{12}$ fixes $a \mathbf{n}_{23 \overline{2}}$ and $\mathbf{n}_{1 \overline{3} 23}$ and so fixes the spine of $\mathscr{S}_{1}$ pointwise. We calculate that $\overline{3} \overline{2} 3 \overline{1} \overline{3} \iota_{12} \mathbf{y}_{0}=\bar{a}^{2} S_{1}^{-1} \mathbf{y}_{0}$. Hence $\mathscr{S}_{1}=\mathscr{B}\left(y_{0}, S_{1}^{-1} y_{0}\right)$. Applying $S_{1}$, we find that $\mathscr{S}_{1}^{-}=\mathscr{B}\left(S_{1} y_{0}, y_{0}\right)$. \(\square\)

Later, in Table 3 we describe $\mathscr{R}_{1}^{ \pm}, \mathscr{S}_{1}^{ \pm}$and their images under powers of $P$ as equidistant hypersurfaces with respect to some other points.

\subsection*{4.6 Combinatorics of $E$}

In this section we describe the combinatorics of $E$ and show that it is a topological ball with piecewise smooth boundary, each piece being contained in one of the bounding bisectors. The proof of the precise combinatorics of $E$ is difficult, but necessary to apply the Poincaré polyhedron theorem. In fact it is delicate even to give a detailed description of the combinatorics (this will be done in Section 4.6.1). Indeed, for a general polyhedron bounded by bisectors in $\mathbf{H}_{\mathbb{C}}^{2}$, it is not sufficient to give the vertices, as there can be for instance distinct 1-cells joining two given vertices (see [DFP05]).

In order to prove the combinatorics, we first construct a combinatorial model $\widehat{E}$ for $E$. We then describe its geometric realization, which is a map $\phi$ from $\widehat{E}$ into $\overline{\mathbf{H}}_{\mathbb{C}}^{2}$, sending each 3-cell into one of the bounding bisectors (see Definition 4.8), and we prove that $\phi(\widehat{E})=E$.

This simultaneously proves the statement of the combinatorics of $E$, and shows that $E$ is a polyhedron in the sense of Section 3.2.

Our combinatorial model is somewhat similar to the one used by Schwartz in Section 6 of [Sch03]. However, our geometric realization of $\widehat{E}$ uses bisectors whereas Schwartz uses affine cells.

\subsection*{4.6.1 Statement of the combinatorics of $E$}

We state the combinatorics in the form of pictures of the 3-cells, with incidence information along each piece of the skeleton. Recall from Section 4 that $E$ only has two isometry classes of faces (applying $\iota$ and powers of $P$ ), so we need only draw pictures for $r_{1}=\mathscr{R}_{1} \cap E$ and $s_{1}=\mathscr{S}_{1} \cap E$.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/31f0f35c-0604-47ef-a2ef-a49ed021037c-33.jpg?height=1261&width=1518&top_left_y=951&top_left_x=288}
\captionsetup{labelformat=empty}
\caption{Figure 6: Adjacency relations of $r_{1}$ and $s_{1}$ with other faces of $\widehat{E}$, for $p=3,4$. Larger font is used to label ridges, and smaller fonts to label lower-dimensional facets.}
\end{figure}

Figures 6 to 8 give a concise, efficient description of the combinatorics. For each 3-face, we give two different pictures (top and bottom), one listing bisectors containing each facet, one listing vertices. At first glance, the pictures may seem a little cryptic, so we briefly explain how the incidence relations can be read off.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/31f0f35c-0604-47ef-a2ef-a49ed021037c-34.jpg?height=1176&width=1445&top_left_y=818&top_left_x=323}
\captionsetup{labelformat=empty}
\caption{Figure 7: Adjacency relations of $r_{1}$ and $s_{1}$ with other faces of $\widehat{E}$, for $p=5,6$. We draw curved lines when two neighboring edges lie on the same intersection of three bisectors.}
\end{figure}

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/31f0f35c-0604-47ef-a2ef-a49ed021037c-35.jpg?height=1181&width=1527&top_left_y=838&top_left_x=283}
\captionsetup{labelformat=empty}
\caption{Figure 8: Adjacency relations of $r_{1}$ and $s_{1}$ with other faces of $\widehat{E}$, for $p=8,12$.}
\end{figure}

Each cell in the picture is contained in the union of the cells whose names are on facets incident to that cell. As an example, we obtain the list of all bounding sides containing the vertex labelled $p_{12}$ on part (c) of Figure 6, Obviously it is contained in $r_{1}$. The picture in (a) suggests that it is on three 2-cells of $r_{1}$, whose labels indicate that $p_{12}$ is also on $r_{1}^{-}, P^{-1} r_{1}^{-}$, and $P^{2} s_{1}$. Similarly, from the 1-cells of $r_{1}$ containing $p_{12}$, we see that it is also on $P r_{1}, P^{-3} s_{1}^{-}$ and $P^{2} r_{1}$. Finally, the labels near that vertex in part (a) of the Figure indicate that it is on $P r_{1}^{-}, P^{-3} s_{1}$ and $P^{-1} s_{1}^{-}$. (See Remark 6.1 below for the vertex notation $p_{u}^{v}, q_{u}^{v}$ ).

Note that the pictures for $P^{k} r_{1}$ and $P^{k} s_{1}$ are obtained simply by applying $P^{k}$, whereas those for $P^{k} r_{1}^{-}$and $P^{k} r_{1}^{-}$one also needs to apply the antiholomorphic involution $\iota$ from Section 4.5.2. Recall that $\iota$ conjugates $R_{1}$ into $R_{1}^{-1}, S_{1}$ into $S_{1}^{-1}$, and $P$ into $P^{-1}$, so the image of the figures in part (a) and (b) under $\iota$ are obtained simply by changing signs. For the figures in parts (c) and (d), one needs to use the description of the action of $\iota$ on vertices according to their labels (see Section 4.5.2).

Remark 4.14 • The vector $\mathbf{n}_{23}$ is a negative vector when $p=3$ and a null vector when $p=4$. The corresponding point $p_{23}$ is therefore in $\mathbf{H}_{\mathbb{C}}^{2}$ and on $\partial \mathbf{H}_{\mathbb{C}}^{2}$ respectively. Hence, for $p=3$ and $p=4$, the combinatorics of the polyhedra $E$ are only the same when viewed in $\mathbf{H}_{\mathbb{C}}^{2} \cup \partial \mathbf{H}_{\mathbb{C}}^{2}$, some vertices being on the ideal boundary for $p=4$ (see also the discussion around Figure 2). A similar remark is in order for $p=5$ and $p=6$, since for $p=6$ the polyhedron $E$ has vertices on the ideal boundary $\partial \mathbf{H}_{\mathbb{C}}^{2}$.
\begin{itemize}
\item[-] The vector $\mathbf{n}_{23}$ is a positive vector when $p \geqslant 5$. Therefore the vertex $p_{23}$ of $r_{1}$ is replaced with a ridge in $m_{23}$, the complex line polar to $\mathbf{n}_{23}$. We refer to this process as truncation. In $s_{1}$, the vertex $p_{23}$ is only replaced with an edge in $m_{23}$ since it only intersects two complex lines orthogonal to $m_{23}$, namely $m_{23 \overline{2}}$ and $m_{\overline{3} 23}$. Similarly, the vertices $p_{12}, p_{13}$ of $r_{1}$ and the vertex $p_{\overline{3} \overline{2} 3123}$ of $s_{1}$ are replaced with edges in the corresponding complex lines. A second truncation process occurs for the $q_{*}$ vertices for $p \geqslant 8$. We use notation of the from $p_{u}^{v}, q_{u}^{v}$ for the new vertices appearing after truncation: $p_{u}^{v}$ or $q_{u}^{v}$ denotes the intersection of the complex lines polar to $\mathbf{n}_{u}$ and $\mathbf{n}_{v}$.
\end{itemize}

\subsection*{4.6.2 Outline of the geometrization of the combinatorial model $\widehat{E}$}

In this section, we build a combinatorial model $\widehat{E}$ for $E$. To keep the notation reasonable, we do not introduce new symbols for the facets of $\widehat{E}$, and simply label them the same as the corresponding facets of $E$.

In order to define $\widehat{E}$, we first define its 3-skeleton $\widehat{E}_{3}$. This is made up of 28 cells, attached according to the adjacency relations indicated in Figures 6 to 8.

Note that each 2-cell is on precisely two 3-cells, which makes it obvious which combinatorial 2-cells get identified. The gluing is then uniquely determined by matching labels of the vertices. The identifications for 0 and 1-cells are most conveniently read off parts (c), (d) of the figures. Indeed the action of $\iota$ and $P$ on the vertices can easily be read off the labels; see Section 4.6.1 and also Tables 16 to 19 in the appendix (Section 7).

It is easy to see that all $k$-cells of the 3 -skeleton $\widehat{E}_{3}$ are homeomorphic to embedded closed balls, and in particular for each $k$-cell $f$ of $\widehat{E}_{3}, \partial f$ is an embedded $(k-1)$-sphere (see Figures 6 through 8).

We will also prove the following, which is much less obvious (see Section 4.7).
Theorem $4.15 \widehat{E}_{3}$ is homeomorphic to $S^{3}$.

This allows us to define $\widehat{E}$, which is obtained by attaching a single 4-cell to $\widehat{E}_{3}$ in the obvious manner.

We now describe a piecewise smooth geometric realization $\phi: \widehat{E} \rightarrow \overline{\mathbf{H}}_{\mathbb{C}}^{2}$, i.e. we describe a specific $k$-ball in $\overline{\mathbf{H}}_{\mathbb{C}}^{2}$ for each $k$-cell of $\widehat{E}$. Naturally, the realization is uniquely determined by the requirement that each 3-cell be mapped into the appropriate bisector (or rather its closure in $\overline{\mathbf{H}}_{\mathbb{C}}^{2}$, since for $p=4$ or 6 some vertices of $E$ lie on the ideal boundary).

We define $\phi$ inductively on dimension, starting from vertices, then extending it successively to the 1-skeleton, then to the 2-skeleton, and so forth. When realizing the $k$-faces, we will check the following conditions on the restriction of $\phi$ to the $k$-skeleton $\widehat{E}_{k}$ :
\begin{itemize}
\item[-] (Consistency) For each $k$-face $f, \phi(f)$ is contained in all the bisectors indicated by the labels in Figures 6 through 8:
\item[-] (Correct side) $\phi\left(\widehat{E}_{k}\right)$ is entirely contained in $F$;
\item[-] (Embeddedness) $\phi$ gives an embedding of $\widehat{E}_{k}$.
\end{itemize}
The consistency condition is obvious for 2 and 3-faces, but it requires some calculations for vertices and edges (note that these lie on more bisectors than their codimension).

The fact that $\phi\left(\widehat{E}_{k}\right)$ lies inside $F$ amounts to showing that for each bounding bisector $\mathscr{B}$, $\phi\left(\widehat{E}_{k}\right)$ is on the same side of $\mathscr{B}$ as $\mathbf{p}$. We will do this by analyzing, for each $k$-face $f$, the intersection $f \cap \mathscr{B}$ with every bounding bisector $\mathscr{B}$. Because the intersection patterns of $F$ are governed by the intersection of bisectors, the "correct side" condition actually implies the embeddedness.

Note that $\phi(\widehat{E})$ is connected, so $\phi(\widehat{E}) \subset F$ actually implies $\phi(\widehat{E}) \subset E$ (recall that $E$ is the connected component of $F$ containing p), provided we can connect p to a single point in $\phi(\widehat{E})$ within $F$. This is contained in the following result, which is easily proved by giving explicit parametrizations for the relevant geodesic segments (see Section 4.8.2), and checking that p is on the correct side of the 28 bounding bisectors.

Lemma 4.16 For $p=3,4$ (respectively $p=5,6,8,12$ ) the geodesic segment $\left[\mathbf{p}, p_{12}\right]$ (resp. $\left[\mathbf{p}, p_{12}^{1}\right]$ ) intersects the 28 bounding bisectors at most at the endpoint $p_{12}$ (resp. $p_{12}^{1}$ ). It is contained in $F$, whereas the complementary geodesic ray, from $p_{12}$ (resp. from $p_{12}^{1}$ ) to $\partial \mathbf{H}_{\mathbb{C}}^{2}$ is entirely outside $F$.

We now sketch the general scheme that allows us to construct the geometric realization $\phi$. For vertices, the labels in the bottom part of Figures 6 through 8 determine an embedding of the 0-skeleton of $\widehat{E}$ (each vertex is the fixed point of a specific isometry in the group). The embedding part of this statement corresponds simply to the fact that all vertices in the list are distinct. The consistency condition will be checked in Section 4.8.1, and the correct side condition then amounts to checking a small set of (strict) inequalities, which can easily be done with a computer.

Now let $k \geqslant 1$, and suppose $\phi$ is already known to give an embedding of the $(k-1)$-skeleton. In order to extend $\phi$ across a $k$-cell $f$ of $\widehat{E}$, we exhibit a specific closed $k$-dimensional ball $D^{k}$ in $\overline{\mathbf{H}}_{\mathbb{C}}^{2}$ containing the $(k-1)$-skeleton of $f$, which is in fact forced by the consistency condition. More specifically, for $k=1$, each ball is simply the (unique) real geodesic segment between the two vertices realizing the 0-skeleton of $f$. For $k=2$ or 3, the $k$-ball is given by the intersection of $4-k$ (closures of) bisectors. The specific set of bisectors is obtained from the labels in Figures 6 to 8. Finally, for $k=4$, the ball is of course the whole of $\overline{\mathbf{H}}_{\mathbb{C}}^{2}$.

Since we assume $\phi$ induces an embedding of the $(k-1)$ skeleton, $\phi(\partial f)$ is a piecewise smoothly embedded $(k-1)$-sphere in $D^{k}$ (with finitely many points on $\partial \mathbf{H}_{\mathbb{C}}^{2}$ ). This gives a well-defined $k$-ball that realizes $f$. Implicit in the above description is the assumption that the relevant pairs of bisectors intersect in disks, which will be proved in Section 4.8.3. We postpone the proof of consistency and embeddedness of the 0, 1, 2 and 3-skeletons, which will be discussed in Sections 4.8.1 through 4.8.5 (for clarity, we collect all results about each dimension in a separate section). Among all the consistency, correct side and embeddedness conditions, the most difficult one is correct side condition for the 2-skeleton. This relies on difficult computations, explained in detail in Section 4.8.4.

Assuming these results, we obtain a realization of all $\widehat{E}$, by mapping the single 4-cell to the 4-ball bounded by $\phi\left(\widehat{E}_{3}\right)$ (this is a piecewise smoothly embedded copy of $S^{3}$ so it bounds a well-defined closed ball). Note that this ball component contains the fixed point p of $P$, by Lemma 4.16. As a summary, we get the following:

Theorem $4.17 \phi$ defines an embedding of $\widehat{E}$, with image contained in $F$.
The following result then follows from elementary topology.
Corollary 4.18 The realization of $\widehat{E}$ is equal to $E$. In particular, $E$ is a polyhedron in the sense of Section 3.2.

Proof. (of Corollary 4.18) By Theorem 4.17, $\phi(\widehat{E}) \subset E$. We now show $E \subset \phi(\widehat{E})$. No point of $E^{\circ}$ is contained in any of the 28 bounding bisectors, hence $E^{\circ}$ has empty intersection with $\phi\left(\widehat{E}_{3}\right)$. Since $E^{\circ}$ is connected and contains p, which is contained in $\phi(\widehat{E})$, we get that $E \subset \phi(\widehat{E})$ as required. \(\square\)

\section*{$4.7 \widehat{E}_{3}$ is homeomorphic to $S^{3}$}

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/31f0f35c-0604-47ef-a2ef-a49ed021037c-38.jpg?height=563&width=1386&top_left_y=1718&top_left_x=352}
\captionsetup{labelformat=empty}
\caption{Figure 9: The combinatorics of the intersection $T^{r} \cap T^{s}$, for $p=3,4$. This intersection is a torus, and accordingly the top and bottom sides (resp. left and right sides) are identified by translation. The bold lines describe 2 splittings of the torus into annuli, corresponding to splittings of the solid tori into pairs of solid cylinders.}
\end{figure}

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/31f0f35c-0604-47ef-a2ef-a49ed021037c-39.jpg?height=400&width=1541&top_left_y=584&top_left_x=275}
\captionsetup{labelformat=empty}
\caption{Figure 10: The combinatorics of the intersection $T^{r} \cap T^{s}$, for $p=5,6$.}
\end{figure}

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/31f0f35c-0604-47ef-a2ef-a49ed021037c-39.jpg?height=675&width=1543&top_left_y=1512&top_left_x=275}
\captionsetup{labelformat=empty}
\caption{Figure 11: The combinatorics of the intersection $T^{r} \cap T^{s}$, for $p=8,12$. The torus is now not embedded, the white squares correspond to pinch points, i.e. they come in pairs that get identified in $\mathbf{H}_{\mathbb{C}}^{2}$.}
\end{figure}

This section contains a proof of Theorem 4.15. We will exhibit $\widehat{E}_{3}$ as the union of two solid tori with common boundary, and check that the boundary circles of a meridian in each intersect at a single point.

In order to do this, consider the following two unions of 3-cells:
$$T^{r}=\bigcup_{k=-3}^{3} P^{k}\left(r_{1} \cup r_{1}^{-}\right) \quad \text { and } \quad T^{s}=\bigcup_{k=-3}^{3} P^{k}\left(s_{1} \cup s_{1}^{-}\right) .$$
Note that these are clearly $P$-invariant (hence their intersection is $P$-invariant as well).
For $p \leqslant 6$, these will turn out to give a solid torus decomposition. For $p=8,12$, the solid tori are obtained from these by an adequate local surgery, to be discussed later in the proof (see Lemma 4.22).

The combinatorial pattern of the intersection of $T^{r}$ and $T^{s}$ is depicted in Figures 9, 10 and 11 for various values of $p$ (compare this to Figure 6.2 of [Sch03]). These pictures can be obtained by somewhat painful bookkeeping from Figures 6 through 8 and their obvious variations, i.e. images under powers of $P$ and/or the antiholomorphic symmetry $\iota$.

A few remarks are in order for the pictures to be read properly. First note that we cannot draw a Euclidean plane figure, since hexagonal faces of $T^{r} \cap T^{s}$ are often glued along two consecutive sides. For instance, we represent hexagons by triangles, thinking of the midpoint of the edge of the triangle as a vertex of the hexagon (see Figure 11).

Secondly, the pictures are embedded in $\widehat{E}_{3}$ only for $p=3,4,5$ and 6; for $p=8$ or 12, the intersection $T^{r} \cap T^{s}$ is obtained from the torus in Figure 11 by identifying 7 pairs of points, indicated in the figure by square vertices. We will refer to these 7 points as pinch points.

We first treat the case $p \leqslant 6$.
Lemma 4.19 If $p \leqslant 6$ then $T^{r}$ and $T^{s}$ are both solid tori, with union homeomorphic to $S^{3}$.
Note that it would suffice to prove that $\pi_{1}\left(T^{r}\right)=\pi_{1}\left(T^{s}\right)=\mathbb{Z}$. It would then follow from Seifert-Van Kampen that $\pi_{1}\left(\widehat{E}_{3}\right)=\pi_{1}\left(T^{r} \cup T^{s}\right)=1$, which implies that $\widehat{E}_{3}$ is homeomorphic to $S^{3}$ (this argument requires checking that $\widehat{E}_{3}$ is a manifold, which follows from the detailed study of the links of its vertices). Using the solution of the Poincaré conjecture seems like overkill, so we now give a bare hands proof.

We prove Lemma 4.19 by constructing disjoint closed disks $D_{1}^{r}$ and $D_{2}^{r}$ in $T^{r}$ whose complements are balls (and similarly $D_{1}^{s}$ and $D_{2}^{s}$ in $T^{s}$ ), and check that $D_{1}^{r}$ and $D_{1}^{s}$ intersect in a single point. The boundary of each of these disks is depicted in Figures 9 and 10; the bold horizontal line is $\partial D_{1}^{r}$, the top (or bottom) horizontal line is $\partial D_{2}^{r}$, and similarly for vertical lines and $\partial D_{j}^{s}$.

Specifically,
$$\begin{aligned}
& D_{1}^{s}=P^{-2} s_{1} \cap s_{1}^{-} \\
& D_{2}^{s}=P^{-1} s_{1} \cap P s_{1}^{-} \\
& D_{1}^{r}=\left(P^{3} r_{1} \cap P^{3} r_{1}^{-}\right) \cup\left(P^{-2} r_{1} \cap P^{2} r_{1}^{-}\right) \cup\left(P^{-3} r_{1} \cap P^{-3} r_{1}^{-}\right) \cup\left(P^{-3} r_{1} \cap P^{3} r_{1}^{-}\right), \\
& D_{2}^{r}=\left(P r_{1} \cap P^{-1} r_{1}^{-}\right) \cup\left(P r_{1} \cap P^{-2} r_{1}^{-}\right) \cup\left(r_{1} \cap r_{1}^{-}\right) \cup\left(P^{2} r_{1} \cap P^{-1} r_{1}^{-}\right) .
\end{aligned}$$
The fact that these are indeed disks is readily checked by using the description of the combinatorics and adjacency relations between the 3-cells given in Figures 6 to 7. The following is clear from those pictures:

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/31f0f35c-0604-47ef-a2ef-a49ed021037c-41.jpg?height=982&width=1545&top_left_y=368&top_left_x=278}
\captionsetup{labelformat=empty}
\caption{Figure 12: The combinatorics of the disks $D_{1}^{r}$ and $D_{2}^{r}$, for $p=5,6$.}
\end{figure}

Proposition 4.20 The circles $\partial D_{1}^{r}$ and $\partial D_{1}^{s}$ intersect in a single point.
For completeness, we give the combinatorial structure of the disks $D_{1}^{r}$ and $D_{2}^{r}$ in Figure 12.
We write $T^{r}=U^{r} \cup V^{r}$ (resp. $T^{s}=U^{s} \cup V^{s}$ ) for the decompositions corresponding to splitting along these disks, which are given in terms of 3-cells of $\widehat{E}_{3}$ by the following:
$$\begin{aligned}
& U^{s}=P s_{1} \cup P s_{1}^{-} \cup P^{3} s_{1} \cup P^{3} s_{1}^{-} \cup P^{-2} s_{1} \cup P^{-2} s_{1}^{-}, \\
& V^{s}=s_{1} \cup s_{1}^{-} \cup P^{2} s_{1} \cup P^{2} s_{1}^{-} \cup P^{-3} s_{1} \cup P^{-3} s_{1}^{-} \cup P^{-1} s_{1} \cup P^{-1} s_{1}^{-}, \\
& U^{r}=r_{1} \cup P^{-1} r_{1} \cup P^{-1} r_{1}^{-} \cup P^{-2} r_{1} \cup P^{-2} r_{1}^{-} \cup P^{3} r_{1}^{-} \cup P^{-3} r_{1}^{-}, \\
& V^{r}=r_{1}^{-} \cup P r_{1} \cup P r_{1}^{-} \cup P^{2} r_{1} \cup P^{2} r_{1}^{-} \cup P^{3} r_{1} \cup P^{-3} r_{1} .
\end{aligned}$$
In order to prove Lemma 4.19, it is enough to prove the following.
Lemma 4.21 $U^{s}$ and $V^{s}$ are homeomorphic to balls, and intersect precisely in the two disks $D_{1}^{s}, D_{2}^{s}$. Likewise, $U^{r}$ and $V^{r}$ are homeomorphic to balls, and intersect precisely in the two disks $D_{1}^{r}, D_{2}^{r}$.

Proof. This follows from a careful study of the gluings, using the fact that each 3-cell of $\widehat{E}_{3}$ is a 3-ball. This is easiest for $U^{s}$ and $V^{s}$, since $F=s_{1} \cup s_{1}^{-}$is a ball, $F \cap P^{ \pm 2} F$ are both disks and $F \cap P^{4} F$ is empty; note that
$$V^{s}=F \cup P^{2} F \cup P^{4} F \cup P^{6} F \quad \text { and } \quad U^{s}=P F \cup P^{3} F \cup P^{5} F .$$

For the $r$-splitting, we write each of $U^{r}$ and $V^{r}$ as an increasing union, gluing a ball along a single closed disk at each stage. More specifically, given a subcomplex $Z$ (which is either
$U^{r}$ or $V^{r}$ ), we give an explicit sequence $C_{n}$ of subcomplexes with $C_{0}=F_{0}$ a 3-cell,
$$C_{n}=C_{n-1} \cup F_{n}$$
for a single 3-cell $F_{n}$ of $\widehat{E}_{3}$, and which terminates with $C_{N}=Z$. The point is to choose the 3-cells $F_{n}$ so that $F_{n} \cap C_{n-1}$ is homeomorphic to a disk.
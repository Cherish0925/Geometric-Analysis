---
retention_scope: session
part: 1
total_parts: 1
---

---
source_file: 2107_09969v1.pdf
converter: mathpix
format: mmd
---

\title{
ON THE GEOMETRY OF A PICARD MODULAR GROUP
}

\author{
MARTIN DERAUX
}

\begin{abstract}
We study geometric properties of the action of the Picard modular group $\Gamma=\operatorname{PU}\left(2,1, \mathcal{O}_{7}\right)$ on the complex hyperbolic plane $H_{\mathbb{C}}^{2}$, where $\mathcal{O}_{7}$ denotes the ring of algebraic integers in $\mathbb{Q}(i \sqrt{7})$. We list conjugacy classes of maximal finite subgroups in $\Gamma$, we give an explicit description of the Fuchsian subgroups that occur as stabilizers of mirrors of complex reflections in $\Gamma$. As an application, we show the existence of a torsion-free subgroup of index 336 in $\Gamma$.
\end{abstract}

\section*{1. Introduction}

The goal of this paper is to study some detailed geometric features of the Picard modular group $P U\left(J, \mathcal{O}_{7}\right)$, where $\mathcal{O}_{7}$ denotes the ring of algebraic integers in $\mathbb{Q}(i \sqrt{7})$, and
$$J=\left(\begin{array}{lll}
0 & 0 & 1 \\
0 & 1 & 0 \\
1 & 0 & 0
\end{array}\right) .$$
Since $J$ has signature $(2,1), P U(J)$ is actually isomorphic to the group $P U(2,1)$ of holomorphic isometries of the complex hyperbolic plane $H_{\mathbb{C}}^{2}$ (which is a symmetric space with $\frac{1}{4}$-pinched sectional curvature).

It is a standard fact that $U\left(J, \mathcal{O}_{7}\right)=U(J) \cap G L\left(3, \mathcal{O}_{7}\right)$ is a lattice in $U(J)$, i.e. a discrete subgroup such that the quotient of $H_{\mathbb{C}}^{2}$ under the action of $U\left(J, \mathcal{O}_{7}\right)$ has finite volume for the symmetric Riemannian metric. From this point on, to simplify notation, we write
$$X=H_{\mathbb{C}}^{2}, \quad G=P U(J), \quad \Gamma=P U\left(J, \mathcal{O}_{7}\right) .$$

The first explicit information about $\Gamma$ was an explicit finite generating set, see Zhao [13]. A standard way to find such a generating set is to work out a fundamental domain for the action, because the side-pairing maps of a fundamental domain generate the group. In principle, one could use the standard construction of Ford domains, but the Ford domain for $\Gamma$ turns out to be very complicated. In fact Zhao used coarser information than the actual Ford domain.

More recently, his method was refined by Mark and Paupert to get an actual presentation (generating set plus defining relations for the group), still without working out an explicit fundamental domain. The rough idea is to use a coarse fundamental domain, i.e. a set $\Omega$ such that $\Gamma \Omega=X$, and such that $T=\{\gamma \in \Gamma: \Omega \cap \gamma \Omega \neq \emptyset\}$ is finite. In that case, it is easy to see that $T$ generates $\Gamma$, and to write defining relations for the group (see [7] for

\footnotetext{
Date: July 21, 2021.
}
instance). In the discussion that follows, we assume we have a coarse fundamental domain and an explicit finite set $T$ as above.

The goal of the present paper is to push the Mark-Paupert techniques a bit further, and give a list of the conjugacy classes of torsion elements (and more generally of maximal finite subgroups) in $\Gamma$. See section 4 for the results.

This gives us some detailed information about the local structure of the quotient orbifold $X / \Gamma$; as far as I know, its global structure is still not understood. Note that, contrary to what was incorrectly stated in [2], the group $\Gamma$ is not the same as the sporadic group $\mathcal{S}\left(\bar{\sigma}_{4}, \infty\right)$, which is contained in $P U\left(H, \mathcal{O}_{7}\right)$ for another Hermitian form. In fact the group $\mathcal{S}\left(\bar{\sigma}_{4}, \infty\right)$ has trivial abelianization, whereas $\Gamma$ has abelianization $\mathbb{Z} / 2 \mathbb{Z}$. This was actually our initial motivation for studying the group $\Gamma$ in detail.

We will also determine the mirror stabililizers for the two conjugacy classes of complex reflections in $\Gamma$ (see section 5; it is a standard fact that these are Fuchsian subgroups, but it is not exactly obvious how to describe these stabilizers explicitly (generating set, signature). We find that one stabilizer has a single cusp, whereas the other has two (the latter case makes for much more complicated computations).

From our list of torsion conjugacy classes, we deduce the existence of a torsion-free subgroup of index 336 in $\Gamma$, which is a principal congruence subgroup (the kernel of the reduction modulo the ideal $\langle i \sqrt{7}\rangle$ ). This is done in section 7.

Note that the methods used in this paper should work for all 1-cusped Picard groups (this happens for slightly more values of $d$, namely $d=1,2,3,7,11,19,43,67,163$ ), but they would require much heavier computation (presentations are known only for $d=1,2,3,7,11$, see [4], [3], [8], [11], [6], [5]).

\section*{2. Complex hyperbolic geometry and Ford domains}

We work in homogeneous coordinates $v=\left(v_{1}, v_{2}, v_{3}\right)$ and write $\langle v, w\rangle=w^{*} J v,\|v\|^{2}=$ $\langle v, v\rangle$. The set of complex lines in $\mathbb{C}^{3}$ that are spanned by a negative vector (i.e. a vector $v \in \mathbb{C}^{3}$ with $\|v\|^{2}<0$ ) is contained in the affine chart $v_{3} \neq 0$ of $P_{\mathbb{C}}^{3}$, where $v$ can be represented as $\left(\frac{v_{1}}{v_{3}}, \frac{v_{2}}{v_{3}}, 1\right)=\left(z_{1}, z_{2}, 1\right)$, with $2 \Re\left(z_{1}\right)+\left|z_{2}\right|^{2}<0$. The distance function in complex hyperbolic space is given by a simple formula in homogeneous coordinates, namely
$$\cosh \left(\frac{1}{2} d([v],[w])\right)=\frac{|\langle v, w\rangle|}{\sqrt{\langle v, v\rangle\langle w, w\rangle}},$$
where $[v]=\mathbb{C} v$ denotes the complex line spanned by $v$. The boundary at infinity of the complex hyperbolic plane, which consists of complex lines spanned by null vectors (i.e. vectors $v \in \mathbb{C}^{3}$ with $\|v\|^{2}=0$ ), is almost entirely contained in the affine chart $z_{3} \neq 0$, only one point is missing, namely $q_{0}=(1,0,0)$. We usually refer to that point as the point at infinity.

Rather than the affine coordinates $\left(z_{1}, z_{2}\right)$ described above, it is convenient to use horospherical coordinates $(z, t, u), z \in \mathbb{C}, t, u \in \mathbb{R}, u>0$, defined by
$$2 z_{1}+\left|z_{2}\right|^{2}=i t-u .$$

Using these coordinates, the hypersurfaces defined by taking $u$ to be a fixed positive constant are horospheres based at the point at infinity. Points with $u=0$ give the boundary at infinity $\partial_{\infty} H_{\mathbb{C}}^{2}$ of $H_{\mathbb{C}}^{2}$ (minus the point at infinity, corresponding to $q_{0}=(1,0,0)$ ).

Each of these points has a unique representative of the form
$$\left(\begin{array}{c}
\frac{-|z|^{2}+i t}{2} \\
z \\
1
\end{array}\right),$$
with $z \in \mathbb{C}$ and $t \in \mathbb{R}$.
The unipotent stabilizer of $q_{0}$ consists of the matrices of the form
$$T(z, t)=\left(\begin{array}{ccc}
1 & -\bar{z} & \frac{-|z|^{2}+i t}{2} \\
0 & 1 & z \\
0 & 0 & 1
\end{array}\right),$$
and it acts simply transitively on $H_{\mathbb{C}}^{2} \backslash\{\infty\}$. This gives $H_{\mathbb{C}}^{2} \backslash\{\infty\}$ the structure of a group, usually called the Heisenberg group. In terms of the coordinates $(z, t) \in \mathbb{C} \times \mathbb{R}$, the Heisenberg group law is the following:
$$(z, t) \star\left(z^{\prime}, t^{\prime}\right)=\left(z+z^{\prime}, t+t^{\prime}+2 i \operatorname{Im}\left(z \bar{z}^{\prime}\right)\right) .$$

Following the notation in section 4.3 of [8], we define
$$T_{1}=T(1, \sqrt{7}), \quad T_{\tau}=T(\tau, 0), \quad T_{v}=T(0,2 \sqrt{7}),$$
where $\tau=\frac{1+i \sqrt{7}}{2}$.
Non-unipotent parabolic elements are usually called twist-parabolic elements; they can be written as $R T(z, t)$ where $R=\operatorname{diag}(1, \zeta, 1),|\zeta|=1$, i.e.
$$R T(z, t)=\left(\begin{array}{ccc}
1 & -\bar{z} & \frac{-|z|^{2}+i t}{2} \\
0 & \zeta & z \\
0 & 0 & 1
\end{array}\right)$$
Since we consider $\Gamma=P U\left(J, \mathcal{O}_{7}\right)$, we only allow for $\zeta$ the units in $\mathcal{O}_{7}$, namely $\pm 1$. From now on, once again following [8], we write $R=\operatorname{diag}(1,-1,1)$.

In the $\mathbb{C}$-factor of the Heisenberg group $\mathbb{C} \times \mathbb{R}, R$ acts as $z \mapsto-z$, and $T_{1}, T_{\tau}$ act as translations by 1 and $\tau$ respectively (whereas $T_{v}$ act trivially). Hence the triangle $D$ which is the Euclidean convex hull of 0, 1 and $\tau$ gives a fundamental domain for the action on $\mathbb{C}$. Note that $T_{1} R, T_{\tau} R$ and $T_{1} T_{\tau} R$ act in the $\mathbb{C}$ factor as half-turns fixing the midpoints of the sides of the triangle, see Figure 1. The group $\Gamma_{\infty}$ is actually generated by $T_{1}, T_{\tau}$ and $R$, see [10] for instance (note that $T_{v}=\left[T_{\tau}, T_{1}\right]$ ). Since $T_{v}$ acts as a translation by $2 \sqrt{7}$ in the $t$-coordinate, it should be quite clear that the prism $P=D \times[0,2 \sqrt{7}]$ is a fundamental domain for the action of $\Gamma_{\infty}$ in $\mathbb{C} \times \mathbb{R}$, see Figure 2. Note that $T_{\tau} R$ and $T_{1} T_{\tau} R$ are sidepairing maps for $P$ (in fact these are complex reflections), and $T_{v}$ as well (it gives the vertical translation pairing the top and bottom triangles of the prism). However $T_{1} R$ is not a side pairing-map (it is given by a glide-reflection), but this will be inconsequential in the present paper.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/1650d7d7-2c89-4c89-a0bb-715787182eea-04.jpg?height=517&width=489&top_left_y=324&top_left_x=802}
\captionsetup{labelformat=empty}
\caption{Figure 1. Action of the cusp group on the $\mathbb{C}$-factor of the Heisenberg group $\mathbb{C} \times \mathbb{R}$.}
\end{figure}

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/1650d7d7-2c89-4c89-a0bb-715787182eea-04.jpg?height=426&width=349&top_left_y=1009&top_left_x=871}
\captionsetup{labelformat=empty}
\caption{Figure 2. $P=D \times[0,2 \sqrt{7}]$ is a fundamental domain for the action of $\Gamma_{\infty}$ on $\mathbb{C} \times \mathbb{R}$}
\end{figure}

Definition 2.1. Let $\Gamma$ be a discrete subgroup of $G$. The Ford domain for $\Gamma$ is defined as
$$F_{\Gamma}=\left\{[x] \in H_{\mathbb{C}}^{2}:\left|\left\langle x, q_{0}\right\rangle\right| \leq\left|\left\langle x, \gamma q_{0}\right\rangle\right| \text { for all } \gamma \in \Gamma\right\}$$

In this definition, $\gamma q_{0}$ stands for $\tilde{\gamma} q_{0}$ for any lift $\tilde{\gamma} \in U\left(J, \mathcal{O}_{7}\right)$ of $\gamma \in \Gamma=P U\left(J, \mathcal{O}_{7}\right)$. Each $\gamma \in \Gamma$ has precisely two lifts that differ by multiplication by $-I d$ (because the only roots of unity in $\mathcal{O}_{7}$, namely 1 and -1), so the inequalities in Definition 2.1 are independent of the lift chosen.

Here and in the rest of the paper, we denote by $\Gamma_{\infty}$ be the stabilizer of the point at $\infty$, i.e. the subgroup of matrices that have $q_{0}$ as an eigenvector. The inequalities in the definition corresponding to elements in $\Gamma_{\infty}$ play no role, so it should be clear that $F_{\Gamma}$ is not a fundamental domain for $\Gamma$.

In order to get a fundamental domain, we select a fundamental domain $P$ for the action of $\Gamma_{\infty}$ in Heisenberg, consider the cone $C_{P}$ with base $P$ in horospherical coordinates:
$$C_{P}=\{(z, t, u):(z, t) \in P, u>0\} .$$
Then we have:

Proposition 2.1. $F_{W} \cap C_{P}$ is a fundamental domain for $\Gamma$.
Note that even $F_{W} \cap C_{P}$ need not have well-defined side-pairing maps, the sides of the Ford domain $F_{W}$ are paired. In fact, given $\gamma \in \Gamma \backslash \Gamma_{\infty}$, write
$$I(\gamma)=\left\{[x] \in H_{\mathbb{C}}^{2}:\left|\left\langle x, q_{0}\right\rangle\right| \leq\left|\left\langle x, \gamma q_{0}\right\rangle\right|\right\} .$$
It follows easily from the definition that $\gamma^{-1}(I(\gamma))=I\left(\gamma^{-1}\right)$, hence the set $F_{\Gamma} \cap I(\gamma)$, if it is a side (i.e. if it has dimension 3), must be paired with $F_{\Gamma} \cap I\left(\gamma^{-1}\right)$ by $\gamma^{-1}$.

The set $I(\gamma), \gamma \in \Gamma \backslash \Gamma_{\infty}$ can be interpreted as a bisector (locus equidistant of two points in $H_{\mathbb{C}}^{2}$ ), or as an isometric sphere (locus of points where the Jacobian of the transformation is 1), or as a metric sphere for the so-called extended Cygan distance, defined by
$$d_{\text {Cygan }}\left((z, t, u),\left(z^{\prime}, t^{\prime}, u^{\prime}\right)\right)=\left(\left(\left|z-z^{\prime}\right|^{2}+\left|u-u^{\prime}\right|\right)^{2}+\left|t-t^{\prime}+2 i \operatorname{Im}\left(z \bar{z}^{\prime}\right)\right|^{2}\right)^{1 / 4} .$$
Using this distance, we can describe $I(\gamma)$ as the Cygan sphere with center $\gamma(\infty)$, and radius $\sqrt{2 /\left|a_{31}\right|}$, where $A=\left(a_{j k}\right)_{j, k=1,2,3}$ is a matrix representative of $\gamma$ (see [8] for instance).

It can be useful also to have an explicit expression for the Cygan sphere of radius $r$ centered at the point $(c, d) \in \mathbb{C} \times \mathbb{R}$ in Heisenberg, namely it consists of points with horospherical coordinates $(z, t, u) \in \mathbb{C} \times \mathbb{R} \times \mathbb{R}_{+}$satisfying
$$\left(\left(|z-c|^{2}+u\right)^{2}+|t-d+2 i \operatorname{Im}(z \bar{c})|^{2}\right)=r^{4} .$$
The basic observation is that if $(z, t, u)$ is in that sphere, then $|z-c| \leq r$ so the $\mathbb{C}$ -component must be contained in the Euclidean disk of radius $r$ centered at $c$. We also have an estimate for the basic estimates $u \leq r^{2}$ and $|t-d| \leq r^{2}$, which gives us some rough control of the size of Cygan spheres in horospherical coordinates.

The domain $P$ is chosen to have affine sides in Heisenberg (since the Heisenberg group acts on itself by affine transformations, see formula (2)). It can also be adjusted to have well-defined side-pairing maps (this requires subdividing its sides into smaller polygons), but we will not do this, since we do not need it for any of the methods used in this paper.

A few Ford domains in $H_{\mathbb{C}}^{2}$ have been studied explicitly, see [1], [9]. Such domains are virtually present in [13] and [8], but it is very complicated to determine their combinatorial structure in detail (or even to describe it on paper!)

To give a rough idea, pictures of (representatives of the isometry type of) the sides of the Ford domain for $\Gamma=U\left(J, \mathcal{O}_{7}\right)$ are given in Figure 3. Needless to say, these pictures will be used anywhere in the paper, but they should give an idea of the intricacy of the combinatorics.

\section*{3. Virtual fundamental domain, algorithms}

Recall that a coarse fundamental domain for a discrete group $\Gamma$ is a set $\Omega$ such that $\Gamma \Omega=X$, and such that $T=\{\gamma \in \Gamma: \Omega \cap \gamma \Omega \neq \emptyset\}$ is finite. In that case, it is easy to see that $T$ generates $\Gamma$, and it is easy to write a group presentation in terms of these generators (see section 13.4 in [7]).

Of course a fundamental domain is a coarse fundamental domain, and this is the kind of coarse fundamental domain we will (virtually) use in this paper. Specifically, we will use

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/1650d7d7-2c89-4c89-a0bb-715787182eea-06.jpg?height=980&width=902&top_left_y=365&top_left_x=592}
\captionsetup{labelformat=empty}
\caption{Figure 3. Sides of the Ford domain for $P U\left(J, \mathcal{O}_{7}\right)$ (four views for each side).}
\end{figure}
$\Omega=F_{\Gamma} \cap C_{P}$, where $C_{P}$ is the cone to the point at infinity in horospherical coordinates, and $P$ is the prism described in [8], i.e.
$$\Omega=\{(a+b \tau, t): 0 \leq a, b, a+b \leq 1,0 \leq t \leq 2\} .$$
By making virtual use of this domain, we mean that, rather than studying the combinatorics of $\Omega$, we will only use algorithmic procedures that allow us to do the following.

Method 3.1. (1) Determine whether a given algebraic point $[x] \in H_{\mathbb{C}}^{2}$ is inside $\Omega$, and list the sides of $\Omega$ that contain it;
(2) If $[x]$ is not in $\Omega$, find an element $\gamma \in \Gamma$ such that $\gamma[x] \in \Omega$.

By an algebraic point $[x] \in H_{\mathbb{C}}^{2}$, we mean that it can be represented in homogeneous coordinates by a vector $x \in \mathbb{C}^{3}$ with algebraic coordinates.

We briefly explain why such methods can be implemented effectively. The main difficulty is that $[X] \in \Omega$ is defined in terms of an infinite set of inequalities.

We first make use of the results in [8], that give us an estimate of the elements $\gamma \in \Gamma$ that play a role in definition (2.1), based on arithmetic considerations.

Definition 3.1. A $\mathbb{K}$-rational point in $P_{\mathbb{C}}^{2}$ is a point that can be represented in homogeneous coordinates as a vector with entries in $\mathcal{O}_{\mathbb{K}}$.

A given a rational point has an essentially unique primitive representative in $\mathcal{O}_{\mathbb{K}}^{3}$, i.e. a vector whose entries have greatest common divisor equal to 1. The only freedom we have to change such a vector is to scale it by unit, and the only units in $\mathcal{O}_{7}$ are $\pm 1$.

By the square norm of a point in $P^{2} \mathbb{C}$, we mean $\|v\|^{2}=v^{*} J v$ for any primitive representative $v \in \mathcal{O}_{\mathbb{K}}^{3}$. Points (resp. vectors) with square norm 0 are called null points (resp. vectors).

Proposition 3.1. For every $A \in U\left(J, \mathcal{O}_{7}\right)$, the first column of $A$ (which represents $A(\infty)$ ) is a primitive null vector in $\mathcal{O}_{\mathbb{K}}^{3}$. Conversely, given any primitive null vector $v \in \mathcal{O}_{\mathbb{K}}^{3}$, there exists an $A \in U\left(J, \mathcal{O}_{7}\right)$ whose first column is $v$.

The converse direction says that the Picard group $\Gamma=U\left(J, \mathcal{O}_{7}\right)$ acts transitively on $\mathbb{K}$-rational null vectors; this is can be reformulation as the statement that the quotient $X / \Gamma$ has exactly one cusp, which is a consequence of the fact that $\mathbb{K}$ has class number 1 (see [14] or section 4.1 in [12]). The theoretical result in Proposition 3.1 is unfortunately difficult to make effective, as discussed in [8].

We review the following definition (see [8]).
Definition 3.2. (1) The depth of a $\mathbb{K}$-rational point $[v] \in \partial_{\infty} H^{2} \mathbb{C} \backslash\{\infty\}$ is given by $\left|v_{3}\right|^{2}$, where $v=\left(v_{1}, v_{2}, v_{3}\right)$ is any primitive integral representative of $[v]$.
\begin{itemize}
\item[(2)] The depth of a matrix $A \in \Gamma$ is the depth of $A(\infty)$.
\end{itemize}

The notion of depth is important, in part because of the following Proposition.
Proposition 3.2. Let $A \in \Gamma$. Then the Cygan center of the isometric sphere $I(A)$ is represented by $A(\infty)$, and its radius is given by $\sqrt{2 / d}$, where $d$ is the depth of $A$.

Note that the depth of any $A \in \Gamma$ is a rational integer, but not every integer occurs as the depth of an element $A \in \Gamma$ (only integers that are norms in $\mathcal{O}_{7}$ occur). For example, the first five numbers that occur as depths of elements in the Picard group $\Gamma$ are 1, 2, 4, 7, 11.

If there exists an element of a given depth, then there exist infinitely many, since preor post-composition with any element of $\Gamma_{\infty}$ does not change the height. However, in a fixed bounded region of the Heisenberg group $\mathbb{C} \times \mathbb{R} \simeq \partial_{\infty} H_{\mathbb{C}}^{2} \backslash\{\infty\}$, there are only finitely many points of a given depth. This is true in particular in our fundamental domain $P$ for the action of $\Gamma_{\infty}$. A list of $\mathbb{K}$-rational points of small depth in $P$ is given in [8].

The following result is a consequence of the covering depth estimate given in [8].
Theorem 3.1. The isometric spheres of elements of depth $\geq 11$ do not intersect the ford domain $F_{\Gamma}$.

Remark 3.1. It turns out that the isometric spheres of the elements of depth 7 do intersect the Ford domain, but in lower-dimensional facets only, i.e. they are not needed in the definition (2.1). This fact is quite painful to prove however, and we will not use it in the sequel.

We will also use the following list of 14 elements in the group, which is a slight modification of the list given in [8] (we want the set of side pairing maps to be closed under
inversion of matrices).
$$\begin{gathered}
A_{1}=\left(\begin{array}{ccc}
0 & 0 & 1 \\
0 & -1 & 0 \\
1 & 0 & 0
\end{array}\right), \quad A_{2}=\left(\begin{array}{ccc}
2 & -\tau & 1-3 \tau \\
\bar{\tau} & 0 & -2-\tau \\
-\tau & -1 & -3+\tau
\end{array}\right), \quad A_{3}=A_{2}^{-1}, \quad A_{4}=A_{2}^{-2}, \quad A_{5}=A_{4}^{-1} \\
A_{6}=\left(\begin{array}{ccc}
i \sqrt{7} & 0 & 4 \\
0 & 1 & 0 \\
2 & 0 & -i \sqrt{7}
\end{array}\right), \quad A_{7}=\left(\begin{array}{ccc}
-\bar{\tau} & 1 & 1 \\
\tau & 0 & 1 \\
2 & \bar{\tau} & -\tau
\end{array}\right), \quad A_{8}=\left(\begin{array}{ccc}
1 & 2-\tau & -2 \\
-1-\tau & -3 & 1+\tau \\
-2 & -2+\tau & 1
\end{array}\right), \\
A_{9}=\left(\begin{array}{ccc}
-1 & 0 & i \sqrt{7} \\
0 & 1 & 0 \\
i \sqrt{7} & 0 & 6
\end{array}\right), \quad A_{10}=\left(\begin{array}{ccc}
-2 & 0 & i \sqrt{7} \\
0 & 1 & 0 \\
i \sqrt{7} & 0 & 3
\end{array}\right), \quad A_{11}=A_{10}^{-1}, \\
A_{12}=\left(\begin{array}{ccc}
-4 & 0 & 3 i \sqrt{7} \\
0 & 1 & 0 \\
i \sqrt{7} & 0 & 5
\end{array}\right), \quad A_{13}=A_{12}^{-1}, \quad A_{14}=A_{9}^{-1}
\end{gathered}$$

The basic fact we will use from [8] is the following.
Theorem 3.2. Let $\gamma \in \Gamma \backslash \Gamma_{\infty}$ be such that $I(\gamma)$ intersects the Ford domain. Then there exists $\alpha, \beta \in \Gamma_{\infty}$ and $j \in\{1, \ldots, 14\}$ such that $\gamma=\alpha A_{j} \beta^{-1}$.

The remaining difficulty is that $\Gamma_{\infty}$ is an infinite group, and we cannot check infinitely many inequalities with a computer; we now explain how to handle this difficulty.

In sections 3.1 through 3.4, we sketch the general algorithms to solve the problems announced in the introduction. We then list the specific results (conjugacy classes of torsion elements, maximal finite subgroups) for the group $U\left(J, \mathcal{O}_{7}\right)$ in section 4.
3.1. Basic algorithms. Recall that we are after algorithmic methods stated in 3.1. Let us assume $x \in \mathbb{C}^{3}$ has algebraic coordinates, and $\|x\|^{2}<0$. We can compute the (algebraic) horospherical coordinates $(z, t, u)$ of $x$, using
$$z=\frac{x_{2}}{x_{3}}, i t-u=2 \frac{x_{1}}{x_{3}}+\left|\frac{x_{2}}{x_{3}}\right|^{2} .$$
We would like to find a cusp element $\gamma \in \Gamma_{\infty}$ such that $\gamma(x)$ has horospherical coordinates $\left(z^{\prime}, t^{\prime}, u^{\prime}\right)$ with $\left(z^{\prime}, t^{\prime}\right) \in P$. Recall that $P \subset \mathbb{C} \times \mathbb{R}$ is $T \times[0,2 \sqrt{7}]$ where $T$ is the convex hull of 0, 1 and $\tau$.

First solve
$$a+b \tau=z \leftrightarrow\left\{\begin{array}{l}
a+\frac{b}{2}=\operatorname{Re}(z) \\
b \sqrt{7}=\operatorname{Im}(z)
\end{array}\right.$$
for real algebraic $a, b$, and compute the floors $k=\lfloor a\rfloor$ and $l=\lfloor b\rfloor, \epsilon=\lfloor a+b\rfloor$. By applying $T_{1}^{-k} T_{\tau}^{-l}$, we may assume the horospherical coordinates $(z, t, u)$ satisfy $z \in T$. Computing $\lfloor t /(2 \sqrt{7})\rfloor$, we get a power of $T_{v}$ that brings the $t$-coordinate in $[0,2 \sqrt{7}]$.

In other words, we may assume that $(z, t) \in P$. Now we use the following.
Proposition 3.3. Let $j \in\{1, \ldots, 14\}$. There is an explicit set $T_{j} \subset \Gamma_{\infty}$ such that for all $\gamma \in \Gamma_{\infty} \backslash T_{j}$, we have $\gamma\left(I\left(A_{j}\right)\right) \cap C_{P}=\emptyset$.

Without the "explicit" request, this is a consequence of discreteness of $\Gamma_{\infty}$. The explicit character follows from elementary estimates using the values of the Cygan radius of $I\left(A_{j}\right)$.

Using Proposition 3.3, we can list all the isometric spheres $\alpha\left(I\left(A_{j}\right)\right)$ that contain $[x]$ (or such that $[x]$ is in the interior of the corresponding Cygan ball). This gives method (1).

For method (2), we first proceed as above to bring the Heisenberg coordinate to $P$, then find the Cygan spheres $\alpha\left(I\left(A_{j}\right)\right)$ that contain $x$, and apply the isometry $\left(\alpha A_{j}\right)^{-1}$ to $x$. This decreases the number of Cygan balls defining the Ford domain that contain $[x]$ in their interior. Then repeat the preceding procedure until that number is 0.
3.2. Conjugacy classes of torsion elements. Clear every torsion element is conjuage to a torsion element that fixes a point in the fundamental domain $\Omega F_{\Gamma} \cap C_{P}$. Moreover, there is a precisely invariant horoball centered at the point at infinity, so there are actually finitely many torsion elements fixing a point in $\Omega$; we now explain a method for listing these elements.

Suppose $\gamma \in \Gamma$ has finite order. There are two possibilities, either $\gamma \in \Gamma_{\infty}$ or not.
3.2.1. $\gamma \in \Gamma_{\infty}$. In this case, $\gamma$ must be a complex reflection, and we may assume that its mirror meets the Heisenberg group $\mathbb{C} \times \mathbb{R}$ in a vertical line that intersects the boundary of the prism $P$. Projecting to the $\mathbb{C}$-factor, it is easy to see that the boundary at infinity of the mirror is given by $\left\{\left(z_{0}, t\right): t \in \mathbb{R}\right\}$ for $z_{0}=0,1 / 2, \tau / 2,(1+\tau) / 2$. This implies that $\gamma$ has one of the following forms:
$$R T_{v}^{k}, \quad T_{1} R T_{v}^{k}, \quad T_{\tau} R T_{v}^{k}, \quad T_{1} T_{\tau} R T_{v}^{k},$$
for some $k \in \mathbb{Z}$ (we will give more details about this in section 4.1). The only complex reflections of this form are
$$R, T_{1} R, T_{1} T_{\tau} R .$$
3.2.2. $\gamma \notin \Gamma_{\infty}$. Suppose $\gamma$ fixes a point $[x] \in P$. It is easy to see from the definition of isometric spheres that we must have $[x] \in I(\gamma) \cap I\left(\gamma^{-1}\right)$, and in particular
$$I(\gamma) \cap I\left(\gamma^{-1}\right) \neq \emptyset .$$

Also, because the fixed point $[x]$ is in the Ford domain, is $I(\gamma)$ must have depth $\leq 7$, so $\gamma=\alpha A_{j} \beta^{-1}$ for some $j \in\{1, \ldots, 14\}$ and $\alpha, \beta \in \Gamma_{\infty}$ (see Theorem 3.2).

Since we only want to list torsion elements up to conjugacy, we may assume $\beta=I d$, i.e. $\gamma=\alpha A_{j}$, and we get
$$\emptyset \neq I(\gamma) \cap I\left(\gamma^{-1}\right)=\alpha\left(I\left(A_{j}\right)\right) \cap I\left(A_{j}^{-1}\right) .$$
Note that we chose the set $\left\{A_{1}, \ldots, A_{14}\right\}$ to be invariant under the operation of taking inverses, so there is a $k \in\{1, \ldots, 14\}$ such that $I\left(A_{j}^{-1}\right)=I\left(A_{k}\right)$, and we must have
$$\alpha\left(I\left(A_{j}\right)\right) \cap A_{k} \neq \emptyset .$$

Proposition 3.4. There is an explicit finite set $T_{j k}$ such that for all $\alpha \in \Gamma_{\infty} \backslash T_{j k}$, $\alpha\left(I\left(A_{j}\right)\right) \cap A_{k}=\emptyset$.

The set can be made explicit by using elementary estimates using the triangle inequality and the known radii of the Cygan spheres $I\left(A_{j}\right), I\left(A_{k}\right)$ (see equation (5)).

From this, we get that every torsion element in $\Gamma \backslash \Gamma_{\infty}$ is conjugate to an element of the finite sets $T_{j k}$ for $j, k \in\{1, \ldots, 14\}$ (and we may restrict to pairs $j, k$ such that $A_{j} A_{k}=I d$ ).

Moreover, given an element $\gamma \in T_{j k}$, there is an algorithm to determine whether $\gamma$ has finite order. Indeed, the eigenvalues of the matrix representative for $\gamma$ (which is unique up to multiplication by $-I d$ ) are algebraic integers, and we can determine whether the are roots of unity by examining their minimal polynomial.

If the eigenvalues are all roots of unity, we can check whether or not the matrix is diagonalizable my computing its minimal polynomial. Hence we have an algorithm to do the following.

Method 3.2. Produce a finite set that contains a representative of every conjugacy class of torsion element in $\Gamma$.

For elements with isolated fixed points, we can use methods of section 3.1, we remove all elements whose fixed point set is not in the fundamental domain $\Omega$, since they must be conjugate to another element in the list.
3.3. Eliminating redundancy. The list obtained by applying the method explained in section 3.2 may have redundancies, in the sense that some elements in the list may be conjugate to each other.

We now explain how to test whether two torsion elements $\gamma_{1}, \gamma_{2}$ are conjugate to each other, assuming that they both have an isolated fixed point. We call $x_{j}$ the isolated fixed point of $\gamma_{j}$; because of the methods of section 3.1, we may assume $x_{1}, x_{2}$ are both in $\Omega$.

Suppose $\gamma_{1}, \gamma_{2}$ are conjugate in $\Gamma$, i.e there exists $\alpha \in \Gamma$ such that $\gamma_{2}=\alpha \gamma_{1} \alpha^{-1}$. Then $\alpha\left(x_{1}\right)=x_{2}$, and in particular
$$\Omega \cap \alpha(\Omega) \neq \emptyset .$$
This implies for some $j \in\{1, \ldots, 14\}, \alpha\left(I\left(A_{j}\right)\right)$ must intersect $P$, and there are finitely many choices of $\alpha$ such that this is the case (as before, this can be made explicit).

Hence we only need to check finitely candidate conjugators $\alpha$ in order to determine whether the two elements are conjugate, making this special case of the conjugation problem solvable.

For pairs of complex reflections, it is more complicated to write a general algorithm to test conjugacy (because the stabilizer of the mirror of one such complex reflection is infinite). In order to treat the special case of $P U\left(J, \mathcal{O}_{7}\right)$, it suffices to use the following two observations
\begin{itemize}
\item[(1)] It two elements are conjugate, then we can find an element that conjugates them by listing all group elements (for instance by listing words in a fixed generating set);
\item[(2)] If two complex reflections have different order, or different Jordan forms, or different square norm for their (primitive) polar vector, then they are not conjugate.
\end{itemize}

For a general group, we are likely to find pairs of elements with the same rough conjugacy invariants (order, Jordan form, square norm of polar vector) but the enumeration of the group fails finding a conjugator (say because we run out of time or memory).
3.4. Finding maximal finite subgroups. In this section, we explain how to determine maximal finite subgroups. We assume that we have applied the methods of section 3 successfully, and that we have a finite list of all torsion elements whose fixed points contain a point in $\Omega$.

The interesting maximal finite subgroups contain an element with an isolated fixed point, since generic points on the mirror of a complex reflection have a cyclic group as their stabilizer, generated by a single complex reflection.

Now take the list of torsion elements with an isolated fixed point in $\Omega$. For each such fixed point $[x]$, we use the methods of section 3.1 to find the list of Ford spheres and sides of $C_{P}$ containing $[x]$.

Now build a graph whose vertex set is in bijection with the set of these isolated fixed points, and join two vertices by a directed edge if there is a side-pairing map sending one to the other (either coming from the Ford domain, or from the prism $P$ ); note that the edges may join a vertex to itself.

The conjugacy classes of maximal finite groups in $\Gamma$ are then given by connected component of this graph (take the image of the obvious representation of the fundamental group of the graph in to $\Gamma$ ).

For concreteness, we work out a couple of explicit examples.
\begin{itemize}
\item[(1)] Consider $M=\left(R T_{1} I T_{1}^{-1}\right)^{2}$ for instance (see the first entry in Table 2). Its isolated fixed point is given by $\left[v_{1}\right]$ where $v_{1}=(-\bar{\tau}, 0,1)$, which has horospherical coordinates $[0, \sqrt{7}, 1]$. This point is on two sides of the cone $C_{P}$ (namely the ones with side-pairing $T_{\tau} R$ and $T_{1} R$ ), as well as on three Ford-Cygan spheres , namely
$$I\left(A_{6}\right), T_{1}\left(I\left(A_{1}\right)\right), T_{1}^{-1} T_{v}\left(I\left(A_{1}\right)\right) .$$
The side-pairing maps associated to these sides are given respectively by
$$A_{6}, T_{1} A_{1} T_{1}^{-1}, T_{1}^{-1} T_{v} A_{1} T_{v}^{-1} T_{1},$$
and each of these elements actually fixes $[v]$.
\end{itemize}

Using the side-pairings coming from $C_{P}$, we find two other points $\left[v_{2}\right],\left[v_{3}\right]$ given $v_{2}=T \tau R v_{1}$ and $v_{3}=T_{1} R v_{1}$. Each is on three Ford-Cygan spheres, that are simply the images of the above three Cygan spheres under $T_{\tau} R$ (or $T_{1} R$ ).

Hence the connected component of the graph containing $\left[v_{1}\right]$ is a triangle as in Figure 4. The stabilizer of $\left[v_{1}\right]$ is generated by $A_{6}, T_{1} A_{1} T_{1}^{-1}, T_{1}^{-1} T_{v} A_{1} T_{v}^{-1} T_{1}$ together with the element
$$\left(T_{1} R\right)^{-1} T_{1} T_{\tau} R T_{\tau} R=R .$$
The linear group generated by $R, A_{6}, T_{1} A_{1} T_{1}^{-1}, T_{1}^{-1} T_{v} A_{1} T_{v}^{-1} T_{1}$ has order 16, and its subgroup of scalar matrices has order 2. In other words, the stabilizer of $\left[v_{1}\right]$ in $\Gamma$ has order 8.
\begin{itemize}
\item[]
\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/1650d7d7-2c89-4c89-a0bb-715787182eea-12.jpg?height=414&width=955&top_left_y=324&top_left_x=571}
\captionsetup{labelformat=empty}
\caption{Figure 4. Cycle graph for the vertex $v_{1}$. We omit the Ford side-pairing maps that fix $v_{2}$ (resp. $v_{3}$ ), since these are simply conjugates of the elements in the label for the loop from $v_{1}$ to itself.}
\end{figure}
It is easy to check (for instance by enumerating the elements in the stabilizer) that the stabilizer contains four complex reflections, two in 1-lines and two in 2-lines. This kind of information is gathered in columns 4 through 6 of Tables 2-6.
\item[(2)] Consider the element $N=\left(T_{\tau} R\right) \cdot T_{1} R\left(T_{1} I\right)^{2} T_{1}^{-1} R T_{1} I T_{1}^{-1} \cdot\left(R T_{\tau}^{-1}\right)$, which is the element of order 6 given in Table 5, conjugated by $T_{\tau} R$ so that its isolated fixed point $[w]$ of $N$ is in $\Omega$.
\end{itemize}

The corresponding point is not on any side of the cone $C_{P}$, but it is on five Ford Cygan spheres, namely
$$I\left(A_{2}\right), I\left(A_{3}\right), R T_{\tau}^{-1}\left(I\left(A_{4}\right)\right), R T_{\tau}^{-1} T_{1}^{-1}\left(I\left(A_{5}\right)\right), T_{\tau}\left(I\left(A_{6}\right)\right) .$$
The point $\left[A_{2}^{-1} w\right]$ is inside the Ford domain, but it is not in the cone $C_{P}$, so we bring it back to the cone by a cusp element. It turns out $T_{\tau} R$ does the job, i.e. $T_{\tau} R A_{2}^{-1} w \in \Omega$. Note that the Cygan sphere for $\left(T_{\tau} R A_{2}^{-1}\right)^{-1}=A_{2} \cdot R T_{\tau}^{-1}$ is of course the same as the one for $A_{2}$, since these two elements differ by pre-composition by a cusp element.

Similar considerations show that (adjusted) side-pairing maps corresponding to the above five Cygan spheres are
$$\begin{gathered}
T_{\tau} R \cdot A_{2}^{-1}, \\
T_{1} T_{\tau} R \cdot A_{3}^{-1}, \\
T_{\tau}^{2} R \cdot\left(T_{\tau} A_{6}^{-1} T_{\tau}^{-1}\right), \\
T_{1} \cdot\left(R T_{\tau}^{-1} A_{4}^{-1} T_{\tau} R\right), \\
T_{1}^{-1} \cdot\left(R T_{\tau}^{-1} T_{1}^{-1} A_{5}^{-1} T_{1} T_{\tau} R\right)
\end{gathered}$$
and all these elements fix $[w]$. In other words, the relevant (connected component of the) cycle graph has a single vertex, and 5 loops.

The above five matrices generate a linear group of order 12, whose projectivization is a cyclic group of order 6. There is a complex reflection in this group, obtained by taking the third power of a generator (see Table 5).

\section*{4. Results}
4.1. Torsion in $\Gamma_{\infty}$. We first consider cusp elements. Suppose $\gamma \in \Gamma_{\infty}$ and $\gamma(\Omega) \cap \Omega \neq \emptyset$. Then $\gamma(P) \cap P \neq \emptyset$. Looking at the first component in Heisenberg space $\mathbb{C} \times \mathbb{R}$, we easily find neighboring triangles in the tiling, which are obtained by applying elements of the form
$$\gamma=T_{1}^{j} T_{\tau}^{k}\left(T_{1} T_{\tau} R\right)^{\epsilon} T_{v}^{l},$$
with $-1, \leq j, k, j+k \leq 1, \epsilon=0$ or 1. A picture of the corresponding tiling is given in Figure 5. For each such element, it is easy to check which values of $l$ give $\gamma(P) \cap P \neq \emptyset$

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/1650d7d7-2c89-4c89-a0bb-715787182eea-13.jpg?height=597&width=598&top_left_y=797&top_left_x=747}
\captionsetup{labelformat=empty}
\caption{Figure 5. Horizontal tiling in Heisenberg space, using coordinates in the $\mathbb{R}$-basis $1, \tau$}
\end{figure}
(in all cases $-1 \leq l \leq 1$ is necessary).
Checking the corresponding elements, we find that the only cusp elements in $T$ are
$$R, T_{1} R T_{1}^{-1}, T_{\tau} R T_{\tau}^{-1}, T_{\tau} R, T_{1} T_{\tau} R,$$
each of order 2.
We will shortly see that $T_{\tau} R$ and $T_{1} T_{\tau} R$ are conjugate in $\Gamma$, but they are not conjugate to $R$. In particular, we have (1) in the following.

Proposition 4.1. Let $\gamma \in \Gamma_{\infty}$.
\begin{itemize}
\item[(1)] If $\gamma$ is a non-trivial torsion element, then it is conjugate in $\Gamma$ to $R$ or to $T \tau R$.
\item[(2)] If $\gamma$ is parabolic but not unipotent, then it is conjugate in $\Gamma$ to $T_{1} R T_{v}^{k}, R T_{v}^{k}$ or $T_{\tau} R T_{v}^{k}$ for some $k \in \mathbb{Z}$.
\end{itemize}

Point (2) follows from the fact that the prism is a fundamental domain for the action of $\Gamma_{\infty}$ in Heisenberg space. Indeed, invariant complex lines for non-unipotent can be assumed to meet the boundary at infinity in one of the four vertical lines $(0, t),\left(\frac{1}{2}, t\right),\left(\frac{\tau}{2}, t\right),\left(\frac{1+\tau}{2}, t\right)$ in Heisenberg. The last to are conjugate in $\Gamma$ (but the first three have distinct conjugacy classes in $\Gamma_{\infty}$ ).

Since our method is not algorithmic for complex reflections, we list the conjugations needed in order to show that there are indeed just two conjugacy classes of complex reflections in $\Gamma$ (both of order 2):
$$\begin{gathered}
\left(T_{1} R\right)^{2} T_{1}^{-1}\left(T_{\tau} R\right)\left(\left(T_{1} R\right)^{2} T_{1}^{-1}\right)^{-1}=I \\
{\left[T_{1}, I\right]\left(T_{\tau} R\right)\left[T_{1}, I\right]^{-1}=T_{1} T_{\tau} R} \\
\left(\begin{array}{ccc}
i \sqrt{7} & 0 & 4 \\
0 & -1 & 0 \\
2 & 0 & -i \sqrt{7}
\end{array}\right)=T_{1} I T_{1}^{-1}(R)\left(T_{1} I T_{1}\right)^{-1} .
\end{gathered}$$
The first two equations show that $T_{\tau} R$ and $T_{1} T_{\tau} R$ are both conjugate to $I$. The left hand side of the last equation is one of the complex reflections produced by listing elements of finite order $\gamma$ with $\Omega \cap \gamma \Omega \neq \emptyset$.
4.2. Conjugacy classes of torsion elements. The results below were of course obtained with the help of a computer (using the methods of section 3), even though we have not yet written a computer program that performs this analysis systematically (for general 1-cusped Picard lattices, say).

For complex reflections, there are precisely two conjugacy classes, liste in Table 1. Note

\begin{table}
\begin{tabular}[t]{|l|l|l|}
\hline Matrix & Polar to mirror $v$ & $\langle v, v\rangle$ \\
\hline $R=\left(\begin{array}{ccc}1 & 0 & 0 \\ 0 & -1 & 0 \\ 0 & 0 & 1\end{array}\right)$ & (0, 1, 0) & 1 \\
\hline $I=\left(\begin{array}{ccc}0 & 0 & 1 \\ 0 & -1 & 0 \\ 1 & 0 & 0\end{array}\right)$ & (1, 0, 1) & 2 \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{TABLE 1. Representatives of conjugacy classes of elements of complex reflections (of order 2) in $P U\left(2,1, \mathcal{O}_{7}\right)$}
\end{table}
that the two classes can be distinguished by the square norm of the primitive vector polar to their mirror. This suggests the following definition.

Definition 4.1. For $j=1,2$, a $j$-line is a complex line polar to a primitive vector $v \in \mathcal{O}_{\mathbb{K}}$ such that $\langle v, v\rangle=j$.

The following result follows from the list of conjugacy classes of complex reflections in $\Gamma$ (see Table 1).

Proposition 4.2. The group $\Gamma$ acts transitively on the set of primitive vectors of square norm 1 (resp. 2) in $\mathcal{O}_{K}^{3}$.

Proof: To each $j$-line ( $j=1$ or 2) polar to $v$, the associated complex reflection is indeed in $U\left(J, \mathcal{O}_{7}\right)$, since it is given by
$$R_{v}(x)=x-2 \frac{\langle x, v\rangle}{\langle v, v\rangle} v,$$
and $\langle v, v\rangle$ divides 2. The transitivity now follows from the fact that there are exactly two conjugacy classes of complex reflections in $\Gamma$. \(\square\)

We list the conjugacy classes of torsion elements with isolated fixed points in Tables 2 through 6. For each class, we give the norm of a primitive vectors representing the fixed point. We also list the order of the stabilizer of the fixed point (obtained with the method explained in section 3.4), as well as the number of 1-lines and 2-lines through that point, see Definition 4.1. Recall that being a 1-line (resp. 2-line) is equivalent to being in the $\Gamma$-orbit of the mirror of $R$ (resp. of $I$ ).

\begin{table}
\begin{tabular}[t]{|l|l|l|l|l|l|}
\hline Matrix & Fixed pt $v$ & $\langle v, v\rangle$ & Stabl & 1-lines & 2-lines \\
\hline $\left(R T_{1} I T_{1}^{-1}\right)^{2}=\left(\begin{array}{ccc}i \sqrt{7} & 0 & 4 \\ 0 & 1 & 0 \\ 2 & 0 & -i \sqrt{7}\end{array}\right)$ & $(-\bar{\tau}, 0,1)$ & -1 & 8 & 2 & 2 \\
\hline $I R=\left(\begin{array}{lll}0 & 0 & 1 \\ 0 & 1 & 0 \\ 1 & 0 & 0\end{array}\right)$ & (-1, 0, 1) & -2 & 4 & 1 & 1 \\
\hline $T_{1}^{2} I\left(T_{1}^{-1} I\right)^{2} T_{1}^{2} I=\left(\begin{array}{ccc}-\bar{\tau} & \tau & 2 \\ \tau & 2 & \bar{\tau} \\ 2 & \bar{\tau} & -\tau\end{array}\right)$ & $(\tau, 1, \bar{\tau})$ & -2 & 8 & 0 & 4 \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{TABLE 2. Representatives of conjugacy classes of elements of order 2 with an isolated fixed point in $P U\left(2,1, \mathcal{O}_{7}\right)$}
\end{table}

\begin{table}
\begin{tabular}[t]{|l|l|l|l|l|l|}
\hline Matrix & Fixed pt $v$ & $\langle v, v\rangle$ & Stabl & 1-lines & 2-lines \\
\hline $T_{1}\left(I T_{1}^{-1}\right)^{2}\left(I T_{1}\right)^{2}=\left(\begin{array}{ccc}-1 & \tau & 1 \\ -\bar{\tau} & 1 & 0 \\ 1 & 0 & 0\end{array}\right)$ & $(\tau, 1,-\tau)$ & -3 & 6 & 0 & 3 \\
\hline $T_{1}^{2}\left(I T_{1}^{-1}\right)^{2}\left(I T_{1}\right)^{2}=\left(\begin{array}{ccc}-1 & -\bar{\tau} & 1 \\ \tau & 1 & 0 \\ 1 & 0 & 0\end{array}\right)$ & $(-\bar{\tau}, 1, \bar{\tau})$ & -3 & 6 & 0 & 3 \\
\hline $\left(R T_{1}\right)^{2} I T_{1} I T_{1}^{-1} R T_{1} I T_{1}^{-1}=\left(\begin{array}{ccc}5 & 0 & -3 i \sqrt{7} \\ 0 & -1 & 0 \\ -i \sqrt{7} & 0 & -4\end{array}\right)$ & $\notin \mathbb{K}^{3}$ & & 6 & 1 & 0 \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 3. Representatives of conjugacy classes of elements of order 3 (isolated fixed point) in $P U\left(2,1, \mathcal{O}_{7}\right)$}
\end{table}

\section*{5. Study of the mirror stabilizers}
5.1. Mirror of $R$. The mirror of $R$ is given by the complex lines in $e_{2}^{\perp}$, so it is quite clear that its stabilizer is isomorphic to $\{ \pm 1\} \times U\left(1,1, \mathcal{O}_{7}\right)$. In terms of our standard

\begin{table}
\begin{tabular}[t]{|l|l|l|l|l|l|}
\hline Matrix & Fixed pt $v$ & $\langle v, v\rangle$ & |Stab| & 1-lines & 2-lines \\
\hline $I T_{1}^{-1} R T_{1}=\left(\begin{array}{ccc}0 & 0 & 1 \\ 0 & 1 & 2 \\ 1 & -2 & -2\end{array}\right)$ & (-1, -1, 1) & -1 & 8 & 2 & 2 \\
\hline $\left(T_{1}^{-1} I\right)^{2}\left(T_{1} I\right)^{2}=\left(\begin{array}{ccc}0 & 0 & 1 \\ 0 & 1 & 1+\bar{\tau} \\ 1 & -1-\tau & -2\end{array}\right)$ & $(\bar{\tau},-\tau,-\bar{\tau})$ & -2 & 8 & 0 & 2+2 \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 4. Representatives of conjugacy classes of elements of order 4 (isolated fixed point) in $P U\left(2,1, \mathcal{O}_{7}\right)$. The occurrence of $2+2$ in the last column means that there are four 2-lines through the fixed point, that come in two distinct orbits under the action of the stabilizer.}
\end{table}

\begin{table}
\begin{tabular}[t]{|l|l|l|l|l|}
\hline Matrix & Fixed pt $v$ & |Stab| & 1-lines & 2-lines \\
\hline $T_{1} R\left(T_{1} I\right)^{2} T_{1}^{-1} R T_{1} I T_{1}^{-1}=\left(\begin{array}{ccc}-5 & 0 & 3 i \sqrt{7} \\ 0 & -1 & 0 \\ i \sqrt{7} & 0 & 4\end{array}\right)$ & $\notin \mathbb{K}^{3}$ & 6 & 1 & 0 \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 5. Representatives of conjugacy classes of elements of order 6 (isolated fixed point) in $P U\left(2,1, \mathcal{O}_{7}\right)$}
\end{table}

\begin{table}
\begin{tabular}[t]{|l|l|l|l|l|}
\hline Matrix & Fixed pt $v$ & Stab & 1-lines & 2-lines \\
\hline $I R T_{1}=\left(\begin{array}{ccc}0 & 0 & 1 \\ 0 & 1 & 1 \\ 1 & -1 & -\bar{\tau}\end{array}\right)$ & $\notin \mathbb{K}^{3}$ & 7 & 0 & 0 \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 6. Representatives of conjugacy classes of elements of order 7 (isolated fixed point) in $P U\left(2,1, \mathcal{O}_{7}\right)$}
\end{table}
horospherical coordinates $(z, t, u)$, the mirror is simply given by the points with $z=0$, i.e. we get a copy of the upper half space $(t, u) \in \mathbb{R}^{2}, u>0$.

The stabilizer can be understood with the same method as in [8], only the computations are simpler. Concretely, to work out the Ford domain for the stabilizer, we restrict to $z=0$ and consider the domain bounded by Cygan spheres for elements $\gamma \in \Gamma$ only when $\gamma$ preserves $z=0$ (this last is equivalent to saying that its matrix representative should have (1, 0, 0) as an eigenvector, and it implies that $\gamma(\infty)$ have 0 as its second homogeneous coordinate). Of course there are infinitely many such elements, but up to the action of $\Gamma_{\infty}$, the points $\gamma(\infty)$ must be the ones listed in [8].

Also, the cusp elements that preserve $z=0$ consists precisely of elements in the infinite cyclic group generated by the vertical translation $T_{v}$.

It turns out that, up to the action of the group generated by $T_{v}$, there is a unique element of height 1 , namely
$$I=\left(\begin{array}{ccc}
0 & 0 & 1 \\
0 & -1 & 0 \\
1 & 0 & 0
\end{array}\right),$$
and a unique element of height 2, given by
$$M=\left(\begin{array}{ccc}
i \sqrt{7} & 0 & 4 \\
0 & 1 & 0 \\
2 & 0 & -i \sqrt{7}
\end{array}\right) .$$
Moreover, the corresponding Cygan spheres intersect at the (isolated) fixed point of
$$M T_{v} I,$$
which has order 6 (its cube is actually equal to $R$, so the transformation acts as an element of order 3 in restriction to the mirror of $R$ ).

It follows from the results in [8] that the Cygan spheres of level 11 or bigger do not intersect the Ford domain, so the determination of the Ford domain for the stabilizer is reduced to finitely many verification, and one verifies that the $T v$-translates of the two Cygan spheres for $I$ and $M$ actually bound the domain, and that a fundamental domain for the action of the stabilizer is as illustrated in Figure 6.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/1650d7d7-2c89-4c89-a0bb-715787182eea-17.jpg?height=670&width=410&top_left_y=1298&top_left_x=841}
\captionsetup{labelformat=empty}
\caption{Figure 6. Fundamental domain with side-pairing for the action of the stabilizer of the mirror of $R$.}
\end{figure}

It is also easy to work out the vertex cycles of the corresponding Ford polygon, to get a presentation for the fixed point stabilizer of the form
$$\left\langle\iota, \mu, v \mid \iota^{2}, \mu^{2},(\mu v \iota)^{3}\right\rangle .$$

The stabilizer is a central extension of this group with presentation
$$\left\langle\iota, \mu, v, \rho \mid \iota^{2}, \mu^{2}, \rho^{2},(\mu v \iota)^{3} \rho^{-1},[\rho, \iota],[\rho, \mu],[\rho, v]\right\rangle .$$

The above discussion shows in particular that the mirror stabilizer has precisely three orbits of points with non-trivial isotropy groups, represented by
\begin{itemize}
\item[-] The common fixed point of $I$ and $R$ (intersection of one 1-line and one 2-line)
\item[-] The fixed point of $\left(R T_{1} I T_{1}^{-1}\right)^{2}$ (intersection of two 1-lines and two 2-lines)
\item[-] The fixed point of $M T_{v} I$ (only one 1-line).
\end{itemize}
5.2. Mirror of $I$. Instead of considering the stabilizer of the mirror of $I$, we will study the mirror of $T_{\tau} R$ (which is conjugate to $I$ in $\Gamma$ ), because its mirror goes through the point at infinity in the Siegel half space.

Let $L$ be the mirror of $T_{\tau} R$, which is given by $v^{\perp}$ with $v=(1,-\tau, 0)$. The structure of the stabilizer of $L$ in $\Gamma$ is significantly more difficult to study. Our main result is the following.

Theorem 5.1. The projection of the stabilizer of $L$ to $P U(1,1)$ is the lattice generated by seven elements $r_{1}, r_{2}, r_{3}, r_{4}, s_{1}, s_{2}$, with presentation
$$\left\langle r_{1}, r_{2}, r_{3}, r_{4}, s_{1}, s_{2}, s_{3}, t_{v} \mid r_{1}^{2}, r_{2}^{3}, r_{3}^{2}, r_{4}^{2},\left(s_{2}^{-1} s_{1}\right)^{2}, s_{1}^{-1} r_{4} r_{1} r_{3} t_{v} r_{2}\right\rangle .$$
This group has precisely two cusps, corresponding to the cyclic groups generated by $t_{v}$ and $s_{2}$. The image of the mirror in the quotient is a $P_{\mathbb{C}}^{1}$ with 2 punctures and 4 orbifold points of weight 2.

Just as in section 5.1, $\operatorname{Stab}(L)$ is in fact a central extension of this group, with center generated by the complex reflection $T_{\tau} R$ itself (which acts trivially on $L$ ).

We obtained this group by using the computer to list many primitive vectors $v \in \mathcal{O}_{\mathbb{K}}^{3}$ with norm 1 or 2, and keeping only those that are orthogonal to $v=(1,-\tau, 0)$ (so that the corresponding complex reflections $R_{v}$ preserves $L$ ). We then studied the Ford domain (see Figure 7) for the group generated by those reflections, whose side-pairing maps are the above generators.

The group elements $r_{1}, \ldots, r_{4}$ are complex reflections of type 2. We describe them by giving vectors $v_{1}, \ldots, v_{4}$ polar to their mirror, recall that the matrix of the reflection $R_{v}$ fixing $v^{\perp}$ can be obtained by using the formula (7).
$$\begin{gathered}
v_{1}=(1,1, \bar{\tau}) \\
v_{2}=(-i \sqrt{7}, \tau, 2) \\
v_{3}=(i \sqrt{7}, \tau, 2) \\
v_{4}=(0,1, \bar{\tau}) .
\end{gathered}$$
For the other two, we give the full matrices, namely
$$s_{1}=\left(\begin{array}{ccc}
-\tau-1 & \tau-2 & \bar{\tau}+2 \\
3 \tau & 4 & -5 \\
6 & 3 \bar{\tau} & 5 \tau-4
\end{array}\right), \quad s_{2}=\left(\begin{array}{ccc}
\tau-3 & i \sqrt{7} & -i \sqrt{7} \\
\bar{\tau}+3 & 1-i \sqrt{7} & i \sqrt{7} \\
-2 i \sqrt{7} & -\tau-3 & \tau+4
\end{array}\right) .$$

It is easy to check that $s_{2}$ is a parabolic element, and whose fixed point is represented by the primitive vector $(-1,1, \bar{\tau})$.

A fundamental domain for the action of the stabilizer of $L$ is described in Figure 7. From this, one easily deduces a presentation of the stabilizer of $L$ (modulo the fixed point stabilizer of $L$, which is a group of order 2), by using the Poincaré polygon theorem. Indeed, the relations that occur in the presentation of equation (8) are the cycle relations coming from the vertices of the fundamental domain.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/1650d7d7-2c89-4c89-a0bb-715787182eea-19.jpg?height=794&width=1095&top_left_y=694&top_left_x=498}
\captionsetup{labelformat=empty}
\caption{Figure 7. A fundamental domain for the action in $L$ of $\operatorname{Stab}(L)$.}
\end{figure}

A priori the above group is only the subgroup of $\operatorname{Stab}(L)$ generated by all the complex reflections in $\operatorname{Stab}(L)$, but it is in fact the full stabilizer, because any holomorphic symmetry of our domain would have to exchange the two cusps (but it is easy to see that there is no $A \in U\left(2,1, \mathcal{O}_{7}\right)$ that exchanges $(1,0,0)$ and $\left.(-1,1, \bar{\tau})\right)$.

\section*{6. A 2-generator presentation}

Theorem 6.1. The group $\Gamma_{7}=P U\left(2,1, \mathcal{O}_{7}\right)$ has the following presentation $\left\langle a, b, c, d \mid a^{7}, b^{2}, c^{6},\left(a d^{2}\right)^{4},\left(c^{-2} d^{2}\right)^{4},\left(c d^{-1} c^{2} d^{-2}\right)^{3},\left(c d^{-2} c^{2} d^{-1}\right)^{3},\left(d^{2} c^{-1} a^{-2} d^{3} c^{2} a^{-2}\right)^{2}, c^{-1} a b, d^{-1} b a\right\rangle$ Moreover, every torsion element in the group is conjugate to an element that occurs in a power relator.

Note that we write this as a 4-generator presentation to help readability, but it should be clear (by looking at the last two relators) that $a, b$ generate the group, and this can clearly be turned into a 2-generator presentation (this is useful to speed up computations using group-theory software like GAP or Magma).

\begin{table}
\begin{tabular}[t]{|l|l|l|l|l|}
\hline Order & Group element & Fixed point $v$ & $\langle v, v\rangle$ & Other descr. \\
\hline 2 & $b$ & ( $1,-\tau, 0$ ) & 2 & $T_{\tau} R$ \\
\hline 2 & $(b a)^{3}=d^{3}=a^{-1} c^{3} a$ & ( $\tau, 0,1$ ) & 1 & $T_{1} I T_{1}^{-1} R T_{1} I T_{1}^{-1}$ \\
\hline 2 & $\left((a b a)^{-1} b a b a b\right)^{2}=\left(d^{-2} c^{2}\right)^{2}$ & $(\tau, 1, \bar{\tau})$ & -2 & \#3 \\
\hline 2 & $(a b a b a)^{2}=\left(a d^{2}\right)^{2}$ & $(\tau+1,1, \bar{\tau})$ & -1 & $A_{2}(\# 1) A_{2}^{-1}$ \\
\hline 3 & $(b a)^{2}=d^{2}$ & not in $\mathbb{Q}(i \sqrt{7})$ & & $T_{1}\left(I T_{1}^{-1} R\right)^{3}$ \\
\hline 3 & $\left[b, a^{-1} b a b a b\right]=c^{-1} d^{2} c^{-2} d$ & $(3+i \sqrt{7}, 1, \bar{\tau})$ & -3 & $T_{v} I\left(T_{\tau} J\right) I T v^{-1}$ \\
\hline 4 & $(a b a)^{-1} b a b a b=d^{-2} c^{2}$ & $(\tau, 1, \bar{\tau})$ & -2 & $I T_{1}^{-1}\left(I T_{1}\right)^{2} I T_{1}^{-1}$ \\
\hline 4 & $a b a b a=a d$ & $(\tau+1,1, \bar{\tau})$ & -1 & $T_{1} I\left(T_{1}^{-1} I\right)^{2} T_{1} I R T_{1} I T_{1}^{-1}$ \\
\hline 6 & $a b=c$ & not in $\mathbb{Q}(i \sqrt{7})$ & & $R T_{1} I R\left(T_{1} I\right)^{2} T_{1}^{-2}$ \\
\hline 7 & $a$ & not in $\mathbb{Q}(i \sqrt{7})$ & & $T_{1} R T_{1} I R T_{1} I$ \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Figure 8. Obvious elements of finite order, obtained from the presentation (6.1).}
\end{table}

\begin{table}
\begin{tabular}[t]{|l|l|l|l|l|}
\hline Order & Group element & Fixed point $v$ & $\langle v, v\rangle$ & Other descr. \\
\hline 2 & $(a b a)^{-1}\left(d^{2} c^{-1} a^{-2} d^{3} c^{2} a^{-2}\right) a b a$ & (1, 0, -1) & -2 & $J=R I$ \\
\hline 3 & $a^{-1} b a^{-1} b a b a b a^{-1} b a b=d^{-2} c^{2} d^{-1} c$ & $(\tau+1, \bar{\tau},-\tau)$ & -3 & $T_{1} I\left(T_{\bar{\tau}}^{-1} J\right) I T_{1}^{-1}$ \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Figure 9. Non-obvious elements of finite order.}
\end{table}

An explicit isomorphism $\phi: G \rightarrow P U\left(2,1, \mathcal{O}_{7}\right)$ extends $\phi(a)=A, \phi(b)=B$ where
$$A=\left(\begin{array}{ccc}
-\tau-2 & i \sqrt{7} & i \sqrt{7} \\
-1 & 1 & 0 \\
\tau-1 & 1 & 1
\end{array}\right), \quad B=\left(\begin{array}{ccc}
1 & \bar{\tau} & -1 \\
0 & -1 & \tau \\
0 & 0 & 1
\end{array}\right) .$$

The fact that $\phi(a)=A, \phi(b)=B$ extends to a group homomorphism (still denoted by $\phi$ ) follows from explicit matrix computation. The fact that this extension is an isomorphism follows from comparison of $G$ with the presentation for $P U\left(2,1, \mathcal{O}_{7}\right)$ given in [8] using the SearchForIsomorphism command in Magma.

We would like to find an element of each torsion conjugacy class expressed as explicit words in $a, b$. We start by gathering geometric data for the obvious elements that occur in the presentation in equation (6.1), see Table 8. In order to get all torsion conjugacy classes (up to replacing any element to a power that generates the same finite cyclic group), we need to write a conjugate of $I R$ and a conjugate of $T_{\bar{\tau}}^{-1} J$ as explicit words in $a$ and $b$. This can be done using the above explicit isomorphism between the presentations (or alternatively by geometric methods using a suitable Dirichlet domain for the group).

The results are give in Table 9.

\section*{7. Torsion-free subgroups}

We now use the results of the previous sections to exhibit an explicit torsion-free subgroup of $\Gamma$. Recall that $\Gamma$ contains elements of order 2, 3, 4, 6 and 7, so the index of any torsion-free subgroup has to be a multiple of $\operatorname{lcm}(\{4,6,7\})=84$.

Consider the ideal $I=\langle i \sqrt{7}\rangle$ in $\mathcal{O}_{\mathbb{K}}$, that satisfies $\mathcal{O}_{\mathbb{K}} / I \equiv \mathbb{F}_{7}$, and let $\phi: \Gamma \rightarrow G L\left(3, \mathbb{F}_{7}\right)$ be the corresponding homomorphism (reduce all coefficients modulo $I$ ). We use the matrices $A$ and $B$ from section 6, and compute
$$\phi(A)=\left(\begin{array}{ccc}
1 & 0 & 0 \\
-1 & 1 & 0 \\
3 & 1 & 1
\end{array}\right), \quad \phi(B)=\left(\begin{array}{ccc}
1 & 4 & -1 \\
0 & -1 & 4 \\
0 & 0 & 1
\end{array}\right) .$$

Proposition 7.1. The group $\Gamma_{0}=\operatorname{Ker}(\phi)$ is a torsion-free subgroup of index 336 in $\Gamma$, which is torsion-free at infinity as well.

Proof: It is easy to verify that the subgroup generated by $\phi(A)$ and $\phi(B)$ has order 336 (this is most conveniently done with group theory software, say GAP or Magma), which gives the statement about the index.

The claim about $\Gamma_{0}$ being torsion-free amounts to verifying that every representative $\gamma$ of a conjugacy class of torsion elements has the property that $\phi(\gamma)$ has the same order as $\gamma$.

The claim about $\Gamma_{0}$ being torsion-free at infinity is equivalent to checking that $\phi\left(T_{1} R\right) \phi\left(T_{v}\right)^{k}$ is non-trivial for every $k$. In fact $\phi\left(T_{v}\right)$ has order 4, so it it enough to check this for $k=0,1,2,3$.

All these verifications are checked by direct computations in $G L\left(3, \mathbb{F}_{7}\right)$. \(\square\)

Remark 7.1. (1) Applying the same construction, but replacing $I$ by the ideal $I^{\prime}=\langle\tau\rangle$ (which satisfies $\mathcal{O}_{\mathbb{K}} / I^{\prime} \equiv \mathbb{F}_{2}$ ) gives a subgroup of index 168, which is not torsion-free.
\begin{itemize}
\item[(2)] Using Magma, one can check that $\Gamma$ has exactly two normal subgroups of index 336, and only one of them is torsion-free.
\item[(3)] The group of order $336 G=\operatorname{Im}(\phi)$ is not isomorphic to the Shephard-Todd $G_{24}$ that was used in [2]. In fact $G$ has trivial center, whereas $G_{24}$ has center order 2.
\end{itemize}

\section*{References}
\begin{itemize}
\item[] [1] Martin Deraux. A 1-parameter family of spherical CR uniformizations of the figure eight knot complement. Geom. Topol., 20(6):3571-3621, 2016.
\item[] [2] Martin Deraux. Non-arithmetic lattices and the Klein quartic. J. Reine Angew. Math., 754:253-279, 2019.
\item[] [3] Elisha Falbel, Gábor Francsics, and John R. Parker. The geometry of the Gauss-Picard modular group. Math. Ann., 349(2):459-508, 2011.
\item[] [4] Elisha Falbel and John R. Parker. The geometry of the Eisenstein-Picard modular group. Duke Math. J., 131(2):249-289, 2006.
\item[] [5] Mahboubeh Ghoshouni and Majid Heydarpour. A Set of Generators for the Picard Modular Group in the Case $\mathrm{d}=11$. Iran J. Sci. Technol. Trans. Sci., 44:1469-1475, 2020.
\item[] [6] Mahboubeh Ghoshouni and Majid Heydarpour. A set of generators for the Picard modular group $\operatorname{SU}\left(2,1, \mathcal{O}_{2}\right)$. Proc. Indian Acad. Sci., Math. Sci., 130(26), 2020.
\item[] [7] James E. Humphreys. Arithmetic groups, volume 789 of Lect. Notes Math. Springer, 1980.
\item[] [8] Alice Mark and Julien Paupert. Presentations for cusped arithmetic hyperbolic lattices. https://arxiv.org/abs/1709.06691.
\item[] [9] John R. Parker and Pierre Will. A complex hyperbolic Riley slice. Geom. Topol., 21(6):3391-3451, 2017.
\end{itemize}
[10] Julien Paupert and Pierre Will. Real reflections, commutators, and cross-ratios in complex hyperbolic space. Groups Geom. Dyn., 11(1):311-352, 2017.
[11] David Polletta. Presentations for the Euclidean Picard modular groups. Geom. Dedicata, 210:1-26, 2021.
[12] Matthew Stover. Cusps of Picard modular surfaces. Geom. Dedicata, 157:239-257, 2012.
[13] Tiehong Zhao. Generators for the Euclidean Picard modular groups. Trans. Am. Math. Soc., 364(6):3241-3263, 2012.
[14] Thomas Zink. über die Anzahl der Spitzen einiger arithmetischer Untergruppen unitärer Gruppen. Math. Nachr., 89:315-320, 1979.
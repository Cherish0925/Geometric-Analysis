---
retention_scope: session
part: 1
total_parts: 3
---

[Part 1/3 of: An analogue of the Gibbons-Hawking Ansatz for quaternionic Kähler spaces]

---
source_file: 1901_11166.pdf
converter: mathpix
format: mmd
---

\title{
AN ANALOGUE OF THE GIBBONS-HAWKING ANSATZ FOR QUATERNIONIC KÄHLER SPACES
}

\author{
RADU A. IONAŞ
}

\begin{abstract}
We show that the geometry of $4 n$-dimensional quaternionic Kähler spaces with a locally free $\mathbb{R}^{n+1}$-action admits a Gibbons-Hawking-like description based on the Galicki-Lawson notion of quaternionic Kähler moment map. This generalizes to higher dimensions a four-dimensional construction, due to Calderbank and Pedersen, of self-dual Einstein manifolds with two linearly independent commuting Killing vector fields. As an application, we use this new Ansatz to give an explicit equivariant completion of the twistor space construction of the local c-map proposed by Roček, Vafa and Vandoren.
\end{abstract}

\section*{Contents}
0 Introduction ..... 2
1 Hyperkähler vs. quaternionic Kähler geometry ..... 5
1.1 General aspects ..... 5
1.2 Killing vector fields ..... 11
1.3 Homothetic Euler vector fields ..... 17
2 Swann bundles ..... 19
2.1 Two structures on the group $\mathbb{H}^{\times} / \mathbb{Z}_{2}$ ..... 19
2.2 The Swann bundle of a quaternion Kähler manifold ..... 21
3 Analogue of the extended Gibbons-Hawking Ansatz for quaternionic Kähler metrics ..... 25
3.1 The extended Gibbons-Hawking Ansatz ..... 25
3.2 Extended Gibbons-Hawking spaces with a hyperkähler cone structure ..... 27
3.3 The space $\operatorname{Im} \mathbb{H P}^{n}$ ..... 31
3.4 The reduction ..... 35
3.5 The quaternionic Kähler Ansatz ..... 40
3.6 The case of four dimensions ..... 42
4 Hyperkähler cones via the Legendre transform construction ..... 44
4.1 The Legendre transform construction ..... 44
4.2 Hyperkähler cone structure conditions ..... 45
5 An example: the local c-map ..... 47
References ..... 57

\section*{0. Introduction}

The Gibbons-Hawking Ansatz [27] is a method of constructing four-dimensional hyperkähler spaces with a tri-Hamiltonian locally free $\mathbb{R}$-action in terms of the solutions of a Bogomolny-type differential equation whose consistency condition is a Laplace equation. It is one of the fundamental constructions in hyperkähler geometry, with vast applications ranging from the construction of gravitational instantons to serving as an asymptotic model or some other type of limit for various geometries and moduli spaces. The original method of Gibbons and Hawking was generalized in [41] by Pedersen and Poon to $4 n$-dimensional hyperkähler spaces with a tri-Hamiltonian locally free $\mathbb{R}^{n}$-action; in what follows we will refer to such spaces as extended Gibbons-Hawking spaces. A key feature of these constructions is the fact that the rank of the action is such that the $n$ orbit parameters of the action together with the $3 n$ components of its associated hyperkähler moment map provide a complete set of coordinates for the hyperkähler space. Geometrically, the hyperkähler structure is defined on the total space of an $\mathbb{R}^{n}$-bundle over an open subset of the space $\mathbb{R}^{n} \otimes \mathbb{R}^{3}$, where it is given explicitly in terms of a Higgs field and $\mathbb{R}^{n}$-connection 1-form satisfying a generalized form of the Bogomolny equation. This construction is general: any $4 n$-dimensional hyperkähler space with a locally free tri-Hamiltonian $\mathbb{R}^{n}$-action can be proven to arise locally in this way.

In this paper we show that a close analogue of this Ansatz exists as well in quaternionic Kähler setting. Recall that hyperkähler and quaternionic Kähler manifolds are $4 n$-dimensional Riemannian manifolds with the holonomy groups of their Levi-Civita connections given by $S p(n)$ and $S p(n) \times_{\mathbb{Z}_{2}} S p(1)$, respectively, or subgroups thereof (here, we extend these definitions to include the pseudo-Riemannian variants of these geometries resulting from replacing the unitary quaternionic group $\operatorname{Sp}(n)$ with any one of its noncompact versions; also, for $n=1$, the holonomy definition is rather too unrestrictive in the quaternionic Kähler case, and one usually discards it: the natural analogues of quaternionic Kähler manifolds in four dimensions are self-dual Einstein manifolds). Both types of geometries are Einstein. Hyperkähler geometry, however, is essentially distinguished from more general quaternionic Kähler one by having zero scalar curvature. This distinction notwithstanding, in specific circumstances it is nonetheless useful to think of the former as the zero scalar curvature limit of the latter. Another, less obvious way in which the two geometries are related was discovered by Swann, who showed in [46] that over any quaternionic Kähler manifold one can construct a quaternionic bundle with fiber $\mathbb{H}^{\times} / \mathbb{Z}_{2}$, where $\mathbb{H}^{\times}$denotes the multiplicative group of non-zero quaternions, the total space of which carries a natural hyperkähler structure as well as a homothetic vector field: that is to say, a hyperkähler cone structure. The power of Swann's result resides in its transformative potential: it gives a canonical way to radically reformulate a quaternionic Kähler geometry problem as a hyperkähler geometry one.

And this is precisely the path that we take in our search for a quaternionic Kähler analogue of the extended Gibbons-Hawking Ansatz: rather than ask the question directly about quaternionic Kähler spaces, we ask instead the corresponding question about hyperkähler cones. Namely, we ask under what conditions an extended Gibbons-Hawking space possesses a hyperkähler cone structure. For any extended Gibbons-Hawking space of real dimension $4 n+4$ (this dimension is chosen for later convenience), the base of its $\mathbb{R}^{n+1}$-fibration is, as we have stated above, an open subset of the space $\mathbb{R}^{n+1} \otimes \mathbb{R}^{3}$, which can be viewed as the space of configurations of $n+1$ distinguishable points in $\mathbb{R}^{3}$. On this
space, one can always define a natural quaternionic action by considering the rigid rotations and simultaneous scalings of such configurations which leave a given point, say, the origin, fixed. These transformations form indeed a quaternionic group since $S O(3) \otimes \mathbb{R}^{+} \cong \mathbb{H}^{\times} / \mathbb{Z}_{2}$. So then, a more specific interrogation would be when can this $\mathbb{H}^{\times} / \mathbb{Z}_{2}$-action on the base of the $\mathbb{R}^{n+1}$-fibration be lifted to a genuine hyperkähler cone structure on the total space, that is, on the extended Gibbons-Hawking space? This question is answered in Proposition 14, which states that a necessary and sufficient condition for that to happen is for the Higgs field of the extended Gibbons-Hawking space to be invariant at rigid rotations and scale with a certain weight under simultaneous scalings of the configurations. What remains now is to match this description of the hyperkähler cone, in which the $\mathbb{R}^{n+1}$-bundle structure is manifest, to the Swann description, centered instead on the $\mathbb{H}^{\times} / \mathbb{Z}_{2}$-bundle structure. This is facilitated by a certain condensed quaternionic reformulation of the extended Gibbons-Hawking formulas that we introduce in §3.1.3. It ultimately yields an explicit description of the geometry of the base of the Swann bundle, which is in this case a $4 n$-dimensional quaternionic Kähler geometry with an inherited locally free isometric $\mathbb{R}^{n+1}$-action.

The emerging picture is summarized in intrinsic terms in subsection 3.5. Its main features are as follows: The quaternionic Kähler structure is defined on the total space of an $\mathbb{R}^{n+1}$-bundle over the space of inequivalent (with respect to rigid rotations and simultaneous scalings) non-degenerate configurations of distinguishable $n+1$ points in $\mathbb{R}^{3}$, which we denote by $\operatorname{Im} \mathbb{H P}^{n}$ (and define precisely in subsection 3.3). A natural set of coordinates is given by the orbit parameters of the $\mathbb{R}^{n+1}$-action together with this action's associated Galicki-Lawson-type moment maps, multiplied by a scale. The latter can also be understood as inhomogeneous local coordinates on $\operatorname{Im} \mathbb{H P}^{n}$. The quaternionic Kähler metric, 2-forms and $S O(3)$ connection 1-forms are given explicitly in these coordinates in terms of a reduced Higgs field and $\mathbb{R}^{n+1}$-connection 1-form satisfying a set of partial differential equations on $\operatorname{Im} \mathbb{H P}^{n}$ similar to the Bogomolny equations from the hyperkähler case. These field equations admit also a dual formulation, a remarkable consequence of which is that the local quaternionic Kähler structure turns out to be completely determined by a single real-valued function on $\operatorname{Im} \mathbb{H P}^{n}$ satisfying a set of linear partial differential constraints. This function is closely related to the hyperkähler potential of the Swann bundle. (Swann bundles have the distinctive feature among hyperkähler spaces that all three elements of a defining triplet of 2-forms-see e.g. Theorem 2-can be derived, as Kähler forms with respect to their corresponding complex structures, from the same Kähler potential.) Very importantly, like in the hyperkähler case, this picture is general: any $4 n$-dimensional quaternionic Kähler space with a locally free isometric $\mathbb{R}^{n+1}$-action arises locally in this way.

The main body of the paper is organized into five sections. In section 1 we give a non-Riemannian characterization of both hyperkähler and quaternionic Kähler manifolds, in a spirit similar to that of exterior differential systems [12]. That is, in each case we formulate a criterion in which the metric is not among the fundamental objects defining the geometry but, rather, is a derived, composite object. The building blocks of either geometry may be considered instead to be triplets of non-degenerate and pointwise linearly independent 2-forms: globally defined in the hyperkähler case, and locally defined in the quaternionic Kähler one. Such a triplet is required to satisfy two conditions: an algebraic condition, and an exterior differential one (Theorems 2 and 3). In the hyperkähler case the latter condition is due to Hitchin [30] and requires that the three 2-forms be symplectic. In the quaternionic Kähler case a corresponding condition was found by Alekseevsky, Bonan and Marchiafava
[2]. These conditions do not constrain the triplets uniquely. In the hyperkähler case one has in fact a half 3-sphere's worth of equivalent triplets to choose from (the triplets can be rotated by $S O(3)$ transformations, whose group manifold is topologically $S^{3} / \mathbb{Z}_{2}$ ). In the quaternionic Kähler case, on the other hand, one regards the triplets as local frames for an $S O(3)$-bundle. The proofs we give to these criterions are new; we base them in both cases on the successive application of two key identities, which we collect together in Lemma 1. We show also that Alekseevsky et al.'s condition can be equivalently replaced by a Hermitian-Einstein-type condition for the curvature 2-form of the associated principal $S O(3)$-bundle, which takes as well the form of an exterior differential condition. This gives us the very useful equivalent quaternionic Kähler criterion of Theorem 4. In the remainder of the section we describe how certain symmetry conditions-namely, the Killing condition and what we call the homothetic Euler condition, which is the basic symmetry of hyperkähler cones - fit into this framework. In spite of the perhaps unusual point of view, the material discussed in this preliminary section is for the most part known, and readers accustomed to the basic concepts of hyperkähler and quaternionic Kähler geometry and interested mainly in the headline subject of the paper can safely skip ahead, to return maybe only for occasional references.

In section 2 we review in detail Swann's quaternionic bundle construction. We clarify among other things the role of the hypercomplex structures on the quaternionic fiber, and review how Killing symmetries fit into this picture as well.

In section 3, after many preparations, we finally address in full force the issue of finding a quaternionic Kähler analogue of the extended Gibbons-Hawking Ansatz, following the strategy exposed above. In the last part of the section we then specialize to four dimensions (i.e. $n=1$ ). The space $\operatorname{Im} \mathbb{H P}^{1}$ is isomorphic to the complex upper half-plane, and we find that our formulas yield in this case precisely the description given by Calderbank and Pedersen in [13] to the four-dimensional avatars of the quaternionic Kähler spaces we consider, which are self-dual Einstein spaces with two linearly independent commuting Killing vector fields. In this sense, therefore, our results can be thought of as a natural higher-dimensional generalization of those of Calderbank and Pedersen.

In section 4 we translate the description of hyperkähler cones from the Gibbons-Hawking-type framework used up until now to the language of the Legendre transform approach of Lindström and Roček [38, 32]. This is useful particularly when one wants to solve the field equations by means of twistor methods.

In section 5, as an application of our newfound Ansatz, we give a thorough and explicit account of the twistor construction of a quaternionic Kähler metric found in [23] by Ferrara and Sabharwal, in connection with the so-called local c-map construction from string theory and supergravity. The twistor approach to this metric was initiated in [43, 44] by Roček, Vafa and Vandoren, and developed further in [40]. The idea is that, if one goes from the Ferrara-Sabharwal space six dimensions higher to the twistor space (in the sense of [32]) of its Swann bundle, there the quaternionic Kähler metric information is encoded in a single-and simple-holomorphic symplectic gluing function. The challenge becomes then to show that the quaternionic Kähler metric can be retrieved from this holomorphic data. In a first stage, by making use of the general methods associated to the Legendre transform approach, one can come down two dimensions from the twistor space and determine from this function the geometry of the Swann bundle. This step has been generally already understood in the literature. The new results of section 3 can then be used to descend a
further four dimensions to retrieve explicitly and in an equivariant manner the Ferrara-Sabharwal metric. This exercise clarifies a number of issues and cements the basis of the twistor-theoretic understanding of this important construction.

\section*{1. Hyperkähler vs. quaternionic Kähler geometry}

\subsection*{1.1. General aspects.}
1.1.1. In Berger's list of special holonomy manifolds, hyperkähler and quaternionic Kähler manifolds are $4 n$-dimensional Riemannian manifolds with the holonomy group of their Levi-Civita connection a subgroup of the unitary quaternionic group $S p(n)$, respectively the group $\operatorname{Sp}(n) \times_{\mathbb{Z}_{2}} \operatorname{Sp}(1) .{ }^{1}$ Here we will distinguish between the two notions and assume, moreover, that hyperkähler manifolds are not subsummed to the quaternionic Kähler ones. There exist also pseudo-Riemannian versions of these manifolds which are obtained by replacing the group $\operatorname{Sp}(n)$ with one of its non-compact versions $\operatorname{Sp}(p, q)$ with $p+q=n$. In these notes we will assume that the notions of hyperkähler and quaternionic Kähler manifolds include these variations as well. In four dimensions (that is, for $n=1$ ), due to the isomorphism $S p(1) \times_{\mathbb{Z}_{2}} S p(1) \cong S O(4)$ the above definition of quaternionic Kähler manifolds is rather unrestrictive as it encompasses all orientable four-manifolds. In this case the holonomy condition is usually replaced by a curvature condition, and the natural four-dimensional analogues of quaternionic Kähler manifolds are considered to be the self-dual Einstein manifolds. In fact, one can show that quaternionic Kähler manifolds are always Einstein [1], while hyperkähler ones are Einstein with vanishing scalar curvature-that is, Ricci-flat.

The holonomy definition can be shown to be equivalent in the quaternionic Kähler case to the existence of a three-dimensional subbundle of the bundle of endomorphisms of the tangent bundle $\operatorname{End}(T M)$ which is locally spanned by three almost complex structures $I_{1}, I_{2}, I_{3}$, forming the algebra of imaginary quaternions $\left(I_{1}^{2}=I_{2}^{2}=I_{3}^{2}=I_{1} I_{2} I_{3}=-1\right)$, and is preserved by the Levi-Civita connection ∇ . That is to say, there exist locally defined 1-forms $\theta_{1}, \theta_{2}, \theta_{3} \in T^{*} M$ such that
$$\nabla_{X} I_{i}=-2 \varepsilon_{i j k} \theta_{j}(X) I_{k}$$
for any vector field $X \in T M$, where the indices $i, j, k$ run over the values $1,2,3, \varepsilon_{i j k}$ denotes the anti-symmetric Levi-Civita symbol and the numerical factor is conventional. In four dimensions, the $\theta_{i}$ can be viewed as the self-dual part of the spin connection.

In the hyperkähler case, on the other hand, the holonomy definition is equivalent to the existence of a globally defined triplet of almost complex structures $I_{1}, I_{2}, I_{3}$ forming the algebra of imaginary quaternions, each element of which is individually preserved by the Levi-Civita connection:
$$\nabla_{X} I_{i}=0$$

\footnotetext{
${ }^{1}$ An explicit embedding of $S p(n) \times_{\mathbb{Z}_{2}} S p(1)$ as a Lie subgroup of $S O(4 n)$, the holonomy group of a general orientable $4 n$-dimensional Riemannian manifold, is given as follows: regard $\mathbb{R}^{4 n}$ as $\mathbb{H}^{n}$ and consider the linear endomorphisms on the latter given by the simultaneous left and right actions $x_{I} \mapsto A_{I J} x_{J} u^{-1}$ for any $\left(x_{I}\right)_{I=1, \ldots, n} \in \mathbb{H}^{n}$, quaternionic unitary matrix $\left(A_{I J}\right)_{I, J=1, \ldots, n}$, and unit quaternion $u$; the summation convention over repeated indices is understood. This preserves the quaternionic norm on $\mathbb{H}^{n}$, and so the corresponding Euclidean norm on $\mathbb{R}^{4 n}$, which thus exhibits it as an element of $O(4 n)$, and in fact of $S O(4 n)$. The $\mathbb{Z}_{2}$-quotient comes from the invariance under a simultaneous change of sign of both $A_{I J}$ and $u$. Note also that for $n>1, S p(n) \times_{\mathbb{Z}_{2}} S p(1)$ is a maximal subgroup of $S O(4 n)$ [29].
}
for any vector field $X \in T M$. In contrast to the quaternionic Kähler setting, one can now show that the almost complex structures are in fact integrable and thus give rise to genuine complex structures.

In either case, the metric $g$ can always be chosen to be simultaneously Hermitian with respect to each $I_{i}$, and by combining it with them one can form three 2-forms $\omega_{i}(X, Y)=g\left(X, I_{i} Y\right)$, for any $X, Y \in T M$, which are defined locally in the quaternionic Kähler setting and globally in the hyperkähler one. In four dimensions, these form a frame of the bundle of self-dual 2-forms. The above covariant differentiation properties readily translate for the 2-forms into
$$\nabla_{X} \omega_{i}=-2 \varepsilon_{i j k} \theta_{j}(X) \omega_{k}$$
in the quaternionic Kähler case and
$$\nabla_{X} \omega_{i}=0$$
in the hyperkähler one, for an arbitrary vector field $X \in T M$. Since the Levi-Civita connection is symmetric, these formulas imply further that
$$d \omega_{i}=-2 \varepsilon_{i j k} \theta_{j} \wedge \omega_{k}$$
in the first case and
$$d \omega_{i}=0$$
in the second, where we now view $\omega_{i}$ and $\theta_{i}$ as differential forms. Note, however, that the reverse implication does not trivially hold.

Assuming the dimension $n$ to be finite and the metric non-degenerate, since each $I_{i}$ is invertible (with inverse $-I_{i}$ ), it follows that each $\omega_{i}$, viewed as an element of $\operatorname{Hom}\left(T^{*} M, T M\right)$, is also invertible, with inverse $\omega_{i}^{-1} \in \operatorname{Hom}\left(T M, T^{*} M\right)$. A simple argument based on the quaternionic algebra shows then that we can write
$$I_{1}=\omega_{3}^{-1} \omega_{2} \quad I_{2}=\omega_{1}^{-1} \omega_{3} \quad I_{3}=\omega_{2}^{-1} \omega_{1} .$$
1.1.2. In this approach, the three 2-forms are composite objects constructed from the metric and the almost complex structures. In what follows we will present an alternative approach in which this relationship is reversed, and they rather than the latter are regarded as the fundamental building objects of the geometry. Our discussion will emphasize in particular the fact that the two geometries inform each other and can be treated in parallel, and that, although we have made a special point of distinguishing between them, it is often convenient in practice to think of hyperkähler geometry as a limit case of quaternionic Kähler geometry, when the hallmark three-dimensional subbundle of the latter becomes trivial and the scalar curvature vanishes.

The proofs of the subsequent two theorems rely crucially on the following technical lemma:

Lemma 1. Let $M$ be a manifold with an almost complex structure $I$ - that is, an endomorphism of the tangent bundle $T M$ such that $I^{2}=-1$ - and let
$$N_{I}(X, Y)=-I^{2}[X, Y]+I([I X, Y]+[X, I Y])-[I X, I Y]$$
for arbitrary vector fields $X, Y \in T M$ be the associated Nijenhuis tensor. A real-valued 2-form $\omega$ on $M$ is
\begin{itemize}
\item[a)] of $(1,1)$ type with respect to $I$ if and only if
$$\omega(X, I Y)=\omega(Y, I X) \stackrel{\text { def }}{=}-g(X, Y)$$
for any $X, Y \in T M$. In this case the following identity holds:
$$\omega\left(N_{I}(X, Y), Z\right)=d \omega(I X, I Y, Z)-d \omega(X, Y, Z)+2 \nabla_{Z} \omega(X, Y)$$
where ∇ is the Levi-Civita connection corresponding to the compatible metric $g$.
\item[b)] of mixed $(2,0)+(0,2)$ type with respect to $I$ if and only if
$$\omega(X, I Y)=-\omega(Y, I X) \stackrel{\text { def }}{=}-\tilde{\omega}(X, Y)$$
for any $X, Y \in T M$. (The complex-valued 2-forms $\omega+i \tilde{\omega}$ and $\omega-i \tilde{\omega}$ are then of pure $(2,0)$ and $(0,2)$ type with respect to $I$, respectively.) In this case we have the identity
$$\omega\left(N_{I}(X, Y), Z\right)=d \omega(I X, I Y, Z)-d \omega(X, Y, Z)+d \tilde{\omega}(I X, Y, Z)+d \tilde{\omega}(X, I Y, Z) .$$
\end{itemize}

Proof. Part (a) is essentially Proposition 4.6 from ch. IX, sec. 4 of reference [36] (the numerical factors differ due to differing normalization conventions for differential forms). Let us reproduce here the proof briefly. On one hand, we transform the last term on the right-hand side of the identity we want to prove as follows
$$\begin{aligned}
\nabla_{Z} \omega(X, Y) & =-g\left(\left(\nabla_{Z} I\right) X, Y\right) \\
& =-g\left(\nabla_{Z}(I X), Y\right)+g\left(I \nabla_{Z} X, Y\right) \\
& =-g\left(\nabla_{Z}(I X), Y\right)-g\left(\nabla_{Z} X, I Y\right)
\end{aligned}$$
and then apply for each resulting term the Koszul formula for the Levi-Civita connection
$$\begin{aligned}
2 g\left(\nabla_{X} Y, Z\right) & =X(g(Y, Z))+Y(g(X, Z))-Z(g(X, Y)) \\
& -g([Y, Z], X)-g([X, Z], Y)+g([X, Y], Z) .
\end{aligned}$$
On the other hand, for the remaining two terms on the right-hand side we use the identity
$$\begin{aligned}
d \omega(X, Y, Z) & =X(\omega(Y, Z))-Y(\omega(X, Z))+Z(\omega(X, Y)) \\
& -\omega([Y, Z], X)+\omega([X, Z], Y)-\omega([X, Y], Z) .
\end{aligned}$$
The result follows then by isolating the expression on the left-hand side and then cancelling the remaining terms by making use of the relationship between $\omega$ and $g$, and the properties which follow from it.

The formula at part (b) can be verified in a relatively more straightforward manner by applying the identity (12) to both the $d \omega$ and the $d \tilde{\omega}$ terms, and then systematically replacing in the resulting expression $\tilde{\omega}$ with $\omega$ by using some version of the defining relation for the former. \(\square\)

With this lemma in hand we can now return to our initial discussion. On the hyperkähler side we have the following criterion, which is in essence a version of Lemma 6.8 of reference [30]:

Theorem 2. A finite-dimensional manifold $M$ is hyperkähler if and only if it possesses a triplet of non-degenerate and pointwise linearly independent 2-forms $\omega_{1}, \omega_{2}, \omega_{3}$ satisfying simultaneously:
\begin{itemize}
\item[-] an algebraic condition: if we define
$$I_{1}=\omega_{3}^{-1} \omega_{2}, I_{2}=\omega_{1}^{-1} \omega_{3}, I_{3}=\omega_{2}^{-1} \omega_{1} \in \operatorname{End}(T M)$$
then we have $I_{1}^{2}=I_{2}^{2}=I_{3}^{2}=-1$.
\item[-] an exterior differential condition: the 2-forms are symplectic, i.e.,
$$d \omega_{1}=d \omega_{2}=d \omega_{3}=0 .$$
\end{itemize}

Proof. Observe that although the algebraic condition formally requires only that $I_{1}, I_{2}, I_{3}$ be almost complex structures, it fully implies in fact that they satisfy the entire imaginary quaternionic algebra. Indeed, since they square to minus the identity we have
$$\begin{aligned}
& I_{1}=\omega_{3}^{-1} \omega_{2}=-\omega_{2}^{-1} \omega_{3} \\
& I_{2}=\omega_{1}^{-1} \omega_{3}=-\omega_{3}^{-1} \omega_{1} \\
& I_{3}=\omega_{2}^{-1} \omega_{1}=-\omega_{1}^{-1} \omega_{2}
\end{aligned}$$
from which we get immediately that $I_{1} I_{2} I_{3}=\left(-\omega_{2}^{-1} \omega_{3}\right)\left(-\omega_{3}^{-1} \omega_{1}\right)\left(-\omega_{1}^{-1} \omega_{2}\right)=-1$.
Let us define now the following sections of $\operatorname{Hom}\left(T^{*} M, T M\right)$ or, equivalently, rank-2 contravariant tensors:
$$\begin{aligned}
& g_{1}=-\omega_{1} I_{1}=-\omega_{1} \omega_{3}^{-1} \omega_{2}=\omega_{1} \omega_{2}^{-1} \omega_{3} \\
& g_{2}=-\omega_{2} I_{2}=-\omega_{2} \omega_{1}^{-1} \omega_{3}=\omega_{2} \omega_{3}^{-1} \omega_{1} \\
& g_{3}=-\omega_{3} I_{3}=-\omega_{3} \omega_{2}^{-1} \omega_{1}=\omega_{3} \omega_{1}^{-1} \omega_{2} .
\end{aligned}$$
Since the $\omega_{i}$ 's are all antisymmetric, by comparing for example the third expression for $g_{1}$ with the fourth one for $g_{2}$ we see that $g_{1}^{T}=g_{2}$, where the superscript $T$ denotes transposition. Similarly, $g_{2}^{T}=g_{3}$ and $g_{3}^{T}=g_{1}$, from which it follows immediately that $g_{1}=g_{2}=g_{3}=$ a symmetric rank- 2 contravariant tensor. In other words, the algebraic condition also implies that we can define a metric on $M$ by
$$g(X, Y)=-\omega_{1}\left(X, I_{1} Y\right)=-\omega_{2}\left(X, I_{2} Y\right)=-\omega_{3}\left(X, I_{3} Y\right)$$
for any $X, Y \in T M$. The minus signs have been chosen in order to ensure compatibility with our original definition of the 2-forms $\omega_{i}$. Such a metric is automatically Hermitian with respect to each $I_{i}$ (this is possible only when $\operatorname{dim} M=4 n$ ), and its signature is in general of type ( $4 n_{+}, 4 n_{-}$), with $n_{+}+n_{-}=n$, so the manifold $M$ is in general pseudo-Riemannian.

Remark now that in order to prove that the manifold $M$ carries a hyperkähler structure it suffices to prove that each $\omega_{i}$ is covariantly constant with respect to the Levi-Civita connection of the metric $g$. The covariant constancy of the $I_{i}$ follows then right away.

This can be shown in two steps. First, note that based on the quaternionic algebra we can write successively $\omega_{2}\left(X, I_{1} Y\right)=g\left(X, I_{2} I_{1} Y\right)=-g\left(X, I_{3} Y\right)=-\omega_{3}(X, Y)$, and since the last expression is antisymmetric at the exchange of $X$ and $Y$ it follows that $\omega_{2}$ is of mixed $(2,0)+(0,2)$ type with respect to $I_{1}$. By part $(b)$ of Lemma 1 we then have
$$\begin{aligned}
\omega_{2}\left(N_{I_{1}}(X, Y), Z\right) & =d \omega_{2}\left(I_{1} X, I_{1} Y, Z\right)-d \omega_{2}(X, Y, Z) \\
& +d \omega_{3}\left(I_{1} X, Y, Z\right)+d \omega_{3}\left(X, I_{1} Y, Z\right) .
\end{aligned}$$
As $\omega_{2}$ and $\omega_{3}$ are by assumption closed, the right-hand side of this equation vanishes, and since moreover $\omega_{2}$ is non-degenerate it follows that the Nijenhuis tensor of $I_{1}$ vanishes. By the Newlander-Nirenberg theorem, $I_{1}$ is then an integrable complex structure.

Second, as $\omega_{1}\left(X, I_{1} Y\right)=-g(X, Y)$ is symmetric at the exchange of $X$ and $Y, \omega_{1}$ is of type $(1,1)$ with respect to $I_{1}$. By part $(a)$ of Lemma 1 we can then write
$$2 \nabla_{Z} \omega_{1}(X, Y)=\omega_{1}\left(N_{I_{1}}(X, Y), Z\right)-d \omega_{1}\left(I_{1} X, I_{1} Y, Z\right)+d \omega_{1}(X, Y, Z) .$$
The vanishing of the Nijenhuis tensor for $I_{1}$ together with the closure of $\omega_{1}$ imply then that $\omega_{1}$ is covariantly constant with respect to the Levi-Civita connection. The covariant constancy of $\omega_{2}$ and $\omega_{3}$, as well as the integrability of $I_{2}$ and $I_{3}$, follow by cyclically permuting the indices in the argument. \(\square\)

Remark. The triplets of 2-forms defining a given hyperkähler metric are not unique. To be more precise, the conditions of the theorem are invariant under the following two types of constant linear transformations:
\begin{itemize}
\item[1)] $\omega_{i} \mapsto \lambda \omega_{i}$ for any non-vanishing constant $\lambda \in \mathbb{R}^{\times}$. The corresponding hyperkähler metric rescales then from $g$ to $\lambda g$.
\item[2)] $\omega_{i} \mapsto R_{i j} \omega_{j}$ for any constant rotation matrix $R_{i j} \in S O(3)$. These transformations leave the metric unchanged. Thus, for any triplet of 2-forms $\omega_{i}$ satisfying the conditions of the theorem one automatically has a half 3-sphere's worth of such triplets giving the same hyperkähler metric (recall that, topologically, $\operatorname{SO}(3) \cong S^{3} / \mathbb{Z}_{2}$ ).
\end{itemize}
Out of these, the only invariance which is perhaps not immediately obvious is that of the algebraic condition at $S O(3)$ rotations. The considerations in the first part of the proof make it clear that the algebraic condition is equivalent to the existence of a triplet $I_{i} \in \operatorname{End}(T M)$ and a metric $g$ such that $\omega_{i} I_{j}=\varepsilon_{i j k} \omega_{k}-\delta_{i j} g$. Then, since $S O(3)$ transformations preserve both the $\varepsilon$-symbol and the $\delta$-symbol (the $S$ and $O$ in $S O(3)$, respectively), this relation is invariant under simultaneous rotations $\omega_{i} \mapsto R_{i j} \omega_{j}$ and $I_{i} \mapsto R_{i j} I_{j}$ while $g$ stays unchanged. That is to say, for each rotated set of $\omega_{i}$ 's there exists a rotated set of $I_{i}$ 's satisfying the same algebraic condition and determining the same metric.

On the quaternionic Kähler side, on the other hand, we have the following version of Proposition 3 from reference [2]:

Theorem 3. A finite-dimensional manifold $M$ is quaternionic Kähler if and only if it possesses a rank-3 $S O(3)$-subbundle $Q$ of the bundle of non-degenerate 2-forms on $M$ and an open covering $\mathcal{C}$ of $M$ on each element $U$ of which one can pick a local frame $\omega_{1}, \omega_{2}, \omega_{3}$ for $\left.Q\right|_{U}$ satisfying simultaneously
\begin{itemize}
\item[-] an algebraic condition: if we define
$$I_{1}=\omega_{3}^{-1} \omega_{2}, I_{2}=\omega_{1}^{-1} \omega_{3}, I_{3}=\omega_{2}^{-1} \omega_{1} \in \operatorname{End}(T M)$$
then we have $I_{1}^{2}=I_{2}^{2}=I_{3}^{2}=-1$.
\item[-] an exterior differential condition: there exist locally defined 1-forms $\theta_{1}, \theta_{2}, \theta_{3}$ such that
$$d \omega_{i}=-2 \varepsilon_{i j k} \theta_{j} \wedge \omega_{k} .$$
\end{itemize}

Proof. The structure of the proof mirrors closely that of the previous theorem. In particular, by virtually the same arguments as before the algebraic condition implies that the almost complex structures $I_{1}, I_{2}, I_{3}$ satisfy the imaginary quaternionic algebra, and that, moreover, a tri-Hermitian metric $g$ can be defined by means of the same equation (17).

The essential difference with respect to the hyperkähler case is that these quantities are now defined locally, and we need to check in addition that they give rise to the requisite
global structures. For that, let us consider two arbitrary overlapping open sets $U, V \in \mathcal{C}$. The two corresponding local frames $\omega_{i U}$ and $\omega_{i V}$ of the vector bundle $Q$ are related on the intersection $U \cap V$ by means of a transition function $R_{i j}$ which is a local $S O(3)$ rotation: $\omega_{i V}=R_{i j} \omega_{j U}$. Adjoining to the symbol of each locally defined quantity its domain of definition we have then by essentially the same argument as in the Remark following the previous theorem $\left(R_{i m} \omega_{m U}\right)\left(R_{j n} I_{n U}\right)=\varepsilon_{i j k}\left(R_{k l} \omega_{l U}\right)-\delta_{i j} g_{U}$. By considering the offdiagonal terms in this relation we can see immediately that we must have $I_{i V}=R_{i j} I_{j U}$, that is, the almost complex structures are local sections - and in fact, frames - of an associated $S O(3)$-subbundle of $\operatorname{End}(T M)$. On the other had, from the diagonal terms we get that $g_{V}=g_{U}$, that is, the metric is globally defined.

To prove that the manifold $M$ carries a quaternionic Käher structure it suffices to show that the action of the Levi-Civita covariant derivative with respect to the metric $g$ on the 2-forms $\omega_{i}$ is of the form (3). The corresponding covariant differentiation property (1) of the almost complex structures $I_{i}$ follows then immediately.

By the same reasoning as in the hyperkähler case, $\omega_{2}$ and $\omega_{1}$ are of mixed $(2,0)+(0,2)$ respectively pure $(1,1)$ type with respect to $I_{1}$. So then by parts $(b)$ and $(a)$ of Lemma 1 the same identities (18) and (19) hold now, too. From the first one, by inserting the expressions for $d \omega_{2}$ and $d \omega_{3}$ given by the current exterior differential condition we retrieve, after a purely algebraic computation, the following form for the Nijenhuis tensor of $I_{1}$ :
$$\begin{aligned}
N_{I_{1}}(X, Y) & =2\left(\theta_{2}(X)-\theta_{3}\left(I_{1} X\right)\right) I_{2} Y+2\left(\theta_{2}\left(I_{1} X\right)+\theta_{3}(X)\right) I_{3} Y \\
& -2\left(\theta_{2}(Y)-\theta_{3}\left(I_{1} Y\right)\right) I_{2} X-2\left(\theta_{2}\left(I_{1} Y\right)+\theta_{3}(Y)\right) I_{3} X .
\end{aligned}$$
Plugging then this into the second identity together with the remaining expression for $d \omega_{1}$ gives us after another series of algebraic manipulations that
$$\nabla_{Z} \omega_{1}(X, Y)=-2 \theta_{2}(Z) \omega_{3}(X, Y)+2 \theta_{3}(Z) \omega_{2}(X, Y) .$$
Permuting the indices cyclically in this argument yields the rest of the components of the desired property (3). \(\square\)

Remark. Quaternionic Käher manifolds are particular examples of quaternionic manifolds (for a detailed review see e.g. [5]). These are manifolds $M$ which carry a three-dimensional subbundle of $\operatorname{End}(T M)$ with fibers spanned at each point by a basis $\left\{I_{1}, I_{2}, I_{3}\right\}$ whose elements satisfy the algebra of imaginary quaternions, and which, in addition, admit a torsion-free connection preserving this structure. If it exists, such a connection, called an Oproiu connection, is not unique. Their so-called structure tensor takes the form
$$\frac{1}{6} \sum_{i=1}^{3} N_{I_{i}}(X, Y)=\sum_{i=1}^{3}\left(\theta_{i}^{\mathrm{Op}}(X) I_{i} Y-\theta_{i}^{\mathrm{Op}}(Y) I_{i} X\right)$$
where the triplet of 1 -forms $\theta_{i}^{\mathrm{Op}}$ are the Oproiu connection 1-forms.
From the above formula for the Nijenuis tensor for $I_{1}$ and its cyclic permutations one can verify that in the quaternionic Kähler case the structure tensor is indeed of this form, with
$$\theta_{i}^{\mathrm{Op}}=\frac{2}{3} \theta_{i}-\frac{1}{3} \varepsilon_{i j k} \theta_{j} I_{k} .$$
(Here we use the convention that the $I_{i}$ act on vector fields from the left and dually, on

1-forms, from the right.) Note that these can be rewritten as
$$\theta_{i}^{\mathrm{Op}}=\theta_{i}+\xi I_{i} \quad \text { with } \quad \xi=\frac{1}{3}\left(\theta_{1} I_{1}+\theta_{2} I_{2}+\theta_{3} I_{3}\right)$$
which essentially means (see e.g. [9]) that in the quaternionic Kähler case the Oproiu connection is equivalent to the Levi-Civita one.

The following alternative version of the criterion enunciated in Theorem 3 also holds:
Theorem 4. The exterior differential condition of Theorem 3 can be replaced with the following condition:
\begin{itemize}
\item[-] The principal $S O(3)$-bundle $\mathcal{Q}$ associated to the bundle $Q$ admits a connection with curvature 2-form equal, up to a non-vanishing constant, to $\omega_{i}$. That is, there exist locally defined connection 1-forms $\theta_{i}$ and a constant $s \neq 0$ such that
\end{itemize}
$$d \theta_{i}+\varepsilon_{i j k} \theta_{j} \wedge \theta_{k}=s \omega_{i} .$$
Proof. The fact that this condition implies the second condition of Theorem 3 is straightforward: the latter is a Bianchi-type consistency condition for the former. The converse implication follows, for $n>1$, from a result first shown by Alekseevsky, see e.g. part (iii) of Theorem 5.7 in [5]. For $n=1$, the condition above is equivalent to the Einstein equation. In either case, one can identify
$$s=\frac{R_{g}}{8 n(n+2)}$$
where $R_{g}$ is the scalar curvature of the metric $g$. ( $s$ is called reduced scalar curvature, and the extra 1/2 factor with respect to the definition in [5] is a matter of convention stemming from our unusual normalization of the $S O(3)$ connection 1-forms.) \(\square\)
1.2. Killing vector fields. Next, we want to explore how symmetry conditions, and in particular the Killing condition, translate in the framework in which triplets of 2-forms rather than the metric and the (almost) complex structures play the fundamental role. In order to address this question, we need to recall first some background material culminating with a general theorem due to B. Kostant concerning Killing vector fields on Riemannian manifolds with special holonomy.
1.2.1. Let $M$ be a Riemannian manifold with metric $g$. By definition, we call an endomorphism $\Omega \in \operatorname{End}(T M)$ skew-symmetric if
$$g(X, \Omega Y)=-g(Y, \Omega X) \stackrel{\text { def }}{=} \omega(X, Y) .$$
for any pair $X, Y \in T M$. Skew-symmetric endomorphisms from $\operatorname{End}(T M)$ are in one-toone correspondence with 2-forms on $M$ by way of the metric. On the space SkewEnd $(T M)$ of such endomorphisms one can define a natural inner product by
$$\left\langle\Omega_{1}, \Omega_{2}\right\rangle=-\frac{1}{\operatorname{dim} M} \operatorname{trace}\left(\Omega_{1} \Omega_{2}\right) .$$
This is in general non-degenerate and, in Riemannian signature, positive definite. Moreover, a choice of orthonormal basis on the tangent space $T_{p} M$ at a point $p \in M$ gives a vector space isometry $T_{p} M \longrightarrow \mathbb{R}^{\operatorname{dim} M}$, with the latter space endowed with the standard Euclidean metric. This determines in turn an isomorphism between $\operatorname{SkewEnd}\left(T_{p} M\right)$ and $\mathfrak{s} \mathfrak{o}(\operatorname{dim} M)$, the Lie algebra of skew-symmetric endomorphisms of $\mathbb{R}^{\operatorname{dim} M}$.
1.2.2. For any vector field $X \in T M$ let us define the operator $A_{X}=\mathcal{L}_{X}-\nabla_{X}$ measuring the difference between the Lie derivative and the Levi-Civita covariant derivative along $X$. Also, for any two vector fields $X, Y \in T M$, let $R_{X, Y}=\left[\nabla_{X}, \nabla_{Y}\right]-\nabla_{[X, Y]}$ be the usual Riemannian curvature operator of the Levi-Civita connection. As derivations acting linearly on any tensor field on $M$ and vanishing on functions, both of these operators are linear algebraic rather than differential in nature and are represented by tensors. The tensors are in either case endomorphisms of the tangent bundle $T M$. For $A_{X}$, this is $\nabla X$, the covariant derivative of $X$, which one may view as the endomorphism of $T M$ defined by $\nabla X Z=\nabla_{Z} X$ for any $Z \in T M$. For $R_{X, Y}$, it is the Riemann curvature endomorphism $R(X, Y)$. So for example, on functions, vector fields and endomorphisms of the tangent bundle we have, respectively,
$$\begin{array}{lll}
A_{X} f=0 & R_{X, Y} f=0 & \forall f \in C^{\infty}(M) \\
A_{X} Z=-\nabla X Z & R_{X, Y} Z=R(X, Y) Z & \forall Z \in T M \\
A_{X} \Omega=-[\nabla X, \Omega] & R_{X, Y} \Omega=[R(X, Y), \Omega] & \forall \Omega \in \operatorname{End}(T M)
\end{array}$$
where the square brackets denote commutators. What is more, $R(X, Y) \in \operatorname{SkewEnd}(T M)$ for all $X, Y \in T M$, whereas $\nabla X \in \operatorname{SkewEnd}(T M)$ if and only if $X$ is a Killing vector field.

In fact, in regard to Killing vector fields we have, moreover, the following properties (see e.g. Proposition 2.6 in ch. VI, sec. 2 of [35]):

Lemma 5. Let $M$ be a Riemannian manifold.
\begin{itemize}
\item[1)] If $X$ is a Killing vector field on $M$ then
$$\left[\nabla_{Y}, A_{X}\right]=R_{X, Y}$$
for any vector field $Y \in T M$.
\item[2)] If both $X$ and $Y$ are Killing vector fields on $M$ then we have
$$R_{X, Y}=\left[A_{X}, A_{Y}\right]-A_{[X, Y]} .$$
\end{itemize}

Proof. The relations follow immediately from the definitions upon using the fact that the Lie derivative with respect to a Killing vector field commutes with the Levi-Civita connection. Formally, this can be expressed as follows: if $X$ is a Killing vector field, then $\left[\mathcal{L}_{X}, \nabla_{Y}\right]=\nabla_{[X, Y]}$ for any vector field $Y$. \(\square\)

Note that in terms of the associated skew-symmetric endomorphisms the operatorial relation (32) can be equivalently written as
$$\nabla_{Y}(\nabla X)=R(Y, X) .$$
This is sometimes known as Kostant's formula.
1.2.3. The isometries of a Riemannian manifold form a Lie group (Myers-Steenrod). On another hand, we have the notion of holonomy group. Given a connected Riemannian manifold $M$, its holonomy group at a point $p \in M$ is by definition the set of linear endomorphisms of the tangent space $T_{p} M$ obtained by parallel transporting tangent vectors with respect to the Levi-Civita connection around piecewise smooth loops based at $p$. This set has naturally the structure of a group. The restricted holonomy group at $p$ is the subgroup coming from contractible loops. The latter is a connected Lie subgroup of the group of orthogonal transformations of $T_{p} M$. By choosing an orthonormal basis for $T_{p} M$ we may identify it with a Lie subgroup of $S O(\operatorname{dim} M)$. This subgroup depends on both the choice
of basis and of base point $p$, but its conjugacy class depends on neither. The possible holonomy groups of simply-connected irreducible Riemannian manifolds have been classified by M. Berger.

The relation between the holonomy group and the (continuous part of the) isometry group of a Riemannian manifold is described by the following result:

Theorem 6 (Kostant [37]). Let $M$ be a Riemannian manifold and $\mathfrak{h}$ be the Lie algebra of the restricted holonomy group at a point $p \in M$. If $X$ is a Killing vector field on $M$, then the skew-symmetric endomorphism of the tangent space $T_{p} M$ determined by $\nabla X$ belongs to the normalizer of $\mathfrak{h}$ in $\mathfrak{s o}(\operatorname{dim} M)$. Moreover, if $M$ is orientable and compact then this belongs simply to $\mathfrak{h}$.

Proof. As a skew-symmetric endomorphism of the tangent bundle, $\nabla X$ can be decomposed uniquely into two orthogonal components with respect to the inner product (30), one belonging to $\mathfrak{h}$ and the other to its orthogonal complement in $\mathfrak{s o}(\operatorname{dim} M)$ :
$$\nabla X=\nabla X^{\mathfrak{h}}+\nabla X^{\mathfrak{h}^{\perp}} .$$
Suppose then we act with $\nabla_{Y}$ for some vector field $Y$ simultaneously on both sides of this equation. One the left-hand side we obtain, by way of the property (34), $R(Y, X)$, which, by the Ambrose-Singer theorem, belongs to $\mathfrak{h}$. On the other hand, since the inner product is preserved by parallel transport, one can argue that $\nabla_{Y}\left(\nabla X^{\mathfrak{h}}\right) \in \mathfrak{h}$ and $\nabla_{Y}\left(\nabla X^{\mathfrak{h}^{\perp}}\right) \in \mathfrak{h}^{\perp}$ for all $Y$. The inner product being non-degenerate, the intersection $\mathfrak{h} \cap \mathfrak{h}^{\perp}$ is trivial, and so it follows that one must have $\nabla_{Y}\left(\nabla X^{\mathfrak{h}^{\perp}}\right)=0$. This means in particular that $\nabla X^{\mathfrak{h}^{\perp}}$ is invariant at parallel transport around a closed loop and thus belongs to the centralizer of $\mathfrak{h}$ in $\mathfrak{s o}(\operatorname{dim} M)$. The first part of the theorem follows then immediately.

For further details as well as the proof of the fact that when $M$ is orientable and compact $\nabla X^{\mathfrak{h}^{\perp}}$ vanishes we direct the interested reader to the original paper [37], or the review in ch. VI of [35]. \(\square\)
1.2.4. Let us return now to the particular case of quaternionic Kähler and hyperkähler manifolds, for which $\operatorname{dim} M=4 n$. Remark that we have now at our disposal three more skew-symmetric endomorphisms of the tangent bundle, namely $I_{1}, I_{2}, I_{3}$. Since SkewEnd $\left(T_{p} M\right)$ is isomorphic in either case, for any point $p \in M$, to the fundamental representation of the Lie algebra $\mathfrak{s o}(4 n)$, it inherits this one's structure. Thus, it naturally splits into three subspaces isomorphic to the $\mathfrak{s p}(n)$ and $\mathfrak{s p}(1)$ Lie subalgebras of $\mathfrak{s o}(4 n)$, and their complement in $\mathfrak{s o}(4 n)$, respectively. The second subspace is spanned by $I_{1}, I_{2}, I_{3}$ and, moreover, any element from the first subspace commutes with any element from the second. What is more, the three subspaces are mutually orthogonal with respect to the inner product (30).

These algebraic properties can be seen explicitly for instance within the so-called $E-H$ formalism of [45]. Let us recall briefly its main aspects. For quaternionic Kähler manifolds one can associate in principle a locally defined vector bundle to each representation of the holonomy group $S p(n) \times_{\mathbb{Z}_{2}} S p(1)$. In particular, the complexified cotangent bundle $T_{\mathbb{C}}^{*} M$ splits locally into a tensor product $E \otimes H$ of two such vector bundles corresponding to the standard complex representations of rank $2 n$ and 2 of $\operatorname{Sp}(n)$ and $\operatorname{Sp}(1)$, respectively. For $n=1$, in four dimensions, where the holonomy definition is side-stepped, one takes instead $E$ and $H$ to be the two spinor bundles of $M$. The bundles $E$ and $H$ come equipped with natural symplectic forms - constant anti-symmetric sections $\varepsilon_{E} \in \Lambda^{2} E$ and $\varepsilon_{H} \in \Lambda^{2} H$. In the hyperkähler case, which in this context is most profitably viewed as a quaternionic Kähler limit case, the same split structure exists, except that the bundle $H$ is now trivial.

Any $S O(4 n)$-module decomposes into direct sums of irreducible $S p(n) \times_{\mathbb{Z}_{2}} S p(1)$-modules, which are tensor products of even total number of $\operatorname{Sp}(n)$ and $\operatorname{Sp}(1)$-modules. In particular, this is the case for the bundle $\Lambda^{2} T^{*} M$. Any 2-form $\omega$ thus decomposes as
$$\omega=\omega^{\mathfrak{s p}(n)}+\omega^{\mathfrak{s p}(1)}+\omega^{\mathfrak{c p l}}$$
where, in a local $E-H$ frame, we have
$$\begin{aligned}
& \omega^{\mathfrak{s p}(n)}=\omega_{E} \otimes \varepsilon_{H}, \text { with } \omega_{E} \in S^{2} E \cong \mathfrak{s p}(n) \\
& \omega^{\mathfrak{s p}(1)}=\varepsilon_{E} \otimes \omega_{H}, \text { with } \omega_{H} \in S^{2} H \cong \mathfrak{s p}(1) \\
& \omega^{\mathfrak{c p l}} \in \Lambda_{0}^{2} E \otimes S^{2} H .
\end{aligned}$$
Here, $S$ and $\Lambda$ denote symmetric respectively anti-symmetric tensor products, and $\Lambda_{0}^{2} E$ denotes the kernel of the contraction of $\Lambda^{2} E$ with the inverse of the symplectic form $\varepsilon_{E}$ (this kernel is trivial for $n=1$ ). Note that the quaternionic Kähler/hyperkähler 2-forms $\omega_{i}$ are of pure $\mathfrak{s p}(1)$ type, and they provide a frame for the respective subbundle of $\Lambda^{2} T^{*} M$.

On another hand, in the same $E-H$ frame the metric factorizes locally as $g=\varepsilon_{E} \otimes \varepsilon_{H}$. Recalling then that any skew-symmetric endomorphism $\Omega$ of $T M$ is related to a corresponding 2-form $\omega$ by $\Omega=g^{-1} \omega$, the statements above, and in particular the orthogonality claim, can be verified directly through simple algebraic calculations.
1.2.5. The curvature tensor also admits an irreducible $E-H$ decomposition [45, Theorem 3.1]. In what follows, though, we will only need the fact that the curvature endomorphism of a quaternionic Kähler manifold satisfies the commutation property
$$\left[I_{i}, R(X, Y)\right]=2 s \varepsilon_{i j k} \omega_{j}(X, Y) I_{k} .$$
For hyperkähler manifolds the right-hand side vanishes, consistent with taking the limit to $s=0$. In the quaternionic Kähler case this is essentially the consistency condition for the differential equation (1), with the Einstein condition (27) taken into account. In the hyperkähler case it is simply the consistency condition for the corresponding equation (2). In either case its structure can be easily understood by purely algebraic arguments from the Ambrose-Singer theorem.

Note in particular that if we multiply this equality from either side with an $I_{l}$ and then take the trace of the result we obtain - using successively the cyclicity property of the trace, the quaternionic algebra, and the fact that the trace of any element from SkewEnd( $T M$ ) vanishes - the following consequence:
$$\left\langle I_{i}, R(X, Y)\right\rangle=s \omega_{i}(X, Y) .$$
1.2.6. For the remainder of this section we will assume that the manifolds are irreducible, by which we mean that their holonomy groups are assumed to be equal to rather than included in $S p(n) \times_{\mathbb{Z}_{2}} S p(1)$ in the quaternionic Kähler case (for $n>1$ ), and $S p(n)$ in the hyperkähler one.

If the quaternionic Kähler or hyperkähler manifold $M$ possesses a Killing vector field $X$, then by Theorem 6 its covariant derivative $\nabla X$ belongs to the normalizer of the Lie subalgebra $\mathfrak{s p}(n) \oplus \mathfrak{s p}(1)$ respectively $\mathfrak{s p}(n)$ in $\mathfrak{s o}(4 n)$, which one can easily see is in both cases $\mathfrak{s p}(n) \oplus \mathfrak{s p}(1)$. With the notations above, this means that $\nabla X^{\mathfrak{c p l}}=0$, and so
$$\nabla X=\nabla X^{\mathfrak{s p}(n)}+\nabla X^{\mathfrak{s p}(1)}$$
with the two remaining components both orthogonal and commuting. In four dimensions this decomposition is automatic for any skew-symmetric endomorphism of $T M$, so in this case one need not resort to holonomy arguments. The second component, in particular, is a linear superposition
$$\nabla X^{\mathfrak{s} \mathfrak{p}(1)}=-\sum_{i=1}^{3} \nu_{X i} I_{i}$$
with coefficients $\nu_{X i}$, where the minus sign is conventionally chosen for later convenience. The generators $I_{i}$ satisfy the orthogonality relations $\left\langle I_{i}, I_{j}\right\rangle=\delta_{i j}$ and $\left\langle I_{i}, \nabla X^{\mathfrak{s p}(n)}\right\rangle=0$, and thus we may identify
$$\nu_{X i}=-\left\langle I_{i}, \nabla X\right\rangle .$$
1.2.7. These coefficients play an important role in the description of Killing symmetries. In the quaternionic Kähler case, switching to an $\mathbb{R}^{3}$-vector notation, we have:

Theorem 7 (Galicki, Lawson [25, 26]). Consider a quaternionic Kähler manifold $M$ with associated principal $S O(3)$-bundle $\mathcal{Q}$, and assume that $M$ has a continuous group of isometries $G$, with Lie algebra $\mathfrak{g}$. Then a vector field $X \in \mathfrak{g}$, that is $X$ is Killing, if and only if there exists a local section $\vec{\nu}_{X}$ of the tensor product bundle $\mathfrak{g}^{*} \otimes \mathcal{Q}$ over $M$ such that ${ }^{2}$
$$\mathcal{L}_{X} \vec{\omega}=-2\left(\iota_{X} \vec{\theta}+\vec{\nu}_{X}\right) \times \vec{\omega}$$
or, equivalently, such that
$$d \vec{\nu}_{X}+2 \vec{\theta} \times \vec{\nu}_{X}=s \iota_{X} \vec{\omega} .$$
Explicitly, this section is given by the formula $\vec{\nu}_{X}=-\langle\vec{I}, \nabla X\rangle$ for any $X \in \mathfrak{g}$ and it is
\begin{itemize}
\item[○] nowhere vanishing
\item[○] the unique solution to the quaternionic-Kähler moment map equation (44)
\item[○] G-equivariant
\item[○] and, for any $X, Y \in \mathfrak{g}$, we have
\end{itemize}
$$2 \vec{\nu}_{[X, Y]}=2 \vec{\nu}_{X} \times 2 \vec{\nu}_{Y}-2 s \vec{\omega}(X, Y) .$$
Proof. Suppose $X$ is a killing vector field on $M$. Then by the rules laid out in the list (31) we have
$$A_{X} I_{i}=\left[I_{i}, \nabla X\right]=\left[I_{i}, \nabla X^{\mathfrak{s p}(1)}\right]=-2 \varepsilon_{i j k} \nu_{X j} I_{k} .$$
The $\mathfrak{s p}(n)$ component of $\nabla X$ drops out because it commutes with the $\mathfrak{s p}(1)$ generators, and for the remaining $\mathfrak{s p}(1)$ component we use the representation (41). Converting then the almost complex structures into 2-forms by means of the metric, which is preserved by the action of $A_{X}$, gives us promptly the rotation property (43).

Conversely, let us assume that we have a vector field $X$ whose Lie action rotates the quaternionic Kähler 2-forms, that is $\mathcal{L}_{X} \omega_{i}=-2 \varepsilon_{i j k} r_{j} \omega_{k}$ for some locally defined triplet of functions $r_{j}$. Using then any one of the expressions (16) of the metric in terms of the quaternionic Kähler 2-forms one can easily check that this implies that $X$ is Killing, regardless of the particular form of the functions $r_{j}$.

Suppose now again that $X$ is Killing. If we act with $\nabla_{Y}$ for some arbitrary $Y \in T M$ on the expression (42) for $\nu_{X i}$ we obtain, by applying the Leibniz rule and then the properties

\footnotetext{
${ }^{2}$ The symbol × denotes the usual $\mathbb{R}^{3}$-vector cross product.
}
(1), (34) and (39), that $\nabla_{Y} \nu_{X i}+2 \varepsilon_{i j k} \theta_{j}(Y) \nu_{X k}=s \omega_{i}(X, Y)$. The quaternionic Kähler moment map equation (44) is simply a rewriting of this equation in the language of differential forms.

Conversely, let us assume that there exists a vector field $X$ satisfying the quaternionic Kähler moment map equation for some locally defined functions $\nu_{X i}$. Then by acting on this equation with an exterior differential and making use of the Einstein property (27) one can show that the rotation property (43) is implied. By the argument above, this implies further that $X$ must be Killing.

The non-vanishing of the section $\nu_{X i}$ follows directly from the quaternionic Kähler moment map equation. Should it vanish at some point, the equation would imply that $X$ would be a null vector for the 2-forms $\omega_{i}$ at that point, which would contradict their non-degeneracy.

For an argument that the solution to the quaternionic Kähler moment map equation is unique we refer the reader to reference [26].

Remark. Note that, unlike the rest of the arguments in the proof, each of the arguments in the last three paragraphs fails in the limit when $s=0$ and thus cannot be extended to the hyperkähler case.

Assume now that we have two Killing vector fields $X, Y \in \mathfrak{g}$. Using the representation (33) for the curvature operator, and then the formulas (46) and (38), we can write
$$A_{[X, Y]} I_{i}=\left[A_{X}, A_{Y}\right] I_{i}-\left[R(X, Y), I_{i}\right]=-2 \varepsilon_{i j k} \nu_{[X, Y] j} I_{k}$$
with $\nu_{[X, Y] j}$ defined as in the theorem.
Finally, since $\mathcal{L}_{Y}$ acts on scalars as $\iota_{Y} d$, from the quaternionic Kähler moment map equation it follows that $\mathcal{L}_{Y} \nu_{X i}=\nu_{[X, Y] i}-2 \varepsilon_{i j k}\left(\iota_{Y} \theta_{j}+\nu_{Y j}\right) \nu_{X k}$, showing that the sections $\nu_{X i}$ transform indeed equivariantly under the infinitesimal action of $G$. \(\square\)
1.2.8. In the hyperkähler limit the coefficients $\vec{\nu}_{X}$ lose the moment map interpretation and become constant.

Theorem 8. Let $M$ be a hyperkähler manifold having a continuous group of isometries $G$, with Lie algebra $\mathfrak{g}$. Then a vector field $X \in \mathfrak{g}$, that is $X$ is Killing, if and only if there exists a constant map $\nu: M \longrightarrow \mathfrak{g}^{*} \otimes \mathbb{R}^{3}$ such that
$$\mathcal{L}_{X} \vec{\omega}=-2 \vec{\nu}_{X} \times \vec{\omega} .$$
Explicitly, the map is given by the formula $\vec{\nu}_{X}=-\langle\vec{I}, \nabla X\rangle$ and, for any $X, Y \in \mathfrak{g}$, we have
$$2 \vec{\nu}_{[X, Y]}=2 \vec{\nu}_{X} \times 2 \vec{\nu}_{Y} .$$
Moreover, if $M$ is compact, $\nu$ vanishes entirely.
Proof. The proof in the quaternionic Kähler case carries over in the limit when $s$ and $\vec{\theta}$ vanish, apart from the three instances identified in the intermediary Remark. In particular, equation (44) now reads simply $d \vec{\nu}_{X}=0$, implying that the functions $\vec{\nu}_{X}$ are constant in hyperkähler setting (note also that rather than being local sections, they are now globally defined). This equation no longer has the form of a moment map condition, nor does it imply anymore the rotation property. As for the remaining equations, (43) and (45), they take in this limit, with less dramatic consequences, the forms (48) and (49), respectively. Finally, the last statement of Theorem 6 implies that, when $M$ is compact, $\nabla X^{\mathfrak{s p}(1)}=0$ for any $X \in \mathfrak{g}$. \(\square\)

Killing vector fields $X$ for which $\vec{\nu}_{X}$ vanishes are known as tri-Hamiltonian (or triholomorphic), and the ones for which this is not the case as rotational (or permuting). (Note that the two notions do not depend on the particular frame chosen in the space of hyperkähler symplectic 2-forms.) So the theorem states that Killing vector fields on hyperkähler manifolds can only be either of tri-Hamiltonian or of rotational type. This generalizes a result proved by other means in four dimensions by Boyer and Finley [11]. In particular, when the manifold is compact, Killing vector fields, should they exist, are necessarily tri-Hamiltonian.
1.3. Homothetic Euler vector fields. We end this section with an examination of a different type of symmetry, conformal in nature rather than Killing, which plays a central role in Swann's celebrated quaternionic bundle construction, reviewed in the next section.

Consider a Riemannian or pseudo-Riemannian manifold $M$ with Levi-Civita connection ∇ We call a vector field $X$ on $M$ homothetic Euler if
$$\nabla_{Y} X=Y$$
for any vector field $Y \in T M$. In the notation of subsection 1.2 this is equivalent to requiring that $\nabla X$ be equal to the identity endomorphism of $T M$. The terminology is justified by the fact that a manifold $M$ possessing such a vector field is automatically a metric cone [28], in which context the vector field is known as an Euler vector field.

A vector field is homothetic Euler if and only if it is homothetic and hypersurface-orthogonal. In fact, we have the following list of equivalent characterizations:

Proposition 9. Let $M$ be a Riemannian or pseudo-Riemannian manifold with metric $g$ and corresponding Levi-Civita connection ∇ . Then the following conditions are equivalent:
\begin{itemize}
\item[a)] $M$ possesses a homothetic Euler vector field $X$.
\item[b)] There exists a function $\kappa$ on $M$ such that $g=\nabla^{2} \kappa$.
\item[c)] There exists a function $\kappa$ on $M$ such that its gradient vector field with respect to the metric, $\iota_{X} g=d \kappa$, satisfies the homothetic property $\mathcal{L}_{X} g=2 g$.
\end{itemize}
If $M$ is assumed in addition to be hyperkähler, then we can add to this list the conditions
\begin{itemize}
\item[d)] There exists a function $\kappa$ on $M$ which is simultaneously a Kähler potential for every hyperkähler Kähler 2-form with respect to its corresponding complex structure, i.e.
\end{itemize}
$$\omega_{i}=\frac{1}{2} d\left(d \kappa I_{i}\right) .$$
\begin{itemize}
\item[e)] There exist four vector fields $X, X_{1}, X_{2}, X_{3} \in T M$ and a function $\kappa$ on $M$ such that
\end{itemize}
$$\iota_{X_{i}} \omega_{j}=\varepsilon_{i j k} \iota_{X} \omega_{k}-\delta_{i j} d \kappa \quad \text { and } \quad \mathcal{L}_{X} \omega_{k}=2 \omega_{k} .$$
Remark. A hyperkähler manifold $M$ with this structure is known as a hyperkähler cone. Due to the property ( $d$ ) the function $\kappa$ is called in this context a hyperkähler potential. Homothetic Euler vector fields were first introduced in a physical setting in relation to theories of $N=2$ hypermultiplets in four spacetime dimensions invariant under superconformal symmetries by de Wit, Kleijn and Vandoren in [19] (see also [20]). The characterizations $(b)$ and $(d)$ precede this definition and are due to Swann [46]. Through the property $(e)$, involving exterior algebra conditions on the hyperkähler symplectic 2-forms, we add to this collection of characterizations one which is closest in spirit to the approach that we have developed in these notes.

Proof. We begin with the case when $M$ is simply Riemannian or pseudo-Riemannian, with metric $g$ and Levi-Civita connection ∇ . Let us recall, first, that for any $X, Y, Z \in T M$ we have the identity $\left(\mathcal{L}_{X} g\right)(Y, Z)=g\left(\nabla_{Y} X, Z\right)+g\left(\nabla_{Z} X, Y\right)$. And, second, that for any function $\kappa$, its Hessian tensor is given by $\nabla_{Y, Z}^{2} \kappa=g\left(\nabla_{Y} X, Z\right)$ for any $Y, Z \in T M$, where $X$ represents now the gradient vector field of $\kappa$ with respect to the metric; this formula holds in fact for any metric-preserving affine connection.
$a) \Rightarrow b), c$ ) Assuming the condition $(a)$ holds, define the function
$$\kappa=\frac{1}{2} g(X, X) .$$
Then, for any vector field $Y \in T M$ we have $\nabla_{Y} \kappa=g\left(X, \nabla_{Y} X\right)=g(X, Y)$, which is to say, $X$ is the gradient of $\kappa$ with respect to the metric. The first and second identities above imply then immediately the conditions $(c)$ and (b), respectively.
$b) \Rightarrow a$ ) Let in this case $X$ be, by definition, the gradient vector field of the function $\kappa$ with respect to the metric. The implication follows then promptly from the Hessian formula above.
$c) \Rightarrow a$ ) The homothetic condition $\mathcal{L}_{X} g=2 g$ implies on one hand, by way of the first Levi-Civita identity above, that $g\left(\nabla_{Y} X, Z\right)+g\left(\nabla_{Z} X, Y\right)=2 g(Y, Z)$ for any $Y, Z \in T M$. On another hand, from the symmetry of the Hessian tensor it follows, by way of the second identity, that $g\left(\nabla_{Y} X, Z\right)=g\left(\nabla_{Z} X, Y\right)$. One gets then that $g\left(\nabla_{Y} X, Z\right)=g(Y, Z)$ for any $Y, Z \in T M$, which then by the fact that the metric $g$ is non-degenerate implies the condition (a).

Let us assume now that the manifold $M$ is, moreover, hyperkähler.
$b) \Rightarrow d)$ We have in this case $\omega_{i}(Y, Z)=g\left(Y, I_{i} Z\right)=\nabla_{Y, I_{i}}^{2} \kappa=\nabla_{Y} \nabla_{Z} \kappa-\nabla_{\nabla_{Y}\left(I_{i} Z\right)} \kappa$, for any $Y, Z \in T M$. Since the hyperkähler complex structures are preserved individually by the Levi-Civita connection we can replace the last term (ignoring the sign) with $\nabla_{I_{i} \nabla_{Y} Z^{\kappa}}$. In differential form language, the result can be written rather more nicely in the form $\omega_{i}=\frac{1}{2} d_{\nabla}\left(d \kappa I_{i}\right)$. As the Levi-Civita connection is torsion-free, which translates into an index symmetry for the Christoffel symbols, we can eventually replace in this expression $d_{\nabla}$ with the usual exterior derivative, $d$.
$d) \Rightarrow e)$ Given the potential function $\kappa$ on $M$, define the vector fields $X, X_{1}, X_{2}, X_{3}$ as the gradients of $\kappa$ with respect to the metric respectively the three hyperkähler symplectic forms, as follows:
$$\iota_{X_{1}} \omega_{1}=\iota_{X_{2}} \omega_{2}=\iota_{X_{3}} \omega_{3}=-\iota_{X} g=-d \kappa .$$
By using the quaternionic properties of the hyperkähler complex structures we get then that $\iota_{X_{1}} \omega_{2}=-\iota_{X_{1}} \omega_{1} I_{3}=\iota_{X} g I_{3}=\iota_{X} \omega_{3}$. Cyclically permuting the indices in this last argument yields a set of formulas which, together with the definitions of the four vector fields, can be assembled in the form of the first condition (52). To obtain the second condition (52), on the other hand, note that we have $\iota_{X} \omega_{i}=\iota_{X} g I_{i}=d \kappa I_{i}$. Then $\mathcal{L}_{X} \omega_{i}=d \iota_{X} \omega_{i}=d\left(d \kappa I_{i}\right)=2 \omega_{i}$.
$e) \Rightarrow c)$ Consider, say, the following off-diagonal component of the first condition (52): $\iota_{X_{1}} \omega_{2}=\iota_{X} \omega_{3}$. From this it follows that $X_{1}=\iota_{X} \omega_{3} \omega_{2}^{-1}=\omega_{2}^{-1} \omega_{3} X=-I_{1} X$, where in the last step we made use of the second expression for $I_{1}$ in (15). Cyclically permuting the indices in this argument gives us
$$X_{i}=-I_{i} X .$$
Substituting this back into the condition we get then from the diagonal components that $\iota_{X} g=d \kappa$. On another hand, the second condition (52) implies immediately by way of any
one of the expressions (16) for the metric that $\mathcal{L}_{X} g=2 g$. This concludes the proof of the chain of equivalences. \(\square\)

Hyperkähler cones are naturally foliated by four-dimensional leaves. More precisely, we have:

Proposition 10. Let $M$ be a hyperkähler cone. Then the four vector fields $X, X_{1}, X_{2}, X_{3}$ at point (e) of Proposition 9 generate the $\mathbb{R} \oplus \mathfrak{s p}(1)$ algebra
$$\left[X_{i}, X_{j}\right]=2 \varepsilon_{i j k} X_{k} \quad\left[X_{i}, X\right]=0$$
with $X$ homothetic Euler and $X_{1}, X_{2}, X_{3}$ Killing vector fields of rotating type.
Proof. Acting with an exterior derivative on the first condition (52) and using the closure of the $\omega_{i}$ to pass to Lie derivatives by way of Cartan's homotopy formula we get that
$$\mathcal{L}_{X_{i}} \omega_{j}=2 \varepsilon_{i j k} \omega_{k} .$$
This means that each one of the vector fields $X_{1}, X_{2}, X_{3}$ generates a rotational action on $M$ and is therefore Killing. We then have
$$\begin{aligned}
\iota_{\left[X_{i}, X_{j}\right]} \omega_{l} & =\left(\iota_{X_{i}} \mathcal{L}_{X_{j}}-\iota_{X_{j}} \mathcal{L}_{X_{i}}+\left[d, \iota_{X_{i}} \iota_{X_{j}}\right]\right) \omega_{l} \\
& =2 \varepsilon_{j l k} \iota_{X_{i}} \omega_{k}-2 \varepsilon_{i l k} \iota_{X_{j}} \omega_{k}-2 \varepsilon_{i j l} d \kappa
\end{aligned}$$
where we used that $\omega_{l}\left(X_{i}, X_{j}\right)=g\left(I_{i} X, I_{l} I_{j} X\right)=-g\left(X, I_{i} I_{l} I_{j} X\right)=\varepsilon_{i l j} g(X, X)=-2 \varepsilon_{i j l} \kappa$, as well as the closure of $\omega_{l}$; resorting again to the first condition (52) and the Jacobi property of the $\varepsilon$-symbol returns in the end
$$=2 \varepsilon_{i j k} \iota_{X_{k}} \omega_{l} .$$
Since the $\omega_{l}$ are non-degenerate, this is equivalent to the first algebraic condition (56). The remaining condition (56) can be derived by a similar argument. \(\square\)

\section*{2. Swann bundles}

In [46] Swann introduced a powerful tool for the study of quaternionic Kähler manifolds by showing that over each such manifold one can construct a quaternionic bundle whose total space carries a hyperkähler cone structure encoding the quaternionic Kähler geometry of the base. This allows one to describe the geometry of manifolds which in general have no integrable complex structures, apart perhaps from accidental ones inessential to their quaternionic Kähler structure, in terms of the hyperkähler geometry of a space of four real dimensions higher possessing a wealth of integrable complex structures. Before we proceed to review the details of Swann's construction it is useful to recall a few facts about (a $\mathbb{Z}_{2}$ quotient of) the multiplicative group of non-zero quaternions, $\mathbb{H}^{\times}$, which plays a key role in this story.
2.1. Two structures on the group $\mathbb{H}^{\times} / \mathbb{Z}_{2}$.
2.1.1. Consider an embedding of the group $\operatorname{Sp}(1)$ of unitary quaternions into $\mathbb{H}^{\times}$. Clearly, every non-zero quaternion can be uniquely represented as a positive real number, its abso-
lute value, times a unit quaternion; this gives a natural isomorphism
$$\mathbb{H}^{\times} \cong \mathbb{R}^{+} \otimes \operatorname{Sp}(1) .$$
Thus, $\mathbb{H}^{\times}$has the structure of a Lie group, with Lie algebra generated by the standard quaternionic basis 1, i, j, k. In what follows we will denote the elements of this basis uniformly with $u_{0}, u_{1}, u_{2}, u_{3}$, respectively - or, simply, $u_{a}$. The indices $a, b, \ldots$ will be assumed to run from 0 to 3 while the indices $i, j, k, \ldots$ to run, as until now, from 1 to 3, and the summation convention over repeated indices will continue to be implied.

The adjoint representation of $\mathbb{H}^{\times}$is four-dimensional and defined by $q^{-1} u_{a} q=R_{a b}(q) u_{b}$, for any $q \in \mathbb{H}^{\times}$. It satisfies the properties
$$\begin{aligned}
& \text { 1. } R_{a b}(\lambda q)=R_{a b}(q) \text { for any } \lambda \in \mathbb{R}^{\times} \\
& \text {2. } R_{a b}\left(q^{-1}\right)=R_{b a}(q) \text {. }
\end{aligned}$$
The first one follows immediately from the definition. Taking in it in particular $\lambda=1 /|q|$ and $\lambda=-1$, one can see that the adjoint representation descends to a representation of the rotation group $S O(3)$, whose double cover is $S p(1)$. This is reducible: one can write it in block-diagonal form as the direct sum of the one-dimensional trivial representation and the three-dimensional irreducible representation $R_{i j}(q)$ of $S O(3)$. On the other hand, by the associativity of quaternionic multiplication and the multiplicative property of the norm, $\left|u_{a}\right|=\left|q^{-1} u_{a} q\right|=\left|R_{a b}(q) u_{b}\right|$, which is to say, adjoint transformations preserve the quaternionic norm. They preserve hence also the associated inner product, and the second relation is the expression of this orthogonality property.

The Lie algebra (i.e. quaternion)-valued left and right-invariant Cartan-Maurer 1-forms of $\mathbb{H}^{\times}$are given by
$$\sigma^{L}=q^{-1} d q=\sigma_{a}^{L} u_{a} \quad \sigma^{R}=q d q^{-1}=\sigma_{a}^{R} u_{a}$$
for any element $q \in \mathbb{H}^{\times}$. Thus defined, each of these satisfy the same set of Cartan-Maurer equations, which in components read
$$\begin{array}{ll}
d \sigma_{i}^{L}+\varepsilon_{i j k} \sigma_{j}^{L} \wedge \sigma_{k}^{L}=0 & d \sigma_{i}^{R}+\varepsilon_{i j k} \sigma_{j}^{R} \wedge \sigma_{k}^{R}=0 \\
d \sigma_{0}^{L}=0 & d \sigma_{0}^{R}=0 .
\end{array}$$
The left and right-invariant Cartan-Maurer 1-forms are related to each other by an adjoint transformation up to a minus sign: $\sigma_{a}^{L}=-R_{a b}\left(q^{-1}\right) \sigma_{b}^{R}$. Note that in particular we have
$$\sigma_{0}^{L}=-\sigma_{0}^{R}=\frac{d|q|^{2}}{2|q|^{2}} .$$
---
retention_scope: session
part: 1
total_parts: 1
---

---
source_file: 1102_1518.pdf
converter: mathpix
format: mmd
---

\title{
BIANCHI TYPE A HYPER-SYMPLECTIC AND HYPER-KÄHLER METRICS IN 4D
}

\author{
L.C. DE ANDRÉS, M. FERNÁNDEZ, S. IVANOV, J.A. SANTISTEBAN, L. UGARTE, AND D. VASSILEV
}

\begin{abstract}
We present a simple explicit construction of hyper-Kähler and hyper-symplectic (also known as neutral hyper-Kähler or hyper-parakähler) metrics in 4D using the Bianchi type groups of class A. The construction underlies a correspondence between hyper-Kähler and hyper-symplectic structures in dimension four.
\end{abstract}

\section*{Contents}
\begin{itemize}
\item[1.] Introduction
\item[2.] Hyper-Kähler metrics in dimension four
\item[2.1.] The group $S U(2)$, Bianchi type $I X$
\item[2.2.] The group $S U(1,1)$, Bianchi type $V I I I$
\item[2.3.] The Heisenberg group $H^{3}$, Bianchi type $I I$, Gibbons-Hawking class
\item[2.4.] Rigid motions of euclidean 2-plane-Bianchi $V I I_{0}$
\item[2.5.] Rigid motions of Lorentzian 2-plane-Bianchi type $V I_{0}$
\item[2.6.] Contractions
\item[3.] Hyper symplectic metrics in dimension 4
\item[3.1.] Bianchi type $I X$ hyper-symplectic metrics and hyper-Kähler Bianchi type $V I I I$ hyper-Kähler metrics
\item[3.2.] Bianchi type $V I I I$ hyper-symplectic metrics and hyper-Kähler Bianchi type $I X$ hyper-Kähler metrics
\item[3.3.] Bianchi type $I I$ hyper-symplectic metrics and hyper-Kähler Bianchi type $I I$ hyper-Kähler metrics
\item[3.4.] Bianchi type $V I I_{0}$ hyper-symplectic metrics and hyper-Kähler Bianchi type $V I_{0}$ metrics
\item[3.5.] Bianchi type $V I_{0}$ hyper-symplectic metrics and hyper-Kähler Bianchi type $V I I_{0}$ metrics
\item[4.] Conclusions
\end{itemize}

References

\section*{1. Introduction}

Manifolds carrying a hyper-symplectic structure are the pseudo-Riemannian counterpart to hyper-Kähler manifolds. They are defined as follows. An almost hyper-paracomplex structure on a $4 n$-dimensional manifold $M$ is a triple $\left(J, P_{1}, P_{2}\right)$ of anticommuting endomorphisms of the tangent bundle of $M$ satisfying the paraquaternionic identities
$$J^{2}=-P_{1}^{2}=-P_{2}^{2}=-I d, \quad J P_{1}=P_{2} .$$
In this case, $\left(M, J, P_{1}, P_{2}\right)$ is said to be an almost hyper-paracomplex manifold. Moreover, if $g$ is a pseudo-Riemannian metric on $\left(M, J, P_{1}, P_{2}\right)$ for which $J$ is an isometry while $P_{1}$ and $P_{2}$ are anti-isometries, then $g$ is called an almost hyper-parahermitian metric. Necessarily $g$ is a neutral metric, that is, of signature $(2 n, 2 n)$. Such a metric gives rise to three 2-forms on $M$ defined in a way similar to the Kähler forms in the positive definite case (see Sections 2 and 3 for details). When these three forms are closed, the structure $\left(g, J, P_{1}, P_{2}\right)$

\footnotetext{
Date: June 8, 2018.
2000 Mathematics Subject Classification. 58J60, 53C26, 53C50.
Key words and phrases. hyper-symplectic structures, hyper-parakähler metrics, hyper-Kähler metrics.
}
is called hyper-symplectic [28]. In this case the structures ( $J, P_{1}, P_{2}$ ) are parallel with respect to the Levi-Civita connection of the neutral metric $g$ [2, 28, 13] and, in particular, integrable. Metrics associated to a hyper-symplectic structure are also called neutral hyper-Kähler [34], para-hyperkähler [6], hyper-parakähler [32], etc.

Manifolds with a hyper-symplectic structure have also a rich geometry. Indeed, the neutral metric is Kähler, Ricci flat and its holonomy group is contained in $\operatorname{Sp}(2 n, \mathbb{R})$ [28]. Furthermore, in dimension four, any hyper-symplectic structure underlies an anti-self-dual and Ricci-flat neutral metric. For this reason such structures have been used in string theory [42, 30, 33, 3, 31, 10, 26] and integrable systems [16, 4, 17]. In fact, in [42] is considered $N=2$ superstring theory, and it is proved that the critical dimension of such a string is 4 and that the bosonic part of the $N=2$ theory corresponds to self-dual metrics of signature (2, 2).

There are not known many explicit hyper-symplectic metrics. In dimension four they were described in [14, 43, 35, 26]. In higher dimensions, hyper-symplectic structures on a class of compact quotients of 2-step nilpotent Lie groups were exhibited in [19]. Also, in [1] is given a procedure to construct hyper-symplectic structures on $\mathbb{R}^{4 n}$ with complete and not necessarily flat associated neutral metrics.

On the other hand, Bourliot, Estes, Petropoulos and Spindel in [8] (see also [7]) show a classification of self-dual four-dimensional gravitational instantons. Their classification is based on the algebra homomorphisms relating the Bianchi group and the group $S O(3)$. In [7] it is noticed that the groups $V I_{0}$ and $V I I I$ of Bianchi classification seem not interesting for gravitational instantons taking into account their complex nature, but they may play a more physical role in the context of neutral hyper-Kähler metrics.

In this paper, following an idea originally proposed by Hitchin [29], we re-construct in a simple way the well known (cohomogeneity-one) hyper-Kähler metrics in dimension four arising from the three-dimensional groups of Bianchi type A and give explicit construction of hyper-symplectic metrics of signature $(2,2)$ (that is, of signature (+, +, -, -)) some of which seem to be new. We follow Hitchin's idea [29] reducing the problem to a solution of a certain system of evolution equations applying two results of Hitchin, which assert that an almost hyper-Hermitian structure (resp. an almost para-hyperhermitian structure) is hyper-Kähler (resp. hyper-symplectic) exactly when the three Kähler forms are closed [27] (resp. [28]). In this way we recover some of the known (Bianchi-type) hyper-Kähler metrics in dimension four 38, 39, 37, 18, 22, 5, 24, 20, 21, 25, 3, 40, 15, 12, 44]. Our approach seems to be particularly simple and leads quickly to the explicit form of the considered metrics. In [35] it was discovered a correspondence between Bianchi type $I X$ hyper-Kähler metric and Bianchi type VIII hyper-symplectic metric. Our construction shows that the system of evolution equations describing the hyper-Kähler metrics of Bianchi types $I X, V I I I, V I I_{0}, V I_{0}, I I$ coincides with the system describing hyper-symplectic metrics of Bianchi types $V I I I, I X, V I_{0}, V I I_{0}, I I$, respectively. This extends the correspondence found in [35] between hyper-Kähler and hyper-symplectic metrics arising from three dimensional groups $S U(2)$ and $S U(1,1)$ to a correspondence between hyper-Kähler and hyper-symplectic metrics arising from the three dimensional groups of Lorentzian and Euclidean motions and the Heisenberg group, respectively.

Convention 1.1. The triple $(i, j, k)$ denotes any cyclic permutation of $(1,2,3)$.
Acknowledgments The research was initiated during the visit of the third author to the Abdus Salam ICTP, Trieste as a Senior Associate, Fall 2008. He also thanks ICTP for providing the support and an excellent research environment. S.I. is partially supported by the Contract 181/2011 with the University of Sofia 'St.Kl.Ohridski'. S.I and D.V. are partially supported by Contract "Idei", DO 02-257/18.12.2008 and DID 02-39/21.12.2009. This work has been also partially supported through grant MCINN (Spain) MTM2008-06540-C02-01/02. Thanks are due also to the referees for valuable comments improving the clarity of the paper.

\section*{2. Hyper-Kähler metrics in dimension four}

In this section we recover some of the known hyper-Kähler metrics in dimension four. To this end, we lift the special structure on the non-Euclidean Bianchi type groups of class A to a hyper-Kähler metric on its product with (an interval in) the real line.

Let us recall firstly that an almost hypercomplex structure on a $4 n$ dimensional manifold $M$ is a triple $\left(J_{1}, J_{2}, J_{3}\right)$ of almost complex structures on $M$ satisfying the quaternionic identities, that is,
$$J_{1}^{2}=J_{2}^{2}=J_{3}^{2}=-1, \quad J_{1} J_{2}=-J_{2} J_{1}=J_{3} .$$
An almost hypercomplex manifold $\left(M, J_{1}, J_{2}, J_{3}\right)$ is said to be almost hyper-Hermitian if there exists a Riemannian metric $g$ on $M$ for which each of the almost complex structures $J_{s}, s=1,2,3$, is an isometry, that is, they satisfy the compatibility conditions
$$g\left(J_{s} \cdot, J_{s} \cdot\right)=g(\cdot, \cdot), \quad s=1,2,3 .$$
In this case, we can define the fundamental 2-forms $F_{s}$ of the almost hyper-Hermitian manifold $\left(M, g, J_{1}, J_{2}, J_{3}\right)$ by
$$F_{s}(\cdot, \cdot)=g\left(J_{s} \cdot, \cdot\right), \quad s=1,2,3 .$$
When the structures $J_{s}, s=1,2,3$, are parallel with respect to the Levi-Civita connection, $\left(M, g, J_{1}, J_{2}, J_{3}\right)$ is said to be a hyper-Kähler manifold. A result of Hitchin [27] states that the fundamental 2-forms are closed exactly when the almost hyper-Hermitian structure is hyper-Kähler.

Let $G$ be a three dimensional Lie group and let $\left\{e^{1}(t), e^{2}(t), e^{3}(t)\right\}$ be a global basis of 1-forms on $G$ for each $t \in I$, where $I \subset \mathbb{R}$ is a connected interval in the real line. We consider the almost hyper-Hermitian structure on $G \times I$ defined by the following fundamental 2-forms
$$\begin{aligned}
& F_{1}=e^{1}(t) \wedge e^{2}(t)+e^{3}(t) \wedge f(t) d t, \\
& F_{2}=e^{1}(t) \wedge e^{3}(t)-e^{2}(t) \wedge f(t) d t, \\
& F_{3}=e^{2}(t) \wedge e^{3}(t)+e^{1}(t) \wedge f(t) d t,
\end{aligned}$$
where $f(t)$ is function of $t \in I$ which does not vanish. Using $\left\{e^{1}(t), e^{2}(t), e^{3}(t), f(t) d t\right\}$ as a positively oriented orthonormal basis the fundamental 2-forms are self-dual (SD). When $M$ is hyper-Kähler it is necessarily anti-self-dual (ASD) and Ricci flat. With the help of Hitchin's theorem [27], it is straightforward to prove the next basic for our purposes result.

Proposition 2.1. The almost hyper-Hermitian structure $\left(F_{1}, F_{2}, F_{3}\right)$ is hyper-Kähler if and only if
$$d e^{12}\left(t_{0}\right)=d e^{13}\left(t_{0}\right)=d e^{23}\left(t_{0}\right)=0,$$
for some $t_{0} \in I$, and the following evolution equations hold
$$\frac{\partial}{\partial t} e^{i j}(t)=-f(t) d e^{k}(t) .$$
Here, $\{i, j, k\}$ denotes an even permutation of $\{1,2,3\}$ and $e^{i j}(t)=e^{i}(t) \wedge e^{j}(t)$.
The hyper-Kähler metric is given by
$$g=\left(e^{1}(t)\right)^{2}+\left(e^{2}(t)\right)^{2}+\left(e^{3}(t)\right)^{2}+f^{2}(t) d t^{2} .$$
Proof. Taking the exterior derivatives in (2.2) and separating the variables, we obtain
$$\begin{aligned}
d F_{1} & =d e^{12}(t)+\left[\frac{\partial}{\partial t} e^{12}(t)+f(t) d e^{3}(t)\right] \wedge d t, \\
d F_{2} & =d e^{13}(t)+\left[\frac{\partial}{\partial t} e^{13}(t)-f(t) d e^{2}(t)\right] \wedge d t, \\
d F_{3} & =d e^{23}(t)+\left[\frac{\partial}{\partial t} e^{23}(t)+f(t) d e^{1}(t)\right] \wedge d t .
\end{aligned}$$
The equations (2.6) imply that all the three 2-forms $F_{i}$ are closed precisely when (2.4) holds and $d e^{12}(t)=$ $d e^{13}(t)=d e^{23}(t)=0$ for all $t \in I$. The latter condition is equivalent to (2.3) because by (2.4) we have that $\frac{\partial}{\partial t}\left(d e^{i j}(t)\right)=d\left(f(t) d e^{k}(t)\right)=f(t) d^{2} e^{k}(t)=0$ for all $t$, that is, $d e^{i j}(t)$ is constant on the connected interval $I$. Finally, Hitchin theorem [27] completes the proof. \(\square\)

In the next table we recall the Bianchi classification [36] (up to isomorphism) of the three dimensional Lie algebras using $d e^{1}=-b_{1} e^{23}, d e^{2}=-a e^{12}-b_{2} e^{31}$, and $d e^{3}=-b_{3} e^{12}+a e^{31}$.

\begin{table}
\begin{tabular}[t]{|l|l|l|l|l|l|l|l|l|l|l|l|}
\hline Type & $I$ & II & $V I_{0}$ & $V I I_{0}$ & VIII & IX & $V$ & IV & $V I I_{a}, a>0$ & III & $V I_{a}, 0<a \neq 1$ \\
\hline $a$ & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 1 & $a$ & 1 & $a$ \\
\hline $b_{1}$ & 0 & 0 & 0 & 0 & 1 & 1 & 0 & 0 & 0 & 0 & 0 \\
\hline $b_{2}$ & 0 & 0 & 1 & 1 & 1 & 1 & 0 & 0 & 1 & 1 & 1 \\
\hline $b_{3}$ & 0 & 1 & -1 & 1 & -1 & 1 & 0 & 1 & 1 & -1 & -1 \\
\hline $G$ & Abelian & Heisenberg a.k.a. Nil & Poincare a.k.a. Lorentzian motions & Euclidean motions & Lorentz $S U(1,1)$ & Rotations $S U(2)$ & & & & & \\
\hline & \multicolumn{6}{|c|}{type A (unimodular)} & \multicolumn{5}{|c|}{type B (non-unimodular)} \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 1. Bianchi classification}
\end{table}

Our goal is to seek the explicit solution of the system given in the previous proposition for each of the three dimensional Bianchi type groups. We will consider the class of left-invariant evolutions, that is to say, $\left\{e^{1}(t), e^{2}(t), e^{3}(t)\right\}$ is a basis of $\mathfrak{g}^{*}$ for all $t \in I, \mathfrak{g}$ being the Lie algebra of $G$, i.e., for some function $c_{j}^{i}(t)$ we have
$$e^{i}(t)=c_{1}^{i}(t) e^{1}+c_{2}^{i}(t) e^{2}+c_{3}^{i}(t) e^{3}, \quad i=1,2,3,$$
with four-dimensional metric (2.5) taking the form $g=f^{2}(t) d t^{2}+c_{i}^{k}(t) c_{j}^{k}(t) e^{i} \odot e^{j}$. This special class of evolutions restricts the applicability of our method to the groups of type A.

Lemma 2.2. Let $\left\{e^{1}(t), e^{2}(t), e^{3}(t)\right\}$ be a basis of left-invariant 1-forms on $G$ for each $t \in I$. Then, (2.3) is satisfied if and only if the Lie group G is of Bianchi type A.

Proof. Let us fix the basis $\left\{e^{1}\left(t_{0}\right), e^{2}\left(t_{0}\right), e^{3}\left(t_{0}\right)\right\}$ of $\mathfrak{g}^{*}$. Then, there are constants $c_{j}^{i} \in \mathbb{R}$ such that
$$e^{i}\left(t_{0}\right)=c_{1}^{i} e^{1}+c_{2}^{i} e^{2}+c_{3}^{i} e^{3}, \quad i=1,2,3,$$
where $\left\{e^{1}, e^{2}, e^{3}\right\}$ denotes the basis of $\mathfrak{g}^{*}$ given in Table 1, i.e. satisfying $d e^{1}=-b_{1} e^{23}, d e^{2}=-a e^{12}-b_{2} e^{31}$ and $d e^{3}=-b_{3} e^{12}+a e^{31}$. Thus $e^{i j}\left(t_{0}\right)=c_{12}^{i j} e^{12}+c_{13}^{i j} e^{13}+c_{23}^{i j} e^{23}$, where $c_{r s}^{i j}=c_{r}^{i} c_{s}^{j}-c_{s}^{i} c_{r}^{j}$.

Since $d e^{12}=d e^{13}=0$ and $d e^{23}=-2 a e^{123}$, we have that condition (2.3) is equivalent to
$$0=d e^{i j}\left(t_{0}\right)=c_{23}^{i j} d e^{23}=-2 a c_{23}^{i j} e^{123}$$
for $(i, j)=(1,2),(1,3)$ and (2,3). Now, $G$ is of Bianchi type B if and only if $a \neq 0$, and therefore (2.3) is satisfied if and only if $c_{23}^{12}=c_{23}^{13}=c_{23}^{23}=0$. But, the latter condition implies $\operatorname{det}\left(c_{j}^{i}\right)=0$, which contradicts the fact that $\left\{e^{1}\left(t_{0}\right), e^{2}\left(t_{0}\right), e^{3}\left(t_{0}\right)\right\}$ is a basis. \(\square\)

In the following sub-sections for each of the Bianchi type A groups we explicitly solve the system of Proposition 2.1 under the restrictive assumption that the evolution of the invariant one forms is diagonal. Specifically, given a basis $\left\{e^{1}, e^{2}, e^{3}\right\}$ of $\mathfrak{g}^{*}$, we will consider the "diagonal" evolution
$$e^{1}(t)=f_{1}(t) e^{1}, \quad e^{2}(t)=f_{2}(t) e^{2}, \quad e^{3}(t)=f_{3}(t) e^{3},$$
where $f_{1}, f_{2}, f_{3}$ are non-vanishing functions of $t \in I$. The corresponding "diagonal" metric is given by
$$g=f_{1}^{2}\left(e^{1}\right)^{2}+f_{2}^{2}\left(e^{2}\right)^{2}+f_{3}^{2}\left(e^{3}\right)^{2}+f^{2} d t^{2} .$$
The function $f$ is introduced for convenience in order to identify the metrics obtained by our method with the known explicit examples of four dimensional hyper-Kähler metrics. We note explicitly that according to [43] a cohomogeneity-one Einstein metric whose general form is
$$g=d T^{2}+h_{i j}(T) e^{i} \odot e^{j}$$
can be assumed to be diagonal, $h_{i j}=0$ for $i \neq j$, when $\left\{e^{i}\right\}$ are the left invariant forms of a Bianchi type VIII or IX group - first one diagonalizes $\left(h_{i j}\right)$ at a time $T_{0}$ and then show that the Ricci flatness implies the vanishing of all off-diagonal terms. On the hand a diagonalization of $\left(h_{i j}\right)$ corresponds to a rotation of the matrix $\left(c_{j}^{i}\right)$ which in turn becomes a rotation of the fundamental 2-forms (2.1). Such a rotation might lead to non-closed 2-forms. Thus our assumption of a diagonal evolution is restrictive in all cases. Our next task is to consider case by case the Bianchi type A groups.
2.1. The group $S U(2)$, Bianchi type $I X$. Let $G=S U(2)=S^{3}$ be described by the structure equations
$$d e^{i}=-e^{j k} .$$
In terms of Euler angles, the left invariant 1-forms $e^{i}$ are given by
$$e^{1}=\sin \psi d \theta-\cos \psi \sin \theta d \phi, \quad e^{2}=\cos \psi d \theta+\sin \psi \sin \theta d \phi, \quad e^{3}=d \psi+\cos \theta d \phi .$$
We evolve the $S U(2)$ structure as in (2.8). Using (2.10) we reduce the evolution equations (2.4) to the following system of ODEs
$$\frac{d}{d t}\left(f_{1} f_{2}\right)=f f_{3}, \quad \frac{d}{d t}\left(f_{1} f_{3}\right)=f f_{2}, \quad \frac{d}{d t}\left(f_{2} f_{3}\right)=f f_{1} .$$
The system (2.12) is equivalent to the following "BGPP" system (see [5])
$$\frac{d}{d t} f_{1}=f \frac{f_{2}^{2}+f_{3}^{2}-f_{1}^{2}}{2 f_{2} f_{3}}, \quad \frac{d}{d t} f_{2}=f \frac{f_{3}^{2}+f_{1}^{2}-f_{2}^{2}}{2 f_{1} f_{3}}, \quad \frac{d}{d t} f_{3}=f \frac{f_{1}^{2}+f_{2}^{2}-f_{3}^{2}}{2 f_{1} f_{2}} .$$
The system (2.13) admits the triaxial Bianchi IX BGPP [5] hyper-Kähler metrics by taking $f=f_{1} f_{2} f_{3}$ and all $f_{i}$ different (see also [24]), and the Eguchi-Hanson [18] hyper-Kähler metric by letting two of the functions $f_{1}, f_{2}, f_{3}$ equal to each other.
2.1.1. The general solution. With the substitution $x_{i}=\left(f_{j} f_{k}\right)^{2}$, the system (2.12) becomes
$$\frac{d x_{i}}{d r}=2\left(x_{1} x_{2} x_{3}\right)^{1 / 4},$$
in terms of the parameter $d r=f d t$. Hence the functions $x_{i}$ differ by a constant, i.e., there is a function $x(r)$ such that $x(r)=x_{1}+a_{1}=x_{2}+a_{2}=x_{3}+a_{3}$. The equation for $x(r)$ is
$$\frac{d x}{d r}=2\left(\left(x-a_{1}\right)\left(x-a_{2}\right)\left(x-a_{3}\right)\right)^{1 / 4}, \text { i.e. } d r=\frac{1}{2} \frac{1}{\left(\left(x-a_{1}\right)\left(x-a_{2}\right)\left(x-a_{3}\right)\right)^{1 / 4}} d x .$$
If we let $h(x)=\frac{1}{2}\left(\left(x-a_{1}\right)\left(x-a_{2}\right)\left(x-a_{3}\right)\right)^{-1 / 4}$ and take into account $x_{i}=\left(f_{j} f_{k}\right)^{2}$, we see from (2.12) that the functions $f_{i}(x)$ satisfy
$$\frac{d}{d x}\left(\left(x-a_{i}\right)^{1 / 2}\right)=h(x) f_{i} .$$
Solving for $f_{i}$ we showed that the general solution of (2.12) is
$$f_{i}(x)=\frac{\left(x-a_{j}\right)^{1 / 4}\left(x-a_{k}\right)^{1 / 4}}{\left(x-a_{i}\right)^{1 / 4}}, \quad f(t)=h(x(t)) x^{\prime}(t), \quad h(x)=\frac{1}{2}\left(\left(x-a_{1}\right)\left(x-a_{2}\right)\left(x-a_{3}\right)\right)^{-1 / 4},$$
where $a_{1}, a_{2}$ and $a_{3}$ are constants, and $x$ is an auxiliary independent variable (substituting any function $x=x(t)$ gives a solution of (2.12) in terms of $t$ in an interval where $f$ and $f_{i}$, with $i=1,2,3$, do not vanish).

The resulting hyper-Kähler metric is given by (2.9) where the forms $e^{1}, e^{2}, e^{3}$ and the functions $f_{1}, f_{2}, f_{3}, f$ are given by (2.11) and (2.15), respectively.
2.1.2. Eguchi-Hanson instantons. A particular solution to (2.12) is obtained by taking $x=(t / 2)^{4}$ and $a_{1}=a_{2}=\frac{1}{16} a, a_{3}=0$, which gives
$$f_{1}=f_{2}=\frac{t}{2}, \quad f_{3}=\frac{1}{2 t}\left(t^{4}-a\right)^{\frac{1}{2}}, \quad f=\sqrt{\frac{t^{4}}{t^{4}-a}},$$
where $t \in(0, \infty)$ if $a \leq 0$, and $t \in\left(a^{\frac{1}{4}}, \infty\right)$ if $a>0$. This is the Eguchi-Hanson instanton [18] with the metric given by
$$g=\frac{t^{2}}{4}\left(\left(e^{1}\right)^{2}+\left(e^{2}\right)^{2}\right)+\frac{t^{4}-a}{4 t^{2}}\left(e^{3}\right)^{2}+\frac{t^{4}}{t^{4}-a}(d t)^{2}$$
where the 1 -forms $e^{1}, e^{2}, e^{3}$ can be found in (2.11).
2.1.3. Triaxial Bianchi type IX BGPP metrics [5]. If we perform the substitution $x=t^{4}, a_{1}=a^{4}, a_{2}=b^{4}$ and $a_{3}=c^{4}$ the metric of (2.15) turns into the triaxial Bianchi $I X$ metrics discovered in [5] (see also [24, 20, 21])
$$\begin{array}{ll}
f_{1}(t)=\frac{\left(t^{4}-b^{4}\right)^{\frac{1}{4}}\left(t^{4}-c^{4}\right)^{\frac{1}{4}}}{\left(t^{4}-a^{4}\right)^{\frac{1}{4}}}, & f_{2}(t)=\frac{\left(t^{4}-a^{4}\right)^{\frac{1}{4}}\left(t^{4}-c^{4}\right)^{\frac{1}{4}}}{\left(t^{4}-b^{4}\right)^{\frac{1}{4}}}, \\
f_{3}(t)=\frac{\left(t^{4}-a^{4}\right)^{\frac{1}{4}}\left(t^{4}-b^{4}\right)^{\frac{1}{4}}}{\left(t^{4}-c^{4}\right)^{\frac{1}{4}}}, & f(t)=\frac{2 t^{3}}{\left(t^{4}-b^{4}\right)^{\frac{1}{4}}\left(t^{4}-c^{4}\right)^{\frac{1}{4}}\left(t^{4}-a^{4}\right)^{\frac{1}{4}}} .
\end{array}$$
By [5] the above metrics are all singular (cannot be completed) with the only exception being the Euclidean flat space (when $a_{1}=a_{2}=a_{3}$ ) and the Eguchi-Hanson instanton, whose completion is the cotangent bundle of the complex projective line $\mathbb{C} P^{1}$. The latter example was extended to higher dimensions by Calabi [9]. In the derivation above we avoided the use of elliptic functions.

We note that the Atiyah-Hitchin class of complete hyper-Kähler metrics is not included in our derivation. In fact, by construction, the natural action of $S U(2)$ extends to a trivial action on the fundamental 2-forms, while it is known that in the Atiyah-Hitchin class the group $S U(2)$ rotates the self-dual forms [2].
2.2. The group $S U(1,1)$, Bianchi type $V I I I$. (Bianchi type $V I I I$ were investigated in [38, 39, 37].) Let $G=S U(1,1)$ be described by the structure equations
$$d e^{1}=-e^{23}, \quad d e^{2}=-e^{31}, \quad d e^{3}=e^{12} .$$
In terms of local coordinates the left invariant forms $e^{i}$ are given by
$$e^{1}=d \psi-\cos \theta d \phi, \quad e^{2}=\sinh \psi d \theta+\cosh \psi \sin \theta d \phi, \quad e^{3}=\cosh \psi d \theta+\sinh \psi \sin \theta d \phi .$$
We evolve the $S U(1,1)$ structure as in (2.8). Using the structure equations (2.19), we reduce the evolution equations (2.4) to the following system of ODEs
$$\frac{d}{d t}\left(f_{1} f_{2}\right)=-f f_{3}, \quad \frac{d}{d t}\left(f_{1} f_{3}\right)=f f_{2}, \quad \frac{d}{d t}\left(f_{2} f_{3}\right)=f f_{1} .$$
Solutions to the above system yield the hyper-Kähler metrics (2.5) found in [5].
2.2.1. Triaxial Bianchi type VIII metrics. Working as in 2.1.1, we obtain the next system for the functions $x_{i}$
$$\frac{d x_{2}}{d r}=\frac{d x_{1}}{d r}=2\left(x_{1} x_{2} x_{3}\right)^{1 / 4}, \quad \frac{d x_{3}}{d r}=-2\left(x_{1} x_{2} x_{3}\right)^{1 / 4} .$$
Solving for $f_{i}$, as in the derivation (2.15), we find that the general solution of (2.20) is
$$\begin{aligned}
& f_{1}(x)=\frac{\left(x-a_{2}\right)^{1 / 4}\left(a_{3}-x\right)^{1 / 4}}{\left(x-a_{1}\right)^{1 / 4}}, \quad f_{2}(x)=\frac{\left(x-a_{1}\right)^{1 / 4}\left(a_{3}-x\right)^{1 / 4}}{\left(x-a_{2}\right)^{1 / 4}}, \\
& f_{3}(x)=\frac{\left(x-a_{1}\right)^{1 / 4}\left(x-a_{2}\right)^{1 / 4}}{\left(a_{3}-x\right)^{1 / 4}}, \quad f(t)=h(x(t)) x^{\prime}(t), \quad h(x)=\frac{1}{2}\left(\left(x-a_{1}\right)\left(x-a_{2}\right)\left(a_{3}-x\right)\right)^{-1 / 4},
\end{aligned}$$
where $a_{1}, a_{2}$ and $a_{3}$ are constants, and $x$ is an auxiliary independent variable (substituting any function $x=x(t)$ gives a solution of (2.12) in terms of $t$ in an interval where $f$ and $f_{i}, i=1,2,3$, do not vanish).

The resulting hyper-Kähler metric is given by (2.9) where the forms $e^{1}, e^{2}, e^{3}$ and the functions $f_{1}, f_{2}, f_{3}, f$ are given by (2.19) and (2.21), respectively.

Taking $f=f_{1} f_{2} f_{3}$ and all $f_{i}$ different into (2.9), we obtain explicit expression of the triaxial Bianchi VIII solutions indicated in [5].

A particular solution is obtained by letting $a_{1}=a_{2}=0, a_{3}=\frac{a}{16}, x=(t / 2)^{4}$ which gives
$$f_{1}=f_{2}=\frac{1}{2}\left(a-t^{4}\right)^{\frac{1}{4}}, \quad f_{3}=\frac{t^{2}}{2}\left(a-t^{4}\right)^{-\frac{1}{4}}, \quad f=t\left(a-t^{4}\right)^{-\frac{1}{4}}, \quad 0<t^{4}<a .$$
The resulting hyper-Kähler metric is
$$g=\frac{\sqrt{a-t^{4}}}{4}\left(\left(e^{1}\right)^{2}+\left(e^{2}\right)^{2}\right)+\frac{t^{4}}{4 \sqrt{a-t^{4}}}\left(e^{3}\right)^{2}+\frac{t^{2}}{\sqrt{a-t^{4}}} d t^{2}$$
where the forms $e^{i}$ are given by (2.19).
2.3. The Heisenberg group $H^{3}$, Bianchi type $I I$, Gibbons-Hawking class. Consider the two-step nilpotent Heisenberg group $H^{3}$ defined by the structure equations
$$d e^{1}=d e^{2}=0, \quad d e^{3}=-e^{12}$$
where we can consider
$$e^{1}=d x, \quad e^{2}=d y, \quad e^{3}=d z-\frac{1}{2} x d y+\frac{1}{2} y d x,$$
with $x, y, z$ the global coordinates functions on $H^{3}$. Now, we evolve the structure of $H^{3}$ according to (2.8). The structure equations (2.22) reduce the evolution equations (2.4) to the following system of ODEs
$$\frac{d}{d t}\left(f_{1} f_{2}\right)=f f_{3}, \quad \frac{d}{d t}\left(f_{1} f_{3}\right)=0, \quad \frac{d}{d t}\left(f_{2} f_{3}\right)=0 .$$
Working as in the previous example, i.e., using the same substitutions we see that the function $x_{i}$ satisfy
$$\frac{d x_{3}}{d r}=2\left(x_{1} x_{2} x_{3}\right)^{1 / 4}, \quad \frac{d x_{1}}{d r}=\frac{d x_{2}}{d r}=0 .$$
The general solution of this system is
$$x_{1}=a, \quad x_{2}=b, \quad x_{3}=\left(\frac{3}{2}(a b)^{1 / 4} r+c\right)^{4 / 3},$$
where $a, b$ and $c$ are constants. Therefore, using again $f_{i}=\left(\frac{x_{j} x_{k}}{x_{i}}\right)^{1 / 4}$, the general solution of (2.24) is
$$\begin{aligned}
& f_{1}=\left(\frac{b}{a}\right)^{1 / 4}\left(\frac{3}{2}(a b)^{1 / 4} r+c\right)^{1 / 3}, \quad f_{2}=\left(\frac{a}{b}\right)^{1 / 4}\left(\frac{3}{2}(a b)^{1 / 4} r+c\right)^{1 / 3}, \\
& f_{3}=\frac{(a b)^{1 / 4}}{\left(\frac{3}{2}(a b)^{1 / 4} r+c\right)^{1 / 3}}, \quad f=r^{\prime}(t),
\end{aligned}$$
where $r=r(t)$ is an arbitrary function for $t$ in an interval where $f$ and $f_{i}, i=1,2,3$ do not vanish.
The resulting hyper-Kähler metric is given by (2.9) where the forms $e^{1}, e^{2}, e^{3}$ and the functions $f_{1}, f_{2}, f_{3}, f$ are given by (2.23) and (2.26), respectively.

A particular solution is obtained by taking $c=0$ and $a=b=1$ into (2.26), which gives
$$f_{1}=f_{2}=\lambda r^{1 / 3}, \quad f_{3}=f_{1}^{-1}$$
with $\lambda=\left(\frac{3}{2}\right)^{1 / 3}$. The substitution $t=\lambda^{2} r^{2 / 3}$ gives $f_{1}=f_{2}=f=t^{\frac{1}{2}}, \quad f_{3}=t^{-\frac{1}{2}}$, with $t>0$. This is the hyper-Kähler metric, first written in [37, 38],
$$g=t\left(d t^{2}+d x^{2}+d y^{2}\right)+\frac{1}{t}\left(d z-\frac{1}{2} x d y+\frac{1}{2} y d x\right)^{2},$$
belonging to the Gibbons-Hawking class [22] with an $S^{1}$-action and known also as Heisenberg metric [25] (see also [3, 40, 15, 12, 44]).
2.4. Rigid motions of euclidean 2-plane-Bianchi $V I I_{0}$. We consider the group $E_{2}$ of rigid motions of Euclidean 2-plane defined by the structure equations
$$\begin{array}{cc}
d e^{1}=0, & d e^{2}=e^{13}, \quad d e^{3}=-e^{12}, \quad \text { where we can consider } \\
e^{1}=d \phi, & e^{2}=\sin \phi d x-\cos \phi d y, \quad e^{3}=\cos \phi d x+\sin \phi d y .
\end{array}$$
We evolve the structure as in (2.8). Using the structure equations (2.27) we reduce the evolution equations (2.4) to the following system of ODE
$$\frac{d}{d t}\left(f_{1} f_{2}\right)=f f_{3}, \quad \frac{d}{d t}\left(f_{1} f_{3}\right)=f f_{2}, \quad \frac{d}{d t}\left(f_{2} f_{3}\right)=0 .$$

With the substitution $x_{i}=\left(f_{j} f_{k}\right)^{2}$, the above system becomes
$$\frac{d x_{1}}{d r}=0, \quad \frac{d x_{2}}{d r}=\frac{d x_{3}}{d r}=2\left(x_{1} x_{2} x_{3}\right)^{1 / 4},$$
in terms of the parameter $d r=f d t$. Hence, there is a function $x(r)$ and three constants $a_{1}, a_{2}, a_{3}$, such that, $x(r)=x_{2}+a_{2}=x_{3}+a_{3}, x_{1}=a_{1}$. The equation for $x(r)$ is
$$\frac{d x}{d r}=2\left(a_{1}\left(x-a_{2}\right)\left(x-a_{3}\right)\right)^{1 / 4}, \quad \text { i.e., } d r=\frac{1}{2} \frac{1}{\left(a_{1}\left(x-a_{2}\right)\left(x-a_{3}\right)\right)^{1 / 4}} d x .$$
If we let $h(x)=\frac{1}{2}\left(a_{1}\left(x-a_{2}\right)\left(x-a_{3}\right)\right)^{-1 / 4}$, and take into account $x_{i}=\left(f_{j} f_{k}\right)^{2}$, we see from (2.28) that the functions $f_{i}(x)$ satisfy
$$\frac{d}{d x}\left(\left(x-a_{i}\right)^{1 / 2}\right)=h(x) f_{i}, \quad i=2,3 .$$
Solving for $f_{i}$ we show that the general solution of (2.12) is
$$\begin{aligned}
& f_{1}(x)=\frac{\left(x-a_{2}\right)^{1 / 4}\left(x-a_{3}\right)^{1 / 4}}{a_{1}^{1 / 4}}, \quad f_{2}(x)=\frac{a_{1}^{1 / 4}\left(x-a_{3}\right)^{1 / 4}}{\left(x-a_{2}\right)^{1 / 4}}, \quad f_{3}(x)=\frac{a_{1}^{1 / 4}\left(x-a_{2}\right)^{1 / 4}}{\left(x-a_{3}\right)^{1 / 4}}, \\
& f(t)=h(x(t)) x^{\prime}(t), \quad h(x)=\frac{1}{2}\left(\left(a_{1}\left(x-a_{2}\right)\left(x-a_{3}\right)\right)^{-1 / 4},\right.
\end{aligned}$$
where $a_{1}, a_{2}$ and $a_{3}$ are constants, and $x$ is an auxiliary independent variable (substituting any function $x=x(t)$ gives a solution of (2.28) in terms of $t$ in an interval where $f$ and $f_{i}, i=1,2,3$, do not vanish).

The resulting hyper-Kähler metric is given by (2.9) where the forms $e^{1}, e^{2}, e^{3}$ and the functions $f_{1}, f_{2}, f_{3}, f$ are given by (2.27) and (2.30), respectively.

A particular vacuum solutions of Bianchi type $V I I_{0}$ is obtained by letting $f_{2}=f_{3}^{-1}$ and $f_{1}=f$, which gives
$$\frac{d}{d t}\left(f f_{3}^{-1}\right)=f f_{3}, \quad \frac{d}{d t}\left(f f_{3}\right)=f f_{3}^{-1}$$
with general solution of the form $f f_{3}+f f_{3}^{-1}=A e^{t}, f f_{3}^{-1}-f f_{3}=B e^{-t}$. Hence,
$$f=f_{1}=\frac{1}{2}\left(A e^{t}+B e^{-t}\right)^{\frac{1}{2}}\left(A e^{t}-B e^{-t}\right)^{\frac{1}{2}}, \quad f_{3}=f_{2}^{-1}=\left(A e^{t}+B e^{-t}\right)^{-\frac{1}{2}}\left(A e^{t}-B e^{-t}\right)^{\frac{1}{2}},$$
where $t>\frac{1}{2} \log \left|\frac{B}{A}\right|$ since $A^{2} e^{2 t}-B^{2} e^{-2 t}>0$. The resulting hyper-Kähler metric is
$$g=\frac{1}{4}\left(A^{2} e^{2 t}-B^{2} e^{-2 t}\right)\left(d t^{2}+d \phi^{2}+\frac{4}{\left(A e^{t}-B e^{-t}\right)^{2}}\left(e^{2}\right)^{2}+\frac{4}{\left(A e^{t}+B e^{-t}\right)^{2}}\left(e^{3}\right)^{2}\right),$$
where $e^{2}, e^{3}$ are given by (2.27). In particular, setting $A=B$ in (2.31) we obtain
$$g=\frac{A^{2}}{2} \sinh 2 t\left(d t^{2}+d \phi^{2}\right)+\operatorname{coth} t\left(e^{2}\right)^{2}+\tanh t\left(e^{3}\right)^{2}$$
which is the vacuum solutions of Bianchi type $V I I_{0}$ [37, 38] with group of isometries $E_{2}$ [25], (see also [44]).
2.5. Rigid motions of Lorentzian 2-plane-Bianchi type $V I_{0}$. Now we consider the group of rigid motions $E(1,1)$ of Lorentzian 2-plane defined by the structure equations and coordinates as follows
$$\begin{array}{ll}
d e^{1}=0, & d e^{2}=e^{13}, \quad d e^{3}=e^{12} \\
e^{1}=d \phi, & e^{2}=\sinh \phi d x+\cosh \phi d y, \quad e^{3}=\cosh \phi d x+\sinh \phi d y .
\end{array}$$
We evolve the structure as in (2.8). Using the structure equations (2.32), the evolution equations (2.4) give the following system of ODEs
$$\frac{d}{d t}\left(f_{1} f_{2}\right)=-f f_{3}, \quad \frac{d}{d t}\left(f_{1} f_{3}\right)=f f_{2}, \quad \frac{d}{d t}\left(f_{2} f_{3}\right)=0 .$$

The general solution of (2.33) is
$$\begin{aligned}
& f_{1}(x)=\frac{\left(x-a_{2}\right)^{1 / 4}\left(a_{3}-x\right)^{1 / 4}}{a_{1}^{1 / 4}}, \quad f_{2}(x)=\frac{a_{1}^{1 / 4}\left(a_{3}-x\right)^{1 / 4}}{\left(x-a_{2}\right)^{1 / 4}}, \quad f_{3}(x)=\frac{a_{1}^{1 / 4}\left(x-a_{2}\right)^{1 / 4}}{\left(a_{3}-x\right)^{1 / 4}}, \\
& f(t)=h(x(t)) x^{\prime}(t), \quad h(x)=\frac{1}{2}\left(\left(a_{1}\left(x-a_{2}\right)\left(a_{3}-x\right)\right)^{-1 / 4},\right.
\end{aligned}$$
where $a_{1}, a_{2}$ and $a_{3}$ are constants, and $x$ is an auxiliary independent variable (substituting any function $x=x(t)$ gives a solution of (2.28) in terms of $t$ in an interval where $f$ and $f_{i}, i=1,2,3$, do not vanish).

The resulting hyper-Kähler metric is given by (2.9) where the forms $e^{1}, e^{2}, e^{3}$ and the functions $f_{1}, f_{2}, f_{3}, f$ are given by (2.32) and (2.34), respectively.

A particular case is obtained by letting $f_{2}=f_{3}^{-1}$ and $f_{1}=f$, which turns the system (2.34) in the form $\frac{d}{d t}\left(f f_{3}^{-1}\right)=-f f_{3}, \frac{d}{d t}\left(f f_{3}\right)=f f_{3}^{-1}$. This system is integrated trivially,
$$f f_{3}^{-1}=a \cos t+b \sin t \quad \text { and } \quad f f_{3}=a \sin t-b \cos t,$$
hence
$$f^{2}=(a \cos t+b \sin t)(a \sin t-b \cos t), \quad f_{3}=(a \sin t-b \cos t) f^{-1} .$$
Therefore,
$$f=f_{1}=(a \cos t+b \sin t)^{1 / 2}(a \sin t-b \cos t)^{1 / 2}, \quad f_{2}^{-1}=f_{3}=(a \cos t+b \sin t)^{-1 / 2}(a \sin t-b \cos t)^{1 / 2},$$
and the hyper-Kähler metric is given by
$$g=(a \sin t-b \cos t)(a \cos t+b \sin t)\left(d t^{2}+d \phi^{2}\right)+\frac{a \cos t+b \sin t}{a \sin t-b \cos t}\left(e^{2}\right)^{2}+\frac{a \sin t-b \cos t}{a \cos t+b \sin t}\left(e^{3}\right)^{2},$$
where $e^{2}$ and $e^{3}$ are defined in (2.32). Introducing $t_{0}$ and $r_{0}$ by letting $r_{0}=\sqrt{a^{2}+b^{2}}, \cos t_{0}=a / \sqrt{a^{2}+b^{2}}$ and $\sin t_{0}=b / \sqrt{a^{2}+b^{2}}$, we have that $t \in\left(t_{0}, t_{0}+\frac{\pi}{2}\right)$, and the above metric can be put in the form
$$g=\frac{1}{2} r_{0}^{2} \sin 2\left(t-t_{0}\right)\left(d t^{2}+d \phi^{2}\right)+\cot \left(t-t_{0}\right)\left(e^{2}\right)^{2}+\tan \left(t-t_{0}\right)\left(e^{3}\right)^{2} .$$
After an obvious re-parametrization the metric (2.36) takes a familiar form
$$g=a^{2} \sin 2 \tau\left(d \tau^{2}+d \phi^{2}\right)+\cot \tau\left(e^{2}\right)^{2}+\tan \tau\left(e^{3}\right)^{2}$$
which is the vacuum solutions of Bianchi type $V I_{0}$ [37, 38] with group of isometries $E_{(1,1)}$ [25], (see also [44]).

As a consequence of the previous subsections we have the following simple fact.
Proposition 2.3. Let $G$ be a 3-dimensional Lie group of Bianchi type A. Then, there exists a complete metric on $G \times \mathbb{R}$ that is globally conformal to a hyper-Kähler metric on $G \times \mathbb{R}$.

Proof. In the previous subsections, for each 3-dimensional Lie group $G$ of Bianchi type A, we have constructed a hyper-Kähler metric of the form $g=g_{t}+(f(t) d t)^{2}$ on $G \times\left(a_{0}, b_{0}\right)$, for some open interval $\left(a_{0}, b_{0}\right) \subset \mathbb{R}$, such that the metric $g_{t}=\sum_{j=1}^{3} f_{j}(t)^{2}\left(e^{j}\right)^{2}$ is a left-invariant metric on $G$ for each $t \in\left(a_{0}, b_{0}\right)$. By a suitable change of variables $t=t(r)$ we can assume that $r$ changes from $-\infty$ to $+\infty$ as $t$ changes from $a_{o}$ to $b_{0}$. Thus, the considered metrics take the form
$$g=\sum_{j=1}^{3}\left(f_{j}(r)\right)^{2}\left(e^{j}\right)^{2}+(\varphi(r))^{2} d r^{2}$$
where $\varphi(r) d r=f(t) d t, \varphi>0$, for the fixed $t=t(r)$. This allows to put $g$ in the form $g=\varphi(r)^{2} \hat{g}$, where
$$\hat{g}=d r^{2}+\sum_{j=1}^{3}\left(f_{j} / \varphi(r)\right)^{2}\left(e^{j}\right)^{2}=d r^{2}+g_{r}$$
An adaptation of the proof of completeness of a doubly warped product of complete Riemannian manifolds [41] shows that $\hat{g}$ is complete. In fact, following [41] consider a Cauchy sequence $\left\{\left(p_{i}, r_{i}\right)\right\}_{i=1}^{\infty}$ in $G \times \mathbb{R}$. From
the form of the metric it follows for any curve $\gamma$ in $G \times \mathbb{R}$ we have $L(\gamma) \geq L\left(\pi_{2} \circ \gamma\right)$ for the corresponding lengths of the curve and its projection, where $\pi_{2}$ is the projection from $G \times \mathbb{R}$ to $\mathbb{R}$. This implies
$$d_{\hat{g}}\left(\left(p_{i}, r_{i}\right),\left(p_{k}, r_{k}\right)\right) \geq\left|r_{i}-r_{k}\right|,$$
hence $\left\{r_{i}\right\}$ is a Cauchy sequence in $\mathbb{R}$. Therefore, the numbers $r_{i}$ belong to a fixed compact interval, $\left|r_{i}\right| \leq R$. Thus, $\inf _{|r| \leq R}\left|f_{j} / \varphi(r)\right|=\sigma>0$ for $j=1,2,3$ and for any curve $\gamma$ with $\left|\pi_{2} \circ \gamma\right| \leq R$ we have $L(\gamma) \geq \sigma L\left(\pi_{1} \circ \gamma\right)$, where $\pi_{1}$ is the projection from $G \times \mathbb{R}$ to $G$. Since for any curve $\alpha(s), s \in[0,1]$ in $G$ we can consider its lift to $G \times \mathbb{R}$ defined by
$$\gamma(s)=\left(\alpha(s), s r^{\prime}+(1-s) r\right)$$
for which we have $\alpha=\pi_{1} \circ \gamma$ and $\pi_{2} \circ \gamma$ has arbitrarily fixed beginning $r$ and end $r^{\prime}$ with $\left|r-r^{\prime}\right| \leq R$, it follows
$$d_{\hat{g}}\left(\left(p_{i}, r_{i}\right),\left(p_{k}, r_{k}\right)\right) \geq \sigma d_{g_{o}}\left(p_{i}, p_{k}\right)$$
where $g_{o}=\sum_{j=1}^{3}\left(e^{j}\right)^{2}$, hence $\left\{p_{i}\right\}_{i=1}^{\infty}$ is a Cauchy sequence in $\left(G, g_{o}\right)$ (use $r=r_{i}$ and $r^{\prime}=r_{k}$ in the above constriction). Noting that the metric $g_{o}$ is a left-invariant metric on the group $G$ it follows that $\left\{p_{i}\right\}_{i=1}^{\infty}$ is a convergent sequence in $G$. Thus, $\left\{\left(p_{i}, r_{i}\right)\right\}_{i=1}^{\infty}$ is a convergent sequence in $(G \times \mathbb{R}, \hat{g})$. By the Hopf-Rinow theorem the latter is a complete Riemannian manifold. \(\square\)
2.6. Contractions. It is worth observing that the hyper-Kähler metrics constructed from the Bianchi groups of type $I I, V I_{o}$ and $V I I_{o}$ (and the trivial Abelian case) can also be obtained using the well known contractions of the Lie algebras $s u(2)$ (i.e. type IX) and $s u(1,1)$ (i.e. type VIII) to any of the former four. In [11] and [23] this idea of exploiting Lie algebra contractions was used to construct explicit metrics of special holonomy. For our purposes, consider the contraction corresponding to the following scaling of $s u(2)$
$$e^{1}=\hat{e}^{1}, \quad e^{2}=\lambda \hat{e}^{2}, \quad e^{3}=\lambda \hat{e}^{3},$$
where $e^{1}, e^{2}, e^{3}$ are the generators of $\operatorname{su}(2)$ as in (2.10). Clearly, we have
$$d \hat{e}^{1}=-\lambda^{2} \hat{e}^{2} \wedge \hat{e}^{3}, \quad d \hat{e}^{2}=-\hat{e}^{3} \wedge \hat{e}^{1}, \quad d \hat{e^{3}}=-\hat{e}^{1} \wedge \hat{e}^{2},$$
which as $\lambda \rightarrow 0^{+}$corresponds to a contraction to the Lie algebra $V I_{0}$ given in (2.32). For each $\lambda>0$ we have that the metric $\hat{g}=\hat{f}_{1}{ }^{2}\left(\hat{e}^{1}\right)^{2}+\hat{f}_{2}{ }^{2}\left(\hat{e}^{2}\right)^{2}+\hat{f}_{3}{ }^{2}\left(\hat{e}^{3}\right)^{2}+\hat{h}(x)^{2} d x^{2}, \hat{f}_{i}=\hat{f}_{i}(x)$ for $i=1,2,3$ is a hyper-Kähler metric provided the following system of ODEs holds true
$$\frac{d}{d x}\left(\hat{f}_{1} \hat{f}_{2}\right)=\hat{f}_{3}, \quad \frac{d}{d x}\left(\hat{f}_{1} \hat{f}_{3}\right)=\hat{f}_{2}, \quad \frac{d}{d x}\left(\hat{f}_{2} \hat{f}_{3}\right)=\lambda^{2} \hat{f}_{1} .$$
Letting $\lambda \rightarrow 0^{+}$we obtain the system (2.33). In this sense, the metric given by (2.35) is obtained from the metric defined by (2.9) and (2.15) using the contraction between the corresponding Lie algebras. The other possible contractions can be treated analogously.

\section*{3. Hyper symplectic metrics in dimension 4}

In this section, following the method of the preceding section, we present explicit hyper-symplectic (also called hyper-parakähler) metrics in dimension four, of signature (2,2). For this, we lift the special structure on the non-Euclidean Bianchi type groups of class A, discovered in the preceding section (Proposition 2.1), to a hyper-symplectic metric on its product with the real line. The construction extends the correspondence between Bianchi type IX hyper-Kähler metrics and Bianchi type VIII hyper-parakähler structures discovered in [35].

First, we recall that an almost hyper-paracomplex structure on a $4 n$-dimensional manifold $M$ is a triple $\left(J, P_{1}, P_{2}\right)$ of endomorphisms of the tangent bundle of $M$ satisfying the paraquaternionic identities, namely,
$$J^{2}=-P_{1}^{2}=-P_{2}^{2}=-1, \quad J P_{1}=-P_{1} J=P_{2} .$$
If in addition, $J, P_{1}$ and $P_{2}$ are integrable (that is, its corresponding Nijenhuis tensor vanishes), the almost hyper-paracomplex structure $\left(J, P_{1}, P_{2}\right)$ on $M$ is called hyper-paracomplex structure. (The Nijenhuis tensor of an endomorphism $P$ of the tangent bundle of $M$ is given by
$$N_{P}(X, Y)=[P X, P Y]-P[P X, Y]-P[X, P Y]+P^{2}[X, Y],$$
for all vector fields $X, Y$ on $M$.)
An almost hyper-paracomplex manifold $\left(M, J, P_{1}, P_{2}\right)$ is said to be almost hyper-parahermitian if there exists a pseudo-Riemannian metric $g$ satisfying the compatibility conditions
$$g(J \cdot, J \cdot)=-g\left(P_{1} \cdot, P_{1} \cdot\right)=-g\left(P_{2} \cdot, P_{2} \cdot\right)=g(\cdot, \cdot) .$$
The compatible metric $g$ is necessarily of neutral signature $(2 n, 2 n)$ because, at each point of $M$, there is a local pseudo-orthonormal frame of vector fields given by
$$\left\{E_{1}, \ldots, E_{n}, J E_{1}, \ldots, J E_{n}, P_{1} E_{1}, \ldots, P_{1} E_{n}, P_{2} E_{1}, \ldots, P_{2} E_{n}\right\} .$$
The fundamental 2-forms are the differential 2-forms on $M$ defined by
$$\Omega_{1}=g(\cdot, J \cdot), \quad \Omega_{2}=g\left(\cdot, P_{1} \cdot\right), \quad \Omega_{3}=g\left(\cdot, P_{2} \cdot\right) .$$
When these forms are closed the almost hyper-parahermitian structure ( $g, J, P_{1}, P_{2}$ ) is said to be hypersymplectic [28] or hyper-parakähler [32]. This implies (adapting the computations of Atiyah-Hitchin [2] for hyper-Kähler manifolds) that the structures $J, P_{1}$ and $P_{2}$ are integrable and parallel with respect to the Levi-Civita connection [28, 13]. In dimension four an almost hyper-paracomplex structure is locally equivalent to an oriented neutral conformal structure (or an $\operatorname{Sp}(1, \mathbb{R})$ structure) and the integrability implies the anti-self-duality of the corresponding neutral conformal structure [34]. In particular, a four dimensional hyper-symplectic structure is equivalent to an anti-self-dual (ASD) and Ricci-flat neutral metric. For this reason such structures have been used in string theory [42, 30, 33, 3, 31, 10] and integrable systems [16, 4, 17].

Let $G$ be a three dimensional Lie group and let $\left\{e^{1}(t), e^{2}(t), e^{3}(t)\right\}$ be a global basis of 1-forms on $G$ for each $t \in I$, where $I \subset \mathbb{R}$ is a connected interval in the real line. We consider the almost hyper-parahermitian structure (or $\operatorname{Sp}(1, \mathbb{R})$-structure) on $G \times I$ defined by the following 2-forms
$$\begin{aligned}
& \Omega_{1}=-e^{1}(t) \wedge e^{2}(t)+e^{3}(t) \wedge f(t) d t, \\
& \Omega_{2}=e^{1}(t) \wedge e^{3}(t)-e^{2}(t) \wedge f(t) d t, \\
& \Omega_{3}=e^{2}(t) \wedge e^{3}(t)+e^{1}(t) \wedge f(t) d t,
\end{aligned}$$
where $f(t)$ is function of $t \in I$ which does not vanish.
We use the ordered pseudo-orthonormal basis given by (3.1) to orient negatively the manifold $M=G \times I$. Then the fundamental 2-forms (3.3) constitute a basis of the self-dual (SD) 2-forms and a hyper-symplectic structure of the form (3.3) is equivalent to an anti-self-dual (ASD) and Ricci-flat neutral metric.

With the help of Hitchin's theorem [28], which states that an almost hyper-parahermitian structure is hyper-symplectic exactly when the fundamental 2-forms are closed, $d \Omega_{s}=0, s=1,2,3$, it is straightforward to prove similarly to Proposition 2.1 the following important fact.

Proposition 3.1. The almost hyper-parahermitian structure $\left(\Omega_{1}, \Omega_{2}, \Omega_{3}\right)$ is hyper-symplectic if and only if the conditions (2.3) are satisfied and the following evolution equations hold
$$\frac{\partial}{\partial t} e^{12}(t)=f(t) d e^{3}(t), \quad \frac{\partial}{\partial t} e^{13}(t)=f(t) d e^{2}(t), \quad \frac{\partial}{\partial t} e^{23}(t)=-f(t) d e^{1}(t) .$$
The hyper-symplectic metric is given by
$$g=\left(e^{1}(t)\right)^{2}+\left(e^{2}(t)\right)^{2}-\left(e^{3}(t)\right)^{2}-f^{2}(t) d t^{2} .$$

As in the previous section, from Lemma 2.2 it follows that the above Proposition can be applied to the evolution (2.8) in the case of the Bianchi type A groups only. For each of the Bianchi type A groups we shall construct explicitly the general triaxial hyper-symplectic metric, which is of the form
$$g=f_{1}^{2}\left(e_{1}\right)^{2}+f_{2}^{2}\left(e_{2}\right)^{2}-f_{3}^{2}\left(e_{3}\right)^{2}-f^{2} d t^{2},$$
by solving the corresponding system for the functions $f_{1}, f_{2}, f_{3}, f$. We shall see that in each case, we obtain a system identical to one of the systems encountered in the hyper-kähler case.
3.1. Bianchi type $I X$ hyper-symplectic metrics and hyper-Kähler Bianchi type $V I I I$ hyper-Kähler metrics. Let $G=S U(2)=S^{3}$ be described by the structure equations (2.10). We evolve the $S U(2)$ structure according to (2.8).

Using (2.10), we reduce the evolution equations (3.4) to the already considered system (2.20). This establishes a correspondence between triaxial Bianchi type IX hyper-symplectic metrics and triaxial hyper-Kähler Bianchi type VIII hyper-Kähler metrics.

The general solution is given by (2.21). Taking $f=f_{1} f_{2} f_{3}$ in (2.21) and all $f_{i}$ different we obtain explicit expression of a triaxial hyper-symplectic metric (3.6), where the forms $e^{1}, e^{2}, e^{3}$ and the functions $f_{1}, f_{2}, f_{3}, f$ are given by (2.11) and (2.21), respectively.

A particular solution is obtained by letting $a_{1}=a_{2}=0, a_{3}=\frac{a}{16}$ in (2.21) which gives
$$f_{1}=f_{2}=\frac{1}{2}\left(a-t^{4}\right)^{\frac{1}{4}}, \quad f_{3}=\frac{t^{2}}{2}\left(a-t^{4}\right)^{-\frac{1}{4}}, \quad f=t\left(a-t^{4}\right)^{-\frac{1}{4}}, \quad 0<t^{4}<a .$$
The resulting hyper-symplectic metric is given by
$$g=\frac{1}{4}\left(a-t^{4}\right)^{\frac{1}{2}}\left(d \theta^{2}+\sin ^{2} \theta d \phi^{2}\right)-\frac{t^{4}}{4\left(a-t^{4}\right)^{\frac{1}{2}}}(d \psi+\cos \theta d \phi)^{2}-\frac{t^{2}}{\left(a-t^{4}\right)^{\frac{1}{2}}} d t^{2}$$
3.2. Bianchi type $V I I I$ hyper-symplectic metrics and hyper-Kähler Bianchi type $I X$ hyper-Kähler metrics. Let $G=S U(1,1)$ be defined by the structure equations (2.18). We evolve the $S U(1,1)$ structure as in (2.8). Using the structure equations (2.18), the evolution equations (3.4) reduce to the already solved system (2.12). The general solution is of the form (2.15) which has also the expression (2.17). A substitution of (2.17) and (2.19) in (3.6) gives the corresponding triaxial hyper-symplectic metrics.

This establishes a correspondence between triaxial Bianchi type IX hyper-Kähler metrics and triaxial Bianchi type VIII hyper-symplectic metrics discovered in [35].

A particular solution to (2.12) is given by (2.16), which results a hyper-symplectic metric in Eguchi-Hanson form [14, 43, 35] given by
$$\begin{aligned}
g=\frac{t^{2}}{4}\left[(d \psi-\cos \theta d \phi)^{2}+(\sinh \psi d \theta+\right. & \left.\cosh \psi \sin \theta d \phi)^{2}\right] \\
& -\frac{t^{2}}{4}\left(1-\frac{a}{t^{4}}\right)(\cosh \psi d \theta+\sinh \psi \sin \theta d \phi)^{2}-\left(1-\frac{a}{t^{4}}\right)^{-1}(d t)^{2} .
\end{aligned}$$

Setting $f=-\frac{f_{3}}{t}$ one obtains another hyper-symplectic metric.
3.3. Bianchi type $I I$ hyper-symplectic metrics and hyper-Kähler Bianchi type $I I$ hyper-Kähler metrics. Consider the two-step nilpotent Heisenberg group $H^{3}$ defined by the structure equations (2.22). We evolve the structure as in (2.8). The structure equations (2.22) reduce the evolution equations (3.4) to the already solved system (2.24) taking $-f_{3}$ instead of $f_{3}$. This is equivalent to consider the two-step nilpotent Heisenberg group $H^{3}$ defined by the structure equations
$$d e_{1}=d e^{2}=0, \quad d e^{3}=e^{12}, \quad e^{1}=d x, \quad e^{2}=d y, \quad e^{3}=d z+\frac{1}{2} x d y-\frac{1}{2} y d x$$
and evolving the structure as in (2.8).
The general solution is of the form (2.26). This establishes the corresponding form of the general triaxial hyper-symplectic metric (3.6) where the functions $f_{1}, f_{2},-f_{3}, f$ and the 1 -forms $e^{1}, e^{2}, e^{3}$ are given by (2.26) and (2.23), respectively.

A particular solution is $f_{1}=f_{2}=f=t^{\frac{1}{2}}, \quad f_{3}=-t^{-\frac{1}{2}}$, with $t>0$. This is the hyper-symplectic metric
$$g=t\left(-d t^{2}+d x^{2}+d y^{2}\right)-\frac{1}{t}\left(d z-\frac{1}{2} x d y+\frac{1}{2} y d x\right)^{2} .$$
3.4. Bianchi type $V I I_{0}$ hyper-symplectic metrics and hyper-Kähler Bianchi type $V I_{0}$ metrics. We consider the group $E_{2}$ of rigid motions of Euclidean 2-plane defined by the structure equations (2.27). We evolve the structure as in (2.8). Using the structure equations (2.27), the evolution equations (3.4) take the form of the already solved system of ODEs (2.33) with a general solution (2.34) giving a correspondence with Bianchi $V I_{0}$ hyper-Kähler metrics.

When $f_{2}=f_{3}^{-1}, f_{1}=f$ we have
$$f=f_{1}=(a \cos t+b \sin t)^{\frac{1}{2}}(a \sin t-b \cos t)^{\frac{1}{2}}, \quad f_{3}=f_{2}^{-1}=(a \sin t-b \cos t)^{\frac{1}{2}}(a \cos t+b \sin t)^{-\frac{1}{2}} .$$
Introducing $t_{0}$ and $r_{0}$ by letting $r_{0}=\sqrt{a^{2}+b^{2}}, \cos t_{0}=a / \sqrt{a^{2}+b^{2}}$ and $\sin t_{0}=b / \sqrt{a^{2}+b^{2}}$, the resulting hyper-symplectic metric can be put in the form
$$g=\frac{1}{2} r_{0}^{2} \sin 2\left(t-t_{0}\right)\left(-d t^{2}+d \phi^{2}\right)+\cot \left(t-t_{0}\right)\left(e^{2}\right)^{2}-\tan \left(t-t_{0}\right)\left(e^{3}\right)^{2},$$
where $e^{2}, e^{3}$ are given by (2.27). After an obvious reparametrization, this metric can be written as
$$g=\frac{1}{2} r_{0}^{2} \sin 2 \tau\left(-d \tau^{2}+d \phi^{2}\right)+\cot \tau(\sin \phi d x-\cos \phi d y)^{2}-\tan \tau(\cos \phi d x+\sin \phi d y)^{2} .$$
3.5. Bianchi type $V I_{0}$ hyper-symplectic metrics and hyper-Kähler Bianchi type $V I I_{0}$ metrics. Now we consider the group of rigid motions $E(1,1)$ of Lorentzian 2-plane defined by the structure equations (2.32). We evolve the structure as in (2.8). Using the structure equations (2.32), the evolution equations (3.4) turn into the solved system of ODEs (2.28) with the general solution given by (2.30) establishing a correspondence with Bianchi $V I_{0}$ hyper-Kähler metrics.

When $f_{2}=f_{3}^{-1}, \quad f_{1}=f$ we have
$$f=f_{1}=\frac{1}{2}\left(A e^{t}+B e^{-t}\right)^{\frac{1}{2}}\left(A e^{t}-B e^{-t}\right)^{\frac{1}{2}}, \quad f_{3}=f_{2}^{-1}=\left(A e^{t}+B e^{-t}\right)^{-\frac{1}{2}}\left(A e^{t}-B e^{-t}\right)^{\frac{1}{2}},$$
and the hyper-symplectic metric is
$$g=\frac{1}{4}\left(A^{2} e^{2 t}-B^{2} e^{-2 t}\right)\left(-d t^{2}+d \phi^{2}+\frac{4}{\left(A e^{t}-B e^{-t}\right)^{2}}\left(e^{2}\right)^{2}-\frac{4}{\left(A e^{t}+B e^{-t}\right)^{2}}\left(e^{3}\right)^{2}\right),$$
where $e^{2}, e^{3}$ are given by (2.32) , and $t>\frac{1}{2} \log \left|\frac{B}{A}\right|$ since $A^{2} e^{2 t}-B^{2} e^{-2 t}>0$. In particular, letting $A=B$ in (3.8) we obtain
$$g=\frac{A^{2}}{2} \sinh 2 t\left(-d t^{2}+d \phi^{2}\right)+\operatorname{coth} t(\sinh \phi d x+\cosh \phi d y)^{2}-\tanh t(\cosh \phi d x+\sinh \phi d y)^{2} .$$

\section*{4. Conclusions}

Several explicit cohomogeneity one hyper-Kähler (local) metrics of Riemannian and neutral signature were found on four dimensional manifolds $M=G \times I, I=(a, b)$. The group $G$ was assumed to be a three dimensional Bianchi type group, which acts on $M$ by left translations on the first factor of $M$. By considering a time dependent evolution of a fixed left invariant basis of one forms on $G$ we defined an almost hyper-Hermitian structure on $M$. The action of $G$ extends to a trivial action on the fundamental 2-forms of the hyper-Hermitian structure. The hyper-Hermitian structure is hyper-Kähler if the defined fundamental 2-forms are closed. It was found that the latter condition can be fulfilled only in the case of Bianchi type A groups. Restricting the evolution to one of diagonal type we obtained a system of ODEs whose solutions give a hyper-Kähler metric. For each of the Bianchi type A groups we found the explicit solution of the system of ODEs. The hyper-Kähler metrics of neutral signature, called hyper-symplectic metrics, were found to be in correspondence with the Riemannian hyper-Kähler metrics based on the type of the system of ODEs. Thus, we give new examples of hyper-symplectic metrics and extend the correspondence between classes of hyper-symplectic metrics and hyper-Kähler metrics given in [35] in the Bianchi VIII and IX cases to all Bianchi type A cohomogeneity one (with trivial action on the fundamental 2-forms) metrics.

\section*{References}
\begin{itemize}
\item[] [1] Andrada, A., \& Dotti, I., Double Products and Hypersymplectic Structures on $\mathbb{R}^{4 n}$, Commun. Math. Phys. 262 (2006) 1-16.
\item[] [2] Atiyah, M.F., \& Hitchin, N., The geometry and dinamics of magnetic monopoles, M.B. Porter Lectures, Rice University, Princeton University Press, Princeton, New-York, 1988.
\item[] [3] Barberis, M.L., Hyper-Kähler metrics conformal to left invariant metrics on four-dimensional Lie groups, Math. Phys. Anal. Geom. 6 (2003), no. 1, 1-8.
\item[] [4] Bartocci, C., \& Mencattini, I., Hyper-symplectic structures on integrable systems, J. Geom. Phys. 50 (2004), 339-344.
\item[] [5] Belinskii, V.A., Gibbons, G.W., Page, D. N., \& Pope, C. N., Asymptotically Euclidean Bianchi IX metrics in quantum gravity, Phys. Lett. B 76 (1978), 433-435.
\item[] [6] Blažiĉ, N., \& Vukmirović, S., Para-hypercomplex structures on a four-dimensional Lie group, Contemporary geometry and related topics, River Edge, N.J. 2004, World Sci. Publishing, pp. 41-56.
\item[] [7] Bourliot, F., Estes, J., Petropoulos, P.M., \& Spindel, Ph., Gravitational instantons, self-duality, and geometric flows, Phys. Rev. D 81 (2010), 104001 (5 pp).
\item[] [8] Bourliot, F., Estes, J., Petropoulos, P.M., \& Spindel, Ph., $G_{3}$-homogeneous gravitational instantons, Class. Quantum Grav. 27 (2010), 102001 (9 pp).
\item[] [9] Calabi, E., Métriques kählériennes et fibrés holomorphes. Ann. Sci. École Norm. Sup. (4) 12 (1979), no.2, 269-294.
\item[] [10] Carvalo, M., Helayel-Neto, J.A., \& de Oliveira, M.W., Locally product structures and supersymmetry, Lett. Math. Phys. 64 (2003), 93-104.
\item[] [11] Chong, Z. W., Cvetic, M., Gibbons, G. W., Lü, H., Pope, C. N., \& Wagner, P., General metrics of $G_{2}$ holonomy and contraction limits. Nuclear Phys. B 638 (2002), no. 3, 459-482.
\item[] [12] Cvetič, M., Gibbons, G.W., Lü, H., \& Pope, C.N., Orientifolds and slumps in $G_{2}$ and Spin(7) metrics, Annals of Phys. 310 (2004), 265-301.
\item[] [13] Dancer, A.S., Jørgensen, H.R., \& Swann, A.F., Metric geometries over the split quaternions, Rend. Sem. Mat. Univ. Politec. Torino 63 (2005), no. 2, 119-139.
\item[] [14] Dancer, A.S., \& Strachan, A.B., Cohomogeneity-one Kähler metrics in Twistor theory (S. Hugget, ed.), Lecture Notes in Pure and Appl. Math. vol. 169, M. Dekker, New York, Basel, Hong Kong, 1995, pp. 9- 27.
\item[] [15] De Smedt, V., \& Salamon, S., Anti-self-dual metrics on Lie groups, Differential geometry and integrable systems (Tokyo, 2000), 63-75, Contemp. Math., 308, Amer. Math. Soc., Providence, RI, 2002.
\item[] [16] Dunajski, M., Hyper-complex four-manifolds from Tzitzeica equation, J. Math. Phys. 43 (2002), 651-658.
\item[] [17] Dunajski, M., \& West, S., Anti-self-dual conformal structures with null Killing vectors from projective structures, Commun. Math. Phys. 272 (2007), no. 1, 85-118.
\item[] [18] Eguchi, T., \& Hanson, A.J., Asymptotically flat self-dual solutions to Euclidean gravity, Phys. Lett. B 74 (1978), 249-251.
\item[] [19] Fino, A., Pedersen, H., Poon, Y.S., \& Sørensen, M., Neutral Calabi-Yau structures on Kodaira manifolds, Commun. Math. Phys. 248 (2004) no. 2, 255-268.
\item[] [20] Ghezelbash, A.M., Bianchi type IX M-branes, Phys. Rev. D 74 (2006) 126004.
\item[] [21] \_\_\_\_, Supergravity solutions without triholomorphic U(1) isometries, Phys. Rev. D 78 (2008), no. 12, 126002, 8 pp.
\item[] [22] Gibbons, G.W., \& Hawking, S.W., Gravitational multi-instantons, Phys. Lett. B 78 (1978), 430-432.
\item[] [23] Gibbons, G. W., Lü, H., Pope, C. N., \& Stelle, K. S., Supersymmetric domain walls from metrics of special holonomy. Nuclear Phys. B 623 (2002), no. 1-2, 3-46.
\item[] [24] Gibbons, G.W., \& Pope, C.N., The positive action conjecture and asymptotically Euclidean metrics in quantum gravity, Commun. Math. Phys. 66 (1979), 267-290.
\item[] [25] Gibbons, G.W., \& Rychenkova, P., Single-sided domain walls in M-theory, J. Geom. Phys. 32 (2000), no. 3, 311-340.
\item[] [26] Göteman, M., \& Lindstrom, U., Pseudo-hyperkähler geometry and generalized Kähler geometry, Lett. Math. Phys. (to appear), arXiv:0903.2376
\item[] [27] Hitchin, N., The self-duality equations on a Riemann surface, Proc. London Math. Soc. 55 (1987) 59-126.
\item[] [28] \_\_\_\_, Hypersymplectic quotients, Acta Acad. Sci. Tauriensis 124 supl., (1990), 169-180.
\item[] [29] \_\_\_\_, Stable forms and special metrics, in Global Differential Geometry: The Mathematical Legacy of Alfred Gray (Bilbao, 2000) volume 288 of Contemp. Math., Amer. Math. Soc., Providence, RI, 2001, 70-89.
\item[] [30] Hull, C.M., Actions for (2,1)sigma models and strings, Nucl. Phys. B 509 (1988), no. 1, 252-272.
\item[] [31] \_\_\_\_, A Geometry for Non-Geometric String Backgrounds, J. High Energy Phys. 2005, no. 10, 065, 30 pp.
\item[] [32] Ivanov, S., \& Zamkovoy, S., Parahermitian and paraquaternionic manifolds, Differential Geom. Appl. 23 (2005), no. 2, 205-234.
\item[] [33] Jensens, G., \& Rigoli, M., Neutral surfaces in neutral four spaces, Mathematische (Catania) 45 (1990), 407-443.
\item[] [34] Kamada, H., Neutral hyper-Kähler structures on primary Kodaira surfaces, Tsukuba J. Math. 23 (1999), 321-332.
\item[] [35] Kamada, H., \& Machida, Y., Self-duality of metrics of type (2,2) on four-dimensional manifolds, Tohoku Math. J. 49 (1997), 259-275.
\item[] [36] Krasiński, A., Behr, C. G., Schücking, E., Estabrook, F. B., Wahlquist, H. D., Ellis, G. F. R., Jantzen, R., \& Kundt, W., The Bianchi classification in the Schücking-Behr approach. Gen. Relativity Gravitation 35 (2003), no. 3, 475-489.
\item[] [37] Lorenz, D., Gravitational instanton solutions for Bianchi types I-IX, Acta Phys. Polonica B 14 (1983), 791-805.
\end{itemize}
\begin{itemize}
\item[] [38] Lorenz-Petzold, D., Positive-definite self-dual solutions of Einstein's field equations, J. Math. Phys. 24 (1983), no. 11, 2632-2634.
\item[] [39] \_\_\_\_, Gravitational instanton solutions, Progr. Theoret. Phys. 81 (1989), no. 1, 17-22.
\item[] [40] Nurowski, P., \& Przanowski, M., A four dimensional example of Ricci flat metric admitting almost Kähler non-Kähler structure, Class. Quantum Grav. 16 (1999), L9-L13.
\item[] [41] O'Neill, B., Semi-Riemannian geometry. With applications to relativity. Pure and Applied Mathematics, 103. Academic Press, Inc., New York, 1983.
\item[] [42] Ooguri, H., \& Vafa, C., Geometry of $N=2$ strings, Nucl. Phys. B 361 (1991), 469-518.
\item[] [43] Tod, K.P., Cohomogeneity-one metrics with self-dual Weyl tensor in Twistor theory (S. Hugget, ed.), Lecture Notes in Pure and Appl. Math. vol. 169, M. Dekker, New York, Basel, Hong Kong, 1995, pp. 171-184.
\item[] [44] Valent, G., \& Yahia, H.B., Integrable geodesic flows and multi-centre versus Bianchi A metrics, Class. Quantum Grav. 24 (2007), 255-276.
\end{itemize}
(Luis C. de Andrés, Marisa Fernández, José A. Santisteban) Universidad del País Vasco, Facultad de Ciencia y Tecnología, Departamento de Matemáticas, Apartado 644, 48080 Bilbao, Spain
E-mail address: luisc.deandres@ehu.es
E-mail address: marisa.fernandez@ehu.es
E-mail address: joseba.santisteban@ehu.es
(Stefan Ivanov) University of Sofia, Faculty of Mathematics and Informatics, blvd. James Bourchier 5, 1164, Sofia, Bulgaria
and Department of Mathematics, University of Pennsylvania, Philadelphia, PA 19104-6395
E-mail address: ivanovsp@fmi.uni-sofia.bg
(Luis Ugarte) Departamento de Matemáticas-I.U.M.A., Universidad de Zaragoza, Campus Plaza San Francisco, 50009 Zaragoza, Spain
E-mail address: ugarte@unizar.es
(Dimiter Vassilev) Department of Mathematics and Statistics, University of New Mexico, Albuquerque, New Mexico, 87131-0001
E-mail address: vassilev@math.unm.edu
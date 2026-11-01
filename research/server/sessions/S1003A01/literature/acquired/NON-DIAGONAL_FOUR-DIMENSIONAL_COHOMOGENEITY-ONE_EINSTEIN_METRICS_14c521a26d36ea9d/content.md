---
retention_scope: session
part: 1
total_parts: 1
---

---
source_file: 1609_02747.pdf
converter: mathpix
format: mmd
---

\title{
NON-DIAGONAL FOUR-DIMENSIONAL COHOMOGENEITY-ONE EINSTEIN METRICS IN VARIOUS SIGNATURES
}

\author{
MACIEJ DUNAJSKI AND PAUL TOD
}

\begin{abstract}
Most known four-dimensional cohomogeneity-one Einstein metrics are diagonal in the basis defined by the left-invariant one-forms, though some essentially non-diagonal ones are known. We consider the problem of explicitly seeking non-diagonal Einstein metrics, and we find solutions which in some cases exhaust the possibilities. In particular we construct new examples of neutral signature non-diagonal Bianchi type VIII Einstein metrics with self-dual Weyl tensor.
\end{abstract}

\section*{1. Introduction}

A (pseudo) Riemannian four-manifold $(\mathcal{M}, g)$ is said to have cohomogeneity-one if it admits an isometry group $G$ acting transitively on codimension-one surfaces in $\mathcal{M}$. Cohomogeneity-one Einstein metrics have been much studied both in the literature of general relativity, where they provide a simple generalisation of the Friedman-Roberson-Walker cosmological models (see e.g. [4]), and in Riemannian geometry where they provide large classes of explicit solutions (see e.g. [11]). In the Riemannian case, the metric on the surfaces of homogeneity is inevitably positive-definite, while in general relativity the surfaces of homogeneity are generally taken to be space-like when the metric is again definite (positive or negative according to convention).

When the surfaces of homogeneity are 3-dimensional, which is the case most-studied in relativity, the most general case has a 3-dimensional transitive group of isometries and these are classified by the Bianchi classification of 3-dimensional Lie algebras, which has been an important part of mathematical cosmology for many years(see the historical account in [6]). We won't review the classification here, for that see e.g. [4] or [11], but we will use the language of the classification. In [3] the authors exhibited an explicit Bianchi type VIII Einstein metric with selfdual Weyl tensor (a so-called 'SD' solution) which is nondiagonal in the sense that the metric on the surfaces of homogeneity (which for brevity we shall call the spatial metric) is not diagonal in the basis of left-invariant one-forms associated with the symmetry, and cannot be diagonalised in this basis. The metric has signature $(2,2)$ (or neutral signature) so that the spatial metric is indefinite. It is known that an Einstein type VIII or IX metric with definite spatial metric may always be assumed to be diagonal in the sense used here: Locally $\mathcal{M}=\mathbb{R} \times G$, and the group coordinates do not appear in the Einstein tensor. The problem of finding cohomogeneity-one Einstein metrics therefore reduces to solving a system of second-order ODEs on the spatial metric with independent variable that can conveniently be called time regardless of the signature; if the spatial metric is diagonalised at one time, then one of the Einstein constraints forces it to stay diagonal at all times. This depends crucially on the field equations and does not necessarily hold for Einstein equations with matter sources. This is made explicit in [11] for Riemannian signature and in [4] for many cases in relativistic cosmology. By an examination of the proof one can see that real type IX metrics of any signature can be assumed to be diagonal without loss of generality, but if one wants nondiagonal type VIII metrics, one may find them in neutral signature. The interplay between diagonalisability and various signatures of $g$ is related to the applicability of Sylvester's Law of Inertia, and can be seen as follows: A general cohomogeneity-one metric takes the form
$$g=d t^{2}+h_{i j}(t) \sigma^{i} \sigma^{j},$$

\footnotetext{
Date: 2 September 2016.
}
where the $\sigma^{i}$ are the left-invariant one forms on $G$ such that
$$d \sigma^{i}+\frac{1}{2} C_{j k}^{i} \sigma^{j} \wedge \sigma^{k}=0$$
The matrix $n^{i j}=C_{k m}^{i} \epsilon^{k m j}$ is symmetric for type VIII. If $h_{i j}$ is positive (or negative) definite, then one can diagonalise $h$ and $n$ simultaneously by changing the basis $\sigma^{i}$. This is not always true if $g$ is neutral, so that $h$ has indefinite signature.

Nondiagonal Einstein metrics of other Bianchi types are known (see e.g. [7] for a Lorentzian vacuum solution and [1] and [10] for a variety of solutions). It is worth noticing that all types apart from VIII and IX have an isometry group with a 2-dimensional Abelian subgroup, and when this group acts orthogonally-transitively the Einstein vacuum equations in any signature are integrable and can be solved by the twistor methods of Mason and Woodhouse and collaborators, [8], following [13] and [12] ${ }^{1}$.

In this paper we set out to find real non-diagonal cohomogeneity-one Einstein metrics. We begin in Section 2 with the simplest case, type I, which has a three-dimensional Abelian isometry group. This case is fairly well-known but the calculation highlights the interaction between the signature and the variety of canonical forms. Some new examples are given by formulae (11) and (15). In Section 3 we show how to obtain nondiagonal real type VIII from complex type IX, both diagonal and nondiagonal. In particular the class class of metrics (29) contains the self-dual Einstein example [3] with $\Lambda \neq 0$ as special case, and the three-parameter family of Ricci-flat metrics (30) generalises the Eguchi-Hanson solution. In Section 4 we briefly consider other types. Where these have orthogonally transitive subgroups of the isometry group they can be solved by twistor methods so we consider direct integration of some examples which do not have orthogonally transitive subgroups of the isometry group. An example of a non-diagonal, self-dual Ricci-flat Bianchi II metric is given by (40).

\section*{2. Type I}

The integrations are particularly simple in this case, but this enables one to see how the different metrics arise from the classification of minimum polynomials of a relevant matrix, and introduces the methods needed later for the more complicated types.
2.1. The vacuum and Einstein equations. For type I, the invariant one-forms are all exact so that one may choose three spatial coordinates $\left(x^{1}, x^{2}, x^{3}\right)$ and the metric can be taken to be
$$g=d t^{2}+h_{i j}(t) d x^{i} d x^{j} .$$
We may calculate the curvature in an unsophisticated manner. First the Christoffel symbols are given by
$$\Gamma_{00}^{0}=\Gamma_{0 i}^{0}=\Gamma_{00}^{i}=\Gamma_{j k}^{i}=0$$
while
$$\begin{aligned}
\Gamma_{i j}^{0} & =-\frac{1}{2} \dot{h}_{i j} \\
\Gamma_{0 j}^{i} & =\frac{1}{2} h^{i k} \dot{h}_{j k},
\end{aligned}$$
with overdot for $d / d t$. Then with the definition of the Riemann tensor as
$$R_{b c d}^{a}=-2 \Gamma_{b[c, d]}^{a}-2 \Gamma_{b[c}^{e} \Gamma_{d] e}^{a},$$

\footnotetext{
${ }^{1}$ In particular all the examples in [1] and [10] do have orthogonally transitive $G_{2}$ actions, and this is in a sense the reason why the integrations there lead to Painlevé equations.
}
we find
$$\begin{aligned}
R_{i 0 j}^{0} & =-\frac{1}{2} \ddot{h}_{i j}+\frac{1}{4} h^{k m} \dot{h}_{i m} \dot{h}_{k j}, \\
R_{i j k}^{0} & =0, \\
R_{j k l}^{i} & =\frac{1}{4} h^{i m} \dot{h}_{j k} \dot{h}_{m l}-\frac{1}{4} h^{i m} \dot{h}_{j l} \dot{h}_{m k} .
\end{aligned}$$
(It follows rapidly from here that self-duality or anti-self-duality of the Riemann tensor at once implies that the curvature entirely vanishes.)

For the Ricci tensor we obtain
$$\begin{aligned}
R_{00} & =-\frac{1}{2} h^{i j} \ddot{h}_{i j}+\frac{1}{4} h^{k m} \dot{h}_{k j} h^{i j} \dot{h}_{i m}, \\
R_{0 i} & =0, \\
R_{i j} & =-\frac{1}{2} \ddot{h}_{i j}+\frac{1}{2} h^{k m} \dot{h}_{i m} \dot{h}_{k j}-\frac{1}{4}\left(h^{m n} \dot{h}_{m n}\right) \dot{h}_{i j} .
\end{aligned}$$
For the vacuum equations, double the last of (3), multiply by $-h^{k i}$ and adopt a matrix notation:
$$h^{-1} \ddot{h}-h^{-1} \dot{h} h^{-1} \dot{h}+\frac{1}{2} \operatorname{tr}\left(h^{-1} \dot{h}\right) h^{-1} \dot{h}=0 .$$
To simplify this introduce $V$ by
$$2 \dot{V} / V=\operatorname{tr}\left(h^{-1} \dot{h}\right)=\frac{d}{d t} \log (\operatorname{det} h),$$
so that $|\operatorname{det} h|=V^{2}$, then (4) becomes
$$d\left(V h^{-1} \dot{h}\right) / d t=0$$
which integrates at once to
$$V h^{-1} \dot{h}=M=\text { constant },$$
or equivalently
$$\dot{h}=V^{-1} h M .$$
Take the trace of (5) to find
$$\operatorname{tr}(M)=2 \dot{V}$$
so that $\ddot{V}=0$ and $V$ is linear in $t$.
Go back to the first of (3) to get another vacuum equation which becomes
$$\operatorname{tr}\left(M^{2}\right)-(\operatorname{tr} M)^{2}=0,$$
and which constrains $M$. Since $h$ and $\dot{h}$ are both symmetric, $M$ is also constrained by (6). Clearly the 4-metric is flat if $M=0$.

At this point it is worth noting the Einstein equations with $\Lambda \neq 0$. Suppose these are
$$R_{i j}=\Lambda h_{i j}, \quad R_{00}=\Lambda$$
then
$$d\left(V h^{-1} \dot{h}\right) / d t=-2 \Lambda V \mathbb{I}$$
with $2 \dot{V} / V=\operatorname{tr}\left(h^{-1} \dot{h}\right)$ as before. Now however, using the (00) equation
$$\ddot{V}=-3 \Lambda V .$$
Solve this with $V(0)=1, \dot{V}(0)=0$ to find
$$V=\cos (3 H t) \text { or } \cosh (3 H t)$$
when $H^{2}=\Lambda / 3$ or $-\Lambda / 3$ respectively. Integrate (8) once to find
$$V h^{-1} \dot{h}=M+\frac{2}{3} \dot{V} \mathbb{I},$$
with constant $M$. Introduce $k=V^{-2 / 3} h$ then $k$ satisfies
$$V k^{-1} \dot{k}=M$$
which is (6) back again. Thus the solutions with $\Lambda \neq 0$ are readily obtained from the solutions with $\Lambda=0$.
2.2. Classification of vacuum solutions. The solutions depend on the canonical forms of $h$ and $M$.
\begin{itemize}
\item[(1)] If $h$ is definite (positive or negative) then, at any fixed instant say $t_{0}$ of $t$, it can be diagonalised with an orthogonal matrix and reduced to the identity by a diagonal matrix. At this instant, (6) forces $M$ to be symmetric so it too can be diagonalised by an orthogonal matrix preserving $h$. But $M$ is constant so now $h$ is diagonal for all time. These are the Kasner solutions.
\item[(2)] If $h$ is indefinite, it can still be reduced at any fixed instant to a diagonal matrix whose entries are ±1. For simplicity suppose this is
$$h\left(t_{0}\right)=\eta:=\operatorname{diag}(1,1,-1),$$
since the other possibility not so far covered follows by $x^{j} \rightarrow i x^{j}$. We are at liberty to perform the transformation
$$h \rightarrow \hat{h}=L^{T} h L, \quad M \rightarrow \hat{M}=L^{-1} M L,$$
where $L$ is a three-dimensional Lorentz matrix. By (6), at time $t_{0}$ the matrix $S:=\eta M$ is symmetric.
To classify canonical forms of $M$ we consider the eigenvalue equation
$$M_{\alpha}{ }^{\beta} X^{\alpha}=\lambda X^{\beta},$$
where Greek indices are 3-dimensional Lorentz indices (and sometimes omitted) and $h=\eta_{\alpha \beta}$ is the Lorentz metric. There are three possibilities:
\begin{itemize}
\item[(a)] If there are three distinct real $\lambda$ then $M$ can be diagonalised and we obtain Kasner again.
\item[(b)] If there are repeated real roots we need to consider the minimum polynomial $m(x)$ of $M$. Taking account of (7) there are three nontrivial cases namely
$$(x-\lambda)(x-\mu)^{2}, x^{2}, x^{3}$$
(we don't need to consider $(x-\lambda)^{k}$ for nonzero $\lambda$ as this would violate (7), and we don't need to consider $m(x)=x$ as this gives flat space).
\begin{itemize}
\item[(i)] $m(x)=(x-\lambda)(x-\mu)^{2}$ with $\lambda, \mu$ distinct. Necessarily $\lambda$ and $\mu$ are real and (7) requires
$$\mu(\lambda+2 \mu)=0,$$
so in particular $\lambda=0$ implies $\mu=0$ and we have the next case so w.l.o.g. $\lambda \neq 0$; also $\lambda=\mu$ implies $\lambda=0$ and is therefore ruled out.
There is a basis of vectors $X, Y, Z$ (omitting the indices) with
$$M X=\lambda X, \quad M Y=\mu Y, \quad M Z=\mu Z+Y .$$
In terms of the matrix $S=S_{\alpha \beta}$ we deduce
$$\lambda X_{\alpha} Y^{\alpha}=S_{\alpha \beta} X^{\alpha} Y^{\beta}=\mu X_{\alpha} Y^{\alpha}$$
so $X_{\alpha} Y^{\alpha}=0$ and similarly $X_{\alpha} Z^{\alpha}=0$. Next
$$\mu Y_{\alpha} Z^{\alpha}=S_{\alpha \beta} Y^{\alpha} Z^{\beta}=\mu Y_{\alpha} Z^{\alpha}+Y_{\alpha} Y^{\alpha}$$
so that $Y$ is a null vector.
Since we are free to add multiples of $Y$ to $Z$ and perform Lorentz transformations, we can assume
$$X=(1,0,0)^{T}, \quad Y=(0,1,1)^{T}, \quad Z=(0, A,-A)^{T},$$
\end{itemize}
\end{itemize}
\end{itemize}
for some nonzero, real $A$ and we find
$$M=\left(\begin{array}{ccc}
\lambda & 0 & 0 \\
0 & \mu+\nu & -\nu \\
0 & \nu & \mu-\nu
\end{array}\right) .$$
where $\nu=1 /(2 A)$, and still $\mu(\lambda+2 \mu)=0$. To find the metrics, take
$$h=\left(\begin{array}{lll}
\alpha & \beta & \gamma \\
\beta & \delta & \epsilon \\
\gamma & \epsilon & \zeta
\end{array}\right),$$
with $h(0)=\eta$ and substitute into (6). Symmetry of $\dot{h}$ requires
$$(\mu+\nu-\lambda) \beta+\gamma \nu=0=-\beta \nu+\gamma(\mu-\nu-\lambda), \quad \nu(2 \epsilon+\delta+\zeta)=0 .$$

Since $\lambda-\mu \neq 0$, the first pair imply $\beta=\gamma=0$ and the vacuum equations reduce to
$$\begin{aligned}
\dot{\alpha} & =\frac{1}{V} \lambda \alpha \\
\dot{\delta} & =\frac{1}{V}(\delta(\mu+\nu)+\epsilon \nu) \\
\dot{\epsilon} & =\frac{1}{V}(-\delta \nu+\epsilon(\mu-\nu)) \\
\dot{\zeta} & =\frac{1}{V}(-\epsilon \nu+\zeta(\mu-\nu)) \\
\dot{V} & =\frac{1}{2}(\lambda+2 \nu)
\end{aligned}$$
There are two cases:
(A) $\mu=0$ when
$$h=\left(1+t / t_{0}\right)^{2} d x^{2}+d y^{2}-d z^{2}+\frac{2 \nu}{\lambda} \log \left(1+t / t_{0}\right)(d y-d z)^{2}$$

The resulting 4-metric (1) is a pp-wave (see e.g. [9])).
\begin{itemize}
\item[(B)] $\lambda+2 \mu=0$ when
$$h=e^{-2 \mu t} d x^{2}+e^{\mu t}\left(\left(d y^{2}-d z^{2}\right)+\nu t(d y-d z)^{2}\right) .$$
\item[(ii)] $m(x)=x^{2}$ : this follows from the previous case by setting $\lambda=\mu=0$ in $M$, and in fact in (11), but the metrics turn out to be flat.
\item[(iii)] $m(x)=x^{3}$ : there will be a basis $X, Y, Z$ with
$$M X=0, \quad M Y=X, \quad M Z=Y,$$
and we are free to perform the changes
$$Z \rightarrow Z+\alpha X+\beta Y, \quad Y \rightarrow Y+\beta X .$$
By similar considerations to those used above, we deduce
$$X_{\alpha} X^{\alpha}=0=X_{\alpha} Y^{\alpha}=X_{\alpha} Z^{\alpha}-Y_{\alpha} Y^{\alpha}$$
so, using Lorentz transformations and the available freedom, w.l.o.g.
$$X=(0,1,1)^{T}, \quad Y=(A, 0,0)^{T}, \quad Z=(C, D,-D)^{T},$$
with $A D \neq 0$. We can deduce $S$ and from it calculate $M$ :
$$M=\left(\begin{array}{ccc}
0 & \lambda & -\lambda \\
\lambda & 0 & 0 \\
\lambda & 0 & 0
\end{array}\right),$$
\end{itemize}
with $\lambda \neq 0$. Note $\operatorname{tr} M=0$ so w.l.o.g. $V=1$, and taking
$$h=\left(\begin{array}{lll}
\alpha & \beta & \gamma \\
\beta & \delta & \epsilon \\
\gamma & \epsilon & \zeta
\end{array}\right),$$
with $h(0)=\eta$, substitute into (6). Symmetry of $\dot{h}$ forces
$$\alpha=\delta+\epsilon=-\zeta-\epsilon, \quad \beta+\gamma=0,$$
reducing the vacuum equations to the system
$$\begin{aligned}
\dot{\alpha} & =0 \\
\dot{\beta} & =\lambda \alpha \\
\dot{\delta} & =\lambda \beta \\
\dot{\epsilon} & =-\lambda \beta \\
\dot{\zeta} & =-\lambda \gamma
\end{aligned}$$
which are solved by
$$\alpha=1, \quad \beta=-\gamma=\lambda t, \quad \delta=1+\frac{1}{2} \lambda^{2} t^{2}, \quad \epsilon=-\frac{1}{2} \lambda^{2} t^{2}, \quad \zeta=-1+\frac{1}{2} \lambda^{2} t^{2} .$$

The metric is
$$g=d t^{2}+d x^{2}+d y^{2}-d z^{2}+2 \lambda t d x(d y-d z)+\frac{1}{2} \lambda^{2} t^{2}(d y-d z)^{2} .$$
For this metric, the components of the Riemann tensor as in (3)-(5) are constant (and not all zero) but the resulting space-time is not homogeneous as the Riemann tensor is not paralle ${ }^{2}$.
\begin{itemize}
\item[(c)] If there is one real root, say $\lambda$ and a complex conjugate pair, say $\mu \pm i \nu$ with real $\mu, \nu$ (and $\nu \neq 0$ or we are in an earlier case) then there are real Lorentz vectors $X, U, V$ with
$$M X=\lambda X, \quad M(U+i V)=(\mu+i \nu)(U+i V) .$$
With the aid of the symmetric matrix $S$ we can write these equations as
$$S_{\alpha \beta} X^{\beta}=\lambda X_{\alpha}, \quad S_{\alpha \beta}\left(U^{\beta}+i V^{\beta}\right)=(\mu+i \nu)\left(U_{\alpha}+i V_{\alpha}\right),$$
and deduce
$$X_{\alpha} U^{\alpha}=0=X_{\alpha} V^{\alpha}=U_{\alpha} U^{\alpha}+V_{\alpha} V^{\alpha} .$$
By rotating $U$ and $V$ in the 2-plane they span:
$$\left(U^{\alpha}+i V^{\alpha}\right) \rightarrow e^{i \phi}\left(U^{\alpha}+i V^{\alpha}\right)$$
we can arrange that $U_{\alpha} V^{\alpha}=0$. Now they cannot both be null so one, say $U$ is space-like and then the other, $V$, is time-like. Since $X$ is orthogonal to both, it must be space-like and we have an orthogonal triad which we can suppose to be normalised. Choose
$$X=(1,0,0)^{T}, \quad U=(0,1,0)^{T}, \quad V=(0,0,1)^{T}$$
then
$$M=\left(\begin{array}{ccc}
\lambda & 0 & 0 \\
0 & \mu & -\nu \\
0 & \nu & \mu
\end{array}\right) .$$
We need to impose (7), which implies
$$2 \lambda \mu+\mu^{2}+\nu^{2}=0 .$$
\end{itemize}

\footnotetext{
${ }^{2}$ This is the metric found in [10] equation (4.10)
}

We know that $\nu \neq 0$ so this also forces $\mu \neq 0$ and we can solve for $\lambda$ :
$$\lambda=-\frac{\left(\mu^{2}+\nu^{2}\right)}{2 \mu} .$$
To find the metric explicitly, first parametrise $h$ :
$$h=\left(\begin{array}{lll}
\alpha & \beta & \gamma \\
\beta & \delta & \epsilon \\
\gamma & \epsilon & \zeta
\end{array}\right),$$
with $h(0)=\eta$ and substitute into (6). Symmetry forces $\beta=\gamma=\zeta+\delta=0$ and leaves the system
$$\begin{aligned}
\dot{\alpha} & =\frac{1}{V} \lambda \alpha \\
\dot{\delta} & =\frac{1}{V}(\mu \delta+\nu \epsilon) \\
\dot{\epsilon} & =\frac{1}{V}(-\nu \delta+\mu \epsilon) \\
\dot{V} & =\frac{1}{2}(\lambda+2 \mu)
\end{aligned}$$
\begin{itemize}
\item[(i)] If $\lambda+2 \mu \neq 0$ then
$$V=1+\frac{t}{t_{0}}, \quad \alpha=\left(1+\frac{t}{t_{0}}\right)^{2 p}, \quad \delta+i \epsilon=\left(1+\frac{t}{t_{0}}\right)^{2(q+i r)}$$
with
$$p=\frac{\lambda}{\lambda+2 \mu}, \quad q+i r=\frac{(\mu-i \nu)}{\lambda+2 \mu}, \quad t_{0}=\frac{2}{\lambda+2 \mu} .$$
Note that
$$p+(q+i r)+(q-i r)=1=p^{2}+(q+i r)^{2}+(q-i r)^{2},$$
so that this metric is essentially a real slice of a complex Kasner metric. This family of metrics appears in [10] as Harrison metrics.
\item[(ii)] If $\lambda+2 \mu=0$ then also $\nu= \pm \mu \sqrt{3}$ and there is just one free parameter. We can assume $V=1$ without loss of generality and then
$$\alpha=e^{-2 \mu t}, \quad \delta=e^{\mu t} \cos (\nu t), \quad \epsilon=-e^{\mu t} \sin (\nu t) .$$
\end{itemize}
We have found all type I vacuum metrics of all signatures, of which (11) and (15) seem to be new. All type I Einstein metrics with nonzero $\Lambda$ can then be found by the method at the end of section 2.1.

\section*{3. Types VIII and IX}

As noted in the Introduction, real type IX Einstein metrics of any signature can be assumed to be diagonal without loss of generality. Similarly type VIII Einstein with positive or negative definite spatial metric can be assumed diagonal without loss of generality. Thus for nondiagonal real Einstein metrics one should consider neutral signature type VIII.
3.1. Nondiagonal type VIII from diagonal type IX. It is possible to obtain all real analytic nondiagonal definite or indefinite type VIII examples by taking real slices of complex type IX solutions. This can be seen as follows: suppose the left-invariant one-forms are $\Sigma_{i}$ for type IX and $\sigma_{i}$ for type VIII, so that
$$d \Sigma_{1}=\Sigma_{2} \wedge \Sigma_{3}, \quad d \Sigma_{2}=\Sigma_{3} \wedge \Sigma_{1}, \quad d \Sigma_{3}=\Sigma_{1} \wedge \Sigma_{2}$$
and
$$d \sigma_{1}=\sigma_{2} \wedge \sigma_{3}, \quad d \sigma_{2}=-\sigma_{3} \wedge \sigma_{1}, \quad d \sigma_{3}=\sigma_{1} \wedge \sigma_{2},$$
then given a real analytic type VIII metric $g$ set
$$\sigma_{1}=i \Sigma_{1}, \quad \sigma_{2}=\Sigma_{2}, \quad \sigma_{3}=-i \Sigma_{3}$$
which, following [5], we shall call 'Kamada's choice', to obtain a complex type IX metric; either this can be diagonalised at any choice of time and will then remain diagonal, so that the original type VIII metric is defined on a real slice of this complex (and diagonal) type IX metric, or it cannot be so diagonalised in which case there are different solutions (that we find below).

However an explicit general solution of the vacuum equations for type IX metrics is not known (and, being chaotic, is never likely to be known) so to find explicit solutions we impose an extra condition, namely self-dual or anti-self-dual (SD or ASD) Weyl tensor. Now we may follow the method of [11], at least for diagonal type IX.

With the conventions of [11], write the type IX metric as
$$g=w_{1} w_{2} w_{3} d T^{2}+\frac{w_{2} w_{3}}{w_{1}} \Sigma_{1}^{2}+\frac{w_{3} w_{1}}{w_{2}} \Sigma_{2}^{2}+\frac{w_{1} w_{2}}{w_{3}} \Sigma_{3}^{2} .$$
In [11] the SD Einstein equations are solved for this metric. In brief, the Levi-Civita connection is coded into three connection variables ( $A_{1}, A_{2}, A_{3}$ ) obtained as first-derviatives of the $w_{i}$, and the first-order system for the $A_{i}$ is reduced to a Painlevé VI equation for the variable $x=\frac{A_{1}-A_{2}}{A_{3}-A_{2}}$.

We shall find nondiagonal real type VIII solutions by imposing a particular set of reality conditions, different from Kamada's choice, and we shall show in an Appendix that these two choices are the only two choices, up to an appropriate equivalence.

We set
$$\Sigma_{1}=-\bar{\Sigma}_{1}=-i \sigma_{1}, \quad \Sigma_{2}=\bar{\Sigma}_{3}=\frac{1}{\sqrt{2}}\left(\sigma_{2}+i \sigma_{3}\right)$$
for real $\sigma_{i}$, then relations (16) hold, as required.
To obtain a real metric, we have
$$h=A \Sigma_{1}^{2}+B \Sigma_{2}^{2}+C \Sigma_{3}^{2}=-A \sigma_{1}^{2}+\frac{1}{2}(B+C)\left(\sigma_{2}^{2}-\sigma_{3}^{2}\right)+i(B-C) \sigma_{2} \sigma_{3},$$
which will be real if $A$ is real and $B=\bar{C}$. Returning to (18) we see that these conditions require $w_{1}$ real and $w_{2}= \pm \bar{w}_{3}$ (w.l.o.g. we take $w_{2}=\bar{w}_{3}$ as the other choice simply changes the overall sign of the metric).

Following the conventions of [11], we find that the functions $A_{i}$ that encode the connection coefficients must satisfy $A_{1} \in \mathbb{R}, A_{2}=\bar{A}_{3}$. Introduce
$$z=\frac{x}{x-1}=\frac{A_{1}-A_{3}}{A_{1}-A_{2}},$$
in terms of $x(T)$ (with $T$ related to $t$ in (1) by $d t^{2}=w_{1} w_{2} w_{3} d T^{2}$ ) then the reality conditions force $z \bar{z}=1$ or equivalently $x+\bar{x}=1$. Substituting $x=\frac{1}{2}+i y$ into (4.8) of [11] we obtain an equation for $y$ :
$$\frac{d}{d T}\left(\left(y^{\prime}\right)^{-3 / 2} y^{\prime \prime}\right)=\frac{1}{2}\left(y^{\prime}\right)^{3 / 2} \frac{\frac{3}{4}-y^{2}}{\left(\frac{1}{4}+y^{2}\right)^{2}}, \quad \text { where } \quad{ }^{\prime}=d / d T .$$
This will have real solutions for $y$, which will in turn give appropriate $z$. To find the metric, continue as in [11], and there will be new SD vacuum metrics in this class.
3.2. Nondiagonal type VIII from non-diagonalisable type IX. While every real symmetric 3 × 3 matrix can be diagonalised by conjugation with a real orthogonal matrix, this is not true for complex symmetric $3 \times 3$ matrix. Consequently a real analytic type VIII metric may complexify to a nondiagonalisable type IX metric and then it will not lie in the previous class.

There are two relevant canonical forms of nondiagonalisable complex symmetric $3 \times 3$ matrix, which are distinguished by the minimum polynomial. If the minimum poynomial has distinct roots then the matrix is diagonalisable so for nondiagonalisability there must be repeated roots and the cases are:
\begin{itemize}
\item[(1)] Minimum polynomial $(x-\lambda)(x-\mu)^{2}$ with $\lambda \neq \mu$, which leads to a spatial metric of the form
$$\left(\begin{array}{ccc}
\lambda & 0 & 0 \\
0 & \mu+\nu & i \nu \\
0 & i \nu & \mu-\nu
\end{array}\right)$$
\item[(2)] Minimum polynomial $(x-\lambda)^{3}$ which leads to spatial metric
$$\left(\begin{array}{ccc}
\lambda-i \mu & \mu & \nu \\
\mu & \lambda+i \mu & i \nu \\
\nu & i \nu & \lambda
\end{array}\right)$$
\end{itemize}
From these by the Kamada choice we obtain two type VIII metrics. Choose the invariant one-forms to satisfy (16) and parametrise the metrics as
\begin{itemize}
\item[(1)]
$$g=d t^{2}-A^{2} \sigma_{1}^{2}+\left(\sigma_{2}-\sigma_{3}\right)\left((B+C) \sigma_{2}+(B-C) \sigma_{3}\right),$$
with $A B \neq 0$.
\item[(2)]
$$g=d t^{2}-\left(\sigma_{1}+\sigma_{2}\right)\left(\left(A^{2}+B\right) \sigma_{1}-\left(A^{2}-B\right) \sigma_{2}+2 C \sigma_{3}\right)-A^{2} \sigma_{3}^{2},$$
with $A \neq 0$.
\end{itemize}
These are evidently real for $A, B, C$ real, and both have neutral signature. We will solve the Einstein equations in the two cases, sometimes completely and sometimes reducing to a secondorder linear ODE which can be regarded as integrable.
3.2.1. Solving the Einstein equations for the metric (21). The Einstein equations $R_{a b}=\Lambda g_{a b}$ for (21) are
$$\begin{aligned}
-\frac{\ddot{A}}{A}-\frac{\ddot{B}}{B}+\frac{\dot{B}^{2}}{2 B} & =\Lambda \\
\frac{\ddot{A}}{A}+\frac{\dot{A} \dot{B}}{A B}-\frac{A^{2}}{2 B^{2}} & =-\Lambda \\
\dot{P}+\frac{\dot{A}}{A} P-C\left(\frac{2}{A^{2}}-\frac{1}{B}\right) & =0 \\
-\frac{\ddot{B}}{2 B}-\frac{\dot{A} \dot{B}}{2 A B}-\frac{A^{2}}{2 B^{2}}+\frac{1}{B} & =\Lambda
\end{aligned}$$
where
$$P=\frac{1}{2 B}(B \dot{C}-C \dot{B}) .$$
Only the third of (23) contains $C$ so we leave it until last. From the others, by elimination of second derivatives, we obtain
$$H:=\frac{\dot{B}^{2}}{2 B^{2}}+2 \frac{\dot{A} \dot{B}}{A B}+\frac{A^{2}}{2 B^{2}}-\frac{2}{B}+2 \Lambda=0,$$
which is the Hamiltonian constraint (and is conserved by virtue of the others).
Define
$$q:=\frac{\dot{B}^{2}}{A^{2} B}-\frac{1}{B},$$
then $\dot{q}=0$ by virtue of (23), so $q=c_{1}$. Evidently the system (23) is now equivalent to this and (24), together with the equation for $P$, and we deduce
$$A^{2}=\frac{\dot{B}^{2}}{1+c_{1} B}$$
for constant $c_{1}$. Use this to eliminate $A$ from (24) to find
$$\ddot{B}+\frac{\left(2-c_{1} B\right)}{4 B\left(1+c_{1} B\right)} \dot{B}^{2}=1-\Lambda B .$$
This integrates to give, if $c_{1} \neq 0$
$$\dot{B}^{2}=F(B)$$
with
$$F(B):=\frac{2}{c_{1}^{3} B}\left(-\frac{2 \Lambda}{3}\left(1+c_{1} B\right)^{3}+2\left(c_{1}+2 \Lambda\right)\left(1+c_{1} B\right)^{2}+2\left(c_{1}+\Lambda\right)\left(1+c_{1} B\right)+c_{2}\left(1+c_{1} B\right)^{3 / 2}\right),$$
with a second constant of integration $c_{2}$, while if $c_{1}=0$
$$\dot{B}^{2}=F(B):=\frac{c_{2}}{B}+B-\frac{2 \Lambda}{3} B^{2} .$$
Now go back to (23) to find $C$. First note
$$A P=\frac{\dot{B}^{2}}{2\left(1+c_{1} B\right)^{1 / 2}}\left(\frac{d C}{d B}-\frac{C}{B}\right)=\frac{B F(B)}{2\left(1+c_{1} B\right)^{1 / 2}} \frac{d}{d B}\left(\frac{C}{B}\right),$$
so that the third of (23) is
$$\frac{d}{d B}\left(\frac{B F}{2\left(1+c_{1} B\right)^{1 / 2}} \frac{d}{d B}\left(\frac{C}{B}\right)\right)=\frac{C}{B} \frac{1}{\left(1+c_{1} B\right)^{1 / 2}}\left(\frac{2 B\left(1+c_{1} B\right)}{F}-1\right) .$$
This is a second-order linear ODE for $C$ which we can suppose has been solved, the solution incorporating two more constants $c_{3}, c_{4}$. The metric is
$$g=d t^{2}-A^{2} \sigma_{1}^{2}+\left(\sigma_{2}-\sigma_{3}\right)\left((B+C) \sigma_{2}+(B-C) \sigma_{3}\right),$$
so use $B$ as time-coordinate to obtain a solution depending on $c_{1}, \ldots, c_{4}$ and $\Lambda$ :
$$g=\frac{d B^{2}}{F(B)}-\frac{F(B)}{1+c_{1} B} \sigma_{1}^{2}+B\left(\sigma_{2}^{2}-\sigma_{3}^{2}\right)+C(B)\left(\sigma_{2}-\sigma_{3}\right)^{2},$$
where we are assuming $F(B)$ and $C(B)$ are known.
In the special case $c_{1}=c_{2}=0$ we have $F=B-\frac{2 \Lambda}{3} B^{2}$ and (28) has the general solution
$$C=c_{3} \frac{B^{2}(1-\Lambda B / 6)}{(1-2 \Lambda B / 3)^{2}}+c_{4} \frac{8 \Lambda^{2} B^{2}-8 \Lambda B+3}{(1-2 \Lambda B / 3)^{2} B},$$
which, with $c_{4}=0$, is recognisable as the solution in equation (7.5) of [3]. Thus that particular nondiagonalisable type VIII Einstein metric complexifies to a nondiagonalisable type IX metric.

There is another simple special case: $c_{1}=0=\Lambda$. Then $F(B)=B+c_{2} B^{-1}$, and (28) has the general solution
$$C=\frac{c_{3} B+3 c_{4} c_{2} B^{2}+c_{4} B^{4}}{c_{2}+B^{2}},$$
with constants of integration $c_{3}, c_{4}$. With $B=r^{2} / 4$ the metric can be written
$$g=\frac{d r^{2}}{1+c_{5} / r^{4}}-\frac{r^{2}}{4}\left(1+c_{5} / r^{4}\right) \sigma_{1}^{2}+\frac{r^{2}}{4}\left(\sigma_{2}^{2}-\sigma_{3}^{2}\right)+\left(\frac{4 c_{3}}{r^{2}}+3 c_{4} c_{5}+c_{4} r^{4}\right)\left(1+c_{5} / r^{4}\right)^{-1}\left(\sigma_{2}-\sigma_{3}\right)^{2} .$$
The Riemann tensor for this metric is SD iff $c_{4}=0$. This metric bears some resemblance to the Eguchi-Hansen metric but it seems to be new.
3.2.2. Solving the Einstein equations for the (22). The metric is
$$g=d t^{2}-\left(\sigma_{1}+\sigma_{2}\right)\left(\left(A^{2}+B\right) \sigma_{1}-\left(A^{2}-B\right) \sigma_{2}+2 C \sigma_{3}\right)-A^{2} \sigma_{3}^{2},$$
with $A \neq 0$. Choose the basis of forms to be
$$\theta^{0}=d t, \quad \theta^{1}=A \sigma_{3}, \quad \theta^{2}=\sigma_{1}+\sigma_{2}, \quad \theta^{3}=\frac{1}{2}\left(A^{2}+B\right) \sigma_{1}-\frac{1}{2}\left(A^{2}-B\right) \sigma_{2}+C \sigma_{3},$$
so that
$$g_{00}=-g_{11}=-g_{23}=1 .$$
Now calculate the Einstein equations as
$$\begin{aligned}
3 \frac{\ddot{A}}{A} & =-\Lambda \\
\frac{\ddot{A}}{A}+2 \frac{\dot{A}^{2}}{A^{2}}-\frac{1}{2 A^{2}} & =-\Lambda \\
\ddot{C}-\frac{\dot{A} \dot{C}}{A}-2 C\left(\frac{\ddot{A}}{A}+\frac{1}{A^{2}}\right) & =0 \\
\ddot{B}-\frac{\dot{A} \dot{B}}{A}-2 B\left(\frac{\ddot{A}}{A}+\frac{1}{A^{2}}\right) & =6 \frac{C^{2}}{A^{4}}+\left(\frac{\dot{C}}{A}-2 \frac{\dot{A} C}{A^{2}}\right)^{2}
\end{aligned}$$
Eliminate $\ddot{A}$ from the first pair to obtain
$$\frac{\dot{A}^{2}}{A^{2}}-\frac{1}{4 A^{2}}=-\Lambda / 3,$$
which is the Hamiltonian constraint. Solutions are
$$\text { For } \Lambda=-3 H^{2}, \quad A=\frac{1}{2 H} \sinh H t ; \quad \text { for } \Lambda=3 H^{2}, \quad A=\frac{1}{2 H} \sin H t .$$
We can deal simultaneously with both signs of $\Lambda$ by introducing
$$z=-2 \dot{A}\left(\frac{3}{\Lambda}\right)^{1 / 2}, \text { so that } \dot{z}=2 A\left(\frac{\Lambda}{3}\right)^{1 / 2}=\left(1-\frac{\Lambda}{3} z^{2}\right)^{1 / 2} .$$
Set $C=F / A^{2}$ in (33) then
$$\left(1-\frac{\Lambda}{3} z^{2}\right) \frac{d^{2} F}{d z^{2}}+\frac{4 \Lambda z}{3} \frac{d F}{d z}-\frac{4 \Lambda}{3} F=0$$
which is solved by
$$F=c_{1} z+c_{2}\left(z^{4}-\frac{18}{\Lambda} z^{2}-\frac{27}{\Lambda^{2}}\right) .$$
Then with $B=G / A^{2}$, (34) becomes
$$\left(1-\frac{\Lambda}{3} z^{2}\right) \frac{d^{2} G}{d z^{2}}+\frac{4 \Lambda z}{3} \frac{d G}{d z}-\frac{4 \Lambda}{3} G=6 C^{2}+(A \dot{C}-2 \dot{A} C)^{2} .$$
with solution
$$G=P I+c_{3} z+c_{4}\left(z^{4}-\frac{18}{\Lambda} z^{2}-\frac{27}{\Lambda^{2}}\right),$$
where $P I$ is the particular integral. Again the metric is obtained subject to solving a secondorder linear ODE.

For vacuum $(\Lambda=0)$ we can obtain the general solution in (4-parameter) closed form:
$$A=\frac{t}{2}, \quad C=\frac{c_{1}}{t^{2}}+c_{2} t^{4}, \quad B=\frac{4 c_{1}^{2}}{t^{6}}-16 c_{1} c_{2}+7 c_{2}^{2} t^{6}+\frac{c_{3}}{t^{2}}+c_{4} t^{4} .$$
This is flat iff $B=C=0$ and it has Weyl tensor which is SD for $c_{2}=0=c_{4}$, or ASD for $c_{1}=0=c_{3}$.

\section*{4. Other types}

If the isometry group admits a 2-dimensional Abelian subgroup and the metric is orthogonally transitive (OT) then the methods of twistor theory can be used to find all Einstein solutions of any signature (see [8], examples in [1],[10] and self-dual Kahler examples in [2]). This will include all Bianchi types except for VIII and IX. Generically, there should be a reduction to a Painlevé equation (as happens in [1] for the Bianchi III examples treated there, which are OT for the group generated by $\left\langle\partial_{x}, \partial_{y}\right\rangle$ ) but type I, as seen above, is actually solvable in elementary functions (and the metrics found are all OT for the subgroup generated by $\left(\partial_{y}, \partial_{z}\right)$ ). It is possible to solve type II and obtain some examples which are not OT (and not in [10]).
4.1. Type II. Consider the metric
$$g=d t^{2}+a^{2} \sigma_{1}^{2}+b^{2} \sigma_{2}^{2}+\left(f \sigma_{2}+c \sigma_{3}\right)^{2},$$
with
$$d \sigma_{1}=\sigma_{2} \wedge \sigma_{3}, \quad d \sigma_{2}=0=d \sigma_{3},$$
which is therefore Bianchi type II. It is convenient to introduce coordinates $(x, y, z)$ by
$$\sigma_{1}=d x+y d z, \quad \sigma_{2}=d y, \quad \sigma_{3}=d z,$$
with corresponding Killing vectors
$$X_{1}=\partial_{x}, \quad X_{2}=\partial_{y}-z \partial_{x}, \quad X_{3}=\partial_{z} .$$
Abelian subgroups of the isometry group are generated by $<X_{1}, X_{2}>$ or $<X_{1}, X_{3}>$ but in both cases orthogonal transitivity implies diagonalisable, so that nondiagonalisable examples will not be OT.

For later use we note that the differential algebra of invariant 1-forms has the symmetry
$$\left(\sigma_{1}, \sigma_{2}, \sigma_{3}\right) \rightarrow\left(\mu^{-1} \nu^{-1} \sigma_{1}, \mu^{-1} \sigma_{2}, \nu^{-1} \sigma_{3}\right)$$
for nonzero constants $\mu, \nu$ and under which the metric components change according to
$$(a, b, c, f) \rightarrow(\mu \nu a, \mu b, \nu c, \mu f) .$$
We exploit this symmetry below to fix some constants.
The Einstein equations are
$$\begin{aligned}
\frac{\ddot{a}}{a}+\frac{\ddot{b}}{b}+\frac{\ddot{c}}{c}+2 L^{2} & =-\Lambda \\
\frac{\ddot{a}}{a}+\frac{\dot{a} \dot{b}}{a b}+\frac{\dot{a} \dot{c}}{a c}-\frac{a^{2}}{2 b^{2} c^{2}} & =-\Lambda \\
\frac{\ddot{b}}{b}+\frac{\dot{a} \dot{b}}{a b}+\frac{\dot{b} \dot{c}}{b c}+2 L^{2}+\frac{a^{2}}{2 b^{2} c^{2}} & =-\Lambda \\
\frac{\ddot{c}}{c}+\frac{\dot{a} \dot{c}}{a c}+\frac{\dot{b} \dot{c}}{b c}-2 L^{2}+\frac{a^{2}}{2 b^{2} c^{2}} & =-\Lambda \\
\dot{L}+\left(\frac{\dot{a}}{a}+2 \frac{\dot{c}}{c}\right) L & =0,
\end{aligned}$$
where
$$L=\frac{1}{2}\left(\frac{\dot{f}}{b}-\frac{f \dot{c}}{c b}\right) .$$
The Hamiltonian constraint is
$$\frac{\dot{a} \dot{b}}{a b}+\frac{\dot{b} \dot{c}}{b c}+\frac{\dot{c} \dot{a}}{c a}-L^{2}+\frac{a^{2}}{4 b^{2} c^{2}}+\Lambda=0 .$$
From the last of (37) deduce
$$L=\frac{c_{1}}{a c^{2}} .$$

In fact $c_{1}$ is one of the two twist potentials for the Abelian subgroup generated by $<X_{1}, X_{3}>$, the other being automatically zero. We insist that $c_{1} \neq 0$ since otherwise the metric is both OT and diagonalisable.

To proceed, change the time-coordinate by
$$d t=a c^{2} d \tau, \text { so } \frac{d}{d \tau}=a c^{2} \frac{d}{d t},$$
for then
$$\frac{d}{d \tau}\left(\frac{f}{c}\right)=2 a b c L=2 c_{1}\left(\frac{b}{c}\right) .$$
Next set $b=X c$, eliminate $\Lambda$ between the third and fourth of (37) and substitute to find
$$\frac{\ddot{X}}{X}+\left(\frac{\dot{a}}{a}+2 \frac{\dot{c}}{c}\right) \frac{\dot{X}}{X}+4 L^{2}=0,$$
or equivalently
$$\frac{d^{2} X}{d \tau^{2}}+4 c_{1}^{2} X=0$$
which is readily solved. Under the symmetry (36) we have $X \rightarrow \mu \nu^{-1} X$ so without loss of generality we may suppose that
$$X=\sin \left(2 c_{1} \tau\right),$$
and the symmetry is reduced to (36) but with $\mu=\nu$. Next the second of (37) translates to
$$\frac{d}{d \tau}\left(\frac{X}{a} \frac{d a}{d \tau}\right)=\frac{a^{4}}{2 X}-\Lambda a^{2} c^{4} X .$$
To make progress, set $\Lambda=0$, when
$$X^{2}\left(\frac{d a}{d \tau}\right)^{2}=\frac{1}{4}\left(a^{6}+c_{2} a^{2}\right),$$
for new constant $c_{2}$ which we suppose for now is nonzero and positive. The residual freedom in (36) allows us to set $c_{2}=4$. Now
$$\frac{2 d a}{a\left(a^{4}+4\right)^{1 / 2}}=\frac{d \tau}{X} .$$
This can be simplified by setting $a^{4}=16 g /(g-1)^{2}$ for then
$$g=c_{3}\left(\tan c_{1} \tau\right)^{-2 / c_{1}} .$$
To find $c$ we go back to the Hamiltonian constraint and calculate
$$0=a^{2} c^{4} H=\left(\frac{c^{\prime}}{c}+\frac{a^{\prime}}{a}+\frac{X^{\prime}}{2 X}\right)^{2}-\frac{1}{4}\left(\frac{X^{\prime}}{X}\right)^{2}-c_{1}^{2}-\frac{1}{X^{2}},$$
with prime for $d / d \tau$. With $X$ known, this gives
$$a c X^{1 / 2}=c_{4}\left(\tan c_{1} \tau\right)^{\beta / 2 c_{1}} \text { where } \beta^{2}=c_{1}^{2}+1 .$$
This will give $c$ and therefore the general vacuum solution. Solutions with $c_{2}<0$ can be obtained by analytic continuation and solutions with $c_{2}=0$ are SD. They have neutral signature, and are not cited in the list of type II solutions in [10]. The metric can be written in the form
$$g=\frac{1}{8 c_{1}^{3}}\left(v_{0}-v\right) e^{-2 v} d v^{2}+\frac{2 c_{1}}{v_{0}-v} \sigma_{1}^{2}+\frac{\left(v_{0}-v\right)}{2 c_{1}} e^{-v}\left(\cosh v\left(\sigma_{2}^{2}+\sigma_{3}^{2}\right)+2 \sinh v \sigma_{2} \sigma_{3}\right) .$$

\section*{Appendix}

Here we address the question of how many distinct ways there are to obtain real type VIII metrics by taking slices of diagonal complex type IX metrics. We shall see that the two choices made in Section 3.1 are essentially all, up to equivalences.

With $\sigma_{i}, \Sigma_{i}$ the invariant 1-forms for type VIII and type IX respectively, set $\sigma=\left(\sigma_{1}, \sigma_{2}, \sigma_{3}\right)^{T}$ and $\Sigma=\left(\Sigma_{1}, \Sigma_{2}, \Sigma_{3}\right)^{T}$. There is freedom
$$\sigma \rightarrow L \sigma, \quad \Sigma \rightarrow P^{T} \Sigma$$
for real Lorentz transformation $L$ and complex orthogonal $P$. Suppose the forms are related by
$$\sigma=M \Sigma=\overline{M \Sigma},$$
where the second equation is the reality condition. The allowed freedom has the effect
$$M \rightarrow L M P,$$
so, provided the top row of $M$ is not a null vector we can use complex $P$ to set the top row of $M$ to be $(\alpha, 0,0)$ with $\alpha \neq 0$. (If the top row of $M$ is a null vector then we can use real $P$ to set it to be $a(1, i, 0)$ for nonzero real $a$, in which case
$$\sigma_{1}=a\left(\Sigma_{1}+i \Sigma_{2}\right) \text { when } \sigma_{1} \wedge d \sigma_{1}=0,$$
which is a contradiction.)
Now
$$\sigma_{1}=\alpha \Sigma_{1}, \quad \sigma_{2}=\beta \Sigma_{1}+\gamma \Sigma_{2}+\delta \Sigma_{3}, \quad \sigma_{3}=\lambda \Sigma_{1}+\mu \Sigma_{2}+\nu \Sigma_{3}$$
for some $\beta, \gamma, \delta, \lambda, \mu, \nu$. From the exterior derivatives
$$d \sigma_{1}=\alpha d \Sigma_{1}=\alpha \Sigma_{2} \wedge \Sigma_{3}$$
but also
$$=2 \sigma_{2} \wedge \sigma_{3}=2\left(\beta \Sigma_{1}+\gamma \Sigma_{2}+\delta \Sigma_{3}\right) \wedge\left(\lambda \Sigma_{1}+\mu \Sigma_{2}+\nu \Sigma_{3}\right) .$$
Thus
$$\beta \nu-\lambda \delta=0=\beta \mu-\lambda \gamma, \quad 2(\gamma \nu-\delta \mu)=\alpha,$$
whence $\beta=0=\lambda$. With $M$ parametrised as
$$M=\left(\begin{array}{cc}
\alpha & 0 \\
0 & \tilde{M}
\end{array}\right),$$
parametrise $\tilde{M}$ as
$$\left(\begin{array}{ll}
\beta & \gamma \\
\delta & \epsilon
\end{array}\right)$$
then
$$d \sigma_{2}=\beta d \Sigma_{2}+\gamma d \Sigma_{3}=\beta \Sigma_{3} \wedge \Sigma_{1}+\gamma \Sigma_{1} \wedge \Sigma_{2}$$
but also
$$=-\sigma_{3} \wedge \sigma_{1}=-\alpha\left(\delta \Sigma_{2}+\epsilon \Sigma_{3}\right) \wedge \Sigma_{1}$$
so that
$$\alpha \delta=\gamma, \quad \alpha \epsilon=-\beta .$$
Consideration of $d \sigma_{3}$ similarly leads to
$$\alpha \beta=\epsilon, \quad \alpha \gamma=-\delta,$$
so that, since e.g. $\beta$ and $\gamma$ are not both zero, we deduce that $\alpha^{2}=-1$. Without loss of generality we may choose $\alpha=i$ whence also
$$\epsilon=i \beta, \quad \delta=-i \gamma .$$
The remaining condition from consideration of $d \sigma_{1}$ now entails
$$\beta^{2}+\gamma^{2}=1 .$$

The complex type IX metric is
$$g=d t^{2}+A \Sigma_{1}^{2}+B \Sigma_{2}^{2}+C \Sigma_{3}^{2},$$
and we wish to obtain a real type VIII metric as
$$\begin{gathered}
=d t^{2}-A \sigma_{1}^{2}+B\left(\beta \sigma_{2}+i \gamma \sigma_{3}\right)^{2}+C\left(\gamma \sigma_{2}-i \beta \sigma_{3}\right)^{2} \\
=d t^{2}-A \sigma_{1}^{2}+\left(B \beta^{2}+C \gamma^{2}\right) \sigma_{2}^{2}+2 i \beta \gamma(B-C) \sigma_{2} \sigma_{3}-\left(B \gamma^{2}+C \beta^{2}\right) \sigma_{3}^{2} .
\end{gathered}$$
For this to be real we require the following to be real
$$A, \quad B \beta^{2}+C \gamma^{2}, \quad B \gamma^{2}+C \beta^{2}, \quad i \beta \gamma(B-C) .$$
By taking combinations of the last three (first minus second plus or minus twice the third) we see that $(\beta \pm i \gamma)^{2}(B-C)$ must be real and therefore so must $(\beta+i \gamma)^{2} /(\beta-i \gamma)^{2}$, so that
$$(\beta+i \gamma)^{2}(\bar{\beta}+i \bar{\gamma})^{2}=(\beta-i \gamma)^{2}(\bar{\beta}-i \bar{\gamma})^{2}$$
whence
$$(\beta \bar{\beta}-\gamma \bar{\gamma})(\gamma \bar{\beta}+\beta \bar{\gamma})=0 .$$
Note that
$$(\beta \bar{\beta}-\gamma \bar{\gamma})^{2}+(\gamma \bar{\beta}+\beta \bar{\gamma})^{2}=1$$
by virtue of (41) so that there is no loss of generality in supposing that whichever factor is zero in (42) the other factor can be assumed to be one.

The reality conditions on the $\Sigma_{i}$ are
$$\bar{\Sigma}_{1}=-\Sigma_{1}, \quad \beta \Sigma_{2}+\gamma \Sigma_{3}=\overline{\beta \Sigma}_{2}+\bar{\gamma} \bar{\Sigma}_{3}, \quad-i \gamma \Sigma_{2}+i \beta \Sigma_{3}=i \bar{\gamma} \bar{\Sigma}_{2}-i \overline{\beta \Sigma}_{3},$$
whence also
$$\Sigma_{2}=(\beta \bar{\beta}-\gamma \bar{\gamma}) \bar{\Sigma}_{2}+(\gamma \bar{\beta}+\beta \bar{\gamma}) \bar{\Sigma}_{3}, \quad \Sigma_{3}=(\gamma \bar{\beta}+\beta \bar{\gamma}) \bar{\Sigma}_{2}-(\beta \bar{\beta}-\gamma \bar{\gamma}) \bar{\Sigma}_{3} .$$
Now by(42) these simplify and we have just two choices: either
$$\Sigma_{2}=\bar{\Sigma}_{2}, \quad \Sigma_{3}=-\bar{\Sigma}_{3}$$
which is Kamada's choice (17) or
$$\Sigma_{2}=\bar{\Sigma}_{3}$$
which is (19), the other choice.

\section*{References}
\begin{itemize}
\item[] [1] T. Christodoulakis and P. A. Terzis, The General Solution of Bianchi Type III Vacuum Cosmology, Class.Quant.Grav. 24 (2007) 875-887 arXiv:gr-qc/0607063.
\item[] [2] M. Dunajski and P. Plansangkate, Scalar-flat Kähler metrics with conformal Bianchi V symmetry. Classical Quantum Gravity 28 (2011), 125004.
\item[] [3] M. Dunajski and T. Mettler, Gauge theory on projective surfaces and anti-self-dual Einstein metrics in dimension four arXiv:1509.04276.
\item[] [4] G. F. R. Ellis and M. A. H. MacCallum, A class of homogeneous cosmological models. Comm. Math. Phys. 12 (1969) 108141.
\item[] [5] H. Kamada and Y. Machida, Self-duality of metrics of type $(2,2)$ on four-dimensional manifolds. Tohoku Math. J. 49 (1997), 259-275.
\item[] [6] A. Krasiński, C. Behr, E. Schücking, F.B. Estabrook, H. D. Wahlquist, G. F. R. Ellis, R. Jantzen and W. Kundt, The Bianchi classification in the Schücking-Behr approach Gen. Relativity Gravitation 35 (2003) 475489.
\item[] [7] V. N. Lukash Gravitational waves that conserve the homogeneity of space (in Russian), Zh.Eks.Teor.Fiz. 67 (1974) 1594.
\item[] [8] L. J. Mason and N. M. J. Woodhouse Integrability, Self-Duality, and Twistor Theory, (1997) LMS Monograph, O.U.P. Oxford.
\item[] [9] H. Stephani, D. Kramer, M. MacCallum, C. Hoenselaers, and E. Herlt (2003) Exact Solutions of Einstein's Field Equations (2003), CUP.
\item[] [10] P. A. Terzis and T. Christodoulakis, Lie algebra automorphisms as Lie point symmetries and the solution space for Bianchi Type I, II, IV, V vacuum geometries, Class. Quantum Grav. 29 (2012) 235007 arXiv:1007.1561.
\item[] [11] K. P. Tod, Cohomogeneity-one metrics with self-dual Weyl tensor, in 'Twistor theory (Plymouth)', 171184, Lecture Notes in Pure and Appl. Math., 169, Dekker, New York, 1995.
\end{itemize}
\begin{itemize}
\item[] [12] R. S. Ward, Stationary axisymmetric space-times: a new approach. Gen. Relativity Gravitation 15 (1983), no. 2, 105109.
\item[] [13] L. Witten, Static axially symmetric solutions of self-dual SU(2) gauge fields in Euclidean four-dimensional space Phys. Rev. D 19, 718 (1979)
\end{itemize}

Department of Applied Mathematics and Theoretical Physics, University of Cambridge, Wilberforce Road, Cambridge CB3 0WA, UK.
E-mail address: m.dunajski@damtp.cam.ac.uk
The Mathematical Institute, Oxford University, Woodstock Road, Oxford OX2 6GG, UK.
E-mail address: tod@maths.ox.ac.uk
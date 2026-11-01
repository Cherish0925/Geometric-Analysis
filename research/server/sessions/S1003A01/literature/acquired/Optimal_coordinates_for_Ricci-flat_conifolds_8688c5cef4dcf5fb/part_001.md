---
retention_scope: session
part: 1
total_parts: 2
---

[Part 1/2 of: Optimal coordinates for Ricci-flat conifolds]

---
source_file: 2203_01711.pdf
converter: mathpix
format: mmd
---

\title{
Optimal coordinates for Ricci-flat conifolds
}

\author{
Klaus Kröncke ${ }^{1}$ and Áron Szabó ${ }^{2}$ \\ ${ }^{1}$ Department of Mathematics, KTH Royal Institute of Technology \\ Lindstedtsvägen 25 \\ 11428 Stockholm, Sweden \\ ${ }^{2}$ Institute of Astronomy, Nicolaus Copernicus University \\ Grudziądzka 5 \\ 87-100 Toruń, Poland \\ E-mail: kroncke@kth.se \\ aron.szabo@v.umk.pl
}

\begin{abstract}
We compute the indicial roots of the Lichnerowicz Laplacian on Ricci-flat cones and give a detailed description of the corresponding radially homogeneous tensor fields in its kernel. For a Ricci-flat conifold $(M, g)$ which may have asymptotically conical as well as conically singular ends, we compute at each end a lower bound for the order with which the metric converges to the tangent cone. As a special subcase of our result, we show that any Ricci-flat ALE manifold ( $M^{n}, g$ ) is of order $n$ and thereby close a small gap in a paper by Cheeger and Tian.
\end{abstract}

\section*{1 Introduction and main results}

Ricci-flat metrics belong perhaps to the most interesting class of Riemannian metrics studied in differential geometry and theoretical physics. Compact Ricci-flat manifolds are particularly hard to find. For a long time, any known compact Ricci-flat manifold was actually flat until the resolution of the Calabi conjecture by Yau provided the existence of other examples [Yau78].

It is easier to construct Ricci-flat metrics on noncompact manifolds where a lot of recent work has been focusing on. The Ricci-flat manifolds we are considering in this paper are allowed to have a finite number of ends which are either asymptotically conical or conically singular. We will refer to these with the unifying notion of conifolds.

Various examples of asymptotically conical Ricci-flat manifolds have been discovered so far. In the subclass of Ricci-flat asymptotically locally Euclidean (ALE for short) manifolds, many examples are provided by Kronheimer's classification [Kro89]. Asymptotically conical Ricci-flat manifolds which are not ALE were found in [BS89, Böh99]. Various additional examples were found over the last decade, see e.g. [CH13, Chi19, FHN21]. On the other hand, many examples of Ricci-flat orbifolds are known (e.g. noncollapsed limits of compact Ricci-flat 4 -manifolds [And90]) and conically singular (nonorbifold) Ricci-flat metrics were constructed in [HS17].

The goal of this paper lies in computing for each end of an arbitrary Ricci-flat conifold the precise order. We compute a formula for the optimal decay, given entirely in terms of spectral data on the link of the cone. This extends previous work of [BKN89, CT94, CH13], who focus on the ALE situation or the Kähler case.

A necessary step in order to compute this order lies in computing possible growth and decay rates for solutions of the linearization of the equation $\mathrm{Ric}=0$ on the tangent cone. The linearization is up to a gauge term given by the Lichnerowicz Laplacian and the growth and decay rates are known as indicial roots. We give a complete computation of all indicial roots, based on the idea of commuting operators and the formulas we get are surprisingly simple.

\subsection*{1.1 Indicial roots of the Lichnerowicz Laplacian on Ricci-flat cones}

Let $\widehat{M}^{n-1}$ be a closed manifold and let $\bar{P}$ be a self-adjoint Laplace type operator on $\bar{M}=(0, \infty) \times \widehat{M}$, which is of the form
$$\bar{P}=-\partial_{r r}^{2}-\frac{n-2}{n} \partial_{r}+\frac{1}{r^{2}} \widehat{P}$$
for some Laplace type operator $\widehat{P}$ on $\widehat{M}$. The Laplace-Beltrami operator with respect to the cone metric on $\bar{M}$ is the simplest operator of this type, but we also allow more general Laplace type operators on vector bundles. The Hodge Laplacian acting on the exterior algebra and the aforementioned Lichnerowicz Laplacian on symmetric 2-tensors are typical examples. If $\bar{P}$ is of such a form and $\nu \in \mathbb{R}$ is an eigenvalue of $\widehat{P}$, we call the (possibly complex) values
$$\xi_{ \pm}(\nu):=-\frac{n-2}{2} \pm \sqrt{\frac{(n-2)^{2}}{4}+\nu}$$
indicial roots of $\bar{P}$ (here, we use the convention $\sqrt{x}:=\sqrt{|x|} \cdot i$ for $x<0$ ). Their union is called indicial set of $\bar{P}$. The real parts of the indicial roots correspond to possible growth and decay rates of radially homogeneous solutions of the equation
$$\bar{P} u=0 .$$
For the Laplace-Beltrami operator on the cone $\bar{M}$, the indicial roots are just calculated from the Laplace eigenvalues on $\widehat{M}$. For more general operators on vector bundles which are of this form, these are in general much harder to compute.

For an operator like the Lichnerowicz Laplacians, it seems to be particularly difficult, since the Lichnerowicz Laplacians on $\widehat{M}$ and $\bar{M}$ are in a very complicated relation to each other, see the formulas in [GMS18, Lemma 7.4] and [Del07, Lemma 4.3] which are lenghty and not very practical for our purposes. This comes from the fact that one has to split up the symmetric (0, 2)-tensors on $\bar{M}$ in radial, tangential and mixed components and the covariant derivative does not preserve this splitting. Our first main result overcomes these problems in the case of Ricci-flat cones.

Theorem 1.1. Let $\left(\bar{M}^{n}, \bar{g}\right)$ be a Ricci-flat cone over a closed manifold $\left(\widehat{M}^{n-1}, g\right)$ with $\widehat{\operatorname{Ric}}=(n-2) \widehat{g}$. Let $0=\lambda_{0}<\lambda_{1} \ldots$ be the eigenvalues of the Laplace-Beltrami operator on $\widehat{M}, \mu_{1}<\mu_{2}<\ldots$ be the eigenvalues of the connection Laplacian on divergence-free 1-forms on $\widehat{M}$ and $\kappa_{1}<\kappa_{2}<\ldots$ be the eigenvalues of the Einstein operator on transverse and traceless tensors on $\widehat{M}$.
\begin{itemize}
\item[(i)] The indicial set of the Lichnerowicz Laplacian $\bar{\Delta}_{L}$ on $\bar{M}$ is given by
$$\begin{aligned}
& \left\{\xi_{ \pm}\left(\kappa_{i}\right), \xi_{ \pm}\left(\mu_{i}+1\right)-1, \xi_{ \pm}\left(\mu_{i}+1\right)+1, \xi_{ \pm}\left(\lambda_{i}\right)-2, \xi_{ \pm}\left(\lambda_{i}\right), \xi_{ \pm}\left(\lambda_{i}\right)+2 \mid i \in \mathbb{N}\right\} \\
& \quad \cup\{-n, 2-n, 0,2\}
\end{aligned}$$
\item[(ii)] The indicial set of $\bar{\Delta}_{L}$ on tensors satisfying the linearized Bianchi gauge is given by
$$\left\{\xi_{ \pm}\left(\kappa_{i}\right), \xi_{ \pm}\left(\mu_{i}+1\right)-1, \xi_{ \pm}\left(\lambda_{i}\right)-2, \xi_{ \pm}\left(\lambda_{i}\right) \mid i \in \mathbb{N}\right\} \cup\{-n, 0\} .$$
\item[(iii)] The indicial set of $\bar{\Delta}_{L}$ on tensors satisfying the linearized Bianchi gauge, but which are not Lie derivatives, is given by
$$E:=\left\{\xi_{ \pm}\left(\kappa_{i}\right), \xi_{ \pm}\left(\lambda_{i}\right) \mid i \in \mathbb{N}\right\} .$$
\end{itemize}

The main result follows from Theorem 3.15 and Proposition 3.20 below. We find the indicial roots by writing down all possible growth and decay rates of radially homogeneous tensors in $\operatorname{ker}\left(\bar{\Delta}_{L}\right)$. Let us briefly outline how we get all these tensors (recall that a tensor with vanishing trace and divergence is called a TT-tensor):
\begin{itemize}
\item[-] If $h$ is a TT-tensor on $\widehat{M}$, any $r^{\alpha} h$ is a TT-tensor on $\bar{M}$. It is quite straightforward to show that if $\widehat{\Delta}_{E} h=\kappa h$ (where $\widehat{\Delta}_{E}$ is the Einstein operator on $\widehat{M}$ ), then $r^{\xi_{ \pm}(\kappa)} h \in \operatorname{ker}\left(\bar{\Delta}_{L}\right)$.
\item[-] If $v \in C^{\infty}(\widehat{M})$ satisfies $\widehat{\Delta} v=\lambda v$, then $r^{\xi_{ \pm}(\lambda)} v$ is harmonic on $\bar{M}$ and therefore, we also have that $r^{\xi_{ \pm}(\lambda)} v \cdot \bar{g} \in \operatorname{ker}\left(\bar{\Delta}_{L}\right)$.
\end{itemize}
In these two cases, the TT and the conformality condition simplify the calculations to a great extent. It would be however far too complicated to work out the general formulas after relaxing these conditions. Instead, in order to get all other $r$-homogeneous tensors in $\operatorname{ker}\left(\bar{\Delta}_{L}\right)$, we exploit commutation formulas involving $\bar{\Delta}_{L}$ and other operators to a great extent:
\begin{itemize}
\item[-] If $\omega$ is a divergence-free 1 -form on $\widehat{M}$ such that $\widehat{\Delta}_{1} \omega:=\widehat{\nabla}^{*} \widehat{\nabla} \omega=\mu \cdot \omega$, then a short calculation shows that $r^{\xi_{ \pm}(\mu+1)} \omega$ is again divergence free and $\bar{\Delta}_{1}\left(r^{\xi_{ \pm}(\mu+1)} \omega\right)=0$. If we now apply the symmetric part $\bar{\delta}^{*}$ of the covariant derivative, we get $\bar{\Delta}_{L}\left(\bar{\delta}^{*}\left(r^{\xi_{ \pm}(\mu+1)} \omega\right)\right)=0$ due to a commutation formula for Ricci-flat manifolds. In addition, we have $\bar{\delta}^{*}\left(r^{\xi_{ \pm}(\mu+1)} \omega\right)=\mathcal{O}\left(r^{\xi_{ \pm}(\mu+1)-1}\right)$ and so, $\xi_{ \pm}(\mu+1)-1$ are both indicial roots. Because $\bar{\Delta}_{L}$ is also of the form (1.1) all indicial roots must be of the form (1.2). Thus, there are further indicial roots which are dual to those two. More precisely, $\xi_{+}(\mu+1)+1$ appears as the weight dual to $\xi_{-}(\mu+1)-1$ and $\xi_{+}(\mu+1)+1$ appears as the weight dual to $\xi_{-}(\mu+1)-1$.
\end{itemize}
- We extend this kind of argumentation when we discuss further indicial roots coming from eigenfunctions of the Laplace-Beltrami operator. If $v \in C^{\infty}(\widehat{M})$ satisfies $\widehat{\Delta} v=\lambda v$, then $v_{ \pm}:=r^{\xi_{ \pm}(\lambda)} v$ are harmonic on $\bar{M}$. By commutation, $d v_{ \pm} \in \operatorname{ker}\left(\bar{\Delta}_{1}\right)$, with $d v_{ \pm}=\mathcal{O}\left(r^{\xi_{ \pm}(\lambda)-1}\right)$. Thus, $\xi_{ \pm}(\lambda)-1$ are both indicial roots of $\bar{\Delta}_{1}$ and as in the previous duality argument, there are also the dual weights $\xi_{\mp}(\lambda)+1$, with corresponding harmonic forms $\omega_{+}=r^{\xi_{+}(\lambda)-\xi_{-}(\lambda)+2} d v_{-}$and $\omega_{-}=r^{\xi-(\lambda)-\xi_{+}(\lambda)+2} d v_{+}$. Applying $\bar{\delta}^{*}$ to $d v_{ \pm}$and $\omega_{ \pm}$yields four elements in $\operatorname{ker}\left(\bar{\Delta}_{L}\right)$ with decay rates
$$\left\{\left(\xi_{ \pm}(\lambda)-1\right)-1,\left(\xi_{ \pm}(\lambda)+1\right)-1\right\}=\left\{\xi_{ \pm}(\lambda), \xi_{ \pm}(\lambda)-2\right\} .$$
Again, duality implies that $\xi_{ \pm}(\lambda)+2$ is also an indicial root as it is dual to $\xi_{\mp}(\lambda)-2$. Finally, if $\lambda=0$ (and hence $v$ is constant), some of the constructed tensors vanish, which is why we need to deal only with the four values
$$\{-n, 2-n, 0,2\}=\left\{\xi_{-}(0)-2, \xi_{-}(0), \xi_{+}(0), \xi_{+}(0)+2\right\} .$$
To conclude the proof, one of course needs to show that the above arguments have, in fact, constructed all the indicial roots. The method explained here not only allows us to compute the indicial roots in an efficient way, but also enables us to read of almost directly which of the corresponding tensors are geometrically essential (cf. Theorem 1.1 (ii) and (iii)).

As a byproduct of our result, we get a new proof of the following theorem (cf. page 22):
Theorem 1.2 ([Krö17, Theorem 1.2]). With the notation of Theorem 1.1 we have $\bar{\Delta}_{L} \geq 0$ in the $L^{2}$-sense if and only if the TT-eigenvalues of the Einstein operator satisfy
$$\kappa_{i} \geq-\frac{(n-2)^{2}}{4} \quad \text { for all } i \in \mathbb{N} .$$

The condition $\bar{\Delta}_{L} \geq 0$ is referred in the literature as the condition of linear stability, which appears in the study of the Einstein-Hilbert action (see e.g. [Bes08, Chapter 4G]) and in the study of dynamical stability of fixed points of the Ricci flow (see e.g. [Ses06]).

The proof in [Krö17] is based on a suitable decomposition of the space of symmetric ( 0,2 )-tensors on $\bar{M}$ and many tedious $L^{2}$-estimates. The new proof presented in this paper is much more stringent and due to Theorem 1.1, the structure of $\bar{\Delta}_{L}$ on the cone is now understood in much greater detail.

Besides its importance for the computation of the order of Ricci-flat AC/CS ends (cf. Definition 1.3), we think that Theorem 1.1 is also of great independent interest. Moreover, there are further potential applications, for example the desingularization of Einstein conifolds by smooth Einstein metrics. In addition, the method of using commuting operators to compute indicial roots can also be used for other operators, in particular the Hodge Laplacian for the exterior algebra, for which the exterior derivative and its adjoint would serve as commuting operators. This could in turn be used to compute convergence rates of other geometric structures at infinity.

\subsection*{1.2 The order of Ricci-flat conifolds}

Let us start this subsection by making the notion of conifolds precise.
Definition 1.3. A manifold $M^{n}$ is called a manifold with ends if there exists a compact subset $K \subset M$, called the core of $M$, such that
\begin{itemize}
\item[(i)] $M \backslash K$ consists of a disjoint union of connected manifolds $M_{i}, i=1, \ldots N$, called the ends of $M$, and
\item[(ii)] for each $i=1, \ldots N$, there exists a closed manifold $\widehat{M}_{i}$ such that $M_{i}$ is diffeomorphic to the manifold $(0, \infty) \times \widehat{M}_{i}$.
\end{itemize}

In the following, we use the convention $\nabla^{0}:=\mathrm{id}$.
Definition 1.4. Let $M^{n}$ be a manifold with ends $M_{i}, i=1, \ldots, N$, endowed with a Riemannian metric $g$.
\begin{itemize}
\item[(i)] We say that an end $M_{i}$ is called asymptotically conical if there exist constants $\tau_{i}, R_{i}>0$, a Riemannian metric $\widehat{g}_{i}$ on $\widehat{M}_{i}$ and a diffeomorphism $\varphi_{i}: M_{i} \rightarrow\left(R_{i}, \infty\right) \times \widehat{M}_{i}$ such that
$$\left|\bar{\nabla}^{k}\left(\left(\varphi_{i}\right)_{*} g-\overline{g_{i}}\right)\right|_{\overline{g_{i}}}=\mathcal{O}\left(r^{-\tau_{i}-k}\right), \quad r \rightarrow \infty,$$
where $\bar{g}_{i}=d r^{2}+r^{2} \widehat{g}_{i}$ denotes the cone metric on $(0, \infty) \times \widehat{M}_{i}$ and $\bar{\nabla}$ denotes its Levi-Civita connection.
\item[(ii)] We say that an end $M_{i}$ is called conically singular if there exist constants $\tau_{i}, R_{i}>0$, a Riemannian metric $\widehat{g}_{i}$ on $\widehat{M}_{i}$ and a diffeomorphism $\varphi_{i}: M_{i} \rightarrow\left(0, R_{i}\right) \times \widehat{M}_{i}$ such that
$$\left|\bar{\nabla}^{k}\left(\left(\varphi_{i}\right)_{*} g-\overline{g_{i}}\right)\right|_{\overline{g_{i}}}=\mathcal{O}\left(r^{+\tau_{i}-k}\right), \quad r \rightarrow 0,$$
where, again, $\bar{g}_{i}=d r^{2}+r^{2} \widehat{g}_{i}$ denotes the cone metric on $(0, \infty) \times \widehat{M}_{i}$ and $\bar{\nabla}$ denotes its Levi-Civita connection.
\end{itemize}

In both cases, $\varphi_{i}$ is called an asymptotic chart and $\tau_{i}$ is called an order of the end $M_{i}$. We call the manifold $\left((0, \infty) \times \widehat{M}_{i}, \bar{g}_{i}\right)$ the tangent cone of the end $M_{i}$, and we say that $M_{i}$ is tangent to its tangent cones. Furthermore, we call $(M, g)$
\begin{itemize}
\item[(iii)] asymptotically conical (AC for short) if all ends are asymptotically conical;
\end{itemize}
\begin{itemize}
\item[(iv)] conically singular (CS for short) if all ends are conically singular and
\item[(v)] conifold (AC/CS for short) if each end is either asymptotically conical or conically singular.
\end{itemize}

Evidently, the order of an end is not unique: if an end is of order $\tau$, then it is also of order $\tau^{\prime}$ for any $\tau^{\prime}<\tau$. Our goal in this paper is to find a lower bound for the order which is as large as possible. To cover a special situation, which we later call the resonance-dominated case, we introduce a slightly refined notion of asymptotic order:

Definition 1.5. With the notation of Definition 1.3, an asymptotically conical end $\left(M_{i}, g_{i}\right)$ of a conifold is called asymptotically conical weakly of order $\tau_{i}$ if there exists an asymptotic chart $\phi_{i}$ in which we have for all $k \in \mathbb{N}$ that
$$\left|\bar{\nabla}^{k}\left(\varphi_{i}\right)_{*} g-\overline{g_{i}}\right|_{\overline{g_{i}}}=\mathcal{O}\left(r^{-\tau_{i}-k} \log (r)\right), \quad r \rightarrow \infty .$$
Note that if and AC end is weakly of order $\tau$, then it is of order $\tau-\epsilon$ for all $\epsilon>0$.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/579a0d2d-ff75-44dd-a528-7e314b4c217e-05.jpg?height=587&width=981&top_left_y=1056&top_left_x=551}
\captionsetup{labelformat=empty}
\caption{Figure 1: Schematic picture of a conifold, cf. Definitions 1.3 and 1.4}
\end{figure}

Now let $(\bar{M}, \bar{g})$ be a Ricci-flat cone and $\lambda_{i}, \mu_{i}, \kappa_{i}$ and $E$ as in Theorem 1.1. Denote by $\operatorname{Re}(E) \subset \mathbb{R}$ the set of real parts of elements in $E$ and define
$$E_{+}:=\operatorname{Re}(E) \cap(0, \infty)=\left\{\xi_{+}\left(\kappa_{i}\right), \xi_{+}\left(\lambda_{i}\right) \mid i \in \mathbb{N}, \kappa_{i}>0\right\} .$$
and
$$\begin{aligned}
E_{-}:= & \operatorname{Re}(-E) \cap(0, \infty) \\
=\{ & \left.-\xi_{-}\left(\kappa_{i}\right),-\xi_{-}\left(\lambda_{i}\right) \mid i \in \mathbb{N}\right\} \cup\left\{-\xi_{+}\left(\kappa_{j}\right) \mid i \in \mathbb{N},-\frac{(n-2)^{2}}{4} \leq \kappa_{j}<0\right\} \\
& \cup\left\{\left.-\operatorname{Re}\left(\xi_{ \pm}\left(\kappa_{j}\right)\right)=\frac{n-2}{2} \right\rvert\, i \in \mathbb{N}, \kappa_{j}<-\frac{(n-2)^{2}}{4}\right\},
\end{aligned}$$
see also Figure 2 on page 13. Furthermore, we define
$$\xi_{+}:=\min E_{+} \quad \xi_{-}:=\min E_{-} .$$
Note that both numbers are positive and depend entirely on spectral data on the link ( $\widehat{M}, \widehat{g}$ ) of the cone. Note also that there are no a priori positive lower or upper bounds for $\xi_{+}$and $\xi_{-}$. We write $\xi_{+}(\widehat{M}, \widehat{g})$, resp. $\xi_{-}(\widehat{M}, \widehat{g})$ if we wish to emphasize the dependence of these values on $(\widehat{M}, \widehat{g})$.

Definition 1.6. We call a Ricci-flat cone resonance-dominated if
$$\left\{\kappa_{i} \mid i \in \mathbb{N}\right\} \cap\left[-\frac{(n-2)^{2}}{4}, 0\right)=\left\{-\frac{(n-2)^{2}}{4}\right\} .$$
An end of a conifold is called resonance-dominated if its tangent cone is resonance-dominated.
Now we are able to formulate the second main result of this paper.
Theorem 1.7. Let $\left(M^{n}, g\right)$ be a Ricci-flat conifold with ends $M_{i}, i=1, \ldots, N$, which are modeled by Ricci-flat cones over Einstein manifolds ( $\widehat{M}_{i}, \widehat{g}_{i}$ ). Then the following assertions hold:
\begin{itemize}
\item[(i)] If $M_{i}, i \in\{1, \ldots, N\}$, is an asymptotically conical end, then it is of order $\xi_{-}\left(\widehat{M}_{i}, \widehat{g}_{i}\right)$ if it is not resonance-dominated and weakly of order $\frac{n-2}{2}$ otherwise.
\item[(ii)] If $M_{i}, i \in\{1, \ldots, N\}$, is a conically singular end, then it is of order $\xi_{+}\left(\widehat{M}_{i}, \widehat{g}_{i}\right)$.
\end{itemize}

Remark 1.8. We do not claim here that the largest possible order of each end is exactly $\xi_{ \pm}\left(\widehat{M}_{i}, \widehat{g}_{i}\right)$. For some conifolds, the order could be a priori larger. However one would need to study this with methods adjusted to these specific situations and can not be treated in this general framework. In this paper, we will use the adjective "optimal" in this sense.

The construction of the asymptotic chart is based on a global slice theorem for the action of the diffeomorphism group on the space of metrics. We impose the Bianchi gauge, which is made precise in Definition 4.5 below.

We will prove that given a conifold metric $g$ on a manifold $M$, there exists for any metric $\tilde{g}$ sufficiently close to $g$ in a suitable topology (with respect to weighted Sobolev spaces) a diffeomorphism $\psi$ on $M$ such that up to an arbitrarily small open subset $U$ (which we are free to choose), $g$ is in Bianchi gauge with respect to $\psi^{*} \tilde{g}$. Given a Ricci-flat conifold $(M, g)$, we may choose now $\tilde{g}$ such that it agrees with $g$ in the core of $M$ and (with respect to given asymptotic charts $\varphi_{i}$ ) agrees with the exact cone metrics $\bar{g}_{i}$ at the ends. With the help of Theorem 1.1, we then compute the order of $g-\psi^{*} \tilde{g}$. As a consequence, the new asymptotic charts $\varphi_{i} \circ \psi$ will give us the desired orders.

In contrast to [BKN89, CT94] who construct the gauge locally at the (single) end, our gauge is constructed globally on all of the manifold and gives us the "optimal" asymptotic charts for all ends at once.
Remark 1.9. Intuitively, one may think of an asymptotic order $\tau$ at infinity to be "small" if $\tau<n-2$, since $n-2$ is the decay rate of the fundamental solution of the Laplace equation. By Theorem 1.7, an AC end has small order if $E_{-} \cap(2-n, 0) \neq \emptyset$. By definition of $E_{-}$, this is the case if some $\kappa_{i}$ are negative (this means that the link of the cone is unstable with respect to the Einstein-Hilbert action, cf. [Bes08, Definition 4.63]).

The notion of ADM mass of an asymptotically Euclidean manifold can be generalized to asymptotically conical manifolds.

Definition 1.10. The ADM mass of an asymptotically conical manifold $(M, g)$ with a single end tangent to $\left((0, \infty) \times \widehat{M}, d r^{2}+r^{2} \widehat{g}\right)$ is
$$m_{A D M}(M, g)=-\frac{1}{\operatorname{vol}\left(S^{n-1}\right)} \lim _{R \rightarrow \infty} \int_{\{R\} \times \widehat{M}}\left\langle\delta_{\bar{g}}\left(\varphi_{*} g\right)+d\left(\operatorname{tr}_{\bar{g}} \varphi_{*} g\right), \partial_{r}\right\rangle d V_{R^{2} \widehat{g}}$$
where $\varphi$ is an asymptotic chart.
In view of Remark 1.9 we obtain the following result:
Corollary 1.11. Let $(\bar{M}, \bar{g})$ be a Ricci-flat cone over an Einstein manifold which is linearly stable with respect to the Einstein-Hilbert action. Then any Ricci-flat AC manifold with tangent cone $(\bar{M}, \bar{g})$ has vanishing ADM mass.

If all $\kappa_{i}$ are positive, then $\xi_{-}>n-2$ and the mass clearly vanishes. If $\kappa_{1}=0$, then $\xi_{-}=n-2$, but the leading term of the asymptotic expansion of $\varphi_{*} g-\bar{g}$ is a TT-tensor, see the proof of Theorem 3.15. Therefore, the mass vanishes in this case, too.

Example 1.12. In [CH13], it is shown that the AC Stenzel metric on $T^{*} S^{m}$ has order $2 \frac{m}{m-1}$ and this is the optimal order. This shows that $2 \frac{m}{m-1} \in E_{-}$. Therefore, $\frac{2 m}{m-1}=-\xi_{+}\left(\kappa_{i_{0}}\right)$ for some $i_{0} \in \mathbb{N}$ and we get $\kappa_{i_{0}}<0$ if $m>2$. We deduce that for $m>2$, the link of the tangent cone of the Stenzel metric is unstable with respect to the Einstein-Hilbert action.

Example 1.13. Any 9-dimensional product Einstein manifold $\widehat{M}_{1} \times \widehat{M}_{2}$ with positive Ricci curvature satisfies $\kappa_{1}=-2(m-2)=-\frac{(m-2)^{2}}{4}$ (with $m=10$ ), see e.g. [Krö15, Section 4]. Moreover, if the products are Einstein-Hilbert stable (for example, if both $\widehat{M}_{1}$ and $\widehat{M}_{2}$ are spheres), all other $\kappa_{i}$ are nonnegative. The 10-dimensional cones over such products are resonance-dominated. Ricci-flat AC manifolds tangent to such cones were constructed in [Böh99] and these examples are by definition resonance-dominated as well.

In more specific geometric situations, where the tangent cones are quotients of Euclidean space, we derive the following from Theorem 1.7

Theorem 1.14. Every Ricci-flat orbifold is of order 2.
Theorem 1.15. Every $n$-dimensional Ricci-flat ALE manifold is ALE of order $n$.
In [BKN89], Theorem 1.5], it was shown that every ALE manifold is of order $n-1$ and it is of order $n$ if the manifold is Kähler or if $n=4$. In [CT94, Theorem 5.103], it was already claimed that the assertion of Theorem 1.15 holds. However, the proof contains a tiny gap which seems to have been overlooked so far in the literature.

Let us explain this gap for completeness. The central argument in [CT94, p. 538] is that any harmonic function $f$ on $\mathbb{R}^{n} / \Gamma$ with $f=\mathcal{O}\left(r^{1-n}\right)$ satisfies $f=\mathcal{O}\left(r^{-n}\right)$ if $\Gamma \neq\{1\}$. This is because the leading order term is exactly of the form $x \mapsto\langle x, a\rangle r^{-1}$ for some $a \in \mathbb{R}^{n}$ and this is not invariant under any nontrivial $\Gamma$. For this reason, it was argued that the same decay rate should also hold for a harmonic TT-tensor. However, if $h$ is a harmonic tensor on $\mathbb{R}^{n} / \Gamma$, expanded in flat coordinates as
$$h=h_{i j} d x^{i} \otimes d x^{j},$$
then the functions $h_{i j}$ are not necessarily $\Gamma$-invariant, so the above argument for functions cannot be applied. Consider the following example: Equip $\mathbb{R}^{4} \cong \mathbb{C}^{2}$ with complex coordinates $\left(z_{1}, \bar{z}_{1}, z_{2}, \bar{z}_{2}\right)$, where $z_{i}=x_{i}+i y_{i}$ and $\bar{z}_{i}=x_{i}-i y_{i}, i=1,2$. Recall that
$$\Delta=-4\left(\partial_{z_{1}} \circ \partial_{\bar{z}_{1}}+\partial_{z_{2}} \circ \partial_{\bar{z}_{2}}\right)$$
where $\partial_{z_{i}}=1 / 2\left(\partial_{x_{i}}-i \partial_{y_{i}}\right)$ and $\partial_{\bar{z}_{i}}=1 / 2\left(\partial_{x_{i}}+i \partial_{y_{i}}\right)$. The function $f: z \mapsto\left(z_{1}\right)^{3}$ is harmonic and invariant under the multiplicative action of the group $\mathbb{Z}_{3}=\left\{1, e^{\frac{2 i \pi}{3}}, e^{\frac{4 i \pi}{3}}\right\}$ and so is its real part, which is given by the function $g=\operatorname{Re}(f):\left(x_{1}, y_{1}, x_{2}, y_{2}\right) \mapsto\left(x_{1}\right)^{3}-4\left(x_{1}\right)\left(y_{1}\right)^{2}$. The tensor $\nabla^{2} g$ is now harmonic and $\Gamma$-invariant and its component functions are linear. Therefore, $h=r^{-4} \nabla^{2} g$ is another harmonic $\Gamma$-invariant tensor which is of order $\mathcal{O}\left(r^{-3}\right)$.

On the other hand, $h=r^{-4} \nabla^{2} g$ is not a TT-tensor and even its trace-free part is not TT. Thus it does not contradict our results which imply that any harmonic $\Gamma$-invariant TT-tensor decaying at infinity decays of order $n$. But as the example of the function $g$ shows, this cannot be directly concluded from the fact that linear functions are not $\Gamma$-invariant for any nontrivial $\Gamma$.

\subsection*{1.3 Structure of the paper}

In Section 2, we introduce some notations, conventions and commutation formulas which we use throughout the paper. In Section 3, Laplace type operators on cones are discussed in great detail. After collecting a few general statements, we first discuss the connection Laplacian on 1-forms. Building upon this, we are able to unravel the complicated structure of the Lichnerowicz Laplacian on cones and prove Theorems 1.1 and 1.2. Section 4 is devoted to the construction of optimal coordinates on conifolds. After an introduction into weighted function spaces and a discussion of decay of Ricci-flat metrics in Bianchi gauge on cones, we prove a slice theorem for the Bianchi gauge on conifolds. These decay results and the slice theorems are then used to prove Theorem 1.7 before we conclude with an application in the orbifold and ALE cases to prove Theorem 1.14 and Theorem 1.15

\section*{Acknowledgments}

The authors want to thank Daniel Grieser, Uwe Semmelmann and Boris Vertman for helpful discussions. The work of the first author is supported by the DFG through the priority program 2026 Geometry at Infinity. The second author was partially funded by the DFG through the Research Training Group 1670 Mathematics Inspired by String Theory and Quantum Field Theory, and the National Science Center (NCN), Poland under grant number OPUS 2021/41/B/ST9/00757. A part of this paper is based on the PhD thesis of the second author.

\section*{2 Notations, conventions and formulas}

For a Riemannian manifold $(M, g)$ we define the Riemannian curvature tensor with the sign convention such that
$$R_{X, Y} Z=\nabla_{X, Y}^{2} Z-\nabla_{Y, X}^{2} Z, \quad \text { for all } X, Y, Z \in C^{\infty}(T M),$$
where ∇ is the Levi-Civita connection of $g$. The Ricci tensor is denoted by Ric and the scalar curvature by scal. The Laplace-Beltrami operator $\Delta: C^{\infty}(M) \rightarrow C^{\infty}(M)$ with the sign convention such that $\Delta f=-\operatorname{tr} \nabla^{2} f=-g^{i j} \nabla_{i j}^{2} f$. With the same sign convention, we define the connection Laplacians
$$\Delta_{1}=-\operatorname{tr} \nabla^{2}: C^{\infty}\left(T^{*} M\right) \rightarrow C^{\infty}\left(T^{*} M\right), \quad \Delta_{2}=-\operatorname{tr} \nabla^{2}: C^{\infty}\left(S^{2} M\right) \rightarrow C^{\infty}\left(S^{2} M\right),$$
on 1-forms and symmetric (0, 2)-tensors, respectively. To distinguish between these operators and the Laplace-Beltrami operator, we sometimes also use the notation $\Delta_{0}$ instead of $\Delta$.

The symmetric tensor product of $\omega, \eta \in C^{\infty}\left(T^{*} M\right)$ is defined as $\omega \odot \eta=\omega \otimes \eta+\eta \otimes \omega \in C^{\infty}\left(S^{2} M\right)$. The divergences of $\omega \in C^{\infty}\left(T^{*} M\right)$ and $h \in C^{\infty}\left(S^{2} M\right)$ are defined with the sign convention such that
$$\delta \omega=-g^{i j} \nabla_{i} \omega_{j} \in C^{\infty}(M), \quad \delta h_{k}=-g^{i j} \nabla_{i} h_{j k} \in C^{\infty}\left(T^{*} M\right),$$
respectively. The formal adjoint $\delta^{*}: C^{\infty}\left(T^{*} M\right) \rightarrow C^{\infty}\left(S^{2} M\right)$ of $\delta$ is given by
$$\left(\delta^{*} \omega\right)_{i j}=\frac{1}{2}\left(\nabla_{i} \omega_{j}+\nabla_{j} \omega_{i}\right) .$$
Note that $\delta^{*} d f=\nabla^{2} f$ for any $f \in C^{\infty}(M)$ and that $\delta^{*}$ is related to the Lie derivative by $2 \delta^{*} \omega=\mathcal{L}_{\omega^{\sharp}} g$, where $\omega^{\sharp} \in C^{\infty}(T M)$ is the dual vector field of $\omega$ with respect to $g$. Note moreover that $\operatorname{tr} \circ \delta^{*}=-\delta$. We also have trace-free versions of $\delta^{*}$ and $\nabla^{2}$, given by
$$\begin{aligned}
\stackrel{\circ}{\delta}^{*} \omega & :=\delta^{*} \omega-\frac{1}{n} \operatorname{tr}\left(\delta^{*} \omega\right) g=\delta^{*} \omega+\frac{1}{n} \delta \omega \cdot g \\
\stackrel{\circ}{\nabla}^{2} f & :=\stackrel{\circ}{\delta}^{*} d f=\nabla^{2} f+\frac{1}{n} \Delta f \cdot g
\end{aligned}$$
Furthermore, we introduce the Bianchi operator, given by
$$B:=\delta+\frac{1}{2} d \circ \operatorname{tr}: C^{\infty}\left(S^{2} M\right) \rightarrow C^{\infty}\left(T^{*} M\right) .$$
This notion comes from the fact that $B$ arises from linearizing the Bianchi gauge condition $V(g, \tilde{g})=0$, where the vector field $V(g, \tilde{g})$ depending on two Riemannian metrics $g, \tilde{g}$ is given in local coordinates by
$$V(g, \tilde{g})^{l}:=g^{i j}\left(\Gamma(g)_{i j}^{l}-\Gamma(\tilde{g})_{i j}^{l}\right) .$$
More precisely, a short calculation shows
$$B(h)=\left.\frac{d}{d t}\right|_{t=0} V(g+t h, g)=-\left.\frac{d}{d t}\right|_{t=0} V(g, g+t h) .$$
The Lichnerowicz Laplacian $\Delta_{L}: C^{\infty}\left(S^{2} M\right) \rightarrow C^{\infty}\left(S^{2} M\right)$ is defined by
$$\Delta_{L} h=\Delta_{2} h-\operatorname{Ric} \circ h+h \circ \operatorname{Ric}-2 \stackrel{\circ}{R} h,$$
where $(h \circ k)_{i j}=g^{m n} k_{i m} h_{j m}$, and the full curvature term is $\stackrel{\circ}{R} h_{i j}=g^{k m} g^{l n} R_{i k l j} h_{m n}$, where $R_{i k l j}=$ $g\left(R_{\partial_{i}, \partial_{k}} \partial_{l}, \partial_{j}\right)$. The term $\stackrel{\circ}{R} \in \operatorname{End}\left(S^{2} M\right)$ is called the curvature potential. Up to a gauge term, $1 / 2 \cdot \Delta_{L}$ is the linearization of the Ricci tensor. More precisely, we have
$$\left.\frac{d}{d t}\right|_{t=0} \operatorname{Ric}_{g+t h}=\frac{1}{2} \Delta_{L} h-\delta^{*}(B h)=\frac{1}{2}\left(\Delta_{L} h-\mathcal{L}_{(B h)^{\sharp}} g\right),$$
see [Bes08, Theorem 1.174]. The Einstein operator $\Delta_{E}: C^{\infty}\left(S^{2} M\right) \rightarrow C^{\infty}\left(S^{2} M\right)$ is defined by
$$\Delta_{E} h=\Delta_{2} h-2 \stackrel{\circ}{R} h .$$
Note that the two operators are related by $\Delta_{L}=\Delta_{E}+2 \lambda$ whenever Ric $=\lambda \cdot g$. In this case, we additionally have
$$\left.\frac{d}{d t}\right|_{t=0}\left[\operatorname{Ric}_{g+t h}-\lambda(g+t h)\right]=\frac{1}{2} \Delta_{E} h-\delta^{*}(B h)=\frac{1}{2}\left(\Delta_{E} h-\mathcal{L}_{(B h)^{\sharp}} g\right),$$
which is easily seen from (2.9). If $\left(M^{n}, g\right)$ is Einstein with $\operatorname{Ric}_{g}=\lambda \cdot g$, we furthermore have a variety of commutation identities involving these differential operators: For $v \in C^{\infty}(M), \omega \in C^{\infty}\left(T^{*} M\right)$ and $h \in C^{\infty}\left(S^{2} M\right)$, we have
$$\begin{aligned}
\Delta_{1}(d v) & =d\left(\Delta_{0} v-\lambda v\right), & \Delta_{0}(\delta \omega) & =\delta\left(\Delta_{1} \omega+\lambda \omega\right), \\
\Delta_{E}\left(\delta^{*} \omega\right) & =\delta^{*}\left(\Delta_{1} \omega-\lambda \omega\right), & \Delta_{1}(\delta h) & =\delta\left(\Delta_{E} h+\lambda h\right), \\
\Delta_{E}\left(\nabla^{2} v\right) & =\nabla^{2}\left(\Delta_{0} v-2 \lambda v\right), & \Delta_{0}(\delta \delta h) & =\delta \delta\left(\Delta_{E} h+2 \lambda h\right), \\
\Delta_{E}(v \cdot g) & =(\Delta v-2 \lambda v) g, & \Delta(\operatorname{tr} h) & =\operatorname{tr}\left(\Delta_{E} h+2 \lambda h\right) .
\end{aligned}$$

The computations can be found in [Lic61], see also [Krö15] p. 8]. Note that the third line follows trivially from the first and the second line and that the formulas on the right-hand side follow from the ones on the left-hand side by taking the formal adjoints. Also, note that from (2.11), we can deduce in an obvious way other commutation formulas involving the operators $\Delta_{L}, \stackrel{\circ}{\delta}^{*}, \stackrel{\circ}{\nabla}^{2}$ and $B$.

The spectrum of a differential operator $P$ is denoted by $\operatorname{spec}(P)$ and its strictly positive part is denoted by $\operatorname{spec}_{+}(P)=\operatorname{spec}(P) \cap(0, \infty)$. If $\lambda$ is an eigenvalue of the operator $P$, we denote the corresponding eigenspace by $E(P, \lambda)$.

For a section $u$ of a Riemannian vector bundle with metric connection, we write $u=\mathcal{O}_{k}\left(r^{\alpha}\right)$ if $\left|\nabla^{l} u\right|=\mathcal{O}\left(r^{\alpha-l}\right)$ for all $l=0, \ldots k$ and $u=\mathcal{O}_{\infty}\left(r^{\alpha}\right)$ if $u=\mathcal{O}_{k}\left(r^{\alpha}\right)$ for all $k \in \mathbb{N}$. Furthermore, we write $u=\mathcal{O}_{k}\left(r^{\alpha} \log r\right)$ if $\left|\nabla^{l} u\right|=\mathcal{O}\left(r^{\alpha-l} \log (r)\right)$ for all $l=0, \ldots k$ and $u=\mathcal{O}_{\infty}\left(r^{\alpha} \log (r)\right)$ if $u=\mathcal{O}_{k}\left(r^{\alpha} \log (r)\right)$ for all $k \in \mathbb{N}$.

For a vector bundle $V$, we denote by $C^{\infty}(V), C^{2, \alpha}(V)$ etc. the space of sections with respective regularity. If $P$ is a differential operator acting on sections of $V$, we denote by $\operatorname{ker}_{C^{\infty}}(P), \operatorname{ker}_{C^{2, \alpha}}(P)$ etc. the elements in the kernel of $P$ with respective regularity, cf. [Pac13]. While $S^{2} M$ denotes the bundle of all symmetric (0,2)-tensors, the subset $S_{+}^{2} M \subset S^{2} M$ is the set of all positive definite scalar products over all points of $M$. Although $S_{+}^{2} M$ does not form a vector bundle, we denote for notational convenience by $C^{\infty}\left(S_{+}^{2} M\right), C^{2, \alpha}\left(S_{+}^{2} M\right)$ etc. the set of Riemannian metrics with the respective regularity.

There are several metrics of interest in this paper, and the interplay between them is crucial. For brevity, a system of diacritical marks has been implemented in the notation. Metrics, covariant derivatives, curvatures, Laplace type operators and bundles connected to the link, a Riemannian cone and a generic metric are denoted by hats ( $\widehat{g}, \widehat{\nabla}$ etc.), overlines ( $\bar{g}, \bar{\nabla}$ etc.) and tildes ( $\tilde{g}, \tilde{\nabla}$ etc.), respectively. Moreover, geometric objects connected to the conifold metric under consideration carry no diacritical marks. This convention is not applied to tangential operators.

\section*{3 Ricci-flat cones and their tangential operators}

Throughout this section, we fix a smooth closed Riemannian manifold ( $\widehat{M}, \widehat{g}$ ) of dimension $n-1$ (with $n>2$ ) and its $n$-dimensional cone, denoted by
$$(\bar{M}, \bar{g})=\left(\mathbb{R}_{+} \times \widehat{M}, d r^{2}+r^{2} \widehat{g}\right),$$
where $r$ is the canonical coordinate on $\mathbb{R}$. We will use the canonical projections to pull back objects on $\widehat{M}$ to objects on $\bar{M}$. For notational convenience, we will drop the explicit reference to the projections. We denote the indices corresponding to coordinates on $\widehat{M}$ by $i, j, k, \ldots$, and the index $r$ refers to the $r$-coordinate in the manifold $\bar{M}$. Let us denote the indices corresponding to coordinates on $\bar{M}$ by $\alpha, \beta, \gamma$. The Christoffel symbols on $\bar{M}$ are related to the ones on $\widehat{M}$ by
$$\bar{\Gamma}_{i j}^{k}=\widehat{\Gamma}_{i j}^{k}, \quad \bar{\Gamma}_{i j}^{r}=-r \cdot g_{i j}, \quad \bar{\Gamma}_{i r}^{j}=\bar{\Gamma}_{r i}^{j}=\frac{1}{r} \delta_{i}^{j},$$
while the other Christoffel symbols vanish. Therefore. the curvature tensors of $\bar{g}$ and $\widehat{g}$ are related by
$$\bar{R}_{i j k l}=r^{2}\left(\widehat{R}_{i j k l}+\left(\widehat{g}_{i k} \widehat{g}_{j l}-\widehat{g}_{i l} \widehat{g}_{j k}\right)\right),$$
while the other components of $\bar{R}$ vanish. Consequently, the Ricci tensors are related by
$$\overline{\operatorname{Ric}}_{i j}=\widehat{\operatorname{Ric}}_{i j}-(n-2) \widehat{g}_{i j},$$
while the other components of $\overline{\operatorname{Ric}}_{i j}$ vanish. In particular, $(\bar{M}, \bar{g})$ is Ricci-flat if and only if $(\widehat{M}, \widehat{g})$ is Einstein with $\widehat{\operatorname{Ric}}=(n-2) \widehat{g}$. Note that this latter condition can be achieved via a homothetic rescaling for any positive Einstein manifold. In this situation, we call $(\bar{M}, \bar{g})$ the Ricci-flat cone over $(\widehat{M}, \widehat{g})$. We will assume from now on that $(\bar{M}, \bar{g})$ is Ricci-flat.

\subsection*{3.1 Conical and tangential operators}

Let $\bar{V}$ be a Riemannian vector bundle over $\bar{M}$ with metric connection $\bar{\nabla}$ and denote its restriction by $\widehat{V}:=\bar{V}_{\{1\} \times \widehat{M}}$. By identifying the bundle restrictions $\left.\widehat{V}\right|_{\{r\} \times \widehat{M}}$ with each other via parallel transport along radial lines (i.e. curves of the form $\gamma(t):=(t, p)$ for fixed $p \in \widehat{M}$ ), we get a natural identification
$$C^{\infty}(\bar{V}) \cong C^{\infty}\left(\mathbb{R}_{+}, C^{\infty}(\widehat{V})\right) .$$
Via this parallel transport, we will sometimes consider sections in $\widehat{V}$ as sections in $\bar{V}$, without mentioning the extension of the domain from $\widehat{M} \cong\{1\} \times \widehat{M}$ to $\bar{M}$ explicitly. Let us assume that all the induced connections ${ }^{r} \nabla$ on $\left.\bar{V}\right|_{\{r\} \times \widehat{M}} \cong \widehat{V}$ do coincide. We denote this connection on $\widehat{V}$ by $\widehat{\bar{\nabla}}$.
Definition 3.1. A self-adjoint Laplace type operator $\bar{\Delta}_{\bar{V}}$ acting on $C^{\infty}(\bar{V})$ is called a conical operator if it is with respect to (3.4) of the form
$$\bar{\Delta}_{\bar{V}}=-\partial_{r r}^{2}-\frac{n-1}{r} \partial_{r}+\frac{1}{r^{2}} \square_{\widehat{V}},$$
where $\square_{\widehat{V}}$ is a self-adjoint Laplace type operator acting on $C^{\infty}(\widehat{V})$. We we call $\square_{\widehat{V}}$ the tangential operator of $\bar{\Delta}_{\bar{V}}$.
Lemma 3.2. If $\bar{\Delta}_{\bar{V}}=\bar{\nabla}^{*} \bar{\nabla}$ is the connection Laplacian of $\bar{V}$, then it is a conical operator and its tangential operator is the connection Laplacian $\widehat{\bar{\nabla}}^{*} \widehat{\bar{\nabla}}=-\widehat{g}^{i j}\left(\bar{\nabla}_{i} \bar{\nabla}_{j}-\bar{\nabla}_{\widehat{\nabla}_{\partial_{i} \partial_{j}}}\right)$ of the induced connection $\widehat{\bar{\nabla}}$ on $\widehat{V}$ with respect to the metric $\widehat{g}$.

Proof. This simply follows from writing
$$\bar{\nabla}^{*} \bar{\nabla}=-\bar{g}^{\alpha \beta}\left(\bar{\nabla}_{\alpha} \bar{\nabla}_{\beta}+\bar{\nabla}_{\bar{\nabla}_{\partial_{\alpha} \partial_{\beta}}}\right)=-\bar{\nabla}_{r} \bar{\nabla}_{r}-\frac{n-1}{r} \bar{\nabla}_{r}-r^{-2} \widehat{g}^{i j}\left(\bar{\nabla}_{i} \bar{\nabla}_{j}-\bar{\nabla}_{\widehat{\nabla}_{\partial_{i}} \partial_{j}}\right),$$
and observing that $\bar{\nabla}_{r} \sim \partial_{r}$ via (3.4). \(\square\)

Lemma 3.3. If $\bar{\Delta}_{\bar{V}}=\bar{\nabla}^{*} \bar{\nabla}+\bar{A}$ with a potential $\bar{A} \in C^{\infty}(\operatorname{End}(\bar{V}))$, then $\bar{\Delta}_{\bar{V}}$ is a conical operator if and only if $\bar{R}=r^{-2} \widehat{A}$ for some potential $\widehat{A} \in C^{\infty}(\operatorname{End}(\widehat{V}))$.
Proof. This is obvious. \(\square\)

Example 3.4. The Laplace-Beltrami operator on $\bar{M}$ is a conical operator and its tangential operator is the Laplace-Beltrami operator on $\widehat{M}$.
Example 3.5. Let $\bar{\Delta}_{1}$ be the connection Laplacian on $T^{*} \bar{M}$, and let $x^{i}$ be coordinates on $\widehat{M}$. Because $\bar{\nabla}_{r} d r=0$ and $\bar{\nabla}_{r}\left(r d x^{i}\right)=0$ the natural identification $\left.\left.T^{*} \bar{M}\right|_{\{1\} \times \widehat{M}} \cong T^{*} \bar{M}\right|_{\{r\} \times \widehat{M}}$ is given by
$$\omega_{r} d r+\omega_{i} d x^{i} \sim \omega_{r} d r+r \omega_{i} d x^{i}$$
It is easy to see that this identification is compatible with the natural connection on $T^{*} \bar{M}$. Thus by Lemma 3.2. $\bar{\Delta}_{1}$ is a conical operator.
Example 3.6. Let $\bar{\Delta}_{L}$ be the Lichnerowicz Laplacian on $S^{2} \bar{M}$. The identification $\left.S^{2} \bar{M}\right|_{\{1\} \times \widehat{M}} \cong$ $\left.S^{2} \bar{M}\right|_{\{r\} \times \widehat{M}}$ coming from parallel transport is given by
$$h_{r r} d r \otimes d r+h_{r i} d r \odot d x^{i}+h_{i j} d x^{i} \otimes d x^{j} \sim h_{r r} d r \otimes d r+r h_{r i} d r \odot d x^{i}+r^{2} h_{i j} d x^{i} \otimes d x^{j} .$$
Again, checking that this identification is compatible with the natural connection on $S^{2} \bar{M}$ is straightforward. Furthermore, the curvature potential $\stackrel{\circ}{\bar{R}} \in C^{\infty}\left(\operatorname{End}\left(S^{2} \bar{M}\right)\right)$ scales correctly under that identification. Thus by Lemma 3.3, $\bar{\Delta}_{L}$ is a conical operator. We denote its tangential operator by $\square_{L}$.

\subsection*{3.2 Harmonic sections of conical operators}

Recall the indicial root functions $\xi_{ \pm}$from (1.2) and let us introduce
$$\eta: \mathbb{C} \rightarrow \mathbb{C}, \quad \eta(x)=x(x+n-2) .$$
By definition,
$$\xi_{ \pm}(x) \in \mathbb{R} \quad \forall x \in\left[-\frac{(n-2)^{2}}{4}, \infty\right),$$
and $\eta$ restricts to a function $\eta: \mathbb{R} \rightarrow \mathbb{R}$. Furthermore, it is easy to see that
$$\begin{aligned}
\eta\left(\xi_{ \pm}(x)\right) & =x, & \xi_{+}(x) \xi_{-}(x) & =-x & & \forall x \in \mathbb{R}, \\
\xi_{+}(\eta(x)) & =x, & \xi_{-}(\eta(x)) & =x+2-n & & \forall x \in \mathbb{R},\left[\frac{2-n}{2}, \infty\right), \\
\xi_{-}(\eta(x)) & =x, & \xi_{+}(\eta(x)) & =x+n-2 & & \forall x \in\left(-\infty, \frac{2-n}{2}\right], \\
\xi_{+}(x)+\xi_{-}(x) & =2-n & \xi_{+}(x)-\xi_{-}(x) & =\sqrt{(n-2)^{2}+4 x} & & \forall x \in \mathbb{R} .
\end{aligned}$$
The following Lemma is obvious from (3.5):
Lemma 3.7. Let $\bar{\Delta}_{\bar{V}}$ be a conical self-adjoint Laplace type operator with tangential operator $\square_{\widehat{V}}$. If $u \in C^{\infty}(\widehat{V})$ satisfies $\square_{\widehat{V}} u=\nu u$ for some $\nu \in \mathbb{R}$, then
$$\bar{\Delta}_{\bar{V}}\left(r^{\xi_{ \pm}(\nu)} u\right)=0 .$$
If $\nu=-\frac{(n-2)^{2}}{4}$, then $\xi_{+}(\nu)=\xi_{-}(\nu)=-\frac{n-2}{2}$ and we also have
$$\bar{\Delta}_{\bar{V}}\left(r^{-\frac{n-2}{2}} \log (r) u\right)=0 .$$
Conversely, if $\bar{u} \in \operatorname{ker}\left(\bar{\Delta}_{\bar{V}}\right)$ is of the form $\bar{u}=r^{\alpha} u$ or $\bar{u}=r^{\alpha} \log (r) u$, with $u \in C^{\infty}(E)$, then we have
$$\square_{\widehat{V}}(u)=\eta(\alpha) u .$$

Definition 3.8. An element $\alpha \in\left\{\xi_{ \pm}(\nu) \mid \nu \in \operatorname{spec}\left(\bar{\Delta}_{\bar{V}}\right)\right\}$ is called an indicial root of $\bar{\Delta}_{\bar{V}}$.
Note that self-adjointness and ellipticity of $\bar{\Delta}_{\bar{V}}$ get inherited to $\square_{\widehat{V}}$ and therefore spec( $\square_{\widehat{V}}$ ) consists solely of eigenvalues of finite multiplicity which tend to infinity. In particular only a finite number of eigenvalues can be negative, a fact we will use later. Let now $\left\{\nu_{i} \mid i \in \mathbb{N}\right\}$ be the eigenvalues of $\square_{\widehat{V}}$, counted with multiplicity and $\left\{u_{i} \in C^{\infty}(\widehat{V}) \mid i \in \mathbb{N}\right\}$ be an orthonormal basis of $L^{2}(\widehat{V})$ such that $\square_{\widehat{V}}\left(u_{i}\right)=\nu_{i} \cdot u_{i}$. Then every $\bar{u} \in \operatorname{ker}\left(\bar{\Delta}_{\bar{V}}\right)$ can be expanded as
$$\bar{u}=\sum_{\substack{i=1 \\ \nu_{i} \neq-\frac{(n-2)^{2}}{4}}}^{\infty}\left(a_{i} r^{\xi_{+}\left(\nu_{i}\right)}+b_{i} r^{\xi_{-}\left(\nu_{i}\right)}\right) u_{i}+\sum_{\substack{j=1 \\ \nu_{j}=-\frac{(n-2)^{2}}{4}}}^{\infty}\left(a_{j} r^{-\frac{n-2}{2}}+b_{j} r^{-\frac{n-2}{2}} \log (r)\right) u_{j},$$
with constants $a_{i}, a_{j}, b_{i}, b_{j}$, which may have to be complex in order to ensure that $\bar{u}$ is real. Note that for $\nu_{i}<-\frac{(n-2)^{2}}{4}$, we have
$$\operatorname{Re}\left(a_{i} r^{\xi_{+}\left(\nu_{i}\right)}+b_{i} r^{\xi_{-}\left(\nu_{i}\right)}\right)=r^{\operatorname{Re}\left(\xi_{+}\left(\nu_{i}\right)\right)}\left(c_{i} \cos \left(\log \left(\operatorname{Im} \xi_{+}\left(\nu_{i}\right)\right)+d_{i} \sin \left(\log \left(\operatorname{Im} \xi_{+}\left(\nu_{i}\right)\right)\right)\right)\right.$$
for some constants $c_{i}, d_{i} \in \mathbb{R}$. Now, let
$$\xi_{+}^{\widehat{V}}:=\min \left\{\operatorname{Re}\left(\xi_{ \pm}\left(\nu_{i}\right)\right) \mid i \in \mathbb{N}\right\} \cap(0, \infty), \quad \xi_{-}^{\widehat{V}}:=\min \left\{-\operatorname{Re}\left(\xi_{ \pm}\left(\nu_{i}\right)\right) \mid i \in \mathbb{N}\right\} \cap(0, \infty) .$$
A straightforward consequence for the boundary behavior of harmonic sections is the following:
Corollary 3.9. Let $\bar{u} \in \operatorname{ker}\left(\bar{\Delta}_{\bar{V}}\right)$, not necessarily defined on all of $\bar{M}$.
\begin{itemize}
\item[(i)] If $\bar{u}$ is defined on $(0, \epsilon) \times \widehat{M}$ and $|\bar{u}| \rightarrow 0$ as $r \rightarrow 0$, then $\bar{u}=\mathcal{O}_{\infty}\left(r^{\xi \hat{V}}\right)$ as $r \rightarrow 0$.
\item[(ii)] If $\bar{u}$ is defined on $(R, \infty) \times \widehat{M}$ and $|\bar{u}| \rightarrow 0$ as $r \rightarrow \infty$, then we divide into two subcases:
\begin{itemize}
\item[] (iia) If $\operatorname{spec}\left(\square_{\widehat{V}}\right) \cap\left[-\frac{(n-2)^{2}}{4}, 0\right) \neq\left\{-\frac{(n-2)^{2}}{4}\right\}$, then $\bar{u}=\mathcal{O}_{\infty}\left(r^{-\xi_{-}^{\widehat{V}}}\right)$ as $r \rightarrow \infty$.
\item[] (iib) If $\operatorname{spec}\left(\square_{\widehat{V}}\right) \cap\left[-\frac{(n-2)^{2}}{4}, 0\right)=\left\{-\frac{(n-2)^{2}}{4}\right\}$, then $\bar{u}=\mathcal{O}_{\infty}\left(r^{-\frac{n-2}{2}} \log (r)\right)$ as $r \rightarrow \infty$.
\end{itemize}
\end{itemize}

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/579a0d2d-ff75-44dd-a528-7e314b4c217e-13.jpg?height=611&width=1030&top_left_y=989&top_left_x=520}
\captionsetup{labelformat=empty}
\caption{Figure 2: The decay rate of decaying harmonic fields at infinity (cf. Corollary 3.9). The figure shows the real part of the indicial roots $\xi_{ \pm}$corresponding to eigenvalues, cf. (1.2). Note that the two branches $\xi_{ \pm}$ coincide at the critical point $-\frac{(n-2)^{2}}{4}$ and here a logarithmic factor arises. However, if there is another eigenvalue in the shaded region then a slower decay rate dominates the logarithmic one at infinity.}
\end{figure}

\subsection*{3.3 The tangential operator of the connection Laplacian $\bar{\Delta}_{1}$}

We define
$$D(\widehat{M}):=\left\{\omega \in C^{\infty}\left(T^{*} \widehat{M}\right) \mid \widehat{\delta} \omega=0\right\} .$$
As it is well known from the Hodge decomposition, we have the $L^{2}$-orthogonal splitting
$$C^{\infty}\left(T^{*} \widehat{M}\right)=d\left(C^{\infty}(\widehat{M})\right) \oplus D(\widehat{M}),$$
since $\widehat{M}$ is compact. Due to the commutation rules (2.11), this splitting is preserved by $\widehat{\Delta}_{1}$ and we have
$$\operatorname{spec}\left(\widehat{\Delta}_{1}\right)=\operatorname{spec}\left(\widehat{\Delta}_{0}-(n-2)\right) \cup \operatorname{spec}\left(\left.\widehat{\Delta}_{1}\right|_{D(\widehat{M})}\right) .$$

Let $0=\lambda_{0}<\lambda_{1}<\lambda_{2} \ldots$ be the eigenvalues of $\widehat{\Delta}$ and let $\mu_{1}<\mu_{2}<\mu_{3} \ldots$ be the eigenvalues of $\left.\widehat{\Delta}_{1}\right|_{D(\widehat{M})}$. A standard calculation shows that $\widehat{\Delta}_{1}=2 \widehat{\delta} \circ \widehat{\delta}^{*}+(n-2)$ holds on $D(\widehat{M})$. In particular, $\mu_{i} \geq(n-2)$ for all $i \in \mathbb{N}$ and $\widehat{\Delta}_{1} \omega=(n-2) \omega$ holds if and only if $\widehat{\delta}^{*} \omega=0$, i.e. if $\omega^{\sharp}$ is a Killing vector field. To emphasize this relation to Killing vector fields, we always start to count the $\mu_{i}$ from 0, whenever $(n-2) \in \operatorname{spec}\left(\left.\widehat{\Delta}_{1}\right|_{D(\widehat{M})}\right)$, i.e. we set $\mu_{0}=(n-2)$.

Lemma 3.10. Let $\omega \in D(\widehat{M}), \varphi \in C^{\infty}(0, \infty)$ and $\bar{\omega} \in C^{\infty}\left(T^{*} \bar{M}\right)$ be given by $\bar{\omega}=\varphi \cdot r \omega$. Then,
$$\bar{\delta} \bar{\omega}=0, \quad \bar{\omega}\left(\partial_{r}\right)=0$$
and
$$\bar{\Delta}_{1} \bar{\omega}=r\left(-\partial_{r r}^{2} \varphi \cdot \omega-(n-1) r^{-1} \partial_{r} \varphi \cdot \omega+\varphi \cdot r^{-2}\left(\widehat{\Delta}_{1}+1\right) \omega\right) .$$
Proof. If $\omega$ and $\bar{\omega}$ are as in the statement, (3.2) implies
$$\bar{\nabla}_{i} \bar{\omega}_{j}=\varphi r \widehat{\nabla}_{i} \omega_{j}, \quad \bar{\nabla}_{r} \bar{\omega}_{j}=\partial_{r} \varphi \cdot r \omega_{j}, \quad \bar{\nabla}_{i} \bar{\omega}_{r}=-\varphi \cdot \omega_{j}, \quad \bar{\nabla}_{r} \bar{\omega}_{r}=0,$$
and (3.10) follows by taking the trace and the fact that $\bar{\omega}_{r}=0$. By applying the covariant derivative once again, we obtain from (3.2) that
$$\begin{array}{ll}
\bar{\nabla}_{i j}^{2} \bar{\omega}_{k}=\varphi \cdot r \widehat{\nabla}_{i j}^{2} \omega_{k}+r^{2} \widehat{g}_{i j} \partial_{r} \varphi \cdot \omega_{k}-r \varphi \widehat{g}_{j k} \omega_{i}, & \bar{\nabla}_{r r}^{2} \bar{\omega}_{k}=r \partial_{r r}^{2} \varphi \cdot \omega_{k}, \\
\bar{\nabla}_{i j}^{2} \bar{\omega}_{r}=-\varphi\left(\widehat{\nabla}_{i} \omega_{j}+\widehat{\nabla}_{j} \omega_{i}\right)=-2 \varphi \cdot\left(\widehat{\delta}^{*} \omega\right)_{i j}, & \bar{\nabla}_{r r}^{2} \bar{\omega}_{r}=0
\end{array}$$
and (3.11) follows by taking the trace and using that $\widehat{\delta} \omega=0$. \(\square\)

Proposition 3.11. The spectrum of the tangential operator $\square_{1}$ is given by
$$\operatorname{spec}\left(\square_{1}\right)=\left\{\mu_{i}+1 \mid i \in \mathbb{N}\right\} \cup\left\{\lambda_{i, \pm}^{(1)} \mid i \in \mathbb{N}\right\} \cup\left\{\lambda_{0,-}^{(1)}\right\},$$
where
$$\lambda_{i, \pm}^{(1)}:=\eta\left(\xi_{ \pm}(\lambda)-1\right) .$$
The corresponding eigenspaces are
$$\begin{aligned}
E\left(\square_{1}, \mu_{i}+1\right) & =\left\{\omega \mid \omega \in E\left(\widehat{\Delta}_{1}, \mu_{i}\right)\right\}, \\
E\left(\square_{1}, \lambda_{i, \pm}^{(1)}\right) & =\left\{\xi_{ \pm}(\lambda) v d r+d v \mid v \in E\left(\widehat{\Delta}, \lambda_{i}\right)\right\}, \\
E\left(\square_{1}, \lambda_{0,-}^{(1)}=n-1\right) & =\{\alpha d r \mid \alpha \in \mathbb{R}\},
\end{aligned}$$
where $i \in \mathbb{N}$.
Remark 3.12. The indicial values of $\bar{\Delta}$ and $\bar{\Delta}_{1}$ coming from an eigenfunction $v \in E\left(\widehat{\Delta}, \lambda_{i}\right)$ are related as follows:
$$\xi_{+}\left(\lambda_{i}\right)=\xi_{+}\left(\lambda_{i,+}^{(1)}\right)+1=\xi_{+}\left(\lambda_{i,-}^{(1)}\right)-1, \quad \xi_{-}\left(\lambda_{i}\right)=\xi_{-}\left(\lambda_{i,-}^{(1)}\right)+1=\xi_{-}\left(\lambda_{i,+}^{(1)}\right)-1 .$$
Proof of Proposition 3.11 Let $\omega \in D(\widehat{M})$ be such that $\widehat{\Delta}_{1} \omega=\mu \omega$. Then due to Lemma 3.10, we have
$$r^{\xi_{ \pm}(\mu+1)}(r \omega) \in \operatorname{ker}\left(\bar{\Delta}_{1}\right) .$$

On the other hand, because $\bar{\Delta}_{1}$ is a conical operator, we have
$$\square_{1} \omega=\eta\left(\xi_{ \pm}(\mu+1)\right) \omega=(\mu+1) \omega,$$
which gives the first type of eigenvalues and eigenforms. Now, take $v \in C^{\infty}(\widehat{M})$ with $\widehat{\Delta} v=\lambda v$. Then,
$$r^{\xi_{ \pm}(\lambda)} v \in \operatorname{ker}(\bar{\Delta}),$$
and because $d \circ \bar{\Delta}=\bar{\Delta}_{1} \circ d$, we also get
$$d\left(r^{\xi_{ \pm}(\lambda)} v\right)=r^{\xi_{ \pm}(\lambda)-1}\left(\xi_{ \pm}(\lambda) v d r+r d v\right) \in \operatorname{ker}\left(\bar{\Delta}_{1}\right)$$
because $(\bar{M}, \bar{g})$ is Ricci-flat. Since $\bar{\Delta}_{1}$ is a conical operator, we conclude that the section
$$\xi_{ \pm}(\lambda) v d r+d v \in C^{\infty}\left(\left.T^{*} \bar{M}\right|_{\{1\} \times \widehat{M}}\right)$$
satisfies
$$\square_{1}\left(\xi_{ \pm}(\lambda) v d r+d v\right)=\lambda_{i, \pm}^{(1)}\left(\xi_{ \pm}(\lambda) v d r+d v\right), \quad \lambda_{i, \pm}^{(1)}:=\eta\left(\xi_{ \pm}(\lambda)-1\right) .$$
For $\lambda>0$, observe that the reals $\xi_{ \pm}(\lambda)$ and the section $d v$ are all nonvanishing. For $\lambda=\lambda_{0}=0$, $v \equiv c \in \mathbb{R}$ and $\xi_{+}(0)=0, \xi_{-}(0)=1-n$. Hence,
$$\xi_{+}(\lambda) v d r+d v=0, \quad \xi_{-}(\lambda) v d r+d v=(1-n) c d r, \quad \lambda_{0,-}=0 .$$
We have now constructed all eigenvalues and eigenspaces stated in the proposition. Since the $L^{2}$-span of the $E\left(\widehat{\Delta}, \lambda_{i}\right)$ is already all of $L^{2}(\widehat{M})$ and the $L^{2}$-span of $E\left(\widehat{\Delta}_{1}, \mu_{i}\right)$ is all of $L^{2}(D(\widehat{M}))$, it follows with the help of (3.8) that the $L^{2}$-span of the eigenspaces for $\square_{1}$ we have constructed so far is already all of
$$L^{2}\left(\left.T^{*} \bar{M}\right|_{\{1\} \times \widehat{M}}\right) \cong L^{2}(\widehat{M}) \oplus L^{2}\left(T^{*} \widehat{M}\right) .$$
This finishes the proof of the lemma. \(\square\)

\subsection*{3.4 The tangential operator of the Lichnerowicz Laplacian $\bar{\Delta}_{L}$}

Let us assume in this subsection that the dimension of $\widehat{M}$ is $n-1 \geq 3$. We have the $L^{2}$-orthogonal splitting
$$C^{\infty}\left(S^{2} \widehat{M}\right)=C^{\infty}(\widehat{M}) \cdot \widehat{g} \oplus\left\{n \widehat{\nabla}^{2} v+\widehat{\Delta} v \cdot \widehat{g} \mid v \in C^{\infty}(\widehat{M})\right\} \oplus \widehat{\delta}^{*}(D(\widehat{M})) \oplus T T(\widehat{M}),$$
where $T T(\widehat{M})=\left\{h \in C^{\infty}\left(S^{2} \widehat{M}\right) \mid \widehat{\operatorname{tr}} h=0, \widehat{\delta} h=0\right\}$ denotes the space of transverse traceless tensors on $\widehat{M}$. The Einstein operator (2.10) has a block diagonal form with respect to this decomposition [Bes08, p. 130] (see also [Krö17, Section 2] for the refined version stated here).

Lemma 3.13. Let $h \in T T(\widehat{M}), \varphi \in C^{\infty}((0, \infty))$ and $\bar{h} \in C^{\infty}\left(S^{2} \bar{M}\right)$ be defined by $\bar{h}=\varphi \cdot r^{2} h$. This tensor satisfies
$$\overline{\operatorname{tr}} \bar{h}=0, \quad \overline{\delta h}=0, \quad \bar{h}\left(\partial_{r}, .\right)=0$$
and
$$\bar{\Delta}_{L} \bar{h}=r^{2}\left(-\partial_{r r}^{2} \varphi \cdot h-(n-1) \cdot r^{-1} \partial_{r} \varphi \cdot h+\varphi \cdot r^{-2} \widehat{\Delta}_{E} h\right) .$$

Proof. The condition $\bar{h}\left(\partial_{r},.\right)=0$ holds as $\bar{h}_{r r}=\bar{h}_{r j}=0$. This immediately implies $\overline{\operatorname{tr}} \bar{h}=0$ as $\widehat{\operatorname{tr}}_{\widehat{g}} h=0$. By using (3.2),
$$\begin{aligned}
& \bar{\nabla}_{i} \bar{h}_{j k}=\varphi r^{2} \widehat{\nabla}_{i} h_{j k}, \quad \bar{\nabla}_{r} h_{i j}=\partial_{r} \varphi \cdot r^{2} h_{i j}, \quad \bar{\nabla}_{i} \bar{h}_{j r}=\bar{\nabla}_{i} \bar{h}_{r j}=-\varphi \cdot r \cdot h_{i j}, \\
& \bar{\nabla}_{i} \bar{h}_{r r}=\bar{\nabla}_{r} \bar{h}_{j r}=\bar{\nabla}_{r} \bar{h}_{r k}=0,
\end{aligned}$$
and by taking the trace with respect to $\bar{g}$ and using $\widehat{\operatorname{tr}} h=0$, we obtain $\overline{\delta h}=0$. Taking the covariant derivative once again, we obtain
$$\begin{aligned}
\bar{\nabla}_{i j}^{2} \bar{h}_{k l} & =\varphi r^{2} \cdot \widehat{\nabla}_{i j}^{2} h_{k l}-r \widehat{g}_{i j} \partial_{r} \varphi \cdot r^{2} h_{k l}+r^{2}\left(\widehat{g}_{i k} h_{j l}+\widehat{g}_{i l} h_{j k}\right), \\
\bar{\nabla}_{r r}^{2} \bar{h}_{k l} & =\partial_{r r}^{2} \varphi \cdot r^{2} h_{k l}, \\
\bar{\nabla}_{i j}^{2} \bar{h}_{r r} & =2 \varphi \cdot h_{i j}, \\
\bar{\nabla}_{r r}^{2} \bar{h}_{r r} & =\bar{\nabla}_{r r}^{2} \bar{h}_{k r}=\bar{\nabla}_{r r}^{2} \bar{h}_{r l}=0, \\
\bar{\nabla}_{i j}^{2} \bar{h}_{k r} & =\bar{\nabla}_{i j}^{2} \bar{h}_{r k}=-2 \varphi r\left(\widehat{\nabla}_{i} h_{j k}+\widehat{\nabla}_{j} h_{i k}\right) .
\end{aligned}$$
By taking the trace and using that $h \in T T(\widehat{M})$, we obtain
$$\bar{\Delta}_{2} \bar{h}=r^{2}\left(-\partial_{r r}^{2} \varphi \cdot h-(n-1) \cdot r^{-1} \partial_{r} \varphi \cdot h+\varphi \cdot r^{-2} \widehat{\Delta}_{2} h\right) .$$
It remains to consider the curvature term. However, the only nonvanishing term of the curvature of $\bar{g}$ is
$$\bar{R}_{i j k l}=r^{2}\left(\widehat{R}_{i j k l}+\widehat{g}_{i k} \widehat{g}_{j l}-\widehat{g}_{i l} \widehat{g}_{j k}\right),$$
therefore
$$\frac{\circ}{R}(\bar{h})_{i j}=\varphi \stackrel{\circ}{\widehat{R}}(h)_{i j},$$
which by adding up finishes the proof of the lemma. \(\square\)

Lemma 3.14. Let $\varphi, \psi \in C^{\infty}((0, \infty)), \omega \in C^{\infty}\left(T^{*} \widehat{M}\right)$ and $v \in C^{\infty}(\widehat{M})$. Then, the form
$$\bar{\omega}=\varphi r \omega+\psi v d r \in C^{\infty}\left(T^{*} \bar{M}\right)$$
satisfies
$$\bar{\delta}^{*} \bar{\omega}=r^{-1} \varphi\left(r^{2} \widehat{\delta}^{*} \omega\right)+r^{-1} \psi v\left(r^{2} \widehat{g}\right)+\partial_{r} \psi \cdot v d r \otimes d r+\frac{1}{2}\left[\left(\partial_{r} \varphi-r^{-1} \varphi\right)(r \omega)+r^{-1} \psi(r d v)\right] \odot d r .$$

Proof. Straightforward calculations show that
$$\begin{array}{ll}
\bar{\nabla}_{i} \bar{\omega}_{j}=r \varphi \widehat{\nabla}_{i} \omega_{j}+r \widehat{g}_{i j} \psi v, & \bar{\nabla}_{r} \bar{\omega}_{r}=\partial_{r} \psi \cdot v, \\
\bar{\nabla}_{r} \bar{\omega}_{j}=r \partial_{r} \varphi \cdot \omega_{j}, & \bar{\nabla}_{i} \bar{\omega}_{r}=\psi \cdot \partial_{i} v-\varphi \omega_{i},
\end{array}$$
and the result is immediate. \(\square\)

Theorem 3.15. The spectrum of the tangential operator $\square_{L}$ of the Lichnerowicz Laplacian is given by
$$\operatorname{spec}(\square L)=\left\{\kappa_{i} \mid i \in \mathbb{N}\right\} \cup\left\{\mu_{i, \pm}^{(1)} \mid i \in \mathbb{N}\right\} \cup\left\{\lambda_{i} \mid i \in \mathbb{N}\right\} \cup\left\{\lambda_{i, \pm}^{(2)} \mid i \in \mathbb{N}\right\} \cup\{0,2 n\},$$
where
$$\mu_{i, \pm}^{(1)}:=\eta\left(\xi_{ \pm}\left(\mu_{i}+1\right)-1\right), \quad \lambda_{i, \pm}^{(2)}:=\eta\left(\xi_{ \pm}\left(\lambda_{i}\right)-2\right) .$$
The corresponding eigenspaces are
$$\begin{aligned}
E\left(\square_{L}, \kappa_{i}\right) & =\left\{h \mid h \in E\left(\widehat{\Delta}_{E}, \kappa_{i}\right)\right\}, \\
E\left(\square_{L}, \mu_{i, \pm}^{(1)}\right) & =\left\{\left.\widehat{\delta}^{*} \omega+\frac{1}{2}\left(\xi_{ \pm}\left(\mu_{i}+1\right)-1\right) \omega \odot d r \right\rvert\, \omega \in E\left(\widehat{\Delta}_{1}, \mu_{i}\right)\right\}, \\
E\left(\square_{L}, \mu_{0,-}^{(1)}=2 n\right) & =\left\{\omega \odot d r \mid \omega \in E\left(\widehat{\Delta}_{1}, \mu_{i}\right)\right\}, \\
E\left(\square_{L}, \lambda_{i, \pm}^{(2)}\right) & =\left\{\left.\stackrel{\circ}{\nabla}^{2} v-\left(\frac{\lambda_{i}}{n-1}-\xi_{ \pm}\left(\lambda_{i}\right)\right) v \stackrel{\circ}{\hat{g}}+\left(\xi_{ \pm}\left(\lambda_{i}\right)-1\right) \widehat{\nabla} v \odot d r \right\rvert\, v \in E\left(\widehat{\Delta}, \lambda_{i}\right)\right\}, \\
E\left(\square_{L}, \lambda_{i}\right) & =\left\{\left.\stackrel{\circ}{\nabla}^{2} v+\frac{\lambda_{i}(n-2)}{n(n-1)} v \stackrel{\circ}{\widehat{g}}-\frac{1}{2}(n-2) \widehat{\nabla} v \odot d r+w \cdot \bar{g} \right\rvert\, v, w \in E\left(\widehat{\Delta}, \lambda_{i}\right)\right\}, \\
E\left(\square_{L}, \lambda_{0}=0\right) & =\{\alpha \bar{g} \mid \alpha \in \mathbb{R}\}, \\
E\left(\square_{L}, \lambda_{0,-}^{(2)}=2 n\right) & =\{\alpha \widehat{\widehat{g}} \mid \alpha \in \mathbb{R}\} .
\end{aligned}$$
Here, $\stackrel{\circ}{\nabla}^{2}$ denotes the trace-free part of the Hessian (2.6) and $\stackrel{\circ}{\widehat{g}}=\widehat{g}-(n-1) d r \otimes d r$ denotes the trace-free part of $\widehat{g}$ with respect to $\bar{g}$.

Remark 3.16. If ( $\widehat{M}, \widehat{g}$ ) admits Killing fields, then we start to count the $\mu_{i}$ from zero and $\mu_{0}=(n-2)$, c.f. the discussion at the beginning of Subsection 3.3. In this case, $\xi_{+}\left(\mu_{0}+1\right)=1$ and the eigenvalue $\mu_{0,+}$ drops as the corresponding eigentensor vanishes. On the other hand $\mu_{0,-}^{(1)}$ still exists and equals $\mu_{0,-}^{(1)}=\lambda_{0,-}^{(2)}=2 n$. Thus by this counting convention, we do not need to distinguish between the cases with or without Killing fields in Theorem 1.1 and always count $\mu_{i}$ for $i \in \mathbb{N}$ there.

Similarly by the Lichnerowicz-Obata eigenvalue inequality [Oba62], we have $\lambda_{i} \geq n-1$ for all $i \in \mathbb{N}$ and equality holds only for the round sphere. In this case, we have $\stackrel{\circ}{\nabla}^{2} v=0$ for the corresponding eigenfunctions. In this case $\xi_{+}\left(\lambda_{1}\right)=1$ and the eigenvalue $\lambda_{1,+}^{(2)}$ drops and the eigenvalue $\lambda_{1,-}^{(2)}=3(n+1)$ is still present.
Remark 3.17. The indicial values of $\bar{\Delta}$ and $\bar{\Delta}_{L}$ coming from an eigenfunction $v \in E\left(\widehat{\Delta}, \lambda_{i}\right)$ are related by
$$\xi_{+}\left(\lambda_{i}\right)=\xi_{+}\left(\lambda_{i,+}^{(2)}\right)+2=\xi_{+}\left(\lambda_{i,-}^{(2)}\right)-2, \quad \xi_{-}\left(\lambda_{i}\right)=\xi_{-}\left(\lambda_{i,-}^{(2)}\right)+2=\xi_{-}\left(\lambda_{i,+}^{(2)}\right)-2$$
and indicial values of $\bar{\Delta}_{1}$ and $\bar{\Delta}_{L}$ coming from an eigenform $\omega \in E\left(\left.\widehat{\Delta}_{1}\right|_{D(\widehat{M})}, \mu_{i}\right)$ are related by
$$\xi_{+}\left(\mu_{i}\right)=\xi_{+}\left(\mu_{i,+}^{(1)}\right)+1=\xi_{+}\left(\mu_{i,-}^{(1)}\right)-1, \quad \xi_{-}\left(\mu_{i}\right)=\xi_{-}\left(\mu_{i,-}^{(1)}\right)+1=\xi_{-}\left(\mu_{i,+}^{(1)}\right)-1 .$$
Proof of Theorem 3.15. Let $h \in T T(\widehat{M})$ be such that $\widehat{\Delta}_{E} h=\kappa h$. Then due to Lemma 3.13, we have
$$r^{\xi_{ \pm}(\kappa)}\left(r^{2} h\right) \in \operatorname{ker}\left(\bar{\Delta}_{L}\right) .$$
Comparing (3.16) and the conical structure of $\bar{\Delta}_{L}$, we however immediately get
$$\square_{L} h=\widehat{\Delta}_{E} h=\kappa h .$$

Next let $\omega \in D(\widehat{M})$ be such that $\widehat{\Delta}_{1} \omega=\kappa \omega$. From Lemma 3.10, we know that
$$\bar{\omega}=r^{\xi_{ \pm}(\mu+1)}(r \omega) \in \operatorname{ker}\left(\bar{\Delta}_{1}\right) .$$
From Lemma 3.14 and the commutation rules (2.11),
$$\bar{\delta}^{*} \bar{\omega}=r^{\xi_{ \pm}(\mu+1)-1}\left[\left(r^{2} \widehat{\delta}^{*} \omega\right)+\frac{1}{2}\left(\xi_{ \pm}(\mu+1)-1\right)(r \omega) \odot d r\right] \in \operatorname{ker}\left(\bar{\Delta}_{L}\right)$$
Because the Einstein operator is conical, we get that the sections
$$h_{ \pm}:=\widehat{\delta}^{*} \omega+\frac{1}{2}\left(\xi_{ \pm}(\mu+1)-1\right) \omega \odot d r \in C^{\infty}\left(\left.S^{2} \bar{M}\right|_{\{1\} \times \widehat{M}}\right)$$
satisfy
$$\square_{L}\left(h_{ \pm}\right)=\eta\left(\xi_{ \pm}(\mu+1)-1\right) h_{ \pm}=\mu_{ \pm}^{(1)} h_{ \pm} .$$
To conclude the discussions on eigenvalues and eigensections generated by elements in $D(\widehat{M})$, we recall that $\mu \geq n-2$ and $\widehat{\Delta}_{1} \omega=(n-2) \omega$ if and only if $\widehat{\delta}^{*} \omega=0$. In this case, $\xi_{+}(\mu+1)-1=\xi_{+}(n-1)-1=0$, therefore $h_{+}=0$ and $\xi_{-}(\mu+1)-1=\xi_{-}(n-1)-1=-n$. This implies $h_{-} \in \mathbb{R} \cdot \omega \odot d r$ and $h_{-} \neq 0$ if $\omega \neq 0$.
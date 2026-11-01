---
retention_scope: session
part: 1
total_parts: 4
---

[Part 1/4 of: [1404.3118] Yamabe type equations with a sign-changing nonlinearity, and the prescribed curvature problem]

---
source_file: 1404_3118.pdf
converter: mathpix
format: mmd
---

\title{
YAMABE TYPE EQUATIONS WITH A SIGN-CHANGING NONLINEARITY, AND THE PRESCRIBED CURVATURE PROBLEM
}

\author{
BRUNO BIANCHINI, LUCIANO MARI, AND MARCO RIGOLI
}

\begin{abstract}
In this paper, we investigate the prescribed scalar curvature problem on a non-compact Riemannian manifold $(M,\langle\rangle$,$) , namely the existence of a con-$ formal deformation of the metric $\langle$,$\rangle realizing a given function \widetilde{s}(x)$ as its scalar curvature. In particular, the work focuses on the case when $\widetilde{s}(x)$ changes sign. Our main achievement are two new existence results requiring minimal assumptions on the underlying manifold, and ensuring a control on the stretching factor of the conformal deformation in such a way that the conformally deformed metric be bi-Lipschitz equivalent to the original one. The topological-geometrical requirements we need are all encoded in the spectral properties of the standard and conformal Laplacians of $M$. Our techniques can be extended to investigate the existence of entire positive solutions of quasilinear equations of the type
$$\Delta_{p} u+a(x) u^{p-1}-b(x) u^{\sigma}=0$$
where $\Delta_{p}$ is the $p$-Laplacian, $\sigma>p-1>0, a, b \in L_{\text {loc }}^{\infty}(M)$ and $b$ changes sign, and in the process of collecting the material for the proof of our theorems, we have the opportunity to give some new insight on the subcriticality theory for the Schrödinger type operator
$$Q_{V}^{\prime}: \varphi \longmapsto-\Delta_{p} \varphi-a(x)|\varphi|^{p-2} \varphi .$$
In particular, we prove sharp Hardy-type inequalities in some geometrically relevant cases, notably for minimal submanifolds of the hyperbolic space.
\end{abstract}

\section*{Contents}
\begin{itemize}
\item[1.] Introduction, I: existence for the generalized Yamabe problem
\item[2.] Introduction, II: our main results in their general setting
\item[3.] Preliminaries
\item[4.] Criticality theory for $Q_{V}$, capacity and Hardy weights
\item[5.] Hardy weights and comparison geometry
\item[5.1.] Hardy weights on manifolds with a pole
\item[5.2.] Hardy weights on minimally immersed submanifolds
\item[5.3.] Specializing our main theorems: an example
\item[6.] Proofs of Theorems 2.1 and 2.2
\item[7.] Proofs of our geometric corollaries, and concluding comments
\end{itemize}

Appendix: the obstacle problem and the pasting lemma

References

\footnotetext{
Date: August 29, 2021.
2010 Mathematics Subject Classification. primary 58J05, 35B40; secondary 53C21, 34C11, 35B09.
Key words and phrases. Yamabe equation, Schrödinger operator, subcriticality, p-Laplacian, spectrum, prescribed curvature.
}

\section*{1. Introduction, I: existence for the generalized Yamabe problem}

Generalizations of the classical Yamabe problem on a Riemannian manifold have been the focus of an active area of research over the past 30 years. Among these, the prescribed scalar curvature problem over non-compact manifolds appears to be challenging: briefly, given a non-compact Riemannian manifold $\left(M^{m},\langle\rangle,\right)$ with scalar curvature $s(x)$ and a smooth function $\widetilde{s} \in C^{\infty}(M)$, the problem asks under which conditions there exists a conformal deformation of $\langle$,$\rangle ,$
$$\widetilde{\langle,\rangle}=\varphi^{2}\langle,\rangle, \quad 0<\varphi \in C^{\infty}(M),$$
realizing $\widetilde{s}(x)$ as its scalar curvature. When the dimension $m$ of $M$ is at least 3, writing $\varphi=u^{\frac{2}{m-2}}$, the problem becomes equivalent to determining a positive solution $u \in C^{\infty}(M)$ of the Yamabe equation
$$\Delta u-\frac{s(x)}{c_{m}} u+\frac{\widetilde{s}(x)}{c_{m}} u^{\frac{m+2}{m-2}}=0, \quad c_{m}=\frac{4(m-1)}{m-2} .$$
Here, $\Delta$ is the Laplace-Beltrami operator of the background metric $\langle$,$\rangle . For m=2$, setting $\varphi=e^{u}$ one substitutes (1.2) with
$$2 \Delta u-s(x)+\widetilde{s}(x) e^{2 u}=0$$
where now $u \in C^{\infty}(M)$ may change sign (see [43]). Hereafter, we will confine ourselves to dimension $m \geq 3$, and $M$ will always be assumed to be connected. Agreeing with the literature, we will call the linear operator in (1.2):
$$L_{\langle,\rangle} \doteq-\Delta-\frac{s(x)}{c_{m}}=-\Delta+\frac{m-2}{4(m-1)} s(x)$$
the conformal Laplacian of $(M,\langle\rangle$,$) .$
The original Yamabe problem is a special case of the prescribed scalar curvature problem, namely that when $\widetilde{s}(x)$ is a constant, and for this reason, in the literature, the prescribed scalar curvature problem is often called the generalized Yamabe problem. Besides establishing existence of a positive solution $u$ of (1.2), it is also useful to investigate its qualitative behaviour since this reflects into properties of $\widetilde{\langle,\rangle}$. For instance, $u \in L^{\frac{2 m}{m-2}}(M)$ is equivalent to the fact that $\widetilde{\langle,\rangle}$ has finite volume. Also, if $u$ is bounded between two positive constants, the identity map
$$i: \quad(M,\langle,\rangle) \longrightarrow(M, \widetilde{\langle,\rangle})$$
is globally bi-Lipschitz, and thus $\widetilde{\langle,\rangle}$ inherits some fundamental properties of $\langle$,$\rangle . For$ instance, geodesic completeness, parabolicity, Gromov-hyperbolicity, etc. (see [36, 35]). Agreeing with the literature, when $C^{-1}\langle,\rangle \leq \widetilde{\langle,\rangle} \leq C\langle$,$\rangle for some constant C>0$ we will say that $\widetilde{\langle,\rangle}$ and $\langle$,$\rangle are uniformly equivalent.$

Given the generality of the geometrical setting, it is reasonable to expect that existence or non-existence of the desired conformal deformation heavily depends on the topological and metric properties of $M$ and their relations with $\widetilde{s}(x)$. As we shall explain in awhile, a particularly intriguing (and difficult) case is when $\widetilde{s}(x)$ is allowed to change sign. In this situation, with the exception of a few special cases, a satisfactory answer to the prescribed curvature problem is still missing. To properly put our results into perspective, first we describe some of the main technical problems that arise when looking for solutions of (1.2) for sign-changing $\widetilde{s}(x)$. Then, we briefly comment on some classical and more recent approaches. In particular, we pause to describe in detail four
results that allow us to grasp the situation in the relevant examples of Euclidean and hyperbolic spaces and to underline the key features of our new achievements. We stress that, when $\widetilde{s}(x) \leq 0$, there is a vast literature and the interaction between topology and geometry is better understood. Among the various references on the existence problem, we refer the reader to [8, 72, 71, 16, 48].

If $\widetilde{s}(x)$ is positive somewhere, basic tools to produce solutions are in general missing. More precisely, uniform $L^{\infty}$-estimates fail to hold on regions where $\widetilde{s}(x)$ is non-negative, and comparison theorems are not valid where $\widetilde{s}(x)$ is positive. This suggests why, in the literature, equation (1.2) in a non-compact ambient space has mainly been studied via variational and concentration-compactness techniques ([37, 80]) or radialization techniques ([57, 56, 42, 8]). We also quote the interesting method developed in [72, 71, [9].

To the best of our knowledge, up to now there have been few attempts to adapt the variational approach to (non-compact, of course) spaces other than $\mathbb{R}^{m}$, [37, 80]. In this respect, a particularly interesting result is the next one due to Q.S. Zhang [80].

Theorem 1.1 ([80], Thm. 1.1). Let $\left(M^{m},\langle\rangle,\right)$ be a complete manifold with dimension $m \geq 3$ and scalar curvature $s(x) \geq 0$. Suppose that $\operatorname{vol}\left(B_{r}(x)\right) \leq C r^{m}$ for some uniform $C$ independent of $x$, and that $M$ has positive Yamabe invariant $Y(M)$ :
$$Y(M)=\inf \left\{\int_{M}\left[|\nabla \phi|^{2}+\frac{s(x)}{c_{m}} \phi^{2}\right]: \phi \in \operatorname{Lip}_{c}(M), \int_{M} \phi^{\frac{2 m}{m-2}}=1\right\},$$
$c_{m}$ as in (1.2). Assume further that
\begin{itemize}
\item[-] $\widetilde{s}(x) \geq 0, \not \equiv 0$ and $\widetilde{s}(x) \rightarrow 0$ as $r(x) \rightarrow+\infty$,
\item[-] $\widetilde{s}(x)$ is sufficiently flat around at least one of its maximum points.
\end{itemize}

Then, there exists a solution $u \in L^{\frac{2 m}{m-2}}(M)$ of (1.2) such that
$$u \leq C(1+r(x))^{-\frac{m-2}{2}},$$
for some $C>0$. In particular, $\widetilde{\langle,\rangle}=u^{\frac{4}{m-2}}\langle$,$\rangle has finite volume and is geodesically$ incomplete.

Remark 1.1. The flatness condition above is the one usually required for the compact Yamabe problem, see [28, 29].

The above theorem is not, indeed, the most general statement of Zhang's result, but however the version here is a good compromise between generality and simplicity, and it is enough for the sake of comparison with our main theorems. On the positive side, topological conditions on $M$ are not so demanding. However, we underline that the polynomial volume growth assumption is essential for Zhang's method to work, hence this excludes the case of negatively curved manifolds like the hyperbolic space $\mathbb{H}_{\kappa}^{m}$ of sectional curvature $-\kappa^{2}$. On the contrary, as the recent [13] highlights, the radialization methods developed by W.M. Ni, M. Naito and N. Kawano in [57, 56, 42] on $\mathbb{R}^{m}$, and by P. Aviles and R. McOwen in [8] for $\mathbb{H}^{m}$ are very flexible with respect to curvature control on $M$, but on the other hand they require $M$ to possess a pole (that is, a point $o$ for which the exponential map $\exp _{o}$ is a diffeomorphism), a quite restrictive topological assumption. We quote the two results, starting from Ni-Naito-Kawano's theorem.

Theorem 1.2 ([57, 56, 42]). Let $\widetilde{s}(x) \in C^{\infty}\left(\mathbb{R}^{m}\right), m \geq 3$, and suppose that there exists $B \in C^{0}(\mathbb{R})$ such that
$$|\widetilde{s}(x)| \leq B(r(x)) \quad \text { and } \quad r B(r) \in L^{1}(+\infty) .$$
Then, there exists a small $\gamma_{0}>0$ such that, for each $\gamma \in\left(0, \gamma_{0}\right)$, there exists a conformal deformation $\widetilde{\langle,\rangle}$ of the flat metric $\langle$,$\rangle such that$
$$\widetilde{\langle,\rangle}_{x} \rightarrow \gamma\langle,\rangle_{x} \quad \text { as } r(x) \rightarrow+\infty .$$
Theorem 1.3 ([8], Thm 4). Let $\left(M^{m},\langle\rangle,\right)$ be a complete manifold with a pole and dimension $m \geq 3$, and suppose that there exist constants $\bar{\kappa} \geq \kappa>0$ such that sectional curvature $K$ of $M$ be pinched as follows:
$$-\bar{\kappa}^{2} \leq K \leq-\kappa^{2}<0, \quad \text { with } \quad \bar{\kappa}^{2}<\frac{(m-1)^{2}}{m(m-2)} \kappa^{2} .$$
Suppose also that $\widetilde{s}(x) \in C^{\infty}(M)$ satisfies
$$-C_{1} \leq \widetilde{s}(x) \leq-C_{2}<0 \quad \text { outside of a compact set, }$$
for some constants $C_{1}, C_{2}>0$. Then, there exists $\delta>0$ sufficiently small such that, if
$$\widetilde{s}(x) \leq \delta \quad \text { on } M,$$
there exists a conformal deformation $\widetilde{\langle,\rangle}$ realizing $\widetilde{s}(x)$ and satisfying
$$C^{-1}\langle,\rangle \leq \widetilde{\langle,\rangle} \leq C\langle,\rangle \quad \text { on } M,$$
for some positive constant $C$.
Remark 1.2. Theorem 1.3 has later been improved in [72] with a different technique: however, the main Theorem 0.1 in [72] still requires (1.11) and a couple of conditions on the curvatures of $M$ that, though more general than (1.9), nevertheless are more demanding than (1.23), (1.24) appearing in our Corollary 1.2 below.

Remark 1.3. For the special case of the Hyperbolic space, in [71] (see Theorem 1.1 therein) the authors were able to guarantee the existence of a solution for the Yamabe equation giving rise to a complete metric even when (1.10) is replaced by the weaker
$$-C r(x)^{2} \leq \widetilde{s}(x)<0 \quad \text { outside of a compact set. }$$
The counterpart of this improvement is that a control of the type (1.12) is no longer available. We remark that, in Theorem 1.1 of [71], condition (1.11) still appears.

Inspired by Ni-Naito-Kawano's approach, in [13] we have obtained sharp existence theorems for (1.2) (and, more generally, for (2.1) below) on manifolds possessing a pole $o$ via mild assumptions on the radial sectional curvature $K_{\text {rad }}$ (the sectional curvature restricted to 2-planes containing $\nabla r$, with $r(\cdot)=\operatorname{dist}(\cdot, o))$. In the particular case of manifolds close to the hyperbolic space, our outcome has been the following result. Observe that condition 1.15 below guarantees the existence of solutions even when $\widetilde{s}(x)$ is strongly oscillating. On the other hand, (1.16) implies that the conformally deformed metric is incomplete and has finite volume.

Theorem 1.4 ([13], Thm 2). Let $(M,\langle\rangle$,$) be a complete manifold of dimension m \geq 3$, with a pole $o$ and sectional curvature $K$ satisfying
$$-\kappa^{2}-\mathcal{K}(r(x)) \leq K(x) \leq-\kappa^{2},$$
for some constant $\kappa>0$ and some non-negative $\mathcal{K} \in C^{0}\left(\mathbb{R}_{0}^{+}\right) \cap L^{1}\left(\mathbb{R}^{+}\right)$. Suppose that the scalar curvature $s(x)$ of $M$ is such that
$$s(x) \geq-\frac{(m-1)^{3} \kappa^{2}}{m-2} \quad \text { on } M .$$
Then, for each $\widetilde{s}(x) \in C^{\infty}(M)$ satisfying, for some $B \in C^{0}\left(\mathbb{R}_{0}^{+}\right)$,
$$|\widetilde{s}(x)| \leq B(r(x)), \quad e^{-2 \kappa r} B(r) \in L^{1}(+\infty),$$
the metric $\langle$,$\rangle can be conformally deformed to a smooth metric \widetilde{\langle,\rangle}$ of scalar curvature $\widetilde{s}(x)$, satisfying
$$\Gamma_{1} e^{-2 \kappa r(x)}\langle,\rangle_{x} \leq \widetilde{\langle,\rangle_{x}} \leq \Gamma_{2} e^{-2 \kappa r(x)}\langle,\rangle_{x} \quad \forall x \in M,$$
for some $0<\Gamma_{1} \leq \Gamma_{2}$. In particular, $\widetilde{\langle,\rangle}$ is incomplete and has finite volume. Furthermore, $\Gamma_{2}$ and consequently $\Gamma_{1}$ can be chosen to be as small as we wish.

Remark 1.4. The growth conditions (1.7) and (1.15) are sharp: it is proved in [21] (for $\mathbb{R}^{m}$ ) and [15] (for $\mathbb{H}_{\kappa}^{m}$ ) that no conformal deformation exists whenever $\widetilde{s}(x) \leq 0$ on $\mathbb{R}^{m}$ (respectively, on $\mathbb{H}_{\kappa}^{m}$ ) and
$$\widetilde{s}(x) \leq-\frac{C}{r(x)^{2} \log r(x)} \quad\left(\text { respectively, } \quad \widetilde{s}(x) \leq-\frac{C e^{2 \kappa r(x)}}{r(x) \log r(x)}\right)$$
for some $C>0$ and large $r(x)$.
The above four results are, to the best of our knowledge, an up-to-date account of what is known on the prescribed scalar curvature problem, in dimension $m \geq 3$ and with sign-changing $\widetilde{s}(x)$, on non-compact manifolds close to $\mathbb{R}^{m}$ and $\mathbb{H}_{\kappa}^{m}$. Figures 1 and 2 below summarize Theorems 1.1 to (1.4) when assumptions overlap.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/8da75ebf-d848-4929-86db-c8e7fa65d354-05.jpg?height=590&width=899&top_left_y=1537&top_left_x=638}
\captionsetup{labelformat=empty}
\caption{Figure 1. Euclidean space, (1.7) and Zhang's assumptions on $\widetilde{s}(x)$ in force.}
\end{figure}

A first step in the direction of removing the pole requirement has been taken in [14] by adapting some ideas of [13] via the use of Green functions. Unfortunately, even though the requirements on $s(x)$ and $\widetilde{s}(x)$ in Theorem 5 of [14] are sharp, they express in a form that is generally difficult to check. In summary, the task of obtaining results

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/8da75ebf-d848-4929-86db-c8e7fa65d354-06.jpg?height=598&width=900&top_left_y=417&top_left_x=639}
\captionsetup{labelformat=empty}
\caption{Figure 2. Manifolds close to $\mathbb{H}_{\kappa}^{m},-C_{1} \leq \widetilde{s}(x) \leq-C_{2}<0$ for large $x$.}
\end{figure}
of the type above but with a substantial weakening of the geometric assumptions calls for new ideas, and this is the objective of the present work. More precisely, we have a twofold concern in this paper. First, we aim to produce an existence theorem for sign-changing $\widetilde{s}(x)$ where topological and geometrical conditions are confined to a minimum. Second, we also want to keep control on the conformally deformed metric, in particular in such a way that $\langle$,$\rangle and \widetilde{\langle,\rangle}$ are uniformly equivalent. Our contributions are Theorems 1.5, 1.6 and 2.3 below, a special case of Theorems 2.1, 2.2 which we are going to describe in awhile.

Notation. Hereafter, given $b \in L_{\text {loc }}^{\infty}(M)$, we respectively denote with $b_{+}$and $b_{-}$its positive and negative parts, so that $b=b_{+}-b_{-}$. For $a \in L_{\text {loc }}^{\infty}(M)$, we will write
$$a(x)=O(b(x)) \quad(\text { respectively }, \quad a(x) \asymp b(x)) \quad \text { as } x \text { diverges }$$
to indicate that there exists a constant $C>0$ and a compact set $\Omega$ such that
$$a(x) \leq C b(x) \quad\left(\text { respectively }, \quad C^{-1} b(x) \leq a(x) \leq C b(x)\right)$$
on $M \backslash \Omega$.
Our first result deals with the case of non-parabolic manifolds with non-negative scalar curvature. We recall that a manifold $M$ is said to be non-parabolic if it admits a positive, non-constant solution of $\Delta u \leq 0$. The notion of non-parabolicity will be recalled later in a more general setting (see Proposition 2.1 and the subsequent discussion), here we limit to refer the interested reader to [34] for deepening. The following theorem shall be compared to Theorems 1.1 and 1.2. In particular, to compare Theorem 1.5 below with Zhang's Theorem 1.1 we need some tools that will be defined in the next introduction, and therefore we postpone the analysis to Remark 2.3.

Theorem 1.5. Let $(M,\langle\rangle$,$) be a non-parabolic manifold of dimension m \geq 3$ and scalar curvature $s(x)$ satisfying
$$s(x) \geq 0 \text { on } M, \quad s \in L^{1}(M),$$
and let $\widetilde{s} \in C^{\infty}(M)$ with the following properties:
$$\widetilde{s}_{+} \text {has compact support, } \quad \widetilde{s} \in L^{1}(M) .$$
Then, for each constant $C>0,\langle$,$\rangle can be pointwise conformally deformed to a new$ metric $\widetilde{\langle,\rangle}$ of scalar curvature $\widetilde{s}(x)$ such that $\widetilde{\langle,\rangle} \leq C\langle$,$\rangle . Moreover, if s$ and $\widetilde{s}$ have compact support, each such $\widetilde{\langle,\rangle}$ can be chosen to be uniformly equivalent to $\langle$,$\rangle .$

Remark 1.5. Non-parabolicity is a very mild requirement, and it is necessary to guarantee existence in all the cases investigated in Theorem 1.5. In fact, if $M$ is scalar flat and taking $\widetilde{s}(x)$ to be compactly supported, non-negative and not identically zero, any eventual solution $u$ of the Yamabe equation (1.2) would be a (non-constant) positive solution of $\Delta u=-\widetilde{s}(x) / c_{m} u^{\frac{m+2}{m-2}} \leq 0$, showing that $M$ must be non-parabolic.

Theorem 1.5 applies, for instance, to the physically relevant setting of asymptotically flat spaces. According to [47], $\left(M^{m},\langle\rangle,\right)$ is called asymptotically flat if
\begin{itemize}
\item[-] its scalar curvature $s(x)$ satisfies (1.17),
\item[-] there exists a compact set $K \subset M$ such that each connected component $U_{j}$ of $M \backslash K$ has a global chart $\Psi_{j}:\left(\mathbb{R}^{m} \backslash B_{R}(0),\langle,\rangle_{\text {can }}\right) \rightarrow U_{j}$ for which the local expression $g_{i j}$ of $\langle$,$\rangle satisfies$
\end{itemize}
$$\left|g_{i j}-\delta_{i j}\right|=O\left(r^{-p}\right), \quad\left|\partial_{k} g_{i j}\right|=O\left(r^{-p-1}\right), \quad\left|\partial_{k l}^{2} g_{i j}\right|=O\left(r^{-p-2}\right)$$
as $r(x)=|x| \rightarrow+\infty$, for some $p>(m-2) / 2$ and for each $1 \leq i, j, k, l \leq m$.
Corollary 1.1. Let $(M,\langle\rangle$,$) be an asymptotically flat manifold of dimension m \geq 3$. Then, for each smooth function $\widetilde{s}(x)$ satisfying
$$\widetilde{s}_{+} \text {has compact support } \quad \text { and } \quad \widetilde{s} \in L^{1}(M),$$
and for each constant $C>0, \widetilde{s}(x)$ is realizable via a conformal deformation $\widetilde{\langle,\rangle \text { of }}\langle$, satisfying $\widetilde{\langle,\rangle} \leq C\langle$,$\rangle . Furthermore, if \widetilde{s} \equiv 0$ outside some compact set, then $\widetilde{\langle,\rangle}$ can be chosen to be uniformly equivalent to $\langle$,$\rangle .$

Now, we deal with manifolds whose original scalar curvature can be somewhere negative.

Theorem 1.6. Let $\left(M^{m},\langle\rangle,\right)$ be a non-parabolic Riemannian manifold of dimension $m \geq 3$ with scalar curvature $s(x)$. Suppose that the conformal Laplacian (1.3) admits a positive Green function on $M$.

Let $\widetilde{s}(x) \in C^{\infty}(M)$ be such that
$$\widetilde{s}_{+} \text {has compact support, } \quad \widetilde{s}(x) \asymp s(x) \text { as } x \text { diverges. }$$
Then, there exists $\delta>0$ such that if
$$\widetilde{s}(x) \leq \delta \quad \text { on } M,$$
then $\widetilde{s}$ is realizable via a uniformly equivalent, conformal deformation $\widetilde{\langle,\rangle}$ of $\langle$,$\rangle .$
Remark 1.6. Observe that (1.21) implies that the original scalar curvature $s(x)$ is non-positive outside a compact set.

Note that Theorems 1.5 and 1.6 seem to be new even in the simpler case $\widetilde{s}(x) \leq 0$ on $M$. In this respect, these are skew with the main theorem in [48] and with Theorem 2.30 of [12].

The requirement (1.3) shows the central role played by the conformal Laplacian $\left.L_{\langle },\right\rangle$ for the Yamabe equation. The relevance of $L_{\langle,\rangle}$for the original Yamabe problem is well-known and highlighted, for instance, in the comprehensive [47]. We will spend a considerable part of the paper to discuss on assumptions like (1.3). Clearly, Theorem 1.6 is tightly related to Aviles-McOwen's Theorem 1.3, a parallel which is even more evident in view of the next

Corollary 1.2. Let $(M,\langle\rangle$,$) be a complete manifold of dimension m \geq 3$ with a pole $o$ and sectional curvature $K$ satisfying
$$K \leq-\kappa^{2},$$
for some constant $H>0$. Suppose further that
$$s(x) \geq-\frac{(m-1)^{3}}{(m-2)} \kappa^{2}$$
on $M$. Let $\widetilde{s}(x) \in C^{\infty}(M)$ satisfying
$$-C_{1} \leq \widetilde{s}(x) \leq-C_{2}<0 \quad \text { outside some compact set },$$
for some constants $0<C_{2}<C_{1}$. Then, there exists $\delta>0$ such that if
$$\widetilde{s}(x) \leq \delta \quad \text { on } M,$$
then $\widetilde{s}(x)$ is realizable by a conformal deformation $\widetilde{\langle,\rangle}$ of $\langle$,$\rangle which is uniformly equiv-$ alent to $\langle$,$\rangle .$

Remark 1.7. Corollary 1.2 improves on Theorem 1.3, since requirement (1.9) in Theorem 1.3 implies (1.23), (1.24). In particular, the hyperbolic space $\mathbb{H}_{\kappa}^{m}$ of sectional curvature $-\kappa^{2}$ satisfies all the assumptions of Corollary 1.2, being $s(x)=-m(m-1) \kappa^{2}$. Moreover, as the proof in [8] shows, (1.9) is essential to ensure the existence of $\delta>0$ in (1.11); the case of equality in (1.24) seems, therefore, hardly obtainable with the approach described in [8]. It is worth to observe that the existence of a pole and the pinching assumption (1.9) on the sectional curvature are needed in [8] to apply both the Laplacian comparison theorems (from above and below) for the distance function $r(x)=\operatorname{dist}(x, o)$ in order to find suitable radial sub- and supersolutions. On the contrary, here the weaker (1.23) and (1.24) are just used to ensure that the conformal Laplacian has a positive Green function.

We pause for a moment to comment on assumption (1.22). Both Theorems 1.5 and 1.6 will be consequences of Theorem 2.3 below, and thus they will be proved via a common technique. The reason why assumption (1.22) is required in Theorem 1.6 but not in Theorem 1.5 can be summarized in the existence, in the second case, of a global, positive supersolution for the conformal Laplacian (that is, a solution $w$ of $L_{\langle,\rangle} w \geq 0$ on $M$ ) which is bounded both from below and from above by positive constants; one can take, for instance, $u \equiv 1$. Such a function is not possible to construct in the general setting of Theorem 1.6 (see Remark 6.2 below for deepening). We stress that, unfortunately, the value of $\delta$ in Corollary 1.2 is not explicit: indeed, it depends on a uniform $L^{\infty}$ bound for solutions of some suitable PDEs, which is shown to exist via an indirect method.
The need of (1.22) to obtain existence for $\widetilde{\langle,\rangle}$ is investigated in Remark 6.4. It is very interesting that the same condition (1.22) appears both in our theorem and in Aviles-McOwen's one, as well as in Theorems 0.1 in [72] and 1.1 in [71], although the techniques to prove them are different. This may suggest that, in general, (1.22) could
not be removable. However, at present we still have no counterexample showing that (1.22) is necessary. For future work, we thus feel interesting to investigate the next

Question. Can assumption (1.22) in Theorem 1.6 be removed, even without expecting the new metric to be uniformly equivalent to 〈, 〉?

\section*{2. Introduction, II: our main results in their general setting}

Although the prescribed scalar curvature problem is the main focus of our investigation, the techniques developed here allow us to study more general classes of PDEs, namely nonlinear extensions (described in (2.4)) of the equation
$$\Delta u+a(x) u-b(x) u^{\sigma}=0 \quad \text { on } M, \quad u>0 \text { on } M$$
with $\sigma>1, a, b \in C^{\infty}(M)$ and sign-changing $b$. Note that the signs of $a, b$ are reversed with respect to those of $s, \widetilde{s}$ in (1.2), and that $\sigma$ can be greater than $\frac{m+2}{m-2}$, preventing a direct use of variational techniques. However, when $\sigma \leq \frac{m+2}{m-2}$ and $b(x)<0$ on $M$, the investigation of (2.1) on Euclidean space is still the core of a very active area of research. In this respect, we quote the seminal [17] and, for sign-changing $b(x)$ (and singular $a(x)$ ), the recent [30].

As a matter of fact, even for (2.1) the spectral properties of the linear part $L=-\Delta-$ $a(x)$ play a prominent role, in particular the analysis of the fundamental tone $\lambda_{1}^{L}(M)$ of the Friedrichs extension of $\left(L, C_{c}^{\infty}(M)\right)$. We recall that $\lambda_{1}^{L}(M)$ is characterized via the Rayleigh quotient as follows:
$$\lambda_{1}^{L}(M)=\inf _{0 \not \equiv \varphi \in \operatorname{Lip}_{c}(M)} \frac{\int_{M}\left[|\nabla \varphi|^{2}-a(x) \varphi^{2}\right] \mathrm{d} x}{\|\varphi\|_{L^{2}(M)}^{2}} .$$
For instance, if $\lambda_{1}^{L}(M)<0$, the situation is somewhat rigid:
\begin{itemize}
\item[(a)] if $b(x) \leq 0$, then (2.1) has no positive solutions. This follows from a direct spectral argument ${ }^{1}$ )
\item[(b)] if $b(x) \geq 0$ and the zero set of $b$ is small in a suitable spectral sense, then there always exist a minimal and a maximal (possibly coinciding) positive solutions of (2.1); see [48, 63] and Section 2.4 in [12].
\end{itemize}
It is important to underline that, in both cases, the geometry of $M$ only reveals via the spectral properties of $L$. In other words, no a-priori assumptions of completeness of $M$, nor curvature nor topological requests are made. As suggested by $(a)$ and (b) above, it seems that the subtler case is that of investigating existence under the assumption $\lambda_{1}^{L}(M) \geq 0$. This condition is often implicitly met in the literature and it is automatically satisfied in many geometric situations. This happens, for instance, for Theorems 1.1 to 1.4

There is another aspect of the above picture which is worth mentioning. Partial differential equations similar to (2.1) are of interest even for quasilinear operators more general than the Laplacian. Just to give an example, of a certain importance in Physics, we can consider the general equation for radiative cooling
$$\kappa^{-1} \operatorname{div}\left(\kappa|\nabla u|^{p-2} \nabla u\right)-\left(\tau \kappa^{-1}\right) u^{4}=0 \quad \text { on } \mathbb{R}^{m},$$
where $\kappa>0$ is the coefficient of the heat conduction and $\tau$ is a function describing the radiation (see [70], p.9). The existence problem for this type of quasilinear PDEs when

\footnotetext{
${ }^{1}$ Indeed, assume the contrary and let $u>0$ solves (2.1); then, $u$ is a positive solution of $L u \geq 0$, and a result of [32 54, 3] implies that $\lambda_{1}^{L}(M) \geq 0$, contradicting our assumption.
}
the coefficient of the nonlinearity changes sign seems to be quite open. This suggests to extend our investigation to the existence of positive solutions to the quasilinear, Yamabe-type equation
$$\Delta_{p, f} u+a(x) u^{p-1}-b(x) F(u)=0 \quad \text { on } M,$$
where $f \in C^{\infty}(M)$,
$$\Delta_{p, f} u=e^{f} \operatorname{div}\left(e^{-f}|\nabla u|^{p-2} \nabla u\right)$$
and $F(u)$ is a nonlinearity satisfying the following assumptions:
$$\left\{\begin{array}{l}
F \in C^{0}(\mathbb{R}), \quad F(0)=0, \quad F>0 \quad \text { on } \mathbb{R}^{+}, \\
\frac{F(t)}{t^{p-1}} \text { is strictly increasing on } \mathbb{R}^{+}, \\
\lim _{t \rightarrow 0^{+}} \frac{F(t)}{t^{p-1}}=0, \quad \lim _{t \rightarrow+\infty} \frac{F(t)}{t^{p-1}}=+\infty
\end{array}\right.$$
The prototype example of $F(t)$ is $F(t)=t^{\sigma}$ for $\sigma>p-1$ and $t \geq 0$. Of course (2.1) is recovered by choosing $p=2$ and $f$ constant. We underline that, even for (2.4) in the Euclidean space and with $F(t)=t^{\sigma}$, there seems to be no result covering the cases described in Theorems 2.1 and 2.2. The family of operators in (2.5) above encompasses two relevant geometrical cases: $\Delta_{p, 0}$ the standard $p$-Laplacian $\Delta_{p}$, and $\Delta_{2, f}$ the drifted Laplacian, $\Delta_{f}$, appearing, for instance, in the analysis of Ricci solitons and quasi-Einstein manifolds. Note that the radiative cooling equation is of type (2.4) provided $1<p \leq 5$. Note also that, since the definition of $\Delta_{p, f}$ is intended in the weak sense, solutions will be, in general, only of class $C_{\text {loc }}^{1, \mu}(M)$ by [78].
Notation. Hereafter, with a slight abuse of notation, with $C_{\text {loc }}^{1, \mu}(M)$ we mean that for each relatively compact open set $\Omega \subset M$, there exists $\mu=\mu(\Omega) \in(0,1)$ such that $u \in C^{1, \mu}(\bar{\Omega})$.

Remark 2.1. We stress that, with possibly the exception of Theorem 1.1 when $F(t)=$ $t^{\sigma}$ and $\sigma \leq p^{*}-1$, the techniques used to prove Theorems 1.1 to 1.4 seem hard to extend to deal with (2.5) for nonradial $f$, even for $p=2$. For constant $f$, it seems also very difficult to adapt them to investigate (2.5) when $p \neq 2$. In particular, the transformation performed in [13] for $p=2$ to absorb the linear term $a(x) u$ can only be applied when the driving operator is linear.

To state our main result, Theorem 2.1 below, we need to introduce some terminology. Let $\mathrm{d} \mu_{f}$ be the weighted measure $e^{-f} \mathrm{~d} x$, with $\mathrm{d} x$ the Riemannian volume element on $M$. For $V \in L_{\text {loc }}^{\infty}(M)$, we consider the functional $Q_{V}$ defined on $\operatorname{Lip}_{c}(M)$ by
$$Q_{V}(\varphi)=\frac{1}{p}\left[\int_{M}|\nabla \varphi|^{p} \mathrm{~d} \mu_{f}-\int_{M} V|\varphi|^{p} \mathrm{~d} \mu_{f}\right] .$$
Its Gateaux derivative $Q_{V}^{\prime}$ is given by
$$Q_{V}^{\prime}(w)=-\Delta_{p, f} w-V|w|^{p-2} w \quad \text { for } w \in W_{\text {loc }}^{1, p}(M) .$$
When $M=\mathbb{R}^{m}$, the spectral properties of $Q_{V}$ have been investigated in [5, 4, 33] and in a series of papers by Y. Pinchover and K. Tintarev (see in particular [67, 68]). From now on, we follow the notation and terminology in [68]. In the linear case $p=2$, $f \equiv 0$, that is, for the Schrödinger operator $Q_{V}^{\prime}=-\Delta-V$, we refer the reader to [54, 3, 60, 59, 55].

To begin with, and according to [55, 67], we recall the following:

Definition 2.1. For $V \in L_{\text {loc }}^{\infty}(M)$, define $Q_{V}$ as in (2.7) and let $\Omega \subseteq M$ be an open set.
\begin{itemize}
\item[i)] $Q_{V}$ is said to be non-negative on $\Omega$ (shortly, $Q_{V} \geq 0$ ) if and only if $Q_{V}(\varphi) \geq$ 0 for each $\varphi \in \operatorname{Lip}_{c}(\Omega)$, that is, if and only if the Hardy type inequality
\end{itemize}
$$\int_{M} V(x)|\varphi|^{p} \mathrm{~d} \mu_{f} \leq \int_{M}|\nabla \varphi|^{p} \mathrm{~d} \mu_{f} \quad \forall \varphi \in \operatorname{Lip}_{c}(\Omega) .$$
holds.
\begin{itemize}
\item[ii)] $Q_{V}$ is said to be subcritical (or non-parabolic) on $\Omega$ if and only if $Q_{V} \geq 0$ there, and there exists $w \in L_{\mathrm{loc}}^{1}(\Omega), w \geq 0, w \not \equiv 0$ on $\Omega$, such that
\end{itemize}
$$\int_{M} w(x)|\varphi|^{p} \mathrm{~d} \mu_{f} \leq Q_{V}(\varphi) \quad \forall \varphi \in \operatorname{Lip}_{c}(\Omega) .$$

Sometimes, especially in dealing with the prescribed scalar curvature problem and when no possible confusion arises, we also say that $Q_{V}^{\prime}$, and not $Q_{V}$, is non-negative (or subcritical). The term "non-parabolic" is justified by the following statement for $Q_{0}$ (that is, $Q_{V}$ with $V(x) \equiv 0$ ), which is part of Proposition 4.4 below:

Proposition 2.1. Let $(M,\langle\rangle$,$) be Riemannian, f \in C^{0}(M)$ and $p>1$. Then, $Q_{0}$ is subcritical on $M$ if and only if there exists a non-constant, positive weak solution $g \in C^{0}(M) \cap W_{\text {loc }}^{1, p}(M)$ of $\Delta_{p, f} g \leq 0$.

According to the literature, the existence of such $g$ is one of the equivalent conditions that characterize $M$ as being not $p$-parabolic; there are various other characterizations of $p$-parabolicity, given in terms of Green kernels, $p$-capacity of compact sets, Ahlfors' type maximum principles, and so on. We refer to the survey [34] for deepening in the linear case $p=2$, and to (see [79, 64, 41, 40, 38]) for $p \neq 2$. The equivalence in Proposition 2.1 has been observed, in the linear setting, by [7, 19, 49], and for $p \neq 2$ it has also recently been proved in [22] with a technique different from our.

In fact, all of these characterizations of the non-parabolicity of $-\Delta_{p, f}$ can be seen as a special case of a theory developed in [55, 66] (when $p=2$ ) and in [67, 68] for operators $Q_{V}$ with potential. In Section 4, we recall the main result in [67, 68], the ground state alternative, and we give a proof of it by including a further equivalent condition, see Theorem 4.1 below; as a corollary, we prove Propositions 4.4 and 2.1.
Remark 2.2. In the prescribed scalar curvature problem, the role of $\langle$,$\rangle and \widetilde{\langle,\rangle}$ can be exchanged. Such a symmetry suggests that those geometric conditions which are invariant with respect to a conformal change of the metric turn out to be more appropriate to deal with the Yamabe equation. This is the case for the non-negativity and the subcriticality of the conformal Laplacian $L_{\langle,\rangle}$of $(M,\langle\rangle$,$) in (1.3). In fact,$ the covariance of $L$ with respect to the conformal deformation $\widetilde{\langle,\rangle}=u^{\frac{4}{m-2}}\langle$,$\rangle of the$ metric:
$$L_{\widetilde{\langle,\rangle}}(\cdot)=u^{-\frac{m+2}{m-2}} L_{\langle,\rangle}(u \cdot)$$
implies that, for each $0 \leq w \in L_{\text {loc }}^{1}(M)$ and $\varphi \in \operatorname{Lip}_{c}(M)$,
$$\int_{M}\left[\|\widetilde{\nabla} \varphi\|^{2}+\frac{\widetilde{s}}{c_{m}} \varphi^{2}\right] \mathrm{d} \widetilde{x}-\int_{M} \widetilde{w} \varphi^{2} \mathrm{~d} \widetilde{x}=\int_{M}\left[|\nabla(u \varphi)|^{2}+\frac{s}{c_{m}}(u \varphi)^{2}\right] \mathrm{d} x-\int_{M} w(u \varphi)^{2} \mathrm{~d} x,$$
where ~ superscript indicates quantities referred to $\widetilde{\langle,\rangle},\|\cdot\|$ is its induced norm, and
$$\widetilde{w}=w u^{-\frac{4}{m-2}} \in L_{\mathrm{loc}}^{1}(M), \quad \widetilde{w} \geq 0 .$$

Consequently, $L_{\langle,\rangle}$is non-negative (resp. subcritical) if and only if so is $L_{\widehat{\langle,\rangle}}$.
Remark 2.3. As a direct consequence of the ground state alternative, the positivity of the Yamabe invariant $Y(M)$ in Zhang's Theorem 1.1 implies that $L_{\langle,\rangle}$is subcritical (see Remark 4.3). On the other hand, in our Theorem 1.5 the subcriticality of $L_{\langle,\rangle}$ follows combining the non-parabolicity of $M$ and $s(x) \geq 0$. Although, in general, the positivity of $Y(M)$ might not imply the non-parabolicity of $M$, this is so if $M$ is scalar flat outside a compact set and $\operatorname{vol}(M)=+\infty$. Indeed, if $s(x) \equiv 0$ outside a compact set $K$, then $Y(M)>0$ gives the validity of an $L^{2}$-Sobolev inequality on $M \backslash K$, and coupling with $\operatorname{vol}(M)=+\infty$ the non-parabolicity of $M$ follows by a result in [20, 64]. We underline that, in the same assumptions, again by [20, 64] property $\operatorname{vol}(M)=+\infty$ is automatic when $M$ is geodesically complete. Summarizing, if the manifold in Zhang's Theorem 1.1 is scalar flat near infinity, the geometric requirements there properly contain those of our Theorem 1.5.

We are now ready to state
Theorem 2.1. Let $M^{m}$ be a Riemannian manifold, $f \in C^{\infty}(M)$ and $p \in(1,+\infty)$. Suppose that $Q_{0}$ is subcritical on $M$, and let $a \in L_{\mathrm{loc}}^{\infty}(M)$ be such that $Q_{a}$ is subcritical on $M$. Consider $b \in L_{\text {loc }}^{\infty}(M)$, and assume
\begin{itemize}
\item[i)] $b_{-}(x)$ has compact support;
\item[ii)] $a(x)=O(b(x))$ as $x$ diverges;
\item[iii)] for some $\theta>0,\left(a(x)-\theta b_{+}(x)\right)_{-} \in L^{1}\left(M, \mathrm{~d} \mu_{f}\right)$.
\end{itemize}
Fix a nonlinearity $F(t)$ satisfying (2.6). Then, there exists $\delta>0$ such that if
$$b(x) \geq-\delta \quad \text { on } M,$$
there exists a weak solution $u \in C_{\text {loc }}^{1, \mu}(M)$ of
$$\left\{\begin{array}{l}
\Delta_{p, f} u+a(x) u^{p-1}-b(x) F(u)=0 \quad \text { on } M \\
0<u \leq\|u\|_{L^{\infty}(M)<+\infty .}
\end{array}\right.$$
If we replace ii) and iii) by the stronger condition
$$\text { iv) } \quad b_{+}(x) \asymp a(x) \quad \text { as } x \text { diverges, }$$
and we keep the validity of (2.11), then $u$ can also be chosen to satisfy
$$\inf _{M} u>0 .$$

In the next theorem, we remove requirement (2.11); see also Remark 6.4 for a related discussion.

Theorem 2.2. Let $M^{m}$ be a Riemannian manifold, $f \in C^{\infty}(M)$ and $p \in(1,+\infty)$. Suppose that $Q_{0}$ is subcritical on $M$ and let $a \in L_{\text {loc }}^{\infty}(M)$ be such that $Q_{a}$ is subcritical on $M$. Consider $b \in L_{\text {loc }}^{\infty}(M)$, and assume
\begin{itemize}
\item[i)] $b_{-}(x)$ has compact support;
\item[] ii') $a(x) \leq 0$ outside a compact set;
\item[] $\left.i i i^{\prime}\right) a(x), b(x) \in L^{1}\left(M, \mathrm{~d} \mu_{f}\right)$.
\end{itemize}

Fix a nonlinearity $F(t)$ satisfying (2.6). Then, there exists a sequence $\left\{u_{k}\right\} \subset C_{\text {loc }}^{1, \mu}(M)$ of distinct weak solutions of
$$\left\{\begin{array}{l}
\Delta_{p, f} u_{k}+a(x) u_{k}^{p-1}-b(x) F\left(u_{k}\right)=0 \quad \text { on } M \\
0<u_{k} \leq\left\|u_{k}\right\|_{L^{\infty}(M)}<+\infty,
\end{array}\right.$$
such that $\left\|u_{k}\right\|_{L^{\infty}(M)} \rightarrow 0$ as $k \rightarrow+\infty$. If we replace $i i^{\prime}$ ) and $i i i^{\prime}$ ) by the stronger condition
$$\left.i v^{\prime}\right) \quad a(x), b(x) \quad \text { have compact support, }$$
then each $u_{k}$ also satisfies $\inf _{M} u_{k}>0$.
One of the main features in the proof of Theorems 2.1 and 2.2 above is a new flexible technique, which is based on a direct use of the non-negativity and subcriticality assumptions on $Q_{a}$ and $Q_{0}$. Consequently, all the geometric information needed on $M$ is encoded in the spectral behaviour of $Q_{0}$ and $Q_{a}$. For this reason, in Sections 4 and 5 we concentrate on operators $Q_{V}$ to show that the assumption on $Q_{0}, Q_{a}$ in Theorems 2.1 and 2.2 can be made explicit and easily verifiable in various relevant cases.

We now come to the strategy to prove Theorems 2.1 and 2.2. The lack of tools to produce solutions in the present generality forces us to proceed along very simple, general schemes. In particular, the argument can be roughly divided into three parts:
\begin{itemize}
\item[(1)] For a big relatively compact domain $\Omega$, we solve locally (2.4) with boundary condition 1 and $b(x)$ replaced by $b_{+}(x)$. Call $z_{\Omega}$ the solution. This is the easiest part, and is addressed in Lemma 6.1.
\item[(2)] We find uniform $L^{\infty}$ estimates from below and above for $z_{\Omega}$, independent of $\Omega$. According to our geometric assumptions, these estimates can be on the whole $M$ or on a relatively compact set $\Lambda$. The proof of this step combines Lemmas 6.2 and 6.3, and Proposition 6.1.
\item[(3)] Making use of the results in Step (2), we "place" $b_{-}$in the Dirichlet problem for (2.4) on a domain $\Omega$ via an iterative procedure, to produce a local solution of (2.4) that possesses uniform upper and lower bounds. The desired global solution is then obtained by passing to the limit along an exhaustion $\left\{\Omega_{j}\right\}$. Note that this is the point where a distinction between Theorems 2.1 and 2.2 appears.
\end{itemize}

Among the lemmas, which are of independent interest, we underline and briefly comment on the next uniform $L^{\infty}$-estimate, Lemma 6.3. This result is a cornerstone both for steps (2) and (3).

Lemma 2.1 (Uniform $L^{\infty}$-estimate). Let $M$ be a Riemannian manifold, $f \in$ $C^{\infty}(M), p \in(1,+\infty)$. Let $A, B \in L_{\mathrm{loc}}^{\infty}(M)$ with $B \geq 0$ a.e. on $M$. Assume that either
\begin{itemize}
\item[(i)] $B \equiv 0$ and $Q_{A}$ is subcritical, or
\item[(ii)] $B \not \equiv 0$ and $Q_{A}$ is non-negative.
\end{itemize}
Suppose that there exist a smooth, relatively compact open set $\Lambda \Subset M$ and a constant $c>0$ such that
$$A \leq c B \quad \text { a.e. on } M \backslash \Lambda,$$
and fix a smooth, relatively compact open set $\Lambda^{\prime}$ such that $\Lambda \Subset \Lambda^{\prime}$, and a nonlinearity $F(t)$ satisfying (2.6).

Then, there exists a constant $C_{\Lambda}>0$ such that, for each smooth, relatively compact open set $\Omega$ with $\Lambda^{\prime} \Subset \Omega$, the solution $0<z \in C^{1, \mu}(\bar{\Omega})$ of
$$\begin{cases}\Delta_{p, f} z+A(x) z^{p-1}-B(x) F(z)=0 & \text { on } \Omega, \\ z=1 & \text { on } \partial \Omega .\end{cases}$$
satisfies
$$z \leq C_{\Lambda} \quad \text { on } \Omega .$$

The proof of the above estimate is accomplished by using non-negativity (resp. subcriticality) of $Q_{A}$ alone. As far as we know, the argument in the proof seems to be new and applicable beyond the present setting. Clearly, when $z$ is $C^{2}$ and $B \in C^{0}(M)$, $B>0$ on $M$, possibly evaluating (2.16) at a interior maximum point $x_{0}$ we get
$$\frac{F(z)}{z^{p-1}}\left(x_{0}\right) \leq \sup _{M}\left(\frac{A_{+}}{B}\right),$$
whence by (2.6) $z\left(x_{0}\right)$ is uniformly bounded from above. Taking into account the boundary condition for $z$, in this case the uniform $L^{\infty}$ estimate is trivial with no assumption on $Q_{A}$. On the other hand, even a single point at which $B(x)=0$ makes this simple argument to fail, and actually Lemma 2.1 will be applied in cases when we have no control at all on the zero-set of $B$. Observe that (2.15) is just assumed to hold outside of a compact set, hence $A$ is not required to be non-positive on the set where $B=0$. This suggests that the validity of (2.18) cannot be recovered "in the limit" by using approximating positive functions $B_{\varepsilon}$ for $B$ and related solutions $z_{\varepsilon}$ for $z$. Note also that, when $B \equiv 0$, Proposition 3.4 below shows that $Q_{A}$ is necessarily non-negative, for otherwise $z$ might not exist for sufficiently large $\Omega$ 's. Therefore, in the present generality at least the non-negativity of $Q_{A}$ on the whole $M$ needs to be assumed in any case.

We pause for a moment to comment on the subcriticality of $Q_{V}$. By its very definition, a sufficient condition for $Q_{V}$ to be subcritical is the coupling of the following two:
\begin{itemize}
\item[-] $Q_{0}$ is subcritical, thus there exists $w \in L_{\text {loc }}^{1}(M), w \geq 0, w \not \equiv 0$ such that
$$\int_{M} w(x)|\varphi|^{p} \mathrm{~d} \mu_{f} \leq \int_{M}|\nabla \varphi|^{p} \mathrm{~d} \mu_{f} \quad \forall \varphi \in \operatorname{Lip}_{c}(M), \quad \text { and }$$
\item[-] $V \leq w, V \not \equiv w$.
\end{itemize}
Therefore, when $Q_{0}$ is subcritical, we can state simple, explicit conditions guaranteeing the subcriticality of $Q_{V}$ provided that we know explicit $w \in L_{\text {loc }}^{1}(M), w \geq 0, w \not \equiv 0$ satisfying (2.19). We define each of these $w$ a Hardy weight for $\Delta_{p, f}$.

In the literature, there are conditions to imply the subcriticality of $Q_{0}$ that involve curvature bounds, volume growths, doubling properties and Sobolev type inequalities. For example, when $f \equiv 0$, in [41] it is proved that a complete, non-compact manifold $M$ with non-negative Ricci curvature outside a compact set is not $p$-parabolic (i.e. $Q_{0}$ is subcritical) if and only if $p<m$. The interested reader can also consult [40, 73]. However, it seems challenging to obtain explicit Hardy weights in the setting of 41, 40, [73]. Nevertheless, Hardy weights have been found in some interesting cases, starting with the famous Hardy type inequality for Euclidean space
$$\left(\frac{m-p}{p}\right)^{p} \int_{\mathbb{R}^{m}} \frac{|\varphi|^{p}}{r^{p}} \mathrm{~d} x \leq \int_{\mathbb{R}^{m}}|\nabla \varphi|^{p} \mathrm{~d} x \quad \forall \varphi \in \operatorname{Lip}_{c}\left(\mathbb{R}^{m}\right),$$
where $r(x)=|x|$ and $m>p$. In recent years ([19, 49, 12, 10, 1, 22, 23, 24]) it has been observed how Hardy weights are related to positive Green kernels for $\Delta_{p, f}$. By exploiting the link established in Proposition 4.4 below, we will devote Section 5 to produce explicit Hardy weights in various geometrically relevant cases, see Theorems 5.1, 5.2, 5.3below: in fact, a typical construction of Hardy weights via the Green kernel is compatible with comparison results for the Laplacian of the distance function, and thus Hardy weights can be transplanted from model manifolds to general manifolds, as observed in [12], Theorem 4.15 and subsequent discussion. Moreover, the set of Hardy weights is convex in $L_{\text {loc }}^{1}(M)$, thus via simple procedures one can produce new weights, such as multipole Hardy weights or weights blowing up along a fixed submanifold of $M$. Hardy weights can also be transplanted to submanifolds, but this procedure is more delicate and requires extra care. Let $N^{n}$ be a Cartan-Hadamard manifold (i.e. a simply connected, complete manifold of non-positive sectional curvature), and let $M^{m}$ be a minimal submanifold of $N^{n}$. Suppose that the sectional curvature $\bar{K}$ of $N$ satisfies $\bar{K} \leq-\kappa^{2}$, for some constant $\kappa \geq 0$. In [19, 49], the authors proved the following Hardy type inequality:
$$\left(\frac{m-2}{2}\right)^{2} \int_{M} \frac{\varphi^{2}}{\rho^{2}} \mathrm{~d} x \leq \int_{M}|\nabla \varphi|^{2} \mathrm{~d} x \quad \forall \varphi \in \operatorname{Lip}_{c}(M),$$
$\rho(x)$ being the extrinsic distance in $N$ from a fixed origin $o \in N$. The Hardy weight in (2.21) is sharp if $\kappa=0$ (in particular, if $N$ is the Euclidean space), but not if $\kappa>0$. Here, we will prove (2.21) as a particular case of Theorem 5.3 below, which also strengthen (2.21) to a sharp inequality when $\kappa>0$, in particular for minimal submanifolds of hyperbolic spaces. We stress that our Hardy weight for $\kappa>0$ is skew with the one found in [49].

Using the Hardy inequalities mentioned before, we can rewrite the subcriticality assumption for $Q_{0}$ and $Q_{V}$ in Theorems 2.1, 2.2 in simple form for a wide class of manifolds; by a way of example, see Corollary 5.1 in Section 7. We conclude by rephrasing Theorems 2.1, 2.2 in the setting of the generalized Yamabe problem.

Theorem 2.3. Let $(M,\langle\rangle$,$) be a non-parabolic Riemannian manifold of dimension$ $m \geq 3$ and scalar curvature $s(x)$. Suppose that the conformal Laplacian $L_{\langle,\rangle}$in (1.3) is subcritical, and let $\widetilde{s} \in C^{\infty}(M)$.
\begin{itemize}
\item[(I)] Assume that
\begin{itemize}
\item[i)] $\widetilde{s}_{+}$has compact support;
\item[ii)] $s_{-}(x)=O\left(\widetilde{s}_{-}(x)\right)$ as $x$ diverges;
\item[iii)] for some $\theta>0,\left(\theta \widetilde{s}_{-}(x)-s_{-}(x)\right)_{+} \in L^{1}(M)$.
\end{itemize}
Then, there exists $\delta>0$ such that if
\end{itemize}
$$\widetilde{s}(x) \leq \delta,$$
the metric $\langle$,$\rangle can be pointwise conformally deformed to a new metric \widetilde{\langle,\rangle}$ with scalar curvature $\widetilde{s}(x)$ and satisfying
$$\widetilde{\langle,\rangle} \leq C\langle,\rangle \quad \text { on } M,$$
for some constant $C>0$. Moreover, if ii) and iii) are replaced by the stronger
$$\text { iv) } \quad s(x) \asymp \widetilde{s}(x) \quad \text { as } x \text { diverges, }$$
then (under the validity of (2.22)) there exists a pointwise conformal deformation $\widetilde{\langle,\rangle}$ of $\langle$,$\rangle as above and satisfying$
$$C_{1}\langle,\rangle \leq \widetilde{\langle,\rangle} \leq C_{2}\langle,\rangle \quad \text { on } M,$$
for some constants $0<C_{1} \leq C_{2}$. In particular, $\widetilde{\langle,\rangle}$ is non-parabolic, and it is complete whenever $\langle$,$\rangle is complete.$
(II) If ii) and iii) are replaced with
ii') $s(x) \geq 0$ outside a compact set;
$\left.i i i^{\prime}\right) s(x), \widetilde{s}(x) \in L^{1}(M)$,
then the existence of the desired conformal deformation is guaranteed without the requirement (2.22), and moreover the constant $C$ in (2.23) can be chosen as small as we wish (so that, indeed, there exist infinitely many conformal deformations realizing $\widetilde{s}$ ). If $i i^{\prime}$ ) and $i i i^{\prime}$ ) are replaced with
$$\left.i v^{\prime}\right) \quad s(x), \widetilde{s}(x) \quad \text { have compact support },$$
each of these conformally deformed metrics $\widetilde{\langle,\rangle}$ satisfies (2.24).
The paper is organized as follows. In Section 3 we collect some basic material on $Q_{V}$ and $Q_{V}^{\prime}$. Section 4 will then be devoted to the criticality theory for $Q_{V}$, its link with Hardy weights and with a $Q_{V}$-capacity theory. In Section 5, we use comparison geometry to produce sharp Hardy inequalities. Section 6 contains the proof of Lemma 2.1 and of our main Theorems 2.1, 2.2. Then, in Section 7 we derive our geometric corollaries, and we place them among the existing literature. Finally, in the Appendix we give a full proof of the pasting lemma, an important technical result for the $Q_{V}$ -capacity theory. Besides the presence of new results, a major concern of Sections 3 to 5 is to help the reader to get familiar with various aspects of the theory of Schrödinger type operators $Q_{V}^{\prime}$. For this reason, the experienced reader may possibly skip them and go directly to Section 6.

\section*{3. Preliminaries}

In this section we recall some general facts for the operators $\Delta_{p, f}, Q_{V}, Q_{V}^{\prime}$ that are extensions, to a quasilinear setting, of some classical results of spectral theory (see [55, 66, 54, 3]). The interested reader may consult [5, 4, 33, 67, 68] for further information.

Notation. Hereafter, given two open subsets $\Omega, U$, with $\Omega \Subset U$ we indicate that $\Omega$ has compact closure contained in $U$. We say that $\left\{\Omega_{j}\right\}$ is an exhaustion of $M$ if it is a sequence of relatively compact, connected open sets $\Omega_{j}$ with smooth boundary and such that $\Omega_{j} \Subset \Omega_{j+1} \Subset M, M=\bigcup_{j} \Omega_{j}$. The symbol $1_{U}$ denotes the characteristic function of a set $U$, and the symbol $\doteq$ is used to define an object.

Definition 3.1. Let $\Omega \subset M$ be an open set and, for $V \in L_{\mathrm{loc}}^{\infty}(\Omega)$, let $Q_{V}, Q_{V}^{\prime}$ be as in (2.7), (2.8). We say that $w \in W_{\text {loc }}^{1, p}(\Omega)$ is a supersolution on $\Omega$ (respectively, subsolution, solution) if $Q_{V}^{\prime}(w) \geq 0$ weakly on $\Omega$ (resp. $\leq 0,=0$ ) that is, if
$$\int_{\Omega}|\nabla w|^{p-2}\langle\nabla w, \nabla \varphi\rangle \mathrm{d} \mu_{f}-\int_{\Omega} V|w|^{p-2} w \varphi \geq 0 \quad(\text { resp. } \leq 0,=0)$$
for each non-negative $\varphi \in \operatorname{Lip}_{c}(\Omega)$.

The basic technical material that is necessary for our purposes is summarized in the following

Theorem 3.1. Let $\Omega \Subset M$ be a relatively compact, open domain with $C^{1, \alpha}$ boundary for some $0<\alpha<1$. Let $f \in C^{\infty}(M), p \in(1,+\infty), V \in L_{\mathrm{loc}}^{\infty}(M)$ and define $Q_{V}, Q_{V}^{\prime}$ as in (2.7), (2.8). Let $g \in L^{\infty}(\Omega), \xi \in C^{1, \alpha}(\partial \Omega)$ and suppose that $u \in W^{1, p}(\Omega)$ is a solution of
$$\begin{cases}Q_{V}^{\prime}(u)=g & \text { on } \Omega, \\ u=\xi & \text { on } \partial \Omega .\end{cases}$$
Then,
\begin{itemize}
\item[(1)] [Boundedness] $u \in L_{\text {loc }}^{\infty}(\Omega)$, and for any relatively compact, open domains $B \Subset$ $B^{\prime} \Subset \Omega$ there exists a positive constant $C=C\left(p, f, m, g, \xi, \Omega,\|u\|_{L^{p}\left(B^{\prime}, \mathrm{d} \mu_{f}\right)}\right)$ such that
$$\|u\|_{L^{\infty}(B)} \leq C .$$
If $\xi \in C^{2, \alpha}(\partial \Omega), C$ can be chosen globally on $\Omega$, and thus $u \in L^{\infty}(\Omega)$.
\item[(2)] $\left[C^{1, \mu}\right.$-regularity] When $u \in L^{\infty}(\Omega)$, there exists $\mu \in(0,1)$ depending on $p, f, m, g, \alpha$ and on upper bounds for $\|u\|_{L^{\infty}},\|g\|_{L^{\infty}},\|\xi\|_{C^{1, \alpha}},\|V\|_{L^{\infty}}$ on $\Omega$ such that
$$\|u\|_{C^{1, \mu}(\bar{\Omega})} \leq C$$
for some constant $C$ depending on $\alpha, p$, the geometry of $\Omega$ and upper bounds for $\|u\|_{L^{\infty}},\|g\|_{L^{\infty}},\|\xi\|_{C^{1, \alpha}},\|V\|_{L^{\infty}}$ on $\Omega$.
\item[(3)] [Harnack inequality]. For any relatively compact open sets $B \Subset B^{\prime} \Subset \Omega$ there exists $C=C\left(f, p, m, B, B^{\prime}\right)>0$ such that, for each $u \geq 0, u \in W^{1, p}(\Omega)$ solution of $Q_{V}^{\prime}(u)=0$ on $\Omega$,
$$\sup _{B} u \leq C \inf _{B^{\prime}} u .$$
In particular, either $u>0$ on $\Omega$ or $u \equiv 0$ on $\Omega$.
\item[] (3a) [Half-Harnack inequalities] For any relatively compact, open sets $B \Subset B^{\prime} \Subset \Omega$ the following holds:
(Subsolutions) for each $s>p-1$, there exists $C=C\left(f, p, m, B, B^{\prime}, V, s\right)>$ 0 such that for each $u \geq 0, u \in W^{1, p}(\Omega)$ solution of $Q_{V}^{\prime}(u) \leq 0$ on $\Omega$
$$\sup _{B} u \leq C\|u\|_{L^{s}\left(B^{\prime}\right)} ;$$
(Supersolutions) for each
$$s \in\left(0, \frac{(p-1) m}{m-p}\right) \quad \text { if } p<m, \quad s \in(0,+\infty) \quad \text { if } p \geq m$$
there exists $C=C\left(f, p, m, B, B^{\prime}, V, s\right)>0$ such that for each $u \geq 0$, $u \in W^{1, p}(\Omega)$ solution of $Q_{V}^{\prime}(u) \geq 0$ on $\Omega$
$$\|u\|_{L^{s}\left(B^{\prime}\right)} \leq C \inf _{B} u .$$
\item[(4)] [Hopf lemma] Suppose that $\xi \geq 0, g \geq 0$ and let $u \in C^{1}(\bar{\Omega})$ be a solution of (3.1) with $u \geq 0, u \not \equiv 0$. If $x \in \partial \Omega$ is such that $u(x)=\xi(x)=0$, then, indicating with $\nu$ the inward unit normal vector to $\partial \Omega$ at $x$ we have $\langle\nabla u, \nu\rangle(x)\rangle 0$.
\end{itemize}

Remark 3.1.
\begin{itemize}
\item[(1)] The local boundedness of $u$ is a particular case of Serrin's theorem, see [70], Theorem 7.1.1, and does not need the boundary condition. When $\xi \in C^{2, \alpha}(\partial \Omega)$, global boundedness can be reached via a reflection technique described at page 54 of [33], see also [77, 11].
\item[(2)] is a global version, Theorem 1 of [50], of a local regularity result in [78] and [27].
\item[(3)] is due to J. Serrin, see Theorem 7.2.1 in [70] for $p<m$, the discussion at the beginning of Section 7.4 therein for $p=m$, and Theorem 7.4.1 for $p>m$.
\item[] (3a) The half-Harnack for subsolutions can be found in Theorem 7.1.1 of [70], the one for supersolutions in the subsequent Theorems 7.1.2 (case $p<m$ ) and 7.4.1 (case $p>m$ ) of [70]. Again, see the discussion at the beginning of Section 7.4 of [70].
\item[(4)] The Hopf lemma can be found in Corollary 5.5 of [69].
\end{itemize}

An important tool for our investigation is the following Lagrangian representation in [67].

Proposition 3.1. For each $\varphi, g \in W_{\text {loc }}^{1, p}(M)$, with $\varphi / g$ a.e. finite on $M$, the Lagrangian
$$\mathcal{L}(\varphi, g)=|\nabla \varphi|^{p}+(p-1)\left(\frac{\varphi}{g}\right)^{p}|\nabla g|^{p}-p\left(\frac{\varphi}{g}\right)^{p-1}|\nabla g|^{p-2}\langle\nabla g, \nabla \varphi\rangle$$
satisfies $\mathcal{L}(\varphi, g) \geq 0$ on $M$, and $\mathcal{L}(\varphi, g) \equiv 0$ on some connected open set $U$ if and only if $\varphi$ is a constant multiple of $g$ on $U$.
Moreover, suppose that $g \in W_{\text {loc }}^{1, p}(M)$ is a positive solution of $Q_{V}^{\prime}(g)=0$ (resp. $Q_{V}^{\prime}(g) \geq 0$ ) on $M$. Then, for $\varphi \in L_{c}^{\infty}(M) \cap W^{1, p}(M), \varphi \geq 0$ it holds
$$Q_{V}(\varphi)=\int_{M} \mathcal{L}(\varphi, g) \mathrm{d} \mu_{f} \quad(\text { resp }, \geq)$$
Proof. The non-negativity of $\mathcal{L}(\varphi, g)$ follows by applying Cauchy-Schwarz and Young inequalities on the third addendum in (3.5), and analyzing the equality case, $\mathcal{L}(\varphi, g) \equiv$ 0 if and only if $\varphi=c g$ on $M$, for some constant $c \in \mathbb{R}$.
We now prove the integral (in)equality in (3.6). By Harnack inequality, $g$ is locally essentially bounded from below on $M$. This, combined with our regularity requirement on $\varphi$, guarantees that $\varphi^{p} / g^{p-1} \in W^{1, p}(M)$ and is compactly supported. Thus, we integrate on $M$ the pointwise identity
$$|\nabla \varphi|^{p}-|\nabla g|^{p-2}\left\langle\nabla g, \nabla\left(\frac{\varphi^{p}}{g^{p-1}}\right)\right\rangle=\mathcal{L}(\varphi, g),$$
and couple with the weak definition of $Q_{V}^{\prime}(g)=0$ (resp. $\geq 0$ ) applied to the test function $\varphi^{p} / g^{p-1}$ :
$$0=\int_{M}|\nabla g|^{p-2}\left\langle\nabla g, \nabla\left(\frac{\varphi^{p}}{g^{p-1}}\right)\right\rangle \mathrm{d} \mu_{f}-\int_{M} V g^{p-1}\left(\frac{\varphi^{p}}{g^{p-1}}\right) \mathrm{d} \mu_{f} \quad(\text { resp. } \leq)$$
to deduce (3.6). \(\square\)

Rewriting the expression of $\mathcal{L}(\varphi, g)$ we deduce the next useful Picone type inequality due to [4, 26, 6].

Proposition 3.2. Let $M$ be a Riemannian manifold, and let $\Omega \Subset M$ be a relatively compact, connected open set. Then, the functional
$$I(w, z)=\int_{\Omega}|\nabla w|^{p-2}\left\langle\nabla w, \nabla \frac{w^{p}-z^{p}}{w^{p-1}}\right\rangle \mathrm{d} \mu_{f}-\int_{\Omega}|\nabla z|^{p-2}\left\langle\nabla z, \nabla \frac{w^{p}-z^{p}}{z^{p-1}}\right\rangle \mathrm{d} \mu_{f}$$
is non-negative on the set
$$\mathcal{D}_{\Omega}=\left\{(w, z) \in W^{1, p}(\Omega) \times W^{1, p}(\Omega): w, z \geq 0 \text { on } \Omega, \frac{w}{z}, \frac{z}{w} \in L^{\infty}(\Omega)\right\} .$$
Furthermore, $I(w, z)=0$ if and only if $w=C z$ on $\Omega$, for some constant $C>0$.
Proof. Since $w, z \in \mathcal{D}_{\Omega}$, it is easy to see that $\frac{w^{p}}{z^{p-1}}, \frac{z^{p}}{w^{p-1}} \in W^{1, p}(\Omega)$. We can therefore expand the integrand in (3.7) and rearrange to deduce that
$$I(w, z)=\int_{\Omega}[\mathcal{L}(w, z)+\mathcal{L}(z, w)] \mathrm{d} \mu_{f}$$
with $\mathcal{L}$ as in (3.5). The first part of previous proposition then gives the desired inequality. \(\square\)

Now, we investigate property $Q_{V} \geq 0$ and its consequences. By its very definition, $Q_{V} \geq 0$ on an open set $\Omega \subset M$ is equivalent to the non-negativity of the fundamental tone
$$\lambda_{V}(\Omega)=\inf _{0 \not \equiv \varphi \in \operatorname{Lip}_{c}(\Omega)} \frac{p Q_{V}(\varphi)}{\|\varphi\|_{L^{p}\left(\Omega, \mathrm{~d} \mu_{f}\right)}^{p}} .$$
If $\Omega$ is a relatively compact domain with smooth boundary, then it is well-known that the infimum (3.8) is attained by a first eigenfunction $\phi \not \equiv 0$ solving Euler-Lagrange equation
$$\left\{\begin{array}{l}
Q_{V}^{\prime}(\phi)=\lambda_{V}(\Omega)|\phi|^{p-2} \phi \quad \text { on } \Omega, \\
\phi=0 \quad \text { on } \partial \Omega,
\end{array}\right.$$
and $\phi>0$ on $\Omega$ up to changing its sign ${ }^{2}$. Furthermore, by Harnack inequality, if $\Omega \subset \Omega^{\prime}$ are two relatively compact open sets and $\Omega^{\prime} \backslash \Omega$ has non-empty interior, then $\lambda_{V}(\Omega)>\lambda_{V}\left(\Omega^{\prime}\right)$.

The next comparison result will be used throughout the paper, and improves on Theorem 5 of [33].

Proposition 3.3. Let $M^{m}, p, f$ be as above and, for $A \in L_{\text {loc }}^{\infty}(M)$, define $Q_{A}, Q_{A}^{\prime}$ as in (2.7), (2.8) with $V(x)=A(x)$. Consider a relatively compact, open set $\Omega \subseteq M$ with smooth boundary, and let $u_{1}, u_{2} \in C^{1, \mu}(\bar{\Omega})$, for some $\mu \in(0,1)$. Furthermore, suppose that, for some non-negative $B \in L^{\infty}(\Omega)$ and a nonlinearity $F(t)$ satisfying (2.6),
$$\left\{\begin{array}{l}
\Delta_{p, f} u_{1}+A\left|u_{1}\right|^{p-2} u_{1}-B F\left(u_{1}\right) \geq 0, \\
\Delta_{p, f} u_{2}+A\left|u_{2}\right|^{p-2} u_{2}-B F\left(u_{2}\right) \leq 0, \\
u_{1} \leq u_{2} \text { on } \partial \Omega, \quad u_{1} \geq 0, u_{2}>0 \quad \text { on } \Omega .
\end{array}\right.$$
Then, either
i) $u_{1} \leq u_{2}$ on $\Omega$, or
ii) $B(x) \equiv 0$ on $\Omega, u_{2}$ satisfies $Q_{A}^{\prime}\left(u_{2}\right)=0, u_{2} \equiv 0$ on $\partial \Omega$, and $\lambda_{A}(\Omega)=0$.

\footnotetext{
${ }^{2}$ Briefly, $|\phi|$ still minimizes the Rayleigh quotient in (3.8), thus it satisfies the Euler-Lagrange equation $Q_{V}^{\prime}(|\phi|)=\lambda_{V}(\Omega)|\phi|^{p-1}$, hence $|\phi|>0$ on $\Omega$ by Harnack inequality in Theorem 3.1. (3).
}

Proof. We let $\xi=u_{2 \mid \partial \Omega} \in C^{1, \mu}(\partial \Omega)$ and let
$$V=A(x)-B(x) \frac{F\left(u_{2}\right)}{u_{2}^{p-1}} .$$
Note that $V \in L^{\infty}(\Omega)$ by (2.6). For $x \in \partial \Omega$ such that $u_{2}(x)=0$, we let $\nu$ be the inward unit normal to $\partial \Omega$ at $x$. Then, applying Theorem 3.1 (4) we deduce that
$$\left\langle\nabla u_{2}(x), \nu\right\rangle(x)>0,$$
by continuity, there thus exists a constant $C>0$ such that
$$u_{1} \leq C u_{2} \quad \text { on } T(\partial \Omega),$$
for some tubular neighbourhood $T(\partial \Omega)$ of $\partial \Omega$. Using assumption $u_{2}>0$ on $\Omega$ we can suppose that (3.10) is true on all of $\bar{\Omega}$ with $C>1$. Because of (3.9) and since $B(x) \geq 0$, $C>1$ and, by (2.6), $F(t) / t^{p-1}$ is increasing on $\mathbb{R}^{+}, C u_{2}$ is still a supersolution:
$$\begin{aligned}
& \Delta_{p, f}\left(C u_{2}\right)+A\left(C u_{2}\right)^{p-1}-B F\left(C u_{2}\right)=C^{p-1}\left[\Delta_{p, f} u_{2}+A u_{2}^{p-1}\right]-B F\left(C u_{2}\right) \\
& \leq C^{p-1} B F\left(u_{2}\right)-B F\left(C u_{2}\right) \leq B\left(C u_{2}\right)^{p-1}\left[\frac{F\left(u_{2}\right)}{u_{2}^{p-1}}-\frac{F\left(C u_{2}\right)}{\left(C u_{2}\right)^{p-1}}\right] \leq 0 .
\end{aligned}$$
Using $u_{1} \geq 0$ as a subsolution, by (3.10) and applying the method of sub- and supersolutions, see Theorem 4.14, page 272, in [25], we find a solution $v$ of
$$\left\{\begin{array}{l}
\Delta_{p, f} v+A|v|^{p-2} v-B F(v)=0, \\
v=u_{2} \quad \text { on } \partial \Omega,
\end{array}\right.$$
satisfying
$$u_{1} \leq v \leq C u_{2} \quad \text { on } \Omega$$
By the $C^{1, \mu}$-regularity of Theorem 3.1, $v \in C^{1, \alpha}(\bar{\Omega})$ for some $\alpha \in(0,1)$. If we show that $v \leq u_{2}$ then (3.12) implies $u_{1} \leq u_{2}$ on $\Omega$ which is the conclusion $i$ ) of the Proposition.

Suppose that this is not the case, that is, assume that the open set $U=\left\{v>u_{2}\right\}$ is non-empty. We are going to prove that ii) holds. Since $v \geq u_{1} \geq 0$ and $v$ is positive on $U$, then $v>0$ on $\Omega$ as a consequence of the Harnack inequality in Theorem 3.1 (use $V=A(x)-B(x) F(v) / v^{p-1}$, which by (2.6) is bounded on $\Omega$ ). Alternatively, one can use the version of the strong maximum principle in Theorem 5.4.1 in [70]. Now, again by the Hopf Lemma of Theorem 3.1. $\langle\nabla v(x), \nu(x)\rangle>0, \nu$ the inward unit normal to $\partial \Omega$ at $x$, at each point $x \in \partial \Omega$ where $v(x)=u_{2}(x)=0$. Hence, the ratio $u_{2} / v$ is well defined at $x$ along the half line determined by $\nu$. This shows that $u_{2} / v$ and similarly $v / u_{2}$ are in $L^{\infty}(\Omega)$. Applying Proposition 3.2 on $U$ we deduce $I\left(u_{2}, v\right) \geq 0$, and $I\left(u_{2}, v\right)=0$ if and only if $u_{2}$ and $v$ are proportional on $U$. However, the positivity of the test function $\left(v^{p}-u_{2}^{p}\right) / u_{2}^{p-1}>0$ on $U$ implies, by (3.9) and (3.11), that
$$0 \leq I\left(u_{2}, v\right) \leq-\int_{U} B\left(u_{2}^{p}-v^{p}\right)\left(\frac{F\left(u_{2}\right)}{u_{2}^{p-1}}-\frac{F(v)}{v^{p-1}}\right) \mathrm{d} \mu_{f} .$$
Being $F(t) / t^{p-1}$ strictly increasing on $\mathbb{R}^{+}$and $B \geq 0$, we deduce
$$B\left(u_{2}^{p}-v^{p}\right)\left(\frac{F\left(u_{2}\right)}{u_{2}^{p-1}}-\frac{F(v)}{v^{p-1}}\right) \geq 0$$
on $U$, whence $I\left(u_{2}, v\right)=0$. We therefore conclude that $u_{2}=c v$ on $U$, for some constant $c$ which, because of the definition of $U$, satisfies $c>1$. Using that $v=u_{2}$ on $\partial U$, we
necessarily have $v=u_{2}=0$ on $\partial U$, hence $U \equiv \Omega$. Substituting $u_{2}=c v$ on $\Omega$ into (3.13) we deduce
$$B\left(c^{p}-1\right) v^{p-1}\left(\frac{F(c v)}{(c v)^{p-1}}-\frac{F(v)}{v^{p-1}}\right) \equiv 0 .$$
Since $v>0$ on $\Omega$ and $F(t) / t^{p-1}$ is strictly increasing, $B \equiv 0$ and, from (3.11), $v>0$ solves
$$\left\{\begin{array}{l}
\Delta_{p, f} v+A(x)|v|^{p-2} v=0 \quad \text { on } \Omega \\
v=0 \quad \text { on } \partial \Omega .
\end{array}\right.$$
Consequently, 0 admits a positive eigenfunction of $Q_{A}^{\prime}$. By a result in [6], $\lambda_{A}(\Omega)=0$, showing the validity of $i i)$. \(\square\)

Remark 3.2. We underline that, in the above proposition, the non-negativity of $Q_{A}$ is not required. However, if $B \equiv 0, u_{2}$ turns out to be a positive solution of $Q_{A}(u) \geq 0$, and using Proposition 3.4 below we automatically have $\lambda_{A}(\Omega) \geq 0$.

In what follows we shall frequently use the next formula: for $I \subset \mathbb{R}$ and $\alpha \in C^{2}(I)$ with $\alpha^{\prime}>0$ on $I$, and for $u \in C^{0}(M) \cap W_{\text {loc }}^{1, p}(M)$ with $u(M) \subset I$ we have, weakly on $M$,
$$\Delta_{p, f} \alpha(u)=\alpha^{\prime}(u)\left|\alpha^{\prime}(u)\right|^{p-2} \Delta_{p, f} u+(p-1) \alpha^{\prime \prime}(u)\left|\alpha^{\prime}(u)\right|^{p-2}|\nabla u|^{p} .$$
A second ingredient is the following existence result that goes under the name of the Allegretto-Piepenbrink theorem, see [5, 4, 33]. We include a proof of the next slightly more general version, for the sake of completeness.

Proposition 3.4. Let $(M,\langle\rangle$,$) be a non-compact Riemannian manifold, f \in C^{\infty}(M)$, $p \in(1,+\infty)$ and, for $V \in L_{\text {loc }}^{\infty}(M)$, set $Q_{V}^{\prime}, Q_{V}$ as in (2.8) and (2.7). Then, the following statements are equivalent:
\begin{itemize}
\item[i)] There exists $w \in C^{0}(M) \cap W_{\text {loc }}^{1, p}(M), w>0$ weak solution of
$$Q_{V}^{\prime}(w) \geq 0 \quad \text { on } M ;$$
\item[ii)] There exists $u \in C_{\text {loc }}^{1, \mu}(M), u>0$ weak solution of
$$Q_{V}^{\prime}(u)=0 \quad \text { on } M ;$$
\item[iii)] $Q_{V} \geq 0$ on $M$.
\item[iv)] For each relatively compact domain $\Omega \Subset M$ with $C^{1, \alpha}$ boundary for some $\alpha \in(0,1)$, and for each $\xi \in C^{1, \alpha}(\partial \Omega), \xi \geq 0$, there exists a unique solution $\varphi \in C^{1, \mu}(\bar{\Omega})$ of
$$\begin{cases}Q_{V}^{\prime}(\varphi)=0 & \text { on } \Omega, \\ \varphi=\xi & \text { on } \partial \Omega\end{cases}$$
satisfying $\varphi \geq 0$ on $\Omega$. Moreover, if $\xi \not \equiv 0$, then $\varphi>0$ on $\Omega$.
\end{itemize}

Proof. The scheme of proof is $i i) \Rightarrow i) \Rightarrow i i i) \Rightarrow i v) \Rightarrow i i)$; Note that the first implication is trivial.
$i) \Rightarrow i i i)$. It follows immediately from Proposition 3.1 and the non-negativity of $\mathcal{L}$. $i i i) \Rightarrow i v)$. By assumption $\lambda_{V}(M) \geq 0$; it follows that, for $\Omega$ as in $i v$ ), by the monotonicity property for eigenvalues $\lambda_{V}(\Omega)>0$. Hence, the variational problem associated to (3.17) is coercive and sequentially weakly lower-semicontinuous (see also Theorem 7.1 in Appendix). Therefore (3.17) admits a weak solution $\varphi \in W^{1, p}(\Omega)$. By the $C^{1, \mu}$-regularity of Theorem 3.1 we have that $\varphi \in C^{1, \mu}(\bar{\Omega})$ for some $\mu \in(0,1)$.

Moreover, by the local Harnack inequality of item (3), $\varphi>0$ on $\bar{\Omega}$ whenever $\phi \geq 0$ on $\Omega$, unless $\varphi \equiv 0$.

By contradiction suppose that $\varphi$ is somewhere negative in $\Omega$. Since $\xi \geq 0$, on $\partial \Omega$, $\varphi_{-}=-\min \{\varphi, 0\} \in \operatorname{Lip}_{0}(\Omega)$ and it is thus an admissible test function for (3.17) on $\Omega$. We have
$$0=Q_{V}^{\prime}(\varphi)\left[-\varphi_{-}\right] \doteq-\int_{\Omega}\left\{|\nabla \varphi|^{p-2}\left\langle\nabla \varphi, \nabla \varphi_{-}\right\rangle-V|\varphi|^{p-2} \varphi \varphi_{-}\right\} \mathrm{d} \mu_{f} \equiv p Q_{V}\left(\varphi_{-}\right)$$
and therefore $\lambda_{V}(\Omega) \leq 0$, a contradiction.
$i v) \Rightarrow i i)$. Choose an exhaustion $\left\{\Omega_{j}\right\}$ of $M$. Let $u_{j}>0, u_{j} \in C^{1, \mu_{j}}\left(\bar{\Omega}_{j}\right) \subset$ $W^{1, p}\left(\Omega_{j}\right)$ be a solution of
$$\left\{\begin{array}{l}
Q_{V}^{\prime}\left(u_{j}\right)=0 \quad \text { on } \Omega_{j} \\
u_{j}=1 \quad \text { on } \partial \Omega_{j} .
\end{array}\right.$$
Fix $x_{0} \in \Omega_{1}$ and rescale $u_{j}$ in such a way that $u_{j}\left(x_{0}\right)=1$ for every $j$. By Theorem 3.1 3), $\left\{u_{j}\right\}$ is uniformly locally bounded in $\Omega$, thus by Theorem 3.12) $\left\{u_{j}\right\}$ is uniformly locally bounded in $C^{1, \mu}(\Omega)$. It follows that $\left\{u_{j}\right\}$ has a subsequence converging weakly and pointwise to a weak solution $u \in C_{\text {loc }}^{1, \mu}(M)$ of
$$\left\{\begin{array}{l}
Q_{V}^{\prime}(u)=0 \quad \text { on } M \\
u\left(x_{0}\right)=1 .
\end{array}\right.$$
Since $u \geq 0$ and $u \not \equiv 0$, again by 3) of Theorem 3.1 we deduce $u>0$ on $M$. This shows the validity of $i i$ ). \(\square\)
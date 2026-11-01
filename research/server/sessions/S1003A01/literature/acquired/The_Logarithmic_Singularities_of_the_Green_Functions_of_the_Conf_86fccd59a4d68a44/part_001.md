---
retention_scope: session
part: 1
total_parts: 2
---

[Part 1/2 of: The Logarithmic Singularities of the Green Functions of the Conformal Powers of the Laplacian]

---
source_file: 1306_3104.pdf
converter: mathpix
format: mmd
---

\title{
THE LOGARITHMIC SINGULARITIES OF THE GREEN FUNCTIONS OF THE CONFORMAL POWERS OF THE LAPLACIAN
}

\author{
RAPHAËL PONGE
}

\begin{abstract}
Green functions play an important role in conformal geometry. In this paper, we explain how to compute explicitly the logarithmic singularities of the Green functions of the conformal powers of the Laplacian. These operators include the Yamabe and Paneitz operators, as well as the conformal fractional powers of the Laplacian arising from scattering theory for Poincaré-Einstein metrics. The results are formulated in terms of Weyl conformal invariants arising from the ambient metric of Fefferman-Graham. As applications we obtain characterizations in terms of Green functions of locally conformally flat manifolds and a spectral theoretic characterization of the conformal class of the round sphere.
\end{abstract}

\section*{Introduction}

Motivated by the analysis of the singularity of the Bergman kernel of a strictly pseudoconvex domain $\Omega \subset \mathbb{C}^{n}$, Fefferman [Fe3] launched the program of determining all local invariants of a strictly pseudoconvex CR structure. This program was subsequently extended to deal with local invariants of other parabolic geometries, including conformal geometry [FG1, BEG]. It has since found connections with various areas of mathematics and mathematical physics such as geometric PDEs, geometric scattering theory and conformal field theory. For instance, the Poincaré-Einstein metric of Fefferman-Graham [FG1, FG3] was a main impetus for the AdS/CFT correspondance.

Green functions of conformally invariant operators plays a fundamental role in conformal geometry. Parker-Rosenberg [PR] computed the logarithmic singularity of Yamabe operator in low dimension. In [Po1, Po2] it was shown that the logarithmic singularities of Green functions of conformally invariant $\Psi$ DOs are linear combinations of Weyl conformal invariants. Those invariants are obtained from complete metric constructions of the covariant derivatives of the curvature tensor of ambient metric of Fefferman-Graham [FG1, FG3]. The approach of [PR] was based on results of Gilkey [Gi3] on heat invariants for Laplace-type operators. It is not clear how to extend this approach to higher order GJMS operators, leave aside conformal fractional powers of the Laplacian.

Exploiting the invariant theory for conformal structures, the main result of this paper is an explicit, and surprinsingly simple, formula for the logarithmic singularities of the Green functions of the conformal powers of the Laplacian in terms of Weyl conformal invariants obtained from the heat invariants of the Laplace operator (Theorem 7.3). Here by conformal powers we mean the operators of Graham-Jenne-Mason-Sparling [GJMS] and, more generally, the conformal fractional powers of the Laplacian [GZ]. These operators include the Yamabe and Paneitz operators.

Granted this result, it becomes straightforward to compute the logarithmic singularities of the Green functions of the conformal powers of the Laplacian from the sole knowledge of the heat invariants of the Laplace operators (see Theorem 7.8 and Theorem 7.9). These results have several important consequences.

In dimension $n \geq 5$ the logarithmic singularity of Green function of the $k$-th conformal power of the Laplacian with $k=\frac{n}{2}-2$ is of special interest since this is a scalar multiple of the normsquare of the Weyl tensor. As a result we see that the vanishing of this logarithmic singularity is equivalent to local conformal-flatness (Theorem 7.11). This can be seen as version in conformal geometry of the conjecture of Radamanov [Ra] on the vanishing of the logarithmic singularity of

\footnotetext{
The research of this paper was partially supported by NSERC discovery grant 341328-07 (Canada), JSPS grant in aid 30549291(Japan), research resettlement and foreign faculty research grants from Seoul National University, and NRF grant for basic research 2013R1A1A2008802 (South Korea).
}
the Bergman kernel. This also enables us to obtain a spectral theoretic characterization of the conformal class of the round sphere amount compact simply connected manifolds of dimension $\geq 5$ (see Theorem 7.13).

The idea behind the proof of Theorem 7.3 is the following. In the Riemannian case, there is a simple relationship between the logarithmic singularities of the Green functions of the powers of the Laplace operator and its heat invariant (see Eq. (6.7)). We may expect that by some analytic continuation of the signature this relationship still pertains in some way in non-Riemannian signature. The GJMS operators are obtained from the powers of the Laplacian associated to the ambient metric (which has Lorentzian signature), so there ought to be some relations between the logarithmic singularities of the Green functions of the conformal powers of the Laplace operator and its heat invariants.

One way to test this conjecture is to look at the special case of Ricci-flat metrics. In this case the computation follows easily from the Riemannian case. The bulk of the proof then is to show that the Ricci-flat case implies the general case. Thus, the analytic extension of the signature is replaced by the new principle that in order to prove an equality between conformal invariants it is enough to prove it for Ricci-flat metrics.

This "Ricci-flat principle" is actually fairly general, and so the results should also for other type of conformally invariant operators that are conformal analogues of elliptic covariant operators. In particular, it should hold for conformal powers of the Hodge Laplacian on forms [BG, Va2] and the conformal powers of the square of the Dirac operator [GMP1, GMP2].

In addition, this approach can be extended to the setting of CR geometry. In particular, in [Po1, Po2] it was shown that the logarithmic singularities of the Green functions of CR invariant hypoelliptic $\Psi_{H}$ DOs are linear combinations of Weyl CR invariants. We may also expect relate the logarithmic singularities of the Green functions of the CR invariant powers of the sub-Laplacian [GG] to the heat invariants of the sub-Laplacian [BGS]. However, the heat invariants for the sub-Laplacian are much less known than that for the Laplace operator. In particular, in order to recapture the Chern tensor requires computing the 3rd coefficient in the heat kernel asymptotics for the sub-Laplacian. In fact, for our purpose it would be enough to carry out the computation in the special case of circle bundles over Ricci-flat Kähler manifolds.

This paper is organized as follows. In Section 1, we recall the main facts on the heat kernel asymptotics for the Laplace operator. In Section 2, we recall the geometric description of the singularity of the Bergman kernel of a strictly pseudoconvex complex domain and the construction of local CR invariants by means of Fefferman's ambient Kähler-Lorentz metric. In Section 3. we recall the construction of the Fefferman-Graham's ambient metric and GJMS operators. In Section 4, we recall the construction of local conformal invariants by means of the ambient metric. In Section 5, we explain the construction of conformal fractional powers of the Laplacian and its connection with scattering theory and the Poincaré-Einstein metric. In Section 6, we gather basic facts about Green functions and their relationship with heat kernels. In Section 7, we state the main result and derive various consequences. In Section 8, we give an outline of the proof of the main result.

Acknowledgements. It is a pleasure to thank Pierre Albin, Charles Fefferman, Rod Gover, Robin Graham, Colin Guillarmou, Kengo Hirachi, Dmitry Jakobson, Andreas Juhl, Andras Vasy, and Maciej Zworski for various discussions related to the subject matter of this paper. Part of the research of this paper was carried out during visits to Kyoto University, McGill University, MSRI, UC Berkeley, and the University of Tokyo. The author wish to thank these institutions for their hospitality.

\section*{1. The Heat Kernel of the Laplace Operator}

The most important differential operator attached to a closed Riemannian manifold $\left(M^{n}, g\right)$ is the Laplace operator,
$$\Delta_{g} u=\frac{-1}{\sqrt{\operatorname{det} g(x)}} \sum_{i, j} \partial_{i}\left(g^{i j}(x) \sqrt{\operatorname{det} g(x)} \partial_{j} u\right) .$$

This operator lies at the interplay between Riemannian geometry and elliptic theory. On the one hand, a huge amount of geometric information can be extracted from the analysis of the Laplace operator. For instance, if $0=\lambda_{0}\left(\Delta_{g}\right)<\lambda_{1}\left(\Delta_{g}\right) \leq \lambda_{2}\left(\Delta_{g}\right) \leq \cdots$ are the eigenvalues of $\Delta_{g}$ counted with multiplicity, then Weyl's Law asserts that, as $k \rightarrow \infty$,
$$\lambda_{k}\left(\Delta_{g}\right) \sim(c k)^{\frac{2}{n}}, \quad c:=(4 \pi)^{-\frac{n}{2}} \Gamma\left(\frac{n}{2}+1\right)^{-1} \operatorname{Vol}_{g}(M),$$
where $\operatorname{Vol}_{g}(M)$ is the Riemannian volume of $(M, g)$. On the other hand, Riemannian geometry is used to describe singularities or asymptotic behavior of solutions of PDEs associated to the Laplace operator. This aspect is well illustrated by the asymptotics of the heat kernel of $\Delta_{g}$.

Denote by $e^{-t \Delta_{g}}, t>0$, the semigroup generated by $\Delta_{g}$. That is, $u(x, t)=\left(e^{-t} \Delta_{g} u_{0}\right)(x)$ is solution of the heat equation,
$$\left(\partial_{t}+\Delta_{g}\right) u(x, t)=0, \quad u(x, t)=u_{0}(x) \quad \text { at } t=0 .$$
The heat kernel $K_{\Delta_{g}}(x, y ; t)$ is the kernel function of the heat semigroup,
$$e^{-t \Delta_{g}} u(x)=\int_{M} K_{\Delta_{g}}(x, y ; t) u(y) v_{g}(y),$$
where $v_{g}(y)=\sqrt{g(x)}|d x|$ is the Riemannian volume density. Equivalently, $K_{\Delta_{g}}(x, y ; t)$ provides us with a fundamental solution for the heat equation (1). Furthermore,
$$\sum e^{-t \lambda_{j}\left(\Delta_{g}\right)}=\operatorname{Tr} e^{-t \Delta_{g}}=\int_{M} K_{\Delta_{g}}(x, x ; t) u(x) v_{g}(x) .$$

Theorem 1.1 (ABP, Gi1, Mi]). Let $\left(M^{n}, g\right)$ be a closed manifold. Then
\begin{itemize}
\item[(1)] As $t \rightarrow 0^{+}$,
$$K_{\Delta_{g}}(x, x ; t) \sim(4 \pi t)^{-\frac{n}{2}} \sum_{j \geq 0} t^{j} a_{2 j}\left(\Delta_{g} ; x\right),$$
where the asymptotics holds with respect to the Fréchet-space topology of $C^{\infty}(M)$.
\item[(2)] Each coefficient $a_{2 j}\left(\Delta_{g} ; x\right)$ is a local Riemannian invariant of weight $2 j$.
\end{itemize}

Remark 1.2. There is an asymptotics similar to (1.3) for the heat kernel of any selfadjoint differential operators with positive-definite principal symbol (see [Gi3, Gr]).

Remark 1.3. A local Riemannian invariant is a (smooth) function $I_{g}(x)$ of $x \in M$ and the metric tensor $g$ which, in any local coordinates, has an universal expression of the form,
$$I_{g}(x)=\sum a_{\alpha \beta}(g(x))\left(\partial^{\beta} g(x)\right)^{\alpha},$$
where the sum is finite and the $a_{\alpha \beta}$ are smooth functions on $\mathrm{Gl}_{n}(\mathbb{R})$ that are independent of the choice of the local coordinates. We further say that $I_{g}(x)$ has weight $w$ when
$$I_{\lambda^{2} g}(x)=\lambda^{-w} I_{g}(x) \quad \forall \lambda>0 .$$
These definitions continue to make sense for pseudo-Riemannian structures of nonpositive signature. Note also that with our convention for the weight, the weight is always an even nonnegative integer.

Examples of Riemannian invariants are provided by complete metric contractions of the tensor products of covariant derivatives of the curvature tensors $R_{i j k l}=\left\langle R\left(\partial_{i}, \partial_{j}\right) \partial_{k}, \partial_{l}\right\rangle$. Namely,
$$\operatorname{Contr}_{g}\left(\nabla^{k_{1}} R \otimes \cdots \otimes \nabla^{k_{l}} R\right) .$$
Such an invariant has weight $w=\left(k_{1}+\cdots+k_{l}\right)+2 l$ and is called a Weyl Riemannian invariant. Up to a sign factor, the only Weyl Riemannian invariants of weight $w=0$ and $w=2$ are the constant function 1 and the scalar curvature $\kappa:=R^{i j}{ }_{j i}$ respectively. In weight $w=4$ we obtain the following four invariants,
$$\kappa^{2},\left.\quad\left|\operatorname{Ric}^{2}:=\operatorname{Ric}^{i j} \operatorname{Ric}_{i j}, \quad\right| R\right|^{2}:=R^{i j k l} R_{i j k l}, \quad \Delta_{g} \kappa,$$
where $\operatorname{Ric}_{i j}:=R_{i j k}^{k}$ is the Ricci tensor. In weight $w=6$ they are 17 such invariants; the only invariants that do not involve the Ricci tensor are
$$|\nabla R|^{2}:=\nabla^{m} R^{i j k l} \nabla_{m} R_{i j k l}, \quad R_{i j}{ }^{k l} R^{i j}{ }_{p q} R^{p q}{ }_{k l}, \quad R_{i j k l} R_{p}^{i}{ }_{q}{ }^{k} R^{p j q l} .$$

Theorem 1.4 (Atiyah-Bott-Patodi [ABP]). Any local Riemannian invariant of weight $w, w \in$ $2 \mathbb{N}_{0}$, is a universal linear combination of Weyl Riemannian invariants of same weight.

Remark 1.5. By using normal coordinates the proof is reduced to determining all invariant polynomial of the orthogonal group $\mathrm{O}(n)$ (or $\mathrm{O}(p, q)$ in the pseudo-Riemannian case). They are determined thanks to Weyl's invariant theory for semisimple groups.

Combining Theorem 1.1 and Theorem 1.4 we obtain the following structure theorem for the heat invariants.

Theorem 1.6 (Atiyah-Bott-Patodi [ABP]). Each heat invariant $a_{2 j}\left(\Delta_{g} ; x\right)$ in (1.3) is a universal linear combination of Weyl Riemannian invariants of weight $2 j$.

Remark 1.7. There is a similar structure result for the heat invariants of any selfadjoint elliptic covariant differential operator with positive principal symbol.

In addition, the first few of the heat invariants are computed.
Theorem 1.8 ( [BGM, MS, Gi2] ). The first four heat invariants $a_{2 j}\left(\Delta_{g} ; x\right), j=0, \ldots, 3$ are given by the following formulas,
$$\begin{gathered}
a_{0}\left(\Delta_{g} ; x\right)=1, \quad a_{2}\left(\Delta_{g} ; x\right)=-\frac{1}{6} \kappa, \left.\quad a_{4}\left(\Delta_{g} ; x\right)=\frac{1}{180}|R|^{2}-\frac{1}{180} \right\rvert\, \text { Ric }\left.\right|^{2}+\frac{1}{72} \kappa^{2}-\frac{1}{30} \Delta_{g} \kappa \\
a_{6}\left(\Delta_{g} ; x\right)=\frac{1}{9 \cdot 7!}\left(81|\nabla R|^{2}+64 R_{i j}{ }^{k l} R^{i j}{ }_{p q} R^{p q}{ }_{k l}+352 R_{i j k l} R_{p}^{i}{ }_{q}{ }_{q} R^{p j q l}\right) \\
+ \text { Weyl Riemannian invariants involving the Ricci tensor. }
\end{gathered}$$
Remark 1.9. We refer to Gilkey's monograph [Gi3] for the full formula for $a_{6}\left(\Delta_{g} ; x\right)$ and formulas for the heat invariants of various Laplace type operators, including the Hodge Laplacian on forms. We mention that Gilkey's formulas involve a constant multiple of $-\left\langle R, \Delta_{g} R\right\rangle=g^{p q} R_{i j k l} R_{i j k l ; p q}$, but this Weyl Riemannian invariant is a linear combination of other Weyl Riemannian invariants. In particular, using the Bianchi identities we find that, modulo Weyl Riemannian involving the Ricci tensor,
$$-\left\langle R, \Delta_{g} R\right\rangle=R_{i j}{ }^{k l} R^{i j}{ }_{p q} R^{p q}{ }_{k l}+4 R_{i j k l} R_{p}^{i}{ }_{q}{ }_{q} R^{p j q l} .$$
This relation is incorporated into (1.5).
Remark 1.10. Polterovich [Po] established formulas for all the heat invariants $a_{j}\left(\Delta_{g} ; x\right)$ in terms of the Riemannian distance function.

Remark 1.11. Combining the equality $a_{0}\left(\Delta_{g} ; x\right)=1$ with (1.2) and (1.3) shows that, as $t \rightarrow 0^{+}$,
$$\sum e^{-t \lambda_{j}\left(\Delta_{g}\right)} \sim(4 \pi t)^{-\frac{n}{2}} \int_{M} v_{g}(x)=(4 \pi t)^{-\frac{n}{2}} \operatorname{Vol}_{g}(M) .$$
We then can apply Karamata's Tauberian theorem to recover Weyl's Law (1.1).
Remark 1.12. A fundamental application of the Riemannian invariant theory of the heat kernel asymptotics is the proof of the local index theorem by Atiyah-Bott-Patodi [ABP] (see also [Gi3]).

\section*{2. The Bergman Kernel of a Strictly Pseudoconvex Domain}

A fundamental problem in several complex variables is to find local computable biholomorphic invariants of a strictly pseudoconvex domain $\Omega \subset \mathbb{C}^{n}$. One approach to this issue is to look at the
boundary singularity of the Bergman metric of $\Omega$ or equivalently its Bergman kernel. Recall that the Bergman kernel is the kernel function of the orthogonal projection,
$$\begin{gathered}
B_{\Omega}: L^{2}(\Omega) \longrightarrow L^{2}(\Omega) \cap \operatorname{Hol}(\Omega) \\
B_{\Omega} u(z)=\int K_{\Omega}(z, w) u(w) d w
\end{gathered}$$
For instance, in the case of the unit ball $\mathbb{B}^{2 n}=\{|z|<1\} \subset \mathbb{C}^{n}$ we have
$$B_{\mathbb{B}^{2 n}}(z, w)=\frac{n!}{\pi^{n}}(1-z \bar{w})^{-(n+1)} .$$

The Bergman kernel lies at the interplay of complex analysis and differential geometry. On the one hand, it provides us with the reproducing kernel of the domain $\Omega$ and it plays a fundamental role in the analysis of the $\bar{\partial}$-Neuman problem on $\Omega$. On the other hand, it provides us with a biholomorphic invariant Kähler metric, namely, the Bergman metric,
$$d s^{2}=\sum \frac{\partial^{2}}{\partial z^{j} \partial z^{\bar{k}}} \log B(z, z) d z^{j} d z^{\bar{k}} .$$

In what follows we let $\rho$ be a defining function of $\Omega$ so that $\Omega=\{\rho<0\}$ and $i \partial \bar{\partial} \rho>0$.
Theorem 2.1 (Fefferman, Boutet de Monvel-Sjöstrand). Near the boundary $\partial \Omega=\{\rho=0\}$,
$$K_{\Omega}(z, z)=\varphi(z) \rho(z)^{-(n+1)}-\psi(z) \log \rho(z),$$
where $\varphi(z)$ and $\psi(z)$ are smooth up to $\partial \Omega$.
Motivated by the analogy with the heat asympototics (1.3), where the role of the time variable $t$ is played by the defining function $\rho(z)$, Fefferman [Fe3] launched the program of giving a geometric description of the singularity of the Bergman kernel similar to the description provided by Theorem 1.1 and Theorem 1.6 for the heat kernel asymptotics.

A first issue at stake concerns the choice of the defining function. We would like to make a biholomorphically invariant choice of defining function. This issue is intimately related to the complex Monge-Ampère equation on $\Omega$ :
$$J(u):=(-1)^{n} \operatorname{det}\left(\begin{array}{cc}
u & \partial_{z^{\bar{k}}} u \\
\partial_{z^{j}} u & \partial_{z^{j}} \partial_{z^{\bar{k}}} u
\end{array}\right), \quad u_{\mid \partial \Omega}=0 .$$
A solution of the Monge-Ampère equation is unique and biholomorphically invariant in the sense that, given any bilohomorphism $\Phi: \Omega \rightarrow \Omega$, we have
$$u(\Phi(z))=\left|\operatorname{det} \Phi^{\prime}(z)\right|^{\frac{2}{n+1}} u(z) .$$

We mention the following important results concerning the Monge-Ampère equation.
Theorem 2.2 (Cheng-Yau [CY]). Let $\Omega \subset \mathbb{C}^{n}$ be a strictly pseudoconvex domain.
\begin{itemize}
\item[(1)] There is a unique exact solution $u_{0}(z)$ of the complex Monge-Ampère equation (2.1).
\item[(2)] The solution $u_{0}(z)$ is $C^{\infty}$ on $\Omega$ and belongs to $C^{n+\frac{3}{2}-\epsilon}(\bar{\Omega})$ for all $\epsilon>0$.
\item[(3)] The metric $d s^{2}=\sum \frac{\partial^{2}}{\partial z^{j} \partial z^{\bar{k}}} \log \left(u_{0}(z)^{-(n+1)}\right) d z^{j} d z^{\bar{k}}$ is a Kähler-Einstein metric on $\Omega$.
\end{itemize}

Theorem 2.3 (Lee-Melrose [LM]). Let $\Omega \subset \mathbb{C}^{n}$ be a strictly pseudoconvex domain with defining function $\rho(z)$. Then, near the boundary $\partial \Omega=\{\rho=0\}$, the Cheng-Yau solution to the Monge-Ampère equation has a behavior of the form,
$$u_{0}(z) \sim \rho(z) \sum_{k \geq 0} \eta_{k}(z)\left(\rho(z)^{n+1} \log \rho(z)\right)^{k},$$
where the functions $\eta_{k}(z)$ are smooth up to the boundary.
The Cheng-Yau solution is not smooth up to the boundary, but if we only seek for asymptotic solutions then we do get smooth solutions.

Theorem 2.4 (Fefferman [Fe1]). Let $\Omega \subset \mathbb{C}^{n}$ be a strictly pseudoconvex domain with defining function $\rho(z)$. Then there are functions in $C^{\infty}(\bar{\Omega})$ that are solutions to the asymptotic Monge-Ampère equation,
$$J(u)=1+\mathrm{O}\left(\rho^{n+1}\right) \text { near } \partial \Omega, \quad u_{\mid \partial \Omega}=0 .$$

Remark 2.5. As it can be seen from (2.2), the error term $\mathrm{O}\left(\rho^{n+1}\right)$ cannot be improved in general if we seek for a smooth approximate solution.

Any smooth solution $u(z)$ of (2.3) is a defining function for $\Omega$ and it is asymptotically biholomorphically invariant in the sense that, for any biholomorphism $\Phi: \Omega \rightarrow \Omega$,
$$u(\Phi(z))=\left|\operatorname{det} \Phi^{\prime}(z)\right|^{\frac{2}{n+1}} u(z)+\mathrm{O}\left(\rho(z)^{n+1}\right)$$

The complex structure of $\Omega$ induces on the boundary $\partial \Omega$ a strictly pseudoconvex CR structure. As a consequence of a well-known result of Fefferman [Fe2] there is one-to-one correspondance between biholomorphisms of $\Omega$ and CR diffeomorphisms of $\partial \Omega$. Therefore, boundary values of biholomorphic invariants of $\Omega$ gives rise to CR invariants of $\partial \Omega$. We refer to [Fe3] for the precise definition of a local CR invariant. Let us just mention that a local CR invariant $I(z)$ has weight $\omega$ when, for any biholomorphism $\Phi: \Omega \rightarrow \Omega$, we have
$$I(\Phi(z))=\left|\operatorname{det} \Phi^{\prime}(z)\right|^{-\frac{w}{n+1}} I(z) \quad \text { on } \partial \Omega$$

Proposition 2.6 (Fefferman [Fe3]). Let $\Omega \subset \mathbb{C}^{n}$ be a strictly pseudoconvex domain. Then
\begin{itemize}
\item[(1)] Near the boundary $\partial \Omega$,
$$K_{\Omega}(z, z)=u(z)^{-(n+1)} \sum_{j=0}^{n+1} I_{u}^{(j)}(z) u(z)^{j}+\mathrm{O}(\log u(z)),$$
where $u(z)$ is a smooth solution of (2.3).
\item[(2)] For each $j$, the boundary value of $I_{u}^{(j)}(z)$ is a local CR invariant of weight $2 j$.
\end{itemize}

This leads us to the geometric part of program of Fefferman: determining all CR invariants of strictly pseudoconvex domain so as to have an analogue of Theorem 1.4 for CR invariants. However, the CR invariant theory is much more involved than the Riemannian invariant theory. The geometric problem reduces to the invariant theory for a parabolic subgroup $P \subset \operatorname{SU}(n+1,1)$. However, as $P$ is not semisimple, Weyl's invariant theory does not apply anymore. The corresponding invariant theory was developed by Fefferman [Fe3] and Bailey-Eastwood-Graham [BEG].

The Weyl CR invariants are constructed as follows. Let $u(z)$ be a smooth approximate solution to the Monge-Ampère equation in the sense of (2.3). On the ambient space $\mathbb{C}^{*} \times \Omega$ consider the potential,
$$U\left(z_{0}, z\right)=\left|z_{0}\right|^{2} u(z), \quad\left(z_{0}, z\right) \in \mathbb{C}^{*} \times \Omega .$$
Using this potential we define the Kähler-Lorentz metric,
$$\tilde{g}=\sum_{0 \leq j, k \leq n} \frac{\partial^{2} U}{\partial z^{j} \partial z^{\bar{k}}} d z^{j} d z^{\bar{k}} .$$
A biholomorphism $\Phi: \Omega \rightarrow \Omega$ acts on the ambient space by
$$\tilde{\Phi}\left(z_{0}, z\right)=\left(\left|\operatorname{det} \Phi^{\prime}(z)\right|^{-\frac{1}{n+1}}, \Phi(z)\right), \quad\left(z_{0}, z\right) \in \mathbb{C}^{*} \times \Omega$$
This is the transformation law under biholomorphisms for $\mathcal{K}_{\Omega}^{\frac{1}{n+1}}$, where $\mathcal{K}_{\Omega}$ is the canonical line bundle of $\Omega$.

Theorem 2.7 (Fefferman [Fe1]).
\begin{itemize}
\item[(1)] The Kähler-Lorentz metric $\tilde{g}$ is asymptotically Ricci flat and invariant under biholomorphisms in the sense that
$$\tilde{\Phi}^{*} \tilde{g}=\tilde{g}+\mathrm{O}\left(\rho(z)^{n+1}\right) \quad \text { and } \quad \operatorname{Ric}(\tilde{g})=\mathrm{O}\left(\rho(z)^{n}\right) \quad \text { near } \mathbb{C}^{*} \times \partial \Omega,$$
where $\Phi$ is any biholomorphism of $\Omega$.
\end{itemize}
\begin{itemize}
\item[(2)] The restriction of $\tilde{g}$ to $S^{1} \times \partial \Omega$ is a Lorentz metric $g$ whose conformal class is invariant under biholomorphisms.
\end{itemize}

Remark 2.8. The above construction of the ambient metric is a special case of the ambient metric construction associated to a conformal structure due to Fefferman-Graham [FG1, FG3] (see also Section 3).

Remark 2.9. We refer to [Le] for an intrinsic construction of the Fefferman circle bundle $S^{1} \times \partial \Omega$ and its Lorentz metric $g$ for an arbitrary nondegenerate CR manifold.

It follows from Theorem 2.7 that, given a Weyl Riemannian invariant $I_{\tilde{g}}\left(z_{0}, z\right)$ constructed out of the covariant derivatives of the curvature tensor of $\tilde{g}$, the boundary value of $I_{\tilde{g}}\left(z_{0}, z\right)$ is a local CR invariant provided that it does not involved covariant derivatives of too high order. This condition is fullfilled if $I_{\tilde{g}}\left(z_{0}, z\right)$ has weight $w \leq 2 n$, in which case its boundary value is a CR invariant of same weight. Such an invariant is called a Weyl CR invariant. We observe that the Ricci-flatness of the ambient metric kills all Weyl invariants involving the Ricci tensor of $\tilde{g}$. Therefore, there are much fewer Weyl CR invariants than Riemannian Weyl invariants.

The following results are the analogues of Theorem 1.4 and Theorem 1.6 for the Bergman kernel.
Theorem 2.10 (Fefferman [Fe3], Bayley-Eastwood-Graham [BEG]). Any local CR invariant of weight $w \leq 2 n$ is a linear combination of Weyl CR invariants of same weight.

Theorem 2.11 (Fefferman [Fe3], Bayley-Eastwood-Graham [BEG]). Let $\Omega \subset \mathbb{C}^{n}$ be a strictly pseudoconvex domain. Then, near the boundary $\partial \Omega$,
$$K_{\Omega}(z, z)=u(z)^{-(n+1)} \sum_{j=0}^{n+1} I_{u}^{(j)}(z) u(z)^{j}+\mathrm{O}(\log u(z)),$$
where $u(z)$ is a smooth solution of (2.3) and, for $j=0, \ldots, n+1$,
$$I_{u}^{(j)}(z)=J_{\tilde{g}}^{(j)}\left(z_{0}, z\right)_{\mid z_{0}=1},$$
where $J_{\tilde{g}}^{(j)}\left(z_{0}, z\right)$ is a linear combination of complete metric contractions of weight $w$ of the covariant derivatives of the Kähler-Lorentz metric $\tilde{g}$.

Remark 2.12. We refer to [Hi] for an invariant description of the logarithmic singularity $\psi(z)$ of the Bergman kernel.

\section*{3. Ambient Metric and Conformal Powers of the Laplacian}

Let $\left(M^{n}, g\right)$ be a Riemannian manifold. In dimension $n=2$ the Laplace operator is conformally invariant in the sense that, if we make a conformal change of metric $\hat{g}=e^{2 \Upsilon} g, \Upsilon \in C^{\infty}(M, \mathbb{R})$, then
$$\Delta_{\hat{g}}=e^{-2 \Upsilon} \Delta_{g} .$$

This conformal invariance breaks down in dimension $n \geq 3$. A conformal version of the Laplacian is provided by the Yamabe operator,
$$\begin{gathered}
P_{1, g}:=\Delta_{g}+\frac{n-2}{4(n-1)} \kappa, \\
P_{1, e^{2 \Upsilon} g}=e^{-\left(\frac{n}{2}+1\right) \Upsilon} P_{1, g} e^{\left(\frac{n}{2}-1\right) \Upsilon} \quad \forall \Upsilon \in C^{\infty}(M, \mathbb{R}) .
\end{gathered}$$
The operator of Paneitz [Pa] is a conformally invariant operator with principal part $\Delta_{g}^{2}$. Namely,
$$\begin{gathered}
P_{2, g}:=\Delta_{g}^{2}+\delta V d+\frac{n-4}{2}\left\{\frac{1}{2(n-1)} \Delta_{g} R_{g}+\frac{n}{8(n-1)^{2}} R_{g}^{2}-2|P|^{2}\right\}, \\
P_{2, e^{2 \Upsilon} g}=e^{-\left(\frac{n}{2}+2\right) \Upsilon} P_{2, g} e^{\left(\frac{n}{2}-2\right) \Upsilon} \quad \forall \Upsilon \in C^{\infty}(M, \mathbb{R}) .
\end{gathered}$$
Here $P_{i j}=\frac{1}{n-2}\left(\operatorname{Ric}_{\mathrm{g}_{i j}}-\frac{R_{g}}{2(n-1)} g_{i j}\right)$ is the Schouten-Weyl tensor and $V$ is the tensor $V_{i j}=$ $\frac{n-2}{2(n-1)} R_{g} g_{i j}-4 P_{i j}$ acting on 1-forms (i.e., $\left.V\left(\omega_{i} d x^{i}\right)=\left(V_{i}{ }^{j} \omega_{j}\right) d x^{i}\right)$.

More generally, Graham-Jenne-Mason-Sparling [GJMS] constucted higher order conformal powers of the Laplacian by using the ambient metric of Fefferman-Graham [FG1, FG3]. This metric extends Fefferman's Kähler-Lorentz metric to any ambient space associated to a conformal structure. It is constructed as follows.

Consider the ray-bundle,
$$G:=\bigsqcup_{x \in M}\left\{t^{2} g(x) ; t>0\right\} \subset S^{2} T^{*} M,$$
where $S^{2} T^{*} M$ is the bundle of symmetric (0, 2)-tensors. We note that $G$ depends only the conformal class $[g]$. Moreover, on $G$ there is a natural family of dilations $\delta_{s}, s>0$, given by
$$\delta_{s}(\hat{g})=s \hat{g} \quad \forall \hat{g} \in G .$$

Let $\pi: G \rightarrow M$ be the canonical submersion of $G$ onto $M$ (i.e., the restriction to $G$ of the canonical submersion of the bundle $S^{2} T^{*} M$ ). Let $d \pi^{t}: S^{2} T^{*} M \rightarrow S^{2} T^{*} G$ be the differential of $\pi$ on symmetric $(0,2)$-tensors. Then $G$ carries a canonical symmetric ( 0,2 )-tensor $g_{0}$ defined by
$$g_{0}(x, \hat{g})=d \pi(x)^{t} \hat{g} \quad \forall(x, \hat{g}) \in G .$$
The datum of the representative metric $g$ defines a fiber coordinate $t$ on $G$ such that $\hat{g}=t^{2} g(x)$ for all $(x, \hat{g}) \in G$. If $\left\{x^{j}\right\}$ are local coordinates on $M$, then $\left\{x^{j}, t\right\}$ are local coordinates on $G$ and in these coordinates the tensor $g_{0}$ is given by
$$g_{0}=t^{2} g_{i j}(x) d x^{i} d x^{j},$$
where $g_{i j}$ are the coefficients of the metric tensor $g$ in the local coordinates $\left\{x^{j}\right\}$.
The ambient space is the ( $n+2$ )-dimensional manifold
$$\tilde{G}:=G \times(-1,1)_{\rho},$$
where we denote by $\rho$ the variable in (-1, 1). We identify $G$ with the hypersurface $G_{0}:=\{\rho=0\}$. We also note that the dilations $\delta_{s}$ in (3.1) lifts to dilations on $\tilde{G}$.

Theorem 3.1 (Fefferman-Graham [FG1, FG3]). Near $\rho=0$ there is a Lorentzian metric $\tilde{g}$, called the ambient metric, which is defined up to infinite order in $\rho$ when $n$ is odd, and up to order $\frac{n}{2}$ when $n$ is even, such that
\begin{itemize}
\item[(i)] In local coordinates $\left\{t, x^{j}, \rho\right\}$,
$$\tilde{g}=2 \rho(d t)^{2}+t^{2} g_{i j}(x, \rho)+2 t d t d \rho,$$
where $g_{i j}(x, \rho)$ is a family of symmetric (0, 2)-tensors such that $\left.g(x, \rho)\right|_{\rho=0}=g_{i j}(x)$.
\item[(ii)] The ambient metric is asymptotically Ricci-flat, in the sense that
$$\operatorname{Ric}(\tilde{g})= \begin{cases}\mathrm{O}\left(\rho^{\infty}\right) & \text { if } n \text { is odd }, \\ \mathrm{O}\left(\rho^{\frac{n}{2}}\right) & \text { if } n \text { is even } .\end{cases}$$
\end{itemize}

Remark 3.2. We note that (i) implies that
$$\tilde{g}_{\mid T G_{0}}=g_{0} \quad \text { and } \quad \delta_{s}^{*} \tilde{g}=s^{2} \tilde{g} \quad \forall s>0,$$
where $g_{0}$ is the symmetric tensor (3.2).
Remark 3.3. The ambient metric is unique up to its order of definition near $\rho=0$. Solving the equation (3.3) leads us to a system of nonlinear PDEs for $g_{i j}(x, \rho)$. When $n$ is even, there is an obstruction to solve this system at infinite order which given by the a conformally invariant tensor. This tensor is the Bach tensor in dimension 4. Moreover, it vanishes on conformally Einstein metrics.

Example 3.4. Suppose that $(M, g)$ is Einstein with $\operatorname{Ric}(g)=2 \lambda(n-1) g$. Then
$$\tilde{g}=2 \rho(d t)^{2}+t^{2}(1+\lambda \rho)^{2} g_{i j}(x)+2 t d t d \rho .$$

Conformal powers of the Laplacian are obtained from the powers of the ambient metric Laplacian $\tilde{\Delta}_{\tilde{g}}$ on $\tilde{G}$ as follows.

Proposition 3.5 (Graham-Jenne-Mason-Sparling [GJMS]). Let $k \in \mathbb{N}_{0}$ and further assume $k \leq \frac{n}{2}$ when $n$ is even. Then
\begin{itemize}
\item[(1)] We define a operator $P_{k, g}: C^{\infty}(M) \rightarrow C^{\infty}(M)$ by
$$P_{k, g} u(x):=\left.t^{-\left(\frac{n}{2}+k\right)} \tilde{\Delta}_{\tilde{g}}^{k}\left(t^{\frac{n}{2}-k} \tilde{u}(x, \rho)\right)\right|_{\rho=0}, \quad u \in C^{\infty}(M),$$
where $\tilde{u}$ is any smooth extension of $u$ to $M \times \mathbb{R}$ (i.e., the r.h.s. above is independent of the choice of $\tilde{u}$ ).
\item[(2)] $P_{k, g}$ is a differential operator of order $2 k$ with same leading part as $\Delta_{g}^{k}$.
\item[(3)] $P_{k, g}$ is a conformally covariant differential operator such that
$$P_{k, e^{2 \Upsilon} g}=e^{-\left(\frac{1}{2} n+k\right) \Upsilon}\left(P_{k, g}\right) e^{\left(\frac{1}{2} n-k\right) \Upsilon} \quad \forall \Upsilon \in C^{\infty}(M, \mathbb{R}) .$$
\end{itemize}

Remark 3.6. The homogeneity of the ambient metric $\tilde{g}$ implies that the r.h.s. is idenpendent of $t$ and obeys (3.6).

Remark 3.7. The operator $P_{k, g}$ is called the $k$-th GJMS operator. For $k=1$ and $k=2$ we recover the Yamabe operator and Paneitz operator respectively.

Remark 3.8. The GJMS operators are selfadjoint [FG2, GZ].
Remark 3.9. The GJMS operator $P_{k, g}$ can also be obtained as the obstruction to extending a function $u \in C^{\infty}(M)$ into a homogeneous harmonic function on the ambient space. In addition, we refer to [FG4, GP, Ju1, Ju2] for various features and properties of the GJMS operarors.

Remark 3.10. When the dimension $n$ is even, the ambient metric construction is obstructed at finite order, and so the GJMS construction breaks down for $k>\frac{n}{2}$. As proved by Graham [Gr1] in dimension 4 for $k=3$ and by Gover-Hirachi [GH] in general, there do not exist conformally invariant operators with same leading part as $\Delta_{g}^{k}$ for $k>\frac{n}{2}$ when $n$ is even.

Remark 3.11. The operator $P_{\frac{n}{2}, g}$ is sometimes called the critical GJMS operator. Note that for $P_{\frac{n}{2}}$ the transformation law (3.6) becomes
$$P_{\frac{n}{2}, e^{2 \Upsilon} g}=e^{-n \Upsilon} P_{\frac{n}{2}, g} \quad \forall \Upsilon \in C^{\infty}(M, \mathbb{R}) .$$
It is tempting to use the critical GJMS operator as a candidate for a subsitute to the Laplacian to prove a version of the Knizhnik-Polyakov-Zamolodchikov (KPZ) formula in dimension $\geq 3$. We refer to [CJ] for results in this direction.

Example 3.12 (Graham [Gr2, FG3], Gover [Go]). Suppose that $\left(M^{n}, g\right)$ is a Einstein manifold with $\operatorname{Ric}_{g}=\lambda(n-1) g, \lambda \in \mathbb{R}$. Then, for all $k \in \mathbb{N}_{0}$, we have
$$P_{k, g}=\prod_{1 \leq j \leq k}\left(\Delta_{g}-\frac{1}{4} \lambda(n+2 j-2)(n-2 j)\right) .$$

\section*{4. Local Conformal Invariants}

In this section, we describe local scalar invariants of a conformal structure and explain how to construct them by means of the ambient metric of Fefferman-Graham [FG1, FG3].

Definition 4.1. A local conformal invariant of weight $w, w \in 2 \mathbb{N}_{0}$, is a local Riemannian invariant $I_{g}(x)$ such that
$$I_{e^{2 \Upsilon} g}(x)=e^{-w \Upsilon(x)} I_{g}(x) \quad \forall \Upsilon \in C^{\infty}(M, \mathbb{R}) .$$

The most important conformally invariant tensor is the Weyl tensor,
$$W_{i j k l}=R_{i j k l}-\left(P_{j k} g_{i l}+P_{i l} g_{j k}-P_{j l} g_{i k}-P_{i k} g_{j l}\right),$$
where $P_{j k}=\frac{1}{n-2}\left(\operatorname{Ric}_{j k}-\frac{\kappa_{g}}{2(n-1)} g_{j k}\right)$ is the Schouten-Weyl tensor. In particular, in dimension $n \geq 4$ the Weyl tensor vanishes if and only if $(M, g)$ is locally conformally flat. Moreover, as the Weyl tensor is conformally invariant of weight 2 , we get scalar conformal invariants by taking complete metric contractions of tensor products of the Weyl tensor.

Let $I_{g}(x)$ be a local Riemannian invariant of weight $w$. By using the ambient metric, Fefferman-Graham [FG1, FG3] produced a recipe for constructing local conformal invariant from $I_{g}(x)$ as follows.

Step 1: Thanks to Theorem 1.4 we know that $I_{g}(x)$ is a linear combination of complete metric contractions of covariant derivatives of the curvature tensor. Substituting into this complete metric contractions the ambient metric $\tilde{g}$ and the covariant derivatives of its curvature tensor we obtain a local Riemannian invariant $I_{\tilde{g}}(t, x, \rho)$ on the ambient metric space $(\tilde{G}, \tilde{g})$. For instance,
$$\operatorname{Contr}_{g}\left(\nabla^{k_{1}} R \otimes \cdots \otimes \nabla^{k_{l}} R\right) \longrightarrow \operatorname{Contr}_{\tilde{g}}\left(\tilde{\nabla}^{k_{1}} \tilde{R} \otimes \cdots \otimes \tilde{\nabla}^{k_{l}} \tilde{R}\right)$$
where $\tilde{\nabla}$ is the ambient Levi-Civita connection and $\tilde{R}$ is the ambient curvature tensor.
Step 2: We define a function on $M$ by
$$\tilde{I}_{g}(x):=\left.t^{-w} I_{\tilde{g}}(t, x, \rho)\right|_{\rho=0} \quad \forall x \in M .$$
If $n$ is odd this is always well defined. If $n$ is even this is well defined provided only derivatives of $\tilde{g}$ of not too high order are involved; this is the case if $w \leq n$. Note also that thanks to the homogeneity of the ambient metric the r.h.s. of (4.2) is always independent of the variable $t$.

Proposition 4.2 ([FG1, FG3]). The function $\tilde{I}_{g}(x)$ is a local conformal invariant of weight $w$.
Remark 4.3. The fact that $\tilde{I}_{g}(x)$ transforms conformally under conformal change of metrics is a consequence of the homogeneity of the ambient metric in (3.4).

We shall refer to the rule $I_{g}(x) \rightarrow \tilde{I}_{g}(x)$ as Fefferman-Graham's rule. When $I_{g}(x)$ is a Weyl Riemannian invariant we shall call $\tilde{I}_{g}(x)$ a Weyl conformal invariant.

Example 4.4. Let us give a few examples of using Fefferman-Graham's rule (when $n$ is even we further assume that the invariants $I_{g}(x)$ below have weight $\leq n$ ).
\begin{itemize}
\item[(a)] If $I_{g}(x)=\operatorname{Contr}_{g}\left(\nabla^{k_{1}} \operatorname{Ric} \otimes \nabla^{k_{2}} R \otimes \cdots \otimes \nabla^{k_{l}} R\right)$, then the Ricci flatness of $\hat{g}$ implies that
$$\tilde{I}_{g}(x)=0 .$$
\item[(b)] (See [FG1, FG3].) If $I_{g}(x)=\operatorname{Contr}_{g}(R \otimes \cdots \otimes R)$ (i.e., no covariant derivatives are involved), then $\tilde{I}_{g}(x)$ is obtained by substituting the Weyl tensor for the curvature tensor, that is,
$$\tilde{I}_{g}(x)=\operatorname{Contr}_{g}(W \otimes \cdots \otimes W) .$$
\item[(c)] (See [FG1, FG3].) For $I_{g}(x)=|\nabla R|^{2}$, we have
$$\tilde{I}_{g}(x)=\Phi_{g}(x):=|V|^{2}+16\langle W, U\rangle+16|C|^{2},$$
where $C_{j k l}=\nabla_{l} P_{j k}-\nabla_{k} P_{j l}$ is the Cotton tensor and the tensors $U$ and $V$ are defined by
$$\begin{gathered}
V_{m i j k l}:=\nabla_{s} W_{i j k l}-g_{i m} C_{j k l}+g_{j m} C_{i k l}-g_{k m} C_{l i j}+g_{l m} C_{k i j}, \\
U_{m j k l}:=\nabla_{m} C_{j k l}+g^{r s} P_{m r} W_{s j k l} .
\end{gathered}$$
\end{itemize}

Theorem 4.5 (Bailey-Eastwood-Graham [BEG], Fefferman-Graham [FG3]). Let $w \in 2 \mathbb{N}_{0}$, and further assume $w \leq n$ when $n$ is even. Then every local conformal invariant of weight $w$ is a linear combination of Weyl conformal invariants of same weight.

Remark 4.6. As in the Riemannian case, the strategy for the proof of Theorem 4.5 has two main steps. The first step is a reduction of the geometric problem to the invariant theory for a parabolic subgroup $P \subset \mathrm{O}(n+1,1)$. This reduction is a consequence of the jet isomorphism theorem in conformal geometry, which is proved in [FG3]. The relevant invariant theory for the parabolic subgroup $P$ is developped in [BEG].

Remark 4.7. We refer to [GrH] for a description of the local conformal invariants in even dimension beyond the critical weight $w=n$.

\section*{5. Scattering Theory and Conformal Fractional Powers of the Laplacian}

The ambient metric construction realizes a conformal structure as a hypersuface in the ambient space. An equivalent approach is to realize a conformal structure as the conformal infinity of an asymptotically hyperbolic Einstein (AHE) manifold. This enables us to use scattering theory to construct conformal fractional powers of the Laplacian.

Let $\left(M^{n}, g\right)$ be a compact Riemannian manifold. We assume that $M$ is the boundary of some manifold $\bar{X}$ with interior $X$. Note we always can realize the double $M \sqcup M$ as the boundary of $[0,1] \times M$. We assume that $X$ carries a AHE metric $g^{+}$. This means that
\begin{itemize}
\item[(1)] There is a definining function $\rho$ for $M=\partial X$ such that, near $M$, the metric $g^{+}$is of the form,
$$g^{+}=\rho^{-2} g(\rho, x)+\rho^{-2}(d \rho)^{2},$$
where $g(\rho, x)$ is smooth up $\partial X$ and agrees with $g(x)$ at $\rho=0$.
\item[(2)] The metric $g^{+}$is Einstein, i.e.,
$$\operatorname{Ric}\left(g^{+}\right)=-n g^{+} .$$
\end{itemize}
In particular $\left(X, g^{+}\right)$has conformal boundary $(M,[g])$, where $[g]$ is the conformal class of $g$.
The scattering matrix for an AHE metric $g^{+}$is constructed as follows. We denote by $\Delta_{g^{+}}$the Laplacian on $X$ for the metric $g^{+}$. The continuous spectrum of $\Delta_{g^{+}}$agrees with $\left[\frac{1}{4} n^{2}, \infty\right)$ and its pure point spectrum $\sigma_{\mathrm{pp}}\left(\Delta_{g^{+}}\right)$is a finite subset of $\left(0, \frac{1}{4} n^{2}\right)$ (see Ma1, Ma2 ). Define
$$\Sigma=\left\{s \in \mathbb{C} ; \Re s \geq \frac{n}{2}, s \notin \frac{n}{2}+\mathbb{N}_{0}, s(n-s) \notin \sigma_{\mathrm{pp}}\left(\Delta_{g^{+}}\right)\right\} .$$
For $s \in \Sigma$, consider the eigenvalue problem,
$$\Delta_{g^{+}}-s(n-s)=0 .$$
For any $f \in C^{\infty}(M)$, the above eigenvalue problem as a unique solution of the form,
$$u=F \rho^{n-s}+G \rho^{s}, \quad F, G \in C^{\infty}(\bar{X}), \quad F_{\mid \partial X}=f .$$
The scattering matrix is the operator $S_{g}(s): C^{\infty}(M) \rightarrow C^{\infty}(M)$ given by
$$S_{g}(s) f:=G_{\mid M} \quad \forall f \in C^{\infty}(M) .$$
Thus $S_{g}(s)$ can be seen as a generalized Dirichlet-to-Neuman operator, where $F_{\mid \partial X}$ represents the "Dirichlet data" and $G_{\mid \partial X}$ represents the "Neuman data".

Theorem 5.1 (Graham-Zworski [GZ]). For $z \in-\frac{n}{2}+\Sigma$ define
$$P_{z, g}:=2^{2 z} \frac{\Gamma(z)}{\Gamma(-z)} S_{g}\left(\frac{1}{2} n+z\right) .$$
The family $\left(P_{z, g}\right)$ uniquely extends to a holomorphic family of pseudodifferential operators $\left(P_{z, g}\right)_{\Re z>0}$ in such way that
\begin{itemize}
\item[(i)] The operator $P_{z, g}$ is a $\Psi D O$ of order $2 z$ with same principal symbol as $\Delta_{g}^{z}$.
\item[(ii)] The operator $P_{z, g}$ is conformally invariant in the sense that
$$P_{z, e^{2 \Upsilon} g}=e^{-\left(\frac{n}{2}+z\right) \Upsilon}\left(P_{z, g}\right) e^{\left(\frac{n}{2}-z\right) \Upsilon} \quad \forall \Upsilon \in C^{\infty}(M, \mathbb{R}) .$$
\item[(iii)] The family $\left(P_{z, g}\right)_{z \in \Sigma}$ is a holomorphic family of $\Psi D O$ s and has a meromorphic extension to the half-space $\Re z>0$ with at worst finite rank simple pole singularities.
\item[(iv)] Let $k \in \mathbb{N}$ be such that $-k^{2}+\frac{1}{4} n^{2} \notin \sigma_{\mathrm{pp}}\left(\Delta_{g^{+}}\right)$. Then
$$\lim _{z \rightarrow k} P_{z, g}=P_{k, g},$$
where $P_{k, g}$ is the $k$-th GJMS operator defined by (3.5).
\end{itemize}

Remark 5.2. Results of Joshi-Sá Barreto [JS] show that each operator $P_{z, g}$ is a Riemannian invariant $\Psi$ DO in the sense that all the homogeneous components are given by universal expressions in terms of the partial derivatives of the components of the metric $g$ (see [Po2] for the precise definition).

Remark 5.3. If $k \in \mathbb{N}$ is such that $\lambda_{k}:=-k^{2}+\frac{1}{4} n^{2} \in \sigma_{\mathrm{pp}}\left(\Delta_{g^{+}}\right)$, then (5.1) holds modulo a finite rank smoothing operator obtained as the restriction to $M$ of the orthogonal projection onto the eigenspace $\operatorname{ker}\left(\Delta_{g^{+}}-\lambda_{k}\right)$.

Remark 5.4. The analysis of the scattering matrix $S_{g}(s)$ by Graham-Zworski [GZ] relies on the analysis of the resolvent $\Delta_{g^{+}}-s(n-s)$ by Mazzeo-Melrose [MM]. Guillarmou [Gu1] established the meromorphic continuation of the resolvent to the whole complex plane $\mathbb{C}$. There are only finite rank poles when the AHE metric is even. This gives the meromorphic continuation of the scattering matrix $S_{g}(z)$ and the operators $P_{z, g}$ to the whole complex plane. We refer to [Va1, Va2] for alternative approaches to these questions.

Remark 5.5. We refer to [CM] for an interpretation of the operators $P_{z, g}$ as fractional Laplacians in the sense of Caffarelli-Sylvestre [CS].

Example 5.6 (Branson Br]). Consider the round sphere $\mathbb{S}^{n}$ seen as the boundary of the unit ball $\mathbb{B}^{n+1} \subset \mathbb{R}^{n+1}$ equipped with its standard hyperbolic metric. Then
$$P_{z, g}=\frac{\Gamma\left(\sqrt{\Delta_{g}+\frac{1}{4}(n-1)^{2}}+1+z\right)}{\Gamma\left(\sqrt{\Delta_{g}+\frac{1}{4}(n-1)^{2}}+1-z\right)}, \quad z \in \mathbb{C}$$
We refer to [GN] for an extension of this formula to manifolds with constant sectional curvature.
A general conformal structure cannot always be realized as the conformal boundary of an AHE manifold. However, as showed by Fefferman-Graham [FG1, FG3] it always can be realized as a conformal boundary formally.

Let $\left(M^{n}, g\right)$ be a Riemannian manifold. Define $X=M \times(0, \infty)$ and let $\bar{X}=M \times[0, \infty)$ be the closure of $X$. We shall denote by $r$ the variable in $[0, \infty)$ and we identify $M$ with the boundary $r=0$.

Theorem 5.7 (Fefferman-Graham [FG1, FG3]). Assume $M$ has odd dimension. Then, near the boundary $r=0$, there is a Riemannian metric $g^{+}$, called Poincaré-Einstein metric, which is defined up to infinite order in $r$ and satisfies the following properties:
\begin{itemize}
\item[(i)] In local coordinates $\left\{r, x^{j}\right\}$,
$$g^{+}=r^{-2}(d r)^{2}+r^{-2} g_{i j}(x, \rho),$$
where $g_{i j}(x, r)$ is a family of symmetric (0, 2)-tensors such that $\left.g(x, r)\right|_{r=0}=g_{i j}(x)$.
\item[(ii)] It is asymptotically Einstein in the sense that, near the boundary $r=0$,
$$\operatorname{Ric}\left(g^{+}\right)=-n g^{+}+\mathrm{O}\left(r^{\infty}\right) .$$
\end{itemize}

Remark 5.8. When the dimension $n$ is even there is also a Poincaré-Einstein metric which is defined up to order $n-2$ in $r$ and satisfies the Einstein equation (5.2) up to an $\mathrm{O}\left(r^{n-2}\right)$ error.

Remark 5.9. The constructions of the Poincaré-Einstein metric and ambient metric are equivalent. We can obtain either metric from the other. For instance, the map $\phi:(r, x) \rightarrow\left(r^{-1}, x,-\frac{1}{2} r^{2}\right)$ is a smooth embedding of $X$ into the hypersurface,
$$\mathcal{H}^{+}=\{\tilde{g}(T, T)=-1\}=\left\{(t, x \rho) ; 2 \rho t^{2}=-1\right\} \subset \tilde{G},$$
where $T=t \partial_{t}$ is the infinitesimal generator for the dilations (3.1). Then $g^{+}$is obtained as the pullback to $X$ of $\tilde{g}_{\mid T \mathcal{H}}$. In particular, the metric $g^{+}$is even in the sense that the tensor $g(x, r)$ has a Taylor expansion near $r=0$ involving even powers of $r$ only.

Example 5.10. Assume that $(M, g)$ is Einstein, with $\operatorname{Ric}(g)=2 \lambda(n-1) g$. Then
$$g^{+}=r^{-2}(d r)^{2}+r^{-2}\left(1-\frac{1}{2} \lambda r^{2}\right) g_{i j}(x) d x^{i} d x^{j}$$

Proposition 5.11. Assume $n$ is odd. Then there is an entire family $\left(P_{g, z}\right)_{z \in \mathbb{C}}$ of $\Psi D O s$ on $M$ uniquely defined up to smoothing operators such that
\begin{itemize}
\item[(i)] Each operator $P_{g, z}, z \in \mathbb{C}$, is a $\Psi D O$ of order $2 z$ and has same principal symbol as $\Delta_{g}^{z}$.
\end{itemize}
\begin{itemize}
\item[(ii)] Each operator $P_{g, z}$ is a conformally invariant $\Psi D O$ in the sense of [Po2] in such a way that, for all $\Upsilon \in C^{\infty}(M, \mathbb{R})$,
$$P_{z, e^{2 \Upsilon}} g=e^{-\left(\frac{n}{2}+z\right) \Upsilon}\left(P_{z, g}\right) e^{\left(\frac{n}{2}-z\right) \Upsilon} \quad \bmod \Psi^{-\infty}(M),$$
where $\Psi^{-\infty}(M)$ is the space of smoothing operators on $M$.
\item[(iii)] For all $k \in \mathbb{N}$, the operator $P_{z, g}$ agrees at $z=k$ with the $k$-th GJMS operator $P_{k, g}$.
\item[(iv)] For all $z \in \mathbb{C}$,
$$P_{z, g} P_{-z, g}=1 \quad \bmod \Psi^{-\infty}(M) .$$
\end{itemize}

Remark 5.12. The equation (5.4) is an immediate consequence of the functional equation for the scattering matrix,
$$S_{g}(s) S_{g}(n-s)=1 .$$
This enables us to extend the family $\left(P_{z, g}\right)$ beyond the halfspace $\Re z>0$.
Remark 5.13. When $n$ is even, we also can construct operators $P_{z, g}$ as above except that each operator $P_{z, g}$ is unique and satisfies (5.3) modulo $\Psi$ DOs of order $z-2 n$.

Remark 5.14. By using a polynomial continuation of the homogeneous components of the symbols of the GJMS operators, Petterson [Pe] also constructed a holomorphic family of $\Psi$ DOs satisfying the properties (i)-(iv) above.

Example 5.15 (Joshi-Sá Barreto [JS]). Suppose that $(M, g)$ is Ricci flat and compact. Then, for all $z \in \mathbb{C}$,
$$P_{g, z}=\Delta_{g}^{z} \quad \bmod \Psi^{-\infty}(M) .$$

As mentioned above, the constructions of the ambient metric and Poincaré-Einstein metric are equivalent. Thus, it should be possible to define the GJMS operators directly in terms of the Poincaré-Einstein metric, so as to interpret the GJMS operators as boundary operators. This interpretation is actually implicit in [GZ]. Indeed, if we combine the definition (3.5) of the GJMS operators with the formula on the 2nd line from the top on page 113 of [GZ], then we arrive at the following statement.

Proposition 5.16 ([GJMS], [GZ]). Let $k \in \mathbb{N}$ and further assume $k \leq \frac{n}{2}$ when $n$ is even. Then, for all $u \in C^{\infty}(M)$,
$$P_{k, g} u=\left.r^{-\frac{1}{2} n-k} \prod_{j=0}^{k-1}\left(\Delta_{g^{+}}+\left(-\frac{1}{2} n+k-2 j\right)\left(\frac{1}{2} n+k-2 j\right)\right)\left(r^{\frac{1}{2} n-k} u^{+}\right)\right|_{r=0},$$
where $u^{+}$is any function in $C^{\infty}(\bar{X})$ which agrees with $u$ on the boundary $r=0$.
Remark 5.17. Guillarmou [Gu2] obtained this formula via scattering theory. We also refer to [GW] for a similar formula in terms of the tractor bundle. In addition, using a similar approach as above, Hirachi [Hi] derived an analogous formula for the CR GJMS operators of Gover-Graham [GG].

\section*{6. Green Functions of Elliptic Operators}

In this section, we describe the singularities of the Green function of an elliptic operator and its closed relationship with the heat kernel asymptotics.

Let $\left(M^{n}, g\right)$ be a Riemannian manifold. Let $P: C_{c}^{\infty}(M) \rightarrow C^{\infty}(M)$ be an elliptic pseudodifferential operator ( $\Psi$ DO ) of (integer) order $m>0$. Its Green function $G_{P}(x, y)$ (when it exists) is the fundamental solution of $P$, that is,
$$P_{x} G_{P}(x, y)=\delta(x-y) .$$
Equivalently, $G_{P}(x, y)$ is the inverse kernel of $P$, i.e.,
$$P_{x}\left(\int_{M} G_{P}(x, y) u(y) v_{g}(y)\right)=u(x) .$$

In general, $P$ may have a nontrivial kernel (e.g., the kernel of the Laplace operator $\Delta_{g}$ consists of constant functions). Therefore, by Green function we shall actually mean a solution of (6.1) modulo a $C^{\infty}$-error, i.e.,
$$P_{x} G_{P}(x, y)=\delta(x-y) \quad \bmod C^{\infty}(M \times M) .$$
This means that using $G_{P}(x, y)$ we always can solve the equation $P v=u$ modulo a smooth error. In other words, $G_{P}(x, y)$ is the kernel function of parametrix for $P$. As such it always exists.

The Green function $G_{P}(x, y)$ is smooth off the diagonal $y=x$. As this is the kernel function of a pseudodifferential operator of order $-m$ (namely, a parametrix for $P$ ), the theory of pseudodifferential operators enables us to describe the form of its singularity near the diagonal.

Proposition 6.1 (See [Ta]). Suppose that $P$ has order $m \leq n$. Then, in local coordinates and near the diagonal $y=x$,
$$G_{P}(x, y)=|x-y|^{-n+m} \sum_{0 \leq j<n-m} a_{j}(x, \theta)|x-y|^{j}-\gamma_{P}(x) \log |x-y|+\mathrm{O}(1),$$
where $\theta=|x-y|^{-1}(x-y)$ and the functions $a_{j}(x, \theta)$ and $\gamma_{P}(x)$ are smooth. Moreover,
$$\gamma_{P}(x)=(2 \pi)^{-n} \int_{S^{n-1}} p_{-n}(x, \xi) d^{n-1} \xi,$$
where $p_{-n}(x, \xi)$ is the symbol of degree $-n$ of any parametrix for $P$.
Remark 6.2. The various terms in (6.2) depends on the various components of the symbol of a parametrix for $P$, and so, at the exception of the leading term $a_{0}(x, \theta)$, they transform in some cumbersome way under changes of local coordinates. However, it can be shown, that the coefficient $\gamma_{P}(x)$ makes sense intrinsically on $M$.

Remark 6.3. Suppose that $P$ is a differential operator. Then any parametrix for $P$ is odd class in the sense of [KV]. This implies that its symbols are homogeneous with respect to the symmetry $\xi \rightarrow-\xi$, e.g., $p_{-n}(x,-\xi)=(-1)^{n} p_{-n}(x, \xi)$. In particular, when the dimension $n$ is odd, we get
$$\int_{S^{n-1}} p_{-n}(x, \xi) d^{n-1} \xi=\int_{S^{n-1}} p_{-n}(x,-\xi) d^{n-1} \xi=-\int_{S^{n-1}} p_{-n}(x, \xi) d^{n-1} \xi=0$$
and hence $\gamma_{P}(x)=0$ for all $x \in M$.
The formula (6.3) provides us with a close relationship with the noncommutative residue trace of Guillemin [Gui1, Gui2] and Wodzicki Wo1, Wo2], since the right-hand side of (6.3) gives the noncommutative residue density of a parametrix for $P$. This noncommutative residue trace is the residual functional induced on integer order $\Psi$ DOs by the analytic extension of the ordinary trace to non-integer order $\Psi$ DOs. This enables us to obtain the following statement.

Proposition 6.4. Assume that $M$ is compact. Then the zeta function $\zeta(P ; s)=\operatorname{Tr} P^{-s}, \Re s>\frac{n}{m}$, has a meromorphic extension to the whole complex plane $\mathbb{C}$ with at worst simple pole singularities. Moreover, at $s=1$, we have
$$m \operatorname{Res}_{s=1} \operatorname{Tr} P^{-s}=\int_{M} \gamma_{P}(x) v_{g}(x) .$$
Remark 6.5. We refer to $[\mathrm{Se}]$ for the construction of the complex powers $P^{s}, s \in \mathbb{C}$. The construction depends on the choice of a spectral cutting for both $P$ and its principal symbol, but the residues at integer points of the zeta function $\zeta(P ; s)=\operatorname{Tr} P^{-s}$ do not depend on this choice.

Remark 6.6. Proposition 6.4 has a local version (see [Gui2, KV, Wo2]). If we denote by $K_{P^{-s}}(x, y)$ the kernel of $P^{-s}$ for $\Re s>\frac{n}{m}$, then the map $s \rightarrow K_{P^{-s}}(x, x)$ has a meromorphic extension to $\mathbb{C}$ with at worst simple pole singularities in such a way that
$$m \operatorname{Res}_{s=1} K_{P^{-s}}(x, x)=\gamma_{P}(x) .$$
We also note that the above equality continues to hold if we replace $P^{-s}$ by any holomorphic $\Psi$ DO family $P(s)$ such that $\operatorname{ord} P(s)=-m s$ and $P(1)$ is a parametrix for $P$. This way Eq. (6.5) continues to hold when $M$ is not compact.

Suppose now that $M$ is compact and $P$ has a positive leading symbol, so that we can form the heat semigroup $e^{-t P}$ and the heat kernel $K_{P}(x, y ; t)$ associated to $P$. The heat kernel asymptotics for $P$ then takes the form,
$$K_{P}(x, x ; t) \sim(4 \pi t)^{-\frac{n}{m}} \sum_{j \geq 0} t^{\frac{j}{m}} a_{j}(P ; x)+\log t \sum_{k \geq 1} t^{k} b_{j}(P ; x) \quad \text { as } t \rightarrow 0^{+} .$$
We refer to [Wi, GS] for a derivation of the above heat kernel asymptotics for $\Psi$ DOs. The residues of the local zeta function $\zeta(P ; s ; x)(x)=K_{P^{-s}}(x, x)$ are related to the coefficient in the heat kernel asymptotic for $P$ as follows.

By Mellin's formula, for $\Re s>0$ we have
$$\Gamma(s) P^{-s}=\int_{0}^{\infty} t^{s-1}\left(1-\Pi_{0}\right) e^{-t P} d t, \quad \Re s>0$$
where $\Pi_{0}$ is the orthogonal projection onto the nullspace of $P$. Together with the heat kernel asymptotics (6.6) this implies that, for $\Re s>\frac{n}{m}$,
$$\begin{aligned}
\Gamma(s) K_{P^{-s}}(x, x) & =\int_{0}^{1} t^{s-1} K_{P}(x, x ; t) d t+h(x ; s) \\
& =(4 \pi)^{-\frac{n}{m}} \sum_{0 \leq j<n} \int_{0}^{1} t^{s+\frac{j-n}{m}} a_{j}(P ; x) t^{-1} d t+h(x ; s) \\
& =(4 \pi)^{-\frac{n}{m}} \sum_{0 \leq j<n} \frac{m}{m s+j-n} a_{j}(P ; x)+h(x ; s) \operatorname{Hol}(\Re s>0),
\end{aligned}$$
where $h(x ; s)$ is a general notation for a holomorphic function on the halfspace $\Re s>0$. Thus, for $j=0,1, \ldots, n-1$, we have
$$\Gamma\left(\frac{n-j}{m}\right) \operatorname{Res}_{s=\frac{n-j}{m}} K_{P^{-s}}(x, x)=(4 \pi)^{-\frac{n}{m}} a_{j}(P ; x) .$$
Combining this with (6.5) we arrive at the following result.
Proposition 6.7 (Compare [PR]). Let $k \in m^{-1} \mathbb{N}$ be such that $m k-n \in \mathbb{N}_{0}$. Then, under the above assumptions, we have
$$\gamma_{P^{k}}(x)=(4 \pi)^{-\frac{n}{m}} \frac{m}{\Gamma(k)} a_{n-m k}(P ; x) .$$

The above result provides us with a way to compute the logarithmic singularities of the Green functions of the powers of $P$ from the knowledge of coefficients of the heat kernel asymptotics. For instance, in the case of the Laplace operator combining Theorem 1.8 and Proposition 6.7 gives the following result.

Proposition 6.8. For $k=\frac{n}{2}, \frac{n}{2}-1, \frac{n}{2}-2$ and provided that $k>0$, we have
$$\begin{gathered}
\gamma_{\Delta_{g}^{\frac{n}{2}}}(x)=(4 \pi)^{-\frac{n}{2}} \frac{2}{\Gamma\left(\frac{n}{2}\right)}, \quad \gamma_{\Delta_{g}^{\frac{n}{2}-1}}(x)=(4 \pi)^{-\frac{n}{2}} \frac{2}{\Gamma\left(\frac{n}{2}-1\right)} \cdot \frac{-1}{6} \kappa, \\
\gamma_{\Delta_{g}^{\frac{n}{2}-2}}(x)=(4 \pi)^{-\frac{n}{2}} \frac{2}{\Gamma\left(\frac{n}{2}-2\right)}\left(\frac{1}{180}|R|^{2}-\frac{1}{180}|\operatorname{Ric}|^{2}+\frac{1}{72} \kappa^{2}-\frac{1}{30} \Delta_{g} \kappa\right) .
\end{gathered}$$

\section*{7. Green Functions and Conformal Geometry}

Green functions of the Yamabe operator and other conformal powers of the Laplacian play an important role in conformal geometry. This is illustrated by the solution to the Yamabe problem by Schoen [Sc] or by the work of Okikoliu [Ok] on variation formulas for the zeta-regularized determinant of the Yamabe operator in odd dimension. Furthermore, Parker-Rosenberg [PR] computed the logarithmic singularity of the Green function of the Yamabe operator in even low dimension.

Theorem 7.1 (Parker-Rosenberg [PR, Proposition 4.2]). Let $\left(M^{n}, g\right)$ be a closed Riemannian manifold. Then
\begin{itemize}
\item[(1)] In dimension $n=2$ and $n=4$ we have
$$\gamma_{P_{1, g}}(x)=2(4 \pi)^{-1}(n=2) \quad \text { and } \quad \gamma_{P_{1}}(x)=0(n=4) \text {. }$$
\item[(2)] In dimension $n=6$,
$$\gamma_{P_{1, g}}(x)=(4 \pi)^{-3} \frac{1}{90}|W|^{2},$$
where $|W|^{2}=W^{i j k l} W_{i j k l}$ is the norm-square of the Weyl tensor.
\item[(3)] In dimension $n=8$,
$$\gamma_{P_{1, g}}(x)=(4 \pi)^{-4} \frac{2}{9 \cdot 7!}\left(81 \Phi_{g}+64 W_{i j}{ }^{k l} W^{i j}{ }_{p q} W^{p q}{ }_{k l}+352 W_{i j k l} W_{p}^{i}{ }_{q}{ }_{q} W^{p j q l}\right),$$
where $\Phi_{g}$ is given by (4.4).
\end{itemize}

Remark 7.2. Parker and Rosenberg actually computed the coefficient $a_{\frac{n}{2}-1}\left(P_{1, g} ; x\right)$ of $t^{-1}$ in the heat kernel asymptotics for the Yamabe operator when $M$ is closed. We obtain the above formulas for $\gamma_{P_{1, g}}(x)$ by using (6.7). We also note that Parker and Rosenberg used a different sign convention for the curvature tensor.

The computation of Parker and Rosenberg in [PR] has two main steps. The first step uses the formulas for Gilkey [Gi2, Gi3] for the heat invariants of Laplace type operator, since the Yamabe operator is such an operator. This expresses the coefficient $a_{\frac{n}{2}-1}\left(P_{1, g} ; x\right)$ as a linear combination of Weyl Riemannian invariants. For $n=8$ there are 17 such invariants. The 2nd step consists in rewriting these linear combinations in terms of Weyl conformal invariant, so as to obtain the much simpler formulas above.

It is not clear how to extend Parker-Rosenberg's approach for computing the logarithmic singularities $\gamma_{P_{k, g}}(x)$ of the Green functions of other conformal powers of the Laplacian. This would involve computing the coefficients of the heat kernel asymptotics for all these operators, including conformal fractional powers of the Laplacian in odd dimension.

As the following result shows, somewhat amazingly, in order to compute the $\gamma_{P_{k, g}}(x)$ the sole knowledge of the coefficients heat kernel asymptotics for the Laplace operator is enough.

Theorem 7.3. Let $\left(M^{n}, g\right)$ be a Riemannian manifold and let $k \in \frac{1}{2} \mathbb{N}$ be such that $\frac{n}{2}-k \in \mathbb{N}_{0}$. Then the logarithmic singularity of the Green function of $P_{k, g}$ is given by
$$\gamma_{P_{k, g}}(x)=\frac{2}{\Gamma(k)}(4 \pi)^{-\frac{n}{2}} \tilde{a}_{n-2 k}\left(\Delta_{g} ; x\right),$$
where $\tilde{a}_{n-2 k}\left(\Delta_{g} ; x\right)$ is the local conformal invariant obtained by applying Fefferman-Graham's rule to the heat invariant $a_{n-2 k}\left(\Delta_{g} ; x\right)$ in (1.3).

Remark 7.4. When $n$ is odd the condition $\frac{n}{2}-k \in \mathbb{N}_{0}$ imposes $k$ to be an half-integer, and so in this case $P_{k, g}$ is a conformal fractional powers of the Laplacian.

Using Theorem 7.3 and the knowledge of the heat invariants $a_{2 j}\left(\Delta_{g} ; x\right)$ it becomes straighforward to compute the logarithmic singularities $\gamma_{P k, g}(x)$. In particular, we recover the formulas of Parker-Rosenberg [PR] stated in Theorem 7.1.

Theorem 7.5 ([Po1, Po2]). Let $\left(M^{n}, g\right)$ be a Riemannian manifold of dimension $n \geq 3$. Then
$$\gamma_{P_{\frac{n}{2}, g}}(x)=\frac{2}{\Gamma\left(\frac{n}{2}\right)}(4 \pi)^{-\frac{n}{2}} \quad \text { and } \quad \gamma_{P_{\frac{n}{2}-1, g}}(x)=0 .$$

Proof. We know from Theorem 1.8 that $a_{0}\left(\Delta_{g} ; x\right)=1$ and $a_{2}\left(\Delta_{g} ; x\right)=-\frac{1}{6} \kappa$. Thus $\tilde{a}_{0}\left(\Delta_{g} ; x\right)=1$. Moreover, as $\kappa$ is the trace of Ricci tensor, from Example 4.4(a) we see that $\tilde{a}_{2}\left(\Delta_{g} ; x\right)=0$. Combining this with Theorem 7.3 gives the result. \(\square\)

Remark 7.6. The equality $\gamma_{P_{\frac{n}{2}}}(x)=2 \Gamma\left(\frac{n}{2}\right)^{-1}(4 \pi)^{-\frac{n}{2}}$ can also be obtained by direct computation using (6.3) and the fact that in this case $p_{-n}(x, \xi)$ is the principal symbol of a parametrix for $P_{\frac{n}{2}, g}$. As $P_{\frac{n}{2}, g}$ has same principal symbol as $\Delta_{g}^{\frac{n}{2}}$, the principal symbol of any parametrix for $P_{\frac{n}{2}, g}$ is equal to $|\xi|_{g}^{-n}$, where $|\xi|_{g}^{2}=g^{i j}(x) \xi_{i} \xi_{j}$.

Remark 7.7. The equality $\gamma_{P_{\frac{n}{2}-1, g}}(x)=0$ is obtained in [Po1, Po2] by showing this is a conformal invariant weight 1 and using the fact there is no nonzero conformal invariant of weight 1. Indeed, by Theorem 1.4 any Riemannian invariant of weight 1 is a scalar multiple of the scalar curvature, but the scalar curvature is not a conformal invariant. Therefore, any local conformal of weight 1 must be zero.

Theorem 7.8. Let $\left(M^{n}, g\right)$ be a Riemannian manifold of dimension $n \geq 5$. Then
$$\gamma_{P_{\frac{n}{2}-2}}(x)=\frac{(4 \pi)^{-\frac{n}{2}}}{\Gamma\left(\frac{n}{2}-2\right)} \cdot \frac{1}{90}|W|^{2} .$$

Proof. By Theorem 1.8 we have
$$a_{4}\left(\Delta_{g} ; x\right)=\frac{1}{180}|R|^{2}-\frac{1}{180}|\operatorname{Ric}|^{2}+\frac{1}{72} \kappa^{2}-\frac{1}{30} \Delta_{g} \kappa .$$
As Example 4.4 (b) shows, the Weyl conformal invariant associated to $|R|^{2}$ by Fefferman-Graham's rule is $|W|^{2}$. Moreover, as $|\operatorname{Ric}|^{2}, \kappa^{2}$, and $\Delta_{g} \kappa$ involve the Ricci tensor, the corresponding Weyl conformal invariants are equal to 0. Thus,
$$\tilde{a}_{4}\left(\Delta_{g} ; x\right)=\frac{1}{180}|W|^{2} .$$
Applying Theorem 7.3 then completes the proof. \(\square\)

Theorem 7.9. Let $\left(M^{n}, g\right)$ be a Riemannian manifold of dimension $n \geq 7$. Then
$$\gamma_{P_{\frac{n}{2}-3}}(x)=\frac{(4 \pi)^{-\frac{n}{2}}}{\Gamma\left(\frac{n}{2}-3\right)} \cdot \frac{2}{9 \cdot 7!}\left(81 \Phi_{g}+64 W_{i j}{ }^{k l} W^{i j}{ }_{p q} W^{p q}{ }_{k l}+352 W_{i j k l} W_{p}^{i}{ }_{q}{ }_{q} W^{p j q l}\right),$$
where $\Phi_{g}(x)$ is given by (4.4).
Proof. Thanks to Theorem 1.8 we know that
$$a_{6}\left(\Delta_{g} ; x\right)=\frac{1}{9 \cdot 7!}\left(81|\nabla R|^{2}+64 R_{i j}{ }^{k l} R^{i j}{ }_{p q} R^{p q}{ }_{k l}+352 R_{i j k l} R_{p}^{i}{ }_{q}{ }_{q} R^{p j q l}\right)+I_{g, 0}^{(3)}(x),$$
where $I_{g, 0}^{(3)}(x)$ is a linear combination of Weyl Riemannian invariants involving the Ricci tensor. Thus $\tilde{a}_{6}\left(\Delta_{g} ; x\right)=0$ by Example 4.4.(a). By Example 4.4.(b), the Weyl conformal invariants corresponding to $R_{i j}{ }^{k l} R_{k l}{ }^{p q} R_{p q}{ }^{i j}$ and $R_{j k}^{i}{ }^{q} R_{i}{ }^{p k}{ }_{l} R_{j}{ }^{p l}{ }_{q}$ are $W_{i j}{ }^{k l} W_{k l}{ }^{p q} W_{p q}{ }^{i j}$ and $W_{j k}^{i}{ }^{q} W_{i}{ }^{p k}{ }_{l} W_{j}{ }^{p l}{ }_{q}$ respectively. Moreover, by Example 4.4.(c) applying Fefferman-Graham's rule to $|\nabla R|^{2}$ yields the conformal invariant $\Phi_{g}$ given by (4.4). Thus,
$$\tilde{a}_{6}\left(\Delta_{g} ; x\right)=\frac{1}{9 \cdot 7!}\left(81 \Phi_{g}+64 W_{i j}{ }^{k l} W^{i j}{ }_{p q} W^{p q}{ }_{k l}+352 W_{i j k l} W_{p}^{i}{ }_{q}{ }_{q} W^{p j q l}\right) .$$
Combining this with Theorem 7.3 proves the result. \(\square\)

Remark 7.10. In the case of Yamabe operator (i.e., $k=1$ ) the above results give back the results of Parker-Rosenberg [PR] as stated in Theorem 7.1.

Let us present some applications of the above results. Recall that a Riemannian manifold $\left(M^{n}, g\right)$ is said to be locally conformally flat when it is locally conformally equivalent to the flat Euclidean space $\mathbb{R}^{n}$. As is well known, in dimension $n \geq 4$, local conformal flatness is equivalent to the vanishing of the Weyl tensor. Therefore, as an immediate consequence of Theorem 7.8 we obtain the following result.

Theorem 7.11. Let $\left(M^{n}, g\right)$ be a Riemannian manifold of dimension $n \geq 5$. Then the following are equivalent:
\begin{itemize}
\item[(1)] $\left(M^{n}, g\right)$ is locally conformally flat.
\item[(2)] The logarithmic singularity $\gamma_{P_{\frac{n}{2}-2}, g}(x)$ vanishes identically on $M$.
\end{itemize}

Remark 7.12. A well known conjecture of Radamanov [Ra] asserts that, for a strictly pseudoconvex domain $\Omega \subset \mathbb{C}^{n}$, the vanishing of the logarithmic singularity of the Bergman kernel is equivalent to $\Omega$ being biholomorphically equivalent to the unit ball $\mathbb{B}^{2 n} \subset \mathbb{C}^{n}$. Therefore, we may see Theorem 7.11 as an analogue of Radamanov conjecture in conformal geometry in terms of Green functions of conformal powers of the Laplacian.

In the compact case, we actually obtain a spectral theoretic characterization of the conformal class of the round sphere as follows.
Theorem 7.13. Let $\left(M^{n}, g\right)$ be a compact simply connected Riemannian manifold of dimension $n \geq 5$. Then the following are equivalent:
\begin{itemize}
\item[(1)] $\left(M^{n}, g\right)$ is conformally equivalent to the round sphere $\mathbb{S}^{n}$.
\item[(2)] $\int_{M} \gamma_{P_{\frac{n}{2}-2}, g}(x) v_{g}(x)=0$.
\item[(3)] $\operatorname{Res}_{s=1} \operatorname{Tr}\left[\left(P_{\frac{n}{2}-2}\right)^{-s}\right]=0$.
\end{itemize}

Proof. The equivalence between (2) and (3) is a consequence of (6.4). By Theorem 7.8, we have
$$\int_{M} \gamma_{P_{\frac{n}{2}-2}, g}(x) v_{g}(x)=\frac{(4 \pi)^{-\frac{n}{2}}}{\Gamma\left(\frac{n}{2}-2\right)} \cdot \frac{1}{90} \int_{M}|W(x)|^{2} v_{g}(x) .$$
As $|W(x)|^{2} \geq 0$ we see that $\int_{M} \gamma_{P_{\frac{n}{2}-2}, g}(x) v_{g}(x)=0$ if and only if $W(x)=0$ identically on $M$. As $M$ is compact and simply connected, a well known result of Kuiper [Ku] asserts that the vanishing of Weyl tensor is equivalent to the existence of a conformal diffeomorphism from $(M, g)$ onto the round sphere $\mathbb{S}^{n}$. Thus (1) and (2) are equivalent. The proof is complete. \(\square\)

\section*{8. Proof of Theorem 7.3}

In this section, we outline the proof of Theorem 7.3. The strategy of the proof is divided into 9 main steps.
Step 1. Let $k \in \frac{1}{2} \mathbb{N}$ be such that $n-2 k \in \mathbb{N}_{0}$. Then $\gamma_{\Delta_{g}^{k}}(x)=2 \Gamma(k)^{-1}(4 \pi)^{-\frac{n}{2}} a_{n-2 k}\left(\Delta_{g} ; x\right)$.
This follows from Proposition 6.7. This is the Riemannian version of Theorem 7.3 and the main impetus for that result.
Step 2. Let $k \in \frac{1}{2} \mathbb{N}$ be such that $n-2 k \in \mathbb{N}_{0}$. Then $\gamma_{P_{k, g}}(x)$ is a linear combination of Weyl conformal invariants of weight $n-2 k$.

This step is carried out in Po1, Po2. This is a general result for the logarithmic singularities of the Green functions of conformally invariant $\Psi$ DOs. For the Yamabe operator, the transformation of $\gamma_{P_{k, g}}(x)$ under conformal change of metrics was observed by Parker-Rosenberg [PR]. Their argument extends to general conformally invariant operators.
Step 3. Let $I_{g}(x)$ be a local Riemannian invariant of any weight $w \in 2 \mathbb{N}_{0}$ if $n$ is odd or of weight $w \leq n$ if $n$ is even. If $(M, g)$ is Ricci-flat, then
$$I_{g}(x)=\tilde{I}_{g}(x) \quad \text { on } M,$$
where $\tilde{I}_{g}(x)$ is the local conformal invariant associted to $I_{g}(x)$ by Fefferman-Graham's rule.
This results seems to be new. It uses the fact that if $(M, g)$ is Ricci flat, then by Example 3.4 the ambient metric is given by
$$\tilde{g}=2 \rho(d t)^{2}+t^{2} g_{i j}(x)+2 t d t d \rho .$$

Step 4. Theorem 7.3 holds when $\left(M^{n}, g\right)$ is Ricci-flat.
If $(M, g)$ is Ricci-flat, then it follows from Example 3.12 and Example 5.15 that $P_{k, g}=\Delta_{g}^{k}$, and hence $\gamma_{P_{k, g}}(x)=\gamma_{\Delta_{g}^{k}}(x)$. Combining this with Step 1 and Step 3 then gives
$$\gamma_{P_{k, g}}(x)=\gamma_{\Delta_{g}^{k}}(x)=2 \Gamma(k)^{-1}(4 \pi)^{-\frac{n}{2}} a_{n-2 k}\left(\Delta_{g} ; x\right)=2 \Gamma(k)^{-1}(4 \pi)^{-\frac{n}{2}} \tilde{a}_{n-2 k}\left(\Delta_{g} ; x\right) .$$
This proves Step 4.
In order to prove Theorem 7.3 for general Riemannian metrics we actually need to establish pointwise versions of Step 4 and Step 3. This is the purpose of the next three steps.

Step 5. Let $I_{g}(x)=\operatorname{Contr}_{g}\left(\nabla^{k_{1}} R \otimes \cdots \otimes \nabla^{k_{l}} R\right)$ be a Weyl Riemannian invariant of weight $<n$ and assume that $\operatorname{Ric}(g)=\mathrm{O}\left(\left|x-x_{0}\right|^{n-2}\right)$ near a point $x_{0} \in M$. Then $\tilde{I}_{g}(x)=I_{g}(x)$ at $x=x_{0}$.

This step follows the properties of the ambient metric and complete metric contractions of ambient curvature tensors described in [FG3].

Step 6. Let $k \in \frac{1}{2} \mathbb{N}$ be such that $n-2 k \in 2 \mathbb{N}_{0}$ and assume that $\operatorname{Ric}(g)=\mathrm{O}\left(\left|x-x_{0}\right|^{n-2}\right)$ near a point $x_{0} \in M$. Then $\gamma_{P_{k, g}}(x)=\gamma_{\Delta_{g}^{k}}(x)$ at $x=x_{0}$.

If $P$ is an elliptic $\Psi \mathrm{DO}$, then (6.3) gives an expression in local coordinates for $\gamma_{P}(x)$ in terms of the symbol of degree $-n$ of a parametrix for $P$. The construction of the symbol of a parametrix shows that this symbol is a polynomial in terms of inverse of the principal symbol of $P$ and partial derivatives of its other homogeneous symbols. It then follows that if $P$ is Riemannian invariant, then $\gamma_{P}(x)$ is of the form (1.4), that is, this is a Riemannian invariant (see Po1, Po2 ).

Moreover, it follows from the ambient metric construction of the GJMS operator [GJMS, FG3] that, when $k$ is an integer, $P_{k, g}$ and $\Delta_{g}^{k}$ differs by a differential operator whose coefficients are polynomials in the covariant derivatives of order $<n-2$ of the Ricci tensor. As a result $\gamma_{P k, g}(x)$ and $\gamma_{\Delta_{g}^{k}}(x)$ differ by a linear combination of complete metric contraction of tensor powers of covariant derivatives of the Ricci tensor. Thus $\gamma_{P_{k, g}}(x)$ and $\gamma_{\Delta_{g}^{k}}(x)$ agree at $x=x_{0}$ if $\operatorname{Ric}(g)$ vanishes at order $<n-2$ near $x_{0}$. This is also true for the conformal fractional powers of the Laplacian thanks to the properties of the scattering matrix for Poincaré-Einstein metric in [JS] and [GZ].
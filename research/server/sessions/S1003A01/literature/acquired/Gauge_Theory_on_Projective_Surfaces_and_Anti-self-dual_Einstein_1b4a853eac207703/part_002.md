---
retention_scope: session
part: 2
total_parts: 2
---

[Part 2/2 of: Gauge Theory on Projective Surfaces and Anti-self-dual Einstein Metrics in Dimension Four]

\footnotetext{
${ }^{5}$ In [19] (see also [6, 23, 24] for other applications of this lift) it was proven that a 'similar' metric
$$g=d \xi_{i} \odot d x^{i}-\Pi_{i j}^{k} \xi_{k} d x^{i} \odot d x^{j}$$
constructed out of the Thomas symbols $\Pi_{i j}^{k}=\Gamma_{i j}^{k}-\frac{1}{3} \Gamma_{i l}^{l} \delta_{j}^{k}-\frac{1}{3} \Gamma_{j l}^{l} \delta_{i}^{k}$ is anti-self-dual and null-Kähler (with ASD null-Kähler two-form) for any choice of $\Gamma_{i j}^{k}$. The Patterson-Walker lift (2.10) is conformally equivalent (up to a diffeomorphism) to the projective Patterson-Walker lift (5.6) only if $\Gamma_{i j}^{j}=\nabla_{i} F$ for some function $F$ on $N$.
}
so that
$$A_{i}=\left(\mathrm{P}_{i j}+\xi_{i} \xi_{j}-\Gamma_{i j}^{k} \xi_{k}\right) \frac{\partial}{\partial \xi_{j}}$$
The Calderbank equations are solved by the Higgs pair
$$\phi_{i}=\epsilon_{i j} \frac{\partial}{\partial \xi_{j}} .$$
Let $M$ be a complement of a projective line in the total space of the bundle $\mathbb{P}(E)$. The corresponding contravariant metric on $M$ is constructed by demanding that the leaves of the rank-2 distribution (5.4) $D \subset T\left(M \times \mathbb{R} \mathbb{P}^{1}\right)$ project down to self-dual two-surfaces on $M$. This gives $\epsilon^{i j}\left(\partial / \partial x^{i}-A_{i}\right) \odot \phi_{j}$, or, in the covariant form,
$$g=\left(d \xi_{i}-\left(\Gamma_{i j}^{k} \xi_{k}-\xi_{i} \xi_{j}-\mathrm{P}_{j i}\right) d x^{j}\right) \odot d x^{i},$$
so that we have recovered the metric of the bi-Lagrangian structure (3.10).
Theorem 5.1. Formula (5.9) defines a metric which does not depend on a choice of a connection in a projective class.

Proof. If we change the connection in the projective class using (2.2) then the Schouten tensor changes by (2.3). To establish the invariance of (5.9) we translate the fibre coordinates according to
$$\hat{\xi}_{i}=\xi_{i}+\Upsilon_{i}$$
in agreement with (5.8). Then
$$\begin{aligned}
& \left(d \hat{\xi}_{i}-\left(\hat{\Gamma}_{i j}^{k} \hat{\xi}_{k}-\hat{\xi}_{i} \hat{\xi}_{j}-\hat{\mathrm{P}}_{j i}\right) d x^{j}\right) \odot d x^{i}=d \xi_{i} \odot d x^{i}+ \\
& \left(\xi_{(j} \Upsilon_{i)}-\Gamma_{i j}^{k} \xi_{k}-\xi_{i} \Upsilon_{j}-\xi_{j} \Upsilon_{i}-\Gamma_{i j}^{k} \Upsilon_{k}-2 \Upsilon_{i} \Upsilon_{j}+\xi_{i} \xi_{j}+\xi_{i} \Upsilon_{j}+\xi_{j} \Upsilon_{i}+\Upsilon_{i} \Upsilon_{j}\right. \\
& \left.+\mathrm{P}_{j i}-\nabla_{(j} \Upsilon_{i)}+\Upsilon_{i} \Upsilon_{j}\right) d x^{i} \odot d x^{j} \\
& =\left(d \xi_{i}-\left(\Gamma_{i j}^{k} \xi_{k}-\xi_{i} \xi_{j}-\mathrm{P}_{j i}\right) d x^{j}\right) \odot d x^{j}
\end{aligned}$$ \(\square\)

The metric is anti-self-dual, and Einstein with scalar curvature equal to 24 . The anti-self-duality is a consequence of the fact that the connection $A$ and the Higgs field $\phi_{i} \pi^{i}$ satisfy the Calderbank equations [7].

\section*{6. Examples}
6.1. Homogeneous model $M=\operatorname{SL}(3, \mathbb{R}) \backslash \operatorname{GL}(2, \mathbb{R})$. Consider the flat projective structure on $(N=$ $\left.\mathbb{R P}^{2},[\nabla]\right)$, and choose $\Gamma_{i j}{ }^{k}=0$. The resulting four manifold is the complement of an $\mathbb{R} \mathbb{P}^{1}$ sub-bundle in the projective cotractor bundle of $\mathbb{R} \mathbb{P}^{2}$ which can be identified with with $M=\operatorname{SL}(3, \mathbb{R}) \backslash \operatorname{GL}(2, \mathbb{R})$. We shall establish this result in arbitrary dimension. Consider $N=\mathbb{R P}^{n}$, with its flat projective structure, and an $\operatorname{SL}(n+1)$ action on the projective cotractor bundle $\mathbb{P}(E)$ minus the diagonal
$$\operatorname{SL}(n+1): \mathbb{R}^{n+1} \times \mathbb{R}_{n+1} \backslash \Delta \longrightarrow \mathbb{R}^{n+1} \times \mathbb{R}_{n+1} \backslash \Delta$$
where the 'diagonal' $\Delta$ consists of all incident pairs of vectors $[v] \in \mathbb{R}^{n+1}$ and forms $[f] \in \mathbb{R}_{n+1}$ s.t. the corresponding point $v \in \mathbb{R P}^{n}$ belongs to the hyperplane $f \in \mathbb{R P}_{n}$. This action is simply
$(v, f) \rightarrow\left(A v, f A^{-1}\right)$. It is transitive, and clearly a subgroup stabilising a pair (point, hyperplane) is $\operatorname{GL}(n)$ which sits in $\operatorname{SL}(n+1)$ as a lower diagonal block.

To finish the proof we need to argue that $\mathbb{R}^{n+1} \times \mathbb{R}_{n+1} \backslash \Delta$ projects down to a complement of an $\mathbb{R P}_{n-1}$ sub-bundle in $\mathbb{P}(E)$. This sub-bundle is just $\mathbb{P}\left(T^{*} N\right)$ and it has an injection into $\mathbb{P}(E)$ given by $f \rightarrow(0, f)$. A point in $N$ with homogeneous coordinates $[1,0, \ldots, 0]$ (corresponding to our choice of an affine chart) is not incident with any cotractor in $\mathbb{P}(E) / \mathbb{R} \mathbb{P}_{n-1}$, so removing a diagonal is equivalent to looking at the complement of this sub-bundle.

The Einstein metric (5.9) on this manifold admits a Kerr-Schild form
$$g=d \xi_{i} \odot d x^{i}+\Lambda\left(\xi_{j} d x^{j}\right)^{2}$$
with eight dimensional isometry group $\operatorname{SL}(3, \mathbb{R})$ [12] in agreement with Theorem 3.10). This metric is a neutral signature analog of the Fubini-Study metric on $\mathbb{C P}^{2}$. Both metrics arise as different real forms of $\operatorname{SL}(3, \mathbb{C}) / \operatorname{GL}(2, \mathbb{C})$. The limit $\Lambda=0$ in (6.1) gives the flat metric.
6.2. Ricci-flat limits. Motivated by the previous example let us now consider the general case of projective structures which admit a connection with skew-symmetric Schouten tensor. In this case one can always choose local coordinates on $N$ and a connection $\nabla \in[\nabla]$ such that [45]
$$\Gamma_{11}^{1}=-\frac{\partial f}{\partial x^{1}}, \quad \Gamma_{22}^{2}=\frac{\partial f}{\partial x^{2}},$$
where $f: N \longrightarrow \mathbb{R}$ is an arbitrary function, and all other components of ∇ vanish ${ }^{6}$. In this case
$$\mathrm{P}=\frac{1}{3} \frac{\partial^{2} f}{\partial x^{1} \partial x^{2}} d x^{1} \wedge d x^{2},$$
and the metric is given by
$$g=d \xi_{i} \odot d x^{i}+\xi_{1} \frac{\partial f}{\partial x^{1}}\left(d x^{1}\right)^{2}-\xi_{2} \frac{\partial f}{\partial x^{2}}\left(d x^{2}\right)^{2}+\Lambda\left(\xi_{j} d x^{j}\right)^{2} .$$
Setting $\Lambda=0$ gives an ASD Ricci-flat metric which has a form of the Patterson-Walker lift (2.10) and has appeared in the work of Derdzinski [14].
6.3. Cohomogeneity-one examples. The dimension of the Lie algebra $\mathfrak{g}$ of projective vector fields for a given projective structure on a surface $N$ can be 8, 3, 2, 1 or 0 (see [30], and also [39, 5, 17]). If the dimension is maximal and equal to 8 then $\mathfrak{g}=\mathfrak{s l}(3, \mathbb{R})$, and the projective structure is flat. We have shown that in this case the resulting metric (1.1) is given by (6.1), and admits 8 Killing vectors in agreement with Theorem 3.10. We shall now consider the submaximal case, where $\mathfrak{g}=\mathfrak{s l}(2, \mathbb{R})$. There are two one-parameter families of non-flat projective structures with this symmetry. Their unparametrised geodesics are integral curves of a second order ODE
$$y^{\prime \prime}=c\left(x y^{\prime}-y\right)^{3},$$
where $c \neq 0$. We compare this to the general second order ODE defining a projective structure (see e.g. [6])
$$y^{\prime \prime}=\Gamma_{22}^{1}\left(y^{\prime}\right)^{3}+\left(2 \Gamma_{12}^{1}-\Gamma_{22}^{2}\right)\left(y^{\prime}\right)^{2}+\left(\Gamma_{11}^{1}-2 \Gamma_{12}^{2}\right) y^{\prime}-\Gamma_{11}^{2},$$

\footnotetext{
${ }^{6}$ An alternative characterisation of the corresponding projective structures is that they arise from second-order ODEs point equivalent to derivatives of first order ODEs [18]. These projective structures where further characterised in [38] and [27].
}
and chose the representative connection ∇ by
$$\Gamma_{11}^{1}=-\Gamma_{12}^{2}=-\Gamma_{21}^{2}=c x y^{2}, \quad \Gamma_{22}^{2}=-\Gamma_{21}^{1}=-\Gamma_{12}^{1}=c x^{2} y, \quad \Gamma_{22}^{1}=c x^{3}, \quad \Gamma_{11}^{2}=c y^{3} .$$
The corresponding ASD Einstein metric (1.1) is
$$g=d \xi_{i} \odot d x^{i}+\Lambda\left(\xi_{i} d x^{i}\right)^{2}+\frac{4 c}{\Lambda}\left(x^{2} d x^{1}-x^{1} d x^{2}\right)^{2}-\Gamma_{i j}^{k} d x^{i} \odot d x^{j},$$
where $x^{i}=(x, y)$. This metric admits a three-dimensional isometry group $S L(2, \mathbb{R})$ generated by left-invariant vector fields $K_{\alpha}, \alpha=1,2,3$ given by
$$K_{1}=x^{1} \frac{\partial}{\partial x^{1}}-x^{2} \frac{\partial}{\partial x^{2}}-\xi_{1} \frac{\partial}{\partial \xi_{1}}+\xi_{2} \frac{\partial}{\partial \xi_{2}}, \quad K_{2}=2 x^{1} \frac{\partial}{\partial x^{2}}-2 \xi_{2} \frac{\partial}{\partial \xi_{1}}, \quad K_{3}=2 \xi_{1} \frac{\partial}{\partial \xi_{2}}-2 x^{2} \frac{\partial}{\partial x^{1}},$$
and acting on $M=\mathbb{R} \times S L(2, \mathbb{R})$ with three-dimensional orbits. We shall use an invariant coordinate $r$ given by $r^{2} \equiv\left(x^{1} \xi_{1}+x^{2} \xi_{2}\right)$ which is constant on the orbits. Let $\sigma^{\alpha}$ be right-invariant one-forms on $S L(2, \mathbb{R})$ such that
$$\mathcal{L}_{K_{\alpha}} \sigma^{\beta}=0, \quad \forall \alpha, \beta, \quad \text { and } \quad d \sigma^{1}+2 \sigma^{2} \wedge \sigma^{3}=0, \quad d \sigma^{2}+\sigma^{2} \wedge \sigma^{1}=0, \quad d \sigma^{3}-\sigma^{3} \wedge \sigma^{1}=0 .$$
There is some freedom, measured by functions of $r$, in choosing these one-forms. If we chose $\Lambda<0$, and take
$$\sigma^{1}=\frac{\xi_{i} d x^{i}-x^{i} d \xi_{i}}{r^{2}}+\frac{2 \Lambda r d r}{\Lambda r^{2}-1}, \quad \sigma^{2}=\frac{\Lambda r^{2}-1}{r^{2}}\left(x^{1} d x^{2}-x^{2} d x^{1}\right), \quad \sigma^{3}=\frac{\xi_{1} d \xi_{2}-\xi_{2} d \xi_{1}}{r^{2}\left(\Lambda r^{2}-1\right)}$$
then the metric (6.4) takes the form
$$g=\frac{d r^{2}}{1-\Lambda r^{2}}-\frac{1}{4} r^{2}\left(1-\Lambda r^{2}\right)\left(\sigma^{1}\right)^{2}-\frac{c}{\Lambda} \frac{\left(\Lambda r^{2}-4\right) r^{4}}{\left(\Lambda r^{2}-1\right)^{2}}\left(\sigma^{2}\right)^{2}+r^{2} \sigma^{2} \odot \sigma^{3}, \quad \Lambda<0 .$$
Note that (6.5) is non-diagonal in the basis defined by the right-invariant one-form on $S L(2, \mathbb{R})$. This is only possible in neutral signature: All cohomogeneity one Einstein metrics in Riemannian signature can be diagonalised [20].

The metric (6.5) appears to be singular when $r=0$, but calculating the invariant norm of the Weyl curvature we find $|C|^{2}=96 \Lambda^{2}$, which is regular. In fact near $r=0$ the metric (6.5) approaches the space of constant curvature which is a neutral signature analogue of the hyperbolic space. To exhibit this space in a standard form we neglect the small terms involving $r^{4}$, and set $r=2 R /\left(1+\Lambda R^{2}\right)$. Then, near $R=0$, the metric (6.5) becomes
$$g \sim \frac{4}{\left(1+\Lambda R^{2}\right)^{2}}\left(d R^{2}-\frac{R^{2}}{4}\left(\left(\sigma^{1}\right)^{2}-4 \sigma^{2} \odot \sigma^{3}\right)\right) .$$
To this end, we note a curious Ricci-flat limit of (6.5). Setting $c=m \Lambda$, and taking the limit $\Lambda \rightarrow 0$ yields a Ricci-flat metric with 9-dimensional group of conformal isometries
$$g=d \xi_{i} \odot d x^{i}+4 m\left(x^{2} d x^{1}-x^{1} d x^{2}\right)^{2} .$$
This is a submaximal metric of neutral signature [12, 28]: if the dimension of the conformal isometry algebra $\mathfrak{g}$ exceeds 9 , then $\mathfrak{g}=\mathfrak{s} \mathfrak{l}(4, \mathbb{R})$, and the metric is conformally flat.

\section*{Appendix A. The construction for higher dimensions}

Of course, the definition of a projective structure makes sense in higher dimensions as well and hence it is natural to ask if the construction described in the main body of this article carries over to higher dimensions. Here we briefly show that this is indeed the case.

As usual, let $\operatorname{PGL}(n+1, \mathbb{R})$ denote the quotient of the general linear group $\operatorname{GL}(n+1, \mathbb{R})$ by its center $Z$, so that
$$\operatorname{PGL}(n+1, \mathbb{R}) \simeq\left\{\begin{array}{cl}
\operatorname{SL}(n+1, \mathbb{R}) & n \text { even, } \\
\operatorname{SL}_{ \pm}(n+1, \mathbb{R}) /\left\{ \pm \mathrm{I}_{n+1}\right\} & n \text { odd, }
\end{array}\right.$$
where $\operatorname{SL}_{ \pm}(n+1, \mathbb{R})$ denotes the group of real ( $n+1$ )-by- $(n+1)$ matrices with determinant ±1.
The projective linear group acts from the left on $\mathbb{R P}^{n}=\left(\mathbb{R}^{n+1} \backslash\{0\}\right) / \mathbb{R}^{*}$ by matrix multiplication. The stabiliser subgroup of the line spanned by ${ }^{t}(10 \ldots 0)$ will be denoted by $G \subset \operatorname{PGL}(n+1, \mathbb{R})$. The elements of $G$ are matrices of the form
$$\left(\begin{array}{cc}
\operatorname{det} a^{-1} & b \\
0 & a
\end{array}\right)$$
for $n$ even and
$$\left[\begin{array}{cc} 
\pm \operatorname{det} a^{-1} & b \\
0 & a
\end{array}\right]$$
for $n$ odd, where $b \in \mathbb{R}_{n}$ and $a \in \mathrm{GL}(n, \mathbb{R})$. Here, the square brackets indicate that the matrix is only well defined up to an overall sign.

Cartan's construction carries over to higher dimensions so that we canonically obtain a Cartan geometry $\left(\pi: P_{[\nabla]} \rightarrow N, \theta\right)$ of type $(\operatorname{PGL}(n+1, \mathbb{R}), G)$ for every projective structure [D] on a smooth $n$-manifold $N$. Again, we write
$$\theta=\left(\begin{array}{cc}
-\operatorname{tr} \phi & \eta \\
\omega & \phi
\end{array}\right)$$
for an $\mathbb{R}_{n}$-valued 1-form $\eta$, an $\mathbb{R}^{n}$-valued 1-form $\omega$ and a $\mathfrak{g l}(n, \mathbb{R})$-valued 1-form $\phi$. The curvature 2-form $\Theta$ satisfies
$$\Theta=d \theta+\theta \wedge \theta=\left(\begin{array}{cc}
0 & L(\omega \wedge \omega) \\
0 & W(\omega \wedge \omega)
\end{array}\right),$$
for smooth curvature functions
$$L: P_{[\nabla]} \rightarrow \operatorname{Hom}\left(\mathbb{R}^{n} \wedge \mathbb{R}^{n}, \mathbb{R}_{n}\right)$$
and
$$W: P_{[\nabla]} \rightarrow \operatorname{Hom}\left(\mathbb{R}^{n} \wedge \mathbb{R}^{n}, \mathbb{R}_{n} \otimes \mathbb{R}^{n}\right) .$$
Note that the function $W$ represents the Weyl projective curvature tensor of $(N,[\nabla])$ and that we have the Bianchi-identity
$$d \Theta=\Theta \wedge \theta-\theta \wedge \Theta,$$
the algebraic part of which reads
$$0=L(\omega \wedge \omega) \wedge \omega \quad \text { and } \quad 0=W(\omega \wedge \omega) \wedge \omega .$$
We have a Lie group embedding defined by
$$\chi: \operatorname{GL}(n, \mathbb{R}) \rightarrow G, \quad a \mapsto\left(\begin{array}{cc}
\operatorname{det} a^{-1} & 0 \\
0 & a
\end{array}\right),$$
for $n$ even and defined by
$$\chi: \mathrm{GL}(n, \mathbb{R}) \rightarrow G, \quad a \mapsto\left[\begin{array}{cc}
\left|\operatorname{det} a^{-1}\right| & 0 \\
0 & a
\end{array}\right],$$
for $n$ odd.
Recall that $\theta$ satisfies the equivariance property
$$R_{g}^{*} \theta=\operatorname{Ad}\left(g^{-1}\right) \circ \theta,$$
for all $g \in G$, where Ad denotes the adjoint representation of $G$. Identifying $\operatorname{GL}(n, \mathbb{R})$ with its image under $\chi$, the equivariance property of $\theta$ implies that the tensor field $\eta \omega:=\eta_{i} \otimes \omega^{i}$ is invariant under the $\operatorname{GL}(n, \mathbb{R})$ right action. Furthermore, since $\omega$ and $\eta$ are both semi-basic for the quotient projection $P_{[\nabla]} \rightarrow P_{[\nabla]} / \operatorname{GL}(n, \mathbb{R})$, it follows that the smooth $2 n$-manifold $M=P_{[\nabla]} / \operatorname{GL}(n, \mathbb{R})$ carries a unique signature $(n, n)$ metric $g$ and a unique non-degenerate 2-form $\Omega$ having the property that $g$ pulls back to $P_{[\nabla]}$ to be the symmetric part of $\eta \omega$ and $\Omega$ pulls back to $P_{[\nabla]}$ to be the anti-symmetric part of $\eta \omega$. Moreover, we compute
$$\begin{aligned}
0= & d(\eta \wedge \omega)=d \eta \wedge \omega-\eta \wedge d \omega=[-\eta \wedge(\phi+\operatorname{Id} \operatorname{tr} \phi)+L(\omega \wedge \omega)] \wedge \omega \\
& -\eta \wedge[-(\phi+\operatorname{Id} \operatorname{tr} \phi) \wedge \omega] \\
= & L(\omega \wedge \omega) \wedge \omega,
\end{aligned}$$
where we used (A.1). It follows that $\Omega$ is symplectic.
We leave it to the interested reader to check that the pair $(g, \Omega)$ defines again a bi-Lagrangian structure on $M$ whose symmetry vector fields are in one-to-one correspondence with the symmetry vector fields of $(N,[\nabla])$. Moreover, we may introduce local coordinates on $M$ so that $g$ and $\Omega$ take the form (3.10). In particular, the metric $g$ is still Einstein with non-zero scalar curvature, as can be verified by direct computation.

\section*{References}
\begin{itemize}
\item[] [1] Atiyah, M. F. (1970) Vector fields on manifolds. Arbeitsgemeinschaft für Forschung des Landes Nordrhein Westfalen 200 , 7-24. 16
\item[] [2] Bailey, T. N., Eastwood, M. G. and Gover, A. R. (1994) Thomas's structure bundle for conformal, projective and related structures. Rocky Mountain J. Math. 24, 1191-1217. 3, 5, 19
\item[] [3] Brozos-Vazquez, M., Garcia-Rio, E., Gilkey, P., Nikcevic, S. and Vazquez-Lorenzo, R. (2009) The Geometry of Walker Manifolds. Synthesis Lectures on Mathematics and Statistics. Morgan and Claypool. 14, 18
\item[] [4] Bryant, R. L. (2001) Bochner-Kähler metrics. J. Amer. Math. Soc. 14, 623-715. 9
\item[] [5] Bryant, R. L., Manno, G. and Matveev, V. (2008) A solution of a problem of Sophus Lie: normal forms of two-dimensional metrics admitting two projective vector fields. Math. Ann. 340, 437. 21
\item[] [6] Bryant, R. L., Dunajski, M., and Eastwood, M. G. (2009) Metrisability of two-dimensional projective structures, J. Differential Geometry 83, 465-499. 19, 21
\item[] [7] Calderbank, D. M. J. (2014) Selfdual 4-manifolds, projective structures, and the Dunajski-West construction. SIGMA 10, 034. 2, 17, 18, 20
\item[] [8] Calderbank, D. M. J. (2014) Integrable Backround Geometries. SIGMA 10, 035. 17
\item[] [9] Čap, A. and Slovák, J. (2009) Parabolic Geometries I: Background and General Theory, American Mathematical Society 2009. 12
\item[] [10] Cartan, E. (1924) Sur les variétés a connexion projective. Bull. Soc. Math. France. 52, 205-241. 4
\item[] [11] Calvino-Louzao, E., García-Río, E., Gilkey, P. and Vazquez-Lorenzo, R. (2009) The geometry of modified Riemannian extensions. Proceedings of the Royal Society A465. 2, 14
\item[] [12] Casey, S., Dunajski, M. and Tod, K. P. (2013) Twistor geometry of a pair of second order ODEs Comm. Math. Phys. 321, 681-701. 21, 22
\end{itemize}
[13] Chudecki, A. and Przanowski, M. (2008) From hyperheavenly spaces to Walker and Osserman spaces: I Class.Quant.Grav. 25 145010. 14
[14] Derdziński, A. (2008) Connections with skew-symmetric Ricci tensor on surfaces. Results Math. 52, 223-245. 2, 15, 21
[15] Derdziński, A (2009) Non-Walker Self-Dual Neutral Einstein Four-Manifolds of Petrov Type III Journal of Geometric Analysis, 19 301-357 2
[16] Díaz-Ramos, J. C. and García-Río, E. and Vázquez-Lorenzo, R. (2006) Four-dimensional Osserman metrics with nondiagonalizable Jacobi operators. J. Geom. Anal. 16 39-52. 2
[17] Dumitriescu, S. and Gulliot, A. (2013) Quasihomogeneous analytic affine connections on surfaces. J. Topol. Anal. 5491. 21
[18] Dunajski, M., and West, S. (2007) Anti-self-dual conformal structures from projective structures. Comm. Math. Phys. 272, 85-118. 18, 21
[19] Dunajski, M. and Tod, K. P. (2010) Four Dimensional Metrics Conformal to Kähler, Math. Proc. Camb. Phil. Soc. 148, 485-503. 19
[20] Dunajski, M. and Tod, K. P. (2017) Non-diagonal four-dimensional cohomogeneity-one Einstein metrics in various signatures. Diff. Geom. Appl in press. arXiv:1609.02747. 22
[21] Eastwood, M. and Matveev, V. S. (2007) Metric connections in projective differential geometry. In Symmetries and Overdetermined Systems of Partial Differential Equations, IMA Vol. Math. Appl., 144. 4
[22] Fefferman, C. L., (1976) Monge-Ampère equations, the Bergman kernel, and geometry of pseudoconvex domains. Ann. of Math. (2) 103, 395-416 12
[23] Hammerl, M. and Sagerschnig, K. (2011) A non-normal Fefferman-type construction of split-signature conformal structures admitting twistor spinors. arXiv:1109.4231. 19
[24] Hammerl, M., Sagerschnig, K., Silhan, J., Taghavi-Chabert, A. and Zadnik, V. Conformal Patterson-Walker metrics. arXiv:1604.08471. 12, 19
[25] Hirzebruch, F. and Hopf, H. (1958) Felder von Flächenelementen in 4-dimensionalen Mannigfaltigkeiten. Math. Ann. 136, 156-172. 16
[26] Kobayashi, S. and Nagano, T. (1964) On projective connections, J. Math. Mech. 13, 215-235. 4
[27] Kryński, W. (2014) Webs and projective structures on a plane. Diff. Geom. Appl. 37, 133. 21
[28] Kruglikov, B. and The, D. (2014) The gap phenomenon in parabolic geometries. J. reine angew. Math. 22
[29] Libermann, P. (1954) Sur le problème d'équivalence de certaines structures infinitésimales, Ann. Mat. Pura Appl. (4) 36, 27-120. 10
[30] Lie, S. (1882) Untersuchungen über geodätische Kurven, Math. Ann. 20. 21
[31] Nurowski, P. and Sparling, G. A. (2003) Three-dimensional Cauchy-Riemann structures and second-order ordinary differential equations. Classical Quantum Gravity. 23, 4995-5016. 12
[32] Mason, L. J. and Woodhouse, N. M. J. (1996) Integrability, selfduality, and twistor theory. Oxford, UK: Clarendon (LMS monographs, new series: 15). 17
[33] Mettler, T. (2015) Extremal conformal structures on projective surfaces, arXiv:1510.01043 7
[34] Mettler, T. (2016) Minimal Lagrangian connections on compact surfaces, arXiv:1609.08033 7
[35] Nakata, F. (2007) Self-dual Zollfrei conformal structures with alpha-surface foliation. J. Geom. Phys. 57, 2077-2097 18
[36] Patterson, E. M. and Walker, A. G. (1952) Riemann extensions. Quart. J. Math., Oxford Ser. (2) 3, 19-28 6, 12
[37] Penrose, R. (1976) Nonlinear gravitons and curved twistor theory, Gen. Rel. Grav. 7, 31-52 7
[38] Randal, M. (2014) Local obstructions to projective surfaces admitting skew-symmetric Ricci tensor Jour. Geom. Phys. 76, 192. 21
[39] Romanovskii, Y. R. (1996) Calculation of local symmetries of second-order ordinary differential equations by Cartans equivalence method, Math. Notes 60 56. 21
[40] Tafel, J. Wojcik, D. (1998) Null Killing vectors and reductions of the self-duality equations, Nonlinearity 11 835. 17
[41] Yano, K. and Ishihara, S. (1973) Tangent and Cotangent Bundles. Differential Geometry Marcel Dekker, Inc. New York. 12
[42] Yano, K. (1955) The Theory Of Lie Derivatives And Its Applications. North Holland 14
[43] Walker, A. G. (1950) Canonical form for a Riemannian space with a parallel field of null planes. Quart. J. Math. Oxford 1, 69 . 14
[44] Walker, A. G. (1953) Riemann extensions of non-Riemannian spaces. In Convegno di Geometria Differenziale. Venice. 18
\begin{itemize}
\item[] [45] Wong, Y. C. (1964) Two dimensional linear connexions with zero torsion and recurrent curvature. Monatsh. Math. 68, 175. 21
\item[] [46] Weyl H. (1921) Zur Infinitesimalgeometrie: Einordnung der projektiven und der konformen Auffassung, Nachr. Ges. Wiss. Göttingen, Math.-Phys. Kl., 1921, 99-112. 3
\end{itemize}

Department of Applied Mathematics and Theoretical Physics, University of Cambridge, Wilberforce Road, Cambridge CB3 0WA, UK.
E-mail address: m.dunajski@damtp.cam.ac.uk
Institut für Mathematik, Goethe-Universität Frankfurt, Robert-Mayer-Str. 10, 60325 Frankfurt, Germany.
E-mail address: mettler@math.uni-frankfurt.de
---
retention_scope: session
part: 4
total_parts: 4
---

[Part 4/4 of: [1210.4707] Boundary pairs associated with quadratic forms]

In [KuK02] (see also the references therein), Kuchment and Kunyansky consider the above-mentioned operator $H_{a}$ appearing as the limit operator in the analysis of photonic crystals supported on a periodic (hexagonal) lattice $\Gamma$ embedded in $X=\mathbb{R}^{2}$. As in our approach, they reduce the eigenvalue problem for $H_{a}$ to an eigenvalue problem for $\Lambda(z)$. Then they investigate the nature of the operator $\Lambda(z)$ on $Y$, and try find a good candidate of a differential operator on $Y$ being close to the pseudo-differential operator $\Lambda(z)$. This problem is still not yet completely understood. We believe that our method helps to analyse these problems further.

\subsection*{6.6 Laplacian with mixed boundary conditions: the Zaremba problem}

\section*{An elliptically regular Zaremba problem}

Let $X$ be a compact Riemannian manifold with smooth boundary $\partial X$. Let $Y \subset \partial X$ be a compact submanifold of the same dimension as $\partial X$, with smooth boundary in $\partial X$, and let $Z:=\overline{\partial X \backslash Y}$. We call the Laplacian on $X$ with Dirichlet condition on $Z$ and Neumann condition on $Y$ the Zaremba Laplacian, denoted by $\Delta_{X}^{Z}$ (in particular, $\Delta^{\mathrm{D}}=\Delta_{X}^{\partial X}$ and $\Delta^{\mathrm{N}}=\Delta_{X}^{\emptyset}$ ).

Let us first compare the Zaremba Laplacian with the Dirichlet Laplacian on $X$. We will see that we can again treat this problem with our boundary pair method.

Set $\mathscr{H}:=\mathrm{L}_{2}(X)$ and set
$$\mathscr{H}^{1}:=\mathrm{H}_{Z}^{1}(X):=\left\{u \in \mathrm{H}^{1}(X) \mid u \upharpoonright_{Z}=0\right\}, \quad \mathfrak{h}(u):=\|\mathrm{d} u\|^{2} .$$
As boundary operator we choose $\Gamma u:=u \upharpoonright_{Y}$.
Theorem 6.36. The boundary pair $(\Gamma, \mathscr{G})$ associated with the form $\mathfrak{h}$ is unbounded, elliptically regular and not positive. The Neumann operator H is the Zaremba Laplacian $\Delta_{X}^{Z}$ on $X$ with Dirichlet condition on $Z$ and Neumann condition on $Y$. Moreover, the Dirichlet operator is the Laplacian $\Delta_{X}^{\mathrm{D}}=\Delta_{X}^{\partial X}$ with (pure) Dirichlet condition on $\partial X$.

The range of the boundary map is $\mathscr{G}^{1 / 2}=\left\{\varphi \in \mathrm{L}_{2}(Y) \mid \widetilde{\varphi} \in \mathrm{H}^{1 / 2}(\partial X)\right\}$, where $\widetilde{\varphi}=\varphi \oplus 0$ is the extension of $\varphi \in \mathrm{L}_{2}(Y)$ by 0 on $Z$. The Dirichlet solution operator is given by $S(z) \varphi=S_{(X, \partial X)}(z) \widetilde{\varphi}$, where $S_{(X, \partial X)}(z)$ is the Dirichlet solution (Poisson) operator for the boundary pair associated with $X$ and the entire boundary $\partial X$.

Finally, the Zaremba Laplacian and the Dirichlet-to-Neumann operator $\Lambda(z)\left(z \notin \sigma\left(\Delta_{X}^{\mathrm{D}}\right)\right)$ have discrete spectrum.
Proof. Clearly, $\Gamma: \mathscr{H} \longrightarrow^{1} \mathscr{G}:=\mathrm{L}_{2}(Y)$ is bounded since $u \mapsto u \upharpoonright_{\partial X}$ is bounded, as well as the restriction map $\mathrm{L}_{2}(\partial Y) \rightarrow \mathrm{L}_{2}(Y)$. Moreover, that $(\Gamma, \mathscr{G})$ is an unbounded boundary pair follows from the existence of $\widetilde{\varphi} \in \mathrm{H}^{1 / 2}(\partial X) \backslash$ $\mathrm{L}_{2}(\partial X)$ such that $\tilde{\varphi} \upharpoonright_{Z}=0$.

The assertion on $\mathscr{G}^{1 / 2}$ and the Dirichlet solution operator is easily seen by noting that for $\varphi \in \mathscr{G}^{1 / 2}$ there exists $u \in \mathrm{H}_{Z}^{1}(X)$ such that $\varphi=u \upharpoonright_{Y}$. In particular, the extension by 0 is just $\widetilde{\varphi}=u \upharpoonright_{\partial X}$, and hence in $\mathrm{H}^{1 / 2}(\partial X)$. The elliptic regularity follows from
$$\mathfrak{q}(\varphi)=\|S \varphi\|_{\mathrm{L}_{2}(X)}^{2}=\left\|S_{(X, \partial X)} \widetilde{\varphi}\right\|_{\mathrm{L}_{2}(X)}^{2} \leq C^{2}\|\widetilde{\varphi}\|_{\mathrm{L}_{2}(\partial X)}^{2}=C^{2}\|\widetilde{\varphi}\|_{\mathrm{L}_{2}(Y)}^{2}$$
for all $\varphi \in \mathscr{G}^{1 / 2}$, where we used the elliptic regularity of the boundary pair associated with the manifold $X$ and boundary $\partial X$ (see Section 6.3). The non-positivity can be seen as in Section 6.3.

As $\stackrel{\circ}{\mathrm{H}}^{1}(X) \subset \mathrm{H}_{Z}^{1}(X) \subset \mathrm{H}^{1}(X)$ we have $H^{\mathrm{D}}=\Delta_{X}^{\mathrm{D}} \geq H=\Delta_{X}^{Z} \geq \Delta_{X}^{\mathrm{N}}$, where the latter is the Laplacian on $X$ with Neumann boundary conditions on the entire boundary $\partial X$. The latter has compact resolvent, so the same is true for the Zaremba and Dirichlet Laplacian $H$ and $H^{\mathrm{D}}$, respectively. Moreover, $\Gamma$ is a compact operator, since $\Gamma u=\widetilde{\Gamma} u \upharpoonright_{Y}$, and $\widetilde{\Gamma}: \mathrm{H}^{1}(X) \longrightarrow \mathrm{L}_{2}(\partial X)$ is compact. In particular, $\Lambda(z)$ has discrete spectrum by Theorem 2.36. \(\square\)

Krein's resolvent formula here relates the resolvent of the Zaremba Laplacian with the pure Dirichlet Laplacian
$$\left(\Delta_{X}^{Z}-z\right)^{-1}-\left(\Delta_{X}^{\mathrm{D}}-z\right)^{-1}=\bar{S}(z) \Lambda(z)^{-1} \bar{S}(\bar{z})^{*} .$$
Since the boundary pair is elliptic, the operators on the RHS all act in the Hilbert spaces $\mathscr{G}=\mathrm{L}_{2}(Y)$ and $\mathscr{H}=\mathrm{L}_{2}(X)$.
Remark 6.38. The domain of the Zaremba Laplacian is contained in $\mathrm{H}^{3 / 2-\varepsilon}(X)$ for all $\varepsilon>0$, but not contained in $\mathrm{H}^{3 / 2}(X)$ itself. The latter can be seen in the following situation where $X=[0, \infty) \times \mathbb{R}$ (or some bounded subset containing 0) and $u(x, y):=\operatorname{Im} \sqrt{x+\mathrm{i} y}$ (see [Sh68]); $u$ fulfils a Dirichlet condition on the positive $x$-axis $Z$ and a Neumann condition on the negative $x$-axis $Y$, and $\Delta u=0$. Moreover, $\partial_{\mathrm{n}} u \upharpoonright_{Z}$ is not in $\mathrm{L}_{2}(Y)$, and hence $u \notin \mathrm{H}^{3 / 2}(X)$. At first sight surprisingly, the Zaremba problem is less regular for smooth boundaries than for certain boundaries with corners (see the discussion in [Gr11, Sec. 4.3] and also [MiMi07]).

\section*{A non-elliptically regular Zaremba problem}

If we use the pure Neumann Laplacian as reference operator (by choosing $\mathscr{H}^{1}:=\mathrm{H}^{1}(X)$ ) and again, $\Gamma u=u \upharpoonright_{Y}$, then the Dirichlet operator $H^{\mathrm{D}}$ is the Zaremba Laplacian $\Delta_{X}^{Y}$, now with Dirichlet condition on $Y$ and Neumann condition on $Z$, and the Neumann operator $H$ is the pure Neumann Laplacian $\Delta_{X}^{\mathrm{N}}$.

Theorem 6.39. The boundary pair $(\Gamma, \mathscr{G})$ associated with the form $\mathfrak{h}$ corresponding to the pure Neumann Laplacian on $X$ is unbounded, and not elliptically regular. The Dirichlet operator $H^{\mathrm{D}}$ is the Zaremba Laplacian $\Delta_{X}^{Y}$, now with Dirichlet condition on $Y$ and Neumann condition on $Z$. The boundary map range space $\mathscr{G}^{1 / 2}$ is $\mathrm{H}^{1 / 2}(Y):=$ $\left\{\psi \upharpoonright_{Y} \mid \psi \in \mathrm{H}^{1 / 2}(\partial X)\right\}$. Finally, the Zaremba Laplacian and the Dirichlet-to-Neumann operator $\Lambda(z)\left(z \notin \sigma\left(\Delta_{X}^{Y}\right)\right)$ have discrete spectrum.

Proof. That the boundary pair is not elliptically regular can be seen as follows: As in Remark 6.38, where $X=$ $[0, \infty) \times \mathbb{R}$, one can find functions $u \in \operatorname{dom} H^{\mathrm{D}}$ (the Zaremba domain) such that $\check{\Gamma}^{\prime} u$ is not contained in $\mathscr{G}$, and hence by Remark 3.6 (i) the boundary pair is not elliptic.

The Neumann operator has discrete spectrum since $X$ is compact with smooth boundary. The compactness of $\Lambda^{-1}$ can be seen as before. \(\square\)

Krein's resolvent formula in this case still holds, but only in its "weak" form
$$\left(\Delta_{X}^{\mathrm{N}}-z\right)^{-1}-\left(\Delta_{X}^{Y}-z\right)^{-1}=S(z) \breve{\Lambda}(z)^{-1} S(\bar{z})^{*},$$
since now, the operators on the RHS map as $\mathscr{H} \rightarrow \mathscr{G}^{-1 / 2} \rightarrow \mathscr{G}^{1 / 2} \rightarrow \mathscr{H}$. Similar formulae have also been shown in [Gr11] and [Pa06]. Moreover, since $R$ and $\Lambda^{-1}$ are compact, we have the spectral relation
$$\lambda \in \sigma\left(\Delta_{X}^{\mathrm{N}}\right) \quad \Leftrightarrow \quad 0 \in \sigma(\Lambda(\lambda)),$$
if $\lambda \notin \sigma\left(\Delta_{X}^{Y}\right)$. In other words, if the spectrum and eigenfunctions of $\Delta_{X}^{\mathrm{N}}$ are known, we know the 0-eigenspace of the Dirichlet-to-Neumann operator (cf. Theorem 4.11 (ii)).

Remark 6.41. We would like to stress here that the boundary pair of Theorem 6.36 can also be treated with the methods of quasi-boundary triples, according to Theorem 1.20 (i). On the other hand, the boundary pair of Theorem 6.39 does not correspond to a quasi boundary triple, and can hence be treated only by our boundary pair concept.

\subsection*{6.7 Example of a generalised boundary pair: discrete Laplacians}

Let us present here another class of examples; in this case, the boundary pair is a generalised one, i.e., $\mathrm{ker} \Gamma$ is no longer dense in $\mathscr{H}$.

Let $(V, E, \partial)$ be a discrete graph, i.e., $V$ denotes the set of vertices, $E$ the set of edges and $\partial: E \longrightarrow V \times V$ maps $e$ onto $\left(\partial_{-} e, \partial_{+} e\right)$, the initial and terminal vertex of $e$; fixing therefore also an orientation. Denote by $E_{v}$ the set of edges $e$ adjacent with the vertex $v \in V$ (i.e., $e \in E_{v}$ iff $v=\partial_{+} e$ or $v=\partial_{-} e$. If $e \in E_{v}$, we denote by $v_{e}$ the vertex on the other end of $e$.

We assume for simplicity here that the graph is finite. Let $\mu: V \longrightarrow(0, \infty)$ and $\varrho: E \longrightarrow(0, \infty)$ be functions, the vertex and edge weights. Let
$$\mathscr{H}:=\ell_{2}(V, \mu), \quad\|f\|_{\ell_{2}(V, \mu)}^{2}:=\sum_{v \in V}|f(v)|^{2} \mu(v),$$
and set
$$\mathfrak{h}(f):=\sum_{e \in E}\left|f\left(\partial_{+} e\right)-f\left(\partial_{-} e\right)\right|^{2} \varrho(e)$$
with $\operatorname{dom} \mathfrak{h}=\mathscr{H}^{1}=\mathscr{H}$. Since this form is bounded, we can omit the subscripts $(\cdot)^{1}$ indicating the form domain. The Neumann operator $H$, i.e., the operator associated with $\mathfrak{h}$ acts as
$$(H f)(v)=\frac{1}{\mu(v)} \sum_{e \in E_{v}} \varrho(e)\left(f(v)-f\left(v_{e}\right)\right) .$$
If we choose $\mu(v)=1$ and $\varrho(e)=1$ then we arrive at the combinatorial Laplacian; if we choose $\mu(v)=\operatorname{deg} v=\left|E_{v}\right|$ and $\varrho(e)=1$, then we arrive at the normalised Laplacian.

We now declare a subset of $V$ as boundary of the graph, i.e., let $\partial V \subset V$ be the set of boundary vertices. The vertices in its complement, $\stackrel{\circ}{V}:=V \backslash \partial V$, are called inner vertices. We set
$$\mathscr{G}:=\ell_{2}(\partial V, \mu), \quad \Gamma f:=f \upharpoonright_{\partial V} .$$
Note that $\mathscr{H}^{\mathrm{D}}:=\operatorname{ker} \Gamma=\ell_{2}(\stackrel{\circ}{V}, \mu)$ is not dense in $\mathscr{H}=\ell_{2}(V, \mu)$. Therefore, $(\Gamma, \mathscr{G})$ is a generalised bounded boundary pair associated with $\mathfrak{h}$. The Dirichlet operator acts formally as $H$, but only on $\ell_{2}(\stackrel{\circ}{V}, \mu)$; if $\iota: \ell_{2}(\stackrel{\circ}{V}, \mu) \hookrightarrow \ell_{2}(V, \mu)$ denotes the natural embedding, and $\pi:=\iota^{*}$ the corresponding projection, then $H^{\mathrm{D}}=\pi H \iota$. Note that this example corresponds to $X=V, Y=\partial V$ and $\nu=\mu \upharpoonright_{\partial V}$ in the notation of Example 2.4.

Before giving a formula for the Dirichlet solution operator, let us represent the operator $H$ in block structure
$$H=\left(\begin{array}{cc}
A & B \\
B^{*} & D
\end{array}\right)$$
with respect to the splitting $\mathscr{H}=\mathscr{G} \oplus \mathscr{H}^{\mathrm{D}}$, i.e., $\ell_{2}(V, \mu)=\ell_{2}(\partial V, \mu) \oplus \ell_{2}(\stackrel{\circ}{V}, \mu)$. Here, $D=H^{\mathrm{D}}$ is the Dirichlet operator, and $A: \mathscr{G} \longrightarrow \mathscr{G}, B: \mathscr{H}^{\mathrm{D}} \longrightarrow \mathscr{G}$. Let $z \notin \sigma(D)$, then $h \in \mathscr{N}(z):=\mathscr{N}^{1}(z)$ iff $(H-z) h \upharpoonright_{\dot{V}}=0$. Denote by $H^{\text {max }}: \mathscr{H} \longrightarrow \mathscr{H}^{\mathrm{D}}$ the operator $H$ restricted to $\mathscr{H}^{\mathrm{D}}$ (this is actually consistent with $H^{\text {min }}:=H^{\mathrm{D}} \cap H$, the minimal operator $H^{\text {min }}$, which acts as $\mathscr{H}^{\mathrm{D}} \rightarrow \mathscr{H}$, and $H^{\text {max }}=\left(H^{\text {min }}\right)^{*}$ ). Using the matrix decomposition, we have $H^{\max } f=B^{*} f_{\partial}+D f_{0}$, where $f=f_{\partial} \oplus f_{0} \in \mathscr{G} \oplus \mathscr{H}^{\mathrm{D}}$.

Moreover,
$$\begin{aligned}
\mathfrak{h}(f, g)=\langle H f, g\rangle_{\mathscr{H}} & =\left\langle B^{*} f_{\partial}+D f_{0}, g_{0}\right\rangle_{\mathscr{H}^{\mathrm{D}}}+\left\langle A f_{\partial}+B f_{0}, g_{\partial}\right\rangle_{\mathscr{G}} \\
& =\left\langle H^{\text {max }} f, g_{0}\right\rangle_{\mathscr{H}^{\mathrm{D}}}+\left\langle\Gamma^{\prime} f, \Gamma g\right\rangle_{\mathscr{G}},
\end{aligned}$$
which can be interpreted as Green's (first) identity (1.14), where the "normal derivative" $\Gamma^{\prime}: \mathscr{H} \longrightarrow \mathscr{G}$ is given by $\Gamma^{\prime} f:=A f_{\partial}+B f_{0}$, i.e.,
$$\left(\Gamma^{\prime} f\right)(v)=\frac{1}{m(v)} \sum_{e \in E_{v}} \varrho(e)\left(f(v)-f\left(v_{e}\right)\right), \quad v \in \partial V .$$

It is now easily seen that the Dirichlet solution operator is given by
$$S(z) \varphi=\varphi \oplus\left(-(D-z)^{-1} B^{*} \varphi\right),$$
(since $\left(H^{\text {max }}-z\right) S(z)=0$ on $\mathscr{H}^{\mathrm{D}}$ and $\Gamma S(z) \varphi=\varphi$ ); note that the inverse exists since $z \notin \sigma(D)$. The Dirichlet-to-Neumann operator is defined as
$$\begin{aligned}
\langle\Lambda(z) \varphi, \psi\rangle_{\mathscr{G}} & =\langle(H-z) S(z) \varphi, g\rangle_{\mathscr{H}} \\
& =\left\langle\left(A-z-B(D-z)^{-1} B^{*}\right) \varphi, \psi\right\rangle_{\mathscr{G}}+\left\langle B^{*} \varphi-(D-z)(D-z)^{-1} B^{*} \varphi, g_{0}\right\rangle_{\mathscr{H}}{ }^{\mathrm{D}}
\end{aligned}$$
where $g \in \mathscr{H}$ is arbitrary with $g \upharpoonright_{\partial V}=\psi$. Since the latter summand vanishes, we obtain for the Dirichlet-to-Neumann operator
$$\Lambda(z)=(A-z)-B(D-z)^{-1} B^{*}: \mathscr{G} \longrightarrow \mathscr{G} .$$
Moreover, the interpretation is the same as in the manifold case: We have $\Lambda(z) \varphi=\Gamma^{\prime} S(z) \varphi$, i.e., the Dirichlet-to-Neumann operator associates to the boundary data $\varphi$ the "normal" derivative of the Dirichlet solution $h=S(z) \varphi$.

Note that the Dirichlet-to-Neumann operator can also be understood as the Schur complement of the block operator $H-z$ with respect to the lower left $\left(\mathscr{H}^{\mathrm{D}} \times \mathscr{H}^{\mathrm{D}}\right)$-block.

Finally, the spectral characterisation reads as follows: if $\lambda \notin \sigma\left(H^{\mathrm{D}}\right)$ (i.e., not an eigenvalue of $D$ ), then $\lambda \in \sigma(H)$ iff $0 \in \sigma(\Lambda)(\lambda)$, i.e., if $\Lambda(\lambda)$ is a singular matrix $(\operatorname{det} \Lambda(\lambda)=0)$. This fact can also be seen directly in this simple situation.

Finally, Krein's resolvent formula is just a variant of the inversion of the block operator $H-z$, namely,
$$\begin{aligned}
R(z)-\iota^{*} R^{\mathrm{D}}(z) \iota & =\left(\begin{array}{cc}
A-z & B \\
B^{*} & D-z
\end{array}\right)^{-1}-\left(\begin{array}{cc}
0 & 0 \\
0 & (D-z)^{-1}
\end{array}\right) \\
& =\binom{\operatorname{id}_{\mathscr{G}}}{-(D-z)^{-1} B^{*}}\left((A-z)-B(D-z)^{-1} B^{*}\right)^{-1}\left(\operatorname{id}_{\mathscr{G}},-B(D-z)^{-1}\right) \\
& =S(z) \Lambda(z)^{-1} S(\bar{z})^{*}
\end{aligned}$$

If we allow infinite graphs, then we may also have unbounded forms $\mathfrak{h}$ (if, e.g., $\mu(v)=1, \varrho(v)=1$ and $\operatorname{deg} v$ is unbounded on the graph) and the above spectral characterisation and Krein's formula become less obvious. Such cases and even more general ones ("discrete Dirichlet forms") are considered in HKLW12. We can also use different weights for the boundary space and therefore also have unbounded boundary pairs. We hope to come back to the unbounded case in a forthcoming publication.

\section*{References}
\begin{itemize}
\item[] [AGrW14] H. Abels, G. Grubb and I. G. Wood, Extension theory and Kreĭn-type resolvent formulas for nonsmooth boundary value problems, J. Funct. Anal. 266 (2014), 4037-4100.
\item[] [AS80] A. Alonso and B. Simon, The Birman-Kreĭn-Vishik theory of selfadjoint extensions of semibounded operators, J. Operator Theory 4 (1980), 251-270.
\item[] [AN70] T. Ando and K. Nishio, Positive selfadjoint extensions of positive symmetric operators, Tôhoku Math. J. (2) 22 (1970), 65-75.
\item[] [AM12] W. Arendt and R. Mazzeo, Friedlander's eigenvalue inequalities and the Dirichlet-to-Neumann semigroup, Commun. Pure Appl. Anal. 11 (2012), 2201-2212.
\item[] [AtE11] W. Arendt and A. F. M. ter Elst, The Dirichlet-to-Neumann operator on rough domains, J. Differential Equations 251 (2011), 2100-2124.
\item[] [AtE12a] \_\_\_\_, Sectorial forms and degenerate differential operators, J. Operator Theory 67 (2012), 33-72.
\item[] [AtE12b] W. Arendt and A. F. M. ter Elst, From forms to semigroups, Spectral theory, mathematical system theory, evolution equations, differential and difference equations, Oper. Theory Adv. Appl., vol. 221, Birkhäuser/Springer Basel AG, Basel, 2012, pp. 47-69.
\item[] [Ar96] Y. M. Arlinskiĭ, Maximal sectorial extensions and closed forms associated with them, Ukraïn. Mat. Zh. 48 (1996), 723-738.
\item[] [Ar99] Y. M. Arlinskii, On functions connected with sectorial operators and their extensions, Integral Equations Operator Theory 33 (1999), 125-152.
\item[] [Ar00] Y. Arlinskii, Abstract boundary conditions for maximal sectorial extensions of sectorial operators, Math. Nachr. 209 (2000), 5-36.
\item[] [Ar12] Y. Arlinskiĭ, Boundary triplets and maximal accretive extensions of sectorial operators, Ch. 3 in HdSS12 (2012), 121-160.
\item[] [BeLa07] J. Behrndt and M. Langer, Boundary value problems for elliptic partial differential operators on bounded domains, J. Funct. Anal. 243 (2007), 536-565.
\item[] [BeLa12] \_\_\_\_, Elliptic operators, Dirichlet-to-Neumann maps and quasi boundary triples, Ch. 6 in HdSS12] (2012), 121-160.
\item[] [BeLaL13] J. Behrndt, M. Langer, and V. Lotoreichik, Schrödinger operators with $\delta$ and $\delta^{\prime}$-potentials supported on hypersurfaces, Ann. Henri Poincaré 14 (2013), 385-423.
\item[] [BeM14] J. Behrndt and T. Micheler, Elliptic differential operators on Lipschitz domains and abstract boundary value problems, J. Funct. Anal. 267 (2014), 3657-3709.
\item[] [BeP] J. Behrndt and O. Post, Convergence of the dirichlet-to-neumann operators on thin branched manifolds, in preparation.
\item[] [BedS09] J. Behrndt and H. de Snoo, On Kreŭn's formula, J. Math. Anal. Appl. 351 (2009), 567-578.
\item[] [BBABr11] H. BelHadjAli, A. Ben Amor and J. F. Brasche, Large coupling convergence: overview and new results, Partial differential equations and spectral theory, Oper. Theory Adv. Appl., vol. 211, Birkhäuser/Springer Basel AG, Basel, 2011, pp. 73-117.
\end{itemize}
\begin{itemize}
\item[] [BABr08] A. Ben Amor and J. F. Brasche, Sharp estimates for large coupling convergence with applications to Dirichlet operators, J. Funct. Anal. 254 (2008), 454-475.
\item[] [Bir56] M. Š. Birman, On the theory of self-adjoint extensions of positive definite operators, Mat. Sb. N.S. 38(80) (1956), 431-450.
\item[] [BrD05] J. Brasche and M. Demuth, Dynkin's formula and large coupling convergence, J. Funct. Anal. 219 (2005), 34-69.
\item[] [BrMN02] J. F. Brasche, M. Malamud and H. Neidhardt, Weyl function and spectral properties of self-adjoint extensions, Integral Equations Operator Theory 43 (2002), 264-289.
\item[] [BGrW09] B. M. Brown, G. Grubb and I. G. Wood, $M$-functions for closed extensions of adjoint pairs of operators with applications to elliptic boundary problems, Math. Nachr. 282 (2009), 314-347.
\item[] [BGPa08] J. Brüning, V. Geyler and K. Pankrashkin, Spectra of self-adjoint extensions and applications to solvable Schrödinger operators, Rev. Math. Phys. 20 (2008), 1-70.
\item[] [CMPc13] R. Carlone, M. Malamud and A. Posilicano, On the spectral theory of Gesztesy-Šeba realizations of 1-D Dirac operators with point interactions on a discrete set, J. Differential Equations 254 (2013), 3835-3902.
\item[] [Da95] E. B. Davies, Spectral theory and differential operators, Cambridge University Press, Cambridge, 1995.
\item[] [DHMdS00] V. Derkach, S. Hassi, M. Malamud and H. de Snoo, Generalized resolvents of symmetric operators and admissibility, Methods Funct. Anal. Topology 6 (2000), 24-55.
\item[] [DHMdS06] \_\_\_\_, Boundary relations and their Weyl families, Trans. Amer. Math. Soc. 358 (2006), 5351-5400.
\item[] [DHMdS09] \_\_\_\_, Boundary relations and generalized resolvents of symmetric operators, Russ. J. Math. Phys. 16 (2009), 17-60.
\item[] [DHMdS12] \_\_\_\_, Boundary triplets and Weyl functions. Recent developments, Ch. 7 in [HdSS12] (2012), 121-160.
\item[] [DM95] V. Derkach and M. Malamud, The extension theory of Hermitian operators and the moment problem, J. Math. Sci. (New York) 73 (1995), 141-242.
\item[] [Di96] Z. Ding, A proof of the trace theorem of Sobolev spaces on Lipschitz domains, Proc. Amer. Math. Soc. 124 (1996), 591-600.
\item[] [EL04] D. Eschwé and M. Langer, Variational principles for eigenvalues of self-adjoint operator functions, Integral Equations Operator Theory 49 (2004), 287-321.
\item[] [Ex08] P. Exner, Leaky quantum graphs: a review, Analysis on graphs and its applications, Proc. Sympos. Pure Math., vol. 77, Amer. Math. Soc., Providence, RI, 2008, pp. 523-564.
\item[] [GeMi08] F. Gesztesy and M. Mitrea, Generalized Robin boundary conditions, Robin-to-Dirichlet maps, and Kreintype resolvent formulas for Schrödinger operators on bounded Lipschitz domains, Perspectives in partial differential equations, harmonic analysis and applications, Proc. Sympos. Pure Math., vol. 79, Amer. Math. Soc., Providence, RI, 2008, pp. 105-173.
\item[] [GeMi09] \_\_\_\_, Robin-to-Robin maps and Krein-type resolvent formulas for Schrödinger operators on bounded Lipschitz domains, Modern analysis and applications. The Mark Krein Centenary Conference. Vol. 2: Differential operators and mechanics, Oper. Theory Adv. Appl., vol. 191, Birkhäuser Verlag, Basel, 2009, pp. 81-113.
\item[] [GeMi11] \_\_\_\_, A description of all self-adjoint extensions of the Laplacian and Kreĭn-type resolvent formulas on non-smooth domains, J. Anal. Math. 113 (2011), 53-172.
\item[] [GG91] V. I. Gorbachuk and M. L. Gorbachuk, Boundary value problems for operator differential equations, Mathematics and its Applications (Soviet Series), vol. 48, Kluwer Academic Publishers Group, Dordrecht, 1991.
\item[] [Gre87] G. Greiner, Perturbing the boundary conditions of a generator, Houston J. Math. 13 (1987), 213-229.
\item[] [Gv85] P. Grisvard, Elliptic problems in nonsmooth domains, Monographs and Studies in Mathematics, vol. 24, Pitman (Advanced Publishing Program), Boston, MA, 1985.
\item[] [Gr68] G. Grubb, A characterization of the non-local boundary value problems associated with an elliptic operator, Ann. Scuola Norm. Sup. Pisa (3) 22 (1968), 425-513.
\item[] [Gr70] \_\_\_\_, Les problèmes aux limites généraux d'un opérateur elliptique, provenant de la théorie variation-nelle, Bull. Sci. Math. (2) 94 (1970), 113-157.
\item[] [Gr08] \_\_\_\_, Krein resolvent formulas for elliptic boundary problems in nonsmooth domains, Rend. Semin. Mat. Univ. Politec. Torino 66 (2008), 271-297.
\item[] [Gr11] \_\_\_\_, The mixed boundary value problem, Krein resolvent formulas and spectral asymptotic estimates, J. Math. Anal. Appl. 382 (2011), 339-363.
\item[] [GKMV13] L. Grubišić, V. Kostrykin, K. A. Makarov and K. Veselić, Representation theorems for indefinite quadratic forms revisited, Mathematika 59 (2013), 169-189.
\item[] [HKLW12] S. Haeseler, M. Keller, D. Lenz and R. Wojciechowski, Laplacians on infinite graphs: Dirichlet and Neumann boundary conditions, J. Spectr. Theory 2 (2012), 397-432.
\end{itemize}
\begin{itemize}
\item[] [HdSS12] S. Hassi, H. S. V. de Snoo and F. H. Szafraniec (eds.), Operator methods for boundary value problems, London Mathematical Society Lecture Note Series, vol. 404, Cambridge University Press, Cambridge, 2012.
\item[] [JN01] J. Janas and S. Naboko, Spectral properties of selfadjoint Jacobi matrices coming from birth and death processes, Recent advances in operator theory and related topics (Szeged, 1999), Oper. Theory Adv. Appl., vol. 127, Birkhäuser, Basel, 2001, pp. 387-397.
\item[] [JK81] D. S. Jerison and C. E. Kenig, The Neumann problem on Lipschitz domains, Bull. Amer. Math. Soc. (N.S.) 4 (1981), 203-207.
\item[] [JeKe95] \_\_\_\_, The inhomogeneous Dirichlet problem in Lipschitz domains, J. Funct. Anal. 130 (1995), 161-219.
\item[] [Ka66] T. Kato, Perturbation theory for linear operators, Springer-Verlag, Berlin, 1966.
\item[] [KoM10] A. S. Kostenko and M. M. Malamud, 1-D Schrödinger operators with local point interactions on a discrete set, J. Differential Equations 249 (2010), 253-304.
\item[] [Kr47] M. Krein, The theory of self-adjoint extensions of semi-bounded Hermitian transformations and its applications. I, Rec. Math. [Mat. Sbornik] N.S. 20(62) (1947), 431-495.
\item[] [KuK02] P. Kuchment and L. Kunyansky, Differential operators on graphs and photonic crystals, Adv. Comput. Math. 16 (2002), 263-290, Modeling and computation in optics and electromagnetics.
\item[] [LT77] H. Langer and B. Textorius, On generalized resolvents and $Q$-functions of symmetric linear relations (subspaces) in Hilbert space, Pacific J. Math. 72 (1977), 135-165.
\item[] [LiMa68] J.-L. Lions and E. Magenes, Problèmes aux limites non homogènes et applications. Vol. 1, Travaux et Recherches Mathématiques, No. 17, Dunod, Paris, 1968.
\item[] [LySt83] V. È. Lyantse and O. G. Storozh, Metody teorii neogranichennykh operatorov, "Naukova Dumka", Kiev, 1983.
\item[] [M92] M. M. Malamud, Certain classes of extensions of a lacunary Hermitian operator, Ukraïn. Mat. Zh. 44 (1992), 215-233.
\item[] [M10] \_\_\_\_, Spectral theory of elliptic operators in exterior domains, Russ. J. Math. Phys. 17 (2010), 96-125.
\item[] [MMo02] M. M. Malamud and V. I. Mogilevskii, Kreĭn type formula for canonical resolvents of dual pairs of linear relations, Methods Funct. Anal. Topology 8 (2002), 72-100.
\item[] [MSch12] M. M. Malamud and K. Schmüdgen, Spectral theory of Schrödinger operators with infinitely many point interactions and radial positive definite functions, J. Funct. Anal. 263 (2012), 3144-3194.
\item[] [McI69] A. G. R. McIntosh, Bilinear forms in Hilbert space, J. Math. Mech. 19 (1969), 1027-1045.
\item[] [McI70] \_\_\_\_, Hermitian bilinear forms which are not semibounded, Bull. Amer. Math. Soc. 76 (1970), 732-737.
\item[] [MiMi07] I. Mitrea and M. Mitrea, The Poisson problem with mixed boundary conditions in Sobolev and Besov spaces in non-smooth domains, Trans. Amer. Math. Soc. 359 (2007), 4143-4182.
\item[] [MiMiT01] D. Mitrea, M. Mitrea, and M. Taylor, Layer potentials, the Hodge Laplacian, and global boundary problems in nonsmooth Riemannian manifolds, Mem. Amer. Math. Soc. 150 (2001), x+120.
\item[] [MiT99] M. Mitrea and M. Taylor, Boundary layer methods for Lipschitz domains in Riemannian manifolds, J. Funct. Anal. 163 (1999), 181-251.
\item[] [MiT03] \_\_\_\_, Potential theory on Lipschitz domains in Riemannian manifolds: the case of Dini metric tensors, Trans. Amer. Math. Soc. 355 (2003), 1961-1985.
\item[] [MiT05] \_\_\_\_, Sobolev and Besov space estimates for solutions to second order PDE on Lipschitz domains in manifolds with Dini or Hölder continuous metric tensors, Comm. Partial Differential Equations 30 (2005), 1-37.
\item[] [Mo12] V. Mogilevskii, Boundary pairs and boundary conditions for general (not necessarily definite) first-order symmetric systems with arbitrary deficiency indices, Math. Nachr. 285 (2012), 1895-1931.
\item[] [MuNP13] D. Mugnolo, R. Nittka and O. Post, Norm convergence of sectorial operators on varying Hilbert spaces, Oper. Matrices 7 (2013), 955-995.
\item[] [Pa06] K. Pankrashkin, Resolvents of self-adjoint extensions with mixed boundary conditions, Rep. Math. Phys. 58 (2006), 207-221.
\item[] [Pc01] A. Posilicano, A Kreĭn-like formula for singular perturbations of self-adjoint operators and applications, J. Funct. Anal. 183 (2001), 109-147.
\item[] [Pc04] \_\_\_\_, Boundary triples and Weyl functions for singular perturbations of self-adjoint operators, Methods Funct. Anal. Topology 10 (2004), 57-63.
\item[] [Pc08] \_\_\_\_, Self-adjoint extensions of restrictions, Oper. Matrices 2 (2008), 483-506.
\item[] [P12] O. Post, Spectral analysis on graph-like spaces, Lecture Notes in Mathematics, vol. 2039, Springer, Heidelberg, 2012.
\item[] [P] \_\_\_\_, Boundary triples associated with quadratic forms, (in preparation).
\end{itemize}
[RS80] M. Reed and B. Simon, Methods of modern mathematical physics I: Functional analysis, Academic Press, New York, 1980.
[Ry07] V. Ryzhov, A general boundary value problem and its Weyl function, Opuscula Math. 27 (2007), 305-331.
[Sa08] J. Sahbani, Spectral theory of certain unbounded Jacobi matrices, J. Math. Anal. Appl. 342 (2008), 663-681.
[Sch12] K. Schmüdgen, Unbounded self-adjoint operators on Hilbert space, Graduate Texts in Mathematics, vol. 265, Springer, Dordrecht, 2012.
[Sh68] E. Shamir, Regularization of mixed second-order elliptic problems, Israel J. Math. 6 (1968), 150-168.
[Tr00] C. Tretter, Linear operator pencils $A-\lambda B$ with discrete spectrum, Integral Equations Operator Theory 37 (2000), 357-373.
[Vi52] M. I. Vishik, On general boundary problems for elliptic differential equations, Trudy Moskov. Mat. Obšč. 1 (1952), 187-246 (English translation in Am. Math. Soc., Transl. (2) 24 (1963), 107-172).
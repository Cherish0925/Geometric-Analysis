---
retention_scope: session
part: 1
total_parts: 4
---

[Part 1/4 of: [1210.4707] Boundary pairs associated with quadratic forms]

---
source_file: 1210_4707.pdf
converter: mathpix
format: mmd
---

\title{
Boundary pairs associated with quadratic forms
}

\author{
Olaf Post
}

September 18, 2018

School of Mathematics, Cardiff University, Senghennydd Road, Cardiff, CF24 4AG, Wales, UK On sabbatical leave from: Department of Mathematical Sciences, Durham University, England, UK
From April 2015: Fachbereich 4 - Mathematik, Universität Trier, 54286 Trier, Germany
E-mail: olaf.post@uni-trier.de

We introduce an abstract framework for elliptic boundary value problems in a variational form. Given a non-negative quadratic form in a Hilbert space, a boundary pair consists of a bounded operator, the boundary operator, and an auxiliary Hilbert space, the boundary space, such that the boundary operator is bounded from the quadratic form domain into the auxiliary Hilbert space.

These data determine a Neumann and Dirichlet operator, a Dirichlet solution and a Dirichlet-to-Neumann operator. The basic example we have in mind is a manifold with boundary, where the quadratic form is the integral over the squared derivative, and the boundary map is the restriction of a function to (a subset of) the boundary of the manifold.

As one of the main theorems, we derive a resolvent formula relating the difference of the resolvents of the Neumann and Dirichlet operator with the Dirichlet solution and the Dirichlet-to-Neumann operator. From this, we deduce a spectral characterisation for a point being in the spectrum of the Neumann operator in terms of the family of Dirichlet-to-Neumann operators. The relation can be generalised also to Robin-type boundary conditions.

We identify conditions expressed purely in terms of boundary pairs, which allow us to relate our concept with existing concepts such as boundary triples. We illustrate the theory by many examples including Jacobi operators, Laplacians on spaces with (non-smooth) boundary and the Zaremba (mixed boundary conditions) problem.

\section*{Contents}
1 Introduction ..... 2
1.1 The basic example for a boundary pair ..... 2
1.2 The abstract theory of boundary pairs ..... 3
1.3 Purpose of this article and outlook ..... 4
1.4 Relation with boundary triples and similar concepts ..... 5
1.5 Extension theory and related other works ..... 7
1.6 Structure of this article ..... 9
1.7 Acknowledgements ..... 9
2 Boundary pairs associated with quadratic forms ..... 9
2.1 Preliminaries: quadratic and sesquilinear forms, scales of Hilbert spaces ..... 9
2.2 Boundary pairs, Dirichlet solution operators and Dirichlet-to-Neumann operators ..... 10
2.3 The Dirichlet solution operator at arbitrary points ..... 12
2.4 The Dirichlet-to-Neumann form at arbitrary points ..... 14
2.5 The Neumann-to-Dirichlet operator ..... 17
3 Boundary pairs with additional properties ..... 18
3.1 Elliptically regular boundary pairs ..... 18
3.2 Positive boundary pairs ..... 22
4 Resolvent formulae and spectral relations ..... 22
4.1 Resolvent formula for boundary pairs ..... 22
4.2 Operator pencils ..... 23
4.3 Spectral relations between the Neumann and the Dirichlet-to-Neumann operator family ..... 25
5 Boundary pairs constructed from other boundary pairs ..... 27
5.1 Robin boundary conditions ..... 27
5.2 Coupled boundary pairs ..... 28
5.3 Direct sum of boundary pairs ..... 30
5.4 Regularisation: Making a boundary pair bounded ..... 30
6 Examples ..... 30
6.1 Examples with finite-dimensional boundary space ..... 30
6.2 Examples with Jacobi operators ..... 31
6.3 Laplacian on Lipschitz domains ..... 34
6.4 Laplacian on a non-compact cylindrical manifold ..... 36
6.5 Dirichlet-to-Neumann operator supported on a metric graph: leaky graphs and photonic crystals ..... 37
6.6 Laplacian with mixed boundary conditions: the Zaremba problem ..... 38
6.7 Example of a generalised boundary pair: discrete Laplacians ..... 39

\section*{1 Introduction}

The following article provides a unified language and approach to very different types of "boundary value problems" based on quadratic forms, which (to our believe) is very natural and starts with minimal assumptions on the model.

\subsection*{1.1 The basic example for a boundary pair}

Probably the best way to illustrate the main subject of this article is to start with our main basic example, from which we borrow the names for the abstract setting: Let $X$ be a manifold with sufficiently smooth boundary $\partial X$ (e.g. Lipschitz, see Section 6.3 for details). We set
$$\mathscr{H}:=\mathrm{L}_{2}(X), \quad \mathfrak{h}(u):=\|\mathrm{d} u\|^{2}, \quad u \in \operatorname{dom} \mathfrak{h}=\mathscr{H}^{1}:=\mathrm{H}^{1}(X),$$
where $\mathrm{H}^{1}(X)$ is the completion of the set of smooth function with respect to the norm given by $\|u\|_{\mathscr{H} 1}^{2}:=\|u\|_{\mathscr{H}}^{2}+\mathfrak{h}(u)$. The operator $H$ associated with $\mathfrak{h}$ is the usual Neumann Laplacian on $X$. As boundary space and operator we set
$$\mathscr{G}:=\mathrm{L}_{2}(Y) \quad \text { and } \quad \Gamma u:=u \upharpoonright_{Y},$$
respectively, where $Y=\partial X$ (or $Y$ is a suitable subset of $\partial X$ ). By a Sobolev trace estimate, $\Gamma: \mathscr{H}^{1} \longrightarrow \mathscr{G}$ is bounded, its kernel is dense in $\mathscr{H}=\mathrm{L}_{2}(X)$, as well as its range $\mathscr{G}^{1 / 2}:=\mathrm{H}^{1 / 2}(Y)$ (the space of those elements $\varphi \in \mathrm{L}_{2}(Y)$ having an extension $\widetilde{\varphi} \in \mathrm{H}^{1 / 2}(\partial X)$, i.e., $\widetilde{\varphi} \upharpoonright_{Y}=\varphi$ ) is dense in $\mathscr{G}$.

The operator $H^{\mathrm{D}}$ associated with the form $\mathfrak{h}^{\mathrm{D}}:=\mathfrak{h} \upharpoonright_{\text {ker } \Gamma}$ is the usual Dirichlet Laplacian (or, if $Y \subseteq \partial X$, a mixed boundary value problem, also called Zaremba problem). The Sobolev space $\mathscr{H}^{1}$ decomposes into the sum of $\mathscr{H}^{1, \mathrm{D}}:=\operatorname{ker} \Gamma$ and $\mathscr{N}^{1}(z)$, where $\mathscr{N}^{1}(z)$ is the space of weak solutions, i.e.,
$$\mathscr{N}^{1}(z):=\left\{h \in \mathscr{H}^{1} \mid \mathfrak{h}(h, f)=z\langle h, f\rangle_{\mathscr{H}} \quad \forall f \in \operatorname{ker} \Gamma=: \mathscr{H}^{1, \mathrm{D}}\right\},$$
and the sum is direct if $z \in \mathbb{C}$ is not in the spectrum of the Dirichlet operator $H^{\mathrm{D}}$. In the latter case, we can invert the boundary operator on the weak solution space and call
$$S(z):=\left(\Gamma \upharpoonright_{\mathscr{N}^{1}(z)}\right)^{-1}: \mathscr{G}^{1 / 2} \longrightarrow \mathscr{H}^{1}$$
the (weak) Dirichlet solution operator or Poisson operator, because $h=S(z) \varphi$ is the (unique) weak solution of the Dirichlet problem $h \in \mathscr{N}^{1}(z)$ with $\Gamma h=\varphi$.

The Dirichlet-to-Neumann operator $\Lambda(z)$ is now defined as the operator associated with the sesquilinear form
$$\mathfrak{l}_{z}(\varphi, \psi):=(\mathfrak{h}-z \mathbf{l})(S(z) \varphi, S(-1) \psi),$$
i.e., $\mathfrak{l}_{z}(\varphi, \psi)=\langle\Lambda(z) \varphi, \psi\rangle_{\mathscr{G}}$ for all $\psi \in \mathscr{G}^{1 / 2}$ and $\varphi \in \operatorname{dom} \Lambda(z) \subset \mathscr{G}^{1 / 2}$. Applying the (first) Green's identity for sufficiently regular $\varphi$ one can see that $\Lambda(z) \varphi=\partial_{\mathrm{n}} h \upharpoonright_{Y}$, i.e., that $\Lambda(z)$ acts as the usual Dirichlet-to-Neumann operator associating the normal derivative of the Dirichlet solution of a boundary value $\varphi$ (see (1.15) below).

As one of the main theorems, we derive a resolvent formula and relate the spectrum of $H$ with the one of the operator pencil $\Lambda(\cdot)$, see Theorem 1.5 below.

\subsection*{1.2 The abstract theory of boundary pairs}

In order to develop an analogue abstract theory, we only need the following data:
\begin{itemize}
\item[-] a closed, non-negative quadratic form $\mathfrak{h}$ with domain $\mathscr{H}^{1}:=\operatorname{dom} \mathfrak{h}$ in a Hilbert space $\mathscr{H}$; where $\mathscr{H}^{1}$ is endowed with its natural norm, see (2.1);
\item[-] an operator $\Gamma: \mathscr{H}^{1} \longrightarrow \mathscr{G}$ (the boundary operator) into another Hilbert space (the boundary space).
\end{itemize}

Definition 1.4. We say that $(\Gamma, \mathscr{G})$ is a boundary pair associated with $\mathfrak{h}$ if $\Gamma$ is bounded,
$$\mathscr{H}^{1, \mathrm{D}}:=\operatorname{ker} \Gamma \text { is dense in } \mathscr{H} \text { and } \quad \mathscr{G}^{1 / 2}:=\operatorname{ran} \Gamma \text { is dense in } \mathscr{G} .$$

We say that the boundary pair is unbounded if the operator $\Gamma$ is not surjective.
In particular, our example above leads to an unbounded boundary pair as the range of the Sobolev trace map $\Gamma$ is $\mathrm{H}^{1 / 2}(Y)$, a space strictly smaller than $\mathrm{L}_{2}(Y)$. It can be seen that a boundary pair is unbounded iff the Dirichlet-to-Neumann operator $\Lambda(z)$ is unbounded (see Theorem 2.11). Moreover, in our example, the Dirichlet solution operator (for $z=0$ ) defined in (1.2) is also called Poisson operator, and this operator extends to a bounded operator $\bar{S}(z): \mathscr{G}=\mathrm{L}_{2}(Y) \longrightarrow \mathscr{H}=\mathrm{L}_{2}(X)$ onto the corresponding $\mathrm{L}_{2}$-spaces; we call such boundary pairs elliptically regular (see Definition 1.10 below).

Let us now formulate one of our main results of this article (see Proposition 2.31 and Theorems 4.3 and 4.14):
Theorem 1.5. Let $(\Gamma, \mathscr{G})$ be an elliptically regular boundary pair, and let $z \in \mathbb{C} \backslash\left(\sigma\left(H^{\mathrm{D}}\right) \cup \sigma(H)\right)$ then the Dirichlet-to-Neumann operator $\Lambda(z)$ has a bounded inverse $\Lambda(z)^{-1}: \mathscr{G} \longrightarrow \mathscr{G}$ and we have
$$R(z)-R^{\mathrm{D}}(z)=\bar{S}(z) \Lambda(z)^{-1} \bar{S}(\bar{z})^{*},$$
relating the difference of the resolvents $R(z)=(H-z)^{-1}$ and $R^{\mathrm{D}}(z)=\left(H^{\mathrm{D}}-z\right)^{-1}$ of the Neumann and Dirichlet operator, respectively, with the (extended) Dirichlet solution operator $\bar{S}(z): \mathscr{G} \longrightarrow \mathscr{H}$ and the Dirichlet-to-Neumann operator $\Lambda(z)$. As a consequence, we deduce a spectral characterisation for a point being in the spectrum of the Neumann operator, namely
$$\lambda \in \sigma(H) \quad \text { iff } \quad 0 \in \sigma(\Lambda(\lambda)),$$
provided $\lambda \notin \sigma\left(H^{\mathrm{D}}\right)$.
One can extend this result in a weaker form also for non-elliptically regular boundary pairs (see Theorems 4.3 and 4.11); we give an example of such a boundary triple below. Resolvent formulas as in (1.6) have been shown in many previous works, see e.g. [BeM14, Cor. 3.14], [AGrW14], BeLa12, Thm. 6.16, Cor. 6.17], [DHMdS12, Thm. 7.26], [DHMdS09, BedS09], [BGrW09, Sec. 2], [BGPa08, Thm. 1.29], [Pc08, Thm. 2.1], [BeLa07, Thm.2.8], [Pc01], to name a few publications. We would also like to stress that one can easily consider Robin-type boundary conditions instead of Neumann boundary conditions, see Remark 1.17. In our approach, the self-adjointness of both operators $H$ and $H^{\mathrm{D}}$ is automatically given.

The spectral relation (1.7), a consequence of the resolvent formula, extends known results for (ordinary) boundary triples to our general context (see e.g. [M10, Thm. 2.8], [BGrW09, Cor. 2.3], [Pc08, BGPa08, BrMN02], going back to ideas already contained in [Vi52] and [Gr68]). We would like to stress that our approach here allows the natural boundary operators and Dirichlet-to-Neumann operator in this context.

The family of Dirichlet-to-Neumann (sesquilinear) forms $\left(\mathfrak{l}_{z}\right)_{z \in \mathbb{C} \backslash \sigma\left(H^{\mathrm{D}}\right)}$ defined in (1.3) fulfils the following important relation
$$\frac{\mathfrak{l}_{z}(\varphi, \psi)-\mathfrak{l}_{w}(\varphi, \psi)}{z-w}=-\langle S(z) \varphi, S(\bar{w}) \psi\rangle_{\mathscr{H}}$$
for $\varphi, \psi \in \mathscr{G}^{1 / 2}$ and $z, w \in \mathbb{C} \backslash \sigma\left(H^{\mathrm{D}}\right)$ (see Theorem 2.23). In particular, for $\bar{w}=z$, this formula implies that
$$-\frac{\left(\operatorname{Im} \mathfrak{l}_{z}\right)(\varphi, \varphi)}{\operatorname{Im} z}=\|S(z) \varphi\|_{\mathscr{H}}^{2}=: \mathfrak{q}_{z}(\varphi) \geq 0$$
for $\varphi \in \mathscr{G}^{1 / 2}$ and $z \in \mathbb{C} \backslash \mathbb{R}$, i.e., $\operatorname{Im} z>0$ implies that $-\operatorname{Im}_{\mathfrak{t}} \geq 0$; We call such a family $\left(-\mathfrak{l}_{z}\right)_{z}$ a sesquilinear-form-valued Nevanlinna function.

\section*{Elliptically regular boundary pairs}

In order to relate our concept of boundary pairs with various concepts of boundary triples in the next subsection, we identify additional properties, expressed in terms of the quadratic form $\mathfrak{q}:=\mathfrak{q}-1$, respectively the Dirichlet solution operator $S:=S(-1)$ (see Definitions 3.1 and 3.15):

Definition 1.10. A boundary pair is elliptically regular (resp. positive) if $\mathfrak{q}$ is a bounded (resp. uniformly positive) quadratic form, i.e., if there is a constant $c \in(0, \infty)$ such that
$$\mathfrak{q}(\varphi):=\|S \varphi\|_{\mathscr{H}}^{2} \leq c^{2}\|\varphi\|_{\mathscr{G}}^{2} \quad\left(\text { resp. } \mathfrak{q}(\varphi) \geq c^{2}\|\varphi\|_{\mathscr{G}}^{2}\right)$$
for all $\varphi \in \mathscr{G}^{1 / 2}=\operatorname{ran} \Gamma$.
One can equivalently use the form $\mathfrak{q}_{z}$ in Definition 1.10 (with $z$-depending constant $c$ ) for some other value $z \in \mathbb{C} \backslash \sigma\left(H^{\mathrm{D}}\right)$ instead of the form $\mathfrak{q}:=\mathfrak{q}_{-1}$ for $z=-1$ (see (3.8)). A simple consequence of the above formula (1.9) is that a boundary pair is elliptically regular (resp. positive) iff $-\mathrm{Im}_{z}$ is a bounded (resp. uniformly positive) form for $\operatorname{Im} z>0$. In particular, elliptic regularity and positivity of a boundary pair can be seen from the family $\left(\mathfrak{l}_{z}\right)_{z}$ of Dirichlet-to-Neumann forms. One purpose of this article is to provide further equivalent characterisation of elliptic regularity and positivity in terms of boundary pairs (see Theorems 3.5 and 3.17).

Remark 1.11. Let us mention that the notation "elliptic regularity" is inspired by our basic example of a Laplacian with smooth boundary $Y=\partial X$ in Section 1.1. the notation relates to the fact that for elliptic regular boundary pairs, $\operatorname{dom} H^{\mathrm{D}}$ and $\operatorname{dom} H$ are both "nice" spaces, i.e., they have enough regularity in the sense that $\operatorname{dom} H^{\mathrm{D}}$ and dom $H$ are subsets of $\mathrm{H}^{2}(X)$. In particular, if $u \in \operatorname{dom} H^{\mathrm{D}}$ then the normal derivative $\Gamma^{\prime} u=\partial_{\mathrm{n}} u \upharpoonright_{Y}$ is an element of the Hilbert space $\mathscr{G}=\mathrm{L}_{2}(Y)$ (see e.g. [LiMa68]). Moreover, we have
$$\mathfrak{h}(u, h)-\left\langle H^{\mathrm{D}} u, h\right\rangle_{\mathscr{H}}=-\left\langle\left(H^{\mathrm{D}}+1\right) u, h\right\rangle_{\mathscr{H}}$$
for $h=S \varphi=S(-1) \varphi$, as $\mathfrak{h}(u, h)=-\langle u, h\rangle$ by (1.1) for $z=-1$. We can rewrite the left hand side as $\left\langle\Gamma^{\prime} u, \varphi\right\rangle_{\mathscr{G}}$, where $\Gamma^{\prime} u=\partial_{\mathrm{n}} u \upharpoonright_{Y}$ is the restriction of the normal derivative onto the boundary $Y$ and $\Gamma h=\varphi$ is the boundary value of the Dirichlet solution $h$. Substituting $u=R^{\mathrm{D}} v=\left(H^{\mathrm{D}}+1\right)^{-1} v \in \operatorname{dom} H^{\mathrm{D}}$, we obtain
$$\left\langle\Gamma^{\prime} R^{\mathrm{D}} v, \varphi\right\rangle_{\mathscr{G}}=-\langle v, S \varphi\rangle_{\mathscr{H}} .$$
hence (1.12) defines a bounded functional $\varphi \mapsto\left\langle\Gamma^{\prime} R^{\mathrm{D}} v, \varphi\right\rangle_{\mathscr{G}}=\langle v, S \varphi\rangle_{\mathscr{H}}$ with bound $\left\|\Gamma^{\prime} R^{\mathrm{D}} v\right\|_{\mathscr{G}}$ and $S$ can be extended to a bounded operator $\bar{S}: \mathscr{G} \longrightarrow \mathscr{H}$. The latter fact is equivalent with the elliptic regularity of the boundary pair (see Theorem 3.5). For an equivalent characterisation of elliptic regularity in terms of the range of $\Gamma^{\prime} R^{\mathrm{D}}$, see Remark 3.6 (i).

We would like to stress that we will show the elliptic regularity in our examples mostly by applying the definition, and not as in the previous remark. Especially for the Zaremba problem or manifolds with Lipschitz boundary (see Sections 6.3 and 6.6), the regularity of the Dirichlet operator is rather delicate, and our approach avoids questions about the operator domains almost completely.

\section*{A non-elliptically regular boundary pair: The Zaremba problem}

There are interesting examples of non-elliptically regular boundary pairs: Consider the Zaremba problem of Section 1.1 (see Section 6.6 for more details): Let $X$ be a compact Riemannian manifold with smooth boundary $\partial X$ and $Y$ a "good" proper subset of $\partial X$ (e.g. $\partial Y$ is a smooth submanifold in the manifold $\partial X$ ). The corresponding boundary pair $(\Gamma, \mathscr{G})$ (with $\mathscr{H}^{1}=\mathrm{H}^{1}(X), \Gamma f=f \upharpoonright_{Y}$ and $\mathscr{G}=\mathrm{L}_{2}(Y)$ ) is not elliptically regular: the Neumann operator of this boundary pair is the usual Neumann Laplacian on $X$ while the Dirichlet operator is the Zaremba Laplacian (Dirichlet conditions on $Y$ and Neumann conditions on $\partial X \backslash Y$ ). Functions in the domain of the Zaremba operator do not all belong to $\mathrm{H}^{3 / 2}(X)$ (a fact which we dub here "non-elliptically regular"), hence the normal derivative $\Gamma^{\prime}$ of such a function is not an element of the boundary Hilbert space $\mathscr{G}=\mathrm{L}_{2}(Y)$. By a similar argument as in Remark 1.11 in the elliptically regular case, one can then conclude that the Dirichlet solution operator cannot have a bounded extension onto $\mathscr{G} \rightarrow \mathscr{H}$, and hence the boundary pair is not elliptically regular (see also Remark 3.6 (i)).

We would like to stress that this example cannot be treated with the quasi-boundary triple method developed by Behrndt and Langer [BeLa07] (see Definition 1.18), but our method still gives a weaker version of Theorem 1.5 (see Theorems 4.3 and 4.11).

There is also an interesting equivalent character of "elliptic regularity" of a boundary pair in terms of an optimal convergence speed for Robin-type resolvents in the works of Brasche et al BrD05, BABr08, BBABr11 (see Remark 3.7 (ii)). Elliptic regularity in a slightly different context appeared also in the works of Arlinskii (Ar00, Ar12, see Remark 3.7 (i)).

\subsection*{1.3 Purpose of this article and outlook}

Let us explain here why we believe that our approach is useful:
\begin{itemize}
\item[-] Boundary pairs give a simple and unified language bringing together very different approaches such as boundary triples, Weyl-Titchmarsh functions, Jacobi operators, elliptic boundary value problems (even with low regularity as for the Zaremba problem or with non-smooth Robin boundary conditions), Dirichlet-to-Neumann operators, boundary conditions for differential form Laplacians, non-negative form perturbations, Dirichlet forms, discrete Laplacians;
\item[-] The concept of boundary pairs uses only very little information on the model, namely only quadratic form domains, but still allows to develop a reasonable spectral analysis of the problem. In particular, one can avoid discussions about operator domains and the rather delicate analysis of regularity on Lipschitz domains or for the Zaremba problem.
\item[-] To our knowledge, the elliptic regularity condition for boundary pairs in Definition 1.10 and its consequences (see Theorem 3.10) have not yet been recognised as an important feature.
\item[-] The form-based approach fits perfectly into the two-Hilbert space convergence scheme developed in [P12, Ch. 4]; especially in the case of parameter-depending spaces such as manifolds shrinking to a metric graph.
\item[-] We see our approach as a starting point for ongoing research, and this article is meant to provide the basic tools for the following aspects:
\begin{itemize}
\item[-] We provide conditions under which a boundary pair fits into existing concepts such as boundary triples (see Section 1.4 below); and in what sense it is more general than existing concepts.
Moreover, we believe that the elliptic regularity and positivity expressed as in Definition 1.10 will lead to further fruitful research.
\item[-] As an example of convergence of operators in different Hilbert spaces and boundary pairs, we mention the forthcoming publication on graph-like manifolds [BeP]). Similarly, we will use these techniques to show convergence of Dirichlet-Laplacians on domains shrinking to a graph.
\item[-] Our approach allows an easy decomposition or coupling technique (see Section 5.2 or [P12, Sec. 3.9]), expressing global objects such as the spectrum or resolvent in terms of local building blocks if the space can be decoupled according to a graph structure (see also the example in Section 6.5).
\item[-] Given a form-valued Nevanlinna function $\left(-\mathfrak{l}_{z}\right)_{z \in \mathbb{C} \backslash[0, \infty)}$, reconstruct the boundary pair up to unitary equivalence in the spirit of [LT77] and [DHMdS12] (uniqueness will only be possible if $H \cap H^{\mathrm{D}}$ is simple, i.e., if $H \cap H^{\mathrm{D}}$ has no non-trivial self-adjoint part).
\item[-] Relate the concept with the theory of Dirichlet forms (cf. [BBABr11] and references therein); assuming that $\mathscr{H}=\mathrm{L}_{2}(X)$ and $\mathscr{G}=\mathrm{L}_{2}(Y)$, and $\Gamma$ is compatible with the (order-theoretic) lattice structure of the $\mathrm{L}_{2}$-spaces.
\end{itemize}
\end{itemize}

It is clear that such a general concept cannot avoid deep analysis on certain classes of problems such as elliptic regularity questions for partial differential operators ( "There is no free lunch . . . "). But we believe that we can provide interesting new links between very different subjects; e.g. the property of a boundary pair to be elliptically regular is equivalent to an optimal convergence rate for Robin-type resolvents as mentioned earlier (see also Remark 3.7 (ii)).

\subsection*{1.4 Relation with boundary triples and similar concepts}

The concept of boundary pairs associated with a non-negative quadratic form is in some sense a generalisation of the concept of boundary triples (also called boundary value spaces) associated with a closed operator $H^{\text {max }}$. We will provide the details of the following results in a forthcoming publication, see [P]. Nevertheless, we believe that it is useful to state the concepts and results already here.

Let $(\Gamma, \mathscr{G})$ be a boundary pair associated with a quadratic form $\mathfrak{h}$. We define its minimal operator by $H^{\text {min }}:=$ $H^{\mathrm{D}} \cap H$. We assume for now on in this section that $H^{\text {min }}$ is densely defined (i.e., $\operatorname{dom} H^{\mathrm{D}} \cap \operatorname{dom} H$ is dense in $\mathscr{H}$ ). In this case, the maximal operator $H^{\text {max }}$ defined by $H^{\text {max }}:=\left(H^{\text {min }}\right)^{*}$ is again a (single-valued) operator.

Definition 1.13 (cf. P12, Def. 3.4.3]). We say that $\left(\Gamma, \Gamma^{\prime}, \mathscr{G}\right)$ is a boundary triple associated with a quadratic form $\mathfrak{h}$ if $(\Gamma, \mathscr{G})$ is a boundary pair associated with $\mathfrak{h}$ such that $H^{\text {min }}=H^{\mathrm{D}} \cap H$ is densely defined, and if $\Gamma^{\prime}: \mathscr{W} \longrightarrow \mathscr{G}$ is a bounded operator, where $\mathscr{W}$ is dense in $\mathscr{H}^{1}=\operatorname{dom} \mathfrak{h}$ and continuously embedded, such that the (first) Green's (first) identity
$$\mathfrak{h}(f, g)=\left\langle H^{\max } f, g\right\rangle_{\mathscr{H}}+\left\langle\Gamma^{\prime} f, \Gamma g\right\rangle_{\mathscr{G}}$$
holds for all $f \in \mathscr{W}$ and $g \in \mathscr{H}^{1}$. We also call $\left(\Gamma, \Gamma^{\prime}, \mathscr{G}\right)$ a boundary triple associated with $(\Gamma, \mathscr{G})$ (and $\mathfrak{h}$ ). We say that the boundary triple is maximal if the space $\mathscr{W}$ cannot be enlarged without violating the boundedness of $\Gamma^{\prime}$ or the validity of Green's identity in $\mathscr{G}$.

For a given boundary pair $(\Gamma, \mathscr{G})$ associated with $\mathfrak{h}$ such that $H^{\text {min }}$ is densely defined, there always exists an associated maximal boundary triple $\left(\Gamma, \Gamma^{\prime}, \mathscr{G}\right)$ (similar as in [Ar00, Def. 2.1] or [Ar12, Def. 3.12]). We will prove this and related results in P.

In the manifold example above, (1.14) is the usual Green's (first) identity where $\Gamma^{\prime}$ is the normal derivative restricted to the boundary. A simple consequence of Green's identity is a justification of the name "Dirichlet-to-Neumann": Let $z \in \mathbb{C} \backslash \sigma\left(H^{\mathrm{D}}\right)$ and let $\varphi$ be sufficiently "regular" in the sense that $h=S(z) \varphi \in \mathscr{W}$, then
$$\mathfrak{l}_{z}(\varphi, \psi)=(\mathfrak{h}-z \mathfrak{l})(S(z) \varphi, g)=\left\langle\left(H^{\max }-z\right) h, g\right\rangle+\left\langle\Gamma^{\prime} h, \Gamma g\right\rangle_{\mathscr{G}}=\left\langle\Gamma^{\prime} h, \psi\right\rangle_{\mathscr{G}},$$
where $g=S(-1) \psi$ (or any other function $g \in \mathscr{H}^{1}$ with $\Gamma g=\psi$ ). Note that as $\mathscr{N}^{1}(z) \subset \operatorname{ker}\left(H^{\text {max }}-z\right)$, we have $\left(H^{\text {max }}-z\right) h=0$. In particular, we have shown that $\varphi$ is in the domain of the associated Dirichlet-to-Neumann operator, and
$$\Lambda(z) \varphi=\Gamma^{\prime} h,$$
i.e., the Dirichlet-to-Neumann operator associates to a boundary value $\varphi$ the "normal derivative" $\Gamma^{\prime} h$ of the solution of the Dirichlet problem $h=S(z) \varphi$.

Remark 1.17. The choice of "Neumann" and "Dirichlet" conditions for boundary pairs is not as restrictive as it looks like at first glance: one can replace the quadratic form $\mathfrak{h}$ by $\mathfrak{h}_{L}$, where $\mathfrak{h}_{L}(u):=\mathfrak{h}(u)+\langle L \Gamma u, \Gamma u\rangle$ for some suitable operator $L$ in $\mathscr{G}$ (e.g. bounded). It can then be shown that $(\Gamma, \mathscr{G})$ is also a boundary pair associated with $\mathfrak{h}_{L}$ (for suitable operators $L$ ), and that the associated Neumann operator is of Robin-type, i.e., functions in its domain fulfil $\Gamma^{\prime} u+L \Gamma u=0$, while the Dirichlet operator is the same as before (see Section 5.1).

\section*{Quasi- and generalised boundary triples}

Let us now shortly review different concepts of boundary triples and relate them to boundary pairs. We will provide the proofs in a forthcoming publication, see [P]. For a recent treatment of (quasi-)boundary triples and related concepts we refer to the nice surveys [DHMdS12] and [BeLa12] and the references therein (see also [Sch12, BGPa08, BeLa07, DHMdS06, BrMN02, Ar96, DM95). Note that the following concepts are formulated on the operator level:

Definition 1.18. Let $H^{\text {min }}$ be a closed, densely defined and symmetric operator in $\mathscr{H}$ and set $H^{\text {max }}=\left(H^{\text {min }}\right)^{*}$.
\begin{itemize}
\item[i.] A triple $\left(\Gamma_{0}, \Gamma_{1}, \mathscr{G}\right)$ is a quasi-boundary triple associated with $H^{\max }$ (see BeLa07, Def. 2.1] or BeLa12, Def. 6.10]) if there is a subspace $\mathscr{W}$ of $\operatorname{dom} H^{\text {max }}$, dense in $\operatorname{dom} H^{\text {max }}$ (with its graph norm), such that
\begin{itemize}
\item[a)] $\left(\Gamma_{0}, \Gamma_{1}\right): \mathscr{W} \longrightarrow \mathscr{G} \oplus \mathscr{G}$ has dense range, where $\left(\Gamma_{0}, \Gamma_{1}\right) f:=\left(\Gamma_{0} f, \Gamma_{1} f\right)$ ("joint dense range").
\item[b)] $H_{0}:=H^{\text {max }} \upharpoonright_{\text {ker } \Gamma_{0}}$ is self-adjoint ("self-adjointness"),
\item[c)] Green's (second) identity
$$\left\langle H^{\max } f, g\right\rangle_{\mathscr{H}}-\left\langle f, H^{\max } g\right\rangle_{\mathscr{H}}=\left\langle\Gamma_{0} f, \Gamma_{1} g\right\rangle_{\mathscr{G}}-\left\langle\Gamma_{1} f, \Gamma_{0} g\right\rangle_{\mathscr{G}}$$
holds for $f, g \in \mathscr{W}$.
\end{itemize}
\item[ii.] The triple $\left(\Gamma_{0}, \Gamma_{1}, \mathscr{G}\right)$ is called a generalised boundary triple associated with $H^{\text {max }}$ (in the sense of DM95, Def. 6.1]) if it fulfils Green's (second) identity (1.19) and if the joint dense range condition (ia) is replaced by the surjectivity of $\Gamma_{0}$, i.e., by $\Gamma_{0}(\mathscr{W})=\mathscr{G}$.
\item[iii.] The triple $\left(\Gamma_{0}, \Gamma_{1}, \mathscr{G}\right)$ is (here) called an ordinary boundary triple associated with $H^{\text {max }}$ if it fulfils Green's (second) identity (1.19), if $\mathscr{W}=\operatorname{dom} H^{\max }$ and if the "joint dense range" condition (ia) is replaced by the "joint surjectivity" condition, i.e., by $\left(\Gamma_{0}, \Gamma_{1}\right)(\mathscr{W})=\mathscr{G} \oplus \mathscr{G}$.
\end{itemize}

A generalised boundary triple is a quasi-boundary triple (see BeLa07, Cor. 3.7] and DM95, Lem. 6.1]), and obviously, an ordinary boundary triple is a generalised and quasi-boundary triple. We will prove the following converse results on boundary pairs with boundary triples in [P]:

Theorem 1.20 ([P]). Let $(\Gamma, \mathscr{G})$ be a boundary pair associated with $\mathfrak{h}$ and let $\left(\Gamma, \Gamma^{\prime}, \mathscr{G}\right)$ be its maximal associated boundary triple (as in Definition 1.13). Then the following holds:
\begin{itemize}
\item[i.] The boundary pair $(\Gamma, \mathscr{G})$ is elliptically regular iff $\left(\Gamma \upharpoonright_{\mathscr{W}}, \Gamma^{\prime}, \mathscr{G}\right)$ is a quasi-boundary triple associated with $H^{\text {max }}$;
\item[ii.] The boundary pair $(\Gamma, \mathscr{G})$ is bounded iff $\left(\Gamma \upharpoonright_{\mathscr{W}}, \Gamma^{\prime}, \mathscr{G}\right)$ is a generalised boundary triple associated with $H^{\text {max }}$.
\item[iii.] The boundary pair $(\Gamma, \mathscr{G})$ is bounded and positive iff $\left(\Gamma \upharpoonright_{\mathscr{W}}, \Gamma^{\prime}, \mathscr{G}\right)$ is an ordinary boundary triple.
\end{itemize}

In [DHMdS06], the more general notation of boundary relation has been introduced (basically, multi-valued operators and boundary maps are allowed). One of the results of [DHMdS06] states a characterisation of boundary relations by their Nevanlinna "functions" $-\Lambda(\cdot)$ (see also the survey [DHMdS12]). In particular, generalised boundary triples have a Nevanlinna function $-\Lambda(\cdot)$ with values in $\mathscr{B}(\mathscr{G})$ (the space of bounded operators) such that $-\operatorname{Im} \Lambda(z)$ is injective, while ordinary boundary triples have again values in $\mathscr{B}(\mathscr{G})$ and uniformly positive operators $-\operatorname{Im} \Lambda(z)$ (so-called uniformly strict Nevanlinna functions), see DHMdS06 for more such characterisations. One can now characterise elliptically regular boundary pairs in terms of $\Lambda(\cdot)$ and reconstruct $(\Gamma, \mathscr{G})$ from it in the spirit of [LT7] (see the outlook list of Section 1.3 above).

To summarise: Our concept of boundary pairs is more general as it includes non-elliptically regular boundary pairs; this concept is not covered by quasi-boundary triples. On the other hand, our concept is only suitable for non-negative operators $H$ and $H^{\mathrm{D}}$ (although there is a natural extension of the theory to semi-bounded or sectorial operators).

Let us illustrate the different properties of boundary pairs and its relation to boundary pairs in a tabular: we also refer to (classes of) examples showing that the above properties of boundary pairs are all independent except the following: A boundary pair $(\Gamma, \mathscr{G})$ with finite-dimensional boundary space is automatically bounded (i.e., $\operatorname{ran} \Gamma=$ $\Gamma\left(\mathscr{H}^{1}\right)=\mathscr{G}$ ) and positive; and a bounded boundary pair is automatically elliptically regular.

\begin{tabular}[t]{|l|l|l|l|l|l|l|l|}
\hline \multicolumn{4}{|l|}{boundary pair is} & \multirow[t]{2}{*}{Examples} & \multicolumn{3}{|c|}{ass. boundary triple is} \\
\hline fin & bdd & ell & pos & & o-bd3 & g-bd3 & q-bd3 \\
\hline ✓ & ✓ & ✓ & ✓ & Section 6.1 (Sturm-Liouville) & ✓ & ✓ & ✓ \\
\hline × & ✓ & ✓ & ✓ & metric graphs with infinitly many vertices, see [P12] & ✓ & ✓ & ✓ \\
\hline × & ✓ & ✓ & × & Example [6.29] modified manifold example & × & ✓ & ✓ \\
\hline × & × & ✓ & ✓ & Example 6.12 (Jacobi) & × & × & ✓ \\
\hline × & × & ✓ & × & Sections 6.3 and 6.5, Theorem 6.36 (mfds) & × & × & ✓ \\
\hline × & × & × & ✓ & Example 6.13 (Jacobi) & × & × & × \\
\hline × & × & × & × & Theorem 6.39 (Zaremba) & × & × & × \\
\hline
\end{tabular}
✓ - yes; $\boldsymbol{X}$ - no. fin: finite dimensional boundary space $\mathscr{G}$; bdd: bounded boundary pair $(\operatorname{ran} \Gamma=\mathscr{G})$; ell: elliptically regular boundary pair; pos: positive boundary pair. o-bd3: the associated boundary triple is an ordinary boundary triple; g-bd3: ... generalised boundary triple; q-bd3: ... quasi-boundary triple.

\subsection*{1.5 Extension theory and related other works}

Let us briefly comment on other concepts, in particular, the concept of extension theory: the characterisation of all possible (self-adjoint) extensions of a given symmetric operator.

\section*{Grubb's extension theorem via forms}

There is a close relation of our form approach with extension theory, especially for non-negative operators: Grubb proved in [Gr70, Sec. 1] that all non-negative and self-adjoint extensions of a minimal, closed, uniformly positive operator $H^{\text {min }}$ lie in between the Friedrichs extension $H^{\mathrm{D}}$ (defined as the operator associated with the closure of the quadratic form $\mathfrak{h}^{\mathrm{D}}(f):=\left\langle H^{\text {min }} f, f\right\rangle$ ) and the so-called Krein or soft extension defined via the quadratic form
$$\operatorname{dom} \mathfrak{h}^{\mathrm{K}}:=\operatorname{dom} \mathfrak{h}^{\mathrm{D}} \dot{+} \operatorname{ker} H^{\max }, \quad \mathfrak{h}^{\mathrm{K}}(u):=\mathfrak{h}^{\mathrm{D}}\left(u^{\mathrm{D}}\right),$$
where $u^{\mathrm{D}}$ is the projection of $u \in \operatorname{dom} \mathfrak{h}^{\mathrm{K}}$ onto dom $\mathfrak{h}^{\mathrm{D}}$ along $\operatorname{ker} H^{\max }\left(H^{\max }:=\left(H^{\min }\right)^{*}\right)$. The associated operator $H^{\mathrm{K}}$ acts on $\operatorname{dom} H^{\mathrm{K}}=\operatorname{dom} H^{\text {min }} \dot{+} \operatorname{ker} H^{\text {max }}$ as $H^{\mathrm{K}} u=H^{\text {min }} u^{\mathrm{D}}$ (a result of Krein, see Kr47, Thm. 14]) and is self-adjoint and non-negative.

To be more precise, Grubb's result is as follows (cf. [Gr70, Cor. 1.3]): If $\mathfrak{h}$ is a closed non-negative quadratic form in $\mathscr{H}$ and $\mathfrak{h} \upharpoonright_{\text {dom }} \mathfrak{h}^{\mathrm{D}}=\mathfrak{h}^{\mathrm{D}}$, such that its domain lies in between $\operatorname{dom} \mathfrak{h}^{\mathrm{D}}$ and $\operatorname{dom} \mathfrak{h}^{\mathrm{K}}$ and $\mathfrak{h}^{\mathrm{K}}(u) \leq \mathfrak{h}(u)$ for all $u \in \operatorname{dom} \mathfrak{h}$, then the associated operator $H$ is an extension of $H^{\text {min }}\left(H^{\text {min }} \subset H \subset H^{\text {max }}\right)$, and all positive extensions of $H^{\text {min }}$ appear in this way. One can also characterise the extension in terms of the quadratic form $\mathfrak{t}$, the restriction of $\mathfrak{h}$ to the space $\mathrm{ker} H^{\mathrm{max}}$. This form then corresponds to our family of Dirichlet-to-Neumann forms at $z=0$.

There are many more approaches to self-adjoint extensions of positive closed operators, see e.g. [M92, AS80, AN70, Bir56, Vi52, Kr47.

Grubb also contributed to the Zaremba (mixed) boundary problem in [Gr11]; she provides Krein-type formula (with the Dirichlet Laplacian as a reference operator, hence it is in our elliptically regular setting, see Theorem 6.36); and also Weyl-type asymptotics for the resolvent difference).

\section*{Arlinskii's boundary pairs}

The notion of boundary pair appears also in works of (see also the survey [Ar12] and references therein), but with the Krein extension as Neumann operator and the additional condition that $\operatorname{ran} \Gamma=\mathscr{G}$. In other words, given a minimal operator $H^{\text {min }}$, Arlinskii defines a boundary pair $(\Gamma, \mathscr{G})$ associated with $\mathfrak{h}^{\mathrm{K}}$ such that $\Gamma\left(\operatorname{dom} \mathfrak{h}^{\mathrm{K}}\right)=\mathscr{G}$, i.e., the boundary pair is bounded in our notation. Arlinskii deals with sectorial operators, and not with non-negative operators, as we do. In our opinion, Arlinskii is mainly interested in characterising all possible variational extensions of the associated minimal operator for sectorial operators (we just mentioned Grubb's result for non-negative operators
above [Gr70]). Arlinskii [Ar99] also associates a boundary triple with a boundary pair in the same spirit as we do in Section 1.4.

Lyantse and Storozh LySt83 use a similar notion of boundary pairs for operators corresponding basically to bounded boundary pairs in our notation. There is another approach for first order systems in [Mo12]. Malamud and Mogilevskii [MMo02] discuss the extension theory for dual pairs of operators or even relations and also provide a Krein-type formula for the resolvents.

\section*{Posilicano's approach}

Posilicano [Pc08] (see also [Pc04, Pc01]) considers (in our notation) a self-adjoint extension $H^{\mathrm{D}}$ and a bounded operator $\Gamma^{\prime}: \operatorname{dom} H^{\mathrm{D}} \longrightarrow \mathscr{G}$ (dom $H^{\mathrm{D}}$ with its graph norm) which is surjective and has dense kernel. He then describes all self-adjoint extensions of the associated minimal operator $H^{\text {min }}:=H^{\mathrm{D}} \upharpoonright_{\text {ker } \Gamma^{\prime}}$ via a Krein-type formula. He also applies his concept to Laplacians on open subsets $X \subset \mathbb{R}^{n}$ with smooth boundary, but the surjectivity condition on $\Gamma^{\prime}$ enforces $\mathscr{G}=\mathrm{H}^{1 / 2}(\partial X)$. Other results on Krein-type resolvent formulae are also considered in AGrW14, DHMdS09, BedS09, Pc01.

\section*{Arendt's and ter Elst's $\Gamma$-elliptic forms}

Arendt and ter Elst [AtE12a] define a generalised notion for sesquilinear forms and associated operators, using an operator playing the role of our boundary operator $\Gamma: \mathscr{H}^{1} \longrightarrow \mathscr{G}$. Namely, they say that a sesquilinear form $\mathfrak{a}$ is is $\Gamma$-elliptic if there exist $\alpha>0$ and $\omega \in \mathbb{R}$ such that
$$\operatorname{Re} \mathfrak{a}(u)+\omega\|\Gamma u\|_{\mathscr{G}}^{2} \geq \alpha\|u\|_{\mathscr{H}^{1}}^{2}$$
holds for all $u \in \mathscr{H}^{1}$.
To such a $\Gamma$-elliptic form $\mathfrak{a}$, one can associate an operator $A$ on $\mathscr{G}$ by setting $\varphi \in \operatorname{dom} A$ and $A \varphi=\psi$ iff there exists $u \in \mathscr{H}^{1}$ such that $\Gamma u=\varphi$ and $\mathfrak{a}(u, v)=\langle\psi, \Gamma v\rangle_{\mathscr{G}}$ for all $v \in \mathscr{H}^{1}$. We say that $A$ is the operator associated with $\left(\mathscr{H}^{1}, \Gamma, \mathfrak{a}\right)$.

We can apply this definition in the following way: Let $(\Gamma, \mathscr{G})$ be a boundary pair associated with $\mathfrak{h}$. Set now $\mathfrak{a}=\mathfrak{h}-z \mathbf{1}$, then it is not difficult to see that the operator associated with $\left(\mathscr{H}^{1}, \Gamma, \mathfrak{h}-z \mathbf{1}\right)$ is the Dirichlet-to-Neumann operator $\Lambda(z)$.

The notation " $\Gamma$-elliptic" does not refer to the Hilbert space $\mathscr{H}$, and hence, there is no direct relation to our notion of "elliptic regularity" in the sense of Definition 1.10, but it can easily be seen that if $\operatorname{Re} z<0$, then $\mathfrak{h}-z \mathbf{1}$ is $\Gamma$-elliptic (with $\alpha=\min \{1,-\operatorname{Re} z\}$ and $\omega=0$ ). On the other hand, if $(\Gamma, \mathscr{G})$ is an elliptically regular boundary pair, and if $0 \notin \sigma\left(H^{\mathrm{D}}\right)$, then $\mathfrak{h}$ is $\Gamma$-elliptic.

Arendt and ter Elst use this abstract concept to define a Dirichlet-to-Neumann operator even on very rough domains, see [AtE11], assuming e.g. that $\Gamma$ is only a closed map in $\mathscr{H}^{1} \rightarrow \mathscr{G}$. They also relate the concept with operator semi-groups (see [AtE12b]). In an older paper, Greiner considers perturbations of semi-groups by boundary conditions in the setting of Banach spaces (see [Gre87]).

\section*{Brasche et al's non-negative form perturbations}

A different approach using the notion of Dirichlet forms is used in the works of Brasche et al BrD05, BABr08, BBABr11, see also [Pc01, Ex. 3.6]). Their concept is called non-negative form perturbations and can equivalently be given (in our notation) by a non-negative closed quadratic form $\mathfrak{h}$ in $\mathscr{H}$ with domain $\mathscr{H}^{1}:=\operatorname{dom} \mathfrak{h}$, an auxiliary Hilbert space $\mathscr{G}$ and an identification operator $\Gamma$, closed as operator $\mathscr{H}^{1} \rightarrow \mathscr{G}$ and densely defined in $\mathscr{H}^{1}$ with dense range ran $\Gamma$ ([BBABr11, Ex. 2.1 and Lem. 2.2]). It is more general than our concept since $\Gamma$ is not assumed to be bounded as operator $\mathscr{H}^{1} \rightarrow \mathscr{G}$ and since $\operatorname{ker} \Gamma$ is not assumed to be dense in $\mathscr{H}$ (we have one example where we also drop the latter density condition, see Section 6.7). We would like to stress that Brasche et al only consider (what we call) the Dirichlet-to-Neumann operator $\Lambda=\Lambda(-1)$ at $z=-1$ and not families of Dirichlet-to-Neumann operators $(\Lambda(z))_{z}$ as we do.

One of the main examples in [BBABr11] is the Laplacian on $\mathbb{R}$ with infinitely many delta interactions on it (in other words, Robin-type perturbations of the Neumann Laplacian on $\mathbb{R}$, see Remark 3.7 (ii)), a case also treated in detail in [KoM10] (see Remark 6.6 and also [MSch12, CMPc13, BeLaL13] for other recent applications of boundary triple methods to delta-type Schrödinger operators). Brasche et al also introduce an interesting equivalent characterisation of "elliptic regularity" of a boundary pair in terms of an optimal convergence speed for Robin-type resolvents in the works of Brasche et al BrD05, BABr08, BBABr11 (see again Remark 3.7 (ii)).

\section*{Applications of boundary triples to elliptic boundary value problems}

There have been many attempts to apply the concept of boundary triples to elliptic boundary value problems on $X$. Most attempts try to keep the concept of boundary triples (namely the "joint surjectivity condition" of Definition 1.18 (iii)), for example by "regularising" the boundary maps by applying some isomorphism $\mathrm{H}^{1 / 2}(\partial X)$ onto $\mathrm{L}_{2}(\partial X)$ (e.g. the square root of the Dirichlet-to-Neumann map $\Lambda^{1 / 2}$ ), see also Section 5.4 for an abstract "regularisation" for boundary pairs. This approach has been used e.g. in [M10, BGrW09, Pa06]).

Abstract formulations of elliptic boundary value problems have already been considered by Grubb in [Gr68, Gr70] where she considers self-adjoint extensions of non-negative (and more general) operators, being elliptic on a subset $X$ of $\mathbb{R}^{n}$ with smooth boundary $\partial X$. Recently, Gesztesy and Mitrea [GeMi11] (see also [GeMi08, GeMi09]) provided a detailed analysis of all extensions of Laplacians on a subclass of Lipschitz domains, also providing Krein-type formulae as in (1.6). They are not using the language of boundary triples, but their results could easily be embedded e.g. in the concept of boundary pairs or quasi-boundary triples. The latter has been successfully applied to elliptic boundary value problems, even in the setting of Lipschitz domains in $\mathbb{R}^{n}$, see [BeM14] and the references therein. There are similar results by Grubb [Gr08], providing Krein-type resolvent formulae also for certain non-smooth domains, using pseudo-differential boundary operator methods adopted to the non-smooth case. Ryzhov Ry07 uses a similar concept as boundary triples (in a weaker version) and also defines what we call Dirichlet-to-Neumann operator. He assumes what we call elliptic regularity (see [Ry07, Prp. 1.16 (2)]).

\subsection*{1.6 Structure of this article}

Section 2 contains the basic notion of a boundary pair, the Dirichlet solution operator and the Dirichlet-to-Neumann operator and properties related with these operators. In Section 3 we find additional properties of boundary pairs needed in order to prove certain Krein-type resolvent formulae and spectral relations in Section 4. Section 5 consists of boundary pairs constructed from others, such as the Robin-type perturbation in Section 5.1 and coupled boundary pairs in Section 5.2, and a construction how to turn an unbounded boundary pair in a bounded one in Section 5.4. In Section 6 we provide many examples including Laplacians on intervals, Jacobi operators, Laplacians on sets with Lipschitz boundary, a Dirichlet-to-Neumann operator supported on an embedded metric graph, the Zaremba problem and discrete Laplacians.

\subsection*{1.7 Acknowledgements}

The author is indebted to many colleagues for helpful discussions and comments while working on this project and for carefully reading earlier versions. These thanks go especially to Yury Arlinskii, Jussi Behrndt, Gerd Grubb, Matthias Langer, Mark Malamud, Marco Marletta, Till Micheler, Jonathan Rohleder, Karl-Michael Schmidt and Michael Strauss. The author acknowledges the financial support of the SFB 647 "Space - Time - Matter" while the author was at the Humboldt University at Berlin and first ideas for this article were developed. The author enjoyed the hospitality at Cardiff University and thanks for the financial support given by the Marie Curie grant "COUPLSPEC". Last but not least the author would like to thank the referees for many useful comments on the article.

\section*{2 Boundary pairs associated with quadratic forms}

\subsection*{2.1 Preliminaries: quadratic and sesquilinear forms, scales of Hilbert spaces}

In this article, $\mathscr{H}, \mathscr{G}$ etc. denote Hilbert spaces with norm and inner product denoted by $\|\cdot\|_{\mathscr{H}},\langle\cdot, \cdot\rangle_{\mathscr{H}}$ etc. Let $\mathscr{H}^{1}$ be a subspace of $\mathscr{H}$ with another inner product $\langle\cdot, \cdot\rangle_{\mathscr{H}^{1}}$, such that the inclusion $\mathscr{H}^{1} \hookrightarrow \mathscr{H}$ is bounded. A sesquilinear form $\mathfrak{h}: \mathscr{H}^{1} \times \mathscr{H}^{1} \longrightarrow \mathbb{C}$ is a map linear in its first and anti-linear in its second argument. A sesquilinear form determines a quadratic form by $\mathfrak{h}(u):=\mathfrak{h}(u, u)$ (denoted by the same symbol), its domain is denoted by dom $\mathfrak{h}=\mathscr{H}^{1}$. A quadratic form uniquely determines its associated sesquilinear form $\mathfrak{h}: \mathscr{H}^{1} \times \mathscr{H}^{1} \longrightarrow \mathbb{C}$ by the polarisation identity $\mathfrak{h}(u, v):=\sum_{k=0}^{3} \mathrm{i}^{k} \mathfrak{h}\left(u+\mathrm{i}^{k} v\right)$. Therefore, we will mostly speak of "forms" in the sequel, meaning either "quadratic form" or "sesquilinear form".

A form is called non-negative resp. (uniformly) positive if $\mathfrak{h}(u) \geq 0$ resp. $\mathfrak{h}(u) \geq c\|u\|_{\mathscr{H}}^{2}$ for all $u \in \operatorname{dom} \mathfrak{h}=\mathscr{H}^{1}$ and some $c>0$. We sometimes write 1 for the form $\mathbf{\imath}(u):=\|u\|_{\mathscr{H}}^{2}$. A non-negative form is called closed if the norm defined by
$$\|u\|_{\mathfrak{h}}^{2}:=\mathfrak{h}(u)+\|u\|_{\mathscr{H}}^{2}$$
is equivalent with the norm on $\mathscr{H}^{1}$, i.e., if $\mathscr{H}^{1}$ is a Hilbert space w.r.t. the norm $\|\cdot\|_{\mathfrak{h}}$.

The adjoint $\mathfrak{a}^{*}$ of a form $\mathfrak{a}$ is defined by $\mathfrak{a}^{*}(\varphi, \psi):=\overline{\mathfrak{a}(\psi, \varphi)}$. The real resp. imaginary part of a form $\mathfrak{a}$ is defined as $\operatorname{Re} \mathfrak{a}:=\frac{1}{2}\left(\mathfrak{a}+\mathfrak{a}^{*}\right)$ resp. Im $\mathfrak{a}:=\frac{1}{2 \mathfrak{i}}\left(\mathfrak{a}-\mathfrak{a}^{*}\right)$. Let $D$ be an open subset of $\mathbb{C}$ invariant under complex conjugation. A family $\left(\mathfrak{l}_{z}\right)_{z \in D}$ of sesquilinear forms is called symmetric, if $\mathfrak{l}_{z}^{*}=\mathfrak{l}_{\bar{z}}$.

If $\mathfrak{h}$ is a closed, non-negative quadratic form, then there is a unique self-adjoint, non-negative operator $H$ defined for those $u \in \mathscr{H}$ such that there is $v \in \mathscr{H}$ with $\mathfrak{h}(u, w)=\langle v, w\rangle_{\mathscr{H}}$ for all $w \in \operatorname{dom} \mathfrak{h}$, and we set $H u:=v$. We also call $H$ the strong operator associated with $\mathfrak{h}$.

A self-adjoint, non-negative operator defines a scale of Hilbert spaces $\mathscr{H}^{k}:=\operatorname{dom}(H+1)^{k / 2}$ with norm $\|u\|_{\mathscr{H}^{k}}:=$ $\left\|(H+1)^{k / 2} u\right\|$ for $k \geq 0$ such that $\operatorname{dom} \mathfrak{h}=\mathscr{H}^{1}$. For negative $k$, we set $\mathscr{H}^{-k}:=\left(\mathscr{H}^{k}\right)^{*}$, where $(\cdot)^{*}$ refers to the pairing induced by the inner product of $\mathscr{H}$. In particular, we can interpret $\mathscr{H}^{-k}$ as the completion of $\mathscr{H}$ with respect to the norm $\|u\|_{\mathscr{H}-k}=\left\|(H+1)^{-k / 2} u\right\|$; for details on scales of Hilbert spaces, see [P12, Sec. 3.2]. We sometimes use the notation $A^{k \rightarrow m}$ (or similar ones) to indicate that $A: \mathscr{H}^{k} \longrightarrow \mathscr{H}^{m}$ is a bounded operator. In this sense, $H^{k \rightarrow k-2}$ is the extension/restriction of $H$, and a bounded operator. Especially, if $k=1$, we write $\breve{H}:=H^{1 \rightarrow-1}$, called the weak operator associated with $\mathfrak{h}$, and defined by $(H u) v:=\mathfrak{h}(u, v)$. There is a very nice summary about these facts in [GeMi08, App. B].

Finally, we denote by $\mathscr{H}=\mathscr{H}_{1} \dot{+} \mathscr{H}_{2}$ the topological sum of $\mathscr{H}_{1}$ and $\mathscr{H}_{2}$, i.e., the sum is direct (but not necessarily orthogonal), and $\mathscr{H}_{1}, \mathscr{H}_{2}$ are closed in $\mathscr{H}$.

\subsection*{2.2 Boundary pairs, Dirichlet solution operators and Dirichlet-to-Neumann operators}

We start with our basic object, using only quadratic form domains for the moment.
Definition 2.2. Let $\mathfrak{h}$ be a closed non-negative and densely defined quadratic form in the Hilbert space $\mathscr{H}$ with domain $\mathscr{H}^{1}:=\operatorname{dom} \mathfrak{h}$. We endow $\mathscr{H}^{1}$ with its natural norm given by (2.1). Moreover, let
$$\Gamma: \mathscr{H}^{1} \longrightarrow \mathscr{G}$$
be a bounded map, where $\mathscr{G}$ is another Hilbert space. We denote the norm of the operator $\Gamma$ by $\|\Gamma\|_{1 \rightarrow 0}$.
\begin{itemize}
\item[i.] We say that $(\Gamma, \mathscr{G})$ is an (ordinary) boundary pair (or $\Gamma$ is a boundary map) associated with the quadratic form $\mathfrak{h}$ if the following conditions are fulfilled:
\begin{itemize}
\item[a)] $\mathscr{H}^{1, \mathrm{D}}:=\operatorname{ker} \Gamma$ is dense in $\mathscr{H}$.
\item[b)] $\mathscr{G}^{1 / 2}:=\operatorname{ran} \Gamma$ is dense in $\mathscr{G}$.
\end{itemize}
\end{itemize}
If the first condition is not fulfilled, i.e., if $\operatorname{ker} \Gamma$ is not dense in $\mathscr{H}$ then we say that the boundary space is large in $\mathscr{H}$ or shortly, that $(\Gamma, \mathscr{G})$ is a generalised boundary pair.
\begin{itemize}
\item[ii.] If $\mathscr{G}^{1 / 2} \subsetneq \mathscr{G}$ (i.e., if the boundary map $\Gamma$ is not surjective), then we call the boundary pair $(\Gamma, \mathscr{G})$ unbounded. Otherwise, if the boundary map is surjective, then we call the boundary pair bounded.
\item[iii.] We call the self-adjoint and non-negative operator $H$ associated with $\mathfrak{h}$ (see Ka66, Thm. VI.2.1]) the Neumann operator. Its resolvent is denoted by $R(z):=(H-z)^{-1}$ for $z \in \mathbb{C} \backslash \sigma(H)$ and we set $R:=R(-1)$. The associated scale of Hilbert spaces is denoted by $\mathscr{H}^{k, \mathrm{~N}}:=\operatorname{dom} H^{k / 2}$ with norm $\|u\|_{k, \mathrm{~N}}:=\left\|(H+1)^{k / 2} u\right\|$.
\item[iv.] Denote by $\mathfrak{h}^{\mathrm{D}}:=\mathfrak{h} \upharpoonright_{\mathscr{H}^{1, \mathrm{D}}}$ the form restricted to $\mathscr{H}^{1, \mathrm{D}}$. (Note that $\mathfrak{h}^{\mathrm{D}}$ is a closed form since $\Gamma: \mathscr{H}^{1} \longrightarrow \mathscr{G}$ is bounded, hence $\operatorname{dom} \mathfrak{h}^{\mathrm{D}}=\operatorname{ker} \Gamma$ is closed in $\mathscr{H}^{1}$.) Moreover, we call the self-adjoint and non-negative operator $H^{\mathrm{D}}$ associated with $\mathfrak{h}^{\mathrm{D}}$ in $\mathscr{H}$ the Dirichlet operator. We denote its resolvent by $R^{\mathrm{D}}(z):=\left(H^{\mathrm{D}}-z\right)^{-1}$ for $z \in \mathbb{C} \backslash \sigma\left(H^{\mathrm{D}}\right)$ and set $R^{\mathrm{D}}:=R^{\mathrm{D}}(-1)$. The associated scale of Hilbert spaces in $\mathscr{H}^{0, \mathrm{D}}$ is denoted by $\mathscr{H}^{k, \mathrm{D}}:=\operatorname{dom}\left(H^{\mathrm{D}}\right)^{k / 2}$ with norm $\|u\|_{k, \mathrm{D}}:=\left\|\left(H^{\mathrm{D}}+1\right)^{k / 2} u\right\|$.
If $(\Gamma, \mathscr{G})$ is a generalised boundary pair, then we denote by $\mathscr{H}^{0, \mathrm{D}}$ the closure of $\operatorname{ker} \Gamma=\mathscr{H}^{1, \mathrm{D}}$ in $\mathscr{H}$. For consistency, we extend $R^{\mathrm{D}}(z)$ by 0 on $\left(\mathscr{H}^{0, \mathrm{D}}\right)^{\perp}$, and denote the extended resolvent by the same symbol, i.e., we set $R^{\mathrm{D}}(z) f:=\left(H^{\mathrm{D}}-z\right)^{-1} f^{\mathrm{D}} \oplus 0$ for $f=f^{\mathrm{D}} \oplus f^{\perp}$.
\end{itemize}

Remark 2.3.
\begin{itemize}
\item[i.] If ran $\Gamma$ is not dense in $\mathscr{G}$, then we can replace $\mathscr{G}$ by $\mathscr{G}_{0}:=\overline{\operatorname{ran} \Gamma}$.
\item[ii.] In most of our examples, $\operatorname{ker} \Gamma$ is dense in $\mathscr{H}$, and we mean by "boundary pair" an "ordinary boundary pair". An example of a generalised boundary pair is presented in Example 2.4 and in Section 6.7.
\item[iii.] We mostly work with unbounded quadratic forms $\mathfrak{h}$. In Section 6.7, we present an example with a bounded form $\mathfrak{h}$ related to a discrete Laplacian on a graph; in this case, $\mathscr{H}=\mathscr{H}^{1}$.
\item[iv.] Note that if the boundary pair $(\Gamma, \mathscr{G})$ associated with $\mathfrak{h}$ is not bounded (i.e., $\operatorname{ran} \Gamma \subsetneq \mathscr{G}$ ), then we can turn it into a bounded boundary pair $(\widetilde{\Gamma}, \widetilde{\mathscr{G}})$ (i.e., $\operatorname{ran} \widetilde{\Gamma}=\widetilde{\mathscr{G}}$ ) associated with $\mathfrak{h}$ by changing the boundary space $\widetilde{\mathscr{G}}$ and its norm, see Proposition 5.9. Nevertheless, after this modification, the boundary space is less natural in many applications, and no longer an ordinary $\mathrm{L}_{2}$-space as in the following basic example.
\end{itemize}

Example 2.4. Let us illustrate the above setting by a prototype we have in mind (see also [BBABr11] and references therein): Assume that $(X, \mu)$ is a measured space. As quadratic form we choose an "energy form", i.e., $\mathfrak{h}(f)=$ $\int_{X}|\mathrm{~d} f|^{2} \mathrm{~d} \mu$, where $|\mathrm{d} f|^{2}$ is usually a sort of squared norm of a "derivative" on $X$. Moreover, we assume that $Y \subset X$ is measurable (the "boundary" of $X$ ) and $\nu$ is a measure on $Y$. We set $\mathscr{H}:=\mathrm{L}_{2}(X, \mu)$ and $\mathscr{G}:=\mathrm{L}_{2}(Y, \nu)$. As boundary map we choose $\Gamma f:=f \upharpoonright_{Y}$. One has to check now that $\Gamma$ is bounded as operator $\mathscr{H}^{1} \rightarrow \mathscr{G}$, i.e., that there is a constant $C>0$ such that
$$\int_{Y}|f|^{2} \mathrm{~d} \nu \leq C \int_{X}\left(|\mathrm{~d} f|^{2}+|f|^{2}\right) \mathrm{d} \mu .$$
If $\mu(Y)>0$, then $(\Gamma, \mathscr{G})$ is a generalised boundary pair, and we may choose as measure $\nu$ the measure induced by $X$ (i.e., $\nu(B):=\mu(B)$ for measurable sets $B \subset Y$ ). In this article, we mostly are interested in the case when $\mu(Y)=0$, i.e., when $\nu$ is supported on a set of $\mu$-measure 0 only. This leads to a boundary map for which ker $\Gamma$ is dense in $\mathscr{H}=\mathrm{L}_{2}(X, \mu)$, i.e., to an ordinary boundary pair.

Definition 2.5. Let $\mathscr{N}^{1}$ be the orthogonal complement of $\operatorname{ker} \Gamma$ in $\mathscr{H}^{1}$. We call the inverse
$$S:=\left(\Gamma \upharpoonright_{\mathscr{N}^{1}}\right)^{-1}: \mathscr{G}^{1 / 2} \longrightarrow \mathscr{N}^{1} \subset \mathscr{H}^{1}$$
of the bijective map $\Gamma: \mathscr{N}^{1} \longrightarrow \mathscr{G}^{1 / 2}:=\operatorname{ran} \Gamma$ the (weak) Dirichlet solution map (at the point $z=-1$ ).
Clearly, $h=S \varphi$ with $\varphi \in \mathscr{G}^{1 / 2}$ is the weak solution of the Dirichlet problem, i.e.,
$$(\mathfrak{h}+\mathfrak{1})(h, f)=\mathfrak{h}(h, f)+\langle h, f\rangle=0 \quad \forall f \in \mathscr{H}^{1, \mathrm{D}}, \quad \Gamma h=\varphi .$$

The Dirichlet solution operator $S$ allows us to define a natural norm on the range $\mathscr{G}^{1 / 2}$ of $\Gamma$, namely we set
$$\|\varphi\|_{\mathscr{G}^{1 / 2}}:=\|S \varphi\|_{\mathscr{H}^{1}},$$
i.e. the norm of the boundary element $\varphi$ is given by the $\mathscr{H}^{1}$-norm of its (weak) Dirichlet solution. Clearly, the operator $S: \mathscr{G}^{1 / 2} \longrightarrow \mathscr{H}^{1}$ and its left inverse $\Gamma: \mathscr{N}^{1} \longrightarrow \mathscr{G}^{1 / 2}$ are isometric. In particular, $\mathscr{G}^{1 / 2}$ is itself a Hilbert space (with its inner product induced by $\|\cdot\|_{\mathscr{G}^{1 / 2}}$ ). Moreover, the natural inclusion $\mathscr{G}^{1 / 2} \hookrightarrow \mathscr{G}$ is bounded, since
$$\|\varphi\|_{\mathscr{G}}=\|\Gamma S \varphi\|_{\mathscr{G}} \leq\|\Gamma\|_{1 \rightarrow 0}\|S \varphi\|_{\mathscr{H}^{1}}=\|\Gamma\|_{1 \rightarrow 0}\|\varphi\|_{\mathscr{G}^{1 / 2}},$$
where $\|\Gamma\|_{1 \rightarrow 0}$ is the norm of $\Gamma$ as operator $\Gamma: \mathscr{H}^{1} \longrightarrow \mathscr{G}$.
Proposition 2.8. Let $(\Gamma, \mathscr{G})$ be a boundary pair associated with $\mathfrak{h}$, then we have:
\begin{itemize}
\item[i.] The Dirichlet solution operator $S$ is closed and densely defined as operator in $\mathscr{G} \rightarrow \mathscr{H}^{1}$. Its domain is given by $\operatorname{dom} S=\mathscr{G}^{1 / 2}$.
\item[ii.] The quadratic form $\mathfrak{l}$ defined by $\mathfrak{l}(\varphi):=\|S \varphi\|_{1}^{2}$ with $\operatorname{dom} \mathfrak{l}=\mathscr{G}^{1 / 2}$ is a closed quadratic form in $\mathscr{G}$. Moreover,
$$\mathfrak{l}(\varphi) \geq \frac{1}{\|\Gamma\|_{1 \rightarrow 0}^{2}}\|\varphi\|_{\mathscr{G}}^{2}$$
for $\varphi \in \mathscr{G}^{1 / 2}$.
\end{itemize}

Proof. (i) The operator $S$ has (by definition) a bounded inverse, hence $S$ is closed.
(ii) The lower bound on $\mathfrak{l}$ follows immediately from (2.7). In order to show that $\mathfrak{l}$ is closed, let $\left(\varphi_{n}\right)_{n}$ be a Cauchy sequence in $\mathscr{G}^{1 / 2}$ with respect to $\mathfrak{l}$, then $\left(\varphi_{n}\right)_{n}$ is also a Cauchy sequence in $\mathscr{G}$, hence converges in $\mathscr{G}$ to an element $\varphi \in \mathscr{G}$. Moreover, $\left(S \varphi_{n}\right)_{n}$ is a Cauchy sequence in $\mathscr{H}^{1}$, hence also convergent to $h \in \mathscr{H}^{1}$. Since $S$ is closed it follows that $\varphi \in \operatorname{dom} S=\mathscr{G}^{1 / 2}$ and $S \varphi=h$, i.e., $\varphi \in \operatorname{dom} \mathfrak{l}$ and $\mathfrak{l}\left(\varphi_{n}-\varphi\right) \rightarrow 0$. \(\square\)

Let us now associate a natural operator $\Lambda$ to a boundary pair $(\Gamma, \mathscr{G})$. It turns out (cf. (1.16)) that $\Lambda$ is the Dirichlet-to-Neumann operator, i.e., $\Lambda \varphi$ associates to a suitable boundary value $\varphi$ the "normal derivative" of the associated solution of the Dirichlet problem $h=S \varphi$.

Definition 2.10. Let $\Lambda$ be the operator associated with the quadratic form $\mathfrak{l}$. Then $\Lambda$ is called the Dirichlet-to-Neumann operator (at the point $z=-1$ ) associated with the boundary map $\Gamma$ and the quadratic form $\mathfrak{h}$. We denote by $\mathscr{G}^{k}$ the natural scale of Hilbert spaces associated with the self-adjoint operator $\Lambda$, i.e. we set
$$\mathscr{G}^{k}:=\operatorname{dom} \Lambda^{k}, \quad\|\varphi\|_{k}:=\left\|\Lambda^{k} \varphi\right\|_{\mathscr{G}} .$$

Note that $\|\varphi\|_{1 / 2}^{2}=\left\|\Lambda^{1 / 2} \varphi\right\|_{\mathscr{G}}^{2}=\mathfrak{l}(\varphi)=\|\varphi\|_{\mathscr{G}^{1 / 2}}^{2}$, i.e. the setting is compatible with our previously defined norm in (2.6). The exponents in the scale of Hilbert spaces $\mathscr{H}^{k}$ and $\mathscr{G}^{k}$ will be consistent with the regularity order of Sobolev spaces in our main examples in Section 6.3, a boundary pair associated with a Laplacian on a manifold with (smooth) boundary.

In the following theorem, we denote the adjoints of $\Gamma: \mathscr{H}^{1} \longrightarrow \mathscr{G}$ w.r.t. the inner products in $\mathscr{H}^{1}$ and $\mathscr{G}$ by $\Gamma^{1 *}$. Similarly, the adjoint of the operator $S$ viewed as (possibly unbounded) operator from $\mathscr{G}$ into $\mathscr{H}^{1}$ with domain $\mathscr{G}^{1 / 2}$ is denoted by $S^{* 1}$. It is easy to see that $\Gamma^{1 *}=R \Gamma^{*}: \mathscr{G} \longrightarrow \mathscr{H}^{1}$ and $S^{* 1}=S^{*}(\breve{H}+1): \mathscr{H}^{1} \longrightarrow \mathscr{G}$, where $\Gamma^{*}: \mathscr{H}^{-1} \longrightarrow \mathscr{G}$ and $S^{*}: \mathscr{G} \longrightarrow \mathscr{H}^{-1}$ are the duals with respect to the pairing $\langle\cdot, \cdot\rangle_{-1,1}: \mathscr{H}^{-1} \times \mathscr{H}^{1} \longrightarrow \mathbb{C}$.

Theorem 2.11. Let $\Gamma$ be a boundary map associated with $\mathfrak{h}$.
\begin{itemize}
\item[i.] We have $\left(\mathscr{G}^{1}=\right) \operatorname{dom} \Lambda=\operatorname{dom} S^{* 1} S$ and
$$\Lambda=S^{* 1} S \geq \frac{1}{\|\Gamma\|_{1 \rightarrow 0}^{2}} .$$
In particular, $\Lambda^{-1}=\Gamma \Gamma^{1 *}$ exists and is a bounded operator in $\mathscr{G}$ with norm bounded by $\|\Gamma\|_{1 \rightarrow 0}^{2}$.
\item[ii.] We have $\|\Gamma\|_{1 \rightarrow 0}^{2}=1 / \inf \sigma(\Lambda)$; in particular, the lower bounds in (2.9) and (2.12) are optimal.
\item[iii.] The boundary pair is unbounded iff $\Lambda$ is unbounded.
\end{itemize}

Proof. (i) The lower bound on $\Lambda$ follows from (2.9). Moreover, by definition of the associated operator (see e.g. [Ka66, Thm. VI.2.1]) $\varphi \in \operatorname{dom} \Lambda$ iff
$$\mathfrak{l}(\cdot, \varphi)=\langle\cdot, \varphi\rangle_{\mathscr{G}^{1 / 2}}=\langle S \cdot, S \varphi\rangle_{\mathscr{H}^{1}}$$
extends to a bounded functional $\mathscr{G} \rightarrow \mathbb{C}$, i.e., iff $S \varphi \in \operatorname{dom} S^{* 1}$. Moreover,
$$\langle\varphi, \Lambda \varphi\rangle_{\mathscr{G}}=\langle\varphi, \varphi\rangle_{\mathscr{G}^{1 / 2}}=\langle S \varphi, S \varphi\rangle_{\mathscr{H}^{1}}=\left\langle\varphi, S^{* 1} S \varphi\right\rangle_{\mathscr{G}}$$
for $\varphi \in \operatorname{dom} \Lambda$. Since $S$ is closed, densely defined and $S^{-1}=\Gamma: \mathscr{N}^{1} \longrightarrow \mathscr{G}$ is bounded, it follows that $S^{* 1}$ is invertible and $\left(S^{* 1}\right)^{-1}=\Gamma^{1 *}$ (cf. [Ka66, Thm. III.5.30]), hence $\Lambda^{-1}=\Gamma \Gamma^{1 *}$.
(ii) From (2.12) we conclude immediately the inequality " $\geq$ ". For the inequality " $\leq$ ", note that there is a sequence $h_{n} \in \mathscr{H}^{1}$ such that $\left\|h_{n}\right\|_{\mathscr{H}^{1}}=1$ and $\left\|\Gamma h_{n}\right\| \rightarrow\|\Gamma\|_{1 \rightarrow 0}$. Moreover, we can assume that $h_{n} \in \mathscr{N}^{1}$, since the component in $\operatorname{ker} \Gamma=\mathscr{H}^{1, \mathrm{D}}$ does not contribute to the norm of $\Gamma$. Let $\varphi_{n}:=\Gamma h_{n}$, then we have
$$\frac{\mathfrak{l}\left(\varphi_{n}\right)}{\left\|\varphi_{n}\right\|^{2}}=\frac{\left\|h_{n}\right\|_{\mathscr{H}}^{2}}{\left\|\Gamma h_{n}\right\|^{2}} \rightarrow \frac{1}{\|\Gamma\|_{1 \rightarrow 0}^{2}},$$
hence $\inf \sigma(\Lambda) \leq 1 /\|\Gamma\|_{1 \rightarrow 0}^{2}$ by the variational characterisation of the spectrum of $\Lambda$.
(iii) Assume that $\operatorname{ran} \Gamma=\mathscr{G}$. Since $\Gamma \upharpoonright_{\mathscr{N}^{1}}: \mathscr{N}^{1} \longrightarrow \mathscr{G}$ is bounded and bijective, its inverse $S$ is bounded as well by the open mapping theorem. Hence $\Lambda=S^{* 1} S$ is bounded. On the other hand, if $\Lambda$ is bounded, then $\mathfrak{l}(\varphi)=\|S \varphi\|_{\mathscr{H}^{1}}^{2}$ is a bounded and everywhere defined quadratic form. In particular, $S: \mathscr{G} \longrightarrow \mathscr{H}^{1}$ is everywhere defined and bounded. For $\varphi \in \mathscr{G}$ we then have $\varphi=\Gamma S \varphi \in \operatorname{ran} \Gamma$, i.e., $\operatorname{ran} \Gamma=\mathscr{G}$. \(\square\)

A similar proof as the one for Theorem 2.11 (iii) shows that the boundary is unbounded iff $\Lambda(z)$ is unbounded for some (any) $z \in \mathbb{C} \backslash \sigma\left(H^{\mathrm{D}}\right)$, see Section 2.4 for the definition of $\Lambda(z)$.

For a bounded boundary pair, the scale of Hilbert spaces $\mathscr{G}^{k}$ consists of one vector space only, and all norms are equivalent, i.e.
$$\|\Gamma\|_{1 \rightarrow 0}^{-2 k}\|\varphi\|_{\mathscr{G}} \leq\|\varphi\|_{\mathscr{G} k} \leq\|\Lambda\|^{k}\|\varphi\|_{\mathscr{G}} .$$

\subsection*{2.3 The Dirichlet solution operator at arbitrary points}

Let us now extend the Dirichlet solution operator to arbitrary spectral points $z \in \mathbb{C} \backslash \sigma\left(H^{\mathrm{D}}\right)$.
Definition 2.14. Let $z \in \mathbb{C}$.
\begin{itemize}
\item[i.] We call
$$\mathscr{N}^{1}(z):=\left\{h \in \mathscr{H}^{1} \mid \mathfrak{h}(h, f)-z\langle h, f\rangle_{\mathscr{H}}=0 \quad \forall f \in \mathscr{H}^{1, \mathrm{D}}\right\}$$
the set of weak solutions in $z \in \mathbb{C}$ (with respect to the boundary pair $(\Gamma, \mathscr{G})$ and the quadratic form $\mathfrak{h}$ ).
\item[ii.] Let $\varphi \in \mathscr{G}^{1 / 2}$. We say that $h$ is a weak solution of the Dirichlet problem at the point $z$, if $h \in \mathscr{N}^{1}(z)$ and $\Gamma h=\varphi$.
\end{itemize}

Note that $\mathscr{N}^{1}(-1)=\mathscr{N}^{1}$ (see Definition 2.5). Moreover, it is easy to see that $\mathscr{N}^{1}(z)$ is a closed subspace of $\mathscr{H}^{1}$.

Proposition 2.15. Let $z \in \mathbb{C} \backslash \sigma\left(H^{\mathrm{D}}\right)$.
\begin{itemize}
\item[i.] Let $h_{1}, h_{2} \in \mathscr{N}^{1}(z)$ be two weak solutions of the same Dirichlet problem $\Gamma h_{1}=\Gamma h_{2}$, then $h_{1}=h_{2}$.
\item[ii.] The spaces $\mathscr{H}^{1, \mathrm{D}}$ and $\mathscr{N}^{1}(z)$ are closed as subspaces of $\mathscr{H}^{1}$ and we have the decomposition
$$\mathscr{H}^{1}=\mathscr{H}^{1, \mathrm{D}} \dot{+} \mathscr{N}^{1}(z),$$
(where "+" denotes the direct topological sum, see the end of Section 2.1) and
$$P(z) g:=S \Gamma g+(z+1) R^{\mathrm{D}}(z) S \Gamma g$$
is the projection of $g$ onto $\mathscr{N}^{1}(z)$ with respect to the above decomposition. The sum is orthogonal if $z=-1$.
\end{itemize}

The choice of $P(z)$ becomes more clear with Theorem 2.21 (i) (choosing $w=-1$ ).
Proof. (i) Assume that $h_{1}$ and $h_{2}$ are two solutions of the Dirichlet problem with $\Gamma h_{1}=\Gamma h_{2}$. Then $h:=h_{1}-h_{2} \in$ $\mathscr{H}^{1, \mathrm{D}} \cap \mathscr{N}^{1}(z)$. Since $\mathfrak{h}^{\mathrm{D}}-z \mathbf{l}$ is non-degenerative on $\mathscr{H}^{1, \mathrm{D}} \times \mathscr{H}^{1, \mathrm{D}}$ for $z \notin \sigma\left(H^{\mathrm{D}}\right)$, we conclude $h=0$.
(ii) The space $\mathscr{H}^{1, \mathrm{D}}=\operatorname{ker} \Gamma$ is closed since $\Gamma$ is bounded, and $\mathscr{N}^{1}(z)$ is easily seen to be closed as subspace of $\mathscr{H}^{1}$, too. Moreover, for $g \in \mathscr{H}^{1}$, we set $g_{z}=P(z) g=h+(z+1) R^{\mathrm{D}}(z) h$ with $h:=S \Gamma g$ and $g^{\mathrm{D}}:=g-g_{z}$. Then $\Gamma g^{\mathrm{D}}=\Gamma g-\Gamma h=0$ and
$$\begin{aligned}
(\mathfrak{h}-z \mathbf{l})\left(g_{z}, f\right) & =(\mathfrak{h}-z \mathbf{l})\left(h+(z+1) R^{\mathrm{D}}(z) h, f\right) \\
& =(\mathfrak{h}+1)(h, f)-(z+1)\langle h, f\rangle+(z+1)\left(\mathfrak{h}^{\mathrm{D}}-z\right)\left(R^{\mathrm{D}}(z) h, f\right)=0
\end{aligned}$$
for $f \in \mathscr{H}^{1, \mathrm{D}}$. Here, the first term vanishes since $\mathscr{N}^{1}$ and $\mathscr{H}^{1, \mathrm{D}}$ are orthogonal in $\mathscr{H}^{1}$; and the second and third term cancel each other. Therefore, we have shown that $g=g^{\mathrm{D}}+g_{z} \in \mathscr{H}^{1, \mathrm{D}}+\mathscr{N}^{1}(z)$. Finally, the sum is direct, since $\mathscr{N}^{1}(z) \cap \mathscr{H}^{1, \mathrm{D}}=\{0\}$ by the uniqueness of the weak Dirichlet solution, cf. (i). \(\square\)

We now define a "solution" operator $S(z)$ as the inverse of the boundary map $\Gamma$, i.e., $h=S(z) \varphi$ is the unique solution of the weak Dirichlet problem $h \in \mathscr{N}^{1}(z)$ and $\Gamma h=\varphi$ for $z \notin \sigma\left(H^{\mathrm{D}}\right)$.
Definition 2.17. Let $S(z): \mathscr{G}^{1 / 2} \longrightarrow \mathscr{H}^{1}$ be given by
$$S(z):=\left(\Gamma \upharpoonright_{\mathscr{N}^{1}(z)}\right)^{-1}: \mathscr{G}^{1 / 2} \longrightarrow \mathscr{N}^{1}(z) \subset \mathscr{H}^{1} .$$
---
retention_scope: session
part: 1
total_parts: 2
---

[Part 1/2 of: Taming the pseudoholomorphic beasts in R × (S1 × S2)]

---
source_file: 1711_02069.pdf
converter: mathpix
format: mmd
---

\title{
Taming the pseudoholomorphic beasts in $\mathbb{R} \times\left(S^{1} \times S^{2}\right)$
}

\author{
Chris Gerig
}

November 10, 2020

\begin{abstract}
For a closed oriented smooth 4-manifold $X$ with $b_{+}^{2}(X)>0$, the Seiberg-Witten invariants are well-defined. Taubes' "SW=Gr" theorem asserts that if $X$ carries a symplectic form then these invariants are equal to well-defined counts of pseudoholomorphic curves, Taubes' Gromov invariants. In the absence of a symplectic form there are still nontrivial closed self-dual 2-forms which vanish along a disjoint union of circles and are symplectic elsewhere. This paper and its sequel describes well-defined counts of pseudoholomorphic curves in the complement of the zero set of such near-symplectic 2-forms, and it is shown that they recover the Seiberg-Witten invariants over $\mathbb{Z} / 2 \mathbb{Z}$. This is an extension of " $\mathrm{SW}=\mathrm{Gr}$ " to non-symplectic 4-manifolds.

The main result of this paper asserts the following. Given a suitable near-symplectic form $\omega$ and tubular neighborhood $\mathcal{N}$ of its zero set, there are well-defined counts of pseudoholomorphic curves in a completion of the symplectic cobordism $(X-\mathcal{N}, \omega)$ which are asymptotic to certain Reeb orbits on the ends. They can be packaged together to form "near-symplectic" Gromov invariants as a function of spin-c structures on $X$.
\end{abstract}

\section*{1 Introduction}

\subsection*{1.1 Motivation}

The Seiberg-Witten invariants, introduced by Witten [51], are defined for any closed oriented 4 -manifold $X$ with $b_{+}^{2}(X) \geq 1$. These invariants $S W_{X}(\mathfrak{s})$ are constructed by counting solutions to the Seiberg-Witten equations associated with a given spin-c structure $\mathfrak{s} \in \operatorname{Spin}^{c}(X)$. When $b_{+}^{2}(X)>1$ the invariants only depend on the smooth structure of $X$ and a choice of "homology orientation" of $X$. When $b_{+}^{2}(X)=1$ the invariants also depend on a choice of "chamber."

The Gromov invariants, introduced by Taubes [33] who generalized the work of Gromov [11] and Ruan [30], are defined for any closed symplectic 4-manifold $(X, \omega)$. These invariants $G r_{X, \omega}(A)$ are constructed by counting pseudoholomorphic curves in $X$ which represent a given homology class $A \in H_{2}(X ; \mathbb{Z})$. The invariants only depend on the smooth structure of $X$.

Now, the existence of a symplectic structure implies that $b_{+}^{2}(X)>0$, and when $b_{+}^{2}(X)=1$ a given symplectic form determines a canonical "chamber" with which to define the Seiberg-Witten invariants of $X$. The symplectic form also determines a canonical "homology orientation" of $X$ and it induces a canonical identification of $H_{2}(X ; \mathbb{Z})$ with $\operatorname{Spin}^{c}(X)$. Under these identifications it was shown by Taubes [36] that the Gromov invariants and the Seiberg-Witten invariants are equivalent. But what occurs when $X$ does not have a symplectic structure? This was originally asked by Taubes during 1995 in a paper 32 from which we quote the ending:
> "It is observed that there are manifolds with nonzero Seiberg-Witten invariants which do not admit symplectic forms. With this understood, one is led to ask whether there is any sort of "Gromov invariant" interpretation for the Seiberg-Witten invariants in the nonsymplectic world."

In the absence of a symplectic form but keeping $b_{+}^{2}(X)>0$, given a generic Riemannian metric on $X$ there are still nontrivial closed self-dual 2-forms which vanish transversally along a disjoint union of circles in $X$ and are symplectic elsewhere. These were studied intensively in unpublished work of Karl Luttinger during the early 1990's (see also [24]). Such a 2-form $\omega$ is called a near-symplectic form, and $X-\omega^{-1}(0)$ is a noncompact symplectic 4-manifold which has an almost complex structure $J$ determined by $\omega$ and the Riemannian metric. It was noticed by Taubes that the estimates on symplectic 4-manifolds which were used to find $J$-holomorphic curves from given Seiberg-Witten solutions could also be used to find $J$-holomorphic curves when $\omega^{-1}(0) \neq \varnothing$.

Theorem 1.1 (Taubes [39]). If $X$ has a nonzero Seiberg-Witten invariant then there exists at least one $J$-holomorphic curve in $X-\omega^{-1}(0)$, homologically bounding $\omega^{-1}(0)$ in the sense that it has intersection number 1 with every linking 2-sphere of $\omega^{-1}(0)$.

This theorem provides evidence that there might be "Gromov invariants" for non-symplectic 4-manifolds, and that they might recover the Seiberg-Witten invariants. An elaboration can be found in [37, 38]. But there are difficulties in constructing well-defined counts of such curves because $J$ becomes singular along $\omega^{-1}(0)$. That is, transversality and a Fredholm theory for the moduli spaces of curves in $X-\omega^{-1}(0)$ is hard to establish (see [35, 40]). We can rephrase the problem (see [41]), for which it is standard to complete $X-\omega^{-1}(0)$ by attaching symplectization ends and then the $J$-holomorphic curves satisfy certain asymptotic conditions. The boundary $Y$ of a tubular neighborhood of $\omega^{-1}(0)$ is a contact manifold, with contact form induced by $\omega$, and the $J$ -holomorphic curves are asymptotic to periodic orbits of the Reeb flow induced by the contact form on $Y$. Models of these curves in the symplectization of $Y=S^{1} \times S^{2}$ are studied in [25, 42, 43, 45], and the aforementioned difficulties are now caused by the contact dynamics: the existence of certain Reeb orbits permits the existence of non-transverse multiply covered curves in the relevant moduli spaces (see Remark 3.10).

As will be explained momentarily, we overcome the transversality difficulties by modifying the chosen neighborhood of $\omega^{-1}(0)$ and hence the contact dynamics on each component $S^{1} \times S^{2}$ of $Y$. We then pick out the appropriate $J$-holomorphic curves to count using embedded contact homology (ECH), a Floer theory constructed by Hutchings [17]. ECH was originally motivated by the desire to find an analog of Taubes' equivalence $S W_{X}=G r_{X, \omega}$ in dimension three, granted that a version of Seiberg-Witten Floer homology [22] existed on the gauge theory side. These two homologies are now known to be isomorphic by Taubes [46], using the same techniques that were used to prove $S W_{X}=G r_{X, \omega}$. All of this machinery plays a crucial role in this paper and its sequel [9].

\subsection*{1.2 Near-symplectic geometry}

Throughout this paper, $(X, g)$ denotes a closed connected oriented smooth Riemannian 4-manifold with $b_{+}^{2}(X) \geq 1$, where $b_{+}^{2}(X)$ denotes the dimension of any maximal positive-definite subspace of $H^{2}(X ; \mathbb{R})$ under the intersection form on $X$. In particular, if $X$ is simply connected then the only spaces excluded by this assumption on $b_{+}^{2}(X)$ are 4-spheres and connected sums of $\overline{\mathbb{C} P^{2}}$, and if $X=S^{1} \times M$ then the only spaces excluded are rational homology 3-spheres $M$.

Let $\omega \in \Omega^{2}(X ; \mathbb{R})$ be a nontrivial closed self-dual (hence harmonic) 2-form. These always exist by Hodge theory, and in fact, the set of such 2-forms determines a subspace $H_{+}^{2}(X ; \mathbb{R}) \subset H^{2}(X ; \mathbb{R})$ for which $b_{+}^{2}(X)=\operatorname{dim} H_{+}^{2}(X ; \mathbb{R})$. A nice property of $\omega$ is that the complement of its zero set $Z:=\omega^{-1}(0)$ is symplectic,
$$\omega \wedge \omega=\omega \wedge * \omega=|\omega|^{2} d \operatorname{vol}_{g}$$
but we cannot always expect $Z=\varnothing$, i.e. for $X$ to be symplectic. For starters, if a symplectic form existed then an almost complex structure could be built from it and the metric, forcing $1-b^{1}(X)+b_{+}^{2}(X)$ to have even parity by characteristic class theory. What we do know in general is that $Z$ cannot contain any open subset of $X$ [6, Corollary 4.3.23].

For generic metrics, Honda [13, Theorem 1.1] and LeBrun [23, Proposition 1] have shown that there exist nontrivial closed self-dual 2-forms that vanish transversally as sections of the self-dual 3-plane subbundle $\bigwedge_{+}^{2} T^{*} X$ of $\bigwedge^{2} T^{*} X \rightarrow X$. Such 2-forms are examples of

Definition 1.2. A closed 2-form $\omega: X \rightarrow \bigwedge^{2} T^{*} X$ is near-symplectic if for all points $x \in X$ either $\omega^{2}(x)>0$, or $\omega(x)=0$ and the rank of the gradient $\nabla \omega_{x}: T_{x} X \rightarrow \bigwedge^{2} T_{x}^{*} X$ is three.

It follows from [1, Proposition 1] that we can always find a metric for which a given nearsymplectic form is self-dual, and we assume throughout this paper that such metrics have been chosen. It follows from the definition that $Z$ consists of a finite disjoint union of smooth embedded circles [28, Lemma 1.2], and $Z$ is null-homologous while the individual zero-circles need not be [29, Proposition 1.1.26]. Moreover, the zero-circles are not all the same but come in two "types" depending on the behavior of $\omega$ near them:

Let $N_{Z}$ denote the normal bundle of $Z \subset X$, identified with the orthogonal complement $T Z^{\perp}$ such that $T X=T Z \oplus N_{Z}$. The gradient $\nabla \omega$ defines a vector bundle isomorphism $\left.N_{Z} \rightarrow \bigwedge_{+}^{2} T^{*} X\right|_{Z}$, and we orient $N_{Z}$ such that $\nabla \omega$ is orientation-reversing. The orientation of $T X$ orients $\bigwedge_{+}^{2} T^{*} X$, so $T Z$ is subsequently oriented. As described in [12, 28, 35], $\omega$ determines a particular subbundle decomposition
$$N_{Z}=L_{Z} \oplus L_{Z}^{\perp}$$
where $L_{Z} \rightarrow Z$ is a rank one line bundle. Explicitly, $L_{Z}$ is the negative-definite subspace with respect to the induced quadratic form on $N_{Z}$,
$$v \mapsto\left\langle\nabla_{v} \omega\left(\partial_{0}, \cdot\right), v\right\rangle$$
where $\partial_{0} \in \Gamma(T Z)$ is the unit-length oriented vector field. A zero-circle of $Z$ is called untwisted if $L_{Z}$ restricted to that zero-circle is orientable, and twisted otherwise. ${ }^{1}$

By work of Luttinger, any given pair $(\omega, g)$ of closed self-dual 2-form and Riemannian metric can be modified so that $Z$ has any positive number of components (see [28, 44]), but as noted by Gompf (see [28, Theorem 1.8]), the number of untwisted zero-circles must have the same parity as that of $1-b^{1}(X)+b_{+}^{2}(X)$. We can use these modifications to get rid of all twisted zero-circles (see [28, Remark 1.9]), and explicit constructions of near-symplectic forms having only untwisted zero-circles are given in [8,31] in terms of handlebody decompositions.

Example 1.3. The "symplectic geometer's dream" would be that $\left(\mathbb{C} P^{2}, \omega_{\mathrm{FS}}\right) \#\left(\mathbb{C} P^{2}, \omega_{\mathrm{FS}}\right)$ is symplectic, but this is not the case. The failure to symplectically glue the Fubini-Study 2-forms across the connect-sum region manifests itself in a near-symplectic form with a single untwisted zero-circle.

\footnotetext{
${ }^{1}$ The literature uses the terminology "even and odd" as well as "orientable and non-orientable" to describe the zero-circles, but the author has found this to be very confusing.
}

\subsection*{1.3 Main results}

Let $\omega$ be a near-symplectic form on $(X, g)$ whose zero set $Z$ has $N \geq 0$ components, all of which are untwisted zero-circles. As we just mentioned, this can always be arranged.

Remark 1.4. The assumption that $Z$ has only untwisted zero-circles can be weakened in this paper to some extent. As will be clarified in the appendix, we may assume $Z$ to also have twisted zero-circles which are non-contractible in $X$.

Let $\mathcal{N}$ denote a union of arbitrarily small tubular neighborhoods of the components of $Z \subset X$. Using Moser-type results of Honda [12] (see also [41, §2e]), $\mathcal{N}$ can be chosen so that the complement
$$\left(X_{0}, \omega\right):=\left(X-\mathcal{N},\left.\omega\right|_{X-\mathcal{N}}\right)$$
is a symplectic manifold with contact-type boundary, where each boundary component is a copy of $\left(S^{1} \times S^{2}, e^{-1} \lambda_{0}\right)$. Here, $\lambda_{0}$ is an overtwisted contact form which is described in Section 3.1, and studied intensively by Taubes in order to characterize the pseudoholomorphic "beasts" living in the symplectization $\mathbb{R} \times\left(S^{1} \times S^{2}\right)$.

Remark 1.5. The orientation of $S^{1} \times S^{2}$ as a contact 3-manifold disagrees with the orientation of $S^{1} \times S^{2}$ as a boundary component of $X_{0}$, so each boundary component of $X_{0}$ is concave (if the orientations agreed then it would be a convex boundary component). This is consistent with a well-known result of Eliashberg: an overtwisted contact 3-manifold cannot be the convex boundary of a symplectic 4-manifold, i.e. there are no symplectic fillings of this contact 3-manifold. But note that $(\mathcal{N}, \omega)$ is a near-symplectic filling.

There is a canonical spin-c structure $\mathfrak{s}_{\omega}$ on $X_{0}$ whose positive spinor bundle is $\mathbb{S}_{+}=\mathbb{C} \oplus K^{-1}$, where $\underline{\mathbb{C}} \rightarrow X_{0}$ denotes the trivial complex line bundle and $K$ is the canonical bundle of $\left(X_{0}, J\right)$ for any chosen $\omega$-compatible almost complex structure $J$. Any other spin-c structure on $X_{0}$ differs from $\mathfrak{s}_{\omega}$ by tensoring with a complex line bundle on $X_{0}$. It follows from Taubes' work on near-symplectic geometry that $\omega$ also induces a canonical identification of $\operatorname{Spin}^{c}(X)$ with the set
$$\operatorname{Rel}_{\omega}(X):=\left\{A \in H_{2}\left(X_{0}, \partial X_{0} ; \mathbb{Z}\right) \mid \partial A=\mathbb{1} \in H_{1}\left(\partial X_{0} ; \mathbb{Z}\right)\right\}$$
where $\mathbb{1}$ is the oriented generator on each component (the orientation conventions are specified in Section 3.1). This correspondence is given by restricting $\mathfrak{s} \in \operatorname{Spin}^{c}(X)$ to $X_{0}$, which differs from $\mathfrak{s}_{\omega}$ by a unique complex line bundle $L_{\mathfrak{s}} \rightarrow X_{0}$, and taking the Poincaré-Lefschetz dual of $c_{1}\left(L_{\mathfrak{s}}\right)$. Denote the resulting class by $A_{\mathfrak{s}} \in \operatorname{Rel}_{\omega}(X)$.

Of relevance to the Seiberg-Witten invariants of $X$ will be $J$-holomorphic curves in a completion of $\left(X_{0}, \omega\right)$ which represent classes in $\operatorname{Rel}_{\omega}(X)$. The completion $(\bar{X}, \omega)$ of $\left(X_{0}, \omega\right)$ is obtained by attaching cylindrical ends to the components of $\partial X_{0}$ and extending $\omega$ over them (see Section 2.2). In order to obtain well-defined counts we need all curves to be transverse. Unfortunately, there are special Reeb orbits in $\left(S^{1} \times S^{2}, \lambda_{0}\right)$ for which there exist non-transverse multiply covered curves in $\bar{X}$ asymptotic to multiple covers of those orbits. ${ }^{2}$ What can we do?

A given class $A \in \operatorname{Rel}_{\omega}(X)$ determines an upper bound $\rho(A)$ of the "lengths" of the possible Reeb orbits which the relevant $J$-holomorphic curves are asymptotic to, so there are only finitely many orbits which permit the existence of non-transverse curves. The idea now is to go back

\footnotetext{
${ }^{2}$ The problem is worse: these non-transverse curves also have negative ECH index (see Remark 3.10).
}
and choose a different tubular neighborhood $\mathcal{N}$, determining a different contact form on $S^{1} \times S^{2}$ having the same contact structure $\xi_{0}$ as $\lambda_{0}$. In particular, we search for a particular contact form whose Reeb orbits of "lengths" less than $\rho(A)$ do not permit the existence of non-transverse curves representing $A$. This is the content of the following lemma, proved in Section 3.2.

Lemma 1.6. For $A \in \operatorname{Rel}_{\omega}(X)$, there exists a tubular neighborhood $\mathcal{N}$ of $Z$ in $X$ such that the symplectic cobordism $(X-\mathcal{N}, \omega)$ has contact-type boundary, where each boundary component is a copy of $\left(S^{1} \times S^{2}, \lambda_{A}\right)$. Here, $\lambda_{A}$ denotes a nondegenerate overtwisted contact form with contact structure $\xi_{0}$ such that its Reeb orbits of symplectic action less than $\rho(A)$ are $\rho(A)$-flat and are either positive hyperbolic or $\rho(A)$-positive elliptic.

The " $\rho(A)$-positive" condition on the elliptic orbits is a key ingredient to preventing the existence of (negative ECH index) non-transverse curves that represent $A$, and this was observed by Hutchings [16] for more general symplectic cobordisms. The " $\rho(A)$-flatness" condition on $\lambda_{A}$ is needed in order to identify our counts of curves with the Seiberg-Witten invariants, as Taubes [46] did for the isomorphism between ECH and Seiberg-Witten Floer cohomology.

Another issue is the possible existence of multiply covered holomorphic exceptional spheres, which is also an issue in Taubes' Gromov invariants for closed symplectic 4-manifolds. Recall that an exceptional sphere in $X$ is an embedded smooth sphere of self-intersection -1, and $X$ is minimal if there are no exceptional spheres. Let
$$\mathcal{E}_{\omega} \subset H_{2}\left(X_{0}, \partial X_{0} ; \mathbb{Z}\right)$$
denote the set of classes represented by symplectic exceptional spheres in $X_{0}$. The issue with multiply covered spheres will be discussed in Section 3.3, and it is avoided in the following two scenarios: Either $X$ is minimal, or $E \cdot A \geq-1$ for every $E \in \mathcal{E}_{\omega}$.

The relevant counts of curves will a priori depend on a suitably generic choice of $J$ and they will be packaged together as elements in $E C H_{*}\left(-\partial X_{0}, \xi_{0}\right)$. Roughly speaking, the ECH chain complex over $\mathbb{Z}$ is generated by "orbit sets" which are finite sets of pairs $(\gamma, m)$ of Reeb orbits $\gamma$ in $\left(-\partial X_{0}, \xi_{0}\right)$ and multiplicities $m \in \mathbb{N}$. To define invariants of $X$, we will first count $J$-holomorphic curves in $\bar{X}$ to obtain a cycle in the ECH chain complex: the asymptotics of each curve define a generator $\Theta$ of the ECH chain complex, and the integer coefficient attached to each such $\Theta$ is an integrally weighted count of the curves which are asymptotic to $\Theta$. Specifically,

Theorem 1.7. Let $(X, \omega, A)$ be as specified above, such that $E \cdot A \geq-1$ for every symplectic exceptional class $E \in \mathcal{E}_{\omega}$. Fix a nonnegative integer $I$ and an ordered set of equivalence classes $[\bar{\eta}]:=\left\{\left[\eta_{1}\right], \ldots,\left[\eta_{p}\right]\right\} \subset H_{1}(X ; \mathbb{Z}) /$ Torsion, where $0 \leq p \leq I$ such that $I-p$ is even. For suitably generic $J$ on $\bar{X}$, there is a well-defined element
$$G r_{X, \omega, J}^{I}(A,[\bar{\eta}]) \in E C H_{*}\left(-\partial X_{0}, \xi_{0}\right)$$
concentrated in a single grading $g(A, I)$. This element is given by integrally weighted counts of (disjoint and possibly multiply covered) $J$-holomorphic curves in $(\bar{X}, \omega)$ which satisfy the following: They are asymptotic to Reeb orbits with respect to $\lambda_{A}$ whose total homology class in each $S^{1} \times S^{2}$ component is the oriented generator; they represent the relative class $A$; they pass through an a priori chosen set of $\frac{1}{2}(I-p)$ base points in $X_{0}$; they pass through an a priori chosen ordered set of $p$ disjoint oriented loops in $X_{0}$ which represent $[\bar{\eta}]$; and they have ECH index $I$.

Here, the "ECH index" may be viewed as a formal dimension of the relevant moduli space of $J$-holomorphic currents, while the point/loop constraints carve out a zero-dimensional subset of the moduli space. These curves are explicitly specified in Proposition 3.16.

Now, a given $\mathfrak{s} \in \operatorname{Spin}^{c}(X)$ determines not only the class $A_{\mathfrak{s}} \in \operatorname{Rel}_{\omega}(X)$ but also an integer
$$d(\mathfrak{s}):=\frac{1}{4}\left(c_{1}(\mathfrak{s})^{2}-2 \chi(X)-3 \sigma(X)\right)$$
where $c_{1}(\mathfrak{s})$ denotes the first Chern class of the spin-c structure's positive spinor bundle, $\chi(X)$ denotes the Euler characteristic of $X$, and $\sigma(X)$ denotes the signature of $X$. This integer $d(\mathfrak{s})$ is the formal dimension of the moduli space of Seiberg-Witten solutions on $X$ with respect to $\mathfrak{s}$.

Using ideas from Seiberg-Witten theory ${ }^{3}$ we will show in [9] that $g\left(A_{\mathfrak{s}}, d(\mathfrak{s})\right)$ is the lowest grading for which $E C H_{*}\left(-\partial X_{0}, \xi_{0}\right)$ is nonzero. After choosing an ordering of the components of $Z$, there is then an identification of the group $E C H_{g\left(A_{\mathfrak{s}}, d(\mathfrak{s})\right)}\left(\partial X_{0}, \xi_{0}\right)$ with $\mathbb{Z}$ (see Proposition 3.2, Remark 3.18, and Lemma 3.26).

Definition 1.8. Fix an ordering of the zero-circles of $\omega$. The near-symplectic Gromov invariants
$$\operatorname{Gr}_{X, \omega, J}: \operatorname{Spin}^{c}(X) \rightarrow \Lambda^{*} H^{1}(X ; \mathbb{Z})$$
are defined as follows. If $E \cdot A_{\mathfrak{s}}<-1$ for some $E \in \mathcal{E}_{\omega}$ then $\operatorname{Gr}_{X, \omega, J}(\mathfrak{s})=0$. Assume now that $E \cdot A_{\mathfrak{s}} \geq-1$ for every $E \in \mathcal{E}_{\omega}$ (which is a vacuous statement when $X$ is minimal). The component of $G r_{X, \omega, J}(\mathfrak{s})$ in $\Lambda^{p} H^{1}(X ; \mathbb{Z})$, for $p \leq d(\mathfrak{s})$ such that $d(\mathfrak{s})-p$ is even, is
$$\left[\eta_{1}\right] \wedge \cdots \wedge\left[\eta_{p}\right] \mapsto G r_{X, \omega, J}^{d(\mathfrak{s})}\left(A_{\mathfrak{s}},[\bar{\eta}]\right) \in \mathbb{Z}$$
and it is defined to be zero for all other integers $p$.
These invariants currently depend on the choice of $\omega$ and $J$, though we expect to establish invariance by varying $(\omega, J)$ and analyzing the resulting moduli spaces of curves. With $\mathbb{Z} / 2 \mathbb{Z}$ coefficients and $X$ minimal, we will show in [9] that they recover the Seiberg-Witten invariants of $X$, hence are smooth invariants of $X$ alone. ${ }^{4}$

Theorem 1.9 (Gerig [9]). Let $(X, \omega)$ be as specified above, with $X$ minimal. Given $\mathfrak{s} \in \operatorname{Spin}^{c}(X)$,
$$G r_{X, \omega}(\mathfrak{s})=S W_{X}(\mathfrak{s}) \in \Lambda^{*} H^{1}(X ; \mathbb{Z}) \otimes \mathbb{Z} / 2 \mathbb{Z}$$
where $\omega$ determines the chamber for defining the Seiberg-Witten invariants when $b_{+}^{2}(X)=1$.
Remark 1.10. We expect that Theorem 1.9 also holds with $\mathbb{Z}$ coefficients, similarly to how Taubes' isomorphisms (between embedded contact homology and a version of Seiberg-Witten Floer homology) with $\mathbb{Z} / 2 \mathbb{Z}$ coefficients can be lifted to $\mathbb{Z}$ coefficients (see [47, §3.b]). Note that the definition of $S W_{X}$ depends on a choice of homology orientation of $X$, while the definition of $G r_{X, \omega}$ depends on a choice of ordering of the zero-circles of $\omega$. We expect that $\omega$, with a fixed ordering of its zero-circles, canonically determines a homology orientation of $X$ (see [9] for an elaboration).

\footnotetext{
${ }^{3}$ We may also be able to establish this fact using $J$-holomorphic curves alone.
${ }^{4}$ There is also a version of this result when $X$ is not minimal (see 9 ).
}

Definition 1.8 is an extension of Taubes' Gromov invariants [33], which were constructed in the setting $Z=\varnothing$. To see how Taubes' invariants fit into the framework of Theorem 1.7, we first set $\partial X_{0}=\varnothing$ so that $(\bar{X}, \omega)=(X, \omega)$ is a closed symplectic 4-manifold. We then make the identification $E C H_{0}(\varnothing, 0) \cong \mathbb{Z}$ whose generator is the empty set of orbits. For a given $\mathfrak{s} \in \operatorname{Spin}^{c}(X)$, the corresponding absolute class $A_{\mathfrak{s}} \in H_{2}(X ; \mathbb{Z})$ determines the ECH index
$$I\left(A_{\mathfrak{s}}\right):=c_{1}(T X) \cdot A_{\mathfrak{s}}+A_{\mathfrak{s}} \cdot A_{\mathfrak{s}} \in 2 \mathbb{Z}$$
which equals $d(\mathfrak{s})$, and Taubes' invariants may be interpreted as
$$\operatorname{Gr}_{X, \omega, J}^{I\left(A_{\mathfrak{s}}\right)}\left(A_{\mathfrak{s}},[\bar{\eta}]\right) \in E C H_{0}(\varnothing, 0)$$
since all $J$-holomorphic curves have no punctures.
Remark 1.11. If $X$ is a symplectic manifold and $\omega_{0}$ is a near-symplectic form, we may consider a deformation of $\omega_{0}$ to a symplectic form $\omega_{1}$ through near-symplectic forms (except at a finite number of times along the deformation). The near-symplectic Gromov invariants of $\left(X, \omega_{0}\right)$ must equal Taubes' Gromov invariants of $\left(X, \omega_{1}\right)$ in light of Theorem 1.9 and [32, Theorem 4.1]. The relation between the respective pseudoholomorphic curves is not pursued in this paper, but we leave the reader with a question: When a zero-circle shrinks and dies, does a holomorphic plane decrease its symplectic area and vanish, or does it close up into a sphere, or else?

Remark 1.12. With respect to Theorem 1.1, we expect that the near-symplectic Gromov invariants are related to counts of $J$-holomorphic curves in $X-Z$ by shrinking $\mathcal{N}$ to its core $Z$. These curves would homologically bound $Z$ in the sense that they have algebraic intersection number 1 with every linking 2-sphere of $Z$. A curve may also "pinch off" along $Z$ in the sense that a portion of the curve forms a multi-sheeted cone in a small neighborhood of a point on $Z$. These properties correspond to the following facts: a relevant $J$-holomorphic curve in $\overline{X-\mathcal{N}}$ is asymptotic to an orbit set on each $S^{1} \times S^{2}$ whose total homology class is the oriented generator of $H_{1}\left(S^{1} \times S^{2} ; \mathbb{Z}\right)$, and some orbits in that set may be contractible. This is in agreement with Taubes' study [35] of the structure of such curves in the vicinity of $Z$.

\subsection*{1.4 Brief outline}

What follows is an outline of the remainder of the paper. Section 2 consists of a review of ECH, with a clarification in Section 2.5 of " $L$-flat approximations" which were defined and used in Taubes' isomorphisms [46]. Section 3.1 consists of the relevant facts of the contact 3-manifold $\left(S^{1} \times S^{2}, \lambda_{0}\right)$. Section 3.2 specifies how the overtwisted contact form $\lambda_{0}$ is to be modified, through a particular change in the tubular neighborhood $\mathcal{N}$ of $Z$. Section 3.3 clarifies the a priori difficulties with constructing well-defined counts of curves in $X_{0}=X-\mathcal{N}$; in particular, we have to separate the cases where the relative classes $A \in \operatorname{Rel}_{\omega}(X)$ may be represented by multiply covered exceptional spheres. Section 3.4 specifies the relevant $J$-holomorphic curves when there are no multiply covered exceptional spheres. Section 3.5 specifies the integer weights that are assigned to the $J$-holomorphic curves for the definition of $G r_{X, \omega, J}^{I}(A,[\bar{\eta}])$. Section 3.6 establishes the independence of choices of base points and loops that are used to define the relevant moduli spaces of $J$-holomorphic curves. Section 3.7 clarifies what $G r_{X, \omega, J}^{I}(A,[\bar{\eta}])$ looks like as a class in ECH. Lastly, the appendix clarifies what changes are to be made in this paper when $\omega$ is chosen to have twisted zero-circles.

Acknowledgements
The author is indebted to Michael Hutchings and Clifford Taubes - their guidance and ideas were valuable, crucial, and appreciated. The author also thanks Tomasz Mrowka for helping to understand certain aspects of monopole Floer homology. This paper forms part of the author's Ph.D. thesis. The author was partially supported by NSF grants DMS-1406312, DMS-1344991, DMS-0943745. The author thanks Harvard University for its hospitality during a part of Fall 2015.

\section*{2 Review of pseudoholomorphic curve theory}

The point of this section is to introduce most of the terminology and notations that appear in the later sections. Further information and more complete details are found in [17].
2.1 Orbits with $\lambda$

Let $(Y, \lambda)$ be a closed contact 3-manifold, oriented by $\lambda \wedge d \lambda>0$. Let $\xi=\operatorname{Ker} \lambda$ be the contact structure, oriented by $d \lambda$. Equivalently, $\xi$ is co-oriented by the Reeb vector field $R$ determined by $d \lambda(R, \cdot)=0$ and $\lambda(R)=1$. A Reeb orbit is a map $\gamma: \mathbb{R} / T \mathbb{Z} \rightarrow Y$ for some $T>0$ with $\gamma^{\prime}(t)=R(\gamma(t))$, modulo reparametrization, which is necessarily an $m$-fold cover of an embedded Reeb orbit for some $m \geq 1$. A given Reeb orbit is nondegenerate if the linearization of the Reeb flow around it does not have 1 as an eigenvalue, in which case the eigenvalues are either on the unit circle (such $\gamma$ are elliptic) or on the real axis (such $\gamma$ are hyperbolic). Assume from now on that $\lambda$ is nondegenerate, i.e. all Reeb orbits are nondegenerate, which is a generic property of contact forms.

An orbit set is a finite set of pairs $\Theta=\left\{\left(\Theta_{i}, m_{i}\right)\right\}$ where the $\Theta_{i}$ are distinct embedded Reeb orbits and the $m_{i}$ are positive integers (this set may be empty). An orbit set is admissible if $m_{i}=1$ whenever $\Theta_{i}$ is hyperbolic. Its symplectic action (or "length") is defined by
$$\mathcal{A}(\Theta):=\sum_{i} m_{i} \int_{\Theta_{i}} \lambda \geq 0$$
and its homology class is defined by
$$[\Theta]:=\sum_{i} m_{i}\left[\Theta_{i}\right] \in H_{1}(Y ; \mathbb{Z})$$
For a given $\Gamma \in H_{1}(Y ; \mathbb{Z})$, the ECH chain complex $E C C_{*}(Y, \lambda, J, \Gamma)$ is freely generated over $\mathbb{Z}$ by equivalence classes of pairs $(\Theta, \mathfrak{o})$, where $\Theta$ is an admissible orbit set satisfying $[\Theta]=\Gamma$ and $\mathfrak{o}$ is a choice of ordering of the positive hyperbolic orbits and a $\mathbb{Z} / 2 \mathbb{Z}$ choice for each such orbit, such that $(\Theta, \mathfrak{o})=-\left(\Theta, \mathfrak{o}^{\prime}\right)$ if $\mathfrak{o}$ and $\mathfrak{o}^{\prime}$ differ by an odd permutation. We will suppress the notation of the orientation choices $\mathfrak{o}$. The differential $\partial_{\mathrm{ECH}}$ will be defined momentarily.
2.2 Curves with $J$

Given two contact manifolds $\left(Y_{ \pm}, \lambda_{ \pm}\right)$, possibly disconnected or empty, a strong symplectic cobordism from $\left(Y_{+}, \lambda_{+}\right)$to $\left(Y_{-}, \lambda_{-}\right)$is a compact symplectic manifold $(X, \omega)$ with oriented boundary
$$\partial X=Y_{+} \sqcup-Y_{-}$$
such that $\left.\omega\right|_{Y_{ \pm}}=d \lambda_{ \pm}$. We can always find neighborhoods $N_{ \pm}$of $Y_{ \pm}$in $X$ diffeomorphic to $(-\varepsilon, 0] \times Y_{+}$and $[0, \varepsilon) \times Y_{-}$, such that $\left.\omega\right|_{N_{ \pm}}=d\left(e^{ \pm s} \lambda_{ \pm}\right)$where $s$ denotes the coordinate on ( $-\varepsilon, 0$ ]. We then glue symplectization ends to $X$ to obtain the completion
$$\bar{X}:=\left((-\infty, 0] \times Y_{-}\right) \cup_{Y_{-}} X \cup_{Y_{+}}\left([0, \infty) \times Y_{+}\right)$$
of $X$, a noncompact symplectic 4-manifold whose symplectic form is also denoted by $\omega$. We will also use the notation $\bar{X}$ to denote the symplectization $\mathbb{R} \times Y$ of $(Y, \lambda)$, with $\omega=d\left(e^{s} \lambda\right)$.

An almost complex structure $J$ on a symplectization $\left(\mathbb{R} \times Y, d\left(e^{s} \lambda\right)\right)$ is symplectization-admissible if it is $\mathbb{R}$-invariant; $J\left(\partial_{s}\right)=R$; and $J(\xi) \subseteq \xi$ such that $d \lambda(v, J v) \geq 0$ for $v \in \xi$. An almost complex structure $J$ on the completion $\bar{X}$ is cobordism-admissible if it is $\omega$-compatible on $X$ and agrees with symplectization-admissible almost complex structures on the ends $[0, \infty) \times Y_{+}$and $(-\infty, 0] \times Y_{-}$.

Remark 2.1. With respect to the Riemannian metric defined by the symplectic form and the admissible almost complex structure, the symplectic form is a self-dual harmonic 2-form.

Given a cobordism-admissible $J$ on $\bar{X}$ and orbit sets $\Theta^{+}=\left\{\left(\Theta_{i}^{+}, m_{i}^{+}\right)\right\}$in $Y_{+}$and $\Theta^{-}=$ $\left\{\left(\Theta_{j}^{-}, m_{j}^{-}\right)\right\}$in $Y_{-}$, a $J$-holomorphic curve $\mathcal{C}$ in $\bar{X}$ from $\Theta^{+}$to $\Theta^{-}$is defined as follows. It is a $J$-holomorphic map $\mathcal{C} \rightarrow \bar{X}$ whose domain is a possibly disconnected punctured compact Riemann surface, defined up to composition with biholomorphisms of the domain, with positive ends of $\mathcal{C}$ asymptotic to covers of $\Theta_{i}^{+}$with total multiplicity $m_{i}^{+}$, and with negative ends of $\mathcal{C}$ asymptotic to covers of $\Theta_{j}^{-}$with total multiplicity $m_{j}^{-}$(see [17, §3.1]). The moduli space of such curves is denoted by $\mathcal{M}\left(\Theta^{+}, \Theta^{-}\right)$, but where two such curves are considered equivalent if they represent the same current ${ }^{5}$ in $\bar{X}$, and in the case of a symplectization $\bar{X}=\mathbb{R} \times Y$ the equivalence includes translation of the $\mathbb{R}$-coordinate. An element $\mathcal{C} \in \mathcal{M}\left(\Theta^{+}, \Theta^{-}\right)$can thus be viewed as a finite set of pairs $\left\{\left(C_{k}, d_{k}\right)\right\}$ or formal sum $\sum d_{k} C_{k}$, where the $C_{k}$ are distinct irreducible somewhere-injective $J$-holomorphic curves and the $d_{k}$ are positive integers.

Let $H_{2}\left(X, \Theta^{+}, \Theta^{-}\right)$be the set of relative 2-chains $\Sigma$ in $X$ such that
$$\partial \Sigma=\sum_{i} m_{i}^{+} \Theta_{i}^{+}-\sum_{j} m_{j}^{-} \Theta_{j}^{-}$$
modulo boundaries of 3-chains. It is an affine space over $H_{2}(X ; \mathbb{Z})$, and every curve $\mathcal{C}$ defines a relative class $[\mathcal{C}] \in H_{2}\left(X, \Theta^{+}, \Theta^{-}\right)$.

A broken $J$-holomorphic curve (of height $n$ ) from $\Theta^{+}$to $\Theta^{-}$is a finite sequence of holomorphic curves $\left\{\mathcal{C}_{k}\right\}_{1 \leq k \leq n}$ and orbit sets $\left\{\Theta_{k}^{ \pm}\right\}_{1 \leq k \leq n+1}$, such that there exists an integer $1 \leq k_{0} \leq n$ such that the following holds:
\begin{itemize}
\item[-] $\left\{\Theta_{k}^{+}\right\}_{k \geq k_{0}}$ belong to $\left(Y_{+}, \lambda_{+}\right)$and $\left\{\Theta_{k}^{-}\right\}_{k \leq k_{0}}$ belong to $\left(Y_{-}, \lambda_{-}\right)$,
\item[-] $\Theta_{1}^{-}=\Theta^{-}$and $\Theta_{n+1}^{+}=\Theta^{+}$and $\Theta_{k}^{-}=\Theta_{k-1}^{+}$for $k>1$,
\item[-] $\mathcal{C}_{k} \in \mathcal{M}\left(\Theta_{k}^{+}, \Theta_{k}^{-}\right)$with respect to $\left.J\right|_{\mathbb{R} \times Y_{+}}$for $k>k_{0}$ (symplectization levels),
\item[-] $\mathcal{C}_{k} \in \mathcal{M}\left(\Theta_{k}^{+}, \Theta_{k}^{-}\right)$with respect to $\left.J\right|_{\mathbb{R} \times Y_{-}}$for $k<k_{0}$ (symplectization levels),
\item[-] $\mathcal{C}_{k_{0}} \in \mathcal{M}\left(\Theta_{k_{0}}^{+}, \Theta_{k_{0}}^{-}\right)$with respect to $J$ (cobordism level),
\item[-] $\mathcal{C}_{k}$ is not a union of unbranched covers of $\mathbb{R}$-invariant cylinders for $k \neq k_{0}$.
\end{itemize}

\footnotetext{
${ }^{5}$ For example, if $\mathcal{C}$ is a $d$-fold cover of an embedded curve $C$, then the associated current is the $\mathbb{R}$-valued functional on $\Omega^{2}(\bar{X})$ given by $\sigma \mapsto d \int_{C} \sigma$. In particular, all branching data of the cover has been lost.
}

The moduli space of such broken curves is denoted by $\overline{\mathcal{M}\left(\Theta^{+}, \Theta^{-}\right)}$. There is an analogous definition of a broken $J$-holomorphic current, with the further requirement that each current $\mathcal{C}_{k}$ for $k \neq k_{0}$ is not a union of $\mathbb{R}$-invariant cylinders with multiplicities.

There are relevant versions of Gromov compactness for the aforementioned moduli spaces. Any sequence of $J$-holomorphic curves $\left\{C^{\nu}\right\}_{\nu \geq 1} \subset \mathcal{M}\left(\Theta^{+}, \Theta^{-}\right)$with fixed genus and uniform energy bound has a subsequence which converges in the sense of SFT compactness [4] to a broken $J$ -holomorphic curve. Any sequence of $J$-holomorphic currents $\left\{\mathcal{C}^{\nu}\right\}_{\nu \geq 1} \subset \mathcal{M}\left(\Theta^{+}, \Theta^{-}\right)$with uniform energy bound has a subsequence which converges in an appropriate sense to a broken $J$-holomorphic current $\left(\mathcal{C}_{1}, \ldots, \mathcal{C}_{n}\right) \in \overline{\mathcal{M}\left(\Theta^{+}, \Theta^{-}\right)}$, such that
$$\sum_{k=1}^{n}\left[\mathcal{C}_{k}\right]=\left[\mathcal{C}^{\nu}\right] \in H_{2}\left(X, \Theta^{+}, \Theta^{-}\right)$$
for $\nu$ sufficiently large (see [35, Proposition 3.3] and [17, Lemma 5.11]).

\subsection*{2.3 ECH}

Denote by $\tau$ a homotopy class of symplectic trivializations of the restrictions of $\xi_{ \pm}=\operatorname{Ker} \lambda_{ \pm}$ to the embedded orbits appearing in the orbit sets $\Theta^{ \pm}$. The ECH index of a current, or more generally of a class in $H_{2}\left(X, \Theta^{+}, \Theta^{-}\right)$, is given by
$$I(\mathcal{C})=c_{\tau}(\mathcal{C})+Q_{\tau}(\mathcal{C})+C Z_{\tau}^{I}(\mathcal{C})$$
where $c_{\tau}(\mathcal{C})$ denotes the relative first Chern class of $\operatorname{det} T \bar{X}$ over $\mathcal{C}$ with respect to $\tau$ (see [17, §3.2]), $Q_{\tau}(\mathcal{C})$ denotes a relative self-intersection pairing with respect to $\tau$ (see [17, §3.3]), and
$$C Z_{\tau}^{I}(\mathcal{C})=\sum_{i} \sum_{k=1}^{m_{i}^{+}} C Z_{\tau}\left(\Theta_{i}^{+k}\right)-\sum_{j} \sum_{k=1}^{m_{j}^{-}} C Z_{\tau}\left(\Theta_{j}^{-k}\right)$$
is a sum of Conley-Zehnder indices (of covers of orbits in $\Theta^{ \pm}$) with respect to $\tau$. The definition of the Conley-Zehnder index will not be reviewed here (see [17, §3.2]), but it is noted that we can adjust $\tau$ over a given embedded orbit $\gamma$ so that
$$C Z_{\tau}\left(\gamma^{m}\right)=0$$
when $\gamma$ is positive hyperbolic,
$$C Z_{\tau}\left(\gamma^{m}\right)=m$$
when $\gamma$ is negative hyperbolic, and
$$C Z_{\tau}\left(\gamma^{m}\right)=2\lfloor m \theta\rfloor+1$$
when $\gamma$ is elliptic. Here, the linearization of the Reeb flow around an elliptic orbit is conjugate to a rotation by angle $2 \pi \theta$ with respect to $\tau$, and $\theta \in \mathbb{R}-\mathbb{Q}$ is the rotation number. The equivalence class of $\theta$ in $\mathbb{R} / \mathbb{Z}$ is the rotation class of the elliptic orbit, which does not depend on $\tau$.

The Fredholm index of a curve $\mathcal{C}$, having $i^{\text {th }}$ positive end asymptotic to $\alpha_{i}$ with multiplicity $m_{i}$ and $j^{\text {th }}$ negative end asymptotic to $\beta_{j}$ with multiplicity $n_{j}$, is given by
$$\operatorname{ind}(\mathcal{C})=-\chi(\mathcal{C})+2 c_{\tau}(\mathcal{C})+C Z_{\tau}^{\mathrm{ind}}(\mathcal{C})$$
where
$$C Z_{\tau}^{\mathrm{ind}}(\mathcal{C})=\sum_{i} C Z_{\tau}\left(\alpha_{i}^{m_{i}}\right)-\sum_{j} C Z_{\tau}\left(\beta_{j}^{n_{j}}\right)$$
If $\mathcal{C}$ has no multiply covered components then we have the index inequality
$$\operatorname{ind}(\mathcal{C}) \leq I(\mathcal{C})-2 \delta(\mathcal{C})$$
where $\delta(\mathcal{C})$ denotes an algebraic count of singularities of $\mathcal{C}$ with positive integer weights (see [17, §3.4]). If $J$ is furthermore generic then $\mathcal{M}\left(\Theta^{+}, \Theta^{-}\right)$is an $\operatorname{ind}(\mathcal{C})$-dimensional manifold near $\mathcal{C}$.

Denote by $\mathcal{M}_{I}\left(\Theta^{+}, \Theta^{-}\right)$the subset of elements in $\mathcal{M}\left(\Theta^{+}, \Theta^{-}\right)$that have ECH index $I$. In a symplectization $\bar{X}=\mathbb{R} \times Y$ there is a characterization of currents with low ECH index. That is, if $J$ is generic and $\mathcal{C}$ is a $J$-holomorphic current in the symplectization $\bar{X}=\mathbb{R} \times Y$ then
\begin{itemize}
\item[-] $I(\mathcal{C}) \geq 0$, with equality if and only if $\mathcal{C}$ is a union of $\mathbb{R}$-invariant cylinders,
\item[-] If $I(\mathcal{C})=1$ then $\mathcal{C}=\mathcal{C}_{0} \sqcup C_{1}$, where $C_{1}$ is an embedded ind = $I=1$ curve and $I\left(\mathcal{C}_{0}\right)=0$.
\end{itemize}
See [17, Proposition 3.7] for a proof. Given admissible orbit sets $\Theta^{ \pm}$of $(Y, \lambda)$, the coefficient $\left\langle\partial_{\mathrm{ECH}} \Theta^{+}, \Theta^{-}\right\rangle$is the signed ${ }^{6}$ count of elements in $\mathcal{M}_{1}\left(\Theta^{+}, \Theta^{-}\right)$. If $J$ is generic then $\partial_{\mathrm{ECH}}$ is well-defined and $\partial_{\text {ECH }}^{2}=0$. The resulting homology is independent of the choice of $J$, depends only on $\xi$ and $\Gamma$, and is denoted by $E C H_{*}(Y, \xi, \Gamma)$.

If $Y$ is connected then Taubes constructed a canonical isomorphism of relatively graded modules
$$E C H_{*}(Y, \xi, \Gamma) \cong \widehat{H M}^{-*}\left(Y, \mathfrak{s}_{\xi}+\Gamma\right)$$
where $\widehat{H M}^{-*}(\cdot)$ is a version of Seiberg-Witten Floer cohomology defined by Kronheimer and Mrowka 22 and $\mathfrak{s}_{\xi}$ is a certain spin-c structure determined by $\xi$. Moreover, both homologies admit absolute gradings by homotopy classes of oriented 2-plane fields on $Y$ and Taubes' isomorphism preserves these gradings (see [7]).

\subsection*{2.4 Gradings and U-maps}

Assume $Y$ to be connected in this section. For each $\Gamma$ there is a canonical absolute $\mathbb{Z} / 2 \mathbb{Z}$ grading on $E C H_{*}(Y, \xi, \Gamma)$ by the parity of the number of positive hyperbolic Reeb orbits in an admissible orbit set $\Theta$. The total sum
$$E C H_{*}(Y, \xi):=\bigoplus_{\Gamma \in H_{1}(Y ; \mathbb{Z})} E C H_{*}(Y, \xi, \Gamma)$$
has an absolute grading by homotopy classes of oriented 2-plane fields on $Y$ (see [14, §3]), the set of which is denoted by $J(Y)$. This grading of an admissible orbit set $\Theta$ is denoted by $|\Theta|$.

As described in [14, §3], [22, §28], and [10, §4], there is a well-defined map $J(Y) \rightarrow \operatorname{Spin}^{c}(Y)$ with the following properties. If $H^{2}(Y ; \mathbb{Z})$ has no 2-torsion then the Euler class of the given 2-plane field uniquely determines the corresponding spin-c structure. There is a transitive $\mathbb{Z}$-action on $J(Y)$ whose orbits correspond to the spin-c structures: If $[\xi] \in J(Y)$ then $[\xi]+n$ is the homotopy class

\footnotetext{
${ }^{6}$ The moduli spaces are coherently oriented in the sense of [20, §9].
}
of a 2-plane field which agrees with $\xi$ outside a small ball $B^{3} \subset Y$ and disagrees with $\xi$ on $B^{3}$ by a map $\left(B^{3}, \partial B^{3}\right) \rightarrow(S O(3),\{\mathbb{1}\})$ of degree $2 n .{ }^{7}$ A given orbit $J(Y, \mathfrak{s})$ is freely acted on by $\mathbb{Z}$ if and only if the corresponding Euler class is torsion.

With that said, $E C H_{*}(Y, \xi, \Gamma)$ has a relative $\mathbb{Z} / d \mathbb{Z}$ grading, where $d$ denotes the divisibility of $c_{1}(\xi)+2 \mathrm{PD}(\Gamma)$ in $H^{2}(Y ; \mathbb{Z}) /$ Torsion. It is refined by the absolute grading and satisfies
$$\left|\Theta^{+}\right|-\left|\Theta^{-}\right| \equiv I(\Sigma) \quad \bmod d$$
for any $\Sigma \in H_{2}\left(Y, \Theta^{+}, \Theta^{-}\right)$, thanks to the index ambiguity formula [17, Equation 3.6].
Similarly to the degree -1 ECH differential, there is a degree -2 chain map
$$U_{y}: E C H_{*}(Y, \xi, \Gamma) \rightarrow E C H_{*-2}(Y, \xi, \Gamma)$$
that counts ECH index 2 currents passing through an a priori chosen base point $(0, y) \in \mathbb{R} \times Y$, where $y$ does not lie on any Reeb orbit (see [17, §3.8]). Such a current is of the form $\mathcal{C}_{0} \sqcup C_{2}$, where $I\left(\mathcal{C}_{0}\right)=0$ and $C_{2}$ is an embedded $\operatorname{ind}\left(C_{1}\right)=I\left(C_{1}\right)=2$ curve passing through $(0, y)$. On the level of homology this $U$-map does not depend on the choice of base point.

\subsection*{2.5 L-flat approximations}

The symplectic action induces a filtration on the ECH chain complex. For a positive real number $L$, the $L$-filtered $E C H$ is the homology of the subcomplex $E C C_{*}^{L}(Y, \lambda, J, \Gamma)$ spanned by admissible orbit sets of action less than $L$. The ordinary ECH is recovered by taking the direct limit over $L$, via maps induced by inclusions of the filtered chain complexes.

Let $u: C \rightarrow \bar{X}$ be an immersed connected $J$-holomorphic curve and denote by $N_{C}$ its normal bundle. The linearization of the $J$-holomorphic equation for $C$ defines its deformation operator, a 1st order elliptic differential operator
$$D_{C}: L_{1}^{2}\left(N_{C}\right) \rightarrow L^{2}\left(T^{0,1} C \otimes N_{C}\right), \quad \eta \mapsto \bar{\partial} \eta+\nu_{C} \eta+\mu_{C} \bar{\eta}$$
where the appropriate sections $\nu_{C} \in \Gamma\left(T^{0,1} C\right)$ and $\mu_{C} \in \Gamma\left(T^{0,1} C \otimes N_{C}^{2}\right)$ are determined by the covariant derivatives of $J$ in directions normal to $C, \bar{\partial}$ is the d-bar operator arising from the Hermitian structure on $N_{C}$, and $\bar{\eta}$ denotes the conjugate of $\eta$ in $N_{C}^{-1}$. Let $N_{C}$ and $T^{0,1} C$ be suitably trivialized on an end of $C$ asymptotic to a Reeb orbit $\gamma$. Then $D_{C}$ is asymptotic (in the sense of [49, §2]) to the asymptotic operator associated with $\gamma$,
$$L_{\gamma}: L_{1}^{2}\left(\gamma^{*} \xi\right) \rightarrow L^{2}\left(\gamma^{*} \xi\right), \quad \eta \mapsto \frac{i}{2} \partial_{t} \eta+\nu \eta+\mu \bar{\eta}$$
and the pair $\left(\nu_{C}, \mu_{C}\right)$ is asymptotic to the pair $(\nu, \mu)$ over $\gamma$.
For a fixed $L>0$ it will be convenient to modify $\lambda$ and $J$ on small tubular neighborhoods of all Reeb orbits of action less than $L$, in order to relate $J$-holomorphic curves to Seiberg-Witten theory most easily. The desired modifications of $(\lambda, J)$ are called $L$-flat approximations, and were introduced by Taubes in [46, Appendix] and [48, Proposition 2.5]. They induce isomorphisms on the $L$-filtered ECH chain complex, but for the point of this paper (see Lemma 3.9 and Section 3.5) we really only need to know that:

\footnotetext{
${ }^{7}$ This convention is opposite to that used in 22.
}
\begin{itemize}
\item[-] The Reeb orbits of action less than $L$ (and their action) are not altered,
\item[-] The $C^{1}$-norm of the difference between the contact forms can be made as small as desired,
\item[-] The pair $(\nu, \mu)$ associated with an elliptic orbit with rotation number $\theta$ in a given trivialization is modified to $\left(\frac{1}{2} \theta, 0\right)$, so that its asymptotic operator is complex linear.
\end{itemize}

Remark 2.2. The proof of Theorem 1.9 in [9] will make crucial use of Taubes' isomorphism between ECH and Seiberg-Witten Floer cohomology, and that makes use of $L$-flat approximations. The key fact here is that Taubes' isomorphism actually exists on the $L$-filtered chain complex level, for which $L$-flat orbit sets are in bijection with Seiberg-Witten solutions of "energy" less than $2 \pi L$.

\section*{3 Towards a near-symplectic Gromov invariant}

This section spells out the proof of Theorem 1.7. We introduce the contact form on $S^{1} \times S^{2}$ that was studied in the past by Taubes, and then we find a different contact form on $S^{1} \times S^{2}$ whose contact dynamics is "tame" in a certain sense. This new contact form is better suited for establishing well-defined counts of $J$-holomorphic curves in $X-Z$. We also find a tubular neighborhood $\mathcal{N}$ of $Z$ in $X$ for which the induced contact dynamics on its boundary $\partial \mathcal{N}$ is given by our new contact form. Then we construct the relevant moduli spaces of $J$-holomorphic curves in $X-\mathcal{N}$ which are to be counted, including their integer weights, and from there we define the relevant class in ECH. We retain the same assumptions that are made in Section 1.3.

\subsection*{3.1 Taubes' contact form}

The main focus of this paper is $S^{1} \times S^{2}$ equipped with Taubes' contact form
$$\lambda_{0}=-\left(1-3 \cos ^{2} \theta\right) d t-\sqrt{6} \cos \theta \sin ^{2} \theta d \varphi$$
for coordinates $(t, \theta, \varphi) \in S^{1} \times S^{2}$ such that $0 \leq t \leq 2 \pi$ and $0 \leq \theta \leq \pi$ and $0 \leq \varphi \leq 2 \pi$. In order for $\lambda_{0} \wedge d \lambda_{0}$ to be positive, $S^{1} \times S^{2}$ is oriented by the 3-form
$$-\sin \theta d t d \theta d \varphi$$
The $S^{1}$-factor will be oriented by the 1-form $-d t$, and the $S^{2}$-factor will be oriented by the 2-form $\sin \theta d \theta d \varphi$. This contact manifold was originally studied in [12, 29, 41], and we now describe some details that will be of use later on.

The Reeb field associated with $\lambda_{0}$ is
$$\frac{-1}{1+3 \cos ^{4} \theta}\left(\left(1-3 \cos ^{2} \theta\right) \partial_{t}+\sqrt{6} \cos \theta \partial_{\varphi}\right)$$
The closed Reeb orbits live in the constant $\theta=\theta_{0}$ slices of $S^{1} \times S^{2}$ satisfying
$$\theta_{0} \in\{0, \pi\} \quad \text { or } \quad \frac{\sqrt{6} \cos \theta_{0}}{1-3 \cos ^{2} \theta_{0}} \in \mathbb{Q} \cup\{ \pm \infty\}$$
The two nondegenerate orbits at $\theta_{0} \in\{0, \pi\}$ are elliptic. They are denoted by $e_{0}, e_{\pi}$ and called the exceptional orbits. The remaining orbits are degenerate, there being an $S^{1}$-family of orbits for each such $\theta_{0}$. In other words,
$$T\left(\theta_{0}\right):=\left\{\text { constant } \theta=\theta_{0} \text { slice }\right\} \subset S^{1} \times S^{2}$$
is a torus foliated by orbits. This contact form is thus not nondegenerate, but it is "Morse-Bott" in the sense of [3].

Remark 3.1. The contact structure $\xi_{0}=\operatorname{Ker} \lambda_{0}$ is overtwisted, as pointed out in [41, §2.f] and [12, Proposition 9]. A well-known result of Hofer states that an overtwisted contact 3-manifold must have at least one contractible orbit, and indeed we see that $T\left(\arccos \left(\frac{1}{\sqrt{3}}\right)\right)$ and $T\left(\arccos \left(-\frac{1}{\sqrt{3}}\right)\right)$ consist of contractible orbits. The remaining orbits are all homologically nontrivial.

With the contact structure $\xi_{0}$ oriented by $d \lambda_{0}$, we compute
$$c_{1}\left(\xi_{0}\right)=-2 \in \mathbb{Z} \cong H^{2}\left(S^{1} \times S^{2} ; \mathbb{Z}\right)$$
by using the section $\sin \theta \partial_{\theta} \in \Gamma\left(\xi_{0}\right)$ and noting that the orientation on $\xi_{0}$ disagrees with the orientation on the $S^{2}$-factor at $\theta=0$ and $\theta=\pi$. The spin-c structure $\mathfrak{s}_{\xi}$ determined by $\xi_{0}$ satisfies
$$c_{1}\left(\mathfrak{s}_{\xi}+1\right)=c_{1}\left(\mathfrak{s}_{\xi}\right)+2=c_{1}\left(\xi_{0}\right)+2=0$$
and so Taubes' isomorphism (2.1) reads
$$E C H_{j}\left(S^{1} \times S^{2}, \xi_{0}, 1\right) \cong \widehat{H M}^{j}\left(S^{1} \times S^{2}, \mathfrak{s}_{\xi}+1\right)$$
where $j \in J\left(S^{1} \times S^{2}, \mathfrak{s}_{\xi}+1\right) \cong \mathbb{Z}$ as $\mathbb{Z}$-sets. There is a unique class $j=\left[\xi_{*}\right]$ represented by an oriented 2-plane field $\xi_{*}$ on $S^{1} \times S^{2}$ which has vanishing Euler class and is invariant under rotations of the $S^{1}$-factor.

Proposition 3.2. If $\Gamma \in H_{1}\left(S^{1} \times S^{2} ; \mathbb{Z}\right)$ is not the oriented generator 1 then
$$E C H_{*}\left(S^{1} \times S^{2}, \xi_{0}, \Gamma\right)=0$$
In the remaining case $\Gamma=1, E C H_{j}\left(S^{1} \times S^{2}, \xi_{0}, 1\right)$ is zero in gradings below $j=\left[\xi_{*}\right]$, and for each $n \geq 0$
$$E C H_{\left[\xi_{*}\right]+n}\left(S^{1} \times S^{2}, \xi_{0}, 1\right) \cong \mathbb{Z}$$
The homotopy class $\left[\xi_{*}\right]$ has odd parity under the absolute $\mathbb{Z} / 2 \mathbb{Z}$ grading on ECH. After perturbing $\lambda_{0}$ to a nondegenerate contact form, $\left[\xi_{*}\right]$ is generated by a single positive hyperbolic orbit wrapping positively once around the $S^{1}$-factor in $T\left(\frac{\pi}{2}\right)=S^{1} \times\{$ equator $\}$.

Proof. The first two statements are proved in [22, §IX.36] for the relevant version of Seiberg-Witten Floer homology, so they follow for ECH via Taubes' isomorphism (2.1). The latter two statements follow from the relevant statements in [18, §12.2.1]. This reference uses a "twisted" version of ECH that remembers some information about the relative homology classes of the $J$-holomorphic curves in $S^{1} \times S^{2}$, but the untwisted version may be obtained via a spectral sequence in [18, §8.1]. \(\square\)

In the upcoming section, $\lambda_{0}$ will be modified in various ways. We now preemptively analyze the contact form $e^{f} \lambda_{0}$ for a given smooth function $f: S^{1} \times S^{2} \rightarrow \mathbb{R}$ depending only on the $\theta$ coordinate, whose contact structure is nonetheless $\xi_{0}$. Such a contact form can be written as
$$\lambda=a_{1}(\theta) d t+a_{2}(\theta) d \varphi$$
for some smooth pair
$$a=\left(a_{1}, a_{2}\right):[0, \pi] \rightarrow \mathbb{R}^{2}-\{(0,0)\}$$

Let $a \times a^{\prime}:=a_{1} a_{2}^{\prime}-a_{2} a_{1}^{\prime}$, where the tick-mark signifies the derivative with respect to $\theta$. The condition for $\lambda$ to be a positive contact form is then
$$\frac{a \times a^{\prime}(\theta)}{\sin \theta}<0$$
for all $\theta \in[0, \pi]$. For $\theta \in(0, \pi)$ the Reeb field of $\lambda$ is
$$R=\frac{1}{a \times a^{\prime}(\theta)}\left(a_{2}^{\prime}(\theta) \partial_{t}-a_{1}^{\prime}(\theta) \partial_{\varphi}\right)$$
and the condition (3.2), for which $T\left(\theta_{0}\right) \subset S^{1} \times S^{2}$ is a torus foliated by orbits, is now given by
$$\frac{a_{1}^{\prime}\left(\theta_{0}\right)}{a_{2}^{\prime}\left(\theta_{0}\right)} \in \mathbb{Q} \cup\{ \pm \infty\}$$
Every embedded orbit in $T\left(\theta_{0}\right)$ represents the same class in $H_{1}\left(T\left(\theta_{0}\right) ; \mathbb{Z}\right)$ and they all have the same action $\mathcal{A}\left(\theta_{0}\right)>0$. There are also two exceptional nondegenerate elliptic orbits at $\theta_{0} \in\{0, \pi\}$.

Lemma 3.3. The exceptional elliptic orbit at $\theta=\theta_{0}$, for $\theta_{0} \in\{0, \pi\}$, has rotation class
$$\left(\operatorname{sign} \lim _{\theta \rightarrow \theta_{0}} \frac{-a_{2}^{\prime}(\theta)}{\sin \theta \cos \theta}\right) \lim _{\theta \rightarrow \theta_{0}} \frac{a_{1}^{\prime}\left(\theta_{0}\right)}{a_{2}^{\prime}\left(\theta_{0}\right)} \quad \bmod 1$$
In particular, the rotation class for either exceptional orbit of $\lambda_{0}$ is $\sqrt{\frac{3}{2}} \bmod 1$.
Proof. The Reeb field along each exceptional orbit is
$$R=\frac{1}{a_{1}\left(\theta_{0}\right)} \partial_{t}$$
Note that $a_{1}\left(\theta_{0}\right)>0$, because $\lambda_{0}$ satisfies it and $e^{f}$ is a positive rescaling. Thus, in a neighborhood of $\theta=\theta_{0}$ the Reeb flow is in the positive $t$-direction and wraps - $\lim _{\theta \rightarrow \theta_{0}} a_{1}^{\prime}\left(\theta_{0}\right) / a_{2}^{\prime}\left(\theta_{0}\right)$ times around the $\varphi$-coordinate circle after traversing once around the $t$-coordinate circle. The rotation class of each elliptic orbit is thus
$$\epsilon \cdot \lim _{\theta \rightarrow \theta_{0}} \frac{-a_{1}^{\prime}\left(\theta_{0}\right)}{a_{2}^{\prime}\left(\theta_{0}\right)} \bmod 1$$
where $\epsilon= \pm 1$ depending on whether the $\varphi$-coordinate circle is positively or negatively oriented with respect to the orientation of the contact planes $T_{\theta_{0}} S^{2}$ given by $d \lambda$. To determine $\epsilon$, we use the Cartesian coordinates
$$\left\{\begin{array}{l}
(x, y)=(\sin \theta \cos \varphi, \sin \theta \sin \varphi) \\
d x d y=\sin \theta \cos \theta d \theta d \varphi
\end{array}\right.$$
near each pole of $S^{2}$. In these coordinates,
$$\left.d \lambda\right|_{T_{\theta_{0}} S^{2}}=\left(\lim _{\theta \rightarrow \theta_{0}} \frac{a_{2}^{\prime}(\theta)}{\sin \theta \cos \theta}\right) d x d y$$
and $\epsilon$ is precisely the sign of this paranthetical expression. \(\square\)

\subsection*{3.2 Changing Taubes' contact form}

In order to obtain well-defined counts of $J$-holomorphic curves which represent a given class $A \in \operatorname{Rel}_{\omega}(X)$, we will need to ensure a bound on their energy as well as a bound on the symplectic action of their orbit sets. As explained in [15], these bounds are given by a particular quantity $\rho(A)$, defined as follows:

Let $u: \Sigma \rightarrow X_{0}$ be any given smooth map which represents $A$, where $\Sigma$ is a compact oriented smooth surface with boundary and $u(\partial \Sigma) \subset \partial X_{0}$. Then
$$\rho(A):=\int_{\Sigma} \omega+\int_{\partial \Sigma} e^{-1} \lambda_{0}$$
This quantity is additive with respect to composition of symplectic cobordisms, and it vanishes on exact symplectic cobordisms (recall that a symplectic cobordism is exact if the contact form on the boundary extends as a global primitive 1-form of the symplectic form). Subsequently, $\rho(A)$ does not change if the symplectic cobordism $\left(X_{0}, \omega\right)$ is modified by composing it with an exact symplectic cobordism.

Remark 3.4. We can view $\rho: \operatorname{Rel}_{\omega}(X) \rightarrow \mathbb{R}$ as either a measure of the failure of exactness of $\omega$, or as an energy. In particular, if $(X, \omega)$ were a closed symplectic manifold, i.e. $\partial X_{0}=\varnothing$ and $A \in H_{2}(X ; \mathbb{Z})$, then $\rho(A)=A \cdot[\omega]$.

Now, three modifications will be made to $\lambda_{0}$. First, we will want all Reeb orbits to be nondegenerate in order to define ECH. Second, we will want all Reeb orbits of action less than $\rho(A)$ to be $\rho(A)$-flat in order to relate the $J$-holomorphic curves to Seiberg-Witten theory. Third, we will want the elliptic orbits of action less than $\rho(A)$, especially the exceptional orbits, to be " $\rho(A)$-positive" in order to guarantee transversality of the relevant moduli spaces of $J$-holomorphic curves (see Remark 3.10 below). As defined in [16], the quantifier " $\rho(A)$-positive" means the following:

Definition 3.5. Fix $L>0$. Let $\gamma$ be a nondegenerate embedded elliptic orbit with rotation class $\theta \in \mathbb{R} / \mathbb{Z}$ and symplectic action $\mathcal{A}(\gamma)<L$. Then $\gamma$ is $L$-positive if $\theta \in(0, \mathcal{A}(\gamma) / L) \bmod 1$.

A key property of any $L$-positive elliptic orbit $\gamma$ is that if $L$ is much greater than $\mathcal{A}(\gamma)$, then $C Z_{\tau}\left(\gamma^{m}\right)=1$ for all $m<L / \mathcal{A}(\gamma)$ and a particular choice of trivialization $\tau$ of $\gamma^{*} \xi_{0}$.

The next lemma below shows how to modify the Morse-Bott orbits, in the sense of [3] and adapted from [16, Lemma 5.4]. For a given positive contact form written as (3.3), the lemma requires the following technical condition
$$a^{\prime} \times a^{\prime \prime}\left(\theta_{0}\right)<0$$
for all $\theta_{0} \in(0, \pi)$ that satisfy (3.4). Note that $\lambda_{0}$ satisfies the technical condition.
Lemma 3.6. Suppose the positive contact form $\lambda=a_{1}(\theta) d t+a_{2}(\theta) d \varphi$ satisfies the technical condition (3.7). Then for every $L>0$ and sufficiently small $\delta>0$, there exists a perturbation $e^{f_{\delta, L}} \lambda$ of $\lambda$ satisfying the following properties:
\begin{itemize}
\item[-] $f_{\delta, L} \in C^{\infty}\left(S^{1} \times S^{2}\right)$ satisfies $\left\|f_{\delta, L}\right\|_{C^{0}}<\delta$,
\item[-] $e^{f_{\delta, L}} \lambda$ agrees with $\lambda$ near the exceptional orbits at $\theta_{0} \in\{0, \pi\}$,
\item[-] Each family of orbits in the torus $T\left(\theta_{0}\right)$ with $\mathcal{A}\left(\theta_{0}\right)<L$ is replaced by a positive hyperbolic orbit and an $L$-positive elliptic orbit, both of action less than $L$ and within $\delta$ of $\mathcal{A}\left(\theta_{0}\right)$,
\item[-] $e^{f_{\delta, L}} \lambda$ has no other embedded orbits of action less than $L$.
\end{itemize}

Proof. The function $f_{\delta, L}$ is given by Bourgeois' perturbation [3] of $\lambda$, which breaks up each $T\left(\theta_{0}\right)$ into two embedded nondegenerate orbits of action slightly less than $\mathcal{A}\left(\theta_{0}\right)$ in addition to orbits of action greater than $L$. Namely, there is a positive hyperbolic orbit and an elliptic orbit $e_{\theta_{0}}$, both representing the same class in $H_{1}\left(T\left(\theta_{0}\right) ; \mathbb{Z}\right)$. For sufficiently small perturbations there cannot exist other orbits of action less than $L$, otherwise we would find a sequence $\left\{\left(\gamma_{k}, \delta_{k}\right)\right\}_{k \in \mathbb{N}}$ of such orbits of uniformly bounded action $L$ and perturbations $\delta_{k} \rightarrow 0$ for which a subsequence converges to one of the original degenerate orbits (by the Arzelà-Ascoli theorem), yielding a contradiction.

It remains to compute the rotation class of the elliptic orbit created from each Morse-Bott family. Let $a^{\perp}:=a_{2}(\theta) \partial_{t}-a_{1}(\theta) \partial_{\varphi}$. The basis $\left\langle\partial_{\theta}, a^{\perp}\right\rangle$ defines a trivialization $\tau$ of the contact structure $\xi$ over $S^{1} \times\left(S^{2}-\{\right.$ poles $\left.\}\right)$, since
$$d \lambda\left(\partial_{\theta}, a^{\perp}\right)=-a \times a^{\prime}(\theta)>0$$
for $0<\theta<\pi$. We then compute the Lie derivatives of the Reeb field $R$,
$$\mathcal{L}_{\partial_{\theta}} R=-\frac{a^{\prime} \times a^{\prime \prime}}{\left(a \times a^{\prime}\right)^{2}} a^{\perp}, \quad \mathcal{L}_{a^{\perp}} R=0$$
to see that the linearized Reeb flow along $T\left(\theta_{0}\right)$ induces the linearized return map
$$P_{T\left(\theta_{0}\right)}:=\mathbb{1}+\left(\begin{array}{cc}
0 & 0 \\
r\left(\theta_{0}\right) \mathcal{A}\left(\theta_{0}\right) & 0
\end{array}\right)$$
on $\xi$ in the chosen basis, where
$$r:=-\frac{a^{\prime} \times a^{\prime \prime}}{\left(a \times a^{\prime}\right)^{2}}$$
The linearized return map along $e_{\theta_{0}}$, denoted $P_{\theta_{0}}$, is a perturbation of $P_{T\left(\theta_{0}\right)}$. To clarify the dependence of this perturbation on $\delta$, we first note that Bourgeois' factor $e^{f_{\delta, L}}$ takes the form $(1+\delta \tilde{f})$ for some function $\tilde{f}$ that is compactly supported in neighborhoods of the tori $T\left(\theta_{0}\right)$ and does not depend on $\delta$. We then claim that the perturbed Reeb field takes the form $R+\mathcal{O}(\delta) R_{1}$, as in [3, Lemma 2.3], where $R_{1}$ is a vector field that may be expressed in terms of $\left\{\tilde{f}, \partial \tilde{f}, a, a^{\prime}\right\}$. Assume this claim for the moment; it will be demonstrated at the very end. So the perturbed linearized return map along $e_{\theta_{0}}$ with respect to $\tau$ is
$$P_{\theta_{0}}=P_{T\left(\theta_{0}\right)}+\mathcal{O}(\delta)\left(\begin{array}{ll}
P_{11} & P_{12} \\
P_{21} & P_{22}
\end{array}\right)$$
where each entry $P_{i j}$ may be expressed in terms of $\left\{\tilde{f}, \partial \tilde{f}, \partial^{2} \tilde{f}, a, a^{\prime}, a^{\prime \prime}\right\}$ along $e_{\theta_{0}}$. We use this bound on the entries of the matrix $P_{\theta_{0}}-P_{T\left(\theta_{0}\right)}$ to analyze the rotation number now.

Since $P_{\theta_{0}}$ is a symplectic matrix which is conjugate in $S L_{2}(\mathbb{R})$ to a rotation matrix, we write
$$P_{\theta_{0}}=\left(\begin{array}{ll}
u_{11} & u_{12} \\
u_{21} & u_{22}
\end{array}\right)\left(\begin{array}{cc}
\cos \phi & -\sin \phi \\
\sin \phi & \cos \phi
\end{array}\right)\left(\begin{array}{ll}
u_{11} & u_{12} \\
u_{21} & u_{22}
\end{array}\right)^{-1}$$
where $u_{11} u_{22}-u_{12} u_{21}=1$ and the rotation number is denoted by $\phi$. Thus,
$$|2 \cos \phi-2|=\left|\operatorname{tr}\left(P_{\theta_{0}}-P_{T\left(\theta_{0}\right)}\right)\right|=\mathcal{O}(\delta)$$
and so $\phi$ can be made arbitrarily small by choosing $\delta$ sufficiently small. Moreover, the bottom-left entry of $P_{\theta_{0}}$ in (3.9) and (3.10) is
$$\left(u_{21}^{2}+u_{22}^{2}\right) \sin \phi=r\left(\theta_{0}\right) \mathcal{A}\left(\theta_{0}\right)+\mathcal{O}(\delta)$$
and so the sign of $\phi$ is the same as the sign of $r\left(\theta_{0}\right)$ for $\delta$ sufficiently small. This precisely means the rotation number of $e_{\theta_{0}}$ has the opposite sign of $a^{\prime} \times a^{\prime \prime}\left(\theta_{0}\right)$, using the description (3.8), so it follows from the technical condition (3.7) that each $e_{\theta_{0}}$ is $L$-positive.

The remaining loose thread is the claimed description of the perturbed Reeb field. In the basis $\left\langle R, \partial_{\theta}, a^{\perp}\right\rangle$ of the tangent bundle of $S^{1} \times\left(S^{2}-\{\right.$ poles $\left.\}\right)$ consider the ansatz
$$R_{\text {perturb }}=R+\left(x_{0} \cdot R+x_{1} \cdot \partial_{\theta}+x_{2} \cdot a^{\perp}\right)$$
The normalization condition $(1+\delta \tilde{f}) \lambda\left(R_{\text {perturb }}\right)=1$ forces
$$x_{0}=-\frac{\delta}{1+\delta \tilde{f}} \tilde{f}$$
because $\lambda(R)=1$ and $\lambda\left(\partial_{\theta}\right)=0$ and $\lambda\left(a^{\perp}\right)=0$. The other defining equation
$$0=d((1+\delta \tilde{f}) \lambda)\left(R_{\text {perturb }}, \cdot\right)=(1+\delta \tilde{f}) d \lambda\left(R_{\text {perturb }}, \cdot\right)+\delta(d \tilde{f} \wedge \lambda)\left(R_{\text {perturb }}, \cdot\right)$$
splits into $d t, d \varphi, d \theta$ component equations. Noting that $d \lambda(R, \cdot)=0$, the $d \theta$ component equation forces
$$x_{2}=\frac{\delta}{(1+\delta \tilde{f})^{2}\left(a \times a^{\prime}\right)} \frac{\partial \tilde{f}}{\partial \theta}$$
and subsequently the $d t$ (or $d \varphi$ ) component equation forces
$$x_{1}=\frac{\delta}{(1+\delta \tilde{f})^{2}\left(a \times a^{\prime}\right)}\left(a_{1} \frac{\partial \tilde{f}}{\partial \varphi}-a_{2} \frac{\partial \tilde{f}}{\partial t}\right)$$
Thus, $R_{\text {perturb }}$ is as claimed. \(\square\)

Now we show how to modify the exceptional orbits while preserving the technical condition (3.7).
Lemma 3.7. Given $c \geq 0$ and $\varepsilon \in\left(0, \sqrt{\frac{3}{2}}\right]$, there exists a smooth nonpositive function $f_{\varepsilon, c}$ on $S^{1} \times S^{2}$ which only depends on the $\theta$ coordinate, such that $e^{f_{\varepsilon, c}} \lambda_{0}$ satisfies the technical condition (3.7) and whose exceptional orbits $e_{0}$ and $e_{\pi}$ have rotation classes both equal to $\varepsilon \bmod 1$.

Proof. By Lemma 3.3, the rotation classes under consideration are
$$\left(\operatorname{sign} \lim _{\theta \rightarrow \theta_{0}}\left(3 \cos \theta-\frac{1}{\cos \theta}\right)\right) \frac{\frac{\partial f_{\varepsilon, c}}{\partial \theta} \frac{3 \cos ^{2} \theta-1}{\sin \theta}-6 \cos \theta}{\sqrt{6}\left(1-3 \cos ^{2} \theta\right)-\frac{\partial f_{\varepsilon, c}}{\partial \theta} \sqrt{6} \cos \theta \sin \theta} \quad \bmod 1$$
for $\theta_{0} \in\{0, \pi\}$. After setting
$$\frac{\partial f_{\varepsilon, c}}{\partial \theta}:=\tilde{f}_{\varepsilon}(\theta) \sin \theta$$
for a smooth function $\tilde{f}_{\varepsilon}:[0, \pi] \rightarrow \mathbb{R}$, it follows that the rotation classes of $e_{0}$ and $e_{\pi}$ are respectively given by
$$\begin{aligned}
-\left.\frac{1}{\sqrt{6}}\left(\tilde{f}_{\varepsilon}(\theta)-3 \cos \theta\right)\right|_{\theta=0} & \bmod 1 \\
\left.\frac{1}{\sqrt{6}}\left(\tilde{f}_{\varepsilon}(\theta)-3 \cos \theta\right)\right|_{\theta=\pi} & \bmod 1
\end{aligned}$$
These are both equal to $\varepsilon$ upon setting $\tilde{f}_{\varepsilon}(\theta)=(3-\sqrt{6} \varepsilon) \cos \theta$. We then pick the antiderivative of $\tilde{f}_{\varepsilon}$ using $c$ so that the desired function on $S^{1} \times S^{2}$ is
$$f_{\varepsilon, c}(t, \theta, \varphi)=-\frac{3-\sqrt{6} \varepsilon}{2} \cos ^{2} \theta-c$$
A brute force calculation shows that $e^{f_{\varepsilon, c}} \lambda_{0}$ satisfies the technical condition (3.7). \(\square\)

Remark 3.8. As a sanity check, if $\varepsilon=\sqrt{\frac{3}{2}}$ and $c=0$ then we recover $\lambda_{0}$.
We now move forward and show how exactly $\lambda_{0}$ is to be modified to prove Lemma 1.6 in the introduction. Such modifications give us control over the orbits of low symplectic action, at the expense of producing new orbits of high symplectic action with unknown properties. This is sufficient for the purposes of this paper, because for a given class $A \in \operatorname{Rel}_{\omega}(X)$ only the orbit sets of symplectic action less than $\rho(A)$ are relevant to the tentative Gromov invariant.

Lemma 3.9. Suppose $(X, \omega)$ is a near-symplectic 4-manifold such that all components of $Z$ are untwisted zero-circles, and fix $A \in \operatorname{Rel}_{\omega}(X)$. Then there is a choice of neighborhood $\mathcal{N}$ of $Z$ in $X$ such that $(X-\mathcal{N}, \omega)$ is a symplectic manifold with contact-type boundary whose boundary components are copies of $\left(S^{1} \times S^{2}, \lambda_{A}\right)$. Here, $\lambda_{A}$ is a nondegenerate contact form with contact structure $\xi_{0}$ but whose orbits of symplectic action less than $\rho(A)$ are all $\rho(A)$-flat and are either positive hyperbolic or $\rho(A)$-positive elliptic.

Proof. By Lemma 3.7, for any $L$ sufficiently greater than $\rho(A)$ there is a smooth function $f_{\varepsilon, c}$ on $S^{1} \times S^{2}$ for any $c \geq 0$ and sufficiently small choice of $\varepsilon$ such that the exceptional orbits of $e^{f_{\varepsilon, c}} \lambda_{0}$ are $L$-positive. By Lemma 3.6, we can perturb this new Morse-Bott contact form (à la Bourgeois) so that all orbits of action less than $L$ are nondegenerate and $L$-positive when elliptic. As explained in Section 2.5, we can perturb the resulting contact form (à la Taubes) so that all orbits of action less than $L$ are furthermore $L$-flat. This new contact form is still degenerate, but it can be perturbed to become nondegenerate without disturbing the existing orbits of action less than $L$ and without introducing other orbits of action less than $L$. Explicitly, let $U \subset S^{1} \times S^{2}$ be the union of $L$-flat neighborhoods of the orbits of action less than $L$, which do not contain any other orbits, and use [2. Lemma 2.2] to make a generic perturbation of the contact form on the complement of $U$.

The final result is a contact form $\lambda_{A}$ which has the same contact structure as $\lambda_{0}$, so for $c$ sufficiently large there exists a smooth negative function $F_{A} \in C^{\infty}\left(S^{1} \times S^{2}\right)$ such that the maximum value of $F_{A}$ over $S^{1} \times S^{2}$ is less than -1 and
$$\lambda_{A}=e^{F_{A}} \lambda_{0}$$

It remains to show that the neighborhood $\mathcal{N}$ can be chosen so that the contact form on any boundary component of $X-\mathcal{N}$ is $\lambda_{A}$, preserving compatibility with $\omega$. Assume without loss of
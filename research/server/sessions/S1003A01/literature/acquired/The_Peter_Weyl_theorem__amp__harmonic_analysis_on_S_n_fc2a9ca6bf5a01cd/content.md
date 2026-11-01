---
retention_scope: session
part: 1
total_parts: 1
---

---
source_file: The_Peter_Weyl_theorem__amp__harmonic_analysis_on_S_n_f6e1f2d07a79.pdf
converter: mathpix
format: mmd
---

\title{
The Peter-Weyl theorem \& harmonic analysis on $S^{n}$
}

\author{
By Luca Nashabeh
}

\begin{abstract}
For finite groups, the Artin-Wedderburn theorem gives a precise decomposition of the algebra of all $\mathbb{C}$-valued functions into matrix algebras. Specialized to the case of cyclic groups, this produces the classical discrete Fourier transform. In this paper, we endeavor to extend these techniques to compact topological groups, proving similar harmonic decompositions on $S^{1}, S^{2}$, and $S^{3}$.
\end{abstract}

\section*{1. Introduction}

The representation theory of finite groups provides us with many powerful tools that not only allow us to directly study the properties and structures of groups, but also give insight into algebras defined on those groups. One of the most powerful results is the following theorem, which gives a relationship between the algebra of $\mathbb{C}$-valued functions on a finite group $G$ and its irreducible representations.

Theorem 1.1 (Artin-Wedderburn theorem). Let $G$ be a finite group and $\mathbb{C}[G]$ its group algebra with the convolution product
$$\left(f_{1} * f_{2}\right)(g)=\sum_{h \in G} f_{1}(h) f_{2}\left(h^{-1} g\right) .$$
Furthermore, let $\rho_{i}: G \rightarrow \operatorname{GL}\left(V_{i}\right)$ for $1 \leq i \leq k$ be the irreducible representations of $G$, and $\tilde{\rho}_{i}: \mathbb{C}[G] \rightarrow \operatorname{End}\left(V_{i}\right)$ the linear extensions to the group algebra. Then, the map
$$\tilde{\rho}=\bigoplus_{i=1}^{k} \rho_{i}, \quad \tilde{\rho}: \mathbb{C}[G] \rightarrow \bigoplus_{i=1}^{k} \operatorname{End}\left(V_{i}\right)$$
is an isomorphism.

\footnotetext{
© 2024 Nashabeh, Luca. This is an open access article distributed under the terms of the Creative Commons BY-NC-ND 4.0 license.
}

A simple example of the power of the Artin-Wedderburn theorem comes from specializing to the cyclic case $G=\mathbb{Z} / n \mathbb{Z}$. Here, we can describe $\rho_{m}$ and $\tilde{\rho}_{m}$ explicitly as
$$\rho_{m}(x)=\zeta_{n}^{m x}=\exp \left(\frac{2 \pi i}{n} m x\right) \quad \text { and } \quad \tilde{\rho}_{m}(f)=\sum_{x \in G} f(x) \exp \left(\frac{2 \pi i}{n} m x\right) .$$
The Artin-Wedderburn theorem then gives us the following classical result.
Corollary 1.2 (Discrete Fourier transform). Let $f \in \mathbb{C}[G] \cong \mathbb{C}^{n}$. Then $f$ can be uniquely decomposed into pure frequencies with amplitudes
$$F_{m}=\sum_{x=1}^{n} f(x) \exp \left(\frac{2 \pi i}{n} m x\right) .$$

More generally, the Artin-Wedderburn theorem allows us to do a Fourier decomposition on any finite group, including non-abelian ones. However, while the Artin-Wedderburn theorem is certainly a powerful result, the requirement of finiteness prevents us from getting a Fourier decomposition for many interesting continuous groups.

The Peter-Weyl theorem is one path to generalizing the Artin-Wedderburn theorem, proving a very similar result not just for finite groups, but indeed for all compact groups. In doing so, we obtain not only the classical Fourier series, which is simply a decomposition on the compact circle group, but also analogous decompositions on all $n$-spheres. However, before we move to proving these exciting results, we will begin with a necessary discussion of the representation theory of compact groups.

\section*{2. Preliminaries on compact groups}

To begin, we should answer the question of what a compact group actually is. As one might guess, in order to make sense of compactness on a group, we need to introduce a topology on the group. Moreover, for this topology to be at all useful, it would be smart to have the topology interact well with the group structure. These ideas motivate the following definition.

Definition 2.1. A topological group $G$ is a group equipped with a topology $\tau$ such that
\begin{itemize}
\item[(1)] The group product is continuous as a function $G \times G \rightarrow G$, with the product topology on $G \times G$;
\item[(2)] The inverse function ${ }^{-1}: G \rightarrow G$ is continuous as a function on $G$.
\end{itemize}
If, in addition, $G$ is compact and Hausdorff, then it is a compact group.
Remark 2.2. The Hausdorff condition is not universal, but we will include it here for simplicity.

Example 2.3. Any finite group equipped with the discrete topology is a compact group. \(\square\)

Example 2.4. More interestingly, consider the group
$$\mathrm{U}(1)=\left\{e^{i \theta} \mid \theta \in[0,2 \pi)\right\} \subseteq \mathbb{C},$$
with the usual topology inherited from $\mathbb{C}$. Since complex multiplication and conjugation are continuous, this is a Hausdorff topological group. Furthermore, since the unit circle is a compact subset of $\mathbb{C}$, this is a compact group. \(\square\)

Example 2.5. Consider the group
$$\mathrm{SU}(2)=\left\{\left.\left[\begin{array}{cc}
\alpha & \beta \\
-\bar{\beta} & \bar{\alpha}
\end{array}\right]| | \alpha\right|^{2}+|\beta|^{2}=1\right\} \subseteq \mathbb{C}^{4} .$$
Again, since matrix multiplication and inversion are rational functions on $\mathbb{C}^{n}$, this is a Hausdorff topological group. Moreover, writing $\alpha=x+i y$ and $\beta=$ $z+i w$, we see that the restriction is
$$x^{2}+y^{2}+z^{2}+w^{2}=1 .$$
In particular, as a topological space, this group is homeomorphic to the 3-sphere $S^{3}$, which is certainly compact. \(\square\)

The most important result about compact topological groups, for our purposes, is the existence of a so-called Haar measure $\mu$. We give a brief statement of the result.

Theorem 2.6 (Haar measure on compact groups). Let $G$ be a compact group. Then, there exists a measure $\mu$ on (Borel) subsets $S \subseteq G$ such that
\begin{itemize}
\item[(1)] $\mu$ is left translation invariant, i.e., for any $g \in G, \mu(g S)=\mu(S)$;
\item[(2)] $\mu$ is right translation invariant, i.e., for any $g \in G, \mu(S g)=\mu(S)$;
\item[(3)] $\mu(G)=1$.
\end{itemize}

Remark 2.7. The original theorem actually applies to locally compact groups and gives some additional regularity properties of this measure.

We will not prove this theorem, as it is not really an exercise in representation theory. However, the interested reader can consult [vdB93, Sec. 1].

As with any measure, the Haar measure allows us to perform integration on a compact group. Moreover, this integration is compatible with the group structure, in the sense that
$$\int_{S} f(x) \mathrm{d} \mu(x)=\int_{g^{-1} S} f(g x) \mathrm{d} \mu(x)=\int_{S g^{-1}} f(x g) \mathrm{d} \mu(x) .$$
As such, choosing $S=G$, we can use the Haar integral to perform an averaging trick similar to the one used with sums in the case of finite groups.

\section*{3. Representation theory of compact groups}
3.1. Continuous representations. Having set up the preliminary background on compact groups, we can now move to the actual subject of their representations. As with finite groups, it is most convenient to work with complex vector spaces, so, unless otherwise mentioned, we will take any vector space to be over $\mathbb{C}$. Unlike in the finite case, however, we do impose a slight extra condition of continuity on representations of infinite groups.

Definition 3.1. Let $G$ be a topological group. A continuous representation of $G$ is a homomorphism $\rho: G \rightarrow \operatorname{GL}(V)$ for some topological Hausdorff vector space $V$, such that the map $(g, v) \mapsto \rho(g) v$ is continuous as a map $G \times V \rightarrow V$. If $V$ is also finite, then we have a finite continuous representation.

A subrepresentation of $V$ is a subspace $W$ fixed by the action of $G$, so that $\left.\rho\right|_{W}$ is also a representation. An irreducible representation $V$ is a representation with no nontrivial subrepresentations (i.e., no subrepresentations except 0 and $V$ itself).

Remark 3.2. The reason to consider $\rho$ as a map $G \times V \rightarrow V$ instead when discussing continuity is so that we do not need to define a topology on $\operatorname{GL}(V)$.

Furthermore, though we will not prove this, the continuity of $\rho$ in this sense is equivalent to the a priori weaker condition that, for any fixed $v \in V$, the map $g \mapsto \rho(g) v$ is continuous as a function $G \rightarrow V$ (see [Mor19, Sec. V.2]).

For the rest of this paper, we will only consider finite continuous representations over $\mathbb{C}$ unless otherwise mentioned. The advantage of doing so is that much of the theory in the finite case carries over completely analogously. For example, we have the following lemma.

Lemma 3.3 (Schur's lemma, part 1). Let $G$ be a compact group, and $V_{1}, V_{2}$ two complex irreducible representations. Then the space of all homomorphisms from $V_{1}$ to $V_{2}$ commuting with the actions of $G$ is
$$\operatorname{Hom}_{G}\left(V_{1}, V_{2}\right)= \begin{cases}0 & V_{1} \not \models V_{2} \\ \mathbb{C} & V_{1} \cong V_{2} .\end{cases}$$

Proof. Let $\rho: V_{1} \rightarrow V_{2}$ be a homomorphism commuting with $G$. Then, as can easily be checked, $\operatorname{ker} \rho$ and $\rho\left(V_{1}\right)$ are subrepresentations of $V_{1}$ and $V_{2}$, respectively. Since $V_{1}$ and $V_{2}$ are irreducible, either $\rho=0$ or $V_{1} \cong V_{2}$. In the latter case, we can then consider an eigenvalue $\lambda$ of $\rho$; since $\rho-\lambda$ has nontrivial kernel, it must be the 0 map, showing that $\rho=\lambda$. \(\square\)

Corollary 3.4. The irreducible representations of compact abelian groups are all one-dimensional.

Proof. Let $V$ be an irreducible representation of an abelian group, and let $\rho(g)$ be the representation of some element $g$. Since the group is abelian, $\rho(g)$ commutes with the action of any other group element so-taking $V_{1}=V_{2}=V$ in Schur's lemma-we conclude that $\rho(g)$ is a scalar. Since this is true for any $g$, for $V$ to be irreducible, it must be one-dimensional. \(\square\)

Example 3.5. We can already determine all the irreducible representations of U(1). By Schur's lemma, we know these are all one-dimensional. Parametrizing U(1) as $\exp (i \theta)$, any irreducible representation must therefore be a continuous function satisfying
$$\rho(x+y)=\rho(x) \rho(y) \quad \text { and } \quad \rho(0)=\rho(2 \pi)=1 .$$
Since $\rho(g) \neq 0$, setting $f(x)=\log (\rho(x))$ gives
$$f(x+y)=f(x)+f(y) \quad \text { and } \quad f(0)=f(2 \pi)+2 \pi i n, n \in \mathbb{Z} .$$
Choosing $f(0)=0$ for convenience, we see that the only continuous functions satisfying these conditions are
$$f_{n}(\theta)=i n \theta .$$
Thus, all irreducible representations of U(1) have the form
$$\rho_{n}(x)=e^{i n \theta} .$$ \(\square\)
3.2. Unitary representations. In the case of finite groups, defining a $G$ -invariant inner product on our representations was ultimately a rather useful tool. Motivated by the technique of averaging there, we can do something similar for compact groups.

Proposition 3.6. Let $G$ be a compact group and $(\rho, V)$ a finite representation. Then there exists an inner product on $V$ such that $\rho(g)$ is unitary for all $g \in G$ (i.e., the inner product is $G$-invariant).

Proof. Using the Haar measure, we can imitate the proof from the case of finite groups. Specifically, let $\langle\cdot, \cdot\rangle$ be any inner product on $V$, and define the new inner product $\langle\cdot, \cdot\rangle_{G}$ by
$$\langle v, w\rangle_{G}=\int_{G}\langle g v, g w\rangle \mathrm{d} g .$$
Note that this is indeed an inner product, as $\langle v, v\rangle_{G}$ is the integral of a continuous, nonnegative quantity which is only identically zero if $v=0$. Furthermore, this inner product is $G$-invariant, as
$$\langle h v, h w\rangle_{G}=\int_{G}\langle g h v, g h w\rangle \mathrm{d} g=\int_{G h}\langle g v, g w\rangle \mathrm{d} g=\langle v, w\rangle_{G} .$$ \(\square\)

Corollary 3.7. Let $G$ be a compact group and $V$ a finite representation. Then $V$ is semisimple (i.e., decomposes as a sum of irreducibles).

Proof. If $V$ is irreducible, we are done. Thus, let $W \subseteq V$ be an irreducible subspace fixed by $G$, and consider $W^{\perp}$ as given by the invariant inner product. We wish to show that $W^{\perp}$ is fixed by $G$. But, for any $v \in W^{\perp}$ and $w \in W$, we know that $\langle g v, w\rangle=\left\langle v, g^{-1} w\right\rangle=0$, since $W$ is fixed by $G$. Thus, $g v$ is orthogonal to everything in $W$, so it is in $W^{\perp}$, showing that $W^{\perp}$ is also fixed by $G$. We can thus write $V=W \oplus W^{\perp}$ and induct on $W^{\perp}$ to get a decomposition into irreducible subspaces. \(\square\)

Corollary 3.8 (Schur's lemma, part 2). Let $G$ be a compact group and $V$ a finite representation such that $\operatorname{End}_{G}(V)=\mathbb{C}$. Then $V$ is irreducible.

Proof. Suppose that $V$ were reducible, so that $V=V_{1} \oplus V_{2}$ with $V_{1}$ and $V_{2}$ nontrivial. Let $P: V \rightarrow V_{2}$ be the orthogonal projection map onto $V_{2}$ given the unitary structure of the proposition. Then $P \in \operatorname{End}_{G}(V)$, so either $P=0$ or $V \cong V_{2}$. But $V_{2} \neq 0$, so $P$ cannot be 0 and $V \cong V_{2}$, a contradiction. \(\square\)

From now on, we will also assume any representation is unitary and denote its inner product as simply $\langle\cdot, \cdot\rangle$.
3.3. Matrix coefficients and Schur orthogonality. In our ultimate discussion of the Peter-Weyl theorem, it will be useful to have a more concrete understanding of the endomorphisms of the representations of $G$. To that end, it would be useful to consider matrix representations of these endomorphisms. However, rather than having to choose a basis for our representations, it is convenient to use the slightly more abstract notion of matrix coefficients.

Definition 3.9. Let $G$ be a compact group and $(\rho, V)$ a finite representation. A matrix coefficient is any function $m_{v, w}^{\rho}: G \rightarrow \mathbb{C}$ of the form
$$m_{v, w}^{\rho}(g)=m_{v, w}(g)=\langle\rho(g) v, w\rangle \quad \text { with } \quad v, w \in V .$$
The span of all matrix coefficients will be denoted $C(G)_{\rho}$. If a specific basis $v_{i}$ is implied, these may also just be written as $m_{i j}$.

Note that this naming makes the most sense if we choose $v, w$ to be from an orthonormal basis, in which case the individual matrix coefficients are just those of the matrix representation of $g$. However, more generally, the matrix coefficients so defined will always be the elements of the matrix representation of $g$ with respect to some basis. The converse, namely that the elements of any matrix representation are actually matrix coefficients, also holds by linearity,
so this definition really is not introducing anything new; it is perhaps just a bit easier to work with.

For finite groups, we had a very strong result on the orthogonality of these matrix coefficients. As one might expect by now, this result raises practically unchanged to the compact case.

Theorem 3.10 (Orthogonality of matrix coefficients). Let $G$ be a compact group and $\left(\rho_{1}, V\right)$ and $\left(\rho_{2}, W\right)$ two irreducible finite representations. Let $v_{1}, v_{2} \in$ $V$ and $w_{1}, w_{2} \in W$. Then we have
$$\int_{G} m_{v_{1}, v_{2}}(g) \overline{m_{w_{1}, w_{2}}(g)} \mathrm{d} g= \begin{cases}\frac{1}{\operatorname{dim} V}\left\langle v_{1}, w_{1}\right\rangle \overline{\left\langle v_{2}, w_{2}\right\rangle} & \rho_{1} \cong \rho_{2} \\ 0 & \text { otherwise }\end{cases}$$

Proof. For any $v \in V, w \in W$, consider the operators
$$L_{v, w}(x)=\langle x, v\rangle w \quad \text { and } \quad T_{v, w}=\int_{G} g L_{v, w} g^{-1} \mathrm{~d} g .$$
Both of these are elements of $\operatorname{Hom}(V, W)$. Furthermore, note that $T_{v, w}$ commutes with the action of $G$, as
$$T_{v, w} g=\int_{G} h L_{v, w}\left(h^{-1} g\right) \mathrm{d} h=\int_{G}(g h) L_{v, w} h^{-1} \mathrm{~d} h=g T_{v, w} .$$
As such, Schur's lemma tells us $T_{v, w}$ is a scalar if and only if $\rho_{1} \cong \rho_{2}$ and is 0 otherwise. To determine this scalar, we can take the trace:
$$\operatorname{Tr} T_{v, w}(g)=\int_{G} \operatorname{Tr} h L_{v, w} h^{-1} \mathrm{~d} h=\int_{G} \operatorname{Tr} L_{v, w} \mathrm{~d} h=\operatorname{Tr} L_{v, w} .$$
The trace of $L_{v, w}$ is most easily evaluated by using an orthonormal basis $e_{i}$ of $V$, yielding
$$\operatorname{Tr} L_{v, w}=\sum_{i=1}^{\operatorname{dim} V}\left\langle L_{v, w}\left(e_{i}\right), e_{i}\right\rangle=\sum_{i=1}^{\operatorname{dim} V}\left\langle e_{i}, v\right\rangle\left\langle w, e_{i}\right\rangle=\langle w, v\rangle .$$
Thus, we have $T_{v, w}(g)=\frac{1}{\operatorname{dim} V}\langle w, v\rangle$. Finally, we can answer our original question by noting that
$$\begin{aligned}
\int_{G} m_{v_{1}, v_{2}}(g) \overline{m_{w_{1}, w_{2}}(g)} \mathrm{d} g & =\int_{G}\left\langle g v_{1}, v_{2}\right\rangle \overline{\left\langle g w_{1}, w_{2}\right\rangle} \mathrm{d} g \\
& =\int_{G}\left\langle g v_{1}, v_{2}\right\rangle\left\langle g^{-1} w_{2}, w_{1}\right\rangle \mathrm{d} g \\
& =\int_{G}\left\langle g\left\langle g^{-1} w_{2}, w_{1}\right\rangle v_{1}, v_{2}\right\rangle \mathrm{d} g \\
& =\left\langle\int_{G} g\left\langle g^{-1} w_{2}, w_{1}\right\rangle v_{1} \mathrm{~d} g, v_{2}\right\rangle \\
& =\left\langle L_{w_{1}, v_{1}} w_{2}, v_{2}\right\rangle .
\end{aligned}$$

Using our classification for $L_{w_{1}, v_{1}}$, we can ultimately conclude
$$\int_{G} m_{v_{1}, v_{2}}(g) \overline{m_{w_{1}, w_{2}}(g)} \mathrm{d} g= \begin{cases}\frac{1}{\operatorname{dim} V}\left\langle v_{1}, w_{1}\right\rangle \overline{\left\langle v_{2}, w_{2}\right\rangle} & \rho_{1} \cong \rho_{2} \\ 0 & \text { otherwise. }\end{cases}$$ \(\square\)
3.4. Characters. Having just proved Schur orthogonality, it is worth taking a brief digression to discuss characters.

Definition 3.11. Let $G$ be a compact group and $(\rho, V)$ a representation. The character $\chi$ of $\rho$ is defined by
$$\chi(g)=\operatorname{Tr} \rho(g) .$$
If $\rho$ is an irreducible representation, $\chi$ is called an irreducible character.
Characters function largely the same as for finite groups. Indeed, the character of the sum of two representations is simply the sum of characters, and therefore any character breaks down into a sum of irreducible characters. We reproduce the following two familiar results.

Corollary 3.12 (Character orthogonality). Let $G$ be a compact group and let $V, W$ be two irreducible representations with characters $\chi_{V}, \chi_{W}$. Then
$$\int_{G} \chi_{V}(g) \overline{\chi_{W}(g)} \mathrm{d} g= \begin{cases}1 & V \cong W \\ 0 & V \not \models W\end{cases}$$

Proof. Choose orthonormal bases $v_{i}$ and $w_{j}$ of $V$ and $W$. Then, we have
$$\chi_{V}(g)=\sum_{i=1}^{\operatorname{dim} V}\left\langle g v_{i}, v_{i}\right\rangle=\sum_{i=1}^{\operatorname{dim} V} m_{v_{i}, v_{i}}(g)$$
and similarly for $\chi_{W}$. Thus,
$$\int_{G} \chi_{V}(g) \overline{\chi_{W}(g)} \mathrm{d} g=\sum_{i=1}^{\operatorname{dim} V} \sum_{j=1}^{\operatorname{dim} W} \int_{G} m_{v_{i}, v_{i}}(g) \overline{m_{w_{j}, w_{j}}(g)} \mathrm{d} g .$$
If $V \not \models W$, we already know this is 0 by Theorem 3.10. On the other hand, if $V \cong W$, we can take $v_{i}=w_{i}$, yielding
$$\sum_{i=1}^{\operatorname{dim} V} \sum_{j=1}^{\operatorname{dim} V} \int_{G} m_{v_{i}, v_{i}}(g) \overline{m_{v_{j}, v_{j}}(g)} \mathrm{d} g=\frac{1}{\operatorname{dim} V} \sum_{i=1}^{\operatorname{dim} V} \sum_{j=1}^{\operatorname{dim} V}\left|\left\langle v_{i}, v_{j}\right\rangle\right|^{2}=1 .$$ \(\square\)

Corollary 3.13. Let $G$ be a compact group and $\chi$ a character of a finite representation. Write $\chi$ as a sum of irreducible characters $\chi=\sum_{i=1}^{k} n_{i} \chi_{i}$.

Then
$$\int_{G}|\chi(g)|^{2} \mathrm{~d} g=\sum_{i=1}^{k} n_{i}^{2} .$$
Namely, $\chi$ is irreducible if and only if the integral is 1.
Example 3.14. If we parametrize the circle group in terms of an angle $\theta \in[0,2 \pi)$, one can check that the Haar measure is given by
$$\mathrm{d} g=\frac{\mathrm{d} \theta}{2 \pi} .$$
Furthermore, since the irreducible representations of U(1) are one-dimensional (see the example), we already have the characters
$$\chi_{n}(\theta)=\rho_{n}(\theta)=\exp (i n \theta) .$$
Thus, by a needlessly complicated proof, we have that
$$\int_{\mathrm{U}(1)} \chi_{n}(g) \overline{\chi_{m}(g)} \mathrm{d} g=\frac{1}{2 \pi} \int_{0}^{2 \pi} e^{i n \theta} e^{-i m \theta} \mathrm{~d} \theta=\delta_{n m} .$$

More interestingly, we also have a finite, integral version of Parseval's identity. Indeed, if $f$ is an arbitrary finite character
$$f=\sum_{i=-N}^{N} n_{i} \chi_{i},$$
then Corollary 3.13 tells us that
$$\frac{1}{2 \pi} \int_{0}^{2 \pi}|f(\theta)|^{2} \mathrm{~d} \theta=\sum_{i=-N}^{N} n_{i}^{2} .$$ \(\square\)

\section*{4. $L^{2}(G)$ \& the Peter-Weyl theorem}

Having digressed enough on the subject of representations, it would be good to remind ourselves of the original goal of describing functions on $G$. In the case of finite groups, this could be achieved by considering the group algebra
$$\mathbb{C}[G]=\bigoplus_{g \in G} \mathbb{C} g,$$
which has a multiplication linearly extending that of $G$. This could be identified as the algebra of all functions $f: G \rightarrow \mathbb{C}$ with the convolution product by letting $f(g)$ be the coefficient of $g$ in $f$.

Unfortunately, directly attempting to use the group algebra in the case of compact groups is a bit too general. Indeed, the space $\mathbb{C}[G] \sim \mathbb{C}^{G}$ contains
plenty of unwieldy and uninteresting functions. More importantly, it also contains plenty of nonintegrable functions, which prevents us from using the tools we have developed. The easiest way to fix this issue is just to get rid of these problematic functions.
4.1. The representation $L^{2}(G)$.

Definition 4.1. Let $G$ be a compact group. Let $L^{2}(G)$ be the Banach space of complex square-integrable functions, i.e., those functions $f: G \rightarrow \mathbb{C}$ such that
$$\int_{G}|f|^{2} \mathrm{~d} g \text { exists and is }<\infty .$$
Then, $G$ acts on $L^{2}(G)$ as
$$(g f)(x)=f\left(g^{-1} x\right) .$$

Remark 4.2. Technically speaking, the space $L^{2}(G)$ is actually a quotient of the above definition by the equivalence of almost-everywhere equality, but we will ignore this complication as it is not essential. For more on $L^{p}$ spaces, see [Axl19, Chap. 7-8].

Example 4.3. The matrix coefficients $C(G)_{\rho}$ are all continuous functions, and hence their squares are integrable over the compact set $G$. Thus, we have
$$C(G)_{\rho} \subseteq L^{2}(G) \text { for all } \rho \text {. }$$ \(\square\)

Example 4.4. For a finite group, we know that $L^{2}(G) \cong \mathbb{C}[G]$, since the integral is just summing over each group element. Thus, an element $f$ looks like
$$f=\sum_{h \in G} f(h) h .$$
Therefore,
$$g f=\sum_{h \in G}(g f)(h) h=\sum_{h \in G} f\left(g^{-1} h\right) h=\sum_{h \in G} f(h) g h .$$
In other words, $L^{2}(G)$ is just the regular representation of $G$, which should not be too surprising given the analogy with the group algebra. \(\square\)

Example 4.5. For the group $\mathrm{U}(1), L^{2}(\mathrm{U}(1))$ can be identified as all square-integrable functions on the circle, since $\mathrm{U}(1) \cong S^{1}$, together with the translation action $f(x) \mapsto f(x-\theta)$. \(\square\)

The reason to choose square integrability, rather than just normal integrability, is that it will allow us to promote $L^{2}(G)$ from just a Banach space to a

Hilbert space, i.e., a space with an inner product. Indeed, we can define
$$\langle f, g\rangle=\int_{G} f \bar{g} \mathrm{~d} x,$$
which is guaranteed to exist by the complex polarization identities. However, before continuing with its representation theory, it is worth digressing to discuss the product structure of $L^{2}(G)$.
4.2. Convolutions. Without being too rigorous, we can think about an element $f \in L^{2}(G)$ as a "weighted integral" of elements of $G$
$$f=\int_{G} f(g) g \mathrm{~d} g .$$
From this, we can calculate the product of two elements as
$$f_{1} * f_{2}=\int_{G} \int_{G} f_{1}(h) f_{2}(g) h g \mathrm{~d} h \mathrm{~d} g=\int_{G}\left(\int_{G} f_{1}(h) f_{2}\left(h^{-1} g\right) \mathrm{d} h\right) g \mathrm{~d} g .$$
Looking at the coefficient of $g$ in this expression thus motivates the following definition for the convolution.

Definition 4.6. Let $G$ be a compact group. Then, for any $f_{1}, f_{2} \in L^{2}(G)$, we define the convolution
$$\left(f_{1} * f_{2}\right)(g)=\int_{G} f_{1}(h) f_{2}\left(h^{-1} g\right) \mathrm{d} h .$$

Remark 4.7. One should prove that this convolution does actually obey the regular associativity and distributivity laws of a product. This is a good exercise in analysis.

Also, note that if $G$ is not discrete, * does not technically have an identity element. However, as we will discuss, one can still approximate an identity element using $L^{2}(G)$ functions.

Note that the convolution is not, in general, abelian (which should not be a surprise, considering $G$ need not be). As such, there are two natural operations we can extract from the convolution by fixing one of the two factors. Specifically, we will write
$$L_{h}(f)=h * f \quad \text { and } \quad R_{h}(f)=f * h \quad \text { for } \quad h, f \in L^{2}(G) .$$
These operations are, in general, very well behaved. Specifically, we have the following collection of technical results from functional analysis, which are only partially reproduced as they are not the focus of this article.

Proposition 4.8. Let $h \in L^{2}(G)$, and define $\tilde{h}(x)=\overline{h\left(x^{-1}\right)}$. Then we have that
\begin{itemize}
\item[(1)] $L_{h}$ and $R_{h}$ are continuous compact operators;
\end{itemize}
\begin{itemize}
\item[(2)] $\left(L_{h}\right)^{*}=L_{\tilde{h}}$ and $\left(R_{h}\right)^{*}=R_{\tilde{h}}$. In particular, if $h=\tilde{h}$, then $L_{h}$ and $R_{h}$ are self-adjoint.
\end{itemize}

Proof.
\begin{itemize}
\item[(1)] The continuity of both $L_{h}$ and $R_{h}$ follows easily enough by applying the Cauchy-Schwarz inequality to show that
$$\left\|L_{h}(f)(g)\right\|=\left\|\int_{G} h(x) f\left(x^{-1} g\right) \mathrm{d} x\right\| \leq\|h\|\|f\|,$$
and similarly for $R_{h}$. Compactness, on the other hand, is more technical, but can be done by noting that the convolution is an integral operator with a compactly supported kernel; the interested reader can find the full details in [Mor19, Chap V.4] or [vdB93, Sec. 8].
\item[(2)] We prove this for $L_{h}$, as the proof for $R_{h}$ is nearly identical.
$$\begin{aligned}
\left\langle L_{h} f_{1}, f_{2}\right\rangle & =\int_{G} h * f_{1} \overline{f_{2}} \mathrm{~d} x \\
& =\int_{G} \int_{G} h(y) f_{1}\left(y^{-1} x\right) \overline{f_{2}(x)} \mathrm{d} y \mathrm{~d} x \\
& =\int_{G \times G} h\left(y^{-1}\right) f_{1}(x) \overline{f_{2}\left(y^{-1} x\right)} \mathrm{d} y \mathrm{~d} x \quad\left(x \rightarrow y x \quad \text { and } \quad y \rightarrow y^{-1}\right) \\
& =\int_{G} f_{1}(x)\left[\int_{G} \overline{h\left(y^{-1}\right)} f_{2}\left(y^{-1} x\right) \mathrm{d} y\right]^{*} \mathrm{~d} x \\
& =\left\langle f_{1}, L_{\tilde{h}} f_{2}\right\rangle
\end{aligned}$$
Thus, if $h=\tilde{h}$, then $L_{h}=L_{\tilde{h}}$ is equal to its adjoint. \(\square\)
\end{itemize}

Despite being very nicely behaved, however, the convolution does have one major weakness: its lack of an identity element. This is rather annoying, as it means that $L^{2}(G)$ with $*$ as the product is a non-unital ring. However, as alluded to, we can still approximate an identity element as well as we need to.

Lemma 4.9. Given any $f \in L^{2}(G)$, there is a sequence of functions $h_{n}$ such that
\begin{itemize}
\item[(1)] $h_{n}=\tilde{h}_{n}$;
\item[(2)] $\left\|h_{n}\right\|=1$;
\item[(3)] $f * h_{n} \rightarrow f$ as $n \rightarrow \infty$.
\end{itemize}

Proof. Denote by $r_{x}$ right multiplication by $x$, i.e., $r_{x} f(y)=f(y x)$.
Now, let $\epsilon>0$, and choose a neighborhood of the identity $U \subseteq G$ such that $U=U^{-1}$ and $\left\|r_{x} f-f\right\|<\epsilon$ for all $x \in U$, which is possible by continuity of the group multiplication. Define $h_{\epsilon}=\frac{1}{\operatorname{Vol}(U)} 1_{U}$. Then $h_{\epsilon}=\tilde{h}_{\epsilon}$ and $\left\|h_{\epsilon}\right\|=1$
by definition. Furthermore, we have
$$\begin{aligned}
f * h_{\epsilon}(g)-f(g) & =\frac{1}{\operatorname{Vol}(U)} \int_{G} f(x) 1_{U}\left(x^{-1} g\right) \mathrm{d} x-f(g) \\
& =\frac{1}{\operatorname{Vol}(U)} \int_{G} f(g x) 1_{U}\left(x^{-1}\right) \mathrm{d} x-\frac{1}{\operatorname{Vol}(U)} \int_{U} f(g) \mathrm{d} x \\
& =\frac{1}{\operatorname{Vol}(U)} \int_{U}\left(r_{x} f\right)(g)-f(g) \mathrm{d} x
\end{aligned}$$
Thus, we can conclude that
$$\begin{aligned}
\left\|f * h_{\epsilon}-f\right\|^{2} & =\frac{1}{\operatorname{Vol}(U)^{2}} \int_{U \times U}\left(\left(r_{x}\right) f-f\right) \overline{\left(\left(r_{y}\right) f-f\right)} \mathrm{d} x \mathrm{~d} y \\
& \leq \frac{1}{\operatorname{Vol}(U)^{2}} \int_{U \times U}\left\|\left(r_{x}\right) f-f\right\| \overline{\left\|\left(r_{x}\right) f-f\right\|} \mathrm{d} x \mathrm{~d} y \\
& =\frac{1}{\operatorname{Vol}(U)^{2}} \int_{U \times U} \epsilon^{2} \mathrm{~d} x \mathrm{~d} y \\
& =\epsilon^{2} .
\end{aligned}$$
In particular, if we take the sequence $h_{n}:=h_{2^{-n}}$, we get an approximation to the identity. \(\square\)
4.3. The Peter-Weyl theorem. We can finally come to our first major result, the titular Peter-Weyl theorem. This, as mentioned earlier, is really just a generalization of the Artin-Wedderburn theorem to compact groups, giving us a decomposition of $L^{2}(G)$, the equivalent to $\mathbb{C}[G]$, into simpler spaces given by the irreducible representations of $G$.

We will still need one more theorem before proving Peter-Weyl: the spectral theorem for compact self-adjoint operators. However, we will just be stating this result, as it is purely a result from functional analysis.

Theorem 4.10 (Spectral theorem). Let $T: V \rightarrow W$ be a compact selfadjoint operator between Hilbert spaces. Then $V$ decomposes as an orthogonal direct sum
$$V=\operatorname{Ker}(T) \bigoplus_{\lambda \in \Lambda} E_{\lambda},$$
where $\Lambda \in \mathbb{R}^{*}$ is a discrete set of eigenvalues, and the $E_{\lambda}$ are orthogonal, finitedimensional eigenspaces.

Proof. See [Mor19, Chap. V.6] or [Axl19, Chap. 10D]. \(\square\)

Having finally gone through all the preliminaries, we present the Peter-Weyl theorem.

Theorem 4.11 (Peter \& Weyl, 1927). Let $G$ be a compact group, and $\widehat{G}$ the set of finite irreducible representations of $G$. Then
$$L^{2}(G) \cong \widehat{\bigoplus}_{\rho \in \widehat{G}} C(G)_{\rho},$$
where $\widehat{\oplus}$ denotes the closure of the direct sum.
Proof. We will denote
$$\mathcal{R}(G)=\widehat{\bigoplus_{\rho \in \widehat{G}}} C(G)_{\rho}$$
for convenience. The proof will consist of two steps: showing that every finite subrepresentation of $L^{2}(G)$ occurs in $\mathcal{R}(G)$, and showing that this implies that the complement of $\mathcal{R}(G)$ is trivial.

For the first step, consider some arbitrary finite representation $V$ of $G$. Without loss of generality, we may take $V$ to be irreducible, since any finite representation is semisimple by Corollary 3.7. Our strategy will be to show that the image of any inclusion map $u: V \rightarrow L^{2}(G)$ commuting with the action of $G$ is in fact contained in $\mathcal{R}(G)$, i.e., is in the span of all matrix coefficients. To do so, take some $v \in V$ and let $f \in L^{2}(G)$. We then have
$$\begin{aligned}
(u(v) * \tilde{f})(g) & =\int_{G} u(v)(h) \overline{f\left(g^{-1} h\right)} \mathrm{d} h \\
& =\int_{G} u(v)(g h) \overline{f(h)} \mathrm{d} h \\
& =\langle u(v) \circ g, f\rangle \\
& =\left\langle u\left(\rho\left(g^{-1}\right) v\right), f\right\rangle \\
& =\left\langle\rho\left(g^{-1}\right) v, u^{*}(f)\right\rangle .
\end{aligned}$$
This is a matrix coefficient for the dual representation of $\rho$, so it is in $\mathcal{R}(G)$. Now, if we take a sequence of $\tilde{f}_{n}$ approximating the identity, we can then conclude that
$$u(v) * \tilde{f}_{n} \rightarrow u(v) \in \mathcal{R}(G) .$$

We are now ready to complete our proof of the theorem. To that end, consider an element $f \in \mathcal{R}(G)^{\perp}$. If we now consider any element $h \in L^{2}(G)$ such that $h=\tilde{h}$, we know that $R_{h}$ is a self-adjoint compact operator. As such, $L^{2}(G)$ decomposes as
$$L^{2}(G)=\operatorname{Ker}\left(R_{h}\right) \bigoplus_{i} E_{\lambda_{i}},$$
where the $E_{\lambda_{i}}$ are finite-dimensional. As such, they are all in $\mathcal{R}(G)$, so $f$ is orthogonal to them. In particular, $f \in \operatorname{Ker}\left(R_{h}\right)$, i.e., $f * h=0$. Again, taking
now a sequence $h_{n}$ that approximates the identity, we conclude that $f=0$, completing the proof. \(\square\)

\section*{5. Applications to $S^{1}$ and $S^{3}$}

After all of that work, we are finally ready to discuss some concrete applications of all of this theory to Fourier-type decompositions on $n$-spheres. We will only handle the cases $S^{1}, S^{2}$, and $S^{3}$ in this article, as the general case needs more sophisticated tools. The cases of $S^{1}$ and $S^{3}$ are easiest to handle thanks to the fact that these two spheres actually have group structures; namely, we have $S^{1} \cong U(1)$ and $S^{3} \cong \mathrm{SU}(2)$ as discussed previously. As such, we will discuss them first.
5.1. U(1) and $S^{1}$. The case of $S^{1}$, though not particularly revolutionary in its conclusion, is still a wonderful and simple example of the Wedderburn-type decomposition we are trying to do. Moreover, it provides the framework with which we can approach more general cases.

Theorem 5.1 (Fourier, 1807). The space $L^{2}\left(S^{1}\right)$ decomposes as
$$L^{2}\left(S^{1}\right) \cong \widehat{\bigoplus_{n \in \mathbb{Z}}} C(\mathrm{U}(1))_{n} \cong \widehat{\bigoplus_{n \in \mathbb{Z}}} \mathbb{C} e^{i n \theta} .$$
More concretely, a function $f \in L^{2}\left(S^{1}\right)$ can be written as
$$f(\theta)=\sum_{n \in \mathbb{Z}} \widehat{f}(n) e^{i n \theta} \quad \text { with } \quad \widehat{f}(n)=\frac{1}{2 \pi} \int_{0}^{2 \pi} f(\theta) e^{-i n \theta} \mathrm{~d} \theta .$$

Proof. Note that $\mathrm{U}(1) \cong S^{1}$. Furthermore, by our classification of the irreducible representations, the span of matrix coefficients is clearly just
$$C(\mathrm{U}(1))_{n} \cong \mathbb{C} \exp (i n \theta) .$$
Thus, applying Theorem 4.11 gives us the first statement.
For the more concrete realization, note that we already know $f$ decomposes as a sum:
$$f=\sum_{n \in \mathbb{Z}} a_{n} e^{i n \theta} .$$
We can then use Theorem 3.10 to isolate what $a_{n}$ is. Specifically, taking the inner product with the matrix coefficient $\overline{m_{n}}=e^{-i n \theta}=m_{-n}$, and recalling that $\mathrm{d} g=\mathrm{d} \theta /(2 \pi)$, gives us that
$$\frac{1}{2 \pi} \int_{0}^{2 \pi} f(\theta) e^{-i n \theta} \mathrm{~d} \theta=\frac{1}{2 \pi} \int_{0}^{2 \pi} \sum_{k \in \mathbb{Z}} a_{k} m_{k} \overline{m_{n}} \mathrm{~d} \theta=\sum_{k \in Z} a_{k} \delta_{k n}=a_{n} .$$ \(\square\)
5.2. Representation theory of SU(2). As we noted previously, SU(2) can be viewed as the manifold $S^{3}$. Thus, to get a Fourier theory on $S^{3}$, it would be sufficient to determine the matrix coefficients of representations of SU(2). Before we can do that, however, we need to actually determine the irreducible representations themselves.

In order to find these irreducible representations, note that there is a natural action of $\operatorname{SU}(2)$ on $\mathbb{C}^{2}$ given by
$$g\left[\begin{array}{l}
z_{1} \\
z_{2}
\end{array}\right]=\left[\begin{array}{cc}
\alpha & \beta \\
-\bar{\beta} & \bar{\alpha}
\end{array}\right]\left[\begin{array}{l}
z_{1} \\
z_{2}
\end{array}\right]=\left[\begin{array}{c}
\alpha z_{1}+\beta z_{2} \\
-\bar{\beta} z_{1}+\bar{\alpha} z_{2}
\end{array}\right] .$$
A slight reframing of this involves considering $\mathbf{z}=\left(z_{1}, z_{2}\right)$ as variables for a 2-variable polynomial $p_{1}(\mathbf{z})=a z_{1}+b z_{2}$. With this reframing, we get a representation
$$\left(g p_{1}\right)(\mathbf{z})=p_{1}\left(g^{-1} \mathbf{z}\right),$$
the inverse being necessary to respect associativity. This can be generalized by considering higher-degree polynomials. Namely, if we let $P_{n}$ be the space of all $\leq n$ degree complex polynomials in 2 variables, we get a representation
$$\left(g p_{n}\right)(\mathbf{z})=p_{n}\left(g^{-1} \mathbf{z}\right) \quad \text { for } \quad p_{n} \in P_{n} .$$

This representation, unfortunately, is not irreducible. Indeed, consider the subspace $\mathcal{P}_{n}$ of all homogeneous degree $n$ polynomials, i.e., the polynomials such that
$$p_{n}(\lambda \mathbf{z})=\lambda^{n} p_{n}(\mathbf{z}) .$$
Then this subspace is invariant under the SU(2) action, as
$$\left(g p_{n}\right)(\lambda \mathbf{z})=p_{n}\left(g^{-1} \lambda \mathbf{z}\right)=p_{n}\left(\lambda g^{-1} \mathbf{z}\right)=\lambda^{n}\left(g p_{n}\right)(\mathbf{z}) .$$
The natural question to ask is whether this new representation is irreducible. The answer, as we will prove, is yes.

Proposition 5.2. The $\operatorname{SU}(2)$ representation on $\mathcal{P}_{n}$ is irreducible for every $n \geq 0$. In particular, there is a representation $\rho_{n}$ of dimension $n+1$ for every $n \geq 0$.

Proof. Our proof will attempt to use Corollary 3.8 by showing that any endomorphism $A$ of $\mathcal{P}_{n}$ commuting with the action of SU(2) is a scalar.

To start our proof, note that the polynomials $p_{k}=z_{1}^{k} z_{2}^{n-k}$ form a basis of $\mathcal{P}_{n}$ for $0 \leq k \leq n$. Now, consider the special elements
$$u_{\theta}=\left[\begin{array}{cc}
e^{-i \theta} & 0 \\
0 & e^{i \theta}
\end{array}\right] \in U(1) \subseteq \mathrm{SU}(2) .$$
These elements are of note, as
$$u_{\theta} p_{k}=\left(e^{i \theta} z_{1}\right)^{k}\left(e^{-i \theta} z_{2}\right)^{n-k}=e^{i \theta(2 k-n)} p_{k} .$$

Namely, the $p_{k}$ are eigenvectors of $u_{\theta}$ with respective eigenvalues $e^{i \theta(2 k-n)}$. As such, in the basis of the $p_{k}$, we have
$$\rho_{n}\left(u_{\theta}\right)=\operatorname{diag}\left(e^{-i \theta n}, e^{-i \theta(n-2)}, \ldots, e^{i \theta n}\right) .$$
By choosing $\theta$ small enough, these eigenvalues are all distinct, so the $p_{k}$ also generate all the eigenspaces of $u_{\theta}$. Since $A$ is assumed to commute with SU(2), it must map each of these eigenspaces to itself. Thus,
$$A p_{k}=\lambda_{k} p_{k} \quad \text { for } \quad 0 \leq k \leq n .$$
We now want to show that $\lambda_{k}=\lambda_{0}$ for all $k$. To do so, consider the new elements
$$r_{\theta}=\left[\begin{array}{cc}
\cos \theta & -\sin \theta \\
\sin \theta & \cos \theta
\end{array}\right] \in U(1) \subseteq \mathrm{SU}(2) .$$
We can then look at the action of $r_{\theta}$ and $A$ on $p_{0}=z_{1}^{n}$. Specifically, we have
$$\begin{aligned}
A r_{\theta} p_{0} & =A\left(\cos \theta z_{1}+\sin \theta z_{2}\right)^{n} \\
& =A \sum_{k=0}^{n}\binom{n}{k}(\cos \theta)^{k}(\sin \theta)^{n-k} z_{1}^{k} z_{2}^{n-k} \\
& =\sum_{k=0}^{n}\binom{n}{k}(\cos \theta)^{k}(\sin \theta)^{n-k} A p_{k} \\
& =\sum_{k=0}^{n} \lambda_{k}\binom{n}{k}(\cos \theta)^{k}(\sin \theta)^{n-k} p_{k} .
\end{aligned}$$
On the other hand, since $A r_{\theta}=r_{\theta} A$, we also get
$$r_{\theta} A p_{0}=\lambda_{0} r \theta p_{0}=\sum_{k=0}^{n} \lambda_{0}\binom{n}{k}(\cos \theta)^{k}(\sin \theta)^{n-k} p_{k} .$$
Comparing these two expressions, we can indeed conclude that $\lambda_{0}=\lambda_{k}$ for all $0 \leq k \leq n$. Thus, $A=\lambda_{0} I$ is a scalar, and we conclude that $\rho_{n}$ is irreducible. \(\square\)

Corollary 5.3. For every $n \geq 0, \mathrm{SU}(2)$ has an irreducible character $\chi_{n}$ given by
$$\chi_{n}\left(u_{\theta}\right)=\sum_{k=0}^{n} e^{i \theta(2 k-n)} .$$

Proof. Note that, by the spectral theorem for finite vector spaces, any element of $\mathrm{SU}(2)$ is conjugate to a diagonal matrix of the form $u_{\theta}$ defined previously. Thus, it is sufficient to define the characters on this subspace.

Now, consider again the basis $p_{k}=z_{1}^{k} z_{2}^{n-k}$ of $\mathcal{P}_{n}$. We already saw that
$$\rho_{n}\left(u_{\theta}\right) p_{k}=e^{i \theta(2 k-n)} p_{k},$$
from which we can conclude that the trace of $\rho_{n}\left(u_{\theta}\right)$ is
$$\chi_{n}\left(u_{\theta}\right)=\sum_{k=0}^{n} e^{i \theta(2 k-n)} .$$ \(\square\)

The previous corollary tells us that the span of the characters of $\operatorname{SU}(2)$ is dense in the even periodic functions. Specifically, denoting $\chi_{n}(\theta):=\chi_{n}\left(u_{\theta}\right)$, we can express $\cos (n \theta)$ for $n \in \mathbb{Z}$ as
$$1=\chi_{0} \quad \text { and } \quad \cos (\theta)=\frac{1}{2} \chi_{1}(\theta) \quad \text { and } \quad \cos (n \theta)=\frac{1}{2}\left(\chi_{n}(\theta)-\chi_{n-2}(\theta)\right),$$
which are dense in the even periodic $L^{2}$ functions by Theorem 5.1. In fact, this observation allows us to conclude that the $\rho_{n}$ we defined give all of the irreducible representations of SU(2).

Proposition 5.4. The $\rho_{n}$ enumerate all irreducible representations of SU(2).

Proof. Let $\rho$ be a representation with character $\chi$. Note that $\chi$ is completely described by its restriction to the $u_{\theta}$, since characters are invariant under conjugation and any SU(2) matrix can be diagonalized. Furthermore, since $u_{\theta}$ is conjugate to $u_{-\theta}$, we must have $\chi(-\theta)=\chi(\theta)$. In other words, $\chi$ is just an even function on the unit circle. Thus, by Theorem 5.1, $\chi$ decomposes as a sum of $\cos (n \theta)$ terms. However, we just saw that $\cos (n \theta)$ can be expressed in terms of the $\chi_{n}$. Thus, $\chi$ can be expressed as a sum of the $\chi_{n}$. In particular, $\chi$ contains at least one of the $\chi_{n}$, so $\chi$ is either one of them or is reducible. \(\square\)
5.3. SU(2) and $S^{3}$. Now that we have a concrete realization and understanding of all of the irreducible representations of SU(2), an application of Theorem 4.11 achieves our stated goal.

Proposition 5.5. The space $L^{2}\left(S^{3}\right) \cong L^{2}(\operatorname{SU}(2))$ decomposes as
$$L^{2}\left(S^{3}\right) \cong \widehat{\bigoplus} \bigoplus_{n \geq 0} C(\mathrm{SU}(2))_{n} .$$

However, this is not really a satisfying result. Indeed, while this is certainly a valid decomposition of the functions on $S^{3}$ into smaller algebras, it is not clear at all what the spaces $C(\operatorname{SU}(2))_{n}$ look like, or how they even relate to functions on $S^{3}$. Thus, to get a better understanding, we need to put a bit more effort into studying the matrix coefficients of SU(2).

Recall that the link between SU(2) and $S^{3}$ we had was based on mapping
$$\left[\begin{array}{cc}
\alpha & \beta \\
-\bar{\beta} & \bar{\alpha}
\end{array}\right] \mapsto\left(x_{1}, y_{1}, x_{2}, y_{2}\right) \in S^{3} \quad \text { where } \quad \alpha=x_{1}+i y_{1}, \beta=x_{2}+i y_{2} .$$

As such, it would make sense to consider the matrix coefficients as functions of $\alpha$ and $\beta$. For example, we can consider the action
$$\left[\begin{array}{cc}
\bar{\alpha} & -\beta \\
\bar{\beta} & \alpha
\end{array}\right] p_{k}=\left(\alpha z_{1}+\beta z_{2}\right)^{k}\left(-\bar{\beta} z_{1}+\bar{\alpha} z_{2}\right)^{n-k}=: F_{k}(\alpha, \beta)$$
as a polynomial in $\alpha, \beta, \bar{\alpha}$, and $\bar{\beta}$. Note that this is particularly convenient, as these 4 variables are linearly related to the variables $x_{1}, y_{1}, x_{2}$, and $y_{2}$.

There are now three insights that allow us to give a more concrete picture of $C(\operatorname{SU}(2))_{n}$. The first is that, since the $p_{k}$ are a basis of $\mathcal{P}^{n}$, a basis for $C(\mathrm{SU}(2))_{n}$ is given by
$$F_{k}^{m}(\alpha, \beta):=z_{1}^{n-m} z_{2}^{m} \text { coefficient of }\left(\alpha z_{1}+\beta z_{2}\right)^{k}\left(-\bar{\beta} z_{1}+\bar{\alpha} z_{2}\right)^{n-k} \text {, }$$
where $0 \leq m, k \leq n$.
Example 5.6. Consider the space $\mathcal{P}_{2}$. We have
$$\begin{aligned}
F_{0}=\left(\alpha z_{1}+\beta z_{2}\right)^{2} & =\alpha^{2} z_{1}^{2}+2 \alpha \beta z_{1} z_{2}+\beta^{2} z_{2}^{2} \\
F_{1}=\left(\alpha z_{1}+\beta z_{2}\right)\left(-\bar{\beta} z_{1}+\bar{\alpha} z_{2}\right) & =-\alpha \bar{\beta} z_{1}^{2}+(\alpha \bar{\alpha}-\beta \bar{\beta}) z_{1} z_{2}+\bar{\alpha} \beta z_{2}^{2} \\
F_{2}=\left(-\bar{\beta} z_{1}+\bar{\alpha} z_{2}\right)^{2} & =\bar{\beta}^{2} z_{1}^{2}-2 \bar{\alpha} \bar{\beta} z_{1} z_{2}+\bar{\alpha}^{2} z_{2}^{2} .
\end{aligned}$$
Thus, the $F_{k}^{m}$, which form a basis for the space of matrix coefficients, are

\begin{tabular}[t]{|l|l|l|l|}
\hline $F_{k}^{m}$ & 0 & 1 & 2 \\
\hline 0 & $\alpha^{2}$ & $2 \alpha \beta$ & $\beta^{2}$ \\
\hline 1 & $-\alpha \bar{\beta}$ & $\alpha \bar{\alpha}-\beta \bar{\beta}$ & $\bar{\alpha} \beta$ \\
\hline 2 & $\bar{\beta}^{2}$ & $-2 \bar{\alpha} \bar{\beta}$ & $\bar{\alpha}^{2}$ \\
\hline
\end{tabular} \(\square\)

The second observation is that $F_{k}$ is still real-homogeneous of degree $n$, i.e.,
$$F_{k}(\lambda \alpha, \lambda \beta)=\left(\lambda \alpha z_{1}+\lambda \beta z_{2}\right)^{k}\left(-\overline{\lambda \beta} z_{1}+\overline{\lambda \alpha} z_{2}\right)^{n-k}=\lambda^{n} F_{k}(\alpha, \beta)$$
for $\lambda \in \mathbb{R}$. Thus, we can also interpret the matrix coefficients as some subspace of the homogeneous polynomials of degree $n$ in 4 real variables, if we choose to write $\alpha, \beta$, and their conjugates in terms of the $x_{i}$ and $y_{i}$.

Example 5.7. Continuing the previous example, we get these degree 2 homogeneous polynomials:
$$\begin{array}{rlrl}
\alpha^{2} & =x_{1}^{2}+2 i x_{1} y_{1}-y_{1}^{2} & \bar{\alpha}^{2} & =x_{1}^{2}-2 i x_{1} y_{1}-y_{1}^{2} \\
\beta^{2} & =x_{2}^{2}+2 i x_{2} y_{2}-y_{2}^{2} & \bar{\beta}^{2} & =x_{2}^{2}-2 i x_{2} y_{2}-y_{2}^{2} \\
2 \alpha \beta & =2\left(x_{1} x_{2}+y_{1} y_{2}\right)+2 i\left(x_{1} y_{2}+x_{2} y_{1}\right) & -\alpha \bar{\beta} & =-x_{1} x_{2}+y_{1} y_{2}+i\left(x_{1} y_{2}-x_{2} y_{1}\right) \\
\bar{\alpha} \beta & =x_{1} x_{2}-y_{1} y_{2}+i\left(x_{1} y_{2}-x_{2} y_{1}\right) & -2 \bar{\alpha} \bar{\beta} & =-2\left(x_{1} x_{2}+y_{1} y_{2}\right)+2 i\left(x_{1} y_{2}+x_{2} y_{1}\right) \\
\alpha \bar{\alpha}-\beta \bar{\beta}=x_{1}^{2}+y_{1}^{2}-x_{2}^{2} & -y_{2}^{2} .
\end{array}$$ \(\square\)

The final observation is that, as a 4-variable real function, $F_{k}\left(x_{1}, y_{1}, x_{2}, y_{2}\right)$ is actually harmonic. If we write
$$\Delta=\frac{\partial^{2}}{\partial x_{1}^{2}}+\frac{\partial^{2}}{\partial y_{1}^{2}}+\frac{\partial^{2}}{\partial x_{2}^{2}}+\frac{\partial^{2}}{\partial y_{2}^{2}}=4 \frac{\partial^{2}}{\partial \alpha \partial \bar{\alpha}}+4 \frac{\partial^{2}}{\partial \beta \partial \bar{\beta}},$$
the symmetry of the two terms defining $F_{k}$ makes it easy to check that it is harmonic. Moreover, since $F_{k}$ is harmonic, each of the $F_{k}^{m}$ is too. We have therefore established that the matrix coefficients $C(\operatorname{SU}(2))_{n}$ are actually homogeneous harmonic polynomials of degree $n$ on $\mathbb{R}^{4}$. These polynomials are so important, in fact, that it is worth giving them a special symbol.

Definition 5.8. Let
$$\mathfrak{H}_{n}^{m}=\left\{p \in \mathcal{P}_{n}\left(\mathbb{R}^{m}\right) \mid \Delta p=0\right\},$$
i.e., the space of all harmonic homogeneous polynomials of degree $n$ on $\mathbb{R}^{m}$.
Example 5.9. The space $\mathfrak{H}_{2}^{4}$ is simple enough that one can manually enumerate the possibilities. Doing so shows that $\mathfrak{H}_{2}^{4}$ is 9-dimensional, with basis
$$x_{1}^{2}-y_{1}^{2}, x_{2}^{2}-y_{2}^{2}, x_{1}^{2}-x_{2}^{2}, x_{1} y_{1}, x_{1} x_{2}, x_{1} y_{2}, y_{1} x_{2}, y_{1} y_{2}, x_{2} y_{2} .$$ \(\square\)

Curiously, the previous examples show that $\mathfrak{H}_{2}^{4}$ and $C(\operatorname{SU}(2))_{2}$ actually have the same dimension and are thus the same space. It turns out this is a general phenomenon: $C(\operatorname{SU}(2))_{n}$ is not only a subspace of $\mathfrak{H}_{n}^{4}$, but is in fact equal to it. Proving this is most easily done by noting both of these spaces have dimension $(n+1)^{2}$. For $C(\mathrm{SU}(2))_{n}$, this follows immediately from the fact that the $n+1$ elements $p_{k}$ form a basis of $\mathcal{P}_{n}$. On the other hand, to see that $\mathfrak{H}_{n}^{4}$ has dimension $(n+1)^{2}$, consult Appendix A. In any case, putting everything together, we finally get the proper hyperspherical decomposition on $S^{3}$.

Theorem 5.10 ( $S^{3}$ hyperspherical decomposition). The space $L^{2}\left(S^{3}\right) \cong$ $L^{2}(\mathrm{SU}(2))$ decomposes as
$$\left.L^{2}\left(S^{3}\right) \cong \bigoplus_{n \geq 0} \mathfrak{H}_{n}^{4}\right|_{S^{3}},$$
where $\left.\right|_{S^{3}}$ denotes restriction to $S^{3} \subseteq \mathbb{R}^{4}$. Furthermore, the coefficients in this decomposition can be calculated as
$$F_{i j}^{n}=\left\langle f, m_{i j}\right\rangle_{\mathrm{SU}(2)}=\int_{S^{3}} f \overline{m_{i j}^{n}} \mathrm{~d} \mu \quad \text { for } \quad 0 \leq i, j \leq n .$$

Remark 5.11. The invariant metric $\mu$ on $\operatorname{SU}(2)$ is, unfortunately, rather complicated, so we will not be writing it down explicitly.

\section*{6. Applications to $S^{2}$}

Our final task is to tackle spherical decompositions on $S^{2}$. This is hindered by the fact that $S^{2}$ has no obvious group structure; in fact, it can be shown that there is no way to give $S^{2}$ a group structure compatible with its geometry (see [Lee18]). For this reason, we will need to change our approach slightly.

The most important insight is that, while $S^{2}$ is not a group itself, it is certainly acted upon very naturally by many groups. In particular, the group SO(3) of three-dimensional rotations has a natural action on the 2-sphere. This action is transitive, i.e., the orbit of every point is all of $S^{2}$ but is not faithful. Indeed, the stabilizer of any point is a subgroup of SO(3) isomorphic to SO(2). This is easy to see geometrically: any rotation that fixes a particular point on the surface of the sphere must be a rotation through that point, and so these collectively form a group of two-dimensional rotations. Thus, by the orbit-stabilizer theorem, we have an identification
$$S^{2} \cong \operatorname{SO}(3) / \operatorname{SO}(2) .$$

This identification now gives us a useful way to think about $L^{2}\left(S^{2}\right)$. Namely, consider a function $f \in L^{2}(\mathrm{SO}(3))$ that is SO(2) invariant. Then, $f$ can just be defined on $\mathrm{SO}(3) / \mathrm{SO}(2)$-cosets, which we just saw are isomorphic to $S^{2}$. On the other hand, any function $f \in L^{2}\left(S^{2}\right)$ can be lifted to a function $f \in L^{2}(\mathrm{SO}(3))$ that is SO(2) invariant, so we have established an isomorphism
$$L^{2}\left(S^{2}\right) \cong L^{2}(\mathrm{SO}(3))^{\mathrm{SO}(2)},$$
where the superscript ${ }^{\mathrm{SO}(2)}$ denotes the subspace of SO(2)-invariant functions. But now note that we can understand $L^{2}(\mathrm{SO}(3))$ very well using Theorem 4.11,
and taking an SO(2)-invariant subspace commutes nicely with the decomposition we had. Indeed, we have
$$L^{2}(\mathrm{SO}(3))^{\mathrm{SO}(2)}=\left[\widehat{\bigoplus}_{\rho \in \widehat{\mathrm{SO}(3)}} C(\mathrm{SO}(3))_{\rho}\right]^{\mathrm{SO}(2)}=\widehat{\bigoplus}_{\rho \in \widehat{\mathrm{SO}(3)}}\left(C(\mathrm{SO}(3))_{\rho}\right)^{\mathrm{SO}(2)} .$$
Because of this, we see that we should try to understand the irreducible representations of SO(3) in order to understand $L^{2}\left(S^{2}\right)$.
6.1. From SU(2) to SO(3) representations. To derive the irreducible representations of SO(3), we will use a classical result that SU(2) is the double-cover of SO(3). Intuitively, this means that there is a way of mapping SU(2) onto SO(3) such that a $2 \pi$ rotation in SO(3) corresponds to the map $-I$ in SU(2). The precise proof and details of this result are not so important for us (see [vdB93, Sec. 20] for the details). All that matters is that there is a surjective homomorphism
$$\phi: \mathrm{SU}(2) \rightarrow \mathrm{SO}(3) \quad \text { with } \quad \operatorname{ker} \phi= \pm I .$$
The existence of this homomorphism allows us to use what we already know about SU(2) representations, namely Proposition 5.4, to completely characterize SO(3) representations.

In particular, consider an irreducible representation $\tilde{\rho}$ of SO(3). We can then lift this to a representation $\rho=\tilde{\rho} \circ \phi$ of SU(2) where $-I$ acts as the identity. Since $\tilde{\rho}$ is irreducible, $\rho$ must be as well, so we can conclude that $\rho=\rho_{n}$ for some $n \geq 0$. But if $n$ is odd, then
$$\rho(-I) p(\mathbf{z})=p(-\mathbf{z})=(-1)^{n} p(\mathbf{z})=-p(\mathbf{z}),$$
so $-I$ does not act as the identity. Thus, $n=2 k$ is even, and we have that $\tilde{\rho}$ is given by projecting $\rho_{2 k}$ onto $\operatorname{SO}(3)$. We thus get the following proposition.

Proposition 6.1. The irreducible representations of $\mathrm{SO}(3)$ are given by
$$\tilde{\rho}_{k}=\rho_{2 k} \circ \phi^{-1} \quad \text { for some } \quad k \geq 0 .$$
In particular, SO(3) has an irreducible representation of dimension $2 k+1$ for every $k \geq 0$.

Remark 6.2. One should reasonably object that $\phi^{-1}$ is not actually defined, since $\phi$ is not injective. Instead, by $\phi^{-1}$, we mean any right inverse of $\phi$ (i.e., a map such that $\phi \circ \phi^{-1}=\mathrm{id}_{\mathrm{SO}(3)}$, which exists since $\phi$ is surjective). That the $\tilde{\rho}_{k}$ do not depend on the choice of right inverse then follows from the fact that the only ambiguity in $\phi^{-1}(g)$ is a ± freedom, which is irrelevant since $\rho_{2 k}(-g)=\rho_{2 k}(g)$.

Having this description of the irreducible representations, we can also ask what the characters of SO(3) are. To do so, note that complexifying SO(3)
and applying the complex spectral theorem shows that any element of SO(3) is conjugate to a matrix
$$R_{\theta}=\left[\begin{array}{ccc}
1 & 0 & 0 \\
0 & \cos \theta & \sin \theta \\
0 & -\sin \theta & \cos \theta
\end{array}\right],$$
which form an SO(2) subgroup. Furthermore, while we will not show it, the preimage of $R_{\theta}$ under $\phi$ is given by
$$u_{\theta / 2}=\left[\begin{array}{cc}
e^{-i \theta / 2} & 0 \\
0 & e^{i \theta / 2}
\end{array}\right],$$
where we are treating the range of $\theta$ as $[0,4 \pi)$ to make this "inverse" continuous. Intuitively, this is just the fact that a full $2 \pi$ rotation in SO(3) corresponds to the map $-I$ in $\mathrm{SU}(2)$. With this in hand, we can calculate the characters.

Corollary 6.3. The character of $\tilde{\rho}_{n}$ is given by
$$\tilde{\chi}_{n}\left(R_{\theta}\right)=\sum_{k=-n}^{n} e^{i \theta k} .$$

Proof. We have
$$\tilde{\chi}_{n}\left(R_{\theta}\right)=\chi_{2 n}\left(u_{\theta / 2}\right)=\sum_{k=0}^{2 n} e^{i \theta(2 k-2 n) / 2}=\sum_{k=0}^{2 n} e^{i \theta(k-n)}=\sum_{k=-n}^{n} e^{i \theta k} .$$ \(\square\)
6.2. Harmonic polynomials and SO(3) representations. While we now have both the characters and descriptions of the irreducible representations, it is still worth thinking about a more direct realization of them. Namely, our current scheme requires lifting elements of SO(3) to SU(2), and then acting on complex 2-variable polynomials, which is rather involved. Ideally, we would directly relate SO(3) representations to functions of 3 real variables.

To do so, we will draw some further inspiration from the case of SU(2) representations and consider the homogeneous harmonic polynomials $\mathfrak{H}_{n}^{3}$ on $\mathbb{R}^{3}$. Since the Laplacian is invariant under rotations, there is a natural action of SO(3) on these polynomials given by
$$g p(\mathbf{r})=p\left(g^{-1} \mathbf{r}\right) .$$
As shown in Appendix A, $\mathfrak{H}_{n}^{3}$ is $2 n+1$ dimensional, the same as $\tilde{\rho}_{n}$. This begs asking if these two representations are, in fact, isomorphic. Indeed, they are.

Proposition 6.4. The representations $\left(\tilde{V}_{n}, \tilde{\rho}_{n}\right)$ from Proposition 6.1 and $\left(\mathfrak{H}_{n}^{3}, \mathfrak{p}_{n}\right)$ of $\operatorname{SO}(3)$ are isomorphic. In particular, the $\mathfrak{H}_{n}^{3}$ also exhaust the irre-ducible representations of SO(3).

Proof. Since the $\tilde{V}_{i}$ exhaust all irreducible representations of SO(3), we must have
$$\mathfrak{H}_{n}^{3}=\bigoplus_{i \in I} \tilde{V}_{m_{i}}$$
for some indexing set $I$. Comparing dimensions, we have that
$$2 n+1=\sum_{i \in I} 2 m_{i}+1 .$$
In particular, we just need to show that $m_{i} \geq n$ for some $i$ and we are done. To do so, we can compare the characters
$$\chi\left(R_{\theta}\right)=\sum_{i \in I} \sum_{k=-m_{i}}^{m_{i}} e^{i \theta k} .$$
Now, notice that if we can show $\mathfrak{p}_{n}\left(R_{\theta}\right)$ has an eigenvalue $e^{i n \theta}$, then the sum on the right must include an $e^{i n \theta}$ term as well, since a character is just the sum of eigenvalues. This would in turn show that one of the $m_{i}$ is greater than $n$, as that is the only way an $e^{i n \theta}$ term could appear.

To show this, consider the polynomial $Y_{n}(\mathbf{r})=(y+i z)^{n}$. This is a harmonic homogeneous polynomial of degree $n$. Indeed, it is holomorphic as a function of $y+i z$, and it is a standard result of complex analysis that the real and imaginary parts of holomorphic functions are harmonic when regarded as functions of two real variables. Furthermore, we have
$$\begin{aligned}
\mathfrak{p}_{n}\left(R_{\theta}\right) Y_{n} & =(y \cos \theta-z \sin \theta+i(y \sin \theta+z \cos \theta))^{n} \\
& =\left(e^{i \theta} y+i e^{i \theta} z\right)^{n} \\
& =e^{i \theta n} Y_{n},
\end{aligned}$$
completing the proof. \(\square\)
6.3. SO(3)/ SO(2) and $S^{2}$. Now that we have a very concrete understanding of the representations of SO(3), the only thing stopping us from determining a decomposition of $L^{2}\left(S^{2}\right)$ is an understanding of the spaces
$$C(\mathrm{SO}(3))_{n}^{\mathrm{SO}(2)} .$$
To do so, let us first consider the general case of a space
$$C(G)_{\rho}^{H} \quad \text { for } \quad H \subseteq G .$$
This is, by definition, just the space of matrix coefficients invariant under the $H$-action. Letting $V$ be the vector space of $\rho$, we can further say that the space of matrix coefficients is isomorphic to the endomorphisms of $V$, since
they match dimension. As such, we can interpret $C(G)_{\rho}^{H}$ as the subspace of $\operatorname{End}(V)$ invariant under the $H$-action, i.e., the endomorphisms
$$A \in \operatorname{End}(V) \quad \text { such that } \quad A h=A \quad \text { for } \quad h \in H .$$
Using now the unitary structure of $V$, we conclude that $A=0$ on the orthogonal complement of $V^{H}$, the subspace of $V$ fixed by $H$. Indeed, we could otherwise restrict to a subspace of $\left(V^{H}\right)^{\perp}$ where $A$ is invertible and conclude that $H$ acts as the identity, a contradiction. Thus, restriction to $V^{H}$ now induces an isomorphism
$$C(G)_{\rho}^{H} \cong \operatorname{Hom}\left(V^{H}, V\right) .$$

Example 6.5. If we take $H=\{1\}$ to be the trivial subgroup, we are just asserting a homomorphism
$$C(G)_{\rho} \cong C(G)_{\rho}^{H} \cong \operatorname{Hom}\left(V^{H}, V\right) \cong \operatorname{End}(V) .$$
If we take $\rho$ to be the trivial representation, on the other hand, and let $H$ be any subgroup, we are asserting that
$$\mathbb{C} \cong C(G)_{1}^{H} \cong \operatorname{Hom}\left(\mathbb{C}^{H}, \mathbb{C}\right) \cong \mathbb{C} .$$ \(\square\)

Applying this to the case of $C(\mathrm{SO}(3))_{n}^{\mathrm{SO}(2)}$, we see that we really just need to study
$$\operatorname{Hom}\left(\tilde{V}_{n}^{\mathrm{SO}(2)}, \tilde{V}_{n}\right) \cong \operatorname{Hom}\left(\mathcal{P}_{2 n}^{\mathrm{SO}(2)}, \mathcal{P}_{2 n}\right) .$$
However, recall from earlier that the preimage of SO(2) in SU(2) is just U(1). Furthermore, the U(1) action on $\mathcal{P}_{2 n}$ was given by
$$u_{\theta} p_{k}=e^{i \theta(2 k-2 n)} p_{k} .$$
This action is trivial only when $k=n$, so the space $\mathcal{P}_{2 n}^{\mathrm{SO}(2)} \cong \mathcal{P}_{2 n}^{\mathrm{U}(1)}$ is actually just one-dimensional, i.e., is just $\mathbb{C}$. In particular, we have
$$C(\operatorname{SO}(3))_{n}^{\operatorname{SO}(2)} \cong \operatorname{Hom}\left(\mathbb{C}, \tilde{V}_{n}\right) \cong \tilde{V}_{n} \cong \mathfrak{H}_{n}^{3} .$$
Thus, we have finally proved our main result on the decomposition of $L^{2}\left(S^{2}\right)$.
Theorem 6.6 ( $S^{2}$ spherical decomposition). The space $L^{2}\left(S^{2}\right) \cong L^{2}(\operatorname{SO}(3))^{\operatorname{SO}(2)}$ decomposes as
$$\left.L^{2}\left(S^{2}\right) \cong \widehat{\bigoplus} \mathfrak{H}_{n \geq 0} \mathfrak{H}_{n}^{3}\right|_{S^{2}} .$$
Furthermore, the coefficients in this decomposition can be calculated as
$$F_{i}^{n}=\left\langle f, m_{i}^{n}\right\rangle_{S^{2}}=\int_{S^{2}} f \overline{m_{i}^{n}} \mathrm{~d} \mu \quad \text { for } \quad|i|<n .$$

Remark 6.7. One might wonder why we are allowed to freely restrict $\mathfrak{H}_{n}^{3}$ to $S^{2}$. However, this restriction actually loses no information, as
$$p(\mathbf{r})=p(r \hat{\mathbf{r}})=r^{n} p(\hat{\mathbf{r}}) \quad \text { for } \quad p \in \mathfrak{H}_{n}^{3} .$$
In particular, $p$ is already determined by its values on $S^{2}$.
Also, as it turns out, the relevant metric $\mathrm{d} \mu$ to use for the integration is indeed the standard metric on a sphere $\mathrm{d} \Omega$, though we will not prove this.

\section*{7. Conclusions}

The results we obtain here are about as far as we can go with just the Peter-Weyl theorem. However, there are definitely many ways to extend these results. For starters, any practical decomposition of functions on $S^{2}$ would ideally involve spherical polar coordinates, as these are the most natural. Indeed, it is possible to derive an explicit formula giving a basis of $\mathfrak{H}_{n}^{3}$ in terms of polar coordinates. For a reference, see [vdB93, Sec. 31].

Generalizing the decompositions discussed here to even-higher-dimensional spheres is also certainly possible. Indeed, just from the results we obtained, one might already guess that a decomposition into harmonic homogeneous polynomials is always possible. This is indeed the case, though a full proof certainly requires much more work. One way to approach this generalization would be to realize that we can always consider $S^{n}$ as a quotient
$$S^{n} \cong \operatorname{SO}(n+1) / \operatorname{SO}(n)$$
and apply similar techniques as we did in Section 6. This path of generalization actually has connections to very current mathematical research, such as the Langlands program (see [GR06]).

On the other hand, one could also consider the idea of further generalizing the Peter-Weyl theorem. Unfortunately, a full generalization to even all locally compact groups is much more difficult. However, the special case of abelian locally compact groups is well understood thanks to Pontryagin duality, which an interested reader can find more about in [Rud17, Chap. 1.7]. This route then gives, for example, the Fourier transform on $\mathbb{R}$, among other things.

\section*{Appendix A. Dimension of $\mathfrak{H}_{m}^{n}$}

Letting $P\left(\mathbb{R}^{n}\right)$ be the space of all polynomials on $\mathbb{R}^{n}$, we will consider the subspaces
$$\mathcal{P}_{m}^{n}=\left\{p \in P\left(\mathbb{R}^{n}\right) \mid p(\lambda \mathbf{r})=\lambda^{m} p(\mathbf{r})\right\} \quad \text { and } \quad \mathfrak{H}_{m}^{n}=\left\{p \in \mathcal{P}_{m}^{n} \mid \Delta p=0\right\} .$$
To start, we calculate the dimension of $\mathcal{P}_{m}^{n}$.
Proposition A.1.
$$\operatorname{dim} \mathcal{P}_{m}^{n}=\binom{n+m-1}{n-1} .$$

Proof. A basis for $\mathcal{P}_{m}^{n}$ is given by the monomials
$$x_{1}^{\alpha_{1}} x_{2}^{\alpha_{2}} \ldots x_{n}^{\alpha_{n}} \quad \text { with } \quad \alpha_{1}+\alpha_{2}+\cdots+\alpha_{n}=m .$$
In particular, the number of such monomials is just the number of ways to write $m$ as the sum of an $n$-tuple of nonnegative integers. This is just the classical stars-and-bars problem from combinatorics, with solution $\binom{n+m-1}{n-1}$. \(\square\)

Having determined the dimension of $\mathcal{P}_{m}^{n}$, we can now determine the dimension of $\mathfrak{H}_{m}^{n}$ by cleverly decomposing it into lower-dimensional homogeneous polynomial spaces.

Proposition A.2.
$$\operatorname{dim} \mathfrak{H}_{m}^{n}=\operatorname{dim} \mathcal{P}_{m}^{n-1}+\operatorname{dim} \mathcal{P}_{m-1}^{n-1} .$$

Proof. Consider some $p=p\left(x_{1}, x_{2}, \ldots, x_{n}\right) \in \mathfrak{H}_{m}^{n}$. We can expand this as a sum around $x_{1}$, giving
$$p=\sum_{k=0}^{m} \frac{f_{k}\left(x_{2}, \ldots, x_{n}\right)}{k!} x_{1}^{k} .$$
Note that $f_{k}$ is a homogeneous polynomial, now of degree $m-k$; in other words, $f_{k} \in \mathcal{P}_{m-k}^{n-1}$. Taking the Laplacian, we get
$$\begin{aligned}
\Delta p & =\sum_{k=2}^{m} \frac{f_{k}}{k!} k(k-1) x_{1}^{k-2}+\sum_{k=0}^{m} \frac{x_{1}^{k}}{k!}\left(\Delta^{\prime} f_{k}\right) \\
& =\sum_{k=0}^{m-2} \frac{f_{k+2}}{k!} x_{1}^{k}+\sum_{k=0}^{m} \frac{x_{1}^{k}}{k!}\left(\Delta^{\prime} f_{k}\right),
\end{aligned}$$
where the $\Delta^{\prime}$ Laplacian excludes the $x_{1}$ coordinate. Analyzing the second term a bit more, we see that if $k=m, m-1$, then $f_{k}$ is a polynomial of degree 0 or 1 , so the Laplacian must vanish. Thus, we get
$$\Delta p=\sum_{k=0}^{m-2} \frac{x_{1}^{k}}{k!}\left(f_{k+2}+\Delta^{\prime} f_{k}\right) .$$

In particular, if $p$ is harmonic, we must have
$$f_{k+2}+\Delta^{\prime} f_{k}=0 \quad \text { for } \quad 0 \leq k \leq m-2 .$$
Thus, specifying $f_{0}$ and $f_{1}$ determines $p$. Namely
$$\mathfrak{H}_{m}^{n} \cong \mathcal{P}_{m}^{n-1} \oplus \mathcal{P}_{m-1}^{n-1},$$
which proves the proposition. \(\square\)

Corollary A.3.
$$\operatorname{dim} \mathfrak{H}_{m}^{n}=\binom{n+m-2}{n-2}+\binom{n+m-3}{n-2} .$$

Example A.4. If we take $n=3$, we get
$$\operatorname{dim} \mathfrak{H}_{m}^{3}=\binom{m+1}{1}+\binom{m}{1}=2 m+1,$$
proving the claim that $\mathfrak{H}_{m}^{3}$ and $\tilde{V}_{m}$ have the same dimension. \(\square\)

Example A.5. If we take $n=4$, we get
$$\begin{aligned}
\operatorname{dim} \mathfrak{H}_{m}^{4} & =\binom{m+2}{2}+\binom{m+1}{2} \\
& =\frac{(m+2)(m+1)}{2}+\frac{(m+1) m}{2} \\
& =\frac{(m+1)(2 m+2)}{2} \\
& =(m+1)^{2},
\end{aligned}$$
proving the claim that $\mathfrak{H}_{m}^{4}$ and $C(\operatorname{SU}(2))_{m}$ have the same dimension. \(\square\)

\section*{References}
[Axl19] Sheldon Axler. Measure, Integration \& Real Analysis. Springer Nature, 2019.
[GR06] Benedict Gross and Mark Reeder. From laplace to langlands via representations of orthogonal groups. Bulletin of the American Mathematical Society, 43:163-205, 2006.
[Lee18] Seewoo Lee. $s^{2}$ is not a lie group. https://web.archive.org/web/20240303215238/https://math.berkeley.edu/ ${ }^{\sim}$ seewoo5/S2notLiegrp.pdf,2018.
[Mor19] Sophie Morel. Representation theory. https://web.archive.org/web/20221223074434/https://perso.ens-lyon.fr/sophie.morel/rep_theory_notes.pdf, 2019.
[Rud17] Walter Rudin. Fourier Analysis on Groups. Dover Publications, 2017.
[vdB93] E.P. van den Ban. Harmonic analysis. https://web.archive.org/web/20220815001533/https://webspace.science.uu.nl/ ${ }^{\sim}$ ban00101/lecnotes/mc93.pdf, 1993.
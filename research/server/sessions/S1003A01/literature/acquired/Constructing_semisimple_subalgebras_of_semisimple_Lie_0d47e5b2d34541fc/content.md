---
retention_scope: session
part: 1
total_parts: 1
---

---
source_file: 1004_1972v1.pdf
converter: mathpix
format: mmd
---

\title{
Constructing semisimple subalgebras of semisimple Lie algebras
}

\author{
Willem A. de Graaf \\ Dipartimento di Matematica \\ Università di Trento \\ Italy
}

\begin{abstract}
Algorithms are described that help with obtaining a classification of the semisimple subalgebras of a given semisimple Lie algebra, up to linear equivalence. The algorithms have been used to obtain classifications of the semisimple subalgebras of the simple Lie algebras of ranks $\leq 8$. These have been made available as a database inside the SLA package of GAP4. The subalgebras in this database are explicitly given, as well as the inclusion relations among them.
\end{abstract}

\section*{1 Introduction}

It is an extensively studied problem to classify the semisimple subalgebras of a complex semisimple Lie algebra $\mathfrak{g}$, up to an equivalence relation. The most natural equivalence relation for this is the one of conjugacy by the inner automorphism group $G$. Two subalgebras of $\mathfrak{g}$ are simply called equivalent if they are conjugate under $G$. In [5], Dynkin also considered the notion of linear equivalence: two subalgebras $\mathfrak{g}_{1}, \mathfrak{g}_{2} \subset \mathfrak{g}$ are said to be linearly equivalent if for every representation $\rho: \mathfrak{g} \rightarrow \mathfrak{g} \mathfrak{l}(V)$ the subalgebras $\rho\left(\mathfrak{g}_{1}\right), \rho\left(\mathfrak{g}_{2}\right)$ of $\mathfrak{g} \mathfrak{l}(V)$ are conjugate under $\operatorname{GL}(V)$.

A subalgebra of $\mathfrak{g}$ is called regular if it is normalised by a Cartan subalgebra of $\mathfrak{g}$. Semisimple subalgebras of this kind correspond to root subsystems of the root system of $\mathfrak{g}$. An $S$-subalgebra is a subalgebra which is not contained in a regular subalgebra.

In [4] Dynkin classified the maximal semisimple $S$-subalgebras of the Lie algebras of classical type, upto equivalence. More precisely, [4] contains a description, or a procedure, by which it is possible for a given Lie algebra of classical type to find its maximal semisimple $S$-subalgebras.

Dynkin treated the Lie algebras of exceptional type in [5]. The main results of this paper are
\begin{itemize}
\item[-] an algorithm to classify the regular subalgebras of a semisimple Lie algebra, up to equivalence,
\end{itemize}
\begin{itemize}
\item[-] a classification of the semisimple $S$-subalgebras, up to equivalence, of the Lie algebras of exceptional type,
\item[-] a classification of the simple subalgebras, up to linear equivalence, of the Lie algebras of exceptional type.
\end{itemize}

Lorente and Gruber ([12]) applied Dynkin's methods to obtain explicit lists of semisimple subalgebras of the simple Lie algebras of classical type. More in particular, they obtained lists of the regular subalgebras and of the $S$-subalgebras of the Lie algebras of classical type of ranks $\leq 6$.

Recently Minchenko ([14]) has revisited Dynkin's classification of the simple subalgebras of the simple Lie algebras of exceptional type. He corrected several small mistakes (most notably he found two extra simple subalgebras in the Lie algebra of type $E_{8}$ ). Secondly he found the classification of the simple subalgebras up to equivalence. Thirdly, he has computed a lot of additional data (such as the normalisers of the subalgebras in $G$ ).

One motivation for studying semisimple subalgebras of semisimple Lie algebras comes from theoretical physics. In models like the vibron model and the interacting boson model (cf. [10]) chains of subalgebras are used. For applications of this kind the subalgebras need to be explicitly given, i.e., for each equivalence class a representative needs to be given by a basis. Furthermore, methods are needed to obtain the inclusion relations between the subalgebras (more precisely: to decide whether two given classes have representatives such that one is contained in the other). The classifications present in the literature do not appear to immediately give this. For example, in [5], only the $S$-subalgebras are explicitly constructed. And only the simple subalgebras are listed, and not the semisimple ones (with the exception of the $S$-subalgebras). Finally no inclusion relations are given (again with the exception of the $S$-subalgebras).

The aim of this paper is to describe algorithms, and report on the results obtained with their implementation, that help with obtaining a classification of the semisimple subalgebras of a given semisimple Lie algebra, up to linear equivalence. Furthermore, the subalgebras are explicitly constructed, as well as the inclusion relations among them. Here we say that the algorithms "help" to obtain a classification as one step in the algorithms (the construction of the subalgebras) is not entirely algorithmic - occasionally some human intervention is needed for that.

Equivalence implies linear equivalence, but the converse is not always true. However, if $\mathfrak{g}$ is of type $A_{n}, B_{n}, C_{n}, F_{4}, G_{2}$ then the two concepts coincide (cf. [14], Theorem 3). In the remaining types there are some exceptions and they are explicitly described ([5], [14]). Hence it is straightforward to obtain the classification of the semisimple subalgebras up to equivalence from the list of semisimple subalgebras up to linear equivalence. One of the main advantages of linear equivalence as opposed to equivalence is that we have a method for deciding it (see Section 3). For these reasons in this paper we focus exclusively on linear equivalence.

By considering embeddings of Lie algebras in $\mathfrak{g}$, rather than subalgebras of $\mathfrak{g}$ we get a slightly different perspective on the problem. Also for embeddings we have the notions of
equivalence and linear equivalence. Let $\tilde{\mathfrak{g}}$ be a semisimple Lie algebra, and $\varphi_{1}, \varphi_{2}: \tilde{\mathfrak{g}} \hookrightarrow \mathfrak{g}$ injective homomorphisms. They are said to be equivalent if there is a $\sigma \in G$ with $\varphi_{1}=\sigma \varphi_{2}$. They are said to be linearly equivalent if for each representation $\rho: \mathfrak{g} \rightarrow \mathfrak{g} \mathfrak{l}(V)$ the induced representations $\rho \varphi_{1}, \rho \varphi_{2}$ of $\tilde{\mathfrak{g}}$ are equivalent. Let $\tilde{\mathfrak{g}}$ be a semisimple Lie algebra, and $\mathfrak{g}^{\prime} \subset \mathfrak{g}$ a subalgebra isomorphic to $\tilde{\mathfrak{g}}$. There can be several non-equivalent embeddings $\tilde{\mathfrak{g}} \hookrightarrow \mathfrak{g}^{\prime}$. This is only possible if $\tilde{\mathfrak{g}}$ has outer automorphisms. From a classification of subalgebras up to linear equivalence it is straightforward to get all embeddings up to linear equivalence. For this reason we concentrate on constructing subalgebras, rather than embeddings.

One approach to the problem is to start from the existing classifications in the literature. One could take the maximal $S$-subalgebras constructed by Dynkin, along with the regular subalgebras, and by successively constructing their subalgebras get the entire list of subalgebras. This, however, would not confirm, or correct, the existing classifcation. Moreover, if the list of maximal subalgebras has an error, then this will lead to many errors in the resulting classification. (And it appears that this can, for example, easily happen in type $D_{2 n}$, see below.) For these reasons the approach taken here aims at obtaining the classification from scratch. This has the added advantage that the classifications in the literature and the new ones can validate each other. In particular, if both are the same then this constitutes a good argument for their correctness.

The main idea used here to classify subalgebras is to start with the ones of smallest rank. The subalgebras of rank 1 are well-known from the classification of the nilpotent $G$-orbits in $\mathfrak{g}$. Secondly we construct the subalgebras of higher rank as a kind of extension of algebras of lower rank. This way we "climb our way up". So, in a sense, it is the reverse approach to starting with the maximal subalgebras.

The algorithms described in this paper have been implemented in the language of the computer algebra system GAP4 ([6]), using the package SLA ([8]). The main result that has been obtained using this implementation is a database of all semisimple subalgebras of the simple Lie algebras of ranks $\leq 8$. This database is also contained in the package SLA. It also contains all inclusion relations between the linear equivalence classes. It is complemented by a function for computing the semisimple subalgebras of a semisimple, non-simple, Lie algebra. In Table 1 we show some statistics relative to the simple Lie algebras of ranks 7, 8. The table contains the number of (linear equivalence classes of) subalgebras, and the number of their isomorphism types.

There is also the question of the field of definition. The simple Lie algebras are given by a multiplication table relative to a Chevalley basis. The subalgebras are given by a basis. However, not all linear equivalence classes of subalgebras have a representative with a basis with coefficients in $\mathbb{Q}$ (with respect to the given Chevalley basis). Our results show that for all semisimple subalgebras of the simple Lie algebras of ranks $\leq 8$ there exists a field extension $F$ of degree $\leq 2$ of $\mathbb{Q}$, such that the subalgebra can be given by a basis with coefficients in $F$. The last column of Table 1 gives a field extension $F$ of $\mathbb{Q}$ such that all semisimple subalgebras can be given by a basis with coefficients in $F$. Here we remark that it is by no means clear that these are the smallest possible fields (except, of course, when the field is $\mathbb{Q}$ ). We have made an effort to keep the fields small; but the problem of finding the absolute smallest field is a difficult one which we do not solve here.

\begin{table}
\begin{tabular}[t]{|l|l|l|l|}
\hline & \# subalgebras & \# types & field of definition \\
\hline $A_{7}$ & 131 & 32 & $\mathbb{Q}$ \\
\hline $B_{7}$ & 849 & 95 & $\mathbb{Q}(\sqrt{-1}, \sqrt{-2}, \sqrt{-3})$ \\
\hline $C_{7}$ & 822 & 76 & $\mathbb{Q}$ \\
\hline $D_{7}$ & 511 & 72 & $\mathbb{Q}(\sqrt{-1}, \sqrt{-3}, \sqrt{-5})$ \\
\hline $E_{7}$ & 501 & 76 & $\mathbb{Q}(\sqrt{-3})$ \\
\hline $A_{8}$ & 232 & 46 & $\mathbb{Q}$ \\
\hline $B_{8}$ & 2186 & 165 & $\mathbb{Q}(\sqrt{-1}, \sqrt{-3})$ \\
\hline $C_{8}$ & 2127 & 126 & $\mathbb{Q}(\alpha), \alpha^{2}-\alpha-1=0$ \\
\hline $D_{8}$ & 1664 & 127 & $\mathbb{Q}(\sqrt{-1}, \sqrt{-3})$ \\
\hline $E_{8}$ & 1183 & 155 & $\mathbb{Q}(\sqrt{-1}, \sqrt{-3}, \beta), \beta^{2}+\beta+2=0$ \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 1: Semisimple subalgebras of the simple Lie algebras of rank 7 and 8. The second column displays the number of linear equivalence classes of subalgebras. The third column has the number of different isomorphism types of subalgebras. The last column has a field over which all subalgebras are simultaneously defined.}
\end{table}

Next there is the question of the validation of the results: how can we be certain that our classifications are correct? Although in this paper we prove the correctness of the method that we use, there is still ample possibility to make mistakes while using it. However we do have some circumstantial evidence for the correctness of our lists. Firstly, the method does not deal with regular subalgebras differently than with other subalgebras. But at the end we find the same regular subalgebras as with Dynkin's algorithm from [5]. Secondly, the $S$-subalgebras that we find in the exceptional types coincide with the ones found by Dynkin. In the classical types for ranks $\leq 6$ we find the same $S$-subalgebras as Lorente and Gruber ([12]) (except in $D_{4}, D_{6}$, see below). Thirdly, also the lists of simple subalgebras agree with those found by Dynkin (and in the case of $E_{8}$ corrected by Minchenko).

One result of our calculations is that in type $D_{2 n}$, for $n=2,3,4$, there appear maximal semisimple subalgebras which are isomorphic, but not linearly equivalent. In type $D_{4}$ there are three (linear equivalence classes of) maximal subalgebras of types $A_{1} B_{2}$ and $B_{3}$. In type $D_{6}$ there are two maximal subalgebras of each type $A_{1} C_{3}$ and $A_{5}$. And in $D_{8}$ there are two maximal subalgebras of each type $B_{2} B_{2}, B_{4}, A_{1} C_{4}$ and $A_{7}$. This appears not to have been known in the literature, for example [13] lists one algebra for each of the above types. In all cases the algebras are conjugate under outer automorphisms. It would be interesting to formulate and prove a general statement about the maximal subalgebras of the Lie algebra of type $D_{2 n}$. However, this would be beyond the scope of this paper. We intend to come back to it in a subsequent paper.

This paper is structured as follows. The next section describes a number of concepts and results from the literature that we need. This allows us at the end of the same section to give a more or less detailed description of the method we use. The subsequent sections then describe every step in detail.

Acknowledgement: It is my pleasure to thank Luigi Scorzato and Lorenzo Fortunato
for having suggested the topic of the paper to me, and for many fruitful discussions about it.

\section*{2 Preliminaries}

Throughout $\mathfrak{g}$ will be a semisimple Lie algebra over $\mathbb{C}$, with a fixed Cartan subalgebra $\mathfrak{h}$. The inner automorphism group of $\mathfrak{g}$ will be denoted $G$.

\subsection*{2.1 The action of the Weyl group}

The Killing form on $\mathfrak{g}$ will be denoted $\kappa$; it is defined by $\kappa(x, y)=\operatorname{Tr}(\operatorname{ad} x \cdot \operatorname{ad} y)$. The form $\kappa$ is nondegenerate on $\mathfrak{g}$ and on $\mathfrak{h}$. Hence we can define a bijection $\mathfrak{h}^{*} \rightarrow \mathfrak{h}, \mu \mapsto \hat{\mu}$, by $\kappa(\hat{\mu}, h)=\mu(h)$, for $h \in \mathfrak{h}$. Then $(\mu, \lambda)=\kappa(\hat{\mu}, \hat{\lambda})$ defines a non-degenerate bilinear form on $\mathfrak{h}^{*}$. Also for $\mu \neq 0$ we set
$$\mu^{\vee}=\frac{2 \hat{\mu}}{(\mu, \mu)} .$$
For $\alpha \in \mathfrak{h}^{*}$ we set $\mathfrak{g}_{\alpha}=\{x \in \mathfrak{g} \mid[h, x]=\alpha(h) x$ for all $h \in \mathfrak{h}\}$. We let $\Phi$ be the set of all nonzero $\alpha \in \mathfrak{h}^{*}$ with $\mathfrak{g}_{\alpha} \neq 0$. Let $\mathfrak{h}_{\mathbb{R}}^{*}$ be the real vector space spanned by $\Phi$. Then ( , ) is an inner product in $\mathfrak{h}_{\mathbb{R}}^{*}$, and $\Phi$ is a (reduced) root system in $\mathfrak{h}_{\mathbb{R}}^{*}$.

For $\alpha, \beta \in \mathfrak{h}_{\mathbb{R}}^{*}$ we set
$$\left\langle\alpha, \beta^{\vee}\right\rangle=\frac{2(\alpha, \beta)}{(\beta, \beta)} .$$
For $\alpha \in \Phi$ we define the reflection $s_{\alpha}: \mathfrak{h}_{\mathbb{R}}^{*} \rightarrow \mathfrak{h}_{\mathbb{R}}^{*}$ by $s_{\alpha}(\mu)=\mu-\left\langle\mu, \alpha^{\vee}\right\rangle \alpha$. The group generated by all $s_{\alpha}$ for $\alpha \in \Phi$ is called the Weyl group, and denoted $W$.

Let $\mathfrak{h}_{\mathbb{R}}$ be the real vector space spanned by all $\alpha^{\vee}$, for $\alpha \in \Phi$. For $\alpha \in \Phi$ we define the linear map $s_{\alpha}: \mathfrak{h}_{\mathbb{R}} \rightarrow \mathfrak{h}_{\mathbb{R}}$ by $s_{\alpha}(h)=h-\alpha(h) h_{\alpha}$. Then $s_{\alpha}\left(\beta^{\vee}\right)=\beta^{\vee}-\left\langle\alpha, \beta^{\vee}\right\rangle \alpha^{\vee}$. A small calculation shows that the following diagram commutes
![](https://cdn.mathpix.com/cropped/02e940a3-1d8b-4e52-a1e5-ad4d829635a4-05.jpg?height=198&width=215&top_left_y=1838&top_left_x=939)

So, more generally, for $w \in W$ and $\mu \in \mathfrak{h}_{\mathbb{R}}^{*}$ we have $w \hat{\mu}=\widehat{w \mu}$. Also $W$ leaves the Killing form on $\mathfrak{h}_{\mathbb{R}}$ and on $\mathfrak{h}_{\mathbb{R}}^{*}$ invariant.

Let < be an order on $\mathfrak{h}_{\mathbb{R}}^{*}$ with
\begin{itemize}
\item[-] $u<v$ implies $u+w<v+w$ for all $w \in \mathfrak{h}_{\mathbb{R}}^{*}$,
\item[-] $u>0$ implies $\lambda u>0$ for all positive $\lambda \in \mathbb{R}$, and $\lambda u<0$ for all negative $\lambda \in \mathbb{R}$.
\end{itemize}
We call such a < a root-order. A root-order defines a partition $\Phi=\Phi^{+} \cup \Phi^{-}$of $\Phi$ into positive and negative roots, and a set $\Delta$ of simple roots. Conversely, if $\Delta$ is a set of simple
roots, then we can define an ordering as follows: express $u, v$ as linear combinations of the elements of $\Delta$, and set $u<v$ if the first nonzero coordinate of $v-u$ is positive. This order will then yield $\Delta$ as set of simple roots.

Let $C^{*} \subset \mathfrak{h}_{\mathbb{R}}^{*}$ be set of all $\mu$ with $\left\langle\mu, \alpha^{\vee}\right\rangle \geq 0$ for all $\alpha>0$. Then every $W$-orbit in $\mathfrak{h}_{\mathbb{R}}^{*}$ has a unique point in $C^{*}$. It is called the fundamental Weyl chamber of $\mathfrak{h}_{\mathbb{R}}^{*}$. Also we let $C \subset \mathfrak{h}_{\mathbb{R}}$ be the set of all $h$ with $\alpha(h) \geq 0$ for all $\alpha>0$. Again, every $W$-orbit in $\mathfrak{h}_{\mathbb{R}}$ has a unique point in $C$. It is called the fundamental Weyl chamber in $\mathfrak{h}_{\mathbb{R}}$.

\subsection*{2.2 Nilpotent orbits}

Let $e \in \mathfrak{g}$ be nilpotent; then the orbit $G \cdot e$ is called a nilpotent orbit. Here we recall some facts on the classification of nilpotent orbits from [1], [2].

Let $e \in \mathfrak{g}$ be nilpotent, then by the Jacobson-Morozov lemma there are $h, f \in \mathfrak{g}$ with $[h, e]=2 e,[h, f]=-2 f,[e, f]=h$. We say that ( $h, e, f$ ) is an $\mathfrak{s l}_{2}$-triple. Note that $G$ acts on $\mathfrak{s l}_{2}$-triples by $\sigma \cdot(h, e, f)=(\sigma \cdot h, \sigma \cdot e, \sigma \cdot f)$. Let $e, e^{\prime} \in \mathfrak{g}$ be nilpotent, lying in $\mathfrak{s l}_{2}$-triples $(h, e, f)$ and $\left(h^{\prime}, e^{\prime}, f^{\prime}\right)$. Then the following are equivalent:
\begin{itemize}
\item[-] $e, e^{\prime}$ lie in the same $G$-orbit,
\item[-] $(h, e, f)$ and $\left(h^{\prime}, e^{\prime}, f^{\prime}\right)$ lie in the same $G$-orbit,
\item[-] $h, h^{\prime}$ lie in the same $G$-orbit.
\end{itemize}
Let $(h, e, f)$ be an $\mathfrak{s l}_{2}$-triple in $\mathfrak{g}$. Then $h$ lies in a Cartan subalgebra of $\mathfrak{g}$. As all Cartan subalgebras of $\mathfrak{g}$ are $G$-conjugate, after possibly replacing the triple by a $G$-conjugate, we may assume that $h \in \mathfrak{h}$. Then $h \in \mathfrak{h}_{\mathbb{R}}$ (indeed: $\alpha(h) \in \mathbb{Z}$ for all $\alpha \in \Phi$ ). Two elements of $\mathfrak{h}_{\mathbb{R}}$ are $G$-conjugate if and only if they are $W$-conjugate (cf. [2] Theorem 2.2.4). Hence, after a further conjugation we may assume $h \in C$. In fact, this $h$ determines the nilpotent orbit uniquely; it is called the characteristic of the orbit.

We call an $h \in \mathfrak{h}$ admissible if it lies in an $\mathfrak{s l}_{2}$-triple $(h, e, f)$. Let $e_{1}, \ldots, e_{t}$ be representatives of the nilpotent $G$-orbits in $\mathfrak{g}$, lying in $\mathfrak{s l}_{2}$-triples $\left(h_{i}, e_{i}, f_{i}\right)$, with $h_{i} \in C$. Then
$$\mathcal{H}=\bigcup_{i=1}^{t} W \cdot h_{i}$$
is the set of all admissible elements in $\mathfrak{h}$.
We will often have the need to run through a $W$-orbit $W \cdot h_{i}$. For this Snow ([16], see also [7]) has devised an efficient algorithm, which makes it possible to run through the orbit and inspect each element without storing all of the orbit. This feature will be very important for us.

\subsection*{2.3 The Dynkin index}

Assume that $\mathfrak{g}$ is simple. It is well-known that upto multilication by nonzero scalars, there exists a unique nondegenerate symmetric $G$-invariant bilinear form on $\mathfrak{g}$. The Killing form is such a form.

Let $\tilde{\mathfrak{g}} \subset \mathfrak{g}$ be a simple subalgebra. Let $\widetilde{G}$ be the group of inner automorphisms of $\tilde{\mathfrak{g}}$. Then $\widetilde{G} \subset G$. Hence the Killing form $\kappa$ of $\mathfrak{g}$ induces a $\widetilde{G}$-invariant bilinear form on $\tilde{\mathfrak{g}}$. Let $\tilde{\kappa}$ denote the Killing form of $\tilde{\mathfrak{g}}$. So $\tilde{\kappa}(x, y)=\eta \kappa(x, y)$ for all $x, y \in \tilde{\mathfrak{g}}$, where $\eta$ is a nonzero scalar.

If we normalise $\kappa$ so that $\kappa\left(\alpha^{\vee}, \alpha^{\vee}\right)=2$ for the short roots $\alpha$, and do the same for $\tilde{\kappa}$, then $\eta$ is called the Dynkin index of $\tilde{\mathfrak{g}}$ in $\mathfrak{g}$. It is the same for all $G$-conjugates of $\tilde{\mathfrak{g}}$. However, it can also happen that nonconjugate subalgebras have the same Dynkin index.

Lemma 1 Let $\tilde{\mathfrak{g}} \subset \mathfrak{g}$ be a semisimple subalgebra that is the direct sum of simple ideals, $\tilde{\mathfrak{g}}=\tilde{\mathfrak{g}}_{1} \oplus \cdots \oplus \tilde{\mathfrak{g}}_{m}$. Then $\kappa\left(\tilde{\mathfrak{g}}_{i}, \tilde{\mathfrak{g}}_{j}\right)=0$ for $i \neq j$.

Proof. Let $x, y \in \mathfrak{g}_{i}$ and $z \in \mathfrak{g}_{j}$. Then $\kappa([x, y], z)=\kappa(x,[y, z])=0$. So since $\mathfrak{g}_{i}=\left[\mathfrak{g}_{i}, \mathfrak{g}_{i}\right]$ the result follows. \(\square\)

\subsection*{2.4 Canonical generators}

Let $\tilde{\mathfrak{g}}$ be a semisimple Lie algebra. Then $\tilde{\mathfrak{g}}$ has a canonical set of generators ([11], Chapter IV). That is a a set of elements $\tilde{x}_{1}, \ldots, \tilde{x}_{r}, \tilde{y}_{1}, \ldots, \tilde{y}_{r}, \tilde{h}_{1}, \ldots, \tilde{h}_{r}$ such that
$$\begin{aligned}
& {\left[\tilde{h}_{i}, \tilde{h}_{j}\right]=0} \\
& {\left[\tilde{x}_{i}, \tilde{y}_{j}\right]=\delta_{i j} \tilde{h}_{i}} \\
& {\left[\tilde{h}_{j}, \tilde{x}_{i}\right]=\widetilde{C}(i, j) \tilde{x}_{i}} \\
& {\left[\tilde{h}_{j}, \tilde{y}_{i}\right]=-\widetilde{C}(i, j) \tilde{y}_{i} .}
\end{aligned}$$
Here $\widetilde{C}$ is the Cartan matrix of the root system of $\tilde{\mathfrak{g}}$. We call the sequence $\left(\tilde{h}_{1}, \ldots, \tilde{h}_{r}\right)$ the $h$-part of the canonical generating set. We note that $\tilde{h}_{i}=\alpha_{i}^{\vee}$, where $\left\{\alpha_{1}, \ldots, \alpha_{r}\right\}$ is a set of simple roots of the root system of $\tilde{\mathfrak{g}}$.

Suppose now that $\tilde{h}_{i} \in \mathfrak{h}$. Then the $\tilde{h}_{i} \in \mathfrak{h}$ are admissible; hence lie in the set $\mathcal{H}$ of Section 2.2. In the sequel we will say that the $h$-part of a canonical generating set lies in $\mathfrak{h}$ to mean that all of its elements do. The next theorem is essentially the same as [5], Theorem 4.1.

Theorem 2 Let $\widetilde{C}$ be the Cartan matrix of a root system. Let $\tilde{x}_{i}, \tilde{y}_{i}, \tilde{h}_{i}$ be elements of a finite dimensional Lie algebra satisfying the relations (1). Then the subalgebra generated by these elements is semisimple, and its root system has Cartan matrix equal to $\widetilde{C}$.

Proof. For $i \neq j$ consider the element
$$y_{i, j}=\left(\operatorname{ad} \tilde{y}_{i}\right)^{-\widetilde{C}(j, i)+1}\left(\tilde{y}_{j}\right) .$$
A short calculation (cf. [7], Lemma 7.11.3) shows that $\left[\tilde{x}_{i}, y_{i, j}\right]=0$ and $\left[\tilde{h}_{i}, y_{i, j}\right]=(\widetilde{C}(j, i)-$ $2) y_{i, j}$. But $\widetilde{C}(j, i)-2<0$. It follows that $y_{i, j}$ generates a finite-dimensional irreducible
$\mathfrak{s l}_{2}$-module of negative highest weight. This is impossible, hence $y_{i, j}=0$. Similarly we have
$$\left(\operatorname{ad} \tilde{x}_{i}\right)^{-\widetilde{C}(j, i)+1}\left(\tilde{x}_{j}\right)=0 .$$
Hence the $\tilde{x}_{i}, \tilde{y}_{i}, \tilde{h}_{i}$ satisfy the Serre relations (see [15], Chapter VI, §4). This implies that the algebra they generate is a quotient of the semisimple Lie algebra $\mathfrak{u}$ corresponding to the Cartan matrix $\widetilde{C}$ by an ideal. This ideal is the sum of some of the simple ideals of $\mathfrak{u}$. But since the $\tilde{x}_{i}, \tilde{y}_{i}, \tilde{h}_{i}$ are nonzero, this ideal has to be zero. \(\square\)

\subsection*{2.5 Solving polynomial equations}

In order to construct the subalgebras that we are after, on some occasions we need to solve polynomial equations in several variables (see Section 4). For this no general algorithm exists, so we have to do it by hand. However, a computational tool that makes this a lot easier is provided by Gröbner bases.

Let $f_{1}, \ldots, f_{s} \in k\left[x_{1}, \ldots, x_{n}\right]$, where $k$ is a field, generate the ideal $I$. Then solving $f_{1}=\cdots=f_{s}=0$ is the same as solving $g=0$ for all $g \in \mathcal{G}$, where $\mathcal{G}$ is any other generating set of $I$. A Gröbner basis is, on many occasions, a particularly convenient generating set for this purpose. Especially if the Gröbner basis $\mathcal{G}$ is computed relative to a lexicographical ordering, then $\mathcal{G}$ has a triangular structure, which often makes solving the polynomial equations easier. Also, if there are no solutions over the algebraic closure of $k$, then the reduced Gröbner basis is $\{1\}$. So this situation is immediately detected. Here we do not go into the details, but refer to [3] for an in-depth discussion of Gröbner bases and polynomial system solving.

\subsection*{2.6 Outline of the method}

Here we summarise the method we use to classify semisimple subalgebras of $\mathfrak{g}$.
Let $\widetilde{C}$ be the $r \times r$ Cartan matrix of the root system of a semisimple Lie algebra. The objective is to classify the semisimple subalgebras of $\mathfrak{g}$ having a root system with Cartan matrix $\widetilde{C}$, up to linear equivalence. We assume that the semisimple subalgebras of $\mathfrak{g}$ of smaller rank have been classified. We note that the classification for rank 1 is known from the classification of the nilpotent orbits in $\mathfrak{g}$.

Let $\tilde{\mathfrak{g}} \subset \mathfrak{g}$ be a subalgebra with Cartan matrix $\widetilde{C}$, and canonical set of generators $\tilde{h}_{i}$, $\tilde{x}_{i}, \tilde{y}_{i}, 1 \leq i \leq r$, satisfying (1). Then the $\tilde{h}_{i}$ lie in a Cartan subalgebra of $\mathfrak{g}$. So since all Cartan subalgebras of $\mathfrak{g}$ are conjugate under $G$, we get that $\tilde{\mathfrak{g}}$ is equivalent, and hence linearly equivalent, to a subalgebra with a canonical generating set with the $h$-part lying in $\mathfrak{h}$. So we may assume that $\tilde{h}_{i} \in \mathfrak{h}$, and hence $\tilde{h}_{i} \in \mathcal{H}$.

In Section 5 we describe methods to assemble a set $H$ of $r$-tuples $\left(\tilde{h}_{1}, \ldots, \tilde{h}_{r}\right) \in \mathcal{H}^{r}$ such that all classes of linearly equivalent subalgebras with Cartan matrix $\widetilde{C}$ have a representative that has a canonical generating set with $h$-part in $H$. Here one of the objectives is to keep this set "small".

Let $\left(\tilde{h}_{1}, \ldots, \tilde{h}_{r}\right) \in H$. Section 4 contains methods that construct $\tilde{x}_{i}, \tilde{y}_{i}$ in $\mathfrak{g}$ satisfying (1), or decide that no such elements exist. In the former case we have found a semisimple subalgebra of $\mathfrak{g}$ with Cartan matrix $\widetilde{C}$ by Theorem 2. In the latter case the $\tilde{h}_{i}$ do not form the $h$-part of a canonical generating set of a subalgebra with Cartan matrix $\widetilde{C}$.

In Section 3 we describe a method for deciding whether two semisimple subalgebras are linearly equivalent. So we can get rid of any linearly equivalent pairs of subalgebras constructed in the previous step. In fact, linear equivalence depends only on the $h$-parts of the canonical generating sets; so we can construct the set $H$ so that no linearly equivalent subalgebras arise. This is important as constructing the subalgebras is one of the most difficult steps.

We used these methods for classifying the semisimple subalgebras of the simple Lie algebras of ranks up to 8. For classifying the semisimple subalgebras of the semisimple, but not simple, Lie algebras we have a separate method, described in Section 6. Finally the last section has the algorithm that we use for deciding inclusion.

\section*{3 Deciding linear equivalence}

The purpose of this section is to describe an algorithm for deciding whether two semisimple subalgebras of $\mathfrak{g}$ are linearly equivalent. For this we assume that they are given by canonical sets of generators, with the $h$-parts lying in $\mathfrak{h}$. First we prove a theorem that in essence is due to Dynkin ([5], Theorem 1.5). Here we show how Dynkin's argument can be adapted to prove the statement that we need (Corollary 5). For this the language of embeddings is more appropriate.

Let $\varphi: \tilde{\mathfrak{g}} \rightarrow \mathfrak{g}$ be an embedding of the semisimple Lie algebra $\tilde{\mathfrak{g}}$ into $\mathfrak{g}$. Let $\tilde{\mathfrak{h}}$ be a fixed Cartan subalgebra of $\tilde{\mathfrak{g}}$ and assume $\varphi(\tilde{\mathfrak{h}}) \subset \mathfrak{h}$. Let $\tilde{\mathfrak{h}}_{\mathbb{R}}^{*}, \mathfrak{h}_{\mathbb{R}}^{*}$ be the $\mathbb{R}$-span of the roots of $\tilde{\mathfrak{g}}$ and $\mathfrak{g}$ respectively. We define a map $\varphi^{*}: \mathfrak{h}_{\mathbb{R}}^{*} \rightarrow \tilde{\mathfrak{h}}_{\mathbb{R}}^{*}$ by $\varphi^{*}(\mu)(\tilde{h})=\mu(\varphi(\tilde{h}))$, where $\tilde{h} \in \tilde{\mathfrak{h}}_{\mathbb{R}}^{*}$.

Let $\rho: \mathfrak{g} \rightarrow \mathfrak{g} \mathfrak{l}(U)$ be a representation and let $\mu$ be a weight of $\rho$, with weight vector $v$. Then for $\tilde{h} \in \tilde{\mathfrak{h}}_{\mathbb{R}}^{*}$ we get $\rho(\varphi(\tilde{h})) v=\mu(\varphi(\tilde{h})) v=\varphi^{*}(\mu)(\tilde{h}) v$. It follows that $\varphi^{*}(\mu)$ is a weight of the representation $\rho \varphi$ of $\tilde{\mathfrak{g}}$. In particular, it lies in $\tilde{\mathfrak{h}}_{\mathbb{R}}^{*}$. Since the weights span the spaces $\tilde{\mathfrak{h}}_{\mathbb{R}}^{*}, \mathfrak{h}_{\mathbb{R}}^{*}$, it follows that $\varphi^{*}\left(\mathfrak{h}_{\mathbb{R}}^{*}\right)=\tilde{\mathfrak{h}}_{\mathbb{R}}^{*}$.

Lemma 3 Let the notation be as above. Fix a root-oder $\prec$ of $\tilde{\mathfrak{h}}_{\mathbb{R}}^{*}$. Fix also a division $\Phi=\Phi^{+} \cup \Phi^{-}$of the roots $\Phi$ of $\mathfrak{g}$ into positive and negative roots, corresponding to a root-order of $\mathfrak{h}_{\mathbb{R}}^{*}$. Let $\Delta \subset \Phi$ denote the corresponding set of simple roots. Then there exists a root-order $<$ of $\mathfrak{h}_{\mathbb{R}}^{*}$, and a $\sigma \in N_{G}(\mathfrak{h})$ with the following properties:
\begin{itemize}
\item[-] The set of positive roots with respect to < is also $\Phi^{+}$;
\item[-] for $\psi=\sigma \varphi$ we have that $\psi^{*}(\mu) \prec \psi^{*}(\lambda)$ implies $\mu<\lambda$,
\item[-] if $\psi^{*}(\mu) \neq \psi^{*}(\lambda)$ then $\mu<\lambda$ implies $\psi^{*}(\mu) \prec \psi^{*}(\lambda)$.
\end{itemize}

Proof. Let $<^{\prime}$ be any root-order on $\mathfrak{h}_{\mathbb{R}}^{*}$. Define the root-order $<^{\prime \prime}$ on $\mathfrak{h}_{\mathbb{R}}^{*}$ by $\mu<^{\prime \prime} \lambda$ if $\varphi^{*}(\mu) \prec \varphi^{*}(\lambda)$, or if those two are equal, $\mu<^{\prime} \lambda$. Let $\Delta^{\prime \prime}$ be the corresponding set of simple
roots. Then there is $w \in W$ with $w \Delta^{\prime \prime}=\Delta$. Let $\sigma \in N_{G}(\mathfrak{h})$ be such that the restriction of $\sigma$ to $\mathfrak{h}$ is $w$. Set $\psi=\sigma \varphi$, and define the root-order $<$ by: $\mu<\lambda$ if $w^{-1} \mu<^{\prime \prime} w^{-1} \lambda$.

Let $\alpha \in \Delta$, and write $\alpha=w \beta$ for some $\beta \in \Delta^{\prime \prime}$. Then $w^{-1} \alpha=\beta>^{\prime \prime} 0$. Hence $\alpha>0$; and therefore the set of positive roots with respect to $<$ is $\Phi^{+}$.

Next, using $\left(w^{-1} \mu\right)(h)=\mu(w h)$ for $h \in \mathfrak{h}$ we get $\psi^{*}(\mu)=\varphi^{*}\left(w^{-1} \mu\right)$. Hence $\psi^{*}(\mu) \prec$ $\psi^{*}(\lambda)$ is the same as $\varphi^{*}\left(w^{-1} \mu\right) \prec \varphi^{*}\left(w^{-1} \lambda\right)$. This implies that $w^{-1} \mu<^{\prime \prime} w^{-1} \lambda$, and hence $\mu<\lambda$. The last statement follows directly from the second. \(\square\)

Theorem 4 Let $\varphi_{1}, \varphi_{1}: \tilde{\mathfrak{g}} \rightarrow \mathfrak{g}$ be two embeddings of $\tilde{\mathfrak{g}}$ into $\mathfrak{g}$. Let $\tilde{x}_{i}, \tilde{y}_{i}, \tilde{h}_{i}$ for $1 \leq i \leq r$ form a canonical set of generators of $\tilde{\mathfrak{g}}$. Write $\tilde{x}_{i}^{1}, \tilde{y}_{i}^{1}, \tilde{h}_{i}^{1}$ and $\tilde{x}_{i}^{2}, \tilde{y}_{i}^{2}, \tilde{h}_{i}^{2}$ for their images under $\varphi_{1}, \varphi_{2}$ respectively. Assume that $\tilde{h}_{i}^{1}, \tilde{h}_{i}^{2} \in \mathfrak{h}$. Then $\varphi_{1}$ and $\varphi_{2}$ are linearly equivalent if and only if there is a $w \in W$ with $w\left(\tilde{h}_{i}^{1}\right)=\tilde{h}_{i}^{2}$ for $1 \leq i \leq r$.

Proof. First suppose that $w \in W$ exists. Let $\rho: \mathfrak{g} \rightarrow \mathfrak{g} \mathfrak{l}(U)$ be a representation of $\mathfrak{g}$. Let $\mu \in \mathfrak{h}_{\mathbb{R}}^{*}$ be a weight of $\rho$, i.e., there are nonzero $u \in U$ with $\rho(h) u=\mu(h) u$ for all $h \in \mathfrak{h}$. Set $\rho_{i}=\rho \varphi_{i}$ for $i=1,2$. Then $\rho_{i}$ is a representation of $\tilde{\mathfrak{g}}$. Observe that $\mu\left(\tilde{h}_{i}^{1}\right)=\kappa\left(\hat{\mu}, \tilde{h}_{i}^{1}\right)=\kappa\left(w \hat{\mu}, w\left(\tilde{h}_{i}^{1}\right)\right)=\kappa\left(\widehat{w \mu}, w\left(\tilde{h}_{i}^{1}\right)\right)=(w \mu)\left(w\left(\tilde{h}_{i}^{1}\right)\right)$. But also $w \mu$ is a weight of $\rho$, with the same multiplicity. Hence it follows that $\rho_{1}$ and $\rho_{2}$ have the same weights with the same multiplicities. Hence $\varphi_{1}, \varphi_{2}$ are linearly equivalent.

Now assume that $\varphi_{1}, \varphi_{2}$ are linearly equivalent. By Lemma 3 there are $\sigma_{1}, \sigma_{2} \in N_{G}(\mathfrak{h})$ such that $\psi_{i}=\sigma_{i} \varphi_{i}$ have the properties stated in Lemma 3 for $\psi$.

Let $\rho: \mathfrak{g} \rightarrow \mathfrak{g} \mathfrak{l}(U)$ be an irreducible representation with highest weight $\lambda$. Set $\rho_{i}=\rho \circ \psi_{i}$. Then from Lemma 3 it follows that $\psi_{i}^{*}(\lambda)$ is the largest weight of $\rho_{i}$ in the ordering $\prec$. As the $\psi_{i}$ are linearly equivalent it follows that $\psi_{1}^{*}(\lambda)=\psi_{2}^{*}(\lambda)$. This is the same as $\lambda\left(\psi_{1}(\tilde{h})\right)=\lambda\left(\psi_{2}(\tilde{h})\right)$ for all $\tilde{h} \in \tilde{\mathfrak{h}}$. Now since $\mathfrak{h}_{\mathbb{R}}^{*}$ is spanned by dominant weights, this equality follows for all $\lambda \in \mathfrak{h}_{\mathbb{R}}^{*}$. Hence $\psi_{1}(\tilde{h})=\psi_{2}(\tilde{h})$ for all $\tilde{h} \in \tilde{\mathfrak{h}}$. In particular, this is true for the $\tilde{h}_{i}$. So $\sigma_{1}\left(\varphi_{1}\left(\tilde{h}_{i}\right)\right)=\sigma_{2}\left(\varphi_{2}\left(\tilde{h}_{i}\right)\right)$. Now let $w_{i} \in W$ be such that $\left.\sigma_{i}\right|_{\mathfrak{h}}=w_{i}$. Then we get the statement of the theorem with $w=w_{2}^{-1} w_{1}$. \(\square\)

Corollary 5 Let $\tilde{\mathfrak{g}}_{1}, \tilde{\mathfrak{g}}_{2}$ be two semisimple subalgebras of $\mathfrak{g}$, both isomorphic to $\tilde{\mathfrak{g}}$. Let $\tilde{h}_{1}^{1}, \ldots, \tilde{h}_{r}^{1}, \tilde{h}_{1}^{2}, \ldots, \tilde{h}_{r}^{2}$, be the $h$-parts of canonical sets of generators of $\tilde{\mathfrak{g}}_{1}$ and $\tilde{\mathfrak{g}}_{2}$ respectively. Assume that $\tilde{h}_{i}^{k} \in \mathfrak{h}$ for all $i, k$. Then $\tilde{\mathfrak{g}}_{1}, \tilde{\mathfrak{g}}_{2}$ are linearly equivalent if and only if there is $a w \in W$ with
$$\left\{w\left(\tilde{h}_{i}^{1}\right) \mid 1 \leq i \leq r\right\}=\left\{\tilde{h}_{i}^{2} \mid 1 \leq i \leq r\right\} .$$

Proof. The "if"-part follows immediately from Theorem 4. For the "only if"-part suppose that $\tilde{\mathfrak{g}}_{1}, \tilde{\mathfrak{g}}_{2}$ are linearly equivalent. Let $\rho: \mathfrak{g} \rightarrow \mathfrak{g} \mathfrak{l}(U)$ be a faithful representation. Then there is $a \in \mathrm{GL}(U)$ with $a \rho\left(\tilde{\mathfrak{g}}_{1}\right) a^{-1}=\rho\left(\tilde{\mathfrak{g}}_{2}\right)$. Set $\tilde{h}_{i}^{3}=\rho^{-1}\left(a \rho\left(\tilde{h}_{i}^{1}\right) a^{-1}\right) \in \tilde{\mathfrak{g}}_{2}$. Let $\widetilde{G}_{2} \subset G$ be the inner automorphism group of $\tilde{\mathfrak{g}}_{2}$. Let $\tilde{\mathfrak{h}}_{2}^{2}, \tilde{\mathfrak{h}}_{2}^{3}$ denote the subspaces of $\tilde{\mathfrak{g}}_{2}$ spanned respectively by the $\tilde{h}_{i}^{2}$ and the $\tilde{h}_{i}^{3}$. These are Cartan subalgebras of $\tilde{\mathfrak{g}}_{2}$ so there is a $\sigma \in \widetilde{G}_{2}$ with $\sigma\left(\tilde{\mathfrak{h}}_{2}^{3}\right)=\tilde{\mathfrak{h}}_{2}^{2}$. Set $\tilde{h}_{i}^{4}=\sigma\left(\tilde{h}_{i}^{3}\right)$. Then also the $\tilde{h}_{i}^{4}$ form the $h$-part of a canonical set of generators of $\tilde{\mathfrak{g}}_{2}$, lying in the same Cartan subalgebra of $\tilde{\mathfrak{g}}_{2}$ as the $\tilde{h}_{i}^{2}$. Let $W_{2}$ denote the Weyl group of $\tilde{\mathfrak{g}}_{2}$ with respect to $\tilde{\mathfrak{h}}_{2}$. Since different sets of simple roots of $\tilde{\mathfrak{g}}_{2}$ are conjugate under $W_{2}$, there is a $u \in W_{2}$ such that $\left\{u\left(\tilde{h}_{i}^{4}\right)\right\}=\left\{\tilde{h}_{i}^{2}\right\}$. Let $\tau \in \widetilde{G}_{2}$ be such
that $\tau$ restricted to $\tilde{\mathfrak{h}}_{2}$ is $u$. Let $\tilde{h}_{1}, \ldots, \tilde{h}_{r}$ form the $h$-part of a canonical generating set of $\tilde{\mathfrak{g}}$. Let $\varphi_{1}: \tilde{\mathfrak{g}} \rightarrow \tilde{\mathfrak{g}}_{1}$ be the isomorphism sending $\tilde{h}_{i}$ to $\tilde{h}_{i}^{1}$. Set $\varphi_{2}=\tau \sigma \varphi_{1}$. Then $\varphi_{2}$ is linearly equivalent to $\varphi_{1}$. Moreover, $\left\{\varphi_{2}\left(\tilde{h}_{i}\right)\right\}=\left\{\tilde{h}_{i}^{2}\right\}$. Now we get the required $w \in W$ from Theorem 4. \(\square\)

So we can decide linear equivalence if we can decide whether two sets of elements, $\left\{h_{1}^{1}, \ldots, h_{r}^{1}\right\}$ and $\left\{h_{1}^{2}, \ldots, h_{r}^{2}\right\}$ of $\mathfrak{h}_{\mathbb{R}}$ are conjugate under $W$. Since $W$ preserves the Killing form we assume that the ordering is such that $\kappa\left(h_{i}^{1}, h_{j}^{1}\right)=\kappa\left(h_{i}^{2}, h_{j}^{2}\right)$ for $1 \leq i, j \leq r$.

We fix a set of positive roots $\Phi^{+}$and corresponding set of simple roots $\left\{\alpha_{1}, \ldots, \alpha_{l}\right\}$. Then the reflections $s_{\alpha_{i}}$ generate $W$.

From Section 2.1 we recall that $C \subset \mathfrak{h}_{\mathbb{R}}$ is the set of all $h$ with $\alpha(h) \geq 0$ for all $\alpha>0$. We note that for a given $h \in \mathfrak{h}_{\mathbb{R}}$ it is straightforward to find its unique $W$-conjugate lying in $C$. Indeed, initially we set $h_{0}=h$. Let $i \geq 0$ and suppose that $h_{i}$ is found. If $h_{i} \in C$ then we are done. Otherwise there is $\alpha_{j}$ with $\alpha_{j}\left(h_{i}\right)<0$. Then set $h_{i+1}=s_{\alpha_{j}}\left(h_{i}\right)$. Note that for $i<j$ we have $h_{j}-h_{i}=\sum_{k=1}^{l} a_{k} \alpha_{k}$ with $a_{k} \in \mathbb{R}$ non-negative, and at least one coefficient $a_{k}$ is positive. Hence all $h_{i}$ are different, and as $W$ is finite the sequence of the $h_{i}$ must land in $C$. From this we also immediately get a $w \in W$ with $w(h) \in C$.

Next we have a method for deciding whether there is a $w \in W$ with $w\left(h_{i}^{1}\right)=h_{i}^{2}$. We first compute $w_{1}, w_{2} \in W$ with $w_{i}\left(h_{1}^{i}\right) \in C$. If those are not equal, then the required $w$ does not exist. Otherwise set $u=w_{2}^{-1} w_{1}$; then $u\left(h_{1}^{1}\right)=h_{1}^{2}$. Now the set of all $v \in W$ sending $h_{1}^{1}$ to $h_{1}^{2}$ is exactly $\operatorname{Stab}_{W}\left(h_{1}^{2}\right) u$, where $\operatorname{Stab}_{W}\left(h_{1}^{2}\right)$ denotes the stabiliser of $h_{1}^{2}$ in $W$.

Set $h=w_{2}\left(h_{1}^{2}\right)$. Let $I$ be the set of all $i$ with $\alpha_{i}(h)=0$. It is known (cf. [9], Theorem 1.12) that $\operatorname{Stab}_{W}(h)$ is generated by the $s_{\alpha_{i}}$ with $i \in I$. Now $\operatorname{Stab}_{W}\left(h_{1}^{2}\right)=w_{2}^{-1} \operatorname{Stab}_{W}(h) w_{2}$. This implies that $\operatorname{Stab}_{W}\left(h_{1}^{2}\right)$ is generated by the reflections $s_{w_{2}^{-1}\left(\alpha_{i}\right)}$, where $i \in I$. The roots $w_{2}^{-1}\left(\alpha_{i}\right)$ for $i \in I$ form a simple system of a root subsystem of $\Phi$, of which $\operatorname{Stab}_{W}\left(h_{1}^{2}\right)$ is the Weyl group.

Now set $h_{i}^{3}=u\left(h_{i}^{1}\right)$ for $1 \leq i \leq r$. We decide if there is $v \in \operatorname{Stab}_{W}\left(h_{1}^{2}\right)$ such that $v\left(h_{i}^{3}\right)=h_{i}^{2}$ for $2 \leq i \leq r$. We can do this as the sequence is shorter. If such a $v$ exists, also the required $w$ (which is $v u$ ) exists. In the other case it does not.

Finally, in order to decide whether there is a $w \in W$ with $\left\{w\left(h_{i}^{1}\right)\right\}=\left\{h_{i}^{2}\right\}$ we loop over all permutations $\pi$ of $\{1, \ldots, r\}$ with $\kappa\left(h_{\pi(i)}^{1}, h_{\pi(j)}^{1}\right)=\kappa\left(h_{i}^{1}, h_{j}^{1}\right)$ for $1 \leq i, j \leq r$. For each such $\pi$ we decide whether there is a $w \in W$ with $w\left(h_{\pi(i)}^{1}\right)=h_{i}^{2}$. Once we find one we stop. Remark. This procedure works well in partice if the number of permutations as above is small. This very often is the case. The main exception being the case where ( $h_{1}^{1}, \ldots, h_{r}^{1}$ ) is the $h$-part of a canonical generating set of a Lie algebra of type $k A_{1}$. In situations like that the algorithm has to work a lot harder, as up to $k$ ! permutations have to be tried. Fortunately, for the simple Lie algebras of ranks $\leq 8$ there are not many subalgebras of such a type with large $k$.

Remark. If a class of linearly equivalent subalgebras splits into more than one class of equivalent subalgebras, then each of the latter classes has a representative having a canonical generating set with $h$-part that is the same for each of them. Only the other generators
$\tilde{x}_{i}, \tilde{y}_{i}$ differ.

\section*{4 Constructing a subalgebra}

In this section we describe algorithms for constructing a canonical generating set of a semisimple subalgebra of $\mathfrak{g}$, given its Cartan matrix and $h$-part.

Let $\tilde{\mathfrak{h}}$ be a subalgebra of $\mathfrak{h}$. For $\mu \in \tilde{\mathfrak{h}}^{*}$ we set
$$\mathfrak{g}(\mu)=\{x \in \mathfrak{g} \mid[\tilde{h}, x]=\mu(\tilde{h}) x \text { for all } \tilde{h} \in \tilde{\mathfrak{h}}\} .$$
Then $\mathfrak{g}$ is the direct sum of the various $\mathfrak{g}(\mu)$.
Lemma 6 Let $\mu \in \tilde{\mathfrak{h}}^{*}$ be such that $\mathfrak{g}(\mu) \neq 0$ and such that there is a $h \in \tilde{\mathfrak{h}}$ with $\mu(h)=2$. Set
$$\begin{aligned}
\mathcal{O}_{\mu} & =\{u \in \mathfrak{g}(\mu) \mid[\mathfrak{g}(0), u]=\mathfrak{g}(\mu)\}, \\
E_{\mu} & =\left\{e \in \mathfrak{g}(\mu) \mid \exists f \in \mathfrak{g}(-\mu) \text { with }(h, e, f) \text { is an } \mathfrak{s l}_{2} \text {-triple }\right\} .
\end{aligned}$$
Let $G_{0}$ be the connected subgroup of $G$ with Lie algebra $\mathfrak{g}(0)$. Then $G_{0}$ has a dense orbit in $\mathfrak{g}(\mu)$, which is equal to $\mathcal{O}_{\mu}$. If $E_{\mu}$ is nonempty then $E_{\mu}=\mathcal{O}_{\mu}$.

Proof. By standard arguments it is proved that $\kappa$ is non-degenerate on $\mathfrak{g}(-\mu) \oplus \mathfrak{g}(\mu)$, and on $\mathfrak{g}(0)$. Hence
$$\mathfrak{a}=\bigoplus_{k \in \mathbb{Z}} \mathfrak{g}(k \mu)$$
is a reductive $\mathbb{Z}$-graded Lie algebra. In [17] it is shown that $\mathfrak{g}(\mu)$ has a dense $G_{0}$-orbit. It is clear that a $u \in \mathfrak{g}(\mu)$ lies in this dense orbit if and only if it lies in $\mathcal{O}_{\mu}$.

Suppose that $E_{\mu}$ is not empty, and let $e \in E_{\mu}$. Then from $\mathfrak{s l}_{2}$-representation theory it follows that ad $e: \mathfrak{g}(0) \rightarrow \mathfrak{g}(\mu)$ is surjective. In other words, $[\mathfrak{g}(0), e]=\mathfrak{g}(\mu)$. Hence the $G_{0}$-orbit of $e$ is dense in $\mathfrak{g}(\mu)$. So this last orbit coincides with $\mathcal{O}_{\mu}$. But then also $E=\mathcal{O}_{\mu}$. \(\square\)

Let $\widetilde{C}$ be the Cartan matrix of the root system of a semisimple Lie algebra. Let $\tilde{h}_{1}, \ldots, \tilde{h}_{r} \in \mathfrak{h}$. We want to find $\tilde{x}_{i}, \tilde{y}_{i} \in \mathfrak{g}$ satisfying the relations (1), or decide that no such elements exist. We assume that $\tilde{h}_{i} \in \mathcal{H}$, as otherwise the required $x_{i}, y_{i}$ certainly do not exist. The space spanned by $\tilde{h}_{1}, \ldots, \tilde{h}_{r}$ will be denoted $\tilde{\mathfrak{h}}$.

First of all, let $\mu_{i} \in \tilde{\mathfrak{h}}^{*}$ be defined by $\mu_{i}\left(\tilde{h}_{j}\right)=\widetilde{C}(i, j)$. We compute bases of $\mathfrak{g}\left(\mu_{i}\right)$ and $\mathfrak{g}\left(-\mu_{i}\right)$, and of $\mathfrak{g}(0)$, which is the centralizer of $\tilde{\mathfrak{h}}$. The $\tilde{x}_{i}, \tilde{y}_{i}$, if they exist, lie in $\mathfrak{g}\left(\mu_{i}\right)$, $\mathfrak{g}\left(-\mu_{i}\right)$ respectively.

In the second step we find $\tilde{x}_{1} \in \mathfrak{g}\left(\mu_{1}\right), \tilde{y}_{1} \in \mathfrak{g}\left(-\mu_{1}\right)$ such that $\left(\tilde{h}_{1}, \tilde{x}_{1}, \tilde{y}_{1}\right)$ is an $\mathfrak{s} \mathfrak{l}_{2}$-triple. For this we use Lemma 6. After trying a few random elements we find an $\tilde{x}_{1} \in \mathfrak{g}\left(\mu_{1}\right)$ with $\left[\mathfrak{g}(0), \tilde{x}_{1}\right]=\mathfrak{g}\left(\mu_{1}\right)$, i.e., such that $\tilde{x}_{1}$ lies in $\mathcal{O}_{\mu_{1}}$. By solving a set of linear equations we either find $\tilde{y}_{1} \in \mathfrak{g}\left(-\mu_{1}\right)$ such that $\left(\tilde{h}_{1}, \tilde{x}_{1}, \tilde{y}_{1}\right)$ is an $\mathfrak{s l}_{2}$-triple, or we decide that that no such
$\tilde{y}_{1}$ exists. In the latter case there is no $\mathfrak{s} \mathfrak{l}_{2}$-triple $\left(\tilde{h}_{1}, \tilde{x}_{1}, \tilde{y}_{1}\right)$ with $\tilde{x}_{1} \in \mathfrak{g}\left(\mu_{1}\right), \tilde{y}_{1} \in \mathfrak{g}\left(-\mu_{1}\right)$. Indeed, in that case the set $E_{\mu_{1}}$ (notation as in Lemma 6) is empty. So in the latter case we stop with the conclusion that the $\tilde{x}_{i}, \tilde{y}_{i}$ do not exist. In the former case we continue.

In this second step we choose a random element $\tilde{x}_{1}$. We do stress that for the existence of the subsequent elements $\tilde{x}_{i}, \tilde{y}_{i}$, for $i>1$ it does not matter which $\tilde{x}_{1}$ is chosen, as long as $\left[\mathfrak{g}(0), \tilde{x}_{1}\right]=\mathfrak{g}\left(\mu_{1}\right)$. Indeed: all elements with that property are conjugate under $G(0)$ as they lie in the same dense orbit.

Now we continue to find the remaining $\tilde{x}_{i}, \tilde{y}_{i}$. For this we use two methods, which we call the linear method and the polynomial method.

For the linear method we suppose that $\tilde{x}_{i}, \tilde{y}_{i}, 1 \leq i \leq s$, for a certain $s$ with $1<s<r$, have been found, satisfying (1). We also assume that all different such sets are $G$-conjugate. In other words, if $\tilde{x}_{i}^{\prime}, \tilde{y}_{i}^{\prime}$ for $1 \leq i \leq s$ also satisfy (1), then there exists $\sigma \in G$ with $\sigma\left(\tilde{x}_{i}^{\prime}\right)=\tilde{x}_{i}$, $\sigma\left(\tilde{y}_{i}^{\prime}\right)=\tilde{y}_{i}, \sigma\left(\tilde{h}_{i}\right)=h_{i}$. Note that by the above construction this is certainly true for $s=1$.

Set
$$\begin{aligned}
\mathfrak{g}^{\prime}\left(\mu_{s+1}\right) & =\left\{u \in \mathfrak{g}\left(\mu_{s+1}\right) \mid\left[u, \tilde{y}_{i}\right]=0 \text { for } 1 \leq i \leq s\right\}, \\
\mathfrak{g}^{\prime}\left(-\mu_{s+1}\right) & =\left\{u \in \mathfrak{g}\left(-\mu_{s+1}\right) \mid\left[u, \tilde{x}_{i}\right]=0 \text { for } 1 \leq i \leq s\right\} .
\end{aligned}$$
Then $\tilde{x}_{s+1} \in \mathfrak{g}^{\prime}\left(\mu_{s+1}\right), \tilde{y}_{s+1} \in \mathfrak{g}^{\prime}\left(\mu_{s+1}\right)$. Let also $\mathfrak{g}^{\prime}(0)$ be the intersection of $\mathfrak{g}(0)$ and the centralizer of all $\tilde{x}_{i}, 1 \leq i \leq s$. By $\mathfrak{s l}_{2}$-representation theory it follows that $\mathfrak{g}^{\prime}(0)$ centralises also all $\tilde{y}_{i}, 1 \leq i \leq s$. Hence $\mathfrak{g}^{\prime}(0)$ acts on $\mathfrak{g}^{\prime}\left(\mu_{s+1}\right)$. Let $G_{0}^{\prime}$ be the connected subgroup of $G$ with Lie algebra $\mathfrak{g}^{\prime}(0)$. There are now two cases that can occur.

In the first case, after trying a few random elements, we find a $\tilde{x}_{s+1} \in \mathfrak{g}^{\prime}\left(\mu_{s+1}\right)$ with $\left[\mathfrak{g}^{\prime}(0), \tilde{x}_{s+1}\right]=\mathfrak{g}^{\prime}\left(\mu_{s+1}\right)$. This means that $G_{0}^{\prime}$ has a dense orbit in $\mathfrak{g}^{\prime}\left(\mu_{s+1}\right)$. By solving a set of linear equations we either find $\tilde{y}_{s+1} \in \mathfrak{g}^{\prime}\left(\mu_{s+1}\right)$ such that $\left(\hbar_{s+1}, \tilde{x}_{s+1}, \tilde{y}_{s+1}\right)$ is an $\mathfrak{s l}_{2}$-triple, or that no such $\tilde{y}_{s+1}$ exists. In the former case we say that the linear method has successfully found $\tilde{x}_{s+1}, \tilde{y}_{s+1}$. Note that this also implies that all sets of $\tilde{x}_{i}, \tilde{y}_{i}$ for $1 \leq i \leq s+1$ are $G$-conjugate. In the latter case we say that the linear method has broken down at step $s+1$.

The second case occurs when, after trying a few random elements, we do not find an $\tilde{x}_{s+1}$ as above. In this case we also say that the linear method has broken down at step $s+1$.

After having found $\tilde{x}_{1}, \tilde{y}_{1}$ we repeat the linear method. If it does not break down then in the end we find a complete set of $\tilde{x}_{i}, \tilde{y}_{i}$. If it breaks down at step $s+1$, then we use the polynomial method.

So for the polynomial method we also assume that $\tilde{x}_{i}, \tilde{y}_{i}$, for $1 \leq i \leq s$, have been found, satisfying the relations (1). For $s+1 \leq k \leq r$ we compute bases of the spaces
$$\begin{aligned}
\mathfrak{g}^{\prime}\left(\mu_{k}\right) & =\left\{u \in \mathfrak{g}\left(\mu_{k}\right) \mid\left[u, \tilde{y}_{i}\right]=0 \text { for } 1 \leq i \leq s\right\}, \\
\mathfrak{g}^{\prime}\left(-\mu_{k}\right) & =\left\{u \in \mathfrak{g}\left(\mu_{k}\right) \mid\left[u, \tilde{x}_{i}\right]=0 \text { for } 1 \leq i \leq s\right\} .
\end{aligned}$$
We express the $\tilde{x}_{i}, \tilde{y}_{i}$ for $s+1 \leq i \leq r$ as linear combinations of the bases of, respectively, $\mathfrak{g}^{\prime}\left(\mu_{k}\right)$ and $\mathfrak{g}^{\prime}\left(-\mu_{k}\right)$, with indeterminates as coefficients. Then the $\tilde{x}_{i}, \tilde{y}_{i}$ satisfy (1) if and only if certain polynomial equations in the coefficients are satisfied. We compute the
polynomial equations, and by Gröbner basis techniques (see Section 2.5), we either solve them, or decide that no solution exists.
Remark. Note that the linear method is heuristic in nature. However, it is automatic: if it succeeds then no further intervention is necessary to construct the subalgebra. We note also that there are situations where the linear method must break down as there are subalgebras that are only defined over an algebraic extension of $\mathbb{Q}$. In this case using the polynomial method is necessary. However, this last method is not entirely automatic (cf. Section 2.5).

Remark. In the next section we give methods to construct a suitable set of candidates $\left(\tilde{h}_{1}, \ldots, \tilde{h}_{r}\right)$ for the $h$-parts of canonical generating sets of semisimple subalgebras. This construction is such that $\left(\tilde{h}_{1}, \ldots, \tilde{h}_{r-1}\right)$ will be the $h$-part of a canonical generating set of a subalgebra of rank $r-1$. However, the $\tilde{x}_{i}, \tilde{y}_{i}$ for $1 \leq i \leq r-1$ do not necessarily lie in the bigger subalgebra, as in the two cases (the algebra of rank $r-1$ and of rank $r$ ) the spaces $\mathfrak{g}\left(\mu_{i}\right)$ are quite different.

\section*{5 Finding candidates}

In this section we deal with the problem of finding a suitable set of candidates for the $h$ parts of canonical generating sets of semisimple subalgebras of $\mathfrak{g}$, with given Cartan matrix $C$. For this we first consider a problem involving characters, whose solution will help us in making the set of candidates smaller.

Let $\tilde{\mathfrak{g}}$ be a semisimple Lie algebra with canonical generators $\tilde{x}_{i}, \tilde{y}_{i}, \tilde{h}_{i}, 1 \leq i \leq r$ satisfying (1). Let $V$ be a finite-dimensional $\tilde{\mathfrak{g}}$-module. Then $V$ is spanned by common eigenvectors of the $\tilde{h}_{i}$. Moreover, the eigenvalues of the $\tilde{h}_{i}$ are integers. For an $e=$ $\left(e_{1}, \ldots, e_{r}\right) \in \mathbb{Z}^{r}$ we set
$$V_{e}=\left\{v \in V \mid \tilde{h}_{i} \cdot v=e_{i} v \text { for } 1 \leq i \leq r\right\} .$$
Let $x_{1}, \ldots, x_{r}$ be indeterminates and write $x^{e}=x_{1}^{e_{1}} \cdots x_{r}^{e_{r}}$. Then the polynomial
$$\sum_{e \in \mathbb{Z}^{r}}\left(\operatorname{dim} V_{e}\right) x^{e}$$
is called the character of the $\tilde{\mathfrak{g}}$-module $V$.
Now fix $i$ with $1 \leq i \leq r$. For $m \in \mathbb{Z}$ we set $V_{m}^{i}=\left\{v \in V \mid \tilde{h}_{i} \cdot v=m v\right\}$, and define the polynomial
$$f_{i}\left(x_{i}\right)=\sum_{m \in \mathbb{Z}}\left(\operatorname{dim} V_{m}^{i}\right) x_{i}^{m} .$$
We call the polynomial $f_{1}+\cdots+f_{r}$ the character-puzzle of $V$. It is clear that from the character of $V$ we can compute its character-puzzle. More generally we say that a
polynomial of the form $f_{1}\left(x_{1}\right)+\cdots+f_{r}\left(x_{r}\right)$ is a character-puzzle. It is clear that a characterpuzzle does not necessarily correspond to a character. If it does we say that it is solvable. Here we consider the following problem: given a character-puzzle $f=f_{1}\left(x_{1}\right)+\cdots+f_{r}\left(x_{r}\right)$ decide whether it is solvable.

For this we proceed as follows. First we note that $V$ is a direct sum of simple modules, determined by a highest weight, which is an $e=\left(e_{1}, \ldots, e_{r}\right)$ with $e_{i} \geq 0$. From the character-puzzle we retrieve all non-negative eigenvalues of the $\tilde{h}_{i}$. This gives a finite number of possibilities for the highest weight of a simple constituent of $V$. For each possible highest weight we compute the character of the corresponding highest weight module (cf. [7]), and from that its character-puzzle $g$. Then we subtract, $h=f-g$. Then recursively we establish whether $h$ is solvable.

If at least one $h$ that we so obtain is solvable then $f$ itself is solvable. Otherwise it is not.

Let $\widetilde{C}$ be the Cartan matrix of (the root system of) a semisimple Lie algebra $\tilde{\mathfrak{g}}$ of rank $r$. In this section we describe how we find a set $H$ of $r$-tuples $\left(\tilde{h}_{1}, \ldots, \tilde{h}_{r}\right) \in \mathcal{H}^{r}$ such that every semisimple subalgebra of $\mathfrak{g}$ isomorphic to $\tilde{\mathfrak{g}}$ is linearly equivalent to a subalgebra with canonical set of generators $\tilde{x}_{i}, \tilde{y}_{i}, \tilde{h}_{i}$ with $\left(\tilde{h}_{1}, \ldots, \tilde{h}_{r}\right) \in H$. We also want the set to be "small" (whatever that means). So, although the set $\mathcal{H}^{r}$ would be a solution to the problem, it is far too big. (For example, if $\mathfrak{g}$ is of type $E_{8}$ then it has $2611951200^{r}$ elements.)

A first reduction is given by Corollary 5: if there are two $r$-tuples $\left(\tilde{h}_{1}, \ldots, \tilde{h}_{r}\right),\left(\tilde{h}_{1}^{\prime}, \ldots, \tilde{h}_{r}^{\prime}\right)$ such that there is a $w \in W$ with $w\left\{\tilde{h}_{i}\right\}=\left\{\tilde{h}_{i}^{\prime}\right\}$, then we can discard one of them.

Secondly, let $\widetilde{C}_{0}$ be the $(r-1) \times(r-1)$-matrix in the top left corner of $\widetilde{C}$. Then we may assume that we know a set $H_{0}$ of $(r-1)$-tuples $\left(\tilde{h}_{1}, \ldots, \tilde{h}_{r-1}\right) \in \mathcal{H}^{r-1}$ such that every semisimple subalgebra of $\mathfrak{g}$ with Cartan matrix $\widetilde{C}_{0}$ is linearly equivalent to exactly one subalgebra with canonical set of generators $\tilde{x}_{i}, \tilde{y}_{i}, \tilde{h}_{i}, 1 \leq i \leq r-1$, with $\left(\tilde{h}_{1}, \ldots, \tilde{h}_{r-1}\right) \in$ $H_{0}$.

Therefore we only put $r$-tuples $\left(\tilde{h}_{1}, \ldots, \tilde{h}_{r}\right)$ into the set $H$ that have $\left(\tilde{h}_{1}, \ldots, \tilde{h}_{r-1}\right) \in H_{0}$. Note that for $r=2$ we know the set $H_{0}$ from the classification of the nilpotent orbits in $\mathfrak{g}$.

So let $\left(\tilde{h}_{1}, \ldots, \tilde{h}_{r-1}\right) \in H_{0}$. We want to extend this $(r-1)$-tuple with an $\tilde{h}_{r}$. If we just take any $\tilde{h}_{r} \in \mathcal{H}$, then the set $H$ gets too big. So we perform further reductions. For this we distinguish two cases.

In the first case, in the Dynkin diagram of $\widetilde{C}$, the node labeled $r$ is not isolated. So it is connected with 1, 2, or 3 bonds to a simple component $\Gamma_{0}$ of the Dynkin diagram of $\widetilde{C}_{0}$. Let $\Gamma$ be the simple component of the Dynkin diagram of $C$, containing $\Gamma_{0}$. Let $i_{1}, \ldots, i_{s}$ be the labels of $\Gamma$, where $i_{s}=r$. Let $\hat{\mathfrak{g}}$ be a simple Lie algebra with Dynkin diagram $\Gamma$, set of canonical generators $\hat{x}_{i}, \hat{y}_{i}, \hat{h}_{i}$, for $1 \leq i \leq s$, and Killing form $\hat{\kappa}$. As seen in Section 2.3 the matrix $\left(\kappa\left(\tilde{h}_{i_{k}}, \tilde{h}_{i_{l}}\right)\right)$ is a scalar multiple of the matrix $\widehat{B}=\left(\hat{\kappa}\left(\hat{h}_{i}, \hat{h}_{j}\right)\right)$. Furthermore, we know the scalar factor $\eta$ from comparing $\kappa\left(\tilde{h}_{i_{1}}, \tilde{h}_{i_{1}}\right)$ and $\hat{\kappa}\left(\hat{h}_{1}, \hat{h}_{1}\right)$. In particular we know what $\kappa\left(\tilde{h}_{r}, \tilde{h}_{r}\right)$ has to be; denote this value by $\theta$.

Now let $h_{1}, \ldots, h_{t}$ be representatives of the $W$-orbits in $\mathcal{H}$ (see Section 2.2). Note that $\kappa(u, u)=\kappa\left(h_{i}, h_{i}\right)$ for all $u$ in the $W$-orbit of $h_{i}$. So we enumerate the orbits of those $h_{i}$
such that $\kappa\left(h_{i}, h_{i}\right)=\theta$. A $\tilde{h}_{r}$ in such an orbit is selected if the matrix $\left(\kappa\left(\tilde{h}_{i_{k}}, \tilde{h}_{i_{l}}\right)\right)$ is equal to $\theta$ times $\widehat{B}$, and $\kappa\left(\tilde{h}_{r}, \tilde{h}_{i}\right)=0$ for $i$ not in $\left\{i_{1}, \ldots, i_{s}\right\}$ (cf. Lemma 1).

If the number of bonds is 1 then we can reduce the work further. Suppose that the node labeled $i_{s}=r$ is connected to the node with label $i_{s-1}$ in $\Gamma$. Let $\beta_{1}, \ldots, \beta_{s}$ be the simple roots of $\hat{\mathfrak{g}}$. Then $\beta_{s-1}$ and $\beta_{s}$ are conjugate under the Weyl group $\widehat{W}$ of $\hat{\mathfrak{g}}$. Also, $\beta_{i}^{\vee}=\hat{h}_{i}$. So from what is said in Section 2.1 it follows that $\hat{h}_{s-1}$ and $\hat{h}_{s}$ are conjugate under $\widehat{W}$. Hence they are conjugate under $\widehat{G}$, the inner automorphism group of $\hat{\mathfrak{g}}$. Now an embedding $\hat{\mathfrak{g}} \hookrightarrow \mathfrak{g}$ induces an embedding $\widehat{G} \hookrightarrow G$. It follows that $\tilde{h}_{i_{s-1}}$ and $\tilde{h}_{r}$ must be conjugate under $G$, which implies that they are conjugate under $W$. The conclusion is that we can limit our search for suitable elements $\tilde{h}_{r}$ to the $W$-orbit of $\tilde{h}_{i_{s-1}}$.

In the second case, in the Dynkin diagram of $\widetilde{C}$, the node labeled $r$ is isolated. In other words, a subalgebra isomorphic to $\tilde{\mathfrak{g}}$ is the direct sum of a subalgebra $\tilde{\mathfrak{g}}_{0}$, with Cartan matrix $\widetilde{C}_{0}$, and a subalgebra isomorphic to $\mathfrak{s l}_{2}$. Then by Lemma 1, we can restrict to adding the $\tilde{h}_{r}$ with $\kappa\left(\tilde{h}_{i}, \tilde{h}_{r}\right)=0$ for $1 \leq i \leq r-1$. Also in this case we run through $\mathcal{H}$ by enumerating the $W$-orbits of the $h_{i}$.

In both cases we can still encounter $W$-orbits that are too large to enumerate. For example, in order to construct the subalgebras of type $A_{2}$, or of type $2 A_{1}$, with the above procedure, one would have to run through all orbits; when $\mathfrak{g}$ is of type $E_{8}$ this amounts to examining 2611951200 elements. In order to reduce the work needed we use characterpuzzles. Let $V$ be the smallest nonzero $\mathfrak{g}$-module. For $\left(\tilde{h}_{1}, \ldots, \tilde{h}_{r}\right) \in \mathcal{H}^{r}$ we compute the corresponding character-puzzle, as in (2), where we view $V$ as a $\tilde{\mathfrak{g}}$-module. We note that all $\tilde{h}_{r}$ in the $W$-orbit of $h_{i}$ lead to the same character-puzzle. So we decide if the characterpuzzle of corresponding to $\left(\tilde{h}_{1}, \ldots, \tilde{h}_{r-1}, h_{i}\right)$ is solvable (i.e., corresponds to a character of $\tilde{\mathfrak{g}}$ ). Only if it is, we enumerate the orbit of $h_{i}$.
Remark. The procedure using character-puzzles eliminates the largest orbits. For example, for $\mathfrak{g}$ of type $E_{8}$, there are 11 orbits (out of a possible 69) that need to be enumerated for constructing the subalgebras of type $A_{2}$; they have sizes 240, 2160, 6720, 17280, 30240, 60480, 69120, 181440, 241920, 483840, 1814400. We also note that $E_{8}$ is a difficult case in two respects: it has by far the largest Weyl group, and the largest minimal faithful representation of all simple Lie algebras of ranks $\leq 8$. The fact that the minimal faithful module has dimension 248 makes solving the character puzzles rather hard. However, it is still worth the wile, as the orbits that are excluded this way are so big. From the sizes of the orbits that still need to be enumerated we also see the need for an algorithm, as the one of Snow ([16]), that does so using little memory.

\section*{6 Subalgebras of semisimple Lie algebras}

Let $\mathfrak{g}=\mathfrak{g}_{1} \oplus \mathfrak{g}_{2}$ be the direct sum of two semisimple ideals. Let $\mathfrak{h}=\mathfrak{h}_{1} \oplus \mathfrak{h}_{2}$ be the corresponding decomposition of the Cartan subalgebra. Then the Weyl group $W$ of $\mathfrak{g}$ is a direct product $W_{1} \times W_{2}$, where $W_{1}$ (respectively $W_{2}$ ) acts trivially in $\mathfrak{h}_{2}$ (respectively $\mathfrak{h}_{1}$ ). Let $L_{i}$ be the set of representatives of the linear equivalence classes of semisimple
subalgebras of $\mathfrak{g}_{i}$. We assume that each element of $L_{i}$ has a canonical set of generators with $h$-part lying in $\mathfrak{h}$.

Let $\mathfrak{a} \oplus \mathfrak{b}_{1}, \mathfrak{b}_{2} \oplus \mathfrak{c}$ be elements of $L_{1}, L_{2}$ respectively, where $\mathfrak{b}_{1}, \mathfrak{b}_{2}$ are isomorphic. Let $h_{i}^{1}, x_{i}^{1}, y_{i}^{1}$ for $1 \leq i \leq s, h_{i}^{1}, x_{i}^{1}, y_{i}^{1}$ for $s+1 \leq i \leq s+r, h_{i}^{2}, x_{i}^{2}, y_{i}^{2}$ for $1 \leq i \leq r, h_{i}^{2}, x_{i}^{2}, y_{i}^{2}$ for $r+1 \leq i \leq r+m$ be a canonical generating sets of respectively $\mathfrak{a}, \mathfrak{b}_{1}, \mathfrak{b}_{2}, \mathfrak{c}$. We assume that the canonical generators of $\mathfrak{b}_{1}, \mathfrak{b}_{2}$ are "in the same order"; that is, mapping $x_{s+i}^{1} \rightarrow x_{i}^{2}, y_{s+i}^{1} \rightarrow y_{i}^{2}, h_{s+i}^{1} \rightarrow h_{i}^{2}$, for $1 \leq i \leq r$ defines an isomorphism $\mathfrak{b}_{1} \rightarrow \mathfrak{b}_{2}$. Let $\pi$ be a permutation of $\{1, \ldots, r\}$ preserving the Cartan matrix of $\mathfrak{b}_{2}$, or, equivalently, such that $\kappa_{2}\left(h_{\pi(i)}^{2}, h_{\pi(j)}^{2}\right)=\kappa_{2}\left(h_{i}^{2}, h_{j}^{2}\right)$ for $1 \leq i, j \leq r$, where $\kappa_{2}$ denotes the Killing form of $\mathfrak{g}_{2}$. Then also mapping $x_{s+i}^{1} \rightarrow x_{\pi(i)}^{2}, y_{s+i}^{1} \rightarrow y_{\pi(i)}^{2}, h_{s+i}^{1} \rightarrow h_{\pi(i)}^{2}$ defines an isomorphism $\mathfrak{b}_{1} \rightarrow \mathfrak{b}_{2}$. Let now $\tilde{\mathfrak{g}}$ be the subalgebra of $\mathfrak{g}$ with canonical generating set
$$\begin{aligned}
\left\{h_{i}^{1}, x_{i}^{1}, y_{i}^{1} \mid 1 \leq i \leq s\right\} \cup\left\{h_{s+i}^{1}+h_{\pi(i)}^{2}, x_{s+i}^{1}+x_{\pi(i)}^{2}, y_{s+i}^{1}+y_{\pi(i)}^{2} \mid\right. & 1 \leq i \leq r\} \cup \\
& \left\{h_{i}^{2}, x_{i}^{2}, y_{i}^{2} \mid r+1 \leq i \leq r+m\right\} .
\end{aligned}$$
Let $L$ denote the set of subalgebras of $\mathfrak{g}$ that can be constructed this way. The next proposition is similar to [5], Theorem 15.1.

Proposition 7 Every semisimple subalgebra of $\mathfrak{g}$ is linearly equivalent to an algebra in $L$.
Proof. Let $\tilde{\mathfrak{g}}$ be a semisimple subalgebra of $\mathfrak{g}$. We may assume that it has a canonical set of generators with $h$-part lying in $\mathfrak{h}$.

Let $p_{i}: \mathfrak{g} \rightarrow \mathfrak{g}_{i}$ denote the projection homomorphism. Then $\operatorname{ker} p_{1} \cap \operatorname{ker} p_{2}=0$. Let $\mathfrak{a}$, $\mathfrak{c}$ be the sum of the ideals of $\tilde{\mathfrak{g}}$ that lie respectively in $\operatorname{ker} p_{2}$ and in $\operatorname{ker} p_{1}$. Let $\mathfrak{b}$ be the sum of the remaining ideals. Then $\tilde{\mathfrak{g}}=\mathfrak{a} \oplus \mathfrak{b} \oplus \mathfrak{c}$, with $\mathfrak{a} \subset \mathfrak{g}_{1}$, and $\mathfrak{c} \subset \mathfrak{g}_{2}$. Let $h_{1}^{1}, \ldots, h_{s}^{1}$, $h_{r+1}^{2}, \ldots, h_{r+m}^{2}$ denote the $h$-parts of canonical generating sets of $\mathfrak{a}$ and $\mathfrak{c}$ respectively. Then $h_{i}^{1} \in \mathfrak{h}_{1}, h_{i}^{2} \in \mathfrak{h}_{2}$.

Let $h_{i}, x_{i}, y_{i}, 1 \leq i \leq r$ be a canonical generating set of $\mathfrak{b}$. Let $H$ denote the set containing the $h_{i}^{1}, 1 \leq i \leq s, h_{i}^{2}, r+1 \leq i \leq r+m$ and $h_{i}, 1 \leq i \leq r$. We must show that there is a $w \in W$ such that $w(H)$ is the $h$-part of a subalgebra in $L$.

Note that $p_{1}$ and $p_{2}$ are injective on $\mathfrak{b}$. Write $h_{s+i}^{1}=p_{1}\left(h_{i}\right), h_{i}^{2}=p_{2}\left(h_{i}\right)$, for $1 \leq i \leq r$. Those elements form the $h$-part of a canonical generating set of a semisimple subalgebra $\mathfrak{b}_{1}$, respectively $\mathfrak{b}_{2}$, of $\mathfrak{g}_{1}$ and $\mathfrak{g}_{2}$. Moreover, the $\mathfrak{b}_{i}$ are isomorphic to $\mathfrak{b}$. In particular, $h_{1}^{1}, \ldots, h_{s+r}^{1}$ form the $h$-part of a canonical generating set of the subalgebra $\mathfrak{a} \oplus \mathfrak{b}_{1}$ of $\mathfrak{g}_{1}$. Therefore, after possibly reordering the elements of $H$, there is a $w_{1} \in W_{1}$ such that the $w_{1}\left(h_{i}^{1}\right)$ form the $h$-part of a canonical generating set of an element of $L_{1}$. Note that this fixes the ordering of the $h_{i} \in H$. We can still reorder the $h_{i}^{2} \in H$, where $r+1 \leq i \leq r+m$. So there is a $w_{2} \in W_{2}$ such that $w_{2}\left(h_{1}^{2}\right), \ldots, w_{2}\left(h_{r}^{2}\right), w_{2}\left(h_{r+1}^{2}\right), \ldots, w_{2}\left(h_{r+m}^{2}\right)$ form the $h$ part of an element of $L_{2}$, up to, possibly, a permutation $\pi$ of the first $r$ elements. This permutation has to leave the Cartan matrix of $\mathfrak{b}_{2}$ invariant. \(\square\)

Proposition 7 gives an immediate procedure for finding a set $L$ containing representatives of all linear equivalence classes of semisimple subalgebras of $\mathfrak{g}$. However, it can still happen that different members of $L$ are linearly equivalent. For weeding out linear equivalent pairs we use the algorithm outlined in Section 3. We also note that $L$ is the disjoint
union of two subsets $L^{\prime}, L^{\prime \prime}$. Here $L^{\prime}$ contains the subalgebras that are the direct sum of an algebra in $L_{1}$ and an algebra in $L_{2}$. And $L^{\prime \prime}$ has the algebras constructed as above with $\mathfrak{b}_{1}, \mathfrak{b}_{2} \neq 0$. Among the algebras in $L^{\prime}$ there are no linear equivalences. Furthermore, an algebra in $L^{\prime}$ is never linearly equivalent to an algebra in $L^{\prime \prime}$.

\section*{7 Deciding inclusion}

For two semisimple subalgebras $\tilde{\mathfrak{g}}_{1}, \tilde{\mathfrak{g}}_{2} \subset \mathfrak{g}$ we write $\tilde{\mathfrak{g}}_{1} \rightarrow \tilde{\mathfrak{g}}_{2}$ if $\tilde{\mathfrak{g}}_{1}$ is linearly equivalent to a subalgebra of $\tilde{\mathfrak{g}}_{2}$. (Here linear equivalence is defined with respecto to $\mathfrak{g}$.) Given $\tilde{\mathfrak{g}}_{1}, \tilde{\mathfrak{g}}_{2}$, with canonical generating sets with $h$-parts in $\mathfrak{h}$, we decide whether $\tilde{\mathfrak{g}}_{1} \rightarrow \tilde{\mathfrak{g}}_{2}$ in the following way: First we let $L$ be the set of representatives of the classes of linear equivalent subalgebras of $\tilde{\mathfrak{g}}_{2}$. We get this from the classification of those subalgebras of $\tilde{\mathfrak{g}}_{2}$. All are given by canonical generating sets having $h$-parts in $\mathfrak{h}$. Then we decide whether $\tilde{\mathfrak{g}}_{1}$ is linearly equivalent to an element of $L$, using the algorithm from Section 3.

Now let $\tilde{\mathfrak{g}}_{1}, \ldots, \tilde{\mathfrak{g}}_{s}$ be a chain of subalgebras. This means that $\tilde{\mathfrak{g}}_{i} \rightarrow \tilde{\mathfrak{g}}_{i+1}$ for $1 \leq i<s$. Then we can compute a realization of the chain; that is if necessary we replace the $\tilde{\mathfrak{g}}_{i}$ by linear conjugates such that $\tilde{\mathfrak{g}}_{i} \subset \tilde{\mathfrak{g}}_{i+1}$. For this we start "at the top", and suppose that $\tilde{\mathfrak{g}}_{i} \rightarrow \cdots \rightarrow \tilde{\mathfrak{g}}_{s}$ has been realised. We compute the subalgebras of $\tilde{\mathfrak{g}}_{i}$ isomorphic to $\tilde{\mathfrak{g}}_{i-1}$, up to linear equivalence. We find a subalgebra $\mathfrak{s}$ that is linearly equivalent to $\tilde{\mathfrak{g}}_{i-1}$, and replace $\tilde{\mathfrak{g}}_{i-1}$ by $\mathfrak{s}$.

\section*{References}
\begin{itemize}
\item[] [1] R. W. Carter. Finite Groups of Lie Type, conjugacy classes and complex characters. John Wiley \& Sons, Chichester, 1985.
\item[] [2] David H. Collingwood and William M. McGovern. Nilpotent orbits in semisimple Lie algebras. Van Nostrand Reinhold Mathematics Series. Van Nostrand Reinhold Co., New York, 1993.
\item[] [3] D. Cox, J. Little, and D. O'Shea. Ideals, Varieties and Algorithms: An Introduction to Computational Algebraic Geometry and Commutative Algebra. Springer Verlag, New York, Heidelberg, Berlin, 1992.
\item[] [4] E. B. Dynkin. Maximal subgroups of the classical groups. Trudy Moskov. Mat. Obšč., 1:39-166, 1952. English translation in: Amer. Math. Soc. Transl. (6), (1957), 245-378.
\item[] [5] E. B. Dynkin. Semisimple subalgebras of semisimple Lie algebras. Mat. Sbornik N.S., 30(72):349-462 (3 plates), 1952. English translation in: Amer. Math. Soc. Transl. (6), (1957), 111-244.
\item[] [6] The GAP Group. GAP - Groups, Algorithms, and Programming, Version 4.4, 2004. (\protect\vrule width0pt\protect\href\{http://www.gap-system.org\}\{http://www.gap-syst
\end{itemize}
\begin{itemize}
\item[] [7] W. A. de Graaf. Lie Algebras: Theory and Algorithms, volume 56 of North-Holland Mathematical Library. Elsevier Science, 2000.
\item[] [8] W. A. de Graaf. SLA - computing with Simple Lie Algebras. a GAP package, 2009. ( protect\vrule width0pt\protect\href\{http://science.unitn.it/\string ${ }^{\sim}$ degraaf/sla.ht
\item[] [9] J. E. Humphreys. Reflection groups and Coxeter groups. Cambridge University Press, Cambridge, 1990.
\item[] [10] F. Iachello and A. Arima. The interacting boson model. Cambridge Monographs on Mathematical Physics. Cambridge University Press, Cambridge, 1987.
\item[] [11] N. Jacobson. Lie Algebras. Dover, New York, 1979.
\item[] [12] M. Lorente and B. Gruber. Classification of semisimple subalgebras of simple Lie algebras. J. Mathematical Phys., 13:1639-1663, 1972.
\item[] [13] W. G. McKay and J. Patera. Tables of dimensions, indices, and branching rules for representations of simple Lie algebras. Marcel Dekker Inc., New York, 1981.
\item[] [14] A. N. Minchenko. Semisimple subalgebras of exceptional Lie algebras. Tr. Mosk. Mat. Obs., 67:256-293, 2006. English translation in: Trans. Moscow Math. Soc. 2006, 225-259.
\item[] [15] J.-P. Serre. Algèbres de Lie semi-simples complexes. W. A. Benjamin, inc., New York-Amsterdam, 1966.
\item[] [16] D. M. Snow. Weyl group orbits. ACM Trans. Math. Software, 16(1):94-108, 1990.
\item[] [17] È. B. Vinberg. The Weyl group of a graded Lie algebra. Izv. Akad. Nauk SSSR Ser. Mat., 40(3):488-526, 709, 1976. English translation: Math. USSR-Izv. 10, 463-495 (1976).
\end{itemize}
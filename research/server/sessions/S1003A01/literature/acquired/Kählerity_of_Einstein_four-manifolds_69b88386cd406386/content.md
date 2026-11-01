---
retention_scope: session
part: 1
total_parts: 1
---

---
source_file: 2206_04870.pdf
converter: mathpix
format: mmd
---

\title{
KÄHLERITY OF EINSTEIN FOUR-MANIFOLDS
}

\author{
XIAOLONG LI AND YONGJIA ZHANG
}

\begin{abstract}
We prove that a closed oriented Einstein four-manifold is either anti-self-dual or (after passing to a double Riemannian cover if necessary) Kähler-Einstein, provided that $\lambda_{2} \geq-\frac{S}{12}$, where $\lambda_{2}$ is the middle eigenvalue of the self-dual Weyl tensor $W^{+}$and $S$ is the scalar curvature. An analogous result holds for closed oriented four-manifolds with $\delta W^{+}=0$.
\end{abstract}

\section*{1. Introduction}

We are concerned with the following question in this paper.
Question 1.1. Under what curvature conditions is a closed Einstein four-manifold Kähler?

There have been several answers to this question. Derdzinski proved a fundamental result [Der83] that if the self-dual Weyl tensor $W^{+}$of a closed oriented Einstein four-manifold is parallel and has at most two distinct eigenvalues at every point, then, after passing to a double Riemannian cover if necessary, the metric is Kähler. A result of Micallef and Wang [MW93, Theorem 4.2] asserts that a closed oriented four-manifold with harmonic self-dual Weyl tensor $\left(\delta W^{+}=0\right)$ and half nonnegative isotropic curvature either is anti-self-dual or has a Kähler universal cover with constant positive scalar curvature (see also [GL99], [RS16], [FKP14], and [Wu17] for alternative proofs).

The purpose of this paper is to provide another curvature condition that characterizes closed Kähler-Einstein four-manifolds. To state our results, let us recall that the bundle $\Lambda^{2}$ of two-forms over an oriented (that is, orientable with an appointed orientation) Riemannian four-manifold ( $M^{4}, g$ ) admits an orthogonal decomposition
$$\Lambda^{2}=\Lambda^{+} \oplus \Lambda^{-},$$
with $\Lambda^{+}$and $\Lambda^{-}$being the +1 and -1 eigenspaces of the Hodge star operator, respectively. Sections of $\Lambda^{+}$are called self-dual two-forms, while sections of $\Lambda^{-}$are called anti-self-dual two-forms. The Riemann curvature tensor may be identified with a self-adjoint linear map
$$\operatorname{Rm}: \Lambda^{2} \rightarrow \Lambda^{2}$$

\footnotetext{
2020 Mathematics Subject Classification. 53C21, 53C25, 53C55.
Key words and phrases. Einstein four-manifolds, Kähler-Einstein, self-dual Weyl tensor, curvature restriction.
The first author's research is partially supported by a start-up grant at Wichita State University.
}
called the curvature operator, via
$$\operatorname{Rm}\left(e_{i} \wedge e_{j}\right)=\frac{1}{2} R_{i j k l} e_{k} \wedge e_{l} .$$
Corresponding to the decomposition $\Lambda^{2}=\Lambda^{+} \oplus \Lambda^{-}$, the Riemann curvature operator Rm can be decomposed into the following irreducible pieces:
$$\operatorname{Rm}=\left[\begin{array}{c|c}
W^{+}+\frac{S}{12} I & \operatorname{Ric} \\
\hline \begin{array}{c}
\circ \\
\operatorname{Ric}
\end{array} & W^{-}+\frac{S}{12} I
\end{array}\right],$$
where $S$ is the scalar curvature, $I$ is the identity map, Ric $=\operatorname{Ric}-\frac{S}{4} g$ is the traceless Ricci tensor, and $W^{ \pm}: \Lambda^{ \pm} \rightarrow \Lambda^{ \pm}$are called the self-dual and anti-self-dual parts of the Weyl curvature operator $W: \Lambda^{2} \rightarrow \Lambda^{2}$. It is also convenient to denote by $\mathrm{Rm}^{+}$and $\mathrm{Rm}^{-}$the restriction of the Riemann curvature operator on $\Lambda^{+}$and $\Lambda^{-}$, respectively. In other words, $\operatorname{Rm}^{ \pm}=W^{ \pm}+\frac{S}{12} I$. A four-manifold $\left(M^{4}, g\right)$ is said to be anti-self-dual if $W^{+} \equiv 0$ and self-dual if $W^{-} \equiv 0$.

It is well-known that on any Kähler surface $\left(M^{4}, J, g\right)$ with the natural orientation (in the sense that the Kähler form is self-dual), the self-dual Weyl operator $W^{+}: \Lambda^{+} \rightarrow \Lambda^{+}$is given by
$$W^{+}=\left[\begin{array}{lll}
\frac{S}{6} & & \\
& -\frac{S}{12} & \\
& & -\frac{S}{12}
\end{array}\right] .$$
In particular, if $\lambda_{1} \leq \lambda_{2} \leq \lambda_{3}$ are the eigenvalues of $W^{+}$, then we have
$$\lambda_{2}=-\frac{S}{12}$$
on any Kähler surface, regardless of the sign of $S$. Equivalently, the middle eigenvalue of $\mathrm{Rm}^{+}$vanishes on any Kähler surfaces.

Our main result states that if a closed oriented Einstein four-manifold satisfies the condition
$$\lambda_{2} \geq-\frac{S}{12},$$
then it is either anti-self-dual or Kähler-Einstein (after passing to a double cover if necessary). More precisely, we prove

Theorem 1.1. Let $\left(M^{4}, g\right)$ be a closed oriented Einstein four-manifold. Denote by $\lambda_{1} \leq \lambda_{2} \leq \lambda_{3}$ the eigenvalues of $W^{+}$and by $S$ the scalar curvature. If $\lambda_{2} \geq-\frac{S}{12}$ everywhere, then one of the following assertions holds:
\begin{itemize}
\item[(1)] $S \neq 0$ and $(M, g)$ is Kähler-Einstein, or has a double Riemannian cover $\pi:\left(M^{*}, g^{*}\right) \rightarrow(M, g)$, where $g^{*}=\pi^{*} g$, such that $\left(M^{*}, g^{*}\right)$ is Kähler-Einstein.
\item[(2)] $(M, g)$ is anti-self-dual with nonnegative scalar curvature. Moreover,
\begin{itemize}
\item[-] if $S>0$, then $M$ is isometric to a quotient of $\mathbb{S}^{4}$ with the round metric or $\mathbb{C} \mathbb{P}^{2}$ with the Fubini-Study metric.
\end{itemize}
\end{itemize}
\begin{itemize}
\item[-] if $S=0$, then either $M$ is flat or its universal cover is a K3 surface with the Calabi-Yau metric.
\end{itemize}

In the nonnegative scalar curvature case, Theorem 1.1 provides a generalization of the result of Micallef and Wang [MW93], as the condition $\lambda_{2} \geq-\frac{S}{12}$ is weaker than half nonnegative isotropic curvature. Recall that an oriented four-manifold is said to have half nonnegative (resp. positive) isotropic curvature if $\mathrm{Rm}^{+}$is twononnegative (resp. two-positive), i.e., the sum of the smallest two eigenvalues of $\mathrm{Rm}^{+}$is nonnegative (resp. positive). In view of $\mathrm{Rm}^{+}=W^{+}+\frac{S}{12} I$, we see that half nonnegative isotropic curvature is equivalent to
$$S \geq 0 \quad \text { and } \quad \lambda_{1}+\lambda_{2} \geq-\frac{S}{6},$$
so it is stronger than the condition $\lambda_{2} \geq-\frac{S}{12}$.
In the negative scalar curvature case, Theorem 1.1 to the best of our knowledge, seems to be the only answer to Question 1.1 other than that of Derdzinski [Der83].

As a corollary of Theorem 1.1, we have a sufficient and necessary condition for a closed Einstein four-manifold to be Kähler.

Corollary 1.2. Let $\left(M^{4}, g\right)$ be a closed and oriented (positive or negative) Einstein four-manifold which satisfies $H^{1}\left(M ; \mathbb{Z}_{2}\right)=0$ and is not isometric to $\mathbb{S}^{4}$ with the round metric. Then $\left(M^{4}, g\right)$ is Kähler if and only if $\lambda_{2}\left(W^{+}\right) \geq-\frac{S}{12}$ everywhere.

In addition, Theorem 1.1 also implies some interesting classification results. In the positive scalar curvature case, we have

Corollary 1.3. Let $\left(M^{4}, g\right)$ be a closed simply-connected Einstein four-manifold with positive scalar curvature. If $\lambda_{2}\left(W^{+}\right)>-\frac{S}{12}$ on $M$, then $W^{+} \equiv 0$ and $M$ is isometric to $\mathbb{S}^{4}$ with the round metric or $\mathbb{C P}^{2}$ with the Fubini-Study metric.

Remark 1.4. Corollary 1.3 was proved by Polombo [Pol92] assuming the stronger condition of half positive isotropic curvature, which is equivalent to
$$S>0 \quad \text { and } \quad \lambda_{1}+\lambda_{2}>-\frac{S}{6} .$$
Alternative proofs of Polombo's result can be found in [MW93], [FKP14], [RS16], and [Wu17].

Remark 1.5. The assumption $\lambda_{2}>-\frac{S}{12}$ in Corollary 1.3 cannot be relaxed in view of the Einstein manifold $\mathbb{S}^{2} \times \mathbb{S}^{2}$, which has $\lambda_{2}=-\frac{S}{12}$ everywhere.

In the Ricci-flat case, we have
Corollary 1.6. Let $\left(M^{4}, g\right)$ be a closed oriented Ricci-flat four-manifold. If $\lambda_{2}\left(W^{+}\right) \geq$ 0 on $M$, then $W^{+} \equiv 0$, and either $M$ is flat or its universal cover is a K3 surface with the Calabi-Yau metric.

Remark 1.7. Corollary 1.6 was proved by Micallef and Wang [MW93] under the stronger condition of half-nonnegative isotropic curvature. Alternative proofs of their result can be found in [FKP14], [RS16], and [Wu17]. However, it seems that none of these proofs work under our weaker curvature assumption.

With a bit more efforts, the method employed to prove Theorem 1.1 also yields analogous results for closed four-manifolds with harmonic (namely, divergence free) self-dual Weyl tensor, i.e.
$$\delta W^{+}:=-\nabla \cdot W^{+}=0 .$$
All Einstein metrics satisfy (1.1) as a consequence of the second Bianchi identity. However, (1.1) is actually much weaker than the Einstein condition.

Theorem 1.8. Let ( $M^{4}, g$ ) be a closed oriented four-manifold with $\delta W^{+}=0$. Denote by $\lambda_{1} \leq \lambda_{2} \leq \lambda_{3}$ the eigenvalues of $W^{+}$and by $S$ the scalar curvature. If $\lambda_{2} \geq-\frac{S}{12}$ everywhere, then one of the following assertions holds:
\begin{itemize}
\item[(1)] $\left(M^{4}, g\right)$ has constant nonzero scalar curvature, and $\left(M^{4}, g\right)$ is Kähler, or has a double Riemannian cover $\pi:\left(M^{*}, g^{*}\right) \rightarrow(M, g)$, where $g^{*}=\pi^{*} g$, such that $\left(M^{*}, g^{*}\right)$ is Kähler.
\item[(2)] $\left(M^{4}, g\right)$ is anti-self-dual with nonnegative scalar curvature.
\end{itemize}

We would like to point out that both Theorem 1.1 and Theorem 1.8 are also motivated by an important work of Peng Wu [Wu21], in which he found a beautiful characterization of conformally Kähler Einstein metrics of positive scalar curvature on closed oriented four-manifolds via the condition $\operatorname{det}\left(W^{+}\right)>0$. LeBrun LeB21, based on his earlier work in [LeB15], provided an entirely different proof of the result and relaxed the assumptions to $W^{+} \neq 0$ and $\left|W^{+}\right|^{-3} \operatorname{det}\left(W^{+}\right) \geq-\frac{5 \sqrt{2}}{21 \sqrt{21}}$. In comparison with Wu and Lebrun's result, Theorem 1.1 has the advantage of giving a curvature characterization in the negative scalar curvature case, but has the disadvantage of using a closed curvature condition. Moreover, the condition $\lambda_{2} \geq-\frac{S}{12}$ is not conformally invariant, thus it does not allow any conformally Kähler manifolds.

Theorem 1.8 implies the following results, which are known under the stronger assumption of half positive (resp. nonnegative) isotropic curvature (see Pol92, [MW93], [FKP14], [RS16], and [Wu17]).

Corollary 1.9. Let $\left(M^{4}, g\right)$ be a closed oriented four-manifold with $\delta W^{+}=0$ and positive scalar curvature. If $\lambda_{2}>-\frac{S}{12}$ on $M$, then $W^{+} \equiv 0$.
Corollary 1.10. Let $\left(M^{4}, g\right)$ be a closed oriented four-manifold with $\delta W^{+}=0$ and nonnonegative scalar curvature. If $\lambda_{2} \geq 0$ on $M$, then $W^{+} \equiv 0$.

To conclude this introduction, we give a brief discussion of our strategies to prove the above-mentioned results. In order to prove Theorem 1.1, we apply the maximum principle to the following partial differential inequality
$$\Delta\left(\lambda_{3}-\lambda_{1}\right) \geq 6\left(\lambda_{3}-\lambda_{1}\right)\left(\lambda_{2}+\frac{S}{12}\right)$$
to conclude that $\lambda_{3}-\lambda_{1}$ must be a constant. Moreover, we must have $\lambda_{2}=-\frac{S}{12}$ everywhere unless $M$ is anti-self-dual. This together with the Einstein condition implies that all the $\lambda_{i}$ 's are constant functions, and their values can be read from the differential inequalities satisfied by them. The desired Kählerity then follows from the work of Derdzinski [Der83].

The key to prove Theorem 1.8 is to show that the scalar curvature must be constant unless $M$ is anti-self-dual. We achieve this by picking up some extra
gradient terms in (1.2), which are used to conclude that the $\lambda_{i}$ 's are constants. It is worth mentioning that these helpful extra terms are used in Wu [Wu21] as well.

The proofs of Theorem 1.1 and Theorem 1.8 are given in Section 2 and Section 3, respectively.

\section*{2. The Einstein Case}

In this section, we prove Theorem 1.1. First of all, we prove two technical propositions which will also be applied in Section 3. Note that Proposition 2.1 assumes only harmonic self-dual Weyl tensor, while Proposition 2.2 assumes, in addition, constant scalar curvature; these assumptions are consequences of the Einstein condition.

Proposition 2.1. Let ( $M^{4}, g$ ) be a closed oriented four-manifold with $\delta W^{+}=0$. Denote by $\lambda_{1} \leq \lambda_{2} \leq \lambda_{3}$ the eigenvalues of $W^{+}$. If $\lambda_{2} \geq-\frac{S}{12}$ everywhere, then either $W^{+} \equiv 0$ or $\lambda_{3}-\lambda_{1}$ is equal to a positive constant and $\lambda_{2}=-\frac{S}{12}$ everywhere.

Proposition 2.2. Let $\left(M^{4}, g\right)$ be a closed oriented four-manifold with $\delta W^{+}=0$ and with constant scalar curvature $S$. Denote by $\lambda_{1} \leq \lambda_{2} \leq \lambda_{3}$ the eigenvalues of $W^{+}$. If $\lambda_{2} \geq-\frac{S}{12}$ everywhere and $W^{+} \not \equiv 0$, then the following statements hold:
\begin{itemize}
\item[(1)] $\lambda_{2}=-\frac{S}{12}$;
\item[(2)] $\lambda_{1}=-\frac{S}{12}$ and $\lambda_{3}=\frac{S}{6}$ if $S>0$, and $\lambda_{1}=\frac{S}{6}$ and $\lambda_{3}=-\frac{S}{12}$ if $S<0$;
\item[(3)] $\nabla W^{+}=0$.
\end{itemize}

Proof of Proposition 2.1. According to [MW93, page 664], $\delta W^{+}=0$ is equivalent to the Weitzenböck formula
$$\Delta W^{+}=\frac{S}{2} W^{+}-2\left(W^{+}\right)^{2}-4\left(W^{+}\right)^{\#},$$
where the $\left(W^{+}\right)^{\#}$ is the adjoint matrix of $W^{+}$. The reader may consult [Ham86] or [CLN06] for more information. If we choose an orthonormal basis $\left\{\omega_{i}\right\}_{i=1}^{3}$ of $\Lambda^{+}$ that diagonalizes $W^{+}$with eigenvalues $\lambda_{1} \leq \lambda_{2} \leq \lambda_{3}$, then, with respect to this basis, we have
$$\left(W^{+}\right)^{2}=\left[\begin{array}{lll}
\lambda_{1}^{2} & & \\
& \lambda_{2}^{2} & \\
& & \lambda_{3}^{2}
\end{array}\right]$$
and
$$\left(W^{+}\right)^{\#}=\left[\begin{array}{lll}
\lambda_{2} \lambda_{3} & & \\
& \lambda_{1} \lambda_{2} & \\
& & \lambda_{1} \lambda_{2}
\end{array}\right] .$$
Therefore, the Weitzenböck formula (2.1) implies the following differential inequalities for the eigenvalues $\lambda_{1}$ and $\lambda_{3}$
$$\begin{aligned}
\Delta \lambda_{1} & \leq \frac{S}{2} \lambda_{1}-2 \lambda_{1}^{2}-4 \lambda_{2} \lambda_{3} \\
\Delta \lambda_{3} & \geq \frac{S}{2} \lambda_{3}-2 \lambda_{3}^{2}-4 \lambda_{1} \lambda_{2}
\end{aligned}$$
Since $\lambda_{1}$ and $\lambda_{3}$ are only locally Lipschitz functions on $M$, the inequalities above are all understood in the sense of barrier (see [Cal58]). To prove (2.2) and (2.3), one may construct the barriers as follows. Fix $p \in M$ and let $\omega \in \Lambda_{p}^{+}$be the unit
eigenvector of $W_{p}^{+}$associated with $\lambda_{3}$. Now we may extend $\omega$ to a neighborhood of $p$ by parallel transport and compute using the normal coordinates at $p$ :
$$\begin{aligned}
\Delta\left(W^{+}(\omega, \omega)\right) & =\left(\Delta W^{+}\right)(\omega, \omega) \\
& =\frac{S}{2} W^{+}(\omega, \omega)-2\left|W^{+}(\omega)\right|^{2}-4\left(W^{+}\right)^{\#}(\omega, \omega) \\
& =\frac{S}{2} \lambda_{3}-2 \lambda_{3}^{2}-4 \lambda_{1} \lambda_{2} \quad \text { at } p .
\end{aligned}$$
Obviously, $W^{+}(\omega, \omega)$ is a lower barrier of $\lambda_{3}$ at $p$, and this proves (2.3); the proof of (2.2) is similar.

Subtracting (2.2) from (2.3) yields
$$\begin{aligned}
\Delta\left(\lambda_{3}-\lambda_{1}\right) & \geq \frac{S}{2}\left(\lambda_{3}-\lambda_{1}\right)-2\left(\lambda_{3}^{2}-\lambda_{1}^{2}\right)+4 \lambda_{2}\left(\lambda_{3}-\lambda_{1}\right) \\
& =\left(\lambda_{3}-\lambda_{1}\right)\left(\frac{S}{2}-2 \lambda_{1}-2 \lambda_{3}+4 \lambda_{2}\right) \\
& =6\left(\lambda_{3}-\lambda_{1}\right)\left(\lambda_{2}+\frac{S}{12}\right),
\end{aligned}$$
where we have used $\lambda_{1}+\lambda_{2}+\lambda_{3}=0$ in the last step. It follows from $\lambda_{2} \geq-\frac{S}{12}$ that
$$\Delta\left(\lambda_{3}-\lambda_{1}\right) \geq 6\left(\lambda_{3}-\lambda_{1}\right)\left(\lambda_{2}+\frac{S}{12}\right) \geq 0,$$
in the sense of barrier. By the maximum principle, we conclude that $\lambda_{3}-\lambda_{1} \equiv c \geq 0$. Note that $c=0$ implies $W^{+} \equiv 0$. In case $c>0$, the desired equality $\lambda_{2}=-\frac{S}{12}$ follows from
$$0=\Delta\left(\lambda_{3}-\lambda_{1}\right) \geq 6\left(\lambda_{3}-\lambda_{1}\right)\left(\lambda_{2}+\frac{S}{12}\right) .$$
The proof is finished. \(\square\)

Proof of Proposition 2.2. Part (1) follows immediately from Proposition 2.1 since $W^{+} \not \equiv 0$.

To prove part (2), we first notice that $\lambda_{3}-\lambda_{1}$ is equal to a positive constant by Proposition 2.1. Now the constant scalar curvature assumption implies that $\lambda_{1}+\lambda_{3}$ is a constant function, as
$$\lambda_{1}+\lambda_{3}=-\lambda_{2}=\frac{S}{12} .$$
It then follows that both $\lambda_{1}$ and $\lambda_{3}$ must be constant functions. Substituting $\lambda_{2}=-\frac{S}{12}$ and $\lambda_{1}+\lambda_{2}+\lambda_{3}=0$ into the differential inequalities satisfied by $\lambda_{1}$ and $\lambda_{3}$, we obtain that
$$\begin{aligned}
& 0=\Delta \lambda_{1} \quad \leq \quad \frac{S}{2} \lambda_{1}-2 \lambda_{1}^{2}-4 \lambda_{2} \lambda_{3}=-2\left(\lambda_{1}+\frac{S}{12}\right)\left(\lambda_{1}-\frac{S}{6}\right) \\
& 0=\Delta \lambda_{3} \quad \geq \frac{S}{2} \lambda_{3}-2 \lambda_{3}^{2}-4 \lambda_{1} \lambda_{2}=-2\left(\lambda_{3}+\frac{S}{12}\right)\left(\lambda_{3}-\frac{S}{6}\right) .
\end{aligned}$$
One easily reads from above inequalities that we must have
$$\begin{aligned}
\lambda_{1}=\lambda_{3}=0, & \text { if } S=0 ; \\
\lambda_{1}=-\frac{S}{12} \text { and } \lambda_{3}=\frac{S}{6}, & \text { if } S>0 ; \\
\lambda_{1}=\frac{S}{6} \text { and } \lambda_{3}=-\frac{S}{12}, & \text { if } S<0 .
\end{aligned}$$
Now part (2) is proved.
Part (3) follows immediately from part (2) and the constant scalar curvature assumption. \(\square\)

We now give the proof of Theorem 1.1.

Proof of Theorem 1.1. If $M$ is anti-self-dual, then $0=\lambda_{2} \geq-S / 12$ implies that $S$ is a nonnegative constant. By Hitchin's classification [Hit74] of half conformally flat Einstein four-manifolds with nonnegative scalar curvature (see also Bes08, Theorem 13.30]), $\left(M^{4}, g\right)$ is one of the manifolds as described in part (2) of the statement.

If $M$ is not anti-self-dual, then by Proposition 2.2, we have that $\nabla W^{+}=0$ and $W^{+}$has at most two distinct eigenvalues at every point. One can then invoke the result of Derdzinski [Der83, Therorem 2] to conclude that either $M$ is Kähler or it has a double cover that is Kähler. Below we provide a more direct proof using an elegant argument of Lebrun [LeB21], which is also applicable to the proof of Theorem 1.8. We shall only present the case where $M$ has negative constant scalar curvature, as it can be easily adapted to the positive scalar curvature case by flipping signs and reversing directions of the related inequalities.

Since $\lambda_{1}=S / 6$ is an isolated eigenvalue of $W^{+}$, we have that the corresponding eigenspaces of $W^{+}$at each point on $M$ form a one-dimensional subbundle of $\Lambda^{+}$. Denote this bundle by $L$. If $L$ is a trivial bundle (in particular, if $H^{1}\left(M ; \mathbb{Z}_{2}\right)=$ 0), then we can find a non-vanishing global section $\omega$ of $L$ with constant norm everywhere. If $L$ does not have a non-vanishing global section, then we may let $M^{*}$ be all the elements in $L$ with constant unit norm, and the restriction of the bundle projection $\pi: M^{*} \rightarrow M$ is a double cover. If we equip $M^{*}$ with the Remannian metric $g^{*}=\pi^{*} g$, then $\left(M^{*}, g^{*}\right)$ also satisfies Proposition 2.1 and $W^{+}$admits a global eigenvector section associated with $\lambda_{1}=S / 6$. Henceforth, we will assume that $L$ admits a global section $\omega$ with constant norm $|\omega| \equiv \sqrt{2}$.

Since $\omega$, when viewed as an operator on $T M$, satisfies
$$\omega \cdot \omega=-\mathrm{id},$$
we have that $\omega$ provides an almost complex structure. We need only to show that $\omega$ is a closed form.

We first observe that
$$W^{+}\left(\nabla_{X} \omega, \nabla_{X} \omega\right) \geq 0 .$$
for any tangent vector $X$. This is because $\omega$ has constant norm, which implies that $\left\langle\nabla_{X} \omega, \omega\right\rangle=0$ and hence $\nabla_{X} \omega$ is in the eigenspace of $\lambda_{2}=\lambda_{3}=-S / 12>0$.

Now recall that when $\delta W^{+}=0$, the following Weitzenböck formula holds (c.f. [MW93, (4.1c)] or [LeB21, Equation (9)])
$$\Delta W^{+}=\frac{S}{2} W^{+}-6 W^{+} \circ W^{+}+2\left|W^{+}\right|^{2} I .$$

It is easy to check that (2.5) is equivalent to (2.1). We now take inner product of (2.5) and $\omega \otimes \omega$, and integrate over $M$ to get
$$\begin{aligned}
0= & \left.\left.\int_{M}\left\langle-\Delta W^{+}+\frac{S}{2} W^{+}-6 W^{+} \circ W^{+}+2\right| W^{+}\right|^{2} I, \omega \otimes \omega\right\rangle d g \\
= & \int_{M}\left(-2 W^{+}(\omega, \Delta \omega)-2 W^{+}\left(\nabla_{e} \omega, \nabla^{e} \omega\right)\right. \\
& \left.+\frac{S}{2} \lambda_{1}|\omega|^{2}-6 \lambda_{1}^{2}|\omega|^{2}+2\left(\lambda_{1}^{2}+\lambda_{2}^{2}+\lambda_{3}^{2}\right)|\omega|^{2}\right) d g \\
\leq & -2 \int_{M} \lambda_{1}\langle\omega, \Delta \omega\rangle d g \\
= & \frac{S}{3} \int_{M}|\nabla \omega|^{2} d g
\end{aligned}$$
where we have applied Proposition 2.2(1)(2) and (2.4). Since $S$ is a negative constant, we have that $\nabla \omega$ vanishes everywhere. It follows that $\omega$ is a Kähler form.

In case where $W^{+} \not \equiv 0$ and $S$ is a positive constant, we can also find a Kähler form in the same way. \(\square\)

It is clear that Corollary 1.2. Corollary 1.3, and Corollary 1.6 can be easily observed from the proof of Theorem 1.1

\section*{3. The Harmonic self-dual Weyl case}

If $M$ is only assumed to have harmonic self-dual Weyl tensor, then the proof given in the previous section breaks down because we cannot conclude that both $\lambda_{1}$ and $\lambda_{3}$ are constant functions without the constant scalar curvature assumption. We shall show, by improving the partial differential inequality satisfied by $\lambda_{3}-\lambda_{1}$, that the scalar curvature must be a constant unless $W^{+} \equiv 0$, as a consequence of $\delta W^{+}=0$ and $\lambda_{2} \geq-\frac{S}{12}$.

Proposition 3.1. Let ( $M^{4}, g$ ) be a closed oriented four-manifold with $\delta W^{+}=0$. Denote by $\lambda_{1} \leq \lambda_{2} \leq \lambda_{3}$ the eigenvalues of $W^{+}$. If $\lambda_{2} \geq-\frac{S}{12}$ everywhere, then either $M$ is anti-self-dual with nonnegative scalar curvature, or $M$ has constant scalar curvature.

Proof. Let us recall some computations in [Der83]. For any $x \in M$, we can choose an orthogonal basis $\omega_{1}, \omega_{2}, \omega_{3}$ of $\Lambda_{x}^{+}$, consisting of eigenvectors of $W^{+}$such that
$$\left|\omega_{1}\right|^{2}=\left|\omega_{2}\right|^{2}=\left|\omega_{3}\right|^{2}=2 .$$
Consequently, we have that, at $x$
$$W^{+}=\frac{1}{2}\left(\lambda_{1} \omega_{1} \otimes \omega_{1}+\lambda_{2} \omega_{2} \otimes \omega_{2}+\lambda_{3} \omega_{3} \otimes \omega_{3}\right)$$
with $\lambda_{1} \leq \lambda_{2} \leq \lambda_{3}$ being the eigenvalues of $W^{+}$. Let $M_{W^{+}} \subset M$ be the open dense set where the number of distinct eigenvalues of $W^{+}$is locally constant. In $M_{W^{+}}$, the pointwise formula (3.2) is valid locally in the sense that the mutually orthogonal sections $\omega_{1}, \omega_{2}, \omega_{3}$ of $\Lambda^{+}$satisfying (3.1) and the functions $\lambda_{1}, \lambda_{2}, \lambda_{3}$ may be assumed differentiable in a neighborhood of any $p \in M_{W^{+}}$.

Since $\Lambda^{+}$is invariant under parallel transport, in a neighborhood of $p \in M_{W^{+}}$, there exist one-forms $a, b$, and $c$ defined near $p$, such that we have (3.2) and
$$\begin{aligned}
\nabla \omega_{1} & =a \otimes \omega_{2}-c \otimes \omega_{3}, \\
\nabla \omega_{2} & =b \otimes \omega_{3}-a \otimes \omega_{1}, \\
\nabla \omega_{3} & =c \otimes \omega_{1}-b \otimes \omega_{2} .
\end{aligned}$$
It was shown by Derdzinski [Der83] that if $\delta W^{+}=0$, then in a neighborhood of $p \in M_{W^{+}}$, we have
$$\begin{aligned}
\nabla \lambda_{1} & =\left(\lambda_{2}-\lambda_{1}\right)\left(\iota_{a} \# \omega_{3}\right)^{\#}+\left(\lambda_{3}-\lambda_{1}\right)\left(\iota_{c} \# \omega_{2}\right)^{\#}, \\
\nabla \lambda_{2} & =\left(\lambda_{1}-\lambda_{2}\right)\left(\iota_{a} \# \omega_{3}\right)^{\#}+\left(\lambda_{3}-\lambda_{2}\right)\left(\iota_{b} \# \omega_{1}\right)^{\#}, \\
\nabla \lambda_{3} & =\left(\lambda_{1}-\lambda_{3}\right)\left(\iota_{c} \# \omega_{2}\right)^{\#}+\left(\lambda_{2}-\lambda_{3}\right)\left(\iota_{b}{ }^{\#} \omega_{1}\right)^{\#},
\end{aligned}$$
and
$$\begin{aligned}
\Delta \lambda_{1}= & 2\left(\lambda_{1}-\lambda_{2}\right)\left|\left(\iota_{a} \# \omega_{3}\right)^{\#}\right|^{2}+2\left(\lambda_{1}-\lambda_{3}\right)\left|\left(\iota_{c} \# \omega_{2}\right)^{\#}\right|^{2} \\
& +\frac{S}{2} \lambda_{1}-2 \lambda_{1}^{2}-4 \lambda_{2} \lambda_{3}, \\
\Delta \lambda_{2}= & 2\left(\lambda_{2}-\lambda_{1}\right)\left|\left(\iota_{a} \# \omega_{3}\right)^{\#}\right|^{2}+2\left(\lambda_{2}-\lambda_{3}\right)\left|\left(\iota_{b} \# \omega_{1}\right)^{\#}\right|^{2} \\
& +\frac{S}{2} \lambda_{2}-2 \lambda_{2}^{2}-4 \lambda_{1} \lambda_{3}, \\
\Delta \lambda_{3}= & 2\left(\lambda_{3}-\lambda_{1}\right)\left|\left(\iota_{c} \# \omega_{2}\right)^{\#}\right|^{2}+2\left(\lambda_{3}-\lambda_{2}\right)\left|\left(\iota_{b} \# \omega_{1}\right)^{\#}\right|^{2} \\
& +\frac{S}{2} \lambda_{3}-2 \lambda_{3}^{2}-4 \lambda_{1} \lambda_{2},
\end{aligned}$$
where $\iota$ is the interior product and \# is the sharp operator.
It follows from the assumption $\lambda_{2} \geq-S / 12$ that in the set $M_{W^{+}}$, we have
$$\begin{aligned}
\Delta\left(\lambda_{3}-\lambda_{1}\right)= & 6\left(\lambda_{3}-\lambda_{1}\right)\left(\lambda_{2}+\frac{S}{12}\right)+4\left(\lambda_{3}-\lambda_{1}\right)\left|\left(\iota_{c^{\#}} \omega_{2}\right)^{\#}\right|^{2} \\
& +2\left(\lambda_{3}-\lambda_{2}\right)\left|\left(\iota_{b^{\#}} \omega_{1}\right)^{\#}\right|^{2}+2\left(\lambda_{2}-\lambda_{1}\right)\left|\left(\iota_{a^{\#}} \omega_{3}\right)^{\#}\right|^{2} \\
\geq & 4\left(\lambda_{3}-\lambda_{1}\right)\left|\left(\iota_{c^{\#}} \omega_{2}\right)^{\#}\right|^{2}+2\left(\lambda_{3}-\lambda_{2}\right)\left|\left(\iota_{b^{\#}} \omega_{1}\right)^{\#}\right|^{2} \\
& +2\left(\lambda_{2}-\lambda_{1}\right)\left|\left(\iota_{a}{ }^{\#} \omega_{3}\right)^{\#}\right|^{2} .
\end{aligned}$$
Since $\lambda_{3}-\lambda_{1}$ is a nonnegative constant on $M$ by Proposition 2.1 we conclude that
$$\left(\lambda_{3}-\lambda_{1}\right)\left|\left(\iota_{c} \# \omega_{2}\right)^{\#}\right|^{2}=\left(\lambda_{3}-\lambda_{2}\right)\left|\left(\iota_{b} \# \omega_{1}\right)^{\#}\right|^{2}=\left(\lambda_{2}-\lambda_{1}\right)\left|\left(\iota_{a} \# \omega_{3}\right)^{\#}\right|^{2}=0,$$
in a neighborhood of $p \in M_{W^{+}}$. This implies that
$$\nabla \lambda_{1}=\nabla \lambda_{3}=0$$
in that neighborhood of $p \in M_{W^{+}}$. Therefore, $\lambda_{1}$ and $\lambda_{3}$ are locally constant on $M_{W^{+}}$. Since $M_{W^{+}}$is open and dense in $M$, and since $\lambda_{1}$ and $\lambda_{3}$ are locally Lipschitz functions, we conclude that $\lambda_{1}$ and $\lambda_{3}$ are global constant functions. Moreover $\lambda_{2}=-\lambda_{1}-\lambda_{3}$ is also a constant.

If $M$ is not anti-self-dual, then we have $\lambda_{2}=-\frac{S}{12}$ by Proposition 2.1 $S$ must be a constant since $\lambda_{2}$ is so. \(\square\)

Proof of Theorem 1.8. If $M$ is anti-self-dual, then we have $S \geq 0$ in view of $0=$ $\lambda_{2} \geq-\frac{S}{12}$. If $M$ is not anti-self-dual, then $M$ has constant scalar curvature by Proposition 3.1. In the latter case, Proposition2.2 is valid and the proof of Kählerity is the same as the proof of Theorem 1.1 given in Section 2. \(\square\)

It is clear that Corollary 1.9 and Corollary 1.10 can be observed from the proof of Theorem 1.8.

Acknowledgment
The authors would like to thank Professor Jiaping Wang for some helpful discussions related to this work.

References
\begin{itemize}
\item[] [Bes08] Arthur L. Besse. Einstein manifolds. Classics in Mathematics. Springer-Verlag, Berlin, 2008. Reprint of the 1987 edition.
\item[] [Cal58] E. Calabi. An extension of E. Hopf's maximum principle with an application to Riemannian geometry. Duke Math. J., 25:45-56, 1958.
\item[] [CLN06] Bennett Chow, Peng Lu, and Lei Ni. Hamilton's Ricci flow, volume 77 of Graduate Studies in Mathematics. American Mathematical Society, Providence, RI; Science Press Beijing, New York, 2006.
\item[] [Der83] Andrzej Derdziński. Self-dual Kähler manifolds and Einstein manifolds of dimension four. Compositio Math., 49(3):405-433, 1983.
\item[] [FKP14] Joel Fine, Kirill Krasnov, and Dmitri Panov. A gauge theoretic approach to Einstein 4-manifolds. New York J. Math., 20:293-323, 2014.
\item[] [GL99] Matthew J. Gursky and Claude Lebrun. On Einstein manifolds of positive sectional curvature. Ann. Global Anal. Geom., 17(4):315-328, 1999.
\item[] [Ham86] Richard S. Hamilton. Four-manifolds with positive curvature operator. J. Differential Geom., 24(2):153-179, 1986.
\item[] [Hit74] Nigel Hitchin. Compact four-dimensional Einstein manifolds. J. Differential Geometry, 9:435-441, 1974.
\item[] [LeB15] Claude LeBrun. Einstein metrics, harmonic forms, and symplectic four-manifolds. Ann. Global Anal. Geom., 48(1):75-85, 2015.
\item[] [LeB21] Claude LeBrun. Einstein manifolds, self-dual Weyl curvature, and conformally Kähler geometry. Math. Res. Lett., 28(1):127-144, 2021.
\item[] [MW93] Mario J. Micallef and McKenzie Y. Wang. Metrics with nonnegative isotropic curvature. Duke Math. J., 72(3):649-672, 1993.
\item[] [Pol92] A. Polombo. De nouvelles formules de Weitzenböck pour des endomorphismes harmoniques. Applications géométriques. Ann. Sci. École Norm. Sup. (4), 25(4):393-428, 1992.
\item[] [RS16] Thomas Richard and Harish Seshadri. Positive isotropic curvature and self-duality in dimension 4. Manuscripta Math., 149(3-4):443-457, 2016.
\item[] [Wu17] Peng Wu. A Weitzenböck formula for canonical metrics on four-manifolds. Trans. Amer. Math. Soc., 369(2):1079-1096, 2017.
\item[] [Wu21] Peng Wu. Einstein four-manifolds with self-dual Weyl curvature of nonnegative determinant. Int. Math. Res. Not. IMRN, (2):1043-1054, 2021.
\end{itemize}

Department of Mathematics, Statistics and Physics, Wichita State University, Wichita, KS, 67260

Email address: xiaolong.li@wichita.edu
School of Mathematical Sciences, Shanghai Jiao Tong University, Shanghai, China, 200240

Email address: zhangyongjia918@163.com
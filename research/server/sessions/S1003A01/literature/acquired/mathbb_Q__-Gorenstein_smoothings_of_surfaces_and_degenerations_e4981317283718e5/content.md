---
retention_scope: session
part: 1
total_parts: 1
---

---
source_file: 1311_4844.pdf
converter: mathpix
format: mmd
---

\title{
$\mathbb{Q}$-GORENSTEIN SMOOTHINGS OF SURFACES AND DEGENERATIONS OF CURVES
}

\author{
GIANCARLO URZÚA
}

\begin{abstract}
In this paper we mainly describe $\mathbb{Q}$-Gorenstein smoothings of projective surfaces with only Wahl singularities which have birational fibers. For instance, these degenerations appear in normal degenerations of $\mathbb{P}^{2}$, and in boundary divisors of the KSBA compactification of the moduli space of surfaces of general type [KSB88]. We give an explicit description of them as smooth deformations plus 3-fold birational operations, through the flips and divisorial contractions in [HTU13]. We interpret the continuous part (smooth deformations) as degenerations of certain curves in the general fiber. At the end, we work out examples happening in the KSBA boundary for invariants $K^{2}=1, p_{g}=0$, and $\pi_{1}=0$ using plane curves.
\end{abstract}

\section*{1. Introduction}
$\mathbb{Q}$-Gorenstein smoothings are interesting degenerations of nonsingular surfaces. For instance, stable limits of nonsingular surfaces in the KSBA compactification of the moduli space of surfaces of general type [KSB88] are $\mathbb{Q}$-Gorenstein smoothings. On the other hand, they provide a non-classical construction of nonsingular projective surfaces with fixed invariants by means of certain singular surfaces; this is the pioneering work of Y. Lee and J. Park [LP07]. They are also present in degenerations of other type of surfaces [Kaw92, Man91, HP10, Prok11].

Let $\mathbb{D}$ be a smooth analytic germ of curve. We are interested in $\mathbb{Q}$-Gorenstein smoothings over $\mathbb{D}$ of irreducible projective surfaces $X$ with only quotient singularities. In this case the $\mathbb{Q}$-Gorenstein condition means that the canonical class of the corresponding 3-fold is $\mathbb{Q}$-Cartier (see [Hack12] for a general discussion). The singularities of $X$ are the so-called T-singularities [KSB88]: they are either du Val singularities, or cyclic quotient singularities $\frac{1}{d n^{2}}(1, d n a-1)$ with $\operatorname{gcd}(n, a)=1$. For du Val singularities we have simultaneous resolution. For the others we have particular partial simultaneous resolution (given by the M-resolutions of [BC94]) which has as special fiber a surface with only Wahl singularities, this is, non du Val T-singularities
with $d=1$ [Wahl81, (5.9.1)]. We remark that Wahl singularities are the log terminal singularities which have a rational homology disk smoothing. It turns out that $\mathbb{Q}$-Gorenstein smoothings over $\mathbb{D}$ of projective surfaces with only Wahl singularities have some common characteristics with nonsingular projective surfaces. In §2 we make this precise, showing their MMP with explicit birational operations as in [HTU13], minimal and canonical models, and some numerical invariants.

In general, it is not clear what produces that a nonsingular projective surface admits a $\mathbb{Q}$-Gorenstein degeneration with only Wahl singularities. This type of degenerations have no vanishing cycles. In [Kaw92], Kawamata describes $\mathbb{Q}$-Gorenstein degenerations when the general fiber has Kodaira dimension 0 or 1, giving a reason for the existence using elliptic fibrations. Hacking [Hack13] discusses it for surfaces of general type with geometric genus 0 via exceptional vector bundles. We recall that the Kodaira dimension of the minimal resolution of the special fiber and of the general fiber may be different. For example, the special fiber could be rational and the general fiber could be of general type. This paper is mainly about $\mathbb{Q}$-Gorenstein smoothings over $\mathbb{D}$ of projective surfaces with only Wahl singularities so that the special and general fiber are birational. (It is actually more general, see Theorem 3.4.) These degenerations appear, for example, when studying normal degenerations of $\mathbb{P}^{2}$ [Man91, HP10], and when studying KSBA boundary in the moduli space of surfaces of general type with $p_{g}=0$ (cf. [Urz13]). In this direction, Corollary 3.5 says: any birational $\mathbb{Q}$-Gorenstein smoothing comes from a smooth deformation (continuous part) followed by certain specific birational 3-fold operations (discrete part). These operations are the explicit flips and divisorial contractions in [HTU13]. A distinguished non-trivial case in this theorem is normal degenerations of $\mathbb{P}^{2}$, which is treated separately in §3 (see Example 3.2).

In §4, we look closer at the above "continuous part". We interpret the deformation as degeneration of certain curves. The work with curves is possible because $\mathbb{Q}$-Gorenstein smoothings with only Wahl singularities happen on a $\mathbb{Q}$-factorial 3-fold, and so we have intersection theory. This is a general property induced by normal surface singularities with a rational homology disk smoothing [Wahl11, Prop.3.1]. Using this we will keep track of curve degenerations after each flip or divisorial contraction; for the precise picture see §4. In that section we show conditions to produce many examples (Propositions 4.2 and 4.3), and we give two concrete ones starting with $\mathbb{P}^{2}$ (Examples 4.4 and 4.5).

Our main motivation is to explore the KSBA boundary of the moduli space of simply connected surfaces of general type with $p_{g}=0$.

The above continuous part gives something to work with when some boundary divisors, which parametrize rational singular surfaces, intersect. This continuous part gives degenerations of rational plane curves. Their parameters give the moduli for the divisors, and their further degenerations produce more divisors. In particular, this is an explicit description of the surfaces in any constructed Wahl divisor $\mathcal{D}\binom{n}{a}$; cf. [Urz13]. These plane curves may be irreducible, reducible but reduced, or reducible and nonreduced; some degenerations could give different families in the same moduli space (so the discrete part is now varying). In §5 we show four examples which give a first look at this way of describing KSBA boundary. All of them are simply connected, $K^{2}=1$, and $p_{g}=0$.

Notation. We use definitions, notations, and facts from [HTU13], [Urz13, Preliminaries]. As in [Urz13], the k1A and k2A extremal nbhds in [HTU13] are denoted by mk1A and mk2A. Our ground field is $\mathbb{C}$.

Acknowledgements. I have benefited from many conversations with Paul Hacking and Jenia Tevelev. I was supported by the FONDECYT Inicio grant 11110047 funded by the Chilean Government.

\section*{Contents}
1. Introduction ..... 1
Notation ..... 3
Acknowledgements ..... 3
2. W-surfaces and their MMP ..... 3
3. Birational $\mathbb{Q}$-Gorenstein smoothings ..... 8
4. Degeneration of curves ..... 13
5. Explicit rational examples of general type ..... 17
5.1. Irreducible septic associated to a $\frac{1}{36}(1,5)$ ..... 17
5.2. Degree 15 curve for a $\frac{1}{16}(1,3)$ and nonreduced degeneration ..... 19
5.3. One septic degeneration for two distinct deformations ..... 20
5.4. A maximally singular stable surface via degenerations ..... 21
References ..... 24

\section*{2. W-surfaces and their MMP}

Let $X$ be a normal surface with only quotient singularities, and let $(0 \in \mathbb{D})$ be a smooth analytic germ of curve. A deformation $(X \subset$ $\mathcal{X}) \rightarrow(0 \in \mathbb{D})$ of $X$ is called a smoothing if its general fiber is smooth. It is $\mathbb{Q}$-Gorenstein if $K_{\mathcal{X}}$ is $\mathbb{Q}$-Cartier. A germ of a normal surface
$X$ is called a T-singularity if it is a quotient singularity and admits a $\mathbb{Q}$-Gorenstein smoothing. By [KSB88, Prop.3.10], any T-singularity is either a du Val singularity or a cyclic quotient singularity of the form $\frac{1}{d n^{2}}(1, d n a-1)$ with $\operatorname{gcd}(n, a)=1$. A T-singularity with a onedimensional $\mathbb{Q}$-Gorenstein versal deformation space is either a node $A_{1}$ or a Wahl singularity $\frac{1}{n^{2}}(1, n a-1)$. Hence Wahl singularities are precisely the T-singularities whose $\mathbb{Q}$-Gorenstein smoothing has Milnor number zero.

Definition 2.1. A $W$-surface is a normal projective surface $X$ together with a proper deformation $(X \subset \mathcal{X}) \rightarrow(0 \in \mathbb{D})$ such that
\begin{itemize}
\item[(1)] $X$ has at most Wahl singularities.
\item[(2)] $\mathcal{X}$ is a normal complex 3-fold with $K_{\mathcal{X}} \mathbb{Q}$-Cartier.
\item[(3)] The fiber $X_{0}$ is reduced and isomorphic to $X$.
\item[(4)] The fiber $X_{t}$ is nonsingular for $t \neq 0$.
\end{itemize}
The W-surface is said to be smooth if $X$ is nonsingular.
These situation coincides with the moderate degenerations in [Kaw92]. Notice that a W-surface has $\mathcal{X}$ terminal [KSB88, Cor.3.6] and $\mathbb{Q}$ factorial. The later assertion comes from the fact that $\mathcal{X} \rightarrow \mathbb{D}$ is a $\mathbb{Q}$-Gorenstein smoothing of singularities with Milnor number zero; see [Ko91, 2.2.7], or [Wahl11, Prop.3.1] in more generality. We use proper and not projective deformations since we will perform flips on such $\mathcal{X}$ which involve deformations of partial resolutions of singularities.

We point out that one produces many examples of W-surfaces in the following way; see [Wahl81, (6.4)], [Man91, §1], [LP07, §2]. One constructs a normal projective surface $X$ with only Wahl singularities and $H^{2}\left(X, T_{X}\right)=0$. Then local deformations glue to global deformations of $X$, and we consider the ones coming from $\mathbb{Q}$-Gorenstein smoothings of the singularities. This gives a W-surface. (For technical details in higher generality see [Hack12, §3].)

The aim of this section is to highlight similarities between W-surfaces and smooth projective surfaces via the general fiber. Let $X$ be a W-surface. Then, we have that $K_{X_{t}}=\left.K_{\mathcal{X}}\right|_{X_{t}}$ for all $t$. Also the invariants $K_{X_{t}}^{2}, \chi_{\text {top }}\left(X_{t}\right), q\left(X_{t}\right)=\operatorname{dim}_{\mathbb{C}} H^{1}\left(X_{t}, \mathcal{O}_{X_{t}}\right)$ (in general, see [GS83]), and $p_{g}\left(X_{t}\right)=\operatorname{dim}_{\mathbb{C}} H^{2}\left(X_{t}, \mathcal{O}_{X_{t}}\right)$ are independent of $t$; cf. [Kaw92]. A key property, which will be used frequently, is that the 3-fold is $\mathbb{Q}$-factorial, which allows us to compare curves in the general and special fibers through intersection theory.

Definition 2.2. A W-surface $X$ is minimal if $K_{X}$ is nef.
Lemma 2.3. If a $W$-surface $X$ is minimal, then $K_{X_{t}}$ is nef for all $t$.

Proof. Since $K_{X}$ is nef and $K_{X}^{2}=K_{X_{t}}^{2}$ for all $t$, we have $K_{X_{t}}^{2} \geq 0$. Notice also that (by [GS83, §3]) $q(X)=q\left(X_{t}\right)$ for all $t$, and so $b_{1}\left(X_{t}\right)$ is even since $X$ is projective with Wahl (and so rational) singularities. Suppose there is a $t \neq 0$ so that $K_{X_{t}}$ is not nef. Then since $K_{X_{t}}^{2}>0$ and $b_{1}\left(X_{t}\right)$ is even, we have that either $X_{t}$ is ruled or $X_{t}$ is a surface of general type [BHPV04, p.91].
(I) Say that $X_{t}$ is ruled: Then $X_{t}$ must be rational since $K_{X_{t}}^{2} \geq 0$. This is because a minimal model of $X_{t}$ has canonical class with selfintersection $8\left(1-q\left(X_{t}\right)\right)$ and so $q\left(X_{t}\right)=1,0$. But if $q\left(X_{t}\right)=1$, then $X_{t}$ is a minimal minimal ruled surface since we must have $K_{X_{t}}^{2}=0$. Here, we can use [B86, §3] to show that the minimal resolution $X$ of $X$ must be a ruled surface as well. But then, since $q(\widetilde{X})=1$, we have that the exceptional divisor of the minimal resolution $\widetilde{X} \rightarrow X$ is contained in fibers of a fibration $\widetilde{X} \rightarrow E$, where $E$ is a curve of genus 1 . But then, the image of the general fiber of $\widetilde{X} \rightarrow E$ in $X$ is a $\mathbb{P}^{1}$ so that $\mathbb{P}^{1} \cdot K_{X}=-2$, contradicting that $K_{X}$ is nef. Therefore, we are left with the case of a rational surface $X_{t}$. But then $q(X)=p_{g}(X)=0$, and so the deformation $(X \subset \mathcal{X}) \rightarrow(0 \in \mathbb{D})$ is projective [Man91, p.6]. Now by [B86, Lemma(1.3)], we have that $h^{0}\left(X,-m K_{X}\right) \geq h^{0}\left(X_{t},-m K_{X_{t}}\right)$ for all $m>0$ divisible by the index of all Wahl singularities in $X$. But $h^{0}\left(X_{t},-m K_{X_{t}}\right)=h^{1}\left(X_{t},-m K_{X_{t}}\right)+\frac{m(m+1)}{2} K_{X_{t}}^{2}+1>0$. On the other hand, $X$ is projective, and $K_{X}$ is nef, so $-m K_{X}$ cannot have global sections.
(II) Say that $X_{t}$ is of general type. Then one can prove the existence of a family of (-1)-curves $\Gamma_{t}$ degenerating to some effective divisor $\Gamma_{0}$ in $X$, which gives $K_{X_{t}} \cdot \Gamma_{t}=-1$ for $t \neq 0$, and so in the limit $K_{X} \cdot \Gamma_{0}=-1$, which contradicts the fact that $K_{X}$ is nef. To see this family of (-1)-curves, we first notice that: if $X_{t_{0}}$ is of general type for some $t_{0} \neq 0$, then all $X_{t}$ are of general type for $t \neq 0$ [BHPV04, VI§8]. Now, by results of Kodaira and Iitaka [BHPV04, IV§4], there is a small disk $\mathbb{D}^{\prime}$ in $\mathbb{D} \backslash\{0\}$ around $t_{0}$ with a family of such $(-1)$ -curves. We want to extend it to the whole disk. To prove this, it is enough to show that for a smooth deformation $(W \subset \mathcal{W}) \rightarrow(0 \in \mathbb{D})$ of a smooth projective surface of general type $W$ there exists a smaller disk $\mathbb{D}^{\prime}$ which contains 0 such that all $(-1)$-curves in the neighbor fibers of $\left(W \subset \mathcal{W}^{\prime}\right) \rightarrow\left(0 \in \mathbb{D}^{\prime}\right)$ deform to a $(-1)$-curve in the central fiber $W$. First, to get this small disk $\mathbb{D}^{\prime}$, we use several times the Kodaira and Iitaka results mentioned above to obtain a minimal model $W_{m}$ for $W$ together with a deformation $\left(W_{m} \subset \mathcal{W}_{m}\right) \rightarrow\left(0 \in \mathbb{D}^{\prime}\right)$. Notice that for general type surfaces, we have minimality if and only if $h^{1}(-K)=0$, and so the canonical class of every fiber in $\left(W_{m} \subset\right.$
$\left.\mathcal{W}_{m}\right) \rightarrow\left(0 \in \mathbb{D}^{\prime}\right)$ is nef. Now restrict to the initial degeneration but over $\mathbb{D}^{\prime}:(W \subset \mathcal{W}) \rightarrow\left(0 \in \mathbb{D}^{\prime}\right)$. Say that $\Gamma_{t}$ is a $(-1)$-curve in some fiber $W_{t}$ of $(W \subset \mathcal{W}) \rightarrow\left(0 \in \mathbb{D}^{\prime}\right)$ which does not belong to the exceptional divisor given by the contractions used to obtain ( $W_{m} \subset$ $\left.\mathcal{W}_{m}\right) \rightarrow\left(0 \in \mathbb{D}^{\prime}\right)$. Then, its image $\Gamma^{\prime}{ }_{t}$ in the minimal model of $W_{t}$ (which is a fiber of $(W \subset \mathcal{W}) \rightarrow\left(0 \in \mathbb{D}^{\prime}\right)$ ) has $\Gamma^{\prime 2}=-1+\sum m_{i}^{2}$ and arithmetic genus $p_{a}\left(\Gamma^{\prime}{ }_{t}\right)=\sum \frac{m_{i}\left(m_{i}-1\right)}{2}$, for some integers $m_{i} \geq 0$, and so the intersection between $\Gamma^{\prime}{ }_{t}$ and the canonical divisor is negative by adjunction, a contradiction. Therefore $\Gamma_{t}$ belongs to the exceptional divisor, and this completes the proof. \(\square\)

If $K_{X}$ is not nef, we run MMP [KM98] in the following way. First, following [KM98, Thm.3.7] for example, there is a $K_{X}$-extremal rational curve $\Gamma$ (with $K_{X} \cdot \Gamma<0$ ). We have three options:
(I) If $\Gamma^{2}>0$, then $\operatorname{Pic}(X)$ has rank 1 and $-K_{X}$ is ample [KK94, 2.3.3]. Hence $-K_{X_{t}}$ is ample for any $t$ [KM98, Prop.1.41], and so $X_{t}$ is rational for any $t$. Moreover, the rank 1 condition implies that $e\left(X_{t}\right)=$ 3 for all $t$, and so $X_{t}$ is isomorphic to $\mathbb{P}^{2}$. This type of degenerations of $\mathbb{P}^{2}$ were classified in [Man91, HP10]. According to [HP10, Cor.1.2], $X$ is a $\mathbb{Q}$-Gorenstein deformation of a weighted projective plane $\mathbb{P}(a, b, c)$ where $(a, b, c)$ satisfies the Markov equation $a^{2}+b^{2}+c^{2}=3 a b c$. In the next section we say more on those degenerations.
(II) If $\Gamma^{2}=0$, then there is a fibration $h: X \rightarrow B$ with irreducible fibers and general fiber isomorphic to $\mathbb{P}^{1}$ [KK94, 2.3.3]. Let $\tilde{h}: \tilde{X} \rightarrow T$ be the corresponding fibration on the minimal resolution $\tilde{X}$ of $X$. Then, over a $b \in B$ where the fiber has a Wahl singularity, the fiber in $\tilde{X}$ has two possible configuration types; see [HP10, Prop.7.4]. It is a simple check that none of them is possible when the singularities are of Wahl type. Therefore, $(X \subset \mathcal{X}) \rightarrow(0 \in \mathbb{D})$ is a smooth deformation of a geometrically ruled surface $X$.
(III) If $\Gamma^{2}<0$, then we can apply to $(X \subset \mathcal{X}) \rightarrow(0 \in \mathbb{D})$ a birational transformation defined by an extremal nbhd of type mk1A or mk2A of flipping or divisorial type; see [HTU13, Thm.5.3]. After that we arrive to another W -surface $\left(X^{+} \subset \mathcal{X}^{+}\right) \rightarrow(0 \in \mathbb{D})$. The fibers of $\mathcal{X} \rightarrow \mathbb{D}$ have changed in one of the following ways:
(W-blow-down) In the divisorial type, we have a birational morphism $X \rightarrow X^{+}$contracting the curve $\Gamma=\mathbb{P}^{1}$ to a Wahl singularity. The minimal resolution of this Wahl singularity is obtained resolving minimally $X$ for singularities on $\Gamma$ and contracting the proper transform of $\Gamma$ and subsequent (-1)-curves (see [HTU13] or [Urz13, §1] for
the numerics). The birational morphism $X_{t} \rightarrow X_{t}^{+}$for $t \neq 0$ is just the blow down of one $(-1)$-curve. The inverse of a W-blow-down will be called a $W$-blow-up. We notice that over the Wahl singularity of $X^{+}$ we can have infinitely many W-blow-ups $X$. If the Wahl singularity in $X^{+}$is $\frac{1}{\delta^{2}}(1, \delta a-1)$, then the new Wahl singularities (one or two) appearing in $X^{+}$are of the type $\frac{1}{n_{i}^{2}}\left(1, n_{i} a_{i}-1\right)$ where $n_{i}=\delta n_{i-1}-n_{i-2}$ and $a_{i}=\delta a_{i-1}-a_{i-2}$ where $\left(n_{0}, a_{0}\right)=(0,1)$ and $\left(n_{1}, a_{1}\right)=(\delta, a)$ (see [HTU13] or [Urz13, §1]). When two singularities appear, then the numbers for the Wahl singularities are $\left(n_{i}, a_{i}\right)$ and $\left(n_{i+1}, a_{i+1}\right)$.
(W-flip) In the flipping type, the birational transformation $X \rightarrow$ $X^{+}$is described in [HTU13] (see also [Urz13, §1]). Roughly it is a minimal resolution of $X$ of the singularities contained in $\Gamma$, followed by blow downs and ups in the total transform of $\Gamma$, finishing with a contraction of two, one or none chain of rational curves. The numerical rules are in [HTU13] (see also [Urz13, §1]). Of course, the birational map $X_{t} \rightarrow X_{t}^{+}$is an isomorphism for $t \neq 0$.

Remark 2.4. There are constraints for anti-W-flips and W-blow-ups. Anti-W-flips for $\left(X^{+} \subset \mathcal{X}^{+}\right) \rightarrow(0 \in \mathbb{D})$, which locally above 0 is the deformation of an extremal $P$-resolution (see [HTU13, §4]), only exist for certain deformations. (For the precise statement see [HTU13, Cor.3.23]) See Example 3.26 in [HTU13] where the anti-flip is not an anti-W-flip. One can produce a similar example in the case of divisorial contractions, using a $\mathbb{Z}_{6}$-quotient of a simple elliptic singularity, whose minimal resolution is a union of 4 smooth rational curves $E_{1}, E_{2}, E_{3}$, and $F$ so that the $E_{i}$ are disjoint, each meets the curve $F$ transversally at a single point, and $E_{1}^{2}=-2, E_{2}^{2}=-3, E_{3}^{2}=-6$, and $F^{2}=$ -2. Similarly to [HTU13, Example 3.26], here one attaches a (-1)-curve transversal at one point of $E_{1}$ to define a canonical (nonterminal) extremal neighborhood. The Wahl singularity in $X^{+}$is $\frac{1}{9}(1,2)$.

When we apply (III) above, we have that either the Picard number of $X$, or the indices of some of its singularities strictly decreases. Thus it ends after finitely many steps with a W-surface as in (I) or (II), or with $K_{X}$ nef.

Definition 2.5. Given a W-surface, a minimal model of it is a minimal W-surface obtained by applying W-blow-downs and W-flips.

Proposition 2.6. A minimal model is unique.
Proof. Assume there are two minimal models $X_{m 1}$ and $X_{m 2}$. We have a birational map $g: \mathcal{X}_{m 1} \rightarrow \mathcal{X}_{m 2}$. Then, since the $\mathcal{X}_{m i}$ are $\mathbb{Q}$-factorial normal analytic 3-folds with terminal singularities and $K_{\mathcal{X}_{m i}}$ nef, we
know that $g$ can be written as composition of analytic flops [Flops, Thm.4.9]. Let $g^{\prime}: \mathcal{X}_{m 1} \rightarrow \mathcal{X}^{\prime}$ be the first flop. So, we have a small contraction $c: \mathcal{X}_{m 1} \rightarrow \mathcal{Y}$ over $\mathbb{D}$ such that $K_{X_{m 1}} \cdot C=0$ for the curves $C$ contracted by $c$ to $y \in \mathcal{Y}$. By [Ko91, Thm.2.2.2], the singularity $y \in \mathcal{Y}$ is terminal, and by [KSB88, Thm.5.3] we obtain that $y \in Y$ is a T-singularity, where $Y$ is the special fiber of $\mathcal{Y} \rightarrow \mathbb{D}$. Locally $X_{m 1} \rightarrow Y$ gives an M-resolution of $y \in Y$ and they are unique [BC94]. Notice that for the contraction $\mathcal{X}^{\prime} \rightarrow \mathcal{Y}$ we have the same situation, with same singularities. Therefore $g^{\prime}$ is an isomorphism, and so $g$. \(\square\)

In the previous lemma, $\mathbb{Q}$-factoriality for $\mathcal{X}$ was crucial. For example, take a rational elliptic surface with a multiplicity two fiber. Assume it has an $I_{2}$ fiber (nodal rational curve). We blow up its two nodes and contract the two (-4)-curves. One can show that there are $\mathbb{Q}$ -Gorenstein smoothings and for any we have a minimal W-surface (a general fiber is an Enriques surface, see [Urz13, Sect.5]). Each of the two images of the (-1)-curves from the nodes of $I_{2}$ gives two different ways to contract, but these two contractions are not related by a flop. The $\mathbb{Q}$-Gorenstein smoothing of the T-singularity [3, 3] gives a 3-fold which is not $\mathbb{Q}$-factorial.

If the minimal model has $K_{X}^{2}>0$, then we also have (unique) canonical model. (This is [Urz13, Lemma3.1].)

Proposition 2.7. Let $X$ be a minimal $W$-surface with $K_{X}^{2}>0$. Then, its canonical model $\left(X_{\text {can }} \subset \mathcal{X}_{\text {can }}\right) \rightarrow(0 \in \mathbb{D})$ has $X_{\text {can }}$ projective surface with only $T$-singularities. This is, it has Du Val singularities or cyclic quotient singularities $\frac{1}{d n^{2}}(1, d n a-1)$ with $\operatorname{gcd}(n, a)=1$.

Proof. We know there is $\left(X_{\text {can }} \subset \mathcal{X}_{\text {can }}\right) \rightarrow(0 \in \mathbb{D})$; cf. [KM98]. We have a birational morphism $\mathcal{X} \rightarrow \mathcal{X}_{\text {can }}$ over $\mathbb{D}$ such that $K_{\mathcal{X}_{\text {can }}}$ is $\mathbb{Q}$ -Cartier and ample. Notice that $X_{\text {can }}$ has log terminal singularities because $X$ has [KM98, pp.102-103]. The singularities of $X_{\text {can }}$ must be T-singularities by [KSB88, §5.2]. \(\square\)

\section*{3. Birational $\mathbb{Q}$-Gorenstein smoothings}

Let $X$ be a W-surface. Why do these smooth projective surfaces $X_{t}$ degenerate to $X$ ? We remark that in this type of degeneration there are no vanishing cycles. One can find an explanation when the general fiber has Kodaira dimension 0 and 1 in [Kaw92, §4]. When $X$ is indeed singular, this has to do with collisions of special fibers on an elliptic fibration of $X_{t}$. Also, there is a general discussion for $q=p_{g}=0$ surfaces in [Hack13] through certain exceptional vector bundles. Here we describe the situation when a resolution of $X$ and $X_{t}$ have the same
plurigenera. In particular, when they are actually birational. This happens for example with the surfaces in [Man91, HP10], and also in many examples of stable surfaces in the KSBA compactification of the moduli space of surfaces of general type; see [Urz13]. We will work with the later at the end of this article.

The claim is: any such W-surface comes from a smooth W-surface, after applying W-blow-downs, and W-flips. Thanks to the MMP described in §2 and a result of Kawamata [Kaw92, Lemma2.4], the only nontrivial case is degenerations of $\mathbb{P}^{2}$. We work out that now.

Let $\mathbb{F}_{m}$ be the Hirzebruch surface with a smooth rational curve $\Gamma_{m}$ with $\Gamma_{m}^{2}=-m$. Let $(0 \in \mathbb{D})$ be a smooth analytic germ of curve. We consider three situations $m=3,5,7$ :
\begin{itemize}
\item[(dm)] A W-surface with $X=\mathbb{F}_{m}, X_{t}=\mathbb{F}_{1}$ for $t \neq 0$, and the (-1)curve of $\mathbb{F}_{1}$ degenerates to $\Gamma_{m}+\sum_{i=1}^{(m-1) / 2} F_{i}$, where $F_{i}$ are distinct fibers of $\mathbb{F}_{m} \rightarrow \mathbb{P}^{1}$.
\end{itemize}

Theorem 3.1. Let $X$ be a $W$-surface with general fiber $\mathbb{P}^{2}$. Then, after applying one $W$-blow-up and finitely many $W$-flips, this $W$-surface becomes the $W$-surface in (dm) for some $m$.

The sequence of W-flips is a guided process as we will see in the proof. For the inverse construction, we remark that anti-W-flips are not automatic from the corresponding "local" extremal P-resolution, they only exist for certain deformations in the deformation space of this P-resolution (see [HTU13]). Moreover, for a given a P-resolution, there are in general infinitely many combinatorial choices for an anti-flip.

First we recall Manetti's [Man91, Thm.18]. Let $X$ be a W-surface with general fiber $\mathbb{P}^{2}$, let $\delta: S \rightarrow X$ be its minimal resolution. Then there is a rational fibration $p: S \rightarrow \mathbb{P}^{1}$, such that the exceptional set of $\delta$ is contained in either 0, or 1, or 2 singular fibers union one section $\Gamma$. Moreover, there is a birational morphism $\mu: S \rightarrow \mathbb{F}_{m}$ contracting the curves in the before mentioned special 1 or 2 fibers such that $\Gamma$ does not intersect the exceptional loci of $\mu$, the image of $\Gamma$ is the negative curve of $\mathbb{F}_{m}$, and $m$ is either 4, 7, or 10 in correspondence to the number of special fibers 0, 1, 2.

First W-blow-up: Let us consider a section of $\mathcal{X} \rightarrow \mathbb{D}$ intersecting $X$ at a point which is contained in a nonsingular fiber of $p: S \rightarrow \mathbb{P}^{1}$. Blow this section up, let $X_{0}$ be this new W-surface whose general fiber is now $\mathbb{F}_{1}$. If $S_{0}$ is the blow up at the point of $S$, then we have created a $(-1)$-curve intersecting $\Gamma$ at one point. This is a flipping mk1A for the Wahl singularity which includes $\Gamma$ in its minimal resolution. We apply the corresponding W-flip. Notice that $\Gamma^{2} \leq-4$, and so for the new W-surface $X_{1}$ we have a minimal resolution $\delta_{1}: S_{1} \rightarrow X_{1}$ with the
same properties as for $\delta: S \rightarrow X$ but now $m$ is either 3, 6, or 9 (in correspondence to the number of special fibers 0, 1, 2).

The birational operations we are going to use are W-flips with flipping curves always in the special (singular) fibers of $p: S \rightarrow \mathbb{P}^{1}$. For this we need the following.

A type of surface will be a W-surface $X_{i}$ with four distinguished rational smooth curves $A, B, C$, and $F$ so that the minimal resolution $\delta_{i}: S_{i} \rightarrow X_{i}$ has a rational fibration $p_{i}: S_{i} \rightarrow \mathbb{P}^{1}$ with at most two singular fibers (as the one above), where $A$ is a (-1)-curve in one singular fiber, $B$ and $C$ are in the other, and $F$ is a general smooth fiber. In addition they must satisfy:
\begin{itemize}
\item[(1)] $B \cdot K_{X_{i}}<0$ and $C \cdot K_{X_{i}}>0$.
\item[(2)] We can contract $B$ in $X$ and $C$ in $X$ to cyclic quotient singularities.
\item[(3)] The special section $\Gamma$ of $S_{i}$ appears in one of the minimal resolutions of the cyclic quotient singularities in (2) with $\Gamma^{2} \leq-3$.
\end{itemize}

The conditions (1) and (2) ensure the existence of an mk1A or mk2A of flipping type for the curve $B$. Notice that, in our case, it is of flipping type since the (-1)-curve of the general fiber $\mathbb{F}_{1}$ degenerates to an effective $\mathbb{Q}$-divisor in $X$ containing $F$. The condition (3) says that we preserve the fibration of $S_{i}$, and so the strict transform of $F$ after the flip is again an $F$ for $S_{i+1}$. In particular we are flipping curves only in the two special fibers.

Before continuing with the proof, we run the MMP of Theorem 3.1 in an example.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/a7e11a57-62e4-4b88-b77b-413295961562-10.jpg?height=620&width=801&top_left_y=1665&top_left_x=661}
\captionsetup{labelformat=empty}
\caption{Figure 1. Running Theorem 3.1 on an example}
\end{figure}

Example 3.2. We take the example in [Man91, p.117]. There $X$ has three Wahl singularities $\frac{1}{4}(1,1), \frac{1}{25}(1,4)$, and $\frac{1}{29^{2}}(1,29 \cdot 21-1)$. The minimal resolution $\delta: S \rightarrow X$ gives the fibration $p: S \rightarrow \mathbb{P}^{1}$ with the exceptional divisor of $\delta$ contained in two fibers and one section $\Gamma$, where $\Gamma^{2}=-10$. In the upper-half corner of Figure 1, we have the dual graph of the exceptional curves of $\delta$ together with two (-1)-curves (one in each of the two fibers), and a fiber. The ● represent the curves in the exceptional divisor, and the numbers are the self-intersections of the curves (no number means -1). As in [HTU13, Urz13], the graphdiagram in Figure 1 shows how we run the MMP in Theorem 3.1. First, we have the W-blow-up of a section of the W-surface $X$ (i.e. of the 3-fold) which intersects a point of the distinguished fiber not in $\Gamma$. The first arrow indicates that birational transformation on the surface $S$. After that, we perform seven W-flips. The $K$-negative curves are marked with a $\ominus$, the $K$-positive flipped ones with a ⊕. After the first flip, we see the curves $A, B, C, F$ above as some permutation of the elements in $\{\circ, \circ, \oplus, \ominus\}$.

Lemma 3.3. Assume that $X_{i}$ is a $W$-surface of type coming from $W$-flips starting with Manetti's situation above. Then, the $W$-flip of $B$ in the $W$-surface $X_{i}$ produces a $W$-surface $X_{i+1}$ of type.

Proof. In $X_{i+1}$, let $A$ be the strict transform of $A$, same for $C$, and let $B$ be the flipped $B$. So we know that $B \cdot K_{X_{i+1}}>0$. We notice that (3) is clear from the Manetti's assumptions on $S_{i} \rightarrow \mathbb{P}^{1}$ and the way a W-flip is performed on $X_{i}$ (it is the contraction of at most two Wahl chains of a blow-up on consecutive nodes from the minimal resolution of the corresponding cyclic quotient singularity). Now $B$ could be in the same singular fiber (in $S_{i+1}$ ) than either $A$ or $C$. We rename curves so that the flipped curve $B$ is $C$, the curve in the same singular fiber than the flipped curve is $B$, and the curve in the other singular fiber is $A$. In this way, $A$ has to be a (-1)-curve in the minimal resolution $S_{i+1}$.

To prove (1), we need to show $B \cdot K_{X_{i+1}}<0$. For this we use that $X_{i+1}$ has Picard number 2. Notice that because of (3), $F \cdot K_{X_{i+1}}<0$, and so $F \equiv u B+v C$ with $u, v \in \mathbb{Q}$. We have two cases: $A \cdot B=0$ or $A \cdot C=0$. Say $A \cdot C=0$, then $A \cdot B>0$ and so $F \cdot A=u B \cdot A$ implies $u>0$. Now $u B^{2}+v C \cdot B=F \cdot B$ implies so $v>0$. Therefore $B \cdot K_{X_{i+1}}<0$. For the other case $A \cdot B=0$, we do similar intersections to obtain the same result, so (1) is true. \(\square\)

Proof of Theorem 3.1. Notice that the $X_{1}$ above (obtained from Man91, Thm.18] applying one W-blow-up and one W-flip) is of type. Then
we apply the W-flips for the W-surfaces $X_{i}$ of type applying previous lemma. They have to terminate on a nonsingular $F_{n} \mathrm{~W}$-surface for some $n$. Notice that $n=3,5,7$ according to the number of special fibers. Also, the (-1)-curve of the general fiber $\mathbb{F}_{1}$ degenerates to the claimed curves in $\mathbb{F}_{n}$. \(\square\)

Let us denote by $P_{m}(Z):=\operatorname{dim}_{\mathbb{C}} H^{0}\left(Z, m K_{Z}\right)$ the plurigenera of a nonsingular projective surface $Z$.

Theorem 3.4. Let $X$ be a $W$-surface, and let $\widetilde{X}$ be a resolution of the singularities of $X$. Assume that $P_{m}(\widetilde{X})=P_{m}\left(X_{t}\right)$ for $t \neq 0$ and $m \gg 0$. Then this $W$-surface can be constructed from a smooth $W$ surface applying a finite number of $W$-blow-downs (or -ups) and anti-W-flips.

Proof. We apply the MMP of §2 to this W-surface. If we arrive to (II), then we are done. If we arrive to (I), then we are done by Theorem 3.1. Otherwise, after finitely many W-flips or W-blow-downs, we obtain the W -minimal model $X^{\prime}$ of $X$. If the W -minimal model is smooth, then we are done. If not, by [Kaw92, Lemma2.4], there are positive integers $m_{1}$ and $m_{2}$ such that
$$P_{m}\left(X_{t}\right)>P_{m}\left(\widetilde{X^{\prime}}\right)$$
for $t \neq 0$ holds for positive integers $m$ with $m_{1}$ dividing $m$ and $m_{2}<m$, where $\widetilde{X^{\prime}}$ is a resolution of $X^{\prime}$. But $P_{m}(\widetilde{X})=P_{m}\left(\widetilde{X^{\prime}}\right)$ and $P_{m}\left(X_{t}\right)=$ $P_{m}\left(X_{t}^{\prime}\right)$ for $t \neq 0$ and all $m$, because plurigenera is a birational invariant between nonsingular varieties. By assumption $P_{m}(\widetilde{X})=P_{m}\left(X_{t}\right)$ for $t \neq 0$ and $m \gg 0$, and so we have a contradiction. Therefore $X^{\prime}$ must be nonsingular. \(\square\)

Corollary 3.5. Let $X$ be a $W$-surface such that $X$ is birational to $X_{t}, t \neq 0$. Then this $W$-surface can be constructed from a smooth $W$-surface applying a finite number of $W$-blow-downs (or -ups) and anti- $W$-flips. \(\square\)

The difficulty of the $\mathbb{Q}$-Gorenstein smoothings in Theorem 3.4 relies mainly on W-flips and W-blow-downs. As we have noticed before, there are choices when one performs inverses of them. Also, their description uses an intricate but explicit combinatoric through continued fractions (cf. [HTU13]). On the other hand, the degenerations in Theorem 3.4 produce interesting degenerations of curves in the general fiber $X_{t}$. This is the topic of the next two sections.

\section*{4. Degeneration of curves}

Here is the situation. Let $X$ be a W -surface. Let $\Gamma_{t}$ be an irreducible curve in the general fiber $X_{t}$. This curve deforms to a divisor $\Gamma_{0}$ in $X$. If $X^{\prime}$ a W -minimal model of $X$, then we want to know explicitly about the degeneration of $\Gamma_{t}^{\prime}$ into $\Gamma_{0}^{\prime}$ (the total transforms of $\Gamma_{t}$ and $\Gamma_{0}$ respectively). Moreover, if $X$ and $X_{t}$ are birational, we can get a nonsingular $X^{\prime}$ (Corollary 3.5) and typically we would have $X^{\prime}$ isomorphic to $X_{t}^{\prime}$. This suggests we can think about this deformation as an explicit degeneration of $\Gamma_{t}^{\prime}$ in $X^{\prime}$. At the end of this section we will show examples using curves in $\mathbb{P}^{2}$. In the next section we will see how these sort of examples show up in the Kollár-Shepherd-Barron-Alexeev boundary of the moduli space of surfaces of general type.

The set-up: Let $X$ be a W-surface, and let $\Gamma_{t}$ be an irreducible curve in $X_{t}$, for $t \neq 0$, degenerating to a divisor $\Gamma_{0}$ in $X$. This is, we have a divisor $\Gamma$ in $\mathcal{X}$ such that $\left.\Gamma\right|_{X_{t}}=\Gamma_{t}$. We write $\Gamma_{0}=\sum_{i=0}^{s} \alpha_{i} D_{i}$ where $D_{i}$ are distinct irreducible curves and $\alpha_{i} \in \mathbb{Z}_{\geq 0}$.

Let $\left(E^{-} \subset X \subset \mathcal{X}\right) \rightarrow(Q \in Y \subset \mathcal{Y})$ be a mk1A or mk2A. Assume $D_{0}=E^{-}$. If it is of divisorial type, then the W-blow-down produces a W-surface $X^{\prime}$ with a divisor $\Gamma^{\prime}$ image of $\Gamma$, such that $\Gamma_{t}^{\prime}$ is an irreducible curve for $t \neq 0$ (or a point if $\Gamma$ is the exceptional divisor), and $\Gamma_{0}^{\prime}=$ $\sum_{i=1}^{s} \alpha_{i} D_{i}^{\prime}$ where $D_{i}^{\prime}$ is the image of $D_{i}$.

If it is of flipping type, then the W-flip produces a W-surface $X^{\prime}$ with a divisor $\Gamma^{\prime}$ proper transform of $\Gamma$, such that $\Gamma_{t}^{\prime}$ is isomorphic to $\Gamma_{t}$ for $t \neq 0$, and $\Gamma_{0}^{\prime}=\sum_{i=1}^{s} \alpha_{i} D_{i}^{\prime}+\beta E^{+}$where $D_{i}^{\prime}$ is the proper transform of $D_{i}, E^{+}$is the flipping curve, and $\beta \in \mathbb{Z}_{\geq 0}$. Since $\mathcal{X}^{\prime}$ is $\mathbb{Q}$-factorial and this is a flip, we have the numerical equivalence
$$\sum_{i=1}^{s} \alpha_{i}\left(D_{i}^{\prime} \cdot K_{X^{\prime}}\right)+\beta\left(E^{+} \cdot K_{X^{\prime}}\right)=\Gamma_{0}^{\prime} \cdot K_{X^{\prime}}=\Gamma_{t}^{\prime} \cdot K_{X_{t}^{\prime}}=\Gamma_{t} \cdot K_{X_{t}}$$
from where one calculates $\beta$. We notice that $\beta=0$ if and only if $\Gamma_{0} \cap E^{-}=\emptyset$. The following is a frequent case.

Proposition 4.1. Assume that in the situation above we have an $m k 1 A$ of flipping type so that $E^{-}$is intersecting at one point one of the ends of the minimal resolution of the corresponding Wahl singularity. Let $\Gamma_{0}=\sum_{i=1}^{s} \alpha_{i} D_{i}$ with $D_{i} \neq E^{-}$for all $i, D_{1} \cdot E^{-}=1$, and $D_{i} \cdot E^{-}=0$ for $i \geq 2$ (see Figure 2). Then $\beta=\alpha_{1}$.

Proof. Let $\frac{1}{n^{2}}(1, n a-1)$ be the Wahl singularity, and let $E_{1}, E_{2}, \ldots, E_{m}$ be the chain of exceptional curves in the minimal resolution as shown in Figure 2. Thus $E_{1} \cdot E^{-}=1$, where as always $E^{-}$is the strict transform of $E^{-}$, so it is a (-1)-curve. Assume that $E_{1}, \ldots, E_{r}$ are all

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/a7e11a57-62e4-4b88-b77b-413295961562-14.jpg?height=163&width=799&top_left_y=400&top_left_x=662}
\captionsetup{labelformat=empty}
\caption{Figure 2. Frequent case}
\end{figure}
(-2)-curves (this set may be empty). Then either $E_{m}^{2}=-(r+2)$ if $r \neq m-1$, or $E_{m}^{2}=-(r+4)$ if $r=m-1$. The W-flip in this case gives $E^{+}=E_{m}$ with either one Wahl singularity on it if $r \neq m-1$ having the Hirzebruch-Jung continued fraction $\left[-E_{r+1}^{2}-1,-E_{r+2}^{2}, \ldots,-E_{m-1}^{2}\right]$, or none [Urz13, Prop.2.8]. Let $a$ and $b$ the discrepancies $(0<a, b<1)$ of $E_{r+1}$ and $E_{m-1}$ for the singularity of $X^{\prime}$ in $E^{+}$. Then $K_{X^{\prime}} \cdot D_{1}^{\prime}=$ $K_{X} \cdot D_{1}-(r+1)+a$ and $K_{X^{\prime}} \cdot E^{+}=r+b$ if $X^{\prime}$ singular, and so in this case
$$\beta=\frac{\alpha_{1}(r+1-a)}{r+b}=\alpha_{1}$$
because $a+b=1$. When $X^{\prime}$ is smooth at $E^{+}, K_{X^{\prime}} \cdot D_{1}^{\prime}=K_{X} \cdot D_{1}-(r+1)$ and $K_{X^{\prime}} \cdot E^{+}=r+1$, so $\beta=\alpha_{1}$. \(\square\)

We will finish this section with two examples derived from vanishing of certain cohomology group.

Proposition 4.2. Let $Z$ be a nonsingular projective surface. Let $\mathcal{W}_{1}, \ldots$, $\mathcal{W}_{r}$ be $r$ chains of $\mathbb{P}^{1}$ 's in $Z$ so that $\mathcal{W}_{i}$ is the exceptional divisor of a Wahl singularity, and $\mathcal{W}_{i} \cap \mathcal{W}_{j}=\emptyset$ for $i \neq j$. Assume there is a curve $\Gamma_{0}=\mathbb{P}^{1}$ in $Z$ such that $\Gamma_{0} \cap \mathcal{W}_{i}=\emptyset$ for all $i$, and
$$H^{2}\left(Z, T_{Z}\left(-\log \left(\mathcal{W}_{1}+\ldots+\mathcal{W}_{r}+\Gamma_{0}\right)\right)\right)=0 .$$
Then there is a $W$-surface $X$ such that $X$ is the contraction of all $\mathcal{W}_{i}$ 's, and there is a divisor $\Gamma \subset \mathcal{X}$ with $\left.\Gamma\right|_{X_{t}}=\mathbb{P}^{1}$ and $\left.\Gamma\right|_{X}=\Gamma_{0}$.
Proof. We first blow-up distinct points on $\Gamma_{0}$ so that $\Gamma_{0}^{2} \leq-2$, if necessary. By the adding-deleting (-1)-curves procedure (for instance, see [PSU13, §4]), we have again $H^{2}\left(Z^{\prime}, T_{Z^{\prime}}\left(-\log \left(\mathcal{W}_{1}+\ldots+\mathcal{W}_{r}+\Gamma_{0}\right)\right)\right)=0$ where $Z^{\prime}$ is the blown-up surface, and $\Gamma_{0}$ is the proper transform of $\Gamma_{0}$. The configurations $\mathcal{W}_{1}, \ldots, \mathcal{W}_{r}, \Gamma_{0}$ correspond to exceptional divisors of cyclic quotient singularities, and they can be contracted to a projective surface $X^{\prime}$. By [LP07, pp.487-488], we have that $H^{2}\left(Z^{\prime}, T_{Z^{\prime}}\left(-\log \left(\mathcal{W}_{1}+\ldots+\mathcal{W}_{r}+\Gamma_{0}\right)\right)\right)=0$ implies $H^{2}\left(X^{\prime}, T_{X^{\prime}}\right)=0$, and that implies no-local-to-global obstructions to deform $X^{\prime}$. In particular, we can glue local $\mathbb{Q}$-Gorenstein smoothings for the Wahl singularities $\mathcal{W}_{i}$, and keep the singularity corresponding to $\Gamma_{0}$. Let $\mathcal{X}^{\prime} \rightarrow \mathbb{D}$ be the corresponding deformation. Since the deformation for the singularity given by $\Gamma_{0}$ is trivial, we can resolve it simultaneously, obtaining
$\mathcal{X}^{\prime \prime} \rightarrow \mathbb{D} \mathbb{Q}$-Gorenstein smoothing of $X^{\prime \prime}$ (which is $X^{\prime}$ with the singularity associated to $\Gamma_{0}$ minimally resolved). The 3 -fold $\mathcal{X}^{\prime \prime}$ has a divisor $\Gamma^{\prime \prime}$ defined by the curve $\Gamma_{0}$. The $(-1)$-curves in $X^{\prime}$ corresponding to the initial blow-up of $W$ intersect $\Gamma_{0}$ at one point. All of them are now contracted to finally obtain the W-surface $X$ with the claimed properties. \(\square\)

Proposition 4.3. Let $\sum_{i=1}^{n} C_{i}$ be a SNC divisor (only nodes as singularities, $C_{i}$ nonsingular curves) in a nonsingular projective surface $W$ with $H^{0}\left(W, \Omega_{W}^{1}\right)=0$. Assume that there is $1<m \leq n$ such that $C_{1}+\ldots+C_{m} \sim-K_{W}$, and the curves $\left\{C_{m+1}, \ldots, C_{n}\right\}$ are numerically independent. ( $m=n$ means no second requirement.) Then
$$H^{2}\left(W, T_{W}\left(-\log \left(C_{1}+\ldots+C_{n}\right)\right)\right)=0 .$$
Proof. By Serre's duality, we need to prove that
$$H^{0}\left(W, \Omega_{W}^{1}\left(\log \left(C_{1}+\ldots+C_{n}\right)\right) \otimes \mathcal{O}_{W}\left(K_{W}\right)\right)=0 .$$
Notice that we have the natural
$$\Omega_{W}^{1}\left(\log \left(\sum_{i=j}^{n} C_{i}\right)\right) \otimes \mathcal{O}_{W}\left(\sum_{i=1}^{j-1} C_{i}+K_{W}\right) \hookrightarrow \Omega_{W}^{1}\left(\log \left(\sum_{i=j+1}^{n} C_{i}\right)\right) \otimes \mathcal{O}_{W}\left(\sum_{i=1}^{j} C_{i}+K_{W}\right),$$
and so by the hypothesis $C_{1}+\ldots+C_{m} \sim-K_{W}$, we want to show $H^{0}\left(W, \Omega_{W}^{1}\left(\log \left(C_{m+1}+\ldots+C_{n}\right)\right)\right)=0$. The long exact sequence in cohomology of the residue short exact sequence
$$0 \rightarrow \Omega_{W}^{1} \rightarrow \Omega_{W}^{1}\left(\log \left(C_{m+1}+\ldots+C_{n}\right)\right) \rightarrow \bigoplus_{i=m+1}^{n} \mathcal{O}_{C_{i}} \rightarrow 0$$
gives the Chern class map $\bigoplus_{i=m+1}^{n} H^{0}\left(C_{i}, \mathcal{O}_{C_{i}}\right) \rightarrow H^{1}\left(W, \Omega_{W}^{1}\right)$ (cf. [GH78, pp.454-462]), and since we are assuming that $\left\{C_{m+1}, \ldots, C_{n}\right\}$ are numerically independent, this map is injective. The extra assumption $H^{0}\left(W, \Omega_{W}^{1}\right)=0$ finishes the proof. \(\square\)

We present two examples to illustrate.
Example 4.4. This is a way to produce a degeneration of a nodal rational plane curve of degree $d$ to $d$ lines in general position. Let $\left\{L_{1}, \ldots, L_{d}\right\}$ be $d$ lines in general position in $\mathbb{P}^{2}$. We assume $d \geq 6$ (this allows as a short uniform argument, this can be adapted for $d<6$ ). We blow-up $\sigma: W \rightarrow \mathbb{P}^{2}$ all the $\binom{d}{2}$ intersection points of this line arrangement. Let $E_{1}, E_{2}, E_{3}$ be the exceptional curves over the three nodes of the triangle $L_{1}, L_{2}, L_{3}$. Then $-K_{W} \sim E_{1}+E_{2}+E_{3}+L_{1}+L_{2}+L_{3}$ and $\left\{L_{4}, \ldots, L_{d}\right\}$ are numerically independent. Thus by Prop. 4.3, $H^{2}\left(W, T_{W}\left(-\log \left(E_{1}+E_{2}+E_{3}+L_{1}+\ldots+L_{d}\right)\right)\right)=0$. We can delete the
$(-1)$-curves $E_{1}, E_{2}, E_{3}$ to have $H^{2}\left(W, T_{W}\left(-\log \left(L_{1}+\ldots+L_{d}\right)\right)\right)=0$. Notice that $L_{i}^{2}=2-d \leq-4$. Let $F_{i}$ be the exceptional curve between $L_{1}$ and $L_{i}, i=2, \ldots, d$. We blow-up $d-6$ times over $L_{1} \cap F_{i}$ to obtain a Wahl configuration $\mathcal{W}_{i}[2, \ldots, 2, d-2]$ for each $i$. Adding-deleting (-1)-curves (see [PSU13, §4]) keeps obstruction zero. If $L_{1}=: \Gamma_{0}$, then we are in the situation of Prop. 4.2, and so we have such a W-surface $X$. The surface $X$ has $d-1$ Wahl singularities of the same type. The curve $\Gamma_{0}$ is $D_{i}$ in Prop. 4.1. We perform $d-1$ W-flips using the $d-1$ (-1)-curves over the $L_{i} \cap F_{i}$ 's, obtaining a smooth W-surface $X^{\prime}$ with the $\Gamma_{t}=\mathbb{P}^{1}$ degenerating to $\sum_{i=1}^{d} L_{i}$. To obtain the planar degeneration, we blow-down the (-1)-curves corresponding to the $L_{i} \cap L_{j}$ with $i, j$ different than 1 . There are $\binom{d}{2}-(d-1)=\frac{(d-1)(d-2)}{2}$ of them. Each of them intersect $\sum_{i=1}^{d} L_{i}$ at two distinct points, and so the corresponding $(-1)$-curve and $\Gamma_{t}$ intersect t two distinct points, this is, each creates a node for $\Gamma_{t}$. After we blow down all of them, we arrive to $\mathbb{P}^{2}$, and we have the degeneration we wanted.

Example 4.5. Fix an integer $n \geq 1$. In this example we degenerate a rational curve of degree $3(n+1)$ with 9 singular points of multiplicity $n+1$ and one node to two general nodal cubics, one with multiplicity 1, and the other with $n$. We start with two such nodal cubics $C_{1}, C_{2}$. We blow up the 9 base points and the two nodes; let $Z$ be the surface. Let $E_{i}$ be the (-1)-curve from the node of $C_{i}$. Using similar arguments as in Prop. 4.3, we can show that $H^{2}\left(Z, T_{Z}\left(-\log \left(C_{1}+C_{2}\right)\right)\right)=0$. We now blow up $n-1$ times over one point of $C_{2} \cap E_{2}$ to obtain the Wahl configuration $[2, \ldots, 2, n+4]$ in a surface $Z^{\prime}$. Let $F_{1}=E_{2}, \ldots, F_{n-1}$ be the (-2)-curves in a chain, so $F_{1} \cap C_{2} \neq \emptyset$. Then $H^{2}\left(Z^{\prime}, T_{Z^{\prime}}\left(-\log \left(C_{1}+\right.\right.\right.$ $\left.\left.\left.C_{2}+F_{1}+\ldots+F_{n-1}\right)\right)\right)=0$. We contract $C_{2}+F_{1}+\ldots+F_{n-1}$ to obtain $X^{\prime}$, and use Prop. 4.2 with $\Gamma_{0}=C_{1}$ to produce a W-surface $X$ with the divisor $\Gamma$. We now W-flip one of the 9 exceptional curves of the 9 base points between $C_{1}$ and $C_{2}$, and then we W-flip $F_{n}, F_{n-1}, \ldots, F_{2}$ using the simple flips of Prop. 4.1 (see Figure 3).

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/a7e11a57-62e4-4b88-b77b-413295961562-16.jpg?height=288&width=990&top_left_y=2052&top_left_x=567}
\captionsetup{labelformat=empty}
\caption{Figure 3.}
\end{figure}

One can compute that $\Gamma_{t}$ degenerates to $C_{1}+n C_{2}+(n-1) F_{1}$. This corresponds to a nonreduced degeneration of $\Gamma_{t}$. For a model in $\mathbb{P}^{2}$ of this deformation, we blow-down $E_{1}, F_{1}$, and the 8 remaining (-1)-curves from the 9 base points. Using intersection numbers, we see that $E_{1}$ in $X_{t}$ is a (-1)-curve intersecting transversally at two points of $\Gamma_{t}$, and for the other 9 (-1)-curves (including $F_{1}$ ), we obtain exceptional (-1)-curves intersecting $\Gamma_{t}$ with multiplicity $n+1$. Hence in $\mathbb{P}^{2}$ the curve $\Gamma_{t}$ has degree $3(n+1)$ and the claimed multiplicities for its singularities.

\section*{5. Explicit rational examples of general type}

We are going to give four examples where birational $\mathbb{Q}$-Gorenstein deformations appear when studying the boundary of the KSBA compactification of the moduli space $\bar{M}$ of simply connected surfaces of general type with $p_{g}=0$ and $K^{2}=1$. We point out that the choice of the invariants is irrelevant for the techniques.
5.1. Irreducible septic associated to a $\frac{1}{36}(1,5)$. In this example we show how to find explicitly a curve in $\mathbb{P}^{2}$ associated to a boundary divisor in $\bar{M}$ which parametrizes rational surfaces with one fixed Wahl singularity. For that we use a further degeneration on two or more Wahl singularities; this is the case in all examples analyzed in [Urz13].

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/a7e11a57-62e4-4b88-b77b-413295961562-17.jpg?height=419&width=792&top_left_y=1491&top_left_x=665}
\captionsetup{labelformat=empty}
\caption{Figure 4. Elliptic fibration with singular fibers $I_{5}, I_{2}, 5 I_{1}$}
\end{figure}

Here we start with the example in [LP07, Fig.6]. We consider that example on a more general elliptic fibration. Let us take the plane configuration in Figure 4: $L_{1}, L_{2}, L_{3}, L$ are lines with a triple point $L \cap L_{1} \cap L_{2}$, and $C$ is a conic forming a triple point at $L_{1} \cap L_{3}$. All other intersections are general. The pencil $\left\{a \cdot C \cdot L+b \cdot L_{1} \cdot L_{2} \cdot L_{3}:[a, b] \in \mathbb{P}^{1}\right\}$ defines an elliptic fibration with singular fibers $I_{5}, I_{2}, 5 I_{1}$ as shown in Figure 4. In that figure we drew two $I_{1}$ 's and five sections which will be used later. Notice that they exists with the shown intersections. We
blow-up twelve times this elliptic fibration to obtain a surface $Z$ and the configuration in Figure 5. The corresponding exceptional divisors are $E_{1}, \ldots, E_{12}$, we blew-up in that order. The five Wahl configurations in [LP07, Fig.6] correspond to $S_{1}, L_{1}, R_{1}, L_{2}, L_{3}=[8,2,2,2,2]$ (numbers are the corresponding minus self-intersections), $F_{1}, E_{3}, E_{4}=[6,2,2]$, $F_{2}, E_{8}, E_{9}=[6,2,2], S_{2}=[4]$, and $C=[4]$. Let $\sigma: Z \rightarrow X$ be the contraction of these five configurations to a normal projective surface $X$ (with five Wahl singularities). As in [LP07], this surface $X$ has no local-to-global obstructions to deform, and $X$ has nef canonical class. Hence W-surfaces $X$ exist, and have general fiber a simply connected surface of general type with $K^{2}=1$ and $p_{g}=0$.

Let $X^{\prime}$ be the minimal resolution of the singularity [8, 2, 2, 2, 2] of $X$. Consider a W-surface $X^{\prime}$ keeping the configuration [8, 2, 2, 2, 2]. The contraction of this configuration in the general fiber gives a surface with one Wahl singularity in the corresponding boundary divisor of $\bar{M}$. We now perform W-flips on the W-surface $X^{\prime}$ to find the minimal model of its general fiber. It turns out to be rational, and so we instead find a way to blow-down enough (-1)-curves to arrive to $\mathbb{P}^{2}$, keeping track of the configuration [8, 2, 2, 2, 2]. Let $\Gamma_{t}$ be the (-8)-curve in this configuration.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/a7e11a57-62e4-4b88-b77b-413295961562-18.jpg?height=275&width=894&top_left_y=1405&top_left_x=614}
\captionsetup{labelformat=empty}
\caption{Figure 5.}
\end{figure}

We first flip the curve $E_{5}$ (in the threefold of the W-surface $X^{\prime}$ ). This curve is as in Prop. 4.1, and so the flipped W-surface $X^{\prime}$ (abuse of notation) has flipped curve $F_{1}$ and $X^{\prime}$ has only three singularities. Now we W-flip the curve $E_{10}$ producing an analog situation: $F_{2}$ is the flipped curve and we have two Wahl singularities $\frac{1}{4}(1,1)$. We now W-flip $E_{12}$ and then $E_{11}$, the resulting W-surface $X^{\prime}$ is now smooth. This shows that the general fiber is indeed rational. By a repeated use of Prop. 4.1, we compute that $\Gamma_{t}$ degenerates to
$$\Gamma_{0}=S_{1}+F_{1}+F_{2}+C+S_{2} .$$
The surface $X^{\prime}$ has $K_{X^{\prime}}^{2}=1-5=-4$, and to get into $\mathbb{P}^{2}$ is enough to blow-down 13 times (-1)-curves. In the W-surface $X^{\prime}$ this corresponds to trivial divisorial contractions driving the general fiber to $\mathbb{P}^{2}$ as well.

The 13 curves we are going to blow-down in $X^{\prime}$ are $S_{5}, L_{3}, L_{2}, R_{1}, L_{1}$, $E_{2}, E_{7}, S_{2}, C, S_{3}, S_{4}, E_{1}$, and $E_{6}$. Each of them induces a blow-down in the general fiber, whose exceptional divisors are shown in Figure 6, we use same letters. This is found by intersecting these curves with $\Gamma_{0}$, then we know the intersection with $\Gamma_{t}$. The curves $S_{2}$ and $C$ may be as in Figure 6 or tangent to the (-8)-curve (double points anyway).

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/a7e11a57-62e4-4b88-b77b-413295961562-19.jpg?height=301&width=799&top_left_y=724&top_left_x=662}
\captionsetup{labelformat=empty}
\caption{Figure 6.}
\end{figure}

We are now in good shape to blowing down the 13 divisors. The image of the configuration of curves in $X^{\prime}$ becomes two nodal cubics $F_{1}$ and $F_{2}$ together with a line $S_{1}$. The two cubics are tangent at two points $P$ and $Q$ with multiplicity 5 and 2, and the line passes through $P$ and $Q$ transversally to each cubic. All other intersections are nodes. For the image of $\Gamma_{t}$ we obtain an irreducible septic with 8 double points, and one $D_{10}$ singular point (i.e. locally of the type $\left\{x\left(y^{2}+x^{8}\right)=0\right\} \subset \mathbb{C}^{2}$ ).

Therefore, the degeneration in the boundary of $\bar{M}$ gives, up to birational (discrete) flips and divisorial contractions, a degeneration (continuous) of the above irreducible septic into the above reducible (but reduced) septic. The irreducible septic represents (up to birational transformations) a boundary divisor (of dimension 7) in $\bar{M}$ associated to the singularity [8, 2, 2, 2, 2].
5.2. Degree 15 curve for a $\frac{1}{16}(1,3)$ and nonreduced degeneration. In the previous example, and the examples below, we will see septics showing up. We chose those examples to put things simple, but naturally higher degree curves appear degenerating to a reducible septics with multiplicities on certain components. For instance, take the above example and work out the singularity [6, 2, 2] (for the [4] we do not obtain rational surfaces but Dolgachev $(2,3)$ surfaces; see [Urz13, Prop.2.3]). Say [6, 2, 2] is $F_{1}+E_{3}+E_{4}$. We do what we did above for [8, 2, 2, 2, 2] but now for [6, 2, 2]. Then, after some flips we get a smooth W-surface, and if we blow-down to $\mathbb{P}^{2}$ in the same way as before, we get an irreducible (rational) curve of degree 15. This curve, which is the image of the (-6)-curve of [6, 2, 2], degenerates to $3 S_{1}+F_{1}+3 F_{2}$,
this is, degenerates to the same septic configuration above (two nodal cubics and a line) but now with multiplicities.
5.3. One septic degeneration for two distinct deformations. Here we produce two distinct degenerations of stable surfaces in the boundary of $\bar{M}$ which correspond to the same degeneration of plane curves. This is, the continuous part could be seen as the same (but the discrete part (3-fold birational transformations) is of course different).

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/a7e11a57-62e4-4b88-b77b-413295961562-20.jpg?height=344&width=997&top_left_y=791&top_left_x=563}
\captionsetup{labelformat=empty}
\caption{Figure 7.}
\end{figure}

We start with a triangle $L_{1}, L_{2}, L_{3}$ and a general cubic passing transversally through $L_{1} \cap L_{2}$ as in Figure 7. The triangle and the cubic defines a pencil which induces an elliptic fibration with sections whose singular fibers are $I_{4}$, and $8 I_{1}$ 's. In Figure 7 we show the $I_{4}$, two chosen $I_{1}$ 's and 7 chosen sections. We blow-up on this configuration in two different ways, obtaining surfaces $Z_{i}$ with $i=1,2$. For $Z_{1}$ we blew-up 11 times, for $Z_{2} 13$ times. The corresponding exceptional divisors are $E_{i}$ and $G_{i}$ respectively, the subindex $i$ indicates the order of the blow-ups. This is shown in Figure 8. We name other irreducible curves with $S_{i}, F_{i}$, and $R$ as shown.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/a7e11a57-62e4-4b88-b77b-413295961562-20.jpg?height=449&width=1197&top_left_y=1760&top_left_x=462}
\captionsetup{labelformat=empty}
\caption{Figure 8.}
\end{figure}

We consider the Wahl configurations $L_{1}, R, L_{2}, S_{3}, E_{6}=[2,3,2,6,3]$, $S_{2}, F_{1}, E_{5}, E_{7}=[3,5,3,2]$, and $F_{2}, E_{9}, E_{10}=[6,2,2]$ in $Z_{1}$; and $S_{1}, L_{1}, R$,
$L_{2}, S_{3}, G_{12}=[3,2,2,2,8,2], F_{1}, G_{6}, G_{7}=[6,2,2]$, and $G_{4}, F_{2}, G_{9}, G_{10}, G_{11}=$ [2, 7, 2, 2, 3] in $Z_{2}$. Let $\sigma_{i}: Z_{i} \rightarrow X_{i}$ be the contraction of the Wahl configurations. Then, one can prove using usual techniques (as in Prop. 4.3) that there are no local-to-global obstructions to deform $X_{i}$. For both cases, we can check that any $\mathbb{Q}$-Gorenstein smoothing produces simply connected surfaces of general type with $K^{2}=1$ and $p_{g}=0$. Let $X_{0}^{i}$ be the minimal resolution of the singularity [2, 3, 2, 6, 3] for $X_{1}$ and [3, 2, 2, 2, 8, 2] for $X_{2}$. We consider W-surfaces $X_{0}^{i}$ which keep the corresponding exceptional divisors. Again the general fiber is the minimal resolution of stable surfaces living in two different boundary divisors of $\bar{M}$ labeled by the singularities [2, 3, 2, 6, 3] and [3, 2, 2, 2, 8, 2]. ${ }^{1}$

Let $\Gamma_{t}^{i}$ be the divisor in the 3-fold corresponding to either the (-6)curve for $i=1$ or the (-8)-curve for $i=2$. Let $E_{6, t}$ be the divisor corresponding to $E_{6}$ in $X_{0}^{1}$, and let $G_{12, t}$ be the divisor corresponding to $G_{12}$ in $X_{0}^{2}$. We now proceed to apply flips to the W-surface $X_{0}^{i}$ to find some nicer model for these deformations. We apply 3 W-flips of the type Prop. 4.1 for each $i$. For $X_{0}^{1}$ we flip $E_{8}, E_{6}, E_{11}$ in that order, and for $X_{0}^{2}$ we do it with $G_{8}, G_{13}, G_{12}$. In both cases we obtain smooth W-surfaces $Y_{0}^{i}$. We have that
$$\Gamma_{0}^{1}=F_{1}+F_{2}+S_{3} \quad \Gamma_{0}^{2}=F_{1}+F_{2}+S_{3} \quad E_{6,0}=S_{2} \quad G_{12,0}=G_{4} .$$

We now blow-down the 13 curves $E_{3}, E_{4}, S_{2}, S_{1}, L_{1}, S_{3}, L_{2}, E_{1}, E_{2}$, $S_{4}, S_{5}, S_{6}, S_{7}$ in $Y_{0}^{1}$. Similarly, we blow-down the 14 curves $G_{5}, G_{4}$, $G_{3}, S_{4}, S_{5}, S_{6}, S_{7}, G_{1}, G_{2}, S_{1}, L_{1}, S_{2}, S_{3}$, and $L_{2}$. The configuration of these exceptional curves (induced by the corresponding divisors) in $X_{t}^{i}$ is shown in Figure 9. Notice that when we blow them down, in both cases we obtain for $\Gamma_{t}^{i}$ a sextic in $\mathbb{P}^{2}$ with 8 nodes and one tacnode such that two nodes and the tacnode are colinear via the (transversal) line $R$. For $Y_{0}^{i}$ we obtain two nodal cubics intersecting at two tacnodes and 5 other points, and a line $R$ so that the two tacnodes intersections, and one more (nodal) intersection are colinear by $R$. Thus, in both cases, an irreducible sextic plus a line degenerate to these two nodal cubics plus a line.
5.4. A maximally singular stable surface via degenerations. In this example we show how to obtain a maximally degenerated surface which has eight Wahl singularities (this is the maximum possible for an unobstructed surface), from a simple configuration of two nodal cubics and a line. That configuration ends up representing a stable surface with one Wahl singularity $\frac{1}{24^{2}}(1,119)$. The corresponding smoothing is simply connected with $K^{2}=1$ and $p_{g}=0$. We present this example the

\footnotetext{
${ }^{1}$ Although in general a Wahl singularity could label two distinct divisors in $\bar{M}$.
}

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/a7e11a57-62e4-4b88-b77b-413295961562-22.jpg?height=331&width=1197&top_left_y=395&top_left_x=464}
\captionsetup{labelformat=empty}
\caption{Figure 9.}
\end{figure}
other way around, starting with the maximally degenerated surface, and then prove that a partial $\mathbb{Q}$-Gorenstein smoothing keeping only that Wahl singularity gives the simple septic above.

We start with seven lines in very special position. The lines $L_{1}, \ldots, L_{6}$ form a complete quadrilateral, and $L_{7}$ is the line passing through $L_{2} \cap L_{4}$ and $L_{3} \cap L_{6}$. This is in Figure 10. We consider the pencil generated by $L_{1}, L_{2}, L_{4}$ and $L_{3}, L_{5}, L_{6}$ which gives an elliptic fibration with singular fibers: $2 I_{5}+2 I_{1}$. The line $L_{7}$ is a particular triple section (see Figure 10); the curves $T_{1}, \ldots, T_{4}$ come from triple points as shown.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/a7e11a57-62e4-4b88-b77b-413295961562-22.jpg?height=462&width=896&top_left_y=1317&top_left_x=614}
\captionsetup{labelformat=empty}
\caption{Figure 10.}
\end{figure}

We now blow up 26 times obtaining a surface $Z^{\prime}$. The 26 exceptional divisors are denoted by $E_{1}, \ldots, E_{26}$ and again the subindex indicates the order of the composition of blow-ups. This is in Figure 11. A nonsingular surface $Z$ is obtained by blowing down the sections $S_{2}$ and $S_{3}$ in Figure 11. In $Z$ we have eight Wahl configurations: $L_{1}, L_{5}, T_{4}, L_{6}, T_{3}, E_{11}, E_{12}, E_{13}=[5,7,2,2,3,2,2,2], T_{2}, E_{19}, E_{20}, E_{21}, E_{22}=$ $[8,2,2,2,2], L_{4}, S_{1}, E_{15}, E_{16}, E_{17}=[8,2,2,2,2], T_{1}, E_{8}=[5,2], L_{2}, E_{7}$ $=[5,2], E_{1}=[4], L_{3}=[4]$, and $L_{7}=[4]$. Let $\sigma: Z \rightarrow X$ be the contraction of these eight configurations.

A sketch of the proof for no local-to-global obstructions for $X$ goes as follows. We start with the minimal elliptic fibration $Y \rightarrow \mathbb{P}^{1}$ with

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/a7e11a57-62e4-4b88-b77b-413295961562-23.jpg?height=393&width=997&top_left_y=402&top_left_x=563}
\captionsetup{labelformat=empty}
\caption{Figure 11.}
\end{figure}
singular fibers $2 I_{5}+2 I_{1}$. Then $H^{2}\left(Y, T_{Y}\left(-\log \left(I_{5}+I_{5}\right)\right)\right)=0$ by Prop. 4.2. We now add-delete $(-1)$-curves keeping this $H^{2}=0$. Notice that $L_{7}$ can be added as a (-1)-curve in some stage of the blow-ups (changing the given order). Thus this follows the usual procedure. Notice that $K_{X}^{2}=-26+2+25=1$.

To see that the canonical class of $K_{X}$ is nef, we use the trick in [LP07]. We look at the resolution $f: Z^{\prime} \rightarrow X$ and write down $f^{*}\left(K_{X}\right)$ in a $\mathbb{Q}$-numerically effective way. Then by intersecting with the curves in the support, one check it is nef. The two key points in the trick are (in our case): (1) to verify that the sums of the discrepancies of $L_{6}$ and $T_{3}$, and of $L_{1}$ and $L_{5}$ are smaller or equal than -1, (2) to verify that the discrepancies of $T_{1}, L_{2}, L_{4}, T_{3}, L_{1}, T_{2}, L_{5}, T_{4}, L_{6}$, and $L_{3}$ (the curves in the original $I_{5}$ fibers) have discrepancies smaller or equal than $-\frac{1}{2}$. Both (1) and (2) are true in our case. Therefore, the general fiber of a $\mathbb{Q}$-Gorenstein smoothing of $X$ is a surface of general type with $K^{2}=1$, $p_{g}=0$, and simply connected (for this, same strategy as in [LP07]).

We now consider a minimal resolution $X^{\prime} \rightarrow X$ of the singularity [5, 7, 2, 2, 3, 2, 2, 2], and a W-surface $X^{\prime}$ keeping the configuration [5, 7, 2, 2, 3, 2, 2, 2]. Let $\Gamma_{t, 1}, \Gamma_{t, 2}$, and $\Gamma_{t, 3}$ be the divisors in the 3-fold of the curves $L_{1}, L_{5}$, and $L_{6}$ in $X^{\prime}$ respectively. We will perform seven W-flips of the type Prop. 4.1 through the curves (and in that order): $E_{9}, E_{7}, E_{2}, E_{26}, E_{23}, E_{18}$, and $E_{5}$. We obtain at this point a smooth W -surface $X^{\prime}$ (by abuse of notation). Then we have
$$\Gamma_{0,1}=L_{1}+L_{7}+T_{1}+L_{2}+E_{1} \quad \Gamma_{0,2}=L_{5}+T_{2}+L_{4}+L_{3} \quad \Gamma_{0,3}=L_{6}$$
which already says that if we continue blowing down from $X^{\prime}$ to arrive into the seven special lines, then the configuration [5, 7, 2, 2, 3, 2, 2, 2] in the general fiber blows down to two nodal cubics $\Gamma_{t, 1}$ and $\Gamma_{t, 2}$, and a line $\Gamma_{t, 3}$. The cubics intersect transversally at nine points and three of them are collinear via $\Gamma_{t, 3}$. Thus this reducible septic gives a surface
with the Wahl singularity [5, 7, 2, 2, 3, 2, 2, 2], and degenerates maximally to a rigid configuration of seven lines which gives a surface with eight Wahl singularities. Finally, we observe that the surface with the one Wahl singularity [5, 7, 2, 2, 3, 2, 2, 2] specializes to the example in [PSU13, Sect.6].

\section*{References}

B86. L. Bǎdescu, Normal projective degenerations of rational and ruled surfaces, J. Reine Angew. Math. 367(1986), 76-89.
BHPV04. W. P. Barth, K. Hulek, C. A. M. Peters, and A. Van de Ven. Compact complex surfaces, Ergebnisse der Mathematik und ihrer Grenzgebiete. 3. Folge., second edition, vol. 4, Springer-Verlag, Berlin, 2004.
BC94. K. Behnke, and J. A. Christophersen. M-resolutions and deformations of quotient singularities, Amer. J. Math. 116(1994), No4, 881-903.
GS83. G.-M. Greuel, J. Steenbrink. On the topology of smoothable singularities, Proceedings of Symposia in Pure Mathematics, v.40(1983), part 1, 535-545.
GH78. P. Griffiths, and J. Harris. Principles of algebraic geometry, Reprint of the 1978 original. Wiley Classics Library. John Wiley \& Sons, Inc., New York, 1994.
Hack13. P. Hacking. Exceptional bundles associated to degenerations of surfaces, Duke Math. J. 162 (2013), no. 6, 1171-1202.
Hack12. P. Hacking. Compact moduli spaces of surfaces of general type, Compact moduli spaces and vector bundles, 1-18, Contemp. Math., 564, Amer. Math. Soc., Providence, RI, 2012.
HP10. P. Hacking, and Y. Prokhorov. Smoothable del Pezzo surfaces with quotient singularities, Compositio Math. 146(2010), 169-192.
HTU13. P. Hacking, J. Tevelev and G. Urzúa. Flipping surfaces, arXiv:1310.1580 [math.AG], preprint 2013.
Kaw92. Y. Kawamata. Moderate degenerations of algebraic surfaces, Complex algebraic varieties (Bayreuth, 1990), 113132, Lecture Notes in Math., 1507, Springer, Berlin, 1992.
Flops. J. Kollár. Flops, Nagoya Math. J. Vol. 113(1989), 15-36.
Ko91. J. Kollár. Flips, flops, minimal models, etc, Surveys in differential geometry 1(1991) 113-199.
KK94. J. Kollár, and S. Kovács. Birational geometry of log surfaces, Pre-print 1994.
KM98. J. Kollár, and S. Mori. Birational geometry of algebraic varieties, CTM 134 (1998).
KSB88. J. Kollár, and N. I. Shepherd-Barron. Threefolds and deformations of surface singularities, Invent. math. 91, 299-338 (1988).
LP07. Y. Lee, and J. Park. A simply connected surface of general type with $p_{g}=0$ and $K^{2}=2$, Invent. Math. 170, 483-505 (2007).
Man91. M. Manetti. Normal degenerations of the complex projective plane, J. reine angew. Math. 419 (1991), 89-118.
Urz13. G. Urzúa. Identifying neighbors of stable surfaces, arXiv:1310.4353 [math.AG], preprint 2013.
PSU13. H. Park, D. Shin, and G. Urzúa. A simply connected numerical Campedelli surface with an involution, Math. Ann. 357(2013), no. 1, 31-49.

Prok11. Y. Prokhorov. A note on degenerations of del Pezzo surfaces, arXiv:1108.5051v1 (2011).
Wahl81. J. Wahl. Smoothings of normal surface singularities, Topology 20(1981), no. 3, 219-246.
Wahl11. J. Wahl. Log-terminal smoothings of grading normal surface singularities, Michigan Math. J. 62(2013), 475-489.

Facultad de Matemáticas, Pontificia Universidad Católica de Chile, Santiago, Chile.
E-mail address: urzua@mat.puc.cl
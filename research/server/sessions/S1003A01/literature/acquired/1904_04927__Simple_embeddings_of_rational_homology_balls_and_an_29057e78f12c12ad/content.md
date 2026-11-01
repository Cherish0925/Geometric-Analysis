---
retention_scope: session
part: 1
total_parts: 1
---

---
source_file: 1904_04927.pdf
converter: mathpix
format: mmd
---

\title{
SIMPLE EMBEDDINGS OF RATIONAL HOMOLOGY BALLS AND ANTIFLIPS
}

\author{
HEESANG PARK, DONGSOO SHIN, AND GIANCARLO URZÚA
}

\begin{abstract}
Let $V$ be a regular neighborhood of a negative chain of 2-spheres (i.e. exceptional divisor of a cyclic quotient singularity), and let $B_{p, q}$ be a rational homology ball which is smoothly embedded in $V$. Assume that the embedding is simple, i.e. the corresponding rational blow-up can be obtained by just a sequence of ordinary blow-ups from $V$. Then we show that this simple embedding comes from the semi-stable minimal model program (MMP) for 3-dimensional complex algebraic varieties under certain mild conditions. That is, one can find all simply embedded $B_{p, q}$ 's in $V$ via a finite sequence of antiflips applied to a trivial family over a disk. As applications, simple embeddings are impossible for chains of 2-spheres with self-intersections equal to -2. We also show that there are (infinitely many) pairs of disjoint $B_{p, q}$ 's smoothly embedded in regular neighborhoods of (almost all) negative chains of 2-spheres. Along the way, we describe how MMP gives (infinitely many) pairs of disjoint rational homology balls $B_{p, q}$ embedded in blown-up rational homology balls $B_{n, a} \# \overline{\mathbb{C P}^{2}}$ (via certain divisorial contractions), and in the Milnor fibers of certain cyclic quotient surface singularities. This generalizes results in Khodorovskiy-2014 [5, 6], H. Park-J. Park-D. Shin-2016 [10], Owens-2017 [8] by means of a uniform point of view.
\end{abstract}

\section*{Contents}
1. Introduction ..... 1
Acknowledgements ..... 4
2. Preliminaries ..... 4
2.1. Singularities and their $P$-resolutions ..... 4
2.2. The semi-stable MMP and flips ..... 6
2.3. Mori sequences ..... 7
3. Simple embeddings and MMP ..... 8
4. Smoothly embedded rational homology balls via MMP ..... 11
5. Rational homology balls in Milnor fibers ..... 15
References ..... 15

\section*{1. Introduction}

Let $0<q<p$ be coprime integers. A rational homology ball $B_{p, q}$ is the 4-manifold obtained by attaching a 1-handle and a single 2-handle with framing $p q-1$ to $B^{4}$ by wrapping the attaching circle of the 2 -handle $p$-times around the 1 -handle with a $q / p$-twist. A rational homology ball $B_{p, q}$ may be also regarded as the Milnor fiber of the $\mathbb{Q}$-Gorenstein

\footnotetext{
2010 Mathematics Subject Classification. 57R40, 57R55, 14E30, 14B07.
Key words and phrases. antiflip, Mori sequence, rational homology ball.
}
smoothing of a cyclic quotient surface singularity of type $\frac{1}{p^{2}}(1, p q-1)$ (i.e. a Wahl singularity). The lens space $L\left(p^{2}, p q-1\right)$ is the boundary of $B_{p, q}$. At the same time, the space $L\left(p^{2}, p q-1\right)$ is a boundary of a regular neighborhood $C_{p, q}$ of a linear chain of 2-spheres $A_{1}, \ldots, A_{s}$, whose dual graph is given by
![](https://cdn.mathpix.com/cropped/3db73a83-7d4a-421e-a1c3-37829f0d2fa0-02.jpg?height=77&width=391&top_left_y=614&top_left_x=868)
where $A_{i} \cdot A_{i}=-a_{i} \leq-2$ with
$$\frac{p^{2}}{p q-1}=a_{1}-\frac{1}{a_{2}-\frac{1}{\ddots-\frac{1}{a_{s}}}}$$
Hence one can rationally blow-up $B_{p, q}$ which has been smoothly embedded in a smooth 4-manifold $W$; that is, $\widetilde{W}=\left(W \backslash B_{p, q}\right) \cup_{L\left(p^{2}, p q-1\right)} C_{p, q}$.

A typical way to produce smooth embeddings of $B_{p, q}$ 's is through the rational blowdown of a $C_{p, q}$ in a smooth 4-manifold $X$. This sometimes gives a 4-manifold which is not trivially related to $X$. For example, from a rational elliptic fibration we can get Enriques or Dolgachev surfaces, or from Lee-Park type of examples we can obtain surfaces of general type by applying rational blow-down to certain blow-ups of $\mathbb{C P}^{2}$ (see e.g. Urzúa [13]). However, it is not easy to detect rational homology balls $B_{p, q}$ embedded in a given 4-manifold $Z$ unless one knows a priori that $Z$ is obtained by performing a rational blowdown surgery.

Khodorovskiy [5, 6] initiates the study of detecting $B_{p, q}$. The author defines simple embeddings of $B_{p, q}$ in $V$ as the corresponding rational blow-up $W=\left(V \backslash \underline{B_{p, q}}\right) \cup C_{p, q}$ is obtained by a sequence of ordinary blow-ups $\pi: W \rightarrow V$, that is, $W=V \sharp k \overline{\mathbb{C} \mathbb{P}^{2}}$ for some $k \geq 1$. Using Kirby calculus, the author shows various instances of simple embeddings in regular neighborhoods of negative 2-spheres.

Theorem (Khodorovskiy [6, Theorem 1.2, 1.3]). There is a rational homology ball $B_{p, 1}$ simple embedded in a regular neighborhood $V_{-(p+1)}$ of a 2-sphere with self-intersection number $-p-1$. In particular, for all odd $p>1$, there exists a simple embedding of the rational homology balls $B_{p, 1} \hookrightarrow V_{-4}$.

Theorem (Khodorovskiy [6, Theorem 1.3]). For all even $p \geq 2$, there exists a simple embedding of the rational homology balls $B_{p, 1} \hookrightarrow B_{2,1} \sharp \overline{\mathbb{C P}}^{2}$.

Then in PPS [10], the authors HP and DS with Jongil Park generalizes Khodorovskiy [6, Theorem 1.2] as follows.

Theorem (PPS [10, Theorem 4.1]). Let $V$ be a plumbing 4-manifold of the $\delta$-half linear chain corresponding to $p^{2} /(p q-1)$ with $1 \leq q<p$. Then there is an embedded rational homology ball $B_{p, q}$ in $V$.

Here the $\delta$-half linear chain associated to $(p, q)$ is, roughly speaking, a half of the negative-definite plumbing graph associated to $C_{p, q}$ (see PPS [10]). The main tools of PPS [10] are techniques from explicit semi-stable minimal model program for 3-dimensional complex algebraic varieties. Using the MMP for 3-folds, they also prove again the result above of Khodorovskiy [6, Theorem 1.3].

Recently Owens [8] gives topological proofs for the results in Khodorovskiy [6] and PPS [10] by using manipulations of knot with bands diagrams representing properly embedded surfaces in $B^{4}$, which also leads the following new embeddings.
Theorem (Owens [8, Theorem 4]). There is a simple embedding $B_{p^{2}, p-1} \hookrightarrow B_{p, 1} \sharp \overline{\mathbb{C} \mathbb{P}^{2}}$.
Theorem (Owens [8, Theorem 5]). Let $F(n)$ is the $n$-th Fibonacci number. Then there is a smooth embedding $B_{F(2 n+2), F(2 n)} \hookrightarrow \overline{\mathbb{C P}^{2}}$.

Owens [8] found also new embeddings into $\mathbb{C P}^{2}$. These embeddings cannot be symplectic by the result of Evans-Smith [1] because they proved that all symplectic embeddings into $\mathbb{C P}^{2}$ are the ones coming from algebraic geometry via the classification of Hacking-Prokhorov [3]. We remark that these complex embeddings are also related to MMP via a blown-up family (see Urzúa [14, Theorem 3.1]).

In this paper we show that all simple embeddings in neighborhoods of linear chains of negative 2-spheres come from the semi-stable MMP for 3-dimensional complex algebraic varieties under certain mild conditions. Explicitly:

Theorem 1.1 (Theorem 3.5 for details). If $V$ is a regular neighborhood of a linear chain of 2-spheres which is diffeomorphic to the minimal resolution of a germ of a cyclic quotient surface singularity, then every plainly simple embedding (Definition 3.1) of $B_{p, q}$ in $V$ comes from a finite sequence of antiflips applied to a trivial family over a disk.

We remark that for a one parameter $\mathbb{Q}$-Gorenstein smoothing of a complex projective surface with only Wahl singularities, we have that if the general fiber is birational to the special fiber, then the $\mathbb{Q}$-Gorenstein smoothing comes from a smooth deformation after applying MMP (see Urzúa [14, Section 3]). In this "birational $\mathbb{Q}$-Gorenstein smoothing" situation all the corresponding embeddings of $B_{p, q}$ 's are simple.
Corollary (Corollary 3.6). There are no plainly simple embedded rational homology balls in a regular neighborhood of a linear chain $\Gamma$ of consisting of only 2 -spheres with selfintersections equal to -2.

So in principle one may find all plainly simple embedded $B_{p, q}$ in $V$ if one can handle the combinatorics of all possible mk1A's or mk2A's anti-flips (see Section 2.3) for a given trivial family with $V$ as its central fiber, which ends up in a $C_{p, q}$ rational blow-down of a blow-up of $V$. But describing this explicitly is a complicated combinatorial problem in general.

However, we generalize theorems of Khodorovskiy [6], PPS [10], Owens [8] above by means of MMP in the following way. Let $V$ be a regular neighborhood of a linear chain of 2-spheres $E_{1} \cup \cdots \cup E_{t}$ whose dual graph $\Gamma$ is given by
![](https://cdn.mathpix.com/cropped/3db73a83-7d4a-421e-a1c3-37829f0d2fa0-03.jpg?height=73&width=153&top_left_y=1968&top_left_x=986)
where $E_{i} \cdot E_{i}=-e_{i} \leq-2$ for all $i=1, \ldots, t$. We prove the following.
Theorem 1.2 (Theorem 4.5, Proposition 4.6). If $e_{t} \geq 3$, then there are pairs of disjoint $B_{p, q}$ 's for various $p, q$ smoothly embedded in $V$. Furthermore, there are infinitely many such pairs unless $e_{1}=\cdots=e_{t-1}=2$ and $e_{t}=3$. All the embeddings are simple.

Here $p$ and $q$ are explicitly determined by numerical data of the graph $\Gamma$; See Theorem 4.5 for details. In particular, we show that there are infinitely many pairs of disjoint $B_{p, q}$ 's in $V_{-n}$ for any $n \geq 4$ (Corollary 4.10).

Another simple consequences of the MMP procedure give the following two theorems.

Theorem 1.3 (cf. Theorem 4.11, Proposition 4.12). For any integers $n, a$ with $n>a \geq 1$ and $(n, a)=1$, there are infinitely many pairs of disjoint rational homology balls smoothly embedded in $B_{n, a} \sharp \overline{\mathbb{C P}^{2}}$, where one of them is ( $B_{n^{2}, n a-1}, B_{n, a}$ ). All of the embeddings except $B_{n, a} \hookrightarrow B_{n, a} \sharp \overline{\mathbb{C P}^{2}}$ are proved to be simple.

Theorem 1.4 (cf. Theorem 5.1). Let $(Q \in Y)$ be a cyclic quotient surface singularity which admits an extremal $P$-resolution $f^{+}: X^{+} \rightarrow Y$. Then there are infinitely many pairs of disjoint rational homology balls smoothly embedded in the Milnor fiber of $(Q \in Y)$ associated to the $P$-resolution $X^{+} \rightarrow Y$ and all of the embeddings are non-simple.

Theorem 1.4 may be regarded as a generalization of Park-Shin [12, Theorem 1.3]:
Theorem (Park-Shin [12, Theorem 1.3]). There is a smoothly embedded $B_{p, 1}$ in a nonsimple way inside a 2-handlebody corresponding to a certain twisted torus knot.

Since any Milnor fibers are Stein, they can be described as 2-handlebodies over Legendrian links. It would be an intriguing problem to find twisted torus knots associated to Milnor fibers, which reinterprets the above theorems in the language of the MMP for 3-folds and 2-handlebodies, vice versa. We leave it for the future research.

The paper is organized as follows. In Section 2 we recall some definitions, notations, and key facts that will be used in the proofs in the next sections. This includes as main tool the explicit semi-stable minimal model program for 3-dimensional algebraic varieties as in HTU [4]. Our main reference will be Urzúa [13, Section 2]. We prove that every simple embedding comes from MMP (Theorem 1.1) in Section 3, via an argument involving semistable MMP and Milnor numbers of smoothings of cyclic quotient surface singularities. The proof of existence of infinitely many simple embeddings (Theorem 1.4) will be given in Section 4, and involves a key combinatorial fact on Wahl singularities plus the universal family of extremal neighborhoods in HTU [4]. We provide non-simple embeddings in Section 5 using directly semi-stable MMP.

Acknowledgements. Heesang Park was supported by Basic Science Research Program through the National Research Foundation of Korea (NRF) funded by the Ministry of Education: NRF-2018R1D1A1B07042134. This paper was written as part of Konkuk University's research support program for its faculty on sabbatical leave in 2019. Dongsoo Shin was supported by Samsung Science and Technology Foundation under Project Number SSTF-BA1402-03. Giancarlo Urzúa was supported by the FONDECYT regular grant 1190066. A part of this work was done when Heesang Park and Dongsoo Shin were on sabbatical leave at Korea Institute for Advanced Study. They would like to thank KIAS for warm hospitality and financial support.

\section*{2. Preliminaries}

We briefly recall some basics on the semi-stable MMP and the related topics used in the present paper. For more details we will refer to Urzúa [13, Section 2]. We would like to point out that Evans-Urzúa [2] gives a symplectic topology guide to this MMP.
2.1. Singularities and their $P$-resolutions. A quotient surface singularity is a germ of the quotient $\mathbb{C}^{2} / G$ by a (small) finite subgroup $G \leq G L(2, \mathbb{C})$. In particular, a cyclic quotient surface singularity of type $\frac{1}{n}(1, a)(n>a \geq 1,(n, a)=1)$ is a germ of a quotient $\mathbb{C}^{2} / \mu_{n}$ of $\mathbb{C}^{2}$ by a multiplicative group $\mu_{n}=\langle\zeta\rangle, \zeta=\exp (2 \pi \sqrt{-1} / n)$, via the action $\zeta \cdot(x, y)=$ $\left(\zeta x, \zeta^{a} y\right)$. Let $E_{1}, \ldots, E_{s}$ be the exceptional curves of the minimal resolution of a cyclic quotient surface singularity of type $\frac{1}{n}(1, a)$ with $E_{j} \cong \mathbb{C P}^{1}$ and $E_{j}^{2}=-e_{j} \leq-2$ for all $j$.

Then the self-intersection number $e_{i}$ 's are determined by the Hirzebruch-Jung continued fraction of $n / a$, that is,
$$\frac{n}{a}=e_{1}-\frac{1}{e_{2}-\frac{1}{\ddots-\frac{1}{e_{s}}}}=:\left[e_{1}, e_{2}, \ldots, e_{s}\right]$$
and the dual graph of $E_{1}, \ldots, E_{s}$ is a linear chain of rational curves
![](https://cdn.mathpix.com/cropped/3db73a83-7d4a-421e-a1c3-37829f0d2fa0-05.jpg?height=73&width=228&top_left_y=782&top_left_x=950)

Notice that two Hirzebruch-Jung continued fractions $n / a=\left[e_{1}, \ldots, e_{s}\right]$ and $n /(n-a)=$ $\left[b_{1}, \ldots, b_{e}\right]$ are dual to each other, this is, we have
$$\left[e_{1}, \ldots, e_{s}, 1, b_{e}, \ldots, b_{1}\right]=0,$$
which implies that the linear chain of rational curves
![](https://cdn.mathpix.com/cropped/3db73a83-7d4a-421e-a1c3-37829f0d2fa0-05.jpg?height=56&width=460&top_left_y=1061&top_left_x=1225)
blown down to 0 .

Let $0 \in \mathbb{D}$ be the an analytic germ of a smooth curve (i.e. an arbitrarily small disk). A one-parameter deformation $(Y \subset \mathscr{Y}) \rightarrow(0 \in \mathbb{D})$ of a normal surface $Y$ is a smoothing of $Y$ if a general fiber is smooth. It is $\mathbb{Q}$-Gorenstein if $K_{\mathscr{Y}}$ is $\mathbb{Q}$-Cartier. A normal surface singularity is of class $T$ if it is a quotient surface singularity and admits a $\mathbb{Q}$-Gorenstein one-parameter smoothing KSB [7, Definition 3.7]. Singularities of class $T$ are determined completely KSB [7, Proposition 3.10], and they can be rational double points or a cyclic quotient surface singularities of type $\frac{1}{d n^{2}}(1, d n a-1)$ for $d \geq 1, n>a \geq 1,(n, a)=1$. Non rational double point T-singularities have a very particular minimal resolution KSB [7, Proposition 3.11].

A Wahl singularity defined by a pair $(n, a)$ is a cyclic quotient surface singularity of type $\frac{1}{n^{2}}(1, n a-1)$ for $n>a \geq 1,(n, a)=1$. Every Wahl singularity admits a $\mathbb{Q}$-Gorenstein smoothing whose Milnor fiber is diffeomorphic to a rational homology ball $B_{p, q}$; Wahl [15, Examples (5.9.1)].

Wahl singularities satisfy the following particular property, which will be key for our result on rational homology balls embedded in negative linear chains.

Corollary 2.1. Let $0<a<n$ be integers with $\operatorname{gcd}(n, a)=1$. Let $n / a=\left[a_{1}, \ldots, a_{p}\right]$ and $n /(n-a)=\left[b_{1}, \ldots, b_{q}\right]$. Then
$$\frac{n^{2}}{n a-1}=\left[a_{1}, \ldots, a_{p-1}, a_{p}+b_{q}, b_{q-1}, \ldots, b_{1}\right] .$$
Proof. See Owens [8, Lemma 3.1] for example. See also Hacking-Prokhorov [3] in more generality. \(\square\)

Corollary 2.2. Let $\stackrel{-a_{1}}{\bullet} \stackrel{-a_{p}}{\bullet}$ be a linear chain with $n / a=\left[a_{1}, \ldots, a_{p}\right]$. Blowing up the vertex $\stackrel{-a_{p}}{\bullet}$ appropriately, we have the following linear chain
![](https://cdn.mathpix.com/cropped/3db73a83-7d4a-421e-a1c3-37829f0d2fa0-05.jpg?height=54&width=883&top_left_y=2312&top_left_x=621)
Proof. This follows easily from the fact that $\left[b_{q}, \ldots, b_{1}, 1, a_{1}, \ldots, a_{p}\right]=0$. \(\square\)

Kollár and Shepherd-Barron [7, Section 3] show that any deformations of a quotient surface singularity can be induced deformations from certain special partial resolutions (called $P$-resolutions; Definition 2.3) with only singularities of class $T$.

Definition 2.3. A $P$-resolution of (a germ of) a quotient surface singularity ( $Q \in Y$ ) is a partial resolution $g: Z \rightarrow Y$ of $Q \in Y$ such that $Z$ has only singularities of class $T$ and $K_{Z}$ is ample relative to $g$.

Proposition 2.4 (cf. KSB [7, Theorem 3.9]). For any smoothing $\pi: \mathscr{Y} \rightarrow \mathbb{D}$ of a quotient surface singularity $(Q \in Y)$, there is a $P$-resolution $g: Z \rightarrow Y$ and a $\mathbb{Q}$-Gorenstein smoothing $\psi: \mathscr{Z} \rightarrow \mathbb{D}$ inducing $\mathbb{Q}$-Gorenstein smoothings of each singularities of class $T$ in $Z$ such that the smoothing $\mathscr{Z} \rightarrow \mathbb{D}$ blows down to $\mathscr{Y} \rightarrow \mathbb{D}$, that is, there is a morphism $G: \mathscr{Z} \rightarrow \mathscr{Y}$ satisfying $\psi=\pi \circ G$.
2.2. The semi-stable MMP and flips. We will use in our proofs the explicit semi-stable MMP for families of surfaces over $\mathbb{D}$ which is described in HTU [4]. We will refer to Urzúa [13, Section 2] as a quick concise reference.

The notation for a three dimensional extremal neighborhood will be
$$(C \subset X \subset \mathscr{X}) \rightarrow(Q \in Y \subset \mathscr{Y}),$$
where $C$ will be always a $\mathbb{P}^{1}, X$ a surface with at most two Wahl singularities such that $C^{2}<0$ and $C \cdot K_{X}<0$, and $C$ contracts to a cyclic quotient singularity ( $Q \in Y$ ). An extremal neighborhood is said to be flipping if the exceptional set of $F$ is $C$. On the other hand, if it is not flipping, then the exceptional set of $F$ is of dimension 2 . In this case we call it a divisorial extremal neighborhood. These flipping or divisorial contractions will be always mk1A or mk2A; see Urzúa [13, Section 2] for definition and numerical description. In these cases, for any flipping extremal neighborhood we always have a proper birational morphism called flip
$$\left(C^{+} \subset X^{+} \subset \mathscr{X}^{+}\right) \rightarrow(Q \in Y \subset \mathscr{Y})$$
where $X^{+} \rightarrow Y$ is an extremal P-resolution of $(Q \in Y)$. We also refer the induced birational map $\mathscr{X}_{-\rightarrow \mathscr{X}^{+}}$as flip. We recall that an extremal $P$-resolution $f^{+}: X^{+} \rightarrow Y$ of a cyclic quotient singularity ( $Q \in Y$ ) is a $P$-resolution such that $C^{+}=\left(f^{+}\right)^{-1}(Q)$ is an irreducible curve with only Wahl singularities.

A useful fact is the following.
Proposition 2.5 (see e.g. Urzúa [13, Proposition 2.8]). If an $m k 1 A$ or $m k 2 A$ is divisorial, then $(Q \in Y)$ is a Wahl singularity. And the divisorial contraction $F: \mathscr{X} \rightarrow \mathscr{Y}$ induces the blowing down of a $(-1)$-curve between the smooth fibers of $\mathscr{X} \rightarrow \mathbb{D}$ and $\mathscr{Y} \rightarrow \mathbb{D}$.

We will use the notation in Urzúa [13, Subsection 2.1] for the extremal neighborhoods mk1a and mk2A. In particular a mk1A will be presented by $\left[e_{1}, \ldots, \overline{e_{i}}, \ldots, e_{s}\right]$ where the Wahl singularity is $\frac{m^{2}}{m a-1}=\left[e_{1}, \ldots, e_{i}, \ldots, e_{s}\right]$. For a mk2A we will write
$$\left[f_{s_{2}}, \ldots, f_{1}\right]-\left[e_{1}, \ldots, e_{s_{1}}\right],$$
where $\frac{m_{2}^{2}}{m_{2} a_{2}-1}=\left[f_{1}, \ldots, f_{s_{2}}\right]$ and $\frac{m_{1}^{2}}{m_{1} a_{1}-1}=\left[e_{1}, \ldots, e_{s_{1}}\right]$ correspond to the two Wahl singularities. For the flip, the extremal P-resolution will be represented by
$$\left[f_{s_{2}}, \ldots, f_{1}\right]-c-\left[e_{1}, \ldots, e_{s_{1}}\right],$$
where $\frac{m_{2}^{\prime 2}}{m_{2}^{\prime} a_{2}^{\prime}-1}=\left[f_{1}, \ldots, f_{s_{2}}\right]$ and $\frac{m_{1}^{\prime 2}}{m_{1}^{\prime} a_{1}^{\prime}-1}=\left[e_{1}, \ldots, e_{s_{1}}\right]$ are the Wahl singularities. Precise terminology and numerics can be found in Urzúa [13, Subsection 2.1].
2.3. Mori sequences. It is proved in HTU [4] that for a fixed extremal P-resolution $X^{+}$, we have a family of flipping extremal neighborhoods of type mk1A and mk2A whose flip is a $\mathbb{Q}$-Gorenstein smoothing of $X^{+}$. It is also proved that for a fixed Wahl singularity $(Q \in Y)$, we have a family of divisorial extremal neighborhoods of type mk1A and mk2A whose divisorial contraction is a $\mathbb{Q}$-Gorenstein smoothing of $(Q \in Y)$. These families can be described numerically via Mori sequences. In these families there is an invariant $\delta \in \mathbb{Z}_{>0}$ which can be read from the intersection of the flipping curve with the canonical class. If $\delta=1$, then the Mori sequence is finite. Otherwise the Mori sequence is infinite.

We summarize briefly HTU [4, Subsection 3.3]. See also Urzúa [13, Section 2].
Let $\mathbb{E}_{1}$ be an mk2A with Wahl singularities defined by pairs $\left(m_{1}, a_{1}\right)$ and $\left(m_{2}, a_{2}\right)$ with $m_{2}>m_{1}$, that is, an mk2A with two Wahl singularities of type $\frac{1}{m_{1}^{2}}\left(1, m_{1} a_{1}-1\right)$ and $\frac{1}{m_{2}^{2}}\left(1, m_{2} a_{2}-1\right)$. Here we also allow the mk1A for special case $m_{1}=a_{1}=1$. Let $\boldsymbol{\delta}=m_{2} a_{1}+m_{1} a_{2}-m_{1} m_{2}$. Since $K_{X} \cdot C=-\delta /\left(m_{1} m_{2}\right)<0$, we have $\boldsymbol{\delta} \geq 1$.

Assume that $\delta m_{1}-m_{2} \leq 0$ from now on. Such an mk2A is called an initial mk2A in HTU [4]. We first define two sequences $d(i)$ and $c(i)$ (called the Mori recursions) as follows: For $i \geq 2$,
$$\begin{aligned}
& d(1)=m_{1}, \quad d(2)=m_{2}, \quad d(i+1)=\delta d(i)-d(i-1), \\
& c(1)=a_{1}, \quad c(2)=m_{2}-a_{2}, \quad c(i+1)=\delta c(i)-c(i-1) .
\end{aligned}$$

Definition 2.6 (Mori sequence for $\delta>1$ ). If $\delta>1$, then a Mori sequence for an initial $\mathrm{mk} 2 \mathrm{~A} \mathbb{E}_{1}$ is a sequence of mk2A's $\mathbb{E}_{i}$ with Wahl singularities defined by the pairs $\left(m_{i}, a_{i}\right)$ and ( $m_{i+1}, a_{i+1}$ ) where
$$m_{i+1}=d(i+1), a_{i+1}=d(i+1)-c(i+1), \quad m_{i}=d(i), a_{i}=c(i) .$$
Notice that $m_{i+1}>m_{i}$.
Definition 2.7 (Mori sequence for $\delta=1$ ). If $\delta=1$, then a Mori sequence for an initial $\operatorname{mk} 2 \mathrm{~A} \mathbb{E}_{1}$ consists of one more $\mathrm{mk} 2 \mathrm{~A} \mathbb{E}_{2}$ defined by the pairs $\left(m_{2}, a_{2}\right)$ and $\left(m_{3}, a_{3}\right)$, where $m_{2}=d(2), a_{2}=c(2)$, and $m_{3}=d(2)-d(1), a_{3}=d(2)-d(1)+c(1)-c(2)$.
Proposition 2.8 (HTU [4, Proposition 3.15, Theorem 3.20]). If $\delta m_{1}-m_{2}<0$, then the $m k 2 A \mathbb{E}_{i}$ 's $(i \geq 1)$ in the Mori sequence of an initial $m k 2 A \mathbb{E}_{1}$ are of flipping type sharing the same $\delta, \Omega, \Delta$ associated to $\mathbb{E}_{1}$ and, after flipping each $\mathbb{E}_{i}$, they have the same extremal $P$-resolution $X^{+}$admitting two Wahl singularities defined by the pairs ( $m_{1}^{\prime}, a_{1}^{\prime}$ ) and ( $m_{2}^{\prime}, a_{2}^{\prime}$ ) where $m_{2}^{\prime}=m_{1}, a_{2}^{\prime}=m_{1}-a_{1}$, and $m_{1}^{\prime}=m_{2}-\delta m_{1}, a_{1}^{\prime} \equiv m_{2}-a_{2}-\delta a_{1}\left(\bmod m_{1}^{\prime}\right)$. Here, in case of $m_{1}=a_{1}=1$, we set $a_{2}^{\prime}=1$.
Proposition 2.9 (HTU [4, Proposition 3.13]). If $\delta m_{1}-m_{2}=0$, then $\mathbb{E}_{i}$ 's are of divisorial type with $m_{1}=\delta, m_{2}=\delta^{2}$, and $a_{2}=\delta^{2}-\left(\delta a_{1}-1\right)$. By Proposition 2.5, the contraction $\mathscr{X}_{i} \rightarrow \mathscr{Y}$ over $\mathbb{D}$ corresponding to $\mathbb{E}_{i}$ induces the blow down $X_{i, t} \rightarrow Y_{t}$ over $0 \neq t \in \mathbb{D}$ of a (-1)-curve between smooth fibers.
Example 2.10 (Mori sequence of a flipping family for $\delta>1$; cf. Urzúa [13, Example 2.14]). Let $(Q \in Y)$ be the cyclic quotient surface singularity of type $\frac{1}{11}(1,3)$. Consider the extremal $P$-resolution $X^{+} \rightarrow Y$ defined by [4] - 3. So we have $m_{1}^{\prime}=1, a_{1}^{\prime}=1$, and $m_{2}^{\prime}=2, a_{2}^{\prime}=1$, and $\delta=3$. There are two corresponding initial flipping mk2A's: One is defined by the pairs $(1,1)$ and $(5,3)$ and the other is defined by $(2,1)$ and (7,5). Therefore the first three entries of each Mori sequences are defined by the following pairs:
$$\begin{aligned}
& \mathbb{E}_{1}:(1,1),(5,3), \mathbb{E}_{2}:(5,2),(14,9), \mathbb{E}_{3}:(14,5),(37,24), \ldots \\
& \mathbb{E}_{1}:(2,1),(7,5), \mathbb{E}_{2}:(7,2),(19,14), \mathbb{E}_{3}:(19,5),(50,37), \ldots
\end{aligned}$$

Notice that two Wahl singularities defined by ( $n, a$ ) and ( $n, n-a$ ) represent the same singularity. So numerical data of any mk1A and any mk2A associated to [4]-3 can be read from
$$\cdots-[3,7,5, \overline{2}, 2,2,2,3,2]-[3,7,2, \overline{2}, 3,2]-[3,5, \overline{2}]-\varnothing$$
and
$$\cdots-[4,7,5, \overline{2}, 2,2,2,3,2,2]-[4,7,2, \overline{2}, 3,2,2]-[4,5, \overline{2}, 2]-[4],$$
where $\varnothing$ represents a smooth point (that is, the case of $m_{1}=a_{1}=1$ in the initial mk2A). These two Mori sequences provide the numerical data of all flipping extremal neighborhoods whose flip have [4]- 3 as central fiber. For example, the mk2A's [3, 7, 2, 2, 3, 2] - [3,5,2] and [4,7,2,2,3,2,2] - [4,5,2,2] or the mk1A [4,7,5,2,2,2,2,3,2,2] have flips whose central fiber is $[4]-3$.

Example 2.11 (Mori sequence of a flipping family for $\delta=1$ ). Let $(Q \in Y)$ be the cyclic quotient surface singularity of type $\frac{1}{13}(1,3)$. Consider the extremal $P$-resolution $X^{+} \rightarrow Y$ defined by $[5,2]-2$. Then $\delta=1$. There are two initial flipping mk2A's; but, their Mori sequences coincide. The numerical data of any mk1A and any mk2A associated to [5,2] -2 can be read from
$$[2,5]-[2,2, \overline{6}]-\varnothing .$$

Example 2.12 (Mori sequence of a divisorial family; Urzúa [13, Example 2.13]). Let $(Q \in \mathscr{Y})$ be the Wahl singularity $\frac{1}{4}(1,1)$. Then the numerical data of any mk1A and mk2A of divisorial type associated to $(Q \in \mathscr{Y})$ is as follows:
$$\cdots-[10, \overline{2}, 2,2,2,2,2]-[8, \overline{2}, 2,2,2]-[6, \overline{2}, 2]-[4] .$$

A flip which appears frequently in this paper is the following.
Proposition 2.13 (cf. Urzúa [13, Proposition 2.15]). Let $n^{2} /(n a-1)=\left[e_{1}, \ldots, e_{s}\right]$. Then the $m k 1 A\left[e_{1}, \ldots, e_{s-1}, \overline{e_{s}}\right]$ is an initial flipping $m k 1 A$ with $\delta=n-a$. If $e_{j}=2$ for all $i_{0}<j \leq s$ and $e_{i_{0}} \geq 3$, then the data for the flip $X^{+}$is
$$e_{1}-\left[e_{2}, \ldots, e_{i_{0}}-1\right] .$$

Proposition 2.14. Let ( $Q \in Y$ ) be a cyclic quotient surface singularity. Suppose that there is an extremal $P$-resolution $X^{+} \rightarrow Y$ defined by $\left[a_{s}, \ldots, a_{1}\right]-c$ with $\left[a_{1}, \ldots, a_{s}\right]=m^{2} /(m a-$ 1). Suppose that $\delta=1$. Then $c=2$ and $a=m-1$. Hence the extremal $P$-resolution is of the form
$$[m+2, \underbrace{2, \ldots, 2}_{m-2}]-2$$
and any mk1A or mk2A corresponding to $X^{+} \rightarrow Y$ can be read from:
$$[\underbrace{2, \ldots, 2}_{m-2}, m+2]-[\underbrace{2, \ldots, 2}_{m-1}, \overline{m+3}]-\varnothing .$$
Proof. Since $\delta=c m_{1}^{\prime} m_{2}^{\prime}-m_{1}^{\prime} a_{2}^{\prime}-m_{2}^{\prime} a_{1}^{\prime}=(c-1) m-a=1$, we have $a=(c-1) m-1$. But $a<m$. Hence $c=2$ and $a=m-1$. Then the other assertions follow easily. \(\square\)

\section*{3. Simple embeddings and MMP}

Let $V$ be a (sufficiently small) regular neighborhood of a linear chain of negative 2spheres $\cup_{i=1}^{r} B_{i}$ with $B_{i} \cdot B_{i} \leq-2$, which may be assumed to be diffeomorphic to the minimal resolution of a germ of a cyclic quotient surface singularity $P$. Assume that there is a smoothly embedded rational homology ball $B_{p, q} \hookrightarrow V$.

An embedding $B_{p, q} \hookrightarrow V$ is said to be simple if the corresponding rational blow-up $W=\left(V \backslash B_{p, q}\right) \cup C_{p, q}$ is obtained by a sequence of ordinary blow-ups $\pi: W \rightarrow V$, that is, $W=V \sharp k \overline{\mathbb{C P}^{2}}$ for some $k \geq 1$; Khodorovskiy [5, 6]. But in this section we consider a slightly more restricted situation.
Definition 3.1. A simple embedding $B_{p, q} \hookrightarrow V$ is said to be plainly simple if the negative 2-spheres of $C_{p, q}$ in $W$ consist of the proper transforms of $B_{i}$ 's and that of the exceptional 2-spheres of $\pi: W \rightarrow V$.

Remark 3.2. It is not necessary that a simple embedding is plainly simple. Recently, Owens [8, 9] show the existence of simple embeddings of $B_{p, q}$ 's in $\mathbb{C P}^{2}$ which are not symplectic. For $B_{5,2}$ one can show that it is not plainly simple.

In this section we show that every plainly simple embedding of $B_{p, q}$ in $V$ comes from a finite sequence of antiflips applied to a trivial family over a disk $\mathbb{D}$; Theorem 3.5. But, in order to state the theorem precisely, we need to introduce some notions.

From now on we assume that there is a plainly simple embedding of $B_{p, q}$ in $V$.
Let $V_{\mathbb{C}}$ be a complex model for $V$. That is, $V_{\mathbb{C}}$ is the minimal resolution of $P$ (of type $\left.\frac{1}{m}(1, b)\right)$ with the exceptional divisors $B=\sum_{i=1}^{r} B_{i}$ such that $\left(V, \cup B_{i}\right)$ is diffeomorphic to $\left(V_{\mathbb{C}}, \cup B_{i}\right)$.

Suppose that the dual graph of $B$ is given by
![](https://cdn.mathpix.com/cropped/3db73a83-7d4a-421e-a1c3-37829f0d2fa0-09.jpg?height=79&width=393&top_left_y=1231&top_left_x=866)
where $m / b=\left[b_{1}, \ldots, b_{r}\right]$.
We may take a sequence of blow-ups $\pi_{\mathbb{C}}: W_{\mathbb{C}} \rightarrow V_{\mathbb{C}}$ so that the dual graph of $W_{\mathbb{C}}$ is the one from $W$, that is, $\pi_{\mathbb{C}}: W_{\mathbb{C}} \rightarrow V_{\mathbb{C}}$ is the complex model of the blow-ups $\pi: W \rightarrow V$.

So there is a diffeomorphism of pairs between $\left(C_{p, q} \subset W\right)$ and $\left(C_{p, q} \subset W_{\mathbb{C}}\right)$. Since $\left(B_{p, q} \subset V\right)$ is obtained by rationally blow-down $W$ along $C_{p, q}$, there is a smoothly embedded $B_{p, q}$ in $V_{\mathbb{C}}$ induced by the rational blow-down of $C_{p, q}$ in $W_{\mathbb{C}}$ so that there is a diffeomorphism of pairs
$$\left(B_{p, q} \subset V_{\mathbb{C}}\right) \sim\left(B_{p, q} \subset V\right) .$$

We denote by $E=\sum_{k=1}^{t} E_{k}$ the divisor in $W_{\mathbb{C}}$ consisting of the rational curves corresponding to $C_{p, q}$ in $W_{\mathbb{C}}$. We contract $E$ from $W_{\mathbb{C}}$ so that we have a singular surface $X$ with one Wahl singularity $x \in X$. Let $f:(X \subset \mathscr{X}) \rightarrow(0 \in \mathbb{D})$ be a deformation of $X$ that is induced by the $\mathbb{Q}$-Gorenstein smoothing of $x \in X$. A general fiber $X_{t}=f^{-1}(t)(t \neq 0)$ is just the rational blow-down of $W_{\mathbb{C}}$ along $C_{p, q}$. Therefore we have a diffeomorphism of pairs
$$\left(B_{p, q} \subset X_{t}\right) \sim\left(B_{p, q} \subset V_{\mathbb{C}}\right) \sim\left(B_{p, q} \subset V\right) .$$

We now compactify $\mathscr{X}$ as we did in PPSU [11, §3] so that we will transform $f: \mathscr{X} \rightarrow \mathbb{D}$ into a proper map $\bar{f}: \overline{\mathscr{X}} \rightarrow \mathbb{D}$ because the relative MMP may be applied to proper maps mostly.

Let $\mathbb{F}_{1}$ be the Hirzebruch surface with the negative section $S_{0}$ with $S_{0} \cdot S_{0}=-1$. Let $S_{\infty}$ be another section of $\mathbb{F}_{1}$ with $S_{\infty} \cdot S_{\infty}=1$ and let $F$ be a fiber of $\mathbb{F}_{1}$, that is, $F \cdot F=0$. We blow up $\mathbb{F}_{1}$ appropriately at $S_{0} \cap F$ (including infinitely near points over there) so that we obtain the following chain of rational curves starting from the proper transform $\bar{S}_{0}$ of $S_{0}$ and ending with the proper transform $\bar{S}_{\infty}$ of $S_{\infty}$ :
![](https://cdn.mathpix.com/cropped/3db73a83-7d4a-421e-a1c3-37829f0d2fa0-09.jpg?height=84&width=945&top_left_y=2333&top_left_x=589)
where $m /(m-b)=\left[a_{1}, \ldots, a_{e}\right]$. Let $\bar{V}_{\mathbb{C}}$ be the blown-up Hirzebruch surface $\mathbb{F}_{1}$ that contains the configuration of rational curves in Equation (3.3) above. Let $\bar{\pi}_{\mathbb{C}}: \bar{W}_{\mathbb{C}} \rightarrow \bar{V}_{\mathbb{C}}$ be the sequence of blow-ups that is the extension of $\pi_{\mathbb{C}}: W_{\mathbb{C}} \rightarrow V_{\mathbb{C}}$. We contract the divisor $E=\sum_{i=1}^{t} E_{i}$ in $\bar{W}_{\mathbb{C}}$ corresponding to $C_{p, q}$ so that we get a singular surface $\bar{X}$ with the Wahl singularity $x \in \bar{X}$. Note that
$$X=\bar{X} \backslash\left(\cup_{i=1}^{e} A_{i} \cup \bar{S}_{\infty}\right) .$$

We will show that the $\mathbb{Q}$-Gorenstein smoothing of $x \in \bar{X}$ can be extended to a deformation of $\bar{f}: \overline{\mathscr{X}} \rightarrow \mathbb{D}$ that preserves the curves $A_{1}, \ldots, A_{e}$ and $\bar{S}_{\infty}$. For this, we contract again the linear chain $A=\cup_{j=1}^{e} A_{j}$ in $\bar{W}_{\mathbb{C}}$ and $\bar{X}$ to a singularity $Q$ respectively so that we get two singular surfaces $\widehat{W}_{\mathbb{C}}$ and $\widehat{X}$ with two singular points $y$ and $Q$.

Lemma 3.3. The obstruction to local-to-global deformations of $\widehat{X}$ vanishes. That is, $H^{2}\left(\widehat{X}, \mathscr{T}_{\widehat{X}}\right)=0$, where $\mathscr{T}_{\widehat{X}}$ is the tangent sheaf of $\widehat{X}$.

Proof. The proofs in PPSU [11, Lemma 3.3, Proposition 3.4] work verbatim. \(\square\)

Proposition 3.4. Any smoothing $\mathscr{X} \rightarrow \mathbb{D}$ of $X$ can be extended to a smoothing $\overline{\mathscr{X}} \rightarrow \mathbb{D}$ of $\bar{X}$ which preserves the curves $A_{1}, \ldots, A_{e}$ and $\bar{S}_{\infty}$ so that $X_{t}=\bar{X}_{t} \backslash\left(\cup_{i=1}^{e} A_{i} \cup \bar{S}_{\infty}\right)$ for $0 \neq t \in \mathbb{D}$.

Proof. Since there is no local-to-global obstruction to deform $\widehat{X}$ by the above Lemma 3.3, one may take a deformation $\widehat{\mathscr{X}} \rightarrow \mathbb{D}$ of $\widehat{X}$ that is an extension of a smoothing of $Y$ such that it preserves the singular point $Q$. By taking a simultaneous resolution of the singularity $Q$ on each fibers of $\widehat{\mathscr{X}} \rightarrow \mathbb{D}$, we obtain the desired smoothing $\overline{\mathscr{X}} \rightarrow \mathbb{D}$ of $\bar{X}$. \(\square\)

Theorem 3.5. Given a plainly simple embedding of a $B_{p, q}$ in $V$ as above, there is a sequence of flips $\mathscr{X}_{1} \rightarrow \mathscr{X}_{2} \rightarrow \rightarrow \cdots \rightarrow \mathscr{X}_{n}$ with $\mathscr{X}=\mathscr{X}_{1}$ such that the central fiber $X_{n, 0}$ of $\mathscr{X}_{n}$ is smooth and equal to $V_{\mathbb{C}}$. Hence we have that $\left(B_{p, q} \subset V\right)$ and $\left(B_{p, q} \subset X_{n, 0}\right)$ are diffeomorphic.

Proof. To simplify notation, let us write $\pi: W \rightarrow V$ instead of $\pi_{\mathbb{C}}: W_{\mathbb{C}} \rightarrow V_{\mathbb{C}}$. Since $b_{2}(V)<b_{2}(W)$, there are $(-1)$-curves on $W$. Moreover since the rational blow-down of $W$ along $C_{p, q}$ is diffeomorphic to $V$ (which is minimal), we must have (-1)-curves in $W$ intersecting $C_{p, q}$ at one point. Let $C$ be one of them. Since $C+C_{p, q}$ is negative definite (the whole exceptional divisor of $\pi$ plus the proper transform of the linear chain $B$ contracts to a cyclic quotient singularity), we have that $C+C_{p, q}$ contracts to a cyclic quotient singularity. As above, let $W \rightarrow X$ be the contraction of $C_{p, q}$, and let $(X \subset \mathscr{X}) \rightarrow(0 \in \mathbb{D})$ be a deformation of $X$ that is induced by the $\mathbb{Q}$-Gorenstein smoothing of the Wahl singularity $x \in X$. We have that $K_{\mathscr{X}} \cdot C<0$. Then the blowing-down deformation of $C \subset X$ into a cyclic quotient singularity $y \in Y$ gives a flipping extremal neighborhood $\mathscr{X} \rightarrow \mathscr{Y}$ over $\mathbb{D}$. Note that a general fiber for both $\mathscr{X}$ and $\mathscr{Y}$ is diffeomorphic to $V$. Let $(C \subset \mathscr{X}) \rightarrow\left(C^{+} \subset \mathscr{X}^{+}=: \mathscr{X}_{2}\right)$ be the flip of $C$ over $\mathscr{Y} \rightarrow \mathbb{D}$.

We want to continue running the relative MMP. (We could think this is happening in families of projective surfaces over $\mathbb{D}$ by compactifying the surface $W$ as it was done in PPSU [11] and explained above. There are no local-to-global obstructions, and we run MMP relative to a blow-up of $B \subset V$.) For that, let us first assume that $K_{\mathscr{X}}+$ is nef. This is the same as assuming $K_{X^{+}}$is nef, where $X^{+}$is the central fiber (see Urzúa [14, Section 2]). Let $V \rightarrow v^{\prime} \in V^{\prime}$ be the contraction of $L$ to a cyclic quotient singularity $v^{\prime} \in V^{\prime}$. Then we have a contraction map $X^{+} \rightarrow V^{\prime}$, and it has $K_{X^{+}}$nef, so it an M-resolution of $v^{\prime} \in V^{\prime}$ (i.e., only Wahl singularities and $K_{X^{+}}$nef), this is a crepant partial resolution of a unique P-resolution of $V^{\prime}$. In particular, the $\mathbb{Q}$-Gorenstein smoothing $X^{+} \subset \mathscr{X}^{+} \rightarrow \mathbb{D}$ blows-down
to a deformation $V^{\prime} \subset \mathscr{V}^{\prime} \rightarrow \mathbb{D}$ so that the general fibers have the same Milnor numbers KSB [7]. Now, the general fiber of $X^{+} \subset \mathscr{X}^{+} \rightarrow \mathbb{D}$ is diffeomorphic to $V$, and so its Milnor number is the number of 2-spheres in the linear chain $B$. But then the deformation $V^{\prime} \subset \mathscr{V}^{\prime} \rightarrow \mathbb{D}$ happens in the Artin component of the versal deformation space of $v^{\prime} \in V^{\prime}$. This is because the Milnor number of a smoothing in the Artin component is the largest one from all components, since the difference of the dimension of any two components is equal to twice the difference between the corresponding Milnor numbers, and the largest dimension corresponds to the one of the Artin component Wahl [15, (4.7.3)]. We note that the Milnor number for the Artin component is the number of 2-spheres in $B$. Therefore, the surface $X^{+}$must be smooth, and so $X^{+}=V$, and this is what we wanted to conclude.

Otherwise, suppose that $K_{X^{+}}$is not nef. Then as it was done e.g. in Urzúa [14, Section 2], there must be a curve $C \subset X^{+}$with $C \cdot K_{X^{+}}<0$ and $C^{2}<0$, and so we are in the situation of an extremal neighborhood of type k1A or k2A as in HTU [4, Section 5], i.e., induced from a $(-1)$-curve in the minimal resolution of $X^{+}$. It must be of flipping type since the general fiber of $X^{+} \subset \mathscr{X}^{+} \rightarrow \mathbb{D}$ is diffeomorphic to $V$. Let $\left(C \subset X^{+} \subset \mathscr{X}^{+}\right)-\rightarrow\left(C^{+} \subset\right.$ $X_{3} \subset \mathscr{X}_{3}$ ) be the flip over $\mathbb{D}$. Note that again, by the same reasons as above, we have the contraction $X_{3} \rightarrow V^{\prime}$. And so, from this point we can apply induction on the number of flips.

We note that the process must end in a smooth deformation $\mathscr{X}_{n} \rightarrow \mathbb{D}$ for some $n$ since at each flip the index of the Wahl singularities involved strictly decrease (see e.g. HTU [4]).

Since we used only flips, the general fiber $X_{n, t}(t \neq 0)$ is isomorphic to $V_{\mathbb{C}}$. Hence $X_{n, 0}$ has no (-1)-curves, and since it is some blow-up of $V_{\mathbb{C}}$, we must have $X_{n, 0}=V_{\mathbb{C}}$. Hence, referring to Equation (3.2), MMP gives an explanation of how $B_{p, q}$ is simply embedded in $V$ via a trivial family plus antiMMP on its complex model $V_{\mathbb{C}}$. \(\square\)

Corollary 3.6. There is no plainly simple embedded rational homology ball $B_{p, q}$ in a neighborhood of the linear chain of 2-spheres whose self-intersection numbers are all (-2).

Proof. Suppose that there is a sequence of flips that induces a simple embedding of a rational homology ball. Think on the last flipped surface $X_{n}^{+}$. Then it comes from a $P$ resolution which consists of only one (-2)-curve. But a (-2)-curve is not $P$-resolution since canonical class is trivial on it. \(\square\)

Remark 3.7. Khodorovskiy [5, Prop.5.1] proves that there are no symplectically embedded $B_{n, 1}$ in $E(2)$ for any $n \geq 2$, which implies that there is no symplectic embedding $B_{n, 1} \hookrightarrow V_{-2}$ for any $n \geq 2$. The above corollary would be a generalization of this phenomenon.

\section*{4. Smoothly embedded rational homology balls via MMP}

We prove the existence of smoothly embedded rational homology balls using Mori sequences of antiflips. We first construct a special flipping mk1A associated to a given linear chain. Let $V$ be a germ of complex surface containing a linear chain
$$\Gamma=\stackrel{-e_{1}}{\bullet} \cdots \cdots \stackrel{-e_{t}}{\bullet}$$
of complex rational curves with $e_{i} \geq 2$ for all $i$. Assume that $e_{t} \geq 3$. If $n / a=\left[e_{1}, \ldots, e_{t}-1\right]$, then, blowing up appropriately $V$ several times (cf. Corollary 2.2), we have a regular
neighborhood $U$ of the linear chain
![](https://cdn.mathpix.com/cropped/3db73a83-7d4a-421e-a1c3-37829f0d2fa0-12.jpg?height=77&width=550&top_left_y=473&top_left_x=786)
where $n^{2} /(n a-1)=\left[b_{1}, \ldots, b_{s}\right]$. Let $U \rightarrow X$ be the contraction of the linear chain $B_{1} \cup$ $\cdots \cup B_{s}$ in $U$ to a Wahl singularity $P \in X$ defined by the pair $(n, a)$. Denote again by $C \subset X$ the image of $C \subset U$. Let $U \rightarrow Z$ be the contraction of $C \subset X$ to a quotient singularity $Q \in Y$. Let $\mathscr{X} \rightarrow \mathbb{D}$ be a deformation of $X$ induced by the $\mathbb{Q}$-Gorenstein smoothing of the singularity $P \in X$ and let $\mathscr{Y} \rightarrow \mathbb{D}$ be the blown-down deformation of $\mathscr{X} \rightarrow \mathbb{D}$. According to Proposition 2.13, $(C \subset \mathscr{X}) \rightarrow(Q \in \mathscr{Y})$ is an initial flipping mk1A.

Definition 4.1. The mk1A constructed above is called the usual initial flipping mk1A associated to the linear chain $\Gamma$. We denote it
![](https://cdn.mathpix.com/cropped/3db73a83-7d4a-421e-a1c3-37829f0d2fa0-12.jpg?height=77&width=550&top_left_y=958&top_left_x=786)
where the vertex □ implies that the corresponding rational curve is contracted to a Wahl singularity. For simplicity, we may denote the above mk2A by $\left[b_{1}, \ldots, b_{s}\right]-1-e_{1}-\cdots-$ $e_{t-1}$, where the bracket [ ] implies that we contract them.

Remark 4.2. The linear chain $\stackrel{-e_{1}}{\bullet} \cdots \cdots \stackrel{-e_{t}}{\bullet}$ is the $\delta$-half linear chain of the Wahl singularity $\frac{1}{n^{2}}(1, n a-1)$ defined in PPS [10, Definition 2.6].

Almost all initial flipping mk1A associated to a linear chain have $\delta>1$ :
Lemma 4.3. Let $\mathbb{E}_{1}$ be the usual initial flipping $m k 1 A$ associated to $\Gamma$. Then $\delta=1$ if and only if $\Gamma$ is of the form
![](https://cdn.mathpix.com/cropped/3db73a83-7d4a-421e-a1c3-37829f0d2fa0-12.jpg?height=52&width=221&top_left_y=1504&top_left_x=952)
Proof. By Proposition 2.13, $\delta=n-a$. Therefore $n-a=1$ iff $a=n-1$ iff $\left[a_{1}, \ldots, a_{t}-1\right]=$ $n /(n-1)=[2, \ldots, 2]$. \(\square\)

Lemma 4.4 (PPS [10, Corollary 3.12]). Applying flips described in Proposition 2.13 repeatedly to the usual initial flipping $m k 1 A(C \subset \mathscr{X}) \rightarrow(Q \in \mathscr{Y})$ associated to $\Gamma$, we have a deformation $\mathscr{Z} \rightarrow \mathbb{D}$ such that all of the fibers are smooth. In particular, the central fiber $Z_{0}$ of $\mathscr{Z} \rightarrow \mathbb{D}$ is the regular neighborhood $V$.

Theorem 4.5. Let $V$ be a regular neighborhood of a linear chain $\Gamma=E_{1} \cup \cdots \cup E_{t}(t \geq 1)$ of 2-spheres whose dual graph is given by
![](https://cdn.mathpix.com/cropped/3db73a83-7d4a-421e-a1c3-37829f0d2fa0-12.jpg?height=71&width=153&top_left_y=1989&top_left_x=986)
where $E_{i} \cdot E_{i}=-e_{i} \leq-2$ for all $i$. Let $n / a=\left[e_{1}, \ldots, e_{t}-1\right]$. If $e_{t} \geq 3$, then there are pairs $\left(B_{m_{i}, a_{i}}, B_{m_{i+1}, a_{i+1}}\right)$ of disjoint rational homology balls smoothly embedded in $V$, where $\left(m_{i}, a_{i}\right)$ and $\left(m_{i+1}, a_{i+1}\right)$ are consecutive pairs of Mori sequences associated to $n^{2} /(n a-$ 1). If, furthermore, $\Gamma$ is not of the form $\stackrel{-2}{\cdots} \cdots{ }^{-2}-3$ then there are infinitely many such pairs of disjoint rational homology balls.

Proof. We may assume that $V$ itself is a complex surface containing the linear chain consisting of complex rational curves.

Let $\mathbb{E}_{1}:\left(C_{1} \subset \mathscr{X}_{1}\right) \rightarrow(Q \in \mathscr{Y})$ be the usual initial flipping mk1A associated to $\Gamma$. According to Lemma 4.4, after a sequence of finite flips applied to $\left(C_{1} \subset \mathscr{X}_{1}\right) \rightarrow(Q \in \mathscr{Y})$, we have a deformation $\mathscr{Z} \rightarrow \mathbb{D}$ such that all of the fibers are smooth. Hence the central fiber $Z_{0}$ is diffeomorphic to a general fiber $Z_{t}(t \neq 0)$. Furthermore the central fiber $Z_{0}$ is equal to the regular neighborhood $V$. Therefore, since a flip changes only the central fiber, $X_{1, t}$ is diffeomorphic to $Z_{t}$, hence, to $V=Z_{0}$.

We may regard the $\operatorname{mk} 1 \mathrm{~A}\left(C_{1} \subset \mathscr{X}_{1}\right) \rightarrow(Q \in \mathscr{Y})$ as an initial flipping mk2A with one more Wahl singularity defined by the pair $(1,1)$. Let $\left(C_{i} \subset \mathscr{X}_{i}\right) \rightarrow(Q \in \mathscr{Y})(i \geq 1)$ be the mk2A with Wahl singularities defined by $\left(m_{i}, a_{i}\right)$ and $\left(m_{i+1}, a_{i+1}\right)$ in the Mori sequence of mk2A's starting from $\left(C_{1} \subset \mathscr{X}_{1}\right) \rightarrow(Q \in \mathscr{Y})$.

Notice that a general fiber $X_{i, t}$ 's $(t \neq 0)$ of $\mathscr{X}_{i} \rightarrow \mathbb{D}$ contains disjoint rational homology balls $B_{m_{i}, a_{i}}$ and $B_{m_{i+1}, a_{i+1}}$ and two general fibers $X_{i, t}$ and $X_{j, t}$ for $t \neq 0$ are diffeomorphic because this is a flip over $\mathbb{D}$. Therefore every $X_{i, t}$ is diffeomorphic to $V$. Hence there are two disjoint pairs of rational homology balls $\left(B_{m_{i}, a_{i}}, B_{m_{i+1}, a_{i+1}}\right)$ smoothly embedded in $V$, as asserted.

Furthermore, if $\Gamma$ is not of the form $\stackrel{-2}{\cdots} \cdots-3$ then $\delta>1$ by Lemma 4.3. Hence the Mori sequence for $\mathbb{E}_{1}$ has infinitely many mk2A's, which implies that there are infinitely many pairs of disjoint rational homology balls embedded in $V$. \(\square\)

Proposition 4.6. The embeddings in the above Theorem 4.5 are simple.
Proof. Let $\mathbb{E}_{i}:\left(C_{i} \subset \mathscr{X}_{i}\right) \rightarrow(Q \in \mathscr{Y})$ be the $i$-th flipping mk2A constructed in the proof of Theorem 4.5. We showed in the proof that a general fiber $X_{i, t}$ is diffeomorphic to the regular neighborhood $V$. Note that the rationally blown up $Z$ can be obtained from $V$ by a sequence of ordinary blowing ups. Hence the assertion follows. \(\square\)

Example 4.7. The usual initial flipping $\mathrm{mk} 2 \mathrm{~A} \mathbb{E}_{1}$ associated to $\begin{array}{llll}-3 & -3 & \text { is } & -3 \\ \bullet & -2 & -1 & -3\end{array}$ For example, the second $\mathrm{mk} 2 \mathrm{~A} \mathbb{E}_{2}$ is $\begin{array}{llllllllll}-3 & -7 & -2 & -2 & -3 & -2 & -1 & -3 & -5 & -2\end{array} \quad \begin{aligned} & -3 \\ & 0\end{aligned}$. The first flip on $\mathbb{E}_{1}$ is given by $\overbrace{}^{-3} \square^{-4}$. Then, the second flip induces the original linear chain $\stackrel{-3}{\bullet} \stackrel{-3}{\bullet}$.

Remark 4.8. One may construct other initial flipping mk2A's $\mathbb{E}_{1}\left(C \subset \mathscr{X}_{1}\right)$ associated to the given linear chain $\Gamma$ such that there is a sequence of flips $\mathscr{X}_{1} \xrightarrow[\rightarrow]{\text { flip }} \mathscr{X}_{2} \xrightarrow[\rightarrow]{\text { flip }} \xrightarrow[-\rightarrow]{\text { flip }} \mathscr{X}_{n}$ where the central fiber $X_{n, 0}$ of $\mathscr{X}_{n}$ is the regular neighborhood of the given linear chain $\Gamma$. For example, the linear chain $\stackrel{-3}{\bullet} \cdot-\frac{-4}{\bullet}$ has the usual one $[3,2,5,4,2]-1-3-2$ but also the new one $1-[4,2,5,4,2,2]-1-[4]-2$. So there are another Mori sequences associated to the given linear chain.

Remark 4.9. If $\Gamma=\stackrel{-2}{\cdots} \cdot-2$, then $B_{n, 1}$ and $B_{n+1,1}$ are smoothly embedded in $V$ by Proposition 2.14. We do not know whether there are more rational homology balls in $V$.

The following Corollary 4.10 and Theorem 4.11 generalize Khodorovskiy [6, Theorems 1.2, 1.3].

Corollary 4.10. Let $V_{-n}$ be a neighborhood of a 2-sphere with self-intersection number $(-n)$ for $n \geq 4$. Then there exist infinitely many pairs of disjoint rational homology balls smoothly embedded in $V_{-n}$. In particular, we have $B_{n-1,1} \hookrightarrow V_{-n}$. Furthermore, if $n=4$, then there is an embedding $B_{2 m+1,1} \hookrightarrow V_{-4}$ for any $m \geq 1$.

Proof. The numerical data for the initial mk1A associated to $\stackrel{-n}{\bullet}^{\text {is }}$ is $[(n-1,1)]-1-$ $[(1,1)]$, that is, $[n+1,2, \ldots, \overline{2}]$. So there is an embedding $B_{n-1,1} \hookrightarrow V_{-n}$. If $n=4$, then the numerical data for the initial mk 1 A is $[5, \overline{2}]$. So the Mori sequence can be described simply by
$$\cdots-[2 m+3, \overline{2}, 2, \ldots, 2]-\cdots-[5, \overline{2}]-\varnothing$$
where $m \geq 1$. Therefore $B_{2 m+1,1}(m \geq 1)$ is smoothly embedded in $V_{-4}$. \(\square\)

Theorem 4.11. For any integers $n, a$ with $n>a \geq 1$ and $(n, a)=1$, there are infinitely many pairs of disjoint rational homology balls $\left(B_{m_{i}, a_{i}}, B_{m_{i+1}, a_{i+1}}\right)$ smoothly embedded in $B_{n, a} \sharp \overline{\mathbb{C P}^{2}}$, where $\left(m_{i}, a_{i}\right)$ and $\left(m_{i+1}, a_{i+1}\right)$ are consecutive pairs of Mori sequences associated to the initial divisorial $m k 2 A$ with two Wahl singularities defined by the pairs $(n, a)$ and $\left(n^{2}, n a-1\right)$. In particular, $\left(m_{1}, a_{1}\right)=(n, a)$ and $\left(m_{2}, a_{2}\right)=\left(n^{2}, n^{2}-(n a-1)\right)$, that is, $B_{n, a} \sqcup B_{n^{2}, n a-1} \hookrightarrow B_{n, a} \sharp \overline{\mathbb{C P}}^{2}$. In particular, there is an embedding $B_{2 m, 1} \hookrightarrow B_{2,1} \sharp \overline{\mathbb{C P}}^{2}$ for any $m \geq 1$.

Proof. Let ( $Q \in Y$ ) be the Wahl singularity defined by the pair ( $n, a$ ). Let $V \rightarrow Y$ be the minimal resolution of $Q$ whose dual graph is given by
![](https://cdn.mathpix.com/cropped/3db73a83-7d4a-421e-a1c3-37829f0d2fa0-14.jpg?height=47&width=155&top_left_y=1147&top_left_x=984)
with $n^{2} /(n a-1)=\left[a_{1}, \ldots, a_{s}\right]$. By Corollary 2.2, after a sequence of appropriate blowing ups of $V$, we have a regular neighborhood $\widetilde{V}$ of the linear chain
![](https://cdn.mathpix.com/cropped/3db73a83-7d4a-421e-a1c3-37829f0d2fa0-14.jpg?height=73&width=415&top_left_y=1323&top_left_x=855)
with $\left(n^{2}\right)^{2} /\left(n^{2}(n a-1)-1\right)=\left[b_{1}, \ldots, b_{t}\right]$. Then we have an $\operatorname{mk} 2 \mathrm{~A} \mathbb{E}_{1}:(C \subset \mathscr{X}) \rightarrow(Q \in$ $\mathscr{Y})$ where there are two Wahl singularities on $C$ defined by the pairs $\left(n^{2}, n a-1\right)$ and $(n, a)$. Then $\delta=n>1$ and one can easily check that this $\operatorname{mk} 2 \mathrm{~A} \mathbb{E}_{1}$ is initial and of divisorial type.

Let $\mathbb{E}_{i}:\left(C_{i} \subset \mathscr{X}_{i}\right) \rightarrow(Q \in \mathscr{Y})$ be the mk2A in the Mori sequence for $\mathbb{E}_{1}$. By Proposition 2.5, there is a blow-down $X_{i, t} \rightarrow Y_{t}(t \neq 0)$ of a $(-1)$-curve between two smooth fibers. Note that $Y_{t}=B_{n, a}$ and there are two disjoint rational homology balls in $X_{i, t}$.

If $n=2$ and $a=1$, then the Mori sequence is just
$$\cdots-[2 m+2, \overline{2}, 2, \ldots, 2]-\cdots-[6, \overline{2}, 2]-[4]$$
where $m \geq 1$. Therefore $B_{2 m, 1}(m \geq 1)$ is smoothly embedded in $B_{2,1} \sharp \overline{\mathbb{C P}}^{2}$. Hence the assertion follows. \(\square\)

The above theorem generalizes Owens [8, Theorem 4] which asserts that there is an embedding $B_{n^{2}, n-1} \hookrightarrow B_{n, 1} \sharp \overline{\mathbb{C} \mathbb{P}^{2}}$.

On the other hand, Owens $[8, § 5]$ extends the notion of simple to embeddings of the form $B_{p, q} \hookrightarrow B_{p^{\prime}, q^{\prime}} \not \sqcup \overline{\mathbb{C} \mathbb{P}^{2}}$ as follows: The embedding $B_{p, q} \hookrightarrow B_{p^{\prime}, q^{\prime}} \nmid \overline{\mathbb{C} \mathbb{P}^{2}}$ is said to be simple if the resulting rational blow-up of $B_{p, q}$ has the same effect as rationally blowing up $B_{p^{\prime}, q^{\prime}}$, together with a sequence of ordinary blow-ups.

Proposition 4.12. The embeddings $B_{m_{i}, a_{i}} \hookrightarrow B_{n, a} \sharp \overline{\mathbb{C P}^{2}}$ in the above Theorem 4.11 are simple for $i>1$.

Proof. As in the proof of Theorem 4.11, let $\mathbb{E}_{i}:\left(C_{i} \subset \mathscr{X}_{i}\right) \rightarrow(Q \in \mathscr{Y})(i \geq 2)$ be the divisorial mk2A with two Wahl singularities $P_{1}$ and $P_{2}$ defined by the pairs $\left(m_{i}, a_{i}\right)$ and ( $m_{i+1}, a_{i+1}$ ) respectively over ( $Q \in \mathscr{Y}$ ) where $Q \in Y_{0}$ is a Wahl singularity defined by the
pair $(n, a)$. If we smooth out $P_{1} \in C_{i} \subset X_{i, 0}$ but keep $P_{2}$, then the mk2A $\mathbb{E}_{i}$ deforms to a divisorial $\operatorname{mk} 1 \mathrm{~A} \mathbb{E}_{i}^{\prime}:\left(C_{i}^{\prime} \subset \mathscr{X}_{i}^{\prime}\right) \rightarrow(Q \in \mathscr{Y})$ with one Wahl singularity defined by the pair $\left(m_{i}, a_{i}\right)$. Then the two embeddings $B_{m_{i}, a_{i}} \hookrightarrow B_{n, a} \sharp \overline{\mathbb{C} \mathbb{P}^{2}}$ via the mk2A $\mathbb{E}_{i}$ and the mk1A $\mathbb{E}_{i}^{\prime}$ are equivalent to each other.

Let $B_{m_{i}, a_{i}} \hookrightarrow B_{n, a} \sharp \overline{\mathbb{C P}^{2}}$ be the embedding obtained via the mk1A $\mathbb{E}_{i}^{\prime}$. The rational blowup along $B_{m_{i}, a_{i}}$ is equivalent to taking the minimal resolution of $P_{i} \in X_{i, 0}^{\prime}$ on the central fiber $X_{i, 0}^{\prime}$ of $\mathbb{E}_{i}^{\prime}$, which is equivalent to taking the minimal resolution $Q \in Y_{0}$ followed by a sequence of ordinary blow-ups. So the assertion follows. \(\square\)

\section*{5. Rational homology balls in Milnor fibers}

We show that there are infinitely many rational homology balls smoothly embedded in the Milnor fibers of certain cyclic quotient surface singularities and the embeddings are non-simple. Thus there is also little obstruction to embedding rational homology balls in smooth 4-manifolds in a 'non-simple' way.

Theorem 5.1. Let $(Q \in Y)$ be a cyclic quotient surface singularity which admits an extremal $P$-resolution $f^{+}: X^{+} \rightarrow Y$ with one Wahl singularity defined by the pair ( $m^{\prime}, a^{\prime}$ ). Then there are infinitely many pairs of disjoint rational homology balls smoothly embedded in the Milnor fiber $M$ associated to the $P$-resolution $X^{+} \rightarrow Y$ and all of these embeddings are non-simple.

Proof. Let $(-c)$ be the self-intersection number of the strict transform of the exceptional divisor of $f^{+}$in the minimal resolution of $X^{+}$. We define an $\operatorname{mk} 2 \mathrm{~A} \mathbb{E}_{1}:\left(C_{1} \subset \mathscr{X}_{1}\right) \rightarrow$ $(Q \in \mathscr{Y})$ by the numerical data $\left(m_{1}, a_{1}\right)=(1,1)$ and $\left(m_{2}, a_{2}\right)=\left(c m^{\prime}-a^{\prime}, m^{\prime}-a^{\prime}\right)$. Then $\delta=c m^{\prime}-m^{\prime}-a^{\prime}<0$ (for $c \geq 2$ and $m^{\prime}>a^{\prime}$ ) and $\delta m_{1}-m_{2}=-m^{\prime}<0$. Therefore $\mathbb{E}_{1}$ is initial and flipping such that, on its flip $\left(C_{1} \subset \mathscr{X}_{1}\right) \rightarrow\left(C^{+} \subset \mathscr{X}^{+}\right)$, the extremal $P$ -resolution $X^{+}$is the central fiber of $\mathscr{X}^{+} \rightarrow \mathbb{D}$.

Notice that there are infinitely many entries $\mathbb{E}_{i}:\left(C_{i} \subset \mathscr{X}_{i}\right) \rightarrow(Q \in \mathscr{Y})(i \geq 1)$ of mk2A's in the Mori sequence starting $\mathbb{E}_{1}$ and that $M \cong X_{t}^{+} \cong X_{i, t}$ for $0 \neq t \in \mathbb{D}$. Hence there are infinitely many pairs of disjoint rational homology balls induced from $\mathbb{E}_{i}$ for $i \geq 1$ smoothly embedded in $M$.

Suppose that an embedding $B \hookrightarrow M$ is induced from an $\operatorname{mk} 2 \mathrm{~A} \mathbb{E}:(C \subset \mathscr{X}) \rightarrow(Q \in \mathscr{Y})$ in the Mori sequence starting from $\mathbb{E}_{1}$. As in the proof of Proposition 4.12, the embedding $B \hookrightarrow M$ is indeed induced from an $\operatorname{mk} 1 \mathrm{~A} \mathbb{E}^{\prime}:\left(C^{\prime} \subset \mathscr{X}^{\prime}\right) \rightarrow(Q \in \mathscr{Y})$ obtained by deforming the mk2A $\mathbb{E}$ by Urzúa [13, Proposition 2.12].

Let $Z$ be the rationally blown-up of the 4-manifold from $M$ along $B$. Then, by construction, $Z$ is diffeomorphic to the minimal resolution of the central fiber $X_{0}^{\prime}$ of $\mathscr{X}^{\prime} \rightarrow \mathbb{D}$ (where $K_{X_{0}^{\prime}}$ is negative), which can be obtained from the minimal resolution of $Y$ by a sequence of ordinary blow-ups. Therefore $M$ must be diffeomorphic to the minimal resolution of $Y$, but then $M$ is the Milnor fiber of the Artin component, and so the P-resolution is smooth, a contradiction. \(\square\)

\section*{References}
\begin{itemize}
\item[] [1] Evans, Jonathan David; Smith, Ivan; Markov numbers and Lagrangian cell complexes in the complex projective plane. Geom. Topol. 22 (2018), no. 2, 1143-1180.
\item[] [2] Evans, Jonathan David; Urzúa, Giancarlo; Antiflips, mutations, and unbounded symplectic embeddings of rational homology balls. arXiv:1807.06073.
\item[] [3] Hacking, Paul; Prokhorov, Yuri; Smoothable del Pezzo surfaces with quotient singularities. Compos. Math. 146 (2010), no. 1, 169-192.
\end{itemize}
[4] Hacking, Paul; Tevelev, Jenia; Urzúa, Giancarlo; Flipping surfaces. J. Algebraic Geom. 26 (2017), no. 2, 279-345.
[5] Khodorovskiy, Tatyana; Symplectic rational blow-up and embeddings of rational homology balls. Doctoral dissertation (2012), Harvard University.
[6] Khodorovskiy, Tatyana; Smooth embeddings of rational homology balls. Topol. Appl. 161 (2014), 386-396.
[7] Kollár, Janos; Shepherd-Barron, Nicholas I.; Threefolds and deformations of surface singularities. Invent. Math. 91 (1988), no. 2, 299-338.
[8] Owens, Brendan; Equivariant embeddings of rational homology balls. Q. J. Math. 69 (2018), no. 3, 1101-1121.
[9] Owens, Brendan; Corrigendum to: Equivariant embeddings of rational homology balls. arXiv:1906.05913.
[10] Park, Heesang; Park, Jongil; Shin, Dongsoo; Smoothly embedded rational homology balls. J. Korean Math. Soc. 53 (2016), no. 6, 1293-1308.
[11] Park, Heesang; Park, Jongil; Shin, Dongsoo; Urzúa, Giancarlo; Milnor fibers and symplectic fillings of quotient surface singularities. Adv. Math. 329 (2018), 1156-1230.
[12] Park, Heesang; Shin, Dongsoo; Rational homology balls in 2-handlebodies. Bull. Korean Math. Soc. 54 (2017), no. 6, 1927-1933.
[13] Urzúa, Giancarlo, Identifying neighbors of stable surfaces. Ann. Sc. Norm. Super. Pisa Cl. Sci. (5) 16 (2016), no. 4, 1093-1122.
[14] Urzúa, Giancarlo, $\mathbb{Q}$-Gorenstein smoothings of surfaces and degenerations of curves. Rend. Semin. Mat. Univ. Padova 136 (2016), 111136.
[15] Wahl, Jonathan; Smoothing of normal surface singularities. Topology 20 (1981), 219-246.
Department of Mathematics, Konkuk University, Seoul 05029, Republic of Korea \& Ko-rea Institute for Advanced Study, Seoul 02455, Republic of Korea
E-mail address: HeesangPark@konkuk.ac.kr
Department of Mathematics, Chungnam National University, Daejeon 34134 \& Korea Institute for Advanced Study, Seoul 02455, Republic of Korea
E-mail address: dsshin@cnu.ac.kr
Facultad de Matemáticas, Pontificia Universidad Católica de Chile, Santiago, Chile
E-mail address: urzua@mat.uc.cl
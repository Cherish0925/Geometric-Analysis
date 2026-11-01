---
retention_scope: session
part: 1
total_parts: 2
---

[Part 1/2 of: Constructing Rational Homology 3-Spheres That Bound Rational Homology 4-Balls]

---
source_file: 2208_14850.pdf
converter: mathpix
format: mmd
---

\title{
Constructing Rational Homology 3-Spheres That Bound Rational Homology 4-Balls
}

\author{
Lisa Lokteva
}

18th January 2024

\begin{abstract}
We present three large families of new examples of plumbed 3-manifolds that bound rational homology 4-balls. These are constructed using two operations, also defined here, that preserve the lack of a lattice embedding obstruction to bounding rational homology balls. Apart from in the cases shown in this paper, it remains open whether these operations are rational homology cobordisms in general.

The families of new examples include a multitude of families of rational surgeries on torus knots, and we explicitly describe which positive torus knots we now know to have a surgery that bounds a rational homology ball.

While not the focus of this paper, we implicitly confirm the slice-ribbon conjecture for new, more complicated, examples of arborescent knots, including many Montesinos knots.
\end{abstract}

\section*{1 Introduction}

In Kirby's problem 4.5 [14], Casson asks which rational homology 3-spheres bound rational homology 4-balls. While rational homology 3-spheres abound in nature, including the $r$-surgery $S_{r}^{3}(K)$ on a knot $K$ for any $r \in \mathbb{Q}-\{0\}$, very few of them actually bound rational homology balls. In fact, Aceto and Golla showed in [2, Theorem 1.1], that for every knot $K$ and every $q \in \mathbb{Z}_{+}$, there exist at most finitely many $p \in \mathbb{Z}_{+}$such that $S_{p / q}^{3}(K)$ bounds a rational homology ball. It is hard to answer Casson's question in full generality, but recently a great deal of progress has been made on specific classes of rational homology 3-spheres. For example, in 2007 we learnt the answer for lens spaces [17, 18], in 2020 for positive integral surgeries on positive torus knots [2, 3], and in between we learnt the answer for several other classes on Seifert fibred spaces with three exceptional fibres [15, 16]. We do not yet know the answer for general Seifert fibred spaces with three exceptional fibres. In [19], the author started studying surgeries on algebraic (iterated torus) knots, which are not Seifert fibred but decompose into Seifert fibred spaces when cut along a maximal system of incompressible tori [12].

An important tool to study which 3-manifolds bound rational homology balls is the following well-known corollary of Donaldson's diagonalisation theorem [8, Theorem 1]:

Proposition 1 (Corollary of Donaldson's Theorem). Let $Y$ be a rational homology 3-sphere and $Y=\partial X$ for $X$ a negative definite smooth connected oriented 4-manifold. If $Y=\partial W$ for a smooth rational homology 4-ball $W$, then there exists a lattice embedding
$$\left(H_{2}(X) / \text { Torsion, } Q_{X}\right) \hookrightarrow\left(\mathbb{Z}^{\mathrm{rk} H_{2}(X)},-\mathrm{Id}\right) .$$
Here, $Q_{X}$ is the intersection form on $H_{2}(X) /$ Torsion. Determining which 3-manifolds in a family $\mathfrak{F}$ bound rational homology 4-balls using lattice embeddings often goes like this:
\begin{itemize}
\item[(i)] Find a negative definite filling $X(Y)$ for every $Y \in \mathfrak{F}$.
\item[(ii)] Guess the family $\mathfrak{F}^{\prime} \subset \mathfrak{F}$ of manifolds whose filling's intersection lattice (that is second homology with the intersection form) embeds into the standard lattice of the same rank.
\item[(iii)] Show that $\left(H_{2}(X(Y)), Q_{X(Y)}\right)$ does not embed into $\left(\mathbb{Z}^{b_{2}(X(Y))},-\mathrm{Id}\right)$ for any $Y \in \mathfrak{F}-\mathfrak{F}^{\prime}$.
\item[(iv)] Hopefully prove that $Y$ bounds a rational homology ball for any $Y \in \mathfrak{F}^{\prime}$.
\end{itemize}

Every step of this process has the potential to go wrong. For starters, there exist 3-manifolds without any definite fillings [10]. However, lens spaces, surgeries on torus knots and large surgeries on algebraic knots do have definite fillings. In fact, they all bound definite plumbings of disc bundles on spheres. Step (iv) is not guaranteed to work either. For example, $S_{-m^{2}}^{3}(K)$ bounds the knot trace $D_{-m^{2}}^{4}(K)\left(D^{4}\right.$ with a $-m^{2}$-framed 2-handle glued along $K$ ) which has intersection lattice $\left(\mathbb{Z},\left(-m^{2}\right)\right)$ which embeds into $(\mathbb{Z},-\mathrm{Id})$, but according to [2, Theorem 1.2], $S_{-m^{2}}^{3}(K)$ bounds a rational homology ball for at most two positive integer values of $m$. However, in [17, 18, 2, 3] the authors managed to find a different filling $X(Y)$ for each $Y$ in such a way that the lattice embedding obstruction turned out perfect. These $X(Y)$ s have been plumbings of disc bundles on spheres with a tree-shaped plumbing graph, moreover satisfying the property that the quantity
$$I=\sum_{v \in V}(-w(v)-3),$$
where $V$ is the set of vertices of the graph and $w(v)$ is the weight of $v$, would be negative.

Steps (ii) and (iii) can sometimes be done at the same time, but often, like in [3] where $\mathfrak{F}$ is the set of positive integral surgeries on positive torus knots, they cannot. It is then important to eliminate embeddable cases early in order to proceed with step (iii). Theorem 1.1 in [3], the classification of positive integral surgeries on positive torus knots bounding rational homology balls, lists 5 families that are Seifert fibred spaces with 3 exceptional fibres. They bound a negative definite starshaped plumbing with three legs. Families (1)-(3) have two complementary legs, that is two legs whose weight sequences are Riemenschneider dual (defined, for the reader's convenience, in Section 2 of this paper). All such 3-manifolds that bound a
rational homology ball have been classified by Lecuona in [15]. Family (5) contains two exceptional graphs which were known to bound rational homology balls both because they arise as boundaries of tubular neighbourhoods of rational cuspidal curves in [9] and because they are surgeries on torus knots $T(p, q)$ where $q \equiv \pm 1$ $(\bmod p)$, which were studied in [2]. However, Family (4) took the authors of [3] a while to find, in the meantime thwarting their attempts at step (iii). Eventually they found Family (4) using a computer. This allowed them to finish off their lattice embedding analysis, but Family (4) still looked surprising and strange and begged the question of "How could we have predicted its existence?"

\subsection*{1.1 GOCL and IGOCL Moves}

This work came out of widening the perspective and asking which boundaries of 4-manifolds described by plumbing trees with negative definite intersection forms and low $I$ bound rational homology balls. As a preliminary question, we asked ourselves which plumbing trees generate an embeddable intersection lattice. We looked at what the graphs of 3-manifolds we know to bound rational homology balls look like and tried to see if there are any common patterns. In [16, Remark 3.2], Lecuona describes how to get all lens spaces that bound rational homology balls from the linear graphs (-2, -2, -2), (-3, -2, -3, -3, -3), (-3, -2, -2, -3) and (-2, -2, -3, -4) using some modifications. (She restates Lisca's result in [17] in the language of plumbing graphs rather than fractions $p / q$ for $L(p, q)$.) In this paper we define a couple of moves called GOCL and IGOCL moves on embedded plumbing graphs that preserve embeddability and generalise the moves described by Lecuona. From this point of view, Lecuona's list simply turns into a list of IGOCL and GOCL moves that keep the graph linear. The IGOCL move was also used by Jonathan Simone in [25] under the name of expansions. The GOCL move is a generalisation of Lisca's expansions in [17].

Now, we may ask ourselves if these moves preserve the property of the described 3-manifolds bounding rational homology balls. There is unfortunately no obvious rational homology cobordism between two 3-manifolds differing by a GOCL or an IGOCL move. We can however prove that repeated applications of these moves to the embeddable linear graphs (-3, -2, -3, -3, -3), (-3, -2, -2, -3) and (-2, -2, -3, -4) give 3-manifolds bounding rational homology balls. This results in the following theorem:

Theorem A. All 3-manifolds described by the plumbing graphs in Figures 1, 2 and 3 bound rational homology balls.

Remark. See Definition 9 for the definition of complementary.
There are several methods to prove this theorem. The easiest one, which we can call The Simple Method, uses the following proposition, which follows from the long exact sequence of the pair combined with Poincaré duality and the Universal Coefficient Theorem:

Proposition 2 (The Simple Method). If a 4-manifold X consists of one 0-handle, $n$ 1-handles, and $n$ 2-handles, and if $\partial X$ is a rational homology $S^{3}$, then $X$ is a rational homology ball.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/2cbcc31b-ba59-4f5d-b0e3-4b51a86cb997-04.jpg?height=749&width=1110&top_left_y=404&top_left_x=470}
\captionsetup{labelformat=empty}
\caption{Figure 1: These are the graphs obtainable by performing IGOCL and GOCL moves on the linear graph (-3, -2, -3, -3, -3). Here the length of the chain of -2's is $k \geq$ $0,\left(a_{1}, \ldots, a_{m_{1}}\right)$ and $\left(\alpha_{1}, \ldots, \alpha_{m_{2}}\right)$ are complementary sequences, and $\left(b_{1}, \ldots, b_{n_{1}}\right)$ and $\left(\beta_{1}, \ldots, \beta_{n_{2}}\right)$ are complementary sequences.}
\end{figure}

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/2cbcc31b-ba59-4f5d-b0e3-4b51a86cb997-04.jpg?height=647&width=1357&top_left_y=1633&top_left_x=346}
\captionsetup{labelformat=empty}
\caption{Figure 2: The form of all graphs obtainable from (-3, -2, -2, -3) using GOCL moves. Here the sequences $\left(a_{1}, \ldots, a_{l_{1}}\right)$ and $\left(\alpha_{1}, \ldots, \alpha_{l_{2}}\right)$ are complementary, as well as the sequences $\left(b_{1}, \ldots, b_{m_{1}}\right)$ and $\left(\beta_{1}, \ldots, \beta_{m_{2}}\right)$, and the sequences $\left(z_{1}, \ldots, z_{n_{1}}\right)$ and $\left(\zeta_{1}, \ldots, \zeta_{n_{2}}\right)$.}
\end{figure}

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/2cbcc31b-ba59-4f5d-b0e3-4b51a86cb997-05.jpg?height=733&width=739&top_left_y=305&top_left_x=656}
\captionsetup{labelformat=empty}
\caption{Figure 3: The form of all graphs obtainable from (-2, -2, -3, -4) by GOCL and IGOCL moves. Here the length of the chain of -2's is $k \geq 0,\left(a_{1}, \ldots, a_{m_{1}}\right)$ and $\left(\alpha_{1}, \ldots, \alpha_{m_{2}}\right)$ are complementary sequences, and $\left(b_{1}, \ldots, b_{n_{1}}\right)$ and $\left(\beta_{1}, \ldots, \beta_{n_{2}}\right)$ are complementary sequences.}
\end{figure}

We use this by showing that we may perform two integral surgeries on the threemanifolds described by these plumbing trees and obtain $\left(S^{1} \times S^{2}\right) \#\left(S^{1} \times S^{2}\right)$. This method works for every one of the families of Figures 1, 2 and 3.

A more refined method is to show that the above plumbed 3-manifolds are double covers of $S^{3}$ branched over a $\chi$-slice link, that is a link bounding a surface $S$ of Euler characteristic 1 in $D^{4}$ [7, Definition 1]. By [7, Proposition 5.1], the double cover of $D^{4}$ branched over a surface of Euler characteristic 1 is a rational homology 4-ball. We use this method, described in Subsection 3.2, and more specifically Proposition 16, for the graphs in Figures 1 and 2. Given the way we construct $S$ in this paper, this method amounts to The Simple Method, but with the extra step of showing that we can perform the surgeries equivariantly under an involution. This extra step is quite challenging, and we do not at this moment know if we can perform it on the family of Figure 3. The bonus of using this, more difficult, method is that we obtain new examples of links that are $\chi$-ribbon in the process.

The families of Figures 1, 2 and 3, together with the one generated by GOCL moves from (-2, -2, -2), include all lens spaces bounding rational homology balls. The (-2, -2, -2) family, however, only includes linear graphs already found by Lisca. On the other hand, the families of Figures 1, 2 and 3 also contain more complicated graphs. In [1], Aceto defines linear complexity of a plumbing tree to be the minimal number of vertices we need to remove in order to get a linear graph. Our families have linear complexities up to 2. Many papers, e.g. [1, 2, 3, 16, 25], that use lattice embeddings to obstruct plumbed 3-manifolds from bounding a rational homology ball have used arguments of the form "If my graph $\Gamma$ is embeddable, then this other linear graph obtained from $\Gamma$ is embeddable, and we know what those look like.", which gets harder to do the further $\Gamma$ is away from being linear. Thus,
we do not yet really have lattice embedding obstructions for families of graphs of complexity greater than 1. The families of Theorem A include many graphs of Seifert fibred spaces. They include Family (4) in [3] and predict its existence because Family (4) is just the intersection between the set of graphs in Figures 1, 2 and 3 and the negative definite plumbing graphs of positive integral surgeries on positive torus knots.

As mentioned above, there is no obvious rational homology cobordism between the 3-manifolds described by two plumbing graphs differing by a GOCL or an IGOCL move. This is interesting in comparison with the case in the works by Aceto 0 and Lecuona [15]. Lecuona shows that given a plumbing graph $\Gamma$, you can modify it to a graph $\Gamma^{\prime}$ by subtracting 1 from the weight of a vertex $v$ and attaching two complementary legs $\left(-a_{1}, \ldots,-a_{m}\right)$ and $\left(-b_{1}, \ldots,-b_{n}\right)$ (see Section 2 or [15] for definitions) to $v$, and the 3-manifolds $Y_{\Gamma}$ and $Y_{\Gamma^{\prime}}$ described by the graphs will be rational homology cobordant, that is bound a rational homology 4-ball if and only if the other one does. Thus, if she wants to know if a $Y_{\Gamma^{\prime}}$, for $\Gamma^{\prime}$ a graph with two complementary legs coming out of the same vertex, bounds a rational homology ball, she can reduce it to the same question for a simpler graph. However, since we do not know if the GOCL and IGOCL moves are rational homology cobordisms, we cannot play this trick for complementary legs growing out of different vertices.

Another work that has shown that applying GOCL moves to embedded plumbing graphs bounding certain rational homology balls gives us new plumbed 3-manifolds that bound rational homology balls is [4] by Akbulut and Larson. They show that the families $\Sigma(2,4 n+1,12 n+5)$ and $\Sigma(3,3 n+1,12 n+5)$ of Brieskorn spheres bound rational homology balls. In fact, these families are obtained by applying GOCL moves to the plumbing graphs of $\Sigma(2,5,17)$ and $\Sigma(3,4,17)$. Just like us in Section 3, they perform a surgery on their spaces and the result of this surgery is the same for each space, in their case a 0-surgery on the figure-eight knot. Their lemma [4, Lemma 2], saying that any integral homology sphere obtained from a surgery on a 0-surgery on a rationally slice knot, can be viewed as a generalisation of The Simple Method and Proposition 2 when $n=1$. With the same technique as Akbulut and Larson, Şavk [24] constructed two more families $\Sigma(2,4 n+3,12 n+7)$ and $\Sigma(3,3 n+2,12 n+7)$ of Brieskorn spheres that bound rational homology balls. These are obtainable from $\Sigma(2,7,19)$ and $\Sigma(3,5,19)$, respectively, using IGOCL moves.

\subsection*{1.2 Rational Surgeries on Torus Knots}

An interesting generalisation of [3, Theorem 1.1], would be to classify all positive rational surgeries on positive torus knots that bound rational homology balls. Theorem A allows us to construct more examples of such surgeries than is sightly to write down. Instead, we may ask ourselves the following question:

Question 3. For which $1<p<q$ with $\operatorname{GCD}(p, q)=1$ is there an $r \in \mathbb{Q}_{+}$such that $S_{r}^{3}(T(p, q))$ bounds a rational homology ball?

Section 4 is dedicated to showing the following theorem:

Theorem B. For the following pairs $(p, q)$ with $1<p<q$ and $\operatorname{GCD}(p, q)=1$, there is at least one $r \in \mathbb{Q}_{+}$such that $S_{r}^{3}(T(p, q))$ bounds a rational ball. Here $k, l \geq 0$.
\begin{itemize}
\item[1.] $(k+2,(l+1)(k+2)+1)$
\item[2.] $(k+2,(l+2)(k+2)-1)$
\item[3.] $(2 k+3,(l+1)(2 k+3)+2)$
\item[4.] $(2 k+3,(l+2)(2 k+3)-2)$
\item[5.] $\left(k^{2}+7 k+11, k^{3}+12 k^{2}+45 k+51\right)$
\item[6.] $\left(S_{l+1}^{(k)}, S_{l+2}^{(k)}\right)$ for $\left(S_{i}^{(k)}\right)$ a sequence defined by $S_{0}^{(k)}=1, S_{1}^{(k)}=2, S_{2}^{(k)}=2 k+7$ and $S_{i+2}^{(k)}=(k+4) S_{i+1}^{(k)}-S_{i}^{(k)}$.
\item[7.] $\left(T_{l+1}^{(k)}, T_{l+2}^{(k)}\right)$ for $\left(T_{i}^{(k)}\right)$ a sequence defined by $T_{0}^{(k)}=1, T_{1}^{(k)}=k+2, T_{2}^{(k)}=$ $k^{2}+6 k+7$ and $T_{i+2}^{(k)}=(k+4) T_{i+1}^{(k)}-T_{i}^{(k)}$.
\item[8.] $\left(U_{l+1}, U_{l+2}\right)$ for $\left(U_{i}\right)$ a sequence defined by $U_{0}=1, U_{1}=3, U_{2}=14$ and $U_{i+2}=5 U_{i+1}-U_{i}$.
\item[9.] $\left(R_{l+1}, R_{l+2}\right)$ for $\left(R_{i}\right)$ a sequence defined by $R_{0}=1, R_{1}=3, R_{2}=17$ and $R_{i+2}=6 R_{i+1}-R_{i}$.
\item[10.] $\left(P_{l+1}, P_{l+2}\right)$ for $\left(P_{i}\right)$ a sequence defined by $P_{0}=1, P_{1}=4, P_{2}=19$ and $P_{i+2}=5 P_{i+1}-P_{i}$.
\item[11.] $\left(Q_{l+1}, Q_{l+2}\right)$ for $\left(Q_{i}\right)$ a sequence defined by $Q_{0}=1, Q_{1}=2, Q_{2}=9$ and $Q_{i+2}=5 Q_{i+1}-Q_{i}$.
\item[12.] $(A,(n+1) Q+P)$ for $P$ and $Q$ such that $L(Q, P)$ bounds a rational homology ball (or equivalently $\frac{Q}{P}$ lying in Lisca's set $\mathcal{R}$ [17]), and $A$ a multiplicative inverse to either $Q$ or $n Q+P$ modulo $(n+1) Q+P$ such that $0<A<$ $(n+1) Q+P$.
\item[13.] $((n+1) Q+P,(l+1)((n+1) Q+P)+A)$ for $P$ and $Q$ such that $L(Q, P)$ bounds a rational homology ball (or equivalently $\frac{Q}{P}$ lying in Lisca's set $\mathcal{R}$ [17]), and A a multiplicative inverse to either $Q$ or $n Q+P$ modulo $(n+1) Q+P$ such that $0<A<(n+1) Q+P$.
\item[14.] $(B, P)$ for $P$ and $Q$ such that $L(Q, P)$ bounds a rational homology ball (or equivalently $\frac{Q}{P}$ lying in Lisca's set $\mathcal{R}$ [17]), and $B$ a multiplicative inverse to either $P\left\lceil\frac{Q}{P}\right\rceil-Q$ or $Q-P\left\lfloor\frac{Q}{P}\right\rfloor$ modulo $P$ such that $0<B<P$.
\item[15.] $(P,(l+1) P+B)$ for $P$ and $Q$ such that $L(Q, P)$ bounds a rational homology ball (or equivalently $\frac{Q}{P}$ lying in Lisca's set $\mathcal{R}$ [17]), and $B$ a multiplicative inverse to either $P\left\lceil\frac{Q}{P}\right\rceil-Q$ or $Q-P\left\lfloor\frac{Q}{P}\right\rfloor$ modulo $P$ such that $0<B<P$.
\end{itemize}
\begin{itemize}
\item[16.] $(P, Q)$ such that there is a number $n$ such that $(P, Q, n) \in \mathcal{R} \sqcup \mathcal{L}$ for the sets $\mathcal{R}$ and $\mathcal{L}$ defined in [3, Theorem 1.1]. (Note that here $r=n \in\{P Q, P Q-$ $1, P Q+1\}$, so we are looking at an integral surgery.)
\end{itemize}

The curious reader can use the methods of Section 4 to obtain the surgery coefficients $r$ too.

In Theorem B, case 16 is shown to bound rational homology balls in [3] and reflects the degenerate cases of surgeries on torus knots that are lens spaces or connected sums of lens spaces, cases 12-15 are shown to bound rational homology balls in [15] because their graphs have a pair of complementary legs, while the cases [1-11] are shown to bound rational homology balls in this paper, using that there exists an $r$ such that $S_{r}^{3}(T(p, q))$ bounds a graph in the families of Figures 1, 2 and 3. The authors of [3] classified all positive integral surgeries on positive torus knots that bound rational homology balls. The classification included 18 families, whereof families (6)-(18) are included in our family 16, family (4) in our family 9, and the others in families 1 and 2.

At the moment of writing we do not know of any other positive torus knots having positive surgeries bounding rational homology balls. The pair $(8,19)$ is in some metric the smallest example not to appear on the list of Theorem B. Thus we may concretely ask:

Question 4. Is there an $r \in \mathbb{Q}_{+}$such that $S_{r}^{3}(T(8,19))$ bounds a rational homology ball?

We may also note that some positive torus knots have many surgeries that bound rational homology balls. For example, Theorem A allows us to construct numerous finite and infinite families of surgery coefficients $r \in \mathbb{Q}_{+}$such that $S_{r}^{3}(T(2,3))$ bounds a rational homology ball. All we need to do is to choose weights in the graphs in Figures 3, 2 and 1 so that we get a starshaped graph with three legs whereof one is (-2) and another is either (-2, -2) or (-3). For example $S_{\frac{(11 k+20)^{2}}{22 k^{2}+79 k+71}}^{3}(T(2,3))$ bounds a plumbing of the shape in Figure 3 with $\left(b_{1}, \ldots, b_{m_{1}}\right)=(4)$ and $\left(a_{1}, \ldots, a_{n_{1}}\right)=(3)$, and thus bounds a rational homology ball for any $k \geq 0$. There are also surgeries on $T(2,3)$ that bound rational balls, but do not have graphs of the shapes of Figures 1, 2 or 3. For example, we have $S_{\frac{64}{7}}^{3}(T(2,3))=-S_{64}^{3}(T(3,22))$, which bounds a rational homology ball because it is the boundary of the tubular neighbourhood of a rational curve in $\mathbb{C} P^{2}$ [9], but whose lattice embedding contains a basis vector with coefficient 2 , which we do not get by applying GOCL or IGOCL moves to (-2, -2, -3, -4), (-3, -2, -2, -3) and (-3, -2, -3, -3, -3). The lattice embedded plumbing graph of $S_{\frac{64}{7}}^{3}(T(2,3))$ does however fit into Family $\mathcal{C}$ of [26] of symplectically embeddable plumbings. Unfortunately, Family $\mathcal{C}$ of [26] contains both surgeries on $T(2,3)$ that bound rational homology balls and ones that do not. For example, $S_{\frac{169}{25}}^{3}(T(2,3))$ of [26, Section 2.4, Figure 12] does not bound a rational ball despite bounding a plumbing with an embeddable intersection form. A later paper [6] classified which surgeries on $T(2,3)$ appearing in Family $\mathcal{C}$, viewed as surface singularity links, bound a rationally acyclic Milnor fibre. Interestingly, all but two of the embedded graphs in that family are
generated by applying IGOCL moves to the graph of $S_{\frac{64}{7}}^{3}(T(2,3))$. However, we do not know if any other members of Family $\mathcal{C}$ bound a rational homology ball which is not a Milnor fibre. Hence, the following is a rich open question worth studying:

Question 5. For which $r \in \mathbb{Q}_{+}$does $S_{r}^{3}(T(2,3))$ bound a rational homology ball?

\subsection*{1.3 Outline}

We start off the paper with Section 2 by recalling some results on complementary legs and the basics of the lattice embedding setup. In Section 3 we define the GOCL and IGOCL moves and show Theorem A. In Section 4 we prove Theorem B for the families 1, 11, while the other families follow directly from [15] and [3].

\section*{Acknowledgements}

This research was carried out by the author when she was a PhD student at the University of Glasgow, funded by the College of Science and Engineering. This is an updated version of a part of her thesis.

\section*{2 Complementary Legs and Lattice Embeddings}

In this section we list some definitions and easy propositions that are helpful to understanding the paper. We recall the definition of lattice embeddings and apply it to plumbing graphs and complementary legs. In this section, we assume that the reader is familiar with plumbings of disc bundles over spheres and how to convert plumbing diagrams into Kirby diagrams. (If not, see [11, Example 4.6.2].)

Notation 6. Given a forest-shaped plumbing graph $\Gamma$ with weight function $W$ : $V \rightarrow \mathbb{Z}$, we may associate to it a 4-manifold $X_{\Gamma}$ by describing its Kirby diagram. First, we draw a small unknot at each vertex of $\Gamma$. Then, for each edge, we create a Hopf linking between the knots corresponding to the edge ends as in Figure 4. We denote the resulting link by $L_{\Gamma}$. Then $X_{\Gamma}$ is the simply-connected 4-manifold obtained by attaching 2-handles with framing $W(v)$ to the unknot at each vertex $v$.

We denote the 3-manifold $\partial X_{\Gamma}$ by $Y_{\Gamma}$.
Remark 6.1. A common abuse of terminology is "the plumbing graph $\Gamma$ bounds a rational homology ball", which means that $Y_{\Gamma}$ bounds a rational homology ball.

Let $\Gamma$ be a forest-shaped plumbing graph. The second homology of $X_{\Gamma}$ is the free abelian group $\mathbb{Z}\left\langle V_{1}, \ldots, V_{k}\right\rangle$ on the vertices and the intersection form is
$$\left\langle V_{i}, V_{j}\right\rangle_{Q_{X}}= \begin{cases}\text { weight of } V_{i} & \text { if } i=j \\ 1 & \text { if } V_{i} \text { is adjacent to } V_{j} \\ 0 & \text { otherwise. }\end{cases}$$

Definition 7. Let $X$ be a 4-manifold with boundary. A lattice embedding
$$f:\left(H_{2}(X) / \text { Torsion, } Q_{X}\right) \hookrightarrow\left(\mathbb{Z}^{N},-\mathrm{Id}\right)$$

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/2cbcc31b-ba59-4f5d-b0e3-4b51a86cb997-10.jpg?height=461&width=604&top_left_y=326&top_left_x=725}
\captionsetup{labelformat=empty}
\caption{Figure 4: Kirby diagram associated to a plumbing.}
\end{figure}
is a linear map $f$ such that $\left\langle V_{i}, V_{j}\right\rangle_{Q_{X}}=\left\langle f\left(V_{i}\right), f\left(V_{j}\right)\right\rangle_{- \text {Id }}$. We will simply denote $\langle\cdot, \cdot\rangle:=\langle\cdot, \cdot\rangle_{\text {-Id }}$. If nothing else is specified, then $N=\operatorname{rk} H_{2}(X)$, that is the number of vertices in the graph.

Common abuses of notation include "embedding of the graph", meaning an embedding of the lattice $\left(H_{2}(X) /\right.$ Torsion, $\left.Q_{X}\right)$, where $X=X_{\Gamma}$ for a plumbing graph $\Gamma$.

Knowing when a lattice embedding exists is useful because of Proposition 1 in the introduction.

Now we turn our heads to lattice embeddings of specific plumbing graphs, namely pairs of complementary legs.

Definition 8. We define the negative continued fraction $\left[a_{1}, \ldots, a_{n}\right]^{-}$as
$$\left[a_{1}, \ldots, a_{n}\right]^{-}=a_{1}-\frac{1}{a_{2}-\frac{1}{\ddots-\frac{1}{a_{n}}}}$$

Negative continued fractions often show up in low-dimensional topology because of the slam-dunk Kirby move [11, Figure 5.30], which allows us to substitute a rational surgery on a knot by an integral surgery on a link.

Definition 9. A two-component weighted linear graph $\left(-\alpha_{1}, \ldots,-\alpha_{n}\right),\left(-\beta_{1}, \ldots,-\beta_{k}\right)$ (with $\alpha_{i}, \beta_{j}$ integers greater than or equal to 2) is called a pair of complementary legs if
$$\frac{1}{\left[\alpha_{1}, \ldots, \alpha_{n}\right]^{-}}+\frac{1}{\left[\beta_{1}, \ldots, \beta_{k}\right]^{-}}=1 .$$
We call the sequence $\left(\beta_{1}, \ldots, \beta_{k}\right)$ the Riemenschneider dual or complement of the sequence $\left(\alpha_{1}, \ldots, \alpha_{n}\right)$, and we call the fractions $\left[\alpha_{1}, \ldots, \alpha_{n}\right]^{-}$and $\left[\beta_{1}, \ldots, \beta_{k}\right]^{-}$complementary.

Definition 10. A Riemenschneider diagram is a finite set of points $S$ in $\mathbb{Z}_{+} \times \mathbb{Z}_{-}$ such that $(1,-1) \in S$ and for every point $(a, b) \in S$ but one, exactly one of $(a+1, b)$
or $(a, b-1)$ is in $S$. If $(n, k) \in S$ is the point with the largest $n-k$, we say that the Riemenschneider diagram represents the fractions $\left[\alpha_{1}, \ldots, \alpha_{n}\right]^{-}$and $\left[\beta_{1}, \ldots, \beta_{k}\right]^{-}$, where $\alpha_{i}$ is one more than the number of points with $x=i$ and $\beta_{j}$ is one more than the number of points with $y=-j$.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/2cbcc31b-ba59-4f5d-b0e3-4b51a86cb997-11.jpg?height=513&width=746&top_left_y=578&top_left_x=660}
\captionsetup{labelformat=empty}
\caption{Figure 5: Example of a Riemenschneider diagram representing the complementary fractions [5, 3, 2, 2] ${ }^{-}$and [2, 2, 2, 3, 4] ${ }^{-}$.}
\end{figure}

Example 11. See Figure 5 for an example of a Riemenschneider diagram.
Proposition 12 (Riemenschneider [23]). The two fractions represented by a Riemen-schneider diagram are complementary.

Remark 12.1. Note that given any continued fraction $\left[\alpha_{1}, \ldots, \alpha_{n}\right]^{-}$with all $\alpha_{i} \geq 2$, we may construct a Riemenschneider diagram representing $\left[\alpha_{1}, \ldots, \alpha_{n}\right]^{-}$and its Riemenschneider dual.

The following theorem is well-known, but we explicitly write out the embedding construction for the reader's convienience.

Proposition 13. Every pair of complementary legs has a lattice embedding.
Proof. The embedding can be constructed algorithmically from a Riemenschneider diagram. Denote the vertices of the two complementary legs by $\left(U_{1}, \ldots, U_{m_{1}}\right)$ and $\left(V_{1}, \ldots, V_{m_{2}}\right)$. These vertices generate the second homology of the plumbed 4-manifold described by the graph. We need to send every vertex to an element of $\mathbb{Z}\left\langle e_{1}, \ldots, e_{m_{1}+m_{2}}\right\rangle$. We will construct this embedding recursively through "partial embeddings", which are maps $f:\left\{U_{1}, \ldots, U_{m_{1}}, V_{1}, \ldots, V_{m_{2}}\right\} \rightarrow \mathbb{Z}\left\langle e_{1}, \ldots, e_{m_{1}+m_{2}}\right\rangle$ such that $\langle f(X), f(X)\rangle \geq$ weight of $X$.

Order the points in the Riemenschneider diagram so that $P_{1}=(1,-1)$, and if $P_{i}=(a, b)$, then point $P_{i+1}$ is either $(a+1, b)$ or ( $a, b-1$ ). Now, we recursively build an embedding as follows.
\begin{itemize}
\item[-] Start by mapping both $U_{1}$ and $V_{1}$ to $e_{1}$.
\item[-] For each non-final $i$, if the current partial embedding is $\left(u_{1}, \ldots, u_{n}\right),\left(v_{1}, \ldots, v_{k}\right)$ (meaning that $\left(U_{1}, \ldots, U_{n}\right)$ gets mapped to $\left(u_{1}, \ldots, u_{n}\right)$ and $\left(V_{1}, \ldots, V_{k}\right)$ gets
\end{itemize}
\begin{itemize}
\item[] mapped to $\left.\left(v_{1}, \ldots, v_{k}\right)\right)$ and $P_{i}=(a, b)$ is such that $P_{i+1}=(a+1, b)$, then the new partial embedding will be $\left(u_{1}, \ldots, u_{n}+e_{i+1}\right),\left(v_{1}, \ldots, v_{k}-e_{i+1}, e_{i+1}\right)$. If $P_{i+1}=(a, b-1)$, then the new partial embedding will be $\left(u_{1}, \ldots, u_{n}-\right.$ $\left.e_{i+1}, e_{i+1}\right),\left(v_{1}, \ldots, v_{k}+e_{i+1}\right)$ instead.
\item[-] If $P_{i}$ is final and the current partial embedding is $\left(u_{1}, \ldots, u_{n}\right),\left(v_{1}, \ldots, v_{k}\right)$, the new embedding will be $\left(u_{1}, \ldots, u_{n}+e_{i+1}\right),\left(v_{1}, \ldots, v_{k}-e_{i+1}\right)$. (Or the other way around, as this sign choice is arbitary.)
\end{itemize}

It is easy to see that an embedding $\left(u_{1}, \ldots, u_{m_{1}}\right),\left(v_{1}, \ldots, v_{m_{2}}\right)$ constructed this way will have the properties:
\begin{itemize}
\item[-] Each $u_{i}$ for $i=1, \ldots, n-1$ and $v_{j}$ for $j=1, \ldots, k$ will be a sum of consecutive basis vectors, all but the last one with coefficient 1, and the last one with coefficient -1. Meanwhile, $u_{n}$ will be a sum of consecutive basis vectors, all with coefficient 1.
\item[-] If the Riemenschneider diagram represents the fractions $\left[\alpha_{1}, \ldots, \alpha_{n}\right]^{-}$and $\left[\beta_{1}, \ldots, \beta_{k}\right]^{-}$, then $\left\langle u_{i}, u_{i}\right\rangle=-\alpha_{i}$ and $\left\langle v_{j}, v_{j}\right\rangle=-\beta_{j}$.
\item[-] Since $u_{i}$ and $u_{i+1}$ have exactly one basis vector in common, one with a positive coefficient and one with a negative one, $\left\langle u_{i}, u_{i+1}\right\rangle=1$, and similarly $\left\langle v_{i}, v_{i+1}\right\rangle=1$.
\item[-] The other pairs $\left(u_{i}, u_{j}\right)$ (with $|i-j|>1$ ) don't share basis vectors and are thus orthogonal. Similarly, the pairs $\left(v_{i}, v_{j}\right)$ with $|i-j|>1$ don't share basis vectors and are thus orthogonal.
\item[-] It is easy to show by induction on the construction that $\left\langle u_{i}, v_{j}\right\rangle=0$ for all $i, j$.
\end{itemize}
These properties show that we are in fact looking at a lattice embedding of the complementary legs. \(\square\)

Remark 13.1. In fact, if $e_{1}$ is fixed to hit the first vertex of each complementary leg, the rest of the embedding is unique up to renaming of elements and sign of the coefficient [5, Lemma 5.2].

The following facts are useful when dealing with lattice embeddings. We will often use these properties without citing them. The first fact follows from reversing the Riemenschneider diagram, the second from embedding the sequences $\left(a_{m}, \ldots, a_{1}\right)$ and $\left(b_{n}, \ldots, b_{1}\right)$ as in Proposition 13 and mapping the -1-weighted vertex to $-e_{1}$, and the rest from looking at a Riemenscheider diagram.

Proposition 14. Let $\left(a_{1}, \ldots, a_{m}\right)$ and $\left(b_{1}, \ldots, b_{n}\right)$ be complementary sequences. Then the following hold:
\begin{itemize}
\item[1.] The sequences $\left(a_{m}, \ldots, a_{1}\right)$ and $\left(b_{n}, \ldots, b_{1}\right)$ are complementary.
\item[2.] The linear graph $\left(-a_{1}, \ldots,-a_{m},-1,-b_{n}, \ldots,-b_{1}\right)$ embeds in $\left(\mathbb{Z}^{m+n},-\mathrm{Id}\right)$.
\end{itemize}
\begin{itemize}
\item[3.] Either $a_{m}$ or $b_{n}$ must equal 2, so assume without loss of generality that $b_{n}=2$. Blowing down the -1 in the linear graph $\left(-a_{1}, \ldots,-a_{m},-1,-b_{n}, \ldots,-b_{1}\right)$ gives us the linear graph $\left(-a_{1}, \ldots,-\left(a_{m}-1\right),-1,-b_{n-1}, \ldots,-b_{1}\right)$. This graph is once again a pair of complementary legs linked by a -1, described by the Riemenschneider diagram obtained by the removing the last point.
\item[4.] Repeatedly blowing down the -1 in linear graphs of the form
$$\left(-a_{1}, \ldots,-a_{m},-1,-b_{n}, \ldots,-b_{1}\right)$$
eventually takes us to ( $-2,-1,-2$ ), or even further to ( $-1,-1$ ) or ( 0 ).
\item[5.] Similarly, blowing up next to the -1 gives the linear graph
$$\left(-a_{1}, \ldots,-\left(a_{m}+1\right),-1,-2,-b_{n}, \ldots,-b_{1}\right)$$
or
$$\left(-a_{1}, \ldots,-a_{m},-2,-1,-\left(b_{n}+1\right), \ldots,-b_{1}\right)$$
, which are both pairs of complementary legs connected by a -1, described by Riemenschneider diagrams that are expansions of the initial one by one dot.
\end{itemize}

\section*{3 Growing Complementary Legs on Lisca's Graphs}

The idea for this work comes from studying the lattice embeddings of linear graphs and other trees that are known to bound rational homology 4-balls. Consider for example Lisca's classification of connected linear graphs that bound rational homology 4-balls [17], in the most convenient form for us described by Lecuona in [16, Remark 3.2]. Every family of embeddable graphs can be obtained from the basic graphs (-2, -2, -2), (-2, -2, -3, -4), (-3, -2, -2, -3) and (-3, -2, -3, -3, -3) by repeated application of two types of moves, one of which is the following: choose a basis vector $e$ hitting exactly two vertices $v$ and $w$, where $w$ is final (Lisca's word for leaf, that is a vertex of degree 1 [17, p. 6]), subtract 1 from the weight of $v$ and attach a new vertex $u$ of weight -2 to $w$. I will show that we can do away with the assumption that $w$ is final and still get 3-manifolds bounding rational homology 4-balls through repeating this operation.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/2cbcc31b-ba59-4f5d-b0e3-4b51a86cb997-13.jpg?height=348&width=422&top_left_y=2094&top_left_x=815}
\captionsetup{labelformat=empty}
\caption{Figure 6: Lisca's (-2, -2, -3, -4) graph with embedding.}
\end{figure}

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/2cbcc31b-ba59-4f5d-b0e3-4b51a86cb997-14.jpg?height=352&width=727&top_left_y=301&top_left_x=661}
\captionsetup{labelformat=empty}
\caption{Figure 7: An expansion of Lisca's (-2, -2, -3, -4) graph with embedding.}
\end{figure}

Example 15. Consider Figure 6, showing an embedding of Lisca's (-2, -2, -3, -4) graph into the standard lattice $\left(\mathbb{Z}\left\langle e_{1}, e_{2}, e_{3}, e_{4}\right\rangle,-\mathrm{Id}\right)$. Note that $e_{4}$ and $e_{3}$ hit two vertices each. Choose $e_{4}$. We can now perform the operation described above by choosing $v$ to be the vertex of weight -4 and $w$ the vertex of weight -3. The result is shown in Figure 7 together with its embedding, which is a kind of "expansion" of the embedding in Figure 6. Our new embedding has two basis vectors hitting exactly two vertices each, namely $e_{3}$ and $f_{1}$, whereas $e_{4}$ now hits three vertices. We may now perform the same operation again on any of these basis vectors, thereby obtaining any graph of the form described in Figure 3, with $k=0$. We will show that these graphs do not only have lattice embeddings, but also bound rational homology 4-balls.

\subsection*{3.1 GOCL and IGOCL moves}

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/2cbcc31b-ba59-4f5d-b0e3-4b51a86cb997-15.jpg?height=1011&width=934&top_left_y=507&top_left_x=569}
\captionsetup{labelformat=empty}
\caption{Figure 8: A GOCL move on a graph with a lattice embedding.}
\end{figure}

We will now introduce two moves on forest-shaped plumbing graphs with a lattice embedding. Let $\Gamma=(V, E, W)$ be a weighted negative definite graph with lattice embedding $F:\left(V, Q_{X_{\Gamma}}\right) \rightarrow\left(\mathbb{Z}^{|V|},-\mathrm{Id}\right)$. Assume that there is a basis vector $e$ of $\mathbb{Z}^{|V|}$ hitting exactly two vertices $A$ and $B$ in $\Gamma$, whose images are $v$ and $w$, in any order we prefer. Then a GOCL (growth of complementary legs) operation is constructing an embedded graph $\left(\Gamma^{\prime}=\left(V^{\prime}, E^{\prime}, W^{\prime}\right), F^{\prime}\right)$ by $V^{\prime}=V \cup C, E^{\prime}=$ $E \cup\{A C\}$ and $u:=F^{\prime}(C)=-\langle e, v\rangle e-f, w^{\prime}:=F^{\prime}(B)=w-\langle e, v\rangle\langle e, w\rangle f$ and $F^{\prime}(D)=F(D)$ for all $D \in V-\{B\}$. This move is illustrated by Figure 8. Note that $\langle e, v\rangle\langle e, w\rangle=\langle f, u\rangle\left\langle f, w^{\prime}\right\rangle$. Thus, the GOCL operation substitutes $e$ by $f$ in the set of basis vectors hitting the graph exactly twice and moreover, the sign difference between the two occurrences of the basis vector is preserved. This operation can therefore be applied repeatedly. If we start with the graph consisting of two vertices of weight -2 and no edges, and the embedding $e_{1}-e_{2}$ and $e_{1}+e_{2}$, then repeated application of GOCL will simply give us two complementary legs.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/2cbcc31b-ba59-4f5d-b0e3-4b51a86cb997-16.jpg?height=753&width=915&top_left_y=370&top_left_x=561}
\captionsetup{labelformat=empty}
\caption{Figure 9: An IGOCL move on a graph with a lattice embedding.}
\end{figure}

The other operation which we will call IGOCL (inner growth of complementary legs) could be described as growing complementary legs from the inside. Suppose a basis vector $e$ hits exactly three vertices $A, B$ and $C$ in $\Gamma$, with their images under the lattice embedding $F$ being $u, v$ and $w$ respectively. Assume also that $B$ and $C$ are adjacent and that $\langle v, e\rangle\langle w, e\rangle=-1$, that is $e$ hits $v$ and $w$ with opposite signs. Then $\Gamma^{\prime}=\left(V^{\prime}, E^{\prime}, W^{\prime}\right)$ is described by $V^{\prime}=V \cup\{D\}, E^{\prime}=$ $(E-\{B C\}) \cup\{B D, D C\}, F^{\prime}(D)=-\langle v, e\rangle e+\langle v, e\rangle f, F^{\prime}(C)=w-\langle w, e\rangle e+\langle w, e\rangle f$, $F^{\prime}(A)=u+\langle u, e\rangle f$ and $F^{\prime}(X)=F(X)$ for all $X \in V-\{A, C\}$. This operation is illustrated in Figure 9. After this operation is performed, we can perform it again on either $e$ or $f$, but the result is essentially the same. What it does is grow a chain of -2's between two vertices and compensate by subtracting from the weight of a different vertex. If we apply the IGOCL operation on a vector hitting a pair of complementary legs three times, we still get a pair of complementary legs, which explains the name.

\subsection*{3.2 The Complicated Method to Show Theorem A}

Now that we have defined the GOCL and IGOCL moves, we want to apply them to Lisca's basic graphs, which are (-2, -2, -2), (-2, -2, -3, -4), (-3, -2, -2, -3), and (-3, -2, -3, -3, -3). We will show for each Lisca graph one by one that the results obtained from repeatedly applying the aforementioned operations always bound rational homology balls. Recall that this can be done for all families using The Simple Method of Proposition 2. This subsection explains The Complicated Method to do that, which has the bonus of showing the $\chi$-sliceness of some links including many Montesinos links not treated by Lecuona in [16].

A link in $S^{3}=\mathbb{R}^{3} \cup\{\infty\}$ is called strongly invertible if it is ambient isotopic to one which both is equivariant with respect to the 180° rotation around the $x$-axis
and fulfils the property that each component intersects the $x$-axis in exactly two points [20]. Now, recall Notation 6. If $\Gamma$ is a tree, then the link $L_{\Gamma}$ is strongly invertible. Let $D$ be some Kirby diagram of $X_{\Gamma}$ such that $L_{\Gamma}$ is in the equivariant position. For example, Figure 10 shows a possible diagram $D$ for the plumbing graph in Figure 7.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/2cbcc31b-ba59-4f5d-b0e3-4b51a86cb997-17.jpg?height=323&width=1041&top_left_y=593&top_left_x=511}
\captionsetup{labelformat=empty}
\caption{Figure 10: Proof that the attaching link of the graph in Figure 7 is strongly invertible.}
\end{figure}

Let $\pi_{D}: X_{\Gamma} \rightarrow X_{\Gamma}$ be the involution given by extending this 180° rotation around the $x$-axis and let $p_{D}: X_{\Gamma} \rightarrow X_{\Gamma} / \pi_{D}$ be the quotient map when we identify $x \sim \pi_{D}(x)$. By [20, Theorem 3], $X_{\Gamma} / \pi_{D}+\cong B^{4}$ and $p$ is a double covering, branched over a surface $S_{D} \subset B^{4}$. The surface $S_{D}$ can be drawn by attaching bands to a disc according to the bottom half of the rotation-equivariant drawing, adding as many half-twists as the weight of the corresponding unknot [20]. (See Figure 11.)

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/2cbcc31b-ba59-4f5d-b0e3-4b51a86cb997-17.jpg?height=417&width=1005&top_left_y=1446&top_left_x=548}
\captionsetup{labelformat=empty}
\caption{Figure 11: $S_{D}$ for $D$ the diagram in Figure 10 is a disc with five bands attached. It lives inside $B^{4}$ with the boundary lying on $S^{3}$, and the interior pushed inside $B^{4}$.}
\end{figure}

By $K_{D}$ we denote the link $K_{D}=S_{D} \cap S^{3}$. Note that $K_{D} \neq L_{\Gamma}$. Also note that $K_{D}=\partial S_{D}$ and that Figure 11 should be understood with the interior pushed into $B^{4}$. Third, note that $S_{D}$ and $K_{D}$ depend on the choice of $D$.

In [7, Definition 1], Donald and Owens define a useful generalisation of sliceness to links. We say that a link in $S^{3}$ is $\chi$-slice if it bounds a surface of Euler characteristic 1 without closed components in $B^{4}$. If the surface has no local maxima, we can call it $\chi$-ribbon. The usefulness of the notion of $\chi$-sliceness lies in the following proposition:

Proposition ([7, Proposition 2.6]). If $L$ is a non-zero-determinant link which bounds a surface $F \subset B^{4}$ with no closed components and of Euler characteristic 1, then $\Sigma_{2}\left(B^{4}, F\right)$ is a rational homology ball.

We now state the proposition at the heart of the complicated method to prove Theorem A:

Proposition 16 (The Complicated Method). Let $\Gamma$ be a tree-shaped negative-definite plumbing graph, and $D$ an equivariant Kirby diagram of $X_{\Gamma}$ as above. If we can equivariantly add $n 2$-handles with unknotted attaching circles to $D$ and obtain a Kirby diagram $D^{\prime}$ that describes the 3-manifold $\#^{n}\left(S^{1} \times S^{2}\right)$, then $K_{D}$ is $\chi$-ribbon, and thus $Y_{\Gamma} \cong \Sigma_{2}\left(S^{3}, K_{D}\right)$ bounds a rational homology ball.

Before we prove this proposition, let us state the following lemma, which is interesting in itself. This lemma follows directly from combining the Smith Conjecture (proven by Waldhausen in [27]) and [13, Proposition 5.1].
Lemma 17. If $L$ is a link such that $\Sigma_{2}\left(S^{3}, L\right) \cong \#^{n}\left(S^{1} \times S^{2}\right)$, then $L$ is the unlink of $n+1$ components.

Proof of Proposition 16. Since $\partial \Sigma_{2}\left(S^{3}, K_{D^{\prime}}\right) \cong \#^{n}\left(S^{1} \times S^{2}\right), K_{D^{\prime}}$ must, by Lemma 17, be the unlink of $n+1$ components. Since $S_{D^{\prime}}$ is obtained from $S_{D}$ by attaching bands, the attachment of bands yields a cobordism $\left(S^{3} \times I, B\right)$ from $\left(S^{3}, K_{D}\right)$ to $\left(S^{3}, K_{D^{\prime}}\right)$ with only index 1 critical points. Since $K_{D^{\prime}}$ is the unlink on $n+1$ components, it bounds $n+1$ discs in $B^{4}$. Let $S$ be the union of $B$ and these discs. It has no maxima and it retracts onto a graph with $n+1$ vertices and $n$ edges, implying that it has Euler characteristic 1. This shows that $K_{D}$ is $\chi$-ribbon, and thus, by [7, Proposition 2.6], $Y_{\Gamma} \cong \partial \Sigma\left(B^{4}, S\right)$, where $\Sigma\left(B^{4}, S\right)$ is a rational homology ball. □

\section*{3.3 (-2, -2, -2)}

This graph has embedding $\left(e_{1}-e_{2}, e_{2}-e_{3},-e_{1}-e_{2}\right)$. The only basis vector hitting twice is $e_{1}$ whose both occurrences are in final vertices. Thus applying the GOCL operation keeps the graph linear and all such graphs have been shown to be bounding rational homology balls by Lisca. In fact, these graphs describe the lens spaces $L\left(p^{2}, p q \pm 1\right)$, for $p>q>0$ with some orientation [17, Lemma 9.2].

\section*{3.4 (-3, -2, -3, -3, -3)}

In this subsection, we show the following proposition using The Complicated Method described in Subsection 3.2.

Proposition 18. Every 3-manifold described by the graph in Figure 1 bounds a rational homology 4-ball.

In particular, we will apply Proposition 16 to any graph $\Gamma$ in the family described by Figure 1. We will construct an equivariant (with respect to the 180° rotation around the $z$-axis) Kirby diagram $D^{\prime}$ of $S^{1} \times S^{2}$, with all components unknotted and intersecting the $z$-axis exactly twice, such that removing one of the components gives us a Kirby diagram $D$ of $X_{\Gamma}$.

The proof will be by Kirby calculus, so in Figure 12 we recall the effect of some blow-ups and blow-downs on Kirby diagrams. Recall that if there are $k$ strands of a link component (counted with sign) in a bunch that we are about to perform a ±1 blow up around, then the framing of that component increases by $\pm k^{2}$.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/2cbcc31b-ba59-4f5d-b0e3-4b51a86cb997-19.jpg?height=304&width=1451&top_left_y=295&top_left_x=300}
\captionsetup{labelformat=empty}
\caption{Figure 12: Useful blow-ups and blow-downs.}
\end{figure}

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/2cbcc31b-ba59-4f5d-b0e3-4b51a86cb997-19.jpg?height=543&width=1412&top_left_y=736&top_left_x=339}
\captionsetup{labelformat=empty}
\caption{Figure 13: Creating a 3-cycle.}
\end{figure}

Proof. Now, we start by the chain
$$(-b_{n_{1}}, \ldots,-b_{1},-(2+k),-1, \underbrace{-2, \ldots,-2}_{k},-\left(1+\beta_{1}\right),-\beta_{2}, \ldots,-\beta_{n_{2}}) .$$
Note that it consists of two Riemenschneider dual chains connected by a -1 , so by Proposition 14.4, it blows down to the (0) chain. Since the graph is a tree, the sign of the crossings doesn't matter yet. We will arrange the crossings around the $-(2+k)$-vertex as in Figure 13a. The chains $\left(-b_{2}, \ldots,-b_{n_{1}}\right)$ and $\left(-2, \ldots,-2,-\left(1+\beta_{1}\right),-\beta_{2}, \ldots,-b_{n_{2}}\right)$, on the other hand, since they are not relevant to the Kirby moves that follow, are represented by tiny squares that freely move on their respective components.

Now we apply the Kirby calculus of Figure 13. The diagram in Figure 13c can no longer be described by a plumbing graph where every vertex is a link component. In fact, the red, blue, and black components form a triple Hopf link. Let us perform a blow-up at the clasp between the blue and the black components. This is a negative clasp, so we need to perform the twisted blow-up of Figure 12c. We obtain Figure 14.

Now note that removing the amber -1-knot in Figure 14 yields the Kirby diagram of Figure 1 with $\left(a_{1}, \ldots, a_{m_{1}}\right)=(2)$. To obtain more general tuples $\left(a_{1}, \ldots, a_{m_{1}}\right)$, we will have to repeatedly blow up the clasps on the -1-weighted component. At the moment, both of these clasps in Figure 14 (in magenta) are negative and can be blown up using Figure 12c, an operation that substitutes a clasp by a -1-weighted ring with two negative clasps on either side. Thus, repeated blow-ups will give us a figure like Figure 14, but with the amber ring potentially

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/2cbcc31b-ba59-4f5d-b0e3-4b51a86cb997-20.jpg?height=721&width=613&top_left_y=343&top_left_x=756}
\captionsetup{labelformat=empty}
\caption{Figure 14}
\end{figure}
substituted by a longer chain. In any case, the link in this figure is strongly invertible, and removing the -1-weighted component yields the Kirby diagram of Figure 1. \(\square\)

\section*{3.5 (-3, -2, -2, -3)}

In this subsection, we show the following proposition:
Proposition 19. Every 3-manifold described by the graph in Figure 2 bounds a rational homology 4-ball.

This is done by applying Proposition 16 to graphs $\Gamma$ described by Figure 2. In particular, for each member of this family, we will construct a Kirby diagram $D^{\prime}$ that 1) describes the 3-manifold $\left(S^{1} \times S^{2}\right) \#\left(S^{1} \times S^{2}\right)$, 2) is equivariant with respect to the 180° rotation around the $z$-axis, 3) only consists of unknotted components that intersect the $z$-axis exactly twice, and 4) removing two of the components yields a Kirby diagram of $X_{\Gamma}$.

Proof. One Kirby diagram of $\left(S^{1} \times S^{2}\right) \#\left(S^{1} \times S^{2}\right)$ is a ( 0,0 )-framed unlink of two components. By Proposition 14.4, one of the unknots with framing 0 blows up to the chain
$$\left(-\beta_{m_{2}}, \ldots,-\beta_{2}, 1-\beta_{1}, 1-b_{1},-b_{2}, \ldots,-b_{m_{1}}\right),$$
which can be seen by noting that the above chain is one blow-up away from
$$\left(-\beta_{m_{2}}, \ldots,-\beta_{1},-1,-b_{1}, \ldots,-b_{m_{1}}\right) .$$
Our first move will be to link the other unknot with framing 0 to the component with framing $1-\beta_{1}$ using a blow-up, thus obtaining Figure 15a. In this figure,

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/2cbcc31b-ba59-4f5d-b0e3-4b51a86cb997-21.jpg?height=741&width=1454&top_left_y=319&top_left_x=296}
\captionsetup{labelformat=empty}
\caption{Figure 15: Creating a $\mathbb{Z}_{2}$-equivariant Kirby diagram of the Figure 2 with two extra 2-handles.}
\end{figure}

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/2cbcc31b-ba59-4f5d-b0e3-4b51a86cb997-21.jpg?height=358&width=1467&top_left_y=1233&top_left_x=306}
\captionsetup{labelformat=empty}
\caption{Figure 16: Zooming in on a part of Figure 15c and blowing up.}
\end{figure}
the chains $\left(-b_{2}, \ldots,-b_{m_{1}}\right)$ and $\left(-\beta_{2}, \ldots, \beta_{m_{2}}\right)$ are represented by tiny squares that freely move on their respective components and if there are two on the same one, they could even pass through each other. Figure 15b is obtained from Figure 15a by a simple isotopy. Note that the purple -1-weighted component is linked with the black and the blue ones with negative clasps. We may thus use Figure 12c to blow it up into an arbitrary chain of negative clasps as in Figure 15c.

Now, zoom into the lower part of Figure 15c and note that it looks like Figure 16a. It is isotopic to Figure 16b, which clearly blows up to Figure 16c. This shows that Figure 15c blows up to Figure 17a. Applying an isotopy of the link gives Figure 17b. The green and the black components are now linked positively. The -1-blowup that gets rid of this linking introduces a new component that links to the green and the black components with a negative and positive clasp respectively. Repeated blow-ups thus give us a chain with all clasps negative except the lowest one. We conclude that Figure 17c is a $\mathbb{Z} / 2 \mathbb{Z}$-equivariant blow-up of Figure 17b and hence of the $(0,0)$ surgery on the 2-component unlink, but we may also note that removing the two -1-weighted components in the "middle" of the purple and turquoise chains gives us a tree-shaped plumbing, namely the one in Figure 2. □

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/2cbcc31b-ba59-4f5d-b0e3-4b51a86cb997-22.jpg?height=872&width=1447&top_left_y=295&top_left_x=317}
\captionsetup{labelformat=empty}
\caption{Figure 17: Creating a $\mathbb{Z} / 2 \mathbb{Z}$-equivariant Kirby diagram of the Figure 2 with two extra 2 -handles.}
\end{figure}

\section*{3.6 (-2, -2, -3, -4)}

In this subsection, we show the following proposition:
Proposition 20. Every 3-manifold described by the graph in Figure 3 bounds a rational homology 4-ball.

This case will be shown in a much simpler way than the one used in Subsections 3.4 and 3.5. By Proposition 2, it is enough to show that performing two integral surgeries on the graphs in Figure 3 gives us $\left(S^{1} \times S^{2}\right) \#\left(S^{1} \times S^{2}\right)$.

Proof. Figure 18a shows the "spine" of Figure 3 as the orange, magenta, green, red, teal, and violet rings. Note that the complementary leg pairs are reduced to dark brown and olive green squares here. The weights of the rings with squares might be affected by the growth of the complementary legs. The blue ring with weight -1 is the first surgery we perform. This first choice of surgery is suggested to us by [5, Figures 17(5) and 17(6)], which provide equivariant surgeries on linear expansions of the graph ( $-2,-2,-3,-4$ ) that yield ( $S^{1} \times S^{2}$ ).

Blowing down the -1-weighted loop gives us Figure 18b. Now the red loop has weight -1 and we may blow it down. We continue blowing down the chain of -2s that follows until we reach Figure 18c. We blow down the orange loop and obtain Figure 18d.

Everything would be well now if only the little squares were not there, as we would have been able to blow down the figure to one 0-framed unknot. However, because we might have grown a two pairs of complementary legs on this figure, Figure 18d might not actually represent a Kirby diagram with any -1-framed loops to blow down.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/2cbcc31b-ba59-4f5d-b0e3-4b51a86cb997-23.jpg?height=2071&width=1294&top_left_y=355&top_left_x=387}
\captionsetup{labelformat=empty}
\caption{Figure 18: The blue component in Subfigure (a) and the black one in Subfigure (e) are the two surgeries performed to transform the 3-manifolds in Figure 3 into ( $S^{1} \times$ $\left.S^{2}\right) \#\left(S^{1} \times S^{2}\right)$.}
\end{figure}

Instead, we will find another surgery to perform and obtain $\left(S^{1} \times S^{2}\right) \#\left(S^{1} \times S^{2}\right)$. Here, it's easier to reason backwards. First, note that the 3-manifold in Figure 18e is $\left(S^{1} \times S^{2}\right) \#\left(S^{1} \times S^{2}\right)$. This can be seen by blowing down the black -1-loop, which would separate the green loop (now 0-framed) from the rest. The rest will be a (-1, -1)-chain with two complementary legs grown on it, which always blows down to (0). Now, note that repeated blow-ups of Figure 18e near the black -1-framed loop allows us to obtain Figure 18d with an extra -1-framed surgery. This extra -1-framed surgery is the one we need to perform in order to obtain $\left(S^{1} \times S^{2}\right) \#\left(S^{1} \times S^{2}\right)$, completing our proof with The Simple Method. \(\square\)

While all the links of Figure 18 appear possible to arrange in an equivariant way, the reader should note that we did not equivariantly add the two extra 2-handles at the same time. Finding an appropriate equivariant diagram $D^{\prime}$ for using Proposition 16 has proven difficult. It is currently unknown if $K_{D}$ is $\chi$-slice for any equivariant Kirby diagram $D$ of $X_{\Gamma}$.

\section*{4 Proof of Theorem B}

In this section, we prove Theorem B by studying the intersection between the graphs in Figures 2, 1, and 3, and plumbing graphs of positive rational surgeries on positive torus knots. First we describe the plumbing graphs of the surgeries on torus knots, and then we go through the intersections with the graphs in Figures 2, 1 and 3 one by one. The change of order compared to Section 3 is because some families obtained from Figure 1 are subfamilies of families obtained from Figure 2.

\subsection*{4.1 Plumbing Graphs of Rational Surgeries on Torus Knots}

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/2cbcc31b-ba59-4f5d-b0e3-4b51a86cb997-24.jpg?height=498&width=455&top_left_y=1700&top_left_x=805}
\captionsetup{labelformat=empty}
\caption{Figure 19: A Kirby diagram with boundary $S_{n}^{3}(T(p, \alpha))$ where $n=\left[N_{1}+\right.$ $\left.p \alpha, N_{2}, \ldots, N_{k}\right]^{-}$and $K=T(p, \alpha)$, here drawn for $k=5$.}
\end{figure}
In order to find the intersection between the plumbing graphs of rational surgeries on torus knots and the graphs obtained from Lisca's graphs by repeated GOCL and IGOCL moves, we need to know what the plumbing graphs of rational surgeries on torus knots look like. Let $n>0$ be a rational number. We want to find a plumbing graph for $S_{n}^{3}(T(p, \alpha))$. We can write $n=\left[N_{1}+p \alpha, N_{2}, \ldots, N_{k}\right]^{-}$for $N_{2}, \ldots, N_{k} \geq 2$.

The 3 -manifold $S_{n}(T(p, \alpha))$ bounds the 4-manifold in Figure 19, which is positive-definite if $n>0$. Now, we will use the same technique as in [19, Section 3] in order to produce a definite plumbing graph. In the process, we need to measure how far we are from being definite, so the following definition is useful.

Definition 21. The positive/negative index of a 4-manifold is the number of positive/negative eigenvalues of its intersection form.

The argument of [19, Section 3] that the blow-ups decrease the surgery coefficient by a constant still holds to show that $S_{n}^{3}(T(p, \alpha))$ bounds the 3-manifold described by the graph in Figure 20.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/2cbcc31b-ba59-4f5d-b0e3-4b51a86cb997-25.jpg?height=294&width=1347&top_left_y=883&top_left_x=352}
\captionsetup{labelformat=empty}
\caption{Figure 20: A plumbing graph of $S_{n}^{3}(T(p, \alpha))$, where $\alpha>p$. Here $\left[1, c_{2}, \ldots, c_{s}\right]^{-}=$ $p / \alpha,\left[d_{1}, \ldots, d_{t}\right]^{-}=\alpha / p$ and $\left[N_{1}, \ldots, N_{k}\right]^{-}=N=n-p \alpha$. In particular, the pair of fractions $\left(\left[c_{2}, \ldots, c_{s}\right]^{-},\left[d_{1}, \ldots, d_{t}\right]^{-}\right)$are complementary. Also, we can write $\left[\left(c_{2}, c_{3}, \ldots, c_{s}\right)=\left(-2^{\left[d_{1}-2\right]}, a_{1}+1, a_{2}, \ldots, a_{r}\right)\right.$ so that $\left[a_{1}, \ldots, a_{r}\right]^{-}$and $\left[d_{2}, \ldots, d_{t}\right]^{-}$ are complementary.}
\end{figure}

The positive index of this graph is $k$ by the same logic as in [19, Section 3]. To obtain a definite graph, we will need the following generalisation of the algorithm in [19, Figure 2]:

Proposition 22. Let $\Gamma$ be a tree-shaped plumbing graph containing a chain (a connected linear subgraph with no nodes, that is vertices of degree greater than 2) $\left(-\alpha_{1}, \ldots,-\alpha_{k}\right)$, as in Figure 21a. Let $\Gamma^{\prime}$ be the graph $\Gamma$ with the chain substituted by the chain $\left(\beta_{1}, \ldots, \beta_{j}\right)$, for $\left[\alpha_{1}, \ldots, \alpha_{k}\right]^{-}$and $\left[\beta_{1}, \ldots, \beta_{j}\right]^{-}$complementary fractions, and the weight of the vertices adjacent to the chain increased by 1. Then $Y_{\Gamma}=Y_{\Gamma^{\prime}}$. Moreover, $b_{+}^{2}\left(X_{\Gamma^{\prime}}\right)=b_{+}^{2}\left(X_{\Gamma}\right)+j$ and $b_{-}^{2}\left(X_{\Gamma^{\prime}}\right)=b_{-}^{2}\left(X_{\Gamma}\right)-k$.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/2cbcc31b-ba59-4f5d-b0e3-4b51a86cb997-26.jpg?height=594&width=1136&top_left_y=319&top_left_x=458}
\captionsetup{labelformat=empty}
\caption{Figure 21: The graphs above bound the same 3-manifold if $\left[\alpha_{1}, \ldots, \alpha_{k}\right]^{-}$and $\left[\beta_{1}, \ldots, \beta_{j}\right]^{-}$are complementary fractions.}
\end{figure}

Example. Before sketching the proof, we will provide an example of the algorithm that we use to change such a chain. Start with the linear graph (-2, -4, -2). Right now, all vertices have negative weights. We want to introduce a positively weighted vertex. Let us perform a 1-blow-up. We obtain $(1,-1,-4,-2)$. Now, we blow down the -1 and obtain (2, -3, -2). We perform a 1-blow-up between the 2 and the -3 and obtain (3, 1, -2, -2). Blowing up a 1 again between the last positively weighted vertex and the first negatively weighted one gives us (3, 2, 1, -1, -2). We blow down the -1 to get (3, 2, 2, -1) and again to obtain (3, 2, 3). We note that every time we perform a 1-blow-up, we increase both the positive index and the number of positive vertices by 1 , and every time we perform a -1-blowdown, we decrease both the negative index and the number of negative vertices by 1. Thus, changing these 3 negative vertices into 3 positive ones decreased the negative index by 3 and increased the positive index by 3.

Proof sketch. This proposition follows from the fact that blow-ups and blow-downs do not change the boundary 3-manifold, together with the algorithm of 1) performing a 1-blow-up at the right of the rightmost chain element greater than 1, 2) blowing down any -1-weighted vertices, and 3) repeating. Following the Riemen-schneider diagram, we see that this algorithm gradually substitutes a sequence by its Riemenschneider dual. Blowing up by 1 increases both the positive index and the number of vertices with positive weight by 1, and blowing down a -1 decreases both the number of vertices with negative weight and the negative index by 1. Thus, substituting the $k$ negative-weighted vertices by $j$ positive-weighted ones substracts $k$ from the negative index and adds $j$ to the positive index. \(\square\)

If $N>1$ and thus $N_{1} \geq 2$, we can use Proposition 22 to substitute the chain $\left(N_{1}, \ldots, N_{k}\right)$ with its negative Riemenschneider complement $\left(-M_{1}, \ldots,-M_{j}\right)$ and obtain the negative definite graph in Figure 22. If $0<N<1$, then the sequence $\left(N_{1}, \ldots, N_{k}\right)$ starts with a 1 possibly followed by some 2's that we can blow down before turning the rest of the chain negative. This will once again give us a negative definite graph, namely the one in Figure 23.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/2cbcc31b-ba59-4f5d-b0e3-4b51a86cb997-27.jpg?height=296&width=1368&top_left_y=309&top_left_x=343}
\captionsetup{labelformat=empty}
\caption{Figure 22: A negative definite plumbing graph of $S_{n}^{3}(T(p, \alpha))$, where $N=n-p \alpha>1$ and $\alpha>p$. Here $\left[1, c_{2}, \ldots, c_{s}\right]^{-}=p / \alpha,\left[d_{1}, \ldots, d_{t}\right]^{-}=\alpha / p$ and if $N=n-p \alpha=a / b$ with $a, b \in \mathbb{Z}_{>0}$, then $\left[M_{1}, \ldots, M_{j}\right]^{-}=\frac{a}{a-b}$.}
\end{figure}

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/2cbcc31b-ba59-4f5d-b0e3-4b51a86cb997-27.jpg?height=343&width=1359&top_left_y=865&top_left_x=346}
\captionsetup{labelformat=empty}
\caption{Figure 23: A negative definite plumbing graph of $S_{n}^{3}(T(p, \alpha))$, where $\alpha>p$ and $0<N<1$. Here $\left[1, c_{2}, \ldots, c_{s}\right]^{-}=p / \alpha,\left[d_{1}, \ldots, d_{t}\right]^{-}=\alpha / p$ and the fraction $\left[P_{1}, \ldots, P_{j}\right]^{-}$is complementary to $\frac{1}{1-N}=\left[N_{2}, \ldots, N_{k}\right]^{-}$. In fact, that means that $N=\frac{1}{\left[P_{1}, \ldots, P_{j}\right]^{-}}$.}
\end{figure}

If $N<0$, that is $N_{1} \leq 0$, then turning the positively-weighted vertices $\left(N_{2}, \ldots, N_{k}\right)$ negative will not be enough to decrease the positive index to 0. Instead, we will use Proposition 22 to turn the two other legs of our graph positive, and we obtain the graph in Figure 24, which has negative index 1. If $N_{1}=0$, we will perform a 0-absorption (see [21, Proposition 1.1]) and obtain the positive definite graph in Figure 25. If $N_{1} \leq 2$, we use Proposition 22 to turn it into a chain of 2s and obtain the graph in Figure 26. If $N_{1}=-1$, we simply blow it down and obtain Figure 26, but with the length of the chain of 2s being 0.

In the graphs of Figures 22,23, 25 and 26, the vertex of degree 3 is called the

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/2cbcc31b-ba59-4f5d-b0e3-4b51a86cb997-27.jpg?height=344&width=1338&top_left_y=2054&top_left_x=355}
\captionsetup{labelformat=empty}
\caption{Figure 24: A plumbing graph of $S_{n}^{3}(T(p, \alpha))$, where $\alpha>p$ and $N<0$. Here the negative index is $1,\left[d_{1}, \ldots, d_{t}\right]^{-}=\alpha / p$ and $\left[e_{1}, \ldots, e_{r}\right]^{-}$is complementary to $\left[d_{2}, \ldots, d_{t}\right]^{-}$.}
\end{figure}

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/2cbcc31b-ba59-4f5d-b0e3-4b51a86cb997-28.jpg?height=344&width=1341&top_left_y=304&top_left_x=354}
\captionsetup{labelformat=empty}
\caption{Figure 25: A positive definite plumbing graph of $S_{n}^{3}(T(p, \alpha))$, where $\alpha>p$ and $-1<N<0$. Here $\left[d_{1}, \ldots, d_{t}\right]^{-}=\alpha / p$ and $\left[e_{1}, \ldots, e_{r}\right]^{-}$is complementary to $\left[d_{2}, \ldots, d_{t}\right]^{-}$.}
\end{figure}

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/2cbcc31b-ba59-4f5d-b0e3-4b51a86cb997-28.jpg?height=344&width=1389&top_left_y=879&top_left_x=328}
\captionsetup{labelformat=empty}
\caption{Figure 26: A positive definite plumbing graph of $S_{n}^{3}(T(p, \alpha))$, where $\alpha>p$ and $N<$ -1. Here $\left[d_{1}, \ldots, d_{t}\right]^{-}=\alpha / p$ and $\left[e_{1}, \ldots, e_{r}\right]^{-}$is complementary to $\left[d_{2}, \ldots, d_{t}\right]^{-}$, and the tail starts with a chain of -2's of length $-N_{1}-1$.}
\end{figure}
node. Removing the node splits the graph into 3 connected components, of which the top left one is called the torso, the bottom left one is called the leg and the right one is called the tail. This vocabulary is chosen to accord with the vocabulary of [19] on iterated torus knots. We also often talk about the torso, leg and tail collectively as legs. This comes from viewing the graphs as general star-shaped graphs rather than graphs of surgeries on torus knots specifically. (The author recommends looking at a flag of Sicily or Isle of Man for a more precise metaphor.) This vocabulary is generally used by Lecuona, for instance in [15] and [16].

We say that two legs of a star-shaped graph are negatively quasi-complementary if either adding one vertex at the end of one leg could make them complementary, and positively quasi-complementary if removing a final vertex from one of the legs could. We say that two legs are complementary if they are either positively or negatively quasi-complementary. Note that the graphs in Figures 22, 23, 25 and 26 are exactly the star-shaped graphs with three legs whereof two are quasi-complementary. In the following subsections, we are thus going to look for star-shaped graphs with a pair of quasi-complementary legs among the graphs in Figures 3, 2 and 1. The following very easy-to-check proposition will come in useful:

Proposition 23. Suppose $Q / P=\left[a_{1}, \ldots, a_{n}\right]^{-}$and $\left(-a_{1},-a_{2}, \ldots,-a_{n}\right)$ is either the leg or torso of the plumbing graph of $S_{r}^{3}(T(p, \alpha))$, a positive rational surgery on a positive torus knot. (Here - $a_{n}$ is the weight of the vertex adjacent to the node.) Then $\alpha / p$ is one of the following:
\begin{itemize}
\item[-] $\frac{Q}{P}$,
\end{itemize}

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/2cbcc31b-ba59-4f5d-b0e3-4b51a86cb997-29.jpg?height=659&width=1037&top_left_y=294&top_left_x=514}
\captionsetup{labelformat=empty}
\caption{Figure 27: It is impossible to choose $k$ so that the length or height difference between the full Riemenshneider diagram and the diagram to the right of the red line is one.}
\end{figure}
\begin{itemize}
\item[-] $\frac{Q}{Q-P}$,
\item[-] $\frac{(l+1) Q+P}{Q}$ for some $l \geq 0$ or
\item[-] $\frac{(l+2) Q-P}{Q}$ for some $l \geq 0$.
\end{itemize}

Note that if $\operatorname{GCD}(P, Q)=1$, then all of these fractions are reduced. However, if $P=Q-1$, then, $\alpha / p=\frac{Q}{Q-P}=Q$ is a degenerate case that we ignore.

\section*{4.2 (-3, -2, -2, -3)}

In this subsection, we prove the following:
Proposition 24. For all torus knots $T(p, q)$ in Families 1, 2, 3, 4, 6 and 7 of Theorem B, there exists an $r \in \mathbb{Q}_{+}$such that $S_{r}^{3}(T(p, q))$ bounds a rational homology ball.

This is done by considering the intersections between the graphs in Figures 22, 23, 25 and 26 (rational surgeries on torus knots) and the graphs in Figure 2 (graphs obtainable from ( $-3,-2,-2,-3$ ) through GOCL moves). Figure 2 is symmetric in the $y$-axis, so it is enough to try two of the vertices for trivalency, say the one with weight $1-\beta_{1}-\zeta_{1}$ and the one with weight $-a_{1}$.

If we want to the vertex with weight $1-\beta_{1}-\zeta_{1}$ to be the trivalent vertex in one of the Figures 22, 23, 25 and 26 , then $l_{1}=m_{1}=1$. Hence $\beta_{i}=\alpha_{j}=2$ for all $i$ and $j$. Also, $l_{2}=1$ or $n_{1}=1$. Suppose that $\left(-\beta_{m_{2}}, \ldots,-\beta_{2}\right)$ is one of the quasi-complementary legs. Proposition 23 would generate that $(p, q)$ belongs to Families 1 and 2 in Theorem B. All of these are possible to produce by setting $l_{2}=1$, which frees us up to choosing $\left(\zeta_{2}, \cdots, \zeta_{n_{2}}\right)$ completely freely.

Now, we consider what happens if the legs other than $\left(-\beta_{2}, \ldots,-b_{m_{2}}\right)$ are quasi-complementary. If $n_{1}=1$, all $\alpha \mathrm{s}, \beta \mathrm{s}$ and $\zeta \mathrm{s}$ become -2, giving us a star-shaped
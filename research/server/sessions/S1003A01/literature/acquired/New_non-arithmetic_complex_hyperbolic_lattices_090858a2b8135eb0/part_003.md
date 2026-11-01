---
retention_scope: session
part: 3
total_parts: 4
---

[Part 3/4 of: New non-arithmetic complex hyperbolic lattices]

To be specific, we give an explicit such sequence for $V^{r}$ that works for all values of $p$ :
$$P^{-3} r_{1}, P^{2} r_{1}^{-}, P^{3} r_{1}, P r_{1}^{-}, P^{2} r_{1}, r_{1}^{-}, P r_{1} .$$
At each stage, we check that $C_{n-1} \cap F_{n}$ is indeed a disk by using the description of the combinatorics given in Figures 6 to 8 (and obvious variations, obtained by applying the suitable power of $P$ and/or the symmetry $\iota$ ).

The corresponding sequence for $U^{r}$ is easily deduced from the one for $V^{r}$ by applying the antiholomorphic involution $\iota$. This finishes the proof of Lemma 4.21, hence also the proof of Lemma 4.19. \(\square\)

We now consider the case $p \geqslant 8$. What remains true from the statement of Lemma 4.19 is the following:

Lemma 4.22 For $p=8$ and 12, $T^{r} \cup T^{s}$ is homeomorphic to $S^{3}$.
However, $T^{r}$ and $T^{s}$ are now singular handlebodies, with complementary singularities as we now explain.

A lot of the description of $T^{r}$ and $T^{s}$ for $p \leqslant 6$ goes through. In particular, we use the same definition for $D_{1}^{r}, D_{2}^{r}, D_{1}^{s}, D_{2}^{s}$, see equation (23), and for $U^{r}, V^{r}, U^{s}, V^{s}$, see equation (24). The picture in Figure 11 makes it clear that $U^{r}$ and $V^{r}$ are cylinders, whereas $U^{s}$ and $V^{s}$ are both singular. We state this more precisely in Lemmas 4.23 and 4.24.

Lemma 4.23 Let $p=8$ or 12. Then $D_{1}^{r}$ and $D_{2}^{r}$ are disjoint embedded closed disks, $U^{r}$ and $V^{r}$ are both homeomorphic to 3-balls. The intersection $U^{r} \cap V^{r}$ is given by the disjoint union of $D_{1}^{r}, D_{2}^{r}$ and seven isolated points. The interior of $T^{r}$ is an open solid torus.

The seven isolated points are given by $q_{123 \overline{2}}^{23 \overline{2}}$ (which is the single intersection point of the 3-cells $r_{1}$ and $P^{2} r_{1}^{-}$), and the six other points in its $P$-orbit. These are indicated by square vertices in Figure 11. As mentioned earlier, we refer to these as pinch points.

The corresponding result for $T^{s}$ is the following. By a bowtie, we mean the result of gluing two triangles along a single vertex, which we call the apex of the bowtie.

Lemma 4.24 Let $p=8$ or 12. Then $D_{1}^{s}, D_{2}^{s}$ are disjoint bowties, with apex at a pinch point. $U^{s}$ contains 3 pinch points, $V^{s}$ contains 4 pinch points, and the interior of $T^{s}$ is an open handlebody of genus 8.

We now analyze the local structure around any of the seven pinch points, say $q_{123 \overline{2}}^{23 \overline{2}}$. It lies on precisely six 3-cells of $\widehat{E}_{3}$ (see Figure 8), namely $r_{1}, P^{2} r_{1}^{-}, s_{1}, P^{2} s_{1}, s_{1}^{-}$and $P^{2} s_{1}^{-}$, and appears as the intersection of two different pairs of hexagons on the boundary torus,
$$r_{1} \cap s_{1}, r_{1} \cap P^{2} s_{1}$$
on the one hand, and
$$P^{2} r_{1}^{-} \cap s_{1}^{-}, P^{2} r_{1}^{-} \cap P^{2} s_{1},$$
see Figure 11.
The link of that vertex is shown in Figure 13. Note that it is homeomorphic to a sphere, so even though both pieces $T^{r}$ and $T^{s}$ are singular, the union $T^{r} \cup T^{s}$ is a 3-manifold.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/31f0f35c-0604-47ef-a2ef-a49ed021037c-43.jpg?height=312&width=414&top_left_y=668&top_left_x=839}
\captionsetup{labelformat=empty}
\caption{Figure 13: Link of $q_{123 \overline{2}}^{23 \overline{2}}$, for $p=8$ or 12.}
\end{figure}

We construct a non-singular solid torus $\widetilde{T}^{r}$ (resp. $\widetilde{T}^{s}$ ) from $T^{r}$ (resp. $T^{s}$ ) by performing an obvious surgery in a small ball near each pinch point, using the picture of the link given in Figure 13 as a guide.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/31f0f35c-0604-47ef-a2ef-a49ed021037c-43.jpg?height=320&width=930&top_left_y=1286&top_left_x=581}
\captionsetup{labelformat=empty}
\caption{Figure 14: We draw vertical sections of a rotationally symmetric local model (think of $T^{r}$ near the pinch point as a circular cone). After surgery near the pinch points, the white bowties become disks.}
\end{figure}

After surgery, the two bowties (shown in white in Figure 14) become disjoint disks, $\widetilde{D}_{1}^{s}$ and $\widetilde{D}_{2}^{s}$, which exhibits $\widetilde{T}^{s}$ as a solid torus (union of two cylinders). The disk $D_{1}^{r}$ is unaffected by the surgery, and it clearly intersects $\widetilde{D}_{1}^{s}$ in a single point, since the intersection point of the bold lines in Figure 11 occurs away from the pinch points. \(\square\)

\subsection*{4.8 Geometric realization}

\subsection*{4.8.1 Realization of the vertices of $\widehat{E}$}

In this section, we describe in detail the 0-skeleton of $\widehat{E}$, depending on the parameter $p$. We describe the geometric realization $\phi$ on the level of the 0-skeleton, check the consistency of this realization with the labels in Figures 6 through 8, as well as the embeddedness of the realization (see Section 4.6.2 for the explanation of this terminology).

Consistency is checked by finding the complete list of bounding bisectors (see Section 4) that contain the realization of each vertex. This will be done case by case in Propositions 4.26, 4.28 and 4.30. Checking embeddedness then requires no further verifications,
since the vertices turn out to be uniquely determined by the set of bounding bisectors that contain them. The correct side condition for vertices amounts to proving a small number of strict inequalities, which is easily done with a computer (the point is that the relevant vertices and bisectors are $k$-rational, where $k=\mathbb{Q}(a, \tau)$, see the discussion in Section 2.7).

As mentioned in Section 4.6.2, the realization of the vertices of $\widehat{E}$ is determined by Figures 6 through 8, where vertices are described as fixed point sets of the isometry given in word notation by their labels (see Section 4.2). The figures only list the vertices of $r_{1}$ and $s_{1}$, but the other ones are obtained from those by applying $\iota$ and/or a power of $P$. For completeness, we list the $P$-orbits of these vertices, depending on the value of $p$. There are two types of vertices, which we call $p_{*}$-vertices and $q_{*}$-vertices (see Section 4.2).
Case $p=3$ or 4: In this case there are two $P$-orbits of vertices, so that $\widehat{E}$ has 14 vertices. There is one $P$-orbit of $p_{*}$-vertices and one $P$-orbit of $q_{*}$-vertices.
\begin{itemize}
\item[1.] The realization of the vertex $p_{w}$ is the unique fixed point in $\overline{\mathbf{H}}_{\mathbb{C}}^{2}$ of the element of $\Gamma$ represented by the word $w$. The seven $p_{*}$-vertices are realized by ideal vertices when $p=4$.
\item[2.] The realization of the vertex $q_{w}$ is the unique fixed point in $\mathbf{H}_{\mathbb{C}}^{2}$ of the map $w \in \Gamma$.
\end{itemize}
A representative of the $P$-orbit of $p_{*}$-vertices is $p_{12}$, realized as the unique fixed point of $R_{1} R_{2}$. A representative of the $q_{*}$-vertices is $q_{123 \overline{2}}$, realized by the unique fixed point of $R_{1} R_{2} R_{3} R_{2}^{-1}$. The $P$-orbits are easy to compute from the fact that $P=R_{1} J$ (and $P^{7}=\mathrm{Id}$ ), for instance
$$\begin{aligned}
P 1 \bar{P} & =1 J 1 \bar{J} \overline{1}=12 \overline{1}, \\
P 23 \overline{2} \bar{P} & =1 J 23 \overline{2} \bar{J} \overline{1}=131 \overline{3} \overline{1}=\overline{3} 13,
\end{aligned}$$
where the last equality follows from the higher braid relation $(31)^{2}=(13)^{2}$. These two equalities give $P q_{123 \overline{2}}=q_{12 \overline{1} \overline{3} 13}$. The vertices are given in Tables 16 and 18 in the appendix (Section 7). From the preceding discussion, we obtain a realization of the 0-skeleton of $\widehat{E}$ into $\overline{\mathbf{H}}_{\mathbb{C}}^{2}$, i.e. a definition of $\phi$ on the level of the 0-skeleton; we now check the consistency of this embedding with the labels of Figures 6 to 8.

First, let us show that $\phi$ sends the vertices of $r_{1}$ and $s_{1}$ to points in the bisectors $\mathscr{R}_{1}$ and $\mathscr{S}_{1}$ respectively.

Lemma 4.25 1. The bisector $\mathscr{R}_{1}$ contains $p_{12}, p_{13}, p_{23}, q_{123 \overline{2}}$ and $q_{1 \overline{3} 23}$.
\begin{itemize}
\item[2.] The bisector $\mathscr{S}_{1}$ contains $p_{23}, p_{\overline{3} \overline{2} 3123}, q_{123 \overline{2}}$ and $q_{1 \overline{3} 23}$.
\end{itemize}

Proof. By construction, $\mathbf{n}_{23}$ lies on the real spine of $\mathscr{R}_{1}$. This vector projects to $p_{23}$, the unique fixed point in $\overline{\mathbf{H}}_{\mathbb{C}}^{2}$ of 23. Likewise, the complex line $m_{1}$ fixed by $R_{1}$ is a slice of $\mathscr{R}_{1}$. The fixed points of 12, 13, $123 \overline{2}$ and $1 \overline{3} 23$ all lie on $m_{1}$ and so are contained in $\mathscr{R}_{1}$ (see notation from section 4.3). This proves part (1). For part (2), begin by observing that the braid relation (see Proposition 4.5) implies $\overline{3} \overline{2} 3123=1 \overline{3} 23 \overline{1} 23 \overline{2}$ and so its fixed point lies on $m_{23 \overline{2}}$ and $m_{1 \overline{3} 23 \overline{1}}$. The rest of the proof follows as in part (1). \(\square\)

To finish the consistency verification, we list the bounding bisectors containing $p_{12}$ and $q_{123 \overline{2}}$ (the list of bisectors containing any vertex is then obtained by applying suitable powers of $P$ ).

Proposition 4.26 Let $p=3$ or 4. Then among the 28 bounding bisectors:
\begin{itemize}
\item[1.] The vertex $p_{12}$ is on $\mathscr{R}_{1}, \mathscr{R}_{1}^{-}, P \mathscr{R}_{1}, P^{-1} \mathscr{R}_{1}^{-}, P^{2} \mathscr{R}_{1}, P^{2} \mathscr{S}_{1}, P^{-3} \mathscr{S}_{1}, P^{-3} \mathscr{S}_{1}^{-}, P \mathscr{R}_{1}^{-}$, $P^{-1} \mathscr{S}_{1}^{-}$;
\item[2.] The vertex $q_{123 \overline{2}}$ is on $\mathscr{R}_{1}, \mathscr{R}_{1}^{-}, \mathscr{S}_{1}, \mathscr{S}_{1}^{-}, P^{2} \mathscr{R}_{1}, P^{2} \mathscr{R}_{1}^{-}, P^{2} \mathscr{S}_{1}, P^{2} \mathscr{S}_{1}^{-}$.
\end{itemize}
Proof. This follows from Lemma 4.25 and Tables 16, 18 in Section 7 (see also the action of $\iota$ on the vertices described in Section 4.6.1). We only treat a couple of cases. For instance, $p_{12} \in P^{-1} \mathscr{R}_{1}^{-}$is equivalent to $P p_{12}=p_{123 \overline{1}} \in \mathscr{R}_{1}^{-}$. Applying $\iota$, this is equivalent to $p_{23} \in \mathscr{R}_{1}$, which was proved in Lemma 4.25.

The fact that $p_{12}$ is on $P^{-3} \mathscr{S}_{1}^{-}$translates into $P^{3} p_{12}=p_{\overline{3} \overline{2} 3123} \in \mathscr{S}_{1}^{-}$, or equivalently by applying $\iota, P^{-3} p_{13} \in \mathscr{S}_{1}$. Since $P p_{13}=p_{12}$ and $P^{7}=i d$, we have $P^{-3} p_{13}=P^{3} p_{12}$. \(\square\)

Case $p=5$ or 6: For $p \geqslant 5$ the word $\left(R_{1} R_{2}\right)^{2}$ is a complex reflection fixing the complex line $m_{12}$. In that case, we replace the vertex $p_{12}$ with four vertices $p_{12}^{1}, p_{12}^{2}, p_{12}^{\overline{2} 12}$ and $p_{12}^{12 \overline{1}}$, that are given by the intersections of $m_{12}$ with $m_{1}, m_{2}, m_{\overline{2} 12}$, and $m_{12 \overline{1}}$ respectively. The $q_{*}$-vertices are unchanged. Thus, there are five $P$-orbits of vertices, so that $\widehat{E}$ has 35 vertices.
\begin{itemize}
\item[1.] The realization of the vertex $p_{w}^{v}$ is the intersection of the complex lines $m_{v}$ and $m_{w}$, fixed by $v$ and $w^{2}$ respectively.
\item[2.] The realization of the vertex $q_{w}$ is the unique fixed point of $w$. The seven $q_{*}$ vertices map to ideal points when $p=6$.
\end{itemize}
The cycles of $q_{*}$-vertices are the same as for $p=3,4$ (see the second row of Table 18). The four orbits of $p_{*}$-vertices are listed in Table 17.

Lemma 4.27 1. The bisector $\mathscr{R}_{1}$ contains the vertices $p_{12}^{2}, p_{12}^{1}, p_{13}^{1}, p_{13}^{3}, p_{23}^{3}, p_{23}^{2}, p_{23}^{23 \overline{2}}$, $p_{23}^{\overline{3} 23}, q_{123 \overline{2}}$ and $q_{1 \overline{3} 23}$.
\begin{itemize}
\item[2.] The bisector $\mathscr{S}_{1}$ contains the vertices $p_{23}^{\overline{3} 23}, p_{23}^{23 \overline{2}}, p_{\overline{3} \overline{2} 3123}^{23 \overline{2}}, p_{\overline{2} 33123}^{\underline{1} 323 \overline{1}}, q_{123 \overline{2}}$ and $q_{1 \overline{3} 23}$.
\end{itemize}

Proof. For $\mathscr{R}_{1}$, the statement is obvious for eight of the ten vertices, since vertices of the form $p_{*}^{1}$ and $p_{23}^{*}$ lie on $m_{1}$ and $m_{23}$ respectively, and these are complex slices of $\mathscr{R}_{1}$. The last two are handled using Lemma 2.3. We treat the case of $p_{12}^{2}$ in detail, $p_{13}^{3}$ is entirely similar.

Note that $m_{12}$ is orthogonal to $m_{1}$, since $R_{1}$ and $\left(R_{1} R_{2}\right)^{2}$ commute. Similary, $m_{2}$ is orthogonal to $m_{23}$. Lemma 2.3 implies that $\mathscr{R}_{1}$ intersects each of the complex lines $m_{2}$ and $m_{12}$ in a real geodesic, and by definition $p_{12}^{2}$ is the intersection point of these two geodesics. This proves part (1). Part (2) is proved similarly. \(\square\)

The analogue of Proposition 4.26 is the following:
Proposition 4.28 Let $p=5$ or 6. Then among the 28 bounding bisectors:
\begin{itemize}
\item[1.] the vertex $p_{12}^{1}$ is on $\mathscr{R}_{1}, \mathscr{R}_{1}^{-}, P \mathscr{R}_{1}, P^{2} \mathscr{R}_{1}, P^{2} \mathscr{S}_{1}, P^{-1} \mathscr{R}_{1}^{-}$;
\item[2.] the vertex $p_{12}^{2}$ is on $\mathscr{R}_{1}, P^{2} \mathscr{R}_{1}, P^{2} \mathscr{S}_{1}, P^{-3} \mathscr{S}_{1}, P^{-3} \mathscr{S}_{1}^{-}, P^{-1} \mathscr{R}_{1}^{-}$;
\item[3.] the vertex $p_{23}^{2}$ is on $\mathscr{R}_{1}, P^{2} \mathscr{S}_{1}, P^{2} \mathscr{S}_{1}^{-}, P^{-3} \mathscr{R}_{1}^{-}, P^{-3} \mathscr{S}_{1}^{-}, P^{-1} \mathscr{R}_{1}^{-}$;
\end{itemize}
\begin{itemize}
\item[4.] the vertex $p_{23}^{3}$ is on $\mathscr{R}_{1}, P^{-3} \mathscr{R}_{1}^{-}, P^{-3} \mathscr{S}_{1}^{-}, P^{-2} \mathscr{R}_{1}^{-}, P^{-1} \mathscr{R}_{1}, P^{-1} \mathscr{R}_{1}^{-}$;
\item[5.] the vertex $q_{123 \overline{2}}$ is on $\mathscr{R}_{1}, \mathscr{R}_{1}^{-}, \mathscr{S}_{1}, \mathscr{S}_{1}^{-}, P^{2} \mathscr{R}_{1}, P^{2} \mathscr{R}_{1}^{-}, P^{2} \mathscr{S}_{1}$ and $P^{2} \mathscr{S}_{1}^{-}$.
\end{itemize}

Case $p=8$ or 12: In this case there are seven $P$-orbits of vertices (so that $\widehat{E}$ has 49 vertices). The cycles of $p_{*}$-vertices are the same as for $p=5,6$ (there are four of them, see Table 17), and there are three orbits of $q_{*}$-vertices, listed in Table 19. Since $\left(R_{1} R_{2} R_{3} R_{2}^{-1}\right)^{3}$ is a complex reflection fixing the complex line $m_{123 \overline{2}}$, we replace the vertex $q_{123 \overline{2}}$ with three vertices lying in this complex line.
\begin{itemize}
\item[1.] The realization of the vertex $p_{w}^{v}$ is the intersection of the complex lines $m_{v}$ and $m_{w}$, fixed by $v$ and $w^{2}$ respectively.
\item[2.] The realization of the vertex $q_{w}^{v}$ is the intersection of the complex lines $m_{v}$ and $m_{w}$, fixed by $v$ and $w^{3}$ respectively.
\end{itemize}

The following lemma is proved as before.
Lemma 4.29 1. The bisector $\mathscr{R}_{1}$ contains the vertices $p_{12}^{2}, p_{12}^{1}, p_{13}^{1}, p_{13}^{3}, p_{23}^{3}, p_{23}^{2}, p_{23}^{23 \overline{2}}$, $p_{23}^{\overline{3} 23}, q_{123 \overline{2}}^{23 \overline{2}}, q_{123 \overline{2}}^{1}, q_{\overline{3} 23}^{\underline{1}}$ and $q_{1 \overline{3} 23}^{\overline{3} 23}$.
\begin{itemize}
\item[2.] The bisector $\mathscr{S}_{1}$ contains the vertices $p_{23}^{\overline{3} 23}, p_{23}^{23 \overline{2}}, p_{\overline{3} \overline{2} 3123}^{23 \overline{2}}, p_{\overline{3} 23123}^{\underline{1} 323 \overline{1}}, q_{123 \overline{2}}^{23 \overline{2}}, q_{123 \overline{2}}^{1}, q_{1 \overline{3} 23}^{1}, q_{1 \overline{3} 23}^{\overline{3} 23}$ and $q_{1 \overline{3} 23}^{1 \overline{3} 23 \overline{1}}$.
\end{itemize}

Proposition 4.30 Let $p=8$ or 12. The $p_{*}$-vertices are on the same bounding bisectors as in the case $p=5,6$, and the $q_{*}$-vertices are on the following bounding bisectors:
\begin{itemize}
\item[1.] the vertex $q_{1 \overline{3} 23}^{1}$ is on $\mathscr{R}_{1}, \mathscr{R}_{1}^{-}, \mathscr{S}_{1}, \mathscr{S}_{1}^{-}, P^{-2} \mathscr{R}_{1}^{-}$and $P^{-2} \mathscr{S}_{1}^{-}$;
\item[2.] the vertex $q_{1323}^{\overline{3} 23}$ is on $\mathscr{R}_{1}, \mathscr{S}_{1}, P^{-2} \mathscr{R}_{1}, P^{-2} \mathscr{R}_{1}^{-}, P^{-2} \mathscr{S}_{1}$ and $P^{-2} \mathscr{S}_{1}^{-}$;
\item[3.] the vertex $q_{123 \overline{2}}^{23 \overline{2}}$ is on $\mathscr{R}_{1}, \mathscr{S}_{1}, \mathscr{S}_{1}^{-}, P^{2} \mathscr{R}_{1}^{-}, P^{2} \mathscr{S}_{1}$ and $P^{2} \mathscr{S}_{1}^{-}$.
\end{itemize}

\subsection*{4.8.2 Realizing edges of $\widehat{E}$}

In this section, we check the consistency and the embeddedness condition for the realization of the 1-skeleton. Each 1-cell is realized as a geodesic segment joining the realization of its two endpoints. According to the description of $\widehat{E}$, each 1 -cell is on four 3 -cells, so we need to check that the geodesic segment realizing each 1-cell is contained in the appropriate set of four bisectors (the set of bisectors is indicated by the labels of Figures 6 to 8). Recall from Section 2.4 that in order to check that a geodesic segment $\left[v_{0}, v_{1}\right]$ is on a bisector $\mathscr{B}$, it is not enough to check that its endpoints $v_{0}$ and $v_{1}$ are on $\mathscr{B}$.

Proposition 4.31 The realization of the 1-skeleton of $\widehat{E}$ is consistent.
Proof. This follows from repeated use of Lemmas 2.2 or 2.3. We illustrate this in a couple of specific cases. First, suppose $p=3$ or 4, and consider the geodesic through $p_{12}$ and $p_{13}$. According to Proposition 4.26, it should be contained in
$$\mathscr{R}_{1}, \quad \mathscr{R}_{1}^{-}, \quad P \mathscr{R}_{1}, \quad P^{-1} \mathscr{R}_{1}^{-} .$$

By definition of the points $p_{12}$ and $p_{13}$, they are both in the mirror of $R_{1}$, which is a common complex slice of $\mathscr{R}_{1}$ and $\mathscr{R}_{1}^{-}$. Moreover, $p_{13}$ (resp. $p_{12}$ ) is on the real spine of $P \mathscr{R}_{1}$ (resp. $P^{-1} \mathscr{R}_{1}^{-}$), so the geodesic is contained in $P \mathscr{R}_{1}$ (resp. $P^{-1} \mathscr{R}_{1}^{-}$).

Now suppose $p \geqslant 5$, and consider the geodesic $\alpha$ through $p_{13}^{1}$ and $p_{12}^{1}$. These two points are on $m_{1}$, which is a common slice of $\mathscr{R}_{1}$ and $\mathscr{R}_{1}^{-}$. Moreover, $m_{1}$ is by construction orthogonal to the complex line $m_{12}$, which is a complex slice of $P^{-1} \mathscr{R}_{1}^{-}$, so Lemma 2.3 implies that $\alpha$ is contained in $P^{-1} \mathscr{R}_{1}^{-}$. Similarly, $m_{1}$ is orthogonal to the slice of $P \mathscr{R}_{1}$ given by $\mathbf{n}_{13}^{\perp}$, so $\alpha$ is contained in $P \mathscr{R}_{1}$.

In some cases, one needs to use both Lemmas 2.2 and 2.3. For instance, for $p=5$ or 6, $p_{12}^{1}$ and $q_{123 \overline{2}}$ are contained in $m_{1}$, so clearly the geodesic joining them is in $\mathscr{R}_{1}$ and $\mathscr{R}_{1}^{-}$. The fact that it is contained in $P^{2} \mathscr{R}_{1}$ follows from Lemma 2.3 (and the fact that $\left\langle\mathbf{n}_{1}, \mathbf{n}_{12}\right\rangle=0$ ), whereas the fact that it is contained in $P^{2} \mathscr{S}_{1}$ follows from Lemma 2.2 (and the fact that $q_{123 \overline{2}}$ is on the real spine of $P^{2} \mathscr{S}_{1}$ ).

In some cases, the application of Lemma 2.3 is not completely obvious, since the orthog-onality check can be a bit more involved. For instance, consider the geodesic through $p \frac{1}{323123}$ and $q_{1 \overline{3} 23}$. Clearly these two points are on $m_{1 \overline{3} 23 \overline{1}}$, so the geodesic is contained in $\mathscr{S}_{1}^{-}$and $P^{-2} \mathscr{S}_{1}$. It is contained in $\mathscr{S}_{1}$ simply because $q_{1 \overline{3} 23}$ is a point of its real spine, but in order to check that it is contained in $P^{-2} \mathscr{R}_{1}$, one needs to check that $\left\langle\mathbf{n}_{1 \overline{3} 23 \overline{1}}, \mathbf{n}_{\overline{3} \overline{2} 3123}\right\rangle=0$. Since $\mathbf{n}_{1 \overline{3} 23 \overline{1}}=P^{3} \mathbf{n}_{2}$ and $\mathbf{n}_{\overline{3} \overline{2} 3123}=P^{3} \mathbf{n}_{12}$ the result follows from $\left\langle\mathbf{n}_{2}, \mathbf{n}_{12}\right\rangle=0$. \(\square\)

Remark 4.32 Lemma 2.3 shows a bit more than the relevant inclusions of geodesics in bisectors. It also implies that the geodesic is in a real slice of certain bisectors - when two adjacent edges are contained in real slices of the same bisector (and their intersection is not on the real spine of that bisector), the two real slices must actually coincide.

Proposition 4.33 The realization of the 1-skeleton of $\widehat{E}$ is embedded and contained in $F$.
Proof. Let $f$ be a 1-cell of $\widehat{E}$. We have just proved that its realization $\phi(f)$ is on (at least) four bounding bisectors. For each other bounding bisector $\mathscr{B}$, we check that $\phi(f)$ is on the correct half-space bounded by $\mathscr{B}$. Since the endpoints of $\phi(f)$ are $k$-rational (with $k=\mathbb{Q}(a, \tau))$, this can be done using arithmetic in $k$, see Section 2.7.

Note that the situation where some 1-cells are tangent to some of the bounding bisectors, alluded to in Section 2.7, really does occur. Specifically, it occurs when an endpoint of the 1-face is a cusp, which happens at certain specific vertices when $p=4$ and $p=6$.

Note that because of the symmetry given by $P$ and $\iota$, it is enough to study the tangencies that appear in (the intersection of $\phi(\widehat{E})$ with)
$$\mathscr{R}_{1} \cap \mathscr{R}_{1}^{-}, \mathscr{R}_{1} \cap \mathscr{S}_{1}, \mathscr{R}_{1} \cap P^{-3} \mathscr{R}_{1}^{-}, \mathscr{R}_{1} \cap P^{-2} \mathscr{R}_{1}^{-}, \mathscr{R}_{1} \cap P^{-1} \cap \mathscr{R}_{1}^{-}, \mathscr{S}_{1} \cap P^{2} \mathscr{S}_{1}^{-}, \mathscr{S}_{1} \cap P^{-2} \mathscr{S}_{1}^{-} .$$
Although not technically needed for the proof, it can be instructive to draw figures of these Giraud disks and their intersection with all bounding bisectors. This is done in Figure 16 for $\mathscr{R}_{1} \cap \mathscr{L}_{1}$, where it should be apparent that tangencies only occur for $p=4$ and $p=6$ (see parts (b) and (d) of the figure). In order for the figure to be read properly, notice that the labels on curves in the graph correspond to the index of the bisectors given in Table 2.

We treat these two tangencies in Proposition 4.34. The other ones are similar.

\begin{table}
\begin{tabular}[t]{|l|l|l|l|l|}
\hline Bisector & $P^{k} \mathscr{R}_{1}$ & $P^{k} \mathscr{R}_{1}^{-}$ & $P^{k} \mathscr{S}_{1}$ & $P^{k} \mathscr{S}_{1}^{-}$ \\
\hline Index notation & $\mathscr{B}_{1+4 k}$ & $\mathscr{B}_{2+4 k}$ & $\mathscr{B}_{3+4 k}$ & $\mathscr{B}_{4+4 k}$ \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 2: Numbering of the bounding bisectors according to $P$-symmetry, for $k=0, \ldots, 6$.}
\end{table}

Proposition 4.34 1. For $p=4$, the real geodesic through $p_{23}$ and $q_{1 \overline{3} 23}$ intersects $P^{-1} \mathscr{R}_{1}$ only at the ideal vertex $p_{23}$.
\begin{itemize}
\item[2.] For $p=6$, the real geodesic through $p_{23}^{23 \overline{2}}$ and $q_{123 \overline{2}}$ intersects $P^{2} \mathscr{R}_{1}^{-}$only at the ideal vertex $q_{123 \overline{2}}$.
\item[3.] For $p=6$, the real geodesic through $p_{23}^{\overline{3} 23}$ and $q_{1 \overline{3} 23}$ intersects $P^{-2} \mathscr{S}_{1}$ only at the ideal vertex $q_{1 \overline{3} 23}$.
\item[4.] For $p=6$, the real geodesic through $q_{123 \overline{2}}$ and $q_{1 \overline{3} 23}$ intersects $P^{2} \mathscr{R}_{1}$ only at the ideal vertex $q_{123 \overline{2}}$.
\end{itemize}
Proof. First let $p=4$. The geodesic arc from $p_{23}$ to $q_{1 \overline{3} 23}$ is a side of $r_{1} \cap s_{1}$. We check that it only intersects $P^{-1} \mathscr{R}_{1}$ at $p_{23}$. Apart from $q_{1 \overline{3} 33}$, the extended real geodesic is parametrized by vectors of the form $\mathbf{a}+t \mathbf{b}$ with
$$\mathbf{a}=\mathbf{n}_{23}, \quad \mathbf{b}=\left\langle\mathbf{n}_{23}, \mathbf{n}_{1 \overline{3} 23}\right\rangle \mathbf{n}_{1 \overline{3} 23},$$
and $t \in \mathbb{R}$ (there are further restrictions on $t$, but this will be irrelevant in what follows). The corresponding point is on $P^{-1} \mathscr{R}_{1}$ (or rather its extension to projective space) if and only if
$$\left|\left\langle\mathbf{a}+t \mathbf{b}, P^{-1} \mathbf{y}_{0}\right\rangle\right|^{2}=\left|\left\langle\mathbf{a}+t \mathbf{b}, P^{-1} R_{1}^{-1} \mathbf{y}_{0}\right\rangle\right|^{2} .$$
Using $\tau=-(1+i \sqrt{7}) / 2$, then $a=e^{2 \pi i / 12}=(\sqrt{3}+i) / 2$, we compute
$$\left|\left\langle\mathbf{a}+t \mathbf{b}, P^{-1} \mathbf{y}_{0}\right\rangle\right|^{2}-\left|\left\langle\mathbf{a}+t \mathbf{b}, P^{-1} R_{1}^{-1} \mathbf{y}_{0}\right\rangle\right|^{2}=-(196156+74140 \sqrt{7}) t^{2},$$
the latter vanishing precisely at $t=0$.
For $p=6$ and $\mathbf{a}=q_{123 \overline{2}}, \mathbf{b}=p_{23}^{23 \overline{2}}$, one gets
$$\left|\left\langle\mathbf{a}+t \mathbf{b}, P^{2} \mathbf{y}_{0}\right\rangle\right|^{2}-\left|\left\langle\mathbf{a}+t \mathbf{b}, P^{2} R_{1} \mathbf{y}_{0}\right\rangle\right|^{2}=-(2525+551 \sqrt{7} \sqrt{3}) t^{2} .$$
For $p=6$ and $\mathbf{a}=q_{123 \overline{2}}, \mathbf{b}=q_{1 \overline{3} 23}$, one gets
$$\left|\left\langle\mathbf{a}+t \mathbf{b}, P^{2} \mathbf{y}_{0}\right\rangle\right|^{2}-\left|\left\langle\mathbf{a}+t \mathbf{b}, P^{2} R_{1}^{-1} \mathbf{y}_{0}\right\rangle\right|^{2}=-(161797+35307 \sqrt{7} \sqrt{3}) t^{2} / 2 .$$
For $p=6$ and $\mathbf{a}=q_{1 \overline{3} 23}, \mathbf{b}=p_{23}^{\overline{3} 23}$, one gets
$$\left|\left\langle\mathbf{a}+t \mathbf{b}, P^{-2} \mathbf{y}_{0}\right\rangle\right|^{2}-\left|\left\langle\mathbf{a}+t \mathbf{b}, P^{-2} S_{1}^{-1} \mathbf{y}_{0}\right\rangle\right|^{2}=-(3524+769 \sqrt{7} \sqrt{3}) t^{2} .$$ \(\square\)

\subsection*{4.8.3 Realizing ridges of $\widehat{E}-$ consistency}

The goal of this section is to show the consistency result for the 2-skeleton of $\widehat{E}$. Recall that we want to realize each 2-face $f$ by using the realization of $\partial f$, which is a piecewise smooth circle (possibly with some ideal vertices) in the intersection of two of the bounding bisectors. We now need to show that the intersection of these two bisectors is a disk. We split the discussion in two cases, depending on the geometry of the intersection (see Section 2.3).
Complex ridges
We first list the ridges of $\widehat{E}$ that get realized in complex lines, calling them simply "complex ridges". The detailed list is given in the appendix (see Table 15).

For $p=3,4$ there are 14 complex lines containing complex ridges, namely the $P$-orbits of $m_{1}$ and $m_{2}$. For $p \geqslant 5$ the point $p_{12}$ is replaced with a ridge in the complex line $m_{12}$ and so there are 21 complex ridges. The $P$-orbits of $m_{12}$ may be found from Table 16 by replacing $p_{w}$ with $m_{w}$ (these are closely related, in fact they are polar to each other). For $p=8,12$ we similarly replace $q_{123 \overline{2}}$ with a ridge in $m_{123 \overline{2}}$, and its $P$-orbit may be read of from the same table by replacing $q_{w}$ with $m_{w}$ in Table 18; this gives a total of 28 complex ridges.

We only analyze the ridges that appear on $r_{1}$ and $s_{1}$, see the bottom and top 2-cells of Figures 6 to 8 (the top 2-cell reduces to a point for small values of $p$ ). We have already shown that, for each such 2-face $f$, the vertices and edges in $\phi(\partial f)$ are contained in a complex line, which is the mirror of a certain complex reflection in the group (see Section 4.8.2). Moreover, the adjacency pictures suggest that we should realize the 2-face in the intersection of two specific bisectors.

The consistency verification amounts to the verification that these two specific bisectors intersect precisely along the complex line mentioned above. We state this in the following.

Proposition 4.35 1. $\mathscr{R}_{1} \cap \mathscr{R}_{1}^{-}$is a complex line, which is $m_{1}$.
\begin{itemize}
\item[2.] For $p \geqslant 5, \mathscr{R}_{1} \cap P^{-3} \mathscr{R}_{1}^{-}$is a complex line, which is $m_{23}$.
\item[3.] $\mathscr{S}_{1} \cap P^{2} \mathscr{S}_{1}^{-}$is a complex line, which is $m_{23 \overline{2}}$.
\item[4.] For $p \geqslant 8, \mathscr{S}_{1} \cap P^{-2} \mathscr{S}_{1}^{-}$is a complex line, which is $m_{1 \overline{3} 23}$.
\end{itemize}
Proof. Parts 1 and 3 are relatively easy, since the corresponding pairs of bisectors are not only cotranchal, they are in fact cospinal. This is obvious for $\mathscr{R}_{1} \cap \mathscr{R}_{1}^{-}$, since the complex spine of $\mathscr{R}_{1}$ is by construction orthogonal to the mirror of $R_{1}$, so $\mathscr{R}_{1}$ and $\mathscr{R}_{1}^{-}=R_{1}\left(\mathscr{R}_{1}\right)$ have the same complex spine.

The case of $\mathscr{S}_{1} \cap P^{2} \mathscr{S}_{1}^{-}$is just a little bit more complicated. By construction $P^{2} S_{1}$ maps $\mathscr{S}_{1}$ to $P^{2} \mathscr{S}_{1}^{-}$, and Proposition 4.4 implies that $P^{2} S_{1}$ is a complex reflection fixing $\mathbf{n}_{23 \overline{2}}$, hence it preserves the complex spine of $\mathscr{S}_{1}$.

For parts 2 and 4, we first prove that the corresponding pair of bisectors is cotranchal, i.e. that the mirror of the relevant complex reflection is indeed contained in the bisector intersection. Then we prove that the intersection really consists only of that common complex slice, by using Proposition 2.7.
Part 2: In this case we need to verify the criterion from Proposition 2.7. That is, we must find the intersection of the real spine $\sigma\left(\mathscr{R}_{1}\right)$ of $\mathscr{R}_{1}$ with $m_{23}$ and lift it to a point $\mathbf{v}_{1}$ so that $\sigma\left(\mathscr{R}_{1}\right)$ is given by real linear combinations of $\mathbf{n}_{23}$ and $\mathbf{v}_{1}$. We know that $\sigma\left(\mathscr{R}_{1}\right)$ is the real
span of $\mathbf{n}_{1}$ and $\mathbf{n}_{23}$ and that $\left\langle\mathbf{n}_{1}, \mathbf{n}_{23}\right\rangle$ is real. Hence we take
$$\mathbf{v}_{1}=\mathbf{n}_{1}-\frac{\left\langle\mathbf{n}_{1}, \mathbf{n}_{23}\right\rangle}{\left\langle\mathbf{n}_{23}, \mathbf{n}_{23}\right\rangle} \mathbf{n}_{23}=\frac{1}{a^{3}+\bar{a}^{3}}\left[\begin{array}{c}
0 \\
-a^{2} \bar{\tau}+\bar{a} \\
-\bar{a}^{2} \tau+a
\end{array}\right] .$$
Now $P^{-3} \mathscr{R}_{1}^{-}=\left(R_{2} R_{3}\right)^{-1} \mathscr{R}_{1}$ and $\bar{a}^{2}\left(R_{2} R_{3}\right)^{-1}$ fixes $\mathbf{n}_{23}$ and so we take
$$\mathbf{v}_{2}=\bar{a}^{2}\left(R_{2} R_{3}\right)^{-1} \mathbf{v}_{1}=\frac{1}{a^{3}+\bar{a}^{3}}\left[\begin{array}{c}
0 \\
\bar{a}^{4} \bar{\tau}+\bar{a} \\
-\bar{a}^{2} \tau-\bar{a}^{5}
\end{array}\right] .$$
Then
$$\begin{aligned}
\left\langle\mathbf{v}_{1}, \mathbf{v}_{1}\right\rangle=\left\langle\mathbf{v}_{2}, \mathbf{v}_{2}\right\rangle= & \left(a^{3}-1\right)\left((1-\tau)-\bar{a}^{3}(1-\bar{\tau})\right) /\left(a^{3}+\bar{a}^{3}\right), \\
\left\langle\mathbf{v}_{2}, \mathbf{v}_{1}\right\rangle= & -\left(a^{3}-1\right)\left((1-\bar{\tau}) \bar{a}^{3}+(1-\tau) \bar{a}^{6}\right) /\left(a^{3}+\bar{a}^{3}\right) .
\end{aligned}$$
Thus
$$\begin{aligned}
& \frac{\left(a^{3}+\bar{a}\right)^{2}}{\left(2-a^{3}-\bar{a}^{3}\right)}\left(4\left\langle\mathbf{v}_{1}, \mathbf{v}_{1}\right\rangle\left\langle\mathbf{v}_{2}, \mathbf{v}_{2}\right\rangle-\left(\left\langle\mathbf{v}_{1}, \mathbf{v}_{2}\right\rangle+\left\langle\mathbf{v}_{2}, \mathbf{v}_{1}\right\rangle\right)^{2}\right) \\
& \quad=\left(a^{3}+\bar{a}^{3}\right)\left(2|1-\tau|^{2}-a^{3}(1-\bar{\tau})^{2}-\bar{a}^{3}(1-\tau)^{2}\right)+2\left(a^{3}-\bar{a}^{3}\right)\left(a^{3}(1-\bar{\tau})^{2}-\bar{a}^{3}(1-\tau)^{2}\right) .
\end{aligned}$$
Both terms are positive for all $p>4$.
Part 4: We argue as in Part 2. The real spine $\sigma\left(\mathscr{S}_{1}\right)$ of $\mathscr{S}_{1}$ is the real span of $a \mathbf{n}_{23 \overline{2}}$ and $\mathbf{n}_{1 \overline{3} 23}$. Its image under $a^{2} 1 \overline{3} 23$ is the real span of $-a \mathbf{n}_{13 \overline{1}}$ and $\mathbf{n}_{1 \overline{3} 23}$. Therefore we construct:
$$\begin{aligned}
& \mathbf{v}_{1}=a \mathbf{n}_{23 \overline{2}}-\frac{\left\langle a \mathbf{n}_{23 \overline{2}}, \mathbf{n}_{1 \overline{3} 23}\right\rangle}{\left\langle\mathbf{n}_{1 \overline{3} 23}, \mathbf{n}_{1 \overline{3} 23}\right\rangle} \mathbf{n}_{1 \overline{3} 23}=\frac{1}{a^{3}+\bar{a}^{3}-1}\left[\begin{array}{c}
-a^{2}-\bar{a} \bar{\tau} \\
a \bar{\tau}+\bar{a}^{2} \tau \\
-1+\tau+2 \bar{a}^{3}
\end{array}\right], \\
& \mathbf{v}_{2}=-a \mathbf{n}_{13 \overline{1}}-\frac{\left\langle-a \mathbf{n}_{13 \overline{1}}, \mathbf{n}_{1 \overline{3} 23}\right\rangle}{\left\langle\mathbf{n}_{1 \overline{3} 23}, \mathbf{n}_{1 \overline{3} 23}\right\rangle} \mathbf{n}_{1 \overline{3} 23}=\frac{1}{a^{3}+\bar{a}^{3}-1}\left[\begin{array}{c}
a^{5} \bar{\tau}+a^{2} \bar{\tau} \\
-a^{4} \tau-a \\
-2 a^{3}-\bar{\tau}
\end{array}\right] .
\end{aligned}$$
We have
$$\begin{aligned}
\left\langle\mathbf{v}_{1}, \mathbf{v}_{1}\right\rangle= & \left\langle\mathbf{v}_{2}, \mathbf{v}_{2}\right\rangle= \\
& \left\langle\mathbf{v}_{2}, \mathbf{v}_{1}\right\rangle=\left(a^{3}-1\right)\left((2-\tau)-\bar{a}^{3}(2-\bar{\tau})\right) /\left(a^{3}+\bar{a}^{3}-1\right),
\end{aligned}$$
Then
$$\begin{aligned}
& \frac{\left(a^{3}+\bar{a}^{3}-1\right)^{2}}{\left(2-a^{3}-\bar{a}^{3}\right)}\left(4\left\langle\mathbf{v}_{1}, \mathbf{v}_{1}\right\rangle\left\langle\mathbf{v}_{2}, \mathbf{v}_{2}\right\rangle-\left(\left\langle\mathbf{v}_{1}, \mathbf{v}_{2}\right\rangle+\left\langle\mathbf{v}_{2}, \mathbf{v}_{1}\right\rangle\right)^{2}\right) \\
& \quad=6|2-\tau|^{2}-\left(4 a^{3}+\bar{a}^{6}\right)(2-\tau)^{2}-\left(4 \bar{a}^{3}+a^{6}\right)(2-\bar{\tau})^{2} .
\end{aligned}$$
This is positive for all $p>6$.
This completes the proof of Proposition 4.35. \(\square\)

\section*{Generic ridges}

\begin{table}
\begin{tabular}[t]{|l|l|l|l|}
\hline Bisector & Equidistant & Bisector & Equidistant \\
\hline $\mathscr{R}_{1}$ & $\mathscr{B}\left(y_{0}, R_{1}^{-1} y_{0}\right)$ & $\mathscr{R}_{1}^{-}$ & $\mathscr{B}\left(y_{0}, R_{1} y_{0}\right)$ \\
\hline $\mathscr{S}_{1}$ & $\mathscr{B}\left(y_{0}, S_{1}^{-1} y_{0}\right)$ & $\mathscr{S}_{1}^{-}$ & $\mathscr{B}\left(y_{0}, S_{1} y_{0}\right)$ \\
\hline $\mathscr{R}_{1}$ & $\mathscr{B}\left(y_{1}, R_{1}^{-1} P y_{1}\right)$ & $P^{-1} \mathscr{R}_{1}^{-}$ & $\mathscr{B}\left(y_{1}, P^{-1} R_{1} y_{1}\right)$ \\
\hline $\mathscr{R}_{1}$ & $\mathscr{B}\left(y_{2}, R_{1}^{-1} P^{2} y_{2}\right)$ & $P^{-2} \mathscr{R}_{1}^{-}$ & $\mathscr{B}\left(y_{2}, P^{-2} R_{1} y_{2}\right)$ \\
\hline $P^{2} \mathscr{S}_{1}$ & $\mathscr{B}\left(y_{2}, P^{2} S_{1}^{-1} P^{-3} y_{2}\right)$ & $P^{3} \mathscr{S}_{1}^{-}$ & $\mathscr{B}\left(y_{2}, P^{3} S_{1} P^{-2} y_{2}\right)$ \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 3: Description of bounding bisectors in terms of $y_{0}, y_{1}$ and $y_{2}$}
\end{table}

In the first part of this section, we checked the consistency of the embedding of complex ridges. We now prove the analogous statement for all the other ridges, which will be realized inside Giraud disks. Recall that given a 2-cell $f$ of $\widehat{E}$, Figures 6 to 8 suggest a pair $\mathscr{B}, \mathscr{B}^{\prime}$ of bounding bisectors that should contain the realization $\phi(f)$. We have already defined the realization on the level of the 1-skeleton, and shown that $\phi(\partial f)$ lies inside $\mathscr{B} \cap \mathscr{B}^{\prime}$ (or possibly its union with finitely many ideal vertices).

The corresponding consistency verification is almost automatic, we simply verify that all the corresponding intersections $\mathscr{B} \cap \mathscr{B}^{\prime}$ are indeed disks, hence $\phi(\partial f)$ bounds a well defined disk, which we use as the realization $\phi(f)$. In order to get these disks, we simply prove that the corresponding pairs of bisectors are coequidistant (see Section 2.3).

Let $\mathbf{y}_{0}, \mathbf{y}_{1}, \mathbf{y}_{2}$ be given by the following formulae:
$$\mathbf{y}_{0}=\left[\begin{array}{c}
-a^{3}\left(\bar{a}^{2} \bar{\tau}+a\right)^{2} \\
\left(a^{2} \bar{\tau}+\bar{a} \tau\right)\left(a^{2} \bar{\tau}-\bar{a}\right) \\
\left(a^{2} \bar{\tau}+\bar{a} \tau\right)\left(\bar{a}^{2} \tau-a\right)
\end{array}\right], \mathbf{y}_{1}=\left[\begin{array}{c}
a\left(1-a^{3} \bar{\tau}\right)^{2} \\
\left(1-a^{3} \bar{\tau}\right)\left(a^{3}-\tau\right) \\
\bar{a}\left(a^{3}-\tau\right)^{2}
\end{array}\right] \mathbf{y}_{2}=\left[\begin{array}{c}
\left(a^{3}-\tau\right)\left(\bar{a}^{3}+\tau\right) \\
\bar{a}\left(1-a^{3} \bar{\tau}\right)\left(1+\bar{a}^{3} \bar{\tau}\right) \\
a\left(1-\bar{a}^{3} \tau\right)\left(1+\bar{a}^{3} \bar{\tau}\right)
\end{array}\right] .$$
Note that $\left\langle\mathbf{y}_{j}, \mathbf{y}_{j}\right\rangle<0$ and so $\mathbf{y}_{j}$ corresponds to a point $y_{j}$ of $\mathbf{H}_{\mathbb{C}}^{2}$. Indeed, the following lemma, which is verified by direct computation, implies that all three points are in $E$.

Lemma 4.36 Let $y_{0}, y_{1}, y_{2}$ be the points in $\mathbf{H}_{\mathbb{C}}^{2}$ corresponding to the vectors given in (26). If $\mathscr{B}$ is any of the 28 bounding bisectors, then the half-space determined by $\mathscr{B}$ that contains the fixed point of $P$ also contains $y_{0}, y_{1}$ and $y_{2}$.

We have already seen in Proposition 4.13 that $\mathscr{R}_{1}, \mathscr{R}_{1}^{-}, \mathscr{S}_{1}$ and $\mathscr{S}_{1}^{-}$are coequidistant from $\mathbf{y}_{0}$. Since $y_{0}$ does not lie on any of their real spines, their pairwise intersections are Giraud disks (apart from $\mathscr{R}_{1} \cap \mathscr{R}_{1}^{-}$, since these two bisectors have the same complex spine). Using the points $y_{1}$ and $y_{2}$ we can describe some of the other intersections between bounding bisectors in a similar way.

Proposition 4.37 Let $y_{0}, y_{1}$ and $y_{2}$ be the points in $\mathbf{H}_{\mathbb{C}}^{2}$ corresponding to the vectors $\mathbf{y}_{0}, \mathbf{y}_{1}$, $\mathbf{y}_{2}$ given in (26). The intersections among bounding bisectors listed in Table 4 are contained in Giraud disks defined by $y_{0}, y_{1}$ and $y_{2}$.

Proof. We must first prove that certain bounding bisectors are coequidistant from $y_{0}, y_{1}$ and $y_{2}$ listed in Table 3. This was proved for $y_{0}$ in Proposition 4.13. We use a similar method to show equidistance from $y_{1}$ and $y_{2}$. Namely, consider two of the bisectors $\mathscr{B}$ and $\mathscr{B}^{\prime}$. We first show that the complex spines of $\mathscr{B}$ and $\mathscr{B}^{\prime}$ intersect in $\mathbf{y}_{j}$, for $j=1$ or 2. We can find vectors spanning the real spine of $\mathscr{B}$ by applying a suitable power of $P$ to the vectors listed

\begin{table}
\begin{tabular}[t]{|l|l|}
\hline Intersection & Giraud disk \\
\hline $\mathscr{R}_{1} \cap \mathscr{S}_{1}$ & $\mathscr{G}\left(y_{0}, R_{1}^{-1} y_{0}, S_{1}^{-1} y_{0}\right)$ \\
\hline $\mathscr{R}_{1}^{-} \cap \mathscr{S}_{1}^{-}$ & $\mathscr{G}\left(y_{0}, R_{1} y_{0}, S_{1} y_{0}\right)$ \\
\hline $\mathscr{S}_{1} \cap \mathscr{S}_{1}^{-}$ & $\mathscr{G}\left(y_{0}, S_{1}^{-1} y_{0}, S_{1} y_{0}\right)$ \\
\hline $\mathscr{R}_{1} \cap P^{-1} \mathscr{R}_{1}^{-}$ & $\mathscr{G}\left(y_{1}, R_{1}^{-1} P y_{1}, P^{-1} R_{1} y_{1}\right)$ \\
\hline $\mathscr{R}_{1} \cap P^{2} \mathscr{S}_{1}$ & $\mathscr{G}\left(y_{2}, R_{1}^{-1} P^{2} y_{2}, P^{2} S_{1}^{-1} P^{-3} y_{2}\right)$ \\
\hline $\mathscr{R}_{1} \cap P^{-2} \mathscr{R}_{1}^{-}$ & $\mathscr{G}\left(y_{2}, R_{1}^{-1} P^{2} y_{2}, P^{-2} R_{1} y_{2}\right)$ \\
\hline $P^{-2} \mathscr{R}_{1}^{-} \cap P^{3} \mathscr{S}_{1}^{-}$ & $\mathscr{G}\left(y_{2}, P^{-2} R_{1} y_{2}, P^{3} S_{1} P^{-2} y_{2}\right)$ \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 4: Giraud intersections among bounding bisectors.}
\end{table}
in Table 1. Using $\iota$,we find an antiholomorphic isometry fixing the spines of $\mathscr{B}$. From this we can then find an image of $y_{j}$ so that $\mathscr{B}$ is coequidistant from $y_{j}$ and this second point.

To be specific, the real spine of $\mathscr{R}_{1}$ is invariant under the involution $\iota_{23}$ defined in (17). We see that $\iota_{23} \mathbf{y}_{1}=\bar{a}^{6} J \mathbf{y}_{1}$ and $\iota_{23} \mathbf{y}_{2}=a^{2} R_{1}^{-1} P^{2} \mathbf{y}_{2}$. Therefore, using $J=R_{1}^{-1} P$ we see that $\mathscr{R}_{1}=\mathscr{B}\left(y_{1}, R_{1}^{-1} P y_{1}\right)=\mathscr{B}\left(y_{2}, R_{1}^{-1} P^{2} y_{2}\right)$. Similarly, the spine of $P^{2} \mathscr{S}_{1}$ is the real span of $\mathbf{n}_{2}=-P^{2} \mathbf{n}_{23 \overline{2}}$ and $\mathbf{n}_{123 \overline{2}}=P^{2} \bar{a} \mathbf{n}_{1 \overline{3} 23}$. These two vectors are fixed by $\bar{a}^{2} R_{2} \iota_{13}$, where $\iota_{13}$ is defined analogously to $\iota_{23}$. We find that $\bar{a}^{2} R_{2} \iota_{13} \mathbf{y}_{2}=a^{2} P^{2} S_{1}^{-1} P^{-3} \mathbf{y}_{2}$. Therefore $P^{2} \mathscr{S}_{1}=\mathscr{B}\left(y_{2}, P^{2} S_{1}^{-1} P^{-3} y_{2}\right)$.

The claims in Table 4 follow at once from those in Table 3. \(\square\)

\subsection*{4.8.4 Realizing ridges of $\widehat{E}$ - embedding}

From the results in Section 4.8.3, we get that $\phi$ gives a well defined realization of each 2-face $f$ of $\widehat{E}$, inside the intersection of two specific bounding bisectors.

For every other bounding bisector $\mathscr{B}$, we now prove that $\phi(f)$ is on the correct side of $\mathscr{B}$. In particular, we will show that $\phi\left(f^{\circ}\right)$ does not intersect $\mathscr{B}$, and $\mathscr{B}$ intersects $\phi(f)$ precisely as predicted from the labels in Figures 6 to 8. From this, it follows that $\phi$ is an embedding on the level of $\widehat{E}_{2}$.

First, observe that when $\phi(f)$ is in a complex line, no further verifications are needed, due to the following.

Lemma 4.38 Let $Q$ be a polygon contained in a complex line $C$, and let $\mathscr{B}$ be a bisector. If $\partial Q$ is entirely on one side of $\mathscr{B}$, then so is $Q$.

Proof. The restriction to $C$ of the orthogonal projection onto the complex spine of $\mathscr{B}$ is an open map (because it is holomorphic). Recall that a set is entirely on one side of $\mathscr{B}$ if and only if its orthogonal projection onto the complex spine is in the corresponding half disk bounded by the real spine. \(\square\)

Orthogonal projections restricted to Giraud disks are, in general, not open. Hence the cases where $\phi(f)$ lies in a Giraud disk are considerably more complicated. They will occupy us for the remainder of this section.

Let us start with a Giraud polygon $T$ in a Giraud disk $\mathscr{G}$ (i.e. a disk bounded by a piecewise geodesic simple closed curve) and a bisector $\mathscr{B}$ not containing $\mathscr{G}$. We describe a general method to prove that $T$ is entirely on one side of $\mathscr{B}$.

Let $\mathscr{B}=\mathscr{B}\left(x_{0}, x_{1}\right)$, and assume that $\mathbf{x}_{0}, \mathbf{x}_{1}$ are lifts of $x_{0}, x_{1}$ with $\left\langle\mathbf{x}_{0}, \mathbf{x}_{0}\right\rangle=\left\langle\mathbf{x}_{1}, \mathbf{x}_{1}\right\rangle$. Using the parametrization given in Section 2.5 (4), we may write an equation for the trace of $\mathscr{B}$ on $\mathscr{G}$ as
$$g\left(t_{1}, t_{2}\right)=0 \text {, where } g\left(t_{1}, t_{2}\right)=\left|\left\langle V\left(t_{1}, t_{2}\right), \mathbf{x}_{0}\right\rangle\right|^{2}-\left|\left\langle V\left(t_{1}, t_{2}\right), \mathbf{x}_{1}\right\rangle\right|^{2} .$$
Since $V\left(t_{1}, t_{2}\right)$ is affine in each variable, equation (27) is quadratic in each variable.
If we claim that $\mathscr{B} \cap T$ is empty, we need to prove that $g$ does not vanish on $T$, for instance that $g>0$ (switch $x_{0}$ and $x_{1}$ if needed). In order to do this, we
\begin{itemize}
\item[1.] check that $g>0$ on the boundary of $T$ (see Section 2.7).
\item[2.] find the critical points of $g$. If they are in $T$, check the sign of the corresponding values of $g$.
\end{itemize}

This strategy works well in most cases, because of the following.
Proposition 4.39 The coefficients of $g$ lie in the field $\mathbb{Q}(a, \tau)$. The fact that $g$ only has non-degenerate critical points can be proved using computations in that number field, and the critical points can then be computed with arbitrary precision.

Since the key to these computations is to be able to compute critical points of $g$, we expand a little on how this can be done in practice. We write $g$ as
$$g\left(t_{1}, t_{2}\right)=a_{0}+a_{1} t_{1}+a_{2} t_{2}+a_{11} t_{1}^{2}+a_{12} t_{1} t_{2}+a_{22} t_{2}^{2}+a_{112} t_{1}^{2} t_{2}+a_{122} t_{1} t_{2}^{2}+a_{1122} t_{1}^{2} t_{2}^{2},$$
where all coefficients are real, and depend explicitly on the vectors $\mathbf{v}_{j}, \mathbf{w}_{j}$ (and are known in exact form, see Proposition 4.39). The partial derivatives of this function are given by
$$\left\{\begin{array}{l}
\frac{\partial g}{\partial t_{1}}\left(t_{1}, t_{2}\right)=\left(a_{1}+a_{12} t_{2}+a_{122} t_{2}^{2}\right)+2 t_{1}\left(a_{11}+a_{112} t_{2}+a_{1122} t_{2}^{2}\right)=P_{2}\left(t_{2}\right)+t_{1} Q_{2}\left(t_{2}\right) \\
\frac{\partial g}{\partial t_{2}}\left(t_{1}, t_{2}\right)=\left(a_{2}+a_{12} t_{1}+a_{112} t_{1}^{2}\right)+2 t_{2}\left(a_{22}+a_{122} t_{1}+a_{1122} t_{1}^{2}\right)=P_{1}\left(t_{1}\right)+t_{2} Q_{1}\left(t_{1}\right)
\end{array}\right.$$
where the polynomials $P_{j}, Q_{j}$ have degree at most two. Coordinates of the critical points must be solutions of a polynomial of degree five, obtained as the resultant of $\frac{\partial g}{\partial t_{1}}$ and $\frac{\partial g}{\partial t_{2}}$ (with respect to, say $t_{1}$ ).

Explicitly, if $\left(t_{1}, t_{2}\right)$ is a critical point, then $t_{2}$ is a root of $\sum_{k=0}^{5} b_{k} x^{k}$ where
$$\begin{aligned}
b_{0}= & a_{1}^{2} a_{112}+4 a_{2} a_{11}^{2}-2 a_{12} a_{11} a_{1} \\
b_{1}= & -4 a_{122} a_{11} a_{1}+2 a_{1}^{2} a_{1122}+8 a_{22} a_{11}^{2}-2 a_{12}^{2} a_{11}+8 a_{2} a_{11} a_{112} \\
b_{2}= & 8 a_{2} a_{11} a_{1122}+2 a_{1} a_{1122} a_{12}-2 a_{1} a_{112} a_{122}-6 a_{12} a_{11} a_{122} \\
& \quad+4 a_{2} a_{112}^{2}-a_{12}^{2} a_{112}+16 a_{22} a_{11} a_{112} \\
b_{3}= & 8 a_{2} a_{112} a_{1122}+8 a_{22} a_{112}^{2}-4 a_{12} a_{112} a_{122}-4 a_{122}^{2} a_{11}+16 a_{22} a_{11} a_{1122} \\
b_{4}= & -3 a_{122}^{2} a_{112}-2 a_{122} a_{1122} a_{12}+4 a_{2} a_{1122}^{2}+16 a_{22} a_{112} a_{1122} \\
b_{5}= & -2 a_{122}^{2} a_{1122}+8 a_{22} a_{1122}^{2}
\end{aligned}$$
The real roots of this polynomial can be computed with arbitrary precision, most easily when it only has simple roots (in that case the Sturm algorithm suffices). In particular, we can count critical points and locate them.

There are situations where the resultant has multiple roots, but there is an easy way to work around these, which turns out to work for all verifications needed in our paper. The point is that there is a simple reason why the resultant can have multiple roots, namely that the intersection $\mathscr{G} \cap \mathscr{B}$ contains a horizontal or a vertical segment.

Each time this happens, we can factor out a linear expression in one of the two variables (or in some cases one factor for each variable), and in fact we will be able to do this exactly (i.e. no numerical approximation is involved).

More specifically, suppose the line $t_{1}=\alpha$ is contained in the graph (the situation is obviously entirely similar for horizontal lines). Then we write the function in the form
$$g\left(t_{1}, t_{2}\right)=p_{0}\left(t_{1}\right)+p_{1}\left(t_{1}\right) t_{2}+p_{2}\left(t_{1}\right) t_{2}^{2},$$
where the $p_{j}$ are polynomials of degree at most two. Then the coefficients $p_{0}, p_{1}$ and $p_{2}$ must have $\alpha$ as a common root, and these roots are easily computed.

Lemma 4.40 The vertical lines in the graph of $g\left(t_{1}, t_{2}\right)=0$ are given by the equations $t_{1}=\alpha$ where $\alpha$ is a common root of the polynomials $p_{j}, j=0,1,2$.

It can easily be guessed using numerical computations whether or not these three polynomials have a common root; when they do not, these numerical computations constitute a proof (possibly after adjusting the precision). When they seem to have a common root, we need to verify this by exact calculations. We will work out the details of these verifications for some explicit examples below.

Note that when $\left\{t_{1}=\alpha\right\}$ is indeed contained in the graph, it is of course easy to extract a factor $\left(t_{1}-\alpha\right)$ from $g\left(t_{1}, t_{2}\right)$. Explicitly, we write
$$g\left(t_{1}, t_{2}\right)=q_{0}\left(t_{2}\right)+q_{1}\left(t_{2}\right) t_{1}+q_{2}\left(t_{2}\right) t_{1}^{2}=\left(t_{1}-\alpha\right) h\left(t_{1}, t_{2}\right)$$
and equate the coefficients of degree 0 and 2 in $t_{1}$, to get
$$h\left(t_{1}, t_{2}\right)=q_{2}\left(t_{2}\right) t_{1}+q_{1}\left(t_{2}\right)+\alpha q_{2}\left(t_{2}\right) .$$

Remark 4.41 When we do this factorization, it is convenient to adjust the sign of $h$ so that it has the same sign as $g$ on the open ridge we are studying. Depending on whether the side lies to the left or right of the line $t_{1}=\alpha$, we factor either $\left(t_{1}-\alpha\right)$ or $\left(\alpha-t_{1}\right)$.

The point of this remark is that in order to verify $g \geqslant 0$ on a Giraud polygon $T$, it is enough to verify that $h \geqslant 0$ on $T$, and we will do this by computing the critical points of $h$. Note that the critical points of $h$ are of course not the same as those of $g$, but they are easier to handle computationally (the relevant resultants will have simple roots, see the above discussion).

We now work out the details of the above computations in some specific cases. In order to allow for the reader to verify the numerical figures given below, we specify explicit coordinates for the relevant Giraud disks, giving specific choices of vectors $\mathbf{v}_{j}$ and $\mathbf{w}_{j}$ defining spinal coordinates as in (4).

It is convenient to adjust the Giraud disk to be bounded in these coordinates, hence we choose the $\mathbf{w}_{j}$ to be negative vectors. For instance, for $\mathscr{R}_{1}$ one can choose $\mathbf{v}=\mathbf{n}_{1}$ and
$$\mathbf{w}=\left\langle\mathbf{n}_{1}, \mathbf{n}_{1}\right\rangle \mathbf{n}_{23}-\left\langle\mathbf{n}_{23}, \mathbf{n}_{1}\right\rangle \mathbf{n}_{1},$$

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/31f0f35c-0604-47ef-a2ef-a49ed021037c-55.jpg?height=1089&width=1559&top_left_y=870&top_left_x=266}
\captionsetup{labelformat=empty}
\caption{Figure 15: Intersection pattern of all the bounding sides with the complex line $\mathscr{R}_{1} \cap \mathscr{R}_{1}^{-}$, according to the values of $p$.}
\end{figure}

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/31f0f35c-0604-47ef-a2ef-a49ed021037c-56.jpg?height=1177&width=1560&top_left_y=823&top_left_x=266}
\captionsetup{labelformat=empty}
\caption{Figure 16: Intersection pattern of all the bounding sides with the Giraud disk $\mathscr{R}_{1} \cap \mathscr{S}_{1}$, according to the values of $p$.}
\end{figure}
which corresponds to the intersection of the real spine of $\mathscr{R}_{1}$ with the mirror of $R_{1}$. For $\mathscr{S}_{1}$, one can choose $\mathbf{v}=\mathbf{n}_{23 \overline{2}}$ and
$$\mathbf{w}=\left\langle\mathbf{n}_{23 \overline{2}}, \mathbf{n}_{1 \overline{3} 23}\right\rangle\left\{\left\langle\mathbf{n}_{23 \overline{2}}, \mathbf{n}_{23 \overline{2}}\right\rangle \mathbf{n}_{1 \overline{3} 23}-\left\langle\mathbf{n}_{1 \overline{3} 23}, \mathbf{n}_{23 \overline{2}}\right\rangle \mathbf{n}_{23 \overline{2}}\right\} .$$
There is then a well-defined parametrization for every Giraud intersection of bounding bisectors, obtained from the above vectors by applying $R_{1}, S_{1}$ and/or powers of $P$.

We give the verifications for one situation, namely $\mathscr{G}=\mathscr{R}_{1} \cap \mathscr{S}_{1}=\mathscr{B}_{1} \cap \mathscr{B}_{3}$ (see Table 2 on page 48 for an explanation of the labelling of the sides). For concreteness, we start by assuming $p=3$ (for other values of $p$ and other ridges, the computations are only longer, but not more complicated). In this case $T$ is a triangle.

The intersection $\mathscr{G} \cap \mathscr{B}_{2}$ is particularly easy, since $\mathscr{R}_{1} \cap \mathscr{R}_{1}^{-}$is a complex line, namely the mirror of $R_{1}$ (see Section 4.8.3). If we take $\mathbf{x}_{0}=\mathbf{y}_{0}, \mathbf{x}_{1}=R_{1} \mathbf{y}_{0}$ and write an equation for $\mathscr{G} \cap \mathscr{B}_{2}$, we get
$$g\left(t_{1}, t_{2}\right)=81(582+127 \sqrt{21})\left(-14+3 \sqrt{21}+3 t_{2}-18 t_{2}^{2}\right) t_{1},$$
where the degree 2 polynomial in $t_{2}$ never vanishes, so the intersection is given by the $t_{2}$-axis.
When $\mathscr{B}=\mathscr{S}_{1}^{-}=\mathscr{B}_{4}$, we take $\mathbf{x}_{0}=\mathbf{y}_{0}, \mathbf{x}_{1}=S_{1} \mathbf{x}$. In that case, we already know that the $t_{2}$-axis is part of $\mathscr{G} \cap \mathscr{S}_{1}^{-}$(see Section 4.8.2), so we must have $a_{0}=a_{2}=a_{22}=0$, but in fact no other coefficient vanishes. The reduced equation $g=f / t_{1}$ is given by
$$h\left(t_{1}, t_{2}\right)=81(6741+1471 \sqrt{21})\left(36-8 \sqrt{21}-15 t_{1}+3 t_{1} \sqrt{21}-3 t_{2} \sqrt{21}+9 t_{2}+18 t_{1} t_{2}\right) / 4 .$$

Here the partial derivatives are both functions of one variable only, which immediately gives a critical point with coordinates
$$((-3+\sqrt{21}) / 6,(5-\sqrt{21}) / 6) \approx(0.26376261 \ldots, 0.06957071 \ldots) .$$
It is easy to verify that this is outside $T$.
The case $\mathscr{B}=P \mathscr{R}_{1}=\mathscr{B}_{5}$ is in a sense generic; there are no horizontal or vertical lines, and the resultant of $\partial f / \partial t_{1}$ and $\partial f / \partial t_{2}$ with respect to $t_{2}$ is given by
$$\begin{aligned}
& -223205130784873566-48707352729720306 \sqrt{21} \\
& +(1289075326223152230+281299298043708180 \sqrt{21}) t_{1} \\
& -(1960742086219144494+427869001351675404 \sqrt{21}) t_{1}^{2} \\
& +(2269952366448531240+495344216342598840 \sqrt{21}) t_{1}^{3} \\
& -(1166845194031834926+254626496473636566 \sqrt{21}) t_{1}^{4} \\
& +(259717950970322292+56675103317162172 \sqrt{21}) t_{1}^{5} .
\end{aligned}$$
This polynomial has precisely one real root, which is a simple root, given approximately by $t_{1}=0.23860554 \ldots$. Substituting this value into the partial derivatives yields a polynomial of degree 1 and a polynomial of degree 2 ; solving the degree one equation gives one value for $t_{2}$, and we get precisely one critical point with coordinates $(0.23860554 \ldots, 0.01603880 \ldots)$. This point is outside $T$.

From now on, we do not write down all the calculations, but simply mention some of the possible phenomena.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/31f0f35c-0604-47ef-a2ef-a49ed021037c-58.jpg?height=1310&width=1609&top_left_y=506&top_left_x=278}
\captionsetup{labelformat=empty}
\caption{Table 5: Lines parallel to coordinate axes contained in the graphs, for $\mathscr{B}_{1} \cap \mathscr{B}_{3}$.}
\end{figure}

\begin{table}
\begin{tabular}[t]{|l|l|l|l|}
\hline $p$ & Side & Coordinates & Function value \\
\hline 8 & $\mathscr{B}_{9}$ & (0.22347669..., 0.06214532...) & 11.44128654... \\
\hline 12 & $\mathscr{B}_{9}$ & (0.38008133. . . , 0.18112900. . .) & 0.23597323... \\
\hline & $\mathscr{B}_{10}$ & (0.38823985…, 0.13852442. . . ) & 0.18097266... \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 6: Critical points inside the ridge for $\mathscr{B}_{1} \cap \mathscr{B}_{3}$.}
\end{table}

Consider the intersection of $\mathscr{G}$ with $P \mathscr{S}_{1}^{-}=\mathscr{B}_{11}$, for instance. In that case $g$ is given by $27(6741+1471 \sqrt{21})\left(-15 t_{1}+3 t_{1} \sqrt{21}+36-8 \sqrt{21}+18 t_{1} t_{2}-3 t_{2} \sqrt{21}+9 t_{2}\right)\left(21-42 t_{1}+\sqrt{21}\right) t_{2} / 56$.
Clearly there are both a horizontal and a vertical line in this intersection, in which case we factor out two linear factors, one linear in $t_{1}$ and the other linear in $t_{2}$. The reduced equation is given by the function
$$81(6741+1471 \sqrt{21})\left(-15 t_{1}+3 t_{1} \sqrt{21}+36-8 \sqrt{21}+18 t_{1} t_{2}-3 t_{2} \sqrt{21}+9 t_{2}\right) / 4 .$$
The latter has one critical point given by
$$((-3+\sqrt{21}) / 6,(5-\sqrt{21}) / 6) \approx(0.26376261 \ldots, 0.06957071 \ldots)$$
and this point is outside $T$.
In fact for $p \leqslant 6$, all critical points turn out to be outside the Giraud polygon, whereas this is not quite true for $p=8$ or 12 (see Table 6). For higher values of $p$, the computations are a bit longer and more tedious than for $p=3$, since the coefficients of the equations live in slightly larger number fields, but they are not more difficult in any essential way.

For the convenience of the skeptic reader (who may be willing to check our claims), we list all horizontal and vertical lines for curves on $\mathscr{B}_{1} \cap \mathscr{B}_{3}$, see Table 5. These are needed to reduce to the case of resultants with only simple root. The numbers given as decimal expansions are written in this manner simply to avoid writing huge formulae, one can easily get explicit algebraic expressions instead.

In Table 6, we list the critical points that lie inside the ridge $\mathscr{B}_{1} \cap \mathscr{B}_{3}$ (there are critical points inside only for $p=8$ and $p=12$ ). For each of them, we need to check that the corresponding value of the function $h$ is strictly positive (recall that $h$ is equal to the equation of the intersection in most cases, it is obtained by dividing by appropriate linear factors in one variable).

For future reference we mention the following consequence of the above arguments.
Proposition 4.42 Let $\rho$ be a ridge of $\widehat{E}$, and let $D$ be the (Giraud or complex) disk containing $\phi(\rho)$. Then there is an open neighborhood $U$ of $\phi(\rho)$ in $D$ such that $U \cap E=\phi(\rho)$.

In particular, even though we did not prove that $\phi(\rho)=D \cap F$, we know that $\phi(\rho)$ is a connected component of $D \cap F$.

\subsection*{4.8.5 Realizing sides of $\widehat{E}$}

As mentioned early in Section 4.6, no consistency verifications are needed for 3-cells. We do need to check embeddedness. More specifically, we check the following.

Proposition 4.43 For each 3-cell $f$ of $\widehat{E}$ and every bounding bisector $\mathscr{B}, \phi(f)$ is on the correct side of $\mathscr{B}$. In particular, $\phi(f)$ is contained in $F$.

This will follow from the following result, which is of general independent interest.
Lemma 4.44 Let $f$ be one of the bounding sides and let $\mathscr{B}$ be any bisector. If $\mathscr{B}$ intersects the interior $f^{\circ}$, then it intersects its boundary $\partial f$ as well.

Proof. (of Lemma 4.44) We may assume that $\mathscr{B}$ does not contain $f$, and we denote by $\mathscr{B}_{f}$ the bisector containing $f$. By Lemma 9.1.5 in [Gol99], $\mathscr{B} \cap \mathscr{B}_{f}$ is either empty or a union of properly embedded disks. If $\mathscr{B}$ intersects the interior of $f$, then by properness it must also intersect its boundary (in $\overline{\mathbf{H}}_{\mathbb{C}}^{2}$ ). \(\square\)

Proof. (of Proposition 4.43) Recall that for each 3-cell $f$ of $\widehat{E}, \partial f$ is a 2-sphere, and we have checked in Section 4.8.4 that $\phi$ embeds that 2-sphere inside one of the bounding bisectors $\mathscr{B}_{f}$ (as well as inside $E$ ). Now if $\mathscr{B}$ is any other bounding bisector, $\mathscr{B}$ cannot intersect $\phi\left(f^{\circ}\right)$. For this we argue by contradiction; if it did, then by Lemma 4.44, it would also intersect $\phi(\partial f)$. But this cannot happen, since the closed set $\phi(f) \cap \mathscr{B} \cap \mathscr{B}_{f}$ has a neighborhood in $\mathscr{B} \cap \mathscr{B}_{f}$ which does not intersect $\phi\left(f^{\circ}\right)$ (see Proposition 4.42). \(\square\)

For completeness, we mention the following consequence of Proposition 4.43.
Proposition 4.45 Let $\mathscr{B}$ be one of the bounding bisectors, and $f$ the side of $\widehat{E}$ such that $\phi(f) \subset \mathscr{B}$. Then $\mathscr{B} \cap E=\phi(f)$.

Note that we have not proved that $\phi(f)$ can also be described as $\mathscr{B} \cap F$, but once again this is not needed in order to apply the Poincaré polyhedron theorem (see the discussion at the beginning of Section 4).

\section*{5 Applying the Poincaré polyhedron theorem}

We proved in Section 4.6 that $E$ is a polyhedron. In this section we verify the remaining hypotheses of the Poincaré polyhedron theorem (Sections 5.2 and 5.3). Using the theorem, we obtain a presentation for $\Gamma$ and we calculate the orbifold Euler characteristic of the quotient orbifold.

Along with the verification of the hypotheses, we will determine local stabilizers of every facet $f$ of $E$. By local stabilizer, we mean the group obtained from the side-pairing maps by following all possible cycles involving $f$. The description of local stabilizers for cusps will imply the existence of a consistent system of horoballs.

Note that the local stabilizer of a facet $f$ is always a subgroup of the full stabilizer of $f$ in $\Gamma$. It will follow from the Poincaré polyhedron that local stabilizers are actually equal to the corresponding full stabilizer. We will determine local stabilizers of ridges in Section 5.2, then for vertices and edges in Section 5.3.

\subsection*{5.1 Hypotheses - side pairing}

In this section, we describe a side pairing for $E$ (in the sense of Section 3.2). For each side $s$, we define an isometry $S=\sigma(s)$ that pairs two sides $s$ and $s^{-}$of $E$. We also show that $E \cap S(E)$ is given precisely by $s^{-}$.

Lemma 5.1 The map $R_{1}$ sends $r_{1}=\mathscr{R}_{1} \cap E$ to $r_{1}^{-}=\mathscr{R}_{1}^{-} \cap E$ preserving the cell structure. The map $S_{1}$ sends $s_{1}=\mathscr{S}_{1} \cap E$ to $s_{1}^{-}=\mathscr{S}_{1}^{-} \cap E$ preserving the cell structure.

Proof. Using the description of the bisectors given in Table 1 it is clear that $R_{1}$ maps $\mathscr{R}_{1}$ to $\mathscr{R}_{1}^{-}$. Moreover, $R_{1}$ maps the complex lines containing ridges of $r_{1}$ to the complex
lines containing ridges of $r_{1}^{-}$. Specifically, $R_{1}$ sends $m_{1}=\mathscr{R}_{1} \cap \mathscr{R}_{1}^{-}$to itself and maps $m_{23}=\mathscr{R}_{1} \cap P^{-3} \mathscr{R}_{1}^{-}$to $m_{123 \overline{1}}=\mathscr{R}_{1}^{-} \cap P^{3} \mathscr{R}_{1}$.

We claim that the Giraud disks containing ridges of $\mathscr{R}_{1}$ are mapped to Giraud disks containing ridges of $\mathscr{R}_{1}^{-}$. For a list of these Giraud disks, see Table 4. We give the details for one such Giraud disk, namely $\mathscr{R}_{1} \cap P^{2} \mathscr{S}_{1}$, the other arguments are entirely similar. Recall that the two corresponding bisectors have the following description in terms of the point $y_{2}$ :
$$\mathscr{R}_{1}=\mathscr{B}\left(y_{2}, R_{1}^{-1} P^{2} y_{2}\right), \quad P^{2} \mathscr{S}_{1}=\mathscr{B}\left(y_{2}, P^{2} S_{1}^{-1} P^{-3} y_{2}\right) .$$
Applying $R_{1}$ to these bisectors, we obtain
$$\mathscr{R}_{1}^{-}=R_{1} \mathscr{R}_{1}=\mathscr{B}\left(R_{1} y_{2}, P^{2} y_{2}\right), \quad R_{1} P^{2} \mathscr{S}_{1}=\mathscr{B}\left(R_{1} y_{2}, P^{2} R_{1}^{-1} P^{2} y_{2}\right) .$$
Here we have used $S_{1}=P^{2} R_{1} P^{-2} R_{1} P^{2}$ and $P^{-5}=P^{2}$ to write $R_{1} P^{2} S_{1}^{-1} P^{-3}=P^{2} R_{1}^{-1} P^{2}$. The third bisector containing this Giraud disk is
$$\mathscr{B}\left(P^{2} y_{2}, P^{2} R_{1}^{-1} P^{2} y_{2}\right)=P^{2} \mathscr{B}\left(y_{2}, R_{1}^{-1} P^{2} y_{2}\right)=P^{2} \mathscr{R}_{1} .$$
Therefore the Giraud disk $\mathscr{R}_{1} \cap P^{2} \mathscr{S}_{1}$ is sent by $R_{1}$ to the Giraud disk $\mathscr{R}_{1}^{-} \cap P^{2} \mathscr{R}_{1}$.
This shows that the complex lines and Giraud disks containing the ridges of $r_{1}$ are sent to complex lines and Giraud disks containing ridges of $r_{1}^{-}$. The corresponding statement about vertices (resp. edges) follows from the one about ridges, since the vertices (resp. edges) can be described as intersections of ridges. This shows that $R_{1}$ maps $r_{1}=\mathscr{R}_{1} \cap E$ to $r_{1}^{-}=\mathscr{R}_{1}^{-} \cap E$, preserving the cell structure. \(\square\)

We now define the side pairing used in our application of the Poincaré polyhedron theorem.
Proposition 5.2 The following map $\sigma$ defines a side pairing on the sides of $E$ :
$$\sigma\left(P^{k} r_{1}^{ \pm}\right)=P^{k} R_{1}^{ \pm 1} P^{-k}, \quad \sigma\left(P^{k} s_{1}^{ \pm}\right)=P^{k} S_{1}^{ \pm 1} P^{-k},$$
where $k=-3, \ldots, 3$. Moreover, this side pairing is compatible with $\Upsilon=\langle P\rangle$.
Proof. We only give the argument for $r_{1}=\mathscr{R}_{1} \cap E$. Applying powers of $P$ and the symmetry $\iota$ gives the result for the other faces $P^{k} r_{1}^{ \pm}$, and the faces $P^{k} s_{1}^{ \pm}$are similar.

In Lemma 5.1 we showed that $R_{1}$ sends $r_{1}$ to $r_{1}^{-}$preserving the cell structure. Moreover, the interior of $E$ is contained in the half-space closer to $y_{0}$ than to $R_{1} y_{0}$, where $y_{0}$ is given in Lemma (4.36). Hence, the interior of $R_{1}^{-1} E$ is contained in the half-space closer to $R_{1}^{-1} y_{0}$ than to $y_{0}$. Thus $E$ and $R_{1}^{-1} E$ intersect in $\mathscr{R}_{1} \cap E=r_{1}$ (see Proposition 4.45) and their interiors are disjoint. Furthermore, any point in the interior of $r_{1}$ has an open neighborhood contained in $E \cup R_{1}^{-1} E$. \(\square\)

\subsection*{5.2 Hypotheses - local tessellation}

We now study the ridge cycles of $E$, as explained in Section 3.2.
For $p=3$ and $p=4$ we obtain the ridge cycles given in Table 7. The second column lists the successive ridges in the cycle, given as the intersection of two sides, whereas in the third column we list the corresponding vertices (with ordering coherent with the successive

\begin{table}
\begin{tabular}[t]{|l|l|l|l|l|l|}
\hline \multirow[t]{2}{*}{$R_{1}$} & $r_{1} \cap r_{1}^{-}$ & $p_{12}$ & $p_{13}$ & $q_{1 \overline{3} 23}$ & $q_{123 \overline{2}}$ \\
\hline & $r_{1} \cap r_{1}^{-}$ & $p_{12}$ & $p_{13}$ & $q_{1323}$ & $q_{123 \overline{2}}$ \\
\hline $R_{1}$ & $r_{1} \cap P^{-1} r_{1}^{-}$ & $p_{12}$ & $p_{13}$ & $p_{23}$ & \\
\hline \multirow[t]{2}{*}{$P^{-1}$} & $P r_{1} \cap r_{1}^{-}$ & $p_{12}$ & $p_{13}$ & $p_{123 \overline{1}}$ & \\
\hline & $r_{1} \cap P^{-1} r_{1}$ & $p_{13}$ & $p_{23}$ & $p_{12}$ & \\
\hline $R_{1}$ & $r_{1} \cap P^{2} s_{1}$ & $p_{23}$ & $p_{12}$ & $q_{123 \overline{2}}$ & \\
\hline $P^{2} R_{1} P^{-2}$ & $P^{2} r_{1} \cap r_{1}^{-}$ & $p_{123 \overline{1}}$ & $p_{12}$ & $q_{123 \overline{2}}$ & \\
\hline $S_{1}^{-1}$ & $s_{1}^{-} \cap P^{2} r_{1}^{-}$ & $p_{123 \overline{1}}$ & $p_{\overline{3}} \overline{2} 3123$ & $q_{123 \overline{2}}$ & \\
\hline $P^{2}$ & $P^{-2} r_{1} \cap s_{1}$ & $p_{\overline{3}} \overline{2} 3123$ & $p_{23}$ & $q_{1 \overline{3} 23}$ & \\
\hline & $r_{1} \cap P^{2} s_{1}$ & $p_{23}$ & $p_{12}$ & $q_{123 \overline{2}}$ & \\
\hline $R_{1}$ & $r_{1} \cap s_{1}$ & $p_{23}$ & $q_{1 \overline{3} 23}$ & $q_{123 \overline{2}}$ & \\
\hline $S_{1}^{-1}$ & $s_{1}^{-} \cap r_{1}^{-}$ & $p_{123 \overline{1}}$ & $q_{1 \overline{3} 23}$ & $q_{123 \overline{2}}$ & \\
\hline $S_{1}^{-1}$ & $s_{1}^{-} \cap s_{1}$ & $p_{\overline{3}} \overline{2} 3123$ & $q_{123 \overline{2}}$ & $q_{1 \overline{3} 23}$ & \\
\hline & $r_{1} \cap s_{1}$ & $p_{23}$ & $q_{1323}$ & $q_{123 \overline{2}}$ & \\
\hline $S_{1}$ & $s_{1} \cap P^{2} s_{1}^{-}$ & $p_{23}$ & $p_{\overline{3}} \overline{2} 3123$ & $q_{123 \overline{2}}$ & \\
\hline $P^{2}$ & $P^{-2} s_{1} \cap s_{1}^{-}$ & $p_{\overline{3}}{ }_{\overline{2}} 123$ & $p_{123 \overline{1}}$ & $q_{1323}$ & \\
\hline & $s_{1} \cap P^{2} s_{1}^{-}$ & $p_{23}$ & $p_{\overline{3} \overline{2} 3123}$ & $q_{123 \overline{2}}$ & \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 7: The ridge cycles for $p=3$, 4. For higher values of $p$ the cycles are the same, but additional vertices appear in the right and column.}
\end{table}
side pairing maps). Applying the side pairing map in the first column (which corresponds to the first side in the second column) gives the line below. The product of these side pairing maps gives the cycle transformation.

This cycle transformation may not be the identity on $\mathbf{H}_{\mathbb{C}}^{2}$, or even on the ridge. However, we can find a power that is the identity, which gives the cycle relation. For example, $R_{1}$ maps $r_{1} \cap r_{1}^{-}$to itself and acts as the identity on this ridge (which can be seen from the vertices in the third column). The cycle relation is $R_{1}^{p}=i d$. On the other hand, for $r_{1} \cap P^{-1} r_{1}^{-}$we obtain the cycle transformation $P^{-1} R_{1}$. This maps $r_{1} \cap P^{-1} r_{1}^{-}$to itself but cyclically permutes the vertices. Therefore the cycle relation is $\left(P^{-1} R_{1}\right)^{3}=i d$.

As a last example, we work out the cycle for the ridge $r_{1} \cap P^{2} s_{1}$. It is mapped by $R_{1}$ to $P^{2} r_{1} \cap r_{1}^{-}$(see the proof of Proposition 5.2), which is then mapped by $P^{2} R_{1} P^{-2}$ to $s_{1}^{-} \cap P^{2} r_{1}^{-}$, which is then mapped by $S_{1}^{-1}$ to $P^{-2} r_{1} \cap s_{1}$. This is clearly in the image of the original ridge under a power of $P$, and the corresponding cycle transformation is
$$P^{2} \cdot S_{1}^{-1} \cdot P^{2} R_{1} P^{-2} \cdot R_{1} .$$
This isometry is in fact the identity (see its expression in terms of the vertices in the last column of Table 7), which corresponds to our definition of $S_{1}$ (see Section 4.1).

For $p=5,6,8$ and 12, the ridge cycles from $p=3,4$ persist, even though the corresponding polygons have extra vertices corresponding to the truncations. We also have an extra ridge cycle associated to $r_{1} \cap P^{-3} r_{1}^{-}$given in Table 8. Note that $P^{-3} R_{1}$ maps $r_{1} \cap P^{-3} r_{1}^{-}$to itself but does not act as the identity on this ridge; $\left(P^{-3} R_{1}\right)^{2}$ acts as the identity on $r_{1} \cap P^{-3} r_{1}^{-}$ but not on $\mathbf{H}_{\mathbb{C}}^{2}$ and $\left(P^{-3} R_{1}\right)^{4 p /(p-4)}=i d$. When $p=8$ and $p=12$ we also have the ridge cycle associated to $s_{1} \cap P^{-2} s_{1}^{-}$given in Table 8.

As a summary, thanks to the action of powers of $P$ and the freedom to choose the initial ridge inside a given ridge cycle (which does not affect the cycle relation, see Section 3.2), it is
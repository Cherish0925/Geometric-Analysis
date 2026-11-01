---
retention_scope: session
part: 4
total_parts: 4
---

[Part 4/4 of: New non-arithmetic complex hyperbolic lattices]

\begin{table}
\begin{tabular}[t]{|l|l|l|l|l|l|l|}
\hline \multirow[t]{3}{*}{$p \geqslant 5$} & $R_{1}$ & $r_{1} \cap P^{-3} r_{1}^{-}$ & $p_{23}^{2}$ & $p_{23}^{232}$ & $p_{23}^{323}$ & $p_{23}^{3}$ \\
\hline & \multirow[t]{2}{*}{$P^{-3}$} & $P^{3} r_{1} \cap r_{1}^{-}$ & $p_{123 \overline{1}}^{121}$ & $p_{123 \overline{1}}^{123 \overline{1}} \overline{1}$ & $p_{123 \overline{1}}^{1323 \overline{1}}$ & $p_{23}^{131}$ \\
\hline & & $r_{1} \cap P^{-3} r_{1}^{-}$ & $p_{23}^{323}$ & $p_{23}^{3}$ & $p_{23}^{2}$ & $p_{23}^{232}$ \\
\hline \multirow[t]{3}{*}{$p \geqslant 8$} & $S_{1}$ & $s_{1} \cap P^{-2} s_{1}^{-}$ & $q_{1 \overline{3} 23}^{1}$ & $q_{1323}^{323}$ & $q_{1323}^{13231}$ & \\
\hline & \multirow[t]{2}{*}{$P^{-2}$} & $P^{2} \cap s_{1}^{-}$ & $q_{123 \overline{2}}^{1}$ & $q_{123 \overline{2}}^{232}$ & $q_{123 \overline{2}}^{1232}$ & \\
\hline & & $s_{1} \cap P^{-2} s_{1}^{-}$ & $q_{1 \frac{223}{23}}^{323}$ & $q_{1323}^{13231}$ & $q_{1 \overline{2} 23}^{1}$ & \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 8: Additional ridge cycles for higher values of $p$.}
\end{table}
enough to consider the ridges $r_{1} \cap r_{1}^{-}, r_{1} \cap P^{-1} r_{1}^{-}, r_{1} \cap P^{2} s_{1}, r_{1} \cap s_{1}, s_{1} \cap P^{2} s_{1}^{-}, r_{1} \cap P^{-3} r_{1}^{-}$ and $s_{1} \cap P^{-2} s_{1}^{-}$. In the penultimate case we only need consider $p=5,6,8$ and 12 and for the last case, we only need consider $p=8$ and 12. We now show local tiling around each of these ridges.

Recall that the ridges of $E$ are of two very different types, depending on whether they are contained in complex lines or in Giraud disks (see Section 4.8.3).

We first consider the complex ridges (see Proposition 4.35 and Section 4.8.4), and show that the local images of $E$ tessellate around those.

Lemma 5.3 The images of $E$ tessellate a neighborhood of $r_{1} \cap r_{1}^{-}, r_{1} \cap P^{-3} r_{1}^{-}, s_{1} \cap P^{2} s_{1}^{-}$ and $s_{1} \cap P^{-2} s_{1}^{-}$for the appropriate values of $p$. Specifically:
\begin{itemize}
\item[1.] $R_{1}^{k} E$ for $k=0,1 \ldots, p-1$ cover a neighborhood of the interior of $r_{1} \cap r_{1}^{-}$;
\item[2.] if $p=5,6,8,12$ then $\left(R_{2} R_{3}\right)^{k} E$ for $k=0,1 \ldots, 2 c-1=4 p /(p-4)-1$ cover a neighborhood of the interior of $r_{1} \cap P^{-3} r_{1}^{-}$;
\item[3.] $\left(R_{2} R_{3} R_{2}^{-1}\right)^{k} E$ for $k=0,1 \ldots, p-1$ cover a neighborhood of the interior of $s_{1} \cap P^{2} s_{1}^{-}$;
\item[4.] if $p=8,12$ then $\left(R_{1} R_{3}^{-1} R_{2} R_{3}\right)^{k} E$ for $k=0,1 \ldots, 3 d-1=6 p /(p-6)-1$ cover a neighborhood of the interior of $s_{1} \cap P^{-2} s_{1}^{-}$.
\end{itemize}

Proof. Using Lemma 3.4 it suffices to consider a fixed point $o$ in each of these ridges and to show that on the orthogonal complex line $C_{o}^{\perp}$ the cycle transformation acts as a rotation through angle $2 \pi / \ell$.

For Parts 1 and 3 this is straightforward since $R_{1}$ and $R_{2} R_{3} R_{2}^{-1}$ are complex reflections with angle $2 \pi / p$ fixing $r_{1} \cap r_{1}^{-}$and $s_{1} \cap P^{2} s_{1}^{-}$respectively. For Parts 2 and 4 we find the rotation angle by finding eigenvalues associated to the complex line and the fixed point.

For $p \geqslant 5$, the complex line $m_{23}$ and the fixed point $o_{23}$ of $R_{2} R_{3}$ contained in $m_{23}$ correspond to the eigenvectors $\mathbf{n}_{23}$ and $\mathbf{o}_{23}$ of $R_{2} R_{3}$ given by:
$$\mathbf{n}_{23}=\left[\begin{array}{c}
a^{3}+\bar{a}^{3} \\
a^{2} \bar{\tau}-\bar{a} \\
\bar{a}^{2} \tau-a
\end{array}\right], \quad \mathbf{o}_{23}=\left[\begin{array}{c}
0 \\
a \tau \\
1-i
\end{array}\right] .$$
(Note that $\left\langle\mathbf{o}_{23}, \mathbf{o}_{23}\right\rangle<0$ for $p \geq 5$.) One easily checks that the eigenvalues are $\bar{a}^{2}$ and $-i a$ respectively. Hence the rotation angle is $(-4 \pi / 3)-(2 \pi / 3 p-\pi / 2)=(p-4) \pi / 2 p=2 \pi / 2 c$.

For $p \geqslant 8$, the complex line $m_{1 \overline{3} 23}$ and the fixed point $o_{1 \overline{3} 23}$ of $R_{1} R_{3}^{-1} R_{2} R_{3}$ correspond to eigenvectors $\mathbf{n}_{1 \overline{3} 23}$ and $\mathbf{o}_{1 \overline{3} 23}$ given by:
$$\mathbf{n}_{1 \overline{3} 23}=\left[\begin{array}{c}
a^{2}+\bar{a} \bar{\tau} \\
a^{4} \tau+a \\
a^{3}-\bar{a}^{3}-\tau
\end{array}\right], \quad \mathbf{o}_{1 \overline{3} 23}=\left[\begin{array}{c}
-a^{2} \bar{\omega} \\
a \\
\bar{\tau}
\end{array}\right]$$
where $\omega=e^{2 \pi i / 3}$. One easily checks that the eigenvalues are $\bar{a}^{2}$ and $-a \omega$ respectively and so the rotation angle is $(-4 \pi / 3)-(2 \pi / 3 p-\pi / 3)=(p-6) \pi / 3 p=2 \pi / 3 d$. \(\square\)

We now consider the Giraud ridges (see Table 4 for a list of the relevant Giraud intersections, and Section 4.8.4 for the fact that these are indeed ridges of $E$ ).

Lemma 5.4 The images of $E$ tessellate a neighborhood of $r_{1} \cap P^{-1} r_{1}^{-}, r_{1} \cap P^{2} s_{1}$ and $r_{1} \cap s_{1}$. Specifically:
\begin{itemize}
\item[1.] $E, R_{1}^{-1} E$ and $P^{-1} R_{1} E$ cover a neighborhood of the interior of $r_{1} \cap P^{-1} r_{1}^{-}$;
\item[2.] $E, R_{1}^{-1} E$ and $P^{2} S_{1}^{-1} E$ cover a neighborhood of the interior of $r_{1} \cap P^{2} s_{1}$;
\item[3.] $E, R_{1}^{-1} E$ and $S_{1}^{-1} E$ cover a neighborhood of the interior of $r_{1} \cap s_{1}$.
\end{itemize}

Proof. Using Lemma 3.3, this follows from the fact that these three ridges are contained in the Giraud disks given in Table 4. The bounding bisectors defining these Giraud disks are coequidistant from one of $y_{0}, y_{1}$ or $y_{2}$, as indicated in Table 3. These bisectors divide $\mathbf{H}_{\mathbb{C}}^{2}$ into three regions as in Lemma 3.3. We know by Lemma 4.36 that $E$ is contained in the region containing $y_{j}$. By applying the side pairing maps in the ridge cycle we obtain copies of $E$ contained in the other two regions. \(\square\)

This proves that the side pairings of the polyhedron $E$ satisfy the cycle conditions of the Poincaré polyhedron theorem.

\subsection*{5.3 Hypotheses - consistent horoballs}

In order to prove the existence of a consistent system of horoballs (see Corollary 5.6 and Corollary 5.9), we need to study local stabilizers of cusps.

In fact we will determine local stabilizers of all vertices (cusps or not), as well as edges. The techniques are similar to those in Section 18.2 of [Mos80]. The order of these stabilizers will be used when we calculate the orbifold Euler characteristic, see Section 5.5.

Proposition 5.5 When $p=3$ or 4 there is a single-orbit of $p_{*}$-vertices. A representative is $p_{12}$ and its stabilizer is $\left\langle R_{1}, R_{2}\right\rangle$. Moreover, there is a single orbit of $\left(p_{*}, p_{*}\right)$ edges. A representative is $\left(p_{13}, p_{12}\right)$ and its stabilizer is $\left\langle R_{1}\right\rangle$.

PROOF. Since $p_{23}=P^{-2} p_{12}, p_{13}=P^{-1} p_{12}, p_{123 \overline{1}}=P p_{12}$ and $p_{\overline{3} \overline{2} 3123}=P^{3} p_{12}$ it is clear that all $p_{*}$-vertices lie in the same orbit.

The action of the side pairing maps on the $p_{*}$-vertices may be expressed in terms of $p_{12}$ as follows. We can write such a vertex as $p_{a}=P^{i} p_{12}$. The side pairing $R$ maps $p_{a}$ to $p_{b}$ and we can write $p_{b}=P^{j} p_{12}$. This corresponds to an element $P^{j} R P^{-i}$ of the stabilizer of $p_{12}$.

We list the side pairing, the vertex, its image and the corresponding word in the stabilizer of $p_{12}$ in terms of $R_{1}$ and $R_{2}$. Taking the inverse of a side pairing map (resp. conjugating it by a power of $P$ ) gives the inverse word (resp. a conjugate word).

\begin{tabular}[t]{|l|l|l|l|}
\hline & Vertex & Image & Word \\
\hline $R_{1}$ & $p_{12}$ & $p_{12}$ & $R_{1}$ \\
\hline $R_{1}$ & $p_{13}=P^{-1} p_{12}$ & $p_{13}=P^{-1} p_{12}$ & $P R_{1} P^{-1}=R_{1} R_{2} R_{1}^{-1}$ \\
\hline $R_{1}$ & $p_{23}=P^{-2} p_{12}$ & $p_{123 \overline{1}}=P p_{12}$ & $P^{-1} R_{1} P^{-2}=R_{2}^{-1} R_{1}^{-1}$ \\
\hline $S_{1}$ & $p_{23}=P^{-2} p_{12}$ & $p_{\overline{2} \overline{2}_{3123}}=P^{3} p_{12}$ & $P^{-3} S_{1} P^{-2}=R_{2}^{-1}$ \\
\hline $S_{1}$ & $p_{\overline{3} \overline{2} 3123}=P^{3} p_{12}$ & $p_{123 \overline{1}}=P p_{12}$ & $P^{-1} S_{1} P^{3}=R_{2}^{-1} R_{1}^{-1} R_{2}$ \\
\hline
\end{tabular}
To show that the stabilizer of $\left(p_{13}, p_{12}\right)$ is generated by $R_{1}$ we argue in the same way as we did for vertex stabilizers. All edges joining two $p_{*}$-vertices are the images under a power of $P$ of either the edge $\left(p_{13}, p_{12}\right)$ or the edge $\left(p_{12}, p_{23}\right)=R_{1}^{-1} P\left(p_{13}, p_{12}\right)$. We describe each edge $\left(p_{*}, p_{*}\right)$ and its image under the side pairing in this way and so obtain an element of the stabilizer of $\left(p_{13}, p_{12}\right)$. We do this for the three $\left(p_{*}, p_{*}\right)$ edges in $r_{1}$ and the single $\left(p_{*}, p_{*}\right)$ edge in $s_{1}$. The others follow by applying powers of $P$.

\begin{tabular}[t]{|l|l|l|l|}
\hline & Edge & Image & Word \\
\hline $R_{1}$ & $\left(p_{13}, p_{12}\right)$ & $\left(p_{13}, p_{12}\right)$ & $R_{1}$ \\
\hline $R_{1}$ & $\left(p_{12}, p_{23}\right)=R_{1}^{-1} P\left(p_{13}, p_{12}\right)$ & $\left(p_{12}, p_{123 \overline{1}}\right)=P\left(p_{13}, p_{12}\right)$ & id \\
\hline $R_{1}$ & $\left(p_{23}, p_{12}\right)=P^{-1}\left(p_{13}, p_{12}\right)$ & $\left(p_{123 \overline{1}}, p_{13}\right)=P R_{1}^{-1} P\left(p_{13}, p_{12}\right)$ & $R_{1}^{-1}$ \\
\hline $S_{1}$ & $\left(p_{23}, p_{\overline{3} \overline{2} 3123}\right)=P^{-2} R_{1}^{-1} P\left(p_{13}, p_{12}\right)$ & $\left.\left(p_{\overline{3} \overline{2} 3123}, p_{123 \overline{1}}\right)=P^{3} R_{1}^{-1} P\left(p_{13}, p_{12}\right)\right)$ & $R_{1}^{-1}$ \\
\hline
\end{tabular}
In fact no group element interchanges $p_{12}$ and $p_{13}$, and so the stabilizer of the edge $\left(p_{13}, p_{12}\right)$ is the intersection of the vertex stabilizers, namely $\left\langle R_{1}\right\rangle$. \(\square\)

In Proposition 4.3 we found the structure of $\left\langle R_{1}, R_{2}\right\rangle$. In particular, for $p=3$ it is finite. When $p=4$, the point $p_{12}$ lies on $\partial \mathbf{H}_{\mathbb{C}}^{2}$ and we have just verified the conjectural stabilizer given in [DPP11]. Since there is a single orbit of cusps, a consistent system of horoballs comprises a single horoball at $p_{12}$ and all its images under the local stabilizer. Since the local stabilizer of $p_{12}$ is generated by complex reflections, any cycle of side pairing maps or elements of $\Upsilon$ that maps $p_{12}$ to itself also maps any horoball at $p_{12}$ to itself. Thus, we immediately have the following corollary:

Corollary 5.6 When $p=4$, the (local) stabilizer in $\Gamma$ of $p_{12} \in \partial \mathbf{H}_{\mathbb{C}}^{2}$ contains no loxodromic maps. In particular, there is a consistent system of horoballs.

Proposition 5.7 When $p \geqslant 5$ there are two orbits of $p_{*}$-vertices. Representatives are $p_{12}^{1}$ and $p_{13}^{1}$ with stabilizers $\left\langle R_{1},\left(R_{1} R_{2}\right)^{2}\right\rangle$ and $\left\langle R_{1},\left(R_{1} R_{3}\right)^{2}\right\rangle$ respectively. There are two orbits of ( $p_{*}, p_{*}$ ) edges. Representatives are ( $p_{13}^{1}, p_{12}^{1}$ ) and ( $p_{12}^{1}, p_{12}^{2}$ ) with stabilizers $\left\langle R_{1}\right\rangle$ and $\left\langle\left(R_{1} R_{2}\right)^{2}\right\rangle$ respectively.

\begin{table}
\captionsetup{labelformat=empty}
\caption{Proof. The $\Gamma$-orbit of $p_{12}^{1}$ in $E$ comprises $P$-orbits of $p_{12}^{1}$ and $p_{12}^{\overline{2} 12}=R_{2}^{-1} p_{12}^{1}$.}
\begin{tabular}[t]{|l|l|l|l|}
\hline & Vertex & Image & Word \\
\hline $R_{1}$ & $p_{12}^{1}$ & $p_{12}^{1}$ & $R_{1}$ \\
\hline $R_{1}$ & $p_{13}^{3}=P^{-1} p_{12}^{1}$ & $p_{13}^{13 \overline{1}}=P^{-1} R_{2}^{-1} p_{12}^{1}$ & $R_{2} P R_{1} P^{-1}=\left(R_{1} R_{2}\right)^{2} R_{1}^{-2}$ \\
\hline $R_{1}$ & $p_{23}^{2}=P^{-2} R_{2}^{-1} p_{12}^{1}$ & $p_{1231}^{121}=P p_{12}^{1}$ & $P^{-1} R_{1} P^{-2} R_{2}^{-1}=R_{1}\left(R_{1} R_{2}\right)^{-2}$ \\
\hline $R_{1}$ & $p_{23}^{323}=P^{-2} p_{12}^{1}$ & $p_{1231}^{13231}=P R_{2}^{-1} p_{12}^{1}$ & $R_{2} P^{-1} R_{1} P^{-2}=R_{1}^{-1}$ \\
\hline $S_{1}$ & $p_{23}^{323}=P^{-2} p_{12}^{1}$ & $p_{323123}^{232}=P^{3} R_{2}^{-1} p_{12}^{1}$ & $R_{2} P^{-3} S_{1} P^{-2}=i d$ \\
\hline $S_{1}$ & $p_{323123}^{232}=P^{3} R_{2}^{-1} p_{12}^{1}$ & $p_{1231}^{13231}=P R_{2}^{-1} p_{12}^{1}$ & $R_{2} P^{-1} S_{1} P^{3} R_{2}^{-1}=R_{1}^{-1}$ \\
\hline
\end{tabular}
\end{table}
Finding the stabilizer of $p_{13}^{1}$ is done in a similar way.
The orbit and stabilizer of the edge ( $p_{13}^{1}, p_{12}^{1}$ ) follow as before. A similar argument shows that no element of the group interchanges $p_{12}^{1}$ and $p_{12}^{2}$. Therefore the stabilizer of $\left(p_{12}^{1}, p_{12}^{2}\right)$ is the intersection of the vertex stabilizers. \(\square\)

Note that, since the stabilizer of $p_{12}^{1}$ is generated by the commuting complex reflections $R_{1}$ and $\left(R_{1} R_{2}\right)^{3}$, its order is simply $2 p^{2} /(p-4)$ which is the product of the orders of these reflections.

Proposition 5.8 When $p \leqslant 6$ there is a single orbit of $q_{*}$-vertices. A representative is $q_{123 \overline{2}}$ with stabilizer $\left\langle R_{1}, R_{2} R_{3} R_{2}^{-1}\right\rangle$. There is a single orbit of ( $q_{*}, q_{*}$ ) edges. A representative is $\left(q_{1 \overline{3} 23}, q_{123 \overline{2}}\right)$ with stabilizer $\left\langle S_{1}\right\rangle$.

Proof. This is similar to the constructions of the stabilizers of the $p_{*}$-vertices.

\begin{tabular}[t]{|l|l|l|l|}
\hline & Vertex & Image & Word \\
\hline $R_{1}$ & $q_{123 \overline{2}}$ & $q_{123 \overline{2}}$ & $R_{1}$ \\
\hline $R_{1}$ & $q_{1 \overline{3} 23}=P^{-2} q_{123 \overline{2}}$ & $q_{1 \overline{3} 23}=P^{-2} q_{123 \overline{2}}$ & $P^{2} R_{1} P^{-2}=R_{1}\left(R_{2} R_{3} R_{2}^{-1}\right) R_{1}^{-1}$ \\
\hline $S_{1}$ & $q_{123 \overline{2}}$ & $q_{1 \overline{3} 23}=P^{-2} q_{123 \overline{2}}$ & $P^{2} S_{1}=\left(R_{2} R_{3} R_{2}^{-1}\right)^{-1}$ \\
\hline $S_{1}$ & $q_{1 \overline{3} 23}=P^{-2} q_{123 \overline{2}}$ & $q_{123 \overline{2}}$ & $S_{1} P^{-2}=R_{1}\left(R_{2} R_{3} R_{2}^{-1}\right)$ \\
\hline
\end{tabular}
There is one $P$-orbit of $\left(q_{*}, q_{*}\right)$ edges. Since $S_{1}$ interchanges $q_{1 \overline{3} 23}$ and $q_{123 \overline{2}}$ we see that the intersection of the vertex stabilizers, namely $\left\langle R_{1}\right\rangle$, has index two in the stabilizer of the edge $\left(q_{1 \overline{3} 23}, q_{123 \overline{2}}\right)$, which is $\left\langle S_{1}\right\rangle$. This is clear since $R_{1}=S_{1}^{2}$. \(\square\)

When $p \leqslant 5$, the stabilizer of $q_{123 \overline{2}}$ has order $24 p^{2} /(6-p)$ by Proposition 4.6. When $p=6$ the point $q_{123 \overline{2}}$ lies on $\partial \mathbf{H}_{\mathbb{C}}^{2}$. Once again its stabilizer agrees with that conjectured in [DPP11] and we have:

Corollary 5.9 When $p=6$, the (local) stabilizer in $\Gamma$ of $q_{123 \overline{2}} \in \partial \mathbf{H}_{\mathbb{C}}^{2}$ contains no loxodromic maps. In particular, there is a consistent system of horoballs.

A similar argument gives the following result.
Proposition 5.10 When $p=8,12$ there is a single orbit of $q_{*}$-vertices. A representative is $q_{123 \overline{2}}^{1}$ with stabilizer $\left\langle R_{1},\left(R_{1} R_{2} R_{3} R_{2}^{-1}\right)^{3}\right\rangle$. There are two orbits of $\left(q_{*}, q_{*}\right)$ edges. Representatives are $\left(q_{1 \overline{3} 23}^{1}, q_{123 \overline{2}}^{1}\right)$ and $\left(q_{123 \overline{2}}^{1}, q_{123 \overline{2}}^{23 \overline{2}}\right)$ with stabilizers $\left\langle S_{1}\right\rangle$ and $\left\langle R_{1} R_{2} R_{3} R_{2}^{-1} R_{1}\right\rangle$ respectively.

Observe that the stabilizer of $q_{123 \overline{2}}^{1}$ is generated by the commuting complex reflections $R_{1}$ and $\left(R_{1} R_{2} R_{3} R_{2}^{-1}\right)^{3}$. Its order is $2 p^{2} /(p-6)$, the product of the orders of these reflections.

Proposition 5.11 For all values of $p$ there are two orbits of $\left(p_{*}, q_{*}\right)$ edges. Representatives are $\left(p_{12}^{1}, q_{123 \overline{2}}^{1}\right)$ and $\left(p_{13}^{1}, q_{1 \overline{3} 23}^{1}\right)$, both with stabilizer $\left\langle R_{1}\right\rangle$. (For low values of $p$ omit the superscript 1 as appropriate.)

Proof. Since the vertices of such an edge are in different orbits, the stabilizer of an the edge must be the intersection of the vertex stabilizers. The only thing to check is that these two edges are in distinct orbits. This may be checked easily as before. \(\square\)

For completeness, we end this section with a description of the links of ideal vertices, which describe the structure of cusp neighborhoods (see Figure 17). Note that these are compact, so even for $p=4$ and $p=6$, our polyhedron $E$ has finite volume (see Section 3.2).

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/31f0f35c-0604-47ef-a2ef-a49ed021037c-67.jpg?height=537&width=1134&top_left_y=1049&top_left_x=479}
\captionsetup{labelformat=empty}
\caption{Figure 17: Combinatorics of the links of ideal vertices.}
\end{figure}

\subsection*{5.4 Conclusion - presentation for $\Gamma$}

In Section 5.2 we verified that images of $E$ under the cosets of $\Upsilon$ in $\Gamma$ satisfied the local tessellation hypotheses of the Poincaré polyhedron theorem. In Corollaries 5.6 and 5.9 above, we showed that when $p=4$ and $p=6$ there are consistent horoballs at the cusps. Note that $E$ has no cusps for the other values of $p$. Thus we have verified the hypotheses of the Poincaré polyhedron theorem. Hence we have proved that $\Gamma$ is discrete and $E$ is a fundamental polyhedron for the cosets of $\Upsilon$ in $\Gamma$.

We may read off a presentation for $\Gamma$ directly from the Poincaré polyhedron theorem; compare Section 20 of [Mos80]. The generators of $\Gamma$ are the side pairing maps $R_{1}$ and $S_{1}$ of $E$ together with the generator $P$ of $\Upsilon$. The relations come from the cycle transformations associated to the ridges and the relation from $\Upsilon$ (there are no reflection relations in this case). For all values of $p$ we obtain the cycle transformations from Table 7:
$$i d=R_{1}^{p}=\left(P^{-1} R_{1}\right)^{3}=P^{2} S_{1}^{-1} P^{2} R_{1} P^{-2} R_{1}=S_{1}^{-2} R_{1}=\left(P^{2} S_{1}\right)^{p} .$$
In addition, for $p=5,6,8$ and 12, from Table 8, we obtain $i d=\left(P^{-3} R_{1}\right)^{4 p /(p-4)}$ and for $p=8$, 12 we obtain $i d=\left(P^{-2} S_{1}\right)^{6 p /(p-6)}$. Finally, we obtain the relation $i d=P^{7}$ from the
stabilizer of $\langle P\rangle$ of $E$. Thus, the Poincaré theorem gives the presentation:
$$\left\langle R_{1}, S_{1}, P \left\lvert\, \begin{array}{c}
i d=R_{1}^{p}=P^{7}=\left(P^{-1} R_{1}\right)^{3}=P^{2} S_{1}^{-1} P^{2} R_{1} P^{-2} R_{1} \\
i d=S_{1}^{-2} R_{1}=\left(P^{2} S_{1}\right)^{p}=\left(P^{-3} R_{1}\right)^{4 p /(p-4)}=\left(P^{-2} S_{1}\right)^{6 p /(p-6)}
\end{array}\right.\right\rangle$$
where we omit the last two relations when the exponent is infinite or negative. Note that for the values of $p$ where these exponents are negative the two relations still hold and follow from the other relations (compare Corollary 5.6 of [Par06] and Section 2.2 of [Mos80]).

We now simplify the relations and change generators in order to recover the presentation of Theorem 1.2. In particular, we recover the relations found in Section 4.3 only using the cycle relations.

The relation $i d=P^{2} S_{1}^{-1} P^{2} R_{1} P^{-2} R_{1}$ clearly implies that $S_{1}=P^{2} R_{1} P^{-2} R_{1} P^{2}$; see (10). Also, Proposition 4.4 implies that $P^{2} S_{1}$ is conjugate to $R_{1}^{-1}$. Hence the relation $i d=\left(P^{2} S_{1}\right)^{p}$ is equivalent to $i d=R_{1}^{p}$, and so may be omitted. We now show that the relation $S_{1}^{2}=R_{1}$, which also implies $S_{1} R_{1}=R_{1} S_{1}$, recovers both the generalized braid relation $\left(R_{1} R_{2}\right)^{2}=$ $\left(R_{2} R_{1}\right)^{2}$ and the braid relation $R_{1}\left(R_{2} R_{3} R_{2}^{-1}\right) R_{1}=\left(R_{2} R_{3} R_{2}^{-1}\right) R_{1}\left(R_{2} R_{3} R_{2}^{-1}\right)$, which were discussed in Section 4.3.

Lemma 5.12 Assume that $P$ has order 7 and that $J=P^{-1} R_{1}$ has order 3. Suppose that $S_{1}, R_{2}$ and $R_{3}$ are defined by
$$S_{1}=P^{2} R_{1} P^{-2} R_{1} P^{2}, \quad R_{2}=J R_{1} J^{-1}=R_{1}^{-1} P R_{1} P^{-1} R_{1}, \quad R_{3}=J^{-1} R_{1} J=P^{-1} R_{1} P .$$
Then, the relation $S_{1}^{2}=R_{1}$ is equivalent to $\left(R_{1} R_{2}\right)^{2}=\left(R_{2} R_{1}\right)^{2}$. Also, the relation $S_{1} R_{1}=$ $R_{1} S_{1}$ is equivalent to $R_{1}\left(R_{2} R_{3} R_{2}^{-1}\right) R_{1}=\left(R_{2} R_{3} R_{2}^{-1}\right) R_{1}\left(R_{2} R_{3} R_{2}^{-1}\right)$.

Proof. Using $P^{4}=P^{-3}, R_{1} P^{-1} R_{1}=P R_{1}^{-1} P$ and $P R_{1} P^{-1}=R_{1} R_{2} R_{1}^{-1}$, we have:
$$\begin{aligned}
S_{1}^{2} R_{1}^{-1} & =P^{2} R_{1} P^{-1}\left(P^{-1} R_{1} P^{-1}\right) P^{-1}\left(P^{-1} R_{1} P^{-1}\right) P^{-1} R_{1} P\left(P R_{1}^{-1}\right) \\
& =P\left(P R_{1} P^{-1}\right)\left(R_{1}^{-1} P R_{1}^{-1} P^{-1}\right)\left(R_{1}^{-1} P R_{1}^{-1} P^{-1}\right) R_{1}\left(P R_{1} P^{-1}\right) R_{1} P^{-1} \\
& =P\left(R_{1} R_{2}\left(R_{2} R_{1}\right)^{-2} R_{1} R_{2}\right) P^{-1} .
\end{aligned}$$
Secondly, one easily checks $R_{2} R_{3} R_{2}^{-1}=R_{1}^{-1} P^{2} R_{1} P^{-2} R_{1}$. Therefore
$$\begin{aligned}
S_{1} R_{1}^{-1} S_{1}^{-1} R_{1} & =P^{2} R_{1} P^{-2} R_{1} P^{2} R_{1}^{-1} P^{-2} R_{1}^{-1} P^{2} R_{1}^{-1} P^{-2} R_{1} \\
& =R_{1}\left(R_{2} R_{3} R_{2}^{-1}\right) R_{1}\left(R_{2} R_{3}^{-1} R_{2}^{-1}\right) R_{1}^{-1}\left(R_{2} R_{3}^{-1} R_{2}^{-1}\right) .
\end{aligned}$$ \(\square\)

Substituting for $P^{-1} R_{1}=J, R_{2}=J R_{1} J^{-1}=R_{1}^{-1} P R_{1} P^{-1} R_{1}$ and $R_{3}=P^{-1} R_{1} P=$ $J^{-1} R_{1} J$, we obtain the presentation given in Theorem 1.2, which agrees with the conjectural presentation given in [DPP11].

\subsection*{5.5 Conclusion - orbifold Euler characteristics}

In this section we prove Theorem 1.3 which gives the orbifold Euler characteristic of the quotient of $\mathbf{H}_{\mathbb{C}}^{2}$ by $\Gamma$. We write $\chi\left(2 \pi / p, \bar{\sigma}_{4}\right)$ for the Euler characteristic $\chi\left(\Gamma\left(2 \pi / p, \bar{\sigma}_{4}\right) \backslash \mathbf{H}_{\mathbb{C}}^{2}\right)$ where $\tau=\bar{\sigma}_{4}=-(1+i \sqrt{7}) / 2$.

\begin{table}
\begin{tabular}[t]{|l|l|l|l|}
\hline & Facet & Stabilizer & Order \\
\hline \multirow[t]{2}{*}{Vertices} & $p_{12}$ & $\left\langle R_{1}, R_{2}\right\rangle$ & $8 p^{2} /(4-p)^{2}$ \\
\hline & $q_{123 \overline{2}}$ & $\left\langle R_{1}, R_{2} R_{3} R_{2}^{-1}\right\rangle$ & $24 p^{2} /(6-p)^{2}$ \\
\hline \multirow[t]{4}{*}{Edges} & ( $p_{12}, p_{13}$ ) & $\left\langle R_{1}\right\rangle$ & $p$ \\
\hline & $\left(p_{12}, q_{231 \overline{2}}\right)$ & $\left\langle R_{1}\right\rangle$ & $p$ \\
\hline & $\left(p_{13}, q_{1 \overline{3} 23}\right)$ & $\left\langle R_{1}\right\rangle$ & $p$ \\
\hline & $\left(q_{123 \overline{2}}, q_{1 \overline{3} 23}\right)$ & $\left\langle S_{1}\right\rangle$ & $2 p$ \\
\hline \multirow[t]{5}{*}{Ridges} & $r_{1} \cap r_{1}^{-}$ & $\left\langle R_{1}\right\rangle$ & $p$ \\
\hline & $r_{1} \cap P^{-1} r_{1}^{-}$ & $\left\langle P^{-1} R_{1}\right\rangle$ & 3 \\
\hline & $r_{1} \cap P^{2} s_{1}$ & id & 1 \\
\hline & $r_{1} \cap s_{1}$ & id & 1 \\
\hline & $s_{1} \cap P^{2} s_{1}^{-}$ & $\left\langle R_{2} R_{3} R_{2}^{-1}\right\rangle$ & $p$ \\
\hline \multirow[t]{2}{*}{Sides} & $r_{1}$ & id & 1 \\
\hline & $s_{1}$ & id & 1 \\
\hline Polyhedron & $E$ & $\langle P\rangle$ & 7 \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 9: The Euler characteristic calculation for $p=3,4$.}
\end{table}

We begin by calculating the orbifold Euler characteristic when $p=3$ and $p=4$. We choose one representative from each $\Gamma$-orbit of facets and give its stabilizer. The stabilizers of vertices and edges, and their orders, were found in Section 5.3. The orders of some vertex stabilizers had also been given in Section 4.3. The ridge cycles described in Section 5.2 give the stabilizers of the ridges. A representative of each orbit of facets and its stabilizer, together with the order of the stabilizer, is given in Table 9. Using these values, the orbifold Euler characteristic is
$$\begin{aligned}
\chi\left(2 \pi / p, \bar{\sigma}_{4}\right) & =\left(\frac{(4-p)^{2}}{8 p^{2}}+\frac{(6-p)^{2}}{24 p^{2}}\right)-\left(\frac{3}{p}+\frac{1}{2 p}\right)+\left(\frac{2}{p}+\frac{1}{3}+2\right)-2+\frac{1}{7} \\
& =\frac{49-42 p+9 p^{2}}{14 p^{2}}
\end{aligned}$$
Putting in $p=3$ and $p=4$ we obtain $\chi\left(2 \pi / 3, \bar{\sigma}_{4}\right)=2 / 63$ and $\chi\left(2 \pi / 4, \bar{\sigma}_{4}\right)=25 / 224$.
We now do the same thing for $p=5$ and $p=6$. The main difference is that the vertex $p_{12}$ has become a complex ridge and we introduce several more vertices. The facets, stabilizers and orders in Table 10 imply that the orbifold Euler characteristic is
$$\begin{aligned}
\chi\left(2 \pi / p, \bar{\sigma}_{4}\right)= & \left(\frac{2(p-4)}{2 p^{2}}+\frac{(6-p)^{2}}{24 p^{2}}\right)-\left(\frac{3}{p}+\frac{p-4}{2 p}+\frac{1}{2 p}\right) \\
& +\left(\frac{2}{p}+\frac{1}{3}+2+\frac{p-4}{4 p}\right)-2+\frac{1}{7} \\
= & \frac{15 p^{2}-140}{56 p^{2}} .
\end{aligned}$$
Putting in $p=5$ and $p=6$ we obtain $\chi\left(2 \pi / 5, \bar{\sigma}_{4}\right)=47 / 280$ and $\chi\left(2 \pi / 6, \bar{\sigma}_{4}\right)=25 / 126$.
Finally, we consider the cases $p=8$ and $p=12$. The facets, stabilizers and orders are given in Table 11, and show that the orbifold Euler characteristic is

\begin{table}
\begin{tabular}[t]{|l|l|l|l|}
\hline & Facet & Stabilizer & Order \\
\hline \multirow[t]{3}{*}{Vertices} & $p_{12}^{1}$ & $\left\langle R_{1},\left(R_{1} R_{2}\right)^{2}\right\rangle$ & $2 p^{2} /(p-4)$ \\
\hline & $p_{13}^{1}$ & $\left\langle R_{1},\left(R_{1} R_{3}\right)^{2}\right\rangle$ & $2 p^{2} /(p-4)$ \\
\hline & $q_{123 \overline{1}}$ & $\left\langle R_{1}, R_{2} R_{3} R_{2}^{-1}\right\rangle$ & $24 p^{2} /(6-p)^{2}$ \\
\hline \multirow[t]{5}{*}{Edges} & ( $p_{12}^{1}, p_{13}^{1}$ ) & $\left\langle R_{1}\right\rangle$ & $p$ \\
\hline & ( $p_{12}^{1}, p_{12}^{2}$ ) & $\left\langle\left(R_{1} R_{2}\right)^{2}\right\rangle$ & $2 p /(p-4)$ \\
\hline & $\left(p_{12}^{1}, q_{123 \overline{2}}\right)$ & $\left\langle R_{1}\right\rangle$ & $p$ \\
\hline & $\left(p_{13}^{1}, q_{1 \overline{3} 23}\right)$ & $\left\langle R_{1}\right\rangle$ & $p$ \\
\hline & $\left(q_{123 \overline{2}}, q_{1 \overline{3} 23}\right)$ & $\left\langle S_{1}\right\rangle$ & $2 p$ \\
\hline \multirow[t]{6}{*}{Ridges} & $r_{1} \cap r_{1}^{-}$ & $\left\langle R_{1}\right\rangle$ & $p$ \\
\hline & $r_{1} \cap P^{-1} r_{1}^{-}$ & $\left\langle P^{-1} R_{1}\right\rangle$ & 3 \\
\hline & $r_{1} \cap P^{2} s_{1}$ & id & 1 \\
\hline & $r_{1} \cap s_{1}$ & id & 1 \\
\hline & $s_{1} \cap P^{2} s_{1}^{-}$ & $\left\langle R_{2} R_{3} R_{2}^{-1}\right\rangle$ & $p$ \\
\hline & $r_{1} \cap P^{-3} r_{1}^{-}$ & $\left\langle R_{2} R_{3}\right\rangle$ & $4 p /(p-4)$ \\
\hline \multirow[t]{2}{*}{Sides} & $r_{1}$ & id & 1 \\
\hline & $s_{1}$ & id & 1 \\
\hline Polyhedron & $E$ & $\langle P\rangle$ & 7 \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 10: The Euler characteristic calculation for $p=5,6$.}
\end{table}

\begin{table}
\begin{tabular}[t]{|l|l|l|l|}
\hline & Orbit & Stabilizer & Order \\
\hline \multirow[t]{3}{*}{Vertices} & $p_{12}^{1}$ & $\left\langle R_{1},\left(R_{1} R_{2}\right)^{2}\right\rangle$ & $2 p^{2} /(p-4)$ \\
\hline & $p_{13}^{1}$ & $\left\langle R_{1},\left(R_{1} R_{3}\right)^{2}\right\rangle$ & $2 p^{2} /(p-4)$ \\
\hline & $q_{123 \overline{2}}^{1}$ & $\left\langle R_{1},\left(R_{1} R_{2} R_{3} R_{2}^{-1}\right)^{3}\right\rangle$ & $2 p^{2} /(p-6)$ \\
\hline \multirow[t]{6}{*}{Edges} & ( $p_{12}^{1}, p_{13}^{1}$ ) & $\left\langle R_{1}\right\rangle$ & $p$ \\
\hline & ( $p_{12}^{1}, p_{12}^{2}$ ) & $\left\langle\left(R_{1} R_{2}\right)^{2}\right\rangle$ & $2 p /(p-4)$ \\
\hline & ( $p_{12}^{1}, q_{123 \overline{2}}^{1}$ ) & $\left\langle R_{1}\right\rangle$ & $p$ \\
\hline & ( $p_{13}^{1}, q_{1 \overline{3} 23}^{1}$ ) & $\left\langle R_{1}\right\rangle$ & $p$ \\
\hline & $\left(q_{123 \overline{2}}^{1}, q_{1 \overline{3} 23}^{1}\right)$ & $\left\langle S_{1}\right\rangle$ & $2 p$ \\
\hline & $\left(q_{123 \overline{2}}^{1}, q_{123 \overline{2}}^{232}\right)$ & $\left\langle R_{1} R_{2} R_{3} R_{2}^{-1} R_{1}\right\rangle$ & $4 p /(p-6)$ \\
\hline \multirow[t]{7}{*}{Ridges} & $r_{1} \cap r_{1}^{-}$ & $\left\langle R_{1}\right\rangle$ & $p$ \\
\hline & $r_{1} \cap P^{-1} r_{1}^{-}$ & $\left\langle P^{-1} R_{1}\right\rangle$ & 3 \\
\hline & $r_{1} \cap P^{2} s_{1}$ & id & 1 \\
\hline & $r_{1} \cap s_{1}$ & $i d$ & 1 \\
\hline & $s_{1} \cap P^{2} s_{1}^{-}$ & $\left\langle R_{2} R_{3} R_{2}^{-1}\right\rangle$ & $p$ \\
\hline & $r_{1} \cap P^{-3} r_{1}^{-}$ & $\left\langle R_{2} R_{3}\right\rangle$ & $4 p /(p-4)$ \\
\hline & $s_{1} \cap P^{-2} s_{1}^{-}$ & $\left\langle R_{1} R_{3}^{-1} R_{2} R_{3}\right\rangle$ & $6 p /(p-6)$ \\
\hline \multirow[t]{2}{*}{Sides} & $r_{1}$ & $i d$ & 1 \\
\hline & $s_{1}$ & $i d$ & 1 \\
\hline Polyhedron & $E$ & $\langle P\rangle$ & 7 \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 11: The Euler characteristic calculation for $p=8,12$.}
\end{table}
$$\begin{aligned}
\chi\left(2 \pi / p, \bar{\sigma}_{4}\right)= & \left(\frac{2(p-4)}{2 p^{2}}+\frac{(6-p)^{2}}{24 p^{2}}\right)-\left(\frac{3}{p}+\frac{p-4}{2 p}+\frac{1}{2 p}+\frac{p-6}{4 p}\right) \\
& +\left(\frac{2}{p}+\frac{1}{3}+2+\frac{p-4}{4 p}+\frac{p-6}{6 p}\right)-2+\frac{1}{7} \\
= & \frac{-98+21 p+2 p^{2}}{14 p^{2}} .
\end{aligned}$$
Putting in $p=8$ and $p=12$ gives $\chi\left(2 \pi / 8, \bar{\sigma}_{4}\right)=99 / 448$ and $\chi\left(2 \pi / 12, \bar{\sigma}_{4}\right)=221 / 1008$.

\section*{6 Arithmeticity and Galois theory}

\subsection*{6.1 Trace fields and commensurability}

Recall from [PP09] that we can adjust the generators $R_{1}, J$ and the Hermitian form $H$ so that their entries lie in
$$\mathbb{L}=\mathbb{Q}\left(\tau, e^{2 \pi i / p}\right) .$$
Note that after making this adjustment, $R_{1}$ no longer has unit determinant.
In this section, we consider the adjoint trace field $k=\mathbb{Q}(\operatorname{tr} \operatorname{Ad} \Gamma)$ for the relevant sporadic triangle groups, i.e. the ones with $\tau=\bar{\sigma}_{4}=-(1+i \sqrt{7}) / 2$, and $p=3,4,5,6,8$ or 12. Recall from [DM86], [Mos80] and [Pau10] that:

Lemma 6.1 The field $\mathbb{Q}(\operatorname{tr} \operatorname{Ad} \Gamma)$ is a commensurability invariant of subgroups $\Gamma<\mathrm{U}(n, 1)$, where $\operatorname{tr} \operatorname{Ad}(\gamma)=|\operatorname{tr}(\gamma)|^{2}$ for $\gamma \in \mathrm{U}(n, 1)$.

Since we have arranged for $R_{1}$ and $J$ (as well as the matrix of the Hermitian form $H$ ) to have entries in $\mathbb{L}=\mathbb{Q}\left(\tau, e^{2 \pi i / p}\right)$, the adjoint trace field is contained in $\mathbb{R} \cap \mathbb{Q}\left(\tau, e^{2 \pi i / p}\right)$.

In fact it is easy to see by computing the trace of a handful of group elements that $k$ contains $\mathbb{Q}\left(\cos \frac{2 \pi}{p}, \sqrt{7} \sin \frac{2 \pi}{p}\right)$. Note that the adjustment indicated above changes the trace of elements of $\Gamma$, but the absolute values of these traces remain the same. In fact the following two traces suffice:
$$\begin{aligned}
\left|\operatorname{tr}\left(R_{1}\right)\right|^{2} & =\left|e^{4 i \pi / 3 p}+2 e^{-2 i \pi / 3 p}\right|^{2} \\
& =5+4 \cos (2 \pi / p), \\
\left|\operatorname{tr}\left(J R_{1} J R_{1}^{-1}\right)\right|^{2} & =\left|e^{-2 \pi i / 3 p}-\bar{\tau} e^{4 i \pi / 3 p}\right|^{2} \\
& =3-2 \Re\left(\tau e^{2 \pi i / p}\right) \\
& =3+\cos (2 \pi / p)+\sqrt{7} \sin (2 \pi / p) .
\end{aligned}$$

Now clearly we can go from $k$ to $\mathbb{L}$ simply by adjoining $\sqrt{-7}$, so $\mathbb{L}$ has degree 2 over $k$. This shows that $k$ is equal to $\mathbb{R} \cap \mathbb{L}$, and
$$k=\mathbb{Q}(\cos (2 \pi / p), \sqrt{7} \sin (2 \pi / p)) .$$
More specifically, for the relevant values of $p$, we find the fields given in Table 12. This shows that the corresponding six lattices are in different commensurability classes; indeed there is only one pair having the same adjoint trace field, but $\Gamma\left(2 \pi / 3, \bar{\sigma}_{4}\right)$ is cocompact whereas $\Gamma\left(2 \pi / 6, \bar{\sigma}_{4}\right)$ is not. For completeness, we also recall the following result from [Pau10].

\begin{table}
\begin{tabular}[t]{|l|l|l|}
\hline $p$ & $k$ & Degree \\
\hline 3 & $\mathbb{Q}(\sqrt{21})$ & 2 \\
\hline 4 & $\mathbb{Q}(\sqrt{7})$ & 2 \\
\hline 5 & $\mathbb{Q}(\sqrt{14} \sqrt{5+\sqrt{5}})$ & 4 \\
\hline 6 & $\mathbb{Q}(\sqrt{21})$ & 2 \\
\hline 8 & $\mathbb{Q}(\sqrt{2}, \sqrt{7})$ & 4 \\
\hline 12 & $\mathbb{Q}(\sqrt{3}, \sqrt{7})$ & 4 \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 12: The list of the adjoint trace fields of the lattices $\Gamma\left(2 \pi / p, \bar{\sigma}_{4}\right)$ shows that these 6 lattices lie in different commensurability classes.}
\end{table}

Theorem 6.2 None of the six lattices $\Gamma\left(2 \pi / p, \bar{\sigma}_{4}\right)$ is commensurable to any Deligne-Mostow lattice.

Indeed, the adjoint trace fields of the lattices in [DM86] are all of the form $\mathbb{R} \cap \mathbb{Q}\left(\zeta_{n}\right)=$ $\mathbb{Q}\left(\cos \frac{2 \pi}{n}\right)$, and only certain values of $n$ actually appear in that list. More specifically, each Deligne-Mostow group in PU(2, 1) is described by a 5-tuple of rational numbers, and $n$ is simply the least common denominator of these rational numbers (see [DM86], Section 12). Note that if $n=2 k$ where $k$ is odd, then $\mathbb{Q}\left(\zeta_{n}\right)=\mathbb{Q}\left(\zeta_{k}\right)$.

Given the degrees that appear in Table 12, it is enough to check the cyclotomic fields of degree 4 or 8. The relevant values of $n$ are listed in Table 13. Since all groups except the one with $p=3$ are non-arithmetic, we only look at the non-arithmetic Deligne-Mostow groups in PU(2, 1). We list the corresponding adjoint trace fields in Table 13. This proves Theorem 6.2.

\begin{table}
\begin{tabular}[t]{|l|l|l|}
\hline $n$ & $\mathbb{Q}\left(\zeta_{n}\right) \cap \mathbb{R}$ & Degree \\
\hline 5 or 10 & $\mathbb{Q}(\sqrt{5})$ & 2 \\
\hline 8 & $\mathbb{Q}(\sqrt{2})$ & 2 \\
\hline 12 & $\mathbb{Q}(\sqrt{3})$ & 2 \\
\hline 15 or 30 & $\mathbb{Q}\left(\sqrt{3} \sqrt{\frac{5+\sqrt{5}}{2}}\right)$ & 4 \\
\hline 16 & $\mathbb{Q}(\sqrt{2+\sqrt{2}})$ & 4 \\
\hline 20 & $\mathbb{Q}\left(\sqrt{\frac{5+\sqrt{5}}{2}}\right)$ & 4 \\
\hline 24 & $\mathbb{Q}(\sqrt{2}, \sqrt{3})$ & 4 \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 13: The list of cyclotomic fields whose totally real field has degree 2 or 4.}
\end{table}

\subsection*{6.2 Arithmeticity}

In this section we apply the Mostow-Vinberg arithmeticity criterion (Proposition 3.1) to study arithmeticity. The result (Proposition 6.4) follows from Theorem 4.1 of [Pau10], but for completeness we provide details for this special case. In the coordinates used in the
previous section $H$ is the following
$$H=\left[\begin{array}{lll}
\alpha & \beta & \gamma \\
\bar{\beta} & \alpha & \beta \\
\bar{\gamma} & \bar{\beta} & \alpha
\end{array}\right]$$
where $\alpha=2-e^{2 \pi i / p}-e^{-2 \pi i / p}, \beta=\left(e^{-2 \pi i / p}-1\right) \tau$ and $\gamma=\left(1-e^{-2 \pi i / p}\right) \bar{\tau}$. In particular, all entries of $H$ lie in $\mathbb{L}=\mathbb{Q}\left(\tau, e^{2 \pi i / p}\right)$. Observe also that $\tau=\bar{\zeta}_{7}+\bar{\zeta}_{7}^{2}+\bar{\zeta}_{7}^{4}$ for $\zeta_{7}=e^{2 \pi i / 7}$, so that $\mathbb{L} \subset \mathbb{Q}\left(\zeta_{7}, \zeta_{p}\right)=\mathbb{Q}\left(\zeta_{7 p}\right)$, where the last equality follows from the fact that 7 is coprime to $p$.

Let $k \in \mathbb{N}$. By the Chinese remainder theorem, there exists $l \in \mathbb{N}$ such that $l \equiv 1(\bmod 7)$ and $l \equiv k(\bmod p)$. In particular, if $k$ is coprime to $p, \zeta_{7 p} \mapsto \zeta_{7 p}^{l}$ induces an automorphism of $\mathbb{Q}\left(\zeta_{7 p}\right)$ which fixes $\zeta_{7}$ and sends $\zeta_{p}$ to $\zeta_{p}^{k}$; hence $\mathbb{L}=\mathbb{Q}\left(\tau, e^{2 \pi i / p}\right)$ has an automorphism fixing $\tau$ and sending $\zeta_{p}$ to $\zeta_{p}^{k}$. Similarly, there is an automorphism of $\mathbb{L}$ fixing $\zeta_{p}$ and sending $\tau$ to $\bar{\tau}$.

Note that all these automorphisms clearly commute with complex conjugation, so that for any $\sigma \in \operatorname{Gal}(\mathbb{L} / \mathbb{Q}), H^{\sigma}$ is a Hermitian form. Although $H$ has signature (2,1), its Galois conjugates $H^{\sigma}$ may have various signatures for different $\sigma$ 's. With the current notation, Proposition 3.1 translates into the following.

Proposition 6.3 The lattice $\Gamma(2 \pi / p, \tau)$ is arithmetic if and only if for any $\sigma \in \operatorname{Gal}(\mathbb{L} / \mathbb{Q})$ not inducing the identity on $k=\mathbb{R} \cap \mathbb{L}$, the form $H^{\sigma}$ is definite.

Since the diagonal elements of $H^{\sigma}$ are all positive, it is indefinite (i.e it has signature $(1,2)$ or $(2,1))$ precisely when $\operatorname{det}\left(H^{\sigma}\right)<0$. We list values of $\operatorname{det}(H)$ and all $\sigma$ with $\operatorname{det}\left(H^{\sigma}\right)<0$ in Table 14 (for $p=5$ there are two non-trivial Galois automorphisms for which $\operatorname{det}\left(H^{\sigma}\right)<0$, we list both of them). It is quite clear from Table 12 that these automorphisms act non-trivially on the adjoint trace field $k$.

\begin{table}
\begin{tabular}[t]{|l|l|l|l|l|}
\hline $p$ & $\tau^{\sigma}, \zeta_{p}^{\sigma}$ & $\Gamma^{\sigma}$ & $\operatorname{det}(H)$ & $\operatorname{det}\left(H^{\sigma}\right)$ \\
\hline 3 & & & $-\frac{1}{2}(9+3 \sqrt{21})$ & \\
\hline 4 & $\bar{\tau}, \zeta_{4}$ & $\Gamma\left(2 \pi / 4, \sigma_{4}\right)$ & $-6-2 \sqrt{7}$ & $-6+2 \sqrt{7}$ \\
\hline 5 & $\bar{\tau}, \zeta_{5}$ & $\Gamma\left(2 \pi / 5, \sigma_{4}\right)$ & $-\frac{\sqrt{5}}{4}(5+\sqrt{5}+\sqrt{14} \sqrt{5-\sqrt{5}})$ & $-\frac{\sqrt{5}}{4}(5+\sqrt{5}-\sqrt{14} \sqrt{5-\sqrt{5}})$ \\
\hline & $\tau, \zeta_{5}^{2}$ & $\Gamma\left(4 \pi / 5, \bar{\sigma}_{4}\right)$ & & $\frac{\sqrt{5}}{4}(5-\sqrt{5}+\sqrt{14} \sqrt{5+\sqrt{5}})$ \\
\hline 6 & $\bar{\tau}, \zeta_{6}$ & $\Gamma\left(2 \pi / 6, \sigma_{4}\right)$ & $-\frac{1}{2}(5+\sqrt{21})$ & $-\frac{1}{2}(5-\sqrt{21})$ \\
\hline 8 & $\tau, \zeta_{8}^{3}$ & $\Gamma\left(6 \pi / 8, \bar{\sigma}_{4}\right)$ & $-1+\sqrt{7}-\sqrt{14}$ & $-1-\sqrt{7}-\sqrt{14}$ \\
\hline 12 & $\tau, \zeta_{12}^{5}$ & $\Gamma\left(10 \pi / 12, \bar{\sigma}_{4}\right)$ & $\frac{3}{2}-\sqrt{3}-\sqrt{7}+\frac{1}{2} \sqrt{21}$ & $\frac{3}{2}+\sqrt{3}-\sqrt{7}-\frac{1}{2} \sqrt{21}$ \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 14: Computation of $\operatorname{det}(H)$ for various values of $p ;$ when there is one, we list an automorphism $\sigma$ such that $H^{\sigma}$ is indefinite.}
\end{table}

Proposition 6.4 Consider the groups $\Gamma\left(2 \pi / p, \bar{\sigma}_{4}\right), p=3,4,5,6,8$ and 12. Then $\Gamma\left(2 \pi / p, \bar{\sigma}_{4}\right)$ is arithmetic if and only if $p=3$.

\section*{7 Appendix: combinatorial data}

In this section we gather together the data about the facets of $E$ and their orbits under $P$.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/31f0f35c-0604-47ef-a2ef-a49ed021037c-74.jpg?height=265&width=1089&top_left_y=546&top_left_x=501}
\captionsetup{labelformat=empty}
\caption{Table 15: $P$-orbits of mirrors of $R_{1}$ and $R_{2}$.}
\end{figure}

Suppose that $u$ and $v$ are words so that $u v$ is conjugate to 12 . If the mirrors of $m_{u}$ and $m_{v}$ intersect in $\overline{\mathbf{H}}_{\mathbb{C}}^{2}$ then their intersection point is denoted $p_{w}$. The relationship between $u$, $v$ and $w$ is slightly subtle. The easiest situation is when $u v=w$, such as $m_{1} \cap m_{2}=p_{12}$. However, any mirror in the group generated by $u$ and $v$ also passes through this point. So, for example, $m_{1} \cap m_{12 \overline{1}}=m_{12 \overline{1}} \cap m_{\overline{2} 12}=p_{12}$.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/31f0f35c-0604-47ef-a2ef-a49ed021037c-74.jpg?height=126&width=1033&top_left_y=1198&top_left_x=531}
\captionsetup{labelformat=empty}
\caption{Table 16: $P$-orbits of $p_{*}$ vertices, for $p=3$ or 4.}
\end{figure}

If $m_{u}$ and $m_{v}$ are ultraparallel then we denote their common perpendicular by $m_{w}$ where $u, v$ and $w$ are related as above. In this case the $P$-orbit of $m_{w}$ may be found using the same subscripts as appear in the $P$-orbit of $p_{w}$ in the Table 16. In this case, $m_{u}$ and $m_{w}$ intersect in $p_{w}^{u}$. The $P$-orbits of these points are given in Table 17.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/31f0f35c-0604-47ef-a2ef-a49ed021037c-74.jpg?height=521&width=1095&top_left_y=1661&top_left_x=499}
\captionsetup{labelformat=empty}
\caption{Table 17: For $p=5$ or 6, there are four $P$-orbits of $p_{*}$ vertices.}
\end{figure}

Similarly, suppose $u$ and $v$ are words in $\Gamma$ so that $u v$ is conjugate to $123 \overline{2}$. If $m_{u}$ and $m_{v}$ intersect in $\overline{\mathbf{H}}_{\mathbb{C}}^{2}$ then we denote their intersection point by $q_{w}$, where $u, v$ and $w$ where $w$ is conjugate in the group generated by $u$ and $v$ to $u v$. These vertices are listed in Table 18.

If $m_{u}$ and $m_{v}$ are ultraparallel then we denote their common perpendicular by $m_{w}$, where $u, v, w$ are related as before. The intersection point of $m_{u}$ and $m_{w}$ is denoted $q_{w}^{u}$; see Table 19.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/31f0f35c-0604-47ef-a2ef-a49ed021037c-75.jpg?height=130&width=1082&top_left_y=372&top_left_x=507}
\captionsetup{labelformat=empty}
\caption{Table 18: $P$-orbits of $q_{*}$ vertices, for $3 \leqslant p \leqslant 6$.}
\end{figure}

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/31f0f35c-0604-47ef-a2ef-a49ed021037c-75.jpg?height=395&width=1127&top_left_y=604&top_left_x=482}
\captionsetup{labelformat=empty}
\caption{Table 19: For $p=8$ or 12, there are three $P$-orbits of $q_{*}$ vertices.}
\end{figure}

\section*{References}
\begin{itemize}
\item[] [ACT02] D. Allcock, J. A. Carlson, and D. Toledo. The complex hyperbolic geometry of the moduli space of cubic surfaces. J. Algebraic Geom., 11(4):659-724, 2002.
\item[] [BHH87] G. Barthel, F. Hirzebruch, and T. Höfer. Geradenkonfigurationen und Algebraische Flächen. Aspects of Mathematics, D4. Friedr. Vieweg \& Sohn, Braunschweig, 1987.
\item[] [CJ76] J. H. Conway and A. J. Jones. Trigonometric diophantine equations (on vanishing sums of roots of unity). Acta. Arithmetica, 30:229-240, 1976.
\item[] [Coh93] H. Cohen. A course in computational algebraic number theory, volume 138 of Graduate Texts in Mathematics. Springer-Verlag, Berlin, 1993.
\item[] [Cor92] K. Corlette. Archimedean superrigidity and hyperbolic geometry. Ann. of Math. (2), 135(1):165-182, 1992.
\item[] [CS10] D. I. Cartwright and T. Steger. Enumeration of the 50 fake projective planes. C. R. Math. Acad. Sci. Paris, 348(1-2):11-13, 2010.
\item[] [Der05] M. Deraux. Dirichlet domains for the Mostow lattices. Experiment. Math., 14(4):467-490, 2005.
\item[] [Der06] M. Deraux. Deforming the $\mathbb{R}$-Fuchsian (4,4,4)-triangle group into a lattice. Topology, 45:989-1020, 2006.
\item[] [DFP05] M. Deraux, E. Falbel, and J. Paupert. New constructions of fundamental polyhedra in complex hyperbolic space. Acta Math., 194:155-201, 2005.
\item[] [DM86] P. Deligne and G. D. Mostow. Monodromy of hypergeometric functions and nonlattice integral monodromy. Inst. Hautes Études Sci. Publ. Math., 63:5-89, 1986.
\item[] [DM93] P. Deligne and G. D. Mostow. Commensurabilities among lattices in $\mathrm{PU}(1, n)$, volume 132 of Annals of Mathematics Studies. Princeton Univ. Press, Princeton, 1993.
\end{itemize}
\begin{itemize}
\item[] [DPP11] M. Deraux, J. R. Parker, and J. Paupert. Census for the complex hyperbolic sporadic triangle groups. Experiment. Math., 20:467-486, 2011.
\item[] [FP06] E. Falbel and J. Parker. The geometry of the Eisenstein-Picard modular group. Duke Math. J., 131:249-289, 2006.
\item[] [Gir21] G. Giraud. Sur certaines fonctions automorphes de deux variables. Ann. Sci. École Norm. Sup., 38:43-164, 1921.
\item[] [Gol99] W. M. Goldman. Complex Hyperbolic Geometry. Oxford Mathematical Monographs. Oxford University Press, 1999.
\item[] [GPS88] M. Gromov and I. Piatetski-Shapiro. Nonarithmetic groups in Lobachevsky spaces. Inst. Hautes Études Sci. Publ. Math., 66:93-103, 1988.
\item[] [GS92] M. Gromov and R. Schoen. Harmonic maps into singular spaces and $p$-adic superrigidity for lattices in groups of rank one. Inst. Hautes Études Sci. Publ. Math., 76:165-246, 1992.
\item[] [Hir83] F. Hirzebruch. Arrangements of lines and algebraic surfaces. In Arithmetic and Geometry, Vol. II, volume 36 of Progr. Math., pages 113-140. Birkhäuser Boston, Mass., 1983.
\item[] [HP96] S. Hersonsky and F. Paulin. On the volumes of complex hyperbolic manifolds. Duke Math. J., 84(3):719-737, 1996.
\item[] [Hsi03] P.-H. Hsieh. Cotranchal bisectors in complex hyperbolic space. Geom. Dedicata, 97:93-98, 2003. Special volume dedicated to the memory of Hanna Miriam Sandler (1960-1999).
\item[] [Kat08] F. Kato. On the Shimura variety having Mumford's fake projective plane as a connected component. Math. Z., 259:631-641, 2008.
\item[] [Kli03] B. Klingler. Sur la rigidité de certains groupes fondamentaux, l'arithméticité des réseaux hyperboliques complexes, et les "faux plans projectifs". Invent. Math., 153(1):105-143, 2003.
\item[] [KM12] A. Kappes and M. Möller. Lyapunov spectrum of ball quotients with applications to commensurability questions. Preprint, arXiv:1207.5433, 2012.
\item[] [Kon00] S. Kondo. A complex hyperbolic structure for the moduli space of curves of genus three. J. Reine Angew. Math., 525:219-232, 2000.
\item[] [Mar75] G. A. Margulis. Discrete groups of motions of manifolds of nonpositive curvature. In Proceedings of the International Congress of Mathematicians (Vancouver, B.C., 1974), Vol. 2, pages 21-34. Canad. Math. Congress, Montreal, Que., 1975.
\item[] [Mar91] G. A. Margulis. Discrete subgroups of semisimple Lie groups, volume 17 of Ergebnisse der Mathematik und ihrer Grenzgebiete. Springer-Verlag, Berlin, 1991.
\item[] [McM13] C. T. McMullen. The Gauss-Bonnet theorem for cone manifolds and volumes of moduli spaces. Preprint, 2013.
\end{itemize}
[McR06] D. B. McReynolds. Finite subgroups of arithmetic lattices in U(2, 1). Geom. Dedicata, 122:135-144, 2006.
[Mos80] G. D. Mostow. On a remarkable class of polyhedra in complex hyperbolic space. Pacific J. Math., 86:171-276, 1980.
[Par06] J. R. Parker. Cone metrics on the sphere and Livne's lattices. Acta Math., 196:1-64, 2006.
[Par08] J. R. Parker. Unfaithful complex hyperbolic triangle groups I: Involutions. Pacific J. Math., 238:145-169, 2008.
[Par] J. R. Parker. Complex Hyperbolic Kleinian Groups. Cambridge University Press, To appear.
[Pau10] J. Paupert. Unfaithful complex hyperbolic triangle groups III: arithmeticity and commensurability. Pacific J. Math., 245:359-372, 2010.
[Pic81] E. Picard. Sur une extension aux fonctions de deux variables du problème de Riemann relatif aux fonctions hypergéométriques. Ann. Sci. École Norm. Sup. (2), 10:305-322, 1881.
[PP09] J. R. Parker and J. Paupert. Unfaithful complex hyperbolic triangle groups II: Higher order reflections. Pacific J. Math., 239:357-389, 2009.
[PY07] G. Prasad and S.-K. Yeung. Fake projective planes. Invent. Math., 168(2):321-370, 2007.
[Rag72] M. S. Raghunathan. Discrete subgroups of Lie groups. Springer-Verlag, New York, 1972. Ergebnisse der Mathematik und ihrer Grenzgebiete, Band 68.
[Rez95] A. Reznikov. Simpson's theory and superrigidity of complex hyperbolic lattices. C. R. Acad. Sci. Paris Sér. I Math., 320(9):1061-1064, 1995.
[Sau90] J. K. Sauter. Isomorphisms among monodromy groups and applications to lattices in PU(1,2). Pacific J. Math., 146(2):331-384, 1990.
[Sch02] R. E. Schwartz. Complex hyperbolic triangle groups. In Proceedings of the International Congress of Mathematicians, Vol. II (Beijing, 2002), pages 339-349, Beijing, 2002. Higher Ed. Press.
[Sch03] R. E. Schwartz. Real hyperbolic on the outside, complex hyperbolic on the inside. Inv. Math., 151(2):221-295, 2003.
[Shv92] O. V. Shvartsman. An example of a nonarithmetic discrete group in the complex ball. In Lie groups, their discrete subgroups, and invariant theory, volume 8 of Adv. Soviet Math., pages 191-196. Amer. Math. Soc., Providence, RI, 1992.
[Sto12] M. Stover. Arithmeticity of complex hyperbolic triangle groups. Pacific J. Math., 257(1):243-256, 2012.
[Tho10] J. M. Thompson. Complex hyperbolic triangle groups. PhD thesis, Durham University, 2010.
\begin{itemize}
\item[] [Thu98] W. P. Thurston. Shapes of polyhedra and triangulations of the sphere. Geometry and Topology Monographs, 1:511-549, 1998.
\item[] [Tit66] J. Tits. Classification of algebraic semisimple groups. In Algebraic Groups and Discontinuous Subgroups (Proc. Sympos. Pure Math., Boulder, Colo., 1965), pages 33-62. Amer. Math. Soc., Providence, R.I., 1966.
\item[] [Vin68] E. B. Vinberg. Discrete groups generated by reflections in Lobačevskiĭ spaces. Math. USSR Sb., 1:429-444, 1968.
\item[] [Wei60] A. Weil. Algebras with involutions and the classical groups. J. Indian Math. Soc., 24:589-623 (1961), 1960.
\item[] [Yeu04] S.-K. Yeung. Integrality and arithmeticity of co-compact lattice corresponding to certain complex two-ball quotients of Picard number one. Asian J. Math., 8(1):107-129, 2004.
\item[] [Zha12] T. Zhao. New construction of fundamental domains for certain Mostow groups. Pacific J. Math., 259(1):209-256, 2012.
\end{itemize}

Martin Deraux
Institut Fourier, Université de Grenoble 1
deraux@ujf-grenoble.fr
John R. Parker
Department of Mathematical Sciences, Durham University
j.r.parker@durham.ac.uk

Julien Paupert
School of Mathematical and Statistical Sciences, Arizona State University
paupert@asu.edu
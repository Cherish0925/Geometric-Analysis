---
retention_scope: session
part: 2
total_parts: 3
---

[Part 2/3 of: [math/0611157] Rational blow-downs and smoothings of surface singularities]

Returning to the proof of Proposition 5.2, suppose now that $\Gamma$ contains no reducible vector. Take a leaf $u$ on a leg of length > 1 and denote the vertex adjacent to $u$ by $u^{\prime}$ (which, by the length assumption, is different from $v_{1}$ ). Since there is no reducible vector on the leg of $u$, according to Lemma 5.3 we get that $-E_{i_{u}}$ is in $u^{\prime}$. Therefore by replacing the edge $\overline{u u^{\prime}}$ with $u+u^{\prime}$ and deleting $-E_{i_{u}}$ from another leaf we get a graph $\Gamma^{\prime}$, and since $\Gamma^{\prime}$ embeds into $(n-1)\langle-1\rangle=\oplus_{i \neq i_{u}}\left\langle E_{i}\right\rangle$ and it is obviously minimal (since leaves contain $-E_{1}$ ), we get that $\Gamma^{\prime} \in \mathcal{S}$. Since it still has an index of type (9), it is of Case (B) or (C). In order to apply induction, we only need to show that $\Gamma^{\prime}$ has full leaves, and since we changed only one leaf, it boils down to showing that $u+u^{\prime}=E_{i_{u^{\prime}}}-\sum_{j} E_{j}$ is full. In other words, we have to find two $-E_{i_{u^{\prime}}}$ in $\Gamma$. The first one is easy to find, since the lack of reducible vectors (by Lemma 5.3) implies that $-E_{i_{u^{\prime}}}$ is in the vector $u_{3} \neq u$ adjacent to $u^{\prime}$. To find the second one, we need a longer argument. Let $v_{l} \in \Gamma$ denote the leaf containing $-E_{i_{u}}$. If the leg of $v_{l}$ is of length $>1$, then (again by the above principle) one $-E_{i_{v_{l}}}$ must be in the (unique) vector adjacent to $v_{l}$, and the other one (which exists, since $v_{l}$ is full) in a leaf, hence there is none in $u^{\prime}$, although $Q\left(u^{\prime}, v_{l}\right)=0$. Since both vectors contain $-E_{i_{u}}$, this implies that $-E_{i_{u^{\prime}}}$ is in $v_{l}$, finishing the argument. We still have to deal with the case when the leg of $v_{l}$ is of length 1, that it, $v_{l}$ is adjacent to the central vertex $v_{1}$. If the third leg of $\Gamma$ (i.e. the one with leaf $w$ distinct from $u$ and $v_{l}$ ) is of length > 1, then using this $w$ as the starting vector instead of $u$ the inductive argument proceeds. Therefore we only need to consider the last case when two legs of $\Gamma$ are of length one. Suppose that the leaves of these short legs are $v_{l}$ and $w$ as above. Then, as above, we can assume that $-E_{i_{u}}$ is in $v_{l}$, and if $-E_{i_{u^{\prime}}}$ is not in $v_{l}$ then $-E_{i_{v_{l}}}$ must be in $u^{\prime}$. This implies that $-E_{i_{v_{l}}}$ cannot be in $u$, hence it must be in $w$, and so either $-E_{i_{u^{\prime}}}$ is in $w$ (finishing our search) or $-E_{i_{w}}$ is in $u^{\prime}$, which contradicts
the fact that $Q\left(u, u^{\prime}\right)=1$ since $-E_{i_{w}}$ also contributes to $u$. This final (long) observation concludes the proof that $u+u^{\prime}$ is full, hence by induction we can assume that $\Gamma^{\prime}$ is full, and since when forming $\Gamma^{\prime}$ from $\Gamma$ we increased the sum of squares by 3, this implies that $\Gamma$ is full. \(\square\)

A useful consequence of the above result provides an easy characterization of full graphs in $\mathcal{S}$ :

Corollary 5.4 The plumbing graph $\Gamma \in \mathcal{S}$ of Cases (B) or (C) is full if and only if $\Gamma$ has three leaves.

Proof The first paragraph of the proof of Proposition 5.2 shows that if $\Gamma$ is full (hence admits only full leaves) then $\Gamma$ has three leaves. Conversely, if $\Gamma$ has three leaves and all leaves are full, then by Proposition 5.2 the plumbing graph $\Gamma$ is full. Consider now the case when $\Gamma$ has three leaves and $v$ is a nonfull leaf. By denoting the unique vector adjacent to $v$ by $v^{\prime}$ we distinguish two cases: If $-E_{i_{v}}$ is not in $v^{\prime}$ then by erasing $v$ and adding $E_{i_{v}}$ to the vector $w\left(\neq v^{\prime}\right)$ containing $-E_{i_{v}}$ we get a minimal graph with three leaves on less vertices, hence induction and the fact $v^{2} \leq-2$ implies that $\Gamma$ is full. If $-E_{i_{v}}$ is in $v^{\prime}$, then the above argument breaks down only if $v^{\prime}=E_{i_{v^{\prime}}}-E_{i_{v}}$, i.e., after deleting $v$ and $-E_{i_{v}}$ the resulting plumbing graph is not minimal. Now adding $v$ to $v^{\prime}$ (and applying induction) we get that the resulting graph $\Gamma^{\prime}$ is full. This, however, means that the other two leaves $w, u$ of $\Gamma$ are full and (by denoting the type (9) index by 1) the basis element $-E_{1}$ is in $v$ (since it is in $v+v^{\prime}$ but $v^{\prime}=E_{i_{v^{\prime}}}-E_{i_{v}}$ ). Since $u$ and $w$ are full, a copy of $-E_{1}$ is in both $u$ and $w$. Now $Q(v, u)=Q(v, w)=0$ implies that $-E_{i_{u}}$ and $-E_{i_{w}}$ are in $v$, and so are in $v+v^{\prime}$. In this case $Q\left(v^{\prime}, u\right)=Q\left(v^{\prime}, w\right)=0$ shows that both $u$ and $w$ contain $-E_{i_{v^{\prime}}}$. In this point we reached the desired contradiction, since a vector other than $v$ can connect to $v^{\prime}$ only through $-E_{i_{v^{\prime}}}$. This final contradiction shows that a graph with three leaves is full. \(\square\)

\subsection*{5.2 Embeddings with indices of Case (B)}

We are now ready to consider graphs $\Gamma \in \mathcal{S}$ with indices of Case (B). As before, we denoted the type (9) index by 1, while the type (2) index will be denoted by 2. Let $v$ denote the vector containing $-E_{2}$. In the classification we follow the strategy of first proving that a graph $\Gamma$ of Case (B) always admits a reducible vector $v$; this vector always contains $-E_{2}$; and, either $v$ is of valency three (in which case we show that $|\Gamma|=4$ and the graph is given by Figure 1(c)), or we can contract it and apply induction.

Proposition 5.5 Suppose that $\Gamma$ is of Case (B) and $v$ contains $-E_{2}$ (where 2 is the index of type (2)). Then for $v$ we have $v^{2}=-2$; in particular, $v=E_{i_{v}}-E_{2}$ is reducible.

Proof We proceed by induction on $|\Gamma|$. For $n=4$ a case-by-case check verifies the result. Suppose that the statement is verified for all graphs on less than $n$ vertices, and $\Gamma$ is of Case (B) defined on $n \geq 5$ vertices.

Suppose first that $\Gamma$ has a nonfull leaf $u=E_{i_{u}}-\sum_{j \in J_{u}} E_{j}$, which is adjacent to $u^{\prime}$. Assume first that $-E_{i_{u}}$ is not in $u^{\prime}$. If $u$ contains $-E_{2}$ then either $u^{2}=-2$, verifying the result, or we can move $-E_{2}$ to any other vector and keep the resulting graph minimal. Therefore in the following we can assume that $-E_{2}$ is not in $u$. Delete $u$ from $\Gamma$ and the single $-E_{i_{u}}$ from the vector $w \in \Gamma$ containing it (hence $w \neq u^{\prime}$ ), and get $\Gamma^{\prime}$ embedded in $(n-1)\langle-1\rangle$. The usual argument shows that $\Gamma^{\prime}$ is minimal: if $w=E_{i_{w}}-E_{i_{u}}$ then $Q(u, w) \neq 0$. Also, since $-E_{2}$ is in $\Gamma^{\prime} \in \mathcal{S}$, it is obviously of Case (B). Therefore by induction $-E_{2}$ is in a vector of square -2 in $\Gamma^{\prime}$. The basis element $-E_{2}$ cannot be in $w \in \Gamma$, since then by induction $\left(w+E_{i_{u}}\right)^{2}=-2$ and so $Q\left(u, E_{i_{w}}-E_{i_{u}}-E_{2}\right)=$ $Q(u, w) \neq 0$. This shows that the vector containing $-E_{2}$ was not changed when creating $\Gamma^{\prime}$ from $\Gamma$ hence the statement of the proposition follows by induction on $\Gamma$. We have to examine the case when $u^{\prime}$ contains $-E_{i_{u}}$. Then adding $u$ to $u^{\prime}$ we can apply induction again. If $-E_{2}$ is in $u+u^{\prime}$ then by induction $\left(u+u^{\prime}\right)^{2}=-2$, implying $u^{2}=\left(u^{\prime}\right)^{2}=-2$. If $-E_{2}$ is not in $u+u^{\prime}$ then $-E_{2}$ is in a vector not altered by adding $u$ to $u^{\prime}$, implying the result.

Suppose next that all leaves are full. Then by the proof of Proposition 5.2 the graph $\Gamma$ has exactly three leaves and (again by Proposition 5.2) $\Gamma$ is full. Assume that $n>4$ and let $u$ be a leaf on the longest leg (of length $>1$ ), adjacent to $u^{\prime}$. Assume first that on this leg all vectors are of the form $w=$ $E_{i_{w}}-\sum_{j \in J_{w}} E_{j}$. By Lemma 5.3 if $u^{\prime}$ does not contain $-E_{i_{u}}$, then on the leg there is a reducible vector $v=E_{i_{v}}-\sum_{j \in J_{v}} E_{j}$ of valency two. Modifying $v$ to $E_{i_{v}}$ we can blow it down, and in the blown-down graph there is at most one $(-1)$-vertex, to which we can add $v-E_{i_{v}}$, hence forming a minimal graph. Note that the blown down graph $\Gamma^{\prime}$ has also three leaves, and since before adding $v-E_{i_{v}}$ it cannot be full, by Corollary 5.4 the graph $\Gamma^{\prime}$ must contain a vector of square (-1); we added $v-E_{i_{v}}$ to this vector. Induction now shows that in this graph $-E_{2}$ is in a vector of square -2. This vector was either intact by our operation, or it is one of the two affected by the blow down. In the first case the proof is obviously complete, in the second case we see that the two vectors (after the blow-down) cannot have the shape $E_{a}-E_{2}$ and $E_{b}+v-E_{i_{v}}$ since these two vectors give zero pairing with each other. This
shows that $v-E_{i_{v}}=-E_{2}$, verifying the statement.
If $u^{\prime}$ contains $-E_{i_{u}}$, then the other $-E_{i_{u}}$ must be in one of the leaves of the graph, cf. the proof of Proposition 5.2. Consider the graph $\Gamma^{\prime}$ we get by adding $u$ to $u^{\prime}$ and deleting $-E_{i_{u}}$ from the other leaf. Since $\Gamma$ was full, the graph $\Gamma^{\prime}$ is also full, and so has full leaves. Then $-E_{2}$ is in a vector of square -2 in $\Gamma^{\prime}$, which cannot be the leaf we modified, since $-E_{1}$ is there, hence it would have square -3 in $\Gamma^{\prime}$. Therefore $-E_{2}$ is either in a vector not changed by our reduction or in $u+u^{\prime}$, both cases implying the result.

Finally we have to consider the case when on the longest leg we chose there is a vector $w$ of the form $-2 E_{3}-\sum_{j \in J_{w}} E_{j}$. In this case $-E_{1}$ must be in $w$, since otherwise the sum of vectors between $w$ and the central vector $v_{1}$ (incuding both) would contain $E_{1}$ and $-2 E_{j}$ for some $j$. (There is no $-E_{1}$ between $w$ and $v_{1}$ since $-E_{1}$ must be in leaf.) Therefore $w$ is a leaf. If $w^{\prime}$ is the unique vector adjacent to $w$ then $-E_{i_{w^{\prime}}}$ is in $w$, hence the argument given in Lemma 5.3 shows the existence of a reducible vector on the leg of $w$. From that fact the proof given above applies. Notice that if there is no vector between $w$ and $v_{1}$ then (since we chose the longest leg of $\Gamma$ ) we get that $|\Gamma|=4$, which case has been already discussed. \(\square\)

As a final preparatory result, we need to examine the case when $\Gamma$ has a reducible vector of valency three.

Lemma 5.6 Suppose that $\Gamma$ is of Case (B) and it has a reducible vector of valency three. Then $|\Gamma|=4$ and $\Gamma$ is isomorphic to the graph given by Figure 1(c).

Proof Obviously $v_{1}=E_{1}-\sum_{j \in J_{1}} E_{j}$ can be the only reducible vector of valency three. Suppose that it is adjacent to $u_{1}, u_{2}, u_{3}$. Then by Corollary 3.5 we have that one of the vectors, say $u_{1}$ must be of the form $u_{1}=-2 E_{3}-$ $\sum_{j \in J_{u_{1}}} E_{j}$. (Recall that in Case (B) the graph contains an index of type (5).) The shape of $v_{1}+u_{1}+u_{2}+u_{3}$ implies that $u_{2}=E_{3}-\sum_{j \in J_{u_{2}}} E_{j}$. If $u_{3}=E_{4}-\sum_{j \in J_{u_{3}}} E_{j}$ then a straightforward argument (based on the fact that $Q\left(u_{i}, u_{j}\right)=0$ for $1 \leq i \neq j \leq 3$ ) shows that $-E_{4}$ must be in $u_{1}$ and $u_{2}$ (since $u_{1}, u_{2}, u_{3}$ all contain $-E_{1}$ by the reducibility assumption). Let $w=v_{1}-E_{1}$; by the reducibility of $v_{1}$ we have that $Q(w, u)=0$ for all $u$ distinct from $v_{1}$. Suppose that $u \in \Gamma$ contains $-E_{2}$. If $u$ is among $\left\{v_{1}, u_{1}, u_{2}, u_{3}\right\}$ then delete $-E_{2}$ from it, otherwise modify $u$ to $u+E_{2}+w$. Finally contract the subgraph $\left\{v_{1}, u_{1}, u_{2}, u_{3}\right\}$ to the single vertex $E_{1}+u_{1}+u_{2}+u_{3}+E_{3}+E_{4}$. In this way we get a new minimal graph $\Gamma^{\prime} \in \mathcal{S}$ on $n-3$ vertices, embedded into $(n-3)\langle-1\rangle$,
since the indices 2, 3, and 4 have been eliminated. Notice that $\Gamma^{\prime}$ contains an index of type (3) (the index 1 which was of type (9) in $\Gamma$ ), hence by Theorem 3.8 (cf. Remark 3.9) we get that $\left|\Gamma^{\prime}\right|=n-3=1$. The classification of graphs on 4 vertices then concludes the proof. \(\square\)

Now we are ready to prove the classification result for this case:

Proof of Theorem 3.12 Let $v \in \Gamma$ be the vector containing $-E_{2}$. By Proposition 5.5 we know that $v+E_{2}=E_{i_{v}}$ is of square -1 and therefore it is reducible. If $v$ is of valency 1 or 2 then we can blow $v+E_{2}=E_{i_{v}}$ down, in the resulting graph $\Gamma^{\prime}$ there is no $E_{i_{v}}$, and in addition there is at most one vector of square -1. By adding $-E_{2}$ to this potential (-1)-vector (resulting $\Gamma^{\prime \prime}$ ), by induction we have $\Gamma^{\prime \prime} \in \mathcal{C}$; moreover the vector we added $-E_{2}$ to has square -2, hence before adding $-E_{2}$ it was of square -1, implying that $\Gamma \in \mathcal{C}$. If the valency of $v$ is three then the application of Lemma 5.6 concludes the proof. \(\square\)

As in Proposition 4.4, we also need that elements of $\mathcal{C}$ actually satisfy the conditions defining $\mathcal{S}$.

Proposition 5.7 If $\Gamma \in \mathcal{C}$ then $\Gamma \in \mathcal{S}$.

Proof The vectors $-2 E_{3}-E_{1}-E_{4}, E_{1}, E_{3}-E_{4}-E_{1}, E_{4}-E_{1}$ provide an appropriate embedding of the graph of Figure 10(c) into $3\langle-1\rangle$. After $n$ blow-ups the resulting graph on $(n+4)$ vertices embeds into $(n+3)\langle-1\rangle$, and by adding $-E_{2}$ to the unique (-1)-vertex, the proof is complete. Notice, for example, that the graph of Figure 1(c) embeds into $4\langle-1\rangle$ as $-2 E_{3}-E_{1}-$ $E_{4}, E_{1}-E_{2}, E_{3}-E_{4}-E_{1}, E_{4}-E_{1}$, cf. Figure 14. \(\square\)

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/df5f5431-21ef-431b-b837-d2c96a8445b9-33.jpg?height=209&width=788&top_left_y=2006&top_left_x=647}
\captionsetup{labelformat=empty}
\caption{Figure 14: The embedding of the first element of $\mathcal{C}$ into $4\langle-1\rangle$}
\end{figure}

\section*{6 Classification of graphs of Case (C)}

Suppose now that $\Gamma$ embeds into $n\langle-1\rangle$ with indices listed under Case (C). Notice first that in this case for every index $i$ there is a unique vector $v_{i}$ such that
$$v_{i}=E_{i}-\sum_{j \in J_{i}} E_{j} .$$
In the following we will distinguish two cases, according to whether the leaves of $\Gamma$ are full or not.

\subsection*{6.1 Graphs with full leaves}

We start with the case when all leaves of the plumbing tree are full. As before, $i=1$ denotes the unique index of type (9); there are exactly three leaves, each containing $-E_{1}$, and if $v=E_{i_{v}}-\sum_{j \in J_{v}} E_{j}$ is a leaf then one $-E_{i_{v}}$ is contained by another leaf, cf. the proof of Proposition 5.2. The unique vector $v_{1}=E_{1}-\sum_{j \in J_{1}} E_{j}$ is of valency three and all other vectors have $\operatorname{deg} v \leq 2$.

\section*{Graphs with reducible vectors}

First we will examine the case when the leaves are full, and the graph contains reducible vectors.

Theorem 6.1 Suppose that $\Gamma$ is a graph with indices of Case (C), all leaves are full and there is a vector which is reducible. Then $\Gamma \in \mathcal{A} \cup \mathcal{B}$.

Proof We will proceed by induction. Consider the reducible vector $v=E_{i_{v}}-$ $\sum_{j \in J_{v}} E_{j}$. Since the leaves are full, a leaf cannot be reducible. If $v$ is of valency two, then change it to $E_{i_{v}}$, blow it down and consider the resulting graph $\Gamma^{\prime}$. Since $\Gamma^{\prime}$ with three leaves cannot be full (we erased $v$ and two further $-E_{i_{v}}$ ), by Corollary 5.4 it is not minimal. Add $v-E_{i_{v}}=-\sum_{j \in J_{v}} E_{j}$ to the (-1)-vector and get $\Gamma^{\prime \prime}$. This is a minimal graph, the leaves are still full, by construction it has a reducible vector (the $(-1)$-vector to which we added $-\sum_{j \in J_{v}} E_{j}$ ), hence induction applies, showing that $\Gamma^{\prime \prime} \in \mathcal{A} \cup \mathcal{B}$. Now $\Gamma$ is gotten from $\Gamma^{\prime \prime}$ by considering the reducible vector $w=E_{i_{w}}-\sum_{j \in J_{w}} E_{j} \in \Gamma^{\prime \prime}$, adding $\sum_{j \in J_{w}} E_{j}$ to it, blowing it up and then subtracting $\sum_{j \in J_{w}} E_{j}$ from the resulting new vertex with decoration (-1).

The blowing down procedure will stop only when $\operatorname{deg} v=3$ for the reducible vector $v$. Since the leaves are full, in this case we have $n=4$, and we get that the resulting graph is one of Figures 1(a) or (b). Since in that case the square of the correction term $-\sum_{j \in J_{w}} E_{j}$ we added to the (-1)-vertex is -2 or -3, it must have been the case throughout the whole process, since the two (or three) basis vectors cannot be grouped in two groups such that they give zero pairing with every other vector. This last observation completes the proof. \(\square\)

\section*{Graphs with no reducible vectors}

The next case to consider is when the graph $\Gamma$ has full leaves and it contains no reducible vector. It turns out that this is the longest case to discuss, and we will divide our classification into futher subcases. To do that, recall that since the graph has full leaves, it is full, and has exactly three leaves $w_{1}, w_{2}$ and $w_{3}$.

Definition 6.2 Suppose that the graph $\Gamma$ of Case (C) is full and admits no reducible vectors.
\begin{itemize}
\item[-] The leaves of $\Gamma$ are of type $\mathbb{Z}_{3}$ if (after possibly renaming the leaves) $-E_{i_{w_{1}}}$ is in $w_{2},-E_{i_{w_{2}}}$ is in $w_{3}$ and $-E_{i_{w_{3}}}$ is in $w_{1}$.
\item[-] The leaves of the graph $\Gamma$ as above are of type $\mathbb{Z}_{2}$ if (again, after possibly renaming the leaves) $-E_{i_{w_{1}}}$ is in $w_{2}$, another $-E_{i_{w_{1}}}$ is in $w_{3}$ and then it follows that $-E_{i_{w_{3}}}$ is in $w_{2}$ and $-E_{i_{w_{2}}}$ is in $w_{3}$.
\item[-] The leaf $w=E_{i_{w}}-\sum_{j \in J_{w}} E_{j}$ of a graph $\Gamma$ with full leaves and no reducible vectors is called free if the single vector $w^{\prime}$ with $Q\left(w, w^{\prime}\right)=1$ does not contain $-E_{i_{w}}$.
\end{itemize}
It is easy to see that if a leaf $w$ is free, then (since $\Gamma$ contains no reducible vector) it is adjacent to the central vertex $v_{1}$ (of valency three), that is $Q\left(w, v_{1}\right)=1$. It is worth mentioning that $Q\left(w, v_{1}\right)=1$ might hold without $w$ being free. In the graph $\Gamma$ there are three leaves, and if all are free then the graph is defined on four vertices and is nonminimal (admitting the shape given by Figure 15, with vectors $E_{2}-E_{1}-E_{3}-E_{4}, E_{1}, E_{3}-E_{1}-E_{2}-E_{4}$ and $E_{4}-E_{1}-E_{2}-E_{3}$ ). In the following therefore we restrict our attention to the cases when there are zero, one or two free leaves in $\Gamma$. In fact, by definition if the leaves $\left\{w_{1}, w_{2}, w_{3}\right\}$ are of type $\mathbb{Z}_{2}$ then $w_{1}$ is automatically free, hence in this case we have only two cases to examine. Notice first that

Lemma 6.3 Any graph $\Gamma \in \mathcal{S}$ of Case (C) with full leaves is either of type $\mathbb{Z}_{3}$ or of type $\mathbb{Z}_{2}$.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/df5f5431-21ef-431b-b837-d2c96a8445b9-36.jpg?height=201&width=329&top_left_y=473&top_left_x=923}
\captionsetup{labelformat=empty}
\caption{Figure 15: (Nonminimal) graph with three free leaves}
\end{figure}

Proof Let $w_{1}=E_{i_{w_{1}}}-\sum_{j \in J_{w_{1}}} E_{j}$ be a leaf. We already know that one $-E_{i_{w_{1}}}$ is in another leaf, say in $w_{2}$. If the third leaf $w_{3}$ also contains $-E_{i_{w_{1}}}$ then in order to have $Q\left(w_{2}, w_{3}\right)=0$ (since both vectors contain $-E_{1}$ and $-E_{i_{w_{1}}}$ ) we have that
$$w_{2}=E_{i_{w_{2}}}-E_{1}-E_{i_{w_{1}}}-E_{i_{w_{3}}}-\ldots \text { and } w_{3}=E_{i_{w_{3}}}-E_{1}-E_{i_{w_{1}}}-E_{i_{w_{2}}}-\ldots,$$
showing that the leaves $\left\{w_{1}, w_{2}, w_{3}\right\}$ are of type $\mathbb{Z}_{2}$.
If the third leaf $w_{3}$ does not contain $-E_{i_{w_{1}}}$ then (in order to achieve $Q\left(w_{1}, w_{3}\right)=$ 0 ) we have that $-E_{i_{w_{3}}}$ is in $w_{1}$. To get $Q\left(w_{2}, w_{3}\right)=0$, we either have that - $E_{i_{w_{3}}}$ is in $w_{2}$, which provides a set of leaves $\left\{w_{1}, w_{2}, w_{3}\right\}$ of type $\mathbb{Z}_{2}$ (with the indices permuted), or $-E_{i_{w_{2}}}$ is in $w_{3}$, showing that the leaves are of type $\mathbb{Z}_{3}$. Since we have examined all possibilities, the proof is complete. \(\square\)

The following two statements now classify graphs with full leaves and no reducible vectors: The graphs of Figures 23-28 (where the expressions of the vertices are also indicated) might be helpful in following the proofs.

Proposition 6.4 Suppose that $\Gamma \in \mathcal{S}$ of Case (C) has full leaves, no reducible vectors and its leaves are of type $\mathbb{Z}_{3}$.
\begin{itemize}
\item[-] If $\Gamma$ has no free leaf then $\Gamma \in \mathcal{W}$.
\item[-] If it has one free leaf then $\Gamma$ is isomorphic to $\Delta_{p, q, r}$ with $p \geq 1$ and $q, r \geq 0$ (and so $\Gamma \in \mathcal{N}$ ).
\item[-] If $\Gamma$ has two free leaves then it is isomprhic to $\Lambda_{p, q, r}$ with $p \geq 1$ and $q, r \geq 0$ (and so $\Gamma \in \mathcal{M}$ ).
\end{itemize}

Proof Suppose first that $\Gamma$ admits no free leaf. Let us fix a leaf $w_{1}$ and assume that $-E_{i_{w_{1}}}$ is in $w_{2}$. If $w_{1}^{\prime}$ is the unique vector adjacent to $w_{1}$, then according to Lemma 5.3 the other $-E_{i_{w_{1}}}$ is in $w_{1}^{\prime}$. The same principle also shows that if $w_{1}^{\prime \prime}$ is the next vector on this leg then it contains $-E_{i_{w_{1}^{\prime}}}$; and so on throughout the leg. At the same time, since $Q\left(w_{2}, w_{1}^{\prime}\right)=0$, the fact that $-E_{i_{w_{1}}}$ is in $w_{1}^{\prime}$
implies that $-E_{i_{w_{1}^{\prime}}}$ must be in $w_{2}$ as well: recall that since there are no free leaves, $-E_{i_{w_{2}}}$ cannot be in $w_{1}^{\prime}$. Suppose that there are $p$ vectors $u_{1}, \ldots, u_{p}$ on the leg of $w_{1}$ (not counting $w_{1}$ and the central vector $v_{1}$ ). Then the above argument shows that in $w_{2}$ we have all the basis vectors $-E_{i_{u_{j}}}$, next to $-E_{i_{w_{1}}}$, $-E_{1}$ and $E_{i_{w_{2}}}$. This shows that $w_{2}^{2} \leq-p-3$. The same argument now applies to all the three legs of $\Gamma$. The central element $v_{1}=E_{1}-\sum_{j \in J_{1}} E_{j}$ must be adjacent to the three legs, and since all three $E_{1}$ 's are in leaves and the leaves are not free, it follows that $v_{1}^{2} \leq-4$. A simple count on the possible value of $\sum v_{i}^{2}$ shows that the estimates sum up to $-3|\Gamma|-1$ (its smallest possible value) therefore the above inequalities must be equalities, and the shape of $\Gamma$ is given by Figure 3 for some appropriate $p, q, r \geq 0$. This concludes the proof of the first case.

Suppose now that $\Gamma$ admits one free leaf, say $w_{1}$. This condition means that one $-E_{i_{w_{1}}}$ is in a leaf, the other is not (since the graph is not of $\mathbb{Z}_{2}$-type), and it is also not in the central vector. Suppose that it is in $u$ on one of the legs. The leg is determined in the following way: if $-E_{i_{w_{1}}}$ is in $w_{2}$ then the vector $u$ must be on the leg of $w_{3}$ otherwise the absence of reducible vectors would imply $Q\left(w_{1}, v_{1}\right)=0$, a contradiction. The vector $u$ divides this leg into two pieces, having $p-1$ vector on the side towards the leaf, and $q$ towards the central element (not counting the leaf and the central vector) for some $p \geq 1$ and $q \geq 0$. The same estimates as before can be used to estimate the squares of the leaves, resulting $w_{1}^{2} \leq-p-2, w_{2}^{2} \leq-q-4$ and $w_{3}^{2} \leq-r-3$ (where $r$ denotes the number of vertices on the leg not containing $u$ ). The central vector must satisfy only $v_{1}^{2} \leq-3$ since there is one free leaf (which can connect to $v_{1}$ by sharing $-E_{1}$ ). On the other hand, since $u$ contains $-E_{i_{w_{1}}}$ we get that $u^{2} \leq-3$. Again, the sum of the estimates already sums up to $-3|\Gamma|-1$, showing that all inequalities must be equalities and so $\Gamma$ is of the form $\Delta_{p, q, r}$. Since the graph is of type $\mathbb{Z}_{3}$, the basis element $-E_{i_{w_{1}}}$ cannot be in the leaf $w_{2}$, therefore we need $p \geq 1$. (The degeneration $p=0$ will lead to a graph of type $\mathbb{Z}_{2}$, cf. Proposition 6.5.)

Finally, the presence of two free leaves $w_{1}, w_{2}$ means that two legs are degenerated to a single leaf, hence the second copies of $-E_{i_{w_{1}}}$ and $-E_{i_{w_{2}}}$ are on the same (nontrivial) leg. An argument similar to the previous one shows that if $-E_{i_{w_{2}}}$ is in the leaf of the long leg, then the basis vector $-E_{i_{w_{1}}}$ is then one closer to the leaf from the two "free" basis elements $-E_{i_{w_{1}}}$ and $-E_{i_{w_{2}}}$. The exact same analyis as above now shows that if these two basis vectors are in different vertices, then $\Gamma$ is of the form $\Lambda_{p, q, r}$ with $p, r \geq 1$; and finally $\Gamma$ is isomorphic to $\Lambda_{p, q, 0}$ if both $-E_{i_{w_{1}}}$ and $-E_{i_{w_{2}}}$ are in the same vector. Notice
that since $\Gamma$ is of type $\mathbb{Z}_{3}$, this vector cannot be a leaf. The degeneration when both these basis elements are in a leaf is exactly $\Lambda_{0, q, 0}$, which case - according to our point of view - falls in the category of Case (B) rather than Case (C). Now this vector $u$ containing both $-E_{i_{w_{1}}}$ and $-E_{i_{w_{2}}}$ will satisfy $u^{2} \leq-4$, hence the usual argument of summing the squares provides the result. \(\square\)

Proposition 6.5 Suppose that $\Gamma \in \mathcal{S}$ of Case (C) has full leaves, no reducible vectors and its leaves are of type $\mathbb{Z}_{2}$.
\begin{itemize}
\item[-] If it has one free leaf then $\Gamma$ is isomorphic to $\Delta_{0, q, r}$ with $q, r \geq 0$, in particular $\Gamma \in \mathcal{N}$.
\item[-] if $\Gamma$ has two free leaves then it is isomprhic to $\Lambda_{0, p, r}(q \geq 0$ and $r \geq 1)$, so $\Gamma \in \mathcal{M}$.
\end{itemize}

Proof Notice that (as we already remarked) the fact that $\Gamma$ is of type $\mathbb{Z}_{2}$ implies that there is a free leaf $w_{1}$, and both $-E_{i_{w_{1}}}$ are in the two other leaves. The same idea and the estimate on the sum of squares shows that such a graph is isomorphic to $\Delta_{0, q, r}$ for some $q, r \geq 0$.
If there are two free leaves $w_{1}, w_{2}$ (and $\Gamma$ is still of type $\mathbb{Z}_{2}$ ) then for $w_{1}$ both $-E_{i_{w_{1}}}$ are in leaves (as is dictated by the fact that $\Gamma$ is of type $\mathbb{Z}_{2}$ ), but the second $-E_{i_{w_{2}}}$ is on the single nontrivial leg. It gives rise to a vector $u$ with $u^{2} \leq-3$, and so the usual estimate on the sum of squares identifies $\Gamma$ with a graph $\Lambda_{0, q, r}$ for $r \geq 1$ and $q \geq 0$. Again, by degenerating $-E_{i_{w_{2}}}$ to the same leaf (i.e., considering $r=0$ ) we get a graph $\Lambda_{0, q, 0}$ of Case (B). \(\square\)

\subsection*{6.2 The case of nonfull leaves}

The final case to be considered is when the graph $\Gamma \in \mathcal{S}$ has indices of Case (C) and it also admits nonfull leaves.

Lemma 6.6 If $\Gamma$ has a nonfull leaf then it has a reducible vector.

Proof As usual, we use induction on $|\Gamma|$. Suppose that $v$ is a nonfull leaf adjacent to $v^{\prime}$. If $v^{\prime}$ contains $-E_{i_{v}}$ then $v$ is reducible, and we are done. If $v^{\prime}$ does not contain $-E_{i_{v}}$, then delete $v$ and $-E_{i_{v}}$ from the graph. (The term $-E_{i_{v}}$ was contained by $w$, and since $Q(v, w)=0$, it is easy to see that $\left(w+E_{i_{v}}\right)^{2} \leq-2$, hence the resulting graph is minimal on less vertices.) Now if the resulting graph $\Gamma^{\prime} \in \mathcal{S}$ admits a nonfull leaf, then induction shows that $\Gamma^{\prime}$ admits a reducible vector. It is obviously reducible in $\Gamma$ as well, unless it
is the (potential) new leaf $v^{\prime}$ of $\Gamma^{\prime}$, in which case (since $-E_{i_{v}}$ was not in $v^{\prime}$ ) we get that $v^{\prime}$ was reducible in $\Gamma$. In case in $\Gamma^{\prime}$ all leaves are full, then we argue as follows: there are exactly three leaves in $\Gamma^{\prime}$, and by Proposition $5.2 \Gamma^{\prime}$ is full, showing that $\sum_{v_{i} \in \Gamma^{\prime}} v_{i}^{2}=-3\left|\Gamma^{\prime}\right|-1$. Since $\Gamma$ is nonfull, we have that $\sum_{v_{i} \in \Gamma} v_{i}^{2}>-3|\Gamma|-1=-3\left(\left|\Gamma^{\prime}\right|+1\right)-1$, and since we have dropped $v$ and $-E_{i_{v}}$ from a vertex of $\Gamma$, it means that $v^{2}>-2$, contradicting the minimality of $\Gamma$. \(\square\)

Before the final argument, we need to study the case when the reducible vector is of valency three, providing the analogue of Lemma 5.6.

Lemma 6.7 If $\Gamma \in \mathcal{S}$ is of Case (C) and it admits a reducible vector of valency three then $|\Gamma|=4$ and $\Gamma$ is isomorphic to one of the graphs of Figure 1(a) or (b).

Proof The proof will proceed by induction on $|\Gamma|$. First, a simple case-by-case check shows that such graph does not exist if $|\Gamma|=5$. Suppose now that $\Gamma \in \mathcal{S}$ admits a reducible vector $v_{1}$ of valency three. Let $v \in \Gamma$ be a leaf with $Q\left(v, v_{1}\right)=0$. If $|\Gamma|>5$ then such leaf exists, and since $v_{1}$ is reducible, it is nonfull. Following the usual line of reasoning, either delete $v$ and the unique further $-E_{i_{v}}$ (if $-E_{i_{v}}$ is not in the unique vector $v^{\prime}$ adjacent to $v$ ) or add $v$ to $v^{\prime}$. In this way we get $\Gamma^{\prime} \in \mathcal{S}$ on $|\Gamma|-1$ vertices, still admitting a reducible vector of valency three, hence induction yields that $\Gamma$ must be equal to 4 . The rest of the statement is an easy exercise. \(\square\)

Theorem 6.8 If $\Gamma$ is of Case (C) and has a nonfull leaf then $\Gamma \in \mathcal{A} \cup \mathcal{B}$.
Proof By Lemma 6.6 the assumption implies that there is a reducible vector $v \in \Gamma$. If $\operatorname{deg} v=3$ then by Lemma 6.7 the theorem is proved. If $v$ is of valency 1 or 2, then we can modify $v$ to $E_{i_{v}}$, blow down $E_{i_{v}}$ and add $v-E_{i_{v}}$ to the potential (-1)-vector of the resulting graph $\Gamma^{\prime}$. We want to argue that $\Gamma^{\prime}$ also admits a reducible vector. If $\Gamma^{\prime}$ has a nonfull leaf then this fact follows from Lemma 6.6. In case all leaves of $\Gamma^{\prime}$ are full, then $\Gamma^{\prime}$ has three leaves and $\Gamma^{\prime}$ is full, hence before adding $v-E_{i_{v}}$ it must have contained a $(-1)$-vector, which is automatically reducible. By induction on $|\Gamma|$ we get that $\Gamma^{\prime} \in \mathcal{A} \cup \mathcal{B}$, therefore in oder to prove the theorem we only need to understand how $\Gamma$ can be rebuilt from the blown down graph $\Gamma^{\prime}$.

Suppose that $v=E_{i_{v}}-\sum_{j \in J_{v}} E_{j}$ is the reducible vector in $\Gamma$, and $w$ is the reducible vector after the blow-down. We add $-\sum_{j \in J_{v}} E_{j}$ to $w$, and repeat
the above procedure. This procedure will terminate only when the reducible vector has valency three, in which case $n=4$, hence the sum of the tails (i.e., $v-E_{i_{v}}$ ) of the reducibles add up to one, two or three basis vectors. If it is one, then it is under Case (B), since it means that that basis vector does not appear anywhere else, hence is of type (2). If it is two or three, then these come from the first reducible vector, since a single $-E_{i}$ cannot be disjoint from all the vectors (since all indices appear in some vector with positive multiplicity). This shows that there are two cases, when $\left(-\sum_{j \in J_{v}} E_{j}\right)^{2}$ is -2 or -3, corresponding to the two cases growing from the two basic examples of Figure 10 which are of Case (C). \(\square\)

In order to complete the equivalence of $\mathcal{S}$ with the set $\mathcal{G} \cup \mathcal{W} \cup \mathcal{N} \cup \mathcal{M} \cup \mathcal{A} \cup \mathcal{B} \cup \mathcal{C}$ we also need

Proposition 6.9 If $\Gamma \in \mathcal{W} \cup \mathcal{N} \cup \mathcal{M} \cup \mathcal{A} \cup \mathcal{B}$ then $\Gamma \in \mathcal{S}$.
Proof The proof of $\mathcal{A} \subset \mathcal{S}$ follows the same idea as the proof of Proposition 5.7. the vectors $E_{2}-E_{1}-E_{3}, E_{1}, E_{3}-E_{1}-E_{4}, E_{4}-E_{1}-E_{2}$ embed Figure 10(a) into $4\langle-1\rangle$ such that the vector $-E_{2}-E_{3}-E_{4}$ gives zero pairing with all these vectors above. After $n$ blow-ups, the addition of $-E_{2}-E_{3}-E_{4}$ to the unique (-1)-vertex provides the embedding. The proof of the inclusion $\mathcal{B} \subset \mathcal{S}$ proceeds in the same way: notice that $E_{1}-E_{2}-E_{3}-E_{4}, E_{1}, E_{3}-E_{1}-$ $E_{2}-E_{4}, E_{4}-E_{1}$ gives an embedding of Figure 10(b) into $4\langle-1\rangle$ and $-E_{2}-E_{3}$ gives zero pairing with all the vectors listed above. Finally, for proving the inclusions $\mathcal{W} \subset \mathcal{S}, \mathcal{M} \subset \mathcal{S}$ and $\mathcal{N} \subset \mathcal{S}$ we give the explicite embeddings by Figures 23 through 28 of the Appendix. \(\square\)

With this final argument the proof of Theorem 1.8 is now complete.

\section*{7 Constructions of rational homology disks through Kirby calculus}

In this section we prove Theorem 1.9 through embedding the plumbing 4-manifold $M_{\Gamma}$ corresponding to certain $\Gamma \in \mathcal{S}$ into $\#_{|\Gamma|} \overline{\mathbb{C P}^{2}}$. Then the complement of $M_{\Gamma}$ (with the reversed orientation) will be an appropriate rational homology disk $B_{\Gamma}$. The embedding of $M_{\Gamma}$ into $\#_{|\Gamma|} \overline{\mathbb{C P}^{2}}$ will be given by Kirby calculus. We start by showing that a graph $\Gamma \in \mathcal{G}$ gives rise to a 4-manifold which embeds into the connected sum of $|\Gamma|$ copies of $\overline{\mathbb{C P}^{2}}$. (This statement
has been already proved in many places, eg. [1], [5].) The proof uses induction: For the starting case $\Gamma=(-4)$ the diagram of Figure 16 shows that by attaching a 2-handle, a 3-handle and a 4-handle to $M_{\Gamma}$ (which in this case can be represented by the (-4)-framed unknot) we get $\overline{\mathbb{C P}^{2}}$, hence the claim follows.

Remark 7.1 This picture is simply the manifestation of the fact that twice the generator of $H_{2}\left(\overline{\left(\mathbb{C P}^{2}\right.} ; \mathbb{Z}\right)$ can be represented by a sphere of self-intersection (-4). Another way to see this diagram is to regard the (-4)-sphere as the representative of twice the generator (with orientation reversed) and the (-1)-sphere as the representative of the generator; then by blowing up one of the two (positive) intersections repeatedly we can build any graph in $\mathcal{G}$ and in the meantime also verify the embedding we are looking for.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/df5f5431-21ef-431b-b837-d2c96a8445b9-41.jpg?height=337&width=1002&top_left_y=1089&top_left_x=588}
\captionsetup{labelformat=empty}
\caption{Figure 16: The embedding of $\Gamma=(-4)$ into $\overline{\mathbb{C P}^{2}}$}
\end{figure}

Now suppose that $\Gamma=\left(-2,-a_{1}, \ldots,-a_{n}-1\right)$ is constructed from $\Gamma^{\prime}=\left(-a_{1}, \ldots,-a_{n}\right)$ by the inductive step we used to construct $\mathcal{G}$ (cf. Subsection 4.1). We claim that by attaching a 2-handle (symbolized by the (-1)-vertex) to $M_{\Gamma}$ as shown by the plumbing graph of Figure 17 we get a 4-manifold which embeds into $\#_{|\Gamma|} \overline{\mathbb{C P}^{2}}$. To see this embedding we proceed by induction again; suppose that it is true for $\Gamma^{\prime}$, and use the diffeomorphism we get by blowing down the $(-1)-$sphere of Figure 17, cf. Figure 18.

In order to show the necessary embedding for elements in $\mathcal{M} \cup \mathcal{N} \cup \mathcal{W}$, notice first that Figure 19 provides three Kirby diagrams for $\overline{\mathbb{C P}^{2}}$ : in (a) the 0-framed circles cancel the 3-handles, while (b) can be reduced to (a) by sliding one of the (-1)-circles off the others; whereas (c) differs from (b) by a simple isotopy. Now repeatedly blowing up the linkings of the three circles $K_{1}, K_{2}$ and $K_{3}$ ( $p+1, q+1$ and $r+1$ times, respectively) we get a configuration of spheres in $(p+q+r+4) \overline{\mathbb{C P}^{2}}$, cf. Figure 20, Sliding the 2-handles corresponding to the circles $A_{i}$ over the handle corresponding to the central circle $K$ we get $M_{\Gamma_{p, q, r}} \subset(p+q+r+4) \overline{\mathbb{C P}^{2}}$, showing that $\partial M_{\Gamma_{p, q, r}}$ bounds a rational homology

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/df5f5431-21ef-431b-b837-d2c96a8445b9-42.jpg?height=225&width=916&top_left_y=610&top_left_x=648}
\captionsetup{labelformat=empty}
\caption{Figure 17: Attachment of the (-1)-framed 2-handle to $M_{\Gamma}$}
\end{figure}

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/df5f5431-21ef-431b-b837-d2c96a8445b9-42.jpg?height=158&width=1155&top_left_y=1100&top_left_x=508}
\captionsetup{labelformat=empty}
\caption{Figure 18: The inductive step}
\end{figure}
disk. Sliding $A_{1}$ over $B_{1}$ and $A_{2}, A_{3}$ over $K$ we get the corresponding result for the 4-manifolds given by the graphs $\Delta_{p, q, r}$. Finally, sliding $A_{1}$ and $A_{2}$ over $B_{1}, B_{2}$ respectively, and $A_{3}$ over $K$ we get the desired results for $\Lambda_{p, q, r}$. Notice that by not applying blow-ups at some linkings of $K_{1}, K_{2}, K_{3}$ we get the degeneration of $\Delta_{p, q, r}$ for $p=0$ and of $\Lambda_{p, q, r}$ for $p=0$ and/or $r=0$. The simple details are left to the reader. Notice that this approach provides a unified treatment of all graphs in $\mathcal{W} \cup \mathcal{N} \cup \mathcal{M}$.

\section*{8 Smoothings of normal surface singularities with vanishing Milnor number}

Next we will show two methods for constructing smoothings of normal surface singularities which are rational homology disks. Notice that even for those cases treated in the previous section we will get stronger results: in this section the rational homology disks are smoothings of singularities, hence are equipped with natural Stein structures; in fact, they will be affine varieties, with computable fundamental group (and sometimes explicitly given universal covering spaces).

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/df5f5431-21ef-431b-b837-d2c96a8445b9-43.jpg?height=919&width=1005&top_left_y=443&top_left_x=584}
\captionsetup{labelformat=empty}
\caption{Figure 19: Surgery diagrams for $\overline{\mathbb{C P}^{2}}$}
\end{figure}
In addition, the algebro-geometric method to be presented below applies to cases which are not covered in Section 7. The constructions in this section will verify Theorem 1.10.

\subsection*{8.1 Smoothings of negative weights}

The first method is similar in spirit to the strategy we used in Section 7. This method, however, has the limitation of being applicable only for star-shaped graphs. Suppose therefore that $\Gamma$ is a star-shaped graph given by the diagram
![](https://cdn.mathpix.com/cropped/df5f5431-21ef-431b-b837-d2c96a8445b9-43.jpg?height=157&width=864&top_left_y=2053&top_left_x=674)
(We assume that $t \geq 3$, thus excluding the case of cyclic quotient singularities.) The strings of $\Gamma$ are described uniquely by the continued fractions shown,

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/df5f5431-21ef-431b-b837-d2c96a8445b9-44.jpg?height=949&width=997&top_left_y=449&top_left_x=586}
\captionsetup{labelformat=empty}
\caption{Figure 20: The diagram of Figure 19(c) after $(p+q+r+3)$ blow-ups}
\end{figure}
starting from the node. Define its dual $\Gamma^{\prime}$ by reversing the sign of all the decorations on $\Gamma$ and applying 'handle-calculus' along the legs to turn the positive numbers into negative again (except for the central vertex, which might have positive decoration). More explicitely, consider $\Gamma^{\prime}$ given by
![](https://cdn.mathpix.com/cropped/df5f5431-21ef-431b-b837-d2c96a8445b9-44.jpg?height=157&width=860&top_left_y=1822&top_left_x=675)
where now $q_{i}=n_{i}-p_{i}$. It is not hard to see that $\partial M_{\Gamma}$ and $\partial M_{\Gamma^{\prime}}$ are orientation-reversing diffeomorphic 3-manifolds; in fact, as noted in the next paragraph, putting on appropriate complex structures, one sees that $M_{\Gamma} \cup M_{\Gamma^{\prime}}$ is analytically isomorphic to a blow-up of some $\mathbb{P}^{1}$-bundle over $\mathbb{P}^{1}$. It follows that for a negative-definite graph $\Gamma$ its dual graph is no longer negative-definite, but its intersection form is of type $(1, r)$. While in Section 7 we embedded the manifold $M_{\Gamma}$ into $\#_{|\Gamma|} \overline{\mathbb{C P}^{2}}$, this time we will find an embedding of $M_{\Gamma^{\prime}}$ cor-
responding to the dual graph $\Gamma^{\prime}$ into $\mathbb{C P}^{2} \#\left(\left|\Gamma^{\prime}\right|-1\right) \overline{\mathbb{C P}^{2}}$, the $\left(\left|\Gamma^{\prime}\right|-1\right)$-fold blow-up of $\mathbb{C P}^{2}$. As will be discussed, a holomorphic embedding of $M_{\Gamma^{\prime}}$ with the above numerical condition will provide the desired smoothing.

Suppose $X=\operatorname{Spec}(A)$ is a weighted homogeneous normal surface singularity; thus, $A$ is positively graded, or $X$ has a good $\mathbb{C}^{*}$-action, or $A$ is the quotient of a positively graded polynomial ring by weighted homogeneous equations (see e.g. [20] for details as to what follows). Assume also that the link is a rational homology sphere and suppose that the exceptional configuration of the minimal good resolution $\tilde{X} \rightarrow X$ is given by the graph $\Gamma$. A natural $\mathbb{C}^{*}$ -compactification of $X$ is given by $\bar{X}=\operatorname{Proj}(A[u])$, where $u$ has weight 1; what has been added is a curve with $t$ cyclic quotient singularities. Resolving just these singularities of $\bar{X}$ yields the projective variety $\bar{X}^{\prime}$, where one has added to $X$ a curve configuration determined by the dual graph $\Gamma^{\prime}$. (Further resolving on $\bar{X}^{\prime}$ the original singularity thus yields two configurations of rational curves, corresponding to $\Gamma$ and to $\Gamma^{\prime}$, connected by rational -1-curves, and blowing down to a $\mathbb{P}^{1}$-bundle over $\mathbb{P}^{1}$, as in [19].)
A smoothing of negative weight of $X$ (and of its compactifications $\bar{X}$ or $\bar{X}^{\prime}$ ) is a smoothing obtained by adding terms of lower weight to the defining equations, and gives rise to deformations of both compactifications which are topologically locally trivial at $\infty$ (see [28] for details). In particular, such a smoothing of $\bar{X}^{\prime}$ gives a smooth projective surface $Z$ with a curve $D$ of type $\Gamma^{\prime}$, and one has that the Milnor fiber of the smoothing is diffeomorphic to $Z-D$ (e.g., [34, Theorem 2.2]). But under suitable cohomological conditions, there is a converse [28, Theorem 6.7] due to Pinkham: an appropriate pair $(Z, D)$ gives rise to a smoothing of negative weight. We give a special case of Pinkham's result:

Theorem 8.1 Let $Z$ be a smooth projective rational surface, and $D \subset Z$ a union of smooth rational curves whose intersection dual graph is of type $\Gamma^{\prime}$. Assume
$$r k H_{2}(D ; \mathbb{Z})=r k H_{2}(Z ; \mathbb{Z}) .$$
If $\Gamma$ is the graph of a rational singularity, then one has a $\mu=0$ smoothing of a rational weighted homogeneous singularity with resolution dual graph $\Gamma$, and the interior of the Milnor fiber is diffeomorphic to $Z-D$.

Proof By [28, Theorem 6.7] one must check the vanishing of $H^{1}\left(Z, \mathcal{O}\left(E^{(k)}\right)\right)$ for all $k \geq 0$, where the $E^{(k)}$ are effective divisors supported on what we have called $D$, and $E=E^{(1)}$ is the central curve. The case $k=0$ is just the vanishing of the first cohomology of $Z$. We follow Pinkham's notation and arguments closely. The key point is that the traces $D^{(k)}$ of the divisors $E^{(k)}$ on
$E$ are the familiar divisors used to write down the graded pieces of a weighted homogeneous singularity whose resolution dual graph is $\Gamma$; the vanishing of their first cohomology on $E$ is equivalent to the rationality of the singularity [27, Theorem 5.7]. Thus, by the exact sequences
$$0 \rightarrow \mathcal{O}\left(E^{(k)}-E\right) \rightarrow \mathcal{O}\left(E^{(k)}\right) \rightarrow \mathcal{O}_{E}\left(D^{(k)}\right) \rightarrow 0,$$
one needs only the vanishing of $H^{1}\left(Z, \mathcal{O}\left(E^{(k)}-E\right)\right)$ for all $k \geq 1$. Write $F_{k}=E^{(k)}-E^{(k-1)}-E$, for $k \geq 1$; these are reduced but reducible effective divisors, supported on the chains of rational curves emanating from $E$. Via the exact sequences
$$0 \rightarrow \mathcal{O}\left(E^{(k-1)}\right) \rightarrow \mathcal{O}\left(E^{(k)}-E\right) \rightarrow \mathcal{O}_{F_{k}}\left(E^{(k)}-E\right) \rightarrow 0,$$
one can proceed inductively from the case $k=1$, reducing the claimed vanishing to showing that $H^{1}\left(F_{k}, \mathcal{O}_{F_{k}}\left(E^{(k)}-E\right)\right)=0$ for all $k \geq 1$. A proof is indicated in [28, Lemma 6.9]; or, one can argue directly with the resolutions of the cyclic quotient singularities whose resolution graphs contain the support of the $F_{k}$. \(\square\)

Remark 8.2 Note that the hypothesis rk $H_{2}(D ; \mathbb{Z})=\operatorname{rk} H_{2}(Z ; \mathbb{Z})$, without the assumption on the rationality of the graph $\Gamma$, gives directly that $Z-D$ is a rational homology disk whose boundary is the link associated to $\Gamma$; one does not need anything about singularities.

We will describe pairs $(Z, D)$ by blowing up appropriately certain curves $C \subset$ $\mathbb{C P}^{2}$, then taking $D$ a subset of the total transform of $C$. Infinite families will come from systematically continuing the blow-up procedure.

Example 8.3 [Graphs in the family $\mathcal{M}$ ] Let $C=C_{1} \cup C_{2} \cup L_{1} \cup L_{2}$ be a plane curve of degree 6, where
\begin{itemize}
\item[(1)] $C_{1}$ and $C_{2}$ are smooth conics with a triple tangency at one point
\item[(2)] $L_{1}$ is the line joining the two intersection points.
\item[(3)] $L_{2}$ is the tangent line to $C_{1}$ at the simple intersection point with $C_{2}$.
\end{itemize}
Blowing-up appropriately 8 times yields a smooth surface $Z$, so that the total transform of $C$ has the dual configuration:
![](https://cdn.mathpix.com/cropped/df5f5431-21ef-431b-b837-d2c96a8445b9-47.jpg?height=420&width=820&top_left_y=464&top_left_x=707)

Here, solid unweighted vertices • denote (-2)-curves, while circle vertices are (-1)'s. Proper transforms of the components of $C$ are labeled as before. One recovers the blow-up procedure by blowing down sequentially first $e_{8}$, then $e_{7}$, etc. Let $\Gamma^{\prime}$ be the configuration obtained by deleting the vertices $e_{6}, L_{1}$, and $e_{8}$; it has rank 9 ( $=\mathrm{rk} H_{2}(Z ; \mathbb{Z})$ ), and is dual to the basic configuration
![](https://cdn.mathpix.com/cropped/df5f5431-21ef-431b-b837-d2c96a8445b9-47.jpg?height=180&width=248&top_left_y=1305&top_left_x=1006)
Thus, this construction gives a rational homology disk bounding the corresponding $\Sigma$. But one can repeatedly blow-up further, between $e_{2}$ and $L_{1}$, and then between the transform of $e_{2}$ and its new neighbour. The same idea works between $e_{4}$ and $e_{6}$ (and again between the transform of $e_{4}$ and the new exceptional curves), as well as between $C_{2}$ and $e_{8}$. Doing this respectively $p, q$, and $r$ times, the new exceptional diagram is
![](https://cdn.mathpix.com/cropped/df5f5431-21ef-431b-b837-d2c96a8445b9-47.jpg?height=586&width=1029&top_left_y=1846&top_left_x=600)

To reverse the process, blow down sequentially the $f_{i}, g_{i}, h_{i}$ starting from the largest subscript (and define $f_{0}=L_{1}, g_{0}=e_{6}, h_{0}=e_{8}$ ). The graph $\Gamma^{\prime}$ obtained by deleting the -1 curves $f_{p}, g_{q}$, and $h_{r}$ is
![](https://cdn.mathpix.com/cropped/df5f5431-21ef-431b-b837-d2c96a8445b9-48.jpg?height=300&width=1136&top_left_y=647&top_left_x=518)
It is easy to calculate that the dual graph $\Gamma$ is of type $\Lambda_{q, r, p}$. (We leave it to the reader to check the special cases when some of the $p, q, r$ are 0.) This gives the desired boundaries for all graphs of type $\mathcal{M}$.

Example 8.4 [Graphs in the families $\mathcal{W}$ and $\mathcal{N}$ ] A similar construction, starting with $C$ the union of 4 lines $L_{1}, L_{2}, L_{3}, L_{4}$ in general position in $\mathbb{C P}^{2}$, yields rational homology ball smoothings for the triply-infinite families of type $\mathcal{W}$ and $\mathcal{N}$. For the (3,3,3) type $\mathcal{W}$, blow-up 6 times, giving
![](https://cdn.mathpix.com/cropped/df5f5431-21ef-431b-b837-d2c96a8445b9-48.jpg?height=359&width=523&top_left_y=1331&top_left_x=861)
Blowing up $p$ additional times between $L_{4}$ and $e_{6}$ and successor $(-1)$-curves, $q$ times between $L_{3}$ and $e_{5}$, and $r$ times between $L_{2}$ and $e_{4}$, and then removing the three (-1)-curves, gives a $\Gamma^{\prime}$ which is easily checked to be dual to $\Gamma_{p, q, r}$.
For the (2,4,4) type $\mathcal{N}$, blow up 7 times, yielding
![](https://cdn.mathpix.com/cropped/df5f5431-21ef-431b-b837-d2c96a8445b9-48.jpg?height=417&width=723&top_left_y=1931&top_left_x=760)
(The self-intersection of $L_{3}$ is 0.) Blowing up $p$ additional times between $L_{1}$ and $e_{4}$ and successor (-1)-curves, $q$ times between $L_{2}$ and $e_{7}$, and $r$ times between $L_{4}$ and $e_{5}$, and then removing the three (-1)-curves, gives $\Gamma^{\prime}$ which is easily checked to be dual to $\Delta_{p, q, r}$.

Remark 8.5 How would one come up with such a configuration, obtainable by blowing up curves in $\mathbb{C P}^{2}$, given a star-shaped candidate $\Gamma$ ? One first forms $\Gamma^{\prime}$ as above. The lattice generated by the vertices is supposed to have a finite overlattice which is the second homology of a surface $Z$; this must be the unimodular odd lattice with signature $(1, n-1)$, where $n$ is the number of curves in $\Gamma^{\prime}$. In particular, generators of the overlattice are certain rational combinations of the vertices in $\Gamma^{\prime}$, and the class $K$ of a canonical divisor is also such a combination. To find suitable rational (-1)-curves on the putative $Z$, one looks for elements $e$ of the overlattice for which $e \cdot e=-1, K \cdot e=-1$, and which intersect exactly two curves in $\Gamma^{\prime}$ (or intersects one curve twice). One might be able to use some of these to produce a configuration which blows down. This approach has succeeded in a number of cases, including all the ones in the above examples. We present two more, of type $\mathcal{C}$, though there are quite a few others.

Example 8.6 [A family in $\mathcal{C}$ ] Next we give an infinite family of graphs in $\mathcal{C}$ which arise from normal surface singularities which admit rational homology disk smoothings. Let $C=C_{1} \cup C_{2}$ be a plane curve of degree 5, where $C_{1}$ is an irreducible nodal cubic, and $C_{2}$ is a smooth quadric intersecting $C_{1}$ in only one point (hence, with intersection multiplicity 6). An affine version of such a curve is
$$\left(y^{2}-x(1-x)^{2}\right)\left(y^{2}-x(1-2 x)\right)=0 .$$
Blowing up appropriately 8 times yields a smooth surface for which the total transform of $C$ has dual configuration
![](https://cdn.mathpix.com/cropped/df5f5431-21ef-431b-b837-d2c96a8445b9-49.jpg?height=199&width=750&top_left_y=2049&top_left_x=710)
Blowing up $p$ additional times between $C_{1}$ and $e_{3}$ and its successor ( -1 )'s,
and then removing the last (-1)-curve, gives $\Gamma^{\prime}$
![](https://cdn.mathpix.com/cropped/df5f5431-21ef-431b-b837-d2c96a8445b9-50.jpg?height=200&width=1039&top_left_y=568&top_left_x=566)
The dual graph $\Gamma$ in this case is of type $\mathcal{C}$, and is
![](https://cdn.mathpix.com/cropped/df5f5431-21ef-431b-b837-d2c96a8445b9-50.jpg?height=186&width=587&top_left_y=897&top_left_x=736)
Thus, this graph corresponds to a singularity with a $\mu=0$ smoothing.

Example 8.7 [A family in $\mathcal{C}$ with a 4-valent node] We finish this subsection by constructing an infinite family of graphs of type $\mathcal{C}$ with one node of valency 4 , which arise from a rational homology disk smoothing of negative weight. We thank E. Shustin for assistance with this example.

We consider four conics in the plane, all contained in the real unit circle:
$$\begin{array}{rlr}
F & = & \left\{x^{2}+y^{2}-1=0\right\} \\
G & = & \left\{x^{2}+y^{2}-1+(1 / 2)(x+1)(y+1)=0\right\} \\
H & = & \left\{x^{2}+y^{2}-1-(3 / 4)\left(x^{2}-1\right)=0\right\} \\
J & = & \left\{x^{2}+y^{2}-1-(1 / 2)(x-1)(y+1)=0\right\} .
\end{array}$$
Relevant intersection points are (1, 0), where $F, H, J$ are pairwise tangent; (-1, 0), where $F, G, H$ are pairwise tangent; (0, 1/2), through which $G, H, J$ pass transversally; and (0, -1), where $G$ and $J$ have a triple tangency, and $F$ has a simple tangency with each of them. Let $L$ be the common tangent line $y=-1$. There are two further important points: $H$ and $J$ also meet transversally at $(-3 / 5,-2 / 5)$, which lies on the straight line $M$ through $(-1,0)$ and (0, -1); and finally $H$ and $G$ meet transversally at (3/5, -2/5), which lies on the straight line $N$ through $(1,0)$ and (0, -1).

We now consider the (complex) plane curve which is the union of the 4 conics $F, G, H, J$ and three lines $L, M, N$, and blow up minimally so that the reduced total transform has only normal crossings. We finally blow up either of the

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/df5f5431-21ef-431b-b837-d2c96a8445b9-51.jpg?height=553&width=995&top_left_y=445&top_left_x=588}
\captionsetup{labelformat=empty}
\caption{Figure 21: The configuration of curves after 11 blow-ups; solid circles represent (-2)-curves, the empty ones (-1)-curves, the ones with a cross correspond to (-3)-curves, while $H \cdot H=-4$}
\end{figure}
two intersection points of the line $L$ and the conic $H$ (which are in the imaginary complex plane). We reach the diagram of Figure 21, where the proper transforms of the seven curves in the plane are given the same name.

Again, blowing down the curves $e_{i}$ starting from the largest subscript will show how to reverse the procedure. Now, removing the vertices $e_{1}, e_{2}, e_{3}, e_{7}$ and $e_{9}$ from the diagram, and then blowing down the $(-1)$-curve $e_{10}$, yields the simpler diagram of Figure 22.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/df5f5431-21ef-431b-b837-d2c96a8445b9-51.jpg?height=452&width=1004&top_left_y=1674&top_left_x=513}
\captionsetup{labelformat=empty}
\caption{Figure 22: The configuration of Figure 21 after blow-ups ( $e_{5}$ and $e_{11}$ are (-1)-curves while $H$ is a (-4)-curve)}
\end{figure}

It is clear that removing $e_{11}$ gives a curve configuration whose components span the second rational homology group of the blown-up plane (recall that $e_{10}$ has been blown down, so after deleting $e_{11}$, the remaining eleven curves are in $\mathbb{C P}^{2} \# 10 \overline{\mathbb{C P}^{2}}$ ). Furthermore, the resulting $\Gamma^{\prime}$ is dual to the graph of a rational singularity, hence one can apply Theorem 8.1. Blowing up further between $H$ and $e_{11}$, and then removing the exceptional curve yield rational homology disk smoothings of negative weight of singularities with resolution graph
![](https://cdn.mathpix.com/cropped/df5f5431-21ef-431b-b837-d2c96a8445b9-52.jpg?height=285&width=649&top_left_y=943&top_left_x=818)
(In the case $p=0$ one has to blow down $e_{11}$ and remove the curve $L$.)

\subsection*{8.2 Examples of $\mu=0$ smoothings via quotients}

Finally we show a second algebro-geometric way for constructing smoothings with $\mu=0$. Besides discussing the (already familiar) cases we have dealt with in the previous subsection, there will be some families of singularities (with resolution graphs in $\mathcal{A} \cup \mathcal{B}$ ) which can be treated in this way. We will show further examples of graphs involving nodes with valency 4 giving rise to singularities with rational homology disk smoothing. Let us start by describing the general strategy first.

Suppose $(\mathcal{Y}, o)$ is the germ of an isolated 3-dimensional normal singularity, $G$ a finite group of automorphisms acting freely off $o$, and $f \in \mathcal{O}_{\mathcal{Y}, o}$ a $G-$invariant function whose zero locus $(Y, o)$ has an isolated normal singularity. (This implies that $\mathcal{Y}$ is Cohen-Macaulay.) Then $f$ defines a smoothing of $(Y, o)$, with Milnor fiber $M_{Y}$; but it also defines a smoothing of $X=Y / G$, whose Milnor fiber $M_{X}$ is the quotient of the free action of $G$ on $M_{Y}$. In particular
$$\chi\left(M_{Y}\right)=|G| \cdot \chi\left(M_{X}\right) .$$
Consequently, if $|G|=\chi\left(M_{Y}\right)=1+\mu_{Y}$, then $\chi\left(M_{X}\right)=1$ and so we have constructed a smoothing of $X$ with Milnor number $\mu_{X}=0$.

In the following, we will denote by $(1 / m)\left[a_{1}, \cdots, a_{n}\right]$ the transformation of $\mathbb{C}^{n}$ which is multiplication of the $j$ th coordinate by $\exp \left(2 \pi i a_{j} / m\right)$ (where $a_{j} \in \mathbb{Z}$ ). All examples below are weighted homogeneous, simplifying calculations. It is easy to check that a given group action is free on $\mathcal{Y}-\{o\}$. Describing the resolution graph of $X$ is achieved by lifting the action of $G$ to the weighted blow-up of $Y$, then dividing and resolving the quotient, cf. [18, Section 8]. One needs to compute the Milnor number $\mu_{Y}$ for $Y$ in order to show that it satisfies $1+\mu_{Y}=|G|$. But, in our examples $Y$ is a complete intersection defined by one or two weighted homogeneous equations, so one can easily apply [9, Korollar 3.10(a) or (c)].

Example 8.8 [Graphs in $\mathcal{G}]$ Let us start with the case of the standard rational blow-down along $L\left(p^{2}, p q-1\right)$ (cf. also [34, (5.9.1)]). Suppose $0<$ $q<p,(q, p)=1$. Let $(\mathcal{Y}, o)=\left(\mathbb{C}^{3}, o\right), G$ the cyclic group generated by $(1 / p)[1, q,-1]$, and $f=x z-y^{p}$. Then one gets $\mu=0$ smoothings of $X$, the cyclic quotient singularity of type $p^{2} /(p q-1)$, whose resolution graph is a chain as in Definition 1.3. The Milnor fiber is a free quotient of the (simply connected) Milnor fiber of the $A_{p-1}$-singularity $x z-y^{p}=0$.

The three basic graphs of Figure 1 (Section 5), corresponding to the spherical triples (3, 3, 3), (2, 4, 4), (2, 3, 6), are resolution graphs of certain log-canonical surface singularities; each is the quotient of a simple elliptic singularity (i.e., cone over an elliptic curve) by a cyclic group acting freely off the singular point. As mentioned in the Introduction, each gives rise to a triply-infinite family of singularities having a smoothing with Milnor number 0, and these examples fill out the classes $\mathcal{W}, \mathcal{N}$, and $\mathcal{M}$.

Example 8.9 [Graphs in $\mathcal{W}$ ] We apply the above principle to graphs of type $\mathcal{W}$; the following is exactly [34, Example (5.9.2)]. Suppose $p, q, r \geq 0$, and let $N=(p+2)(q+2)(r+2)+1$. Let $(\mathcal{Y}, o)=\left(\mathbb{C}^{3}, o\right), G$ the cyclic group generated by $(1 / N)[1,(q+2)(r+2),-(r+2)]$, and $f=x y^{p+2}+y z^{q+2}+z x^{r+2}$. Then one gets $\mu=0$ smoothings of rational singularities whose resolution graphs we claim are the $\Gamma_{p, q, r}$ as in Figure 3. The Milnor fiber has fundamental group $G$.

We indicate how to find the quotient graph $\Gamma$. Give the variables $x, y, z$ weights $a, b, c$, respectively, where $a=(p+2)(q+1)+1, b=(q+2)(r+1)+1, c=$ $(r+2)(p+1)+1$; this makes $f$ weighted homogeneous, of weight $N$. Since $G$ preserves weights, the quotient is still weighted homogeneous; and it is rational, with discriminant group of order $N^{2}$ (by Proposition 2.4). We show that the graph $\Gamma$ of the quotient has three chains of rational curves, corresponding to the continued fractions (from the outside to the center) $a /(q+1), b /(r+1), c /(p+1)$.

This will give $\Gamma_{p, q, r}$, except that the central self-intersection of -4 is deduced at the end from the calculation of the discriminant order.

Use the weights $a, b, c$ to do a weighted blow-up of $\mathbb{C}^{3}$, as in [18, Section 4]. This space is covered by three open sets. The first is the quotient of a copy of $\mathbb{C}^{3}$, with coordinates $u, v, w$, modulo the cyclic action of $S=(1 / a)[-1, b, c]$, and the coordinates are related by $x=u^{a}, y=u^{b} v, z=u^{c} w$. The proper transform of $f=0$ is checked to be the smooth surface given by $v^{p+2}+v w^{q+2}+w=0$. A lifting of the the generator of $G$ to this $\mathbb{C}^{3}$ is $T=(1 / a N)[1, q+1,-1]$; one divides the smooth surface by the group generated by $T$ and $S$. But $T^{N}$ is computed to be the inverse of $S$, so one only needs to divide by $T$. Further, $T^{a}=(1 / N)[1,0,0]$ is a pseudo-reflection; so one divides out first by this transformation, replacing the variable $u$ by $u^{\prime}=u^{N}$. Thus, in the $u^{\prime}, v, w$ space, one has the smooth surface $v^{p+2}+v w^{q+2}+w=0$, and a cyclic group action generated by $(1 / a)[1, q+1,-1]$. The only fixed point occurs at $u^{\prime}=v=w=0$; at such a point, $u^{\prime}$ and $v$ are local analytic coordinates, and one divides out by the group $(1 / a)[1, q+1]$. The image of $u^{\prime}=0$ is the central rational curve, so the continued fraction expansion of $a /(q+1)$ goes from the outer curve into the central curve. This is the cyclic quotient singularity claimed above.

Example 8.10 [Graphs in $\mathcal{N}$ ] Suppose now that $p, q, r \geq 0$, and let us define $N=(p+1)(q+3)(r+2)+q+2$. Let $(\mathcal{Y}, o) \subset\left(\mathbb{C}^{4}, o\right)$ be the hypersurface singularity given by the equation $\left(x^{q+2}+z^{r+2}-y w=0\right), G$ the cyclic group generated by $(1 / N)[1,(q+3),-(p+1)(q+3),-1]$, and $f=x w-y^{p+1} z$. Then one gets $\mu=0$ smoothings of rational singularities with resolution graph $\Delta_{p, q, r}$ as in Figures 4 and 5. The Milnor fiber has fundamental group $G$.

Example 8.11 Embed the plane cubic curve $A^{3}+B^{3}-A C^{2}=0$ into $\mathbb{C P}^{5}$ via the Veronese embedding
$$[A, B, C] \mapsto\left[x_{0}, x_{1}, x_{2}, y_{0}, y_{1}, y_{2}\right] \equiv\left[A^{2}, B^{2}, C^{2}, B C, A C, A B\right],$$
and let $Y \subset \mathbb{C}^{6}$ be the affine cone. Let $\mathcal{Y}$ be the total space of the oneparameter smoothing (with parameter $T$ ) of $Y$, given $Y$ is defined by 9 equations, as in [26, (9.6)], and a 1-parameter smoothing (with parameter $T$ ) is given by the vanishing of the nine expressions
$$\begin{aligned}
& x_{0} x_{1}-y_{2}^{2}+T y_{1} \\
& x_{1} x_{2}-y_{0}^{2}+T y_{1} \\
& x_{0} x_{2}-y_{1}^{2}+T y_{0}
\end{aligned}$$
$$\begin{gathered}
x_{0} y_{0}-y_{1} y_{2}+T x_{1} \\
x_{1} y_{1}-y_{0} y_{2}+T x_{0} \\
x_{2} y_{2}-y_{0} y_{1}+T^{2} \\
x_{0}^{2}+x_{1} y_{2}-y_{1}^{2} \\
x_{1}^{2}+x_{0} y_{2}-y_{0} y_{1} \\
x_{1} y_{0}+x_{0} y_{1}-x_{2} y_{1}-T y_{2} .
\end{gathered}$$
(This requires some checking, but easily follows as in [26, (9.6)].) The cyclic group $G$ of order 6, acting on the $X_{i}, Y_{j}, T$ via $(1 / 6)[1,3,1,2,4,5,0]$, acts freely off the origin of $\mathcal{Y} . T$ is $G$-invariant, and $Y \bmod G$ is the by-now-familiar singularity with resolution graph
![](https://cdn.mathpix.com/cropped/df5f5431-21ef-431b-b837-d2c96a8445b9-55.jpg?height=183&width=250&top_left_y=1118&top_left_x=1003)
The Milnor fiber of $Y$ is simply connected, with Euler characteristic 6; so, one has a $\mu=0$ smoothing of $X$, whose Milnor fiber has fundamental group $G$.

Example 8.12 [A family of graphs in $\mathcal{A}$ ] Let $p \geq 0$, and for convenience write $m=3 p^{2}+9 p+7, r=3 p^{2}+6 p+2=m-(3 p+5), n=9(p+2)$ and $a=$ $3 p+5$. Consider the metacyclic group $G \subset G L(3, \mathbb{C})$, acting freely on $\mathbb{C}^{3}-\{0\}$, generated by $S=(1 / m)\left[1, r, r^{2}\right]$ and $T$ defined by $T(x, y, z)=(y, z, \omega x)$, where $\omega=\exp (2 \pi i /(a+1))$. One easily finds that $S^{m}=T^{n}=I, T S T^{-1}=S^{r}$, and $T^{3}$ is multiplication by $\omega$. Further, $G /[G, G]$ is cyclic of order $n$, generated by the image of $T$, and $|G|=m n$. Let $\mathcal{Y}=\mathbb{C}^{3}$, and $f=x^{a} y+y^{a} z+\omega x z^{a}$. Then $f$ is $G$-invariant, and defines a hypersurface singularity $Y$ whose Milnor fiber has Euler characteristic $1+a^{3}=m n=|G|$. Thus, one gets a $\mu=0$ smoothing of a rational singularity whose resolution graph has valency 4:
![](https://cdn.mathpix.com/cropped/df5f5431-21ef-431b-b837-d2c96a8445b9-55.jpg?height=277&width=687&top_left_y=2083&top_left_x=799)

To find the resolution graph, let $\bar{G}$ be the image of $G$ in $P G L(3, \mathbb{C})$ (modding out by $T^{3}$ ), and locate the orbits in the projective plane curve defined by $f$ on which $\bar{G}$ acts with non-trivial isotropy. Then, resolve the hypersurface singularity via one blow-up, divide out by $T^{3}$, and find and describe the fixed points of $\bar{G}$ on this smooth surface. One finds three orbits on which every point has isotropy of order 3; and 3 points where the isotropy is generated by $S$, and the image of $T$ puts them into one $\bar{G}$-orbit. Dividing out then gives all the information on the resolution, except for the weight of the central curve; this can be computed by noting that the discriminant group has order $n^{2}$.

Since the Milnor fiber of $Y$ is simply connected, the fundamental group of the $\mu=0$ Milnor fiber is the non-abelian group $G$. (This perhaps explains why this example, originally discovered in 1983, was surprising - a Seifert manifold with 4 branches which bounds a rational homology ball.) Note that this example is of type $\mathcal{A}$.

Remark 8.13 There are very few "interesting" subgroups of $G L(3, \mathbb{C})$ which act freely off the origin, see [35].

Example 8.14 [A family in $\mathcal{B}$ ] Let $p \geq 2$, and for convenience write $m=2 p^{2}-2 p-1, r=2(p-1)^{2}, n=8 p, a=2 p-1$. Consider the group $G \subset G L(4, \mathbb{C})$, generated by $S=(1 / m)[1, r,-1,-r]$ and $T$ defined by $T(x, y, z, w)=\left(\eta^{4} w, x, y, z\right)$, where $\eta=\exp (2 \pi i / 4 n)$. One easily finds that $S^{m}=T^{n}=I, T^{-1} S T=S^{r}$, and $T^{4}$ is multiplication by $\eta^{4}$. Again, $G /[G, G]$ is cyclic of order $n$, generated by the image of $T$, and $|G|=m n$. Let $\mathcal{Y}=\left\{x z+\eta^{2} y w=0\right\} \subset \mathbb{C}^{4}$, on which $G$ can be checked to act freely off the origin. Then $f=x^{a} y+y^{a} z+z^{a} w+\eta^{4 a} w^{a} x$ is $G$-invariant, and defines a complete intersection singularity $Y$ whose Milnor fiber has Euler characteristic $m n=|G|$. Thus, one gets a $\mu=0$ smoothing of a rational surface singularity. The same approach as above (first finding fixed points of some $\bar{G}$ on the projective curve) yields that the resolution graph of the singularity is
![](https://cdn.mathpix.com/cropped/df5f5431-21ef-431b-b837-d2c96a8445b9-56.jpg?height=277&width=687&top_left_y=2112&top_left_x=799)

\section*{9 Appendix: Embeddings of graphs in $\mathcal{W} \cup \mathcal{M} \cup \mathcal{N}$ into diagonal lattices}

In this final section we explicitely describe embeddings of the graphs in $\mathcal{W} \cup$ $\mathcal{M} \cup \mathcal{N}$ into diagonal lattices of equal rank. Formally, these embeddings verify one direction of the equivalence in Theorem 1.8 - although this is the 'less interesting' direction of the theorem.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/df5f5431-21ef-431b-b837-d2c96a8445b9-57.jpg?height=449&width=1005&top_left_y=825&top_left_x=585}
\captionsetup{labelformat=empty}
\caption{Figure 23: The embedding of the graph $\Gamma_{p, q, r} \in \mathcal{W}$ into the diagonal lattice; here $C=E_{1}-F_{1}-G_{1}-H_{1}, P=E_{2}-E_{1}-E_{3}-H_{p}-\ldots-H_{1}, Q=$ $E_{3}-E_{1}-E_{4}-G_{q}-\ldots-G_{1}, R=E_{4}-E_{1}-E_{2}-F_{r}-\ldots-F_{1}$ (where the basis of the diagonal lattice is given by $\left\{E_{1}, \ldots, E_{4}, F_{1}, \ldots, F_{r}, G_{1}, \ldots, G_{q}, H_{1}, \ldots, H_{p}\right\}$ )}
\end{figure}

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/df5f5431-21ef-431b-b837-d2c96a8445b9-57.jpg?height=152&width=1276&top_left_y=1571&top_left_x=448}
\captionsetup{labelformat=empty}
\caption{Figure 24: The embedding of the graph $\Delta_{p, q, r}$ in for $p \geq 1$ and $q, r \geq 0$; here $C=E_{1}-G_{1}-H_{1}, D=H_{q+1}-E_{3}-F_{1}, P=E_{3}-E_{1}-E_{2}-F_{p-1}-\ldots-F_{1}, Q=$ $E_{4}-E_{1}-E_{3}-H_{q+1}-\ldots-H_{1}$ and $R=E_{2}-E_{1}-E_{4}-G_{r}-\ldots-G_{1}$. The basis in the diagonal lattice is now $\left\{E_{1}, \ldots, E_{4}, F_{1}, \ldots, F_{p-1}, G_{1}, \ldots, G_{r}, H_{1}, \ldots, H_{q+1}\right\}$}
\end{figure}

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/df5f5431-21ef-431b-b837-d2c96a8445b9-58.jpg?height=173&width=1002&top_left_y=645&top_left_x=585}
\captionsetup{labelformat=empty}
\caption{Figure 25: The embedding of the graph $\Delta_{0, q, r} ; C=E_{1}-G_{1}-H_{1}, Q=$ $E_{4}-E_{1}-E_{2}-E_{4}-H_{q}-\ldots-H_{1}, R=E_{3}-E_{1}-E_{2}-E_{4}-G_{r}-\ldots-G_{1}$ (the basis in the diagonal lattice is now $\left\{E_{1}, \ldots, E_{4}, G_{1}, \ldots, G_{r}, H_{1}, \ldots, H_{q}\right\}$ )}
\end{figure}

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/df5f5431-21ef-431b-b837-d2c96a8445b9-58.jpg?height=587&width=1370&top_left_y=1231&top_left_x=356}
\captionsetup{labelformat=empty}
\caption{Figure 26: The embedding of the graph $\Lambda_{p, q, r}$ for $p, r \geq 1$ and $q \geq 0$; here $C=E_{1}-H_{1}, D_{1}=H_{q+1}-G_{1}-E_{3}, D_{2}=G_{r}-F_{1}-E_{2}, P=E_{2}-$ $E_{1}-E_{4}-F_{p-1}-\ldots-F_{1}, Q=E_{4}-E_{1}-E_{3}-H_{q+1}-\ldots-H_{1}, R=$ $E_{3}-E_{1}-E_{2}-G_{r}-\ldots-G_{1}$}
\end{figure}

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/df5f5431-21ef-431b-b837-d2c96a8445b9-59.jpg?height=169&width=1189&top_left_y=621&top_left_x=514}
\captionsetup{labelformat=empty}
\caption{Figure 27: The embedding of the graph $\Lambda_{0, q, r}$ for $r \geq 1$ and $q \geq 0 ; C=$ $E_{1}-H_{1}, D=H_{q+1}-E_{3}-G_{1}, Q=E_{3}-E_{1}-E_{4}-E_{2}-H_{q+1}-\ldots-H_{1}$, $R=E_{4}-E_{1}-E_{3}-E_{2}-G_{r-1}-\ldots-G_{1}$}
\end{figure}

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/df5f5431-21ef-431b-b837-d2c96a8445b9-59.jpg?height=173&width=1142&top_left_y=1571&top_left_x=515}
\captionsetup{labelformat=empty}
\caption{Figure 28: The embedding of the graph $\Lambda_{p, q, 0}$ for $p \geq 1$ and $q \geq 0 ; C=$ $E_{1}-H_{1}, D=H_{q+1}-E_{2}-E_{3}-F_{1}, P=E_{2}-E_{1}-E_{4}-F_{p-1}-\ldots-F_{1}$, $Q=E_{4}-E_{1}-E_{3}-H_{q+1}-\ldots-H_{1}$}
\end{figure}
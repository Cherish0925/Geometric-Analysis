---
retention_scope: session
part: 2
total_parts: 2
---

[Part 2/2 of: DEHN SURGERIES AND RATIONAL HOMOLOGY BALLS]

Third subcase: $n \in\left\{k q^{2}+q-1, k q^{2}+q, k q^{2}+q+1\right\}$.
Suppose $n=p q=k q^{2}+q$, then we have
$$S_{k q^{2}+q}^{3}\left(T_{k q+1, q}\right) \cong-L(k q+1, q) \#-L(q, k q+1) \cong-L(k q+1, q) \#-L(q, 1) .$$
It follows from [14] that this manifold bounds a rational homology ball if and only if $q=4$ and $k \in\{2,6\}$. These values correspond to the triples (25, 4; 100) and (9, 4; 36). Recall that $S_{p q \pm 1}^{3}\left(T_{p, q}\right)=-L\left(p q \pm 1, q^{2}\right)$. It follows that when $n=p q \pm 1=k q^{2}+q \pm 1$ we have
$$S_{k q^{2}+q \pm 1}^{3}\left(T_{k q+1, q}\right)=-L\left(k q^{2}+q \pm 1, q^{2}\right) .$$
According to [14] if this lens space bounds a $\mathbb{Q} H B^{4}$ then $-3 \leq I\left(\frac{k q^{2}+q+1}{q^{2}}\right) \leq 1$. It follows from Lemma 6.8 that $I\left(\frac{k q^{2}+q+1}{q^{2}}\right)=k-1$, and therefore we may assume that $k=2$. Again by Lemma 6.8 the positive plumbing graph associated to $L\left(2 q^{2}+q+1, q^{2}\right)$ can be depicted as
![](https://cdn.mathpix.com/cropped/72ba5561-4a2e-4e16-9100-e636a5a592d5-26.jpg?height=142&width=655&top_left_y=2207&top_left_x=734)
It is easy to check that the corresponding integral lattice does not embed (start with the 2-chain and then examine the vector whose square is 3). In order to conclude we need
to the study the family of lens spaces $L\left(k q^{2}+q-1, q^{2}\right)$. By Lemma 6.8 the positive plumbing graph corresponding to $-L\left(k q^{2}+q-1, q^{2}\right)$ can be depicted as
![](https://cdn.mathpix.com/cropped/72ba5561-4a2e-4e16-9100-e636a5a592d5-27.jpg?height=140&width=659&top_left_y=427&top_left_x=733)
The dual of this linear graph is
![](https://cdn.mathpix.com/cropped/72ba5561-4a2e-4e16-9100-e636a5a592d5-27.jpg?height=143&width=919&top_left_y=684&top_left_x=602)
Recall that we may assume $k \notin\{1,4\}$ and $q>2$. If $(k, q) \notin\{(2,3),(2,5)\}$ the integral lattice which corresponds to the above graph does not embed by Lemma 6.7.

If $(k, q)=(2,3)$ the surgery coefficient is 20, and if $(k, q)=(2,5)$ it is 54; in neither case is it a square, hence the corresponding 3-manifolds do not bound.

Second case: $p=k q-1$. By Theorem 1.3 we may assume that $k \leq 9$. Note that $p^{*}=q-1$ and $q^{*}=k$. We obtain
$$S_{n}^{3}\left(T_{k q-1, q}\right)=Y\left(2 ; \frac{k q-1}{k}, \frac{q}{q-1}, \frac{k q^{2}-q-n}{k q^{2}-q-n-1}\right) .$$
Just like in the first case we split the proof according to the following possibilities:
\begin{itemize}
\item[(1)] $n>p q+1=k q^{2}-q+1$;
\item[(2)] $n<p q-1=k q^{2}-q-1$;
\item[(3)] $n \in\left\{k q^{2}-q-1, k q^{2}-q, k q^{2}-q+1\right\}$.
\end{itemize}

First subcase: $n>p q+1=k q^{2}-q+1$.
The positive canonical plumbing graph for $S_{n}^{3}\left(T_{k q-1, q}\right)$, described in Proposition 6.6, is indefinite. By taking the dual of this graph, i.e. by considering the positive canonical plumbing graph of $-S_{n}^{3}\left(T_{k q-1, q}\right)$, we obtain a positive definite plumbing graph. It can be written as
![](https://cdn.mathpix.com/cropped/72ba5561-4a2e-4e16-9100-e636a5a592d5-27.jpg?height=439&width=1065&top_left_y=1905&top_left_x=529)
This graph has two 2-chains: the first has length $N_{1}=\left(n-k q^{2}+q-1\right)+1+(q-2)$, which is at least 3 since all summands are positive; the second has length $N_{2}=k-2$.

Observe that $N_{1}=3$ only if $q=3$ and $n=p q+2$, in which case $n$ can never be a square since 2 is not a quadratic residue mod 3. We can then assume that $N_{1}>3$, and that the vectors in the corresponding chain are
$$e_{1}+e_{2}, \ldots, e_{n-k q^{2}+q}+e_{n-k q^{2}+q+1}, \ldots, e_{N_{1}}+e_{N_{1}+1}$$
where $e_{n-k q^{2}+q}+e_{n-k q^{2}+q+1}$ corresponds to the central vertex of the plumbing graph. As in the proof of Lemma 6.7, the second 2-chain can be written as
$$e_{N_{1}+2}+e_{N_{1}+3}, \ldots, e_{N_{1}+N_{2}+1}+e_{N_{1}+N_{2}+2}$$
since it is easy to exclude the exceptional embedding $\left\{e_{1}+e_{2}, e_{1}+e_{3}, e_{1}-e_{2}\right\}$ when $N_{2}=3$. Note that in the above expressions for the 2-chains we already used all the available basis vectors. Call $v$ the vector whose square is 3. Clearly $v$ must hit at least two basis vectors which appear in the same 2-chain. If $v$ hits more than one basis vector appearing in a 2-chain then it hits all the basis vectors in that chain. It follows that $N_{2}=2$, i.e. $k=4$.

Call $w$ the vector whose square is $q$. The top portion of the 2 -chain linked to $w$ involves $q-1$ basis vectors. It follows that $w$ must hit some basis vector in the bottom portion of 2-chain, and therefore all of them. This implies that $w$ does not hit any basis vector in the top portion of the two chain (we would have $w \cdot w>q$ ). Therefore $n-k q^{2}+q=q$, i.e. $n=4 q^{2}$. The surgered manifold is
$$Y\left(2 ; \frac{4 q-1}{4 q-5}, q, \frac{q}{q-1}\right) .$$
By Lemma 6.2 these manifolds are rational homology cobordant to $L(4,1)$, and therefore to $S^{3}$. They correspond to the triples $\left(4 q-1, q ; 4 q^{2}\right)$.

Second subcase: $n<p q-1$.
The positive canonical plumbing graph of $S_{n}^{3}\left(T_{k q-1, q}\right)$ may be written as
![](https://cdn.mathpix.com/cropped/72ba5561-4a2e-4e16-9100-e636a5a592d5-28.jpg?height=370&width=477&top_left_y=1644&top_left_x=824)
This graph is positive definite.
If $k=2$ this graph does not embed, by Lemma 6.7; in fact, since $q \geq 3$, the above graph contains a 2-chain whose length is at least 4. As usual the vectors belonging to this 2-chain may be written as
$$e_{1}+e_{2}, \ldots, e_{q}+e_{q+1}, \ldots, e_{k q^{2}-n-1}+e_{k q^{2}-n},$$
where $e_{q}+e_{q+1}$ corresponds to the central vertex of the graph. Note that we can only use one more basis vector to write down the image of the vectors with weights $q$ and $k$. Let us denote these vectors as $v_{1}$ and $v_{2}$. Let us also put $N=k q^{2}-q-n$.

If $k=3$ we must have $v_{2} \cdot e_{i}=0$ for each $i \leq N$. It follows that $v_{2}=\alpha e_{N+1}$, which is impossible because $v_{2} \cdot v_{2}=k=3$ is not a square.

If $k=5$ either we may apply the same argument as above or the length of the 2-chain is 4 . In this last case we quickly obtain $n=41$ which is not a square.

Similarly if $k=6$ we have two possibilities according to whether the length of the 2-chain is 4 or 5. If this length is 4 then $q=3$ and $n=49$. These values correspond to the triple (17, 3; 49). By [6] the corresponding surgered manifold bounds a $\mathbb{Q} H B^{4}$. If the length of the 2-chain is 5 then either $q=3$ and $n=48$ or $q=4$ and $n=94$ both cases can be excluded since $n$ is not a square. We keep arguing in the same way. For a fixed value of $k$ (which is not a square) we consider the possible lengths of 2 -chain. Each length gives several possible pairs for $(q, n)$. We list the values obtained in this way below. Let $l$ be the length of the 2 -chain.
\begin{itemize}
\item[-] if $q=3$ then $56 \leq n=62-l \leq 58$;
\item[-] if $q=4$ then $105 \leq n=111-l \leq 106 ;$
\item[-] if $q=5$ then $n=174-l=168$;
\end{itemize}
All these cases can be excluded because $n$ is not a square.
If $k=8$ we proceed exactly in the same way. In this case there are some candidate triples, but they can all be excluded by looking at the vector $v_{1}$ whose weight is $q$. We omit the details. Now suppose that $k \in\{4,9\}$. In both cases we can exclude the expression $v_{2}=\sqrt{k} e_{i}$ for some $i \leq N+1$ (because $v_{1} \cdot v_{2}=1$ ). Therefore we may proceed as we did for the other values of $k$.

Suppose $k=4$. The vector $v_{2}$ must hit some basis vector which appears in the expression of the 2-chain, but then it must hit all of them. Since the 2-chain has length at least 4 this is impossible (because $v_{2} \cdot v_{2}=4$ ).

Suppose now that $k=9$. Just like above we conclude that the length of the 2 -chain is at most 8, this means that $4 \leq 9 q^{2}-n-1 \leq 8$. Moreover there is a portion of the 2-chain whose length is $q-1$ which implies that $3 \leq q \leq 7$. These two inequalities are enough to spell out all possible pairs $(q, n)$ as indicated below.
\begin{itemize}
\item[-] if $q=3$ then $75 \leq n=80-l \leq 79$;
\item[-] if $q=4$ then $139 \leq n=143-l \leq 142$;
\item[-] if $q=5$ then $221 \leq n=224-l \leq 223$;
\item[-] if $q=6$ then $321 \leq n=323-l \leq 322$;
\item[-] if $q=7$ then $n=340-l=339$.
\end{itemize}
In no case is $n$ a square, and this concludes this subcase.
Third subcase: $n \in\left\{k q^{2}-q-1, k q^{2}-q, k q^{2}-q+1\right\}$.
If $n=p q=k q^{2}-q$ we have
$$-S_{n}^{3}\left(T_{k q-1, q}\right)=L(k q-1, q) \# L(q, k q-1)=L(k q-1, q) \# L(q, q-1) .$$
It follows from [14] that if this manifold bounds a $\mathbb{Q} H B^{4}$ then $q=4$. In particular both summands in the above expression must bound a $\mathbb{Q} H B^{4}$. The first summand is $L(4 k-1,4)$. It does not bound because $4 k-1$ is not square . If $n=k q^{2}-q \pm 1$ we have
$$-S_{n}^{3}\left(T_{k q-1, q}\right)=L\left(k q^{2}-q \pm 1, q^{2}\right) .$$

We start with $L\left(k q^{2}-q+1, q^{2}\right)$. Using Lemma 6.8 we obtain
$$\frac{k q^{2}-q+1}{q^{2}}=k-\frac{1}{\frac{q^{2}}{q-1}}=\left[k, q+2,2^{[q-2]}\right]^{-} .$$
It follows that $I\left(\frac{k q^{2}-q+1}{q^{2}}\right)=k-2$. If $L\left(k q^{2}-q+1, q\right)$ bounds a $\mathbb{Q} H B^{4}$ then $-3 \leq$ $I\left(\frac{k q^{2}-q+1}{q^{2}}\right) \leq 1$ which implies $2 \leq k \leq 3$. The linear plumbing graph of $-L\left(k q^{2}-q+\right.$ $1, q^{2}$ ) can be depicted as
![](https://cdn.mathpix.com/cropped/72ba5561-4a2e-4e16-9100-e636a5a592d5-30.jpg?height=147&width=642&top_left_y=757&top_left_x=747)
If $k=2$ and $q>3$, by Lemma 6.7 this graph does not embed. If $k=2$ and $q=3$ the corresponding surgered manifold is $L(16,9)$ which, by [14] bounds a $\mathbb{Q} H B^{4}$. The corresponding triple for this surgery is (5, 3; 16). Now we may assume that $k=3$. It can be checked directly that in this case the graph does not embed; start with the 2-chain and the vertex whose weight is 3.

Now we look at $L\left(k q^{2}-q-1, q^{2}\right)$. Using Lemma 6.8 we obtain
$$\frac{k q^{2}-q-1}{q^{2}}=k-\frac{1}{\frac{q^{2}}{q+1}}=\left[k, q, 2^{[q]}\right]^{-} .$$
It follows that $I\left(\frac{k q^{2}-q-1}{q^{2}}\right)=k-6$, but since $-3 \leq I\left(\frac{k q^{2}-q-1}{q^{2}}\right) \leq 1$ we have $3 \leq k \leq 7$. The linear plumbing graph of $-L\left(k q^{2}-q+1, q^{2}\right)$ can be depicted as
![](https://cdn.mathpix.com/cropped/72ba5561-4a2e-4e16-9100-e636a5a592d5-30.jpg?height=142&width=624&top_left_y=1571&top_left_x=751)
As usual, the 2-chain can be written as
$$\left(e_{1}+e_{2}, e_{2}+e_{3}, \ldots, e_{q}+e_{q+1}\right) .$$
Call $v$ the vector whose weight is $q$. It is easy to see that $v \cdot e_{i}=0$ if $2 \leq i \leq q+1$ and therefore we may write $v=e_{1}+\sqrt{q-1} e_{q+2}$. Call $w$ the vector whose weight is $k$. We can write
$$w=\gamma e_{q+2}+\beta \sum_{i=1}^{q+1}(-1)^{i} e_{i} .$$
Since $w \cdot w=k$ and $w \cdot v=1$, we have $(q+1)^{2} \beta^{2}+\gamma^{2}=k$ and $\beta+\gamma \sqrt{q-1}=1$. From which we obtain
$$(q+1)^{2} \beta^{2}+\frac{(1-\beta)^{2}}{q-1}=k .$$
Since $q \geq 3, \beta \neq 0$ and $k \leq 7$ we get a contradiction and the proof is complete. \(\square\)

\section*{References}
\begin{itemize}
\item[] [1] Paolo Aceto, Rational homology cobordisms of plumbed 3-manifolds, 2015. Preprint available at arXiv:1502.03863.
\item[] [2] Jozséf Bodnár, Daniele Celoria, and Marco Golla, Cuspidal curves and Heegaard Floer homology, Proc. London Math. Soc. 112 (2016), no. 3, 512-548.
\item[] [3] Maciej Borodzik and Charles Livingston, Heegaard Floer homology and rational cuspidal curves, Forum Math. Sigma 2 (2014), e28, 23.
\item[] [4] Andrew J. Casson and John L. Harer, Some homology lens spaces which bound rational homology balls, Pacific J. Math. 96 (1981), no. 1, 23-36.
\item[] [5] Simon K. Donaldson, An application of gauge theory to four-dimensional topology, J. Differential Geom. 18 (1983), no. 2, 279-315.
\item[] [6] Javier Fernández de Bobadilla, Ignacio Luengo, Alejandro Melle Hernández, and Andras Némethi, Classification of rational unicuspidal projective curves whose singularities have one Puiseux pair, Real and complex singularities, 2007, pp. 31-45.
\item[] [7] Ronald Fintushel and Ronald J. Stern, A $\mu$-invariant one homology 3-sphere that bounds an orientable rational ball, Four-manifold theory, 1982, pp. 265-268.
\item[] [8] Joshua E. Greene, A note on applications of the $d$-invariant and Donaldson's theorem, 2015. Preprint available at arXiv.org:1512.08244.
\item[] [9] Jennifer Hom and Zhongtao Wu, Four-ball genus bounds and a refinement of the Ozsvath-Szabo tau-invariant, 2014. To appear in J. Symplectic Geom.
\item[] [10] Stanislav Jabuka, Sinai Robins, and Xinli Wang, When are two Dedekind sums equal?, Int. J. Number Theory 7 (2011), no. 8, 2197-2202.
\item[] [11] \_\_\_\_, Heegaard Floer correction terms and Dedekind-Rademacher sums, Int. Math. Res. Not. IMRN 1 (2013), 170-183.
\item[] [12] Ana G. Lecuona, On the slice-ribbon conjecture for Montesinos knots, Trans. Amer. Math. Soc. 364 (2012), no. 1, 233-285.
\item[] [13] W. B. R. Lickorish, A representation of orientable combinatorial 3-manifolds, Ann. of Math. (2) 76 (1962), 531-540.
\item[] [14] Paolo Lisca, Lens spaces, rational balls and the ribbon conjecture, Geom. Topol. 11 (2007), 429-472.
\item[] [15] \_\_\_\_, Sums of lens spaces bounding rational balls, Algebr. Geom. Topol. 7 (2007), 2141-2164.
\item[] [16] Ciprian Manolescu and Peter Ozsváth, On the Khovanov and knot Floer homologies of quasi-alternating links, Proceedings of Gökova Geometry-Topology Conference 2007, 2008, pp. 60-81.
\item[] [17] Yves Mathieu, Closed 3-manifolds unchanged by Dehn surgery, J. Knot Theory Ramifications 1 (1992), no. 3, 279-296.
\item[] [18] John W. Milnor, Spin structures on manifolds, Enseignement Math. (2) 9 (1963), 198-203.
\item[] [19] Walter D. Neumann, A calculus for plumbing applied to the topology of complex surface singularities and degenerating complex curves, Trans. Amer. Math. Soc. 268 (1981), no. 2, 299-344.
\item[] [20] Walter D. Neumann and Frank Raymond, Seifert manifolds, plumbing, $\mu$-invariant and orientation reversing maps, Algebraic and geometric topology (Proc. Sympos., Univ. California, Santa Barbara, Calif., 1977), 1978, pp. 163-196.
\item[] [21] Yi Ni and Zhongtao Wu, Cosmetic surgeries on knots in $S^{3}$, J. Reine Angew. Math. 706 (2015), 1-17.
\item[] [22] Brendan Owens and Sašo Strle, Dehn surgeries and negative-definite four-manifolds, Selecta Math. (N.S.) 18 (2012), no. 4, 839-854.
\item[] [23] Peter S. Ozsváth and Zoltán Szabó, Absolutely graded Floer homologies and intersection forms for four-manifolds with boundary, Adv. Math. 173 (2003), no. 2, 179-261.
\item[] [24] \_\_\_\_, Heegaard floer homology and alternating knots, Geom. Topol. 7 (2003), 225-254.
\item[] [25] \_\_\_\_, On the Floer homology of plumbed three-manifolds, Geom. Topol. 7 (2003), 185-224 (electronic).
\end{itemize}
[26] \_\_\_\_, Holomorphic disks and topological invariants for closed three-manifolds, Ann. of Math. (2) 159 (2004), no. 3, 1027-1158.
[27] Heesang Park, Dongsoo Shin, and András Stipsicz, Normal complex surface singularities with rational homology disk smoothings, 2013. preprint available at arXiv.org:1311.1929.
[28] Jacob Rasmussen, Lens space surgeries and a conjecture of Goda and Teragaito, Geom. Topol. 8 (2004), 1013-1031.
[29] Vladimir A. Rohlin, New results in the theory of four-dimensional manifolds, Doklady Akad. Nauk SSSR (N.S.) 84 (1952), 221-224.
[30] C. T. C. Wall, Singular points of plane curves, Vol. 63, Cambridge University Press, 2004.
[31] Andrew H. Wallace, Modifications and cobounding manifolds, Canad. J. Math. 12 (1960), 503-528.
Alfréd Rényi Institute of Mathematics, Budapest, Hungary
E-mail address: aceto.paolo@renyi.mta.hu
Department of Mathematics, Uppsala University, Uppsala, Sweden
E-mail address: marco.golla@math.uu.se
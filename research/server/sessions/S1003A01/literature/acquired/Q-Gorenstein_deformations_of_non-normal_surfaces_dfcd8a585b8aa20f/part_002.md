---
retention_scope: session
part: 2
total_parts: 2
---

[Part 2/2 of: Q-Gorenstein deformations of non-normal surfaces]

It only remains to show part (5) of the lemma. I will only indicate how to do the first part when $p, q, r<\infty$. The rest are similar. In this case, $P \in H$ is a degenerate cusp of embedding dimension 4 of type $T_{p, q, r}^{4}$ with $p, q, r<\infty$ and the singular locus $\Delta$ of $H$ is $C$. First we describe the minimal resolution of the
normalization of $H$. Let $f: U \longrightarrow H$ be the minimal semiresolution, $\pi: U^{\prime} \longrightarrow U$ the normalization of $U, \Gamma$ the reduced part of $f^{-1}(P)$ and $C$ the dual curve of $U$. Let $E_{1}, \ldots, E_{n}$ the $f$-exceptional curves, $C^{\prime}=\pi^{-1}(C)$ and $F_{i}=\pi^{*}\left(E_{i}\right)$. Then by subadjunction, $\omega_{U^{\prime}}=\pi^{*} \omega_{U} \otimes \mathcal{O}_{U^{\prime}}\left(-C^{\prime}\right)$, we find that
$$E_{i} \cdot \Gamma=F_{i}^{2}+2-F_{i} \cdot C^{\prime}$$
Now considering that $\Gamma$ is a cycle and $\Gamma \cdot C=2$, it follows that
$$\Gamma^{2}=\sum_{i=1}^{n} F_{i}^{2}+2 n-2$$
In our case $\Gamma^{2}=-4$ and hence
$$\sum_{i=1}^{n} F_{i}^{2}=-2-2 n$$
and hence, considering that $\tilde{H}$ has cyclic quotient singularities and the extended dual graph of $\tilde{H}$ is a chain [Ba83], we get the two possibilities for the fundamental cycle that are claimed in 5.a. Now one easily sees that
$$\left(C^{\prime}+F_{1}+F_{2}+\sum E_{i}+\sum D_{i}+\sum B_{i}\right) \cdot E=0$$
where $E$ is any of the $E_{i}, B_{i}$ or $D_{i}$. Hence the blow up of $H$ along $C$ is obtained from $U^{\prime}$ be contracting all exceptional curves except those of self intersection $\leq-3$. An explicit calculation of the blow up now using the normal forms given in Lemma 2.11 shows the relation between the $p, q, r$ and the number of the -2 exceptional curves.

Alternatively, one could first describe explicitely the blow up $g: H_{W} \longrightarrow H$ of $H$ along $C$ by using the normal forms given in Lemma 2.11. Straightforward calculations show that $g^{-1}(P)=F_{1}+F_{2}$ and $g^{-1}(C)=C^{\prime}+F_{1}+F_{2}$. Moreover, $C^{\prime} \cap F_{i}=P_{i}, P_{1} \notin F_{2}, P_{2} \notin F_{1} . P_{1} \in H_{W}$ is an $A_{p-2}$ DuVal double point and $P_{2} \in$ $H_{W}$ is an $A_{q-2}$ DuVal double point. Now one can easily find the minimal resolution of $\tilde{H}$. The abstract method described above has the advantage that it allows us directly to find all the possible fundamental cycles for the singularities in question without explicit calculations using normal forms. That would be particularly useful in dealing with cusps of higher embedding dimension.

We now want to describe $H^{\prime}$. According to diagram (5) in the proof of Proposition 3.12, $H^{\prime}$ fits in the commutative diagram
![](https://cdn.mathpix.com/cropped/3a943e92-46c2-468a-b7d5-2fca918ccfb3-21.jpg?height=303&width=370&top_left_y=1860&top_left_x=877)
In the notation and setting of diagram (5), $H_{W}=g_{*}^{-1} H$ is the blow up of $H$ along $C$. Hence $E \cap H_{W}=C^{\prime}$, and $F \cap H_{W}=F_{1}+F_{2}$, as we saw earlier. Moreover, $F_{i} \not \subset E$, $i=1,2$. Now $Z$ is the blow up of $W$ along $E$ and hence $H_{Z}=h_{*}^{-1} H_{W}$ is the blow up of $H_{W}$ along $C^{\prime}$. A similar argument as above shows that the $h$-exception curves are $E_{1}$ and $B_{1}$. Finally $\phi$ contracts $F=\mathbb{P}^{2}$, and hence $H^{\prime}$ is obtained from $H_{Z}$ by contracting $F_{1}$ and $F_{2}$ and the $f$-exceptional curves correspond to $E_{1}$ and $B_{1}$
as claimed. Now, explicit calculations using the description of the extended dual graphs, give the claims about $E_{1}^{\prime 2}$ and $B_{1}^{\prime 2}$. \(\square\)

Let $L$ be the locally free part of $T_{q G}^{1} \otimes \mathcal{O}_{C}=T_{q G}^{1}(H) /($ torsion $)$ and $d=\operatorname{deg} L$. Let $H \subset X$ be an embedding as in Corollary 3.11 and let $f: E \subset Y \longrightarrow X \supset C$ the divisorial contraction as in Proposition 3.12. Then $D^{\prime}=H^{\prime} \cdot E=C^{\prime}+F_{0}$, where $F_{0}$ is supported on finitely many fibers which by Lemma 4.1 must be over degenerate cusps with $\Gamma^{2}=-3$ and $\Gamma^{2}=-4$ of type $T_{p, q, r}^{4}$ with $p, q, r \leq \infty$ and at least one of $p, q$ is $\geq 3$. More precisely, let $P \in H$ be a degenerate cusp of type $T_{p, q, r}^{4}$. Then $f^{-1}(P)=F_{1}+F_{2}, F_{i} \cong \mathbb{P}^{1}$ and $Q \in E$ is an $A_{1}$ double point, where $Q=F_{1} \cap F_{2}$. Then in a neighborhood of $P \in H, F_{0}=f^{-1}(P)=F_{1}+F_{2}$ and $Q \notin C^{\prime}$, if $p, q \geq 3$, and $F_{0}=F_{1}$ if one of $p, q$ is 2. In the last case, $C^{\prime}$ goes through the singular point of $E$. Over a point $P \in H$ of type $T_{2,2, r}^{4}$ or such that $\Gamma^{2}=-1,-2, H^{\prime}=\tilde{H}$ and $D^{\prime}=C^{\prime}$ either breaks into the union of two transversal curves or it has a node, as shown by Lemma 4.1. $E$ is normal, its singularities are over slt points of $H$ and over degenerate cusps of embedding dimension 4 and they are described explicitly in Proposition 3.12. Moreover from the description of $H^{\prime}$ given in Lemma 4.1 it is clear that $C^{\prime}$ goes through exactly those singularities of $E$ that are over slt points of $H$ or over degenerate cusps of type $T_{2, q, r}^{4}$.

It must also be pointed out that since $E$ is $\mathbb{Q}$-Cartier in $Y, E \cdot H^{\prime}=D^{\prime}$ is also $\mathbb{Q}$-Cartier in $H^{\prime}$ and hence intersection numbers make sense there. However, in the degenerate cases when at least one of $p, q, r$ is $\infty, H^{\prime}$ is not normal and $C^{\prime}$ is not $\mathbb{Q}$-Cartier in $H^{\prime}$.

Since $H$ is singular along $C$ and generically $n c, f$ is generically the blow up of $C$ and hence
$$f^{*} H=H^{\prime}+2 E$$
Moreover, $E^{2}=-\delta+F_{1}$, where $\delta$ is a section over $C$ and $F_{1}$ is supported on finitely many fibers. Intersecting (1) with $E$ we find
$$f^{*}(D)=H^{\prime} \cdot E+2 E^{2}=D^{\prime}-2 \delta+2 F_{1}$$
where $D \in \operatorname{Pic}(C)$ and $\operatorname{deg}(D)=H \cdot C=d$. Now it is possible to write $K_{E}=$ $a D^{\prime}+f^{*}\left(D_{1}\right)$, for some number $a$ and $D_{1} \in \operatorname{Pic}(C) \otimes \mathbb{Q}$. Intersecting with a general fiber $l$ we find that $a=-1$ and hence
$$K_{E}=-D^{\prime}+f^{*}\left(D_{1}\right)$$
Intersecting now with $D^{\prime}$ we find that
$$K_{E} \cdot D^{\prime}+D^{\prime 2}=2 \operatorname{deg}\left(D_{1}\right)$$
where all intersection numbers above are in $E$. Taking into account that $D^{\prime}=$ $C^{\prime}+F_{0}$ we find that
$$K_{E} \cdot D^{\prime}+D^{\prime 2}=K_{E} \cdot C^{\prime}+C^{\prime 2}+\left(K_{E} \cdot F_{0}+2 C^{\prime} \cdot F_{0}\right)-\frac{\mu}{2}$$
where $\mu$ is the number of singularities $P \in H$ of type $T_{2, q, r}^{4}$, with $q \geq 3$. Over a neighborhood of a singularity of this type, $f^{-1}(P)=F_{1}+F_{2}$, and $F_{0}=F_{1}$. Moreover, $F_{i}^{2}=-1 / 2$, and thus the term $-\mu / 2$ in the above formula.

Claim:
$$K_{E} \cdot F_{0}+2 C^{\prime} \cdot F_{0}=2 c_{3}+2 c_{4}-2 m$$
where $c_{3}, c_{4}$ are the number of degenerate cusps with $\Gamma^{2}=-3,-4$ and $m$ the number of degenerate cusps of type $T_{2,2, r}^{4}$ that lie on $C$.

Let $P \in H$ be a degenerate cusp with $\Gamma^{2}=-3,-4$. Then from the earlier discussion, $f^{-1}(P)=F_{0}=\mathbb{P}^{1}$ if $\Gamma^{2}=-3$ and $f^{-1}(P)=F_{1}+F_{2}$, if $\Gamma^{2}=-4$. Moreover, $F_{0}=F_{1}+F_{2}$ if $P \in H$ is of type $T_{p, q, r}^{4}, p, q \geq 3$, and $F_{0}=F_{1}$, if $p=2$, $q \geq 3$. Suppose that $P \in H$ is of type $T_{p, q, r}^{4}, p, q \geq 3$. Then $K_{E} \cdot F_{0}+2 C^{\prime} \cdot F_{0}=2$.

Now suppose that $P \in H$ is of type $T_{2, q, r}^{4}, q \geq 3$. Then
$$K_{E} \cdot F_{0}+2 F_{0} \cdot C^{\prime}=K_{E} \cdot F_{1}+2 F_{1} \cdot C^{\prime}=-1+2(1 / 2+1)=2$$
as before. A similar calculation for points with $\Gamma^{2}=-3$ shows the claim.
Therefore (5) becomes
$$K_{E} \cdot C^{\prime}+C^{\prime 2}+2 c_{3}+2 c_{4}-2 m-\frac{\mu}{2}=2 \operatorname{deg}\left(D_{1}\right)$$
By adjunction
$$K_{E} \cdot C^{\prime}+C^{\prime 2}=2 p_{a}\left(C^{\prime}\right)-2+\operatorname{Diff}\left(C^{\prime}, E\right)$$
where $\operatorname{Diff}\left(C^{\prime}, E\right)$ is the different of $C^{\prime}$ in $E$. Now (5) becomes
$$\operatorname{deg}\left(D_{1}\right)=p_{a}\left(C^{\prime}\right)-1+c_{3}+c_{4}-m-\frac{\mu}{4}+\frac{1}{2} \operatorname{Diff}\left(C^{\prime}, E\right)$$
Intersecting (3) with $\delta$ in $E$ we find that
$$K_{E} \cdot \delta=-D^{\prime} \cdot \delta+f^{*}\left(D_{1}\right) \cdot \delta=-D^{\prime} \cdot \delta+\operatorname{deg}\left(D_{1}\right)$$
Intersecting (2) with $\delta$ in $E$ we find
$$d=D^{\prime} \cdot \delta-2 \delta^{2}+2 F_{1} \cdot \delta$$
where $E^{2}=-\delta+F_{1}$. Taking into account this, (6) becomes
$$K_{E} \cdot \delta+\delta^{2}=-d-\delta^{2}+2 F_{1} \cdot \delta+p_{a}\left(C^{\prime}\right)-1+c_{3}+c_{4}-m-\frac{\mu}{4}+\frac{1}{2} \operatorname{Diff}\left(C^{\prime}, E\right)$$
Claim:
$$-\delta^{2}+2 \delta \cdot F_{1}=\frac{1}{2} D_{H^{\prime}}^{\prime 2}+\frac{1}{2} d$$
where by $D_{H^{\prime}}^{\prime}{ }^{2}$ we mean the self intersection of $D^{\prime}$ in $H^{\prime}$.
Intersecting (2) with $E$ and taking into account that $E \cdot \delta=-\delta^{2}+\delta \cdot F_{1}$ and $D_{H^{\prime}}^{\prime}{ }^{2}=E \cdot D^{\prime}$, we find that
$$-d=E \cdot D^{\prime}-2\left(E \cdot \delta-E \cdot F_{1}\right)={D_{H^{\prime}}}^{2}-2\left(E \cdot \delta-E \cdot F_{1}\right)$$
But $E \cdot F_{1}=\left(-\delta+F_{1}\right) \cdot F_{1}=-\delta \cdot F_{1}$. Hence $E \cdot \delta-E \cdot F_{1}=-\delta^{2}+2 \delta \cdot F_{1}$. Therefore
$$-d={D_{H^{\prime}}^{\prime}}^{2}-2\left(-\delta^{2}+2 \delta \cdot F_{1}\right)$$
and hence
$$-\delta^{2}+2 \delta \cdot F_{1}=\frac{1}{2} D_{H^{\prime}}^{\prime 2}+\frac{1}{2} d$$
as claimed. Taking this into account, (7) becomes
$$\delta \cdot K_{E}+\delta^{2}=-d+\frac{1}{2} D_{H^{\prime}}^{\prime}{ }^{2}+\frac{1}{2} d+p_{a}\left(C^{\prime}\right)-1+c_{3}+c_{4}-m-\frac{\mu}{4}+\frac{1}{2} \operatorname{Diff}\left(C^{\prime}, E\right)$$
Let $\operatorname{Diff}(\delta, E)$ be the different of $\delta$ in $E$. Then by adjunction
$$K_{E} \cdot \delta+\delta^{2}=2 p_{a}(C)-2+\operatorname{Diff}(\delta, E)$$
and (9) becomes
$$d=D_{H^{\prime}}^{\prime}{ }^{2}+2\left(p_{a}\left(C^{\prime}\right)-1\right)-2\left(2 p_{a}(C)-2\right)+2\left(c_{3}+c_{4}-m\right)-\frac{\mu}{2}+\operatorname{Diff}\left(C^{\prime}, E\right)-2 \operatorname{Diff}(\delta, E)$$
We now want to calculate the differents $\operatorname{Diff}\left(C^{\prime}, E\right)$ and $\operatorname{Diff}(\delta, E)$. The next lemma allows us to do so.

Lemma 4.3. Let $0 \in C \subset H$ be the germ of a cyclic quotient singularity of type $\frac{1}{n}(1, a)$ around a smooth curve $C$. Let $f: U \longrightarrow H$ be the minimal resolution. Assume that the extended dual graph is
$$\stackrel{\bullet}{C}-\stackrel{\circ}{E_{1}}-\cdots-\stackrel{\circ}{E_{m}}$$
Then
$$\operatorname{Diff}(C, 0 \in H)=1-1 / n$$
Proof. In the minimal resolution $U$ we have the following equations
$$\begin{gathered}
K_{U}=f^{*} K_{H}+\frac{a-n+1}{n} E_{1}+\{\text { other }\} \\
f^{*} C=C_{U}+\frac{a}{n} E_{1}+\{\text { other }\}
\end{gathered}$$
Hence
$$2 p_{a}(C)-2=K_{U} \cdot C_{U}+C_{U}^{2}=K_{H} \cdot C+C^{2}-1+1 / n$$
and the lemma follows. \(\square\)

From Proposition 3.12 and Lemma 4.1 it follows that the singular points of $E$ lie over slt points of $H$ and degenerate cusps with $\Gamma^{2}=-4$. More precisely, let $P \in H$ be an slt point. Then $E$ has two singular points on $f^{-1}(P)$ which are of type $1 / n(1,2 a)$ and $1 / n(1,-2 a)$. Let $P \in H$ be a degenerate cusp with $\Gamma^{2}=-4$. Then $f^{-1}(P)=F_{1}+F_{2}$ and $E$ has an $A_{1}$ double point at $Q=F_{1} \cap F_{2}$.
$C^{\prime}$ goes through exactly those singular points of $E$ that lie over slt points of $H$ and degenerate cusps of type $T_{2, q, r}^{4}$. Over $T_{2,2, r}^{4}$ points, $C^{\prime}$ is either nodal or normal crossing at the singular point $Q \in E$ and it is easy to see that in such a case, $C^{\prime}$ is Cartier in $E$ and hence these points contribute nothing to the different $\operatorname{Diff}\left(C^{\prime}, E\right)$.

Let $s$ and $\mu$ be the numbers of slt and $T_{2, q, r}^{4}, q \geq 3$, points respectively. Then by the previous lemma
$$\begin{gathered}
\operatorname{Diff}\left(C^{\prime}, E\right)=\sum_{i=1}^{s}\left(\operatorname{Diff}\left(C^{\prime}, P_{i} \in E\right)+\operatorname{Diff}\left(C^{\prime}, P_{-i} \in E\right)\right)+\sum_{Q} \operatorname{Diff}\left(C^{\prime}, Q \in E\right)= \\
2\left(s-\sum_{i=1}^{s} \frac{1}{n_{i}}\right)+\frac{\mu}{2}
\end{gathered}$$
where $\left(P_{i} \in E\right) \cong 1 / n_{i}\left(1,2 a_{i}\right),\left(P_{-i} \in E\right) \cong 1 / n_{i}\left(1,-2 a_{i}\right)$ are the singular points over slt points and $(Q \in E) \cong\left(x y-z^{2}=0\right) \subset \mathbb{C}^{3}$ are the singularities over points of type $T_{2, q, r}^{4}, q \geq 3$.

Now $\delta$ is a section and it goes through one of the singular points of $E$ that lie over slt points of $H$, but it also goes through the singular point of $E$ that lies over a degenerate cusp of embedding dimension 4. The last assertion can either be seen by direct calculations from Proposition 3.12, or as follows. Let $P \in H$ be a degenerate cusp of embedding dimension 4 and let $l=f^{-1}(0)=l_{1}+l_{2}$. By Proposition 3.12.
$E$ is singular at $Q=l_{1} \cap l_{2}$. Then if $\delta$ does not go through this singularity, then $-1 / 2=K_{Y} \cdot l_{i}=E \cdot l_{i}=(-\delta+l) \cdot l_{i}=\delta \cdot l_{i} \in \mathbb{Z}$. Therefore to calculate the different of $\delta$ in $E$ it is necessary to also consider the singular points that lie over degenerate cusps of embedding dimension 4. By Proposition 3.12, all such points are isomorphic to $\left(x y-z^{2}=0\right) \subset \mathbb{C}^{3}$. Then by applying the previous lemma once more we find $\operatorname{Diff}(\delta, Q \in E)=1-1 / 2=1 / 2$, and hence
$$\operatorname{Diff}(\delta, E)=\sum_{i=1}^{c_{4}} \operatorname{Diff}\left(\delta, Q_{i} \in E\right)+\sum_{i=1}^{s} \operatorname{Diff}\left(\delta, R_{i} \in E\right)=s-\sum_{i=1}^{s} \frac{1}{n_{i}}+\frac{c_{4}}{2}$$
where $Q_{i} \in E$ are the singular points over the degenerate cusps of $H$ and $R_{i} \in E$ is $P_{i}$ or $P_{-i}$ as above over the slt points. Therefore we find that
$$\operatorname{Diff}\left(C^{\prime}, E\right)-2 \operatorname{Diff}(\delta, E)=-c_{4}+\frac{\mu}{2}$$
Hence (10) becomes
$$d={D_{H^{\prime}}^{\prime}}^{2}+2\left(p_{a}\left(C^{\prime}\right)-1\right)-2\left(2 p_{a}(C)-2\right)+2 c_{3}+c_{4}-2 m$$
The next simple lemma gives a singular version of the ramification formula for curves.

Lemma 4.4. Let $\pi: C^{\prime} \longrightarrow C$ be a finite morphism between two curves with $C$ smooth. Suppose that $C^{\prime}$ has at worst nodes as singularities and let $n$ be the number of them. Then
$$2 p_{a}\left(C^{\prime}\right)-2=\operatorname{deg} \pi\left(2 p_{a}(C)-2\right)+\operatorname{deg} R+2 n$$
where $R$ is the part of the ramification divisor in the smooth part of $C^{\prime}$.
To see the proof of it, let $p: \tilde{C} \longrightarrow C^{\prime}$ be the normalization of $C^{\prime}$ (i.e, the blow up of the nodes). Then use the standard ramification formula for $\pi \circ p$ and the fact that $p_{a}\left(C^{\prime}\right)=p_{a}(\tilde{C})+n$.

In our case now, $C^{\prime}$ is ramified exactly over the pinch points of $H$ and over degenerate cusps with $\Gamma^{2}=-1,-2$ as well as over points of type $T_{2,2, r}^{4}$. Moreover, $C^{\prime}$ is smooth over the pinch points but it is nodal or nc over the degenerate cusps. Hence by the previous lemma
$$2 p_{a}\left(C^{\prime}\right)-2=2\left(2 p_{a}(C)-2\right)+p+2 c_{1}+2 c_{2}+2 m$$
where $p, c_{1}$ and $c_{2}$ are the numbers of pinch points and degenerate cusps with $\Gamma^{2}=-1,-2$ respectively. Then (11) becomes
$$d={D_{H^{\prime}}^{\prime}}^{2}+p+2 c_{1}+2 c_{2}+2 c_{3}+c_{4}=\hat{D}^{2}+p+2 c_{1}+2 c_{2}+2 c_{3}+c_{4}$$
where $\hat{D}=\nu^{*}\left(D^{\prime}\right)$. Let $\hat{C}$ be the divisorial part of $\nu^{-1}\left(C^{\prime}\right)$. Next we will get a formula for $d$ that involves $\hat{C}^{2}$ instead of $\hat{D}^{2}$. Then we will reduce it to the normalization $\tilde{H}$ of $H$. Let $U_{3}$ be the set of points $P$ such that $P \in H$ is a degenerate cusp with $\Gamma^{2}=-3, W_{4}$ the set of points $Q$ such that $Q \in H$ is a degenerate cusp of type $T_{p, q, r}^{4}$ with $p, q \geq 3$, and $V_{4}$ the set of points $R$ such that $R \in H$ is a degenerate cusp of type $T_{2, q, r}^{4}$ with $q \geq 3$.

Let $\alpha$ be a divisor in $H^{\prime}$. In what follows we will denote by $\hat{\alpha}$ the divisorial part of $\nu^{-1}(\alpha)$.

By Proposition 3.12 and Lemma 4.1, if $P \in U_{3}$, then near $P, F_{0}=f^{-1}(P)=$ $F_{P} \cong \mathbb{P}^{1}$, if $Q \in W_{4}$, then near $Q, F_{0}=f^{-1}(Q)=F_{1, Q}+F_{2, Q}$, where $F_{i, Q}$ are smooth rational curves intersecting transversally at a point. Finally if $R \in V_{4}$, then
$f^{-1}(Q)=F_{1, R}+F_{2, R}$ and near $R, F_{0}=F_{R}$, where $F_{R}=F_{i, R}$ for $i=1$ or 2. Hence,
$$\hat{D}=\hat{C}+\sum_{P \in U_{3}} \hat{F}_{P}+\sum_{Q \in W_{4}}\left(\hat{F}_{1, Q}+\hat{F}_{2, Q}\right)+\sum_{R \in V_{4}} \hat{F}_{R}$$
Therefore
$$\hat{D}^{2}=\hat{C}^{2}+\sum_{P \in U_{3}} \beta_{3}(P)+\sum_{Q \in W_{4}} \beta_{4}(Q)+\sum_{R \in V_{4}} \beta^{\prime}(R)$$
where $\beta_{3}(P)=\hat{F}_{P}^{2}+2 \hat{C} \cdot \hat{F}_{P}, \beta_{4}(Q)=\left(\hat{F}_{1, Q}+\hat{F}_{2, Q}\right)^{2}+2 \hat{C} \cdot\left(\hat{F}_{1, Q}+\hat{F}_{2, Q}\right)$ and $\beta_{4}^{\prime}(R)=\hat{F}_{R}^{2}+2 \hat{C} \cdot \hat{F}_{R}$.

Let $P \in U_{3}, Q \in W_{4}$ and $R \in V_{4}$. Then $P \in H$ is of type $T_{p, q}^{3}, Q \in H$ of type $T_{p, q, r}^{4}$ and $R \in H$ of type $T_{2, q, r}^{4}$. Then according to Lemma 4.1.4 and some straightforward calculations in the minimal resolution of $\hat{H}$ we find that,
$$\begin{gathered}
\hat{F}_{P}^{2}=-1-\frac{1}{p}-\frac{1}{q} \\
\hat{F}_{1, Q}^{2}=-1-\frac{1}{p-2}+\frac{2 r-3}{4 r-4} \\
\hat{F}_{2, Q}^{2}=-1-\frac{1}{q-2}+\frac{2 r-3}{4 r-4} \\
\hat{F}_{1, Q} \cdot \hat{F}_{2, Q}=\frac{1}{4 r-4} \\
\hat{C} \cdot \hat{F}_{1, Q}=\frac{1}{p-2} \\
\hat{C} \cdot \hat{F}_{2, Q}=\frac{1}{q-2}
\end{gathered}$$
and therefore,
$$\begin{gathered}
\beta_{3}(P)=-1+\frac{1}{p}+\frac{1}{q} \\
\beta_{4}(Q)=-1+\frac{1}{p-2}+\frac{1}{q-2} \\
\beta_{4}^{\prime}(R)=\frac{1}{q-2}-\frac{2 r-3}{4 r-4}
\end{gathered}$$
where in the case that any of the $p, q, r$ is infinity, we understand the above formulas to mean the corresponding limits at infinity.

Let $g: \hat{H} \longrightarrow \tilde{H}$ be the contraction of the $f$-exceptional curves, i.e., of $\hat{F}_{0}$. Then
$$g^{*} \tilde{C}=\hat{C}+\sum_{P \in U_{3}} \gamma_{P} \hat{F}_{P}+\sum_{Q \in W_{4}}\left(\gamma_{1, Q} \hat{F}_{1, Q}+\gamma_{2, Q} \hat{F}_{2, Q}\right)+\sum_{R \in V_{4}} \gamma_{R}^{\prime} \hat{F}_{R}$$
and therefore
$$\tilde{C}^{2}=\hat{C}^{2}+\sum_{P \in U_{3}} \delta_{3}(P)+\sum_{Q \in W_{4}} \delta_{4}(Q)+\sum_{R \in V_{4}} \delta_{4}^{\prime}(R)$$
where $\delta_{3}(P)=\left(\gamma_{P} \hat{F}_{P}\right) \cdot \hat{C}, \delta_{4}(Q)=\left(\gamma_{1, Q} \hat{F}_{1, Q}+\gamma_{2, Q} \hat{F}_{2, Q}\right) \cdot \hat{C}$ and $\delta_{4}^{\prime}(R)=\gamma_{R}^{\prime} \hat{F}_{R} \cdot \hat{C}$.
Claim:
\begin{itemize}
\item[(1)] Let $P \in U_{3}$ be a degenerate cusp of type $T_{p, q}^{3}$. Then
$$\delta_{3}(P)=\frac{(p+q)^{2}}{p q(p+q+p q)}$$
\item[(2)] Let $Q \in W_{4}$ be a degenerate cusp of type $T_{p, q, r}^{4}$ with. Then
$$\delta_{4}(Q)=\frac{1}{p-2}+\frac{1}{q-2}-\frac{r(p+q)-4}{r p q-p-q}$$
\item[(3)] Let $R \in V_{4}$ be a degenerate cusp of type $T_{2, q, r}^{4}$. Then
$$\delta_{4}^{\prime}(R)=\frac{(4 r+q-6)^{2}}{4(2 r q-q-2)(r-1)(q-2)}$$
\end{itemize}
where again in the case that any of $p, q, r$ is infinity, we understand the above formulas to mean the corresponding limits at infinity.

Assuming the claim, then from (13), (15) and (24) it follows that
$$d=\tilde{C}^{2}+\sum_{P \in U_{3}}\left(\beta_{3}(P)-\delta_{3}(P)\right)+\sum_{Q \in W_{4}}\left(\beta_{4}(Q)-\delta_{4}(Q)\right)+\sum_{R \in V_{4}}\left(\beta_{4}^{\prime}(R)-\delta_{4}^{\prime}(R)\right)+k$$
where $k=p+2 c_{1}+2 c_{2}+2 c_{3}+c_{4}$. On the other hand,
$$\begin{gathered}
\beta_{3}(P)-\delta_{3}(P)=-1+\frac{1}{p}+\frac{1}{q}-\frac{(p+q)^{2}}{p q(p+q+p q)}=-1+\frac{p+q}{p+q+p q} \\
\beta_{4}(Q)-\delta_{4}(Q)=-1+\frac{1}{p-2}+\frac{1}{q-2}-\frac{1}{p-2}-\frac{1}{q-2}+\frac{r(p+q)-4}{r p q-p-q}=-1+\frac{r(p+q)-4}{r p q-p-q} \\
\beta_{4}^{\prime}(R)-\delta_{4}^{\prime}(R)=\frac{1}{q-2}-\frac{2 r-3}{4 r-4}-\frac{(4 r+q-6)^{2}}{4(2 r q-q-2)(r-1)(q-2)}=-1+\frac{r(2+q)-4}{2 r q-q-2}
\end{gathered}$$
Hence
$$d=\tilde{C}^{2}+p+2 c_{1}+2 c_{2}+\sum_{P \in U_{3}} \alpha_{3}(P)+\sum_{Q \in U_{4}} \alpha_{4}(Q)$$
where $U_{3}$ and $U_{4}$ are the sets of degenerate cusps of multiplicity 3 and 4, respectively. Let $P \in U_{3}$ be of type $T_{p, q}^{3}$. Then
$$\alpha_{3}(P)=1+\frac{p+q}{p q+p+q}$$
let $Q \in U_{4}$ be of type $T_{p, q, r}^{4}$. Then
$$\alpha_{4}(Q)=\frac{r(p+q)-4}{r p q-p-q}$$
This concludes the proof of Theorem 3.1.
The claim follows from a lengthy but straightforward calculation. I will indicate how to do the second part about $\delta_{4}(Q)$. This is local over a degenerate cusp $Q \in H$ with $\Gamma^{2}=-4$. Suppose that the cusp is of type $T_{p, q, r}^{4}$ with $r \geq 3$. Then locally around $Q$ we can write
$$g^{*} \tilde{C}=\hat{C}+\gamma_{1, Q} F_{1, Q}+\gamma_{2, Q} F_{2, Q}$$
Intersecting with $F_{1, Q}$ and $F_{2, Q}$ and taking into consideration (16)-(21), it follows that
$$\begin{aligned}
& 4(r-1)-2(p r+p-4) \gamma_{1, Q}+(p-2) \gamma_{2, Q}=0 \\
& 4(r-1)+(q-2) \gamma_{1, Q}-2(q r+q-4) \gamma_{2, Q}=0
\end{aligned}$$

A straightforward calculation now using (18)-(24) shows that
$$\delta_{4}(Q)=\frac{1}{p-2} \gamma_{1, Q}+\frac{1}{q-2} \gamma_{2, Q}=\frac{1}{p-2}+\frac{1}{q-2}-\frac{r(p+q)-4}{r p q-p-q}$$

\section*{References}
\begin{itemize}
\item[] [Art66] M. Artin, On isolated rational singularities of surfaces, Amer. J. Math. 88, 1966, 129-136.
\item[] [AM69] M. Atiyah, I. MacDonald, Introduction to Commutative Algebra, Addison-Wesley, 1969.
\item[] [Gra72] H. Grauert, Über die deformationen isolierter singularitäten analytischer mengen, Inv. Math. 25, 1972, 171-198.
\item[] [Gra74] H. Grauert, Der Satz von Kuranishi für kompakte komplexe Räume, Inv. Math. 25, 1974, 107-142.
\item[] [Has-Kov04] B. Hassett, S. Kovács, Reflexive pull-backs and base extension, J. Algebraic Geometry 13, 2004, 233-247.
\item[] [Ka77] U. Karras, Deformations of cusp singularities, Proc. Symp. in Pure Math. Vol 30, 1977, 37-44.
\item[] [Ko91] J. Kollár, Flips, flops, minimal models, etc., Surv. in Diff. Geom. 1, 1992, 293-323.
\item[] [Ko93] J. Kollár, ed., Flips and abundance for algebraic threefolds, Astérisque 211, 1993.
\item[] [KoBa88] J. Kollár, N. I. Shepherd-Barron, Threefolds and deformations of surface singularities, Invent. Math. 91, 1988, 299-338.
\item[] [Ko-Mo92] J. Kollár, S. Mori, Classification of three-dimensional flips, J. Am.Math. Soc. Vol. 5 no. 3, 1992, 533-703.
\item[] [Li-Sch67] S. Lichtenbaum, M. Schlessiger, The cotangent complex of a morphism, Trans. Amer. Math. Soc. 128, 1967, 41-70.
\item[] [Ma-Ro71] A. Markoe, H. Rossi, Families of strongly pseudo convex manifolds, Symposium in several complex variables, Lecture Notes in Math. vol 184, Springer, 1971, 182-208.
\item[] [Ba83] N. I. Shepherd-Barron, Degenerations with numerically effective canonical divisor, Progress in Math. Vol 29, 1983, 33-84.
\item[] [Sch68] M. Schlessinger, Functors of Artin rings, Trans. AMS 130, 1968, 208-222.
\item[] [Ste98] J. Stevens, Degenerations of elliptic curves and equations for cusp singularities, Math. Ann. 311, 1998, 199-222.
\item[] [Ste91] J. Stevens, Partial resolutions of rational quadruple points, Internat. J. Math. 2, 1991, pp 205-221.
\item[] [Tzi03] N. Tziolas, Terminal 3-fold divisorial contractions of a surface to a curve I, Compositio Mathematica 139 no3, 2003, 239-261.
\item[] [Tzi05] N. Tziolas, Three dimensional divisorial extremal neighborhoods, Math. Ann. 333, 2005, 315-354.
\item[] [Wa76] J. Wahl, Equisingular deformations of normal surface singularities I, Ann. Math. 104, 1976, 325-356.
\end{itemize}
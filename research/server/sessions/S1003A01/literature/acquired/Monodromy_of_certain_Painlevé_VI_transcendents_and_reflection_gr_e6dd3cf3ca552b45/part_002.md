---
retention_scope: session
part: 2
total_parts: 4
---

[Part 2/4 of: Monodromy of certain Painlevé–VI transcendents and reflection groups]

QED
Corollary 1.2. An admissible triple $\left(x_{1}, x_{2}, x_{3}\right)$ specifies an algebraic solution of PVI $\mu$, with $2 \mu \notin \mathbb{Z}$, if and only if it satisfies (1.21) and its orbit, under the action (1.30) of the braid group, is finite.

Remark 1.9. We stress that the action (1.30) preserves the relation (1.21).
In this way, the problem of the classification of all the algebraic solutions of the $\mathrm{PVI} \mu$ reduces to the problem of the classification of all the finite orbits of the action (1.30) under the braid group in the three dimensional space (see [Dub], appendix F). Here we give a simple necessary condition for a triple $\left(x_{1}, x_{2}, x_{3}\right)$ to belong to a finite orbit.

Lemma 1.12. Let $\left(x_{1}, x_{2}, x_{3}\right)$ be a triple belonging to a finite orbit. Then:
$$x_{i}=-2 \cos \pi r_{i}, \quad r_{i} \in \mathbf{Q}, \quad 0 \leq r_{i} \leq 1, \quad i=1,2,3 .$$
Here Q is the set of rational numbers.
Proof. Let us prove the statement for, say, the coordinate $x_{1}$. Consider the transformation
$$\beta_{1}^{2}:\left(x_{1}, x_{2}, x_{3}\right) \mapsto\left(x_{1}, x_{2}+x_{1} x_{3}-x_{1}^{2} x_{2}, x_{3}-x_{1} x_{2}\right),$$
as a linear map on the plane $\left(x_{2}, x_{3}\right)$. This linear map preserves the quadratic form
$$x_{2}^{2}+x_{3}^{2}-x_{1} x_{2} x_{3} .$$
If $x_{1}=2$, we put $r_{1}=1$; otherwise we reduce the quadratic form to the principal axes, introducing the new coordinates
$$\tilde{x}_{2}=\frac{\sqrt{2+x_{1}}}{2}\left(x_{2}-x_{3}\right), \quad \tilde{x}_{3}=\frac{\sqrt{2+x_{1}}}{2}\left(x_{2}+x_{3}\right) .$$
In these new coordinates the preserved quadratic form becomes a sum of squares and the transformation $\beta_{1}^{2}$ is a rotation by the angle $\pi+2 \alpha$, where $\alpha$ is such that $x_{1}=-2 \cos \alpha$.

To have a finite orbit of $\left(\tilde{x}_{2}, \tilde{x}_{2}\right)$ under the iterations of $\beta_{1}^{2}$, the angle $\alpha$ must be a rational multiple of $\pi$. In this way the statement for $x_{1}$ is proved. To prove it for $x_{2}$ and $x_{3}$ we have to consider the iterations of $\beta_{2}^{2}$ and $\beta_{2}^{-1} \beta_{1}^{2} \beta_{2}$ respectively. QED

Remark 1.10. Thanks to the above lemma, for the finite orbits of the braid group, it is equivalent to deal with the triples $\left(x_{1}, x_{2}, x_{3}\right)$, or with the triangles with angles $\left(\pi r_{1}, \pi r_{2}, \pi r_{3}\right)$, with $x_{i}=-2 \cos \pi r_{i}$ and $0 \leq r_{i} \leq 1$ (we may assume, changing if necessary two of the signs, that at most one of the $x_{i}$ is positive). Observe that the quantity
$$x_{1}^{2}+x_{2}^{2}+x_{3}^{2}-x_{1} x_{2} x_{3}-4$$
is greater than 0 if and only if the triangle $\left(r_{1}, r_{2}, r_{3}\right)$ is hyperbolic, namely $\sum r_{i}<1$; it is equal to 0 , if and only if the triangle $\left(r_{1}, r_{2}, r_{3}\right)$ is flat, namely $\sum r_{i}=1$, and it is less than 0 if and only if the triangle $\left(r_{1}, r_{2}, r_{3}\right)$ is spherical, namely $\sum r_{i}>1$. Thanks to (1.21), a flat triangle gives a resonant value of $\mu$, and it is thus forbidden.
1.3.2. Classification of the triples $\left(x_{1}, x_{2}, x_{3}\right)$ corresponding to the algebraic solutions. We deal with the classification of all the finite orbits of the triples $\left(x_{1}, x_{2}, x_{3}\right)$ of the form (1.32), with at most ${ }^{3}$ one $r_{i}$ being equal to $\frac{1}{2}$. According to Lemma 1.12, any point of these $B_{3}$-orbits must have the same form (1.32). This condition is crucial in the classification.

Definition. We say that an admissible triple $\left(x_{1}, x_{2}, x_{3}\right)$ is good if for any braid $\beta \in B_{3}$ one has
$$\beta\left(x_{1}, x_{2}, x_{3}\right)=\left(-2 \cos \pi r_{1}^{\beta},-2 \cos \pi r_{2}^{\beta},-2 \cos \pi r_{3}^{\beta}\right),$$
with some rational numbers $0 \leq r_{i}^{\beta} \leq 1$.
Theorem 1.6. Any good triple belongs to the orbit of one of the following five
$$\begin{aligned}
& \left(-2 \cos \frac{\pi}{2},-2 \cos \frac{\pi}{3},-2 \cos \frac{\pi}{3}\right), \\
& \left(-2 \cos \frac{\pi}{2},-2 \cos \frac{\pi}{3},-2 \cos \frac{\pi}{4}\right), \\
& \left(-2 \cos \frac{\pi}{2},-2 \cos \frac{\pi}{3},-2 \cos \frac{\pi}{5}\right), \\
& \left(-2 \cos \frac{\pi}{2},-2 \cos \frac{\pi}{3},-2 \cos \frac{2 \pi}{5}\right), \\
& \left(-2 \cos \frac{\pi}{2},-2 \cos \frac{\pi}{5},-2 \cos \frac{2 \pi}{5}\right) .
\end{aligned}$$
All these orbits are finite and pairwise distinct. They contain all the permutations of the triples (1.33), (1.34), (1.35), (1.36) and (1.37), and also the triples
$$\left(2 \cos \frac{\pi}{3}, 2 \cos \frac{\pi}{3}, 2 \cos \frac{\pi}{3}\right),$$

\footnotetext{
${ }^{3}$ This corresponds to the fact that we deal only with admissible triples.
}
$$\begin{gathered}
\left(-2 \cos \frac{2 \pi}{3},-2 \cos \frac{\pi}{4},-2 \cos \frac{\pi}{4}\right), \\
\left(-2 \cos \frac{2 \pi}{3},-2 \cos \frac{\pi}{5},-2 \cos \frac{\pi}{5}\right) \quad\left(-2 \cos \frac{4 \pi}{5},-2 \cos \frac{4 \pi}{5},-2 \cos \frac{4 \pi}{5}\right), \\
\left(-2 \cos \frac{2 \pi}{3},-2 \cos \frac{2 \pi}{5},-2 \cos \frac{2 \pi}{5}\right), \quad\left(-2 \cos \frac{2 \pi}{5},-2 \cos \frac{2 \pi}{5},-2 \cos \frac{2 \pi}{5}\right), \\
\left(-2 \cos \frac{3 \pi}{5},-2 \cos \frac{\pi}{3},-2 \cos \frac{\pi}{5}\right),\left(-2 \cos \frac{2 \pi}{5},-2 \cos \frac{\pi}{3},-2 \cos \frac{\pi}{3}\right), \\
\left(-2 \cos \frac{2 \pi}{3},-2 \cos \frac{\pi}{3},-2 \cos \frac{\pi}{5}\right),
\end{gathered}$$
respectively, together with all their permutations.
Corollary 1.3. There are five finite orbits of the action (1.30) of the braid group on the space of the admissible triples $\left(x_{1}, x_{2}, x_{3}\right)$ satisfying
$$x_{1}^{2}+x_{2}^{2}+x_{3}^{2}-x_{1} x_{2} x_{3} \neq 4 .$$
The lengths of the orbits (1.33), (1.34), (1.35), (1.36) and (1.37), are equal to 4, 9, 10, 10 and 18 respectively.

Remark 1.11. The action of the pure braid group $P_{3}$ on the above orbits gives the same orbits for any of them but (1.34). The orbit (1.34), under the action of the pure braid group $P_{3}$, splits into three different orbits of three points. So the $P_{3}$-orbit (1.33) has four points, the three $P_{3}$-orbits (1.34) have three points each, (1.35) and (1.36) have ten points each and (1.37) has eighteen points. These orbits give rise to all the algebraic solutions of the $\mathrm{PVI} \mu$ equation, for $\mu$ is given by (1.21). The number of the points of each orbit with respect to the action of $P_{3}$ coincides with the number of the branches of the correspondent algebraic solution.

Proof of Theorem 1.6. The braid group acting on the classes of triples $\left(x_{1}, x_{2}, x_{3}\right)$, is generated by the braid $\beta_{1}$ and by the cyclic permutation:
$$\left(x_{1}, x_{2}, x_{3}\right) \mapsto\left(x_{3}, x_{1}, x_{2}\right) .$$
As a consequence it suffices to study the operator:
$$\left(x_{i}, x_{j}, x_{k}\right) \mapsto\left(-x_{i}, x_{j}, x_{k}-x_{i} x_{j}\right),$$
up to cyclic permutations. This transformation works on the triangles with angles $\pi r_{i}$, $\pi r_{j}, \pi r_{k}$ as follows:
$$\left(r_{i}, r_{j}, r_{k}\right) \mapsto\left(1-r_{i}, r_{j}, r_{k}^{\prime}\right),$$
where $r_{k}^{\prime}$ is such that:
$$\cos \pi r_{k}^{\prime}=\cos \pi r_{k}+2 \cos \pi r_{i} \cos \pi r_{j} .$$

The first step is to classify all the rational triples $\left(r_{i}, r_{j}, r_{k}\right)$ such that $r_{k}^{\prime}$, defined by (1.39) is a rational number, $1>r_{k}^{\prime}>0$, for every choice of $i \neq j \neq k \neq i, i, j, k=1,2,3$. Equivalently we want to classify all the rational solutions of the following equation:
$$\cos \pi r_{k}+\cos \pi\left(r_{i}+r_{j}\right)+\cos \pi\left(r_{i}-r_{j}\right)+\cos \pi\left(1-r_{k}^{\prime}\right)=0,$$
or all the rational quadruples $\left(\varphi_{1}, \varphi_{2}, \varphi_{3}, \varphi_{4}\right)$ such that:
$$\cos 2 \pi \varphi_{1}+\cos 2 \pi \varphi_{2}+\cos 2 \pi \varphi_{3}+\cos 2 \pi \varphi_{4}=0,$$
where the $\varphi_{i}$ are related with the $r_{i}$ by the following relations:
$$\varphi_{1}=r_{k} / 2, \quad \varphi_{2}=\frac{r_{i}+r_{j}}{2}, \quad \varphi_{3}=\frac{\left|r_{i}-r_{j}\right|}{2}, \quad \varphi_{4}=\frac{\left|1-r_{k}^{\prime}\right|}{2} .$$
Such a classification is given by the following:
Lemma 1.13. The only rational solutions $\left(\varphi_{1}, \varphi_{2}, \varphi_{3}, \varphi_{4}\right), 0 \leq \varphi_{i}<1$, considered up to permutations and up to transformations $\varphi_{i} \rightarrow 1-\varphi_{i}$, of the equation (1.40) consist of the following non-trivial solutions:
$$\begin{aligned}
& \left(\frac{1}{30}, \frac{11}{30}, \frac{2}{5}, \frac{1}{6}\right) \\
& \left(\frac{7}{30}, \frac{17}{30}, \frac{1}{5}, \frac{1}{6}\right) \\
& \left(\frac{1}{7}, \frac{2}{7}, \frac{3}{7}, \frac{1}{6}\right)
\end{aligned}$$
and of the following "trivial" ones, of three types:
\begin{itemize}
\item[(d)] : $\cos 2 \pi \varphi_{4}=0$. The solutions obtained in [Cro] have the form
$$(d .1):\left(\frac{1}{3}, \frac{1}{10}, \frac{3}{10}, \frac{1}{4}\right),(d .2):\left(\varphi, \varphi+\frac{1}{3}, \varphi+\frac{2}{3}, \frac{1}{4}\right),(d .3):\left(\frac{1}{4}, \varphi,\left|\varphi-\frac{1}{2}\right|, \frac{1}{4}\right),$$
where $\varphi$ is any rational number $0 \leq \varphi<1$.
\item[(e)] : $\cos 2 \pi \varphi_{4}=1$. The solutions obtained in [Gor] have the form
$$(e .1):\left(\frac{1}{3}, \frac{1}{4}, \frac{1}{3}, 0\right), \quad(e .2):\left(\frac{1}{2}, \varphi,\left|\varphi-\frac{1}{2}\right|, 0\right), \quad(e .3):\left(\frac{1}{3}, \frac{1}{5}, \frac{2}{5}, 0\right),$$
where $\varphi$ is any rational number $0 \leq \varphi<1$.
\item[(f)] : $\cos 2 \pi \varphi_{1}+\cos 2 \pi \varphi_{2}=0, \quad \cos 2 \pi \varphi_{3}+\cos 2 \pi \varphi_{4}=0$. The solutions are obvious
$$\varphi_{2}=\left|1 / 2-\varphi_{1}\right|, \quad \varphi_{4}=\left|1 / 2-\varphi_{3}\right|,$$
where $\varphi_{1}, \varphi_{3}$ are two arbitrary rational numbers $0 \leq \varphi_{i}<1$.
\end{itemize}

Proof. We follow the idea of Gordan [Gor] (see also [Cro]). In this proof we use the same notations as in [Cro], except for the $\varphi_{i}$ which there are called $r_{i}$. Let us recall the notations.

Let $\varphi_{k}=\frac{n_{k}}{d_{k}}$ where $d_{k}, n_{k}$ are either positive coprime integers, $d_{k}>n_{k}$, or $n_{k}=0$. Let $p$ be the largest prime which is a divisor of $d_{1}, d_{2}, d_{3}$, or $d_{4}$ and let $\delta_{k}, l_{k}, c_{k}, \nu_{k}$ be the integers such that
$$d_{k}=\delta_{k} p^{l_{k}} \quad \text { and } \quad n_{k}=c_{k} \delta_{k}+\nu_{k} p^{l_{k}},$$
where $\delta_{k}$ is prime to $p, 0 \leq c_{k}<p^{l_{k}}, c_{k}=0$ if $l_{k}=0$, but otherwise $c_{k}$ is prime to $p$. So
$$\varphi_{k}=\frac{\nu_{k}}{\delta_{k}}+\frac{c_{k}}{p^{l_{k}}}=f_{k}+\frac{c_{k}}{p^{l_{k}}} .$$
We assume that $l_{1} \geq l_{2} \geq l_{3} \geq l_{4}$ and define the function:
$$g_{k}(x)=\left\{\begin{array}{cc}
\frac{1}{2}\left[e^{2 \pi i f_{k}} x^{c_{k} p^{l_{1}-l_{k}}}+e^{-2 \pi i f_{k}} x^{p^{l_{1}}-c_{k} p^{l_{1}-l_{k}}}\right] & \text { if } c_{k} \neq 0 \\
\cos 2 \pi \varphi_{k} & \text { if } c_{k}=0
\end{array}\right.$$
and, in our case:
$$U(x)=\sum_{1}^{4} g_{k}(x) .$$
As in [Cro], $g_{k}\left(\exp \left(\frac{2 \pi i}{p^{l_{1}}}\right)\right)=\cos 2 \pi \varphi_{k}$ and $U\left(\exp \left(\frac{2 \pi i}{p^{l_{1}}}\right)\right)=0$. Let us introduce the polynomial
$$P(x)=1+x^{p^{l_{1}-1}}+x^{2 p^{l_{1}-1}} \cdots x^{(p-1) p^{l_{1}-1}} .$$
This is the minimal polynomial of $\exp \left(\frac{2 \pi i}{p^{l_{1}}}\right)$ with coefficients in $\mathbf{Q}$, that is such that i) $P\left(\exp \left(\frac{2 \pi i}{p^{l_{1}}}\right)\right)=0$ and ii) $P(x)$ is irreducible in the ring of polynomials with rational coefficients. A stronger result was proved by Kronecker (see [Kr]): the polynomial $P(x)$ remains irreducible over any extension of the form $\mathbf{Q}\left(\zeta_{1}, \cdots, \zeta_{n}\right)$, where $\zeta_{i}$ is a root of the unity of the order coprime with $p$. As a consequence, the following lemma holds true (see [Gor])

Lemma 1.14. If we express the polynomial $U(x)$ as a sum of polynomials $U_{t}(x)$,
$$U(x)=\sum_{t=0}^{p^{l_{1}-1}-1} U_{t}(x),$$
where $U_{t}(x)$ contains those terms of $U(x)$ of the form $b x^{c}$ with $c=t \bmod \left(p^{l_{1}-1}\right)$, then every $U_{t}(x)$ is divisible by $P(x)$.

We now apply this lemma in our case. The indices of the powers of $x$ are:
$$c_{1}, p^{l_{1}}-c_{1}, c_{2} p^{l_{1}-l_{2}}, p^{l_{1}}-c_{2} p^{l_{1}-l_{2}}, c_{3} p^{l_{1}-l_{3}}, p^{l_{1}}-c_{3} p^{l_{1}-l_{3}}, c_{4} p^{l_{1}-l_{4}}, p^{l_{1}}-c_{4} p^{l_{1}-l_{4}} .$$
If all the following conditions are satisfied:
$$l_{1}, l_{2}, l_{3}>1, \quad l_{1}>l_{2}, l_{3}, l_{4}, \quad l_{2}>l_{3}, l_{4}, \quad l_{3}>l_{4}, \quad l_{4}>0,$$
\begin{itemize}
\item[] then there are no indices equal to each other $\bmod \left(p^{l_{1}-1}\right)$ and there is no solution of (1.40). So we have to study the cases in which one of them is violated.
\item[1)] : $l_{1}=1 \geq l_{2} \geq l_{3} \geq l_{4}$. In this case, since the degree of $U(x)$ is less than $p$, and the degree of $P(x)$ is $p-1$, being $U(x)$ divisible by $P(x)$, we must have $U(x)=m P(x)$, for some constant $m$. There are four possibilities:
\item[1.1)] : $l_{1}=l_{2}=l_{3}=l_{4}=1$ then $U(0)=0$ and $\mathrm{P}(0)=1$. Then $m=0$ and $U(x) \equiv 0$; moreover if the sum of two (three) terms representing two (three) of the functions $g_{k}$ vanishes, then the sum of the two (three) functions vanishes. As a consequence there are only the following possibilities:
\item[1.1.1)] : $g_{i}=-g_{j}$ and $g_{k}=-g_{l}$ for some distinct $i, j, k, l=1, \cdots 4$. This gives rise to the trivial case (f).
\item[1.1.2)] : $g_{l}=0$ for some $l=1, \cdots 4$; this is the trivial case (d).
\item[1.1.3)] : $U(x)$ contains only two powers of $x$. If $b_{1}, \cdots, b_{4}$ are the coefficients if one of the powers $x^{c}$, then:
$$b_{1}+b_{2}+b_{3}+b_{4}=0, \quad \text { and } \quad \frac{1}{b_{1}}+\frac{1}{b_{2}}+\frac{1}{b_{3}}+\frac{1}{b_{4}}=0,$$
namely $b_{1}, \cdots, b_{4}$ are the solutions of the following biquadratic equation:
$$z^{4}+\left(b_{1} b_{2}+b_{1} b_{3}+b_{1} b_{4}+b_{2} b_{3}+b_{2} b_{4}+b_{3} b_{4}\right) z^{2}+b_{1} b_{2} b_{3} b_{4}=0 .$$
As a consequence $b_{i}+b_{j}=0, b_{l}+b_{k}=0, \frac{1}{b_{i}}+\frac{1}{b_{j}}=0$ and $\frac{1}{b_{l}}+\frac{1}{b_{k}}=0$, for some distinct $i, j, k, l=1, \cdots, 4$. Then this case reduces to the trivial case (f).
\item[1.2)] $l_{1}=l_{2}=l_{3}=1, l_{4}=0$; then $U(0)=\cos 2 \pi \varphi_{4}$ and then $U(x)=\cos 2 \pi \varphi_{4} P(x)$, where $P(x)$ is a polynomial with $p$ powers of $x$. Since in $U$ we have at most 7 powers and $p$ must be prime, then $p$ can only be equal to 2, 3, 5, 7.
\item[1.2.1)] Case $p=2$. Since $p$ is the largest prime in $d_{1}, \cdots, d_{4}$, we must have $d_{1}=d_{2}=d_{3}=$ $d_{4}=2$ and $\delta_{k}=1$. Then $\nu_{k}=0, c_{k}=1$ and this provides no solution.
\item[1.2.2)] Case $p=3$. In this case there are the two following possibilities:
$$\frac{1}{2} e^{2 \pi i f_{1}}+\frac{1}{2} e^{2 \pi i f_{2}}+\frac{1}{2} e^{2 \pi i f_{3}}=\cos 2 \pi \varphi_{4}=\frac{1}{2} e^{-2 \pi i f_{1}}+\frac{1}{2} e^{-2 \pi i f_{2}}+\frac{1}{2} e^{-2 \pi i f_{3}}$$
or
$$\frac{1}{2} e^{-2 \pi i f_{1}}+\frac{1}{2} e^{2 \pi i f_{2}}+\frac{1}{2} e^{2 \pi i f_{3}}=\cos 2 \pi \varphi_{4}=\frac{1}{2} e^{2 \pi i f_{1}}+\frac{1}{2} e^{-2 \pi i f_{2}}+\frac{1}{2} e^{-2 \pi i f_{3}} .$$
In both the case one can show that there are no solutions. In fact, for example, in the first case one has to solve the following equations:
$$2 \cos 2 \pi \varphi_{4}=\cos 2 \pi f_{1}+\cos 2 \pi f_{2}+\cos 2 \pi f_{3}, \quad \sin 2 \pi f_{1}+\sin 2 \pi f_{2}+\sin 2 \pi f_{3}=0 .$$
Using the classification of all the possible rational solution (d.1), (d.2), (d.3) of the case (d), one can show that there are no solutions.
\end{itemize}
\begin{itemize}
\item[1.2.3)] Case $p=5$. In this case we have:
$$\frac{1}{2} e^{2 \pi i f_{k}}=\frac{1}{2} e^{-2 \pi i f_{k}}=\frac{1}{2} e^{2 \pi i f_{i}}+\frac{1}{2} e^{ \pm 2 \pi i f_{j}}=\cos 2 \pi \varphi_{4},$$
for some distinct $i, j, k=1,2,3$. Then $f_{k}$ is 0 or $\frac{1}{2}$ and $\varphi_{4}=\frac{1}{6}$ or $\varphi_{4}=\frac{1}{3}$ respectively. Following the same computations of [Cro] we obtain the two solutions (a) and (b).
\item[1.2.4)] Case $p=7$. In this case we have:
$$\frac{1}{2} e^{2 \pi i f_{1}}=\frac{1}{2} e^{-2 \pi i f_{1}}=\frac{1}{2} e^{2 \pi i f_{2}}=\frac{1}{2} e^{-2 \pi i f_{2}}=\frac{1}{2} e^{2 \pi i f_{3}}=\frac{1}{2} e^{-2 \pi i f_{3}}=\cos 2 \pi \varphi_{4},$$
which has the following solutions:
$$f_{1}=f_{2}=f_{3}=0 \quad \text { and } \quad \varphi_{4}=\frac{1}{6} \quad \text { or } \quad f_{1}=f_{2}=f_{3}=\frac{1}{2} \quad \text { and } \quad \varphi_{4}=\frac{1}{3} .$$
This gives the solution (c).
\item[1.3)] $l_{1}=l_{2}=1$ and $l_{3}=l_{4}=0$. Then $U(x)=\left(\cos 2 \pi \varphi_{3}+\cos 2 \pi \varphi_{4}\right) P(x)$; again in $U$ we have at most 5 powers and then $p=2,3,5$. The case $p=2$ is treated as in [Cro];
\item[1.3.1)] : In the case $p=3$ either
$$\frac{1}{2} e^{2 \pi i f_{1}}+\frac{1}{2} e^{2 \pi i f_{2}}=\frac{1}{2} e^{-2 \pi i f_{1}}+\frac{1}{2} e^{-2 \pi i f_{2}}=\cos 2 \pi \varphi_{3}+\cos 2 \pi \varphi_{4},$$
or:
$$\frac{1}{2} e^{2 \pi i f_{1}}+\frac{1}{2} e^{-2 \pi i f_{2}}=\frac{1}{2} e^{-2 \pi i f_{1}}+\frac{1}{2} e^{2 \pi i f_{2}}=\cos 2 \pi \varphi_{3}+\cos 2 \pi \varphi_{4} .$$
In the former case, for $f_{1}=f_{2}$, with $\cos 2 \pi f_{2}=\cos 2 \pi \varphi_{3}+\cos 2 \pi \varphi_{4}$ and this gives again the solution (b). The latter case is equivalent.
\item[1.3.2)] : In the case $p=5$ one has:
$$\frac{1}{2} e^{2 \pi i f_{1}}=\frac{1}{2} e^{-2 \pi i f_{1}}=\frac{1}{2} e^{2 \pi i f_{2}}=\frac{1}{2} e^{-2 \pi i f_{2}}=\cos 2 \pi \varphi_{3}+\cos 2 \pi \varphi_{4},$$
which gives $f_{1}=f_{2}=0$ or $f_{1}=f_{2}=\frac{1}{2}$. We treat the former case (the latter is equivalent); then $\cos 2 \pi \varphi_{3}+\cos 2 \pi \varphi_{4}=\frac{1}{2}$ and we can show that this case reduces to the trivial solutions (d) and (e).
\item[1.4)] $l_{1}=1$ and $l_{2}=l_{3}=l_{4}=0$. In this case, as in [Cro], there is no solution, but the trivial one (d).
\item[2)] $l_{1} \geq 2, l_{1} \geq l_{2}, l_{3}, l_{4}$. This case can be treated as the analogous one in [Cro]. This concludes the proof of Lemma 1.13. \(\square\)
We now use the above lemma to classify all the triangles which correspond to good triples. Every quadruple generates twelve triangles. In fact, given a solution $\left(\varphi_{1}, \cdots, \varphi_{4}\right)$ we have six ways to choose the pair $\left(\varphi_{i}, \varphi_{j}\right)$ such that
$$\cos 2 \pi \varphi_{i}+\cos 2 \pi \varphi_{j}=2 \cos \pi\left(\varphi_{i}+\varphi_{j}\right) \cos \pi\left(\varphi_{i}-\varphi_{j}\right) .$$
\end{itemize}

Chosen the pair $\left(\varphi_{i}, \varphi_{j}\right)$, we have two ways for choosing $\varphi_{k}$, in order to have the triangle
$$\left(2 \varphi_{k}, \varphi_{i}+\varphi_{j},\left|\varphi_{i}-\varphi_{j}\right|\right) .$$
The remaining $\varphi_{l}$ is, by definition, such that the above triangle is mapped, by the braid (1.38), to:
$$\left(\left|\varphi_{i}-\varphi_{j}\right|,\left|1-\varphi_{i}-\varphi_{j}\right|,\left|1-2 \varphi_{l}\right|\right) .$$
Let us analyze all the triangles generated by the solutions of the equation (1.40), and keep the good ones, namely the ones for which the new $r_{k}^{\prime}$, given by (1.39), is rational for every $i, j, k$, cyclic permutation of $1,2,3$.

In order to do this, observe that if there exists a permutation $p$ such that the triple $\left(r_{p(1)}, r_{p(2)}, r_{p(3)}\right)$ gives via (1.41) values of $\varphi_{1}, \varphi_{2}, \varphi_{3}$ such that there is not any rational $\varphi_{4}$ such that $\varphi_{1}, \varphi_{2}, \varphi_{3}, \varphi_{4}$ satisfy (1.40), then $\left(r_{1}, r_{2}, r_{3}\right)$ is not a good triple. In fact, every permutation $p$ is generated by ciclic permutations and the permutation $p_{23}:\left(r_{1}, r_{2}, r_{3}\right) \rightarrow$ $\left(r_{1}, r_{3}, r_{2}\right)$. Cyclic permutations are elements of the braid group, so the statement is obvious for them. For $p_{23}$, the statement is a trivial consequence of the fact that the triples $\left(r_{1}, r_{2}, r_{3}\right)$ and $\left(r_{1}, r_{3}, r_{2}\right)$ give via (1.41) the same values of $\varphi_{1}, \varphi_{2}, \varphi_{3}$.

So we will exclude all the triangles $\left(r_{1}, r_{2}, r_{3}\right)$ for which there exists at least a permutation that gives rise to values of $\left(\varphi_{1}, \varphi_{2}, \varphi_{3}\right)$ for which rational solutions $\varphi_{4}$ of (1.40) do not exist.

Solution (a). Using (1.42), we obtain the triangles
$$\begin{gathered}
\left(\frac{1}{15}, \frac{1}{30}, \frac{23}{30}\right),\left(\frac{1}{15}, \frac{1}{5}, \frac{8}{15}\right),\left(\frac{1}{15}, \frac{7}{30}, \frac{17}{30}\right),\left(\frac{4}{15}, \frac{7}{30}, \frac{13}{30}\right), \\
\left(\frac{11}{15}, \frac{11}{30}, \frac{13}{30}\right),\left(\frac{11}{15}, \frac{2}{15}, \frac{1}{5}\right),\left(\frac{4}{5}, \frac{2}{15}, \frac{1}{5}\right),\left(\frac{1}{5}, \frac{1}{5}, \frac{7}{15}\right), \\
\left(\frac{1}{3}, \frac{11}{30}, \frac{13}{30}\right),\left(\frac{2}{3}, \frac{1}{30}, \frac{7}{30}\right),\left(\frac{1}{3}, \frac{1}{5}, \frac{3}{5}\right),\left(\frac{1}{3}, \frac{1}{3}, \frac{2}{5}\right) .
\end{gathered}$$
The last two points
$$\left(\frac{1}{3}, \frac{1}{5}, \frac{3}{5}\right) \quad\left(\frac{1}{3}, \frac{1}{3}, \frac{2}{5}\right)$$
belong to the orbit (1.37). The above values suitably permuted, except the (1.43), give rise via (1.41), to the following values of $\left(\varphi_{1}, \varphi_{2}, \varphi_{3}\right)$ (written in the same order as the correspondent generating triangles)
$$\begin{array}{lll}
\left(\frac{1}{60}, \frac{5}{12}, \frac{7}{20}\right), & \left(\frac{1}{10}, \frac{3}{10}, \frac{7}{30}\right), & \left(\frac{7}{60}, \frac{19}{60}, \frac{1}{4}\right), \\
\left(\frac{1}{10}, \frac{13}{30}, \frac{3}{10}\right), & \left(\frac{1}{15}, \frac{1}{20}, \frac{1}{12}\right), & \left(\frac{11}{60}, \frac{7}{10}, \frac{3}{20}\right), \\
\left.0, \frac{1}{5}, \frac{7}{30}\right), & \left(\frac{1}{20}, \frac{11}{60}, \frac{23}{60}\right), & \left(\frac{1}{60}, \frac{9}{20}, \frac{13}{60}\right) .
\end{array}$$
there isn't any rational number $\varphi_{4}$ such that any of the quadruples build with these triples and $\varphi_{4}$ is in the class described by Lemma 1.13.

Solution (b). Using (1.42), the triangles are
$$\begin{gathered}
\left(\frac{7}{15}, \frac{11}{30}, \frac{23}{30}\right),\left(\frac{7}{15}, \frac{2}{5}, \frac{11}{15}\right),\left(\frac{7}{15}, \frac{1}{30}, \frac{11}{30}\right),\left(\frac{2}{15}, \frac{1}{30}, \frac{19}{30}\right), \\
\left(\frac{2}{15}, \frac{1}{30}, \frac{17}{30}\right),\left(\frac{2}{15}, \frac{1}{15}, \frac{3}{5}\right),\left(\frac{2}{5}, \frac{1}{15}, \frac{2}{5}\right),\left(\frac{2}{5}, \frac{11}{15}, \frac{2}{5}\right), \\
\left(\frac{1}{3}, \frac{1}{30}, \frac{13}{30}\right),\left(\frac{1}{3}, \frac{11}{30}, \frac{23}{30}\right),\left(\frac{2}{5}, \frac{1}{3}, \frac{4}{5}\right),\left(\frac{1}{3}, \frac{1}{3}, \frac{4}{5}\right) .
\end{gathered}$$
The last two points are equivalent to:
$$\left(\frac{1}{3}, \frac{1}{5}, \frac{3}{5}\right) \quad\left(\frac{2}{3}, \frac{1}{3}, \frac{1}{5}\right)$$
of the orbit (1.37). As before one can show that if $\left(r_{1}, r_{2}, r_{3}\right)$ is one of the above values, except the (1.44), then there exists a permutation such that the $r_{k}^{\prime}$ defined by (1.39) is no-more rational. In fact we obtain for example the following values of $\left(\varphi_{1}, \varphi_{2}, \varphi_{3}\right)$, which don't fall in the values obtained in Lemma 1.13:
$$\begin{array}{llll}
\left(\frac{11}{60}, \frac{37}{60}, \frac{3}{20}\right), & \left(\frac{1}{5}, \frac{3}{5}, \frac{2}{15}\right), & \left(\frac{1}{60}, \frac{5}{12}, \frac{1}{20}\right), & \left(\frac{1}{60}, \frac{3}{4}, \frac{23}{60}\right), \\
\left(\frac{1}{30}, \frac{23}{30}, \frac{11}{30}\right), & \left(\frac{1}{60}, \frac{7}{20}\right), & \left.\frac{2}{5}, 0\right), & \left(\frac{11}{30}, \frac{2}{5}, 0\right), \\
& \left(\frac{1}{60}, \frac{23}{60}, \frac{1}{20}\right), & \left(\frac{11}{60}, \frac{11}{20}, \frac{13}{60}\right) .
\end{array}$$
Solution (c).
$$\begin{gathered}
\left(\frac{2}{7}, \frac{1}{7}, \frac{5}{7}\right),\left(\frac{2}{7}, \frac{5}{42}, \frac{19}{42}\right),\left(\frac{2}{7}, \frac{11}{42}, \frac{25}{42}\right),\left(\frac{4}{7}, \frac{11}{42}, \frac{25}{42}\right),\left(\frac{4}{7}, \frac{2}{7}, \frac{4}{7}\right),\left(\frac{4}{7}, \frac{1}{42}, \frac{13}{42}\right), \\
\left(\frac{1}{7}, \frac{1}{42}, \frac{29}{42}\right),\left(\frac{1}{7}, \frac{5}{42}, \frac{23}{42}\right),\left(\frac{1}{7}, \frac{1}{7}, \frac{4}{7}\right),\left(\frac{1}{3}, \frac{1}{7}, \frac{3}{7}\right),\left(\frac{1}{3}, \frac{2}{7}, \frac{4}{7}\right),\left(\frac{1}{3}, \frac{1}{7}, \frac{5}{7}\right) .
\end{gathered}$$
As before one can show that if $\left(r_{1}, r_{2}, r_{3}\right)$ is one of the above values then there exists a permutation such that the $r_{k}^{\prime}$ defined by (1.39) is no more rational. In fact we obtain for example the following values of $\left(\varphi_{1}, \varphi_{2}, \varphi_{3}\right)$, which are not included in the values described by Lemma 1.13:
$$\begin{array}{lll}
\left(\frac{1}{14}, \frac{1}{2}, \frac{3}{14}\right), & \left(\frac{5}{84}, \frac{31}{84}, \frac{1}{12}\right), & \left(\frac{11}{84}, \frac{37}{84}, \frac{13}{84}\right), \\
\left(\frac{1}{7}, \frac{4}{7}, 0\right), & \left(\frac{11}{84}, \frac{7}{12}, \frac{1}{84}\right), \\
\left.\frac{11}{84}, \frac{11}{84}\right), & \left(\frac{1}{84}, \frac{5}{12}, \frac{23}{84}\right), & \left(\frac{5}{84}, \frac{29}{84}, \frac{17}{84}\right),
\end{array}$$
$$\left(\frac{1}{7}, \frac{2}{7}, 0\right), \quad\left(\frac{1}{14}, \frac{8}{21}, \frac{1}{21}\right), \quad\left(\frac{1}{7}, \frac{19}{42}, \frac{5}{42}\right), \quad\left(\frac{1}{14}, \frac{11}{21}, \frac{4}{21}\right) .$$
Solution (d.1).
$$\begin{array}{ccc}
\left(\frac{2}{3}, \frac{3}{20}, \frac{3}{20}\right), & \left(\frac{1}{3}, \frac{1}{20}, \frac{9}{20}\right), & \left(\frac{1}{5}, \frac{1}{20}, \frac{1}{20}\right), \\
\left(\frac{1}{5}, \frac{1}{12}, \frac{7}{12}\right), & \left(\frac{2}{30}, \frac{19}{30}\right), \\
\left(\frac{1}{2}, \frac{7}{30}, \frac{13}{30}\right), & \left(\frac{3}{5}, \frac{3}{20}, \frac{7}{20}\right), & \left(\frac{3}{5}, \frac{7}{30}, \frac{13}{30}\right), \\
\left(\frac{11}{30}, \frac{1}{5}, \frac{2}{5}\right), & \left(\frac{1}{2}, \frac{1}{5}, \frac{2}{5}\right) .
\end{array}$$
The last two points are equivalent to:
$$\left(\frac{1}{3}, \frac{1}{5}, \frac{3}{5}\right) \quad\left(\frac{1}{2}, \frac{2}{5}, \frac{1}{5}\right)$$
of the orbit (1.37), which is now complete. We can again exclude all the other values of $\left(r_{1}, r_{2}, r_{3}\right)$, with the same trick as above.

Solution (d.2). In this case we have that any of the triangles generated is equivalent to one of the following:
$$\begin{gathered}
\left(|1-2 \varphi|, \frac{|1-4 \varphi|}{4}, \frac{1+4 \varphi}{4}\right), \quad\left(\frac{1}{2}, \frac{|1-4 \varphi|}{4}, \frac{|3-4 \varphi|}{4}\right), \quad\left(\frac{1}{2}, \frac{|1-4 \varphi|}{4}, \frac{1+4 \varphi}{4}\right), \\
\left(2 \varphi, \frac{|1-4 \varphi|}{4}, \frac{|3-4 \varphi|}{4}\right), \quad\left(\frac{1}{2}, \frac{1}{2}, \frac{|1-4 \varphi|}{2}\right),
\end{gathered}$$
where $\varphi$ is an arbitrary rational number. The last triangle is forbidden because it has two right angles, and the first four ones are all equivalent to a flat triangle, so they are again forbidden because they give rise to a an half-integer value of $\mu$.

Solution (d.3). The generated triangles are the following:
$$\begin{gathered}
\left(\frac{1}{2}, \frac{1}{3}, 2 \varphi+\frac{1}{3}\right),\left(\left|\frac{2}{3}-2 \varphi\right|, \frac{1}{3}, 2 \varphi+\frac{1}{3}\right),\left(\frac{1}{2}, \frac{2}{3}, \frac{2}{3}+2 \varphi\right),\left(\frac{2}{3}+2 \varphi, \frac{2}{3}, \frac{2}{3}+2 \varphi\right), \\
\left(\frac{2}{3}+2 \varphi, \frac{|1-4 \varphi|}{4}, \frac{1+4 \varphi}{4}\right),\left(\left|\frac{2}{3}-2 \varphi\right|, \frac{|1-4 \varphi|}{4}, \frac{1+4 \varphi}{4}\right),\left(\frac{1}{2}, \frac{1}{3}, 1+2 \varphi\right), \\
\left(2 \varphi, \frac{1}{3}, 1+2 \varphi\right),\left(\left|\frac{2}{3}-2 \varphi\right|, \varphi+\frac{1}{12}, \varphi+\frac{7}{12}\right),\left(2 \varphi, \varphi+\frac{1}{12}, \varphi+\frac{7}{12}\right), \\
\left(\frac{2}{3}+2 \varphi, \varphi+\frac{5}{12}, \varphi+\frac{11}{12}\right),\left(2 \varphi, \varphi+\frac{5}{12}, \varphi+\frac{11}{12}\right) .
\end{gathered}$$

This case must be studied carefully because we have to classify the allowed values of the rational variable $\varphi$ in order that, applying the transformation (1.38), we obtain always rational values.

Let us analyze the first triangle. It is mapped by (1.38) to a triangle equivalent to the second:
$$\left(\frac{1}{2}, \frac{1}{3}, 2 \varphi+\frac{1}{3}\right) \mapsto\left(\frac{1}{3}+2 \varphi, \frac{2}{3}, 2 \varphi+\frac{1}{3}\right) \sim\left(\left|\frac{2}{3}-2 \varphi\right|, \frac{1}{3}, 2 \varphi+\frac{1}{3}\right) .$$
If we apply the braid (1.38), with $r_{i}=\frac{2 \pi}{3}, r_{j}=r_{k}=2 \varphi+\frac{1}{3}$, we have to solve:
$$\cos \frac{2 \pi}{3}+2 \cos ^{2} \pi\left(2 \varphi+\frac{1}{3}\right)=\cos \pi r_{k}^{\prime},$$
or, equivalently, for $\varphi$ and for the new $\varphi_{k}$ :
$$\cos \frac{2 \pi}{3}+\cos 2 \pi\left(2 \varphi+\frac{1}{3}\right)+1+\cos 2 \pi \varphi_{k}=0 .$$
We classify the values of the allowed $\varphi$ using the Lemma 1.13 in the case (e). We have six possibilities for $\varphi$ :
\begin{itemize}
\item[i)] if $\varphi_{k}=\frac{1}{2}$, then $\varphi=\frac{11}{24}$. In this case we obtain, from (1.46), all the points of the orbit (1.34).
\item[ii)] if $\varphi_{k}=\frac{1}{4}$, then $\varphi=0$. In this case we obtain, from (1.46), all the points of the orbit (1.33).
\item[iii)] if $\varphi_{k}=\frac{1}{2}$, then $\varphi=\frac{1}{4}$. In this case we obtain, from (1.46), the following points:
\end{itemize}
$$\left(\frac{1}{2}, \frac{1}{3}, \frac{5}{6}\right), \quad\left(\frac{1}{6}, \frac{2}{3}, \frac{1}{6}\right) .$$
We exclude them because there exists a permutation such that the $r_{k}^{\prime}$ defined by (1.39) is no-more rational.
\begin{itemize}
\item[iv)] if $\varphi_{k}$ is free to vary, then $2 \varphi+\frac{1}{3}=\frac{1}{2}$. In this case we obtain, from (1.46), the forbidden point:
$$\left(\frac{1}{2}, \frac{1}{3}, \frac{1}{2}\right),$$
so we have to exclude it.
\item[v)] if $\varphi_{k}=\frac{1}{5}$, then $\varphi=\frac{1}{30}$, and we obtain, from (1.46), the following two points of the orbit (1.36):
$$\left(\frac{1}{2}, \frac{1}{3}, \frac{2}{5}\right), \quad\left(\frac{2}{5}, \frac{2}{3}, \frac{2}{5}\right) .$$
\item[vi)] if $\varphi_{k}=\frac{2}{5}$, then $\varphi=\frac{13}{30}$, and we obtain the following two points of the orbit (1.35):
$$\left(\frac{1}{2}, \frac{1}{3}, \frac{1}{5}\right), \quad\left(\frac{1}{5}, \frac{2}{3}, \frac{1}{5}\right) .$$
\end{itemize}

In the same way we can study all the other triangles and show that we don't obtain any other value but the ones described in Theorem 1.6.

Solution (e.1). The generated triangles are the following:
$$\left(0,0, \frac{2}{3}\right),\left(0, \frac{1}{12}, \frac{7}{12}\right),\left(0, \frac{1}{2}, \frac{2}{3}\right),\left(\frac{2}{3}, \frac{1}{12}, \frac{7}{12}\right)\left(\frac{2}{3}, \frac{1}{3}, \frac{1}{3}\right),\left(\frac{1}{2}, \frac{1}{3}, \frac{1}{3}\right),\left(\frac{2}{3}, \frac{1}{4}, \frac{1}{4}\right) ;$$
the first four are forbidden because there exists a permutation such that the $r_{k}^{\prime}$ defined by (1.39) is no-more rational. So we have to exclude them. The fifth and the sixth are points of the orbit (1.33) and the last of (1.34).

Solution (e.2). The generated triangles are the following:
$$\begin{gathered}
\left(2 \varphi, \frac{1}{2}, \frac{1}{2}\right),\left(|1-2 \varphi|, \frac{1}{2}, \frac{1}{2}\right),\left(\frac{1}{2}, \frac{1}{2}, \frac{|1+4 \varphi|}{2}\right),(1, \varphi, \varphi), \\
\left(1, \frac{|1-2 \varphi|}{2}, \frac{|1-2 \varphi|}{2}\right),\left(0, \frac{1}{2}, \frac{|1-4 \varphi|}{2}\right),(|1-2 \varphi|, \varphi, \varphi),\left(0, \frac{|1-2 \varphi|}{2}, \frac{1+2 \varphi}{2}\right), \\
(0, \varphi, 1-\varphi),\left(2 \varphi, \frac{|1-2 \varphi|}{2}, \frac{|1-2 \varphi|}{2}\right),\left(|1-2 \varphi|, \frac{|1-2 \varphi|}{2}, \frac{1+2 \varphi}{2}\right),(2 \varphi, \varphi, 1-\varphi),
\end{gathered}$$
They are all forbidden, the first three because they have two right angles, the next three ones, because we can prove that necessarily $\varphi=\frac{1}{2}$, then the first has two right angles, the second gives $\left|\cos \pi r_{k}^{\prime}\right|=3$ and the last gives $\left|\cos \pi r_{k}^{\prime}\right|=2$; all the others because they are equivalent to a flat triangle.

Solution (e.3). The generated triangles are the following:
$$\begin{gathered}
\left(0, \frac{2}{15}, \frac{8}{15}\right),\left(0, \frac{1}{15}, \frac{11}{15}\right),\left(0, \frac{1}{5}, \frac{3}{5}\right),\left(\frac{2}{3}, \frac{1}{5}, \frac{3}{5}\right),\left(\frac{2}{5}, \frac{1}{15}, \frac{11}{15}\right),\left(\frac{4}{5}, \frac{2}{15}, \frac{8}{15}\right), \\
\left(\frac{4}{5}, \frac{1}{5}, \frac{1}{5}\right),\left(\frac{2}{3}, \frac{1}{5}, \frac{1}{5}\right),\left(\frac{2}{3}, \frac{2}{5}, \frac{2}{5}\right),\left(\frac{2}{5}, \frac{2}{5}, \frac{2}{5}\right),\left(\frac{2}{5}, \frac{1}{3}, \frac{1}{3}\right),\left(\frac{1}{5}, \frac{2}{3}, \frac{1}{3}\right) .
\end{gathered}$$
We exclude the first six because we can show that there exists a permutation such that the $r_{k}^{\prime}$ defined by (1.39) is no-more rational. The seventh and the eighth give two points of the orbit (1.36), the ninth and tenth two points of the orbit (1.39) and the last two, two points of (1.39).

Solution (f) We have obtained all the points of all the orbits of Theorem 1.6. To show that there are no other points we still have to examine the case (f). In this case all the obtained triangles are equivalent to the following:
$$\begin{aligned}
\left(\frac{\varphi_{1}}{2}, \frac{\left|2-\varphi_{1}+\varphi_{3}\right|}{4},\right. & \left.\frac{\left|2-\varphi_{1}-\varphi_{3}\right|}{4}\right),\left(\frac{\varphi_{1}}{2}, \frac{1}{2}, \frac{\left|1-\varphi_{1}\right|}{2}\right), \\
\left(\frac{\varphi_{1}}{2}, \frac{\left|4-\varphi_{1}-\varphi_{3}\right|}{4},\right. & \left.\frac{\left|\varphi_{1}-\varphi_{3}\right|}{4}\right) .
\end{aligned}$$

Applying the transformation (1.38) to the above triangles, we find that we have to solve for $\varphi_{1}, \varphi_{3}$ and for the new $\varphi$ obtained from the (1.39), the following three equations respectively:
$$\begin{gathered}
\cos \pi \frac{\left|2-\varphi_{3}\right|}{2}+\cos \pi \varphi_{1}+\cos 2 \pi \varphi+1=0, \\
\cos \pi \frac{\left|1+\varphi_{1}-\varphi_{3}\right|}{2}+\cos \pi \frac{\left|1-\varphi_{1}-\varphi_{3}\right|}{2}+\cos 2 \pi \varphi=0, \\
2 \cos \pi \frac{\varphi_{1}+\varphi_{3}}{4}+\cos \pi \frac{\left|3 \varphi_{1}-\varphi_{3}\right|}{4}+\cos 2 \pi \varphi=0 .
\end{gathered}$$
We again can use Lemma 1.13 to prove that we don't obtain any new point. Let us show this in for the first triangle
$$\left(\frac{\varphi_{1}}{2}, \frac{\left|2-\varphi_{1}+\varphi_{3}\right|}{4}, \frac{\left|2-\varphi_{1}-\varphi_{3}\right|}{4}\right) .$$
We have to solve the equation
$$\cos \pi \frac{\left|2-\varphi_{3}\right|}{2}+\cos \pi \varphi_{1}+\cos 2 \pi \varphi+1=0 .$$
Using Lemma 1.13, the possible values for $\left(\frac{\left|2-\varphi_{3}\right|}{2}, \varphi_{1}, \varphi\right)$ are the (e.1), (e,2) and (e.3). Consider the case (e.1), then the possible solutions for the pair $\left(\varphi_{1}, \varphi_{3}\right)$, are
$$\left(\varphi_{1}, \varphi_{3}\right)=\left(\frac{1}{2}, \frac{2}{3}\right), \quad\left(\frac{2}{3}, 1\right), \quad\left(\frac{2}{3}, \frac{2}{3}\right) .$$
Let us substitute these solutions in (1.48); we obtain the triangles
$$\left(\frac{1}{4}, \frac{13}{24}, \frac{5}{24}\right), \quad\left(\frac{1}{3}, \frac{7}{12}, \frac{1}{12}\right), \quad\left(\frac{1}{3}, \frac{1}{2}, \frac{1}{6}\right),$$
which are all flat, and thus forbidden. Let us now consider the case (e.2). In this case we obtain two possibilities: either $\varphi_{3}=0$ and $\varphi_{1}$ is a free parameter, or $\varphi_{1}=1$ and $\varphi_{1}$ is a free parameter. In both the cases the triangle (1.48) is flat, and thus forbidden. Let us now consider the last case (e.3). The possible solutions for the pair $\left(\varphi_{1}, \varphi_{3}\right)$, are
$$\left(\varphi_{1}, \varphi_{3}\right)=\left(\frac{2}{5}, \frac{2}{3}\right), \quad\left(\frac{2}{3}, \frac{6}{5}\right), \quad\left(\frac{2}{5}, \frac{2}{5}\right), \quad\left(\frac{4}{5}, \frac{6}{5}\right), \quad\left(\frac{4}{5}, \frac{2}{3}\right), \quad\left(\frac{2}{3}, \frac{2}{5}\right) .$$
Substituting these values in (1.48), we obtain all flat angles. We can repeat the same proof for the other two triangles in (1.47). In this way we conclude the proof of the theorem. QED

\subsection*{1.4. Monodromy data and reflection groups.}

We reformulate here the above parameterization of the monodromy data by classes of equivalence of triples $\left(x_{1}, x_{2}, x_{3}\right)$ in a geometric way. Let us consider a three-dimensional
space $V$ with a basis $\left(e_{1}, e_{2}, e_{3}\right)$ and with a symmetric bilinear form $(\cdot, \cdot)$ given, in this basis, by the matrix
$$g:=\left(\begin{array}{ccc}
2 & x_{1} & x_{3} \\
x_{1} & 2 & x_{2} \\
x_{3} & x_{2} & 2
\end{array}\right)$$
namely
$$\left(e_{i}, e_{i}\right)=2, \quad \text { for } \quad i=1,2,3, \quad \text { and } \quad\left(e_{1}, e_{2}\right)=x_{1}, \quad\left(e_{2}, e_{3}\right)=x_{2}, \quad\left(e_{1}, e_{3}\right)=x_{3} .$$
Observe that the bilinear form (1.50) does not degenerate. Indeed,
$$\operatorname{det} g=8-2\left(x_{1}^{2}+x_{2}^{2}+x_{3}^{2}-x_{1} x_{2} x_{3}\right)=8 \cos ^{2} \pi \mu \neq 0,$$
due to the non-resonance assumption $2 \mu \notin \mathbb{Z}$. The three planes $p_{1}, p_{2}, p_{3}$ orthogonal to the basic vectors $\left(e_{1}, e_{2}, e_{3}\right)$ possess the following properties:
1) The normal vectors to these planes are non-isotropic (i.e. $\left.\left(e_{i}, e_{i}\right) \neq 0\right)$.
2) None of the planes is orthogonal to the other two.

Conversely, a three-dimensional space $V$ with a non-degenerate symmetric bilinear form $(\cdot, \cdot)$ and with an ordered triple of planes satisfying the above conditions, uniquely determines the matrix $g$ of the form (1.50), and then the monodromy data of a solution of $\mathrm{PVI} \mu$.

We define three reflections $R_{1}, R_{2}, R_{3}$ with respect to the three planes $\left(p_{1}, p_{2}, p_{3}\right)$ :
$$R_{i}: \begin{aligned}
& V \rightarrow V \\
& x \mapsto x-\left(e_{i}, x\right) e_{i}
\end{aligned} \quad i=1,2,3 .$$
These reflection have the following matrix representation in the basis $\left(e_{1}, e_{2}, e_{3}\right)$ :
$$R_{1}=\left(\begin{array}{ccc}
-1 & -x_{1} & -x_{3} \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right), \quad R_{2}=\left(\begin{array}{ccc}
1 & 0 & 0 \\
-x_{1} & -1 & -x_{2} \\
0 & 0 & 1
\end{array}\right), \quad R_{3}=\left(\begin{array}{ccc}
1 & 0 & 0 \\
0 & 1 & 0 \\
-x_{3} & -x_{2} & -1
\end{array}\right) .$$
Let us consider the group $G \subset \mathcal{O}(V,(\cdot, \cdot))$ of the linear transformations of $V$, generated by the three reflections $R_{1}, R_{2}, R_{3}$. The matrix $g$ will be called the Gram matrix of the reflection group $G$. It determines the subgroup $G \subset \mathcal{O}(V,(\cdot, \cdot))$ uniquely. We observe that, for an admissible triple, the group $G$ is irreducible, namely there are no non-trivial subspaces of $V$ which are invariant with respect to all the transformations of $G$.

We conclude that the branches of the solutions of $\mathrm{PVI} \mu$ can be parameterized by groups $G \subset \mathcal{O}(3)$ with a marked ordered system of generating reflections $R_{1}, R_{2}, R_{3}$. Let us describe what happens with the triples of generators under the analytic continuation of the solution.

We define an action of the braid group $B_{3}$ on the systems of generators $R_{1}, R_{2}, R_{3}$ of the reflection group $G$ :
$$\begin{aligned}
& \beta_{1}:\left(R_{1}, R_{2}, R_{3}\right) \mapsto\left(R_{1}, R_{2}, R_{3}\right)^{\beta_{1}}:=\left(R_{2}, R_{2} R_{1} R_{2}, R_{3}\right), \\
& \beta_{2}:\left(R_{1}, R_{2}, R_{3}\right) \mapsto\left(R_{1}, R_{2}, R_{3}\right)^{\beta_{2}}:=\left(R_{1}, R_{3}, R_{3} R_{2} R_{3}\right),
\end{aligned}$$
where $\beta_{1,2}$ are the standard generators of the braid group. Observe that the groups generated by the reflections $\left(R_{1}, R_{2}, R_{3}\right)$ and $\left(R_{1}, R_{2}, R_{3}\right)^{\beta}$ coincide for any $\beta \in B_{3}$. In particular the following lemma holds true:

Lemma 1.15. For any braid $\beta \in B_{3}$, the transformations $\beta\left(R_{1}, R_{2}, R_{3}\right)$ are reflections with respect to some planes orthogonal to some new basic vectors $\left(e_{1}^{\beta}, e_{2}^{\beta}, e_{3}^{\beta}\right)$. The Gram matrix with respect to the basis $\left(e_{1}^{\beta}, e_{2}^{\beta}, e_{3}^{\beta}\right)$ has the form:
$$\left(e_{i}^{\beta}, e_{i}^{\beta}\right)=2, \quad i=1,2,3, \quad\left(e_{1}^{\beta}, e_{2}^{\beta}\right)=x_{1}^{\beta}, \quad\left(e_{2}^{\beta}, e_{3}^{\beta}\right)=x_{2}^{\beta}, \quad\left(e_{1}^{\beta}, e_{3}^{\beta}\right)=x_{3}^{\beta},$$
where $\left(x_{1}^{\beta}, x_{2}^{\beta}, x_{3}^{\beta}\right)=\beta\left(x_{1}, x_{2}, x_{3}\right)$.
Proof. It is sufficient to check the statement for the generators $\beta_{1,2}$. For $\beta=\beta_{1}$ :
$$e_{1}^{\beta_{1}}=e_{2}, \quad e_{2}^{\beta_{1}}=e_{1}-x_{1} e_{2}, \quad e_{3}^{\beta_{1}}=e_{3},$$
for $\beta=\beta_{2}$ :
$$e_{1}^{\beta_{2}}=e_{1}, \quad e_{2}^{\beta_{2}}=e_{3}, \quad e_{3}^{\beta_{2}}=e_{2}-x_{2} e_{3} .$$
Computing the Gram matrix we prove the lemma. \(\square\)
1.4.1. Reflection groups and algebraic solutions Let us figure out what are the reflection groups corresponding to the finite orbits classified in Theorem 1.6.

Theorem 1.7. The orbit (1.33) corresponds to the group $W\left(A_{3}\right)$ of symmetries of regular tetrahedron, the orbit (1.34) corresponds to the group $W\left(B_{3}\right)$ of symmetries of the regular octahedron, the orbits (1.35), (1.36), (1.37) correspond to different choices of a system of generating reflections in the group $W\left(H_{3}\right)$ of symmetries of icosahedron.

Proof. It is sufficient to find one point in each of the orbits (1.33), (1.34), (1.35), (1.36), (1.37) that corresponds to a triple of symmetry planes of a regular polyhedron. To this end, we associate to a regular polyhedron a standard triple of symmetry planes using the following construction. Let 0 be the center of the polyhedron. Take a face of the polyhedron and denote $H$ the center of this face, $P$ a vertex and $Q$ the center of an edge of the face passing through the vertex $P$. The standard triple consists of the symmetry planes trough the points $O P Q, O Q H, O H P$ respectively. Let us compute the angles between the planes of each regular polyhedron. It is convinient to use the Schläfli symbol $\{p, q\}$ for regular polyhedra (see [Cox]). In these notations, the face of the regular polyhedron $\{p, q\}$ is a regular $p$-gon, the vertex figure is a regular $q$-gon. We immediately see that the angles between the planes of the standard triple are
$$\begin{array}{llll}
\text { between } & O P Q & \text { and } & O Q H \\
\text { between } & O Q H & \text { and } & O H P \\
\text { between } & O H P & \text { and } & O P Q \\
& & \frac{\pi}{p}
\end{array},$$
So, for the tetrahedron $\{3,3\}$ we obtain the angles $\left(\frac{\pi}{2}, \frac{\pi}{3}, \frac{\pi}{3}\right)$, for the octahedron $\{3,4\}$ the angles $\left(\frac{\pi}{2}, \frac{\pi}{3}, \frac{\pi}{4}\right)$, for the icosahedron $\{3,5\}$ the angles $\left(\frac{\pi}{2}, \frac{\pi}{3}, \frac{\pi}{5}\right)$. In this way, we obtain the triples (1.33), (1.34), (1.35). The reciprocal polyherda (i.e. cube \{4, 3\} and dodecaherdon
\{5, 3\}) give the same angles up to permutations. As we already know, the permuted triples of (1.34) or (1.35) belong to the same orbit. So, the standard triples of cube and dodecahedron are $B_{3}$-equivalent to those of octahedron and icosahedron respectively.

To obtain the last two orbits (1.36) and (1.37), we apply the above construction of the standard triple to great icosahedron and dodecahedron respectively. These non convex regular polyhedra both have icosaherdal symmetry (see [Cox]). Their Schläfli symbols are $\left\{3, \frac{5}{2}\right\}$ and $\left\{5, \frac{5}{2}\right\}$ respectively. This means that the faces of these polyhedra are regular triangles or pentagons, but the vertex figures are pentagrams. The above computation gives the triples (1.36) and (1.37). Again we need not consider the reciprocal stellated polyhedra. Theorem 1.7 is proved. QED
1.4.2. Classification of the monodromy data, second proof. We present here another proof of Theorem 1.6, based on the idea suggested by E. B. Vinberg. We start with the following:

Algebraic Lemma. Let $(x, y, z)$ be an admissible triple of real numbers, satisfying the inequalities:
$$x^{2}+y^{2}+z^{2}-x y z>4,$$
and
$$|x|,|y|,|z| \leq 2 .$$
Then there exists a braid $\beta \in B_{3}$ such that the absolute value of some of the coordinates of $\beta(x, y, z)$ is strictly greater than 2.

Before proving the lemma, we observe that we can assume, without loss of generality, that all the coordinates of $(x, y, z)$ are non-zero; in fact, for any admissible triple, there exists a braid $\beta \in B_{3}$ such that all the coordinates of $\beta(x, y, z)$ are non-zero. Let us denote $b_{x}, b_{y}$ and $b_{z}$ the following braids:
$$\begin{array}{ccc}
b_{x}:= & \beta_{2}, & b_{x}(x, y, z)=(z,-x, x-y z), \\
b_{y}:= & \beta_{2}^{-1} \beta_{1} \beta_{2}, & b_{y}(x, y, z)=(-y+x z,-x,-z), \\
b_{z}:= & \beta_{1}, & b_{z}(x, y, z)=(-x, z-x y, y) .
\end{array}$$

Lemma 1.16. Let ( $x, y, z$ ) be a triple of non-zero real numbers, satisfying
$$0<|z|,|x|,|y| \leq 2$$
and
$$x^{2}+y^{2}+z^{2}-x y z=4+c^{2}, \quad c>0 .$$
Denote $\left(x^{\prime}, y^{\prime}, z^{\prime}\right):=\beta(x, y, z)$, where
$$\beta=\left\{\begin{array}{lll}
b_{x} & \text { if } & |x| \leq|y|,|z|, \\
b_{y} & \text { if } & |y| \leq|x|,|z|, \\
b_{z} & \text { if } & |z| \leq|x|,|y| .
\end{array}\right.$$

Then:
$$\min \left\{\left|x^{\prime}\right|,\left|y^{\prime}\right|,\left|z^{\prime}\right|\right\} \geq \min \{|x|,|y|,|z|\}$$
and
$$\left|x^{\prime}\right|+\left|y^{\prime}\right|+\left|z^{\prime}\right| \geq|x|+|y|+|z|+\min \left\{z^{2}, 2 c\right\} .$$
Proof. Let us prove the lemma in the case where $|z| \leq|x|,|y|$ and $\beta=b_{z}$. The other cases can be proved in the same way. If the signs of $z$ and of $x y$ are opposite then
$$\left|y^{\prime}\right|=|z|+|x y| \geq|z|+z^{2}, \quad\left|x^{\prime}\right|=|x|, \quad\left|z^{\prime}\right|=|z|$$
and (1.57), (1.58) are proved. Let us suppose that the signs of $z$ and of $x y$ are the same. Changing the triple $(x, y, z)$ to an equivalent one, we can assume that all the coordinates are positive. If we prove now that
$$2 z+2 c \leq x y,$$
where $c$ is given in (1.56), we have that $\left|y^{\prime}\right|=|x y-z| \geq z+2 c$ and the lemma is proved. To prove (1.59) we find the constrained minimum of the function $x y$ on the domain $D$ defined by the conditions (1.55) and (1.56). The Lagrange function
$$F(x, y, z):=x y-\lambda\left(x^{2}+y^{2}+z^{2}-x y z\right),$$
has the local maximum at
$$x=y=\sqrt{\frac{4+c^{2}-z^{2}}{2-z}},$$
and no minimum in the interior of $D$. It remains to study the values of the function $x y$ on the boundary of $D$. If, say, $z=y$ then the positive root $x$ of the equation
$$x^{2}+2 z^{2}-x z^{2}=4+c^{2}$$
is greater than 2. So the boundaries $z=y$ and $z=x$ are not reached for $(x, y, z) \in D$, and then $|z|<|x|,|y|$. It remains the last boundary to be studied. If, say, $y=2$, we find $x=z \pm c$. Since $x \geq z$, then $x=z+c$ and $x y=2(z+c)$; this is the minimum of the function $x y$. \(\square\)

Proof of Algebraic Lemma. As observed above we can always reduce to the case where all the coordinates $(x, y, z)$ are non-zero. Put:
$$\Delta(x, y, z):=\min \left\{x^{2}, y^{2}, z^{2}, 2 \sqrt{x^{2}+y^{2}+z^{2}-x y z-4}\right\} .$$
Using Lemma 1.16, we can build a braid $b_{1}$ such that the coordinates:
$$\left(x_{1}, y_{1}, z_{1}\right):=b_{1}(x, y, z)$$
satisfy the inequalities
$$\min \left\{\left|x_{1}\right|,\left|y_{1}\right|,\left|z_{1}\right|\right\} \geq \min \{|x|,|y|,|z|\} \quad\left|x_{1}\right|+\left|y_{1}\right|+\left|z_{1}\right| \geq|x|+|y|+|z|+\Delta(x, y, z) .$$

Since the quantity $x^{2}+y^{2}+z^{2}-x y z-4$ is preserved by the action of the braid group, we obtain:
$$\Delta\left(x_{1}, y_{1}, z_{1}\right) \geq \Delta(x, y, z) .$$
If the absolute value of some of the coordinates $\left(x_{1}, y_{1}, z_{1}\right)$ is greater than 2, the lemma in proved. Otherwise we apply again the construction of Lemma 1.16 to the triple $\left(x_{1}, y_{1}, z_{1}\right)$. In this way we obtain a sequence of braids $b_{1}, b_{2}, b_{3} \cdots$ such that the corresponding triples
$$\left(x_{k+1}, y_{k+1}, z_{k+1}\right):=b_{k+1}\left(x_{k}, y_{k}, z_{k}\right)$$
satisfy
$$\Delta\left(x_{k+1}, y_{k+1}, z_{k+1}\right) \geq \Delta\left(x_{k}, y_{k}, z_{k}\right) .$$
Iterating the inequality (1.57), we obtain that
$$\left|x_{k}\right|+\left|y_{k}\right|+\left|z_{k}\right| \geq|x|+|y|+|z|+k \Delta(x, y, z) .$$
Hence, in a finite number of steps we build a triple such that the absolute value of at least one of the coordinates in greater than 2. This concludes the proof of Algebraic Lemma. QED

Corollary 1.4. For an algebraic solution of $P V I \mu$, specified by an admissible triple $x_{i}=$ $-2 \cos 2 \pi r_{i}$, the value of $\mu$ must be real, the strict inequalities
$$\left|x_{i}\right|<2, \quad i=1,2,3,$$
hold true and the matrix $g$ defined in (1.50) is positive definite.
Proof. Let us prove that, for an algebraic solution, the triple $\left(x_{1}, x_{2}, x_{3}\right)$ must satisfy the inequality:
$$x_{1}^{2}+x_{2}^{2}+x_{3}^{2}-x_{1} x_{2} x_{3}<4 .$$
Indeed, if $x_{1}^{2}+x_{2}^{2}+x_{3}^{2}-x_{1} x_{2} x_{3}>4$, then, according to the Algebraic Lemma the triple is not a good one. This contradicts the assumption that the solution is algebraic. If $x_{1}^{2}+x_{2}^{2}+x_{3}^{2}-x_{1} x_{2} x_{3}=4$, then $\mu=\frac{1}{2}+k$ with $k \in \mathbb{Z}$. This contradicts the basic assumption $2 \mu \notin \mathbb{Z}$. Then (1.62) is satisfied and $\mu$ is a real number. Let us now prove (1.61). If one of the coordinates, say $x_{1}$, is such that $x_{1}= \pm 2$, then
$$x_{1}^{2}+x_{2}^{2}+x_{3}^{2}-x_{1} x_{2} x_{3}=4+\left(x_{2} \mp x_{3}\right)^{2},$$
and, being $x_{2} ~ x_{3}$ real numbers, (1.62) is violated. So, $x_{i} \neq \pm 2$ for every $i$. Finally, applying the Sylvester criterion to the matrix $g$, we prove that $g$ is positive definite. In fact
$$\operatorname{det} G=8-2\left(x_{1}^{2}+x_{2}^{2}+x_{3}^{2}-x_{1} x_{2} x_{3}\right)>0,$$
and for any principal minor
$$\operatorname{det}\left(\begin{array}{cc}
2 & x_{i} \\
x_{i} & 2
\end{array}\right)=4-x_{i}^{2}>0 .$$
QED

Lemma 1.17. For an algebraic solution of $P V I \mu$ the reflection group $G$ acts in the Euclidean space.

The proof immediately follows from the fact that the correspondent Gram matrix is positive definite.

Corollary 1.5. For a good triple $\left(x_{1}, x_{2}, x_{3}\right)$ and for any braid $\beta \in B_{3}$, there exists three integer positive numbers $n_{12}^{\beta}, n_{13}^{\beta}$ and $n_{23}^{\beta}$ such that:
$$\left(R_{i}^{\beta} R_{j}^{\beta}\right)^{n_{i j}^{\beta}}=\mathbf{1}, \quad \text { for } \quad i \neq j, \quad i, j=1,2,3 .$$
Proof. If $\left(e_{1}, e_{2}\right)=x_{1}=-2 \cos \pi r$ with $r=\frac{m}{n}, m, n \in \mathbb{Z}$, then $R_{1} R_{2}$ is a rotation by the angle $2 \pi \frac{m}{n}$. Hence:
$$\left(R_{1} R_{2}\right)^{n}=1 .$$
This holds true for any pair $R_{i}$ and $R_{j}$. Moreover, for any braid $\beta \in B_{3}$, the triple $\beta\left(x_{1}, x_{2}, x_{3}\right)$ is again good, then (1.63) is proved. \(\square\)

Corollary 1.6. The set of the solutions of the PVI $\mu$ equation with a real non resonant value of $\mu$ and real parameters $\left(x_{1}, x_{2}, x_{3}\right)$ satisfying
$$\left|x_{i}\right|<2, \quad i=1,2,3,$$
is invariant with respect to the analytic continuation.
Proof. Applying the Sylvester criterion to the matrix $g$ defined in (1.50), we obtain that $g$ is positive definite. So the reflections $R_{1}, R_{2}, R_{3}$ can be realized in the Euclidean space. After a transformation $\left(x_{1}, x_{2}, x_{3}\right) \mapsto\left(x_{1}^{\beta}, x_{2}^{\beta}, x_{3}^{\beta}\right)=\beta\left(x_{1}, x_{2}, x_{3}\right)$, the new numbers $\left(x_{1}{ }^{\beta}, x_{2}{ }^{\beta}, x_{3}{ }^{\beta}\right)$ are the entries of the Gram matrix:
$$g^{\beta}:=\left(\begin{array}{ccc}
2 & x_{1}^{\beta} & x_{3}^{\beta} \\
x_{1}^{\beta} & 2 & x_{2}^{\beta} \\
x_{3}^{\beta} & x_{2}^{\beta} & 2
\end{array}\right) \text {, }$$
of the basis $\left(e_{1}^{\beta}, e_{2}^{\beta}, e_{3}^{\beta}\right)$, in the same Euclidean space. Then this matrix must be positive definite, namely $x_{i}^{2}<4$ as we wanted to prove. \(\square\)

In the second part of this paper, we will identify the set described in Corollary 1.6 with the class of solutions of $\mathrm{PVI} \mu$ having asymptotic behaviour of algebraic type. This identification will be crucial in the computation of the five algebraic solutions of $\mathrm{PVI} \mu$ we have classified.

As we have just shown, a good triple
$$\left(x_{1}, x_{2}, x_{3}\right)=\left(-2 \cos \pi \frac{m_{1}}{n_{1}},-2 \cos \pi \frac{m_{2}}{n_{2}},-2 \cos \pi \frac{m_{3}}{n_{3}}\right),$$
corresponds to a representation of the Coxeter group generated by three reflections $R_{1}$, $R_{2}, R_{3}$ satisfying
$$R_{1}^{2}=R_{2}^{2}=R_{3}^{2}=\mathbf{1}, \quad\left(R_{1} R_{2}\right)^{n_{1}}=\left(R_{2} R_{3}\right)^{n_{2}}=\left(R_{1} R_{3}\right)^{n_{3}}=\mathbf{1},$$
in the three-dimensional Euclidean space. We denoted by $G$ the image of this representation. Moreover, for any braid $\beta \in B_{3}$, the matrices
$$\left(R_{1}^{\beta}, R_{2}^{\beta}, R_{3}^{\beta}\right):=\beta\left(R_{1}, R_{2}, R_{3}\right),$$
satisfy the same identities (1.64), with some new integers $n_{1}^{\beta}, n_{2}^{\beta}, n_{3}^{\beta}$. We stress that the reflections $R_{1}^{\beta}, R_{2}^{\beta}, R_{3}^{\beta}$ generate the same group $G$.

Theorem 1.8. It follows from the above property that $G$ is an irreducible finite Coxeter group.

Let $n$ be the least common multiple of $n_{1}, n_{2}$ and $n_{3}$. Put:
$$\zeta=2 \cos \frac{\pi}{n} .$$

Lemma 1.18. The numbers
$$x_{i}=-2 \cos \pi \frac{m_{i}}{n_{i}}, \quad i=1,2,3,$$
belong to the ring $\mathcal{K}_{0}$ of integers of the field $\mathcal{K}:=\mathbf{Q}[\zeta]$.
Recall (see [Wey]) that $\mathcal{K}$ is the normal extension of $\mathbf{Q}$ generated by $\zeta$ and $\mathcal{K}_{0}$ is the ring of all the algebraic integer numbers of $\mathcal{K}$, namely it consists of all the elements $x \in \mathcal{K}$ satisfying an algebraic equation of the form
$$x^{k}+a_{1} x^{k-1}+\cdots+a_{k}=0, \quad \text { with } \quad a_{i} \in \mathbb{Z} .$$

Proof of Lemma 1.18. Let $n=n_{i} m_{i}^{\prime}$, then
$$\cos \pi \frac{m_{i}}{n_{i}}=T_{m_{i} m_{i}^{\prime}}\left(\cos \frac{\pi}{n}\right)=T_{m_{i} m_{i}^{\prime}}\left(\frac{1}{2} \zeta\right),$$
where
$$T_{k}(x)=\cos (k \arccos x)=2^{k-1} x^{k}+\sum_{s=0}^{k-1} 2^{s-1} a_{k s} x^{s},$$
are the Tchebyscheff polynomials of the first kind (see [Bat]). Recall that all the coefficients $a_{k s}$ are integers, so $x_{i}=-2 \cos \pi \frac{m_{i}}{n_{i}}$ is a polynomial of $\zeta$ with integer coefficients. Moreover $\zeta$ is a root of the monic algebraic equation with integer coefficients
$$2 T_{n}\left(\frac{\zeta}{2}\right)+2=\zeta^{n}+\sum_{s=0}^{n-1} a_{n s} \zeta^{s}+2=0$$

Hence $\zeta \in \mathcal{K}_{0}$ and $x_{i}=-2 T_{m_{i} m_{i}^{\prime}}\left(\frac{\zeta}{2}\right) \in \mathcal{K}_{0}$, as we wanted to prove.

Proof of Theorem 1.8. From the formulae (1.51) it follows that the matrices $R_{1}, R_{2}$ and $R_{3}$ are all defined over the same ring $\mathcal{K}_{0}$ of integers of $\mathcal{K}$ :
$$R_{i} \in \operatorname{Mat}\left(\mathcal{K}_{0}, 3\right) .$$
Moreover, these matrices are orthogonal with respect to $g$ :
$$R_{i}^{T} g R_{i}=g,$$
where $g$ is defined in (1.50). Let
$$\Gamma:=\operatorname{Gal}(\mathcal{K}, \mathbf{Q})$$
the Galois group of $\mathcal{K}$ over $\mathbf{Q}$, namely the group of all automorphisms
$$\phi: \mathcal{K} \rightarrow \mathcal{K},$$
identical on $\mathbf{Q}$.
For any $\phi \in \Gamma$ we denote $\phi\left(R_{i}\right)$ and $\phi(g)$ the matrices obtained from $R_{i}$ and $g$ by the action
$$\left(x_{1}, x_{2}, x_{3}\right) \mapsto\left(\phi\left(x_{1}\right), \phi\left(x_{2}\right), \phi\left(x_{3}\right)\right) .$$

Lemma 1.19. For any $\phi \in \Gamma$ the following statements hold true:
\begin{itemize}
\item[i)] $\operatorname{det} \phi(g) \neq 0$,
\item[ii)] The matrices $\phi\left(R_{i}\right)$ are orthogonal with respect to $\phi(g)$.
\item[iii)] For any $\beta \in B_{3}$ the matrices $\phi\left(R_{i}\right)^{\beta}$ satisfy the Coxeter relation (1.63).
\end{itemize}
The proof is obvious, due to the fact that any automorphism preserves all the algebraic relations.

From the above lemma, and from Algebraic Lemma, it follows that for any $\phi \in \Gamma$, the real symmetric matrix $\phi(g)$ must be positive definite. We will show that this implies that the group $G$ is finite. Let $N$ be the order of the Galois group $\Gamma$. We construct the block-diagonal matrices
$$\mathcal{R}_{i} \in \operatorname{Mat}\left(\mathcal{K}_{0}, 3 N\right), \quad i=1,2,3,$$
as the matrices formed by 3 × 3 blocks on the diagonal, such that the $j$-th block is $\phi_{j}\left(R_{i}\right)$, for $\phi_{j} \in \Gamma, j=1,2, \cdots, N$. The matrices $\mathcal{R}_{i}$ are orthogonal with respect to $\mathcal{G}$, that is the block-diagonal matrix having $\phi_{j}(G)$, for $\phi_{j} \in \Gamma, j=1,2, \cdots, N$, on the diagonal blocks. We can apply Lemma 1.19 to the matrices $\mathcal{R}_{i}$ to show that they satisfy the Coxeter relation (1.63). As a consequence we obtain a representation of our reflection group $G$ into the orthogonal group
$$\begin{aligned}
G & \rightarrow \mathcal{O}\left(\mathcal{K}^{3 N}, \mathcal{G}\right) \\
R_{i} & \mapsto \mathcal{R}_{i} .
\end{aligned}$$
By construction the matrices $\mathcal{R}_{i}$ preserve the sublattice
$$\mathcal{K}_{0}^{3 N} \subset \mathcal{K}^{3 N}$$
of the vectors the components of which are algebraic integers of the field $\mathcal{K}$. We recall (see [Wey]) that the ring $\mathcal{K}_{0}$ of the algebraic integers of the field $\mathcal{K}$, is a finite-dimensional lattice. As a consequence, the image of the representation (1.68) is a discrete subgroup of the orthogonal group. Since $\mathcal{G}$ is positive definite, the orthogonal group is compact and, hence, $G$ must be finite. The theorem is proved.

QED
To complete the classification of the monodromy data related to the algebraic solutions it remains to classify the objects
$$\left(G, R_{1}, R_{2}, R_{3}\right),$$
where $G$ is one of the Coxeter groups $A_{3}, B_{3}$ and $H_{3}$ and $\left(R_{1}, R_{2}, R_{3}\right)$ is a triple of generating reflections considered modulo the action (1.52) of the braid group. This can be done by a straightforward computation of all the orbits of the triples of generating reflections. All of them were described and classified by Schwartz (see the introduction). We arrive again at the list of Theorem 1.6, where, as we already know, the triples (1.33) generate the group $W\left(A_{3}\right)$ of the symmetries of the tetrahedron, (1.34) generate the group $W\left(B_{3}\right)$ of the symmetries of the cube, while (1.35), (1.36) and (1.37) correspond to three inequivalent triples of the generating reflections of the group $W\left(H_{3}\right)$.

\section*{2. GLOBAL STRUCTURE OF THE SOLUTIONS OF PAINLEVE' VI $\mu$ HAV-ING CRITICAL BEHAVIOUR OF ALGEBRAIC TYPE}

In the first part of this paper, we found a class of solutions of $\mathrm{PVI} \mu$ invariant with respect to the analytic continuation. For them, the reflection group $G$ acts in the three-dimensional Euclidean space. Recall that the parameter $\mu$ must be real, the coordinates of the admissible triples $\left(x_{1}, x_{2}, x_{3}\right)$ must be real and satisfy the inequality
$$-2<x_{i}<2, \quad i=1,2,3 .$$
In this second part, we prove that this class of solutions coincides with the class of the solutions of $\mathrm{PVI} \mu$ having critical behaviour of the algebraic type
$$y(x)=\left\{\begin{array}{rc}
a_{0} x^{l_{0}}\left(1+\mathcal{O}\left(x^{\varepsilon}\right)\right), & \text { as } \quad x \rightarrow 0, \\
1-a_{1}(1-x)^{l_{1}}\left(1+\mathcal{O}\left((1-x)^{\varepsilon}\right)\right), & \text { as } \quad x \rightarrow 1, \\
a_{\infty} x^{1-l_{\infty}}\left(1+\mathcal{O}\left(x^{-\varepsilon}\right)\right), & \text { as } \quad x \rightarrow \infty,
\end{array}\right.$$
where $\varepsilon>0$ is small enough, the indices $l_{0}, l_{1}, l_{\infty}$ are real and the coefficients $a_{0}, a_{1}, a_{\infty}$ are some complex numbers. We compute the behaviour of any branch of these solutions near the critical points. These results will be used to compute explicitly all the algebraic solutions classified in the first part.

First of all, we fix the notations. Let us choose:
$$u_{1}=0, \quad u_{2}=x, \quad u_{3}=1 .$$
Then the Fuchsian system (1.1) reads
$$\frac{\mathrm{d}}{\mathrm{~d} z} Y=\mathcal{A}(z, x) Y=\left(\frac{\mathcal{A}_{1}}{z}+\frac{\mathcal{A}_{2}}{z-x}+\frac{\mathcal{A}_{3}}{z-1}\right) Y,$$
and, putting
$$\mathcal{A}_{1}:=A_{0}, \quad \mathcal{A}_{2}:=A_{x}, \quad \mathcal{A}_{3}:=A_{1}, \quad \mathcal{A}_{\infty}=A_{\infty},$$
we obtain
$$\frac{\mathrm{d}}{\mathrm{~d} z} Y=\left(\frac{A_{0}}{z}+\frac{A_{1}}{z-1}+\frac{A_{x}}{z-x}\right) Y .$$
The branch cuts in $\overline{\mathbb{C}}$ are the same as in Section 1.1. We call now the basic loops $\gamma_{0}, \gamma_{x}, \gamma_{1}$. They are fixed as before, namely $\gamma_{0}, \gamma_{x}, \gamma_{1}$ play the role of the preceding $\gamma_{1}, \gamma_{2}, \gamma_{3}$ (see figure 1). The Schlesinger equations read:
$$\begin{aligned}
\frac{\mathrm{d}}{\mathrm{~d} x} A_{0}(x) & =-\frac{\left[A_{0}, A_{x}\right]}{x}, \\
\frac{\mathrm{~d}}{\mathrm{~d} x} A_{1}(x) & =-\frac{\left[A_{1}, A_{x}\right]}{x-1}, \\
\frac{\mathrm{~d}}{\mathrm{~d} x} A_{x}(x) & =\frac{\left[A_{0}, A_{x}\right]}{x}+\frac{\left[A_{1}, A_{x}\right]}{x-1} .
\end{aligned}$$
The correspondent monodromy matrices are
$$M_{0}, \quad M_{x}, \quad M_{1},$$
which play the role of the preceding $M_{1}, M_{2}, M_{3}$ respectively. We recall that they satisfy
$$M_{\infty} M_{1} M_{x} M_{0}=1, \quad \operatorname{det}\left(M_{i}\right)=1, \quad \operatorname{Tr}\left(M_{i}\right)=2, \quad \text { for } \quad i=0,1, x,$$
with
$$M_{\infty}=\left(\begin{array}{cc}
\exp (2 i \pi \mu) & 0 \\
0 & \exp (-2 i \pi \mu)
\end{array}\right) .$$
With the above choice of $A_{\infty}, A_{1}, A_{x}$ and $A_{0}$, satisfying
$$\operatorname{det} A_{i}=0, \quad \operatorname{Tr}\left(A_{i}\right)=0, \quad i=0,1, \infty,$$
the non-singular solution $A(z, x)$ of the Schlesinger equations turns out to be related to the solution of $\mathrm{PVI} \mu$ in the following way (see [JMU]):
$$[A(y, x)]_{12}=0, \quad \text { iff } \quad y(x) \text { solves } \mathrm{PVI} \mu,$$
where $y$ is not identically equal to $0,1, x$.
We now state the first main theorem of this second part:

Theorem 2.1. For any admissible triple $\left(x_{0}, x_{1}, x_{\infty}\right), x_{i} \in \mathbb{R},\left|x_{i}\right|<2$ for $i=0,1, \infty$, there exists a unique branch $y\left(x ; x_{0}, x_{1}, x_{\infty}\right)$ of a solution of $P V I \mu$, with the parameter $\mu$ satisfying the equation:
$$4 \sin ^{2} \pi \mu=x_{0}^{2}+x_{1}^{2}+x_{\infty}^{2}-x_{0} x_{1} x_{\infty},$$
with the asymptotic behaviour (2.1) near the critical points $0,1, \infty$. The indices are given by
$$l_{i}=\frac{1}{\pi} \arccos \left(\cos 2 \pi r_{i}\right)=\left\{\begin{array}{rl}
2 r_{i} & \text { if } 0<r_{i} \leq \frac{1}{2} \\
2-2 r_{i} & \text { if } \frac{1}{2} \leq r_{i}<1
\end{array} \quad i=0,1, \infty,\right.$$
with
$$x_{i}=-2 \cos \pi r_{i}, \quad i=0,1, \infty,$$
and the leading coefficients $a_{0}, a_{1}, a_{\infty}$ are single-valued functions of the equivalence class of $x_{0}, x_{1}, x_{\infty}$ and of $\mu$. Namely, the coefficient $a_{0}$, for $x_{0} \neq 0$, is given by:
$$a_{0}=\frac{\exp (-i \pi \phi)}{4\left(2 \mu+l_{0}-1\right)^{2}} \frac{\Gamma^{2}\left(1-l_{0}\right) \Gamma^{2}\left(\frac{1+l_{0}}{2}\right) \Gamma\left(\frac{1+l_{0}}{2}+\mu\right) \Gamma\left(\frac{1+l_{0}}{2}-\mu\right)}{\Gamma^{2}\left(l_{0}\right) \Gamma^{2}\left(\frac{1-l_{0}}{2}\right) \Gamma\left(\frac{1-l_{0}}{2}+\mu\right) \Gamma\left(\frac{1-l_{0}}{2}-\mu\right)}$$
where
$$\exp (i \pi \phi)=\frac{x_{0}^{2} x_{1}^{2}-2 x_{1}^{2}-2 x_{0} x_{1} x_{\infty}+2 x_{\infty}^{2}+i x_{1} \operatorname{sign}\left(x_{0}\right) \sqrt{4-x_{0}^{2}}\left(2 x_{\infty}-x_{0} x_{1}\right)}{2\left(x_{1}^{2}-x_{0} x_{1} x_{\infty}+x_{\infty}^{2}\right)}$$
and for $x_{0}=0$
$$a_{0}=\frac{x_{\infty}^{2}}{x_{1}^{2}+x_{\infty}^{2}} .$$
The coefficient $a_{1}$ is given by the same formula with the substitution $x_{0} \leftrightarrow x_{1}, l_{0} \mapsto l_{1} ; a_{\infty}$ is given by the same formula too, after the substitution $\left(x_{0}, x_{1}, x_{\infty}\right) \mapsto\left(x_{\infty},-x_{1}, x_{0}-x_{1} x_{\infty}\right)$ and $l_{0} \mapsto l_{\infty}$. Conversely any solution of the PVI $\mu$ equation, with a real value of $\mu$, having critical behaviour of algebraic type, can be obtained by the above construction.
Remark 2.1. The relation (2.8) determines $\mu$ up to the transformations
$$\mu \mapsto \pm \mu+n, \quad n \in \mathbb{Z} .$$
According to the results of Section 1.2, such an ambiguity can be absorbed by the action of a symmetry on $\mathrm{PVI} \mu$. Recall that these symmetries preserve the class of the algebraic solutions.

Theorem 2.1 will be proved in Section 2.4.

\subsection*{2.1. Local theory of the solutions of $\mathbf{P V I} \mu$ having critical behaviour of algebraic type}
2.1.1. Local asymptotic behaviour around 0. In this section we characterize the local asymptotic behaviour of the solutions of $\mathrm{PVI} \mu$ near the singular point $x=0$. First of all let us characterize the type of asymptotic behaviour that can be related to the algebraic solutions.

Lemma 2.1. Let $y(x)$ be an algebraic solution of PVI $\mu$. Then the first term of its Puiseux series is
$$y(x) \sim a_{0} x^{1-\sigma_{0}} \quad \text { as } \quad x \rightarrow 0 .$$
for some constant $a_{0} \neq 0$ and the rational number $\sigma_{0}$ must satisfy $0 \leq \sigma_{0}<1$, with $a_{0} \neq 1$ if $\sigma_{0}=0$.
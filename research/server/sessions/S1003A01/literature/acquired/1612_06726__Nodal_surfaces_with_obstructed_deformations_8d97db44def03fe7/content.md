---
retention_scope: session
part: 1
total_parts: 1
---

---
source_file: 1612_06726.pdf
converter: mathpix
format: mmd
---

\title{
NODAL SURFACES WITH OBSTRUCTED DEFORMATIONS
}

\author{
REMKE KLOOSTERMAN
}

\begin{abstract}
In this text we show that the deformation space of a nodal surface $X$ of degree $d$ is smooth and of the expected dimension if $d \leq 7$ or $d \geq 8$ and $X$ has at most $4 d-5$ nodes. (The case $d \leq 7$ was previously covered by Alexandru Dimca using different techniques.)

For $d \geq 8$ we give explicit examples of nodal surfaces with $4 d-4$ nodes, for which the tangent space to the deformation space has larger dimension than expected.
\end{abstract}

\section*{1. Introduction}

In his recent PhD thesis Yan Zhao [10] studied the deformation theory of nodal surfaces. He showed that for particular families of sextic surfaces the dimension of the deformation space equals the expected dimension. There are various deformation spaces for singular varieties (i.e., either preserving the analytic or the topological types of the singularities). However, for nodal varieties these spaces coincide and we call them "the deformation space".

Zhao's results motivated us to prove the following result.
Theorem 1.1. Let $X \subset \mathbf{P}^{3}$ be a nodal surface of degree $d$. If $d \leq 7$ or $d \geq 8$ and $X$ has at most $4(d-1)-1$ nodes then the deformation space of $X$ is smooth and has the expected dimension.

The case $d \leq 7$ was proven by Dimca [3] using different techniques. The above bound is sharp:

Theorem 1.2. Suppose $X \subset \mathbf{P}^{3}$ is a nodal surface of degree $d \geq 8$ with $4(d-1)$ nodes. Then the tangent space to the deformation space does not have the expected dimension if and only if the locus of the nodes form a complete intersection of multidegree $(1,4, d-1)$.

The proof relies on the fact that the difference between the expected dimension and the actual dimension of the tangent space at a surface $X$ equals the defect of the linear system of degree $d$ polynomials through the nodes of $X$. Then we use some ideas from [8, Proof of Theorem 4.1] to bound the Hilbert function of an ideal $I$, which has defect in certain degree, and has finite base locus in a lower degree.

As an application we discuss surfaces of the form
$$f_{1} f_{2}+f_{3}^{2} f_{4}$$
with $\operatorname{deg}\left(f_{1}\right)=1$ and $4 \leq \operatorname{deg}\left(f_{3}\right) \leq d / 2$. (See Example 4.5) We show that in the extreme case $\operatorname{deg}\left(f_{3}\right)=4$ these surfaces form the singular locus of the

\footnotetext{
The author would like to thank Arnaud Beauville for pointing out the paper [3]. The author would thank the referee for many valuable suggestions to improve the exposition.
}
deformation space, whereas in the other extreme case $\operatorname{deg}\left(f_{3}\right)=d / 2$ we show that the deformation space is smooth but not of the expected dimension.

Deformation theory of singular hypersurfaces have been studied extensively. The starting point for deformation of nodal surfaces is the paper [1]. For our applications, the slightly different presentation in [10, Chapter 3] is more suitable.

\section*{2. Preliminaries}

Let $S=\mathbf{C}\left[x_{0}, \ldots, x_{n}\right]$. For a homogeneous ideal $I \subset S$ denote with $h_{I}(k)=$ $\operatorname{dim} S / I_{k}$, the Hilbert function of $I$. Let
$$0 \rightarrow F_{s} \rightarrow F_{s-1} \rightarrow \cdots \rightarrow F_{0} \rightarrow S / I \rightarrow 0$$
be a free resolution of $S / I$, where $F_{i}=\oplus S(-j)^{\beta_{i, j}}$. If the resolution is minimal then the $\beta_{i, j}$ are called the Betti numbers of $S / I$. Under the weaker assumption that each $F_{i}$ is finitely generated we set $B_{j}=\sum_{i=0}^{s}(-1)^{i} \beta_{i, j}$. Then
$$h_{I}(k)=\sum_{j=0}^{k} B_{j}\binom{n+k-j}{n}$$
This formula allows us to recover $B_{k}$ from $h_{I}(k)$ and the $B_{j}$ with $j<k$. In particular, the $B_{j}$ are independent of the resolution. The Hilbert polynomial $p_{I}(x)$ of $I$ equals
$$\sum_{j \geq 0} B_{j} \frac{(n+x-j)(n+x-j+1) \ldots(x-j+1)}{n!} .$$
The defect of $I$ in degree $k$ is the difference $p_{I}(k)-h_{I}(k)$ and is denoted by $\delta_{k}(I)$. This equals
$$\sum_{j \geq k+n+1} B_{j} \frac{(n+k-j)(n+k-j+1) \ldots(k-j+1)}{n!}$$
which in turn equals
$$(-1)^{n} \sum_{j \geq k+n+1} B_{j}\binom{j-k-1}{n} .$$
In particular, if $I$ has defect in degree $k$ then for some $j \geq k+n+1$ we have $B_{j} \neq 0$.
Proposition 2.1. Let $\Sigma \subset \mathbf{P}^{n}$ be a closed subscheme of dimension 0. Let $I$ be the ideal of $\Sigma$. Suppose that $h_{I}(k-n) \neq \operatorname{length}(\Sigma)$. Let $t$ be a positive integer and let $f_{0}, \ldots, f_{n} \in S_{t}$ be polynomials without a common zero. Let $\varphi: \mathbf{P}^{n} \rightarrow \mathbf{P}^{n}$ given by $\left(f_{0}, \ldots, f_{n}\right)$ be the associated morphism. Let $I_{t}$ be the ideal of $\varphi^{-1}(\Sigma)$. Then
$$\operatorname{length}\left(\varphi^{-1}(\Sigma)\right)-h_{I_{t}}(t k-n-1) \geq\binom{ n+t}{n}-n .$$
Proof. Let $X$ be a scheme and let $\ell$ be a linear form such that $X \not \subset V(\ell)$. Then multiplication by $\ell$ yields an injective linear map $S / I(X)_{k} \rightarrow S / I(X)_{k+1}$. In particular, the Hilbert function of $I(X)$ is increasing. If $\operatorname{dim} X=0$ then the Hilbert polynomial is constant and therefore the defect is a decreasing function.

Therefore it suffices to prove the result for the highest possible value for $k$, i.e., we may assume that $h_{I}(j)=\operatorname{length}(\Sigma)$ for $j \geq k-n+1$. Let $B_{i}(I)$ be as defined above. Then $B_{i}(I)=0$ for $i \geq k+2$. By assumption, $\delta_{k-n}(I)$ and $\delta_{k-n-1}(I)$ are positive. Hence
$$(-1)^{n} B_{k+1}(I) \text { and }(-1)^{n}\left(B_{k+1}(I)(n+1)+B_{k}(I)\right)$$
are positive. The pull back of a free resolution of $S / I$ is a free resolution of $S / I_{t}$. In particular, $B_{j}\left(I_{t}\right)=0$ if $t \nmid j$ and $B_{t j}\left(I_{t}\right)=B_{j}(I)$. From this it follows that $\delta_{t k-n}\left(I_{t}\right)$ equals
$$(-1)^{n}\left(B_{t(k+1)}\left(I_{t}\right)\binom{n+t}{n}+B_{t k}\left(I_{t}\right)\right)=(-1)^{n}\left(B_{k+1}(I)\binom{n+t}{n}+B_{k}(I)\right) .$$
This is at least
$$(-1)^{n} B_{k+1}(I)\left(\binom{n+t}{n}-n-1\right)+1 \geq\binom{ n+t}{n}-n .$$ \(\square\)

Macaulay [9] described the possible Hilbert functions of homogeneous ideals. Gotzmann [4] described what happens in the extreme case. As a corollary we obtain the following result. (For the deduction see [8, Section 2].)

Theorem 2.2 (Macaulay-Gotzmann). Let $I \subset S$ be an ideal. If $h_{I}(k) \leq k$ then $h_{I}(k+1) \leq h_{I}(k)$. If, moreover, $I_{k+1}$ is base point free then $h_{I}(k+1)<h_{I}(k)$ or $h_{I}(k)=0$.

Remark 2.3. This result is a key ingredient in various proofs of the explicit Noether-Lefschetz Theorem (e.g. [6]) and is also used in the author's proof [8] for the fact that a nodal hypersurfaces of degree $d$ in $\mathbf{P}^{4}$ with less than $(d-1)^{2}$ nodes is factorial.

In the following we use the Alexander polynomial of hypersurfaces with isolated singularities. Suppose $X=V(f) \subset \mathbf{P}^{n}$ is a hypersurface with isolated singularities. Then $f$ defines an affine hypersurface in $\mathbf{A}^{n+1}$ with a one-dimensional singular locus. Let $F=V(f-1) \subset \mathbf{A}^{n+1}$ be the affine Milnor fiber. Fix a primitive $d$-th root of unity $\zeta$. Let $T$ be the map multiplying each $x_{i}$ with $\zeta$. Then $T$ acts on $F$. The Alexander polynomial $\Delta_{X}(t)$ of $X$ is the characteristic polynomial of $T^{*}$ acting on $H^{n-1}(F)$.

Proposition 2.4. Let $X \subset \mathbf{P}^{n}$ is a hypersurface with isolated singularities. Then the only zeros of the Alexander polynomial are $d$-th roots of unity. Let $\alpha$ be a root of unity different from one. Then one can bound the exponent of $(t-\alpha)$ in $\Delta_{X}$ by
$$(-1)^{n+1} \frac{1-(-1)^{n}(d-1)^{n}}{d} .$$
Proof. Let $H$ be a general hyperplane then it follows from [2, Theorem 4.1.24] that $\Delta_{X}(t)$ divides the characteristic polynomial of the monodromy of the Milnor fiber $F^{\prime}$ associated with $X \cap H$. From [2, Example 4.1.23] it follows that the latter polynomial equals $(t-1)^{(-1)^{n}}\left(t^{d}-1\right)^{\chi}$, with $\chi=(-1)^{n+1} \frac{1-(-1)^{n}(d-1)^{n}}{d}$. \(\square\)

In the surface case $(n=3)$ we find that the exponent is at most $d^{2}-3 d+3$. The following result explains how to calculate the Alexander polynomial of a nodal hypersurface:

Theorem 2.5 (Dimca, [2, Theorem 6.4.5]). Let $X \subset \mathbf{P}^{n}$ be a nodal hypersurface of degree $d$. Let $\Sigma \subset X$ be the locus of the nodes. Then the Alexander polynomial $\Delta_{X}(t)$ of $X$ equals
$$\left(t-(-1)^{n}\right)^{\delta}$$
with $\delta=0$ if $d n$ is odd and $\delta$ equals the defect of $I(\Sigma)$ in degree $\frac{n d}{2}-n-1$ if $d n$ is even.

\section*{3. Deformations of nodal surfaces}

In [1] and [10] the deformation theory of a degree $d$ nodal surface $X$ in $\mathbf{P}^{3}$ is studied. In both texts the authors consider deformations of the minimal resolution of singularities of $X$ (as an abstract variety) preserving the -2 curves. Moreover, Zhao studies deformations of $X$ as $V$-manifold.

It turns out that for $d \geq 5$ the deformation space is unobstructed if and only if the ideal of the nodes of $X$ does not have defect in degree $d$.

A different approach to study deformation of hypersurfaces with isolated singularities is due to Greuel and several collaborators including Shustin, and Shustin's students. The first paper taking this approach seems to be [7]. Although most of their results are for plane curves only, some of their results hold for arbitrary hypersurfaces. In this case they fix an ambient variety $Y$ and a divisor $\mathcal{L}$ on $Y$. They consider two equivalence relations among singularities, namely equianalytic and equisingular. Then for a choice of one of the equivalence relations and fixed types $T_{1}, \ldots T_{s}$ they consider the locus $V_{|\mathcal{L}|}\left(T_{1}, \ldots, T_{s}\right)$ of hypersurfaces in $|\mathcal{L}|$ with singularities of type $T_{1}, \ldots, T_{s}$.

Consider now the case of $s$ nodes. Then the two equivalence relations coincide and we denote with $V_{|\mathcal{L}|}\left(s A_{1}\right)$ the subspace of $|\mathcal{L}|$ of hypersurfaces with $s$ nodes. We expect that this locus has codimension $s$ inside $\mathcal{L}$. In e.g., [5] it is shown that the codimension of the tangent space at $X \in V_{|\mathcal{L}|}\left(s A_{1}\right)$ equals $s-\delta$ where $\delta$ is the defect of the linear system of polynomials in $|\mathcal{L}|$ vanishing at the $s$ nodes of $X$. I.e., the difference between expected and actual dimension of the tangent space is the same in both theories.

The main differences between the two approaches is the following: in the first approach one finds that the tangent space to the deformation space can be identified with $(I / J)_{d}$, where $I$ is the ideal of the nodes and $J$ is the Jacobian ideal of $X$, and in the second approach the tangent space can be identified with $I_{d} / \mathbf{C} F$, where $F$ is the defining polynomial of $X$. If $d \geq 3$ then $\operatorname{dim} J_{d}=16$ (see [3, Corollary 4.3] or [10, Proposition 3.3.8]). In this case one has a natural identification between $J_{d} / F$ and the tangent space to $\operatorname{Aut}\left(\mathbf{P}^{3}\right)$.

In the cases $d=2$ and $d=4$ one has to be a bit more careful. In the case $d=2$ a surface with a node has infinite automorphisms group and in the case $d=4$ there is a difference between embedded deformations (i.e., deformations as a surface in $\mathbf{P}^{3}$ ) and abstract deformations.

\section*{4. Proof of Theorems}

The following proposition is the same as [3, Corollary 1.3], but our proof is different from Dimca's proof.

Proposition 4.1. Let $X$ be a nodal surface of degree $d$. Let $\Sigma$ be the locus of points where $X$ has a node and let $I=I(\Sigma)$. Then $h_{I}(k)=\# \Sigma$ for $k>\frac{3}{2} d-4$.

In particular, if $h_{I}(d)<\# \Sigma$ then $d \geq 8$.
Proof. Let $s$ be an even integer. Take a general degree- $s$ base change $\varphi: \mathbf{P}^{3} \rightarrow \mathbf{P}^{3}$. Let $\tilde{I}$ be the ideal of the nodes of $\tilde{X}:=\varphi^{-1}(X)$. Since $\varphi$ is general we may assume that $\tilde{I}$ is the pull back of $I$ under $\varphi$.

If $h_{I}(k)<\# \Sigma$ for some $k>\frac{3}{2} d-4$ then $\delta_{\tilde{I}}\left(\frac{3}{2} s d-4\right) \geq\binom{ s+3}{3}-3$ by Proposition 2.1
By Theorem 2.5 we have that $\delta_{\tilde{I}}\left(\frac{3}{2} s d-4\right)$ is the exponent of $(t+1)$ in the Alexander polynomial of $\varphi^{-1}(X)$ and by Proposition 2.4 this exponent is at most
$(s d)^{2}-3 s d+3$. For $s$ sufficiently large this is smaller than $\binom{s+3}{3}-3$ and we have a contradiction. Hence $h_{I}(k)=\# \Sigma$ for $k>\frac{3}{2} d-4$. \(\square\)

Remark 4.2. This proposition is the same as [3, Corollary 1.3]. Dimca bounds the degree of the syzygies by using spectral sequences and an argument comparing the Hodge filtration and the pole order filtration on the cohomology of the complement of the affine Milnor fiber associated with the defining polynomial of $X$.

Proposition 4.3. Let $X$ be a nodal surface of degree $d$. Suppose $d \geq 8$. Let $I$ be the ideal of the nodes of $X$. If $X$ has at most $4 d-5$ nodes then $h_{I}(d)=\# \Sigma$. If $X$ has $4 d-4$ nodes and $h_{I}(d)<\# \Sigma$ then $I$ is a complete intersection ideal of degree $(1,4, d-1)$.

Proof. Let $\ell$ be a general linear form. Let $I_{H}=(I, \ell)$. Consider the exact sequence
$$0 \rightarrow(S / I)_{k} \xrightarrow{\ell}(S / I)_{k+1} \rightarrow\left(S / I_{H}\right)_{k+1} \rightarrow 0 .$$
Denote with $I_{H}=(I, \ell)$. From this exact sequence it follows that
$$h_{I}(k)=\sum_{j=0}^{k} h_{I_{H}}(k) .$$

Suppose now that $h_{I}(d)<\# \Sigma$. If for some $k \geq 0$ we have that $h_{I_{H}}(k)=0$ then for all $m \geq k$ we have $h_{I_{H}}(m)=0$. In particular, $h_{I}(m)$ is constant for $m \geq k-1$. Since $h_{I}(d)<\# \Sigma$ and $h_{I}(k)=\# \Sigma$ for $k$ large, we find that $h_{I_{H}}(d+1) \neq 0$.

We construct now the following ideal $J$. Take $J_{d+1}$ such that $\left(I_{H}\right)_{d+1} \subset J_{d+1}$ and $h_{J}(d+1)=1$. For $k<d+1$ set
$$J_{k}=\left\{f \in S_{k}: f S_{d+1-k} \subset J_{d+1}\right\}$$
and set $J_{k}=S_{k}$ for $k>d+1$. Now set $J=\oplus_{k} J_{k}$. Then $J$ contains $I_{H}$. Moreover, $J$ is closed under addition and under multiplication by -1. To show that $J$ is an ideal we have to show that for every $f \in J_{k}, g \in S_{m}$ the product $f g$ is contained in $J_{k+m}$. If $k+m \geq d+2$ then $J_{k+m}=S_{k+m}$ and there is nothing to prove. If $k+m \leq d+1$ then for every $h \in S_{d+1-k-m}$ we have $(f g) h=f(g h) \in f S_{d+1-k} \subset J_{d+1}$. Hence $f g \in J$ and $J$ is an ideal.

We constructed $J$ in such a way that for any integer $k$ the pairing $(S / J)_{k} \times$ $(S / J)_{d+1-k} \rightarrow(S / J)_{d+1} \cong \mathbf{C}$ is perfect, i.e., $S / J$ is Artinian Gorenstein with socle degree $d-1$. In particular, $h_{J}(k)=h_{J}(d+1-k)$.

The vector space $I_{d-1}$ contains all partial derivatives of the defining polynomial of $X$. In particular, it has a finite base locus and therefore $\left(I_{H}\right)_{d-1}$ has empty base locus. Hence also $J_{d-1}$ has empty base locus. Since $d-2>4$ we can apply Theorem 2.2 to obtain $h_{J}(d) \geq 2, h_{J}(d-1) \geq 3$ and $h_{J}(d-2) \geq 4$. Applying Theorem 2.2 again we find that $h_{J}(k) \geq 4$ for $k \geq 4$. Using that $S / J$ is Aritinian Gorenstein we obtain that $h_{J}(3)=h_{J}(d-2) \geq 4$. Similarly we find $h_{J}(k) \geq k+1$ for $k=0,1,2$. All in all we find
$$\# \Sigma \geq h_{I}(d+1)=\sum_{k=0}^{d+1} h_{I_{H}}(k) \geq \sum_{k=0}^{d+1} h_{J}(k) \geq 4 d-4 .$$
Hence if $\# \Sigma<4 d-4$ then $h_{I}(d)=\# \Sigma$.

Consider now the extreme case, i.e., $h_{I}(d)<\# \Sigma$ and $\# \Sigma=4(d-1)$. Then from the above discussion it follows that $I_{H}=J$ and we have that
$$h_{I_{H}}(k)=\left\{\begin{array}{cl}
k+1 & \text { for } 0 \leq k \leq 2 \\
4 & \text { for } 3 \leq k \leq d-2 \\
d+2-k & \text { for } d-1 \leq k \leq d+1
\end{array}\right.$$
Using (1) we find that $h_{I}(k)=\frac{1}{2}(k+1)(k+2)$ for $k \in\{0,1,2\}$, that $h_{I}(k)=4 k-2$ for $3 \leq k \leq d-2$ and $h_{I}(d-1)=4(d-1)-2-1$. Hence $h_{S}(1)-h_{I}(1)=1$ and therefore $I$ has a generator $f_{1}$ in degree 1. The ideal generated by $f_{1}$ and the ideal $I$ have the same Hilbert function up to degree 3, but their Hilbert functions differ in degree 4, so $I$ has another generator $f_{2}$ in degree 4. The ideal $\left(f_{1}, f_{2}\right)$ is the ideal of a quartic plane curve. Its Hilbert function equals $4 k-2$ for $k \geq 4$. Hence $I_{k}=\left(f_{1}, f_{2}\right)_{k}$ for $k \leq d-2$. However, for degree $k-1$ we find that $h_{I}(k-1)$ is one less than the Hilbert function of $\left(f_{1}, f_{2}\right)$. Hence there is a third generator for $I$ in degree $d-1$. As remarked above we have that $I_{d-1}$ has finite base locus. Hence $f_{1}, f_{2}, f_{3}$ define a complete intersection, containing $\Sigma$. The length of this complete intersection equals $4(d-1)$. Since $\Sigma$ has the same length we find that $\Sigma$ is a complete intersection of multidegree $(1,4, d-1)$. \(\square\)

Remark 4.4. In the case that $h_{I}(d)<\# \Sigma$ and $\# \Sigma=4(d-1)$ we have that $I=\left(g_{1}, g_{2}, g_{3}\right)$, with $\operatorname{deg}\left(g_{1}\right)=1, \operatorname{deg}\left(g_{2}\right)=4, \operatorname{deg}\left(g_{3}\right)=d-1$. Since $I$ is a complete intersection ideal we have that $I^{2}$ is generated by products of the generators of $I$. From $f \in I^{2}$ and $\operatorname{deg}\left(g_{3}^{2}\right)>\operatorname{deg}(f)$ it now follows that $f \in\left(g_{1}, g_{2}\right)$, i.e., the quartic curve containing all the nodes is contained in $X$.

Proof of the Theorems. Let $X \subset \mathbf{P}^{3}$ be a nodal surface. As argued in the previous section we have that the tangent space to the deformation space of $X$ has the expected dimension if and only if the ideal of the nodes of $X$ does not have defect in degree $d$. By the previous two propositions the latter can only happen if $d \geq 8$ and $\# \Sigma \geq 4 d-4$. If $d \geq 8$ and $\# \Sigma=4 d-4$ holds and the tangent space has too large dimension if and only if the ideal of the nodes is a complete intersection of degree $(1,4, d-1)$. \(\square\)

Finally, we would like to discuss whether the defect of $I$ in degree $d$ can be explained by singularities of the deformation space or is induced by deformation spaces with excessive dimension.

Example 4.5. Let $d \geq 8$ and let $4 \leq a \leq \frac{1}{2} d$. Suppose now we have a polynomial $f$ of degree $d$, such that the singular locus of $V(f)$ contains a complete intersection $\Sigma$ of multidegree $(1, a, d-1)$. For the moment assume that the plane containing $\Sigma$ is given by $x_{0}=0$. Then we can find $f_{2} \in \mathbf{C}\left[x_{1}, x_{2}, x_{3}\right]_{a}, g \in \mathbf{C}\left[x_{1}, x_{2}, x_{3}\right]_{d-1}$ such that $I(\Sigma)=\left(x_{0}, f_{2}, g\right)$.

Since $f$ has double points at $\Sigma$ we find that $f \in\left(x_{0}, f_{2}, g\right)^{2}$. From the fact that $\left(x_{0}, f_{2}, g\right)$ is a complete intersection ideal it follows that its square is generated by all products of two generators of $\left(x_{0}, f_{2}, g\right)$. Each generator of degree at most $d$ is divisible by $x_{0}$ except for $f_{2}^{2}$. In particular, there exist polynomials $f_{1} \in$ $\mathbf{C}\left[x_{0}, x_{1}, x_{2}, x_{3}\right]_{d-1}$ and $f_{3} \in \mathbf{C}\left[x_{1}, x_{2}, x_{3}\right]_{d-2 a}$ such that
$$f=x_{0} f_{1}+f_{2}^{2} f_{3} .$$
This decomposition is unique, except for the fact that we may multiply $f_{3}$ by a non-zero constant and divide $f_{2}$ by the square of the same constant. Conversely,
every $f$ of the above form defines a surface singular at $x_{0}=f_{1}=f_{2}=0$. Hence the locus $L_{0} \subset S_{d}$ of polynomials $f$ such that $V(f)_{\text {sing }}$ contains a complete intersection $\Sigma$ of multidegree $(1, a, d-1)$ and $\Sigma \subset V\left(x_{0}\right)$ has dimension
$$\binom{d-1+3}{3}+\binom{a+2}{2}+\binom{d-2 a+2}{2}-1 .$$
If we drop the condition $\Sigma \subset V\left(x_{0}\right)$ we find a locus $L$ of dimension
$$\binom{d-1+3}{3}+\binom{a+2}{2}+\binom{d-2 a+2}{2}+2 .$$
Its codimension in $S_{d}$ equals
$$\frac{1}{2}\left(-5 a^{2}+3 a+4 d a-6\right)$$
For small $a$ this codimension is larger than the number of nodes. Hence for small $a$ we have that $L$ is a proper closed subset of some component of the deformation space. The smallest $a$ possible is $a=4$. In that case we have by the results of this section that $h_{I}(d)=4(d-1)$. In particular, for $a=4$ we have $L$ is precisely the singular locus of the space of degree $d$ surfaces with $4(d-1)$ nodes.

For
$$\frac{1}{10} 2 d+5+\sqrt{4 d^{2}+20 d-95}<a<\frac{1}{2} d$$
we have that the codimension of $L$ in $S_{d}$ is less than $a(d-1)$. However, the codimension of $L$ in $S_{d}$ is strictly larger than $h_{I}(d)$. So either $L$ is a component of the deformation space, and this component is nonreduced or $L$ is a proper closed subset in a larger component.

Finally, if $d$ is even and $a=\frac{1}{2} d$ then the codimension of $L$ in $S_{d}$ equals $h_{I}(d)$. In particular, $L$ is an irreducible component of the deformation space and this component is smooth and not of the expected dimension.

We have two geometric-topological characterisations for the case $a=\frac{1}{2} d$.
If $a<1 / 2 d$ then we have that $\operatorname{rank} \mathrm{CH}^{1}(X)>1$, (i.e., the hyperplane section and the degree $a$ curve $f_{1}=f_{3}=0$ are linearly independent in $\mathrm{CH}^{1}(X)$ ), whereas for $a=\frac{1}{2} d$ we have $\operatorname{rank} \mathrm{CH}^{1}(X)=1$ for very general $X$.

A second characterisation is given by the Alexander polynomial, this polynomial is a constant polynomial in the case $a<\frac{1}{2} d$ and equals ( $t+1$ ) in the case $a=\frac{1}{2} d$.

\section*{References}
\begin{itemize}
\item[] [1] D. M. Burns, Jr. and J. M. Wahl. Local contributions to global deformations of surfaces. Invent. Math., 26:67-88, 1974.
\item[] [2] A. Dimca. Singularities and topology of hypersurfaces. Universitext. Springer-Verlag, New York, 1992.
\item[] [3] A. Dimca. On the syzygies and Hodge theory of nodal hypersurfaces. Preprint available at arxiv:math/1310.5344v1, 2013.
\item[] [4] G. Gotzmann. Eine Bedingung für die Flachheit und das Hilbertpolynom eines graduierten Ringes. Math. Z., 158:61-70, 1978.
\item[] [5] A. Gourevitch and D. Gourevitch. Geometry of obstructed equisingular families of algebraic hypersurfaces. J. Pure Appl. Algebra, 213:1865-1889, 2009.
\item[] [6] M.L. Green. Components of maximal dimension in the Noether-Lefschetz locus. J. Differential Geom., 29:295-302, 1989.
\item[] [7] G.-M. Greuel and U. Karras. Families of varieties with prescribed singularities. Comp. Math., 69:83-100, 1989.
\end{itemize}
\begin{itemize}
\item[] [8] R. Kloosterman. Maximal families of nodal varieties with defect. Preprint, available at arXiv:1310.0227v1, 2013.
\item[] [9] F. S. Macaulay. Some Properties of Enumeration in the Theory of Modular Systems. Proc. London Math. Soc., S2-26:531, 1927.
\item[] [10] Y. Zhao. Deformations of nodal surfaces. PhD thesis, Leiden University, 2016. Available at https://openaccess.leidenuniv.nl/handle/1887/44549.
\end{itemize}

Università degli Studi di Padova, Dipartimento di Matematica, Via Trieste 63, 35121 Padova, Italy
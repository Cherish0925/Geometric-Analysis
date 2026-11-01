---
retention_scope: session
part: 1
total_parts: 1
---

---
source_file: math_9808052.pdf
converter: mathpix
format: mmd
---

\title{
Surgery and the Yamabe invariant
}

\author{
Jimmy Petean \\ Max-Planck Institut für Mathematik, Bonn, Germany \\ and Gabjin Yun ${ }^{1}$ \\ Department of Mathematics \\ Myong-Ji University, Korea
}

\begin{abstract}
We study the Yamabe invariant of manifolds obtained as connected sums along submanifolds of codimension greater than 2. In particular: for a compact connected manifold $M$ with no metric of positive scalar curvature, we prove that the Yamabe invariant of any manifold obtained by performing surgery on spheres of codimension greater than 2 on $M$ is not smaller than the invariant of $M$.
\end{abstract}

\section*{1 Introduction}

Given a smooth compact manifold $M^{n}$ of dimension $n$ the Yamabe invariant of $M$ is defined in the following way: first pick a conformal class $\mathcal{C}$ of Riemannian metrics on $M$ and let
$$Y(M, \mathcal{C})=\inf _{g \in \mathcal{C}} \frac{\int_{M} s_{g} d v o l_{g}}{\left(\operatorname{Vol}_{g}(M)\right)^{\frac{n-2}{n}}} .$$
Here $s_{g}$ is the scalar curvature of $g$ and $\operatorname{Vol}_{g}(M)$ is the volume of $M$ with respect to the metric $g$. Then
$$Y(M)=\sup _{\mathcal{C}} Y(M, \mathcal{C})$$

\footnotetext{
${ }^{1}$ Supported in part by KOSEF 960-7010-201-3.
}
is the Yamabe invariant of $M$ (the supremum is taken over the family of all conformal classes of metrics on $M$ ). This invariant was introduced by O. Kobayashi in [5] and it is also frequently called the sigma constant of $M$. Note that $Y(M)$ is an invariant of the smooth structure of $M$.

Yamabe first considered what we called $Y(M, \mathcal{C})$ in [10]. He gave a proof that $Y(M, \mathcal{C})$ is always achieved by a metric in $\mathcal{C}$. His proof contained a mistake pointed out by Trudinger [9], and fixed in succesive steps by Trudinger, Aubin [3] and Schoen [8]; so proving that in every conformal class there is a metric with constant scalar curvature. A basic fact about the Yamabe invariant is that it is positive if and only if the manifold admits a metric of positive scalar curvature. The study of the invariant is then naturally divided into two cases: when $Y(M)>0$ and when $Y(M) \leq 0$.

We will be concerned in this paper with manifolds for which the Yamabe invariant is non-positive. In this case, every conformal class admits a unique metric of unit volume and constant scalar curvature. That constant is precisely the Yamabe constant of the conformal class. Hence the Yamabe invariant in this case is the supremum of the scalar curvature over the space of metrics of constant scalar curvature and unit volume. Also in this case, we can express the Yamabe invariant as
$$Y(M)=-\left(\inf _{\mathcal{M}} \int_{M}\left|s_{g}\right|^{n / 2} d v o l_{g}\right)^{2 / n},$$
where $\mathcal{M}$ is the space of Riemannian metrics on $M$ (c.f. [2], [6]). So the study of the Yamabe invariant in this case is equivalent to the study of the infimum of this natural Riemannian functional. This is clearly not true in the positive case, where the infimum considered is always zero.

Computations of the invariant are not easy to carry out. Nevertheless, there has been some success in low dimensions. In dimension 4, LeBrun computed the invariants for all compact Kähler surfaces with non-positive Yamabe invariant (see [6]). The computations of the invariant for 3-dimensional manifolds (always with non-positive invariant) are a by-product of Anderson's program for the hyperbolization conjecture (see [1]). The invariants are readily computable in dimension 2 from the Gauss-Bonnet formula.

We will prove the following:

Theorem 1 Let $M_{1}, M_{2}$ be compact smooth $n$-dimensional manifolds. Suppose that a $k$-dimensional manifold $W$ embedds into both $M_{1}$ and $M_{2}$ with trivial normal bundle. Assume $k<n-2$. Let $M_{1,2}^{W}$ be the manifold obtained by gluing $M_{1}$ and $M_{2}$ along $W$. Then
\begin{itemize}
\item[a)] If $Y\left(M_{i}\right) \leq 0$, then $Y\left(M_{1,2}^{W}\right) \geq-\left[\left(-Y\left(M_{1}\right)\right)^{n / 2}+\left(-Y\left(M_{2}\right)\right)^{n / 2}\right]^{2 / n}$.
\item[b)] If $Y\left(M_{1}\right) \leq 0$ and $Y\left(M_{2}\right)>0$ then $Y\left(M_{1,2}^{W}\right) \geq Y\left(M_{1}\right)$.
\end{itemize}
Here as usual $M_{1,2}^{W}$ is constructed by deletting the image of $W$ on both $M_{1}$ and $M_{2}$ and then identifying $x \in M_{1}-W$ with $h_{2} j h_{1}^{-1}(x)$, where $h_{i}$ is a trivialization of the normal bundle of $W$ in $M_{i}$ (i.e. a diffeomorphism between the normal bundle and a tubular neighbourhood of $W$ ) and $j$ is the inversion in $\mathbf{R}^{n-k}-\{0\}\left(j(v)=v /\|v\|^{2}\right)$. The resulting $M_{1,2}^{W}$ will depend on (the homotopy class of) the trivializations $h_{i}$ although we do not make this explicit in our notation.

In particular, we have:
Corollary 1 If $\hat{M}$ is obtained from $M$ by performing surgery of codimension at least 3 and $Y(M) \leq 0$ then $Y(\hat{M}) \geq Y(M)$.

Note that O. Kobayashi [5] has proved the 0-dimensional case of this result (i.e. for connected sums at points).

In the next section we will carry out the main computations. We will show that given a metric $g$ on $M$, we can deform $g$ on the end of $M-W(W$ is an embedded submanifold of codimension at least 3) without appreciably changing the volume or the minimum of the scalar curvature (more precisely, for any positive $\epsilon$ we will show that we can construct a deformation with scalar curvature bounded below by $s_{g}-\epsilon$ and volume bounded above by $\operatorname{Vol}_{g}(M)+\epsilon$ ). Moreover we will be able to "choose" how the metric looks like at the end of $M-W$. This will be done following the constructions of Gromov-Lawson [4] and Schoen-Yau [7]. In the last section we will use this construction to prove the results we mentioned.

\section*{2 The main construction}

Let $(M, g)$ be a compact smooth Riemannian manifold of dimension $n$. Let $W$ be a $k$-dimensional embedded submanifold $(k \leq n-3)$ with trivial normal bundle $N$. Also let $S$ be the unit sphere bundle of $N$. Of course, $M-W$ has an end diffeomorphic to $S \times(0,1)$. In this section we will construct, for any positive (small) constant $\epsilon_{0}$, a metric $\hat{g}$ on $M-W$ which verifies:
\begin{itemize}
\item[a)] $\hat{g}=g$ away from the end.
\item[b)] the scalar curvature, $s_{\hat{g}}$, of $\hat{g}$ is greater than $s_{g}-\epsilon_{0}$ everywhere.
\item[c)] $\operatorname{Vol}_{\hat{g}}(M-W) \leq \operatorname{Vol}_{g}(M)+\epsilon_{0}$.
\item[d)] at the end $\hat{g}=h+d E^{2}+d t^{2}$, where $h$ is any metric on $W$ picked
\end{itemize} previously, $d E^{2}$ is the Euclidean metric on the sphere $S^{n-k-1}(r)$ and $d t^{2}$ is the Euclidean metric on the line. The positive number $r$ can be taken as small as desired.

In the next section we will use this construction to prove the results mentioned in the introduction.

We will separate our task into two steps:
Step 1: construct $\hat{g}$ satisfying (a), (b) and (c) so that in the end it looks like the product of the Euclidean metric on the line and the metric $g_{\delta}$ induced by $g$ on the $\delta$-sphere bundle of $N$ (here we will be able to pick $\delta$ as small as we want).

Step 2: for $\delta$ small enough find a homotopy $d s_{t}, 0 \leq t \leq 1$, between the metric $g_{\delta}$ and any metric like the one described in d) so that the "total" metric $d s_{t}+d t^{2}$ on $S \times[0,1]$ has positive scalar curvature everywhere and has volume as small as we want. Note that we will use this construction for metrics of non-positive scalar curvature, hence this will be enough to verify condition (b).

Let us begin with Step 1. The construction can be done following the one by Gromov and Lawson [4] in their study of metrics with positive scalar curvature (see also [7]). We will only sketch briefly those parts where the construction in [4] applies directly to our case.

First choose a positive number $\epsilon$ so that the exponential map gives a diffeomorphism between the $\epsilon$ ball in the normal bundle and an open neigh-
bourhood $U_{\epsilon}$ of $W$ in $M$. Of course, we can pick $\epsilon$ as small as we want. Let $N_{\epsilon}$ denote the $\epsilon$ ball in the normal bundle, i.e. $N_{\epsilon}=\{(x, y) \in N:\|y\|<\epsilon\}$. Pull back the metric $g$ from $M$ to $N_{\epsilon}$ via the exponential map. We will still call this metric on $N_{\epsilon}$ by $g$.

For any $0<\delta<\epsilon$ we will denote by $S^{\delta} N$ the (n-k-1)-sphere bundle of points in $N$ of norm $\delta$ and we will call $g_{\delta}$ the restriction of $g$ to $S^{\delta} N$. Also, for any point $(x, y) \in N$, let $r(x, y)=\|y\|$ denote the distance (measured by $g)$ from $(x, y)$ to $W$.

Now pick any $r_{1}$ so that $0<r_{1}<\epsilon$. In the plane with coordinates $(t, r)$ consider a smooth curve $\gamma$ which moves vertically from $(0, \epsilon)$ to $\left(0, r_{1}\right)$, then is the graph of a strictly decreasing function $h$ joinning the points $\left(0, r_{1}\right)$ and $\left(t_{f}, r_{f}\right)$, and then stays on the horizontal line $r=r_{f}$ (here $t_{f}$ is a positive number and $0<r_{f}<r_{1}$ ).

Let $M^{\gamma}=\left\{((x, y), t) \in N_{\epsilon} \times \mathbf{R}:(r(x, y), t) \in \gamma\right\}$. Let $g^{\gamma}$ denote the restriction to $M^{\gamma}$ of the product metric $g+d t^{2}$ ( $d t^{2}$ denotes the Euclidean metric on the line). To complete Step 1 we need to show that we can pick $\gamma$ so that the metric $g^{\gamma}$ has the required restrictions on scalar curvature and volume (from the shape of $\gamma$ one can immediately see that $g^{\gamma}$ will verify condition (a) and will have the required form at the end).

Let us study the volume of $g^{\gamma}$. More precisely, we will describe what conditions must verify $\gamma$ in order that the volume of $M^{\gamma}$ is bounded by some chosen small positive constant $u$.

The horizontal piece of $\gamma$ can be taken arbitrarily small. So we only need to consider the volume of the part of $\gamma$ corresponding to the graph of $h$.

We will then restrict our attention to the piece of $\gamma$ given by the graph of $h$. But to avoid introducing new notation we will keep calling $\gamma$ the smaller curve and $g^{\gamma}$ the restriction of the metric to this piece. To estimate the volume of $g^{\gamma}$ we will compare its volume element to the one of the original metric $g$. Of course, dvol $_{g^{\gamma}}=$ dvol $_{g^{\gamma}}\left(e_{1}, \ldots, e_{n}\right)$ dvol $_{g}$; where $e_{1}, \ldots, e_{n}$ form a $g$-orthonormal basis (at certain point).

Let $h^{-1}:\left(r_{f}, r_{1}\right) \rightarrow\left(0, t_{f}\right)$ be the inverse function of $h$. Consider the map
$$F: N_{r_{1}}-\overline{N_{r_{f}}} \rightarrow M^{\gamma}$$
given by $F(x, y)=\left(x, y, h^{-1}(r(x, y))\right) . F$ is clearly a diffeomorphism (onto the part of $\gamma$ corresponding to the graph of $h$ ) and we will use it to bring the
metric $g^{\gamma}$ to $N_{r_{1}}-\overline{N_{r_{f}}}$.
The function $r: N_{r_{1}}-\overline{N_{r_{f}}} \rightarrow \mathbf{R}$ is a smooth submersion. So, at any point $q=(x, y) \in N_{r_{1}}-\overline{N_{r_{f}}}$, the kernel of $r_{* q}$ has dimension $n-1$. Let $e_{2}, \ldots, e_{n}$ be a $g$-orthonormal basis of $\operatorname{Kernel}\left(r_{* q}\right)$. And let $e_{1}$ be a unitary vector orthogonal to that space.

We have to compute $\left(\text { dvol }_{g^{\gamma}}\right)_{F(q)}\left(F_{* q} e_{1}, \ldots, F_{* q} e_{n}\right)$. Now for $i=2, . ., n$ we have $F_{* q} e_{i}=\left(e_{i}, 0\right)$ as elements of $T_{q} M \oplus T_{F(q)} \mathbf{R}$. Moreover,
$$\left(\operatorname{dvol}_{g^{\gamma}}\right)_{F(q)}\left(F_{* q} e_{1}, \ldots, F_{* q} e_{n}\right)=\sqrt{\operatorname{det}\left(g^{\gamma}\left(F_{*} e_{i}, F_{*} e_{j}\right)_{i j}\right)} .$$

It follows from the previous considerations that the (n-1)×(n-1) matrix obtained by deletting the first row and column of $g^{\gamma}\left(F_{*} e_{i}, F_{*} e_{j}\right)_{i j}$ is the identity. But also,
$$g^{\gamma}\left(F_{*} e_{i}, F_{*} e_{1}\right)=\delta_{i 1}+d t^{2}\left(\left(h^{-1} r\right)_{*} e_{i},\left(h^{-1} r\right)_{*} e_{1}\right) .$$
Hence the matrix is diagonal, having 1 in all but the first diagonal entry and $1+d t^{2}\left(\left(h^{-1} r\right)_{*} e_{i},\left(h^{-1} r\right)_{*} e_{1}\right)$ in the first.

We need to compute, or estimate, $\left(h^{-1} r\right)_{*} e_{1}$.
Claim: Pick any small positive constant $u$. If $r_{1}$ is small enough then at any $q$ in $N_{r_{1}}-W$ we have $\left|r_{* q} e_{1}-1\right| \leq u$. Here we are identifying the tangent space of the real line with the real numbers, and we are picking the $e_{1}$ "with the right sign".

To prove the claim, let $\left(x_{1}, \ldots, x_{k}\right)$ be coordinates for $W$ on an open set $U$. Pick an orthonormal frame for $N$ over $U$ and let $\left(y_{1}, \ldots, y_{n-k}\right)$ be the induced coordinates on the fibers. Hence $(r(x, y))^{2}=y_{1}^{2}+\ldots+y_{n-k}^{2}$.

In $U \times D^{n-k}\left(r_{1}\right)$ it is easy to find a $g$-orthonormal basis for the kernel of $r_{*}$. At a point $(x, y)$ let $\frac{\partial}{\partial r}$ be the unitary vector tangent to the geodesic line from 0 to $y$. Let $v_{2}, \ldots v_{n-k}$ be an orthonormal basis of the tangent space to the sphere of radius $r(x, y)$. Let $w_{n-k+1}, \ldots, w_{n}$ be a $g$-orthonormal basis of the tangent space to $U$ at $x$. Note that at $q \in N_{r_{1}}$,
$$g\left(v_{i}, w_{j}\right) \in o\left(r_{1}\right), \quad g\left(\partial / \partial r, w_{j}\right) \in o\left(r_{1}\right)$$
and since we are in geodesic coordinates $g\left(\frac{\partial}{\partial r}, v_{i}\right)=0$. Applying the Gram-Schmidt process to the basis $v_{2}, \ldots, v_{n-k}, w_{n-k+1}, \ldots, w_{n-1}, \frac{\partial}{\partial r}$ we get an orthonormal basis. The first $n-1$ vectors will be an o.n. basis for the kernel
of $r_{*}$. The last vector, which is the vector $e_{1}$ in the claim, will differ from $\frac{\partial}{\partial r}$ by $o\left(r_{1}\right)$. But it is clear that $r_{*}\left(\frac{\partial}{\partial r}\right)=\frac{\partial}{\partial t}$ and the claim follows.

Hence, with the notation we were using before the claim,
$$g^{\gamma}\left(F_{* q} e_{1}, F_{* q} e_{1}\right)=1+(1+o(u))^{2}\left(\frac{\partial h^{-1}}{\partial t}(r(q))\right)^{2}$$

Finally,
$$\begin{gathered}
\operatorname{dvol}_{g^{\gamma}}\left(e_{1}, \ldots, e_{n}\right)=\sqrt{1+(1+o(u))^{2}\left(\frac{\partial h^{-1}}{\partial t}(r(q))\right)^{2}} \leq \\
\leq 1-(1+o(u)) \frac{\partial h^{-1}}{\partial t}(r(q))
\end{gathered}$$
and we have
$$\operatorname{Vol}_{g^{\gamma}}\left(N_{r_{1}}-N_{r_{f}}\right) \leq \operatorname{Vol}_{g}\left(N_{r_{1}}\right)-(1+o(u)) \int_{N_{r_{1}}-N_{r_{f}}} \frac{\partial h^{-1}}{\partial t}(r(q)) d v o l_{g} .$$

To estimate the last integral we will need the following result, whose proof is elementary.

Lemma 1 Given $\delta>0$ small enough, there exists a constant $\mathcal{K}$, depending on $g$ and $\delta$, such that for all $0<r_{a}<r_{b}<\delta$,
$$\operatorname{Vol}_{g}\left(N_{r_{b}}-N_{r_{a}}\right) \leq\left(r_{b}-r_{a}\right) \mathcal{K} .$$

Now we can see what are the conditions we need for $\gamma$. Suppose we want to make the volume of the portion of $M-W$ with the newly defined metric less than $\epsilon_{0}$. Picking $r_{1}$ small enough we can make the first term in (1) less than $\epsilon_{0} / 2$. It follows from the previous lemma that the second term in (1) is bounded by $2(1+o(u)) \mathcal{K} t_{f}$. As we let $r_{1}$ tend to 0, the first 3 factors in the previous product are bounded independently of $r_{1}$ (with a little effort we could prove that the product actually tends to 0, but we will not need this).

So, to keep the volume under control, we just need to construct $\gamma$ so that as $r_{1}$ tends to $0, t_{f}$ also tends to 0.

We will now show that we can construct such a curve $\gamma$ which satisties also our requirements about the scalar curvature. More precisely, given any small positive $r_{1}$ we will construct $\gamma$ so that $t_{f} \leq 7 r_{1}$ and $s_{g^{\gamma}} \geq s_{g}-\epsilon_{0}$ (where $\epsilon_{0}$ is a positive number we fixed previously).

Let $\theta$ be the angle between the $r$-axis and the tangent to $\gamma$ (at some point). Let $\kappa$ be the principal curvature of $\gamma$. We have the following formula for the scalar curvature of $g^{\gamma}$ (it is computed in [4]),
$$s_{g^{\gamma}}=s_{g}+O(1) \sin ^{2} \theta+\frac{(n-k-1)(n-k-2)}{r^{2}} \sin ^{2} \theta-(n-k-1) \frac{\kappa}{r} \sin \theta .$$
The function $O(1)$ is bounded independently of $r, \theta$ and $\kappa$. Let $\mathcal{A}$ be an upper bound for it.

To construct $\gamma$ we will be describing how we make $\theta$ vary from 0 to $\pi / 2$. Let $s$ be the arclength parameter. Let $\kappa(s)$ be the curvature of $\gamma$ at (length) $s$. The change of $\theta$ between $s_{1}$ and $s_{2}$ is given by the integral of $\kappa(s)$ (between $s_{1}$ and $s_{2}$, of course).

We will describe the function $\kappa(s)$. First pick $\theta_{0}$ so that
$$\left(\mathcal{A}+\frac{4 n}{r_{1}^{2}}\right) \sin \theta_{0}<\epsilon_{0} .$$

Bend $\gamma$ changing $\theta$ from 0 to $\theta_{0}$ by a curve of length $r_{1} / 2$. We can do this keeping $\kappa(s)$ bounded by $2 / r_{1}$, and so it is easy to see from (2) that we will have $s_{g^{\gamma}} \geq s_{g}-\epsilon_{0}$. We will continue on the straight line of angle $\theta_{0}$ till we get to a point with $r=r_{2}<\left(\sin \theta_{0}\right) / \mathcal{A}$. We will now make a new bend of length $r_{2} / 2$. In order to keep the desired inequality for the scalar curvature it is enough to keep $\kappa(s)$ bounded by $\left(\sin \theta_{0}\right) / 2 r_{2}$; hence we will increase $\theta$ by about $\left(\sin \theta_{0}\right) / 4$. Then we will continue again in a straight line (of angle $\theta_{1}$ ) for an arbitrarily small period of time. We will repeat this process until we got to a horizontal line ( $\theta=\pi / 2$ ). Note that the amount of $\theta$ we can increase at every bend is about $\left(\sin \theta_{n-1}\right) / 4$ (where $\theta_{n-1}$ is the angle previous
to the new bending). It is then clear that we need to repeat the process only a finite number of times. Now pick $i$ so that $\sin \theta_{i}$ is about $1 / 2$. Then we will clearly finish the process at the step $i+10$. Hence the length of $\gamma$ in this last part of the process is bounded by $5 r_{1}$. On the other hand all the previous bends will verify that $r_{k-1}-r_{k} \geq(1 / 4) r_{k-1}$. This implies that the length of the first bends (and straight lines) are bounded by twice the decrease in $r$. Hence the total length of $\gamma$ up to the $i$-th step is bounded by $2 r_{1}$. We can then construct the whole $\gamma$ of length bounded by $7 r_{1}$. Therefore $t_{f} \leq 7 r_{1}$. This completes Step 1 of the construction.

Step 2: We have already deform $g$ so that in the end we have the product metric $g_{\delta}+d t^{2}$. We now want to find a homotopy between $g_{\delta}$ and some canonical metrics. We will have a family $g^{t}, a \leq t \leq b$ of metrics of positive scalar curvature on a compact manifold $X$ and we need to know conditions under which the metric $g^{t}+d t^{2}$, on $X \times[a, b]$, has positive scalar curvature and small volume.

The following two lemmas are the tools we need to study this problem. The first one will give us a bound on the total volume of a homotopy and is completely elementary,

Lemma 2 Let $g^{t}, a \leq t \leq b$, be a family of metrics on the compact manifold $X$. Let $d t^{2}$ be the Euclidean metric on the interval $(a, b)$ and consider the metric $G=g^{t}+d t^{2}$ on $X \times(a, b)$. We have,
$$\operatorname{Vol}_{G}(X \times(a, b)) \leq \sup _{a \leq t \leq b}\left\{\operatorname{Vol}_{g^{t}}(X)\right\}(b-a) .$$

We will be concerned with the case in which all the metrics $g^{t}$ have strictly positive scalar curvature. One can then see ([4], [7]) that doing the homotopy slowly in time (stretching the interval) the scalar curvature of the total metric is also positive. We will now write down explicitly how much we need to stretch the interval in order to get positive scalar curvature.

First we need to introduce some notation. Suppose we have a homotopy, $H=\left\{g^{t}\right\}, 0 \leq t \leq 1$, of positive scalar curvature metrics on a compact manifold $X$. Let
$$s(H)=\min _{(x, t)}\left\{s_{g^{t}}(x)\right\} .$$

Now consider a system of coordinates $\bar{x}=\left(x_{1}, \ldots, x_{n}\right)$ in some open neighbourhood in $X$. Let $G_{a}$ be the metric $g^{t}+a^{2} d t$. Let $g_{i k}(x, t)=$ $g^{t}\left(\partial / \partial x_{i}, \partial / \partial x_{k}\right)$ and let $g^{i k}$ denote as usual the coefficients of the inverse of the matrix $\left(g_{i k}\right)$. By a straightforward computation we get the following formula,
$$\begin{aligned}
s_{G_{a}}(x, t)=s_{g^{t}}(x)+ & \frac{1}{4 a^{2}}\left(g^{i k} \frac{\partial g_{j k}}{\partial t} g^{j p} \frac{\partial g_{i p}}{\partial t}-g^{i k} \frac{\partial g_{i k}}{\partial t} g^{j p} \frac{\partial g_{j p}}{\partial t}\right)(x, t) \\
& -\frac{1}{2 a^{2}}\left(g^{i k} \frac{\partial^{2} g_{i k}}{\partial t^{2}}+\frac{\partial}{\partial t}\left(g^{i k} \frac{\partial g_{i k}}{\partial t}\right)\right)(x, t),
\end{aligned}$$
where $s_{G_{a}}$ and $s_{g^{t}}$ denote the scalar curvatures of the metrics $G_{a}$ and $g^{t}$, respectively.

We will call $\mathcal{B}(x, t)$ the expression multiplied by $1 / a^{2}$ in the previous formula and $\mathcal{B}(H)$ the maximum of $\mathcal{B}(x, t)$ on $X \times[0,1]$. Note that $\mathcal{B}(x, t)$ does not depend on the system of coordinates. We have (compare to [4, Lemma 3]

Lemma 3 Let $H=g^{t}, 0 \leq t \leq 1$, be a family of metrics of strictly positive scalar curvature on the compact manifold $X$. The metric $\hat{G}_{a}=g^{t / a}+d t^{2}$ on $X \times[0, a]$ has positive scalar curvature if $a>\sqrt{\mathcal{B}(H) / s(H)}$.

Proof: Consider the map between $X \times[0,1]$ and $X \times[0, a]$ given by multiplication by $a$ in the $t$-coordinate. Pulling back the metric $\hat{G}_{a}$ via this diffeomorphism we get the metric $G_{a}=g^{t}+a^{2} d t^{2}$ on $X \times[0,1]$. The lemma now follows directly from our formula for the scalar curvature of $G_{a}$. \(\square\)

Now let us come back to our problem. We want to study the metric $g$ close to $W$. Find a coordinate system of the form $\left(x_{1}, \cdots, x_{k}, y_{k+1}, \cdots, y_{n}\right)$. Where the $x_{i}$ are coordinates for $W$ and the $y_{i}$ are coordinates on the normal bundle induced by an orthonormal frame (make the identification via the exponential map). As before $r(x, y)$ will denote the distance between the point $(x, y)$ and $W$. So $r^{2}=\Sigma y_{i}^{2}$.

The metric $g$ can be expressed in these coordinates in the form,
$$\begin{aligned}
g=\Sigma\left(g_{i j}(x, 0)+\right. & o(r)) d x_{i} d x_{j}+\Sigma o(r) d x_{i} d y_{\alpha}+ \\
& +\Sigma\left(\delta_{\alpha \beta}+o\left(r^{2}\right)\right) d y_{\alpha} d y_{\beta} .
\end{aligned}$$

We will first homotope $g_{\delta}$ to the product metric $g_{\delta}^{N}=\left.g\right|_{W}+d E^{2}(\delta)$ on $W \times S^{n-k-1}$ ( $d E^{2}(\delta)$ is the standard Euclidean metric on the $\delta$-sphere). It is easy to see from our local formula that the metrics $g_{\delta}$ and $g_{\delta}^{N}$ will differ only by low order terms. Consider the simplest homotopy $g_{\delta}^{t}=t g_{\delta}^{N}+(1-t) g_{\delta}$. In local coordinates $g_{\delta}^{t}$ will look like $g_{\delta}^{N}$ plus some terms of order $o(r)$ multiplied by $t$. If we call $H^{1}$ this family of metrics we have then that $\mathcal{B}\left(H^{1}\right)$ is bounded independently of $\delta$ (for $\delta$ smaller than some fixed small $\delta_{0}$ ). It is also clear that $s\left(H^{1}\right)$ is bounded below by some positive multiple of $1 / \delta^{2}$. We also have that the volume of the metrics $g_{\delta}^{t}$ go to 0 as we take $\delta$ small. It follows from the previous lemmas that given any $\epsilon_{0}>0$ for any $\delta$ small enough the metric $g_{\delta}^{t}+d t^{2}$ on $W \times S^{n-k-1} \times[0,1]$ will have positive scalar curvature everywhere and volume less than $\epsilon_{0}$.

Hence we can assume now that at the end we have the product metric, $g_{\delta}^{N}$, of the Euclidean metrics (on the $\delta$-sphere and on the line) and the restriction of $g$ to $W$.

Finally, we need to show that we can change the metric $\left.g\right|_{W}$ to any other metric $h$ on $W$. Consider again the homotopy $g^{t}=t\left(h+d E^{2}\right)+(1-t) g_{\delta}^{N}$. Of course, the homotopy only works on the $W$-part, while we always have the Euclidean metric on the $\delta$-sphere. Let us call $H^{2}$ this homotopy. It is again easy to see that $\mathcal{B}\left(H^{2}\right)$ is bounded independently of $\delta$ (it is actually independent of $\delta$ ), while $s\left(H^{2}\right)$ is bounded below by some positive multiple of $1 / \delta^{2}$. The volumes of the metrics $g^{t}$ tend to 0. These observations and the previous lemmas show that if $\delta$ is small enough the metric $g^{t}+d t^{2}$ on $W \times S^{n-k-1} \times[0,1]$ has positive scalar curvature and volume less than $\epsilon_{0}$.

We have therefore finished Step 2 and so our construction.

\section*{3 Proof of Theorem 1}

In this section we will use the previous construction to prove the results mentioned in the introduction. We will use the following well known result
(see [5]),
Lemma 4 Let $\mathcal{C}$ be a conformal class of Riemannian metrics on the compact $n$-dimensional manifold $M$. Assume $n \geq 3$ and $Y(M, \mathcal{C}) \leq 0$. Let $g$ be any metric in $\mathcal{C}$. Then,
$$Y(M, \mathcal{C}) \geq \min \left(s_{g}\right)\left(\operatorname{Vol}_{g}(M)\right)^{2 / n} .$$

Proof of Theorem 1: We will use the same notations as in the introduction. To begin, fix any positive $\epsilon$. Pick conformal classes $\mathcal{C}_{i}$ in $M_{i}$ so that $Y\left(M_{i}, \mathcal{C}_{i}\right) \geq Y\left(M_{i}\right)-\epsilon$ (for $i=1,2$ ). Let $g_{i}$ be the metric of volume $\lambda_{i}$ in $\mathcal{C}_{i}$ realizing $Y\left(M_{i}, \mathcal{C}_{i}\right)$. Renormalize the metrics so that $\lambda_{1}+\lambda_{2}=1$.

Now construct metrics $\hat{g}_{i}$ in $M_{i}-W$, as in the previous section (using the $\epsilon$ we have just picked), so that they coincide in the ends. Then we can glue them together to obtain a metric $\hat{g}$ on $M_{1,2}^{W}$. The volume of $\hat{g}$ satisfies
$$\operatorname{Vol}_{\hat{g}}\left(M_{1,2}^{W}\right) \leq 1+2 \epsilon$$

Note also that the scalar curvature of $g_{i}$ is constant equal to
$$s_{g_{i}}=Y\left(M_{i}, \mathcal{C}_{i}\right)\left(\lambda_{i}\right)^{-2 / n} .$$

Hence,
$$s_{\hat{g}} \geq \min \left\{\frac{Y\left(M_{1}, \mathcal{C}_{1}\right)}{\left(\lambda_{1}\right)^{2 / n}}-\epsilon, \frac{Y\left(M_{2}, \mathcal{C}_{2}\right)}{\left(\lambda_{2}\right)^{2 / n}}-\epsilon\right\}$$
everywhere. So, from the previous lemma, we get:
$$Y\left(M_{1,2}^{W}, \mathcal{C}_{\hat{g}}\right) \geq(1+2 \epsilon)^{2 / n} \min \left\{\frac{Y\left(M_{1}, \mathcal{C}_{1}\right)}{\left(\lambda_{1}\right)^{2 / n}}-\epsilon, \frac{Y\left(M_{2}, \mathcal{C}_{2}\right)}{\left(\lambda^{2}\right)_{2 / n}}-\epsilon\right\}$$

To simplify the notation, we will write $a_{i}=Y\left(M_{i}, \mathcal{C}_{i}\right)$. Assume first that both $a_{1}$ and $a_{2}$ are strictly negative. We can rescale the metrics so that $\lambda_{1}$ is any number in (0,1), and $\lambda_{2}=1-\lambda_{1}$. The minimum appearing in the previous formula will be the greatest when the two numbers are equal. This happens when
$$\lambda_{i}=\frac{\left|a_{i}\right|^{n / 2}}{\left|a_{1}\right|^{n / 2}+\left|a_{2}\right|^{n / 2}}$$
Then we get
$$\min \left\{\frac{Y\left(M_{1}, \mathcal{C}_{1}\right)}{\left(\lambda_{1}\right)^{2 / n}}-\epsilon, \frac{Y\left(M_{2}, \mathcal{C}_{2}\right)}{\left(\lambda_{2}\right)^{2 / n}}-\epsilon\right\}=-\left(\left|a_{1}\right|^{n / 2}+\left|a_{2}\right|^{n / 2}\right)^{2 / n}-\epsilon$$
and so,
$$Y\left(M_{1,2}^{W}, \mathcal{C}_{\hat{g}}\right) \geq-(1+2 \epsilon)^{2 / n}\left[\left(\left(-Y\left(M_{1}\right)+\epsilon\right)^{n / 2}+\left(-Y\left(M_{2}\right)+\epsilon\right)^{n / 2}\right)^{2 / n}+\epsilon\right] .$$
Since $Y\left(M_{1,2}^{W}\right)=\sup _{\mathcal{C}}\left\{\left(Y\left(M_{1,2}^{W}, \mathcal{C}\right)\right\}\right.$ and $\epsilon$ was arbitrary, we get
$$Y\left(M_{1,2}^{W}\right) \geq-\left[\left(-Y\left(M_{1}\right)\right)^{n / 2}+\left(-Y\left(M_{2}\right)\right)^{n / 2}\right]^{2 / n},$$
finishing the proof of Theorem 1 in this case. If $a_{i}=0$ the result follows easily making $\lambda_{i}$ tend to 0. Part b) of Theorem 1 follows in the same way since the fact that $Y\left(M_{2}\right)>0$ implies that $M_{2}$ admits a scalar flat metric. We have therefore finished the proof of Theorem 1. \(\square\)

Acknowledgements: The first author would like to thank the hospitality of the directors and staff of the Max-Planck Institut, where he stayed during the preparation of this work. He is also very grateful to Claude LeBrun for very helpful observations on previous versions of this paper and to Vyach-eslav Krushkal for many explanations about surgery techniques. The second author would like to express his gratitude to M. T. Anderson for advice.

\section*{References}
\begin{itemize}
\item[] [1] M. Anderson, Scalar Curvature and Geometrization Conjectures for 3-manifolds, Comparison Geometry, MSRI Publ. 30 (1996), 47-80.
\item[] [2] M. Anderson, Extrema of curvature functionals on the space of metrics on 3-manifolds, Calc. Var. 5 (1997), 199-269.
\end{itemize}
\begin{itemize}
\item[] [3] T. Aubin, Equations differentielles non lineaires et probleme de Yamabe concernant la courbure scalaire, J. Math. Pures Appl. 55 (1976), 269-296.
\item[] [4] M. Gromov, H. B. Lawson, The classification of simply connected manifolds of positive scalar curvature, Ann. Math. 111 (1980) 423-434.
\item[] [5] O. Kobayashi, Scalar Curvature of a metric with Unit Volume, Math. Ann. 279 (1987), 253-265.
\item[] [6] C. LeBrun, Kodaira Dimension and the Yamabe Problem, to appear in Comm. An. Geom.
\item[] [7] R. Schoen, S.T. Yau, On the structure of manifolds with positive scalar curvature, Manuscr. Math. 28 (1979), 159-183.
\item[] [8] R. Schoen, Conformal deformation of a Riemannian metric to constant scalar curvature, Journal Diff. Geom. 20 (1984), 479-495.
\item[] [9] N.S. Trudinger, Remarks concerning the conformal deformation of Riemannian structures on compact manifolds, Ann. Scuola Norm. Sup. Pisa 22 (1968), 265-274.
\item[] [10] H. Yamabe, On a deformation of Riemannian structures on compact manifolds, Osaka Math. J. 12 (1960), 21-37.
\end{itemize}

\section*{Authors' addresses:}

Jimmy Petean
Max-Planck-Institut für Mathematik
Bonn, Germany.
email: petean@mpim-bonn.mpg.de
Gabjin Yun
Department of Mathematics
Myong Ji University
Yong In, Kyung Ki, Korea 449-728
email: gabjin@wh.myongji.ac.kr
---
retention_scope: session
part: 2
total_parts: 2
---

[Part 2/2 of: Kähler-Einstein metrics with mixed Poincaré and cone singularities along a normal crossing divisor]

Now we may look at the terms $R_{p \bar{q} r \bar{s}}$ where $p, q \in K$ but $r, s \notin K$. If $r, s \notin J$, then $A(p, q, r, s) R_{p \bar{q} r \bar{s}}(z)=A(p, q) R_{p \bar{q} r \bar{s}}(z)$ is uniformly bounded in $z \in V \cap X_{l c}$ as we can see by looking at the expression of the metric (4.4). So now we may suppose that $r$ or $s$ belongs to $J$. The only term in the metric which may cause trouble is $\sum_{j \in J} \frac{\left|z_{j}\right|^{2} \beta_{j p q}}{\left(\left|z_{j}\right|^{2} e^{-\varphi_{j}}+\varepsilon^{2}\right)^{a_{j}}}+$ $\left(\left(\left|z_{j}\right|^{2} e^{-\varphi_{j}}+\varepsilon^{2}\right)^{1-a_{j}}-\varepsilon^{2\left(1-a_{j}\right)}\right) \frac{\partial^{2} \varphi_{j}}{\partial z_{p} \partial \bar{z}_{q}}$. But Lemma 4.2 enables us to use the computations of [11, Section 4.3] word for word, so as to show that $A(p, q, r, s) R_{p \bar{q} r \bar{s}}(z)$ is uniformly bounded in $z \in V \cap X_{l c}$.

The next step in bounding the curvature of $\omega_{\varepsilon}$ from below consists now in looking at the terms $R_{p \bar{q} r \bar{s}}$ for $p, q \in J$. Then the terms in $g_{p \bar{q}}$ coming from the Poincaré part are of the form $\sum_{k} \frac{\nu_{k}}{\log \left|z_{k}\right|^{2}}$ as (4.4) shows. These terms are uniformly bounded in $V \cap X_{l c}$, as well as their derivatives with respect to the variables $z_{r}, \bar{z}_{s}$ as long as $r, s \notin K$; in that that case [11, Sections 4.3-4.4] gives us the expected lower bound for $A(p, q, r, s) R_{p \bar{q} r \bar{s}}$. If now $r \in K$, then we saw earlier that $A(r) \frac{\partial}{\partial z_{r}}\left(\frac{\nu_{r}}{\log \left|z_{r}\right|^{2}}\right)$, $A(s) \frac{\partial}{\partial \bar{z}_{s}}\left(\frac{\nu_{s}}{\log \left|z_{k}\right|^{2}}\right), A(r)^{2} \frac{\partial^{2}}{\partial z_{r} \partial \bar{z}_{r}}\left(\frac{\nu_{r}}{\log \left|z_{r}\right|^{2}}\right)$ are bounded functions in $V \cap X_{l c}$, so that, using Lemma 4.2, the boundedness of $A(p, q, r, s) R_{p \bar{q} r \bar{s}}$ is equivalent to the one of $A(p, q, r, s) R_{p \bar{q} r \bar{s}}^{g^{(C)}}$ whenever $p, q \in J$. And by [11, Section 4.3],
we know the existence of this bound (which is an upper and lower bound, as $\#\{p, q, r, s\} \geqslant 2$ ).

Finally, for the last step, we need to look at mixed terms $R_{p \bar{q} r \bar{s}}$ for $p \in K$ and $q \in J$ (or one of those not belonging to $J \cup K$ ). As $p \neq q$, the operators $A(r) \frac{\partial}{\partial z_{r}}, A(s) \frac{\partial}{\partial \bar{z}_{s}}$ and $A(r, s) \frac{\partial^{2}}{\partial z_{r} \partial \bar{z}_{r}}$ map $g_{p \bar{q}}$ to a bounded function, as can be checked separately for $g^{(P)}$ (cf. the previous computations) and $g^{(C)}$ (cf. [11, Section 4.3]).

So we are done: $\omega_{\varepsilon}$ has holomorphic bisectional curvature uniformly bounded from below on $X_{l c}$.

\subsection*{4.2.3. Bounding the $\omega_{\varepsilon}$-Laplacian of $F_{\varepsilon}$}

Remember that
$$F_{\varepsilon}=f+\psi_{\varepsilon}+\log \left(\frac{\omega^{n}}{\prod_{j \in J}\left(\left|s_{j}\right|^{2}+\varepsilon^{2}\right)^{a_{j}} \omega_{\varepsilon}^{n}}\right) .$$
At the point $x$ (which is point $p$ of Lemma 4.1) , the $(p, \bar{q})$ component of $\omega_{\varepsilon}(x)$ is
$$\begin{aligned}
g_{p \bar{q}}(x)= & u_{p \bar{q}}(x)+\frac{\delta_{p q, J}}{\left(\left|z_{p}\right|^{2}+\varepsilon^{2}\right)^{a_{p}}} \\
& +\sum_{j \in J}\left(\left(\left|z_{j}\right|^{2}+\varepsilon^{2}\right)^{1-a_{j}}-\varepsilon^{2\left(1-a_{j}\right)}\right) \frac{\partial^{2} \varphi_{j}}{\partial z_{p} \partial \bar{z}_{q}}(x) \\
& +\delta_{p q, K} \frac{i d z_{p} \wedge d \bar{z}_{p}}{\left|z_{p}\right|^{2} \log ^{2}\left|z_{p}\right|^{2}}+\sum_{k=r+1}^{d} \frac{\nu_{k}}{\log \left|z_{k}\right|^{2}}
\end{aligned}$$
whereas the $(p, \bar{q})$ component of $\omega(x)$ is
$$g_{p \bar{q}}^{(P)}(x)=u_{p \bar{q}}(x)+\delta_{p q, K} \frac{i d z_{p} \wedge d \bar{z}_{p}}{\left|z_{p}\right|^{2} \log ^{2}\left|z_{p}\right|^{2}}+\sum_{k=r+1}^{d} \frac{\nu_{k}}{\log \left|z_{k}\right|^{2}} .$$
Expanding the determinant of those metrics makes it clear that there exists $C>0$ such that
$$C^{-1} \leqslant \frac{\omega^{n}}{\prod_{j \in J}\left(\left|s_{j}\right|^{2}+\varepsilon^{2}\right)^{a_{j}} \omega_{\varepsilon}^{n}} \leqslant C$$
so that $F_{\varepsilon}$ is bounded on $X_{l c}$.
Let us now get to bounding $\Delta_{\omega_{\varepsilon}} F_{\varepsilon}$. Actually we will show that $\pm d d^{c} F_{\varepsilon} \leqslant$ $C \omega_{\varepsilon}$ for some uniform $C>0$, which is stronger than just bounding the $\omega_{\varepsilon}$-Laplacian of $F_{\varepsilon}$, but we need this strengthened bound if we want to produce Kähler-Einstein metrics by solving our Monge-Ampère equation.

There are three terms in $F_{\varepsilon}$, namely $f, \psi_{\varepsilon}$ and $\log f_{\varepsilon}$ where
$$f_{\varepsilon}=\frac{\omega^{n}}{\prod_{j \in J}\left(\left|s_{j}\right|^{2}+\varepsilon^{2}\right)^{a_{j}} \omega_{\varepsilon}^{n}} .$$
The first two terms are easy to deal with: indeed, there exists $C>0$ (independent of $\varepsilon$ ) such that $\omega_{\varepsilon} \geqslant C^{-1} \omega$ on $X_{l c}$. Therefore, if one chooses $M$ such that $M \omega \pm d d^{c} f>0$ (the assumptions on $f$ give the existence of such an $M$ ), then $d d^{c} f \leqslant C M \omega_{\varepsilon}$. Moreover, $\omega_{\varepsilon}=\omega+d d^{c} \psi_{\varepsilon}>0$ so that $\pm d d^{c} \psi_{\varepsilon} \leqslant \max (C, 1) \omega_{\varepsilon}$. Therefore it only remains to bound $d d^{c} \log f_{\varepsilon}$.

We will use the following basic identities, holding for any smooth functions $f>0$ and $u, v$ on some open subset of $U \subset X$ :
$$\begin{aligned}
d d^{c} \log f & =\frac{1}{f} d d^{c} f+\frac{1}{f^{2}} d f \wedge d^{c} f \\
d d^{c}\left(\frac{1}{f}\right) & =-\frac{1}{f^{2}} d d^{c} f+\frac{2}{f^{3}} d f \wedge d^{c} f \\
d d^{c}(u v) & =u d d^{c} v+v d d^{c} u+d u \wedge d^{c} v-d^{c} u \wedge d v \\
\nabla(u v) & =(\nabla u) v+u(\nabla v)
\end{aligned}$$

We just saw that $f_{\varepsilon}$ is bounded below by some fixed constant $C^{-1}>0$ on $X_{l c}$, so that by (4.13), $\pm d d^{c} \log f_{\varepsilon}$ will be dominated by some fixed multiple of $\omega_{\varepsilon}$ if we show that both $\pm d d^{c} f_{\varepsilon} \leqslant C \omega_{\varepsilon}$ and $\left|\nabla_{\varepsilon} f_{\varepsilon}\right|_{\omega} \leqslant C$ for some uniform $C>0$ (the last term denotes the norm computed with respect to $\omega$ of the $\omega_{\varepsilon}$-gradient of $f_{\varepsilon}$, defined as usual by $d f_{\varepsilon}(X)=\omega_{\varepsilon}\left(\nabla_{\varepsilon} f_{\varepsilon}, X\right)$ for every vector field $X$ ). For convenience, we will split the computation by writing
$$\begin{aligned}
f_{\varepsilon}=\left(\prod_{j \in J}\left(\left|s_{j}\right|^{2}+\varepsilon^{2}\right)^{a_{j}} \cdot \prod_{k \in K}\left|s_{k}\right|^{2}\right. & \left.\log ^{2}\left|s_{k}\right|^{2} \cdot \omega_{\varepsilon}^{n}\right)^{-1} \\
& \cdot\left(\prod_{k \in K}\left|s_{k}\right|^{2} \log ^{2}\left|s_{k}\right|^{2} \cdot \omega^{n}\right)
\end{aligned}$$
By (4.14)-(4.15), we only need to check that the gradient $\nabla_{\varepsilon}$ of the terms inside the parenthesis is bounded, and that their $\pm d d^{c}$ is dominated by some fixed multiple of $\omega_{\varepsilon}$. Let us begin with the second one, which is simpler:

Lemma 4.3. - Let $\omega$ be a Kähler form of Carlson-Griffiths type on $X_{l c}$, and let $\omega_{0}$ be some smooth Kähler form on $X$. We set
$$V=\left(\prod_{k \in K}\left|s_{k}\right|^{2} \log ^{2}\left|s_{k}\right|^{2}\right) \cdot \frac{\omega^{n}}{\omega_{0}^{n}}$$
Then there exists $C>0$ such that $\pm V$ is $C \omega-p s h$ on $X_{l c}$.

Proof. - We write, with our usual coordinates (cf. Lemma 4.1):
$$\begin{aligned}
\omega^{n}= & \prod_{k \in K} \frac{1}{\left|z_{k}\right|^{2} \log ^{2}\left|z_{k}\right|^{2}}\left(1+\sum_{K_{i} \subset K} A_{i} \prod_{k_{i} \in K_{i}} \frac{1}{\log \left|z_{k_{i}}\right|^{2}}\right) \\
& +\sum_{K_{j}, K_{l}, K_{m}, K_{p} \subset K} A_{j l m p} \prod_{k_{j} \in K_{j}} \frac{1}{\left|z_{k_{j}}\right|^{2} \log ^{2}\left|z_{k_{j}}\right|^{2}} \cdot \prod_{k_{l} \in K_{l}} \frac{1}{z_{k_{l}} \log ^{2}\left|z_{k_{l}}\right|^{2}} \\
& \cdot \prod_{k_{m} \in K_{m}} \frac{1}{\bar{z}_{k_{m}} \log ^{2}\left|z_{k_{m}}\right|^{2}} \cdot \prod_{k_{p} \in K_{p}} \frac{1}{\log \left|z_{k_{p}}\right|^{2}} \cdot \Omega
\end{aligned}$$
for $\Omega$ some smooth volume form on $X$ and where the second sum is taken over the subsets $K_{j}, K_{l}, K_{m}, K_{p}$ of $K$ that are disjoint, and where $A_{i}, A_{j l m p}$ are smooth functions on the whole $X$. Let us apply the operators $A(i, j) \frac{\partial}{\partial z_{i} \partial \bar{z}_{j}}$ and $g^{i \bar{j}} \frac{\partial}{\partial z_{i}} \cdot \frac{\partial}{\partial \bar{z}_{j}}$ to $\frac{1}{\log \left|z_{k}\right|^{2}}, z_{k}, \bar{z}_{k},\left|z_{k}\right|^{2} \log \left|z_{k}\right|^{2}$ and $\left|z_{k}\right|^{2} \log ^{2}\left|z_{k}\right|^{2}$, and check that we obtain bounded functions. We already did it for the first term, so we only have to compute:
$$\begin{aligned}
\frac{\partial}{\partial z_{k}}\left(\left|z_{k}\right|^{2} \log \left|z_{k}\right|^{2}\right) & =\bar{z}_{k} \log \left|z_{k}\right|^{2}+\bar{z}_{k}=\mathcal{O}(1) \frac{\partial^{2}}{\partial z_{k} \partial \bar{z}_{k}}\left(\left|z_{k}\right|^{2} \log \left|z_{k}\right|^{2}\right) \\
& =\log \left|z_{k}\right|^{2}+2 \\
& =c\left(\frac{1}{\left|z_{k}\right|^{2} \log ^{2}\left|z_{k}\right|^{2}}\right) \frac{\partial}{\partial z_{k}}\left(\left|z_{k}\right|^{2} \log ^{2}\left|z_{k}\right|^{2}\right) \\
& =\bar{z}_{k} \log ^{2}\left|z_{k}\right|^{2}+2 \bar{z}_{k} \log \left|z_{k}\right|^{2} \\
& =\mathcal{O}(1) \frac{\partial^{2}}{\partial z_{k} \partial \bar{z}_{k}}\left(\left|z_{k}\right|^{2} \log ^{2}\left|z_{k}\right|^{2}\right) \\
& =\log ^{2}\left|z_{k}\right|^{2}+4 \log \left|z_{k}\right|^{2}+2=\mathcal{O}\left(\frac{1}{\left|z_{k}\right|^{2} \log ^{2}\left|z_{k}\right|^{2}}\right)
\end{aligned}$$
This shows that the $\omega_{\varepsilon}$-gradient of these factors (denote them generically $\kappa)$ is bounded. As for $d d^{c} \kappa$, the previous computations show that in coordinates, its $(i, j)$-th term is uniformly bounded by $C A(i, j)$ for every $i, j$ (this is actually stronger than saying that it becomes bounded when multiplied with $g^{i \bar{j}}$, condition which would however be sufficient to show that the $\omega_{\varepsilon}$-Laplacian is bounded). Therefore, as the matrix of $\omega_{\varepsilon}$ can be written $\operatorname{diag}\left(A(1)^{2}, \ldots, A(n)^{2}\right)+\mathcal{O}(1)$ in coordinates, and using the Cauchy-Schwarz inequality, one easily obtains $C>0$ such that $\pm d d^{c} \kappa \leqslant C \omega_{\varepsilon}$.

In fact, once we we saw that the only singular terms were $\frac{1}{\log \left|z_{k}\right|^{2}}$, $\left|z_{k}\right|^{2} \log \left|z_{k}\right|^{2}$ and $\left|z_{k}\right|^{2} \log ^{2}\left|z_{k}\right|^{2}$, we could have used the usual quasicoordinates as in 1.6 to conclude. \(\square\)

Let us now get to the term inside the first parenthesis of (4.17). For this, notice that in the expansion of $\omega_{\varepsilon}^{n}$, we find the terms of (4.18) multiplied by terms of the form
$$C(z)+\sum_{I \subseteq J} A_{I}(z) \prod_{i \in I}\left(\left|z_{i}\right|^{2} e^{-\varphi_{i}}+\varepsilon^{2}\right)^{a_{i}}$$
where $C(z)$ and $A_{I}(z)$ are sums of terms of the form
$$\begin{array}{r}
B(z) \prod_{j_{l} \in J_{l}}\left[\left(\left|z_{j_{l}}\right|^{2} e^{-\varphi_{j_{l}}}+\varepsilon^{2}\right)^{1-a_{j_{l}}}-\varepsilon^{2\left(1-a_{j_{l}}\right)}\right] \cdot \prod_{j \in J_{k}} \frac{z_{j_{k}} \alpha_{j_{k}}}{\left(\left|z_{j_{k}}\right|^{2} e^{-\varphi_{j_{k}}}+\varepsilon^{2}\right)^{\lambda_{j_{k}} a_{j_{k}}}} \\
\cdot \prod_{j \in J_{m}} \frac{\bar{z}_{j_{m}} \bar{\alpha}_{j_{m}}}{\left(\left|z_{j_{m}}\right|^{2} e^{-\varphi_{j_{m}}}+\varepsilon^{2}\right)^{\lambda_{j_{m}} a_{j_{m}}}} \prod_{j_{p} \in J_{p}} \frac{\left|z_{j_{p}}\right|^{2} \beta_{j_{p}}}{\left(\left|z_{j_{p}}\right|^{2} e^{-\varphi_{j_{p}}}+\varepsilon^{2}\right)^{a_{j_{p}}}}
\end{array}$$
where $I, J_{l}, J_{k}, J_{m}, J_{p}$ are disjoint subsets of $J$, and where $B(z)$ is smooth independent of $\varepsilon, \alpha_{j}$ is smooth and vanishes at $x, \beta_{j}$ is smooth and vanishes at order at least 2 at $p$, and $\lambda_{j} \in\{0,1 / 2\}$. And now, using Lemma 4.2 and [11, Section 4.5] (we must slightly change the argument therein as said above to control the $d d^{c}$ with respect to $\omega_{\varepsilon}$ and not only $\Delta_{\omega_{\varepsilon}}$ ), we can conclude that the appropriate $d d^{c}$ (resp. gradients) of those quantities are dominated by $C \omega_{\varepsilon}$ (resp. bounded). Combining this with the previous computations, we deduce that $\Delta_{\omega_{\varepsilon}} F_{\varepsilon}$ is bounded on the whole $X_{l c}$.

\subsection*{4.3. End of the proof}

Remember that we wish to extract from the sequence of smooth metrics $\omega_{\varepsilon}+d d^{c} \varphi_{\varepsilon}$ on $X_{l c}$ some subsequence converging to a smooth metric on $X \backslash \operatorname{Supp}(\Delta)$. In order to do this, we need to have a priori $\mathscr{C}^{k}$ estimates for all $k$. The usual bootstrapping argument for the Monge-Ampère equation allows us to deduce those estimates from the $\mathscr{C}^{2, \alpha}$ ones for some $\left.\alpha \in\right] 0,1[$. The crucial fact here is that we have at our disposal the following local result, taken from [17] (see also [27], [6, Theorem 5.1]), which gives interior estimates. It is a consequence of Evans-Krylov's theory:

Theorem. - Let $u$ be a smooth psh function in an open set $\Omega \subset \mathbb{C}^{n}$ such that $f:=\operatorname{det}\left(u_{i \bar{j}}\right)>0$. Then for any $\Omega^{\prime} \Subset \Omega$, there exists $\left.\alpha \in\right] 0,1[$ depending only on $n$ and on upper bounds for $\|u\|_{\mathscr{C}^{0}(\Omega)}, \sup _{\Omega} \Delta \varphi,\|f\|_{\mathscr{C}^{0,1}(\Omega)}$, $1 / \inf _{\Omega} f$, and $C>0$ depending in addition on a lower bound for $d\left(\Omega^{\prime}, \partial \Omega\right)$ such that:
$$\|u\|_{\mathscr{C}^{2, \alpha}\left(\Omega^{\prime}\right)} \leqslant C .$$

In our case, we choose some point $p$ outside the support of the divisor $\Delta$, and consider two coordinate open sets $\Omega^{\prime} \subset \Omega$ containing $p$, but not intersecting $\operatorname{Supp}(\Delta)$. In that case, we may find a smooth Kähler metric $\omega_{p}$ on $\Omega$ such that on $\Omega^{\prime}$, the covariant derivatives at any order of $\omega_{\varepsilon}$ are uniformly bounded (in $\varepsilon$ ) with respect to $\omega_{p}$. Then one may take $u=\varphi_{\varepsilon}$ in the previous theorem, and one can easily check that there are common upper bounds (i.e. independent of $\varepsilon$ ) for all the quantities involved in the statement. This finishes to show the existence of uniform a priori $\mathscr{C}^{2, \alpha}\left(\Omega^{\prime}\right)$ estimates for $\varphi_{\varepsilon}$.

As we mentioned earlier, the ellipticity of the Monge-Ampère operator automatically gives us local a priori $\mathscr{C}^{k}$ estimates for $\varphi_{\varepsilon}$, which ends to provide a smooth function $\varphi$ on $X \backslash \operatorname{Supp}(\Delta)$ (extracted from the sequence $\left.\left(\varphi_{\varepsilon}\right)_{\varepsilon}\right)$ such that $\omega_{\infty}=\omega+d d^{c} \varphi$ defines a smooth metric outside $\operatorname{Supp}(\Delta)$ satisfying
$$\left(\omega+d d^{c} \varphi\right)^{n}=\frac{e^{\varphi+f}}{\prod_{j \in J}\left|s_{j}\right|^{2 a_{j}}} \omega^{n}$$
Moreover, the strategy explained at the beginning of the previous Section 4.2 and set up all along the section shows that this metric $\varphi$ has mixed Poincaré and cone singularities along $\Delta$, so this finishes the proof of the main theorem.

\subsection*{4.4 Remarks}

It could also be interesting to study the following equation:
$$\left(\omega+d d^{c} \varphi\right)^{n}=\frac{e^{f}}{\prod_{j \in J}\left|s_{j}\right|^{2 a_{j}}} \omega^{n}$$
where $\omega$ is of Carlson-Griffith's type, and ask whether its eventual solutions have mixed Poincaré and cone singularities. This equation has been recently studied and solved by H. Auvray in [1, Theorem 4] in the case where $\Delta_{k l t}=$ 0 (the "logarithmic case"), and for $f$ vanishing at some order along $\Delta$. To adapt his results, one would need to show that one can make a choice of $\psi_{\varepsilon}$ so that $F_{\varepsilon}$ vanishes along $\Delta_{l c}$ at some fixed order, which we have been unable to do so far.

\section*{5. A vanishing theorem for holomorphic tensor fields}

Given a pair $(X, \Delta)$, where $X$ is a compact Kähler manifold and $\Delta=$ $\sum a_{i} \Delta_{i}$ a $\mathbb{R}$-divisor with simple normal crossing support such that $0 \leqslant a_{i} \leqslant$

1, there are many natural ways to construct holomorphic tensors attached to $(X, \Delta)$.

To begin with, one defines the tensor fields on a manifold $M$, which are contravariant of degree $r$ and covariant of degree $s$ as follows
$$T_{s}^{r} M:=\left(\otimes^{r} T_{M}\right) \otimes\left(\otimes^{s} T_{M}^{\star}\right) .$$
In our present context, we consider $M:=X_{0}$, that is to say the Zariski open set $X \backslash \operatorname{Supp}(\Delta)$. Let us recall the definition of the orbifold tensors introduced by F. Campana [9]. To avoid a possible confusion with the standard orbifold situation (i.e. when $a_{i}=1-\frac{1}{m}$ for some integer $m$ ), we will not use his terminology and refer to these tensors as $\Delta$-holomorphic tensors.

Let $x \in X$ be a point; since the hypersurfaces ( $\Delta_{i}$ ) have strictly normal intersections, there exist a small open set $\Omega \subset X$, together with a coordinate system $z=\left(z_{1}, \ldots, z_{n}\right)$ centered at $x$ such that $\Delta_{i} \cap \Omega=\left(z_{i}=0\right)$ for $i=1, \ldots, d$ and $\Delta_{i} \cap \Omega=\emptyset$ for the others indexes. We define the locally free sheaf $T_{s}^{r}(X \mid \Delta)$ generated as an $\mathcal{O}_{X}$-module by the tensors
$$z^{\left\lceil\left(h_{I}-h_{J}\right) \cdot a\right\rceil} \frac{\partial}{\partial z_{I}} \otimes d z^{J}$$
where the notations are as follows:
\begin{itemize}
\item[(1)] $I$ (resp. $J$ ) is a collection of positive integers in $\{1, \ldots, n\}$ of cardinal $r$ (resp. $s$ ) (we notice that we may have repetitions among the elements of $I$ and $J$, and we count each element according to its multiplicity).
\item[(2)] For each $1 \leqslant i \leqslant n$, we denote by $h_{I}(i)$ the multiplicity of $i$ as element of the collection $I$.
\item[(3)] For each $i=1, \ldots, d$ we have $a_{i}:=1-\tau_{i}$, and $a_{i}=0$ for $i \geqslant d+1$.
\item[(4)] We have
$$z^{\left\lceil\left(h_{I}-h_{J}\right) \cdot a\right\rceil}:=\prod_{i}\left(z^{i}\right)^{\left\lceil\left(h_{I}(i)-h_{J}(i)\right) \cdot a_{i}\right\rceil}$$
\item[(5)] If $I=\left(i_{1}, \ldots, i_{r}\right)$, then we have
$$\frac{\partial}{\partial z_{I}}:=\frac{\partial}{\partial z_{i_{1}}} \otimes \cdots \otimes \frac{\partial}{\partial z_{i_{r}}}$$
and we use similar notations for $d z^{J}$.
\end{itemize}

Hence the holomorphic tensors we are considering here have prescribed zeros/poles near $X \backslash X_{0}$, according to the multiplicities of $\Delta$. In the cone case $\left(\Delta_{l c}=0\right)$, those tensors have a nice interpretation ([11, Lemma 8.2]):

Lemma 5.1. - Assume $\Delta_{l c}=0$, and let $u$ be a smooth section of the bundle $T_{s}^{r}\left(X_{0}\right)$. Then $u$ corresponds to a holomorphic section of $T_{s}^{r}(X \mid D)$ if and only if $\bar{\partial} u=0$ and $u$ is bounded with respect to some metric with cone singularities along $\Delta$.

In [11], the vanishing and parallelism theorems are proved using the classical Bochner formula with an appropriate cut-off function for the space of bounded (for the cone metric) holomorphic sections of $T_{s}^{r}\left(X_{0}\right)$, and the lemma above enables to transfer this property to $\Delta$-holomorphic tensors.

Unfortunately, there is no such simple correspondence in the general logcanonical case. For example, if $\Delta$ has only one component (with coefficient 1) of local equation $z=0$, then $\frac{d z}{z}$ is a local section of $T_{1}^{0}(X \mid \Delta)$ but it is not bounded with respect to any metric having Poincaré singularities along $\Delta$.

The idea is to force $\Delta$-holomorphic tensors to be bounded by twisting them with the trivial line bundle $L=\mathcal{O}_{X}$ equipped with the singular hermitian metric
$$h_{L}=e^{-2 s \sum_{k} \log \log \frac{1}{\left|s_{k}\right|^{2}}}=\prod_{k \in K} \frac{1}{\log ^{2 s}\left|s_{k}\right|^{2}}$$
where the $\left(s_{k}\right)_{k \in K}$ are the sections of the divisors $\Delta_{k}$ appearing in $\Delta_{l c}=$ $\lceil\Delta\rceil$. In more elementary terms, we just change the reference metric measuring those tensors. Then, using a twisted Bochner formula, we will be able to carry on the computations done in [11] to obtain the vanishing. It will be practical for the following to introduce the following notation:

Definition 5.2. - Let $(X, \Delta)$ be a pair such that $\Delta$ has simple normal crossing support and coefficients in [0, 1]. The space of bounded holomorphic tensors of type ( $r, s$ ) for ( $X, \Delta$ ) is defined by
$$\mathscr{H}_{B}^{r, s}(X \mid \Delta)=\left\{u \in \mathscr{C}^{\infty}\left(X_{0}, T_{s}^{r}\left(X_{0}\right)\right) ; \exists C ;|u|_{h}^{2} \leqslant C \text { and } \bar{\partial} u=0\right\}$$
where $h=g_{r, s} \otimes h_{L}$ is a metric on $T_{s}^{r}\left(X_{0}\right)$ induced by $h_{L}$ and a metric $g$ on $X_{0}$ having mixed Poincaré and cone singularities along $\Delta$.

Of course, this definition does not depend on the choice of the metric $g$ having Poincaré and cone singularities along $\Delta$; it coincides with the one introduced in [11] for klt pairs. The main point about this definition, which legitimates it, consists in the following proposition giving the expected identification between bounded and $\Delta$-holomorphic tensors:

Proposition 5.3. - With the previous notations, we have a natural identification:
$$\mathscr{H}_{B}^{r, s}(X \mid \Delta)=H^{0}\left(X, T_{s}^{r}(X \mid \Delta)\right) .$$

Proof. - We only need to check it locally on $\Omega=\left(\mathbb{D}^{*}\right)^{p} \times\left(\mathbb{D}^{*}\right)^{q} \times$ $\mathbb{D}^{n-(k+l)}$, where the boundary divisor restricted to $\Omega$ is given by
$$\sum_{k=1}^{p} d_{k}\left[z_{i}=0\right]+\sum_{k=p+1}^{p+q}\left[z_{k}=0\right],$$
and we choose $g$ to be the model metric $\omega_{\Delta}$ given in the introduction.
Let us begin with the inclusion $\mathscr{H}_{B}^{r, s}(X \mid \Delta) \subset H^{0}\left(X, T_{s}^{r}(X \mid \Delta)\right)$. By orthogonality of the different $\frac{\partial}{\partial z_{I}} \otimes d z^{J}$, we only have to consider $u=$ $v \frac{\partial}{\partial z_{I}} \otimes d z^{J}$ for some (holomorphic) function $v$ satisfying:
$$\frac{|v|}{\prod_{k=1}^{p}\left|z_{k}\right|^{\left(h_{I}(k)-h_{J}(k)\right) a_{k}} \prod_{k=p+1}^{p+q}\left|z_{k}\right|^{h_{I}(k)-h_{J}(k)}\left(\log \frac{1}{\left|z_{k}\right|^{2}}\right)^{s+h_{I}(k)-h_{J}(k)}} \leqslant C .$$
Consider now the function
$$w:=\frac{v}{\prod_{k=1}^{p} z_{k}^{\left\lceil\left(h_{I}(k)-h_{J}(k)\right) a_{k}\right\rceil} \prod_{k=p+1}^{p+q} z_{k}^{h_{I}(k)-h_{J}(k)}}$$
whose modulus $|w|$ can also be rewritten in the form
$$\begin{array}{r}
\frac{|v|}{\prod_{k=1}^{p}\left|z_{k}\right|^{\left(h_{I}(k)-h_{J}(k)\right) a_{k}} \prod_{k=p+1}^{p+q}\left|z_{k}\right|^{h_{I}(k)-h_{J}(k)}\left(\log \frac{1}{\left|z_{k}\right|^{2}}\right)^{s+h_{I}(k)-h_{J}(k)}} \\
\cdot \frac{\prod_{k=p+1}^{p+q}\left(\log \frac{1}{\left|z_{k}\right|^{2}}\right)^{s+h_{I}(k)-h_{J}(k)}}{\prod_{k=1}^{p}\left|z_{k}\right|^{\left\lceil\left(h_{I}(k)-h_{J}(k)\right) a_{k}\right\rceil-\left(h_{I}(k)-h_{J}(k)\right) a_{k}}} .
\end{array}$$
The first factor is bounded; moreover, using the fact that $0 \leqslant\lceil x\rceil-x<1$ for every real number $x$ and that $\left(\log \frac{1}{|z|}\right)^{\alpha}$ is integrable at 0 for every real number $\alpha$, we conclude that the second factor is also $L^{2}$. This finishes to prove that $w$ is $L^{2}$, so in particular it extends across the support of our divisor, and therefore, $u \in H^{0}\left(\Omega, T_{s}^{r}\left(\Omega \mid \Delta_{\mid \Omega}\right)\right)$.

For the reverse inclusion, every "irreducible" $\Delta$-holomorphic tensor $u \in$ $H^{0}\left(\Omega, T_{s}^{r}\left(\Omega \mid \Delta_{\mid \Omega}\right)\right)$ can be written
$$u=\prod_{k=1}^{p} z_{k}^{\left\lceil\left(h_{I}(k)-h_{J}(k)\right) a_{k}\right\rceil} \prod_{k=p+1}^{p+q} z^{h_{I}(k)-h_{J}(k)} v \frac{\partial}{\partial z_{I}} \otimes d z^{J}$$
for some holomorphic function $v$, and some $I \in\{1, \ldots, n\}^{r}, J \in\{1, \ldots, n\}^{s}$. So for $g$ the metric on $X_{0}$ attached to $\omega_{\Delta}$, and setting $h=g_{r, s} \otimes h_{L}$ as in

Definition 5.2, we have:
$$|u|_{h}=\frac{|v| \prod_{k=1}^{p}\left|z_{k}\right|^{\left\lceil\left(h_{I}(k)-h_{J}(k)\right) a_{k}\right\rceil-\left(h_{I}(k)-h_{J}(k)\right) a_{k}}}{\prod_{k=p+1}^{p+q}\left(\log \frac{1}{\left|z_{k}\right|^{2}}\right)^{s+h_{I}(k)-h_{J}(k)}}$$
which is clearly bounded near the divisor since $s+h_{I}(k)-h_{J}(k) \geqslant 0$ for all $k$. \(\square\)

Now we can state the main result of this section, which is a partial generalization of [11, Theorem C]:

Theorem 5.4. - Let $(X, \Delta)$ be a pair such that $\Delta=\sum a_{i} \Delta_{i}$ has simple normal crossing support, with coefficients satisfying: $\frac{1}{2} \leqslant a_{i} \leqslant 1$ for all $i$.

If $K_{X}+\Delta$ is ample, then there is no non-zero $\Delta$-holomorphic tensor of type ( $r, s$ ) whenever $r \geqslant s+1$ :
$$H^{0}\left(X, T_{s}^{r}(X \mid \Delta)\right)=0 .$$

Proof of Theorem 5.4. - Proposition 5.3 allows us to reduce the vanishing of the $\Delta$-holomorphic tensors to the one of bounded tensors as defined in 5.2. The proof of this result is similar to the one of [11, Theorem C], the two main new features being the existence of a Kähler-Einstein metric with mixed Poincaré and cone singularities along $\Delta$ (cf. Theorem A), and the use of a twisted Bochner formula. For this reason, we will give a relatively sketchy proof, and we will refer to [11] for the details we skip.

To fix the notations, we write $\Delta=\sum_{j \in J} a_{j} \Delta_{j}+\sum_{k \in k} \Delta_{k}$ where for all $j \in J$, we have $a_{j}<1$. In the following, any index $j$ (resp. $k$ ) will be implicitly assumed to belong to $J$ (resp. $K$ ), whereas the index $i$ will vary in $J \cup K$.

As $K_{X}+\Delta$ is ample, Theorem A guarantees the existence of a Kähler metric $\omega_{\infty}$ on $X_{0}$ such that - Ric $\omega_{\infty}=\omega_{\infty}$, and having mixed Poincaré and cone singularities along $\Delta$. We choose now an element $u \in \mathscr{H}_{B}^{r, s}(X \mid \Delta)$ with $r \geqslant s+1$, and we want to use a Bochner formula to show that $u=0$.

To do this, we need to perform a cut-off procedure, and control the error term so that one can pass to the limit in the cut-off process. Let us now get a bit more into the details.

Step 1: The cut-off procedure. We define $\rho: X \rightarrow]-\infty,+\infty]$ by the formula
$$\rho(x):=\log \left(\log \frac{1}{\prod_{i}\left|s_{i}(x)\right|^{2}}\right) .$$
For each $\varepsilon>0$, let $\chi_{\varepsilon}:[0,+\infty[\rightarrow[0,1]$ be a smooth function which is equal to zero on the interval $[0,1 / \varepsilon]$, and which is equal to 1 on the interval
$[1+1 / \varepsilon,+\infty]$. One may for example define $\chi_{\varepsilon}(x)=\chi_{1}\left(x-\frac{1}{\varepsilon}\right)$, so that
$$\sup _{\varepsilon>0, t \in \mathbb{R}_{+}}\left|\chi_{\varepsilon}^{\prime}(t)\right| \leqslant C<\infty,$$
and we define $\theta_{\varepsilon}: X \rightarrow[0,1]$ by the expression
$$\theta_{\varepsilon}(x)=1-\chi_{\varepsilon}(\rho(x)) .$$
We assume from the beginning that we have
$$\prod_{i}\left|s_{i}\right|^{2} \leqslant e^{-2}$$
at each point of $X$, and then it is clear that we have
$$\theta_{\varepsilon}=1 \Longleftrightarrow \prod_{i}\left|s_{i}\right|^{2} \geqslant e^{-e^{1 / \varepsilon}}$$
and also
$$\theta_{\varepsilon}=0 \Longleftrightarrow \prod_{i}\left|s_{i}\right|^{2} \leqslant e^{-e^{1+1 / \varepsilon}} .$$
We evaluate next the norm of the $(0,1)$-form $\bar{\partial} \theta_{\varepsilon}$; we have
$$\bar{\partial} \theta_{\varepsilon}(x)=\chi_{\varepsilon}^{\prime}(\rho(x)) \frac{1}{\log \frac{1}{\prod_{i}\left|s_{i}(x)\right|^{2}}} \sum_{i} \frac{\left\langle s_{i}, D^{\prime} s_{i}\right\rangle}{\left|s_{i}\right|^{2}}(x) .$$
As $\omega_{\infty}$ has mixed Poincaré and cone singularities along $\Delta$, we have:
$$\left|\bar{\partial} \theta_{\varepsilon}\right|_{\omega_{\infty}}^{2} \leqslant \frac{C\left|\chi_{\varepsilon}^{\prime}(\rho)\right|^{2}}{\log ^{2} \frac{1}{\prod_{j}\left|s_{j}\right|^{2}}}\left(\sum_{j} \frac{1}{\left|s_{j}\right|^{2\left(1-a_{j}\right)}}+\sum_{k} \log ^{2}\left|s_{k}\right|^{2}\right)$$
at each point of $X_{0}$. Indeed, this is a consequence of the fact that the norm of the (1,1)-forms
$$\frac{i\left\langle D^{\prime} s_{j}, D^{\prime} s_{j}\right\rangle}{\left|s_{j}\right|^{2 a_{j}}} \quad \text { and } \quad \frac{i\left\langle D^{\prime} s_{k}, D^{\prime} s_{k}\right\rangle}{\left|s_{k}\right|^{2} \log ^{2}\left|s_{k}\right|^{2}}$$
with respect to $\omega_{\infty}$ are bounded from above by a constant.
Let $\varepsilon>0$ be a real number; we consider the tensor
$$u_{\varepsilon}:=\theta_{\varepsilon} u .$$
It has compact support, hence by the (twisted) Bochner formula (see e.g. [16, Lemma 14.2]), we infer
$$\int_{X_{0}}\left|\bar{\partial}\left(\# u_{\varepsilon}\right)\right|_{h}^{2} d V_{\omega_{\infty}}=\int_{X_{0}}\left|\bar{\partial} u_{\varepsilon}\right|_{h}^{2} d V_{\omega_{\infty}}+\int_{X_{0}}\left(\left\langle\mathcal{R}\left(u_{\varepsilon}\right), u_{\varepsilon}\right\rangle_{h}+\gamma\left|u_{\varepsilon}\right|_{h}^{2}\right) d V_{\omega_{\infty}}$$
where:
\begin{itemize}
\item[] $\cdot \mathcal{R}$ is a zero-order operator such that in our case $\left(-\operatorname{Ric} \omega_{\infty}=\omega_{\infty}\right)$, we have
$$R_{j \bar{i}}=-\delta_{j i},$$
and therefore the linear term $\left\langle\mathcal{R}\left(u_{\varepsilon}\right), u_{\varepsilon}\right\rangle$ becomes simply $(s-r)\left|u_{\varepsilon}\right|^{2}$;
\item[-] $h=\omega_{\infty, *} \otimes h_{L}$, where $\omega_{\infty, *}$ denotes the canonical extension of $\omega_{\infty}$ to the appropriate tensor fields (which are respectively $T_{r}^{s}\left(X_{0}\right) \otimes$ $\Omega^{0,1}\left(X_{0}\right), T_{s}^{r}\left(X_{0}\right) \otimes \Omega^{0,1}\left(X_{0}\right)$ and $\left.T_{s}^{r}\left(X_{0}\right)\right)$;
\item[-] $\gamma=\operatorname{tr}_{\omega_{\infty}}\left(\Theta_{h}(L)\right)$ is the trace with respect to $\omega_{\infty}$ of the curvature of $(L, h)$.
\end{itemize}

Here we need to be cautious because of the singularities of the metric $h_{L}$ on $\Delta$. Indeed, the Bochner formula applies to smooth hermitian metrics; however one can consider here some metric $h_{L, \varepsilon}$ which would coincide with $h_{L}$ whenever $\theta_{\varepsilon}>0$ and which is a smooth metric near $\Delta$. For example, on can set $h_{L, \varepsilon}=\theta_{\varepsilon / 2} h_{L}+\left(1-\theta_{\varepsilon / 2}\right)$. Then for each $\varepsilon<1$, there exists an open set $U_{\varepsilon} \supset \overline{\left\{\theta_{\varepsilon}>0\right\}}$ on which $h_{L, \varepsilon}=h_{L}$ so that in particular, in the formula (5.3), one can replace $h_{L}$ by $h_{L, \varepsilon}$ without affecting anything.

There remains two steps to achieve now: the first one consists in evaluating the correction term $\gamma$ induced by the curvature of $L$, and the second one is to show that the integration by part is valid in the Poincaré-cone setting; more precisely we have to prove that the error term $\int_{X_{0}}\left|\bar{\partial} u_{\varepsilon}\right|_{h}^{2} d V_{\omega_{\infty}}$ converges to 0 as $\varepsilon$ goes to 0.

Step 2: Dealing with the curvature of $(L, h)$. We work on local charts where $\Delta_{l c}$ is given by $\left\{\prod_{k \in K} z_{k}=0\right\}$.

To begin with, we know that there exists $A>0$ such that $\omega_{\infty} \leqslant A\left(\omega_{\text {klt }}+\right.$ $\left.\sum_{k} \frac{i d z_{k} \wedge d \bar{z}_{k}}{\left|z_{k}\right|^{2} \log ^{2}\left|z_{k}\right|^{2}}\right)$ where $\omega_{\text {klt }}$ is some smooth metric on $X \backslash \operatorname{Supp}\left(\Delta_{k l t}\right)$ having cone singularities along $\Delta_{k l t}$. It will be useful to introduce the notation $\omega_{\text {lc }}:=\omega_{\text {klt }}+\sum_{k} \frac{i d z_{k} \wedge d \bar{z}_{k}}{\left|z_{k}\right|^{2} \log ^{2}\left|z_{k}\right|^{2}}$. Moreover, the usual computations (see e.g. [23, Lemma 1]) show that there exists a smooth (1, 1)-form $\alpha$ on our chart satisfying
$$-\sum_{k \in K} d d^{c} \log \log \frac{1}{\left|s_{k}\right|^{2}} \geqslant \sum_{k \in K} \frac{i d z_{k} \wedge d \bar{z}_{k}}{\left|z_{k}\right|^{2} \log ^{2}\left|z_{k}\right|^{2}}+\frac{1}{B} \alpha$$
where $B$ is a constant which can be taken as large as wanted up to scaling the (smooth) metrics on the $\Delta_{k}$ 's, which does not affect their curvature.

Therefore, the curvature $\Theta_{h_{L}}(L)$ of $L$ satisfies:
$$\begin{aligned}
\operatorname{tr}_{\omega_{\infty}}\left(-\Theta_{h_{L}}(L)\right) & \geqslant A^{-1} \operatorname{tr}_{\omega_{\mathrm{lc}}}\left(-\Theta_{h_{L}}(L)\right) \\
& \geqslant 2 s A^{-1} \operatorname{tr}_{\omega_{\mathrm{lc}}}\left(\sum_{k \in K} \frac{i d z_{k} \wedge d \bar{z}_{k}}{\left|z_{k}\right|^{2} \log ^{2}\left|z_{k}\right|^{2}}+\frac{1}{B} \alpha\right) \\
& \geqslant 2 s|K| A^{-1}+2 s(A B)^{-1} \operatorname{tr}_{\omega_{\mathrm{lc}}} \alpha
\end{aligned}$$
As $\omega_{\mathrm{lc}}$ dominates some smooth form on $X$, the quantity $\operatorname{tr}_{\omega_{\mathrm{lc}}} \alpha$ is bounded on $X_{0}$ so that $2 s(A B)^{-1} \operatorname{tr}_{\omega_{\mathrm{lc}}} \alpha$ can be made as small as we want by scaling the metrics on the divisors as explained above. Therefore one has
$$\gamma=\operatorname{tr}_{\omega_{\infty}}\left(\Theta_{h_{L}}(L)\right) \leqslant \frac{1}{2}$$
on $X_{0}$.
Step 3: Controlling the error term. Let us get now to the last step in showing that the term
$$\int_{X_{0}}\left|\bar{\partial} u_{\varepsilon}\right|_{h}^{2} d V_{\omega_{\infty}}$$
tends to zero as $\varepsilon \rightarrow 0$. Since $u$ is holomorphic, we have
$$\bar{\partial} u_{\varepsilon}=u \otimes \bar{\partial} \theta_{\varepsilon} ;$$
we recall now that $u \in \mathscr{H}_{B}^{r, s}(X \mid \Delta)$, so we have
$$\left|\bar{\partial} u_{\varepsilon}\right|_{h}^{2} \leqslant C\left|\bar{\partial} \theta_{\varepsilon}\right|_{\omega_{\infty}}^{2} .$$
By inequality (5.2) above we infer
$$\begin{aligned}
& \int_{X_{0}}\left|\bar{\partial} u_{\varepsilon}\right|_{h}^{2} d V_{\omega_{\infty}} \\
& \quad \leqslant C \int_{X_{0}} \frac{\left|\chi_{\varepsilon}^{\prime}(\rho)\right|^{2}}{\log ^{2} \frac{1}{\prod_{i}\left|s_{i}\right|^{2}}}\left(\sum_{j} \frac{1}{\left|s_{j}\right|^{2\left(1-a_{j}\right)}}+\sum_{k} \log ^{2}\left|s_{k}\right|^{2}\right) d V_{\omega_{\infty}}
\end{aligned}$$
As $\omega_{\infty}$ as mixed Poincaré and cone singularities along $\Delta$, we have:
$$\int_{X_{0}}\left|\bar{\partial} u_{\varepsilon}\right|_{h}^{2} d V_{\omega_{\infty}} \leqslant C \int_{X_{0}} \frac{\left|\chi_{\varepsilon}^{\prime}(\rho)\right|^{2}\left(\sum_{j} \frac{1}{\left|s_{j}\right|^{2\left(1-a_{j}\right)}}+\sum_{k} \log ^{2}\left|s_{k}\right|^{2}\right)}{\prod_{j}\left|s_{j}\right|^{2 a_{j}} \prod_{k}\left|s_{k}\right|^{2} \log ^{2}\left|s_{k}\right|^{2} \cdot \log ^{2} \frac{1}{\prod_{i}\left|s_{i}\right|^{2}}} d V_{\omega}$$
for some constant $C>0$ independent of $\varepsilon$; here we denote by $\omega$ a smooth hermitian metric on $X$. We remark that the support of the function $\chi_{\varepsilon}^{\prime}(\rho)$ is contained in the set
$$e^{-e^{1+1 / \varepsilon}} \leqslant \prod_{i}\left|s_{i}\right|^{2} \leqslant e^{-e^{1 / \varepsilon}}$$
so in particular we have
$$\frac{\left|\chi_{\varepsilon}^{\prime}(\rho)\right|^{2}}{\log ^{1} 2 \frac{1}{\prod_{j}\left|s_{i}\right|^{2}}} \leqslant C e^{-\frac{1}{2 \varepsilon}}$$
We also notice that for each indexes $j_{0} \in J$ and $k_{0} \in K$ we have respectively:
$$\begin{aligned}
& \int_{X_{0}} \frac{d V_{\omega}}{\left|s_{j_{0}}\right|^{2} \log ^{3 / 2}\left(\frac{1}{\prod_{i}\left|s_{i}\right|^{2}}\right) \prod_{j \neq j_{0}}\left|s_{j}\right|^{2 a_{j}} \prod_{k}\left|s_{k}\right|^{2} \log ^{2}\left|s_{k}\right|^{2}} \\
& \quad \leqslant C \int_{X_{0}} \frac{d V_{\omega}}{\left|s_{j_{0}}\right|^{2} \log ^{3 / 2}\left(\frac{1}{\left|s_{j_{0}}\right|^{2}}\right) \prod_{j \neq j_{0}}\left|s_{j}\right|^{2 a_{j}} \prod_{k}\left|s_{k}\right|^{2} \log ^{2}\left|s_{k}\right|^{2}}
\end{aligned}$$
and
$$\begin{aligned}
& \int_{X_{0}} \frac{d V_{\omega}}{\left|s_{k_{0}}\right|^{2} \log ^{3 / 2}\left(\frac{1}{\prod_{i}\left|s_{i}\right|^{2}}\right) \prod_{j}\left|s_{j}\right|^{2 a_{j}} \prod_{k \neq k_{0}}\left|s_{k}\right|^{2} \log ^{2}\left|s_{k}\right|^{2}} \\
& \quad \leqslant C \int_{X_{0}} \frac{d V_{\omega}}{\left|s_{k_{0}}\right|^{2} \log ^{3 / 2}\left(\frac{1}{\left|s_{k_{0}}\right|^{2}}\right) \prod_{j}\left|s_{j}\right|^{2 a_{j}} \prod_{k \neq k_{0}}\left|s_{k}\right|^{2} \log ^{2}\left|s_{k}\right|^{2}}
\end{aligned}$$
and the integral in the right hand sides are convergent, given that the hypersurfaces $\left(\Delta_{i}\right)$ have strictly normal intersections.

Finally we combine the inequalities (5.7)-(5.8), and we get
$$\int_{X_{0}}\left|\bar{\partial} u_{\varepsilon}\right|^{2} d V_{\omega_{\infty}} \leqslant C e^{-\frac{1}{2 \varepsilon}}$$

Step 4: Conclusion. As we can see, the relations (5.3) and (5.9) combined with the fact, coming from (5.4), that
$$\left\langle\mathcal{R}\left(u_{\varepsilon}\right), u_{\varepsilon}\right\rangle_{h}+\gamma\left|u_{\varepsilon}\right|_{h}^{2} \leqslant\left(\frac{1}{2}+s-r\right)\left|u_{\varepsilon}\right|_{h}^{2}$$
(which tends to $\left(\frac{1}{2}+s-r\right)|u|_{h}^{2}$ ) will give a contradiction if $u$ is not identically zero on $X_{0}$ (we recall that by hypothesis we have $r \geqslant s+1$ ). \(\square\)

\section*{BIBLIOGRAPHY}
\begin{itemize}
\item[] [1] H. Auvray, "The space of Poincaré type Kähler metrics on the complement of a divisor", arXiv:1109.3159, 2011.
\item[] [2] E. Bedford \& B. Taylor, "A new capacity for plurisubharmonic functions", Acta Math. 149 (1982), no. 1-2, p. 1-40.
\item[] [3] S. Benelkourchi, V. Guedj \& A. Zeriahi, "A priori estimates for weak solutions of complex Monge-Ampère equations", Ann. Sc. Norm. Super. Pisa, Cl. Sci. 7 (2008), no. 1, p. 81-96.
\end{itemize}
[4] R. Berman, S. Boucksom, P. Eyssidieux, V. Guedj \& A. Zeriahi, "Kähler-Einstein metrics and the Kähler-Ricci flow on log-Fano varieties", arXiv:1111.7158v2, 2011.
[5] R. J. Berman, "A thermodynamical formalism for Monge-Ampèe equations, Moser-Trudinger inequalities and Kähler-Einstein metrics", Adv. Math. 248 (2013), p. 1254-1297.
[6] Z. Beocki, "The Calabi-Yau theorem", in Complex Monge-Ampère equations and geodesics in the space of Kähler metrics, Lecture Notes in Math., vol. 2038, Springer, Heidelberg, 2012, p. 201-227.
[7] S. Boucksom, P. Eyssidieux, V. Guedj \& A. Zeriahi, "Monge-Ampère equations in big cohomology classes", Acta Math. 205 (2010), no. 2, p. 199-262.
[8] S. Brendle, "Ricci flat Kähler metrics with edge singularities", Int. Math. Res. Not. IMRN (2013), no. 24, p. 5727-5766.
[9] F. Campana, "Orbifoldes spéciales et classification biméromorphe des variétés kähleriennes compactes", arXiv:0705.0737, 2009.
[10] -, "Special orbifolds and birational classification: a survey ", arXiv:1001.3763, 2010.
[11] F. Campana, H. Guenancia \& M. Păun, "Metrics with cone singularities along normal crossing divisors and holomorphic tensor fields", Ann. Sci. Éc. Norm. Supér. (4) 46 (2013), no. 6, p. 879-916.
[12] J. Carlson \& P. Griffiths, "A defect relation for equidimensional holomorphic mappings between algebraic varieties", Ann. Math. 95 (1972), p. 557-584.
[13] S.-Y. Cheng \& S.-T. Yau, "On the existence of a complete Kähler metric on noncompact complex manifolds and the regularity of Fefferman's equation", Commun. Pure Appl. Math. 33 (1980), p. 507-544.
[14] B. Claudon, " $\Gamma$-reduction for smooth orbifolds", Manuscripta Math. 127 (2008), no. 4, p. 521-532.
[15] J.-P. Demailly, "Potential theory in several complex variables", Lecture given at the CIMPA in 1989, completed by a conference given in Trento, 1992; avalaible at the author's webpage: http://www-fourier.ujf-grenoble.fr/~demailly/books. html.
[16] J.-P. Demailly, "Algebraic criteria for Kobayashi hyperbolic projective varieties and jet differentials", in Algebraic geometry-Santa Cruz 1995, Proc. Sympos. Pure Math., vol. 62, Amer. Math. Soc., Providence, RI, 1997, p. 285-360.
[17] D. Gilbarg \& N. S. Trudinger, Elliptic partial differential equations of second order, Springer-Verlag, Berlin-New York, 1977, Grundlehren der Mathematischen Wissenschaften, Vol. 224, x+401 pages.
[18] P. A. Griffiths, Entire holomorphic mappings in one and several complex variables, Princeton University Press, Princeton, N. J.; University of Tokyo Press, Tokyo, 1976, The fifth set of Hermann Weyl Lectures, given at the Institute for Advanced Study, Princeton, N. J., October and November 1974, Annals of Mathematics Studies, No. 85, $\mathrm{x}+99$ pages.
[19] V. Guedj \& A. Zeriahi, "The weighted Monge-Ampère energy of quasi plurisubharmonic functions", J. Funct. An. 250 (2007), p. 442-482.
[20] V. Guedj \& A. Zeriahi, "Intrinsic capacities on compact Kähler manifolds", J. Geom. Anal. 15 (2005), no. 4, p. 607-639.
[21] T. Jeffres, "Uniqueness of Kähler-Einstein cone metrics", Publ. Mat. 4444 (2000), no. 2, p. 437-448.
[22] T. Jeffres, R. Mazzeo \& Y. Rubinstein, "Kähler-Einstein metrics with edge singularities", arXiv:1105.5216, with an appendix by C. Li and Y. Rubinstein, 2011.
[23] R. Kobayashi, "Kähler-Einstein metric on an open algebraic manifolds", Osaka 1. Math. 21 (1984), p. 399-418.
\begin{itemize}
\item[] [24] S. KoŁodziej, "The complex Monge-Ampère operator", Acta Math. 180 (1998), no. 1, p. 69-117.
\item[] [25] -, "Stability of solutions to the complex Monge-Ampère equations on compact Kähler manifolds", Preprint, 2001.
\item[] [26] R. Mazzeo, "Kähler-Einstein metrics singular along a smooth divisor", Journées "Équations aux dérivées partielles" (Saint Jean-de-Monts, 1999) (1999), p. Exp. VI, 10.
\item[] [27] Y. T. Siu, Lectures on Hermitian-Einstein metrics for stable bundles and KählerEinstein metrics, DMV Seminar, vol. 8, Birkhäuser Verlag, Basel, 1987, 171 pages.
\item[] [28] G. Tian \& S.-T. Yau, "Existence of Kähler-Einstein metrics on complete Kähler manifolds and their applications to algebraic geometry", in Mathematical aspects of string theory (San Diego, Calif., 1986), Adv. Ser. Math. Phys., vol. 1, World Sci. Publishing, Singapore, 1987, p. 574-628.
\item[] [29] S.-T. Yau, "A general Schwarz lemma for Kähler manifolds", Amer. J. Math. 100 (1978), p. 197-203.
\end{itemize}

Manuscrit reçu le 23 février 2012, accepté le 22 juillet 2013.

Henri GUENANCIA
Université Pierre et Marie Curie
Institut de Mathématiques de Jussieu, Paris
\& École Normale Supérieure
Département de Mathématiques et Applications
Paris (France)
guenancia@math.jussieu.fr
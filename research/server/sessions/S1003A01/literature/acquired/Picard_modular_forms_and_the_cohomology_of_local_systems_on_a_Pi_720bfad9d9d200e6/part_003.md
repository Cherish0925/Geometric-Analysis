---
retention_scope: session
part: 3
total_parts: 4
---

[Part 3/4 of: Picard modular forms and the cohomology of local systems on a Picard modular surface]

Together, case iv) and v) contribute $(q+1)\left(\mathbf{s}_{4}+\mathbf{s}_{3,1}\right)$ and they form a $\mathbb{P}^{1}$-bundle under the morphism (5.1). Hence, their image (the four cusps) contribute $\mathbf{s}_{4}+\mathbf{s}_{3,1}$ and we get a trace of Frobenius equal to
$$\operatorname{Tr}\left(F_{q}, e_{c}\left(\mathcal{X}_{\Gamma[\sqrt{-3}]}^{*} \otimes \bar{k}, \overline{\mathbb{Q}}_{\ell}\right)\right)=\left(q^{2}+q+1\right) \mathbf{s}_{4},$$
which echoes the fact that $X_{\Gamma[\sqrt{-3}]}^{*} \cong \mathbb{P}^{2}$.
8.2.1. The genus 2 case. There are two strata in $\mathcal{X}_{\Gamma[\sqrt{-3}]}^{(2)}$, one consisting of smooth genus 2 curves and one consisting of pairs of genus one curves, one with action of type $(1,0)$ and one of type (0, 1), joined at a ramification point on each curve. There is an action of $\mathfrak{S}_{2} \times \mathfrak{S}_{2}$ on the two pairs of ramification points, one pair where the action of $\alpha$ is by $\rho$ and one by $\rho^{2}$. Let us use the notation $\mathbf{p}_{i}$ and $\tilde{\mathbf{p}}_{i}$, and $\mathbf{s}_{\mu}$ and $\tilde{\mathbf{s}}_{\mu}$, for the basis of representations of the two components of $\mathfrak{S}_{2} \times \mathfrak{S}_{2}$. A consideration analogous to the ones above shows that
$$\begin{aligned}
& \operatorname{Tr}\left(F_{q}, e_{c}\left(\mathcal{X}_{\Gamma[\sqrt{-3}]}^{(2)} \otimes \bar{k}, \overline{\mathbb{Q}}_{\ell}\right)\right)=\left((q+1) q(q-1)(q-2) \frac{\mathbf{p}_{1}^{2} \tilde{\mathbf{p}}_{1}^{2}}{4}\right. \\
+ & \left.\left(q^{2}-q\right)(q+1) q \frac{\mathbf{p}_{2} \tilde{\mathbf{p}}_{1}^{2}+\mathbf{p}_{1}^{2} \tilde{\mathbf{p}}_{2}}{4}+\left(q^{2}-q\right)\left(q^{2}-q-2\right) \frac{\mathbf{p}_{2} \tilde{\mathbf{p}}_{2}}{4}\right) /((q+1) q(q-1)) \\
& \quad+\frac{\mathbf{p}_{1}^{2} \tilde{\mathbf{p}}_{1}^{2}}{4}+\frac{\mathbf{p}_{1}^{2} \tilde{\mathbf{p}}_{2}}{4}+\frac{\mathbf{p}_{2} \tilde{\mathbf{p}}_{1}^{2}}{4}+\frac{\mathbf{p}_{2} \tilde{\mathbf{p}}_{2}}{4}=q \mathbf{s}_{2} \tilde{\mathbf{s}}_{2}-\mathbf{s}_{1,1} \tilde{\mathbf{s}}_{1,1},
\end{aligned}$$
and we can conclude the following.
Proposition 8.3. We have an equality of elements in $K_{0}\left(\mathrm{Gal}_{F}^{\mathfrak{S}_{4}}\right)$ :
$$\left.e_{c}\left(\mathcal{X}_{\Gamma[\sqrt{-3}]}^{(2)} \otimes \bar{k}, \overline{\mathbb{Q}}_{\ell}\right)\right)=\mathbb{L} \mathbf{s}_{2} \tilde{\mathbf{s}}_{2}-\mathbf{s}_{1,1} \tilde{\mathbf{s}}_{1,1} .$$
8.3. Euler characteristics of local systems for elliptic curves. Using the results of Section 6.2.1 and Section 7.3 we find that
$$\operatorname{Tr}\left(F_{q}, e_{c}\left(\mathcal{X}_{\Gamma[\sqrt{-3}]}^{(1)} \otimes \bar{k}, \mathbb{W}_{k}\right)\right)=\sum_{i=0}^{2} \rho^{k i}\left(a_{\mathfrak{p}_{q}}+b_{\mathfrak{p}_{q}} \rho^{2}\right)^{k}\left(\mathbf{p}_{1}^{2}+(-1)^{k} \mathbf{p}_{2}\right),$$
for all $q$ such that $q \equiv_{3} 1$. This equality, together with the fact that an element in $K_{0}\left(\mathrm{Gal}_{F}\right)$ is determined by all traces of Frobenius, shows the following.

Proposition 8.4. For any $k \geq 0$, we have the equality in $K_{0}^{\mathfrak{S}_{4}}\left(\operatorname{Gal}_{F}\right)$ :
$$e_{c}\left(\mathcal{X}_{\Gamma[\sqrt{-3}]}^{(1)}, \mathbb{W}_{k}\right)= \begin{cases}\mathbb{L}^{0, k} \mathbf{s}_{2} & \text { if } k \equiv_{6} 0 \\ \mathbb{L}^{k, 0} \mathbf{s}_{1^{2}} & \text { if } k \equiv_{6} 3 \\ 0 & \text { if } k \neq_{3} 0\end{cases}$$

\section*{9. Numeric Euler characteristics of local systems}

In this section the ground field will be $\mathbb{C}$, we will consider the compactly supported Betti cohomology, and we will find a formula for the integervalued Euler characteristic,
$$E_{c, \mu}\left(X_{\Gamma[\sqrt{-3}]}, \mathbb{W}_{\lambda}\right):=\sum_{i=0}^{4}(-1)^{i} \operatorname{dim}_{\mathbb{C}} H_{c, \mu}^{i}\left(X_{\Gamma[\sqrt{-3}]}, \mathbb{W}_{\lambda}\right) \in \mathbb{Z}$$
for any $\lambda$ and $\mu$, where $H_{c, \mu}^{i}$ is the $\mu$-isotypic component of $H_{c}^{i}$. Examples of computations using this formula will be found in Section 13.1.

Similarly to the above we will write,
$$E_{c}\left(X_{\Gamma[\sqrt{-3}]}, \mathbb{W}_{\lambda}\right):=\sum_{\mu \vdash 4} \frac{E_{c, \mu}\left(X_{\Gamma[\sqrt{-3}]}, \mathbb{W}_{\lambda}\right)}{\operatorname{dim} \mathbf{s}_{\mu}} \mathbf{s}_{\mu} \in \mathbb{Z}\left[\mathfrak{S}_{4}\right] .$$
The reader should compare this section to the article [6] and the references therein. Note that by comparison theorems this numerical Euler characteristic will be the same if Betti cohomology is replaced by $\ell$-adic étale cohomology as described in Section 7. So, $E_{c}\left(X_{\Gamma[\sqrt{-3}]}, \mathbb{W}_{\lambda}\right)$ equals $\operatorname{dim} e_{c}\left(\mathcal{X}_{\Gamma[\sqrt{-3}]}, \mathbb{W}_{\lambda}\right)$ for any $\lambda$ of even weight.

We stratify our moduli space $X_{\Gamma}$, first into $X_{1, \Gamma}, X_{2, \Gamma}$ and $X_{3, \Gamma}$ as in Section 5.3. We then stratify further into strata $\Sigma_{i}(G)$, for $i=1,2,3$ and $G$ a finite group, consisting of the curves corresponding to points of $X_{i, \Gamma}$ whose automorphism group equals $G$. As usual, let $H^{1}(C, \mathbb{C})^{\rho}$ denote the $\rho$-eigenspace of $H^{1}(C, \mathbb{C})$ when acting by $\alpha$. Say that $g \in G$ has eigenvalues $\xi_{1}(g), \xi_{2}(g)$ and $\xi_{3}(g)$ when acting on $H^{1}(C, \mathbb{C})^{\rho}$ of a curve $C \in \Sigma(G)$. Say furthermore that the induced action of $g \in G$ on the four ramification points of $C \in \Sigma_{i}(G)$ where $\alpha$ acts by $\rho$ has $\nu_{i}$ cycles of length $i$. Note that this data will be constant on the strata, i.e. independent of the choice of $C \in \Sigma_{i}(G)$.

If $e_{c}\left(\Sigma_{i}(G)\right)$ denotes the usual compactly supported Euler characteristic of $\Sigma_{i}(G)$ then
$$E_{c}\left(X_{\Gamma[\sqrt{-3}]}, \mathbb{W}_{\lambda}\right)=\sum_{i=1}^{3} \sum_{G} \frac{E_{c}\left(\Sigma_{i}(G)\right)}{|G|} \sum_{g \in G} s_{\lambda}\left(\xi_{1}(g), \xi_{2}(g), \xi_{3}(g)\right) \mathbf{p}_{\nu} .$$
In the sections below, we will find the necessary information to compute this formula for any given $\lambda$.

In all cases below, the automorphism groups that appear are cyclic, so it is enough to give the three eigenvalues of a generator, which we will denote by $\phi$, together with its cycle type as a permutation of the four ramification points.

\subsection*{9.1. Numerical Euler characteristics for smooth curves of genus 3.}

One easily finds that there are four different cyclic automorphism groups in this case, namely the generic case $\mathbf{C}_{3}$ and then $\mathbf{C}_{6}, \mathbf{C}_{9}$ and $\mathbf{C}_{12}$. The strata for $\mathbf{C}_{9}$ and $\mathbf{C}_{12}$ consist of a single point. For $\mathbf{C}_{6}$, the stratum is 1-dimensional. Each isomorphism class can be represented by a curve of the form $f=x^{4}+a x^{2}+1$ with $a \in \mathbb{C}$. To make this a smooth curve we need $a^{2} \neq 0,1$. Moreover, two curves of this form are isomorphic precisely if their coefficients $a$ differ by a sign. This shows that the Euler characteristic of this stratum equals -1. The whole moduli space $X_{1, \Gamma}$ is described in the end of Section 2 and we find that it has Euler characteristic 1 (compare with the point count in Section 8.2). From this it follows that the Euler characteristic of the generic (open dense) stratum must be 0 .

We have an isomorphism $H^{1}(C, \mathbb{C}) \cong H^{0}(C, \Omega) \oplus \overline{H^{0}(C, \Omega)}$ and the subspace $H^{1}(C, \mathbb{C})^{\rho}$ has a basis consisting of $d x / y^{2}, x d x / y^{2}$ and the dual of $d x / y$. The eigenvalues of the action of $\phi$ on $H^{1}(C, \mathbb{C})^{\rho}$ can thus be found through its action on this basis.

We exemplify such a computation in the case of $\mathbf{C}_{9}$. The other cases are completely analogous. We have that $\phi$ applied to $d x / y^{2}, x d x / y^{2}$ and $d x / y$ equals $\rho d x /\left(\epsilon^{2} y^{2}\right)=\epsilon d x / y^{2}, \rho^{2} d x /\left(\epsilon^{2} y^{2}\right)=\rho \epsilon d x / y^{2}$ and $\rho d x /(\epsilon y)=\epsilon^{2} d x / y$. The action should be on the dual of $\rho d x / y$ and hence this eigenvalue becomes $\epsilon^{-2}=\rho^{2} \epsilon$. We see that the action of $\phi$ cyclically permutes three of the ramification points and fixes the fourth.

The data to compute the contribution from the strata $X_{1, \Gamma[\sqrt{-3}]}$ to equation (9.1), is found in the table below.

\begin{tabular}[t]{|l|l|l|l|l|l|}
\hline $G$ & $f$ & $\Sigma_{1}(G)$ & $\phi(x, y)$ & $\xi_{1}(\phi), \xi_{2}(\phi), \xi_{3}(\phi)$ & $\mathbf{p}_{\nu}$ \\
\hline $\mathbf{C}_{3}$ & & 0 & $(x, \rho y)$ & $\rho, \rho, \rho$ & $\mathbf{p}_{1}^{4}$ \\
\hline $\mathbf{C}_{6}$ & $x^{4}+a x^{2}+1$ & -1 & $(-x, \rho y)$ & $\rho,-\rho,-\rho$ & $\mathbf{p}_{2}^{2}$ \\
\hline $\mathbf{C}_{9}$ & $x\left(x^{3}-1\right)$ & 1 & $(\rho x, \epsilon y)$ & $\epsilon, \rho \epsilon, \rho^{2} \epsilon$ & $\mathbf{p}_{1} \mathbf{p}_{3}$ \\
\hline $\mathbf{C}_{12}$ & $x^{4}-1$ & 1 & $(i x, \rho y)$ & $-\rho, i \rho,-i \rho$ & $\mathbf{p}_{4}$ \\
\hline
\end{tabular}
9.2. Numerical Euler characteristics for smooth genus 2 curves joined with elliptic curves. Let us first consider smooth genus 2 curves $C_{f_{1}, f_{2}}$ together with a marked root of $f_{2}$, which we place in infinity, see Section 5.7. Note that the hyperelliptic involution does not fix the marked point. There are two strata. The generic strata, with automorphism group $\mathbf{C}_{3}$, has a representative $f_{1}=x^{2}+a x+1, f_{2}=x$ for each $a \neq 0 \in \mathbb{C}$. This gives an Euler characteristic equal to -1. The strata with automorphism group $\mathbf{C}_{6}$ consists of a point, given by $a=0$. In this case, the involution switches the two ramification points where $\alpha$ acts by $\rho$. In both cases, the subspace $H^{1}\left(C_{f_{1}, f_{2}}, \mathbb{C}\right)^{\rho}$ has a basis consisting of $x d x / y^{2}$ and the dual of $d x / y$. Computations as in the previous section gives the following table.

\begin{tabular}[t]{|l|l|l|l|l|l|}
\hline $G$ & $f_{1} f_{2}^{2}$ & $\Sigma_{1}(G)$ & $\phi(x, y)$ & $\xi_{1}(\phi), \xi_{2}(\phi), \xi_{3}(\phi)$ & $\mathbf{p}_{\nu}$ \\
\hline $\mathbf{C}_{3}$ & $\left(x^{2}+a x+1\right) x^{2}$ & -1 & $(x, \rho y)$ & $\rho, \rho$ & $\mathbf{p}_{1}^{2}$ \\
\hline $\mathbf{C}_{6}$ & $\left(x^{2}+1\right) x^{2}$ & 1 & $(-x, \rho y)$ & $\rho,-\rho$ & $\mathbf{p}_{2}$ \\
\hline
\end{tabular}

The elliptic curves come with a marked ramification point at infinity and there is only one stratum consisting of the curve with equation $y^{3}=$ $x^{2}+1$ and automorphism group $\mathbb{Z} / 6 \mathbb{Z}$ generated by the element $\phi:(x, y) \mapsto$ $(-x, \rho y)$. The single eigenvalue of $\phi$ acting on $H_{c}^{1}(C, \mathbb{C})^{\rho}$ is $-\rho$. Furthermore $\phi^{i}$ permutes the ramification points if $i$ is odd and fixes them if $i$ is even.

The possible automorphism groups of curves $C_{f_{1}, f_{2}, f_{3}} \in X_{2, \Gamma[\sqrt{-3}]}$ are just products of the automorphism groups for $C_{f_{1}, f_{2}}$ and $C_{f_{3}}$. Moreover, we have that $H^{1}\left(C_{f_{1}, f_{2}, f_{3}}, \mathbb{C}\right)^{\rho} \cong H^{1}\left(C_{f_{1}, f_{2}}, \mathbb{C}\right)^{\rho} \oplus H^{1}\left(C_{f_{3}}, \mathbb{C}\right)^{\rho}$. So, piecing together the information above enables us to compute the contribution from $X_{2, \Gamma[\sqrt{-3}]}$ to equation (9.1).
9.3. Numerical Euler characteristics for triples of elliptic curves. Triples of elliptic curves $C_{f_{1}, f_{2}, f_{3}^{2}}$ are described in Section 5.8. The "backbone", corresponding to $f_{3}^{2}$, will only have an automorphism group generated by $\alpha$, because two of its ramification points are fixed. Then there is an additional automorphism $\sigma$ by switching the two "wings" corresponding to $f_{1}$ and $f_{2}$. This gives rise to an automorphism group of the form $G=\mathbf{C}_{3} \times\left(\mathbf{C}_{6} \prec \mathfrak{S}_{2}\right)$, where $\}$ denotes the wreath product. Say that $\alpha_{i}$ is an automorphism of $C_{f_{i}}$ for $i=1 \ldots 3$ with eigenvalues $\tau_{i}$ acting on $H^{1}\left(C_{f_{i}}, \mathbb{C}\right)^{\rho}$, then these will also be the eigenvalues of the induced action on $H^{1}\left(C_{f_{1}, f_{2}, f_{3}^{2}}, \mathbb{C}\right)^{\rho} \cong H^{1}\left(C_{f_{1}}, \mathbb{C}\right)^{\rho} \oplus H^{1}\left(C_{f_{2}}, \mathbb{C}\right)^{\rho} \oplus H^{1}\left(C_{f_{3}^{2}}, \mathbb{C}\right)^{\rho}$. If the previous automorphism is composed with the involution in $\mathfrak{S}_{2}$, the eigenvalues will be $\left(\tau_{1} \tau_{2}\right)^{1 / 2},-\left(\tau_{1} \tau_{2}\right)^{1 / 2}, \tau_{3}$. From this information one can compute the contribution from $X_{3, \Gamma[\sqrt{-3}]}$ to equation (9.1).

\section*{10. Our approach}

Here we will explain the approach that led us to the conjectures on Picard modular forms in Section 11 and 12.
10.1. Computer counts over finite fields. Using the results of Section 8 we computed
$$\operatorname{Tr}\left(F_{q}, e_{c, \mu}^{\text {norm }}\left(\mathcal{X}_{\Gamma[\sqrt{-3]}} \otimes \bar{k}, \mathbb{W}_{\lambda}\right)\right)$$
for all prime powers $q \equiv_{3} 1$ such that $q \leq 67$, and all partitions $\lambda$ such that $n_{1}+n_{2}+2 \leq 40$. These traces always turned out to be in $\mathbb{Z}[\rho]$ as they should be, see Section 7.3.

The conjectures of this section are based upon these computer counts (using the equality (7.2)).
10.2. Preview. We are interested in calculating the trace of Hecke operators on the $\mathfrak{S}_{4}$-isotypic components of the space $S_{j, k, l}\left(\Gamma_{1}[\sqrt{-3}]\right)$ of cusp forms of given weight. In the analogous case of the space $S_{k}$ of cusp forms of weight $k$ on $\operatorname{SL}(2, \mathbb{Z})$ one can use for even $k>0$ the formula
$$\operatorname{Tr}\left(T(p), S_{k+2}\right)=\operatorname{Tr}\left(F_{p}, S[k+2]\right)$$
with $S[k+2]$ the Chow motive of dimension $2 \operatorname{dim} S_{k+2}$ associated by Scholl ([44]) to the space $S_{k+2}$ and $F_{p}$ denotes Frobenius. By Deligne's result the motive $S[k+2]$ can be found inside the cohomology of a local system $\mathbb{V}_{k}$ on the moduli space $\mathcal{A}_{1}$ of elliptic curves
$$e_{c}\left(\mathcal{A}_{1}, \mathbb{V}_{k}\right)=-S[k+2]-1$$
and we thus can use counts of points over finite fields to calculate the trace of Frobenius on this cohomology and thus the traces of the Hecke operators. Note that the -1 in the last formula comes from the Eisenstein cohomology. By replacing $e_{c}$ by the inner cohomology $e_{!}$we get rid of it. We remark that equation (10.1) still holds for $k=0$ if we put $S[2]=-\mathbb{L}-1$.

We want the analogue of this for our Picard modular case. Ideally, in our case one would hope for the existence of a motive $S[j, k, l]$ of dimension $3 \operatorname{dim} S_{j, k, l}(\Gamma[\sqrt{-3}])$ defined over $F$ such that
$$\operatorname{Tr}\left(T(\nu), S_{j, k, l}\left(\Gamma_{1}[\sqrt{-3}]\right)=\operatorname{Tr}\left(F_{\nu}, S[j, k, l]\right)\right.$$
with $T(\nu)$ the Hecke operator for any $\nu \in \mathbb{Z}[\rho]$ such that $\nu \equiv_{3} 1$ and $\nu \bar{\nu}=p$ a prime and $F_{\nu}$ is the Frobenius as in Section 7.3 (see also Section 6.1). Moreover, $S[j, k, l]$ should appear $\mathfrak{S}_{4}$-equivariantly in the second inner cohomology group of the corresponding local system on our moduli space, see Proposition 3.3.

However, one must expect deviations from this due to the fact that there will be liftings from U(1) and GL(2). In Section 11 we make precise conjectures on all such lifts. To any of these lifts $f$ that is a Hecke eigenform we can (conjecturally) associate a reducible 3-dimensional Galois representation $M_{f}$ defined over $F$ such that
$$\operatorname{Tr}(T(\nu), f)=\operatorname{Tr}\left(F_{\nu}, M_{f}\right) .$$
But for most of these in we only see a contribution from a 1-dimensional or 2-dimensional part of $M_{f}$ in the étale cohomology of our local systems. After removing these cusp forms we are left with a (conjectural) Hecke-invariant
subspace of what we call genuine Picard modular forms and that we denote by $S_{j, k, l}^{\text {gen }}\left(\Gamma_{1}[\sqrt{-3}]\right)$. So, to each Hecke eigenform in this space there should be a 3-dimensional Galois representation appearing in the cohomology and its (normalized) Hodge degrees in Betti cohomology should be $(j+k-1,0)$, $(j+1, k-2)$ and $(0, j+k-1)$.

For any $n_{1} \equiv_{3} n_{2}$ and $n_{1} \equiv_{2} n_{3}$, our goal is to have a formula analogous to equation (10.1), namely,
$$e_{c}^{\text {norm }}\left(\mathcal{X}_{\Gamma[\sqrt{-3}]}, \mathbb{W}_{\lambda}\right)=\breve{S}[n(\lambda)]+e_{\text {extr }}(\lambda)$$
equivariant for the action of $\mathfrak{S}_{4}$ and with $e_{\text {extr }}(\lambda)$ coming from endoscopic groups such that (except for the case $n_{1}=n_{2}=n_{3}=0$ )
$$\operatorname{Tr}\left(T(\nu), S_{n(\lambda)}^{\text {gen }}(\Gamma[\sqrt{-3}])\right)=\operatorname{Tr}\left(F_{\nu}, \breve{S}[n(\lambda)]\right) .$$
for any $\nu \equiv_{3} 1$ with norm $p$ a prime and with $n(\lambda)=\left(n_{2}, n_{1}+3, n_{2}+n_{3}-1\right)$. Ideally equation (10.2) should be an equality of motives, but we can also treat it as an equality of bookkeeping devices for calculating traces as in equation (10.3). To make equation (10.2) hold also in the case $n_{1}=n_{2}=$ $n_{3}=0$ we put $\breve{S}[0,3,2]=\left(\mathbb{L}^{2}+\mathbb{L}+1\right) \mathbf{s}_{4}$, see Proposition 8.1.

Analogously, for the numerical Euler characteristic we should have
$$\operatorname{dim}_{\mathfrak{S}_{4}} S_{n(\lambda)}^{\text {gen }}(\Gamma[\sqrt{-3}])=\frac{1}{3}\left(E_{c}\left(X_{\Gamma[\sqrt{-3}]}, \mathbb{W}_{\lambda}\right)-E_{\text {extr }}(\lambda)\right) .$$

This is formulated in Main conjecture 12.9 and Conjecture 12.12. All of the conjectures of the following sections was found by analyzing the data described in Section 10.1 together with all of the knowledge acquired in the previous sections.
10.3. Notation for local systems and Hecke operators. In the following sections we will use a slightly different notation for our local systems $\lambda=n_{1} \gamma_{1}+n_{2} \gamma_{2}+n_{3} \gamma_{3}$ writing $\lambda=(a+i, i,-b+i)$ with $n_{1}=a, n_{2}=b$, $n_{3}=-b+i$. Assume from now on that $a \equiv_{3} b$ and put $n(\lambda)=(b, a+3, i+2)$. So, if $i \equiv_{2} a+b$ then we expect a Galois representation (of dimension 1, 2 or 3) corresponding to each eigenform in $S_{n(\lambda)}(\Gamma[\sqrt{-3}])$ appearing (with positive coefficient) in $e_{c}\left(\mathcal{X}_{\Gamma[\sqrt{-3}]}, \mathbb{W}_{\lambda}\right)$. If $i \not \neq 2_{2} a+b$ we expect the same contribution but with the $\mathfrak{S}_{4}$-action twisted by $\mathbf{s}_{14}$, compare Proposition 7.4.

By $\nu$ we will always mean an element of $\mathbb{Z}[\rho]$ such that $\nu \equiv_{3} 1$ and $\nu \bar{\nu}=p$ with $p$ a prime. To such an element there is a corresponding Hecke operator acting on $S_{n(\lambda)}(\Gamma[\sqrt{-3}])$ that we denote by $T(\nu)$, see Section 2.3.

Finally, $\mu$ will denote a partition of 4.

\section*{11. Conjectured Lifts}

By analyzing the data described in Section 10.1 we see Galois representations in the cohomology of our local systems that seem to be associated to lifts of modular forms from U(1) or GL(2). The conjectures of this section are based upon these examples.

Each such lifted eigenform then contributes a piece of dimension 1, 2 or 3 to the cohomology. It is important for us to identify the 1-dimensional and 2-dimensional pieces in order to be left with the 'genuine' Picard modular forms with associated irreducible 3-dimensional Galois representations.

We will use the notation from Section 10.3.
11.1. Notation for elliptic modular forms. We write $\Gamma_{0}(N)$ and $\Gamma_{1}(N)$ for the usual subgroups of $\operatorname{SL}(2, \mathbb{Z})$ and we write $S_{k}\left(\Gamma_{0}(N)\right)$ for the space of cusp forms of weight $k$ on $\Gamma_{0}(N)$ and $S_{k}^{\text {new }}\left(\Gamma_{0}(N)\right)$ for the subspace of new forms. The dimensions of these spaces will be denoted by $s_{k}\left(\Gamma_{0}(N)\right)$ and $s_{k}^{\text {new }}\left(\Gamma_{0}(N)\right)$. In our case we will have level $N=3$ or $N=9$.

We note for level 3 and even $k>2$ the dimension formula
$$s_{k}^{\text {new }}\left(\Gamma_{0}(3)\right)= \begin{cases}\left\lfloor\frac{k}{6}\right\rfloor+1 & \text { if } k \equiv_{12} \pm 2 \\ \left\lfloor\frac{k}{6}\right\rfloor-1 & \text { if } k \equiv_{12} 0 \\ \left\lfloor\frac{k}{6}\right\rfloor & \text { else. }\end{cases}$$
For odd $k$ we split the space $S_{k}\left(\Gamma_{1}(3)\right)$ as
$$S_{k}\left(\Gamma_{1}(3)\right)=S_{k}^{-}\left(\Gamma_{1}(3)\right) \oplus S_{k}^{+}\left(\Gamma_{1}(3)\right)$$
into the ±-eigenspace for the Fricke operator $W_{3}$. For odd $k \geq 3$ the dimension of $S_{k}^{ \pm}\left(\Gamma_{1}(3)\right)$ is given by
$$s_{k}^{-}\left(\Gamma_{1}(3)\right)=\left\lfloor\frac{k-3}{6}\right\rfloor, \quad s_{k}^{+}\left(\Gamma_{1}(3)\right)= \begin{cases}\left\lfloor\frac{k-3}{6}\right\rfloor+1 & \text { if } k \equiv_{6} 1, \\ \left\lfloor\frac{k-3}{6}\right\rfloor & \text { else. }\end{cases}$$

Inside the space $S_{k}^{\text {new }}\left(\Gamma_{0}(9)\right)$ we consider the eigenforms $f$ for which the twist $f_{\chi}$, with $\chi$ the non-trivial character modulo 3, is also an eigenform in $S_{k}^{\text {new }}\left(\Gamma_{0}(9)\right)$. These generate a subspace $\Sigma_{k} \subset S_{k}^{\text {new }}\left(\Gamma_{0}(N)\right)$. It may happen that $f=f_{\chi}$ and then $f$ will have Hecke eigenvalues $a(p)=0$ for $p \equiv_{3} 2$. This happens for $k \equiv_{3} 1$, and thus $k \equiv_{6} 4$. A Hecke operator $T(p)$ with $p \equiv_{3} 2$ will have characteristic polynomial on this space that is a polynomial in $x^{2}$ or $x$ times a polynomial in $x^{2}$. We decompose $\Sigma_{k}$ for even $k$
$$\Sigma_{k}=S_{k}^{-}\left(\Gamma_{0}(9)\right) \oplus S_{k}^{+}\left(\Gamma_{0}(9)\right)$$
where $S_{k}^{ \pm}\left(\Gamma_{0}(9)\right)$ is the ±-eigenspace for the twisting $f \mapsto f_{\chi}$. We found experimentally the dimension formulas for $\Sigma_{k}^{ \pm}\left(\Gamma_{0}(9)\right)$
$$s_{k}^{-}\left(\Gamma_{0}(9)\right)= \begin{cases}\left\lfloor\frac{k+4}{12}\right\rfloor-1 & k \equiv_{12} 10 \\ \left\lfloor\frac{k+4}{12}\right\rfloor & \text { else }\end{cases}$$
and
$$s_{k}^{+}\left(\Gamma_{0}(9)\right)= \begin{cases}\left\lfloor\frac{k+4}{12}\right\rfloor+1 & k \equiv_{12} 4 \\ \left\lfloor\frac{k+4}{12}\right\rfloor & \text { else. }\end{cases}$$

For odd $k$ and $\chi$ the quadratic character modulo 3 we will use the space $S_{k}^{\text {new }}\left(\Gamma_{0}(9), \chi\right)$ with dimension
$$s_{k}^{\chi}\left(\Gamma_{0}(9)\right)=\left\lfloor\frac{k+1}{6}\right\rfloor .$$
Finally, another space we will use occurs for $k \equiv_{6} 1$. We consider the subspace $S_{k}^{\chi}\left(\Gamma_{0}(9)\right)$ of $S_{k}^{\text {new }}\left(\Gamma_{0}(9), \chi\right)$ with $\chi$ the quadratic character modulo 3, generated by eigenforms such that both $f$ and its twist $f_{\chi}$ both belong to $S_{k}^{\text {new }}\left(\Gamma_{0}(9), \chi\right)$ and are distinct.
11.2. One-dimensional lifts. Here we present the conjectured lifts of modular forms from U(1). For each of these lifts we see a 1-dimensional piece in the cohomology of the corresponding local system $\mathbb{W}_{\lambda}$ with trace of the Frobenius $F_{\nu}$ equal to $\nu^{a+b+2}$, compare Definition 12.4.
Case 1. For $a \equiv_{6} 3$ there is a theta series $\zeta_{a+3} \in S_{0, a+3,1}(\Gamma[\sqrt{-3}])$ with $\mathfrak{S}_{4}$-representation $\mathbf{s}_{1}$. This eigenform is constructed in [18, Prop. 2]. For $a=3$ we find the form $\zeta$. The Hecke eigenvalue of $T(\nu)$ is given by
$$\nu^{a+2}+(p+1) \bar{\nu}^{a+1},$$
see [18, Prop. 9].
In both of the following two cases the lift in $S_{b, a+3, l}(\Gamma[\sqrt{-3}])$ will have a Hecke eigenvalue of $T(\nu)$ given by
$$\nu^{a+b+2}+\nu^{b+1} \bar{\nu}^{a+1}+\bar{\nu}^{a+b+2} .$$

Case 2. For $(a, b) \equiv_{6}(5,2)$ we find an eigenform in $S_{b, a+3,2}(\Gamma[\sqrt{-3}])$ with $\mathfrak{S}_{4}$-representation $\mathbf{s}_{4}$.

The first example is found in $S_{2,8,2}(\Gamma[\sqrt{-3}])$ and it is described in [9, Example 16.7].
Case 3. We conjecture that there is a lift
$$S_{b+2}^{-}\left(\Gamma_{0}(9)\right) \rightarrow S_{b, a+3,1-a}(\Gamma[\sqrt{-3}])$$
with representation $\mathbf{s}_{4}$.
11.3. Two-dimensional lifts. The Hecke eigenvalue of $T(p)$ for an elliptic eigenform $f$ will be denoted by $a_{p}(f)$. For each lift of an elliptic eigenform $f$, i.e. a lift from GL(2), described in this section we see a 2-dimensional piece in the cohomology of the corresponding local system $\mathbb{W}_{\lambda}$ with trace of Frobenius $F_{p}$ equal to $a_{p}(f) \nu^{b+1}$ in all cases but the first, where we just see $a_{p}(f)$, compare Definition 12.5.
Case 1. We conjecture that there is a lift
$$S_{a+b+3}^{-}\left(\Gamma_{0}(9)\right) \rightarrow S_{b, a+3,2}(\Gamma[\sqrt{-3}])$$
with $\mathfrak{S}_{4}$-representation $\mathbf{s}_{4}$ and the lift of an eigenform $f$ will have Hecke eigenvalue of $T(\nu)$ given by
$$a_{p}(f)+\nu^{b+1} \bar{\nu}^{a+1} .$$

An example is given by the lift from $S_{8}^{-}\left(\Gamma_{0}(9)\right)$ to $S_{1,7,2}(\Gamma[\sqrt{-3}])$; the generating lift is $\Psi_{1}$ described in [9, p. 44]. Another example is the lift from $S_{12}^{-}\left(\Gamma_{0}(9)\right)$ to $S_{0,12,2}(\Gamma[\sqrt{-3}])=\mathbb{C} \zeta^{2}$, already considered by Finis in [18, p. 178].

In the following five cases we will have a lift of an elliptic eigenform $f$ to $S_{b, a+3, l}(\Gamma[\sqrt{-3}])$ and it will have a Hecke eigenvalue of $T(\nu)$ given by
$$a_{p}(f) \nu^{b+1}+\bar{\nu}^{a+b+2} .$$
Case 2a. We conjecture that there is a lift
$$S_{a+2}\left(\Gamma_{0}(1)\right) \rightarrow S_{b, a+3, b}(\Gamma[\sqrt{-3}])$$
with $\mathfrak{S}_{4}$-representation $\mathbf{s}_{2,1^{2}}+\mathbf{s}_{1^{4}}$.
The first example is the lift of $\Delta \in S_{12}\left(\Gamma_{0}(1)\right)$ to a form in $S_{1,13,1}(\Gamma[\sqrt{-3}])$ given in the table on page 43 of [9]. Lifts of this type were constructed by Kudla in [32, Thm. 5.3].
Case 2b. We conjecture that there is a lift
$$S_{a+2}^{-}\left(\Gamma_{1}(3)\right) \rightarrow S_{b, a+3, b}(\Gamma[\sqrt{-3}])$$
with $\mathfrak{S}_{4}$-representation $\mathbf{s}_{4}+\mathbf{s}_{3,1}$.
The first example is the lift from $S_{9}^{-}\left(\Gamma_{1}(3)\right)$ to $S_{1,10,1}(\Gamma[\sqrt{-3}])$ which appears in the table on p. 43 of [9]. Lifts of this type were constructed by Kudla as in Case 2a.
Case 3. We conjecture that there is a lift
$$S_{a+2}^{\text {new }}\left(\Gamma_{0}(3)\right) \rightarrow S_{b, a+3, b}(\Gamma[\sqrt{-3}])$$
with $\mathfrak{S}_{4}$-representation $\mathbf{s}_{2,1^{2}}$.
The lift of $(\eta(3 \tau) \eta(\tau))^{6} \in S_{6}\left(\Gamma_{0}(3)\right)$ to an element of $S_{1,7,1}(\Gamma[\sqrt{-3}])$ is an example.
Case 4. We conjecture that there is lift
$$S_{a+2}^{-}\left(\Gamma_{0}(9)\right) \rightarrow S_{b, a+3, b}(\Gamma[\sqrt{-3}])$$
with $\mathfrak{S}_{4}$-representation $\mathbf{s}_{3,1}$
An example is the form $F_{9,2}$ of Finis [18, p. 151] found in $S_{0,6,0}(\Gamma[\sqrt{-3}])$.
Case 5. We conjecture that there is a lift
$$S_{a+2}^{\chi}\left(\Gamma_{0}(9)\right) \rightarrow S_{b, a+3, b}(\Gamma[\sqrt{-3}])$$
with $\mathfrak{S}_{4}$-representation $\mathbf{s}_{2,2}$.
The first example is the lift from $S_{5}^{\chi}\left(\Gamma_{0}(9)\right)$ to $S_{3,6,0}(\Gamma[\sqrt{-3}])$ described in [9, p. 50].
11.4. Genuine Picard modular forms. We conjecture that the space $S_{n(\lambda)}(\Gamma[\sqrt{-3}])$ decomposes into a Hecke-invariant direct sum of a subspace generated by all the lifts described in Section 11.2 and 11.3 and a subspace $S_{n(\lambda)}^{\text {gen }}(\Gamma[\sqrt{-3}])$ which we call the space of genuine Picard modular forms.
11.5. Three-dimensional lifts. As above, the Hecke eigenvalue of $T(p)$ for an elliptic eigenform $f$ of weight $k$ will be denoted by $a_{p}(f)$. In the cohomology of our local systems we see examples of 3-dimensional pieces of the form $\operatorname{Sym}^{2}\left(M_{f}\right)$, with $M_{f}$ the motive associated to the elliptic eigenform, and with Hecke eigenvalue for $T(\nu)$ equal to $a_{p}(f)^{2}-p^{k-1}$.

We list these (conjectural) examples of lifts, which should be eigenforms in $S_{n(\lambda)}^{\text {gen }}(\Gamma[\sqrt{-3}])$, without formulating more general conjectures.
\begin{itemize}
\item[-] The eigenform $f \in S_{5}^{\chi}\left(\Gamma_{0}(9)\right)$ lifts to an eigenform in $S_{3,6,2}(\Gamma[\sqrt{-3}])$ with $\mathfrak{S}_{4}$-representation $\mathbf{s}_{2,1^{2}}+\mathbf{s}_{1^{4}}$.
\item[-] The eigenform $f \in S_{6}\left(\Gamma_{0}(3)\right)$ lifts to an eigenform in $S_{4,7,2}(\Gamma[\sqrt{-3}])$ with $\mathfrak{S}_{4}$-representation $\mathbf{s}_{3,1}$.
\item[-] The eigenform $f \in S_{7}^{\chi}\left(\Gamma_{0}(9)\right)$ lifts to an eigenform in $S_{5,8,2}(\Gamma[\sqrt{-3}])$ with $\mathfrak{S}_{4}$-representation $\mathbf{s}_{14}$.
\item[-] The eigenform $f \in S_{8}^{-}\left(\Gamma_{0}(9)\right)$ lifts to an eigenform in $S_{6,9,2}(\Gamma[\sqrt{-3}])$ with $\mathfrak{S}_{4}$-representation $\mathbf{s}_{4}$.
\item[-] The eigenform $f \in S_{9}^{-}\left(\Gamma_{1}(3)\right)$ lifts to an eigenform in $S_{7,10,2}(\Gamma[\sqrt{-3}])$ with $\mathfrak{S}_{4}$-representation $\mathbf{s}_{4}$.
\end{itemize}

\section*{12. Conjectures on the cohomology of local systems}

Recall the notation from Section 10.3. We will consider the normalized motivic (in the sense of Definition 7.6) Euler characteristic with compact support
$$e_{c}(\lambda):=e_{c}^{\text {norm }}\left(\mathcal{X}_{\Gamma[\sqrt{-3}]}, \mathbb{W}_{\lambda}\right)$$
and the inner variant of this $e_{!}(\lambda)$. Define also $e_{c, \mu}(\lambda)$ as in Section 7.2. Put also $E_{c}(\lambda):=E_{c}\left(X_{\Gamma[\sqrt{-3}]}, \mathbb{W}_{\lambda}\right)$, see Section 9 .

Put $\lambda^{\prime}=(b-i,-i,-a-i)$, so $\left(\lambda^{\prime}\right)^{\prime}=\lambda$, and note by Proposition 7.2 that we have a duality
$$e_{c}\left(\lambda^{\prime}\right)=\overline{e_{c}(\lambda)} .$$
12.1. The main conjecture. In this section we formulate the main conjectures of the article. First we present a series of definitions of different contributions to the cohomology.

The contributions making up the extraneous contribution $e_{\text {extr }}(\lambda)$, see Definition 12.8, will consist of Hecke characters $\mathbb{L}^{i, j}$, see Section 7.1, and motives from elliptic modular forms. Namely, to all the spaces of elliptic modular forms $S_{k}\left(\Gamma_{0}(1)\right), S_{k}^{\text {new }}\left(\Gamma_{0}(3)\right), S_{k}^{ \pm}\left(\Gamma_{1}(3)\right), S_{k}^{ \pm}\left(\Gamma_{0}(9)\right)$ and $S_{k}^{\chi}\left(\Gamma_{0}(9)\right)$ introduced in Section 11.1 we have corresponding motives (of twice their dimension) $S\left[\Gamma_{0}(1), k\right], S^{\text {new }}\left[\Gamma_{0}(3), k\right], S_{k}^{ \pm}\left[\Gamma_{1}(3), k\right], S^{ \pm}\left[\Gamma_{0}(9), k\right]$ and $S^{\chi}\left[\Gamma_{0}(9), k\right]$ with the property that for any prime $p$ the trace of the Hecke operator $T(p)$ on the space of modular forms equals the trace of Frobenius $F_{\nu}$ on the corresponding motive.

Definition 12.1. We define the $\mathfrak{S}_{4}$-representations
$$\alpha_{j}=\left\{\begin{array}{ll}
\mathbf{s}_{4} & j \equiv_{6} 0 \\
\mathbf{s}_{14} & j \equiv_{6} 3 \\
0 & \text { else }
\end{array} \quad \text { and } \quad \beta_{j}= \begin{cases}\mathbf{s}_{3,1} & j \equiv_{6} 0 \\
\mathbf{s}_{2,1^{2}} & j \equiv_{6} 3 \\
0 & \text { else. }\end{cases}\right.$$
and we define $\delta_{j}$ to be 1 if $j \equiv_{6} 0$ and 0 else.
Proposition 3.9 gives a formula for the (normalized) Eisenstein cohomology $e_{\text {Eis }}(\lambda)=e_{c}(\lambda)-e_{!}(\lambda)$ for all regular $\lambda$. Proposition 3.9 is only formulated in Betti cohomology, but Harder's result is actually motivic in the sense of Section 7.2. We generalize the formula in the following definition.
Definition 12.2. We define $e_{\text {Eis }}^{\prime}(\lambda)$ as
$$\begin{aligned}
-\left(\alpha_{i}+\beta_{i}\right) \mathbb{L}^{0,0}+\left(\alpha_{i-b-1}\right. & \left.+\beta_{i-b-1}\right) \mathbb{L}^{b+1,0}+\left(\alpha_{i+a+1}+\beta_{i+a+1}\right) \mathbb{L}^{0, a+1} \\
& - \begin{cases}\alpha_{i-1}(\mathbb{L}+1) \mathbb{L}^{b+1,0} & \text { if } a=0 \text { and } b \equiv_{2} 0 \\
\alpha_{i+1}(\mathbb{L}+1) \mathbb{L}^{0, a+1} & \text { if } b=0 \text { and } a \equiv_{2} 0\end{cases}
\end{aligned}$$

All the following contributions should be found in $e_{!}(\lambda)$. Note that the Hodge degrees of all these contributions, for a regular local system, are either $(a+b+2,0),(b+1, a+1)$ or $(0, a+b+2)$, as they need to be, see Section 3.2. Note also that the sign is always positive, which it should be for regular local systems since in that case only the second inner cohomology group can be non-zero, see Section 3.2.

Definition 12.3. We define the central endoscopic term $e_{\mathrm{ce}}(\lambda)$ as
$$\begin{array}{r}
\alpha_{i}\left(s_{a+b+3}\left(\Gamma_{0}(1)\right)+s_{a+b+3}^{-}\left(\Gamma_{1}(3)\right)\right) \mathbb{L}^{b+1, a+1} \\
+\beta_{i}\left(s_{a+b+3}\left(\Gamma_{0}(1)\right)+s_{a+b+3}^{\text {new }}\left(\Gamma_{0}(3)\right)+s_{a+b+3}^{+}\left(\Gamma_{1}(3)\right)\right) \mathbb{L}^{b+1, a+1} \\
+\beta_{i+3} s_{a+b+3}^{+}\left(\Gamma_{0}(9)\right) \mathbb{L}^{b+1, a+1}+\left(\delta_{i}+\delta_{i+3}\right) s[2,2] s_{a+b+3}^{\chi}\left(\Gamma_{0}(9)\right) \mathbb{L}^{b+1, a+1} \\
+\alpha_{i} \mathbb{L}^{b+1, a+1} \text { if }(a, b) \equiv_{6}(5,5) .
\end{array}$$

The following two contributions are connected to the lifted (holomorphic) forms in $S_{b, a+3, i+2}\left(\Gamma_{1}[\sqrt{-3}]\right)$ described in the conjectures of Section 11.
Definition 12.4. (holomorphic 1-dimensional lifts) We define $e_{1 \ell}(\lambda)$ as
$$\alpha_{i+a+4} s_{b+2}^{-}\left(\Gamma_{0}(9)\right) \mathbb{L}^{a+b+2,0}+ \begin{cases}\alpha_{i+3} \mathbb{L}^{a+b+2,0} & \text { if }(a, b) \equiv_{6}(5,2) \\ \alpha_{i+4} \mathbb{L}^{a+2,0} & \text { if } a \equiv_{6} 3 \text { and } b=0\end{cases}$$

Definition 12.5. (holomorphic 2-dimensional lifts) We define $e_{2 \ell}(\lambda)$ as
$$\begin{array}{r}
\alpha_{i+3} S^{-}\left[\Gamma_{0}(9), a+b+3\right] \\
+\alpha_{i-b-1}\left(S\left[\Gamma_{0}(1), a+2\right]+S^{-}\left[\Gamma_{1}(3), a+2\right]\right) \mathbb{L}^{b+1,0} \\
\beta_{i-b-1}\left(S\left[\Gamma_{0}(1), a+2\right]+S^{\mathrm{new}}\left[\Gamma_{0}(3), a+2\right]+S^{-}\left[\Gamma_{1}(3), a+2\right]\right) \mathbb{L}^{b+1,0} \\
+\beta_{i-b+2} S^{-}\left[\Gamma_{0}(9), a+2\right] \mathbb{L}^{b+1,0} \\
+\left(\delta_{i-b-1}+\delta_{i-b+2}\right) s[2,2] S^{\chi}\left[\Gamma_{0}(9), a+2\right] \mathbb{L}^{b+1,0} .
\end{array}$$

Let $\bar{S}_{j, k, l}(\Gamma[\sqrt{-3}])$ be isomorphic as a vector space to $\bar{S}_{j, k, l}(\Gamma[\sqrt{-3}])$ but such that the Hecke operator $T(\nu)$ acts on $\bar{S}_{j, k, l}(\Gamma[\sqrt{-3}])$ as $T(\bar{\nu})$ acts on $S_{j, k, l}(\Gamma[\sqrt{-3}])$. The following two contributions (i.e. Definition 12.6 and Definition 12.7) are connected to the lifted anti-holomorphic forms. In other words connected to the lifted (holomorphic) forms in $\bar{S}_{a, b+3,-i-1}(\Gamma[\sqrt{-3}])$ except for the contribution of the form $\alpha_{i+3} S^{-}\left[\Gamma_{0}(9), a+b+3\right]$. Compare this with Proposition 7.2.

Definition 12.6. (anti-holomorphic 1-dimensional lifts) We define $e_{\overline{1 \ell}}(\lambda)$ as
$$\alpha_{i-b+2} s_{a+2}^{-}\left(\Gamma_{0}(9)\right) \mathbb{L}^{0, a+b+2}+ \begin{cases}\alpha_{i+3} \mathbb{L}^{0, a+b+2} & \text { if }(a, b) \equiv_{6}(2,5) \\ \alpha_{i-2} \mathbb{L}^{0, b+2} & \text { if } a=0 \text { and } b \equiv_{6} 3 .\end{cases}$$

Definition 12.7. (anti-holomorphic 2-dimensional lifts) We define $e_{\overline{2 \ell}}(\lambda)$ as
$$\begin{array}{r}
\alpha_{i+a+1}\left(S\left[\Gamma_{0}(1), b+2\right]+S^{-}\left[\Gamma_{1}(3), b+2\right]\right) \mathbb{L}^{0, a+1} \\
+\beta_{i+a+1}\left(s\left[\Gamma_{0}(1), b+2\right]+S^{\mathrm{new}}\left[\Gamma_{0}(3), b+2\right]+S^{-}\left[\Gamma_{1}(3), b+2\right]\right) \mathbb{L}^{0, a+1} \\
+\beta_{i+a+4} S^{-}\left[\Gamma_{0}(9), b+2\right] \mathbb{L}^{0, a+1} \\
+\left(\delta_{i+a+1}+\delta_{i+a+4}\right) s[2,2] S^{\chi}\left[\Gamma_{1}(9), b+2\right] \mathbb{L}^{0, a+1} .
\end{array}$$

Definition 12.8. We put
$$e_{\mathrm{extr}}(\lambda)=e_{\mathrm{Eis}}^{\prime}(\lambda)+e_{\mathrm{ce}}(\lambda)+e_{1 \ell}(\lambda)+e_{2 \ell}(\lambda)+e_{\overline{1 \ell}}(\lambda)+e_{\overline{2 \ell}}(\lambda)$$
and we define $e_{\text {extr }, \mu}(\lambda)$ as in Section 7.2.
Main Conjecture 12.9. We conjecture that for any $\lambda \neq(0,0,0), \nu$ and $\mu$, if $i \equiv_{2} a+b$ then,
$$\operatorname{Tr}\left(T(\nu), S_{n(\lambda)}^{\text {gen }}(\Gamma[\sqrt{-3}])^{\mu}\right)=\operatorname{Tr}\left(F_{\nu}, e_{c, \mu}(\lambda)-e_{\text {extr }, \mu}(\lambda)\right) .$$

Assuming that the conjecture is true, this gives a possibility to compute the trace of the Hecke operators $T(\nu)$ by counts of points over $\mathbb{F}_{p}$ as described in Section 8.

Remark 12.10. Note that $e_{\text {extr }}\left(\lambda^{\prime}\right)=\overline{e_{\text {extr }}(\lambda)}$.
The main conjecture then implies that there is a Hecke-invariant isomorphism between $S_{j, k+3, l}^{\text {gen }}\left(\Gamma[\sqrt{-3})^{\mu}\right.$ and $\bar{S}_{k, j+3,1-l}^{\text {gen }}\left(\Gamma[\sqrt{-3})^{\mu}\right.$. Note that in general
$$\operatorname{dim} S_{j, k+3, l}(\Gamma[\sqrt{-3}]) \neq \operatorname{dim} S_{k, j+3,1-l}(\Gamma[\sqrt{-3}]) .$$
According to Theorem 4.7 the difference of dimensions is equal to

\begin{tabular}[t]{|l|l|l|l|}
\hline & $l \equiv_{3} 0$ & $l \equiv_{3} 1$ & $l \equiv_{3} 2$ \\
\hline $j \equiv_{3} 0$ & $k-1$ & $1-j$ & 0 \\
\hline $j \equiv_{3} 1$ & $1-j$ & $k-1$ & 0 \\
\hline $j \equiv_{3} 2$ & 0 & 0 & $k-j$ \\
\hline
\end{tabular}
which is a consequence of the presence lifts.

Definition 12.11. We define $E_{\text {extr }}(\lambda)$ as $e_{\text {extr }}(\lambda)$ but replacing
\begin{itemize}
\item[] $\star \mathbb{L}^{i, j}$ by 1 for any $i, j$
\item[] ★ $S\left[\Gamma_{0}(1), k\right], S^{\text {new }}\left[\Gamma_{0}(3), k\right], S^{ \pm}\left[\Gamma_{1}(3), k\right], S^{ \pm}\left[\Gamma_{0}(9), k\right], S^{\chi}\left[\Gamma_{0}(9), k\right]$ respectively by $2 \operatorname{dim} S_{k}\left(\Gamma_{0}(1)\right), 2 \operatorname{dim} S_{k}^{\text {new }}\left(\Gamma_{0}(3)\right), 2 \operatorname{dim} S_{k}^{ \pm}\left(\Gamma_{1}(3)\right)$, $2 \operatorname{dim} S_{k}^{ \pm}\left(\Gamma_{0}(9)\right), 2 \operatorname{dim} S_{k}^{\chi}\left(\Gamma_{0}(9)\right)$ for any $k$,
\end{itemize}
in the formulas of Definition 12.2 until Definition 12.7. This gives an element in the Galois group of representations of $\mathfrak{S}_{4}$.

Conjecture 12.12. We conjecture that for any $\lambda$,
$$\operatorname{dim}_{\mathfrak{S}_{4}} S_{n(\lambda)}^{\text {gen }}(\Gamma[\sqrt{-3}])=\frac{1}{3}\left(E_{c}(\lambda)-E_{\text {extr }}(\lambda)\right) .$$
12.2. A congruence modulo 9. Our experimental data lead us to conjecture a congruence for the eigenvalues of Hecke operators.

Conjecture 12.13. For any $j, k, l \geq 0, \nu$ and $\mu \vdash 4$ we conjecture that
$$\operatorname{Tr}\left(T(\nu), S_{j, k+3, l}^{\text {gen }}(\Gamma[\sqrt{-3}])^{\mu}\right) \equiv_{9} 3 \operatorname{dim} S_{j, k+3, l}^{\text {gen }}(\Gamma[\sqrt{-3}])^{\mu} .$$

Remark 12.14. If one uses the evidence of the results in [9] one might also conjecture that for a prime $p \equiv 2(\bmod 3)$ the trace on the space of genuine forms is divisible by 9.

For the lifted forms described in Section 11.5 this means that for a prime $p \equiv_{3} 1$ the congruence
$$a_{p}(f)^{2}-p^{k-1} \equiv_{9} 3$$
should hold and similarly a congruence $a_{p}(f)^{2}-p^{k-1} \equiv_{9} 0$ for primes $p \equiv_{3} 2$.
12.3. Evidence. The conjectures of this section and the previous were based upon the computations described in Section 10.1. Here we list a series of regularities in this data that lends credence to the conjectures.

The following holds for all $\lambda$ such that $a+b+2 \leq 40$.
\begin{itemize}
\item[-] The integer
$$E_{c}(\lambda)-E_{\text {extr }}(\lambda)$$
is divisible by 3.
\item[] ★ We find, using Theorem 4.7, that $\operatorname{dim} S_{n(\lambda)}\left(\Gamma_{1}[\sqrt{-3}]\right)$ equals
$$\frac{1}{3}\left(E_{c}(\lambda)-E_{\text {extr }}(\lambda)\right),$$
when replacing $\mathbf{s}_{\mu}$ with $\operatorname{dim} \mathbf{s}_{\mu}$, and adding the dimension of the lifts described in Section 11.
\item[-] If
$$E_{c}(\lambda)-E_{\text {extr }}(\lambda)=0$$
then
$$\operatorname{Tr}\left(F_{q}, e_{c}(\lambda)-e_{\text {extr }}(\lambda)\right)=0,$$
for $q \leq 67$ and $q \equiv_{3} 1$.
\end{itemize}
\begin{itemize}
\item[-] We have that (compare with Conjecture 12.13)
$$\operatorname{Tr}\left(F_{q}, e_{c}(\lambda)-e_{\text {extr }}(\lambda)\right) \equiv_{9} E_{c}(\lambda)-E_{\text {extr }}(\lambda),$$
for $q \leq 67$ and $q \equiv_{3} 1$.
\item[-] All traces computed (for $j=0$ ) in [18] match with the ones computed using Conjecture 12.9 for $p \leq 67$ and $p \equiv_{3} 1$.
\item[-] The ring of scalar valued modular forms, i.e. when $j=0$, is given in Proposition 2.2. This gives a formula for $\operatorname{dim} S_{0, k+3, l}^{\text {gen }}(\Gamma[\sqrt{-3}])^{\mu}$ for any $k, l, \mu$, which matches the one given by Conjecture 12.12 (for $a+b+2 \leq 40$ ). For instance we have that
$$S_{0,6 k+3,2}(\Gamma[\sqrt{-3}])=M_{0,6 k-9,0}(\Gamma[\sqrt{-3}]) \zeta^{2}$$
and
$$\operatorname{dim}_{\mathfrak{S}_{4}} S_{0,6 k+3,2}(\Gamma[\sqrt{-3}])=\operatorname{Sym}^{2 k-3}\left(\mathbf{s}_{2,1^{2}}\right)$$
for $k \geq 2$.
\item[-] All traces computed in [9] match with the ones computed using Conjecture 12.9 for $p \leq 67$ and $p \equiv_{3} 1$.
\end{itemize}

Note that the information
$$\operatorname{Tr}\left(F_{q^{r}}, e_{c}(\lambda)-e_{\text {extr }}(\lambda)\right),$$
for $r=1, \ldots,\left(E_{c}(\lambda)-E_{\text {extr }}(\lambda)\right)$ gives a way to compute the characteristic polynomial of $F_{q}$ acting on $e_{c}(\lambda)-e_{\text {extr }}(\lambda)$, assuming that it is effective of dimension $E_{c}(\lambda)-E_{\text {extr }}(\lambda)$.

For all $\lambda$ such that $a+b+2 \leq 40$ and $E_{c}(\lambda)-E_{\text {extr }}(\lambda)=3$, see further in Section 13.2, the characteristic polynomial for $q=4$ and the partial information for $q=7$ has the expected structure (namely the one derived from the results of Section 2.3).

See also Section 14 for evidence coming from congruences studied by Harder.
12.4. Modules of vector-valued forms. Define
$$\mathcal{M}_{j}=\mathcal{M}_{j}^{0} \oplus \mathcal{M}_{j}^{1} \oplus \mathcal{M}_{j}^{2}$$
with
$$\mathcal{M}_{j}^{\ell}=\oplus_{k} M_{j, k, l}(\Gamma[\sqrt{-3}]) .$$
Then $\mathcal{M}_{j}$ is a module over $\mathcal{M}_{0}$; for $\mathcal{M}_{0}$ see Proposition 2.2. Guided by the heuristics of our conjectures the structure of some modules $\mathcal{M}_{j}$ was determined in [9], e.g. for $j=1,2,3$. For example, the module $\mathcal{M}_{1}^{0}$ is generated over $\mathcal{M}_{0}^{0}$ by three forms $\Phi_{0}, \Phi_{1}, \Phi_{2} \in S_{1,7,0}\left(\Gamma_{1}[\sqrt{-3}]\right)$ satisfying a relation $\varphi_{0} \Phi_{0}+\varphi_{1} \Phi_{1}+\varphi_{2} \Phi_{2}=0$ with $\varphi_{0}, \varphi_{1}, \varphi_{2}$ generators of the ring $\mathcal{M}_{0}^{0}$. For a table of Hecke eigenvalues of the $\Phi_{i}$ we refer to [9, Table 7].
12.5. Conjecture for the moduli space of genus 2 curves. In this section we will be brief and give a similar conjecture to the one above but in the case of genus 2.

Define the normalized compactly supported Euler characteristic $e_{c}^{\text {norm }}$ analogously to Definition 7.6. Recall the notation from Section 8.2.1 and define the representation,
$$\alpha_{k}=\left\{\begin{array}{ll}
\mathbf{s}_{2} \tilde{\mathbf{s}}_{2} & k \equiv_{2} 0 \\
\mathbf{s}_{1,1} \tilde{\mathbf{s}}_{2} & k \equiv_{2} 1
\end{array} \quad \text { and } \quad \beta_{k}= \begin{cases}\mathbf{s}_{1,1} \tilde{\mathbf{s}}_{1,1} & k \equiv_{2} 0 \\
\mathbf{s}_{2} \tilde{\mathbf{s}}_{1,1} & k \equiv_{2} 1\end{cases}\right.$$

Let $W_{3}$ denote the Fricke operator and for any prime $p$ let $T(p)$ be the Hecke operator. For the proofs of the following properties of $W_{3}$, see [2].

If $k>0$ is even, and $f \in S_{k+2}\left(\Gamma_{1}(3)\right)$ is an eigenform with $T(p) f=$ $a_{p} f$ then $a_{p}=\bar{a}_{p}$ for all primes $p$. Moreover, $a_{3}= \pm 3^{k / 2}$ and $W_{3}(f)=$ $-\operatorname{sgn}\left(a_{3}\right) f$. The ±-spaces of $W_{3}$ are clearly Hecke invariant and we denote the ±-eigenspaces of $S_{k+2}\left(\Gamma_{1}(3)\right)$ by $S_{k+2}^{ \pm}\left(\Gamma_{1}(3)\right)$. Define $S^{ \pm}\left[\Gamma_{1}(3), k+2\right]$ analogously.

If $k$ is odd, then $S_{k+2}\left(\Gamma_{1}(3)\right)=S_{k+2}\left(\Gamma_{0}(3), \chi\right)$, where $\chi$ is the Dirichlet character of order 2. If $f \in S_{k+2}\left(\Gamma_{0}(3), \chi\right)$ is an eigenform with $T(p) f=a_{p} f$, then $\bar{a}_{p}=\chi(p) a_{p}$ for all $p \nmid 3$ and $W_{3}(f)=c \bar{f}$ for some $c \in \mathbb{C}$ with $|c|=1$, and $W_{3}^{2}(f)=-f$. If $f \neq \bar{f}$ then $\pm i \bar{c} f+\bar{f}$ is an eigenvector for $W_{3}$ with eigenvalue $\mp i$. If $p \equiv_{3} 1$ then both these are also eigenvectors of $T(p)$ with eigenvalue $a_{p}$. For $k \equiv_{3} 2$ then there is an eigenvector $f \in S_{k+2}\left(\Gamma_{0}(3), \chi\right)$ such that $a_{3}=(-3)^{(k+1) / 2}, W_{3}(f)=(-1)^{(k+1) / 2} i f$ and
$$a_{p}(f)=\operatorname{Tr}\left(F_{p}, \mathbb{L}^{k+1,0}+\mathbb{L}^{0, k+1}\right) .$$
We denote the $\pm i$-eigenspaces of $S_{k+2}\left(\Gamma_{1}(3)\right)$ by $S_{k+2}^{ \pm}\left(\Gamma_{1}(3)\right)$, and we define $S^{ \pm}\left[\Gamma_{1}(3), k+2\right]$ analogously.
Conjecture 12.15. For any $k>0, l \geq 0$ such that $k \equiv_{6} l$,
$$\begin{gathered}
e_{c}^{\text {norm }}\left(\mathcal{X}_{\Gamma[\sqrt{-3}]}^{(2)}, \mathbb{W}_{k, l}\right)=-\alpha_{k}-\beta_{k}-S^{+}\left[\Gamma_{1}(3), k+2\right] \alpha_{k}-S^{-}\left[\Gamma_{1}(3), k+2\right] \beta_{k} \\
+\delta_{k+1}\left(\mathbb{L}^{k+1,0} \alpha_{k}+\mathbb{L}^{0, k+1} \beta_{k}\right)+\delta_{k+7}\left(\mathbb{L}^{0, k+1} \alpha_{k}+\mathbb{L}^{k+1,0} \beta_{k}\right)
\end{gathered}$$
as elements of $K_{0}^{\mathfrak{S}_{2} \times \mathfrak{S}_{2}}\left(\mathrm{Gal}_{F}\right)$, and where $\delta_{i}=1$ if $i \equiv_{12} 0$ and 0 otherwise.
For $k=0$, put $S^{+}\left[\Gamma_{1}(3), 2\right]=-\mathbb{L}-1$ and $S^{-}\left[\Gamma_{1}(3), 2\right]=0$ to make the formula correct, by Proposition 8.3. Looking at how $\mathfrak{S}_{2} \times \mathfrak{S}_{2}$ acts on the two cusps of the Bailey-Borel compactification we find that the Eisenstein contribution to $e_{c}^{\text {norm }}\left(\mathcal{X}_{\Gamma[\sqrt{-3}]}^{(2)}, \mathbb{W}_{k, l}\right)$, for $k \equiv_{6} l$, is equal to $-\alpha_{k}-\beta_{k}$ (compare the proof of Proposition 3.9).

\section*{13. Examples}

We now illustrate our conjectures and calculations by examples.
13.1. Explicit examples. Let us study a series of local systems in some detail.
13.1.1. $\lambda=(10,4,4)$. In the cohomology of this local system we expect to find contributions from the forms in $S_{0,9,0}\left(\Gamma_{1}[\sqrt{-3}]\right)$.

From the formula described in Section 7 we get the numerical Euler characteristic,
$$E_{c}\left(X_{\Gamma[\sqrt{-3}]}, \mathbb{W}_{\lambda}\right)=\mathbf{s}_{4}+2 \mathbf{s}_{3,1}+3 \mathbf{s}_{2,1^{2}}+\mathbf{s}_{1^{4}} .$$

Following Section 12.1 the only non-zero contributions we have to $e_{\text {extr }}(\lambda)$ are
$$\begin{gathered}
e_{\mathrm{Eis}}^{\prime}(\lambda)=\mathbb{L}^{1,0}\left(\mathbf{s}_{2,1^{2}}+\mathbf{s}_{1^{4}}\right), \\
e_{\overline{1} \ell}(\lambda)=\mathbb{L}^{0,8} \mathbf{s}_{4}
\end{gathered}$$
and
$$e_{2 \ell}(\lambda)=S^{-}\left[\Gamma_{0}(9), 8\right] \mathbb{L}^{1,0} \mathbf{s}_{3,1}+S^{\text {new }}\left[\Gamma_{0}(3), 8\right] \mathbb{L}^{1,0} \mathbf{s}_{2,1^{2}} .$$
In $e_{2 \ell}(\lambda)$, the $\mathbf{s}_{3,1}$-term comes from the Kudla lift denoted $F_{9,1}=\varphi_{0} \varphi_{1}\left(\varphi_{0}-\right.$ $\varphi_{1}$ ) and the $\mathbf{s}_{2,1^{2}}$-term comes from the Kudla lift of weight 9 denoted $F_{9,2}$ by Finis ([18, Tables p. 151 and 177]).

Removing the extraneous contributions should leave us with contributions from the genuine Picard modular cusp forms. Starting with the numerical Euler characteristic we get
$$E_{c}\left(X_{\Gamma[\sqrt{-3}]}, \mathbb{W}_{\lambda}\right)-E_{\operatorname{extr}}\left(X_{\Gamma[\sqrt{-3}]}, \mathbb{W}_{\lambda}\right)=0,$$
so there should be no genuine forms. And indeed we find that
$$\operatorname{Tr}\left(F_{\nu}, e_{c}(\lambda)\right)-\operatorname{Tr}\left(F_{\nu}, e_{\text {extr }}(\lambda)\right)$$
which conjecturally equals
$$\operatorname{Tr}\left(T(\nu), S_{0,9,0}^{\text {gen }}(\Gamma[\sqrt{-3}])\right)$$
is 0 for all $p \leq 67$.
This also fits (adding the lifts) with the formula
$$\operatorname{dim}_{\mathfrak{S}_{4}} S_{0,9,0}(\Gamma[\sqrt{-3}])=\mathbf{s}_{3,1}+\mathbf{s}_{2,1^{2}}$$
that we find by Proposition 2.2.
13.1.2. $\lambda=(16,4,4)$. In the cohomology of this local system we expect to find contributions from the forms in $S_{0,15,0}(\Gamma[\sqrt{-3}])$.

Again, from the formula in Section 7 we get,
$$E_{c}\left(X_{\Gamma[\sqrt{-3}]}, \mathbb{W}_{\lambda}\right)=\mathbf{s}_{4}+5 \mathbf{s}_{3,1}+3 \mathbf{s}_{2^{2}}+7 \mathbf{s}_{2,1^{2}}+\mathbf{s}_{1^{4}} .$$

Similarly to the previous case, following Section 12.1, we find that $e_{\text {extr }}(\lambda)$ consists of
$$\begin{gathered}
e_{\mathrm{Eis}}^{\prime}(\lambda)=\mathbb{L}^{1,0}\left(\mathbf{s}_{2,1^{2}}+\mathbf{s}_{1^{4}}\right), \\
e_{\bar{\ell} \bar{\ell}}(\lambda)=\mathbb{L}^{0,14} \mathbf{s}_{4}
\end{gathered}$$
and
$$e_{2 \ell}(\lambda)=S^{-}\left[\Gamma_{0}(9), 14\right] \mathbb{L}^{1,0} \mathbf{s}_{3,1}+S^{\mathrm{new}}\left[\Gamma_{0}(3), 14\right] \mathbb{L}^{1,0} \mathbf{s}_{2,1^{2}} .$$

Removing the extraneous contributions should leave us with contributions from the genuine Picard modular cusp forms. Starting with the numerical Euler characteristic we get
$$E_{c}\left(X_{\Gamma[\sqrt{-3}]}, \mathbb{W}_{\lambda}\right)-E_{\operatorname{extr}}\left(X_{\Gamma[\sqrt{-3}]}, \mathbb{W}_{\lambda}\right)=3 \mathbf{s}_{3,1}+3 \mathbf{s}_{2^{2}} .$$

Dividing this expression by 3 gives the conjectural result
$$\operatorname{dim}_{\mathfrak{S}_{4}} S_{0,15,0}^{\text {gen }}(\Gamma[\sqrt{-3}])=\mathbf{s}_{3,1}+\mathbf{s}_{2^{2}} .$$
Together with the lifts we get
$$\operatorname{dim}_{\mathfrak{S}_{4}} S_{0,15,0}(\Gamma[\sqrt{-3}])=2 \mathbf{s}_{3,1}+\mathbf{s}_{2^{2}}+3 \mathbf{s}_{2,1^{2}},$$
which fits with the formula we find by Proposition 2.2.
We can then compute
$$\operatorname{Tr}\left(F_{\nu}, e_{c}(\lambda)\right)-\operatorname{Tr}\left(F_{\nu}, e_{\text {extr }}(\lambda)\right)$$
which conjecturally equals,
$$\operatorname{Tr}\left(T(\nu), S_{0,15,0}^{\text {gen }}(\Gamma[\sqrt{-3}])\right) .$$

For the two 1-dimensional isotypic components of the space of genuine forms we then (conjecturally) get Hecke eigenvalues, and a few of them are given in the following table. Note that the analogue of the Ramanujan conjecture for this situation holds; $N\left(\xi_{\nu}\right) \leq 3 N(\nu)^{a+b+2}$ for eigenvalues $\xi_{\nu}$. Similar observations can be made for the other tables appearing in this section.

\begin{table}
\begin{tabular}[t]{|l|l|l|}
\hline $p$ & $S_{0,15,0}^{\text {gen }}(\Gamma[\sqrt{-3}])^{\left(2^{2}\right)}$ & $S_{0,15,0}^{\text {gen }}(\Gamma[\sqrt{-3}])^{(3,1)}$ \\
\hline 7 & $-388107 \rho-1608891$ & $-524625-205857 \rho$ \\
\hline 13 & $-60967989 \rho-9061701$ & $-36504663+20888505 \rho$ \\
\hline 19 & $-578216997 \rho-665720736$ & $-398615136-1035916731 \rho$ \\
\hline 31 & $-690422256 \rho-8829510909$ & $32032766937+14052080592 \rho$ \\
\hline 37 & $-111679368147 \rho-59483009571$ & $30023590017-12661429743 \rho$ \\
\hline 43 & $-98981609184 \rho+131622854187$ & $298590045213+634311769248 \rho$ \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{13.1.3. $\lambda=(32,2,2)$. In the cohomology of this local system we expect to find contributions from the forms in $S_{0,33,1}(\Gamma[\sqrt{-3}])$.}
\end{table}

Again, from the formula in Section 7 we get,
$$E_{c}\left(X_{\Gamma[\sqrt{-3}]}, \mathbb{W}_{\lambda}\right)=9 \mathbf{s}_{4}+27 \mathbf{s}_{3,1}+9 \mathbf{s}_{2^{2}}+19 \mathbf{s}_{2,1^{2}}+2 \mathbf{s}_{1^{4}} .$$

Following Section 12.1 we find that that $e_{\text {extr }}(\lambda)$ only consists of
$$e_{\mathrm{Eis}}^{\prime}(\lambda)=\mathbb{L}^{0,31} \mathbf{s}_{2,1^{2}}-\mathbb{L}^{1,32} \mathbf{s}_{1^{4}} .$$

Removing this contribution from the Euler characteristic and dividing by 3, as in the previous example, we get the following conjecture,
$$\operatorname{dim}_{\mathfrak{S}_{4}} S_{0,33,1}^{\text {gen }}(\Gamma[\sqrt{-3}])=3 \mathbf{s}_{4}+9 \mathbf{s}_{3,1}+3 \mathbf{s}_{2^{2}}+6 \mathbf{s}_{2,1^{2}}+\mathbf{s}_{1^{4}} .$$
Since there are no lifts, this is the same as the dimensions of all cusp forms and it equals the formula $\mathbf{s}_{1^{4}} \operatorname{Sym}^{9}\left(\mathbf{s}_{2,1^{2}}\right)$, found using Proposition 2.2.

Some (conjectural) Hecke eigenvalues for the 1-dimensional isotypic component of the space of genuine forms corresponding to $\mathbf{s}_{1^{4}}$ are given in the following table.

\begin{tabular}[t]{|l|l|}
\hline $p$ & $S_{0,33,1}^{\text {gen }}(\Gamma[\sqrt{-3}])^{\left(1^{4}\right)}$ \\
\hline 7 & $-17187741337239 \rho-27371045932368$ \\
\hline 13 & $619757358250752891 \rho-73897512261622296$ \\
\hline 19 & $32397975717682438611 \rho+161109729684241303755$ \\
\hline 31 & $-450614269323285049766016 \rho+463109207345192219515905$ \\
\hline 37 & $4464950074069806168802623 \rho-679365937587169490840376$ \\
\hline 43 & $-62575475768038597846807512 \rho-83275045472246397000970011$ \\
\hline
\end{tabular}
13.1.4. $\lambda=(7,1,-2)$. In the cohomology of this local system we expect to find contributions from the forms in $S_{3,9,0}\left(\Gamma_{1}[\sqrt{-3}]\right)$. Note that the modular forms occuring here are described in [9, Prop. 15.2].

From the formula described in Section 7 we get
$$E_{c}\left(X_{\Gamma[\sqrt{-3}]}, \mathbb{W}_{\lambda}\right)=\mathbf{s}_{4}+5 \mathbf{s}_{3,1}+6 \mathbf{s}_{2^{2}}+9 \mathbf{s}_{2,1^{2}}+4 \mathbf{s}_{1^{4}} .$$

From Proposition 3.9 and Section 12.1 we get
$$e_{\mathrm{Eis}}^{\prime}(\lambda)=e_{\mathrm{Eis}}(\lambda)=\mathbb{L}^{4,0}\left(\mathbf{s}_{2,1^{2}}+\mathbf{s}_{1^{4}}\right) .$$
The only other non-zero contributions we have to $e_{\text {extr }}(\lambda)$ are
$$e_{\overline{1 \ell}}(\lambda)=\mathbb{L}^{0,11} \mathbf{s}_{4}$$
and
$$e_{2 \ell}(\lambda)=S^{-}\left[\Gamma_{0}(9), 8\right] \mathbb{L}^{4,0} \mathbf{s}_{3,1}+S^{\mathrm{new}}\left[\Gamma_{0}(3), 8\right] \mathbb{L}^{4,0} \mathbf{s}_{2,1^{2}} .$$

Again, removing the extraneous contributions from the Euler characteristic and dividing by 3, we get the following conjecture,
$$\operatorname{dim}_{\mathfrak{S}_{4}} S_{3,9,0}^{\text {gen }}(\Gamma[\sqrt{-3}])=\mathbf{s}_{3,1}+2 \mathbf{s}_{2^{2}}+2 \mathbf{s}_{2,1^{2}}+\mathbf{s}_{1^{4}} .$$
Together with the lifts we get the conjecture,
$$\operatorname{dim}_{\mathfrak{S}_{4}} S_{3,9,0}(\Gamma[\sqrt{-3}])=2 \mathbf{s}_{3,1}+2 \mathbf{s}_{2^{2}}+3 \mathbf{s}_{2,1^{2}}+\mathbf{s}_{1^{4}} .$$
This conjectural expression fits with that Theorem 4.7 tells us, namely that,
$$\operatorname{dim} S_{3,9,0}(\Gamma[\sqrt{-3}])=20 .$$

For the two 1-dimensional isotypic components of the space of genuine forms we then (conjecturally) get Hecke eigenvalues, and a few of them are given in the following table.

\begin{tabular}[t]{|l|l|l|}
\hline $p$ & $S_{3,9,0}^{\text {gen }}(\Gamma[\sqrt{-3}])^{(3,1)}$ & $S_{3,9,0}^{\text {gen }}(\Gamma[\sqrt{-3}])^{\left(1^{4}\right)}$ \\
\hline 7 & $-2661-3735 \rho$ & $-39273-37755 \rho$ \\
\hline 13 & $697611-853785 \rho$ & $-616209-1939509 \rho$ \\
\hline 19 & $-4019046-4493727 \rho$ & $2924922+16469397 \rho$ \\
\hline 31 & $236296587+26549946 \rho$ & $-13532361-40067046 \rho$ \\
\hline 37 & $381974925-151949367 \rho$ & $-294789795-270210663 \rho$ \\
\hline 43 & 685398387 + $28100862 \rho$ & $1093524015+1099688094 \rho$ \\
\hline
\end{tabular}
13.1.5. $\lambda=(11,5,2)$. In the cohomology of this local system we expect to find contributions from the forms in $S_{3,9,1}(\Gamma[\sqrt{-3}])$.

Again, from the formula in Section 7 we get,
$$E_{c}\left(X_{\Gamma[\sqrt{-3}]}, \mathbb{W}_{\lambda}\right)=4 \mathbf{s}_{4}+7 \mathbf{s}_{3,1}+5 \mathbf{s}_{2^{2}}+6 \mathbf{s}_{2,1^{2}}+3 \mathbf{s}_{1^{4}} .$$

From Proposition 3.9 and Section 12.1 we get that the only non-zero contribution we have to $e_{\text {extr }}(\lambda)$ are
$$e_{\mathrm{Eis}}^{\prime}(\lambda)=e_{\mathrm{Eis}}(\lambda)=\mathbb{L}^{0,7}\left(\mathbf{s}_{4}+\mathbf{s}_{3,1}\right) .$$
and
$$e_{\overline{2 \ell}}(\lambda)=\mathbb{L}^{0,7} S^{\chi}\left[\Gamma_{0}(9), 5\right] \mathbf{s}_{2,2} .$$

Removing this contribution from the Euler characteristic and dividing by 3, as in the previous example, we get the following conjecture,
$$\operatorname{dim}_{\mathfrak{S}_{4}} S_{3,9,1}^{\text {gen }}(\Gamma[\sqrt{-3}])=\mathbf{s}_{4}+2 \mathbf{s}_{3,1}+\mathbf{s}_{2^{2}}+2 \mathbf{s}_{2,1^{2}}+\mathbf{s}_{1^{4}} .$$
This is the same as the dimensions of all cusp forms since there are no lifts which fits with the result
$$\operatorname{dim} S_{3,9,1}(\Gamma[\sqrt{-3}])=16,$$
following from Theorem 4.7.
Using the same method as above, we compute some (conjectural) Hecke eigenvalues for two of the 1-dimensional spaces in the following table. Note that the eigenform in $S_{3,9,1}^{\text {gen }}(\Gamma[\sqrt{-3}])^{\left(1^{4}\right)}$ equals $\left(E_{0}+E_{2}+E_{2}-E_{3}\right) \zeta$, with $E_{i}$ the Eisenstein series given in [9, Lemma 15.1].

\begin{tabular}[t]{|l|l|l|}
\hline $p$ & $S_{3,9,1}^{\text {gen }}(\Gamma[\sqrt{-3}])^{(2,2)}$ & $S_{3,9,1}^{\text {gen }}(\Gamma[\sqrt{-3}])^{\left(1^{4}\right)}$ \\
\hline 7 & $-39753 \rho-15702$ & $-3303 \rho-20562$ \\
\hline 13 & $-2259729 \rho-462012$ & $39537 \rho-662244$ \\
\hline 19 & $-813897 \rho-7616175$ & $-12094443 \rho-15482085$ \\
\hline 31 & $62423118 \rho+189603705$ & $13979610 \rho-2791545$ \\
\hline 37 & $154008855 \rho-213937620$ & $-132007005 \rho-420798660$ \\
\hline 43 & $-1091048814 \rho-311480763$ & $-1442196450 \rho-484155105$ \\
\hline
\end{tabular}
13.1.6. $\lambda=(9,3,0)$. In the cohomology of this local system we expect to find contributions from the forms in $S_{3,9,2}(\Gamma[\sqrt{-3}])$.

Once again, using the formula in Section 7 we get,
$$E_{c}\left(X_{\Gamma[\sqrt{-3}]}, \mathbb{W}_{\lambda}\right)=2 \mathbf{s}_{4}+7 \mathbf{s}_{3,1}+3 \mathbf{s}_{2^{2}}+4 \mathbf{s}_{2,1^{2}} .$$

From Proposition 3.9 and Section 12.1 we get the non-zero contributions to $e_{\text {extr }}(\lambda)$ as
$$\begin{gathered}
e_{\mathrm{Eis}}^{\prime}(\lambda)=e_{\mathrm{Eis}}(\lambda)=-\mathbb{L}^{0,0}\left(\mathbf{s}_{2,1^{2}}+\mathbf{s}_{1^{4}}\right), \\
e_{\mathrm{ce}}(\lambda)=\mathbb{L}^{4,7}\left(\mathbf{s}_{3,1}+2 \mathbf{s}_{2,1^{2}}+\mathbf{s}_{1^{4}}\right),
\end{gathered}$$
and
$$e_{2 \ell}(\lambda)=S^{-}\left[\Gamma_{0}(9), 12\right] \mathbf{s}_{4} .$$

As in the previous examples, we use the numerical Euler characteristic to get the following conjecture,
$$\operatorname{dim}_{\mathfrak{S}_{4}} S_{3,9,2}^{\text {gen }}(\Gamma[\sqrt{-3}])=2 \mathbf{s}_{3,1}+\mathbf{s}_{2^{2}}+\mathbf{s}_{2,1^{2}} .$$
Together with the 1-dimensional space of lifts above we get
$$\operatorname{dim} S_{3,9,2}(\Gamma[\sqrt{-3}])=12,$$
which fits with Theorem 4.7.
Some (conjectural) Hecke eigenvalues for the 1-dimensional spaces are found in the following table.

\begin{tabular}[t]{|l|l|l|}
\hline $p$ & $S_{3,9,2}^{\text {gen }}(\Gamma[\sqrt{-3}])^{(2,2)}$ & $S_{3,9,2}^{\text {gen }}(\Gamma[\sqrt{-3}])^{\left(2,1^{2}\right)}$ \\
\hline 7 & $-522 \rho-771$ & $-42405-73422 \rho$ \\
\hline 13 & $64731-1053828 \rho$ & $2150805+1144836 \rho$ \\
\hline 19 & $9397530 \rho+10858953$ & $1117083-2630970 \rho$ \\
\hline 31 & $-199487250 \rho-223012887$ & $17764311-9145350 \rho$ \\
\hline 37 & $-283226796 \rho-170478933$ & $144010695+424906308 \rho$ \\
\hline 43 & $456864210 \rho-855993435$ & $-365663985-1035862434 \rho$ \\
\hline
\end{tabular}
13.1.7. $\lambda=(11,0,-5)$. In the cohomology of this local system we expect to find contributions from the forms in $S_{5,14,2}(\Gamma[\sqrt{-3}])$.

Using the formula in Section 7 we get,
$$E_{c}\left(X_{\Gamma[\sqrt{-3}]}, \mathbb{W}_{\lambda}\right)=9 \mathbf{s}_{4}+27 \mathbf{s}_{3,1}+18 \mathbf{s}_{2^{2}}+27 \mathbf{s}_{2,1^{2}}+9 \mathbf{s}_{1^{4}} .$$

From Proposition 3.9 and Section 12.1 we get the non-zero contributions to $e_{\text {extr }}(\lambda)$ as
$$\begin{gathered}
e_{\text {Eis }}^{\prime}(\lambda)=e_{\text {Eis }}(\lambda)=\left(-\mathbb{L}^{0,0}+\mathbb{L}^{6,0}+\mathbb{L}^{0,12}\right)\left(\mathbf{s}_{4}+\mathbf{s}_{3,1}\right), \\
e_{\mathrm{ce}}(\lambda)=3 \mathbb{L}^{6,12}\left(\mathbf{s}_{4}+\mathbf{s}_{3,1}+\mathbf{s}_{2,2}\right) . \\
e_{\overline{2 \ell}}(\lambda)=\mathbb{L}^{0,12} S^{\chi}\left[\Gamma_{1}(9), 7\right] \mathbf{s}_{2^{2}} .
\end{gathered}$$
and
$$e_{2 \ell}(\lambda)=\mathbb{L}^{6,0} S^{-}\left[\Gamma_{1}(3), 13\right]\left(\mathbf{s}_{4}+\mathbf{s}_{3,1}\right)+\mathbb{L}^{6,0} S^{\chi}\left[\Gamma_{1}(9), 13\right] \mathbf{s}_{2^{2}} .$$

As in the previous examples, we use the numerical Euler characteristic to get the following conjecture,
$$\operatorname{dim}_{\mathfrak{S}_{4}} S_{5,14,2}^{\text {gen }}(\Gamma[\sqrt{-3}])=\mathbf{s}_{4}+7 \mathbf{s}_{3,1}+3 \mathbf{s}_{2^{2}}+9 \mathbf{s}_{2,1^{2}}+3 \mathbf{s}_{1^{4}} .$$
Together with the 2-dimensional space of lifts above we get
$$\operatorname{dim} S_{5,14,2}(\Gamma[\sqrt{-3}])=66,$$
which fits with Theorem 4.7.
Some (conjectural) Hecke eigenvalues for the 1-dimensional space of genuine cusp forms are found in the following table.

\begin{table}
\begin{tabular}[t]{|l|l|}
\hline $p$ & $S_{5,14,2}^{\text {gen }}(\Gamma[\sqrt{-3}])^{(4)}$ \\
\hline 7 & $-38516760 \rho-13589673$ \\
\hline 13 & $-6017408280 \rho-7487727117$ \\
\hline 19 & $546522935760 \rho+368972351247$ \\
\hline 31 & $20336092789320 \rho+55796255768703$ \\
\hline 37 & $-147394045113480 \rho+55302806453187$ \\
\hline 43 & $134094712536720 \rho-23648747132697$ \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{13.2. One-dimensional spaces of genuine forms. The cases for which
$$\operatorname{dim} S_{j, k, l}^{\text {gen }}\left(\Gamma_{1}[\sqrt{-3}]\right)^{\mu}=1$$
are of special importance to us since in these cases counts of points over finite fields gives (using Conjecture 12.9) Hecke eigenvalues rather than just traces.}
\end{table}

For $\mu=(4)$ we found 78 such cases using Conjecture 12.12. We list all such $(j, k, l)$ below, but because of Remark 12.10 we only list them up to duality.

\begin{table}
\captionsetup{labelformat=empty}
\caption{13.2. One-dimensional spaces of genuine forms. The cases for which
$$\operatorname{dim} S_{j, k, l}^{\text {gen }}\left(\Gamma_{1}[\sqrt{-3}]\right)^{\mu}=1$$
are of special importance to us since in these cases counts of points over finite fields gives (using Conjecture 12.9) Hecke eigenvalues rather than just traces.}
\begin{tabular}[t]{|l|l|l|l|l|l|l|}
\hline (0, 15, 1) & (0, 21, 1) & (0, 24, 1) & (0, 27, 0) & (0, 30, 1) & (0, 30, 2) & (0, 33, 0) \\
\hline (0, 36, 0) & (0, 36, 2) & (0, 39, 2) & (0, 42, 0) & (0, 45, 2) & (1, 16, 0) & (1, 19, 0) \\
\hline (1, 19, 1) & (1, 19, 2) & (1, 22, 1) & (1,25,1) & (1, 28, 2) & (2, 11, 0) & (2, 11, 1) \\
\hline (2, 14, 0) & (2, 14, 1) & (2, 20, 2) & (2, 23, 2) & (3, 9, 1) & (3, 12, 0) & (3, 12, 1) \\
\hline (3, 15, 0) & (3, 18, 2) & (4, 7, 0) & (4, 10, 0) & (4, 10, 2) & (4,13,2) & (5, 8, 0) \\
\hline (5, 11, 2) & (5, 14, 2) & (6, 9, 0) & (6, 9, 2) & (7, 10, 2) & & \\
\hline
\end{tabular}
\end{table}

For $\mu=(3,1),\left(2^{2}\right),\left(2,1^{2}\right),\left(1^{4}\right)$ we found 35, 44, 35, 76 cases respectively.

\section*{14. Congruences of Harder type}

According to Harder a prime appearing in the denominator of a critical value of an $L$-function sometimes leads to a congruence between modular forms, see [24]. The shape of these congruences was discussed by Harder after we found instances of congruences, see [25] and see also Dummigan's discussion in [14].

In the case at hand we look at the standard $L$-function associated to an algebraic Hecke character $\psi_{m}$ with the following Euler factors. For a prime $p \equiv_{3} 1$ with $p=\nu_{p} \bar{\nu}_{p}$ and $\nu_{p} \equiv \bar{\nu}_{p} \equiv_{3} 1$ we have
$$L_{p}\left(\psi_{m}, s\right)=1 /\left(1-\nu_{p}^{m} p^{-s}\right)\left(1-\bar{\nu}_{p}^{m} p^{-s}\right)$$
and for a prime $p \equiv_{3} 2$ we have
$$L_{p}\left(\psi_{m}, s\right)=1 /\left(1-(-p)^{m} p^{-s}\right),$$
while for $p=3$ we have $L_{3}\left(\psi_{m}, s\right)=1$ unless $m \equiv_{6} 0$ and then $L_{3}\left(\psi_{m}, s\right)=$ $1 /\left(1-(\sqrt{-3})^{m} 3^{-s}\right)$. The completed $L$-function
$$\Lambda\left(\psi_{m}, s\right)=\frac{\Gamma(s)}{(2 \pi)^{s}} \prod L_{p}\left(\psi_{m}, s\right)$$
extends to a holomorphic function of $s$ and satisfies a functional equation relating $s$ with $m+1-s$. According to (an analogue of) a result of Hurwitz we get rational quotients of critical values
$$Q(m, n):=\frac{\Lambda\left(\psi_{m}, n-1\right)}{\Lambda\left(\psi_{m}, n\right)} \in \mathbb{Q} \quad \text { for } n=m, m-1, \ldots,\left[\frac{m+1}{2}\right] .$$

Conjecture 14.1. (Harder's conjecture) If a prime $\ell>m$ divides the denominator of $Q(m, n)$ there exists a Picard modular cusp form of weight $(b, a+3)=(m-n, 2 n-m+1)$, which is an eigenform of the Hecke algebra, such that its Hecke eigenvalues $\lambda_{\nu_{p}}$ for $p \equiv_{3} 1$ satisfy the congruence
$$\lambda_{\nu_{p}} \equiv \ell \bar{\nu}_{p}^{a+b+2}+\left(p^{a+1}+1\right) \nu_{p}^{b+1} .$$

We found the following cases where the data available to us are in accordance with this conjecture. If the index of the local system $\mathbb{W}_{\lambda}$ is $\lambda=(a+i, i,-b+i)$, we list the weight $(j, k, l)=(b, a+3, i+2)$ of the modular forms, the representation of $\mathfrak{S}_{4}$, the index $(m, n)=(a+2 b+3, a+b+3)$, the congruence prime $\ell$ and the value of $Q(m, n)$.

\begin{tabular}[t]{|l|l|l|l|l|}
\hline $j, k, l$ & $\mu$ & $(m, n)$ & $\ell$ & $Q(m, n)$ \\
\hline 2, 11, 2 & $\left(1^{4}\right)$ & $(15,13)$ & 53 & $2^{4} / 3 \cdot 53$ \\
\hline 1, 13, 1 & $\left(1^{4}\right)$ & $(15,14)$ & 19 & $53 / 2 \cdot 5 \cdot 19$ \\
\hline 1, 13, 1 & $\left(2,1^{2}\right)$ & $(15,13)$ & 19 & $53 / 2 \cdot 5 \cdot 19$ \\
\hline 6, 9, 0 & $\left(1^{4}\right)$ & $(21,15)$ & 271 & 233/2 • 5 • 271 \\
\hline 3, 12, 0 & (4) & $(18,15)$ & 29 & 3 • 5/2 • 29 \\
\hline 5, 11, 2 & $\left(1^{4}\right)$ & $(21,16)$ & 17 & 271/2 • 3 • 11 • 17 \\
\hline 2, 20, 2 & (4) & $(24,22)$ & 97 & $11 \cdot 457 / 2^{2} \cdot 3 \cdot 5^{2} \cdot 97$ \\
\hline 1, 22, 1 & (4) & $(24,23)$ & 41 & $23 \cdot 97 / 2 \cdot 3 \cdot 5 \cdot 11 \cdot 41$ \\
\hline 0, 27, 0 & $\left(1^{4}\right)$ & $(27,27)$ & 449 & $3^{2} \cdot 179 \cdot 223 / 2^{2} \cdot 11 \cdot 17 \cdot 23 \cdot 449$ \\
\hline 0, 33, 0 & $\left(1^{4}\right)$ & $(33,33)$ & 17093 & $19 \cdot 84802789 / 2^{2} \cdot 5 \cdot 11 \cdot 17 \cdot 23 \cdot 29 \cdot 17093$ \\
\hline
\end{tabular}
The Hecke eigenvalues in two of these cases are found in the following table.

\begin{tabular}[t]{|l|l|l|}
\hline $p$ & $S_{2,11,2}^{\text {gen }}(\Gamma[\sqrt{-3}])^{\left(1^{4}\right)}$ & $S_{6,9,0}^{\text {gen }}(\Gamma[\sqrt{-3}])^{\left(1^{4}\right)}$ \\
\hline 7 & $113760 \rho+180273$ & $-742581 \rho-967245$ \\
\hline 13 & $6574680 \rho+4136763$ & $-11444355 \rho+37295661$ \\
\hline 19 & $-3105720 \rho+22527309$ & $-1411116471 \rho-1183781976$ \\
\hline 31 & $1128613680 \rho-206255175$ & $2162847960 \rho+20439895125$ \\
\hline 37 & $-1059546600 \rho-631344705$ & $113910723225 \rho+29288724825$ \\
\hline 43 & $-3998935080 \rho-6398875995$ & $-55912815000 \rho-92116884255$ \\
\hline
\end{tabular}

In fact, we searched for congruences in our heuristic data (for the cases where the space $S_{j, k, l}^{\text {gen }}(\Gamma[\sqrt{-3}])^{\mu}$ has dimension 1) and then checked the value of the corresponding quotient of critical $L$-values. In all cases except one the congruence prime showed up in $Q(m, n)$. The one extra congruence not explained by the above conjecture occurs for the local system $\mathbb{W}_{\lambda}$ with $\lambda=(16,1,1)$ and $\mu=(3,1)$. We found a congruence modulo $\ell=37$. But the corresponding $Q(18,18)=3 \cdot 7 \cdot 19 / 2 \cdot 5 \cdot 11 \cdot 17$ does not show 37. Harder thinks that this congruence might be due to the second factor $c(\phi, 0)$ in [22, page 590]. We list some eigenvalues for the case $\lambda=(16,1,1)$.

\begin{tabular}[t]{|l|l|}
\hline $p$ & $S_{0,18,0}(\Gamma[\sqrt{-3}])^{(3,1)}$ \\
\hline 7 & $-37133403-19436265 \rho$ \\
\hline 13 & $-114953793-826184565 \rho$ \\
\hline 19 & $82348187646+48917648907 \rho$ \\
\hline 31 & $2339550247917-489600934794 \rho$ \\
\hline 37 & $6061060465185+27008238932829 \rho$ \\
\hline 43 & $-13426382809671-41363330321286 \rho$ \\
\hline
\end{tabular}
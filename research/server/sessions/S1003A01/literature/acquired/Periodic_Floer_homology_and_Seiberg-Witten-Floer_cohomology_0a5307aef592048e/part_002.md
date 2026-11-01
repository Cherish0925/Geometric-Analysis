---
retention_scope: session
part: 2
total_parts: 4
---

[Part 2/4 of: Periodic Floer homology and Seiberg-Witten-Floer cohomology]

This lemma is proved in Section 2.4.
Define a vector field, $\partial_{t^{\prime}}$, on $M$ as follows:
$$\partial_{t^{\prime}}= \begin{cases}\left(\varphi_{\gamma}\right)_{*} \mathrm{v}_{\gamma} & \text { over the image of } \varphi_{\gamma}, \text { for all } \gamma \in \Lambda_{N}, \\ \partial_{t} & \text { otherwise. }\end{cases}$$
This vector field $\partial_{t^{\prime}}$ is the desired modification of $\partial_{t}$.
Part 2. The set of almost complex structures $\mathcal{J}_{0 f}$. In this and the next part, we digress to describe the criteria for membership in the subset $\mathcal{J}_{1 f}$ of the set of almost complex structures on $\mathbb{R} \times M$. The criteria are of two sorts. The first sort is a standard genericity condition: It requires that all irreducible, pseudoholomorphic subvarieties be non-degenerate in the sense that a certain associated Fredholm operator has trivial cokernel. To say more, suppose that $C \subset \mathbb{R} \times M$ is an irreducible, pseudoholomorphic subvariety. There
exists a model curve for $C$, denoted $C_{0}$. This is a smooth, complex curve with a smooth, pseudoholomorphic map
$$\varphi_{0}: C_{0} \rightarrow M,$$
which is 1-1 on the complement of a finite set, onto $C$. The subvariety $C$ is said to be immersed when $\varphi_{0}$ is an immersion.

The operator in question has a relatively straightforward description in the case when $C$ is immersed. Supposing that such is the case, then a normal bundle $\mathrm{N} \rightarrow C_{0}$ is defined so that it restricts to any open set $U \subset C_{0}$ that is embedded by $\varphi_{0}$ as the pull-back via $\varphi_{0}$ of the normal bundle of $\varphi_{0}(U) \subset C$ in $\mathbb{R} \times M$. The almost complex structure $J$ endows N with the structure of a complex line bundle. This said, view N henceforth as a complex line bundle. Then there exists on $C_{0}$ a canonical, $\mathbb{R}$-linear Fredholm operator that maps sections over $C_{0}$ of N to those of $\mathrm{N} \otimes T^{0,1} C_{0}$. This operator is denoted as $\mathcal{D}_{C}$. Its action on a section $\eta$ of N can be written as
$$\mathcal{D}_{C} \eta=\bar{\partial} \eta+\nu_{C} \eta+\mu_{C} \bar{\eta},$$
where the notation is as follows: Fix a Hermitian metric on N so as to give the latter a holomorphic structure; this is used to define $\bar{\partial}$. Meanwhile, $\nu_{C}$ and $\mu_{C}$ are respective sections of $T^{0,1} C_{0}$ and $\mathrm{N}^{\otimes 2} \otimes T^{0,1} C_{0}$ that are defined using the one-jet along $C$ of $J$. Note that a change of Hermitian metric is compensated by a change in what is meant by $\nu_{C}$. This is why (2.4) is canonical. The operator $\mathcal{D}_{C}$ arises in the following way: Fix $\varepsilon>$ 0 and let $\eta$ denote a section of N . The composition of first $\varepsilon \eta$ and then the metrics exponential map defines a deformation of the subvariety $C$. This deformation is pseudoholomorphic to first order in $\varepsilon$ if and only if $\mathcal{D}_{C} \eta=0$. The assumption that all periodic orbits are non-degenerate implies that $\mathcal{D}_{C}$ maps $L_{1}^{2}\left(C_{0} ; \mathrm{N}\right)$ to $L^{2}\left(C_{0} ; \mathrm{N} \otimes T^{0,1} C_{0}\right)$ as a Fredholm operator. The kernel of $\mathcal{D}_{C}$ is used here to denote the space of sections in $L_{1}^{2}\left(C_{0} ; \mathrm{N}\right)$ that are annihilated by $\mathcal{D}_{C}$. The cokernel of $\mathcal{D}_{C}$ is used here to denote its $L^{2}\left(C_{0} ; \mathrm{N}^{\otimes 2} \otimes T^{0,1} C_{0}\right)$ cokernel. This is the kernel of the formal adjoint. Note also that the kernel and cokernel elements are smooth. In any event, the index of $\mathcal{D}_{C}$ denotes its index as a Fredholm operator from $L_{1}^{2}\left(C_{0} ; \mathrm{N}\right)$ to $L^{2}\left(C_{0} ; \mathrm{N} \otimes T^{0,1} C_{0}\right)$. This Fredholm version of $\mathcal{D}_{C}$ is the Fredholm operator that was alluded to at the outset. There is an analogous Fredholm version of $\mathcal{D}_{C}$ in the case when $\varphi_{0}$ is not an immersion; it is described for example in Section 4 of [HT1].

The interest in these operators stems from the following fact: The set of irreducible, pseudoholomorphic subvarieties has a topology whereby a neighborhood of any given such subvariety $C$ is homeomorphic to the zero locus of a smooth map from a ball in $\operatorname{Ker}\left(\mathcal{D}_{C}\right)$ to $\operatorname{Coker}\left(\mathcal{D}_{C}\right)$.

A by-now standard argument using the Smale-Sard theorem can be used to prove the following:

Lemma 2.3. There is a residual subset $\mathcal{J}_{0 f} \subset \mathcal{J}_{f}$ of almost complex structures with the following property: If $J \in \mathcal{J}_{0 f}$, and if $C$ is an irreducible, $J$-pseudoholomorphic subvariety, then $\mathcal{D}_{C}$ has trivial cokernel.

In terms of this, the first criterion for $J$ to be in $\mathcal{J}_{1 f}$ is:
$$[\mathrm{J} 1]: J \in \mathcal{J}_{0 f} .$$
Part 3. The set of almost complex structures $\mathcal{J}_{1 f}$. This part describes the second sort of criteria for membership in $\mathcal{J}_{1 f}$. Assume that $J \in \mathcal{J}_{0 f}$. The criteria here involve the ends of pseudoholomorphic subvarieties that comprise the set $\mathcal{M}_{1}\left(\Theta, \Theta^{\prime}\right)$ for pairs $\Theta, \Theta^{\prime}$ in the set $\mathcal{A}$. To say more, suppose that $\Sigma \in \mathcal{M}_{1}\left(\Theta, \Theta^{\prime}\right)$. The fact that $\Sigma$ is in a one-dimensional moduli space implies that there is a unique $(C, m) \in \Sigma$ with such that the submanifold $C$ not $\mathbb{R}$-invariant. Let $\mathcal{E} \subset C$ denote an end. Reintroduce the notation $q_{\mathcal{E}}, \lambda_{q_{\mathcal{E}}}$, and $\varsigma_{q_{\mathcal{E}}}$ from the discussion of (1.7); and define a subset $\operatorname{div}_{\mathcal{E}} \subset\left\{1, \ldots, q_{\mathcal{E}}\right\}$ as follows: An integer $q$ is in $\operatorname{div}_{\mathcal{E}}$ if either of the following is true:
\begin{itemize}
\item[(1)] $q=q_{\mathcal{E}}$,
\item[(2)] $q$ is a proper divisor of $q_{\mathcal{E}}$, and there is a $(2 \pi q)$-periodic eigenfunction $\varsigma_{q}$ of the operator in (1.8) with eigenvalue $\lambda_{q}$ of the same sign as $\lambda_{q_{E}}$, such that $\left|\lambda_{q_{E}}\right|>\left|\lambda_{q}\right|>0$.
\end{itemize}
Note that the sign in item (2) above is positive or negative, respectively, when $\mathcal{E}$ is a positive or negative end. We now state the other criteria for $J$ to be in $\mathcal{J}_{1 f}$ :

For any choice of $\Theta, \Theta^{\prime}, \Sigma, C$ described above,
[J2a]: $\operatorname{div}_{\mathcal{E}}=\left\{q_{\mathcal{E}}\right\}$ for any end $\mathcal{E}$ of $C$.
[J2b]: Fix any two distinct ends of $C, \mathcal{E}$ and $\mathcal{E}^{\prime}$, which are both positive or both negative such that their respective constant $s \in \mathbb{R}$ slices converge as $|s| \rightarrow \infty$ to the same periodic orbit in $M$, and such that $q_{\mathcal{E}}=q_{\mathcal{E}^{\prime}}=: q$. Fix respective $2 \pi q$-periodic eigenfunctions $s_{q_{\mathcal{E}}}$, $\varsigma_{q_{\mathcal{E}^{\prime}}}$ for the $\mathcal{E}$ and $\mathcal{E}^{\prime}$ 's versions of the operator (1.8). Then $\varsigma_{q_{E}}(t) \neq$ $\varsigma_{q_{E^{\prime}}}(t+2 \pi k)$ for any integer $k$.

Definition 2.2. $\mathcal{J}_{1 f}$ is the set of almost complex structures $J$ satisfying all three conditions [J1], [J2a], [J2b] above.

The arguments in Sections 3 and 4 of [HT1] can be adapted with only notational changes to prove that the set $\mathcal{J}_{1 f}$ is a residual subset of $\mathcal{J}_{0 f}$. By way of a parenthetical remark with regards to [J2a], Section 3 in [HT1] shows that $\lambda_{q_{E}}$ is the smallest positive/largest negative eigenvalue of a $2 \pi q_{\mathcal{E}^{-}}$periodic eigenfunction. Moreover, the condition that $\Sigma$ have periodic Floer homology index 1 implies the following: Let $q$ denote a proper divisor of $q_{E}$,
and let $\lambda$ denote the eigenvalue of a $2 \pi q$-periodic eigenfunction with the sign as $\lambda_{q_{E}}$. Then $|\lambda|>\left|\lambda_{q_{E}}\right|$.
Part 4. The modified almost complex structure $J^{\prime}$ The next lemma describes a modified version of the given almost complex structure, $J$; this is to go with the modified version of $f$ provided by Lemma 2.1 and the modified version of $\partial_{t}$ provided by Lemma 2.2.

Lemma 2.4. Given an integer N, there exists $\kappa>1$ with the following significance: Fix $\delta<\kappa^{-1}$ and let $f^{\prime}$ denote a map given by Lemma 2.1. Define $\partial_{t^{\prime}}$ from $f^{\prime}$ as done subsequent to Lemma 2.2. Then there is an almost complex structure, $J^{\prime}$, on $T(\mathbb{R} \times M)$ with the properties listed below:
\begin{itemize}
\item[-] $J^{\prime} \partial_{s}=\partial_{t^{\prime}}$.
\item[-] $J^{\prime}$ is tamed by $d s \wedge d t+w_{f}$.
\item[-] Fix $\gamma \in \Lambda_{N}$ and extend Lemma 2.2's map $\varphi_{\gamma}$ as a map
$$\hat{\varphi}_{\gamma}: \mathbb{R} \times\left(S^{1} \times D\right) \rightarrow \mathbb{R} \times M, \quad(\sigma,(\tau, z)) \mapsto\left(s=q \sigma, \varphi_{\gamma}(\tau, z)\right) .$$
Then $J^{\prime}\left(\hat{\varphi}_{\gamma}\right)_{*} \partial_{z}=\left(\hat{\varphi}_{\gamma}\right)_{*} \mathrm{i} \partial_{z}$ on a neighborhood of the $z=0$ locus.
\item[-] $J^{\prime} \in \mathcal{J}_{1 f^{\prime}}$.
\item[-] For any pair of periodic Floer homology generators, there is a canonical 1-1 correspondence between the $J$-pseudoholomorphic curves that contribute to the periodic Floer homology differential and those that are $J^{\prime}$-pseudoholomorphic. This correspondence is such that partnered curves contribute identical ±1 weights to the respective differentials.
\end{itemize}

This lemma is proved in Section 2.4.
With $N$ given and a choice of $\delta$ obeying the conditions of Lemmas 2.1-2.4, fix $f^{\prime}$ as in Lemma 2.1 and $J^{\prime}$ as in Lemma 2.4. The pair $\left(f^{\prime}, J^{\prime}\right)$ is said to be an $(\delta, N)$-approximation to $(f, J)$. The following is a direct corollary of Lemmas 2.1 and 2.4:

Proposition 2.1. Fix a pair $(f, J)$ with $f: F \rightarrow F$ satisfying (1.1) and $J \in \mathcal{J}_{1 f}$. Use the latter to define the chain complex and differential for periodic Floer homology. Then there exists an integer $N_{*} \geq 1$ such that $\forall N \geq N_{*}$, there exists an $\delta_{N} \in \mathbb{R}$ with the following significance:

Given any $\delta \in\left(0, \delta_{N}\right)$ and an $(\delta, N)$-approximation, $\left(f^{\prime}, J^{\prime}\right)$, to $(f, J)$, the tautological identification of the respective generators induces a canonical isomorphism from the f -version of the periodic Floer chain complex to the $f^{\prime}$-version, that intertwines the corresponding differentials. In particular, the two versions of periodic Floer homology are canonically isomorphic.

Remark. The definition of periodic Floer homology that was given originally in [H1] restricted the pair $(f, J)$ to those where $f$ obeys the fifth item of Lemma 2.1 and where $J$ near each $\gamma \in \Lambda_{N}$ version of $\mathbb{R} \times \gamma$ is constant when written in a suitable coordinate chart. This understood, Proposition 2.1 can
be viewed as the assertion that the periodic Floer homology for any pair $(f, J)$ can be computed using a pair of the sort described in [H1].
2.3. Preliminary constructions. The proofs of Lemmas 2.1-2.4 require some preliminary constructions which will be used in the definitions of $f^{\prime}$ and $\varphi_{\gamma}$. These are given in the subsequent two parts of this subsection.

Part 1. The tubular neighborhood maps $\varphi_{\gamma}$. Fix $\gamma \in \Lambda_{N}$. This first part describes a tubular neighborhood map for $\gamma$ that is shown in Section 2.4 to satisfy the requirements of Lemma 2.2. In what follows, $q$ denotes the period of $\gamma$.

Let $z=\left(z_{1}, z_{2}\right)$ denote the symplectic coordinates centered on the corresponding fixed point p of $f$ as described in Lemma 2.1. Use these coordinates to identify a neighborhood of $\mathrm{p} \in F$ with a small radius disk $D^{\prime} \subset \mathbb{R}^{2}$ about the origin. This then gives a smooth map $\varphi_{0}:[0,2 \pi] \times D^{\prime} \rightarrow M$ that embeds $[0,2 \pi) \times D^{\prime}$ and is such that
$$\left(\varphi_{0}\right)_{*} \partial_{\tau}=\partial_{t} \quad \text { and } \quad \varphi_{0}(2 \pi, z)=\varphi_{0}\left(0, f^{q}(z)\right) .$$
The map $z \mapsto f^{q}(z)$ maps $D^{\prime}$ to $\mathbb{R}^{2}$ and fixes the origin. It also preserves the area-form $w_{F}$. This understood, there exists a homotopy of area-preserving maps,
$$\left\{\psi_{\tau}(z): D^{\prime \prime} \rightarrow \mathbb{R}^{2}\right\}_{\tau \in[0,2 \pi]},$$
where $D^{\prime \prime}$ is a disk $D^{\prime \prime} \subset D^{\prime}$, and $\psi_{\tau}$ is such that:
\begin{itemize}
\item[-] $\psi_{\tau}(0)=0$ for all $\tau$,
\item[-] $\psi_{\tau}(z)=z$ near $\tau=0$, and
\item[-] $\psi_{\tau}(z)=f^{-q}(z)$ near $\tau=2 \pi$.
\end{itemize}
Let $D^{*} \subset D^{\prime \prime}$ denote a small radius disk about the origin such that $D^{*}$ is in $\psi_{\tau}\left(D^{\prime \prime}\right)$ for all $\tau$. Define the map
$$\varphi_{1}:[0,2 \pi] \times D^{*} \rightarrow M, \quad(\tau, z) \mapsto \varphi_{0}\left(\tau, \psi_{\tau}(z)\right) .$$
By construction, $\varphi_{1}(0, z)=\varphi_{1}(2 \pi, z)$. As a consequence, $\varphi_{1}$ defines a map from $S^{1} \times D^{*}$ into $M$ such that $\varphi_{1}^{*} d t=q d \tau$.

By assumption, $J$ maps the kernel of $\pi_{*}$ to itself along $\gamma$. It is also the case that the quadratic form $w_{F}(\cdot, J(\cdot))$ is positive on the kernel of $\pi_{*}$ along $\gamma$. As a consequence, the action of $J$ along $\gamma$ on $\varphi_{1 *} \partial_{z}$ is such that
$$\left(\varphi_{1}^{-1}\right)_{*} J\left(\varphi_{1}\right)_{*} \partial_{z}=\mathrm{i}\left(1+|v|^{2}\right)^{1 / 2} \partial_{z}+v \partial_{\bar{z}},$$
where $v$ here is a smooth map from $S^{1}$ to $\mathbb{C}$. This understood, we may define:
Definition 2.3. Set $\varphi_{\gamma}: S^{1} \times D^{*} \rightarrow M$ to be the map that sends any given point $(\tau, z)$ to $\varphi_{1}\left(\tau, V_{\tau} z\right)$, where the map $\tau \mapsto V_{\tau}$, from $S^{1}$ to $\operatorname{Sl}(2 ; \mathbb{R})$ is chosen so that $\varphi_{\gamma}$ satisfies the following properties:
\begin{itemize}
\item[-] The vector field $q^{-1} \partial_{t}$ is the push-forward via $\varphi_{\gamma}$ of a vector field on $S^{1} \times D^{*}$ that can be written as
$$\partial_{\tau}-2 \mathrm{i}(\nu z+\mu \bar{z}+\mathfrak{r}) \partial_{z}+2 \mathrm{i}(\nu \bar{z}+\bar{\mu} z+\overline{\mathfrak{r}}) \partial_{\bar{z}},$$
where $\nu$ is an $\mathbb{R}$-valued function on $S^{1}$ and $\mu$ is a $\mathbb{C}$-valued function. Meanwhile $\mathfrak{r}$ is such that its absolute value is bounded by $\kappa|z|^{2}$, and its derivatives are bounded in absolute value by $\kappa|z|$ for a positive constant $\kappa$.
\item[-] $J\left(\varphi_{\gamma}\right)_{*} \partial_{z}=\left(\varphi_{\gamma}\right)_{*} \mathrm{i} \partial_{z}$ along $\gamma$.
\end{itemize}

In what follows, $F$ is identified with $\pi^{-1}(0) \subset M$ and $\varphi_{\gamma}$ is used to identify $\{2 \pi k / q\} \times D^{*} \subset S^{1} \times D^{*}$ with a disk in $F$, for any given $k \in\{0, \ldots, q\}$. Granted these identifications, then $\left(\varphi_{\gamma}\right)^{*} f$ on a small radius, concentric subdisk in the $\tau=2 \pi k / q$ disk inside $S^{1} \times D^{*}$ is obtained from (2.5) by following the integral curves of (2.5) from this subdisk to where they intersect the $\tau=2 \pi(k+1) / q$ disk in $S^{1} \times D^{*}$.
Part 2. The maps $u_{\tau}: D \subset F \rightarrow F$. This part constructs an $S^{1}$-parametrized family of area-preserving maps $\mathrm{u}_{\tau}$ from a certain disk in $F$ to $F$. This family is used to construct the map $f^{\prime}$.

To start, introduce $(\nu, \mu)$ to denote the pair of functions that arise when writing $q^{-1}\left(\varphi_{\gamma}^{-1}\right)_{*} \partial_{t}$ as in (2.5). There exists a one-parameter set, $\left\{\left(\nu^{\lambda}, \mu^{\lambda}\right)\right\}_{\lambda \in[0,1]}$, of respectively $\mathbb{R}$-valued and $\mathbb{C}$-valued functions on $S^{1}$ satisfying the following:
\begin{itemize}
\item[-] $\left(\nu^{0}, \mu^{0}\right)=\left(\nu_{\gamma}, \mu_{\gamma}\right)$, and $\left(\nu^{1}, \mu^{1}\right)=(\nu, \mu)$.
\item[-] Let $K^{\lambda} \in \operatorname{Sl}(2 ; \mathbb{R})$ be defined so that given $z \in \mathbb{R}^{2}, K^{\lambda} \cdot z$ is the value at $\tau=2 \pi$ of the solution to the equation
$$\frac{\mathrm{i}}{2} \frac{d}{d \tau} \eta+\nu^{\lambda} \eta+\mu^{\lambda} \bar{\eta}=0, \quad \eta(0)=z .$$
Then each $\lambda \in[0,1]$ version of $K^{\lambda}$ is conjugate in Sl ( $2 ; \mathbb{R}$ ) to $K_{\gamma}$.
\end{itemize}
Fix such a one-parameter family.
Reintroduce the function $\chi$ from Section 1.4. Fix $\rho_{0} \in\left(0, \delta^{16}\right)$ and set $\lambda^{*}$ to be the function on $\mathbb{R}^{2}$ given by $\lambda^{*}(z)=\chi\left(\ln |z| / \ln \rho_{0}\right)$. Introduce respective $\mathbb{R}$-valued and $\mathbb{C}$-valued functions on $S^{1} \times D$ given at $(\tau, z)$ by $\left(\nu^{\lambda^{*}}, \mu^{\lambda^{*}}\right)$. With these function in hand, set
$$\mathfrak{r}^{(1)}=\left(\nu^{\lambda^{*}}-\nu_{\gamma}\right) z+\left(\mu^{\lambda^{*}}-\mu_{\gamma}\right) \bar{z}+\lambda^{*} \mathfrak{r}+\mathfrak{e},$$
where $\mathfrak{r}$ also comes from (2.5), and where $\mathfrak{e}$ is a smooth map from $S^{1} \times D^{*}$ to $\mathbb{C}$ with the following properties:
\begin{itemize}
\item[-] $\mathfrak{e}$ is supported where $|z| \in\left(\rho_{0}^{7 / 16}, \rho_{0}^{5 / 16}\right)$.
\item[-] $\mathfrak{e}$ and its derivatives to order 100 are bounded by $\rho_{0}^{1000}$.
\end{itemize}

The term $\mathfrak{e}$ is used subsequently as a source of "suitably generic" perturbations.

Choose $\delta$ small enough so that the disk in $\mathbb{C}$ about the origin with radius $\delta$ lies in $D^{*}$. There exists a constant $c_{0}$ so that over the disk $D \subset D^{*}$ of radius $c_{0}^{-1} \delta_{*}$, the following family of maps $\left\{\mathrm{u}_{\tau}^{(1)}: D \rightarrow D^{*}\right\}_{\tau \in[0,2 \pi]}$ is well-defined: Given $z \in \mathbb{C}$, solve the differential equation
$$\frac{\mathrm{i}}{2} \frac{d}{d \tau} \eta+\nu_{\gamma} \eta+\mu_{\gamma} \bar{\eta}+\mathfrak{r}^{(1)}(\eta)=0, \quad \eta(0)=z,$$
and set
$$\mathbf{u}_{\tau}^{(1)}(z):=\eta(\tau) .$$
This map has the following three properties:
\begin{itemize}
\item[-] There is a disk $D^{(1)} \subset D$ centered at the origin of radius less than $\rho_{0}^{1 / 2}$ such that $\mathrm{u}_{\tau}^{(1)}$ acts on a neighborhood of $D^{(1)}$ as multiplication by the matrix $U(\tau)$ that is constructed in Section 2.1 from the solutions to the linear equation depicted in (2.3).
\item[-] There is a disk $D^{(2)} \subset D$ of radius less than $\rho_{0}^{1 / 4}$ that contains $D^{(1)}$ and is such that $\mathrm{u}_{\tau}^{(1)}$ acts on a neighborhood of $D-D^{(2)}$ as an areapreserving map. Furthermore, if $k \in\{0, \ldots, q-1\}$, then $\mathrm{u}_{\tau=2 \pi k / q}^{(1)}$ on $D-D^{(2)}$ is given by $\varphi_{\gamma}^{*} f$ on $\{2 \pi k / q\} \times\left(D-D^{(2)}\right)$.
\item[-] Each $\mathrm{u}_{\tau}^{(1)}$ is nearly area-preserving in the sense that its pull-back of the area form $\frac{\mathrm{i}}{2} d z \wedge d \bar{z}$ can be written as
\end{itemize}
$$\left(1+\mathfrak{w}_{\tau}\right) \frac{\mathrm{i}}{2} d z \wedge d \bar{z},$$
where the error term, $\mathfrak{w}_{\tau}$, is supported in $D^{(2)}-D^{(1)}$ and is such that $\left|\mathfrak{w}_{\tau}\right| \leq c_{0}\left|\ln \rho_{0}\right|^{-1}$.
Now set
$$\mathbf{u}_{\tau}:=\varrho_{\tau} \circ \mathbf{u}_{\tau}^{(1)},$$
where $\varrho_{\tau}$ is a diffeomorphism of $D^{*}$, which is the identity on $D^{(1)}$ and on $D-D^{(2)}$ so that the result is area-preserving.

The map $\varrho_{\tau}$ is defined using Moser's trick. To elaborate, the map $\varrho_{\tau}$ is obtained by integrating a $\tau$-dependent vector field on $D^{(2)}-D^{(1)}$ that vanishes near the boundary. This is to say that $\frac{\partial}{\partial_{\tau}} \varrho_{\tau}=\mathrm{v}_{\tau}\left(\varrho_{\tau}\right)$, where $\tau \mapsto \mathrm{v}_{\tau}$ is a vector field with compact support on $D^{(2)}-D^{(1)}$. This vector field $\mathrm{v}_{\tau}$ is chosen so that its contraction with the form in (2.8) is an anti-derivative, $\mathfrak{b}_{\tau}$, of the two-form $\frac{\mathrm{i}}{2} \mathfrak{w}_{\tau} d z \wedge d \bar{z}$ with compact support in $D^{(2)}-D^{(1)}$. To say more about this anti-derivative, introduce the cylindrical coordinates $(\rho, \theta)$ on $D$ by writing $z=\rho e^{\mathrm{i} \theta}$. The two-form $\frac{\mathrm{i}}{2} \mathfrak{w}_{\tau} d z \wedge d \bar{z}$ can be written as
$d\left(h_{\tau} d \theta\right)$, where
$$h_{\tau}(\rho, \theta)=\int_{0}^{\rho} \mathfrak{w}_{\tau}(x, \theta) x d x$$
The function $h_{\tau}$ is zero on $D^{(1)}$ and it depends only on the angle $\theta$ on a neighborhood of $D-D^{(2)}$. The fact that $\frac{\mathrm{i}}{2} \mathfrak{w}_{\tau} d z \wedge d \bar{z}$ has integral zero over $D^{(2)}$ implies that $h_{\tau}=\frac{\partial}{\partial \theta} u_{\tau}$ on $D-D^{(2)}$ where $u_{\tau}$ is a function only of the angle $\theta$. This understood, let $\rho_{(2)}$ denote the radius of $D^{(2)}$, and then define
$$\mathfrak{b}_{\tau}=h_{\tau} d \theta-d\left(\left(1-\chi\left(|\cdot| / \rho_{2}\right) u_{\tau}\right) .\right.$$
This one-form has compact support in $D-D^{(2)}$ and is such that $d \mathfrak{b}_{\tau}=$ $\frac{\mathrm{i}}{2} \mathfrak{w}_{\tau} d z \wedge d \bar{z}$. Note for future reference that $\left|\mathfrak{b}_{\tau}\right|$ and its $\tau$-derivative are both bounded by $c_{0}\left|\ln \rho_{0}\right|^{-1}|z|$. In addition, $\left|\nabla \mathfrak{b}_{\tau}\right|$ and its $\tau$-derivative are bounded by $c_{0}\left|\ln \rho_{0}\right|^{-1}|z|$. It follows as a consequence that $\mathrm{v}_{\tau}$ and its corresponding derivatives obey similar bounds.
2.4. Proofs of Lemmas 2.1, 2.2 and 2.4. We now have the ingredients to define the modified map:

Definition 2.4. Given a pair $(\delta, N)$ of a small positive number and an integer, let $f^{\prime}: F \rightarrow F$ be the following map:
$$f^{\prime}=\left\{\begin{array}{cc}
\left(\varphi_{\gamma}^{-1}\right)^{*} \mathrm{u}_{\tau=2 \pi k / q} & \text { on } \varphi_{\gamma}(\{2 \pi k / q\} \times D), \\
& \forall k \in\{0, \ldots, q-1\} \text { and } \gamma \in \Lambda_{N} ; \\
f & \text { on the remainder of } F .
\end{array}\right.$$
In the above, $q$ denotes the period of $\gamma$, and the parameters $\mathfrak{e}, \rho_{0}$ that enter into the definition of $\mathrm{u}_{\tau=2 \pi k / q}$ are chosen as follows:
\begin{itemize}
\item[-] the perturbation term $\mathfrak{e}$ in (2.6) is chosen in a suitably generic fashion so that all periodic points of $f^{\prime}$ are non-degenerate periodic points;
\item[-] let $\rho_{0}=\delta^{32}$.
\end{itemize}

By construction, $f^{\prime}$ obeys the first two items of Lemma 2.1, and it obeys the remaining items if all periodic orbits of $f^{\prime}$ with period $N$ or less are in $f^{\prime}$ s version of $\Lambda_{N}$. To prove this, suppose that $\gamma^{\prime} \subset F$ is a periodic orbit of $f^{\prime}$ with period $q^{\prime} \in\{1, \ldots, N\}$. Let $\mathrm{p}^{\prime} \in \gamma^{\prime}$. Given that $\left|f-f^{\prime}\right| \leq c_{0} \rho_{0}^{1 / 4}$, it follows that $\left|\operatorname{dist}\left(f^{\prime q^{\prime}}\left(\mathrm{p}^{\prime}\right), \mathrm{p}^{\prime}\right)\right| \leq c_{0} \rho_{0}^{1 / 4}$ also. Thus, if $\delta<c_{0}^{-1}$, then there is an orbit $\gamma \subset \Lambda_{N}$ of order a divisor, $q$, of $q^{\prime}$, and a point $\mathrm{p} \in \gamma$ with the following property: Each $k \in\left\{1, \ldots, q^{\prime}\right\}$ version of $f^{k}(\mathrm{p})$ has distance $c_{0} \rho_{0}^{1 / 4}$ or less from both $f^{k}\left(\mathrm{p}^{\prime}\right)$ and $\left(f^{\prime}\right)^{k}\left(\mathrm{p}^{\prime}\right)$. This understood, $\mathrm{p}^{\prime}$ and its $f^{\prime}$ iterates are in the image via the tubular neighborhood map $\varphi_{\gamma}$ of the set $\bigcup_{1 \leq k \leq q}\{2 \pi k / q\} \times D$. No generality is lost by assuming that $\mathrm{p}^{\prime}$ is in the $\varphi_{\gamma}$ image of a point $(0, z) \in S^{1} \times D$.

Let $\eta(\tau)$ denote the solution to (2.7) with $\eta(0)=z$ and set the constant
$$\lambda=\lambda^{*}(z) .$$
Given that $\eta$ obeys (2.7), it follows that
$$c_{0}^{-1}|z| \leq|\eta| \leq c_{0}|z|$$
at all $\tau \in S^{1}$. As a consequence, $\left|\lambda^{*}(\eta)-\lambda\right| \leq c_{0}|\ln \delta|^{-1}$ at each $\tau \in S^{1}$. This then implies that the equation for $\eta$ can be written as
$$\frac{\mathrm{i}}{2} \frac{d}{d \tau} \eta+\nu^{\lambda} \eta+\mu^{\lambda} \bar{\eta}+\mathfrak{x}(\eta)=0,$$
where $|\mathfrak{x}(\eta)| \leq c_{0}|\ln \delta|^{-1}|\eta|$. Integrating (2.12) finds that
$$\left|\left(1-\left(K^{\lambda}\right)^{q^{\prime} / q}\right) z\right| \leq c_{0}|\ln \delta|^{-1}|z| .$$
This last inequality requires that $z=0$ when $\delta$ is small by virtue of the fact that $K^{\lambda}$ is conjugate in $\operatorname{Sl}(2 ; \mathbb{R})$ to $K_{\gamma}$ and $\operatorname{det}\left(1-\left(K_{\gamma}\right)^{q^{\prime} / q}\right) \neq 0$ for all integer multiples $q^{\prime}$ of $q$.

To obtain Lemma 2.2, take $\mathfrak{r}^{\prime}$ to be the version of $\mathfrak{r}^{(1)}$ given by (2.6) that is used to construct $f^{\prime}$. This done, then the lemma only summarizes definitions of $\varphi_{\gamma}$ and the map $f^{\prime}$ given in the previous section.

The proof of Lemma 2.4 differs only in notation from the proof of Proposition 2.5 from [T1] given in the latter's Appendix. The reader is referred to this same Appendix for the details. The five remarks that follows serve only to point out certain key points that enter the proof.

Remark 2.1. It is a relatively straightforward exercise with matrices to construct an almost complex structure $J^{\prime}$ that obeys all but the fifth item of Lemma 2.4, and which has the following additional properties: First, $\left|J-J^{\prime}\right|$ is zero except in the image via the maps from $\left\{\varphi_{\gamma}\right\}_{\gamma \in \Lambda_{N}}$ of the set in $S^{1} \times D$ where $|z| \leq \rho_{0}^{1 / 4}$. Second, the difference between $J$ and $J^{\prime}$ on such an image is such that $\left|J-J^{\prime}\right| \leq c_{0}|z|$. In general $\left|\nabla\left(J-J^{\prime}\right)\right|$ will be $\mathcal{O}(1)$. This last fact complicates a direct perturbation theoretic construction of the desired pairing between $J$ and $J^{\prime}$ pseudoholomorphic curves.

Remark 2.2. To see how this problem is addressed, keep in mind that the $f$ and $f^{\prime}$ versions of the set $\Lambda_{N}$ agree; as a consequence, so do the two versions of the generating set $\mathcal{A}$ for the periodic Floer homology chain complex. This understood, fix a pair $\Theta_{-}$and $\Theta_{+}$from $\mathcal{A}$ so as to consider the $J$ and $J^{\prime}$ versions of the space $\mathcal{M}_{1}\left(\Theta_{+}, \Theta_{-}\right)$. The relatively large size of $\left|\nabla\left(J-J^{\prime}\right)\right|$ precludes a direct comparison between the $J$ and $J^{\prime}$ versions of this set. Even so, an indirect comparison can be made as follows: Fix some large integer $Q$ so as to compare successive versions of $\mathcal{M}_{1}\left(\Theta_{+}, \Theta_{-}\right)$as defined by
an ordered set, $\left\{J_{k}\right\}_{0 \leq k \leq Q}$, of almost complex structures with the following properties:
\begin{itemize}
\item[-] $J_{0}=J$, and $J_{Q}$ is the desired $J^{\prime}$.
\item[-] $J_{k}=J$ on the complement of the images via the maps $\left\{\varphi_{\gamma}\right\}_{\gamma \in \Lambda_{N}}$ of where $|z| \leq \rho_{0}^{1 / 4}$.
\item[-] $\left|J_{k}-J_{k-1}\right| \leq c_{0} Q^{-1}|z|$ on the image of $\mathbb{R} \times S^{1} \times D$ of any map from the set $\left\{\varphi_{\gamma}\right\}_{\gamma \in \Lambda_{N}}$.
\item[-] $\left|\nabla\left(J_{k}-J_{k-1}\right)\right| \leq c_{0} Q^{-1}$.
\item[-] Each $\gamma \in \Lambda_{N}$ version of the cylinder $\mathbb{R} \times \gamma$ is $J_{k}$-pseudoholomorphic.
\end{itemize}

Remarks 2.3. Perturbation-theoretic tools are used to construct a 1-1 correspondence between the pseudoholomorphic curves in the respective versions of $\mathcal{M}_{1}\left(\Theta_{+}, \Theta_{-}\right)$as defined by the almost complex structures at successive steps. Likewise, perturbation theory is used to prove that paired almost pseudoholomorphic curves have equal ±1 weights of the sort used to compute the embedded contact homology differential.

The use of perturbative tools exploits four key facts. Here are the first three:
Fact 1. The factor $Q^{-1}$ can be very small.
Fact 2. Each $\gamma \in \Lambda_{N}$ version of the cylinder $\mathbb{R} \times \gamma$ is $J_{k}$-pseudoholomorphic for each $k$.
Fact 3. Successive versions of $\left|J_{k+1}-J_{k}\right|$ can have support in successively smaller neighborhoods of $\bigcup_{\gamma \in \Lambda_{N}} \gamma$; and these neighborhoods can be made as small as desired, independent of $Q$ and $\delta$.
To say something about the fourth key fact, suppose that $C$ is a non- $\mathbb{R}$ invariant subvariety that appears in some element from the $J_{k}$ version of $\mathcal{M}_{1}\left(\Theta_{+}, \Theta_{-}\right)$. Any given end $\mathcal{E} \subset C$ at large $|s|$ is described by (1.7) but with the functions $(\nu, \mu)$ dependent on the index $k$. This understood, here is the fourth fact:
Fact 4. There is a lower bound, independent of $k, Q$ and $\delta$ to the absolute value of the eigenvalue $\lambda_{q_{E}}$ that can appear in (1.7).

Remark 2.4. These four facts are relevant because any given non- $\mathbb{R}$ invariant, $J_{k}$-pseudoholomorphic subvariety will intersect the small neighborhoods in Fact 3 above in only two ways. First, such a subvariety, $C$, can intersect this neighborhood near the points where it intersects a cylinder of the form $\mathbb{R} \times \gamma$ with $\gamma \in \Lambda_{N}$. There are but a finite set of points where $C$ intersects any given $\mathbb{R}$-invariant cylinder. In fact, there is a bound on the number of such points that is essentially topological and so independent of $C$ and of the index $k$. In particular, if the modification from one step to the next is done in a very small neighborhood of the cylinders $\{\mathbb{R} \times \gamma\}_{\gamma \in \Lambda_{N}}$, then the region where $J_{k+1} \neq J_{k}$ will intersect all but the very large $|s|$ part of $C$ in a set of at most $c_{0}^{-1}$ disks, each with very small area. This has the following
consequences: The subvariety $C$ is $J_{k+1}$-pseudoholomorphic except at very large $|s|$, and except in a union of at most $c_{0}^{-1}$ disks, each very small area. Moreover, $C$ is nearly $J_{k+1}$-pseudoholomorphic in each such disk if $Q$ is large and $\delta$ is small, both in a pointwise sense and in an $L^{2}$ sense.

The subvariety $C$ also intersects the region where $J_{k+1} \neq J_{k}$ at points far out on its ends, thus at very large values of $|s|$. The area of intersection here is, of course, infinite. However, the relevant versions of (1.7) are used to prove that this is of no ultimate consequence. In particular, $C$ is nearly $J_{k+1}$-pseudoholomorphic in a pointwise sense and also in an $L^{2}$ sense if $Q$ is large and $\delta$ is small.

Remark 2.5. This final remark concerns a most crucial point in the constructions from the Appendix of [T1]: The perturbative approach from this appendix will construct a partner to $C$ from the $J_{k+1}$ version of $\mathcal{M}_{1}\left(\Theta_{+}, \Theta_{-}\right)$ provided that the operator $\mathcal{D}_{C}$ from (2.4) is invertible. The four facts stated above, and Fact 4 in particular, guarantee that such is the case when $Q$ is large and $\delta$ is very small.

\section*{3. Constructing Seiberg-Witten solutions on $M$}

Define $M$ from a given area-preserving map $f: F \rightarrow F$. The purpose of this section is to explain how the constructions in Section 3 of [T2] are used to associate solutions to certain versions of the Seiberg-Witten equations to finite sets with any given element a pair consisting of a closed integral curve of $\partial_{t}$ and a positive integer. Such an association can also be obtained from the constructions in the article Gr ⇒ SW from [T6]. The constructions from Section 3 of [T2] differ with regard to certain details from those in the Gr ⇒ SW article, but they are identical in spirit.

The relation between the solutions to the Seiberg-Witten equations and sets of closed integral curves is described in Theorem 3.1 of the upcoming Section 3.4. The intervening subsections set the stage.
3.1. Vortices. This subsection summarizes some of what is said in Section 2 of [T2] about the vortex equations on $\mathbb{C}$. These are equations for a pair $(A, \alpha)$ where $A$ is a connection on the product $\mathbb{C}$-bundle over $\mathbb{C}$ and $\alpha$ is a section of this bundle. These equations read
$$* F_{A}=-\mathrm{i}\left(1-|\alpha|^{2}\right) \quad \text { and } \quad \bar{\partial}_{A} \alpha=0 .$$
Here, $F_{A}$ denotes the curvature two-form of $A$ and $\bar{\partial}_{A}$ is the d-bar operator defined by $A$. These equations are augmented with the constraint that (1 - $\left.|\alpha|^{2}\right)$ be integrable. Solutions $(A, \alpha)$ and $\left(A^{\prime}, \alpha^{\prime}\right)$ are deemed gauge equivalent when there exists a map $u: \mathbb{C} \rightarrow S^{1}$ such that $A^{\prime}=A-u^{-1} d u$ and $\alpha^{\prime}=u \alpha$.

The space of equivalence classes of solutions has path components $\left\{\mathfrak{C}_{m}\right\}_{m=0,1, \ldots}$. The space $\mathfrak{C}_{0}$ consists of the gauge equivalence classes of the
pair $\left(A_{I}, \alpha=1\right)$ where $A_{I}$ is the product connection on $\mathbb{C} \times \mathbb{C}$. Meanwhile, any given $m \geq 1$ version of $\mathfrak{C}_{m}$ consists of the gauge equivalence classes of solutions to (3.1) with $\alpha$ having $m$ zeros counting multiplicity. Each such $\mathfrak{C}_{m}$ has the structure of a complex manifold. The complex structure is such that the holomorphic tangent space to $\mathfrak{C}_{m}$ at the equivalence class of some given solution $\mathfrak{c}=(A, \alpha)$ has a canonical identification with the $L^{2}$ kernel of the operator:
$$\begin{aligned}
\vartheta_{\mathfrak{c}}: C^{\infty}(\mathbb{C} ; \mathbb{C} \oplus \mathbb{C}) & \rightarrow C^{\infty}(\mathbb{C} ; \mathbb{C} \oplus \mathbb{C}), \\
(x, \iota) & \mapsto\left(\partial x+2^{-1 / 2} \bar{\alpha} \iota, \bar{\partial}_{A} \iota+2^{-1 / 2} \alpha x\right) .
\end{aligned}$$
Here, $\partial$ denotes $\frac{\partial}{\partial z}$. The $L^{2}$ kernel of $\vartheta_{\mathfrak{c}}$ is denoted by $\operatorname{Ker}\left(\vartheta_{\mathfrak{c}}\right)$ in what follows. The space $\mathfrak{C}_{m}$ is biholomorphic to $\mathbb{C}^{m}$; and the collection of functions $\left\{\sigma_{q}\right\}_{1 \leq q \leq m}$ on $\mathfrak{C}_{m}$ given by
$$\sigma_{q}=\frac{1}{2 \pi} \int_{\mathbb{C}} z^{q}\left(1-|\alpha|^{2}\right)$$
give a set of holomorphic coordinates on $\mathfrak{C}_{m}$.
The inner product on $L^{2}(\mathbb{C} ; \mathbb{C} \oplus \mathbb{C})$ gives $\mathfrak{C}_{m}$ a Kähler metric. To be explicit, the induced Hermitian inner product on $T_{1,0} \mathfrak{C}_{m}$ is such that the square of the norm of any given element $(x, \iota)$ in $\operatorname{Ker}\left(\vartheta_{\mathfrak{c}}\right)$ is
$$\frac{1}{\pi} \int_{\mathbb{C}}\left(|x|^{2}+|\iota|^{2}\right) .$$
Except for the $n=1$ case, this Kähler metric is not the pull-back of the standard metric on $\mathbb{C}^{m}$ via the holomorphic identification that is defined by the functions $\left(\sigma_{1}, \ldots, \sigma_{m}\right)$.

The action of $S^{1}$ on $\mathbb{C}$ as multiplication by the unit complex numbers induces an isometric action of $S^{1}$ on $\mathfrak{C}_{m}$. This action has a unique fixed point, this being the unique solution to (3.1) whose version of $\alpha$ vanishes at the origin with degree $m$. This point in $\mathfrak{C}_{m}$ is called the symmetric vortex.

Of interest in what follows are certain sorts of dynamical flows on $\mathfrak{C}_{m}$. To say more, fix a pair $(\nu, \mu)$ of maps from $S^{1}$ to $\mathbb{R}$ and $\mathbb{C}$. Use the latter to define the real valued function
$$ɦ=h_{(\nu, \mu)}:=\frac{1}{4 \pi} \int_{\mathbb{C}}\left(2 \nu|z|^{2}+\left(\mu \bar{z}^{2}+\bar{\mu} z^{2}\right)\right)\left(1-|\alpha|^{2}\right) .$$
on $S^{1} \times \mathfrak{C}_{m}$. View this as a one-parameter family of functions on $\mathfrak{C}_{m}$. Use the Kähler two-form to define the corresponding one-parameter family of Hamiltonian vector fields. Of interest are the closed, integral curves of this family. These are maps $\mathfrak{c}: S^{1} \rightarrow \mathfrak{C}_{m}$ that obey at each $\tau \in S^{1}$ the equation
$$\frac{\mathrm{i}}{2} \mathfrak{c}^{\prime}+\left.\nabla^{(1,0)} ɦ\right|_{\mathfrak{c}}=0,$$
where $\mathfrak{c}^{\prime}$ is shorthand for the $(1,0)$ part of $\mathfrak{c}_{*} \frac{d}{d \tau}$, and where $\nabla^{(1,0)} \mathfrak{f}$ denotes the $(1,0)$ part of the gradient of $f$.

A solution to (3.6) is said to be non-degenerate when a certain auxiliary, self-adjoint operator has trivial kernel. To elaborate, suppose for the moment that $\mathfrak{c}: S^{1} \rightarrow \mathfrak{C}_{m}$ is any given map. Associate to the latter the symmetric operator
$$\zeta \mapsto \frac{\mathrm{i}}{2} \nabla_{\tau} \zeta+\left.\left(\nabla_{\zeta_{\mathbb{R}}} \nabla^{(1,0)} \mathfrak{h}\right)\right|_{\mathfrak{c}}$$
on $C^{\infty}\left(S^{1} ; \mathfrak{c}^{*} T_{1,0} \mathfrak{C}_{n}\right)$. Here, $\nabla_{\tau}$ denotes the covariant derivative on $C^{\infty}\left(S^{1}\right.$; $\left.\mathfrak{c}^{*} T_{1,0} \mathfrak{C}_{n}\right)$ as defined by the pull back of the Levi-Civita connection on $T_{1,0} \mathfrak{C}_{n}$. Meanwhile, $\left.\left(\nabla_{\zeta_{\mathbb{R}}} \nabla^{(1,0)} ɦ\right)\right|_{\mathfrak{c}}$ denotes the covariant derivative at $\mathfrak{c}$ along the vector defined by $\zeta$ in $\left.T \mathfrak{C}_{n}\right|_{\mathfrak{c}}$ of the vector field $\nabla^{(1,0)} \hbar \in C^{\infty}\left(\mathfrak{C}_{n} ; T_{1,0} \mathfrak{C}_{n}\right)$. A solution to (3.6) is non-degenerate when the operator depicted in (3.7) has trivial kernel.

The subsequent lemma plays a key role in what follows.
Lemma 3.1. Fix a positive integer $m$ and a pair $(\nu, \mu): S^{1} \rightarrow \mathbb{R} \times \mathbb{C}$ whose version of (1.8) has trivial $2 \pi q$ periodic kernel for each $q \in\{1, \ldots, m\}$. Then the space of solutions to the corresponding version of (3.6) is compact; and it is finite if all solutions are non-degenerate.

The proof of this lemma is identical to the proof given in Section 2b of [T4] of the latter's Proposition 2.1.

All solutions to (3.6) are known in special cases. What follows summarizes what is said in Lemmas 2.1-2.3 of [T2].
Lemma 3.2. (a) Fix a pair $(\nu, \mu)$ with $\nu$ a real valued function on $S^{1}$ and $\mu$ a $\mathbb{C}$-valued function. Use this pair to define the operator, $\mathcal{P}: C^{\infty}(\mathbb{R}, \mathbb{C}) \rightarrow C^{\infty}(\mathbb{R}, \mathbb{C})$ by the rule $\eta \mapsto \frac{\mathrm{i}}{2} \frac{d}{d \tau} \eta+\nu \eta+\mu \bar{\eta}$. Assume that 0 is the only $2 \pi$-periodic element in the kernel of $\mathcal{P}$. Then there is a unique solution to the corresponding $m=1$ version of (3.6), which is the constant map to the symmetric vortex. This solution is non-degenerate.
\begin{itemize}
\item[(b)] Fix an irrational number R and set $(\nu=\mathrm{R}, \mu=0)$. Then there is a unique solution in $m \geq 1$ version of $\mathfrak{C}_{m}$ to the corresponding version of (3.6). This is the constant map from $S^{1}$ to the symmetric vortex $\mathfrak{c}_{0} \in \mathfrak{C}_{m}$. This solution is non-degenerate.
\item[(c)] Fix $\mathrm{R} \in \frac{1}{2} \mathbb{Z}$ and a positive number $z$. Set $\left(\nu=\frac{1}{2} \mathrm{R}, \mu=-\frac{\mathrm{i}}{4 \pi} z \mathrm{e}^{2 \mathrm{iR} \tau}\right)$. Then there is a unique solution to the corresponding $m=1$ version of (3.6). This is the map to the symmetric vortex. This solution is non-degenerate. On the other hand, there are no solutions to the $m>1$ versions.
\end{itemize}

Fix $m \geq 1$ and suppose that $(\nu, \mu)$ are as described in Lemma 3.1. In such circumstance, any given non-degenerate solution to the corresponding
version of (3.6) can be assigned an integer degree. To do this, use the given pair $(\nu, \mu)$ to define the operator $\mathcal{P}$ in Lemma 3.2. Let $\eta(\tau)$ denote a nontrivial element in the kernel of $\mathcal{P}$. Then $\eta(\tau)$ can be written as
$$\eta(\tau)=U(\tau)\left(\eta_{0}\right),$$
where $U(\tau)$ is an $\mathbb{R}$-linear map from $\mathbb{C}$ to $\mathbb{C}$ that defines a matrix in $\operatorname{Sl}(2 ; \mathbb{R}$ when $\mathbb{C}$ is written as $\mathbb{R}^{2}$. The pair $(\nu, \mu)$ is said to be elliptic with rotation number a given real number $\mathrm{R} \notin \mathbb{Z}$ when $U$ on $[0,2 \pi]$ defines a path in $\operatorname{Sl}(2 ; \mathbb{R})$ that is homotopic in $\operatorname{Sl}(2 ; \mathbb{R})$ via a homotopy $\left\{U_{x}(\cdot)\right\}_{x \in[0,1]}$ with the following three properties: The matrix $U_{x}(0)$ is the identity, the matrix $U_{x}(2 \pi)$ is conjugate in $\operatorname{Sl}(2 ; \mathbb{R})$ to $U(2 \pi)$, and the path $U_{x=1}(\cdot)$ is the rotation with smooth angle parametrization $\tau \mapsto 2 \pi \mathrm{R} \tau$. It is assumed in what follows that R is irrational when $(\nu, \mu)$ are elliptic. The pair $(\nu, \mu)$ is said to be hyperbolic when the absolute value of the trace of $U(2 \pi)$ is greater than 2. In this case, there is a one-parameter family of pairs of function
$$\left\{\left(\nu_{x}, \mu_{x}\right): S^{1} \rightarrow \mathbb{R} \times \mathbb{C}\right\}_{x \in[0,1]}$$
with the following three properties:
\begin{itemize}
\item[-] $\left(\nu_{0}, \mu_{0}\right)=(\nu, \mu)$.
\item[-] Each pair $\left(\nu_{x}, \mu_{x}\right)$ has a corresponding $U_{x}(2 \pi)$ whose trace has absolute value at least 2.
\item[-] The path $\tau \mapsto U_{x=1}(\tau)$ as defined by the pair $\left(\nu_{1}, \mu_{1}\right)$ is the rotation with smooth angle parametrization $\tau \mapsto 2 \pi \mathrm{R} \tau$ with rotation number $\mathrm{R} \in \frac{1}{2} \mathbb{Z}$.
\end{itemize}
Granted the preceding, let
$$\mathfrak{c}_{0}: S^{1} \rightarrow \mathfrak{C}_{m}$$
denote the constant map to the symmetric vortex in $\mathfrak{C}_{m}$. Associate to $\mathfrak{c}_{0}$ the operator
$$\mathcal{R}: C^{\infty}\left(S^{1} ; T \mathfrak{C}_{m} \mid c_{0}\right) \rightarrow C^{\infty}\left(S^{1} ; T \mathfrak{C}_{m} \mid c_{0}\right),$$
that is defined as follows:
\begin{itemize}
\item[-] If $(\nu, \mu)$ is elliptic with rotation number R, this operator is the version of (3.7) with $\hbar=\mathfrak{h}_{\left(\frac{1}{2} \mathrm{R}, 0\right)}$.
\item[-] If $(\nu, \mu)$ is hyperbolic with rotation number R, the operator $\mathcal{R}$ is the version of (3.7) with $\mathfrak{h}=\mathfrak{h}_{\left(\frac{1}{2}\left(\mathrm{R}-\mathrm{R}^{\prime}\right), 0\right)}$, where $\mathrm{R}^{\prime}>0$ is an irrational number such that $m \mathrm{R}^{\prime} \ll 1$.
\end{itemize}
Lemma 2.4 in [T2] asserts that the operator $\mathcal{R}$ has trivial kernel in these cases.

Definition 3.1. Let $(\nu, \mu)$ be as in Lemma 3.1, and suppose that $\mathfrak{c}: S^{1} \rightarrow$ $\mathfrak{C}_{m}$ is non-degenerate in the sense that (3.7) has trivial kernel. Then the degree of $\mathfrak{c}$, denoted
$$\operatorname{deg}_{\mathfrak{C}}(\mathfrak{c})=\operatorname{deg}_{\mathfrak{C}}(\mathfrak{c},(\nu, \mu))$$
in the following, is the spectral flow from the operator $\mathcal{R}$ to $\mathfrak{c}$ 's version of (3.7).

For the definition of this spectral flow, see, e.g., Section 2 of [T8]).
Lemma 3.3. Let $(\nu, \mu)$ be the pair $\left(\nu_{\gamma}, \mu_{\gamma}\right)$ that appears in Definition 2.1. Fix $m \in\{1,2, \ldots\}$ when $(\nu, \mu)$ are elliptic and set $m=1$ when $\gamma$ is hyperbolic. Then the map to the symmetric vortex $\mathfrak{c}_{0}: S^{1} \rightarrow \mathfrak{C}_{m}$ has degree
$$\operatorname{deg}_{\mathfrak{C}}\left(\mathfrak{c}_{0},\left(\nu_{\gamma}, \mu_{\gamma}\right)\right)= \begin{cases}0 & \text { when } \gamma \text { is elliptic or negative hyperbolic, } \\ 1 & \text { when } \gamma \text { is positive hyperbolic. }\end{cases}$$
Proof. When $\gamma$ is elliptic, this is true by definition. When $\gamma$ is hyperbolic and $m=1$, the operator in (3.7) when written using the (3.3)'s coordinate $\sigma_{1}$ to identify $\mathfrak{C}_{1}$ with $\mathbb{C}$ is the operator $\mathcal{P}$ that appears in Lemma 3.2. This understood, the observation about the spectral flow in the negative hyperbolic case follows from the fact that the version of $\mathcal{P}$ with $(\nu, \mu)=(\pi, 0)$ has trivial $2 \pi$-periodic kernel. Meanwhile, the calculation of the assertion about the spectral flow in the positive hyperbolic case follows by direct computation using the [0, 1]-parametrized path $x \mapsto \mathcal{P}_{x}$ with $\mathcal{P}_{x}$ defined by $\left(\nu_{x}, \mu_{x}\right)=(-(1-x) \delta,-i \delta)$ with $\delta \in(0,1)$. \(\square\)
3.2. Periodic orbits and vortices. Return now to the context where $F$ is a surface with area form $w_{F}$ and $f: F \rightarrow F$ is an area-preserving map. Let $M$ denote the resulting three-manifold. Suppose that $\Theta$ is a finite set whose elements are described next. A given element is a pair $(\gamma, m)$ with $\gamma$ a closed integral curve of $\partial_{t}$ and $m$ a positive integer. Assume that distinct pairs from $\Theta$ have distinct integral curves. Note that $\Theta$ can be taken to be the empty set.

Let $(\gamma, m) \in \Theta$. Fix a tubular neighborhood map $\varphi_{\gamma}: S^{1} \times D_{\gamma} \rightarrow M$ with $D_{\gamma} \subset \mathbb{C}$ a disk about the origin. The map $\varphi_{\gamma}$ should be chosen to obey the conditions set forth by the first two items and the fourth item of Lemma 2.2. Use this map $\varphi_{\gamma}$ to define corresponding functions $(\nu, \mu)$; and let $\mathfrak{C}_{(\gamma, m)}$ denote the set of solutions to the corresponding version (3.6) with $\mathfrak{h}=h_{(\nu, \mu)}$. Let
$$\mathfrak{C} \Theta:=\times_{(\gamma, m) \in \Theta} \mathfrak{C}_{(\gamma, m)} .$$
Use $\mathfrak{C} \Theta^{*} \subset \mathfrak{C} \Theta$ to denote the subset of elements with the property that constituent maps $\left\{\mathfrak{c}_{\gamma}: S^{1} \rightarrow \mathfrak{C}_{m}\right\}_{(\gamma, m) \in \Theta}$ are non-degenerate.

Now suppose that a class $\Gamma \in H_{1}(M ; \mathbb{Z})$ has been specified. As in the introduction, use $d_{\Gamma}$ to denote the intersection number between $\Gamma$ and a typical fiber of the projection map $\pi$. Let $p$ denote the greatest integer divisor of the class $c_{\Gamma} \in H^{2}(M ; \mathbb{Z})$.

Let $\mathcal{Z}$ denote the set whose elements are described next. A given element is a set $\Theta$ as just described, but constrained so that the integral chain
$\sum_{(\gamma, m) \in \Theta} m \gamma$ represents the class $\Gamma$. Note that $\mathcal{Z}=\emptyset$ if $d_{\Gamma} \leq 0$ and if $\Gamma=0$, then $\mathcal{Z}$ has only the element $\Theta=\emptyset$. Hutchings specifies in Definition 1.5 of [H1] a relative $\mathbb{Z} / p \mathbb{Z}$-degree for each element $\Theta \in \mathcal{Z}$. This degree is relative in the following sense: A reference element $\Theta^{*} \in \mathcal{Z}$ is assigned degree 0 when $\mathcal{Z} \neq \emptyset$, then each $\Theta \in \mathcal{Z}$ has a well defined degree assignment in $\mathbb{Z} / p \mathbb{Z}$. This degree is denoted by $\operatorname{deg}_{p F h}(\Theta)$. If $\Theta^{\prime}$ is a second element in $\mathcal{Z}$, then the difference $\operatorname{deg}_{p F h}(\Theta)-\operatorname{deg}_{p F h}\left(\Theta^{\prime}\right)$ is the $\mathbb{Z} / p \mathbb{Z}$ reduction of what was denoted in Section 1.1 by $I\left(\Theta, \Theta^{\prime} ; Z\right)$, where $Z$ is a two-chain in $M$ with $\partial Z=\sum_{(\gamma, m) \in \Theta} m \gamma-\sum_{(\gamma, m) \in \Theta^{\prime}} m \gamma$.

The relative $\mathbb{Z} / p \mathbb{Z}$-degree for a given $\Theta \in \mathcal{Z}$ can be used to assign a relative $\mathbb{Z} / p \mathbb{Z}$-degree to each $x=\left\{\mathfrak{c}_{\gamma}\right\}_{(\gamma, m) \in \Theta} \in \mathfrak{C} \Theta^{*}$, this being
$$\operatorname{deg}_{\mathfrak{C} \mathcal{Z}}(x):=\operatorname{deg}_{p F h}(\Theta)+\sum_{(\gamma, m) \in \Theta} \operatorname{deg}_{\mathfrak{C}}\left(\mathfrak{c}_{\gamma}\right) .$$
3.3. The Seiberg-Witten equations. This subsection sets the stage for the definition of the relevant versions of the Seiberg-Witten equations.
3.3.1. The almost complex structure $\boldsymbol{J}$. Suppose that a non-degenerate $f$ is given to define $M$, and that $J \in \mathcal{J}_{f}$ is an $\mathbb{R}$-invariant almost complex structure on $\mathbb{R} \times M$. Recall that by definition, such a $J$ satisfies:
\begin{itemize}
\item[(1)] $J \partial_{s}=\partial_{t}$ where $\partial_{t}$ is a vector field on $M$ with $\left\langle d t, \partial_{t}\right\rangle=1$ whose first return is $f$.
\item[(2)] $J$ is tamed by the form $\Omega_{F}=d s \wedge d t+w_{F}$.
\end{itemize}

Because of item (1) above, the almost complex structure $J$ is determined by its action on $\operatorname{Ker}\left(\pi_{*}\right)$. Its action here determines a pair $(\mathfrak{j}, a)$ where $j$ is an endomorphism of $\operatorname{Ker}\left(\pi_{*}\right)$ with square -1 and $a$ is a section of $\operatorname{Hom}\left(\operatorname{Ker}\left(\pi_{*}\right) ; \mathbb{R}\right)$. These are defined so that
$$J v=\mathfrak{j} v+a(v) \partial_{s}+a(\mathfrak{j} v) \partial_{t} \quad \text { for } v \in \operatorname{Ker}\left(\pi_{*}\right) .$$
The assertion that $J$ is tamed by $w_{0}$ is equivalent to the assertion that
$$|a(v)|^{2}<4 w_{F}(v, \mathfrak{j} v) .$$

It is important for what follows to note that
$$J\left(v+a(v) \partial_{t}\right)=\mathfrak{j} v+a(\mathfrak{j} v) \partial_{t} .$$

As a consequence, $J$ preserves the subbundle
$$K^{-1}=\left\{v+a(v) \partial_{t}: v \in \operatorname{Ker}\left(\pi_{*}\right)\right\} .$$

By design, this subbundle has the structure of a complex line bundle over $M$. The bundle is of course isomorphic to the kernel of $\pi_{*}$ with its complex
structure defined by $\mathfrak{j}$. The bundle $K^{-1}$ is the kernel of the one-form
$$a=d t-a,$$
where $a$ is viewed here and subsequently as a one-form on $M$ that annihilates $\partial_{t}$.
3.3.2. The metric $\boldsymbol{g}$. The almost complex structure $J$ and the area form $w_{F}$ together define a metric $g$ on $M$ as follows:
\begin{itemize}
\item[-] The vector field $\partial_{t}$ has norm 1 and is orthogonal to $K^{-1}$.
\item[-] The inner product on $K^{-1}$ is given by $w_{F}(\cdot, \mathfrak{j}(\cdot))$.
\end{itemize}
With this definition, $g$ is such that
$$|\mathrm{a}|=1 \quad \text { and } \quad * \mathrm{a}=w_{F} .$$
Use this metric to define the oriented orthonormal frame bundle of $M$ and to define the corresponding Spin ${ }^{\mathbb{C}}$ lifts of this frame bundle.
3.3.3. The Spin ${ }^{\mathbb{C}}$ structure. Fix a Spin ${ }^{\mathbb{C}}$-bundle $\pi: \mathcal{F} \rightarrow M$, and let
$$\mathbb{S}=\mathcal{F} \times_{U(2)} \mathbb{C} \rightarrow M$$
denote the corresponding $\mathbb{C}^{2}$-bundle. Clifford multiplication on $\mathbb{S}$ by the oneform a from (3.11) has eigenvalues ±i, and so splits $\mathbb{S}$ as a direct sum of the corresponding two eigenbundles. This splitting is written as
$$\mathbb{S}=E \oplus E \otimes K^{-1},$$
where the convention has $\mathrm{cl}(\mathrm{a})$ acting as i on the left most summand. The assignment of $c_{1}(E)$ to the Spin ${ }^{\mathbb{C}}$-bundle defines a 1-1 correspondence between the set of equivalence classes of Spin ${ }^{\mathbb{C}}$-bundles over $M$ and the elements in $H^{2}(M ; \mathbb{Z})$. The canonical Spin ${ }^{\mathbb{C}}$-structure is one whose spinor bundle is splits as $\mathbb{S}_{I}=I_{\mathbb{C}} \oplus K^{-1}$, where $I_{\mathbb{C}}$ here denotes a complex line bundle that is isomorphic to the product bundle $M \times \mathbb{C}$.
3.3.4. Spin ${ }^{\mathbb{C}}$ connections and Dirac operators. As explained in Section 1c of the article SW ⇒ Gr from [T6], there is a unique connection, $A_{K}$, on $K^{-1}$ which is characterized as follows: Fix a unit norm section, $1_{\mathbb{C}}$, of the bundle $I_{\mathbb{C}}$, and let $A_{I}$ denote the unique Hermitian connection on $I_{\mathbb{C}}$ that makes $1_{\mathbb{C}}$ covariantly constant. Use the pair $A_{K}$ and $A_{I}$ to define a connection on $\operatorname{det}(\mathbb{S})$. Then the section $\psi_{I}=\left(1_{\mathbb{C}}, 0\right)$ obeys the Dirac equation.

Because of (3.12), the connection $A_{K}$ and a Hermitian connection on $E$ together define a connection $\mathbb{A}$ on $\operatorname{det}(\mathbb{S})=E^{\otimes 2} \otimes K^{-1}$. Conversely, a connection on the latter bundle defines with $A_{K}$ a Hermitian connection on $E$. This understood, the Seiberg-Witten equations are viewed in what follows as equations for a pair $(A, \psi)$ of connection on $E$ and section of $\mathbb{S}$.

The corresponding Dirac operator is denoted now as $D_{A}$. The space of smooth, Hermitian connections on $E$ is denoted in what follows by $\operatorname{Conn}(E)$.
3.3.5. The 3-dimensional Seiberg-Witten equations. The versions of the Seiberg-Witten equations of interest are parametrized by a number $r>$ 1. Fix such an $r$. With the metric and Spin ${ }^{\text {C }}$-structure chosen previously, the corresponding equations for a pair $(A, \psi)$ from the space $\operatorname{Conn}(E) \times$ $C^{\infty}(M ; \mathbb{S})$ read
$$B_{A}=r\left(\psi^{\dagger} \tau \psi-\mathrm{ia}\right)-\frac{1}{2} B_{A_{K}}-\frac{\mathrm{i}}{2} * \wp, \quad \text { and } \quad D_{A} \psi=0 .$$
Here, $B_{A}$ denotes the Hodge star of $A$ 's curvature two-form, and $\wp$ is a closed two-form in the cohomology class $2 \pi c_{1}(\mathfrak{s})$. Solutions $(A, \psi)$ and $\left(A^{\prime}, \psi^{\prime}\right)$ are gauge equivalent if there is a smooth map, $u$, from $M$ to $S^{1}$ such that
$$A^{\prime}=A-u^{-1} d u \quad \text { and } \quad \psi^{\prime}=u \psi .$$
Because $* \mathrm{a}=w_{f}$, the equations in (3.13) correspond to a version of (1.11) with
$$\varpi=2 r w_{f}+\wp, \quad \Psi=(2 r)^{1 / 2} \psi,$$
and $\mathbb{A}$ defined from $A$ and $K$ as above. When $r$ is fixed, we shall use $(\mathbb{A}, \Psi)$ and $(A, \psi)$ interchangably to denote a configuration, and write the configuration space as $\operatorname{Conn}(E) \times C^{\infty}(M, \mathbb{S})$. Use $\mathcal{C}^{r}$ in what follows to denote the space of gauge equivalence classes of solutions to (3.13).
3.3.6. The relative grading. Each configuration $\mathfrak{c}=(A, \psi)$ has an associated elliptic, symmetric operator
$$\mathfrak{L}_{\mathfrak{c}}: C^{\infty}\left(M ; \mathrm{i} T^{*} M \oplus \mathbb{S} \oplus \mathrm{i} \mathbb{R}\right) \rightarrow C^{\infty}\left(M ; \mathrm{i} T^{*} M \oplus \mathbb{S} \oplus \mathrm{i} \mathbb{R}\right),$$
which sends any given section $(b, \eta, \phi)$ of $\mathrm{i} T^{*} M \oplus \mathbb{S} \oplus \mathrm{i} \mathbb{R}$ to the section whose respective $\mathrm{i} T^{*} M, \mathbb{S}$ and $\mathrm{i} \mathbb{R}$ components are
$$\left\{\begin{array}{l}
* d b-d \phi-2^{-1 / 2} r^{1 / 2}\left(\psi^{\dagger} \tau \eta+\eta^{\dagger} \tau \psi\right), \\
D_{A} \eta+2^{1 / 2} r^{1 / 2}(\operatorname{cl}(b) \psi+\phi \psi), \\
* d * b-2^{-1 / 2} r^{1 / 2}\left(\eta^{\dagger} \psi-\psi^{\dagger} \eta\right) .
\end{array}\right.$$
(Note that despite its appearance, $\mathfrak{L}_{\mathfrak{c}}$ depends only on the configuration $\mathfrak{c}=(\mathbb{A}, \Psi)$, not on $r$.) A configurationc is said to be non-degenerate when $\mathfrak{L}_{\mathfrak{c}}$ has trivial cokernel. Let $\mathfrak{c}_{-}, \mathfrak{c}_{+}$be non-degenerate configurations. Given a path $\mathfrak{d}(s)$ of configurations from $\mathfrak{c}_{-}$to $\mathfrak{c}_{+}$, let $\mathcal{J}(\mathfrak{d})$ denote the spectral flow of the associated family of operators from $\mathfrak{L}_{\mathfrak{c}_{-}}$to $\mathfrak{L}_{\mathfrak{c}_{+}}$, defined as in [T8]. For $\mathfrak{c}_{+}=u \cdot \mathfrak{c}_{-}$, one has
$$\mathcal{J}(\mathfrak{d})=\left\langle c_{1}(\mathfrak{s}),[u]\right\rangle,$$
where $u \in C^{\infty}\left(M ; S^{1}\right)$ is a gauge transformation and $[u]$ denotes its cohomology class:
$$[u]:=u^{-1} d u /(2 \pi \mathrm{i}) .$$

Thus, as promised in Section 1.2, we may write $\mathcal{J}\left(\mathfrak{c}_{-}, \mathfrak{c}_{+} ; \mathfrak{h}\right)=\mathcal{J}(\mathfrak{d})$, which depends only on the gauge equivalence classes of $\mathfrak{c}_{-}, \mathfrak{c}_{+}$, and the relative homotopy class $\mathfrak{h}$ of $\mathfrak{d}$. Fix a non-degenerate reference configuration $\mathfrak{c}_{E}:=$ $\left(A_{E}, \psi_{E}\right)$. Given a non-degenerate configuration $\mathfrak{c}$, let
$$\operatorname{deg}_{S W}(\mathfrak{c}):=\mathcal{J}\left(\mathfrak{c}, \mathfrak{c}_{E}\right) \in \mathbb{Z} / p \mathbb{Z} .$$
This depends only on the gauge equivalence class of $\mathfrak{c}$.
3.4. Periodic orbits and Seiberg-Witten solutions. Fix a class $\Gamma \in$ $H^{1}(M ; \mathbb{R})$. Let $\mathfrak{s}_{\Gamma}$ denote the Spin ${ }^{\mathbb{C}}$ structure whose spinor bundle splits as in (3.12) with the first Chern class of the bundle $E$ equal to the Poincaré dual of $\Gamma$. The theorem that follows refers to the versions of (3.13) as defined for this particular Spin ${ }^{\mathbb{C}}$ structure.

Theorem 3.1. Let $\boldsymbol{\mu}_{P}=\left\{\left(F, w_{F}\right), f, \Gamma, J\right\}$ and $\boldsymbol{\mu}_{S}=\left\{M, \mathfrak{s}_{\Gamma}, \varpi_{r}, g, \mathfrak{q}\right\}$ be corresponding periodic Floer homology and Seiberg-Witten-Floer cohomology data sets as in the statement of Theorem 1.1, and let $r \geq 1$. Use $\mathcal{C}^{r}$ to denote the space of gauge equivalence classes of solutions to the corresponding version of (3.13). Then:
\begin{itemize}
\item[(1)] If $d_{\Gamma} \leq 0$ and $\Gamma \neq 0$, then $\mathcal{C}^{r}=\emptyset$ for all sufficiently large $r$.
\item[(2)] If $\Gamma=0$, then $\mathcal{C}^{r}$ consists of a single element for all sufficiently large $r$.
\item[(3)] Suppose that $d_{\Gamma}>0$. Let
$$\mathfrak{X}= \begin{cases}\bigcup_{\Theta \in \mathcal{Z}} \mathfrak{C} \Theta & \text { if } \mathfrak{C} \Theta^{*}=\mathfrak{C} \Theta \text { for all } \Theta \in \mathcal{Z}, \\ \text { a finite subset of } \bigcup_{\Theta \in \mathcal{Z}} \mathfrak{C} \Theta^{*} & \text { otherwise. }\end{cases}$$
There exists, for all sufficiently large r, a 1-1 map
$$\Phi^{r}: \mathfrak{X} \rightarrow \mathcal{C}^{r}$$
with the following properties:
\item[(a)] The image of $\Phi^{r}$ consists of non-degenerate solutions to (3.13).
\item[(b)] If $x_{-}, x_{+} \in \mathfrak{X}$, then
$$\operatorname{deg}_{S W}\left(\Phi^{r}\left(x_{+}\right)\right)-\operatorname{deg}_{S W}\left(\Phi^{r}\left(x_{-}\right)\right)=\operatorname{deg}_{\mathfrak{C} \mathcal{Z}}\left(x_{-}\right)-\operatorname{deg}_{\mathfrak{C} \mathcal{Z}}\left(x_{+}\right) .$$
\item[(c)] If $\mathfrak{C} \Theta^{*}=\mathfrak{C} \Theta$ for all $\Theta \in \mathcal{Z}$ and $\mathfrak{X}=\bigcup_{\Theta \in \mathcal{Z}} \mathfrak{C} \Theta$, then $\Phi^{r}$ is also onto $\mathcal{C}^{r}$.
\end{itemize}

Proof of Theorem 3.1. There are five parts to the proof of this theorem. Part 1 constructs the solution whose existence is asserted by the second item. Part 2 constructs the map $\Phi^{r}$ from $\mathfrak{X}$ into $\mathcal{C}^{r}$ and proves that it is one to one. Part 3 proves items (3a) and (3b) of the assertions. Part 4 establishes some basic a priori bounds for solutions of (3.13). These bounds are then used in Part 5 to prove item (1), the uniqueness assertion of item (2), and item (3c). \(\square\)

Part 1. The solution whose existence is asserted by item (2) can be constructed by copying almost verbatim what is done in the first parts of Section 2d of [T9], with the following replacements:
$$\left\{\begin{array}{l}
\text { - Replace the contact form a in }[\mathbf{T 9}] \text { by the one-form a intro- } \\
\text { duced in }(3.11) . \\
\text { - Replace } B_{A_{K}} \text { in }[\mathbf{T 9}] \text { by } \\
\qquad B_{0}:=B_{A_{K}}+\mathrm{i} * \wp
\end{array}\right.$$
These replacements do not affect the arguments in Section 2d of [T9]; and these prove the following:

Lemma 3.4. Suppose that the Spin ${ }^{\mathbb{C}}$ structure is the canonical one. Then there exists a constant $\kappa>1$ such that for all $r \geq \kappa$, there is a solution, $\left(A_{0}, \psi_{0}\right)$, to (3.13) with the following properties:
\begin{itemize}
\item[-] $\left|\psi_{0}\right| \geq 1-\kappa r^{-1 / 2}$ on the whole of $M$.
\item[-] If $(A, \psi)$ is a solution to (3.13) and if $|\psi| \geq 1-\kappa^{-1}$ on the whole of $M$, then $(A, \psi)$ is gauge equivalent to $\left(A_{0}, \psi_{0}\right)$.
\end{itemize}

Part 2. The map $\Phi^{r}$ is constructed by copying what is done in Section 3 of [T2]. The latter constructs the analog of the map $\Phi^{r}$ in the following context: First the orbits that appear in any given set from $\mathcal{Z}$ are closed integral curves of the Reeb vector field of a contact 1-from on $M$. Second, that same contact one-form is used as the one-form a to define (3.13). With the same sort of replacements as (3.16), these constructions can be applied in the present context with only cosmetic changes. The proof that the current version of $\Phi^{r}$ is injective is obtained by copying almost verbatim what is said in Section 3g of [T2] to prove the latter's Theorem 1.1. Note in this regard that the function E that appears in equation (1.12) and Theorem 1.1 of [T2] has an analog here; the definition is the same:
$$\mathrm{E}(A)=i \int_{M} \mathrm{a} \wedge * B_{A},$$

What is denoted by $\ell_{\gamma}$ in [T2] corresponds here to $2 \pi q$, where $q$ is the period of $\gamma$. As a consequence,
$$\sum_{(\gamma, m) \in \Theta} m \ell_{\gamma}=2 \pi d_{\Gamma} .$$
More is said in the upcoming Part 4 of the proof of Theorem 3.1 about the values of the function E in (3.17) on the space $\mathcal{C}^{r}$.
Part 3. What is asserted by items (3a) and (3b) of Theorem 3.1 has its analog in Theorem 1.1 of [T3]. Again, with the same sort of substitution
as (3.16), the arguments in Section 2 of [T3] can be applied here with only cosmetic changes to prove items (3a) and (3b) of Theorem 3.1.

Part 4. This part of the proof establishes the key a priori bounds on the behavior of solutions to (3.15). The first of these is an analog of Lemma 2.3 in [T4]:

Lemma 3.5. There exists a constant $\kappa>1$ with the following significance: Suppose that $r \geq \kappa$ and that $(A, \psi=(\alpha, \beta))$ is a solution to (3.13). Then:
\begin{itemize}
\item[(1)] $|\alpha| \leq 1+\kappa r^{-1}$.
\item[(2)] $|\beta|^{2} \leq \kappa r^{-1}\left(1-|\alpha|^{2}\right)+\kappa^{2} r^{-2}$.
\item[(3)] $\left|\nabla_{A} \alpha\right|^{2} \leq \kappa r\left(1-|\alpha|^{2}\right)+\kappa^{2}$.
\item[(4)] $\left|\nabla_{A} \beta\right|^{2} \leq \kappa\left(1-|\alpha|^{2}\right)+\kappa^{2} r^{-1}$.
\end{itemize}
In addition, for each integer $q \geq 1$, there exists a constant $\kappa_{q}$ such that when $r \geq \kappa$, then
\begin{itemize}
\item[(5)] $\left|\nabla_{A}^{q} \alpha\right|+r^{1 / 2}\left|\nabla_{A}^{q} \beta\right| \leq \kappa_{q} r^{q / 2}$.
\end{itemize}
Proof of Lemma 3.5. The first two item and the final item are proved by copying what is done in the proofs of Lemmas 2.2-2.4 of [T7]. The third and fourth items are proved by copying what is done in the proof of the analogous assertions of Lemma 2.3 in [T4]. \(\square\)

The next a priori bound concerns the integral ofr $\left(1-|\alpha|^{2}\right)$ over $M$. Note that a bound on this integral gives a bound on the value of the function E from (3.17). This follows by using (3.13) and the first two items in Lemma 3.5 to write
$$* B_{A}=-\mathrm{i}\left(r\left(1-|\alpha|^{2}\right)+\mathfrak{e}_{1}\right) w_{f}+\mathfrak{e}_{2},$$
where $\mathfrak{e}_{1}$ and $\mathfrak{e}_{2}$ are such that:
$$\begin{aligned}
& \left|\mathfrak{e}_{1}\right| \leq c_{0}\left(1-|\alpha|^{2}\right)+c_{0}^{2} r^{-1} ; \\
& \left|\mathfrak{e}_{2}\right| \leq r^{1 / 2}\left|\left(1-|\alpha|^{2}\right)\right|+c_{0} \quad \text { and } \text { a } \wedge \mathfrak{e}_{2}=0 .
\end{aligned}$$

Lemma 3.6. There exists a constant $\kappa>1$ with the following significance: Suppose that $r \geq \kappa$ and that $(A, \psi)$ is a solution to (3.13). Then
$$r \int_{M}\left|1-|\alpha|^{2}\right| \leq \kappa .$$
Proof. Since $\frac{\mathrm{i}}{2 \pi} F_{A}$ represents the first Chern class of the bundle $E$ in de Rham cohomology, it follows that
$$\mathrm{i} \int_{M} d t \wedge * B_{A}=4 \pi^{2} d_{\Gamma}$$

Meanwhile, the first two items in Lemma 3.5 together with (3.18) imply that the integral on the left-hand side is no less than
$$\left(1-c_{0}^{-1}\right) r \int_{M}\left(1-|\alpha|^{2}\right)-c_{0} .$$
This bounds the integral over $M$ of $r\left(1-|\alpha|^{2}\right)$ by an $r$ and $(A, \psi)$ independent constant. Together with the first item in Lemma 3.5, such a bound supplies the same sort of bound on the integral over $M$ of $\left|\left(1-|\alpha|^{2}\right)\right|$. \(\square\)

Part 5. This part proves assertions (1), (3c), and the uniqueness assertion in item (2) of Theorem 3.1. To start, consider a sequence $\left\{\left(r_{n},\left(A_{n}, \psi_{n}=\right.\right.\right.$ $\left.\left.\left.\left(\alpha_{n}, \beta_{n}\right)\right)\right)\right\}_{n=1,2, \ldots}$ such that $\left\{r_{n}\right\}_{n=1,2, \ldots}$ is unbounded, and such that $\left(A_{n}, \psi_{n}\right)$ obeys the $r=r_{n}$ version of (3.13). If $c_{1}(E)=0$, assume in addition that $\left(A_{n}, \psi_{n}\right)$ is not the solution $\left(A_{0}, \psi_{0}\right)$ given by Lemma 3.4.

Given the bound supplied by Lemma 3.6, the argument from Section 6d of [T7] (or part I of [T6]) can be used with only notational modifications to find a finite set $\Theta=\{(\gamma, m)\}$ with the following properties:
\begin{itemize}
\item[-] $\gamma$ is a closed integral curve of $\partial_{t}$ and $m$ is a positive integer.
\item[-] $\sum_{(\gamma, m) \in \Theta} m \gamma$ defines a chain that represents $\Gamma$ in $H_{1}(M ; \mathbb{Z})$.
\item[-] The loci $\alpha_{n}^{-1}(0)$ converges geometrically to $\sum_{(\gamma, m) \in \Theta} m \gamma$ in the following sense: Fix $\delta>0$. If $n$ is large, then $\left|\alpha_{n}\right| \geq 1-\delta$ at distances greater than $c_{0} r^{-1 / 2}$ from $\bigcup_{(\gamma, m) \in \Theta} \gamma$. Meanwhile, for any given $(\gamma, m) \in \Theta$, the restriction of $\alpha_{n} /\left|\alpha_{n}\right|$ to the boundary of the $\varphi_{\gamma}$ image of a disk $\{\tau\} \times D$ has degree $m$.
\item[-] $\frac{\mathrm{i}}{2 \pi} F_{A}$ converges as a current to $\sum_{(\gamma, m) \in \Theta} m \gamma$.
\end{itemize}
These last conclusions imply that $d_{\Gamma}>0$ if $\Theta \neq\{\emptyset\}$ and thus assertion (1) of Theorem 3.1. If $\Theta=\{\emptyset\}$, these conclusions with Lemma 3.4 imply the uniqueness assertion (2) of Theorem 3.1.

Granted $d_{\Gamma}>0$, then item (3c) of Theorem 3.1 is proved by copying almost verbatim the arguments that are given in Section 2a of [T4]. The latter prove an analog for the case when the one-form a in (3.13) is a contact one-form. This contact condition plays no essential role in the arguments in Section 2a of [T4].

\section*{4. Pseudoholomorphic curves and Seiberg-Witten solutions on $\mathbb{R} \times M$}

Fix a non-degenerate, area-preserving map $f: F \rightarrow F$ so as to construct the manifold $M$, and a monotone class $\Gamma \in H_{1}(M ; \mathbb{Z})$ with $d_{\Gamma}>0$. With $\Gamma$ given, define $\mathcal{Z}$ as in Section 3.2. Fix next a $J \in \mathcal{J}_{1 f}$. By Lemmas 2.1-2.4, we may assume without loss of generality that the pair $(f, J)$ obeys the following constraint: Let $(\gamma, m)$ denote any given element from $\mathcal{Z}$ and let $q$ denote the period of $\gamma$. There is a disk $D \subset \mathbb{C}$ about the origin and a tubular
neighborhood map $\varphi_{\gamma}: S^{1} \times D \rightarrow M$ such that:
$$\left\{\begin{array}{l}
\text { - The curve } \gamma \text { is } \varphi_{\gamma}(\cdot, 0) \text {. } \\
\text { - The vector field } q^{-1} \partial_{t} \text { is the pushforward from } S^{1} \times D \text { of } \\
\quad \partial_{\tau}-2 \mathrm{i}\left(\nu_{\gamma} z+\mu_{\gamma} \bar{z}+\mathfrak{r}\right) \partial_{z}+2 \mathrm{i}\left(\nu_{\gamma} \bar{z}+\bar{\mu} \gamma z+\overline{\mathfrak{r}}\right) \partial_{\bar{z}} \\
\quad \text { where } \quad\left(\nu_{\gamma}, \mu_{\gamma}\right) \text { are given in }(2.1) \text { and where } \mathfrak{r} \text { is zero on a } \\
\text { neighborhood of } S^{1} \times\{0\} \text {. } \\
\text { - The almost complex structure } J \text { is such that } J \cdot \varphi_{\gamma *} \partial_{z}=\varphi_{\gamma *} \mathrm{i} \partial_{z} \\
\text { on the image of a neighborhood of } S^{1} \times\{0\} \text { under } \varphi_{\gamma}
\end{array}\right.$$

Recall from Section 1.1 that $\mathcal{A} \subset \mathcal{Z}$ denotes the subset that consists of those elements $\Theta$ that do not partner hyperbolic integral curves of $\partial_{t}$ with numbers greater than 1. Given (4.1), the following is now a consequence of Lemma 3.2:
$$\left\{\begin{array}{l}
\bullet \mathfrak{C} \Theta^{*}=\mathfrak{C} \Theta \text { for all } \Theta \in \mathcal{Z} . \\
\bullet \mathfrak{C} \Theta \text { is a single point if } \Theta \in \mathcal{A}, \text { and } \mathfrak{C} \Theta=\emptyset \text { otherwise. }
\end{array}\right.$$

Use the almost complex structure $J$ to define the metric on $M$ as done in the preceding section. Use the Spin ${ }^{\mathbb{C}}$-structure on $M$ whose spinor bundle splits as in (3.12) with $c_{1}(E)=e_{\Gamma}$. For $r \geq 1$, let $\mathcal{C}^{r}$ denote the corresponding space of gauge equivalence classes to (3.13). Because of (4.2), all sufficiently large $r$ versions of Theorem 3.1's map $\Phi^{r}$ supply a 1-1 correspondence between the set $\mathcal{A}$ and the set $\mathcal{C}^{r}$.
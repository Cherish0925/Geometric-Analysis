---
retention_scope: session
part: 2
total_parts: 3
---

[Part 2/3 of: [1710.05380] Kähler-Einstein metrics: Old and New - arXiv]

\section*{3. First obstructions to existence of Kähler-Einstein metrics}

In this section, we discuss two obstructions to the existence of Kähler-Einstein metrics:
Matsushima: the automorphisms group of Kähler-Einstein Fano manifolds is reductive (namely, it is the complexification of a maximal compact subgroup);
Futaki: the functional $F$ defined on the space of holomorphic vector fields as in (8) vanishes when there exists a Kähler-Einstein metric.
More in general, these obstructions hold for constant scalar curvature Kähler metric (cscK). Note that, if $\omega \in 2 \pi c_{1}(X)$ is a cscK metric on $X^{n}$ Fano, then $\omega$ is in fact KE. Indeed, by the $\sqrt{-1} \partial \bar{\partial}$ -Lemma, we have that $\operatorname{Ric}(\omega)-\omega=\sqrt{-1} \partial \bar{\partial} f$. Taking trace with the metric, we find that $0=$ $S c(\omega)-n=\Delta_{\omega} f$, i.e. $f$ has to be constant.

We are going to prove the statements in the more general cscK case, since they require only a bit more effort than in the KE case.
3.1. Matsushima-(Lichnerowicz) theorem. On a $\left(X^{n}, g\right)$ Hermitian manifold, we consider the Lie algebra $\mathfrak{h}$ of holomorphic vector fields (that is, real vector fields $V$ such that $\mathcal{L}_{V} J=0$, equivalently, $\left.\bar{\partial} V^{(1,0)}=0\right)$.

We also consider the Lie algebra $\mathfrak{k}_{g}$ of the isometry group $\operatorname{Isom}(X, g)$ (that is, $\mathfrak{k}_{g}$ contains vector fields $V$ such that $\mathcal{L}_{V} g=0$, called Killing vector fields). If $\left(X^{n}, g\right)$ is compact Kähler, then $\mathfrak{k}_{g} \subseteq \mathfrak{h}$, see e.g. [Gau15, Proposition 2.2.1]. Indeed, notice that the associated (1, 1)-form $\omega$ to $g$ is harmonic, e.g. since $d * \omega=\frac{1}{(n-1)!} d \omega^{n-1}=0$. Take any $\psi \in \operatorname{Isom}_{0}(X, g)$, the connected component of the identity. Then $\psi^{*}[\omega]=[\omega]$. By uniqueness of the harmonic representative, $\psi^{*} \omega=\omega$. Thus, we have proven that, for any $V \in \mathfrak{k}_{g}$, it holds $\mathcal{L}_{V} \omega=0$. This, together with $\mathcal{L}_{V} g=0$, gives $\mathcal{L}_{V} J=0$.

We also consider the Lie algebra $\mathfrak{a}_{g}$ of parallel vector fields (that is, $\mathfrak{a}_{g}$ contains vector fields $V$ such that $\nabla V=0$, where ∇ is the Levi-Civita connection of $g$ ). Clearly, $\mathfrak{a}_{g} \subseteq \mathfrak{k}_{g}$ and $\mathfrak{a}_{g}$ is Abelian, since ∇ is torsion-free. If $g$ is Kähler, then $\mathfrak{a}_{g}$ is complex, that is, if $V \in \mathfrak{a}_{g}$ then also $J V \in \mathfrak{a}_{g}$ (just using that $J$ is parallel).

Finally, we consider the space $\mathfrak{h}_{0}$ of holomorphic vector fields with zeroes, consisting of $V \in \mathfrak{h}$ such that $V(p)=0$ at some point $p$, and $\mathfrak{k}_{0}$ the space of Killing vector fields with zeros.

Before stating the next theorem, we recall that the Albanese map [Bla56], also called Jacobi map, associated to a compact Kähler manifold $X^{n}$ is
$$\begin{gathered}
A: X \rightarrow \operatorname{Alb}(X):=H^{0}\left(X ; \Omega_{X}^{1}\right)^{\vee} / H_{1}(X ; \mathbb{Z}) \simeq \mathbb{C}^{h^{1,0}} / \Gamma \\
p \mapsto \int_{p_{0}}^{p}-
\end{gathered}$$
where $p_{0}$ is fixed. It is well defined since any holomorphic form is closed on a compact Kähler manifold. Any morphism from $X$ to a compact complex torus factors uniquely through the Albanese map. It yields an isomorphism
$$A^{*}: H^{0}\left(\operatorname{Alb}(X) ; \Omega_{\operatorname{Alb}(X)}^{1}\right) \stackrel{\simeq}{\rightarrow} H^{0}\left(X ; \Omega_{X}^{1}\right) .$$

We also consider the operator that acts on $f \in \mathcal{C}^{\infty}(X ; \mathbb{C})$ as
$$\partial^{\sharp} f:=\left(\operatorname{grad}_{g} f\right)^{1,0} \stackrel{\operatorname{loc}}{=} g^{i \bar{j}} f_{, \bar{j}} \partial_{z_{i}} .$$

Theorem 3.1 (Matsushima [Mat57], Carrell-Lieberman [CL73], LeBrun-Simanca [LBS94]). Let $\left(X^{n}, \omega\right)$ be a compact Kähler manifold. Then the following properties are equivalent for a holomorphic vector field $Z \in \mathfrak{h}$ :
\begin{itemize}
\item[(i)] $Z \in \mathfrak{h}_{0}$;
\item[(ii)] $Z$ is tangent to the fibres of the Albanese map;
\item[(iii)] $Z=\partial^{\sharp} f$ for some $f \in \mathcal{C}^{\infty}(X ; \mathbb{C})$.
\end{itemize}

Proof. We prove that (i) implies (ii). We want to prove that $Z$ is tangent to the fibres of the Albanese map, equivalently, $\mu(d A(Z))=0$ for any $\mu \in H^{0}\left(\operatorname{Alb}(X), \Omega_{\operatorname{Alb}(X)}^{1}\right)$. By the isomorphism (7), this is equivalent to show that $\eta(Z)=0$ for any $\eta \in H^{0}\left(X, \Omega_{X}^{1}\right)$, where $\eta=A^{*} \mu$. We conclude by noticing that $\eta(Z)$ is a holomorphic function on $X$ compact, then it is constant, in fact, $\eta(Z)=0$ because $Z$ has non-empty zero-set.

We prove that (ii) implies (iii). Define the following (0, 1)-form:
$$\varphi:=\sqrt{-1} \iota_{Z} \omega \stackrel{\text { loc }}{=} \sqrt{-1} Z^{k} g_{k \bar{j}} d \bar{z}^{j} .$$
By the Cartan formula, we have $\mathcal{L}_{\mathrm{Re} Z} \omega=-\sqrt{-1} d \varphi$, where the right-hand side is a (1,1)-form since $Z$ is holomorphic: then $\bar{\partial} \varphi=0$. We now use Hodge theory to construct the potential $f$. Take any $\alpha \in \mathcal{H}_{\omega}^{0,1}$, the space of harmonic (0, 1)-form; set $\beta:=\bar{\alpha}$. Then $(\varphi, \alpha)_{\omega}=g^{k \bar{j}} \varphi_{k} \overline{\alpha_{j}}=\sqrt{-1} Z^{j} \beta_{j}=$ $\sqrt{-1} \beta(Z)=0$ by the assumption that $Z$ is tangent to the fibres of the Albanese map. We have proven that $\varphi \perp \mathcal{H}_{\omega}^{0,1}$. By Hodge theory, we have $\varphi=\bar{\partial} f+\bar{\partial}^{*} h$. But $\left\|\bar{\partial}^{*} h\right\|_{L^{2}}^{2}=\left(\bar{\partial}^{*} h, \bar{\partial}^{*} h\right)_{L^{2}}=$ $(h, \bar{\partial}(\varphi-\bar{\partial} f))_{L^{2}}=0$. So $\varphi=\bar{\partial} f$, and $Z=\partial^{\sharp} f$.

We prove that (iii) implies (i). Take $Z=\partial^{\sharp} f$ holomorphic. (Note that $f$ is complex-valued, and not just real-valued, so we cannot apply the maximum principle directly.) We have that $Z(\bar{f})=g^{i \bar{j}} f_{, \bar{j}} \overline{f_{\overline{, i}}}=|Z|^{2} \geq 0$. Set $c=\min |Z|^{2}>0$ and $C=\max |Z|^{2}$. We have to prove that $c=0$. Fix $p \in X$. Construct $F: \mathbb{C} \rightarrow X^{n}$ with $F(0)=p$ and $d F\left(\frac{d}{d z}\right)=Z$. Define $h:=f \circ F: \mathbb{C} \rightarrow \mathbb{C}$. We have $0 \leq|h| \leq C$ and $\frac{d \bar{h}}{d z_{j}}=Z(\bar{f}) \geq c$. Apply the Stokes theorem to a disk $\Delta_{r}$ of radius $r>0$. We have $\frac{1}{2 \pi} \int_{0}^{2 \pi} h(r \exp (\sqrt{-1} \vartheta)) \exp (\sqrt{-1} \vartheta) d \vartheta=\frac{1}{2 \pi r} \int_{\partial \Delta_{r}} h d z=\frac{2 \sqrt{-1}}{8 \pi r} \int \frac{d \bar{h}}{d z} d x d y \geq c r$. Letting $r \rightarrow+\infty$ we see that $c=0$, since the first integral is clearly bounded. \(\square\)

Remark 3.2. - When $X^{n}$ is Fano, then $\mathfrak{h}=\mathfrak{h}_{0}$ (this follows either by $\operatorname{Alb}(X)$ being trivial by the vanishing result, or because $X$ is simply-connected).
\begin{itemize}
\item[-] $\mathfrak{h}_{0}$ is an ideal in $\mathfrak{h}$ when the manifold is Kähler, but there are counterexamples in the non-Kähler case where it is not a linear subspace (consider for example the Hopf surface $\mathbb{C}^{2} \backslash 0 /$ $\langle z \mapsto 2 z\rangle$, with local coordinates $(z, w) \in \mathbb{C}^{2}$, then both $v=z \partial_{z} \in \mathfrak{h}_{0}$ and $t=w \partial_{w} \in \mathfrak{h}_{0}$, but $v+t \notin \mathfrak{h}_{0}$ ).
\end{itemize}

Cleraly $Z=\partial^{\sharp} f$ is holomorphic if and only if $f \in \operatorname{ker}\left(\bar{\partial} \partial^{\sharp}\right)^{*} \bar{\partial} \partial^{\sharp}$. Such fourth order operator is called Lichnerowicz operator and by a (slightly tedious) computation can be show to be equal to
$$\mathbb{L}_{\omega}(\varphi):=\Delta_{\omega}^{2} \varphi+(\operatorname{Ric}(\omega), \partial \bar{\partial} \varphi)_{\omega}+\partial^{\sharp} \varphi\left(\operatorname{Sc}_{\omega}\right),$$
see e.g. [Szé14, page 59], [Gau15, page 63, Proposition 2.6.1].
In general, $\mathbb{L}_{\omega}$ is not a real operator, that is, $\overline{\mathbb{L}_{\omega}(\varphi)} \neq \mathbb{L}_{\omega}(\bar{\varphi})$. We will define the complex conjugate
$$\tilde{\mathbb{L}}_{\omega}(\varphi):=\overline{\mathbb{L}_{\omega}(\bar{\varphi})} .$$
We have $\tilde{\mathbb{L}}_{\omega}(\varphi)-\mathbb{L}_{\omega}(\varphi)=\partial^{\sharp} \varphi\left(\mathrm{Sc}_{\omega}\right)-\bar{\partial}^{\sharp} \bar{\varphi}\left(\mathrm{Sc}_{\omega}\right)$.
Proposition 3.3. Let $\left(X^{n}, \omega\right)$ be a compact Kähler manifold. Then the space of Killing vector fields with zeroes is given by
$$\mathfrak{k}_{0}=\left\{\operatorname{Jgrad}_{g} f: f \in \mathcal{C}^{\infty}(X ; \mathbb{R}) \text { such that } \partial^{\sharp} f \in \mathfrak{h}_{0}\right\} \text {. }$$
Proof. The inclusion " $\supseteq$ " follows since $J_{\operatorname{grad}_{g}} f$ is a real holomorphic vector field being also Hamiltonian, whence it is Killing. The inclusion " $\subseteq$ " is as follows. Take $X \in \mathfrak{k}_{0}$. Then $J X \in \mathfrak{h}_{0}$. Consider $Z=J X+\sqrt{-1} X$ with $\bar{\partial} Z=0$. We know that $Z=\partial^{\sharp} f$ where $f \in \mathcal{C}^{\infty}(X ; \mathbb{C})$, say $f=u+\sqrt{-1} v$. Then $\operatorname{Re} \partial^{\sharp} f=\operatorname{grad}_{g} u+J \operatorname{grad}_{g} v$. Then $X=-\operatorname{grad}_{g} v+J \operatorname{grad}_{g} u$. We claim that $\operatorname{grad}_{g} v=0$. By Cartan, $0=\mathcal{L}_{X} \omega=d \iota_{-\operatorname{grad}_{g} v+J \operatorname{grad}_{g} u}(\omega)=d g\left(-J \operatorname{grad}_{g} v, \_\right)-d\left(g\left(\operatorname{grad}_{g} u, \_\right)\right)=d J d v=$ $2 \sqrt{-1} \partial \bar{\partial} v$. Since $X$ is compact, then $v$ is constant. \(\square\)

Theorem 3.4 (Matsushima [Mat57], Lichnerowicz [Lic58]). Let $\omega$ be a cscK metric on $X^{n}$ compact complex manifold. Then
$$\mathfrak{h}_{0}=\mathfrak{k}_{0} \oplus J \mathfrak{k}_{0} .$$
Proof. Clearly, $\mathfrak{k}_{0} \oplus J \mathfrak{k}_{0} \subseteq \mathfrak{h}_{0}$. Take $Z=\partial^{\sharp} f$ with $\mathbb{L}_{\omega}(f)=0$. Since $\omega$ is $\operatorname{cscK}$, then $\mathbb{L}=\tilde{\mathbb{L}}_{\omega}$ is a real operator. Then $\mathbb{L}_{\omega}(\operatorname{Re} f)=\mathbb{L}_{\omega}(\operatorname{Im} f)=0$. Then we can conclude by the previous proposition. (See also e.g. [Gau15, Theorems 3.6.1-2], [Szé14, Proposition 4.18]). \(\square\)

Remark 3.5. By Bochner [Boc46], if $V$ is Killing, then $\frac{1}{2} \Delta_{g}|V|^{2}=-\operatorname{Ric}(g)(V, V)+|\nabla V|^{2}$. Thus:
\begin{itemize}
\item[-] if $\operatorname{Ric}(\omega)=0$, then $\mathfrak{h}=\mathfrak{a}$;
\item[-] if $\operatorname{Ric}(\omega)=-\omega$, then $\mathfrak{h}=0$.
\end{itemize}

Remark 3.6. Recall that $\operatorname{Isom}(M, g)$ is always a compact Lie group [MS39]. In particular, $\mathfrak{h}_{0}$ is reductive.

Example 3.7. Consider $\hat{X}^{2}=\mathrm{Bl}_{p} \mathbb{C P}^{2}$, that is, locally on $U \ni p$, it is $\hat{X} \stackrel{\text { loc }}{=}\{((z, w),[u: v]) \in$ $\left.U \times \mathbb{C P}^{1}: z v-w u=0\right\}$. We have $K_{\hat{X}}=\pi^{*} K_{\mathbb{C P}^{2}} \otimes \mathcal{O}(E)$, where $E \simeq \mathbb{C P}^{1}$ is the exceptional divisor. $K_{\hat{X}}^{-1}$ is still ample. Then
$$\operatorname{Aut}(\hat{X})=\left\{\left(\begin{array}{lll}
\star & \star & \star \\
0 & \star & \star \\
0 & \star & \star
\end{array}\right)\right\} / \mathbb{C}^{*}$$
and
$$\mathfrak{h}(\hat{X})=\left\{\left(\begin{array}{ccc}
0 & \star & \star \\
0 & \star & \star \\
0 & \star & \star
\end{array}\right)\right\} \simeq \mathfrak{g} \mathfrak{l}(2 ; \mathbb{C}) \oplus \mathbb{C}^{2}$$
which cannot be given by a complexification of a compact Lie group. Then, by the Matsushima-Lichnerowicz theorem, $\hat{X}$ is an example of a Fano manifold that does not admit cscK metric, in particular, does not admit Kähler-Einstein metrics.

Even if the blow-up in a point of $\mathbb{C P}^{2}$ is not KE, such space is related to two important (positive) Einstein metrics.
\begin{itemize}
\item[-] The Page metric [Pag79] (see e.g. [Bes87, 9.125]) constructed as $g_{P}=\mathrm{Sc}_{\text {extr }}^{-2} g_{\text {extr }}$ where $g_{\text {extr }}$ is the explicit Calabi's extremal metric (that is, with holomorphic grandient of the scalar curvature) in $2 \pi c_{1}(X)$.
\item[-] The $Y^{2,1}$ irregular Sasaki-Einstein metric constructed on the smooth bundle $S^{1} \hookrightarrow K \rightarrow$ $\mathrm{Bl}_{p} \mathbb{C P}^{2}$ by deforming the natural $\mathbb{C}^{*}$-action. This metric was first constructed by physicists studying the AdS-CFT correspondence [MS06].
\end{itemize}
3.2. Futaki invariant. Let $\left(X^{n}, \omega\right)$ be a compact Kähler metric. Set $\hat{S}$ the value of the eventual constant scalar curvature of some metric in $[\omega]$. Note that $\hat{S}$ is a cohomological invariant depending just on $c_{1}(X)$ and $[\omega]$, determined by
$$[\omega]^{n} \hat{S}=\int_{X} \mathrm{Sc}_{\omega} \omega^{n}=n \int_{X} \operatorname{Ric}(\omega) \wedge \omega^{n-1}=2 \pi n c_{1}(X) \cdot[\omega]^{n-1} .$$
For $Z=\partial^{\sharp} f$, define
$$F(Z, \omega):=\int_{X} f\left(\mathrm{Sc}_{\omega}-\hat{S}\right) \omega^{n} .$$

Theorem 3.8 (Futaki [Fut83]). If $\omega$ and $\omega^{\prime}$ are cohomologous, then $F(Z, \omega)=F\left(Z, \omega^{\prime}\right)$. Therefore $F(Z, \omega)=F(Z,[\omega])$. In particular, if there exists $\omega^{\prime} \in[\omega] \csc K$, then $F=0$.

Proof. Note that the space of Kähler metrics in $[\omega]$ is connected. Take $\left(\omega_{t}\right)_{t}$ a path of metrics in $[\omega]$, for example of the form $\omega_{t}=\omega+\sqrt{-1} \partial \bar{\partial}(t \varphi)$. We show that $\dot{F}\left(Z, \omega_{t}\right):=\frac{d}{d t}\left\lfloor_{t=0} F\left(Z, \omega_{t}\right)=0\right.$. We compute:
\begin{itemize}
\item[-] $\dot{f}_{t}=\partial^{\sharp} f(\varphi)$ :
Indeed, $\bar{\partial} \dot{f}_{t}=\bar{\partial}\left(Z^{j} \varphi_{, j}\right)$ since $Z$ is holomorphic;
\item[-] $\dot{\mathrm{Sc}}_{\omega_{t}}=-\tilde{\mathbb{L}}_{\omega}(\varphi)+\partial^{\sharp} \operatorname{Sc}_{\omega}(\varphi)$ :
indeed, $\operatorname{Ric}\left(\omega_{t}\right)=\operatorname{Ric}(\omega)-\sqrt{-1} t \partial \bar{\partial} \Delta \varphi+o(t)$, then $\operatorname{Sc}_{\omega_{t}}=g_{t}^{i \bar{j}}\left(\operatorname{Ric}\left(\omega_{t}\right)\right)_{i \bar{j}}=\left(g^{i \bar{j}}-t g^{i \bar{\ell}} g^{k \bar{j}} \varphi_{, k \bar{\ell}}\right)\left(\operatorname{Ric}_{i \bar{j}}-\right.$ $\left.t(\Delta \varphi)_{, i \bar{j}}\right)+o(t)=\mathrm{Sc}_{\omega}-t \Delta^{2} \varphi-t g^{i \bar{\ell}} g^{k \bar{j}} \varphi_{, k \bar{\ell}} \mathrm{Ric}_{i \bar{j}}+o(t)=\mathrm{Sc}_{\omega}-t \tilde{\mathbb{L}}_{\omega}+t \partial^{\sharp} \mathrm{Sc}_{\omega}(\varphi)+o(t)$;
\item[-] $\dot{\omega}_{t}^{n}=\Delta \varphi \omega^{n}$.
\end{itemize}

Thus
$$\begin{aligned}
\dot{F}_{t} & =\int_{X}\left(\partial^{\sharp} f(\varphi)\left(\mathrm{Sc}_{\omega}-\hat{S}\right)-f \overline{\mathbb{L}}_{\omega}(\varphi)+f \partial^{\sharp} \mathrm{Sc}_{\omega}(\varphi)+f(\operatorname{Sc}(\omega)-\hat{S}) \Delta \varphi\right) \omega^{n} \\
& =-\int_{X} f \overline{\mathbb{L}}_{\omega}(\varphi) \omega^{n}=-\left(f, \mathbb{L}_{\omega}(\varphi)\right)_{L^{2}} \\
& =-\left(\mathbb{L}_{\omega}(f), \varphi\right)_{L^{2}}=0,
\end{aligned}$$
by integrating by part and by using that $\mathbb{L}_{\omega}(f)=0$, since $f$ is holomorphic. \(\square\)

The Futaki invariant will be central in the definition of the notion of K-stability, see Section 5.1.
Remark 3.9 (Other equivalent formulations of the Futaki invariant). Let $\psi$ a solution of $\mathrm{Sc}_{\omega}-\hat{S}=$ $\Delta_{\omega} \psi$, so, for $Z=\partial^{\sharp} f$, we have
$$\begin{aligned}
F(Z,[\omega]) & =\int_{X} f(\operatorname{Sc}(\omega)-\hat{S}) \omega^{n} \\
& =\left(f, \bar{\partial}^{*} \bar{\partial} \psi\right)=(\bar{\partial} f, \bar{\partial} \psi) \\
& =\int_{X} \partial^{\sharp} f(\psi)=\int_{X} Z(\psi) \omega^{n}
\end{aligned}$$
so that we can write
$$F(Z,[\omega])=\int_{X} Z(\psi) \omega^{n}$$
3.3. Mabuchi functional and evidences for uniqueness. On the space $\mathcal{K}_{[\omega]}=\left\{\varphi: \omega_{\varphi}:=\right.$ $\omega+\sqrt{-1} \partial \bar{\partial} \varphi>0\}$ of Kähler metrics in [ $\omega$ ], consider the following 1-form:
$$\alpha_{\varphi}(\psi):=\int_{X} \psi\left(\hat{S}-\operatorname{Sc}_{\omega_{\varphi}}\right) \omega_{\varphi}^{n} .$$

We compute
$$\begin{aligned}
\frac{d}{d t}\left(\alpha_{\varphi+t \psi_{2}}\left(\psi_{1}\right)\right) & =\int\left(\psi_{1}\left(\mathbb{L}_{\omega_{\varphi}} \psi_{2}-\partial^{\sharp} \psi_{2}\left(\mathrm{Sc}_{\omega_{\varphi}}\right)\right)+\psi_{1}\left(\hat{S}-\mathrm{Sc}_{\omega_{\varphi}}\right) \Delta_{\omega_{\varphi}} \psi_{2}\right) \omega_{\varphi}^{n} \\
& =\int_{X}\left(\psi_{1} \mathbb{L}_{\omega_{\varphi}} \psi_{2}-\left(\hat{S}-\mathrm{Sc}_{\omega_{\varphi}}\right) \partial^{\sharp} \psi_{1}\left(\psi_{2}\right)\right)
\end{aligned}$$
which is symmetric in $\psi_{1}$ and $\psi_{2}$, since they are both real. Then
$$d \alpha=0 .$$
Then there exists $\mathcal{M}: \mathcal{K}_{[\omega]} \rightarrow \mathbb{R}$ such that
$$\alpha=d \mathcal{M} .$$
Such $\mathcal{M}$ is called Mabuchi K-energy. (See also e.g. [Gau15, Section 4.10], [Szé14, Proposition 4.23].)

The Mabuchi metric [Mab87, Sem92, Don99] on $\mathcal{K}_{[\omega]}$ is defined as
$$\left\langle\psi_{1}, \psi_{2}\right\rangle_{\varphi}:=\int_{X} \psi_{1} \psi_{2} \omega_{\varphi}^{n} .$$
We look at the geodesics for such metric: let $\left(\varphi_{t}\right)_{t}$ a path in $\mathcal{K}_{[\omega]}$ connecting $\varphi_{0}=0$ and $\varphi_{1}=\varphi$, and consider the energy functional
$$E(\varphi)=\int_{0}^{1} \int_{X} \dot{\varphi}_{t}^{2} \omega_{\varphi_{t}}^{n} d t$$

We look at geodesics, that is, critical point of $E$. We compute
$$\left.\frac{d}{d s}\right|_{s=0} E(\varphi+s \psi)=\int_{0}^{1} \int_{X}-2 \psi_{t}\left(\ddot{\varphi}_{t}-\partial^{\sharp} \dot{\varphi}_{t}\left(\dot{\varphi}_{t}\right)\right) \omega_{\varphi_{t}}^{n}$$
so the geodesic equation is
$$\ddot{\varphi}_{t}-\left|\partial \dot{\varphi}_{t}\right|_{\omega_{\varphi_{t}}}^{2}=0 .$$
Remark 3.10. Consider now $\hat{X}=X \times[0,1] \times \mathbb{S}^{1}$. Donaldson [Don99] and Semmes [Sem92] observed that, by extending
$$\Phi(p, t, s):=\varphi_{t}(p)$$
then the geodesic equation can be given as
$$\left(\omega_{0}+\sqrt{-1} \partial \bar{\partial} \phi\right)^{n+1}=0$$
on $\hat{X}$, from which one can use pluripotential theory to study geodesics [Che00].
Lemma 3.11. The Mabuchi functional is convex along smooth geodesics.
Proof. Let $\left(\varphi_{t}\right)_{t}$ be a geodesic. We compute
$$\begin{aligned}
\frac{d^{2}}{d t^{2}} \mathcal{M}\left(\varphi_{t}\right) & =\frac{d}{d t} \int_{X} \dot{\varphi}_{t}\left(\hat{S}-\operatorname{Sc}_{\omega_{\varphi_{t}}}\right) \omega_{\varphi_{t}}^{n} \\
& =\int_{X}\left(\ddot{\varphi}_{t}\left(\hat{S}-\operatorname{Sc}_{\omega_{\varphi_{t}}}\right)+\dot{\varphi}_{t}\left(\mathbb{L}_{\omega}\left(\varphi_{t}\right)-\partial^{\sharp} \varphi_{t}\left(\operatorname{Sc}_{\omega_{\varphi_{t}}}\right)\right)+\dot{\varphi}_{t}\left(\hat{S}-\operatorname{Sc}_{\omega_{\varphi_{t}}}\right) \Delta_{\omega_{\varphi_{t}}} \dot{\varphi}_{t}\right) \omega_{\omega_{\varphi_{t}}}^{n} \\
& =\int_{X}\left(\left|\bar{\partial} \partial^{\sharp} \dot{\varphi}_{t}\right|_{\omega_{\varphi_{t}}}^{2}+\left(\hat{S}-\operatorname{Sc}_{\omega_{\varphi_{t}}}\right)\left(\ddot{\varphi}_{t}-\left|\partial \dot{\varphi}_{t}\right|^{2}\right)\right) \omega_{\omega_{\varphi_{t}}}^{n} \\
& =\int\left|\bar{\partial} \partial^{\sharp} \dot{\varphi}_{t}\right|_{\omega_{\varphi_{t}}}^{2} \omega_{\omega_{\varphi_{t}}}^{n} \geq 0 .
\end{aligned}$$ \(\square\)

Now, assume that any $\varphi_{1}, \varphi_{2}$ can be connected by smooth geodesics [Don99]. The previous result would then yield uniqueness of cscK metrics. Indeed, if there existed two cscK metrics, by convexity we get that $\bar{\partial} \partial^{\sharp} \varphi_{t}=0$, and then there exists $F$ automorphism such that $F^{*} \omega_{2}=\omega_{1}$ (i.e. the metric would be unique up to automorphisms). But the assumption on the regularity of geodesics is false: the optimal regularity is $C^{1,1}$ as proven by [DL12], which follows previous works [Don02a, LV13]. In any case, such approach turned out to be the correct one, at the price of working with weaker regularity [CTW17, BB17]. In the KE Fano case, the first proof of uniqueness (up to automorphisms) was given by Bando and Mabuchi with different techniques [BM87].

\section*{4. A criterion for the existence of Kähler-Einstein metrics on Fano manifolds}

We try to construct a Kähler-Einstein metric in $2 \pi c_{1}(X)>0$, i.e., $\operatorname{Ric}(\omega)=\omega$. This is equivalent to solve the Monge-Ampère (2) with $\lambda=1$, namely, the equation
$$\omega_{\varphi}^{n}=\exp (f-\varphi) \omega^{n}$$
for $\omega_{\varphi}:=\omega+\sqrt{-1} \partial \bar{\partial} \varphi>0$, where $f$ is the Ricci potential normalized such that $f_{X} \exp f \omega^{n}=1$.
We set up the continuity method along the Aubin path
$$\omega_{\varphi_{t}}^{n}=\exp (f-t \varphi) \omega^{n}$$
varying $t \in[0,1]$. This equation is equivalent to asking
$$\operatorname{Ric}\left(\omega_{\varphi_{t}}\right)=(1-t) \omega+t \omega_{\varphi_{t}} \geq t \omega_{\varphi_{t}}>0,$$

Note that we (crucially!) get a lower bound on the Ricci curvature along the path.
Remark 4.1. Define the Székelyhidi invariant [Tia92, Szé11] of ( $X^{n}, \omega$ ) as
$$R(X):=\sup \left\{t \in[0,1]: \operatorname{Ric}\left(\omega_{\varphi_{t}}\right) \geq t \omega_{t}\right\} \in(0,1],$$
where $\left(\omega_{t}\right)_{t}$ is the Aubin path starting at the background metric $\omega$. In fact, $R(X)$ does not depend on the background $\omega$ [Szé11, Theorem 1]. For example, $R\left(\mathrm{Bl}_{p} \mathbb{C P}^{2}\right)=\frac{6}{7}$. Explicit computations for toric manifolds can be found in [Li11]. It was conjectured [Szé11, Conjecture 13] that $R(X)=1$ if and only if $K$-semi-stable. Such conjecture has been proven by C. Li [Li15b].

Solution for $t=0$ the solvability of the Aubin's path follows by first Calabi's conjecture, Theorem 2.1. Openness is studies by means of the linearization
$$D \mathcal{E}\left(\_, t\right)=\Delta_{\omega_{\varphi_{t}}}+t,$$
with the same notation as at page 12. It is relative easy to show that the first eigenvalue of the Laplacians satisfies $-\lambda_{1}(t) \geq t$, with equality only for $t=1$ see e.g. [Tia00, Remark 6.13]. Thus we have that the kernel is trivial for $t \in(0,1)$. For $t=1$, we have that the kernel is given by holomorphic vector fields with zeros.
4.1. Some a priori estimates. The Laplacian and higher order estimates can be repeated. We study now the $\mathcal{C}^{0}$-estimates, which we know they would fail in general, but we can hope to find some sufficient condition for them to hold.

On $\left(X^{n}, \omega\right)$ compact Kähler manifold, set $\omega_{\varphi}:=\omega+\sqrt{-1} \partial \bar{\partial} \varphi$, and consider the functional
$$I_{\omega}(\varphi)=f_{X} \varphi\left(\omega^{n}-\omega_{\varphi}^{n}\right) .$$
We have $I_{\omega}(\varphi) \geq 0$. In fact, $I_{\omega}$ is equivalent to the generalized energy functional
$$J_{\omega}(\varphi):=\sqrt{-1} \sum_{k=0}^{n-1} \frac{k+1}{n+1} f_{X} \partial \varphi \wedge \bar{\partial} \varphi \wedge \omega^{k} \wedge \omega_{\varphi}^{n-k} \geq 0 .$$
More precisely, [Tian87, Lemma 2.2],
$$\frac{1}{n+1} I_{\omega}(\varphi) \leq J_{\omega}(\varphi) \leq \frac{n}{n+1} I_{\omega}(\varphi) .$$

Theorem 4.2 (Tian [Tian87]). Let $\left(X^{n}, \omega\right)$ be a compact Fano Kähler manifold. Along the Aubin path $\left\{\omega_{\varphi_{t}}:=\omega+\sqrt{-1} \partial \bar{\partial} \varphi_{t}\right\}_{t \in[0,1]}$, we have the a priori estimates
$$\left\|\varphi_{t}\right\|_{L^{\infty}} \leq C_{t}\left(1+I_{\omega}\left(\varphi_{t}\right)\right),$$
with $C_{t} \leq C(\epsilon)$ for all $t>\epsilon$ for any chosen $\epsilon>0$.
Proof. The equation for the Aubin path yields $f_{X} \exp (t \varphi) \omega_{\varphi}^{n}=f_{X} \exp f \omega^{n}=1$, where recall that $f$ is the Ricci potential of $\omega$ with the normalization above. It follows that $\inf \varphi \leq 0$ and $\sup \varphi \geq 0$. We claim that
$$\|\varphi\|_{L^{\infty}} \leq \operatorname{osc} \varphi:=\sup \varphi-\inf \varphi \leq C_{t}\left(1+I_{\omega}\left(\varphi_{t}\right)\right) .$$

As for $\sup \varphi$, an estimate follows by using the Green function as for first Calabi's conjecture:
$$\sup \varphi \leq C\left(1+f_{X} \varphi_{t} \omega^{n}\right) .$$
Indeed, if $G$ is the Green function such that $G \geq 0$, then write $\varphi(x)=f_{X} \varphi \omega^{n}+f-\Delta_{\omega} \varphi G\left(x, \_\right) \omega^{n} \leq$ $C\left(1+f_{X} \varphi \omega^{n}\right)$ since $-\Delta_{\omega} \varphi \leq n$.

We prove now an estimate for $\inf \varphi$. Take $1 \leq \tilde{\varphi}_{t}:=\max \left\{1,-\varphi_{t}\right\}$. Note that $\tilde{\varphi}_{t}^{n}\left(n-\Delta_{\omega_{\varphi_{t}}} \varphi_{t}\right) \geq 0$, and then integrate on $X$ with respect to the moving metric $\omega_{\varphi_{t}}$ to get
$$f_{X}\left|\nabla_{\omega_{\varphi_{t}}}\left(\tilde{\varphi}_{t}\right)^{\frac{p+1}{2}}\right| \omega_{\varphi_{t}}^{n} \leq C(p, n) f_{X} \tilde{\varphi}^{\frac{p+1}{2}} \omega_{\varphi_{t}}^{n} .$$
Use the Sobolev embedding with respect to $\omega_{\varphi_{t}}^{n}$. Since $\operatorname{Ric}\left(\omega_{\varphi_{t}}\right) \geq t$, then we can take a Sobolev constant that depends only on $C$ and $n$. Then, by Moser's iteration, and using the recalled first eigenvalue estimate:
$$\begin{aligned}
\sup \tilde{\varphi}_{t} & \leq\left\|\tilde{\varphi}_{t}\right\|_{L^{2}} \leq \frac{C}{t}\left(\left\|\tilde{\varphi}_{t}\right\|_{L^{1}}+1\right) \\
& \leq \frac{C}{t}\left(1-f_{X} \varphi_{t} \omega_{\varphi_{t}}^{n}\right)
\end{aligned}$$
where the second inequality follows by the Poincaré inequality. At the end, we get
$$\left\|\varphi_{t}\right\|_{L^{\infty}} \leq \sup \varphi_{t}-\inf \varphi_{t} \leq C\left(1+f_{X} \varphi_{t} \omega^{n}\right)+\frac{C}{t}\left(1-f_{X} \varphi_{t} \omega_{\varphi_{t}}^{n}\right),$$
proving the statement. See also e.g. [Tia00, Lemma 6.19]. \(\square\)

Definition 4.3 (Tian's properness [Tian87]). Let $\left(X^{n}, \omega\right)$ be a compact Kähler manifold. Consider the space $\mathcal{K}_{[\omega]}$ of Kähler metrics in the Kähler class [ $\omega$ ]. A functional $F_{\omega}$ on $\mathcal{K}_{[\omega]}$ is called proper if
$$F_{\omega}(\varphi) \geq f\left(I_{\omega}(\varphi)\right)$$
for some $f(t)$ increasing function as $t \rightarrow+\infty$.
We take the Mabuchi functional $\mathcal{M}_{\omega}$. Recall that it is the primitive of the closed 1-form $\alpha(\psi)=$ $\left(\psi, \mathrm{Sc}_{\omega_{\varphi}}-\hat{S}\right)_{L_{\omega \varphi}^{2}}$, and it can be expressed as, see e.g. [Tia00, page 95],
$$\mathcal{M}_{\omega}(\varphi)=f_{X} \log \frac{\omega_{\varphi}^{n}}{\omega^{n}} \omega_{\varphi}^{n}+f_{X}\left(f\left(\omega^{n}-\omega_{\varphi}^{n}\right)-\left(I_{\omega}-J_{\omega}\right)(\varphi)\right),$$
where $f$ is the Ricci potential of $\omega$. Here the first integral represents the "entropy" and the second integral is the "energy".

Theorem 4.4 (Tian). Let $\left(X^{n}, \omega\right)$ be a compact Fano Kähler manifold. If the Mabuchi functional $\mathcal{M}_{\omega}$ is proper, then there exists a Kähler-Einstein metric.

Proof. Let $\varphi_{t}$ a solution of (10). We compute
$$\begin{aligned}
\frac{d}{d t} \mathcal{M}_{\omega}\left(\varphi_{t}\right) & =-\frac{d}{d t} f_{X} t \varphi_{t} \omega_{\varphi_{t}}^{n}-\frac{d}{d t}\left(I_{\omega}-J_{\omega}\right)\left(\varphi_{t}\right) \\
& =-f_{X} \varphi_{t} \omega_{\varphi_{t}}^{n}-t f_{X} \dot{\varphi}_{t} \omega_{\varphi_{t}}^{n}-t f \varphi_{t} \Delta_{\omega_{\varphi_{t}}} \dot{\varphi}_{t} \omega_{\varphi_{t}}^{n}-\frac{d}{d t}\left(I_{\omega}-J_{\omega}\right)\left(\varphi_{t}\right) \\
& =f_{X} \Delta_{\omega_{\varphi_{t}}} \dot{\varphi}_{t} \omega_{\varphi_{t}}^{n}-t f_{X} \varphi_{t} \Delta_{\omega_{\varphi_{t}}} \dot{\varphi}_{t} \omega_{\varphi_{t}}^{n}-\frac{d}{d t}\left(I_{\omega}-J_{\omega}\right)\left(\varphi_{t}\right) \\
& =-t f_{X} \varphi_{t} \Delta_{\omega_{\varphi_{t}}} \dot{\varphi}_{t} \omega_{\varphi_{t}}^{n}-\frac{d}{d t}\left(I_{\omega}-J_{\omega}\right)\left(\varphi_{t}\right)
\end{aligned}$$
where we are using that $\Delta_{\omega_{\varphi_{t}}} \dot{\varphi}_{t}=-\varphi_{t}-t \dot{\varphi}_{t}$ as follows by differentiating the equation. By the equation, we compute
$$\frac{d}{d t}\left(I_{\omega}-J_{\omega}\right)\left(\varphi_{t}\right)=-f_{X} \varphi_{t} \Delta_{\omega_{\varphi_{t}}} \dot{\varphi}_{t} \omega_{\varphi_{t}}^{n}$$
$$=f_{X}\left(\Delta_{\omega_{\varphi_{t}}} \dot{\varphi}_{t}+t \dot{\varphi}_{t}\right) \Delta_{\omega_{\varphi_{t}}} \dot{\varphi}_{t} \geq 0 .$$
At the end, we get
$$\frac{d}{d t} \mathcal{M}_{\omega}\left(\varphi_{t}\right)=-(1-t) \frac{d}{d t}\left(I_{\omega}-J_{\omega}\right)\left(\varphi_{t}\right) \leq 0$$
If we assume that $\mathcal{M}_{\omega}$ is proper, then $I_{\omega}-J_{\omega}$ is bounded along the Aubin path. Then, by Theorem 4.2, we get $\left\|\varphi_{t}\right\|_{L^{\infty}} \leq C$. (See also e.g. [Tia00, Theorem 7.13].) \(\square\)

Remark 4.5. It is proven by Tian in [Tia97] that for manifold with discrete automorphism also the viceversa of the above Theorem holds. This was used for proving that there exists a Fano threefold with no holomorphic vector fields which has no KE metric (the famous deformation of the Mukai-Umemura manifold [Tia97, Section 7]). This result was crucial for the understanding of the relations between existence of KE metrics and stability conditions, and it sees in the work of Berman we will describe in the last lecture its ultimate incarnation.
4.2. $\alpha$-invariant criterion. For a compact Kähler manifold ( $X^{n}, \omega$ ), define the $\alpha$-invariant [Tian87] as
$$\begin{aligned}
\alpha(X):= & \sup \left\{\alpha>0: \text { there exists } C_{\alpha}\right. \text { such that, } \\
& \text { for any } \omega+\sqrt{-1} \partial \bar{\partial} \varphi>0, \\
& \text { it holds } \left.f_{X} \exp (-\alpha(\varphi-\sup \varphi)) d V_{g} \leq C_{\alpha}\right\} .
\end{aligned}$$
where $d V_{g}$ is any smooth volume form.
Theorem 4.6 (Tian [Tian87, Theorem 2.1]). Let $\left(X^{n}, \omega\right)$ be a compact Fano Kähler manifold. If $\alpha(X)>\frac{n}{n+1}$, then there exists a Kähler-Einstein metric.
Proof. Let $\alpha<\alpha(X)$ be such that the condition in (11) holds. By definition, there exists $C_{\alpha}$ such that, for any $\omega+\sqrt{-1} \partial \bar{\partial} \varphi>0$,
$$\begin{aligned}
\log C_{\alpha} & \geq \log f_{X} \exp (-\alpha(\varphi-\sup \varphi)) \exp f \omega^{n} \\
& =\log f_{X} \exp \left(-\alpha(\varphi-\sup \varphi)-\log \frac{\omega_{\varphi}^{n}}{\omega^{n}}+f\right) \omega_{\varphi}^{n} \\
& \geq-f_{X} \log \frac{\omega_{\varphi}^{n}}{\omega^{n}} \omega_{\varphi}^{n}+\alpha\left(\sup \varphi-f_{X} \varphi \omega_{\varphi}^{n}\right) \\
& \geq-f_{X} \log \frac{\omega_{\varphi}^{n}}{\omega^{n}} \omega_{\varphi}^{n}+\alpha I_{\omega}(\varphi)
\end{aligned}$$
So we have
$$\begin{aligned}
\mathcal{M}_{\omega}(\varphi) & \geq-\left(I_{\omega}-J_{\omega}\right)(\varphi)+\alpha I_{\omega}(\varphi)-C_{\alpha}^{\prime} \\
& \geq\left(\alpha-\frac{n}{n+1}\right) I_{\omega}(\varphi)-C_{\alpha}^{\prime \prime}
\end{aligned}$$
which proves that the Mabuchi functional is proper. The conclusion follows by Theorem 4.4. \(\square\)

Remark 4.7. The same result holds by considering the action of a finite group $G$ : one can define an invariant $\alpha_{G}$, and if $\alpha_{G}>\frac{n}{n+1}$, then there exists a $G$-invariant Kähler-Einstein metric [Tian87, Theorem 4.1].
Remark 4.8. If $\alpha=\frac{n}{n+1}$, then Fujita [Fuj16b] proved $K$-stability. The existence of a KE metrics follows by the crucial result of [CDS15] we will describe in the last lecture.

Remark 4.9. Demailly (see appendix of [CS08]) identified $\alpha(X)=\operatorname{glct}(X)$ as the global log canonical threshold. It is defined as
$$\begin{aligned}
\operatorname{glct}(X):= & \sup \{\lambda>0:(X, \lambda D) \text { is log -canonical } \\
& \text { for all } D \text { effective } \mathbb{Q} \text {-divisor with } D^{\prime} \sim_{\mathbb{Q}}-K_{X}, \\
& \text { i.e. } \left.D \in\left|-m K_{X}\right| \text { such that } D=\frac{1}{m} D^{\prime}\right\}
\end{aligned}$$
The point is that, for $D=s_{D}^{-1}(0) \in\left|-m K_{X}\right|$, then $\eta=\frac{1}{m} \log \left|s_{D}\right|^{2}$ is a singular metric in $c_{1}(X)$ that can be used (by Demailly's approximation) to estimate the alpha invariant.

For example, Chetsov [Che08] computed the $\alpha$-invariant for Del Pezzo surfaces, i.e. two dimensional Fanos, of degree $c_{1}^{2}(X)=1$ (which have small anticanonical linear system): if there are no anti-canonical curves with cusps, then $\alpha(X)=1$; if there are cusps, then $\alpha(X)=\frac{5}{6}$, which still satisfies the criterion for existence of KE metrics.

\section*{5. Towards K-stability}

We are aimed at the Yau-Tian-Donaldson conjecture on existence of Kähler-Einstein metrics in the Fano case Theorem 0.3, which gives equivalence between the existence of KE metrics on Fano manifolds and the algebraic geometric notion of K-polystability.

Now some reasons why we should expect something as Theorem 0.3.
\begin{itemize}
\item[-] Historical: The problem is the analogous in the case of varieties of the problem of equipping vector bundles with Hermitian-Einstein metrics. This is addressed by the Hitchin-Kobayashi correspondence, which indeed show that the existence of such special metric on the vector bundles is equivalent to stability in the sense of Mumford [Don87, UY86, LY87, LT95]. In a certain sense, the Yau-Tian-Donaldson conjecture is a "more non-linear" version of the Hitchin-Kobayashi correspondence.
\item[-] Moduli: From a more heuristic point of view, recall the following fact concerning jump of complex structures for Fano manifolds. Let $\mathcal{X} \xrightarrow{\pi} \Delta$ be a holomorphic submersion. There are cases in which $X_{t}=\pi^{-1}(t)$ are all smooth Fano, with $X_{t} \cong X_{t^{\prime}}$ for any $t, t^{\prime} \neq 0$, but $X_{0} \nsupseteq X_{t}$. It follows that the moduli space of complex structures cannot be Hausdorff, since there would be non-closed points that cannot be separated: $\left[X_{0}\right] \in \overline{\left[X_{t}\right]}$. But the moduli space of Einstein metrics are Hausdorff. This suggests that by "removing" non KE Fanos we could hopefully get a nice (algebraic) moduli space of Fano manifolds, with topology compatible with distance (Gromov-Hausdorff, see next 6.3) induced by the KE metrics. Algebro-geometric notion of stabilities are good for constructing separated moduli in algebraic geometry.
\end{itemize}

Now we move to some more mathematical reasons which should motivate why the notion of K-stability is a natural one.
5.1. Variational point of view. The space $\mathcal{K}_{\omega}$ of Kähler potentials (say on a Fano, even if this description is more general for the cscK problem) looks like an infinite dimensional negative curvature space in the Mabuchi metric: $K_{\varphi}\left(\phi_{1}, \phi_{2}\right) \phi_{3}=-\left\{\left\{\phi_{1}, \phi_{2}\right\}_{\varphi}, \phi_{3}\right\}_{\varphi}$, where $\{,\}_{\varphi}$ is the Poisson's bracket for $\omega_{\varphi}$. As we have seen in section 3.3 such space admits geodesics for which the Mabuchi energy is convex. Note the following: take $f$ such that $\operatorname{grad} f$ is holomorphic. Denote by $\psi_{t}$ the flux of $\operatorname{grad} f$ : then $\psi_{t}^{*} \omega=\omega+\sqrt{-1} \partial \bar{\partial} \varphi_{t}$ where $\dot{\varphi}_{t}=f$. Essentially by definition, the Futaki invariant is the derivative of the Mabuchi's energy:
$$\frac{d}{d t} \mathcal{M}_{\omega}\left(\varphi_{t}\right)=F\left((\operatorname{grad} f)^{1,0}\right)$$

Thus we can make the following "speculation" (since we are on an infinite dimensional space, so care must be considered...): since the Mabuchi's energy is convex on $\mathcal{K}_{\omega}$ and its critical points are precisely the KE metrics, if at the "infinity" of $\mathcal{K}_{\omega}, \mathcal{M}_{\omega}$ has positive slope, we can suspect that a critical point actually do exists. In order to check the "slope at infinity" we could look for something like:
$$\lim _{t \rightarrow+\infty} \frac{d \mathcal{M}_{\omega}\left(\varphi_{t}\right)}{d t}=: \tilde{\mathrm{DF}}\left(\left(\varphi_{t}\right)_{t}\right)$$
where $\tilde{\text { DF }}$ should be a kind of "Futaki invariant".
Thus, we would have the following "geodesic stability picture": if we know that $\tilde{\mathrm{DF}}>0$ for all geodesic rays probing infinity, then we expect to have a critical point: in this case, we would say that $X$ is stable, and hopefully there exists some minimum, i.e., a Kähler-Einstein metric. If $\tilde{\mathrm{DF}} \geq 0$, we would say that $X$ is semistable. The case in which we can find rays such that $\tilde{\mathrm{DF}}<0$ is unstable (and there is no minimum, i.e., a KE metric should not exist).

The precise mathematical definition of DF will be given for special (algebraic) rays: test configurations. In such case, the limits at infinity are singular algebraic varieties with a $\mathbb{C}^{*}$ action, and $\tilde{\mathrm{DF}}$ will be precisely equal to the Futaki invariant on the singular limits at infinity if such limits are not too singular (actually this was used in the first definition of K-stability proposed by Tian [Tia97]). Moreover, as we will see, such Futaki invariant admits a purely algebro geometric definition which extends to very singular limits (after Donaldson [Don02b]). It is worth noting that, thanks to deep algebro-geometric results, to test stability is sufficient to consider only mildly singular degenerate limits for which the original Tian's definitition works [LX14].

Thus we should expect that if we have a KE metric, it should be relatively "easier" to show that on such algebraic geodesic rays we have positivity of the $D F$ invariant (this is the content of Berman's result we will discuss in Section 6). The other direction seems to be harder: we are imposing a condition only on certain algebraic directions in $\mathcal{K}_{\omega}$, which are much less than all possible infinities. The fact that this will be sufficient is deep. The proof of CDS, as we will see, is essentially arguing by contradiction by constructing destabilizing (algebraic) test configurations, but the actual way to do this is quite involved. Anyway, notice that a more pure variational viewpoint has been recently proved to be also successful to show existence for K-stable Fano manifolds, at least in the case of no holomorphic vector fields, see Berman-Boucksom-Jonsson [BBJ15].
5.2. Moment map picture for cscK. Let $\left(M^{2 n}, \omega\right)$ be a compact symplectic manifold. When $\pi_{1}(X)=\{1\}$, then $\mathcal{L}_{X} \omega=0$ yields that there exists $h$ such that $d h=-\iota_{X} \omega$. Let $G$ be a compact group in $\operatorname{Sympl}(M, \omega)$. A moment map for the action of $G$ is given by
$$\mu: M \rightarrow \mathfrak{g}^{\vee}$$
a $G$-equivariant map such that, for any $v \in \mathfrak{g}$,
$$d\langle\mu, v\rangle=-\omega\left(\rho(v), \_\right),$$
where $\rho$ denotes the derivative of the action. The symplectic quotient is then defined as
$$M /^{\text {sym }} G:=\mu^{-1}(0) / G .$$

For example, $\mathbb{C}^{n} /{ }^{\text {sym }} U(1)=\mu^{-1}(0) / U(1) \cong S^{2 n-1} / S^{1} \cong \mathbb{C P}^{n-1}$ with $\mu(z)=|z|^{2}-1$.
Consider now $\left(X^{n}, \omega\right)$ a compact Kähler manifold. We focus on $\omega$ the symplectic structure on the underlying smooth manifold $M^{2 n}$. Consider the infinite-dimensional Kähler manifold
$$\mathcal{I}_{\omega}=\{\omega \text {-compatible complex structures on } M\} .$$
Its tangent space is
$$T_{J} \mathcal{I}_{\omega}=\{A \in \operatorname{End}(T M): A J+J A=0, \quad \omega(A x, y)+\omega(x, A y)=0\} .$$

There is a tautological complex structure
$$\mathcal{J}_{J} A=J A .$$
There is a natural $L^{2}$-metric:
$$\langle A, B\rangle_{J}=\int_{M} g_{J}(A, B) \frac{\omega^{n}}{n!},$$
where $g_{J}=\omega\left(\_, J_{-}\right)$. Then
$$\left(\mathcal{I}_{\omega}, \mathcal{J},\langle\text { _|_}\rangle\right)$$
is Kähler. (See also e.g. [Tia00, Chapter 4], [Szé14, Section 4.1].)
Consider the action of $\mathcal{G}_{\omega}$ the group of (Hamiltonian) symplectomorphisms. Its tangent space can be identified as $T \mathcal{G}_{\omega} \simeq \mathcal{C}_{0}^{\infty}(M ; \mathbb{R})$ the space of zero-average smooth functions. Then:

Theorem 5.1 (Donaldson [Don97], Fujiki [Fuj90]). Let $\left(M^{2 n}, \omega\right)$ be a Kähler manifold, and consider the action $\mathcal{G}_{\omega}$ of (Hamiltonian) symplectomorphism on the space $\mathcal{I}_{\omega}$ of $\omega$-compatible complex structures. Then the action $\mathcal{G}_{\omega} \circlearrowleft \mathcal{I}_{\omega}$ is symplectic, with moment map
$$\mu: \mathcal{I}_{\omega} \rightarrow \mathcal{C}_{0}^{\infty}(M ; \mathbb{R}), \quad J \mapsto \mathrm{Sc}_{g_{J}}-\hat{S}$$
where $g_{J}:=\omega\left(\_, J_{-}\right)$and $\hat{S}$ is a cohomological invariant.
This means we have two operators $R: \mathcal{C}_{0}^{\infty}(M ; \mathbb{R}) \rightarrow T_{J} \mathcal{I}_{\omega}$ defined as $h \mapsto \mathcal{L}_{X_{h}} J$ (the infinitesimal action) and $S: T_{J} \mathcal{I}_{\omega} \rightarrow \mathcal{C}_{0}^{\infty}(M ; \mathbb{R})$ defined as $D(A)=D S c_{J}(A)$ (the derivative of the moment map), such that $(S(A), h)_{L^{2}}=-\Omega(R(h), A):=<J A, R(A)>$. That is, $S^{*}=-J R$.

Then the symplectic quotient $\mu^{-1}(0) / \mathcal{G}_{\omega}$ would be the "moduli space of cscK metrics in $[\omega]$ ". Let's us elaborate a bit more about this. If $F$ is a symplectomorphism, then $F^{*} \omega=\omega$, and $g_{F^{*} J}=F^{*} g$, i.e. nothing interesting is really happing about the metric (the tensor changes, but the underlying metric spaces are still isometric). To do something metrically non trivial we should look at "the complexification of the symplectomorphisms". While such group does not exist, at least infinitesimally is clear how it should act:
$$R(i h):=J R(h)=J \mathcal{L}_{X_{h}} J=\mathcal{L}_{J X_{h}} J .$$
Of course this does not preserve the symplectic form, but instead, as we computed previously: $\mathcal{L}_{J X_{h}} \omega=2 \sqrt{-1} \partial \bar{\partial} h$, Thus it acts precisely by deforming within the Kähler class! So looking at zero of the moment map within a complexified orbit corresponds to the problem of searching for a KE metric (or more generally, for a csck metric) in the space of Kähler potentials as we did in previous sections. From this point of view, the Mabuchi functional should be seen as a convex norm in such orbit (see discussion of Kempf-Ness theorem in the next section), whose critical points are the zeros of the moment map. Of course, if we find a $J$ within the complexified orbit which is inside the zero of the moment map (i.e. a cscK metric), we can apply Moser's theorem [Mos65, CdS01] to find a diffeomorphism which pull back the new symplectic Kähler form to the fixed symplectic background one (while keeping the abstract biholomorphism type of the complex manifold unchanged). Thus the complexified orbits for which we can find such points should be "special" (read "stable"), see previous discussion on "geodesic stability".

Remark 5.2. Note that smooth hypersurfaces in $\mathbb{C P}^{n}$ are all symplectomorphic (for the natural symplectic structure induced by the Fubini-Study form), and the existence problem of KE metric on them fits the above picture.

The next section is going to describe the classical Geometric Invariant Theory (GIT) notion of stability. This is crucial to motivate algebraically the notion of K-stability (that is, the rigorous notion of stability needed to make sense of the vague "stability" notion we described so far).
5.3. Introduction to GIT. For a gentle introduction see [Tho06]. More advanced one are [New78] and [Mum77]. The standard complete reference is [MFK94]. The following example contains the main ideas of GIT:

Example 5.3. Consider the action $\mathbb{C}^{*} \circlearrowleft \mathbb{C}^{2}$ given by
$$t \mapsto\left(\begin{array}{cc}
t & 0 \\
0 & t^{-1}
\end{array}\right) .$$
Note that the topological quotient $\mathbb{C}^{2} /{ }^{\text {top }} \mathbb{C}^{*}$ is not Hausdorff. From the algebro-geometric point of view, we have
$$\mathbb{C}^{2}=\operatorname{Spec} \mathbb{C}[x, y] .$$
We know what the functions on " $\mathbb{C}^{2} / \mathbb{C}^{*}$ " should be: simply look at the $\mathbb{C}^{*}$-invariant polynomials, that is, $\mathbb{C}[x, y]^{\mathbb{C}^{*}}=\mathbb{C}[x y]=\mathbb{C}[t]$. Then
$$\mathbb{C}^{2} / / \mathbb{C}^{*}=\operatorname{Spec} \mathbb{C}[x, y]^{\mathbb{C}^{*}}=\operatorname{Spec} \mathbb{C}[t]=\mathbb{C} .$$
We have the map
$$\mathbb{C}^{2} \rightarrow \mathbb{C}, \quad(x, y) \mapsto x y .$$
Substantially, you use invariants to define quotients.
More generally: take $G$ reductive acting as $G \circlearrowleft \operatorname{Spec} R=X$ on the algebraic variety $X$, where $R$ is a finitely generated graded $\mathbb{C}$-algebra. Then define
$$X / / G:=\operatorname{Spec} R^{G}$$
where $R^{G}$ is finitely generated thanks to reductivity.
Consider now compact quotients.
Definition 5.4. Let $G \subseteq \operatorname{SL}(N+1)$ act as $G \circlearrowleft X \subseteq \mathbb{C P}^{N}$, and assume that $G$ is reductive. Take $x \in X$, and let $\hat{x}$ be a lift to $\mathbb{C}^{N+1}$. We say that $x \in X$ is:
\begin{itemize}
\item[-] GIT-semistable if $0 \notin \overline{G \cdot \hat{x}}$;
\item[-] GIT-stable if $G \cdot \hat{x}$ is closed and its stabilizer is finite;
\item[-] GIT-polystable if $G \cdot \hat{x}$ is closed.
\end{itemize}

This is the fundamental result of GIT:
Theorem 5.5 ([Mum77]). Let $G \circlearrowleft X$ be reductive. Define the compact space by taking invariant sections:
$$Y:=\operatorname{Proj} \bigoplus_{k} H^{0}\left(X ; \mathcal{O}_{X}(k)\right)^{G} .$$
Then there exists
$$\Phi: X \supset X^{s s} \rightarrow Y=: X / / G$$
surjective such that, for $x, y \in X^{s s}$ the set of GIT-semistable points:
$$\Phi(x)=\Phi(y) \quad \text { if and only if } \quad \overline{G \cdot x} \cap \overline{G \cdot y} \cap X^{s s} \neq \varnothing ;$$
and, for $x, y \in X^{s}$ the set of GIT-stable points:
$$\Phi(x)=\Phi(y) \quad \text { if and only if } \quad x=g \cdot y \text { for some } g \in G \text {. }$$

There is only one closed orbit in semi-stable-equivalence classes, and it is the polystable orbit. Thus, $X^{s} / G \subseteq X^{s s} / / G$ is a compactification of the moduli space of stable points, for which we can think at $X^{s s} / / G$, set-theoretically, as the moduli space of polystable objects. In Example 5.3, the origin has to be considered as a polystable point. The points in the axes as semistable ones. The points in the hyperbolas $x y=s \neq 0$ as stable.

We introduce now the Hilbert-Mumford criterion. Let $G \circlearrowleft X \subseteq \mathbb{C P}^{N}$ reductive, and consider a 1-parameter subgroup $\lambda: \mathbb{C}^{*} \rightarrow G$ of $G$. Take a point $x \in X$ and consider $\lim _{t \rightarrow 0} \lambda(t) \cdot x=x_{0} \in X$. Look at the complex line $\mathbb{C}_{x_{0}}$ over $x_{0}$. There is a $\mathbb{C}^{*}$-action on it: $\lambda(t) \circlearrowleft \mathbb{C}_{x_{0}}$ as some power $t^{-w}$, where $w$ is called the weight. Define
$$\mu(x, \lambda):=w .$$

Theorem 5.6 (Hilbert-Mumford criterion [Mum77]). Let $G \circlearrowleft X$ be reductive, and $x \in X$. Then:
\begin{itemize}
\item[-] $x$ is $G I T$-stable if and only if $\mu(x, \lambda)>0$ for any $\lambda$ one-parameter subgroup.
\item[-] $x$ is GIT-semistable if and only if $\mu(x, \lambda) \geq 0$ for any $\lambda$ one-parameter subgroup.
\end{itemize}

The implication " $x$ stable implies $\mu(x, \lambda)>0$ for any $\lambda$ " follows directly by "pictures". The implication " $\mu(x, \lambda) \geq 0$ for any $\lambda$ implies $x$ semistable" is hard; see [MFK94, Theorem 2.1].

Example 5.7. For example, for $\mathrm{SL}(2 ; \mathbb{C})$ acting on binary forms identified with $\operatorname{Sym}^{2}\left(\mathbb{C}^{2}\right)$, GITstability is related to polynomials with multiple roots. This is a nice exercise to do in order to practice with GIT stability (use Hilbert-Mumford criterion).

We are now going to quickly review the Kempf-Ness theorem, which relate finite dimensional symplectic quotient to GIT. Moreover, we discuss the relation with the infinite dimensional picture of the scalar curvature as a moment map.

Look at $\mathbb{C}^{*} \circlearrowleft\left(\mathbb{C}^{2}, \omega_{\text {std }}\right)$, with $\mathrm{U}(1) \subset \mathbb{C}^{*}$ Hamitonian action $\left(h=|x|^{2}-|y|^{2}\right)$. We clearly get
$$\mathbb{C}^{2} /^{\text {sym }} \mathrm{U}(1) \stackrel{\text { top }}{\simeq} \mathbb{C}^{2} / / \mathbb{C}^{*},$$
i.e. the GIT quotient and the symplectic quotient are identified!
More generally, the Kempf-Ness theorem states that if we have some compact $K \subseteq \operatorname{SU}(N+1)$ with $K^{\mathbb{C}} \subseteq \operatorname{SL}(N+1)$, and $K$ acting symplectically on $\left(X, \omega_{F S}\right)$ with moment map $\mu(Z)=$ $\sqrt{-1} \frac{Z_{j} \bar{Z}_{j}}{|Z|^{2}}$. Then
$$X / / K^{\mathbb{C}} \cong X /^{\text {sym }} K .$$
The idea of the proof consists in studying the $\log$ norm function $m=\log |g \cdot \hat{x}|^{2}$ on $K^{\mathbb{C}} / K$. The crucial point is that such function is convex on the complexified orbits, and its critical points coincide with the zero of the moment map. Thus, if the slope at infinity of $m$ is positive (which holds if the orbit is stable, since the weights at infinity are positive), we can find a critical point (that is, a zero of the moment map).

Let us go back to the infinite dimensional case. In such situation the log norm corresponds to the Mabuchi energy on the "complexified orbits" of the symplectomorphisms. Thus the complexified orbits which intersect the zero of the moment map (cscK) should be "stable". Thus, in this infinite dimensional setting, we should still have:
$$\text { " } \mu^{-1}(0) / \mathcal{G}_{\omega} \cong \mathcal{I}_{\omega}^{\text {stab }} / \mathcal{G}_{\omega}^{\mathbb{C}}=: \mathcal{I}_{\omega} / / \mathcal{G}_{\omega}^{\mathbb{C}} \text { ". }$$
In the KE case, the rigorous notion of stability condition is going to be, of course, K-stability. " $\mathcal{I}_{\omega} / / \mathcal{G}_{\omega}^{\mathbb{C}}$ " should be a purely algebraic moduli spaces of stable varieties (K-moduli), which could also be rigorously constructed in the Fano case (e.g. see the survey [Spo17]).

Remark 5.8. This moduli picture can be thought as an higher dimensional analogous of the identification between moduli spaces of metric with constant Gauss curvature on surface of genus $g$ and the complex Deligne-Mumford moduli space of curves.

We are now ready to finally define $K$-stabilty.
5.4. Definition of K-stability. For ( $X, K_{X}^{-1}$ ) Fano manifold, we want to define a "GIT-like" notion of stability, following the dictionary:
\begin{itemize}
\item[-] 1-parameter subgroups $\lambda$ correspond to test configurations $\mathcal{X} \rightarrow \mathbb{C}$;
\item[-] weight $\mu(x, \lambda)$ corresponds to Donaldson-Futaki invariant $D F(X, \mathcal{X})$.
\end{itemize}

In analogy with the Hilbert-Mumford criterion, we define:
\begin{itemize}
\item[-] $X$ is $K$-stable if $D F(X, \mathcal{X})>0$ for any test-configuration $\mathcal{X}$;
\item[-] $X$ is $K$-semistable if $D F(X, \mathcal{X}) \geq 0$ for any test-configuration $\mathcal{X}$;
\item[-] $X$ is $K$-polystable if $X$ is K-semistable and $D F(X, \mathcal{X})=0$ if and only if $\mathcal{X}=X \times \mathbb{C}$.
\end{itemize}

So let us define what is a test configuration and what is the Donaldson-Futaki invariant.
A test configuration of exponent $\ell \in \mathbb{N}$ is a flat family
![](https://cdn.mathpix.com/cropped/0a5a377b-914e-4765-8387-588b1f5c3986-32.jpg?height=187&width=228&top_left_y=781&top_left_x=918)
such that, for $X_{1}=\pi^{-1}(1)$ :
\begin{itemize}
\item[(1)] $\mathcal{L}$ is relative ample and $\mathcal{L}{ }_{\left\lfloor X_{1}\right.} \simeq K_{X_{1}}^{-\ell}$;
\item[(2)] $\pi$ is $\mathbb{C}^{*}$-equivariant.
\end{itemize}

Although a priori quite abstract, test configurations are concrete:
Theorem 5.9 (Ross-Thomas [RT07]). All test configurations are realized by 1-parameters subgroups in $P G L(N+1)$ for embedding of $X \hookrightarrow \mathbb{C P}^{N}$.

Remark 5.10. Note that $N$ in the above result is not fixed! In principle, we should consider test configurations arising as $N \rightarrow+\infty$. This is why K-stability is very hard to check! K-stability should be considered as a (new, non-GIT) stability condition defined on the "stack" of Fano varieties, where the $D F$ invariant can be seen as the weigh of a stacky line bundle, the so-called CM line [PT09]. This fancier approach is relevant for precise moduli considerations.

The next is an example of a test configuration for $\mathbb{C} \mathbb{P}^{1}$.
Example 5.11. For example, consider $X=\left\{x y=z^{2}\right\}$ obtained as the image of the Veronese embedding $\mathbb{C P}^{1} \ni[x: y] \mapsto\left[x^{2}: y^{2}: x y\right] \in \mathbb{C P}^{2}$. Conider the $\mathbb{C}^{*}$-action
$$\lambda(t)=\left(\begin{array}{lll}
t & & \\
& 1 & \\
& & t^{-1}
\end{array}\right),$$
and define
$$X_{t}:=\lambda(t) \cdot X=\left\{x y=t z^{2}\right\} .$$
As $t \rightarrow 0$, we get $X_{0}=\{x y=0\}$.
Now we introduce the Donaldson-Futaki invariant. Consider a test configuration. We get an action $\mathbb{C}^{*} \circlearrowleft X_{0}$ inducing an action $\mathbb{C}^{*} \circlearrowleft H^{0}\left(X_{0} ; \mathcal{L}\left\lfloor_{X_{0}}^{\otimes k}\right)\right.$ for any $k$. By the Riemann-Roch theorem, we write the Hilbert polynomial
$$h_{k}:=\operatorname{dim} H^{0}\left(X_{1} ; \mathcal{L}\left\lfloor\stackrel{\otimes}{X}_{1}^{\otimes k}\right)=a_{0} k^{n}+a_{1} k^{n-1}+\mathcal{O}\left(k^{n-2}\right) .\right.$$
Similarly, we write the weight for the action $\mathbb{C}^{*} \circlearrowleft \wedge^{\text {top }} H^{0}\left(X_{0} ; \mathcal{L}_{0}^{\otimes k}\right)$ as:
$$w_{k}=b_{0} k^{n+1}+b_{1} k^{n}+\mathcal{O}\left(k^{n-1}\right) .$$
Set the Donaldson-Fujiki invariant as
$$D F(X, \mathcal{X}):=\frac{a_{1} b_{0}-a_{0} b_{1}}{a_{0}} .$$

Let us compute the $D F$ invariant for the previous Example 5.11 of test configuration.
Example 5.12. Recall that $X_{0}=\operatorname{Proj} \mathbb{C}[x, y, z] /\langle x y\rangle$. We have
$$\begin{aligned}
H^{0}\left(\mathcal{O}_{X_{0}}(1)\right) & =\langle x, y, z\rangle \\
H^{0}\left(\mathcal{O}_{X_{0}}(2)\right) & =\left\langle x^{2}, x z, y^{2}, y z, z^{2}\right\rangle \\
H^{0}\left(\mathcal{O}_{X_{0}}(3)\right) & =\left\langle x^{3}, x^{2} z, x z^{2}, y^{3}, y^{2} z, y z^{2}, z^{3}\right\rangle,
\end{aligned}$$
and so on. In general,
$$\begin{aligned}
h_{k} & :=\operatorname{dim}\{\text { polynomials of degree } k\}-\operatorname{dim}\{\text { polynomials of degree } k-2\} \\
& =2 k+1
\end{aligned}$$
Similar computations for the weight give:
$$w_{k}=\frac{k(k-1)}{2} .$$
At the end, we get:
$$D F\left(\mathbb{C P}^{1}, \mathcal{X}\right)=\left(\frac{1}{2}+2 \cdot \frac{1}{2}\right) \cdot \frac{1}{2}=\frac{3}{4}>0,$$
as it should be, since $X$ is $K$-stable because it is KE.
Finally, let us see that at least for smooth central fiber, the $D F$ invariant recovers the classical Futaki invariant.

Proposition 5.13. If the central fiber $X_{0}$ is smooth, then the algebro-geometric Futaki invariant $F$ and the $D F$ invariant are essentially the same: if $Z$ generates the $\mathbb{C}^{*}$-action
$$D F\left(X_{0}, \mathcal{X}\right)=\frac{1}{4 \pi} F(Z) .$$
Proof. For more details on this approach via Kähler quantization, see e.g. [Szé14, Proposition 7.15].
Take $L \rightarrow\left(X_{0}, \omega\right)$ be a Kähler manifold with $L$ ample. Consider $H^{0}\left(X_{0} ; L^{\otimes k}\right)$ and take $\underline{s}^{k}=$ $\left(s_{0}^{k}, \ldots, s_{N_{k}}^{k}\right)$ an orthonormal basis of holomorphic sections with respect to the $L^{2}$-metric induced by $\omega$. Denote by $h$ the Hermitian structure on $L$ with positive curvature $\omega$. Introduce the Bergman kernel
$$b_{h}(p)=\sum_{j=0}^{N_{k}}\left|s_{j}^{k}(p)\right|_{h}^{2}>0,$$
where $N_{k}+1=\operatorname{dim} H^{0}\left(X_{0} ; L^{\otimes k}\right)$. It is easy to see that does not depend on the choice of the orthonormal basis.

Since $L$ is ample,
$$\varphi_{\underline{s}^{k}}: X_{0} \hookrightarrow \mathbb{C P}^{N_{k}}, \quad p \mapsto\left[s_{0}^{k}(p): \cdots: s_{N_{k}}^{k}(p)\right]$$
is well-defined for $k \gg 1$, and we compute
$$\varphi_{\underline{s}^{k}}^{*} \omega_{F S}=k \omega+\sqrt{-1} \partial \bar{\partial} \log b_{h^{n}} .$$

The important (and not trivial!) fact proven by Tian [Tia90b], Ruan [Rua98], Zelditch [Zel98], Lu [Lu00], Catlin [Cat99] is that
$$b_{h^{k}}=1+\frac{\mathrm{Sc}_{\omega}}{4 \pi} \cdot \frac{1}{k}+\mathcal{O}\left(\frac{1}{k^{2}}\right)$$
As a consequence,
$$\omega=\frac{1}{2 \pi k} \varphi_{k}^{*} \omega_{F S}+\mathcal{O}\left(\frac{1}{k^{2}}\right),$$
and we recover the Hilbert polynomial expression:
$$h_{k}=k^{n} \int_{X_{0}} \frac{\omega^{n}}{n!}+\frac{k^{n-1}}{4 \pi} \int_{X_{0}} \operatorname{Sc}_{\omega} \frac{\omega^{n}}{n!}+\mathcal{O}\left(k^{n-2}\right) .$$

This gives
$$a_{0}=\int_{X_{0}} \frac{\omega^{n}}{n!}, \quad a_{1}=\frac{1}{4 \pi} \int_{X_{0}} \operatorname{Sc}_{\omega} \frac{\omega^{n}}{n!}$$

Let us do similar computation for the weights. We assume that the $\mathbb{C}^{*}$ action comes from complexification of a U(1)-action for the embedding:
![](https://cdn.mathpix.com/cropped/0a5a377b-914e-4765-8387-588b1f5c3986-34.jpg?height=201&width=758&top_left_y=795&top_left_x=653)
Recall that the moment map for $\omega_{F S}$ and the $U(n+1)$-action is $\mu(Z)=\frac{\sqrt{-1} Z_{i} \bar{Z}_{j}}{|Z|^{2}}$. Let $f$ Hamiltonian for $\omega$, and $f_{k}=-2 \pi\left(A_{k}\right)_{i, j} \frac{\left(s_{i}^{k}, s_{j}^{k}\right)_{h^{k}}}{b_{h}^{k}}$ is Hamiltonian for $\omega_{F S \mid k}$. Then
$$f-\frac{1}{2 \pi k} f_{k}=\mathcal{O}\left(k^{-2}\right) .$$

We compute
$$\begin{aligned}
\int_{X_{0}} f b_{h^{k}} \frac{\omega^{n}}{n!} & =\frac{1}{2 \pi k} \int_{X_{0}} f_{k} b_{h^{k}} \frac{(k \omega)^{n}}{k^{n} n!}+\mathcal{O}\left(k^{-2}\right) \\
& =\frac{1}{2 \pi k} \int_{X_{0}} f\left(1+\frac{S c_{\omega}}{4 \pi} \frac{1}{k}+\mathcal{O}\left(k^{-2}\right)\right) \frac{\omega^{n}}{n!}
\end{aligned}$$
Then
$$w_{k}=-k^{n+1}\left(\int_{X_{0}} f \frac{\omega^{n}}{n!}+\frac{1}{4 \pi k} \int_{X_{0}} \mathrm{Sc}_{\omega} \omega^{n}+\mathcal{O}\left(k^{-2}\right)\right),$$
whence we get
$$b_{0}=-\int_{X_{0}} f \frac{\omega^{n}}{n!}, \quad b_{1}=-\frac{1}{4 \pi k} \int_{X_{0}} \mathrm{Sc}_{\omega} \omega^{n} .$$
By plugging-in these expressions in $D F$, we get the statement. \(\square\)

Remark 5.14.
\begin{itemize}
\item[-] In the Fano case, the same holds for mildly singular (klt) central fiber $X_{0}$.
\item[-] By analyzing in deeper detail the Kähler quantization picture, Donaldson proved [Don01] that cscK manifolds with no holomorphic vector fields are asymptotically balanced, condition which coincides with certain asymptotic GIT stability (Chow stability). However, there are examples which show that asymptotic Chow stability is not enough to capture the cscK or KE existence problem in general.
\item[-] With similar technique, Donaldson showed [Don05] a lower bound on the $L^{2}$ norm of the scalar curvature: $\left\|\mathrm{Sc}_{\omega}-\overline{\mathrm{Sc}}\right\|_{L^{2}} \geq-D F /\|\mathcal{X}\|$. This is clearly enough to conclude K-semistability for the general cscK case (improved to K-polystability by Stoppa in the case with no holomorphic vector fields [Sto09])
\end{itemize}

With the above results we have closed the circle between the rough "geodesic stability" and the properly defined algebraic notion of K-stability. Moreover, the infinite moment map picture makes quite clear that it is natural to expect that such stability condition can precisely capture
the existence problem. As we will discuss in the next section, this is precisely the case in our Fano situation.

\section*{6. Equivalence Between existence of Kähler-Einstein and K-stability}

The goal of this last section is to describe some of the ideas in the proof of equivalence between existence of KE metrics on Fano manifolds and K-stability, as well as to shortly describe compact moduli spaces of such manifolds and some explicit examples.
6.1. Berman's result. In [Ber16] it is proved that K-polystability is a necessary condition for the existence of a KE metrics on smooth (or even mildly singular) Fanos. Previous results in this direction are given by works of Tian, Donaldson, and Stoppa.

We do not discuss in detail Berman's proof, but we simply emphasize the main points. The argument is based on a crucial formula for the Donaldson-Futaki invariant:
$$D F(X, \mathcal{X})=\lim _{t \rightarrow \infty} \frac{d}{d t} \mathcal{D}_{\omega}\left(\varphi_{t}\right)+\epsilon .$$

Let us explain its meaning. Here $\mathcal{X} \rightarrow \Delta_{\tau} \subseteq \mathbb{C}^{*}$ is a test configuration for a Fano variety $X \cong X_{1}$. Starting from a Kähler metric $\omega_{\phi}=\omega+\sqrt{-1} \partial \bar{\partial} \phi$ on $X_{1}$ one can construct a weak geodesic ray in the Mabuchi metric (i.e. a weak solution of the homogeneus Monge-Ampère equation, compare Remark 3.10) with boundary datum $\phi$. Let us denote with $\phi_{t}:=\rho_{\tau}^{*} \psi_{\tau}$ such geodesic ray emanating from $\phi$, where $t=-\log |\tau|^{2}$ and $\rho_{\tau}$ is the $\mathbb{C}^{*}$-action which identifies the general fibres.
$\mathcal{D}_{\omega}$ denotes the Ding functional [Din88]. The Ding functional has the advantage that it can be defined for metric of less regularity with respect to the Mabuchi energy. It has the property that its critical points are again the KE metrics as for the Mabuchi functional. It takes the explicit form
$$\mathcal{D}_{\omega}(\varphi)=-\frac{1}{(n+1)!} \sum_{j=0}^{n} f_{X} \varphi \omega_{\varphi}^{j} \wedge \omega^{n-j}-\log \left(f_{X} \exp (f-\varphi) \omega^{n}\right),$$
where $f$ is the Ricci potential of $\omega$.
The Berman's formula thus states that, similarly to what we discussed for the Mabuchi's energy, the Donaldson-Futaki invariant is the slope at infinity in the space of Kähler potentials of the Ding functional plus an error term denoted by $\epsilon$ which has the crucial property of being non-negative. Actually the term $\epsilon$ can be explicitly given in terms of purely algebro-geometric data of the test-configuration and its resolutions.

Thanks to the this formula (12), the idea of proof is now very clear. If we start the geodesic ray $\phi_{t}$ from the KE potential $\phi_{0}=\phi^{K E}$, using that the KE equation is the Euler-Lagrange equation of the Ding functional, we have $\frac{d}{d t} \mathcal{D}_{\omega}\left(\phi_{t}\right)_{\mid t=0}=0$ (more precisely, Berman proved that is non-negative, the issue being related to regularity properties of the ray). Moreover, since also the Ding functional is convex along the ray, we have that its slope at infinity $\lim _{t \rightarrow \infty} \frac{d}{d t} \mathcal{D}_{\omega}\left(\phi_{t}\right)$ is still non negative. Hence, by the formula and the positivity of the error term, we find that the Donaldson-Futaki invariant of an arbitrary test configuration is non-negative (i.e. $X$ is K-semistable). It is then possible to analyze in further details what happens in the the case of DF invariant equal to zero, to conclude that the error term vanishes and $X_{1}$ is biholomorphic to $X_{0}$ (the point is that one can show that the Ding function has to be affine, and the test configuration generated by an holomorphic vector field).

Remark 6.1. • The Ding functional can be defined also for mildly singular Fano varieties (more precisely klt Fanos, see later). Thus Berman's formula gives K-polystability also for
\begin{itemize}
\item[] such very natural class of singular varieties. As we will see, this is the class of singularities which need to be considered for moduli spaces compactification of smooth KE Fano manifolds.
\item[-] The formula for $\epsilon$ was used to define the notion of Ding stability, a notion that is a priori stronger but then equivalent to K-stability. This notion has been relevant for some of the newest developments in the area, for example in the works of K. Fujita (e.g. [Fuj15, Fuj16a]).
\end{itemize}
6.2. K-polystability implies existence of KE metrics: Donaldson's cone angle continuity path. The goal of the next sections is to give a "map" of the main steps in the proof of the existence of KE metrics on K-polystable Fano manifolds. We hope that such description could be of some help for readers of the seminal papers [CDS15].

The first idea in the proof is to consider a "specialization" of the Aubin's continuity path $\operatorname{Ric}\left(\omega_{t}\right)=t \omega_{t}+(1-t) \omega$, see (10), with $\omega \in 2 \pi c_{1}(X)$, by replacing the smooth background Kähler form $\omega$ with a current of integration $\delta_{D}$ along a smooth divisor $D$ given as zero of a smooth section of the line bundle $K_{X}^{-1}$. That is, we consider the following path, called Donaldson's cone angle continuity path:
$$\operatorname{Ric}\left(\omega_{\beta}\right)=\beta \omega+2 \pi(1-\beta) \delta_{D},$$
for $\beta \in(0,1]$.
Note that the metric $\omega_{\beta}$ is exactly KE with Einstein constant equal to $\beta$ on $X \backslash D$, but the price to pay is that is not longer smooth near $D$ : it has so-called conical singularities. Roughly, this means that near the divisor $D$, if we choose local coordinates $\left(z_{j}\right)_{j}$ so that $D$ is given by $z_{n}=0$, the metric looks like (is uniformly equivalent to) the model flat cone (transverse to $D$ ) metric:
$$\omega_{\beta} \sim \frac{\sqrt{-1}}{|z|^{2(1-\beta)}} d z_{n} \wedge d \bar{z}_{n}+\sqrt{-1} \sum_{j=1}^{n-1} d z_{j} \wedge d \bar{z}_{j}$$

Since it is not always possible to find a smooth anti-canonical sections, one need to consider plurianti-canonical sections, that is sections of powers $K_{X}^{-\lambda}$ of the anti-canonical bundle. Then the generic sections are smooth by Bertini's theorem . The value of the Einstein constant in the corresponding conical continuity path is given by $r(\beta)=1-\lambda(1-\beta)$, and it is positive as soon as $\beta>1-\frac{1}{\lambda}$.

The idea is now simply to prove that the set of cone angles $\beta \mathrm{s}$, for which we can solve equation 13 is non-empty, open and closed under the assumption of $K$-polystability of $X$. Then, letting $\beta \rightarrow 1$, the cone angles can "open-up" to a genuinely smooth KE metric on X (of course there is plenty of things to be proven to make such statement precise!). As a historical comment, let us point out that a similar strategy to deform cone angle Einstein metrics (with cone singularities along smooth real curves) to smooth Einstein metric was proposed by Thurston as a way to attack the 3D Poincarè conjecture [Thu82].

The fact that cone angle metrics (with no assumption on the curvature) always exist is easy: take $\omega=\omega_{0}+\varepsilon \sqrt{-1} \partial \bar{\partial}\left|s_{D}\right|_{h_{0}}^{2 \beta}$ with $\omega_{0}$ smooth background metric (the curvature of the Chern connection of some Hermitian metric $h_{0}$ on the plurianti-canonical bundle) and $\varepsilon \ll 1$. Of course they do not satisfy our equation (13). Thus non-emptiness of the set of solutions for small cone angles follows by taking $\lambda>0$ and apply the orbifold version of the negative KE problem for $\beta=\frac{1}{m}<1-\frac{1}{\lambda}$, see [DK01, Section 6.2], [CDS15, Part III, Section 5], using the above conical $\omega$ as background. If $\lambda=1$ one could instead use a result of Berman [Ber13] which says that for sufficiently small $\beta$ s, a log version of the alpha invariant criterion ensures existence of conical KE metrics along $D$ of positive Einstein constant.

Even if not needed in the proof, we would like to make some remarks about the behaviour of the conical KE metrics for small cone angles.

Remark 6.2. For $\lambda>1$ the conical (negative) KE metrics converge as $\beta \rightarrow 0$ to complete cuspidal KE metrics (with hyperbolic cuspidal behaviour transverse to $D$ ) as proven in [Gue15].

For $\lambda=1$, an interesting well-known conjecture states that the KE cone metrics converge to the complete Calabi-Yau metrics on $X \backslash D$ constructed by Tian and Yau in [TY90, TY91].

If the anti-canonical bundle admits roots, we can consider also $\lambda<1$. However, in such case small angle metrics do not exist: it is a (log)-K-unstable regime, as proved in [LS14]. Heuristically it is clear: we would expect convergence to complete metrics with strictly positive Ricci tensor, and this contradicts Myers' theorem.

Openness is definitely more sophisticated. The idea is to use some implicit function theorem, combined with the fact that there are no holomorphic vector fields tangential to $D$ [Don12, Section 4.4] (which would be related to infinitesimal isometries as we have discussed in section 3.1, and hence would give obstructions to the linearization of the problem). However, using naive (weighted) Hölder spaces will not work. The actual function spaces to be consider are given by a variation of usual Hölder spaces where one considers norms of only certain second order derivatives [Don12, Section 4.3] (essentially the one which appear in the complex Hessian). In any case, in [Don12, Theorem 2] it is proved that if we assume existence of conical KE metrics, we can move the cone angle a bit and still find conical KE metrics.

Remark 6.3. Detailed study of conical KE metrics (generalized energy functionals, alpha invariant, asymptotic analysis, etc. . . ) can be found in the works of Jeffres, Mazzeo, and Rubinstein [JMR16].

From now on, we are taking for granted that we have found conical KE metric for small cone angles, and that the KE condition is open. Thus we need to understand what happens to conical KE spaces $\left(X, \omega_{\beta_{i}}\right)$ as $\beta_{i} \nearrow \underline{\beta}$. The crucial point is now to establish a weak geometric compactness result, which will ensure that, after eventually passing to a subsequence, we can find a limit space $X_{\infty}$ with sufficiently good property (via partial regularity results). In particular, if $X_{\infty}$ can be proved to be an algebraic space we can try to use the $K$-stability hypothesis to show that bad behaviours cannot happens and that $X_{\infty}$ is still biholomorphic to $X$ and the limit metric structure is a cone angle metric on $X$ along $D$ with cone angle $\underline{\beta}$. By the continuity argument we could then show that $\beta$ can go to one, and in this case the metric converge to a smooth KE metric.
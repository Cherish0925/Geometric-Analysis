---
retention_scope: session
part: 2
total_parts: 2
---

[Part 2/2 of: The Geometry of Weakly Self-dual Kähler Surfaces]

THEOREM 3. A Kähler surface is of Calabi type if and only if either:
\begin{itemize}
\item[(i)] it is locally a Kähler product of two Riemann surfaces, one of which admits a Killing vector field; or
\item[(ii)] it admits a Hamiltonian 2-form whose associated Killing vector fields are dependent but not both zero.
\end{itemize}
The Kähler structure is then given explicitly by the Calabi construction (46)-(47): in case (i) $a=0$, while in case (ii) we may take $a=1, b=0$ without loss of generality.

\subsection*{3.2. WEAKLY SELF-DUAL KÄHLER SURFACES OF CALABI TYPE}

We begin this section by computing the curvature of a Kähler surface of Calabi type which is not a local Kähler product. Therefore we set $a=1, b=0$, and write $w(z)=z / V(z)$, so that the Kähler structure is
$$\begin{aligned}
& g=z g_{\Sigma}+\frac{z}{V(z)} \mathrm{d} z^{2}+\frac{V(z)}{z}(\mathrm{~d} t+\alpha)^{2}, \\
& \omega=z \omega_{\Sigma}+\mathrm{d} z \wedge(\mathrm{~d} t+\alpha),
\end{aligned}$$

As with ortho-toric Kähler surfaces, the curvature is entirely determined by the scalar curvature $s$ of $g$, the conformal scalar curvature $\kappa$ of the Hermitian pair $(g, I)$, and the trace-free part $\rho_{0}$ of the Ricci form of $(g, J)$.

LEMMA 10. For a nonproduct Kähler surface ( $M, g, J, \omega$ ) of Calabi type, given by (56)-(57), $\rho_{0}$ is a multiple $\mu$ of the Kähler form $\omega_{I}$ of the Hermitian pair $(g, I)$, and $\mu, s, \kappa$ are given by
$$\begin{aligned}
& \mu=-\frac{1}{4 z}\left(s_{\Sigma}+\left(\frac{V_{z}}{z^{2}}\right)_{z} z^{2}\right), \\
& s=\frac{s_{\Sigma}-V_{z z}}{6 z} \\
& \kappa=\frac{1}{6 z}\left(s_{\Sigma}-z^{2}\left(z^{2}\left(\frac{V}{z^{4}}\right)_{z}\right)_{z}\right),
\end{aligned}$$
where $s_{\Sigma}$ is the scalar curvature of $\Sigma$. In particular, on the open subset of $M$ where $\mu$ has no zero, the anti-self-dual almost-complex structure determined by $\rho_{0}$ is equal to $I$.

Proof. The Ricci form $\rho$ is given by $\rho=\rho_{\Sigma}-\frac{1}{2} \mathrm{~d} J \mathrm{~d} \log V$. The first term is $\frac{1}{2} s_{\Sigma} \omega_{\Sigma}$, and we compute the second term as follows:
$$\begin{aligned}
\mathrm{d} J \mathrm{~d} \log V & =\mathrm{d}\left(\frac{V_{z}}{V} J \mathrm{~d} z\right)=\mathrm{d}\left(\frac{V_{z}}{z}(\mathrm{~d} t+\alpha)\right) \\
& =\frac{V_{z z}}{z} \mathrm{~d} z \wedge(\mathrm{~d} t+\alpha)+V_{z}\left(\frac{1}{z} \omega_{\Sigma}-\frac{1}{z^{2}} \mathrm{~d} z \wedge(\mathrm{~d} t+\alpha)\right) .
\end{aligned}$$
Evidently we may write this as a linear combination of $\omega$ and $\omega_{I}$, and we readily obtain (58) and (59).

The conformal scalar curvature is most easily computed by noticing that the conformal Kähler metric $\bar{g}=z^{-2} g$ is also of Calabi type, with $\bar{z}=1 / z$ and $\bar{V}(\bar{z})=\bar{z}^{4} V(1 / \bar{z})=V(z) / z^{4}$. Hence, its scalar curvatures are
$$\frac{s_{\Sigma}-\bar{V}_{\bar{z} \bar{z}}}{6 \bar{z}}=\frac{z}{6}\left(s_{\Sigma}-z^{2}\left(z^{2}\left(\frac{V}{z^{4}}\right)_{z}\right)_{z}\right)$$
from which (60) follows, since $\kappa=z^{-2} \bar{s}$. \(\square\)

PROPOSITION 14. Let $M$ be a nonproduct Kähler surface $M$ of Calabi type, with Killing vector field $K$. Then the scalar curvature of $M$ is a momentum map for a multiple of $K$ if and only if $g_{\Sigma}$ has constant curvature $k$ and $V$ is of the form
$$V(z)=A_{1} z^{4}+A_{2} z^{3}+k z^{2}+A_{3} z+A_{4} .$$
Any Kähler surface given by (56)-(57) is extremal, with Ricci form $\mu \omega_{I}+\frac{3}{2} s \omega$, where
$$\begin{aligned}
& \mu=-A_{1} z+\frac{A_{3}}{2 z^{2}}, \\
& s=-2 A_{1} z-A_{2} .
\end{aligned}$$
also the conformal scalar curvature of $(g, I)$ is
$$\kappa=-\frac{A_{3}}{z^{2}}-\frac{2 A_{4}}{z^{3}} .$$

Hence:
\begin{itemize}
\item[(i)] $g$ has constant scalar curvature if and only if $A_{1}=0$;
\item[(ii)] $g$ is scalar-flat (i.e., anti-self-dual) if and only if $A_{1}=A_{2}=0$.
\item[(iii)] $(g, J)$ is Kähler-Einstein if and only if $A_{1}=A_{3}=0$;
\item[(iv)] $g$ is weakly self-dual if and only if $A_{3}=0$.
\item[(v)] $g$ is self-dual if and only if $A_{3}=A_{4}=0$.
\item[(vi)] $(g, J)$ is bi-extremal if and only if $g$ is weakly self-dual;
\item[(vii)] the Bach tensor of $g$ vanishes if and only if $4 A_{1} A_{4}-A_{2} A_{3}=0$.
\end{itemize}

Proof. From (59), we have
$$6 z s+V_{z z}=s_{\Sigma} .$$

If $s$ is an affine function of $z$, then both sides of this equation must be constant. Hence $s_{\Sigma}=2 k$ and $V$ must be a quartic in $z$ with quadratic term $k z^{2}$. The formulae for $\mu, s$ and $\kappa$ are immediate, as are (i)-(v). (For (iv) we use the fact that $I$ is integrable and $z^{-2} \omega_{I}$ is closed, so that weak self-duality is equivalent to the equation $\mathrm{d} s=2 \mathrm{~d} \mu$.)
(vi) The Pfaffian $p$ of the normalized Ricci form is given by
$$p=\left(-2 A_{1} z-\frac{1}{2} A_{2}+\frac{A_{3}}{2 z^{2}}\right)\left(-\frac{1}{2} A_{2}-\frac{A_{3}}{2 z^{2}}\right)$$
in particular, $p$ is a rational function of $z$; since $z$ is a holomorphy potential, $p$ is a holomorphy potential if and only if it is an affine function of $z$, if and only if $A_{3}=0 ; p$ is then equal to $-\frac{1}{2} A_{2}\left(s+\frac{1}{2} A_{2}\right)$.
(vii) For any extremal Kähler surface the Bach tensor is $J$-invariant and the corresponding anti-self-dual 2-form, is expressed by (21) which yields
$$\tilde{B}=\frac{\left(4 A_{1} A_{4}-A_{2} A_{3}\right)}{z^{2}} \omega_{I} .$$ \(\square\)

This family of extremal Kähler metrics has been considered in many places. In particular, it includes the extremal Kähler metrics of cohomogeneity one under $U(2)$ constructed by Calabi in [14]; more generally, it turns out that these metrics all have cohomogeneity one under a (local) action of a four-dimensional Lie group, locally isomorphic to a central extension of the isometry group of a surface of constant curvature $k$. We refer to these metrics as extremal Kähler surfaces of Calabi type and briefly recall how they may be realized as diagonal Bianchi metrics, of class IX, VIII or II, according to whether $k$ is positive, negative or zero.

Up to rescaling, we can-and will-assume that $k=\varepsilon$, with $\varepsilon=1,0$ or -1. As is well known, we can now write $\mathrm{d} t+\alpha=\sigma_{3}$ and introduce $t$-dependent 1-forms $\sigma_{1}, \sigma_{2}$ on $\Sigma$ with $g_{\Sigma}=\sigma_{1}^{2}+\sigma_{2}^{2}, \sigma_{1} \wedge \sigma_{2}=\omega_{\Sigma}$ and
$$\mathrm{d} \sigma_{1}=\varepsilon \sigma_{2} \wedge \sigma_{3}, \quad \mathrm{~d} \sigma_{2}=\varepsilon \sigma_{3} \wedge \sigma_{1}, \quad \mathrm{~d} \sigma_{3}=\sigma_{1} \wedge \sigma_{2} .$$

By substituting $\sigma_{1}, \sigma_{2}, \sigma_{3}$ in (56)
$$g=\frac{z}{V(z)} \mathrm{d} z^{2}+z\left(\sigma_{1}^{2}+\sigma_{2}^{2}\right)+\frac{V(z)}{z} \sigma_{3}^{2} ;$$
the complex structure $J$ is determined by
$$J \sigma_{1}=\sigma_{2}, \quad J \mathrm{~d} z=\frac{V(z)}{z} \sigma_{3}$$
while the Kähler form $\omega$ is
$$\omega=\mathrm{d} z \wedge \sigma_{3}+z \sigma_{1} \wedge \sigma_{2}=\mathrm{d}\left(z \sigma_{3}\right) .$$

We here recognize bi-axial diagonal Bianchi metrics of class IX, VIII or II, according as $\varepsilon$ is equal 1, -1 or 0; these admit a cohomogeneity one local action of SU(2) if $\varepsilon=1$, of $\operatorname{SU}(1,1)$ if $\varepsilon=-1$, of the Heisenberg group Nil if $\varepsilon=0$, and the orbits are level sets of $z$. This can be seen as follows: denote by $\left(Z_{1}, Z_{2}, Z_{3}=K_{1}\right)$ the triplet of
vector fields determined by $\sigma_{i}\left(Z_{j}\right)=\delta_{i j}$ and $\mathrm{d} z\left(Z_{i}\right)=0, i, j=1,2,3$, where $\delta_{i j}$ is the Kronecker symbol. Then, for each value of $z, Z_{1}, Z_{2}, Z_{3}$ are tangent to the corresponding orbit $M_{z}$ and generate a Lie algebra isomorphic to $\mathfrak{s u}(2), \mathfrak{s u}(1,1)$ or $\mathfrak{n i l}{ }^{3}$ according as $\varepsilon$ is equal to 1, -1 or 0; therefore, each orbit can be locally identified to the corresponding Lie group and we can locally construct a new triple of independent vector fields, $\left(\tilde{Z}_{1}, \tilde{Z}_{2}, \tilde{Z}_{3}\right)$, such that $\left[\tilde{Z}_{i}, Z_{j}\right]=0$ and $\mathrm{d} z\left(\tilde{Z}_{i}\right)=0, i, j=1,2,3$ (for each orbit, if $\left(Z_{1}, Z_{2}, Z_{3}\right)$ is a basis of left-invariant vector fields, $\left(\tilde{Z}_{1}, \tilde{Z}_{2}, \tilde{Z}_{3}\right)$ is a basis of right-invariant vector fields); $\tilde{Z}_{1}, \tilde{Z}_{2}, \tilde{Z}_{3}$ are clearly Killing with respect to $g$ and all commute with $K_{1}$.

If $\varepsilon \neq 0, K_{1}, \tilde{Z}_{1}, \tilde{Z}_{2}, \tilde{Z}_{3}$ generate a four-dimensional Lie algebra, corresponding to a local action of $U(2)$ if $\varepsilon=1$, of $U(1,1)$ if $\varepsilon=-1$. If $\varepsilon=0, \tilde{Z}_{3}$ equals $K_{1}$, up to a constant factor; on the other hand, we get an additional Killing vector field $\tilde{K}_{1}$ generated by the rotations around the origin in the Euclidean 2 -plane $\mathrm{E}^{2}$ of $x, y$; then, $\tilde{K}_{1}, K_{1}, \tilde{Z}_{1}, \tilde{Z}_{2}$ generate a four-dimensional Lie algebra, say $\mathfrak{g}$, corresponding to a local action of the group, $G$, obtained by forming the semi-direct product of Nil by $S^{1}$ for the natural action of $S^{1}$ on Nil by (outer) automorphisms; the centre of $G=\mathrm{Nil} \ltimes S^{1}$ coincides with the centre of Nil; the latter is one-dimensional again and the quotient of $G$ by its center is isomorphic to $\operatorname{Isom}\left(\mathbb{E}^{2}\right)$; in other words, $G$ is isomorphic to a (nontrivial) one-dimensional central extension of $\operatorname{Isom}\left(\mathrm{E}^{2}\right)$.

If we concentrate our attention on weakly self-dual Kähler surfaces, we readily infer from the foregoing:

THEOREM 4. Let $(M, g, J)$ be a weakly self-dual Kähler surfaces. Denote by $s$ the scalar curvature and by $p$ the Pfaffian of the normalized Ricci form; let $K_{1}=J \operatorname{grad}_{g} s$ and $K_{2}=J \operatorname{grad}_{g} p$ be the associated Killing vector fields and assume that $K_{1}$ has no zero and that $K_{2}=b K_{1}$, where $b$ is a real constant (possibly zero).
(i) Then $(M, g, J)$ admits a local action of cohomogeneity one of $G=U(2), U(1,1)$ or Nil × $S^{1}$ and is locally isomorphic to a diagonal Bianchi metric of class IX, VIII or II respectively.

More precisely, let $\sigma_{1}, \sigma_{2}, \sigma_{3}$ denote the (local) 1-forms on $M$ induced by this action, corresponding to a triple of G-invariant 1-forms on G, so that $\mathrm{d} \sigma_{3}=\sigma_{1} \wedge \sigma_{2}, \mathrm{~d} \sigma_{2}=$ $\varepsilon \sigma_{3} \wedge \sigma_{1}, \mathrm{~d} \sigma_{1}=\varepsilon \sigma_{2} \wedge \sigma_{3}$, where $\varepsilon=1,-1$ or 0 according as $G=U(2), U(1,1)$ or Nil $\ltimes S^{1}$; then, the Kähler structure ( $g, J$ ) can be put in the form (67)-(68), where $z$ is an affine function of $s$ and $V(z)$ is of the form
$$V(z)=A_{1} z^{4}+A_{2} z^{3}+\varepsilon z^{2}+A_{4} .$$
(ii) Conversely, each Kähler surface of the form (67)-(68), with $V$ given by (70) is weakly self-dual.
(iii) This Kähler structure is self-dual if and only if $A_{4}=0$.

Remark 6. By substituting $A_{3}=0$ in (62) and (64), we readily infer that $A_{4}$ and the constant $c$ appearing in (23) and (24) are linked together by
$$c=2 A_{1}^{3} A_{4} ;$$
moreover, $A_{1} \neq 0$, as $s$ is nonconstant, so that $A_{4}=0$ if and only if $c=0$; as we already know, both conditions are equivalent to $g$ being self-dual. \(\square\)

\subsection*{3.3. THE WEAKLY SELF-DUAL KÄHLER METRIC ON THE FIRST HIRZEBRUCH SURFACE}

We close this section by providing an example of a compact weakly self-dual Kähler surface $(M, g, J)$; this belongs to the family of extremal metrics constructed in [14] by E. Calabi on the first Hirzebruch surface $F_{1}$, viewed as the compactification of the total space of the tautological line bundle $L=\mathcal{O}(-1)$ over the complex projective line $\mathbb{C} P^{1}=\mathbb{P}\left(\mathbb{C}^{2}\right)$ obtained by adding a section at infinity, say $C_{\infty}$; then, the zero section, $C_{0}$, has self-intersection -1 and $F_{1}$ can also be considered as a blown up of the projective plane $\mathbb{C} P^{2}$ at some point, with exceptional divisor $C_{0}$, and $F_{1}-C_{0}=$ $\mathrm{C}^{2}-\{(0,0)\}$.

We here recall the main features of Calabi's construction from [14]. Let $r$ be the usual norm in $\mathbb{C}^{2}$ and, for convenience, introduce the function $t$ defined on $\mathrm{C}^{2}-\{(0,0)\}$ by $\mathrm{e}^{t}=r^{2}$; the group $U(2)$ naturally acts on $F_{1}$, by preserving $C_{0}$ and $C_{\infty}$; by [15], the connected group of isometries, $\operatorname{Isom}_{0}(M, g)$, of any compact extremal Kähler surface $(M, g, J)$ is a maximal compact subgroup of the connected group of holomorphic transformations $\operatorname{Aut}_{0}(M, J)$; it follows that any extremal metric on $F_{1}$ is isometric to a $\mathrm{U}(2)$-invariant metric, in particular has a globally defined potential on the open set $M_{0}=F_{1}-C_{0}=\mathrm{C}^{2}-\{(0,0)\}$ of the form $u=u(t)$; the Kähler form is thus given by $\omega=\psi(t) \mathrm{dd}^{c} t+\psi^{\prime}(t) \mathrm{d} t \wedge \mathrm{~d}^{c} t$, where $\psi(t):=u^{\prime}(t)$; conversely, any such Kähler metric extends to $F_{1}$ if and only if $\psi(t)$ extends to a $C^{\infty}$ function of $\mathrm{e}^{t}$ in the neighbourhood of $t=-\infty$ and to a $C^{\infty}$ function of $\mathrm{e}^{-t}$ in the neighbourhood of $t=\infty$; in particular, $\psi$ has a limit $a$ when $t \rightarrow-\infty$ and a limit, $b$, when $t \rightarrow \infty$,with $0<a<b$; the corresponding Kähler class $[\omega]$ is then equal to $4 \pi\left(-a\left[C_{0}\right]+b\left[C_{\infty}\right]\right)$, where $\left[C_{0}\right]$ and $\left[C_{\infty}\right]$ denotes the Poincaré dual of $C_{0}$ and similarly for $\left[C_{\infty}\right]$; conversely, each Kähler class on $F_{1}$ is of this form, for some pair $0<a<b$; it is easily checked that the Ricci for is given by $\rho=\mathrm{dd}^{c} v$, with $v=t-\frac{1}{2} \log \psi-\frac{1}{2} \log \psi^{\prime}$, so that $s=2\left(\left(v^{\prime} / \psi\right)+\left(v^{\prime \prime} / \psi^{\prime}\right)\right)$; on the other hand, such a metric is extremal if and only if $s$ is an affine function of $\psi$; by easy successive partial integrations, we infer that this metric is extremal if and only if $\psi$ satisfies the following differential relation: $\psi \psi^{\prime}=V(\psi)$, where $V$ is a polynomial of the form (61); moreover, the extremal metric is actually defined on $F_{1}$ and has its Kähler class parameterized by the pair $(a, b)$ as above if and only if the coefficients of $V$ are given by
$$\begin{array}{ll}
A_{1}=\frac{-2 a}{(b-a)\left(a^{2}+4 a b+b^{2}\right)}, & A_{2}=\frac{\left(3 a^{2}-b^{2}\right)}{(b-a)\left(a^{2}+4 a b+b^{2}\right)}, \\
A_{3}=\frac{a b\left(3 a^{2}-b^{2}\right)}{(b-a)\left(a^{2}+4 a b+b^{2}\right)}, & A_{4}=\frac{-2 a^{3} b^{2}}{(b-a)\left(a^{2}+4 a b+b^{2}\right)} ;
\end{array}$$
we thus get an extremal Kähler metric, say $g_{(a, b)}$, in each Kähler class of $F_{1}$ (we have a similar construction for the other Hirzebruch surfaces $F_{k}$ [14]; the coefficients of $V$ are then given by (76) below).

All these metrics are of cohomogeneity one under the action of $U(2)$ and can also be put in the form (67)-(68), with the same parameter $\psi$, the same polynomial $V(\psi)$, $\mathrm{d}^{c} t=\sigma_{3}$ and $\mathrm{dd}^{c} t=\sigma_{1} \wedge \sigma_{2}$; in particular, according to Proposition 14, $g_{(a, b)}$ if weakly self-dual if and only if $A_{3}=0$, and this happens if and only if $a$ and $b$ are related by
$$b^{2}=3 a^{2} ;$$
in this case, $A_{2}=0$ as well, meaning that $p=0$, and $V(\psi)=A_{1} \psi^{4}+\psi^{2}+A_{4}$ is a function of $\psi^{2}$; in particular, $\psi \psi^{\prime}=V(\psi)$ is easily integrated into
$$\psi=a\left(\frac{1+3 \mathrm{e}^{t+t_{0}}}{1+\mathrm{e}^{t+t_{0}}}\right)^{\frac{1}{2}}=a\left(\frac{1+3 \mathrm{e}^{t_{0}} r^{2}}{1+\mathrm{e}^{t_{0}} r^{2}}\right)^{\frac{1}{2}},$$
where $t_{0}$ is a constant; the latter can be made equal to zero without loss of generality by a mere translation of the parameter $t$, i.e. a rescaling of $r$; then, up to rescaling, the Kähler form is given by
$$\omega=\frac{\left(1+3 \mathrm{e}^{t}\right)^{\frac{1}{2}}}{\left(1+\mathrm{e}^{t}\right)^{\frac{1}{2}}} \mathrm{dd}^{c} t+\frac{\mathrm{e}^{t}}{\left(1+\mathrm{e}^{t}\right)^{\frac{3}{2}}\left(1+3 \mathrm{e}^{t}\right)^{\frac{1}{2}}} \mathrm{~d} t \wedge \mathrm{~d}^{c} t .$$

In the sequel, the Kähler metric given by (75) will be referred to as the Calabi weakly self-dual Kähler metric of $F_{1}$. It may be noticed that, according to (72), the scalar curvature $s=-2 A_{1} \psi$ is nonconstant and (strictly) positive.

In the next section we show that, conversely, each compact weakly self-dual Kähler surface with nonconstant scalar curvature is, up to rescaling, isomorphic to the first Hirzebruch surface equipped with the Calabi weakly self-dual Kähler metric.

\section*{4. Compact Weakly Self-dual Kähler Surfaces}

Compact self-dual Kähler surfaces have been described by B.-Y. Chen in [20]: these are locally symmetric, hence of constant holomorphic sectional curvature or, locally the product of Riemann surfaces of opposite constant curvature (see [13] for a higher-dimensional generalization).

In [32], W. Jelonek proved that compact real analytic weakly self-dual Kähler surfaces are either Kähler-Einstein, or locally the product of two Riemann surfaces of constant Gauss curvatures, or biholomorphic to a ruled surface.

We show that the hypothesis of real analyticity can actually be removed and that, except in the case when the scalar curvature is constant, the only weakly self-dual Kähler ruled surface is the first Hirzebruch surface $F_{1}$ equipped with the Calabi weakly self-dual Kähler metric, as described in the preceding section (up to rescaling). More precisely, we have the following result.

THEOREM 5. Let $(M, g, J)$ be a compact weakly self-dual Kähler surface. Then $(M, g, J)$ is either
\begin{itemize}
\item[(i)] Kähler-Einstein; or
\item[(ii)] locally isomorphic to the product of two Riemann surfaces of constant Gauss curvatures, or
\item[(iii)] up to rescaling, isomorphic to the first Hirzebruch surface $F_{1}$ equipped with a Calabi weakly self-dual Kähler metric.
\end{itemize}

Proof. By Proposition 6, we know that $g$ is either self-dual, hence, by the above mentioned result of B.-Y. Chen, described by (i) or (ii), or of constant scalar curvature, hence, again, described by (i) or (ii), or of nonconstant scalar curvature. In the latter case, the (negative) Kähler structure ( $\bar{g}, I$ ) is globally defined; it then follows from a result of Kotschick [36] that the signature of $M$ is zero [36]; moreover, since the (real) holomorphic field $K_{1}=J \operatorname{grad}_{g} s$ has nonempty zero set, we know by [19] that the Kodaira dimension of the Kähler surface $(M, J)$ is $-\infty$, hence $(M, J)$ is a ruled surface which is the projectivization $\mathbb{P}(E)$ of a rank 2 holomorphic vector bundle $E$ over a compact complex curve $\Sigma$ [11].

If $\Sigma=\mathbb{C} P^{1},(M, J)$ is a Hirzebruch surface $F_{k}=\mathbb{P}(\mathcal{O} \oplus \mathcal{O}(-k))$, where $k$ is a positive integer, or the product $\mathrm{C} P^{1} \times \mathrm{C} P^{1}$; the only extremal Kähler metrics of $\mathbb{C} P^{1} \times \mathbb{C} P^{1}$ are the (symmetric) product metrics, which are of constant scalar curvature; on the other hand, any maximal compact subgroup of $\operatorname{Aut}_{0}(M, J)$ is conjugate to U(2), and therefore any extremal Kähler metric must be a cohomogeneityone U(2) metric [15], hence, locally of the form (67) with $\varepsilon=1$ (cf. the end of the preceding section for the case when $k=1$ ); as shown by E. Calabi in [14], for each $k>0$, any Kähler class of $F_{k}$ carries a unique extremal Kähler metric (up to a reparameterization); each one can be put in the form (67), where the polynomial $V$, in the notation of (61), is determined by
$$\begin{aligned}
A_{1} & =\frac{(k+1) a+(k-1) b}{(b-a)\left(a^{2}+b^{2}+4 a b\right)}, & A_{2} & =\frac{(2-k) b^{2}-(k+2) a^{2}}{(b-a)\left(a^{2}+b^{2}+4 a b\right)}, \\
A_{3} & =\frac{a b\left((2-k) b^{2}-(k+2) a^{2}\right)}{(b-a)\left(a^{2}+b^{2}+4 a b\right)}, & A_{4} & =\frac{a^{2} b^{2}((k+1) a+(k-1) b)}{(b-a)\left(a^{2}+b^{2}+4 a b\right)},
\end{aligned}$$
where $0<a<b$ are the parameters of the Kähler class; according to Proposition 14, $g$ is weakly self-dual precisely when $A_{3}=0$; in the present situation, this is equivalent to $A_{2}=0$ and happens if and only if $k=1$ and $\mu:=a / b=1 / \sqrt{3}$, i.e. if $(M, g, J)$ is the first Hirzebruch surface equipped with a Calabi weakly self-dual Kähler metric.

We now show that a compact ruled surface $(M, J)$ whose base $\Sigma$ is a compact complex curve of genus $\mathbf{g}(\Sigma)$ at least 1 does not carry weakly self-dual Kähler metrics of non-constant scalar curvature. We thus assume that $(M, J)=\mathrm{P}(E)$ carries a weakly self-dual Kähler metric of non-constant scalar curvature to get a contradiction.

Using an argument from [38, 49], we first observe that the rank two vector bundle $E$ splits as $E=\mathcal{O} \oplus L$, where $\mathcal{O}$ stands for the trivial holomorphic line bundle and $L$ is a holomorphic line bundle $L$ of degree $\operatorname{deg}(L)>0$. Indeed, recall the already mentioned result of E. Calabi [15] that the connected component of the isometry group $\operatorname{Isom}_{0}(M, g)$ is a maximal compact subgroup in $\operatorname{Aut}_{0}(M, J)$; according to
M. Maruyama [41], the group of automorphisms of ruled surfaces can be described as follows: If $\mathbf{g}(\Sigma) \geqslant 1$, there exists an exact sequence
$$\{\mathbf{1}\} \rightarrow \operatorname{Aut}_{\Sigma}(\mathbb{P}(E)) \rightarrow \operatorname{Aut}(\mathbb{P}(E)) \rightarrow \operatorname{Aut}(\Sigma),$$
where $\operatorname{Aut}_{\Sigma}(\mathrm{P}(E))$ denotes the group of relative automorphisms of the bundle $\mathbb{P}(E) \rightarrow \Sigma$, and $\operatorname{Aut}(\Sigma)$ is the group of automorphisms of $\Sigma$ (of course, $\operatorname{Aut}(\Sigma)$ is finite if $\mathbf{g}(\Sigma) \geqslant 2$ ); on the other hand, the (nontrivial) homomorphic vector field $\Xi_{1}=K_{1}-i J K_{1}$ whose real part is the Killing vector field $K_{1}=J \operatorname{grad}_{g} s$ has a nonempty zero set; since $\Xi_{1}$ preserves the (unique) ruling $M=\mathbb{P}(E) \rightarrow \Sigma$, it projects onto a holomorphic vector field on the base $\Sigma$; since $\Xi_{1}$ has at least one zero, the induced vector field on $\Sigma$ vanishes; it follows that $\Xi_{1}$ is tangent to the $\mathrm{C} P^{1}$ fibers (equivalently, $\Xi_{1}$ belongs to the Lie algebra of $\operatorname{Aut}_{\Sigma}(\mathrm{P}(E))$ ); this shows that the kernel of the group homomorphism $f: \operatorname{Isom}_{0}(M, g) \rightarrow \operatorname{Aut}_{0}(\Sigma)$ induced by the exact sequence (77) is a nontrivial compact subgroup of $\operatorname{Aut}_{\Sigma}(\mathrm{P}(E))$; one can therefore find an $S^{1}$ in the connected component of the identity of $\operatorname{Aut}{ }_{\Sigma}(\mathrm{P}(E))$; denote by $\Xi_{0}$ the induced holomorphic vector field, such that the imaginary part $K_{0}=\operatorname{Im}\left(\Xi_{0}\right)$ generates the $S^{1}$-action, whereas $\Xi_{0}$ itself generates a $\mathrm{C}^{*}$-action; as a matter of fact, $\Xi_{0}$ can be identified to a traceless holomorphic section of $\operatorname{End}(E)$, say $\mathbf{s}$; note that $\mathbf{s}$ is of constant determinant; since $K_{0}=\operatorname{Im}\left(\Xi_{0}\right)$ generates a periodic $S^{1}$-action, s must be diagonalizable; this shows that we have a holomorphic splitting of $E$ into eigensubbundles of s; by twisting by a line bundle, we obtain the splitting $E=\mathcal{O} \oplus L$, where $\operatorname{deg}(L) \geqslant 0$; then, $\Xi_{0}$ is nothing but the Euler vector field of $L$. If the degree of $L$ is zero, then any Kähler class contains a locally symmetric Kähler metric [51], so that any extremal Kähler metric on $(M, J)$ is of constant scalar curvature [14], a contradiction; we thus obtain a splitting $E=\mathcal{O} \oplus L$ where $L$ is a holomorphic line bundle of $\operatorname{deg}(L)>0$.

As $\operatorname{Isom}_{0}(M, g)$ is a maximal compact subgroup in $\operatorname{Aut}_{0}(M, J)$, we may assume [49] that (up to a biholomorphism) the metric $g$ is invariant under the fixed $S^{1}$ action generated by $K_{0}=\operatorname{Im}\left(\Xi_{0}\right)$. For any nontrivial Killing vector field, $K$, which arises from a real holomorphy potential, the argument already used above shows that $\Xi=K-i J K$ must be tangent to the fibers, and therefore $\Xi \wedge \Xi_{0}=0$. In particular, we get that $K_{0}=f K_{1}+h J K_{1}$, where $f, h$ are smooth functions defined on an open dense subset of $M$ where $K_{1}=J \operatorname{grad}_{g} s \neq 0$. But $\left\langle K_{0}, J K_{1}\right\rangle=-\mathrm{d} s\left(K_{0}\right)=-\mathcal{L}_{K_{0}} s=0$, i.e. $h=0$, and therefore $f$ is a constant. By rescaling the metric if necessary we may assume therefore that $K_{1}=K_{0}=\operatorname{Im}\left(\Xi_{0}\right)$. Similarly, $K_{2}=J \operatorname{grad}{ }_{g} p$ must be a constant multiple of $K_{1}$ and by Theorem 4, $g$ must be locally of cohomogeneity one, i.e., $g$ can be written of the form (67) on an open dense subset of $M$.

Note that $M$ contains exactly two curves fixed by the $\mathrm{C}^{*}$-action generated by $\Xi_{0}$, corresponding to the zero and infinity sections, $C_{0}$ and $C_{\infty}$, of $M=\mathrm{P}(\mathcal{O} \oplus L)$; moreover, the function $z$ appearing in (67) makes sense on the whole of $M$ as being a momentum map of the corresponding $S^{1}$-action (up to multiplication by a nonzero constant); it then follows that $z: M \rightarrow \mathbb{R}$ maps $M$ onto an interval $[a, b]$, such that $z$ is regular on $M-\left(z^{-1}(a) \cup z^{-1}(b)\right)$; therefore, for any $t_{0} \in(a, b), \Sigma=z^{-1}\left(t_{0}\right) / S^{1}$,
whereas $C_{0}=z^{-1}(a)$ and $C_{\infty}=z^{-1}(b)$ (see [38]). By using an argument from [38, p. 42], it is shown that $q=\left|K_{1}\right|^{2}$ is a smooth function on $\Sigma \times[a, b]$, which satisfies the boundary conditions
$$q(., a)=q(., b)=0 ; \quad\left(\frac{\partial}{\partial z} q\right)(., a)=-\left(\frac{\partial}{\partial z} q\right)(., b)=k,$$
where $k$ is a real constant; for Calabi's metrics (67) one has $q=(V(z)) / z$, so that the Equations (78) read
$$V(a)=V(b)=0 ; \quad V^{\prime}(a)=k a ; \quad V^{\prime}(b)=-k b ;$$
we thus obtain the following values for the coefficients $A_{1}, A_{2}, A_{3}, A_{4}$ of $V$ (notations of (61)):
$$\begin{array}{rlrl} 
& A_{1}=\frac{k(a+b)+\varepsilon(a-b)}{(b-a)\left(a^{2}+4 a b+b^{2}\right)}, & A_{2} & =\frac{-k\left(a^{2}+b^{2}\right)+2 \varepsilon\left(b^{2}-a^{2}\right)}{(b-a)\left(a^{2}+4 a b+b^{2}\right)}, \\
A_{3}=\frac{a b\left(-k\left(a^{2}+b^{2}\right)+2 \varepsilon\left(b^{2}-a^{2}\right)\right)}{(b-a)\left(a^{2}+4 a b+b^{2}\right)}, & A_{4} & =\frac{a^{2} b^{2}(k(a+b)+\varepsilon(a-b))}{(b-a)\left(a^{2}+4 a b+b^{2}\right)} ;
\end{array}$$
according to Proposition 14 we have $A_{3}=0$, and from (79) we also get $A_{2}=0$; by (63) and (62) it follows that the Ricci tensor of $g$ has two distinct eigenvalues, equal to $s / 6$ and $s / 3$, respectively; by Proposition 6, Ric ${ }_{0}$ nowhere vanishes on $M$, meaning that the scalar curvature $s$ nowhere vanishes as well; since $K_{1}$ is a non-trivial Killing vector field, $s$ must be everywhere positive; this shows that the first Chern class $c_{1}(M)$ of $(M, J)$ is positive, and therefore $c_{1}^{2}(M)>0$, a contradiction [11].

Remark 7. The case (ii) of Theorem 5 includes in particular ruled surfaces $\mathrm{P}(E)$ over a Riemann surface $\Sigma$ of genus $g \geqslant 1$ when the holomorphic vector bundle $E$ is stable or polystable, cf., e.g., [51].

\section*{5. Weakly Self-dual Almost Kähler Manifolds}

\subsection*{5.1. THE MATSUMOTO-TANNO IDENTITY FOR ALMOST KÄHLER 4-MANIFOLDS}

Recall that an almost Kähler manifold is an almost Hermitian manifold $(M, g, J, \omega)$ for which the Kähler 2-form $\omega$ is closed. The almost complex structure $J$ of an almost Kähler manifold is not integrable in general; if it is, we obtain a Kähler manifold.

We would like to identify the Ricci tensor Ric of an almost Kähler manifold with a 2 -form $\rho$, the Ricci form, as in the Kähler case. However, only the $J$-invariant part of Ric defines a 2-form, whereas on a (nonintegrable) almost Kähler manifold, the Ricci tensor is not in general $J$-invariant. We shall therefore impose $J$-invariance as an extra requirement.

Throughout this section we will always assume that $(M, g, J)$ is an almost Kähler 4-manifold whose Ricci tensor is $J$-invariant, i.e., $\operatorname{Ric}(J \cdot, J \cdot)=\operatorname{Ric}(\cdot, \cdot)$. We then adopt the notations of Section 1, and, in analogy with the Kähler case, we consider the type $(1,1)$ Ricci form, $\rho$, of $(M, g, J)$ defined by $\rho(\cdot, \cdot)=\operatorname{Ric}(J \cdot, \cdot)$; the anti-self-dual part of $\rho$ is denoted by $\rho_{0}$. It is a remarkable fact [22] that even though $J$ is not integrable, $\rho$ is still a closed (1,1)-form (although it is no longer a representative of $1 / 2 \pi c_{1}^{\mathrm{R}}$ ). Using this observation, the proof of Lemma 1 easily extends to the case of almost Kähler 4-manifolds with $J$-invariant Ricci tensor.

LEMMA 11. For any almost Kähler 4-manifold with J-invariant Ricci tensor the identity (1) is satisfied. In particular, the anti-self-dual Weyl tensor $W^{-}$of such a manifold is harmonic if and only if the Matsumoto-Tanno identity (2) is satisfied.

Proof. The proof follows the one given in the Kähler case, with slight modifications in places where the nonintegrability of $J$ must be taken into account: the Cotton-York tensor is now written as
$$\begin{aligned}
C_{X, Y}(Z)= & -\frac{1}{2}\left(\left(\nabla_{X \rho}\right)(Y, J Z)-\left(\nabla_{Y} \rho\right)(X, J Z)\right)-\frac{1}{2}\left(\rho\left(Y,\left(\nabla_{X} J\right)(Z)\right)-\right. \\
& \left.-\rho\left(X,\left(\nabla_{Y} J\right)(Z)\right)\right)+\frac{1}{2}(d s(X)\langle Y, Z\rangle-d s(Y)\langle X, Z\rangle) .
\end{aligned}$$
Since $\rho$ closed [22], we have
$$\left(\nabla_{X} \rho\right)(Y, J Z)-\left(\nabla_{Y} \rho\right)(X, J Z)=-\left(\nabla_{J Z} \rho\right)(X, Y) .$$
As an algebraic object, $\nabla_{X} J$ is a skew-symmetric endomorphism of $T M$, associated (by $g$-duality) to the section $\nabla_{X} \omega$ of the bundle of $J$-anti-invariant 2-forms; it then anti-commutes with $J$, and commutes with any skew-symmetric endomorphism associated to a section of $\Lambda^{-} M$; in particular, $\nabla_{X} J$ commutes with the endomorphism corresponding to $\rho_{0}$ via the metric (which will be still denoted by $\rho_{0}$ ). We thus obtain
$$\begin{aligned}
& \rho\left(Y,\left(\nabla_{X} J\right)(Z)\right)-\rho\left(X,\left(\nabla_{Y} J\right)(Z)\right) \\
& \quad=\frac{3 s}{2}\left(\left(\nabla_{Y} \omega\right)(X, J Z)-\left(\nabla_{X} \omega\right)(Y, J Z)\right)+\left(\nabla_{X} \omega\right)\left(Y, \rho_{0}(Z)\right)-\left(\nabla_{Y} \omega\right)\left(X, \rho_{0}(Z)\right) .
\end{aligned}$$
By using the closedness of $\omega$ we derive
$$\rho\left(Y,\left(\nabla_{X} J\right)(Z)\right)-\rho\left(X,\left(\nabla_{Y} J\right)(Z)\right)=\frac{3 s}{2}\left(\nabla_{J Z} \omega\right)(X, Y)-\left(\nabla_{\rho_{0}(Z)} \omega\right)(X, Y) .$$
Substituting (81) and (82) in (80), we finally get
$$\nabla_{Z} \rho_{0}=-\frac{3 s}{2} \mathrm{~d} s(Z) \omega-2 C(J Z)-\nabla_{\operatorname{Ric}_{0}(Z)} \omega+\mathrm{d} s \wedge J Z^{p},$$
The $\Lambda^{-} M$-component of (83) gives the identity (1); the last part of the lemma is immediate. \(\square\)

It follows that Lemma 4 and, hence, Proposition 1 remain true for weakly self-dual Kähler surfaces, so that on the open set $M_{0}$ where $\rho_{0} \neq 0$ the almost Hermitian structure ( $\bar{g}=\lambda^{-2} g, I$ ) defined on $M_{0}$ by $\rho_{0}=\lambda \omega_{I}$ (see Lemma 2) is Kähler.

The theory of Hamiltonian 2-forms $\varphi$ does not extend automatically to the almost Kähler case: there is no reason, in general, to suppose that the trace and Pfaffian of $\varphi$ are Poisson-commuting holomorphy potentials, nor can we appeal to the open mapping theorem when $J$ is not integrable. On the other hand, Proposition 3 does generalize in the following sense: if we write $\sigma=\xi+\eta$ and $\pi=\xi \eta$, then $d \xi$ and $d \eta$ are orthogonal and $J \mathrm{~d} \sigma=2 I \mathrm{~d} \lambda$ on the closure of $M_{0}$.

Fortunately, when $\varphi$ is the Ricci form, we can show more.
LEMMA 12. On a weakly self-dual almost Kähler 4-manifold with J-invariant Ricci tensor, $K=J \operatorname{grad}_{g} s$ is a Killing vector field.

Proof. On $M_{0}$, the Ricci tensors of both $\bar{g}=\lambda^{-2} g$ and $g$ are $I$-invariant, and therefore $I \operatorname{grad}_{g} \lambda$ is Killing vector field (with respect to both metrics) [7]. Since $I \mathrm{~d} s=2 J \mathrm{~d} \lambda, J \mathrm{~d} s=2 I \mathrm{~d} \lambda$ and $K$ is a Killing vector field on $M_{0}$. On the other hand if $\lambda$ vanishes identically on an open set $U$ then $g$ is Einstein on $U$, so that $s$ is constant, and $K$ is a trivial Killing vector field. Hence, by continuity, $K$ is a Killing vector field everywhere. \(\square\)

Because of this observation, it is natural to strengthen the definition of Hamiltonian 2-forms in the almost Kähler case: we say that a closed $J$-invariant 2-form $\varphi$ on an almost Kähler 4-manifold is Hamiltonian if its trace-free part $\varphi_{0}$ is a twistor 2-form and its trace $\sigma$ is a momentum map for a Killing vector field.

Note that for any Killing vector field $K, \nabla_{X}(\nabla K)=R_{K, X}^{g}$ and so the 1-jet $\{K, \nabla K\}$ is parallel with respect to a globally defined connection, cf. [35]. Hence if $K$ vanishes on an open set so does $\nabla K$, and therefore $K$ vanishes on any connected component meeting that open set. It follows that if $\varphi$ is Hamiltonian, the open set $M_{0}$ where $\varphi_{0} \neq 0$ is dense or empty in each connected component.

In particular, we obtain the following generalization of Proposition 6.
PROPOSITION 15. Let $(M, g, J, \omega)$ be a connected weakly self-dual almost Kähler 4-manifold with $J$-invariant Ricci tensor. Then one of the following holds:
\begin{itemize}
\item[(i)] $\rho_{0}$ is identically zero; then, $(g, J, \omega)$ is an Einstein almost Kähler 4-manifold; or
\item[(ii)] the scalar curvature $s$ of $g$ is constant, but $\rho_{0}$ is not identically zero; then, $(g, J)$ is obtained from a Kähler surface $(g, I)$ with two distinct constant principal Ricci curvatures, $\lambda$ and $\mu$, in the following manner: $J$ equals to $I$ on the $\lambda$-eigenspace of the Ricci tensor, but to -I on the μ-eigenspace; hence I is compatible with the opposite orientation of $(M, J)$; or
\item[(iii)] $s$ is not constant and $g$ is self-dual; or
\end{itemize}
\begin{itemize}
\item[(iv)] $W^{-}$and $\rho_{0}$ have no zero; then, $\left(\bar{g}=\lambda^{-2} g, I\right)$ is a globally defined extremal Kähler metric of non-constant scalar curvature, which is compatible with the opposite orientation of $(M, J)$.
\end{itemize}

\subsection*{5.2. WEAK SELF-DUALITY, HAMILTONIAN 2-FORMS, AND A CONJECTURE OF GOLDBERG}

The existence of nonintegrable almost Kähler 4-manifolds listed in (i)-(iv) of Proposition 15 appears to be a nontrivial problem. We collect below some remarks and known results on this issue:
\begin{itemize}
\item[-] A long-standing conjecture of Goldberg [28, 47] states that a compact Einstein almost Kähler manifold must be a Kähler-Einstein manifold. The first local examples of nonintegrable Einstein almost Kähler 4-manifolds have been recently discovered in [44, 9]; we shall provide new examples (see Example 2 below), but for all these examples the Ricci tensor and the anti-self-dual Weyl tensor identically vanish.
\item[-] The almost Kähler 4-manifolds described in Proposition 15(ii) have been recently studied in [6]. It is known that there are essentially two examples of homogeneous Kähler surfaces $(M, g, I)$ which give rise to homogeneous non-integrable almost Kähler 4-manifolds described in (ii) of Proposition 15; specifically, $(M, g, I)$ is either isomorphic to $\left(\mathrm{SU}(2) \ltimes \mathrm{Sol}_{2}\right) / \mathrm{U}(1)$ (in the case when the signature of the Hermitian form is (2,2), cf. [48]), or to $\left(\operatorname{Isom}\left(\mathbb{E}^{2}\right) \ltimes \operatorname{Sol}{ }_{2}\right) / \operatorname{SO}(2)$ (in the case when the signature of the Hermitian form is $(0,2)$, cf. [51]); see also Example 3 below. However, there are also many nonhomogeneous examples [4].
\item[-] We believe that there should exist nonintegrable examples of almost Kähler 4-manifolds described in Proposition 15(iii) and (iv). However, as we discuss below, it is not clear how to generalize the constructions of Sections 2 and 3 to obtain such examples.
\end{itemize}

According to Proposition 4, for a weakly self-dual Kähler surface, not only the scalar curvature, but also the Pfaffian of the normalized Ricci form is a momentum map for a Killing vector field. Indeed, this much holds for the trace and the Pfaffian of the normalized 2-form associated to any Hamiltonian 2-form, by Proposition 2.

Hence, one approach to generalize the constructions of Sections 2 and 3 to the almost Kähler case is to study Hamiltonian 2-forms such that the Pfaffian is also a momentum map for a Killing vector field. The following Lemma shows that there are no nonintegrable examples with linearly independent Killing vector fields, which means that there is no direct generalization of the constructions of Section 2.

LEMMA 13. For an almost Kähler 4-manifold with a Hamiltonian 2-form $\varphi$, the Pfaffian $\pi$ of the associated normalized 2-form $\tilde{\varphi}$ is a momentum map for a Killing
vector field $\tilde{K}=J \operatorname{grad}_{g} \pi$ if and only if either $(g, J)$ is a Kähler or $\tilde{K}$ is a constant multiple of $K=J \operatorname{grad}_{g} \sigma$.

Proof. Since $\pi=\frac{1}{4} \sigma^{2}-\lambda^{2}$ we have $\mathrm{d} \pi=\frac{1}{2} \sigma \mathrm{~d} \sigma+\varphi_{0}(J \mathrm{~d} \sigma)$. Straightforward calculation gives
$$\nabla(J d \pi)=\mathrm{d} \sigma \wedge J \mathrm{~d} \sigma-\frac{1}{2}|\mathrm{~d} \sigma|^{2} \omega+\frac{1}{2} \sigma \nabla(J \mathrm{~d} \sigma)-\varphi_{0} \circ \nabla \mathrm{~d} \sigma .$$
Since $K=J \operatorname{grad}_{g} \sigma$ is Killing by assumption, it follows that $J \operatorname{grad}_{g} \pi$ is Killing if and only if $\varphi_{0} \circ \nabla \mathrm{~d} \sigma$ is skew. This is automatic on the open set where $\varphi_{0}$ vanishes, where $d \sigma=0$ and hence $d \pi=0$. Therefore we can assume $\varphi_{0}$ is nonvanishing and write $\varphi_{0}=\lambda \omega_{I}$, where $I$ is a complex structure of the opposite orientation to $J$.

Now $I \circ \nabla \mathrm{~d} \sigma$ is skew if and only if $\nabla \mathrm{d} \sigma$ is $I$-invariant; since $J$ and $I$ commute, this means that the $J$-anti-invariant part of $\nabla \mathrm{d} \sigma$ must be $I$-invariant. But $K=J \operatorname{grad}_{g} \sigma$ is Killing, so the $J$-anti-invariant part of $\left(\nabla_{X} \mathrm{~d} \sigma\right)(Y)$ is equal to $2\left(\nabla_{X} \omega\right)(K, Y)+$ $\left(\nabla_{K} \omega\right)(X, Y)$. The latter is $I$-invariant if and only if for any vector field $X$ we have
$$\left(\nabla_{I X} J\right)(K)=I\left(\nabla_{X} J\right)(K) .$$
Suppose now that $\nabla_{X} J=A \neq 0$ for a vector $X$ at some point. Since $\nabla_{I X} J$, like $A$, is a $J$ -anti-invariant endomorphism, we can write $\nabla_{I X} J=b A+c J A$ for some $b, c \in \mathbb{R}$. Equation (84) now reads $b A(K)+c J A(K)=I A(K)$. Since $A$ commutes with $I$ and anticommutes with $J$, by applying $A$ to the both sides we obtain: $-b K+c J K=-I K$. However $K$ is orthogonal to both $J K$ and $I K$, and so $b=0$ and $c= \pm 1$. Thus, on the open set where $J$ is nonintegrable and $\varphi_{0} \neq 0$, we have $J \mathrm{~d} \sigma= \pm I \mathrm{~d} \sigma= \pm 2 J \mathrm{~d} \lambda$, so $\mathrm{d} \pi$ and $\mathrm{d} \sigma$ are linearly dependent. \(\square\)

The Calabi construction in Section 3 does generalize to the almost Kähler case and generates some new examples of self-dual Ricci-flat almost Kähler 4-manifolds. However, we shall see that there are no nonintegrable examples of nonconstant scalar curvature.

PROPOSITION 16. Let $(M, g, J, \omega)$ be an almost Kähler 4-manifold with $J$-invariant Ricci tensor and a nonvanishing Hamiltonian Killing vector field K. Suppose that the pair $\left(\bar{g}=\lambda^{-2} g, I\right)$ is Kähler, where $\lambda$ is a momentum map for a nonzero multiple of $K$, and $I$ is equal to $J$ on $\operatorname{span}(K, J K)$, but to $-J$ on the orthogonal complement of $\operatorname{span}(K, J K)$.

Then either $J$ is integrable, or $(g, \omega)$ is given explicitly by
$$\begin{aligned}
& g=\frac{W}{z}\left(z^{2} g_{\Sigma}+\mathrm{d} z^{2}\right)+\frac{z}{W}\left(\mathrm{~d} t+\frac{V}{z} \mathrm{~d} z+\beta\right)^{2}, \\
& \omega=z W \omega_{\Sigma}+\mathrm{d} z \wedge\left(\mathrm{~d} t+\frac{V}{z} \mathrm{~d} z+\beta\right),
\end{aligned}$$
where $g_{\Sigma}$ is a metric on 2 -manifold $\Sigma$ with area form $\omega_{\Sigma}, \beta$ is a 1 -form on $\Sigma$ with $d \beta=W \omega_{\Sigma}$, and $V+i W$ is an arbitrary holomorphic function on $\Sigma$.

Conversely any such metric satisfies the above hypotheses, and $J$ is integrable if and only if the function $W$ is constant.

Proof. Without loss of generality, we take $\lambda=z$ to be a momentum map for $K$ (with respect to $\omega$ ). As in Proposition 13, cf. LeBrun [37], we may introduce coordinates such that
$$\begin{aligned}
& g=\mathrm{e}^{u} w\left(\mathrm{~d} x^{2}+\mathrm{d} y^{2}\right)+w \mathrm{~d} z^{2}+w^{-1}(\mathrm{~d} t+\alpha)^{2} \\
& \omega=\mathrm{e}^{u} w \mathrm{~d} x \wedge \mathrm{~d} y+\mathrm{d} z \wedge(\mathrm{~d} t+\alpha) \\
& \bar{\omega}=z^{-2}\left(-\mathrm{e}^{u} w \mathrm{~d} x \wedge \mathrm{~d} y+\mathrm{d} z \wedge(\mathrm{~d} t+\alpha)\right)
\end{aligned}$$
where $\bar{\omega}$ is the Kähler form of $I$ with respect to $\bar{g}=z^{-2} g$. The integrability of $I$ together with the closedness of $\omega$ and $\bar{\omega}$ yields
$$\mathrm{e}^{u} w=h(x, y) z, \quad \mathrm{~d} \alpha=-w_{x} \mathrm{~d} y \wedge \mathrm{~d} z+w_{y} \mathrm{~d} x \wedge \mathrm{~d} z+h(x, y) \mathrm{d} x \wedge \mathrm{~d} y$$
from which we obtain the integrability condition
$$w_{x x}+w_{y y}=0 .$$
The Ricci tensor of $g$ is $J$-invariant if and only if
$$\left(\frac{z u_{z}-2}{z w}\right)_{x}=0 \quad \text { and } \quad\left(\frac{z u_{z}-2}{z w}\right)_{y}=0$$
so that we can write $z u_{z}=f(z) z w-2$. Since $e^{u} w=h(x, y) z$, we obtain $(z w)_{z}+$ $f(z) / z(z w)^{2}=0$.
The latter is explicitly integrated, and we get
$$z w(x, y, z)=\frac{1}{F(z)+G(x, y)}$$
for some functions $F(z)$ and $G(x, y)$. By substituting into (87) we discover that either $F$ or $G$ must be constant.

If $G$ is constant, then $w_{x}=w_{y}=0$, i.e., $g$ is of Calabi type and $J$ is integrable.
Consider now the case when $F$ is a constant; then, $w=W / z$ and $\mathrm{e}^{u}=z^{2} \mathrm{e}^{U}$, where $W(x, y)$ is a positive harmonic function and $\mathrm{U}(x, y)$ is an arbitrary function of $(x, y)$; the almost Kähler structure $(g, \omega)$ takes the form (85)-(86) where:
\begin{itemize}
\item[-] $g_{\Sigma}=\mathrm{e}^{U}\left(\mathrm{~d} x^{2}+\mathrm{d} y^{2}\right)$;
\item[-] $\omega_{\Sigma}=\mathrm{e}^{U} \mathrm{~d} x \wedge \mathrm{~d} y$;
\item[-] $W$ is a positive harmonic function on $\Sigma$;
\item[-] $\alpha$ satisfies $\mathrm{d} \alpha=-W_{y} \mathrm{~d} x \wedge \mathrm{~d} z / z+W_{x} \mathrm{~d} y \wedge \mathrm{~d} z / z+W \omega_{\Sigma}$ and we can locally choose $t$ so that $\alpha=V \mathrm{~d} z / z+\beta$, where $V$ is a harmonic conjugate of $W$ and $\mathrm{d} \beta=W \sigma_{\Sigma}$.
\end{itemize}
This almost Hermitian structure ( $g, J, \omega$ ) is almost Kähler with $J$-invariant Ricci tensor, since $w, \mathrm{e}^{u}$ and $\alpha$ solve the required equations. \(\square\)

One directly calculates the normalized scalar curvature $s$ of the metric (85): it is given by
$$s=\frac{1}{6 z W \mathrm{e}^{U}}\left(U_{x x}+U_{y y}+2 \mathrm{e}^{U}\right) .$$

On a weakly self-dual almost Kähler 4-manifold with $J$-invariant Ricci tensor, we have seen that $s$ is a momentum map for a Killing vector field. However, $s$ cannot be a multiple of $z$ unless it vanishes. Hence, this construction does not yield any nonintegrable weakly self-dual almost Kähler metrics of Calabi type with nonconstant scalar curvature. However, it does provide the following new examples of self-dual Ricci-flat strictly almost Kähler 4-manifolds.

EXAMPLE 2. Let $(g, J, \omega)$ be given by (85) and suppose that $s=0$; this means that $U$ is a solution of the Liouville equation, i.e., that $g_{\Sigma}$ is the standard metric on an open subset of $S^{2}$, while $H=W+i V$ is a nonconstant holomorphic function on $\Sigma$ with positive real part. If we write $z=r$, we see that the metric
$$g=\frac{W}{r}\left(\mathrm{~d} r^{2}+r^{2} g_{S^{2}}\right)+\frac{r}{W}(\mathrm{~d} t+\alpha)^{2}$$
is given by applying the Gibbons-Hawking Ansatz using the harmonic function $W / r$, which is invariant under dilation with weight -1 in the sense that
$$r \frac{\partial}{\partial r}\left(\frac{W}{r}\right)=-\frac{W}{r} .$$
(In fact this is the natural scaling weight for $W / r$, since it is the Higgs field of an abelian monopole on $\mathbb{R}^{3}$.)

This class of Gibbons-Hawking metrics has been studied before in [16] and [18]. In addition to the triholomorphic Killing vector field $\partial / \partial t$, these metrics also admit a triholomorphic homothetic vector field $r \partial / \partial r$. Therefore, by [27], the local quotient by $r \partial / \partial r$ is a hyperCR Einstein-Weyl space. In this case the quotient Einstein-Weyl structure was obtained explicitly in [16] and is an Einstein-Weyl space with a geodesic symmetry.

The reader is referred to these references for more information. However, to the best of our knowledge, the observation that these metrics are almost Kähler is new. Note that the Kähler form is not an eigenform of the Weyl tensor, showing that the solutions are different from the previously known examples of Nurowski-Przanowski [44] and Tod, which were obtained by applying the Gibbons-Hawking Ansatz to a translation-invariant harmonic function.

We next use the rough classification given by Proposition 15 to obtain the following partial result which motivates the further study of compact weakly self-dual almost Kähler 4-manifolds with $J$-invariant Ricci tensor:

THEOREM 6. Suppose that there exists a compact weakly self-dual almost Kähler 4-manifold $(M, g, J, \omega)$ with $J$-invariant Ricci tensor, for which the almost complex structure $J$ is not integrable. Then one of the following two alternatives holds:
\begin{itemize}
\item[(i)] The scalar curvature of $g$ is a negative constant; then $M$ admits an Einstein, non-integrable almost Kähler structure; or
\item[(ii)] $(M, g, J, \omega)$ belongs to case (iv) of Proposition 15, and the globally defined Kähler structure $(\bar{g}, I)$ is isomorphic to an extremal Kähler metric which is not locally of cohomogeneity one, on a minimal ruled surface $S=\mathrm{P}(\mathcal{O} \oplus L) \rightarrow \Sigma_{\mathbf{g}}$ with $\mathbf{g} \geqslant 1$ and $\operatorname{deg} L>0$.
\end{itemize}

Proof. We inspect the possible compact nonintegrable almost Kähler 4-manifolds given by (i)-(iv) of Proposition 15.

The case of constant scalar curvature is described by Proposition 15(i), (ii). Our claim then follows by [47] and [6, Th.2].

Suppose that $s$ is not constant, i.e., that $K=J \operatorname{grad}_{g} s$ is a nontrivial Killing vector field by Lemma 12. Let $x_{0} \in M$ be a zero of $K$; then, the isotropy subgroup $H\left(x_{0}\right)$ of the connected group of isometries of $(M, g)$ is a compact group of dimension at least one; one can therefore take an $S^{1}$ in $H\left(x_{0}\right)$. Hodge theory implies that on a compact almost Kähler manifold any isometry which is homotopic to the identity inside the group of diffeomorphisms is a symplectomorphism (see e.g. [39]); hence the chosen isometric $S^{1}$-action is symplectic with respect to $\omega$. Since $x_{0}$ is a fixed point of the $S^{1}$ -action, we obtain a Hamiltonian $S^{1}$-action on $(M, \omega)$ [40]. The manifold is then equivariantly (and orientedly) diffeomorphic to a rational or a ruled complex surface endowed with a holomorphic circle action [10, 2, 34]. Moreover, in this case ( $M, g, J, \omega$ ) is given by Proposition 15 (iii) or (iv).

Consider first the case (iii). Since $s$ is not constant, the self-dual Weyl tensor $W^{+}$ does not vanish [5, Cor.1]. By the Chern-Weil formulae, the signature of $M$ is strictly positive and, therefore, $M$ is diffeomorphic to $\mathrm{CP}^{2}$ [11]. Combining the results of [30] and [46], one sees that on $\mathrm{CP}^{2}$ the only self-dual conformal structure with nontrivial (conformal) Killing vector field is the standard one. Thus, modulo diffeomorphisms, we may assume that $g$ is conformal to the standard Kähler metric $\left(g_{0}, \omega_{0}\right)$. Since $\omega$ and $\omega_{0}$ are both harmonic self-dual 2-forms on $\left(\mathrm{CP}^{2}, g_{0}\right)$, and since $b^{+}\left(\mathrm{CP}^{2}\right)=1$, we conclude that $\omega=\operatorname{const} . \omega_{0}$, showing that $J$ is integrable, a contradiction.

Suppose ( $M, g, J, \omega$ ) is as in Proposition 15(iv). Now $\rho_{0}$ determines an integrable almost complex structure $I$ compatible with $g$ and with the opposite orientation of $(M, J)$, such that $\left(\bar{g}=\lambda^{-2} g, I\right)$ is an extremal Kähler metric with $\operatorname{Igrad}_{\bar{g}} \bar{s}=$ const.K. Denote by $\bar{M}$ the smooth manifold $M$ endowed with the orientation induced by $I$. Thus, the oriented smooth 4-manifolds $M$ and $\bar{M}$ both admit complex structures. Since $M$ is the underlying smooth manifold of a rational or a ruled complex surface, we conclude as in the proof of Theorem 5 that the complex surface $(\bar{M}, I)$ is a ruled surface of the form $\mathrm{P}(E)$, where $E \rightarrow \Sigma_{\mathbf{g}}$ is a holomorphic rank 2 bundle over a compact Riemann surface $\Sigma_{\mathbf{g}}$ of genus $\mathbf{g}$, and which splits as $E=\mathcal{O} \oplus L$ for a holomorphic line bundle $L$ of degree $\operatorname{deg}(L)>0$.

We have to prove that $\mathbf{g} \geqslant 1$. Indeed, if $\mathbf{g}=0$, we obtain the Hirzebruch surface $F_{k}=\mathrm{P}(\mathcal{O} \oplus \mathcal{O}(-k))$, where $k$ is a positive integer. As we have already observed in the proof of Theorem 5, the extremal Kähler metrics on these surfaces are the Calabi
cohomogeneity-one U(2)-metrics, i.e. $\bar{g}$ is given by the Calabi construction (67)-(68); since $g=$ const. $\bar{s}^{2} \bar{g}$, it follows that $g$ is a cohomogeneity-one metric as well and therefore $\operatorname{grad}_{\bar{g}} \bar{s}=$ const.grad $_{g} s$, showing that $J K=I K$. Since $s$ is not constant, by Lemma 13, $J$ is integrable on the open dense subset where $d s \neq 0$, hence everywhere. We thus conclude that $\mathbf{g} \geq 1$. Note that the above local argument applies to any extremal Kähler $\bar{g}$ which is locally of cohomogeneity one, so that the last part of the theorem also follows. \(\square\)

We do not have any examples in case (ii) of the above theorem. Indeed, the only examples we know of extremal Kähler metrics on the minimal ruled surfaces in (ii) are locally cohomogeneity-one Calabi-type metrics [49,50].

\subsection*{5.3. ALMOST KÄHLER 4-MANIFOLDS OF CONSTANT LAGRANGIAN SECTIONAL CURVATURE}

In this section we deduce another global result from Theorem 6. An almost Kähler 4-manifold $(M, g, \omega)$ is said to have (pointwise) constant Lagrangian sectional curvature if the sectional curvature of $g$, at each point of $M$, is constant on the set of Lagrangian 2-planes at that point-recall that the latter are the planes $X \wedge Y$ with $\omega(X, Y)=0$. One can make the same definition for almost Kähler manifolds of any dimension, but for $2 n>4$, any almost Kähler $2 n$-manifold of constant Lagrangian sectional curvature is in fact Kähler with constant holomorphic sectional curvature [23, 24]. Conversely, it is easy to see that any complex space form has constant Lagrangian sectional curvature (see, e.g., [25]).

In four dimensions, the situation is more interesting. A simple local calculation (cf. e.g. [5]) shows that an almost Kähler 4-manifold has constant Lagrangian sectional curvature if and only if the Ricci tensor is $J$-invariant, the Weyl tensor is self-dual, and the Kähler form is one of its roots (i.e., $M$ has Hermitian Weyl tensor in the sense of [3]).

The following homogeneous example shows that the integrability for almost Kähler 4-manifolds with constant Lagrangian sectional curvature does not follow locally (nor even for complete metrics).

EXAMPLE 3. Consider the homogeneous Kähler surface $M=\left(\mathrm{SU}(2) \times \mathrm{Sol}_{2}\right) / \mathrm{U}(1)$, where $\mathrm{Sol}_{2}$ denotes the real two-dimensional solvable subgroup of upper triangular matrices in $\mathrm{SL}_{2}(\mathrm{R})$.

We take the unique left-invariant Kähler structure $(g, I)$ on $M$, determined by the property that the constant principal Ricci curvatures are equal to $(-1,+1)$, cf. [48]. According to Proposition 15(ii), $(M, g)$ admits an almost Kähler structure $J$ with $J$-invariant Ricci tensor. Since the scalar curvature of $g$ is zero, $g$ is self-dual (with the orientation opposite to $I$ ) [26]; furthermore, $J$ is not integrable [6], and by using the general formulae in [12, Ch. 7] one easily checks that $(M, g, J)$ has constant Lagrangian sectional curvature.

In contrast to this example, there were a number of reasons [3, 5] to believe that a compact almost Kähler 4-manifold of constant Lagrangian curvature must be a selfdual Kähler metric. The conjectured integrability of the almost complex structure has been proved under some additional assumptions on curvature [5] or the topology [3] of the manifold, but the general question was left open. As a consequence of Theorem 6 we are now able to give a positive answer.

COROLLARY 1. A compact, four-dimensional, almost Kähler manifold has constant Lagrangian sectional curvature if and only if it is a Kähler self-dual surface.

Proof. Suppose $(M, g, J, \omega)$ is a compact almost Kähler 4-manifold of constant Lagrangian sectional curvature, but for which $J$ is not integrable. According to [5, Th. 2] the scalar curvature $s$ of $g$ is not constant; then, by Theorem 6, the smooth manifold $M$ is diffeomorphic to a minimal ruled surface. Since any such surface admits an orientation reversing involution, we conclude that $M$ carries a complex structure which is compatible with the orientation induced by $\omega$. Then, by [3, Cor. 2], the almost complex structure $J$ must be integrable, contradicting our assumption. \(\square\)

\section*{Acknowledgements}

The first author was supported in part by a FCAR grant NC-7264 and by NSERC grant OGP0023879, the second author by the Leverhulme Trust and the William Gordon Seggie Brown Trust. All three authors are members of EDGE, Research Training Network HPRN-CT-2000-00101, supported by the European Human Potential Programme.

\section*{References}
\begin{itemize}
\item[1.] Abreu, M.: Kähler geometry of toric varieties and extremal metrics, Internat. J. Math. 9 (1998), 641-651.
\item[2.] Ahara, K. and Hattori, A.: Four dimensional symplectic $S^{1}$-manifolds admitting moment map, J. Fac. Sci. Univ. Tokyo, Sect. IA 38 (1991), 251-298.
\item[3.] Apostolov, V. and Armstrong, J.: Symplectic 4-manifolds with Hermitian Weyl tensor, Trans. Amer. Math. Soc. 352 (2000), 4501-4513.
\item[4.] Apostolov, V., Armstrong, J. and Draghici, T.: Local rigidity of certain classes of almost Kähler 4-manifolds, Ann. Global Annal. Geom. 21 (2002), 151-176.
\item[5.] Apostolov, V. and Draghici, T.: Almost Kähler 4-manifolds with J-invariant Ricci tensor and special Weyl tensor, Quart. J. Math. 51 (2000), 275-294.
\item[6.] Apostolov, V., Draghici, T. and Moroianu, A.: A splitting theorem for Kähler manifolds with constant eigenvalues of the Ricci tensor, Internat. J. Math. 12 (2001), 769-789.
\item[7.] Apostolov, V. and Gauduchon, P.: The Riemannian Goldberg-Sachs Theorem, Internat. J. Math. 8 (1997), 421-439.
\item[8.] Apostolov, V. and Gauduchon, P.: Self-dual Einstein Hermitian 4-manifolds, Ann. Scuola Norm. Sup. Pisa Cl. Sci (5) 1 (2002), 203-243.
\item[9.] Armstrong, J.: An ansatz for almost-Kähler, Einstein 4-manifolds, Preprint 1997, J. reine angew. Math. 542 (2002), 53-84.
\end{itemize}
\begin{itemize}
\item[10.] Audin, M.: Hamiltoniens périodiques sur les variétés symplectiques de dimension 4, In: C. Albert (ed.) Géométrie symplectique et mécanique, Proc. 1988, Lecture Notes in Math. 1416, Springer, New York, 1990.
\item[11.] Barth, W., Peters, C. and Van de Ven, A.: Compact Complex Surfaces, Springer-Verlag, Berlin, 1984.
\item[12.] Besse, A. L.: Einstein Manifolds, Ergeb. Math. Grenzgeb. 3, Springer-Verlag, Berlin, 1987.
\item[13.] Bryant, R.: Bochner-Kähler metrics, J. Amer. Math. Soc. 14 (2001), 623-715.
\item[14.] Calabi, E.: Extremal Kähler metrics, In: Seminar on Differential Geometry, Princeton Univ. Press, 1982, pp. 259-290.
\item[15.] Calabi, E.: Extremal Kähler metrics II, In: I. Chavel and H. M. Farkas (eds), Differential Geometry and Complex Analysis, Springer-Verlag, New York, 1985.
\item[16.] Calderbank, D. M. J. and Pedersen, H.: Selfdual spaces with complex structures, Einstein-Weyl geometry and geodesics, Ann. Inst. Fourier 50 (2000), 921-963.
\item[17.] Calderbank, D. M. J. and Pedersen, H.: Selfdual Einstein metrics with torus symmetry, J. Differential Geom. 60 (2002), 485-521.
\item[18.] Calderbank, D. M. J. and Tod, K. P.: Einstein metrics, hypercomplex structures and the Toda field equation, Differential Geom. Appl. 14 (2001), 199-208.
\item[19.] Carrell, J., Howard, A. and Kosniowski, C.: Holomorphic vector fields on compact complex manifolds, Math. Ann. 204 (1973), 73-81.
\item[20.] Chen, B.-Y.: Some topological obstructions to Bochner-Kähler metrics and their applications, J. Differential Geom. 13 (1978), 574-588.
\item[21.] Derdziński, A.: Self-dual Kähler manifolds and Einstein manifolds of dimension four, Compositio Math. 49 (1983), 405-433.
\item[22.] Draghici, T.: On some 4-dimensional almost Kähler manifolds, Kodai Math. J. 18 (1995), 156-163.
\item[23.] Falcitelli, M. and Farinola, A.: Six-dimensional almost Kähler manifolds with pointwise constant antiholomorphic sectional curvature, Riv. Mat. Univ. Parma (5) 6 (1997), 143-156.
\item[24.] Falcitelli, M., Farinola, A. and Kassabov, O.: Almost Kähler manifolds whose antiholomorphic sectional curvature is pointwise constant, Rend. Mat. Appl. (7) 18 (1998), 151-166.
\item[25.] Ganchev, G.: On Bochner curvature tensors in almost Hermitian manifolds, Pliska Studia Mate. Bulgarica 9 (1987), 33-43.
\item[26.] Gauduchon, P.: Surfaces kählériennes dont la courbure vérifie certaines conditions de positivité, In: Géométrie riemannienne en dimension 4, Sém. A. Besse, 1978/79.
\item[27.] Gauduchon, P. and Tod, K. P. Hyperhermitian metrics with symmetry, J. Geom. Phys. 25 (1998), 291-304.
\item[28.] Goldberg, S. I.: Integrability of almost Kähler manifolds, Proc. Amer. Math. Soc. 21 (1969), 96-100.
\item[29.] Guillemin, V.: Kähler structures on toric varieties, J. Differential Geom. 40 (1994), 285-309.
\item[30.] Gursky, M.: Conformal vector fields on four-manifolds with negative scalar curvature, Math. Z. 232 (1999), 265-273.
\item[31.] Hwang, A. and Maschler, G.: Central Kähler metrics with non-constant central curvature, Preprint 2000.
\item[32.] Jelonek, W.: Compact Kähler surfaces with $\delta W^{-}=0$, Differential Geom Appl. 16 (2002), 267-276.
\item[33.] Jelonek, W.: Extremal Kähler AC-surfaces, Preprint 2001.
\end{itemize}
\begin{itemize}
\item[34.] Karshon, Y.: Periodic Hamiltonian flows on four-dimensional manifolds, In: Contact and Symplectic Geometry (Cambridge, 1994), Publ. Newton Inst. 8, Cambridge Univ. Press, Cambridge, 1996, pp. 43-47.
\item[35.] Kostant, B.: Holonomy and the Lie algebra of infinitesimal motions of a Riemann manifold, Trans. Amer. Math. Soc. 80 (1955), 528-542.
\item[36.] Kotschick, D.: Orientations and geometrisations of compact complex surfaces, Bull. London Math. Soc. 29 (2) (1997), 145-149.
\item[37.] LeBrun, C. R.: Explicit self-dual metrics on $\mathrm{C} P^{2} \cdots \mathrm{C} P^{2}$, J. Differential Geom. 34 (1991), 223-253.
\item[38.] LeBrun, C. R. and Singer, M.: Existence and deformation theory of scalar flat Kähler metrics on compact complex surfaces, Invent. Math. 112 (1993), 273-313.
\item[39.] Lichnerowicz, A.: Théorie des groupes de transformations, Dunod, Paris, 1958.
\item[40.] McDuff, D.: The moment map for circle actions on symplectic manifolds, J. Geom. Phys. 5 (1988), 149-160.
\item[41.] Maruyama, M.: On automorphism groups of ruled surfaces, J. Math. Kyoto Univ. 11 (1971), 89-112.
\item[42.] Maschler, G.: Central Kähler metrics, Preprint, 2000.
\item[43.] Matsumoto, M. and Tanno, S. On Kähler spaces with parallel or vanishing Bochner curvature tensor, Tensor N.S. 27 (1973), 291-294.
\item[44.] Nurowski, P. and Przanowski, M.: A four-dimensional example of Ricci flat metric admitting almost Kähler non-Kähler structure, Classical Quantum Gravity 16 (3) (1999), L9-L13.
\item[45.] Pontecorvo, M.: On twistor spaces of anti-self-dual Hermitian surfaces, Trans. Amer. Math. Soc. 331 (1992), 653-661.
\item[46.] Poon, Y.-S.: Compact self-dual manifolds with positive scalar curvature, J. Differential Geom. 24 (1986), 97-132.
\item[47.] Sekigawa, K.: On some compact Einstein almost Kähler manifolds, J. Math. Soc. Japan 36 (1987), 677-684.
\item[48.] Shima, H.: On homogeneous Kähler manifolds with non-degenerate canonical Hermitian form of signature (2, 2(n-1)), Osaka J. Math. 10 (1973), 477-493.
\item[49.] Tønnesen-Friedman, C.: Extremal Kähler metrics on minimal ruled surfaces, J. reine angew. Math. 502 (1998), 175-197.
\item[50.] Tønnesen-Friedman, C.: Extremal Kähler metrics and Hamiltonian functions II, Glasgow Math. J. 44 (2002), 241-253.
\item[51.] Wall, C. T. C.: Geometric structures on compact complex analytic surfaces, Topology 25 (1986), 119-153.
\end{itemize}
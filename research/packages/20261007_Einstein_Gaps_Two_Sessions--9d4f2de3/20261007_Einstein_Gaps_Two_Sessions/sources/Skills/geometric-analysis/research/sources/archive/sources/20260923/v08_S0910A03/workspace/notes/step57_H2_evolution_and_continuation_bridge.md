# Step 57: H₂ evolution on the exact cutoff flow and W^{1,p} curvature bridge

> **Step 58 corrections.** Preserve the term-level signed-Hessian calculation and
> the implication \(T,\nabla T\in L^p\ (p>4)\Rightarrow T\in L^\infty\).
> Sections 8.1--8.3 are superseded by
> `step58_critical_to_subcritical_bridge.md`: the first-exit estimate must not use
> \(Y(0)\), and the \(q=3\) Sobolev variable is \(aF_T^{3/2}\), not
> \(a^{1/2}F_T^{3/2}\). Sections 9.2(a,c,d) and the common-time conclusion in
> §10 are not established: bounded curvature does not control evolving cutoff
> jets across the degenerate collar. A finite coupled continuation hierarchy and
> fixed-background restart conversion remain necessary.

Session: S0910A03. Agent2 / Constructor. Phase: Execute.

## 0. Purpose

This note achieves two things:

1. **Complete term-by-term derivation** of the unweighted shifted-curvature energy
   $H_2^\alpha = \int\eta_\alpha^2(1+|T|^2)\,d\mu$ on the exact normalized cutoff
   flow from Step 56, compared to A01 step25.

2. **The W^{1,p}\to L^\infty$ continuation bridge**: the Step 56 base pair plus
   Sobolev embedding produces pointwise curvature control, replacing the infinite
   staggered hierarchy with a finite-order argument.

The first item is a valid input to the critical bridge. The second yields
unweighted pointwise curvature on a positive-time slab, but does not alone close
the finite-regularity restart problem across the degenerate collar.

## 1. Setup

**Flow.** $\partial_tg=-2aE$, $E=\operatorname{Ric}_g+g$, $a=\chi^2$, on a
closed Riemannian manifold $(M^n,g_0)$, $n=4$. Smooth existence on $[0,T)$ is
provided by Step 56 Theorem 4.3.

**Shifted curvature.**
\[
 G=\frac{g\owedge g}{2(n-1)},\qquad T=\operatorname{Rm}+G,\qquad U=aT.
\tag{1.1}
\]
Key properties: $\operatorname{Ric}(G)=g$, so $\operatorname{Ric}(T)=E$;
$\nabla G=0$; $|G|\le C_n$; $|T|$ is comparable to $|\operatorname{Rm}|+O(1)$.

**Buffered support.** Fix one selected support $\alpha$:
\[
 \chi_\alpha=1\text{ on }B_{5r},\quad
 \operatorname{supp}\chi_\alpha\subset B_{6r},\quad
 \eta_\alpha=1\text{ on }B_{6r},\quad
 \operatorname{supp}\eta_\alpha\subset B_{7r}.
\tag{1.2}
\]
Write $\chi=\chi_\alpha$, $\eta=\eta_\alpha$, $a=\chi^2$. The standing
cancellations on the buffer collar $\{6r<d<7r\}$:
\[
 a=0,\quad da=0 \text{ on }\operatorname{supp}(d\eta),\qquad
 \nabla a\cdot\nabla\eta=0\text{ everywhere}.
\tag{1.3}
\]

**Standing cutoff identities.**
\[
 \nabla a=2\chi\nabla\chi,\qquad
 \frac{|\nabla a|^2}{a}=4|\nabla\chi|^2\le\frac{4C_\chi^2}{r^2},\qquad
 \nabla^2a=2\,d\chi\otimes d\chi+2\chi\nabla^2\chi.
\tag{1.4}
\]

**Energies.**
\[
 H_2=\int\eta^2F_T^2\,d\mu,\quad
 D_2=\int\eta^2a|\nabla T|^2\,d\mu,\qquad
 F_T=(1+|T|^2)^{1/2}.
\tag{1.5}
\]
Because $\nabla G=0$: $|\nabla T|=|\nabla\operatorname{Rm}|$, so $D_2$ equals
A01's dissipation $\int\eta^2a|\nabla\operatorname{Rm}|^2$ exactly.

## 2. Time derivative of H₂: decomposition

\[
 \frac{d}{dt}H_2
 =\underbrace{\int\eta^2\partial_t(F_T^2)\,d\mu}_{(\mathrm{I})}
 +\underbrace{\int\eta^2F_T^2\,\partial_t(d\mu)}_{(\mathrm{II})}.
\tag{2.1}
\]

### (II) Volume-form term

Under $h=\partial_tg=-2aE$:
\[
 \partial_t(d\mu)=-a\,\operatorname{tr}_g(E)\,d\mu,
\qquad \operatorname{tr}_g(E)=\operatorname{scal}+n.
\tag{2.2}
\]
Hence
\[
 |(\mathrm{II})|\le C_n\int\eta^2aF\cdot F_T^2\,d\mu\le C_n\int\eta^2aF_T^3\,d\mu,
\tag{2.3}
\]
since $|s+n|\le\sqrt{n}|E|\le C_nF\le C_nF_T$. **Identical to A01 eq.\ (2.4).**

### (I) Norm variation

$\partial_t(F_T^2)=\partial_t(1+|T|^2)=\partial_t|T|^2$. This has two parts:
\[
 \partial_t|T|^2_g=2\langle T,\partial_tT\rangle_g+(\text{metric variation of }|T|^2_g).
\tag{2.4}
\]

**Metric variation.** $|T|^2=g^{ip}g^{jq}g^{kr}g^{ls}T_{ijkl}T_{pqrs}$.
Each $\partial_tg^{ij}=2aE^{ij}$ gives a contribution bounded by $Ca|E||T|^2$.
With 4 inverse metrics:
\[
 |(\text{metric variation of }|T|^2)|\le4\cdot Ca|E||T|^2\le C_naF_T^3.
\tag{2.5}
\]
**Same structure as A01 eq.\ (2.5)** with $T$ replacing $\operatorname{Rm}$.

### Evolution of $T$

\[
 \partial_tT=\partial_t\operatorname{Rm}+\partial_tG.
\tag{2.6}
\]

**$\partial_t\operatorname{Rm}$**: under $h=-2aE=-2a\operatorname{Ric}-2ag$:
\[
 \partial_t\operatorname{Rm}
 =\underbrace{a(\Delta_L\operatorname{Rm}+Q(\operatorname{Rm}))}_{(A)}
 +\underbrace{2(\nabla a)\otimes_{\rm sym}(\nabla E)}_{(B)}
 +\underbrace{(\nabla^2a)\owedge E}_{(C)}
 +\underbrace{a\operatorname{Rm}*E}_{(D_1)},
\tag{2.7}
\]
where $(A)$ comes from the $-2a\operatorname{Ric}$ part via Hamilton's formula,
$(B),(C)$ from the Leibniz rule on $\nabla^2(aE)$, and $(D_1)$ collects the
algebraic $\operatorname{Rm}*h$ terms.  The normalization part $h_{\rm conf}=-2ag$
contributes to (C) via $\nabla^2(ag)=(\nabla^2a)\cdot g$ (since $\nabla g=0$)
and to $(D_1)$ via $\operatorname{Rm}*(-2ag)=-2a\operatorname{Rm}$.

**$\partial_tG$**: from $G=g\owedge g/(2(n-1))$ with the KN convention
$(g\owedge g)_{ijkl}=2(g_{ik}g_{jl}-g_{il}g_{jk})$, the Leibniz rule gives
$\partial_t(g\owedge g)=h\owedge g+g\owedge h=2(h\owedge g)$ for symmetric $h$.
Hence
\[
 \partial_tG=\frac{h\owedge g}{n-1}=-\frac{2a}{n-1}(E\owedge g).
\tag{2.8}
\]
This is purely algebraic: $|\partial_tG|\le C_na|E|\le C_naF_T$. It adds to the
Type (D) terms:
\[
 (D)=a\operatorname{Rm}*E-\frac{a}{n-1}E\owedge g=aT*E+(\text{bounded corrections}).
\tag{2.9}
\]

## 3. Type (A): Bochner pair

We work directly with $T$, not $\operatorname{Rm}$, to avoid double-counting.
The principal part of $\partial_tT$ gives the Bochner term $a\Delta_LT$
(from Hamilton's formula applied to $\operatorname{Rm}$, plus the identity
$\Delta_LG=\operatorname{Rm}*G$ which is algebraic).  After contraction with
$2T$, the rough-Laplacian Bochner identity gives:
\[
 2\langle T,a\Delta T\rangle=a\Delta|T|^2-2a|\nabla T|^2.
\tag{3.1}
\]
The difference $\Delta_LT-\Delta T$ is an algebraic contraction
$\operatorname{Rm}*T$, absorbed into Type (D).  No separate shifted-curvature
term is needed because $\Delta|T|^2$ already includes the full $T=\operatorname{Rm}+G$.

**Integration of the Bochner pair on $\eta^2$:**
\[
 \int\eta^2a\Delta|T|^2\,d\mu=-\int\nabla(\eta^2a)\cdot\nabla|T|^2\,d\mu.
\tag{3.2}
\]
Expanding $\nabla(\eta^2a)=2\eta a\nabla\eta+\eta^2\nabla a$:

- **Cross term:** $\int2\eta a(\nabla\eta)\cdot\nabla|T|^2=0$ by (1.3):
  on $\operatorname{supp}(d\eta)$, $a=0$.

- **Cutoff term:** Using $\nabla|T|^2=2\langle T,\nabla T\rangle$ and Young with parameter $\varepsilon$:
\[
 |\nabla a\cdot\langle T,\nabla T\rangle|
 \le\frac\varepsilon2a|\nabla T|^2
 +\frac{1}{2\varepsilon}\frac{|\nabla a|^2}{a}|T|^2
 \le\frac\varepsilon2a|\nabla T|^2+\frac{2C_\chi^2}{\varepsilon r^2}|T|^2.
\tag{3.3}
\]

**Collection of the Bochner pair:**
\[
 \int\eta^2\bigl(a\Delta|T|^2-2a|\nabla T|^2\bigr)\,d\mu
 \le-(2-\varepsilon)D_2+\frac{C}{\varepsilon r^2}H_2.
\tag{3.4}
\]
**This matches A01 eq.\ (2.12)** exactly.  No extra shifted-curvature term
appears because $\Delta|T|^2$ already contains the full information.

## 4. Type (B): first-derivative cutoff

After contraction with $2\eta^2T$:
\[
 |2\eta^2(\nabla a)(\nabla E)*T|
 \le C\eta^2|\nabla a||\nabla\operatorname{Rm}||T|.
\tag{4.1}
\]
(Here $|\nabla E|=|\nabla\operatorname{Ric}|\le C|\nabla\operatorname{Rm}|=C|\nabla T|$.)
Young with parameter $\varepsilon'$:
\[
 \int|(\text{Type B})|\le\varepsilon'D_2+\frac{C}{\varepsilon' r^2}H_2.
\tag{4.2}
\]
**Identical to A01 eq.\ (2.14).**

## 5. Type (C): Hessian of $a$, integration by parts

After contraction with $2\eta^2T$, the Type (C) terms have the form
\[
 I_C=\int\eta^2(\nabla^2a)_{ij}\mathcal T^{ij}\,d\mu,
 \qquad |\mathcal T|\le C|E||T|\le CF_T^2.
\tag{5.1}
\]

**Integration by parts** (the central signed-Hessian mechanism):
\[
 I_C=-\int\nabla_ka\,\nabla_k(\eta^2\mathcal T)\,d\mu
 =-\int\eta^2(\nabla a)\cdot(\nabla\mathcal T)\,d\mu
 -2\int\eta(\nabla\eta)(\nabla a)\mathcal T\,d\mu.
\tag{5.2}
\]
The second integral vanishes by (1.3).  For the first:
\[
 |\nabla\mathcal T|\le C(|\nabla E||T|+|E||\nabla T|)
 \le C|\nabla T|F_T.
\tag{5.3}
\]
Therefore
\[
 |I_C|\le\int\eta^2|\nabla a||\nabla T|F_T\,d\mu
 \le\varepsilon''D_2+\frac{C}{\varepsilon''r^2}H_2.
\tag{5.4}
\]
(Using Young: $|\nabla a||\nabla T|F_T\le(\varepsilon/2)a|\nabla T|^2+(1/(2\varepsilon))(|\nabla a|^2/a)F_T^2$.)

**Identical to A01 eq.\ (2.17).** Every Hessian-of-$a$ term reduces to
weighted dissipation $+$ $r^{-2}H_2$ using only $|d\chi|$.  No $\|\nabla^2\chi\|_\infty$
or higher cutoff jet appears. $\square$

## 6. Type (D): algebraic reactions and normalization

The combined algebraic terms are:
\[
 (D)=aT*T*T+(\Delta_L-\Delta)T*T+\text{(metric variation)}+\text{(volume form)}+\text{(G-evolution)}.
\tag{6.1}
\]

**Zero-order normalization terms.** The conformal part $h_{\rm conf}=-2ag$
contributes, at zero order (treating $a$ as a pointwise scaling factor):
tensor reaction $-2a\operatorname{Rm}$ (from $R*h$), four inverse-metric
variations $+8a|\operatorname{Rm}|^2$ (raising by $\partial_tg^{-1}=+2ag^{-1}$),
and volume change $-an\,d\mu$.  Together these give
\[
 \partial_t\bigl(|\operatorname{Rm}|^2d\mu\bigr)_{\rm zero-order\ conf}
 =(4-n)a|\operatorname{Rm}|^2d\mu.
\]
For $n=4$, this vanishes. This is the **zero-order algebraic cancellation
at $n=4$**, not general local conformal invariance of $\int|\operatorname{Rm}|^2$.
The $\nabla^2a$ terms from the non-constant cutoff are handled separately by
Type (C), and $\int|W|^2$ (not $\int|\operatorname{Rm}|^2$) is the true
conformal invariant.

For $F_T^2=1+|T|^2=1+|\operatorname{Rm}|^2+2\langle\operatorname{Rm},G\rangle+|G|^2$:
- On $|\operatorname{Rm}|^2$: the cancellation gives zero.
- On the constant $1$: the volume change gives $-4a\,d\mu$.
- On $2\langle\operatorname{Rm},G\rangle$ and $|G|^2$: zero-order
  variations bounded by $CaF_T$.
- The G-evolution (2.8) contracted with $2T$:
  $|2\langle T,\partial_tG\rangle|\le Ca|T||E|\le CaF_T^2$.

All of these are absorbed into the cubic potential:
\[
 \int\eta^2|(\text{Type D})|\le C_1\int\eta^2aF_T^3\,d\mu+C_0,
\tag{6.2}
\]
Every localized constant contribution carries the active factor $a$ and, since
$0\le a\le1$ and $F_T\ge1$, is bounded by $H_2$ (or by the cubic potential).
Thus (6.2) may be sharpened by replacing $C_0$ with $C(1+r^{-2})H_2$; no source
proportional to the total volume of $M$ is needed.

## 7. Collection: the H₂ inequality

Choosing $\varepsilon=\varepsilon'=\varepsilon''=\delta_0/4$ with $\delta_0<2$:
\[
\boxed{
 \frac d{dt}H_2+(2-\delta_0)D_2
 \le C_1\int\eta^2aF_T^3\,d\mu+C_2(1+r^{-2})H_2.}
\tag{7.1}
\]

**Term-by-term comparison with A01 eq.\ (2.19):**

| Component | A01 ($F^2=1+|\operatorname{Rm}|^2$) | This note ($F_T^2=1+|T|^2$) | Difference |
|--|--|--|--|
| Bochner pair | $-(2-\delta_0)D_2+Cr^{-2}H_2$ | Identical (direct $T$-Bochner) | None |
| Type (B) | $\varepsilon'D_2+Cr^{-2}H_2$ | Identical | $|\nabla T|=|\nabla\operatorname{Rm}|$ |
| Type (C) | $\varepsilon''D_2+Cr^{-2}H_2$ | Identical | No higher cutoff jet |
| Zero-order norm. | Cancellation at $n=4$ | Same; localized constants $\le CH_2$ and $G$-terms $\le CY$ | Relative |
| G-evolution | N/A | $\le CaF_T^2$ | Into $C_1\int aF_T^3$ |
| Dissipation | $\int\eta^2a|\nabla\operatorname{Rm}|^2$ | $=\int\eta^2a|\nabla T|^2$ | Equal |

**Conclusion:** The H₂ inequality (7.1) has the same structure as A01's with
constants depending only on $n$, the cutoff ratios, and $\delta_0$.
No higher cutoff jet $\|\nabla^2\chi\|$ appears. The shifted variable $T$ adds
only bounded algebraic terms that do not change the principal analysis.

## 8. Sobolev absorption and first-exit closure

This section is superseded by Step 58. The critical $H_2$ absorption uses
$w_2=\chi F_T=a^{1/2}F_T$, whereas the separate $q=3$ evolution uses
$z_3=aF_T^{3/2}$. The following old definition loses one factor of $a^{1/2}$
and must not be used for the $q=3$ equation:
\[
 Y=\int\eta^2u^2\le\|\eta u\|_4^2\cdot\operatorname{Vol}^{1/2}
 (\text{not the correct absorption—see below}).
\]

The correct absorption of the quartic potential $I_4=\int\eta^2a^2F_T^4$
in the $Y$ evolution follows A01 eq.\ (5.2):
\[
 I_4=\int F_T\cdot u^2\le\|F_T\|_{L^2(\operatorname{supp}\chi)}\|\eta u\|_4^2
 \le K_2^{1/2}\cdot\mathcal S(D_3+Cr^{-2}Y),
\tag{8.1}
\]
where $D_3=\int\eta^2a^2F_T|\nabla\operatorname{Rm}|^2$, $K_2=\int_{\operatorname{supp}\chi}F_T^2\le H_2$,
and $\mathcal S$ is the local Sobolev constant.  The product
\[
 \gamma=\mathcal S K_2^{1/2}\le C_nr^2(1+\kappa_0)
\tag{8.2}
\]
is collapse-independent, where $\kappa_0^2\operatorname{Vol}(B_r)\ge\int_{B_r}|\operatorname{Rm}|^2$
and the Sobolev constant uses $\mathcal S\asymp r^2/\operatorname{Vol}(B_r)^{1/2}$
(Maheux–Saloff-Coste under $\operatorname{Ric}\ge-(n-1)r^{-2}$).

The preceding route is invalid because $Y(0)$ is not controlled by the critical
energy. Step 58 instead proves
\[
 Y\le C\mathcal S H_2^{1/2}(D_2+r^{-2}H_2),
\]
absorbs it directly in the $H_2$ equation, and obtains relative $H_2$ control
and a spacetime $Y$ bound before choosing a good positive-time slice.

### Defect energy $Q_\alpha$

The local defect $Q_\alpha=\int\eta^2|E|^2$ satisfies the same homogeneous inequality
as A01 eq.\ (3.4):
\[
 Q_\alpha'+cX_\alpha\le\frac{C}{r^2}Q_\alpha+C\int\eta^2aF|E|^2,
\tag{8.4}
\]
where $X_\alpha=\int\eta^2a|\nabla E|^2$, and the curvature potential is absorbed
by $Q$ through the Sobolev variable $w=\chi E$ (A01 eq.\ (3.5)):
\[
 \int aF|E|^2\le\gamma(X_\alpha+Cr^{-2}Q_\alpha),
\tag{8.5}
\]
giving $Q_\alpha'\le Cr^{-2}Q_\alpha$ when $\gamma$ is small.  Every term is
homogeneous in $E$: if $E=0$, the RHS vanishes.

### $J_6$ persistence

The Step 35 identity carries verbatim: $s=|E|^2$ is smooth, the test function
$3\eta^2a^4s^2$ is smooth, and the Kato-free mechanism gives
$J_6'\le C(1+r^{-2})J_6$ when $\gamma$ is small (Step 35, eq.\ 0.1).
No change from the shifted $T$ variable, since $J_6$ involves only $E$.

## 9. The W^{1,p}→L^∞ continuation bridge

This is the new result from the Strategist's observation, using the Step 56
base pair.

### 9.1 Statement

**Proposition 9.1** (Finite-order continuation).
*Suppose the exact flow $\partial_tg=-2a(E)$ exists smoothly on $[0,T^*)$
and the first-exit curvature estimate*
\[
 \|aF_T(t)\|_\infty\le\frac{C\gamma}{t}
\tag{9.1}
\]
*holds on $(0,T^*)$. If $T^*<\infty$, then for any $\tau\in(0,T^*)$:*

*(i) $|T(t)|\le C_{p,\tau}$ pointwise for $t\in[\tau,T^*]$, hence
$|\operatorname{Rm}(t)|\le C_{p,\tau}$.*

*(ii) Smooth extension past $T^*$ additionally requires enough coupled
$(U_m,C_{m+1})$ and unweighted $T_m$ levels to recover the finite
$H^{s_0}$ restart norm in a fixed background. The pointwise curvature bound
alone does not supply these cutoff-jet estimates.*

### 9.2 Proof

**Step 1: Bilipschitz equivalence.** On $[\tau,T^*]$:
\[
 |\partial_tg|=2a|E|\le2|U|\le2\|U\|_\infty.
\tag{9.2}
\]
From (9.1), $\|U\|_\infty\le C\gamma/\tau<\infty$, so
$e^{-C(T^*-\tau)/\tau}g(\tau)\le g(t)\le e^{C(T^*-\tau)/\tau}g(\tau)$.

**Step 2: Unweighted $T_0$ seed (Step 56, eq.\ 1.1).**
\[
 \frac d{dt}\|T\|_q^q+c\int a|\nabla T|^2|T|^{q-2}\le C_{K}\|T\|_q^q+C\operatorname{Vol},
\tag{9.3}
\]
where $K=\|U\|_\infty\le C\gamma/\tau$.  Grönwall on $[\tau,T^*]$:
\[
 \|T(t)\|_q\le e^{C_K(T^*-\tau)/q}\bigl(\|T(\tau)\|_q+C\operatorname{Vol}^{1/q}\bigr)<\infty.
\tag{9.4}
\]

**Step 3: Coupled pair $(V,Z)$ (Step 56, eq.\ 3.8).**
\[
 \frac d{dt}\bigl(\|V\|_p^p+\|Z\|_p^p\bigr)+cD^U_{1,p}
 \le C_{K}\bigl(1+\|T\|_p^p+\|V\|_p^p+\|Z\|_p^p\bigr).
\tag{9.5}
\]
By (9.4), $\|T\|_p$ is bounded on $[\tau,T^*]$.  Grönwall gives
$(V,Z)\in L^\infty([\tau,T^*];L^p)$ for every $p$.

**Step 4: $X=\nabla T$ (Step 56, eq.\ 4.5).**
\[
 \frac d{dt}\|X\|_p^p+cD^T_{1,p}
 \le C_K\bigl(1+\|X\|_p^p+\|T\|_{2p}^{2p}+\|V\|_{2p}^{2p}+\|Z\|_{2p}^{2p}\bigr).
\tag{9.6}
\]
All RHS norms are bounded by Steps 2–3.  Hence $\nabla T\in L^\infty([\tau,T^*];L^p)$
for every $p$.

**Step 5: Kato + Sobolev embedding.**
By Kato's inequality, $|d|T||\le|\nabla T|$ a.e.  So $|T|\in W^{1,p}(M,g(t))$
for every $p$. For $p>n=4$, the Sobolev embedding on the closed manifold
$(M,g(t))$ (with a bilipschitz-equivalent Sobolev constant) gives
\[
 \|T(t)\|_\infty\le C_S\bigl(\|T(t)\|_p+\|\nabla T(t)\|_p\bigr)<\infty
\tag{9.7}
\]
for $t\in[\tau,T^*]$.  The constant $C_S$ depends on $(M,g(\tau),K,p)$ (per-datum),
not on the collapsing sequence.  $\square$

**Step 6: remaining finite-regularity continuation problem.** Pointwise
$|T|<\infty$ gives $|\operatorname{Rm}|<\infty$ on $[\tau,T^*]$, but the
following older shortcut is not a proof of extension across the degenerate
collar. Already the next pair contains $\chi\nabla^4\chi*U$ and the evolution
of $\nabla^3\chi$ contains $\nabla^2U$. These exchanges must be estimated through
a finite staggered hierarchy and converted to fixed-background $H^{s_0}$ data;
ordinary Shi estimates apply only on the plateau.

(a) **Higher derivatives with bounded coefficients.** Once $|\operatorname{Rm}|$
is bounded, the evolution equations for $\nabla^mU$ and $\nabla^{m+1}\chi$ have
coefficients bounded by $C(K,\|\nabla^j\chi\|)$ for $j\le m$.  Each level of the
staggered hierarchy $T_m\to(U_{m+1},C_{m+2})\to T_{m+1}$ closes by standard
Grönwall with bounded data—no absorption, interpolation, or structural argument
is needed beyond the first level.  On the plateau $\{a=1\}$, this is the standard
Shi estimate: $|\nabla^k\operatorname{Rm}|\le C_k/t^{k/2}$.

(b) **Connection velocity.** $\partial_t\Gamma=g^{-1}*\nabla\operatorname{Ric}(U)$.
Since $|V|=|\nabla U|\in L^p$ for all $p$:
\[
 \|\Gamma(T^*)-\Gamma(\tau)\|_{L^p}\le\int_\tau^{T^*}\|V(s)\|_p\,ds<\infty.
\tag{9.8}
\]

(c) **Uniform $H^s$ bound on $[\tau,T^*]$.** With $|\operatorname{Rm}|\le C$,
the staggered hierarchy has bounded coefficients at every level.  By induction
on $m$, each $\|\nabla^mT\|_q$ satisfies a Grönwall inequality with coefficient
$C(m,K,C_\chi,q)$ and forcing from lower levels.  Therefore
$g(t)\in H^s$ uniformly on $[\tau,T^*]$ for every $s$.  The sequence of
approximating metrics converges in $C^\infty$, giving smooth limit data $g(T^*)$.

(d) **Restart.** The Step 56 local theorem applied to $g(T^*)$ restarts the flow for
a positive time, contradicting maximality of $T^*$. $\square$

**Corrected remark.** The first block plus Sobolev embedding yields unweighted
$|T|_\infty$; it does not replace the cutoff-jet hierarchy. Only finitely many
levels should be needed to reach the Step 56 threshold $s_0>n/2+4$, after which
tame higher-order estimates propagate, but those finite levels must still be
proved. No per-datum Sobolev constant may enter the sequence-uniform first-exit
chain.

## 10. Complete chain: start → first exit → common observation time

The full argument for each datum $i$ in the Ishida–LeBrun sequence:

1. **Start.** Step 56 Theorem 4.3 gives a smooth flow on $[0,T_i]$, $T_i>0$
   depending on $g_i$ and $\chi$.

2. **Maximal extension.** Restart at every smooth endpoint to form a maximal
   smooth branch $[0,T_i^*)$.

3. **First-exit estimates on $(0,\min\{T_i^*,\theta r^2\})$.** Run:
   - the Step 58 relative $H_2\to\int Y\to Y(t)$ bridge, using $H_2(0)$ but no $Y(0)$;
   - $Y$ propagation (A01 §5 structure);
   - $Q_\alpha$ Grönwall (§8.4);
   - $J_6$ persistence (Step 35);
   - Weighted Moser: $\|aF_T(t)\|_\infty\le C\gamma/t$;
   - Integrable defect: $\|aE(t)\|_\infty\le C\delta(r^2/t)^{1/3}$;
   - Metric drift $< c$ for $t\le\theta r^2$.

   All constants use only: $n$, $\gamma=\mathcal S K_2^{1/2}$, $r$,
   $\|d\chi\|_\infty\le Cr^{-1}$, $\delta_i=\|E_i\|_\infty$, and
   $\operatorname{Vol}(M,g_i)$.  None uses high Sobolev norms of $g_i$
   or higher cutoff jets.

4. **Unfinished continuation if $T_i^*<\theta r^2$.** On the terminal slab
   $[T_i^*/2,T_i^*)$, the curvature endpoint gives $\|U\|_\infty<\infty$ and
   Proposition 9.1 gives $|T|_\infty<\infty$. To contradict maximality one must
   still close enough coupled cutoff/curvature levels to obtain fixed-background
   $H^{s_0}$ restart data. Until that finite hierarchy is supplied, a common
   observation time has not been proved.

5. **Current conclusion.** The curvature first-exit branch is available on every
   existing smooth interval; extension of every datum to $\theta r^2$ remains open.

## 11. $Q_{\rm global}$ identity

With disjoint outer supports $B_{7r}(x_\alpha)$ and $\rho=\sum_\alpha\eta_\alpha^2$:
\[
 Q_{\rm rest}(t)=\int(1-\rho)|E(t)|^2\,d\mu_t=Q_{\rm rest}(0)
\tag{11.1}
\]
because $a=0$ on $\operatorname{supp}(1-\rho)$.  Therefore
\[
 Q_{\rm global}(t)=Q_{\rm rest}(0)+\sum_\alpha Q_\alpha(t)
 \le e^{Ct/r^2}Q_{\rm global}(0).
\tag{11.2}
\]
This is the corrected identity from Step 56 §6.2.

## 12. Scope and status

**Established conditionally (modulo smooth flow existence from Step 56 and
term-by-term PDE tensor verification):**

1. The unweighted $H_2$ inequality (7.1) on the exact flow, with identical
   structure to A01's and no higher cutoff jet.
2. The Sobolev absorption via the collapse-independent $\gamma$.
3. The finite-order continuation bridge replacing the infinite staggered hierarchy.
4. The logical chain from per-datum start to sequence-uniform common time.
5. The global $Q$ identity with stationary remainder.

**Not established by this note:**

- Full term-by-term PDE tensor verification of the first-exit weighted Moser
  endpoint.  The endpoint $\|aF(t)\|_\infty\le C\gamma/t$ is inherited from the
  established H₂–Y–Moser chain; this note supplies the H₂ input and the
  continuation bridge but does not independently re-derive the Moser iteration.
- The terminal spectral density mechanism (Steps 43, 47).
- Positive branch, arbitrary topology, $n\ge5$, dimension-only constants, Lean.
- Complete Yau Problem 26 resolution.

## 13. Sources

- A01 step25: `Sessions/S0910A01/workspace/notes/step25_tensor_energy_derivation.md`
- Step 56 tame construction: `workspace/notes/step56_tame_direct_flow_repair.md`
- Step 56 base pair: `workspace/notes/step56_positive_time_base_pair.md`
- Step 35 J₆ persistence: `workspace/notes/step35_unregularized_J6_persistence_lemma.md`
- Step 47 terminal density: `workspace/notes/step47_consolidated_negative_IL_gap_theorem.md`

# Step 26: General-$p$ tensor inequality, initial Sobolev resolution, and first-exit closure

## 0. Purpose and scope

This note resolves two of the three remaining analytic obstacles identified by
the Step 25 TTCS verification for the 4D negative-branch conditional gap theorem.
The obstacles were:

1. The general-$p$ weighted tensor inequality (Step 25, eq. 4.2) lacks a
   complete proof: only $q=2,3$ and the quadratic defect have index-level
   derivations.
2. The initial relative Sobolev inequality on collapsed selected balls has no
   source-level justification.
3. The normalized Yang–Wang smooth continuation/extension remains unwritten.

This step proves (1) and resolves (2). Obstacle (3) remains the single open
analytic task.

## 1. Initial Sobolev inequality on collapsed balls

### 1.1 The geometric input

Each selected good support is contained in a geodesic ball $B_r(x)$ of fixed
radius $r = r_*(n, K_0, \varepsilon)$ (the Li radius), on a closed
four-manifold $(M,g)$ with

$$
\operatorname{Ric}_g \ge -(1+\delta)g.
$$

The ball may have arbitrarily small volume (collapsed).  The question is
whether the relative Sobolev inequality

$$
\|u\|_4^2
\le \mathsf S\bigl(\|\nabla u\|_2^2 + r^{-2}\|u\|_2^2\bigr),
\qquad u \in C_c^\infty(B_r(x)),
\tag{1.1}
$$

holds with $\mathsf S = Cr^2\operatorname{Vol}(B_r)^{-1/2}$ where $C$ depends
only on the dimension and $Kr^2$.

### 1.2 The Maheux–Saloff-Coste theorem

**Theorem** (Maheux–Saloff-Coste, Math. Ann. 303, 1995, Theorem 1.1).
Let $(M^n,g)$ be a complete Riemannian manifold with $\operatorname{Ric} \ge kg$
for some $k \in \mathbb{R}$.  Let $1 \le p < n$ and
$p^* = np/(n-p)$.  Then there exist constants $A(p), C(p) > 0$ such that for
every $r > 0$, every $x \in M$, and every
$\phi \in C^\infty(B(x,r))$,

$$
\left(\frac{1}{V}\int_{B(x,r)}|\phi - \phi_B|^{p^*}\right)^{1/p^*}
\le A e^{C(1+\sqrt{|k|}r)}\,r
\left(\frac{1}{V}\int_{B(x,r)}|\nabla\phi|^p\right)^{1/p},
$$

where $V = \operatorname{Vol}(B(x,r))$ and $\phi_B = V^{-1}\int\phi$.

The proof uses two ingredients requiring only $\operatorname{Ric} \ge kg$:

- **Bishop–Gromov doubling:** $V(B_{2r})/V(B_r) \le D(n, Kr^2)$;
- **Buser's Poincaré inequality:** under Ric $\ge$ kg,
  $\int_{B_r}|f - f_B|^p \le C(n,K,r)\,r^p\int_{B_r}|\nabla f|^p$.

Together, doubling + Poincaré implies Sobolev by the Hajłasz–Koskela
framework (Mem. AMS 145, 2000).

### 1.3 Application to compactly supported functions in dimension four

For $u \in C_c^\infty(B_r(x))$, the mean $u_B$ satisfies
$|u_B| \le V^{-1/p}\|u\|_p$.  A triangle inequality then gives

$$
\|u\|_{p^*} \le C' e^{C(1+\sqrt{|k|}r)}\,r\,V^{1/p^*-1/p}\|\nabla u\|_p
+ C''V^{1/p^*-1/p}\|u\|_p.
$$

With $p = 2$ and $n = 4$: $p^* = 4$, $1/p^* - 1/p = -1/4$.  Squaring:

$$
\|u\|_4^2 \le C(4,Kr^2)\,r^2\,V^{-1/2}
\bigl(\|\nabla u\|_2^2 + r^{-2}\|u\|_2^2\bigr).
\tag{1.2}
$$

Therefore

$$
\boxed{\mathsf S = C(n,Kr^2)\,r^2\,\operatorname{Vol}(B_r)^{-1/2}}
\tag{1.3}
$$

**depends only on the dimension and the product $Kr^2$, not on the volume.**

For the pinching sequence: $K = 1+\delta \le 2$ and $r = r_*$ is uniformly
bounded, so $Kr^2$ is uniformly bounded.  Therefore $C(n,Kr^2)$ is uniform
across the sequence, and $\mathsf S$ has the explicit volume scaling (1.3).

### 1.4 Transfer to the buffered support

The fixed auxiliary cutoff $\eta$ has $\operatorname{supp}\eta \subset B_r(x)$.
Any function $u$ with $\operatorname{supp}u \subset \operatorname{supp}\eta$ is
compactly supported in $B_r$, and (1.2) applies.  Under $C^0$ metric
comparability $e^{-2I}g_0 \le g(t) \le e^{2I}g_0$ with $I$ small, the same
inequality holds for $g(t)$ with modified constant $\mathsf S(t) \le 2\mathsf S(0)$.

**Conclusion.** The initial Sobolev inequality is available without any
noncollapse hypothesis, resolving obstacle (2).

## 2. Corrected $\bar\beta$ definition and collar handling

### 2.1 The collar problem

The auxiliary domain $\operatorname{supp}\eta$ includes a stationary collar
$\{a = 0\}$ where the flow velocity vanishes.  The curvature energy

$$
H_2 = \int\eta^2 F^2\,d\mu
$$

includes this collar's time-independent contribution

$$
C_{\rm col} = \int_{\operatorname{supp}\eta \setminus \operatorname{supp}\chi}
\eta^2 F_0^2\,d\mu_0.
$$

### 2.2 Definition

Define

$$
\bar\beta(t) = \mathsf S(t) \cdot \bigl(H_2(t) - C_{\rm col}\bigr)^{1/2}
= \mathsf S(t) \cdot \left(\int_{\operatorname{supp}\chi} F(t)^2\,d\mu_t\right)^{1/2}.
\tag{2.1}
$$

This equals $\mathsf S \cdot \|F\|_{L^2(\operatorname{supp}\chi)}$ and
coincides with the Step 25 definition of $\beta$.  The key identity is

$$
\widehat H_2(t) := H_2(t) - C_{\rm col}
= \int_{\operatorname{supp}\chi} F(t)^2\,d\mu_t,
\tag{2.2}
$$

and the energy inequality (Step 25, eq. 2.5) becomes, after subtracting the
time-constant collar:

$$
\widehat H_2' + cD_2
\le C\int\eta^2 aF^3 + Cr^{-2}\widehat H_2 + Cr^{-2}C_{\rm col}.
\tag{2.3}
$$

**Corrected active-region inequality.**  Since all cutoff remainder terms
contain $a$, $da$, or $|da|^2/a$, their support lies in $\{a > 0\}$.  The
energy inequality for the active region alone is

$$
\widehat H_2' + cD_2
\le C\int\eta^2 aF^3 + Cr^{-2}\widehat H_2.
\tag{2.3}
$$

This has no additive collar constant.  The collar contributes only to the
time-independent part of $H_2$.

### 2.3 Critical absorption with $\bar\beta$

Since $\eta = 1$ on $\operatorname{supp}\chi$:

$$
\int\eta^2 aF^3
= \int F(\chi F)^2
\le \|F\|_{L^2(\operatorname{supp}\chi)}\,\|\chi F\|_4^2
\le \bar\beta(D_2 + r^{-2}\widehat H_2).
\tag{2.4}
$$

(Note: $\bar\beta = \mathsf S \widehat H_2^{1/2}$ and
$\|\chi F\|_4^2 \le \mathsf S(D_2 + r^{-2}\widehat H_2)$, so the product
is $\bar\beta(D_2 + r^{-2}\widehat H_2)$ with no extra $\mathsf S^{-1}$.)

If $\bar\beta(t) \le \bar\beta_* \ll 1$, this absorbs into the left side,
yielding

$$
\widehat H_2(t) \le e^{Ct/r^2}(\widehat H_2(0) + C_{\rm col})
\le e^{Ct/r^2}H_2(0).
\tag{2.5}
$$

Thus $\bar\beta(t) \le C\bar\beta(0)\,e^{Ct/r^2}$, which is propagated.

## 3. Complete general-$p$ weighted tensor inequality

### 3.1 Statement

**Lemma.** Under the buffered support assumptions (Step 25, eq. 1.1), metric
comparability $\Lambda^{-1}g_0 \le g(t) \le \Lambda g_0$, and the relative
Sobolev inequality (1.1), the following holds for any $p \ge 3$ and
$\Phi = F$ (curvature) or $\Phi = (|E|^2 + \varepsilon^2)^{1/2}$ (regularized
defect).  Define

$$
K_p = \int\eta^2 a^{p-2}\Phi^p\,d\mu,
\qquad
Z_p = \eta a^{(p-1)/2}\Phi^{p/2}.
$$

Then

$$
\frac{d}{dt}K_p + c\|\nabla Z_p\|_2^2
\le Cp^2 r^{-2}K_p + Cp\int\eta^2 a^{p-1}F\Phi^p\,d\mu,
\tag{3.1}
$$

where $c > 0$ is uniform and $C$ depends on $n, \Lambda$.

### 3.2 Proof for $\Phi = F$ (curvature)

**Step A: Time derivative of $K_p$.**  Since $a = \chi^2$ is time-independent:

$$
\frac{d}{dt}\int\eta^2 a^{p-2}F^p\,d\mu
= \int\eta^2 a^{p-2}\frac{d}{dt}(F^p)\,d\mu
+ \int\eta^2 a^{p-2}F^p\frac{d(d\mu)}{d\mu}\,d\mu.
$$

The measure variation is $\partial_t d\mu = -a\tau\,d\mu$ where
$\tau = \operatorname{tr}E$.  Since $|\tau| \le CF$, this contributes

$$
\left|\int\eta^2 a^{p-2}F^p \cdot(-a\tau)\,d\mu\right|
\le C\int\eta^2 a^{p-1}F^{p+1}\,d\mu.
\tag{3.2}
$$

For $d(F^p)/dt$: since $F^2 = 1 + |\operatorname{Rm}|^2$,

$$
\frac{d}{dt}F^p = \frac p2 F^{p-2}\frac{d}{dt}|\operatorname{Rm}|^2.
$$

Now $\partial_t|\operatorname{Rm}|^2 = 2\langle\operatorname{Rm},
\partial_t\operatorname{Rm}\rangle + (\text{inverse-metric variation})$.
The inverse-metric variation is bounded by $Ca|E||\operatorname{Rm}|^2 \le CaF^3$.
Thus

$$
\frac{d}{dt}F^p \le \frac p2 F^{p-2}
\bigl[2\langle\operatorname{Rm}, \partial_t\operatorname{Rm}\rangle
+ CaF^3\bigr].
\tag{3.3}
$$

**Step B: Laplacian contribution.**  Using the tensor evolution
$\partial_t\operatorname{Rm} = a\Delta\operatorname{Rm} + a\mathcal{A} +
(da)*\nabla E + (\nabla^2 a)*E$, the Laplacian part gives:

$$
p\int\eta^2 a^{p-2}F^{p-2}\langle\operatorname{Rm}, a\Delta\operatorname{Rm}\rangle\,d\mu.
$$

Setting $w = \eta^2 a^{p-2}$ and applying A01's identity (3.3):

$$
p\int wa\,F^{p-2}\langle R, \Delta R\rangle
= -p\int wa\,F^{p-2}|\nabla R|^2
- p(p-2)\int wa\,F^{p-2}|\nabla F|^2
- p\int\langle d(wa), F^{p-2}\langle R, \nabla R\rangle\rangle.
\tag{3.4}
$$

The first two terms provide the dissipation $\ge c\|\nabla Z_p\|_2^2$ because
(see Step C for the gradient of $Z_p$):

$$
|\nabla Z_p|^2
\le C_p\bigl(a^{p-1}F^{p-2}|\nabla\operatorname{Rm}|^2
+ a^{p-2}|d\chi|^2 F^p + |d\eta|^2 a^{p-1}F^p\bigr).
\tag{3.5}
$$

(The weight-derivative contribution $a^{p-3}|da|^2F^p = 4a^{p-2}|d\chi|^2F^p$
is already controlled by $Cr^{-2}K_p$, and the gradient term coefficient
$a^{p-1}F^{p-2}$ matches the dissipation $D_p$.)

The gradient dissipation from (3.4) controls the principal part of
$\|\nabla Z_p\|_2^2$ after absorbing cutoff-derivative remainders.

**Step C: Boundary term from $d(wa)$.**

$$
d(wa) = d(\eta^2 a^{p-1})
= 2\eta\,d\eta \cdot a^{p-1} + (p-1)\eta^2 a^{p-2}\,da.
$$

The $d\eta$ part: On $\operatorname{supp}d\eta$, $a = 0$.  For $p \ge 3$,
$a^{p-1} = 0$ there.  **This term vanishes.**

The $da$ part contributes:

$$
p(p-1)\int\eta^2 a^{p-2}\langle da, F^{p-2}\langle R, \nabla R\rangle\rangle\,d\mu
= p(p-1)\int\eta^2 a^{p-2}\langle da, F^{p-1}\nabla F\rangle\,d\mu.
$$

By Young's inequality with parameter $\varepsilon$:

$$
\le \varepsilon\int\eta^2 a^{p-1}F^{p-2}|\nabla\operatorname{Rm}|^2
+ C_\varepsilon p^2\int\eta^2 a^{p-3}|da|^2 F^p.
$$

Since $a^{p-3}|da|^2 = a^{p-3}\cdot 4a|d\chi|^2 = 4a^{p-2}|d\chi|^2$,
the second term is $\le Cp^2 r^{-2}K_p$.

**Step D: Hessian-$a$ terms.**  The term $\int w F^{p-2}\operatorname{Rm}*(\nabla^2 a)*E$
is integrated by parts once (A01, eq. 3.4):

$$
\int\eta^2 a^{p-2}F^{p-2}\operatorname{Rm}*(\nabla^2 a)*E
= -\int da * \nabla(\eta^2 a^{p-2}F^{p-2}\operatorname{Rm}*E).
$$

The derivative inside hits four factors.  When it hits $\eta$: on
$\operatorname{supp}d\eta$, $da = 0$, so zero.  When it hits $a^{p-2}$: gives
$(p-2)a^{p-3}da$, combined with the outer $da$ gives
$a^{p-3}|da|^2 = 4a^{p-2}|d\chi|^2$.  When it hits $F^{p-2}$ or
$\operatorname{Rm}*E$: contributes $|da|F^{p-1}|\nabla\operatorname{Rm}|$.
Young's inequality then gives:

$$
\le \varepsilon D_p + Cp^2 r^{-2}K_p.
$$

The $(da)*\nabla E$ term is handled identically (A01, eq. 3.5).

**Step E: Algebraic reaction.**  All curvature, metric-variation, and
measure terms are bounded by $CaF^3$ per unit testing density (A01, eq. 3.2).
Integrating against $\eta^2 a^{p-2}F^{p-2}$ gives:

$$
Cp\int\eta^2 a^{p-1}F^{p+1}\,d\mu.
\tag{3.6}
$$

**Step F: Assembly.**  Combining Steps B–E:

$$
K_p' + c D_p \le Cp^2 r^{-2}K_p + Cp\int\eta^2 a^{p-1}F^{p+1}\,d\mu,
\tag{3.7}
$$

where $D_p = \int\eta^2 a^{p-1}F^{p-2}|\nabla\operatorname{Rm}|^2$.

To convert this into the form (3.1), note that $D_p$ controls the principal
part of $\|\nabla Z_p\|_2^2$: with $Z_p = \eta a^{(p-1)/2}F^{p/2}$,

$$
|\nabla Z_p|^2 \le C_p(a^{p-1}F^{p-2}|\nabla\operatorname{Rm}|^2
+ a^{p-2}|d\chi|^2 F^p + |d\eta|^2 a^{p-1}F^p).
$$

The last term vanishes by support properties.  Therefore

$$
\|\nabla Z_p\|_2^2 \le C_p(D_p + r^{-2}K_p),
$$

and (3.7) implies (3.1) after adjusting constants.  $\square$

### 3.3 Proof for $\Phi = (|E|^2+\varepsilon^2)^{1/2}$ (regularized defect)

The defect equation (A01, eq. 6.4) gives

$$
(\partial_t - a\Delta)|E|^2
= -2a|\nabla E|^2 + 4a\operatorname{Rm}(E,E)
+ 2\langle E, \mathcal{C}_a(E)\rangle.
\tag{3.8}
$$

For $\Phi_\varepsilon = (|E|^2+\varepsilon^2)^{1/2}$:

$$
\partial_t\Phi_\varepsilon = \frac{1}{2\Phi_\varepsilon}\partial_t|E|^2,
$$

The exact chain rule is
$$
(\partial_t - a\Delta)\Phi_\varepsilon^p
= \frac{p}{2}\Phi_\varepsilon^{p-2}(\partial_t - a\Delta)|E|^2
- p(p-2)a\Phi_\varepsilon^{p-2}|\nabla\Phi_\varepsilon|^2.
$$

The last term is a favorable gradient correction.  Testing the defect equation
(3.8) against $q = \frac{p}{2}\eta^2 a^{p-2}\Phi_\varepsilon^{p-2}$ and
expanding the $\mathcal{C}_a(E)$ Hessian terms via A01 identity (6.5), with
$dq$ having the same structure as in the curvature case:

- The $da$ part gives $Cp^2 r^{-2}K_p[\Phi_\varepsilon]$ (using
  $a^{p-3}|da|^2 = 4a^{p-2}|d\chi|^2$);
- The $\nabla\Phi_\varepsilon$ cross terms are absorbed by the
  $p(p-2)$ scalar dissipation;
- The curvature reaction $4a\operatorname{Rm}(E,E)$ contributes
  $CaF|E|^p \le CaF\Phi_\varepsilon^p$.

All estimates are uniform in $\varepsilon$ because $\Phi_\varepsilon \le F + \varepsilon$
and $|\nabla\Phi_\varepsilon| \le |\nabla E|$.

**The key structural property** is that the defect equation has no curvature-only
source: all terms contain $E$, $\nabla E$, or traces.  Therefore the reaction
is bounded by $CaF\Phi^p$, not $CaF^2\Phi^{p-1}$.

Sending $\varepsilon \to 0$: zero-order terms by dominated convergence;
gradient dissipation by weak lower semicontinuity.  This yields (3.1) for
$\Phi = |E|$.  $\square$

### 3.4 Remark on noninteger powers

For integer $p$, $a^{p-2} = \chi^{2(p-2)}$ is smooth.  For noninteger $p$
arising in the Moser iteration ($p_j = 3 \cdot (3/2)^j$), the weight
$\chi^{2(p-2)}$ is not automatically smooth at zeros of $\chi$, since
$\chi^\alpha$ for non-even-integer $\alpha$ may lack smoothness at
$\chi = 0$.

The standard remedy is to choose $\chi$ infinitely flat at the boundary of
its support (which is compatible with the maximal-function selection), or to
work at the $W^{1,\infty}$ level: $a^{p-2}$ is Lipschitz for $p \ge 3$, and
the energy estimates use only first derivatives of the weight.  The
conclusion at each Moser step is derived for smooth approximants
$a_\varepsilon^{p-2}$ with $a_\varepsilon = (\chi^2 + \varepsilon)$, then
passed to the limit by dominated convergence.

In either case, the critical quotient $|da|^2/a = 4|d\chi|^2$ has a bounded
extension to $\{\chi = 0\}$.

## 4. Explicit $J_6$ propagation

Define $J_6 = \int\eta^2 a^4|E|^6\,d\mu$.  This is $K_6[|E|]$.  By
equation (3.1) with $p = 6$ and $\Phi = |E|$:

$$
J_6' + c\|\nabla Z_6\|_2^2
\le Cr^{-2}J_6 + C\int\eta^2 a^5 F|E|^6\,d\mu.
\tag{4.1}
$$

The reaction term satisfies:

$$
\int\eta^2 a^5 F|E|^6
= \int F\,|\eta a^{5/2}|E|^3|^2
\le \|F\|_{L^2(\operatorname{supp}\chi)}\,\|\eta a^{5/2}|E|^3\|_4^2.
$$

Since $Z_6 = \eta a^{5/2}|E|^3$, the Sobolev inequality gives

$$
\|Z_6\|_4^2 \le \mathsf S(\|\nabla Z_6\|_2^2 + r^{-2}\|Z_6\|_2^2).
$$

Now $\|Z_6\|_2^2 = \int\eta^2 a^5|E|^6 \le J_6$ (since $a \le 1$).  Hence:

$$
\int\eta^2 a^5 F|E|^6
\le \bar\beta(\|\nabla Z_6\|_2^2 + r^{-2}J_6).
$$

(Using $\|F\|_{L^2(\operatorname{supp}\chi)} = \bar\beta/\mathsf S$ and
$\|Z_6\|_4^2 \le \mathsf S(\|\nabla Z_6\|_2^2 + r^{-2}J_6)$.)


For small $\bar\beta$, this absorbs the gradient and gives

$$
\boxed{J_6(t) \le e^{Ct/r^2}J_6(0) \le Ce^{C\theta}\delta^6 V.}
\tag{4.2}
$$

This is a genuine $p = 6$ critical absorption, not merely "homogeneity."

## 5. Subcritical Moser iteration: complete proof

### 5.1 The absorption chain

From equation (3.1), on a positive-time slab $[t/2, t]$ with
$\mathsf S^2 H_3(s) \le C\bar\beta_*^3/s$ (established by Step 25, eq. 3.2),
the Young absorption (Step 25, eq. 4.6) gives:

$$
K_p' + \frac c2\|\nabla Z_p\|_2^2
\le Cp^3\left(r^{-2} + \frac{\bar\beta_*^3}{t}\right)K_p.
\tag{5.1}
$$

### 5.2 Parabolic iteration

Choose nested time slabs $[\tau_j, t]$ with $\tau_0 = t/2$,
$\tau_j = t(1 - 2^{-(j+1)})$, and set $p_{j+1} = (3/2)p_j$.

**Time-cutoff energy estimate.** A standard time cutoff $\zeta_j$ equal to
$1$ on $[\tau_{j+1}, t]$ and supported on $[\tau_j, t]$, with
$|\zeta_j'| \le C4^j/t$, applied to (5.1) gives:

$$
\sup_{[\tau_{j+1},t]}K_{p_j}
+ \int_{\tau_{j+1}}^t\|\nabla Z_{p_j}\|_2^2
\le L_j\,\mathcal{M}_{p_j,j},
\tag{5.2}
$$

where $L_j = Cp_j^3 \cdot 4^j(t^{-1} + r^{-2})$ and
$\mathcal{M}_{p,j} = \int_{\tau_j}^t K_p(s)\,ds$.

**Sobolev step.** By the parabolic embedding (Sobolev in space + Hölder in
time):

$$
\mathcal{M}_{p_{j+1},j+1}
\le C\mathsf S\,(L_j\mathcal{M}_{p_j,j})^{3/2}.
\tag{5.3}
$$

This uses $K_{2p} \le \mathsf S^2(\|\nabla Z_p\|_2^2 + r^{-2}K_p)^2$ and
$K_{3p/2} \le K_p^{1/2}K_{2p}^{1/2}$, combined with the time integration.

**Normalized iteration.** Setting $m_j = \mathcal{M}_{p_j,j}^{1/p_j}$:

$$
m_{j+1} \le (C\mathsf S)^{2/(3p_j)} L_j^{1/p_j}\,m_j.
\tag{5.4}
$$

The infinite product converges:

$$
\prod_{j=0}^\infty (C\mathsf S)^{2/(3p_j)}L_j^{1/p_j}
= (C\mathsf S)^{(2/3)\sum 1/p_j}
\cdot \prod_j L_j^{1/p_j}
< \infty
\tag{5.5}
$$

because $\sum 1/p_j = 3/p_0 < \infty$ and
$\sum(\log L_j)/p_j \le C\sum(j + \log p_j)/p_j < \infty$.

### 5.3 Endpoint estimates

**Curvature ($\Phi = F$, $p_0 = 3$):**  From Step 25 eq. 3.2:
$\mathcal{M}_{3,0} = \int_{t/2}^t H_3(s)\,ds \le C\bar\beta_*^3/\mathsf S^2$.

The iteration (5.4)–(5.5) yields

$$
\boxed{\|aF(t)\|_{L^\infty(\operatorname{supp}\chi)}
\le \frac{C\bar\beta_*}{t}, \qquad 0 < t \le r^2.}
\tag{5.6}
$$

**Defect ($\Phi = |E|$, $p_0 = 6$):**  From (4.2):
$\mathcal{M}_{6,0} = \int_{t/2}^t J_6(s)\,ds \le Ct\delta^6 V$.

Using $\mathsf S = Cr^2 V^{-1/2}$:

$$
\boxed{\|aE(t)\|_{L^\infty(\operatorname{supp}\chi)}
\le C\delta\left(\frac{r^2}{t}\right)^{1/3}, \qquad 0 < t \le r^2.}
\tag{5.7}
$$

Both estimates hold on the full active support including the transition collar.

## 6. First-exit closure

### 6.1 Metric comparability from the defect bound

$$
e^{-2I(t)}g_0 \le g(t) \le e^{2I(t)}g_0,
\qquad
I(t) = \int_0^t\|aE(s)\|_\infty\,ds.
\tag{6.1}
$$

From (5.7): $I(\theta r^2) \le (3/2)C\delta\theta^{2/3}r^2$.
For $\delta \ll 1$, $I(t) \le 1/100$, say.

This simultaneously preserves:

1. **Volume ratio:** $\operatorname{Vol}_{g(t)} \ge e^{-8I}\operatorname{Vol}_{g_0}$.
2. **Sobolev constant:** $\mathsf S(t) \le e^{CI}\mathsf S(0) \le 2\mathsf S(0)$.
3. **Cutoff gradient:** $|d\chi|_{g(t)} \le e^I|d\chi|_{g_0} \le 2r^{-1}$.
4. **Support containment:** $\exp_x$ maps remain $C^0$-close.
5. **Critical product:** $\bar\beta(t) = \mathsf S(t)\widehat H_2(t)^{1/2}$
   is improved by the $H_2$ estimate.

### 6.2 First-exit argument

The first-exit conditions are:

- (F1) Metric: $e^{-1/10}g_0 \le g(t) \le e^{1/10}g_0$
- (F2) Sobolev: $\mathsf S(t) \le 2\mathsf S(0)$
- (F3a) Curvature: $\widehat H_2(t) \le 2\widehat H_2(0)$
- (F3b) Defect: $Q(t) \le 2Q(0)$
- (F4) $J_6(t) \le 2J_6(0)$

**Claim:** For $\bar\beta(0) \le \varepsilon_0$ and $\delta \le \delta_0$
(depending on $n$), and for $0 < t \le \theta r^2$ with $\theta$ small enough,
if (F1)–(F4) hold on $[0,T)$, then they hold with strict improvement on
$[0,T)$, hence cannot exit.

*Proof sketch:*
- (5.7) gives $I(t) \le C\delta\theta^{2/3}r^2 \le 1/20$, improving (F1).
- (F1) improves (F2) and the cutoff bound.
- (2.3) gives $\widehat H_2(t) \le e^{C\theta}\widehat H_2(0) < 2\widehat H_2(0)$
  for small $\theta$, improving (F3a).  No collar constant enters.
- The defect $Q$ is propagated by Step 25 eq. 3.1 (third line), also
  improving (F3b).
- (4.2) improves (F4).
- $\bar\beta(t) \le C\bar\beta(0)e^{C\theta}$, preserving the critical
  smallness.

**This closure is conditional on smooth existence of the flow to time
$\theta r^2$**, which requires the normalized Yang–Wang continuation theorem
(obstacle 3, still open).

## 7. Complete conditional chain

$$
\begin{aligned}
&\text{Ric pinching on critical Ishida–LeBrun }M\\
\longrightarrow{} &\text{Maheux–Saloff-Coste Sobolev on good ball (Section 1)}\\
\longrightarrow{} &\text{small }\bar\beta\text{ at maximal-function good support}\\
\longrightarrow{} &\text{first-exit }H_2, H_3, J_6, Q\text{ (Sections 2–4)}\\
\longrightarrow{} &\|a\operatorname{Rm}(t)\|_\infty \le C\bar\beta/t
  \text{ (Section 5)}\\
\longrightarrow{} &\|aE(t)\|_\infty \le C\delta(r^2/t)^{1/3}
  \text{ (Section 5)}\\
\longrightarrow{} &\text{metric/Sobolev/cutoff comparison (Section 6)}\\
\longrightarrow{} &\text{first-exit closure (Section 6)}\\
\longrightarrow{} &\text{plateau }a=1\text{: standard Shi estimates}\\
\longrightarrow{} &\text{smooth exponential-chart compactness}\\
\longrightarrow{} &\text{calibrated }W^+\text{ spectrum, projector contradiction (Step 6)}
\end{aligned}
$$

The single remaining analytical obligation is smooth continuation of the
degenerate normalized cutoff flow.

## 8. What the Wang continuation requires

Wang proves (Theorem 6.3 of the pseudolocality paper) that bounded
$|\chi^2\operatorname{Rm}|$ extends the unnormalized local Ricci flow.  His
induction couples:

1. Unweighted $L^p$ curvature norms (finite by $|a\operatorname{Rm}| \le C/t$);
2. Derivatives $\nabla^m(a\operatorname{Rm})$ by standard interior Bernstein;
3. Derivatives $\nabla^m\chi$ bounded by bilipschitz metric comparison.

The added $-2ag$ term contributes:

- To the curvature evolution: an additional $-2a\operatorname{Rm}$, which is
  already controlled by $|a\operatorname{Rm}|$;
- To the Christoffel variation: terms involving $a\cdot g$, bounded by $Ca$;
- To higher derivatives: the $m$-th derivative of $-2a\operatorname{Rm}$
  involves $\nabla^m\chi$ and $\nabla^{m-k}\operatorname{Rm}$, handled by the
  same induction.

No new geometric quantity is needed.  The adaptation is a structural exercise
using the established bounds.  It can be done by starting from any positive
time $t_0 > 0$ where $|a\operatorname{Rm}(t_0)|$ is bounded.

## 9. Reproducible verification

See `workspace/scripts/verify_step26_general_p_and_sobolev.py`.

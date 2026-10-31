# Step 49: Normalized cutoff flow — superseded construction attempt

> **Step 50 supersession.** Sections 1.3(c), 2.3, 3.2--3.3, 4, and 5 below
> cannot establish the stated existence or extension theorems. Metric equivalence
> does not control the evolving connection or covariant cutoff jets; an
> \(L^{n/2}\) curvature bound does not give pointwise curvature; and
> \(\nabla_g^ka\) is not a prescribed bounded source. The valid replacement is
> `step50_normalized_yang_wang_verification.md`: short-time start is a direct
> lower-order perturbation of Yang's transported smooth-tame system, while
> continuation separately couples shifted weighted curvature, unweighted
> curvature, cutoff jets, and the connection. The nonlinear
> \(a+\varepsilon^2\) construction below is not established and must not be cited.

Session: S0910A03. Agent2 / Constructor. Phase: Execute.

## 0. Purpose and scope

This note provides the missing per-datum flow start and positive-time extension
for the **normalized** cutoff Ricci flow

$$
\partial_t g = -2b\,(\operatorname{Ric}(g) + g), \qquad g(0) = g_0,
\tag{0.1}
$$

where $b = \chi^2$ (exact degenerate flow) or $b_\varepsilon = \chi^2 + \varepsilon^2$
(regularized flow), and $\chi \in C^\infty(M)$, $0 \le \chi \le 1$, is a fixed smooth
cutoff on a closed smooth $n$-manifold $M$.

The **unnormalized** equation $\partial_tg = -2\chi^2\operatorname{Ric}$ has short-time
existence by Yang's Theorem 8.2 (two independent approaches: transported-coefficient
DeTurck system, or coefficient regularization with $\varepsilon$-independent energy
bounds; \cite{yang1992}). Extension under bounded $|\chi^2\operatorname{Rm}|$ is proved
by Wang's Theorem 4.1 (\cite{wang2015pseudolocality}), via the staggered induction
$\nabla^m(\chi^2\operatorname{Rm}) \to \nabla^{m+1}\chi \to \nabla^m\operatorname{Rm}$.

**The normalized equation (0.1) differs by $-2bg$.** This term is zeroth order in $g$
and has $\varepsilon$-independent coefficients: $\nabla^k b_\varepsilon = \nabla^k(\chi^2)$
for all $k \ge 1$. We prove:

1. The normalization creates only bounded lower-order corrections in every
   curvature-derivative energy, preserving the $\varepsilon$-independent Grönwall
   structure (§2–§3).
2. Coefficient regularization produces a common $\varepsilon$-independent per-datum
   existence time, and the $\varepsilon \to 0$ limit is a smooth exact degenerate
   flow (§4).
3. The extension criterion (bounded $|\chi^2\operatorname{Rm}|$ implies smooth extension)
   carries over unchanged (§5).
4. If a maximal exact flow ends at finite $T^* > 0$, the Moser endpoint is bounded
   on $[T^*/2, T^*)$, so the staggered estimates give smooth extension past $T^*$
   — a contradiction (§6).

**What this note does NOT prove.** It provides the per-datum flow construction and
extension criterion. The sequence-uniform first-exit observation time, the localized
$K_2/J_m/Q$ estimates, and the terminal topological contradiction all require the
exact $\varepsilon = 0$ flow to exist first, and they use localized support identities
(stationary collars, disjoint supports, frozen complement) that are valid only for
the exact degenerate flow. These are developed in the companion notes from Steps 35–47
and are invoked only after the exact flow established here.

---

## 1. The normalization perturbation: exact formulas

Write $a = \chi^2$ and $b$ for either $a$ or $b_\varepsilon = a + \varepsilon^2$.

### 1.1 Christoffel variation from $h = -2b\,g$

Using $\nabla g = 0$ (Levi-Civita compatibility):

$$
\partial_t\Gamma^k_{ij}\big|_N
= \tfrac12 g^{k\ell}\bigl(\nabla_i(-2bg_{j\ell})
+ \nabla_j(-2bg_{i\ell}) - \nabla_\ell(-2bg_{ij})\bigr)
= -\bigl(\delta^k_j\,\partial_ib + \delta^k_i\,\partial_jb
- g_{ij}\,\nabla^kb\bigr).
\tag{1.1}
$$

All terms involve only $\nabla b = \nabla a = 2\chi\nabla\chi$
($\varepsilon$-independent, bounded by $2\|\nabla\chi\|_\infty$).

### 1.2 Curvature variation from $h = -2b\,g$

Since $b$ is a scalar, $[\nabla_i,\nabla_j]b = 0$, and the curvature variation
$\partial_tR^k{}_{lij}|_N = \nabla_i(\partial_t\Gamma^k_{jl})|_N - (i \leftrightarrow j)$
simplifies. Lowering $k$ and including the metric variation $h_{km}R^m{}_{lij}$:

$$
\partial_t R_{klij}\big|_N = -2b\,R_{klij}
+ \bigl(g_{ki}H_{jl} + g_{jl}H_{ik} - g_{kj}H_{il} - g_{il}H_{jk}\bigr),
\tag{1.2}
$$

where $H_{ij} = \nabla_i\nabla_jb = \nabla_i\nabla_ja$ is the Hessian of $b$
(equal to $\nabla^2a$ for all $\varepsilon$, bounded by $C(\chi)$).
The derivation: $g_{km}\partial_tR^m{}_{lij} = (g\owedge H)_{klij}$ (positive sign
because the two minus signs from (1.1) compose with the antisymmetrization
to produce the standard KN product); the lowering term $h_{km}R^m = -2bR_{klij}$.

In Kulkarni–Nomizu notation:

$$
\partial_t\operatorname{Rm}\big|_N = -2b\,\operatorname{Rm} + g\owedge\nabla^2 b.
\tag{1.3}
$$

### 1.3 Structural properties

(a) **Reaction term** $-2b\,\operatorname{Rm}$: linear in Rm, coefficient
$b \in [0,\,1+\varepsilon^2]$. In the $L^p$ energy $\int|\operatorname{Rm}|^p$,
the covariant tensor variation contributes $-4b|\operatorname{Rm}|^2$, but the
four inverse-metric factors in $|\operatorname{Rm}|^2 = g^{\cdot\cdot}g^{\cdot\cdot}
g^{\cdot\cdot}g^{\cdot\cdot}R\cdots R\cdots$ each contribute $+2b$, giving $+8b|\operatorname{Rm}|^2$.
Net reaction on $|\operatorname{Rm}|^2$: $+4b|\operatorname{Rm}|^2$. Combined with the
volume variation $-nb\,d\mu$, the full $L^p$ contribution is
$(2p-n)\int b|\operatorname{Rm}|^p\,d\mu$. **This is positive for $p > n/2$,
not dissipative.** However, it is bounded by $(2p-n)\cdot 2\int|\operatorname{Rm}|^p$
(since $b \le 2$), so it enters the Gr\"onwall coefficient additively.

(b) **Source term** $+g\owedge\nabla^2b$: depends only on $\nabla^2a$ and $g$,
no curvature. Bounded by $C(\chi) := 4\|\chi\nabla^2\chi + |\nabla\chi|^2\|_\infty$
pointwise, independent of $\varepsilon$ and independent of curvature.

(c) **$\varepsilon$-independence** of all normalization terms: the **coordinate**
derivatives $\partial^kb_\varepsilon = \partial^ka$ for $k \ge 1$. The covariant
derivatives $\nabla^k_{g(t)}a$ additionally involve the evolving connection
$\Gamma(g(t))$, but under metric equivalence $\frac12g_0 \le g(t) \le 2g_0$,
all connection coefficients and hence all $\|\nabla^k_{g(t)}a\|_\infty$ are
controlled by $C(g_0, \chi)$. This is $\varepsilon$-independent because the
metric equivalence itself is established $\varepsilon$-independently (see \S4).

(d) **Volume form variation** from $-2bg$:
$\frac{d}{dt}d\mu\big|_N = \tfrac12\operatorname{tr}(g^{-1}(-2bg))\,d\mu = -nb\,d\mu$.

---

## 2. Combined curvature evolution

### 2.1 Full evolution of Rm

Combining Yang's formula for $\partial_tg = -2b\operatorname{Ric}$
(cf.\ Wang \cite{wang2015pseudolocality}, equation after Theorem 4.1)
with the normalization (1.3):

$$
\partial_t R_{ijkl}
= b\bigl[\Delta R_{ijkl} + Q(R)_{ijkl} - \operatorname{Ric}\owedge R\bigr]
+ \bigl[\nabla^2b \circledast \nabla\operatorname{Ric}
+ \nabla b \circledast \nabla\operatorname{Rm}\bigr]
\underbrace{- 2b\,R_{ijkl} + (g\owedge\nabla^2b)_{ijkl}}_{\text{normalization}},
\tag{2.1}
$$

where $Q(R)$ is Hamilton's curvature quadratic and $\circledast$ denotes
algebraic tensor products with bounded combinatorial coefficients.

> **Correction note (TTCS-verified).** The cutoff interaction with Ric produces
> $\nabla^2b\circledast\operatorname{Ric}$ and $\nabla b\circledast\nabla\operatorname{Ric}$
> (not $\nabla\operatorname{Rm}$). Additionally, at $m \ge 1$, the time derivative
> $\partial_t\nabla^m\operatorname{Rm}$ picks up connection-commutator terms
> $\sum_{r=0}^{m-1}\nabla^r\dot\Gamma_N*\nabla^{m-1-r}\operatorname{Rm}$
> where $\dot\Gamma_N \sim \nabla a$ (bounded, $\varepsilon$-independent).
> These are lower-order but must be included in the staggered induction.

### 2.2 $L^p$ energy evolution

Set $E_p(t) = \int_M|\operatorname{Rm}|^p\,d\mu$. The complete normalization
contribution to $\frac{d}{dt}E_p$ includes the tensor variation, inverse-metric
variation, and volume variation:

**Full norm variation from $h = -2bg$:**
$|\operatorname{Rm}|^2 = g^{ik}g^{jl}g^{mr}g^{ns}R_{ijmn}R_{klrs}$ has four
inverse-metric factors, each contributing $+2b$ from $\partial_tg^{-1} = +2bg^{-1}$.
The covariant tensor variation $\partial_tR_{ijkl}|_N = -2bR_{ijkl} + (g\owedge H)_{ijkl}$
contributes $-4b|\operatorname{Rm}|^2 + 2\langle\operatorname{Rm},g\owedge H\rangle$.
Net: $\partial_t|\operatorname{Rm}|^2|_N = 4b|\operatorname{Rm}|^2
+ 2\langle\operatorname{Rm},g\owedge\nabla^2b\rangle$.

**Combined with volume variation $-nb\,d\mu$:**
$$
\frac{d}{dt}\int|\operatorname{Rm}|^p\,d\mu\bigg|_N
= (2p-n)\int b|\operatorname{Rm}|^p\,d\mu
+ p\int|\operatorname{Rm}|^{p-2}\langle\operatorname{Rm},g\owedge\nabla^2b\rangle\,d\mu.
\tag{2.2a}
$$

For $p > n/2$, the reaction coefficient $(2p-n)$ is **positive** (not dissipative).
But since $0 \le b \le 2$, it is bounded:
$(2p-n)\int b|\operatorname{Rm}|^p \le 2(2p-n)E_p$.
The source term: $|p\int|\operatorname{Rm}|^{p-2}\langle\operatorname{Rm},g\owedge H\rangle|
\le Cp\,C_2(\chi)(E_p + \operatorname{Vol})$ by Young.

**Combined upper bound:**

$$
\frac{d}{dt}E_p \le \bigl[\text{Yang's bound}\bigr]
+ C(n,p,\chi)\bigl(E_p + \operatorname{Vol}\bigr).
\tag{2.2}
$$

The additional Grönwall coefficient $C(n,p,\chi)$ is $\varepsilon$-independent and
polynomial in $p$.

### 2.3 Higher-derivative evolution

Wang's Lemma 4.4 gives for the unnormalized flow:

$$
\partial_t(\nabla^m\operatorname{Rm})
= \chi^2\Delta\nabla^m\operatorname{Rm}
+ \sum_{i+j+k=m+2,\,k\le m+1}\nabla^i\chi*\nabla^j\chi*\nabla^k\operatorname{Rm}
+ \sum_{i+j+k=m}\nabla^i(\chi^2)*\nabla^j\operatorname{Rm}*\nabla^k\operatorname{Rm}.
$$

The normalization adds (including connection-commutator terms from $\dot\Gamma_N$):

$$
\partial_t(\nabla^m\operatorname{Rm})\big|_N
= \nabla^m\bigl(-2b\operatorname{Rm} + g\owedge\nabla^2b\bigr)
+ \sum_{r=0}^{m-1}\nabla^r\dot\Gamma_N*\nabla^{m-1-r}\operatorname{Rm},
\tag{2.3}
$$

where $\dot\Gamma_N \sim \nabla a$ is the normalization Christoffel variation (1.1).
The first term expands to $-2b\nabla^m\operatorname{Rm}$
plus lower-order products $\nabla^j b\cdot\nabla^{m-j}\operatorname{Rm}$ ($j \ge 1$)
and $\nabla^{m+2}a$ (fixed smooth). The commutator terms involve only
$\nabla^r(\nabla a)$ (bounded) times previous-level curvature.

Every term is controlled by:

- $-2b\,\nabla^m\operatorname{Rm}$: current-level reaction (bounded coefficient $b \le 2$)
- $\nabla^ja$ for $j \ge 1$: coordinate derivatives of fixed smooth functions
  (bounded, $\varepsilon$-independent; covariant versions controlled by metric equivalence)
- $\nabla^{m-j}\operatorname{Rm}$ for $j \ge 1$: previous induction levels
- $\nabla^{m+2}a$: fixed smooth function on $M$, bounded

**Conclusion:** The normalization terms at every derivative order fit into the same
algebraic structure as Yang/Wang's cutoff terms, with the replacement
$\text{cutoff}\to\text{cutoff}+\text{normalization}$ at each level. The staggered
induction closes with $\varepsilon$-independent bounds, provided connection commutators
are included at each level.

---

## 3. Staggered induction with normalization

Wang's extension proof (Theorem 4.1, Lemmas 4.4–4.6, 4.10–4.11, Proposition 4.13)
uses the staggered hierarchy:

$$
\nabla^m(\chi^2\operatorname{Rm}) \;\longrightarrow\; \nabla^{m+1}\chi
\;\longrightarrow\; \nabla^m\operatorname{Rm}.
\tag{3.1}
$$

### 3.1 Weighted curvature $U = b\,\operatorname{Rm}$

For the normalized flow, the weighted variable $U = b\operatorname{Rm}$ evolves by:

$$
\partial_tU = b\,\partial_t\operatorname{Rm} + (\partial_tb)\operatorname{Rm}.
\tag{3.2}
$$

The extra $\partial_tb$ vanishes for $b = a$ (time-independent cutoff).
For $b_\varepsilon$, $\partial_tb_\varepsilon = 0$ as well since $\chi$ is fixed.
So $\partial_tU = b\,\partial_t\operatorname{Rm}$, and the normalization adds:

$$
b\,\partial_t\operatorname{Rm}\big|_N = b(-2b\operatorname{Rm} + g\owedge\nabla^2b)
= -2b^2\operatorname{Rm} + b(g\owedge\nabla^2b)
= -2bU + b(g\owedge\nabla^2a).
\tag{3.3}
$$

The $-2bU$ term is a bounded reaction. The source $b(g\owedge\nabla^2a)$
is bounded by $C(\chi)$ pointwise.

### 3.2 Weighted higher derivatives $\nabla^m U$

At the $m$-th derivative level, the extra normalization terms in $\nabla^m U$ involve:
- $b\nabla^m(-2b\operatorname{Rm})$: gives $-2b^2\nabla^m\operatorname{Rm}$
  plus lower-order terms involving $\nabla^j(b^2)$ for $j \ge 1$, all bounded.
- $b\nabla^m(g\owedge\nabla^2b)$: involves $\nabla^{m+2}a$ (bounded) and lower.

All terms have $\varepsilon$-independent coefficients and are at most linear in
previous-level curvature quantities. The staggered induction (3.1) closes exactly
as in Wang's proof, with the Grönwall coefficients acquiring additive constants from
the normalization source terms.

### 3.3 Cutoff-jet evolution $\nabla^m\chi$

Wang's Lemma 4.6: $\partial_t|\nabla^m\chi| \le C\sum_{k\le m-1}
|\nabla^k(\chi^2\operatorname{Ric})|\cdot|\nabla^{m-k}\chi|$.

For the normalized flow, $\partial_tg = -2b(\operatorname{Ric}+g)$, so
$\partial_t\Gamma$ gets the extra (1.1). The evolution of $|\nabla^m\chi|$ gets
extra terms from $\partial_t\Gamma|_N$ coupling to $\nabla^{m-1}\chi$:

$$
\partial_t|\nabla^m\chi|\big|_N \le C\sum_{k\le m-1}|\nabla^k(b\cdot g)|
\cdot|\nabla^{m-k}\chi| \le C(\chi)\sum_{k\le m-1}|\nabla^{m-k}\chi|.
\tag{3.4}
$$

These are bounded by previous-level cutoff jets (since $b\cdot g$ has bounded
derivatives of all orders in the fixed coordinate system). The Grönwall structure
is preserved.

---

## 4. Coefficient-regularized existence and $\varepsilon\to0$ passage

### 4.1 Regularized equation for $\varepsilon > 0$

$$
\partial_tg_\varepsilon = -2b_\varepsilon(\operatorname{Ric}(g_\varepsilon) + g_\varepsilon),
\qquad g_\varepsilon(0) = g_0, \qquad b_\varepsilon = \chi^2 + \varepsilon^2.
\tag{4.1}
$$

Since $b_\varepsilon \ge \varepsilon^2 > 0$, the operator
$g \mapsto -2b_\varepsilon(\operatorname{Ric}(g) + g)$ is a quasilinear second-order
strictly elliptic operator (after DeTurck gauge fixing), plus a bounded zeroth-order
term $-2b_\varepsilon g$. Standard quasilinear parabolic theory gives a unique smooth
maximal solution $g_\varepsilon$ on $[0, T_\varepsilon)$ with $T_\varepsilon > 0$.

### 4.2 $\varepsilon$-independent per-datum existence time

The common existence time is established by a first-exit argument on the energy
and metric equivalence, not by integrating the Moser endpoint from $t = 0$.

Define the first-exit time $\tilde T_\varepsilon$ as the supremum of times $t$ such that:
- $E_{n/2}(t) = \int|\operatorname{Rm}_\varepsilon|^{n/2}\,d\mu \le 2E_{n/2}(0)$,
- $\frac12 g_0 \le g_\varepsilon(t) \le 2g_0$.

**Energy bound:** By (2.2), $\frac{d}{dt}E_{n/2} \le C(n,\chi)(E_{n/2} + \operatorname{Vol})$.
Grönwall gives $E_{n/2}(t) \le (E_{n/2}(0) + C\cdot\operatorname{Vol}\cdot t)e^{Ct}$,
which stays below $2E_{n/2}(0)$ for $t \le T_1(g_0, \chi)$.

**Metric equivalence:** On $[0, \tilde T_\varepsilon)$, the pointwise drift rate is:
$$
|\partial_tg_\varepsilon|_{g_0} \le 2b_\varepsilon(|\operatorname{Ric}_\varepsilon|_{g_0}
+ |g_\varepsilon|_{g_0}).
\tag{4.2}
$$
By Sobolev ($n/2 = 2$ in dimension 4) applied to the $L^{n/2}$ energy bound and metric
equivalence, $|\operatorname{Ric}_\varepsilon|$ is controlled by
$\mathcal C_S \cdot E_{n/2}^{2/n}$ (which is finite and $\varepsilon$-independent on
the first-exit interval). Together with $|g_\varepsilon|_{g_0} \le 2$, the drift is
$O(C(g_0,\chi)\cdot t)$, so metric equivalence holds for
$t \le T_2(g_0, \chi)$.

**Moser endpoint (a posteriori, for $t > 0$):**
$$
\|b_\varepsilon\operatorname{Rm}_\varepsilon\|_\infty(t)
\le C(n)\mathcal C_S(t)\bigl(t\|\nabla\chi\|_\infty^2 + 1\bigr)\,t^{-1}
+ C'(\chi)\,t.
\tag{4.3}
$$
The extra $C'(\chi)t$ comes from the normalization source. This is finite for each
$t > 0$ and $\varepsilon$-independent, but **diverges as $t \to 0$**.
It is used only in the positive-time slab argument (§6), not for metric equivalence.

Setting $T_0 = \min(T_1, T_2) > 0$ gives the $\varepsilon$-independent per-datum
existence time.

### 4.3 $\varepsilon$-uniform higher-derivative estimates

On any compact $K \subset \{\chi > 0\}$, set $\eta = \inf_K\chi^2 > 0$.
Then $b_\varepsilon \ge \eta$ on $K$, so on $K$ the equation is uniformly
parabolic with parabolicity constant $\eta$. Interior Schauder estimates give:

$$
\|\nabla^m\operatorname{Rm}_\varepsilon\|_{C^0(K\times[\tau,T_0])}
\le C(K, \tau, m, g_0, \chi)
\tag{4.5}
$$

for each $\tau > 0$, $m \ge 0$, independent of $\varepsilon$.

### 4.4 $\varepsilon\to 0$ passage

**Interior.** On nested compacts $K_k = \{\chi \ge 1/k\}$, the $\varepsilon$-uniform
$C^{m,\alpha}$ bounds (4.5) and Arzelà–Ascoli give a diagonal subsequence
$g_\varepsilon \to g$ in $C^\infty_{\mathrm{loc}}(\{\chi > 0\} \times (0, T_0])$.

**Zero set.** On the interior of $\{\chi = 0\}$: $b_\varepsilon = \varepsilon^2$,
$\nabla b_\varepsilon = 0$, $\nabla^2b_\varepsilon = 0$. The curvature evolution
reduces to $\partial_t\operatorname{Rm} = \varepsilon^2(\Delta\operatorname{Rm}
+ \text{Rm*Rm}) - 2\varepsilon^2\operatorname{Rm}$. By Grönwall on
$\int|\operatorname{Rm}|^p$:
$|\operatorname{Rm}_\varepsilon(t)| \le C(g_0)\cdot e^{C\varepsilon^2t}$
(bounded, not blowing up). Therefore:
$|g_\varepsilon(t) - g_0| \le 2\varepsilon^2\int_0^t(C(g_0) + n + 1)\,ds
= O(\varepsilon^2 t) \to 0$ as $\varepsilon \to 0$.

**Interface and global regularity.** The diagonal interior limit combined with the
zero-set stationarity gives a $C^0$ limit $g(t)$ on all of $M$ for $t \in (0, T_0]$.
For full $C^\infty(M)$ smoothness across $\partial\operatorname{supp}(\chi)$,
the argument cannot rely on weighted estimates $a^m\nabla^m\operatorname{Rm} \in L^p$
alone (as correctly noted by TTCS: a degenerate weight can hide unmatched jets).

Instead, we invoke Yang's Theorem 8.2 directly: the unnormalized cutoff equation
$\partial_tg = -2\chi^2\operatorname{Ric}$ has a smooth solution on $M$ by Yang's
Approach 1 (transported-coefficient DeTurck system with smooth-tame estimates) or
Approach 2 (coefficient regularization with convergence on all of $M$). The extra
$-2\chi^2 g$ is a smooth zeroth-order perturbation that does not change the principal
symbol, the DeTurck gauge structure, or the smooth-tame estimates. Yang's proof
therefore applies to the normalized equation, giving a smooth solution on all of $M$.

The coefficient-regularization route (Approach 2 above) provides the additional
$\varepsilon$-uniform energy bounds needed for the first-exit framework.

**Conclusion (existence):**

> **Theorem 4.1 (Per-datum existence).** *Let $(M, g_0)$ be a closed smooth
> Riemannian manifold, $\chi \in C^\infty(M)$, $0 \le \chi \le 1$. Then there
> exists $T_0 = T_0(g_0, \chi) > 0$ and a smooth family $g(t)$, $t \in [0, T_0]$,
> satisfying $\partial_tg = -2\chi^2(\operatorname{Ric}(g) + g)$ on $M \times (0,T_0]$,
> with $g(0) = g_0$. The solution is smooth on all of $M$ for $t > 0$, including
> across $\partial\operatorname{supp}(\chi)$, and $g(t)|_{\{\chi=0\}} = g_0|_{\{\chi=0\}}$
> for all $t$. The existence time $T_0$ depends on $(g_0, \chi)$ through $\varepsilon$-independent
> quantities: the initial curvature energy $\int|\operatorname{Rm}_0|^{n/2}$, the
> initial Sobolev constant, and $\|\nabla\chi\|_\infty$.*
>
> *Proof route: Yang's Theorem 8.2 Approach 2 adapted to the normalized equation.
> Global smoothness by Yang's Approach 1 (smooth-tame DeTurck). The zeroth-order
> perturbation $-2\chi^2g$ does not affect the principal symbol, derivative loss,
> or smooth-tame estimates.*

---

## 5. Extension criterion

### 5.1 Statement

> **Theorem 5.1 (Extension).** *Let $g(t)$, $t \in [0, T^*)$, be a smooth solution
> of $\partial_tg = -2\chi^2(\operatorname{Ric} + g)$ on a closed manifold $M$, with
> $T^* < \infty$. If $\|\chi^2\operatorname{Rm}\|_\infty$ is uniformly bounded on
> $[0, T^*)$, then $g(t)$ extends smoothly past $T^*$.*

### 5.2 Proof

Follows the exact structure of Wang's Theorem 4.1, adapted for the normalization.

**Step 1: Metric equivalence.** If $|\chi^2\operatorname{Rm}| \le K$ on $[0, T^*)$,
then $|\operatorname{Ric}| \le K/\varepsilon_0^2$ on $\{\chi \ge \varepsilon_0\}$,
and the metric drift $|g(t) - g_0| \le 2K T^* + 2T^*$ (the $2T^*$ from the
normalization term $-2\chi^2g$) is bounded. So metrics $g(t)$ are uniformly
equivalent to $g_0$ on $[0, T^*)$.

**Step 2: Sobolev constant and gradient control.** From metric equivalence,
$\|\nabla\chi\|_\infty(t) \le C$ and $\mathcal C_S(t) \le C$ uniformly
(Wang's Proposition 4.9 analog).

**Step 3: $L^p$ curvature bounds.** By (2.2), $\frac{d}{dt}\int|\operatorname{Rm}|^p
\le C(K,\chi)\int|\operatorname{Rm}|^p + C(\chi)\operatorname{Vol}$.
Grönwall gives $\|\operatorname{Rm}\|_p(t) \le C(g_0, \chi, K, p, T^*)$ uniformly
(Wang's Lemma 4.10 analog).

**Step 4: Staggered derivative bounds.** Wang's induction scheme
$\nabla^m(\chi^2\operatorname{Rm}) \to \nabla^{m+1}\chi \to \nabla^m\operatorname{Rm}$
carries through with the normalization corrections from §3. At each level:

- The extra $-2b\nabla^m\operatorname{Rm}$ is a bounded reaction (coefficient $\le 2K$).
- The extra $\nabla^m(g\owedge\nabla^2a)$ involves only fixed smooth functions.
- The extra cutoff-jet corrections (3.4) are absorbed by previous-level bounds.

The conclusion: $\|\nabla^m(\chi^2\operatorname{Rm})\|_p$,
$\|\nabla^{m+1}\chi\|_p$, and $\|\nabla^m\operatorname{Rm}\|_p$ are
uniformly bounded on $[0, T^*)$ for all $m \ge 0$ and $p > 100$.

**Step 5: Smooth extension.** Sobolev embedding $\to$ uniform $C^k$ bounds
$\to$ Arzelà–Ascoli gives a smooth limit $g(T^*) = \lim_{t\to T^*}g(t)$.
Restart using Theorem 4.1. $\square$

---

## 6. Positive-time slab argument and continuation

### 6.1 Context

In the first-exit framework (Steps 35–47), the Moser iteration endpoint on
a first-exit interval $[0,T]$ gives:

$$
|\chi^2\operatorname{Rm}(t)| \le C\gamma/t,
\tag{6.1}
$$

where $\gamma = \mathcal S\cdot K_2^{1/2}$ is the collapse-independent absorption
parameter.  **This bound diverges as $t \to 0$.**

Step 48 correctly observed that this CANNOT be used as a uniform $|\chi^2\operatorname{Rm}|$
bound on $[0, T]$. The correct logical use is:

### 6.2 Continuation by contradiction

Suppose the exact degenerate flow $g(t)$ from Theorem 4.1 has a finite maximal existence
time $T^* > 0$ (i.e., cannot be extended past $T^*$ by any restart). By the extension
criterion (Theorem 5.1), we must have:

$$
\limsup_{t \to T^*}\|\chi^2\operatorname{Rm}(t)\|_\infty = \infty.
\tag{6.2}
$$

But on the slab $[T^*/2, T^*)$, the Moser endpoint (6.1) gives:

$$
|\chi^2\operatorname{Rm}(t)| \le C\gamma/t \le 2C\gamma/T^* < \infty
\qquad\text{for } t \in [T^*/2, T^*).
\tag{6.3}
$$

This is a **finite** bound (depending on $T^*$ but not approaching infinity).
Theorem 5.1 then gives smooth extension past $T^*$, contradicting maximality.

### 6.3 Conclusion

> **Corollary 6.1 (Per-datum global existence on the first-exit interval).**
> *Once the first-exit estimates (§5 of the companion notes) are established on
> an exact $\varepsilon = 0$ flow, the flow exists smoothly for the entire
> first-exit observation time $T = \theta r^2$. The curvature endpoint (6.1)
> is valid for all $t \in (0, T]$, with the understanding that it diverges as
> $t \to 0$ but is finite for each positive time.*

### 6.4 The correct logical order

The dependencies are now:

1. **Per-datum start** (Theorem 4.1): uses only $g_0$, $\chi$, standard parabolic
   theory, and $\varepsilon$-independent energy estimates. Produces an exact smooth
   flow on some $[0, T_0]$.

2. **Localized first-exit estimates**: applied to the EXACT $\varepsilon = 0$ flow
   from step 1. Uses stationary collars ($\partial_tg = 0$ where $\chi = 0$),
   disjoint-support summation, localized $K_2$/$J_m$/$Q$ identities. These are NOT
   available for the $b_\varepsilon$-flow.

3. **Sequence-uniform observation time**: from the self-improving nature of the
   first-exit bootstrap — if $K_2(t) < 2K_2(0)$ and metric drift $< d_0$, the
   Grönwall coefficient ensures a uniform $T = \theta r^2$ with $\theta$ depending
   only on the support parameters.

4. **Continuation** (Corollary 6.1): if the first-exit time is less than the maximal
   existence time, no action needed. If the maximal time $T^*$ is less than $\theta r^2$,
   the positive-time slab argument gives a contradiction.

5. **Terminal topological contradiction** (§7 of companion notes): uses the smooth flow
   at the observation time $T$ to extract bounded-curvature charts and invoke the
   spectral density.

Steps 2–5 are invoked ONLY AFTER the exact flow from step 1 exists.

---

## 7. Explicit source identification

| Result | Source | Normalization status |
|--------|--------|---------------------|
| Short-time existence, $\varepsilon$-regularization | Yang Thm 8.2, Approach 2 | Extra terms $\varepsilon$-independent, lower-order |
| Moser curvature endpoint | Yang Thm 9.2 | Extra source integrates to $O(t)$, subdominant |
| Extension under bounded $\chi^2\operatorname{Rm}$ | Wang Thm 4.1, Lemmas 4.4–4.13 | Staggered induction + normalization (§3) |
| Staggered derivative hierarchy | Wang Rmk 4.2, Props 4.9–4.13 | Same structure, additive Grönwall corrections |
| Metric equivalence, Sobolev control | Yang §9, Wang Prop 4.9 | Extra drift $O(T^*)$ from $-2\chi^2g$ |

**What is newly derived here** (not directly in Yang or Wang):
- Formula (1.2)–(1.3) for the curvature variation under $-2bg$
- The explicit $\varepsilon$-independence argument for the Grönwall coefficient (§2.2)
- The positive-time slab continuation (§6.2), which resolves the $\gamma/t$
  divergence at $t = 0$ without requiring a uniform bound on $[0, T]$
- The logical ordering (§6.4) separating per-datum construction from sequence-uniform
  localized estimates

---

## 8. Summary and interface

**Established (structural compatibility):** The normalization $-2\chi^2 g$ adds only
bounded lower-order corrections to Yang's curvature energy hierarchy and Wang's
staggered derivative induction. The $L^p$ reaction coefficient is $(2p-n)b$ (positive
for $p > n/2$, not dissipative, but bounded). All extra terms have $\varepsilon$-independent
coordinate derivatives; covariant derivatives are controlled by metric equivalence.

**Per-datum existence (Theorem 4.1):** Follows from Yang's Theorem 8.2 (both approaches)
with the zeroth-order normalization perturbation. Approach 1 (smooth-tame DeTurck) gives
global smoothness on $M$. Approach 2 (coefficient regularization) gives the
$\varepsilon$-independent energy bounds needed for the first-exit framework. The interface
regularity across $\partial\operatorname{supp}(\chi)$ requires Yang's full smooth-tame
framework (Approach 1), not only diagonal Arzelà–Ascoli on interior compacts.

**Extension (Theorem 5.1):** Structurally compatible with Wang's proof. The complete
arbitrary-order staggered induction with connection commutators and the normalization
corrections is classified but not yet carried through as a complete formal proof with
all constants (cf.\ Steps 40, 44, 45 for partial realizations). The note explicitly
records this as conditional.

**Positive-time slab argument (§6.2):** Logically sound. If $T^*$ is a finite maximal time,
the Moser endpoint $C\gamma/t$ is bounded on $[T^*/2, T^*)$, giving smooth extension —
contradiction. This resolves the $\gamma/t$ divergence at $t = 0$ without circular reasoning.

**Interface to the first-exit framework:** Once an exact $\varepsilon = 0$ flow exists
(Theorem 4.1), the localized support estimates (Steps 35–47) begin on the exact flow only.
The first-exit bootstrap produces a sequence-uniform observation time, and the slab argument
ensures the flow reaches that time. The terminal topological contradiction then applies.

**Not established:** Uniqueness of the degenerate flow. Complete formal staggered induction
with all connection commutators and constants. Any result for the positive branch,
arbitrary four-manifold topology, dimensions $n \ge 5$, dimension-only constants,
or Lean formalization.

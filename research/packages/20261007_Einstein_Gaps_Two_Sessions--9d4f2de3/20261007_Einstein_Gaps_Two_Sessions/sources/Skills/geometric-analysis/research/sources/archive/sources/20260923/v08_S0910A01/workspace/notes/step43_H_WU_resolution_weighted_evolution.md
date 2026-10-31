# Step 43: Resolution of H-WU — exact weighted $U_m$ evolution and cutoff-jet provenance

Session: S0910A01. Agent2 / Constructor. Phase: Execute.

## 0. Purpose

Resolve hypothesis H-WU from the Step 42 repair: derive the exact tensor-level
evolution equation for $U_m = \nabla^m U$ where $U = aT$, $a = \chi^2$,
$T = \operatorname{Rm} + G$, under $\partial_t g = -2aE$, and prove that
**every surviving $C_{m+2}$ contribution carries the $\chi C_{m+2}$ weight
needed by A03's staggered energy mechanism.**

This is the "full arbitrary-order index-level tensor ledger" identified by
A03 #363 as outstanding, and the "exact all-order weighted $U_m$ equation"
identified by Step 42 §4 as unresolved.

---

## 1. Setup and conventions

Closed Riemannian manifold $(M, g(t))$ with smooth cutoff $\chi: M \to [0,1]$
fixed as a function.  Define:

$$
a = \chi^2, \quad E = \operatorname{Ric}_g + g, \quad
T = \operatorname{Rm} + G, \quad G = \frac{g \owedge g}{2(n-1)},
\quad U = aT. \tag{1.1}
$$

Flow: $\partial_t g = -2aE$, metric variation $h = -2aE$.

Notation: $C_k = \nabla^k \chi$, $T_m = \nabla^m T$, $U_m = \nabla^m U$.
Indices of covariant derivatives are taken with respect to $g(t)$.

**Key scalar identity:**

$$
\nabla^k a = \nabla^k(\chi^2) = \sum_{s=0}^{k} \binom{k}{s} C_s \otimes C_{k-s}.
\tag{1.2}
$$

The **top single jet** is $2\chi C_k$ (from $s = 0$ and $s = k$).
All other terms are products $C_s C_{k-s}$ with $1 \le s \le k-1$, both
factors of order $\le k-1$.  In particular:

$$
|\nabla a|^2/a = 4|d\chi|^2, \qquad
\nabla^2 a = 2\chi C_2 + 2 C_1 \otimes C_1. \tag{1.3}
$$

---

## 2. Evolution of the unweighted shifted curvature $T$

From the Besse variation formula (Theorem 1.174) under $h = -2aE$, the
all-lower Riemann evolution has the structure:

$$
\partial_t R_{ijkl} = \underbrace{-[(\nabla^2 a) \star E]_{ijkl}}_{\text{Hessian-}a}
\;\underbrace{- 2[(\nabla a) \star (\nabla E)]_{ijkl}}_{\text{gradient-}a}
\;\underbrace{- [a \nabla^2 E]_{ijkl}^{\rm Lich}}_{\text{principal}}
\;+ R \star h, \tag{2.1}
$$

where the Hessian-$a$ contraction from Step 35 is:

$$
[(\nabla^2 a) \star E]_{ijkl} =
A_{ik}E_{jl} - A_{il}E_{jk} - A_{jk}E_{il} + A_{jl}E_{ik}, \tag{2.2}
$$

with $A_{ij} = \nabla_i \nabla_j a$.  The principal part, after resolving the
specific index symmetrizations and using the second Bianchi identity, gives
the Lichnerowicz Laplacian $a\Delta_L \operatorname{Rm}$ plus curvature
reaction.

The $G$ variation is:

$$
\partial_t G = \frac{-2a}{n-1}(E \owedge g). \tag{2.3}
$$

Combining with $\nabla G = 0$, the shifted curvature equation is:

$$
(\partial_t - a\Delta)T = (\nabla^2 a) \star E + (\nabla a) \star (\nabla E)
+ a \cdot \mathcal{Q}(T) + \mathcal{N}(a,T), \tag{2.4}
$$

where $\mathcal{Q}$ is the quadratic curvature reaction and $\mathcal{N}$
collects the normalization ($+g$) and $G$-variation terms.  The reaction
satisfies $|\mathcal{Q}| \le C(|T|^2 + |T| + 1)$ and the normalization
$|\mathcal{N}| \le Ca(|T| + 1)$.

**Critical structural observation:**  The maximum cutoff-derivative order
in $\partial_t T$ is **two** (from $\nabla^2 a$).  All other terms involve
$\nabla a$ (order 1) or $a$ (order 0) only.

---

## 3. Evolution of the weighted curvature $U = aT$

Since $a = \chi^2$ is time-independent as a scalar function:

$$
\partial_t U = a \partial_t T. \tag{3.1}
$$

**Proof:** $U = aT$ where $a: M \to \mathbb{R}$ is fixed.  For any
time-dependent tensor $T$, $\partial_t(aT) = a \partial_t T + (\partial_t a)T
= a\partial_t T$.

---

## 4. Evolution of $U_m = \nabla^m U$

Apply $\nabla^m$ to both sides of $\partial_t U = a\partial_t T$:

$$
\partial_t U_m = \partial_t(\nabla^m U)
= \nabla^m(a \partial_t T) + [\partial_t, \nabla^m]U. \tag{4.1}
$$

The two terms are analyzed separately.

### 4.1 Main term: $\nabla^m(a\partial_t T)$

By the Leibniz rule for covariant derivatives:

$$
\nabla^m(a\partial_t T) = \sum_{j=0}^{m} \binom{m}{j}
(\nabla^j a) \nabla^{m-j}(\partial_t T). \tag{4.2}
$$

**Cutoff-jet content of each summand.**

The term $\nabla^{m-j}(\partial_t T)$ involves $\nabla^{m-j}$ applied to
equation (2.4).  The highest cutoff derivative in $\partial_t T$ is from
$(\nabla^2 a) \star E$ (order 2).  By Leibniz, $\nabla^{m-j}((\nabla^2 a)
\star E)$ has top single jet from $(\nabla^{m-j+2}a) \star E$, which is
$C_{m-j+2}$ (more precisely, $2\chi C_{m-j+2}$ from (1.2)).

Combined with the outer $(\nabla^j a)$, which has top single jet
$\chi C_j$ from (1.2), the product's highest single-order jet is:

$$
\max(j, m-j+2) \le m+1 \quad \text{for } j \ge 1. \tag{4.3}
$$

At $j = 1$: $\max(1, m+1) = m+1$.  At $j = m$: $\max(m, 2) = m$.  No
$C_{m+2}$ arises for $j \ge 1$.

At $j = 0$: the full content of $a\nabla^m(\partial_t T)$ is analyzed next.

### 4.2 The $j = 0$ term and the unique $C_{m+2}$ source

$$
a\nabla^m(\partial_t T) \ni a \nabla^m\bigl((\nabla^2 a) \star E\bigr).
\tag{4.4}
$$

Using the factorization from §3: $a(\nabla^2 a) \star E = (\nabla^2 a) \star
(aE)$, we write:

$$
a\nabla^m((\nabla^2 a) \star E) = \nabla^m((\nabla^2 a) \star (aE))
- \sum_{j=1}^{m}\binom{m}{j}(\nabla^j a)\nabla^{m-j}((\nabla^2 a) \star E).
\tag{4.5}
$$

Wait — this identity follows because $\nabla^m(a \cdot F) = a\nabla^m F +
\sum_{j=1}^m \binom{m}{j}(\nabla^j a)\nabla^{m-j}F$ for any tensor $F$.
Since $aF = a[(\nabla^2 a) \star E] = (\nabla^2 a) \star (aE)$, we have:

$$
a\nabla^m((\nabla^2 a) \star E) = \nabla^m((\nabla^2 a) \star (aE))
- \sum_{j=1}^m \binom{m}{j}(\nabla^j a)\nabla^{m-j}((\nabla^2 a) \star E).
$$

But it is simpler to directly expand the Leibniz product
$\nabla^m((\nabla^2 a) \star (aE))$:

$$
\nabla^m((\nabla^2 a) \star (aE)) = \sum_{s=0}^{m}
\binom{m}{s}(\nabla^{s+2}a) \star \nabla^{m-s}(aE) + \mathcal{R}_{\rm com},
\tag{4.6}
$$

where $\mathcal{R}_{\rm com}$ denotes curvature-commutator corrections from
reordering covariant derivatives.  These corrections involve **lower**
derivative orders of both factors plus curvature, hence their single-jet order
is strictly less than $C_{m+2}$.

**The $s = m$ term:**

$$
(\nabla^{m+2}a) \star (aE) = (2\chi C_{m+2} + \text{product terms}) \star (aE).
\tag{4.7}
$$

Since $|aE| = |a(\operatorname{Ric}+g)| \le C|U|$, the dangerous piece is:

$$
\boxed{2\chi C_{m+2} \star (aE) \le 2\chi C_{m+2} \cdot C|U|.} \tag{4.8}
$$

This is exactly the $\chi C_{m+2} U_0$ structure in A03 Step 40 equation (2.4).

**The $s < m$ terms in (4.6):** $(\nabla^{s+2}a)$ has top jet $C_{s+2}$, and
$\nabla^{m-s}(aE)$ has cutoff jets from $\nabla^{m-s}(aE) =
\sum_r (\nabla^r a)(\nabla^{m-s-r}E)$ with max jet $C_{m-s}$.
Neither factor alone reaches $C_{m+2}$; they are products of lower jets.

### 4.3 Other terms in $a\nabla^m(\partial_t T)$

The gradient-$a$ term: $a\nabla^m((\nabla a) \star (\nabla E))$.  By Leibniz,
the highest single jet from putting all $m$ derivatives on $\nabla a$ gives
$(\nabla^{m+1}a)(aE) \star (\nabla E)$, with top jet $C_{m+1}$.  No $C_{m+2}$.

The principal (Lichnerowicz) term: $a\nabla^m(a\Delta T) = a^2\nabla^m(\Delta T)
+ \cdots$.  The Laplacian involves two derivatives of $T$ but no derivatives
of $a$, so derivatives of $a$ enter only through the outer Leibniz. The
highest jet from $(\nabla^m(a^2))\Delta T$ is $4\chi^3 C_m$. No $C_{m+2}$.

Quadratic reaction: $a\nabla^m(a \mathcal{Q}(T))$.  Contains $a^2$ times
curvature products; $\nabla^m(a^2)$ has top jet $4\chi^3 C_m$.  No $C_{m+2}$.

Normalization/G-variation: $a\nabla^m(\mathcal{N}(a,T))$.  $\mathcal{N}$
involves $a \cdot T$ products; same analysis gives max jet $C_m$.  No $C_{m+2}$.

### 4.4 Commutator term $[\partial_t, \nabla^m]U$

The standard commutator expansion (Hamilton):

$$
[\partial_t, \nabla^m]U = \sum_{k=0}^{m-1}\sum_{l=0}^{k}\binom{k}{l}
(\nabla^l(\partial_t\Gamma)) \star (\nabla^{m-1-l}U). \tag{4.9}
$$

**Cutoff content of $\nabla^l(\partial_t\Gamma)$:**

$$
\partial_t\Gamma = \frac{1}{2}g^{-1}\nabla h = -g^{-1}\nabla(aE)
= -g^{-1}[(\nabla a)E + a\nabla E]. \tag{4.10}
$$

The maximum single jet in $\partial_t\Gamma$ is $C_1$ (from $\nabla a$).
After $l$ derivatives:

$$
\nabla^l(\partial_t\Gamma) \sim \nabla^{l+1}(aE) + \text{commutator corrections},
$$

hence max single jet $C_{l+1}$ (from $(\nabla^{l+1}a)E$).

**Cutoff content of $\nabla^{m-1-l}U$:**

$$
\nabla^{m-1-l}U = \sum_{r=0}^{m-1-l}\binom{m-1-l}{r}
(\nabla^r a)T_{m-1-l-r},
$$

hence max single jet $C_{m-1-l}$ (from $r = m-1-l$).

**Combined:** The maximum single jet from the commutator over all
$0 \le l \le k \le m-1$ is:

$$
\max_{0 \le l \le m-1} \max(l+1, m-1-l) = m \quad\text{(at } l = m-1\text{)}.
\tag{4.11}
$$

**Conclusion:** The commutator produces at most $C_m$-level jets.
No $C_{m+2}$ or $C_{m+1}$ from this source.

---

## 5. Main result: cutoff-jet provenance theorem

> **TTCS Step 43 correction (incorporated).**  In the parabolic form
> $(\partial_t - a\Delta)U_m = \cdots$, extracting $a\Delta U$ from
> $a^2\Delta T$ produces an additional term $-(\Delta a)U$ whose $m$-th
> derivative also contains $C_{m+2}$ — but again with the $\chi$ weight.
> The correct statement has TWO $C_{m+2}$ sources in the parabolic form,
> both carrying $\chi$.

**Parabolic form derivation.**  From $a\Delta(aT) = a^2\Delta T + a(\Delta a)T
+ 2a\nabla_p a\nabla^p T$:

$$
(\partial_t - a\Delta)U = a\partial_t T - a\Delta U
= -(\Delta a)U - 2\nabla a \cdot \nabla U + 4|d\chi|^2 U
+ (\nabla^2 a) \star (aE) + \text{lower}. \tag{5.0}
$$

The $-(\Delta a)U$ term, after $m$ derivatives:

$$
-\nabla^m((\Delta a)U) \ni -(\nabla^m\Delta a)U_0
= -(2\chi\operatorname{tr}(C_{m+2}) + \text{lower products})\cdot U. \tag{5.0a}
$$

This is a second $C_{m+2}$ source, also carrying $\chi$.

**Proposition (H-WU resolution).**  In the parabolic evolution
$(\partial_t - a\Delta)U_m = \text{RHS}_m$ for the weighted shifted curvature
$U_m = \nabla^m(\chi^2(\operatorname{Rm}+G))$ under $\partial_t g =
-2\chi^2(\operatorname{Ric}+g)$:

(a) **All** single cutoff jets $C_{m+2} = \nabla^{m+2}\chi$ in $\text{RHS}_m$
carry explicit $\chi$ and have coefficients that are algebraic contractions
of $U$, i.e., the form $\chi C_{m+2} \star \mathcal{A}(U)$ with
$|\mathcal{A}(U)| \le C_n|U|$.

(b) There are exactly two tensor-level sources of $C_{m+2}$:
- the Hessian-$a$ contraction: $(\nabla^{m+2}a) \star (aE) = 2\chi C_{m+2}
  \star (aE) + \text{lower products}$;
- the extracted Laplacian term: $-(\nabla^m\Delta a)U = -2\chi
  \operatorname{tr}(C_{m+2})U + \text{lower products}$.

Both have top jet $2\chi C_{m+2} \star \mathcal{A}(U)$ by identity (1.2).

(c) All other terms in $\text{RHS}_m$ contribute single cutoff jets of
order at most $m+1$:
- outer Leibniz ($j \ge 1$ in (4.2)): max jet $m+1$ (at $j = 1$);
- commutator: max jet $m$ (§4.4);
- gradient-$a$ drift: max jet $m+1$;
- $4|d\chi|^2 U$: max jet $m$ after $m$ derivatives;
- reaction, normalization, $G$: max jet $m$ (§4.3).

(d) **No bare $C_{m+2} \star \mathcal{A}(U)$ term (without $\chi$) exists.**

*Proof.*  The Hessian-$a$ source is proved in §4.2 via the factorization
$a(\nabla^2 a) \star E = (\nabla^2 a) \star (aE)$ and identity (1.2).  The
Laplacian source is proved by (5.0a) and identity (1.2) applied to
$\Delta a = \operatorname{tr}(\nabla^2 a)$.  The commutator bound is (4.11).
Curvature-commutator corrections from reordering covariant derivatives
satisfy $\operatorname{Rm} \star \nabla^{r'} a$ with $r' \le m$ (TTCS §6),
hence max jet $C_m$.  The absence of bare $C_{m+2}$ is verified by exhaustive
source tracing in §§4.1–4.4 and (5.0). $\square$

---

## 6. Matching with A03's corrected coupled energy mechanism

A03 Step 45 is the operative form of the staggered estimate.  In the parabolic
form there are two $C_{m+2}$ sources: the Hessian coefficient term and the
extracted $-(\Delta a)U$ term.  Proposition 5 shows that both are of the
common form
\[
  \chi C_{m+2}*\mathcal A(U_0),\qquad |\mathcal A(U_0)|\le C|U_0|.
\]

For the energy step set
\[
  V=U_m,
  \qquad Z=C_{m+1}=\nabla^{m+1}\chi,
  \qquad P(V)=|V|^{p-2}V.
\]
The cutoff-jet equation has current term $U_m*C_1$, so $Z$ is the current
partner of $V$, not data from an earlier layer.  The top source gives
\[
I_{\rm top}=\int \chi C_{m+2}*U_0*P(V).
\tag{6.1}
\]
Integrating once off $C_{m+2}=\nabla C_{m+1}$ yields
\[
C_1*Z*U_0*P(V),\qquad
\chi Z*U_1*P(V),\qquad
\chi Z*U_0*\nabla P(V).
\tag{6.2}
\]
The final term is absorbed by the weighted dissipation:
\[
\left|\int\chi ZU_0|V|^{p-2}\nabla V\right|
\le \varepsilon\int\chi^2|\nabla V|^2|V|^{p-2}
+C_{p,\varepsilon}K^2\int |Z|^2|V|^{p-2}.
\tag{6.3}
\]
The residual closes in the same exponent:
\[
\int |Z|^2|V|^{p-2}
\le {2\over p}\|Z\|_p^p+{p-2\over p}\|V\|_p^p.
\tag{6.4}
\]
Thus no current-step $L^{2p}$ input for $C_{m+1}$ is required at the $U_m$
stage.

The middle term $\chi Z*U_1*P(V)$ is handled as in A03 Step 45.  For
$m\ge2$, write one ordered copy of $Z=C_{m+1}$ as $\nabla C_m$ and integrate
again.  The new terms have either already completed factors or signed-Hessian
form; at $m=2$ the term $\chi C_2*U_2*P(U_2)$ is treated by the same
Hessian integration-by-parts structure, and at $m=1$ the original
$\chi C_2*U_1*P(U_1)$ already has that form.

The corrected $(db*db)T$ family also contributes only same-pair terms.  Before
expanding $b=\chi^2+\varepsilon^2$, keep the allocation as
$B_{r+1}*B_{s+1}*T_t$.  Its current pieces are
\[
B_1*B_1*T_m
=4{\chi^2\over b}(C_1*C_1)*\left[U_m-\sum_{q=1}^mB_q*T_{m-q}\right]
\]
and
\[
B_{m+1}*B_1*T_0
=4{\chi^2\over b}C_{m+1}*C_1*U_0+\hbox{lower}.
\]
Their coefficients are bounded uniformly in the coefficient regularization.

Combining the $V$ equation with the $Z$ equation gives the current-pair
estimate
\[
{d\over dt}\bigl(\|U_m\|_p^p+\|C_{m+1}\|_p^p\bigr)
+c_{m,p}\int b|\nabla U_m|^2|U_m|^{p-2}
\le C_{m,p}\bigl(1+\|U_m\|_p^p+\|C_{m+1}\|_p^p\bigr).
\tag{6.5}
\]
Only after this pair is propagated is $T_m$ estimated, using finite higher
exponents of the just-completed pair where needed.  The order is
\[
T_0\longrightarrow (U_1,C_2)\longrightarrow T_1
\longrightarrow (U_2,C_3)\longrightarrow T_2\longrightarrow\cdots .
\]

---

## 7. Why the weight $\chi$ is essential

If the top cutoff source were a bare $C_{m+2} \star (aE)$ (without $\chi$),
Term (III) in the integration by parts would produce:

$$
\int |C_{m+1}||aE||U_m|^{p-2}|\nabla U_m|.
$$

To absorb $|\nabla U_m|$ into the dissipation $D_{m,p}^U = \int\chi^2
|\nabla U_m|^2|U_m|^{p-2}$, one would need $\varepsilon\chi^2|\nabla U_m|^2
\ge \varepsilon|\nabla U_m|^2$, which fails when $\chi \to 0$ in the
transition region.  This is the structural impossibility identified in
Step 42 §4.

The factor $\chi$ in $2\chi C_{m+2}$ is not a cosmetic improvement; it is
the **necessary** pairing factor for the weighted dissipation in the
degenerate-cutoff regime.

---

## 8. Status after the Step 44 current-pair correction

> **A03 Step 45 independent confirmation.** A03's coordinate-time tensor ledger
> (`step45_coordinate_tensor_ledger_and_regularized_closure.md`) independently
> derives the same weight structure using $b = \chi^2 + \varepsilon^2$ and
> coordinate $\partial_t$.  The critical family (U3) has $B_1*B_1*T_m =
> 4(\chi^2/b)(C_1*C_1)*[U_m - \text{lower}]$ with bounded coefficient, and
> the top cutoff term is $2\chi C_{m+2}*U_0$.  Two independent TTCS verifiers
> found the staggered induction closes uniformly in $\varepsilon$.  110/110
> algebraic checks pass.

The corrected Proposition in §5 establishes the complete tensor-level
cutoff-jet provenance:

- **All** $C_{m+2}$ terms in the parabolic form $\text{RHS}_m$ carry explicit
  $\chi$ with coefficients that are algebraic contractions of $U$.
- There are exactly two $C_{m+2}$ sources: the Hessian-$a$ contraction and the
  extracted Laplacian term.  Both have the form $\chi C_{m+2}*\mathcal{A}(U)$.
- All other terms have single-jet order $\le m+1$.
- No bare $C_{m+2}$ term exists.
- The $\chi$ weight is essential for pairing with weighted dissipation (§7).

Combined with A03 Step 45 (coefficient-regularized coordinate ledger),
A03 Step 44 (zero-order $T$ seed), and A03 Step 40 (staggered $(U_m, C_{m+1})$
induction), the extension statement is:

**Under $\sup|U| \le K$, all derivatives $\nabla^m U$, $\nabla^m T$, and
$\nabla^{m+1}\chi$ are in $L^p$ for every finite $p$ and every $m$.  Hence
the solution extends smoothly past any finite $T_*$ where $|U|$ remains
bounded.**

This supplies H-WU in the corrected current-pair form.  Together with A03 Step
45's coefficient-regularized existence/restart (§6 of that note), the per-datum
flow platform is usable for the restricted negative route.  The simultaneous
support, first-exit, global $Q$, and terminal chain is reviewed in
`step44_preceptor_reading_first_exit_terminal_chain.md`.

---

## 9. Evidence and companion files

- Step 42 repair and weight comparison: `step42_uniform_gap_weight_terminal_repairs.md`
- Step 35 Hessian-$a$ tensor contractions: `step35_tensor_variation_and_hessian_a.md`
- A03 Step 40 staggered induction: `Sessions/S0910A03/workspace/notes/step40_staggered_all_order_continuation_candidate.md`
- A03 Step 44 zero-order $T$ seed: `Sessions/S0910A03/workspace/notes/step44_zero_order_T_seed_repair.md`
- A03 Step 43 general-order $T$ estimate: `Sessions/S0910A03/workspace/notes/step43_general_order_unweighted_T_estimate.md`
- A03 Step 44 Yang start/restart: `Sessions/S0910A03/workspace/notes/step44_normalized_yang_tame_start_restart.md`
- Verification script: `workspace/scripts/step43_weighted_evolution_verify.py`

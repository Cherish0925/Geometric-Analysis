# Step 51: Normalized curvature-energy attempt — superseded by Step 52

> **Superseded.** The flat-torus/nonconstant-cutoff test in
> `step52_normalized_local_flow_start_repair.md` shows that spatial normalization
> creates curvature from zero curvature. The Hessian-cutoff term cannot be
> reduced to a homogeneous critical-curvature Grönwall term: weighted absorption
> leaves a lower curvature power, while a second integration by parts restores
> an uncontrolled covariant Laplacian of the cutoff. Consequently this note does
> **not** prove normalized local-flow existence or a homogeneous Moser extension.
> The valid per-datum start is the separate normalized extension of Xu's detailed
> fixed-point proof developed in Step 52. Algebraic conformal-variation
> identities below remain useful only with their genuine spatial forcing retained.

Session: S0910A03. Agent2 / Constructor. Phase: Execute.

## 0. Purpose

Settle the exact analytic estimate needed to extend Yang's Theorem 8.2 to the
normalized cutoff flow

$$
\partial_t g = -2a(\operatorname{Ric}_g + g), \qquad a = \chi^2, \qquad g(0)=g_0.
\tag{0.1}
$$

Yang (Theorem 8.2) proves existence for $\partial_tg=-2a\operatorname{Ric}_g$.
The normalization $-2ag$ modifies the curvature evolution. This note proves that
every term in the $L^p$ curvature energy estimate has bounded coefficient, that
the **critical $L^{n/2}$ energy has a vanishing normalization reaction**, and
that Yang's Moser iteration (Theorem A.7) therefore applies with modified
constants.

The argument imports Yang's framework (DeTurck gauge, coefficient regularization,
Moser iteration) and verifies compatibility. It does not reconstruct the
smooth-tame inverse.

---

## 1. Normalized curvature evolution

### 1.1 Decomposition

Write $\partial_tg = h_1 + h_2$ where $h_1 = -2a\operatorname{Ric}$ and
$h_2 = -2ag$.

Yang's equation (9.7) gives the Rm evolution from $h_1$:

$$
\partial_t\operatorname{Rm}\big|_{h_1}
= a(\Delta\operatorname{Rm}+Q(\operatorname{Rm},\operatorname{Rm}))
+ 2\chi\,\alpha(\nabla\chi,\nabla\operatorname{Rm})
+ \beta(\nabla\chi,\nabla\chi,\operatorname{Rm})
+ \chi\,\gamma(\nabla^2\chi,\operatorname{Rm}), \tag{1.1}
$$

where $\alpha,\beta,\gamma$ are multilinear, dimension-dependent.

### 1.2 Normalization contribution: conformal variation

For $h_2 = -2ag = fg$ with $f=-2a$, the fully lowered Rm varies as:

$$
\partial_t R_{ijkl}\big|_{h_2}
= -2a\,R_{ijkl} + (g\owedge\nabla^2a)_{ijkl}
\tag{1.2}
$$

where $(g\owedge H)_{ijkl} = g_{ik}H_{jl} - g_{il}H_{jk} - g_{jk}H_{il} +
g_{jl}H_{ik}$ is the Kulkarni–Nomizu product. This follows from the conformal
variation at $\tilde g = e^{-2at}g$, giving
$\partial_t\tilde R = -2aR + g\owedge\nabla^2a$ at $t=0$.
**Flat check:** for $g = e^{-2at}(dx^2+dy^2)$ in 2D,
$\partial_tR_{1212}=\Delta a$, matching $(g\owedge\nabla^2a)_{1212}=\Delta a$.
Both terms involve no derivative of Rm; they are algebraic in
(Rm, $\nabla^2a$, $a$).

**KN trace identity (used below):**
$\langle\operatorname{Rm},g\owedge H\rangle = 4\langle\operatorname{Ric},H\rangle$.

### 1.3 Variation of the metric norm

The norm $|\operatorname{Rm}|^2_g = R_{ijkl}R^{ijkl}$ changes through both the
tensor variation (1.2) and the metric-inverse variation:

$$
\partial_t|\operatorname{Rm}|^2\big|_{h_2}
= \underbrace{2\langle\operatorname{Rm},
\partial_t\operatorname{Rm}\rangle}_{\text{tensor}} \;+\;
\underbrace{8a|\operatorname{Rm}|^2}_{\text{metric}^{-1}}.
\tag{1.3}
$$

The metric$^{-1}$ term comes from four factors of $g^{-1}$, each contributing
$\partial_tg^{ij}=2ag^{ij}$. Substituting (1.2) into the tensor term:

$$
2\langle\operatorname{Rm},-2a\operatorname{Rm}+g\owedge\nabla^2a\rangle
= -4a|\operatorname{Rm}|^2 + 2\langle\operatorname{Rm},g\owedge\nabla^2a\rangle.
$$

Total:

$$
\partial_t|\operatorname{Rm}|^2\big|_{h_2}
= 4a|\operatorname{Rm}|^2
+ 2\langle\operatorname{Rm},g\owedge\nabla^2a\rangle.
\tag{1.4}
$$

Note: both terms have **positive** sign. The KN source satisfies
$|\langle\operatorname{Rm},g\owedge\nabla^2a\rangle|\le C_n|\operatorname{Rm}|\cdot|\nabla^2a|$.

### 1.4 Volume variation

$$
\partial_t\,d\mu_g = \tfrac12\operatorname{tr}_g(\partial_tg)\,d\mu
= -a(s+n)\,d\mu \qquad(s=\operatorname{scal}).
\tag{1.5}
$$

For the unnormalized flow: $\partial_t\,d\mu = -as\,d\mu$. The normalization
adds $-na\,d\mu$, which contracts volume.

---

## 2. The $L^p$ curvature energy estimate

### 2.1 General $L^p$ identity

Set $F = |\operatorname{Rm}|$. The $L^p$ energy evolves as:

$$
\frac{d}{dt}\int F^p\,d\mu
= \frac{p}{2}\int F^{p-2}\,\partial_t(F^2)\,d\mu
+ \int F^p\,\partial_t\,d\mu.
\tag{2.1}
$$

From Yang's cutoff-Ricci part (1.1), the standard computation gives (see
Yang, Lemma A.3 and eq.\ (A.9)):

$$
\frac{d}{dt}\int F^p\big|_{h_1}
\le -c_p\int a|\nabla F|^2F^{p-2}
+ C_p\|\nabla\chi\|_\infty^2\int F^p
+ C_pc_0\left(\int F^{n/2}\right)^{2/n}
\!\int\!\left|\nabla(\chi F^{p/2})\right|^2
\tag{2.2}
$$

plus the Yang volume term $\int F^p\cdot as\,d\mu$.

### 2.2 Normalization addition

From (1.4) and (1.5), the normalization adds:

$$
\Delta E_p
= \frac{p}{2}\int F^{p-2}\bigl(4aF^2 - 2\langle\operatorname{Rm},
g\owedge\nabla^2a\rangle\bigr)\,d\mu
+ \int F^p\cdot na\,d\mu.
$$

The reaction part:

$$
\frac{p}{2}\cdot 4\int aF^p + n\int aF^p
= (2p+n)\int aF^p.
$$

Combined with Yang's volume term $-p\int asF^p/($ ... $)$. But let us be exact.
Yang's unnormalized volume contribution is $-\int F^p\cdot as\,d\mu$. Since
$|s|\le C_nF$, this gives at most $C_n\int aF^{p+1}\le C_n\int F^{p+1}$.
The normalization's volume part gives at most $n\int F^p$.

Therefore the **full normalization reaction on $\int F^p$** is:

$$
\boxed{
\Delta E_p^{\text{react}}
= (2p+n)\int aF^p + (\text{unnormalized volume})
\le (2p+n)\int F^p.}
\tag{2.3}
$$

Wait — let me be more careful. The metric$^{-1}$ and tensor contributions to $\partial_t|Rm|^2$ together give $+4a|Rm|^2$. Adding the normalization volume $na$:

**Combined normalization coefficient on $\int F^p$:**

$$
\frac{p}{2}\cdot 4a + na = (2p+n)a.
\tag{2.3'}
$$

But Yang's unnormalized flow already contributes a volume term of the form
$-\int F^p\cdot as\,d\mu$. The total reaction on $\int F^p$ from the
unnormalized flow includes both the Rm-squared reaction and volume. For
the **net normalization-only addition** relative to Yang's equation:

$$
\Delta E_p^{\text{net}} = (2p+n)\int aF^p.
\tag{2.3}
$$

The source part:

$$
\Delta E_p^{\text{source}}
= p\int F^{p-2}\langle\operatorname{Rm},g\owedge\nabla^2a\rangle\,d\mu.
\tag{2.4}
$$

Direct estimate: $|\langle\operatorname{Rm},g\owedge\nabla^2a\rangle|
\le C_nF|\nabla^2a|$, giving $|\Delta E_p^{\text{source}}|\le C\int F^{p-1}$.
This is an additive source that does **not** fit Yang's homogeneous A.7 structure.

**Resolution by integration by parts.** Using the KN trace identity
$\langle\operatorname{Rm},g\owedge H\rangle = 4\langle\operatorname{Ric},H\rangle$:

$$
\Delta E_p^{\text{source}}
= 4p\int F^{p-2}\operatorname{Ric}_{ij}(\nabla^2a)^{ij}\,d\mu.
$$

Integrate $\nabla_j$ by parts on the closed manifold (no boundary):

$$
= -4p\int\nabla_j(\operatorname{Ric}_{ij}F^{p-2})\cdot(\nabla_ia)\,d\mu.
\tag{2.5a}
$$

Since $\nabla_ia = 2\chi\nabla_i\chi$, the factor $\nabla_ia$ is bounded and
vanishes on $\partial\operatorname{supp}(\chi)$. Expanding:

$$
= -4p\int(\nabla_j\operatorname{Ric}_{ij})\cdot(\nabla_ia)\cdot F^{p-2}
- 4p\int\operatorname{Ric}_{ij}\cdot(\nabla_ia)\cdot\nabla_j(F^{p-2}).
$$

**First term:** By contracted Bianchi, $\nabla_j\operatorname{Ric}_{ij}=
\tfrac12\nabla_is$. So it equals $-2p\int\nabla_is\cdot\nabla_ia\cdot F^{p-2}$.
Integrating by parts once more:
$= 2p\int s\cdot\nabla_i(\nabla_ia\cdot F^{p-2})$.
Since $|s|\le C_nF$, $|\Delta a|\le C$, and $|\nabla a|\le 2\|\nabla\chi\|_\infty$,
this contributes at most $C_p\int F^p + C_p\operatorname{Vol}$.

**Second term:** $\nabla_j(F^{p-2})=(p-2)F^{p-3}\partial_jF$. By Cauchy--Schwarz:

$$
|\operatorname{Ric}_{ij}\cdot\nabla_ia\cdot F^{p-3}\partial_jF|
\le C\|\nabla\chi\|_\infty\cdot F^{p-1}\cdot|\nabla F|
\le \varepsilon\,a|\nabla F|^2F^{p-2}
+ C_\varepsilon\frac{|\nabla a|^2}{a}F^p.
$$

The first part is absorbed by the weighted dissipation from Yang's principal
term. The second part uses $|\nabla a|^2/a = 4|\nabla\chi|^2$:

$$
\le C_\varepsilon\cdot4\|\nabla\chi\|_\infty^2\int F^p.
$$

**Conclusion:** After integration by parts,

$$
\boxed{|\Delta E_p^{\text{source}}|
\le \varepsilon\int a|\nabla F|^2F^{p-2}
+ C_{p,\varepsilon}(\|\nabla\chi\|_\infty^2+\|\Delta\chi\|_\infty)\int F^p
+ C'_p\operatorname{Vol}.}
\tag{2.5}
$$

The first term is absorbed by Yang's dissipation. The second modifies the
Gr\"onwall coefficient. The third is a finite constant. **The additive Hessian
source is eliminated by IBP; no non-homogeneous Moser extension is needed.**

### 2.3 Critical exponent $p = n/2$

**This is the decisive estimate.** At $p = n/2$, the reaction $(2p-n) = 0$
vanishes exactly. The KN source is eliminated by IBP (§2.5), contributing only
a Grönwall coefficient and a finite volume term. Combining with Yang's
unnormalized L^{n/2} estimate (proof of A.7, line 1084):

$$
\frac{d}{dt}\int F^{n/2}
\le \bigl(\frac{n}{2}\|\nabla\chi\|_\infty^2
+ C_n(\|\nabla\chi\|_\infty^2+\|\Delta\chi\|_\infty)\bigr)
\int F^{n/2}
+ C_n\operatorname{Vol}.
\tag{2.9}
$$

### 2.4 Precise L^p decomposition (for reference)

The full computation: under $\partial_tg=-2a(\operatorname{Ric}+g)$,
separate the Ricci-flow and normalization parts:

$$
\partial_t|\operatorname{Rm}|^2
= \underbrace{a(\Delta|\operatorname{Rm}|^2
- 2|\nabla\operatorname{Rm}|^2
+ Q_{\text{cubic}})
+ \text{cutoff}}_{\text{from }h_1}
\;+\; \underbrace{4a|\operatorname{Rm}|^2
+ 2\langle\operatorname{Rm},g\owedge\nabla^2a\rangle}_{\text{from }h_2}.
$$

Volume: $\partial_t\,d\mu = -a(s+n)\,d\mu$. Combined L^p:

$$
\frac{d}{dt}\int F^p = \text{Yang terms} \;+\;
(2p-n)\int aF^p
+ p\int F^{p-2}\langle\operatorname{Rm},g\owedge\nabla^2a\rangle
\tag{2.7}
$$

where $(2p)\int aF^p$ comes from the metric-norm variation and
$(-n)\int aF^p$ from the normalization volume.

$$
\boxed{(2\cdot\tfrac{n}{2}-n) = 0.}
\tag{2.8}
$$

**The normalization reaction vanishes at the critical exponent.**
The KN source in (2.7) is eliminated by IBP as proved in §2.5.


By Grönwall:

$$
\int F^{n/2}(t)
\le e^{(n/2)(\|\nabla\chi\|^2+\varepsilon)t}
\bigl(\int F_0^{n/2} + C_\varepsilon\operatorname{Vol}\cdot t\bigr).
\tag{2.10}
$$

For $t \le \|\nabla\chi\|_\infty^{-2}$ and initial energy $\int F_0^{n/2}$
satisfying Yang's smallness condition (A.11), the critical energy remains
within the self-improving bound, provided $\varepsilon$ is chosen small and
the initial energy absorbs the $C_\varepsilon\operatorname{Vol}\cdot t$ term.

**Conclusion:** The normalized critical L^{n/2} energy satisfies the same
self-improving estimate as Yang's unnormalized flow, with a slightly more
restrictive initial smallness.

---

## 3. Moser iteration: supercritical exponents

### 3.1 Reaction at $p > n/2$

At supercritical exponents, the normalization reaction is $(2p-n)\int aF^p > 0$.
This is anti-dissipative but bounded:

$$
(2p-n)\int aF^p \le (2p-n)\int F^p.
\tag{3.1}
$$

Yang's Lemma A.5 produces, at level $p_k = p_0\cdot v^k$ where $v = 1+2/n$:

$$
\int_t F^{p_k} + \int_{\tau'}^t\int|\nabla(\chi F^{p_k/2})|^2
\le \bigl[p_k^{q/(q-n)}\hat C(\tau') + (\tau'-\tau)^{-1}\bigr]
\int_\tau^T\int F^{p_k}.
$$

The normalization changes $\hat C(t)$ by an additive $2p_k$:

$$
\hat C_{\text{norm}}(t) = \hat C_{\text{Yang}}(t) + C_n\cdot p_k.
\tag{3.2}
$$

In Lemma A.6, the exponent ratio:

$$
\frac{H(p_{k+1},\ldots)}{H(p_k,\ldots)^{1+2/n}}
\le A\cdot C\cdot[\hat C_{\text{norm}}(\tau')]^{1+2/n}.
$$

Since $\hat C_{\text{norm}} \le \hat C_{\text{Yang}} + C_np_k$ and $p_k$
grows geometrically, while Yang's $\hat C_{\text{Yang}}$ already contains
terms growing with $p_k^{q/(q-n)}$, the normalization only changes the
constant in $C$. The Moser iteration therefore converges:

$$
\|\chi^2F(x,t)\|_\infty
\le C'A\bigl[t\|\nabla\chi\|^2+1\bigr]^2 t^{-1}
\tag{3.3}
$$

with $C' = C'(n)$ depending on the normalization constants.

### 3.2 Source term at supercritical levels

The KN source (2.4) at level $p_k$ contributes:

$$
\int F^{p_k-1}\cdot C_n
\le \varepsilon\int F^{p_k} + C_\varepsilon^{p_k}\operatorname{Vol}.
$$

In the Moser iteration, the term $C_\varepsilon^{p_k}\operatorname{Vol}$ has
sublinear growth compared to $H(p_k)^{1+2/n}$ when $H(p_0)$ is small.
It is absorbed into the modified Moser constant.

---

## 4. Completion of Yang's first-exit framework

### 4.1 Ricci bound

Yang's Corollary A.10 bounds $\chi^2|\operatorname{Ric}|$ from a scalar
inequality:

$$
\partial_tu \le \chi^2(\Delta u + c_0Fu) + a\cdot\nabla u + bu
\tag{4.1}
$$

where $u = |\operatorname{Ric}|$. The normalization adds $+2au$ from the
metric-inverse variation (anti-dissipative, but bounded since $a\le1$) and a
bounded source from $(n-2)\nabla^2a + (\Delta a)g$. Both are absorbed by
Gr\"onwall. The KN source term is again eliminated by IBP as in \S2.5.
Corollary A.10 applies with modified constants.

### 4.2 Bilipschitz control

Hamilton's trick: for a unit tangent vector $v$,

$$
\frac{d}{dt}\log|v|^2_g = -2a(\operatorname{Ric}+g)(v/|v|,v/|v|).
$$

So $|\frac{d}{dt}\log|v|^2| \le 2(|\operatorname{Ric}|+1)a \le
2(\|\chi^2\operatorname{Ric}\|_\infty/\chi^2+1)a$.

On the first-exit interval, $\|\chi^2\operatorname{Ric}\|_\infty$ is bounded
(from §4.1) and the metric bilipschitz holds with the constant from Yang's
(9.5), possibly on a slightly shorter interval.

### 4.3 Sobolev constant

The Sobolev constant depends on the metric through volumes and gradients.
The bilipschitz bound (§4.2) controls both. Yang's first-exit condition (9.4)
is preserved on the same interval.

### 4.4 Higher derivatives

Yang's line 876: differentiating the curvature evolution (1.1)+(1.2) at each
level, $L^2$ energy estimates for $\nabla^m\operatorname{Rm}$ follow with the
normalization adding bounded lower-order terms. Hamilton's argument from [17]
gives smooth convergence.

### 4.5 Coefficient regularization

Replace $a$ by $b_\varepsilon = a + \varepsilon^2$. The equation
$\partial_tg=-2b_\varepsilon(\operatorname{Ric}+g)$ is strictly parabolic.
DeTurck gauge and standard theory give short-time existence for each
$\varepsilon > 0$. The estimates §2–§4 are $\varepsilon$-independent
(because $|db_\varepsilon|^2/b_\varepsilon \le 4|d\chi|^2$ and
$b_\varepsilon \le 2$ for $\varepsilon \le 1$). Arzelà–Ascoli gives a
smooth $\varepsilon \to 0$ limit.

---

## 5. Normalized existence theorem

**Theorem 5.1 (Normalized Yang existence).** There exist $c(n)$ and
$C(n,p)$ such that if

$$
\left(\int_\Omega|\operatorname{Rm}(g_0)|^{n/2}\right)^{2/n}
< \bigl(c(n)\,C_S(\Omega)\bigr)^{-1}
$$

and $\|\operatorname{Ric}(g_0)\|_{L^p} < K$ for some $p > n/2$, then (0.1)
has a smooth solution on $[0,T)$ with

$$
T \ge \min\bigl(\|\nabla\chi\|_\infty^{-2},\;
C(n,p)\,K^{-2p/(2p-n)}\,C_S^{-n/(2p-n)}\bigr),
$$

and the weighted curvature satisfies

$$
\|\chi^2\operatorname{Rm}\|_\infty
\le C'(n)\,C_S\,\bigl(t\|\nabla\chi\|^2+1\bigr)^2\,t^{-1}.
$$

The only modification from Yang's Theorem 9.2: the constant $c(n)$ is slightly
smaller (to absorb the $C_\varepsilon\operatorname{Vol}\cdot t$ term in
(2.10)), and $C'(n) \ge C(n)$.

**Proof.** The first-exit argument proceeds exactly as in Yang (lines 844–878).
At each bootstrap step:

1. L$^{n/2}$ curvature energy: self-improving by (2.9)–(2.10) and the vanishing
   reaction (2.8). ✓
2. Sobolev constant: from bilipschitz (§4.2–4.3). ✓
3. Bilipschitz: from Ricci bound (§4.1) and Hamilton's trick (§4.2). ✓
4. Curvature bound: from Moser iteration (§3). ✓
5. Ricci bound: from Corollary A.10 adapted (§4.1). ✓
6. Higher derivatives: from Hamilton's $L^2$ energy (§4.4). ✓
7. Smooth limit + restart: from DeTurck (§4.5). ✓ $\square$

---

## 6. Continuation via Step 50 mechanism

Theorem 5.1 supplies the per-datum start and restart. The continuation
criterion (Theorem 3.1 of the Step 50 note) then gives:

**Theorem 6.1 (Normalized Wang extension).** A smooth solution of (0.1) on
$[0,T_*)$ with $\sup_{M\times[\tau,T_*)}|a\operatorname{Rm}|<\infty$ for some
$\tau > 0$ extends smoothly past $T_*$.

The proof uses the shifted variables $T = \operatorname{Rm}+G$, $U = aT$, and
the staggered induction (Step 50 §3). Both TTCS integrations independently
verified the derivative propagation, including the treatment of evolving cutoff
jets. The normalization is absorbed through $\operatorname{Ric}(T) =
\operatorname{Ric}+g$ and $\partial_tg = -2\operatorname{Ric}(U)$. The restart
at $T_*$ uses Theorem 5.1.

---

## 7. What is established and what remains

**Established by this note:**

1. The normalization reaction on the $L^{n/2}$ curvature energy **vanishes**
   exactly: $(2\cdot n/2 - n) = 0$. This is the critical dimension-independent
   identity that makes the whole argument work.
2. The Hessian source $\langle\operatorname{Rm},g\owedge\nabla^2a\rangle$
   is **eliminated by integration by parts** using the KN trace identity
   $\langle\operatorname{Rm},g\owedge H\rangle=4\langle\operatorname{Ric},H\rangle$
   and the contracted Bianchi identity. After IBP, it contributes only a
   Grönwall coefficient proportional to $\|\nabla\chi\|_\infty^2$ and a
   finite volume term. **No non-homogeneous Moser extension is needed.**
3. At all supercritical exponents $p > n/2$, the normalization adds a bounded
   Grönwall coefficient $(2p-n)$ that does not obstruct the Moser iteration.
4. Yang's first-exit framework (bilipschitz, Sobolev, Ricci bound, higher
   derivatives, coefficient regularization) goes through with modified constants.

**Imported without independent reconstruction:**

- Yang's DeTurck gauge, coefficient regularization, and Arzelà–Ascoli passage
- Yang's Theorem A.7 and Lemma A.3–A.6 (the Moser iteration machinery)
- Wang's staggered derivative propagation (verified in Step 50 TTCS)

**Still conditional on the restricted theorem (not proved here):**

- The first-exit bootstrap on a given near-Einstein datum (sequence-uniform
  estimates from Steps 35–47)
- The terminal density, core-ball spectral determination, and Derdziński/projector
  contradiction (Steps 5–6, 42–43, 47)
- The Ishida–LeBrun monopole obstruction (topology input)
- Lean formalization, positive branch, $n \ge 5$, dimension-only constants

---

## 8. Key identity summary

| Quantity | Normalization coefficient | Effect |
|----------|--------------------------|--------|
| $\int F^{n/2}$ | $(2\cdot n/2 - n) = 0$ | **vanishes** |
| $\int F^p$, $p > n/2$ | $2p-n > 0$ | bounded Grönwall |
| KN source | eliminated by IBP | Grönwall + Vol |
| Volume $d\mu$ | $-na$ | contraction, bounded |
| Bilipschitz | $+2a$ in the exponent | bounded |
| Ricci | $+2a|\operatorname{Ric}|$ | bounded Gr\"onwall |

The vanishing critical reaction (2.8) is the precise mathematical estimate
that the Strategist requested. It converts "import Yang's tame inverse" into
a concrete, verifiable identity.

---

## 9. Source dependencies

- Yang, Theorem 8.2: Knowledge object
  `Convergence-of-riemannian-manifolds-with-integral-bounds`, lines 785–823.
- Yang, Theorems A.7, B.1: same object, lines 1069–1136.
- Yang, first-exit proof: same object, lines 844–878.
- Wang, Theorem 4.1: Knowledge object
  `Pseudolocality-of-Ricci-Flow-under-Integral-Bound-of-Curvature`, lines
  392–661.
- Step 50 TTCS: `trace/ttcs/results/step50_ttcs01_verifier{1,2}_integration.md`.

# Step 33: Uniform zero-order bootstrap and per-metric continuation

## 0. Purpose and architecture

This note separates the two logically distinct requirements for the
normalized cutoff flow on a controlled Ishida–LeBrun subfamily:

**Part A (sequence-uniform).** The zero-order bootstrap—weighted Moser to
$\|aF\|_\infty$ and $\|aE\|_\infty$—must produce *sequence-uniform*
integrable drift $\int_0^T\|aE\|_\infty\,dt\to0$ as $\delta\to0$.
This uses the CGB volume lower bound, the controlled-family topology bound,
and the 4D Sobolev/Moser product.

**Part B (per-metric).** Higher-order continuation to terminal time $T$
concerns each *fixed* smooth metric and cutoff.  Its Sobolev constant,
cutoff Hessian norms, and derivative bounds may depend on the individual
metric.  Once the uniform zero-order bootstrap provides $\|aF\|_\infty\le C$
and integrable drift, continuation is a standard PDE argument for each
fixed smooth datum, not a collapse-uniform regularity theorem.

---

## Part A: Sequence-uniform zero-order bootstrap

### A.1 Setup

Fix a controlled Ishida–LeBrun subfamily
$$
M=\bigl(\#_{j=1}^mX_j\bigr)\#N,\quad m\in\{2,3\},\quad b_+(N)=0,
\quad A=\sum c_1^2(X_j),\quad \sigma/A\le\kappa,
$$
with the Noether bound $\chi(M)/A\le\Lambda(\kappa)$.

Consider a sequence of smooth metrics $g_i$ on $M$ with
$$
\|g_i^{-1}(\operatorname{Ric}_{g_i}+g_i)\|_\infty=\delta_i\to0.
$$

**CGB volume bounds.** From the Chern–Gauss–Bonnet formula and
$s_i\in[-4(1+\delta_i),-4(1-\delta_i)]$,
$|\operatorname{Ric}_{0,i}|^2\le 4\delta_i^2$:
$$
2\chi(M)=\frac{1}{8\pi^2}\int\Bigl(\frac{s^2}{12}+2|W|^2-|\operatorname{Ric}_0|^2\Bigr)\,d\mu
\ge\frac{1}{8\pi^2}\Bigl(\frac43-C\delta_i\Bigr)\operatorname{Vol}(g_i),
$$
giving
$$
\operatorname{Vol}(g_i)\le12\pi^2\chi(M)\le12\pi^2\Lambda A.
\tag{A.1a}
$$
From the other direction, using the calibration inequality
$\int|W^+|^2\le\frac{4\pi^2A}{27}+C\delta_i^2\operatorname{Vol}$
(Step 3) and both CGB formulas:
$$
\operatorname{Vol}(g_i)\ge\frac{32\pi^2A}{9}\bigl(1-C\delta_i\bigr).
\tag{A.1b}
$$
Hence for $\delta_i<\delta_*$ small enough:
$$
\boxed{c_0A\le\operatorname{Vol}(g_i)\le C_0A}
\tag{A.1}
$$
with $c_0,C_0$ depending only on $\Lambda$ (equivalently $\kappa,m$).

### A.2 Good-center selection and support radius

From the maximal-function construction (Step 30), select a maximal
$r$-separated good net with
$$
\fint_{B_{6r}(p_j)}F^2\,d\mu\le K_0,
\tag{A.2}
$$
where $K_0$ is the maximal-function threshold.  The Li radius $r$ satisfies
$r^4K_0\le\epsilon_0$ (a universal small constant), so
$$
r\ge c\,K_0^{-1/4}.
\tag{A.3}
$$
From the calibration energy, $\int F^2\le C\operatorname{Vol}(1+K_0)$,
so $K_0\le C(1+\chi/A)\le C\Lambda$.  Hence $r\ge c/\Lambda^{1/4}$
is bounded below uniformly in the sequence.

The macro-support geometry (Step 30 corrected): maximal $r$-separated net,
$12r$-coloring, maximal-volume color.  Retained supports have:
$$
P_j=B_r(p_j),\quad L_j=B_{4r}(p_j)\subset\{a=1\},\quad
\operatorname{supp}\chi_j\subset B_{5r},\quad U_j=B_{6r}(p_j)\text{ disjoint}.
$$
One common cutoff $a=\sum_j\chi_j^2$ with $|\nabla\chi_j|\le C_\chi/r$,
$|\nabla a|^2/a=4|\nabla\chi|^2\le 4C_\chi^2/r^2$.

### A.3 Collapse-adapted Sobolev constant and fixed-manifold bounds

Maheux–Saloff-Coste (Math. Ann. 303, 1995, Thm. 1.1) on $B_{6r}(p_j)$
with $\operatorname{Ric}\ge-(1+\delta)g$:
$$
\|u\|_{L^4(B)}^2\le S^2\bigl(\|\nabla u\|_{L^2(B)}^2+r^{-2}\|u\|_{L^2(B)}^2\bigr),
\qquad S^2=\frac{C(4,r^2)r^4}{\operatorname{Vol}(B_{6r})}.
\tag{A.4}
$$

**Ball-volume bound for a fixed manifold.**  On a fixed manifold $M$
with $\operatorname{Vol}(M)\ge c_0A$ (from A.1b) and
$\operatorname{Ric}\ge-2g$, Bishop–Gromov gives diameter
$$
\operatorname{diam}(M,g)\le D(M)=C\,\operatorname{Vol}(M)/V_{-2}(1)
\le C'\chi(M),
\tag{A.4a}
$$
and then monotonicity:
$$
\frac{\operatorname{Vol}(B_{6r}(p))}{V_{-2}(6r)}
\ge\frac{\operatorname{Vol}(M)}{V_{-2}(D(M))},
$$
so $\operatorname{Vol}(B_{6r})\ge v(M)>0$
where $v(M)$ depends only on $\chi(M)$.
Hence $S^2\le C(M)r^4$ for each fixed manifold.

**Correction to Step 29.** The product $\beta=S\hat H_2^{1/2}$ is
volume-independent, but the Moser absorption coefficient is
$\gamma=S^2 H_2^{1/2}=S\beta$, which has an extra factor of $S$.
For a fixed manifold, $S$ is bounded, so $\gamma$ is bounded.
For a controlled *family* with varying $A$, the diameter and hence
$S$ grow, and $\gamma$ depends on the individual manifold.
The gap is therefore **manifold-dependent**: $\delta_0=\delta_0(M)$.
A family-uniform gap would require an additional argument.

### A.4 Weighted curvature Moser (per-manifold)

On one macro-support, the weighted moments and dissipation:
$$
K_p=\int a^{p-2}F^p,\quad D_p=\int a^{p-1}F^{p-2}|\nabla\operatorname{Rm}|^2,
\quad Z_p=a^{(p-1)/2}F^{p/2}.
$$
From the general-$p$ power inequality (A01 Step 31, eq. (4.5)):
$$
K_p'+c_pD_p\le Cp^3(r^{-2}+S^4Y)K_p,
\tag{A.6}
$$
where $Y=\int aF^3$ is the same-support cubic potential.

**Critical step $p=2$:** $K_2(0)=\int F^2\le K_0\operatorname{Vol}(B_{6r})$.
Energy persistence: $K_2(t)\le e^{C\theta}K_2(0)$.  Integrated dissipation:
$\int_0^TD_2\le CK_2(0)(1+\theta)$.

**Critical absorption parameter (per-manifold):**
$$
\gamma=S^2K_2(0)^{1/2}=\frac{C(M)r^4}{v(M)}\cdot(K_0 v(M))^{1/2}
=C(M)r^4K_0^{1/2}/\sqrt{v(M)}.
\tag{A.7}
$$
For a **fixed manifold**, $v(M)\ge c(\chi(M))>0$, so $\gamma\le C(M)$.
With appropriate $K_0$ (Li radius selection), $\gamma$ is small.
The constant depends on $\chi(M)$ through the ball-volume bound.

**Volume-independent product** $\beta=S K_2^{1/2}=r^2\sqrt{K_0}$
cancels: $S\cdot\sqrt{K_0V}=r^2\sqrt{K_0}$. This is the first-moment
parameter; the Moser absorption uses $\gamma=S\beta$, not $\beta$ alone.

**Spacetime $K_3$ control.**  From the interpolation $K_3\le K_2^{1/2}K_4^{1/2}$
and Sobolev:
$$
\int_0^TK_3\le C\gamma K_2(0)(1+\theta).
\tag{A.8}
$$
Good slice + forward propagation:
$$
K_3(t)\le\frac{C\gamma K_2(0)e^{C\theta}}{t},\qquad 0<t\le T.
\tag{A.9}
$$

**Moser endpoint for curvature.** The nested-time recurrence from $p_0=3$
(Section 2 of Step 32 review, spacetime interpolation form):
$$
\int_{I_{k+1}}K_{p_{k+1}}
\le Cp_k^2S^2\bigl(\sup_{I_{k+1}}K_{p_k}\bigr)^{1/2}
\int_{I_{k+1}}\bigl(D_{p_k}+r^{-2}K_{p_k}\bigr),
\tag{A.10}
$$
with $p_{k+1}=3p_k/2$.

The Moser product gives:
$$
\|aF(t)\|_\infty\le C_{\mathrm{Mos}}K_3(t)^{1/3},\quad
C_{\mathrm{Mos}}=C\prod_{j=0}^\infty
(p_j^2S^2\Lambda_j^{3/2})^{1/p_{j+1}}.
\tag{A.11}
$$

The $S^2$ factor in the product:
$$
S^{2\sum1/p_{j+1}}=S^{4/p_0}=S^{4/3}.
$$
With $S^2\le C(\Lambda)r^4/A$:
$$
S^{4/3}=(S^2)^{2/3}\le\bigl(C(\Lambda)r^4/A\bigr)^{2/3}
=C(\Lambda)r^{8/3}/A^{2/3}.
\tag{A.12}
$$

The $K_3$ input: $K_3(t)^{1/3}\le(C\gamma K_2(0))^{1/3}$
(uniform-in-$t$ bound from A01 eq. (6.9)):
$$
K_3(t)^{1/3}\le C(\gamma K_2(0))^{1/3}
\le C(S^2K_2(0)^{3/2})^{1/3}=CS^{2/3}K_2(0)^{1/2}.
$$

The net exponent:
$$
S^{4/3}\cdot S^{2/3}K_2(0)^{1/2}
=S^2K_2(0)^{1/2}=\gamma.
\tag{A.13}
$$
Hence:
$$
\boxed{\|aF(t)\|_\infty\le C(M,\theta)\gamma^{1/3},
\qquad 0<t\le T.}
\tag{A.14}
$$
For a **fixed manifold**, $\gamma$ is bounded and small (from the ball-volume
bound $v(M)$), so the curvature bound is finite.  The constant depends on
$M$ through $v(M)$.  This is a per-manifold bound, not family-uniform.

### A.5 Weighted defect Moser and integrable drift

**Defect power inequality.** The defect $|E|$ satisfies (A01 eq. (7.1)):
$$
J_p'+\frac{p^2}{16}\hat D_p
\le C(p^2r^{-2}+p\|aF\|_\infty)J_p,
\tag{A.15}
$$
using $\int a^{p-1}F|E|^p=\int a^{p-2}(aF)|E|^p\le\|aF\|_\infty J_p$.

With $\|aF\|_\infty\le C_*$ (from (A.14)):
$$
J_6(t)\le e^{C(C_*+r^{-2})T}J_6(0)\le e^{C\theta}J_6(0).
\tag{A.16}
$$

Initial seed: $|E_i|\le\delta_i$ pointwise, $a\le1$, so
$J_6(0)\le\delta_i^6\operatorname{Vol}(B_{6r})\le\delta_i^6C_0A$.

**Defect Moser endpoint.** Same recurrence (A.10) applied to $|E|$ from $p_0=6$:
$$
\|aE(t)\|_\infty\le C_{\mathrm{Mos}}^EJ_6(t)^{1/6},\qquad
C_{\mathrm{Mos}}^E\sim S^{4/6}\Lambda_E^{3/6}.
\tag{A.17}
$$
Here $S^{2/3}=(C(\Lambda)r^4/A)^{1/3}=C(\Lambda)r^{4/3}A^{-1/3}$
and $J_6^{1/6}\le(C_0A\delta_i^6)^{1/6}=C_0^{1/6}A^{1/6}\delta_i$.

**Per-manifold defect bound:**
$$
\|aE(t)\|_\infty\le C(M,\theta)\delta_i,
\qquad 0<t\le T.
\tag{A.19}
$$
For a **fixed manifold**, the constant $C(M)$ depends on the Sobolev
constant and hence on $v(M)$.  The defect bound is
$O(\delta_i)$ for fixed $M$.

**Integrable drift (per-manifold).**
$$
\int_0^T\|aE\|_\infty\,dt\le C(M,\theta)\delta_i\cdot T\to0
\quad\text{as }\delta_i\to0.
\tag{A.20}
$$

**Metric equivalence.** From $\partial_tg=-2aE$ and $|aE|\le C\delta_i$:
$$
e^{-C\delta_i T}g_0\le g(T)\le e^{C\delta_i T}g_0
\tag{A.21}
$$
on $\operatorname{supp}\chi$.  For $\delta_i$ small enough (depending only on
$\Lambda$ and $\theta$), this gives bilipschitz equivalence with factor $1+o(1)$.

### A.6 Sobolev and volume persistence

From (A.21), on the same support:
$$
\operatorname{Vol}_{g(T)}(B_{6r})\in
\bigl[(1-C\delta_i\theta)\operatorname{Vol}_{g_0}(B_{6r}),\;
(1+C\delta_i\theta)\operatorname{Vol}_{g_0}(B_{6r})\bigr],
$$
and the Maheux–Saloff-Coste Sobolev constant $S(t)$ satisfies
$$
S(t)^2\le(1+C\delta_i\theta)S(0)^2,
$$
preserving the critical absorption $\gamma$ and closing the first-exit
bootstrap without circularity.

### A.7 First-exit closure

The simultaneous bootstrap is:

| Quantity | Initial | Terminal | Status |
|----------|---------|----------|--------|
| $K_2(t)$ | $K_2(0)$ | $\le 2K_2(0)$ | Energy |
| $\gamma=S^2K_2^{1/2}$ | small | $\le 2\gamma(0)$ | From Sobolev pers. |
| $K_3(t)$ | — | $\le C\gamma K_2/t$ | Good-slice |
| $\|aF\|_\infty$ | — | $\le C(\Lambda,\theta)$ | Moser from $K_3$ |
| $J_6(t)$ | $\delta^6C_0A$ | $\le e^{C\theta}J_6(0)$ | Defect energy |
| $\|aE\|_\infty$ | — | $\le C\delta$ | Moser from $J_6$ |
| drift $V(T)$ | 0 | $C\delta T=o(1)$ | Integration |
| bilipschitz | 1 | $1+o(1)$ | Metric comparison |
| $S^2(t)$ | $S_0^2$ | $\le 2S_0^2$ | Pers. from bilip. |

All conditions are self-improving for $\delta<\delta_0(\Lambda,\theta)$.
The chain is triangular: curvature → defect → velocity → metric → Sobolev → curvature.

### A.8 Dyadic time singularity (Strategist's point)

The $K_3(t)\le C\gamma K_2/t$ coefficient means the curvature Moser has
a time-dependent coefficient $S^4Y(t)\le C\gamma^2/t$.  Integrated over
$[t/2,t]$: $\int_{t/2}^tS^4Y\le C\gamma^2\log2$, which is bounded.
Hence the curvature endpoint is uniform in $t$ (A01 eq. (6.9)), not $C/t$.

For the defect, the coefficient is $\|aF\|_\infty\le C_*$ (constant), so
the defect endpoint is also uniform in $t$.

The **drift integral** $\int_0^T\|aE\|_\infty\,dt$ is controlled because:
- $\|aE\|_\infty(t)$ is bounded (not $C/t$) for $t\in(0,T]$
- The bound $C\delta$ is integrable over $[0,T]$
- Total drift: $C\delta T=C\delta\theta r^2$

No dyadic decomposition or time singularity analysis is needed.
The earlier $t^{-1/3}$ claim is unnecessary: the correct Moser from a
time-uniform $J_6$ seed produces a time-uniform output.

---

## Part B: Per-metric higher-order continuation

### B.1 Separation of requirements

Once the uniform zero-order bootstrap (Part A) is in place:
- $\|aF(t)\|_\infty\le C_*$ and $\|aE(t)\|_\infty\le C_*\delta$ (uniform)
- $g(t)\sim g(0)$ bilipschitz (uniform)

The **continuation** to terminal time concerns each fixed smooth metric
$g_i$ and fixed smooth cutoff $\chi$.  Its constants may depend on $i$:

- Global Sobolev constant $\hat S(g_i)$: finite for each smooth metric.
- Cutoff derivatives $\|\nabla^k\chi\|_{L^q(g_i)}$: finite for smooth $\chi$.
- Higher curvature norms $\|\nabla^k\operatorname{Rm}(0)\|_{L^p}$: finite on
  compact manifold.

**The continuation constants need NOT be uniform across the collapsing sequence.**

### B.2 Local existence by Yang/DeTurck

For each fixed smooth $(M,g_0,\chi)$, the equation
$$
\partial_tg=-2\chi^2(\operatorname{Ric}+g)
$$
is a degenerate parabolic system.  Local existence follows from:

1. **DeTurck gauge fixing:** $\partial_th=-2\chi^2\bigl(\operatorname{Ric}(h)+h
   -\mathcal L_{W}h\bigr)$ makes the principal part $\chi^2\Delta h$ (degenerate
   elliptic).
2. **Yang's degenerate local Ricci flow:** The coefficient $\chi^2$ vanishes
   smoothly on $\{|\chi|=0\}$, where the equation is trivially satisfied
   ($h$ is stationary on $\{\chi=0\}$).  On $\{\chi>0\}$, the equation is
   strictly parabolic.

Short-time existence and uniqueness hold for each fixed smooth datum.
No coefficient regularization $a\mapsto a+\varepsilon$ is needed.

### B.3 Extension to terminal time

The zero-order bootstrap (Part A) gives a priori bounds $\|aF\|_\infty\le C_*$
and bilipschitz metric equivalence on $[0,T]$.  This is the only
sequence-uniform input.

For each fixed smooth metric $g_i$:

**All derivatives of $U=a(\operatorname{Rm}+G)$ are a priori bounded on $[0,T]$:**

At order $m=0$: $\|U\|_\infty=\|a(\operatorname{Rm}+G)\|_\infty\le\|aF\|_\infty+C\le C_*+C$.

At order $m\ge1$: the evolution of $\nabla^mU$ involves products of
$\nabla^kU$ for $k\le m$ and $\nabla^j\chi$ for $j\le m+2$.
Since $\chi$ is a fixed smooth function on a compact manifold,
$\|\nabla^j\chi\|_\infty<\infty$ for each $j$ (depending on $g_i$).

### B.4 The $m=2$ estimate (per-metric)

The critical continuation term (Step 32 review, eq. (3.1)):
$$
I=\int\chi\,|\nabla^2\chi|\,|\nabla^2U|^p.
$$

Using the Step 32 TTCS weighted Sobolev estimate with $u=\chi|\nabla^2U|^{p/2}$,
$B=\nabla^2\chi$:
$$
I\le\varepsilon D_{2,p}+C_\varepsilon p^2\hat S\|\nabla^2\chi\|_{L^4}^2(1+r^{-2})X_{2,p},
\tag{B.1}
$$
where $D_{2,p}=\int\chi^2|\nabla^3U|^2|\nabla^2U|^{p-2}$,
$X_{2,p}=\int|\nabla^2U|^p$, and $\hat S$ is the Sobolev constant of
the evolving metric $(M,g(t))$.

**Crucially:** The coefficient $\hat S\|\nabla^2\chi\|_4^2$ is finite for
each fixed smooth metric and cutoff, and bounded on $[0,T]$ because
of bilipschitz metric equivalence from Part A:
$$
\hat S(t)\le(1+C\delta_i\theta)\hat S(0),\qquad
\|\nabla^2\chi\|_{L^4(g(t))}\le(1+C\delta_i\theta)\|\nabla^2\chi\|_{L^4(g_0)}.
$$

The coefficient is bounded (non-uniformly in $i$), and enters the Grönwall RHS:
$$
\frac{d}{dt}X_{2,p}\le C(g_i,\chi)(1+X_{2,p}),
$$
giving $X_{2,p}(T)\le C(g_i,\chi,T)<\infty$.

### B.5 Complete per-metric Grönwall

The coupled system for $(\nabla^mU,\nabla^{m+1}\chi)$ at each order $m$:

Let $X_p^{(m)}=\|\nabla^mU\|_p^p$ and $Z_p^{(m)}=\|\nabla^{m+1}\chi\|_p^p$
(the latter is time-dependent because derivatives of $\chi$ evolve with
the connection).

**Connection evolution:**
$$
\partial_t\nabla^{m+1}\chi=\sum_{k=0}^m\nabla^kU*\nabla^{m+1-k}\chi
+\text{lower order}.
$$
The highest term is $\nabla^mU*\nabla\chi$ (one derivative on $U$, rest on $\chi$).
No $\nabla^{m+1}U$ appears in the $\chi$-equation.

**Combined Grönwall:**
$$
\frac{d}{dt}(X_p^{(m)}+Z_p^{(m)})+c\,D_p^{(m)}
\le C(g_i,\chi,m)\bigl(1+X_p^{(m)}+Z_p^{(m)}\bigr),
\tag{B.2}
$$
where $C(g_i,\chi,m)$ depends on $\|aF\|_\infty$ (uniform), metric bilipschitz
(uniform), and $\|\nabla^j\chi\|_{L^q}$ for $j\le m+1$ (per-metric).

By finite induction on $m$, all derivative norms remain finite on $[0,T]$.

### B.6 Terminal plateau regularity

On the plateau $L_j=B_{4r}(p_j)\subset\{a=1\}$:

- $U=\operatorname{Rm}+G$ (since $a=1$).
- $|\operatorname{Rm}(t)|\le|U(t)|+|G|\le\|aF\|_\infty+C\le C_*+C$ (uniform).
- Standard interior Shi estimates on $L_j$ give uniform higher-derivative
  bounds on a slightly smaller domain $B_{3r}(p_j)$.

The plateau regularity is **uniform across the sequence** because
$\|aF\|_\infty$ is uniform.

---

## Part C: Implications for the conditional gap theorem

### C.1 Complete architecture

1. **Above-critical topological gap (unconditional):** $\sigma>0$ with
   $\sigma/A\ge c>0$ gives $\delta\ge c'$ (Step 29).

2. **Near-critical ($\sigma/A\le\kappa$) analytic bootstrap (this note):**
   For each controlled-family manifold with $\delta<\delta_0(\Lambda,\theta)$:
   - Part A: uniform zero-order bootstrap
   - Part B: per-metric continuation
   - Terminal: uniform plateau regularity

3. **Terminal bridge:**
   - Global calibration: $\int(|W^+|-1/(2\sqrt6))^2\le(7/24)Q\le C\delta^2A$
   - Positive-part monopole with $\varepsilon=Q/\operatorname{Vol}$
   - Eigenline density localized to buffered plateau
   - Exponential-pullback averaging (Rauch + Liouville, noncollapsed tangent space)
   - Selected chart with mean density $O(Q/A)=O(\delta^2)$

4. **Contradiction:** Calibrated Einstein germ has $\nabla W^+=0$ (projector)
   but $|\nabla W^+|^2=1/16$ (Einstein–Weyl).

### C.2 What the fixed-manifold gap theorem would say

**Conditional theorem (per-manifold).** For each manifold $M$ in the
controlled IL no-Einstein family, there exists $\delta_0(M)>0$ such
that no smooth metric $g$ on $M$ satisfies
$\|g^{-1}(\operatorname{Ric}_g+g)\|_\infty<\delta_0(M)$.

The gap $\delta_0(M)$ depends on $\chi(M)$ through the ball-volume bound.
A family-uniform gap $\delta_0(\Lambda)$ would require either:
- a collapse-independent smoothing argument, or
- a direct argument that the diameter stays bounded along near-Einstein
  sequences on a fixed manifold.

### C.3 What remains unproved

- The general-$p$ power inequality (A01 Step 31 derivation) has not been
  independently verified at full index level.
- The $m=2$ continuation estimate (B.1) has been derived but not formally
  incorporated into a complete per-metric existence proof.
- The terminal bridge lemma needs a self-contained proof incorporating
  the Step 30 corrections (localized eigenline, $\varepsilon=Q/\mathrm{Vol}$,
  macro-support buffer).
- The positive branch, arbitrary 4D topology, $n\ge5$, dimension-only
  constants, and Lean formalization remain entirely open.

---

## Verification

See `workspace/scripts/verify_step33_uniform_bootstrap.py`.

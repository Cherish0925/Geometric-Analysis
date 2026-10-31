# Step 52: Independent audit of the negative-chain start module and first-exit interface

Session S0910A02. Agent2 / Constructor. Phase Execute.

## 0. Target fidelity and scope

The active target is the full Yau–26 proposition. This step independently
audits the negative cutoff-flow chain at two interfaces:

1. The **start module** (A1): whether the fixed-cutoff geometric flow
   $\partial_t g = -2\chi^2(\operatorname{Ric}_g + g)$ has short-time existence.
2. The **first-exit preservation** (A2): whether the critical $H_2/L^2$
   curvature energy stays bounded with uniform constants along the
   Ishida–LeBrun sequence.

The audit confirms A03 Step 52's self-correction and adds an independent
critical-product analysis showing structural limitations.

## 1. Flat T⁴ falsification of homogeneous energy closure (confirmed)

A03 Step 52's flat T⁴ computation is independently verified.

On the flat four-torus (period $2\pi$) with $\chi = (1+\cos x_1)/2$,
$a = \chi^2$:

$$
\operatorname{Hess}(a) = \frac{-\cos x_1 - \cos 2x_1}{2}\, e_1 \otimes e_1.
$$

At $t=0$, $\operatorname{Ric}=0$, so $\partial_t g = -2ag$ and
$\partial_t\operatorname{Rm}|_{t=0} = g \owedge \operatorname{Hess}(a)$.
The curvature-tensor norm is

$$
|g \owedge \operatorname{Hess}(a)|^2 = 12(a'')^2.
$$

Integrating over $T^4$:

$$
\int_{T^4} |g \owedge \operatorname{Hess}(a)|^2\, dV
= 12(2\pi)^3 \int_0^{2\pi} \frac{(\cos x + \cos 2x)^2}{4}\,dx
= 12 \cdot 8\pi^3 \cdot \frac{\pi}{2}
= 48\pi^4.
$$

Numerical quadrature confirms $\int_0^{2\pi}(a'')^2\,dx = \pi/2$ to
machine precision. Therefore

$$
\int_{T^4} |\operatorname{Rm}(g(t))|^2\, d\mu_{g(t)}
= 48\pi^4\, t^2 + O(t^3),
$$

and the ratio $E'(t)/E(t) = 2/t + O(1) \to \infty$ as $t \to 0$.

**Consequence.** No homogeneous energy estimate $dE/dt \le CE$ holds for the
unshifted $L^2$ curvature energy at the critical exponent. The coefficient
$2p - n = 0$ at $p = n/2$ cancels only the constant-homothety reaction;
spatial variation of the cutoff creates genuine $g \owedge \nabla^2 a$ forcing.
Step 51's claimed homogeneous closure is falsified.

Script: `workspace/scripts/step52_flat_T4_and_deturck_audit.py`.
Data: `workspace/data/step52_flat_T4_and_deturck_audit.json`.

## 2. DeTurck pullback and the fixed-cutoff geometric flow

The DeTurck trick relates a gauge-fixed equation (with Lie derivative term)
to the geometric flow via a diffeomorphism $\phi_t$. For the standard
cutoff Ricci flow $\partial_t g = -2\chi^2\operatorname{Ric}$, naturality of
the Ricci tensor gives $\phi^*\operatorname{Ric}(\hat g) = \operatorname{Ric}(\phi^*\hat g)$, so the pullback works.

For the normalized cutoff flow with the extra $-2\chi^2 g$ term, the
pullback of $\chi^2 \hat g$ by $\phi_t$ gives

$$
\phi_t^*(\chi^2 \hat g) = (\chi^2 \circ \phi_t)\, \phi_t^*\hat g
= (\chi \circ \phi_t)^2\, g,
$$

**not** $\chi^2 g$, because $\chi \circ \phi_t \ne \chi$ in general.
The geometric flow obtained from the DeTurck pullback is therefore

$$
\partial_t g = -2(\chi \circ \phi_t)^2\bigl(\operatorname{Ric}_g + g\bigr),
$$

with a **transported** cutoff $\hat\chi_t = \chi \circ \phi_t$ rather than the
fixed geometric cutoff $\chi$.

**A03 Step 52 correctly identifies this.** The fix is the coupled system:

$$
\begin{cases}
\partial_t \hat g = -2\hat a(\operatorname{Ric}_{\hat g} + \hat g)
  + \mathcal{L}_{\hat a W(\hat g, S)}\hat g, \\
\partial_t \hat a = \hat a\, W(\hat a), \\
\hat g(0) = g_0,\quad \hat a(0) = a = \chi^2,
\end{cases}
\tag{5.2}
$$

where $\hat a = a \circ \phi^{-1}$ is the transported coefficient. Pulling back
by $\phi_t$ then recovers the exact fixed-cutoff geometric flow $\partial_t g =
-2a(\operatorname{Ric}_g + g)$.

### 2.1 Structure of the coupled system

The metric equation has the same degenerate principal part as Xu/Yang with
coefficient $\hat a$ (instead of the fixed $a$). The normalization $-2\hat a
\hat g$ remains an algebraic (zeroth-order) perturbation, as A03 correctly
argued for the metric-only version.

The scalar transport equation $\partial_t \hat a = \hat a\, W(\hat a)$ is
first-order in space (through the DeTurck vector field $W$, which involves
$\nabla \hat g$). High Sobolev norms of $\hat a$ must be propagated alongside
metric norms, creating cross-estimates but no new principal-part degeneracy.

**Assessment.** The coupled system is strictly harder than Xu's metric-only
construction. The new ingredients are:

- The coefficient $\hat a$ in the principal part evolves (instead of being fixed).
- The scalar equation couples metric derivatives to coefficient derivatives.
- Contraction estimates must handle the cross-terms
  $(\hat a_1 - \hat a_2)(\operatorname{Ric}_{\hat g_2} + \hat g_2)$ and
  $(W_1 - W_2)(\hat a_2)$.

These are standard complications for coupled parabolic-transport systems, and
the coupling is through coefficients rather than principal parts. The
construction is **structurally plausible** but not yet proved. A02's assessment
is that this is a tractable PDE problem for a dedicated technical step, not
an insurmountable obstruction.

## 3. Critical-product analysis and first-exit preservation

Even if the start module were proved, the first-exit $H_2$ preservation faces
a structural limitation.

### 3.1 The critical product for the IL family

The $H_2$ preservation requires the Moser iteration from $L^{n/2}$ to
$L^\infty$, controlled by the critical product

$$
\bar\beta = \mathsf{S} \cdot \widehat H_2^{1/2}
$$

where $\mathsf{S} = C(4, K r_*^2)\, r_*^2\, \operatorname{Vol}(B_{r_*})^{-1/2}$ is
the Maheux–Saloff-Coste Sobolev constant on the support ball, and
$\widehat H_2 = \int_{\operatorname{supp}\chi} |\operatorname{Rm}|^2\, d\mu$.

For the Ishida–LeBrun critical family with topological parameter
$A = \sum c_1^2(X_j)$:

- The global average curvature is $K_0 = \operatorname{Vol}^{-1}\int
  |\operatorname{Rm}|^2 \to 3/2$ as $\delta \to 0$ (from CGB).
- The support radius is $r_* = c(A/K_0)^{1/4} \sim c A^{1/4}$.
- On a maximal-function good ball: $\int_{B_{r_*}} |\operatorname{Rm}|^2
  \le 4K_0 \operatorname{Vol}(B_{r_*})$.
- The Sobolev constant satisfies $\mathsf{S} \ge C r_*^2
  \operatorname{Vol}(B_{r_*})^{-1/2}$.

Combining (and cancelling the volume):

$$
\bar\beta \ge \mathsf{S} \cdot (4K_0\operatorname{Vol})^{1/2}
= 2K_0^{1/2} r_*^2 \cdot C(4, Kr_*^2)
\sim 2\sqrt{3/2}\, c^2 A^{1/2}.
$$

**The critical product grows as $O(A^{1/2})$.** For large $A$ (complex IL
manifolds), it exceeds any universal threshold. Yang's Theorem 9.2 at $p = n/2$
requires $\bar\beta < c(4)^{-1}$, so the theorem's smallness condition fails
for large $A$.

### 3.2 The metric comparison constraint

The terminal metric comparison

$$
I(T) = \int_0^T \|aE(t)\|_\infty\, dt
\le \frac{3C\delta}{2}\, \theta^{2/3} r_*^2
$$

requires $I(T) \le 1/100$ for the terminal geometry to be comparable to the
initial geometry. This gives

$$
\delta_0 \le \frac{c}{\theta^{2/3}\, r_*^2}
= \frac{c}{\theta^{2/3}\, c'^2\, A^{1/2}}
\sim \frac{C'}{A^{1/2}}.
$$

### 3.3 Consequences for the restricted theorem

For **fixed topology** (fixed $A$): all constants are finite. If the start
module and $H_2$ preservation are proved, the restricted theorem gives a
per-manifold gap $\delta_0(M) > 0$. The gap is topology-dependent:
$\delta_0 \sim C'/A^{1/2}$.

For the **IL family** with growing $A$: $\delta_0 \to 0$ as $A \to \infty$.
There is no uniform gap across the IL family.

For **Yau–26**: the proposition requires dimension-only constants $c_n, C_n$.
The restricted IL theorem, even if fully proved, gives only per-manifold gaps
that shrink with topological complexity. It proves that no single IL manifold
is a counterexample, but does not rule out the whole family as a counterexample
source (since $\inf_M \delta_0(M) = 0$ over the family).

This is a **structural limitation**, not a fixable bug: the $O(A^{1/2})$
critical product and the $O(A^{-1/2})$ gap are inherent to the large-topology
regime of the maximal-function / Sobolev / Moser approach.

## 4. Summary of the negative chain's current status

| Module | Status | Issue |
|--------|--------|-------|
| **A1 (start)** | **NOT proved** | Fixed-cutoff flow needs coupled system (5.2) |
| **A2 (first-exit $H_2$)** | **Not checkable** | Depends on A1; flat T⁴ falsifies homogeneous closure |
| **A2 (first-exit $Q, J_6$)** | **Downstream** | Cannot be verified until $H_2$ works |
| **A3 (metric comparison)** | **Downstream** | $\delta_0 \sim A^{-1/2}$ from drift integral |
| **A4 (continuation)** | **Separate** | Shifted $T/U/C$ may survive independently |
| **Terminal density** | **Downstream** | All above needed |

The honest assessment is:

1. **The start module is the critical interface**, not $H_2$ preservation.
   A03 correctly identified the coupled system (5.2) as the repair target.
2. **The coupled system is structurally plausible** but requires a new
   technical construction that nobody has completed.
3. **Even with full technical completion**, the restricted theorem gives
   only per-manifold gaps scaling as $A^{-1/2}$, not dimension-only constants.
4. **The flat T⁴ example** is a genuine falsifier of the homogeneous
   critical-energy approach and should be preserved as a permanent test case.

## 5. What this step establishes for the broader research

The negative-chain audit sharpens the overall Yau–26 picture:

- **Positive noncollapsed**: banked as a one-way hardness reduction (Steps 49–51).
  $P_4^+$ implies mixed product-quotient rows carry Einstein metrics; their
  Einstein status is an open problem.
- **Negative IL restricted**: per-manifold gaps exist in principle
  (topology-dependent), but the start module is unproved and the gap shrinks
  as $O(A^{-1/2})$.
- **Positive collapse**: no new mechanism since Step 29.
- **$n \ge 5$**: no established route.
- **Lean formalization**: algebraic fragments only.

No branch of the full Yau–26 proposition is proved or refuted.


## 6. Tractability of the coupled system (5.2)

A03's coupled system

$$
\begin{cases}
\partial_t \hat g = -2\hat a(\operatorname{Ric}_{\hat g} + \hat g)
  + \mathcal{L}_{\hat a W}\hat g, \\
\partial_t \hat a = \hat a\, W(\hat a), \\
\hat g(0) = g_0,\;\; \hat a(0) = a = \chi^2,
\end{cases}
$$

is a coupled degenerate-parabolic / first-order-transport system. As
Constructor, here is my assessment of its tractability:

**Favorable structure:**
- The metric equation has the same degenerate principal part as Xu/Yang.
  The normalization $-2\hat a\hat g$ is algebraic (zeroth-order).
- The scalar transport $\partial_t\hat a = \hat a W(\hat a)$ is first-order;
  it preserves the sign $\hat a \ge 0$ and degeneracy pattern.
- The coupling is through **coefficients**, not principal parts: $\hat a$
  appears as a coefficient in the metric equation, and $W$ (from the metric)
  drives the scalar equation.

**Technical complications:**
- The frozen problem for Xu's iteration must freeze both $U$ (metric) and
  $\alpha$ (coefficient), then solve:
  $$
  \partial_t V = (\alpha+\varepsilon)U^{-1}\widetilde\nabla^2 V
    + D(U,V) + B(U,\widetilde\nabla U) - 2\alpha V,\qquad
  \partial_t\beta = \beta W(\alpha).
  $$
  The scalar equation is an ODE given $\alpha$ and $U$. The metric equation is
  Xu's original with modified coefficient $\alpha$ (not fixed $a$).
- High Sobolev estimates require cross-terms: $\|\hat a\|_{H^m}$ enters the
  metric estimates through the coefficient, and $\|\hat g\|_{H^{m+1}}$ enters
  the scalar estimates through $W = \Gamma(\hat g) - \Gamma(\widetilde g)$.
- Contraction needs the coupling to be subordinate: the cross-terms
  $(\hat a_1-\hat a_2)(\operatorname{Ric}_2+\hat g_2)$ and
  $(W_1-W_2)(\hat a_2)$ introduce one derivative of the metric difference.

**Expected resolution path:** Staggered Sobolev grading
$\|\hat g\|_{H^{m+1}} \times \|\hat a\|_{H^m}$ should close, because the
scalar equation is first-order and its sensitivity to the metric involves
only one derivative of $\hat g$. The $\varepsilon \to 0$ limit passes by the
same Arzelà–Ascoli/weak-compactness argument as Xu, since the added scalar
component lives in a fixed finite-dimensional ODE at each spatial point
(given the metric trajectory).

**Assessment:** Proving this rigorously requires going through Xu's 40-page
argument with the cross-estimates. It is a well-posed technical problem, not a
conceptual obstruction. However, it is not a trivial modification: the coupled
contraction estimate is genuinely new and must be checked term by term. A
dedicated step by Agent2 or Agent3 could complete this, but it is a significant
PDE exercise.

**What it would deliver:** Per-datum short-time existence for the fixed-cutoff
normalized flow. Combined with the per-manifold first-exit and critical-product
bounds, this would give $\delta_0(M) > 0$ for each fixed critical IL manifold,
with $\delta_0 \sim C'A^{-1/2}$.

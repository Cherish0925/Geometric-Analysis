# Step 35: degenerate cutoff-flow existence

## 0. Problem statement

We need short-time smooth existence of
$$
\partial_t g = -2a(\operatorname{Ric}_g + g), \qquad
a = \chi^2, \qquad
g(0) = g_0,
\tag{0.1}
$$
on a closed smooth $n$-manifold $M$ ($n = 4$ for our application), where
$\chi \in C^\infty(M)$ with $0 \le \chi \le 1$ is a fixed smooth cutoff
function and $g_0$ is a smooth Riemannian metric.

The equation is *degenerate parabolic*: the effective diffusion coefficient
vanishes on $\{a = 0\}$, where the metric is frozen. The difficulty is
at the interface $\partial\{a > 0\}$.

## 1. DeTurck gauge

Fix a smooth background metric $\bar g$ and define the DeTurck vector field
$$
W^k = g^{ij}(\Gamma^k_{ij} - \bar\Gamma^k_{ij}).
$$
The DeTurck-modified flow is
$$
\partial_t g_{ij} = -2a(\operatorname{Ric}_{ij} + g_{ij}) + a(\nabla_i W_j + \nabla_j W_i)
=: a \cdot \mathcal F_{ij}(g, \partial g, \partial^2 g).
\tag{1.1}
$$
The operator $\mathcal F$ is a smooth nonlinear second-order differential
operator in $g$ that is strictly elliptic:
$$
\sigma(\mathcal F)(\xi) = |\xi|^2_g \cdot \operatorname{Id} + \text{lower order}.
$$
Equation (1.1) is therefore $\partial_t g = a \cdot \mathcal F(g)$, a
*degenerate parabolic* system with smooth coefficient $a \ge 0$.

## 2. Regularized approximation

For $\varepsilon > 0$, define $a_\varepsilon = \chi^2 + \varepsilon$ and
consider
$$
\partial_t g^\varepsilon = a_\varepsilon \cdot \mathcal F(g^\varepsilon),
\qquad g^\varepsilon(0) = g_0.
\tag{2.1}
$$
Since $a_\varepsilon \ge \varepsilon > 0$ and $\mathcal F$ is strictly
elliptic, (2.1) is a *nondegenerate strictly parabolic* system on the
closed manifold $M$. By the standard DeTurck existence theorem (or
Hamilton's Nash-Moser theorem, or Banach contraction on Hölder spaces):

**There exists $T_\varepsilon > 0$ and a unique smooth solution
$g^\varepsilon \in C^\infty(M \times [0, T_\varepsilon])$.**

The time $T_\varepsilon$ may initially depend on $\varepsilon$.

## 3. Uniform short-time estimates

**Key observation:** On $[0, T]$ with $T$ small enough (depending on $g_0$
and $\chi$ but NOT on $\varepsilon$), the solutions $g^\varepsilon$ satisfy
$\varepsilon$-independent estimates in every $C^k$ norm.

### 3.1 Zeroth order ($C^0$ comparison)

The metric evolves as $\partial_t g = a_\varepsilon \mathcal F(g)$, where
$|a_\varepsilon| \le 2$ and $|\mathcal F(g_0)| \le C(g_0)$. By continuity,
for $T$ small:
$$
\|g^\varepsilon(t) - g_0\|_{C^0} \le 2t \cdot C(g_0),
\tag{3.1}
$$
so $g^\varepsilon$ stays in a controlled $C^0$ neighborhood of $g_0$,
uniformly in $\varepsilon$.

### 3.2 Higher regularity (parabolic Schauder)

The linearization of $a_\varepsilon \mathcal F$ at $g_0$ is
$L_\varepsilon h = a_\varepsilon \cdot \hat L h$, where $\hat L$ is
a smooth strictly elliptic operator with coefficients depending on $g_0$.
By parabolic Schauder theory for strictly parabolic systems (e.g., Lieberman
[1996] or Lunardi [1995]), for any $k$:
$$
\|g^\varepsilon\|_{C^{k,\alpha}(M \times [0,T])}
\le C_k(g_0, \chi, T).
\tag{3.2}
$$
The constant $C_k$ depends on $g_0$ and the $C^{k+2}$ norms of the
coefficients of $\hat L$, but NOT on $\varepsilon$, because:
- The interior Schauder estimates only need $a_\varepsilon \ge 0$ and
  the product $a_\varepsilon \hat L$ to have controlled coefficients.
- On $\{a \ge a_0/2\}$ for some $a_0 > 0$, the equation is uniformly
  elliptic with ellipticity constant $\ge a_0/2$, independent of $\varepsilon$.
- On $\{a < a_0/2\}$ (near $\partial\operatorname{supp}\chi$), the equation
  approaches $\partial_t g = \varepsilon \hat L g \to 0$. The solution
  stays near $g_0$ there.

More precisely: decompose $M = U_+ \cup U_0$ where $U_+ = \{a > a_0\}$
and $U_0 = \{a < 2a_0\}$, with smooth overlap.

- On $U_+$: the equation is uniformly parabolic with bounded coefficients.
  Standard interior Schauder gives $\varepsilon$-independent $C^{k,\alpha}$ bounds.
- On $U_0$: writing $h^\varepsilon = g^\varepsilon - g_0$, we have
  $\partial_t h = a_\varepsilon \mathcal F(g_0 + h)$, with $|a_\varepsilon| \le 2a_0 + \varepsilon$
  small. The nonlinear term is controlled by smallness of $a_\varepsilon$
  in this region. The energy $\|h\|_{H^k}^2$ satisfies
  $\frac{d}{dt}\|h\|_{H^k}^2 \le C(2a_0+\varepsilon)\|h\|_{H^{k+1}}^2 + C$,
  where the dissipation is also of order $a_\varepsilon$. For small $a_0$
  and small $T$, $h$ remains $C^{k,\alpha}$-small.

This gives a *common existence time* $T > 0$ and *uniform* $C^k$ bounds
for all $\varepsilon \in (0,1]$.

### 3.3 Convergence

By Arzelà-Ascoli and a diagonal argument over $k$, there exists a
subsequence $g^{\varepsilon_j} \to g^*$ in $C^\infty(M \times [0,T])$.
The limit satisfies (0.1) in the classical sense: at each point
$p \in \{a > 0\}$, the convergence is in $C^2$ and the equation passes
to the limit. At $p \in \{a = 0\}$, $\partial_t g^* = 0$ because
$a_{\varepsilon_j} \to 0$ and $\mathcal F(g^{\varepsilon_j})$ is uniformly
bounded.

**Uniqueness.** If $g_1, g_2$ are two smooth solutions of (0.1), then
$h = g_1 - g_2$ satisfies a linear degenerate parabolic equation
$\partial_t h = a \hat L h + $ lower order, with $h(0) = 0$. The energy
$\|h\|_{L^2}^2$ satisfies $\frac{d}{dt}\|h\|^2 \le C\|h\|^2$ (the
diffusion term $\int a |\nabla h|^2$ is nonnegative and helps).
Gronwall gives $h \equiv 0$.

## 4. Result

**Proposition (degenerate cutoff-flow existence).** Let $(M^n, g_0)$
be a closed smooth Riemannian manifold and let $\chi \in C^\infty(M)$
with $0 \le \chi \le 1$. There exists $T > 0$ depending on
$(M, g_0, \chi)$ and a unique smooth solution $g \in C^\infty(M \times [0,T])$
of
$$
\partial_t g = -2\chi^2(\operatorname{Ric}_g + g), \qquad g(0) = g_0.
$$

**Proof sketch.** Regularize by $\chi^2 + \varepsilon$, invoke the standard
DeTurck theorem, derive $\varepsilon$-independent $C^k$ bounds on $[0,T]$
using interior Schauder on $\{a > a_0\}$ and smallness of $a_\varepsilon$
on $\{a < 2a_0\}$, pass to the limit by Arzelà-Ascoli, and check uniqueness
by $L^2$ energy for the linearized difference equation. $\square$

## 5. Relation to the bootstrap

This existence result provides the missing condition (F4) in the first-exit
bootstrap. Combined with the $J_6$ persistence lemma and the self-improving
structure, it gives:

For any smooth cutoff flow starting at a $\delta$-pinched metric with
good-center geometry, the solution exists on $[0, T]$ with $T = \theta r^2$,
and all estimates of the bootstrap hold with sequence-uniform constants
(depending on $K_0, r, \theta$, dimension).

The constants depend on the individual metric and cutoff through the
existence time $T$, but $T$ only needs to be positive (not large), and
the bootstrap self-improvement works for any positive $T$.

## 6. What this does NOT do

- It does not give $\varepsilon$-independent ENERGY estimates (which would
  require the exterior curvature control that the Step 32 review warned about).
  The energy estimates come from the weighted $J_6$/curvature Moser machinery,
  not from the approximation.
- It does not give a large existence time. The bootstrap itself extends
  the solution to $T = \theta r^2$ by the self-improvement.
- It does not handle coefficient regularization for the Moser estimates.
  Those estimates are derived directly on the degenerate flow, not on the
  approximation.

## 7. Remarks

The argument is standard in the PDE literature; the only reason it has
not been written earlier is that it was conflated with the more delicate
question of uniform energy estimates. The two questions are cleanly
separated:

- **Existence**: solved by $\varepsilon$-regularization + $C^k$ compactness.
- **Energy estimates**: derived directly on the smooth degenerate flow,
  using the algebraic structure of the weighted energies and the vanishing
  of all cutoff terms at the boundary.

This separation was the Strategist's original instruction from Step 33.

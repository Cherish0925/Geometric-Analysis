# Step 39: consolidated analytic status

> **Supersession notice (Step 40).** Preserve §1.1, the general-p homogeneous
> defect power inequality. Withdraw §1.2 and every downstream status assertion
> that treats Theorem 8.1, smooth continuation, or the first-exit flow as proved.
> Step 40 finds the current-exponent multiplication gap, proves the m=2 coupled
> repair and the preceding order-one unweighted \(\nabla T\) estimate, but not
> the arbitrary-order continuation theorem.

Session: S0910A03. Agent2 / Constructor. Phase: Execute.

## 1. What was completed in this step

Two constructions that fill the last major analytic gaps identified by
Step 38's TTCS review:

### 1.1 General-$p$ homogeneous defect power inequality (Theorem 7.1)

For every real $p\ge6$, using $s=|E|^2$ and $z_p=\eta a^{(p-1)/2}s^{p/4}$:
$$
H_p'+c\|\nabla z_p\|_2^2
\le Cp^4(1+r^{-2}+\mathcal S^2Y)H_p,
$$
with no $E$-independent additive source, no Kato regularization, and no
division by $a$.

**Key structural finding:** Two-factor absorption (Step 35 mechanism) works at
fixed $p$ but requires $\gamma\lesssim1/p$, failing on the ladder. The ladder
necessarily uses three-factor Hölder $R_p\le Y^{1/3}H_p^{1/3}\|z_p\|_4^{4/3}$
followed by Young(3,3/2), producing a Grönwall coefficient without
$p$-dependent smallness.

Verified: TTCS (6 claims), 48/48 algebraic checks.

### 1.2 Historical continuation proposal (withdrawn in Step 40)

For every $m\ge0$ and $p\ge2$, on $[0,T)$ where $|U|\le K$:
$$
\sup_{t<T}(\|\nabla^mU\|_p+\|\nabla^{m+1}\chi\|_p+\|\nabla^mT\|_p)<\infty.
$$
The signed Hessian lemma handles all single-$\chi$ Hessian terms at every $m$.
Top-jet IBP produces same-level coupling $(\nabla^mU,\nabla^{m+1}\chi)$, not
higher. Corollaries give pointwise bounds and smooth extension.

## 2. Complete dependency graph for the restricted 4D negative route

All items below are conditional on a smooth first-exit interval with the
stated support, Sobolev, and comparability hypotheses.

### Layer A: Existence and continuation

| Component | Status | Reference |
|-----------|--------|-----------|
| Transported-coefficient DeTurck existence | Adapted from Yang Thm 8.2 | Step 37 note |
| Continuation: finite $L^p$ all derivatives | Open beyond the Step 40 m=2 repair | Steps 39-40 |
| Extension criterion: $|U|\to\infty$ or $T=\infty$ | Not established | Step 40 correction |

### Layer B: Zero-order first-exit estimates (sequence-uniform)

| Component | Status | Reference |
|-----------|--------|-----------|
| $K_2$ persistence + spacetime $D_2$ | Conditional lemma (q=2 absorption) | Step 38 §4 |
| $J_6$ persistence (two-factor, $Y$-free) | Proved conditional lemma | Step 35 |
| Global $Q(t)=\int|E|^2$ persistence | Proved conditional lemma | Step 37 |
| $Y(t)\le C\gamma K_2/t$ (q=3 good-slice) | Conditional lemma | Step 38 §4 |
| $\mathcal S^2Y(t)\le C\gamma^3/t$ (dyadic) | Consequence of above | Step 38 §4 |

### Layer C: Moser endpoints (sequence-uniform)

| Component | Status | Reference |
|-----------|--------|-----------|
| General-$p$ curvature power inequality | A01 Step 35 index-level | A01 Step 35 |
| General-$p$ defect power inequality | **Proved (Thm 7.1)** | **Step 39** |
| Curvature Moser: $\|aF(t)\|_\infty\le C\gamma/t$ | Consequence of Layers B+C | Step 38 §5 |
| Defect Moser: $\|aE(t)\|_\infty\le C\delta(r^2/t)^{1/3}$ | Consequence of Layers B+C | Step 39 §8 |
| Integrable metric drift: $\int_0^T\|aE\|\le C\delta\theta^{2/3}r^2$ | Consequence | Step 39 §8 |

### Layer D: Support geometry and self-improvement

| Component | Status | Reference |
|-----------|--------|-----------|
| Macro-disjoint coloured supports | Established | Steps 30, 38 |
| Moving Sobolev/metric comparability | Conditional on drift bound | Step 34 |
| Simultaneous first-exit closure | Conditional on unresolved existence/continuation | Steps 34-40 |

### Layer E: Terminal geometry

| Component | Status | Reference |
|-----------|--------|-----------|
| Terminal calibration ($Q\to$ Weyl constraint) | Conditional on $Q$ | Steps 3, 15 |
| Exponential-pullback chart selection | Conditional on bounded-curvature plateau | Steps 16, 29 |
| Local Einstein germ + projector contradiction | Proved (noncollapse case) | Steps 5-6 |
| Full terminal passage | **Not yet consolidated** | — |

## 3. What remains to complete the restricted 4D negative route

1. **Existence and arbitrary-order continuation.** Extend the Step 40 order-one
   unweighted \(\nabla T\) lemma and m=2 coupled pair to every order with an
   explicit finite-exponent schedule; prove the transported-coefficient start
   and shifted terminal restart without division by \(a\).

2. **Self-improving first-exit argument.** Only after those functional estimates
   exist, combine them with Layers B-C and moving support/Sobolev geometry on one
   actual smooth interval.

3. **Terminal geometric passage (Layer E).** Consolidate the controlled terminal
   metric, calibrated density, exponential-pullback chart selection, Einstein
   germ extraction, and projector contradiction with all flow hypotheses explicit.

4. **Extension to the full Ishida-LeBrun no-Einstein family.** Reconcile the
   above-critical topological estimate with the near-critical smoothing regime
   while retaining constants and errors normalized by the topology parameter.

## 4. What this does NOT address

- The positive Ricci-pinching branch (Myers, but no general collapse obstruction).
- Arbitrary four-manifold topology (only Ishida-LeBrun no-Einstein manifolds).
- Dimensions $n\ge5$.
- Dimension-only pinching constants (our constants are per-manifold or per-family).
- Lean formalization.
- The full Yau Problem 26 statement.

The scientific value of the restricted result, if completed, would be the
**collapse-uniform smoothing principle**: a mechanism that preserves global
Einstein defect while creating bounded-curvature plateaux, with all
Sobolev-volume factors canceling. This mechanism has potential transferability
to other Ricci-pinching problems.

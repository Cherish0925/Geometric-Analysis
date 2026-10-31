# Step 35: assembled first-exit bootstrap (provisional)

## 0. Purpose

This note assembles the conditional chain from the proved $J_6$ lemma
(§35 companion note), the curvature energy inequalities (A01 Step 33
and A03/A01 earlier steps), and the moving-geometry requirements,
into a self-improving first-exit argument. It shows precisely which
premises are now established and which remain conditional.

## 1. Ingredients (status)

| Ingredient | Status | Source |
|---|---|---|
| $J_6$ persistence: $J_6(t) \le e^{C(1+r^{-2})t}J_6(0)$ | **PROVED** (conditional on flow existence and first-exit geometry) | Step 35 lemma |
| Curvature power inequality: $K_p' + cD_p \le Cp^N(r^{-2}+1+\mathcal S^2Y)K_p$ | Conditional (two routes for Hessian-$a$) | A01 Step 33 eq 3.2 |
| $K_2$ persistence: $\sup K_2 + \int D_2 \le CK_2(0)$ | Conditional on $q=2$ energy + small $\gamma$ | Step 34 eq 3.1 |
| Curvature seed: $\int_0^t Y \le C\gamma K_2(0)$ | Conditional on $K_2$ persistence | Step 34 eq 3.2 |
| Pointwise curvature: $Y(t) \le C\gamma K_2/t$ | From $q=3$ forward propagation | Step 34 eq 3.3 |
| Curvature Moser endpoint: $\|aF(t)\|_\infty \le C\gamma/t$ | Conditional on curvature Moser chain | Step 34 eq 4.6 |
| Defect Moser: $\|aE(t)\|_\infty \le C\delta(r^2/t)^{1/3}$ | From $J_6$ persistence + defect Moser | Step 34 eq 4.8 |
| Integrable drift: $\int_0^T\|aE\|_\infty \le C\delta\theta^{2/3}r^2$ | From defect endpoint | Step 34 eq 4.9 |
| Moving Sobolev: $\mathcal S(t) \le 2\mathcal S(0)$ | From metric drift < bilipschitz threshold | Standard |
| Flow existence | **Open** (degenerate coefficients) | Step 34 §6, Step 32 |
| Continuation ($\nabla^m U$, cutoff jets) | **Open** (datum-dependent) | Step 34 §6 |

## 2. The bootstrap argument

Define the first-exit time
$$
T^* = \sup\{t > 0 : \text{conditions (F1)--(F4) hold on } [0,t]\},
$$
where the conditions are:

- **(F1)** $K_2(t) \le 2 K_2(0)$;
- **(F2)** $\mathcal S(t) \le 2\mathcal S(0)$;
- **(F3)** $\int_0^t \|aE(s)\|_\infty\,ds \le \alpha$ for some bilipschitz threshold $\alpha > 0$;
- **(F4)** The smooth flow exists on $[0,t]$ and the support/buffer geometry is comparable.

**Step A: $J_6$ persistence (unconditional on curvature).** The Step 35
lemma gives, under (F1)--(F4):
$$
J_6(t) \le e^{C(1+r^{-2})t} J_6(0) \le C_1 \delta^6 V.
\tag{2.1}
$$
This uses only $K_2$ control (through $\gamma$), not $Y$ or $\|aF\|_\infty$.

**Step B: $K_2$ persistence and curvature seed.** The $q=2$ energy
inequality with small $\gamma$ gives (F1) self-improved. Combined with $q=3$:
$$
\int_0^t Y \le C\gamma K_2(0), \qquad
Y(t) \le C\gamma K_2(0)/t.
\tag{2.2}
$$

**Step C: Curvature Moser iteration.** Using (2.2) as the coefficient
seed in A01 eq.\ (3.2), the nested spacetime recurrence starting at $p_0 = 3$
gives
$$
\|aF(t)\|_\infty \le C\gamma/t, \qquad t \in (0,T^*].
\tag{2.3}
$$

**Step D: Defect Moser iteration.** Using (2.1) as the defect seed
and the general defect inequality (A01 eq.\ 4.4) with the same $\mathcal S^2 Y$
coefficient, the nested recurrence from $p_0 = 6$ gives
$$
\|aE(t)\|_\infty \le C\delta(r^2/t)^{1/3}.
\tag{2.4}
$$

Here the key observation: the $J_6$ seed (2.1) is **independent** of
the curvature Moser output (2.3), so there is no circularity in
using the curvature coefficient (2.2) for the defect Moser iteration.
The structure is:

$K_2$ persistence $\to$ $J_6$ persistence (Step A, via $\gamma$)
$K_2$ persistence $\to$ curvature seed $Y$ (Step B)
$Y$ $\to$ curvature Moser (Step C, gives $\|aF\|_\infty$)
$J_6$ + $Y$ $\to$ defect Moser (Step D, gives $\|aE\|_\infty$)

There is no circular dependence.

**Step E: Integrable drift.** From (2.4):
$$
\int_0^{T^*} \|aE(s)\|_\infty\,ds
\le C\delta \theta^{2/3} r^2.
\tag{2.5}
$$
For $\delta < \delta_0 := \alpha/(C\theta^{2/3}r^2)$, this gives
$\int_0^{T^*}\|aE\|_\infty < \alpha$, strictly improving (F3).

**Step F: Sobolev and $K_2$ comparisons.** The metric evolves as
$\partial_t g = -2aE$, so under the bilipschitz threshold (F3) with
$\alpha$ small, the ball volumes and Sobolev constants change by
a controlled factor. Specifically, if $g(t) = (1 + O(\alpha))g(0)$,
then $V(t) = (1+O(\alpha))V(0)$ and
$\mathcal S(t) = (1+O(\alpha))\mathcal S(0)$, strictly improving (F2).
The $K_2$ comparison uses both the metric change and the curvature
integral; for small $\delta$, (F1) is also strictly improved.

**Conclusion.** If $T^* < T = \theta r^2$, Steps A--F show that all
conditions (F1)--(F4) are strictly improved at $T^*$, contradicting
the definition. Therefore $T^* \ge T$, and all estimates hold on $[0,T]$.

## 3. Dependencies on flow existence and continuation

The argument above is conditional on (F4): smooth existence of the
degenerate cutoff flow and qualitative regularity of the cutoff jets.
This is the last genuinely open analytic obstacle:

1. **Degenerate existence.** The coefficient $a = \chi^2$ vanishes on
   $\operatorname{supp}(1-\chi)$. A rigorous existence statement for
   $\partial_tg = -2\chi^2(\operatorname{Ric}+g)$ on $[0,T]$ with
   smooth initial data and fixed smooth $\chi$ is needed. DeTurck's
   trick works where $a > 0$; the degenerate region $\{a=0\}$ is a
   stationary collar ($\partial_tg = 0$ there), so the issue is the
   regularity at the interface $\{a = 0\} \cap \{a > 0\}$.

2. **Cutoff jet control.** The evolving Hessian $\nabla^2_{g(t)}\chi$
   satisfies $\partial_t\nabla^2\chi = -(\partial_t\Gamma)\cdot\nabla\chi$.
   The base pair $(\nabla U, \nabla^2\chi)$ must be controlled by
   a datum-dependent Gronwall, as specified in Step 34 §6.

3. **Higher continuation.** For terminal plateau regularity, all
   derivatives $\nabla^m U$ must be finite (datum-dependent constants).

These are per-metric (not sequence-uniform) requirements, acceptable for
the bootstrap: given any one smooth initial datum and fixed smooth cutoff,
qualitative smoothness and finite constants suffice.

## 4. What this bootstrap establishes (conditional)

**Conditional on smooth flow existence (F4):** for every
maximal-function good center with $K_0 r^2 \le \Lambda$ and every
$\theta > 0$, there exists $\delta_0 = \delta_0(\Lambda, \theta, r) > 0$
such that if $\|g^{-1}(\operatorname{Ric}+g)\|_\infty < \delta_0$, then:

- $J_6(T) \le C\delta^6 V$ at $T = \theta r^2$;
- $\|aF(T)\|_\infty \le C\gamma/T$ (positive-time curvature bound);
- $\|aE(T)\|_\infty \le C\delta(r^2/T)^{1/3}$ (defect endpoint);
- $\int_0^T\|aE\|_\infty \le C\delta\theta^{2/3}r^2$ (integrable drift);
- the metric $g(T)$ is $(1+O(\delta\theta^{2/3}r^2))$-bilipschitz to $g(0)$;
- the curvature $|\operatorname{Rm}_{g(T)}| \le C\gamma/(Tr^2)$ on the
  plateau $\{a = 1\}$.

The constants $\delta_0$ and $C$ depend on $\Lambda, \theta, r$ and dimension;
they are sequence-uniform (independent of which member of the controlled
near-critical family is being considered).

## 5. How this connects downstream

The terminal curvature bound on the plateau, combined with the metric
bilipschitz equivalence, gives a smooth metric on each plateau center
with controlled geometry. The terminal calibration inequality
$$
\int\left(|W^+|-\frac{1}{2\sqrt6}\right)^2 \le \frac{7}{24}\int|E|^2
$$
and the global $Q$ control then feed into the exponential-pullback
averaging, eigenline density, and the local projector obstruction
(Einstein germ with calibrated $W^+$-spectrum is impossible).

The remaining gap between this conditional bootstrap and a theorem
is the degenerate-flow existence/continuation (§3), which must be
addressed separately.

## 6. Verification

The defect seed algebra is verified by `verify_step35_defect_algebra.py`
(28 checks). The curvature seed and Moser exponents are verified by
previous scripts. The bootstrap logic (dependency graph, absence of
circularity, self-improvement at $T^*$) is structural and inspectable
from §2.

# Step 35: per-metric cutoff-jet continuation

## 0. Purpose

This note proves that on the interval $(0, T]$ where the zero-order bootstrap
holds, the smooth solution of $\partial_t g = -2aE$ has uniformly bounded
derivatives of all orders on the plateau $\{a = 1\}$, and finite (datum-dependent)
derivatives everywhere. This is the continuation component (F4) of the first-exit
bootstrap.

## 1. Zero-order input from the bootstrap

On the first-exit interval $[0, T]$ (with $T = \theta r^2$), the bootstrap gives:

- $\|aF(t)\|_\infty \le C\gamma/t$ for $t \in (0, T]$ (curvature Moser endpoint);
- $\|aE(t)\|_\infty \le C\delta(r^2/t)^{1/3}$ for $t \in (0, T]$ (defect endpoint);
- $J_6(t) \le C\delta^6 V$ (defect persistence);
- metric bilipschitz: $e^{-\alpha}g(0) \le g(t) \le e^{\alpha}g(0)$ with
  $\alpha = C\delta\theta^{2/3}r^2$.

These are sequence-uniform (independent of which member of the near-critical
family, or which point in the collapsing sequence).

## 2. Plateau regularity via Shi estimates

On the plateau $\{a = 1\}$, the flow is exactly the normalized Ricci flow:
$$
\partial_t g = -2(\operatorname{Ric} + g) \qquad \text{on } \{a = 1\}.
\tag{2.1}
$$
For any $t_0 > 0$, the Moser endpoint gives
$$
|\operatorname{Rm}(x, t_0)| \le C\gamma/t_0 + C =: K_0(t_0)
\qquad \forall\, x \in \{a = 1\}.
\tag{2.2}
$$
By Shi's derivative estimates for the Ricci flow (Shi [1989]; the
normalized term $-2g$ is lower order):
$$
|\nabla^m \operatorname{Rm}(x, t)|
\le \frac{C_m K_0(t_0)}{(t - t_0)^{m/2}}
\qquad \forall\, x \in \{a = 1\},\ t > t_0.
\tag{2.3}
$$
At any fixed $t > 0$, all curvature derivatives are finite on the plateau.
Constants depend on $t_0$ (which we can take as $t/2$), hence on $t, \gamma, r$
but not on the individual metric beyond the bootstrap bounds.

## 3. Exterior regularity (trivial)

On $\{a = 0\}$, the flow is $\partial_t g = 0$, so $g(t) = g(0)$ for all $t$.
All derivatives are those of the smooth initial metric.

## 4. Transition region: coupled cutoff-jet estimate

The transition region $\{0 < a < 1\}$ requires the coupled estimate for
the shifted curvature and cutoff Hessians.

### 4.1 Setup

Recall $T = \operatorname{Rm} + G$ where $G = g \wedge g / (2(n-1))$,
$U = aT$, and $\operatorname{Ric}(U) = a(\operatorname{Ric} + g) = aE$.

The connection variation under $h = \partial_t g = -2aE$ is:
$$
\partial_t \Gamma^k_{ij}
= -g^{kl}(a_i E_{jl} + a \nabla_i E_{jl} + a_j E_{il}
  + a \nabla_j E_{il} - a_l E_{ij} - a \nabla_l E_{ij}).
\tag{4.1}
$$
This involves $\nabla a \cdot E$ and $a \cdot \nabla E$, both bounded by
$C(|da|F + a|\nabla\operatorname{Rm}|)$.

### 4.2 Evolution of $\nabla^2\chi$

Since $\chi$ is a fixed smooth function:
$$
\partial_t(\nabla_i \nabla_j \chi)
= -(\partial_t \Gamma^k_{ij}) \nabla_k \chi.
\tag{4.2}
$$
Using (4.1) and $|\nabla\chi| \le C/r$:
$$
|\partial_t \nabla^2 \chi|
\le \frac{C}{r}(|da|F + a|\nabla\operatorname{Rm}|).
\tag{4.3}
$$
Since $|da| = 2|\chi||d\chi| \le C/r$ and $F \le |T| + C$:
$$
|\partial_t \nabla^2 \chi|
\le \frac{C}{r^2}|T| + \frac{C}{r} a |\nabla\operatorname{Rm}|.
\tag{4.4}
$$

### 4.3 Evolution of $\nabla U$

The covariant derivative of $U = aT = a\operatorname{Rm} + aG$ evolves as:
$$
\partial_t(\nabla U) = a \Delta(\nabla U) + \mathcal A_1(\nabla U)
+ \mathcal A_0(U, \nabla^2\chi, \nabla\chi, T, \nabla T),
\tag{4.5}
$$
where $\mathcal A_1$ is a linear operator with coefficients bounded by
$C(|T| + 1)$ (from the Lichnerowicz reaction and connection variation),
and $\mathcal A_0$ contains:
- $\nabla a * \partial_t T$: bounded by $C|d\chi| \cdot (|\nabla U| + |da|F + \ldots)$
- $a * (\partial_t\Gamma) * T$: bounded by $a(|da|F + a|\nabla\operatorname{Rm}|)|T|$
- Algebraic: $\nabla(aG)$ contributions from $\partial_t g$

The precise structure (from the Codex work, §6) is that every term either
contains $\nabla U$ (controlled by dissipation + Gronwall) or is bounded by
known quantities at the previous level.

### 4.4 $L^p$ energy for the base pair

Define $\mathcal E_p(t) = \|\nabla U(t)\|_p^p + \|\nabla^2\chi(t)\|_p^p$.
From (4.4) and (4.5), using integration by parts for the diffusion term:
$$
\frac{d}{dt}\mathcal E_p
\le -c \int a |\nabla^2 U|^p + C_p \Lambda(t) \mathcal E_p + C_p R(t),
\tag{4.6}
$$
where:
- $\Lambda(t) = 1 + r^{-2} + \|T(t)\|_\infty + \|a\nabla\operatorname{Rm}(t)\|_\infty^{2/(p-1)}$
  is a coefficient depending on the individual smooth solution;
- $R(t) = C\|T(t)\|_p^p / r^{2p}$ is a lower-order source from $\nabla^2\chi$.

### 4.5 Finiteness of the Gronwall coefficient

For any smooth solution on $(0, T]$ with the zero-order bootstrap:
- $\|T(t)\|_\infty = \|\operatorname{Rm}(t) + G(t)\|_\infty$ is finite at every $t > 0$
  (the solution is smooth by the degenerate existence proposition);
- $\|a\nabla\operatorname{Rm}(t)\|_\infty$ is finite at every $t > 0$
  (smooth solution).

Therefore $\Lambda(t)$ and $R(t)$ are *locally integrable* on $(0, T]$ for
each fixed smooth solution (they may blow up at $t = 0$, but they are
finite for $t > 0$ and integrable near $t = 0$ by the Moser endpoint
$\|aF\|_\infty \le C\gamma/t$).

By Gronwall:
$$
\mathcal E_p(t) \le \left(\mathcal E_p(t_0) + \int_{t_0}^t R(s)\,ds\right)
\exp\left(\int_{t_0}^t C_p\Lambda(s)\,ds\right)
\tag{4.7}
$$
for any $0 < t_0 < t \le T$. Both integrals are finite because the
integrands are locally bounded smooth functions on $(t_0, T]$.

### 4.6 Higher-order induction

Given the base pair $(\nabla U, \nabla^2\chi) \in L^p$ for all $p$, the
next level:
- Finite unweighted $\|\nabla T\|_p$ follows from $T = U/a$ on $\{a > 0\}$
  and smoothness on $\{a = 0\}$ (where $T$ is controlled by initial data).
- The pair $(\nabla^2 U, \nabla^3 \chi)$ satisfies the same Gronwall structure
  with coefficients now controlled by the base pair.

The induction proceeds: at level $m$, control $(\nabla^m U, \nabla^{m+1}\chi)$
using all previous levels. The Codex work (§6--§7) confirms that the
finite Hölder schedule closes at each level, with the single-$\chi$ term
$$
\int \chi|\nabla^{m+1}\chi||\nabla^m U|^p
$$
handled by the $L^4$ control of $\nabla^{m+1}\chi$ from the previous pair.

**Conclusion.** All spatial derivatives of $g(t)$ are bounded on $M \times [\tau, T]$
for every $\tau > 0$, with constants depending on $g_0, \chi, \tau, T$.

## 5. Combined result

**Proposition (smooth continuation).** Let $g$ be a smooth solution of
$\partial_t g = -2\chi^2(\operatorname{Ric}+g)$ on $M \times [0, T]$ with
the first-exit bootstrap bounds. Then:

(a) On the plateau $\{a = 1\}$ and for every $t_0 > 0$ and $m \ge 0$:
$$
|\nabla^m \operatorname{Rm}(x,t)| \le C_m(t_0) \qquad \forall\, t \ge t_0.
$$

(b) On the transition $\{0 < a < 1\}$ and for every $t_0 > 0$ and $m \ge 0$:
$$
\|\nabla^m U(t)\|_p + \|\nabla^{m+1}\chi(t)\|_p \le C_{m,p}(g_0,\chi,t_0)
\qquad \forall\, t \ge t_0.
$$

(c) On the exterior $\{a = 0\}$: $g(t) = g(0)$, all derivatives bounded
by initial data.

(d) The terminal metric $g(T)$ is smooth on all of $M$, with curvature
bounded on the plateau by $C/T$ (sequence-uniform) and everywhere by
datum-dependent constants.

## 6. Relevance

This completes condition (F4) of the first-exit bootstrap: given smooth
short-time existence (from the degenerate existence proposition), the
continuation holds automatically from the zero-order Moser estimates.
The constants in (a) are sequence-uniform; those in (b) are datum-dependent
but finite. Both are sufficient for the terminal geometric passage, which
only needs the plateau regularity (a) and the global $L^2$ defect control
(from $J_6$ persistence).

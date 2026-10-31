# Step 54: First-exit and continuation on the exact transported-cutoff flow

> **Step 55 correction:** two interfaces in this note are superseded by
> `Sessions/S0910A01/workspace/notes/step55_joint_bootstrap_background_continuation_repair.md`.
> First, the first-exit bootstrap must use the coupled pair
> \(\Gamma(t)=\sup_{s\le t}\mathcal S(s)H_2(s)^{1/2}\) and
> \(V(t)=\int_0^t\|aE(s)\|_\infty ds\); it must not assume an evolving
> unweighted bound \(|E(t)|\le\delta\).  Sobolev constants are transported by
> bilipschitz comparison from \(V\), not by preserving a Ricci lower bound.
> Second, continuation must use a fixed background connection
> \(\bar\nabla=\nabla^{g(\tau)}\) and the connection difference
> \(A=\nabla^{g(t)}-\bar\nabla\); one cannot integrate
> \(\nabla^m(\partial_t g)\) as \(\partial_t(\nabla^m g)\), since
> \(\nabla^{g(t)}g(t)=0\).  Terminal noncollapse is on exponential pullback
> balls, not necessarily on image balls in a collapsed base.

Session: S0910A01. Agent2 / Constructor. Step 54. Phase: Execute.

## 0. Purpose and scope

This note gives a coherent derivation of the first-exit smoothing estimates
and continuation mechanism for the restricted Ishida–LeBrun theorem.  It
takes as input the per-datum exact flow from A03 Step 56 (doubly regularized
construction, tame hierarchy, smooth limit and geometric pullback) and
connects it to the tensor estimates from A01 Steps 34–36.

The central mathematical distinction (Strategist) is between two kinds of
energy:

1. **Augmented curvature energies** $H_q^\alpha = \int \eta_\alpha^2 a^{q-2} F_T^q$
   with $F_T = (1 + |T|^2)^{1/2}$, $T = \operatorname{Rm} + G$,
   $G = g \owedge g / (2(n-1))$.  These already contain the support volume
   through the constant $1$ in $F_T$, so a volume-proportional normalization
   contribution can be absorbed without introducing a collapse-independent
   additive constant.

2. **Defect energies** $J_6 = \int \eta^2 a^4 |E|^6$, $Q = \int |E|^2$,
   where $E = \operatorname{Ric} + g$.  These must remain genuinely
   homogeneous in $E$ because $E = 0$ is an exact stationary solution for
   every cutoff; a curvature-only additive source there would destroy the
   required $Q/A \to 0$ propagation.

The flat-torus test disproves a source-free estimate for *bare curvature*
under a nonconstant normalized cutoff: $\partial_t g = -2\chi^2(\operatorname{Ric}+g)$
applied to $g = g_{\text{flat}}$ with nonconstant $\chi$ creates curvature
from zero (§1.4).  But this does **not** disprove augmented-energy estimates:
$H_2 = \int \eta^2 (1 + |\operatorname{Rm}|^2)$ starts at a positive value
$\ge \operatorname{Vol}(B_{7r})$ and the normalization reaction is homogeneous
in $|R|^2$, hence controlled by $H_2$ itself.  For defect energies, the
Hessian-$a$ contraction tensor $B_{\rm def}$ vanishes at $E=0$ (Step 35 §6.1),
so the defect equation has no bare Hessian-$a$ source.

This note does **not** close the restricted IL theorem.  It identifies the
exact remaining load (§8) and shows that the tensor–energy architecture is
internally consistent on the exact flow.

---

## 1. Flow input from A03 Step 56

### 1.1 The exact degenerate flow

For each fixed smooth datum $(M, g_0, \chi)$ with $\chi \in C^\infty(M, [0,1])$,
A03's construction gives a smooth solution on $[0, T_0(g_0, \chi)]$:
$$
\partial_t g = -2\chi^2(\operatorname{Ric}_g + g), \qquad g(0) = g_0.
\tag{1.1}
$$
This is obtained as the smooth $(\varepsilon, \nu) \to 0$ limit of the doubly
regularized DeTurck-transported system, pulled back to the original manifold.
The lifespan $T_0$ depends on $\|g_0\|_{H^{s_0}}$ and $\|\chi\|_{H^{s_0}}$
(with $s_0 > n/2 + 4$) but **not** on the regularization parameters.

### 1.2 Structural properties of (1.1)

Write $a = \chi^2$ and $E = \operatorname{Ric}_g + g$.  On the exact flow:

- **Stationary collar**: where $\chi = 0$, $\partial_t g = 0$ and all spatial
  jets $\nabla^m g$ are time-independent.

- **Global $a$ bounds**: $0 \le a \le 1$, $|\nabla a|^2/a = 4|\nabla\chi|^2 \le C/r^2$,
  and $\nabla^r a = \nabla^r(\chi^2)$ for $r \ge 1$ are time-independent.

- **Disjoint-support summation**: on the exact flow (not on regularized
  approximants), if $\{B_{7r}(x_\alpha)\}$ are disjoint, then the flow on each
  support is coupled to the rest only through the frozen complement metric.

### 1.3 Cutoff convention

We use the buffered geometry from §4 of the consolidated proof:
$$
\chi_\alpha = 1 \text{ on } B_{5r}(x_\alpha), \quad
\operatorname{supp} \chi_\alpha \subset B_{6r}(x_\alpha), \quad
\eta_\alpha = 1 \text{ on } B_{6r}(x_\alpha), \quad
\operatorname{supp} \eta_\alpha \subset B_{7r}(x_\alpha),
$$
with $B_{7r}(x_\alpha)$ pairwise disjoint.  The global weight is
$a = \sum_\alpha \chi_\alpha^2$, and $a = 0$ on $\operatorname{supp} \nabla \eta_\alpha$
for every $\alpha$.

### 1.4 Flat-torus benchmark

On $(T^4, g_{\rm flat})$ with nonconstant $\chi$: $E = g$, so
$\partial_t g = -2\chi^2 g$.  The connection variation is
$\delta\Gamma = -d\chi^2 \otimes g + \cdots$, and curvature is created
at rate $\partial_t \operatorname{Rm}|_{t=0} = O(\nabla^2(\chi^2))$.
This means $|R|^2$ grows from zero proportionally to $|\nabla^2 a|^2 t^2$
at leading order.

**What the benchmark rules out:** any estimate of the form
$\partial_t |\operatorname{Rm}|^2 \le a \Delta |\operatorname{Rm}|^2 + C a |\operatorname{Rm}|^3$
without an additive source.

**What it does not rule out:**
- Augmented-energy estimates where $F_T^2 = 1 + |T|^2$ starts positive, and the
  Hessian-$a$ contraction is absorbed by signed IBP (Step 35 §3.3).  The signed
  IBP gives $|T_H| \le \varepsilon D_2 + C r^{-2} H_2$, with no bare additive
  constant; the curvature creation from $\nabla^2 a$ is controlled, not eliminated.
- Defect-energy estimates where $B_{\rm def}|_{E=0} = 0$, because on the flat
  torus $E = g \ne 0$ (the defect is as large as the metric, so the $E$-homogeneous
  Hessian source is $O(1)$, consistent with curvature creation).

**Precise mechanism of curvature creation:** at $t=0$ on the flat torus,
$\operatorname{Rm} = 0$ so the normalization reaction $+4a|R|^2 = 0$.
Curvature is created by the Hessian-$a$ term
$\partial_t \operatorname{Rm}|_0 \sim (\nabla^2 a) \owedge E$, not by the
normalization.  The normalization reaction is always harmless (absorbed into
$CaF^3$), but it is not the creation mechanism.

The Ishida–LeBrun application concerns $|E| \le \delta \ll 1$, where
the Hessian-$a$ source is $O(\delta^2)$ through $B_{\rm def}$ and
$O(\delta) \cdot F$ through $B_{\rm curv}$; both are absorbed by signed IBP.

---

## 2. The augmented curvature energy $H_2^\alpha$

### 2.1 Definition and initial bound

Set
$$
T = \operatorname{Rm} + G, \quad G = \frac{g \owedge g}{2(n-1)}, \quad
F_T = (1 + |T|^2)^{1/2}.
\tag{2.1}
$$
Since $|G|^2 = n/(2(n-1))$ for the curvature-tensor norm convention used here, and $|T|^2 = |{\rm Rm}|^2 + 2\langle {\rm Rm}, G \rangle + |G|^2$,
we have $1 + |T|^2 \asymp_n 1 + |{\rm Rm}|^2 = F^2$ with dimensional constants:
$$
c_n F^2 \le F_T^2 \le C_n F^2.
\tag{2.2}
$$

The critical curvature energy is
$$
H_2^\alpha(t) = \int \eta_\alpha^2 F_T^2 \, d\mu_t
= \int \eta_\alpha^2 (1 + |T|^2) \, d\mu_t.
\tag{2.3}
$$
This is **unweighted in $a$**: it controls curvature throughout the $\eta_\alpha$
support, including the small-$a$ collar where $\chi$ is decaying.

At time zero, the maximal-function threshold gives
$r^4 \fint_{B_{7r}} |\operatorname{Rm}|^2 \le \widetilde\gamma^2$,
hence
$$
H_2^\alpha(0) \le C(1 + \kappa_0^2) \operatorname{Vol}(B_{7r}),
\tag{2.4}
$$
where $\kappa_0 = \widetilde\gamma / r^2$.

### 2.2 Absorption parameter and Whitney cancellation

The localized Sobolev constant satisfies
$\mathcal{S}(t) \lesssim r^2 V^{-1/2}$, where $V$ is the
support-ball volume.  The absorption parameter is
$$
\gamma = \mathcal{S}(0) \cdot (H_2^\alpha(0))^{1/2}
\le C r^2 V^{-1/2} \cdot \sqrt{C(1+\kappa_0^2) V}
= C r^2 \sqrt{1 + \kappa_0^2}.
\tag{2.5}
$$
The collapse-dependent volume $V$ in $\mathcal{S}$ cancels against
the volume factor in $H_2^\alpha(0)$.  This is the fundamental
**Whitney volume cancellation**: the absorption threshold is
collapse-independent.

### 2.3 Evolution and the small-$\gamma$ condition

Under the exact flow (1.1), the augmented energy evolves as (Step 34 §§2–4):
$$
(K_p^\eta)' + c [p D_p^{\rm Rm} + p(p-2) D_p^F]
\le C p^N (r^{-2} + 1 + \mathcal{S}^2 Y) K_p^\eta, \quad p \ge 3,
\tag{2.6}
$$
where $K_p^\eta = \int \eta^2 a^{p-2} F_T^p$, $Y = K_3^\eta = \int \eta^2 a F_T^3$,
and $D_p^{\rm Rm}$, $D_p^F$ are the Bochner and radial dissipation terms.

For $p = 2$ (the unweighted critical energy), the pre-absorption form is
$$
(H_2^\alpha)' + c D_2^\alpha
\le C Y_T + C(1 + r^{-2}) H_2^\alpha,
\tag{2.7a}
$$
where $Y_T = \int \eta^2 a F_T^3$.  The integrated potential satisfies
$$
Y_T \le (H_2^\alpha)^{1/2} \|\chi F_T\|_4^2
\le C \mathcal{S} (H_2^\alpha)^{1/2}(D_2^\alpha + r^{-2} H_2^\alpha).
\tag{2.7b}
$$
Absorbing $D_2^\alpha$ requires the **small critical energy condition**:
$$
\gamma(t) = \mathcal{S}(t)(H_2^\alpha(t))^{1/2} \le \gamma_*,
\tag{2.7c}
$$
where $\gamma_*$ is a fixed dimensional absorption threshold.  Only under
this condition does the closed Grönwall
$$
(H_2^\alpha)' \le C(1 + r^{-2}) H_2^\alpha
\tag{2.7}
$$
hold.  The condition $\gamma \le \gamma_*$ is part of the first-exit
bootstrap (§3A below).  The absorption is not unconditional; Step 34
already states this requirement explicitly.

The normalization reaction $+4a|R|^2$ and Hamilton quadratic are both
absorbed by $CaF_T^3$ (Step 35 eq.\ 2.6), which feeds into the $CY_T$
term in (2.7a).  No bare additive constant independent of $H_2^\alpha$
is introduced, because every term in the evolution is proportional to
$F_T^q$ for some $q \ge 2$.

---

## 2A. First-exit bootstrap (superseded by Step 55)

The argument originally written here assumed an evolving unweighted bound
$|E(t)|\le\delta$ and used it to control metric drift and Sobolev constants.
That assumption is not supplied by the pinched initial metric under the cutoff
flow.  The corrected argument is in
`Sessions/S0910A01/workspace/notes/step55_joint_bootstrap_background_continuation_repair.md`.

The corrected bootstrap uses the coupled quantities
$$
\Gamma(T)=\sup_{0\le t\le T}\mathcal S(t)H_2^\alpha(t)^{1/2},
\qquad
V(T)=\int_0^T\|aE(t)\|_\infty\,dt.
$$
Metric comparison follows from
$e^{-2V(T)}g(0)\le g(T)\le e^{2V(T)}g(0)$, hence the local Sobolev constant
is transported from the initial metric by bilipschitz comparison
($\mathcal S(t)\le e^{8V(t)}\mathcal S(0)$ in dimension four).  The defect
endpoint
$$
\|aE(t)\|_\infty\le C\delta(r^2/t)^{1/3}
$$
is integrable at $t=0$, so it improves $V(T)$ on $T\le\theta r^2$.
Together with the $H_2$ Grönwall under $\Gamma\le\gamma_*$, this closes the
joint $(\Gamma,V)$ bootstrap for small initial defect, small initial critical
energy, and small fixed observation parameter $\theta$.  No preservation of a
Ricci lower bound and no unweighted $|E(t)|\le\delta$ estimate is used.

---

## 3. First-exit curvature branch

### 3.1 Integrated potential

Within the bootstrap interval $[0, \theta_* r^2]$, the $H_2$ Grönwall and
small-$\gamma$ condition give controlled evolution.  The absorption
parameter satisfies
$$
\gamma(t) \le (3/4)\gamma_* = O(r^2 \sqrt{1+\kappa_0^2}).
\tag{3.1}
$$

The integrated curvature potential (Step 34 §3) is
$$
B(t) = \int_0^t \mathcal{S}(s)^2 Y(s) \, ds.
\tag{3.2}
$$
From the $p = 3$ inequality (2.6), after a good-slice argument:
$$
B(T) \le C \gamma^3.
\tag{3.3}
$$

### 3.2 Curvature Moser iteration

The combined reaction coefficient in (2.6) is
$\mathcal{S}^2 Y + r^{-2} + 1$.  The standard $p \to \infty$ Moser
iteration (doubling $p$ at each step, using $K_{2p} \le
\mathcal{S}^2 \|aF_T^p\|_4^2$) gives the curvature endpoint:
$$
\|a F_T(t)\|_\infty \le \frac{C \gamma}{t}, \quad 0 < t \le T.
\tag{3.4}
$$
On the plateau $\{a = 1\}$, this gives $|F_T(t)| \le C\gamma/t$ and hence
$|\operatorname{Rm}(t)| \le C\gamma/t + C_n$.  At the terminal time
$T = \theta r^2$:
$$
|\operatorname{Rm}(T)| \le C \gamma / (\theta r^2) + C_n
\le C \sqrt{1+\kappa_0^2} / \theta + C_n = K,
\tag{3.5}
$$
a fixed curvature bound independent of the sequence index.

---

## 4. First-exit defect branch

### 4.1 Defect homogeneity

The Hessian-$a$ contraction for $\partial_t |E|^2$ (Step 35 §5–6):
$$
B_{\rm def}^{pq} = |E|^2 g^{pq} + (\operatorname{tr} E) E^{pq}
- 2(E^2)^{pq},
\tag{4.1}
$$
satisfies $B_{\rm def}|_{E=0} = 0$, $|B_{\rm def}| \le C |E|^2 = C s$,
and $|\nabla B_{\rm def}| \le C |E| |\nabla E|$.

This quadratic vanishing is the critical structural property.  It means:
- On the flat torus where $E = g$, the Hessian-$a$ source is $O(|E|^2) = O(1)$,
  consistent with large defect creating curvature.
- On an almost-Einstein metric with $|E| \le \delta$, the source is $O(\delta^2)$,
  hence *controlled by the defect itself*.

### 4.2 $J_6$ persistence

The unregularized sixth-power defect functional
$J_6 = \int \eta^2 a^4 |E|^6$ satisfies, after absorption (Step 34 §4 + Step 35 §6.4):
$$
J_6' + c X_6 \le C(1 + r^{-2}) J_6 + C P_6,
\tag{4.2a}
$$
where $X_6 = \int \eta^2 a^5 |E|^4 |\nabla E|^2$ and
$P_6 = \int \eta^2 a^5 F_T |E|^6$.  The reaction term satisfies
$$
P_6 \le C \gamma(t)(X_6 + r^{-2} J_6),
\tag{4.2b}
$$
using the critical Sobolev embedding and the absorption parameter $\gamma$.
Under the small-$\gamma$ condition (2.7c), the $X_6$ term is absorbed
into the dissipation, giving:
$$
J_6' + c' X_6 \le C(1 + r^{-2}) J_6.
\tag{4.2}
$$

**Grönwall:** $J_6(t) \le e^{C(1+r^{-2})t} J_6(0)$, conditional on
$\gamma(t) \le \gamma_*$ throughout.

### 4.3 Defect Moser endpoint

The $q = 2, 3$ defect hierarchy and Moser iteration give:
$$
\|a E(t)\|_\infty \le C \delta \left(\frac{r^2}{t}\right)^{1/3},
\quad 0 < t \le T.
\tag{4.3}
$$
Here $\delta = \|E(0)\|_\infty$ is the initial defect.  Importantly, the
initial defect $\delta$ **persists as a factor**: no curvature-only additive
source contaminates this estimate.  This is guaranteed by the $E$-homogeneity
of $B_{\rm def}$.

---

## 5. Metric drift and Sobolev control

### 5.1 Drift estimate (corrected)

The metric velocity is controlled by the weighted defect:
$$
|\partial_t g|=2a|E|.
$$
Thus the distortion is measured by
$$
V(T)=\int_0^T\|aE(t)\|_\infty\,dt,
\qquad
e^{-2V(T)}g_0\le g(T)\le e^{2V(T)}g_0.
\tag{5.1}
$$
Using the endpoint (4.3),
$$
V(T)
\le C\delta\int_0^T(r^2/t)^{1/3}\,dt
={3\over2}C\delta r^{2/3}T^{2/3}
=C\delta\theta^{2/3}r^2
\tag{5.2}
$$
for $T=\theta r^2$.  This is the estimate used in the Step 55 joint
$(\Gamma,V)$ bootstrap; no evolving unweighted $|E(t)|\le\delta$ bound is
assumed.

### 5.2 Sobolev constant control (corrected)

Sobolev constants are transported by bilipschitz comparison with the initial
metric.  If $e^{-2V}g_0\le g(t)\le e^{2V}g_0$, then in dimension four
$$
\mathcal S(t)\le e^{8V(t)}\mathcal S(0).
\tag{5.3}
$$
This replaces the unsupported Ricci-lower-bound/volume-comparison argument.
The coupled bootstrap in Step 55 uses (5.2)--(5.3) and the $H_2$ Grönwall to
improve both $\Gamma(T)$ and $V(T)$.

---

## 6. Continuation mechanism

### 6.1 The per-datum start problem

A03's construction gives $T_0(g_0, \chi) > 0$ depending on high Sobolev
norms.  The key observation is that $T_0$ need not be uniform across the
sequence: the first-exit estimates below are independent of $T_0$ once
a smooth solution exists.

### 6.2 Staggered hierarchy for all-order bounds

On the exact flow, define:
$$
U_m = \nabla^m(a T), \quad C_{m+1} = \nabla^{m+1} \chi, \quad
T_m = \nabla^m T.
\tag{6.1}
$$
The weighted extension schedule is:
$$
T_0 \to (U_1, C_2) \to T_1 \to (U_2, C_3) \to T_2 \to \cdots
\tag{6.2}
$$

At each weighted stage, the coupled energy satisfies (Step 45 §5.3):
$$
\frac{d}{dt}(\|U_m\|_p^p + \|C_{m+1}\|_p^p)
+ c \int a |\nabla U_m|^2 |U_m|^{p-2}
\le C(1 + \|U_m\|_p^p + \|C_{m+1}\|_p^p).
\tag{6.3}
$$

The decisive structural fact: every highest cutoff jet $C_{m+2}$ in the
weighted evolution carries a $\chi$ weight from the product-rule identity
$$
\nabla^{m+2}(\chi^2) = 2\chi C_{m+2} + \text{lower terms with } C_j, j \le m+1.
$$
After integration by parts, the remaining $\chi$ pairs with the weighted
dissipation $\int \chi^2 |\nabla U_m|^2 |U_m|^{p-2}$.

### 6.3 Continuation via a fixed background connection (Step 55 correction)

Avoiding division by $a$ is necessary but not sufficient.  With
$\nabla=\nabla^{g(t)}$ one has $\nabla g(t)=0$ identically, so
$\nabla^m(\partial_tg)$ cannot be integrated as $\partial_t(\nabla^mg)$.
The corrected bridge is recorded in
`Sessions/S0910A01/workspace/notes/step55_joint_bootstrap_background_continuation_repair.md`.

On a positive-time slab $[\tau,T_*)$, fix
$$
\bar\nabla=\nabla^{g(\tau)},\qquad A=\nabla^{g(t)}-\bar\nabla.
$$
The connection variation gives
$$
\partial_tA=g^{-1}*\nabla^{g(t)}(aE),
\tag{6.4}
$$
and conversion from evolving to fixed covariant derivatives is triangular:
$\bar\nabla^m\partial_tA$ contains the current top term
$U_{m+1}=\nabla^{m+1}(aT)$ and only lower fixed-background derivatives of
$A$.  Hence completed current-pair estimates imply fixed-background bounds
for $A$; then $\bar\nabla g=A*g$ gives fixed-background Sobolev bounds for
metric components, and the fixed scalar cutoff has time-independent
$\bar\nabla^j\chi$ with evolving cutoff jets controlled by $A$.

Thus restart follows from the triangular system
$$
(U_j,C_{j+1})\ \text{finite for the needed orders}
\Longrightarrow A\ \text{finite in a fixed background}
\Longrightarrow (g(t),\chi)\ \text{smooth restart data}.
$$
The full finite-order current-pair estimates still have to be written; this
section is no longer a proof of continuation by moving-covariant metric
derivatives.

---

## 7. Global $Q$ propagation

### 7.1 Partition and stationary remainder

$$
Q_{\rm global}(t) = Q_{\rm rest}(0) + \sum_\alpha Q_\alpha(t),
\tag{7.1}
$$
where $Q_{\rm rest} = \int (1 - \rho) |E|^2$ is constant (stationary collar)
and $Q_\alpha = \int \eta_\alpha^2 |E|^2$.

### 7.2 Local $Q_\alpha$ propagation

The defect $E$ satisfies on each support (after critical Sobolev absorption):
$$
Q_\alpha' + c D_E^\alpha \le C P_2^\alpha + C(1 + r^{-2}) Q_\alpha,
\tag{7.2a}
$$
where $D_E^\alpha = \int \eta_\alpha^2 a |\nabla E|^2$ and
$P_2^\alpha = \int \eta_\alpha^2 a F_T |E|^2$.  The reaction satisfies
$$
P_2^\alpha \le C \gamma(t)(D_E^\alpha + r^{-2} Q_\alpha).
\tag{7.2b}
$$
Under the small-$\gamma$ condition, absorption gives:
$$
Q_\alpha' \le C(1 + r^{-2}) Q_\alpha.
\tag{7.2}
$$

**Important:** the pointwise curvature endpoint $aF_T \le C\gamma/t$ from (3.4)
cannot be used directly for the $Q$ Grönwall from $t = 0$, because $t^{-1}$
is not integrable.  The correct route is the critical $L^2$-Sobolev absorption
(7.2a)–(7.2b), which does not involve $t^{-1}$.

### 7.3 Global bound

$$
Q_{\rm global}(T)
\le Q_{\rm rest}(0) + e^{CT/r^2} \sum_\alpha Q_\alpha(0)
\le e^{CT/r^2} Q_{\rm global}(0).
\tag{7.3}
$$
Since $Q_{\rm global}(0)/A_i \to 0$ (from $\delta_i \to 0$ and
calibrated volume), we get $Q_{\rm global}(T)/A_i \to 0$ for
$T = \theta r^2$.

---

## 8. Interface with the terminal contradiction

### 8.1 Terminal chart properties (pullback-localized)

At $T=\theta r^2$, the terminal metric has bounded curvature on the plateau
$\{a=1\}$ inside $B_{5r}(x_\alpha)$ and the selected center set has
$A$-proportional measure.  For each center $p$ with buffer inside the plateau,
local compactness is applied to the exponential pullback ball
$$
\mathcal B_\rho(p)\subset T_pM,
\qquad \tilde g_p=(\exp_p)^*g(T).
$$
Rauch comparison supplies uniform geometry and positive volume on
$(\mathcal B_\rho(p),\tilde g_p)$.  This is not a uniform noncollapse
statement for the image ball in the base manifold, where $\exp_p$ may fold in
a collapsed region.  The averaged density $A_\rho\Phi(p)$ is the mean on this
pullback ball, and the Step 53 unit-tangent Liouville argument controls its
integral over centers without using injectivity of $\exp_p$.

### 8.2 Topological recalibration

The terminal metric on the same smooth manifold $M_i$ satisfies the mixed
SW inequality and $\int \Phi \le 119 Q(T) = o(A_i)$.

### 8.3 Proportional-volume averaging

The Liouville-invariance averaging (patched Step 53, §7.2) gives
$$
\int_{P_i^{\rm in}} A_\rho \Phi_i(p) \, d\mu_T(p) \le C \int_M \Phi_i \le 119C \, Q_i(T),
\tag{8.1}
$$
using geodesic-flow preservation of Liouville measure on the unit tangent
bundle.  This does not use injectivity of $\exp_p$; no collapse-dependent
multiplicity arises.

Proposition 3.2 (local lower bound from compactness) then gives
$A_\rho \Phi(p) \ge \eta' > 0$ for all $p \in P^{\rm in}$, so
$$
\eta' \operatorname{Vol}(P^{\rm in}) \le 119 C \, Q_i(T),
\tag{8.2}
$$
contradicting $Q_i(T)/A_i \to 0$ and $\operatorname{Vol}(P^{\rm in}) \ge c A_i$.

---

## 9. Summary of remaining load

### 9.1 What is now coherent (TTCS-corrected)

The following components form a consistent derivation when assembled:

| Module | Source | Status |
|--------|--------|--------|
| Per-datum exact flow | A03 Step 56 | Proved modulo standard quasilinear parabolic details |
| Coupled first-exit bootstrap | Step 55 note | Uses $(\Gamma,V)$; avoids evolving unweighted $|E|\le\delta$ |
| Augmented $H_2$ first-exit | Steps 34–35 + §2–3 | Tensor-level proved; small-$\Gamma$ condition explicit |
| Defect $J_6$ and endpoints | Step 35 + §4 | Tensor-level proved; small-$\Gamma$ absorption explicit |
| Metric drift | §5 + Step 55 | From integrable weighted endpoint for $aE$ |
| Sobolev constant closure | Step 55 | Bilipschitz comparison from $V$, not Ricci lower-bound preservation |
| Fixed-background continuation bridge | Step 55 + A03 base pair | Bridge formulated with $A=\nabla^{g(t)}-\bar\nabla$; full current-pair induction still needed |
| Global $Q$ propagation | Step 36 + §7 | Proved; $L^2$-Sobolev route, not pointwise $t^{-1}$ |
| Terminal pullback charts | §8.1 + Step 55 | Rauch/noncollapse on exponential pullback balls, not base image balls |
| Liouville averaging | Step 53 §7.2 patch | Verified (no $\exp_p$ multiplicity) |
| Local lower bound (Prop 3.2) | Step 45 §3 | Proved by compactness |
| Topological recalibration | Step 45 §2, §7.1 | Pure algebra + SW |
| Terminal pullback charts | §8.1 above + Step 55 | Pullback-localized compactness |
| Liouville averaging | Step 53 §7.2 patch | Verified (no $\exp_p$ multiplicity) |
| Local lower bound (Prop 3.2) | Step 45 §3 | Proved by compactness |
| Topological recalibration | Step 45 §2, §7.1 | Pure algebra + SW |

### 9.2 What requires completion (TTCS-corrected)

1. **$F_T$ tensor verification:** TTCS confirmed the shifted version
   $B_T^{pq} = T^p{}_j{}^q{}_l E^{jl}$ satisfies the same
   bounds.  Should be written out once for the record.  Not a structural gap.

2. **Moser iteration details:** standard but should be recorded with the
   correct polynomial $p$-growth constants.

3. **Finite-order current-pair induction and continuation:** the main structural point
   ($C_{m+2}$ carries $\chi$ weight) is verified; A03 Step 56 base pair
   confirms the earliest block $T_0 \to (V,Z) \to X$ without division
   by $a$.  Step 55 supplies the fixed-background connection bridge needed
   after current-pair bounds are available.  The complete finite-order
   current-pair induction remains to be written.

4. **$Q$ propagation:** **Already proved in Step 36** (eqs 3.3-3.6)
   using the $L^2$-Sobolev absorption chain
   $\int F(\chi E)^2 \le C\gamma(X_U + r^{-2}Q_U)$.  This note's §7.2
   now correctly cites that route.  No new work needed.

5. **Convention consistency:** $|G|^2 = n/(2(n-1)) = 2/3$ in $n=4$.

### 9.3 What this does NOT establish

- The restricted IL theorem is not yet complete.  The corrected first-exit
  and continuation interfaces are in Step 55, and the remaining items in
  §9.2 still need explicit completion in that corrected form.
- The positive branch, arbitrary 4-manifold topology, dimensions $n \ge 5$,
  and the full Yau Problem 26 proposition remain open.
- The Lean formalization has not been attempted.

---

## 10. Verification

Script `workspace/scripts/step54_first_exit_verify.py` checks:
- augmented-energy norm equivalence (2.2) in $n = 4$;
- Whitney cancellation identity (2.5);
- Grönwall coefficients in (2.7), (4.2), (7.2);
- defect homogeneity $B_{\rm def}|_{E=0} = 0$;
- signed IBP absorption coefficients (3.9 of Step 35);
- metric drift integral (5.2);
- $A$-cancellation in the proportional-volume argument (8.2).

File: `Sessions/S0910A01/workspace/scripts/step54_first_exit_verify.py`.

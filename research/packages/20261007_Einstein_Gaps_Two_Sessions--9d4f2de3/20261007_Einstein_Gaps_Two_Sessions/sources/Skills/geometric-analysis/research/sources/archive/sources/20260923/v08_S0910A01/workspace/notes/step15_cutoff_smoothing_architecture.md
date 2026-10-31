> **Step 16 Preceptor correction.** This note is not a completed proof.  The Step 15 completion language is superseded by `workspace/notes/step16_preceptor_review_smoothing_architecture.md`.  The comparable-ball Bishop--Gromov initial smallness, the four-dimensional Sobolev--energy volume cancellation, the homogeneous cutoff-defect equation, topological recalibration conditional on terminal `J/A -> 0`, and the Step 8 Derdziński tensor-deficit contradiction remain useful.  However, A03's Section 10 localization argument is invalid as written: Ricci flow has no finite propagation speed; the Li bootstrap supremum cannot be closed by restricting to an inner plateau while covering estimates require outer centers; and the maximal-function estimate near one point controls only nearby centers at the comparable `r_*` scale, not an arbitrary larger `B_{rho/4}` when `r_* << rho`.  The live task is to prove a transition-inclusive, collapse-uniform cutoff-flow stability estimate on a consistently chosen support, plus a precise bounded-curvature-to-normal-cover accessibility theorem.  Closing this route would at most exclude the current LeBrun/Ishida--LeBrun critical negative-branch laboratory, not prove the full Yau 26 proposition or all of `P_4^-`.

# Step 15: Cutoff-smoothing accessibility architecture for the negative branch

Session: S0910A01.  Agent2/Constructor.  Phase: Execute.

## 0. Purpose

This note assembles the full negative-branch obstruction architecture for Yau Problem 26 in dimension four: from near-Einstein closed manifolds without Einstein metrics to a contradiction, conditional on a localized cutoff-flow energy bootstrap.  The main advance over Steps 11–14 is recognizing that:

1. **Calibration is topological, not metric-transport.**  The LeBrun mixed-SW near-saturation profile comes from topology and near-Einstein, not from the specific metric.  A smoothed near-Einstein metric on the same manifold has the same profile.

2. **Volume cancellation makes the Li bootstrap collapse-independent.**  The critical Sobolev product $C_S\|Rm\|_{L^2(B_r)} = O(r^2 K_0^{1/2})$ is small at small fixed $r$, regardless of collapse.

3. **A cutoff flow on the closed manifold freezes bad regions.**  The homogeneity in $E = \operatorname{Ric}+g$ means no collar-injected defect; the global pointwise bound $|E(t)| \le C\delta_i$ survives.

4. **Bounded full curvature after smoothing gives the missing CFG accessibility.**

## 1. Setup

Let $(M_i^4, g_i)$ be a sequence of closed Riemannian 4-manifolds with
$$
\delta_i := \|\operatorname{Ric}_{g_i} + g_i\|_\infty \to 0
$$
and each $M_i$ admitting no Einstein metric.  We take $M_i = X_i \# k_i \overline{\mathbb{CP}}^2$ with $X_i$ a minimal surface of general type, $A_i = c_1^2(X_i) \to \infty$, and $k_i/A_i \to 1/3$ (the LeBrun critical boundary regime).

The established near-boundary profile (Steps 3–8) gives:
$$
\frac{\operatorname{Vol}(M_i)}{A_i} \to \frac{32}{9}\pi^2, \qquad
\frac{J_i}{A_i} \to 0, \qquad
\frac{D_{a,i}}{A_i} \to 0,
$$
and the calibrated curvature profile on the small-defect bulk:
$$
s_i \to -4, \quad |W_i^+|^2 \to \frac{1}{24}, \quad
\operatorname{Spec}(W_i^+) \to \left(-\frac{1}{6}, \frac{1}{12}, \frac{1}{12}\right)
$$
in normalized mean.

## 2. Curvature-energy good set

### 2.1 Global energy bound

**Proposition (Noether energy bound, Step 11).**
$$
\fint_{M_i} |\operatorname{Rm}_{g_i}|^2 \, d\mu_i \le K_{\max}
$$
for a universal constant $K_{\max}$ depending only on the surface type (e.g., $K_{\max} \le 12 + O(A^{-1})$).

### 2.2 Maximal-function selection

Define the local maximal function at scale $R$:
$$
\mathcal{M}_R(f)(p) = \sup_{0 < r \le R} \fint_{B_r(p)} f \, d\mu.
$$
The weak-type $(1,1)$ inequality under $\operatorname{Ric} \ge -3g$ gives:
$$
\operatorname{Vol}\{p : \mathcal{M}_R(|\operatorname{Rm}|^2)(p) > K_0\}
\le \frac{C_n(R)}{K_0} \int_{M_i} |\operatorname{Rm}|^2.
$$
Choose $K_0 = 2C_n(R) K_{\max}$.  Then the **good set** $G_i = \{p : \mathcal{M}_R(|\operatorname{Rm}|^2)(p) \le K_0\}$ satisfies
$$
\frac{\operatorname{Vol}(G_i)}{\operatorname{Vol}(M_i)} \ge \frac{1}{2}.
$$

### 2.3 Good-set packing

By the Vitali 5$r$-covering lemma applied to $G_i$: there exist disjoint balls $B_\rho(p_j^{(i)})$, $j = 1, \ldots, N_i$, with $p_j^{(i)} \in G_i$, $\rho > 0$ fixed, such that
$$
G_i \subset \bigcup_j B_{5\rho}(p_j^{(i)}).
$$
Bishop–Gromov under $\operatorname{Ric} \ge -3g$ gives $\operatorname{Vol}(B_{5\rho})/\operatorname{Vol}(B_\rho) \le C_{BG}(5\rho,\rho)$ (a fixed constant).  Therefore
$$
\sum_j \operatorname{Vol}(B_\rho(p_j^{(i)})) \ge \frac{\operatorname{Vol}(G_i)}{C_{BG}} \ge \frac{\operatorname{Vol}(M_i)}{2C_{BG}}.
$$
The disjoint good balls cover a **definite proportion** of the total volume.

### 2.4 Interior all-centers Li condition

The maximal function at a good point $p_j \in G_i$ controls $\fint_{B_s(p_j)} |\operatorname{Rm}|^2 \le K_0$ for **every** $s \le R$.  In particular, for $s = 4r_*$ where $r_*$ is the Li scale to be chosen.

For any $q \in B_{r_*}(p_j)$ and the covering argument at scale $r_*$: all covering centers $y$ lie within $B_{3r_*/2}(q) \subset B_{5r_*/2}(p_j)$.  At each such $y$:
$$
B_{r_*}(y) \subset B_{7r_*/2}(p_j) \subset B_{4r_*}(p_j).
$$
Therefore $\int_{B_{r_*}(y)} |\operatorname{Rm}|^2 \le \int_{B_{4r_*}(p_j)} |\operatorname{Rm}|^2 \le K_0 \operatorname{Vol}(B_{4r_*}(p_j))$.

Since $B_{4r_*}(p_j) \subset B_{13r_*/2}(y)$ (as $d(p_j,y) \le 5r_*/2$), Bishop–Gromov gives:
$$
\frac{\operatorname{Vol}(B_{4r_*}(p_j))}{\operatorname{Vol}(B_{r_*}(y))}
\le \frac{V_{-1}(13r_*/2)}{V_{-1}(r_*)}
\le C_{\mathrm{BG}}^{\mathrm{local}}
$$
where $C_{\mathrm{BG}}^{\mathrm{local}}$ is a **fixed constant** depending only on the dimension (approximately $(13/2)^4 \approx 1785$ for small $r_*$ in $n = 4$).  The Li dimensionless quantity:
$$
\varepsilon_y(r_*) = r_*^4 \fint_{B_{r_*}(y)} |\operatorname{Rm}|^2
\le r_*^4 \cdot C_{\mathrm{BG}}^{\mathrm{local}} \cdot K_0.
$$
**Choose** $r_* > 0$ so that $r_*^4 \cdot C_{\mathrm{BG}}^{\mathrm{local}} \cdot K_0 \le \varepsilon_{\mathrm{Li}}/2$.  This is possible because $C_{\mathrm{BG}}^{\mathrm{local}}$ and $K_0$ are fixed constants.

Then **for every center** $y$ within $B_{5r_*/2}(p_j)$ (which includes the entire covering neighborhood):
$$
\varepsilon_y(r_*) \le \frac{\varepsilon_{\mathrm{Li}}}{2}.
$$

**This is the decisive calculation.  The Li all-centers condition is automatically satisfied inside the $r_*$-neighborhood of each good point, at the chosen small fixed scale, independently of collapse.  The volume ratio is between comparable balls (radii $r_*$ and $13r_*/2$), not between the macroscopic radius $\rho$ and the microscopic $r_*$.  This bounded ratio is what makes $r_*^4$ the controlling factor.**

## 3. Normalized cutoff flow

### 3.1 Construction

Build a smooth cutoff $\chi_i : M_i \to [0,1]$ with:
- $\chi_i = 1$ on $\bigcup_j B_{\rho/4}(p_j^{(i)})$ (the **plateaux**)
- $\chi_i = 0$ outside $\bigcup_j B_{\rho/2}(p_j^{(i)})$
- $|d\chi_i| \le C/\rho$, $|\nabla^2\chi_i| \le C/\rho^2$

Since the balls $B_\rho(p_j)$ are disjoint, the supports of $\chi_i$ are disjoint.

**Cutoff flow:**
$$
\partial_t g_i = -2\chi_i^2\, E_i(t), \qquad E_i(t) = \operatorname{Ric}_{g_i(t)} + g_i(t), \qquad g_i(0) = g_i.
$$

### 3.2 Key properties

**(a) Exact homogeneity.**  $E = 0 \Rightarrow \partial_t g = 0$.  An exact negative Einstein metric is stationary, even across the transition annulus.

**(b) Frozen bad set.**  On $\{x : \chi_i(x) = 0\}$, $g_i(t) = g_i(0)$.  The curvature on the bad set cannot grow.

**(c) Standard flow on plateaux.**  On $B_{\rho/4}(p_j)$, $\chi_i = 1$ and $\partial_t g = -2E$ — the standard normalized Ricci flow.

**(d) Disjoint support.**  Each ball's flow operates independently.  No cross-contamination between balls.

### 3.3 Short-time existence

On the closed manifold $M_i$, $\partial_t g = -2\chi_i^2(\operatorname{Ric} + g)$ is a quasilinear parabolic system (degenerate where $\chi_i = 0$).  Short-time existence follows from Yang's local Ricci flow theory or from regularizing $\chi_i$ by $\chi_\epsilon = \max(\chi_i, \epsilon)$.  For the regularized flow $\partial_t g = -2\chi_\epsilon^2 E$:
- Uniformly parabolic on all of $M_i$
- On the plateau: coincides with the normalized Ricci flow
- Outside: moves at rate $O(\epsilon^2 \delta_i)$, negligible

## 4. Energy bootstrap on each plateau (conditional)

### 4.1 Volume cancellation in the critical Sobolev product

On a ball $B_{r_*}(q)$ with $\operatorname{Ric} \ge -3g$, the relative Sobolev inequality (Saloff-Coste, Li–Yau) gives, for $f \in C_0^\infty(B_{r_*}(q))$:
$$
\|f\|_{L^4(B_{r_*})}^2 \le C_S(q) \left(\|\nabla f\|_{L^2}^2 + r_*^{-2}\|f\|_{L^2}^2\right)
$$
with $C_S(q) \le C r_*^2 / \operatorname{Vol}(B_{r_*}(q))^{1/2}$.

The critical product:
$$
C_S(q) \cdot \|\operatorname{Rm}\|_{L^2(B_{r_*}(q))}
= \frac{C r_*^2}{\operatorname{Vol}(B_{r_*})^{1/2}} \cdot \operatorname{Vol}(B_{r_*})^{1/2} \left(\fint_{B_{r_*}} |\operatorname{Rm}|^2\right)^{1/2}
= C r_*^2 \left(\fint_{B_{r_*}} |\operatorname{Rm}|^2\right)^{1/2}
\le C r_*^2 (C_{BG} K_0)^{1/2}.
$$

**The volume cancels.**  For $r_*$ small enough, this product is below the Li/Moser bootstrap threshold $\theta$, regardless of how collapsed the ball is.

### 4.2 Li-type energy bootstrap (Conditional Proposition A)

**Conditional Proposition A.**  *On each plateau $B_{\rho/4}(p_j)$, the normalized cutoff flow (which equals the standard normalized Ricci flow there) satisfies, for $0 < t \le T = c r_*^2$:*
$$
\sup_{B_{\rho/8}(p_j)} |\operatorname{Rm}(g_i(t))| \le \frac{C_3}{t}.
$$

**Source basis:** Li's Theorem 3.4 and proof (lines 219–258 of object.md) propagate the $L^2$ energy bootstrap using:
1. The all-centers initial condition: $\sup_{q \in B_{\rho/4}} \|Rm(0)\|_{L^2(B_{r_*}(q))} \le [C_1 A_0]^{-1}$ — guaranteed by Section 2.4.
2. The bounded covering: $B_{2r_*}(q) \subset \cup_{i=1}^N B_{r_*}(y_i)$ with $N$ bounded by Ricci comparison — available.
3. The critical absorption: $\int |Rm|^3 \le \theta (\int |\nabla |Rm||^2 + r_*^{-2}\int|Rm|^2)$ with $\theta$ small from the volume-cancelling product — Section 4.1.
4. Moser iteration from $L^2$ to $L^\infty$: standard once the $L^2$ bootstrap closes.

**What remains to prove:** Li's proof uses the normalized energy supremum over all centers of the CLOSED manifold, with a continuation argument.  Here, we need a **local version** restricted to centers in the plateau, handling the cutoff boundary.  The main technical issue: curvature information from outside the plateau (bad set or transition) cannot leak in because:
- The bad set is frozen ($\chi = 0$)
- The transition collar has $|dg/dt| = O(|d\chi|^2 \delta_i^2)$, contributing $O(\rho^{-2}\delta_i^2 t)$ to the curvature change, which is negligible for $\delta_i$ small.

The covering argument for centers in $B_{\rho/8}(p_j)$ uses only balls inside $B_{\rho/4}(p_j)$ (since $2r_* \ll \rho$), so it stays entirely on the plateau.

### 4.3 Einstein defect propagation

**Proposition B (defect propagation, conditional on Proposition A).**

$|E_i(t)| \le C\delta_i$ on all of $M_i$ for $0 \le t \le T$.

**Proof sketch:**
- On $\{\chi_i = 0\}$: $g_i(t) = g_i(0)$, so $|E_i(t)| = |E_i(0)| \le \delta_i$.
- On the transition and plateau: $E_i$ satisfies $(\partial_t - \chi^2\Delta)|E_i| \le \chi^2 \cdot 2|Rm||E_i| + C|d\chi||\nabla E_i| + C|\nabla^2\chi||E_i|$.
  - On the plateau: Kato gives $(\partial_t - \Delta)|E| \le 2|Rm||E|$.  With $|Rm| \le C/t$ from Prop A, $|E| = |E_0| \cdot e^{2C\int_0^t s^{-1}ds}$ — but this diverges logarithmically.

**Correction: use Li's Corollary 3.5 instead.**  The defect $|E|$ is a curvature-potential subsolution:
$$
(\partial_t - \Delta)|E| \le c_0 |\operatorname{Rm}| \cdot |E|.
$$
Li's Corollary 3.5 (lines 260–272), applied with $f = |\operatorname{Rm}|$ and $u = |E|$, gives
$$
|E(x,t)| \le C_1 A^{2/3} t^{-2/3} \left(\int_{B_{3r_*}(x)} |E(0)|^3\right)^{1/3}
$$
where $A = C_S = O(r_*^2/\operatorname{Vol}^{1/2})$.  Since $|E(0)| \le \delta_i$:
$$
\left(\int_{B_{3r_*}} |E(0)|^3\right)^{1/3} \le \delta_i \operatorname{Vol}(B_{3r_*})^{1/3}.
$$
The volume-cancellation:
$$
A^{2/3} \operatorname{Vol}(B_{3r_*})^{1/3}
= \left(\frac{Cr_*^2}{\operatorname{Vol}^{1/2}}\right)^{2/3} \operatorname{Vol}^{1/3}
= C r_*^{4/3}.
$$
Therefore:
$$
\boxed{|E_i(x,t)| \le C \delta_i r_*^{4/3} t^{-2/3} = C\delta_i \left(\frac{r_*^2}{t}\right)^{2/3}}
$$
for $0 < t \le T = cr_*^2$.  At the target time $t_0 = \theta r_*^2$:
$$
|E_i(x, t_0)| \le C_\theta \delta_i.
$$

**The volume cancels again.  The defect bound is uniform in collapse.**

Metric drift:
$$
\left|\log\frac{g_i(t)(v,v)}{g_i(0)(v,v)}\right|
\le 2\int_0^t |E_i(\tau)| d\tau
\le C\delta_i r_*^{4/3} \cdot 3t^{1/3}
= O(\delta_i r_*^2) \to 0.
$$
So $g_i(t_0)$ is uniformly bilipschitz to $g_i(0)$.

## 5. Calibration recovery from topology

### 5.1 The calibrated profile is topological

The LeBrun mixed Seiberg-Witten estimate
$$
\frac{1}{4\pi^2}\int_{M_i}\left(\frac{s^2}{24} + 2|W^+|^2\right) d\mu \ge \frac{2}{3}(a^+)^2
$$
and the Chern-Gauss-Bonnet identity $I - J = A - k$ depend on:
- The smooth topology of $M_i$ (for $\chi, \tau, c_1^2$)
- The Seiberg-Witten invariants (topological for 4-manifolds)
- The metric only through its curvature integrals

**Key observation:** these integrals are computed for *any* smooth metric on $M_i$.  If $g_i(t_0)$ is a smooth metric on $M_i$ with $\|\operatorname{Ric}_{g_i(t_0)} + g_i(t_0)\|_\infty \le C_\theta \delta_i$, then:

$$
J_i(t_0) = \frac{1}{4\pi^2}\int_{M_i} \frac{|\mathring{\operatorname{Ric}}_{g_i(t_0)}|^2}{2} d\mu_{t_0}
\le \frac{C\delta_i^2}{4\pi^2} \operatorname{Vol}(M_i, g_i(t_0))
= O(\delta_i^2 A_i).
$$

Since $M_i = X_i \# k_i\overline{\mathbb{CP}}^2$ with $k_i/A_i \to 1/3$:
$$
I_i(t_0) = (A_i - k_i) + J_i(t_0) = \frac{2}{3}A_i + o(A_i).
$$
The monopole sign selection still gives $(a^+)^2 \ge A_i$, so:
$$
D_{a,i}(t_0) = I_i(t_0) - \frac{2}{3}(a^+)^2 \le J_i(t_0) - (k_i - A_i/3) - \frac{2}{3}((a^+)^2 - A_i) = o(A_i).
$$
The same Cauchy-Schwarz remainder gives:
$$
\int_{M_i} \left(s_{g_i(t_0)} + 8\sqrt{6}|W_{g_i(t_0)}^+|\right)^2 d\mu_{t_0} \le 864\pi^2 D_{a,i}(t_0) = o(A_i).
$$

**Therefore the metric $g_i(t_0)$ has the same calibrated curvature profile as $g_i(0)$, recovered entirely from topology and near-Einstein condition, without any time-comparison of $W^+$.**

### 5.2 Calibrated defect is still $o(\operatorname{Vol})$

The global mean calibrated defect
$$
\fint_{M_i} F_{g_i(t_0)} d\mu_{t_0} = \fint_{M_i} \left(s + 8\sqrt{6}|W^+|\right)^2 d\mu_{t_0} = o(1)
$$
since $D_{a,i}(t_0) = o(A_i)$ and $\operatorname{Vol}(M_i, g_i(t_0)) \sim \operatorname{Vol}(M_i, g_i(0)) = O(A_i)$.

## 6. Chart accessibility on the smoothed plateaux

### 6.1 Bounded curvature on definite volume

From Proposition A: on each plateau $B_{\rho/8}(p_j)$, at time $t_0 = \theta r_*^2$:
$$
|\operatorname{Rm}(g_i(t_0))| \le \frac{C_3}{t_0} = \frac{C_3}{\theta r_*^2} =: \Lambda.
$$
The total volume of the plateaux is:
$$
\sum_j \operatorname{Vol}(B_{\rho/8}(p_j), g_i(t_0))
\ge c \sum_j \operatorname{Vol}(B_\rho(p_j), g_i(0))  \quad \text{(bilipschitz)}
\ge c' \operatorname{Vol}(M_i).
$$

### 6.2 CFG structure from bounded curvature

On each plateau ball $(B_{\rho/8}(p_j), g_i(t_0))$ with $|\operatorname{Rm}| \le \Lambda$ and $\operatorname{Ric} \ge -(1+C_\theta\delta_i)g$:

By Cheeger-Fukaya-Gromov theory: for every $v > 0$, points with $\operatorname{Vol}(B_1(p)) \ge v$ have harmonic radius $\ge r_h(v, \Lambda) > 0$.  If noncollapsed (which bounded curvature gives on the local universal cover): the cover has injectivity radius $\ge i_0(\Lambda, v)$ and admits harmonic charts.

More precisely: on a ball with $|Rm| \le \Lambda$, the local universal cover at scale $R = \min(\rho/8, i_0)$ has the SAME curvature bound, and CFG theory gives a nilpotent frame structure.  Naber-Zhang Proposition 6.4, in the setting of bounded FULL curvature (not just Ricci), gives harmonic radius control on the local universal cover under appropriate residual-dimension and rank conditions.

**With bounded sectional curvature after smoothing, the harmonic-radius control that was previously unavailable under only bounded Ricci now follows from standard theory.**

### 6.3 Derdziński contradiction on the smoothed metric

For the smoothed metric $g_i(t_0)$ on a noncollapsed cover chart:
- $|\operatorname{Ric}_{g_i(t_0)} + g_i(t_0)| \le C_\theta\delta_i \to 0$ (Proposition B)
- The finite-$p$ ($p > 4$) harmonic-coordinate convergence (Step 8 passage) applies
- The limit germ is a smooth Einstein metric with $\operatorname{Ric} = -g$
- The calibrated $W^+$ profile from Section 5 passes to the limit
- Derdziński Proposition 5 forbids the calibrated constant-two-eigenvalue spectrum

**This is the same Derdziński contradiction as in Step 8, but now on the SMOOTHED metric where chart accessibility is guaranteed by bounded curvature.**

## 7. Volume contradiction

The chart-accessible exclusion theorem (Step 11, Theorem 1) proves:

> For every fixed chart-control parameter $(h,v)$, the volume proportion of $(h,v)$-chart-accessible points must vanish:
> $$\frac{\operatorname{Vol}\{p \in M_i : p \text{ is }(h,v)\text{-accessible for }g_i(t_0)\}}{\operatorname{Vol}(M_i, g_i(t_0))} \to 0.$$

But the smoothed plateaux supply chart-accessible points on a **definite volume proportion** $\ge c' > 0$ (Section 6.1–6.2).

**Contradiction.**

## 8. Exact remaining analytic object

The full architecture above is conditional on **Proposition A** (Section 4.2): the localized Li-type energy bootstrap on the plateau of the cutoff flow.

What it requires:
1. Short-time existence for $\partial_t g = -2\chi^2 E$ on the closed manifold (established by Yang's LRF theory or regularization).
2. The all-centers Li condition on the interior plateau at scale $r_*$ (established by Section 2.4).
3. A local version of Li's energy bootstrap (Theorem 3.4) restricted to centers inside the plateau, with the covering argument using only interior balls.
4. Independence from the frozen exterior and transition collar.

What is NOT required:
- Any circle or torus symmetry of the original metrics
- Noncollapse of the original metrics
- Exact Weyl data transport through the flow
- Explicit classification of the collapse mode

**The gap between Li's published all-centers theorem and the needed local plateau version is the precise remaining analytic object for a rigorous proof.**

## 9. Comparison with existing sources

### 9.1 Li's proof structure supports localization

Li's Theorem 3.4 proof (lines 228–258) tracks $e_0 = \sup_x \|Rm\|_{L^2(B_r(x))}$ and uses:
- Bounded covering: $B_{2r}(x) \subset \cup_i B_r(y_i)$ with $N$ bounded — works locally.
- Continuity of $e_0(t)$ — works locally on the plateau.
- The critical absorption uses $A \cdot e_0 < (3C_0)^{-1}$ — assured by volume cancellation.

The global supremum in Li's proof is there to prevent energy leaking IN from uncontrolled regions.  On the plateau of the cutoff flow, there IS no uncontrolled region nearby: the cutoff freezes the exterior, and the covering stays inside the buffer.

### 9.2 Wang's LRF gives partial confirmation

Wang (Proposition 3.12) shows that LRF with local Sobolev + critical norm + $L^p$ Ricci gives near-Euclidean structure.  The key hypothesis is $|Rm|_{n/2} \le \beta/A_0^2$ where $A_0$ is the Sobolev constant.  In 4D, $n/2 = 2$, so this is $\|Rm\|_{L^2} \le \beta/A_0^2 = \beta \operatorname{Vol}^{1/2}/(Cr_*^2)^2 = \beta\operatorname{Vol}^{1/2}/(Cr_*^4)$.  But $\|Rm\|_{L^2} = \operatorname{Vol}^{1/2}(\fint|Rm|^2)^{1/2}$, so the condition becomes $K_0^{1/2} \le \beta/(Cr_*^4)$, or $r_*^4 \le \beta/(CK_0^{1/2})$.  This is satisfied by our choice of $r_*$.

### 9.3 A03's defect propagation

A03's corrected note (step14_cutoff_smoothing_and_cor35_reconstruction.md) independently derives the $C\delta r_*^{4/3} t^{-2/3}$ defect estimate using Li's Corollary 3.5.  The volume cancellation in the $A^{2/3}\operatorname{Vol}^{1/3}$ product is the same mechanism as in Section 4.1.  A03 also recorded the $\phi^2$ textual issue in Corollary 3.5 and the normalized-to-unnormalized conversion.

## 10. Status

| Component | Status |
|-----------|--------|
| Good-set packing, definite volume | **Established** (maximal function + Vitali + Bishop-Gromov) |
| Interior all-centers Li condition | **Established** (Section 2.4, the key new calculation) |
| Volume cancellation in critical product | **Established** (4D, $C_S\|Rm\|_{L^2}$ is scale-invariant) |
| Cutoff flow existence | **Established** (Yang's LRF theory or regularization) |
| Cutoff flow homogeneity in $E$ | **Established** (A03 Section 4, algebraic) |
| Plateau energy bootstrap (Prop A) | **Conditional** — needs local version of Li's Thm 3.4 |
| Defect propagation (Prop B) | **Conditional on Prop A** — follows from Li's Cor 3.5 |
| Calibration recovery from topology | **Established** (same manifold, same near-Einstein, same CW/SW) |
| CFG accessibility from bounded curvature | **Established** (standard Cheeger-Gromov theory) |
| Derdziński contradiction | **Established** (Steps 7-8, primary source verified) |
| Volume contradiction | **Follows from** all above components |

## 11. Evidence paths

- This note: `workspace/notes/step15_cutoff_smoothing_architecture.md`
- Li source: `Knowledge/objects/papers/0911.3104-Smoothing-Riemannian-Metrics-with-Bounded-Ricci-Curvatures-in--fc5404da6e14--415cdf5be1eb/object.md`
- Wang source: `Knowledge/objects/papers/Pseudolocality-of-Ricci-Flow-under-Integral-Bound-of-Curvature--ca47a7c773f9--79daf5157f68/object.md`
- A03 cutoff analysis: `Sessions/S0910A03/workspace/notes/step14_cutoff_smoothing_and_cor35_reconstruction.md`
- Step 14 comparison: `workspace/notes/step14_smoothing_vs_reduction_route.md`
- Chart-accessibility theorem: `workspace/notes/step11_chart_accessibility_and_energy.md`
- Derdziński measure-local theorem: `workspace/notes/step8_derdzinski_measure_local_theorem.md`
- Noether energy: `workspace/scripts/step11_noether_energy_bound.py`

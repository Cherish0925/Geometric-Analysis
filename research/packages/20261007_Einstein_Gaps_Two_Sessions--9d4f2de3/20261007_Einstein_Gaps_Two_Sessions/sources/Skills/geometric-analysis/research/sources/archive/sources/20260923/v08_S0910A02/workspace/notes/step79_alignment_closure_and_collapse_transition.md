# Step 79: Harmonic-form alignment closure and the collapse transition theorem

Session `S0910A02`. Agent2 / Constructor. Phase Execute.

## Purpose

This note establishes two results for the four-dimensional positive branch $P_4^+$ of Yau--26:

1. The **precise closure** of the proposed summed Weitzenböck/harmonic-form mechanism: it cannot produce a new positive Einstein nonexistence obstruction on the mixed rows, for structural reasons that locate the exact frontier.

2. The **transition-scale theorem** for the collapse branch: Bishop--Gromov monotonicity provides the controlled-annulus ingredient identified as missing in Step 75, yielding a rigorous outermost-model classification for collapsing near-Einstein sequences.

These two results replace the local desingularization route (closed in Step 78 as non-decisive) and the integral Weyl-energy route (closed here) with a sharply formulated collapse-front opening.

---

## 1. Precise closure of the harmonic-form alignment mechanism

### 1.1. Statement of the proposed mechanism

The proposal (Strategist, Step 78): for a positive Einstein 4-manifold $(M^4,g)$ with $b_+(M) = 3$, the three independent harmonic self-dual forms $\omega_1,\omega_2,\omega_3$ each satisfy the Weitzenböck inequality
$$\int |\nabla\omega_a|^2 + \frac{s}{3}\int|\omega_a|^2 = 2\int W^+(\omega_a,\omega_a)\,dV,$$
forcing $\int W^+(\omega_a,\omega_a) \ge \frac{s}{6}\int|\omega_a|^2 > 0$ for each $a$. Since $\mathrm{tr}\,W^+ = 0$, at most two eigenvalues of $W^+$ can be positive at any point, and three independent forms all needing positive $W^+$-pairing should create a geometric squeeze.

Source: Wu/LeBrun Weitzenböck formula (line 141 of the Einstein--Self-Dual--Weyl--Conformally-Kähler Knowledge object).

### 1.2. Why the mechanism fails

**All classical estimates are lower bounds.** The Gursky positive-Yamabe bound gives $\int|W^+|^2 \ge \frac{4\pi^2(2\chi+3\tau)}{3} = \frac{64\pi^2}{3}$ for the $\chi=8,\tau=0$ rows. The Gursky--LeBrun positive-Einstein bound gives $\int|W^+|^2 \ge \int s^2/24$. The Bishop bound $\lambda^2V \le 24\pi^2$ combined with CGB gives $\int|W^\pm|^2 \ge 24\pi^2$. These are all *lower bounds* on Weyl energy. The CGB identity $\int|W^\pm|^2 = 32\pi^2 - \lambda^2V/3$ supplies an *upper bound* of $32\pi^2$, but the resulting range $\int|W^\pm|^2 \in [24\pi^2,\, 32\pi^2]$ is nonempty and unconstrained. A contradiction would require an a priori *upper bound* on Weyl energy sharper than $32\pi^2$, which no available tool provides.

Verified: `workspace/data/step79_transition_constants_verify.json`.

**The three-lump concentration is realizable.** The three harmonic self-dual forms cannot be pointwise proportional (closedness + Aronszajn) or disjointly supported (unique continuation). However, they CAN concentrate in three separate regions of the manifold with exponentially small tails. On $\#_3(S^2\times S^2)$ with thin connect-sum necks, each $H^2_+$-generator concentrates on one $S^2\times S^2$ piece and decays exponentially through the necks. A positive Einstein metric produced by Ozuch-type orbifold desingularization — if it exists — would have exactly this structure near the four $A_1$ nodes. The Weitzenböck integral is then replicated in three separate regions of the manifold, each contributing $\sim\frac{s}{6}\int|\omega_a|^2$ independently, with no cross-interference. This means the summed inequality $\sum_a\int W^+(\omega_a,\omega_a) \ge \frac{s}{6}\sum_a\int|\omega_a|^2$ does not produce tighter constraints than the single-form inequality.

**The $\det W^+$ regime is complementary.** With $b_+ \ge 2$, two independent harmonic self-dual forms must each have positive $W^+$-pairing on average. Generically, this forces two positive eigenvalues $\alpha \ge \beta > 0$ of $W^+$ at most points, with $\gamma = -\alpha-\beta < 0$. Then $\det W^+ = \alpha\beta\gamma < 0$, precisely the complement of the $\det W^+ > 0$ hypothesis in Wu/LeBrun's Theorem 2.1 (line 148 of the Knowledge object). Wu's theorem states that $\delta W^+ = 0$ plus $\det W^+ > 0$ forces conformally Kähler structure, which in turn forces $b_+ = 1$ (Proposition 2.2, line 181). So $b_+ \ge 2$ pushes $\det W^+$ into the opposite sign, and the entire conformally-Kähler classification machinery loses its input.

### 1.3. The frontier statement

The known-example pattern $\min(b_+,b_-) \le 1$ among simply connected compact positive Einstein 4-manifolds is fully explained by the current classification: all known examples are either symmetric ($S^4$, $\mathbb{CP}^2$, $S^2\times S^2$) or conformally Kähler (del Pezzo surfaces $\mathbb{CP}^2\#k\overline{\mathbb{CP}}^2$, $0\le k\le 8$, plus the Page and Chen--LeBrun--Weber non-Kähler Hermitian metrics, all having $b_+ = 1$ in the Kähler orientation).

Source: LeBrun 2024 lecture notes (staging/acquired/Einstein\_Metrics\_Four-Manifolds), Propositions 2.2--2.3 of the Wu/LeBrun source, LeBrun--Ozuch admissible sequence theory.

The frontier: $P_4^+$ requires the existence of positive Einstein metrics with $\min(b_+,b_-) \ge 2$ that are non-conformally-Kähler in both orientations. No known construction produces such metrics; no known obstruction excludes them. Both the proof hemisphere and the refutation hemisphere require new mathematics on this family, and no rearrangement of Weyl integrals will decide it.

---

## 2. The transition-scale theorem

This theorem provides the controlled-annulus ingredient for the collapse branch of $P_4^+$, resolving the gap identified in Step 75.

### 2.1. Setup and definition

Let $(M^n,g)$ be a closed Riemannian $n$-manifold with $\mathrm{Ric}_g \ge (n-1)\kappa g$ for some $\kappa > 0$. By the Bishop--Gromov monotonicity theorem, the volume ratio
$$\Theta(x,r) := \frac{\mathrm{Vol}_g(B(x,r))}{V_{n,\kappa}(r)}$$
is nonincreasing in $r \in (0,\infty)$, where $V_{n,\kappa}(r)$ is the volume of a geodesic ball of radius $r$ in the simply connected model space form $M^n_\kappa$ of constant sectional curvature $\kappa$.

We have $\lim_{r\to 0^+}\Theta(x,r) = 1$ (smooth manifold) and $\Theta(x,D) = V(M)/V_{n,\kappa}(D)$ for $D \ge \mathrm{diam}(M,g)$.

**Definition.** For $\epsilon \in (0,1)$, the *transition scale* at $x$ is
$$\rho_\epsilon(x) := \sup\bigl\{r > 0 : \Theta(x,r) \ge \epsilon\bigr\}.$$

By monotonicity of $\Theta$ and the boundary values ($\Theta(\cdot,0^+)=1$, $\Theta(\cdot,D) \le V/V_{n,\kappa}(D)$):

- $\rho_\epsilon(x) > 0$ for all $x$ (since $\Theta(x,\cdot)$ starts at 1);
- $\rho_\epsilon(x) \le D$ whenever $V(M)/V_{n,\kappa}(D) < \epsilon$;
- for $r \le \rho_\epsilon(x)$: $\Theta(x,r) \ge \epsilon$;
- for $r > \rho_\epsilon(x)$: $\Theta(x,r) \le \epsilon$.

### 2.2. Statement

**Theorem (Outermost Transition).** Let $(M_i^n, g_i)$ be a sequence of closed Riemannian $n$-manifolds with
$$\mathrm{Ric}_{g_i} \ge (n-1)\kappa\, g_i,\qquad \kappa > 0,\qquad V(M_i,g_i) \to 0.$$
For any $\epsilon \in (0,1)$, there exist points $p_i \in M_i$ and scales $\rho_i \to 0^+$ such that the rescaled pointed sequence $\bigl(M_i,\, \tilde g_i := \rho_i^{-2}g_i,\, p_i\bigr)$ satisfies:

**(a) Noncollapsing at unit scale.** $\mathrm{Vol}_{\tilde g_i}(B_{\tilde g_i}(p_i,1)) \to \epsilon\,\omega_n$ as $i \to \infty$.

**(b) Collapse at all larger scales.** For every fixed $R \ge 1$:
$$\frac{\mathrm{Vol}_{\tilde g_i}\bigl(B_{\tilde g_i}(p_i,R)\bigr)}{\omega_n R^n} \le \epsilon.$$
(Since $V_{n,\kappa}(t) \le \omega_n t^n$ for $\kappa > 0$, the correction factor is $\le 1$, not $\ge 1$.)

**(c) Ricci decay (requires two-sided control).** Under the one-sided hypothesis $\mathrm{Ric} \ge (n-1)\kappa g$ alone, the rescaled Ricci satisfies only $\mathrm{Ric}_{\tilde g_i} \ge (n-1)\kappa\rho_i^2\,\tilde g_i \to 0$ as a lower bound. **The upper bound does not follow**: shrinking round spheres $(S^4, t_i^2 g_{\mathrm{rd}})$ satisfy fixed positive Ricci, $V \to 0$, and $\rho_i \asymp t_i$, but the transition-scale rescaling recovers a fixed round sphere, not a Ricci-flat limit.

In the **near-Einstein** application ($\|\mathrm{Ric}_{g_i} - g_i\|_{\mathrm{op}} \le \delta_i \to 0$), both sides are controlled: $|\mathrm{Ric}_{\tilde g_i}|_{\tilde g_i} = \rho_i^2|\mathrm{Ric}_{g_i}|_{g_i} \le (1+\delta_i)\rho_i^2 \to 0$, so the rescaled Ricci converges to zero uniformly.

**(d) Volume ratio bound on any limit.** By Cheeger--Colding, a subsequence converges in pointed measured GH sense to a noncollapsed RCD$(0,n)$ space $(X_\infty, d_\infty, p_\infty)$. Volume continuity gives
$$\frac{\mathrm{Vol}(B(p_\infty,R))}{\omega_n R^n} \le \epsilon \qquad \text{for all } R \ge 1.$$
If $X_\infty$ is noncompact, $\mathrm{AVR}(X_\infty) \le \epsilon$. **Warning**: the limit may be compact (as in the shrinking-sphere example); noncompactness requires the near-Einstein condition or another argument excluding diameter proportional to $\rho_i$.

**(e) ALE dichotomy (dimension 4).** If the limit is a smooth noncompact ALE 4-manifold asymptotic to $\mathbb{R}^4/\Gamma$, then $\mathrm{AVR} = 1/|\Gamma|$, hence $|\Gamma| \ge 1/\epsilon$.

### 2.3. Proof

**Scale existence and decay.** Choose $p_i \in M_i$ maximizing $\rho_\epsilon$ over $M_i$, and set $\rho_i := \rho_\epsilon(p_i)$. Then $\rho_\epsilon(x) \le \rho_i$ for all $x \in M_i$.

Claim: $\rho_i \to 0$. If not, $\rho_i \ge c > 0$ along a subsequence. By definition, $\Theta(p_i,c) \ge \epsilon$, so $V_{g_i}(B(p_i,c)) \ge \epsilon V_{n,\kappa}(c)$. But $V(M_i) \ge V_{g_i}(B(p_i,c)) \ge \epsilon V_{n,\kappa}(c) > 0$, contradicting $V(M_i) \to 0$. $\square$

**Part (a).** $\mathrm{Vol}_{\tilde g_i}(B_{\tilde g_i}(p_i,1)) = \rho_i^{-n}\mathrm{Vol}_{g_i}(B_{g_i}(p_i,\rho_i))$. By the definition of $\rho_i$: $\mathrm{Vol}_{g_i}(B_{g_i}(p_i,\rho_i)) \ge \epsilon V_{n,\kappa}(\rho_i)$. For small $\rho_i$: $V_{n,\kappa}(\rho_i) = \omega_n\rho_i^n(1 - C_n\kappa\rho_i^2 + O(\rho_i^4))$. So $\mathrm{Vol}_{\tilde g_i}(B_{\tilde g_i}(p_i,1)) \ge \epsilon\omega_n(1 - C_n\kappa\rho_i^2) =: \epsilon'\omega_n$ with $\epsilon' \to \epsilon$ as $i \to \infty$.

**Part (b).** For $R \ge 1$, the ball $B_{g_i}(p_i,R\rho_i)$ has $R\rho_i > \rho_i$, so $\Theta(p_i,R\rho_i) \le \epsilon$:
$$V_{g_i}(B_{g_i}(p_i,R\rho_i)) \le \epsilon V_{n,\kappa}(R\rho_i).$$
Since $\kappa > 0$: $V_{n,\kappa}(t) \le \omega_n t^n$ for all $t > 0$ (the sphere has smaller balls than Euclidean space). Therefore
$$\mathrm{Vol}_{\tilde g_i}(B_{\tilde g_i}(p_i,R))/(\omega_n R^n) = \rho_i^{-n}V_{g_i}(B(p_i,R\rho_i))/(\omega_n R^n) \le \epsilon V_{n,\kappa}(R\rho_i)/(\omega_n(R\rho_i)^n) \le \epsilon.$$

**Part (c).** Under $\mathrm{Ric}_{g_i} \ge (n-1)\kappa g_i$ only: $\mathrm{Ric}_{\tilde g_i} \ge (n-1)\kappa\rho_i^2\tilde g_i \to 0$ (lower bound only). The upper bound requires additional hypothesis. In the near-Einstein case $|\mathrm{Ric}_{g_i} - g_i| \le \delta_i$: the operator norm scales as $|\mathrm{Ric}_{\tilde g_i}|_{\tilde g_i} = \rho_i^2|\mathrm{Ric}_{g_i}|_{g_i} \le (1+\delta_i)\rho_i^2 \to 0$.

**Part (d).** The pointed sequence has Ric lower bound $\to 0$ and unit-ball volume $\to \epsilon\omega_n > 0$. Cheeger--Colding gives a pointed measured GH limit $(X_\infty,d_\infty,\mathcal{H}^n,p_\infty)$. Colding's volume continuity gives $\mathcal{H}^n(B(p_\infty,R)) \le \epsilon\omega_nR^n$ for a.e. $R \ge 1$; monotonicity extends to all $R$.

**Part (e).** For a smooth ALE 4-manifold asymptotic to $\mathbb{R}^4/\Gamma$: $\mathrm{AVR} = 1/|\Gamma|$. Combined with (d): $1/|\Gamma| \le \epsilon$, so $|\Gamma| \ge 1/\epsilon$. $\square$

### 2.4. Maximality corollary

Since $p_i$ was chosen to maximize $\rho_\epsilon$ over $M_i$, every other point $x \in M_i$ has $\rho_\epsilon(x) \le \rho_i$. After rescaling, for any $y \in (M_i,\tilde g_i)$ and $R \ge 1$:
$$\frac{\mathrm{Vol}_{\tilde g_i}(B(y,R))}{\omega_n R^n} \le \epsilon(1 + o(1)).$$
Therefore the entire rescaled manifold is $\epsilon$-collapsed at scale $\ge 1$, and $p_i$ is the most noncollapsed point.

---

## 3. Four-dimensional positive collapse: first consequences

### 3.1. Chern--Weil energy concentration

For a near-Einstein sequence $(M^4,g_i)$ with $\|\mathrm{Ric}_{g_i} - g_i\|_{\mathrm{op}} \le \delta_i \to 0$ and $V_i \to 0$:
$$\int_{M}|W_{g_i}|^2\,dV_{g_i} = 8\pi^2\chi - \frac{s_i^2V_i}{24} + O(\delta_i^2V_i) \to 8\pi^2\chi.$$
For $\chi = 8$: $\int|W|^2 \to 64\pi^2$. For $\tau = 0$: each chirality $\to 32\pi^2$.

The Weyl energy cannot live in the collapsed bulk (where bounded curvature and $V \to 0$ kill all integrals). It must concentrate into finitely many curvature-concentration points, each producing a Ricci-flat bubble after rescaling.

### 3.2. Outermost model classification

The transition-scale theorem provides the first rigorous layer. The outermost bubble at $p_i$ is a complete noncollapsed Ricci-flat 4-manifold (in the Cheeger--Naber sense: smooth away from finitely many orbifold points) with $\mathrm{AVR} \le \epsilon$. For any $\epsilon > 0$:

| Model | AVR | Conclusion |
|---|---|---|
| **ALE** with group $\Gamma$ | $1/|\Gamma|$ | $|\Gamma| \ge 1/\epsilon$; chirality energy $8\pi^2\chi_{\mathrm{ALE}} = 8\pi^2(1+\mathrm{rank})$ |
| **ALF** (multi-Taub-NUT, Atiyah--Hitchin) | $0$ | volume growth $\sim cR^3$; Euler $\chi_{\mathrm{ALF}} = k_{\mathrm{NUT}}$ |
| **ALG** | $0$ | volume growth $\sim cR^2$ |
| **ALH** | $0$ | volume growth $\sim cR$ |

For a sequence converging to the outermost bubble, the $\epsilon$ can be taken arbitrarily small (diagonal argument), so:

For a fixed $\epsilon$, the outermost model has volume ratio $\le \epsilon$ at all large scales; if ALE, $|\Gamma| \ge 1/\epsilon$. **Warning** (TTCS correction): taking $\epsilon \to 0$ changes $p_i$ and $\rho_i$, so a simple diagonal argument does not produce a fixed model with $\mathrm{AVR} = 0$. What it shows is that for any desired level of collapse, the outermost model has at most that volume ratio.

### 3.3. ALE exclusion from the CGB energy budget

**Proposition (ALE Exclusion).** For $\epsilon < 1/48$, in the setting of the Transition-Scale Theorem applied to a collapsing near-positive-Einstein sequence on a $\chi = 8$ mixed row, the outermost Ricci-flat bubble model cannot be a hyper-Kähler ALE 4-manifold.

**Proof.** The CGB energy of the compact manifold satisfies $\int_M|W|^2 \to 8\pi^2\chi = 64\pi^2$ as $V \to 0$. Each ALE bubble at scale $\rho_j$ absorbs a definite Weyl energy: for a hyper-Kähler ALE resolution of $\mathbb{C}^2/\Gamma$ (ADE classification by Kronheimer), with rank $r$ and $\chi_{\mathrm{top}} = r+1$, the Hitchin--Nakajima CGB formula gives
$$\int_{\mathrm{ALE}}|W|^2 = 8\pi^2\!\left(\chi_{\mathrm{top}} - \frac{1}{|\Gamma|}\right).$$
The outermost bubble must carry energy $\le 64\pi^2$, so $\chi_{\mathrm{top}} - 1/|\Gamma| \le 8$, hence $\chi_{\mathrm{top}} \le 8$ (since $1/|\Gamma| > 0$), and rank $r \le 7$.

Among all ADE groups with rank $r \le 7$, the maximum group order is:
| Type | Rank | $|\Gamma|$ | $\chi_{\mathrm{top}}$ | Energy/$\pi^2$ | Fits? |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $E_7$ | 7 | 48 | 8 | 63.83 | ✓ |
| $E_6$ | 6 | 24 | 7 | 55.67 | ✓ |
| $D_7$ | 7 | 20 | 8 | 63.60 | ✓ |
| $A_7$ | 7 | 8 | 8 | 63.00 | ✓ |
| $E_8$ | 8 | 120 | 9 | 71.93 | ✗ |
| $A_8$ | 8 | 9 | 9 | 71.11 | ✗ |

The maximum feasible $|\Gamma|$ is **48** (type $E_7$). The transition-scale theorem gives $|\Gamma| \ge 1/\epsilon$. For $\epsilon < 1/48$: $|\Gamma| > 48$, exceeding all feasible ADE groups. $\square$

Verified: `workspace/data/step79_ale_exclusion.json`.

**Chiral refinement (TTCS Branch 2 observation).** A hyper-Kähler ALE 4-manifold is (anti-)self-dual: $W^- = 0$, so all Weyl energy lives in one chirality. Since $\int|W^\pm|^2\,dV$ is conformally invariant and decomposes additively across bubbles (up to vanishing neck energy), each bubble's chirality energy is bounded by the total chirality budget. For the $\chi = 8$, $\tau = 0$ balanced rows:
$$\int_M|W^\pm|^2 \to 32\pi^2 \quad\text{(each chirality)}.$$
A hyper-Kähler ALE bubble then satisfies $8\pi^2(\chi_{\mathrm{top}} - 1/|\Gamma|) \le 32\pi^2$, giving $\chi_{\mathrm{top}} \le 4$ and rank $\le 3$. The maximum feasible $|\Gamma|$ drops from 48 to **4** (type $A_3$, energy $30\pi^2 < 32\pi^2$; $D_4$ has rank 4, energy $39\pi^2 > 32\pi^2$).

**For the balanced rows and $\epsilon < 1/4$, no hyper-Kähler ALE can be the outermost model.**

For the non-balanced rows ($\tau = \pm 2$), the chirality budgets are $(20\pi^2, 44\pi^2)$, giving the weaker outermost bubble bound $|\Gamma| \le 8$ (type $D_4$ in the larger chirality). The chiral assignment depends on the bubble's orientation relative to the ambient manifold.

**Consequence.** Under collapse of near-positive-Einstein metrics on the $\chi = 8$ mixed rows, the outermost model at any $\epsilon < 1/48$ **cannot be a smooth Kronheimer hyper-Kähler ALE 4-manifold** (ADE classified). Inner ALE bubbles at deeper scales remain possible within the residual energy.

**Remaining gap.** The exclusion is proved for ADE/Kronheimer ALE. Non-hyper-Kähler Ricci-flat ALE 4-manifolds (with $\Gamma \subset SO(4) \setminus SU(2)$) are not covered by the ADE table. The CGB formula $\int|W|^2 = 8\pi^2(\chi - 1/|\Gamma|)$ applies to ALL smooth ALE spaces, but the $\chi$-$|\Gamma|$ relation depends on the topology of the resolution, which is type-dependent. A complete exclusion of all ALE types requires either:
- A holonomy reduction theorem: ALE Ricci-flat 4-manifolds with suitable curvature decay have holonomy $\subset SU(2)$ (partial results by Bando--Kasue--Nakamura, Tian--Yau); or
- A direct $\chi$-$|\Gamma|$ bound for non-ADE ALE resolutions showing that large $|\Gamma|$ forces large $\chi$.

### 3.4. Connection to Step 71 quantum accounting

The Step 71 ADE enumeration is now properly contextualized. For inner ALE bubbles after removing the outermost (non-ALE) model, the residual energy budget constrains $\sum_j\mathrm{rank}_j$, and the chirality accounting $\sum_j\tau_j + \mathrm{APS\ corrections} = 0$ constrains the self-dual/anti-self-dual distribution. The Step 71 result that pure ADE half-flat atoms cannot achieve single-chirality quantum $Q = 4$ remains a useful diagnostic for the inner structure.

### 3.5. The near-Einstein specialization and remaining steps

In the Yau--26 application, the hypothesis is not bare $\mathrm{Ric} \ge \kappa g$ but near-Einstein: $\|\mathrm{Ric}_{g_i} - g_i\|_{\mathrm{op}} \le \delta_i \to 0$. This provides:
- Two-sided Ricci control, so part (c) gives $\mathrm{Ric}_{\tilde g_i} \to 0$ uniformly.
- Noncompact limits: Myers diameter $D_i \le \pi\sqrt{3/(1-\delta_i)}$ is bounded, but $D_i/\rho_i \to \infty$ because $\rho_i \to 0$ and $D_i$ is bounded below (Myers is an upper bound, but any point at distance $> \rho_i$ exists since $M$ is not a single ball).
- Smooth Ricci-flat limits: with two-sided Ricci convergence to zero, Cheeger--Naber regularity gives smoothness away from a discrete singular set in dimension 4.

**Remaining steps for a complete collapse analysis:**

1. **Regularity of the limit**: Needs the two-sided Ricci control (available in near-Einstein case) plus Cheeger--Naber in dimension 4 to identify the limit as a smooth Ricci-flat orbifold with isolated singularities.

2. **Holonomy reduction**: Is the smooth part of the outermost model hyper-Kähler? For ALE 4-manifolds, Bando--Kasue--Nakamura and related results imply $\mathrm{hol} \subset SU(2)$ under suitable curvature decay. A complete argument must either establish this reduction or handle non-hyper-Kähler Ricci-flat ALE types separately using direct $\chi$-$|\Gamma|$ bounds.

3. **Outermost non-ALE models**: Once ALE is excluded (for $\epsilon < 1/48$ in the ADE case, or for all ALE types after holonomy reduction), the outermost model has $\mathrm{AVR} = 0$ or $\mathrm{AVR}$ below any ALE threshold. Identifying this as ALF, ALG, ALH, or another specific Ricci-flat end type requires the Chen--Chen classification or similar.

4. **Chirality accounting**: The signature integral with APS boundary corrections at the transition scale:
$$\tau(M) = \sum_j \tau_j^{\mathrm{loc}} + \sum_{\text{boundaries}} \eta(\partial) + \text{gluing corrections}.$$

5. **Inner bubble-tree**: Below the outermost scale, inner ALE bubbles distribute the remaining $\chi$ and energy. The CGB constraint $\sum_j\mathrm{rank}_j \le 7$ (after E_7 exclusion) limits their total complexity.

6. **Assembly**: The collapsed bulk has $\chi_{\mathrm{bulk}} = 0$ if it admits an F-structure. Whether the bulk is regular enough for this requires Ricci-only collapse theory (Cheeger--Fukaya--Gromov with weakened curvature hypotheses).

---

## 4. Combined positive-branch ledger

### Noncollapsed front

**Status:** The Cheeger--Naber compactness + ALE bubbling route is conditional on:
- Ozuch transversality and the full gauged kernel slice (Step 76--77 corrections);
- The first obstruction vanishes on the product quotient (known: rank-one on the 2-plane);
- Higher obstruction tower: cannot be forced to vanish by pinching alone (Step 74);
- J-symmetry eliminates transverse components to all orders (A01 Step 80), but the surviving 2×2 radial system is unresolved;
- Local desingularization cannot distinguish chirality patterns at available order (Step 78).

### Collapse front (newly opened)

**Status:** The transition-scale theorem provides the controlled-annulus framework:
- Outermost model has $\mathrm{AVR} \le \epsilon$ for any $\epsilon > 0$ (proved above).
- **ALE exclusion**: for $\chi = 8$ and $\epsilon < 1/48$, no Kronheimer hyper-Kähler ALE can be the outermost model (energy budget); with chiral refinement on balanced $\tau = 0$ rows, $\epsilon < 1/4$ suffices.
- **Remaining non-ADE ALE gap**: non-hyper-Kähler Ricci-flat ALE types not yet excluded (requires holonomy reduction or $\chi$-$|\Gamma|$ bound).
- ALF/ALG/ALH atom tables and APS chirality corrections needed for complete accounting.

**Remaining:** regularity of the limit, holonomy identification, chirality accounting, inner bubble-tree, and assembly.

### Refutation front

**Status:** A full positive-branch refutation requires proving that one fixed mixed row admits no Einstein metric of any sign ($\lambda > 0$, $\lambda = 0$, $\lambda < 0$).
- $\lambda > 0$: no classical obstruction found; the known-example pattern $\min(b_+,b_-) \le 1$ is explained by conformally Kähler structure, not by a general theorem.
- $\lambda = 0$: Hitchin's theorem requires holonomy $\subset SU(2)$, forcing $\chi = 24$, $\tau = -16$. The mixed rows have $\chi = 8$, so Ricci-flat Kähler is excluded. But non-Kähler Ricci-flat ($\mathrm{hol} = SO(4)$) exists in principle; no known obstruction applies.
- $\lambda < 0$: requires separate analysis; PSC and simply connected, but simplicial volume vanishes.

---

## 5. Source index

- Weitzenböck formula for self-dual 2-forms: `Knowledge/.../Einstein-Manifolds-Self-Dual-Weyl-Curvature-and-Conformally-Kaehler-Geom--78ee11b88e78.../object.md`, lines 140--164.
- Wu/LeBrun Proposition 2.2 and det $W^+$ criterion: same source, lines 181--197.
- Gursky positive-Yamabe bound: `Knowledge/.../The-Weyl-functional-on-4-manifolds-of-positive-Yamabe--45ae2a681cf1.../object.md`, lines 88--102.
- Gursky--LeBrun positive-Einstein estimate: `Knowledge/.../On-Einstein-Manifolds-of-Positive-Sectional-Curvature--d0e2b5d0776d.../object.md`, lines 206--224.
- LeBrun 2024 del Pezzo/Hermitian list: `Sessions/S0910A02/staging/acquired/Einstein_Metrics__-_Four-Manifolds_08862d5b95354876/part_001.md`.
- LeBrun--Ozuch admissible sequences: `Knowledge/.../Desingularizations-of-Conformally-Kaehler-Einstein-Orbifolds--8fe1aa31deb8.../object.md`, lines 35--69, 595--619.
- Step 71 quantum accounting: `workspace/notes/step71_collapse_quantum_and_lean_scope.md`.
- Step 75 controlled-annulus gap: `workspace/data/step75_symmetry_selection_collapse.json`.
- Step 78 mixed-row topology: `workspace/data/step64_positive_mirror_homeomorphism.json`.
- Verification data: `workspace/data/step79_transition_constants_verify.json`.

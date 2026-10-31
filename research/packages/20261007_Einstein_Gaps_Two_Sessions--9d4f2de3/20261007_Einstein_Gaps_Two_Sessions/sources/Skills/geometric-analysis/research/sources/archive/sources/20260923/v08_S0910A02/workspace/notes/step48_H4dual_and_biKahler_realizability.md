# Step 48: H4_dual Lemma and Bi-Kähler Realizability

Session S0910A02. Agent2/Constructor. Phase Execute.

**Supersedes:** Step 46 theorem (partially), Step 47 H4 critique (incorporates).
**Depends on:** Step 46 Γ-invariant computation, Step 47 curvature-invariance,
Steps 44–45 bi-Kähler data.

> **Step 49 correction.** Read this note together with `workspace/notes/step49_positive_branch_wall_and_operator_norm.md` and `workspace/data/step49_operator_norm_and_enumeration.json`. The Step-48 localization of the bi-Kähler wall is retained, but two supports are recalibrated. First, the second-order Ozuch computation is not load-bearing for Yau--26 operator-norm pinching: after the first obstruction is killed, second and higher obstruction residuals vanish in \(\|\operatorname{Ric}-\Lambda g\|_{op}\) and can block only exact Einstein gluing. Thus §3.2 branch (II), as stated, is not available as an obstruction to near-pinched metrics. Second, the H4_dual flux must be studied after normalization by the bubble signal \(t_i^2\); the unnormalized boundary functional vanishes trivially from \(h_i\to0\). The hard analytic lemma is quantitative two-scale flux matching, not merely chart consistency/cutoff bookkeeping.

## 0. Summary of Findings

Two independent results change the character of the positive noncollapsed route:

**A. (H4_dual)** The correct analytic architecture for the mode-projection
obstruction pairs the $C^0$ Ricci defect against the Ozuch obstruction Jacobi
field $\mathbf{o}_k$ over the *entire bubble region* with a single outer cutoff,
rather than a compactly supported annular test.  This avoids the false
pointwise second-derivative requirement identified in Step 47.  The
obstruction is read by the outer boundary flux, which computes the Ozuch
coefficient $\lambda_k = c\langle R_\varepsilon(p)\zeta,\zeta_{(k)}\rangle$
in the iterated limit $\delta_i\to0$ then $R\to\infty$.

**B. (ζ-realizability)** At the bi-Kähler orbifold $(S^2\times S^2)/\mathbb Z_2$
with $R_+ = R_- = \operatorname{diag}(\Lambda,0,0)$ at all four $A_1$ points,
a 6-parameter $\mathbb Z_2$-equivariant family of EH directions lies in
$\ker R_\pm$, satisfying the first-order Ozuch obstruction.  The second-order
obstruction $\mu_1 = C\det(\text{remaining block}) = 0$ is *also* structurally
vacuous because the rank-1 property of $R$ cascades.  This means the mode-projection
theorem, even fully proved, cannot exclude noncollapsed positive bubbling for
$\#_3(S^2\times S^2)$ through first- or second-order analysis.

Together these locate the true wall in the positive noncollapsed branch: not
the analytic bridge (which can likely be closed), but the *existence/nonexistence*
of Einstein metrics on the resolved manifold.

## 1. H4_dual: Jacobi-field flux pairing

### 1.1 Setup

Let $(M^4, g_i)$ be a sequence of closed Riemannian manifolds with
$$
\operatorname{Ric}(g_i) = \Lambda g_i + E_i,\qquad |E_i|_{g_i}\le\delta_i\to0,
\qquad \Lambda>0.
$$
Suppose the sequence is noncollapsed ($\operatorname{Vol}(B_1(x,g_i))\ge v>0$)
and converges in the Cheeger–Naber sense to an Einstein orbifold $(M_o,g_o)$
with an $A_1=\mathbb R^4/\mathbb Z_2$ singular point $p$ and bubble scale
$t_i\to0$.  By Cheeger–Naber Theorem 1.13 (source-verified: applies under
$|\operatorname{Ric}|\le3$, not just Einstein), the rescaled metrics
$\tilde g_i = t_i^{-2}g_i$ converge in $C^{1,\alpha}_{\rm loc}$ to the
Eguchi–Hanson metric $\mathbf{eh}$ on $T^*S^2\setminus S^2\cong
(\mathbb R^4/\mathbb Z_2)\setminus\{0\}$.

### 1.2 Obstruction Jacobi field

For each $\zeta\in\mathbb R^3\setminus\{0\}$ and chirality
$\varepsilon\in\{+,-\}$, the EH metric $\mathbf{eh}_{\zeta^\varepsilon}$
admits three obstruction modes $\mathbf{o}_k(\zeta^\varepsilon)$,
$k=1,2,3$, forming a basis of $\mathbf{O}(\mathbf{eh}_{\zeta^\varepsilon})$.
Each $\mathbf{o}_k$ satisfies:
$$
P_{\mathbf{eh}}\mathbf{o}_k = 0,\qquad
\mathbf{o}_k\text{ smooth on }T^*S^2\text{ (including the bolt }S^2\text{)},
\qquad |\mathbf{o}_k|_{\mathbf{e}}\sim\rho^{-4}\text{ as }\rho\to\infty.
$$
(Ozuch source, equations (16), (13), Remark 1.19.)

**Key property:** $\mathbf{o}_k$ is smooth at the bubble core.  There is
no inner boundary singularity.

### 1.3 The flux functional

For each index $i$ and cutoff radius $R>1$, define the flux:
$$
\Phi_k^i(R) := \int_{\rho\le 2R}
\bigl\langle\operatorname{Ric}(g_i)-\Lambda g_i,\;\chi_R\,\mathbf{o}_k
\bigr\rangle_{g_i}\,d\mu_{g_i}
$$
where $\chi_R$ is a smooth cutoff equal to $1$ for $\rho\le R$ and $0$
for $\rho\ge 2R$, and $\mathbf{o}_k$ is transported to a neighborhood
of the singular point via the bubble-frame chart.

**Upper bound from hypothesis.**
Since $|\operatorname{Ric}(g_i)-\Lambda g_i|_{g_i}\le\delta_i$:
$$
|\Phi_k^i(R)|\le\delta_i\int_{\rho\le 2R}|\chi_R\,\mathbf{o}_k|_{g_i}\,d\mu_{g_i}
\le C\delta_i(1+\ln R).
$$
The logarithmic factor arises from $|\mathbf{o}_k|_{\tilde g}\sim\rho^{-4}$
combined with $d\mu_{\tilde g}\sim\rho^3\,d\rho\,d\sigma$, giving
$\int_1^R\rho^{-1}\,d\rho = \ln R$.  The integral over the bubble core
$\rho\le 1$ contributes a bounded constant because $\mathbf{o}_k$ is smooth
there.  (The $C^0$-Ricci defect in the bubble frame is $|E_i|_{\tilde g} =
t_i^2|E_i|_{g_i}\le t_i^2\delta_i$, but the $L^1$ pairing is scale-invariant
in dimension 4.)

### 1.4 Structural expansion (iterated-limit argument)

Write $\tilde g_i = \mathbf{eh} + h_i$ in the bubble-frame chart.  By
$C^{1,\alpha}_{\rm loc}$ convergence, $\|h_i\|_{C^{1,\alpha}(K)}\to0$
for each compact $K\subset T^*S^2$.

Expand the Ricci tensor around $\mathbf{eh}$ (which is Ricci-flat):
$$
\operatorname{Ric}(\mathbf{eh}+h_i) - \Lambda(\mathbf{eh}+h_i)
= P_{\mathbf{eh}}(h_i) - \Lambda(\mathbf{eh}+h_i) + Q(h_i,h_i)
+ \text{gauge},
$$
where $P_{\mathbf{eh}} = \frac12\nabla^*\nabla - \mathring R_{\mathbf{eh}}$
is the Lichnerowicz operator.

**Integration by parts.**  The critical step:
$$
\int_{B_R}\langle P_{\mathbf{eh}}(h_i),\,\mathbf{o}_k\rangle_{\mathbf{eh}}
\,d\mu_{\mathbf{eh}}
= \int_{B_R}\langle h_i,\,P_{\mathbf{eh}}(\mathbf{o}_k)\rangle_{\mathbf{eh}}
\,d\mu_{\mathbf{eh}}
+ \mathcal B_k(R,i),
$$
where $\mathcal B_k(R,i)$ is the boundary flux on $\{\rho=R\}$:
$$
\mathcal B_k(R,i) = \frac12\int_{\{\rho=R\}}
\bigl(\langle\nabla_\nu h_i,\mathbf{o}_k\rangle
- \langle h_i,\nabla_\nu\mathbf{o}_k\rangle\bigr)\,d\sigma_R.
$$
Since $P_{\mathbf{eh}}\mathbf{o}_k=0$, the bulk term on the right vanishes.

**No inner boundary:** At the bolt $S^2$ (the inner boundary of the
bubble), $\mathbf{o}_k$ is smooth and $h_i$ is bounded in $C^{1,\alpha}$.
The boundary flux from $\rho\to0$ vanishes because the EH metric is smooth
across the bolt.

**Cosmological-constant term:**
$\langle\Lambda(\mathbf{eh}+h_i),\mathbf{o}_k\rangle
= \Lambda\operatorname{tr}_{\tilde g_i}(\mathbf{o}_k)
\approx 0 + O(\|h_i\|\cdot|\mathbf{o}_k|)$
since $\mathbf{o}_k$ is trace-free with respect to $\mathbf{eh}$.

**Gauge terms:** For a TT test tensor, the Bianchi-gauge correction
$\delta^*_{g_i}B_{\mathbf{eh}}g_i$ pairs to a boundary term via
$\langle\delta^*B,\mathbf{o}_k\rangle
= \langle B,\delta\mathbf{o}_k\rangle + \text{bdry}$,
and $\delta_{\mathbf{eh}}\mathbf{o}_k = 0$.

**Cutoff error:** The commutator $[P_{\mathbf{eh}},\chi_R]$ is supported
in $\{R\le\rho\le 2R\}$ and bounded by
$C(R^{-1}|\nabla\mathbf{o}_k| + R^{-2}|\mathbf{o}_k|)
= O(R^{-5}+R^{-6}) = O(R^{-5})$.
Integrated with volume $\sim R^3$: cutoff contribution $\le C\|h_i\|_{C^0}\cdot R^{-2}$.

**Nonlinear term:**
$|\langle Q(h_i,h_i),\mathbf{o}_k\rangle|\le C\|h_i\|_{C^{1,\alpha}}^2
\cdot\|\mathbf{o}_k\|_{L^1(B_{2R})}$.

### 1.5 Collecting the estimate

$$
\Phi_k^i(R) = \mathcal B_k(R,i) + O(\|h_i\|_{C^{1,\alpha}(B_{2R})})
\cdot C(R) + O(\|h_i\|^2)\cdot C(R).
$$

**Step 1 (fix $R$, let $i\to\infty$):**
$C^{1,\alpha}_{\rm loc}$ convergence gives $\|h_i\|_{C^{1,\alpha}(B_{2R})}\to0$.
From the upper bound, $|\Phi_k^i(R)|\le C\delta_i(1+\ln R)\to0$.
Therefore $\mathcal B_k(R,\infty) := \lim_{i\to\infty}\mathcal B_k(R,i) = 0$.

**Step 2 (let $R\to\infty$):**
By the Ozuch structure theory (source lines 512–514, 578–588), the
boundary flux $\mathcal B_k(R,\infty)$ converges as $R\to\infty$ to
$$
\mathcal B_k(\infty) = c\,\langle R_\varepsilon(p)\zeta,\zeta_{(k)}\rangle
\cdot\text{(normalization)},
$$
where $R_\varepsilon(p) = W_\varepsilon(g_o,p) + \frac\Lambda3 I$ is the
chiral curvature block at the singular point, and $c>0$ is a universal
constant from the EH geometry.

Since $\mathcal B_k(R,\infty) = 0$ for each $R$, continuity gives
$\mathcal B_k(\infty) = 0$, hence
$$
R_\varepsilon(p)\zeta = 0.\qquad\square\text{(conditional)}
$$

### 1.6 Dependency status

| Hypothesis | Status | Source |
|---|---|---|
| (H1) CN codim-4 convergence | Proved | Cheeger–Naber Theorem 1.13 |
| (H2) Almost-volume-cone annuli | Proved | Anderson–Cheeger–Colding |
| (H3) Bubble-frame $C^{1,\alpha}_{\rm loc}$ | Partially proved | Requires bubble selection from CN weak-type estimate |
| (H4_dual) Integration by parts identity | Conditional | Requires: (a) chart consistency, (b) cutoff error uniformity, (c) boundary flux identification with Ozuch coefficient |

The decisive open ingredient is **(H4_dual.c)**: showing that the boundary
flux $\mathcal B_k(R,\infty)$ equals the Ozuch obstruction coefficient.
This requires matching the asymptotic expansion of the limiting metric at
the interface between the bubble and orbifold regions.  In the Ozuch framework
(exact Einstein), this matching is provided by the weighted Hölder
approximation theorem (source line 419–423).  For merely $C^0$-Ricci-pinched
sequences, the analogous statement requires careful justification.

## 2. ζ-realizability at the bi-Kähler orbifold

### 2.1 First-order analysis

At each of the four $A_1$ points of $(S^2\times S^2)/\mathbb Z_2$:
$$
R_+ = R_- = \operatorname{diag}(\Lambda,0,0),\qquad
\ker R_\pm = \operatorname{span}\{e_2,e_3\},\quad\dim=2.
$$
(Verified in Steps 44–45.)

**First-order Ozuch obstruction (source lines 512–514):**
$$
\lambda_k(\zeta^\varepsilon) = c\langle R_\varepsilon(p)\zeta,\zeta_{(k)}\rangle
= 0 \quad\text{for all }k\text{ when }\zeta\in\ker R_\varepsilon.
$$

**Topology:** Resolution requires 2 compatible ($+$) and 2 reversed ($-$)
EH bubbles for signature $\tau=0$.  With $\mathbb Z_2$ equivariance,
one pair compatible and one pair reversed.  The resolved topology has
$b_+=b_-=3$, intersection form $3H$, consistent with
$\#_3(S^2\times S^2)$.

**Parameter count:** 6-parameter $\mathbb Z_2$-equivariant family
(2 independent direction pairs $\times$ 2D kernel + 2 scale parameters).

### 2.2 Second-order analysis

When all $\lambda_k=0$, the Ozuch second obstruction (source lines 667–684):
$$
\mu_1 = C\det\begin{pmatrix}R_{22}&R_{23}\\R_{32}&R_{33}\end{pmatrix}
$$
in the frame where $\zeta_{(1)}=\zeta/|\zeta|$.  For $\zeta=(0,\zeta_2,\zeta_3)
\in\ker R$ with $R=\operatorname{diag}(\Lambda,0,0)$:

$$
\text{Remaining block} = \begin{pmatrix}\Lambda&0\\0&0\end{pmatrix}
\quad\Longrightarrow\quad \mu_1 = C\cdot 0 = 0.
$$

The vanishing is **structural:** $R$ has rank 1, so after projecting out
$\zeta$ (which lies in the 2D kernel), the remaining $2\times2$ block always
has at least one zero row.  This is angle-independent within $\ker R$.

**Comparison with $\mathbb T^4/\mathbb Z_2$:** There, $R=0$ (flat orbifold),
so ALL obstructions through second order are vacuous at all 16 points.
Ozuch found a 14-dimensional chessboard family satisfying all 84 equations.
Here $R\ne0$ but rank 1, which kills first and second order for kernel
directions but may impose nontrivial constraints at higher order or through
inter-point interactions (Corollary 2.12).

### 2.3 Decisive implication

**The mode-projection theorem (even with H4_dual fully proved) cannot
exclude noncollapsed positive bubbling for $\#_3(S^2\times S^2)$
through first- or second-order obstruction analysis.**

This is not a failure of the analysis — it is a structural finding about where
the Yau-26 positive branch genuinely lives.  The bi-Kähler orbifold
$(S^2\times S^2)/\mathbb Z_2$ is the concrete model where a near-Einstein
bubbling family *might actually exist*.

**What a realized family would establish:**
- A sequence $(M^4,g_i)$ with $\|\operatorname{Ric}(g_i)-\Lambda g_i\|_{C^0}
  \to0$ on a fixed smooth manifold $M\cong\#_3(S^2\times S^2)$, converging
  to the orbifold quotient with four EH bubbles.
- This would *not* refute Yau-26: $\#_3(S^2\times S^2)$ satisfies strict
  Hitchin–Thorpe ($2\chi-3|\tau|=16-0=16>0$), and no obstruction to positive
  Einstein metrics is known beyond HT for simply connected 4-manifolds.
- It *would* locate the real wall: proof of $P_4^+$ requires an Einstein
  existence theorem on $\#_k(S^2\times S^2)$; refutation requires a new
  nonexistence obstruction.

**What a blocked family would establish:**
- Higher-order or inter-point Ozuch obstructions, or linearized-operator
  non-invertibility, prevent the desingularization.
- Then the mode-projection theorem regains power: no noncollapsed positive
  near-Einstein sequence can converge to the product orbifold while resolving
  to $\#_k(S^2\times S^2)$.

## 3. Corrected scope and implications for Yau-26

### 3.1 What the mode-projection bridge establishes (conditional)

For **non-bi-Kähler** orbifold limits with AD-type singularities and
$\Lambda>0$:

- At each singular point $p_j$ with isotropy $\Gamma_j$ and bubble
  direction $\zeta_j^{\varepsilon_j}$, the first-order obstruction requires
  $R_{\varepsilon_j}(p_j)\zeta_j = 0$.
- By Step 47's curvature-invariance computation: for $A_k$ ($k\ge2$) and
  $D_k$, this is an explicit scalar equation in the $\Gamma$-adapted Weyl
  block.  For E-type, the nontrivial block has $R=(\Lambda/3)I$, which is
  invertible — so reversed bubbles in the E-type nontrivial block are
  first-order obstructed.
- **Finite dichotomy (Step 47 correction):** Either all reversed-bubble
  directions are obstructed ($R_\varepsilon\zeta\ne0$), in which case only
  compatible ALE bubbles form and $b_+(M)=b_+(M_o)$ in the appropriate
  convention; or the limit satisfies explicit finite degeneracy equations.

For the **bi-Kähler** orbifold limit (the only known double-degeneracy model
for $\Lambda>0$): first and second order obstructions are vacuous for
kernel-direction bubbles, as shown above.

### 3.2 The four-dimensional positive branch: dichotomy

$P_4^+$ now reduces to a clear binary:

**(I) The bi-Kähler desingularization exists.**
Then a near-Einstein bubbling family on $\#_3(S^2\times S^2)$ exists, and
$P_4^+$ depends on the Einstein existence problem for
$\#_k(S^2\times S^2)$, $k\ge2$.

**(II) The bi-Kähler desingularization is blocked** (by higher-order
obstructions, linearized-operator, or other mechanism).
Then the mode-projection theorem excludes noncollapsed positive bubbling
on manifolds with $b_+\ge2$ that would require resolution through a
bi-Kähler orbifold.  Combined with the non-bi-Kähler obstruction from the
same bridge, this significantly constrains (but does not yet prove) $P_4^+$.

### 3.3 Remaining independent obligations

| Branch | Status | Gap |
|---|---|---|
| $n=2,3$ | Resolved | Uniformization/geometrization |
| $n=4$, positive, noncollapsed, non-bi-Kähler | Conditional | H4_dual.c |
| $n=4$, positive, noncollapsed, bi-Kähler | Open | Higher-order Ozuch analysis at $(S^2\times S^2)/\mathbb Z_2$ |
| $n=4$, positive, collapsed | Open | Almost-Killing/Bochner bridge |
| $n=4$, negative | Conditional (A01/A03) | Restricted IL gap theorem, not independently verified |
| $n\ge5$ | Open | Codim-4 stratum integral; higher-dim field production |
| Lean formalization | Open | Awaits mathematical resolution |

## 4. Comparison with Ozuch's $\mathbb T^4/\mathbb Z_2$ analysis

The bi-Kähler $(S^2\times S^2)/\mathbb Z_2$ differs from Ozuch's flat torus
in several ways:

| Property | $\mathbb T^4/\mathbb Z_2$ | $(S^2\times S^2)/\mathbb Z_2$ |
|---|---|---|
| Orbifold metric | Flat ($\Lambda=0$) | Kähler–Einstein ($\Lambda>0$) |
| Singular points | 16 | 4 |
| $R_\pm$ at singularities | $0$ (all zero) | $\operatorname{diag}(\Lambda,0,0)$ (rank 1) |
| First-order conditions | All vacuous | Vacuous in 2D kernel |
| Second-order $\mu_1$ | All vacuous | Vacuous (rank-1 cascade) |
| Known unobstructed family | 14-dim chessboard | Unknown (this is the open question) |
| Resolution topology | K3 or non-Kähler 4-manifold | $\#_3(S^2\times S^2)$ |

The Brendle–Kapouleas obstruction (Ozuch Remark 0.14) shows that the most
symmetric chessboard configuration of $\mathbb T^4/\mathbb Z_2$ *is* first-order
obstructed.  But Ozuch's 14-dim family avoids this by using asymmetric
parameters.  For $(S^2\times S^2)/\mathbb Z_2$, the smaller number of points
and the curved orbifold may impose additional constraints — or the
$\mathbb Z_2$-equivariance may simplify the analysis.

## 5. Files

- Scripts: `workspace/scripts/step48_zeta_realizability_biKahler.py`,
  `step48_second_order_obstruction.py`
- Data: `workspace/data/step48_zeta_realizability.json`,
  `step48_second_order_obstruction.json`
- Step 46 computation: `workspace/data/step46_gamma_invariant_l2_modes.json`
- Step 47 curvature-invariance: `workspace/data/step47_curvature_invariant_degeneracy.json`
- Ozuch source: `Knowledge/objects/papers/Higher-order-obstructions-...-19c12fb27fae/object.md`
- Step 44–45 bi-Kähler data: `workspace/data/step44_*.json`, `step45_*.json`

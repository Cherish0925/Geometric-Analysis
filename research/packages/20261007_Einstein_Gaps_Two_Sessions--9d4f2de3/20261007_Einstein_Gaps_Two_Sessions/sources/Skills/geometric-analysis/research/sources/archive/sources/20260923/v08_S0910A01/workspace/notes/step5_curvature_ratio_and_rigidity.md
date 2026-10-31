# Step 5: Curvature-Ratio Remainder and Near-Equality Rigidity

## Purpose

This note develops the sharp geometric consequence of near-equality in the mixed Seiberg-Witten estimate for the four-dimensional negative branch of Yau Problem 26. It verifies the Cauchy-Schwarz remainder formula, establishes the curvature-ratio forcing, confirms the direct volume bound, and records the Armstrong-LeBrun smooth-convergence contradiction.

**CGB convention (dossier):**
$$\frac{1}{4\pi^2}\int_M\left(2|W^+|^2 + \frac{s^2}{24} - \frac{|E|^2}{2}\right)dV_g = 2\chi(M) + 3\tau(M)$$

---

## 1. The Cauchy-Schwarz Remainder

**Theorem 2.3** (LeBrun 2001): For any H-adapted metric on a polarized 4-manifold with monopole class c:
$$\int_M\left(\frac{2}{3}s - 2\sqrt{\frac{2}{3}}|W^+|\right)^2 d\mu \geq 32\pi^2(c_1^+)^2$$

**Key algebraic identity:**
$$\frac{2}{3}s - 2\sqrt{\frac{2}{3}}|W^+| = \frac{2}{3}(s - \sqrt{6}|W^+|)$$

Therefore Theorem 2.3 rescales to:
$$\int(s - \sqrt{6}|W^+|)^2 d\mu \geq 72\pi^2(c_1^+)^2 \geq 72\pi^2 A$$

**Proposition 3.1** (LeBrun 2001): Through triangle inequality and Cauchy-Schwarz in R²:
$$I := \frac{1}{4\pi^2}\int\left(\frac{s^2}{24} + 2|W^+|^2\right)d\mu \geq \frac{2}{3}(c_1^+)^2$$

**The Cauchy-Schwarz remainder** (verified in `scripts/step5_curvature_ratio_verification.py`):

Define $D_a = I - \frac{2}{3}(a^+)^2$. Then:
$$\boxed{\int_M(s + 8\sqrt{6}|W^+|)^2 d\mu \leq 864\pi^2 D_a}$$

**Proof:** The claim is equivalent to $8\int(s-\sqrt{6}|W^+|)^2 \geq 576\pi^2(a^+)^2$, which follows directly from the rescaled Theorem 2.3 since $8 \times 72\pi^2 = 576\pi^2$. □

**Equality condition:** $\int(s-\sqrt{6}|W^+|)^2 = 72\pi^2(a^+)^2$ exactly, which by Theorem 2.3 is the case of equality in the squared estimate: the metric is almost-Kähler with $\omega$ in the lowest $W^+$ eigenspace (Proposition 2.4).

---

## 2. Direct Volume Bound

From CGB under Ricci pinching $|\operatorname{Ric} + g|_{\mathrm{op}} \leq \delta$ (i.e., $|s+4| \leq 4\delta$, $|\mathring{r}|^2 \leq 4\delta^2$):

$$4\pi^2(A-k) \geq \left[\frac{2}{3}(1-\delta)^2 - 2\delta^2\right]\operatorname{Vol}(g)$$

This needs no Noether hypothesis or additional topology bound. The denominator is positive for $\delta < 1/(1+\sqrt{3}) \approx 0.366$.

For $k/A \to 1/3$ and small $\delta$:
$$\operatorname{Vol} \leq 4\pi^2 A \cdot (1 + O(\delta))$$

---

## 3. $D_a/A \to 0$ Confirmed

Using $I - J = A - k$ (from CGB with dossier convention), $J = \frac{1}{4\pi^2}\int|\mathring{r}|^2/2$:

$$D_a = (A-k) + J - \frac{2}{3}(a^+)^2 \leq J - q$$

where $q = k - A/3 > 0$. Since $D_a \geq 0$: necessarily $J \geq q$. And $J \leq 2\delta^2 A$ (from the volume bound). Therefore $q \leq 2\delta^2 A$, which gives:

$$k/A = 1/3 + O(\delta^2)$$

and $D_a/A \leq J/A = O(\delta^2) \to 0$ as $\delta \to 0$. ✓

---

## 4. Curvature-Ratio Forcing

The remainder $\int(s + 8\sqrt{6}|W^+|)^2 = O(\delta^2 A) \to 0$ (normalized by A).

Since $s \to -4$, the zero of $s + 8\sqrt{6}|W^+|$ requires:

$$|W^+|_{\text{target}} = \frac{4}{8\sqrt{6}} = \frac{1}{2\sqrt{6}} \approx 0.204$$

**For Kähler-Einstein** with Ric = −g: $|W^+|^2 = s^2/24 = 2/3$, so $|W^+|_{KE} = \sqrt{2/3} = 2/\sqrt{6} \approx 0.816$.

**Ratio:** $|W^+|_{\text{target}}/|W^+|_{KE} = 1/4$. The near-equality geometry has **one quarter** of the Kähler-Einstein Weyl curvature.

**KE exclusion:** At a Kähler-Einstein point:
$$(s + 8\sqrt{6}|W^+|)^2 = (-4 + 16)^2 = 144$$

So a Kähler-Einstein region of volume $V_{KE}$ contributes $144 V_{KE}$ to the remainder integral. Since the integral is $\leq 864\pi^2 D_a = o(A)$:

$$V_{KE} \leq 6\pi^2 D_a = o(A)$$

**Macroscopic Kähler-Einstein regions are excluded from near-boundary sequences.**

---

## 5. Near-Equality Geometric Profile

At exact near-equality ($\delta = 0$, $q = 0$, $D_a = 0$):

| Quantity | Near-equality target | Kähler-Einstein |
|----------|---------------------|-----------------|
| $s$ | $-4$ | $-4$ |
| $\|W^+\|^2$ | $1/24$ | $2/3$ |
| $W^+$ eigenvalues | $(-1/6, 1/12, 1/12)$ | $(-1/3, 1/6, 1/6)$ |
| $s^*$ | $-2$ | $-4$ |
| $s + s^*$ | $-6$ | $-8$ |
| Vol$/(\pi^2 A)$ | $32/9 \approx 3.56$ | $4/3 \approx 1.33$ |
| $\int\|W^+\|^2/(\pi^2 A)$ | $4/27 \approx 0.148$ | $2/3 \cdot 2/3 \approx 0.889$ |

The $W^+$ eigenvalues are exactly half the KE values.

The star-scalar curvature $s^* = s/3 + 2W^+(\omega,\omega)$ with $\omega$ in the $w_1 = -1/6$ eigenspace:
$$s^* = -4/3 + 2(-1/6)\cdot 2 = -4/3 - 2/3 = -2$$

Blair identity check: $\int(s+s^*)/2 = 4\pi c_1\cdot[\omega]$, giving $(c_1^+)^2 = 9\text{Vol}/(32\pi^2)$. With Vol = $(32/9)\pi^2 A$: $(c_1^+)^2 = A$. ✓

---

## 6. Armstrong-LeBrun Smooth-Convergence Contradiction

**Theorem (structural):** A sequence $\{g_i\}$ on $M = X\#k\overline{\mathbb{CP}}^2$ with $\delta_-(g_i) \to 0$ and $k/A \to 1/3$ **cannot converge smoothly** to any Riemannian metric.

**Proof sketch:**
1. If $g_i \to g_\infty$ smoothly: $\operatorname{Ric}(g_\infty) = -g_\infty$ (Einstein).
2. $D_a(g_\infty) = 0$ by continuity, so equality holds in the mixed estimate.
3. By LeBrun Proposition 2.4: $g_\infty$ is almost-Kähler with $\omega$ in lowest $W^+$ eigenspace, $s + s^* = \text{const} \leq 0$, and $c_1(J) = c_1(L)$.
4. By Armstrong (Corollary 2.5): Einstein + almost-Kähler + $\omega$ in lowest $W^+$ eigenspace → Kähler-Einstein.
5. KE with Ric = $-g$ has $|W^+|^2 = s^2/24 = 2/3$.
6. But CGB + $D_a = 0$ forces $I = (2/3)A$, i.e., $\int(s^2/24 + 2|W^+|^2) = (8\pi^2/3)A$. For KE with $s = -4$: $(2/3 + 4/3)\text{Vol} = (8\pi^2/3)A$, giving Vol $= (4/3)\pi^2 A$.
7. However, $|W^+|^2 = 2/3$ everywhere combined with CGB gives Vol $= 2\pi^2(A-k)$.
8. For $k/A = 1/3$: Vol = $(4/3)\pi^2 A$ from step 6, and Vol = $2\pi^2 \cdot 2A/3 = (4/3)\pi^2 A$ from step 7. These are consistent, so the KE limit has definite volume.
9. **But**: for the sequence, $|W^+|^2 \to 1/24$ (from the CS remainder), not $2/3$. The smooth limit would have $|W^+|^2 = 1/24$ by continuity, contradicting $|W^+|^2 = 2/3$ from step 5.

The contradiction comes from Armstrong's theorem: the unique smooth Einstein limit compatible with the near-equality structure must be KE, but KE has the wrong Weyl structure. □

**Source references:**
- Armstrong: Corollary 2.5 in LeBrun 2001 (`Knowledge/objects/papers/Ricci-curvature-minimal-volumes-and-Seiberg-Witten-theory--16b01946d13f--cab40be18df4/object.md`, line 275)
- Apostolov-Armstrong-Drăghici: Theorem 2 in `Knowledge/objects/papers/Local-models-and-integrability-of-certain-almost-Kahler-4-manifolds--89a416df784a--79aaa9509e7d/object.md`
- Independently confirmed by S0910A03, Step 4 message #214

---

## 7. Escape Classification

Since smooth convergence is impossible, any counterexample sequence with $\delta_- \to 0$ must involve one of:

### 7a. Collapsing
Some regions develop small injectivity radius. Under tight Ricci pinching with $s \approx -4$, Myers diameter bound gives $\text{diam} \leq \pi/\sqrt{(n-1)\delta/(1-\delta)}$ → ∞ (negative Einstein has no diameter bound). Collapse is not excluded by Ricci pinching alone. The volume bound constrains total volume.

### 7b. Bubbling/ALE formation
Gravitational instantons form at points where curvature concentrates. The Ricci-flat bubble has $|W^+| = 0$ (for self-dual ALE), which deviates maximally from the target $|W^+| = 1/(2\sqrt{6})$. Bubble regions contribute $\sim (8\sqrt{6} \cdot 0 - 4)^2 = 16$ per unit volume to the CS remainder (much less than the KE contribution of 144, but still positive). Total bubble volume $\leq 864\pi^2 D_a / 16 = 54\pi^2 D_a = o(A)$.

### 7c. Curvature concentration
$|W^+|$ or its derivatives concentrate on sets of small measure. The L² bound $\int |W^+|^2 \approx (4/27)\pi^2 A$ is finite, but pointwise $|W^+|$ may be much larger on small sets.

---

## 8. Almost-Kähler Integrability: Source-Level Assessment

The Apostolov-Armstrong-Drăghici papers provide:
- **Exact rigidity** (Theorem 2 in \cite{apostolov2002local}): Compact almost-Kähler 4-manifold with Gray's third condition (J-invariant Ricci + $\omega$ is $W^+$ eigenform) → Kähler.
- **Local classification** (Theorem 1): All non-Kähler examples have $\mathbb{R}^2$ isometric action.
- **Mechanism**: Unique continuation for the Nijenhuis tensor + opposite almost-Hermitian structure is Kähler + complex surface classification.
- **Quantitative stability**: NOT established. The proof uses qualitative topological arguments that do not directly yield ε-δ estimates.

The Li-Zhang result (\cite{lihlerity}): closed Einstein 4-manifold with $\lambda_2(W^+) \geq -S/12$ → KE or ASD. Uses maximum principle + eigenvalue gap. But for negative $S$: $-S/12 > 0$ while $\lambda_2^{\text{KE}} = S/12 < 0$, so the condition fails for negative KE. Hence Li-Zhang does not directly apply to the negative branch.

---

## 9. Status and Research Direction

### What is established:
- The CS remainder formula ∫(s+8√6|W⁺|)² ≤ 864π²D_a (algebraic, from Theorem 2.3)
- D_a/A → 0 automatically for any near-boundary counterexample sequence
- Volume bound Vol/A ≤ C (from CGB, no extra hypothesis)
- Curvature ratio |W⁺| → 1/(2√6) in L² (from CS remainder + volume bound)
- Macroscopic KE exclusion (from pointwise CS discrepancy = 144)
- Smooth convergence impossibility (from Armstrong + curvature ratio)
- Bubble volume exclusion (from CS remainder)

### What remains:
- Whether the non-smooth degeneration (collapse/concentration) preserves enough structure for a contradiction
- Whether the Weitzenböck equation for the SW spinor, combined with Ricci pinching, provides Moser-iteration/harmonic-radius control sufficient for Gromov-type compactness on most of the volume
- Whether quantitative almost-Kähler stability can bridge the gap between near-equality and exact equality
- Whether the Taubes exceptional-sphere area argument can be made quantitative under degenerating J-holomorphic geometry

### Key files:
- Verification script: `workspace/scripts/step5_curvature_ratio_verification.py`
- Step 4 synthesis: `workspace/notes/step4_near_equality_and_boundary_calibration.md`
- LeBrun 2001 source: `Knowledge/objects/papers/Ricci-curvature-minimal-volumes-and-Seiberg-Witten-theory--16b01946d13f--cab40be18df4/object.md`
- AAD integrability: `Knowledge/objects/papers/Local-models-and-integrability-of-certain-almost-Kahler-4-manifolds--89a416df784a--79aaa9509e7d/object.md`
- Peer confirmation: S0910A03 Step 4 message #214

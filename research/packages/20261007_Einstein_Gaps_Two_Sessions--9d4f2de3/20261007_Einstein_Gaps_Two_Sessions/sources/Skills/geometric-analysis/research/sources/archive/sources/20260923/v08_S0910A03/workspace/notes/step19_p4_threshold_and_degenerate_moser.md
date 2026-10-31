# Step 19: Volume-independent β, p>4 connection-drift threshold, and the degenerate ε-regularity target

> **Step 20 replacement notice.** The volume-independent critical parameter and the p>4 threshold for a quantitative connection-drift estimate remain mathematically valid, but that derivative estimate is no longer required for the zero-order first-exit. The Step 19 use of an unweighted Li iteration in the transition is replaced by the weighted Wang moments \(H_q=\int a^{q-2}F^q\) and \(J_m=\int a^{m-2}|E|^m\); see `step20_weighted_wang_hierarchy_and_whitney_correction.md`. In addition, unweighted global defect preservation is not automatic from the integrated cancellation alone: it requires the triangular curvature-potential absorption recorded in Step 20.

## Summary

This step establishes two proved results and formulates one conditional architecture.

**Proved:**  In dimension 4, Wang's critical parameter β = A₀²·‖Rm‖_{L²} is volume-independent: β = C²r²√K₀ = C'√ε, where K₀ is the curvature mean, r the Li radius, and ε = r⁴K₀. This is the same 4D Sobolev-energy cancellation that drives the L² energy persistence.

**Proved:**  The connection and cutoff-Hessian drifts under the cutoff flow require p > 4 (not just p > 2 as for metric drift) for time-integrability. For p = 6, both metric drift ~ C δ θ^{2/3} r² and connection drift ~ C δ θ^{1/6} are simultaneously controlled.

**Conditional:**  If the localized degenerate ε-regularity theorem (|χ²Rm| ≤ Cβ/t from small relative L² curvature energy on each ball) and a localized weighted Bernstein estimate can be proved for the finite-neighbor system under the normalized cutoff flow, then the simultaneous first-exit closes and yields the fixed-topology negative-pinching gap for critical Ishida–LeBrun 4-manifolds. These two PDE results are not corollaries of Wang's or Li's published theorems; they are new targets.

---

## 1. Volume-independent β (proved)

On a ball B_r(x) in a 4-manifold with Ric ≥ −3g, the relative Sobolev inequality gives
$$
\|f\|_{L^4(B_r)} \le A(∥∇f∥_{L^2(B_r)} + r^{-1}∥f∥_{L^2(B_r)}),
\qquad A \le C_S r V^{-1/4},
$$
where V = Vol(B_r) and C_S depends only on the Ricci lower bound.

The maximal-function selection (Step 9) gives, at a good point p:
$$
\fint_{B_r(p)}|\operatorname{Rm}|^2 \le K_0.
$$
Therefore R = ∫_{B_r}|Rm|² ≤ K₀V. Wang's critical parameter is
$$
\beta = A^2 \cdot \|{\operatorname{Rm}}\|_{L^2(B_r)}
= C_S^2 r^2 V^{-1/2} \cdot \sqrt{K_0 V}
= C_S^2 r^2 \sqrt{K_0}.
$$
**Volume cancels exactly.** With the Li radius r_* = (ε_Li/K₀)^{1/4}:
$$
\boxed{\beta = C_S^2 \sqrt{\varepsilon_{\mathrm{Li}}}}.
$$
For ε_Li sufficiently small (< (2n²C_S²)^{-2} = (32C_S²)^{-2}), β falls below Wang's threshold 1/(2n²).

**Remark (TTCS correction).**  On the expanded ball Ũ_α covering neighboring supports, ∫_{Ũ_α}|Rm|² ≤ Σ_{β~α} R_β ≤ N·2ε_*, where N is the finite neighbor count.  The correct localized product is therefore
$$
A_α^2 \|{\operatorname{Rm}}\|_{L^2(\widetilde U_α)}
\le C_S^2 C_V^{1/2} r_*^2 \sqrt{K_0},
$$
with C_V the Bishop–Gromov volume-doubling ratio.  This is still volume-independent and still O(√ε_Li), but the constants absorb the neighbor count and doubling ratio.

**Dimension specificity.**  Volume cancellation holds in any dimension for the critical L^{n/2} energy:
$$
A^2 \|{\operatorname{Rm}}\|_{L^{n/2}} \lesssim r^2 K_{n/2}^{2/n}.
$$
The special 4D feature is that L² IS the critical exponent, so the existing L² curvature control (from Chern–Weil, maximal function, and near-saturation) directly supplies the critical input.  For n > 4, the critical L^{n/2} energy is not controlled by L² data alone.

---

## 2. Connection-drift threshold: p > 4 (proved)

Assume the weighted defect estimate holds for some fixed p > 2:
$$
|U(t)| = |\chi^2 E(t)| \le C_p \delta (r^2/t)^{2/p}.  \tag{M_p}
$$
Then the metric drift
$$
\int_0^{\theta r^2} |U(t)|\, dt \le C_p \frac{p}{p-2} \delta \theta^{1-2/p} r^2  \tag{1}
$$
is finite for p > 2.  This is the Step 18 result.

Now assume the **companion weighted derivative estimate**:
$$
|\chi \nabla U(t)| \le C_p \delta t^{-1/2}(r^2/t)^{2/p}.  \tag{D_p}
$$
Then the connection drift
$$
\int_0^{\theta r^2} |\chi \nabla U(t)|\, dt
= C_p \delta r^{4/p} \int_0^{\theta r^2} t^{-1/2-2/p} dt
\le C_p \frac{2p}{p-4} \delta \theta^{1/2-2/p} r  \tag{2}
$$
is finite **if and only if p > 4**.  The endpoint p = 4 gives logarithmic divergence.

**Cutoff-Hessian drift.** Since ∂_t(Hess_g a) = −(∂_t Γ)·da and |da| = 2χ|dχ| ≤ 2C_χ/r:
$$
|\partial_t(\nabla^2 a)| \le 2C_χ |d\chi| \cdot |\chi \nabla U|.
$$
(TTCS correction: this uses the identity |da|·|∂_tΓ| ~ |dχ|·|χ∇U|, which controls only the contraction with da, hence the weighted Hessian change.  The full connection ∂_tΓ ~ ∇U is not controlled by χ∇U near χ = 0; however, Hess(a) depends only on da·∂_tΓ, so the weighted estimate suffices for this specific quantity.)

Integrating:
$$
|\nabla^2 a(t) - \nabla^2 a(0)|_\infty
\le \frac{2C_\chi}{r} \int_0^{\theta r^2} |\chi\nabla U| \, dt
\le C_p' \frac{2p}{p-4} \delta \theta^{1/2-2/p}.  \tag{3}
$$
This is O(δ) (dimensionless), controlled for small δ.  Note: the factor 1/r from |dχ| and the factor r from integration of the time exponent cancel exactly, confirming the dimensional analysis in the verification script.

**Optimal choice.** For p = 6:
- Metric drift coefficient: p/(p−2) = 3/2, exponent θ^{2/3}
- Connection drift coefficient: 2p/(p−4) = 6, exponent θ^{1/6}
- Absorption threshold: ε_*(6) ~ 1/p² = 1/36, manageable

---

## 3. Weighted Bernstein mechanism (target, not proved)

For U satisfying the degenerate tensor equation
$$
\partial_t U = a(\Delta_L U - 2U) + \mathcal{B}_a(U),
\qquad a = \chi^2,
$$
the effective diffusion length at location x is χ(x)√t.  The **target** interior gradient estimate is:
$$
|\chi \nabla U(x,t)| \le \frac{C}{r} \sup_{Q_{r,t}} |U| \cdot \frac{1}{\sqrt{t/r^2}}  \tag{4}
$$
where Q_{r,t} is a suitable parabolic cylinder.  Combined with (M_p):
$$
|\chi \nabla U(t)| \le \frac{C C_p \delta}{r} (r^2/t)^{2/p} \cdot r/\sqrt{t}
= C_p' \delta t^{-1/2}(r^2/t)^{2/p},
$$
which is precisely (D_p).

**Why this is a target, not a proved result (TTCS):**  Differentiating the tensor equation for U produces:
$$
\partial_t(\nabla U) = a \Delta_L(\nabla U) + a \operatorname{Rm}*\nabla U + a \nabla\operatorname{Rm}*U + \nabla a * \nabla^2 U + \nabla^2 a * \nabla U + \nabla^3 a * U.
$$
The term a·∇Rm·U is NOT controlled by |aRm| ≤ C/t alone.  The weighted curvature derivative ∇(χ²Rm) must be bounded separately.  Wang's Proposition 4.14 provides qualitative control under strong global hypotheses, but not the quantitative, δ-linear, t^{−1/2−2/p} rate with volume-independent constants needed here.

A rigorous proof would require:
- A localized degenerate parabolic W^{1,∞} estimate for the tensor U
- Constants depending only on provisional Sobolev geometry, neighbor count, curvature potential K₃, and cutoff derivatives
- Independence from collapsed volume

---

## 4. Wang/Yang degenerate ε-regularity (target, not proved)

The target result, analogous to Wang Theorem 6.3 localized to the finite-neighbor system:

**Target Theorem.**  *In dimension 4, for each ball U_α in the finite-neighbor good-point system with Li radius r_*, if the coupled critical energy satisfies R_α(t) ≤ 2ε_* for t ∈ [0, θr²], then*
$$
\|\chi^2 \operatorname{Rm}(t)\|_\infty \le \frac{C \beta}{t},
\qquad \beta = C_S^2 C_V^{1/2} \sqrt{\varepsilon_{\mathrm{Li}}}.
$$

**Why this is new (TTCS):**  Wang's Theorem 6.3 uses:
1. A GLOBAL Sobolev inequality on the whole manifold
2. GLOBAL L^{n/2} curvature energy smallness
3. GLOBAL L^p Ricci bound

The localized version needs:
1. RELATIVE Sobolev on each ball (available from Bishop–Gromov)
2. LOCAL curvature energy per ball (available from coupled system)
3. LOCAL Ricci bound (available: Ric = −(1+O(δ))g)

But also:
- Provisional metric equivalence throughout the first-exit
- Sobolev constant persistence under the evolving metric
- Finite-neighbor boundary terms in the energy equation
- Volume-form evolution ∂_t dμ = −tr(aE) dμ in the Moser power integrals
- Independent localization cutoff η_α with all gradient and Hessian terms

**Normalized-flow correction (TTCS):**  The additional term from h₂ = −2χ²g in the curvature evolution is
$$
D\operatorname{Rm}_g(h_2) \sim (\nabla^2 a) \owedge g + a \cdot \operatorname{Rm}.
$$
The Hessian term is an additive source, not directly O(r^{-2})∫|Rm|^{n/2}.  After integration by parts, it produces |da|·|Rm|^{q−2}|∇Rm| terms that must be absorbed into the gradient dissipation.  Two viable approaches:
- Use F = (1+|Rm|²)^{1/2} so that lower-power terms are absorbed; the near-Einstein baseline |Rm| ≥ c > 0 ensures that the regularized norm doesn't change the critical scaling.
- Merge the full velocity h = −2aE into a single variation; the source terms then vanish when E = 0.

---

## 5. Architecture of the conditional first-exit closure

Fix p = 6.  The first-exit argument on [0, T_*) where T_* is the first time any provisional bound is saturated:

| Step | Input | Result | Status |
|------|-------|--------|--------|
| 0 | Maximal function + good points | R_α(0) ≤ ε_*, K₀ bounded | **Proved** (Step 9) |
| 1 | Coupled L² system | R_α(t) ≤ 2ε_* | **Conditional** on first-exit (Step 18) |
| 2 | 4D volume-independent β | β ≤ C√ε_Li | **Proved** (this step) |
| 3 | Localized degenerate Moser | \|χ²Rm\| ≤ Cβ/t | **TARGET** (new PDE theorem) |
| 4 | Li Cor 3.5 with curvature potential | \|U\| ≤ C₆δ(r²/t)^{1/3} | Conditional on Step 3 |
| 5 | Weighted Bernstein | \|χ∇U\| ≤ C₆δt^{-1/2}(r²/t)^{1/3} | **TARGET** (new PDE theorem) |
| 6a | Metric integration (p=6 > 2) | drift ≤ (3/2)C₆δθ^{2/3}r² | Follows from Step 4 |
| 6b | Connection integration (p=6 > 4) | drift ≤ 6C₆δθ^{1/6} | Follows from Step 5 |
| 6c | Hessian integration (p=6 > 4) | drift ≤ 6C₆δθ^{1/6} | Follows from Step 5 |
| 7 | Metric eq + BG | Relative Sobolev preserved | Follows from Step 6a |
| 8 | All provisional bounds improved | First-exit not reached | Follows from Steps 1-7 |

**The argument has no logical circularity:** it is a simultaneous first-exit with provisional assumptions that are STRICTLY IMPROVED at each step.  But it requires **two new PDE theorems** (Steps 3 and 5) that are not available from existing literature.

---

## 6. Unweighted global defect (separate requirement)

The weighted estimates control χ²E but not E near χ = 0.  The downstream 7/24 calibration inequality (Step 15) requires the GLOBAL unweighted L² defect:
$$
Q(t) = \int_M |E(t)|^2 \, d\mu(t).
$$
On the plateau (χ = 1), |E| = |U| ≤ C₆δ(r²/t)^{1/3} and metric equivalence gives volume control.  Outside the support (χ = 0), the metric doesn't evolve, so E(t) = E(0) and Q contribution is fixed.

On the transition (0 < χ < 1), the defect E evolves but the weighted bound only gives |U| = χ²|E| ≤ C₆δ(r²/t)^{1/3}, so |E| ≤ C₆δ(r²/t)^{1/3}/χ², which blows up.  However:
- The transition volume is O(r·δ_transition·V^{3/4}) for a collar of width δ_transition
- The defect equation ∂_tE = a(Δ_LE − 2E) + C_a(E) has the global L² estimate:
$$
\frac{d}{dt}\int_M |E|^2 d\mu \le Cr^{-2}\int_M |E|^2 d\mu
$$
(from the integrated energy identity with cutoff cancellations from Step 14).

This formal Gronwall conclusion is superseded by Step 20. The curvature reaction must first be absorbed through the full-support small critical energy, yielding a triangular finite-neighbor inequality for local unweighted defect energies. Only that strengthened estimate gives Q(t) ≤ e^{Cθ}Q(0) without an additive curvature-dissipation error.

---

## 7. Topological uniformity (from Step 18, corrected)

For critical Ishida–LeBrun manifolds with minimal general-type summands X_j and b₊(N) = 0:
$$
\frac{\chi(M)}{A} \le \frac{65}{6},
\qquad
\bar{K} = \frac{\int_M |\operatorname{Rm}|^2}{\operatorname{Vol}(M)}
\le \frac{8\pi^2 \chi(M) + C \operatorname{Vol}}{\operatorname{Vol}(M)}
\le C(1 + \chi/A).
$$
So K̄ ≤ C is uniformly bounded, and the Li radius r_* is universal for this subclass.  If the conditional first-exit closure is established, the pinching gap would be **uniform across this family**, not merely fixed-topology.

---

## 8. Current status

**Established (unconditional):**
- Volume-independent β in 4D: β ≤ C√ε_Li
- p > 4 threshold for connection/Hessian drift integrability
- p > 2 threshold for metric drift integrability
- Coupled L² energy as a bootstrap lemma (conditional on first-exit geometry)
- Fixed-p spatial Lᵖ propagation for U = aE (conditional on first-exit)
- 7/24 calibration inequality for evolved metrics (from topology)
- Triangular global L² defect preservation, conditional on full-support small-energy/Sobolev absorption (Step 20 replacement)
- Exponential-pullback averaging lemma (Step 16)
- Local projector/Derdziński contradiction on noncollapsed patches (Step 6)
- Noether bound χ(M)/A ≤ 65/6 for the standard subclass (Step 18)

**Step 20 replacement tasks:**
1. Complete the finite-neighbor weighted Wang recurrence from fixed q=2,3 curvature moments to |χ²Rm| and from J₆ to |χ²E|, retaining nested spatial/time cutoffs and evolving measure.
2. Adapt Wang's qualitative smooth-extension induction to the normalized cutoff flow −2χ²(Ric+g). Quantitative weighted Bernstein is optional rather than load-bearing for this zero-order closure.

The 4D Sobolev-energy cancellation and the exact cutoff powers provide the structural mechanism.

---

## Evidence

- `workspace/scripts/verify_step19_p4_threshold_and_bernstein.py`: confirms all drift exponents, p > 4 threshold, connection/Hessian scaling
- `workspace/scripts/verify_step19_volume_independent_beta.py`: confirms volume cancellation, β scaling, numerical closure
- Independent TTCS verification: `trace/ttcs/results/step19_ttcs01_verifier1_integration.md` and branch records
- Prior steps: Step 14 cutoff-flow homogeneity, Step 15 L² chain, Step 16 exponential-chart, Step 17 coupled energy, Step 18 fixed-p and Noether
- Sources: Wang `\cite{wang2009pseudolocality}` Thm 6.3, Li `\cite{lismoothing}` Thms 2.5/3.4/Cor 3.5

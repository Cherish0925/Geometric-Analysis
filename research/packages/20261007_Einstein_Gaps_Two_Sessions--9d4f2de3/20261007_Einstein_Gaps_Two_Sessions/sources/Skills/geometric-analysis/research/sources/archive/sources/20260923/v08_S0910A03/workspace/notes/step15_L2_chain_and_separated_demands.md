# Step 15: L² completion-square chain, separated analytic demands, and the precise remaining conditional

> **Step 16 correction.** Sections 10--13 below are withdrawn. The localized Li argument has a domain mismatch: a supremum over all centers in `Omega_work` needs adjacent covering balls beyond its boundary, while restricting to `Omega_inner` recreates the uncontrolled inner/outer energy problem. Ricci flow has no finite propagation speed, so the numerical buffer calculation does not remove transition influence. The fixed-topology gap asserted in Sections 12--13 is not established. The metric-by-metric L² calibration inequality in Section 1 remains valid. See `workspace/notes/step16_preceptor_correction_exponential_chart_and_cutoff_targets.md` for the corrected transition-inclusive target and exponential-pullback reconstruction lemma.

## 0. Purpose and correction

This note develops the Strategist's observation that **global L² defect preservation suffices for the topological near-saturation argument**, which is strictly weaker than the pointwise O(δ) global control previously targeted. The completion-square chain is a universal metric-independent inequality requiring NO volume control as additional input. The TTCS verifier confirmed all steps and improved the chain constant from ≈0.41 to 7/24. Combined with A01's cutoff smoothing architecture, this separates the three analytic demands more cleanly and identifies the precise remaining conditional.

Step 13's inner/outer L² Gronwall and numerical absorption factors are superseded by this note and the Step 14 Cor 3.5 reconstruction. Step 12's dismissal of smoothing is also corrected.

## 1. The L² completion-square chain (universal, metric-independent)

**Theorem 1 (L² chain).** On a fixed critical Ishida-LeBrun 4-manifold M with 2χ+3τ = 2A/3, for ANY smooth Riemannian metric g on M and E = Ric_g + g:

(a) (Chern-Gauss-Bonnet) I - R = 2A/3 where I = (4π²)⁻¹∫(s²/24 + 2|W⁺|²) dμ and R = (8π²)⁻¹∫|Ric₀|² dμ.

(b) (Seiberg-Witten monopole) K ≥ A where K = (72π²)⁻¹∫(s - √6|W⁺|)² dμ. This holds for every metric g on M (the sign-averaging argument selects a monopole class depending on g, but the bound K ≥ A is metric-independent).

(c) (Completion square upper bound)
$$
\int_M (s + 8\sqrt{6}|W^+|)^2 \, d\mu \le 108 \int_M |E|^2 \, d\mu.
$$

(d) (Weyl modulus estimate, volume-independent)
$$
\int_M \left(|W^+| - \frac{1}{2\sqrt{6}}\right)^2 d\mu \le \frac{7}{24} \int_M |E|^2 \, d\mu.
$$

**Proof of (c).** From the algebraic identity (verified computationally):
$$
27\left(\frac{s^2}{24} + 2w^2\right) - (s - \sqrt{6}w)^2 = \frac{1}{8}(s + 8\sqrt{6}w)^2,
$$
integrating gives ∫(s + 8√6|W⁺|)² = 8·36π²(3I − 2K). With I = 2A/3 + R and K ≥ A:
3I − 2K ≤ 3(2A/3 + R) − 2A = 3R.
So ∫(s + 8√6|W⁺|)² ≤ 864π²R = 108∫|Ric₀|². Since |Ric₀|² = |E₀|² ≤ |E|², the bound follows. □

**Proof of (d) with improved constant.** Set q = s + 4 = tr(E) and v = |W⁺| − 1/(2√6). Then s + 8√6|W⁺| = q + 8√6v. Using the trace-traceless decomposition Q = ∫|E|² = P + X/4 where P = ∫|Ric₀|² and X = ∫q²:

From (c): ‖q + 8√6v‖₂ ≤ √(108P).
Triangle inequality: 8√6 ‖v‖₂ ≤ √(108P) + ‖q‖₂ = √(108P) + √X.

By Cauchy-Schwarz on (√(108P), √X) dotted with (1,1):
(√(108P) + √X)² ≤ (108 + 1)(P + X) = 109(P + X).

But P + X ≤ P + 4(Q − P) = 4Q − 3P ≤ 4Q. So we'd get 109·4Q/384... which is worse.

Instead, using (√(108P) + √X)² ≤ (108 + 4)(P + X/4) = 112Q:
384 ‖v‖₂² ≤ 112Q, giving ‖v‖₂² ≤ 112Q/384 = 7Q/24. □

Note: the constant 7/24 ≈ 0.292 is sharp within this method (TTCS-verified).

**Volume recovery** (NOT an additional input; follows from Q → 0):
If ∫|E|² → 0 on a fixed manifold, then ∫|s+4|² ≤ 4∫|E|² → 0 and the energy profiles converge:
$$
R → 0, \quad I → 2A/3, \quad \text{Vol} → 32π²A/9.
$$
Volume boundedness is derived, not assumed.

## 2. Application to cutoff-smoothed metrics

**Key structural observation**: The L² chain holds for EVERY smooth metric on M, including metrics produced by a cutoff flow ∂_t g = −2χ²E. Since the cutoff flow acts on the original closed manifold M and produces a smooth metric g(t) on M for short time, the chain applies at every time:

$$
\int_M \left(|W^+_{g(t)}| - \frac{1}{2\sqrt{6}}\right)^2 d\mu_{g(t)} \le \frac{7}{24} \int_M |E(t)|^2 \, d\mu_{g(t)}.
$$

**This eliminates the need to transport W⁺ data through the flow.** The calibrated Weyl profile is recovered from topology + small L² defect, not from metric comparison.

## 3. Three separated analytic demands

The Strategist's key insight is to separate the program into three demands with different analytic requirements:

### Demand A: Metric equivalence (weighted pointwise)
**What**: g(t) is uniformly bilipschitz to g(0) on the whole manifold.
**Why needed**: Preserve the volume of the plateau; ensure bounded-curvature regions remain definite volume.
**What it requires**: ∫₀ᵗ χ²|E(τ)| dτ → 0 uniformly. On the plateau (χ=1), Li's Cor 3.5 gives |E(τ)| ≤ Cδ(r²/τ)^{2/3}, which is integrable and yields O(δr²). In the transition, χ² < 1 suppresses the metric change. The frozen exterior (χ=0) is unchanged.
**Analytic difficulty**: LOW (follows from the plateau estimate once the curvature bootstrap closes).

### Demand B: Global L² defect preservation (unweighted global)
**What**: Q(t) = ∫_M |E(t)|² dμ(t) → 0 as δ_i → 0, uniformly for t ∈ [0,T].
**Why needed**: Restores the calibrated Weyl profile and all Chern-Weil/monopole near-saturation.
**What it requires**: The integrated defect-energy inequality has the right homogeneous structure (no additive source independent of E). The Hessian-cutoff terms cancel after integration by parts (verified in Step 14).
**Analytic difficulty**: MEDIUM. The TTCS generator showed that the critical term ∫χ²|Rm||E|² can be absorbed by the gradient dissipation using a local normalized Sobolev quadratic form, PROVIDED the local normalized curvature energy remains small during the flow. This is the curvature bootstrap.

### Demand C: Parabolic plateau regularity (pointwise on χ=1)
**What**: On each plateau (χ=1), the smoothed metric has bounded curvature and small pointwise Einstein defect.
**Why needed**: Produces the bounded-curvature input for CFG accessibility and the local Einstein limit for the forbidden germ.
**What it requires**: Li's Theorem 3.4 (localized to the plateau) for bounded curvature; Li's Cor 3.5 for the defect.
**Analytic difficulty**: This is the LOAD-BEARING unresolved piece.

## 4. The single-ball Sobolev absorption mechanism (TTCS generator)

The TTCS generator identified the correct mechanism for closing Demand B.

On a maximal-function good ball B_{2ρ}(p) with cutoff χ supported inside:

$$
\frac{dQ}{dt} + c_0 \int \chi^2 |\nabla E|^2 \le C(1 + D^{-2})Q + C \int \chi^2 |\text{Rm}| \, |E|^2.
$$

Using the relative Sobolev inequality with v = χ|E|:

$$
\int \chi^2 |\text{Rm}| \, |E|^2 \le \|\text{Rm}\|_{L^2(B_{2ρ})} \cdot \|\chi E\|_{L^4}^2 \le C_S \varepsilon^{1/2} \left(\|\nabla(\chi E)\|_2^2 + ρ^{-2} \|\chi E\|_2^2\right)
$$

where ε = ρ⁴ fint|Rm|² is the **normalized local curvature energy**. The volume cancels:
$$
\|\text{Rm}\|_{L^2} \cdot V^{-1/2} = (V \cdot \fint|Rm|^2)^{1/2} \cdot V^{-1/2} = (\fint|Rm|^2)^{1/2},
$$
and the Sobolev coefficient C_S ∼ ρ²/V^{1/2} provides the matching V^{-1/2}.

For ε sufficiently small (choosing r_* small enough), the gradient term is absorbed:

$$
C_S \varepsilon^{1/2} < c_0/2 \implies \frac{dQ}{dt} \le C(1 + ρ^{-2})Q.
$$

Gronwall over t ∈ [0, θρ²]: **Q(t) ≤ C_θ Q(0) = O(δ²Vol)**.

**The crucial condition**: the normalized curvature energy ε(t) must REMAIN small during the flow. This is exactly the curvature-energy bootstrap (Demand C).

## 5. The coupled bootstrap system

The TTCS generator formulated the precise remaining analytic object as a coupled system. For each covering center α, define:

$$
R_α(t) = \frac{ρ^4}{V_α(0)} \int φ_α^2 |\text{Rm}(t)|^2, \qquad P_α(t) = \frac{ρ^4}{V_α(0)} \int φ_α^2 |E(t)|^2,
$$

with R(t) = sup_α R_α(t), P(t) = sup_α P_α(t).

The bootstrap requires:
$$
D^+P \le Cρ^{-2} P, \qquad D^+R \le Cρ^{-2}(R + P).
$$

The second inequality involves:
1. ∫χ²|Rm|³ absorbed by Sobolev from R^{1/2} smallness (critical 4D)
2. ∇χ · ∇E · Rm terms handled by |dχ|²/χ = 4|dχ|² identity
3. ∇²χ · E · Rm giving Cρ⁻²(∫|E|² + ∫|Rm|²)
4. Adjacent-ball terms closed by the sup and buffered covering
5. Metric equivalence preserving volume normalization and Sobolev short-time

If the coupled system closes: P(t) ≤ e^{CT/ρ²} P(0) and R(t) ≤ e^{CT/ρ²}(R(0) + CTP(0)/ρ²). Since R(0) is within threshold and P(0) = O(δ²ρ⁴), both remain controlled.

## 6. Monopole/eigenline passage under L² convergence

The Strategist asks whether the Weyl-modulus L² estimate alone yields the forbidden spectrum. The TTCS verifier's answer: **NO, additional input is needed.**

The same modulus |W⁺|² = 1/24 can correspond to different spectra, e.g., (-1/6, 1/12, 1/12) or (1/(4√3), -1/(4√3), 0). The forbidden spectrum requires additionally:
$$
\det(W^+) = -\frac{|W^+|^3}{3\sqrt{6}},
$$
which is the EXTREMAL determinant for given modulus (two eigenvalues equal, one simple).

**This extremality comes from the monopole near-saturation**, not from the Weyl modulus alone. The mechanism is:

1. The Seiberg-Witten harmonic form ω_a (for a monopole class a) is a GLOBAL harmonic self-dual 2-form on M.
2. Near-saturation forces ω_a to concentrate in the lowest W⁺-eigenline.
3. On the smoothed bounded-curvature metric, ω_a is smooth with bounded gradient (Bochner estimate).
4. By unique continuation for harmonic forms on connected manifolds, ω_a ≠ 0 almost everywhere (it can't vanish on an open set without being identically zero).
5. On the noncollapsed CFG cover of a plateau ball, the pullback of ω_a is nonzero.
6. At the local Einstein limit, the pulled-back form is a nonzero harmonic self-dual form in the lowest W⁺-eigenline, forcing the two-eigenvalue spectrum.

The complete chain for the eigenvalue structure is therefore:
- L² chain (Theorem 1) → Weyl modulus
- Bounded curvature + unique continuation → nonvanishing harmonic form
- Monopole near-saturation → form in lowest eigenline
- Two distinct constant eigenvalues → ∇W⁺ = 0 (projector lemma, Step 6)
- Einstein-Weyl → |∇W⁺|² = 1/16 (contradiction)

The passage from L² to eigenvalue DOES require bounded curvature and the CFG noncollapsed cover. This is Demand C.

## 7. Complete architecture and the precise conditional

**Conditional Theorem.** Let M^4 be a fixed critical Ishida-LeBrun manifold (D = A/3, no Einstein metric). If the localized Li curvature-energy bootstrap (the coupled system in Section 5) can be closed on the plateau of the normalized cutoff flow, then:

inf_g ‖Ric_g + g‖_∞ > 0,

i.e., M does not admit metrics with arbitrarily tight negative Ricci pinching.

**Architecture of the conditional proof:**
1. Good-set packing: maximal function + Vitali → definite-volume disjoint good balls (ESTABLISHED)
2. Interior Li condition: BG comparable-ball ratio × r*⁴ → small dimensionless energy at all covering centers (ESTABLISHED, A01 Section 2.4)
3. Cutoff flow: ∂_t g = -2χ²E on M, homogeneous in E, frozen exterior (ESTABLISHED)
4. Curvature bootstrap: localized Li Thm 3.4 on each disjoint plateau → |Rm(t₀)| ≤ C/t₀ (CONDITIONAL)
5. Defect propagation: Li Cor 3.5 → |E(t₀)| ≤ C_θ δ, volume-independent (CONDITIONAL ON 4)
6. Global L² chain: ∫|E(t₀)|² ≤ C_θ δ² Vol → calibrated Weyl profile from topology (ESTABLISHED unconditionally; the Q(t) estimate follows from 4)
7. Metric equivalence: ∫₀^{t₀} |E| dt = O(δr*²) → bilipschitz (FROM 5)
8. CFG accessibility: bounded curvature (4) + collapse → nilpotent covers → noncollapsed patches (ESTABLISHED from standard theory)
9. Harmonic form: unique continuation → ω_a ≠ 0 a.e. on bounded-curvature manifold (ESTABLISHED)
10. Forbidden germ: noncollapsed Einstein limit + nonvanishing form + calibrated spectrum → ∇W⁺ = 0 vs |∇W⁺|² = 1/16 (ESTABLISHED, Step 6)
11. Volume contradiction: forbidden germ excludes noncollapsed covers → but CFG guarantees them on definite volume (CONTRADICTION)

**The single remaining conditional is Step 4: the localized curvature-energy bootstrap.**

## 8. Comparison with A01 and peer status

A01's Step 15 architecture (msg #267, note step15_cutoff_smoothing_architecture.md) is essentially the same program with equivalent conclusions. Key points of alignment:
- The all-centers Li condition through comparable-ball BG ratio (A01 Section 2.4 = our §4)
- The volume cancellation in the critical Sobolev product (A01 Section 4.1 = our §4)
- The calibration from topology (A01 Section 5 = our §1-2)
- The remaining conditional: localized Li Thm 3.4 (A01 Section 8 = our §5)

A03's additions beyond A01:
- The L² chain Theorem 1 with sharp constant 7/24 (TTCS-verified)
- The explicit three-demand separation (Strategist's insight)
- The coupled bootstrap system formulation (TTCS generator)
- The monopole/eigenline passage analysis (TTCS verifier + Strategist's question)
- The unique continuation argument for nonvanishing harmonic forms

A02 is independently working on the positive branch via toric methods (msgs #265-266).

## 9. Evidence paths

- This note: `workspace/notes/step15_L2_chain_and_separated_demands.md`
- Computational verification: `workspace/scripts/verify_L2_completion_square_chain.py`
- Step 14 cutoff analysis: `workspace/notes/step14_cutoff_smoothing_and_cor35_reconstruction.md`
- Step 6 forbidden germ: `workspace/notes/step6_local_projector_obstruction_and_collapse_reduction.tex`
- Step 3 near-saturation: `workspace/notes/step3_boundary_near_saturation.tex`
- Step 4 Weyl profile: `workspace/notes/step4_weyl_profile_and_bubble_restriction.tex`
- TTCS integrations: `trace/ttcs/results/step15_ttcs01_generator1_integration.md`, `step15_ttcs01_verifier1_integration.md`
- A01 architecture: `Sessions/S0910A01/workspace/notes/step15_cutoff_smoothing_architecture.md`
- Li source: `Knowledge/objects/papers/0911.3104-Smoothing-Riemannian-Metrics-with-Bounded-Ricci-Curvatures-in--fc5404da6e14--415cdf5be1eb/object.md`


## 10. The localized bootstrap: why Li's proof applies on the plateau

### 10.1 The key observation

Li's Theorem 3.4 proof (source lines 228-258) uses the supremum over all centers of M only for one purpose: to ensure that the covering argument in lines 232-233 can be applied at EVERY center. On our plateau, the covering can be performed entirely within the plateau, so the global supremum is unnecessary.

Specifically: set the inner plateau Ω_inner = B_{ρ/8}(p_j) and the working domain Ω_work = B_{ρ/4}(p_j), where the cutoff flow equals the normalized Ricci flow (χ ≡ 1 on Ω_work). Since r_* ≪ ρ/4 (by construction):

- For any x ∈ Ω_inner, B_{r_*}(x) ⊂ B_{ρ/8+r_*}(p_j) ⊂ Ω_work.
- For the covering: B_{2r_*}(x) ⊂ ∪B_{r_*}(y_i) with y_i ∈ B_{3r_*/2}(x) ⊂ B_{ρ/8+3r_*/2}(p_j) ⊂ Ω_work.
- All covering balls: B_{r_*}(y_i) ⊂ B_{ρ/8+5r_*/2}(p_j) ⊂ Ω_work.

**Therefore the covering argument uses ONLY balls within Ω_work, where the flow is the standard normalized Ricci flow. No cutoff terms, no transition effects.**

### 10.2 The localized bootstrap parameter

Define:
$$
e_0^{\rm loc} = \sup_{x \in \Omega_{\rm work}, \, 0 \le t \le T'} \left(\int_{B_{r_*}(x)} |\text{Rm}(t)|^2 \, d\mu_t\right)^{1/2}.
$$

**Initial condition** (from A01 Section 2.4, our Section 4): For all x ∈ Ω_work,
$$
\left(\int_{B_{r_*}(x)} |\text{Rm}(0)|^2\right)^{1/2} \le (6C_0 A_x)^{-1}
$$
where A_x = Cr_*²/Vol(B_{r_*}(x))^{1/2} is the local Sobolev coefficient. This uses the maximal-function good point condition at p_j and the comparable-ball BG ratio.

**Bootstrap threshold**: e_0^{loc} ≤ (3C_0 A)^{-1} (doubled from initial).

### 10.3 Why the proof goes through

Li's proof has five steps, all local:

**Step 1 (Energy evolution, line 231).** For cutoff φ supported in B_{r_*}(y_i) ⊂ Ω_work:
$$
\frac{\partial}{\partial t} \int \phi^{q+2} f^p + \int |\nabla(\phi f^{p/2})|^2 \le C_{p,q} \|\nabla\phi\|_\infty^2 \int \phi^q f^p.
$$
This is a LOCAL estimate on B_{r_*}(y_i). Under the normalized Ricci flow on Ω_work, this follows from the standard computation with f = |Rm| satisfying ∂_t f ≤ Δf + C_0 f² (the -2f from normalization is dropped as favorable). ✓

**Step 2 (Covering, lines 232-234).** Choose φ and use the bounded covering of B_{2r_*}(x) by N balls. ALL covering balls are inside Ω_work. ✓

**Step 3 (Energy propagation, lines 235-243).** The growth of ∫_{B_{r_*}(x)} f² is bounded by 2N‖∇φ‖²_∞ (e_0^{loc})² t, using data from adjacent balls within Ω_work. The bootstrap: if e_0^{loc}(0) ≤ (6C_0A)^{-1}, then for T' < Cr_*², e_0^{loc} < (3C_0A)^{-1}. ✓

**Step 4 (L³ estimate, lines 246-254).** Uses the Sobolev inequality on B_{r_*}(y_i) ⊂ Ω_work and the bootstrap bound on e_0^{loc}. ✓

**Step 5 (Moser iteration, lines 255-258).** Yields |f(x,t)| ≤ C_1/t for x ∈ Ω_inner, 0 < t < C_2 r_*². ✓

**Critical point**: No step uses data from outside Ω_work. The parabolic propagation distance during 0 < t < θr_*² is O(r_*), which is ≪ dist(Ω_inner, ∂Ω_work) = ρ/8.

### 10.4 Metric equivalence

Under the normalized flow ∂_t g = -2E on Ω_work:
$$
\left|\log\frac{g(t)(v,v)}{g_0(v,v)}\right| \le 2\int_0^t |E(\tau)| \, d\tau.
$$

Initially |E| ≤ δ_i. After Cor 3.5 (applied using the bootstrap above):
$$
|E(x,t)| \le C\delta_i (r_*^2/t)^{2/3}.
$$

The metric drift: 2∫₀^t Cδ_i(r_*²/τ)^{2/3} dτ = 6Cδ_i r_*^{4/3} t^{1/3} = O(δ_i r_*²) → 0. So the metric equivalence ½g₀ ≤ g(t) ≤ 2g₀ holds for δ_i small enough. This preserves the Sobolev inequality and volume comparisons.

**The key advantage**: the metric equivalence depends on the DEFECT E (which is O(δ_i), small), not on the full curvature |Rm| (which is O(1/t), large). The normalized flow separates these two scales.

### 10.5 Volume form

Under normalized flow: ∂_t dμ = -(s+4) dμ = -τ dμ with |τ| ≤ 2|E| ≤ Cδ_i. So the volume form changes by factor exp(O(δ_i t)) ≈ 1. Li's condition ∂_t dV ≤ cf dV (line 222) holds with c = C (since |∂_t dV/dV| = |τ| ≤ 2|E| ≤ C|Rm| for near-Einstein metrics).

### 10.6 The localized proposition

**Proposition (Localized plateau smoothing).** Let (M^4, g_i) be a sequence of closed Riemannian 4-manifolds with |Ric + g_i| ≤ δ_i → 0. Let p_j ∈ M_i be a maximal-function good point with M₁(|Rm|²)(p_j) ≤ K₀. Let r_* = r_*(K₀, ε_Li) be the Li scale from Section 2.4. Let ∂_t g_i = -2χ²(Ric+g_i) be the cutoff flow with χ=1 on B_{ρ/4}(p_j). Then for 0 < t < C₂r_*²:

$$
\sup_{B_{ρ/8}(p_j)} |\text{Rm}(g_i(t))| \le \frac{C_3}{t}, \qquad
\sup_{B_{ρ/8}(p_j)} |\text{Ric}_{g_i(t)} + g_i(t)| \le C_\theta \delta_i.
$$

The first estimate follows from Li's Theorem 3.4 applied on Ω_work = B_{ρ/4}(p_j) with the localized bootstrap (Section 10.3). The second follows from Li's Corollary 3.5 applied to u = |E| with the curvature potential f = |Rm| (now controlled by the first estimate).

### 10.7 Why the global supremum is not needed

Li's original proof uses the global supremum to guarantee:
1. Energy cannot leak in from uncontrolled regions.
2. The bootstrap holds at EVERY center simultaneously.

In our setting:
1. Energy cannot leak in because the exterior is FROZEN (χ=0 outside B_{ρ/2}) and the flow on the plateau is a genuine Ricci flow. The parabolic finite propagation speed ensures independence from the boundary.
2. The bootstrap only needs to hold at centers inside Ω_work, and the all-centers condition at these centers is established by the maximal-function good point + BG comparison.

The localization is not a weakening of Li's theorem but an observation that its proof structure is inherently local. Li takes the global supremum for convenience in the statement, not because the proof requires global data.


## 11. Flow conversion and the metric equivalence advantage

### 11.1 Normalized-to-unnormalized conversion

Li's Theorem 3.1 is stated for the unnormalized Ricci flow ∂_s ḡ = -2Ric_ḡ. For the normalized flow ∂_t g = -2(Ric+g), set ḡ(s) = e^{2t}g(t) with s = (e^{2t}-1)/2. Then ḡ solves the unnormalized flow.

The curvature: |Rm(g(t))| = e^{-2t}|Rm(ḡ(s))| ≈ |Rm(ḡ(s))|/|1+2s| ≈ |Rm(ḡ(s))| for small s.
Li gives: |Rm(ḡ(s))| ≤ C₃/s. Converting: |Rm(g(t))| ≤ C₃/(t(1+2t)) ≈ C₃/t for small t.

The Ricci bound: K = |Ric(g₀)| = |E(0) - g₀| ≤ δ + n = 4 + δ. Li's existence time: T ≥ C₂ min(r_*², K⁻¹) = C₂ r_*² (since r_*² ≪ K⁻¹ ≈ 1/4).

### 11.2 The metric equivalence advantage of normalized flow

Under the normalized flow: ∂_t g = -2E with |E| ≤ δ initially. The metric changes at rate 2|E| = O(δ), giving |log(g(t)/g₀)| ≤ 2δt ≤ 2δθr_*² → 0. **The metric equivalence is NOT a limiting factor** because the driving quantity is the small DEFECT E, not the potentially large curvature.

Under the unnormalized flow: ∂_s ḡ = -2Ric, |Ric| ≤ K ≈ 4. The metric changes at rate ≈ 8, giving equivalence for s ≤ O(K⁻¹). Since T = C₂r_*² ≪ K⁻¹, this is also fine.

### 11.3 Sobolev preservation

The Sobolev constant A(x) = Cr_*²/Vol(B_{r_*}(x))^{1/2} changes under metric equivalence:
- Volume ratio: Vol(t)/Vol(0) ∈ [e^{-Cδt}, e^{Cδt}] ≈ 1
- Radius comparison: B_{r_*}^{g(t)}(x) ⊃ B_{cr_*}^{g_0}(x) for c close to 1
- So A(x,t) ≤ (1+Cδt)A(x,0) ≈ A(x,0)

The product A·e₀ stays below the bootstrap threshold.

## 12. Withdrawn attempted resolution

**Withdrawn in Step 16.** The analysis in Sections 10-11 does not resolve the localized Li curvature-energy bootstrap. The following text is retained only to identify the failed argument. Its asserted observations do not form a proof:

1. **The proof is inherently local**: Li's covering argument uses only balls B_{r_*}(y_i) with y_i within B_{3r_*/2}(x) of the center x. On the inner plateau, these balls stay inside the working domain.

2. **No external contamination**: The parabolic propagation distance O(r_*) is much smaller than the distance from Ω_inner to the transition boundary (ρ/8 ≫ r_*). The frozen exterior and degenerate transition cannot affect the inner plateau during the bootstrap time.

3. **Metric equivalence is automatic**: The normalized flow is driven by the small defect E, not the potentially large curvature. The metric changes by O(δr_*²) over the bootstrap time, which is negligible.

4. **The global supremum is cosmetic**: Li takes sup over all x ∈ M for the statement, but the proof only uses local data within the covering neighborhood.

**Therefore: Proposition A from A01 Section 4.2 is not a separate conditional—it follows from Li's published proof applied to the plateau of the cutoff flow.**

## 13. Corrected status summary (Step 16)

| Component | Status |
|-----------|--------|
| L² chain Theorem 1 (constant 7/24) | **Established** (algebraic, independently checked) |
| Three separated analytic demands | **Formulated** |
| Localized Li bootstrap | **Unproved**; the attempted plateau localization fails by domain mismatch and infinite parabolic propagation |
| Defect propagation (Corollary 3.5) | Conditional on a transition-inclusive dynamic curvature/Sobolev package |
| Global L² → calibrated Weyl modulus | Established at each smooth metric, conditional on terminal global L² defect being small |
| Collapse reconstruction | CFG assertion withdrawn as an automatic step; Step 16 supplies an exponential-pullback averaging lemma conditional on a positive-volume bounded-curvature buffer |
| Harmonic-form amplitude/eigenline passage | Unique continuation is insufficient; Step 16 supplies joint nonnegative densities and a positive-part weight repair conditional on terminal defect and bounded geometry |
| Forbidden germ | Established under the local regular-limit and calibrated-spectrum inputs (Step 6) |
| Fixed-topology gap | **Not established** |

The remaining central analytic problem is a transition-inclusive cutoff-flow existence and continuation theorem on the entire active support, jointly controlling local normalized curvature energy, Sobolev geometry, cutoff derivatives, metric equivalence, and global L² Einstein defect. See `workspace/notes/step16_preceptor_correction_exponential_chart_and_cutoff_targets.md`.

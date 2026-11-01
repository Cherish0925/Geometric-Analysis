# TTCS Independent Branch Record

```json
{
  "step_id": 84,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step83_normalized_action_weyl_deficit_and_AKE_degenerations.md",
    "Sessions/S1003A01/trace/ttcs/results/step83_ttcs01_verifier1_integration.md",
    "Knowledge/objects/papers/2603.09028-Einstein-deformations-of-Kähler-Einstein-metrics--062c0a015de6--2a0f3c1e029d/object.md",
    "Knowledge/objects/papers/Higher-order-obstructions-to-the-desingularization-of-Einstein-metrics--94f76f3b5378--19c12fb27fae/object.md",
    "Knowledge/objects/papers/Almost-Kähler-smoothings-of-compact-complex-surfaces-with-A-1-singulari--577e023dd490--0aaf7a1a8cdc/object.md"
  ]
}
```

## Task

Critically check the Step-83 no-concentration theorem and sharpen it for a one-level A1/Eguchi–Hanson degeneration of closed negative almost-Kähler Einstein four-manifolds. In particular: (i) verify the measure-defect sign argument and extension of the constant-length harmonic form across the orbifold point; (ii) decide exactly what convergence of the forms/torsion is available and what is not (especially normalized torsion direction); (iii) derive the linearized equations for an AKE pair (g_t,omega_t) at a Kähler–Einstein metric in a gauge that distinguishes complex/Kähler tangent directions from genuinely nonintegrable directions; and (iv) analyze what the Eguchi–Hanson core contributes, including its 3-dimensional L2 Einstein kernel and hyperkähler parallel forms. State any correction needed in Step 83 and formulate a rigorously scoped local normal-rigidity proposition whose missing weighted estimate is explicit. Do not infer full local rigidity merely from energy vanishing or action constancy.

## Output

# Memo: Step 83 no-concentration theorem and the one-level A₁ / Eguchi–Hanson degeneration of closed AKE four-manifolds with s<0

## Summary

- **The sign argument and the orbifold extension in Theorem 83.5 are correct.** For one A₁ point they can be sharpened. Matched orientation of the bubble is forced. The vanishing sphere has S·S = −2. W⁺ energy is quantized as m ∈ {0, 12π²}, and only m = 0 occurs.
- **Two convergence statements in Step 83 need correction.**
  - Matching the bubble's parallel form to ω_V(p) requires a neck decay estimate. It is available through an indicial gap (§2).
  - The no-concentration statement controls absolute torsion energy, not the normalized torsion direction.
- **Linearization at a Kähler–Einstein metric (s<0).** In a Koiso–Nagy gauge, the first-order AKE directions split as ε(g) ⊕ Re H^{2,0}. The first summand is integrable. The second consists entirely of nonintegrable directions.
- **Nagy's identity h₂⁺ = h₁².** It is exactly the condition that the fixed form ω₀ remains compatible with g_t to second order.
- **The Eguchi–Hanson core adds no nonintegrable linear directions.** Combined with Ozuch's first obstruction, it forces a smoothing-type geometry (Vernier's picture) when V is Kähler–Einstein.
- **Normal rigidity is reduced to one explicit weighted inequality** for the reduced Einstein–Hilbert action (Proposition P, §5).

Conventions: as in Step 83, |ω|² = 2, with ω self-dual in the orientation of M. Pointwise constants depend on whether |∇ω|² uses the tensor norm or the form norm; no conclusion below depends on that factor.

---

## 1. Measure-defect argument and extension across the orbifold point

### Sign argument

The setting is (N): s ≡ s₀, Vol_n → Vol(V), and smooth convergence on compact subsets of V∖{p}. Splitting the integrals gives

- lim D(g_n) = D(V) − m, with m ≥ 0;
- lim T_AK(g_n) = T_AK(V) + m_T, with m_T ≥ 0, because the density |W₃⁺|² + 3q²/32 is pointwise ≥ 0.

The second limit exists along the subsequence because T_AK(g_n) = D(g_n).

The orbifold identity D(V) = T_AK(V) needs only two things:

- a pointwise algebraic identity;
- one integration of a divergence built from ω_V, ∇ω_V and ∇²ω_V.

Orbifold Stokes applies once ω_V is smooth and Γ-invariant in the chart. Underlying-space characteristic numbers play no role. Then

T_AK(V) + m_T = T_AK(V) − m,

so m = m_T = 0. This is correct.

### Extension across p

1. Lift to B⁴∖0 with Γ = {±1}. The limit metric g_V is smooth in the orbifold chart (orbifold compactness).
2. Since −1 acts trivially on Λ², invariance imposes no constraint on the value ω_V(0).
3. For any test form φ: ∫⟨ω_V, (d+d*)(χ_ε φ)⟩ ≤ C ‖φ‖_{C¹} (ε⁴ + ‖dχ_ε‖_{L¹}) = O(ε³).
4. Hence ω_V is weakly harmonic and lies in L^∞, so elliptic regularity makes it smooth.
5. Closedness, self-duality and |ω_V|² = 2 pass to the extension by continuity.

This is correct as written in Step 83.

### Sharpening for one A₁ point with a single EH bubble

**(a) Orientation and quantization.** Assume Ozuch's description of the degeneration, so that neck energy tends to 0. Then m equals the bubble's W⁺ energy.

- Matched EH (W⁺ = 0 in M's orientation): m = 0.
- Reversed EH: m = ∫|W⁻_EH|² = 8π²(χ(T*S²) − 1/|Γ|) = 12π².

So m ∈ {0, 12π²}, and the identity m = 0 excludes the reversed bubble.

**(b) Topological consistency.**

- Matched EH contributes 2·(3/2) + 3·(−1) = 0 to the curvature integral of 2χ+3τ. This matches T₊(M) = T₊^{curv}(V).
- Reversed EH would contribute 6.
- The vanishing sphere satisfies S·S = −2 in M's orientation. This is the self-intersection of a Lagrangian sphere, consistent with §4.
- b⁺(M) = b⁺(V) and b⁻(M) = b⁻(V) + 1.
- 2χ+3τ of M equals K_V², since the A₁ singularity is crepant.

**(c) A pointwise constraint at the orbifold point.** For a harmonic constant-length self-dual form, Weitzenböck gives

|∇ω|² = 2W⁺(ω,ω) − 2s/3.

With e = ω/√2 and R⁺ = W⁺ + (s/12)·Id on Λ⁺, this yields

R⁺(e,e) = (|∇ω|² + s)/4.

- In the Kähler–Einstein case, R⁺_V(p) = diag(Λ, 0, 0) with first vector ω_V(p) and Λ = s/4.
- For a strict AKE orbifold endpoint, Ozuch's first obstruction requires det R⁺_V(p) = 0, with the gluing direction ζ̂ ∈ ker R⁺_V(p). This applies under the hypotheses of Ozuch's framework (Ozu19b; the 2012.13316 statements assume integrable orbifold deformations). It is a genuine local constraint for the orbifold Goldberg problem.

---

## 2. What convergence is available

### Available without further input

- ω_n → ω_V in C^∞ on compact subsets of V∖{p}, and therefore ∇ω_n → ∇ω_V there.
- T_AK(g_n) → T_AK(V). The torsion density measures converge weakly with no atom at p.
- Since ∫q² is scale-invariant and m_T = 0, the integral of q² over B_δ(p) tends to 0 as n → ∞ and then δ → 0.
- On the rescaled core, ω'_n → ω_∞ with ω_∞ parallel.

### Point 1: torsion on the core is not pointwise small

Unrescaled torsion on the core is |∇ω_n| = o(r_n^{-1}). It is not o(1). Only ∫_core |∇ω_n|² → 0 follows, by Hölder: ∫|τ|² ≤ (∫|τ|⁴)^{1/2} · Vol(core)^{1/2}.

### Point 2: matching ω_∞(∞) with ω_V(p) needs a neck estimate

The bound ∫_neck |∇ω|⁴ → 0 is critical in dimension four. On N dyadic annuli it controls total oscillation only by N^{3/4}(Σ ε_k)^{1/4}, and N ~ log(δ/r_n) is unbounded. Step 83(c) gives a parallel form on the bubble but no relation between that form and ω_V(p).

The missing decay comes from an indicial gap.

- On R⁴/Z₂, self-dual harmonic forms have coefficients that are even harmonic functions, with rates 0, ±2, ±4, ….
- Ozuch's weighted control of the neck gives g_n = e + O(r² + t_n² r^{-4}).
- With this control, the three-annulus argument shows ω_n is within o(1) of a single constant form on the whole neck.

Hence ω_∞ is the hyperkähler form on EH whose asymptotic value is ω_V(p). This lemma should be added to 83.5(c). Without it, the bubble's Kähler direction is undetermined.

### Point 3: the normalized torsion direction is not controlled

The relation m_T = 0 controls the absolute amount of concentrated torsion energy. In the small-torsion regime (Cor. 83.6), T_AK(g_n) → 0 as well, so the fraction of torsion energy inside B_δ(p) is unconstrained.

τ_n/‖τ_n‖ may converge to 0 on every compact subset of V∖{p}, with all of its mass in the neck or core. In that regime 83.5(b) reduces to 0 = 0, and the only surviving content is m = 0.

Step 83 says "torsion … never escape[s] into bubbles". This should read: no positive amount of torsion energy escapes; a fraction of vanishing torsion energy may.

A finite-dimensional substitute for the torsion direction does not concentrate (§4).

- The EH core has no L² self-dual harmonic forms. Its only L² harmonic form Ω is anti-self-dual.
- It also has no decaying self-dual harmonic forms: on EH, ∇*∇σ = 0 makes |σ|² subharmonic.
- Standard weighted Hodge gluing therefore gives isomorphisms I_n : H⁺(V) → H⁺_{g_n}(M) with I_n(α) → α smoothly on the bulk.
- Writing ω_n = I_n(c_n ω_V + Re φ_n) with φ_n ∈ H^{2,0}(V), the normalized direction φ_n/‖φ_n‖ always has a nonzero limit on the bulk.

The torsion splits into two sources:

- ε_n ∇Re φ, spread over the bulk;
- ∇I_n ω_V, generated by the bubble and neck.

The normalized torsion direction is decided by the competition between these two.

---

## 3. Linearized AKE equations at a Kähler–Einstein metric

### Setup

Let (g₀, ω₀, J₀) be Kähler–Einstein with E = s/4 < 0. Unknowns are (h, σ), and J = g^{-1}ω. The AKE system is:

- Ric(g) = (s/4) g;
- dω = 0;
- ω ∈ Λ⁺_g;
- ω ∧ ω = 2 vol_g.

### Gauge

Use Bianchi gauge, fix the volume form pointwise as in Nagy's Lemma 3.7, and take diffeomorphisms preserving the volume form. In this gauge h₁ is TT and lies in Koiso's space ε(g₀).

For E < 0, Nagy's (5) and (17) give:

- ker Δ_E ∩ Sym^{2,+} = 0;
- ε = { h ∈ Sym^{2,−} : ∂̄h = 0, δh = 0 }.

### Algebra

Identify Sym²₀ ≅ Λ⁺ ⊗ Λ⁻. The J-invariant traceless part is ω₀ ⊗ Λ⁻; the J-anti-invariant part is ω₀^⊥ ⊗ Λ⁻.

With J' = (1 − H)(J + S), linearized compatibility J'² = −1 reads JS + SJ = −(H − JHJ). Therefore:

- J-anti-invariant h leaves ω₀ compatible, so σ⁻ = 0;
- J-invariant traceless h forces σ⁻ = h⁺(J₀·,·);
- the length condition gives ⟨σ⁺, ω₀⟩ = ½ tr h.

### First-order solutions

Since h₁ = h⁻, the conditions become σ⁻ = 0, σ closed and self-dual (hence harmonic), and σ ⊥ ω₀ pointwise. Thus

**T₁(AKE at KE) = ε(g₀) ⊕ Re H^{2,0}(g₀)**, modulo Lie derivatives (L_X g, L_X ω₀).

The second summand has real dimension 2p_g = b⁺ − 1.

### Which directions are integrable

- **(h, 0) with h ∈ ε.** These are Koiso's complex-deformation directions. Along them J̇ = −H₁J₀ and σ₁ = 0, since g(1+H)(1−H)J = gJ + O(t²). They are integrable at first order because ∂̄(HJ) = 0.
- **(0, Re φ).** Along a Kähler curve ∇_{g_t} ω_t ≡ 0, so the linearized torsion vanishes on (h, 0). By linearity the linearized torsion of (h, σ) is ∇^{g₀}σ = ∇Re φ.
  - If ∇φ = 0, then |φ| is constant, so i∂∂̄ log|φ|² = 0 forces Ric = 0. This contradicts s < 0.
  - So every φ ≠ 0 is a genuinely nonintegrable direction, and q_t ≥ t²|∇Re φ|² + O(t³).

### Second order

Nagy's Theorem 1.6(i) gives h₂⁺ = h₁². Write J_t = g_t^{-1}ω₀ = (1 + A)J with A = −tH₁ + t²(H₁² − H₂/2).

- J_t² = −1 − A + JAJ + AJAJ.
- The t-term cancels because H₁ is J-anti-invariant.
- The t²-term from B⁺ = H₁²/2 is −2B⁺.
- The term AJAJ contributes t²·H₁JH₁J = t²H₁².
- The h₂⁻ part cancels because it is J-anti-invariant.

So J_t² = −1 + O(t³). With the volume form fixed, ω₀ stays g_t-self-dual of length √2 to second order.

Consequences:

- Every second-order Einstein jet at a Kähler–Einstein metric with s<0, in Nagy's gauge, is automatically an almost-Kähler jet with fixed ω₀ and σ ≡ 0.
- Its second-order integrability defect is the Maurer–Cartan expression (Nagy Rem. 4.9). Nagy (Rem. 4.22) identifies it with the harmonic tensor ∂̄h₂ + [h₁,h₁]^c, up to the change h ↔ −H/2 between parametrizations, whose factor should be checked.
- Consistency check: by 83.1 together with LeBrun's equality rigidity (under the hypotheses of LeBrun's Prop. 4.1), every Einstein curve through such a metric is Kähler–Einstein. So this harmonic tensor must vanish for h₁ tangent to actual curves.

For the direction (h₁, Re φ), the second-order length condition reduces to the pointwise requirement

|Re φ|² + ⟨ω₀, γ(h₁, φ)⟩ = constant,

where:

- γ is the self-dual exact correction closing the algebraically determined form σ₂⁻ = A_{h₁}(Re φ);
- solvability holds because ∫β ∧ dα = 0 whenever (dα)⁺ = 0.

With h₁ = 0 this forces |φ| constant, hence φ = 0. This is a functional obstruction on finite-dimensional data.

### Smooth case

If AKE metrics g_n converge smoothly to a Kähler–Einstein g₀, Theorem 83.1 makes D(g_n) = 0, hence T_AK = 0, for n large. So smooth convergence to a Kähler–Einstein metric forces the AKE structure to be Kähler. Every nonintegrable approach has to pass through an orbifold.

---

## 4. Contribution of the Eguchi–Hanson core

Let ω_∞ = ω_a be the limiting hyperkähler form, with a ∈ S² as determined by §2.

### L² Einstein kernel O(eh)

The kernel has basis o_k = Ω ∘ θ_k⁺. Choose the basis (ζ̂, a, ζ̂×a), which is possible when ζ ⊥ a.

| Kernel direction | Type relative to J_a | Geometric meaning |
|---|---|---|
| o_ζ̂ (size) | J_a-anti-invariant | complex smoothing parameter |
| o_{ζ̂×a} | J_a-anti-invariant | complex smoothing parameter |
| o_a | J_a-invariant | changes the symplectic area [ω]·[S]; forces σ⁻ ∝ Ω |

- The two J_a-anti-invariant directions together form the complex smoothing parameter ε ∈ ℂ* of z₁² + z₂² + z₃² = ε² (Vernier, Remark 12).
- All three directions are integrable. **The core adds no nonintegrable linear directions.**

### Parallel self-dual forms

- The parallel self-dual forms make up a 3-dimensional space; at fixed length √2 they form an S².
- The tangent directions at a are ω_b with b ⊥ a. They are integrable but do not decay; they have weight 0.
- Their asymptotic value must match the bulk value Re φ(p) ∈ ω_V(p)^⊥.
- So bulk nonintegrable directions extend across the core as an integrable rotation of the hyperkähler form. Their nonintegrability is supported in the bulk and the neck.

### Kähler–Einstein limit

In this case ker R⁺_V(p) = ω_V(p)^⊥. Ozuch's first obstruction then gives ζ̂ ⊥ a, so S is ω_∞-Lagrangian.

- The degeneration is of **smoothing type**, as in Vernier's construction, not of resolution type.
- Quantitatively, [ω_n]·[S] = t_n (2π⟨a, ζ̂_n⟩ + o(1)) = o(t_n).
- This is consistent with c₁·[S] = 0.
- Ozuch's second obstruction is then automatic: det of R⁺ on span(ω_V, ζ̂×…) = Λ·0 = 0. Kähler–Einstein orbifold points therefore impose no exclusion through Ozuch's first two obstructions.

### Dichotomy on p_g(V)

- **p_g(V) = 0.** The bulk carries no nonintegrable direction at the linear level. The torsion of a strict AKE metric near V can come only from ∇I_n ω_V, so its normalized profile is expected to localize at the neck. A Vernier-type mismatch gives |N| ~ (gluing radius) in the annulus (Vernier, Lemma 22).
- **p_g(V) > 0.** The directions Re H^{2,0}(V) compete with the neck torsion.

Vernier's constant-Hermitian-scalar-curvature AK smoothings exist with exactly this geometry, including over orbifolds that are not complex-smoothable. Any rigidity argument therefore has to use Ric = (s/4)g, not almost-Kähler moment-map data alone.

---

## 5. Conditional local normal rigidity

### Setting

- (V, g_V, ω_V) is a compact Kähler–Einstein orbifold with s < 0, one A₁ point p, and integrable orbifold Einstein deformations g_v.
- By the orbifold version of 83.1, Ŝ(g_v) = Ŝ(V).
- M is the smoothing, containing the vanishing sphere S.
- By Ozu19a/b, every Einstein metric GH-close to V is, after a diffeomorphism, the Einstein-modulo-obstructions metric ĝ_{ζ,v} with obstruction vector o^A(ζ,v) = 0.
- Define F(ζ,v) := Ŝ(ĝ_{ζ,v})². Volume convergence gives F → Ŝ(V)² as (ζ,v) → 0.

### Missing weighted estimate (W)

There exist C, θ ∈ (0, ½], β ∈ (0,1) and ρ₀ > 0 such that for 0 < |ζ| + ‖v‖ < ρ₀,

|F(ζ,v) − Ŝ(V)²|^{1−θ} ≤ C ‖o^A(ζ,v)‖_{r_D^{-2} C^{0,α}_β(g^D)},

in Ozuch's weighted spaces.

### Proposition P

Assume (W). Then there is a GH-neighbourhood U of V such that every AKE metric on M in U, with a single EH bubble, is Kähler–Einstein.

If V admits no complex smoothing, the conclusion is that U contains no AKE metrics.

**Proof.**

1. For such g, o^A = 0, so (W) gives Ŝ(g)² = Ŝ(V)².
2. Theorem 83.5 gives m = 0, so T₊(M) = T₊^{curv}(V) as a topological identity.
3. Hence D(g) = Ŝ(V)²/16 − 2π² T₊^{curv}(V) = D(V) = 0.
4. Since D = T_AK, the torsion vanishes and g is Kähler.

The conclusion for an arbitrary GH-neighbourhood follows by contradiction along sequences. ∎

### Why m = 0, T_AK → 0 and constancy of Ŝ do not suffice

- m = 0 and T_AK → 0 give only Ŝ(g_n)² − Ŝ(V)² = 16 T_AK(g_n) → 0, with no rate relative to o^A.
- Constancy of Ŝ (Theorem 83.1) holds on connected sets of the smooth moduli space, and g_n is not connected to V inside it.
- A model computation shows what can go wrong. Along a ray ζ = t ζ̂ one has o^A ≈ λt + μt² and F − F(0) ≈ aλt² + bμt³. At a zero of o^A away from λ = 0, F − F(0) need not vanish.

The first obstruction gives λ → 0 but no further control. Closing (W) means controlling F at the critical points accumulating at the stratum ζ = 0.

### Inputs that would give the conclusion

- **Real-analyticity of (ζ,v) ↦ F** in coordinates quadratic in ζ. This would give a Łojasiewicz gradient inequality, and since |dF| ≈ |o^A|, it would give (W). The logarithmic terms in Ozuch's expansions (his Remark 2.11) obstruct plain analyticity.
- **Definability of F** in an o-minimal structure containing such terms, for example ℝ_{an,exp}. Definable C¹ functions have finitely many critical values, which gives the conclusion of P directly, as in Prop. 83.7. This bypasses (W).

### Linear alternative (necessary but not sufficient)

A uniform weighted inverse, in a weight inside the indicial gap, for the linearized AKE system at Vernier-type glued data, transverse to the approximate kernel

(glued ε) ⊕ O(eh) ⊕ Re H^{2,0}(V) ⊕ (rotations),

reduces the problem to a finite-dimensional obstruction map. It then still needs a quantitative nondegeneracy of the obstruction on Re H^{2,0}, which (W) supplies.

**Additional remark.** Suppose V is not complex-smoothable but M is symplectic with b⁺ > 1. If LeBrun's equality rigidity applies, (W) excludes all Einstein metrics with a matched EH bubble near V, not only AKE ones, since D = 0 forces Ŝ² = 32π² c₁².
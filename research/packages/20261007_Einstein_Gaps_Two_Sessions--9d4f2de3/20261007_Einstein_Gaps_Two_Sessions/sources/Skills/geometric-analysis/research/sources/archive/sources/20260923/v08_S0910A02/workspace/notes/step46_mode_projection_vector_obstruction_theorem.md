# Step 46: Mode-Projection Vector-Obstruction Theorem (Conditional)


> **Step 49 correction.** The mode-projection bridge remains valuable exactly as a *first-obstruction* theorem for \(C^0\) Ricci operator pinching. Do not escalate it to second/higher Ozuch obstructions as a way to block near-pinched metrics: after the first obstruction is killed, second and higher residual obstruction tensors vanish in \(\|\operatorname{Ric}-\Lambda g\|_{op}\) as the gluing scale tends to zero, even when they prevent an exact Einstein desingularization. The hard analytic H4_dual problem is the normalized two-scale flux identity \(\mathcal B/t_i^2\), not the unnormalized boundary functional.

> **Step 48 supersession.** The H4 formulation and the Kähler corollary are both replaced by Step 48's construction: `workspace/notes/step48_H4dual_and_biKahler_realizability.md`. H4_dual uses the Ozuch Jacobi field over the entire bubble with a single outer cutoff (not a compactly supported annular test). The bi-Kähler realizability analysis shows that the second-order Ozuch obstruction μ₁ is ALSO structurally vacuous at (S²×S²)/ℤ₂ because R has rank 1. The representation computation (§1) and the window analysis (§3.2) remain valid. The Γ-invariant/curvature-invariance results from Steps 46–47 are preserved and incorporated.

> **Step 47 Preceptor correction.** Sections 4.2--4.4 below contain review-level overstatements. The word "generic" is not legitimate for an orbifold limit supplied by a sequence; the corrected application is a finite dichotomy: either each required bubble direction has \(R_\pm(p)\zeta\ne0\) and is obstructed, or the fixed limit lies in an explicit degeneracy locus at one of finitely many singular points/directions. Also, H4 should not be pursued as a pointwise radial ODE with a uniform source bound, because Step 11's Calderón--Zygmund spike denies the needed uniform second-derivative control. The corrected H4 target is a dual integration-by-parts pairing against compactly supported divergence-free/TT test tensors, moving derivatives onto the test tensor and deriving the one-dimensional mode equation distributionally. Finally, the Step 46 E-type "compatible bubble locus" is misframed for positive Kähler limits: at an orbifold fixed point the curvature block is itself isotropy-invariant in the same spin-2 representation; for E-type the nontrivial block has \(W=0\) and hence \(R=(\Lambda/3)I\), invertible for \(\Lambda>0\). See `workspace/notes/step47_preceptor_review_mode_projection.md` and `workspace/data/step47_curvature_invariant_degeneracy.json`.
Session S0910A02. Agent2/Constructor. Phase Execute.

## 0. Scope

This note states a conditional theorem for the four-dimensional positive noncollapsed branch of Yau-26. It does NOT prove any branch of the full proposition. The active target remains the all-dimensional statement with Lean formalization.

## 1. Representation theory: Γ-invariant l=2 TT harmonics

### 1.1 Setup

For a singularity modeled on C(S³/Γ) with Γ ⊂ SU(2) acting freely on S³, the ALE space is asymptotic to R⁴/Γ with leading TT decay at rate r^{-(l+2)} where l is the lowest angular mode with nontrivial Γ-invariant component. For Γ ⊂ SU(2)\_L, the l=2 TT tensor eigenspace on S³ decomposes into:

- **Self-dual sector** (Λ²₊ ≅ su(2)\_L): Γ acts by Ad, factoring through Γ/{±1} ⊂ SO(3). The Γ-invariant subspace has dimension d^Γ_SD = dim(V₂^{Γ/{±1}}) where V₂ is the 5D (spin-2) representation of SO(3).
- **Anti-self-dual sector** (Λ²₋ ≅ su(2)\_R): Γ acts trivially. Full 5D space is invariant, d^Γ_ASD = 5.

### 1.2 Classification (verified by character computation, `step46_gamma_invariant_l2_modes.json`)

| ADE type | Γ (binary) | Γ/{±1} in SO(3) | d^Γ_SD | d^Γ_ASD | Compatible obs. |
|----------|------------|-----------------|--------|---------|-----------------|
| A₁       | Z₂         | {1}             | 5      | 5       | Full 5D, effective |
| A_k, k≥2 | Z_{k+1}   | Z_{(k+1)/gcd(2,k+1)} | 1–3  | 5 | ≥1D, effective |
| D_k, k≥4 | D*_{k-2}  | D_{k-2}         | 1–2    | 5       | ≥1D, effective |
| **E₆**   | **T***     | **T ≅ A₄**     | **0**  | 5       | **VACUOUS** |
| **E₇**   | **O***     | **O ≅ S₄**     | **0**  | 5       | **VACUOUS** |
| **E₈**   | **I***     | **I ≅ A₅**     | **0**  | 5       | **VACUOUS** |

**Mechanism**: The exceptional groups T, O, I have no invariant direction in their natural 3D representation (the adjoint), and consequently no trivial component in the 5D (spin-2) representation:

- T ≅ A₄: χ₂|_T = ω ⊕ ω² ⊕ 3D, trivial multiplicity = 0
- O ≅ S₄: χ₂|_O = 2D ⊕ 3D, trivial multiplicity = 0  
- I ≅ A₅: χ₂|_I = 5D (irreducible), trivial multiplicity = 0

### 1.3 Consequences for the obstruction

- **AD types in compatible orientation**: Γ-invariant l=2 self-dual modes exist. The ALE asymptotic coefficient ζ^+ lies in a ≥1-dimensional invariant subspace. The vector condition R₊(p)ζ^+ = 0 is nontrivial.
- **E types in compatible orientation**: No Γ-invariant l=2 self-dual mode exists. The ALE leading TT self-dual decay is at l ≥ 4 (rate r^{-6} or faster). The l=2 Wronskian pairing produces no constraint. **First-order obstruction is structurally vacuous.**
- **ALL types in reversed orientation**: The full 5D anti-self-dual space is Γ-invariant. The condition R₋(p)ζ^- = 0 is always nontrivial for nontrivial ζ^-.

This means the theorem below covers AD-type compatible bubbles and all reversed bubbles, but has a structural gap for E-type compatible bubbles (a second exceptional locus beyond the bi-Kähler orbifold locus identified in Steps 44–45).

## 2. Conditional Theorem

**Theorem (Mode-Projection Vector Obstruction, conditional)**

*Let (M⁴, g_i) be a sequence of closed Riemannian 4-manifolds with*
$$\|\operatorname{Ric}(g_i) - \Lambda g_i\|_{\rm op} \le \delta_i \to 0, \qquad \Lambda > 0, \qquad \operatorname{Vol}(M,g_i) \ge v_0 > 0.$$

*Assume:*
- **(H1)** [Cheeger–Naber 2015] The GH limit (X, g_∞) exists, is an Einstein orbifold with isolated singularities p₁,...,p_N modeled on C(S³/Γ_k), and the convergence is C^{1,α} ∩ W^{2,q} away from the singularities. **[PROVED: CN Thm 1.4 + Cor 5.8 + Thm 5.12]**
- **(H2)** [Volume comparison] On each balanced annulus A_R = {R ≤ d(·,p_k) ≤ 2R} with t_k ≪ R ≪ R_macro, the annulus is an almost-volume-cone:
$$\left|\frac{\operatorname{Vol}(A_R)}{\omega_3 R^4/|\Gamma_k|} - 1\right| \le \varepsilon(R)$$
with ε(R) → 0 as R → 0 (from the lower Ricci bound via Bishop–Gromov + Cheeger–Colding). **[PROVED: BG + CC96 almost-volume-cone]**
- **(H3)** [Annular gauge existence] On a selected good dyadic annulus [R, 2R] within the usable window t_k ≪ R ≪ min(t_k^{1/2}, t_k^{2/3}δ^{-1/6}), there exist harmonic coordinates in which the metric satisfies
$$g_{ij} = (g_{\rm cone})_{ij} + h_{ij}, \qquad |h|_{C^{1,\alpha}} \le \eta(R)$$
with η → 0 as i → ∞ (for fixed R). The good annulus is selected by the Cheeger–Naber weak-type estimate: on each dyadic scale, the bad set {r_h ≤ εR} has measure fraction ≤ Cε⁴; with ~½log₂(1/t_k) available scales, one annulus with controlled harmonic gauge exists. **[PARTIALLY PROVED: weak-type selection exists by CN Thm 1.13; the patching to a global annular gauge with controlled metric is CONJECTURAL]**
- **(H4)** [Mode projection and l=2 radial equation] Define the l=2 Γ_k-invariant TT mode function
$$a_i(\rho) = \rho^{-2} \int_{S_\rho/\Gamma_k} \langle g_i - g_{\rm cone}, Y \rangle \, dS_\rho$$
where Y is a unit Γ_k-invariant l=2 TT tensor harmonic on S³/Γ_k (when it exists). **Each smooth metric g_i gives a smooth function a_i(ρ)**; the C^{1,α} convergence issue is only for the limit, not for individual sequence members. Each a_i satisfies the radial ODE
$$a'' + \frac{3}{\rho}a' - \frac{8}{\rho^2}a = S_i(\rho), \qquad |S_i| \le C(\delta_i + |h_i|^2/\rho^2 + \Lambda t_k^2)$$
where the source bound uses the C⁰ Ricci pinching hypothesis (valid pointwise on smooth g_i). **[CONJECTURAL: the precise derivation from the Bianchi-gauged Ricci equation involves (a) the angular projection commutator from higher modes, (b) gauge correction terms from the distance function not being a harmonic coordinate, (c) nonlinear error control. The key simplification is that each g_i is smooth, so the ODE is classical, not weak; the difficulty is transferring it to a coordinate-free setting compatible with the GH convergence.]**

*Then, for each singular point p_k and each ALE bubble of orientation ± and parameter direction ζ^± occurring there:*
$$\mathbf{R}^\pm_{g_\infty}(p_k)\,\zeta^\pm = 0$$
*provided that the l=2 Γ_k-invariant TT harmonic space in the relevant chirality sector is nontrivial (i.e., the obstruction is effective).*

*More precisely: if the l=2 Γ_k-invariant self-dual/anti-self-dual TT space is nontrivial, the Wronskian extraction on the good annulus gives*
$$\alpha_+(R) = \frac{16\,a(2R) - a(R)}{63\,R^2} \to \langle \mathbf{R}^\pm(p_k)\zeta^\pm, \zeta^\pm_{(2)}\rangle$$
*as i → ∞ then R → ∞, with error O(δ_i ln R) + O(R^{-2}) + O(t_k^2R^4).*

### 2.1 Proof sketch

**Step A** (Bridge 1, proved by (H1)+(H2)): The GH limit has isolated singular points. Away from them, the convergence is C^{1,α} ∩ W^{2,q} and the limit is smooth Einstein. If no singularities exist, the limit is smooth Einstein on a manifold diffeomorphic to M (by Cheeger's diffeomorphism stability). Done.

**Step B** (Annulus selection, partially proved by (H3)): The Cheeger–Naber weak-type L² estimate (Theorem 1.13, under |Ric| ≤ 3) gives, in dimension 4,
$$\operatorname{Vol}(T_r\{r_h \le r\} \cap B_1(p_k)) \le C(v)\,r^4.$$
On each dyadic annulus [2^j t_k, 2^{j+1} t_k], the fraction of the annulus where r_h < ε·2^j t_k is at most Cε⁴. With N ~ ½log₂(1/t_k) scales available in the window, a pigeonhole/selection argument produces an annulus where the harmonic coordinates cover at least fraction 1 - Cε⁴ of each spherical shell, with metric C^{1,α}-close to the cone. The conjectural part is patching these local charts to a global annular gauge.

**Step C** (Mode projection and Wronskian, conjectural by (H4)): On the good annulus, project the metric perturbation h_i = g_i - g_cone against the l=2 Γ-invariant TT harmonic Y. The l=2 mode function a_i satisfies the radial ODE by the Bianchi-gauged linearization of the Ricci equation. The homogeneous solutions are ρ² (growing, carrying orbifold curvature) and ρ⁻⁴ (decaying, carrying ALE asymptotic).

The Wronskian W = ρ³(f₁f₂' - f₂f₁') = -6 is constant. On [R, 2R], the growing coefficient is extracted by the formula
$$\alpha_+ = \frac{16\,a(2R) - a(R)}{63\,R^2}$$
which cancels the ρ⁻⁴ contribution. The error from the source term is:
$$|\Delta\alpha_+| \le C\int_R^{2R} |S_i(s)|\,s^{-1}\,ds \le C(\delta_i \ln 2 + |h_i|^2_{L^\infty}\,R^{-2}\ln 2 + \Lambda t_k^2 \ln 2).$$
For fixed R in the window and δ_i → 0, this tends to 0.

**Step D** (Identification): The growing coefficient α_+ in the bubble frame coincides with the Ozuch obstruction coefficient ⟨R^±(p_k)ζ^±, ζ^±_{(2)}⟩ by the structural identity between the indicial root and the curvature tensor pairing. This identification follows from the exact computation of the Ricci-flat ALE asymptotic (Biquard [Biq13], Ozuch [Ozu19a]) and the correspondence between the r² mode on the orbifold side and the curvature endomorphism.

## 3. Annulus window

The usable window for the Wronskian pairing is
$$t_k \ll r \ll \min\bigl(t_k^{1/2},\; t_k^{2/3}\delta^{-1/6}\bigr).$$

**Sources of error** (pairing with test function f₁ = r²):
- Ricci defect: δ∫r⁵dr ~ δR⁶, small when R⁶ ≪ t_k⁴/δ, i.e., R ≪ t_k^{2/3}δ^{-1/6}.
- Quadratic orbifold: |h|²r⁴ with |h|~r², giving R⁸ ≪ t_k⁴, i.e., R ≪ t_k^{1/2}.
- Λ-source: Λt_k²∫r⁵dr ~ Λt_k²R⁶ ≪ t_k⁴, i.e., R ≪ t_k^{1/3}/Λ^{1/6} (subleading when Λ ~ 1).

The number of dyadic scales in the window is ~½log₂(1/t_k), growing without bound as the bubble scale shrinks. The Cheeger–Naber weak-type estimate (requiring only |Ric| ≤ 3, not Einstein) bounds the bad set to relative measure ≤ Cε⁴ per scale. A selection argument across ~½log₂(1/t_k) scales finds a good annulus. This is the mechanism by which Bridge 1 is discharged: not by prescribing a radius, but by selecting one.

## 4. Scope and effectiveness

### 4.1 Where the theorem is effective

| Singularity type | Compatible bubble | Reversed bubble |
|------------------|-------------------|-----------------|
| A_k (all k ≥ 1)  | **Effective** (d^Γ_SD ≥ 1) | **Effective** (d^Γ_ASD = 5) |
| D_k (all k ≥ 4)  | **Effective** (d^Γ_SD ≥ 1) | **Effective** (d^Γ_ASD = 5) |
| E₆               | **Vacuous** (d^Γ_SD = 0)   | **Effective** (d^Γ_ASD = 5) |
| E₇               | **Vacuous** (d^Γ_SD = 0)   | **Effective** (d^Γ_ASD = 5) |
| E₈               | **Vacuous** (d^Γ_SD = 0)   | **Effective** (d^Γ_ASD = 5) |

### 4.2 Known exceptional loci

1. **Bi-Kähler orbifold locus** (Steps 44–45): Orbifolds where R₊ = R₋ = diag(Λ,0,0) everywhere — specifically, quotients of S²(r)×S²(r) under Einstein isometries. Both chiral determinants vanish. The first-order vector condition is satisfied in the kernel directions; the theorem gives directional but not determinantal constraints. Currently, the balanced Z₂ quotient is not proved to realize any #_k(S²×S²) because parity/spin is unresolved.

2. **E-type compatible bubble locus** (this step): For E₆, E₇, E₈ singularities in compatible orientation, no l=2 self-dual harmonic survives the quotient. The leading self-dual TT decay is at l ≥ 4 with rate r^{-6} or faster, and the l=2 Wronskian pairing produces zero signal. A first-order theorem for these types would require pairing against l=4 or higher modes, with different indicial roots and window.

3. **Kähler orbifold locus** (generic case): For a single-Kähler limit, R₊ = diag(Λ,0,0) but R₋ is generic (det R₋ ≠ 0 generically). Compatible (ASD) bubbles are always unobstructed, but reversed bubbles face the full R₋ obstruction. This gives b₊(M) = b₊(O) in the generic Kähler limit — the LeBrun–Ozuch b₊ ≤ 1 conclusion, now derived from the obstruction rather than assumed as admissibility. For generic KE limits with b₊(O) = 1, only ASD bubbles can form, forcing b₊(M) = 1 and excluding #_k(S²×S²) for k ≥ 2.

### 4.3 Kähler dichotomy corollary

**Corollary** (conditional on (H3)–(H4)): *Under the hypotheses of the Theorem, if the GH limit is a positive Kähler–Einstein orbifold with only AD-type singularities, then*
$$b_+(M) = b_+(M_o).$$

*In particular, if b₊(M_o) = 1 (as for del Pezzo orbifolds), then b₊(M) = 1, excluding M = #_k(S²×S²) for k ≥ 2.*

**Proof sketch**: A positive KE orbifold has W₊ = diag(2Λ/3, −Λ/3, −Λ/3) in the (ω, Λ²₊,₀) basis, hence R₊ = diag(Λ, 0, 0). Compatible (ASD) bubbles test R₊ and the 2D kernel always provides a direction, so compatible bubbles are always first-order unobstructed. Reversed (SD) bubbles test R₋ = W₋ + (Λ/3)Id. For a **generic** KE limit, W₋ is unconstrained and det R₋ ≠ 0, so reversed bubbles are first-order obstructed. Consequently, only compatible (ASD) bubbles can form, each contributing (b₊, b₋) = (0, b₂(ALE)) — specifically for the hyperkähler ALE in the SU(2)_L complex orientation: (0, b₂). Therefore b₊(M) = b₊(M_o).

This recovers the conclusion of LeBrun–Ozuch's Theorem 4.1 (b₊ conservation under admissible desingularization) directly from the first-order mode-projection obstruction, without the Hermitian/conformally Kähler admissibility hypothesis. The input is the Cheeger–Naber C^{1,α} convergence plus the mode-projection bridge.

### 4.4 Consequences for the stress family #_k(S²×S²)

Combining the above:
- **Non-Kähler orbifold limits**: Both det R₊ and det R₋ are generically nonzero. All bubble types face nontrivial first-order obstruction. These limits cannot desingularize to #_k(S²×S²) for k ≥ 2 (modulo (H3)–(H4)).
- **Generic Kähler orbifold limits**: By the Kähler dichotomy, b₊(M) = b₊(M_o) = 1. This directly excludes #_k(S²×S²) for k ≥ 2.
- **Bi-Kähler orbifold limits**: R₊ = R₋ = diag(Λ,0,0). Both bubble orientations see a 2D kernel. The theorem gives directional constraints but does not obstruct all configurations. This is the remaining open case.
- **Limits with E-type singularities in compatible orientation**: The l=2 obstruction is structurally vacuous. This is a second open case.

The bi-Kähler locus is classified (quotients of S²(r)×S²(r)); its Z_p quotients may not realize #_k(S²×S²) (evenness unproved). The E-type locus requires higher angular modes (l ≥ 4) for compatible bubbles.

### 4.5 The bi-Kähler classification

An Einstein 4-orbifold Kähler for both orientations has both ω₊ (self-dual Kähler form) and ω₋ (anti-self-dual Kähler form) parallel. The product J₊J₋ is a parallel involution splitting TM into two parallel rank-2 distributions. Einstein + positive scalar curvature + parallel splitting forces equal constant curvature on both factors. So a positive bi-Kähler Einstein 4-orbifold is a finite quotient of S²(r) × S²(r) with r = 1/√Λ, having b₂(O) ≤ 2 and χ_orb = 4/|G|.

This is a small explicit set. Whether its Z_p quotients with mixed-orientation EH resolutions realize the stress family topology as smooth manifolds remains an open combinatorial/topological question (evenness/spin unproved).

## 5. Forward: dimension n ≥ 5

The analytic core — a divergence identity paired against angular modes on a good annulus — is sign-agnostic and does not inherently require dimension 4. What requires dimension 4 is:

- **Codimension-4 singular set is isolated points** (Cheeger–Naber). In n ≥ 5, the codimension-4 singular set can be a **stratum** of dimension n - 4 ≥ 1.
- **S³ cross-sections** of the tangent cones. In n ≥ 5, the cross-sections are higher-dimensional links, and the ALE bubbles are 4-dimensional (with S³/Γ link) attached at points of the stratum.

If the bridge closes in dimension 4, the first extension to ask is: does the pairing become an **integral along the stratum** with 4-dimensional ALE cross-sections? The angular mode on C(S³/Γ) is the same; the additional n-4 directions along the stratum contribute only through the variation of the orbifold curvature R(p) along the stratum. This is a structural question about the interaction of the mode-projection formalism with strata, not a fundamentally different analysis.

## 6. Dependency summary

| Hypothesis | Status | Source |
|-----------|--------|--------|
| (H1) GH limit, codim-4, C^{1,α} convergence | **PROVED** | Cheeger–Naber 2015, Thm 1.4 + 5.8 + 5.12 |
| (H2) Almost-volume-cone on balanced annuli | **PROVED** | Bishop–Gromov + Cheeger–Colding 1996 |
| (H3) Annular harmonic gauge via selection | **PARTIALLY PROVED** | CN Thm 1.13 gives weak-type estimate; patching is conjectural |
| (H3') Enough dyadic scales in the window | **PROVED** | Window analysis: N ~ ½log₂(1/t_k) scales |
| (H4) Mode projection → radial ODE | **CONJECTURAL** | Derivation: angular commutator, gauge correction, nonlinear error. Each g_i is smooth, so ODE is classical. |
| Step D identification with Ozuch | **CONDITIONAL** | Depends on Ozuch [Ozu19a] + Biquard [Biq13,Biq16]; Remark 0.3 extends to general Kleinian Γ via [Biq16, Lemme 9/12]. |
| Γ-invariant l=2 modes | **PROVED** | Character computation (this step) |

The theorem is a conditional result. If (H3) and (H4) are established, it becomes a rigorous theorem covering all AD-type singularities and all reversed bubbles.

## Files

- Representation theory: `workspace/scripts/step46_gamma_invariant_l2_modes.py`, `workspace/data/step46_gamma_invariant_l2_modes.json`
- Annulus window: `workspace/scripts/step46_annulus_window_analysis.py`, `workspace/data/step46_annulus_window_analysis.json`
- Ozuch source: `Knowledge/objects/papers/Higher-order-obstructions-to-the-desingularization-of-Einstein-metrics--94f76f3b5378--19c12fb27fae/object.md`
- Step 42 mode projection: `workspace/notes/step42_mode_projection_bridge_resolution.md`
- Step 45 bi-Kähler review: `workspace/notes/step45_preceptor_review_biKahler_loophole.md`

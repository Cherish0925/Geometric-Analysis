# TTCS Independent Branch Record

```json
{
  "step_id": 56,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step56_common_time_and_terminal_compactness.md",
    "Sessions/S0910A01/workspace/notes/step55_joint_bootstrap_background_continuation_repair.md",
    "Sessions/S0910A01/workspace/notes/step55_finite_restart_threshold_and_C3_exchange.md",
    "Sessions/S0910A03/workspace/notes/step58_critical_to_subcritical_bridge.md",
    "Sessions/S0910A01/workspace/data/step56_common_time_terminal_verify.json"
  ]
}
```

## Task

Verify the common observation time and terminal compactness theorem in the attached note for the restricted IL cutoff flow ∂_t g = -2χ²(Ric+g) in dimension 4.

Key claims to check:

1. §2.5 Smooth convergence at T*: The argument uses H^7 bounds → Sobolev embedding H^7(M^4) ↪ C^{4,α} → Schauder bootstrap on the DeTurck system to get C^∞ convergence. Is H^7 → C^{4,α} correct for n=4? Does the Schauder bootstrap work for the degenerate equation (the coefficient χ² vanishes)? The note says 'in the DeTurck gauge, the system is strictly parabolic after ε-regularization.' Is this sufficient?

2. §2.6 Restart and uniqueness: The pasting argument uses: both solutions arise as ε→0 limits of the unique strictly parabolic ε-regularized DeTurck system, so they agree on the overlap. Is this logically sound? Does it require the ε-regularized solutions to converge uniformly, or is there a subtlety?

3. §4 Terminal compactness: The note claims that bounded curvature K on pullback balls, Rauch noncollapse v₀, and vanishing defect ∫Φ/A→0 suffice for strong W^{2,q}_loc convergence through harmonic coordinates without sequence-uniform derivative bounds. Is this the correct compactness mechanism? Does the upgrade from C^{1,α} harmonic to W^{2,q} to C^∞ on the Einstein limit work?

4. §5 A-cancellation: The global contradiction uses ∫Φ ≤ 119 Q(T) ≤ C δ² A and Vol(P^in) ≥ c₀ A to get mean(Φ) ≤ Cδ²/c₀. Does the A factor cancel correctly? Is the Liouville averaging from Step 53 §7.2 (unit tangent bundle, geodesic flow invariance) correctly invoked for pullback balls under collapse?

5. §2.7 Separation of roles: Verify that no per-datum constant from §2 leaks into the sequence-uniform estimates in §3-§5. In particular, check that the terminal curvature K in §3.1 comes from the first-exit bootstrap (sequence-uniform Γ and θr²), not from the per-datum H^{s₀} continuation.

## Output

## Verifier memo — common observation time and terminal compactness for ∂ₜg = −2χ²(Ric+g), n=4

Orientation. I read the two Step 55 notes, the Step 56 assembly, the Step 58 curvature branch, and the 21-item structural JSON. The overall logical chain in §6.1 is coherent as a conditional architecture, and the arithmetic in the JSON matches the text where I could recompute it. Below I address the five items with the concrete mathematical objects involved, then state what the module reaches relative to the stated research goal. The three imported analytic modules (A per-datum existence, B curvature Moser, C defect Moser) are taken as given, as the note itself marks them not-yet-proven; my remarks concern the reasoning that is written out in Step 56 §2–§5.

---

### 1. §2.5 smoothing at T★

**Sobolev embedding is correct.** On a closed 4-manifold, Hˢ ↪ Cᵏ,α when s − n/2 > k + α. For s=7, n=4: 7−2 = 5 > 4+α for every α<1, so H⁷ ↪ C⁴,α (α<1) as the JSON states. The two thresholds used (s₀ > n/2+2 = 4 in §2.5; s₀ > n/2+4 = 6 for the restart package in Step 55) are both satisfied by s₀=7 with no conflict.

**The Schauder step (2.8) is the delicate one because a = χ² vanishes.** The equation is degenerate parabolic: the DeTurck-gauge principal symbol is a·g^{ab}∂ₐ∂_b, which is only *uniformly* elliptic after the viscosity term, giving (χ²+ε)g^{ab}∂ₐ∂_b. For each fixed ε>0 the regularized system is uniformly parabolic and the two-orders-per-step bootstrap Cᵏ,α→Cᵏ⁺²,α holds — but with ε-dependent Schauder constants that degenerate near {χ=0} as ε→0. Writing "the transported system is strictly parabolic (after ε-regularization)" therefore does not by itself deliver a C^∞ bound on the ε→0 limit g(T★) in the collar and on {χ=0}. As stated, (2.8) treats the equation as if it were uniformly parabolic globally, which it is not.

The conclusion is nevertheless reachable, but by a different route:
- On the interior of {χ=0} the flow is ∂ₜg = 0, so g(t) ≡ g(0), smooth by hypothesis — no elliptic smoothing needed.
- On {χ ≥ c > 0} the equation is locally uniformly parabolic; interior parabolic regularity gives C^∞ with constants depending on dist(·,{χ=0}).
- The genuinely delicate set is the interface where χ→0. Smoothness across it is governed by the vanishing order of the *fixed smooth weight* χ and the smoothness of the data — this is a degenerate-parabolic smoothness statement, not "standard Schauder."

Two clean substitutes exist for the interface: (i) continue the current-pair Hˢ induction to *all* orders (the general pattern in Step 55 §4 is written for every k, so extending beyond s₀=7 gives Hˢ for all s, hence C^∞ by Sobolev, using energy identities on the exact degenerate flow rather than ε-regularized Schauder); or (ii) do not pass to C^∞ at all, and restart from the finite-regularity H⁷/C⁴,α datum if A03 Step 56's local existence theorem accepts finite-regularity initial data. Which substitute is intended matters, because §2.6 then uses "g(T★) is smooth." If the local restart theorem needs only H⁷ (which is what s₀=7 was sized for), then (2.8) is not load-bearing and the degeneracy question is moot; if genuine C^∞ is required, route (i) is the mathematically clean source and (2.8) as written does not supply it.

---

### 2. §2.6 restart and pasting

The pasted function g̃ (original on [0,T★], restart on [T★,T★+ε₁)) is continuous at T★. Being a solution across T★ requires the one-sided ∂ₜg to match there. Both pieces satisfy ∂ₜg = −2χ²E with the common value g(T★), which is at least C² in space, so −2χ²E(g(T★)) is well defined and equal computed from either side; the two one-sided time derivatives coincide and g̃ ∈ C¹ₜ solves the equation at T★. That direct matching is the substance, and it works.

The written justification — "both arise as ε→0 limits of the unique strictly parabolic ε-regularized system with data at τ; parabolic uniqueness on the overlap; ε→0 preserves agreement" — is more convoluted than needed and, as phrased, implicitly requires the ε-regularized solution starting at τ to exist with ε-uniform Hˢ control on a *common* interval [τ, T★+ε₁] and to converge there. That ε-uniform continuation past T★ is exactly what the contradiction argument is trying to establish, so invoking it as justification is close to circular. There is also no true "overlap" between [0,T★) and [T★,T★+ε₁) beyond the single point T★, so "uniqueness on the overlap" is not the operative fact.

The genuinely needed input is **uniqueness for the exact degenerate flow in the Hˢ energy class**: two Hˢ solutions with the same datum agree. This holds by an energy estimate for the difference, using a = χ² ≥ 0 as a fixed smooth weight (the weight is nonnegative and the diffusion is monotone where positive; where χ=0 the equation is a pointwise ODE with unique solution). Recommending this energy-uniqueness statement in place of the ε-limit argument removes the ε-uniform convergence question from both §2.5 and §2.6 at once.

---

### 3. §4 terminal compactness

The mechanism — bounded |Rm|≤K on pullback balls, Rauch noncollapse v₀ on the pullback ball, harmonic coordinates with C¹,α control, elliptic Ricci system, W^{2,q} regularity, subsequential convergence, vanishing defect forcing an Einstein limit — is the standard Anderson–Cheeger harmonic-coordinate compactness, and the decision to work on the exponential pullback (B_ρ(p), (exp_p)★g) in T_pM rather than the image ball is the correct move under collapse: the pullback carries Euclidean-order volume (4.3) regardless of folding. The harmonic-radius lower bound at the center follows from |Rm|≤K plus the center's volume lower bound; propagation of the volume lower bound to interior points of B_{ρ/2} uses Bishop–Gromov, which is available since |Rm|≤K gives Ric ≥ −3K. The buffer condition (Prop 1.2(iii), all geodesics of length ≤ρ inside the plateau) is doing real work: it keeps the geodesics in the region where |Rm|≤K, so the Rauch Jacobian bounds (4.2) apply along them. All of this is sound.

Two points of internal precision:

- **The statement "g_i → g_∞ in C^∞_loc, RHS of (4.4) converging in C^{k,α} for every k" (§4.4) is stronger than the available control and is not needed.** The W^{2,q} bound gives second derivatives of g_i bounded in L^q, hence converging only *weakly* in L^q; the E_i term in the RHS converges strongly only in L² and only because ‖E_i‖_{L²(B_ρ)}→0 is supplied independently by (4.6)/the defect, not by Rellich (Rellich gives strong first-derivative convergence, not strong second-derivative convergence). So the pre-limit metrics g_i converge in C^{1,α′} and W^{2,q}, and their scalar/Weyl parts s_i, W⁺_i (second order) converge weakly in L^q. The *limit* g_∞ is genuinely smooth Einstein (Ric_{g_∞} = −g_∞ weakly ⟹ smooth by elliptic bootstrap in harmonic coordinates), and that is all the germ argument requires.

- The identifications s_∞ = −4, |W⁺_∞|² = 1/24, 𝒢_∞ = 0 under the hypothetical 𝒜_ρΦ→0 should be read through **lower semicontinuity of the L² norms under weak convergence**: ∫(s_i+4)²→0 with weak convergence forces s_∞=−4 a.e., etc. This is consistent with the available second-order convergence and is the correct way to state §4.3–§4.5, in place of "C^∞_loc convergence of g_i."

The forbidden-germ arithmetic is correct. The calibrated spectrum (−1/6, 1/12, 1/12) is traceless with |W⁺|² = 1/36+1/144+1/144 = 1/24; the Ric=−g Kähler-Einstein spectrum (1/3,1/3,−2/3) is traceless with |W⁺|² = 2/3, matching |W⁺|² = s²/24 = 16/24 at s=−4. The contradiction 1/24 ≠ 2/3 is genuine. It can be stated even more directly through the density itself: for a Kähler-Einstein germ with s=−4 one has 8√6|W⁺| = 8√6·√(2/3) = 16, so (s+8√6|W⁺|)² = (−4+16)² = 144, i.e. Φ ≥ 144 there and 𝒜_ρΦ cannot approach 0. Either way the lower control η>0 is robust and does not degrade with the smallness of v₀ (v₀ = 4.73×10⁻⁸ in the JSON is tiny but only forces δ to be correspondingly small along the sequence, which is permitted since δ_i→0).

Caution on imports: the two implications "𝒢=0 ⟹ Kähler (Derdziński)" and the precise definition of 𝒢 are from Step 45 and are not present in the supplied files, so I cannot independently confirm them here. The whole forbidden-germ contradiction rests on those; they should be treated as verified upstream, not by this note.

---

### 4. §5 A-cancellation and Liouville averaging

**Arithmetic cancels correctly.** ∫_M Φ dμ ≤ 119 Q(T) ≤ 119 e^{Cθ}Q(0), Q(0) ≤ δ²Vol(M), Vol/A ≤ C give ∫Φ ≤ Cδ²A; with Vol(P^in) ≥ c₀A the average value ∫_{P^in}𝒜_ρΦ / Vol(P^in) ≤ Cδ²A/(c₀A) = Cδ²/c₀. The A cancels dimensionally, and the incompatibility with 𝒜_ρΦ ≥ η follows for δ < √(c₀η/C).

**The load-bearing inequality (5.3), ∫_{P^in}𝒜_ρΦ(p) dμ(p) ≤ C∫_M Φ dμ, does hold under collapse, and the reason is exactly the pullback formulation.** Writing 𝒜_ρΦ(p) = V_p⁻¹∫_{B_ρ(p)}(exp_p)★(Φ dμ_g) with V_p = Vol_{g̃_p}(B_ρ) ∈ [v₀, C], and using dμ_{g̃_p} = (exp_p)★(dμ_g), one gets

∫_{P^in}∫_{B_ρ(p)}(exp_p)★(Φ dμ_g) dμ(p) = ∫_M Φ(q)·[∫_{P^in} n_p(q) dμ(p)] dμ_g(q),

where n_p(q) counts geodesics of length <ρ from p to q. By the symmetry of the geodesic relation, the inner bracket equals Vol_{g̃_q}({v∈B_ρ⊂T_qM : exp_q v ∈ P^in}) ≤ Vol_{g̃_q}(B_ρ) ≤ C_Rauch, uniformly. Folding of exp_p inflates n_p(q), but this is exactly compensated because the pullback (tangent-bundle Liouville) measure counts the folded sheets with the same multiplicity; the total stays bounded by the tangent-ball volume. This is why the note is right that injectivity of exp_p on the base is not required. The estimate needs |Rm|≤K on the ρ-neighborhood of P^in (for the Rauch Jacobian bounds along all these geodesics), which the buffer condition supplies. The invocation of Step 53 §7.2 is therefore appropriate; the one implicit ingredient worth stating explicitly is that the buffer places the entire ρ-neighborhood of P^in inside the K-controlled plateau, so the multiplicity bound C_Rauch is uniform.

---

### 5. §2.7 separation of the two constant systems

The separation holds as stated. The terminal curvature K in §3.1 comes from ‖aF_T(t)‖_∞ ≤ CΓ/t (Step 58 eq. 4.11) evaluated at t = θr² on {a=1}: |Rm(T)| ≤ CΓ/(θr²) + C_n =: K(γ★,θ,r,n). Here Γ ≤ γ★ is the sequence-uniform first-exit quantity, and θ, r are fixed geography values; none of K_τ, the per-datum Sobolev constant of g(τ), or the current-pair constants of Step 55 enter K. The per-datum constants live entirely in §2 and set only the smooth-existence time, not any terminal magnitude. §3–§5 use Γ, θr², Q(0)/A, and the proportional-volume constant c₀, all sequence-uniform.

One structural remark, not a leak: §3–§5 depend *logically* (not through constants) on §2, because ‖aF_T‖_∞ ≤ CΓ/t is used at t=θr², which presumes smooth existence to θr² — and that is precisely what §2 provides per datum. This is the intended architecture of a common observation time, and the note describes it correctly. Worth confirming upstream that Step 58's Moser endpoint is derived on the smooth-existence interval and that its C, Γ carry no hidden per-datum dependence; the JSON's role-separation item asserts this but does not test it, since the JSON checks are structural/algebraic (its own disclaimer says so).

---

### What this module reaches, and what it does not

Taking modules A, B, C as given, the chain in §6.1 assembles into a single statement: within the specific four-dimensional Ishida–LeBrun connected-sum family with the Ric=−g normalization (q≥0, full monopole sign family), there is an ε>0 depending on the geography data (m, {c₁²(X_j)}, (2χ+3τ)(N)) such that no metric in that family has ‖g⁻¹(Ric_g+g)‖_{∞,op} < ε. The two mathematical repairs I would emphasize before this reads as complete are (i) the C^∞/finite-regularity source for g(T★) in §2.5 (route it through the all-order energy induction or restart from H⁷, not degenerate-Schauder), and (ii) the energy-uniqueness statement for the exact degenerate flow in §2.6 (replacing the ε-limit pasting language). The §4 compactness and §5 A-cancellation are mathematically sound once §4.3–§4.5 are restated with weak-L^q convergence plus L² lower semicontinuity rather than C^∞_loc convergence of the sequence.

Relative to the stated research goal — dimension-only constants c_n < C_n for every n≥2 and *every* closed manifold, with the pinching *producing* an Einstein metric — this module is a different and much narrower object. It concerns one 4-dimensional family, the produced separation ε depends on the geography parameters rather than on n alone (§6.4 states this), the positive Einstein-constant branch is untouched, dimensions n≥5 carry no analogue of the SW/Weyl calibration, and the Lean formalization required by the completion standard is not begun. It also runs in the direction of an obstruction for a sub-family (metrics cannot be too near Ric=−g there) rather than the construction the problem statement asks for; how such an obstruction would be turned into a statement about the Yau pinching hypothesis is not something the supplied files establish. These are the substantive pieces of scientific material that remain between this note and the problem posed.
# TTCS Independent Branch Record

```json
{
  "step_id": 84,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step83_normalized_action_weyl_deficit_and_AKE_degenerations.md",
    "Sessions/S1003A01/workspace/notes/step79_second_tier_dWplus_kodaira_and_log_torsion_identity.md",
    "Sessions/S1003A01/workspace/notes/step80_regularized_torsion_transport.md",
    "Knowledge/objects/papers/2603.09028-Einstein-deformations-of-Kähler-Einstein-metrics--062c0a015de6--2a0f3c1e029d/object.md",
    "Knowledge/objects/papers/Integrability-of-Einstein-deformations-and-desingularizations--8e63541ce32f--b5af64ba3e90/object.md",
    "Knowledge/objects/papers/Higher-order-obstructions-to-the-desingularization-of-Einstein-metrics--94f76f3b5378--19c12fb27fae/object.md",
    "Knowledge/objects/papers/Deformations-of-nodal-Kähler-Einstein-Del-Pezzo-surfaces-with-discrete--9b4cc6f157f8--c134bd6a8c7c/object.md"
  ]
}
```

## Task

Develop the strongest concrete matched-analysis route for the following problem. We have a sequence of closed negative almost-Kähler Einstein four-manifolds converging noncollapsed with bounded diameter to a Kähler–Einstein orbifold with one A1 point, and Step 83 proves that all self-dual Weyl/torsion concentration vanishes and the unique bubble is orientation-matched Ricci-flat Kähler Eguchi–Hanson. We want local exclusion of strict AKE pairs near this one-level degeneration, not finiteness of the entire compactified Einstein moduli. Read the supplied notes and sources. Separate the actual tangent directions (Kähler complex/smoothing deformations and gauge) from a hypothetical nonintegrable AKE normal direction, and derive what a contradiction/blow-up argument would need on the exterior, cone neck, and Eguchi–Hanson core. Identify a precise weighted normal operator, its likely kernel/cokernel, matching data, and one estimate or finite-dimensional map whose proof would settle the local question. Be alert to the fact that negative KE Einstein Jacobi fields are J-anti-invariant Kodaira–Spencer tensors and are tangent to Kähler families, while the AKE torsion is a derivative quantity; do not confuse these. Also incorporate the hyperkähler rotation freedom of Eguchi–Hanson and explain whether it is tangent Kähler/smoothing data or a possible strict-AKE entrance. Produce a mathematical memo with equations and a decisive next calculation, not general advice.

## Output

# Matched analysis for local exclusion of strict AKE metrics near a KE orbifold with one A₁ point

## Summary

- **Main conclusion.** At this one-level degeneration the problem has an exact finite-dimensional reduction, and the only hyperkähler direction that leaves the Kähler family is already Einstein-obstructed with a fixed coefficient s/4.
- **What remains open.** Everything else is controlled by one object: the complex Kuranishi map κ(t,v) of the orbifold V, including the smoothing parameter t. The local question is settled whenever a uniform Łojasiewicz-type statement holds for the reduced Weyl-deficit function at the A₁ end.
- **Case already closed.** When H²(V,Θ_V)=0 the argument in §4 closes completely (Proposition A).

**Setting.** We work with (g_n,ω_n), almost-Kähler Einstein (AKE) with s≡s₀<0, converging noncollapsed with bounded diameter to a Kähler–Einstein (KE) orbifold (V,g_V,J_V) with one point p modelled on ℂ²/ℤ₂. By Step 83 (Theorem 83.5):
- the self-dual Weyl concentration vanishes, m=0;
- T_AK(g_n)→T_AK(V)=0;
- the bubble is Eguchi–Hanson (EH), Kähler for the parallel limit form I of the rescaled ω_n.

The construction parametrizes the Einstein locus near V in Ozuch's one-level chart, separates its directions, and isolates what forces Kählerness.

---

## 1. Matched geometry at p

**Curvature of V at p.** For a Kähler surface with |ω|²=2, W⁺ has eigenvalue s/6 on ω̂=ω/√2 and −s/12 on the plane Λ^{2,0}_ℝ. Hence

  R⁺_V(p) = W⁺ + (s/12)Id = (s/4) Î⊗Î,  Î = ω_V(p)/√2.

This is exactly the form diag(0,0,Λ) with Λ=s/4 in Ozuch's Theorem 0.2, so both of Ozuch's compact obstructions are met automatically by a KE orbifold.

**Eguchi–Hanson parameter.** The EH bubble is eh_ζ with ζ∈ℝ³≅Ω⁺(ℝ⁴/ℤ₂), oriented so the hyperkähler forms are self-dual for the orientation of M. Write ζ=|ζ|φ with φ = cosθ ê + sinθ Î, ê⊥Î, and use the adapted unit frame

  e₁=φ (scale), e₂ = −sinθ ê + cosθ Î (tilt), e₃ = ê×Î (phase).

**First obstruction.** Biquard's first obstruction λ_k = c⟨R⁺(p)φ,e_k⟩, with c≠0 fixed by the normalization of o_k, gives

  λ₁ = c(s/4)sin²θ,  λ₂ = c(s/4) sinθ cosθ,  λ₃ = 0.

Ozuch's estimate t λ_k + t²μ_k = O(t^{5/2}), with t=|ζ| the area scale, then forces θ = O(t), i.e.

  ζ_Î = |ζ| sinθ = O(|ζ|²).

**Interpretation.**
- For complex structures orthogonal to ζ, EH_ζ is the smoothing w₁²+w₂²+w₃²=τ.
- The constraint ζ⊥Î therefore says: an Einstein desingularization is, to leading order, the complex smoothing in the orbifold complex structure J_V(p).
- The parameter is τ = ζ₂+iζ₃ (identifying ζ₂,ζ₃ with the components along ê and e₃ at θ=0), the holomorphic period ∫_E Ω of the vanishing Lagrangian sphere E.
- The crepant resolution (ζ∥Î) is excluded by λ₁ = c s/4 ≠ 0. This is consistent with the absence of a KE metric on the resolution, since K·E=0 there.

**Period of ω on the vanishing cycle.**
- The ω_Î-period of E in the bubble is ∝ ζ_Î.
- For KE metrics, [ω] = (8π/|s|)K and K·E=0, so ∫_E ω = 0 exactly.
- For AKE metrics, Step 79 gives β = γ − (s/4)ω closed and [γ]=2πc₁. Hence

  ∫_E ω_n = (4/|s|)⟨[β_n],E⟩.

So the tilt is read off by a single cohomological quantity built from the torsion-quadratic class [β_n]. The first obstruction bounds it by O(|ζ|²) whatever the AK structure is.

**Neck matching data.**
- Orbifold side (Ozuch, Prop. A.1): H₂ = −(Λ/9)r⁴g_{S³} + (r²/6)(W⁺_{ij}θ_i⁻∘ω_j⁺ + W⁻_{kl}θ_k⁺∘ω_l⁻), with W⁺ = diag(s/6,−s/12,−s/12) in the frame (Î,ê,e₃).
- Core side: H⁴ = −ρ(ζ)⁻∘ζ⁺/(2r⁴), with |H⁴|∼|ζ|²r⁻⁴.
- The only mixed term is Ric°⁽²⁾(H⁴,H₂) = Σ_j R⁺_{kj} θ_l⁻∘ω_j⁺/r⁴, where k is the ζ-direction.
- With R⁺_{kj} = (s/4)δ_{kÎ}δ_{jÎ}, this is (s/4)⟨φ,Î⟩θ⁻∘ω_Î⁺/r⁴. It vanishes on matched configurations, so H₂⁴ = 0 (Ozuch, Lemma 2.3). It is the sole source of λ₂.
- The radial obstruction ΛV(eh) + Q(W⁻_eh, W⁺_V(p)) = 0 holds automatically, because Kähler smoothings exist (Spotti).

---

## 2. Tangent directions versus normal directions

| direction | geometric meaning | status |
|---|---|---|
| v ∈ O(g_V) | Einstein Jacobi fields of the orbifold KE metric, s<0. These are J-anti-invariant, ∂̄-closed, divergence-free (Koiso), ≅ H¹(V,Θ_V) for the reflexive (orbifold) tangent sheaf | tangent to Kähler families when integrable |
| o_{e₁}, o_{e₃} | scale and phase of τ; o_{e₁} ≈ (L_Xg)° with X ∼ r∂_r (Ozuch, Lemma 4.4) | tangent: complex smoothing |
| L_Y g, L_{Y'}g | gauge, and harmonic extensions of the Killing fields of the cone | gauge |
| o_{e₂} | tilt ζ_Î, rotation of ζ toward Î | Einstein-normal, uniformly obstructed: ∂_θ λ₂ = c s/4 |
| ω ↦ ω + ε Re φ, φ ∈ H⁰(K_V) | rotation of the AK form into Λ^{2,0}_ℝ | linearized-AKE kernel with first-order torsion; obstructed at second order (§6) |
| v_⊥ ∈ H¹(Θ_V) with κ₂(v_⊥) ≠ 0 | complex-obstructed Kodaira–Spencer directions | the only conceivable Einstein, non-Kähler entrance |

**Torsion order counting.**
- For a Kodaira–Spencer tensor h, the deformed almost complex structure J_h = (1−h)⁻¹J(1−h) has first-order Nijenhuis tensor ∂̄h = 0.
- Its second-order Nijenhuis tensor is ∂̄h₂ + [h,h]^c. By Nagy (Remark 4.22), its harmonic part is the complex obstruction H([h,h]^c).
- For AK structures |∇ω| ≍ |N|. So along an Einstein-normal deviation of size ε one has q = O(ε⁴), and T_AK ≥ ∫|W₃⁺|² ≍ ‖∂-curl α‖² = O(ε⁴).

Consequently:
- The Weyl deficit of a strict AKE metric near the KE family is a quartic quantity, controlled by |κ|² with κ the complex Kuranishi map.
- Soft compactness (T_AK→0) carries no rate information.
- Nagy's second-order unobstructedness of Einstein deformations (Theorem 1.5) is precisely the statement that the reduced Einstein map has no quadratic term. The first possible Einstein obstruction is cubic and should be the gradient of the quartic |κ₂|².

**The three hyperkähler rotations of Eguchi–Hanson.**
1. **Rotation of ζ about Î (the U(1) phase of τ).** This is tangent Kähler/smoothing data.
2. **Rotation of ζ toward Î (the tilt).** This is Einstein-obstructed with coefficient s/4, so ζ_Î = O(|ζ|²). It is not an AKE entrance: the Einstein equation alone fixes it, independently of ω.
3. **Rotation of the bubble's parallel form I with ζ fixed.** It is free in the core, since all of ω_I, ω_J, ω_K are parallel on EH. It is pinned by exterior matching, because ω_n→ω_V smoothly and parallel self-dual forms on the cone are constant. Globally it is the rotation ω + εRe φ, whose torsion ∇Re φ ≠ 0 lives on the exterior (Ricci curvature ≠ 0 there).

**Conclusion of §2.** The core carries no strict-AKE freedom. Any strict entrance must come from the exterior Kuranishi structure.

---

## 3. Weighted normal operator and the finite-dimensional map

**Operator.** On the naive gluing g^D_{ζ,v}, take the gauged Einstein operator

  P = ½∇*∇ − R̊,  P : C^{2,α}_{β,*}(g^D) → r_D^{-2} C^{α}_{β}(g^D),  0<β<1 small,

with Ozuch's decoupling norm (constant trace-free tensors split off in the neck).

**Model operators by region.**
- **Exterior: P_{g_V} on V∖p.** For β∈(0,2) the weighted kernel is O(g_V) = KS(V). The singular homogeneous solutions r⁻², r⁻⁴ are excluded by the weight.
- **Neck: P_e on ℝ⁴/ℤ₂.** The ℤ₂-invariant homogeneous harmonic symmetric 2-tensors have even degrees. They decompose into the Ω⁺⊗Ω⁻ sectors θ_i^∓∘ω_j^±. The weight avoids every indicial root; constants are handled by the * part of the norm.
- **Core: P_eh.** The L²-kernel is O(eh) = span(o₁,o₂,o₃), all coming from variations of ζ (Ozuch, Remark 4.3).

**Approximate kernel and cokernel.** P is formally self-adjoint, so

  Õ = O(g_V) ⊕ span(o_{e₁}, o_{e₂}, o_{e₃}),  coker ≅ Õ.

There is a uniform estimate ‖h‖ ≤ C‖Ph‖ for h ⊥ Õ (Ozuch).

**Effect of the weight on the tilt mode.** Because of the weight r_D⁻², the tilt mode has ‖P o_{e₂}‖ ∼ t|s/4| in these norms. So it belongs to Õ, and its nondegeneracy appears after dividing the obstruction by t.

**Finite-dimensional map.** Ozuch (2019b) shows every Einstein metric GH-close to V is the Einstein-modulo-obstructions metric g(ζ,v) for a unique (ζ,v). The Einstein locus is

  ℰ = Ob⁻¹(0),  Ob : ℝ³ × O(g_V) → ℝ³ × O(g_V),
  Ob = (tλ_k + t²μ_k + O(t^{5/2}))_{k=1,2,3} ⊕ (ν_l(ζ,v)).

**Tilt elimination.** Ob₂/t = c(s/4)θ + O(t + |v|), so ∂_θ(Ob₂/t) = c s/4 + o(1). This needs one routine input: parameter-derivative bounds on Ozuch's remainder, ‖∂_ζ(Ob − tλ − t²μ)‖ = o(t). Granting it, the implicit function theorem gives

  ℰ ⊂ Γ = {θ = F(τ,v)},

a real (2+m)-dimensional graph over (τ∈ℂ^*, v∈O(g_V)), where m = dim_ℝ O(g_V).

**Cross-check on the orbifold couplings.** Along integrable v the curvature is R⁺_{g_v}(p) = (s/4)Î_v⊗Î_v. Hence ∂_v R⁺ = (s/4)(İ⊗Î + Î⊗İ) with İ⊥Î, and

  ⟨∂_vR⁺ ζ,ζ⟩ = (s/2)⟨İ,ζ⟩⟨Î,ζ⟩ = O(|ζ||ζ_Î|).

So the order-t² couplings ν_l between the smoothing and the orbifold Jacobi fields vanish on matched configurations. This is consistent with the Kähler family.

**Blow-up argument, made finite.** Suppose g_n = g̃_n + h_n with g̃_n Kähler–Einstein, h_n ⊥ T K, ε_n = ‖h_n‖ → 0. Rescale ĥ_n = h_n/ε_n and pass to limits region by region:
- the exterior limit lies in O(g_V) and is killed by orthogonality;
- the neck limit is a homogeneous solution, excluded by the weight;
- the core limit is a multiple of o_{e₂}, excluded by the uniform s/4 coefficient.

Hence ĥ_n → 0, contradicting ‖ĥ_n‖ = 1, unless Õ contains near-kernel directions not tangent to K. Those are exactly the v_⊥ directions. So the full contradiction argument reduces to the reduced map on Γ.

---

## 4. Proposition A (the unobstructed case)

**Proposition A.** Assume H²(V,Θ_V) = 0 and Ozuch's parameter-derivative bound. Then every Einstein metric on M GH-close to V is Kähler–Einstein. In particular no strict AKE metric lies in a GH-neighbourhood of V.

**Proof.**
1. Since H²(Θ_V) = 0 and the local Ext² of a hypersurface singularity vanishes, T²_V = 0. Hence Def(V) is smooth of complex dimension h¹(Θ_V) + 1.
2. The exact sequence H¹(Θ_V) → Ext¹(Ω_V,O_V) → H⁰(Ext¹) = ℂ_τ → H²(Θ_V) = 0 shows that the smoothing direction is realized. This gives Spotti's genericity C≠0.
3. Each fibre with τ≠0 has K ample, so carries a unique Aubin–Yau KE metric. These metrics converge to g_V.
4. The map Def(V)^{τ≠0} → Γ is continuous and injective: Aut is finite, and the KE metric determines J up to sign. It is also proper. Since dim_ℝ = 2+m = dim Γ, invariance of domain makes the KE locus K open in Γ.
5. K is closed in Γ ∩ U: limits of KE metrics in the smooth region are Kähler–Einstein.
6. Γ ∩ U ∩ {τ≠0} ≅ (punctured disc) × ball is connected, so K = Γ ⊇ ℰ.
7. On a KE metric D = 0, so T_AK = D = 0 for every AK structure with the same orientation. Hence every AK structure on such a metric is Kähler. ∎

---

## 5. The obstructed case: reduced deficit and one decisive estimate

**The reduced deficit is a volume excess.** For every Einstein g on M, with m=0 and D(V)=0,

  D(g) = (Ŝ²(g) − Ŝ²(V))/16 = (s²/16)(Vol(g) − Vol(V))  at equal s.

Define 𝒟(τ,v) := D(g(ζ(τ,v),v)) on Γ. Then:
- critical points of 𝒟 are exactly the Einstein points;
- 𝒟 ≡ 0 on the Def-locus κ⁻¹(0), since there the metrics are Kähler–Einstein.

**Lower bound at Einstein points.** M is symplectic, because the g_n are AKE. For b⁺>1, Taubes makes the canonical class a monopole class, and LeBrun's estimate gives D ≥ 0 at Einstein points, with equality iff KE. Independently, D = T_AK ≥ 0 at AKE points. A strict AKE metric is therefore an Einstein point with 𝒟 > 0, i.e. one with volume strictly above Vol(V).

**Decisive estimate (uniform one-sided Łojasiewicz at the A₁ end).** There exist C, ε, ϑ>0 such that on Γ ∩ {|τ|+|v|<ε, τ≠0}:

  𝒟 > 0  ⟹  |∇_{(τ,v)}𝒟| ≥ C 𝒟^{1−ϑ}.  (L)

**Why (L) settles the local question.** At an Einstein point the Lyapunov–Schmidt gradient vanishes (∇𝒟 equals Ob up to an invertible matrix). So (L) forces 𝒟 ≤ 0, hence D = 0, hence g is Kähler–Einstein and T_AK = 0. This gives a GH-neighbourhood of V with no strict AKE metric, and with it the local uniform gap inf T_AK > 0 over strict AKE metrics near V.

**Where (L) already holds.**
- On the slice τ = 0: Koiso analyticity on the orbifold.
- In case A: there 𝒟 ≡ 0 on Γ.

**Mechanism to prove (L): Kähler–Kuranishi comparison.** Use κ(τ,v) ∈ H²(V,Θ_V), the holomorphic Kuranishi map of V with the smoothing parameter. Here τ enters holomorphically, as in plumbing, while the gluing scale |τ| does not.

**Target identity.**

  𝒟(τ,v) = A ζ_Î-part (eliminated) + ⟨κ,G κ⟩ + R,  G uniformly positive,

with R and ∇R small relative to the corresponding terms of ⟨κ,Gκ⟩.

**Why it gives (L).** |κ|² is real-analytic, so it satisfies Łojasiewicz's gradient inequality; (L) follows if G is C¹-controlled in (τ,v). The comparison is also consistent with:
- Nagy (the quadratic Einstein term vanishes);
- LeBrun (sign);
- D = T_AK ≍ ‖H(N)‖²-type quartic behaviour.

**The term linear in τ.** Write κ(τ,0) = δ τ + O(τ²), where δ ∈ H²(Θ_V) is the local-to-global smoothing class (Burns–Wahl theory; source to retrieve: Burns–Wahl, "Local contributions to global deformations of surfaces", and work on smoothability of nodal canonical surfaces). The order-|τ|² coefficient of 𝒟(τ,0) is purely local at p:
- the first-order effect of the exterior Green-type correction vanishes by criticality of Ŝ at g_V, up to local terms at p;
- the O(g_V)-projection enters only quadratically, at order ≥ t⁴;
- the remaining local coefficient is the radial obstruction ΛV(eh) + Q(W⁻_eh, W⁺_V(p)), which is zero for matched KE data.

Hence 𝒟(τ,0) = O(|τ|³). So a term |δτ|² cannot appear in 𝒟. Two alternatives follow:
- (a) If δ ≠ 0, the comparison must be read on AK structures, not on metrics. A strict AKE metric at (τ,v) would satisfy T_AK = D = O(|τ|³) together with T_AK ≳ |κ(τ,v)|² ≳ |δτ|². This is a contradiction for small τ.
- (b) If δ = 0, the comparison concerns only the higher Kuranishi terms.

Alternative (a) needs one AK-specific coercivity, which is not yet proved:

  T_AK ≥ c₀ (|s|/16)Q,  Q = ∫|∇ω|²,  uniformly near the KE family.

By the Step-79 balance (|s|/16)Q = ∫|η|² + T_AK, this is equivalent to

  ∫|η|² ≤ (1−c₀)(|s|/16)Q,

a spectral gap for the operator α ↦ d_b*α = −2η̄ on torsions satisfying (d_bα)⁻ = 0. On the complete Bianchi-VIII model the ratio is ∫|η|² / ((|s|/16)Q) = 16/48 = 1/3, i.e. c₀ = 2/3 there.

---

## 6. AKE side lemma: rotation by holomorphic 2-forms

At a KE pair (g,ω) with s<0, consider the linearized AKE problem (closed, self-dual, |ω|² = 2).

**Kernel.** It is

  {(h_KS, θ_KS)} ⊕ {(L_Xg, L_Xω)} ⊕ {(0, Re φ) : φ ∈ H⁰(K)}.

The last summand has first-order torsion ∇Re φ ≠ 0: a parallel holomorphic 2-form would make K flat.

**Second order with h₁ = 0.**
- The Einstein equation forces h₂ ∈ KS ⊕ gauge ⊕ ℝg.
- KS tensors have the form (ψ-plane)⊗Ω⁻, so they leave ω self-dual to first order and are trace-free.
- Hence θ₂ is harmonic self-dual modulo gauge, and ⟨ω,θ₂⟩ is constant.
- The length condition 2⟨ω,θ₂⟩ + |Re φ|² − c·tr h₂ = 0 then forces |φ|² ≡ const.
- Since |K| ≠ ∅ for K ample, φ has zeros, so the only solution is φ = 0.

**Remaining cross term.** For h₁ ≠ 0 there is a bilinear term B(h₁,φ): the ω-component of the self-dual completion of −(∗′h₁)Re φ. To finish the "rotation is not an entrance" lemma, one must compute the pointwise identity |φ|²/2 + B(h₁,φ) ∈ ℝ. The symmetric part of ω∘Re φ is trace-only, so the length-level cross term vanishes; only B remains.

---

## 7. Next calculations, in order of decisiveness

1. **Quartic Einstein–Hilbert coefficient at a smooth KE surface with s<0.**
   - **Setup.** Take Nagy's second-order solution: h₁ ∈ KS, h₂⁺ = h₁², h₂⁻ = 𝐡₂ − ½L_{J∇f}J, Δ_E𝐡₂ = −2δ[h₁,h₁]^c, (Δ−2E)f = −½tr h₁². Solve the third order modulo E(g) with residual o₃(h₁).
   - **Prediction.** 𝒟(εh₁) = c ε⁴ ‖H([h₁,h₁]^c)‖² + O(ε⁵) with c > 0. Equivalently ⟨o₃(h₁),h₁⟩ ∝ −‖H[h₁,h₁]^c‖².
   - **Expected identity.** ‖H‖² = ‖[h₁,h₁]^c‖² − ½⟨Δ_E𝐡₂,𝐡₂⟩, using ∂̄* = δ on Sym^{2,−} (Corollary 4.3) and ∂̄𝐡₂ ⊥ harmonic. The fourth-order expansion of Ŝ should reduce, by Nagy's Propositions 4.14–4.20, to exactly these two terms with ratio 1 : −½.
   - **Tests.** The computation is tensorial; the integration-by-parts reduction suits the symbolic tensor engine. Products Σ_g×Σ_h with g,h ≥ 2 should give zero, since their deformations are unobstructed and [μ₁,μ₂]^c = 0. A source search is needed for a general-type surface with a nonzero cup product H¹(Θ)×H¹(Θ) → H²(Θ) to test a nonvanishing case.
2. **Uniform version at the A₁ end.** Show that the order-|τ|² coefficient of 𝒟(τ,0) equals the radial obstruction and vanishes. This is an explicit check: Biquard–Hein's V(eh), W⁺_V(p) = diag(s/6, −s/12, −s/12), and Ozuch's Q.
3. **Tilt elimination inputs.** Compute c in λ_k = c⟨R⁺φ,e_k⟩, which fixes the s/4 nondegeneracy, and prove the derivative bound on Ozuch's remainder.
4. **Spectral gap c₀ for the AK torsion operator on the degenerating KE family.** This closes case (a), δ ≠ 0, without any analyticity.

Items 1 and 2, proved uniformly in τ, give (L) and hence local exclusion. Item 4 handles δ ≠ 0 independently.
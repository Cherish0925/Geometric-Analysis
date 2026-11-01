# TTCS Independent Branch Record

```json
{
  "step_id": 65,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step63_SU2_nut_and_clean_zero_surface.md",
    "Sessions/S1003A01/workspace/notes/step64_exceptional_points_second_order_zero.md",
    "Sessions/S1003A01/workspace/notes/spirit_step64_homogeneous_zero_identity.md",
    "Sessions/S1003A01/workspace/notes/step55_darboux_ricci_compatibility.md",
    "Knowledge/objects/papers/Local-models-and-integrability-of-certain-almost-Kahler-4-manifolds--89a416df784a--79aaa9509e7d/object.md"
  ]
}
```

## Task

Analyze the compact torsion-zero surface problem using the established Step-62 cone, Step-63 degree formula, and the proposed higher-order leading normal form. The goal is to derive, if possible, an intrinsic normal-expansion equation along a smooth J-complex surface C contained in {T=0}: identify the rank-two normal coefficient corresponding to W_3^+|_C, how the exact AAD/soldered equations constrain its tangential covariant derivative including normal connection and second fundamental form, and whether they imply a similarity-principle relation or allow negative winding. Do not assume holomorphicity. Distinguish what follows from the supplied equations from a proposed route; correct the false inference that zero linear term controls winding.

## Output

# Memo: the normal expansion along a torsion-zero surface C, the equation satisfied by W₃⁺|_C, and the winding question

Labels: **[D]** derived here from the supplied equations; **[D\*]** derived, with one named step still to be checked against conventions or computer algebra; **[R]** proposed route.

Conventions follow Step 62/64: source coordinates z = (z₁, z₂), where z₁ is tangent to C and z₂ is normal to it. The torsion a is written as f ∈ ℂ² with target structure i·a = Ja. B = D_{z̄} f, A = (B − Bᵀ)/2, S = (B + Bᵀ)/2. The complex-linear derivative of f is h·I.

---

## 1. The exact first-order system behind the "principal half-twistor equation" [D]

AAD (23) gives the Ricci identities da − Ja∧b = −R(Jφ) and d(Ja) + a∧b = −R(φ).

For Einstein metrics, R(ω) = W⁺(ω⁺) + W⁻(ω⁻) + (s/12)ω. So R(φ) and R(Jφ) lie in Λ⁺, and therefore

  (da − Ja∧b)⁻ = 0, (d(Ja) + a∧b)⁻ = 0.

These are exactly the Λ⁻ ⊗ K⁻¹ components of d^∇T = [J, R]. Put ψ = a + iJa, a (1,0)-form; the map a ↦ ψ is ℂ-antilinear, so ψ ~ f̄. The system becomes

  (dψ + iψ∧b)^{1,1}_0 = 0, i.e. ∂̄^b ψ is a multiple of Ω.

**Count.** Λ^{1,1}_0 gives 3 complex = 6 real conditions on the 16 real components of ∇a. This leaves 10, which matches the Step-62 first-jet count (c, S, A).

**Ellipticity.** The symbol ξ̄⊗v ↦ (ξ̄⊗v)₀ is injective, because a rank-one matrix is never a nonzero multiple of the identity. So T solves a linear, overdetermined elliptic first-order system with smooth coefficients.

**Consequences.**
- The Spirit form f_m = z h(z̄) + g(z̄) is simply the symbol equation obeyed by the lowest Taylor term at a zero of order m. Lower-order terms Γψ have degree ≥ m.
- The (L_m) argument therefore rests on an exact equation.
- I verified the one algebraic step that is easy to slip on: for M = v⊗ℓ, tr(M̄ M) = |ℓ·v̄|².

**Bianchi adds nothing new at this order.** The form Θ := dψ + iψ∧b = −R(Jφ) + iR(φ) satisfies d^bΘ = iψ∧db, which is identically true. Its Ω-coefficient is ∝ η_c := ⟨η,φ⟩ + i⟨η,Jφ⟩, and its K⁻¹-part contains W₃⁺. Along C, the K⁻¹-component of AAD (33) (Step-55 (3.6)/(7.4)) is the same relation as the order-w equations of §3 below. It carries no independent information at that order.

## 2. The normal coefficient and its bundle [D]

Let C ⊂ {T = 0} be smooth, with T vanishing to first order at generic points.

**Zero set alone.** Since a vanishes on C, tangential derivatives of T vanish on C, so f(z₁, 0) ≡ 0. This forces c = 0 and B e₁ = 0, so h = 0 on C. In the ψ-picture, the normal derivative of ψ is ℂ-linear in w. Then dψ|_C is a pure (2,0)-form, so Θ|_C has no Ω-component, which gives **η|_C = 0 without using the cone**.

**Cone (Step 62).** Write B = [[0, b₁₂], [0, b₂₂]]. Then ‖A‖² − ‖S‖² = −|b₂₂|², so the cone forces b₂₂ = 0. Hence

  f = β(z₁) z̄₂ e₁ + O(|z₂|²).

The normal–normal coefficient b₂₂ drops out of dψ, so it is invisible to curvature and only the cone removes it.

**Bundle.** β is a ℂ-antilinear map N → TC ⊗ K⁻¹, i.e. a section of N̄* ⊗ TC ⊗ K⁻¹ ≅ N ⊗ TC ⊗ (TC⊗N) = K_J⁻²|_C, using K⁻¹|_C = TC ⊗ N. This gives deg = 2(χ(C) + C·C), as in Step 63.

**β is W₃⁺|_C up to a universal constant, and the identification is ℂ-linear.** Under U(1)_{TC} × U(1)_N, both β and W₃⁺ have weight (2,2). Any covariant (frame-equivariant) pointwise relation between them must be ℂ-linear: a conjugate-linear one would intertwine weights (2,2) and (−2,−2), so it would be zero. Hence the winding of W₃⁺|_C equals the winding of β in its natural trivializations. This fixes the orientation question that decides §3.

**Pointwise curvature identity.** On C, a = 0, η = 0 and κ = s, so γ_J|_C = R(Ω)|_C = (s/4) dA_C.

Since ∇J = 0 on C, the first canonical connection equals Levi-Civita there. The connection induced on K⁻¹|_C is the trace of the u(2)-connection in an adapted unitary frame, namely ∇^{TC} ⊗ ∇^N. The second fundamental form occupies off-diagonal blocks and drops out of the trace. Therefore

  **K_C + K_⊥ = s/4 pointwise on C**, and the curvature of K⁻²|_C is (s/2) dA.

This refines Step 63's integrated formula χ + C·C = s·Area/8π.

## 3. Tangential derivatives of β [D\*]

Expand f₁ = β z̄₂ + ½γ₁ z̄₂² + ε₁|z₂|² + …, and f₂ = ½γ₂ z̄₂² + ε₂|z₂|² + ½κ₂ z₂² + ….

The order-w components of ∂_{z_j} f_k = δ_{jk} h + (Γf)_{jk} give:
- ε₁ = κ₂ = 0, up to Γβ terms.
- h = χ z̄₂ + O(|z₂|²), with χ := ε₂.
- **∂^D_C β = χ + Lβ.** Here ∂^D_C is the ℂ-linear (holomorphic) tangential derivative for the connection of §2, and χ is the normal derivative of the transverse curvature η along C.
- ∂̄^D_C β is unconstrained by the linear system, since the antilinear part S + A is free.
- γ₁ is free; it is Step 64's κ.

**Role of the second fundamental form.** II could enter through the normal component of ∇_ν∇_{ē₁}T. It does so only via II(∂_z, ∂_{z̄}). Since ∇J|_C = 0, II is complex-bilinear, so this component vanishes. Shape-operator commutator terms land on ∇_{TC}T = 0. This is the starred step: the frame computation of the order-w (z̄₁, 2) component should confirm that it produces no condition such as β·II = 0.

**Consequence for the Step-64 mechanism (a).** The linear equations control ∂β, not ∂̄β.
- If χ were O(|β|), a similarity principle would make β anti-holomorphic-type.
- Its zeros would then have winding −k, which is the sign required by deg K⁻²|_C = s·Area/4π < 0.
- So the hoped-for similarity contradiction points the wrong way for s < 0.

The Weitzenböck formula on C agrees with this. With curvature (s/2) dA, one has ∫|∂^Dβ|² − ∫|∂̄^Dβ|² = c·s∫|β|² with c > 0. For s < 0 this favours ∂̄β, which is the free data.

## 4. Winding versus multiplicity

Step 64's inference "zero linear part ⇒ winding ≠ ±1" is not valid:
- z|z|² and z̄|z|² have zero linear part and windings +1 and −1.
- A homogeneous leading part z^a z̄^b has winding a − b, with |a − b| ≤ k.

Step 64's quadric only shows that the first jet of β vanishes at an exceptional point. With (L₂) this means β = O(|z|²) there; more generally, (L_m) gives β = O(|z|^m) at an exceptional point where T vanishes to order m. Neither statement says anything about winding.

## 5. The second-normal-order identity along C [D\*]

**The identity.** Take the |z₂|²-coefficient of the flat transcription of (G):

  |B₁₁|² + |B₂₂|² + 2Re(B̄₁₂B₂₁) + 8|h|² + 6Re Σ f̄_j ∂_{z̄_j} h = 0.

This uses ‖A‖² − ‖S‖² = −Re Σ B̄_{jk}B_{kj}, together with ε₂ = χ = ∂β. It gives, as a function on C,

  **E := |∂̄β|² + |γ₂|² + 15|χ|² + 8 Re(β̄ ∂̄χ) + (curved terms) = 0.**

γ₁ cancels between ‖A‖² and ‖S‖², and no third-order data survive.

**Validation.** At a zero of β this reads |∂̄β|² + |γ₂|² + 15|∂β|² = 0. With ∂̄β = 2Q¹₁₂, γ₂ = 2Q²₂₂ and ∂β = δ₂, this is exactly 4(|Q¹₁₂|² + |Q²₂₂|² + (15/4)|δ₂|²). That is Step 64's trace relation, which the saved fit reproduced to a residual of 3·10⁻¹².

**Positivity at a zero.** Let β vanish to finite order k at p, with leading part β_k = Σ c_j z^{k−j} z̄^j. The degree-(2k−2) part of E is built from β_k, ∂β_k, ∂̄∂β_k and the leading part of γ₂. Averaging over |z| = r kills the cross-monomials, leaving

  Σ_j |c_j|² [ j² + 15(k−j)² + 8j(k−j) ] + avg|γ₂|² = 0.

Each bracket is positive for k ≥ 1, so β_k = 0, a contradiction. (If γ₂ has lower degree, the term |γ₂|² dominates alone and must vanish.)

**Curved terms.** These are exact pointwise expressions in covariant normal jets:
- s·q contributes ∝ s|β|²;
- commutator terms give R·∇a·∇a ∝ |β|², or β × (∂β, ∂̄β, γ₂);
- terms coupling β to γ₁ would require B₁₂^{(1)} ≠ 0, which §3 excludes;
- cubic dictionary corrections are excluded by weight.

All of these have degree ≥ 2k − 1. The starred step is to confirm with computer algebra that no γ₁-coupled term survives.

**Resulting structure.** Einstein metrics and the harmonic form Ω are real-analytic, so β is analytic on C. Hence **β is either nowhere zero or identically zero on each component**, for every s.

With Step 63 this gives: **for s ≠ 0, every closed smooth surface component of {T = 0} has β ≡ 0**, i.e. it lies in {∇Ω = ∇²Ω = 0}. This holds whether or not W₃⁺ winds. It closes Step 64's open exceptional-point problem without any winding argument.

## 6. Higher order and arithmetic consequences [R]

Suppose T vanishes to exact order m along C, with leading term f = β_m z̄₂^m e₁ (this is (L_m), and it also forces TC to be J-complex automatically).

- Then β_m ∈ Γ(TC² ⊗ N^{m+1}).
- The same transcription gives the coefficient |∂̄β|² + (m+2)(m+4)|χ|² + 2(m+3) Re(β̄ ∂̄χ) + |γ|².
- Its angular average, j² + (m+2)(m+4)(k−j)² + 2(m+3) j(k−j), is again positive.

If this order-m computation is confirmed, β_m is nowhere zero. Combining 2χ(C) + (m+1) C·C = 0 with χ + C·C = s·Area/8π gives:

| Case | Consequence |
|---|---|
| m = 1 | s = 0 (Step 63) |
| s < 0 | genus g ≥ 2, C·C = 4(g−1)/(m+1), so (m+1) divides 4(g−1) |
| s > 0 | sphere with m = 3 and C·C = −1 |

## 7. Control

The Ricci-flat Gibbons–Hawking/Tod metrics of AAD Theorem 1 provide a test case. At a nondegenerate critical point of the holomorphic function h on Σ, the orbit {p} × ℝ² is a J-complex zero surface. Along it:
- β ∝ h″(p) is constant and nonzero;
- η ≡ 0, so χ = 0;
- II = 0 because dw = dv = 0 at p;
- m = 1, and the torus quotient has C·C = 0.

This is consistent with every formula above. It shows that s ≠ 0 is genuinely used in Step 63, but it does not test the coefficients of the curved terms.

## 8. Remaining computations

1. **Frame computation of the order-w (z̄₁, 2) equation** (§3). This decides whether II contributes.
2. **Symbolic expansion of the covariant |w|²-coefficient of (G).** This should confirm that E has no γ₁-coupled terms and give the exact coefficient of s|β|². It can be tested numerically with the Step-62/64 jet code at a rank-two point by fitting the 8 Re(β̄∂̄χ) coefficient.
3. **The order-m version of §5**, which is needed for the arithmetic consequences in §6.
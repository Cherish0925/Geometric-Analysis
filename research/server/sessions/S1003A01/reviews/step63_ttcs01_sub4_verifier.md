# TTCS Independent Branch Record

```json
{
  "step_id": 63,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A01/workspace/notes/spirit_step62_clean_zero_surface_consequence.md",
    "Sessions/S1003A01/workspace/notes/step63_SU2_nut_and_clean_zero_surface.md",
    "Sessions/S1003A01/workspace/notes/step62_torsion_zero_prolongation.md",
    "Knowledge/objects/papers/Local-models-and-integrability-of-certain-almost-Kahler-4-manifolds--89a416df784a--79aaa9509e7d/object.md"
  ]
}
```

## Task

Check the proposed global consequence for a closed smooth surface contained in the torsion-zero set of a nonzero-scalar Einstein almost-Kähler four-manifold. Verify every bundle/orientation/curvature step: singular DT plus the Step-62 cone implying c=0 and rank-two complex-antilinear DT; J-invariance and orientation of TC; A nonzero and eta=0, W3+ nonzero; W3+ as K_J^{-2}; gamma_J=R(Omega)-a wedge Ja and R(Omega)=(s/4)Omega under Einstein, q=0, eta=0; the resulting Chern-degree contradiction. Also assess the extension to exceptional DT=0 points and the sign/factor deg(K_J^{-2}|C)=s Area/(4 pi). Provide a direct corrected proof if needed, grounded in the supplied AAD primary source.

## Output

# Verification memo: closed surfaces in the torsion-zero set of an Einstein AK 4-manifold with s ≠ 0

## Summary

The proposition and its proof (Spirit note and Step 63 §1) are correct.

- **Step-62 inputs actually used.** Only two are needed:
  - the cone relation (2.1) together with the determinant formula, which give c = 0;
  - Theorem 62.A, which gives W₃⁺ ≠ 0.
- **η = 0 and R(Ω) = (s/4)Ω on C.** Both follow directly from AAD's Weitzenböck formula (20) once ∇a(p) is complex-antilinear. The Step-62 coefficient dictionary is not needed for these two facts. The direct computation also reproduces the dictionary's magnitude |η|² = 4|c|², which is an independent check of it.
- **Bundle and factor checks.** W₃⁺ is a section of K_J^{-2} with the correct complex structure (the sign matters only in the extension). γ_J represents 2πc₁. The J-orientation of C makes Ω|_C the positive area form. The factor deg(K_J^{-2}|_C) = s·Area/(4π) is right.
- **Exceptional-point extension.** It can be sharpened in three ways:
  - |W₃⁺|² = |∇T|²/4 holds exactly along C, so the zero set of W₃⁺|_C is exactly E = C ∩ {DT = 0};
  - adjunction gives the integrality relation s·Area(C) = 8π(χ(C) + C·C);
  - the local winding of W₃⁺ is the J-type of a specific component of ∇³Ω(p).

## 1. Step-by-step verification

**(a) Singular DT.** Along C we have T ≡ 0, so ∇_vT = 0 for v ∈ TC. At a zero, ∇T is tensorial. In AAD gauge, at p:

∇_vT = (∇_v a) ⊗ φ − J(∇_v a) ⊗ Jφ.

Here φ and Jφ are independent, and ∇J(p) = 0, so ∇_v(Ja) = J∇_v a. Hence ker DT_p = ker L, where ⟨LX, Y⟩ := (∇_X a)(Y).

A gauge change a′ = cos θ·a − sin θ·Ja rotates L by an element of U(1) at p. So ker L is gauge-independent.

Kernel ⊇ T_pC forces det_R L = 0. The determinant is unchanged under transpose, and transpose preserves J-linear/antilinear type. So the slot convention of Step 62's f is irrelevant for this step.

**(b) Consequences of the cone.**
- On (2.1), det_R L = 9|c|⁴ + |det B|². Vanishing forces c = 0 and det B = 0.
- Since L ≠ 0, B is a nonzero complex 2×2 matrix of complex rank one.
- The real determinant of z ↦ B z̄ is |det B|², because conjugation on ℂ² has real determinant +1.
- So L is complex-antilinear with real rank 2.

**(c) Kernel and orientation.**
- For antilinear L, Lv = 0 implies L(Jv) = −J(Lv) = 0. So ker L is a J-complex line of real dimension 2, hence equal to T_pC.
- C is therefore J-invariant. It is oriented by J, so orientability is not an extra hypothesis.
- With Ω(X, Y) = g(JX, Y), we get Ω(v, Jv) = |v|² > 0. So Ω|_C is the positive area form.
- Immersed closed surfaces work equally well, via pullback.

**(d) A ≠ 0.** With c = 0, (2.1) reads ‖A‖² = ‖S‖². So A = 0 would force B = 0. Moreover, det(S + A) = det S + a² = 0 gives |det S| = ‖S‖²/2. This is exactly the degenerate stratum of Corollary 62.B/C, so the setup is consistent.

**(e) η = 0 and R(Ω) = (s/4)Ω, directly from AAD.** At p ∈ Z, a(p) = 0, so the ∇φ terms drop and

∇*∇Ω(p) = −(tr L)·φ + tr(JL)·Jφ.

Write L = L₊ + L₋ (J-linear plus antilinear parts). Then tr L₋ = 0 and tr(JL₋) = 0, by cyclicity and anticommutation. Step 62 has L₊ = c·I with c = c_R + c_I J, so

∇*∇Ω(p) = −4c_R φ − 4c_I Jφ, and |∇*∇Ω(p)|² = 32|c|².

Compare with ∇*∇u = 2η at p, using u = Ω/√2 and r = s/6. This gives |η|² = 4|c|², the dictionary value, so the magnitude is independently confirmed.

On C, c = 0, so ∇*∇Ω = 0. By AAD (20), R(Ω) = ρ + ½∇*∇Ω. Einstein gives ρ = Ric(J·,·) = (s/4)Ω. Hence R(Ω) = (s/4)Ω on C.

This also gives ρ*″ = 0, which is η = 0 (W₂⁺ = 0), with no norm convention involved. The Rayleigh value κ = s (from q = 0, i.e. s* = s in AAD (20)) is consistent with this but not needed for it.

**(f) W₃⁺ ≠ 0.** Theorem 62.A gives

4 trV² = |∇²Ω|² + 12|η|² ≥ |∇T|² > 0.

This needs only Theorem 62.A, not the V ↔ A coefficients.

I checked Derdziński's formula used in Theorem 62.A on the Kähler–Einstein spectrum (s/6, −s/12, −s/12): the right-hand side vanishes on both eigenspaces, as it must for parallel W⁺. The identification |W₃⁺|² = trV² matches AAD (8): the [[Λ^{0,2}]]-block is −κ/12 + W₃⁺ with κ = 6r, and W₃⁺ is its traceless part.

**(g) W₃⁺ ∈ Γ(K_J^{-2}).**
- AAD: [[Λ^{0,2}]] ≅ K_J^{-1} =: ℒ via (Jψ)(X, Y) = −ψ(JX, Y). W₃⁺ is the symmetric J-anticommuting part of W⁺ on this bundle.
- Every real endomorphism of a 2-plane that anticommutes with J has the form [[x, y], [y, −x]]. So "symmetric" is automatic, and these are exactly the antilinear endomorphisms of ℒ.
- Take a unit frame e with E(e) = w e. Under e′ = e^{iθ}e, antilinearity gives w′ = e^{−2iθ}w. This is the transformation law of a section of ℒ². The complex structure E ↦ J∘E acts as w ↦ iw.
- Hence the bundle is K_J^{-2}, with c₁ = 2c₁(M, J), and not its conjugate. This agrees with AAD (9), where (λ + iμ) rotates by 2θ.

**(h) Chern form.**
- AAD (25): γ_J = −db = R(Ω) − a∧Ja represents 2πc₁(M, J). As a sign check, in the Kähler–Einstein case γ_J = ρ = (s/4)Ω, which is positive on CP².
- γ_J is gauge-independent and globally smooth.
- On C, a = 0 pointwise, because |∇Ω|² = 4|a|². So γ_J|_C = (s/4)Ω|_C.
- Integrating: 2π⟨c₁(J), [C]⟩ = (s/4)·Area(C), with [C] J-oriented.

**(i) Contradiction.** A nowhere-zero W₃⁺|_C trivializes K_J^{-2}|_C, so 2⟨c₁, [C]⟩ = 0. This contradicts s·Area/(4π) ≠ 0. The argument runs componentwise, so C need not be connected.

For s > 0 the proposition concerns noncompact M only, since Sekigawa already covers compact M with s ≥ 0.

## 2. Self-contained proof

Let C ⊂ Z be closed with ∇T ≠ 0 on C.

1. At p ∈ C, TC ⊂ ker L, so det_R L = 0. On the cone (2.1), this gives c = 0 and det B = 0.
2. Hence L is antilinear of real rank 2, ker L = T_pC is J-complex, and Ω|_C = dA_J.
3. Antilinearity gives tr L = tr(JL) = 0. Then ∇*∇Ω = 0 on C, so AAD (20) and Einstein give R(Ω) = (s/4)Ω on C.
4. Theorem 62.A gives 4|W₃⁺|² ≥ |∇T|² > 0 on C.
5. W₃⁺|_C is a nowhere-zero section of K_J^{-2}|_C, so 2⟨c₁(J), [C]⟩ = 0.
6. But ∫_C γ_J = (s/4)·Area(C) ≠ 0 with γ_J ∈ 2πc₁. Contradiction. ∎

## 3. Exceptional points (DT = 0 on C)

Assume C ⊂ Z is a closed smooth surface and C₀ = C \ E is dense.

**J-invariance and η = 0 on all of C.**
- J-invariance of TC is a closed condition, so it extends from C₀ to C.
- At points of E, ∇T = 0, so ∇*∇Ω = 0 trivially. Thus η = 0 and R(Ω) = (s/4)Ω hold along all of C.

**Exact vanishing locus.** With η ≡ 0 on C, Theorem 62.A becomes |W₃⁺|² = |∇T|²/4 along C. So the zero set of W₃⁺|_C is exactly E. This confirms the note's statement that W₃⁺ vanishes wherever DT = 0, and makes it sharp.

**Degree and factor.** The degree formula deg K_J^{-2}|_C = 2c₁(J)[C] = s·Area/(4π) is correct, including sign and factor. Here [C] is J-oriented and the fiber carries its complex orientation, so the two integrals use the same orientation. For s < 0 the degree is below zero.

**Adjunction and integrality.** TC is J-invariant and its orthogonal complement N_C is J-invariant, so TM|_C = TC ⊕ N_C as complex bundles. Hence c₁(J)[C] = χ(C) + C·C, and

  s·Area(C) = 8π(χ(C) + C·C), Σ_{p∈E} ind_p(W₃⁺|_C) = 2(χ(C) + C·C).

For s < 0, this requires χ(C) + C·C < 0. Either at least one isolated zero has index below zero, or E is non-isolated and carries a localized class of that sign.

**What the local winding is.** On Z, with a = 0, AAD (23) reads da = −R(Jφ) and d(Ja) = −R(φ). Einstein gives R|_{Λ⁺} = W⁺ + s/12, and κ = s on Z cancels the scalar term on [[Λ^{0,2}]]. Therefore

  W₃⁺(φ) = −(d(Ja))″, W₃⁺(Jφ) = −(da)″ along Z.

This is gauge-covariant at a = 0. So W₃⁺|_C is the (0,2)-part of the exterior derivative of the torsion 1-form.

At a nondegenerate zero p ∈ E, the index is the sign of det of the map

  T_pC → (K_J^{-2})_p, v ↦ ∇_vW₃⁺,

which is the (0,2)-part of d(∇_v a) — a tangential component of ∇³Ω(p). The index is +1 if this map is C-linear and −1 if it is C-antilinear. The higher-order computation must therefore determine the J-type of the tangential (0,2)-component of ∇²a at a second-order zero. The candidate second-order identity in Step 62 §5.1, |∇³Ω|² = 4ΣtrV_i² − 24Σ|η_i|², which is still unverified, is the natural tool. It would need to be refined to separate the C-linear and antilinear parts of v ↦ V_v restricted to T_pC.

**AAD's Bianchi identities do not close this.** On Z we have ρ₀ = 0, Ric″ = 0, A = 0 and ∇Ω = 0. Also d(κ − s) = (3/2)dq = 0 on Z, using κ − s = 3q/2 from AAD (20). AAD Corollary 1 (37)–(38) then reduces to

  2(δW₃⁺)″_Z = −(∇_{JZ}ρ*″)″,

plus a corresponding Ω-component involving δρ*″. Along C, ρ*″ vanishes, but its normal derivatives need not. So δW₃⁺ is driven by the normal derivative of η. This is a full divergence, not a tangential ∂̄-operator on C. No holomorphicity of W₃⁺|_C, and hence no sign of the winding, follows from AAD's Bianchi identities without controlling ∂_ν η along C. The note is right not to assume holomorphicity.

## 4. Remaining dependencies

- **Determinant formula on the cone.** The cone (2.1) and det = 9|c|⁴ + |det B|² are the only inputs that force c = 0. The general off-cone formula |c|⁴ − |c|²(‖S‖² − ‖A‖²) + |det B|² can vanish with c ≠ 0.
- **Theorem 62.A** supplies W₃⁺ ≠ 0. Its λ-independence matches the observation that s enters only through γ_J|_C.
- **Consistency controls.** Gibbons–Hawking (s = 0, degree 0) and noncompact zero surfaces are consistent with the result, as both notes state.
# TTCS Independent Branch Record

```json
{
  "step_id": 65,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A01/workspace/notes/spirit_step64_homogeneous_zero_identity.md",
    "Sessions/S1003A01/workspace/notes/step62_torsion_zero_prolongation.md",
    "Sessions/S1003A01/workspace/notes/step64_exceptional_points_second_order_zero.md",
    "Sessions/S1003A01/workspace/scripts/spirit_step64_homogeneous_quadric_check.py",
    "Sessions/S1003A01/workspace/data/spirit_step64/homogeneous_quadric_comparison.json"
  ]
}
```

## Task

Independently verify the mathematical derivation in Spirit Step 64's homogeneous zero identity for Einstein almost-Kähler four-manifolds. Check the exact scalar Delta-q formula (G), all constants/sign conventions relative to the established Step-62 normalization, the passage to the leading polynomial identity H_m for a finite-order torsion zero f_m=z h(bar z)+g(bar z), and the claimed all-orders classification f_m=kappa (bar z_2)^m e_1 for m>=2. Pay particular attention to the bidegree separation, the argument forcing h=0, the Hermitian form tr(conjugate(M)M), maximal totally isotropic dimension, integration/mixed-partial argument, and whether any exceptional polynomial cases were missed. State exactly what is proved and what still depends on unproved formal/gauge assumptions.

## Output

# Verification memo: the Step-64 homogeneous zero identity (G) → (H_m) → (L_m)

## Summary

- **Formula (G)** is correct. All constants agree with the Step-62 normalization, and (G) reproduces Theorem 62.A at a zero.
- **Passage to (H_m)** is correct. The one ingredient not yet written out is the leading-order coframe dictionary for general m. It follows from the exact AAD Ricci identities by degree counting, as sketched in §2 below.
- **Classification (L_m)** is correct for every m ≥ 2, and no polynomial case is missed. The bidegree separation, the argument forcing h = 0 and the isotropy argument do not depend on the sign of the cross coefficient, which is the only constant in (H_m) carrying a gauge-dependent sign.

I re-derived each step by hand. The details follow.

## 1. Formula (G)

**Conventions used.** Δ = tr∇². ΔΩ = −2W⁺Ω + (s/3)Ω. ΔW⁺ = (s/2)W⁺ − 6W⁺² + 2tr(W⁺²)I.

**Normalization check of the Derdziński formula.** The Kähler W⁺ = diag(s/6, −s/12, −s/12) is parallel, with tr W⁺² = s²/24. The formula must therefore annihilate it:
- u-entry: s²/12 − s²/6 + s²/12 = 0.
- u^⊥-entry: −s²/24 − s²/24 + s²/12 = 0.

So the formula is consistent with the Step-62 normalization.

**Relation between r and q.** From |u| = 1, |∇u|² = −⟨Δu, u⟩ = 2r − s/3. Hence q = 2|∇u|² = 4r − 2s/3, which is r = s/6 + q/4.

**AAD isotropy.** Write ∇u = a⊗φ̂ − Ja⊗ψ̂ with φ̂ = φ/√2 and ψ̂ = ψ/√2. Since ⟨a, Ja⟩ = 0 and |Ja| = |a|,

Σᵢ ∇ᵢu⊗∇ᵢu = |a|² I_{u⊥}, and q = 4|a|².

This gives the stated (q/4)I.

**Product rule.**

Δ⟨W⁺u,u⟩ = ⟨ΔW⁺u,u⟩ + 2⟨W⁺Δu,u⟩ + 4Σ⟨∇ᵢW⁺∇ᵢu,u⟩ + 2Σ⟨W⁺∇ᵢu,∇ᵢu⟩.

The two cross terms are equal because W⁺ is symmetric. The individual pieces are:
- (W²)_uu = r² + |η|².
- tr W² = (3/2)r² + 2|η|² + trV², using trV = 0.
- ⟨ΔWu,u⟩ = (s/2)r − 3r² − 2|η|² + 2trV².
- 2⟨WΔu,u⟩ = −4r² − 4|η|² + (2s/3)r.
- 2Σ⟨W∇ᵢu,∇ᵢu⟩ = (q/2)·tr(W|_{u⊥}) = −(q/2)r.

**Sum.** The algebraic part is (7s/6)r − 7r² − (q/2)r − 6|η|² + 2trV², as stated. After substituting r, the s² terms cancel. The sq coefficient is 7/24 − 14/24 − 2/24 = −3/8, and the q² coefficient is −7/16 − 2/16 = −9/16. Multiplying by 4 gives (G) exactly.

**Control.** At a zero, Δq = 2|∇²Ω|² and the derivative source vanishes, so (G) returns |∇²Ω|² = 4trV² − 12|η|², which is Theorem 62.A.

## 2. Passage to (H_m)

**Finite order of zeros.** Ric = λg and harmonic Ω make (g, Ω) real-analytic. A zero of infinite order on a connected manifold therefore forces Kähler. So every torsion zero of a strictly almost-Kähler Einstein manifold has finite order m, which makes the "finite-order" hypothesis automatic.

**Degree bookkeeping.** Take normal coordinates, so g = δ + O(|x|²) and J − J₀ = O(|x|²). Then:
- q = 4|f_m|² + O(|x|^{2m+1}).
- Δ_g q = Δ_flat(4|f_m|²) + O(|x|^{2m−1}).

The degree-(2m−2) coefficient of (G) is therefore well defined. Its sq and q² terms have degree ≥ 2m.

**Leading dictionary for general m (to be written out).** The exact AAD identities read

da = −R(ψ) + (θ∧a-type terms) + O(a²),

and similarly for d(Ja). Here θ is the u^⊥-frame connection. Each correction is of degree ≥ m, while da has degree m−1. In R(ψ), the ψ-component is V₂₂ − q/8, and q/8 has degree 2m. Einstein removes the Λ⁻ part. Consequently the Step-62 linear dictionary applies verbatim to Df_m(x) at degree m−1:
- the C-linear part of Df_m(x) is scalar, h(x)I;
- η = −2h;
- |η|² = 4|h|²;
- trV² = 4‖A‖².

**The half-twistor form.** Write ∂_{z_j}f_k = hδ_{jk}. Equality of mixed partials, ∂_{z_i}h δ_{jk} = ∂_{z_j}h δ_{ik}, gives ∂_z h = 0. Hence f = z·h(z̄) + g(z̄). Δ_flat f = 4D_w h is correct.

**The cross term.** The term equals D_aη₁ − D_{Ja}η₂ plus higher-order terms. Put P = Σ f̄_j ∂_{w_j}h. With η = −2h:
- D_f η = −2P;
- D_{if} η = 2iP;
- so the cross term is −4 Re P, as stated.

**Assembly.** The left side is Δq = 8Re⟨Δf, f⟩ + 8‖Df‖², with ‖Df‖² = 4|h|² + 2‖B‖². The right side is 32‖A‖² − 96|h|² − 64 Re P. Dividing by 16 gives (H_m). For m = 1, Dh = 0 and (H_1) is exactly the cone (2.1).

**Script check.** `spirit_step64_homogeneous_quadric_check.py` implements (H_2) correctly:
- B_{tb} = z_t δ_b + 2Q^t_{ab} z̄_a;
- −tr(B̄B) uses entrywise conjugation, and −tr(B̄B) = ‖A‖² − ‖S‖²;
- vdot(f, δ) equals P.

## 3. From (H_m) to (I_m), (J_m), (K_m)

**Bidegrees** in (w, w̄), with z = w̄:

| object | bidegree |
|---|---|
| h | (m−1, 0) |
| g | (m, 0) |
| z⊗Dh | (m−2, 1) |
| Dg | (m−1, 0) |

**The (m−1, m−1) part.**
- tr(conj(z⊗Dh)(z⊗Dh)) = |Σ wₖ∂ₖh|² = (m−1)²|h|².
- tr(conj(Dg)Dg) contributes its full value.
- In Re P, the term conj(zh)·Dh gives (m−1)|h|² by Euler.
- The total |h|² coefficient is (m−1)² + 6(m−1) + 8 = (m+1)(m+3).

**The (m−2, m) part.** The cross term in tr(B̄B) is 2m·Re Σ ḡ∂h. Adding the explicit 6 Re Σ ḡ∂h gives the coefficient 2(m+3).

So (I_m) is exactly −(H_m), reorganized. For m ≥ 2 the bidegrees (m−2, m), (m, m−2) and (m−1, m−1) are distinct, and the coefficient identity in independent monomials gives (J_m) and (K_m).

**Robustness to the dictionary sign.** Suppose the cross term were +4 Re P, or carried an extra Im P. Gauge invariance under the common phase of a and η forces the form f̄∂h, never f∂h. Then:
- the (m−1, m−1) coefficient would become (m−2)² + 7 > 0;
- the cross coefficient would become 2(m−1) ≠ 0;
- the Im P term drops out of the (m−1, m−1) part.

In every case the argument below goes through unchanged.

## 4. The classification argument

**Case 1: the components of g are linearly independent.** This is equivalent to the values of g spanning C². Then Σᵢ conj(gᵢ)(ζ)∂ᵢh(w) = 0 for all ζ and w forces Dh ≡ 0, hence h = 0 because its degree m−1 is at least 1.

**Case 2: g takes values in a line.** Use a simultaneous U(2) change on source and target, together with the target phase. (H_m) is invariant under these, because B ↦ UBUᵀ preserves tr(B̄B). Take g = (G, 0).
- (J_m) gives ∂₁h = 0.
- With Dg = [[∂₁G, ∂₂G], [0, 0]], tr(conj(Dg)Dg) = |∂₁G|² ≥ 0.
- (K_m) then gives h = 0.

**Case 3: g = 0.** Then (K_m) gives h = 0 and f_m = 0, so the zero is not of order m.

**The Hermitian form.** H(M, M) = |M₁₁|² + |M₂₂|² + 2Re(M̄₁₂M₂₁). The last term is a hyperbolic pair, so the signature is (3, 1). A totally isotropic subspace therefore has dimension at most min(3, 1) = 1. (K_m) with h = 0 makes the span of the coefficient matrices M_α of Dg totally isotropic. Hence Dg = M·p(w).

**Mixed partials.** M_{kj}∂ᵢp = M_{ki}∂ⱼp says every row of M is parallel to Dp(w). Dp ≢ 0 because deg p ≥ 1. This excludes rank 2, so M = v⊗ℓ and Dp ∥ ℓ, which gives p = c(ℓ·w)^{m−1}.

**Integration and isotropy.** Integrating gives g = κv(ℓ·w)^m. The isotropy condition is H(v⊗ℓ, v⊗ℓ) = |ℓ·v̄|² = 0, so v is Hermitian-orthogonal to the vector dual to ℓ. One unitary maps this orthonormal pair to (e₁, e₂), and the target phase makes κ real.

**Result.** f_m = κ z̄₂^m e₁, which satisfies (H_m) identically.

**No missed cases.** The cases g = 0, independent components, and a line exhaust the possibilities. M = 0 gives g constant, hence g = 0. Rank 2 is excluded.

**Consequences.**
- The admissible leading jets at an order-m zero (m ≥ 2) form the U(2)-orbit of κ z̄₂^m e₁. This is a real 4-dimensional cone (κ ∈ C, ℓ ∈ CP¹), compared with the 16-dimensional linear space at m = 2 in Step 64 §1.
- A testable prediction follows: least-squares minimizers of the ten saved quadrics should all be of this form.
- Corollary 64.B's normal form now follows for every exceptional point, without the surface hypotheses.
- At m = 2, (K₂) has |h|² coefficient 15, consistent with the 15/4 trace relation.

## 5. What is proved and what is not

**Proved:**
- Formula (G) exactly.
- (H_m) as the degree-(2m−2) Taylor coefficient of (G). This needs only the general-m leading dictionary, which is a short write-up of the degree argument in §2 and involves no further assumption.
- The algebraic classification (L_m).

**Not addressed:**
- Completeness of (H_m) as the full obstruction.
- Whether κ ≠ 0 extends to a formal or analytic germ, for any λ. A natural Ricci-flat test object is the Gibbons–Hawking family with w + iv = 1 + ε(x+iy)^{m+1}. I have not verified its torsion order.
- The actual zero set. Higher Taylor terms can change it.
- The index of degenerate zeros. The leading term is non-isolated, vanishing on the J-complex line {z₂ = 0}, so it carries no index information.

**Remarks in note §5 that hold:**
- V_leading ∝ w₂^{m−1}, so W₃⁺|_C is invisible at leading order.
- The b = z|z|² and b = z̄|z|² examples correctly refute the Step-64 statement that a vanishing linear part forbids winding ±1.
- A ∂̄-bound with coefficient blowing up like 1/|b| gives no constraint on winding.
# TTCS Independent Branch Record

```json
{
  "step_id": 84,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step84_corrections_and_matched_control.md",
    "Sessions/S0910A01/workspace/data/step84_chirality_angular_difference.json",
    "Sessions/S0910A01/workspace/data/step84_chirality_obstruction_projection.json",
    "Sessions/S0910A01/workspace/scripts/step84_chirality_obstruction_projection.py",
    "Sessions/S0910A01/workspace/notes/step79_angular_rho_and_tilt_repair.md",
    "Sessions/S0910A01/workspace/notes/step81_L_exchange_and_radial_ledger.md"
  ]
}
```

## Task

Verify the chirality H^4 angular difference finding for the (S²×S²)/Z₂ product-orbifold Einstein desingularization.

The computation claims:
1. For Ozuch's angular map rho_x(zeta)_j = x^T(zeta^+ ∘ omega_j^-)x/|x|², using insertion direction zeta = omega_2:
   - H⁴(zeta⁺) = -Σ_j rho_j · (omega_2⁺ · omega_j⁻) / (2r⁴)
   - H⁴(zeta⁻) = -Σ_j rho_j · (omega_j⁺ · omega_2⁻) / (2r⁴)

2. The cross-compositions C[j,k] = omega_j⁺ · omega_k⁻ satisfy C[j,k] ≠ C[k,j] for j≠k, making H⁴_+ ≠ H⁴_- as symmetric 2-tensors.

3. The Gram matrices for the radial obstruction O_1 coupling are:
   - Same chirality: tr(C[1,j]·C[1,k]) = 4·delta_{jk}
   - Cross chirality: tr(C[j,1]·C[1,k]) = 4·delta_{j,1}·delta_{k,1}
   So same-chirality couples to all rho components equally, while cross-chirality couples only to rho_2.

4. The pointwise chirality difference in the obstruction overlap is 4(rho_1² + rho_3²) = 4(1 - rho_2²), with S³ mean exactly 8/3.

5. This means c_opp ≠ c_same at the H⁴ angular level: the inter-node Green response is genuinely chirality-dependent.

Please verify:
(a) The Ozuch source formulas for H⁴ in both chiralities (Prop 1.16 vs Section 1.2.3)
(b) Whether C[j,k] = C[k,j] or not (the key algebraic question)
(c) The Gram matrix computation and its interpretation
(d) Whether any cancellation in the Green-projected integral could restore chirality independence
(e) The mathematical significance: does nonzero 8/3 mean the mixed-chirality nearby-orbifold Einstein construction is genuinely obstructed?

## Output

# Verification Memo: chirality H⁴ angular difference on (S²×S²)/Z₂

I reconstructed the 2‑form algebra from scratch and checked the numerical outputs against closed‑form calculation. The algebraic and numerical content of items (1)–(4) is correct. Item (5) is correct as a statement about the *same‑node* H⁴–obstruction pairing, but the phrase "inter‑node Green response is genuinely chirality‑dependent" reaches beyond what the same‑node computation shows. Details below, including one convention discrepancy between the Step 81 and Step 84 notes that I checked and found does not affect the result.

## (b) The core algebra C[j,k] ≠ C[k,j] — confirmed

Using the standard bases
ω₁⁺=e₁₂+e₃₄, ω₂⁺=e₁₃−e₂₄, ω₃⁺=e₁₄+e₂₃ and ω₁⁻=e₁₂−e₃₄, ω₂⁻=e₁₃+e₂₄, ω₃⁻=e₁₄−e₂₃, I formed the matrix products directly. Because self‑dual and anti‑self‑dual 2‑forms generate the two commuting su(2) factors of so(4), each product C[j,k]=ω_j⁺ω_k⁻ commutes (ω⁺ω⁻=ω⁻ω⁺) and is therefore a *symmetric* matrix — consistent with H⁴ being a symmetric 2‑tensor.

Explicit computation gives
- C[0,1]=ω₁⁺ω₂⁻ has entries +1 at (0,3),(3,0) and −1 at (1,2),(2,1);
- C[1,0]=ω₂⁺ω₁⁻ has entries −1 at (0,3),(3,0) and −1 at (1,2),(2,1).

Hence C[0,1]−C[1,0] has entries +2 at (0,3),(3,0), zero elsewhere — exactly the `A01_matrix` in the JSON. So C[j,k]≠C[k,j] for j≠k is correct, and this is what makes H⁴₊≠H⁴₋ as symmetric tensors. The tensor difference is confined to the two directions transverse to the insertion index: since A[1,1]=C[1,1]−C[1,1]=0, the difference Δ=−ρ₁A₀₁−ρ₃A₂₁ carries only ρ₁,ρ₃ (not the insertion component ρ₂). ‖A₀₁‖²=‖A₂₁‖²=8, A₀₁·A₂₁=0, so ⟨‖Δ‖²⟩_{S³}=(1/3)(8+8)=16/3≈5.333, matching `Delta_squared_norm_mean`≈5.32. The max tensor difference √8≈2.828 also matches.

## (c) Gram matrices — confirmed analytically

I computed C[1,1]=diag(−1,1,−1,1) and the six needed products, then took traces (Frobenius inner products, since all C are symmetric).

- Same chirality tr(C[1,j]C[1,k]): the three matrices C[1,0],C[1,1],C[1,2] have disjoint nonzero support, each with squared‑Frobenius norm 4, giving **4·I**.
- Cross chirality tr(C[j,1]C[1,k]): I checked all nine entries. Off‑diagonal and (0,0),(2,2) entries vanish by disjoint support; only (1,1)=tr(C[1,1]²)=4 survives, giving **diag(0,4,0)**.

Both match the JSON exactly. The interpretation is sound: the receiver radial obstruction O₁∝ω₂⁺∘ρ⁻=Σρ_k C[1,k] (consistent with Remark 1.19, O₁⁴=2H⁴₊), so the same‑chirality overlap is ‖O₁‖‑type isotropic, Σρ_jρ_k·4δ_{jk}=4|ρ|², while the opposite‑chirality overlap collapses onto the single insertion index, 4ρ₂². Geometrically: an opposite‑chirality source aligns with the receiver obstruction only through the insertion direction itself.

## (4) The value 8/3 — confirmed analytically

|ρ|=1 pointwise (Remark 1.15: ρ_x is quaternionic conjugation, an isometry; I verified |ρ|²=1 at the test point x=(0.4,0.8,−0.4,0.2), ρ=(0.48,0.36,0.80)). Hence the overlap difference is 4|ρ|²−4ρ₂²=4(1−ρ₂²)=4(ρ₁²+ρ₃²)≥0 pointwise.

For the mean I did not rely on the Monte‑Carlo estimate. Write ρ₂=(x₂²+x₄²)−(x₁²+x₃²)=2u−1. On S³ the squared coordinates are Dirichlet(½,½,½,½); the sum of any two components u is Beta(1,1)=Uniform(0,1). Then ⟨(2u−1)²⟩=4·(1/3)−4·(1/2)+1=1/3, so ⟨ρ₂²⟩=1/3 and ⟨4(1−ρ₂²)⟩=8/3≈2.667. This matches `ell0_chirality_difference`=2.668 and the ≈1/3 diagonal of `rho_correlation_matrix_S3_mean`. Confirmed.

## A convention discrepancy I checked (Step 81 vs Step 84), and why the result survives

The Step 81 note defines *two distinct* angular maps ρ⁻_j(x)=xᵀ(ω₂⁺∘ω_j⁻)x/|x|²=xᵀC[1,j]x and ρ⁺_j(x)=xᵀ(ω₂⁻∘ω_j⁺)x/|x|²=xᵀC[j,1]x, which differ for j≠1. The Step 84 script instead uses a *single* ρ vector for both H⁴₊ and H⁴₋. Physically the −chirality source in a fixed ambient orientation should carry its own map ρ⁺, so the two notes are not using the same object. I checked whether this changes the overlap difference:

The cross Gram is supported only at (j,k)=(1,1), i.e. the insertion index. There C[1,1]=ω₂⁺ω₂⁻=ω₂⁻ω₂⁺, so ρ⁺₁=ρ⁻₁=ρ₂ identically. Therefore the opposite‑chirality overlap 4ρ⁺₁ρ⁻₁=4ρ₂² is independent of the ρ⁺/ρ⁻ distinction, and the same‑chirality overlap 4|ρ⁻|²=4 involves ρ⁻ only. The 4(1−ρ₂²) result is robust to this discrepancy. It would be worth aligning the two notes' conventions in writing, since the L‑transport statements in Step 81 depend on the ρ⁺/ρ⁻ definition in a way that does not obviously enjoy the same protection.

## (a) Source formulas — what I can and cannot certify

I cannot see the Ozuch text (Prop 1.16, Section 1.2.3) in the supplied material, so the assignment H⁴(ζ⁺)=−ρ(ζ)⁻∘ζ⁺/2r⁴ and H⁴(ζ⁻)=−ζ⁻∘ρ(ζ)⁺/2r⁴ is taken from the note's reproduction. Two things are internally consistent and support the transcription: (i) with ω⁺,ω⁻ commuting, both orderings reduce to the C‑matrix forms used in the script; (ii) O₁⁴=2H⁴₊ (Remark 1.19) reproduces the receiver obstruction Σρ⁻_k C[1,k], and I verified ‖H⁴₊‖=‖H⁴₋‖ pointwise (both =4 before the 1/2r⁴ factor: Σρ_jρ_k tr(C[1,j]C[1,k])=4|ρ|² and the transpose family gives 4|ρ|² too), matching `H4_norms_are_equal:true`. The single point that a reader must confirm against the primary text is that H⁴₋ genuinely reverses the SD/ASD roles (ζ⁻ paired with ω_j⁺) rather than merely re‑labelling; the norm‑equal / tensor‑unequal signature is the fingerprint of that reversal and is self‑consistent, but its truth rests on the Ozuch source.

## (d) Could Green projection restore chirality independence?

Two observations sharpen this.

First, H⁴ has no monopole: ⟨H⁴⟩_{S³}=−Σ⟨ρ_j⟩C[1,j]/2=0 because each ρ_j is a degree‑2 (ℓ=2) harmonic with zero mean. Consequently the neck coupling propagates through ℓ≥2 channels, and the number 8/3 is *not* a spurious ℓ=0 monopole artifact — it is the ℓ=0 part of the *product* of two ℓ=2 angular profiles, i.e. their L²(S³) inner product.

Second, and this is the essential point separating this computation from the reduced‑equation coefficient: the quantity computed here is a *same‑node* pairing ⟨H⁴_source(x), O₁_receiver(x)⟩ integrated over one S³ cross‑section. The actual inter‑node coefficient is c∼⟨G_product(H⁴ at node j), O₁ at node i⟩, where G is the linearized Einstein/Lichnerowicz resolvent (with DeTurck gauge) on the product orbifold. In a harmonic‑diagonal single‑neck model the coefficient is Σ_ℓ K_ℓ⟨P_ℓ(source),P_ℓ(receiver)⟩, and the difference between same and opposite chirality is Σ_ℓ K_ℓ[|P_ℓ(recv)|²−⟨P_ℓ(src),P_ℓ(recv)⟩]. The value 8/3 is exactly this sum with all K_ℓ set to 1. With genuine radial weights K_ℓ the difference is generically nonzero — a cancellation would require a conspiracy across the ℓ=2,4 channels — but this is not proven by the present data, because (i) the ℓ‑decomposition of 4(1−ρ₂²)=8/3−4(ρ₂²−1/3) into its ℓ=2,4 parts is not computed here, and (ii) the true product‑orbifold resolvent is not a single‑neck radial kernel and its K_ℓ are not determined. Since the pointwise difference is nonnegative and not identically zero, no *positive* angular measure can cancel it; but the resolvent is not a positive angular measure, so a rigorous statement of non‑cancellation needs the harmonic weights.

## (e) Mathematical significance

The verified content establishes: the leading angular pairing of an EH source against the receiver's radial obstruction is strictly larger for aligned chirality (value 4) than for opposite chirality (value 4ρ₂²≤4), with mean difference 8/3. This is genuine structural evidence that the same‑ and opposite‑chirality inter‑node responses differ, and it correctly refutes any assumption that mixed and same‑chirality gluings share the same t³ coefficient.

It does not yet mean the mixed‑chirality nearby‑orbifold construction is proven obstructed, for reasons the notes themselves partly record:

1. c is a Green‑propagated coefficient; the same‑node 8/3 is a proxy (see (d)).
2. Step 81 §6 flags that Ozuch's necessary estimate t_iλ_i+t_i²μ_i=O(t_max^{5/2}) is not sharp enough to expose a clean t³ layer, and Remark 2.11 warns of possible log terms (t_i t_j² log t_j). So even the existence of a pure constant t³ matrix B is not established from the source; the actual power/log structure must be pinned down.
3. The control relation F_same(t)=0, imported from KE existence on Bl₅P² (Tian/OSS), assumes the KE degeneration is realized in the *same* Ozuch coordinates, insertion directions, scale ratios, and normalization as the mixed path. Step 84 §1.2 itself corrects that this identification is not yet done; without it, F_mixed=2(c_opp−c_same)t³ is not licensed.
4. Even a fully established nonzero t³ coefficient would obstruct only this specific A+J(+L)-equivariant, equal‑scale, diagonal mixed‑chirality gluing ansatz on #₃(S²×S²). It carries no implication for other Einstein metrics on that manifold, and none for the general Yau‑26 existence question.

## What would close the argument

- The ℓ=2,4 decomposition of 4(1−ρ₂²) on S³ and the corresponding radial weights K_ℓ of the linearized product‑orbifold resolvent between the two node sites, to convert the same‑node 8/3 into the actual inter‑node c_opp−c_same.
- The primary‑text confirmation of H⁴(ζ⁻)'s SD/ASD‑reversed form, and a single consistent ρ⁺/ρ⁻ convention shared by the Step 81 transport statements and the Step 84 overlap.
- The sharp radial expansion (power and log content past O(t^{5/2})) so that a t³ (or t³ log t) coefficient is an actual term rather than an assumed layer.
- The coordinate/normalization identification of the Bl₅P² KE path with the mixed path, so the F_same=0 control is genuinely applicable.

Net: items (1)–(4) are correct and I reproduce them by hand; the ρ‑convention subtlety is real but harmless to this result; item (5) is correct as a same‑node H⁴ statement and points strongly toward chirality‑dependent inter‑node coupling, while the reduced‑equation coefficient and the resulting statement about the mixed construction require the Green propagation, the sharp radial expansion, and the KE‑path identification that are not yet in hand.
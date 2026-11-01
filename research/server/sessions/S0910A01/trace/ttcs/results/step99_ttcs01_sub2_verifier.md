# TTCS Independent Branch Record

```json
{
  "step_id": 99,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step99_geometric_mode_bridge_check.md",
    "Sessions/S0910A01/workspace/notes/step98_trace_obstruction_theorem.md",
    "Sessions/S0910A01/workspace/scripts/step99_tensor_partial_jets.py",
    "Sessions/S0910A01/workspace/scripts/step99_partial_jet_exact_contract.py",
    "Sessions/S0910A01/workspace/scripts/step99_chirality_cancellation_structure.py",
    "Sessions/S0910A01/workspace/scripts/step99_exact_degree_pair_cancellation.py",
    "Sessions/S0910A01/workspace/data/step99_partial_jet_exact_contract.json",
    "Sessions/S0910A01/workspace/data/step99_exact_degree_pair_cancellation.json",
    "Knowledge/objects/papers/Higher-order-obstructions-to-the-desingularization-of-Einstein-metrics--94f76f3b5378--19c12fb27fae/object.md"
  ]
}
```

## Task

Verify the Step 99 product-orbifold bridge check. The scientific question is whether the Step 98 raw chirality calculation should be treated as a restricted implemented spectral-model mechanism and whether Step 99 legitimately strengthens it by (i) showing omitted same-factor partial tensor jets for actual electric/full-Lie magnetic m=2 tensor families contract exactly to zero with the Step96 source/receiver functionals, and (ii) showing same-chirality zeros in the implemented AA/BB tensor model arise from signed fixed-degree polarization cancellation rather than support-level absence. Read the notes/scripts/data and identify any mathematical or coding errors, normalization risks, false interpretations, or useful next proof targets. Do not decide final Yau26 status; focus on correctness of this bridge evidence and its limits.

## Output

## Verification memo — Step 99 product-orbifold bridge check

### 1. The restatement of Step 98 is scientifically warranted

Treating the Step 98 chirality maps as a response inside the *implemented* spectral model — built from the Step 96 boundary source functional and the specific AB one-form / AA-BB tensor-scalar families — rather than as the complete leading Ozuch interaction is the correct reading of what the scripts compute. The corrected note's three factual repairs check out:

- **Topology.** For `#_3(S²×S²)`: connected sum gives χ = 4+4+4 − 2·2 = 8 and additive signature τ = 0. This also matches the resolution count: quotient underlying space has χ = (4−4)/2 + 4 = 4, and replacing each of the 4 cone points (χ=1) by an exceptional S² (χ=2) adds 4, giving χ = 8. Hitchin–Thorpe 8 ≥ (3/2)·0 imposes nothing, and `#_k(S²×S²)` carries positive scalar curvature so the ordinary Seiberg–Witten route gives no positive-Einstein exclusion. All correct. (One genuine subtlety: the smooth type and τ of the *mixed*-orientation filling depend on the self-intersection signs of the exceptional spheres; τ = 0 is stated for the specific `#_3(S²×S²)` identification, and the operative conclusions — no Hitchin–Thorpe, PSC — are robust regardless.)
- **Arithmetic.** 8a·t² ≈ 0.25154 t² vs the earlier 0.503 t² is a clean factor-of-2 matrix-trace correction (a ≈ 0.031442; 2a per adjacent source, 4a = 0.12577 isotropic, 8a for two adjacent sources). Internally consistent; the spin-2 channel 0.008 t² does sit below the isotropic 2a t² = 0.0629 t².

### 2. The local constructions in `step99_tensor_partial_jets.py` are correct

I re-derived the pieces the strengthening rests on:

- **Metric.** From g = dr² + sin²r dφ² one gets g_xx = 1 − y²/3, g_xy = xy/3, g_yy = 1 − x²/3, matching the code exactly (my first attempt via the curvature-tensor formula had a sign slip; the direct computation confirms the code). `ginv` is the correct O(2) inverse and √g = 1 − r²/6 follows from det g = 1 − r²/3.
- **Eigenfunction correction α.** I computed Δ_g ψ for ψ = b(x²−y²)(1+αr²) to degree 2 and obtained Δ_g ψ = b(12α−2)(x²−y²). Setting this to −μψ gives 12α−2 = −μ, i.e. **α = (2−μ)/12 exactly**, matching the code. Hence ψ is a genuine S² eigenmode to the needed order and E = Hess ψ + (μ/2)ψ g is truly trace-free (tr_g E = Δ_g ψ + μψ = 0). J at O(2) with J∂_x = ∂_y is consistent.

These verifications matter because trace-freeness and the eigenfunction property are what make E, M the intended electric / full-Lie magnetic modes rather than arbitrary tensors.

### 3. Partial-jet contraction (item i): a real but presumption-laden strengthening

The distinction the data draws is genuine and important: `arbitrary_same_factor_support_test` shows the receiver annihilates *all* same-factor rank-4 support (max 0), while the Step 96 **source does not** annihilate arbitrary same-factor support. Yet for the actual electric/magnetic m=2 partial jets ∂_p∂_q T, both source and receiver give exactly zero — confirmed symbolically in `step99_partial_jet_exact_contract.json` (all entries "0"). So the non-trivial content is that these specific families lie in the kernel of the source functional; this is not a generic receiver-sparsity artifact. That is a legitimate advance over Step 98's restricted product form.

Two things this does and does not settle:
- It addresses the ∂²T·f(pole) term (both derivative indices in the tensor's own factor). It presumes f(pole) enters only as a linear scalar amplitude, which is fine because contraction is linear.
- The note's further assertion that the **mixed first-derivative term** ∂_pT·∂_qf (one index in each factor, embedded in the mixed block H[a,c,p,2+q]) is invisible to both functionals is **not exercised by this script** — `arbitrary_support_max` only tests all-indices-in-one-factor support. It is attributed to `step99_modewise_selection_check.py`, which is not in the supplied material, so that portion of the strengthening cannot be independently reproduced from what is here. This is worth isolating because the mixed term is precisely the other piece of the full product-eigentensor second jet.

The stated presumption — that the true geometric eigentensor's same-factor jet lies inside the electric/full-Lie magnetic m=2 span, and that the Step 96 H⁴ functional is the correct distributional source — is the load-bearing input and is correctly identified as unproved.

### 4. Fixed-degree cancellation (item ii): consistent, with one uncovered slice

The logical architecture is sound: the heat prefactor π²·e^{−τP}/(P·norm) is strictly positive for every mode (P = (μ_t+μ_s)/2 − 1 ≥ 3 on the tested ranges, no zero divisor), so **per-degree vanishing of the ++/-- blocks implies the heat-summed B_{++}=B_{--}=0 independent of the positive weights.** The exact-rational certificate delivers that per-degree vanishing for the tested pairs, and its cross-block pattern (AA nonzero only for pair NS, BB only for SN) matches the Step 98 heat-sum table (NN←NS in AA, NN←SN in BB). The exact-degree script also enforces the same diagonal source/receiver mode matching (same kind, tseed, sseed) as the heat-sum script, so the two computations are contracting the same object. This internal cross-check is reassuring.

**One concrete uncovered region.** The heat-sum structure script sums `for ls in range(1, Lmax+1)` — it *includes* ℓ_scalar = 1, whose zonal m=0 harmonic has a nonzero isotropic Hessian at the pole and therefore feeds the AA/BB ++ block. The exact certificate tests only (2,2),(2,3),(3,2),(4,5),(5,4),(8,7), all ℓ_scalar ≥ 2, excluded because the *relative* m0 weight 2μ/(μ−2) diverges at μ=2. Consequences:
- The numerically observed B_{++}=0 (with ℓ_scalar=1 present) is therefore not fully certified by the exact ℓ_scalar ≥ 2 algebra.
- A useful inference: since the ℓ_scalar=1 mode has *only* the m=0 polarization (no m=2 partner to cancel against), the numerical B_{++}=0 already implies that the **pure-isotropic-scalar contribution to the same-chirality block vanishes on its own**. This can be confirmed cheaply by an exact check that isolates the m0-only ++ contribution using its absolute (not relative-to-m2) amplitude. If m0-alone gives ++=0, the uncovered slice is benign; if not, the numerical result and the certificate would be in tension. This is the single most direct check to close the item.

### 5. Normalization and reproducibility risks

- **Rationalization.** `rat(x)=Rational(str(float(x))).limit_denominator(1e6)` makes "exact" mean exact *relative to rationalized Step 96 coefficients*. Because the ++ block returns hard zeros (not 1e-13 residues) and the same rationalization is applied uniformly, the vanishing is consistent with structural sign-matching among rational coefficients; it presumes the underlying Step 96 receiver/source coefficients are genuinely rational (plausible: π_tr projections and curvature contractions are rational, with √ and π factoring into common amplitudes). If any Step 96 coefficient were irrational, an exact-0 obtained after limit_denominator could in principle differ from the true contraction. Recording the pre-rationalization residual magnitude would remove this doubt.
- **The m0 weight 2μ/(μ−2)** is load-bearing for the fixed-degree result and is asserted from the S² addition theorem rather than derived in-place. Whether the ++ vanishing depends on this exact value or holds for m0 alone (see §4) determines how sensitive the certificate is; deriving it directly is worthwhile.
- **Node-sign convention** (base = (−1)^ℓ, s2 seed flips sign) encodes the action of the π-rotation involution and the north/south pole reflection on scalar and tensor harmonics. This convention determines which cross-blocks are nonzero (NS vs SN vs SS). It is internally consistent with the Step 98 table but is not derived from the involution's action on the harmonics; a rigorous derivation of the pole-to-pole transport for the m=2 tensor value and the m=0/m=2 scalar Hessian would put the whole cross-block pattern on firm ground.
- Step 96's `receiver_matrix` / `source_matrix_over_pi2` are treated as black boxes here; the entire Step 99 conclusion inherits whatever assumptions define the Step 96 H⁴ boundary functional, which is not re-derived in the supplied material.

### 6. A concrete correspondence to sharpen the bridge

The exact cross-block matrices carry a recognizable structure. In the compact (00,11,01) representation the surviving +−/−+ block is [[1/2,−1/2,0],[−1/2,1/2,0],[0,0,±1/2]]; the top-left 2×2 [[1/2,−1/2],[−1/2,1/2]] is a single-direction (rank-one) form on (00,11). This mirrors Ozuch's linearized anti-self-dual curvature response, eqn (13): d_e R⁻(H⁴(ζ⁺)) = 12 π_tr(ρ(ζ)⁻ ⊗ ρ(ζ)⁻)/r⁶, a traceless π_tr(ρ⊗ρ) object built on one direction. Identifying the implemented +−/−+ block with this π_tr(ρ⊗ρ) curvature response — including the node-frame transport and quotient normalization — is the most direct route from the implemented model to the geometric gluing coefficient, and it would simultaneously supply the structural proof of the same-chirality vanishing (the (2,0)+(0,2) Kähler-kernel argument in §3 of the note). The same-chirality zero being a rank-one/self-dual-kernel phenomenon and the surviving block being the Ozuch rank-one curvature form are two faces of one identity; making that identity precise is the natural target.

### 7. What remains unproved (restated precisely)

The evidence establishes: (a) the omitted same-factor second jets of the electric/full-Lie magnetic m=2 families contract to exact zero against the Step 96 source and receiver, and (b) same-chirality vanishing in the implemented AA/BB model is a signed fixed-degree polarization cancellation (for ℓ_scalar ≥ 2), not per-mode support absence. It does not establish, and the notes correctly do not assert: the mixed first-derivative invisibility from supplied code; the ℓ_scalar=1 same-chirality vanishing as an exact certificate; the derivation of the pair map from the full geometric eigentensor basis with the Ozuch distributional identity, node-frame transport, and quotient factors; the self / deformation / complement / projector-motion terms of the projected equation and whether the positive inter-node direction survives projection; and heat-tail / o(t³) remainder control in a shared normalization. The implemented positivity of the inter-node matrix therefore does not yet function as an Ozuch obstruction, and even a completed local statement would remain specific to this product-orbifold degeneration and would not settle the interval proposition, whose output Einstein constant is unrestricted.

Net reading: the Step 99 work is a correct and genuine strengthening of a correctly restated implemented-model mechanism, with verified local geometry and one cleanly closable coverage gap (ℓ_scalar=1 / isolated m0), a few clearly identifiable normalization dependencies (m0 weight, node signs, Step 96 functional), and a well-posed geometric target (the π_tr(ρ⊗ρ) correspondence) that would convert the numerical/algebraic pattern into a proof.
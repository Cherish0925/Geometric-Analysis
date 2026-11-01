# TTCS Independent Branch Record

```json
{
  "step_id": 88,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step87_missed_mode_green_correction.md",
    "Sessions/S0910A01/workspace/data/step88_four_node_chirality_assembly.json",
    "Sessions/S0910A01/workspace/data/step87_missed_killing_mode_boundary.json",
    "Sessions/S0910A01/workspace/data/step87_l1_oneform_source_matrix.json",
    "Sessions/S0910A01/trace/ttcs/results/step87_ttcs01_verifier1_integration.md"
  ]
}
```

## Task

Verify the four-node assembled chirality source structural theorem for the product orbifold (S²×S²)/Z₂ desingularization. The claim has three parts:

1. NODE-SIGN COINCIDENCE: For the axial Killing-Killing mode h=(*dZ_A)⊙(*dZ_B) with P eigenvalue 1, the source boundary projection satisfies B_j^ε(h) = ε·s_j·(π²/2) where s=(+1,-1,-1,+1) for nodes (NN,NS,SN,SS). The sign vector s coincides with the mixed-chirality assignment pattern. Verify this from the normal-coordinate expansion of *dZ on each S² factor (sign reversal at the south pole of the height-function Killing form).

2. STRUCTURAL NON-CANCELLATION: The four-node chirality-odd assembled source is Σ_j w_j ε_j s_j. For mixed-diagonal (ε_j=s_j), this equals Σ w_j (always positive). For all-same (ε_j=+1) with equal scales, it equals 0. Therefore the mixed-chirality construction activates a global response absent from the symmetric KE control, and no positive scale choice can cancel it.

3. EIGENSPACE ISOLATION: Among the complete quotient-descending TT modes at λ=1, only the axial mode *dZ_A⊙*dZ_B has nonzero chirality source difference at the V₂ boundary-pairing level. The equatorial modes (*dX⊙*dX, etc.) have V₀≠0 at the poles and zero V₂ chirality source difference. Therefore the chirality-odd source at λ=1 is one-dimensional and there is no intra-eigenspace cancellation.

Check each part mathematically. For part 3, verify that the equatorial Killing forms at the poles have constant leading terms that do not produce fully-mixed V₂ derivative/tensor index quartets. Also check: does P h=1>0 mean this is a correction field (not an obstruction), and what is the physical content? Can higher eigenspaces (λ>1) potentially cancel the λ=1 contribution, or does the 1/λ decay in the spectral sum make the leading term dominant?

## Output

# Verification Memo — Four‑Node Assembled Chirality Source for (S²×S²)/ℤ₂

## Summary judgment

The three structural statements hold at the level they are actually computed: the node‑sign vector `s=(+,−,−,+)` follows from an orientation‑independent property of the height functions; the assembled source superposition does not cancel under the mixed‑diagonal chirality assignment while it does cancel for the equal‑scale symmetric assignment; and among the coexact one‑form products the axial `*dZ_A⊙*dZ_B` is the unique carrier of a nonzero chirality difference in the quartic link‑sphere pairing. All three, however, are statements about a **local source superposition** `Σ_j w_j B_j^{ε_j}`, not about the inter‑node obstruction `L_i G_P^⊥ S_j` that actually enters the Einstein deformation. Two mathematical facts keep the single‑eigenspace result from settling `c_opp − c_same`: the receiver functional is distinct from the source functional, and modes at other eigenvalues (including the `−1` shape mode) enter with weights `1/λ` of both signs. I also found one genuine internal number inconsistency (a factor of two in the reported per‑node constant) that should be reconciled in the deliverable, and one enumeration that is asserted rather than proven (completeness of the `λ=1` TT eigenspace beyond one‑form products).

---

## Part 1 — Node‑sign coincidence `s=(+,−,−,+)`

This is correct, and there is a cleaner reason for it than the frame‑orientation wording used in the notes.

The Killing one‑form on a unit `S²` is `*du` with `u = cosθ` the height function. Directly,
`*du = −sin²θ dφ`, with `|*du|²_p = sin²θ` and zeros exactly at the two poles. In an orientation‑preserving normal chart at the north pole `α ≈ x₁dx₀ − x₀dx₁`; at the south pole the same global one‑form expands as `α ≈ −(x₁dx₀ − x₀dx₁)`. The sign flip is **not** a frame artifact — it is forced by the fact that `u = +1` at N and `u = −1` at S, so the second‑order coefficient of `*du` carries the sign of `u` at the pole. This makes the per‑factor sign `σ(N)=+1`, `σ(S)=−1` an invariant, independent of any choice of local orientation.

Because the source integrand is bilinear in the two factor coefficients, the node sign factorizes,
`s_j = σ_A(pole_A)·σ_B(pole_B)`, giving `NN:+`, `NS:−`, `SN:−`, `SS:+`. This is exactly the `sign_vector` in `step88_four_node_chirality_assembly.json`, and it is read off consistently from the `B_plus_over_pi2` signs there.

One point that deserves explicit care and is handled correctly only because of a fixed global orientation: the chirality label `ε` in `B_ε` is defined through the self‑dual/anti‑self‑dual `C_{2k}` vs `C_{k2}` families, which are fixed relative to the ambient orientation of the resolved 4‑manifold. If the four node frames were taken with independent local orientations, a reflection between nodes would swap `+↔−` and could contaminate `s_j`. The computation avoids this because all four `A₁` charts inherit one ambient orientation, so `s_j` comes only from the height‑function coefficient and `ε` is a globally fixed splitting. Worth stating in the writeup that the node signs and the SD/ASD split are referred to a single orientation; otherwise the coincidence `s = mixed‑chirality pattern` is not well posed.

Also confirm the quotient generator: the simultaneous `π`‑rotation about the two Z‑axes fixes `{N,S}×{N,S}` with local isotropy `−I` on `ℝ⁴`, i.e. four `A₁` points, matching Eguchi–Hanson gluing. `*dZ` is invariant under rotation about its own axis, so `*dZ_A⊙*dZ_B` descends. This is internally consistent with the `descends_under_simultaneous_pi_rotation: true` entry.

## Part 2 — Non‑cancellation of the assembled source

Given Part 1, the algebra is elementary and correct: the chirality‑odd assembled source `Σ_j w_j ε_j s_j (const)` becomes `Σ_j w_j (const)` when `ε_j = s_j` (since `s_j²=1`), which is strictly positive for positive weights, and becomes `(const)Σ_j w_j s_j = 0` for `ε_j=+1` at equal weights because `Σ_j s_j = 1−1−1+1 = 0`. The mechanism statement — that the node‑sign vector coinciding with the chirality assignment converts an alternating sum into a total — is exactly right for this superposition.

What this establishes and what it does not:

- It establishes that **if** the assembled radial obstruction were the positively weighted node sum of the local source projections, mixed‑diagonal chirality could not be cancelled by any positive scale choice, while the symmetric equal‑scale configuration sees zero from this mode.
- It does **not** establish the same for the actual obstruction. The object that feeds the Einstein deformation is the inter‑node response `L_i G_P^⊥ S_j` (source at node `j`, transported by the resolvent on `(ker P)^⊥`, received by the curvature functional at node `i`). The transport `G_P^⊥` and the receiver `L_i` carry their own node‑dependent signs and can reintroduce sign structure that the pure source sum does not see. The positivity of the weights `w_j` themselves (bubble scales entering the assembled functional) is also assumed rather than derived here.

So Part 2 is a correct statement about `Σ_j w_j B_j^{ε_j}` and a well‑motivated heuristic for the obstruction, but the phrase “activates a global response absent from the symmetric control” is proven for the source superposition, not for the radial obstruction that decides Einstein solvability.

## Part 3 — One‑dimensional chirality‑odd source at `λ=1`

The eigenspace count is clean and I can reproduce it. Quotient‑descending coexact one‑form products `*dX_a⊙*dX_b` require even total parity under the `π`‑rotation with `X,Y` odd and `Z` even. The even products are the four odd×odd combinations `XX, XY, YX, YY` plus the one even×even `ZZ`, giving dimension 5, matching `lambda_1_TT_eigenspace.dimension_on_quotient: 5`. Among these only `ZZ` has both factors vanishing at the Z‑poles, hence `V₀ = 0` and a pure quadratic (`V₂`) jet; the `X/Y` combinations have `V₀ ≠ 0` at the poles (their Killing fields do not vanish on the Z‑axis) and the data record zero chirality difference in the quartic pairing for all of them. This confirms the isolation statement at the `V₂` link‑sphere pairing level: the chirality‑odd source at `λ=1` from this family is one‑dimensional, with no intra‑family cancellation.

The reason the equatorial modes give zero chirality difference is exactly as stated: the SD/ASD‑splitting source arises from the fully mixed four‑index quartet `M_{03,12}, M_{12,03}` in the pure `V₂` jet; a mode with `V₀ ≠ 0` contributes to the source through constant‑times‑jet channels that do not populate the mixed quartet symmetrically, and the computed difference is zero. This is consistent.

Two things temper the “one‑dimensional” statement:

1. **Completeness of the eigenspace.** The dimension‑5 count is for the coexact one‑form product family only. That the entire `λ=1` TT eigenspace on the quotient is exactly this 5‑dimensional space is asserted, not shown. On each `S²` there are no TT symmetric 2‑tensors (genus 0), which removes the scalar×2‑tensor channel, but a full tensor‑harmonic decomposition of the product operator `P = ½∇*∇ − R̊` — checking that no other constituent combination lands at exactly `λ_P = 1` in the TT class — is not in the supplied data. The `l=1` one‑form product is the only family exhibited.
2. **The `V₂` pairing is not the whole source.** The `V₀ ≠ 0` equatorial modes still require the constant‑jet/receiver‑frame handling noted in the step 87 material; their zero here is at the quartic pairing only, not a statement that they contribute nothing to the obstruction through the receiver side. So the one‑dimensionality is specific to the quartic source pairing.

---

## The two physical questions

**Is `Ph = h > 0` a correction field rather than an obstruction, and what is its content?**
Yes. `λ = 1 ≠ 0` places `h` in `(ker P)^⊥`, so it is not a zero mode and the nonzero source violates no solvability condition; `P` is invertible on this mode and produces a definite first‑order correction field `G_P^⊥ S`. The physical content is second order: this chirality‑dependent correction field feeds back into the radial obstruction through its pairing with the receiver curvature functional. The leading obstruction quantity has the schematic form `Σ L_i G_P^⊥ S_j`, i.e. a bilinear pairing of the source at one node, transported by the resolvent, against the curvature response at another node. The `λ=1` mode being active means one specific channel of this bilinear pairing is nonzero, which is what removes the earlier mode‑by‑mode annihilation, but the pairing itself is the physical obstruction, not the source alone.

**Can higher eigenspaces cancel the `λ=1` term, or does `1/λ` decay make the leading term dominant?**
The `λ=1` term cannot be promoted to control the total. The resolvent weights each eigenspace by `1/λ`, so `λ=1`, being the smallest positive eigenvalue in this family, carries the largest positive weight per mode — but three facts prevent “largest weight per mode” from meaning “dominant”:
- Eigenspace dimension grows with `λ` (Weyl growth in dimension 4), and the source/receiver coefficients built from the quartic jet grow polynomially, so the per‑shell contribution need not decrease with `λ`; absolute convergence of the spectral sum requires the product decay to beat the dimensional growth, which the simple `ℓ^{-3}` estimate in the earlier note did not secure.
- Modes at eigenvalue below zero (in particular the `P = −1` shape mode) enter with weight `1/λ < 0`, i.e. with sign opposite to the `λ=1` term; these contribute to `c_opp − c_same` with the opposite orientation and are not suppressed.
- The obstruction is a source‑against‑receiver pairing, not a source self‑pairing, so per‑eigenspace terms can carry either sign independently of the sign of the source difference.

Consequently higher and sub‑zero eigenspaces can add to or cancel the `λ=1` contribution, and the nonzero `λ=1` term establishes only that `c_opp − c_same` is not forced to vanish by a mode‑wise argument. Its actual value and sign require the regularized resolvent sum over all admissible sectors, with the `−1` modes and the kernel projection handled explicitly, and with the same‑node local part subtracted.

---

## One number to reconcile and one convention to state

- **Factor of two.** `step88_...json` reports per‑node `B_plus_over_pi2 = ±0.25` and the odd‑source pattern `s_j·π²/4`, but the same file’s `structural_theorem.statement` string writes `(π²/2)`, and the task text also states `ε·s_j·(π²/2)`. The step 87 data give `B_+ = π²/2` for the unsymmetrized `α⊗β+β⊗α`. The discrepancy is the symmetric product normalization: `⊙ = ½(⊗+⊗)` halves the source to `ε s_j π²/4`. The per‑node constant in the theorem string should be brought to `π²/4` to match the `⊙` data, or the notation changed. The structural conclusions (sign pattern, non‑cancellation, isolation) are independent of this overall constant.
- **The dimensionless `9/256` is normalization‑free, which is correct.** With `B` linear in the mode and `‖h‖²` quadratic, `B²/(λ‖h‖²)` is invariant under rescaling `h`; I checked both normalizations give `9π²/256`. Note however that this number uses `source²`, i.e. it identifies source with receiver. The receiver curvature response is a different functional (values `±1` in the script convention, not `π²/2`), so `9/256` is a formal single‑mode self‑pairing and not the physical `L_i G_P^⊥ S_j` coefficient. It should not be read as a contribution to `c_opp − c_same`.
- **`‖h‖² = 64π²/9` checks out.** On `S²`, `|*dZ|² = sin²θ` gives `∫_{S²}|*dZ|² = 8π/3`; the product symmetric tensor has `|h|² = 2|α|²|β|²` (cross term vanishes across factors), so `∫_{S²×S²} = 128π²/9`, and the quotient value is `64π²/9`. Consistent.
- **`Ph = h` checks out.** On unit `S²`, coexact `l=1` one‑forms satisfy `Δ_H α = 2α`, and Weitzenböck with `Ric = g` gives `∇*∇α = α`; the product gives `∇*∇h = 2h`. The Lichnerowicz curvature term `R̊h` vanishes because `h` is fully mixed while the product Riemann tensor has no mixed `AB` components, so `P h = ½·2h − 0 = h`. Consistent with the stated sector eigenvalue `½(2+2−2)=1`.

## What remains open before this reaches `c_opp − c_same`

The exact unresolved object is the orientation‑fixed, inter‑node, `L²`‑normalized, regularized bilinear pairing `L_i G_P^⊥ (S_j^+ − S_j^-)` summed over the four nodes and all admissible eigenspaces, with the kernel projection and the `−1` eigenvalue modes treated explicitly and the same‑node singular part subtracted. The present work rigorously supplies one input to this — an active, sign‑resolved `λ=1` source channel with a matching nonzero receiver response — and shows the naive source superposition does not cancel under the mixed‑diagonal assignment. It does not yet supply the resolvent transport, the receiver normalization against the Ozuch/Biquard radial obstruction variables, the completeness of the `λ=1` TT eigenspace, or the convergent sum over the remaining spectrum, so the sign and magnitude of `c_opp − c_same` are not determined by these three statements.
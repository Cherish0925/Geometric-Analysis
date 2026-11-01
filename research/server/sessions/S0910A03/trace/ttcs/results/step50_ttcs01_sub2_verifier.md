# TTCS Independent Branch Record

```json
{
  "step_id": 50,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step50_normalized_yang_wang_verification.md",
    "Sessions/S0910A03/workspace/notes/step44_normalized_yang_tame_start_restart.md",
    "Knowledge/objects/papers/Convergence-of-riemannian-manifolds-with-integral-bounds--2b2a6e7ac566--6b3174861309/object.md"
  ]
}
```

## Task

Independently verify the source-based short-time existence argument in the Step 50 note for the degenerate normalized cutoff flow ∂t g=-2χ²(Ric+g). Read Yang's actual Theorem 8.2 lines 785–823 and the Step 44/Step 50 notes. Check the exact Eulerian variation δ[-2(χ∘φ^{-1})² ĝ], its placement in Yang's displayed D h+E ψ slots, and whether the stated Sobolev product/composition estimates genuinely preserve Yang's neighborhood-uniform smooth-tame inverse and unchanged finite derivative loss. Identify any missing term, regularity index, circularity, or unjustified passage. This should be a direct mathematical verification, not a generic review.

## Output

## Verification memo: source-based short-time existence for ∂ₜg = −2χ²(Ric+g)

### Summary

The short-time (start/restart) argument in Step 50 §2 and Step 44 is mathematically correct as a reduction, and the three items you asked me to check hold: the Eulerian variation δ[−2(χ∘φ⁻¹)²ĝ] is computed correctly, it lands exactly in Yang's zeroth-order D and E slots, and the product/composition estimates do preserve Yang's tame inverse with the same finite derivative loss. The one substantive thing to keep in view is that the argument imports — and does not reconstruct — Yang's Theorem 8.2 tame inverse, including two ingredients that Yang's text compresses into "standard arguments." I detail each below with the checks I actually ran.

### 1. The Eulerian variation is correct (with an explicit sign check)

The only term added to Yang's transported DeTurck metric equation is `−2âĝ`, `â = (χ∘φ⁻¹)²`; the DeTurck gauge term `−δ̂*(â S⁻¹δG(S))` in (2.1)/(1.1) is character-for-character Yang's (8.5), so nothing else is new. Since `â` depends on `φ` only (not on `ĝ`), the full variation of the new term is exactly

- `∂/∂ĝ`: `−2âh`,
- `∂/∂φ`: `−2(δâ)ĝ`, with `δχ̂ = −dχ̂(ζ)`, `ζ = δφ∘φ⁻¹`, hence `δâ = −2χ̂ dχ̂(ζ)`, giving `+4χ̂ dχ̂(ζ)ĝ`.

I verified the sign of `δχ̂` on the model `φ_s = id + sV`, `φ₀ = id`: then `ζ = V`, `χ̂_s = χ∘φ_s⁻¹ ≈ χ − s dχ(V)`, so `δχ̂ = −dχ(V) = −dχ̂(ζ)`. This reproduces (2.3) and the boxed (2.4)

  `δ(−2âĝ) = −2âh + 4χ̂ dχ̂(ζ)ĝ`.

There is no derivative of `h` or of `ζ` in either piece, and no cross-term from `δĝ` entering `â` (because `∂â/∂ĝ = 0`). The variation is complete; nothing is missing.

### 2. Placement in the D, E slots is type-consistent and complete

`−2âh`: scalar × symmetric 2-tensor → symmetric 2-tensor; this is a zeroth-order operator on `h`, so `D ↦ D − 2â·Id`. `4χ̂ dχ̂(ζ)ĝ`: `dχ̂(ζ)` is a scalar contraction of a vector deformation, times `ĝ`; this maps the diffeomorphism deformation (vector) to a symmetric 2-tensor, which is exactly the type of Yang's `E`. So after the `ζ↔ψ` identification, `E ↦ E + 4χ̂ dχ̂(·)ĝ`. Both are genuinely zeroth order; the principal term `2χ̂²Δh` and the first-order slots `B, C` are untouched. This is why the parabolic structure and the χ̂-weighted dissipation are unchanged. (2.6) is correct.

### 3. Pullback/gauge cancellation is intact

I checked (2.2)/(1.3). For `g = φ*ĝ`, the added term contributes `φ*(−2âĝ) = −2(φ*â)(φ*ĝ) = −2a g`, using `φ*â = (χ∘φ⁻¹∘φ)² = χ² = a`. Because `âĝ` carries no curvature and no DeTurck gauge structure, it does not enter the Lie-derivative cancellation that DeTurck's term performs; that cancellation is Yang's, unchanged. So the geometric equation `∂ₜg = −2a(Ric_g + g)` is produced exactly, with no coefficient limit. This is the correct and non-circular start construction, in contrast to the `a+ε²` nonlinear route the note discards in §1.

### 4. The product/composition estimates preserve the tame inverse with unchanged loss — and the reason is stronger than stated

The Moser estimate (2.7) (`s₀ > n/2+2`, `s ≥ s₀`) and the composition/inversion estimate (2.8) are standard tame calculus on the diffeomorphism neighborhood, and `K_u` in (2.9) is a zeroth-order operator whose coefficients (`â`, `χ̂ dχ̂`, `ĝ`) are smooth-tame functions of the reference pair. Hence (2.10)–(2.11) follow: the high–low form with a finite loss `r`, and in the differentiated energy the worst allocation is `⟨∇ˢh, ∇ˢ(4χ̂dχ̂(ζ)ĝ)⟩ ≲ E_s(h)^{1/2}E_s(ψ)^{1/2}`, a same-order coupling with no term at order `s+1`, so it does not compete with `‖χ̂∇^{s+1}h‖²`. Gronwall on the combined energy `E_s(h)+A_s E_s(ψ)` closes.

The decisive point that makes "loss `r` unchanged" solid — and I think this deserves emphasis because it is what actually secures the reduction — is that the composition type `χ∘φ⁻¹` and its `φ`-derivatives already occur in Yang's system. Yang's own DeTurck gauge term `δ̂*(â S⁻¹δG(S))` contains `â`, and its `φ`-variation produces `δâ = −2χ̂dχ̂(ζ)` times a smooth tensor, with a `δ̂*` applied. So Yang's `r` already covers `dχ̂(ζ)`-type compositions carrying one `δ̂*`. The normalization's new term is the *same* composition type with *no* `δ̂*`, i.e. milder. Therefore it fits inside Yang's existing loss a fortiori, and introduces no new composition class. The note's phrase "no new composition type" is thus justified by the structure of Yang's gauge term, not merely asserted.

### 5. What is imported rather than proved (genuinely open for a self-contained/Lean version)

The verification above establishes the incremental adaptation. It rests on Yang's Theorem 8.2 possessing the neighborhood-uniform smooth-tame inverse it asserts. Two specific pieces of that inverse are not visible in the source excerpt (lines 785–823 read "The smooth tame estimates are obtained by standard arguments") and are therefore not independently checkable from the supplied material:

- **Symmetrizability of the ψ-transport.** Step 44 §3.3 needs `P∇ψ` to be covariant differentiation along a smooth field (a smooth symmetrizer) so that (3.7) closes without losing derivatives in `ψ`. Yang does not display `P`. This is highly plausible (the φ-equation is a transport equation generated by a vector field), but it is an input, not a derived fact, and it is precisely where the `ψ` energy could otherwise leak derivatives.
- **Reference pairs with φ ≠ id.** Yang's displayed linearization appears set at the identity (`ζ = ψ` there). The note's neighborhood-uniform statement uses `φ` in an `H^{s₀+1}` neighborhood of the identity and identifies `ζ = ψ∘φ⁻¹` by right translation, invoking tame composition. This is the form a fixed-point/Nash–Moser scheme needs, and Yang asserts it, but the source does not exhibit the uniform-over-reference estimates.

The Step 44/50 notes state openly (§3.6, §7; §2.4) that they do not reconstruct Yang's inverse. So the memo's positive verdict on the start is: correct *given* Yang's inverse. For the ultimate Lean formalization, these two pieces plus the full high–low tame inverse must be built explicitly; they are the real residual work behind "standard arguments."

### 6. Minor notes

- Yang writes the linearized diffusion coefficient as `2χ²Δh`; reading `χ` here as the transported `χ̂ = χ∘φ⁻¹` (as the note does) is the correct interpretation after the DeTurck substitution.
- The note augments Yang's homogeneous displayed system with forcing `f, η`; this is the standard Nash–Moser residual forcing and is consistent.
- The restart/gluing in Step 44 §6 (autonomy ⇒ matching right/left time-jets at `T_*` from `C^∞` convergence) is a correct standard argument.
- The shifted-curvature identities in §3.1 (`G = g⊛g/(2(n−1))`, `Ric(G)=g`, so `Ric(T)=Ric+g`) belong to the continuation (§3), not the start; the factor `1/(2(n−1))` is exactly the normalization that makes `Ric(G)=g`. This is internal to the extension argument and not part of the short-time existence you asked me to check, but the identity is convention-consistent.

**Bottom line for the start:** variation correct, placement correct and type-consistent, gauge cancellation intact, tame estimates preserved with unchanged finite loss (backed by the observation that the same composition type already sits in Yang's gauge term). The construction is non-circular. The only things not settled from the supplied source are Yang's own compressed inverse ingredients (ψ-transport symmetrizer, reference-uniform tame inverse), which the notes correctly flag as imported.
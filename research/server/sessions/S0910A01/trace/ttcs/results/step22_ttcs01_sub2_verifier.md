# TTCS Independent Branch Record

```json
{
  "step_id": 22,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step22_current_energy_formulation.md",
    "Sessions/S0910A01/workspace/notes/step22_weak_nested_moment_estimate.md",
    "Sessions/S0910A01/workspace/plans/route_assessment_step22.md",
    "Sessions/S0910A01/workspace/scripts/step22_energy_normalization.py",
    "Sessions/S0910A01/workspace/scripts/step22_first_exit_energy.py",
    "Sessions/S0910A01/workspace/scripts/step22_weak_moment_ledger.py",
    "Sessions/S0910A03/workspace/notes/step20_weighted_wang_hierarchy_and_whitney_correction.md"
  ]
}
```

## Task

Verify the Step 22 repair to the cutoff-flow smoothing argument for Yau Problem 26's four-dimensional negative LeBrun/Ishida-LeBrun laboratory. Read the corrected notes and scripts. The scientific questions: (1) Does the correction correctly distinguish component energy int_U F^2 <= M Vol(U) from the false Whitney-volume-normal bound int_W F^2 <= C M Vol(W)? (2) Does the retained scale-invariant Whitney estimate ell^4 average_W F^2 and the Sobolev product A_W^2||F||_2 <= C r^2 sqrt(M) follow with the right powers? (3) Is the current component first-exit formulation Gamma(t)=sup A_alpha^2 H_2,alpha(t)^{1/2} the right way to prove energy persistence and cubic potential A^4 H_3 <= C Gamma^3/t? (4) Does the weak nested moment estimate use the correct weights H_q=int eta^2 a^(q-2)F^q and v_q=eta a^((q-1)/2)F^(q/2), and are the Holder/Sobolev exponents, finite-neighbor terms, and endpoint scalings scientifically consistent? Identify any remaining mathematical gaps or wrong inferences, especially about transition curvature closeness, metric displacement, unweighted defect Q, and plateau bounded-curvature needs. Do not decide the whole research route; give a mathematical verification memo.

## Output

## Verification memo: Step 22 energy correction for the cutoff-flow smoothing route (4D LeBrun / Ishida–LeBrun setting)

I re-derived the algebra behind each numbered relation in the two Step 22 notes and the A03 Step 20 note, and I re-ran the exponent bookkeeping the three scripts encode. Below I separate what checks exactly, what is internally consistent but rests on an un-written PDE input, and one quantitative tension the notes do not address. The scripts are exponent/scaling consistency checks, not derivations of the tensor inequality and not numerical PDE evidence; I verified they certify what they say they certify.

### Q1 — component energy vs. the false volume-normal bound: correct

The distinction is mathematically right. With `U=B_{5r}(p)`, `W=B_ℓ(y)`, `y∈B_{4r}(p)`, `ℓ=crχ₀≤r`, one has `W⊂U` (since `4r+ℓ≤5r`), so `∫_W F² ≤ ∫_U F² ≤ M Vol(U)` — relation (1.2). The refusal of `∫_W F² ≤ CM Vol(W)` is correct: the total budget permits all energy to concentrate in `W`, and `Vol(W)/Vol(U)` can be as small as `∼χ₀⁴`, so the mean over `W` can grow like `χ₀⁻⁴ M`. I confirmed `step22_energy_normalization.py` realizes exactly this worst case (`meanW/M = 5⁴/(c⁴χ₀⁴)`).

One point worth stating explicitly: the volume comparison `Vol(W) ≥ b(ℓ/5r)⁴ Vol(U)` (1.3) is Bishop–Gromov between **non-concentric** balls. It is obtained by comparing concentric balls at `y`: `B_ℓ(y) ⊂ B_{9r}(y) ⊃ B_{5r}(p)`, giving `Vol(W) ≥ b'(ℓ/9r)⁴ Vol(U)`. The exponent 4 is correct; the constant differs from `5⁻⁴` and is absorbed into `b`. This step uses a lower Ricci bound on the **evolving** metric `g(t)`, or a bilipschitz transfer of the initial Bishop–Gromov. The transfer of a shrinking-ratio inequality between `W` and `U` under bilipschitz equivalence is legitimate (the exponent survives, the constant degrades by a bounded power of `Λ`), so this is coherent given that the pinching hypothesis supplies a lower Ricci bound at `t=0`.

### Q2 — scale-invariant Whitney estimate and Sobolev product: right powers

Both survive with correct powers.
- `ℓ⁴ ⨏_W F² ≤ b⁻¹5⁴ M r⁴` (1.4): I recomputed `ℓ⁴·meanW/(Mr⁴)=5⁴/b`, independent of `χ₀`. The script prints a constant `625` across all `χ₀`, confirming cancellation.
- `A_W²‖F‖_{L²(W)} ≲ r²√M` (1.5): using the 4D relative Sobolev scaling `A_W² ≃ ℓ² Vol(W)^{-1/2}` (this is `ℓ² Vol^{-2/n}` at `n=4`), I get `A_W²‖F‖₂ = ℓ² Vol(W)^{-1/2}(M Vol(U))^{1/2} ≃ 25 r²√M`, again `χ₀`-independent. The script's `gamma` reproduces `25 r²√(M/b)`. Powers are all correct.

### Q3 — first-exit `Γ(t)=sup_α A_α² H_{2,α}(t)^{1/2}` and cubic potential: structurally sound

- Initial smallness `Γ(0) ≤ Cr²√(1+K₀)` (2.2) is the same quantity as (1.5), consistent.
- The `q=2` reaction absorption is correct: `H₃=∫η²aF³=∫F·(ηa^{1/2}F)²`, Hölder + 4D Sobolev on `v₂=ηa^{1/2}F` give `H₃ ≤ γ(D₂+r⁻²H₂)`, and `γ=A²‖F‖₂` is the `Γ`-controlled small factor (2.4). The `a`-weight in `∫η²aF²≤H₂` is dominated because `a≤1`. Absorption for `CΓ_*` small yields (2.5).
- The rate constant in `H'_{2,α} ≤ Cr⁻²Σ_{β∼α}H_{2,β}` is genuinely `χ₀`-independent: `a|dη|²≤C4^k r⁻²` and `|da|²/a=4|dχ|²≤Cr⁻²`. I verified `a|dη|²=χ₀²(crχ₀)⁻²=1/(c²r²)` in the ledger, matching (1.2). Hence persistence `Γ(t) ≤ C_Λ e^{CNθ/2}Γ(0)` (2.7) over `T=θr²` with dimensional/overlap constants only.
- The first-exit continuity closes for small `θ`: with threshold `4Γ(0)` and `C_Λ e^{CNθ/2} → C_Λ` as `θ→0`, a bilipschitz `C_Λ≈1.2` stays below 4. `step22_first_exit_energy.py` confirms this numerically (`Γ(T)=1.39e-3 < 4Γ₀=4.42e-3`) and the ring-graph ODE reproduces the `e^{C·deg·θ}` boundedness.
- Cubic potential `A⁴H₃(t) ≤ CΓ_*³/t` (3.5): I re-derived the chain. The spacetime bound `∫₀^t ΣH₃ ≤ CΓ_* ΣH₂(0)` (3.1) follows from integrating (2.3) and `∫₀^t ΣH₂ ≤ Cθr²ΣH₂(0)`; the `q=3` inequality (3.3) with `v₃=ηaF^{3/2}` (I checked `v₃²·F=η²a²F⁴=∫η²a^{q-1}F^{q+1}` at `q=3`) gives `H'_{3,α}≤Cr⁻²ΣH₃`; backward averaging on `[t/2,t]` produces (3.4); then `H₂(0)≤Γ(0)²/A⁴` and comparable `A` on the neighbor star give (3.5), up to using `Γ(0)≲Γ_*`. Correct.

### Q4 — weights, Hölder/Sobolev exponents, endpoints: all consistent

The weighted scheme is internally exact and 4-dimensionally correct.
- Weights: `v_q²=η²a^{q-1}F^q`, `v_q⁴=η²a^{2q-2}F^{2q}=H_{2q}` density, `Fv_q²=η²a^{q-1}F^{q+1}=` reaction. Verified symbolically (matches the ledger's `add`/`mulc` assertions).
- Reaction Hölder `R_q ≤ H₃^{1/3}H_{3q/2}^{2/3}` (2.1): the density `a`- and `F`-powers are exactly `(q-1,q+1)`; I recomputed `1/3+(3q/2-2)·2/3=q-1` and `1+(3q/2)·2/3=q+1`. Correct.
- Interpolation `H_{3q/2}≤H_q^{1/2}H_{2q}^{1/2}` (2.2) is Cauchy–Schwarz on the split `a^{(q-2)/2}F^{q/2}·a^{(2q-2)/2}F^q`; density matches.
- 4D Sobolev `H_{2q}^{1/2}=‖v_q‖₄²≤A²(D_q+C4^k r⁻²H_q)` (2.3). Combined with Young gives `R_q ≤ εD_q + C(4^k r⁻² + ε⁻²A⁴H₃)H_q` (2.4); I checked the Young split `X^{2/3}Y^{1/3}` with `X=εD_q`, `Y=ε⁻²A⁴H₃H_q`. Once `A⁴H₃≤CΓ_*³/s` on `[t/2,t]`, the reaction becomes the lower-order potential (2.6). The same algebra transfers verbatim to the defect moments `J_m`, `z_m` (2.7).
- Iteration exponent: `q_{j+1}=3q_j/2` is precisely the parabolic-Moser gain `(n+2)/n=6/4=3/2` at `n=4`. This is the right dimensional exponent and is one reason the whole construction is 4-specific.
- Convergence: `Σ1/q_j=3/q₀`, `Σ(j+log q_j)/q_j<∞`; polynomial-in-`q`, `4^j`, and fixed Sobolev/overlap factors have convergent products. Verified.
- Endpoints: I reproduced both from (11.4). Curvature `q₀=2`: `A²(t⁻¹)^{3/2}(tH₂)^{1/2}` with `H₂≤Γ_*²/A⁴` gives exactly `CΓ_*/t` (4.3). Defect `q₀=6`: `A^{2/3}t^{-1/2}(tδ⁶V)^{1/6}` with `A≃rV^{-1/4}` gives exactly `δ(r²/t)^{1/3}` (4.4). Volume factors cancel as stated.

I also spot-checked the two most dangerous terms in the un-written tensor inequality (1.1), because the entire distinction between the valid weighted scheme and the false unweighted one lives in the count of `a`-powers:
- The `da*∇E` term contributes `∫η²a^{q-2}F^{q-1}|da||∇Rm|`; regrouping against `∇v_q` and using `|da|²/a=4|dχ|²≤Cr⁻²` gives `≤εD_q+Cr⁻²H_q` — no negative power of `a`, consistent with (1.2).
- The reaction `a(Rm*Rm)` contributes `∫η²a^{q-2}·a·F^{q+1}=∫η²a^{q-1}F^{q+1}` — exactly the claimed power `a^{q-1}F^{q+1}`.

So the two structurally risky terms produce the exact weights the notes assert. This raises confidence that (1.1) is derivable as stated, but the full contraction (every Hessian-`a` integration by parts, the evolving-measure term `∂_t dμ=-tr(aE)dμ`, the `F=(1+|Rm|²)^{1/2}` regularization producing lower-order constants, and all reaction cross-terms) is not written and remains the central un-derived PDE input.

### Correctly removed wrong inference

The excision in §5 (both notes) is right. `∫₀^T|aE|dt ≤ Cδr²` (5.1) controls the C⁰/bilipschitz displacement of the metric but says nothing about `Rm(T)−Rm(0)`, which involves second derivatives the hypotheses do not bound. I also checked (5.1) is consistent with (4.4): `∫₀^{θr²} Cδ(r²/t)^{1/3}dt = Cδ r² θ^{2/3}`, finite because the exponent `1/3<1`. Not using transition curvature closeness, and instead carrying bounded curvature on plateaux (`a=1`) plus triangular defect energy through the transition, is the mathematically defensible route.

### Remaining mathematical pieces and one tension

The notes are forthright about most of these; I confirm they are genuine and add specificity.

1. **Full tensor derivation of (1.1)/(2.1)/(A03 3.1)** for `∂_t g=-2χ²(Ric+g)`. Spot-checks pass, but the complete `a`-power accounting is what makes or breaks the weighted scheme; it is the foundation of everything downstream.

2. **Existence, lifespan, and smooth extension of the spatially-cutoff normalized flow** on `[0,θr²]`. The moment machinery presupposes a smooth solution with first-exit comparability. A03 §12 correctly records that no published theorem states this for `−2χ²(Ric+g)`; Wang's Theorem 4.1 / Lemmas 4.4–4.14 and Fei He's normalized-flow remark are structural precedent, not a solution theorem. This is a prerequisite, not a detail, and adapting Wang's `−2a·Ric` extension to the `+g` normalization is explicitly acknowledged as un-written.

3. **A single simultaneous first-exit continuity argument.** Metric comparability, persistence of relative Sobolev constants, buffered containment, `Γ`-smallness, and defect-energy preservation are coupled: small `Γ` ⇒ small `∫|aE|` ⇒ metric stays comparable ⇒ Sobolev persists ⇒ `Γ` stays small. The notes establish each piece conditionally on the others but do not run the joint continuity showing that the common first-exit time actually reaches `θr²` with all quantities inside their thresholds at once. This assembly is distinct from the individual estimates and is not present.

4. **Provenance and uniformity of the initial budget `∫_U F² ≤ M Vol(U)`, `M≃1+K₀`.** This is the sole link to the actual Yau-26 hypothesis, and it is upstream of these notes. The pinching `c_n g≤Ric≤C_n g` bounds Ricci but not the Weyl part of `Rm` in dimension 4, so `F=(1+|Rm|²)^{1/2}` is not controlled pointwise; the `L²` curvature budget must come from 4D curvature-integral / signature–Euler identities (the LeBrun `∫|W|²` mechanism). Neither the derivation of `M` from the hypothesis nor the behavior of `K₀` along the pinched/near-Einstein sequence appears here. Without it the machinery has no initial data.

5. **A quantitative tension the notes do not analyze.** Making `Γ(0)=Cr²√(1+K₀)` small forces `r ≲ (1+K₀)^{-1/4}`, hence the plateau curvature scale `r⁻² ≳ (1+K₀)^{1/2}`. The sharp bound `|aRm(t)|≤CΓ_*/t` at `t=θr²` also gives `∼√(1+K₀)/θ`. So the "bounded curvature on plateaux" is bounded only at scale `r`, and that scale grows with `K₀`. Whether a smooth limit can be extracted along the sequence depends on how `K₀` behaves as the sequence collapses/pinches — which is not addressed. This coupling between the once-fixed `r`, the budget `K₀`, and the plateau curvature scale is a concrete quantitative question that should be resolved before the terminal contradiction can be trusted.

6. **The terminal geometric contradiction** — from `|aRm|≤Cr⁻²` on `a=1` plateaux plus preserved `Q=∫_M|E|²`, via the Step 16 exponential-pullback averaging and the Step 8 Derdzinski/Einstein-germ argument — uses machinery not in the supplied files. I cannot verify it here; its inputs (plateau bounded curvature at scale `r`, triangular `Q`-preservation) are the ones produced above, but the transfer to a local Einstein-germ contradiction is asserted, not shown.

7. **A03 §5 triangular unweighted defect** `Q'_α ≤ Cr⁻²Σ_{β∼α}Q_β` (4.1/5.2) via testing by `η²E`: stated with the same `Γ_*`-smallness, but the full integration-by-parts proof is not written. `Q_support(T)≤e^{Cθ}Q_support(0)` then preserves `Q/A→0` because the metric is stationary off the support — this logic is sound provided the estimate itself is proved.

### One correctly-stated fact about reach

Even completing items 1–7 addresses only the 4-dimensional LeBrun / Ishida–LeBrun setting. The `3/2` iteration exponent, the `F⁴/|E|⁴` Sobolev structure, and the curvature-integral budget are all specific to `n=4`; nothing here transfers to other dimensions, to the opposite-sign Einstein branch, or to the full all-dimensional interval statement, and the Lean formalization is untouched. The notes state this accurately.

**Summary judgment on the four questions.** (1) Yes, the component/volume-normal distinction is correct and the `χ₀⁻⁴` growth is real. (2) Yes, the scale-invariant Whitney mean and the Sobolev product carry the right powers. (3) Yes, `Γ(t)` is a viable first-exit quantity and the cubic potential `A⁴H₃≤CΓ_*³/t` follows from the same budget with correct exponents. (4) Yes, the weights `H_q`, `v_q`, the Hölder/Sobolev/Young exponents, the `q→3q/2` iteration, and both endpoint scalings are internally exact and dimensionally correct for `n=4`. No hard algebraic error surfaced. What is not yet in hand is the full tensor derivation of the driving inequality, the existence/extension theorem for the normalized cutoff flow, the single joint continuity argument, the derivation and sequence-uniformity of the initial `L²` curvature budget (with the `K₀`–`r` plateau-scale tension), and the terminal Einstein-germ contradiction.
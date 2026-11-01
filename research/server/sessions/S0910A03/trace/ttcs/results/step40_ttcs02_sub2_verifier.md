# TTCS Independent Branch Record

```json
{
  "step_id": 40,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step40_staggered_all_order_continuation_candidate.md",
    "Sessions/S0910A03/workspace/notes/step40_m2_coupled_continuation_mechanism.md",
    "Sessions/S0910A03/workspace/notes/step38_hessian_ibp_and_conditional_moser_repair.md",
    "Sessions/S0910A03/workspace/codex_loop/work/shifted_curvature_continuation.md",
    "Sessions/S0910A01/workspace/notes/step38_continuation_repair_and_support_normalization.md",
    "Knowledge/objects/papers/Pseudolocality-of-Ricci-Flow-under-Integral-Bound-of-Curvature--ca47a7c773f9--79daf5157f68/object.md"
  ]
}
```

## Task

Verify the proposed arbitrary-order staggered energy induction in step40_staggered_all_order_continuation_candidate.md. The central question is whether, after the m=2 extra signed integration by parts, every current-order cutoff-jet/lower-U product at arbitrary m can be reduced without demanding a current unknown at a larger exponent. Check the structural equations for U_m, C_{m+1}, and T_m against Wang Section 4 and the shifted-curvature derivation. In particular: (i) classify all ways current U_m, current C_{m+1}, or derivatives U_{m+1}, C_{m+2}, T_{m+1} can appear; (ii) verify the extra IBP on chi C_{m+1} U_1 P(U_m), including commutators, for m>=3; (iii) verify the subsequent unweighted T_m energy when expanding nabla^{m+2}a honestly; (iv) check the finite exponent schedule and cutoff-jet evolution; (v) identify any missing term that defeats equations (2.9), (2.11), or (3.6). Do not accept a schematic appeal to Wang if a current-level multiplier is hidden. Give a direct mathematical verdict on the energy induction. The terminal restart/short-time existence may be treated separately.

## Output

## Verdict

The staggered energy induction is structurally sound at arbitrary order. After the extra signed integration by parts, every current-order cutoff‑jet/lower‑U product reduces to previous‑level factors (at finite exponents) plus current dissipation, and **no current unknown (U_m, C_{m+1}, or T_m) is ever demanded at an exponent above p**. Equations (2.9), (2.11), and (3.6) hold as stated, and the staggered chain (4.2) closes all three families in every finite L^p on the positive‑time slab. The one place still resting on an unexpanded assertion is the tensor content of the normalization / G lines (𝒢_m, 𝒩_m), and there ∇G=0 genuinely forces the asserted structure, so it does not conceal a current‑level multiplier. I confirmed the decisive points independently below.

## 1. The structural equations match Wang §4 shifted

Wang's Lemma 4.5 for ∇^m(χ²Rm) is
∂_t∇^m(χ²Rm)=χ²Δ∇^m(χ²Rm)+Σ_{i+j+k=m+2,k≤m+1}∇^iχ∇^jχ∇^k(χ²Rm)+Σ_{i+j+k=m,k≤m-1}∇^i(χ²)∇^j(χ²Rm)∇^kRm+χ²Rm∇^m(χ²Rm).
Replacing χ²Rm→U=aT gives (1.4) term‑for‑term, with the residual χ²Rm→U shift and the -2ag normalization collected into 𝒢_m. Since ∇G=0, the only new algebra is Ric(T)=E, Ric(U)=aE, so T_k=∇^kRm for k≥1 and T_m (m≥1) is literally the ∇^mRm energy of Wang Prop 4.13. Equation (1.5) is the corresponding unweighted Wang Lemma 4.4 shifted. These are faithful.

## 2. The decisive combinatorial fact (this is what makes the all-order induction actually complete)

The companion m=2 note hedged that "the all-order pattern has not yet been written for arbitrary distributions." That hedge is unnecessary, and the staggered note's §2 classification is in fact exhaustive. In the first sum of (1.4), α+β+γ=m+2 with a **two-cutoff-factor** product forces:

- **C_{m+2} can appear only with U_0.** α=m+2 ⇒ β=γ=0, i.e. only Γ_1=χC_{m+2}∗U.
- **C_{m+1} can appear only with U_0 or U_1.** one factor C_{m+1} ⇒ the other C_β has β=1-γ≥0 ⇒ γ∈{0,1}: γ=0 gives Γ_2=dχC_{m+1}∗U, γ=1 gives χC_{m+1}∗U_1. No χC_{m+1}∗U_2,…,U_m exists.
- The second sum Σ∇^i a∗U_j∗T_k (i≤m) and 𝒢_m contain ∇^i a with i≤m, expanding by (1.8) to cutoff order ≤ C_m only — **no C_{m+1} and no C_{m+2}** outside the first sum.

I verified this enumeration directly. It is the load-bearing point: the current top jet couples only to U-derivative ≤1, and the next jet only to U itself. Every other allocation carries cutoff order ≤ m and U-order ≤ m-1, i.e. previous-level. So there is exactly one term type (χC_{m+1}∗U_1) that resists a same-exponent bound, plus the copy of it produced by integrating Γ_1 once. No unwritten distribution remains.

## 3. The extra IBP on χ C_{m+1} U_1 P(V), including commutators (m≥3)

Writing Z=C_{m+1}=∇C_m and integrating once (2.6) gives
∫χ Z U_1 P(V) = −∫dχ C_m U_1 P(V) − ∫χ C_m U_2 P(V) − ∫χ C_m U_1 ∇P(V) + ℛ_com.
I checked each descendant:
- term 1: three factors C_m,U_1,|V|^{p-1}, Hölder (2p,2p,p/(p-1)); C_m,U_1 previous ⇒ finite.
- term 2: m=2 ⇒ U_2=V so it is the signed Hessian χC_2 B(V) (Step 38 lemma); m≥3 ⇒ C_m,U_2 both previous, Hölder (2p,2p,p/(p-1)).
- term 3: ∇P(V)~|V|^{p-2}∇V, Young ⇒ εD^U + C∫|C_m|²|U_1|²|V|^{p-2}, then Hölder with C_m,U_1∈L^{4p} and a finite-volume slack (exponent sum (p-1)/p<1). Verified.

The commutator remainder ℛ_com is exactly the reordering ∇^{m+1}χ vs ∇(∇^mχ): [∇,∇]∇^{m-1}χ = Σ_{s=0}^{m-1}∇^s Rm ∗ C_{m-1-s}. Its highest curvature factor is ∇^{m-1}Rm = T_{m-1} (using ∇G=0), **which is closed at the end of stage m−1** and available at every finite exponent. So ∫T_{m-1}U_1|V|^{p-1}≤‖T_{m-1}‖_{2p}‖U_1‖_{2p}‖V‖_p^{p-1}. I confirmed the commutator cannot raise the curvature order to T_m. Crucially, **C_{m+1} is entirely removed** by this IBP; after it, C_{m+1} survives only in the exponent-p couplings |Z|²|V|^{p-2} (from ∇P(V)·χ Z U in Γ_1) and |Z||V|^{p-1} (Γ_2), both closing by Young at exponent p. This matches Wang Prop 4.14's actual mechanism: Wang's Γ_3 = χ∇^{m+1}χ∗∇(χ²Rm) is the identical term, and "control as Γ_4" there is precisely this second integration.

## 4. The T_m step with ∇^{m+2}a expanded fully

∇^{m+2}a = 2χ C_{m+2} + Σ_{s=1}^{m+1} C_s C_{m+2-s}. The middle sum has cutoff order ≤ C_{m+1}, **now known from the current-pair step** — this is the payoff of ordering the pair before T_m. Only 2χC_{m+2}∗T survives; (3.3) integrates the derivative off C_{m+2} onto C_{m+1} (known), giving: dχC_{m+1}T P(X) (finite product), χC_{m+1}T_1 P(X) (m=1: signed Hessian; m≥2: T_1 previous), and χC_{m+1}T ∇P(X) → εD^T + C∫|C_{m+1}|²|T|²|X|^{p-2} with C_{m+1},T∈L^{4p}. I checked that the r=m+1 allocation ∇^{m+1}a∗T_1 also uses only C_{m+1}(known)×T_1(previous), no IBP needed. ∇a∗T_{m+1} is absorbed by D^T; ∇²a∗T_m splits into signed Hessian χC_2 X plus bounded dχ²X. Connection-variation in the T_m equation produces at most U_m∗T_0 (m−1 connection insertions, ∂_tΓ~U_1 ⇒ ∇^{m-1}(∂_tΓ)~U_m), with U_m known from the pair; not U_{m+1}. Quadratic terms with current X carry coefficient aT=U (|U|≤K). So (3.6) holds.

## 5. Finite exponent schedule and cutoff-jet evolution

At the pair step the current unknowns V=U_m, Z=C_{m+1} enter only through |Z|²|V|^{p-2} and |Z||V|^{p-1} (both L^p), while previous levels are used at Np/4p (finite, since (1.7) supplies all finite q at earlier levels). The apparent χZU_1 route is removed by §3. So the ascent p→2p on a current unknown never occurs — it is a finite triangular induction, exactly as (4.1)–(4.2) states.

For the cutoff jet, the connection-variation sum ∂_t C_{m+1}=Σ_{r=0}^{m-1}∇^r(∂_tΓ)∗C_{m-r} peaks at ∇^{m-1}(∂_tΓ)∗C_1 ~ U_m∗C_1 = V×bounded, **not** U_{m+1}: the first derivative of a scalar carries no connection, so there are m (not m+1) connection insertions. This is the shifted Wang Lemma 4.6, and it gives d/dt‖Z‖_p^p ≤ C(1+‖V‖_p^p+‖Z‖_p^p) with V at exponent p. Summing with (2.9) and dropping the coercive D closes the pair by Gronwall. Verified.

One notational point: the "U_0∗C_{m+1}" term listed in (2.10) is not a connection-variation output (which produces U_1∗C_m,…,U_m∗C_1); it is the metric/measure variation ∂_t g^{-1}~aE~U contracting |C_{m+1}|² in d/dt∫|Z|^p, giving the K‖Z‖_p^p term. It is harmless and correctly lands on the right side, but it is mislabeled as a connection term.

## 6. The single asserted-but-unwritten piece

The only step still resting on assertion rather than displayed algebra is the exact tensor content of 𝒢_m/𝒩_m (normalization -2ag and the G-shift) — the S0910A01 Step 38 note also records that "every tensor contraction in (1.2)… every normalization/G lower term" is not yet expanded. My independent check supports the assertion: aG has ∇^i(aG)=(∇^i a)∗G (parallel G), so every derivative of the G-shift is a cutoff-jet times parallel G, contributing no curvature derivative and no U-derivative above the main terms; likewise ∇^i(ag)=(∇^i a)∗g. Hence these lines cannot raise the U- or T-derivative order or introduce a cutoff jet above C_{m+2}. This is why the schematic step here is not a hidden current-level multiplier. A fully written expansion would remove the last non-displayed link, but nothing in the algebra points to a defeating term.

## 7. What is verified vs. what remains outside this energy question

The energy induction — pair (U_m,C_{m+1}) then T_m, at arbitrary m — is correct: (2.9),(2.11),(3.6) hold and the staggered chain gives finite L^p for all three families on [τ,T_*). I found no term defeating them. Items I could not directly inspect: `verify_shifted_curvature.py` (referenced as checking the convention-sensitive contractions), and the full 𝒢_m/𝒩_m expansion (asserted, and supported by ∇G=0). The terminal restart / transported-coefficient short-time construction in §5 (5.3) is a separate matter and was not part of this verification.

Two substantive strengthenings the notes could record, since they are true and remove residual hedging: (a) the §2 classification is exhaustive — the two-cutoff-factor structure of ∇^{m+2}(χ²) limits current-jet couplings to U-derivative ≤ 1, so there is no "arbitrary distribution" left to handle; (b) the commutator remainder's highest curvature factor is exactly T_{m-1}, which the staggered order guarantees is in hand before the pair step of stage m.
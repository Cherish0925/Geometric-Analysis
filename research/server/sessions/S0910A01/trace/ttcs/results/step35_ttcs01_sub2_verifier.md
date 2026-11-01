# TTCS Independent Branch Record

```json
{
  "step_id": 35,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step35_tensor_variation_and_hessian_a.md",
    "Sessions/S0910A01/workspace/scripts/step35_tensor_hessian_verification.py",
    "Sessions/S0910A03/workspace/notes/step35_unregularized_J6_persistence_lemma.md",
    "Sessions/S0910A01/workspace/notes/step34_integrated_potential_q3_and_defect.md"
  ]
}
```

## Task

Verify the index-level derivation of the two Hessian-a contraction tensors for the normalized cutoff flow dt g = -2a(Ric+g) on a 4-manifold. Specifically check:

1. CURVATURE TENSOR: Starting from the standard all-lower Riemann variation formula dt R_{ijkl} = g_{lp}[nabla_j(delta Gamma^p_{ik}) - nabla_i(delta Gamma^p_{jk})] + R_{ijk}^p h_{lp}, with h = -2aE and E = Ric+g, the Hessian-a terms in dt|Rm|^2 give Sigma_H = 8 A_{pq} B^{pq}_curv where B^{pq}_curv = R^p_j^q_l E^{jl}. Verify the pair-symmetry and antisymmetry reductions that eliminate two of the four terms and double the remaining two. Check the derivative structure |nabla B_curv| <= CF|nabla Rm| from the explicit product rule. Does this correctly use |nabla E| = |nabla Ric| <= C|nabla Rm|?

2. DEFECT TENSOR: Starting from the Besse Theorem 1.174 Ricci linearization 2(DRic)[h]_{ij} = g^{kl}(-nabla_k nabla_l h_{ij} + nabla_k nabla_i h_{jl} + nabla_k nabla_j h_{il} - nabla_i nabla_j h_{kl}) + curvature terms, extract the Hessian-a part of dt E_{ij} and show the contribution to dt|E|^2 is Sigma_H^E = 2 A_{pq} B^{pq}_def where B_def = s g^{pq} + tau E^{pq} - 2(E^2)^{pq}. Verify this matches A03's formula (which has 2*B_def due to test function convention).

3. NORMALIZATION CANCELLATION: Verify that the +g in E = Ric+g produces no additional quadratic curvature term in the algebraic/lowering variation, only the normalization lowering -2aR_{ijkl}, because R_{ijkl} - R_{ijkl} = 0 from the skew symmetry R_{ijlk} = -R_{ijkl}.

4. DISSIPATION: Verify the pre-absorption dissipation is -pD_p^Rm - p(p-2)D_p^F, not -p(p-3)D_p^F.

## Output

# Verification Memo: Hessian-a Contraction Tensors for ∂_t g = −2a(Ric+g), n=4

I reworked all four requested derivations from first principles (independent index calculation, not a reading of the notes' own algebra). All four central identities are correct. Two small imprecisions in the surrounding text are worth recording because they touch the derivative-structure bound; neither disturbs the final estimates. Details below.

## 1. Curvature tensor Σ_H = 8 A_pq B_curv^pq — confirmed

Extracting the Hessian-a part of (2.1) directly: with h_{k β}=−2aE_{k β}, the double covariant derivative retains, in its ∇²a piece, only −2A_{μν}E_{k β}. Feeding this through δΓ and lowering with g_{lα}, I get

- g_{lα}∇_j δΓ^α_{ik}|_{∇²a} = −A_{ji}E_{kl} − A_{jk}E_{il} + A_{jl}E_{ik},
- subtracting the i↔j version, the symmetric A_{ij}E_{kl} pieces cancel (A_{ji}=A_{ij}),

giving exactly (2.7):
(H_a)_{ijkl} = −A_{jk}E_{il} − A_{il}E_{jk} + A_{ik}E_{jl} + A_{jl}E_{ik}. The lowering term R_{ijk}^α h_{αl} contributes no ∇²a part because h is undifferentiated. This matches the note.

The two symmetry reductions are correct:
- **Pair symmetry** R^{ijkl}=R^{klij} with relabel i↔k, j↔l sends term 2 → term 1; the relabel i↔j, k↔l (under which R^{ijkl}→R^{jilk}=R^{ijkl}) sends term 4 → term 3. Hence Σ_H = 4R^{ijkl}(A_{ik}E_{jl} − A_{jk}E_{il}), i.e. (3.2). (Note: the "same relabel" phrasing in §3.1 for terms 3–4 is loose — the working relabel is i↔j, k↔l, not i↔k, j↔l — but the conclusion terms 3=4 is right.)
- **First-pair antisymmetry** R^{ijkl}=−R^{jikl}, relabel i↔j, gives R^{ijkl}A_{jk}E_{il} = −R^{ijkl}A_{ik}E_{jl}, so the bracket contracts to 2R^{ijkl}A_{ik}E_{jl}. Therefore Σ_H = 8R^{ijkl}A_{ik}E_{jl} = 8A_{pq}B_curv^{pq}, B_curv^{pq}=R^p{}_j{}^q{}_l E^{jl}. Confirmed (3.3).

**Prefactor 2 is right:** only ∂_t R_{ijkl} carries the ∇²a part; the four inverse-metric variations of |Rm|² depend on h=−2aE with no ∇²a. So the Hessian-a contribution to ∂_t|Rm|² is precisely 2R^{ijkl}(H_a)_{ijkl}.

**Derivative structure |∇B_curv| ≤ CF|∇Rm|:** B_curv is an algebraic contraction of Rm and E, so ∇B_curv = (∇Rm)E + Rm(∇E). With |E| ≤ CF (since |Ric| ≤ C|Rm| ≤ CF and F ≥ 1) and |Rm| ≤ F, this gives CF|∇Rm| **provided** |∇E| ≤ C|∇Rm|. That input is valid and used correctly: E = Ric + g, ∇g = 0, so ∇E = ∇Ric, and ∇Ric = g^{kl}∇R_{kilj} is a trace of ∇Rm, hence |∇Ric| ≤ C(n)|∇Rm|. This is the correct (Ricci-controlled-by-Riemann) direction. The signed IBP route (iv) then genuinely produces D_p^Rm (not merely D_p^F), which I checked closes under Young: |∇a|a^{p−2}F^{p−1}|∇Rm| → ε a^{p−1}F^{p−2}|∇Rm|² + C_ε(|∇a|²/a)a^{p−2}F^p, and |∇a|²/a = 4|∇χ|² ≤ Cr^{−2}. Correct.

## 2. Defect tensor B_def = s g^pq + τ E^pq − 2(E²)^pq — confirmed

From the Besse 1.174 form, the ∇²a part of each of the four second-derivative terms (with h=−2aE, ∇²h|_{∇²a}=−2A E):

1. −g^{kl}∇_k∇_l h_{ij} → +2(Δa)E_{ij}
2. +g^{kl}∇_k∇_i h_{jl} → −2A^l{}_i E_{jl}
3. +g^{kl}∇_k∇_j h_{il} → −2A^l{}_j E_{il}
4. −g^{kl}∇_i∇_j h_{kl} → +2A_{ij}τ, τ=g^{kl}E_{kl}

Dividing 2∂_tR_{ij} by 2 reproduces (5.2), and ∂_tg=−2aE adds nothing in ∇²a, so (5.3) holds. Contracting Σ_H^E = 2E^{ij}(∂_tE_{ij})|_{∇²a}: the four pieces give 2(Δa)s, −2A_{il}(E²)^{il}, −2A_{il}(E²)^{il}, +2τ⟨A,E⟩, summing to 2A_{pq}[s g^{pq} + τE^{pq} − 2(E²)^{pq}]. Confirmed (5.5), including the E=0 vanishing (every term is O(E²)) and |B_def| ≤ Cs.

**A03 match:** A03's B^{ij}=2g^{ij}|E|²+2τE^{ij}−4E^{ik}E_k{}^j = 2B_def^{ij}. The factor 2 is exactly the test-function convention (q=3η²a⁴s² gives 3s²·Σ_H^E = 3s²·2A_{pq}B_def, absorbed as A_{ij}B^{ij}(q) with B^{ij}(q)=q·2B_def). Consistent.

**One imprecision in the derivative bound (6.4).** All four terms of ∇B_def are individually O(s^{1/2}|∇E|):
- (∇s)g: |∇s| ≤ 2|E||∇E| = O(s^{1/2}|∇E|);
- (∇τ)E: |∇τ| = |g^{ij}∇E_{ij}| ≤ C|∇E| (direct trace of ∇E), times |E|=s^{1/2};
- τ∇E: |τ| = |tr E| ≤ √n·|E| = √n s^{1/2} always, so O(s^{1/2}|∇E|);
- ∇(E²): O(|E||∇E|) = O(s^{1/2}|∇E|).

Hence the correct, clean bound is |∇B_def| ≤ Cs^{1/2}|∇E|, exactly as stated in the §7.2 summary and script check D4. The line inside (6.4) that writes "≤ Cs^{1/2}|∇E| + C|∇E|" adds a spurious s⁰ term, and its justification chain "|∇τ|=|∇R| ≤ C|∇Rm| ≤ C|∇E|+C" runs through the wrong-direction inequality |∇Rm| ≤ C|∇E| (full Riemann is not controlled by Ricci) and is unnecessary. The direct trace estimate |∇τ| ≤ C|∇E| makes the τ-terms clean without any additive constant. This does not change the IBP: route (iv) in §6.4 uses s²·s^{1/2}|∇E| = s^{5/2}|∇E| and Young → εX_6 + C_ε r^{−2}J_6, which the clean bound supports directly. I recommend replacing (6.4)'s bound by the single term Cs^{1/2}|∇E| — it is both correct and stronger, and it removes the incorrect intermediate step.

## 3. Normalization cancellation — confirmed, plus independent scaling confirmation

Two distinct effects of the +g in E:

- **Lowering variation:** R_{ijk}^α h_{αl} = −2a R_{ijk}^α(R_{αl}+g_{αl}) = −2a(R_{ijk}^α R_{αl} + R_{ijkl}). The +g part is −2aR_{ijkl}. Correct.
- **Algebraic k,l-index pieces:** the combination R_{ijkp}E_l^p + R_{ijlp}E_k^p, with E_l^p=R_l^p+δ_l^p, gives δ-parts R_{ijkl} + R_{ijlk} = R_{ijkl} − R_{ijkl} = 0 by the last-pair skew symmetry R_{ijlk} = −R_{ijkl}. So no extra Rm∗Rm term from +g here. Correct.

This is genuinely airtight for the stated combination. The §2.3 "commutator terms" presentation is schematic, but the global bookkeeping is pinned down independently and exactly by the pure-scaling solution g(t)=e^{−2t}g₀: Γ fixed ⇒ ∂_tR_{ijkl} = −2R_{ijkl}; four inverse metrics each scale +2 ⇒ ∂_t|Rm|² = −4|Rm|² + 8|Rm|² = +4|Rm|²; d μ scales −4 in n=4 ⇒ ∫|Rm|²dμ invariant. This exact-solution check (§1, script S1/S2/NC3) is the strongest evidence that the normalization coefficients (−4 from lowering, +8 from metric variation, net +4a|Rm|²) are correctly assigned, and it confirms the note's insistence that the +4a|Rm|² normalization term be carried inside the CaF³ reaction rather than treated as pointwise damping.

## 4. Dissipation −pD_p^Rm − p(p−2)D_p^F — confirmed

Testing with (p/2)η²a^{p−2}F^{p−2}:
- Explicit Bochner −2a|∇Rm|²: → −p·η²a^{p−1}F^{p−2}|∇Rm|² = −pD_p^Rm.
- Diffusion aΔ(F²) by parts: −(p/2)∫⟨∇(η²a^{p−1}F^{p−2}), 2F∇F⟩. The ∇ landing on F^{p−2}=(p−2)F^{p−3}∇F gives −p(p−2)∫η²a^{p−1}F^{p−2}|∇F|² = −p(p−2)D_p^F. The ∇a cross terms are Young-absorbed (εD_p^F + Cr^{−2}K_p); the ∇η term vanishes on the collar.

So the coercive quadratic is −pD_p^Rm − p(p−2)D_p^F. At p=2, F^{p−2}=1 has no gradient, so the radial term is absent — consistent with the script's Dp2 note. The earlier −p(p−3)D_p^F differs by exactly +pD_p^F, i.e. a spuriously reintroduced radial dissipation; at p=3 it wrongly gave 0 whereas the correct −p(p−2) retains −3D_3^F. The corrected form is the one that matches the standard IBP. Confirmed. (Ancillary: |∇F| ≤ |∇Rm| since F∇F=⟨Rm,∇Rm⟩ and |Rm| ≤ F, so D_p^F ≤ D_p^Rm — both dissipations are genuine and sign-definite.)

## Additional consistency points I checked

- **Three-factor Hölder (2.12):** a-exponents 1/3+(p−2)/3+2(p−1)/3 = p−1; F-exponents 1+p/3+2p/3 = p+1. Exact. The §4.2 (z_p²)^{2/3} and (2.12) z_p^{4/3} are the same object.
- **Two-factor defect Hölder:** w_6²=η²a⁵s³, Fw_6²=η²a⁵Fs³=P_6, Hölder (2,4,4) ⇒ P_6 ≤ ‖F‖₂‖w_6‖₄². The third gradient term of w_6 gives ≤ 9X_6 via |∇s|² ≤ 4s|∇E|². Correct, and the absorption parameter γ = 𝒮K_2^{1/2} = Cr²√K_0 is volume-cancelled as claimed.
- **The s^{3/2} vs s^{5/2} slip:** A03's displayed (3.6a) shows s^{3/2}; the term (∇a)·∇E·E tested with 3η²a⁴s² is η²a⁴|∇a|s^{5/2}|∇E| — power 5/2. A01's §5 already records this as a typo; the Young step (→ εX_6 + Cr^{−2}J_6) uses 5/2 and is unaffected. Worth fixing in the A03 display for internal consistency with its own (3.4a).
- **Sign convention of (2.1):** the ordering ∇_j δΓ_{ik} − ∇_i δΓ_{jk} is one admissible convention (a global sign relative to some texts). It is applied consistently and, since the Hessian-a term is bounded in absolute value after IBP, the overall sign does not enter the absorption estimates.

## What these identities reach and what they do not

The four computations are correct tensor-algebra facts about the linearization of Rm and Ric under h=−2aE, together with the induced power inequalities (2.14) and (5.14/6.2). They establish the index-level content that Step 34 had carried as a premise (the derivative structure (2.10), the Hessian contraction (5.8), the corrected radial coefficient). That closes exactly the two obligations §7.1–7.2 name.

They do **not** by themselves advance the pinch-to-Einstein statement of Problem 26, and the notes are explicit about this. The remaining mathematical substance — degenerate-flow short-time existence and continuation with coupled cutoff jets, simultaneous first-exit closure carrying 𝒮(t), K_2^η(t), J_6(t) and the moving metric/support comparability, terminal bounded-curvature plateaux, and the terminal calibration/exponential-pullback selection feeding the Derdziński forbidden-germ argument — is where the actual geometric content of even the Ishida–LeBrun four-dimensional model sits, and none of it is touched by these identities. In particular the whole construction presumes a smooth solution of the degenerate flow ∂_tg=−2aE on a provisional first-exit interval; the identities are statements about that solution's derivatives, not a proof it exists or persists. So the correct reading is: these are sound, reusable computational building blocks for one flow-based route on one four-dimensional family, verified at the level requested, with the geometric closure entirely ahead.

One concrete item to resolve next if this route is pursued: the first-exit argument needs the moving-Sobolev/metric-comparability premise 𝒮(t) ≤ 2𝒮(0) to be produced by the very drift estimate (6.3–6.4) it feeds, so the logical order of that self-improvement (which quantity bootstraps which) should be written out as an actual coupled inequality rather than assumed provisionally — that coupling, not the tensor algebra, is where the present chain is still open.
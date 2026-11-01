# TTCS Independent Branch Record

```json
{
  "step_id": 34,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step34_integrated_potential_q3_and_defect.md",
    "Sessions/S0910A01/workspace/scripts/step34_integrated_potential_q3_verify.py",
    "Sessions/S0910A01/workspace/notes/step33_curvature_power_inequality.md",
    "Sessions/S0910A01/workspace/notes/step25_tensor_energy_derivation.md",
    "Sessions/S0910A03/workspace/notes/step34_restored_weighted_flow_state_and_exact_obligations.md"
  ]
}
```

## Task

Verify the Step 34 corrected fixed-exponent analytic layer for the selected-support normalized cutoff flow in the Yau-26 restricted 4D negative route. Read the new note and script, plus the prior Step 33 power note and Step 25 q=2 derivation as background. Focus on scientific correctness: (i) the all-lower curvature convention and pure scaling test; (ii) the corrected diffusion dissipation -p D_Rm - p(p-2) D_F before cutoff absorption; (iii) the volume-form term being controlled by the curvature reaction via |s+4|<=CF rather than C delta K_p; (iv) the integrated-potential bound B(t)<=C gamma^3 from q=2 and its use to obtain q=3 same-support propagation by good-slice + Gronwall without circularity; (v) the regularized defect derivation from Ricci variation and whether the no-additive-source conclusion is justified at the stated level. Identify any mathematical faults or missing assumptions that would invalidate these fixed-exponent consequences, and distinguish them from the later unproved moving-Sobolev/cutoff-jet continuation obligations.

## Output

# Verification Memo — Step 34 Fixed-Exponent Analytic Layer (S0910A01)

## Summary judgment

I reproduced the five requested pieces by hand and independently. At the fixed-exponent level they are mathematically correct, and Step 34 genuinely repairs two errors carried in Step 33 (the diffusion dissipation coefficient and the volume-form treatment). I found no fault that invalidates the fixed-exponent consequences B(t)≤Cγ³, the good-slice q=3 propagation, or the J₆ persistence. The one structural over-inclusion I found (an aE\*E term in the defect equation) does not affect the no-additive-source conclusion. What remains genuinely open is the coupled first-exit closure of the moving Sobolev constant and the higher-order cutoff-jet control for the Moser endpoint; these are correctly separated from the fixed-exponent seeds and are not defects in this note.

---

## (i) All-lower curvature convention and pure scaling test — correct

Under ∂ₜg = −2g, g(t)=e^{−2t}g₀, the Christoffel symbols are unchanged, so the (1,3) tensor R_{ijk}{}^l is time-fixed and the all-lower R_{ijkl}=g_{lα}R_{ijk}{}^α scales as e^{−2t}. Then

- |R|² = g^{ia}g^{jb}g^{kc}g^{ld}R R scales as (e^{2t})⁴·(e^{−2t})² = e^{4t}, giving ∂ₜ|R|² = 4|R|²;
- in dimension four dμ scales as e^{−4t}, so ∂ₜ(|R|²dμ)=0, and ∂ₜ(F²dμ)=−4dμ for F²=1+|R|².

This matches (1.4) and the note's statement that the conformal part is a weighted lower-order source, not a pointwise damping of |R|². The script's `norm_sq_log_derivative = 2·(−2)+4·2 = 4` and `integral = 0` encode this correctly. The equation (1.2) is an upper inequality whose principal diffusion −2a|∇Rm|² is the standard Bochner coefficient carried by the cutoff weight a; the scaling test is a bookkeeping consistency check on the conformal/reaction terms, and it passes.

## (ii) Corrected diffusion dissipation −pD_p^{Rm} − p(p−2)D_p^F — correct, and a real repair

Testing aΔF² by (p/2)a^{p−2}F^{p−2} with ΔF²=2FΔF+2|∇F|², then integrating by parts on ∫a^{p−1}F^{p−1}ΔF:

- the +2|∇F|² piece gives +pD_p^F;
- the IBP gives −p(p−1)D_p^F − p(p−1)∫a^{p−2}F^{p−1}∇a·∇F;
- sum from aΔF²: **−p(p−2)D_p^F** − p(p−1)(cross term).

The explicit −2a|∇Rm|² gives **−pD_p^{Rm}** directly. Total −pD_p^{Rm}−p(p−2)D_p^F, exactly (2.5). I confirm this fixes a genuine Step 33 error: Step 33 (3.1) carries −p(p−3)D_p^F, i.e. an extra +pD_p^F introduced by routing the −2a|∇Rm|² through a spurious "Kato term" −p(D_p^{Rm}−D_p^F). Step 34 avoids Kato entirely and does not double-count. The correction is not cosmetic: at p=3, Step 33's coefficient p(p−3)=0 leaves no radial dissipation to absorb the p(p−1) cross term (2.6), whereas Step 34's p(p−2)=3>0 does. This matters for the deferred Moser iteration; it does not change the p=3 forward inequality (2.15), which drops dissipation and is therefore identical either way.

The script's §2 check is self-referential (it asserts −p(p−2)=−p(p−2)); the mathematical content rests on the note's IBP, which I verified.

## (iii) Volume-form term via |s+4|≤CF, not CδK_p — correct and conceptually important

In dimension four tr E = s+4, ∂ₜdμ = −a(s+4)dμ, so the volume contribution to K_p′ is −∫a^{p−1}(s+4)F^p, bounded in absolute value by C∫a^{p−1}F^{p+1} = the same reaction R_p as (2.10) since |s+4|≤√n|E|≤CF. Step 33's (2.V) instead wrote |∫a^{p−1}(s+4)F^p|≤CδK_p, which silently assumes pointwise smallness |E|≲δ available only after the smoothing is established — circular. Step 34's placement of the volume term inside the F^{p+1} reaction is correct and removes that hidden input.

The three-factor absorption is sound. I verified the identity a^{p−1}F^{p+1}=(aF³)^{1/3}(a^{p−2}F^p)^{1/3}z_p^{4/3} (a-exponent (1+(p−2)+2(p−1))/3=p−1, F-exponent 1+(p/3)+(2p/3)=p+1), and the Young split: writing ‖z_p‖₄^{4/3}≤(S·𝒢)^{2/3} and grouping (S^{2/3}M)·𝒢^{2/3}≤ε𝒢+C_εS²M³ with M³=Y·K_p yields exactly the coefficient **S²Y** in (2.13). The single-Sobolev-factor S² (not S⁴) is consistent with the A03 §1.1 correction of Step 33's spurious extra factor. The elimination of the additive C₀p source in Step 33 (3.1) is also justified: lower F-powers from the "1" in F²=1+|Rm|² satisfy ∫a^{p−2}·1≤∫a^{p−2}F^p=K_p, so they are multiplicative in K_p, not a constant. This multiplicative form is what makes the later Gronwall clean.

## (iv) Integrated potential B(t)≤Cγ³ and non-circular q=3 propagation — correct

I reproduced the chain:

- Interpolation (3.2): Y=∫aF³≤‖F‖₂‖a^{1/2}F‖₄²≤CSK₂^{1/2}(D₂+r^{−2}K₂) via Hölder(2,4,4) with ‖F‖₂²=K₂ and the Sobolev estimate for χF. Correct.
- On {S(t)≤2S(0), K₂(t)≤2K₂(0)}, SK₂^{1/2}≤Cγ; substituting into (3.1) and choosing Cγ<c/2 gives K₂′+(c/2)D₂≤C′r^{−2}K₂, hence sup K₂+∫D₂≤CK₂(0). For θ small this also self-closes K₂(t)≤2K₂(0).
- ∫₀ᵗY≤Cγ∫(D₂+r^{−2}K₂)≤CγK₂(0) (3.4); then B(t)≤(2S(0))²∫Y≤Cγ·S(0)²K₂(0)=Cγ³ since γ²=S(0)²K₂(0). Correct.

The non-circularity is genuine: **B is derived from the q=2 estimate alone and uses no pointwise Y bound.** The good-slice τ∈[t/4,t/2] with Y(τ)≤(4/t)∫Y≤CγK₂(0)/t, followed by integrating (2.15) with exp(C∫(r^{−2}+1)+C∫S²Y) and ∫S²Y≤B(t)≤Cγ³, gives Y(t)≤CγK₂(0)/t and S²Y≤Cγ³/t (4.4). The integrating-factor coefficient is controlled by the q=2 quantity B, not by Y itself, so the Gronwall closes without circularity. The pointwise 1/t is an output on positive dyadic slabs, not an input at t=0. Script §5–§7 confirm the γ volume cancellation (γ=r²√K₀, collapse-independent) and the Gronwall form; the numeric constants there are placeholders, so the PASS demonstrates the algebraic form, not the true universal constant.

## (v) Regularized defect from Ricci variation and no additive source — justified, with one harmless over-inclusion

The structural point is correct. ∂ₜRic = DRic_g(∂ₜg) is the linearization applied to h=−2aE, hence homogeneous in aE (and its derivatives). The contracted Bianchi identity ∇^iR_{ij}=½∇_js converts the ∇²(tr h) and div h terms so that the principal part is the elliptic Lichnerowicz operator, matching the standard Ricci-flow identity ∂ₜRic=Δ_LRic; the a-cutoff and +g normalization leave residual ∇a\*∇E, ∇²a\*E, and linear aE terms, exactly (5.2). Because the operator is a differential expression in aE, ∂ₜE vanishes wherever E≡0 on a neighborhood — there is no curvature-only source term. This is the mechanism that makes the defect inequality (5.11) purely multiplicative.

One point to record precisely: the exact instantaneous linearization is linear in E, so the aE\*E quadratic term written in (5.2) is an over-inclusion. It is harmless because |aE\*E|≤Ca|E|²≤CaF|E|², dominated by the same reaction ∫a^{p−1}Ff_ε^p (5.8) that already carries the Rm\*(aE) term. The no-additive-source conclusion is therefore unaffected. The three-factor identity for the defect (5.9) checks out (F-exponent 1, f_ε-exponent p, a-exponent p−1), giving coefficient S²Y again, so the SAME potential B controls both curvature and defect. Consequently J₆(t)≤J₆(0)exp(C∫(r^{−2}+1+S²Y))≤C(θ,γ)J₆(0), with ∫S²Y≤B≤Cγ³ integrable from zero — the key improvement over bounding the reaction by the nonintegrable ‖aF‖_∞~γ/t. The ε-regularization introduces no source because Δ|E|²=Δf_ε² (ε constant), and |∇f_ε|≤|∇E|, |E|≤f_ε make the cross and Hessian terms uniform in ε. Correct.

## Signed Hessian IBP (Route B) — resolves the fixed-p cutoff-Hessian issue

The §2.1 tensor IBP integrates the actual tensor ∇_i∇_j a (not the invalid |∇²a|), moving one derivative onto a^{p−2}, F^{p−2}, and B^{ij}(Rm). The results are paid by r^{−2}K_p, D_p^F, and D_p^{Rm} respectively, using only |∇a|≤Cr^{−1} (controlled by bilipschitz equivalence, since |∇a|²=g^{ij}∂_ia∂_ja). This genuinely avoids the evolving pointwise |∇²_{g(t)}a| bound, which bilipschitz equivalence does not supply (A03 §6). So at the fixed-p energy level (2.14),(5.11), the cutoff-Hessian obstruction is removed; the cutoff-jet induction (∇²U,∇³χ, etc.) is needed only for the higher-order continuation feeding the Moser endpoint, which is a separate later item.

---

## Load-bearing assumptions to keep visible (distinct from faults)

These do not invalidate the fixed-exponent module but determine the interval on which it holds:

1. **Moving Sobolev first exit S(t)≤2S(0).** The K₂≤2K₂(0) part self-closes from (3.1)+(3.2). The S≤2S(0) part does not: S depends on the evolving geometry, and its control requires the metric-drift bound (4.8)–(4.9), which requires J₆ persistence, which uses B≤Cγ³, which uses S≤2S(0). This is a coupled bootstrap, correctly named the "central open loop" in A03 §5. The fixed-exponent consequences are valid on the maximal interval where the provisional S bound holds; closing that interval is the substantive remaining work.

2. **Smooth existence and metric comparability ½g₀≤g(t)≤2g₀ on [0,θr²]** for the degenerate quasilinear flow ∂ₜg=−2a(Ric+g) (degenerate where a=0, normalized Ricci flow on {a=1}). Assumed in Step 25 §6; not established here.

3. **Higher-order cutoff-jet base pair (∇U,∇²χ) and its evolution (6.7)** — required for the high-p Moser endpoint (4.5),(4.8), not for the fixed-p seeds. Correctly deferred.

4. **Coverage.** As the note states, even full closure of these items addresses only the selected Ishida–LeBrun negative four-dimensional configuration, not the positive branch, general four-manifold topology, n≥5, or the full Problem 26.

## Nature of the script

The script verifies (a) scaling exponents, (b) the three-factor Hölder exponents, (c) the γ and endpoint volume cancellations — all genuine algebra that I confirm — and (d) the Gronwall/integrated-potential form with placeholder constants (illustrative). The diffusion-coefficient check in §2 is tautological. §10 explicitly records the unproved PDE premises rather than asserting them. The all-PASS result therefore supports the algebra and scaling of the fixed-exponent mechanism, conditional on the separately established tensor PDE and moving-geometry inputs, which is exactly what the note states.

## Net

Items (i)–(v) are correct at the stated conditional level; Step 34 repairs the Step 33 dissipation coefficient (−p(p−2) vs −p(p−3)) and the volume-form treatment (F^{p+1} reaction vs CδK_p), and the S²Y coefficient, the B≤Cγ³ integrated potential, the non-circular good-slice q=3 propagation, and the ε-uniform homogeneous defect inequality all check out. The only within-module imprecision is the harmless aE\*E over-inclusion in (5.2). Everything that could invalidate the endpoint program lives in the coupled moving-Sobolev first-exit closure, smooth existence/comparability, and higher-order cutoff jets — which the note separates from the fixed-exponent seeds correctly.
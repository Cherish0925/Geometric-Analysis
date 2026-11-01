# TTCS Independent Branch Record

```json
{
  "step_id": 33,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step33_curvature_power_inequality.md",
    "Sessions/S0910A01/workspace/notes/step32_nested_moser_and_tensor_audit.md",
    "Sessions/S0910A03/workspace/notes/step34_restored_weighted_flow_state_and_exact_obligations.md",
    "Sessions/S0910A01/workspace/scripts/step33_curvature_power_verification.py"
  ]
}
```

## Task

Verify two specific mathematical claims in the curvature power inequality for the degenerate cutoff flow d_t g = -2 chi^2(Ric+g).

**Claim 1 (Hessian IBP structure):** In the general-p energy inequality, the Hessian-of-a term contributes to d/dt K_p as C*p*integral(a^{p-2}|nabla^2 a|F^p). If one bounds the tensor contraction pointwise BEFORE testing (replacing <Rm, nabla^2 a*(Rm+I)> by |nabla^2 a|*F^2), then the IBP reduces nabla^2 a to nabla a and the derivative hits only a^{p-2}F^p, producing (p-2)a^{p-3}|nabla a|^2 F^p and p*a^{p-2}F^{p-1}|nabla F|. Neither term involves nabla Rm directly; the full-tensor dissipation D_p^Rm is NOT consumed by this specific IBP step. Check: is this correct? Is there a hidden subtlety where the pointwise bound before testing loses essential cancellation or introduces an error? Compare with the alternative of keeping the tensor contraction and IBP-ing that.

**Claim 2 (J_6 persistence by bounded Gronwall):** The defect power inequality has Gronwall coefficient Lambda(t) = C*p^N*(r^{-2} + 1 + S^2*Y(t)). The positive-time curvature seed gives S^2*Y(t) <= gamma^3/t for t > 0, with gamma = S*K_2(0)^{1/2} <= C*r^2*sqrt(K_0). The integral from 0 to T of S^2*Y(s) ds is FINITE despite the 1/t singularity because: (a) Y(0) is finite for smooth initial data, (b) S^2*Y(0) <= C*gamma^3, (c) the integrated Gronwall is gamma^3*(1 + |log(T/t_0)|) + ... which is bounded for fixed r, theta. Therefore J_6(T) <= J_6(0)*exp(C_Lambda) with C_Lambda sequence-uniform. This avoids using the pointwise curvature bound ||aF|| <= C*gamma/t (whose singularity is nonintegrable at t=0). Check: is this argument mathematically correct? Specifically, does the smoothness of initial data justify replacing the 1/t bound by the finite initial value near t=0? Is there a gap in the transition from the initial-time regime (Y bounded) to the positive-time regime (Y <= gamma*K_2/t)?

## Output

## Verifier memo — two assertions in the curvature/defect power inequality for ∂ₜg = −2χ²(Ric+g)

I checked the algebra of the enumerated derivation (Step 33 §§2.1–2.7, §4) directly, reconstructed both integrations by parts, and tested the two assertions against explicit constructions. The two conclusions are essentially correct, but each rests on a step that is written more loosely than the underlying mathematics allows, and in each case the rigorous route is different from the one presented. I also found one exponent label that is wrong as printed. Details below.

---

### Statement 1 — the Hessian-of-a term and whether it consumes Dₚ^Rm

**What is genuinely correct.** The Bochner+Kato accounting is right. I reproduced §2.1: with ψ=a^{p−2},
B = −p(p−2)Dₚ^F − p(p−1)Iₐ^{∇F}, and Kato gives −p(Dₚ^Rm−Dₚ^F), so the net is −pDₚ^Rm − p(p−3)Dₚ^F − p(p−1)Iₐ^{∇F}, matching (2.3), and both dissipation coefficients are ≥0 for p≥3. This part is sound.

**Where the written mechanism is not a valid operation.** §2.6 first replaces the tensor contraction ⟨Rm, ∇²a∗(Rm+I)⟩ by the pointwise majorant |∇²a|F², producing the scalar integrand p∫a^{p−2}|∇²a|F^p, and *then* writes “integrate one derivative from ∇²a,” i.e. ∫|∇²a|Φ ≲ ∫|∇a||∇Φ|. Once the absolute value |∇²a| has been taken, this is no longer an integration by parts: |∇²a| carries no divergence structure. The inequality ∫|∇²a|Φ ≲ ∫|∇a||∇Φ| is in fact false in general. One-dimensional witness: take a=χ² a standard cutoff and Φ≡1. Then ∫|∂²a| = TotalVariation(∂a) > 0 because ∂a rises and falls, while ∫|∂a||∂Φ| = 0. So the left side exceeds the right. The “derivative hits only a^{p−2}F^p” narrative therefore cannot be justified by IBP on the pointwise-majorized integrand.

**What is actually true, and it splits into two clean routes.**

- *Route A — pointwise Hessian control, no IBP at all.* If one keeps the pointwise majorant, the correct estimate is simply |∇²a| = |∇²χ²| ≤ C(χ|∇²χ|+|∇χ|²) ≤ Cr^{−2}, giving I_C ≤ Cp r^{−2}Kₚ directly. No integration by parts, and indeed **no dissipation of any kind is consumed** — neither Dₚ^Rm nor Dₚ^F. So the conclusion “this term does not touch Dₚ^Rm” is *true along this route*. The price is exactly the moving-metric Hessian bound |∇²_{g(t)}χ|_{g(t)} ≤ Cr^{−2}, which is the very cutoff-jet obligation flagged in A03 Step 34 §6 (eq. 6.1–6.3: ∂ₜ∇²χ = ∇U∗∇χ is not zero, so this bound does not follow from a fixed initial cutoff). This dependence is the real content and it is not visible in the §2.6 presentation.

- *Route B — honest tensor IBP.* If instead one keeps ⟨Rm, ∇²a∗(Rm+I)⟩ as a genuine tensor and IBPs the honest ∇²a=∇(∇a), the derivative ∇ᵢ hits the three factors of Gⁱʲ = a^{p−2}F^{p−2}·Rm∗(Rm+I):
 – on a^{p−2}: (p−2)a^{p−3}|∇a|²F^p ~ (p−2)r^{−2}Kₚ (no ∇Rm);
 – on F^{p−2}: a^{p−2}|∇a|F^{p−1}|∇F| ~ εDₚ^F + Cr^{−2}Kₚ (∇F, not ∇Rm);
 – **on the curvature factor Rm∗(Rm+I): ∇(Rm∗(Rm+I)) produces a^{p−2}|∇a|F^{p−1}|∇Rm| ~ εDₚ^Rm + Cr^{−2}Kₚ — this term does involve ∇Rm and does consume Dₚ^Rm.**

So the Step 32 §5 review is correct: the *honest tensor IBP* of the Hessian term does draw on Dₚ^Rm. Step 33's assertion that “Dₚ^Rm is NOT consumed by this specific IBP step” is therefore route-dependent, not a property of the term itself. It holds only via Route A, which is not an IBP but a pointwise Hessian bound requiring evolving-cutoff control. The §2.6 “Important note” already half-recognizes this (it admits the tensor formulation yields ∇Rm), but the note presents the pointwise-first path as an *IBP* that avoids Dₚ^Rm, and that particular path is not a legitimate computation.

**Is essential cancellation lost by bounding pointwise first?** No hidden cancellation with the good dissipation is lost. The Hessian term is an error contribution, not sign-definite, and is meant to be dominated; an upper bound is appropriate and does not interfere with the −pDₚ^Rm−p(p−3)Dₚ^F pair. The only substantive cost of the pointwise majorant is the moving-metric |∇²χ| bound noted above.

**Net for Moser.** Either route closes: Route A consumes nothing but needs the evolving Hessian bound; Route B consumes an ε-fraction of Dₚ^Rm, whose coefficient p is available. The final absorbed form εDₚ^Rm + Cp^N r^{−2}Kₚ (or εDₚ^F + …) is correct. What should be corrected in the write-up is (i) delete the invalid “IBP of |∇²a|” sentence, (ii) state Route A's dependence on |∇²_{g(t)}χ| explicitly and tie it to the Step 34 §6 cutoff-jet pair, or (iii) adopt Route B and accept the ε Dₚ^Rm charge — in which case the statement “Dₚ^Rm not consumed” must be dropped.

---

### Statement 2 — J₆ persistence from a bounded Gronwall integral

**The conclusion is correct.** ∫₀ᵀ 𝒮²Y(s) ds is finite and C_Λ is sequence-uniform, so J₆(T) ≤ (const)·J₆(0). But the finiteness is cleanest, and most defensible, through a route the note does not use as its primary argument.

**The clean route.** A03 Step 34 eq. (3.2) gives the *integrated* seed ∫₀ᵗ Y(s) ds ≤ Cγ K₂(0), valid from time zero, with no 1/s factor. Then, since 𝒮²K₂(0)=γ² (from γ=𝒮K₂(0)^{1/2}),
∫₀ᵀ 𝒮²Y ds = 𝒮² ∫₀ᵀ Y ds ≤ 𝒮²·CγK₂(0) = Cγ·γ² = Cγ³.
This is finite directly, with no singularity at 0 and no interval splitting. This is the correct backbone of Statement 2, and it is the same quantity that appears in Step 33 (4.5) as the γ³ term — but obtained without any transition matching.

**Where the Step 33 §4.1 presentation is under-justified.** The note instead derives finiteness by splitting [0,T] at t₀=min(1,T/2), bounding ∫₀^{t₀}𝒮²Y ≤ 𝒮²Y(0)·t₀ on the initial slab and ∫_{t₀}^T γ³/s ds = Cγ³ log(T/t₀) on the tail. The tail is fine: with t₀=T/2 the log is log2, uniform in T (correct, and the whole reason the 1/s seed is integrable *away from 0*). The initial slab is the soft point. Bounding ∫₀^{t₀}𝒮²Y ≤ 𝒮²Y(0)·t₀ requires 𝒮²Y(s) ≤ 𝒮²Y(0) on the *entire* [0,T/2]. Smoothness of the initial data gives only continuity of Y(s) at 0, hence 𝒮²Y(s) ≤ 2𝒮²Y(0) on *some* [0,τ] with τ>0 solution-dependent. If τ < T/2 and τ is not shown to be bounded below sequence-uniformly, the leftover interval [τ, T/2] is controlled only by the 1/s seed, contributing γ³ log((T/2)/τ), which is not uniformly bounded unless τ is quantitatively controlled. Concretely: the 1/s seed equals the initial value at t\*≈γ³/𝒮²Y(0); one needs the boundedness interval τ to reach t\*, which is not supplied by continuity alone.

So the direct answer to your question — “does smoothness justify replacing the 1/t bound by the finite initial value near t=0?” — is: smoothness justifies it on an a priori short, solution-dependent interval, and the transition from the bounded-initial regime to the γ³/t regime has exactly the gap that τ may be smaller than the presumed t₀=T/2. The remedy is not to patch the matching but to use the integrated seed ∫₀ᵗ Y ≤ CγK₂(0), which never introduces a 1/s integrand and makes the splitting unnecessary. With that seed, the transition question does not arise and Statement 2 is correct.

**A structural point to state explicitly (additive source).** The defect inequality (4.4) is J_p′ + c_p D_p^E ≤ Cp^N(r^{−2}+1+𝒮²Y)J_p + C₀′p. Gronwall gives J₆(T) ≤ (J₆(0) + C₀′·p·(source integral))·exp(C_Λ), not J₆(0)exp(C_Λ) as written in (4.6). The additive source is legitimately dropped only in the limit where the hierarchy is homogeneous in E — which is exactly the note's own observation that E≡0 is preserved and “no purely curvature term appears.” The residual C₀′ comes solely from the regularization f_ε=(|E|²+ε)^{1/2} (f_ε=√ε when E=0), so C₀′=C₀′(ε)→0. The step J₆(T)≤J₆(0)exp(C_Λ) is therefore valid in the ε→0 limit, but this should be said, together with ε-uniformity of C_Λ, so that the target (4.7) J₆(T) ≤ Cδ⁶V does not silently swallow an O(Vol)·pT source term. As written, the source is dropped without comment.

**No circular dependence.** The curvature seed 𝒮²Y ≤ γ³/t (and its integrated form) is produced from the q=2/q=3 curvature energy and does not reference J₆. It feeds the defect Gronwall one-directionally, so there is no loop between the curvature seed and J₆ persistence. This is clean, provided the curvature seed itself is established (it is listed as a conditional obligation, Step 34 §5 items 1–3, under Cγ<c₂/2).

---

### Ancillary items found while checking the algebra

1. **Hölder exponent mislabel (§2.7c, and Step 32 (2.5)).** The three-factor identity a^{p−1}F^{p+1}=(aF³)^{1/3}(a^{p−2}F^p)^{1/3}z_p^{4/3} is exact — I verified both exponents: a-side 1/3+(p−2)/3+(4/3)(p−1)/2 = p−1, F-side 1+p/3+2p/3 = p+1. But the stated Hölder triple “(3,3,3/2)” is wrong: 1/3+1/3+2/3 = 4/3 ≠ 1. The correct triple is **(3,3,3)**, giving ‖(aF³)^{1/3}‖₃‖(a^{p−2}F^p)^{1/3}‖₃‖z_p^{4/3}‖₃ = Y^{1/3}Kₚ^{1/3}‖z_p‖₄^{4/3}. The downstream result ‖z_p‖₄^{4/3} — which is what the Sobolev step (0.2) then consumes — is correct; only the printed exponent label is wrong. Your own verification script (item 6, the comment block) already noticed “Holder requires sum = 1 … Correct: use (3,3,3)” but the note text was not updated. Fix the label to (3,3,3) in both notes.

2. **The verification script does not corroborate the two substantive assertions.** For Statement 1, the script encodes `check("Hessian IBP does NOT produce nabla Rm directly", True, …)` and `check("nabla Rm requirement comes from I_B …", True)` — these are hard-coded PASS lines, not computations, and (per the Route A/B analysis) the first is true only via the pointwise route, not via the IBP the string names. For Statement 2, `check("Gronwall integral bounded …", …)` uses two different numerical values of γ (0.025 in the log-integral test, r²√K₀≈9.3e−6 in C_Λ); both happen to give finite C_Λ≈0.1, but the inconsistency means the numbers are illustrative, not a check of the mechanism. The genuinely computational parts (exponent matches in §2.1, §2.3, §2.7b, defect §4.2) are correct. Step 34 §1.3 already records that the earlier `check(...,True)` pattern is assertion rather than verification; the same applies here, so the script should not be read as independent support for either assertion's PDE content.

---

### Summary of standing

- Statement 1: conclusion (Hessian term is absorbable, and can avoid Dₚ^Rm) is attainable, but only via a pointwise |∇²_{g(t)}χ| ≤ Cr^{−2} bound that is itself the evolving cutoff-jet obligation; the printed “IBP of |∇²a|” step is not a valid operation, and the honest tensor IBP does draw on Dₚ^Rm (Step 32 was right). The two notes should be reconciled on this point.
- Statement 2: the finiteness of ∫₀ᵀ 𝒮²Y and the sequence-uniform C_Λ hold, and are cleanly secured by the integrated seed ∫₀ᵗ Y ≤ CγK₂(0); the split-at-t₀ argument as written leaves an unquantified transition interval [τ, T/2]. The exponential-only J₆(T) ≤ J₆(0)exp(C_Λ) needs the ε→0 homogeneity stated so the additive source is accounted for.
- Both conclusions feed forward correctly (curvature endpoint γ/t, defect endpoint δ(r²/t)^{1/3}, integrable drift Cδθ^{2/3}r²), and the volume cancellations in §5 are algebraically exact. The remaining substance is the moving-metric Hessian control for Statement 1's Route A (or acceptance of the Dₚ^Rm charge in Route B), and installing the integrated seed as the primary support for Statement 2.
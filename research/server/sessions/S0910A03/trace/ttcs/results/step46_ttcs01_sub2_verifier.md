# TTCS Independent Branch Record

```json
{
  "step_id": 46,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step41_corrected_restricted_defect_gap_theorem.md",
    "Sessions/S0910A01/workspace/notes/step42_uniform_gap_weight_terminal_repairs.md",
    "Sessions/S0910A01/workspace/notes/step34_integrated_potential_q3_and_defect.md",
    "Sessions/S0910A01/workspace/notes/step35_tensor_variation_and_hessian_a.md",
    "Sessions/S0910A01/workspace/notes/step36_analytic_platform_and_global_Q.md",
    "Sessions/S0910A03/workspace/notes/step39_general_p_defect_power_inequality.md",
    "Sessions/S0910A03/workspace/notes/step45_coordinate_tensor_ledger_and_regularized_closure.md"
  ]
}
```

## Task

Independently reconstruct the support-selection and simultaneous first-exit portion of the proposed family-uniform negative Ricci-defect gap for the Ishida–LeBrun geography. Work on one exact degenerate normalized cutoff flow obtained by the Step 45 coefficient-regularization limit. Check the quantifiers and all collapse-sensitive constants: maximal-function threshold, weighted coloring and disjoint outer buffers, smooth cutoffs with only a uniform gradient bound, a single global coefficient, matched local Sobolev domains, initial K2 and gamma, moving Sobolev comparison, homogeneous K2-to-Y propagation, fixed J6, all-p defect Moser, integrable metric drift, global unweighted Q, and continuation to T=theta r^2. Identify any load-bearing mathematical failure or domain/weight mismatch; if repairable, give a precise corrected construction and dependency argument rather than merely listing concerns. Distinguish per-datum continuation estimates from sequence-uniform first-exit estimates.

## Output

## Verifier memo: support selection and simultaneous first-exit for the λ<0 Ishida–LeBrun defect gap

Working object: the exact degenerate flow ∂_t g = −2χ²(Ric_g+g), a=χ², a global cutoff supported on disjoint macro-supports, obtained as the ε→0 limit of the Step 45 coefficient-regularized transported system b_ε=χ²+ε². I treat existence of this limit as supplied by Step 45 and reconstruct the geometric selection and the sequence-uniform first-exit bootstrap independently, tracking every collapse- and A-sensitive constant.

Overall reconstruction result: the geometric selection is genuinely collapse-robust, the volume-cancellation mechanism that makes γ and both Moser endpoints insensitive to Vol(B_r)→0 is correct, and the simultaneous first-exit statement closes as a strict continuity bootstrap once it is assembled into a single exit time T* with all conditions inside its definition. The source notes derive each energy estimate separately with the moving-comparison premise stated but never write that combined T*; that assembly is the missing load-bearing object, and I give it explicitly below. Two inputs remain genuinely unresolved at the derivation level and both are per-datum, not sequence-uniform: the all-order derivative propagation used for continuation past a finite maximal time (H-WU / Step 45 tensor families, whose exhaustiveness is checked only by a scalar partition script), and the tame estimates for the regularized existence limit. I found no internal inconsistency that blocks the first-exit portion; I found one weight/domain matching item and one geography-uniform (not universal) constant that must be stated as such.

---

### 1. Support selection is collapse-robust — verified with the constants

**Maximal-function step (Step 41 (2.1)–(2.4)).** The weak-type bound Vol{𝓜_{R₀}(|Rm|²)>λ} ≤ C(R₀)λ⁻¹∫|Rm|² is the Bishop–Gromov maximal inequality under Ric≥−2g, which holds along the whole family because near-critical normalization gives Ric≈−g, hence Ric≥−2g eventually. With λ=γ₀²/r⁴ and ∫|Rm|²≤C₀A this gives Vol(bad)≤C r⁴γ₀⁻²A. **One point to state precisely:** C₀ here is *not* universal. Using |Rm|²=|W|²+2|Ric°|²+s²/6 and the 4D Gauss–Bonnet/signature identities,
∫|Rm|² = ∫|W⁺|²+∫|W⁻|²+2∫|Ric°|²+⅙∫s², with ∫|W⁻|²=∫|W⁺|²−12π²τ. Along the family this is O(A) only because the ratios (2χ+3τ)/A and τ/A stay bounded in the Ishida–LeBrun geography. So C₀ is *geography-uniform*, which is exactly the level of uniformity the family-uniform statement asserts; it is worth writing C₀=C₀(geography) rather than C₀ universal.

**Coloring / disjoint outer buffers (Step 41 Step 2).** The number of colors N₀ needed to make B_{7r} disjoint is the packing number of an r-separated set inside B_{15r} under Ric≥−2g. The standard comparison — disjoint B_{r/2}(x_β) inside B_{31r}(x_β)⊇B_{16r}(x_α), so #β ≤ V_{−2}(31r)/V_{−2}(r/2) — is a ratio of explicit comparison volumes and is **independent of the actual (possibly collapsing) local volumes**. This is genuinely collapse-robust; N₀=N₀(n,r) is universal for r≤r₀. I confirm this is not sensitive to collapse, and it is the correct reason the single-color disjointness survives.

**Plateau volume (Step 41 (d), Step 42 §3).** Vol(∪B_{5r}) ≥ Vol(good) ≥ α₀A; one color retains ≥α₀A/N₀; Vol(B_r)≥[V_{−2}(r)/V_{−2}(5r)]Vol(B_{5r}) (concentric Bishop–Gromov, collapse-robust ratio) gives Vol(P^{in})≥c′α₀A. All steps use only comparison-volume ratios, so the retained plateau volume stays proportional to A even under collapse and under A→∞. Verified.

---

### 2. Parameter-choice consistency (γ₀, r, θ, γ*) — apparent tension resolved

The initial absorption parameter is γ=𝒮(0)K₂^η(0)^{1/2}. With the volume-normalized Sobolev constant 𝒮≃C_S r²V^{−1/2} and K₂^η(0)=∫η²(1+|Rm|²)≤V(1+γ₀²/r⁴), the V-powers cancel exactly:
γ ≤ C_S r²(1+γ₀²/r⁴)^{1/2} = C_S(r⁴+γ₀²)^{1/2}.
There is a genuine tension worth naming: the absorption steps (Step 34 (3.4), Step 39 (6.2)) require Cγ below a fixed fraction, while the bad-set estimate requires C r⁴γ₀⁻² < 32π²/9 for a positive good-set fraction. Both are satisfiable simultaneously only because γ₀ and r are *two independent free parameters*: fix the absorption threshold γ* first (universal), then γ₀ = γ*/(3C_S) small, then r⁴ ≤ min(γ₀², c γ₀²) so both r⁴+γ₀² ≲ γ₀² and the bad-set fraction stays below ½. This ordering closes. It should be written explicitly, because it forces γ₀ (hence r₀, hence α₀ and the volume fraction) to depend on the Sobolev structural constant C_S — a dependency the notes leave implicit.

---

### 3. The volume-normalized local Sobolev inequality is a load-bearing standard input

Every collapse cancellation (γ in §2, both Moser endpoints in §6) rests on 𝒮≃C_S r²V^{−2/n} with C_S=C(n,Kr²) depending only on dimension and the lower Ricci bound times r², *not* on noncollapsing. This is true — it is the doubling+Poincaré⇒scale-invariant Sobolev machinery under Ric≥−(n−1)K (Saloff-Coste; Maheux–Saloff-Coste), which is exactly collapse-robust. But it is load-bearing and the notes only write "𝒮≃C(4,Kr²)r²V^{−1/2}" without pinning the statement. A self-contained writeup needs the Dirichlet form
‖u‖_{2n/(n−2)}² ≤ C(n,Kr²) r² Vol(B)^{−2/n}(‖∇u‖₂²+r^{−2}‖u‖₂²), u∈C_c^∞(B),
valid on every good ball B_{7r}(x_α) with one C(n,Kr²) uniform over the family. This is the single analytic fact on which the entire "collapse cancels" architecture depends, and it is the right one.

**Matched domains (item flagged in the task).** The notes use B_{5r} (plateau), B_{7r} (support), supp η, and B_{R₀} (maximal function) somewhat interchangeably. A consistent nested family B_{5r}⊂B_{7r}⊂supp η⊂B_{R₀} with all pairwise volume ratios controlled by Bishop–Gromov (collapse-robust) and the Sobolev constant taken on the outermost ball must be fixed once; the estimates then all live on one Sobolev domain per support. This is bookkeeping, not an obstruction, but it is currently not matched in writing.

---

### 4. The simultaneous first-exit bootstrap — explicit assembly

This is the object the source enumerates piecewise (Step 36 §4) but does not assemble. Here is the single continuity argument, with the strict improvements checked.

Fix i large so δ_i is small. Step 45 gives a maximal smooth degenerate-flow solution on [0,T_max), T_max>0 (per-datum). Define
> T* = sup{ t ≤ min(T_max, θr²) : for all supports α and all s≤t,
> (E1) K₂^η_α(s) ≤ 2K₂^η_α(0); (E2) 𝒮_α(s) ≤ 2𝒮_α(0); (E3) ∫₀^s ‖aE‖_∞ dσ ≤ α₀ }.

The conditions are closed and, on [0,T*], the derived estimates hold; I check each improves strictly.

- **(E1) improves.** Step 34 (3.1)+(3.4): (K₂^η)′+cD₂^η ≤ CY+Cr^{−2}K₂^η with Y≤Cγ(t)(D₂^η+r^{−2}K₂^η). On [0,T*], (E1)+(E2) give γ(t)=𝒮(t)K₂(t)^{1/2}≤2√2·γ(0)≤2√2γ*, so choosing γ* with 2√2Cγ*<c/2 absorbs D₂^η, leaving (K₂^η)′≤Cr^{−2}K₂^η, hence K₂^η(t)≤e^{Cθ}K₂^η(0). Choose θ with e^{Cθ}<2. Strict.
- **(E3) improves.** The defect Moser endpoint (§6) gives ‖aE(t)‖_∞≤Cδ(r²/t)^{1/3}, integrable: ∫₀^{θr²}=(3/2)Cδθ^{2/3}r². For i large this is < α₀ with room. Strict.
- **(E2) improves.** (E3) gives bilipschitz g(t)=(1+O(δ))g(0) on each support, so volumes and gradients on the ball move by (1+O(δ)) factors and 𝒮(t)≤(1+O(δ))𝒮(0)<2𝒮(0). Strict.

So T* cannot be an interior exit; T*=min(T_max,θr²). **Non-circularity:** the estimates that improve (E1)–(E3) are derived under (E1)–(E3) on the closed interval [0,t⁠], which is the legitimate continuity method — there is no vicious loop, provided the improvements are strict (they are, for θ and δ small). This is exactly the "moving-geometry premise closed by the drift and continuation" of Step 34 §0, now made into one exit time.

**Reaching θr².** If T_max ≤ θr², take τ=T_max/2. The curvature Moser bound ‖aF(t)‖_∞≤Cγ/t gives |U|=|aT|≤Cγ/τ+C=:K(τ)<∞ on [τ,T_max), and (E3) gives finite bilipschitz on all of [0,T_max). Feeding these into the per-datum continuation (Step 41 Thm 5.1 / Step 36 §2) forces all higher spatial derivatives finite on [τ,T_max), so the solution extends past T_max — contradiction. Hence T_max>θr² and T*=θr². The bootstrap closes.

The strict-improvement structure is sound. The residual is entirely in the continuation input feeding this last paragraph (§5).

---

### 5. Per-datum vs sequence-uniform separation — where the open inputs sit

The task's central quantifier question resolves cleanly, and the separation is correctly designed in the notes:

- **Sequence-uniform (family) estimates:** support selection constants (§1), γ (§2), homogeneous K₂→Y (Step 34 (5.3): multiplicative, no bare additive C₀T — this is what "survives collapse"), fixed J₆(t)≤e^{C(1+r^{−2})t}J₆(0) with J₆(0)≤C(2δ)⁶V, Theorem 7.1 all-p defect power inequality, both Moser endpoints, drift, and Q(t)≤e^{C(1+r^{−2})t}Q(0) with Q(0)/A≤Cδ²→0. **These use only |∇χ|≤C/r**, never a pointwise ∇²χ bound — the signed-Hessian IBP in Step 35 §3.3/§6.4 and Step 34 (2.11) deliberately keep the Hessian contracted with the tensor B_curv, B_def and pay it by |∇a|²/a≤Cr^{−2}. So the first-exit layer is genuinely uniform over the collapsing family with unbounded numbers of supports (sup-based drift does not accumulate; energies sum linearly over disjoint supports).

- **Per-datum estimates:** short-time existence and continuation. The higher cutoff jets ∇^mχ (m≥2) and all higher-order derivative propagation enter only here. Step 45 correctly places these constants as per-datum (depending on g_i's smooth norms and on τ, T_max) and requires only *finiteness* for extension — not uniformity. This is the right split, and it is the reason the whole route is phrased in U=aT (Step 36 (2.3)–(2.5)): the sequence-uniform Moser controls exactly |U|=|aT|, which is exactly the quantity the per-datum continuation consumes. The weight matches; no mismatch there.

- **Step 45's genuine contribution to the open input.** The earlier Step 41/42 ambiguity (χC_{m+2}U vs bare C_{m+2}U) is resolved at the induction-structure level by working with b=χ²+ε², never dividing by b, and using the ε-uniform ratios |B₁|²/b=4(χ²/b)|C₁|²≤4|C₁|² and χ²/b≤1 (Step 45 (3.2)). The dangerous current cutoff jet (Step 45 (4.5)) carries coefficient 4(χ²/b)C_{m+1}C₁U₀, bounded because U₀ is bounded — the two χ factors are what convert the base-stage C₂T₀ into a bounded C₂U₀ coupling. This is correct and is the right fix. **The residual concern:** the exhaustiveness of the tensor families (T1)–(T6),(U1)–(U7) and the exactness of their coefficients from the true all-covariant Riemann variation is verified only by a scalar/partition script (110/110), which by its own statement "is not evidence for tensor contractions or PDE existence." So the continuation theorem is structurally supported but not yet an index-level tensor proof. Because continuation is per-datum and only needs finiteness, this does not touch the sequence-uniform first-exit closure — but it is the remaining substance before T_max>θr² is unconditional.

---

### 6. Collapse-insensitivity of the two Moser endpoints — arithmetic confirmed

This is the crux and it checks exactly.

**Defect (Step 39 §8).** ‖aE(t)‖_∞ ≤ C 𝒮^{1/3} t^{−1/2}(∫_{t/2}^t H₆)^{1/6}. With H₆=J₆≤Cδ⁶V and 𝒮≃r²V^{−1/2}:
𝒮^{1/3}=r^{2/3}V^{−1/6}; (∫H₆)^{1/6}≤(t·Cδ⁶V)^{1/6}=Ct^{1/6}δV^{1/6}. Product: r^{2/3}V^{−1/6}·t^{−1/2}·t^{1/6}δV^{1/6}=Cδ r^{2/3}t^{−1/3}=Cδ(r²/t)^{1/3}. The V^{−1/6} from Sobolev cancels V^{1/6} from J₆^{1/6} exactly. **Collapse-insensitive; verified.**

**Curvature (Step 34 (4.4), Step 39 §8).** ‖aF(t)‖_∞≲γ/t with γ≤C(r⁴+γ₀²)^{1/2} (§2). Collapse-insensitive; verified.

**p-uniform gradient comparison (Step 39 (5.4)).** ‖∇z_p‖₂²≤¾𝒟_p+Cp²r^{−2}H_p with the ¾ *p-independent* because q/(2(q−1))≤¾ for q≥3, which requires retaining the chain-rule dissipation q(q−1)X′_p rather than discarding it as at the fixed p=6 seed. This is a correct and necessary structural point; the two-factor absorption's linear-in-𝒟_p coefficient (Step 39 §6) genuinely cannot climb the ladder (it would demand γ≲p^{−1}), and the three-factor route converts the reaction into the Grönwall multiplier Cp^N𝒮²Y instead. I confirm this dichotomy is real and correctly resolves the Step 38 ambiguity.

One consistency point that looks contradictory but is not: Y(t)≤CγK₂(0)/t (Step 34 (4.4)) and ∫₀^t Y≤CγK₂(0) (Step 34 (3.6)) coexist because the pointwise 1/t bound is a crude Grönwall-on-a-slice consequence, not saturated near 0; the energy integral is the tight statement. The Moser step uses the 1/t form as an ess-sup on dyadic slabs (S²Y≤Cγ³/t), which is legitimate. No inconsistency.

---

### 7. Items to fix or state, in order of load

1. **Assemble the single exit time T* (§4).** The strict-improvement bootstrap must appear as one argument; presently the pieces live in Steps 34/36/39 with the moving-comparison premise asserted separately in each. This is fillable exactly as in §4 and is the main missing writing.
2. **Continuation input (§5).** T_max>θr² is per-datum and rests on the tensor-family exhaustiveness of Step 45, which is checked only combinatorially. An index-level derivation that families (U1)–(U7) are complete and that no term escapes the bounded-coefficient/forcing dichotomy is the remaining substance. Because it is per-datum finiteness, it does not affect the sequence-uniform estimates.
3. **Uniform volume-normalized Sobolev (§3)** and **matched nested balls** must be stated with the C(n,Kr²)-only constant and one Sobolev domain per support; the collapse cancellations depend on this exact form.
4. **C₀ in the maximal-function step is geography-uniform, not universal** (§1); write it as such.

---

### 8. Substance of the target statement

For fixed topology with q>0 the pointwise bound δ ≥ c√(q/A) (Step 42 §3, consistent with q/A ≤ Cδ² from (2.4) and Vol/A→32π²/9) already gives a positive threshold, but it *degrades* as A→∞ with q/A→0 — precisely the collapsing / unbounded-topology regime. A family-uniform ε_IL independent of A, q, N is therefore a genuinely stronger assertion than the elementary mixed Seiberg–Witten bound, and the flow-plus-Derdziński architecture is what would supply it. The first-exit portion reconstructed here is the mechanism that carries Q(θr²)/A→0 and bounded-curvature plateaux to the terminal calibration; the terminal recalibration (Step 41 §7, verified Chern–Weil algebra I−J=2A/3−q and (κ⁺)²≥κ²=A) and the Derdziński germ (Step 41 §8) are downstream of the task's portion and were spot-checked as internally correct, but their own compactness passage (strong W^{2,p}, Step 42 §5) is a separate object.

Net: on the Step-45 degenerate flow, the support-selection and simultaneous first-exit portion is a consistent, collapse-robust, non-circular bootstrap once assembled as in §4; its remaining unconditional dependence is the per-datum continuation/existence input, which is correctly separated from the sequence-uniform family estimates and does not weaken them. All statements here remain inside the λ<0 Ishida–LeBrun geography and do not touch the λ>0 route, general four-manifold topology, n≥5, dimension-only constants, or the Lean formalization.
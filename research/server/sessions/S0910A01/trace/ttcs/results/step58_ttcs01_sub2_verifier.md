# TTCS Independent Branch Record

```json
{
  "step_id": 58,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step58_all_order_continuation_proof.md",
    "Sessions/S0910A01/workspace/notes/step55_finite_restart_threshold_and_C3_exchange.md",
    "Sessions/S0910A01/workspace/notes/step57_preceptor_deTurck_uniqueness_and_scope_review.md",
    "Sessions/S0910A01/trace/ttcs/results/step57_ttcs02_verifier1_integration.md"
  ]
}
```

## Task

Verify the proof-level all-order continuation note for the restricted four-dimensional negative IL cutoff flow. Focus on five specific mathematical points:

1. CORRECTED BASE EQUATIONS (§2): The T-equation is ∂_t T = aΔT + B₁*∇T + B₂*T + a(T*T + T). The U-equation after the (B₁*B₁)*T = 4(C₁*C₁)*U identity is ∂_t U = div(a∇U) + B₁*∇U + B₂*U + 4(C₁*C₁)*U + U*U + aU. Verify: (a) T=U=0 is stationary, (b) no independent constant forcing a·1 or a² appears, (c) the conversion from ∂_t U = a·∂_t T using the Laplacian product rule is correct.

2. INDUCTION BASE (§3, §5.2): The base layer T₀,T₁,U₁,C₂ ∈ L^q is established by the curvature/defect Moser endpoints and the W^{1,p} bridge. Verify that the general induction mechanism (§5) genuinely fails at m=1 — specifically that I₁ = ∫χ|C₂||U₁|^p cannot be closed by the same Hölder-Sobolev pattern because U₁ is the current unknown.

3. CRITICAL RESIDUAL ABSORPTION (§5.2): For m≥2, the residual I_m = ∫χ|C_{m+1}||U₁||U_m|^{p-1} is controlled using f=χ|U_m|^{p/2}, Hölder (4,p,4,2p/(p-2)), and U₁∈L⁴ as a base-layer quantity. Verify the exponent matching, the role of U₁ as known (not current), and whether Young yields the correct linear Grönwall structure.

4. SIGNED-HESSIAN INTEGRATION (§5.3): The term χC₂*U_m is not treated as a bounded coefficient. Integration by parts replaces C₂=∇C₁+... and produces ε D_{m,p}^U + C||C₁||_∞²||V||_p^p. Verify this uses only ||∇χ||_∞, not ||∇²χ||_∞.

5. AUTONOMOUS SPLICE (§8): The C^∞ convergence g(t)→g_* from §7, plus positive-definiteness from §8.1, plus the recursive jet identity F_ℓ(g*) = lim ∂_t^ℓ g(t) = ∂_s^ℓ ĝ(0), gives a smooth spliced solution across T*. Verify: (a) all one-sided jets genuinely match because the PDE is autonomous; (b) no uniqueness comparison is needed; (c) the positive-definiteness argument from the integrable defect endpoint is correct.

## Output

# Verification memo: all-order continuation note (Step 58) for the four-dimensional Ric→−g Ishida–LeBrun cutoff flow

I checked the five requested points by redoing the underlying computations rather than reading the star-product statements at face value. All five hold. Below are the concrete confirmations, the one linchpin identity that the whole coupled system rests on (worth stating explicitly), and the substantive proof obligations that are imported rather than settled in this note.

---

## Point 1 — Corrected base equations (§2)

**(a) Stationarity.** With `T = Rm + G`, `G = g⊛g/6`, `n=4`: `T≡0` forces `Rm = −G`, i.e. constant sectional curvature `−1/(n−1) = −1/3`, hence `Ric = (n−1)(−1/3)g = −g`, so `E = Ric + g = 0` and `∂_t g = −2aE = 0`. Since the metric does not move, `∂_t Rm = 0` and `∂_t G = 0`, giving `∂_t T = ∂_t U = 0`. The stationarity is genuine, not assumed.

**(b) Absence of independent constant forcing.** Because `T=U=0` is a rest state, any putative `a·1` or `a²` term (which does not vanish at `T=0`) is inconsistent with the flow. So the earlier structural equations carrying such forcing were incorrect, and the corrected forms `a(T*T+T)` and `U*U+aU` (each vanishing at the rest state) are the right ones. This is a correct removal.

**(c) The `∂_t U = a·∂_t T` conversion into divergence form is correct.** I verified the divergence grouping explicitly. Using `∇U = a∇T + B₁*T`, `ΔU = aΔT + 2B₁*∇T + B₂*T`, and `div(a∇U) = aΔU + ∇a·∇U`:

    div(a∇U) = a²ΔT + 3aB₁*∇T + aB₂*T + (B₁*B₁)*T.

From `∂_t U = a∂_t T = a²ΔT + aB₁*∇T + aB₂*T + a²(T*T) + a²T`, subtracting:

    ∂_t U − div(a∇U) = −2aB₁*∇T + a²(T*T) + a²T − (B₁*B₁)*T.

Now `a²(T*T) = U*U`, `a²T = aU`, and `−2aB₁*∇T = −2B₁*(∇U − B₁*T) = −2B₁*∇U + 2(B₁*B₁)*T`, giving

    ∂_t U = div(a∇U) − 2B₁*∇U + (B₁*B₁)*T + U*U + aU.

This matches (2.3) at the star-product level (the `−2` sits inside the `B₁*∇U` symbol). One point worth recording: the `B₂*U` term the note carries is the *full-Hessian* contraction of `∇²a` with `U` coming from `a·∂_t T`, which is not identical to the *trace* `(Δa)U` produced inside `ΔU`; the two do not cancel, so keeping `B₂*U` is correct and not redundant.

**The `(B₁*B₁)*T = 4(C₁*C₁)*U` identity is exact.** With `B₁ = ∇(χ²) = 2χC₁`, every contraction obeys `(B₁*B₁)*T = 4χ²(C₁*C₁)*T = 4(C₁*C₁)*(aT) = 4(C₁*C₁)*U`. No division by `a`; the identity is algebraic and holds where `χ=0`. This is what removes the unweighted `T` from the `U`-equation.

**One nuance about "bounded coefficients."** The note's remark in §2.5 that every coefficient of `U` is bounded is slightly imprecise: `B₂ = ∇²(χ²) = 2χC₂ + 2C₁*C₁`, and because the `C_j` are covariant derivatives with respect to the evolving connection, `C₂ = ∇^{g(t)}²χ` inherits only finite-`L^q` control (through the connection difference `A`), not `L^∞`. The `2χC₂` piece is exactly the signed-Hessian term treated separately in §5.3. `C₁ = dχ` is genuinely `L^∞` (a scalar's first covariant derivative is the ordinary differential, connection-free). So the distinction "`C₁∈L^∞`, `C₂∈L^q` only" is internally consistent and is the correct reason the χC₂ terms need special handling.

---

## Point 2 — The mechanism does not close at m=1 (§5.2)

Confirmed, and the reason is exactly as stated. The general residual after integrating the top cutoff term is
`I_m = ∫ χ|C_{m+1}||U₁||U_m|^{p-1}`. At `m=1` this becomes `I₁ = ∫ χ|C₂||U₁|^p`, and in the Hölder split (5.7) the factor playing the role of the known `‖U₁‖₄` coincides with the current unknown: there are then *three* factors built from `U₁` (`f = χ|U₁|^{p/2}`, `‖U₁‖_p`, and `‖U₁‖₄`). The Sobolev inequality (5.6) absorbs one into `D_{1,p}`, but the extra `‖U₁‖₄` is not controllable current data, so Young produces a term nonlinear in the current unknown and cannot yield the linear differential inequality. Hence `T₀,T₁,U₁,C₂∈L^q` must be supplied by the curvature/defect Moser endpoints and the `W^{1,p}→L^∞` bridge, and the uniform mechanism starts at `m=2`. The reasoning is sound; starting the same estimate at `m=1` would be circular.

---

## Point 3 — Critical residual absorption for m≥2 (§5.2)

**Exponent matching is exact.** For `(4, p, 4, 2p/(p−2))`: `1/4 + 1/p + 1/4 + (p−2)/(2p) = 1/2 + [2 + (p−2)]/(2p) = 1/2 + 1/2 = 1`. The factor assignment `f→L⁴`, `C_{m+1}→L^p`, `U₁→L⁴`, `|U_m|^{p/2−1}→L^{2p/(p−2)}` reproduces `‖U_m‖_p^{p/2−1}` in the last slot, matching (5.7).

**Sobolev step is correct.** `∇(χ|V|^{p/2}) = (∇χ)|V|^{p/2} + (p/2)χ|V|^{p/2−1}∇|V|`, so `‖∇f‖₂² ≤ C‖C₁‖_∞²‖V‖_p^p + Cp²∫a|V|^{p−2}|∇V|²` with `χ² = a`, giving `‖f‖₄² ≤ C_S(p²D_{m,p}^U + C‖V‖_p^p)`, exactly (5.6).

**The role of `U₁` as known and the linear structure.** With `‖U₁‖₄` treated as a fixed base constant (legitimate for `m≥2`), the two Young steps yield `I_m ≤ εD_{m,p}^U + C(1 + ‖C_{m+1}‖_p^p + ‖U_m‖_p^p)` — linear in the two `L^p` energies, hence a genuine linear Grönwall right-hand side after adding the cutoff-jet inequality. The `‖Z‖_p²‖V‖_p^{p−2}` intermediate is split by Young with exponents `p/2, p/(p−2)` into `‖Z‖_p^p + ‖V‖_p^p`. Correct.

---

## Point 4 — Signed-Hessian integration (§5.3)

Correct, and it uses only `‖∇χ‖_∞`. Writing `C₂ = ∇C₁` (the covariant Hessian of the differential `C₁ = dχ`, no extra connection insertions), integration by parts gives
`|J_m| ≤ C∫|C₁|²|V|^p + Cp∫χ|C₁||V|^{p-1}|∇V|`.
The second integral factors as `|C₁||V|^{p/2} · (χ|V|^{p/2−1}|∇V|)`; Young against the weighted gradient gives `ε∫χ²|V|^{p−2}|∇V|² + C‖C₁‖_∞²‖V‖_p^p = εD_{m,p}^U + C‖C₁‖_∞²‖V‖_p^p`. No `L^∞` bound on `C₂ = ∇²χ` enters; only `‖C₁‖_∞ = ‖∇χ‖_∞ ≤ C/r`. This is precisely why the finite-`L^q`-only control of `C₂` is not an obstruction.

---

## Point 5 — Autonomous splice (§8)

**(a) One-sided time jets match.** The flow map `F(g) = −2χ²(Ric_g + g)` carries no explicit `t`, so differentiating `∂_t g = F(g)` gives `∂_t^ℓ g = F_ℓ(g)` with `F_{ℓ+1} = DF_ℓ[F]`, each `F_ℓ` a differential operator in the spatial jet of `g` and the fixed `χ`. The old branch has `∂_t^ℓ g(t) = F_ℓ(g(t)) → F_ℓ(g_*)` by `C^∞` convergence (§7) and continuity of `F_ℓ`; any solution `ĝ` with `ĝ(0)=g_*` has `∂_s^ℓ ĝ(0) = F_ℓ(g_*)`. All one-sided time derivatives at `T_*` agree. Also the equation itself holds at `T_*`: left derivative `F₁(g_*) = F(g_*)` equals the right derivative `F(g_*)`.

**(b) No two-solution comparison is used.** Matching all one-sided time derivatives plus continuity of each gives `C^∞` regularity of the spliced curve in `t`; combined with spatial smoothness this is a genuine smooth solution across `T_*`. This is a Whitney/Borel-type junction argument on the two one-sided Taylor expansions, and it does not require an overlap estimate for two metrics on a common interval. It correctly avoids the ungauged raw-metric `L²` comparison that §1 of the Step 57 note showed to be non-parabolic.

**(c) Positive-definiteness.** From `‖∂_t g‖_{g,op} ≤ 2‖aE‖_∞ ≤ C_E δ(r²/t)^{1/3}` and `∫_τ^{T_*}(r²/t)^{1/3}dt = r^{2/3}·\tfrac{3}{2}(T_*^{2/3}−τ^{2/3}) < ∞` (the exponent `−1/3 > −1` is integrable, and `τ>0`, `T_*<∞`), the operator-Grönwall bound `e^{−2V_*}g(τ) ≤ g(t) ≤ e^{2V_*}g(τ)` with `V_* = ∫_τ^{T_*}‖aE‖_∞` holds. This bilipschitz control is what keeps `g_*` non-degenerate; `C^∞` convergence alone would only produce a smooth symmetric 2-tensor. The note correctly invokes both.

---

## Linchpin worth stating explicitly: triangularity of the cutoff-jet equation

The entire coupled `(U_m, C_{m+1})` induction closes only because `∂_t C_{m+1}` is forced by `U_m`, not `U_{m+1}`. I verified this. Since `C₁ = dχ` is time-independent, writing `C_{m+1} = ∇^m C₁` and using `∂_t(∇^m A) = ∇^m∂_t A + Σ_{r+s=m−1}∇^r(∂_tΓ)*∇^s A` with `∂_t A = 0` and `∇^r(∂_tΓ) = ∇^r(g^{-1}*U₁) ∼ U_{r+1}` gives

    ∂_t C_{m+1} = Σ_{r+s=m−1} U_{r+1}*C_{s+1},   top term (r=m−1): C₁*U_m.

Explicit low cases confirm it: `∂_t C₂ = C₁*U₁`, `∂_t C₃ = C₁*U₂ + C₂*U₁`. The commutator sum runs to `r+s=m−1`, one lower than the `m` derivatives on `C₁`, so the highest current index is `U_m`. This is exactly the structure that makes the pair system solvable stage by stage without ever needing the next current level; it is the load-bearing point of §4.2 and it is correct.

Two related structural checks also hold: the zeroth-order spatial-commutator coefficient `a·Rm` is bounded because `a·Rm = U − aG` (both bounded on the slab), and the extremal `a∇^mRm*U_0` reduces via `aT_m = U_m − Σ_{q=1}^m \binom{m}{q}B_q*T_{m−q}` (exact Leibniz, all unweighted `T`-factors at index `≤ m−1`) to `U_m*U_0` plus strictly prior terms, since `∇^mG = 0` for `m≥1`. No bare `T_m` survives outside bounded-coefficient or prior-level products.

---

## What is imported rather than settled here, and what still needs writing

The five points are internally correct. The material the note depends on but does not itself establish:

1. **Index-level exhaustiveness of the `T_m`/`U_m`/`C_{m+1}` families.** The remainder polynomials `𝒫_m, ℛ_m, 𝒮_m` are described schematically. In particular the time-reordering products `(∇^qRm)*U_{r−q}*U_s` and `(∇^qRm)*U_{r−q}*T_s` with `q ≤ m−2` are asserted to be strictly lower-level but are not written into the remainder with all index constraints enumerated. The verification scripts count integer allocations (a consistency test) but do not generate the tensor identities from the PDE. A single index-level commutator lemma — base curvature evolution plus the full contraction inventory — is the outstanding piece. The Step 57 note and the earlier verification memo both flag the same thing; it remains open.

2. **The base layer `T₀,T₁,U₁,C₂∈L_t^∞L_x^q`.** This is input from the curvature first-exit branch, defect Moser endpoint, and `W^{1,p}` bridge. The uniform-in-`t` `L^q` control of the unweighted `T₀` on the collar (where `a→0`, so `‖U‖_∞≤K` does not by itself bound `T`) rests on the curvature branch, not on this note. At each fixed time `T(·,t)` is bounded since `M⁴` is compact and `g(t)` smooth, but the uniform-in-`t` finite-`L^q` statement is the curvature branch's responsibility.

3. **The signed-Hessian contraction estimate** used in §5.3/§5.4 is invoked from the earlier defect endpoint work; it is applied here but not re-derived.

4. **Per-datum local existence and gauge reconstruction** (transported-cutoff DeTurck) is the one input the note itself marks conditional. The `C^∞` convergence in §7 also rests on the fixed-background `H^s` induction of §7.4, which is written at the same schematic level as the current-pair tower.

5. **What the result addresses.** The whole construction lives on the four-dimensional Ric→−g Ishida–LeBrun geography and, as the note states, produces a uniform pinching gap for that family. It does not yield the dimension-only two-sided Ricci constants `c_n < C_n` of Yau 26, does not treat the `λ>0` sign, general four-dimensional topology, or `n≥5`, and there is no Lean formalization. The refutation direction of Yau 26 would additionally require defeating both signs of `λ`. The internal correctness of Steps 55/57/58 is consistent with the material addressing only the restricted family.

Net: the five specific computations are correct as written; the residual work is the index-level tensor enumeration behind the schematic star-products and the two imported analytic inputs (base layer and per-datum existence).
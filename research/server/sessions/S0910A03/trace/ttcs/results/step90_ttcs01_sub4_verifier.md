# TTCS Independent Branch Record

```json
{
  "step_id": 90,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step89_twist_bochner_and_resolvent.md",
    "Sessions/S0910A03/trace/ttcs/results/step89_ttcs01_verifier1_integration.md",
    "Sessions/S0910A03/workspace/scripts/step89_symbolic_twist_ricci.py",
    "Sessions/S0910A03/workspace/data/step89_symbolic_twist_ricci.json",
    "Sessions/S0910A03/workspace/scripts/step90_charge_potential_verify.py",
    "Sessions/S0910A03/workspace/data/step90_charge_potential_verify.json",
    "Sessions/S0910A03/workspace/scripts/step90_exchange_inequality_verify.py",
    "Sessions/S0910A03/workspace/data/step90_exchange_inequality_verify.json",
    "Sessions/S0910A03/workspace/notes/step86_forced_bochner_superlevel_and_localization.md",
    "Sessions/S0910A03/workspace/notes/step88_reflection_free_minimal_separator.md"
  ]
}
```

## Task

Independently verify and strengthen the Step 90 structured forced free-T^2 reduction. Read the Step 89 derivation, its verifier, and the two new symbolic outputs/scripts. Check in the established H^2 normalization whether Q=(1/2)e^{-3σ}q^T M^{-1}q satisfies Hess_H Q=Qh and |grad_H Q|^2=Q^2; whether the fixed-charge twist source is S_F=-grad_H Q; and whether <dU,D S_F>=-Qe+3<dσ,<grad Q,dU>> plus a term linear in dq. Verify the exact invariant coefficient/norm relating dq to mixed Ricci defect and the round-cusp physical law w'+3w=forcing. Then derive the strongest valid Bochner or combined-energy inequality available without treating variable Q as constant. Keep inf Q (curvature), sup/source norms, and separator average distinct. State plainly whether the +Qe base term cancels, whether any further cancellation with the area equation is available, and what remains unresolved for a complete forced-twist obstruction. Do not extrapolate beyond the free-T^2 class.

## Output

# Verification Memo — Step 90 structured forced free‑T² reduction

Session S0910A03 material: Step 89 note + its verifier integration, `step90_charge_potential_verify.py/.json`, `step90_exchange_inequality_verify.py/.json`, with Steps 86 and 88 as context.

## 1. Overall reading

The horospherical‑potential structure, the source identification, the structured covariant‑derivative identity, the canonical charge‑norm, and the round‑cusp first‑order law are all correct as stated, and I reproduced the load‑bearing ones independently. The **central structural result — the pointwise cancellation of the two linear‑in‑Q terms** — is genuine and holds for variable Q; it cleanly resolves the sign oscillation between Steps 88 and 89. Two items need correction or explicit derivation before they can carry weight: (i) the stated magnitude of the σ–charge exchange term understates its Q‑dependence, and (ii) the invariant coefficient relating `dq` to the mixed Ricci defect is asserted, not derived, in these artifacts. The forced‑twist case with Q>0 (asymptotic/forced ends) is not closed by any inequality present here; I explain below exactly which term blocks it and why the two published decompositions push the same difficulty into different, still‑uncontrolled places.

## 2. Items verified (with independent recomputation)

**Horospherical potential.** In the Iwasawa chart `M = [[e^a+β²e^{-a}, βe^{-a}],[βe^{-a}, e^{-a}]]` (det M = 1) with `h = da² + e^{-2a}dβ²` (Gaussian curvature −1, since −(e^{-a})″/e^{-a} = −1), I confirmed at the point `a=β=0`, `q=(q0,0)` that `∂_a Q = −Q`, `∂_β Q = 0`, so `grad Q = (−Q,0)`, `Hess_{aa}Q = Q`, `Hess_{ββ}Q = −Γ^a_{ββ}∂_aQ = e^{-2a}Q`, `Hess_{aβ}=0`, i.e. `Hess Q = Q h` and `|grad Q|² = Q²`. The script's symbolic residuals are zero for all `(a,β,σ,q)`, so these hold identically. Geometric identification: `Hess f = f h` with `|∇f|²=f²` forces `f = C·e^{b}`, `b` a Busemann function (`|∇b|=1`, `Hess b = h − db⊗db`). Thus `Q` is the exponential of a Busemann function scaled by `e^{-3σ}`. This is exactly the classical charged harmonic‑map (Ernst/stationary‑axisymmetric) potential and is why the two identities are forced rather than coincidental. **Verified.**

**Source S_F = −grad_H Q.** At the canonical diagonal point the α‑component of `S` equals `Q`, matching the exact vertical equation `Lα = Q` established (and verified) in Step 89. The residual is zero. This is consistent with the reduced Einstein twist stress; the full identification for arbitrary `M` (all off‑diagonal orientations) rests on the classical reduction and on the generic‑jet identity below rather than on a full index‑level derivation recorded in these files. **Verified at the canonical point; the all‑M physical identification is well grounded in the standard reduction but is not itself written out here.**

**Structured identity `<dU, D S_F> = −Qe + 3X + R_q`.** Symbolic residual zero for generic `u`, `σ`‑jet, and `dq` jets. I confirmed the mechanism: the pure target part is `<u_i, D(−grad Q) u_i> = −<u_i, (Hess Q) u_i> = −Q|u_i|²`, summing to `−Qe`; the factor 3 in the exchange term comes directly from `S_F ∝ e^{-3σ}`, so `∂_σ S_F = −3 S_F = 3 grad Q`, giving `3X` with `X = Σ_i (dσ·e_i)⟨grad Q, dU(e_i)⟩`. **Verified.**

**Canonical charge‑norm `|D_q S[dq]|² = 2Q|b|²`.** With `dq = e^{(3/2)σ}(b1,b2)`, `D_qS = q0 e^{-3σ/2}(b1,b2)`, norm² `= q0² e^{-3σ}(b1²+b2²) = 2·(½q0²e^{-3σ})·|b|² = 2Q|b|²`. **Verified.** Note the `√Q` scaling of `|D_qS|` — this is the correct scaling for the charge‑derivative term and is what I use in §3.

**Φ(A) ≥ ½e².** With eigenvalues `λ1,λ2` of `A=U*h`: `Φ = ½tr(A²)+2det A = ½(λ1²+λ2²)+2λ1λ2 = ½e² + det A ≥ ½e²`. **Verified.** This term (target curvature −1) is the load‑bearing quadratic driving the whole reaction; it is inherited from Steps 86–89, where it was checked, and everything below depends on it.

**Round‑cusp first‑order law.** With `w = e^{-(3σ+α)/2}q`, differentiation gives `w' + (3σ'/2 + α'/2)w = e^{-(3σ+α)/2}q'` identically; on the round cusp (`σ=2r,α=0`) this is `w'+3w = b`. This is an integrating‑factor identity, not an independent physical input, but it correctly encodes the damping. The exact envelope `w(t) = e^{-3Δ}w(t0) + (B/3)(1−e^{-3Δ})` is the solution of `w'+3w=B`. Physical content: a sustained forcing `|b|≤B` leaves `|w|` at order `B/3`, not forced to zero. **Verified,** and it correctly shows that on a merely asymptotic cusp a forced charge need not decay — so `Q` need not vanish asymptotically there.

## 3. Correction: the exchange‑term magnitude is understated

The JSON strings assert `|3X| ≤ 3|dσ|√(Qe)` and the corresponding Young lower bound `3X ≥ −((9/2)η p²e + Q/(2η))`. This understates the Q‑dependence. Since `|grad_H Q| = Q` (verified identically, not `√Q`), Cauchy–Schwarz gives, tightly,

  `Σ_i ⟨grad Q, dU(e_i)⟩² ≤ |grad Q|² · Σ_i|dU(e_i)|² = Q² e`,

hence
  `|X| ≤ |dσ|·Q·√e`, i.e. `|3X| ≤ 3|dσ|·√(Q²e)`.

At `a=β=0`, `q=(q0,0)` the contraction is `⟨grad Q, dU(e_i)⟩ = −Q·(dU(e_i))^a`, attaining this bound when `dU` points in the `a`‑direction — so `Q√e`, not `√(Qe)`, is the sharp size. For `Q>1` the stated string is not even a valid upper estimate. The correct Young form carries `Q²`:

  `3|dσ|Q√e ≤ (9/2)η|dσ|²e + Q²/(2η)`,

so the residual forcing after absorbing `(9/2)η|dσ|²e` into the `|dσ|²`‑energy is `Q²/(2η)`, of order `Q²`, not `Q`. The distinction from the charge term is structural: `R_q` involves `D_qS` with `|D_qS|=√(2Q)|b|` (so `√Q` scaling, correctly giving `|R_q|≤√(2Qe)|b|`), whereas the exchange term involves `grad Q` with norm `Q` (so `Q` scaling). The two were conflated. The symbolic identity itself is untouched by this — only the hand‑written inequality string is affected. The consequence is important: the exchange forcing is order `Q²`, which makes the variable‑Q twisted case harder to close, not easier (see §5).

## 4. Item needing derivation: dq ↔ mixed Ricci defect coefficient

The relation `|b|² = 4|E_mix|²_HS`, hence `|b| ≤ 2√2 δ`, is stated in both JSON files, but neither script derives it. `step90_exchange`'s `maxwell_norm_residual = 4·Emix_sq − 4·Emix_sq = 0` is a placeholder, not a check. The genuine content — the coefficient in `dq = 2ρ E_mix` and the resulting factor 4 — requires the invariant mixed‑Ricci/Maxwell formula normalized to the present conventions. Step 89's SymPy did compute the mixed component `Ric(e_r,V_1) = (P_r α_z/2 − P_r λ_z + P_r σ_z + P_{rz}/2)e^{α−2λ+σ}`, and Step 88 attributes the conservation structure to the toric source with constant twist scalars in the exact case, while noting its "variable‑G stress coefficients still need translation into the present normalization." So the coefficient is at present asserted. Because `R_q` (and `|b|`) vanish identically in the exact case (`E=0 ⟹ dq=0`), this affects only the forced case, where the exchange term already dominates; still, `|b|≤2√2δ` should not be used as established until the mixed‑Ricci normalization is written out.

## 5. Central assembly: the +Qe cancellation and what it does and does not buy

**The cancellation is real and pointwise.** Two linear‑in‑Q contributions enter the orbit‑map Bochner identity:
- from the base drift curvature `Ric^4_σ = (−3+Q)γ_B + ½U*h` (Einstein‑solved sign, verified in the Step 89 integration), giving reaction `−(3−Q)e = −3e + Qe`;
- from the target derivative of the source, `⟨dU, D S_F⟩ = −Qe + 3X + R_q`, giving `−Qe`.

Both carry the identical pointwise function `Q(x)` with coefficient exactly 1, so they cancel for variable Q without any constancy assumption. The exact structured reaction is therefore

  `½Le = |DdU|² + ½|dU(∇σ)|² + det A + ½e² − 3e + 3X + R_q`,

i.e. reaction `½e² − 3e + 3X + R_q` — the same `e−6` reaction as the untwisted case, with the twist surviving only through the sign‑indefinite exchange `3X` and the charge‑derivative `R_q`. This is the correct resolution of the Step 88 (+Q "favorable") / Step 89‑intermediate (−Q "adverse") oscillation: **the leading linear twist effect on the reaction is neither; it cancels.** `step90_exchange`'s `post_cancellation_structured_reaction = e²/2 − 3e + 3X` records exactly this.

**Consistency with the Step 89 integration's `e−6+2Q` form.** The Step 89 verifier wrote `½Le ≥ ½e(e−6+2Q) + div_σV − Q²` (divergence form, keeping +Qe as a mass reduction and packaging the rest as a divergence with a `−Q²` forcing). Step 90's `½e(e−6) + 3X + R_q` is the same quantity re‑expressed: equating them gives the identity `Qe + div_σV − Q² = 3X + R_q`. Both are valid; they differ in where the twist is stored.

**Why neither decomposition closes the variable‑Q case.** The twist source has `|S_F| = |grad Q| = Q`, which is order 1, not order δ. This order‑1 magnitude is what obstructs closure, and each decomposition exposes it differently:
- **Divergence form (Step 89 route).** The flux is `V(·)=⟨dU(·),S_F⟩` with `|V| ≤ Q√e` — order 1, so the Step 87 input `|V| ≤ 2δ√e` does not transfer. Step 89 handled this by putting `f = Q + 2δ` into the resolvent forcing and reducing the mass to `κ = 6 − 2Q`, obtaining a constant‑Q crossing `Q_* ≈ 0.8986` against the floor `12 + 2Q`. This computation is internally consistent (I did not re‑run the numerics, but the algebra of `κ=6−2Q`, `K=3−Q`, and the self‑consistent ceiling is coherent). Its operative assumption is **Q constant**; the Step 89 integration itself states this and gives the conservation constraint `d(ρ G *F)=0`, `Q(x) = (1/2)ρ^{-2}c_a G^{ab}c_b`, showing Q is generically a function. A constant resolvent mass therefore requires either constant Q or uniform Q bounds plus a variable‑potential resolvent theorem that is not present.
- **Structured form (Step 90 route).** The +Qe cancels, mass returns to 6, but the exchange `3X` carries `|dσ|`, which is uncontrolled: the area equation `Lσ = 6 + Q − T` forces `|dσ| = O(1)`, and with the corrected §3 bound the exchange forcing is `O(Q²)`. So the structured route trades a mass shift for an order‑1 forcing.

Both are honest re‑packagings of an order‑1 twist source; the cancellation removes the *linear* Q reaction but not the *quadratic/first‑derivative* Q content. In consequence the number `Q_* ≈ 0.899` is a constant‑Q arithmetic value, not an established obstruction for genuine twisted connectors, and the earlier `0.77` was the sign‑error premise. **Neither is a theorem for variable Q.**

## 6. Further cancellation with the area equation

The available route is exactly Step 86 §9's combined energy `W = e + c|dσ|²`. The exchange term `3X` (order `Q|dσ|√e`) can be absorbed into the `|dσ|²e` cross term generated by the `X=|dσ|²` Bochner via the Young split, leaving a `Q²/(2η)`‑type forcing. This is structurally available but reproduces precisely the Step 86 open bootstrap: the combined‑energy reaction closes to `W²/(2(1+c)) − (3+δ)W − D + P` with a spectral/resolvent gap that decays like `B^{-1}`, so a thin high‑`e` layer with large perimeter‑to‑volume ratio is not excluded at the pointwise level. So there is **no new exact cancellation with the area equation beyond the linear +Qe cancellation**; the exchange term folds into the same unresolved bootstrap already recorded in Step 86 §7 and §9.

## 7. Exact ends versus asymptotic/forced ends

The cleanest fully‑supported statement in the free‑T² class remains the one that removes twist by structure, not by δ:
- For a complete free‑T² OT metric with two **exact** outward‑expanding cusp open sets (`F=0` on those ends), charge conservation `d(ρ G *F)=0` forces the conserved charge `c_a=0`, hence `F≡0` and `Q≡0` on the connected free region. The twisted analysis then collapses to the untwisted reaction `½e²−3e`, and the Step 88 minimal‑separator floor `sup e ≥ 12−8δ` versus the resolvent ceiling `B(δ)` gives the crossing `δ_* = 0.246249…`. The separator floor is independent of twist (its Gauss identity does not use OT), and `|II|² ≥ Q` only raises it. **This class is intact.**
- For **merely asymptotic** ends (physical `F→0` but `q≠0` as `ρ→∞`) and for **forced** connectors, `Q` need not vanish (the §2 round‑cusp envelope shows a sustained forced charge persists), so the order‑1 twist source is present and the case is open per §5–§6.

## 8. What remains unresolved for a complete forced‑twist obstruction

Stated plainly, in the free‑T² class only:

1. A **variable‑potential resolvent (or spectral‑gap) estimate** that admits an order‑1, spatially varying source `S_F=−grad Q` with `|S_F|=Q(x)`, keeping `inf_B Q` (curvature parameter `K=3−inf Q`), the source size `sup Q` (flux/forcing), and the separator average `⟨Q⟩` distinct. The present resolvent constant `2/√(3−Q+δ)` was derived under a constant mass; the artifacts do not contain the variable‑mass version, and the Step 89 integration flags this exact gap.
2. **Control of `|dσ|`** independent of the pointwise bound one is trying to prove — equivalently, closing the Step 86 §9 `W`‑bootstrap so the exchange `3X` (with the corrected `Q√e|dσ|` size) is absorbed. Without it, the structured reaction `½e²−3e+3X+R_q` does not yield a pointwise ceiling.
3. The **invariant coefficient `dq = 2ρ E_mix`** in the present normalization (§4), needed before `|b|≤2√2δ` may be used; this controls `R_q` in the forced (not exact) case.
4. The **full‑M identification** of the reduced Einstein twist stress with `−grad_H Q` (verified at the canonical point and via generic‑jet derivative structure; the arbitrary‑orientation index derivation is not written in these files, though it is standard in the charged harmonic‑map reduction).

None of the above extends beyond the free‑T² class, and — as recorded in Steps 86 and 88 — even a complete obstruction here would not touch the diffuse non‑OT S³‑neck mechanism or the general graph‑manifold setting, and so would not by itself settle either direction of the full problem.

## 9. Two concrete corrections to fold into the record

- The exchange inequality string `|3X| ≤ 3|dσ|√(Qe)` and the Young forcing `Q/(2η)` should read `|3X| ≤ 3|dσ|·Q√e` and `Q²/(2η)` (§3); `|grad_H Q| = Q`, verified identically, is the reason.
- The `|b|² = 4|E_mix|²_HS` relation is currently a placeholder (`4·Emix_sq − 4·Emix_sq = 0`); it needs the mixed‑Ricci normalization to become a derived coefficient (§4).

Everything else in Steps 89–90 that I checked reproduces correctly, and the +Qe cancellation is a real and useful clarification of the twist reaction.
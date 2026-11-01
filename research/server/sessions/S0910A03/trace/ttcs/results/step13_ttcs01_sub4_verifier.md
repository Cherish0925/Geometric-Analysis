# TTCS Independent Branch Record

```json
{
  "step_id": 13,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/scripts/verify_einstein_defect_evolution.py",
    "Sessions/S0910A03/workspace/notes/step12_reduced_equations_accessibility.md"
  ]
}
```

## Task

Verify the following claim about the Einstein defect evolution under normalized Ricci flow. For the flow d/dt g = -2(Ric + g), define E = Ric(g) + g. The claim is: d/dt E = Delta_L E - 2E, where Delta_L is the Lichnerowicz Laplacian. Furthermore, the squared norm satisfies (d/dt - Delta)|E|^2 = -2|nabla E|^2 + 4 R_{ikjl} E_{ij} E_{kl}. The derivation uses: (1) contracted Bianchi identity div(E) = (1/2) d(tr E) to cancel the Hessian-of-trace terms in the variation formula; (2) substitution R_{ik} = E_{ik} - g_{ik} to cancel tr(E^3) and |E|^2 terms in the |E|^2 evolution. Check each step for correctness. Then assess the consequence: under Ye Li's smoothing (which gives |Rm(g(t))| <= C/t for t in (0, T)), the Gronwall estimate for sup|E(t)|^2 gives a growth factor exp(int_0^{t_0} 4C/t dt) = exp(4C log(t_0/0)) = infinity, so the Einstein defect is NOT controlled pointwise through the flow. Is this analysis correct? Are there alternative estimates (using integral norms, parabolic regularity, or the -2E damping term) that could circumvent this gap?

## Output

## Verification memo: Einstein-defect evolution under normalized Ricci flow

I checked both tensor identities by independent hand computation using the standard linearization of Ricci, then examined the time-integral argument and the alternatives. The two identities are correct. One statement inside Part 3 of the script is internally inconsistent with the identity the script itself proves in Part 2, though it does not change the divergence conclusion. The interesting mathematical content is in the alternatives, where the sup-norm divergence is a norm-specific artifact rather than an intrinsic obstruction.

### 1. Identity `d/dt E = Δ_L E − 2E` — correct

I used the linearization of Ricci under `∂_t g = v`:

`2 ∂_t R_ij = −Δ_L v_ij − ∇_i∇_j(tr v) + ∇_i(div v)_j + ∇_j(div v)_i`,

which I confirmed against the canonical special case `v = −2Ric` (unnormalized flow), where the trace and divergence terms cancel and one recovers the known `∂_t Ric = Δ_L Ric`. This fixes the sign convention the script uses (its stated formula is exactly `2×` this).

Now with `v = −2E = −2(Ric + g)`:
- `tr v = −2(s + n) = −2 tr E`, so `−∇_i∇_j(tr v) = +2∇_i∇_j s` (since `n` is constant, `∇(tr E) = ∇s`).
- Contracted Bianchi: `div(Ric) = ½ ds`, `div(g) = 0`, hence `div(E) = ½ ds = ½ d(tr E)`, so `(div v)_j = −∇_j s`, giving `∇_i(div v)_j + ∇_j(div v)_i = −2∇_i∇_j s`.
- `−Δ_L v = +2Δ_L E`.

Summing: `2∂_t R_ij = 2Δ_L E_ij + 2∇_i∇_j s − 2∇_i∇_j s = 2Δ_L E_ij`, so `∂_t R_ij = Δ_L E_ij`. Adding `∂_t g_ij = −2E_ij` gives `∂_t E = Δ_L E − 2E`. The Hessian-of-trace cancellation via contracted Bianchi is exactly as the script describes. **Correct.**

### 2. Identity `(∂_t − Δ)|E|² = −2|∇E|² + 4 R_{ikjl}E_{ij}E_{kl}` — correct

`∂_t|E|² = 2⟨∂_t E, E⟩ + (∂_t g^{ik}g^{jl})E_{ij}E_{kl}`, with `∂_t g^{ik} = +2E^{ik}` giving the metric-variation term `+4 tr(E³)`.

From `2⟨Δ_L E, E⟩ = Δ|E|² − 2|∇E|² + 4R_{ikjl}E_{ij}E_{kl} − 4R_{ik}E_{ij}E_{kj}` and the `−2E` term contributing `−4|E|²`, substitute `R_{ik} = E_{ik} − g_{ik}`:

`R_{ik}E_{ij}E_{kj} = tr(E³) − |E|²` (I verified `E_{ik}E_{ij}E_{kj} = tr(E³)` as `tr(E·E²)`, and `g_{ik}E_{ij}E_{kj} = |E|²`).

So `−4R_{ik}E_{ij}E_{kj} = −4 tr(E³) + 4|E|²`. Collecting the reaction terms:

`+4 tr(E³)` (metric variation) `− 4 tr(E³) + 4|E|²` (Lichnerowicz) `− 4|E|²` (damping) `= 0`.

Every `tr(E³)` and `|E|²` term cancels, leaving `(∂_t − Δ)|E|² = −2|∇E|² + 4R_{ikjl}E_{ij}E_{kl}`. **Correct**, matching the script's Part 2.

### 3. Internal inconsistency in Part 3 (`−2` linear damping)

Part 2 proves that the linear `−4|E|²` damping **cancels exactly** against the `+4|E|²` produced by the background Ricci `≈ −g` acting through the Lichnerowicz zeroth-order term. The final `|E|²` equation therefore carries **no linear damping**. Equivalently, rewriting the tensor equation with `R_{ik} = E_{ik} − g_{ik}`:

`∂_t E = ΔE + 2R_{ikjl}E_{kl} − 2(E²)_{ij}`,

the `+2E` from `−(R_{ik}E_{kj}+R_{jk}E_{ki})` at the background exactly annihilates the `−2E` damping; what survives is the *quadratic* `−2E²`, which is sign-indefinite and negligible for small `E`.

Consequently the Part-3 model ODE `df/dt = (−2 + 4C/t)f` mislabels a linear damping that Part 2 already showed does not exist; the consistent model is `df/dt = (4C/t)f` (with at most a nonlinear `−2 tr(E³)` correction). This matters for interpretation: the Part-6 narrative "favorable damping `−2E` drives `E → 0`" and "Einstein is a stable fixed point when curvature is bounded" is not supported by the `|E|²` identity. Genuine linear decay of `E` near an Einstein metric with `Ric = −g` requires `Δ_L < 2` on the relevant deformation modes — a spectral property of `Δ_L` on that Einstein background, not an automatic consequence of the `−2` coefficient. The cancellation in `|E|²` is precisely the signature of marginal (neutral) behavior in that norm.

This inconsistency does **not** alter the divergence conclusion: with or without a spurious `−2`, the factor `(t₀/ε)^{4C}` diverges because the `4C/t` term is what drives it and `exp(−2(t₀−ε))` stays `O(1)`.

### 4. The time-integral divergence — correct as a statement about the sup-norm maximum principle

Bounding `4R_{ikjl}E_{ij}E_{kl} ≤ c|Rm||E|²` (dimensional constant `c`; writing `4` is convention-dependent and inessential) and applying the scalar maximum principle to `f(t) = sup_x|E|²`:

`d/dt f ≤ (4C/t) f`  ⟹  `f(t₀) ≤ f(ε)(t₀/ε)^{4C}`.

Since `∫_0^{t₀} dt/t = ∞`, the amplification `→ ∞` as `ε → 0`, and equally the forward estimate from `t = 0` has a non-integrable coefficient at the lower limit. The `sympy` `dsolve` outputs are consistent with this. The informal `log(t₀/0)` in the task text is a shorthand for this divergent integral; the substance is correct. So the sup-norm maximum principle with the crude bound `|Rm| ≤ C/t` does not control `E` across `t → 0`. **Correct.**

The essential point is that this is a statement about one particular estimate in one particular norm, not a theorem that `E` is uncontrolled. The non-integrability comes entirely from replacing the actual curvature by its pointwise upper envelope `C/t`; that envelope is realized only on small concentrating sets.

### 5. Alternatives that address the divergence

**(a) Critical `L²` energy in dimension 4 — the most promising.** The reaction integrated is `∫_M 4R_{ikjl}E_{ij}E_{kl} ≤ 4(∫_M|Rm|²)^{1/2}(∫_M|E|^4)^{1/2}`. The Ye Li hypothesis (Theorem 3.6, `0911.3104`) is exactly a control on the *scale-invariant* quantity `r⁴ fint_{B_r}|Rm|²`; in dimension 4 `∫_M|Rm|²` is scale-invariant and need not blow up like `1/t²` even though `|Rm|_∞ ~ C/t`, because the pointwise blow-up concentrates on sets of small volume. If `∫_M|Rm|²(t) ≤ Λ` uniformly, then

`d/dt ∫_M|E|² ≤ −2∫|∇E|² + 4Λ^{1/2}‖E‖_{L^4}²`,

and the dimension-4 Sobolev/Gagliardo–Nirenberg inequality `‖E‖_{L^4}² ≲ ‖∇E‖_{L²}‖E‖_{L²} + ‖E‖_{L²}²` lets the good term `−2∫|∇E|²` absorb the reaction when `Λ` is small enough (which is exactly the smallness the smoothing hypothesis supplies). This is the standard Moser/energy mechanism, and it closes precisely in the regime where the sup-norm argument diverges. The time-integrability improves because the driving norm is `(∫|Rm|²)^{1/2}` (a bounded, scale-critical quantity) rather than `sup|Rm| = C/t`. This is the concrete route worth developing, and it is directly compatible with the step-12 note's own observation (Part 9) that the calibrated energy density is the natural small quantity.

**(b) Shi-type parabolic regularity does not cross `t = 0`.** Once `|Rm| ≤ C/t`, derivative estimates `|∇^k Rm| ≤ C_k/t^{1+k/2}` hold, and `E` obeys a parabolic equation with these coefficients. Local parabolic estimates on `[t₀/2, t₀]` control `E(t₀)` from `E(t₀/2)` cleanly. But this only relocates the difficulty to `[0, t₀/2]`; the accumulation as `t → 0` is untouched. So interior parabolic regularity alone does not bridge the initial time.

**(c) `C⁰` metric equivalence transfers structure, not pointwise `E`.** Ye Li's `|v|_{g(0)} < √2 |v|_{g(t)}` (used in the step-12 two-layer note) carries volume, distance, and fibration/topological data from `g(t)` back to `g(0)` without ever preserving `sup|E|`. For the research program the transferable object is metric-measure/structural information, and the divergent sup-norm estimate is not the operative obstruction to that transfer.

**(d) Monotone-functional route.** "Almost-Einstein implies close to Einstein" statements in the literature are driven by monotonicity of entropy-type functionals of `Ric + g` along the flow, again bypassing pointwise Gronwall.

### Summary for use

- Both tensor identities `∂_t E = Δ_L E − 2E` and `(∂_t − Δ)|E|² = −2|∇E|² + 4R_{ikjl}E_{ij}E_{kl}` are correct; the Bianchi cancellation and the `R = E − g` substitution are both valid.
- The sup-norm maximum-principle estimate genuinely diverges under `|Rm| ≤ C/t`, because `∫_0 dt/t = ∞`. This part of the analysis is sound.
- The Part-3/Part-6 language attributing linear damping to `−2E` in the `|E|²` equation contradicts Part 2, where that damping cancels; the surviving nonlinear term is `−2 tr(E³)`. Fix this wording, and note that fixed-point stability actually rests on the spectrum of `Δ_L` on the `Ric = −g` background.
- The divergence is specific to the sup norm with the pointwise curvature envelope. An `L²` energy estimate in dimension 4, using the scale-critical `∫|Rm|²` bound the smoothing hypothesis already provides together with the `−2|∇E|²` term and Sobolev absorption, is the concrete construction that can control the integral norm of `E` where the pointwise argument does not. Whether `∫_M|Rm|²(t)` stays uniformly bounded (rather than growing) along the Ye Li flow is the one quantitative input this route needs and is not yet established in the supplied material; that is the precise unresolved point to settle before the energy estimate can be asserted.
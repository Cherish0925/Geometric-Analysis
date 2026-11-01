# TTCS Independent Branch Record

```json
{
  "step_id": 91,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step88_reflection_free_minimal_separator.md",
    "Sessions/S0910A03/workspace/notes/step90_structured_forced_twist_and_radial_escape.md",
    "Sessions/S0910A03/workspace/notes/step85_bochner_comparison_theorem.md",
    "Sessions/S0910A03/workspace/data/step91_flat_slice_and_stability.json"
  ]
}
```

## Task

Verify the following geometric claim about free-T² metrics with twist on a 4-manifold. Setting: (X⁴,g) complete, free isometric T²-action, g = γ_B + G_ab(dξ^a + A^a)(dξ^b + A^b), G = e^σ M with det M = 1, ρ = e^σ. Connection curvature F^a = dA^a = f^a vol(γ_B). Twist energy Q = (1/2)G_{ab}f^af^b. Orbit-shape map U: B → H² with e = |dU|². Defect E = Ric_g + 3g, ‖E‖_op ≤ δ.

Claim 1 (twist contribution to |II|²): Let Σ = π⁻¹(C) be an invariant hypersurface, C a curve in the base B with tangent T and normal ν. In the orthonormal frame {e_T, e₁, e₂, e_ν}, the second fundamental form satisfies:
  |II|² = |II|²_OT + Q
where |II|²_OT = κ² + (1/2)h_ν² + (1/2)e_ν (with κ = geodesic curvature, h_ν = ∂_ν σ, e_ν = |dU(ν)|²) and the twist contribution is Q through the off-diagonal terms II(e_T, e_a).

Verify: From the Kaluza-Klein/O'Neill formulas, II(e_T, e_a) = (1/2)G_{aa}^{1/2}f^a (in orthonormal orbit frame, for diagonal G). Then 2∑_a II(e_T,e_a)² = (1/2)G_{ab}f^af^b = Q.

Claim 2 (separator stability): If Σ is minimal and area-minimizing in its homology class, then ∫_Σ(|II|² + Ric(ν,ν))dvol ≤ 0 (second variation with φ=1). Since Ric(ν,ν) = -3 + E(ν,ν) ≥ -3 - δ:
  ⟨|II|²⟩_Σ ≤ 3 + δ
and hence Q_C := ⟨Q⟩_Σ ≤ 3 + δ.

Claim 3 (raised floor): The separator identity from Step 88 gives ⟨e_s⟩ = 12 - 2⟨D⟩ + 2⟨|II|²⟩ + ⟨h²⟩ where h = (log ρ)_T. With |II|² = |II|²_OT + Q, this becomes ⟨e_s⟩ ≥ 12 - 8δ + 2Q_C.

Claim 4 (resolvent-floor obstruction): At the exact OT threshold δ* ≈ 0.246 where the Step 87 ceiling B(δ*) = 12 - 8δ*, any Q_C > 0 would make the floor strictly exceed the ceiling, ASSUMING the ceiling still applies. However, the ceiling B(δ) was derived under Q=0 (exact OT). With Q>0, the Bochner identity is modified and the ceiling may increase. The key question is whether the ceiling increases faster or slower than the floor.

Please verify all four claims, check the O'Neill formula for II(e_T, e_a) carefully, and assess whether the resolvent-floor argument genuinely constrains Q_C or whether the modified ceiling with Q>0 invalidates it.

## Output

## Verification memo: twist contribution to the minimal separator and the resolvent-floor argument

I checked the four assertions against the O'Neill/Kaluza–Klein geometry, the Step 88 separator identity, the Step 85–87 Bochner material, and the arithmetic recorded in `step91_flat_slice_and_stability.json`. Assertions 1–3 are correct and mutually consistent; I reconstruct them below with the factors made explicit. Assertion 4 correctly identifies that the resolvent-floor combination does not constrain `Q_C`, and I give the quantitative reason the modified ceiling outruns the floor.

### Assertion 1 — the twist term in |II|² (correct, and true for general G)

Set the base orthonormal frame `(T,ν)` with `vol_{γ_B}(T,ν)=1`, so `F^a(T,ν)=f^a`. Let `K_a=∂_{ξ^a}` be the fundamental fields, `g(K_a,K_b)=G_{ab}`, and `e_â=(G^{-1/2})_a{}^c K_c` the orbit orthonormal frame. The unit normal of `Σ=π⁻¹(C)` is the horizontal lift `e_ν`.

Using the O'Neill integrability tensor `A_XY=½ v[X̃,Ỹ]` for horizontal lifts and the skew identity `g(A_XY,V)=-g(A_XV,Y)`:

- `A_Tν = ½ v[T̃,ν̃] = -½ Σ_a f^a K_a` (abelian curvature: `v[T̃,ν̃]=-F^a(T,ν)K_a`).
- `II(e_T,e_â) = g(∇_{e_T}e_â,e_ν) = g(A_{e_T}e_â,e_ν) = -g(A_{e_T}e_ν,e_â) = ½ (G^{1/2}f)_a`.

For diagonal `G` this is `II(e_T,e_â)=½√{G_{aa}} f^a`, matching the stated formula and the JSON entry `II(e_T,e_1)=(1/2)sqrt(G_11)*f1`. Summing the off-diagonal pairs,
$$
2\sum_a II(e_T,e_â)^2 = 2\cdot\tfrac14 f^T G f = \tfrac12 G_{ab}f^af^b = Q,
$$
and this holds for **non-diagonal** `G` as well (the general step `∑_a[(G^{1/2}f)_a]^2 = f^TGf`), so the invariant content is robust, not tied to a diagonal ansatz.

I also confirmed that twist does not perturb the other blocks, which is what makes the additive split `|II|²=|II|²_OT+Q` legitimate:
- `II(e_T,e_T)`: the vertical `A_{e_T}e_T=½v[T̃,T̃]=0`, so only the base geodesic curvature survives, giving `κ`.
- `II(e_â,e_b̂)`: Koszul with the Killing fields and connection-invariance of `e_ν` gives `g(∇_{K_a}K_b,e_ν)=-½ e_ν(G_{ab})`, which depends on the normal derivative of the fiber metric only, not on `A`.

The vertical block decomposition also reproduces `|II|²_OT` cleanly. Writing `G=e^σM`, the orthonormal vertical shape operator is `S=-½[σ_ν I + M^{-1/2}M_νM^{-1/2}]`, whose trace part is `-h_ν` and whose traceless part carries `¼\,tr((M^{-1}M_ν)^2)=½ e_ν`. Hence `|S|²=½h_ν²+½e_ν`, and together with `κ²` this is exactly `|II|²_OT`. **Assertion 1 verified.**

### Assertion 2 — separator stability bound (correct, with two conditions that Step 88 supplies)

`Σ=π⁻¹(C)` is a closed 3-manifold (`T²`-bundle over the essential loop `C`), so `φ≡1` is admissible in the second variation
$$
\delta^2A(1)=-\int_\Sigma(|II|^2+\mathrm{Ric}(ν,ν))\,dv \ge 0.
$$
With `Ric(ν,ν)=E(ν,ν)-3\ge-3-δ`, this gives `⟨|II|²⟩_Σ\le 3+δ`, hence `Q_C=⟨Q⟩\le⟨|II|²⟩\le 3+δ`. Two points make this rigorous and I confirmed both hold in the Step 88 construction:

1. **Stationarity/stability under `φ≡1`.** The Step 88 separator is the minimizer of weighted length `∫_Cρ\,ds` = 3-volume among invariant hypersurfaces. `φ≡1` is an invariant normal variation (moving `C` in `B`), so minimality among invariant competitors already forces `δ²A(1)\ge0`. One does not need full stability against non-invariant deformations for this test function.
2. **Measure identity.** `dv_Σ = ρ\,ds\times(\text{const torus volume})` since `√{\det G}=e^σ=ρ`. Therefore `⟨\cdot⟩_Σ` with the induced 3-volume equals the `ρ`-weighted average `⟨\cdot⟩_C` used elsewhere. `Q` and `|II|²` are `T²`-invariant (functions on `B`), so the averages coincide.

The JSON records `Q_C ≤ 3 + δ` and `<|II|^2>_C ≤ 3 + δ` consistently. **Assertion 2 verified.**

### Assertion 3 — the raised floor (correct, and consistent with Step 88 §2.1)

The Step 88 identity (2.5), `⟨e_s⟩=12-2⟨D⟩+2⟨|II|²⟩+⟨h²⟩`, uses `R_g-2Ric(ν,ν)=D-6` (exact, from `E=Ric+3g`) and the intrinsic `⟨R_q⟩=½(⟨h²⟩-⟨e_s⟩)`. I checked that turning on twist does not disturb the intrinsic side: the connection restricted to `Σ` is flat because `F^a=f^a\,ds\wedge dn` pulls back to zero on `Σ` (which omits the normal direction), so `R_q` retains the form (2.3). Only the extrinsic `|II|²` gains `+Q`. With `|D|\le4δ`, `⟨h²⟩\ge0`, `|II|²_OT\ge0`,
$$
⟨e_s⟩ \ge 12-8δ+2Q_C,\qquad \sup_B e \ge ⟨e_s⟩\ge 12-8δ+2Q_C .
$$
This is internally consistent — `R_q` unchanged, `|II|²` raised by `Q`, and the ambient `R_g`, `Ric(ν,ν)` absorb the twist so the Gauss equation stays an identity. **Assertion 3 verified.**

### Assertion 4 — the resolvent-floor combination does not constrain `Q_C`

The concern raised is the decisive one, and the material supports it strongly. The ceiling `B(δ)` (Step 87/88 eq. 4.4) and the crossing `δ_*≈0.24625` are objects derived at `Q=0`. Feeding a `Q>0` floor into that `Q=0` ceiling — which is exactly what the JSON block `resolvent_floor_combination` does (`Q_C_max_resolvent = 0.0` for every listed `δ`) — is not a valid comparison, for three reasons.

**(i) The ceiling rises with twist, and faster than the floor.** The correct twist-modified comparison is Step 90 eq. (3.4),
$$
12+2Q_C-8δ \le \Big[\tfrac{2(Q_++2δ)}{\sqrt{3-Q_-+δ}}+\sqrt{2(3-Q_-+δ)+\tfrac{5(Q_++2δ)^2}{3-Q_-+δ}}\Big]^2 .
$$
It reduces to `B(δ)` at `Q_+=Q_-=0` (the `5(2δ)²=20δ²` and `2(2δ)/\sqrt{3+δ}` terms recover eq. 4.4). Differentiating the right side at `Q=0` (small `δ`, `a=3+δ≈3`) gives `∂(\text{ceiling})/∂Q_+ ≈ 4\sqrt2 ≈ 5.66`, whereas the floor rises at rate `2` in `Q_C`. For large `Q_+` the ceiling behaves like `≈6\,Q_+^2`, purely quadratic, while the floor stays linear. So under any uniform-`Q` reading the ceiling outpaces the floor immediately, and the specialized crossing indeed moves outward — Step 90 records it going from `0.246` to `0.8986` in the `Q(x)\equiv q` specialization. Twist relaxes the obstruction rather than reinforcing it.

**(ii) The floor and ceiling depend on different functionals.** The floor uses `Q_C` (the `ρ`-weighted separator average). The ceiling uses `Q_+=\sup_B Q` and `Q_-=\inf_B Q`. These are independent: the stability bound of Assertion 2 controls only `Q_C`, and says nothing about `Q_+`. With exact outward-expanding `OT` ends, `Q_-=0`, so the global curvature parameter in the ceiling stays `3+δ`, while `Q_+` is unconstrained. No single-variable comparison exists without a further theorem tying `Q_+` to `Q_C` (equivalently, a variable-potential resolvent estimate whose ceiling depends on `Q_C` rather than `Q_+`). Step 90 states this explicitly: no one of `Q_-,Q_+,Q_C` can be collapsed into a single `Q_max`, and the Step 87 Fisher/Beta computation does not admit a spatially varying mass without new work.

**(iii) Large `Q_+` is exhibited concretely.** Step 90 §6–7 integrates the exact reduced Einstein system for a charged radial core and reaches `r=4` for `Q_0=0.1,…,100`, with every solution redshifting to a near-`OT` end (`Q→0`, `u→2`, `H→1`). It then discharges `w=\sqrt{2Q}` to zero with `\max|b|=O(δ)` mixed forcing and only `O(δ^2)` residual in the remaining horizontal equation (27 sampled collars, all with `‖E‖_{op}<0.925δ`). This means the local regular family permits arbitrarily large interior `Q_+` while keeping `Q_-→0` at the ends and small operator defect — precisely the situation in which the `Q=0` ceiling cannot be invoked and the modified ceiling sits far above the floor.

**Assessment of Assertion 4:** correct. The resolvent-floor combination as tabulated does not genuinely bound `Q_C`; it is the `Q=0` ceiling applied illegitimately to a `Q>0` floor. Note additionally that the flat-slice entry in the same JSON (`H² lower bound 9-6δ`, barrier `δ≥3/2`) is a separate, self-contained pointwise statement for a *radial cylindrical* charged throat and does constrain that specialized geometry; it is independent of the resolvent argument and should not be conflated with it.

### What would be needed to close the twisted case

The three verified pieces (Assertions 1–3) plus Assertion 2 deliver a real, correct partial structure: twist adds exactly `Q` to `|II|²`, stability bounds the separator average `Q_C\le3+δ`, and the separator floor is raised to `12-8δ+2Q_C`. What is absent is any control of `Q_+` (or a resolvent/Bochner ceiling whose right side is governed by `Q_C` and `Q_-` rather than `Q_+`) that stays below `12-8δ+2Q_C`. Given item (i), such a ceiling would have to grow in `Q_+` at a rate below `2` per unit `Q_C` with `Q_+\ge Q_C` — the opposite of the observed `≈5.66`/quadratic growth. The Step 90 radial family provides an explicit obstacle to any hoped-for `Q_+=O(δ)` estimate drawn from mixed-Ricci control and one exact `OT` end. So the correct reading is that the twist extension is open, and the specific resolvent-floor closure attempted in `step91` does not obstruct it.

One foundational note carried in from Step 87: the resolvent gradient estimate (eq. 4.3) is stated there as an upper estimate, not a proved equality. Even the `Q=0` ceiling `B(δ)` therefore rests on that estimate; the present task's arithmetic is downstream of it and does not re-establish it.
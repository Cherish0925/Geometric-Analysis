# TTCS Independent Branch Record

```json
{
  "step_id": 30,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A02/workspace/notes/step30_route_reassessment_noncollapsed_bubble_variational.md",
    "Sessions/S0910A02/workspace/data/step30_noncollapsed_bubble_variational_audit.json",
    "Sessions/S0910A02/workspace/notes/step8_preceptor_review_positive_branch.md",
    "Knowledge/objects/papers/Integrability-of-Einstein-deformations-and-desingularizations--8e63541ce32f--b5af64ba3e90/object.md"
  ]
}
```

## Task

Develop sharper mathematical construction routes for the Step-30 variational Pohozaev/Komar bridge. We need ideas that could turn C^0 Ricci pinching in a noncollapsed four-dimensional ALE/orbifold bubble annulus into the Ozuch/Biquard first-obstruction projection R_+ v=0, ideally using minimizers of int |L_Z g|^2 or related divergence-free pairings rather than full curvature smoothing. Propose concrete lemmas, model problems, scale choices, and falsifying tests that Agent2/Agent3 can execute next. Preserve the exact Yau-26 target and do not claim final success.

## Output

## Sharpening the Step‑30 variational Pohozaev/Komar bridge

The exact Yau‑26 target is unchanged: for every `n≥2`, decide whether dimension‑only `c_n<C_n` force any closed connected smooth `M^n` with `c_n g≤Ric_g≤C_n g` to carry some Einstein metric. What follows develops the noncollapsed four‑dimensional positive branch and does not assert that branch is settled.

### 1. The backbone: an exact flux identity for a `C^0`‑Ricci‑safe divergence‑free tensor

The right object to transport across a neck is the fully nonlinear modified Einstein tensor, not any formal second variation. In the positive normalization (`Ric_g≈g`, `n=4`) set
`𝓔_g := Ric_g − ½ s_g g + g`.
This is divergence‑free for the genuine metric `g` (contracted Bianchi: `δ_g(Ric−½s g)=0`, `δ_g g=0`), it vanishes identically on `Ric=g`, and under `‖Ric_g−g‖_op≤δ` it is pointwise small: `‖𝓔_g‖_op ≤ δ + ½·4·δ = 3δ`, `tr_g 𝓔_g = 4−s_g = O(δ)`. This is the crucial contrast with `Ric_g−g`, which is not divergence‑free once `s_g` varies.

Applying Ozuch's Lemma 1.4 to the divergence‑free `T=𝓔_g` and any vector field `Z` gives, on any annulus `Ω={r_1≤r≤r_2}`, the **exact** relation

  `F_Z(r_2) − F_Z(r_1) = ½ ∫_Ω ⟨𝓔_g , 𝓛_Z g⟩_g dV_g`, where `F_Z(r):=∫_{Σ_r} 𝓔_g(Z,ν_g) dA_g`.

No smallness, gauge, or normal form is used. The right side is majorized by `½‖𝓔_g‖_{L^∞}·‖𝓛_Z g‖_{L^1} ≤ (3/2)·δ·E`, `E:=‖𝓛_Z g‖_{L^1(Ω)}`. Every derivative sits on the smooth test field `Z`; no `∇Ric` ever appears. **Lemma A** is therefore already `C^0`‑Ricci‑safe and does not require the Biquard–Ozuch weighted expansion. The entire program reduces to two independent questions: (i) choose `Z` to make `E` small, and (ii) show that the two limiting values of `F_Z` encode the Biquard–Ozuch obstruction.

For the bubble side it is cleaner to use the rescaled normalization. If a bubble forms at scale `t`, put `g̃=g/t²`; then `Ric_{g̃}=Ric_g` as a `(0,2)`‑tensor, so `‖Ric_{g̃}−t²g̃‖_op≤δt²` and the Ricci‑flat‑normalized tensor `𝓔̃:=Ric_{g̃}−½s_{g̃}g̃ + t²·½·2·g̃` obeys `‖𝓔̃‖_op=O(δt²)`, `𝓔̃→0` as `t→0`. The same identity gives `F̃_Z(ρ_2)−F̃_Z(ρ_1)=½∫⟨𝓔̃,𝓛_Z g̃⟩ = O(δt²·E)`. The bubble is thus a place where the transported quantity is nearly conserved with a doubly‑small error.

### 2. Possibility I — rotation field, tensorial `R_+v` obstruction

Take `Z` asymptotic to a cone rotation Killing field `Y_i^+=ω_i^+(r∂_r)` on `ℝ^4/Γ`. The plateau mechanism is this. In the neck the metric carries an orbifold part `H_2~r²` and a bubble part `~t²H^4`, `|H^4|~r^{-4}`. The linear pieces `𝓔^{(1)}(H_2)`, `𝓔^{(1)}(H^4)` flux to zero against a Killing `Z` (Ozuch Prop 1.6(1)), so the leading surviving contribution to `F_Z(r)` in the neck is the cross term `𝓔^{(2)}(H_2,H^4)`, which is `r`‑independent and equals precisely Ozuch's Taub pairing — for the Eguchi–Hanson orientation, `∫_{S^3/Γ}Ric_e^{(2)}(H_2,H^4)(Y_i^+,∂_r)`, equivalent by Corollary 4.10 to `R_e^{+,(1)}(H_2)ω_1^+`. Lemma A says this plateau is stable across the neck up to `O(δ·E)`. Because `Z` extends to a regular harmonic vector field `Y'` on the smooth bubble core (Ozuch Prop 4.2), integrating the identity from the core outward makes the inner limit of the rescaled flux `O(δt²·E)`. Conservation across scales then forces the neck plateau, i.e. the obstruction, to be `O(δ·E)+O(t^{σ})`.

This route reaches the exact `R_+v=0` datum, but its signal is tensorial and orientation‑dependent, and the neck energy `E` must be beaten against a definite positive power of `t` (Section 4). It should be developed alongside, not instead of, the scalar route below.

### 3. Possibility II — conformal field `r∂_r`, renormalized‑volume obstruction (most robust, most decisive)

The radial flux is the higher‑value target because it produces a **single number** that is hard to cancel. Ozuch's radial obstruction (his (54)/(10)) reads `Λ·𝒱(g_b) + Q(W_b^+,W_o^-)+Q(W_b^-,W_o^+)=0`, where `𝒱(g_b)<0` strictly for any nonflat Ricci‑flat ALE bubble (Biquard–Hein reduced volume) and `Λ` is the orbifold Einstein constant at the singular point. Two structural facts make this ideal for the pinched setting:

- In the positive branch the limit orbifold is Einstein with `Λ≈+1>0` after normalization. So `Λ·𝒱(g_b)` is a definite negative number bounded away from zero by the bubble's quantized `L^2` curvature energy.
- At any singular point where the orbifold Weyl curvature is small (conformally‑flat‑type point), the `Q` terms are small and the obstruction cannot vanish: `Λ𝒱(g_b)≈0` is impossible. This is exactly Ozuch's Corollary 4.11 driving Theorem 0.9 (spherical/hyperbolic orbifolds admit no smooth Einstein desingularization).

The mechanism for Yau‑26: use `Z` asymptotic to `r∂_r` (with `δ_e^*(r∂_r)=e`, so `𝓛_{r∂_r}g` measures exactly the departure of `g` from radial homothety). Lemma A transports the radial flux `F_{r∂_r}(r)` across the neck with error `O(δ·E)`. The inner rescaled limit is `O(δt²·E)` on the smooth core; the outer limit computes the orbifold's `Ric_e^{(2)}(H_2,H^4)(r∂_r,∂_r)` pairing, which by Ozuch's Remark 0.5 equals `c(Λ𝒱(g_b)+ Weyl terms)`. Near‑conservation then forces

  `Λ·𝒱(g_b) = −Q(W_b^+,W_o^-)−Q(W_b^-,W_o^+) + O(δ·E)+O(t^{σ})`.

This is a genuine constraint every pinched positive‑branch bubbling must obey: the bubble's renormalized volume is tied to the orbifold Weyl curvature at `p`. Where the orbifold singular point is close to conformally flat, `Λ𝒱(g_b)` must be near zero while `𝒱(g_b)` is bounded below in magnitude and `Λ≈1` — a contradiction that would exclude bubbling there. The scalar nature means the argument needs only the sign of `Λ` and the strict negativity/size of `𝒱`, not the full tensorial normal form. This is the sharpest place to press.

### 4. The variational field is Ozuch's harmonic extension; coercivity converts `C^1` closeness into curvature‑order energy

Minimizing `J(Z)=∫_Ω|𝓛_Z g|²=4∫|δ_g^*Z|²` with prescribed cone asymptotics has Euler–Lagrange equation `δ_g δ_g^* Z=0` — precisely the harmonic vector field `Y'` (resp. `X` for `r∂_r`) that Ozuch constructs (Props 4.1–4.2). So the variational object is not an ad hoc device; it is the canonical field that makes the deformation `𝓛_Z g` an actual infinitesimal deformation, decaying like the bubble curvature (`r^{-4}` in CMC gauge) rather than like a raw cutoff error.

The quantitative payoff is a coercivity statement. On the ALE model annulus, `δ_g δ_g^*` is invertible on fields decaying at infinity (Ozuch Lemma B.2 with weight `β∈(0,2)`), so the minimizer with asymptotic `Y` obeys
  `‖Z−Y‖_{C^{2,α}_β} ≤ C‖δ_g δ_g^* Y‖`.
For a cone Killing/conformal field `Y`, the forcing `δ_g δ_g^* Y` vanishes on the exact model and equals a curvature‑order pairing on `g` (via the Bochner relation `∇^*∇Y − Ric(Y)` controlling failure to be Killing). Hence `E=‖𝓛_Z g‖_{L^1}` is bounded by curvature‑order quantities of `g`, not by raw annular `C^1` closeness `η`. This is the precise resolution of the Step‑30 scaling worry: the transplant contributes `η²r^4` competing with the `t^4`‑type signal and demands `η≪t^2/r^2`, whereas the minimizer's error is set by an energy minimum tied to the concentrated curvature. The decisive quantitative target becomes
  `δ_i · E_i ≪ (signal power in t_i)`,
with `E_i` controlled by Lemma C. Whether `E_i` is bounded, or grows like `log(1/t_i)`, or worse, is the single most important number the executor should pin.

### 5. Concrete model problems

- **M1 (flat‑cone calibration).** On `A={1≤r≤R}⊂ℝ^4/Γ` with `Y_i^+` and `r∂_r`, recompute Ozuch Cor 4.10 organized as the flux `F_Z(r)` of the nonlinear `𝓔_g` (not the formal `E^{(2)}`), fixing the exact constant relating `F_{Y_i^+}` to `R_e^{+,(1)}(H_2)ω_1^+` and `F_{r∂_r}` to `Λ𝒱(g_b)+Q`. Symbolic; a small Lean kernel can verify the final `3×3` algebra.

- **M2 (Eguchi–Hanson quantitative plateau).** Take the exact `eh` metric glued to a model quadratic `H_2`, perturbed to `‖Ric−g‖_op≤δ` by an explicit small conformal or trace‑free perturbation. Compute `F_Z(r)` numerically across `c√t≤r≤c^{-1}`; verify a plateau equal to the M1 obstruction with deviation `≤C·δ·E`. This fixes the true power of `t` in the signal and the constant `C`, hence the exact required relation between `δ`, `E`, and `t`.

- **M3 (variational vs transplant).** On the `eh` annulus compute `E` for (a) a cutoff rotation/radial field and (b) the minimizer solving `δ_gδ_g^*Z=0`. Verify the minimizer removes the `η²r^4` term and yields `E` bounded by curvature‑order data, confirming Lemma C empirically and measuring the actual growth of `E` in `t`.

- **M4 (renormalized‑volume radial flux).** Compute `F_{r∂_r}` for a positive orbifold point (`Λ≈1`) with a nonflat ALE bubble and verify it reproduces `c·Λ𝒱(g_b)+`Weyl terms. Then, holding the orbifold Weyl small, test whether `Λ𝒱(g_b)=O(δE)` is forced impossible — the concrete positive‑branch exclusion.

### 6. Distinguishing tests that would reveal the bridge as empty in some regime

- **T1 (energy growth).** For the minimizer on the neck, determine whether `E_i` stays below `t_i^{2}/δ_i` (equivalently `δ_iE_i≪` signal). Construct a `δ`‑pinched neck metric where `E` blows up faster than the signal permits; if the minimizer cannot avoid this in some `δ`–`t` window, that window carries no information and must be identified explicitly. If instead `E` is bounded (or grows slowly), the bridge operates.

- **T2 (hidden obstruction).** Test whether a nonzero obstruction can be masked by bubble orientation or by an `L^1`–`L^2` mismatch in the pairing. Verify `‖𝓛_Z g‖_{L^1(neck)}` for the minimizer is bounded by a geometric constant independent of the unknown `H_2`; if it re‑introduces dependence on `H_2` (i.e. on the normal form), the `C^0`‑safety of the mechanism is not yet genuine and the coercivity input must be strengthened.

### 7. What must still be established

The identity and the coercivity are robust; the structural obligations are: (i) multi‑scale bubble trees — Lemma A must be summed over a dyadic decomposition of scales, tracking `F_Z` through each neck, and the total error `ΣδE` controlled; (ii) matching the rescaled inner limit to the orbifold outer limit through the intermediate necks, using the Cheeger–Naber `C^{1,α}∩W^{2,q}` regular‑region control that bounded Ricci plus noncollapse already supplies (this is the substitute for the exact weighted normal form, and it is exactly what one is trying to survive on); (iii) selecting `Z` adapted to each bubble's `Λ^2_+` orientation and, for `r∂_r`, verifying the harmonic radial field's higher‑than‑expected agreement with `r∂_r` (Ozuch's volume‑gauge remark) persists under pinching; (iv) uniform noncollapse and uniform `δ_i→0` along the sequence so that `δ_iE_i` and `t_i^{σ}` both vanish.

The radial/renormalized‑volume route (Section 3) is the most likely to produce a decisive statement, because it converts the whole obstruction into one strictly negative number `𝒱(g_b)` weighted by a positive `Λ`, controlled against orbifold Weyl. If M4 shows that near conformally‑flat orbifold points the pinched constraint cannot be met, that excludes bubbling there and, combined with the empty‑singular‑set case already noted, moves the noncollapsed positive branch toward actual Einstein existence — one live route within the full Yau‑26 problem, not a resolution of it.
# TTCS Independent Branch Record

```json
{
  "step_id": 79,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step79_angular_rho_and_tilt_repair.md",
    "Sessions/S0910A01/workspace/data/step79_angular_rho_verify.json",
    "Sessions/S0910A01/workspace/data/step79_tilt_linearization.json",
    "Knowledge/objects/papers/Higher-order-obstructions-to-the-desingularization-of-Einstein-metrics--94f76f3b5378--19c12fb27fae/object.md",
    "Knowledge/objects/papers/Integrability-of-Einstein-deformations-and-desingularizations--8e63541ce32f--b5af64ba3e90/object.md"
  ]
}
```

## Task

Verify the Step 79 mathematical repair of the positive mixed-row product-orbifold obstruction problem. Read the repair note plus the two data files and the relevant Ozuch source excerpts. Check: (1) whether Ozuch's rho_x dependence invalidates the Step 78 fixed-rho rank-one/block-diagonal conclusions; (2) whether the factor-traceless bare scalar-decoupling theorem survives for zeta in span{omega2,omega3}; (3) whether the tilt linearization D_phi lambda=(0,c Lambda a,0) at phi0=omega2 is correctly interpreted as making mu2 adjustable and leaving the cokernel component as the actual second-order local condition; (4) whether the response to A02's r=0 KE-control argument is mathematically sound or too strong. Give a direct scientific memo with corrections and next computation priorities.

## Output

## Verifier memo — Step 79 repair of the positive product-orbifold obstruction problem

I reproduced the two scripts' central algebra by hand against Ozuch's Definition 1.14, Proposition 1.16, Lemma 2.14, and the Theorem 0.2 proof (lines 818–826). The four assertions hold. Details, one genuine cross-effect the note only half-states, and where the material stops short of the top problem, follow.

### (1) The `rho_x` correction is correct and the withdrawals are warranted

The key algebraic fact: `ρ_x` is conjugation by the unit quaternion `x` on pure quaternions (Remark 1.15), so the map `x ↦ ρ_x(ζ)` is the double cover `S³ → SO(3)`. For fixed `ζ≠0`, `ρ_x(ζ)` therefore sweeps the entire radius-`|ζ|` sphere in `ℝ³` as `x` ranges over `S³`. It is not confined to any fixed vector or to `ker R⁻`. The data corroborate this exactly: `E[ρ⊗ρ] ≈ I/3` (uniform-on-sphere second moment), `mean ρ ≈ 0`, and for `R⁻=diag(1,0,0)` the mean of `|R⁻ρ_x|` is `0.498 ≈ 1/2`, which is `E[|ρ₁|]` for a uniform unit vector. So `R⁻ρ_x` and the off-block entries of `d_eR⁻` are nonzero on a full-measure set; they vanish only on a measure-zero locus.

I verified the closed-form `ρ` components. For `ζ=ω₂` the composition matrices in the JSON give `x^T M₁ x = -2(x₁x₄+x₂x₃)`, `x^T M₂ x = -(x₁²-x₂²+x₃²-x₄²)`, `x^T M₃ x = 2(x₁x₂-x₃x₄)`, matching the printed formulas; the sample point `(0.4,0.8,-0.4,0.2)` gives `(0.48,0.36,0.8)` with unit norm, matching. The four Step 78 statements (frozen `ρ=(0,cosα,sinα)`, pointwise `R⁻ρ=0`, block-diagonal `dR⁻`, and the second-obstruction vanishing inferred from them) genuinely rest on freezing `ρ_x`, and are correctly withdrawn.

One point the note states and should keep front-of-mind: `λ_k, μ_k, ν_l` are all **integral** quantities (Prop. 2.10, 2.19, Lemma 2.14). Neither pointwise nonvanishing of `R⁻ρ_x` (shown here) nor pointwise vanishing (the frozen-`ρ` error) settles them. The correction removes a false simplification; it does not by itself move the obstruction value.

### (2) The factor-traceless statement survives, and is genuinely stronger

For `ζ⁺ = aω₂⁺ + bω₃⁺` and arbitrary `η⁻ = Σc_jω_j⁻`, `η⁻∘ζ⁺` is a linear combination of the six basis products `ω_j⁻∘ω₂⁺`, `ω_j⁻∘ω₃⁺`, each of which has zero trace on each `S²` factor (JSON `max_basis_factor_trace = 0`). By linearity in both `η⁻` and `(a,b)` the whole family is factor-traceless, so `H⁴(ζ⁺) = -ρ_x(ζ)⁻∘ζ⁺/(2r⁴)` pairs to zero pointwise with `f g₁` and `f g₂` for **every** `x` — precisely because `ρ_x(ζ)⁻` runs over all anti-self-dual directions. This is stronger than any frozen-`ρ` version.

The contrast that makes this meaningful, and that I checked directly: `ω₁⁺∘ω₁⁻ = diag(-1,-1,1,1)`, whose factor traces are `(-2,+2) ≠ 0`. So the EH/curvature direction `ω₁` does couple to the shape scalar `g₁-g₂`; only the in-kernel directions `span{ω₂,ω₃}` decouple. The statement is exactly a statement about the kernel of `R = diag(Λ,0,0)`, and it is correctly restricted to the bare tensor. The recorded reservation is right: the Bianchi-corrected source, the Green response on the orbifold, and the `Q^{(2)}` residual can each re-introduce scalar content; factor-tracelessness of `H⁴` is necessary, not sufficient, for scalar decoupling of the full source.

### (3) The tilt linearization and its cokernel reading are correct

I reproduced the series independently. With `φ(ε)=normalize(ω₂+ε(aω₁+bω₃))` and `R=diag(Λ,0,0)`, `Rφ = (Λaε,0,0)/N`. Using the orthonormal obstruction frame `ζ_(1)=φ`, `ζ_(2)=φ×ζ_(3)`, `ζ_(3)` the in-plane complement,

- `λ₁ = c⟨Rφ,φ⟩ = cΛa²ε² + O(ε⁴)`,
- `λ₂ = cΛaε − cΛa³ε³ − ½cΛab²ε³ + O(ε⁵)` — this matches the printed cubic terms exactly, which is a good check that the symbolic frame handling is consistent,
- `λ₃ = 0` (in this frame `ζ_(3)` has no `ω₁`-component, so it annihilates `Rφ`).

Hence `D_φλ(a,b) = (0, cΛa, 0)`. The structural reading is sound: the image of `D_φλ` is one-dimensional (the `λ₂`/out-of-kernel direction), and `b` (rotation inside `ker R`) is first-order invisible. Substituting into `tλ(φ(t)) + t²μ(φ₀) = t²(D_φλ(a,b)+μ(φ₀)) + o(t²)` gives:

- component 1: `μ₁ = 0`, not touched by the tilt, and already zero because Lemma 2.14 gives `μ₁ = C·det` of the transverse block, which for `diag(Λ,0,0)` (transverse `2×2` block `diag(Λ,0)`) has determinant zero;
- component 2: `cΛa + μ₂ = 0`, absorbable by `a = -μ₂/(cΛ)`;
- component 3: `μ₃ = 0`, the surviving cokernel condition, because `D_φλ₃ = 0`.

So the reduced second-order content is `Π_{coker Dλ} μ = 0`, i.e. `μ₃ = 0` (with `μ₁ = 0` free), not a two-number `μ₂=μ₃=0` verdict. Using `μ(φ₀)` at order `t²` is legitimate since `μ(φ(t)) = μ(φ₀)+O(t)` feeds only order `t³`. Also note that because Ozuch's estimate is `O(t^{5/2})`, the component-1 equation `tλ₁ = cΛa²t³` sits below the stated precision, consistent with `μ₁` being the only order-`t²` datum there. All correct.

**Cross-effect that deserves explicit statement.** Absorbing `μ₂` requires `a = -μ₂/(cΛ) ≠ 0`, which tilts `φ` out of `ker R` by `O(t)`. But the factor-tracelessness of (2) holds only for `ζ⁺ ∈ span{ω₂,ω₃}`; the added `aεω₁` term makes `H⁴(φ⁺)` acquire factor trace `∼ aε` through `ω₁⁺∘ω₁⁻`. So the tilt that clears `μ₂` re-introduces exactly the scalar (`g₁-g₂`) coupling that the untilted in-kernel direction avoided, at order `O(t)`. Sections (2) and (3) are therefore coupled: the surviving local problem is `μ₃(φ₀)=0` **together with** the `O(t)` scalar source generated by the mandatory tilt. The note gestures at "even scalar and negative modes" in item 6.3 but does not name this specific mechanism; it should, because it is the quantitative link between the two results.

### (4) The reply to the `r=0` Kähler–Einstein argument is sound, and correctly not over-strong

The assertion that all local `μ_k` vanish "by the `r=0` KE control" is too strong for a precise reason. A Kähler–Einstein orbifold has `R⁺` of the rank-one form `diag(0,0,Λ)` (Ozuch formula (4)); with `φ₀` in the two-dimensional kernel, the transverse block has determinant zero, so `μ₁ = 0`. But this is exactly what Lemma 2.14 already delivers — KE-ness at `r=0` reproduces the first/`μ₁` obstruction and adds nothing about the transverse `μ₂,μ₃`. In Ozuch's **generic** Theorem 0.2 proof, both transverse `λ₂,λ₃` have invertible first variation (formula (56)), so both transverse `μ₂,μ₃` are absorbed by the tilt, leaving `μ₁` as the sole survivor. In the **rank-one/kernel-dimension-2** situation here, only `λ₂` has nonzero derivative; `λ₃` starts at `ε³`. Thus `μ₃` is a transverse second obstruction that the tilt cannot absorb — the very degeneracy Ozuch flags in the introduction ("kernel dimension 2 or 3 ⟹ a 2- or 3-dimensional family Einstein to `o(t²)`"). Consequently a genuine KE desingularization would force only `Π_{coker}μ = 0` (i.e. `μ₃=0`), and even that inference presumes Ozuch's coordinates keep `φ_n` fixed to `o(t)` and that the orbifold deformation variables `v_n` enter at lower order — statements not established in the recorded material. The reply is therefore correct and appropriately measured; the reasoning it gives (transverse `μ` absorbed by `O(t)` motion of the EH direction, per lines 818–826) is the right source anchor.

### Relevance to the top problem

The whole product-orbifold/EH machinery lives in dimension 4, for Einstein-orbifold desingularization with `ℝ⁴/ℤ₂` singularities, and answers "which orbifolds arise as bubbling limits of Einstein 4-manifolds." Yau-26 asks whether Ricci pinching `c_n g ≤ Ric_g ≤ C_n g` forces existence of **some** Einstein metric `h` on the same `M`, in all dimensions and sign-unrestricted, with `h` not required near `g`. The Ozuch obstruction constrains Einstein metrics **near a specific orbifold via a specific bubbling**; it does not rule out arbitrary Einstein metrics on `M`. The logical bridge from "this configuration is obstructed" to "this `M` carries no Einstein metric while admitting a Ricci-pinched metric" is not present in the supplied material. The note's own framing as "one stress test, not a proof or refutation" matches this; the bridge itself remains to be built and is the part that would connect the branch to the research problem.

### Next computation priorities (in decreasing decisiveness)

1. **Compute `μ₃(φ₀)` for a concrete product configuration** (e.g. Ozuch Example 4.19, inside the 14-dimensional family satisfying `λ, μ₁, ν`). Since `μ₁=0` automatically and `μ₂` is absorbable, the entire local second-order content reduces to this single number. It requires the actual `underline{h}₂`, the `Q^{(2)}(underline{h}₂,underline{h}₂)` term, and — crucially — the fact that `μ^j` depends on the other nodes through `H_{j,2} ∝ |ζ|² r²` (equation (67)), i.e. through the `B^L_{j-i}` coupling matrices of Section 4. So `μ₃^j` is a function of the full `{ζ_i}`, not a purely single-node quantity.
2. **Quantify the scalar re-coupling from the `μ₂`-absorbing tilt.** With `a = -μ₂/(cΛ)`, evaluate the `O(t)` factor-trace of `H⁴(φ⁺)` and its projection onto the even shape mode `g₁-g₂` via the projected-product pseudo-inverse. This is the (2)–(3) interaction and enters at the same order the antipodal symmetry does not remove.
3. **Order-`t³` paired inter-node response**, treated together with the quadratic self-response of the first tilt; this is downstream of 1 and 2 and only matters if both clear.

Numerical/symbolic hygiene of the two scripts is good: unit-norm of `ρ_x` to `~1e-16`, `E[ρ⊗ρ]≈I/3`, and the cubic tilt series all reproduce by hand.
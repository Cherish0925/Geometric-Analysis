# TTCS Independent Branch Record

```json
{
  "step_id": 74,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/data/step70_ricci_T2inv.json",
    "Sessions/S0910A03/workspace/scripts/step74_linearized_mode_analysis.py",
    "Sessions/S0910A03/workspace/data/step74_linearized_modes.json",
    "Sessions/S0910A03/workspace/notes/step73_tail_completion_and_core_entry.md"
  ]
}
```

## Task

Verify the following derivation for the linearized Einstein equations around the flat hyperbolic cusp g0 = dt^2 + e^{2t}(dz^2 + dx^2 + dy^2), perturbed by T^2-invariant diagonal modes a=t+alpha(t)cos(kz), b=t+beta(t)cos(kz), c=t+gamma(t)cos(kz):

1. The constraint E_{01}=0 linearizes to beta'+gamma'=0, so beta+gamma=const for each k!=0 mode.
2. E_{00}=0 gives h''+2h'=0 for h=alpha+beta+gamma.
3. The anisotropy psi=beta-gamma satisfies psi''+3psi'-k^2 e^{-2t}psi=0.
4. Under x=ke^{-t}, this becomes x^2 psi_xx + 4x psi_x - x^2 psi = 0, which via psi=x^{-3/2}z reduces to the modified Bessel equation with nu=3/2.
5. The I-branch psi ~ x^{-3/2}I_{3/2}(x) is bounded as t->infinity (x->0), while the K-branch grows as e^{3t}.

Check each step. Also verify: does this BVP structure (center Neumann + cusp boundedness) give a unique solution per Fourier mode? What happens at k=0 (zero mode)? Are there corrections needed for the constraint propagation? Does the E_{11} equation actually give the correct z-derivative terms?

## Output

## Verification memo: linearized Einstein modes at the flat hyperbolic cusp

I re-derived every step from the exact `step70` Ricci components, linearizing about `a=b=c=t` with the complex mode `a=t+α(t)e^{ikz}`, etc. Three of the five stated results hold exactly; steps 4 and 5 carry a sign error in the change of variables that inverts the physical picture. Details and the corrected structure follow.

### Steps 1–3 are correct

Working to first order in `α,β,γ` (write `e=e^{ikz}`, `h=α+β+γ`):

- **E₀₀ (step 2).** `R₀₀ = -(a_t²+a_tt+…) = -3 - e(2h'+h'')`, so `E₀₀ = R₀₀+3 = -e(h''+2h')`. Vanishing gives `h''+2h'=0`. ✓
- **E₀₁ (step 1).** Only `b_z,c_z,b_{tz},c_{tz}` contribute at first order; the `a`-perturbation multiplies an already-first-order `b_z`, hence drops. Result `R₀₁ = -ik(β'+γ')e`, so `β'+γ'=0`, `β+γ=W` constant for `k≠0`. ✓
- **E₂₂−E₃₃ (step 3).** I verified the three tangential components explicitly:
  - `E₁₁/e^{2a} = -(α''+3α'+h') + k²e^{-2t}(β+γ)`
  - `E₂₂/e^{2b} = -(β''+3β'+h') + k²e^{-2t}β`
  - `E₃₃/e^{2c} = -(γ''+3γ'+h') + k²e^{-2t}γ`
  
  Subtracting the last two with `ψ=β-γ` gives `ψ''+3ψ'-k²e^{-2t}ψ=0`. ✓

On your explicit question about **E₁₁ z-derivatives**: the first-order spatial contribution is exactly `-b_zz-c_zz = k²(β+γ)e`; the products `a_z b_z`, `b_z²`, etc. are second order. So the `k²e^{-2t}(β+γ)` term the script uses is right, and the `z`-direction source is `β+γ` (not `β` or `γ` alone) — this asymmetry is genuine and correct.

### Step 4 has a sign error in the change of variables

With `x=ke^{-t}`, `dx/dt=-x`, so `ψ'=-xψ_x` and `ψ''=x²ψ_xx+xψ_x` (both agree with the script). Substituting into `ψ''+3ψ'-x²ψ=0` (using `k²e^{-2t}=x²`):

$$
x^2\psi_{xx}+x\psi_x+3(-x\psi_x)-x^2\psi
= x^2\psi_{xx}-2x\psi_x-x^2\psi=0.
$$

The script wrote `x²ψ_xx + 4x ψ_x - x²ψ = 0`; it substituted the `+3ψ'` term with the wrong sign (as if `-3ψ'`), turning `-2x` into `+4x`. The correct reduced equation is

$$
\psi_{xx}-\tfrac{2}{x}\psi_x-\psi=0 .
$$

The modified-Bessel reduction and `ν=3/2` survive, but the **prefactor exponent flips sign**. Setting `ψ=x^{3/2}w(x)` (I verified directly by substitution):

$$
x^2 w''+x w'-(x^2+\tfrac94)w=0 ,
$$

the modified Bessel equation with `ν=3/2`. Hence

$$
\psi = x^{3/2}\big[A\,I_{3/2}(x)+B\,K_{3/2}(x)\big],\qquad x=ke^{-t},
$$

with `x^{+3/2}`, not `x^{-3/2}`.

### Step 5 conclusion is reversed

Using the correct prefactor and `x→0` as `t→∞`:

- `I`-branch: `x^{3/2}I_{3/2}(x)\sim x^{3}=k^3e^{-3t}\to 0` — **decays like `e^{-3t}`.**
- `K`-branch: `x^{3/2}K_{3/2}(x)\sim\sqrt{\pi/2}\,\text{const}` — **tends to a nonzero constant.**

An independent check bypassing the substitution confirms this: as `t→∞` the potential `k²e^{-2t}\to0`, so the equation limits to `ψ''+3ψ'=0` with solutions `const` and `e^{-3t}`. **Both solutions are bounded; there is no exponentially growing anisotropy mode toward the cusp.** The claimed `e^{3t}`-growing `K`-branch does not exist as a solution — the function `x^{-3/2}K_{3/2}(x)\sim e^{3t}` that the script evaluates (see `psi_K` and the `K_branch_ratio_t10≈e^{30}` entries in `step74_linearized_modes.json`) is the solution of the *incorrect* `+4/x` equation, not of the actual ODE. The numerical `I_branch_ratio` values (integrating the correct ODE but from initial data taken from the wrong `x^{-3/2}I_{3/2}`) stay `O(1)` only because that initial data excites the constant `K`-mode; they neither validate nor represent the true `I`-branch, which decays like `e^{-3t}`.

The qualitative research message is not lost — center anisotropy is still strongly suppressed toward the cusp; in fact the pure `I`-branch attenuation is `e^{-3t}`, stronger than the `O(1)` transmission the script tabulated (`~0.2659/I_0`). But the mechanism must be restated: attenuation comes from the decaying `I`-branch, and the mode that must be removed to reach a clean cusp is the *constant* `K`-branch, not an exponential runaway.

### The center–cusp two-point problem

Because both branches are bounded, a mere boundedness demand at the cusp does **not** single out a branch. The condition that actually matches a pure flat cusp (where the `x,y` directions are isotropic, `ψ→0`) is decay `ψ→0`, which selects the `I`-branch and kills the constant `K`-branch. Paired with center reflection `ψ'(0)=0`, the homogeneous two-point problem then generically has only `ψ≡0`, so the inhomogeneous (sourced) problem is uniquely solvable per `k≠0` mode. The dimension count (unique solution per Fourier mode) can therefore stand, but the supporting statement in the script ("exclude `e^{3t}` growth") should be replaced by "require `ψ→0`, i.e. exclude the nonzero constant mode."

### The k=0 zero mode is not covered and is where the moduli live

At `k=0` the factor `k` makes `E₀₁≡0`, so the constraint `β+γ=const` is vacuous and the tangential equations reduce to `α''+3α'+h'=0`, `β''+3β'+h'=0`, `γ''+3γ'+h'=0` with `h''+2h'=0`. Their solutions include **non-decaying constant anisotropy modes** — the Bianchi-I/Kasner perturbations that change the shape of the `T²` (indeed `T³`) fiber. These are exactly the flat-torus shape moduli, and they are *not* attenuated toward the cusp. This sector is the natural home of the torus-shape degeneration discussed in `step73` §4 (the sub-zero-Yamabe `T³` conformal-infinity question), and it deserves separate treatment; the `k≠0` decay result says nothing about it.

### A constraint relation the summary omits (constraints do propagate at linear order)

Summing the three tangential equations gives `h''+6h' = 2k²e^{-2t}(β+γ)`. Compared with `E₀₀`'s `h''+2h'=0`, this forces the extra relation

$$
h' = \tfrac12 k^2 e^{-2t}(β+γ).
$$

I checked it is consistent: with `β+γ=W` constant, `h=h_0-\tfrac14k^2W e^{-2t}` satisfies both `h''+2h'=0` and the sum. So the linearized Hamiltonian/momentum constraints (`E₀₀`, `E₀₁`) do propagate consistently against the tangential equations — this is the linear counterpart of the concern raised in `step73` §5 that the reduced `(E_{tt}+E_{zz},E_x,E_y)` system need not control the remaining components. At linear order the five components are mutually consistent for the three functions, leaving four free constants per `k≠0` mode (`ψ`: 2, `W`: 1, `h_0`: 1). The script's remark "`α'=h'`" is merely the trivial restatement `α'=h'-(β'+γ')`; the genuine relation `h'=\tfrac12k^2e^{-2t}(β+γ)` linking trace evolution to the transverse trace `W` was not recorded and should be, since it fixes how the volume/trace mode is driven by the residual `β+γ`.

### Net effect on the research

The linearized system itself (steps 1–3, the `E₁₁` source, the constraint propagation) is on solid ground, and the two-point problem can still be uniquely solvable per non-zero mode. What needs correction before this supports the core-entry construction: (i) the anisotropy ODE reduces to `ψ_xx-\tfrac2x\psi_x-ψ=0` with solution `x^{+3/2}[A I_{3/2}+B K_{3/2}]`; (ii) the cusp behavior is `I`-branch `∼e^{-3t}` decay versus `K`-branch `→const`, with no exponential growth; (iii) the selection principle is `ψ→0` (kill the constant mode), and the resulting center-to-cusp transmission of anisotropy is exponentially small (`~e^{-3R}`), not `O(1)`; (iv) the `k=0` shape-moduli sector, carrying the non-decaying anisotropy, is untreated and is the physically decisive one for a `T³` cusp. Re-running `step74` with the corrected ODE (`ddp = -3*dp - k^2 e^{-2t} p` is already the correct integrand; only the closed-form `psi_I`/`psi_K` prefactors and the growth narrative need fixing) and adding the `k=0` analysis would make the mode picture match the actual equations.
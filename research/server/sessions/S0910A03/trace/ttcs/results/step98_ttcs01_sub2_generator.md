# TTCS Independent Branch Record

```json
{
  "step_id": 98,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/scripts/step98_full_matrix_joint_transition.py",
    "Sessions/S0910A03/workspace/scripts/step98_direct_spd_transition.py",
    "Sessions/S0910A03/workspace/data/step98_direct_spd_N16_interior.json",
    "Sessions/S0910A03/workspace/data/step98_center_residual_resolution.json",
    "Sessions/S0910A03/workspace/notes/step96_charged_koiso_local_evolution_and_joint_matching.md",
    "Sessions/S0910A03/workspace/notes/step94_charge_sign_correction_and_global_flux.md",
    "Sessions/S0910A03/workspace/plans/step96_route_map.md"
  ]
}
```

## Task

Given the exact charged Koiso center data and Step 98's full SPD logarithmic-matrix finite-domain formulation, develop a mathematically serious next construction/obstruction experiment that can distinguish genuine two-ended matching from low-resolution overfitting. Work directly with the supplied equations and artifacts. Seek a representation that preserves the full center q,K and both attachments, allows resolution continuation, and exposes residual projections versus inverse scales. Specify a small number of decisive computations, exact variables/boundary conditions, and what numerical scaling would reveal. Do not treat the cosh exterior as solving the inner transition and do not assume a gauge change cures elliptic Cauchy ill-posedness.

## Output

## What the Step‑98 residual is actually measuring

Before designing a new experiment it is worth separating the three distinct contributions hiding inside the reported "operator_sup 32 → 1.36" decrease, because two of them are not geometry.

**(i) The center floor is Fourier resolution, not matching.** `step98_center_residual_resolution.json` is decisive here: at `ns=16` the momentum/Codazzi block alone reads `mom_orth = 1.363`, and this is exactly the `center_operator_sup = 1.3634…` that the direct solver reports as its "final" value on both halves. The same table shows `mom_orth` collapsing 1.363 → 6.7×10⁻⁶ as `ns` goes 16 → 128, with `Enn` and `ET_orth` already at 10⁻¹³. So the least‑squares run at `ns=16` drives the interior residual down to a discretization floor set by under‑resolving the winding orbit matrix `M(U(s))` (wind 2, tenfold target circle). The dramatic 260 → 8.9 vector‑norm drop is genuine removal of the crude quintic's interior overshoot **plus** arrival at that floor. Nothing about two‑ended matching can be read from a number that equals the `ns=16` center artifact. Any interpretable interior reading needs `ns ≥ 96` (floor 3×10⁻⁴) with the center‑only resolution value reported alongside every collar residual.

**(ii) The `e^{2r}q₀` exterior is not Einstein.** `known_metric_validation` correctly certifies `e^{2r}·I` (flat slice → a piece of H⁴, `Ric=−3g`) to ~0. But `build_half` attaches to `X=2RI`, i.e. `q(R)=e^{2R}q₀` with `q₀` the **charged Koiso** slice, for which `R(q_Σ)=−6−S<−6`. A uniform homothety `e^{2r}q₀` of a non‑flat slice does not solve `Ric=−3g`; its tangential defect is exactly the persistent `end_operator_sup ≈ 1.07` that the optimizer cannot remove and that is independent of `ns`. This is the concrete meaning of "do not treat the cosh exterior as solving the inner transition": the outer attachment is itself an inconsistent piece, so the collar is being asked to interpolate to a non‑solution. The `1.07` end value is a modeling defect, not an obstruction.

Conclusion: the current artifact does not distinguish matching from overfitting because its final value is `max(center Fourier floor, wrong‑exterior offset)`. The experiment must eliminate (i) by resolution and (ii) by using a genuine exterior, and only then look at the interior.

## Computation 1 (cheapest, most decisive): the correct exterior as a radial charged‑end ODE

The exterior must carry the **same conserved coordinate charge** as the center, because `dq=0` is exact for `Ric=−3g` (Step 94 §1, §4). The right object is not `e^{2r}q₀` but a solution of the reduced radial system with fixed nonzero `q`:

$$
\sigma''+\sigma'^2 = 6+Q,\qquad
U''+\sigma'U'+\Gamma(U)(U',U') = -\,Q\,\nabla\beta(U),\qquad
Q=e^{-3\sigma}F(U),\ \ F=\tfrac12 q^{\top}M(U)^{-1}q,
$$

with `β=log F`, `|∇β|_{H²}=1`, `Hess β = h − dβ⊗dβ` (Step 94 (2.3)). Integrate outward seeking the expanding end `σ→∞`. Two exclusive outcomes, obtainable from a few ODE integrations plus checking the Hamiltonian constraint `R(q_Σ)−H²+|W|²=−6` along the ray:

- **A complete end exists** with `σ→∞`, `U→U_∞` (orbit shape freezes), `Q=e^{-3σ}F→0` while `q` stays fixed and the Hamiltonian identity holds. Then a charged asymptotic Einstein end exists whose metric approaches the flat cusp but whose conserved label `q≠0`. This is the construction target: replace `e^{2r}q₀` in `build_half`'s endpoint with this slice, quintic‑match `X` to it, and re‑run — now the `end_operator_sup` should fall toward 0, isolating the genuine interior residual.
- **No complete end exists**: the orbit equation drives `U` to run away (`F→∞`) or the Hamiltonian constraint cannot be maintained with `q≠0` and `σ→∞`. Then the only `Q→0` ends are `q=0` (Ostrom– Typographic aside: the flat‑slice cusp), and exact conservation `dq=0` plus the OT resolvent obstruction of Steps 85–88 forbid attaching a nonzero‑charge center to such an end. That is the obstruction, delivered by ODE analysis rather than by 864‑parameter fits.

Step 94 §6 already showed the area subsystem alone admits `Q>0` with `ρ~e^{√6 r}`, but explicitly noted that freezing `M=I` while `Q>0` violates the orbit equation `Z=0`. The computation above is exactly the missing test of whether the **coupled** `(σ,U)` system closes with `q≠0`. This is the single sharpest fork in the whole program and it is nearly free.

## Computation 2: reframe the collar as a well‑posed Dirichlet problem, read the Dirichlet‑to‑Neumann defect

Step 98 over‑prescribes the center: it fixes both `q(0)=q₀` **and** `q_n(0)=2K₀` (a full Cauchy jet) *and* the endpoint value. For an elliptic system this is inconsistent in general, and the residual it produces is a confounded mixture. The correct decomposition uses the fact that the germ already exists as an exact analytic local solution (Koiso, verified), so on a thin collar `E=0` is exactly achievable by analytic continuation.

Represent the collar in DeTurck/Bianchi gauge so that `Ric+3g=0` becomes a genuinely elliptic quasilinear system, and solve the **well‑posed** end‑value (Dirichlet) problem on `[ε,R]×S¹`:
- inner edge data at `r=ε`: the germ slice `q(ε,·)` from the exact Taylor/short‑collar data (Step 96 §4, `H_n=3−S`, `σ_{nn}=6+Q`, `a_{nn}=−3−S−Q`);
- outer edge data at `r=R`: the exact charged end from Computation 1;
- conserved charge fixed to the center `q`.

Because this is a Dirichlet problem for an elliptic system, it is solvable and `E→0` in the interior as `N→∞`. The gauge choice does this and only this — it does **not** make the normal Cauchy problem well posed; one must never shoot `q_n` outward. The single remaining object is the **DtN defect** on the circle:

$$
\mathcal D(s) \;=\; q_n^{\text{solved}}(\varepsilon,s)\;-\;2K_0(\varepsilon,s),
$$

the mismatch between the normal derivative the elliptic solve produces at the inner edge and the germ's exact second fundamental form. This is a one‑dimensional quantity on `S¹`, cleanly separated from center Fourier resolution (which now only limits how well the exact germ slice is represented) and from the exterior (now consistent). Its distinguishing signatures:

- `‖𝒟‖` converges as `N→∞` at fixed `R`, and → 0 as `R→∞`: the germ genuinely completes; step‑98‑style decrease was real matching.
- `‖𝒟‖` converges in `N` and floors at a positive value for every `R`: a real matching defect; overfitting is excluded precisely because the interior is exactly Einstein and the defect lives on the interface.
- `‖𝒟‖` keeps shrinking with `N` at fixed `R` with a high‑frequency, non‑convergent Fourier profile: discretization noise, not geometry.

Tabulate the Fourier spectrum of `𝒟` versus `N` for `ns ∈ {48,64,96,128}` and `R ∈ {1,2,3,4}`. Convergence of the spectrum in `N` is the discriminant between real interface data and fit noise.

## Computation 3: the (N,R) scaling of the linearized matching operator

This is the object the route map already identified but has not executed at both ends with a correct exterior. Linearize the reduced residual `E(V)=(H,T,Z,B_{mix})` (Step 94 (8.1), Step 96 (7.2)) about the best collar on `Ω=[−R,R]×S¹`, Coulomb/conformal gauge, Fourier(s)×Chebyshev(r), all `s` modes retained, both ends fixed to the Computation‑1 charged end, one shared charged‑Koiso center. Compute the smallest singular value `σ_min` and its normalized left/right singular fields.

The essential discipline that separates real physics from overfitting is to display `σ_min(N,R)` as a **two‑index table** and verify `N`-convergence at each fixed `R` *before* reading any `R`-scaling. Three signatures:

- **A — discretization near‑kernel (artifact):** `σ_min` decreases as `N` grows at fixed `R`; the right singular field is high‑frequency and delocalized; no `N`-limit. Reject.
- **B — redshift near‑kernel (favoring construction):** at each `R`, `σ_min` converges in `N`; then `σ_min(R) ~ e^{-cR}` with the right field localized in a charge taper at distance `~R` and the left field escaping toward the far end. Approximate connectors with defect → 0 exist as `R→∞`.
- **C — finite obstruction:** `σ_min(R)` converges in `N` and tends to `σ_*>0` as `R→∞`, with a bounded left field having nonzero pairing against the center germ data (the exact charge). No completion with vanishing defect.

The exponent `c` in Signature B is not to be fitted blindly; it is fixed by the **indicial roots** of the linearized reduced operator about the exact asymptotic end from Computation 1. This is a resolution‑free ODE calculation and it predicts which signature to expect. About the flat‑slice cusp, `ρ=e^{σ}` with `σ''+σ'^2=6` gives `σ=\sqrt6\,r`, hence physical `Q=e^{-3\sigma}F=e^{-3\sqrt6\,r}F` while the conserved coordinate charge is the indicial‑exponent‑zero mode (it is the conservation law itself — non‑decaying as a label, entering the metric only through `Q`). So a coordinate‑charge taper imprints a Ricci defect controlled by `Q`, decaying at the geometric rate `3\sqrt6` per unit `r`; Step 94 §6's fitted `−3\sqrt6R/2` for `‖b‖_∞` is the area‑subsystem shadow of this. If the indicial spectrum shows the charge/orbit perturbations decaying at a definite positive rate and the exact charged end of Computation 1 exists, expect Signature B; if Computation 1 finds no charged end, the conserved‑charge mode cannot be tapered to an admissible end and one expects Signature C with the left field pinned to the center charge.

## What to tabulate and what each outcome establishes

Report, for `ns ∈ {48,64,96,128}`, `R ∈ {1,2,3,4}`:
1. the center‑only momentum floor (from the resolution table) beside every collar number, so no reader mistakes the floor for geometry;
2. the corrected `end_operator_sup` with the Computation‑1 exterior (should approach 0), confirming the `1.07` was the homothety inconsistency;
3. `‖𝒟‖` and its Fourier spectrum versus `N` (Computation 2);
4. `σ_min(N,R)` and the localization of its singular fields (Computation 3);
5. the indicial roots at the exact end and the predicted `c`.

The joint reading is unambiguous. If Computation 1 yields a complete charged `Q→0` end **and** `σ_min(R)~e^{-cR}` at the indicially predicted `c` with a taper‑localized right field and escaping left field, then arbitrarily‑small‑defect two‑ended charged connectors exist in this free‑`T²`, `Ric=−3g` class — a construction line worth pushing toward a closed or complete assembly. If Computation 1 finds no charged end, or `σ_min→σ_*>0` with a center‑paired left field and `‖𝒟‖` floored across `R`, then conservation `dq=0` plus the OT resolvent result forbids completion — an obstruction proof independent of any finite fit. Either way the confounds of the present artifact are removed, resolution continuation is honored, and the residual is projected against the one geometrically meaningful inverse scale, the transition length `R`.

Two guards throughout: never differentiate `q_n` outward as an evolution (the gauge fixes the Dirichlet problem, not the elliptic Cauchy instability), and never let the `ns=16` center value stand in for interior geometry.
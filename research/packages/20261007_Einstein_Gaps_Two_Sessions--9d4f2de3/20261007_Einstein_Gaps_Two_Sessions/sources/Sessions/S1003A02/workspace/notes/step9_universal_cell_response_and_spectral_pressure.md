# Step 9 — Universal Burns-cell response, positive-KE sign reversal, and the second-order spectral problem

Conventions: `P=∫|Ric°|²`; scripts report `P/(8π²)`. Cell scale is `x0=a²`.
The strongest analytic support is `trace/ttcs/results/step9_ttcs01_generator1_integration.md`; computation reading is `step9_ttcs01_verifier1_integration.md`; the relative-calibration reading is `step9_ttcs01_verifier2_integration.md`.

## 1. Universal first-order response: statement now supported, proof reduced to one ALE boundary computation

For an oriented background metric near `p`, identify the Burns Kähler direction at infinity with a unit `ζ∈Λ⁺_p`. The first-order law suggested by Steps 8–9 is

\[
 \frac{P(g_a)-P(g;B_a)}{8\pi^2}
 =1-a^2\,\mathcal R^+_p(\zeta,\zeta)+o(a^2),
 \qquad \mathcal R^+=W^++\frac{s}{12}I.
\]

Here the background ball is removed on the right; for an Einstein complex-space-form bulk it contributes no `P`. The topological term is exact:

\[
 P=4\int|\mathcal R^+|^2-8\pi^2T_+,
\]

and a blow-up changes `T_+` by `-1`, so it remains to prove

\[
 \Delta\int|\mathcal R^+|^2
 =-2\pi^2a^2\mathcal R^+_p(\zeta,\zeta)+o(a^2).
\]

The Burns asymptotic metric has

\[
 g_{B,a}=g_0+a^2H_\zeta+O(a^4r^{-4}),\qquad
 H_\zeta=r^{-2}\{dr^2-(J_\zeta dr)^2\}.
\]

SO(3)+ equivariance forces the linear response to pair the scalar and spin-2 pieces of `R+` with `ζ⊗ζ`. The coefficient and sign reduce to the matrix-valued ALE transgression

\[
 \int_{S^3_\infty}\mathcal T_{\mathcal R^+}(H_\zeta)
 =-\pi^2\zeta\otimes\zeta
\]

with the gluing orientation. The scalar part of this boundary flux can already be checked directly; the full matrix-valued computation has not yet been carried out in the session. Assuming it, the separate first variations are

\[
 \frac{4\Delta W_+}{8\pi^2}=-a^2W^+(\zeta,\zeta)+o(a^2),\qquad
 \frac{\Delta S/12}{8\pi^2}=-a^2\frac{s}{12}+o(a^2).
\]

This is the precise remaining proof object. An `O(a^4)` remainder needs a second matched expansion and is not yet justified generally; `o(a²)` is the natural first theorem.

The relation to Einstein desingularization is structural. The scalar cell potential is `-a²<R+ζ,ζ>`. Its scale derivative is `-<R+ζ,ζ>` and its angular derivative is `-2a² Π_{ζ⊥}R+ζ`; both vanish exactly when `R+ζ=0`. Hence Ozuch's vector obstruction is the full critical-point equation of the same first-order cell potential. If `R+` is indefinite, zero scalar cost alone does not imply the vector obstruction.

## 2. Decisive positive-versus-negative Kähler–Einstein computation

New script `workspace/scripts/o11_general_bulk_cell.py` extends the aligned U(2) cell to the signed complex-space-form collar

\[
 K_{bulk}=x+\kappa x^2,\qquad s=-24\kappa,
 \qquad \mathcal R^+(\omega,\omega)=-6\kappa.
\]

At fixed `X=0.25`, degree 8 and 500-point quadrature:

| κ | bulk | x0 | P/(8π²) | slope `(P-1)/x0` | predicted |
|---|---|---:|---:|---:|---:|
| +1 | complex hyperbolic | .003 | 1.01853255 | +6.1775 | +6 |
| +1 | complex hyperbolic | .001 | 1.00605811 | +6.0581 | +6 |
| -1 | Fubini–Study sign | .003 | .98305786 | -5.6474 | -6 |
| -1 | Fubini–Study sign | .001 | .99410593 | -5.8941 | -6 |

Thus an actual same-metric positive-KE cell has `P<8π²`. There is no hard-coded CH subtraction: `P` is directly integrated. The sign reversal is already visible in the explicit four-constant Kähler seed, whose expansion is

\[
 \frac{P}{8\pi^2}=1+6\kappa x_0+9(\kappa^2+X^{-2})x_0^2+O(x_0^3).
\]

Therefore a finite outer radius cannot create the first-order sign; it enters at second order. This verifies the strategist's crucial falsification test and shows that a universal per-blow-up `8π²` lower bound is false on backgrounds with a positive eigenvalue of `R+`. It also explains why blow-ups of positive KE manifolds can be cheap. This experiment verifies the aligned complex-space-form specialization of the universal tensor law, not the full general-background law by itself.

## 3. Perpendicular CH cell and collaboration with S1003A01

High-degree smooth fixed-slot computations at `θ=π/2` remain above threshold:

| x0 | degree | P/(8π²) | excess |
|---:|---:|---:|---:|
| .03 | 10/10 | 1.018595845 | .018596 |
| .10 | 10/10 | 1.151480821 | .151481 |
| .20 | 10/10 | 1.444267492 | .444267 |
| .30 | 10/10 | 1.817084160 | .817084 |

The `.03` optimizer ended abnormally and the larger points hit iteration limits, so these remain ansatz upper bounds. The `.03` profile was exported with `G,h` and their first two x-derivatives at 1601 points:

- `data/o11perp/profile_perp_smooth_x0.03.npz`
- `data/o11perp/profile_perp_smooth_x0.03.csv`

Peer S1003A01 independently obtained a stronger exact Bianchi-IX relative calibration. In bolt-adapted variables `u_i` it gives

\[
 \frac{P}{8\pi^2}-1=
 \int\left(\sum_i\frac{\lambda_i}{4}E_i^2+
 \frac{2u_1u_2u_3}{\lambda_2}\right)dt.
\]

On the smooth `x0=.01` profile the three squares total `.003428047`, the signed cubic is `-.00143166`, leaving `.001996387`. This is more mathematically valuable than another profile search: threshold is reduced to a matrix Hardy/Riccati problem for `η=(u1,u3)`. A sufficient certificate is a symmetric `Γ(t)` satisfying

\[
 N-\dot\Gamma+K^T\Gamma+\Gamma K-\Gamma A^{-1}\Gamma\succeq0
\]

with the correct bolt boundary sign. On the exact CH segment, channels `v±=u1±u3` factor through explicit positive Jacobi solutions

\[
 y_+=x(1+x)^{1/2},\qquad y_-=x(1+x)^{-5/2}.
\]

The critical transformed variables are

\[
 z_+=\frac{u_1+u_3}{x\sqrt{1+x}},\qquad
 z_-=\frac{(1+x)^{5/2}}x(u_1-u_3),
\]

which turn the outer signed potentials into weighted squares plus a boundary quadratic form. The missing theorem is an inner Burns-to-CH Dirichlet-to-Neumann comparison. A resonance remains possible because `u2≈3x`, `u3≈-x0/x` gives `u2u3≈-3x0` across the logarithmic neck; its Schur complement could in principle produce an `x0² log(1/x0)` term. No constructed metric presently realizes a negative term, and all computed profiles are positive.

## 4. Full-mode Hessian pressure and why no negative cell was established

Three Hessian prototypes were built:

- `o11_radial_hessian.py`: all SU(2)-invariant radial variations of `G` and six entries of symmetric `h`;
- `o11_full_hessian.py`: arbitrary coordinate tensor modes (found to have a measure/global-smoothness problem);
- `o11_full_hessian2.py`: geometric-coframe modes (better, but low angular quadrature and no gauge quotient).

The radial quadrature reproduces the cell energy to `4e-10`. At 3 radial modes all 21 raw eigenvalues were positive (minimum `8.27`). At 6 modes a raw eigenvalue `-1.63` appeared, and at 8 modes two appeared (`-23.18,-1.44`). These are not established negative directions:

1. the expanded-space projected gradient is large (`5.22`, `12.65`), so the base is not stationary there;
2. the parametrization `G→G exp(d)` adds gradient-dependent second-coordinate terms;
3. diffeomorphism modes were not removed;
4. the negative values do not converge with resolution;
5. direct symmetric line samples rose on both sides at the tested amplitude; smaller amplitudes scaled by `||g^{-1}th||∞` are needed.

The non-invariant prototypes likewise cannot decide the question yet. A true next spectral computation must use the natural coframe, include all SU(2)-invariant shifts, build the Lie-derivative map for compactly supported vector fields, project to its L2-orthogonal/Bianchi complement, re-optimize to projected stationarity, and only then solve the generalized Ritz problem. Non-invariant extensions should use globally smooth Wigner-D modes rather than raw Euler trigonometric functions.

The exact relative calibration now gives the sharper route within symmetry; the gauge-fixed spectral calculation remains the correct route beyond symmetry.

## 5. What changed in O11

- The universal first-order object is `-a² R+(ζ,ζ)`, not a universal positive blow-up cost.
- Positive Kähler–Einstein curvature gives a real sub-`8π²` Burns cell at first order; negative Kähler–Einstein curvature makes aligned cells expensive.
- On negative KE backgrounds, the dangerous perpendicular directions are exactly `ker R+`, where first order cancels and the Einstein desingularization obstruction also vanishes.
- Coefficient 4 for balanced negative-KE surgery, if true, is a second-order theorem. Within SU(2), it is now a critical matrix Hardy/Riccati or inner/outer Dirichlet-to-Neumann comparison. Beyond symmetry, it is a gauge-fixed weighted spectral problem.
- The proposed global lower-bound architecture must allow cheap cells wherever the near-minimizing bulk develops positive `R+`. Quantitative LeBrun saturation must therefore control the positive part of `R+` strongly enough that any distributed cell saving is subordinate to the bulk deviation cost.

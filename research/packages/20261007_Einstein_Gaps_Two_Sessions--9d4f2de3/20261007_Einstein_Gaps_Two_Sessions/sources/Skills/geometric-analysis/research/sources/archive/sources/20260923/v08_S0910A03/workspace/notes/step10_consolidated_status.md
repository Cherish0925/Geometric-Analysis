# Step 10 consolidated status

## Central correction

Step 9 overstated the Taub–NUT–AdS example. It does **not** refute the adjustable-buffer cover problem relevant to the calibrated LeBrun sequence.

For a point at distance `1/2` from the NUT:

- balls of radius at most `1/3` lie in a fixed annulus and have bounded curvature mean;
- balls with radius greater than `1/2` capture the NUT curvature core and have mean `|Rm|^2 = Θ(nu^{-1})`;
- a large covering domain containing the NUT does not unwrap the short Hopf circle;
- a fixed smaller buffered domain avoiding the NUT does unwrap it and has a noncollapsed hyperbolic limit;
- that unwrapped limit has `W+=0`, `s=-4`, hence scalar–Weyl calibration deficit `16`, not `0`.

The exact calculation is in:

- `workspace/scripts/compute_taub_nut_ads_curvature.py`
- `workspace/scripts/analyze_taub_nut_ads_multiscale.py`
- `workspace/notes/step10_multiscale_cover_and_diffuse_pontryagin.tex`

The script verifies

`|W|^2_tensor = 32 nu^2 (4nu^2-3)^2 / [3(r+nu)^6]`,

NUT curvature growth `~3/(2nu^4)`, and cumulative full-Weyl energy tending to `32pi^2`. In its chosen orientation, `W+=0` and `W-` has eigenvalues

`(2nu(4nu^2-3)/(3(r+nu)^3), same, -4nu(4nu^2-3)/(3(r+nu)^3))`.

## Correct scaling

For `g_hat=a^2 g`, Ricci as a `(0,2)` tensor is unchanged, but the Ricci and Weyl curvature endomorphisms scale by `a^{-2}`. After rescaling `g_hat=r^{-2}g`, the forbidden spectrum is

`(-r^2/6, r^2/12, r^2/12)`, not the unchanged numerical spectrum.

For a negative Einstein scale `kappa>0`, the forbidden germ is

`Ric=-kappa g`, `Spec(W+)=(-kappa/6,kappa/12,kappa/12)`.

The projector calculation gives `nabla W+=0`, while the Einstein–Weyl identity requires `|nabla W+|^2=kappa^3/16`. The contradiction survives every fixed radius and disappears only when the available scale tends to zero.

## Revised accessibility problem

The remaining fixed-topology negative-branch question is multiscale and includes freedom to select the buffered downstairs domain before taking its cover.

A sufficient theorem would say: for every finite curvature-mean bound `K`, the positive-volume calibrated good set contains a point and a scale `rho>=r_*(K)>0` such that an appropriate buffered normal cover has uniform four-dimensional volume ratio and harmonic radius. Naber–Zhang then supplies the chart in maximal-rank, nondegenerate-model cases; normal-cover mean transport carries the calibrated deficit upstairs; the forbidden Einstein germ gives a contradiction.

Failure would require persistent rank loss, model degeneration, or contraction/twist structure at every fixed scale. Standard Taub–NUT and real-hyperbolic cusp profiles do not meet the simultaneous calibration input.

## Diffuse Pontryagin mechanism

For the Levi-Civita connection on `Lambda^2_+`,

`rho_+=(1/(4pi^2))(s^2/24+2|W+|^2-|Ric0|^2/2)`

satisfies

`||rho_+ - 3/(16pi^2)||_L1 -> 0`.

Hence characteristic mass follows volume on every measurable region. It cannot be placed only in vanishing-volume NUT cores.

Comparing with a basic/split connection `B`,

`P(F_A)-P(F_B)=d T_P(A,B)`.

When the base has dimension at most three, `P(F_B)=0`; positive-volume collapsed bulk therefore requires persistent non-basic Chern–Simons flux. In invariant circle collapse, with

`F_A=F_H + eta wedge Xi`, `Xi=i_V F_A`,

one has `P(F_A)=2 eta wedge P(Xi,F_H)`. Bounded horizontal curvature plus the positive characteristic density forces a positive mean of `|Xi|^2`. This is a rigorous obstruction to **basic** collapse, but not yet to collapse itself: scaled holonomy variation, O’Neill tensors, nil commutators, or fiber-frame twist can carry the density diffusely while ordinary fiber holonomy remains small.

The key next inequality must decompose `Xi` into fixed-scale accessibility, contraction-filling curvature, and O’Neill/nil twisting costs. This is more precise than counting NUT charges.

## Other corrections and collaboration

- A full counterexample to the interval statement in dimension `n` requires failure of both normalized signs in that dimension, but the two witness manifolds need not be the same.
- S0910A02's opposite-warping Calderón–Zygmund spike shows that small pointwise Ricci defect plus small `L^2` curvature energy does not imply pointwise curvature control. Future arguments should use harmonic charts, finite-`p` estimates, smoothing, or weak test-field identities.
- S0910A01's basic-collapse Pontryagin observation agrees with the diffuse-density calculation, but only a definite triple—not merely a pair—of local self-dual forms is enough for the pointwise frame-parallel argument without further structure.

The complete Yau problem, both signs in dimension four, higher dimensions, and Lean formalization remain open. The current work is still Explore.

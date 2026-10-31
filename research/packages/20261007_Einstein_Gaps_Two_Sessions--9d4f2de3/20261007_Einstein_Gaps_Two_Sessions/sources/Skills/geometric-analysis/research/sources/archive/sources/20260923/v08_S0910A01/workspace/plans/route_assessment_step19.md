# Route assessment after Step 19

## What Step 19 established

### Whitney-ball reduction (A01, this step)

The degenerate cutoff-flow operator `partial_t - chi^2 Delta` is reduced
to a non-degenerate operator on each Whitney ball `B_{cr chi_0}(y)`.

Three uniform cancellations, verified numerically and checked by TTCS:

1. **BG energy transfer**: `ell^4 fint |Rm|^2 <= C K_0 r^4`, with the
   `chi_0^4` in `ell^4` canceled by the `chi_0^{-4}` volume ratio.
   Independent of `chi_0` for `chi_0` from 1 to 1e-6.

2. **Sobolev product**: `A_ell^2 ||Rm||_2 <= C sqrt(K_0) r^2`, the same
   4D Sobolev-energy cancellation as in Step 17, now at every Whitney level.

3. **Diffusion-time matching**: physical time `theta r^2` provides smoothing
   at ALL Whitney levels simultaneously; the ratio `sqrt(theta)/c` is
   chi_0-independent.

### Volume-independent beta (A03 Step 19, proved)

Wang's critical parameter `beta = A^2 ||Rm||_2 = C sqrt(eps_Li)` cancels
collapsed volume in 4D because L^2 IS the critical exponent.  This is the
same cancellation as above, in the Wang/Yang framework.

### p > 4 connection threshold (A03 Step 19, proved)

The derivative estimate `|chi nabla(chi^2 E)| ~ delta t^{-1/2}(r^2/t)^{2/p}`
is time-integrable iff `p > 4`.  For `p = 6`, both metric drift (theta^{2/3})
and connection drift (theta^{1/6}) are O(delta).

### TTCS corrections incorporated

- `a - a_0 = O(Lca_0)`, not `O(c^2 a_0)`; handled by uniform ellipticity
- localization factor `exp(C theta/c^2)`, not `exp(C theta)`
- energy budget must be local per support component
- squared Sobolev coefficient `A^2`, not `A`
- integration by parts of `nabla^2 a` generates essential defect coupling
- overlap boundedness controls unnormalized integrals; normalized-energy
  summation needs finite-neighbor differential inequality

## Current mathematical state

The four-dimensional negative LeBrun/Ishida-LeBrun route has been reduced to
exactly two non-degenerate PDE theorems, plus standard organizational work:

**Target 1: localized curvature eps-regularity.**
|chi^2 Rm| <= C beta/t from small relative L^2 energy under the cutoff flow,
on the finite-neighbor Whitney system.

**Target 2: localized weighted tensor Bernstein.**
|chi nabla(chi^2 E)| <= C_p delta t^{-1/2}(r^2/t)^{2/p} with volume-
independent constants.

Both targets involve non-degenerate (uniformly elliptic on Whitney balls)
tensor parabolic equations with bounded cutoff perturbation and normalized-flow
source terms.

The closure architecture (A03): with p = 6, Targets 1-2 close the first-exit
with no circularity.  The unweighted Q(t) <= e^{C theta} Q(0) is separate.

## What remains for the full Yau 26 problem

- Targets 1-2 above (non-degenerate PDE, but genuine new theorems)
- Positive branch: no serious route; A02's toric crux is specialized
- Higher dimensions n >= 5: no W+ decomposition, no Derdzinski mechanism
- Lean formalization: not begun

## Best next work

For the negative four-dimensional branch: write the complete tensor curvature
evolution under partial_t g = -2 a E with all terms explicit, derive the
coupled local energy inequality on a single Whitney ball, and verify that
the cutoff perturbation + normalized-flow source terms are absorbable.  This
is the technical core of Target 1.

For the broader problem: examine whether the Whitney reduction framework
(which works in any dimension at the critical L^{n/2} exponent) can be
combined with other obstruction mechanisms beyond W+ in dimensions n >= 5.

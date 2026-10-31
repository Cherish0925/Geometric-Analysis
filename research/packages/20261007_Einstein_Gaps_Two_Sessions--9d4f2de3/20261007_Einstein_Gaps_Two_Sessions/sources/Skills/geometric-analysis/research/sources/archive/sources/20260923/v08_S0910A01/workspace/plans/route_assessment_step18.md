# Route assessment after Step 18

## What this step changed

Step 18 removed the remaining unsupported inference that the radius-repaired
plateau geometry proves a localized Li bootstrap.  The containment of covering
balls in the plateau is valid geometry, but the center supremum in Li's argument
is not closed by that containment.  The live object is now a full-support,
transition-inclusive cutoff-flow theorem.

## Verified algebra and scripts

1. `workspace/scripts/step18_weighted_cutoff_algebra.py` verifies the scalar
   transformation for `f=aK`, `a=chi^2`:

   ```text
   f_t <= a Delta f - 2<nabla a,nabla f>
          +(2|nabla a|^2/a-Delta a)f + c f^2 + aT.
   ```

   The reaction is `c f^2`, not `c f^2/a`; `|nabla a|^2/a=4|nabla chi|^2`.
   After integrating by parts in the scalar principal energy, no pointwise
   Hessian of `a` remains.

2. `workspace/scripts/step17_sobolev_energy_cancellation.py` was corrected so it
   only records the four-dimensional Sobolev-energy scale fact.  It no longer
   says this proves full-support smoothing.  The corrected run shows
   `A_U ||Rm||_2 = sqrt(K0) r_*^2`, independent of volumes from `1` to `1e-24`.

3. `workspace/scripts/step18_energy_absorption_terms.py` verifies the normalized
   scaling of cutoff-gradient remainders and the critical product
   `K0^(2/n) r^2` in dimension `n` when `L^{n/2}` curvature is available.

4. `workspace/scripts/step18_constant_diffusivity_weight_scaling.py` confirms
   the model reason `aRm` is the natural target: for constant diffusivity,
   `||aK(t)||_inf` scales like `1/t` independently of `a`.

5. `workspace/scripts/step18_degenerate_model_heat_kernel.py` was corrected after
   TTCS noticed the drift sign error.  In the linear `a=x^2` model, normalized
   boundary spikes do not create large weighted output.  This is consistency
   evidence only, not a geometric theorem.

## Current mathematical state

A03's Step 18 note and scripts refine the picture.  The coupled local `L^2`
energy system is best treated as a first-exit lemma: under provisional metric,
Sobolev, finite-neighbor, cutoff, and local-energy controls, the
Sobolev-energy cancellation improves the local curvature/defect energies.  It
is not a standalone theorem independent of those evolving controls.  Complete
tensor bookkeeping of all `nabla^2 a` contractions is still needed.

The weighted defect variable `U=aE` gives a stronger route for metric control.
For fixed `p>2`, A03 derives an inequality for `w=|U|`:

```text
d/dt int eta^2 w^p + c int eta^2 a |nabla w^(p/2)|^2
 <= cutoff terms + C int eta^2 a |Rm| w^p + C int eta^2 w^(p+1).
```

Relative Sobolev plus small critical energy can absorb the reactions for one
fixed `p`; direct iteration to infinity fails because the coefficient grows like
`p sqrt(epsilon)`.  A second stage needs a weighted curvature-potential estimate
such as `A_U^4 int a|Rm|^3 <= C/t`, yielding
`|aE| <= C_p delta (r^2/t)^(2/p)`, integrable exactly for `p>2`.

Unweighted `Q(t)=int|E|^2` remains separate and necessary for LeBrun
recalibration.  It must be controlled directly by the defect energy inequality;
weighted `aE` cannot control transition energy where `a` is small.

## Support and topology corrections

If the full support is `B_{5r_*}(p)`, the initial maximal-function control must
reach at least `6r_*`; the earlier `4r_*` radius only controls the inner plateau
and nearby covering balls.

The topology-uniformity input is Noether plus connected-sum arithmetic, not
BMY.  For standard Ishida-LeBrun minimal-general-type summands with `b_+(N)=0`
and `D=A/3`, A03 obtains `chi(M)/A <= 65/6`; broader summands need explicit
upper bounds before uniform constants are asserted.

## Best next work

A mathematically decisive next action is to construct the degenerate weighted
curvature-potential estimate.  A promising local framework is Whitney scaling
near the cutoff boundary: where `chi(x)>0`, work on balls of radius comparable
to `r chi(x)`, on which `a` is comparable to `a(x)` and the diffusion length
`sqrt(a(x)t)` remains inside the same region for `t<=theta r^2`.  The goal is a
Moser/mean-value estimate for the tensor curvature equation with the coupled
`E` terms and only first cutoff derivatives after integration by parts.

Parallel routes remain important: A02 is pursuing the positive toric crux for
`#_k(S^2 x S^2)`; this does not solve the full positive branch but targets a
serious strict-Hitchin-Thorpe laboratory.  The global Yau 26 problem remains
open beyond the critical four-dimensional negative laboratory.

## Additional Step 18 execution asset

`workspace/scripts/step18_whitney_scaling.py` verifies the local Whitney-scale
coefficient arithmetic near the cutoff boundary.  At a point with
`chi(x0)=chi0>0`, a ball of radius `ell=c r chi0` makes `a/chi0^2`, the drift
coefficient, and the potential coefficient uniformly bounded after rescaling;
for `L=2,c=0.1`, the principal coefficient lies in `[0.640,1.440]`, drift is at
most `40`, and the potential coefficient is at most `16`.  This suggests the
next proof should use Whitney balls and time `theta r^2` with `sqrt(theta)<=c/2`
to derive the weighted curvature-potential estimate on the transition.

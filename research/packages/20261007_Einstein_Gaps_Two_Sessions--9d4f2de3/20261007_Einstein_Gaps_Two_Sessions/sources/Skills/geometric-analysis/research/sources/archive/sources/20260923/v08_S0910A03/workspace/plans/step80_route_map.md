# Step 80 route map: resolve the reflected inner layer before extending the tail

**Step 81 supersession**: The VII₀ collapse is now rigorously proved (not
just numerical). The angular-slip energy cancellation is corrected to
trace-only. The volume-weighted universal contraction ⟨u'(0)⟩_ρ=-3
holds for any area profile. The z-dependent case remains genuinely open.
See `workspace/plans/step81_route_map.md`.

## Current mathematical position

The negative graph-manifold route still has an all-Einstein exclusion on the
candidate topology and an explicit long expanding tail with vanishing defect.
The missing object is a connector from a reflected scalar-minus-six `T^3`
center into that tail.  Step 80 verifies that this is a coupled base/orbit-area/
orbit-shape problem and localizes the current computational failure to the
first physical `O(1)` layer.

## Correct equations and scales

For `g=gamma_B+e^sigma M` with `det M=1`,

\[
E_B=Ric(gamma_B)-Hess sigma-\tfrac12d sigma^2
-\tfrac12U^*h_{H^2}+3gamma_B.
\]

On a frozen cusp the map stress cannot be cancelled.  Physical source
integration uses `rho dvol(gamma_B)`; on the cusp this is `e^{3r} dr dz`.
Common `N^{-2}` lattice scaling changes only `sigma` by a constant and leaves
`U` unchanged.

## Evidence from the paired finite-mode run

From the Step 69 reflected center, with projected Koiso second jet and all five
Ricci components:

- joint base/area/shape freedom lowers RMS and much of the residual profile;
- sampled operator sup remains approximately `15` for `R=4,6` at physical
  `r≈0.2`;
- outgoing `S-I` and scaled intrinsic curvature are already small for large
  `R`, so extending the tail does not address the hard part;
- the present peak is not a theorem: wrong fourth/higher germ jets, L2 rather
  than max optimization, finite sampling, incomplete convergence, and omission
  of the second `H^2` variable all remain.

## Next construction

Build a separate inner-domain solver, not another whole-core-to-cosh carrier.

1. Represent an exact/high-accuracy scalar-minus-six reflected center and
   recursively compute the Einstein even jets through at least order six:
   `p=Ric+3`, `w=D Ric[2p^flat]-6p`, with normal and momentum compatibility.
2. On `0<=r<=0.6–1`, match these jets and leave outgoing value and shape free.
   Free corrections should begin beyond the matched order.  Use fixed physical
   weights, a pointwise-max surrogate, and off-grid evaluation.
3. Save pointwise/modewise `C_B` and `T_B` in `E_B=C_B-T_B`, plus the physical
   matrix Noether/forcing flux with weight `e^{a+sigma}`.
4. Add full `H^2` freedom.  The minimal angular-slip candidate is a rotating
   center `m^2 sinh^2 d*=12` with
   `d=d0+A cos(kz)`, `psi=mz+B sin(kz)`, and
   `B(0)=-(m/k)coth(d*)A(0)`.  Its linearized sign
   `A''(0)=(k^2-m^2)A(0)` makes `k<m` the first concrete mechanism capable of
   reducing hyperbolic radius while preserving central stress to first order.
   Zero and `2k` backreaction in `sigma` and the base must be solved, not
   prescribed.

## Interpretation of possible outcomes

If the inner peak retreats with jet order, resolution, and the angular-slip
variable, continue the outgoing Cauchy data toward the Step 73 tail.  If a
same-sign compatibility mode persists under those improvements, derive its
analytic origin from the zero/`2k` equations or the convex-distance flux.  The
existing numerical peak alone chooses neither outcome.

The positive normalized branch, higher dimensions, and final Lean proof remain
separate unresolved parts of Yau 26.  Peer A02's positive-side alignment
mechanism and A01's mixed-chirality Green response should continue in parallel.

## Files

- `workspace/notes/step80_joint_base_response_and_inner_layer.md`
- `workspace/scripts/step80_base_identity_verify.py`
- `workspace/data/step80_base_identity.json`
- `workspace/scripts/step80_joint_base_response.py`
- `workspace/data/step80_joint_base_response_summary.json`
- `workspace/data/step80_residual_atlas.json`
- `workspace/scripts/step80_koiso_jet_recurrence.py`
- `workspace/data/step80_koiso_jet_recurrence.json`
- `workspace/scripts/step80_angular_slip_verify.py`
- `workspace/data/step80_angular_slip.json`
- `trace/ttcs/results/step80_ttcs01_verifier1_integration.md`
- `trace/ttcs/results/step80_ttcs01_generator1_integration.md`

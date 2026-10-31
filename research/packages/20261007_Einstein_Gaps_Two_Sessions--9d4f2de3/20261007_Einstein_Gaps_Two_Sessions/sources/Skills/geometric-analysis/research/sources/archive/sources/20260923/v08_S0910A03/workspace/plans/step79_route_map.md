# Step 79 route map: after the OT reduction and weighted harmonic-map mechanism

> **Superseded by Step 80 where relevant.** Physical cusp forcing has weight `e^{3r}`, common lattice scaling does not create an orbit-map distance `2 log N`, and the main computation must start from reflected scalar-minus-six data with joint base/area response. See `workspace/notes/step80_joint_base_response_and_inner_layer.md`.

## Research position

The full Yau 26 problem remains unresolved. The negative graph-manifold route
now has a complete mathematical framework through which the finite connector
problem is understood:

### Solved modules

1. **Step 73 expanding tail:** Explicit metric construction removes order-one
   anisotropy at cost O(K^{-1}+K^{-2}+e^{-2r_0}), with confirmed exit jets.

2. **Step 78 VII_0 barrier:** Fixed helicoidal orbit map (d(r), kz) in H^2
   cannot reach expanding interface; proved for delta <= 3/5.

3. **Step 79 OT reduction:** The orthogonally transitive T^2-invariant Einstein
   system reduces to a weighted harmonic map to H^2 coupled to area/base
   equations. Verified on round cusp and Step 73 tail.

### Sharpened decisive question

The TTCS maximum principle shows: for **exact** Einstein reflected connectors,
constant outer boundary orbit data forces constant orbit map throughout
(because d^2_{H^2}/2 is convex and Hess >= g_{H^2}).

Therefore the connector **must** be approximate: ||Ric + 3g|| = ||E|| -> 0
as a parameter. The forced orbit equation becomes:

  div(rho M^{-1}dM) = -2 e^{2lam} rho E^circ_orbit

Even as ||E||_infinity -> 0, the weighted forcing e^{2lam} rho ||E|| can
remain O(1) on a long expanding connector (because the weight grows
exponentially). The decisive question is:

**Can a sequence of approximate connectors with ||E||_infty -> 0 transfer
the center's O(1) orbit energy to the exit while satisfying all constraints
(Hamilton, momentum, DeTurck) and reaching the Step 73 tail interface?**

This is a specific BVP/sequence construction problem, not an abstract
existence question.

### Additional constraints from TTCS

1. **Matrix Noether flow:** Q(r) = int_z rho M^{-1}M_r dz = 0 at all r
   (from reflection). This is an sl(2,R)-valued constraint.

2. **Weighted stress balance:** The orbit stress T_ij satisfies
   div(rho T) = -(1/2) e_H2 grad(rho), coupling orbit energy to area gradient.

3. **Center energy floor:** int rho d_s^2 / int rho >= 12 - 8delta
   (Step 76 identity). The center's orbit energy is order one and lattice-
   independent.

### Mechanism (structural, not proved)

- In VII_0: psi_z = k frozen, d must increase.
- In general OT: psi(r,z) free, conservation governs but doesn't freeze it.
- Growing e^sigma (from Lambda=-3 area equation) can enable angular
  redistribution and d-source removal.
- The Step 73 tail IS the asymptotic version of this mechanism.
- But "growing weight necessarily absorbs angular momentum" is a possible
  mechanism, not a conservation-law proof.

## Next mathematical objects

### Priority 1: Weighted forced harmonic-map analysis

Study the forced equation

  div(rho grad d) = rho sinh(d)cosh(d)|grad psi|^2 + 2 e^{2lam} rho E^circ_d

on an expanding cylinder [0,R] x S^1 with R -> infinity, sigma ~ 2r,
and ||E|| ~ 1/K -> 0 but the weighted force rho E ~ e^{2r}/K.

Does the maximum principle for d^2_H2/2 survive when the RHS accumulates?
What is the critical balance between the maximum-principle bound and
the weighted forcing?

### Priority 2: Explicit finite-mode test

Construct a specific family of approximate metrics:
- Reflected center with Koiso-type R=-6 data on T^3
- Expanding transition region with anisotropy cutoff function
- Step 73 tail at the exit
- Compute the full ||E||_infty and all constraint violations

This would be a numerical existence/non-existence experiment for the
specific BVP.

### Priority 3: Positive branch

The mixed-chirality #_3(S^2 x S^2) positive route needs non-Kahler
Einstein existence. A01's automorphism removal and Lichnerowicz Green
transfer are the active analytical tools. Continue to monitor and
exchange exact calculations.

## Key files

- `workspace/notes/step79_ot_reduction_and_mechanism.md`
- `workspace/scripts/step79_ot_einstein_reduction.py`, `step79_verify_cusp_tail.py`
- `workspace/data/step79_ot_reduction.json`, `step79_verifications.json`
- `trace/ttcs/results/step79_ttcs01_verifier1_integration.md`
- Prior: step78_rotating_eigenframe_barrier.md, step73_tail_completion_and_core_entry.md,
  step76_center_energy_transport_and_scattering.md, step77_pe_scattering_correction.md

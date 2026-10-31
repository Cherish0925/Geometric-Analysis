# Step 75 scope correction

This route map no longer supports a fixed interval \(R\approx5\), frequency-uniform mode stability, or a three-equation-plus-post-check construction.  The reflection transfer factor is \(\sinh(k)/k\), the CMC ODE does not evolve the constrained slice geometry, and all five Ricci components must be controlled in a parameter-dependent family.  Exact umbilic finite exit data are incompatible with nonconstant center anisotropy; a viable exit retains a small unweighted but nonzero anisotropy flux for the adiabatic tail.  Current structure is recorded in `step75_reflection_core_flux_and_center_theorem.md`.

# Step 74 route map (supersedes step72_route_map.md)

Session: S0910A03. Phase: Explore.

## Key Step 74 advances

1. **Z-independent impossibility**: δ ≥ 3/2 for all z-independent diagonal T²-invariant cores.
   Proves that z-dependence is structurally essential (not just numerically helpful).

2. **Corrected linearized modes**: Anisotropy equation reduces to modified Bessel ν=3/2.
   Both branches bounded (I-branch decays at rate 3, K-branch → constant).
   NO growing modes. BVP (Neumann + Dirichlet) is well-posed and unique.

3. **Core length estimate**: CMC ODE reaches |S-I|² < 0.01 by t ≈ 3.
   The nonlinear core is a COMPACT BVP on [0,R] × S¹ with R ≈ 5.

## Problem decomposition (negative branch, dim 4)

| Module | Status | Key fact |
|--------|--------|----------|
| **Koiso center** | EXISTS | Local exact Ric=-3g germ with R(q₀)=-6, S(0)=0 |
| **Core BVP** | OPEN | Nonlinear elliptic on [0,R]×S¹, R~5; linearized well-posed |
| **Tail** (Step 73) | SOLVED | O(1) anisotropy removed with O(K⁻¹) defect |
| **Einstein exclusion** | EXISTS | Di Cerbo: extended graph manifolds have no Einstein metrics |

**The critical bottleneck is the core BVP.**

## Viable routes (prioritized)

### Route 1: Nonlinear core BVP (A03 primary)

**Strategy:** Solve the T²-invariant Einstein-DeTurck BVP on [0,R] × S¹.
- Unknowns: a(t,z), b(t,z), c(t,z) (3 functions of 2 variables)
- Equations: 3 tangential + constraint propagation
- BC: reflection at t=0, near-cusp Dirichlet at t=R
- Domain: compact, R ≈ 5
- Method: pseudo-spectral (Chebyshev × Fourier) + Newton iteration

**Why feasible:** Linear analysis shows no growing modes; CMC ODE
reaches near-cusp data in finite time; domain is compact.

**What it would establish:** Existence of approximate negative Einstein
cores on T³-collar geometries. Combined with tail + Di Cerbo → complete
negative-branch counterexample for dim 4.

### Route 2: Positive mixed-row desingularization (A01/A02 primary)

**Status:** A01 and A02 are computing the finite-dimensional Ozuch
obstruction for (S²×S²)/Z₂. Four scalar kernel modes, inter-node
Green response needed. Bianchi-corrected local scalar projection = 0.
Diagonal r=2 spin row is the first clean computation target.

**What it would establish:** Einstein metrics on specific positive
manifolds. Doesn't directly address Yau 26 positive branch universally.

### Route 3: Surface bundle E_D Einstein nonexistence (deferred)

**Status:** Explicit δ→0 metrics exist. No known Einstein exclusion.
**Obstacle:** A genuinely hard open problem with no current mechanism.

## Reusable assets

- Modified Bessel mode analysis for T²-invariant Einstein on R×T³
- Energy uniqueness identity for the anisotropy BVP
- Z-independent impossibility (δ ≥ 3/2 floor)
- Adiabatic tail completion lemma (Step 73)
- Weighted normal identity e^{2t}(H-3) = −3 − ∫e^{2s}|S-I|²ds
- Koiso center Yamabe solver (Step 69)
- Conformal gauge elliptic system (Step 72, det = 2k⁶)
- CMC gauge core equations and ODE model

# Supersession notice (Step 73)

This map's closure of the approximate `T^2` graph route and its `P_4^+ => n>=6` language are withdrawn. Exact anisotropy rigidity remains useful, but a verified adiabatic expanding tail removes anisotropy at defect `O(K^{-1}+K^{-2}+e^{-2r_0})`; core entry and graph gluing remain open. Products extend particular near-pinched input families only and neither reduce arbitrary high-dimensional manifolds nor preserve absence of arbitrary Einstein metrics. The corrected route is in `workspace/notes/step73_tail_completion_and_core_entry.md`.

# Step 72 route map (supersedes step70_route_map.md)

Session: S0910A03. Phase: Execute → Explore.

## Major route change: T²-invariant graph neck BLOCKED

### What was established (Steps 62–72)

The T²-invariant graph-manifold construction for Yau 26 (negative branch)
was the most developed counterexample candidate. Step 72 established a
three-link obstruction chain that rigorously blocks it:

1. **Yamabe impossibility** (Step 72): R=−6 on T³ requires a metric outside
   the flat conformal class. In the T²-invariant ansatz, this forces
   nonconstant f(θ), giving nonconstant orbit anisotropy d = 2f(θ).

2. **Drift-Laplacian amplification** (Step 72, TTCS verified): The exact
   Einstein equation forces d = b−c to satisfy Δd + ∇σ·∇d = 0. Near the
   cusp boundary, Frobenius analysis shows z-oscillation modes are
   AMPLIFIED: factors 1.175 (n=1), 1.813 (n=2), 3.339 (n=3).

3. **Cusp rigidity** (Step 72, TTCS verified): Flat hyperbolic cusps have
   constant T² cross-section (d = const). The O(1) mismatch between
   center oscillation and cusp constancy cannot be absorbed by the
   O(δ·log(1/δ)) forcing available to approximate solutions.

### What remains from the graph route

- **Without T² symmetry**: The drift-Laplacian argument is specific to
  T²-invariant metrics. A general 4D construction could evade it, but
  would require solving the full 4D Einstein PDE without symmetry reduction.
  This is vastly harder and has no natural relationship to cusp geometry.

- **Higher dimensions**: For n ≥ 5, the fiber dimension is ≥ 4, and the
  Yamabe/anisotropy obstruction chain may not apply. But A02's Step 74
  product propagation shows dim 4 is the bottleneck for positive branch.

### Complementary findings from A01 and A02

- **A01 Step 73–74**: Verified Preissmann obstruction (isotropic center
  defect ≥ 2/3), explicit Koiso center fibers, exponential ODE anisotropy
  decay at rate √3. Confirmed that A01-type Yamabe fibers work but have
  nonconstant d. The graph-neck shear budget shows normal-only patches
  are insufficient.

- **A02 Step 74**: Three structural results for the positive branch:
  (a) ℓ=2 is the unique log-critical mode for C⁰ pinching
  (b) Higher Biquard obstructions are subcritical — cannot be forced to
      vanish by tight pinching
  (c) Product propagation: P₄⁺ resolves all n ≥ 6

## Current viable routes

### Route 1: Restricted negative gap (IL assembly)

**Status**: Most mature certified result. A01's 9-module assembly covers
the restricted Ishida–LeBrun family. Not a full Yau 26 result but a
publishable theorem.

**What it proves**: For certain 4-manifolds without Einstein metrics,
sufficiently tight normalized negative Ricci pinching is impossible.

**What it lacks**: Dimension-only constants, positive branch, Lean.

### Route 2: Positive branch gap theorem (A02 primary)

**Status**: A02 has ℓ-classification and tower impossibility. The
(S²×S²)/Z₂ mixed-row computation is identified as the crux.

**Value**: If successful, P₄⁺ resolves all n ≥ 6 automatically.

**Obstacles**: Higher Biquard obstructions are subcritical. Either tower
rigidity or a global existence method is needed.

### Route 3: Surface bundle E_D

**Status**: Explicit δ→0 construction exists (manuscript Chapter 6).
Einstein nonexistence on E_D is OPEN. All standard exclusion mechanisms
fail (Hitchin–Thorpe satisfied, b₊ > 1, no general asphericity argument).

**Value**: If Einstein nonexistence proved, gives complete negative
counterexample for dim 4.

**Obstacles**: No known mechanism excludes Einstein metrics on E_D. The
harmonic-morphism route was invalidated (Step 69). The monodromy-specific
approach is unexplored.

### Route 4: Non-symmetric graph construction

**Status**: Unexplored. Requires full 4D Einstein PDE without reduction.

**Value**: Would complete the negative branch if successful.

**Obstacles**: No symmetry to exploit. Much harder than T²-invariant case.

## Recommended priorities

1. **Route 2 (positive branch)**: Highest strategic value. A02 leads.
   A03 can contribute through verification and complementary analysis.

2. **Route 1 (IL restricted gap)**: Certify A01's assembly as a standalone
   theorem. Nearest to completion.

3. **Route 3 (E_D nonexistence)**: Investigate monodromy-specific Einstein
   obstruction on surface bundles. Long shot but high value if successful.

4. **Route 4**: Defer unless Routes 2–3 fail.

## Key reusable assets

- Conformal gauge elliptic structure (det = 2k⁶) for any T²-invariant
  Einstein computation
- Drift-Laplacian/orbit-area identities and Frobenius mode data
- Weighted normal identity e^{2t}(H-3) = −3 − ∫e^{2s}|S−I|²ds
- Boundary Gauss compatibility: δ ≥ (9−H²)/6 for flat conformal class
- Isotropic impossibility (algebraic): s'+s²=1 vs s'+3s²=3
- All cutoff-flow and defect-hierarchy modules from Steps 17–61

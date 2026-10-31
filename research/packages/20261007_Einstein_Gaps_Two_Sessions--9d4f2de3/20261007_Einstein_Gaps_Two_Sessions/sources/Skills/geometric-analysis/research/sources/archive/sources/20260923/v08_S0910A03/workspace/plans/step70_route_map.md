# Step 70 Route Map (supersedes step68_route_map.md)

Session: S0910A03. Phase: Explore.

## New structural results from Step 70

### Critical identity (Theorem)
For any Ric=-3g metric on [0,R]×T³ with S(0)=0:
$$e^{2t}(H-3) = -3 - \int_0^t e^{2s}|S-I|^2 ds$$
- H < 3 at all finite times (exact cores approach cusp exponentially, never reach it)
- 3-H ≥ 3e^{-2t} (exponential approach rate)
- Approximate core with defect δ requires R ≥ ½log(6/δ) (necessary)
- For PE conformal infinity: R_{h₀} < -12 pointwise (flat AH cusp impossible)

### Elliptic correction
The T²-invariant system is elliptic (not hyperbolic). Step 69 numerical blow-up
was Hadamard ill-posedness of the elliptic Cauchy problem, not a geometric singularity.

### Peripheral algebra
Covers of type (N,1,1) exist iff b₁(M̄) > b₃(M̄). Verified algebraically.

## Updated route map

### Negative branch — graph manifold route
**Status:** Advanced but not complete.

**What we have:**
- Critical identity showing exact reflection cores exist to all time IF they
  don't develop finite-time singularities (which the identity doesn't exclude)
- Anisotropic quotient construction solving the lattice/scale mismatch
- Peripheral algebraic reduction: need b₃=0 for specific manifolds
- All flat-slice collars obstructed by H² ≥ 9-6δ
- Koiso local germ: exact, analytic, with H'(0)=3

**Key remaining question:** Does the exact Koiso extension survive to t=∞?
In the isotropic case (flat T³): YES, H=3tanh(t) → 3.
For nonflat scalar-minus-six centers: OPEN.
The intrinsic curvature decays as e^{-2a} → 0, suggesting stability
of the cusp attractor, but this needs proof (or a computable example).

**Construction pipeline if global existence holds:**
1. Koiso center q → exact Einstein half-core [0,∞)×T³ ✓ (if exists)
2. Truncate at R = ½log(6/δ) → defect ≈ 6e^{-2R} = δ ✓ (from identity)
3. Match to cusp via smooth transition → defect O(δ) ✓ (terminal layer easy)
4. Anisotropic quotient q_N → Vol = N^{-2}·Vol(q₁) ✓
5. Peripheral (N,1,1) cover → cusp matching ✓ (if b₃=0)
6. Graph gluing → closed manifold with Einstein exclusion ✓ (Di Cerbo)

### Negative branch — surface bundle route
**Status:** δ→0 achieved, Einstein nonexistence open.
Harmonic-map shortcut blocked (Ch.9 exact baseline).
Only monodromy-specific arguments could work.

### IL restricted module (A01 lead)
**Status:** Complete self-contained proof notes for all 9 modules.
Gives a geography-dependent gap for IL families, not dimension-only constants.

### Positive branch
**Status:** No known positive-Ricci/no-Einstein manifold.
A02 pursuing mixed A1 obstruction; remains the harder open direction.

## Research priorities for A03

1. **Global existence of Koiso extension** (the decisive question):
   - Stability analysis around the cusp attractor S=I
   - DeTurck BVP numerical experiment (elliptic, well-posed)
   - Energy/monotonicity methods for shear control
   
2. **Peripheral b₃ verification** for specific hyperbolic 4-manifold pieces

3. **If global existence fails:** approximate core construction using
   controlled defect in the transition layer (R ~ log(1/δ))

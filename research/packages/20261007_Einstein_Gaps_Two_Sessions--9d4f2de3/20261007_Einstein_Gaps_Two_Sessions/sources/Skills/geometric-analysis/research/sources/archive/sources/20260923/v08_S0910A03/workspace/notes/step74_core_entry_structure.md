# Step 75 scope correction

The bounded modified-Bessel basis does **not** give frequency-uniform stability for reflection data.  For the solution of
\(\psi''+3\psi'-k^2e^{-2t}\psi=0\) with \(\psi(0)=1\), \(\psi'(0)=0\),
\[
\lim_{t\to\infty}\psi(t)=\frac{\sinh k}{k},
\]
so the transfer grows exponentially with Fourier frequency.  The scalar Neumann--Dirichlet operator is invertible at each fixed mode, but this does not establish invertibility of the full nonlinear Einstein boundary map.  The CMC ODE below prescribes its curvature source and cannot determine a fixed physical core length; the normal balance requires a parameter-dependent length when both the defect and \(3-H(R)\) tend to zero.  An exact finite exit with vanishing anisotropy normal derivative is also incompatible with a nonconstant scalar-minus-six reflection center.  The valid material below is the mode equation, its two radial basis solutions, the fixed-mode energy identity, and the z-independent obstruction; all fixed-length and frequency-stability interpretations are superseded by Step 75.

# Step 74: Core-entry structure for graph-manifold Einstein construction

Session S0910A03. Agent2/Constructor. Phase Explore.

## 1. Z-independent impossibility (new)

**Theorem.** *No smooth Ric = −3g metric on [0,R) × T³ with a totally
geodesic T³ center exists in the diagonal T²-invariant class with
z-independent coefficients.*

**Proof.** For g = dt² + e^{2a(t)}dz² + e^{2b(t)}dx² + e^{2c(t)}dy²,
fiber slices are flat (Ric₃ = 0). The tangential sum gives H' + H² = 9,
the normal equation H' + |S|² = 3, so |S|² = H² − 6. At the reflection
center, H(0) = 0 and |S(0)|² = 0, giving 0 = −6, contradiction. □

**Approximate version.** For ‖E‖_op ≤ δ on such metrics, the center
constraint yields |H² − |S|² − 6| ≤ 4δ, hence δ ≥ 3/2. This is
precisely the collar barrier found in Step 63.

**Isotropic variant.** For isotropic S = sI, the tangential equation
forces Ric(q₀) = −2g₀ (negative Einstein on T³), impossible by
Preissmann (π₁(T³) abelian, no sec < 0). Every viable core must be
anisotropic from the start.

**Verification:** `scripts/step74_z_independent_impossibility.py` →
`data/step74_z_independent_impossibility.json`.

## 2. Corrected linearized mode analysis

Around the flat hyperbolic cusp g₀ = dt² + e^{2t}(dz² + dx² + dy²),
T²-invariant diagonal perturbations with Fourier mode cos(kz) satisfy
the linearized Einstein system:

- E₀₀ = 0: h″ + 2h′ = 0, where h = α + β + γ (trace). Solution:
  h = H₀ + De^{−2t}.
- E₀z = 0 (k ≠ 0): (β + γ)′ = 0, so w = β + γ = W (constant in t).
- E_xx − E_yy = 0: anisotropy ψ = β − γ satisfies

  ψ″ + 3ψ′ − k²e^{−2t}ψ = 0.

- E_zz gives coupling: 4D + k²W = 0.

### Bessel reduction (corrected from initial derivation)

Setting x = ke^{−t} and ψ = x^{3/2}z(x) gives the modified Bessel
equation with ν = 3/2:

  x²z″ + xz′ − (x² + 9/4)z = 0.

Solution: ψ = x^{3/2}[AI_{3/2}(x) + BK_{3/2}(x)].

**TTCS correction applied:** The initial derivation had an incorrect
prefactor x^{−3/2} from a chain-rule sign error. The correct prefactor
is x^{3/2}. Both branches are verified to machine precision against
direct ODE integration.

### Asymptotic behavior (as t → ∞, x → 0)

- I-branch: ψ ~ Cx³ = Ck³e^{−3t} → 0 (decays to zero)
- K-branch: ψ → √(π/2) ≈ 1.253 (approaches a nonzero constant)

**Both branches are bounded.** No exponentially growing modes exist.
This is consistent with the large-t limit ψ″ + 3ψ′ = 0, whose
solutions are const and e^{−3t}.

### BVP well-posedness

Since both branches are bounded, "Neumann + boundedness" provides only
one condition for a second-order ODE and does not determine a unique
solution. The correct BVP requires:

- **Neumann at center (t = 0):** ψ′(0) = 0 (reflection)
- **Dirichlet at far end (t = R):** ψ(R) = specified value

This gives a unique solution by the energy identity:

  (e^{3t}ψ′)′ − k²e^tψ = 0.

Multiplying by ψ and integrating on [0,R] with the boundary conditions
shows the homogeneous kernel is zero.

For k = 0, the equation is ψ″ + 3ψ′ = 0 with solution ψ = C + De^{−3t}.
Neumann at center fixes D = 0; the constant C is the cusp cross-section
shape modulus, which must be determined by the global geometry.

### Constraint propagation

The linearized contracted Bianchi identities give a first-order system
for (E_tt, E_tz). If all three tangential equations (E_zz, E_xx, E_yy)
are satisfied, then E_tt and E_tz satisfy a homogeneous system that
propagates from initial data. This requires compatible constraint data
on at least one boundary, and solving only the anisotropy equation is
not sufficient to control all five components.

**Verification:** `scripts/step74_corrected_mode_analysis.py` →
`data/step74_corrected_modes.json`.

## 3. Structural assessment

### What the mode analysis establishes

The absence of growing modes in the linearized system is **favorable**
for the core-entry construction. Center anisotropy does not amplify
toward the cusp; rather, the I-branch decays exponentially at rate 3.
This is consistent with Step 73's adiabatic tail module, which removes
O(1) anisotropy with O(K⁻¹) Ricci cost in the nonlinear regime.

### What the mode analysis does NOT establish

1. The center (S = 0) is far from the cusp (S = I) in the nonlinear
   sense. The linearized analysis applies near the cusp, not near the
   center. The center-to-cusp transition is a large-amplitude nonlinear
   problem.

2. The full constraint propagation requires solving all five Einstein
   components, not just the anisotropy difference equation.

3. The coupling relation 4D + k²W = 0 constrains the trace and sum
   modes jointly, introducing a nonlocal effect.

4. The Koiso center provides local existence near t = 0, but the
   global continuation to the cusp regime involves the full PDE
   dynamics, not just the ODE model.

## 4. Updated core-entry decomposition

The graph-neck construction now decomposes into three solved/open pieces:

| Module | Status | Key result |
|--------|--------|------------|
| **Tail** (Step 73) | SOLVED | Removes O(1) anisotropy with O(K⁻¹) defect |
| **Linearized modes** (Step 74) | FAVORABLE | No growing modes; BVP well-posed |
| **Nonlinear core** | OPEN | Center-to-cusp transition; CMC ODE model OK but PDE unproven |

The critical remaining problem: construct a sequence of approximate
metrics on [0,Rⱼ] × T³ with reflection center (S = 0), controlled
full Ricci defect, and near-cusp exit data at t = Rⱼ. The linearized
well-posedness and the CMC ODE (which naturally reaches cusp-like data)
are both supportive, but the nonlinear PDE existence remains open.

## 5. Positive branch status (from peer group)

A01 Step 77 (#521) withdrew the Step 76 claims about Ozuch obstructions
vanishing. The corrected status:
- TT kernel of P on (S²×S²)/Z₂ is zero
- Four non-TT scalar kernel modes u_iG_j exist
- ν_l equations cannot be deleted without proper slice derivation
- The decisive object is the inter-node singular-subtracted Green
  response H_{ij,2}, not the bare local curvature block
- A01 #524 further found that Bianchi-corrected local scalar projection
  is zero (cancellation between raw and coordinate-correction terms)

A02 Step 76 (#522) audited the product-Green factorization and corrected
the spectral denominator structure. The diagonal r=2 spin row is
identified as the clean first calculation target.

The positive branch remains active but technically immature: the
finite-dimensional obstruction map requires the full product P-resolvent
with additive spectral denominators, proper scalar slice, and D8 checks
before any coefficient can be evaluated.

## Files

- `scripts/step74_z_independent_impossibility.py` → `data/step74_z_independent_impossibility.json`
- `scripts/step74_corrected_mode_analysis.py` → `data/step74_corrected_modes.json`
- `trace/ttcs/results/step74_ttcs01_verifier1_integration.md` (independent verification)

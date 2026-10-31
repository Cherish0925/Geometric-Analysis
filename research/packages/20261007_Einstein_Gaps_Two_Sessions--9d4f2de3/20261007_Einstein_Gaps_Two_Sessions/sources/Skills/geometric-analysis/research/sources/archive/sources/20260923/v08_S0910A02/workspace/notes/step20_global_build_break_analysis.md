# Step 20: Global BUILD/BREAK analysis via stream-function modulus

Session S0910A02. Agent2/Constructor. Phase Execute.

## 0. Scope

The active Yau-26 target is unchanged. This step addresses the four-dimensional
positive branch toric crux: does the full coupled reduced Einstein system on the
periodic-label `#_k(S^2 × S^2)` polygon models admit solutions with total flux
→ 0 as `m = 2k+2 → ∞`, or is there a χ-uniform lower bound?

## 1. TTCS verification: the fork is NOT a pure eigenvalue question

A grounded TTCS verifier confirmed three critical corrections to the strategist's
proposed "clean 2D eigenvalue test":

**(a)** The volume-gap fork is NOT equivalent to whether `λ₁^Dir(Ω, g_B) ≈ 2`
permits small `∫w`. The eigenfunction scale is free analytically (`w → cw`
preserves all interior equations) but fixed geometrically by unit rod closure.
However, unit closure normalizes the COLLAPSING fiber slope, not the surviving
fiber value. The surviving fiber value q on a p-rod — which determines the
rod flux — is part of the coupled solution, not a prescribed quantity.

**(b)** `Area(Ω) ≥ c > 0` does NOT imply `∫w ≥ c' > 0`. The Faber-Krahn
area bound (if valid for curved polygons) controls a base length scale, but
`∫w` depends on the geometrically normalized amplitude. Without a Harnack or
Dirichlet-to-Neumann estimate tied to unit closure, area and volume are not
comparable. The Step 14 Euclidean Faber-Krahn constant also has a gap: it
applies to flat domains, not to arbitrary curved polygons.

**(c)** Boundary-localized negative curvature does NOT force λ₁ upward. By
domain monotonicity, an interior subdomain with `λ₁^D(U) ≤ 2+ε` gives
`λ₁^D(Ω) ≤ 2+ε` regardless of boundary curvature. McKean requires global
pointwise curvature control, not boundary-localized. Gauss-Bonnet total
curvature does not determine the spectrum.

**Correct formulation:** The decisive number is
$$
I_m = \inf_{(\Omega,g_B,w,v)\in\mathcal A_m} \left(-\int_{\partial\Omega}\partial_\nu w\,ds\right),
$$
where `A_m` is the admissible class of solutions to the FULL coupled reduced
system (eigenvalue + v-equation + traceless horizontal + Gauss-Bonnet + unit
closure) on even m-gons with periodic labels.

Evidence: `trace/ttcs/results/step20_ttcs01_verifier1_integration.md`.

## 2. Traceless horizontal equation: no new LOCAL obstruction

The traceless horizontal equation
$$
u_{zz} + \frac12(u_z^2 + v_z^2) = 0
$$
(u = log w, v = log(p/q), conformal z of g_B) was evaluated in flat rod-collar
coordinates. The CORRECTED computation gives a residual of exactly `(1+2A)/4`,
independent of `r` and `s`. This is confirmed numerically at multiple (A,s,r)
values with difference from expected `≤ 10^{-10}`.

**Interpretation:** This residual is NOT a new constraint. It equals the base
curvature effect (`K_B = -A` at the rod). The Step 19 corner matching already
checked the full Ricci tensor in FERMI coordinates of the curved base, where
both trace and traceless horizontal parts are automatically included. The flat-
base residual is a coordinate artifact from using flat coordinates for a curved
metric.

Evidence: `data/step20_traceless_horizontal_corrected.json`,
`scripts/step20_traceless_corrected.py`.

## 3. m=4 calibration: 33× gap between seed flux and actual minimum

For the rectangular model (m=4, S²×S²):

| Quantity | Seed (A=16) | Actual minimum |
|----------|-------------|----------------|
| Flux per rod | 2/33 ≈ 0.061 | 2 |
| Total flux | 8/33 ≈ 0.242 | 8 |
| `∫w` | 4/33 ≈ 0.121 | 4 |
| Vol₄ | 4.79 | 16π² ≈ 157.9 |

**Gap factor: 33×.** The local rod/corner data passes all Step 19 tests with
A = 16, but the full system forces A = 0 (flat base, square rectangle) as
the unique minimizer.

**Mechanism:** The eigenvalue constraint `π²/L_x² + π²/L_y² = 2` combined with
the AM-GM inequality on the product `L_x²L_y² ≥ π⁴` forces `flux = 8L_x²L_y²/π⁴ ≥ 8`.

For the non-separated (non-rectangular) case on the m=4 polygon, the Page metric
on a DIFFERENT topology (CP²#$\overline{\text{CP}}^2$, pentagon) shows that
non-flat bases DO occur, but the only known S²×S² Einstein metric is the product
(flat base, A=0).

Evidence: `data/step20_rectangular_flux_calibration.json`,
`scripts/step20_rectangular_flux_calibration.py`.

## 4. Stream function and conformal modulus approach

The v-equation `div(w∇v) = 0` gives a stream function `ψ` defined by
`dψ = *(w dv)`. On a p-rod, the outward flux of `w∇v` equals `∫q ds` = rod
flux `Φ_i`. So ψ is constant on each rod with jumps equal to the rod fluxes,
and total oscillation = total flux.

**Energy identity:**
$$
\int_\Omega |\nabla\psi|^2\,dA = \int_\Omega w^2|\nabla v|^2\,dA
= 2\int_\Omega w^2\,dA + 4\int_\Omega K_B w^2\,dA.
$$

For the square (K_B = 0): `∫|∇ψ|² = 2∫w² ≈ 4.93`, `flux² = 64`,
ratio ≈ 0.077.

**Path to BUILD theorem:** If the **conformal modulus** of the alternating-rod
polygon is bounded below uniformly in m, then the Dirichlet energy of ψ and the
flux are locked together, giving a χ-uniform flux lower bound.

The conformal modulus of the polygon with alternating Dirichlet boundary
conditions (ψ = const_i on rod_i) measures the "extremal length" of the family
of curves connecting p-rods to q-rods. If this modulus is bounded below by a
positive constant independent of m, the flux cannot collapse.

For the separated rectangle, the modulus is `L_y/L_x` (aspect ratio), and the
AM-GM constraint forces it to be bounded. For general m-gons, the analogous
estimate must use the full polygon geometry.

Evidence: `data/step20_global_energy_identity.json`,
`scripts/step20_global_energy_identity.py`.

## 5. The BUILD obstruction pathway

The results of this step identify a concrete mathematical path to a BUILD proof:

**Theorem target (conformal modulus lower bound):**
For the reduced polar Einstein system on a smooth `(2k+2)`-gon with periodic
labels, geodesic edges, right-angle corners, λ₁ = 2, and unit closure:
$$
-\int_{\partial\Omega}\partial_\nu w\,ds \ge c_0 > 0
$$
independently of k.

**Proof strategy sketch:**
1. The stream function ψ with boundary oscillation = total flux satisfies
   `∫|∇ψ|² = 2∫w² + 4∫K_B w²`.
2. By a modulus/capacity lower bound, `∫|∇ψ|² ≥ M · (total flux)²/P` where
   M is the conformal modulus and P is the perimeter.
3. The modulus M depends on the polygon's "conformal type". For alternating
   Dirichlet conditions on an m-gon, the modulus is controlled by the ratios
   of adjacent rod lengths and the interior geometry.
4. Combined with the energy identity, this gives a lower bound on total flux
   in terms of M, ∫w², and ∫K_B w².

**Current gap:** The modulus lower bound (step 3) is the unproved part. It
requires a geometric estimate showing that the polygon with many short rods
cannot have arbitrarily small conformal modulus.

## 6. What this changes

| Statement | Before Step 20 | After Step 20 |
|-----------|----------------|---------------|
| Traceless horizontal | Not checked beyond product | No local obstruction (verified) |
| m=4 gap | Not computed | 33× gap: seed flux 0.24 vs actual 8 |
| Fork type | "pure eigenvalue?" | Full coupled Dirichlet-to-Neumann |
| BUILD path | "energy identity?" | Stream function modulus (concrete) |
| Faber-Krahn area | "unconditional" | CONDITIONAL on curved isoperimetric |

## 7. Files

| File | Content |
|------|---------|
| `scripts/step20_traceless_corrected.py` | Corrected flat-base residual computation |
| `data/step20_traceless_horizontal_corrected.json` | Residual = (1+2A)/4, no new obstruction |
| `scripts/step20_rectangular_flux_calibration.py` | m=4 seed vs actual minimum |
| `data/step20_rectangular_flux_calibration.json` | 33× gap data |
| `scripts/step20_global_energy_identity.py` | Stream function and energy identity |
| `data/step20_global_energy_identity.json` | Modulus path to BUILD theorem |
| `trace/ttcs/results/step20_ttcs01_*` | TTCS verification records |

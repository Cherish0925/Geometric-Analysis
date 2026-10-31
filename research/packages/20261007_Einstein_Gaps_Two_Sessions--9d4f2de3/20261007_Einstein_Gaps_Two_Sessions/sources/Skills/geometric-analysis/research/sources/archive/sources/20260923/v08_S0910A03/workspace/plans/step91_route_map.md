# Step 91 route map: separator stability and the z-dependent frontier

> **Step 92 correction:** lines below that infer a positive-curvature requirement
> at a turning slice are superseded. Contracted Gauss gives
> \(R(q)=-6+D+\mathcal H^2-|II|^2\); at the minimal separator
> \(R(q)\le-6+4\delta\). The full weighted stability form, not the withdrawn
> curvature conflict, is the active direction.

## Established this Step

1. **Flat-slice barrier** kills the radial cylindrical charged throat:
   R(q_r) = 0 on constant-coefficient T³ slices → H² ≥ 9 - 6δ → δ ≥ 3/2
   for any smooth cylindrical interpolation. The Step 90 control program is
   unnecessary.

2. **Twist enters |II|² as Q**: O'Neill/Koszul formula gives
   |II|² = κ² + (1/2)h_ν² + (1/2)e_ν + Q, verified by TTCS with correct
   sign convention (ε = ±1 from orientation, squared contribution unambiguous).

3. **Separator stability → Q_C ≤ 3 + δ**: second variation with φ=1 on the
   ρ²γ_B-geodesic lift, combined with Ric(ν,ν) ≥ −3 − δ.
   Raised floor: ⟨e_s⟩ ≥ 12 − 8δ + 2Q_C.

4. **Resolvent does NOT constrain Q_C**: the modified ceiling grows with Q_+
   at rate ~8.86 vs. floor rate 2. The only twist bound is stability.

5. **Toral BH equivalence**: coordinate change φ = θ + kx reproduces the
   radial charged ansatz. Large Q_0 reflects a rotated T² subgroup, not
   new curvature. The "rapid Q redshift" is this coordinate rotation.

## Absorbed peer results

- **A01 #668**: same-chirality B_same = 0 universally; mixed-diagonal
  desingularization has trace obstruction Δ_tr = 0.503 t² > 0 at equal scales.
  If the convergence ladder confirms and the result extends to a rigorous
  nonexistence theorem, this identifies specific smooth 4-manifolds whose
  perturbative KE approach fails. It does NOT yet prove global Einstein
  nonexistence (non-perturbative solutions may exist).

- **A02 #653, #658**: gate-1 cleared via T² weight parity; selection rules
  corrected to anisotropy σ-matching; r=0 is degeneracy |P|=|Q|; Q-channel
  lives in tensor sectors AA/BB only; high-dimensional obstructions need
  non-4D-specific tools.

## The z-dependent frontier, corrected

The flat-slice barrier shows exactly what is needed for a free cylindrical
connector: intrinsically curved \(T^3\) slices. For any slice,
\[
R(q)=-6+D+\mathcal H^2-|II|^2.
\]
At the minimal separator \(\mathcal H=0\), the required scalar curvature is
negative. In arclength \(s\) along the base loop,
\[
R(q)=-2\partial_sh-\tfrac32h^2-\tfrac12e_s,
\]
so tangential orbit energy is one source of precisely that negative curvature.
There is no opposing positive-curvature requirement. Also, minimality
\(\mathcal H=0\) and stationarity \(\partial_r\mathcal H=0\) are distinct.

### Key open question

The minimizing loop supplies the complete invariant stability inequality
\[
\int_C\rho V\phi^2ds
\le\int_C\rho\bigl[(\phi_s)^2+(3-E_{\nu\nu})\phi^2\bigr]ds,
\quad
V=\kappa^2+\tfrac12h_\nu^2+\tfrac12e_\nu+Q,
\]
for every smooth periodic \(\phi\). The constant test sees only \(\langle V\rangle\).
The active question is whether the scalar identity, Maxwell transport, and the
orbit equation force twist or normal-energy concentration into a set whose
weighted capacity is too large for this Jacobi form, or whether two-variable
data can jointly satisfy all of them. Stability alone gives neither a
pointwise ceiling nor a universal concentration length.

### Parallel routes

1. **Two-variable construction**: Build z-dependent metrics on S¹ × ℝ base
   with negatively curved T³ slices, check whether the Bochner and separator
   constraints can be simultaneously satisfied.

2. **Curvature-energy tradeoff**: Derive the explicit relationship between
   R(q_r), e_s, and h_T for T²-invariant T³ slices. This is an intrinsic
   Gauss calculation on the 3D slice.

3. **Non-T² routes**: The S³-neck N#N route has no torus symmetry; the
   BCG scale δ ∼ 3/(4χ) is a lower bound only. The positive-branch
   desingularization obstruction (A01 #668) needs convergence and extension
   to global nonexistence.

None of these currently resolves the full Yau Problem 26 or begins the
required Lean formalization.

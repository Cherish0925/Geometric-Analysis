# Step 79: orthogonally transitive reduction and the weighted harmonic-map mechanism

Session `S0910A03`, Agent2 / Explore.

> **Step 80 correction.** The structural OT equations below remain useful, but the proposed cusp-based forcing budget and route interpretation are superseded by `workspace/notes/step80_joint_base_response_and_inner_layer.md`. In physical cusp radius the source weight is `e^{3r}`, not `e^{4r}`; common lattice scaling leaves the normalized orbit map `U` unchanged and does not imply `d_0=2 log N`; and a zero-mode transition on an already expanding cusp does not solve the reflected scalar-minus-six core-entry problem. The base stress equation shows that the base metric and orbit area must respond jointly in the first physical layer.

## 1. Overview: what the VII_0 barrier actually excludes

Step 78 proved that the Bianchi VII_0 rotating-eigenframe ansatz cannot reach the
Step 73 expanding-tail interface.  The barrier mechanism is the permanent positive
feedback: K = 2k²a⁻²sinh²d increases monotonically because the angular velocity
ψ_z = k is frozen.  This Step derives the **full** orthogonally transitive (OT)
T²-invariant Einstein system and identifies the structural mechanism by which
**general** solutions can break the VII_0 barrier.

The key insight: the orbit part of the Einstein system is a **weighted harmonic map
to H²** = SL(2,ℝ)/SO(2), and the weight grows exponentially due to the cosmological
constant Λ = −3.  The VII_0 ansatz restricts the orbit map to a helicoidal geodesic
in H², freezing the angular degree of freedom.  General two-base-variable solutions
allow the angular momentum to be absorbed by the growing weight, removing the
positive feedback that drives contraction.

## 2. Twist vanishing on reflected Einstein cores

For commuting Killing fields X, Y on a manifold with Ric = −3g, the rank-two
twist scalars
\[
  c_X = *(X^\flat \wedge Y^\flat \wedge dX^\flat),
  \qquad
  c_Y = *(X^\flat \wedge Y^\flat \wedge dY^\flat)
\]
are **constant** (the Einstein and Killing identities together force dc_X = dc_Y = 0).
A reflection fixing the central hypersurface pointwise reverses orientation, hence
reverses the Hodge star, and sends c_X → −c_X.  Since c_X is constant: c_X = 0.
Similarly c_Y = 0.

**Consequence:** Exact reflected Einstein cores with free T² action are orthogonally
transitive.  The horizontal distribution (orthogonal to T² orbits) is integrable.

**Distinction:** Off-diagonal orbit metric G_{xy} ≠ 0 is **not** twist.  Twist measures
the non-integrability of the horizontal distribution.  Off-diagonal G records the
shape of T² orbits in SL(2)/SO(2).  Both exist in orthogonally transitive geometry.
The Li–Liu A(r,z) term in dy + Adx is an off-diagonal orbit metric entry, not a twist.

**For approximate cores** (Ric = −3g + E): the twist scalars are no longer constant
but satisfy dc_X = O(‖E‖), with a geometry-dependent conversion.  A uniform
small-twist estimate on a long collapsing or expanding connector requires separate
analysis.

## 3. The full orthogonally transitive Einstein reduction

### Metric and variables

\[
  g = e^{2\lambda}(dr^2 + dz^2) + G_{ab}(r,z)\,d\xi^a d\xi^b,
  \tag{3.1}
\]
where (r,z) parametrize the 2D base in conformal gauge, and (ξ^1, ξ^2) = (x,y)
are the T² orbit coordinates.  All functions depend on (r,z) only.

Decompose the orbit metric:
\[
  G = e^\sigma M, \qquad
  \sigma = \tfrac12\log\det G,\qquad
  \det M = 1.
  \tag{3.2}
\]
The unimodular matrix M parametrizes a point in H² = SL(2,ℝ)/SO(2).

### Iwasawa coordinates on H²

In the Iwasawa parametrization:
\[
  M = \begin{pmatrix}
  e^\alpha + \beta^2 e^{-\alpha} & \beta e^{-\alpha} \\
  \beta e^{-\alpha} & e^{-\alpha}
  \end{pmatrix},
  \qquad \det M = 1,
  \tag{3.3}
\]
with (α, β) ∈ ℝ².  The H² metric is ds²_H = dα² + e^{−2α}dβ².

### Polar coordinates on H²

In geodesic polar coordinates (d, ψ) with d = geodesic distance from identity:
\[
  ds^2_H = dd^2 + \sinh^2(d)\,d\psi^2.
  \tag{3.4}
\]
The diagonal case has β = 0 and α = d; VII_0 has d = d(r), ψ = kz.

## 4. Structural equations (Ric = −3g)

### 4.1. Area equation (orbit Ricci trace)

\[
  \boxed{
  \sigma_{rr} + \sigma_{zz} + \sigma_r^2 + \sigma_z^2 = 6\,e^{2\lambda}.
  }
  \tag{4.1}
\]
Equivalently, with ρ = e^σ:
\[
  \Delta\rho = 6\,e^{2\lambda}\rho.
  \tag{4.2}
\]
This is the Liouville-type area equation.  The cosmological constant Λ = −3
appears on the right-hand side and drives **exponential growth** of the orbit area.

### 4.2. Orbit map equation (orbit Ricci traceless part)

\[
  \boxed{
  \operatorname{div}\!\bigl(e^\sigma M^{-1}\,dM\bigr) = 0.
  }
  \tag{4.3}
\]
This is the **weighted harmonic map equation** from (base, flat dr² + dz²) to
(H², g_H²), with weight e^σ.

In H² polar coordinates (d, ψ):
\[
  \underbrace{(e^\sigma d_r)_r + (e^\sigma d_z)_z}_{\text{weighted Laplacian of }d}
  = e^\sigma\sinh(d)\cosh(d)\bigl(\psi_r^2 + \psi_z^2\bigr),
  \tag{4.4}
\]
\[
  \boxed{
  (e^\sigma\sinh^2\!\!(d)\,\psi_r)_r
  + (e^\sigma\sinh^2\!\!(d)\,\psi_z)_z = 0.
  }
  \tag{4.5}
\]
Equation (4.5) is a **conservation law** for the angular momentum current
J_i = e^σ sinh²(d) ψ_i.

In Iwasawa coordinates (α, β) with ds²_H = dα² + e^{−2α}dβ²:
\[
  (e^\sigma \alpha_r)_r + (e^\sigma \alpha_z)_z
  = -e^{\sigma - 2\alpha}\bigl(\beta_r^2 + \beta_z^2\bigr),
  \tag{4.6}
\]
\[
  (e^{\sigma-2\alpha}\beta_r)_r + (e^{\sigma-2\alpha}\beta_z)_z = 0.
  \tag{4.7}
\]
**Correction:** The sign in (4.6) is negative because the Christoffel symbol
Γ^α_{ββ} = e^{−2α} > 0 in these coordinates.  In the diagonal case β = 0,
both sides vanish and the sign is immaterial.  The polar-coordinate
d-equation (4.4) has the correct positive sign because
Γ^d_{ψψ} = −sinh(d)cosh(d) < 0.

### 4.3. Base conformal factor

From the sum of base-base Einstein equations:
\[
  \boxed{
  \Delta\lambda = \frac{|\nabla\sigma|^2 - e_{H^2}}{4},
  }
  \tag{4.8}
\]
where
\[
  e_{H^2} = |\nabla\alpha|^2 + e^{-2\alpha}|\nabla\beta|^2
  = |\nabla d|^2 + \sinh^2(d)|\nabla\psi|^2
  \tag{4.9}
\]
is the H² energy density of the orbit map.

### 4.4. Base constraints

The difference equation (Ric_{rr} − Ric_{zz} = 0) and the cross equation
(Ric_{rz} = 0) provide the conformal-gauge conditions:
\[
  \sigma_{rz} = \sigma_r\lambda_z + \sigma_z\lambda_r
  - \tfrac12\sigma_r\sigma_z - \tfrac12 e_{H^2,rz},
  \tag{4.10}
\]
where $e_{H^2,rz}$ is the symmetric inner product of the orbit map gradients.

## 5. Verification on known solutions

### 5.1. Round cusp (H⁴)

For g = dr² + e^{2r}(dz² + dx² + dy²) in conformal coordinates t = −e^{−r}:
λ = −log(−t), σ = −2log(−t), orbit map trivial (M = I).

- Area: 6/t² = 6/t²  ✓
- Conformal: 1/t² = 4t^{−2}/4 = 1/t²  ✓
- Ric_{rr}: −3/t² = −3/t²  ✓
- Orbit Ric: −3G  ✓

### 5.2. Step 73 expanding tail

For g = dr² + e^{2r}[dz² + N^{−2}e^v dx² + N^{−2}e^{−v}dy²]:
σ = 2r − 2logN, α = v, β = 0.  Orbit equation (4.6) gives:
\[
  v_{rr} + 3v_r + e^{-2r}v_{zz} = 0,
  \tag{5.1}
\]
exactly Step 73's equation.  Linearized: ψ″ + 3ψ′ − k²e^{−2r}ψ = 0,
exactly the Step 74/75 mode equation.  ✓

## 6. The mechanism breaking the VII_0 barrier

### 6.1. VII_0 as a restricted orbit map

In VII_0, the orbit map is **helicoidal** in H²:
\[
  (r,z) \mapsto \bigl(d(r),\, kz\bigr) \in (H^2,\,dd^2+\sinh^2\!\!(d)\,d\psi^2).
\]
The angular velocity ψ_z = k is **fixed**.  The d-equation becomes:
\[
  (e^\sigma d')' = e^\sigma\sinh(d)\cosh(d)\,k^2,
  \tag{6.1}
\]
whose right-hand side is always positive for d > 0.  This forces d to increase
monotonically, creating the VII_0 barrier.

The conservation law (4.5) is trivially satisfied because everything depends
only on r.  **The angular degree of freedom is frozen.**

### 6.2. General orbits: angular relaxation

In a general 2-variable solution (d(r,z), ψ(r,z)), the conservation law (4.5)
constrains ψ but does not freeze it.

**Integrated conservation:** Integrating (4.5) over a z-circle at radius r:
\[
  \Phi(r) := \int_{S^1} e^\sigma\sinh^2\!\!(d)\,\psi_r\,dz = \text{const in }r.
\]
At a reflected center (r = 0): ψ_r(0,z) = 0, hence **Φ ≡ 0**.

The mean z-flux satisfies no similar conservation; it evolves as:
\[
  \frac{d}{dr}\int_{S^1} e^\sigma\sinh^2\!\!(d)\,\psi_z\,dz
  = -\int_{S^1}\partial_z(e^\sigma\sinh^2\!\!(d)\,\psi_z)\,\psi_z\,dz
\]
(from differentiating and using (4.5)), which depends on the z-profile.

### 6.3. The key mechanism

In an **expanding region** where σ grows (driven by the area equation (4.1)
through Λ = −3):

1. **Escape from the VII_0 ODE region:**  General two-variable maps to H²
   are not subject to the Step 78 invariant-region argument, because the
   angular gradient ∇ψ can vary with (r,z) rather than being frozen at k.
   The d-equation source sinh(d)cosh(d)|∇ψ|² can become small where
   |∇ψ| decreases, removing the monotone forcing.

2. **Conservation and redistribution:** The angular conservation law (4.5) governs
   ψ but does not freeze it.  On a circle: d/dr ∫ ρ sinh²(d) ψ_r dz = 0, and
   the reflected center forces this flux to vanish.  The z-averaged angular
   z-flux ∫ ρ sinh²(d) ψ_z dz is **not** directly controlled by the
   conservation law; its evolution depends on the z-profile.  Therefore
   "growing e^σ absorbs angular momentum" is a possible mechanism, not a
   conservation-law consequence.

3. **H² negative curvature:** The target space H² has sectional curvature K = −1.
   For maps from a cylinder to a negatively curved space, there is **no topological
   obstruction** to energy decay.  The energy density can decrease, unlike for
   maps to S² where concentration phenomena arise.

4. **Cosmological constant role:** The area growth is driven by Λ = −3 through
   equation (4.1).  In the vacuum Ernst reduction (Λ = 0), the area is
   **harmonic** and the mechanism is absent.

5. **Full matrix Noether flow (TTCS correction):**  The orbit equation gives
   a matrix conservation law
   \[
     \mathcal Q(r) = \int_{S^1}\rho\,M^{-1}M_r\,dz \equiv 0
   \]
   (from reflection).  This is an sl(2,ℝ)-valued constraint stronger than the
   scalar angular flux.

This is exactly the mechanism already realized in the Step 73 expanding tail:
the anisotropy function v decays on the expanding background because the
weighted Laplacian equation (5.1) admits decaying solutions.

### 6.4. Comparison table

| Feature | VII_0 | General OT |
|---------|-------|------------|
| Base dependence | r only | (r,z) both |
| H² map | geodesic d(r) + linear ψ=kz | full (d,ψ)(r,z) |
| Angular freedom | frozen ψ_z = k | ψ(r,z) evolves via conservation |
| d-equation source | sinh·cosh·k² > 0 always | sinh·cosh·|∇ψ|² ≥ 0, can vanish |
| d monotone? | YES (barrier theorem) | NOT NECESSARILY |
| Weight growth | a shrinks (contraction) | e^σ can grow (expansion) |
| Tail realization | unreachable | Step 73 tail works |

## 7. Boundary conditions for the finite connector

A finite connector from a reflected center (r = 0) to the Step 73 tail
interface (r = R → ∞) requires:

**At r = 0** (reflection):
\[
  d_r(0,z) = \psi_r(0,z) = \sigma_r(0,z) = \lambda_r(0,z) = 0.
\]

**At the exit** (r = R, approaching tail interface):
\[
  d(R,z) \to 0, \quad \psi_z(R,z) \to 0, \quad
  S \approx I, \quad \text{scaled slice curvature} \to 0.
\]

**Conserved quantity:** Φ = 0 (radial angular flux) at all r.

**Center data:** The center metric q₀ has R(q₀) = −6 and carries
order-one anisotropy energy:
\[
  \langle d_s^2\rangle_\rho \ge 12 - 8\delta
  \tag{7.1}
\]
(Step 76 identity).  This center energy must be transported outward and
dissipated by the expanding weight.

## 8. What this Step establishes and what remains

### Established

- The full OT T²-invariant Einstein system reduces to a **weighted harmonic map
  to H²** coupled to area and conformal-factor equations (§4).
- This is verified on the round cusp and Step 73 tail (§5).
- The VII_0 barrier is a **frozen angular momentum** phenomenon, not a general
  property of the orbit map space (§6).
- General OT solutions can relax angular momentum through the expanding weight,
  removing the positive feedback that drives d growth (§6.3).
- Twist vanishes on exact reflected cores (§2).

### Not established

- **Existence** of a finite vanishing-defect connector solving the full coupled
  system with the required boundary conditions.  The structural escape from
  VII_0 is identified, but no explicit solution or numerical evidence for the
  full nonlinear problem has been produced.

- **Convex distance maximum principle (TTCS, critical):**  For **exact** Einstein
  connectors, the function F(U) = ½d²_{H²}(U, P) satisfies
  div(ρ∇(F∘U)) ≥ ρ|dU|², because H² has curvature −1 and Hess(F) ≥ g_{H²}.
  On a reflected cylinder with constant outer boundary U = P, this forces
  U ≡ P.  **An exact Einstein connector cannot relax nontrivial center data
  to a constant orbit map at a finite exit.**  The construction therefore
  requires approximate connectors with ‖E‖_∞ → 0.  For those, the forcing
  term on the RHS of (4.3) is sourced by E_orbit, and the weighted
  accumulation e^{2λ}ρ E°_orbit can remain O(1) even as ‖E‖ → 0 on a
  long expanding connector.  Whether this defeats the maximum principle is
  the decisive open question.

- Whether additional conservation laws (the matrix Noether flow, weighted
  stress balance, or monotone quantities from the coupled system) prevent
  the orbit energy from decaying.

- The precise role of the base constraints (4.10) in restricting the connector
  geometry.

- Extension to the positive branch or higher dimensions.

## 9. Files

- `workspace/scripts/step79_ot_einstein_reduction.py` and
  `workspace/data/step79_ot_reduction.json`: structural reduction and energy
  identity verification.
- `workspace/scripts/step79_verify_cusp_tail.py` and
  `workspace/data/step79_verifications.json`: round cusp and tail verification.
- Independent TTCS branches: `trace/ttcs/results/step79_ttcs01_*`.

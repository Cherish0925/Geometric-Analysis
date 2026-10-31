# Step 81: constant-speed-loop centers, angular-slip analysis, and the reflected collapse mechanism

Session `S0910A03`, Agent2 / Execute.

## 1. Summary of results

This Step established five structural results for reflected Einstein evolution
from T²-invariant centers on T³, with two key corrections from TTCS.

### Results established

1. **Exact orbit-matrix parametrization**: M=cosh(d)I+sinh(d)n(θ) with
   n(θ)=[[cosθ,sinθ],[sinθ,-cosθ]], n²=I. The SL(2)/SO(2) metric is
   dd²+sinh²(d)dθ². Rotating loop d=d*, θ=kz has energy k²sinh²(d*)=12
   for R(q₀)=-6 with constant area. (θ is the H² polar angle, not the
   eigenframe angle; the eigenframe rotates at θ/2.)

2. **Exact S'(0) eigenvalue formula** (TTCS-derived):
   $$
   \operatorname{Spec}S'(0) = \{-3,\; 3+\sqrt{3(k^2+12)},\; 3-\sqrt{3(k^2+12)}\}.
   $$
   For k=2: orbit eigenvalues 9.928 and -3.928. For k=8: 18.100 and -12.100.
   The orbit eigenvalue split L=√(3(k²+12))=6 coth(d*). The z-eigenvalue -3
   is universal for all constant-area R=-6 centers.

3. **Angular-slip energy cancellation** (corrected): The perturbation
   d=d*+ε cos(q z), θ=kz-(k/q)coth(d*)ε cos(qz)
   preserves the orbit **energy trace** to O(ε²):
   $$
   |U_z|^2 = 12 + \varepsilon^2[q^2\sin^2(qz)-(2k^2+12)\cos^2(qz)]+O(\varepsilon^3).
   $$
   For k=2, q=1: max deviation coefficient = 20, matching numerics.
   
   **TTCS correction**: The angular slip does NOT preserve the full orbit Ricci
   tensor to first order. Only the scalar/Ric_zz cancellation holds. The
   traceless orbit Ricci changes at O(ε), so S'(0) orbit eigenvalues change
   at O(ε) even though the z-eigenvalue changes only at O(ε²).

4. **Volume-weighted universal contraction** (corrected): With ρ=√(det G)
   as the geometric volume weight:
   $$
   \boxed{\langle u'(0)\rangle_\rho = -3}
   $$
   for **any** area profile, not just constant area. The non-weighted
   result ⟨u'(0)⟩_s = -3+⟨h²⟩_s uses unit arclength, not geometric volume.
   Non-constant area satisfies the coupling constraint e=12-4ḣ-3h²≥0.

5. **VII₀ finite-distance collapse** (rigorous): For exact Einstein on the
   Bianchi VII₀ system, K≥6 implies H'≤3-H²≤3, giving H≤√3. Then
   $$-u(r) \geq \sqrt{3}(1-e^{-\sqrt{3}r})$$
   forces K to grow beyond 10, after which H'≤-1-H² gives
   (arctan H)'≤-1, and the solution cannot exist on arbitrarily long
   intervals. Numerical collapse radii: k=2: r=0.362; k=3: 0.340;
   k=4: 0.316; k=6: 0.274; k=8: 0.241.

### TTCS-established scope limitations

- The VII₀ collapse proof relies on K=-R(q_r) being a single scalar with
  monotone feedback. In the full z-dependent OT system, R(q_r) involves
  area derivatives, matrix-map energy, and spatial derivatives with no
  known analogous monotone quantity. **The collapse does NOT generalize to
  the full z-dependent system by the present argument.**

- The convex-distance maximum principle (Step 79) excludes exact Einstein
  connectors with constant exit orbit map, but approximate connectors have
  weighted forcing e^{2λ}ρ||E||_orbit that can accumulate over long cylinders.

- Non-reflected metrics (S(0)≠0) are not covered by the universal -3 result.

## 2. Orbit matrix and scalar curvature

In SL(2,ℝ)/SO(2) with the Cartan metric:

$$
\frac12\operatorname{tr}((M^{-1}dM)^2) = dd^2 + \sinh^2(d)\,d\theta^2.
$$

For M = cosh(d)I + sinh(d)n(θ):
- det M = 1 ✓
- M⁻¹ = cosh(d)I - sinh(d)n(θ) ✓  
- Eigenvalues e^{±d}, so M is positive definite ✓

For constant-area center q₀=dz²+M(z)dx²:
$$
\mathcal{A} = \frac12 M^{-1}M_z,\qquad
|\mathcal{A}|^2 = \frac14\operatorname{tr}(Q^2) = \frac12|U_z|^2_{H^2}.
$$

Flat T² orbits: Ric(q₀)_{zz} = -|A|², R(q₀) = -|A|² = -½|U_z|².
So R=-6 ⟺ |U_z|²=12 ⟺ k²sinh²(d*)=12 for a rotating loop.

Verified numerically for k=1,2,3,4 with Nz=512; e_{H²} deviates from 12
by at most 0.01 (finite-difference error).

## 3. Exact S'(0) eigenvalues

For the reflected germ S(0)=0, S'(0) = Ric(q₀)+3I.

**z-direction**: S'_z = -|A|²+3 = -6+3 = -3 (universal for constant area).

**Orbit direction**: For d=d*, θ=kz, the traceless part of Ric_orbit has
eigenvalues ±L where
$$
L = \frac{k^2}{2}\sinh(d_*)\cosh(d_*) = 6\coth(d_*) = \sqrt{3(k^2+12)}.
$$

Full S'(0) spectrum:
$$
\{-3,\; 3+\sqrt{3(k^2+12)},\; 3-\sqrt{3(k^2+12)}\}.
$$

| k | d* | S'_z | S'_orbit+ | S'_orbit- | min |
|---|-----|------|-----------|-----------|-----|
| 1 | 1.956 | -3 | 9.245 | -3.245 | -3.245 |
| 2 | 1.317 | -3 | 9.928 | -3.928 | -3.928 |
| 3 | 0.987 | -3 | 10.937 | -4.937 | -4.937 |
| 4 | 0.783 | -3 | 12.162 | -6.162 | -6.162 |
| 8 | 0.421 | -3 | 18.100 | -12.100 | -12.100 |

The min eigenvalue is always the orbit minus direction (except for k=1
where it's close to -3). Higher k gives faster orbit contraction.

## 4. Angular-slip energy cancellation (corrected)

For d=d*+ε cos(qz), θ=kz+εb sin(qz) with b=-(k/q)coth(d*):

$$
|U_z|^2 = 12 + \varepsilon^2[q^2\sin^2(qz) - (2k^2+12)\cos^2(qz)] + O(\varepsilon^3).
$$

**Numerical verification** (k=2, q=1):
- ε=0.01: max|speed²-12|=0.002, ratio/ε²=20.09
- ε=0.10: max|speed²-12|=0.209, ratio/ε²=20.88
- ε=0.50: max|speed²-12|=5.589, ratio/ε²=22.36

The limit coefficient is exactly 20 = 2k²+12-q² = 2·4+12-1 = 19 maximum
and q²=1 minimum, range [-20,1]. Max deviation is 20ε².

**Critical correction**: The angular slip preserves the **trace** |U_z|² to
O(ε) but NOT the full orbit Ricci. From the TTCS-derived formula:
$$
Q' = -k^2sc\,n + \varepsilon[-mq c^2 \sin(qz)\,t + mqsc\sin(qz)\,J + \ldots] + O(\varepsilon^2)
$$
where s=sinh(d*), c=cosh(d*). The traceless part of Q' changes at O(ε).

Therefore: **u'(0,z)=-3+O(ε²) everywhere, but the orbit S' eigenvalues
change at O(ε)**. The angular slip provides an O(ε) orbit-Ricci perturbation
on top of the unchanged z-contraction.

## 5. Volume-weighted universal contraction (corrected)

For **any** reflected center (constant or non-constant area):
$$
\langle u'(0)\rangle_\rho = \frac{\int u'(0,s)\rho(s)\,ds}{\int\rho(s)\,ds} = -3.
$$

Proof: for q₀=ds²+G(s), ρ=√(det G), h=ρ'/ρ:
$$u'(0,s) = 3 + \dot{h} + h^2 - 6 = -3+\dot{h}+h^2.$$
Volume-weight: ⟨ḣ⟩_ρ = -⟨h²⟩_ρ (integration by parts with ρ̇=hρ).
So ⟨u'(0)⟩_ρ = -3+⟨ḣ⟩_ρ+⟨h²⟩_ρ = -3.

The coupling constraint: e=12-4ḣ-3h² ≥ 0 (orbit map energy must be ≥ 0)
limits how much area variation can be introduced.

## 6. VII₀ collapse mechanism (rigorous)

For exact Einstein on the Bianchi VII₀:
1. K(0)=6 ≥ 3, so u'(0)=-3 < 0.
2. H'=9-H²-K ≤ 9-K ≤ 3, so H ≤ √3 tanh(√3r) < √3.
3. From u'+Hu=3-K with K≥6: -u(r) ≥ √3(1-e^{-√3r}).
4. (log K)' = -2u+2 coth(d)d' ≥ -2u ≥ 2√3(1-e^{-√3r}).
5. K grows beyond 10 in finite radius; then H'≤-1-H² forces blowup.

The collapse is a genuine curvature singularity: a→0, d→∞, K→∞.

**Does not generalize to z-dependent case**: The full OT orbit equation
div(ρ M⁻¹∇M)=0 allows flux redistribution between the r and z directions,
subject to the Noether constraint ∫ρ M⁻¹M_r dz = 0. This breaks the
scalar monotone mechanism that drives the VII₀ collapse.

## 7. Implications for the graph construction

**What is now excluded**:
- The VII₀ subclass (any even winding, z-independent) cannot connect a
  reflected R=-6 center to the Step 73 expanding tail with ||E||_op ≤ 3/5.
  This is a rigorous O(1) defect lower bound for this ansatz.

**What remains open**:
- Full z-dependent OT system with the coupled (γ_B, σ, M) equations.
  The orbit equation has genuinely new matrix transport directions.
- Non-constant-area centers (volume-weighted average is still -3, but
  non-weighted average can be shifted; coupling constraint limits this).
- Non-reflected metrics (S(0)≠0): the universal -3 result does not apply.
- Non-OT geometry (twist forced by defect in approximate case).

**The decisive open problem**: Does the full coupled (γ_B, σ, M) system
on the first O(1) layer admit a monotone or non-local quantity that
inherits the VII₀ feedback, or does the spatial redistribution genuinely
provide an escape? This determines whether the graph-manifold route is
fundamentally blocked or merely technically difficult.

## 8. Files

- `workspace/scripts/step81_geodesic_loop_center.py`: parametrization and 3D Ricci
- `workspace/scripts/step81_evolution.py`: S'(0) eigenvalues and VII₀ evolution
- `workspace/scripts/step81_contraction_analysis.py`: energy preservation and contraction
- `workspace/data/step81_geodesic_loop_center.json`
- `workspace/data/step81_evolution.json`
- `workspace/data/step81_contraction_analysis.json`
- `trace/ttcs/results/step81_ttcs01_verifier1_integration.md`

**Supersession notices**:
- Step 80 angular_slip.json condition "m²sinh²d=12" is correct in the H² polar convention
  (where θ=kz and the eigenframe rotates at k/2). But the claim that "angular slip
  preserves orbit Ricci to first order" is false: only the energy trace is preserved.
- Step 80 route_map.md: the VII₀ collapse is rigorous but does not generalize
  to the z-dependent system.

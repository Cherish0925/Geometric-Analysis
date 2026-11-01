# TTCS Independent Branch Record

```json
{
  "step_id": 67,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step80_Q4_universal_functional_and_lambda_quadratic.md",
    "Sessions/S1003A02/workspace/data/step80/lambda_scan_a.json",
    "Sessions/S1003A02/workspace/data/step80/universal_pi.json",
    "Sessions/S1003A02/workspace/data/step80/recon_F012_gen2_lam0.json",
    "Sessions/S1003A02/workspace/data/step80/recon_F012_gen5_lam-5.json",
    "Sessions/S1003A01/workspace/notes/step62_torsion_zero_prolongation.md",
    "Sessions/S1003A01/workspace/notes/step65_homogeneous_torsion_zero_classification_and_surface_transport.md",
    "Sessions/S1003A01/workspace/data/step67/verify_A02_step80_reconstructions.json"
  ]
}
```

## Task

Analyze the corrected order-6 scalar functional scientifically. Read A02's Step-80 note/data and A01's independent verification. Develop a coordinate-free interpretation or at least a sharp invariant ansatz for the universal multiplier and Phi6 on the first-jet cone, respecting U(2) invariance and weighted homogeneity. Explain why F0,F1,F2 can each change sign, identify plausible invariant generators and dimensionless ratios, and propose exact symbolic/numerical experiments that could recover the formula without assuming the earlier false positivity. Also assess whether compact negative Einstein almost-Kahler geometry supplies any known pointwise/global control of the torsion-derivative-to-lambda ratio that could make this finite-order law globally useful.

## Output

# Memo: the order-6 scalar functional Φ₆, its invariant structure, and its global relevance

## 0. Summary

- **Cross-checks.** A01's file `verify_A02_step80_reconstructions.json` independently reproduces the Step-80 order-6 jets. It matches the monomial indexing and the anti-J₀ basis. It recomputes Φ₆ = −0.16528, −0.23691 and −0.41612. It gets per-order residuals equal to A02's to two digits, cone residual about 1e-16, and index +1. The control jet keeps the residual 4.64 with `phi_at_saved_z = Φ₆ = 0.8419`. The order-6 existence statement in the even branch therefore stands as a floating-point result.

- **What fixes the form of Φ₆.** Four structural facts, derived below, determine much of its shape:
  1. a cokernel count that identifies ℓ with the spherical-mean component of one scalar compatibility;
  2. a Schur-complement form that makes Φ₆ rational, with the λ-quadratic law following from where λ enters;
  3. a complex-dilation (μ = i) symmetry that makes the even-branch formal theory blind to the sign of λ;
  4. U(2) invariant theory with an explicit generator list, a 4-dimensional orbit space on the unit cone, and a unique cubic invariant that controls F₁.

- **Two corrections to the reading of Step 80.**
  - The order-6 law was computed on the even branch (H₃ = 0). There is also strong evidence that it was computed on the slice W⁻(p) = 0. A zero of a closed manifold need not be even and has free W⁻(p). The statement "every nondegenerate zero satisfies Φ₆ ≤ 0" in §5.2–5.3 therefore does not yet apply to closed manifolds.
  - The withdrawn λ = −40 value is actually supported by the data.

- **Global use.** No known global input controls the ratio Λ = λ/tn² at zeros in the direction that would be needed. Even perfect control of Λ would not make the even-branch order-6 law decisive.

## 1. Data-level points

**The λ = −40 entry.**
- In `lambda_scan_a.json`, the rank-13, indefinite, sign-flipped record (`Hr_eig_max` 5.9e-15, `cos_ref` −1) is jet_index 1.
- Jet 0 at λ = −40 has quad_rank 12, a definite form, and Φ₆ = −0.19221. This lies on its own quadratic fit: 0.82202 + 0.84208 − 1.85630 = −0.19220.
- `recon_lsA_jet0_lam-40` reported rank 13 for the same point. The rank decision is therefore tolerance-sensitive. The Hr eigenvalues scale roughly like λ⁻² at large |λ|: Hr_eig_min is 0.204 at λ = 0, 0.0144 at λ = ±5, and 2.45e-4 at λ = ±40. This points to a λ-dependent basis normalization. A threshold relative to the largest eigenvalue would stabilize the rank.
- Jet 1 at λ = −40 is predicted by its quadratic to give 0.24820 − 0.12252 − 0.32552 ≈ −0.200.

**Zero sets of the two λ-scan jets.** Both fitted quadratics have F₂ < 0. Their roots are:
- jet 0: Λ ≈ −37.2 and +19.1, consistent with Φ₆(20) = −0.063;
- jet 1: Λ ≈ −28.2 and +43.3, consistent with Φ₆(40) = +0.045.

So both "obstructed" jets become unobstructed in the strongly near-Kähler ratio |Λ| ≳ 30.

**gen2.** With (F₀, F₁, F₂) = (−0.165, 0.014, 2.1e-5), Φ₆ < 0 for roughly −7×10² < Λ < 12. This covers essentially all λ < 0.

**Size of the reconstructed jets.** At unit torsion the Taylor coefficients are large: ‖H₄‖ ~ 2×10³ and ‖H₈‖ ~ 5×10⁶ for gen2 at λ = 0. This comes from z* = −H_π⁻¹j combined with a small H_π eigenvalue. A crude root test, ‖H_k‖^{1/k} ≈ 7, suggests a formal radius of order 0.1 in torsion units. The monomial-basis norms are not invariant, so Fischer/Bombieri norms should be used before reading growth (and convergence) from these numbers. The control jet's ‖H₈‖ = 3.5e14 is the least-squares blow-up of an inconsistent system, as expected.

## 2. The surviving row is the spherical mean of one scalar compatibility

**Cokernel count.** The flat L₆ has a 259-dimensional cokernel, and 259 = 4·C(8,3) + C(7,3) = 4·56 + 35:
- 4·56 = 224 is the linearized contracted Bianchi identity: four functions at degree 5;
- 35 is one scalar function at degree 4.

The per-order excess C(k+1,3) is the dimension of degree-(k−2) polynomials in four variables:

| order k | excess C(k+1,3) | already identified object |
|---|---|---|
| 2 | 1 | the cone (62.A), i.e. Δq(p) |
| 4 | 10 | the ten quadrics, identified in Step 65 as the degree-2 coefficients of (65.1) |
| 6 | 35 | 35 rows (this step) |
| 8 | 84 | stated excess for order 8 |

**Why the system has one scalar of excess.** The unknowns are six anti-J₀ functions minus one Hamiltonian gauge function, five in all. The equations are ten minus four Bianchi identities, six in all. The system is therefore overdetermined by one scalar.

**Natural identification.** The 35 rows are the degree-4 Taylor coefficients of a single second-order scalar compatibility operator applied to E. At orders 2 and 4 this compatibility is already known to coincide with the torsion-energy identity (65.1).

**Why exactly one row survives.** Real U(2)-invariant polynomials on C² are radial, because U(2) is transitive on S³. In degree 4 only |z|⁴ is invariant. Degree-4 polynomials decompose under SO(4) as 25 + 9 + 1; the "1" is the full trace Δ²(·)(0), equivalently the S³-mean.

This explains why ℓ is the same for every jet. The 34 non-radial components are absorbed linearly by H₆ (rank_JK = 34). The radial component is not absorbed. This is the same mechanism as in Step 62, where the trace-free part of Hess q is matched by free ∇²W⁺ and only the trace is fixed.

**Coordinate-free ansatz.**

> Φ₆ is the critical value, over admissible third torsion jets T₃, of the r⁴-coefficient of the spherical mean of (65.1) about the zero:
> ⨍_{S³}[ (65.1)-residual ]₄ = c₁ ⨍|T₃ − T₃*(θ,λ)|² + Φ₆(θ,λ).

Here T₃ comes from H₄. Its square is the positive 12-dimensional block ℓ·Q(H₄,H₄). This is the next instance of the pattern "square of free data = algebraic expression in lower data", as in |∇²Ω|² = 4trV² − 12|η|².

For Φ₆ < 0 the order-6 solution set in the active H₄ block is an 11-ellipsoid. The square root t = √(−2Φ₆/h_min) in `step80_reconstruct.py` is one point on it.

**Test.**
- Rotate ℓ by random U(2) and SO(4) elements and check cos(ℓ, gℓ) = 1.
- In exact rationals, split off the 224 Bianchi directions.
- Find the scalar second-order operator P with P∘Ric′(h) ≡ 0 on anti-J₀ h, using the span of the U(2)-invariant operators on symmetric tensors: ∂ᵢ∂ⱼEᵢⱼ, Δ tr E, ω^{ik}ω^{jl}∂ᵢ∂ⱼE_{kl}, and their J-twisted versions.
- Compare ℓ with E₆ ↦ Δ²P(E₆)(0). Also compare it with the linearization of the residual of (65.1).

## 3. Rational form and the λ-quadratic law

**Rational form.** The reduction is a constrained quadratic minimization in the free H₄:
- objective: Q(h) + 2b(θ,λ)·h + P(θ,λ);
- constraint: C(θ)h = r(θ,λ), the order-4 rows.

Weights fix where λ enters: b ~ θ² + λ, r ~ θ³ + λθ, P ~ θ⁴ + λθ³ + λ²θ². The critical value is a KKT bordered determinant:

> Φ₆ = N(θ,λ)/D(θ), with D = det[[Q, Cᵀ],[C, 0]] restricted to the active space, and N quadratic in λ.

So the exact λ-quadratic law (cubic coefficient about 1e-11 over λ ∈ [−40, 40]) is what this structure predicts. It requires the form Q and the active subspace to be λ-independent, with λ entering b, r, P affinely. The λ-dependence of the printed Hr eigenvalues must then be a basis artifact. F₀, F₁ and F₂ share the common denominator D.

**Evidence that Φ₆ is not polynomial in θ.** Take the small-c jets. On the unit cone with c = 0, ‖A‖² = ‖S‖² = 1/4 is forced, so every degree-2 invariant is fixed. Yet F₂ ranges over 1.1–3.6 ×10⁻³ there. A weight-4 polynomial invariant would be constant on that slice. Two explanations remain:
- F₂ is rational, i.e. D(θ) varies; or
- Φ₆ depends on hidden H₂ data that the pipeline sets non-equivariantly (see §6).

**A pole near S = 0.** The S ≈ 0 jets (bigc0–2) have F₀ = 4.5–79. At S = 0 the jet has stabilizer containing SU(2), so C(θ) may change rank and D → 0. The SU(2)-nut slice (A01 §5.3) would then be a singular locus of the generic reduction and needs its own reduction. **Test:** follow Φ₆·‖S‖^k along S → 0 at fixed (c, a), and record quad_rank and rank_JK.

## 4. Complex-dilation symmetry: the even-branch formal theory does not see the sign of λ

**Derivation.** The scaling g̃(x) = g(μx) = μ⁻²δ_μ*g has three properties:
- it keeps ω₀ fixed;
- it gives (H_k, λ) → (μᵏH_k, μ²λ);
- it gives E_d → μ^{d+2}E_d.

These are polynomial identities in μ, so they hold for μ = i. On the even branch the image H̃_{2j} = (−1)ʲH_{2j} is real. The Darboux gauge and the anti-J₀ condition are linear in each H_k and are preserved. Hence:

> **Proposition [derivation above].** (H_{2j}, λ) ↦ ((−1)ʲH_{2j}, −λ) is a bijection between real formal even AKE jets with Einstein constant λ and those with −λ. It sends a real-analytic even germ H(x) to H(ix), which is again a real-analytic Riemannian germ. The torsion first jet goes θ → −θ, and det(−Df) = det Df, so index +1 is kept.

This is the compact/noncompact duality of symmetric spaces, here extended to point-symmetric AKE germs. In Darboux coordinates the CP² germ is sent to the CH² germ.

**"Even" in invariant terms.** A germ is even when it is invariant under −I ∈ U(2), the central symmetry. All SU(2)-nut germs are automatically even, since −I ∈ SU(2). So A01's triaxial λ < 0 nut problem is formally and analytically equivalent to the λ > 0 one with flipped jet.

**Consequences.**
1. Φ₆(−θ, −λ) = Φ₆(θ, λ). Hence F₀ and F₂ are even and F₁ is odd under θ → −θ.
2. θ and −θ are not U(2)-equivalent in general. The center acts by c → e^{2iφ}c and (a, S) → e^{4iφ}(a, S), so c → −c forces (a, S) fixed. Since F₁ is odd, it must take both signs on every pair {θ, −θ} unless it vanishes identically. This is the structural reason F₁ changes sign.
3. **The sign of λ enters local formal theory only through odd-order data.** The odd jets H₃, H₅, … become imaginary under μ = i, and terms such as λ·(odd)² flip sign. Any local obstruction specific to λ < 0 cannot come from the even branch. The even-branch constraint {Φ₆ ≤ 0} at λ < 0 is the mirror image under θ → −θ of the constraint at λ > 0.

**Cheap pipeline test.** Rerun the λ-scan with −θ and check that F₁ flips while F₀ and F₂ are unchanged.

## 5. U(2) invariant theory of the first-jet cone

**Weights.** From the A01 dictionary, η ↔ c, V ↔ a, and b = W₃⁺|_C ∈ K_J⁻² (Step 65). So c ∈ K⁻¹, a ∈ K⁻², and S ∈ Sym²C² ⊗ K⁻¹. The action is c → det(U)c, a → det(U)²a, S → det(U)·U S Uᵀ. U(2) = U(1)₊·SU(2)₋, and S is complex spin-1 under SU(2)₋.

**Generators.**
- Real quadratic invariants: |c|², |a|², ‖S‖².
- Complex invariants:
  - w₁ = a c̄², of degree 3; this is the only cubic invariant;
  - w₂ = det S · ā², of degree 4;
  - det S · c̄⁴ = w₂w₁²/|a|⁴;
  - |det S|² (real).

**Dimension count.** The jet space is 10-dimensional, a generic orbit is 4-dimensional, the cone removes 1 and the normalization removes 1. Unit-cone orbits are therefore 4-dimensional, with coordinates

- γ = |c|²/tn² ∈ [0, 1/20],
- ρ = 2|det S|/‖S‖² ∈ [0, 1],
- θ₁ = arg w₁,
- θ₂ = arg w₂,

plus the ratio Λ = λ/tn² = s/|∇²Ω(p)|².

The Step-80 "c²-fraction" is |c|²/(|c|² + ‖S‖² + ‖A‖²), which is at most 1/9.

**Invariant form of the determinant.** det B = det S + a², so

det_R Df = 9|c|⁴ + |det S|² + |a|⁴ + 2 Re w₂ on the cone.

The degenerate stratum is {c = 0, ρ = 1, θ₂ = π}.

Check for gen2, computed from `jet_input`:
- det S = −0.05287 + 0.02381i;
- a² = 0.14862 − 0.06605i;
- w₂ = −0.009431 + 0.00005i;
- 9|c|⁴ + |det S|² + |a|⁴ + 2Re w₂ = 0.005667 + 0.003363 + 0.026452 − 0.018862 = 0.016620, matching detD = 0.016619.

**Invariants of the two unobstructed reconstructed jets.**

| jet | γ | ρ | θ₁ | θ₂ |
|---|---|---|---|---|
| gen2 | 0.0251 | 0.93 | 174.5° | 180.0° |
| gen5 | 0.0279 | 0.75 | 129° | 161° |

Both have det S nearly anti-aligned with a², i.e. lie close to the θ₂ = π direction of the degenerate stratum. Tabulating (γ, ρ, θ₁, θ₂) for all 20 Step-80 jets would show whether sign(F₀) is organized by cos θ₂ and ρ.

**F₁.** Every odd invariant is linear in w₁ times an even invariant (Re/Im of w₁·E). This gives two predictions.

- **Prediction (sharp): F₁ ≡ 0 on {c = 0}.** The small-c rows have F₁ ≈ 0, which confirms this.
- **Leading term.** If F₁ is polynomial, it equals Re(e^{−iθ₀}w₁)·κ. The anti-unitary symmetry (g, ω) ↦ (σ*g, −σ*ω) conjugates the complex invariants, possibly with a sign, and so selects either Re w₁ or Im w₁. A two-point fit to gen2 and gen5 gives κ ≈ 12 and θ₀ ≈ 91°, i.e. F₁ ≈ 12·Im w₁:

| jet | Im w₁ | 12·Im w₁ | observed F₁ |
|---|---|---|---|
| gen2 | 0.000965 | 0.012 | 0.014 |
| gen5 | 0.00881 | 0.106 | 0.108 |

  This is compatible with the S ≈ 0 jets, where |F₁| = 0.14 ≤ 12|w₁| = 0.27. It is a fit, not a test. Whether the symmetry selects Im in A02's convention requires computing the induced action on (c, a, S); the AAD sign conventions are gauge-dependent.
- **If Φ₆ is rational,** F₁ = Im(w₁)·(even weight-0 invariant ratio).

## 6. Hidden data in H₂: W⁻(p)

**Count.**
- H₂ has 6×10 = 60 coefficients.
- Quartic Hamiltonians give 35 gauge directions; their degree-3 vector fields are never Killing.
- E₀ imposes 10 equations.
- This leaves 15 = 10 (torsion jet θ) + 5. The extra 5 are W⁻(p), which is unconstrained by 62.A since W⁺(p) is fixed by θ and λ.

**What the pipeline computed.** `jet_input` lists only (c, S, A). Any U(2)-equivariant choice of the remaining H₂ data, such as minimal norm, gives W⁻(p) = 0. The reason is that no linear equivariant map exists from θ to W⁻ ∈ Sym²₀Λ⁻, which is spin-2 with trivial center while θ has no such component. So Step 80 computes Φ₆(θ, W⁻ = 0, λ).

**Why this matters.** At weight 8 there are invariant couplings such as W⁻(S, S̄), W⁻(S, S)·ā², terms in λ and W⁻, and |W⁻|² terms. These can move the hypersurface {Φ₆ = 0}.

**Test.**
- Add the five W⁻ directions to H₂ and rescan.
- Check U(2) invariance of Φ₆ under rotated inputs. If Φ₆ is not U(2)-invariant, non-equivariant hidden data are present, and this would also account for the F₂ spread on the c = 0 slice.

## 7. Why F₀, F₁, F₂ each take both signs

- **All three.** Φ₆ = P − ½ jᵀH⁻¹j: an indefinite algebraic term minus a Schur-complement term ≥ 0. The universal form ℓ·Q is indefinite on all of H₄ (99/84 split of signs) and definite only on the 12-dimensional active block. Nothing forces the sign of either difference, exactly as with 4trV² − 12|η|² at order 2.
- **F₁.** It is odd under θ → −θ (§4) and proportional to w₁ (§5), so it must change sign.
- **F₂.** It is the λ² coefficient, i.e. the leading term in the near-Kähler regime |Λ| → ∞. Coordinate-free, it is the order-6 condition for an infinitesimal J-anti-invariant Einstein deformation of a local Kähler–Einstein germ, evaluated at a nondegenerate zero of the deformation's torsion. Nothing in that linear problem fixes the sign. The data agree: F₂ > 0 on small-c jets and F₂ < 0 on most generic jets.

## 8. Experiments that recover the formula without assuming a sign

1. **Symmetries (cheap).**
   - U(2) and anti-unitary invariance of Φ₆.
   - Φ₆(−θ, −λ) = Φ₆(θ, λ).
   - F₁|_{c=0} = 0.
   - The CP² ↔ CH² Darboux germs as an exact check of the μ = i map.
2. **Exact cokernel and identification of ℓ (§2),** in rational arithmetic at the flat background.
3. **Exact Schur complement over Q(λ).**
   - Choose rational points on the cone: pick rational c and S, and rational a with |a|² = 4|c|² + ‖S‖²/2, which needs a sum of two rational squares.
   - Obtain N(θ, λ)/D(θ) exactly and confirm degree 2 in λ.
   - Read off the degrees of N and D in θ from exact rational interpolation along stereographically parametrized rational curves on the cone.
4. **Invariant reconstruction.** With D in hand, fit D·F_i by exact linear algebra in the finite basis of U(2)-invariant monomials of the right weight and anti-unitary parity:
   - generators |c|², ‖S‖², Re/Im w₁, Re/Im w₂, |det S|², Re/Im(w₁w̄₂), …;
   - reduce modulo the cone relation;
   - use rational reconstruction for the coefficients.

   This recovers F₀, F₁, F₂ with no positivity input. A sign map over (γ, ρ, θ₁, θ₂, Λ) then follows directly.
5. **Extra jet data.** Rerun with W⁻(p) ≠ 0 and with odd jets H₃ ≠ 0, i.e. ∇Rm(p) data. The odd jets are the only place a λ-sign asymmetry can enter.
6. **SU(2) slice and true germs.** Separate reduction at S = 0. Then compare with A01's triaxial Einstein ODE with Ω = Σxᵢωᵢ at a regular nut: if regular nut solutions exist, they are genuine analytic even germs, and Φ₆ ≤ 0 must hold at their jets.
7. **Order 8 on the ellipsoid.** Minimize Φ₈ over the order-6 ellipsoid together with the new free data. The expected excess is 84 = C(9,3) with one radial survivor. On the even branch it is again λ-symmetric.

## 9. Global control of Λ at zeros in compact Einstein almost-Kähler geometry with λ < 0

**Available inputs.**

- **(a) Pointwise, at a zero.** From 62.A and 62.B(3):
  |∇²Ω(p)|² = 4trV² − 12|η|² ≤ 4(|W⁺|²(p) − s²/24),
  so |Λ| ≥ |s|/(4(|W⁺|²(p) − s²/24)).
- **(b) L² curvature control.** ∫|W⁺|² is fixed by 2χ + 3τ and s²Vol through Gauss–Bonnet and signature. LeBrun's Seiberg–Witten estimates for symplectic Einstein manifolds add L² relations between |W⁺| and s. With noncollapsing, ε-regularity (Anderson, Bando–Kasue–Nakajima, Tian) converts these into pointwise bounds on |W⁺|, except at finitely many concentration points. That gives a lower bound |Λ| ≥ Λ* at most zeros, with Λ* not quantitatively large.
- **(c) A cohomological mean.** With s* − s = ½|∇ω|² and ∫(s + s*)/2 dμ = 4πc₁·[ω]:
  ⟨|∇ω|²⟩ = 16|λ|(1 − κ), where κ = 2πc₁·[ω]/(λ[ω]²) and κ = 1 exactly in the Kähler–Einstein case.
  This controls average torsion energy relative to λ, not the Hessian of q at its minima.

**What is missing.** No known estimate gives a lower bound on tn² at zeros, i.e. an upper bound on |Λ|. Elliptic bounds on ∇ᵏΩ from ∇*∇Ω = 2W⁺Ω − (s/3)Ω point the same way as (a).

**Why Λ control would not suffice for even germs.** The order-6 law is not monotone in Λ:
- gen2 is unobstructed throughout Λ ∈ (−7×10², 12);
- the λ-scan jets are unobstructed for Λ ≲ −30.

Every tested Λ-window with λ < 0 contains unobstructed even jets.

**What a global use would require.**
- Odd-order data at the zeros, where λ-sign information lives (§4), together with W⁻(p) dependence (§6).
- A mechanism linking the local constraint to global counts: 5χ + 6τ zeros of index +1, Poincaré–Hopf for q, or the weighted-charge identity of A01 §5.4. These need a signed weight built from the order-6 data.

The even, W⁻ = 0 law Φ₆ ≤ 0 alone cannot supply that link.
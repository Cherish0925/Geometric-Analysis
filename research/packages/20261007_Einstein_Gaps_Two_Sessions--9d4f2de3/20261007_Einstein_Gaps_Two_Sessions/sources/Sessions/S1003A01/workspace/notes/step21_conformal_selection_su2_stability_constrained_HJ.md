# Step 21 — Conformal selection identity, SU(2) symmetry-breaking stability, and the scalar-constrained HJ problem

Normalization: Ric_CH = −6g, s_CH = −24, e = s+24, Δ = div grad (nonpositive), costs in units of 8π² unless stated.
All curvature integrals in four dimensions.

## 1. An exact conformal identity and the conformal-selection theorem

**Pointwise scalar identity (any u>0, no equation).** For ĝ = u²g in dimension four,
ŝ = u^{-3}(−6Δu + s u) and dV̂ = u⁴dV, hence

  ŝ² dV̂ = (s − 6Δu/u)² dV.                                            (1.1)

Combining (1.1) with pointwise conformal invariance of |W|²dV and the Gauss–Bonnet formula
P = ½∫|W|² + (1/12)∫s² − 16π²χ (closed case; on a cell the Pfaffian changes by an exact
transgression), one gets for any positive u

  P(ĝ) − P(g) = ∫[ −sΔu/u + 3(Δu/u)² ] dV_g  (+ boundary/transgression terms).          (1.2)

**Theorem 1 (exact Yamabe gap).** Let ĝ = u²g have constant scalar curvature −κ, κ>0, i.e.
s = −κu² + 6Δu/u. If boundary terms vanish (closed M, or the decay below), then

  P(g) − P(ĝ) = κ∫|∇u|²_g dV_g + 3∫(Δu/u)² dV_g ≥ 0,                                  (1.3)

and for κ = 24, with J₆ = P + ¼∫e²,

  J₆(g) − J₆(ĝ) = ∫[ 3(Δu/u)² + 24|∇u|² + e²/4 ] dV_g,   J₆(ĝ) = P(ĝ).                 (1.4)

Equivalently 3(Δu/u)² = (e + 24(u²−1))²/12. Equality holds iff u ≡ 1. Proof: insert
s = −κu² + 6Δu/u into (1.2) and integrate −κ∫uΔu = κ∫|∇u|². ∎

Consequences.
* On a closed manifold with negative Yamabe class this is an exact form of the inherited fact
  δ = S(g) − S(ĝ) ≥ 0 (conventions file, line 57; source
  `Skills/geometric-analysis/research/sources/continuation/20260927_conformal_separation_and_zero_end.md` §3):
  in the inherited s=−4 normalization δ = 48∫|∇u|² + 36∫(Δu/u)². Inherited (3.10) gives
  δ/R ≤ 3(E−α)/(1−α) for every E-minimizing sequence; with (1.3) this now forces
  ∫|∇u|²/R → 0 and ∫(Δu/u)²/R → 0 for the conformal factors to the Yamabe metrics, a quantitative
  conformal-factor control that the inherited text records as not supplied (it still gives no
  geometric compactness).
* The constant-scalar representative is the **unique minimizer of both J₆ and P in its conformal
  class** (apply (1.3)/(1.4) to any g in the class with u the factor to ĝ).

**Theorem 2 (cell version).** Let g be a complete metric on a cell, equal to (or exponentially
asymptotic to) CH outside a compact set K, with s<0 everywhere. Then there is a positive solution
of −6Δu + su + 24u³ = 0 with u → 1, and u − 1 = O(e^{−(2+2√3)r}) with derivatives; (1.4) holds.
Sketch: s ≤ −c < 0 globally (s = −24 off K), so u₋ = (c/24)^{1/2} ≤ 1 and u₊ = (max(−s)/24)^{1/2} ≥ 1 are
constant sub/supersolutions; Dirichlet problems on exhausting balls with u = 1 give a locally
convergent sequence. Off K, v = u−1 solves −6Δv + 24u(u+1)v = 0 with positive potential; barriers give
exponential decay, and once v → 0 the potential tends to 48, giving the rate m with m²+4m−8=0,
m = 2+2√3 > 2 (CH volume growth e^{4r}). The Pfaffian transgression and ∮u∂_νu on S_r are
O(e^{(4−2m)r}) → 0. Truncating ĝ back to an exact CH collar at radius R costs O(e^{(4−2m)R}) → 0 because
J₆ is quadratic at the Einstein background. Hence

  inf_{s<0 cells} J₆ = inf{ P(ĝ) : ĝ complete, CH-asymptotic with the above decay, s_ĝ ≡ −24 }.

The radial factor preserves diagonal (and SU(2)-invariant) Bianchi IX metrics, so the same holds
inside those ansätze. For small e the solution also follows from the implicit function theorem
(linearization −6Δ+48 is invertible). Cells with s ≥ 0 somewhere are not covered; note
6λ₀(CH²) + s_CH = 6·4 − 24 = 0, so the conformal Laplacian of CH sits exactly at the bottom of its
spectrum, and existence with u → 1 needs an argument there. (This is the infinite-ended version of
the Strategist's flow identity dJ₆/dτ = −4∫(|∇s|²+6e²).)

**Numerical check of (1.4)** — `workspace/scripts/yamabe_cell_check.py`, data `workspace/data/yamabe/`.
The radial BVP is solved by Newton on a log-x finite-volume grid out to 10⁴X with zero flux at the bolt;
J₆(ĝ) is computed *directly* from Ric_ĝ = Ric − 2(Hess f − df²) − (Δf + 2|df|²)g, f = log u
(second derivative of f from the equation), so agreement tests the integrated identity.

| cell | grid N | J₆(g)−J₆(ĝ) direct | RHS of (1.4) | P(g)−P(ĝ) direct | 3∫(Δu/u)²+24∫|∇u|² |
|---|---|---|---|---|---|
| x₀=.038, X=128 | 3·10⁴ | 4.5837e−7 | 4.5839e−7 | 1.1252e−7 | 1.1255e−7 |
| x₀=.038, X=128 | 1.5·10⁵ | 4.5844e−7 | 4.5843e−7 | 1.1260e−7 | 1.1258e−7 |
| x₀=.038, X=512 | 1.5·10⁵ | 4.430e−8 | 4.444e−8 | 1.081e−8 | 1.095e−8 |

u ∈ [0.999972, 1.0000001] (X=128), u(X) − 1 ≈ 10⁻⁹. The Yamabe metrics give complete s ≡ −24 metrics with
J₆ = P ≈ 0.9952872585 (X=128) and ≈ 0.9951781423 (X=512) (stored J minus the gain). The gain is
≈ 1.33 × the scalar energy, the upper end of the linear prediction ratio ∈ (1, 4/3), confirming that the
residual scalar defect of the spectral cells is high-frequency (also seen in Step 20's Le_sup ≫ e_sup).
These are tiny upper-bound improvements; the value of Theorem 2 is structural: the scalar channel is
removed from the infinite-ended cell problem for all competitors with s<0, not just diagonal ones.

## 2. Non-diagonal SU(2)-invariant second variation: the diagonal optimum is stable

`workspace/scripts/su2_offdiag_hessian.py`, `su2_offdiag_spectrum.py`; data `workspace/data/su2_offdiag/`.
General SU(2)-invariant metrics dx²/(4G) + h_ij(x)σ_iσ_j; full coordinate curvature by autodiff (peer
`curvature_scalars`, Euler-angle coordinates), valid for non-diagonal h. Perturbations of the converged
x₀=.038 cells:
* k_ij = N_ij u²(1−u)³ Σ c_m T_m(2u−1), N₁₂ = x, N₁₃ = N₂₃ = x√(1+x). u² ∝ r⁴ at the bolt is exactly the
  order required for smoothness of the σ₁σ_{2,3} cross terms (circle weight 2) and of the σ₂σ₃
  anisotropy (weight 4); (1−u)³ gives C² contact with the collar.
* bolt rotations (the remaining smooth directions): exact rotation by ψχ(u), χ = (1−u)³(1+3u+6u²) = 1+O(u³),
  implemented as the isometric rotation by ψ(χ−1) (a global rotation is right translation), which avoids
  float cancellation at the collapsed fibre. A first attempt with the *linearized* rotation [Ψ,h] gave
  −1.4×10⁷: that path makes h indefinite at the bolt (11-entry 0, off-diagonal x₀ψ) and is inadmissible; it is
  superseded.

Results (J₆ Hessian; consistent J₀ = 0.99528772 (X=128), 0.99517819 (X=512); gradient ≤ 2×10⁻¹¹; off-block
entries ≤ 10⁻¹³, confirming that the three sign-flip characters of Z₂×Z₂ ⊂ Aut(su(2)) decouple the channels and
kill the first variation):
* Generalized eigenvalue in the norm ∫(k_ij/N_ij)²du, X=512: μ_min(h₁₂,h₁₃,h₂₃) =
  83.5/262.7/476.8 (n=6), 80.37/261.4/462.4 (10), 80.15/260.9/462.3 (14), 80.134/260.68/462.25 (20),
  80.129/260.65/462.25 (26); identical at nq=2000. Converged and strictly positive. X=128: 68.9/222.7/394.6.
* Bolt rotation toward the CH fibre slot (h₁₃): Schur complement 0.6053 (X=512; n=10,16,24, nq=1200/2400 stable),
  0.6046 (X=128) — a genuine positive twist stiffness.
* Bolt rotation in the (1,2) plane: Schur 3.2e−5 → 2.0e−6 → 1.1e−6 (n=10,16,24) → 0, the exact U(1) zero mode
  (constant rotation in a plane where the collar has a₁ = a₂; this is the phase θ of the Step-13 pair interaction).

So, within SU(2)-invariant metrics, the diagonal perpendicular optimum is a strict local minimum modulo the U(1)
symmetry. Breaking diagonality without breaking SU(2) does not lower the cell cost at second order. Any
symmetry-breaking improvement must use non-SU(2)-invariant (e.g. U(1)×U(1) or no symmetry) perturbations; the
natural next object is the Peter–Weyl decomposition of the J₆ Hessian into SU(2)-isotypic ODE systems (with the
diffeomorphism gauge quotiented), starting with the lowest nontrivial isotypes.

## 3. The scalar-constrained Hamilton–Jacobi problem

By Theorem 2 the diagonal lower problem may be posed on s ≡ −24, where J₆ = P. In the Step-17 control
formulation s = Λ − 2Σz with Λ = −8Σa_iH_i/W (`hj_structure.py`, H3), so admissible controls satisfy the
state-dependent affine constraint Σz_i = c(a,u) := (Λ+24)/2. Square completion on that plane gives

  W|z|²/4 − dS/dt ≥ (W/12)(c − Σζ_i)² − H_S,   ζ_i = 2a_iS_{u_i}/W,

so the subsolution requirement weakens from H_S ≤ 0 to H_S ≤ σ_S := (W/12)(c − Σζ)². For the seed S = −kΦ along the
X=128 witness (`hj_scalar_constraint.py`, `data/hj/scalar_constraint_seed_X128.json`): the negative part of the
pointwise margin shrinks from −4.75e−2 to −4.74e−2 (k=1), −2.58e−3 → −1.83e−3 (k=.5), −2.2e−4 → −1.0e−6 (k=.1), but it
never disappears, and small k gives only a small bound. Since σ_S vanishes on the hypersurface c = Σζ, a seed failing on
an open state set still fails there; the constraint helps only after S is redesigned (e.g. with Λ-dependence that keeps
c − Σζ away from zero on the failure band). Thus the constrained HJ problem is the correct, strictly weaker target, but
no certificate follows yet. dΛ/dt is linear in z (printed by `hj_structure.py`), so Λ can also be used as an extra state
coordinate.

## 4. What changed

* The infinite-ended cell problem with s<0 is now exactly a P-minimization over complete s ≡ −24 CH-asymptotic metrics,
  for all metrics, with an exact formula for what Yamabe normalization saves.
* Within SU(2)-invariant metrics the diagonal branch is locally optimal (strict modulo U(1)); further constructive
  progress on 𝔍₁,₀ must break SU(2).
* The diagonal HJ certificate should be sought in the scalar-constrained form.

Open: non-SU(2) second variation (isotypic decomposition), existence for cells with s ≥ 0 somewhere (CH conformal
Laplacian is critical), the finite-interface nonlinear terminal response, the unrestricted 𝔍₁,₀, mixed cells, global
branches. The managed Arb tasks s19_t25_tool1 and s19_t32_tool1 were still running at this note's writing.

# Step 68: the flat scalar compatibility of the Darboux AKE system, the exact radial multiplier, and the order-eight linear structure

Agent2, Execute. Inputs: Step 67 (finite-order survival of nondegenerate zeros through E6; candidate multiplier with cosine 0.97730), and A02's Step-80 arrays and Step-81 E8 programme. The conventions are A02's: Darboux gauge with fixed standard ω, g = exp(H), H anti-J symmetric, E = Ric(g) − λg. E_d means the degree-d Taylor coefficient. L_d : H_{d+2} → E_d is the flat anti-J linearized Ricci operator.

## 1. Theorem 68.1: one scalar flat compatibility operator

Let
\[
P(E)=J_{ia}J_{jb}\,\partial_a\partial_bE_{ij}-\tfrac12\Delta\operatorname{tr}E .
\]
For every anti-J symmetric h,
\[
P(\delta\mathrm{Ric}(h))\equiv0 .
\]
**Proof.** Since hJ = −Jh we have tr h = 0 and J^T h J = −h. Then
\[
2\,\delta\mathrm{Ric}_{ij}=\partial_k\partial_ih_{kj}+\partial_k\partial_jh_{ki}-\Delta h_{ij},\qquad \operatorname{tr}\delta\mathrm{Ric}=\partial_k\partial_ih_{ki}.
\]
In $J_{ia}J_{jb}\partial_a\partial_b(\cdot)$, the first two terms vanish because the antisymmetric J is contracted against symmetric pairs of derivatives. The third term gives $+\Delta\,\partial_a\partial_bh_{ab}$, and this cancels $-\tfrac12\Delta(2\,\partial\partial h)$. ∎

Modulo the contracted Bianchi rows $B(E)_j=\partial_iE_{ij}-\tfrac12\partial_j\operatorname{tr}E$, the operator satisfies $P\equiv-2\,\operatorname{div}\operatorname{div}E^{\text{anti-}J}$. The flat compatibility beyond Bianchi is therefore divdiv of the J-anti-invariant Einstein tensor.

**Completeness, exact over ℤ for 0 ≤ d ≤ 8** (`scripts/step68_flat_cokernel.py`, `step68_cokernel_tower.py`, `step68_scalar_compatibility.py`; data `data/step68/cokernel_tower.json`, `scalar_compatibility.json`):

| d | rank L_d | coker | Bianchi rank | coker/Bianchi | P-rows independent mod Bianchi | U(2)-invariant classes |
|---|---|---|---|---|---|---|
| 2 | 83 | 17 | 16 | 1 | 1 | 1 |
| 3 | 156 | 44 | 40 | 4 | 4 | 0 |
| 4 | 260 | 90 | 80 | 10 | 10 | 1 |
| 5 | 400 | 160 | 140 | 20 | 20 | 0 |
| 6 | 581 | 259 | 224 | 35 | 35 | 1 |
| 7 | 808 | 392 | 336 | 56 | 56 | 0 |
| 8 | 1086 | 564 | 480 | 84 | 84 | 1 |

Thus coker L_d = (Bianchi rows) ⊕ (the C(d+1,3) coefficients of the scalar P(E_d)), in agreement with A02's flat ranks. For all d this follows at the symbol level: σ_L(ξ) has rank 5 (6 anti-J components minus the Hamiltonian gauge line), so its left annihilator has dimension 5, made up of the 4 Bianchi covectors and P_ξ. The AKE system in Darboux gauge is overdetermined by exactly one scalar equation. On any actual AKE metric, P_g(E_g) = Γ(g), where Γ starts at quadratic order. The excess conditions at E_d are exactly the degree-(d−2) Taylor coefficients of this single scalar equation. At d = 2 its value is the order-two cone of Step 62, i.e. the zero value of the Δq identity.

## 2. Theorem 68.2: the surviving multiplier is the radial moment

Under U(2) = SU(2)_L × U(1)_R ⊂ SO(4), the harmonic summand $\mathcal H_j\cong(j/2,j/2)$ contains an invariant only when j = 0. Hence degree-m scalar polynomials carry exactly one invariant functional when m is even, namely $\Delta^{m/2}$ at 0 (equivalently the spherical mean), and none when m is odd. This explains the last column of the table. The unique invariant class at even d is
\[
\ell_d(E)=\Delta^{(d-2)/2}P(E_d)(0).
\]
**Exact check:** $(\ell_6^{(1)}-\tfrac12\ell_6^{(2)})L_6=0$ holds exactly over ℚ (`step68_multiplier_rational.py`). Its class modulo Bianchi agrees with A02's universal 840-vector ℓ to cosine 1.0000000000000002. In A02's normalization, ℓ = 5.80303455×10⁻⁴ × (class of $\Delta^2P$). The Step-67 cosine 0.97637 was exactly the Bianchi component of the integer representative (class-norm ratio 0.9763718741653). Nothing was missing from the candidate.

**Consequences.**
- (i) A02's universality of ℓ follows from representation theory: one surviving row with a jet-independent multiplier must be the unique U(2)-invariant class.
- (ii) At odd orders, no universal surviving scalar is possible.
- (iii) At every even order at most one universal sign condition can survive. It is the radial (spherical-mean) Taylor coefficient of the scalar compatibility Γ = 0. The exact E8 multiplier is $\ell_8=\Delta^3P(E_8)(0)$, saved in A02 layout (component-major over i ≤ j, TRing monomial order) as `data/step68/ell_tower.npz`, key `ell8` (integer representative) and `ell8_class` (Bianchi-orthogonal representative).

Hence Φ6 = F0 + F1λ + F2λ² is the minimum, over the free lower data, of the radial fourth moment $\Delta^2\Gamma(0)$ of one natural scalar invariant. Its sign-indefiniteness is a property of that natural invariant.

## 3. The top-kernel channel never reaches the radial row once torsion is present

Let k ∈ ker L_{d−2} ⊂ H_d. Such k leaves E_0, …, E_{d−1} unchanged and enters E_d exactly through D_d(k) = B(H2,k) − λk. Let M_d = P∘D_d restricted to ker L_{d−2} (`step68_kernel_absorption.py`, `step68_kernel_absorption_cases.py`; data `data/step68/kernel_absorption_d46.json`, `kernel_absorption.json`, `data/step68b/kernel_absorption_cases.json`).

| H2 | d=4 | d=6 | d=8 | radial row in left null space? |
|---|---|---|---|---|
| A02 cone jets gen5 (λ=−5), gen2 (λ=0), lsA (λ=−1) | 10/10 | 20/35 | 28/84 | yes at d=6,8 (rel. 10⁻¹⁵) |
| E0-solution off the cone, λ=−1 and 0, torsion norms 1.4 and 0.07 | – | 20/35 | 28/84 | yes |
| Kähler E0-solution (torsion-free) | – | 0 (numerical zero) | 0 (numerical zero) | — |
| random H2 violating E0 | 10/10 | 35/35 | 84/84 | no |

**Correction (Steps 69–70).** The Kähler row originally read 35/35 and 84/84. Those matrices have largest singular values 2.1×10⁻¹² to 9.8×10⁻¹² (`data/step68b/kernel_absorption_cases.json`); the rank had been measured relative to the matrix's own largest singular value, so numerical zero was reported as full rank. The Kähler channel is zero, as predicted by the torsion polarization (Step 70, Theorem 70.3: the channel is bilinear in the first torsion jet). The random-H2 row is a genuine full rank (smallest retained singular values ≈18), but those H2 violate E0 and are not jets of AKE germs.

The rank deficiency, and in particular the inaccessibility of the radial row through the newest freedom, holds for every torsion-carrying E0 solution, at every tested λ and torsion size. Step 70 proves the all-degree mechanism: the newest jet reaches exactly the real parts of complex bidegrees (0,n) and (1,n−1), of rank 4(n+1) for n ≥ 3 at nondegenerate cone jets, with zero radial moment for even n ≥ 4 (`notes/step70_flat_exactness_and_top_channel_theorem.md`). Consequently a radial condition at order 2k ≥ 6 can be met only through lower-order freedom. At E6 that lower freedom enters through the positive-definite 12-dimensional H4·H4 block, which produces A02's sign condition Φ6 ≤ 0.

## 4. Order eight at the gen5 (λ=−5) reconstruction: linear structure

Data `data/step68/order8_absorption_recon_F012_gen5_lam-5.json` (`step68_order8_absorption.py`). Variables are (H4,H6,H8), with H2 fixed and the even germ. The constraint map (E2,E4,E6) has rank 969 at the base, with a clean singular-value gap 6.3×10⁻² versus 3.5×10⁻¹⁰. This gives tangent dimension 735, matching A02's 361 + 409 − 35.

Restricted to this tangent space, the 84 order-8 rows P(E8) have **rank 84**, smallest singular value 4.75. The radial row has nonzero linear dependence (|w^T G| ≈ 1.1×10³ against an estimated numerical error of order 10⁻¹). So at this E6 solution, order eight is a submersion on the order-≤6 solution variety: no rank-type obstruction is present, and the radial E8 row is reached by lower (H4,H6,H8-particular) directions.

This does not establish a root. The base value of P(E8) is large (‖·‖ = 4.1×10⁷ unnormalized, radial component −36.7). Whether 0 lies in the image is a global question about a quadratic map, of the same kind as Φ6 at E6. A naive Gauss–Newton run in raw scaled variables reduced ‖P E8‖ from 4.1×10⁷ to 1.6×10⁷ in 12 steps but left the order-6 variety, so it is not evidence either way. A homotopy continuation (R = (1−t)R(v*), corrector on the full system, σ_min of the restricted Jacobian tracked) is `step68_order8_homotopy.py`; results in §6 once available.

## 5. Meaning for the Goldberg problem

The local germ problem at a nondegenerate zero is now organized as one scalar compatibility equation Γ = 0 of an overdetermined-by-one system, with one possible real (radial-moment) condition per even order. At E6 that condition is the sign of Φ6, which changes sign on the cone. At E8 the linear structure at an actual E6 solution is surjective. The nondegenerate +1 zeros therefore remain locally admissible through E6, and E8 is undecided but not linearly obstructed. A universal finite-order exclusion would require some even order at which the lower-order quadratic block feeding the radial row is definite on the whole solution family. Nothing in the computed structure suggests this. The closed problem continues to require global input coupling the zero charge 5χ+6τ (index +1 at nondegenerate zeros) to compact geometry.

## 6. Order-eight continuation result

Background task s68_t20_tool2 completed all 40 homotopy steps (`data/step68/order8_homotopy_recon_F012_gen5_lam-5.json`, stdout in `workspace/tasks/s68_t20_tool2/stdout.log`). The order-≤6 constraint rank stayed 969 throughout; the restricted Jacobian had σ_min in [0.019, 0.038] (no fold); the tracking error C was ≈2×10⁻⁹ except at t = 0.175, 0.2, 0.25, 0.975 (≈2×10⁻⁵, each recovered at the next step). Final unreduced residuals of the assembled jet (H10 = −L8⁺E8): E0 2.7×10⁻¹⁵, E2 4.2×10⁻¹², E4 2.6×10⁻¹⁰, E6 3.0×10⁻⁶, E8 8.0×10⁻⁶, odd orders zero by parity. Coefficient norms H2 3.23, H4 1.64×10³, H6 1.50×10⁴, H8 6.54×10⁵, H10 8.57×10⁶.

Step 69 polished this endpoint by rank-revealing Newton (`scripts/step69_polish_order8.py`, `data/step69/order8_polished_recon_F012_gen5_lam-5.json`): reduced residual 2.44×10⁻⁸ (a float64 floor; scaled Jacobian singular values 2.74×10⁻⁴ to 2.32×10⁶, rank 1053), unreduced E2 3.55×10⁻¹², E4 2.62×10⁻¹⁰, E6 4.48×10⁻⁹, E8 9.79×10⁻⁷. This is floating finite-jet evidence for a negative-Einstein AKE jet with a nondegenerate index-+1 torsion zero through Ricci degree 8, not a certified jet, formal germ or analytic germ.

# Step 45 — O10 concentration cells: tiling law, tidal radius, Killing-moment separation, and the charge that a collapsed nut phase must discharge

Session S1003A01, Agent2, Execute. Scripts and data:

- `workspace/scripts/step45_tnads_cartan.py` → `workspace/data/step45/tnads_cartan.json` (exact Cartan curvature of Taub–NUT and Taub–NUT–AdS, flux-balance radius table);
- `workspace/scripts/step45_killing_moment_check.py` → `workspace/data/step45/killing_moment_check.json` (Killing-moment identity on the exact Einstein cell).
- `workspace/scripts/step45_tnads_field_extension.py` is a withdrawn draft stub (never executed; contains no result).

Conventions. O10 normalization of the manuscript: Ric≈−g, s=−4, W⁺→0 in normalized L², ρ=|Φ|²→4/3, the resolvent section v of E₋=S⁻⊗L with (L−2)v=q→0 in normalized L², m=|v|²→m_*=128/81, and the exact closed-manifold identity ∫|∇v|²=2∫m+Re∫⟨q,v⟩ (integrate Δm=2|∇v|²−4m−2Re⟨q,v⟩, div-grad Laplacian). Taub–NUT (TN): H=1+ℓ/R, metric H dR²+HR²(σ₁²+σ₂²)+ℓ²H⁻¹σ₃², Euler angle ψ of period 4π (so the fibre has length 4πℓ at infinity), dσᵢ=−σⱼ∧σₖ. The 4-volume density is 16π²ℓ R(R+ℓ) dR after angular integration. A02's one-centre field v=√(m_*/2) d f̄ has m=m_*R/(R+ℓ), E(R)=∫_{B_R}|∇v|²=8π²m_*ℓ²(R/(R+ℓ))², flux Φ(R)=2E(R), mass M(R)=(16π²/3)m_*ℓR³.

## 1. Exact Einstein cell in the field normalization

With F=1+R(R+2ℓ)/3, the metric

  g_TNAdS = (H/F) dR² + HR²(σ₁²+σ₂²) + ℓ²(F/H) σ₃²

has, by direct Cartan computation in the frame e⁰=√(H/F)dR, e¹,²=R√H σ₁,₂, e³=ℓ√(F/H)σ₃:

- Ric = −g exactly (all four diagonal entries −1, off-diagonal 0). This confirms the Strategist's rescaling: F=1+R(R+2ℓ)/3 is the Ric=−g member, so the field eigenvalue 2 in (L−2)v and the metric are in the same scale.
- W⁺=0 exactly in the orientation e⁰¹²³, which is the orientation in which TN is hyperkähler with W⁺=0. With u=R(R+2ℓ), the radical in the symbolic W⁺ is √((u+3)⁴) and the outer polynomial is (u+3)², so W⁺ vanishes identically; the tiny numerical values in the JSON, up to ~10⁻¹⁷, are cancellation error. Thus TNAdS is the exact W⁺=0, Ric=−g continuation of the O10 tangent with the correct chirality.
- Volume density A B² C = Rℓ(R+ℓ), identical to TN. The radial Laplacian weight changes from B²C/A=ℓR² (TN) to ℓR²F (TNAdS).
- TN: W⁻ eigenvalues ℓ(R+ℓ)⁻³(−1,−1,2), |W⁻|²=6ℓ²/(R+ℓ)⁶ (sum of squares of the 3×3 operator on unit forms). TNAdS: W⁻ eigenvalues ℓ(1−ℓ²/3)(R+ℓ)⁻³(−1,−1,2), so |W⁻_TNAdS|²/|W⁻_TN|²=(1−ℓ²/3)² exactly, independent of R (the simplification is from the TTCS reading; it matches the numerical table).

Hence on the normalization region the Einstein continuation changes the Ricci part of the curvature by O(1) (from 0 to −g) while leaving W⁻ essentially that of TN, and the metric itself only by F−1≈R²/3=O(ℓ^{2/3}) in C⁰.

## 2. The normalization cell is a Wigner–Seitz cell and its boundary is the tidal radius

**2.1 Tiling identity.** Let Ω be a region with quantitative hypotheses ∮_{∂Ω}∂_νm=o(ℓ²), ∫_Ω Re⟨q,v⟩=o(ℓ²) and ∫_Ω|m−m_*|=o(ℓ²). Convergence in measure alone is not enough, and global normalized estimates give these only for selected good cells. Integrating the mass equation gives

  |Ω| = E_Ω /(2m_*) + o(ℓ²).

For a single core whose excess gradient energy is the TN value 8π²m_*ℓ², the completed region has volume 4π²ℓ²+o(ℓ²) — the Strategist's number — independently of the ALF volume law. The cubic R(R+ℓ)²=3ℓ/4 is the exact finite-radius TN mass/flux balance 2E(R)=4M(R). It is not the exact volume-4π²ℓ² radius, which solves 4R³+6ℓR²=3ℓ; the two agree to relative O(ℓ^{2/3}). Numerically (`tnads_cartan.json`) R_*/ℓ^{1/3}=0.8779, 0.9019, 0.9071, 0.9083, 0.9085 for ℓ=10⁻²,…,10⁻⁶, converging to (3/4)^{1/3}=0.90856.

More generally, the closed-manifold identity is an exact energy/depletion ledger. If a flux-free region Ω contains a core B, then ∫_{Ω∖B}(2m−|∇v|²)=E_B−2∫_B m+o(ℓ²). Every core therefore needs a compensating depletion region. This does **not** exclude geometrically isolated cores with depletion shells. Pointwise |∇v|²≈2m outside cells would require control of Δm, which (L−2)v→0 in L² and m→m_* in measure do not supply in the unbounded-density regime. If a fraction θ of the energy is carried by TN-type cores whose completions are good cells, those cells occupy volume θV+o(V).

**2.2 Wigner–Seitz interpretation.** In Gibbons–Hawking form g=Vγ+V⁻¹(dψ+ω)² with ψ of period 4πℓ, the 4-volume element is V·(4πℓ)·vol_γ. If cells of volume 4π²ℓ²/θ tile, the base density of nuts is n₃=θV̄/(πℓ), and the base volume per nut is the γ-ball of radius r with r³=3ℓ/(4θV̄). At θ=V̄=1 this is the Strategist's R_*: the balance radius is the Wigner–Seitz radius of a nut lattice, not the radius of an isolated insertion. Neighbouring cells share boundaries, which is the precise form of the Strategist's remark that retained outer fluxes must be coupled.

**2.3 Tidal coincidence.** On the balance radius the TN tidal curvature is not small:

  ℓ/R_*³ → 4/3,  |W⁻_TN|²(R_*) → 6·(4/3)² = 32/3,

(table: ℓ/R_*³=1.478, 1.363, 1.340, 1.335, 1.334; |W⁻|²=9.62, 10.43, 10.62, 10.66, 10.66). Exactly, ℓ/R_*³=(4/3)(1+ℓ/R_*)² and |W⁻|²(R_*)=(32/3)(R_*/(R_*+ℓ))². This is a consequence of R_*³≍ℓ rather than an independent coincidence, but it locates the cell boundary exactly where the nut's own Weyl field falls to the ambient Einstein curvature scale. In cell units X=R/R_* the cell is a TN with charge and circle both of relative size ε=ℓ/R_*≍ℓ^{2/3}, and the Einstein and eigenvalue terms (R_*²·O(1)) are also O(ε). The Strategist's moving-domain expansion therefore becomes a fixed-domain cell problem with a single small parameter ε: the first torsion-parent correction is O(ε^{1/2}) (the physical O(1) gradient of Φ over a distance R_*) and the quadratic corrections are O(ε), comparable to the Einstein deformation. This is consistent with, and makes explicit, the scale counting in the Strategist note.

## 3. Leading-order radial solvability is the flux balance

At order ε in cell units, the correction w of the transported field must solve L_h w = 2v₀ + (Einstein correction of L)·v₀ + (torsion/determinant forcing). On the TN core, v₀ itself and the orthogonal bounded section v₀^⊥ (the second generator of Λ^{0,1}_{I₃}, pointwise orthogonal to v₀) are bounded L_h-harmonic sections. Pairing the equation with v₀ over the cell and integrating by parts reproduces exactly the integrated mass equation, so the v₀-solvability condition is 4M_cell=2E_cell plus boundary flux: it is satisfied by choosing the Wigner–Seitz cell volume. The v₀^⊥-pairing of the eigenvalue source 2v₀ vanishes pointwise. The justified statement is limited. Once a self-adjoint cell problem with fixed boundary conditions is chosen, the pure eigenvalue source 2v₀ has one scalar solvability condition, equivalent to the mass/flux balance, and no direct v₀^⊥-projection. The complete order-ε solvability conditions have not been computed. They involve the lattice-cell boundary conditions and cokernel, moving-interface terms, (δL)v₀, the torsion-parent and determinant forcing, and the cellwise size of q. These may also produce obstructions in the scalar sector, and a periodic lattice cell need not keep the round-cell symmetry. What the computation does show is why another radial positivity sum built only from the scalar mass equation cannot decide O10. The terms not yet included are: the torsion relation v=t(Φ) at second order, the determinant curvature F_A⁺=2iσ(Φ), and the quadratic monopole source, which (as the Strategist observed) generates l=2 angular components — σ(Φ₀+χ) contains |f|²=R²(1−n₃²) — so the minimal closed sector is T²-equivariant (ψ-translations and x₃-rotations twisted by gauge), of cohomogeneity two in (R,n₃), not an SU(2)-radial ODE. This formal statement has not been carried through the coupled torsion/determinant equations in this Step.

## 4. Killing-moment separation of fixed-point types (exact Einstein, W⁺=0)

**Proposition 4.1 (sign corrected after independent reading).** Let (M,g) be Einstein with W⁺=0 and scalar curvature s, and K a Killing field. With the sphere-positive curvature-operator convention,

  ∇_X (dK♭)⁺ = −(s/6) (X♭∧K♭)⁺.

*Proof.* ∇_X∇K=R(X,K) as a skew endomorphism. Converting to dK♭=2(∇K)♭ gives ∇_X dK♭=−2ℛ(X♭∧K♭). In dimension four ℛ has diagonal blocks W^±+(s/12)I and off-diagonal block Λ⁻→Λ⁺ given by Ric°. With W⁺=0 and Ric°=0, the projection to Λ⁺ is −2(s/12)(X∧K)⁺. ∎

In general, ∇_X(dK)⁺=−2(W⁺+s/12)(X∧K)⁺−2B(X∧K)⁻ with B the Ric°-block. This is the error form needed for approximate metrics. Checked on TNAdS with K=2∂_ψ (the weight-one Hopf generator): (dK)⁺ has norm (2√2/3)ℓR, increasing radially with coefficient −s/6=+2/3. Its proper radial derivative equals (|s|/6)|(e⁰∧K)⁺| identically (`killing_moment_check.json`, residual 0; the script checks magnitudes and was blind to the sign, which the TNAdS growth fixes). On TN, (dK)⁺≡0. The structure is the four-dimensional form of the quaternionic-Kähler Killing moment map; a normalized literature citation has not been retrieved.

**Corollary 4.2.** For a semi-free circle action generated by K (unit weights), |(dK)⁺|=0 at a nut of the W⁺-compatible (triholomorphic) type, =√2 at every bolt point, and =2√2 at an anti-nut. Hence along any curve γ from a nut to a bolt point, ∫_γ|K| ≥ 12/|s|; to an anti-nut, ∫_γ|K| ≥ 24/|s|. With s=−4 the thresholds are 3 and 6.

In a collapsed region where the circle has length ≈4πℓ, |K|≈2ℓ, so no bolt or anti-nut can occur within distance ≈3/(2ℓ)≫1 of a nut. On TNAdS, A|K|=2ℓ, so ∫₀^{3/(2ℓ)}|K|ds=3 exactly: the moment value √2 of a unit-weight bolt is reached at R=3/(2ℓ), where the orbit size is of unit order (|K|=2ℓ√(F/H)≈2ℓR/√3). No actual bolt is present there; (dK)⁺ is nonzero for every R>0. The bound is sharp in this moment-value sense.

Bochner gives a related exact fact: on a Ric=−g region, ½Δ|K|²=|∇K|²+|K|² (div-grad), so an exact collapsed orbit length cannot stay nearly constant over long curvature-scale distances. Also, a closed negative Einstein manifold has no nonzero Killing field, so every exact circle-action statement here concerns proper regions.

**Conditional topological consequence.** Assume an exact, globally oriented, semi-free circle action on a region with genuine free-orbit boundary, and fix nut signs relative to the 4D orientation. Removing invariant neighbourhoods of the fixed set and applying Stokes on the orbit space to the closed curvature of a principal connection, the boundary Chern numbers sum to zero. Compatible nuts have one sign, anti-nuts the opposite, and bolts enter through their normal Euler numbers. A region with N compatible nuts and no other fixed components therefore transmits boundary degree of magnitude N, and a closed orbit space containing only same-sign nuts is impossible. TNAdS does not discharge its nut: the degree-one bundle is transmitted outward while the circle opens.

None of these hypotheses is established for actual O10 sequences. W⁺ and Ric° are small only in normalized L² while W⁻ is unbounded, so neither an exact or controlled semi-free action nor a globally oriented circle structure follows. Path integrals of the error term in the general form of Proposition 4.1 are not controlled by four-dimensional L² smallness. Moreover, c₂(E₋) is a signed index count of zeros of a transverse section, and no theorem identifies every zero of v with a TN nut of index +1. The count N≍θV/ℓ² is therefore a model count.

## 5. Dense phase at the macroscopic scale (flat-base leading order)

Averaging the GH equation ΔV=−4πℓΣδ_a over cells requires the core energy as a function of the local background V̄, and this normalization matters. If the four-volume per core is frozen at 4π²ℓ²/θ, then n₃=θV̄/(πℓ) and Δ_γV̄=−4θV̄, a Helmholtz law. If instead V̄ is the actual local GH background and the field norm at the cell edge is fixed, the core is a homothety by V̄ of a TN of charge ℓ/V̄, with E_core=8π²m_*ℓ²/V̄. Then n₃=θV̄²/(πℓ) and

  Δ_γ V̄ = −4θ V̄²,  i.e. Δ_g V̄ = −4θ V̄ for circle-invariant V̄.

The second closure is the internally consistent one when V̄ varies macroscopically; the linear Helmholtz profile is not established. Either way the source is strictly negative and of the same order as the Einstein curvature. The dense phase therefore has macroscopic structure on the curvature scale, and V̄ is driven down; where V̄→0 the circle length 4πℓ/√V̄ grows. On a closed base the averaged equation has no positive solution (∫Δ_γV̄=0 against a strictly negative source), recovering the conditional degree obstruction of §4. With Λ=−1 the flat base must be replaced by the Jones–Tod Einstein–Weyl base and the monopole equation *(dV+θ_W V)=dω. For the Einstein condition, Tod's Toda description relates V to the Toda potential, so V is not free. The homogenized equation with source density proportional to V is the next precise object. In the hyperbolic Einstein–Weyl model (θ_W=0), positive solutions of (Δ+μ)V=0 exist iff μ is at most the bottom of the spectrum. This links admissible nut density to spectral data of the base, but it has not been derived for the actual Toda case.

## 6. What this changes for O10

1. Under the good-cell hypotheses, the flux-forced normalization region of a TN-type core has volume 4π²ℓ²+o(ℓ²) and base radius ≍ℓ^{1/3}. Its boundary is where the core's Weyl field falls to the Einstein scale. If such cores carry a fixed fraction θ of the energy, their completions tile a fixed fraction θ of the volume, with base spacing ≍ℓ^{1/3}, as Wigner–Seitz cells of a dense collapsed nut phase. The exact global identity is a depletion ledger. It does not by itself exclude isolated cores with depletion shells, but every core must pay for its energy through a compensating region of volume ≍ℓ².
2. The exact Einstein continuation (TNAdS, Ric=−g, W⁺=0 verified) costs nothing in the metric equation on the cell. In the scalar sector, the pure eigenvalue source is balanced by the mass/flux condition. The full order-ε coupled solvability, including torsion-parent, determinant-curvature and lattice-interface terms in the T²-equivariant sector, is the decisive local computation still to be made.
3. Within an exact semi-free circle-action model, the phase cannot close on itself. It transmits boundary degree N, which must be cancelled by bolts or anti-nuts; for exact W⁺=0 Einstein geometry these lie beyond ∫|K|≥3. TNAdS shows only transmission of one unit while the circle opens. A coarea estimate in an exact invariant collar gives schematically Vol(T)≳N·inf_T|K|²/|dK|. With |K|≍ℓ, N≍V/ℓ² and |dK|≍1 this is only O(V), not a contradiction. A superlinear volume would need |dK|≲|K| or another O'Neill-tensor bound, and in O10 the large derivative may be carried by the uncontrolled W⁻ geometry. The precise missing analytic quantity is therefore **the Ric° and W⁺ cost of maintaining large |dK|/|K| at collapsed circle length**. For the complex-hyperbolic Nil cusp (W⁺=0 after orientation reversal), a horosphere of degree N and central circle length L has volume ∝NL². Opening from L=ℓ to L=1 costs volume ≍N≍V/ℓ², while retaining only the tail L≤ℓ costs ≍Nℓ²≍V. This is a scaling heuristic only: degree-sign compatibility, capping, field extension and defects are unchecked.
4. The O11 results (certified sub-four cells, period-linear ledger, Ricci-flow consequence) are unaffected.

Open items carried forward: (i) the order-ε T²-equivariant coupled cell problem with torsion and determinant curvature, posed periodically on the Wigner–Seitz lattice with shared fluxes; (ii) a weak form of Proposition 4.1 under L² control, using its exact error form, or an ε-regularity input on the collapsed region; (iii) a homogenized Jones–Tod/Toda equation derived from the actual metric and field system, with the correct power of V̄ in the source; (iv) the Ric°/W⁺ cost of large |dK|/|K| at collapsed circle length, which is the quantity that could turn §6.3 into a density-free O10 inequality; (v) a theorem relating zeros of v (signed c₂(E₋) count) to TN-type cores.

Independent reading: `trace/ttcs/results/step45_ttcs01_verifier1_integration.md`. Its corrections — the sign of Proposition 4.1, the mass/flux versus volume radius, the depletion-ledger formulation, the limited §3 statement, the conditional degree theorem, the V̄² homogenization, and transmission rather than discharge in TNAdS — are incorporated above.

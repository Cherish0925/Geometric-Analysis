# Step 77 Route Map

Session `S0910A03`, Agent2 / Explore.

## Current state of the negative branch (dimension 4)

### Established results

1. **R_γ ≤ -24 under a global normal foliation** for the center-normalized PE
   representative of a reflected Einstein core on [0,∞) × T³ with S(0)=0.
   Pointwise Riccati comparison gives H ≤ 3 tanh(r). Preissmann excludes equality
   on every ray, hence strictness somewhere, but not automatically at each
   boundary point. Formula: R_γ(x) = -12 - 4∫₀^∞ e^{2r}|S-I|²(r,x) dr.

2. **Center theorem**: For any T²-cohomogeneity-one scalar-(-6) center,
   K_orb ≥ 3 and λ_min S'(0) ≤ -3 + 3δ at defect δ.  Integrated center
   energy: ⟨d_s²⟩_ρ ≥ 12 - 8δ.

3. **ASD obstruction**: ASD + Ric=-3g + totally geodesic T³ ⟹ W=0 ⟹
   sec = -1 ⟹ impossible on T³ (Preissmann).  So any reflected core must be
   non-ASD.

4. **Expanding tail**: Order-one anisotropy erased at vanishing Ricci cost
   over a long expanding tail, uniformly in lattice parameter N.

5. **Exact anisotropy rigidity**: In the diagonal T²-invariant class, exact
   reflected cores cannot have zero orbit-anisotropy flux at a finite exit.

6. **Fuchsian decomposition (notation corrected)**: put u_H=3-H,
   w=3(1-tanh r), z=u_H-w and Z=e^{2r}z. Then
   Z'=((u_H+w)/3)Z+e^{2r}|P|², Z(0)=0, and
   -R_γ/4=6+lim Z. The Fuchsian (cosh) warped product contributes the first
   term 6; anisotropic stress contributes the nonnegative second term.

### Three distinct geometric objects (corrected from Step 76)

| Object | Location | Condition |
|--------|----------|-----------|
| q₀ (center metric) | r=0, S=0 | R(q₀)=-6 |
| γ (conformal infinity) | r→∞, PE end | R_γ ≤ -24 pointwise under global normal foliation; strict somewhere (center-norm.) |
| g₃ (TT filling datum) | PE expansion coeff. | tr_γ(g₃)=0, div_γ(g₃)=0 |

The leading PE stress e^{2r}S° → Sch(γ)°♯ is determined by γ alone.  The
nonlocal filling datum is g₃, extracted at order e^{-3r}:
  e^{3r}[S° - Sch°♯ e^{-2r}] → -(3/2) γ⁻¹g₃.

### Unresolved core question

Does there exist a non-ASD PE Einstein filling on (0,∞) × T³ whose backward
evolution from the PE end reaches S=0 at finite distance?  Equivalently, does
the scattering map Φ:(γ,g₃)→S(0) contain 0 in its image?

Anderson's Fredholm index 0 theory gives locally discrete fillings for fixed
conformal class, but neither existence nor surjectivity.  The dimension of the
center data (2 function d.o.f. after gauge/constraint) matches the PE data,
so the problem is not over-determined by naive dimension count.

The defect alternative: even if no exact core exists, approximate cores with
weighted defect moments O(1) but pointwise defect → 0 might suffice.  The
weight e^{2r} in ∫e^{2r}E_{rr}dr means pointwise-small defect can accumulate
finite renormalized stress.

## Current state of the positive branch (dimension 4)

A01 reports: all Ozuch O(t^{5/2})-level obstructions vanish for the mixed-
chirality (S²×S²)/Z₂ product quotient under A+J+L symmetries.  The surviving
system is a 2×2 radial equation at O(t³).  OSS/Tian confirm KE on Bl₅(P²) for
the same-chirality case (framework validation).  The mixed-chirality resolution
#₃(S²×S²) is not Fano, so KE existence is not guaranteed by OSS/Tian.

A02 reports: classical Weitzenböck/Gursky-LeBrun mechanisms cannot obstruct
positive Einstein on chi=8 mixed rows.  Chiral ALE exclusion: max |Γ|=4 on
balanced rows.  Outermost model must be ALF/ALG/ALH.

Status: no positive-branch obstruction or existence theorem.

## Next steps (prioritized)

### A. Finite forced matrix connector (supersedes ordinary Jacobi analysis)
A complete non-ASD PE filling is sufficient but unnecessary for the graph
construction. Derive the full two-base-variable T²-reduced Einstein--DeTurck
system for the orbit matrix U∈SL(2,R)/SO(2), Hamilton--Codazzi equations, and a
small source E. Seek a parameter-dependent finite connector with sup|E|→0 and
exit S→I plus scaled intrinsic curvature→0. A decaying Jacobi field preserving
a Li--Liu cusp normally preserves that end type; cusp opening is a singularly
translated transition and should not be inferred from an ordinary kernel.

### B. Full T²-reduced Einstein-DeTurck system
Derive the complete reduced system for the matrix-valued orbit block
G = ρU with U ∈ SL(2,ℝ)/SO(2), including all Hamilton/momentum constraints,
the DeTurck gauge, and the conformal factor.  This extends the scalar d=b-c
equation to the full orbit shape space and is needed for any rigorous
shooting or BVP computation.

### C. Forward shooting from center data
Implement a numerical forward evolution from validated center data (q₀, S=0)
with R(q₀) = -6, monitoring:
  - λ_min(ḡ_r) (PE vs collapse)
  - e^{-2r}||Ric(q̄_r)|| (damping effectiveness)
  - e^{3r}[P - Ric(γ)°♯ e^{-2r}] (filling response g₃)
Use the Koiso seed family from Step 69 as initial data.  This is an elliptic
Cauchy problem (ill-posed), but finite-precision forward propagation may reveal
whether PE behavior or singularity formation is the generic outcome.

### D. Weighted defect accounting
For the approximate (non-exact) route, develop bookkeeping for the weighted
moments ∫e^{2r}E_{rr}dr and ∫e^{3a}E_T° dr along candidate approximate
cores.  These determine whether the renormalized PE stress can be achieved
with vanishing pointwise defect.  Check whether existing numerical residuals
(~16 in Step 75) are artifacts of finite spectral parameterization or
structural lower bounds.

### E. Positive branch complementary work
Continue absorbing A01/A02 positive-branch results. Standard #₃(S²×S²) has
b₊=3 and cannot be positive Kähler--Einstein; the mixed-chirality problem needs
a genuinely non-Kähler Einstein mechanism. The direct Ozuch radial computation
at O(t³) remains a useful local desingularization test.

## Evidence files for this step

- `workspace/notes/step77_pe_scattering_correction.md` (main note)
- `workspace/scripts/step77_pe_expansion_verify.py` → `data/step77_pe_expansion.json`
- `workspace/scripts/step77_improved_bound_verify.py` → `data/step77_improved_bound.json`
- Corrected `workspace/notes/step76_center_energy_transport_and_scattering.md`
  (twist energy eq. 9.5)
- `trace/ttcs/results/step77_ttcs01_generator1_integration.md`
- `trace/ttcs/results/step77_ttcs01_verifier1_integration.md`
- Group messages: #553 (corrections), #561 (improved bound)

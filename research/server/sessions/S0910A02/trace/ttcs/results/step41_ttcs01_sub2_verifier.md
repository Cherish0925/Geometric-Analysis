# TTCS Independent Branch Record

```json
{
  "step_id": 41,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A02/workspace/notes/step40_diagonal_sector_rigidity_and_polygon_gap.md",
    "Sessions/S0910A02/workspace/data/step40_diagonal_sector_and_symmetric_wedge.json",
    "Sessions/S0910A02/workspace/data/step40_linearized_deformation_analysis.json",
    "Sessions/S0910A02/workspace/data/step41_regular_polygon_eigenvalue_probe_corrected.json",
    "Knowledge/objects/papers/Toric-Einstein-4-manifolds-with-non-negative-sectional-curvature--24d1f88fe098--1315c2a6cd67/object.md",
    "Sessions/S0910A02/workspace/notes/step33_routeA_consolidation_indicial_topology.md",
    "Sessions/S0910A03/workspace/notes/step40_staggered_all_order_continuation_candidate.md"
  ]
}
```

## Task

Evaluate the Step-40 diagonal toric reframe and the Step-41 critical updates for the Yau-26 project. The central questions are: (1) Does Liu's source really make the diagonal-sector identification unconditional for closed simply connected Einstein 4-manifolds with diagonal T^2 action, without nonnegative sectional curvature? (2) What exactly is source-grade about the reduced orbit-metric problem: fixed g_Σ determines g^Ω uniquely, but existence requires determinant/eigenfunction and boundary compatibility; does this justify saying the system is overdetermined, and what remains unproved? (3) Does the corrected Step-41 FEM probe legitimately strengthen or weaken the claim that constant-curvature m>=6 diagonal polygons are inconsistent? Treat it only as numerical evidence. (4) For Yau-26 route allocation, how much value should remain in the diagonal toric front versus returning to Route A's noncollapsed bridges or the negative cutoff-flow front? Please identify hidden overclaims, target drift, and the best next mathematical object to attack, using the files, not general guesses.

## Output

## Verification memo — Step-40 diagonal reframe and Step-41 eigenvalue probe

I read the two Step-40 files, the corrected Step-41 JSON, the full Liu source (arXiv:2311.04840), and the Step-33/A03-Step-40 route notes. The four questions resolve differently: the structural identification is well grounded in the source, but the strength attributed to the resulting non-existence evidence is larger than the numbers support, and the connection to Yau-26 is thinner than the diagonal front's activity level suggests.

### 1. The diagonal-sector identification is genuinely unconditional — with two things to correct

The chain Step 40 uses is sound and requires no sectional-curvature hypothesis:

- **Geometric polarity / twist scalars vanish.** Liu Theorem 3.1 (Section 3) states this for any isometric T² on a closed simply connected Einstein 4-manifold, with no curvature assumption. The proof forces α,β constant from Ric(X,Vᵢ)=0 and then zero by continuity at the singular strata. Confirmed.
- **Diagonal action ⟹ diagonal metric.** Liu Proposition 5 uses only that g₁₂^Ω solves the linear PDE (9), vanishes along every codimension-2 stratum, and Lemma 5.2 (uniqueness among R^even). Lemma 5.2 rests on the strong maximum principle applied to w=u/u₀ with u₀=g₁₁^Ω+g₂₂^Ω, again with no sec≥0. Confirmed unconditional.
- **Label restriction to ±e₁,±e₂.** The JSON argument (a rod needs p²a²+q²b²→0 on a codimension-2 set, so one of p,q vanishes) is correct: with a,b>0 in the interior and orthogonal action fields, both vanishing is a codimension-4 (vertex) event, so rods carry (±1,0) or (0,±1). This is really the definitional content of Liu's "diagonal action" (Def 2) plus the vertex determinant condition, so it is not new mathematics but it is correctly stated.

Two corrections to the write-up:

- The Step-40 "Theorem (structural)" mildly conflates two directions — "diagonal action ⟹ diagonal metric" (Prop 5) and "diagonal metric ⟹ alternating labels" (the a,b argument). The stated conclusion (diagonal action ⟺ alternating-label polygon, unconditional) is correct, but item 2 as written is Prop 5, not the label argument; keep them separate to avoid a circular reading.
- The `polygon_comparison` table assigns topologies to **odd** m (m=5 → "#_1(S²×S²)"). A strictly alternating ±e₁,±e₂ polygon must have even m, and the identification is m=2k+2 (m=4→k=1, m=6→k=2, …). m=5 gives k=1.5 and does not correspond to any diagonal toric 4-manifold. The `b_plus_versus_m` block correctly lists only even m. The odd-m rows are regular-polygon geometry probes, not manifolds; the topology strings there are meaningless and should be removed or relabeled to prevent a later step from treating m=5 as a real target.

### 2. What is source-grade in the reduced problem, and what the "overdetermined" language actually covers

The rigorous, source-backed structure is:

1. **φ = orbit volume is the principal Dirichlet eigenfunction, eigenvalue 2Λ** (Liu Prop 2). This constrains g_Σ: its principal Dirichlet eigenvalue must equal 2Λ.
2. **Given g_Σ, the fiber metric g_ij^Ω is uniquely determined** by the linear elliptic PDE (9) with Dirichlet data from the rod ODEs and Neumann/smoothness data at fixed points (Liu Prop 3 + Lemma 5.2). "At most one" is proved.
3. **The nonlinear compatibility det(g_ij^Ω)=φ²** must hold, because φ is *both* the eigenfunction defining the PDE coefficients *and* the square root of the fiber determinant. Liu Prop 4 shows this is exactly where the flat-square case dies: the unique PDE solution gives det = sin²x sin²y + (p²/2)sin⁴x sin²y, which equals φ²=sin²x sin²y only for p=0. This is the true obstruction equation, and it is source-grade.

Against this, the Step-40 §4 "3 constraints for 1 free function ⟹ overdetermined ⟹ rigid" statement is a **heuristic linearized count, not a theorem**, and the note's own text says so. Two things weaken the count beyond what the note flags:

- The three "constraints" are objects of incomparable codimension. An integral solvability condition (Fredholm, one scalar), a set of Neumann corrections along edges (functional data on ∂Σ), and the traceless horizontal Einstein equation (a full PDE) cannot be added as "1+1+1 = 3 > 1." A genuine rigidity statement needs an actual Fredholm index or an implicit-function argument at the product metric, showing the linearized map has trivial cokernel after the true gauge (Λ-rescaling, the (1,0) kernel mode) is removed. The kernel computation (eigenfunctions sin(nx)cos(my), only (1,0) survives) is correct and is the right start, but the "overdetermined" conclusion is not yet earned.
- Liu's uniqueness is for **fixed g_Σ**. What Step 40 needs — and what remains entirely open — is existence/non-existence as g_Σ ranges over all admissible curved m-gon metrics (right angles, geodesic edges, λ₁=2Λ) with the nonlinear det=φ² closure. Liu closed m=4 only because sec≥0 forced g_Σ flat (totally geodesic Σ ⊂ M), then Lemma 5.1 gave the square, then Prop 4. Removing sec≥0 removes the flatness of g_Σ, and that is precisely the unexplored region.

So the defensible statement is: *for fixed g_Σ the Einstein fiber metric is unique (source), and the flat/constant-curvature representatives are obstructed by det=φ² for m≥6 (numerics, §3 below); existence over general curved g_Σ is open.* The word "rigid/isolated" should stay attached to the linearized count, not to a proof.

### 3. The corrected Step-41 probe: a real numerical improvement that, read at the right curvature, weakens rather than strengthens the intuitive obstruction

The correction itself is legitimate. The superseded probe used a `lambda2^2` mass weight; the corrected one uses the proper conformal mass weight for the Dirichlet eigenvalue on the Poincaré-disk polygon (mass with λ₂=4/(1−r²)², Euclidean energy). The `m6_convergence` array (λ₁ at unit curvature ≈ 6.981→6.973 as vertices go 1436→5744) shows clean convergence, so the reported λ₁ values are trustworthy as numerics.

But the quantitative reading matters, and here Step 40 and Step 41 point in opposite directions:

- Step 40's headline "**68.7% gap at m=6**" is computed in the **large-A asymptotic** (L_rod≈π/√(2A), s_reg≈1.317/√A). Large A is not where a solution can live. The eigenvalue condition λ₁=2 pins the curvature at A_eig≈0.287 for m=6, far from large A.
- At the physically forced curvature, Step 41 reports `rod_over_side_at_Aeig ≈ 1.018` for m=6 — the rod is only **~1.8% longer** than the edge — and `lambda1_at_side_match ≈ 1.890` (a ~5.5% defect from 2), with `relative_A_gap ≈ 5.8%`. These are near-miss numbers.
- The mismatch **grows with m** (m=5: 2.1%, m=6: 5.8%, m=8: 15.8%, m=10: 27%, m=12: 38%). So the first genuine target, m=6 = #₂(S²×S²), is the case where constant curvature *almost* closes.

Net: the corrected probe legitimately establishes that **no constant-curvature regular m-gon simultaneously satisfies edge-length matching and λ₁=2Λ**, for the tested m, and it does so more reliably than the flawed earlier run. But this is (i) a necessary condition under a constant-curvature restriction, and (ii) at m=6 the discrepancy is a few percent — comfortably within reach of a variable-curvature profile at fixed ∫K (Gauss–Bonnet fixes only the integral, not the profile). The correct reading is that the constant-curvature restriction produces a small mismatch at m=6, i.e. a near-miss that variable curvature could plausibly absorb, not a strong exclusion. The 68.7% figure should not be carried forward as the measure of the obstruction; the ~2% figure at A_eig is the relevant one.

### 4. Route allocation, target drift, and the best next object

**Target drift on the diagonal front.** Step 40 §7 states plainly that even a complete proof of "no diagonal T²-Einstein on #_k(S²×S²), k≥2" would not settle the Yau-26 positive branch: the antecedent supplies only C⁰ Ricci pinching (not T² symmetry), the output metric need not be toric, and a pinched metric may collapse along a different fibration. This is correct and it caps the value of the whole front. The diagonal sector is a positive-sign, four-dimensional, symmetry-restricted laboratory. Combined with the §3 near-miss at m=6, continued constant-curvature FEM has low marginal value: it is refining a necessary condition of a restricted ansatz whose full success still would not touch the mechanism Yau-26 needs.

If the diagonal front continues at all, the load-bearing object is not more constant-curvature spectra but the **variable-curvature nonlinear compatibility** det(g_ij^Ω)=φ² on the hexagonal (m=6) orbit space: does there exist a curved right-angled hexagon metric g_Σ with λ₁=2Λ whose Liu-PDE fiber solution closes det=φ² and meets all rod Dirichlet/Neumann/smoothness data? That is the actual existence question; the eigenvalue probe only tests one necessary condition of it.

**The b₊≤1 thread connects to Route A.** Step 40 §5 notes every known simply connected positive Einstein 4-manifold has b₊≤1, while #_k(S²×S²) has b₊=k. Step 33 independently reaches b₊=1 through the LeBrun–Ozuch Hermitian/admissible Del Pezzo classification, which would exclude #_k(S²×S²), k≥2, in one stroke — but only after the Hermitian/admissible input is supplied, which is exactly what a raw C⁰-pinched sequence does not give. The toric b₊ observation and the Route-A topology filter are the same exclusion approached from two sides, both blocked by the same missing structural input. Making this explicit is more useful than pursuing either in isolation.

**Route A (noncollapsed positive, 4D)** has a concrete, finite, decidable next object that also sits closer to the real problem (no symmetry assumed): the Lichnerowicz/Bianchi indicial inventory of symmetric 2-tensors on the cone C(S³/ℤ₂), with ℤ₂ parity, trace/Bianchi/volume gauge and pure-gauge quotient handled explicitly, culminating in the (2,−4) Wronskian pairing matrix matched against Ozuch's R₊v=0 condition (Step 33 §5–§8). The flat-cone sanity model already reduces the even roots in (−4,2) to the removable (0,−2) pair plus the geometric (2,−4) pair; replacing that sanity model by the genuine tensor spherical-harmonic computation would either close the bubble alternative of the noncollapsed positive subcase or expose a surviving mode. This is the highest-value object available.

**The λ<0 cutoff-flow front** (A03 Step 40) is advancing on the derivative-energy induction — the staggered all-order estimate correctly removes the two Step-39 errors (no false χ factor in ∇^{m+2}a; no current cutoff jet pushed to exponent 2p), and the finite triangular exponent schedule closes each (U_m,C_{m+1})→T_m stage. But it explicitly does not establish the transported-coefficient terminal restart, the sequence-uniform smoothing, or terminal calibration, and even completed it is a four-dimensional λ<0-family mechanism. The existential obstacle for this front is the per-manifold-versus-dimension-uniform gap recorded in Step 33 §9 (and the retraction there): Bishop–Gromov + CGB give only a per-manifold volume lower bound, so the flow currently supports at most fixed-topology statements, which cannot produce the dimension-only c_n,C_n the problem demands. That gap — a dimension-uniform lower volume/collapse-scale mechanism independent of the individual manifold — is the load-bearing unproved object on this front, more so than the terminal restart.

**Summary of hidden overstatements to correct in the record.**
- "68.7% gap at m=6" — evaluated at an irrelevant large-A regime; the relevant value at A_eig is ~1.8% (rod/edge) and ~5.5% (λ₁ defect), a near-miss.
- "product metric is rigid / m≥6 excluded" language — supported only by a dimensionally-naive constraint count and by constant-curvature numerics; the variable-curvature existence question and the det=φ² closure over curved g_Σ are untouched.
- Odd-m topology labels in `polygon_comparison` — not real manifolds; remove.
- The diagonal front's implicit framing as a Yau-26 sub-result — §7 already limits it to a stress test of one collapse scenario; that limit should govern how much further computation is invested.

The single best next mathematical object is the genuine Lichnerowicz/Bianchi indicial and Wronskian computation on C(S³/ℤ₂) in Route A: finite, decidable, route-determining, and connected to the C⁰-pinched problem without a symmetry assumption. Within the toric front, if continued, the object worth attacking is the variable-curvature det(g^Ω)=φ² existence on the m=6 hexagon, not further constant-curvature eigenvalue refinement.
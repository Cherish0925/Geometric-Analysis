# Step 2 synthesis — O10/O11 combined research state

## A. O10: Taub–NUT tangent blocks the simplest proof strategy

### Key finding (from TTCS generator 2, verified against the extract)

The full leading coupled tangent system at a radial-energy concentration scale admits a **nontrivial complete solution**: one-centre Taub–NUT with an opposite-chiral spinor from a holomorphic coordinate. Its amplitude is
\[
m=m_*\frac{R}{R+\ell},\qquad m_*=128/81,
\]
which has a genuine lower well (m→0 at the nut, m→m* at infinity), nonzero radial Dirichlet energy ∫|∇v|²=8π²m*ℓ², and satisfies all of:
- Ric=0, W⁺=0 (leading metric is hyper-Kähler)
- F_A=0 (determinant connection flat at leading order)
- ∇_AΦ₀=0, |Φ₀|²=4/3 (parallel positive spinor)
- D⁻v=0, P_{J+}∇v=0, ∇*∇v=0 (Dirac, type, rough-harmonic)
- Both curvature equations (3.6) hold (real Levi-Civita connection)
- First-order torsion parent exists (linear perturbation of parallel Φ₀)

The connection supporting the well is the **actual ASD spin connection of Taub–NUT**, which is instanton-like.

### What this rules out
A density-free endpoint proof cannot use a Liouville theorem asserting "every complete finite-energy geometric tangent with nonzero radial mass is trivial." The round S³-warped, flat R²×T², and ALE HK ansätze *are* obstructed (the first by Ricci flatness ⟹ flatness, the second by bounded harmonic functions on R², the third by ALE end representation theory + Bishop–Gromov). Taub–NUT escapes because its end is ALF (circle-collapsed), not ALE.

### What remains for O10
Two specific mathematical objects could still save the density-free theorem:
1. **Order-r² field compatibility**: at leading order F_A=0; the monopole source and bounded determinant-curvature model are order r². Completing the equations at order r² on Taub–NUT gives a coupled linear system for (k, a, Φ₂) with radial ODE reduction in the biaxial equivariant sector. Solvability with decaying/matchable asymptotics is the precise question.
2. **ALF end matching cost**: Taub–NUT has an asymptotically finite Hopf circle. Embedding it into a noncollapsed closed manifold may force a scale-invariant Ricci cost that cannot be sent to zero. This is a transition-annulus calculation, not a global identity.

If (1) has a decaying solution and (2) has affordable matching, the Taub–NUT local core becomes a genuine building block for an O10 escape. If either has an obstruction, that obstruction identifies the specific identity needed for a general proof. Either outcome is a scientific advance.

## B. O11: comprehensive cell-problem picture

### Exact reduction (verified by TTCS verifier)
\[
P(g)-8\pi^2Q=4\bigl(W_+(g)-\tfrac43\pi^2A\bigr)+\frac{S(g)-32\pi^2A}{12}
\]
and for a single cell U replacing a CH ball B:
\[
P(U)-8\pi^2=4\Delta W_++\frac{\Delta S}{12}.
\]
Burns gives exactly 8π²; every U(2)-invariant cell computed has P > 8π², with slope (P/8π²−1)/x₀ → 6 as x₀→0. The split is 4ΔW+ → 4x₀ and ΔS/12 → 2x₀ (units of 8π²).

### S1003A01 triaxial result (conformal SU(2)-diagonal, message 739)
Their independent numerical optimization over a broader ansatz (full conformal triaxial) confirms: no sub-threshold cell. All optima lie above the conformal Kähler lower bound of Theorem 1 of the corpus (I54). Non-Kähler (triaxial w-direction) only decreases at high cost, never crossing the threshold. Conjecture C1: the Theorem 1 bound holds for the entire conformal almost-Kähler diagonal class.

### TTCS verifier corrections and clarifications
1. `u2_curvature.py` labels chirality opposite to the complex orientation; `u2_xcoord.py` correctly swaps. Code is substantively correct but documentation should be fixed.
2. The Kähler formula 1+6x₀+9x₀²(1+X⁻²) is a small-x₀ expansion, not the exact finite-X expression. In the limit X→∞ it becomes exactly (1+3x₀)².
3. The outer matching is C¹/H², not literally CH on an open collar (can be smoothed with vanishing error).
4. "Every U(2) cell has P > 8π²" is *not proved*; only every returned parametrized profile has that property. Numerical minima are upper bounds.
5. The slope-6 universality heuristic misses a possible relative-orientation modulus (angle between Burns and CH Kähler forms). The U(2) computation tests only the aligned case θ=0.

### TTCS generator 1: ΔW+ ≥ 0 is likely false
The strict total-Weyl connected-sum construction gives δ(W++W−) < 0 with δ(W+−W−) = 0 (signature), hence δW+ = δW− < 0. If that construction can be localized to a cell, then ΔW+ < 0. The real question is the *joint* bound P(U) ≥ 8π², not the separate ΔW+ ≥ 0.

### Most decisive next tests for O11
1. **Burns weighted deformation complex**: classify the kernel on Burns, compute the boundary pairing −8π²λm_K, prove or disprove orientation-universality.
2. **Strict Weyl one-neck + conformal scalar minimization**: on the Malchiodi–Malizia gluing metric, fix the Weyl energy and minimize S inside the cell by a conformal factor; this is a scalar fourth-order BVP. If the scalar saving exceeds 48 times the Weyl deficit, P(U) < 8π².
3. **Non-monotone-b cells (internal neck)**: use full biaxial Bianchi IX to allow a(t) turning points, multiple throats, and long near-Einstein segments.
4. **Composite blow-up+handle cells**: the balanced family has k/ℓ = 8/7; test P(U_{1,1}) < 40π² as the minimal compound.

## C. Research priorities

| Priority | Question | Object to compute | Decides |
|---|---|---|---|
| 1 | O10 order-r² completion | Coupled (k,a,Φ₂) radial ODE on Taub–NUT | Whether ALF escape or new obstruction identity |
| 2 | O11 Burns perturbative theorem | Weighted kernel + boundary pairing + orientation | Per-site penalty universality |
| 3 | O11 Weyl gluing cell cost | Θ = 4ΔW+ + ΔS/12 on MM metric | Whether strict Weyl saving lowers P |
| 4 | O10 ALF matching cost | Transition annulus Ric cost for circle scaling | Whether noncollapsed embedding is affordable |

## D. Files

- `workspace/notes/step2_blowup_cell_problem_O11.md` — detailed O11 cell reduction, exact Kähler formula, numerical table and interpretation
- `workspace/notes/step1_field_compatibility_and_route_portfolio.md` — inherited route portfolio from Step 1
- `workspace/scripts/u2_curvature.py`, `u2_xcoord.py`, `kahler_cell_exact.py`, `u2_cell_jax_log.py` — computation chain
- `workspace/data/u2grid/u2_cell_grid2.jsonl` — full numerical results
- `workspace/figures/u2_cell_cost.png` — cell cost figure
- `trace/ttcs/results/step2_ttcs01_generator1_integration.md` — O11 full generator memo
- `trace/ttcs/results/step2_ttcs01_generator2_integration.md` — O10 Taub–NUT tangent memo
- `trace/ttcs/results/step2_ttcs01_verifier1_integration.md` — verification of cell computation

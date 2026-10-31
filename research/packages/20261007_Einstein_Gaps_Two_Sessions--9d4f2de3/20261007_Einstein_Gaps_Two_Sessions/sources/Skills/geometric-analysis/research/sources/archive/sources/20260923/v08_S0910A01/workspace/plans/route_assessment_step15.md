# Route assessment after Step 15 — superseded by Step 16 Preceptor review

> **Step 16 correction.** The previous Step 15 assessment overstated the state of the proof.  It treated A03's localization argument and the smoothing-to-accessibility links as completed.  That completion wording is withdrawn.  The live review and corrected route are in `workspace/notes/step16_preceptor_review_smoothing_architecture.md`.

## What Step 15 genuinely contributed

### 1. A coherent conditional smoothing architecture

Step 15 assembled a valuable route for the four-dimensional negative LeBrun/Ishida--LeBrun critical laboratory:

good-set packing → local Li-scale initial smallness → cutoff normalized flow → possible curvature-energy bootstrap → defect propagation → topological recalibration → bounded-curvature cover accessibility → Step 8 Derdziński tensor-deficit contradiction.

This architecture is useful because it identifies where collapse enters and where a smoothing theorem could bypass the lack of initial harmonic radius.  It is not currently a proof.

### 2. Comparable-ball Bishop--Gromov transfer

The calculation is valid in its precise local range.  If a maximal-function good point `p` satisfies

\[
\mathcal M_R(|Rm|^2)(p)\le K_0,
\]

then for centers `y` with `d(p,y) <= 5r_*/2`,

\[
r_*^4\fint_{B_{r_*}(y)}|Rm|^2
\le r_*^4K_0 {V_{-1}(13r_*/2)\over V_{-1}(r_*)}.
\]

Taking `r_*` small makes Li's initial dimensionless quantity small independently of collapse.  This does not control all centers in a much larger `B_{rho/4}(p)` unless the support scale is chosen consistently or a stronger maximal-function hypothesis is imposed on every required center.

### 3. L² completion-square and topological recalibration

A03's algebraic chain

\[
\int\left(|W^+|-{1\over2\sqrt6}\right)^2\le {7\over24}\int|E|^2
\]

is a useful volume-independent modulus estimate on critical topology.  For the full forbidden spectrum, the Step 8 explicit tensor-deficit route should be used:

\[
0\le\int \mathcal G\le48\pi^2D,
\qquad
\mathcal G=f^2-(a_-)^2.
\]

If a terminal smoothed metric satisfies `J/A -> 0`, then Chern--Weil and LeBrun's mixed SW estimate can be rerun on that metric.  This avoids transporting `W^+` through the flow.  The needed input is terminal global integral Ricci-defect control, not merely local plateau estimates.

### 4. Homogeneous cutoff-defect evolution

The equation

\[
\partial_tg=-2\chi^2(\operatorname{Ric}+g)
\]

has a defect evolution whose transition terms are homogeneous in `E` and its derivatives.  Exact negative Einstein metrics are stationary even across the transition.  This removes an additive source at `E=0`, but it does not by itself prove amplification bounds for small nonzero `E`; transition terms such as `d\chi * \nabla E` require an actual energy estimate.

## What Step 15 did not establish

### Invalid localization argument

A03's Sections 10--12 argued that Li's proof localizes directly to an inner plateau because covering balls stay in a working domain and because parabolic propagation has scale `sqrt(t)`.  This is invalid as written:

- Ricci flow has no finite propagation speed; a diffusion length is not a boundary of influence.
- Li's bootstrap supremum over a working domain needs covering balls for centers near the working-domain boundary; these may leave the domain.
- Restricting the supremum to an inner domain recreates the unclosed inner/outer energy inequality corrected in A03 Step 14.
- The comparable-ball good-point estimate controls only centers near the chosen point at the `r_*` scale, not an arbitrary larger plateau when `r_* << rho`.

### Uniform cutoff-flow package remains open

The needed theorem must give collapse-uniform existence time, persistence of local normalized curvature energy, metric equivalence, interior `C/t` curvature control, and global defect control including transition annuli.  Existing Li/Yang/Wang results strongly motivate this but have not yet been matched to the exact hypotheses.

### CFG accessibility remains a separate theorem

Bounded curvature is the right entry point for collapse theory, but the Step 9--11 contradiction needs genuine buffered normal covers with lifted noncollapse and harmonic-radius control on a fixed volume proportion.  Naber--Zhang rank/residual-dimension hypotheses or CFG fibration output must be verified and converted into this exact accessibility statement; the current notes have not done that.

## Correct current status of the negative LeBrun critical route

| Component | Status |
|-----------|--------|
| Good-set packing | Valid, subject to scale choices |
| Comparable-ball initial Li smallness | Valid for nearby centers at comparable scale |
| Sobolev--energy collapse cancellation | Valid and important |
| Cutoff defect homogeneity | Valid algebraic support |
| Uniform cutoff-flow existence with estimates | Open |
| Plateau curvature bootstrap | Open; direct localization argument invalid |
| Transition-inclusive global defect control | Open |
| Topological recalibration | Conditional on terminal `J/A -> 0`; use Step 8 tensor deficit for spectrum |
| Bounded-curvature normal-cover accessibility | Open unless a precise theorem is proved/sourced |
| Derdziński forbidden germ | Valid once controlled chart/cover and explicit defects are present |
| Volume contradiction | Conditional on the open analytic and geometric links |

## Actual scope

Closing this route would exclude an important critical LeBrun/Ishida--LeBrun family of negative-branch counterexample sequences.  It would not prove the full four-dimensional negative sign branch for arbitrary no-Einstein four-manifolds, would not settle the positive branch, and would not address dimensions `n >= 5`.

## Next work

The highest-priority next action is not final theorem writing.  It is to establish or disprove the missing mechanism:

1. formulate a support-scale-consistent cutoff-flow theorem with all centers controlled inside the support;
2. prove a closed curvature-energy and Einstein-defect estimate retaining the `chi` transition terms, aiming at `Q_i(t_0)/A_i -> 0` plus interior `|Rm| <= C/t` on smoothed plateaux;
3. source or prove the bounded-curvature-to-buffered-normal-cover accessibility statement needed by the Step 9 mean-transport and Step 8 Derdziński contradiction.

Positive-branch toric work and higher-dimensional routes remain separate and substantially less developed.

## Key files

- `workspace/notes/step16_preceptor_review_smoothing_architecture.md` — live correction and repair target
- `workspace/notes/step15_cutoff_smoothing_architecture.md` — superseded architecture with useful calculations
- `workspace/scripts/step15_smoothing_architecture_verification.py` — numerical checks of scale constants only
- `Sessions/S0910A03/workspace/notes/step15_L2_chain_and_separated_demands.md` — peer note; Sections 10--12 localization argument is invalid as written
- `workspace/notes/step14_smoothing_vs_reduction_route.md` — source comparison
- `trace/ttcs/results/step15_ttcs01_verifier1_integration.md` — TTCS concerns supporting conditional status

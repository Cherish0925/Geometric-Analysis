# Step 31: Consolidated status

## Summary

This step resolved the weighted Moser iteration controversy, established
the coupled continuation theorem, corrected the support and terminal
constructions, and received three independent confirmations
(TTCS V1, Codex, own derivation) of the weighted route.

## Established results (this step)

### 1. Weighted Moser interpolation is correct
The alleged "half-power gap" (A01 #323) is irrelevant because the iteration
never uses ||Z_p||_3^3. The actual parabolic step combines:
- sup_t K_p (energy)
- K_{2p} = ||Z_p||_4^4 (Sobolev on Z_p = a^{(p-1)/2}Φ^{p/2})
- K_{3p/2} ≤ K_p^{1/2} K_{2p}^{1/2} (Cauchy-Schwarz)

**∇Z_p gradient decomposition** (key mechanism): ||∇Z_p||_2^2 ≤ Cp²(D_p + r^{-2}K_p)
where D_p is the a-WEIGHTED curvature dissipation from the energy inequality.
No unweighted gradient is needed. No lower bound on a is needed.

**Three independent confirmations:**
- TTCS Step 31 V1: "插值恒等式、∇Z_p 的权重匹配以及极限 ||aΦ||∞ 都正确"
- Codex report: "The strongest valid replacement is the mixed weighted recurrence"
- verify_step31_weighted_interpolation.py: 8/8 checks pass

### 2. Unweighted Moser on U = aT FAILS
The diffusion is a·ΔU, so energy controls only ∫a|U|^{p-2}|∇U|².
Sobolev needs unweighted ∫|U|^{p-2}|∇|U||². Since a ≤ 1, we cannot
bound unweighted from a-weighted. Codex provides a concrete 1D counterexample.

### 3. Coupled continuation theorem
At order m, the induction couples (∇^mU, ∇^{m+1}χ):
  d/dt(X_p + Z_p) + cD ≤ C(1 + X_p + Z_p)
Grönwall closes without dividing by χ. Then ∇^mT is recovered on the
plateau (where a = 1, so T = U directly).

**TTCS correction incorporated:** On transition region {0 < a < 1/2},
the flow IS active. Resolution: the continuation only needs U-derivative
bounds (for flow existence) and plateau regularity (for terminal argument).
Transition-region T-bounds are not needed.

### 4. Support geometry (corrected)
- Maximal r-separated good net in G = {M_r(F²) ≤ ΛK̄}
- Graph coloring at distance 12r
- Maximal-volume color retains ≥ Vol(M)/(2(N+1)) of strict centers
- B_{6r} disjoint auxiliary domains
- Chart radius reduced to 2r (TTCS correction for bilipschitz safety)

### 5. Terminal density (corrected)
- ε = Q/Vol for positive-part regularization
- Vol ≤ Cχ(M) from CGB (TTCS correction: volume UPPER bound)
- Eigenline density restricted to bounded-curvature plateau L_i
- Q/A → 0 via: Q ≤ Cδ²Vol ≤ Cδ²χ(M) ≤ CΛδ²A

## TTCS corrections applied (5 items)
1. Sobolev step: no square root in critical p=2 formula
2. Reaction term weight: a^{p-1}, not a^{p-2}
3. Chart radius: 2r, not 3r
4. Q/A: use Vol ≤ Cχ(M), not Vol ≥ cA
5. Transition region: flow IS active on {0 < a < 1/2}

## What remains for the negative branch
- Full multi-step Moser recurrence with nested time cutoffs (bookkeeping)
- Regularization a → a+ε passage (standard degenerate parabolic theory)
- Projector parallelism from eigenline saturation (density definition in Step 16)
- Interior Shi estimates on plateau at positive time (standard)

These are technical completions, not mathematical obstacles.

## What remains for full Yau 26
- Positive normalized branch (all dimensions)
- Unrestricted 4D topology (non-IL manifolds)
- Dimensions n ≥ 5
- Dimension-only constants
- Lean 4 formalization

## Files produced
- `workspace/notes/step31_weighted_moser_interpolation_and_first_exit.md` (main)
- `workspace/notes/step31_coupled_continuation_theorem.md` (continuation)
- `workspace/notes/step31_corrected_support_and_terminal_density.md` (geometry)
- `workspace/scripts/verify_step31_weighted_interpolation.py` (exit 0)
- `workspace/scripts/verify_step31_coupled_continuation.py` (exit 0)
- `workspace/codex_loop/Research_Report.md` (independent Codex confirmation)
- `workspace/codex_loop/work/weighted_moser_and_continuation_repair.md`
- `workspace/codex_loop/work/verify_weighted_moser_coupling.py` (exit 0)
- `trace/ttcs/results/step31_ttcs01_verifier1_integration.md`

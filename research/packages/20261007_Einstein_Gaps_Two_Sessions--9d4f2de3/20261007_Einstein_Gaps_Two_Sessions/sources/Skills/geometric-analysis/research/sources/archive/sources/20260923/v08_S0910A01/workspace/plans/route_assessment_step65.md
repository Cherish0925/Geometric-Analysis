# Route assessment: Step 65

Session S0910A01, Agent2 / Constructor. Phase: Execute.

## What Step 65 produced

A self-contained per-datum existence theorem for the exact degenerate cutoff
flow: `workspace/notes/step65_per_datum_existence_theorem.md` (603 lines).

The theorem proves: given a closed manifold, a smooth positive metric g₀, a
smooth cutoff χ:M→[0,1], and any σ∈ℝ, there exists T₀ > 0 (depending on
the smooth datum) and a smooth solution g(t) of ∂ₜg = -2χ²(Ric - σg) on
[0,T₀].  The construction uses:

1. A doubly regularized (ε,ν) transported-DeTurck system with diagonal
   strongly parabolic principal blocks.
2. A standard quasilinear parabolic theorem (Theorem A) with explicitly
   verified strong Legendre–Hadamard hypotheses.
3. The (ε,ν)-independent tame hierarchy (Proposition 3.1 of A03 Step 56)
   giving all-order Sobolev bounds on a common time interval.
4. All-order continuation argument: if T_max < T₀, all H^m norms stay
   bounded (by Grönwall on the tame inequality for each m with s₀-level
   coefficient), hence all C^k norms stay bounded, contradicting Theorem A's
   continuation criterion.
5. Arzelà–Ascoli diagonal subsequence convergence in C^∞.
6. Geometric pullback via the DeTurck diffeomorphism.

TTCS verification (`trace/ttcs/results/step65_ttcs01_verifier1_integration.md`)
found three genuine repairs, all incorporated:
- Lie cross term uses β²/(β²+ε) ≤ 1, not β⁴; the fourth power belongs to
  the transport coupling.
- Continuation must invoke the all-order tame hierarchy, not merely the s₀
  bound, to prevent arbitrary C^k blow-up.
- Uniqueness of the degenerate limit is not established by subsequential
  compactness alone; the claim was softened accordingly.

Structural verification: 24/24 (`workspace/data/step65_per_datum_existence_verify.json`).

## What this changes for the restricted IL theorem

Before Step 65, the restricted IL negative gap theorem was conditional on
one named hypothesis: per-datum existence of the degenerate cutoff flow
(recorded in Steps 61–64 route assessments).  This theorem removes that
hypothesis for σ = -1.  The conditional chain is now:

  SW budget → proportional-volume support → **per-datum existence (Step 65)** →
  (Γ,V) bootstrap → curvature/defect endpoints → continuation →
  common-time smoothing → terminal compactness → forbidden germ →
  A-cancellation contradiction.

The per-datum existence is the first link after the topological/geometric
input.  The remaining chain (Steps 55–63) has been previously verified at
proof level, with the Step 64 convention sweep ensuring internal consistency.

## What this does NOT settle

1. Sequence-uniform time (Level 2): requires the first-exit bootstrap, not
   the per-datum theorem.
2. Dimension-only constants (Level 3): requires a global Yau-26 mechanism.
3. Positive branch: no Seiberg–Witten calibration analogue is known.
4. Arbitrary four-manifold topology: restricted to IL geography.
5. Dimensions n ≥ 5: no curvature-budget mechanism.
6. Lean formalization: unstarted.
7. Full Yau 26: far from resolved.

## Next mathematical priorities

1. **Assemble the restricted IL theorem as a self-contained conditional
   statement**, conditional only on the Seiberg–Witten geography input
   (no further analytic hypothesis).  This is a genuine new mathematical
   result.

2. **Return to the Yau-26 crux**: positive-branch calibration, mixed-filling
   counterexample candidates, higher-dimensional mechanisms.

3. **Independent verification of the tame hierarchy**: A03's allocation
   script (14M checks) verifies the combinatorial structure; the analytic
   argument should be independently checked term by term.

4. **Peer coordination**: A02's obstruction framework (#479) for mixed EH
   patterns on (S²×S²)/ℤ₂ is positive-branch work; A03's correction (#478)
   withdraws the curved-slice closure.  The graph-manifold counterexample
   route remains open in the general γ(r,x) class.

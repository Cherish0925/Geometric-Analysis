# TTCS Independent Branch Record

```json
{
  "step_id": 21,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "unavailable",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step21_derivative_free_first_exit_and_plateau_regularity.md",
    "Sessions/S0910A03/workspace/notes/step20_weighted_wang_hierarchy_and_whitney_correction.md",
    "Sessions/S0910A03/workspace/notes/step19_p4_threshold_and_degenerate_moser.md"
  ]
}
```

## Task

The derivative-free first-exit framework reduces the 4D negative-branch cutoff-flow program to one PDE task: the localized zero-order Moser iteration for the degenerate normalized cutoff flow. Consider what alternative approaches or structural insights could bypass or simplify this remaining PDE localization.

Specifically: (A) Wang's proof is for the unnormalized cutoff Ricci flow on a complete manifold with global Sobolev and energy bounds. The needed adaptation is to finite-neighbor domains with normalized flow. What is the simplest way to extract the needed local estimates? Could the completed-manifold trick (extend the closed manifold trivially and apply Wang's global theorem) work? Could a time-layer argument avoid the nested-cutoff/evolving-measure complexity?

(B) Is there a more direct route to the calibrated contradiction that avoids the full Moser iteration? For example: if one only needs |Rm| bounded at some positive time on the plateau (not the sharp C/t rate), could a softer estimate suffice? The downstream needs are: (i) smooth compactness at fixed time T_0, (ii) defect → 0 on the limit, (iii) |W+| = 1/(2sqrt6) on the limit.

(C) A02's CZ spike audit shows that the weighted estimate is not broken by singular-kernel transplants. Could this stability property be used constructively to prove the estimate, e.g., by showing that the heat kernel of the degenerate operator dt - chi^2 Delta smooths faster than it generates curvature?

## Output

[No usable scientific output was produced by this independent branch.]
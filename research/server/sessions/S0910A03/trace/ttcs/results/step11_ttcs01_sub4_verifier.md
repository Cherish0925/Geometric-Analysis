# TTCS Independent Branch Record

```json
{
  "step_id": 11,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "unavailable",
  "context_files": [
    "Sessions/S0910A03/workspace/scripts/circle_reduction_weyl.py",
    "Sessions/S0910A03/workspace/scripts/verify_static_incompatibility.py",
    "Sessions/S0910A03/workspace/notes/step6_local_projector_obstruction_and_collapse_reduction.tex"
  ]
}
```

## Task

Verify the following static circle reduction formulas for a 4D Einstein metric with Ric = -g.

For a static Kaluza-Klein metric g = g_B + ℓ(x)² dψ² with Ric = -g:
1. The Einstein equations give: Ric_B = h - g_B and Δ_B ℓ = ℓ, where h = Hess_B(ℓ)/ℓ and tr(h) = 1.
2. The curvature operator on Λ²₊ (Besse convention) in the adapted SD basis has matrix R̂₊ with:
   - Diagonal: (R̂₊)₁₁ = 2h₃₃ - 1, (R̂₊)₂₂ = 2h₂₂ - 1, (R̂₊)₃₃ = 2h₁₁ - 1
   - Off-diagonal: (R̂₊)₁₂ = -2h₂₃, (R̂₊)₁₃ = 2h₁₃, (R̂₊)₂₃ = -2h₁₂
3. Hence W⁺ = R̂₊ + (1/3)I has: (W⁺)₁₁ = 2h₃₃ - 2/3, (W⁺)₂₂ = 2h₂₂ - 2/3, (W⁺)₃₃ = 2h₁₁ - 2/3, etc.
4. tr(R̂₊) = -1 = s/4, tr(W⁺) = 0.
5. The calibrated spectrum (-1/6, 1/12, 1/12) requires h = diag(3/8, 3/8, 1/4) in the eigenbasis.

For a cohomogeneity-one model g = dt² + a(t)² g_{S²} + ℓ(t)² dψ²:
6. The calibrated spectrum + Einstein give a'' = 3a/8 AND (a')² = 1 + a²/4, but differentiating the second gives a'' = a/4 ≠ 3a/8. Contradiction.
7. The ONLY constant-eigenvalue static Einstein has u = v = 1/3 (i.e., h = I/3, W⁺ = 0).

For the twisted case g = g_B + ℓ²(dψ + A)²:
8. The modified Laplacian is Δ_B ℓ + (ℓ³/4)|F|² = ℓ, giving tr(h) = 1 - ℓ²|F|²/4 < 1.
9. Near a smooth NUT (ℓ → 0), twist corrections to W⁺ are O(ℓ²), so the static formula W⁺ ≈ 2J(h - I/3) holds to leading order.

Check all signs, factors, and index assignments. Verify against the known results: constant curvature K = -1/3 gives h = I/3 and W⁺ = 0; the Taub-NUT-AdS has W⁺ = 0 but nontrivial warping (so twist must compensate).

## Output

[No usable scientific output was produced by this independent branch.]
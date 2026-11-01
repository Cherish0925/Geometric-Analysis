# TTCS Independent Branch Record

```json
{
  "step_id": 2,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "unavailable",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step2_quantitative_4d_analysis.tex",
    "Sessions/S0910A03/workspace/notes/step2_cap_analysis_and_route.tex",
    "Sessions/S0910A03/workspace/scripts/verify_chern_weil_pinching.py",
    "Sessions/S0910A03/workspace/scripts/critical_compatibility_model.py"
  ]
}
```

## Task

Verify the following chain of quantitative estimates for closed 4-manifolds M = X # k CPbar^2 under negative Ricci pinching ||Ric_g + g||_op <= delta < 1/(1+sqrt(3)).

CLAIM 1 (Theorem A): Using LeBrun 1996 (scalar curvature SW bound int s^2 >= 32pi^2 A where A=c_1^2(X)), the CGB + signature combination 4pi^2 k <= 4pi^2 A - E_s + E_R with E_R/E_s <= 3delta^2/(1-delta)^2, and E_s >= 4pi^2 A/3 from SW, one gets k/A <= 2/3 + delta^2/(1-delta)^2.

CLAIM 2 (Theorem A'): Using LeBrun 1998 Theorem A (the Weyl estimate 2 int|W+|^2 + int s^2/24 > (32/57)*4pi^2 A for any metric on M with nonvanishing SW invariant), combined with the CGB+signature identity 2 int|W+|^2 + int s^2/24 - int|Ric_0|^2/2 = 4pi^2(A-k), the LeBrun bound becomes int|Ric_0|^2/2 > 4pi^2(k - 25A/57). For k = 25A/57 exactly, this reduces to int|Ric_0|^2/2 > 0, giving NO pinching constraint.

CLAIM 3: For k/A slightly above 25/57, the leading-order pinching gap is delta^2 > (k/A - 25/57)/(3(1-k/A)). For k integer, k/A-25/57 >= 1/(57A), giving delta > C/sqrt(A) -> 0 as A -> infinity.

CLAIM 4: M = X_19 # 1875 CPbar^2 (degree-19 smooth hypersurface in CP^3, A = 19*15^2 = 4275, k = 25*4275/57 = 1875) satisfies: (a) LeBrun 1998 excludes all Einstein metrics, (b) 2chi-3|tau| = 2400 > 0, (c) k/A = 25/57 exactly, so no Chern-Weil/SW obstruction to tight pinching.

CLAIM 5: The positive branch is consistent with Q_4 true: tight positive pinching (Ric approx +g) forces s>0, killing SW invariant, finite pi_1 (Myers), and 2chi>3|tau| (strengthened HT). All known no-Einstein 4-manifolds have obstructions that are eliminated by these conditions.

For each claim, check the algebra, identify any gaps, and assess whether the chain from SW bound through CGB through pointwise ratio to the final k/A bound is rigorous.

## Output

[No usable scientific output was produced by this independent branch.]
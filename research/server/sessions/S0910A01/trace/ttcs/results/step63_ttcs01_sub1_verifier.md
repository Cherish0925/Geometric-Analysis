# TTCS Independent Branch Record

```json
{
  "step_id": 63,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "unavailable",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step63_curvature_variation_index_proof.md",
    "Sessions/S0910A03/workspace/notes/step57_H2_evolution_and_continuation_bridge.md",
    "Sessions/S0910A01/workspace/notes/step34_integrated_potential_q3_and_defect.md"
  ]
}
```

## Task

Verify the index-level curvature variation and H_2 inequality derivation for the restricted 4D cutoff flow partial_t g = -2aE, a=chi^2, E=Ric+g, n=4, T=Rm+G, F_T=(1+|T|^2)^{1/2}, H=int eta^2 F_T^2 d mu.

The proof note claims to close Premise C1 from the Step 61 gate audit: the index-level tensor identities consumed by the curvature Moser endpoint. Check these items:

(1) PURE-SCALING CHECKSUM: For a=1, E=g (partial_t g = -2g), does the derivation give partial_t R_{ijkl} = -2R_{ijkl}? The connection contribution should vanish (nabla g = 0, nabla a = 0), and the metric-variation contribution h_{l alpha} R^alpha_{ijk} = -2g_{l alpha} R^alpha_{ijk} = -2R_{ijkl}. Check §3.4 and the checksum table in §9.

(2) CURVATURE VARIATION (3.11): partial_t R_{ijkl} = a Delta_L R + (nabla^2 a)*E + (nabla a)*(nabla E) + a Rm*E + a Q(Rm). Is this the correct general form? The Ricci part h_Ric = -2a Ric gives the Lichnerowicz Laplacian via Hamilton's formula; the conformal part h_conf = -2ag gives Hessian terms via (3.8). Check that every term carries at least one factor of a or a derivative of a (no a-free source).

(3) HESSIAN TENSOR B (Lemma 4.1): The Hessian terms from (4.2) and (4.3) contracted with 2T give 2(nabla^2 a) B where B is algebraic in E, g, T. The bound |nabla B| <= C F_T |nabla Rm| follows from nabla g = 0, nabla T = nabla Rm, and |nabla E| <= C|nabla Rm| (Bianchi). Is the Bianchi inequality |nabla Ric| <= C|nabla Rm| correct? Is the structural argument (B algebraic in E,g,T implies nabla B involves only nabla E, nabla T, nabla g) sound?

(4) H_2 INEQUALITY (8.2): H' + c_0 D_2 <= C_0 Y + C_H(1+r^{-2})H + C_V||aE||_inf H, where D_2 = int eta^2 a|nabla Rm|^2, Y = int eta^2 a F_T^3. The metric-drift term C_V||aE||_inf H is new (Premise C2). Check that it correctly accounts for the metric variation (5.2) and volume-form (6.3) contributions proportional to |E|.

(5) SIGNED IBP (§7): The Hessian term 2 int eta^2 (nabla^2 a) B is integrated by parts; the cutoff cross term vanishes (a=da=0 on supp d eta); the main term is absorbed by Young with |nabla a|^2/a <= Cr^{-2}. No higher cutoff jet appears. Is this consistent with Step 34 eq 2.8 and A03 Step 57 eq 5.4?

(6) NORMALIZATION BOOKKEEPING: For a=1, E=g: partial_t|T|^2 = -4|T|^2 + 8|T|^2 = +4|T|^2, partial_t(d mu) = -4 d mu, so partial_t int|Rm|^2 d mu = 0 in dim 4. The +4|T|^2 is absorbed into CaF_T^3. Is this consistent with the n=4 conformal invariance of int|Rm|^2 d mu?

Read the proof note at Sessions/S0910A01/workspace/notes/step63_curvature_variation_index_proof.md and the A03 Step 57 tensor calculation at Sessions/S0910A03/workspace/notes/step57_H2_evolution_and_continuation_bridge.md. Report any errors in the tensor calculations, sign errors, missing terms, or structural gaps.

## Output

[No usable scientific output was produced by this independent branch.]
# Route assessment after Step 44

## Main scientific outcome

Agent4 reviewed the assembled first-exit/support/terminal chain for the restricted four-dimensional negative Ishida--LeBrun route.  The coefficient-weight repair is retained as a real analytic advance, but the proof must be read through A03 Step 45's corrected current-pair mechanism and through coefficient regularization as a construction of an exact degenerate flow.

The current restricted result is:

\[
M=(\#_{j=1}^mX_j)\#N,
\qquad m\in\{2,3\},\qquad b_+(N)=0,
\qquad q=4m-(2\chi+3\tau)(N)-A/3\ge0,
\]
with \(A=\sum_jc_1^2(X_j)\) and the Ishida--LeBrun monopole sign family.  The accumulated work supports a family-uniform negative gap \(\varepsilon_{\rm IL}>0\) excluding
\[
\|g^{-1}(\operatorname{Ric}_g+g)\|_{\infty,\mathrm{op}}<\varepsilon_{\rm IL}
\]
on this no-Einstein geography, after consolidating the corrected modules into a clean proof.

## Corrections made in this step

1. Wrote `workspace/notes/step44_preceptor_reading_first_exit_terminal_chain.md`, the durable review of the chain.
2. Patched `step43_H_WU_resolution_weighted_evolution.md`: the \(U_m\) step now uses the current pair \((U_m,C_{m+1})\), closing by the same-exponent estimate
\[
{d\over dt}(\|U_m\|_p^p+\|C_{m+1}\|_p^p)+c\int b|\nabla U_m|^2|U_m|^{p-2}
\le C(1+\|U_m\|_p^p+\|C_{m+1}\|_p^p),
\]
not previous-layer \(C_{m+1}\in L^{2p}\).
3. Patched `step43_H_DT_assessment.md`: H-DT now rests on coefficient regularization and smooth limit to the exact \(a=\chi^2\) flow, not on a broad smooth-tame perturbation assertion.
4. Patched `step41_corrected_restricted_defect_gap_theorem.md`:
   - support construction uses strict \(\chi,\eta\) buffers and the direct maximal-function threshold;
   - the unnormalized energy input uses a smaller threshold rather than relying on shrinking \(r\) alone;
   - terminal cohomology notation separates exceptional classes \(e_\ell\) from Einstein defect \(E\);
   - terminal deficit is \(D_{\rm av}=J-q-(2/3)\sum(e_\ell^+)^2\);
   - terminal pullback density is \(\Phi=|E|^2+(s+4)^2+(s+8\sqrt6|W^+|)^2+\mathcal G\), so the Einstein limit is supported by local defect vanishing.
5. Ran existing verification scripts:
   - `step43_weighted_evolution_verify.py`: 54/54 structural checks;
   - A03 `verify_step45_weight_partitions.py`: 110/110 scalar/partition checks;
   - `step34_integrated_potential_q3_verify.py`: 48/48 algebra/scaling checks;
   - `step36_platform_Q_verify.py`: 20/20 dependency/weight checks;
   - `step28_terminal_pullback_constants.py`: terminal constants and pullback-selection implication verified.
6. TTCS independently reviewed the assembled chain and agreed that the restricted family-uniform negative gap follows after the above corrections, using Step35's curvature/defect signed-Hessian tensor calculations as established modules.  TTCS also emphasized that Step45's curve/weighted ledger does not automatically replace the defect ledger used in \(J_6\) and global \(Q\); those remain supplied by Steps 34--36.

## Present status of the restricted theorem

The proof architecture is now coherent on one exact degenerate flow:

1. coefficient regularization constructs an exact \(a=\chi^2\) flow on a common per-datum interval;
2. exact-flow support localization supplies stationary complement and disjoint summation;
3. support selection keeps \(A\)-proportional plateau volume using \(\operatorname{Vol}/A\to32\pi^2/9\);
4. first-exit estimates propagate \(K_2^\eta\), \(Y\), \(J_6\), Moser endpoints, and global \(Q\);
5. terminal recalibration uses \(q\ge0\) and the sign-averaged monopole family;
6. Liouville--Rauch averaging and strong finite-\(W^{2,p}\) convergence produce the forbidden Derdziński germ.

The next Constructor step should consolidate this into a clean theorem note, preferably `workspace/notes/step45_consolidated_IL_negative_gap_proof.md`, using the corrected modules rather than the older Step 41/43 language.  The note should keep all assumptions and constants explicit, avoid importing regularized-flow localization before the exact limit, and cite the exact supporting files.

## Relation to the full Yau 26 goal

This remains a restricted four-dimensional negative-sign theorem.  It does not settle positive Ricci pinching, arbitrary four-manifold topology, dimensions \(n\ge5\), dimension-only constants for the full proposition, or Lean formalization.  A02 message #367 corrected the positive noncollapsed bi-Kähler stress example: the product example is a finite exceptional locus, not a reason to abandon first-order positive noncollapsed work.  After the restricted negative theorem is consolidated, the research should return to broader routes with this result as a reliable exclusion tool rather than as an endpoint.
# Step 20 consolidated mathematical status

The cutoff-flow route for the four-dimensional negative critical Ishida–LeBrun laboratory now has a transition-compatible zero-order structure.

## Established in this step

1. **Weighted curvature moments.** For
   \[
   H_q=\int\eta^2a^{q-2}F^q,\quad F=(1+|\mathrm{Rm}|^2)^{1/2},\quad a=\chi^2,
   \]
   the natural Sobolev variable is \(\eta a^{(q-1)/2}F^{q/2}\). Tensor testing and one integration by parts remove Hessian-\(a\), leaving \(|da|^2/a=4|d\chi|^2\), localization terms, and the weighted reaction \(\int a^{q-1}F^{q+1}\). The curvature layer closes through \(\nabla E=\operatorname{contr}(\nabla\mathrm{Rm})\).

2. **Transition cubic potential.** Fixed \(q=2\) and \(q=3\) estimates yield, conditionally on the provisional local Sobolev/energy geometry,
   \[
   A^4\int\eta^2aF^3(t)\le C\gamma^3/t,
   \qquad \gamma=A^2\|F\|_2\lesssim r^2\sqrt{1+K_0}.
   \]
   This avoids the invalid conversion to an unweighted Li potential.

3. **Compatible defect moments.** The correct hierarchy is
   \[
   J_m=\int\eta^2a^{m-2}|E|^m,
   \]
   not the weaker \(\int|aE|^m\). Initial pinching supplies \(J_6\). The exact interpolation
   \[
   \int a^{m-1}F|E|^m
   \le\varepsilon X_m+C\varepsilon^{-2}A^4H_3J_m
   \]
   follows from \(J_{3m/2}\le(J_mJ_{2m})^{1/2}\).

4. **High-exponent product.** For \(q_{j+1}=3q_j/2\), all polynomial exponent losses and nested-cutoff factors have convergent products. The endpoint scaling is \(|a\mathrm{Rm}|\sim\gamma/t\) from \(q_0=2\), and \(|aE|\sim\delta(r^2/t)^{1/3}\) from \(q_0=6\), provided the exact nested time-space energy recurrence is established.

5. **Triangular unweighted defect energy.** Global calibration requires local inequalities
   \[
   Q_\alpha'\le Cr^{-2}\sum_{\beta\sim\alpha}Q_\beta.
   \]
   An additive \(\varepsilon\int a|\nabla\mathrm{Rm}|^2\) error is not acceptable because it can be order \(\varepsilon A\).

6. **Derivative-free first-exit.** Quantitative pointwise \(|\chi\nabla(aE)|\) is not required for the zero-order first-exit. Metric equivalence controls fixed cutoff-gradient norms, fixed-domain Sobolev constants, volumes, and buffered containment. Integrable \(|aE|\) improves metric equivalence directly. Connection/Hessian estimates can be generated qualitatively inside a smooth-extension theorem.

7. **Whitney corrections.** Effective time \(a_0t\) and radius \(cr\chi_0\) are compatible uniformly over cutoff levels, but \(|a-a_0|/a_0=O(c)\), not \(O(c^2)\). A support-global average does not imply local Whitney smallness; centered buffered local budgets are required.

## Still to prove

- Derive the exact nested time-space recurrence, with time cutoffs, finite-neighbor outer terms, evolving measure, and a regularization at \(a=0\), from the tensor inequalities. The exponent product itself is no longer the issue.
- Prove the triangular support-summed \(Q\) inequality in the same finite-neighbor system.
- Adapt Wang's smooth-extension induction from \(\partial_tg=-2a\operatorname{Ric}\) to \(\partial_tg=-2a(\operatorname{Ric}+g)\). Retrieved sources did not supply this spatially cutoff normalized theorem directly. Fei He explicitly notes that analogous results hold for globally normalized Ricci flow with the defect \(\operatorname{Ric}-\lambda g\), which supports the structure but does not replace the needed written adaptation.
- Only after these tasks can the flow supply a bounded-curvature positive-volume plateau for the exponential-chart/calibrated-germ contradiction.

No four-dimensional gap theorem, no complete branch result, no full proof or disproof of Yau Problem 26, and no Lean formalization has been obtained.

Primary evidence: `step20_weighted_wang_hierarchy_and_whitney_correction.md`; scripts `verify_step20_weighted_moment_hierarchy.py`, `verify_step20_whitney_bernstein_weights.py`, `verify_step20_moser_recurrence_products.py`; TTCS integrations `step20_ttcs01_*` and `step20_ttcs02_*`.

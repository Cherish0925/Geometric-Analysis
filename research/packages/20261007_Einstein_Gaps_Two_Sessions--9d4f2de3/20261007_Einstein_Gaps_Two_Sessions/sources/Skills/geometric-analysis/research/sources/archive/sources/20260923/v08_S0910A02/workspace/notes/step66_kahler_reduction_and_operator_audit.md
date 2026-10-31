# Step 66: Kähler reduction check, solver-agnostic operator audit, and EH ODE constraint

Session `S0910A02`, Agent3/Actuator, Execute.

## Purpose

The Step-65 metric export ran into two named obstacles: bolt regularity and ambient quadratic-jet matching for Biquard's correction tensor `h` on Eguchi--Hanson. The Step-66 Strategist proposed three changes:

1. decouple the operator-norm certificate from BVP convergence by directly auditing the Ricci endomorphism of any assembled metric/profile;
2. decouple existence-flow experiments from the refined small-defect export: naive starts are legitimate flow starts even though their defect is not small;
3. verify whether a Kähler-potential identity reduces the tensor BVP to one scalar radial equation.

This note records the executed checks. Main scripts/data:

- `workspace/scripts/step66_kahler_symbolic.py` -> `workspace/data/step66_kahler_symbolic.json` (first-pass symbolic check; contains a deliberate correction path)
- `workspace/scripts/step66_kahler_substitute_step65.py` -> `workspace/data/step66_kahler_substitute_step65.json` (decisive exact substitution into Step-65 full-4D formulas)
- `workspace/scripts/step66_operator_audit_profiles.py` -> `workspace/data/step66_operator_audit_profiles.json` (solver-agnostic first-order Ricci-endomorphism audit of radial profiles)
- `workspace/scripts/step66_ode_matrix_extract.py` -> `workspace/data/step66_ode_matrix_extract.json`
- `workspace/scripts/step66_ode_compatibility.py` -> `workspace/data/step66_ode_compatibility.json`

## 1. Kähler-potential check: scalar identity true, naive global shortcut false

Use the EH convention from Step 65:
\[
 g_{EH}=W^{-1}dr^2+\frac{r^2}{4}(\sigma_1^2+\sigma_2^2+W\sigma_3^2),\qquad W=1-r^{-4},
\]
with orthonormal coframe
\[
 e_0=W^{-1/2}dr,\quad e_1=\frac r2\sigma_1,\quad e_2=\frac r2\sigma_2,\quad e_3=\frac{r\sqrt W}{2}\sigma_3,
\]
and Kähler form \(\omega=e_0\wedge e_3+e_1\wedge e_2\).

For a radial scalar \(\phi\), writing \(q=\phi'\), the Kähler-type tensor has coefficients
\[
 h_\phi=i\partial\bar\partial\phi
 = A_\phi(e_0^2+e_3^2)+B_\phi(e_1^2+e_2^2),
\]
where in the Step-65 normalization
\[
 A_\phi={r(r^4-1)q'+(r^4+3)q\over r^5},\qquad
 B_\phi={2(r^4-1)q\over r^5}.
\]

The Strategist's proposed diagnostic `i∂∂bar(r²)=2ω` is **false** in these conventions. Direct calculation gives
\[
 i\partial\bar\partial(r^2)=(4+4r^{-4})e_0\wedge e_3+(4-4r^{-4})e_1\wedge e_2,
\]
so the anti-self-dual discrepancy is \(8r^{-4}\). This is the same obstruction channel Step 65 saw when `h=c r² g` failed the full linearized Ricci equation.

There is nevertheless an exact radial Kähler potential on the punctured end:
\[
 q=\phi'={2r^5\over r^4-1},\qquad
\phi=r^2+{1\over2}\log\frac{r^2-1}{r^2+1},
\]
for which \(A_\phi=B_\phi=4\), i.e. \(i\partial\bar\partial\phi=4\omega\). The logarithm is singular at the bolt. This is not a harmless coordinate singularity: it encodes the nontrivial Kähler class/bolt cohomology.

The decisive exact check used Step-65's full four-dimensional linearized Ricci formulas (including angular Christoffels) and substituted the above Kähler variation. The exact identity returned by `step66_kahler_substitute_step65.py` is
\[
 d\operatorname{Ric}_{EH}(h_\phi)=-\frac12\, i\partial\bar\partial\bigl(A_\phi+B_\phi\bigr)
\]
(in coordinate components: factor `-1/2` was the unique exact match among tested factors). Thus the scalar Kähler reduction is locally correct.

But it does **not** collapse Biquard's global smooth BVP to one smooth scalar equation. To solve
\[
 d\operatorname{Ric}(h)=\Lambda g_{EH}
\]
inside the pure Kähler-potential ansatz would require a scalar \(S=A_\phi+B_\phi\) satisfying
\[
 -\tfrac12 i\partial\bar\partial S=\Lambda\omega.
\]
Since the potential for \(\omega\) is logarithmically singular at the bolt, a smooth global scalar cannot represent this cohomology class. This is precisely why Biquard Lemma 4.1 solves
\[
 d_{EH}\operatorname{Ric}(h)=\Lambda e_h+\frac13\sum_j\lambda_j o_j,
\]
with compactly supported obstruction tensors \(o_j\); the obstruction term represents the bolt/core cohomology not captured by a smooth scalar potential.

Interpretation: the scalar identity is useful as a decomposition and audit tool, not as a complete global closed-form `h`.

## 2. Solver-agnostic first-order operator audit

`step66_operator_audit_profiles.py` defines a reusable radial-profile audit. Given any diagonal U(2)-invariant correction
\[
 h=f_1(r)e_0^2+f_2(r)(e_1^2+e_2^2)+f_3(r)e_3^2,
\]
it uses Step-65's full-4D linearized Ricci formulas to compute frame components of
\[
 d\operatorname{Ric}_{EH}(h)-\Lambda g_{EH}
\]
and records the sup operator defect over a radial grid. This is a solver-independent first-order certificate interface: BVP convergence is not the certificate; direct Ricci-endomorphism audit is.

The profile results for \(\Lambda=1\) were:

- `raw` (`h=0`): max defect = 1, median = 1. This re-confirms the raw EH insert has order-one core defect.
- `r2metric` (`h=r²g`): max defect ≈ 8.92, sample at r=2 has frame dRic ≈ (-6.125,-5.875,-6.125). This catches the Lichnerowicz-vs-full-linearized-Ricci trap.
- `kpot_parallel` (`h=4g`, generated by the singular end potential with constant Laplacian): max defect = 1. Parallel scaling has zero linearized Ricci and does not address the source.
- `scalar_cutoff` profiles solving the local scalar equation away from the bolt: at r=2 frame dRic ≈ (0.99999,0.99999,0.99992), and the far-region median defect is ≈3e-6, but the all-region maximum is O(5--12) depending on cutoff width, and a remaining far-region maximum ≈1.14 persists near the artificial truncation. This is exactly the expected picture: the scalar potential kills the source away from the bolt but leaves a compact core/transition defect where smooth cutoff replaces the singular cohomological potential.

This validates the Strategist's certification separation. Future profiles (from a real Biquard/Fredholm solve, numerical BVP, or finite-element output) can be audited by the same interface. The raw profile is not near-pinched; a divergence result from raw flow cannot refute P4+. But raw starts remain legitimate for existence-oriented Einstein-DeTurck/variational searches.

## 3. ODE system correction: rank-two plus compatibility, not free 2+1

Step 65 described the EH correction equation as “two second-order plus one first-order constraint.” Step 66 sharpened this by matrix extraction.

Using the Step-65 full-4D formulas and converting to frame components, the algebraic system for the unknown highest derivatives \((f_1',f_2'',f_3'')\) has
\[
\operatorname{rank}M=2,
\qquad \operatorname{rank}(M|b)=3
\]
for generic lower-order data. A left-null vector is
\[
(-1,2,1),
\]
so the compatibility constraint is
\[
\Lambda r^6-3f_1r^4-f_1+2f_2r^4+2f_2+2f_2'r^5+f_3r^4-f_3+f_3'r^5-f_3'r=0.
\]
Then the `(11)` and `(33)` equations solve for \(f_2''\) and \(f_3''\) in terms of \(f_1'\) and lower-order data, but \(f_1'\) must be chosen to keep the compatibility constraint propagated. This explains the numerical resistance in Step 65: arbitrary asymptotic gauge constants or naive bolt Neumann data will generally leave the constraint manifold.

Practical consequence: if the refined `h` solve is continued, implement it as a constrained first-order/second-order system, not as an unconstrained BVP. Bolt regularity and ambient-H matching are boundary conditions **on the constraint manifold**. The singular denominators in the raw formulas near r=1 are expected and should be treated in a proper-distance/Frobenius coordinate.

## 4. Consequence for the balanced-row experiment

The flow experiment should no longer be serialized behind the refined `h` export.

- Refutation direction: still requires small \(\delta\), hence a genuine Biquard correction `h` or equivalent audited profile. The current scalar cutoff is only a diagnostic; its O(1) compact defect cannot support a P4+ refutation.
- Existence direction: does **not** require small defect. The naive glued metric is a smooth legitimate flow/variational start. The del Pezzo `r=0` row is the necessary control because a positive KE metric is known there; if a symmetry-respecting flow cannot find the control, its behavior on the balanced rows is uninterpretable.

A Codex-loop proposal has been prepared to prototype the decoupled naive-start flow/control pipeline. It should treat the operator-norm audit interface above as an independent certificate, not as part of convergence.

No branch of Yau--26 is proved or refuted by these computations. They correct the export route and produce reproducible diagnostic/audit infrastructure.

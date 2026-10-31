# Step 88 route map: minimal separators remove nonreflection as an OT escape

## New established extension

The Step 87 massive-resolvent ceiling is independent of reflection. On a complete
free-\(T^2\), orthogonally transitive metric whose quotient is a cylinder with two
exact outward-expanding ends, the auxiliary metric
\(\widehat\gamma=\rho^2\gamma_B\) is complete and proper and the primitive
essential loop class is coercive. A shortest embedded essential
\(\widehat\gamma\)-geodesic lifts to an invariant minimal \(T^3\).

Its exact averaged Gauss identity is
\[
\langle e_s\rangle
=12-2\langle \operatorname{tr}E-2E(\nu,\nu)\rangle
 +2\langle|\mathrm{II}|^2\rangle+\langle h^2\rangle,
\]
so \(\sup e\ge12-8\delta\). Combining with Step 87 gives nonexistence for
\(\delta<0.246249763690668\ldots\), now without reflection. Two expanding end
orientations, exact constant-orbit-map end neighborhoods, free action, OT, and
smooth complete attachment remain explicit hypotheses.

Main file: `workspace/notes/step88_reflection_free_minimal_separator.md`.

## Strategic consequence

A nonreflected complete OT connector is no longer a distinct route. The real next
symmetry-class question is connection twist (failure of OT), not another choice of
center or foliation. No averaging argument from arbitrary metrics to symmetric
metrics is available, and none should be assumed.

## Next mathematical object: variable-fibre Abelian reduction

For
\[
g=\gamma+G_{ab}(d\xi^a+A^a)(d\xi^b+A^b),\qquad F^a=dA^a,
\]
derive the full variable-\(G\) Ricci blocks in the conventions already fixed for
\(G=e^\sigma M\). The next work should establish, by direct tensor computation and
independent checking:

1. translate Liu's exact mixed Ricci/twist-scalar conservation formula
   \cite{liutoric} into the present \((\rho,M,F)\) normalization, then derive its
   forced small-defect version;
2. the coefficients and signs of connection-curvature stress in the area, base,
   and traceless orbit equations;
3. use the already twist-stable minimal-separator identity: restriction of the
   connection to a one-dimensional base curve is locally gauge-trivial, so the
   floor remains \(12-8\delta\); quantify any additional mixed contribution to
   \(|\mathrm{II}|^2\);
4. derive the modified weighted Bochner identity and whether charge/area coupling controls
   the adverse tension-square and divergence terms;
5. exploit the now source-supported distinction: an exact OT open end forces the
   exact constant twist scalars to vanish globally, whereas merely asymptotic ends
   can have decaying physical curvature with nonzero conserved twist.

This immediately narrows the twist route: with the exact attachments used in the
Step 88 theorem, exact Einstein twist is absent, so only approximate forcing or a
weaker asymptotic attachment can exploit it. The TTCS generator offers plausible
base/vertical formulas and a bounded-twist theorem target, but those coefficients
are not yet established for variable
\(G\). Liu's primary source now establishes constancy of the exact twist scalars
\cite{liutoric}; it does not by itself settle the remaining stress coefficients in
our normalization. Use `trace/ttcs/results/step88_ttcs01_generator1_integration.md`
as a hypothesis source, not as proof.

## Complementary routes and scope

* The diffuse non-OT/non-warped \(S^3\)-neck mechanism on \(N\#N\) remains outside
  all torus-reduction results. A02 message #638 emphasizes that local barriers do
  not rule out volume-scale spreading.
* The BCG--Chern--Gauss--Bonnet inequality is a necessary lower defect scale, not a
  construction prescription.
* A02's orbifold+ALE result concerns its volume-convergent construction class; it
  is not a theorem about every near-pinched manifold or every no-Einstein
  mechanism.
* The positive branch remains independent. Peer messages #633/#640/#645/#648
  corrected successive product-orbifold interpretations. The rank-one curvature
  target and odd gauge invariance are valuable; the current target is still the
  physical Ozuch/Biquard response on the allowed two-dimensional kernel plane.
  It requires solving for the singular field and extracting its regular second
  jet, retaining all pair/self/complement and frame/projector terms, and improving
  the remainder below order \(t^3\). The reported mixed-row coefficient is not yet
  an Einstein obstruction theorem.
* None of these restricted advances solves the full sign-unrestricted,
  all-dimensional Yau Problem 26 or begins its final Lean formalization.

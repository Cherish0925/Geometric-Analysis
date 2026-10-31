# Yau26: Uniform Rigidity and Near-Einstein Stability

## Highest research objective

Work toward an original, rigorous, independently checkable resolution of Yau Problem 26. Use the following working formulation, retaining its distinction from later commentary on the historical problem:

For every integer \(n\ge2\), do there exist real constants \(c_n<C_n\), depending only on \(n\), such that every closed, connected, smooth real \(n\)-manifold \(M\) with a smooth Riemannian metric \(g\) satisfying
\[
c_ng\le\operatorname{Ric}_g\le C_ng
\]
admits a smooth Riemannian metric \(h\) with
\[
\operatorname{Ric}_h=\lambda h,\qquad \lambda\in\mathbb R?
\]
The inequalities are pointwise inequalities of quadratic forms. The conclusion concerns the same smooth manifold, without requiring proximity to \(g\), preservation of its symmetries, or agreement of Einstein signs.

Write
\[
\delta_\sigma(g)=\|g^{-1}\operatorname{Ric}_g-\sigma I\|_{L^\infty,\mathrm{op}},
\qquad e_\sigma(M)=\inf_g\delta_\sigma(g),\quad \sigma=\pm1.
\]
In each dimension the interval statement is equivalent to a dimension-uniform sufficient small-defect threshold for at least one sign. A full affirmative solution must cover every dimension and the entire stated manifold class. A full disproof needs failure of both sign branches in one fixed dimension; the branches may use different manifolds or sequences of manifolds. Every counterexample must exclude Einstein metrics of all signs on the same smooth objects carrying the approximate inputs.

Seek substantial new theorems, constructions, and mechanisms toward this objective. A complete intermediate theorem is valuable progress, while the highest objective retains its full scope.

The three research lines are complementary ways to investigate the original problem, not an established complete solution or fixed divisions between proof and counterexample. Prioritize work that broadens applicable geometry, connects approximate inputs with global Einstein existence or nonexistence, or identifies a decisive obstruction to that connection. Quantitative improvements should explain which mathematical conclusion they strengthen or make attainable.

## Inherit the research and begin mathematical work

Read `Skills/qiushi-yau26/SKILL.md`, then `research/20260916.md` and `references/research-map.md` within that Skill. All subsequent `research/` and `references/` paths are relative to `Skills/qiushi-yau26/`. Follow the relevant proof chains in the English papers and the detailed earlier manuscripts, rather than treating their summaries as proofs. The package incorporates both the three previous Sessions and subsequent web-based research.

Understand the arguments needed for the current problem and check their critical dependencies against primary sources. Correct a concrete error where found while preserving unaffected work. Compare prospective new results with the closest available literature; neither a familiar technique nor a new name decides originality.

Formulate a consequential mathematical question and start proving, constructing, estimating, or testing it. Use focused literature work and calculations to resolve actual uncertainties. Develop new objects, representations, invariants, analytic spaces, constructions, or proof methods when useful; the existing routes are starting points, not restrictions.

## Initial emphasis: rigidity and near-Einstein stability

Your starting papers are `research/20260916_uniform_gap.tex` and `research/20260916_rigidity.tex`, with the related spinor, Weyl, and flow arguments located by the research map.

The existing manuscript develops an exact-Einstein uniform gap under the monopole input \(\mathrm{MP}(A)\) and relative Euler bound \(\chi(M)\le LA\), followed by its application to general-type blow-ups. Its mechanism uses an average curvature budget, fixed-scale selection, local unfolding, defect transfer, and a forbidden Einstein germ. Understand that mechanism and its source assumptions. Its exact-Einstein proof is separate from the unfinished extension to arbitrarily collapsed approximate metrics.

The central continuation question is how much topological near-equality can constrain the approximate equation. For the blow-up family with \(X\) a closed minimal complex surface of general type, \(b_+(X)>1\), and \(k\ge0\),
\[
M=X\#k\overline{\mathbb{CP}}^{\,2},\qquad A=c_1^2(X)>0,
\]
a concrete target is to prove or disprove a uniform bound
\[
\delta_-(g)^2+\left(\frac13-\frac{k}{A}\right)_+\ge c_*>0
\qquad\text{for }\delta_-(g)\le\tfrac14,
\]
with constants independent of \(X,k\), diameter, volume ratios, and maximum full curvature. A general theorem may instead declare explicit dependence on a fixed relative Euler budget \(L\).

Possible approaches include quantitative near-equality estimates, controlled local developments retaining small average defect, weak testing of sourced Weyl/Hodge equations, and local smoothing with adequate time and support estimates. Select, combine, replace, or extend these approaches according to the mathematical obstruction. The proposed (SC) statement is one sufficient route, not a mandatory theorem to prove.

Keep the exact and approximate regularity hypotheses distinct. A proof that uses derivatives of the Ricci defect must obtain their required control or work in a justified weak formulation. If smoothing is used, the existence time, transfer of defect, and relation to the original manifold belong to that argument.

Seek a stronger rigidity theorem, a useful generalization, or a genuine geometric escape mechanism. A model defeating a sufficient local argument does not alone refute Yau26. Conversely, a new family of small-defect inputs may give the construction and global Sessions a concrete target. Maintain the existing exact-gap result as a separate manuscript argument while investigating these new questions.

## Independent research and collaboration

This is an initial research emphasis, not a permanent role. Coordinate with the other Sessions around actual objects and mathematical dependencies. Share the exact statement, assumptions, normalization, key argument or calculation, and a readable artifact location. Ask concrete questions that a collaborator can advance. Combine compatible results on the same objects, and retain independent judgments when evidence disagrees.

Keep a sustained current question while it remains productive; change direction when new mathematics warrants it. Alternatives remain available without requiring equal effort for every route. Investigate whether a failed approach rules out only its ansatz or reveals a more general mechanism.

Use the available mathematical tools, shell, Skills, and MCP interfaces through their normal contracts. Choose analytic reasoning, symbolic computation, numerical exploration, rigorous computation, or formal proof according to the problem. Work in this Session's workspace and exchange results through the authorized Session Group interface; do not overwrite other Sessions or the shared research baseline.

Record material progress as clear mathematical English and editable LaTeX: precise statements, full derivations, assumptions and constant dependencies, relevant prior work, and reproducible calculations where used. Keep the current question, new finding, unresolved step, and next useful action easy to recover. Numerical evidence, conditional implications, and established results retain their actual scopes. Develop papers as results mature; a completed document is not by itself completion of Yau26.

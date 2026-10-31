# Yau26: Global Einstein Existence on the Same Smooth Manifold

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

## Initial emphasis: Einstein existence on a specified smooth object

Start with `research/20260916_global.tex`, then the construction and rigidity arguments needed for the selected object.

Your central question is whether the same smooth manifold can support arbitrarily small pointwise Ricci defect while supporting no Einstein metric of any sign, or whether its approximate geometry can instead be connected to a genuine Einstein metric. Positive existence results and nonexistence results are both relevant outcomes.

Compare the available objects briefly, then select one explicit current problem and pursue its decisive missing implication. Keep other objects as alternatives and comparison models; the selection can change when new evidence warrants it. A fixed object gives focus, but sequences of different manifolds in a fixed dimension are also admissible.

The existing starting points have different open questions:

- On \(E_D\) and the specified finite covers, approximate inputs and global variational values are available. Investigate full-curvature-energy attainment, general Einstein structure, or another global mechanism applying to arbitrary metrics. Nonattainment of the scalar, Ricci, or volume extrema does not settle full-curvature attainment. An unknown Einstein metric need not respect the bundle projection or any chosen complex structure; a structural implication must be proved.
- In the precise extended-graph category with an all-sign nonexistence theorem, investigate a complete small-defect metric with the full Ricci equations, constraints, shared endpoint data, and global topology simultaneously satisfied. Alternatively, derive a genuine global obstruction to such approximation. Local cores and separately constructed tails are not yet a common two-ended solution.
- On fixed marked \(A_1\) resolutions, identify the actual smooth type before testing global Einstein existence. Obstruction near one orbifold limit is not nonexistence on the entire metric space. The specified BCGP and Campedelli smoothings already provide positive existence examples through changed complex structures; they are starting points for other existence questions, not non-Einstein counterexamples.

Use variational identities, topology, harmonic methods, algebraic deformation, geometric limits, or new constructions as the object requires. The existing connected-sum pinching gap and model-class connector results may eliminate or reshape a candidate; preserve their precise dependence on topology and their domains.

Seek a substantial global theorem or construction that advances the actual existence decision. Make every new necessary condition act on the claimed class of arbitrary Einstein metrics, and every purported sufficient construction close on its declared smooth object. Coordinate with the other Sessions when a new topological obstruction calls for inputs, or a new approximate family calls for an existence decision.

The positive branch and higher-dimensional mechanisms remain available. A full affirmative resolution must also address dimensions and manifold classes not covered by four-dimensional oriented tools; a fixed-dimension two-sign disproof does not require solving all higher dimensions first.

## Independent research and collaboration

This is an initial research emphasis, not a permanent role. Coordinate with the other Sessions around actual objects and mathematical dependencies. Share the exact statement, assumptions, normalization, key argument or calculation, and a readable artifact location. Ask concrete questions that a collaborator can advance. Combine compatible results on the same objects, and retain independent judgments when evidence disagrees.

Keep a sustained current question while it remains productive; change direction when new mathematics warrants it. Alternatives remain available without requiring equal effort for every route. Investigate whether a failed approach rules out only its ansatz or reveals a more general mechanism.

Use the available mathematical tools, shell, Skills, and MCP interfaces through their normal contracts. Choose analytic reasoning, symbolic computation, numerical exploration, rigorous computation, or formal proof according to the problem. Work in this Session's workspace and exchange results through the authorized Session Group interface; do not overwrite other Sessions or the shared research baseline.

Record material progress as clear mathematical English and editable LaTeX: precise statements, full derivations, assumptions and constant dependencies, relevant prior work, and reproducible calculations where used. Keep the current question, new finding, unresolved step, and next useful action easy to recover. Numerical evidence, conditional implications, and established results retain their actual scopes. Develop papers as results mature; a completed document is not by itself completion of Yau26.

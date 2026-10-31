# Yau26: Pointwise Near-Einstein Constructions

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

## Initial emphasis: pointwise constructions and exact repair

Start with `research/20260916_construction.tex` and the relevant chapters of `research/20260912.tex`; use `research/20260916_global.tex` to identify which smooth objects would make a new construction consequential.

There are two distinct starting mechanisms:

- Fixed marked \(A_1\) resolutions: an Eguchi-Hanson core correction, common radial gauge, and logarithmic interpolation of quadratic Weyl jets yield the stated pointwise defect and degeneration limits.
- Fixed Dehn-twist surface bundles \(E_D\): slow interpolation, balanced double collars, and subsequent tensor corrections yield different approximation orders. The original fixed-fibre family and the corrected families have different geometric and volume properties.

Understand both sufficiently to choose a present construction problem; they need not advance in lockstep. Coordinate the choice of smooth object with the global Session, while keeping both mechanisms available.

Pursue a new construction theorem, a meaningful extension of its applicable topology or singularities, a sharp estimate in a precisely stated class, or an exact existence result. Useful questions include which markings and filling data support pointwise approximation; how monodromy and degeneration can be varied; and which freedoms reduce Ricci error while retaining the desired global topology. New mechanisms beyond these two families are welcome.

The controlling quantity is the global, unweighted Ricci-endomorphism supremum. Write the actual closed smooth object, transitions, positive-definiteness domain, and errors on the core, transition, and exterior regions. State uniformity across any newly varying data. For the spherical \(A_1\) application, compare the pointwise endpoint with Ozuch's finite-\(L^p\) and exact-desingularization results; a logarithmic cutoff alone is not the claimed novelty.

For exact repair, place residual, inverse or approximate inverse, nonlinear estimate, admissible radius, and kernel/cokernel equations in the same spaces and scales. Maximum-norm control cannot be inferred from an \(L^2\) spectral gap alone. A leading projected obstruction needs the remaining terms controlled at its actual order.

A construction theorem does not require global Einstein nonexistence to be a complete result. To supply a branch counterexample, however, its actual smooth manifold must also have an all-sign nonexistence theorem. Restricted conformal or gluing obstructions do not supply that theorem. Check the topology before pursuing it: some standard spherical fillings and specified algebraic resolutions already admit Einstein metrics elsewhere in their metric spaces.

Preserve the full construction arguments and develop new applications or theorems whose mathematical gain is explicit.

## Independent research and collaboration

This is an initial research emphasis, not a permanent role. Coordinate with the other Sessions around actual objects and mathematical dependencies. Share the exact statement, assumptions, normalization, key argument or calculation, and a readable artifact location. Ask concrete questions that a collaborator can advance. Combine compatible results on the same objects, and retain independent judgments when evidence disagrees.

Keep a sustained current question while it remains productive; change direction when new mathematics warrants it. Alternatives remain available without requiring equal effort for every route. Investigate whether a failed approach rules out only its ansatz or reveals a more general mechanism.

Use the available mathematical tools, shell, Skills, and MCP interfaces through their normal contracts. Choose analytic reasoning, symbolic computation, numerical exploration, rigorous computation, or formal proof according to the problem. Work in this Session's workspace and exchange results through the authorized Session Group interface; do not overwrite other Sessions or the shared research baseline.

Record material progress as clear mathematical English and editable LaTeX: precise statements, full derivations, assumptions and constant dependencies, relevant prior work, and reproducible calculations where used. Keep the current question, new finding, unresolved step, and next useful action easy to recover. Numerical evidence, conditional implications, and established results retain their actual scopes. Develop papers as results mature; a completed document is not by itself completion of Yau26.

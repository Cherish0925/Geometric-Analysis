# O11 sharp calibration: what a coupled metric–field variation can and cannot prove

2026-09-30. Continuation E. This is an unsuccessful closure attempt with a precise reason for failure. It proves no improved lower bound for O11 and constructs no cheaper metric. It is deliberately short: the conclusions below should prevent further iterations of the same formal variation from being counted as progress.

## 1. The quantity that must change

On the original balanced family let
\[
P(g)=\int|\operatorname{Ric}^{\circ}|^2,
\qquad Q=k+4\ell.
\]
The target lower bound is \(P\ge8\pi^2Q-o(Q)\). Continuation D gave the exact simultaneous-field identity
\[
P(g)-8\pi^2Q=\mathcal A(g,\boldsymbol\Phi)
 -4\mathbb E_\epsilon K_\epsilon(g,\Phi_\epsilon),
\qquad\mathcal A\ge0.\tag{1}
\]
Here each \(\Phi_\epsilon\) is an actual ordinary SW solution for its supplied sign class. The definitions and normalization of all summands are retained from D/O11_Global_Sharp.md.

## 2. An exact obstruction to gaining information by field selection

For a fixed metric, define the set \(\mathscr S(g)\) of choices of one actual solution for each supplied class. Equation (1) implies, for every \(\boldsymbol\Phi\in\mathscr S(g)\),
\[
4\mathbb E K_\epsilon-\mathcal A
=8\pi^2Q-P(g).\tag{2}
\]
In particular the left side is independent of the choice of solutions. Minimizing the kinetic term among solutions or selecting another solution in a moduli space cannot improve this particular difference: its positive terms change by exactly the compensating amount. With the full equally weighted sign cube retained, the supremum and infimum of the left side over \(\mathscr S(g)\) coincide. Changing the supplied class set or its weights requires a new decomposition and is not covered by this assertion.

This is not a no-go theorem for simultaneous-field analysis. New relations between the fields, such as a coercive estimate not used in (1), could still supply the desired inequality. It says that selection by itself contributes no further inequality.

## 3. Coupled metric–SW differentiation returns the old metric variation

Suppose, for the sake of testing this approach, that a sufficiently smooth branch \((g_t,\boldsymbol\Phi_t)\) of actual solutions is available. The original supply theorem does not by itself guarantee such a branch through an arbitrary solution; the following calculation is conditional on it. Differentiating (1) gives exactly
\[
\frac{d}{dt}(\mathcal A-4\mathbb E K_\epsilon)
=DP(g_t)[\dot g_t].\tag{3}
\]
The second and all higher variations likewise agree with those of \(P\), because \(8\pi^2Q\) is metric independent. The SW-branch derivative does not leave an extra signed term that pays the topological constant.

Thus an already selected near-stationary, near-stable sequence can yield derivative estimates for the difference in (1), but this differentiation alone gives no estimate for its value. This remains true even if a smooth field branch exists and all derivative norms are controlled. Writing the functional in actual-field coordinates cannot recover a lost additive constant from local first and second derivatives.

For the existing threshold functional
\[
F_\gamma=P-\gamma S,\qquad
S=\int s^2,\qquad \gamma=O(h),
\]
the precise statement is
\[
\frac{d}{dt}(\mathcal A-4\mathbb E K_\epsilon-\gamma S)
=DF_\gamma[\dot g_t].
\]
For the already admissible adaptive tests with \(DS[H]=O(Q)\), the \(\gamma DS\) correction is \(o(Q)\). No new topological term appears in this correction.

## 4. Why the coupled energy functional does not repair this automatically

The SW equations are the zero set of an appropriate sum-of-squares functional with a topological correction. Its value and first variation vanish on an exact solution when the metric and fields vary through solutions. Adding such a zero functional to \(P\), then differentiating along the same solution branch, again gives \(DP\). A useful argument would need an independently positive off-branch second variation, a proven comparison metric, or a new global restriction on the attainable curvature data. None of those follows merely from the equations being variational.

In particular it is not legitimate to differentiate a curvature inequality with an \(O(Q)\) unsaturated remainder as though equality held at a \(P\)-near-minimizer. Near-minimality of \(P\) is not saturation of the SW scalar inequality.

## 5. Relation to the classical optimal-curvature problem

The primary source checked this turn is Claude LeBrun, *Curvature Functionals, Optimal Metrics, and the Differential Topology of 4-Manifolds*, arXiv:math/0404251, https://arxiv.org/pdf/math/0404251.

Equation (6), printed p. 8, gives
\[
\int|\operatorname{Rm}_{\mathrm{op}}|^2
=8\pi^2\chi(M)+P.
\]
Section 11, printed pp. 39–40, explicitly distinguishes the then-unsolved full-curvature infimum on general-type blowups from exactly computable scalar and Ricci infima. This is a historical source statement, not a claim that the 2026 literature has been exhausted. It explains why applying the classical Ricci-minimization theorem cannot automatically decide O11: subtracting a separately minimized scalar functional does not commute with taking an infimum.

The project already established this geometric identification. It is not new research credit for this turn. The fresh source check only prevents the erroneous assumption that an exact Ricci infimum already supplies the exact trace-free Ricci infimum.

## 6. Actual outcome

This attempt does not close O11. It identifies a redundant operation to stop repeating: optimizing or smoothly differentiating the same exact identity over actual fields does not create the missing sharp estimate. The missing information remains an independent bound
\[
4\mathbb E K_\epsilon\le\mathcal A+o(Q)
\]
on true near-minimizers, or a real competitor disproving it. A proof of that inequality must contain a global coercive/comparison step not already contained in the equality (1). The equality remains useful as an accounting identity, but is not evidence that such a step has been obtained.

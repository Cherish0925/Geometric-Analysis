# Current results and mathematical questions

The statements below route to full proofs in the included manuscript;
they are not replacements for the hypotheses in those proofs. The
consolidated baseline includes the September web increment and the
3 October scientific overview; Section 4 includes the 4 October construction
and its subsequent scope clarification. See [conventions](conventions-and-literature.md)
for norms and normalization.

## 1. An actual-form interface

For a smooth self-dual two-form `psi`, put

\[
q=|\psi|^2,\quad A_\psi=\frac q{24}I-\frac18\psi\otimes\psi,
\quad B_\psi=\fint|\Delta_H\psi|^2,
\]
\[
d_\psi=\fint\bigl(|\operatorname{Ric}+g|^2+
|W^+-A_\psi|^2+(q-2)^2\bigr).
\]

The bounded-form theorem gives

\[
\|\psi\|_\infty\le K\quad\Longrightarrow\quad
(1+B_\psi)d_\psi\ge c(K)>0.
\]

This interface does not assume a spin structure or monopole class. Its
fixed polynomial model, amplitude bound and source cost are explicit.
The spinor identities used in linear coercivity are additional structure.
Proof: manuscript `sec:bounded-forms`; conceptual connection:
[field interfaces](../research/paper/sections/field_interfaces_and_curvature_interactions.tex).

## 2. Single-solution parameter analysis and N1

On a negative Yamabe representative with `s=-4`, one ordinary actual
monopole gives the finite-parameter estimate

\[
(1+b)\left(\frac PV+\frac{D_\beta}{\beta V}\right)
\ge c_{\rm par}\frac{(\beta-2)^2}{\beta^4},
\qquad b=\frac{(-a^2)_+}{V},\quad 2\le\beta<\infty.
\]

The same structure and solution are used throughout. The parameter
`beta=8` aligns with Chern--Weil:

\[
D_8=108\pi^2(T_+-2p/3)+\frac{27}{2}P.
\]

Exact conformal transfer yields the negative-square version of N1,

\[
\mathcal J(g)+\left(\frac{T_+}{A}-\frac23\right)_+
\ge\frac{c_*}{1+(-a^2)_+/(2\pi^2A)}.
\]

There is also the relative-shortfall version

\[
\mathcal J(g)+\left(\frac{T_+}{A}-\frac23\right)_+
\ge\frac{c}{1+(T_+-a^2)_+/A}.
\]

Thus `a^2>=0` already removes the negative-square cost in the first
formula. A positive lower bound on `J` itself requires subtracting
the displayed topological summand. To apply the theorem to every metric
on a manifold, supply its hypothesis on every conformal class with a
common `A`. The inheritance from older conformal supply, Pin lifting
and descent, and the separate Ricci-flat exclusion are included proofs.

Read [trace-free gap](../research/paper/sections/tracefree_gap.tex),
especially `def:trf-input`, `cor:trf-nu`, `cor:trf-y`.

## 3. Linear coercivity: I40/I41 and its single-solution form

Let

\[
\Sigma=S-32\pi^2p,\qquad \Pi=P+D_2,
\qquad Y=(T_+-a^2)_+.
\]

Under the stated single-Yamabe-monopole input,

\[
0\le\Sigma\le C\{\Pi+\sqrt{\Pi Y}\},\qquad
(p-T_+)_+\le C_T\{\Pi+\sqrt{\Pi Y}\}.
\]

In particular, `a^2>=T_+` gives `Sigma <= C(P+D_2)` without an
additional scalar-variance or background-volume term. The proof
retains a non-small curvature background that annihilates the actual
calibrated spinor. The exact Hessian identity then charges the
incompatible part; the determinant-square budget and the same-field
weak Bianchi test close the remaining energy. This is stronger than
replacing every curvature contribution by its absolute size.

Read [linear coercivity](../research/paper/sections/linear_coercivity.tex)
and [its single-solution form](../research/paper/sections/single_solution_coercivity.tex).
Classical supply, new analysis and actual applications are distinct
steps of the same proof chain.

## 4. Sharp scale and the variational problem

For the specified balanced family

\[
M_j=X_j\#k_j\overline{\mathbb{CP}}^{\,2}
\#\ell_j(S^1\times S^3),\quad
A_j=c_1^2(X_j),\quad Q_j=k_j+4\ell_j,\quad h_j=Q_j/A_j\to0,
\]

the current results give, for sufficiently small `h_j`,

\[
c h_j\le\alpha_j:=\inf_g\mathcal E(g)
=\inf_g\mathcal J(g)\le\frac{4h_j}{1+h_j},
\qquad
\alpha_j=4\frac{\inf_gP(g)}{8\pi^2A_j}+O(h_j^2).
\]

Linear order is settled. The handle-only subfamily has the exact displayed
upper value. Coefficient four is also established in the specified
recovery neighborhoods and localization regimes, but is not a universal
balanced optimum. The 4 October finite-scale construction, including its
full transition cost and smooth matching, gives on suitable balanced CH
cover towers

\[
\limsup_j\frac{\alpha_j}{h_j}<3.999215<4.
\]

Thus the earlier candidate `inf P = 8 pi^2 Q + o(Q)` is false in that
admissible family. The construction is existential in the cover tower;
it does not determine every previously fixed tower's optimum or classify
all near-minimizers. The unrestricted best first-order cost remains open.
The latest continuation also establishes the classical threshold for a
complete pure-handle cell, without implying additivity for mixed
blowup--handle cells. A cell infimum is not automatically the all-metric
infimum. The [comparison supplement](../research/supplements/20261004_classical_and_quantitative_gaps.tex),
Section 6, includes the transfer formula and links to the dated proof texts.

The newer variational selection supplies genuine near-minimizers with
critical integral near-stationarity and near-stability. Adaptive
curvature tests and same-field Walsh identities give additional signed
information. Matching a global lower bound to the best available
constructions remains the variational question; a universal lower bound
with coefficient four is no longer a candidate in the family just described.

For this ordinary surgery family with the specified `b_+>=2` supply,
the complete ordinary-monopole convex and positive-plane budgets are
both `A`. This follows from classical simultaneous scalar recovery;
it does not compute the complete class budget of the different BF
connected sums.

Read [variational geometry](../research/paper/sections/variational_geometry.tex)
and [global cost](../research/paper/sections/variational_selection_and_global_cost.tex).
The recent Weyl constructions supply a related comparison: on the same
metric, the Weyl saving must pay its scalar cost to lower the Ricci defect.
The finite-scale construction above includes that coupled cost. A saving
at only a fraction `theta` of the blowup sites contributes that fraction
to the first-order change. It cannot be counted as a saving at every site.

## 5. Every fixed finite-density endpoint is established

Under the theorem's original actual conformal supply, with

\[
p\ge A>0,\qquad a^2\ge T_+,\qquad \chi(M)/A\le B<\infty,
\]

the endpoint theorem gives

\[
\kappa_\beta=\fint|\operatorname{Ric}+g|^2+D_\beta/V
\ge c(B)\frac{(\beta-2)^2}{\beta^2},
\qquad c(B)\ge c_0(1+B)^{-N_0}
\]

for some finite, non-optimal universal exponent `N_0`. No pointwise
Ricci, diameter, noncollapse, or uniform Sobolev bound is added.
Strong actual currents lead to a bounded same-bundle resolvent and
the fifth determinant line. Chern pairing and a positive-potential
test are two proof endings, not successive unproved steps.

The original balanced family has uniformly bounded `chi/A`, so this
endpoint theorem already covers it. Removing the density bound is a
different extension, not a missing proof for that family.

Read [finite-density endpoint](../research/paper/sections/finite_density_endpoint.tex),
`thm:finite-density-endpoint`, `cor:finite-density-polynomial`, and
[primitive-error transfer](../research/paper/sections/web_primitive_rate.tex).

## 6. Structure, realization and constructions already available

The proof library also contains the following substantial results in
their specified ranges:

| Theme | Established content | Principal labels |
| --- | --- | --- |
| Actual forms and joint structures | Harmonic Chern alignment, product calibration, positive-period inertia, sign-correlation criterion, variable-amplitude and signed Weyl identities | `sec:actual-forms`, `sec:period-inertia`, `sec:joint-matrix`, `sec:signed-weyl` |
| Whole marked cores | Sharp costs for specified complete fillings, relative determinant charge, boundary transfer, and local high-index models | `sec:whole-core`, `sec:marked-charge`, `sec:actual-core-fit` |
| Compactness and exact realization | Topological bubble exclusion, bilateral bidisk realization, Chern-boundary complex-hyperbolic realization, and finite-cover versions | `sec:ale-boundary`, `sec:bilateral`, `sec:chern-boundary`, `sec:virtual-realization` |
| Nonlinear repair and slow geometry | Full cyclic integrable-kernel repair with its quantitative loss; fixed-amplitude slow-family identities; local full-tensor and higher-dimensional repair | `sec:cyclic-kernel`, `sec:slow-moduli`, `sec:local-repair`, `sec:higher-local-repair` |
| Complete matching | Orbifold compactification, whole Milnor filling and harmonic-zero scale conditions | `sec:orbifold`, `sec:milnor-matching`, `sec:harmonic-zeros` |
| Fixed smooth manifolds | Dehn-twist and shear approximating metrics, monodromy, canonical and symmetry restrictions on possible exact outputs | `sec:fixed-bundle-geometry`, `sec:closed-shear`, `sec:shear-global` |
| Consequences and further constructions | Conformal-flow time estimates, quadratic-curvature/matter applications, A1/log-Weyl and algebraic construction programs | `sec:conformal-flow`, `sec:quadratic-matter`; original construction/global manuscripts |

These are not all instances of one unproved obstruction-or-existence
dichotomy. The [research map](research-map.md) locates each sufficient
set of global hypotheses and its complete source.

## 7. Questions that would change the present theory

| Question | Missing mathematical conclusion | Sufficient resolution |
| --- | --- | --- |
| Density-independent weak endpoint (O10) | Actual critical transitions when the core and exterior degenerate together at unbounded density | A uniform estimate under the original supply, or a closed actual counterexample satisfying all its quantifiers |
| Balanced optimal cost (O11) | The first-order lower bound against every competing geometry, not only specified recovery neighborhoods | Matching asymptotic lower and upper bounds; the coefficient need not be four |
| New actual scope | A natural object not covered by the old suppliers, or genuinely new simultaneous-field information | Supply the weaker interface on that object and obtain a new geometric conclusion |
| Full BF comparison | Control of all possible monopole classes on the stated BF connected sums at the needed precision | A complete budget bound; the known sign-family comparison is already available |
| Boundary realization | Global control after deleting the diameter hypothesis at the specified Chern boundary | Exact complex-hyperbolic realization, or a counterexample to that precise extension |
| Fixed-manifold existence | Whether the fixed Dehn-twist/shear manifold carries any Einstein metric | A construction or exclusion covering all exact candidates, not only a chosen repair neighborhood |
| General matching and repair | Structure, fields and full marked cores on the same relevant scales | The particular global transfer or nonlinear realization needed by the chosen problem |

For the positive-potential route to O10, a retained fifth-line mass and
its full weak equation must hold for the same test. Existing radial
identities do not yet eliminate the middle-amplitude concentration.
In the normalized zero-Weyl form limit,
`avg |nabla omega|^2 -> 8/3`, not zero. For O11 the remaining signed
error must be `o(Q)` with `Q=Ah`; an `o(V)` estimate is insufficient.

A complete bubble tree, a Gamma-limit or a classification of every
near-minimizer can be valuable conclusions, but none is a compulsory
prerequisite if a shorter argument settles the stated target. The
existing independent paper chain, its endpoint completeness, its
optimality and unrestricted exact existence are different completion
questions.

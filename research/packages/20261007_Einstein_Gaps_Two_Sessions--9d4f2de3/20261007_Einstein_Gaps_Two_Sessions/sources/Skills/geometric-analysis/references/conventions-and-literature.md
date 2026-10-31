# Conventions and literature

## Normalization ledger

Unless a source explicitly changes the convention, the integral theory is
on a closed oriented smooth four-manifold. Set

\[
V=\operatorname{Vol}(M),\quad S=\int s^2,\quad
P=\int|\operatorname{Ric}^{\circ}|^2,\quad R=P+S/4,
\quad T_+=2\chi+3\tau,\quad T_-=2\chi-3\tau.
\]

In the N1 sections, `T` means `T_+`. A subscript `+` on `T_+` denotes
orientation, whereas `(x)_+=max(x,0)` denotes positive part. For an actual
determinant class `a`, `p=(a_g^+)^2` is its positive harmonic projection
square; `A>0` is the stated lower budget. Class selection may depend on
the metric or conformal class only as allowed by the relevant supplier.

Weyl norms in the manuscript are operator Hilbert--Schmidt norms on
two-forms. Thus

\[
\mathcal W_{\rm ten}=\int W_{ijkl}W^{ijkl}
=4\int(|W^+|^2+|W^-|^2)=4\mathcal W_{\rm op},
\]
\[
4\pi^2T_+=S/24+2\int|W^+|^2-P/2,
\qquad P=2\mathcal W_{\rm op}+S/12-16\pi^2\chi.
\]

The full-curvature operator convention gives
`int |Rm|^2 = 8 pi^2 chi + P`. Do not apply it using the unconverted
four-index tensor norm.

The scale-invariant defects are

\[
\mathcal E(g)=\inf_{\lambda\ne0}
\frac{\int|\operatorname{Ric}-\lambda g|^2}{\lambda^2V},
\qquad \mathcal J(g)=4P/R\quad(R>0).
\]

For `R>0`,

\[
\mathcal E=4-\frac{(\int s)^2}{VR}
=\mathcal J+\frac{\int(s-\bar s)^2}{R}.
\]

For a Ricci-flat metric `R=0`, `J` is undefined and `E=4`. In the
positive-budget actual applications, scalar solvability excludes this
case separately. If
`delta_sigma=||g^{-1} Ric-sigma I||_{L^infty,op}`, then
`E <= 4 delta_sigma^2`; the reverse implication is not supplied.

On a negative Yamabe class, normalize the unique Yamabe representative
to `s=-4`. With `delta=S(g)-S(ghat)>=0`,

\[
P(g)=P(\widehat g)+\delta/12,\qquad
R(g)=R(\widehat g)+\delta/3.
\]

Consequently `J(g)` is a convex combination of `J(ghat)` and `1`.
This is not unconditional monotonicity under every conformal change.

The common parameter convention is

\[
D_\beta=(1+\beta^{-1})S+6(\beta+1)\int|W^+|^2-72\pi^2p.
\]

The finite-parameter estimate uses `D_beta/(beta V)`; the
finite-density endpoint uses `D_beta/V`. On `s=-4`,
`avg |Ric+g|^2=P/V`. Some historical texts call both Ricci defects `r`;
read their definition before moving an estimate.

For the constant rescaling of an ordinary monopole used in the current
sections,

\[
D_B\Phi=0,\qquad F_B^+=2i\sigma(\Phi),\qquad
|\sigma(\Phi)|^2=|\Phi|^4/8.
\]

The ordinary normalization instead has `F_B^+=i sigma(Psi)` and
`Phi=Psi/sqrt(2)`. Auxiliary torsion, bounded resolvent sections, and
the section of the **fifth tensor power** `L^{\otimes5}` are distinct
objects; that fifth power is not a Lebesgue exponent.

For finite covers, integrals and topological squares scale by the degree,
whereas `J` and `T/A` do not. Pin-minus applications use the actual
compatible lift and the invariant metrics and weights needed in the
proof, not arbitrary non-invariant solvability on the cover.

## Literature connections

The full bibliography is in [the manuscript](../research/Curvature_Realizability.tex)
and [its editable bibliography](../research/paper/references.tex).
The following fourteen primary entries are the October overview's
reading spine, not the whole bibliography. Their links preserve the
versions used in the integration.

| Source | How it enters the mathematics |
| --- | --- |
| [LeBrun, 2001](https://arxiv.org/abs/math/0003068) | Actual monopoles, curvature inequalities, classical Einstein obstructions, and simultaneous surgery recovery. |
| [Kotschick, special monopoles](https://arxiv.org/abs/math/0306022) | Class-square hypotheses and their actual gauge-theoretic meaning. |
| [Bauer--Furuta I](https://arxiv.org/abs/math/0204340) | Stable-cohomotopy refinement as a supplier. |
| [Bauer II](https://arxiv.org/abs/math/0204267) | Connected-sum nonvanishing with its precise hypotheses. |
| [Ishida--LeBrun](https://arxiv.org/abs/math/0111228) | Existing BF curvature applications and their comparison baseline. |
| [LeBrun, optimal curvature](https://arxiv.org/abs/math/0404251) | The distinction between Ricci-energy and full-curvature extrema, particularly Section 11. |
| [LeBrun, convex geometry](https://arxiv.org/abs/math/0611450) | Multiple-class convex budgets and equality structure. |
| [Furuta--Matsuo, v3](https://arxiv.org/abs/1405.1219v3) | Spectral differential defects for smooth pairs; topological consequences additionally require perturbed solvability. |
| [Ishida--Matsuo--Nakamura](https://arxiv.org/abs/1505.05948) | Actual twisted monopoles and double-cover lift. |
| [LeBrun, Einstein overview, v1](https://arxiv.org/abs/2609.03033v1) | Einstein four-manifolds, chiral connections, and gauge curvature constraints. |
| [Apostolov--Armstrong--Draghici, v2](https://arxiv.org/abs/math/0109098v2) | Exact almost-Kähler integrability under the stated curvature conditions; a point of comparison for weak-error rigidity. |
| [Anderson, curvature functionals](https://arxiv.org/abs/math/0511034) | Ideal minimizing configurations and the geometric hypotheses needed to use them. |
| [Malchiodi--Malizia, 2025 v1](https://arxiv.org/abs/2505.17752v1) | Strict Weyl-energy gluing on the prescribed connected sum, with the two-factor chirality conditions. |
| [Malchiodi--Malizia, 2026 v2](https://arxiv.org/abs/2604.17547v2) | Different gluing mechanism: a non-half-self-dual Bach-flat factor and a non-spherical positive-Yamabe locally conformally flat factor. |

The 2025 Weyl theorem applies to the stated complex-hyperbolic blowup
topology. Its strict Weyl gain must still be combined with scalar cost
and a reproducible first-order saving to affect the balanced optimum.
The half-self-dual complex-hyperbolic factor does not satisfy the
different 2026 theorem's non-half-self-dual hypothesis.

At fixed topology the comparison is exactly

\[
\Delta P=2\Delta\mathcal W_{\rm op}+\Delta S/12.
\]

Relative to two *separate* connected-sum factors, it becomes

\[
\Delta_\# P=2\Delta_\#\mathcal W_{\rm op}
+\Delta_\# S/12+32\pi^2.
\]

These formulas compare the same constructed metrics. They do not follow
by independently minimizing and then subtracting the terms.

## Classical bounds and subsequent quantitative results

The [mathematical comparison](../research/supplements/20261004_classical_and_quantitative_gaps.tex)
derives the classical normalized bound
`J >= (2-3t)/(2-t)` for `0<t=T_+/A<2/3`, the inherited surgery upper
bound, the critical N1 transfer with class-square costs, and explicit
formal data separating I40/I41 from the listed classical numerical
budgets. It also includes the 4 October sub-four construction and its
global transfer, so the earlier candidate coefficient is not mistaken
for the current optimum. Theorem 7.5 is in LeBrun's **2026 overview**,
not the **2006 convex-geometry paper**. All comparisons retain the
individual theorems' actual-supply hypotheses.

# First scientific line: from functional excess to Einstein defect

This increment answers a specific question left by the previous actual-form
paper: what usable conclusion follows **without already assuming the Ricci
error is small**?

The answer has two parts. On the original metric, scalar coherence is a
separate requirement. Within its conformal class, the negative Yamabe
representative removes that requirement and gives a direct integral bound.
The explicit separating-neck example demonstrates the distinction.

## Read these three results

1. [Energy selection and all minimizing sequences](line1_energy_selection.md)
   ([LaTeX](line1_energy_selection.tex), [PDF](line1_energy_selection.pdf)).
   For \(T=A-d\), \(C=8\pi^2A\), \(H=8\pi^2d\), and
   \(J=\int|\operatorname{Ric}|^2-C-H\), the actual polarized monopole
   hypotheses give
   \[
   H-\sqrt{J(C+J)}
   \le\int|\operatorname{Ric}^{\circ}|^2\le H+J.
   \]
   Every minimizing sequence has
   \[
   \mathcal E(g_j)=\frac{4d}{A+d}
     +\frac{\int(s_j-\bar s_j)^2}{8\pi^2(A+d)}+o(1).
   \]
   This extends the previous Kähler-only profile to all metrics. Its
   Yamabe representatives satisfy
   \(\mathcal E(\widehat g_j)\to4d/(A+d)\).

2. [An actual conformal-neck construction](line1_conformal_neck.md)
   ([LaTeX](line1_conformal_neck.tex), [PDF](line1_conformal_neck.pdf)).
   A fixed product of hyperbolic surfaces has conformally Kähler,
   non-Kähler metrics with \(p=a^2=T\), vanishing LeBrun defect, vanishing
   trace-free Ricci energy, and limiting relative defect \(2/5\).
   A variant even has \(\|\operatorname{Ric}^{\circ}\|_\infty\to0\).
   Both bulk regions remain present with different scalar scales.
   This is not a Yau26 counterexample: the same manifold admits product
   Einstein metrics.

3. [A non-Kähler converse, with two choices of metric](line1_non_kahler_bridge.md)
   ([LaTeX](line1_non_kahler_bridge.tex), [PDF](line1_non_kahler_bridge.pdf)).
   Negative scalar band and scalar spectral control give stability of the
   original metric from functional and period inputs. Alternatively, the
   negative Yamabe representative satisfies the simpler bound
   \[
   \mathcal E(\widehat g)\le
     \frac{4[p-T+4D(g)]}{2p-T+4D(g)}
   \]
   with no scalar-band or spectral-gap assumption. The note also states
   the actual-form supply and its joint second-order budget.

## Relation to the existing research

The existing uniform integral obstruction near the forbidden \(2/3\)
topological ratio is not reproved or replaced. Its calibration argument
remains in the original manuscripts. The new energy-selection calculation
instead uses classical inequalities directly.

The earlier form supply produces \(t=1/2\), an allowed Round21 root.
Substituting this value into the root-distance inequality is not an
additional obstruction. The new consequences above use information absent
from that substitution: the polarized period budget and scalar coherence,
or a change to the Yamabe representative.

These are additions to the project, with complete derivations, not three
claims of worldwide originality. Their classical inputs and prior-round
overlap are identified in the papers. In particular, the energy-selection
formula, its corollaries, and its independent rederivation are one result,
not separately counted breakthroughs.

The connection to Yau26 is precise: integral closeness after conformal
normalization is not pointwise Ricci pinching, nor exact existence.
At a fixed positive \(d/A\), pointwise near-Einstein inputs cannot also
minimize the absolute Ricci energy. At \(d=0\), the conformal estimate
supplies integral inputs, but the passage to the required pointwise or
exact conclusion is still a mathematical problem.

## Evidence and preserved sources

- [Verification record](line1_bridge_verification.md): executed checks,
  proof-review scope, compilation and source comparison.
- [Previous turn's entry](START_LINE1_20260923.md): actual-form theorem,
  Kähler controls, all seven unchanged uploaded sources and their coverage.
- The archive retains the previous tracked research snapshot. No original
  Skill, source upload, live Session, or service was replaced by this increment.

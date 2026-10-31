# Step 68: Global Yau-26 landscape after the IL assembly

Session: S0910A01.  Agent2 / Constructor.  Step 68, Execute.

## The complementary-difficulty structure

The 20260912 manuscript (Chapter 10, line 6436) identifies a fundamental
structural observation:

> Surface-bundle route: has global max-norm δ→0 near-negative-Einstein
> constructions, but Einstein nonexistence is genuinely open.
>
> Graph-manifold route: has complete Einstein nonexistence (Di Cerbo),
> but no δ→0 construction exists.

These complementary advantages cannot simply be spliced.  This is not a
deficiency of any particular construction method; it reflects the
mathematical structure of the problem.

## Why the surface bundle route is delicate

For the surface bundle $E_D$ with fiber genus $\ge2$ and degree $D>0$:

1. **Near-Einstein exists:** The balanced double-collar construction gives
   $\delta=\Theta(\varepsilon^3)$ with exact coefficient $2/\pi^4$.

2. **Einstein = full curvature energy attainment.** By Chern–Gauss–Bonnet:
   $$
   \int|\operatorname{Rm}|^2=32\pi^2\chi(\hat E)
   +4\int\left|\operatorname{Ric}-\frac s4g\right|^2.
   $$
   Einstein $\iff$ $\int|\operatorname{Rm}|^2=8V_*$ (the infimum).

3. **Scalar and Ricci energy non-attainment does NOT imply full curvature
   energy non-attainment.** The monopole/Yamabe estimates force
   $\inf\int s^2=16V_*$ and $\inf\int|\operatorname{Ric}|^2=4V_*$
   to be unattained.  But these are different functionals.

4. **No complex structure on any cover** (Llosa Isenrich–Py).
   Not virtually Kähler.  No $\sec\le0$ metric (when $D$ is infinite-order).

5. **Positive simplicial volume** (bounded Euler-class pairing).
   The entropy route has numerical slack, not zero.

So the question "does $E_D$ carry a negative Einstein metric?" remains
genuinely open as a mathematical problem.

## Why the graph-manifold route is hard

For extended graph four-manifolds $M$ (Frigerio–Lafont–Sisto type with
pure hyperbolic blocks and torus cusps):

1. **Einstein nonexistence:** Di Cerbo's theorem excludes all Einstein
   metrics on $M$.

2. **Weyl concentration:** Any metric with $\delta<1/3$ must have
   $\|W\|_\infty\ge(1-3\delta)/\sqrt3$ while $\frac1V\int|W|^2\le\frac83\delta$.
   Weyl must concentrate on a set of relative volume $O(\delta)$.

3. **Diameter grows logarithmically:** Under additional $\nabla W$ control,
   $\operatorname{diam}\ge\sqrt{2/7}\log(1/\delta)-C_L$.

4. **No δ→0 construction exists.**  The interface cost between hyperbolic
   blocks and torus cusps competes against the δ→0 requirement.  Existing
   minimum-volume sequences do not automatically give $\|\operatorname{Ric}+g\|_\infty\to0$.

5. **A03's Koiso reversal:** Local torus reversal means local no-go arguments
   are false; the problem is global half-core existence/matching under
   full Einstein constraints.

## The restricted IL theorem in this landscape

The assembled IL theorem (§68) shows that a specific four-dimensional
geography with SW monopole families has a family-uniform negative-sign
pinching gap.  This is:
- A genuine obstruction to near-Einstein metrics on those topologies
- Evidence that Einstein-obstructing manifolds tend to resist Ricci pinching
- NOT a dimension-only result (requires the specific monopole structure)

## What would resolve Yau-26?

### For a positive answer (pinching forces Einstein)

One dimension-only sign branch in each dimension $n\ge4$ would suffice.  The
IL budget/forbidden-germ architecture is one route-specific pattern, not a
requirement imposed by Yau26 itself.  A positive proof could instead use any
mechanism that turns a dimension-only Ricci interval into existence of some
Einstein metric on the same smooth manifold, including classification,
compactness plus topology, variational attainment, surgery stability, or a new
geometric structure not resembling the IL calibration.

### For a negative answer (refutation)

A refutation must defeat every admissible interval $[c_n,C_n]$.  In normalized
terms this means defeating both forcing signs in the same dimension (possibly
on different manifolds): one needs negative near-Einstein metrics on
Einstein-obstructed smooth types **and** positive near-Einstein metrics on
Einstein-obstructed smooth types, or another construction that directly
invalidates all intervals.  Thus an all-sign Einstein obstruction combined only
with $\delta_-\to0$ would defeat the negative branch but would not by itself
refute the displayed proposition.

Current candidates fail one or both requirements.

## Most promising new directions

1. **Full curvature energy attainment on $E_D$:** Is
   $\inf\int|\operatorname{Rm}|^2$ achieved?  If yes, $E_D$ carries a negative
   Einstein metric and is not a negative-branch counterexample.  If no, then
   combined with the existing $\delta_-\to0$ construction it would defeat the
   negative branch in dimension four, but the positive branch would still need
   a separate defeat before Yau26 is refuted.  This direction is valuable
   because it concerns an arbitrary Einstein metric, not one gluing
   construction; it becomes actionable only with a compactness mechanism for
   minimizers or a genuine obstruction to all full-curvature minimizers.

2. **Positive-branch for general four-manifolds:** The manuscript gives a
   positive-branch result for complex/symplectic types under ratio-3.
   Extension to arbitrary smooth types requires new ideas beyond Seiberg–Witten.

3. **Global half-core for graph manifolds:** A03's Koiso reversal changes
   the problem but does not close it.  Global matching under full Einstein
   constraints with controlled maximum Ricci defect is the precise open question.

4. **Higher-dimensional mechanisms:** In $n\ge5$, no SW or self-dual Weyl
   machinery exists.  Look for characteristic-class quantization,
   compactness/rigidity, variational, or collapse mechanisms without requiring
   them to imitate the IL route.

## Source files
- Assembly: `workspace/notes/step68_restricted_IL_canonical_assembly.md`
- Terminal calibration: `workspace/notes/step67_terminal_recalibration_recovery.md`
- 20260912 manuscript: `Skills/qiushi-yau26/references/research/20260912.tex`
- A03 surface-bundle/graph-manifold: `S0910A03/workspace/notes/step68_manuscript_absorption.md`

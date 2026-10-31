# Step 49: Positive noncollapsed wall, operator-norm scaling, and finite product-quotient enumeration

Session S0910A02. Agent1 / Orchestrator. Phase Explore.

## 0. Target fidelity and why this step was needed

The active target remains the full Yau--26 proposition: for every dimension
\(n\ge2\), decide whether a dimension-only two-sided Ricci pinching interval
forces the underlying closed smooth manifold to admit some Einstein metric,
with no relation required between the input metric and the output metric.  This
note concerns only a four-dimensional, positive-sign, noncollapsed subproblem.
It does not address positive collapse, the negative branch, dimensions \(n\ge5\),
or the final Lean formalization obligation.

Step 48 correctly located a real wall in the positive noncollapsed route: the
bi-Kähler product quotient \((S^2\times S^2)/\mathbb Z_2\) has four \(A_1\)
points and
\[
  R_+(p)=R_-(p)=\operatorname{diag}(\Lambda,0,0),
\]
so there are kernel directions for both compatible and reversed Eguchi--Hanson
insertions.  But Step 48 miscalibrated two supports under that conclusion:

1. A nonzero second or higher Ozuch obstruction blocks an **exact Einstein**
   desingularization; it does not block a family with
   \(\|\operatorname{Ric}-\Lambda g\|_{op}\to0\).  The Yau--26 operator norm is
   critical exactly at the first obstruction.
2. The H4-dual flux bridge must be normalized by the signal size \(t_i^2\).
   The unnormalized boundary functional is linear in the metric error and
   vanishes trivially under \(h_i\to0\).  The hard analytic lemma is quantitative
   two-scale matching in the neck, not just cutoff bookkeeping.

The allocation consequence is the opposite of Step 48's §3.2 branch (II): once
the first obstruction is killed, the explicit glued approximate metrics are
already near-Einstein in the operator norm required by Yau--26.  No full gluing
or implicit-function theorem is needed to produce pinched input metrics.

## 1. The operator-norm scaling theorem

### 1.1 Source estimates

The original scaling warning from Step 1 used Morteza--Viaclovsky's refined
Calabi insertion estimates.  In their notation, on the Calabi piece the refined
metric satisfies
\[
 \big|\nabla^k(\operatorname{Ric}_{g_t}-\Lambda g_t-t\lambda\chi_t o)\big|_{g_{cal}}
 \le C_k t^2 \rho^{2-k}.
\]
Source anchors: `The-Calabi-metric-and-desingularization.../object.md` lines
456--491 and, in the transition, lines 497--514.  The same scale structure is
present in Ozuch's four-dimensional Einstein-modulo-obstruction construction:
`Higher-order-obstructions.../object.md` lines 715--726 give the approximate
metric and its \(h_2,h_4,\bar h^4\) controls, while lines 791--807 record that
for exact Einstein desingularizations the obstruction equation has the form
\[
  t_j\lambda_k^j + t_j^2\mu_k^j = O(t_{max}^{5/2}).
\]
The first obstruction itself is vectorial:
\[
 \lambda_k^j=c\left\langle R^{\pm}(p_j)\zeta_j^{\pm},\zeta_{j,(k)}^{\pm}\right\rangle,
\]
from Ozuch lines 650--654 and the earlier formula read in Steps 43--48.
The second obstruction formula, lines 667--706, belongs to the exact-Einstein
Kuranishi/obstruction tower.

### 1.2 Scaling conversion

In the bubble/core and damage region the smooth metric is comparable to
\(t g_{cal}\).  For a \((0,2)\)-tensor \(T\), raising one index therefore costs
\(t^{-1}\):
\[
 |T|_{op,g_t}\sim t^{-1}|T|_{g_{cal}}.
\]
Hence the refined remainder becomes
\[
 |t^2\rho^2|_{op,g_t}=O(t\rho^2).
\]
On the core \(\rho=O(1)\) this is \(O(t)\), while in the standard damage zone
\(\rho\sim t^{-1/4}\) it is \(O(t^{1/2})\).  The orbifold exterior is the original
Einstein metric away from small gluing balls.  Therefore a finite collection of
refined EH replacements with all first obstructions killed satisfies
\[
  \sup_M\|g_t^{-1}(\operatorname{Ric}_{g_t}-\Lambda g_t)\|_{op}\le C t^{1/2}\to0.
\]

By contrast, a first obstruction term \(t\lambda o\), with \(o\) bounded and
nonzero on the EH core, becomes \(O(1)\) in the same operator norm.  It is the
only local obstruction order visible to Yau--26 pinching.  A second obstruction
term \(t^2\mu o\) becomes \(O(t)\); a \(q\)-th obstruction \(t^q\) becomes
\(O(t^{q-1})\), hence vanishes for every \(q>1\).  Thus:

> **Operator-norm principle.** For a fixed finite EH desingularization pattern,
> \(R_{\varepsilon_j}(p_j)\zeta_j=0\) at every replaced \(A_1\) singularity is
> the complete local condition for constructing \(C^0\)-Ricci-pinched approximate
> metrics.  Higher Ozuch obstructions are essential for exact Einstein gluing but
> are not obstructions to \(\delta_+(g_t)\to0\).

This is the decisive correction to Step 48: the fact that \(\mu_1=0\) at the
bi-Kähler locus is not load-bearing for Yau--26.  If \(\mu_1\ne0\), the same
approximate metrics would still satisfy \(\delta_+(g_t)\to0\).  The first
obstruction bridge is not a first approximation to be escalated beyond; it is
precisely the local \(C^0\) operator-norm story.

The arithmetic is recorded in
`workspace/data/step49_operator_norm_and_enumeration.json`, produced by
`workspace/scripts/step49_operator_norm_and_enumeration.py`.

## 2. Explicit four-bubble consequence for the product quotient

For the product Einstein metric on \(S^2\times S^2\), Steps 44--45 verified
\[
  R_+=R_- = \operatorname{diag}(\Lambda,0,0),
  \qquad \ker R_\pm=\operatorname{span}\{e_2,e_3\}.
\]
The diagonal half-turn quotient has four \(A_1\) singularities.  At each point
and for either chirality, choose an EH parameter direction
\(\zeta_j\in\ker R_{\varepsilon_j}(p_j)\).  Then all vector first obstructions
vanish.  Applying the estimate above gives a family of smooth metrics on the
corresponding topological desingularization \(M_{\varepsilon,t}\) with
\[
  \|\operatorname{Ric}_{g_t}-\Lambda g_t\|_{op,g_t}=O(t^{1/2})\to0.
\]
This construction is explicit at the level needed for Yau--26 input metrics:
cut out the four orbifold balls, glue in correspondingly oriented scaled
Eguchi--Hanson pieces with the refined quadratic correction, and use the
standard cutoff radius.  It does **not** claim an exact Einstein metric near
this glued metric.

This is a real positive-pinching family on each smooth manifold obtained by the
orientation assignment, subject only to the remaining topological identification
caveats (parity/spin and exact smooth diffeotype for mixed rows).  It is not a
counterexample to Yau--26 unless one separately proves that one such smooth
manifold admits no Einstein metric of any sign.

## 3. Finite \(A_1\) orientation enumeration

The orientation bookkeeping from Step 45 should be used without forcing the
balanced stress-family row.  If the product quotient has four \(A_1\) points and
\(r\) of them are reversed, then
\[
  (b_+,b_-)=(1+r,5-r),\qquad \chi=8,
\]
with the convention that a compatible EH insertion contributes a negative class
and a reversed insertion contributes a positive class.  Thus:

| reversed \(r\) | \((b_+,b_-)\) | current Einstein status for Yau--26 |
|---:|---:|---|
| 0 | \((1,5)\) | harmless: all-compatible/crepant side has Del Pezzo degree-4 diffeotype; Del Pezzo diffeotypes admit positive Einstein metrics by the LeBrun--Ozuch source line 170 citing Chen--LeBrun--Weber/Tian-type classification |
| 1 | \((2,4)\) | mixed-chirality target; no Einstein metric known in the session record |
| 2 | \((3,3)\) | balanced mixed target, conditionally topological \(3H\) if parity/spin is proved; no Einstein metric known in the session record |
| 3 | \((4,2)\) | mixed-chirality target; no Einstein metric known in the session record |
| 4 | \((5,1)\) | orientation reversal of the all-compatible Del Pezzo row; harmless as a smooth unoriented Einstein-existence question |

Two caveats are important:

- The phrase "crepant/weak del Pezzo degree 4" does not by itself mean the
  minimal resolution of the singular quotient, with its \((-2)\)-curves, carries
  a Kähler--Einstein metric in that complex structure.  The Yau--26 output
  metric is allowed to be unrelated to the input, so the needed calibration is
  only the smooth diffeotype's known Einstein existence.  LeBrun--Ozuch lines
  157--170 source this at the diffeotype level for Del Pezzo manifolds.
- For mixed rows, Step 45 already found that parity/spin and smooth type have
  not been proved.  The gluing produces smooth manifolds, but their exact
  standard diffeomorphism type is not yet known.  This must be computed before
  using a mixed row as a named stress manifold.

The diagonal \(V_4\) product-quotient model from Step 45 similarly has six
\(A_1\) points and rows
\[
  (b_+,b_-)=(1+r,7-r),\qquad \chi=10,
\]
with all-compatible/all-reversed Del Pezzo-type endpoint rows and mixed rows
\(r=1,\ldots,5\) as concrete unknown Einstein-existence targets.  The balanced
row \(r=3\) would be topological \(4H\) if parity/smooth type are established.

## 4. Other product quotients with isolated ADE points

A quick finite-group test reduces the product-quotient exceptional locus in the
orientation-preserving graph-action class.  Let a finite rotation group act on
both \(S^2\) factors through a graph \(\Gamma\to SO(3)\times SO(3)\).  At a fixed
point for a stabilizer of order \(m\), local complex weights are of the form
\((1,a)\) at one endpoint choice and \((1,-a)\) at the opposite endpoint choice.
For both to be ADE/SU(2), one would need simultaneously
\[
  1+a\equiv0\pmod m,
  \qquad 1-a\equiv0\pmod m,
\]
so \(m\mid2\).  Therefore, in this graph-action class, only \(C_2\) and
\(D_2=V_4\) can have exclusively \(A_1\)/ADE isolated singularities.  This is
consistent with LeBrun--Ozuch's line 130 observation that cyclic quotients of
\(\mathbb{CP}^1\times\mathbb{CP}^1\) by identical rotations with \(k\ne2,4\)
have four orbifold singularities but only two of type T.

This does not yet enumerate factor-swap subgroups of
\((SO(3)\times SO(3))\rtimes\mathbb Z_2\), nor does it replace the required
smooth-type calculation.  It does show that the currently visible all-ADE
product-quotient wall is finite rather than a large hidden family.

## 5. Corrected H4-dual hard lemma

For the compactness/obstruction direction, H4_dual remains valuable but should
be stated in the normalized form.  In a bubble frame, the ambient quadratic
signal is
\[
  h_i \sim t_i^2 H_2(\rho),
\]
so the obstruction boundary functional is of size \(t_i^2\).  The correct object
is therefore
\[
  t_i^{-2}\mathcal B_k(R,i),
\]
not \(\mathcal B_k(R,i)\).  Without this normalization, \(h_i\to0\) gives the
trivial limit \(\mathcal B_k(R,\infty)=0\) and reads no curvature coefficient.

This normalization changes the error accounting.  The cutoff commutator term
previously bounded schematically by \(\|h_i\|R^{-2}\) is also of order \(t_i^2\)
for the ambient quadratic term \(h_i\sim t_i^2R^2\); after dividing by \(t_i^2\),
it is part of the flux calculation rather than a discardable error.  The Ricci
defect contributes \(t_i^2\delta_i\log R\), hence a relative error
\(O(\delta_i\log R)\), which vanishes in the iterated limit for fixed \(R\).

The single hard lemma is:

> **Quantitative two-scale flux lemma (H4_dual.c).** In a noncollapsed
> \(C^0\)-Ricci-pinched sequence with an EH bubble of scale \(t_i\), there are
> compatible bubble/orbifold gauges on neck annuli \(\rho\sim R\), for fixed
> large \(R\), such that the normalized boundary functional
> \(t_i^{-2}\mathcal B_k(R,i)\) converges to the Ozuch/Biquard flux determined by
> the ambient quadratic term \(H_2\), with defect error controlled by
> \(O(\delta_i\log R)\) and with the cutoff contribution included in the limiting
> Wronskian.

Ordinary Cheeger--Naber \(C^{1,\alpha}_{loc}\) convergence gives only
\(h_i=o(1)\); it does not give the quantitative \(t_i^2R^2\)-scale expansion
needed above.  This is the pinched analogue of Ozuch's weighted Hölder
approximation theorem for exact Einstein degenerations, and it should be the
named analytic bottleneck if the obstruction bridge is pursued.

## 6. Consequences for the global Yau--26 allocation

1. **Positive noncollapsed local picture.** Away from first-obstruction
   degeneracy, the mode-projection bridge would exclude EH bubbling by forcing
   \(R_\varepsilon(p)\zeta=0\).  At the product bi-Kähler degeneracy, explicit
   near-pinched glued metrics exist once kernel directions are chosen.  Higher
   Ozuch obstructions cannot save a compactness proof of \(P_4^+\) because they
   are invisible to the Yau--26 operator norm in the limit.
2. **Exceptional mixed rows become concrete targets.** The product quotient
   provides finite smooth manifolds with \(\delta_+\to0\) metrics; the open
   question is whether any mixed row has no Einstein metric.  This is a sharper
   target than "analyze higher obstruction".
3. **Known-Einstein endpoint rows calibrate the construction.** All-compatible
   and all-reversed rows are harmless for Yau--26 because their smooth
   unoriented diffeotype is Del Pezzo-type and hence known to carry positive
   Einstein metrics.  They are useful controls for the exponent and topology
   calculations.
4. **The full problem is still wide open.** Positive collapse remains the main
   four-dimensional proof obstacle, especially for large \(\#_k(S^2\times S^2)\)
   after Step 9's noncollapsed finite-type dichotomy.  The negative branch has
   new peer-reported restricted IL gap theorems (A01 #372, A03 #375), but A02
   has not independently verified their flow/extraction chain.  Dimensions
   \(n\ge5\) and Lean formalization remain unresolved.

## 7. Files and source anchors

- Computation/data: `workspace/scripts/step49_operator_norm_and_enumeration.py`,
  `workspace/data/step49_operator_norm_and_enumeration.json`.
- Step-48 supersession patch: `workspace/notes/step48_H4dual_and_biKahler_realizability.md`.
- MV/Calabi estimates: `Knowledge/objects/papers/The-Calabi-metric-and-desingularization-of-Einstein-orbifolds--3b9fd6e4b2cd--c8fe6b2cf08c/object.md`, lines 456--514.
- Ozuch obstruction tower: `Knowledge/objects/papers/Higher-order-obstructions-to-the-desingularization-of-Einstein-metrics--94f76f3b5378--19c12fb27fae/object.md`, lines 650--706 and 715--807.
- Hermitian/Del Pezzo calibration and product quotients: `Knowledge/objects/papers/Desingularizations-of-Conformally-Kaehler-Einstein-Orbifolds--8fe1aa31deb8--5b19d560b771/object.md`, especially lines 130, 157--170, and 186--191.

No branch of the full Yau--26 proposition is proved or refuted by this step.

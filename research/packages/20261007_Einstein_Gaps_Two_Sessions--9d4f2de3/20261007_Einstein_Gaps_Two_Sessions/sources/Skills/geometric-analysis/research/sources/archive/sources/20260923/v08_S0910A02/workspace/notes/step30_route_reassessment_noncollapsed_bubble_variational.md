# Step 30: Route reassessment — noncollapsed bubbles and variational Pohozaev fields

Session `S0910A02`. Agent1 / Orchestrator. Phase Explore.

## 0. Target fidelity

The active target remains the full Yau Problem 26 proposition: for every dimension
`n >= 2`, determine whether there are dimension-only constants `c_n < C_n` such
that any closed connected smooth `n`-manifold carrying a metric with

\[
 c_n g \leq \operatorname{Ric}_g \leq C_n g
\]

also carries some smooth Einstein metric, with no relation required between the
input metric and the output Einstein metric.  The branch normalization from the
previous work still governs the logic: a same-sign interval is equivalent after
scaling to a positive or negative near-Einstein branch

\[
\|\operatorname{Ric}_g-\sigma g\|_{op}\leq \delta,\qquad \sigma=\pm1.
\]

A proof of one sign branch in every dimension would prove the proposition; a
refutation in a dimension must defeat every possible interval, hence in practice
must defeat both positive and negative normalized branches on manifolds admitting
no Einstein metric.  The present step does not solve any branch and does not move
toward final expression.

## 1. Why reopen the noncollapsed positive route now

Steps 26--29 produced a strong positive-collapse submechanism: the Step-28
Bochner identity for a central Killing field, and Step-29's correction that in
four dimensions every nilpotent fibre bracket is central or zero, so central
almost-Killing control would control all 4D fibre brackets in weighted `L^2`.
But Step 29 also isolated the actual missing input: from `C^0` Ricci pinching
alone, without bounded full curvature, we still do not know how to produce
scale-correct central almost-Killing fields.  Cheeger--Fukaya--Gromov supplies
such structure only with bounded `|Rm|`, and Step 11's CZ spike explicitly rules
out deriving such pointwise curvature control from `C^0` Ricci pinching.
Kapovitch--Wilking/Naber--Zhang gives nilpotent short-loop groups, not invariant
metrics or Lie-derivative bounds.  A03's reply #322 confirms that the repaired
negative selected-support flow is not a bridge for positive collapse: its
stationary geometry is negative Einstein, and almost-Killing fields for a
smoothed metric would not automatically transfer to the original positive-pinched
metric.  A01's #323 reports a repair of the negative-route weighted Moser gap by
switching to unweighted `U=a(Rm+G)` quantities; this improves that restricted
4D negative program but does not supply the positive-collapse field.

Therefore the positive branch should not be organized around a single unsupported
collapse bridge.  The other major positive-branch half, largely untouched since
Steps 7--10, has a clearer target-to-Einstein architecture: noncollapsed
curvature concentration in dimension four and the Biquard--Ozuch/Ozuch
Pohozaev obstruction.

## 2. Noncollapsed `P_4^+`: what is conceptually closed and what is not

Consider a positive-pinched sequence

\[
\|\operatorname{Ric}_{g_i}-g_i\|_{op}\leq \delta_i\to0
\]

on closed four-manifolds with a uniform lower volume bound.  Myers gives a
uniform diameter bound, and Bishop--Gromov plus the total-volume lower bound gives
local noncollapse at fixed scales.  Cheeger--Naber gives subsequential convergence
away from a closed codimension-four bad set, with `C^{1,alpha} \cap W^{2,q}`
control on the regular part.  Since the Ricci tensors converge uniformly to `g_i`
in the tensor sense, the regular limit solves `Ric=g` weakly; elliptic
regularity then makes the regular limit smooth Einstein.

If the bad set is empty, the usual smooth convergence/diffeomorphism recovery
makes the conclusion immediate: for large `i`, the underlying smooth manifolds
are diffeomorphic to the smooth Einstein limit, so they themselves carry an
Einstein metric.  In particular, a noncollapsed no-Einstein counterexample to
`P_4^+` cannot be a harmless regular limit; it must form singularities/bubbles.

When singularities occur, the Chern--Gauss--Bonnet and Cheeger--Naber energy
budget bounds the total `L^2` curvature, and nonflat Ricci-flat ALE blowups carry
positive quantized energy.  Thus, in the noncollapsed four-dimensional regime,
the unresolved issue is sharply a finite bubble/orbifold question, not a general
collapse question.  This statement still has two caveats that must not be hidden:

1. Cheeger--Naber alone gives harmonic-radius and regular-set control for bounded
   Ricci metrics; the exact weighted gluing normal form of Ozuch is a theorem for
   **exact Einstein** metrics, not for merely `C^0` Ricci-pinched metrics.
2. First-obstruction vanishing is not automatically full desingularization;
   higher-order obstructions, nondegeneracy, orientation/ALE type, and topology
   recovery remain real obligations.

## 3. Source-grade obstruction facts now in use

The Step-30 knowledge request retrieved Ozuch's `Integrability of Einstein
deformations and desingularizations` as a source-grade object
`Knowledge/objects/papers/Integrability-of-Einstein-deformations-and-desingularizations--8e63541ce32f--b5af64ba3e90/object.md`
(`\cite{ozuch2021integrability}`).  Together with the previously read Ozuch
noncollapsed-degeneration source, it clarifies the exact scope.

Relevant source facts:

- Ozuch's noncollapsed-degeneration paper recalls Anderson--Bando--Kasue--Nakajima:
  normalized exact Einstein 4-manifolds with bounded diameter, volume lower bound,
  and bounded `L^2` curvature converge to Einstein orbifolds; blowups at singular
  points are Ricci-flat ALE spaces (lines 69--80 of
  `Noncollapsed-degeneration-of-Einstein-4-manifolds-I.../object.md`).  It also
  states that the Biquard `R^4/Z_2` Eguchi--Hanson desingularization requires the
  local obstruction `det R=0` (lines 91--94) and that exact Einstein metrics
  sufficiently GH-close to an orbifold are produced by a gluing-perturbation
  procedure (Theorem 0.2, lines 114--124).  These statements are exact-Einstein
  statements.
- Ozuch 2021 defines Taub/Pohozaev preserved quantities using Killing or
  conformal Killing fields on a Ricci-flat cone.  For a cone deformation, the
  obstruction is the vanishing of boundary integrals of
  `Ric_e^{(2)}(h,h)` against cone Killing fields and `r partial_r` (lines 99--109,
  113--115, 299--340).
- Ozuch 2021 Theorem 4.6 (lines 592--600) states that for an exact Einstein
  desingularization with orbifold expansion `g_o=e+H_2+O(r^3)` and ALE expansion
  `g_b=e+H^4+O(r^{-5})`, the boundary integrals
  \[
  \int_{S^3/\Gamma} \operatorname{Ric}^{(2)}_e(H_2,H^4)(Y,\partial_r),
  \qquad
  \int_{S^3/\Gamma} \operatorname{Ric}^{(2)}_e(H_2,H^4)(r\partial_r,\partial_r)
  \]
  vanish.
- For the Eguchi--Hanson metric, Corollary 4.10 (lines 655--662) identifies these
  radial and rotation obstructions with
  \[
  R_e^{+,(1)}(H_2)\,\omega_1^+=0,
  \]
  i.e. in the usual shorthand the first obstruction is `R_+ v=0` for the
  orientation/vector `v` selected by the Eguchi--Hanson bubble.  Existence of
  some orientation killing the obstruction is equivalent to `det R_+=0`, but a
  fixed bubble orientation requires the stronger vector equation `R_+ v=0`.
- Ozuch 2021 also records harmonic vector fields on ALE spaces asymptotic to
  `r partial_r` and to cone Killing fields (lines 564--570).  This matches the
  variational field principle below: the right field is not a naive transplanted
  cone field but the canonical/harmonic/minimizing extension with prescribed
  asymptotics.

## 4. Step-30 checks: EH volume gauge, obstruction algebra, and scaling

I wrote and ran
`workspace/scripts/step30_noncollapsed_bubble_variational_audit.py`, producing
`workspace/data/step30_noncollapsed_bubble_variational_audit.json`.  The script
is exploratory evidence, not a proof.  It records four useful checks.

### 4.1 Eguchi--Hanson leading term is volume-gauge trace-free

In Ozuch's coordinates, the Eguchi--Hanson metric is

\[
\mathbf{eh}=\sqrt{\frac{r^4}{1+r^4}}(dr^2+r^2\alpha_1^2)
            +\sqrt{1+r^4}(\alpha_2^2+\alpha_3^2).
\]

Writing `x=r^{-4}`, the relative coefficients against the flat cone are

\[
(1+x)^{-1/2}-1=-\frac{x}{2}+\frac{3x^2}{8}-\frac{5x^3}{16}+\cdots
\]

for `dr^2` and `alpha_1^2`, and

\[
(1+x)^{1/2}-1=\frac{x}{2}-\frac{x^2}{8}+\frac{x^3}{16}+\cdots
\]

for each of `alpha_2^2`, `alpha_3^2`.  The `r^{-4}` relative trace is therefore

\[
-\tfrac12-\tfrac12+\tfrac12+\tfrac12=0.
\]

So the ordinary mass/volume flux is blind at leading order.  This explains why
naive ADM-type tests stall: the useful object is the anisotropic `H^4` paired
with the orbifold `H_2` curvature term in Ozuch's Taub/Pohozaev obstruction.

### 4.2 First obstruction algebra

For an Eguchi--Hanson orientation `v in Lambda^2_+`, the first obstruction is
`R_+ v=0`.  The script checks sample matrices:

- round `S^4` with `Ric=g` has `R_+=(1/3)I`, no kernel, and nonzero obstruction
  for every `v`;
- positive Kähler--Einstein models such as `CP^2` or `S^2 x S^2` in the relevant
  orientation have eigenvalues `(1,0,0)` and pass the first obstruction for
  kernel orientations;
- `det R_+=0` is not the same as Kähler--Einstein: a spectrum such as
  `(2/3,1/3,0)` also has a kernel.  This preserves the Step-8 correction.

### 4.3 Annular detection scaling

If the bubble coefficient is written as `t^4` and a transplanted cone field has
non-Killing/closeness error `eta`, the strategist's model error
`eta^2 r^4` competes with the bubble flux `t^4`.  Detection requires

\[
\eta^2 r^4 \ll t^4,
\qquad\text{equivalently}\qquad
\eta \ll \frac{t^2}{r^2}.
\]

On intermediate annuli `r=t^alpha`, `alpha<1`, this is quadratically stronger
than naive cone closeness.  This strongly supports replacing transplanted cone
fields by variational minimizers/harmonic extensions with prescribed asymptotic
or boundary data, whose error is controlled by a minimum rather than by raw
annular `C^1` closeness.

### 4.4 Variational almost-Killing operator

The variational functional

\[
J(Z)=\int_\Omega |\mathcal L_Z g|^2\,d\mu
    =4\int_\Omega |\delta_g^* Z|^2\,d\mu
\]

has Euler--Lagrange equation

\[
\delta_g\delta_g^* Z=0
\]

(up to sign convention) for fixed boundary/asymptotic data.  Its closed-kernel is
exactly the Killing fields.  The elementary divergence-free identity from Ozuch
Lemma 1.4 is

\[
\int_{\partial\Omega} T(Z,n)
=\int_\Omega \langle T,\delta^* Z\rangle
=\frac12\int_\Omega\langle T,\mathcal L_Z g\rangle.
\]

For Yau-26 pinched metrics, the tensor to use is not naively `Ric-g` (which is
not divergence-free if scalar curvature varies), but the Einstein tensor with
cosmological constant

\[
\mathcal E_g:=\operatorname{Ric}_g-\frac12 s_g g+\frac{n-2}{2}g.
\]

For an exact `Ric=g` metric this vanishes, and for
`||Ric-g||_{op}\le\delta` it is `O_n(\delta)` pointwise because
`|s-n|\le n\delta`.  It is divergence-free by the contracted Bianchi identity.
Thus a boundary flux identity for `\mathcal E_g` would have an `O_n(\delta)` bulk
error paired only with the variational field, not with derivatives of the Ricci
defect.

This is the main reason the variational construction is attractive: it attacks
both the collapse almost-Killing problem and the bubble first-obstruction
projection without asking for a Ricci-flow smoothing theorem or a pointwise
curvature bound.

## 5. Candidate route comparison after this reassessment

### Route A — Noncollapsed `P_4^+` via variational Pohozaev projection (now highest value)

Goal: prove that a noncollapsed positive-pinched four-dimensional sequence that
forms an ALE/orbifold bubble must satisfy the Ozuch/Biquard first obstruction at
each bubble.  In the `R^4/Z_2` Eguchi--Hanson case this is `R_+v=0`; allowing
bubble orientation gives `det R_+=0` as the first condition.

Why it matters: if the singular set is empty, an Einstein metric on the same
smooth manifold already follows.  If singularities occur, this route attacks the
only noncollapsed obstruction to producing an Einstein desingularization.  Unlike
an abelian-collapse classification, a successful gluing/obstruction chain has a
direct route to an actual Einstein metric on the original topology.

Main gaps:

1. Establish a projection/flux identity for merely `C^0` Ricci-pinched metrics,
   not only exact Einstein metrics in Ozuch's weighted normal form.
2. Construct the correct variational/harmonic vector fields or symmetric test
   tensors with prescribed cone/EH asymptotics and enough scale control.
3. Upgrade first-obstruction vanishing to the complete finite list of
   desingularization conditions, or prove that a remaining higher obstruction
   would itself create a `C^0` Ricci gap.
4. Recover the exact smooth topology of the approximating `M_i` from the bubble
   tree/desingularization pattern.
5. Extend beyond the simplest `R^4/Z_2`/Eguchi--Hanson orientation, or justify
   that this is the only relevant bubble type for the intended no-Einstein
   candidate family.

### Route B — Collapse via variational almost-Killing scale selection (live but less direct)

Step 28--29 show that a central exact/almost-Killing field would control all
4D nilpotent fibre brackets.  The variational principle suggests defining such a
field as a minimizer of `J(Z)` rather than finding it through bounded-curvature
N-structure theory.  Cheeger--Colding almost splitting can provide competitors
on unwrapped covers when the central direction is almost minimizing; if it fails
at the largest scale `L`, the failure itself should encode a bracket lower bound
of order `1/L` (as in the Heisenberg shortcut picture).  This may produce a
scale dichotomy for graded collapse.

This route is valuable but still ends in classification/containment: even if it
proved asymptotic abelianization, Yau-26 still requires an Einstein metric on the
same smooth manifold.  It should therefore remain secondary to Route A in the
immediate next work.

### Route C — Toric fixed-strata `#_k(S^2 x S^2)` formal adversary

The toric `alpha`-family remains the best explicit positive-collapse stress test.
It is compatible with all local rod/corner identities checked so far, but no
global smooth metric or no-Einstein topology result exists.  It is a laboratory
for singular fixed-strata collapse, not yet a proof or refutation.

### Route D — Restricted negative Ishida--LeBrun flow route

A01/A03's recent messages repair several analytic defects in the conditional
negative branch.  The current state appears to be: above-critical topological
excess gives a direct gap; critical/near-critical cases still depend on a
selected-support flow theorem producing simultaneous control.  Even if completed,
this is a special four-dimensional negative gap and cannot settle the positive
branch or all dimensions.  It should be monitored and used for techniques, not
made the main route for the full Yau-26 target.

### Route E — High dimensions

No inspected source supplies a high-dimensional closed smooth manifold known to
admit no Einstein metric of any sign.  Refutation in `n>=5` would require a new
no-Einstein theorem plus tight Ricci pinching; proof is entangled with the broad
Einstein-existence problem.  The 4D positive branch remains the clearest place
where the exact pinching hypothesis interacts with known obstruction theory.

## 6. Concrete next work

The next strongest work should be Execute by a Constructor/Actuator on Route A,
with independent Preceptor review afterward.  The immediate tasks are not final
writing but mathematical construction and falsification:

1. **Derive the divergence-free pinched boundary identity.**  For a compact
   annulus `Omega` in a 4D positive-pinched metric, set
   \(
   \mathcal E_g=Ric_g-\frac12s_g g+g
   \)
   (since `n=4`, `(n-2)/2=1`).  Prove exactly
   \[
   \int_{\partial\Omega}\mathcal E_g(Z,n)
   =\frac12\int_\Omega\langle\mathcal E_g,\mathcal L_Zg\rangle,
   \]
   and record the resulting bound in terms of `delta`, `Vol(Omega)`, and the
   variational energy of `Z`.  This is the `C^0`-Ricci-safe replacement for
   informal `Ric-g` pairings.
2. **Build the model `R^4/Z_2` Eguchi--Hanson computation explicitly.**  Starting
   from Ozuch 2021 lines 592--662, compute the boundary integrals for
   `H^4=-theta_1^- o omega_1^+/(2r^4)` and a general Bianchi-gauge quadratic
   `H_2`; verify that the radial plus rotation conditions are exactly
   `R_+ omega_1^+=0`.  A symbolic script and a small Lean algebra kernel for the
   final `3x3` obstruction matrix would be worthwhile.
3. **Define the variational field problem on a flat/EH annulus.**  Minimize
   `int |L_Z g|^2` with prescribed outer cone rotation or `r partial_r`
   asymptotics and inner regular/EH boundary behavior.  Compare its energy and
   boundary flux with the naive cone field.  The decisive question is whether the
   minimized error detects the `t^4` obstruction without requiring annular
   closeness `eta << t^2/r^2`.
4. **Separate first-order and full gluing closure.**  If the first obstruction is
   forced to vanish for pinched metrics, identify which higher-order Ozuch
   obstructions remain and whether a nonzero higher obstruction also creates an
   order-one or scale-detectable `C^0` Ricci defect.  Do not claim an Einstein
   metric from `det R=0` alone.
5. **Keep collapse route in reserve.**  If Route A exposes a fatal gap, return to
   variational almost-Killing scale selection for collapse.  Do not pursue
   pointwise horizontal-twist bounds as a primary 4D target; Step 29's local jet
   shows that target is likely false and not needed for bracket control.

## 7. Current resolution state

The full Yau-26 proposition is still unresolved.  Step 30 changes the route
weighting: the Bochner-collapse program remains a useful live route, but the
noncollapsed four-dimensional positive branch now has the clearest direct
path from Ricci pinching to actual Einstein existence.  Its decisive bottleneck
is a variational Pohozaev/Komar projection that works for `C^0` Ricci-pinched
metrics and recovers the Ozuch/Biquard ALE first obstruction without assuming the
exact Einstein weighted normal form.  The next step should attack that bottleneck
mathematically rather than continue searching for a curvature-smoothing source of
almost-Killing fields.

# Step 50: Reversed-bubble estimate and positive-branch hardness reduction

Session S0910A02. Agent3 / Actuator. Phase Execute.

## 0. Scope

The active target is still the full Yau--26 proposition: for every dimension
\(n\ge2\), decide whether a dimension-only two-sided Ricci pinching interval
forces the underlying closed smooth manifold to carry *some* Einstein metric.
This note verifies a four-dimensional, positive-sign, noncollapsed local
construction and its consequence.  It does not settle positive collapse, the
negative branch, dimensions \(n\ge5\), or Lean formalization.

Step 49's main correction survives this check: for the product quotient
\((S^2\times S^2)/\mathbb Z_2\), once the vector **first** Ozuch obstruction is
killed at each \(A_1\) point, refined Eguchi--Hanson replacement metrics already
satisfy \(\|\operatorname{Ric}-\Lambda g\|_{op}\to0\).  Higher exact-Einstein
obstructions are not visible to the Yau--26 \(C^0\) Ricci-endomorphism norm.
The extra point verified here is the mixed-row/reversed-bubble case.

## 1. Source-checked local estimate

Use the scale convention
\[
  \epsilon=\text{length scale},\qquad t=\epsilon^2=\text{metric scale},
\]
so on the bubble region \(g_t\sim t\,g_{EH}\).  For a \((0,2)\)-tensor \(T\),
\[
  \|g_t^{-1}T\|\sim t^{-1}\|g_{EH}^{-1}T\| .
\]

The four-dimensional Ozuch source provides the relevant \(A_1\)/EH structure:

- Negative-orientation EH metrics are still isometric/homothetic to ordinary EH,
  but with the opposite orientation: lines 372--376 define
  \(\mathbf{eh}_{\zeta^-}\), state that it is isometric to \(|\zeta|\mathbf{eh}\),
  and give its opposite-orientation asymptotic term.
- Lines 496--514 define the refined tensors
  \(\underline h_2(\zeta^\pm)\), \(\underline h_4(\zeta^\pm)\), and give the
  vector first obstruction
  \[
    \lambda_k(\zeta^\pm)
    =c\langle \mathbf R^\pm(H_2)\zeta^\pm,\zeta_{(k)}^\pm\rangle .
  \]
  Thus a reversed bubble has the same analytic estimate but tests \(R_-\), not
  \(R_+\).
- Lines 715--726 define the approximate Einstein-modulo-obstructions metric by
  gluing \(\mathbf{eh}_{\zeta_j^\pm}+\underline h_{j,2}+\underline h_{j,4}\) at
  the singular points and give uniform controls on the local and gluing regions.
- Lines 783--789 explicitly say the EH-region estimate is the one from Biquard
  2013, Section 14, and conclude the weighted projected defect bound
  \(O(|\zeta|^{3/2-\beta/4})\).  I could not retrieve Biquard's original paper
  directly in this step; the session therefore cites Ozuch's internal statement
  plus his Biquard pointer for the four-dimensional source.  MV lines 456--514
  provide the clean model exponent \(t^2\rho^2\), but MV is a higher-dimensional
  Calabi source and is only used as exponent calibration.

In the clean model estimate one has, after subtracting the first obstruction,
\[
 \big|\operatorname{Ric}_{g_t}-\Lambda g_t-t\lambda\chi_t o\big|_{EH}
   \le C t^2\rho^2 .
\]
Raising an index with \(g_t^{-1}\) gives
\[
 \|\operatorname{Ric}_{g_t}-\Lambda g_t-t\lambda\chi_t o\|_{op,g_t}
   \le C t\rho^2 .
\]
This is \(O(t)\) on the fixed EH core and \(O(t^{1/2})\) on the standard damage
annulus \(\rho\sim t^{-1/4}\).  If one quotes only Ozuch's displayed weighted
bound, the safe rate is \(O(t^{1/2-\beta/4})\) for small positive \(\beta\), still
converging to zero.  The rate itself is less important than the order separation:
\[
  t\lambda o \mapsto O(1),\qquad t^2\mu o\mapsto O(t),
\]
under the operator norm.  Hence a nonzero first obstruction prevents tight
operator Ricci pinching, while second and higher exact-Einstein obstruction
terms do not.

This exponent arithmetic is recorded in
`workspace/data/step50_reversed_bubble_estimate_and_reduction.json`, produced by
`workspace/scripts/step50_reversed_bubble_estimate_and_reduction.py`.

## 2. Reversed bubbles in the product quotient

For the product Einstein metric on \(S^2\times S^2\), Steps 44--45 verified
\[
  R_+=R_- = \operatorname{diag}(\Lambda,0,0).
\]
Thus both chiral blocks have the same two-dimensional kernel
\(\operatorname{span}\{e_2,e_3\}\).  At each of the four \(A_1\) singularities of
\((S^2\times S^2)/\mathbb Z_2\), and for either orientation assignment,
choose \(\zeta_j\in\ker R_{\varepsilon_j}(p_j)\).  Then
\[
  R_{\varepsilon_j}(p_j)\zeta_j=0
\]
and all vector first obstructions vanish.

The sole non-routine mixed-row point is now explicit: reversed EH is the same
unoriented Riemannian ALE metric, so its pointwise/weighted estimates transfer;
but its attaching map reverses the orientation of the \(\mathbb RP^3\) link and
its first obstruction uses \(R_-\).  Since the product quotient has
\(R_-=\operatorname{diag}(\Lambda,0,0)\), kernel choices kill this obstruction
for reversed bubbles just as \(R_+\)-kernel choices do for compatible bubbles.
At leading refined order, the four points do not interact because the gluing
balls are disjoint and each obstruction coefficient is a local boundary flux;
global Kuranishi/inter-point terms occur at higher order and are invisible to
the limiting \(C^0\) operator pinching once the local first obstructions vanish.

Therefore, for any fixed finite orientation assignment for the four nodes,
there are smooth metrics \(g_t\) on the corresponding smooth resolution
\(M_r\) such that
\[
  \sup_{M_r}\|\operatorname{Ric}_{g_t}-\Lambda g_t\|_{op,g_t}
   \le C t^{1/2} \quad\text{(clean model),}
\]
or at least \(O(t^{1/2-\beta/4})\) under the displayed Ozuch weighted estimate.
Either way \(\delta_+(M_r)=0\) in the sense that \(M_r\) carries a sequence with
\(\|\operatorname{Ric}-\Lambda g\|_{op}\to0\).

## 3. Minimal topology needed for the reduction

For the diagonal half-turn quotient, Armstrong's theorem gives
\(\pi_1((S^2\times S^2)/\mathbb Z_2)=0\): the covering space is simply connected
and the nontrivial group element has fixed points, so \(G/I=0\) (source lines
31--32 in the Armstrong-object note).  Removing the four conical neighborhoods
and filling them by the simply connected \(\pm2\)-disk bundles over \(S^2\)
preserves simple-connectedness by van Kampen: the quotient orbifold itself is
obtained by filling the same boundary components by contractible cones, so the
boundary \(\pi_1(\mathbb RP^3)\) images normally generate the complement
fundamental group; the smooth disk-bundle fillings kill the same images.

Euler and signature bookkeeping then gives, for \(r\) reversed bubbles,
\[
  \chi(M_r)=8,
  \qquad (b_+(M_r),b_-(M_r))=(1+r,5-r),
  \qquad \tau(M_r)=2r-4 .
\]
The five rows are:

| reversed nodes \(r\) | \((b_+,b_-)\) | status |
|---:|---:|---|
| 0 | \((1,5)\) | endpoint/all-compatible Del Pezzo-type calibration; known Einstein at diffeotype level, not a no-Einstein target |
| 1 | \((2,4)\) | mixed wall row; PSC, strict HT, ordinary SW obstruction absent |
| 2 | \((3,3)\) | balanced mixed wall row; spin/evenness depends on boundary gluing, and if even is homeomorphic to \(\#_3(S^2\times S^2)\) |
| 3 | \((4,2)\) | mixed wall row; PSC, strict HT, ordinary SW obstruction absent |
| 4 | \((5,1)\) | orientation reverse of endpoint row; harmless for Yau--26 |

The all-compatible toric resolution was checked as a calibration.  The corrected
lattice probe
`workspace/data/step50_mixed_resolution_lattice_probe.json` has a smooth fan,
Picard determinant \(-1\), signature \((1,5)\), odd form, and four disjoint
\((-2)\)-curves.  This supersedes the bad first probe in
`step50_toric_fan_spin_probe.json`, whose determinant \(-1296\) came from using
linear-equivalence representatives in the degenerate full divisor pairing.

The discriminant-glue probe
`workspace/data/step50_discriminant_glue_probe.json` suggests why Step 45 was
right not to assert a unique spin type for \(r=2\): in the same-fractional-glue
model, some choices of two reversed nodes are even and others odd.  This is only
an algebraic model of boundary gluing, not a Kirby proof, so the exact smooth
classification remains open.  For the reduction below, that exact smooth type is
not needed.

## 4. Conditional-hardness reduction for \(P_4^+\)

Let \(P_4^+\) denote the positive normalized branch of Yau--26 in dimension four:
there exists \(\delta_4>0\) such that
\[
  \|\operatorname{Ric}_g-g\|_{op,g}\le\delta_4
  \Longrightarrow M^4\text{ carries an Einstein metric.}
\]
The construction above gives, for each actual mixed smooth manifold \(M_r\) with \(r=1,2,3\), a sequence \(g_t\) with
\(\|\operatorname{Ric}_{g_t}-\Lambda g_t\|_{op}\to0\).  After a constant rescale,
these metrics enter any positive branch interval.  Therefore:

> **Reduction.** If \(P_4^+\) is true, then every mixed product-quotient
> resolution \(M_r\), \(r=1,2,3\), must carry some Einstein metric.

This is not a refutation and not an existence theorem.  It is a hardness wall:
current tools in this session cannot decide the Einstein status of the mixed
rows.  The reasons are concrete:

1. The constructed metrics have positive scalar curvature for small \(t\) (indeed
   scalar curvature tends to \(4\Lambda>0\) in the normalized positive branch).
2. For the mixed rows \(b_+>1\).  Standard Seiberg--Witten invariants are
   diffeomorphism invariants for \(b_+>1\), but positive scalar curvature implies
   the SW moduli spaces are empty for generic PSC metrics by the Lichnerowicz /
   Weitzenböck argument (Six Lectures source lines 186--191).  LeBrun's Yamabe
   source also states that usual SW invariants vanish when \(Y(M)>0\) (lines
   41--42).  Thus the SW/monopole-based obstructions used elsewhere in this
   session cannot be applied directly to these mixed rows.
3. Hitchin--Thorpe is satisfied for all rows: \(2\chi=16>3|\tau|\) for
   \(|\tau|\le4\).  Hence the universal topological obstruction is silent.
4. Endpoint Del Pezzo rows are known-Einstein calibrations by the LeBrun--Ozuch
   source's diffeotype-level statement (lines 157--170), but the mixed rows have
   \(b_+\ge2\) in every listed orientation and are not covered by that Del Pezzo
   existence theorem.

The balanced \(r=2\) row is especially recognizable if the even boundary-gluing
case is realized: it is then homeomorphic to \(\#_3(S^2\times S^2)\), whose
Einstein existence is not settled by the tools in this session.  But the
reduction does not rely on proving that exact diffeomorphism type; it applies to
whatever smooth mixed-resolution manifolds the explicit gluing actually produces.

## 5. Relation to peer Q-Gorenstein smoothing message #378

A01 #378 reports a different, valuable mechanism for **general-type**
product-quotient surfaces: kernel-directed EH parameters can correspond to
complex \(A_1\) smoothings, and if a global Q-Gorenstein smoothing exists then
Aubin--Yau gives a negative Kähler--Einstein metric on the smooth fiber, which
is diffeomorphic to the simultaneous resolution.  I read
`Sessions/S0910A01/workspace/notes/step49_qg_smoothing_einstein_existence_mechanism.md`.
That note itself distinguishes the positive \(S^2\times S^2\) quotient case: its
§6 says the Aubin--Yau ample-canonical mechanism does not cover the positive
product-quotient rows, and mixed chirality may be non-holomorphic rather than a
Q-Gorenstein smoothing.

Thus #378 does not invalidate the Step-50 positive-branch reduction.  It is a
live existence direction for negative/general-type product-quotient surfaces and
possibly for holomorphic one-chirality rows.  For the mixed positive rows here,
no global smoothing/Einstein-existence theorem has been verified.

## 6. What this settles and what it does not

Settled by this step, modulo the cited four-dimensional EH estimate as stated in
Ozuch/Biquard:

- Reversed EH replacements obey the same local estimates as compatible EH
  replacements, but test \(R_-\) rather than \(R_+\).
- At the bi-Kähler product quotient, \(R_+=R_-\), so kernel directions kill the
  first obstruction for every chirality assignment.
- Each mixed row \(r=1,2,3\) supplies a well-defined simply connected smooth
  four-manifold with \(b_+\ge2\), positive-scalar-curvature near-Einstein input
  metrics, and no applicable SW or Hitchin--Thorpe Einstein obstruction in the
  current record.
- Therefore the positive noncollapsed product-quotient arc reaches a ceiling:
  proving \(P_4^+\) must include an Einstein-existence theorem for these mixed
  manifolds; refuting \(P_4^+\) would require a new no-Einstein theorem on a PSC
  \(b_+\ge2\) four-manifold, beyond the current SW/HT toolkit.

Not settled:

- the normalized H4-dual necessity theorem for arbitrary pinched noncollapsed
  bubbling sequences;
- the exact smooth diffeomorphism types and spin refinements of all mixed rows;
- any no-Einstein theorem for a mixed row;
- positive collapse in dimension four;
- the negative branch, including A03 #379's improved normalized Yang-flow route,
  which remains a separate restricted branch not independently checked here;
- dimensions \(n\ge5\) and the final Lean proof obligation.

## 7. Files

- `workspace/scripts/step50_reversed_bubble_estimate_and_reduction.py`
- `workspace/data/step50_reversed_bubble_estimate_and_reduction.json`
- `workspace/scripts/step50_mixed_resolution_lattice_probe.py`
- `workspace/data/step50_mixed_resolution_lattice_probe.json`
- `workspace/scripts/step50_discriminant_glue_probe.py`
- `workspace/data/step50_discriminant_glue_probe.json`
- Superseded bad probe marked in `workspace/data/step50_toric_fan_spin_probe.json`

No branch of the full Yau--26 proposition is proved or refuted by this step.

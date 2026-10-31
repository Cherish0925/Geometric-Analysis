---
title: Einstein Gaps on Four-Manifolds
subtitle: Constructions, compatibility estimates, and current sharpness problems
date: 7 October 2026
header-includes:
  - \usepackage{esint}
---

# Mathematical setting

The common problem is to determine how closely a smooth four-manifold can
approach Einstein geometry, under specified topological and actual gauge-field
constraints. The work concerns uniform lower bounds, optimal values, geometric
constructions, and the distinction between a vanishing infimum and an exact
Einstein metric. These questions are related but not equivalent.

This synthesis records the mathematical contributions of Sessions S1003A01
and S1003A02. It separates their inherited theory from new constructions and
estimates, and separates conclusions about all competing metrics from
conclusions about marked cells or restricted geometric classes. The full
proof texts and computational sources accompany it. The snapshot was taken
on 7 October 2026 at 10:47:26--10:47:27, Asia/Shanghai; the latest included
research notes are A01 Step 38 and A02 Step 44.

On a closed oriented four-manifold set
\[
 P(g)=\int_M|\operatorname{Ric}^{\circ}|^2,\quad
 S(g)=\int_Ms^2,\quad R(g)=P(g)+\tfrac14S(g),\quad
 T_\pm=2\chi\pm3\tau.
\]
With the operator norm convention for Weyl curvature,
\[
 4\pi^2T_\pm=\frac{S}{24}+2\int|W^\pm|^2-\frac P2.
\]
For \(R>0\), the normalized defects are
\[
 \mathcal J(g)=\frac{4P}{R},\qquad
 \mathcal E(g)=4-\frac{(\int s)^2}{VR}
 =\mathcal J(g)+\frac{S-(\int s)^2/V}{R}.
\]
Write \(\alpha(M)=\inf_g\mathcal E(g)\). A Ricci-flat metric has
\(\mathcal E=4\), while \(\mathcal J\) is undefined there. On a constant
scalar-curvature metric with \(R>0\), the two defects agree.

For surgery families,
\[
 M=X\#k\overline{\mathbb{CP}}^{2}\#\ell(S^1\times S^3),\qquad
 A=c_1^2(X)>0,\quad Q=k+4\ell,\quad h=Q/A.
\]
The original balanced problem includes both blow-ups and handles. A theorem
for pure blow-ups \(\ell=0\) is not automatically a theorem for that problem.

Local raw energies use a different notation:
\[
 J_\lambda(g)=\int_C|\operatorname{Ric}-\lambda g|^2.
\]
Thus the notes' \(J_6\), on a background \(\operatorname{Ric}=-6g\), means
\(\int|\operatorname{Ric}+6g|^2\), not the normalized \(\mathcal J\).
Numerical cell costs are usually divided by \(8\pi^2\).

# Inherited analytical backbone

The following are inputs to these Sessions, not newly established results of
the two runs:

* The single-solution finite-parameter estimates and the N1 normalized gap,
  including the explicit negative-class-square and class-square-shortfall
  versions.
* The I40/I41 coercivity estimate
  \[
  \Sigma\le C\{\Pi+\sqrt{\Pi Y}\},\quad
  \Sigma=S-32\pi^2p,\quad \Pi=P+D_2,\quad Y=(T_+-a^2)_+.
  \]
* The matched linear scale \(ch\le\alpha\le4h/(1+h)\) on the specified
  balanced families, and the small-\(h\) variational reduction
  \[
  \alpha_j=4\frac{\inf_gP(g)}{8\pi^2A_j}+O(h_j^2).
  \]
* The finite-topological-density endpoint theorem, with a constant depending
  on an upper bound for \(\chi/A\).
* The all-metric pure-handle sharp value, classical monopole suppliers, and
  the previous relative Chern--Weil and complete-cell transfer framework.

The full inherited manuscript is
[Curvature Realizability](sources/Skills/geometric-analysis/research/Curvature_Realizability.tex).
Its editable sections and source library are also included. Material copied
back into the Skill on 4 October, notably the strict cheap-cell construction,
remains an output of these Sessions rather than an older input.

The relevant classical distinction is between \(\inf R\) and \(\inf P\).
LeBrun's exact Ricci-energy calculations and recovery constructions do not
allow subtraction of independently attained infima. Likewise, the
Malchiodi--Malizia Weyl-energy improvement does not by itself control the
additional scalar contribution to \(P\) or to a raw Einstein residual.

# A strict improvement of the balanced asymptotic upper bound

## The complete cheap cell

A01 and A02 construct and check a smooth ordinary \((-1)\)-blow-up cell with
an exact complex-hyperbolic outer collar. The useful geometry is triaxial and
perpendicular to the usual Kähler alignment. The original argument checks
positive definiteness, bolt regularity, ordinary blow-up topology relative to
the marked boundary, and finite-order contact with the CH metric. A further
cutoff smoothing has arbitrarily small energy loss.

The current degree-20 profile, with \(x_0=3/100\) and outer parameter
\(X=128\), has the recorded interval enclosure
\[
 \frac{J_6}{8\pi^2}
 \in[0.995670030344086466\ldots,
       0.995670030355130639\ldots].
\]
In particular there is a fixed \(\eta>0\) such that the rescaled smooth cell
has cost at most \(8\pi^2(1-\eta)\). The analytic admissibility and smoothing
argument is separate from the interval integration of a specific profile.

For appropriately selected residual-finite covers, sufficiently many
disjoint marked balls admit insertion of this cell. The handle pieces are
chosen at shrinking scales so that their aggregate errors are \(o(Q)\).
For the balanced ratios \(k/Q\to2/9\), \(\ell/Q\to7/36\),
\[
 \limsup\frac{\alpha(M_j)}{h_j}
 \le 4-\frac89\eta<3.9961512<4.
\]
The bookkeeping is \(28/9+(8/9)p_{1,0}\), not \(4p_{1,0}\), where
\(p_{1,0}\) is the normalized single-blow-up cost.

This changes the answer to a substantive question: the standard shrinking
recovery is not asymptotically optimal on these selected balanced families.
It does not identify the sharp coefficient or establish the same bound for
every prescribed covering tower. Refining the interval enclosure is a
strengthening of the same construction, not a second independent mechanism.

Proofs: [A01 Step 10](sources/Sessions/S1003A01/workspace/notes/step10_rigorous_subthreshold_cell_and_O11.md),
[A01 Step 11](sources/Sessions/S1003A01/workspace/notes/step11_independent_review_O11_and_mixed_cost.md),
[A02 independent cell calculation](sources/Sessions/S1003A02/workspace/notes/step11_subthreshold_perpendicular_cell.md),
and [A01 Step 33, section 6](sources/Sessions/S1003A01/workspace/notes/step33_surgery_slope_law_and_ASD_retention.md).

## Transfer to non-ball-quotient Kähler--Einstein backgrounds

A01 subsequently transfers the construction to compactifications of ramified
arithmetic ball-quotient covers. Their smooth negative KE metrics have
\[
 A_m=c_1^2(\bar X_m),\qquad
 \Delta_m=3\chi(\bar X_m)-A_m>0,\qquad \Delta_m/A_m\longrightarrow0.
\]
The strict Chern-number inequality shows that these compact surfaces are not
compact ball quotients.

The argument uses smooth convergence on a fixed compact region away from
the compactification divisor. Galois lifts provide \(d_m\asymp A_m\)
disjoint insertion regions with the same \(C^2\) error \(\varepsilon_m\to0\).
A fixed annular buffer joins the exact CH cell to the KE host, at raw
Ricci-defect cost \(O(\varepsilon_m^2)\) per insertion. Across \(O(Q_m)\)
insertions this is \(o(Q_m)\); the unchanged KE bulk contributes no raw
Einstein defect.

If \(\Delta_m/Q_m\to r\in[0,1)\) and the surgery parameters are balanced,
\[
 \limsup\frac{\alpha(M_m)}{h_m}
 \le4-\frac{8\eta}{9}(1-r),
\]
while the inherited actual-field theorem supplies a positive linear lower
bound. This is a new family and transfer argument, not a second cheap-cell
construction.

More generally, put
\[
 \theta=k/Q,\qquad r=\Delta/Q,\qquad \sigma=4r+18\theta.
\]
The characteristic numbers give
\[
 T_+=A-Q,\qquad \frac{3T_-}{A}=1+(\sigma-3)h.
\]
On the supplied families the existing lower theory and the new recovery give
\[
 \liminf\frac\alpha h\ge
 \max\left\{\frac43(3-\sigma)_+,\frac{18}{19}(4+c_0-\sigma)_+\right\},
 \qquad
 \limsup\frac\alpha h\le4(1-\eta\theta).
\]
The lower information depends on \(\sigma\); this separated recovery depends
on \(\theta\). Neither formula identifies the sharp transition or minimum.
The loss of the balanced saving at \(r=1\) is not a general existence barrier.

Proofs: [ramified transfer](sources/Sessions/S1003A01/workspace/notes/step31_ramified_KE_transfer_and_interface_simplification.md)
and [slope law](sources/Sessions/S1003A01/workspace/notes/step33_surgery_slope_law_and_ASD_retention.md).
These results use a fixed region away from the divisor; they do not depend
on the later, incomplete near-divisor Calabi-cap transfer.

# Endpoint estimates without a density bound in a specified region

For an actual class, let
\[
 D_\beta=(1+\beta^{-1})S+6(\beta+1)\int|W^+|^2-72\pi^2p,
 \quad
 \kappa_\beta=\fint|\operatorname{Ric}+g|^2+D_\beta/V.
\]
Fix \(\vartheta<3/4\). A02's L-prime statement assumes a fixed \(\operatorname{Spin}^c\)
structure supplying an unperturbed monopole on every metric of the chosen
conformal class, with
\[
 p\ge A>0,\qquad a^2\ge T_+,\qquad T_+\le\vartheta A.
\]
It proves
\[
 \kappa_\beta(g)\ge c_L(\vartheta)>0
 \quad\text{for every metric in that class and every finite }\beta\ge2.
\]
The same constant works on the entire finite half-line; this is not a bound
only on a compact parameter interval. There is no Euler-density assumption.

The large-parameter part follows by combining Chern--Weil with LeBrun's
weighted estimate. The decisive numerator is
\[
 N_\vartheta(\beta)=
 (3/4-\vartheta)\beta^2+(1/2-11\vartheta/4)\beta+6-\vartheta,
\]
with discriminant
\[
 \frac{57}{16}(\vartheta-2/3)(\vartheta+142/19).
\]
At \(\vartheta=2/3\), it equals \((\beta-8)^2/12\). For
\(2/3\le\vartheta<3/4\), the inherited finite-parameter non-saturation
theorem handles the bounded bad interval, and a conformal comparison returns
to the original metric. The constant degenerates as \(\vartheta\uparrow3/4\).

For a minimal general-type Kähler surface with \(p_g\ge1\), sign averaging
and a split according to the blow-up ratio combine this result with the
finite-density theorem. The resulting Corollary K gives, on all its blow-ups,
\[
 \kappa_\beta(g)\ge c_K(\beta-2)^2/\beta^2
\]
for all metrics and all \(\beta\ge2\). This expands the actual endpoint
range. The unrestricted high-density endpoint remains open, and a bound for
\(\kappa_\beta\) is not a bound for \(\alpha\): field alignment and Einstein
proximity measure different conditions.

Proof entry: [A02 Step 6](sources/Sessions/S1003A02/workspace/notes/step6_theorems_and_O11_rotation.md),
with the full conformal argument in
[Step 5 verifier integration](sources/Sessions/S1003A02/trace/ttcs/results/step5_ttcs01_verifier1_integration.md).

# General background response and conformal selection

## Burns insertion on an arbitrary fixed background

A02's Theorem F takes a closed oriented smooth Riemannian four-manifold
\((M,g)\), a point \(p\), and a unit self-dual form \(\zeta\in\Lambda_p^+\).
For a Burns insertion with exceptional area \(\pi x\) and cutoff radius
\(x^{1/5}\), it gives
\[
 P(\widehat g_x)=P(g)+8\pi^2\{1-xR_p^+(\zeta,\zeta)\}+O(x^{6/5}),
 \qquad R^+=W^++\frac{s}{12}I.
\]
The remainder constant depends on local background control. The corresponding
raw Einstein-residual formula requires an Einstein background.

The proof combines the scalar-flat, self-dual-flat linear Burns tail with its
cut-annulus transgression and separate estimates on the core, intermediate
region, and cutoff region. It identifies the first-order dependence on
ambient curvature and insertion direction. For a negative KE background,
the perpendicular directions lie in \(\ker R^+\); on a real hyperbolic
background every direction has positive first-order cost.

This is an upper construction, not a lower bound for the infimum over all
cells. Its remainder is larger than a possible \(x^2\log(1/x)\) contribution,
so it does not prove the more delicate kernel-direction saving uniformly on
general backgrounds.

Proof: [A02 Step 20](sources/Sessions/S1003A02/workspace/notes/step20_burns_response_and_neck_quantization.md).

## Conformal selection without a symmetry assumption

A01 treats every smooth complete connected cell that is exactly CH outside
a compact set, with normalization \(\operatorname{Ric}=-6g\). No sign
condition is imposed on the scalar curvature in the core. Ordered global
barriers, exhaustion, and the maximum principle give a unique positive
solution
\[
 -6\Delta_gu+s_gu+24u^3=0,\qquad u\to1,
\]
so that \(\widehat g=u^2g\) has scalar curvature \(-24\). For every
\(4<m<2+2\sqrt3\), its derivatives decay as \(O(e^{-mr})\).
This removes the linear boundary transgression and yields
\[
 P(g)-P(\widehat g)=24\int|\nabla u|^2+3\int(\Delta u/u)^2.
\]
Together with cutoff recovery, it proves equality of the exact-CH-ended
\(P\)- and \(J_6\)-infima and the corresponding scalar-normalized aCH
infimum for \(2<\mu<2+2\sqrt3\).

This removes the diagonal, symmetry, and scalar-sign assumptions from that
local variational reduction. It does not prove attainment or determine the
unrestricted cell value. Arbitrary asymptotically CH inputs require separate
forcing and decay hypotheses.

Proof: [A01 Step 22](sources/Sessions/S1003A01/workspace/notes/step22_exact_CH_conformal_reduction.md).

# An exact Einstein filling with nonstandard conformal infinity

A02's Theorem E constructs a complete real-analytic diagonal Bianchi--IX
metric on \(\mathcal O(-1)\to\mathbb{CP}^1\) with
\[
 \operatorname{Ric}=-6g,
 \qquad \rho_\infty\in[2.19013,2.19242].
\]
The conformal infinity is a nonstandard Rossi CR sphere, and the convergence
rate is at least \(O(e^{-1.99t})\).

The argument consists of an analytic Fuchsian bolt construction, exact
constraint propagation, interval transport of forty initial boxes, opposite
exit faces of a verified block, a Wazewski continuation argument, and
quadratic drift control at infinity. An off-bolt interval calculation shows
that both chiral Weyl blocks have simple spectrum. Analyticity then excludes
a conformally Kähler structure on any nonempty open set, in either
orientation.

This is a precise existence result with a computer-assisted proof component.
It is independent of the cheap-cell upper construction. Because
\(\rho_\infty\ne1\), it is not a zero-cost filling with the prescribed
standard CH boundary. In particular it does not show that the marked-cell
infimum vanishes.

Proof and data: [A02 Step 15](sources/Sessions/S1003A02/workspace/notes/step15_ach_projected_theory.md),
[Rossi enclosure](sources/Sessions/S1003A02/workspace/data/ach_capd/rossi_enclosure_b0.8.json),
[Weyl discriminants](sources/Sessions/S1003A02/workspace/data/ach_capd/weyl_discriminant_t0.5.json).

# The actual-field mechanism behind a saving

The newer A02 analysis works with simultaneous actual monopole solutions for
the full exceptional-sign family on the same scalar-\(-4\) metric. The input
includes the required simple-type identity and, for handle summands, the
appropriate higher-type or holonomy supplier. Set
\[
 \rho_\epsilon=|\Phi_\epsilon|^2\in[0,2],\quad
 n_\epsilon=\psi_\epsilon/\rho_\epsilon,\quad
 \mathfrak S=8\pi^2Q-P.
\]
On the nonzero-spinor set, decompose the normalized spinor derivative into
amplitude, phase, Lee, and Nijenhuis components. The pointwise Dirac equation
fixes the Lee component; it does not fix the Nijenhuis component. Retaining
the amplitude Weitzenböck identity and the same-family Walsh terms gives
\[
 \mathfrak S=
 \frac12\mathbb E_\epsilon\int\rho_\epsilon^2
 |\nabla n_\epsilon|_{\mathcal W_2}^2-\mathcal B,
 \qquad \mathcal B\ge0.
\]
Here \(\mathcal B\) is the explicit sum of amplitude, phase/Lee, Weyl-model,
and Walsh losses in the source theorem. The equivalent Weyl expression
identifies the signed interaction with \(W^+-W_{0,\epsilon}\).

Consequently, if an admissible simultaneous family is integrable on its
nonzero sets, then \(P\ge8\pi^2Q\). Conversely, a fixed proportional saving
forces a comparable amount of weighted Nijenhuis energy. This relates the
construction-side saving to genuine gauge fields; it does not yet bound
that saving on all competing geometries.

The paired-field analysis also identifies why exceptional sign changes do
not automatically add a new positive cost. The relative twisting line has
class \(\pm E_i\), not \(\pm2E_i\); its fixed negative square is carried by
the anti-self-dual part, while amplitude and directional differences see
different components. Recounting a Walsh sector as an independent positive
charge would count the same information twice.

Proofs: [paired-field scope](sources/Sessions/S1003A02/workspace/notes/step38_kahler_and_paired_field_scope.md)
and [Nijenhuis and Weyl identities](sources/Sessions/S1003A02/workspace/notes/step40_nijenhuis_form_and_pointwise_exhaustion.md).

# Boundary mechanisms and limitations of local estimates

The Sessions develop exact chiral transgressions on diagonal annuli,
boundary-corrected almost-Kähler formulas, CR pinning, standard-CR truncation,
exterior ground states, and joint quadratic estimates. These have three
distinct uses:

1. They compute costs for specified marked boundaries and identify zero
   modes that carry interface data without raw curvature cost.
2. They exclude particular controlled escape channels, including specified
   nearly Euclidean necks and developed-Rossi-to-product connectors.
3. They identify the hypotheses needed before a local cost can be used in a
   global lower bound.

For example, the corrected AK expression is
\[
 \widehat P[t_0,t_1]=\int_{t_0}^{t_1}L_{AK}+B(t_1)-B(t_0).
\]
A positive bulk AK term can be cancelled by the boundary term; it is not an
additional independent charge. The diagonal control calibration similarly
has the exact form
\[
 \widehat P=\Delta\mathfrak b_++\int L(c-c^*),\qquad L>0.
\]
Its calibrated trajectories are ASD scalar-flat trajectories. The exact
calibration does not turn sampled trajectory destinations or numerically
optimized path costs into uniform lower bounds for all paths.

The pure-handle marked-cell infimum is \(32\pi^2\ell\), approached but not
attained for \(\ell>0\). This is a useful localization of the inherited
global handle theorem. Mixed-cell additivity and identification of cell
specific energy with the unrestricted closed-manifold optimum remain open.

Sources: [A01 AK boundary correction](sources/Sessions/S1003A01/workspace/notes/step29_boundary_corrected_AK_exterior_and_contact_capacity.md),
[A02 transgressions](sources/Sessions/S1003A02/workspace/notes/step27_chiral_transgression_and_small_bolt.md),
[A02 truncation](sources/Sessions/S1003A02/workspace/notes/step26_truncation_flux_and_branch_completeness.md),
[A02 calibration](sources/Sessions/S1003A02/workspace/notes/step35_calibration_theorem_and_branch_classification.md).

# What the latest analyses establish

## Pointwise combinations and exceptional periods

The constant affine combinations considered in A02 Step 40, followed by
discarding known-sign terms and applying the indicated sharp Weyl
Cauchy--Schwarz estimate, recover exactly the classical threshold
\(P/(8\pi^2)\ge k-A/3\) for pure blow-ups. Their envelope binds at
\(\rho=3/2\). This excludes that specified algebraic strategy as a source of
a stronger estimate; it does not exclude nonlinear pointwise inequalities,
other multipliers, joint constraints among all fields, or differential
methods.

Step 42 specializes to pure blow-ups with \(b^+\ge2\) and basic classes
exactly \(\pm K_X\). A classical Taubes argument excludes a nowhere-zero
closed self-dual common field with zero exceptional periods. It rules out an
exact formal configuration, not a sequence with small periods or thin zero
sets. The almost-Kähler torsion profile retains its period-angle factor;
the inequality \(\eta\ge1\) is not automatic for \(b^+\ge2\).

## Cotton pairing

Step 43 computes the model divergence on the stated almost-Kähler first jets
and uses the closed constant-scalar Cotton pairing. The desired second-jet
bound, treatment of zeros and cutoffs, and noncircular control of the Weyl
error remain missing. A conditional estimate \(P\ge R_N^2/(\Lambda A)\),
together with a separate saving bound, would yield a quadratic-scale lower
bound. It is not an established new Einstein gap, nor is it already a
statement for the original balanced family.

## The newly included perturbative note

A02 Step 44 proposes a cover-uniform perturbative theorem near CH hosts and
an almost-Kähler pocket estimate. They require different conclusions.

Write
\[
 C_+=\frac1{4\pi^2}\left(\frac S{24}+2\int|W^+|^2\right)
     =T_++\frac{P}{8\pi^2}.
\]
The pocket calculation, with \(\ell_{AK}=8\pi K_\omega\cdot[\omega]>0\),
\(\theta=\int|\nabla\omega|^2/\ell_{AK}\), and
\(\varphi=\operatorname{Vol}\{s^*\ge0\}/V<1\), gives
\[
 C_+\ge\frac{\ell_{AK}^2}{128\pi^2V}
 \left[3\theta^2-2\theta+1+
 \frac{\varphi}{1-\varphi}(1-\theta)_+^2\right]
 \ge\frac{\ell_{AK}^2}{128\pi^2V}\frac{2}{3-2\varphi}.
\]
It follows from a two-region convex quadratic minimization. Relating this
almost-Kähler structure to the actual canonical monopole branch is a
separate question.

The claimed two-sided perturbative comparison is not established by the
given proof. Indeed, at \(Q=0\) the exact Nijenhuis identity is
\[
 -P=\tfrac12R_N-\mathcal B,\qquad\mathcal B\ge0.
\]
This implies \(-P\le R_N/2\), not \(2P\le R_N\). The latter is used in
Step 44. Its linearized SW estimate also retains the whole derivative norm
while using the same derivative energy to supply a positive mass term on a
zero-potential sector. A weaker estimate might be repaired by allocating
part of the derivative term, but the displayed inequality does not follow
as written. The spinor normalization and the uniform Hölder inverse require
consistent treatment as well.

The accompanying review also gives a geometric reason to reject a general
reverse comparison: a nearby non-Einstein Kähler metric can have an
integrable canonical monopole direction, hence zero Nijenhuis energy but
positive \(P\). Integrability also persists under conformal scalar
normalization. The possible one-sided estimate \(R_N\le CP\) is a different
statement; its uniform analytic estimates still need completion.

Accordingly, the proposed theorem must not be used as a completed two-sided
cover-uniform comparison. The original note and its accompanying review are
both preserved. The separate pocket inequality does not depend on the
incorrect reverse comparison.

Sources: [Step 42](sources/Sessions/S1003A02/workspace/notes/step42_ak_torsion_profile_taubes_goldberg.md),
[Step 43](sources/Sessions/S1003A02/workspace/notes/step43_w0_cotton_quadratic_law_and_debts.md),
[Step 44](sources/Sessions/S1003A02/workspace/notes/step44_perturbative_ke_coercivity_and_pocket_price.md),
and [its accompanying review](sources/Sessions/S1003A02/trace/ttcs/results/step44_ttcs01_sub1_verifier.md).

# Classical applications and computational exploration

Canonical-model resolutions and rational blow-down constructions supply
zero-\(\alpha\) examples through existing geometry. Their role here is to
separate a zero infimum from attainment and from exact Einstein existence.
Real-hyperbolic blow-up nonexistence uses classical entropy and rigidity
theorems. A proposed sharp formula on real-hyperbolic blow-ups remains
conditional on an unproved Yamabe-invariant equality. These are not new
unconditional gap theorems.

Gibbons--Hawking coupled tangent models rule out an overly strong local
Liouville shortcut, but are not closed-manifold O10 counterexamples.
Small-bolt asymptotics, collapsed-control optimizations, higher angular
variations, and Calabi-cap transports provide candidates and tests. Their
floating values do not prove global lower bounds or stability.

In particular A01's latest Calabi-cap work has no certified improvement on
the CH cheap cell. A coarse Step-38 response lowered the training objective
but raised the independently sampled value. Neither this failure nor a
finite-dimensional absence of descent proves that all cap constructions
fail. The near-divisor cap transfer and packing also still need the stated
uniform chart and lattice inputs.

Sources: [A02 theorem package](sources/Sessions/S1003A02/workspace/notes/theorem_package_v1.md),
[A01 cap transfer](sources/Sessions/S1003A01/workspace/notes/step35_cap_transfer_neutrality_and_cap_cells.md),
[A01 latest response](sources/Sessions/S1003A01/workspace/notes/step38_curvature_conditioned_cap_response.md).

# The remaining global mathematical questions

The inherited N1 and I40/I41 theorems do not wait for these questions. The
two strongest unresolved upgrades have precise endpoints.

**Unrestricted O10.** Determine whether the original actual-field inputs
exclude an endpoint sequence with unbounded topological density, or construct
a closed-manifold sequence satisfying all those inputs. The new
\(T_+/A<3/4\) result removes a genuine subregion from the unknown set; it does
not settle the remaining high-density range.

**O11.** Determine the actual infimum or sharp asymptotic coefficient on the
specified families. On the selected sub-four families the answer cannot be
the former candidate \(4\). A lower bound must allow the saving already
realized by the construction. A universal decomposition into independently
priced standard surgery pieces would therefore be the wrong conclusion.

There are two legitimate ways to close the missing implication: a direct
global estimate using actual fields and curvature equations, or a geometric
description of arbitrary near-minimizers that supplies the hypotheses of a
sharp local estimate, with total remainder \(o(Q)\). Neither method is
imposed as a prerequisite for the other. Extra pure-blow-up, period-angle,
diagonal, or collar assumptions must either be supplied from the target
problem or remain explicit restrictions.

The most coherent mathematical connection emerging from the two Sessions is
that topology-changing cost is not a fixed additive tariff. Ambient chiral
curvature, the insertion direction, nonintegrability of actual fields, and
the marked boundary can change which costs are realizable. The constructions
show that some savings really occur; the missing sharp lower theory must
explain how far those mechanisms can go.

# Primary literature and attribution

The bibliography is retained in the inherited paper and Session notes. The
following comparisons are especially relevant to the claimed increments.

* C. LeBrun, *Ricci Curvature, Minimal Volumes, and Seiberg--Witten Theory*,
  [arXiv:math/0003068](https://arxiv.org/abs/math/0003068): curvature budgets,
  exact Ricci-energy infima, recovery, and the exceptional-period argument.
* C. LeBrun, *Curvature Functionals, Optimal Metrics, and the Differential
  Topology of 4-Manifolds*, [arXiv:math/0404251](https://arxiv.org/abs/math/0404251):
  the distinction between Ricci and full-curvature optimization.
* A. Malchiodi and F. Malizia, *Weyl energy and connected sums of four-manifolds*,
  [arXiv:2505.17752](https://arxiv.org/abs/2505.17752): strict Weyl-energy
  improvement, which must be distinguished from the joint scalar and Ricci
  cost controlled here.
* T. Ozuch, *Higher order obstructions to the desingularization of Einstein
  metrics*, [arXiv:2012.13316](https://arxiv.org/abs/2012.13316): exact Einstein
  desingularization obstructions, not an arbitrary-cell energy formula.
* O. Biquard and M. Herzlich, *A Burns--Epstein invariant for ACHE
  4-manifolds*, [arXiv:math/0111218](https://arxiv.org/abs/math/0111218):
  boundary CR geometry and characteristic identities.
* D. Calderbank and M. Singer, *Einstein metrics and complex singularities*,
  [arXiv:math/0206229](https://arxiv.org/abs/math/0206229): related complete
  Einstein constructions with their own topology and curvature hypotheses.

The local applicability of these sources is stated at each use in the
original proofs. Establishing priority for the new formulas or filling
requires comparison of their exact statements, not just matching subjects.

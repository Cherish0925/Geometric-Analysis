# S1003A01: Mathematical Results

## Setting and inherited inputs

For a closed four-manifold, write
\[
\mathcal E(g)=\inf_{\lambda\ne0}
\frac{\int|\operatorname{Ric}-\lambda g|^2}{\lambda^2\operatorname{Vol}(g)},
\qquad \alpha(M)=\inf_g\mathcal E(g),
\qquad P(g)=\int|\operatorname{Ric}^{\circ}|^2.
\]
For the surgery families considered below,
\[
M=X\#k\overline{\mathbb{CP}}^{\,2}\#\ell(S^1\times S^3),
\qquad A=c_1^2(X),\quad Q=k+4\ell,\quad h=Q/A.
\]
Local raw cell energies are not the normalized closed-manifold defect. In the
notes, \(J_6=\int|\operatorname{Ric}+6g|^2\) on the normalization
\(\operatorname{Ric}_{CH}=-6g_{CH}\), and
\(J_1=\int|\operatorname{Ric}+g|^2\) after rescaling. Numerical cell costs
are usually divided by \(8\pi^2\).

The inherited theory includes I40/I41 coercivity, actual monopole-field
supply, relative Chern--Weil identities, complete-cell transfer to closed
families, and the all-metric pure-handle value
\(\alpha=4h/(1+h)\). These are inputs, not new A01 theorems. The inherited
balanced-family conjecture was that the unrestricted first-order coefficient
equals \(4\). A01 supplies a strict counterconstruction to that conjectured
value, but does not determine the optimal coefficient.

Baseline sources: [linear coercivity](sources/Skills/geometric-analysis/research/paper/sections/linear_coercivity.tex),
[variational geometry](sources/Skills/geometric-analysis/research/paper/sections/variational_geometry.tex),
[variational selection and global cost](sources/Skills/geometric-analysis/research/paper/sections/variational_selection_and_global_cost.tex),
[relative cell cost](sources/Skills/geometric-analysis/research/sources/continuation/20260928_relative_cell_cost.md),
and [localization and coupled filling](sources/Skills/geometric-analysis/research/sources/continuation/20260928_localization_and_coupled_filling.md).
The [4 October supplement](sources/Skills/geometric-analysis/research/supplements/sources/20261004/README.md)
contains session results copied back into the research corpus; it is not a
pre-session source of those results.

Steps through 28 precede the 6 October resumption. Steps 29--38 form the
post-resumption increment. The groups below distinguish analytical results,
rigorous computations, conditional tools, floating experiments, and withdrawn
claims. Analytical status refers to the argument in the linked manuscript,
not to an independent priority or publication claim.

## Main results

### A01-01. Certified subthreshold blow-up cell and a strict sub-four upper construction

**Status:** Analytical construction with rigorous interval arithmetic.
The principal result was completed before resumption; later work improves
the witness and its numerical enclosure.

A smooth ordinary \((-1)\)-blow-up cell with an exact complex-hyperbolic
exterior satisfies \(J_1<8\pi^2\). The construction uses a perpendicular
bolt and a triaxial metric, not an exceptional topology. Its admissibility
argument checks positivity, bolt weights and smoothness, relative boundary
topology, and smoothing of the finite-order outer join with vanishing loss.

The first Step10--11 Arb enclosure already proves strictness:
\[
\frac{J_6}{8\pi^2}
=0.999116243135324311\pm2.24\times10^{-19}<1.
\]
Insertion into suitably chosen balanced covering families gives
\[
\limsup_m\frac{\alpha(M_m)}{h_m}
\le4-\frac{8\eta}{9}<4,
\qquad \frac{J_1}{8\pi^2}\le1-\eta.
\]
This disproves the inherited universal coefficient-four optimality claim
for that family. It is an upper construction, not a matching lower bound,
an exact optimum, or a theorem for every preassigned covering tower.

The larger-collar profile from Steps14--15 reaches approximately
\(0.99567\). Step33 re-encloses the same \(x_0=0.03\), \(X=128\),
degree-20 profile:
\[
0.995670030344086466734639542551
\le\frac{J}{8\pi^2}\le
0.995670030355130638306920215251.
\]
It yields
\[
\eta\ge0.004329969644869361693079784749,
\qquad
\limsup\alpha/h\le3.996151138093449456272817969112,
\]
with the displayed closed-family endpoint obtained by letting the smoothing
loss tend to zero. A fixed smooth witness retains a slightly smaller strict
margin. The additional digits strengthen the certificate; they are not a
second conceptual breakthrough.

Proofs: [Step10](sources/Sessions/S1003A01/workspace/notes/step10_rigorous_subthreshold_cell_and_O11.md),
[Step11](sources/Sessions/S1003A01/workspace/notes/step11_independent_review_O11_and_mixed_cost.md),
[Step15](sources/Sessions/S1003A01/workspace/notes/step15_bolt_neutral_transport_and_area_branch.md),
and [Step33](sources/Sessions/S1003A01/workspace/notes/step33_surgery_slope_law_and_ASD_retention.md).

Certificate chain: [enclosure script](sources/Sessions/S1003A01/workspace/scripts/perp_rigorous_enclosure.py),
[profile coefficients](sources/Sessions/S1003A01/workspace/data/perp_area/x00.03_X128_d20.json),
[exact J enclosure](sources/Sessions/S1003A01/workspace/data/step33/rigorous_x00.03_X128_d20_J_exact.json),
[P enclosure](sources/Sessions/S1003A01/workspace/data/step33/rigorous_x00.03_X128_d20_P_exact.json),
and [S enclosure](sources/Sessions/S1003A01/workspace/data/step33/rigorous_x00.03_X128_d20_S_exact.json).
The rigorous script uses the standard Python library and `python-flint`.
Its trust dependencies include the geometric formula and its code
transcription; the floating optimizer is not substituted for the interval
certificate, and the full geometric theorem is not Lean-formalized.

### A01-02. Nonsymmetric conformal reduction for exact-CH-ended cells

**Status:** Pre-resumption analytical result.

For a smooth, complete, connected marked cell that is exactly CH outside a
compact set, Step22 constructs a unique positive \(u\to1\) satisfying
\[
-6\Delta u+su+24u^3=0,
\qquad s(u^2g)=-24.
\]
Neither SU(2) symmetry nor an initial negative scalar-curvature assumption
is required. The exact decrease is
\[
P(g)-P(u^2g)
=24\int|\nabla u|^2+3\int(\Delta u/u)^2.
\]
Barrier, exhaustion, uniqueness, decay, and exact-collar truncation arguments
identify the relevant infima of \(P\), \(J_6\), and scalar-normalized
asymptotically CH classes. The proof uses decay
\(4<m<2+2\sqrt3\); the asymptotic-class formulation has its stated range
\(2<\mu<2+2\sqrt3\), not arbitrary stronger weights.

This removes scalar-sign and symmetry restrictions from the variational
reduction. It does not compute the reduced infimum or prove attainment.

Proof: [Step22](sources/Sessions/S1003A01/workspace/notes/step22_exact_CH_conformal_reduction.md).
Supporting computations, not substitutes for the proof:
[Yamabe check](sources/Sessions/S1003A01/workspace/scripts/yamabe_cell_check.py),
[conformal stationarity check](sources/Sessions/S1003A01/workspace/scripts/conformal_stationarity_check.py),
and [conformal numerical search](sources/Sessions/S1003A01/workspace/scripts/perp_conformal_lm.py).

### A01-03. Transfer to ramified compact Kähler--Einstein surfaces

**Status:** Post-resumption analytical application, independent of the
unfinished near-divisor cap-transfer program.

The certified cell transfers to negative KE surfaces obtained from highly
ramified toroidal compactifications of arithmetic nonuniform ball quotients.
With
\[
A_m=c_1^2(\bar X_m),\qquad
\Delta_m=3\chi(\bar X_m)-A_m>0,\qquad
\Delta_m/A_m\to0,
\]
the closed backgrounds are not compact ball quotients.

The argument uses Biquard--Guenancia smooth convergence on a fixed compact
set away from the divisors. A preliminary congruence cover supplies an
embedded marked CH ball of radius
\(\sqrt6\operatorname{arsinh}\sqrt{128}\approx7.6451263\), plus a fixed
buffer. Galois pullback supplies \(d_m\asymp A_m\) disjoint sites with the
same \(C^2\) discrepancy \(\varepsilon_m\to0\). Buffer interpolation
adds \(O(\varepsilon_m^2)\) raw defect per site and
\(O(\varepsilon_m)\) volume and scalar-moment errors. The untouched
background is exactly Einstein, so no error proportional to its entire
volume is incurred.

For \(Q_m\to\infty\), \(Q_m=o(A_m)\),
\(\Delta_m/Q_m\to r\in[0,1)\), and the balanced proportions
\[
\frac{k_m}{Q_m}\to\frac{2(1-r)}9,
\qquad
\frac{\ell_m}{Q_m}\to\frac{7+2r}{36},
\]
the construction gives
\[
\limsup_m\frac{\alpha(M_m)}{h_m}
\le4-\frac{8\eta}{9}(1-r)<4.
\]
Inherited polarized actual-field estimates also give a positive linear
lower order. Those field-supply results and the BG convergence theorem
are dependencies, not new A01 theorems.

This proof does not require the near-divisor Theorem T or packing
Proposition P in A01-09. Small compactly supported \(C^2\) perturbations
of a fixed smooth strict cell also yield nonsymmetric strict cells. This
openness statement proves neither nonsymmetric minimality nor stability.

Proof: [Step31](sources/Sessions/S1003A01/workspace/notes/step31_ramified_KE_transfer_and_interface_simplification.md).
Algebraic support: [topology window](sources/Sessions/S1003A01/workspace/scripts/step31_topology_window.py)
and [ramified transfer law](sources/Sessions/S1003A01/workspace/scripts/step32_ramified_transfer_law.py).

### A01-04. Two-parameter surgery law

**Status:** Post-resumption analytical synthesis and enlargement of the
parameter range.

On the ramified families, let
\[
\theta=k/Q,\qquad r=\Delta/Q,\qquad
\sigma=4r+18\theta,\qquad Q=o(A).
\]
The characteristic numbers satisfy
\[
T_+=A-Q,\qquad 3T_-/A=1+(\sigma-3)h.
\]
For convergent finite parameter limits, the actual-field lower estimates
and certified upper construction give
\[
\liminf\frac{\alpha}{h}\ge
\max\left\{\frac43(3-\sigma)_+,\,
\frac{18}{19}(4+c_0-\sigma)_+\right\},
\qquad
\limsup\frac{\alpha}{h}\le4(1-\eta\theta).
\]
The first lower branch is explicit; \(c_0>0\) in the inherited linear
window is nonexplicit. Consistency with the pure-handle value forces
\(c_0\le2/9\). The lower mechanisms depend on \(\sigma\), whereas this
upper construction depends on the blow-up fraction \(\theta\).

For \(\theta>0\) and \(\sigma<4+c_0\), a positive all-metric linear
gap coexists with a strict sub-four construction. The explicit subregion
is \(\sigma<3\). Inert-prime Picard towers supply the stated finite
\(r\) regimes through \(A_n\asymp p^{8n}\) and
\(\Delta_n\asymp p^{6n}\).

The disappearance of saving at \(r=1\) on the old balanced slice is not a
phase-transition theorem. For \(\sigma\ge4+c_0\), these lower estimates
become silent; they do not establish zero gap or Einstein existence.
The analytical lower machinery is inherited. The parameter organization,
application regimes, and their geometric realization are the new synthesis.

Proof: [Step33](sources/Sessions/S1003A01/workspace/notes/step33_surgery_slope_law_and_ASD_retention.md).
Support: [fraction-window script](sources/Sessions/S1003A01/workspace/scripts/step33_fraction_window.py)
and [symbolic output](sources/Sessions/S1003A01/workspace/data/step33/fraction_window.json).

### A01-05. Kähler period laws and pure-handle comparisons

**Status:** Pre-resumption analytical refinements and consequences.

For a Kähler one-point blow-up with exact KE collar, exceptional period
\(t=\int_E\omega\), and background Einstein constant \(\lambda\),
\[
P=2(2\pi-\lambda t)^2+rac14\int(s-4\lambda)^2,
\qquad
J_\lambda=2(2\pi-\lambda t)^2+rac12\int(s-4\lambda)^2.
\]
Here \(J_\lambda=\int|\operatorname{Ric}-\lambda g|^2\) uses the
signed Einstein constant. The negative-background core was inherited.
The signed extension and positive-curvature examples show that the
\(8\pi^2\) threshold is not independent of the background sign:
suitable smooth FS-collar Kähler cells lie below it. The explicit U(2)
moment minimization retains its profile-positivity and restricted-class
conditions. A general-background optimal Burns response still requires
control of minimizing profiles and is not established.

The inherited exact pure-handle closed theorem yields the local consequence
\[
\inf J_{0,\ell}=32\pi^2\ell,
\]
not attained by a fixed smooth positive-handle cell. No additivity theorem
for mixed \(J_{k,\ell}\) is proved. In particular, the possibility of a
mixed cell cheaper than separately placed blow-up and handle pieces remains
open; the pure-handle closed theorem must not be counted again as A01 work.

Proofs: [Step8](sources/Sessions/S1003A01/workspace/notes/step8_kahler_period_law_and_Rplus_response.md)
and [Step11](sources/Sessions/S1003A01/workspace/notes/step11_independent_review_O11_and_mixed_cost.md).
Support: [period calculation](sources/Sessions/S1003A01/workspace/scripts/kahler_period_cell.py),
[restricted infimum](sources/Sessions/S1003A01/workspace/scripts/kahler_cell_infimum.py),
[smooth positive-background cell](sources/Sessions/S1003A01/workspace/scripts/kahler_smooth_countercell.py),
and [space-form response](sources/Sessions/S1003A01/workspace/scripts/spaceform_scalar_response.py).

## Analytical tools and conditional mechanisms

### A01-06. CH exterior calculus, neutral modes, joint duality, and bolt diagnostics

**Status:** Mainly pre-resumption identities and conditional estimates,
not a global cell lower bound.

This group comprises chiral boundary transgressions, exact CH linear ground
states and endpoint costs, the Einstein mass null line, corrected
Hamilton--Jacobi/Riccati formulations, the shared three-component Ricci/Gram
dual, neutral Green identities, and the cluster budget limiting simultaneous
pair savings. The CH ground states include
\(f_+=x\sqrt{1+x}\) and \(f_-=x/(1+x)^{5/2}\).

The zero-cost exterior mode shows that some interface data can be carried
without the proposed raw action payment. Shared dual constraints cannot be
charged independently. For frozen cores, adjustable exterior energy bounds
the aggregate cluster saving; independently optimized pair savings cannot
simply be summed. Riccati chart poles do not by themselves indicate negative
bulk energy. Uniform entry of arbitrary competitors into the controlled
linear or dual regime remains unproved.

A separate exact calculation evaluates the two Weyl blocks at the bolt of
the Einstein filling supplied by A02:
\[
W_A=\operatorname{diag}(-41/16,-41/16,41/8),\qquad
W_B=\operatorname{diag}(-91/16,-91/16,91/8).
\]
Their squared norms are \(5043/128\) and \(24843/128\). Both are
nonzero; comparison with the KE curvature requirement excludes Kählerity
in either orientation. This is an A01 diagnostic of the shared/A02
construction, not a new A01 Einstein existence theorem. An earlier
three-distinct-eigenvalue argument was corrected.

Proof chain: [Step5](sources/Sessions/S1003A01/workspace/notes/step5_slice_charge_and_zero_flux.md),
[Step6](sources/Sessions/S1003A01/workspace/notes/step6_perpendicular_dual_cost_and_relative_calibration.md),
[Step7](sources/Sessions/S1003A01/workspace/notes/step7_perpendicular_verification_and_endpoint_map.md),
[Step14](sources/Sessions/S1003A01/workspace/notes/step14_large_collar_resistance_and_cluster_budget.md),
[Step15](sources/Sessions/S1003A01/workspace/notes/step15_bolt_neutral_transport_and_area_branch.md),
[Step16](sources/Sessions/S1003A01/workspace/notes/step16_joint_dual_calibration_and_exact_bolt_chirality.md),
[Step17](sources/Sessions/S1003A01/workspace/notes/step17_hamilton_jacobi_kahler_manifold_and_cs_hessian.md),
[Step18](sources/Sessions/S1003A01/workspace/notes/step18_corrected_riccati_and_H4_comparison.md),
and [Step19](sources/Sessions/S1003A01/workspace/notes/step19_exterior_null_line_LM_stationary_cells.md).

Principal code: [transgression check](sources/Sessions/S1003A01/workspace/scripts/transgression_closed_form_check.py),
[CH modes](sources/Sessions/S1003A01/workspace/scripts/ch_linear_einstein_modes.py),
[exterior null line](sources/Sessions/S1003A01/workspace/scripts/exterior_null_line.py),
[joint dual calibration](sources/Sessions/S1003A01/workspace/scripts/joint_dual_calibration.py),
[neutral bolt flux](sources/Sessions/S1003A01/workspace/scripts/neutral_flux_bolt.py),
and [exact bolt Weyl calculation](sources/Sessions/S1003A01/workspace/scripts/ach_bolt_weyl_exact.py).
The Lean artifacts [PerpGroundState](sources/Sessions/S1003A01/workspace/proofs/PerpGroundState.lean),
[JointDualGram](sources/Sessions/S1003A01/workspace/proofs/JointDualGram.lean),
and [RiccatiShift](sources/Sessions/S1003A01/workspace/proofs/RiccatiShift.lean)
certify restricted algebraic identities, not the full geometric argument.

### A01-07. Degeneration, recovered volume, and controlled matching budgets

**Status:** Pre-resumption conditional analytical tools.

Under a controlled recovered-CH region, a strict cell saving forces a
quantitative amount of unrecovered background volume. The associated
developing-map rigidity argument retains its hypotheses on a connected,
compact effective orbifold and an embedded locally CH exterior. Neither
statement supplies the required recovered region for arbitrary sequences.

Scalar-normalized low-action rescalings can be scalar-flat without being
Ricci-flat. Consequently, exact Einstein bolt series do not classify all
near-minimizing geometries. Prefix action and positive-variation estimates
exclude selected spurious cheap connectors. The controlled first-jet
scaling must satisfy both chiral budgets and the prefix inequality; an
apparently free transition need not be admissible.

Renormalized-momentum Green estimates quantify mismatch costs on explicitly
controlled expanding intervals. The global implication remains missing:
arbitrary near-minimizers have not been shown to enter and leave these
intervals with controlled scale, flux, volume, and incoming momentum. Exact
Einstein arcs can carry free momentum, so a local estimate alone does not
force the desired global payment.

Sources: [Step3](sources/Sessions/S1003A01/workspace/notes/step3_coupled_compensation_and_route_reassessment.md),
[Step4](sources/Sessions/S1003A01/workspace/notes/step4_positive_q_and_recovered_volume.md),
[Step25](sources/Sessions/S1003A01/workspace/notes/step25_degeneration_matching_and_charge.md),
[Step26](sources/Sessions/S1003A01/workspace/notes/step26_action_budget_matching.md),
and its [summary](sources/Sessions/S1003A01/workspace/notes/step26_step_summary.md).
Support: [bolt matching orders](sources/Sessions/S1003A01/workspace/scripts/step25_bolt_matching_orders.py),
[chiral bridge profile](sources/Sessions/S1003A01/workspace/scripts/chiral_bridge_profile.py),
[independent constraint and pinning](sources/Sessions/S1003A01/workspace/scripts/step26_independent_constraint_and_D_pin.py),
[flux laws](sources/Sessions/S1003A01/workspace/scripts/step27_flux_laws.py),
and [cell flux budget](sources/Sessions/S1003A01/workspace/scripts/step27_cell_flux_budget.py).

### A01-08. Almost-Kähler representation and corrected interface bookkeeping

**Status:** Pre-resumption structural analysis with post-resumption boundary
corrections.

For diagonal perpendicular-bolt exact-CH cells, the canonical conformal
almost-Kähler representation degenerates at the bolt. It is not a smooth
almost-Kähler filling or an ordinary conical completion. The gap identity
reorganizes the inherited relative Chern--Weil identity. Added structure
includes Chern--Stokes pinning, Nijenhuis transport, forced nonintegrability,
channel cancellations, and conditional terminal positivity. In the notes'
normalization,
\[
\widehat P-1
=12H_s+6G+\frac32Q_\delta+\frac12Q_A-\frac32N.
\]
The signed Nijenhuis term cannot be silently dropped.

Step29 supplies the exact local boundary formula
\[
\widehat P[t_0,t_1]
=\int_{t_0}^{t_1}L_{\rm AK}+B(t_1)-B(t_0).
\]
It explains why large positive AK tail terms can be canceled by boundary
conversion. The CH mass null mode is preserved, and contact closure is not
an independent additional charge. Step31 simplifies the interface expression.

This is a mechanism and bookkeeping result, not a new unrestricted positive
lower margin. A nonsymmetric extension would require the appropriate relative
closed self-dual form, with its periods and zero set controlled; that input is
not supplied. The far-tail positivity hypotheses also do not settle the
near-bolt region.

Sources: [Step28](sources/Sessions/S1003A01/workspace/notes/step28_AK_gap_identity_nijenhuis_transport.md),
[Step29](sources/Sessions/S1003A01/workspace/notes/step29_boundary_corrected_AK_exterior_and_contact_capacity.md),
and [Step31](sources/Sessions/S1003A01/workspace/notes/step31_ramified_KE_transfer_and_interface_simplification.md).
Support: [AK identity](sources/Sessions/S1003A01/workspace/scripts/step28_ak_gap_identity.py),
[Chern--Stokes check](sources/Sessions/S1003A01/workspace/scripts/step28_chern_stokes_check.py),
[local AK flux](sources/Sessions/S1003A01/workspace/scripts/step29_local_AK_flux.py),
[exterior bridge](sources/Sessions/S1003A01/workspace/scripts/step29_ak_exterior_bridge.py),
[contact capacity](sources/Sessions/S1003A01/workspace/scripts/step29_capacity_contact.py),
and [interface simplification](sources/Sessions/S1003A01/workspace/scripts/step30_B_minus_bplus.py).

### A01-09. ASD retention, the Calabi cap model, and incomplete cap transfer

**Status:** Post-resumption exact identities and model calculations,
conditional applications, and unfinished proof obligations.

Writing \(S_0=32\pi^2A\), \(B=\int|W^-|^2\), and
\(B_\Delta=8\pi^2\Delta/3\), the exact identity is
\[
P=\frac{S-S_0}{12}+4(B-B_\Delta)
+8\pi^2A\,h(1-6\theta).
\]
Retention \(B\ge B_\Delta-o(Q)\) yields the corresponding
\(r\)-independent conditional lower bound
\(\mathcal E\ge4h(1-6\theta)+o(h)\). Beating a positive such floor
requires \(O(Q)\)-scale ASD depletion. Retention is not proved for all
metrics. A coarse floor for specified disjoint, topology-preserving
modifications with KE boundary annuli does not imply that all such
modifications fail to improve the current upper construction.

The explicit Calabi cap, its chiral Weyl operators, and its energy integral
provide a concrete environment in which background ASD energy could change.
For the normalized model, \(\Theta(\tau)=2\tau^2/3-c/\tau\),
\(\operatorname{Ric}=-g\), \(s=-4\), and
\[
|W^+|^2=2/3,\qquad |W^-|^2=6c^2/\tau^6.
\]
The cap's favorable \(R^-\) direction does not automatically improve the
\(R^+\)-controlled first Burns response. The relative ledger
\[
b=a+12\pi^2k,\qquad
P=8\pi^2(k+4\ell)+4a+\delta S/12
\]
retains scalar-square, volume, and scalar-moment exchange. A near-tariff
value of \(P\) alone does not rule out net ASD depletion.

Two links needed for transfer from this model to the actual near-divisor
geometry remain incomplete:

- Theorem T proposes uniform higher-order comparison on normalized cap
  slabs. The reciprocal-angle covers still require explicit uniform
  holomorphic chart sizes, reference coefficients, potential normalization
  and oscillation, ellipticity, and source Hölder bounds. The model-to-actual
  concentration corollary is subject to the same gap.
- Proposition P proposes \(\asymp\Delta\) embedded fixed-scale cap
  sites. The Heisenberg scaling and count are consistent, but the relevant
  lattice inclusions and central-index calculations remain to be written
  explicitly before quoting the proposition as a theorem.

These obligations do not affect A01-03, which operates on fixed compact
regions away from the divisor. Even after both are completed, a sufficiently
cheap cap competitor must still be constructed and certified.

Sources: [Step33](sources/Sessions/S1003A01/workspace/notes/step33_surgery_slope_law_and_ASD_retention.md),
[Step35](sources/Sessions/S1003A01/workspace/notes/step35_cap_transfer_neutrality_and_cap_cells.md),
and [Step36](sources/Sessions/S1003A01/workspace/notes/step36_perpendicular_cap_transplant.md).
Support: [cusp-closing Weyl calculation](sources/Sessions/S1003A01/workspace/scripts/step33_cusp_closing_Wminus.py)
and [cap Weyl operator](sources/Sessions/S1003A01/workspace/scripts/step34_cap_weyl_operator.py).

## Numerical exploration

### A01-10. Local searches, pair interactions, and finite-dimensional stability

**Status:** Exploratory floating computations, except for witnesses
subsequently covered by A01-01's rigorous certificates.

The session developed diagonal and triaxial searches, compensated and
positive-\(q\) routes, pair-overlap trials, large-collar and area branches,
H4 comparisons, conformal relaxation, and SU(2)/angular stability probes.
These provide candidates and identify failure modes; they do not establish
unrestricted optimality or stability.

The small computed pair-overlap saving remained uncertified. Positive Ritz
values in finite spaces do not determine the physical gauge-slice spectral
bottom. Step24 corrects an angular row/column and multiplicity issue; higher
isotypes and the gauge-resolved problem remain open. The smaller floating
value near \(0.995178\) did not obtain the required interval certificate.

Sources: [Step2](sources/Sessions/S1003A01/workspace/notes/step2_cell_problem_and_triaxial_numerics.md),
[Step3](sources/Sessions/S1003A01/workspace/notes/step3_coupled_compensation_and_route_reassessment.md),
[Step4](sources/Sessions/S1003A01/workspace/notes/step4_positive_q_and_recovered_volume.md),
[Step9](sources/Sessions/S1003A01/workspace/notes/step9_subthreshold_cell_verification.md),
[Step13](sources/Sessions/S1003A01/workspace/notes/step13_pair_overlap_interaction.md),
[Step21](sources/Sessions/S1003A01/workspace/notes/step21_conformal_selection_su2_stability_constrained_HJ.md),
[Step23](sources/Sessions/S1003A01/workspace/notes/step23_scalar_relaxed_j1_CR_pinning_and_certification.md),
and [Step24](sources/Sessions/S1003A01/workspace/notes/step24_normalized_gauge_resolved_j1.md).

Principal drivers: [cell search](sources/Sessions/S1003A01/workspace/scripts/cell_opt.py),
[compensation](sources/Sessions/S1003A01/workspace/scripts/cell_compensation.py),
[positive-q search](sources/Sessions/S1003A01/workspace/scripts/cell_qsearch.py),
[pair overlap](sources/Sessions/S1003A01/workspace/scripts/pair_overlap_trial.py),
[collar continuation](sources/Sessions/S1003A01/workspace/scripts/perp_collar_continue.py),
[off-diagonal spectrum](sources/Sessions/S1003A01/workspace/scripts/su2_offdiag_spectrum.py),
and [normalized angular gauge](sources/Sessions/S1003A01/workspace/scripts/angular_normalized_gauge.py).

### A01-11. Cap transplantation and curvature-conditioned response through Step38

**Status:** Post-resumption floating JAX/Sobol experiments; no certified cap
improvement or cap-infimum theorem.

Positive congruence transport and improved geodesic marking reduce a large
coordinate-dependent apparent penalty. The tested cap costs remain around
\(1.057\), above the certified CH reference near \(0.99567\). This
comparison concerns the transported trial family, not an intrinsic cap
tariff. Long-range exponential-chart accuracy, global embedding, and
rigorous quadrature error have not been certified.

Step38 uses the response representation
\[
g(c)=B(c)^Tg_0B(c),\qquad B=I+\tfrac12g_0^{-1}h(c),
\]
with tensors supported in \(0.45<r<0.78\). Thus the tested modes leave
the whole bolt neighborhood and its jets unchanged. Positivity follows
when \(B\) is nonsingular; sampled positive eigenvalues do not prove
continuum nonsingularity.

SVD conditions the derivative of the complete discrete weighted Ricci
residual, including moving-frame and moving-volume terms. It is the
Gauss--Newton norm for that least-squares problem, not an intrinsic
frozen-weight Einstein-operator norm. Paired samples reduce variance.

Ten tested CH modes give no material descent: the paired change is
\((-5.89\pm9.10)\times10^{-7}\). A coarse cap fit lowers its training
cost by about \(0.00992\), but independent validation increases the
response-region action by \(0.00870\pm0.00109\). This exposes spatial
overfitting despite improved coefficient conditioning. In the output,
`response_improvement` means optimized minus base cost; positive is worse.

The discrete exponential map requires refinement checks. A cap-minus-CH
integral over the response band is not a full-cell correction. Only the
optimized-minus-base response integral is complete when the perturbation
vanishes outside that band. The refined cap fit is not used as a completed
result in the Step38 note. Failure of these fixed-bolt modes does not exclude
cap-adapted bolt areas or jets, mixed topology, or better markings.

Step38 also incorporates attributed A02 paired-field information: under
the stated closed blow-up basic-class hypotheses, a nowhere-zero self-dual
harmonic form cannot have zero exceptional period. The local canonical form
evades that excluded model by degenerating at the bolt. The imported
Cotton discussion identifies a derivative mismatch and, conditionally, a
quadratic rather than linear scale. These are A02 dependencies, not new A01
theorems. The frozen A01 sequence ends with Step38.

Sources: [Step36](sources/Sessions/S1003A01/workspace/notes/step36_perpendicular_cap_transplant.md),
[Step37](sources/Sessions/S1003A01/workspace/notes/step37_cap_congruence_transport.md),
[Step38](sources/Sessions/S1003A01/workspace/notes/step38_curvature_conditioned_cap_response.md),
[A02 Step42](sources/Sessions/S1003A02/workspace/notes/step42_ak_torsion_profile_taubes_goldberg.md),
and [A02 Step43](sources/Sessions/S1003A02/workspace/notes/step43_w0_cotton_quadratic_law_and_debts.md).

Drivers: [perpendicular transplant](sources/Sessions/S1003A01/workspace/scripts/step36_cap_perp_transplant.py),
[congruence transport](sources/Sessions/S1003A01/workspace/scripts/step37_cap_congruence_transport.py),
[exponential-map transport](sources/Sessions/S1003A01/workspace/scripts/step37_cap_expmap_transport.py),
[response search](sources/Sessions/S1003A01/workspace/scripts/step37_cap_response_opt.py),
and [conditioned response](sources/Sessions/S1003A01/workspace/scripts/step38_expmap_gn_response.py).
Data: [Step37 records](sources/Sessions/S1003A01/workspace/data/step37/),
[CH paired control](sources/Sessions/S1003A01/workspace/data/step38/ch_band_gn1_fit32.json),
and [cap cross-validation](sources/Sessions/S1003A01/workspace/data/step38/cap_band_gn1_cv.json).
Incomplete output placeholders are not completed evidence.

## Withdrawals and corrections

### A01-12. Correction register

The following restrictions supersede stronger statements in earlier notes.

- The same-entire-collar infimum comparison
  \(\lvert j_{g_1}(R)-j_{g_2}(R)\rvert\le C\varepsilon^2\) is
  withdrawn. The interpolated competitor equals the target only on a
  smaller outer collar. The valid replacement transfers a given competitor
  with additional buffer space at \(O(\varepsilon^2)\) defect cost;
  it neither compares the original identical-collar classes nor excludes
  first-order background-adapted core responses.
  See [Step35](sources/Sessions/S1003A01/workspace/notes/step35_cap_transfer_neutrality_and_cap_cells.md).
- C2 matching and vanishing boundary Einstein defect alone do not remove
  weak normal stress or force continuation as CH. The required stronger
  matching or stress condition must remain explicit.
  See [Step4](sources/Sessions/S1003A01/workspace/notes/step4_positive_q_and_recovered_volume.md).
- Near-tariff blow-up action does not by itself exclude net ASD depletion;
  the relative scalar-square term permits scalar-moment and volume exchange.
  See [Step35](sources/Sessions/S1003A01/workspace/notes/step35_cap_transfer_neutrality_and_cap_cells.md).
- The coarse separated-modification floor does not show that every such
  modification fails to improve the present specific upper coefficient.
  See [Step33](sources/Sessions/S1003A01/workspace/notes/step33_surgery_slope_law_and_ASD_retention.md).
- The value near \(0.995178\), unrestricted stationarity or stability,
  an intrinsic positive cap tariff, and completed Theorem T/Proposition P
  transfer are not certified conclusions.
  See [Step23](sources/Sessions/S1003A01/workspace/notes/step23_scalar_relaxed_j1_CR_pinning_and_certification.md),
  [Step24](sources/Sessions/S1003A01/workspace/notes/step24_normalized_gauge_resolved_j1.md),
  and [Step36](sources/Sessions/S1003A01/workspace/notes/step36_perpendicular_cap_transplant.md).
- A hardcoded zero AK numerical residual is not an independent identity
  check. See [Step28](sources/Sessions/S1003A01/workspace/notes/step28_AK_gap_identity_nijenhuis_transport.md).
- Positivity of the response metric requires nonsingularity of \(B\);
  its conditioning is discrete Gauss--Newton conditioning; and a paired
  cap-minus-CH band integral is not the total cap correction.
  See [Step38](sources/Sessions/S1003A01/workspace/notes/step38_curvature_conditioned_cap_response.md).

## Source and computational dependencies

The proof texts, coefficient records, and scripts have different roles.
Preserve the script import closure and original inputs, not only a final
driver or a plotted value. In particular,
[perp_dual_cost.py](sources/Sessions/S1003A01/workspace/scripts/perp_dual_cost.py)
and [step36_cap_perp_transplant.py](sources/Sessions/S1003A01/workspace/scripts/step36_cap_perp_transplant.py)
import [A02's o11_perp_cell.py](sources/Sessions/S1003A02/workspace/scripts/o11_perp_cell.py)
through the shared user-root Session layout. The frozen two-Session relative
layout preserves that dependency. The subsequent cap scripts depend on these
modules. This computational sharing does not make every A02 theorem an A01
contribution.

Biquard--Guenancia convergence, LeBrun's polarized field supply, Džambić's
arithmetic invariants, and the regularity tools invoked for cap comparison
are external proof dependencies. Their roles and the uncompleted uniformity
checks are retained in the linked notes. The contribution map does not
claim exhaustive literature novelty or independent verification of every
external input.

The remaining unrestricted problem is not the existence of one more local
identity. It is to determine the optimal closed-manifold defect and explain
arbitrary near-minimizers, either by proving entry into a controlled
geometric regime or by another argument with the same quantifiers. The
strict construction, nonsymmetric conformal reduction, new-background
transfer, and parameter law remain substantive results without that closure.

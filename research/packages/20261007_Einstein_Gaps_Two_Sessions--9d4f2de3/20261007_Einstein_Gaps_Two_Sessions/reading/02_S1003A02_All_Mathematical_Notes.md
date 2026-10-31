# S1003A02 complete mathematical notes

Original notes follow in numerical step order. Later corrections are retained in their original locations. The current synthesis and correction table are the reading entry points.

- [step1_field_compatibility_and_route_portfolio.md](../sources/Sessions/S1003A02/workspace/notes/step1_field_compatibility_and_route_portfolio.md)
- [step2_blowup_cell_problem_O11.md](../sources/Sessions/S1003A02/workspace/notes/step2_blowup_cell_problem_O11.md)
- [step2_synthesis_O10_O11.md](../sources/Sessions/S1003A02/workspace/notes/step2_synthesis_O10_O11.md)
- [step4_O10_localization_and_orbifold_test.md](../sources/Sessions/S1003A02/workspace/notes/step4_O10_localization_and_orbifold_test.md)
- [step6_theorems_and_O11_rotation.md](../sources/Sessions/S1003A02/workspace/notes/step6_theorems_and_O11_rotation.md)
- [step8_first_order_cell_law_ASD_Qprinciple.md](../sources/Sessions/S1003A02/workspace/notes/step8_first_order_cell_law_ASD_Qprinciple.md)
- [step9_universal_cell_response_and_spectral_pressure.md](../sources/Sessions/S1003A02/workspace/notes/step9_universal_cell_response_and_spectral_pressure.md)
- [step11_subthreshold_perpendicular_cell.md](../sources/Sessions/S1003A02/workspace/notes/step11_subthreshold_perpendicular_cell.md)
- [step13_einstein_fillings_blown_up_ball.md](../sources/Sessions/S1003A02/workspace/notes/step13_einstein_fillings_blown_up_ball.md)
- [step14_chirality_nut_and_control_localization.md](../sources/Sessions/S1003A02/workspace/notes/step14_chirality_nut_and_control_localization.md)
- [step15_ach_projected_theory.md](../sources/Sessions/S1003A02/workspace/notes/step15_ach_projected_theory.md)
- [step19_theorem_package_and_selection_lemma.md](../sources/Sessions/S1003A02/workspace/notes/step19_theorem_package_and_selection_lemma.md)
- [step20_burns_response_and_neck_quantization.md](../sources/Sessions/S1003A02/workspace/notes/step20_burns_response_and_neck_quantization.md)
- [step21_entropy_hyperbolic_cells_and_offbolt_weyl.md](../sources/Sessions/S1003A02/workspace/notes/step21_entropy_hyperbolic_cells_and_offbolt_weyl.md)
- [step22_hyperbolic_volume_mass_and_weyl_certificate.md](../sources/Sessions/S1003A02/workspace/notes/step22_hyperbolic_volume_mass_and_weyl_certificate.md)
- [step23_yamabe_identity_hyperbolic_sharp_gap_and_cell_channels.md](../sources/Sessions/S1003A02/workspace/notes/step23_yamabe_identity_hyperbolic_sharp_gap_and_cell_channels.md)
- [step25_diagonal_cell_compactness_and_CR_pinning.md](../sources/Sessions/S1003A02/workspace/notes/step25_diagonal_cell_compactness_and_CR_pinning.md)
- [step26_truncation_flux_and_branch_completeness.md](../sources/Sessions/S1003A02/workspace/notes/step26_truncation_flux_and_branch_completeness.md)
- [step27_chiral_transgression_and_small_bolt.md](../sources/Sessions/S1003A02/workspace/notes/step27_chiral_transgression_and_small_bolt.md)
- [step28_saturation_control_and_revised_diagonal_structure.md](../sources/Sessions/S1003A02/workspace/notes/step28_saturation_control_and_revised_diagonal_structure.md)
- [step29_collapsed_saturation_value_four.md](../sources/Sessions/S1003A02/workspace/notes/step29_collapsed_saturation_value_four.md)
- [step30_Qdoubleprime_beta_pinning_and_anisotropic_collapse.md](../sources/Sessions/S1003A02/workspace/notes/step30_Qdoubleprime_beta_pinning_and_anisotropic_collapse.md)
- [step31_charge_variation_constraint_pinning_nonround_opening.md](../sources/Sessions/S1003A02/workspace/notes/step31_charge_variation_constraint_pinning_nonround_opening.md)
- [step33_link_charges_global_decomposition_static_channel.md](../sources/Sessions/S1003A02/workspace/notes/step33_link_charges_global_decomposition_static_channel.md)
- [step34_characteristic_constraint_calculus_and_N_probe.md](../sources/Sessions/S1003A02/workspace/notes/step34_characteristic_constraint_calculus_and_N_probe.md)
- [step35_calibration_theorem_and_branch_classification.md](../sources/Sessions/S1003A02/workspace/notes/step35_calibration_theorem_and_branch_classification.md)
- [step38_kahler_and_paired_field_scope.md](../sources/Sessions/S1003A02/workspace/notes/step38_kahler_and_paired_field_scope.md)
- [step40_nijenhuis_form_and_pointwise_exhaustion.md](../sources/Sessions/S1003A02/workspace/notes/step40_nijenhuis_form_and_pointwise_exhaustion.md)
- [step42_ak_torsion_profile_taubes_goldberg.md](../sources/Sessions/S1003A02/workspace/notes/step42_ak_torsion_profile_taubes_goldberg.md)
- [step43_w0_cotton_quadratic_law_and_debts.md](../sources/Sessions/S1003A02/workspace/notes/step43_w0_cotton_quadratic_law_and_debts.md)
- [step44_perturbative_ke_coercivity_and_pocket_price.md](../sources/Sessions/S1003A02/workspace/notes/step44_perturbative_ke_coercivity_and_pocket_price.md)
- [theorem_package_v1.md](../sources/Sessions/S1003A02/workspace/notes/theorem_package_v1.md)


---

## Source step1_field_compatibility_and_route_portfolio.md

Original: [sources/Sessions/S1003A02/workspace/notes/step1_field_compatibility_and_route_portfolio.md](../sources/Sessions/S1003A02/workspace/notes/step1_field_compatibility_and_route_portfolio.md)

# Step 1 — actual-field compatibility and route portfolio

## 1. What the inherited theory really measures

The common mechanism has four logically distinct layers.

1. **Actual supply.** For each metric or conformal class in the stated range, topology or gauge theory supplies a genuine field with a fixed global charge. The quantifier matters: a harmonic form existing for one chosen metric is not the same input as an ordinary monopole class solving the equations for every relevant conformal class.
2. **Algebraic alignment.** Small curvature defect forces the field and selected curvature block toward a particular algebraic orbit. The bounded-form theorem is the supplier-independent version: for a bounded self-dual form \(\psi\),
   \[
   (1+B_\psi)d_\psi\ge c(K),\qquad B_\psi=\fint|\Delta_H\psi|^2.
   \]
   Linear coercivity uses more: spinor curvature action, the determinant-square identity, and same-field weak Bianchi cancellation.
3. **Differential prolongation and charge.** Near algebraic alignment is not enough. The coupled field equations produce a derived section or tensor whose differential equation is incompatible with its nonzero characteristic charge. At the zero-Weyl endpoint the decisive derived object is a section of \(L^5\).
4. **Compactness versus realization.** The incompatibility becomes a uniform gap only when concentration cannot hide the derived charge. Conversely, an upper bound must come from a real metric on the same topology and must pay scalar and Weyl costs on that one metric.

Thus the independent information controlling an Einstein gap is not only a topological number. It consists of: (a) the metric-wise accessible field/charge budget; (b) the algebraic curvature orbit selected by that field; (c) the differential order at which compatibility sees the charge; (d) concentration behavior at the critical four-dimensional scale; and (e) the least same-metric geometric cost of realizing the topology. This explains why separate infima, formal fields, or local models cannot determine \(\alpha(M)\).

A useful unifying target is a **charge-versus-realization inequality**: actual field charge must either produce a quantitative compatibility cost, or be carried by explicitly classifiable concentrating cells whose complete metric cost can be computed. The first alternative gives lower bounds and rigidity; the second gives constructions or genuine degeneration mechanisms. O10 and O11 test the two extreme density regimes of this same principle.

## 2. O10: the remaining object is a radial capacity defect, not the final line inverse

The finite-density theorem assumes actual conformal monopole supply, \(p\ge A>0\), \(a^2\ge T_+\), and \(\chi/A\le B\), and proves
\[
\kappa_\beta=\fint|\operatorname{Ric}+g|^2+D_\beta/V
 \ge c(B)(\beta-2)^2/\beta^2.
\]
The strong-current conclusions before the opposite-Weyl bound are already substantial: on the scalar \(-4\) representative, the actual positive spinor has \(\rho\to4/3\); its cubic torsion and a bounded same-bundle resolvent \(v\) have \(m=|v|^2\to m_*=128/81\), \((\nabla^*\nabla-2)v\to0\), and fixed total gradient mass \(\fint|\nabla v|^2\to2m_*\). The determinant curvature has a bounded model plus small \(L^2\) error independently of \(W^-\).

The density bound first enters when one turns these weak facts into Hessian and fourth-moment bounds for the negative-spinor resolvent. It gives \(dm\to0\), reduces the first jet to one horizontal coefficient \(c\), preserves a fixed \(L^2\) mass of the resulting \(L^5\) section, and makes the weak Cauchy–Riemann test legal. The final positive line resolvent itself uses only Ricci and determinant-line curvature and has no \(W^-\) block.

Without a density bound, the inherited work has isolated the exact escape:

- radial energy is confined to lower-amplitude wells, while deep wells carry asymptotically vanishing energy only after the depth tends to zero;
- the amplitude defect has a nonnegative capacity-scale measure \(\mu\), and the scalar mass equation allows nonzero \(\mu\);
- the complete first jet has
  \[
  b=d\,\theta_1+c\,\theta_2,\qquad d=-\frac{m_3+i m_4}{2m},
  \]
  so radial energy can consume the fixed total gradient budget and leave no fixed mass for \(c\);
- the global polynomial one-form \(\mathcal B=v\wedge\nabla v\in\Omega^1(L^3)\) obeys exact divergence and self-dual exterior equations, but its Weitzenböck potential has eigenvalues \(-3\) in the radial \(\theta_1\) direction and \(+1\) in the horizontal \(\theta_2\) direction;
- weighting the type projection and the positive-spinor Cartan equation produces exact cancellations rather than a missing positive radial term;
- scalar amplitude models on a flat torus realize the capacity phenomenon, so scalar consequences alone cannot remove it.

This changes the best O10 route. Repeating scalar truncations or estimating the final \(L^5\) inverse is unlikely to decide the problem. The decisive mathematical question is whether the **full coupled radial-horizontal Cartan system** admits a nonzero concentration tangent object.

### Proposed concentration-tangent program

Assume an escaping O10 sequence. Select a concentration point and scale on which a fixed amount of radial energy is present while the original defect is small relative to that energy. Rescale the complete fields, not only \(m\). The target is a classification of finite-energy tangent systems for
\[
(v,\Phi,\mathcal A,\text{negative spin connection};\ d,c)
\]
that retain the Dirac equation, the type projection, determinant-curvature fit, and the two coupled Cartan equations. There are two meaningful outcomes:

1. every tangent system with nonzero radial capacity carries a definite opposite-chiral/topological cell; then aggregate charge accounting may show that each such cell forces a nonvanishing amount of the original defect or identify the exact high-density degeneration;
2. a genuine finite-energy tangent exists with radial mass and zero compatibility cost; it supplies the local core needed for an O10 counterexample, after global matching and actual supply are addressed.

A mere harmonic or scalar tangent is insufficient. The rescaled negative spin connection may bubble because \(W^-\) is precisely uncontrolled, so the classification must include that connection rather than assume it becomes flat.

**Continue** this route if a good-scale selection preserves the full equations and yields a finite-energy tangent with quantized connection or determinant data. **Adjust** toward a direct compensated identity if all possible scales lose one essential equation. **Stop** scalar-only work if it produces only the already-allowed defect measure \(\mu\).

## 3. O11: the recent strict Weyl gluing is scientifically relevant but presently misses the required joint cost

For the balanced family,
\[
\alpha_j=4\frac{\inf_gP(g)}{8\pi^2A_j}+O(h_j^2),\qquad
Q_j=A_jh_j,
\]
so coefficient four is equivalent to \(\inf P=8\pi^2Q+o(Q)\). Every improvement must be on a single metric and accurate to \(o(Q)\).

The 2025 Malchiodi–Malizia construction gives a real strict Weyl-energy decrease on a connected sum when the two metrics are non-locally-conformally-flat and not of the same chirality. Its leading interaction has order \(a^4\) and is chosen negative by aligning the Weyl tensors. It applies to the complex-hyperbolic / reversed Fubini–Study chirality pattern. However, the paper does not estimate scalar energy or traceless-Ricci energy. Therefore it does not yet change the balanced coefficient. The 2026 locally conformally flat construction has different hypotheses: its Bach-flat factor must have both Weyl chiralities, so a half-self-dual complex-hyperbolic factor is excluded.

The exact same-metric identity is
\[
\Delta P=\tfrac12\Delta\mathcal W_{\rm ten}+\Delta S/12
\]
on fixed topology, while comparison to disconnected summands includes the additional \(32\pi^2\) topological term. This is especially important here: the standard blowup recovery cost \(8\pi^2\) is obtained only after the scalar contribution of the conformally blown-up positive Einstein piece is accounted for. A strict Weyl saving alone does not determine its sign relative to \(8\pi^2\).

### Proposed one-neck calculation before any large replicated construction

Choose the 2025 gluing with the reversed Fubini–Study factor on the inverted side and compute, in the authors' actual \(W^{2,\infty}\) metric and a smooth approximation,
\[
\Delta_\#P
 =\tfrac12\Delta_\#\mathcal W_{\rm ten}+\Delta_\#S/12+32\pi^2
\]
through the first nonzero neck order. Compare it directly with \(8\pi^2\), not with zero. The unknown scalar term should be expanded in the same conformal-normal and biharmonic interpolation variables as the known Weyl interaction. Also test whether using the scalar-flat Green-function conformal blowup of the Fubini–Study factor preserves a usable interaction after its additional asymptotic mass terms are included.

If one obtains a fixed per-site saving \(\delta>0\), replication must be performed on a positive fraction of the \(k_j\) blowup sites with all exterior and smoothing errors \(o(Q_j)\). Sparse blowup density \(k_j/A_j\to0\) suggests using explicit uniformly thick finite covers of a fixed complex-hyperbolic surface, where separated sites and uniform local geometry may be available. If the gluing scale must tend to zero and the saving is only \(O(a_j^4)\to0\) per site, then the total saving is \(o(Q_j)\) and this route cannot change the first-order coefficient.

**Continue** if the one-neck expansion produces a negative joint \(P\)-correction relative to the standard \(8\pi^2\) cost with a fixed admissible scale. **Adjust** if scalar loss cancels the Weyl gain but leaves a tunable interaction parameter. **Stop** this route for O11 if every smooth matching forces the per-site saving to vanish with the neck scale.

## 4. New suppliers: what is and is not genuinely new

A harmonic self-dual form exists whenever \(b_+>0\), and it has zero Hodge source, but after \(L^2\) normalization it has no metric-uniform \(L^\infty\) bound on degenerating metrics. Hence it does not automatically satisfy the bounded-form interface with a universal \(K\). Near-symplectic harmonic forms have useful zero-set geometry, as in Taubes' work, but that still does not provide the missing uniform amplitude input over all metrics.

An almost-Kähler form has \(|\omega|^2=2\) and \(\Delta_H\omega=0\), so it perfectly supplies the bounded-form interface for the restricted class of compatible almost-Kähler metrics. Exact harmonic-Weyl identities then yield rigidity in strong settings. This is a meaningful model of the unified mechanism, but it does not control \(\alpha(M)\) over all metrics unless one proves an actual compatible form for every competitor or a transfer from arbitrary metrics.

Bauer–Furuta, special monopoles, and twisted/Pin-minus monopoles broaden actual supply but remain gauge-field suppliers for essentially the same analytical mechanism. Furuta–Matsuo spectral defects add simultaneous differential information, yet their topological curvature conclusions still use perturbed Seiberg–Witten solvability. A genuinely new supplier should therefore do more than rename a monopole input: it must provide, uniformly over the required competitors, a bounded field or an alternative derived charge with a differential equation strong enough to survive critical concentration.

The most promising supplier search is presently not arbitrary harmonic forms, but one of:

- a twisted or cover field whose characteristic charge survives where ordinary class squares do not, coupled to a supplier-independent bounded-form/prolongation theorem;
- several simultaneous actual fields whose joint period matrix prevents the radial capacity escape;
- a calibrated structure with controlled zeros and a quantitative extension across them, strong enough to apply to all metrics in a natural geometric subclass and yield a new Einstein-gap statement there.

**Continue** only when a concrete family and exact all-metric quantifier are supplied. **Adjust** if the field gives only one-metric rigidity. **Stop** treating existence of an unconstrained harmonic form as sufficient input for a universal gap.

## 5. Strategic relation among density, cell cost, and degeneration

O10 and O11 should not be conflated, but they are linked by cell economics. O11 asks for the first derivative of the optimal cost when topological cells are sparse: does each blowup/handle force the standard first-order payment, or can interactions lower it? An O10 escape at unbounded \(\chi/A\) would require topology of one chirality to proliferate while its compatibility cost per unit volume tends to zero. A plausible geometric escape would therefore be a network of increasingly cheap opposite-chiral cells whose scalar/Weyl/transition costs collectively vanish. Conversely, a density-independent endpoint would amount to proving that such proliferation cannot erase the actual-field charge.

This suggests a longer-term unification through a density-dependent cell-energy function: low-density slope is the O11 coefficient; high-density behavior controls O10; equality and near-equality describe the limiting cell packing, bubble tree, or diffuse phase. The current finite-density result shows positivity on every bounded density interval but its polynomial lower bound may decay. Determining whether that decay reflects real cell interactions or only loss in the proof is a central mathematical question.

## 6. Primary sources and inherited files used

- `Skills/geometric-analysis/references/results-and-questions.md`
- `Skills/geometric-analysis/research/paper/sections/finite_density_endpoint.tex`
- `Skills/geometric-analysis/research/paper/open_problems.tex`
- `Skills/geometric-analysis/research/Curvature_Realizability.tex`, especially the unbounded-density radial sections around lines 37900–38730
- `Skills/geometric-analysis/research/paper/sections/field_interfaces_and_curvature_interactions.tex`
- `Skills/geometric-analysis/research/paper/sections/variational_geometry.tex`
- `Skills/geometric-analysis/research/paper/sections/variational_selection_and_global_cost.tex`
- `Knowledge/objects/papers/Weyl-Curvature-Einstein-Metrics-and-Seiberg-Witten-Theory--010d90d7328e--6fed64eff4e5/object.md`
- `Knowledge/objects/papers/Weyl-energy-and-connected-sums-of-four-manifolds--aac98700a100--c47de95b9e22/object.md`
- `Knowledge/objects/papers/Decreasing-Weyl-s-energy-by-connected-sums-with-locally-conformally-flat--11b0a0441be3--33e40653ce36/object.md`
- `Knowledge/objects/papers/Seiberg-Witten-invariants-and-pseudo-holomorphic-subvarieties-for-self-d--e08aaea42bbd--110dfa965f9f/object.md`



---

## Source step2_blowup_cell_problem_O11.md

Original: [sources/Sessions/S1003A02/workspace/notes/step2_blowup_cell_problem_O11.md](../sources/Sessions/S1003A02/workspace/notes/step2_blowup_cell_problem_O11.md)

# Step 2 — the blow-up cell problem behind O11: exact reduction and the first U(2) computation

## 1. Exact reduction of the coefficient question to a W⁺/scalar functional

Conventions: Hilbert–Schmidt norms on two-forms (manuscript convention), \(S=\int s^2\), \(W_\pm=\int|W^\pm|^2\), \(P=\int|\mathrm{Ric}^\circ|^2\), \(T_+=2\chi+3\tau\). The identity \(4\pi^2T_+=S/24+2W_+-P/2\) gives, for every metric on a closed manifold,
\[
P=\frac{S}{12}+4W_+-8\pi^2T_+ .
\]
On \(M=X\#k\overline{\mathbb{CP}}^2\#\ell(S^1\times S^3)\) with \(A=c_1^2(X)\), \(Q=k+4\ell\), \(T_+(M)=A-Q\). For the Kähler–Einstein metric on \(X\), \(S_{KE}=32\pi^2A\) and \(W_+^{KE}=S_{KE}/24=\tfrac43\pi^2A\). Hence the **exact** all-metric identity
\[
\boxed{P(g)-8\pi^2Q=\frac{S(g)-32\pi^2A}{12}+4\Bigl(W_+(g)-\tfrac43\pi^2A\Bigr).}
\]
LeBrun's polarized scalar estimate gives \(S(g)\ge32\pi^2A\) for every metric on the blow-ups (its supply for the handle summands must be taken from the corpus' supply statements). Thus:

* the O11 coefficient-4 lower bound \(\inf P\ge8\pi^2Q-o(Q)\) holds as soon as \(W_+(g)\ge\tfrac43\pi^2A-o(Q)\) for metrics with \(P=O(Q)\);
* conversely, any competitor with a better coefficient must lower the self-dual Weyl energy below its Kähler–Einstein value by an amount \(\gtrsim Q\) while its scalar excess stays below \(48\times\) that deficit.

Equivalently, with \(\Phi(g)=\frac1{4\pi^2}\int(s^2/24+2|W^+|^2)\), coefficient 4 is \(\inf\Phi=A-o(Q)\). LeBrun's Weyl–scalar estimate gives only \(\Phi\ge\frac23A\) (this is exactly the Einstein obstruction \(k<A/3\)); the recovery metrics give \(\Phi\to A\). So **O11 is the asymptotic, small-\(h\) form of the sharpening of LeBrun's 2/3 estimate** — the same quantity whose sharp value would decide Einstein metrics on blow-ups with \(k<A/3\). (Literature status of a sharp \(\Phi\)-bound should be confirmed by a knowledge request before any novelty statement.) This explains why separate infima cannot settle O11: the relaxation using only \(S\ge32\pi^2A\) and \(\int(s-\sqrt6|W^+|)^2\ge72\pi^2A\) has optimum \(F=S/12+4W_+=\tfrac{16}3\pi^2A<8\pi^2A\), attained at \(|W^+|/|s|=\sqrt6/48\), far from the Kähler ratio \(1/(2\sqrt6)\).

For a cell \(U\) (blown-up ball) that replaces a complex-hyperbolic ball \(B\) and agrees with it near \(\partial B\), Gauss–Bonnet and signature with identical boundary data give
\[
P(U)=8\pi^2+4\,\Delta W_++\frac{\Delta S}{12},\qquad \Delta=\int_U-\int_B .
\]
Because the bulk is Einstein, \(P(M)=\sum_{\rm cells}P(U_i)\) for sparse disjoint cells. With covers of a fixed ball quotient (injectivity radius \(\to\infty\)), any fixed cell can be planted at \(k_j\ll A_j\) sites; a single cell with \(P(U)<8\pi^2\) would give \(\limsup\alpha_j/h_j<4\) on blow-up subfamilies. So the decisive non-perturbative constructive test is \(\inf_U P(U)\) over complete cells.

## 2. Exact Kähler U(2) cells

U(2)-invariant metrics in the coordinate \(x=b^2\): \(g=\frac{dx^2}{4G}+F\sigma_3^2+x(\sigma_1^2+\sigma_2^2)\) (round unit \(S^3=\sum\sigma_i^2\)). Bolt (exceptional sphere of self-intersection −1, area \(\pi x_0\)): \(F(x_0)=G(x_0)=0\), \(F'(x_0)G'(x_0)=1\). Complex hyperbolic (Ric = −6g): \(F=G=x+x^2\); Burns: \(F=G=x-x_0\), \(P=8\pi^2\) exactly (checked). Kähler iff \(F=G=K\); then \(s=(8-4(xK)'')/x\), \(|\mathrm{Ric}^\circ|^2=4(x^2K''+2x-2K)^2/x^4\), and with \(K=x+H\), \(P=4\pi^2\int L^2x^{-3}dx\), \(L=x^2H''-2H\). The Euler–Lagrange solution is \(L=c_1x^3+c_2\), giving the exact optimum (script `kahler_cell_exact.py`)
\[
\frac{P_{\rm K\ddot ahler}}{8\pi^2}=1+6x_0+9x_0^2(1+X^{-2})+O(x_0^3)\quad(\text{gluing radius }X=\sinh^2R).
\]
The linear term coincides with the global Hodge-index bound for Kähler metrics on \(X\#k\overline{\mathbb{CP}}^2\): \(\int s^2\ge32\pi^2(c_1\cdot[\omega])^2/[\omega]^2\) gives \(P\ge8\pi^2k(1+2\varepsilon)\) with \(\varepsilon=3x_0\) in these units. Kähler cells therefore never beat \(8\pi^2\).

## 3. Non-Kähler U(2) cells (numerical; scripts `u2_curvature.py`, `u2_xcoord.py`, `u2_cell_jax_log.py`)

Parametrization: \(F=K_{\rm opt}e^{\phi p_1}\), \(G=K_{\rm opt}e^{\phi p_2}\), Chebyshev polynomials of degree 12 in \(u=\log(x/x_0)/\log(X/x_0)\), \(\phi=(1-u)^3\), bolt constraint \(p_1+p_2=0\) at \(x_0\); exact JAX gradients, L-BFGS. The identity \(P-8\pi^2=4\Delta W_++\Delta S/12\) is reproduced to \(10^{-8}\)–\(10^{-12}\) in every run, an independent check of the curvature formulas and orientation. Data: `workspace/data/u2grid/u2_cell_grid2.jsonl`; figure `workspace/figures/u2_cell_cost.png`.

| \(x_0\) | \(X\) | Kähler opt. \(P/8\pi^2\) | non-Kähler min | slope \((P/8\pi^2-1)/x_0\) | \(4\Delta W_+/8\pi^2\) | \(\Delta S/12/8\pi^2\) |
|---|---|---|---|---|---|---|
| 0.0003 | 10 | 1.0018008 | 1.0017942 | 5.981 | 0.00119 | 0.00060 |
| 0.003 | 10 | 1.01808 | 1.01763 | 5.876 | 0.0116 | 0.0060 |
| 0.03 | 10 | 1.1882 | 1.1636 | 5.45 | 0.100 | 0.063 |
| 0.1 | 10 | 1.6915 | 1.5073 | 5.07 | 0.279 | 0.229 |
| 0.3 | 50 | 3.611 | 2.453 | 4.84 | 0.650 | 0.802 |
| 1.0 | 50 | 16.06 | 6.42 | 5.42 | 1.67 | 3.74 |
| 3.0 | 50 | 103.0 | 25.6 | 8.2 | 4.5 | 20.1 |
| 10 | 50 | 1277 | 198 | 19.7 | 23.6 | 173.8 |

Results are insensitive to \(X\in\{2,10,50\}\) at fixed \(x_0\) (cells are local). Observed facts:

1. Every computed U(2) cell has \(P>8\pi^2\); the cost increases with the bolt size, and the infimum \(8\pi^2\) is approached only as \(x_0\to0\) (shrinking Burns bubble). It is not attained.
2. The first-order penalty is \(6x_0\) for non-Kähler cells as well: the non-Kähler improvement over the Kähler optimum is of second order (\(\approx0.06x_0\) at \(x_0=3\cdot10^{-4}\), \(\approx0.5x_0\) at \(x_0=0.03\)).
3. Both pieces pay separately at every tested size: \(\Delta W_+>0\) and \(\Delta S>0\); near the Burns limit they split exactly as in the Kähler case, \(4\Delta W_+\approx4x_0\), \(\Delta S/12\approx2x_0\) (units \(8\pi^2\)). The opposite energy satisfies \(W_-(U)>12\pi^2\) (the Burns value).

## 4. Interpretation and its range

Within U(2) symmetry, a blow-up cell planted in complex-hyperbolic space cannot lower the first-order Einstein-gap coefficient: the per-site cost is \(8\pi^2(1+6x_0+\dots)\) with \(\pi x_0\) the exceptional area in Ric = −6g units; scale-invariantly, \(8\pi^2\bigl(1+|\lambda|\,\mathrm{Area}(E)/\pi+\dots\bigr)\) with \(\mathrm{Ric}=\lambda g\) outside the cell. The correction is positive and linear in the exceptional area times background curvature, so near-minimizers must concentrate their blow-up bubbles at vanishing scale. This is a concrete near-extremal/degeneration statement: within this class the infimum is a bubbling limit, consistent with nonattainment of \(\alpha\).

A mechanism for the universality of the coefficient 6 beyond U(2): Burns minimizes \(4W_++S/12\) among asymptotically flat fillings of the blow-up (where it vanishes), so it is a critical point of \(P\) for decaying variations. In a scaled gluing \(g_\varepsilon\), any change of the bubble's shape enters at second order, while the order-\(\varepsilon^2\) term is a boundary pairing between the Burns \(r^{-2}\) asymptotic mode (Kähler mass \(x_0\)) and the background curvature at the site. For a complex-hyperbolic background this pairing is U(2)-invariant, so its value should be the same for non-symmetric competitors: \(P=8\pi^2(1+6x_0)+O(x_0^2\log)\). Proving this would give a rigorous first-order statement: no small-scale perturbation of a Burns bubble, symmetric or not, lowers the per-site cost.

What the computation does not cover: cells without U(2) symmetry; clusters of several blow-ups in one cell (multi-centre/toric cells, same \(Q\)); handle cells \(S^1\times S^3\) (cost \(32\pi^2\)); non-monotone \(b\) (necks inside the cell); the full balanced family, whose lower bound also uses the opposite chirality through \(U=3\min(T_+,T_-)/A\). Numerical minima are upper bounds for the U(2) infimum only within the parametrization.

## 5. Work that would decide O11 from here

* **Perturbative theorem (both sides at once).** Prove \(P(g)\ge8\pi^2(1+6x_0)-Cx_0^2\log(1/x_0)\) for all metrics \(C^{2}\)-close (in weighted norms) to a scaled Burns bubble glued into a complex-hyperbolic background, without symmetry. This upgrades "coefficient 4 in recovery neighbourhoods" to a quantitative strict per-site penalty and identifies the boundary pairing.
* **Non-perturbative cells without symmetry.** The cell problem \(\inf_U P(U)\) is a well-posed local variational problem. The natural next class is \(T^2\)-invariant (toric) cells, which contain multi-centre blow-up clusters and Gibbons–Hawking/LeBrun hyperbolic-ansatz metrics; cohomogeneity two, still computable.
* **Local W⁺ inequality.** The data suggest the stronger local statement \(\Delta W_+\ge0\) for every cell. A proof (even in U(2)) would follow from a local SW/Kähler-calibration argument and would be the cell form of the needed global inequality \(W_+\ge\frac43\pi^2A-o(Q)\).
* **Positioning.** Request literature on sharp lower bounds for \(\int(s^2/24+2|W^+|^2)\) and \(\int|W^+|^2\) on blow-ups of minimal general-type surfaces (LeBrun 1998–2004, Gursky, Sung, Kim) and on Einstein metrics on \(X\#k\overline{\mathbb{CP}}^2\) for \(k<c_1^2/3\).



---

## Source step2_synthesis_O10_O11.md

Original: [sources/Sessions/S1003A02/workspace/notes/step2_synthesis_O10_O11.md](../sources/Sessions/S1003A02/workspace/notes/step2_synthesis_O10_O11.md)

# Step 2 synthesis — O10/O11 combined research state

## A. O10: Taub–NUT tangent blocks the simplest proof strategy

### Key finding (from TTCS generator 2, verified against the extract)

The full leading coupled tangent system at a radial-energy concentration scale admits a **nontrivial complete solution**: one-centre Taub–NUT with an opposite-chiral spinor from a holomorphic coordinate. Its amplitude is
\[
m=m_*\frac{R}{R+\ell},\qquad m_*=128/81,
\]
which has a genuine lower well (m→0 at the nut, m→m* at infinity), nonzero radial Dirichlet energy ∫|∇v|²=8π²m*ℓ², and satisfies all of:
- Ric=0, W⁺=0 (leading metric is hyper-Kähler)
- F_A=0 (determinant connection flat at leading order)
- ∇_AΦ₀=0, |Φ₀|²=4/3 (parallel positive spinor)
- D⁻v=0, P_{J+}∇v=0, ∇*∇v=0 (Dirac, type, rough-harmonic)
- Both curvature equations (3.6) hold (real Levi-Civita connection)
- First-order torsion parent exists (linear perturbation of parallel Φ₀)

The connection supporting the well is the **actual ASD spin connection of Taub–NUT**, which is instanton-like.

### What this rules out
A density-free endpoint proof cannot use a Liouville theorem asserting "every complete finite-energy geometric tangent with nonzero radial mass is trivial." The round S³-warped, flat R²×T², and ALE HK ansätze *are* obstructed (the first by Ricci flatness ⟹ flatness, the second by bounded harmonic functions on R², the third by ALE end representation theory + Bishop–Gromov). Taub–NUT escapes because its end is ALF (circle-collapsed), not ALE.

### What remains for O10
Two specific mathematical objects could still save the density-free theorem:
1. **Order-r² field compatibility**: at leading order F_A=0; the monopole source and bounded determinant-curvature model are order r². Completing the equations at order r² on Taub–NUT gives a coupled linear system for (k, a, Φ₂) with radial ODE reduction in the biaxial equivariant sector. Solvability with decaying/matchable asymptotics is the precise question.
2. **ALF end matching cost**: Taub–NUT has an asymptotically finite Hopf circle. Embedding it into a noncollapsed closed manifold may force a scale-invariant Ricci cost that cannot be sent to zero. This is a transition-annulus calculation, not a global identity.

If (1) has a decaying solution and (2) has affordable matching, the Taub–NUT local core becomes a genuine building block for an O10 escape. If either has an obstruction, that obstruction identifies the specific identity needed for a general proof. Either outcome is a scientific advance.

## B. O11: comprehensive cell-problem picture

### Exact reduction (verified by TTCS verifier)
\[
P(g)-8\pi^2Q=4\bigl(W_+(g)-\tfrac43\pi^2A\bigr)+\frac{S(g)-32\pi^2A}{12}
\]
and for a single cell U replacing a CH ball B:
\[
P(U)-8\pi^2=4\Delta W_++\frac{\Delta S}{12}.
\]
Burns gives exactly 8π²; every U(2)-invariant cell computed has P > 8π², with slope (P/8π²−1)/x₀ → 6 as x₀→0. The split is 4ΔW+ → 4x₀ and ΔS/12 → 2x₀ (units of 8π²).

### S1003A01 triaxial result (conformal SU(2)-diagonal, message 739)
Their independent numerical optimization over a broader ansatz (full conformal triaxial) confirms: no sub-threshold cell. All optima lie above the conformal Kähler lower bound of Theorem 1 of the corpus (I54). Non-Kähler (triaxial w-direction) only decreases at high cost, never crossing the threshold. Conjecture C1: the Theorem 1 bound holds for the entire conformal almost-Kähler diagonal class.

### TTCS verifier corrections and clarifications
1. `u2_curvature.py` labels chirality opposite to the complex orientation; `u2_xcoord.py` correctly swaps. Code is substantively correct but documentation should be fixed.
2. The Kähler formula 1+6x₀+9x₀²(1+X⁻²) is a small-x₀ expansion, not the exact finite-X expression. In the limit X→∞ it becomes exactly (1+3x₀)².
3. The outer matching is C¹/H², not literally CH on an open collar (can be smoothed with vanishing error).
4. "Every U(2) cell has P > 8π²" is *not proved*; only every returned parametrized profile has that property. Numerical minima are upper bounds.
5. The slope-6 universality heuristic misses a possible relative-orientation modulus (angle between Burns and CH Kähler forms). The U(2) computation tests only the aligned case θ=0.

### TTCS generator 1: ΔW+ ≥ 0 is likely false
The strict total-Weyl connected-sum construction gives δ(W++W−) < 0 with δ(W+−W−) = 0 (signature), hence δW+ = δW− < 0. If that construction can be localized to a cell, then ΔW+ < 0. The real question is the *joint* bound P(U) ≥ 8π², not the separate ΔW+ ≥ 0.

### Most decisive next tests for O11
1. **Burns weighted deformation complex**: classify the kernel on Burns, compute the boundary pairing −8π²λm_K, prove or disprove orientation-universality.
2. **Strict Weyl one-neck + conformal scalar minimization**: on the Malchiodi–Malizia gluing metric, fix the Weyl energy and minimize S inside the cell by a conformal factor; this is a scalar fourth-order BVP. If the scalar saving exceeds 48 times the Weyl deficit, P(U) < 8π².
3. **Non-monotone-b cells (internal neck)**: use full biaxial Bianchi IX to allow a(t) turning points, multiple throats, and long near-Einstein segments.
4. **Composite blow-up+handle cells**: the balanced family has k/ℓ = 8/7; test P(U_{1,1}) < 40π² as the minimal compound.

## C. Research priorities

| Priority | Question | Object to compute | Decides |
|---|---|---|---|
| 1 | O10 order-r² completion | Coupled (k,a,Φ₂) radial ODE on Taub–NUT | Whether ALF escape or new obstruction identity |
| 2 | O11 Burns perturbative theorem | Weighted kernel + boundary pairing + orientation | Per-site penalty universality |
| 3 | O11 Weyl gluing cell cost | Θ = 4ΔW+ + ΔS/12 on MM metric | Whether strict Weyl saving lowers P |
| 4 | O10 ALF matching cost | Transition annulus Ric cost for circle scaling | Whether noncollapsed embedding is affordable |

## D. Files

- `workspace/notes/step2_blowup_cell_problem_O11.md` — detailed O11 cell reduction, exact Kähler formula, numerical table and interpretation
- `workspace/notes/step1_field_compatibility_and_route_portfolio.md` — inherited route portfolio from Step 1
- `workspace/scripts/u2_curvature.py`, `u2_xcoord.py`, `kahler_cell_exact.py`, `u2_cell_jax_log.py` — computation chain
- `workspace/data/u2grid/u2_cell_grid2.jsonl` — full numerical results
- `workspace/figures/u2_cell_cost.png` — cell cost figure
- `trace/ttcs/results/step2_ttcs01_generator1_integration.md` — O11 full generator memo
- `trace/ttcs/results/step2_ttcs01_generator2_integration.md` — O10 Taub–NUT tangent memo
- `trace/ttcs/results/step2_ttcs01_verifier1_integration.md` — verification of cell computation



---

## Source step4_O10_localization_and_orbifold_test.md

Original: [sources/Sessions/S1003A02/workspace/notes/step4_O10_localization_and_orbifold_test.md](../sources/Sessions/S1003A02/workspace/notes/step4_O10_localization_and_orbifold_test.md)

# Step 4 — Where density can matter: an elementary density-free endpoint, the 3/4 window, Kähler closure of O10, and the orbifold-limit test

Conventions are those of `Skills/geometric-analysis/references/conventions-and-literature.md`
(operator Hilbert–Schmidt Weyl norms, $S=\int s^2$, $P=\int|\mathrm{Ric}^\circ|^2$,
$W=\int|W^+|^2$, $T_+=2\chi+3\tau$, $p=(a_g^+)^2$). The endpoint quantity is
the one of `thm:finite-density-endpoint`
(`Skills/geometric-analysis/research/paper/sections/finite_density_endpoint.tex`, l.13–43):
$$
\kappa_\beta(g)=\fint|\mathrm{Ric}+g|^2+\frac{D_\beta}{V},\qquad
D_\beta=(1+\beta^{-1})S+6(\beta+1)W-72\pi^2p ,
$$
for **every** metric $g$ of the conformal class (it is not scale invariant; the factor $g$ fixes the scale).
Symbolic checks: `workspace/scripts/o10_localization.py` → `workspace/data/o10_localization.json`.

## 1. Exact rewriting

Since $|\mathrm{Ric}+g|^2=|\mathrm{Ric}^\circ|^2+(s+4)^2/4$ and
$4\pi^2T_+=S/24+2W-P/2$, i.e. $P=S/12+4W-8\pi^2T_+$,
$$
V\kappa_\beta=\Bigl(\tfrac{13}{12}+\tfrac1\beta\Bigr)S+(6\beta+10)W+\int\frac{(s+4)^2}{4}-8\pi^2T_+-72\pi^2p. \tag{1.1}
$$
LeBrun's estimate $\int(s-\sqrt6|W^+|)^2\ge72\pi^2p$ (valid for every metric when the
actual monopole exists) and the pointwise inequality $(x+y)^2\le(1+\gamma^{-1})x^2+(1+\gamma)y^2$ give,
for every $\gamma>0$,
$$
72\pi^2p\le(1+\gamma^{-1})S+6(1+\gamma)W. \tag{1.2}
$$
(With $\gamma=\beta$ this is $D_\beta\ge0$.)

## 2. Theorem L (density-free endpoint below the 3/4 ratio)

**Hypotheses.** Actual conformal monopole supply as in `thm:finite-density-endpoint`,
$p\ge A>0$, $a^2\ge T_+$, and $T_+\le\theta A$ for a number $\theta<3/4$.
**No Euler-density bound.**

**Conclusion.** There is $c(\theta)>0$, independent of the manifold, structure, $A$, metric and $\beta$, with
$$
\kappa_\beta(g)\ge c(\theta)\frac{(\beta-2)^2}{\beta^2}\qquad(\beta\ge2).
$$

**Proof.** If $T_+<0$ put $\theta=0$ below (drop $-8\pi^2T_+\ge0$). Otherwise
$T_+\le\theta A\le\theta p$, so $-8\pi^2T_+-72\pi^2p\ge-72\pi^2\lambda p$ with $\lambda=1+\theta/9$.
Insert (1.2) with $\gamma=\gamma_{\max}=(9\beta-\theta+6)/(\theta+9)$, the value that cancels the $W$
coefficient $(6\beta+10)-6\lambda(1+\gamma)$. Then
$$
V\kappa_\beta\ge\int\Bigl(a\,s^2+\frac{(s+4)^2}{4}\Bigr),\qquad
a(\theta,\beta)=\frac{(\tfrac34-\theta)\beta^2+(\tfrac12-\tfrac{11}{4}\theta)\beta+6-\theta}{\beta(9\beta-\theta+6)} .
$$
For $a>0$ the pointwise minimum of $as^2+(s+4)^2/4$ is $16a/(4a+1)$, so
$\kappa_\beta\ge16a/(4a+1)$. The numerator $N(\beta)$ of $a$ is quadratic in $\beta$ with leading
coefficient $3/4-\theta>0$ and discriminant
$$
\mathrm{disc}(\theta)=\tfrac{57}{16}\theta^2+\tfrac{97}{4}\theta-\tfrac{71}{4}
=\tfrac{57}{16}\bigl(\theta-\tfrac23\bigr)\bigl(\theta+\tfrac{142}{19}\bigr).
$$
* $\theta<2/3$: $N>0$ for all $\beta$, and $a(\theta,\beta)\to a_\infty=1/12-\theta/9$; hence
  $\inf_{\beta\ge2}a>0$ and the bound holds for every $\beta\ge2$ from (1.1)–(1.2) alone.
* $2/3\le\theta<3/4$: $N<0$ exactly on an interval $(\beta_-(\theta),\beta_+(\theta))$ containing $\beta=8$
  ($\theta=2/3$ gives the double root $\beta=8$); $\beta_+(\theta)\to\infty$ as $\theta\uparrow3/4$
  (e.g. $\theta=0.74$: roots $\approx3.5,150$). For $\beta\ge2\beta_+(\theta)$ the elementary bound applies with
  $a\ge a_0(\theta)>0$. For $2\le\beta\le2\beta_+(\theta)$ use the density-free single-solution parameter estimate
  (results-and-questions §2): since $a^2\ge T_+\ge0$, $b=(-a^2)_+/V=0$ and
  $\kappa_\beta\ge(P+D_\beta/\beta)/V\ge c_{\rm par}(\beta-2)^2/\beta^4\ge c_{\rm par}(2\beta_+)^{-2}(\beta-2)^2/\beta^2$.
  When $T_+<0$ the case $\theta=0$ of the first bullet applies for every $\beta$ ($a(0,\beta)=\frac{\beta^2/4+\beta/6+2}{\beta(3\beta+2)}\ge1/12$). $\square$

*Scope check still owed.* The elementary branch holds for every metric of the class. The bounded-$\beta$ branch
quotes the single-solution parameter estimate, which results-and-questions §2 states on the $s=-4$ Yamabe
representative; for arbitrary metrics of the class one must use the same conformal transfer the corpus uses in
`thm:finite-density-endpoint` (read its proof for the transfer before citing Theorem L for non-Yamabe metrics).
For $\theta<2/3$ no such issue arises.

Values of the $\beta\to\infty$ constant $16a_\infty/(4a_\infty+1)$: $\theta=0$: $1$; $\theta=1/2$: $0.4$;
$\theta=2/3$: $1/7$; $\theta=0.74$: $0.0177$ (table in the JSON).

**What the proof shows structurally.** The *same quadratic* produces two classical thresholds:
uniformity in $\beta$ fails first at $\theta=2/3$ with the double root at $\beta=8$ — exactly LeBrun's
Einstein-obstruction ratio and the corpus' Chern–Weil-aligned parameter
($D_8=108\pi^2(T_+-2p/3)+27P/2$, in which $S$ and $W$ cancel). The large-$\beta$ endpoint fails only at
$\theta=3/4$. Thus Chern–Weil + LeBrun see everything except the window $T_+/A\ge3/4$ at large $\beta$.

## 3. The $\beta=\infty$ saturation configuration

Suppose $\kappa_{\beta_j}(g_j)\to0$ with $\beta_j\to\infty$ (the only regime the finite-density
theorem needs density for). From (1.1)–(1.2): $P/V\to0$, $\fint(s+4)^2\to0$, $\beta_jW/V\to0$, and
$S-72\pi^2p=o(V)$. Hence, asymptotically,
$$
p/V\to\frac{2}{9\pi^2},\qquad T_+/V\to\frac1{6\pi^2},\qquad \frac{T_+}{p}\to\frac34 ,
$$
the numerology of a negative Einstein metric with $W^+=0$ (e.g. real hyperbolic, or a complex-hyperbolic
quotient with reversed orientation) carrying a monopole that **saturates LeBrun's estimate at $W^+=0$**,
$S=72\pi^2p$. Such saturation is impossible on a smooth closed manifold (equality in LeBrun's improved
estimate forces Kähler–Einstein, whose $|W^+|=|s|/(2\sqrt6)\ne0$). So:

> **O10 in its exact form** = uniform-in-density quantitative strictness of LeBrun's $W^+$-improved
> estimate on almost-$W^+$-flat, almost-negative-Einstein geometries, in the window $T_+\ge\frac34A$.

The Euler number is invisible in all of these limits: $W^-$ enters none of $P,S,W,T_+$. Indeed
$8\pi^2\chi/V\to2/3+\fint|W^-|^2$, so $\chi/A\to\infty$ means $\fint|W^-|^2\to\infty$, i.e. $W^-$-bubbles.
For symplectic minimal $M$ with $a=c_1(K)$ one has $a^2=T_+$, so saturation needs
$p=(a^+)^2\to\frac43a^2$, i.e. $(a^-_g)^2\to-\frac13a^2$: the harmonic ASD part of the canonical class must be
macroscopic — the opposite of Kähler geometry, where $a^-=0$.

## 4. Kähler surfaces: O10 holds (Corollary K)

Let $X$ be a minimal Kähler surface of general type with $p_g\ge1$ ($b_+\ge3$), $A=c_1^2(X)$, and
$M=X\#k\overline{\mathbb{CP}}^2$ for any $k\ge0$, with LeBrun's blow-up supply (for each conformal class a
basic class $\pm K_X\pm E_1\pm\cdots$ with $p\ge A$; $a^2=T_+=A-k$). Then
$\kappa_\beta\ge c_K(\beta-2)^2/\beta^2$ for all $\beta\ge2$, all metrics, all $k$, with a universal $c_K>0$.

*Proof.* If $k\ge0.3A$ then $T_+\le0.7A$: Theorem L with $\theta=0.7$. If $k<0.3A$, Noether's inequality
$c_2\le5c_1^2+36-12q$ for minimal surfaces of general type gives $\chi(M)/A\le5.3+36/A\le41.3$, and
`thm:finite-density-endpoint` applies with $B=41.3$. $\square$

So no counterexample to O10 can be Kähler (or a blow-up of Kähler); the window $T_+\ge\frac34A$ together
with $\chi/A\to\infty$ forces non-Kähler manifolds far below the Noether line, $b_-\approx5b_+$ — e.g.
minimal symplectic manifolds with $0<c_1^2\ll\chi$. **The window is nonempty:** Braungardt–Kotschick
(`Knowledge/objects/papers/Einstein-metrics-and-the-number-of-smooth-structures-on-a-four-manifold--937ef5235565--e616882f6ef1/object.md`,
Theorem 4) realise every first-quadrant lattice point $(\chi_h,c_1^2)$ with $c_1^2\le(9-\epsilon)\chi_h-c(\epsilon)$ by
infinitely many simply connected minimal symplectic manifolds. Fix $c_1^2=A\ge1$ and let $\chi_h\to\infty$: $b_+=2\chi_h-1\ge3$,
Taubes gives the canonical-class monopole for every metric, $p\ge a^2=c_1^2=A$, $a^2=T_+$, and
$\chi/A=(12\chi_h-A)/A\to\infty$. For those, $T_+=A$, $\theta=1$, squarely in the window. **These are the
manifolds on which O10 is genuinely open.**

**Quantitative Hitchin–Thorpe (no field input).** For every metric, $P\ge S/12-8\pi^2T_+$; hence if
$T_+\le0$ then $\mathcal J=4P/(P+S/4)\ge1$, and $\mathcal E\ge\mathcal J\ge1$ (the $R=0$ case has $\mathcal E=4$).
Same with $T_-$. So $\alpha(M)\ge1$ whenever $2\chi\le3|\tau|$; product metrics on $S^2\times\Sigma_g$
($g\ge2$) give $\mathcal E=4-2(K_1+K_2)^2/(K_1^2+K_2^2)\to2$, so $1\le\alpha(S^2\times\Sigma_g)\le2$. The sharp
value in this region is a separate (fieldless) question.

## 5. Orbifold-limit test (strategist's test), computed

Let $X_0$ be a Kähler–Einstein orbifold of general type ($s=-4$) whose singular points are of type
$A_{k_i-1}$ ($\mathbb C^2/\mathbb Z_{k_i}$, $SU(2)$ action), and $Y\to X_0$ its minimal (crepant) resolution: $Y$ is a
smooth minimal surface of general type with $(-2)$-curve chains, $K_Y=\pi^*K_{X_0}$ nef, not ample, so $Y$ has
no Kähler–Einstein metric.

*Glued metrics.* Insert Kronheimer's hyperkähler ALE $A_{k-1}$ metrics scaled by $\varepsilon^2$, cut off at
$r\sim\varepsilon^{1/2}$ (orbifold metric $=$ flat $+O(r^2)$, ALE metric $=$ flat $+O(\varepsilon^4r^{-4})$). The error is
supported on annuli of volume $O(\varepsilon^2)$ with bounded curvature error, and the cores have volume
$O(\varepsilon^4)$; hence $\fint|\mathrm{Ric}+g|^2=O(\varepsilon^2)$ and $\alpha(Y)=0$.

*Field terms.* The ALE cores are Ricci-flat Kähler for the same complex structure, so $s=0$ and $W^+=0$
there (complex orientation): they contribute nothing to $S$ or $W$. Their $L^2$ harmonic forms are ASD and
$K_Y\cdot E=0$ for every exceptional curve, so $p(g_\varepsilon)\to K_Y^2$. With the KE values
$|W^+|^2=2/3$, $p=V/2\pi^2$,
$$
\kappa_\beta(g_\varepsilon)\longrightarrow\frac{4(\beta-2)^2}{\beta}\qquad(\text{exactly the KE orbifold value}).
$$
So on this sequence the whole endpoint gap is carried by $D_\beta$ (bulk misalignment of $W^+$ from $|s|/(\beta\sqrt6)$),
the Ricci part tends to zero, and $\kappa_2\to0$. $Y$ lies in the bounded-density range (Noether) and in the
window ($T_+/A=1$), consistently with the theorem.

*Meaning for the human question.* $Y$ gives $\alpha(Y)=0$ (arbitrarily good integral approximation) on a
manifold with no Kähler–Einstein metric. **Correction to the expected obstruction:** the leading
Biquard/Ozuch obstruction to Einstein desingularization is $\det\mathbf R^+(x)=0$ with
$\mathbf R^+=W^++\tfrac s{12}$ on $\Lambda^+$ (Ozuch I, `Knowledge/objects/papers/Noncollapsed-degeneration-of-Einstein-4-manifolds-I--20d576a9333c--50e8cddb3834/object.md`, l.89–130),
not $\det W^+=0$. At a KE point $W^+=\mathrm{diag}(s/6,-s/12,-s/12)$, so $\mathbf R^+=\mathrm{diag}(s/4,0,0)$ has rank one and
$\det\mathbf R^+=0$: **the leading obstruction is satisfied** and does not exclude Einstein metrics near the limit.
The Kähler route is obstructed cohomologically ($K_Y\cdot E=0$, $K_Y$ not ample). The LeBrun–Ozuch rigidity
(admissible Einstein sequences converging to conformally Kähler orbifolds are eventually Kähler–Einstein;
`Knowledge/objects/papers/Desingularizations-of-Conformally-Kaehler-Einstein-Orbifolds--8fe1aa31deb8--5b19d560b771/object.md`)
is proved for $\lambda>0$ through Wu's criterion $\det W^+>0$; for negative KE, $\det W^+=s^3/864<0$, so that
mechanism is unavailable. Whether non-Kähler Einstein metrics exist on $Y$ near the orbifold limit is therefore
decided only by higher-order (second-order / tree) obstructions — undecided in the material read so far.
This makes $Y$ the cleanest test of "gap zero vs. existence": a concrete degenerating family with
$\mathcal E\to0$ where both outcomes (a non-KE Einstein metric, or non-attainment) are live. It also shows **$\kappa_\beta$ for $\beta\ne2$ is not an Einstein gap**:
it is a field-alignment gap that stays $\ge4(\beta-2)^2/\beta$ on metrics with $\mathcal E\to0$. The passage from
$\kappa$ to $\alpha$ is the N1 combination with the topological summand $(T_+/A-2/3)_+$, which is $1/3$ on $Y$.

## 6. Consequence for the O10 programme (re-aiming Steps 2–3)

* **Local payments vanish.** $W^+$-flat hyperkähler cores (ALE, or the multi–Taub–NUT tangent of Step 3)
  contribute zero to every term of $\kappa_\beta$ ($P$, $S$-defect $O(\text{vol})$, $W$, and $p$ when $a\cdot E=0$).
  The "positive transition payment per Euler unit" alternative of Step 3 is false locally — the $Y$ sequence
  realises zero local cost per Euler unit. A density-free theorem must be global, as the strategist anticipated.
* **Orbifold bulks are excluded.** If a would-be counterexample had $W^+$-flat bubbles and a bulk converging to
  an orbifold of bounded Euler density, an orbifold version of the finite-density theorem (with the saturation
  of §3 impossible on orbifolds as well) would contradict it. So any O10 counterexample needs essential
  non-orbifold degeneration at the bulk scale: collapse, accumulation of orbifold points, or a shift of the
  harmonic period point $a^-_g$ carried by the degeneration (§3 requires $(a^-)^2\approx-T_+/3$).
* **The live mechanism.** ALF multi–Taub–NUT carries $L^2$ harmonic ASD forms not dual to compact spheres (the
  Taub–NUT form); unlike ALE $(-2)$-classes, they are not killed by $a\cdot E=0$. Whether degenerating ALF cores can
  move the period point so as to give $p\approx\frac43a^2$ while the bulk is $W^+$-flat is the precise question
  that replaces the order-$r^2$ "transition cost" programme. A counterexample would have to realise it on a
  non-Kähler manifold with $T_+\ge\frac34A$, $\chi/A\to\infty$; a theorem would prove quantitative strictness of
  LeBrun's improved estimate uniformly in $\fint|W^-|^2$.

## 7. O11 (kept in view)

Unchanged this Step: the decisive objects are a fixed-scale non-symmetric cell with $4\Delta W_++\Delta S/12<0$
or a lower-bound theorem $P(U)\ge8\pi^2$ for every $\mathbb{CH}^2$-asymptotic cell. Note the analogy now visible:
in O11 the Burns cell has $P(U)=8\pi^2=-8\pi^2T_+(\text{cell})$ exactly by (1.1)-type bookkeeping
($s=0$, $W^+=0$), i.e. the scalar-flat Kähler cell is the $T_+$-saturating object, just as the $W^+$-flat
bubble is the $\chi$-carrying, $T_+$-neutral object in O10.



---

## Source step6_theorems_and_O11_rotation.md

Original: [sources/Sessions/S1003A02/workspace/notes/step6_theorems_and_O11_rotation.md](../sources/Sessions/S1003A02/workspace/notes/step6_theorems_and_O11_rotation.md)

# Step 6 — Theorem library entries (L′, structural quadratic, K, Z) and the O11 relative-orientation computation

Conventions: `Skills/geometric-analysis/references/conventions-and-literature.md`
(V, S=∫s², P=∫|Ric°|², W=∫|W⁺|² operator-HS, T₊=2χ+3τ, p=(a⁺_g)², D_β, E, J).
Session sources: `notes/step4_O10_localization_and_orbifold_test.md`,
`trace/ttcs/results/step5_ttcs01_verifier1_integration.md` (full proof of L′, K),
`trace/ttcs/results/step5_ttcs01_verifier2_integration.md` (zero-gap, Ozuch direction).

This note organises the mathematics in three layers, because the Step 4–5 work showed they are
genuinely different objects:

* **alignment defects** κ_β = ⨍|Ric+g|² + D_β/V (field–curvature alignment for an actual monopole);
* **the Einstein defect** E(g) = inf_λ ∫|Ric−λg|²/(λ²V) and α(M) = inf_g E(g);
* **bridges**: E ≤ κ-type bounds go one way only; the canonical-model sequence (Theorem Z) shows
  κ_β (β≠2) can stay ≥ 4(β−2)²/β while E → 0.

---------------------------------------------------------------------------------------------

## 1. Theorem L′ (density-free alignment endpoint below ratio 3/4)

**Statement.** Fix θ<3/4. Let M be closed oriented, [g] a conformal class, and suppose one fixed
Spin^c structure with determinant class a admits an unperturbed monopole for every metric of [g].
Put p=(a⁺_h)² (conformally invariant), and assume p ≥ A > 0, a² ≥ T₊, T₊ ≤ θA. Then there is
c_L(θ)>0 depending only on θ with

  κ_β(h) ≥ c_L(θ)   for every h∈[g] and every finite β ≥ 2.

No Euler-density hypothesis enters. The hypothesis a² ≥ T₊ is used only when 2/3 ≤ θ < 3/4.

**Proof** (complete; verified by two independent branches, Step 5): exact rewriting
Vκ_β = (13/12+1/β)S + (6β+10)W + ∫(s+4)²/4 − 8π²T₊ − 72π²p; LeBrun split
72π²p ≤ (1+1/γ)S + 6(1+γ)W; optimal γ_max=(9β−θ+6)/(9+θ) cancels W and gives
κ_β ≥ 16a/(1+4a) with a(θ,β)=N_θ(β)/(β(9β−θ+6)); three cases T₊≤0 (κ_β ≥ 1), θ<2/3
(N_θ>0 everywhere), 2/3≤θ<3/4 (bad interval (β₋,β₊)∋8 handled on the Yamabe representative
by the single-parameter theorem with its true factor b=(−a²)₊/V̂ = 0, transfer
κ̂_β ≤ κ_β/(1−√κ_β−κ_β/16), 0≤δ≤D_β). Full text with every inequality: verifier-1 integration
§§2–4. The constant does not survive θ↑3/4 because a_∞(θ)=1/12−θ/9.

## 2. Structural theorem: one quadratic produces 2/3, β=8 and 3/4

N_θ(β) = (3/4−θ)β² + (1/2−11θ/4)β + 6−θ,  disc N_θ = (57/16)(θ−2/3)(θ+142/19).

(i) θ<2/3: N_θ>0 for all β; (ii) θ=2/3: N_{2/3}(β)=(β−8)²/12 (double root at β=8);
(iii) 2/3<θ<3/4: N_θ<0 exactly on (β₋,β₊) with 2<β₋<8<β₊; (iv) θ=3/4: leading coefficient
vanishes, a_∞=0. Together with the Chern–Weil identity D₈ = 108π²(T₊−(2/3)p) + (27/2)P,
this shows that LeBrun's Einstein-obstruction ratio 2/3, the corpus's aligned parameter β=8, and
the large-parameter threshold 3/4 are the discriminant zero, its double root, and the vanishing
of the leading coefficient of a single quadratic. Interpretation: the elementary Chern–Weil +
LeBrun information is exhausted precisely in the window T₊ ≥ (3/4)A, β→∞, whose zero
sequences would have to saturate LeBrun's W⁺-improved estimate at W⁺=0 (p/V→2/(9π²),
T₊/p→3/4). This is the only place where Euler density can matter.

## 3. Corollary K (Kähler blow-ups)

X minimal Kähler of general type, p_g ≥ 1, A=c₁²(X), M=X#k CP̄². Universal c_K>0:
κ_β(g) ≥ c_K(β−2)²/β² for all metrics, all β≥2. Proof: sign averaging p ≥ A, a²=T₊=A−k;
k ≥ 0.3A → L′ with θ=0.7; k<0.3A → Noether gives χ/A ≤ 53/10+36/A ≤ 41.3 → finite-density
theorem. c_K=min{c_L(7/10), c_FD(41.3)}. The (β−2)² factor is necessary (KE: κ_β=4(β−2)²/β).

---------------------------------------------------------------------------------------------

## 4. Theorem Z (the h=0 endpoint of the balanced theory) — statement and scope

Let X be a compact minimal complex surface of general type, M its underlying smooth manifold.

(Z1) α(M)=0. Construction: canonical model X_can has only ADE singularities and carries an
orbifold Kähler–Einstein metric g_KE with Ric=−g (Kobayashi, Tsuji, Aubin–Yau in orbifold form);
glue Kronheimer ALE hyperkähler metrics of scale ε into each singular point via cut-offs in an
annulus ε^{1/2}-type. Ricci residual is O(1) on a region of volume O(ε²) (plateau + annulus) and
O(ε^2/r^4)-small-times on the transition, so ∫|Ric+g|²/V → 0, hence E→0.
(Ricci-flat cores contribute zero; E is scale-invariant, so normalisation is irrelevant.)

(Z2) Attainment. Because E=(4P+L_s)/R ≥ 0 with E(g)=0 iff Ric=λg with λ≠0, the infimum 0 is
attained iff M carries an Einstein metric with non-zero Einstein constant. (A Ricci-flat metric
has E=4.) For general-type M, λ>0 is impossible (b₊ ≥ 1 with SW class excludes positive
Ricci ... actually λ>0 forces finite π₁ and positive Yamabe, excluded by the SW class), so
attainment ⇔ existence of a negative Einstein metric on M.

(Z3) K_X ample ⇒ attained (Aubin–Yau). K_X nef, not ample ⇒ no KE metric for the given complex
structure; the smooth question (another complex structure obtained by smoothing X_can, or a
non-Kähler Einstein metric) is open in general and is *exactly* the attainment question for α.

(Z4) Local obstruction structure (A₁ points, Ozuch's first two compact obstructions). In the
Kähler splitting of Λ⁺ at a negative KE orbifold point, R⁺ = W⁺ + s/12 = diag(s/4,0,0) = diag(−1,0,0).
First obstruction: gluing direction ζ∈Λ⁺ must satisfy R⁺ζ=0. The holomorphic resolution direction
ζ∥ω fails it; directions ζ⊥ω (rotated hyperkähler / smoothing directions) pass it. The second
obstruction is the determinant of the residual 2×2 block of R⁺ on ω^⊥, which is 0 — passes
automatically. Hence the published obstructions forbid only the holomorphic resolution
direction: they do not exclude Einstein metrics near the orbifold built with ζ⊥ω.
Not derived for A_{k−1}, k≥3.

Attribution status: (Z1) is very likely known folklore in the Einstein/LeBrun–Kotschick
literature (almost-Einstein metrics on minimal surfaces with (−2)-curves); a literature check is
running (task s6_t1_tool2). What is specific to this programme: the equivalence (Z2) at the level
of α, its placement as the Q=0 (h=0) endpoint of the balanced family c·h ≤ α ≤ 4h/(1+h), the
contrast with the alignment defects (κ_β ≥ 4(β−2)²/β along the same sequence), and the
direction analysis (Z4).

## 5. Degeneration dichotomy — precise form and what is missing

Candidate Theorem D. Let g_j on fixed M have E(g_j)→0, normalised by λ_j=−1 (possible: the SW
class forces negative Yamabe type). Then V_j ∈ [2π²A, 12π²χ+o(1)] (LeBrun scalar bound and
Gauss–Bonnet), ∫|Rm|² ≤ 8π²χ+o(1). Claim: after passing to a subsequence, either (a) the
sequence is noncollapsed and converges to a negative Einstein orbifold with Ricci-flat ALE
bubble trees at finitely many points, or (b) it collapses on a set of positive measure.

What is proved in the literature: (a) holds for Einstein metrics (Anderson, Bando–Kasue–Nakajima)
and for critical metrics of quadratic functionals with a Sobolev bound (Tian–Viaclovsky).
What fails for arbitrary minimizing sequences: ∫|Ric+g|² → 0 is an L² (critical-exponent)
Ricci bound and gives no ε-regularity; conformal or bubbling defects of size o(1) in L²Ric can
in principle accumulate. The theorem therefore needs either an L^p (p>2) Ricci bound along the
sequence or selection of near-critical sequences with an equation that has ε-regularity. Which
hypothesis can be *supplied* (e.g. by a Ricci-flow smoothing of the minimizing sequence, which
preserves smallness of ⨍|Ric+g|² for short time and yields L^∞ control at scale √t) is the open
analytic step. This is the correct frame for the Braungardt–Kotschick Q=0 question: α=0 there
would require (a) a negative Einstein orbifold whose resolution is the non-Kähler symplectic
manifold, or (b) collapse.

---------------------------------------------------------------------------------------------

## 6. O11: the relative-orientation modulus of the blow-up cell (computation run this Step)

Script: `scripts/o11_rotated_cell.py` (curvature by automatic differentiation of the coordinate
metric; validated: flat ⇒ 0; CH ⇒ s=−24, Ric°=0, |W⁻_c|=0, |W⁺_c|²=24=s²/24; Burns ⇒ s=0,
W⁺_c=0; constant rotation ⇒ isometric invariants; θ=0 Kähler cell reproduces the U(2) code
P_K(0.01,1)=1.0618551601104 to 1e-14; identity residual (P−1)−(4ΔW⁺+ΔS/12)/8π² ≤ 2e-10).

Family: g = dx²/4G + h_ij s^i s^j, h = Rot₂(φ(x)) diag(x e^{w}, x e^{−w}, F) Rot₂(φ)^T.
φ ≡ θ near the bolt, φ → 0 (C²) at the CH boundary x=X; w, and the U(2) modes of F, G free.
This is the full SU(2)_L-invariant cell class with one free relative angle: since CH and Burns
are both SU(2)_L × U(1)-invariant, θ∈[0,π/2] is the *only* modulus of the tangent-space
identification modulo symmetries, i.e. exactly the angle between the Burns Kähler form ω_B and
ω_CH in Λ⁺. θ≠0 cells are non-Kähler for every complex structure compatible with either end.

### 6.1 Results (X=1, degU=6, degw=4, degr=6, 2×300 Gauss nodes; `data/o11rot/summary.csv`,
`figures/o11_rotation_slope.png`, localized-rotation runs `data/o11rot/loc_*.json`)

slope := (P_opt/8π² − 1)/x₀ (upper bound for the optimum in the family):

| x₀ | θ=0 | π/8 | π/4 | 3π/8 | π/2 | π/2 (localized rotation) |
|---|---|---|---|---|---|---|
| 0.001 | 5.956 | 6.950 | 9.581 | 13.107 | 16.894 | 15.37 |
| 0.003 | 5.900 | 6.828 | 9.207 | 12.205 | 15.200 | 14.30 |
| 0.01  | 5.779 | 6.651 | 8.771 | 11.208 | 13.395 | 12.97 |
| 0.03  | 5.619 | 6.447 | 8.324 | 10.236 | 11.721 | — |

All identity residuals (P−1) − (4ΔW⁺+ΔS/12)/8π² are ≤ 3e-10. In every cell both 4ΔW⁺>0 and ΔS>0.

What this shows.
1. **θ=0 reproduces the U(2) picture**: slope → 6 as x₀→0 with a negative second-order non-Kähler
   correction (ΔP_nonK ≈ −4.6e-4 at x₀=0.003, −4.1e-3 at x₀=0.01: exponent ≈ 1.8).
2. **Misalignment is penalized at first order.** P(θ)−P(0) ≥ 0 in every run and is of order
   x₀ (not o(x₀)): for small angles [P(θ)−P(0)]/(8π²x₀ sin²θ) ≈ 5.9–6.8, close to the Kähler
   slope itself. At θ=π/2 the penalty per x₀ grows slowly as x₀↓0 (≈1 per unit of log(1/x₀));
   the localized-rotation runs reduce it by only ~10%, and several optimizations stopped at
   iteration/line-search limits, so the log growth is not yet separated from parametrization
   effects. Empirical law at moderate angles: slope(θ) ≈ 6(1+sin²θ).
3. Consequently the relative-orientation modulus — the only remaining modulus of the
   SU(2)_L-invariant cell, and the one along which Malchiodi–Malizia's Weyl interaction
   W^M⊛W^Z ∝ (3cos²θ−1) changes sign — does not produce P(U)<8π²: the Weyl saving it could
   create is of order a⁴ while the misalignment penalty enters at order x₀ through *both*
   4ΔW⁺ (dominant) and ΔS. Within SU(2)_L-invariant cells the Kähler alignment is the
   first-order optimum; this is evidence for coefficient 4, not a lower-bound proof.
   Mechanism: the Burns r⁻² tail is anisotropic along ω_B, the CH quadratic jet is anisotropic
   along ω_CH (W⁺_CH ∝ diag(2,−1,−1) in (ω_CH,…)); the two anisotropies change sign at the
   crossover radius x ~ √x₀, and rotating the axis where both are O(√x₀) costs O(x₀ θ²).

Remaining O11 cell freedom not covered: cells without SU(2)_L symmetry (genuinely
four-dimensional profiles), cells whose exceptional region is not Burns-like (non-Kähler
ASD fillers), and fixed-scale cells far from the x₀→0 regime (x₀≥0.1 was covered only in U(2)).

---------------------------------------------------------------------------------------------

## 7. New consequence of the literature check: zero Einstein gap on non-Kähler minimal
##    symplectic manifolds (Theorem Z′), and why BK manifolds escape this mechanism

Sources read: Şuvaina, *The Yamabe invariant of a class of symplectic 4-manifolds*
(arXiv 1410.1236; Knowledge `The-Yamabe-invariant-of-a-class-of-symplectic-4-manifolds--93fc75a3247d`),
Theorem A, Prop. 4.1–4.2, §3 construction; LeBrun, *Kodaira dimension and the Yamabe problem*
(CAG 1999, cited there as [18]) for the Kähler/ADE case.

**Attribution of (Z1).** LeBrun's 1999 Yamabe computation for minimal Kähler surfaces uses exactly
the canonical-model orbifold KE metric with ADE ALE cores, and Şuvaina extends it to T-singularities
with Ricci-flat ALE Kähler rational balls B_{n,m}. Their sequences are built to make
∫s² → 32π²c₁²; on their interpolation annuli g−g_eucl=O(t²), ∂g=O(t), ∂²g=O(1) and the annular
volume → 0, while the cores are Ricci-flat and the bulk is Einstein. Hence the *same* sequences
satisfy ∫|Ric+g|²/V → 0. So (Z1) is a direct consequence of LeBrun 1999 / Şuvaina 2015 and must be
attributed to them; the α-level content added here is (Z2)–(Z4) and the endpoint placement.

**Theorem Z′.** Let N be the generalized rational blowdown (Şuvaina Theorem A) of linear chains of
type 1/n²(1,nm−1) in a complex surface M such that the contracted orbifold M̂′ has ample K. Then α(N)=0. (Blow-ups N#ℓCP̄² are not covered; whether the corpus lower bound c·h applies to them depends on
its supply hypotheses for N and must be checked separately.) In particular the simply connected, minimal,
symplectic, **non-Kähler** manifolds Y_n (n≥4) on the half-Noether line, c₁²=n−3, c₂=11n+3
(Prop. 4.2), have α(Y_n)=0. Proof: Şuvaina's metrics g_t on Y_n are orbifold KE outside shrinking
annuli, Ricci-flat Kähler ALE (B_{n−2,1} and the A_{n−4} resolution) inside, with bounded curvature
on annuli of volume → 0; E(g_t) ≤ ∫|Ric+g_t|²/V_t → 0. ∎ (Attainment on Y_n ⇔ a negative Einstein
metric on Y_n; none is Kähler–Einstein since Y_n is not complex.)

Consequence for the Q=0 question: **non-Kählerness alone does not create a positive Einstein gap.**
The strategist's "Einstein-gap version of O10" therefore cannot be a principle of the form
"Q=0 and non-Kähler ⇒ α>0".

**Why the Braungardt–Kotschick family (fixed c₁²=A, χ_h→∞) is different.** Y_n has bounded density
χ/A→11. For the orbifold-KE mechanism on a manifold with c₁²=A, the limit is a stable surface with
quotient (T or ADE) singularities and K ample, K²=A; by Alexeev's boundedness of stable surfaces with
fixed K² (to be retrieved and cited exactly), these form a bounded family, and the Ricci-flat ALE
Kähler fillers of a given group are finitely many (Kronheimer; Şuvaina/Răsdeaconu–Şuvaina
classification, Knowledge `ALE-Ricci-flat-Kahler-surfaces-and-weighted-projective-spaces`). Hence
**Proposition B (to be completed with the exact Alexeev statement):** for fixed A, only finitely many
diffeomorphism types arise as single-level Kähler-orbifold Einstein desingularizations with
c₁²=A. So on all but finitely many members of a BK sequence, α=0 would require a *non-Kähler*
Einstein orbifold limit, a deeper bubble tree, or collapse — exactly the dichotomy of §5, with the
Kähler branch removed. This is the sharp form of the Einstein-gap density question.




---

## Source step8_first_order_cell_law_ASD_Qprinciple.md

Original: [sources/Sessions/S1003A02/workspace/notes/step8_first_order_cell_law_ASD_Qprinciple.md](../sources/Sessions/S1003A02/workspace/notes/step8_first_order_cell_law_ASD_Qprinciple.md)

# Step 8 — First-order O11 cell law, ASD Yamabe upper bound, intrinsic Q-principle

Conventions: `Skills/geometric-analysis/references/conventions-and-literature.md`
(`P=∫|Ric°|²`, `R=P+S/4`, `T_±=2χ±3τ`, operator Weyl norms, `E=(4P+L_s)/R`).
Surgery data: `variational_geometry.tex` §1 (`M=X#kCP²bar#ℓ(S¹×S³)`, `Q=k+4ℓ`, `T_+=A−Q`).

## 1. O11: the first-order cell cost is −x₀R⁺(ζ,ζ), not 6x₀(1+sin²θ)

**What was computed.**

(a) `scripts/o11_rotation_hessian.py` (repaired: Step-6 filenames are `grid_x0<x0>_th0.json`;
options `--degr --nq --out`). Relaxed θ²-Hessian (Schur complement over linear rotation
modes) at the aligned optimized cells. Data `data/o11rot/rh_x*_d*_n*.json`,
merged `data/o11rot/rotation_hessian.json`. Rotation block positive definite in every run;
quadrature-independent (nq 300 = 600 to all digits).

(b) `scripts/o11_rotation_density.py`: pointwise second variation `L=Aφ'²+2Bφ'φ''+Cφ''²`
(gauge invariance under constant right rotation makes L independent of φ). It reproduces
the Chebyshev Schur value to 4e-9 relative (e.g. x₀=0.01: 5.902830531 vs 5.902830555),
then minimizes over profiles with 64 modes on the whole interval. Relaxed coefficient
`(1/2)H_eff/x₀`:

| x₀ | 0.03 | 0.01 | 0.003 | 0.001 | 3e-4 | 1e-4 |
|---|---|---|---|---|---|---|
| relaxed (N=64) | 5.552 | 5.712 | 5.858 | 5.940 | 5.983 | 5.999 |
| aligned slope (P₀−1)/x₀ | 5.619 | 5.779 | 5.900 | 5.956 | 5.984 | 5.994 |

The optimal rotation profile peaks at x/√x₀ = 0.85, 0.90, 0.96, 0.98, 0.98, 0.98: at the
Burns/CH crossover. Data `data/o11rot/rotation_density_x0*.json/.npz`.
New aligned cells x₀=3e-4, 1e-4 (`grid_x00.0003_th0.json`, `grid_x00.0001_th0.json`).

(c) **Correction of Step 6.** That Hessian lives in the *diabatic* family of
`o11_rotated_cell.py`: h = R(φ)diag(xe^w, xe^{−w}, F)R^T with the single slot F carrying
both the bolt-collapsing direction and the CH fibre. Writing the off-diagonal mode as
h₁₃ = φ(F−x) shows it forces h₁₃ = 0 at the crossover F=x — an artificial constraint.
The superposition picture h ≈ xI − x₀nn^T + x²e₃e₃^T has an avoided eigenvalue crossing
there: the collapsing branch ends *perpendicular* to the CH fibre (adiabatic family).

`scripts/o11_perp_cell.py` implements fixed-slot cells: bolt in s¹ slot, CH fibre in s³ slot,
frame rotation β(x) with relative angle θ = π/2 − β(bolt) (`--theta=`), a fixed-slot aligned
control (`--aligned`, reproduces 5.906 at x₀=0.003 and 5.992 at 0.001, i.e. the Kähler cell),
and a `--smooth` option making the bolt anisotropy O((x−x₀)²) (charge-4 smoothness; the
w-mode u·poly is only C^{1,1} at the bolt; values identical to 5 digits, e.g. perp 0.01:
1.001996 vs 1.002006). Runners: `o11_perp_runs.sh`, `o11_adia_runs.sh`. Data
`data/o11perp/*.json`, table `data/o11perp/first_order_law.csv`, figure
`figures/o11_first_order_law.png` (script `o11_first_order_law_fig.py`).
Chern–Weil identity residuals ≤ 4e-10 in all cells.

Best cell (upper bound) (P/8π²−1)/x₀ at x₀=0.003, versus 6cos²θ:

| θ | 0 | π/8 | π/4 | 3π/8 | π/2 |
|---|---|---|---|---|---|
| best found | 5.900 | 6.19 | 3.25 | 0.96 | 0.044 |
| 6cos²θ | 6 | 5.12 | 3.00 | 0.88 | 0 |
| 4ΔW₊/x₀ | 3.88 | 4.15 | 1.24 | −1.06 | −1.99 |
| 2(3cos²θ−1) | 4 | 3.12 | 1 | −1.12 | −2 |
| (ΔS/12)/x₀ | 2.01 | 2.04 | 2.01 | 2.02 | 2.03 |

At x₀=0.01 the adiabatic θ=π/8 cell (5.720) is already *below* the aligned Kähler cell (5.779).
At θ=π/2 the excess is second order: P/8π²−1 = 1.0e-5, 1.3e-4, 2.0e-3, 1.9e-2, 0.154 at
x₀ = 0.001, 0.003, 0.01, 0.03, 0.1 (≈ +10…21 x₀², still positive; optimizer stopped by
line search, so upper bounds).

**First-order cell law (conjecture with strong evidence).** For a Burns bubble of scale x₀
(x=r² units) in the complex-hyperbolic ball (s=−24), with orientation ζ ∈ Λ⁺ (|ζ|=1,
the Burns Kähler form), the infimum over SU(2)_L cells is

  P(U)/8π² = 1 − x₀ R⁺(ζ,ζ) + O(x₀²),  R⁺ = W⁺ + s/12 = diag(s/4,0,0) in (ω_CH, ω₂, ω₃),

  4ΔW₊ = −x₀ W⁺(ζ,ζ)·8π² = 2x₀(3cos²θ−1)·8π²,  ΔS/12 = −x₀(s/12)·8π² = 2x₀·8π².

Mechanism: at order x₀ = a²·|Rm_CH| the excess is the linear response of the Burns metric
to the background curvature at the blown-up point; SO(3)₊-equivariance allows only the
spin-0 (s) and spin-2 (W⁺ ∈ S²₀Λ⁺) parts of the background to pair with ζ⊗ζ, so the
θ-dependence must be a + b·P₂(cosθ). The measured components fit exactly this form,
with the Malchiodi–Malizia sign-changing pattern (3cos²θ−1) appearing in the Weyl term
already at order a² (the strict Weyl saving, maximal −2x₀ at θ=π/2, exactly cancels the
universal scalar cost +2x₀). A proof would compute the two response coefficients
(−1 for W⁺ and s) from the Burns ALE asymptotics; the numerics fix them to <2%.

**Consequences.**
1. The aligned (holomorphic) blow-up is the *most* expensive orientation at first order,
   not the cheapest. Step 6's "misalignment penalty ≈6x₀sin²θ" is a diabatic-ansatz
   artifact; its log growth at π/2 came from the ansatz, not geometry.
2. The first-order cost is ≥0 exactly because R⁺ ≤ 0 on a negative Kähler–Einstein
   background, and vanishes precisely on ker R⁺ = ω^⊥ — the same directions in which
   Ozuch's first obstruction R⁺ζ=0 is satisfied (Step 5–6 analysis). The O11 cell cost and
   the Einstein-desingularization obstruction are the same tensor.
3. O11 at fixed scale therefore reduces to the *second-order* term at ζ ⊥ ω:
   numerically +O(10–20)x₀² > 0. No tested cell has P(U) < 8π²; coefficient 4 survives,
   but the margin is now O(x₀²), not O(x₀). A sub-threshold cell, if any, must be sought at
   ζ ⊥ ω_CH and finite x₀ (0.03–0.3), beyond SU(2)_L symmetry.
4. For the lower-bound theorem, the natural statement becomes: cell excess ≥ −x₀R⁺(ζ,ζ)
   + c x₀² with R⁺ ≤ 0 — a "no-A-loss" inequality must be quadratic, not linear, near ω^⊥.

## 2. ASD Yamabe upper bound (new theorem)

**Normalization check.** Chern–Weil (ledger): W₊ = 2π²T₊ − R/12 + P/3, R = P + S/4, hence
P = 4W₊ + S/12 − 8π²T₊. With W₊=0 and T₊=A(1−h): P = S/12 + 8π²A(h−1),
R = S/3 + 8π²A(h−1) — Agent4's formula is exact in corpus conventions
(sympy: `scripts/asd_yamabe_bound.py`).

**Theorem ASD.** Let M be closed oriented with a monopole class a such that, for the metric
in question, p=(a⁺)² ≥ A > 0, and T₊(M) = A(1−h). Let [g] be an anti-self-dual conformal
class (W⁺=0) and g_Y its Yamabe metric, σ = S(g_Y)/(8π²A).
(i) σ ≥ 9 (LeBrun: ∫(s−√6|W⁺|)² ≥ 72π²p with W⁺=0). Strict unless equality in LeBrun,
    which forces Kähler with W⁺=0 hence s=0, impossible; so σ>9.
(ii) inf_{g∈[g]} E(g) = E(g_Y) = 1 + 9(h−1)/(σ+3h−3).
    Proof: W⁺=0 is conformally invariant, so every g∈[g] has R = S/3+8π²A(h−1) and
    E = 4 − 3ι/(σ_g+3h−3), ι = (∫s)²/(8π²AV). In a negative Yamabe class
    (∫s)²/V ≤ Y² = S(g_Y) and S(g) ≥ S(g_Y), so E(g) ≥ E(g_Y), equality at g_Y.
(iii) For h>1, E(g_Y) is decreasing in σ, hence
    1 < E(g_Y) < (4h−1)/(h+2) = 4 − 9/(h+2);
    for h<1 the inequalities reverse: max(0,(4h−1)/(h+2)) < E(g_Y) < 1.
    Uniformly: |E(g_Y)−1| < 3|h−1|/(h+2).

**Corollary (large-h window).** Let X be minimal of general type (b⁺≥2 or the corpus's
polarized supply), A = c₁²(X), M = X#ℓ(S¹×S³)#kCP²bar, Q = k+4ℓ, h=Q/A. By Taubes
(existence of ASD conformal structures on N#kCP²bar, k ≥ k_T(N)), for k ≥ k_T and h>1:

   1 ≤ α(M) < (4h−1)/(h+2) < 4h/(1+h).

The lower bound is the orientation-specific Hitchin–Thorpe estimate (T₊≤0 ⇒ R ≤ 4P ⇒ J≥1).
The improvement over surgery recovery is 4h/(1+h) − (4h−1)/(h+2) = (5h+1)/((h+1)(h+2)) > 0.
If k_T ≤ A (unknown), the same gives α<1 for 1/3≤h<1 and, at h=1 exactly, α(M)=1 attained
by a non-Einstein ASD Yamabe metric.

**Large-h question, sharpened.** Over ASD competitors α_ASD → 1 iff σ_Y/h → ∞ along Taubes
classes; for general metrics J = (σ+48w+12h−12)/(σ+12w+3h−3) (w = W₊/8π²A) is decreasing
in σ and increasing in w for h>1, so the H–T value 1 is approached only by W₊ = o(Ah),
S ≫ Ah. The asymptotic of α at large h is in [1, 4−9/(h+2)); whether σ_Y can be made ≫ h
on X#kCP²bar is the open quantitative Taubes problem.

## 3. Intrinsic Q-principle

**Budget.** For closed oriented M let 𝔐 be the (finite) set of monopole classes with
a² ≥ T₊ (automatic for classes with nonzero ordinary SW invariant: expected dimension
(a²−T₊)/4 ≥ 0). Define

   A(M) = max{ c² : c ∈ conv 𝔐 },  Q(M) = A(M) − T₊(M) ≥ 0,  h = Q/A,  U = 3min(T₊,T₋)/A.

**Lemma (metric-wise supply).** If A(M)>0, every metric g admits a ∈ 𝔐 with
(a_g⁺)² ≥ A and a² ≥ T₊, chosen constantly on the conformal class.
Proof: c = Σtᵢaᵢ attains A; a ↦ (a_g⁺)² is a positive semidefinite quadratic form, hence
convex, so max_i(aᵢ⁺)² ≥ (c⁺)² ≥ c² = A; H⁺_g is conformally invariant.

This is exactly the "common A on every conformal class" input of `cor:trf-nu`,
`thm:linear-window`. Examples: X#kCP²bar with X minimal general type: 𝔐 = {±K ± E₁ ±…±E_k},
conv = image of a cube, A = K_X², Q = k (sign averaging is the convex hull). With handles,
the loop-insertion classes have a² = A − k > T₊, Q = k+4ℓ. **Note:** the alternative
"Q = A − max_{𝔐} a²" is wrong for handle summands (it gives Q=0 for handle-only manifolds,
where the corpus proves α = 4h/(1+h) > 0); the correct excess is A − T₊.

**Theorem Q (positive direction, proved pieces).** Assume A(M)>0.
(Q1) h ≥ 1 (T₊ ≤ 0): α ≥ 1 (no monopole needed).
(Q2) 1/3 ≤ h < 1: α ≥ c_* universal (N1/trace-free gap, `cor:trf-nu`, since a² ≥ T₊ > 0
     removes the negative-square cost and (T₊/A−2/3)₊ = 0). By the relative-shortfall
     form, positivity extends to h > 1/3 − c.
(Q3) 0 < h < 1/3: α ≥ J ≥ (L_h − U)₊/(L_h + U/18), L_h = 1+(1+c₀)h (`thm:linear-window`);
     α ≥ c h whenever 3T₋ ≤ A(1+h) (handle-dominated; includes the balanced family as
     arranged in the corpus).
(Q0) h = 0 can give α = 0: Theorem Z (minimal general type), Z′ (Şuvaina Y_n).

**Conjecture Q.** α(M) > 0 ⟺ Q(M) > 0, under A(M) > 0.
Open in the positive direction exactly on 0<h<1/3 with 3T₋ > A(1+(1+c₀)h)
(blow-up-dominated: X#kCP²bar with k ≪ A has 3T₋/A ≈ 1+15h). Open in the negative
direction on Q=0 manifolds outside the Kähler/Şuvaina-orbifold mechanism (e.g.
Braungardt–Kotschick, fixed A, χ→∞; Proposition B remains suspended).
Relation to §1: for the blow-up-dominated region the corpus balanced theorem needs the
cell cost; §1 shows the per-blow-up excess over 8π² is O(x₀²) at ζ ⊥ ω, so the
positive direction there hinges on a lower bound of P at the 8π²k level (no-A-loss), not on
an O(x₀) margin.

## 4. Zero-gap exposition repair (Z′)

In Şuvaina's metrics g_t: exterior exactly negative KE (Ric = −g after scaling), so
|Ric+g|² = 0 there; the rescaled Ricci-flat ALE interiors have |Ric+g|² = |g|² = 4
pointwise, contributing 4·Vol(interior) = O(t⁴)→0; the interpolation annuli have
g−g_eucl = O(t²), ∂g = O(t), ∂²g = O(1), uniformly elliptic, hence |Rm|, |Ric| = O(1)
and contribution O(Vol(annulus)) → 0. Hence ∫|Ric+g|²/Vol → 0 and α = 0. Assumptions:
contracted orbifold with ample canonical sheaf; Y_n are non-Kähler (the inspected source
does not assert absence of all complex structures).



---

## Source step9_universal_cell_response_and_spectral_pressure.md

Original: [sources/Sessions/S1003A02/workspace/notes/step9_universal_cell_response_and_spectral_pressure.md](../sources/Sessions/S1003A02/workspace/notes/step9_universal_cell_response_and_spectral_pressure.md)

# Step 9 — Universal Burns-cell response, positive-KE sign reversal, and the second-order spectral problem

Conventions: `P=∫|Ric°|²`; scripts report `P/(8π²)`. Cell scale is `x0=a²`.
The strongest analytic support is `trace/ttcs/results/step9_ttcs01_generator1_integration.md`; computation reading is `step9_ttcs01_verifier1_integration.md`; the relative-calibration reading is `step9_ttcs01_verifier2_integration.md`.

## 1. Universal first-order response: statement now supported, proof reduced to one ALE boundary computation

For an oriented background metric near `p`, identify the Burns Kähler direction at infinity with a unit `ζ∈Λ⁺_p`. The first-order law suggested by Steps 8–9 is

\[
 \frac{P(g_a)-P(g;B_a)}{8\pi^2}
 =1-a^2\,\mathcal R^+_p(\zeta,\zeta)+o(a^2),
 \qquad \mathcal R^+=W^++\frac{s}{12}I.
\]

Here the background ball is removed on the right; for an Einstein complex-space-form bulk it contributes no `P`. The topological term is exact:

\[
 P=4\int|\mathcal R^+|^2-8\pi^2T_+,
\]

and a blow-up changes `T_+` by `-1`, so it remains to prove

\[
 \Delta\int|\mathcal R^+|^2
 =-2\pi^2a^2\mathcal R^+_p(\zeta,\zeta)+o(a^2).
\]

The Burns asymptotic metric has

\[
 g_{B,a}=g_0+a^2H_\zeta+O(a^4r^{-4}),\qquad
 H_\zeta=r^{-2}\{dr^2-(J_\zeta dr)^2\}.
\]

SO(3)+ equivariance forces the linear response to pair the scalar and spin-2 pieces of `R+` with `ζ⊗ζ`. The coefficient and sign reduce to the matrix-valued ALE transgression

\[
 \int_{S^3_\infty}\mathcal T_{\mathcal R^+}(H_\zeta)
 =-\pi^2\zeta\otimes\zeta
\]

with the gluing orientation. The scalar part of this boundary flux can already be checked directly; the full matrix-valued computation has not yet been carried out in the session. Assuming it, the separate first variations are

\[
 \frac{4\Delta W_+}{8\pi^2}=-a^2W^+(\zeta,\zeta)+o(a^2),\qquad
 \frac{\Delta S/12}{8\pi^2}=-a^2\frac{s}{12}+o(a^2).
\]

This is the precise remaining proof object. An `O(a^4)` remainder needs a second matched expansion and is not yet justified generally; `o(a²)` is the natural first theorem.

The relation to Einstein desingularization is structural. The scalar cell potential is `-a²<R+ζ,ζ>`. Its scale derivative is `-<R+ζ,ζ>` and its angular derivative is `-2a² Π_{ζ⊥}R+ζ`; both vanish exactly when `R+ζ=0`. Hence Ozuch's vector obstruction is the full critical-point equation of the same first-order cell potential. If `R+` is indefinite, zero scalar cost alone does not imply the vector obstruction.

## 2. Decisive positive-versus-negative Kähler–Einstein computation

New script `workspace/scripts/o11_general_bulk_cell.py` extends the aligned U(2) cell to the signed complex-space-form collar

\[
 K_{bulk}=x+\kappa x^2,\qquad s=-24\kappa,
 \qquad \mathcal R^+(\omega,\omega)=-6\kappa.
\]

At fixed `X=0.25`, degree 8 and 500-point quadrature:

| κ | bulk | x0 | P/(8π²) | slope `(P-1)/x0` | predicted |
|---|---|---:|---:|---:|---:|
| +1 | complex hyperbolic | .003 | 1.01853255 | +6.1775 | +6 |
| +1 | complex hyperbolic | .001 | 1.00605811 | +6.0581 | +6 |
| -1 | Fubini–Study sign | .003 | .98305786 | -5.6474 | -6 |
| -1 | Fubini–Study sign | .001 | .99410593 | -5.8941 | -6 |

Thus an actual same-metric positive-KE cell has `P<8π²`. There is no hard-coded CH subtraction: `P` is directly integrated. The sign reversal is already visible in the explicit four-constant Kähler seed, whose expansion is

\[
 \frac{P}{8\pi^2}=1+6\kappa x_0+9(\kappa^2+X^{-2})x_0^2+O(x_0^3).
\]

Therefore a finite outer radius cannot create the first-order sign; it enters at second order. This verifies the strategist's crucial falsification test and shows that a universal per-blow-up `8π²` lower bound is false on backgrounds with a positive eigenvalue of `R+`. It also explains why blow-ups of positive KE manifolds can be cheap. This experiment verifies the aligned complex-space-form specialization of the universal tensor law, not the full general-background law by itself.

## 3. Perpendicular CH cell and collaboration with S1003A01

High-degree smooth fixed-slot computations at `θ=π/2` remain above threshold:

| x0 | degree | P/(8π²) | excess |
|---:|---:|---:|---:|
| .03 | 10/10 | 1.018595845 | .018596 |
| .10 | 10/10 | 1.151480821 | .151481 |
| .20 | 10/10 | 1.444267492 | .444267 |
| .30 | 10/10 | 1.817084160 | .817084 |

The `.03` optimizer ended abnormally and the larger points hit iteration limits, so these remain ansatz upper bounds. The `.03` profile was exported with `G,h` and their first two x-derivatives at 1601 points:

- `data/o11perp/profile_perp_smooth_x0.03.npz`
- `data/o11perp/profile_perp_smooth_x0.03.csv`

Peer S1003A01 independently obtained a stronger exact Bianchi-IX relative calibration. In bolt-adapted variables `u_i` it gives

\[
 \frac{P}{8\pi^2}-1=
 \int\left(\sum_i\frac{\lambda_i}{4}E_i^2+
 \frac{2u_1u_2u_3}{\lambda_2}\right)dt.
\]

On the smooth `x0=.01` profile the three squares total `.003428047`, the signed cubic is `-.00143166`, leaving `.001996387`. This is more mathematically valuable than another profile search: threshold is reduced to a matrix Hardy/Riccati problem for `η=(u1,u3)`. A sufficient certificate is a symmetric `Γ(t)` satisfying

\[
 N-\dot\Gamma+K^T\Gamma+\Gamma K-\Gamma A^{-1}\Gamma\succeq0
\]

with the correct bolt boundary sign. On the exact CH segment, channels `v±=u1±u3` factor through explicit positive Jacobi solutions

\[
 y_+=x(1+x)^{1/2},\qquad y_-=x(1+x)^{-5/2}.
\]

The critical transformed variables are

\[
 z_+=\frac{u_1+u_3}{x\sqrt{1+x}},\qquad
 z_-=\frac{(1+x)^{5/2}}x(u_1-u_3),
\]

which turn the outer signed potentials into weighted squares plus a boundary quadratic form. The missing theorem is an inner Burns-to-CH Dirichlet-to-Neumann comparison. A resonance remains possible because `u2≈3x`, `u3≈-x0/x` gives `u2u3≈-3x0` across the logarithmic neck; its Schur complement could in principle produce an `x0² log(1/x0)` term. No constructed metric presently realizes a negative term, and all computed profiles are positive.

## 4. Full-mode Hessian pressure and why no negative cell was established

Three Hessian prototypes were built:

- `o11_radial_hessian.py`: all SU(2)-invariant radial variations of `G` and six entries of symmetric `h`;
- `o11_full_hessian.py`: arbitrary coordinate tensor modes (found to have a measure/global-smoothness problem);
- `o11_full_hessian2.py`: geometric-coframe modes (better, but low angular quadrature and no gauge quotient).

The radial quadrature reproduces the cell energy to `4e-10`. At 3 radial modes all 21 raw eigenvalues were positive (minimum `8.27`). At 6 modes a raw eigenvalue `-1.63` appeared, and at 8 modes two appeared (`-23.18,-1.44`). These are not established negative directions:

1. the expanded-space projected gradient is large (`5.22`, `12.65`), so the base is not stationary there;
2. the parametrization `G→G exp(d)` adds gradient-dependent second-coordinate terms;
3. diffeomorphism modes were not removed;
4. the negative values do not converge with resolution;
5. direct symmetric line samples rose on both sides at the tested amplitude; smaller amplitudes scaled by `||g^{-1}th||∞` are needed.

The non-invariant prototypes likewise cannot decide the question yet. A true next spectral computation must use the natural coframe, include all SU(2)-invariant shifts, build the Lie-derivative map for compactly supported vector fields, project to its L2-orthogonal/Bianchi complement, re-optimize to projected stationarity, and only then solve the generalized Ritz problem. Non-invariant extensions should use globally smooth Wigner-D modes rather than raw Euler trigonometric functions.

The exact relative calibration now gives the sharper route within symmetry; the gauge-fixed spectral calculation remains the correct route beyond symmetry.

## 5. What changed in O11

- The universal first-order object is `-a² R+(ζ,ζ)`, not a universal positive blow-up cost.
- Positive Kähler–Einstein curvature gives a real sub-`8π²` Burns cell at first order; negative Kähler–Einstein curvature makes aligned cells expensive.
- On negative KE backgrounds, the dangerous perpendicular directions are exactly `ker R+`, where first order cancels and the Einstein desingularization obstruction also vanishes.
- Coefficient 4 for balanced negative-KE surgery, if true, is a second-order theorem. Within SU(2), it is now a critical matrix Hardy/Riccati or inner/outer Dirichlet-to-Neumann comparison. Beyond symmetry, it is a gauge-fixed weighted spectral problem.
- The proposed global lower-bound architecture must allow cheap cells wherever the near-minimizing bulk develops positive `R+`. Quantitative LeBrun saturation must therefore control the positive part of `R+` strongly enough that any distributed cell saving is subordinate to the bulk deviation cost.



---

## Source step11_subthreshold_perpendicular_cell.md

Original: [sources/Sessions/S1003A02/workspace/notes/step11_subthreshold_perpendicular_cell.md](../sources/Sessions/S1003A02/workspace/notes/step11_subthreshold_perpendicular_cell.md)

# Step 11 — Finite-scale perpendicular cell below the Burns threshold

## 1. Frozen cell

Use the degree-eight coefficient vector in

`Sessions/S1003A01/workspace/data/perp_collar/x0.01_X8_J_d8.json`.

It defines on \(x\in[x_0,X]\), \(x_0=.01\), \(X=8\),
\[
 g=\frac{dx^2}{4G}+F\sigma_1^2+x\sigma_2^2+xe^w\sigma_3^2,
\]
with the \(\sigma_1\)-circle collapsing at the bolt and the complex-hyperbolic Kähler fibre in the \(\sigma_3\) slot. The background normalization is \(\operatorname{Ric}=-6g\). Set
\[
 P=\int |\operatorname{Ric}^\circ|^2,
 \qquad J_6=P+\frac14\int(s+24)^2=\int|\operatorname{Ric}+6g|^2.
\]
The one-cell topological threshold is \(8\pi^2\).

## 2. Independent reconstruction

`workspace/scripts/o11_collar_independent_verify.py` reconstructs the profile from the frozen decimal coefficients without importing the peer's cell, curvature, or spin-diagnostic code. It uses the Cartan variables
\[
 u_i=\dot a_i-\frac{a_j^2+a_k^2-a_i^2}{a_ja_k},\quad
 H_i=u_i+\frac12u_ju_k,\quad \lambda_i=\frac{a_ja_k}{a_i}
\]
and evaluates both
\[
 \frac P{8\pi^2}=\int\sum_i\frac{\lambda_i}{4}
 \left(\dot u_i-\frac{2H_i}{\lambda_i}\right)^2dt
\]
and the relative calibration
\[
 \frac P{8\pi^2}-1=\int(S_1+S_2+S_3+2u_1u_2u_3/\lambda_2)dt,
\]
together with the scalar square. Split Gauss orders 200, 400 and 800 agree to the displayed precision:
\[
\begin{aligned}
S_1&=.00159729167196687,\\
S_2&=.00052244698325698,\\
S_3&=.00109028656646375,\\
C_3&=-.00410132248809498,\\
P/(8\pi^2)&=.9991087027335926,\\
(J_6-P)/(8\pi^2)&=7.54040173166\times10^{-6},\\
J_6/(8\pi^2)&=.9991162431353243.
\end{aligned}
\]
The positive-square and relative evaluations of \(P\) differ by less than \(5\times10^{-15}\). This independently reproduces peer computations but does not by itself turn floating quadrature into a proof.

The script also verifies
\[
 F=G=w=0,\quad F'G'=1,\quad w'=0
\]
at the bolt, and exact complex-hyperbolic values and first jets at \(X\). On 20,001 points,
\[
\min G/(x-x_0)=1.0321404811,\qquad
\min F/(x-x_0)=.9661766585.
\]
Metric positivity is in fact analytic from
\[
F=(x-x_0)e^{q_F}+x_0S(u)>0,
\quad G=((x-x_0)+(x^2+x_0)S(u))e^{q_G}>0,
\]
with \(0\le S\le1\).

## 3. Ball arithmetic status

`workspace/scripts/o11_collar_arb_certificate.py` is a second independent evaluator in 160-bit python-flint/Arb. It propagates the decimal coefficients and all derivatives entering the spin formula through a second-order jet algebra. Composite Simpson meshes 500, 1000 and 2000 give the normalized defect integral
\[
J_6/(8\pi^2)-1=
-.0008837566079749,
-.0008837568484957,
-.0008837568636623.
\]
Inflating the finest Richardson change by a factor \(1000\) gives
\[
J_6/(8\pi^2)<.99911624414745<1.
\]
The Arb balls rigorously contain the finite Simpson sums and their roundoff propagation, but the Simpson remainder is still estimated from mesh convergence rather than a proved interval bound for the fourth derivative; the decimal JSON values were also first parsed as binary64 in this exploratory script. Thus this is strong high-precision evidence, not yet a theorem-level certificate. Raw interval subdivision is ineffective near the bolt because the spin expressions have severe dependency cancellation. The right final certification route is to parse each decimal as an exact rational and factor
\[
y=x-x_0,\quad F=y\widehat F,\quad G=y\widehat G,
\quad w=y^2\widehat w
\]
and simplify the relative-plus-scalar density before Arb subdivision, or to derive an analytic derivative bound for the transformed integrand. TTCS derived regular variables \(u_1=\sqrt y\,U_1\), \(u_2=\sqrt y\,U_2\), \(u_3=U_3\), which cancel every half-power in the density; the complete formulas and a rigorous Taylor/Simpson enclosure scheme are in `trace/ttcs/results/step11_ttcs01_generator1_integration.md`. The boundary primitive is \(u_1^2+u_3^2+u_1u_2u_3\), not \(\sum u_i^2+u_1u_2u_3\); this auxiliary diagnostic was corrected in the independent script and did not enter the reported energy. The fixed margin is \(8.84\times10^{-4}\), so only a modest global bound is required.

## 4. Smooth collar

The stored profile agrees with complex hyperbolic space through the second \(x\)-jet at \(X\), because every free perturbation carries \((1-u)^3\). It is therefore a smooth bolt metric with a \(C^2\) direct CH attachment. Multiplying the third-order deviation by a flat cutoff in a collar of width \(\delta\) changes the curvature defect by \(O(\delta)\) pointwise on volume \(O(\delta)\), and hence changes \(J_6\) by \(O(\delta^3)\). Since the deficit is strict, sufficiently small \(\delta\) produces a smooth exact-CH-collar cell with \(J_6<8\pi^2\). A quantitative cutoff bound can be added after the frozen integral receives a theorem-level enclosure; no optimization enters this smoothing statement.

## 5. Consequence for O11

After scaling \(\widetilde g=6g\),
\[
\int|\operatorname{Ric}_{\widetilde g}+\widetilde g|^2dV_{\widetilde g}=J_6(g).
\]
For a complex-hyperbolic ball quotient, residual finiteness first supplies a fixed finite cover containing the required radius-\(\sqrt6\,\operatorname{arsinh}\sqrt8\) ball, plus a smoothing buffer. Further covers supply disjoint lifts proportional to the covering degree. The inherited one-cell transfer formula is
\[
\limsup\frac{\alpha(M_j)}{h_j}
\le \frac{28}{9}+\frac{J_1}{9\pi^2}
=4-\frac{8\varepsilon_0}{9},
\qquad \frac{J_1}{8\pi^2}=1-\varepsilon_0.
\]
For the frozen numerical value, \(\varepsilon_0=.0008837568647\), giving coefficient approximately
\[
3.9992144383<4.
\]
Accordingly, once the one remaining integral enclosure is completed, O11 has a negative answer: the handle coefficient four is not the blow-up coefficient. The upper construction uses a finite-scale perpendicular cell, not a bubbling Burns limit. The sharp blow-up coefficient is then the infimum of the complete-cell cost (including nonsymmetric cells), which remains open.

## 6. Relation to the logarithmic neck and curvature response

The Step-10 shrinking-cell family has
\[
J_6/(8\pi^2)=1-9x_0^2\log(1/x_0)+O(x_0^2).
\]
The fixed \(X=8\), \(x_0=.01\) cell produces a much larger practical deficit and shows that constant reduction is secondary to proving one cell. The logarithmic mechanism remains structurally important: it explains why the kernel direction \(\zeta\perp\omega\) is eventually subthreshold even though its first-order response vanishes.

A cheap exact sign test was recorded in `o11_neck_sign_quick.py`. Under analytic continuation from CH to the positive complex-space-form collar, the mixed constants reverse sign but the minimized P and J neck forms retain value \(-18\), so the integrated coefficient remains \(-9\) on both curvature signs. This supports a quadratic second-order curvature response: first order is \(-a^2\mathbf R^+(\zeta,\zeta)\), while the logarithmic kernel response is even in the ambient curvature. This continuation is not yet an independent general-bulk derivation, but it strengthens the conjectural coefficient \(-|\mathbf R^+|^2a^4\log(1/a^2)/4\) in the rank-one Kähler block, since \(|\mathbf R^+|^2/4=9\) for eigenvalue magnitude six.

## 7. Rigorous enclosure completed

Peer S1003A01 subsequently supplied `workspace/scripts/perp_rigorous_enclosure.py`, which implements a stronger version of the required regularization directly for the orthonormal Ricci tensor. It factors
\[
y=x-x_0,\quad F=y\widehat F,\quad G=y\widehat G,\quad w=y^2\widehat w,
\]
rewrites every Ricci component without removable bolt singularities, and calls python-flint's `acb.integral`. The integrator contracts the callback with `analytic=True` on complex ellipses; the code forwards this flag to every logarithm and square root, while the removable entire function \(\phi(z)=(e^z-1)/z\) uses a direct quotient away from zero and a series with a rigorous tail near zero. The witness is the exact binary64 coefficient vector stored in the JSON record, with \(x_0=1/100\) and \(X=8\) exact; this is a legitimate explicit real metric even though it is not the exact-decimal-rational witness proposed above.

I reran the enclosure independently at 160, 256, and 320 bits. TTCS identified one formal weakness in the peer implementation: the near-zero Taylor remainder radius for \(\phi\) was obtained by a float conversion with a large safety factor. `workspace/scripts/perp_rigorous_enclosure_strict.py` replaces this by the pure-Arb bound `abs(z).upper()` and otherwise preserves the bolt-regular Ricci code. Its 256-bit output is `workspace/data/o11_strict_arb_x001_X8_256.json`. At tolerance \(10^{-20}\), it gives
\[
\begin{aligned}
J_6/(8\pi^2)&\in[0.999116243135324311\pm2.25\times10^{-19}],\\
P/(8\pi^2)&\in[0.999108702733592648\pm4.58\times10^{-19}],\\
(J_6-P)/(8\pi^2)&\in[7.540401731663\times10^{-6}\pm3.80\times10^{-19}].
\end{aligned}
\]
The 160- and 320-bit runs also enclose the same value strictly below one. The upper bound certifies
\[
\boxed{J_6<8\pi^2},\qquad
\varepsilon_0:=1-J_6/(8\pi^2)>0.0008837568646756.
\]
The closed Ricci formula and all desingularized rewritings were checked symbolically against the independent Cartan derivation by `Sessions/S1003A01/workspace/scripts/check_bianchi_ricci_closed_form.py`; the run returned zero for all four Ricci components and the \(D_1,A_1,A_2,A_3\) rewrites. The binary64 coefficient vector is itself an exact dyadic-rational witness after freezing; at 256 bits `arb(float(v))` contains that dyadic with zero radius, so no optimizer convergence or uncertain target coefficients enter the proof.

Therefore the strict O11 counterexample is now a theorem: after smooth exact-CH attachment and residual-finite replication,
\[
\boxed{
\limsup_{j\to\infty}\frac{\alpha(M_j)}{h_j}
\le4-\frac89\varepsilon_0
<3.999214438342511<4.
}
\]
This disproves the universal coefficient-four conjecture for the balanced blow-up family. It does not determine the sharp coefficient: the cell infimum within and beyond diagonal \(SU(2)\) symmetry, a matching global lower bound, and the near-extremal structure remain open.



---

## Source step13_einstein_fillings_blown_up_ball.md

Original: [sources/Sessions/S1003A02/workspace/notes/step13_einstein_fillings_blown_up_ball.md](../sources/Sessions/S1003A02/workspace/notes/step13_einstein_fillings_blown_up_ball.md)

# Step 13 — SU(2)-invariant Einstein fillings of the blown-up ball and the "total depletion" endpoint of 𝔓_{1,0}

Agent2, Execute. Scripts: `workspace/scripts/einstein_bolt_series.py`, `einstein_bolt_shoot.py`, `einstein_bolt_fig.py`.
Data: `workspace/data/einstein_bolt/series_n{1,3}.json`, `workspace/data/einstein_bolt_runs/` (bisection records `bis*_n1.json`,
biaxial `biax_n1.json`, `biax_n3.json`, summary `ach_family_summary.csv`). Figure: `workspace/figures/einstein_bolt_ach_family.png`.

## 1. Why this question

The cell cost satisfies the Chern–Weil identity P = 8π² + 4ΔW₊ + ΔS/12 relative to the CH ball it replaces. "Total depletion",
𝔓_{1,0} = 0, is exactly the existence (in a limit) of an Einstein metric with Ric = −6g on the blown-up ball D#CP̄² which is
asymptotic to CH² with *standard* CR infinity, fast enough that truncation costs vanish. For ACH Einstein metrics the free
(mass-type) term enters at order e^{−4r}, so truncation at radius R costs O(e^{−4R}) against volume e^{4R}; existence would give
𝔓_{1,0} = 𝔍_{1,0} = 0 and, through covers, α(X#kCP̄²) = o(h) along large-injectivity-radius ball quotients — inside LeBrun's open
range k < c₁²/3. Nonexistence is the geometric reason one expects p_{1,0} > 0. This step settles the question inside the
cohomogeneity-one class that contains every cell built so far (diagonal Bianchi IX), and finds a new family on the way.

## 2. Exact setup and local theory at the bolt

g = dt² + a₁²σ₁² + a₂²σ₂² + a₃²σ₃², dσᵢ = 2σⱼ∧σₖ. Orthonormal Ricci (Cartan-checked in S1003A01):
R₀₀ = −Σaᵢ''/aᵢ, Rᵢᵢ = −aᵢ''/aᵢ − (aᵢ'/aᵢ)(aⱼ'/aⱼ + aₖ'/aₖ) + 2(aᵢ⁴ − (aⱼ² − aₖ²)²)/(a₁a₂a₃)².
Checks: CH (a₁=a₃=sinh t, a₂=sinh t cosh t) gives Ric = −6 in all four components; Burns (a₁=a₂=√(t²+x₀), a₃=t) is scalar-flat.
All three slot forms ωᵢ = aᵢ dt∧σᵢ + aⱼaₖ σⱼ∧σₖ are self-dual for dt∧σ₁∧σ₂∧σ₃, so with the bolt in slot 3 and a₃'(0)=1 the
manifold is the blown-up ball with its complex orientation, whichever slot carries the CH Kähler direction at infinity:
slot 3 = aligned (U(2), Burns direction ∥ ω_CH), slot 1 or 2 = perpendicular (Burns direction ⟂ ω_CH).

**Regular series (sympy, exact).** For a₃ = n t + …, a₁(0) = a₂(0) = b, Einstein Ric = −6g with the constraint:
- n = 1: p₂ = q₂ = (3b² + 2)/(2b), r₃ = −2/(3b²), r₅ = (27b⁴ + 72b² + 53)/(60b⁴); the t⁴ anisotropy d = p₄ − q₄
  (a₁ − a₂ = d t⁴ + …, the charge-4 bolt mode) is free. Regular O(−1) Einstein bolts form a **two-parameter family (b, d)**.
- n = 3: no free anisotropy through order 6; p₄ = q₄ = −(12b² + 35)/(24b³), r₃ = −2/b².

**Kähler condition read from the series.** The slot-3 Kähler condition (a₁a₂)' = 2a₃ at second order gives
2(3b² + 2) = 2n. For n = 3 this forces b² = 1/3, the Calabi-ansatz KE metric on O(−3) with bolt area πb² = π/3 = 2π(n−2)/6
(matches ∫_E ρ = 2π c₁·E = −6 Area). For n = 1 it reads 3b² + 2 = 1: impossible — the local form of the global obstruction
∫_E ρ = 2π > 0 > −6 Area(E) to any negative KE metric containing a (−1)-curve. The slot-1 Kähler condition (a₂a₃)' = 2a₁ fails at
the bolt (b ≠ 2b), so the perpendicular solutions below are not Kähler for any slot structure.

## 3. Asymptotic types and the shooting method

In Lᵢ = log aᵢ, yᵢ = Lᵢ': yᵢ' = 6 − yᵢ² − yᵢ(yⱼ+yₖ) + Potᵢ, constraint y₁y₂+y₂y₃+y₃y₁ = 6 + ½ΣPotᵢ (held to ≤10⁻¹¹).
Fates: AH (yᵢ → √2, conformal infinity a triaxial Berger sphere); ACH with Kähler slot k (yₖ → 2, others → 1,
κₖ = aₖ/(aᵢaⱼ) → 1, Rossi ratio ρ = aᵢ/aⱼ → const; ρ is a neutral direction: (L_i−L_j)'' + 4(L_i−L_j)' = O(e^{−2t}), so ρ freezes);
singular (one aᵢ blows up, the other two collapse in finite t). ACH is a saddle: in the 2-parameter bolt family it is the
separatrix between AH and singular, found by bisection in d at fixed b (70 halvings; plateau length limited by binary64).

**Validation.** O(−3), U(2): b < 1/√3 singular, b > 1/√3 AH, b = 1/√3 stays on the ACH₃ plateau (deviation 8×10⁻⁸ at t ≈ 8)
before roundoff exit — the method recovers the Calabi KE ACH metric exactly where the series predicts.

## 4. Results for the blown-up ball (n = 1)

**(A) Aligned/U(2) bolts are never ACH.** With a₁ = a₂ enforced exactly, every b ∈ [0.003, 100] gives an AH metric
(Taub–bolt–AdS type) with Berger squashing c₃/c₁ ≤ 0.2887 (max near b = 1; 0.0013 at b = .003, 0.0047 at b = 100). Never ACH,
never round. (Consistent with the Kähler obstruction: U(2) ACH Einstein ⇒ Calabi/Page–Pope ⇒ impossible for n = 1.)

**(B) A one-parameter family of complete perpendicular ACH Einstein metrics on D#CP̄².** For each b ≳ 0.29 the AH/singular
separatrix d*(b) approaches the ACH₁ fixed point (κ₁ → 0.998–0.9998, y → (2,1,1) to 10⁻³–10⁻⁴), the Kähler-type direction at
infinity being slot 1, perpendicular to the bolt fibre. The CR infinity is a **Rossi sphere** with ratio ρ(b) = a₂/a₃:

| b | 0.29 | 0.4 | 0.55 | 0.7 | 0.8 | 0.9 | 1.1 | 1.5 | 2 | 4 | 8 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ρ | 3.20 | 2.63 | 2.30 | 2.20 | 2.196 | 2.22 | 2.32 | 2.65 | 3.18 | 5.63 | 10.9 |

ρ_min ≈ 2.20 at b ≈ 0.75–0.8; ρ ≈ 1.36 b for large b; ρ increases as b ↓ 0.29, below which the separatrix no longer approaches
ACH (min deviation 0.1–0.8, a different transition). Plateau drift of ρ is ≈ 3 % and comes from the departure; the neutral-mode
estimate above bounds the remaining asymptotic change by ≈ 10⁻³ relative. Since ρ and 1/ρ are CR-equivalent, the image of the
family in the Rossi line is ρ ∈ [≈2.20, ∞), and **the standard sphere ρ = 1 is not reached.**

**(C) Consequence (numerical theorem-level evidence, not a proof).** Within diagonal SU(2)-invariant metrics there is no Einstein
metric on the blown-up ball with Ric = −6g asymptotic to CH² with standard CR infinity: aligned bolts are AH, and perpendicular
ACH bolts realize only Rossi spheres with ρ ≳ 2.2. Hence the "total depletion" endpoint of the cell problem does not occur in the
class containing all cells constructed so far, and the codimension count is overdetermined: 2 bolt parameters versus the 2
conditions (ACH separatrix, ρ = 1). The cheap cells are *perpendicular* precisely because the perpendicular bolt family is the
only one that reaches the ACH stratum at all; their cost below 8π² measures how far the exact-CH collar can be bent toward an
Einstein filling whose CR infinity sits at ρ ≥ 2.2.

## 5. What this does and does not settle

Settled numerically: the structure of SU(2)-diagonal Einstein O(−1) bolts (two parameters; AH generic; ACH separatrix only in the
perpendicular orientation; Rossi ratio bounded below by ≈ 2.2; U(2) bolts AH with squashing ≤ 0.289).
Not settled: (i) a proof — needs a rigorous separatrix enclosure (e.g. interval shooting from an ACH asymptotic expansion with
parameter ρ inward to the bolt) or a monotone quantity for the ODE; (ii) non-diagonal/non-symmetric Einstein fillings of the
standard sphere (Biquard's ACH deformation theory makes the filling map Fredholm; the standard sphere is far from ρ ≈ 2.2 in CR
moduli); (iii) the quantitative lower bound for 𝔓_{1,0}: nonexistence of an Einstein limit suggests, but does not imply,
𝔓^{SU(2)}_{1,0} > 0 — one still needs compactness of P-minimizing SU(2) sequences with variable outer radius (ODE compactness
on the bolt side plus control of where the defect sits).

## 6. Proposed next constructions

1. **Rigorous version of (B)/(C):** asymptotic expansion of ACH₁ Einstein solutions with Rossi ρ (free data: ρ, the e^{−4t}
   mass-type coefficient and t-shift), interval integration inward, matching with the bolt series — a computer-assisted
   theorem "ρ(b) ≥ 2.1 for all b" plus large/small-b asymptotics.
2. **Ball cross-check:** the same shooting from a nut gives the SU(2) Einstein ACH fillings of Rossi spheres on B⁴, which must pass
   through CH² at ρ = 1 (Biquard's family); this calibrates the ρ measurement.
3. **Cost of CR mismatch:** a lower bound P_cell ≥ F(ρ_min) in the SU(2) class via a calibration/Lyapunov functional built from the
   neutral mode u = L₂ − L₃ (u'' + 4u' is forced only by Einstein defects), i.e. "to bend the Einstein separatrix's ρ ≈ 2.2 to the
   collar's ρ = 1 one must pay Ricci defect"; compare with the certified p ≈ 0.9991 cell.
4. **Literature:** SU(2)-invariant ACH Einstein metrics and Rossi spheres (Hitchin's Painlevé VI SDE family, Biquard's
   "Métriques autoduales sur la boule", Biquard–Herzlich Burns–Epstein invariant, which gives χ − 3τ = 5 for these fillings).



---

## Source step14_chirality_nut_and_control_localization.md

Original: [sources/Sessions/S1003A02/workspace/notes/step14_chirality_nut_and_control_localization.md](../sources/Sessions/S1003A02/workspace/notes/step14_chirality_nut_and_control_localization.md)

# Step 14 — Chirality, nut calibration, and where the complete-cell action is spent

Agent3, Execute. This note records the consequences of four checks on the Step-13 diagonal Einstein-bolt picture and relates them to the supplied classical-gap supplement and the peer's larger exact-collar cells.

## 1. Frontier context from the supplied supplement

The human-supplied `Skills/geometric-analysis/research/supplements/20261004_classical_and_quantitative_gaps.tex` gives the clean classical position for handle-free blow-ups:
\[
8\pi^2\max\{0,k-A/3\}\le \inf P\le 8\pi^2k.
\]
Thus for \(0<k<A/3\), precisely the region probed by an isolated blow-up cell in a large complex-hyperbolic cover, the listed classical lower value is zero. A positive complete-cell infimum combined with an all-competitor decomposition theorem would add the first positive information in that range. The same supplement also records:

- under negative-Yamabe closure, \(\inf\mathcal E=\inf\mathcal J\) whenever \(\inf\mathcal E<1\);
- the N1 neighborhood estimate
  \[
  \mathcal J+(T/A-2/3)_+\ge c_*/(1+\nu/(2\pi^2));
  \]
- the actual-field differential estimate
  \[
  \Sigma\le C\{\Pi+\sqrt{\Pi Y}\};
  \]
- exact formal integral data obeying the displayed classical numerical budgets but having \(\mathcal J=o(h)\), showing why a localization or decomposition theorem must transport same-field differential information rather than only Chern–Weil numbers.

These facts sharpen the role of the cell problem without changing the route.

## 2. The Step-13 ACH bolt branch is not self-dual

Script: `workspace/scripts/einstein_chirality_check.py`.
Data: `workspace/data/einstein_bolt_chirality.json`.
Independent reading: `trace/ttcs/results/step14_ttcs01_verifier1_integration.md`.

The script reconstructs the exact radial 2-jet of a diagonal Bianchi-IX Einstein trajectory at a sample time and feeds it to the independent coordinate/JAX curvature evaluator from `o11_rotated_cell.py`. Complex hyperbolic space calibrates the two Weyl blocks:
\[
(s,|\operatorname{Ric}^\circ|^2,WA,WB)=(-24,0,0,24),
\]
so in the complex orientation \(WA=|W^-|^2\), \(WB=|W^+|^2\).

For representative near-separatrix bolt shoots, both blocks are nonzero in the core. At \(t=0.08\):

| bolt radius \(b\) | \(|W^-|^2\) | \(|W^+|^2\) |
|---:|---:|---:|
| 0.35 | 2369.60 | 409.52 |
| 0.8 | 167.83 | 36.13 |
| 4 | 7.96 | 6.40 |

Therefore the observed family is neither self-dual nor anti-self-dual in the bulk. Hitchin/Tod Painlevé-VI self-dual Einstein theory cannot classify this branch. Orientation reversal only swaps the two nonzero blocks.

Along the finite ACH plateau, \(W^-\) decays strongly while \(|W^+|^2\) approaches the CH value. For \(b=0.8\),
\[
|W^-|^2(t=1)=2.47\times10^{-2},\qquad
|W^-|^2(t=2)=3.13\times10^{-6},
\]
and at the closest recorded point it is \(8.25\times10^{-13}\), while \(|W^+|^2\) is near \(24\) on the reliable part of the plateau. This is compatible with \(|W^-|=O(e^{-4t})\), but the trajectories eventually leave the unstable ACH saddle. The correct statement is that the branch is **asymptotically half-conformally-flat if the exact separatrix exists**, because its leading curvature approaches CH; it is not a globally self-dual family. Leading curvature convergence does not fix the horizontal CR modulus \(\rho\), so it is fully compatible with the Step-13 Rossi ratios \(\rho\gtrsim2.2\).

This redirects rigor to the full constrained Einstein ODE: existence of the bolt-to-ACH separatrix, its limiting \(\rho(b)\), and a certified separation from \(\rho=1\). Biquard's self-dual ball theory remains a calibration/comparison, not a substitute.

## 3. Smooth-nut cross-check of the ACH readout

Scripts and data:

- `workspace/scripts/einstein_nut_series.py`;
- `workspace/data/einstein_nut/series.json`;
- `workspace/scripts/einstein_nut_shoot.py`;
- `workspace/data/einstein_nut_runs.json`.

The exact smooth-nut expansion is
\[
a_i=t+c_i t^3+d_i t^5+O(t^7),\qquad c_1+c_2+c_3=1,
\]
with two free cubic coefficients. In terms of \(q=c_2,r=c_3\),
\[
\begin{aligned}
c_1&=1-q-r,\\
d_1&=\frac3{20}(8q^2+28qr-13q+8r^2-13r+4),\\
d_2&=\frac3{20}(8q^2-12qr-3q-12r^2+12r-1),\\
d_3&=-\frac3{20}(12q^2+12qr-12q-8r^2+3r+1).
\end{aligned}
\]
Complex hyperbolic space with fibre slot 2 occurs at
\[
(c_1,c_2,c_3)=(1/6,2/3,1/6),
\]
where these fifth-order terms exactly match \(a_1=a_3=\sinh t\), \(a_2=\tfrac12\sinh2t\). The shoot gives closest approach
\[
\kappa_2=0.99999834,\qquad \rho_2=1+O(10^{-13}),\qquad
|(y_1,y_2,y_3)-(1,2,1)|=2.03\times10^{-5}.
\]
Cyclic copies recover the other fibre slots. Hence the Step-13 definitions
\[
\kappa_k=\frac{a_k}{a_i a_j},\qquad \rho_k=\frac{a_i}{a_j}
\]
are correctly normalized, and \(\rho=1\) is the standard CR point.

The numerical endpoint at large \(t\) must not be used: the ACH saddle has an unstable rate \(+2\), so even the exact-CH initial truncation eventually exits because binary64/truncation error is amplified. Closest approach is the meaningful datum. Generic nut parameters are merely local Einstein germs; they run to AH or singular ends unless one parameter is tuned. The current runs therefore do not construct Biquard's nonunit Rossi family. They only validate the classifier, slot convention, \(\kappa\)-normalization and \(\rho=1\) basepoint.

## 4. The certified cell does not pay in a late CR-correction layer

Script: `workspace/scripts/o11_cell_einstein_shadow.py`.
Data and figure:

- `workspace/data/o11_cell_einstein_shadow.json`;
- `workspace/figures/o11_cell_einstein_shadow.png`.

For the certified \(X=8,x_0=0.01\) profile, the bolt radius is \(b=0.1\). The bolt anisotropy is
\[
d=(a_1-a_2)/t^4\approx-0.46227,
\]
consistent in sign with the fixed-slot convention. Matching \((b,n,d)\) to a Ric\(=-6g\) bolt orbit does **not** match the full 2-jet: the cell has \(p_{2,\mathrm{cell}}\approx5.16\), while Einstein regularity forces
\[
p_{2,E}=\frac{3b^2+2}{2b}=10.15.
\]
The compared Einstein trajectory therefore separates immediately and its numerical integration fails by \(t\approx0.297\); values extrapolated after that time have no geometric meaning. Moreover \(b=0.1\) is below the Step-13 threshold at which the AH/singular boundary visibly approaches an ACH saddle.

The positive-square action is concentrated at the bolt scale:
\[
t_{50}=0.0649,\quad t_{75}=0.1009,\quad t_{90}=0.1496,\quad t_{99}=0.3191,
\]
while the exact CH collar begins at outer geodesic distance \(t\approx1.755\). These quantiles are close to the Burns bubble density. Thus the literal story “follow an Einstein ACH filling, then pay most of the cost in a late CR layer” is false for this witness. The metric pays almost the full \(8\pi^2\) positive action in the Burns-like core and reaches the exact CH collar with little additional positive-square action.

This cumulative plot does **not** locate the small subthreshold saving \(1-P/(8\pi^2)\approx8.9\times10^{-4}\); it mainly resolves the unit Burns cost. The saving comes from the calibrated cubic interaction against the completed squares and must be studied by a Burns-centered expansion, not by the cumulative positive density alone.

The strongest supported variational object is therefore a local weighted control value from regular \((-1)\)-bolt data to a CH-directed transverse section,
\[
\mathcal I_{\rm core}=\inf\int_0^\tau\sum_i\frac{\lambda_i}{4}
\left(u_i'-\frac{2H_i}{\lambda_i}\right)^2dt,
\]
or a Hamilton--Jacobi subsolution/calibration for this action. In the small-bubble regime, the more precise route is the Burns-centered identity
\[
\frac{P}{8\pi^2}=1+S_1+S_2+S_3+
\int\frac{2u_1u_2u_3}{\lambda_2}\,dt,
\]
which can prove or sharpen the supported \(-9b^4\log(1/b^2)\) response. A compactness contradiction for all free-radius cells still needs control over varying bolt radius, collapse of the weights \(\lambda_i\), the Einstein constant and migration of the defect.

## 5. New large-collar evidence and the neutral flux variable

Peer note: `Sessions/S1003A01/workspace/notes/step14_large_collar_resistance_and_cluster_budget.md`.

The peer has now rigorously enclosed physically continued cells:
\[
\frac{J_6(X=32)}{8\pi^2}<0.998736769872,\qquad
\frac{J_6(X=64)}{8\pi^2}<0.998702764484,
\]
with \(P(X=64)/(8\pi^2)<0.998701\). These improve the separated balanced construction to
\[
\limsup\alpha_j/h_j<3.998846902+\varepsilon,
\]
for arbitrarily small collar smoothing loss. Fixed-radius profiles stabilize from \(X=32\) to \(64\), supporting a complete finite-action diagonal limit, but not proving stationarity, optimality or a positive limiting infimum.

The reduced neutral mode is not controlled by endpoint ratio alone. In the model
\[
\mathcal A_T(q)=\int_0^T e^{4t}(q''+4q')^2dt,
\]
with clamped endpoints, the exact minimum tends to \(64(\Delta q)^2\). But the transported quantity is
\[
\Phi=q+\tfrac14q',\qquad \Phi'=\tfrac14(q''+4q'),
\]
so a free entrance slope can change \(q\) at zero model cost. For the exact diagonal metric,
\[
(Wq')'=W(V-E),\qquad
V=\frac{4(a_2^2-a_3^2)(a_2^2+a_3^2-a_1^2)}{W^2},\quad
E=(\operatorname{Ric}^\circ)_{22}-(\operatorname{Ric}^\circ)_{33},
\]
and \(|\operatorname{Ric}^\circ|^2\ge E^2/2\). A diagonal lower theorem thus requires low-cost entry into a noncollapsed ACH tube, control of \(W\), the potential \(V\), and the entrance flux \(q'\), together with rigorous separation of the bolt Einstein filling map from the standard value \(\rho=1\). Ratio mismatch alone is insufficient.

## 6. Resulting research judgment

Three potential shortcuts were tested and rejected in their strong form:

1. The bolt branch is not Hitchin/Biquard self-dual in the interior.
2. The ball calibration validates \(\rho\), but generic nut germs are not automatically ACH fillings.
3. The certified small-b cell does not realize a late CR-mismatch payment.

What survives is a coherent two-scale structure:

- **core:** a nearly Burns bolt cost with a small negative cubic correction, naturally attacked by the exact three-squares-plus-cubic identity and a local control calibration;
- **end:** a finite-weight ACH neutral-mode resistance governed by the flux-corrected variable \(\Phi\), relevant only after noncollapse, potential and entrance-flux control are established.

The large-collar continuation indicates that both scales may coexist in a complete finite-action diagonal profile. Turning this into \(\mathfrak P^{SU(2)}_{1,0}>0\) requires a coercive compactness/decomposition statement linking them; the ODE enclosure of the non-self-dual bolt-to-ACH branch remains a separate necessary input. None of this excludes nonsymmetric standard-CR Einstein fillings or yields an unrestricted global lower bound yet.



---

## Source step15_ach_projected_theory.md

Original: [sources/Sessions/S1003A02/workspace/notes/step15_ach_projected_theory.md](../sources/Sessions/S1003A02/workspace/notes/step15_ach_projected_theory.md)

# Step 15–17 synthesis: projected ACH dynamics and a validated Einstein filling of the blown-up ball

Session S1003A02. This note records the exact structure found in Step 15, the repaired validated
computation of Steps 16–17, and the resulting existence theorem. It replaces the dropped
"Step-15 note". Every numerical statement below is tied to a script and a data file.

## 1. Setting

Diagonal Bianchi IX metrics on (0,∞)×SU(2),
  g = dt² + a1(t)² σ1² + a2(t)² σ2² + a3(t)² σ3²,  dσ_i = 2 σ_j∧σ_k,
with Einstein normalization Ric = −6g (complex hyperbolic CH² has holomorphic sectional curvature −4;
in these variables CH² is a1=a3=sinh t, a2=sinh t cosh t, up to slot permutation).
With L_i = log a_i, y_i = L_i' the Einstein equations are
  y_i' = 6 − y_i (y1+y2+y3) + Pot_i,
  Pot_i = 2 e^{2L_i−2L_j−2L_k} − 8 e^{−2L_i} sinh²(L_j−L_k),
together with the constraint C = y1y2+y2y3+y3y1 − 6 − ½ΣPot_i = 0, which propagates by C' = −2SC.
Bolt: slot 3 collapses, a3 = t + O(t³), a1(0)=a2(0)=b. With σ3 normalized as for the Burns metric
this is the zero section of O(−1) → CP¹, so the manifold is the total space of O(−1), i.e. the
interior of D⁴ # CP̄² (blown-up ball). The regular bolt data form a two-parameter family (b,d),
d = p4 − q4 the t⁴ coefficient of a1 − a2 (Step 13, `scripts/einstein_bolt_series.py`).

## 2. Compact ACH system (Step 15, `scripts/ach_projected.py`, `data/ach_projected/structure.json`)

For fibre slot f and horizontal slots (g,h) in cyclic order put
  W = (y_f, y_g, y_h, κ, q, ζ),  κ = a_f/(a_g a_h),  q = log(a_g/a_h),  ζ = 1/(a_g a_h).
The system is exactly autonomous:
  y_f' = 6 − y_f S + 2κ² − 8ζ² sinh²q/κ²,
  y_g' = 6 − y_g S − 2κ² + 4ζ e^{−q} + 4ζ² sinh 2q/κ²,
  y_h' = 6 − y_h S − 2κ² + 4ζ e^{q} − 4ζ² sinh 2q/κ²,
  κ' = κ(y_f − y_g − y_h),  q' = y_g − y_h,  ζ' = −ζ(y_g + y_h).
(Agreement with the (L,y) field: 1.4×10⁻¹⁵ relative.)

**Equilibrium curve.** ACH_f = {E(q) = (2,1,1,1,q,0)}. A metric converging to E(q∞) has
a_f ~ c_f e^{2t}, a_g, a_h ~ e^{t}, κ → 1: it is asymptotically complex hyperbolic, its
conformal infinity is the left-invariant CR structure on S³ with contact form σ_f and Levi form
proportional to ρσ_g² + ρ⁻¹σ_h², ρ = e^{q∞} (Rossi sphere). ρ and 1/ρ are CR-equivalent; ρ=1 is the
standard sphere (validated by the smooth-nut computation of Step 14, which recovers CH² at ρ=1).

**Spectrum.** The Jacobian at E(q) has characteristic polynomial
  λ(λ−2)(λ+2)(λ+4)(λ+6)(λ+8)
(exact sympy). Modes: one unstable (+2), ζ/time-shift (−2), anisotropy a=y_g−y_h (−4), −6, the
constraint mode (−8), and the neutral Rossi direction (0). Left unstable eigenvector
  l_u = (1, −1, −1, 6, 0, −2 cosh q).
Consequence: the ACH stable set is codimension one; the two-parameter bolt family meets it
generically in a curve. This is the observed one-parameter family d*(b) and explains why no
stronger matching (e.g. prescribing ρ) is available inside the symmetric class.

**Neutral invariant.** Φ̃ = q + (y_g − y_h)/4 − ζ sinh q has derivative exactly quadratic in
(W − E(q), ζ) (`scripts/ach_phi_drift.py` verifies symbolically that the constant and linear
ζ-terms cancel). Φ̃ → q∞ on the equilibrium curve, so ρ∞ is read off any section with an
O(ζ²) error.

## 3. Cusp isolating block (Step 15, `scripts/ach_block_verify.py`, `data/ach_block/`)

Eigen-coordinates with the linear ζ-forcing removed (dy_f=y_f−2, ds=y_g+y_h−2, dk=κ−1, a=y_g−y_h):
  u = dy_f − ds + 6dk − 2cosh q ζ  (rate +2),  σ1 = dy_f − ds − 2dk + 2cosh q ζ  (−6),
  σ2 = 2dy_f + 3ds + 2dk − 4cosh q ζ  (−8),  â = a + 4 sinh q ζ  (−4).
Block B(K,ζ0,Q) = {|u|,|σ1|,|σ2|,|â| ≤ Kζ, 0<ζ≤ζ0, q∈Q}; rescaled coordinates ub=u/ζ etc.

**Lemma B (Arb-verified).** For K=1, ζ0=10⁻², Q=[0.70,0.90]:
(i) on the slabs ½K ≤ ±ub ≤ K, ±ub' > 0 (margins ≥ 1.87); (ii) on the faces s1b, s2b, ab = ±K the
flow points strictly inward (margins ≥ 1.82); (iii) y_g + y_h ≥ c = 1.99846 on B, hence
ζ' ≤ −cζ; (iv) on B, |Φ̃'| ≤ M ζ² with M = 19.5825 (`data/ach_block/phidrift_K1_z0.01_q0.7_0.9.json`).
Face functions are divided by ζ symbolically and the hyperbolic functions rewritten through E=e^q
(interval arithmetic cannot cancel 12e^q − 12e^q; the unrewritten version failed falsely).
Further patches up to q ≤ 3.2 are in `data/ach_block/` (margins ≥ 1.64).

Consequences inside B: a solution in B at time T with q(T) a distance
δ_q = (K + 4 sinh 0.9)ζ(T)/c from ∂Q keeps q∈Q while it stays in B; a solution that stays in B
for all t ≥ T has ζ → 0 exponentially, |W − E(q)| ≤ C ζ, q → q∞ with |q∞ − Φ̃(T)| ≤ Mζ(T)²/(2c);
it is therefore a complete ACH end with Rossi parameter q∞.

## 4. The regular bolt: analytic Fuchsian lemma (Step 17, `scripts/ach_bolt_fuchs.py`)

Put s = t², a1 = A(s), a2 = B(s), a3 = tC(s), D = s d/ds. Exactly (sympy check of
s(a1''−rhs1) = E_A, s(a2''−rhs2) = E_B, t(a3''−rhs3) = E_C returns 0, 0, 0):
  E_A = 4D²A + 4DA(DB/B + DC/C) − 6sA − 2(A⁴−B⁴)/(AB²C²) − 4s/A + 2s²C²/(AB²),
  E_B = (A↔B),
  E_C = (4D²+2D)C + 2(C+2DC)(DA/A+DB/B) − 6sC − [2s²C⁴ − 2(A²−B²)²]/(CA²B²).
With σ = (A+B)/2 − b, δ = A − B, γ = C − 1 the linear part at s=0 is
L = (4D², 4D² − 16, 4D² + 2D): σ and γ are nonresonant for k≥1, δ has the resonance k=2,
whose coefficient is the free parameter d. The formal solution (b = 4/5) begins
  σ = 49s/20 − 2335s²/1536 + …,  δ = d s² + 497 d s³/240 + …,  γ = −25s/24 + 68837 s²/15360 + …,
agreeing with the t-series of Step 13 (p2, r3, r5 differences = 0).

**Lemma F.** Let N=6, m=7, s0=10⁻⁴ (t0 = 10⁻²), d ∈ [0.28697953, 0.28701987]. Write
Y = Y_N + R with Y_N the exact order-N polynomial. R solves
  R = L⁻¹[Φ(Y_N+R) − Φ(Y_N) + ρ_N],
where the inverses are the radial integrals (D−c)⁻¹f(s) = ∫₀¹ λ^{−c−1} f(λs) dλ, giving on functions
with |f| ≤ F|s|^m the bounds
  (4D²)⁻¹: |R| ≤ F|s|^m/(4m²), |DR| ≤ F|s|^m/(4m);
  (4D²−16)⁻¹: |R| ≤ F|s|^m/(4(m−2)(m+2)), |DR| ≤ F m|s|^m/(4(m−2)(m+2));
  (4D²+2D)⁻¹: |R| ≤ F|s|^m/(2m(2m+1)), |DR| ≤ F|s|^m/(2(2m+1)).
The residual ρ_N is an exact rational function, its numerator exactly divisible by s^m; Arb/acb
bounds over 60 complex squares covering the closed disc |s| ≤ s0 give sup|ρ_N|/|s|^m ≤
(1.78×10⁵, 3.40×10³, 1.47×10⁶). Interval Jacobians of Φ over {|s|≤s0} × (Y_N + ball) give a
nonnegative matrix M with M r + c ≤ r/2 componentwise for
  r = (1.81×10³, 1.27×10⁴, 37.8, 2.64×10², 1.39×10⁴, 9.75×10⁴)
(seminorm constants of R_σ, DR_σ, R_δ, DR_δ, R_γ, DR_γ), and contraction factor 0.0325 in the
r-weighted max norm. Hence there is a unique solution with these bounds; since the integral
operators preserve holomorphy on the disc, A, B, C are holomorphic in s, so the metric is
real-analytic across the bolt (A, B even in t, a3 odd, A−B = O(t⁴), C(0)=1: the smoothness
conditions for the O(−1) bolt). Uniqueness among solutions with R = O(s^m) (contraction on small
discs plus regular ODE uniqueness) identifies it with the bolt Einstein metric of data (4/5, d).
The constraint holds identically: t²C is continuous, vanishes at t=0 because C(0)=1, and C' = −2SC
with S = 1/t + O(t) forces t²C ≡ const = 0.
Data: `data/ach_capd/fuchs_boxes_N6_complex.json` (complex-disc, used) and `fuchs_boxes_N6.json`
(real interval, identical boxes). The remainder at s0 is ≤ 10⁵ s0⁷ ≈ 10⁻²³, below binary64
resolution of the boxes; it is nevertheless included before outward rounding.

## 5. Validated transport (Steps 16–17)

`scripts/ach_bolt_capd.cpp` is a CAPD C0-Lohner integrator for X = (m, δ_L, L3, y_m, η, y3) with
L1,2 = m ± δ_L/2, y1,2 = y_m ± η/2, using the cancellation-free identities
  P1 + P2 = 8e^{−2m} cosh δ_L − 4e^{2L3−4m},
  P1 − P2 = 8e^{−2L3} sinh 2δ_L − 8e^{−2m} sinh δ_L,
  P3 = 2e^{2L3−4m} − 8e^{−2L3} sinh² δ_L.
The Step-16 version had a wrong y_m equation (it used a non-identity for P1+P2), which is why the
Step-16 pilot ran away to ub ≈ −1988. It was repaired. `scripts/ach_capd_field_check.py` parses the
field string directly from the C++ source: symbolic difference from the exact potentials = 0 in
all seven components; 2000 random states agree with `rhs_md` to 1.4×10⁻¹⁴; a CAPD point box chained
from t0=0.01 to t=2.7 contains the DOP853 solution at every checkpoint (widths ≤ 3.3×10⁻⁶)
(`data/ach_capd/field_check.json`). The Step-16 pilot files `ach_capd_pilot_t0*.json` enclose the
erroneous system and are void.

`scripts/ach_wazewski_run.py` transports the 40 Fuchsian boxes (d-subintervals of width
1.0085×10⁻⁶ tiling [0.28697953, 0.28701987]) from t0 = 0.01 to T = 2.75 (dt 0.05, order 30).
Result (`data/ach_capd/wazewski_T2.75.json`): every box lies in B(1, 10⁻², [0.70,0.90]) with
ζ(T) ∈ [0.009647, 0.009658], q(T) ∈ [0.80095, 0.80105], |s1b|, |s2b| ≤ 0.05, ab ≈ 0.27, and the
q-faces at distance > δ_q ≈ 0.024; the first box has ub ∈ [−0.754, −0.708] (lower egress slab) and
the last ub ∈ [0.708, 0.754] (upper slab); ub increases monotonically across the tiling.
Floating design (`data/ach_capd/passage_design_T2.75.json`): dub/dd ≈ 3.7×10⁴ at T.

## 6. Theorem (complete ACH Einstein metric on the blown-up ball with non-standard CR infinity)

**Theorem E.** There is d₀ ∈ [0.28697953, 0.28701987] such that the diagonal SU(2)-invariant metric
with regular O(−1) bolt data (b, d) = (4/5, d₀) is a complete real-analytic Einstein metric,
Ric = −6g, on the total space of O(−1) → CP¹ (the interior of D⁴#CP̄²). It is asymptotically complex
hyperbolic with fibre direction σ1: y1 → 2, y2, y3 → 1, a1/(a2a3) → 1, all at rate O(e^{−1.99t}),
and its CR infinity is the left-invariant Rossi sphere with
  ρ∞ = lim a2/a3 ∈ [2.19013, 2.19242]  (q∞ ∈ [0.78396, 0.78500]),
in particular not the standard CR sphere. The metric has exactly SU(2) symmetry in the diagonal
class with a1 ≢ a2 (δ = d₀ s² + …, d₀ ≠ 0) and a2/a3 ↛ 1.

*Proof.* Lemma F gives the real-analytic bolt solution for every d in the interval, with rigorous
state boxes at t0; CAPD transports them to T = 2.75, where all lie in B. Let S± ⊂ [d−,d+] be the
sets of d whose orbit leaves B after T through the face ub = ±1. Strict egress (Lemma B(i)) makes
exit times continuous, so S± are relatively open; they are disjoint. Only the u-faces can be exit
faces: stable faces are strict ingress, ζ = ζ0 is ingress (ζ' < 0), ζ = 0 is not reached in finite
time, and q-faces are not reached while in B by the drift bound. The left endpoint lies in the
lower slab, which is forward-invariant until exit through ub = −1, so d− ∈ S− unless its orbit stays
forever, and likewise d+ ∈ S+. Connectedness of the d-interval then gives d₀ ∉ S+ ∪ S−: its orbit
stays in B for all t ≥ T. By §3 it converges exponentially to E(q∞) with
|q∞ − Φ̃(T)| ≤ Mζ(T)²/(2c) ≤ 4.57×10⁻⁴; Φ̃(T) ∈ [0.784419, 0.784546] over all boxes
(`data/ach_capd/rossi_enclosure_b0.8.json`). Completeness: t is arclength on [0,∞) and the orbits are
compact. Einstein: the second-order system plus C ≡ 0 (§4). ∎

Scope. This is one value b = 4/5 of the branch. It proves existence, not uniqueness in b or d,
and gives no nonexistence. Not proved here: non-Kählerness for an arbitrary (non-invariant) complex
structure and the failure of half-conformal flatness. Inside the diagonal class the Kähler bolt
condition 3b²+2 = n fails (3.92 ≠ 1, Step 13), and Step 14 found both Weyl halves large near the
bolt numerically, but a rigorous pointwise interval evaluation of W± (e.g. |W±|² ≠ 24, the
Kähler–Einstein value for Ric = −6g) is still to be done; the bolt 2-jet makes this an exact
algebraic computation at t = 0.

## 7. Branch picture (numerical, Step 15; not part of Theorem E)

`data/ach_projected/brA–brD.json`, `cont_down.json` (468 pts), `cont_up.json` (240 pts):
d*(b) smooth and monotone on b ∈ [0.138, 400]; ρ(b) has a minimum ρ_min ≈ 2.1897 near b ≈ 0.765,
rises to 5.88 at b = 0.138 (d* ≈ 3×10⁻⁹, collapse of the anisotropy) and grows like ≈1.343 b for
large b; ρ converges in ζ* as O(ζ*) (6×10⁻⁸ between ζ* = 10⁻⁴ and 10⁻⁵). At b = 0.8,
d* = 0.286999618893, ρ = 2.19185374, inside the rigorous enclosure above. The fate enumeration at
b = 0.8 (363 signed d values, `data/ach_fate/fate_b0.8.json`) found exactly four fate changes: the
mirror ACH1/ACH2 pair d = ±0.28699961889 (ρ and 1/ρ) and SING/OTHER boundaries at |d| ≈ 20.65
approaching no ACH stratum; no orbit approached the Kähler-type ACH3 stratum. The Step-15
background continuation/root task s15_t16_tool2 hit its 3600 s limit with no further output; the
earlier `roots` mode is flawed (U undefined on singular orbits) and superseded by the fate method.

## 8. Literature position

Primary sources now in Knowledge (read via the strategist's retrieval):
Biquard–Herzlich, *A Burns–Epstein invariant for ACHE 4-manifolds*
(`Knowledge/objects/papers/A-Burns-Epstein-invariant-for-ACHE-4-manifolds--4fc106911938--96372cf5692f/object.md`):
for every ACH Einstein 4-manifold
  (1/8π²)∫(3|W⁻|² − |W⁺|² + Scal²/24) = χ − 3τ + ν(X)
(Thm 1.2/Cor. 7.3), with a variation formula for ν in terms of the Cartan tensor (Thm 8.1).
Biquard's Astérisque 265 produces ACH Einstein fillings of small CR deformations of the standard
sphere on the ball; Akbar's Taub-bolt-AdS metrics are biaxial real-AH with CP² topology;
Calderbank–Singer toric self-dual fillings require special-orbit self-intersection ≥ 3; Page–Pope
metrics live on O(−n) with the wrong topology for n=1. None gives an ACH Einstein metric on O(−1),
and none fills a Rossi sphere off the ball. Theorem E is therefore new as far as the primary
literature located goes. For the blown-up ball χ − 3τ = 2 − 3(−1) = 5, and ν(S³_std) = −1, so the
Biquard–Herzlich identity does not obstruct a standard-CR Einstein filling: any diagonal
nonexistence statement is dynamical (separatrix geometry), not characteristic-class.

**Independent check available.** On Theorem E's metric the identity predicts
ν(S³_ρ) = (1/8π²)∫(3|W⁻|² − |W⁺|² + 24) − 5 with ρ ∈ [2.1901, 2.1925]; computing the convergent
integral along the branch and comparing with ν of Rossi spheres (via Thm 8.1 integrated from ρ=1)
would validate the whole branch and the ρ-readout independently.

## 9. What this means for the Einstein-gap problem

Theorem E is a realization/existence result on the Einstein side of the single blow-up problem:
the blown-up ball carries complete ACH Einstein metrics, but the ones found have non-standard CR
infinity, so they cannot be glued into a ball quotient as exact-collar cells. The complete-cell
infima p_{1,0}, 𝔓_{k,ℓ} concern defect cells with *standard* CH collar; Step 14/15 showed the
certified cheap cells pay in a Burns core and do not shadow this branch. The branch is therefore
relevant as (a) the possible P→0 compactness endpoint in the diagonal class — a sequence of
diagonal standard-collar cells with P → 0 would have to converge to an Einstein filling with
ρ = 1 or degenerate — and (b) an exact example in the existence/realization axis. Diagonal
nonexistence at ρ = 1 requires the whole branch (both ends) plus completeness of the stratum
enumeration; it remains open.



---

## Source step19_theorem_package_and_selection_lemma.md

Original: [sources/Sessions/S1003A02/workspace/notes/step19_theorem_package_and_selection_lemma.md](../sources/Sessions/S1003A02/workspace/notes/step19_theorem_package_and_selection_lemma.md)

# Step 19 — theorem package, independent reading of Theorem E, and the supercritical selection lemma

## 1. Consolidated mathematical package

The dependence-ordered research package is now

`workspace/notes/theorem_package_v1.md`.

It separates the direct defect, trace-free Ricci energy, and alignment functionals; records the actual-field bulk theorems; separates zero infimum from attainment; states the signed marked-cell response at its proved scope; retains the general Burns transgression and the full logarithmic remainder as open; records both certified cells and the improved balanced upper coefficient; distinguishes construction-level cell subadditivity from the unrestricted closed-manifold infimum; and includes Theorem E with its exact bolt geometry. The package is a research map, not a manuscript or a completion statement.

The common mechanism that survives this separation is:

1. an actual metric-wise field and its differential identities control the regular bulk;
2. a topology change is realized by a complete marked cell whose cost responds to the ambient self-dual curvature;
3. first-order-free directions can use a negative quadratic interaction, while handles retain a different exact cost;
4. exact Einstein filling may require changing the boundary CR structure;
5. the unrestricted \(\alpha\)-problem still needs a passage from global near-minimizers to regular bulk plus marked cells or collapse.

The first-order law for arbitrary bulk, the error-controlled \(-9\) kernel law, \(p_{1,0}>0\), equality of global and cell asymptotics, and standard-CR diagonal nonexistence remain open in the same package.

## 2. Independent mathematical reading of Theorem E

The proof in `workspace/notes/step15_ach_projected_theory.md` and its source artifacts were read as one argument rather than as unrelated computations.

### 2.1 Regular bolt

With \(s=t^2\), \(a_1=A(s)\), \(a_2=B(s)\), and \(a_3=tC(s)\), `workspace/scripts/ach_bolt_fuchs.py` verifies algebraically that its three Fuchsian equations are equivalent to the diagonal Einstein equations. For
\[
(\sigma,\delta,\gamma)=((A+B)/2-b,A-B,C-1),
\]
the linear part is
\[
(4D^2,\ 4D^2-16,\ 4D^2+2D),\qquad D=s\partial_s.
\]
The only positive-integer resonance is the \(s^2\) coefficient of \(\delta\), which is the free bolt parameter \(d\). The remainder starts at order \(s^7\), so it does not change this coefficient. The radial inverses on functions vanishing to order seven have the displayed factors \(1/(4m^2)\), \(1/[4(m-2)(m+2)]\), and \(1/[2m(2m+1)]\), together with their \(D\)-bounds.

The complex-disc enclosure covers \(|s|\le10^{-4}\) and gives a self-map with Lipschitz factor \(0.03251\). Hence the fixed point is holomorphic in \(s\), not merely a solution on the positive real axis. The parity conditions \(A,B,C\) analytic in \(s\), \(C(0)=1\), and \(A-B=O(s^2)=O(t^4)\) are exactly the regular \(\mathcal O(-1)\) bolt conditions in this normalization. Constraint propagation has \(\mathcal C'=-2S\mathcal C\); since \(S\sim t^{-1}\) and the regular series has \(t^2\mathcal C\to0\), the constraint vanishes identically.

There is one minor interval-implementation point to repair for a completely literal rerun: the residual and Jacobian suprema at lines 204 and 227 are converted from Arb upper endpoints to ordinary binary64 without applying `nextafter` toward \(+\infty\). The recorded self-map has roughly a factor-two margin and the contraction factor is only \(0.03251\), so multiplying all such stored suprema by \(1+10^{-12}\) is far inside the proved inequalities and absorbs binary64 rounding. The argument is unchanged, but the script should use directed outward conversion and be rerun before this computation is exported as a standalone certificate.

### 2.2 Validated passage and staying orbit

`workspace/scripts/ach_capd_field_check.py` parses the vector field directly from `ach_bolt_capd.cpp`; its symbolic difference from the exact anisotropy-resolving Einstein field is zero in all seven components. The corrected mean-potential cancellation is therefore present in the code actually transported. The Fuchsian boxes are converted to outward binary64 endpoints, and CAPD transports a tiled parameter interval to \(T=2.75\).

The block computation verifies that the stable faces are inward, both unstable faces are outward, \(\zeta\) decreases, and a staying orbit cannot reach a \(q\)-face because the total future drift is smaller than its recorded distance from those faces. The first and last parameter boxes lie in opposite unstable slabs. Continuity of the bolt family and the exit map therefore gives a parameter whose orbit stays in the block for all future time. This is the required Ważewski argument; the construction does not infer existence from a floating root.

Inside the block, \(\zeta'\le-1.99846\zeta\), all nonneutral coordinates are \(O(\zeta)\), and
\[
\widetilde\Phi=q+(y_g-y_h)/4-\zeta\sinh q,
\qquad |\widetilde\Phi'|\le19.5826\zeta^2.
\]
Thus the radial time extends to infinity, the metric is complete, its curvature approaches the ACH equilibrium, and the integrated drift gives
\[
\rho_\infty\in[2.1901328141,2.1924133695].
\]
[Corrected in Step 20 after peer message 771.] The repaired exact bolt Weyl blocks are diag(−41/16,−41/16,41/8) and diag(−91/16,−91/16,91/8), with squared norms 5043/128 and 24843/128; the earlier three-distinct-eigenvalue values came from a symbol collision. Both blocks are nonzero, so the metric is neither half-conformally-flat. Non-Kählerness follows because a Kähler metric with s=−24 must have Kähler-side Weyl spectrum exactly (−4,2,2), with norm 24, and neither block has this spectrum in either orientation. See theorem_package_v1.md §6.2.

The Biquard--Herzlich curvature integral was not computed in this Step. It is an optional independent branch validation and should first return the CR \(\nu\)-invariant from the convergent combined density; conversion to the Burns--Epstein invariant needs its additive contact normalization.

## 3. Supercritical selection: the valid lemma

Work on one closed negative-Yamabe four-manifold in the scalar-normalized class
\[
\mathcal S_{-4}=\{g\in C^\infty:\ s_g=-4\}.
\]
Set
\[
p=\inf_{\mathcal S_{-4}}P,
\qquad R_1(g)=\int|\nabla\operatorname{Rm}_g|^2\,d\mu_g.
\]
Let \(\delta>0\), choose smooth \(g_0\in\mathcal S_{-4}\) with \(P(g_0)\le p+\delta\), and suppose \(0<R_1(g_0)<\infty\). Put \(\varepsilon=\delta/R_1(g_0)\). If a smooth \(g\in\mathcal S_{-4}\) satisfies
\[
P(g)+\varepsilon R_1(g)
\le \inf_{\mathcal S_{-4}}(P+\varepsilon R_1)+\delta,
\]
then
\[
P(g)+\varepsilon R_1(g)
\le P(g_0)+\varepsilon R_1(g_0)+\delta
\le p+3\delta.
\]
Consequently
\[
0\le P(g)-p\le3\delta,
\qquad R_1(g)\le3R_1(g_0).
\]
No attained minimum, gauge choice, or Euler equation is needed: a smooth approximate minimizer exists by the definition of the infimum. The scalar normalization is essential because \(P\) is scale invariant while \(R_1(c^2g)=c^{-2}R_1(g)\). If \(R_1(g_0)=0\), the comparison metric has parallel curvature and should be treated separately rather than defining \(\varepsilon\) by division.

A smooth exact-collar cell has finite \(R_1\). The certified profiles are initially matched through the second jet; multiplying their third-order collar deviation by a flat cutoff produces a smooth exact-collar metric with finite \(R_1\) and arbitrarily small change of the quadratic curvature cost. A smooth closed gluing and its smooth scalar-minus-four Yamabe representative also have finite \(R_1\).

## 4. Why the lemma does not yet remove concentration

The energy comparison is correct, but the stronger compactness conclusion proposed for it does not follow.

### 4.1 The comparison depends on \(\delta\)

For each \(\delta\), define the regularity profile
\[
\mathcal R_*(\delta)=
\inf\{R_1(g):g\in\mathcal S_{-4},\ P(g)\le p+\delta\}.
\]
The lemma gives a selected metric with \(R_1\le3R_1(g_0)\), and optimizing the comparison gives essentially \(R_1\lesssim\mathcal R_*(\delta)\). It gives a uniform derivative bound as \(\delta\downarrow0\) only if
\[
\sup_{0<\delta<\delta_0}\mathcal R_*(\delta)<\infty.
\]
That is new geometric information, not a consequence of the comparison. A certified construction cannot be substituted for \(g_0\) at arbitrarily small \(\delta\) unless it is already known to lie within \(\delta\) of the unknown infimum. Choosing an arbitrary smooth \(\delta\)-near-minimizer supplies finite \(R_1(g_0)\), but that number may diverge arbitrarily fast as \(\delta\to0\).

This dependence is particularly important for the balanced family. Fixed-size smooth blow-up cells have finite derivative energy per cell before scalar normalization, but the sharp handle value is approached by shrinking cores, and neither the handle scales nor the derivatives introduced by the global Yamabe replacement have yet been bounded uniformly. Even a total estimate \(R_1=O(A_j)\) would allow one concentration scale as small as \(A_j^{-1/2}\), because a fixed-profile bubble at scale \(r\) has derivative-curvature cost of order \(r^{-2}\). An extensive total bound does not give local equiintegrability.

### 4.2 Intrinsic derivative energy is not a uniform Sobolev estimate

For a fixed metric with Sobolev constant \(C_S(g)\),
\[
\|\operatorname{Rm}\|_4^2
\le C_S(g)\bigl(\|\nabla\operatorname{Rm}\|_2^2+	ext{lower-order term}\bigr).
\]
A uniform conclusion therefore needs a uniform local Sobolev or harmonic-radius input. The intrinsic bound on \(\int|\nabla\operatorname{Rm}|^2\) does not itself provide that input. Global volume noncollapse alone, with only \(s=-4\) and an \(L^2\) trace-free Ricci bound, does not give uniform volume ratios, Ricci bounds, or harmonic coordinates.

The retrieved regularity literature reinforces this distinction. Anderson--Bando--Kasue--Nakajima compactness applies to Einstein metrics with diameter, volume, and \(L^2\)-curvature control; the Ricci-flow regularity results require a flow equation and scalar/Ricci hypotheses. These equations are precisely what the selected metrics do not yet possess uniformly. Thus the statement “curvature is bounded in \(W^{1,2}\), hence in \(L^4\), hence harmonic-coordinate compactness” is valid only after a uniform Sobolev/harmonic-radius structure has been supplied.

### 4.3 Correct mathematical consequence

The elementary lemma converts any *already uniformly regular* family of comparisons approaching \(p\) into a uniformly regular selected near-minimizing family. It does not create such comparisons. Conditional on

- \(\sup_jR_1(g_{0,j})<\infty\) (or a suitable locally equiintegrable analogue),
- uniform local Sobolev/volume-radius control on the noncollapsed region,
- the corresponding harmonic-coordinate theorem,

the supercritical bound can exclude fixed-energy bubbles whose scales tend to zero in that region. Collapse and topology accounting would still require separate arguments.

## 5. Revised compactness front

The useful next object is the regularity profile \(\mathcal R_*(\delta)\), not merely the penalized functional. There are three possible advances:

1. prove a uniform or quantitatively controlled upper bound for \(\mathcal R_*(\delta)\) from a new construction that approaches the true infimum, rather than only the known upper construction;
2. derive from an approximate Euler equation for \(P+\varepsilon R_1\) a local Sobolev/harmonic-radius estimate whose constants depend on the controlled combination \(\varepsilon R_1\) in a way that survives \(\varepsilon\to0\);
3. formulate a local regularizer or concentration function whose comparison bound is equiintegrable, not merely extensive.

Any of these would connect the lemma to the desired bulk/cell decomposition. Without one of them, Anderson's existing ideal-minimizer theorem remains stronger on fixed topology, while the family-uniform, marked-cell and actual-field passage stays open. The matrix-valued Burns transgression remains the complementary local theorem of broad reach.



---

## Source step20_burns_response_and_neck_quantization.md

Original: [sources/Sessions/S1003A02/workspace/notes/step20_burns_response_and_neck_quantization.md](../sources/Sessions/S1003A02/workspace/notes/step20_burns_response_and_neck_quantization.md)

# Step 20 — Burns first-order response theorem, neck quantization, and exact-cell rigidity

Session S1003A02, Agent2. Conventions: curvature operator \(\mathcal R:\Lambda^2\to\Lambda^2\) with
\(\langle\mathcal R(e_1\wedge e_2),e_1\wedge e_2\rangle=\sec(e_1,e_2)\); \(\mathbf R^+=P_+\mathcal RP_+=W^++\frac s{12}I\)
on \(\Lambda^+\); norms are endomorphism norms (so \(|W^+|^2=24\), \(s^2/24=24\) on \(\mathbb{CH}^2\) with \(s=-24\));
\(8\pi^2\chi=\int(|W|^2-\tfrac12|\mathrm{Ric}^\circ|^2+\tfrac{s^2}{24})\), \(12\pi^2\tau=\int(|W^+|^2-|W^-|^2)\) on closed manifolds;
\(P=\int|\mathrm{Ric}^\circ|^2\). Script and exact output:
`workspace/scripts/burns_transgression_flux.py`, `workspace/data/burns_transgression_flux.json`.

---

## 1. Theorem F (first-order Burns response; general bulk)

**Burns metric in the session normalization.** On \(\mathbb C^2\setminus0\) with standard \(J\), Kähler form
\(\omega=dx_1\wedge dx_2+dx_3\wedge dx_4\in\Lambda^+\), the Kähler potential \(|z|^2+x_0\log|z|^2\) gives *exactly*
\[
B_{x_0}=\delta+x_0h,\qquad h_{ij}=\frac1{t^2}\Big(\delta_{ij}-\frac{x_ix_j}{t^2}-\frac{(Jx)_i(Jx)_j}{t^2}\Big),
\]
i.e. \(dt^2+(t^2+x_0)(\sigma_1^2+\sigma_2^2)+t^2\sigma_3^2\): the session profile \(a_1=a_2=\sqrt{t^2+x_0},a_3=t\), whose
exceptional curve has area \(\pi x_0\). Since \(B_{x_0}\) is affine in \(x_0\) and \(W^+(B_{x_0})=s(B_{x_0})=0\) for all
\(x_0\), the tail satisfies **pointwise** \(P_+\mathcal R^{\rm lin}(h)P_+=0\) on \(t>0\) (verified exactly).

**Exact transgression (computed).** For any cutoff \(\chi\) (1 near 0, 0 near \(r_0\)), the integral over the cut
annulus \(\Phi^{\pm\pm}=-\int P_\pm\mathcal R^{\rm lin}(\chi h)P_\pm\,dx\) is the inner-sphere flux and is independent of
\(\chi,r_0\). Exact monomial integration on \(S^3\) gives, in the orthonormal bases with \(w_1=\omega/\sqrt2\),
\[
\Phi^{++}=\pi^2\,w_1w_1^{T},\qquad \Phi^{--}=\tfrac{\pi^2}{3}I,\qquad \Phi^{+-}=0 .
\]
The sign convention was checked on the normal-coordinate jet of constant curvature \(K\) (\(R_{1212}=K\),
\(\mathbf R^\pm=KI\)). Hence the scalar flux is \(F_s=-\int s^{\rm lin}(\chi h)=4\operatorname{tr}\Phi^{++}=4\pi^2\).

**Theorem F.** Let \((M,g)\) be a closed oriented Riemannian 4-manifold, \(p\in M\), \(\zeta\in\Lambda^+_p\) a unit
self-dual form, and let \(\hat g_{x_0}\) on \(\hat M=M\#\overline{\mathbb{CP}}^2\) be obtained in \(g\)-normal coordinates at \(p\),
with a frame identifying \(\zeta\) with \(w_1\), by
\(\hat g_{x_0}=\pi^*g+x_0\chi(r/r_0)h\), \(r_0=x_0^{1/5}\). Then
\[
\boxed{\;P(\hat g_{x_0})=P(g)+8\pi^2\big(1-x_0\,\mathbf R^+_p(\zeta,\zeta)\big)+O(x_0^{6/5})\;}
\]
with the constant depending on \(\|g\|_{C^3}\) near \(p\). If \(g\) is Einstein, \(\operatorname{Ric}=\lambda g\), the same holds for
\(J(\hat g)=\int|\operatorname{Ric}-\lambda\hat g|^2\).

**Proof.** (i) *Topological reduction.* \(\chi(\hat M)=\chi(M)+1\), \(\tau(\hat M)=\tau(M)-1\) and the two Chern–Weil
identities give the exact identity \(P(\hat g)-P(g)-8\pi^2=4\Delta W^++\Delta S/12\), where
\(\Delta W^+=\int|W^+|^2\) of \(\hat g\) minus that of \(g\), and \(\Delta S\) likewise for \(\int s^2\); the metrics agree outside
\(B_{r_0}\).

(ii) *Inner region \(r\le r_0/2\)* (two sub-regions; repaired after the Step-20 TTCS verification). Here
\(\hat g=B_{x_0}+k\), \(k=g-\delta=O(r^2)\), \(\partial k=O(r)\), \(\partial^2k=O(1)\).
*Core \(r\le\sqrt{x_0}\):* rescale \(y=x/\sqrt{x_0}\), \(x_0^{-1}\hat g=B_1+K\), \(K=O(x_0|y|^2)\) in \(C^2\); \(B_1\) has bounded
geometry near the exceptional curve, so \(|W^+(\hat g)|+|s(\hat g)|\le C\) in original units, while
\(dV_{\hat g}\le C(r^3+x_0r)\,dr\,d\Omega\) (note \(\sqrt{\det B_{x_0}}=1+x_0/r^2\), so the volume form is *not* within
\(O(1)dx\) of flat there). Core contributions: \(O(\int_0^{\sqrt{x_0}}(r^3+x_0r)dr)=O(x_0^2)\).
*Intermediate \(\sqrt{x_0}\le r\le r_0/2\):* the mixed finite difference
\(F(B_{x_0}+k)-F(\delta+k)-F(B_{x_0})+F(\delta)\), \(F\in\{W^+,s\}\), has vanishing pure terms
(\(F(B_{x_0})=F(\delta)=0\)), and every remaining term carries a Burns-tail factor and a bulk-jet factor, giving
\(|F(\hat g)-F(g)|\le Cx_0/r^2\); the relative volume correction is also \(O(x_0/r^2)\). The energy-density difference is
\(O(x_0/r^2+x_0^2/r^4)dx\), integrating to \(O(x_0r_0^2+x_0^2\log(1/x_0))\). No first-order term arises in the inner
region: the linearized self-dual curvature and scalar curvature of the tail vanish pointwise.

(iii) *Cut annulus \(r_0/2\le r\le r_0\).* Here \(\hat g=g+x_0\chi h\), \(|\partial^j(x_0\chi h)|\le Cx_0r_0^{-2-j}\).
Expanding,
\(|W^+(\hat g)|^2dV_{\hat g}-|W^+(g)|^2dV_g=2\langle W^+(g),x_0P_+\mathcal R^{\rm lin}_\delta(\chi h)P_+\rangle_0dx+E\),
with \(|E|\le C(x_0r_0^{-2}+x_0^2r_0^{-8})\) (curvature-dependent part of the linearization, projector and volume
variation, quadratic terms). Since \(W^+(g)=W^+_p+O(r_0)\) in the normal frame,
\[
\Delta W^+_{\rm cut}=-2x_0\langle W^+_p,\Phi^{++}_0\rangle+O(x_0r_0+x_0r_0^2+x_0^2r_0^{-4}),\quad
\Delta S_{\rm cut}=-2x_0s_pF_s+O(\cdots).
\]
(iv) *Assembly.* \(4\Delta W^++\Delta S/12=-8x_0\langle W^+_p,\Phi_0^{++}\rangle-\tfrac{2}{3}x_0s_p\operatorname{tr}\Phi^{++}
=-8x_0\langle\mathbf R^+_p,\Phi^{++}\rangle=-8\pi^2x_0\mathbf R^+_p(\zeta,\zeta)\), plus errors
\(O(x_0r_0+x_0^2r_0^{-4}+x_0^2\log(1/x_0))=O(x_0^{6/5})\) for \(r_0=x_0^{1/5}\). For Einstein \(g\),
\(J(\hat g)-P(\hat g)=\frac14\int(s_{\hat g}-4\lambda)^2dV_{\hat g}\). The core bound (\(|s|\le C\) on volume \(O(x_0^2)\)), the
intermediate bound \(|s_{\hat g}-4\lambda|\le Cx_0/r^2\) and the annulus bound \(Cx_0r_0^{-4}\) make this
\(O(x_0^2\log(1/x_0)+x_0^2r_0^{-4})=O(x_0^{6/5})\). \(\square\)

The proof was checked independently (`trace/ttcs/results/step20_ttcs01_verifier1_integration.md`). That check
confirmed the flux matrices, the curvature sign, the \(\tfrac14\) two-form pairing and the orientation. It also gave an
independent scalar check: \(n_i(\partial_jh_{ij}-\partial_i\operatorname{tr}h)=2/r^3\), hence \(F_s=4\pi^2\). The two
denominator `assert`s in the script are vacuous (they always test \(0=0\)). The denominators are in fact constants
times powers of \(t^2\), so the output is unaffected.

**Checks.** (a) Kähler topology: the scalar flux says \(\int s\,dV\) drops by \(4\pi^2x_0=4\pi\cdot\mathrm{area}(E)\),
exactly the Kähler identity \(\int s\,dV=4\pi c_1\cdot[\omega]\) with \(c_1(\hat M)\cdot[\hat\omega]=c_1\cdot[\omega]-\mathrm{area}(E)\).
(b) Complex space forms: \(\mathbf R^+=\operatorname{diag}(s/4,0,0)\) in the Kähler frame; for \(\mathbb{CH}^2\) (\(s=-24\))
the aligned slope is \(+6\), the perpendicular slope \(0\), and for Fubini–Study \(-6\): this reproduces the exact Kähler
seed \(1+6\kappa x_0+\dots\) and the numerical slopes \(5.90\), \(0.044\) (near-perpendicular), \(-5.9\) of Steps 8–9.
(c) \(\Phi^{+-}=0\): trace-free Ricci of the bulk does not enter at first order, as \(U(2)\)-representation theory requires
(the only \(U(2)\)-invariant linear functionals of the curvature are \(s\) and \(W^+(\zeta,\zeta)\)).

**Status change.** The Step-8/9 "Burns transgression" conjecture \(\int T_{\mathbf R^+}(H_\zeta)=-\pi^2\zeta\otimes\zeta\)
is now a theorem with its normalization fixed (\(x_0\) = area/\(\pi\) of the exceptional curve), orientation fixed
(\(\zeta\in\Lambda^+\), summand \(\overline{\mathbb{CP}}^2\)), and an explicit \(O(x_0^{6/5})\) remainder. It is an upper-bound
(construction) statement; it says nothing yet about the infimum's first-order coefficient from below.

### Consequences
1. **Strict blow-up saving criterion.** If \(g\) attains \(\inf_MP\) (e.g. \(g\) Einstein) and
   \(\lambda_{\max}(\mathbf R^+_p)>0\) at some \(p\), then \(\inf_{M\#\overline{\mathbb{CP}}^2}P<\inf_MP+8\pi^2\). Since
   \(\operatorname{tr}\mathbf R^+=s/4\), this holds wherever \(s>0\), and for \(s<0\) Einstein metrics wherever an eigenvalue
   of \(W^+\) exceeds \(|s|/12\).
2. **Three bulk regimes for Einstein \(s<0\).** Real hyperbolic: \(\mathbf R^+=\frac s{12}I<0\), every direction costs at
   first order (prediction: blow-up cells over hyperbolic bulk are first-order rigid, cost \(\ge8\pi^2\) to first order, the
   handle-like regime). Kähler–Einstein: eigenvalues \((s/4,0,0)\), a 2-sphere of kernel directions
   \(\omega^\perp=\ker\mathbf R^+\), which are exactly Ozuch's first-obstruction-free directions \(\mathbf R^+\zeta=0\); the
   cost below \(8\pi^2\) then comes from second order (the \(-9x_0^2\log\) neck mechanism, Step 10, and the certified
   cells). Einstein metrics with \(W^+\) eigenvalue \(>|s|/12\): first-order saving.
3. The same tensor \(\mathbf R^+_p\) is the linear obstruction to Einstein desingularization (Ozuch, \(A_1\)) and the
   linear cost of the defect cell. Theorem F is the defect-side half of this correspondence for a general bulk.

---

## 2. Neck quantization of blow-up concentration

**Lemma Q (bubble form).** Let \((N,h)\) be complete, oriented, scalar-flat, ALE with one end \(S^3/\Gamma\)
(order \(>0\), so the Gauss–Bonnet boundary term tends to \(8\pi^2/|\Gamma|\) and the signature boundary term to
\(\eta(S^3/\Gamma)\)). Then
\[
P(N)=2\!\int|W|^2-16\pi^2\Big(\chi(N)-\frac1{|\Gamma|}\Big)\ \ge\ 8\pi^2\Big[3|\tau(N)+\eta|-2\chi(N)+\frac2{|\Gamma|}\Big].
\]
For \(\Gamma=1\): \(N\simeq\) blow-ups/handles of \(\mathbb R^4\) with \(\chi=1+k-2\ell\), \(\tau=-k\) gives
\(P(N)\ge8\pi^2(k+4\ell)=8\pi^2Q\). Equality for one blow-up iff \(W^+=0\) (Burns attains it: \(P=8\pi^2\)).

**Lemma Q′ (neck form, no completeness).** Let \(g\) be any metric on a cell \(U_0\cong D\#\overline{\mathbb{CP}}^2\) and
\(\Sigma\subset U_0\) an embedded 3-sphere bounding an inner region \(U\) with \(\tau(U)=-1\). Suppose a collar of
\(\Sigma\), rescaled by its radius, is orientation-preservingly \(\varepsilon\)-close in \(C^2\) to the Euclidean annulus
\(\{1\le|x|\le2\}\) with \(U\) on the ball side. Here \(\varepsilon\)-closeness is taken in the sense that the Gauss–Bonnet and
signature boundary transgressions are within \(C\varepsilon\) of the flat values; this follows, for example, by
interpolating to an exactly flat annulus inside the collar. Then \(P(g;U)\ge8\pi^2-C\varepsilon\). *Proof.* Mayer–Vietoris gives \(b_1(U)=0\), \(b_2(U)=1\), so
\(\chi(U)\le2\). Gauss–Bonnet and signature with boundary: the boundary terms are within \(C\varepsilon\) of those of a
flat ball (\(8\pi^2\) and \(0\)). Thus \(P(U)=2\int_U|W|^2+\frac1{12}\int_Us^2-16\pi^2\chi(U)+16\pi^2+O(\varepsilon)\ge
24\pi^2-16\pi^2-C\varepsilon\). \(\square\) The scalar term only helps, so no normalization of \(s\) is needed.

**Consequence for \(p_{1,0}\).** By the certified cell (\(x_0=3/100,X=64\)), \(\mathfrak P_{1,0}\le0.99584841\cdot8\pi^2\).
Hence along any sequence with \(P\to\mathfrak P_{1,0}\), for every \(\varepsilon<0.0041\cdot8\pi^2/C\), **no** sphere
enclosing the exceptional class has an \(\varepsilon\)-Euclidean neck. Concentration of the \((-1)\)-class into an
almost-flat bubble is energetically excluded. Handles are the opposite: their bubble bound \(32\pi^2\ell\) equals the
cell infimum, so concentration is allowed, and it is how the handle infimum is approached.

---

## 3. No exact Einstein cells (proportionality rigidity)

**Lemma R.** Let \(U\) be a compact connected cell with exact \(\mathbb{CH}^2\)-collar (\(\operatorname{Ric}=-6g\) there) and
topology change \((\Delta\chi,\Delta\tau)\) relative to the ball with \(\Delta\chi\ne3\Delta\tau\). Then \(U\) carries no
Einstein metric extending the collar; in particular \(P(U)>0\) for every such cell.
*Proof.* An Einstein metric is real-analytic in harmonic coordinates. \(\nabla\mathrm{Rm}=0\) and the \(\mathbb{CH}^2\)
curvature type hold on the collar, hence on all of \(U\). The Gauss–Bonnet and signature densities are then the
\(\mathbb{CH}^2\) constants, \(6/\pi^2\) and \(2/\pi^2\), and the boundary terms coincide with those of the ball.
So \(\Delta\chi=\frac6{\pi^2}\Delta V\) and \(\Delta\tau=\frac2{\pi^2}\Delta V\), i.e. \(\Delta\chi=3\Delta\tau\).
For \(k\) blow-ups and \(\ell\) handles \((\Delta\chi,\Delta\tau)=(k-2\ell,-k)\), and proportionality holds iff \(\ell=2k\). So
every cell with \(\ell\ne2k\) is excluded, in particular all pure blow-up and pure handle cells. \(\square\)
"Exact collar" means equality with the full normalized \(\mathbb{CH}^2\) metric, preserving the complex orientation. The
family \(\ell=2k\) needs a separate rigidity argument for locally complex-hyperbolic fillings of a geodesic sphere
(developing map plus convexity); that argument is not supplied here.

**Consequence (for \(\ell\ne2k\)).** \(\mathfrak P_{k,\ell}=0\) can occur only through degeneration of minimizing sequences:
collar radius \(X\to\infty\) (the limit is a complete ACH-type filling; if Einstein, it is a standard-CR counterpart of
Theorem E), collapse, or concentration through *curved* necks (almost-flat necks are excluded by Lemma Q′).
Positivity of \(p_{1,0}\) is thus reduced to a compactness statement with three named alternatives.

---

## 4. Handles: what is and is not proved about softness

The handle infimum \(32\pi^2\ell\) is approached by shrinking cores and not attained (peer, Step 11). A fixed core
profile at scale \(r\) has \(\int|\nabla\mathrm{Rm}|^2\sim r^{-2}\). The statement "\(R^*(\delta)\to\infty\) for pure-handle
cells" follows **if** bounded \(\int|\nabla\mathrm{Rm}|^2\), \(s=-24\) and a lower injectivity-radius bound imply \(W^{2,4}\)
subconvergence. That follows from Anderson's harmonic-radius theorem for \(\|\mathrm{Rm}\|_{L^p}\), \(p>2\), with
injectivity radius bounded below; Sobolev embedding gives \(L^4\) curvature on harmonic balls. The limit would
attain \(32\pi^2\ell\) in \(W^{2,4}\), contradicting non-attainment provided the equality analysis holds in that
regularity. So: along every handle-minimizing sequence, either \(R_1\to\infty\) or the injectivity radius
\(\to0\). The unconditional version needs a collapse exclusion near the core.

---

## 5. Repairs and open edges
- `ach_bolt_fuchs.py`: Arb-to-binary64 suprema are now rounded outward (`up()`: nextafter plus \(10^{-12}\) relative
  inflation), and the self-map and contraction inequalities are re-verified in Arb with exact rational inverse factors
  (rerun recorded as `fuchs_boxes_N6{,_complex}_v2.json`). Rerun result: complex-disc Lipschitz factor
  0.0325075, real 0.0112241, self-map verified in Arb; the 40 emitted binary64 initial boxes are bit-identical to the
  Step-17 boxes, so the Ważewski transport and the \(\rho_\infty\) enclosure stand unchanged.
- Peer correction (message 771): exact bolt Weyl blocks are diag(−41/16,−41/16,41/8), diag(−91/16,−91/16,91/8);
  non-Kählerness now rests on the Kähler-side spectrum \((-4,2,2)\) being violated (theorem package §6.2).
- Theorem F is an upper-bound theorem. The matching lower statement, that every cell of Burns parameter \(x_0\)
  pays at least \(8\pi^2(1-x_0\lambda_{\max}(\mathbf R^+))+o(x_0)\), needs a cell compactness/stability theory at
  scale \(\sqrt{x_0}\). Lemma Q′ supplies its zeroth-order part under an almost-flat neck.
- Hyperbolic-bulk prediction: \(\mathfrak P^{\mathbb H^4}_{1,0}=8\pi^2\), approached and not attained. This is a
  testable dichotomy against the CH case, and the cleanest place to look for a sharp single-cell lower bound.



---

## Source step21_entropy_hyperbolic_cells_and_offbolt_weyl.md

Original: [sources/Sessions/S1003A02/workspace/notes/step21_entropy_hyperbolic_cells_and_offbolt_weyl.md](../sources/Sessions/S1003A02/workspace/notes/step21_entropy_hyperbolic_cells_and_offbolt_weyl.md)

# Step 21 — Entropy supplier, real-hyperbolic cells, exact-collar rigidity, and off-bolt Weyl spectra

Conventions: curvature operator norms and Chern–Weil formulas are those of `theorem_package_v1.md`. For the real-hyperbolic calculations the exact normalization is
\[
K=-2,\qquad \operatorname{Ric}=-6g,\qquad s=-24.
\]
Thus all cell costs below are divided by \(8\pi^2\). The corresponding scalar-\(-12\), sectional-curvature-\(-1\) formulas follow by scale invariance.

## 1. Exact-collar Einstein rigidity has no exceptional topology

Step 20 proved by analytic continuation and Hirzebruch proportionality that an Einstein metric agreeing with \(\mathbb{CH}^2\) on a collar is locally complex hyperbolic throughout. The temporary topological calculation only excluded \(\ell\ne2k\). The locally symmetric continuation actually closes every case.

**Lemma R (closed form).** Let \(U\) be a connected smooth marked cell with an exact \(\mathbb{CH}^2\) collar. If an Einstein metric on \(U\) extends that collar, then \(U\) is the standard complex-hyperbolic ball cell. Hence its marked topology is trivial: \(k=\ell=0\).

**Proof.** Einstein metrics are real analytic in harmonic coordinates. The tensor \(\nabla\mathrm{Rm}\) vanishes and the complex-hyperbolic curvature tensor holds on the collar, hence on all of connected \(U\). The universal cover \(\widetilde U\) develops by a local isometry into \(\mathbb{CH}^2\). The collar \(S^3\times(a,b)\) is simply connected, so its preimage is a disjoint union of isometric collar copies. On each copy, the developing map agrees with the inclusion of a geodesic-sphere collar after a global isometry of \(\mathbb{CH}^2\); analyticity/local-symmetry continuation extends this to the connected component of the ball complement. Any two ball complements in \(\mathbb{CH}^2\) intersect, so there can be only one such lift. The deck group therefore preserves that lift. Because it covers the simply connected collar and acts freely, the deck group is trivial. The developing map is the standard ball filling, and no marked blow-up or handle topology remains. \(\square\)

The upshot is stronger than the previous \(\ell\ne2k\) statement: every exact-collar cell with \((k,\ell)\ne(0,0)\) has positive defect at each fixed smooth metric. A zero infimum, if it occurs, must arise through degeneration: the collar recedes to a complete ACH limit, collapse occurs, or topology concentrates through a non-Euclidean neck. Lemma Q' already excludes an almost-Euclidean neck for a blow-up minimizing below \(8\pi^2\).

## 2. Volume entropy is a new field-free supplier

The actual source `Knowledge/objects/papers/ENTROPIES-VOLUMES-AND-EINSTEIN-METRICS--0ee1eb110f9d--94203f883336/object.md` states Kotschick's entropy-strengthened Einstein inequality
\[
\chi(X)\ge \frac32|\sigma(X)|+\frac{\lambda(X)^4}{108\pi^2},
\]
and Corollary 3 (Sambusetti/BCG): if a closed Einstein four-manifold \(X\) maps with nonzero degree \(d\) to a closed real-hyperbolic four-manifold \(Y\), then
\[
\chi(X)\ge \frac32|\sigma(X)|+|d|\chi(Y),
\]
with equality only when \(X\) is real hyperbolic. The proof uses Besson--Courtois--Gallot entropy, Bishop comparison after Einstein normalization, and exact rigidity; it does not use monopoles.

For
\[
X=Y\#k\overline{\mathbb{CP}}^{\,2}
\]
the pinch map has degree one, \(\sigma(Y)=0\), and
\[
\chi(X)=\chi(Y)+k,\qquad \sigma(X)=-k.
\]
The Einstein inequality would require \(k\ge3k/2\), impossible for every \(k\ge1\). Therefore:

**Theorem H (entropy-supplied Einstein nonexistence).** Every blow-up \(Y\#k\overline{\mathbb{CP}}^{\,2}\), \(k\ge1\), of a closed oriented real-hyperbolic four-manifold admits no Einstein metric.

This extends the supplier portfolio beyond gauge fields: the supplier is the homological minimal-volume entropy, unchanged by simply connected blow-up summands. It establishes exact nonexistence but not a positive \(L^2\) Einstein gap for the low-blow-up range. The entropy proof uses a pointwise Einstein/Ricci normalization before Bishop comparison. Small critical \(L^2\) trace-free Ricci does not provide that pointwise hypothesis. This is the same critical-exponent obstruction encountered in field transport and compactness, now in entropy form.

The Yamabe-invariant search did not find a theorem proving
\[
Y(Y\#k\overline{\mathbb{CP}}^{\,2})=Y(Y)
\]
for a closed real-hyperbolic four-manifold. The Kotschick source contains no Yamabe computation. Hence the constant-scalar lower theorem below remains conditional on the scalar-energy/volume input; it is not promoted to an unconditional gap theorem.

For reference, raw Chern–Weil gives only
\[
P(g)\ge \frac1{24}\int s_g^2+4\pi^2k-8\pi^2\chi(Y),
\]
and therefore the unconditional Hitchin--Thorpe-scale positivity \(P\ge4\pi^2(k-2\chi(Y))\) only when \(k>2\chi(Y)\).

## 3. Same-metric real-hyperbolic cell identities

Let \(U\cong D\#\overline{\mathbb{CP}}^{\,2}\) agree to the necessary collar jet with the real-hyperbolic ball \(B\), in the orientation where the exceptional class has square \(-1\). Relative Chern–Weil gives
\[
\frac{P(U)}{8\pi^2}-1
=4\frac{\int_U|W^+|^2}{8\pi^2}
+\frac{\int_U s^2/12-48\operatorname{Vol}(B)}{8\pi^2}. \tag{3.1}
\]
For
\[
J= P+\frac14\int_U(s+24)^2,
\]
the pointwise identity
\[
\frac{s^2}{12}+\frac{(s+24)^2}{4}=\frac{(s+18)^2}{3}+36
\]
gives
\[
\frac{J(U)}{8\pi^2}-1
=4\frac{\int_U|W^+|^2}{8\pi^2}
+\frac{\int_U(s+18)^2/3}{8\pi^2}
+\frac{36\operatorname{Vol}(U)-48\operatorname{Vol}(B)}{8\pi^2}. \tag{3.2}
\]
Thus a subthreshold \(J\)-cell would require a large enough volume deficit, with scalar near \(-18\) on the useful portion, to defeat the nonnegative Weyl and square terms. For a constant-scalar \(s=-24\) cell, (3.1) is
\[
P-8\pi^2=4\int|W^+|^2+48\{\operatorname{Vol}(U)-\operatorname{Vol}(B)\}.
\]
Consequently \(\operatorname{Vol}(U)\ge\operatorname{Vol}(B)\) implies the sharp \(P\ge8\pi^2\) lower bound. On a closed blow-up, an analogous hyperbolic-volume comparison for scalar \(-24\) metrics would yield the exact coefficient \(8\pi^2\) per blow-up. No such Yamabe-volume theorem is presently established here.

## 4. Numerical pressure on finite-scale real-hyperbolic saving

Peer code `Sessions/S1003A01/workspace/scripts/h4_perp_cell.py` uses
\[
F=x,\qquad G=x+2x^2,
\]
which was symbolically checked to have \(s=-24\), \(P=0\). It implements ordinary \(O(-1)\) bolt regularity and exact H4 two-jet contact. The peer large-collar \(X=64\), degree-16 \(P\)-optimized values are
\[
\begin{array}{c|c}
x_0&P/(8\pi^2)\\\hline
.003&1.00605638296\\
.01&1.02046688095\\
.03&1.06306956649.
\end{array}
\]
The new independent channel evaluator `workspace/scripts/h4_cell_channel_analysis.py` reconstructs these records at 1600-node quadrature. Its identities close to \(<4\times10^{-13}\). Data are in `workspace/data/h4_cell_channels.json`. The volume ratios are
\[
1.0000167741,\quad1.0000479885,\quad1.0001185601,
\]
the scalar means are \(-23.99985,-23.99959,-23.99905\), and the fractions of volume with \(|s+18|\le3\) are only about \(1.3\times10^{-7},1.4\times10^{-6},1.2\times10^{-5}\). The scalar-volume channels in (3.1) are positive and contribute approximately \(2.004x_0,2.004x_0,1.995x_0\), while the inferred \(4W^+\) terms are positive and smaller (roughly second order). Thus these profiles realize Theorem F's \(+2x_0\) response rather than a nonlinear saving.

The scan was extended to \(x_0=.1,.3,1\) at \(X=64\), degree 18. The floating values were
\[
P/(8\pi^2)=1.22129,\ 1.71385,\ 3.78377,
\]
with volume ratios \(1.00041,1.00131,1.00539\) and scalar still near \(-24\). The \(x_0=.3,1\) optimizers hit their iteration limits, but their large positive margins make them useful exclusions of an obvious continuation to a subthreshold branch, not minimizer estimates. A separate \(J\)-targeted run at \(x_0=.03,X=64\) gave
\[
P/(8\pi^2)=1.06462009,\qquad J/(8\pi^2)=1.06507303,
\]
again with no volume deficit and no scalar-near-\(-18\) region. Records: `workspace/data/h4_cell_channels_extended.json` and source JSON files beside it.

This is restricted numerical evidence. It does not prove the all-metric or even full diagonal infimum. It does show that the CH finite-collar surprise was actively sought in the H4 analogue over a much wider bolt-scale range and that the only available nonlinear channels remained on the positive side.

## 5. Off-bolt Weyl splitting for Theorem E

At the bolt, both chiral Weyl blocks have forced multiplicity \((2,1)\); this cannot test conformal Kählerness. The new script `workspace/scripts/ach_weyl_degeneracy_offbolt.py` integrates the exact Einstein ODE from the bolt series, reconstructs the exact radial two-jet, and independently evaluates both chiral curvature-operator blocks in coordinates. It sampled the central shooting parameter and both endpoints of the validated \(d\)-interval. Data: `workspace/data/ach_capd/weyl_degeneracy_offbolt.json`.

At \(t=.5\), uniformly across the three sampled parameters, the central spectra are approximately
\[
W_A=(-0.845829,-0.841893,1.687721),
\]
\[
W_B=(-1.96026,0.49655,1.46371).
\]
The smallest eigenvalue gaps are about \(3.94\times10^{-3}\) and \(0.967\). The reconstructed scalar is \(-24\) and \(|\operatorname{Ric}^\circ|\approx2.5\times10^{-11}\), which strongly cross-checks the coordinate curvature evaluation.

If both chiral Weyl blocks have simple spectrum at one point, then no conformal rescaling can be Kähler in either orientation near that point: a Kähler four-metric has the \((1,2)\) Weyl eigenvalue multiplicity in its complex orientation, and eigenvalue multiplicity is conformally invariant in dimension four. Since the metric is analytic, positivity of the discriminant at one point would also exclude a conformally Kähler open set anywhere in that orientation.

Current status: compelling floating evidence, not yet a theorem for the Ważewski-selected orbit. The validated existence theorem selects an unspecified \(d_0\) in the full interval; sampling endpoints and center does not enclose every \(d\). The clean next computation is interval transport of all 40 Fuchsian \(d\)-boxes to \(t=.5\), followed by an outward-rounded orthonormal-frame evaluation of both Weyl discriminants. The observed smaller gap \(3.9\times10^{-3}\) is plausible for CAPD/Arb certification.

## 6. Updated common picture

The direct-gap theory now has three distinct suppliers with different analytical continuations:

1. monopole/harmonic fields supply curvature alignment and differential prolongation;
2. the ambient self-dual curvature operator supplies the signed local topology-response law;
3. volume entropy supplies exact Einstein nonexistence on hyperbolic blow-ups.

All three become difficult at the same dimension-four critical exponent when one asks for a quantitative near-Einstein theorem. Metric-wise fields can be lost in bubbling; \(L^2\) curvature does not provide uniform Sobolev/harmonic-radius control; and entropy comparison needs pointwise Ricci control rather than critical \(L^2\) trace-free Ricci. This identifies a genuine common obstruction rather than three unrelated technical failures.



---

## Source step22_hyperbolic_volume_mass_and_weyl_certificate.md

Original: [sources/Sessions/S1003A02/workspace/notes/step22_hyperbolic_volume_mass_and_weyl_certificate.md](../sources/Sessions/S1003A02/workspace/notes/step22_hyperbolic_volume_mass_and_weyl_certificate.md)

# Step 22 — Hyperbolic volume/mass structure and the off-bolt Weyl theorem

Conventions follow `theorem_package_v1.md`. Two real-hyperbolic normalizations are used explicitly:

- closed scale: `K=-1`, `Ric=-3g`, `s=-12`;
- cell scale: `K=-2`, `Ric=-6g`, `s=-24`.

## 1. Closed hyperbolic blow-ups: a quantitative pointwise-Ricci theorem

Let \((Y,g_0)\) be a closed oriented real-hyperbolic four-manifold at
\(K=-1\), let
\[
X=Y\#k\overline{\mathbb{CP}}^{\,2},\qquad k\ge1,
\]
and let \(f:X\to Y\) be the degree-one pinch map. Relative Chern–Weil gives,
for every constant-scalar metric \(g\) on \(X\) with \(s_g=-12\),
\[
P(g)=8\pi^2k+4\int_X|W_g^+|^2+12\{\operatorname{Vol}_g(X)-\operatorname{Vol}_{g_0}(Y)\}. \tag{1.1}
\]
Here \(P=\int|\operatorname{Ric}^\circ|^2\) and the Weyl norm is the curvature-operator norm.

**Theorem H\(_\varepsilon\) (entropy gap with a Ricci floor).** If, in addition,
\[
\operatorname{Ric}_g\ge-3(1+\varepsilon)g,\qquad \varepsilon\ge0,
\]
then
\[
\operatorname{Vol}_g(X)\ge(1+\varepsilon)^{-2}\operatorname{Vol}_{g_0}(Y), \tag{1.2}
\]
and therefore
\[
P(g)\ge 8\pi^2k
-12\operatorname{Vol}_{g_0}(Y)\left[1-(1+\varepsilon)^{-2}\right]. \tag{1.3}
\]
If \(\varepsilon=0\), BCG rigidity says equality in (1.2) forces the pinch map to be homotopic to a Riemannian covering. This is impossible when \(k>0\). Hence for every \(k>0\),
\[
\operatorname{Ric}_g\ge-3g,\\ s_g=-12
\quad\Longrightarrow\quad
P(g)>8\pi^2k. \tag{1.4}
\]

**Proof.** The degree-one Besson–Courtois–Gallot inequality gives
\[
h(g)^4\operatorname{Vol}_g(X)\ge 3^4\operatorname{Vol}_{g_0}(Y).
\]
Bishop comparison under the stated Ricci floor gives
\(h(g)\le3\sqrt{1+\varepsilon}\). This proves (1.2). Substitution into
(1.1), followed by discarding \(4\int|W^+|^2\ge0\), proves (1.3).
Equality for \(\varepsilon=0\) is the BCG equality case. \(\square\)

This theorem is the exact coefficient-eight lower result in a natural
pointwise-Ricci class. Expanding its loss gives
\[
12\operatorname{Vol}(Y)[1-(1+\varepsilon)^{-2}]
=24\operatorname{Vol}(Y)\varepsilon+O(\varepsilon^2).
\]
It also isolates the critical difficulty: the unrestricted direct defect gives
only \(L^2\) control of \(\operatorname{Ric}^\circ\), not the Ricci floor needed
by Bishop comparison.

Primary source read: `Knowledge/objects/papers/Differentiable-rigidity-under-Ricci-curvature-lower-bound--cfb4c9cdd3c7--65a5a48bd00c/object.md`, especially Theorems 1.1 and 1.5 and the entropy derivation at lines 91–100.

## 2. The constant-scalar sharp gap and the hyperbolic volume problem

Equation (1.1) makes the unresolved scalar-normalized statement precise. The
degree-one scalar-volume inequality
\[
s_g\ge-12\quad\Longrightarrow\quad
\operatorname{Vol}_g(X)\ge\operatorname{Vol}_{g_0}(Y) \tag{2.1}
\]
would imply, for \(s_g\equiv-12\), the exact lower bound
\(P(g)\ge8\pi^2k\). Conversely, the volume inequality is exactly the missing
scalar input in this Chern–Weil route; the Weyl term means the numerical bound
\(P\ge8\pi^2k\) alone does not logically imply (2.1) for an individual
metric. Thus “equivalence” must be read as equivalence of the proposed
*field-free derivation* and the scalar-volume statement, not literal logical
equivalence metric by metric.

For negative Yamabe invariant, (2.1) is the assertion
\[
Y(X)\le Y(Y)=-12\operatorname{Vol}_{g_0}(Y)^{1/2}. \tag{2.2}
\]
The standard connected-sum inequality supplies the opposite inequality
\(Y(X)\ge Y(Y)\) because \(\overline{\mathbb{CP}}^2\) has positive Yamabe
invariant. Consequently (2.1) on the blow-up is equivalent to the Yamabe
identity
\[
Y\!\left(Y\#k\overline{\mathbb{CP}}^{\,2}\right)=Y(Y). \tag{2.3}
\]
The available primary sources establish this identity for important
Seiberg–Witten-supplied families, but not for arbitrary closed
real-hyperbolic four-manifolds. `Differentiable rigidity...` records that
Perelman settles the corresponding scalar-volume infimum in dimension three,
whereas in dimensions at least four the general connected-sum/Yamabe argument
only gives the easy inequality. No source retrieved here proves (2.3) in
four dimensions. This is the degree-one hyperbolic scalar-volume problem often
associated with Schoen's volume comparison question; we retain its unresolved
status rather than promote it to a theorem.

## 3. Exact-H\(^4\)-exterior cells: scalar-floor topology is impossible

Let \((M^4,g)\) be complete without boundary, exactly hyperbolic of sectional
curvature \(-1\) outside a compact set, with spherical end, and suppose
\(s_g\ge-12\). Chruściel–Delay's Theorem 1.6 states that in dimensions
\(3\le n\le7\) such a manifold is isometrically diffeomorphic to
\(\mathbb H^n\); their proof is non-spin. In general their Theorem 1.3 derives
AH energy positivity from the asymptotically Euclidean positive mass theorem,
and Huang–Jang–Martin supply zero-mass rigidity. For an exactly hyperbolic
exterior the mass vector is zero, so rigidity applies.

After scaling to the cell normalization, this yields:

**Theorem H\(_\mathrm{cell}\).** A complete exact-\(H^4\)-exterior
four-manifold with \(s\ge-24\) is hyperbolic space. Therefore no
\(D\#k\overline{\mathbb{CP}}^2\), \(k\ge1\), exact-\(H^4\)-collar cell can
satisfy \(s\ge-24\) everywhere.

Primary sources:

- `Knowledge/objects/papers/The-hyperbolic-positive-energy-theorem--8a032b16b3af--cfd203eab901/object.md`, Theorems 1.3 and 1.6;
- `Knowledge/objects/papers/Mass-Rigidity-for-Hyperbolic-Manifolds--36e83c2bd58b--2559be97cc05/object.md`, Theorem 3.

This is stronger and more general than the diagonal computations, but it does
not yet imply \(P\ge8\pi^2\): every topologically nontrivial competitor must
dip below the hyperbolic scalar value, and a sharp integral theorem must show
that its \((s+24)^2\) payment and Weyl energy dominate any negative
cosmological Einstein–Hilbert response. The positive-mass theorem supplies the
rigid scalar-floor half of the desired calibration, not the quantitative
completion for metrics that cross below the floor.

## 4. Why the complex-hyperbolic witness evades this rigidity

Maerten–Minerbe's ACH positive-mass theorem applies to a **spin,
asymptotically complex-hyperbolic Kähler/Hermitian manifold** with
\(s\ge s_{CH}\); in even complex dimension it additionally assumes
contractibility. It is not a non-spin all-metric theorem on
\(O(-1)\). See
`Knowledge/objects/papers/A-mass-for-asymptotically-complex-hyperbolic-manifolds--0585fd23b4a7--593794dd4404/object.md`, Theorem 0.1.

The certified cheap perpendicular CH cell also leaves the scalar-floor regime
explicitly. `workspace/scripts/ch_cell_scalar_min.py` evaluates the same
frozen metric used by the Arb cost certificate. At the bolt,
\[
s=-24.802356352356668<-24,
\]
and a 6801-point profile gives \(s<-24\) from the bolt through approximately
\(u=0.9428\), approaching \(-24\) in the exact collar. The value at the bolt is
directly enclosed using the Arb point evaluation. Record:
`workspace/data/ch_cell_scalar_profile_x003_X64.json`.

Thus this witness would not contradict even an all-metric ACH theorem carrying
the hypothesis \(s\ge s_{CH}\). The real/complex contrast is therefore
sharper than “real AH has a non-spin theorem, complex AH does not”: the CH
witness violates both the known structural hypotheses and the scalar lower
bound.

## 5. Computer-assisted off-bolt Weyl theorem for Theorem E

The Step-21 C++ draft was not correct. It used a wrong sign in solving the
Einstein equations for orbit sectional curvatures and inferred mixed curvature
entries from an invalid shortcut. `workspace/scripts/ach_weyl_interval.cpp`
now computes:

- \(K_{0i}=-(y_i'+y_i^2)\);
- \(K_{ij}\) from \(\operatorname{Ric}_{ii}=K_{0i}+K_{ij}+K_{ik}=-6\);
- the mixed entries directly from the Cartan connection, e.g.
  \[
  R_{0123}=-y_1n_1+y_2A+y_3C,
  \]
  with \(n_i=2a_i/(a_ja_k)\),
  \(A=(n_1+n_2-n_3)/2\), and cyclic analogues.

The runner `workspace/scripts/ach_weyl_interval_run.py` first compares the
CAPD formula to the independent coordinate/JAX curvature evaluation at the
same CAPD endpoint midpoint. The sorted spectra agree within
\(5.6\times10^{-15}\); the reconstructed scalar is \(-24\), and the
trace-free Ricci norm is \(8.5\times10^{-15}\).

It then transports all forty outward-rounded analytic Fuchsian boxes from
\(t=.01\) to \(t=.5\). Every signed pairwise gap in both chiral blocks excludes
zero. The weakest lower distances from zero are
\[
0.966994778415921,
\qquad
0.003926698448708077,
\]
and the corresponding discriminant lower bounds are
\[
66.18831770098221,
\qquad
0.0006333125307976167.
\]
The complete interval record is
`workspace/data/ach_capd/weyl_discriminant_t0.5.json`.

**Theorem E\(^+\).** The validated ACH Einstein metric of Theorem E has simple
Weyl spectrum in both chiralities at \(t=.5\). Hence no metric conformal to it
is Kähler in either orientation on a neighborhood of that orbit. Because the
Einstein metric is real analytic, a conformally Kähler structure on any
nonempty open set would force the appropriate Weyl discriminant to vanish
identically; the certified nonzero value excludes this. Thus the metric is not
conformally Kähler on any nonempty open set in either orientation.

This strictly strengthens the exact bolt result: the bolt proves non-Kähler and
non-half-conformally-flat, whereas the off-bolt interval theorem excludes
local conformal Kählerness.



---

## Source step23_yamabe_identity_hyperbolic_sharp_gap_and_cell_channels.md

Original: [sources/Sessions/S1003A02/workspace/notes/step23_yamabe_identity_hyperbolic_sharp_gap_and_cell_channels.md](../sources/Sessions/S1003A02/workspace/notes/step23_yamabe_identity_hyperbolic_sharp_gap_and_cell_channels.md)

# Step 23 — The Yamabe identity: sharp conditional gap on hyperbolic blow-ups and the two-channel structure of marked cells

Conventions: \(P=\int|\mathrm{Ric}^\circ|^2\), \(S=\int s^2\), Weyl norms are curvature-operator norms,
\(R=\int|\mathrm{Ric}|^2=P+S/4\), \(\mathcal J=4P/R\), \(\mathcal E=\inf_\lambda\int|\mathrm{Ric}-\lambda g|^2/(\lambda^2V)=\mathcal J+\int(s-\bar s)^2/R\)
(`Skills/geometric-analysis/references/conventions-and-literature.md`). Same-metric Chern–Weil:
\(8\pi^2(2\chi+3\tau)=\int(4|W^+|^2-|\mathrm{Ric}^\circ|^2+s^2/12)\).

## 1. The conformal Yamabe identity (closed and relative)

Let \(g\) be a metric, \(\hat g=u^2g\), \(u>0\), with \(\hat s\equiv-24\), i.e.
\[
6\Delta_g u=s\,u+24u^3\qquad(\Delta=\operatorname{div}\nabla).\tag{1.1}
\]
Put \(\sigma=s+24\). Multiplying (1.1) by \(u\) and integrating,
\[
I:=\int(\sigma u^2+24u^4-24u^2)\,d\mu_g=-6\int|\nabla u|^2. \tag{1.2}
\]
The pointwise algebraic identity
\[
\frac{\sigma^2}{12}-4\sigma-48(u^4-1)+4(\sigma u^2+24u^4-24u^2)=\frac1{12}\bigl(\sigma+24(u^2-1)\bigr)^2
\]
and (1.2) give
\[
\int\Bigl(\frac{\sigma^2}{12}-4\sigma\Bigr)-48\int(u^4-1)
=\frac1{12}\int\bigl(\sigma+24(u^2-1)\bigr)^2+24\int|\nabla u|^2 .\tag{1.3}
\]
By (1.1), \(\sigma+24(u^2-1)=s+24u^2=6\Delta u/u\), so the first term on the right is \(3\int(\Delta u/u)^2\).

**Closed form (exact LeBrun identity).** On a closed manifold with Yamabe constant \(Y[g]<0\), let \(\hat g\) be the
Yamabe metric normalized to \(\hat s=-24\); then \(Y[g]^2=576\,\mathrm{Vol}(\hat g)\) and (1.3) reads
\[
\int s_g^2\,d\mu_g=Y[g]^2+36\int\Bigl(\frac{\Delta u}{u}\Bigr)^2+288\int|\nabla u|^2. \tag{1.4}
\]
This sharpens LeBrun's inequality \(\int s^2\ge Y[g]^2\) (equality iff \(s\) constant) to an identity. With
P scale-invariant and \(W^+\) conformally invariant this is equivalent to the identity found independently by S1003A01
(message #776): \(P(g)-P(\hat g)=24\int|\nabla u|^2+3\int(\Delta u/u)^2\).

**Relative form (marked cells).** Let \((U,g)\) be complete and exactly the \(\mathrm{Ric}=-6\) model (real hyperbolic
\(K=-2\), or complex hyperbolic, holomorphic curvature \(-4\)) outside a compact set, and let \(\hat g=u^2g\) be the
complete solution of (1.1) with \(u\to1\). On the exact exterior the linearization of (1.1) is \(6\Delta w=48w\); its
decaying radial solutions are \(w\sim e^{-4\sqrt2\,t}\) (H\(^4\), with volume growth \(e^{3\sqrt2t}\)) and
\(w\sim e^{-(2+2\sqrt3)t}\) (CH\(^2\), volume growth \(e^{4t}\)). All integrands in (1.3) are therefore integrable,
the boundary flux \(\oint u\partial_\nu u\to0\), and with \(B\) the model ball replaced by the cell,
\[
\int_{U_{\rm int}}\frac{s^2}{12}-48\,\mathrm{Vol}(B)
=48\,\mathrm{RV}(\hat g)+3\int\Bigl(\frac{\Delta u}{u}\Bigr)^2+24\int|\nabla u|^2,
\qquad
\mathrm{RV}(\hat g)=\bigl[\mathrm{Vol}_g(U_{\rm int})-\mathrm{Vol}(B)\bigr]+\int(u^4-1)\,d\mu_g. \tag{1.5}
\]
\(\mathrm{RV}(\hat g)\) is the renormalized volume of \(\hat g\) relative to the model for the **fixed marked end**
(the identification of the exterior with the model exterior is part of the data). In (1.5) the conformal integral
\(\int(u^4-1)\,d\mu_g\) runs over the **whole complete cell**, not only over \(U_{\rm int}\); \(U_{\rm int}\) and the model
ball \(B\) are matched truncations (same exterior cut). With this definition moving the cut through the exact end
changes neither \(\mathrm{RV}\) nor \(\Delta W_+\). (Step-24 repair.) Since \(W^+\) is conformally invariant, combining with
\(P_{\rm cell}-8\pi^2=4\Delta W_++[\int_{U_{\rm int}}s^2/12-48\mathrm{Vol}(B)]\) gives

**Theorem C (two-channel cell identity).** Let \(U\) be a complete marked cell of topology \((k,\ell)\) (i.e. \(D^4\#k\overline{\mathbb{CP}}^2\) with \(\ell\) handles), exactly equal to the
H\(^4\) or CH\(^2\) model outside a compact set for a fixed marking of the end, and let \(u\to1\) solve (1.1) with
\(u-1\) and its first two derivatives decaying faster than the inverse volume growth (\(e^{-3\sqrt2t}\) for H\(^4\), \(e^{-4t}\)
for CH; the rates above give this). Then, with the matched relative volume (1.5),
\[
P_{\rm cell}(g)-8\pi^2(k+4\ell)=4\Delta W_+ +48\,\mathrm{RV}(\hat g)+3\int\Bigl(\frac{\Delta u}{u}\Bigr)^2+24\int|\nabla u|^2,\tag{1.6}
\]
(the constant is \(8\pi^2\) for one blow-up)
and \(P_{\rm cell}(\hat g)-8\pi^2(k+4\ell)=4\Delta W_++48\,\mathrm{RV}(\hat g)\) exactly. The closed identity (1.4) is the
exact defect form of LeBrun's estimate; it is already implicit in LeBrun's 1996 Lemma 1 computation
\cite{lebrun1996four}, so its novelty here is the relative (cell) version and its use as a channel decomposition. In real-hyperbolic bulk
\(\Delta W_+=\int|W^+|^2\ge0\). Hence

- the H\(^4\) cell lower bound \(P_{\rm cell}\ge8\pi^2\) follows from the renormalized-volume comparison
  \(\mathrm{RV}(\hat g)\ge0\) for complete \(\hat s\equiv-24\) metrics on \(D\#k\overline{\mathbb{CP}}^2\) conformal to
  exact-H\(^4\)-collar metrics (a local, topological form of the hyperbolic Schoen volume question), and is equivalent
  to the statement \(\inf\{4\int|W^+|^2+48\mathrm{RV}(\hat g)\}\ge0\) over such \(\hat g\);
- in complex-hyperbolic bulk the Weyl channel \(4\Delta W_+\) has no sign and is the only possible saving channel if
  \(\mathrm{RV}\ge0\).

Existence of \(u\): for exact-H\(^4\) exteriors the cell is conformally compact and the Loewner–Nirenberg /
Aviles–McOwen / Andersson–Chruściel–Friedrich solution exists and is unique. **For exact-CH exteriors existence is now
unconditional** (S1003A01, `Sessions/S1003A01/workspace/notes/step22_exact_CH_conformal_reduction.md`, read and
checked in Step 24): piecewise weak barriers \(u_-=0\) on the core, \(1-e^{-a(r-R)}\) on the end, and \(u_+=M\) on the core,
\(1+(M-1)e^{-a(r-R)}\) on the end have the correct jump signs for \(-6\Delta\); exhaustion, Harnack positivity and a
maximum-principle comparison give a unique positive \(u\to1\) for **every** smooth exact-CH-ended cell, with no sign
condition on \(s\) (the spectral criticality \(6\lambda_0(CH^2)+s_{CH}=0\) is circumvented by the barriers). Bootstrapping
gives \(u-1=O(e^{-mr})\) with all derivatives for every \(4<m<2+2\sqrt3\). Consequently Theorem C holds for every
smooth exact-CH-ended cell, and the exact-ended \(J_6\) infimum equals the infimum of \(P\) over complete scalar \(-24\)
metrics asymptotic to the same marked CH end at a rate \(>4\).

## 2. Numerical evaluation of the channels (all diagonal cells available in both bulks)

Script `workspace/scripts/cell_yamabe_rv.py` (finite-volume Newton solve of (1.1) in \(z=\log x\) from the bolt to
\(x=10^{12}\); interior integrals by Simpson in \(q=\sqrt u\) with ball-density subtraction; every row run at
\(N=2000\) and \(4000\); the residual of (1.5) falls by \(\approx4\times\), i.e. it is the \(O(h^2)\) discretization error).
Data: `workspace/data/cell_yamabe_rv_h4.json`, `workspace/data/cell_yamabe_rv_ch_*.json`. Units: \(8\pi^2\).

| bulk | cell | \(P-1\) | \(4\Delta W_+\) | \(48\,\mathrm{RV}(\hat g)\) | \(Q=3\int(\Delta u/u)^2+24\int|\nabla u|^2\) |
|---|---|---|---|---|---|
| H4 | x0=.003,X=64 | .0060564 | .0000448 | .0059746 | .0000384 |
| H4 | x0=.01,X=64 | .0204669 | .0004287 | .0196932 | .0003408 |
| H4 | x0=.03,X=64 | .0630696 | .0032069 | .0573917 | .0024755 |
| H4 | x0=.1,X=64 | .2212945 | .0242920 | .1763832 | .0206208 |
| H4 | x0=.3,X=64 | .7138523 | .1198339 | .4646966 | .1293328 |
| H4 | x0=1,X=64 | 2.7837715 | .5616916 | 1.3830789 | .8390285 |
| H4 | x0=.03, J-opt | .0646201 | .0035830 | .0609064 | .0001296 |
| CH | x0=.003,X=64 | −.0002048 | −.0063926 | .0061871 | .0000001 |
| CH | x0=.01,X=64 | −.0012996 | −.0229953 | .0216969 | .0000005 |
| CH | x0=.03,X=64 (certified witness) | −.0041516 | −.0747382 | .0706363 | .0000018 |
| CH | x0=.05,X=128 | −.0037125 | −.1252945 | .1216119 | .0000034 |

Findings.

1. \(\mathrm{RV}(\hat g)>0\) in every cell of both bulks, including the certified cheap CH witness and H\(^4\) cells
   up to \(x_0=1\). In two CH cells the raw volume difference \(\mathrm{Vol}_g-\mathrm{Vol}(B)\) is negative
   (\(-3.4\times10^{-4}\) at \(x_0=.01\)); the conformal normalization restores positivity, so the relevant object is
   \(\mathrm{RV}(\hat g)\), not the raw volume.
2. **The cheap CH cell pays in renormalized volume and saves entirely in Weyl curvature.** At the certified witness,
   \(48\mathrm{RV}=+0.0706\), \(Q=2\times10^{-6}\), \(4\Delta W_+=-0.0747\). The scalar/volume channel is a cost in both
   bulks; the CH/H\(^4\) contrast lies in the Weyl channel alone.
3. **The two halves of \(\mathbf R^+=W^++\tfrac{s}{12}I\) in Theorem F are the two channels.** As \(x_0\to0\):
   \(48\mathrm{RV}/x_0=1.992,1.968,1.913\) (H\(^4\)) and \(2.062,2.170,2.355\) (CH) \(\to 2=-s_p/12\);
   \(4\Delta W_+/x_0=0.015,0.043,0.107\to0=W^+_p\) (H\(^4\)) and \(-2.131,-2.300,-2.491\to-2=-W^+_p(\zeta,\zeta)\) for the
   perpendicular CH direction. The quadratic terms scale like \(x_0^2\) (\(Q/x_0^2\approx4.3,3.4,2.8\) for H\(^4\)).
   In the Burns-gluing proof of Theorem F, the scalar flux \(4\pi^2x_0\) produces
   \(\Delta S/12=-8\pi^2x_0s_p/12+O(x_0^{6/5})\) and the self-dual flux \(\Phi_{++}=\pi^2\zeta\otimes\zeta\) produces
   \(4\Delta W_+=-8\pi^2x_0W^+_p(\zeta,\zeta)+O(x_0^{6/5})\); by (1.5), \(48\mathrm{RV}(\hat g)=\Delta S/12-Q\). The
   numerical \(Q=O(x_0^2)\) says that the first-order scalar response *is* the renormalized volume of the Yamabe
   representative. A proof of \(Q=o(x_0)\) for the Burns-glued metrics would make this a theorem
   (\(\sigma\approx24\) on a core of volume \(O(x_0^2)\), \(w=O(x_0)\) there; the estimate needed is an
   \(L^2\) bound on \(\nabla w\) at that scale).
4. The H\(^4\) Yamabe correction decays exactly at the real-hyperbolic mass order (\(\rho^4\)); its coefficient \(c\)
   (`decay_coeff_c`) is positive in every H\(^4\) cell (\(c/x_0\approx0.034\) for small cells), consistent with
   Chruściel–Delay positivity and Huang–Jang–Martin rigidity for \(\hat g\). The CH indicial root \(2+2\sqrt3\) is not
   tied to any mass order; no CH mass statement is drawn.

## 3. Hyperbolic blow-ups: exact Chern–Weil reduction to the Yamabe invariant

Let \(Y\) be a closed oriented real-hyperbolic four-manifold, \(X_k=Y\#k\overline{\mathbb{CP}}^2\),
\(Y_{\rm hyp}=Y[g_{\rm hyp}]<0\). Gauss–Bonnet for \(g_{\rm hyp}\) gives \(Y_{\rm hyp}^2/12=16\pi^2\chi(Y)\), and
\((2\chi+3\tau)(X_k)=2\chi(Y)-k\). Therefore, **for every metric** \(g\) on \(X_k\),
\[
P(g)=8\pi^2k+4\int|W^+|^2+\frac{S(g)-Y_{\rm hyp}^2}{12}. \tag{3.1}
\]
If \(Y[g]<0\), (1.4) refines this to
\[
P(g)=8\pi^2k+4\int|W^+|^2+\frac{Y[g]^2-Y_{\rm hyp}^2}{12}+3\int\Bigl(\frac{\Delta u}{u}\Bigr)^2+24\int|\nabla u|^2 .\tag{3.2}
\]
Kobayashi's connected-sum inequality (\(\overline{\mathbb{CP}}^2\) has positive Yamabe invariant) gives
\(Y(X_k)\ge Y(Y)\ge Y_{\rm hyp}\); \(Y(X_k)\) is nondecreasing in \(k\).

**Theorem H (sharp gap on hyperbolic blow-ups, conditional on one Yamabe identity).** Assume
\[
\mathcal Y(Y\#k\overline{\mathbb{CP}}^2)=Y_{\rm hyp}. \tag{H}
\]
((H) is the conjunction of Schoen's conjecture \(\mathcal Y(Y)=Y_{\rm hyp}\) and blow-up invariance
\(\mathcal Y(X_k)=\mathcal Y(Y)\); it implies (H) for every \(k'\le k\).) Then:

1. \(P(g)>8\pi^2k\) for every metric on \(X_k\), and \(\inf P=8\pi^2k\). The infimum is not attained.
2. In the \(\mathcal E\)-normalization, for \(1\le k\le2\chi(Y)\),
   \[
   \alpha(X_k)=\inf\mathcal E=\inf\mathcal J=\frac{4k}{k+6\chi(Y)},
   \]
   For \(1\le k<2\chi(Y)\) this value is not attained. At the endpoint \(k=2\chi(Y)\) the common infimum equals \(1\)
   (unconditionally, since \(\mathcal J\ge1\) there by (3.1)); attainment of \(\mathcal J=1\) is equivalent to an
   anti-self-dual metric on \(X_k\), attainment of \(\mathcal E=1\) additionally to constant scalar curvature, and the
   present argument does not exclude either. (Step-24 correction.)
3. Every \(P\)-minimizing sequence satisfies \(\int|W^+|^2\to0\), \(Y[g_j]\to Y_{\rm hyp}\),
   \(\int|\nabla u_j|^2+\int(\Delta u_j/u_j)^2\to0\): minimizing sequences become globally asymptotically
   half-conformally-flat and Yamabe-extremal. That the total \(8\pi^2k\) is carried as \(8\pi^2\) by each exceptional
   class is known only for the explicit Burns sequences; for an arbitrary minimizing sequence it requires a
   localization theorem that is not available. (Step-24 correction.)

*Proof.* (1) Under (H), \(Y[g]\le\mathcal Y(X_k)=Y_{\rm hyp}<0\) for every \(g\), so \(Y[g]^2\ge Y_{\rm hyp}^2\) and
(3.2) gives \(P\ge8\pi^2k\). Upper bound: Theorem F at \(k\) distinct points of \((Y,g_{\rm hyp})\), where
\(\mathbf R^+=-2I\) in the \(\mathrm{Ric}=-6\) scale, gives metrics with
\(P=8\pi^2k(1+2x_0)+O(kx_0^{6/5})\to8\pi^2k\). If \(P(g)=8\pi^2k\), equality in (3.2) forces \(\nabla u=0\), so \(g\)
has constant negative scalar curvature and \(Y[g]=\mathcal Y(X_k)\): \(g\) attains the Yamabe invariant
\(\sup_{[g]}\inf\). A metric attaining a nonpositive Yamabe invariant is Einstein (LeBrun \cite{lebrun1996four}, §2,
via the Schoen variational argument; equivalently it minimizes \(\int s^2\) over all metrics, Ishida–LeBrun
Prop. 12, and the Euler–Lagrange equation \(-2s\,\mathrm{Ric}+\tfrac12s^2g=0\) for constant \(s\ne0\) gives
\(\mathrm{Ric}=\tfrac s4g\)). Then \(P(g)=0<8\pi^2k\), a contradiction; strictness of \(P>8\pi^2k\) follows the same way.
Independently, Sambusetti's entropy theorem excludes Einstein metrics on \(X_k\).
(2) Write \(t=P/S\), so \(\mathcal J=16t/(4t+1)\) is increasing in \(t\). By (3.1),
\(t\ge\tfrac1{12}-8\pi^2(2\chi(Y)-k)/S\). For \(k\le2\chi(Y)\) the right side increases with \(S\), and
\(S\ge Y[g]^2\ge Y_{\rm hyp}^2=192\pi^2\chi(Y)\) (LeBrun's estimate and (H)) gives \(t\ge k/(24\chi(Y))\), i.e.
\(\mathcal E\ge\mathcal J\ge4k/(k+6\chi(Y))\). The Burns sequences have \(P\to8\pi^2k\), \(S\to Y_{\rm hyp}^2\) and
\(\int(s-\bar s)^2\to0\) (the scalar curvature differs from \(-24\) only on cores of volume \(O(x_0^2)\)), so
\(\mathcal E\to4k/(k+6\chi(Y))\). Non-attainment for \(k<2\chi(Y)\): equality forces \(P=8\pi^2k\), excluded by (1). At
\(k=2\chi(Y)\) the bound \(\mathcal J\ge1\) is attained exactly by anti-self-dual metrics (\(P-S/12=4\int|W^+|^2\) there),
which (1) does not exclude. (3) is read off from (3.2) and \(S\to Y_{\rm hyp}^2\). \(\square\)

**Unconditional content.** Without (H), put \(y_k=\mathcal Y(X_k)^2/Y_{\rm hyp}^2\in[0,1]\) (with \(y_k=0\) if
\(\mathcal Y(X_k)\ge0\)). The same argument gives, for every metric,
\[
P\ge8\pi^2k-\frac{(1-y_k)Y_{\rm hyp}^2}{12},\qquad
\frac{P}{S}\ge\frac{2\chi(Y)y_k-(2\chi(Y)-k)}{24\chi(Y)y_k}\quad(k\le2\chi(Y)),
\]
while Theorem F gives \(\inf P\le8\pi^2k\) and \(\alpha(X_k)\le4k/(k+6\chi(Y))\). Thus on hyperbolic blow-ups the
lower-bound problem is controlled by the Yamabe invariant: \(\alpha(X_k)>0\) whenever \(y_k>1-k/(2\chi(Y))\);
\(y_k=1\) is **sufficient** for the sharp value \(\inf P=8\pi^2k\) (the Yamabe lower estimate then meets the Burns upper
estimate) but is not proved necessary, since for \(y_k<1\) the decomposition does not exclude compensation by the
Weyl and conformal-square terms; any shortfall below \(8\pi^2k\) is at most \((1-y_k)\cdot16\pi^2\chi(Y)\). For
\(k>2\chi(Y)\), (3.1) gives \(P-S/12\ge8\pi^2(k-2\chi(Y))>0\), so \(\mathcal E\ge\mathcal J>1\) **pointwise**, but conformal
inflation (\(S\to\infty\) in a fixed conformal class with \(W^+\) fixed) gives \(\inf\mathcal J=1\); there is no uniform
separation of \(\mathcal J\) above one, and \(\inf\mathcal E\) is only known to lie between \(1\) and the Burns value
\(4k/(k+6\chi(Y))\). (Step-24 correction.)

**Relation to Theorem H\(_\varepsilon\).** H\(_\varepsilon\) (Step 22) is the pointwise-Ricci shadow: under
\(\mathrm{Ric}\ge-3(1+\varepsilon)g\), BCG entropy plus Bishop supplies the volume comparison that (H) supplies for
every metric. The dimension-four difficulty on this family is located in the Yamabe invariant: (H) is the only missing
input, and no \(L^2\)-regularity question remains once it is available.

Status of (H): the retrieved sources (LeBrun 1996, Ishida–LeBrun, Akutagawa–Botvinnik–Kobayashi–Seshadri,
Kotschick's survey, `Differentiable rigidity...`) compute \(\mathcal Y\) for Seiberg–Witten/Bauer–Furuta-supplied
families and record the three-dimensional Perelman result; none proves Schoen's conjecture or blow-up invariance for
closed real-hyperbolic four-manifolds. The Brendle–Chodosh asymptotically hyperbolic volume comparison was not
retrieved by this Step's request. (H) is therefore recorded as the single open hypothesis.

## 4. What this changes

- The scalar side of both the closed and the cell problems is now an exact identity rather than an inequality; the
  only non-sign-definite terms are \(\Delta W_+\) and a renormalized/Yamabe volume.
- The CH/H\(^4\) contrast is completely located: identical positive volume cost \(\approx-x_0s/12\), opposite Weyl
  response \(-x_0W^+(\zeta,\zeta)\). **Superseded target (Step 24):** a linear trade-off
  \(4\Delta W_+\ge-\Lambda\cdot48\mathrm{RV}-\eta\) is not a usable lower-bound target. In the CH kernel direction Theorem F
  forces the two channels to cancel at first order, so the measured \(\Lambda\in[1.03,1.06]\) tends to \(1\) and
  \(\Lambda-1\) is a second-order Weyl excess; and \(\Lambda>1\) gives no absolute bound without an upper bound on RV. The
  correct cell problem is absolute:
  \(\inf\{8\pi^2+4\Delta W_++48\mathrm{RV}(\hat g)\}>0\) over complete scalar \(-24\) metrics asymptotic to the marked
  standard CH end on \(O(-1)\). The certified cheap cells delete only \(\Delta W_+\approx-1.5\) of self-dual Weyl energy,
  whereas a zero-cost cell with \(\mathrm{RV}\ge0\) must delete at least \(2\pi^2\approx19.7\) (relative signature
  \(\Delta W_+-\int|W^-|^2=-12\pi^2\)); they are perturbative Burns bubbles far from the zero-cost regime, so positivity
  of \(p_{1,0}\) is a compactness-and-degeneration statement, not a profile optimization.
- For H\(^4\) cells, \(\mathrm{RV}(\hat g)\ge0\) (all tested cells positive, with first-order value \(x_0/24\)) is the
  precise local statement; it is a topological, asymptotically-hyperbolic analogue of the closed problem (H).



---

## Source step25_diagonal_cell_compactness_and_CR_pinning.md

Original: [sources/Sessions/S1003A02/workspace/notes/step25_diagonal_cell_compactness_and_CR_pinning.md](../sources/Sessions/S1003A02/workspace/notes/step25_diagonal_cell_compactness_and_CR_pinning.md)

# Step 25 — Diagonal blow-up cells: CR pinning at finite cost, face dynamics, and the structure of minimizing sequences

Session S1003A02, Agent2. Conventions: diagonal Bianchi-IX metrics
\(g=dt^2+\sum a_i^2\sigma_i^2\), \(d\sigma_i=2\sigma_j\wedge\sigma_k\) (so \(\sum\sigma_i^2\) is the unit round \(S^3\),
\(\int_{S^3}\sigma_{123}=2\pi^2\)); \(y_i=a_i'/a_i\); costs \(\widehat P=P/(8\pi^2)\), threshold \(1\); the CH end is normalized
to \(\mathrm{Ric}=-6g\), \(a_g=a_h=\sinh t\) (contact plane), \(a_f=\sinh t\cosh t\) (Reeb slot). Compact ACH variables
\((y_f,y_g,y_h,\kappa,q,\zeta)\), \(\kappa=a_f/(a_ga_h)\), \(q=\log(a_g/a_h)\), \(\zeta=1/(a_ga_h)\), as in
`workspace/scripts/ach_projected.py`; the Rossi/neutral variable is
\[
\widetilde\Phi=q+\tfrac14(y_g-y_h)-\zeta\sinh q,
\qquad \rho_\infty=e^{\widetilde\Phi(\infty)}\ \text{on ACH ends},\qquad \widetilde\Phi\equiv0\ \text{on exact CH}.
\]

The question of this note: in the diagonal (SU(2)-invariant diagonal) class
\(\mathscr C_{\rm diag}\) of smooth metrics on \(O(-1)\) that are exactly CH outside a compact set, what can a
minimizing sequence for \(\widehat P\) do, and how is the infimum
\(p^{\rm diag}_{1,0}\le0.99585\) (certified, `Sessions/S1003A01/workspace/data/perp_area/rigorous_x00.03_X64_d16.json`)
related to exact Einstein metrics? By Theorem C and the exact-CH barrier theorem the problem may equivalently be posed
for \(P\) over scalar-\(-24\) diagonal metrics (the Yamabe factor \(u\) is unique, hence \(SU(2)\)-invariant and a function of
\(t\); it lowers \(P\) by \(24\int|\nabla u|^2+3\int(\Delta u/u)^2\)).

## 1. CR pinning: an exact identity and a sharp inequality

**Identity.** For *every* diagonal metric put \(e_i=\mathrm{Ric}(e_i,e_i)+6\) in the orbit directions. Since
\(\mathrm{Ric}_{ii}=-y_i'-y_iS+\mathrm{Pot}_i\) (\(S=\sum y_j\), \(\mathrm{Pot}_i\) the orbit-curvature potentials),
\[
y_i'=6-y_iS+\mathrm{Pot}_i-e_i ,
\]
and differentiating \(\widetilde\Phi\) gives exactly
\[
\widetilde\Phi'=\zeta^2G\;-\;\tfrac14\,(e_g-e_h)=\zeta^2G-\tfrac14\bigl(\mathrm{Ric}^\circ_{gg}-\mathrm{Ric}^\circ_{hh}\bigr), \tag{1.1}
\]
where \(\zeta^2G\) is the Einstein drift polynomial of `ach_phi_drift.py` (no constraint is used). Verified in
`workspace/scripts/cr_pinning_check.py` → `workspace/data/cr_pinning_check.json`: the control part is symbolically
\(-(e_g-e_h)/4\); the free part vanishes on the ACH curve \(E(q)\); CH and H\(^4\) solve the uncontrolled system
exactly; a randomly forced integration reproduces (1.1) to \(7\times10^{-16}\).

**Lemma P (CR pinning).** For any diagonal metric on \([T_0,T_1]\times S^3\), with \(W=a_1a_2a_3\),
\[
\Bigl|\widetilde\Phi(T_1)-\widetilde\Phi(T_0)-\int_{T_0}^{T_1}\zeta^2G\,dt\Bigr|
\le\Bigl(\frac{\widehat P_{[T_0,T_1]}}2\Bigr)^{1/2}\Bigl(\int_{T_0}^{T_1}\frac{dt}{W}\Bigr)^{1/2}. \tag{1.2}
\]
*Proof.* \(P_{[T_0,T_1]}=2\pi^2\int W|\mathrm{Ric}^\circ|^2dt\ge2\pi^2\int W\bigl((\mathrm{Ric}^\circ_{gg})^2+(\mathrm{Ric}^\circ_{hh})^2\bigr)\ge\pi^2\int W(e_g-e_h)^2\);
apply Cauchy–Schwarz to \(\frac14\int(e_g-e_h)\) with weights \(W^{\pm1/2}\) and use \(P=8\pi^2\widehat P\). \(\square\)

**Corollary P1.** If a cell is exactly CH for \(t\ge T_1\) and on \([T,T_1]\) its orbits satisfy \(W\ge c\,e^{4t}/16\) and its
state lies in a cusp block of the Step-15 type (so \(|\int_T^\infty\zeta^2G|\le\delta(T)=\sup_B|G|\,\zeta(T)^2/(2c_B)\); the
verified blocks cover \(q\in[0.70,3.20]\), e.g. \(\sup|G|\le19.58\), \(c_B\ge1.998\) for \(q\in[0.7,0.9]\); **the standard-end block
\(B(K=1,\zeta_0=10^{-2},q\in[-0.3,0.3])\) was verified this step** — all egress/ingress faces pass, \(\zeta\)-decay factor
\(\ge1.99844\), \(q\)-drift \(\le0.0111\), \(\sup_B|G|\le7.354\) — files `workspace/data/ach_block/block_K1_z0.01_q-0.3_0.3.json`,
`workspace/data/ach_block/phidrift_K1_z0.01_q-0.3_0.3.json`), then
\[
\widehat P_{[T,\infty)}\ \ge\ \frac c2\,e^{4T}\bigl(|\widetilde\Phi(T)|-\delta(T)\bigr)_+^2 . \tag{1.3}
\]
(\(\int_T^\infty16e^{-4t}/c=4e^{-4T}/c\).) Thus correcting a Rossi squashing \(\log\rho\) at radius \(T\) costs at least
\(\tfrac12e^{4T}(\log\rho)^2\) in units \(8\pi^2\).

**Sharpness (linear theory).** `workspace/scripts/squash_escape_cost.py` (data `workspace/data/squash_escape_cost.json`)
linearizes the antisymmetric sector \(a_g=Ae^{\theta/2},a_h=Ae^{-\theta/2}\) about CH: \(dz_g=-dz_h=\tfrac12\theta''+(2\coth2t+\operatorname{csch}2t)\theta'+16\frac{\cosh2t-3}{\cosh4t-1}\theta\), \(ds=0\),
kernel \(\{k^{-1},k^{-1}\!\int m\}\), \(k=\tanh^4t\). In Abel form the cost is \(\int w(\psi')^2\), \(\theta=k^{-1}\varphi\),
\(\psi=\varphi'/m\), \(m=(1+\tanh2t)^2e^{-4t}\tanh^7t/\tanh^22t\), \(w=(1+\tanh2t)^4e^{-8t}\sinh^9t/(8\cosh^5t\tanh^42t)\).
For interior data \((\varphi,\psi)(T)\) the minimum cost of reaching exact CH is \((\theta_\infty^{\rm int})^2/G(T)\) with
\(G(T)=\int_T^\infty M^2/w\), \(M(t)=\int_t^\infty m\), where \(\theta^{\rm int}_\infty\) is the conformal-infinity squashing of the
interior linearized Einstein end. Numerically \(e^{-4T}/G(T)=0.6974,0.5283,0.5005,0.50000018\) at \(T=.5,2,4,8\), and
exactly \(m\sim4e^{-4t}\), \(w\sim e^{-4t}/8\), \(G\sim2e^{-4T}\): \(Q_{\min}\sim\frac12C^2e^{4T}\). The constant \(\tfrac12\) of
(1.3) (with \(c=1\)) is therefore asymptotically optimal; the Cauchy–Schwarz equality case is the linear optimizer.

**Meaning.** The CR structure at infinity is not a free boundary datum for finite-cost cells: wherever the orbit volume is
large, the Rossi parameter is frozen at the cost \(\tfrac12e^{4T}(\Delta\log\rho)^2\). In particular the validated
nonstandard Einstein filling of Theorem E (\(\rho_\infty\in[2.1901,2.1925]\)) is *not* a bounded-cost limit of exact-CH
diagonal cells on growing compacta in which the orbits remain in the ACH block: any such cell agreeing with it to
radius \(T\) pays at least \(\approx\tfrac12e^{4T}(0.784)^2\). The "escape to the diagonal Einstein branch" degeneration is
forced to the standard value \(\rho=1\).

## 2. Off-curve excursions at large orbit volume: the conformal-infinity face

The ACH curve \(E(q)=(2,1,1,1,q,0)\) has spectrum \(\{2,0,-2,-4,-6,-8\}\). Since \(\zeta'=-\zeta(y_g+y_h)\), the unstable
manifold of \(E(q)\) lies in the invariant face \(\zeta=0\) (conformal infinity). On the face the \((y,\kappa)\)-system
\[
y_f'=6-y_fS+2\kappa^2,\quad y_{g,h}'=6-y_{g,h}S-2\kappa^2,\quad \kappa'=\kappa(y_f-y_g-y_h),\quad q'=y_g-y_h
\]
does not involve \(q\), with constraint \(y_fy_g+y_gy_h+y_hy_f-6+\kappa^2=0\). Face spectrum at \(E(q)\): \(\{2,0,-4,-6,-8\}\),
unstable vector \((0.8,-0.6,-0.6,1,0)\). `workspace/scripts/face_unstable_fates.py` (data
`workspace/data/face_unstable_fates.json`, \(\varepsilon=10^{-3},10^{-5}\)) integrates both branches:

- \(\kappa\uparrow\): finite-time blow-up (\(t\approx3.4\), resp. \(5.7\)), with \(y_g=y_h\to-\infty\): contact radii collapse at
  finite radius; this is the singular fate.
- \(\kappa\downarrow\): convergence to the real-hyperbolic AH point \(\kappa=0\), \(y_i=\sqrt2\) (the \(K=-2\) H\(^4\) end), which
  is attracting in the face (eigenvalues \(-\sqrt2\) in \(\kappa\), \(-3\sqrt2,-3\sqrt2,-6\sqrt2\) in \(y\)).

Neither branch returns to the ACH curve, and \(q\) is constant along both. Consequently a cell that is in the ACH block at a
radius where \(W\) is large cannot leave the curve and return to the exact standard end through near-Einstein dynamics:
leaving along the unstable direction leads to an AH end or a singularity, and returning requires \(O(1)\) control
where \(\int dt/W\) is tiny, which costs \(\gtrsim W\). The rigorous form needed is a shadowing statement: on intervals
where \(W\ge W_*\), the integrated control is at most \((\widehat P/2)^{1/2}(\int dt/W)^{1/2}\) by the same Cauchy–Schwarz
argument applied to every component of (1.1)-type equations, so the state is a \(\delta\)-pseudo-orbit of the Einstein flow
with \(\delta\to0\) as \(W_*\to\infty\); together with the face phase portrait (no chain from \(E(q)\) back to the curve off the
curve) this excludes large-volume excursions. The face phase portrait is so far established numerically for the
unstable branches; a validated version (or a Lyapunov function on the face) is a bounded computation.

## 3. Structure of diagonal minimizing sequences

Let \(g_j\in\mathscr C_{\rm diag}\) with \(\widehat P(g_j)\to p^{\rm diag}_{1,0}\le0.99585\), CH end normalized to
\(\mathrm{Ric}=-6\), bolt radius \(b_j\). Proved inputs: lower semicontinuity of \(\widehat P=\int\frac W4|z|^2dt\) under local
\(H^2\) convergence of noncollapsed diagonal metrics (control enters the dynamics affinely; \(z\) weakly convergent in
weighted \(L^2\)); Lemma P; Lemma Q′ (an almost-Euclidean neck enclosing the \((-1)\)-class forces
\(\widehat P\ge1-C\varepsilon\)); the bubble inequality \(\widehat P(N)\ge3|\tau+\eta|-2\chi+2/|\Gamma|=1\) for an ALE bubble on
\(O(-1)\) with \(\Gamma=1\); exact-collar Einstein rigidity (no Einstein exact-CH-collar cell).

The alternatives, after passing to a subsequence, are:

1. **Scale-separated bolt concentration** (\(b_j\to0\) with an almost-Euclidean annulus between bolt scale and CH scale):
   excluded, cost \(\ge1-o(1)>p^{\rm diag}_{1,0}\), whatever the inner geometry (Burns-type, Taub-bolt-type, collapsed).
2. **Collapsed connector** (\(b_j\to0\) without an almost-Euclidean annulus; e.g. a Taub-bolt ALF core whose Hopf circle
   stays short up to the CH scale): not excluded. This is the genuine collapse branch of the cell problem.
3. **Large bolt** (\(b_j\to\infty\)): not excluded by a proof. Numerically the cost rises above \(1\) on the area table; the
   rescaled limit would be a cohomogeneity-one metric with a flat bolt plane, and the needed statement is positivity of
   its cost per unit bolt area.
4. **Interior collapse/neck at finite radius**: necks that are almost Euclidean and enclose the bolt are excluded by
   Q′; other degenerate orbits are open.
5. **Large-volume excursion off the ACH curve**: excluded modulo the shadowing lemma and the face phase portrait (§2).
6. **Escape with a nonstandard CR structure**: excluded by Lemma P while the orbits stay in the block.
7. **Noncollapsed convergence** (none of 2–5): local smooth convergence to a complete diagonal \(g_\infty\) on \(O(-1)\)
   with \(\widehat P(g_\infty)\le p^{\rm diag}_{1,0}\); its tail lies in the block, so by Lemma P (uniform in \(j\), since
   \(\int_T^\infty dt/W_j\le4e^{-4T}/c\)) \(\widetilde\Phi_\infty(T)\to0\): \(g_\infty\) has the **standard** CR infinity.

**Theorem D (conditional structure theorem).** Assume the minimizing sequence avoids alternatives 2–4 (uniform bolt
bounds \(0<c\le b_j\le C\) and uniform orbit noncollapse on compact radii) and that its tails beyond a fixed \(T_0\) lie in
the ACH block. Then, granting the truncation lemma below, \(p^{\rm diag}_{1,0}\) is attained by a complete diagonal metric
\(g_\infty\) on \(O(-1)\) asymptotic to the standard CH end, and:

- if \(p^{\rm diag}_{1,0}>0\), \(g_\infty\) is a non-Einstein \(P\)-critical (in the diagonal class) complete cell;
- \(p^{\rm diag}_{1,0}=0\) **if and only if** there is a complete diagonal Einstein ACH metric on \(O(-1)\) with standard CR
  infinity (the "if" direction needs only the truncation lemma; the "only if" direction is the attainment).

*Truncation lemma (needed, sketched).* A complete diagonal metric with finite \(\widehat P\), in the block for \(t\ge T_0\)
with \(\widetilde\Phi\to0\), can be cut off to exact CH with cost change \(\to0\). In block coordinates the physical deviations
from CH are the stable modes of rates \(4,6\) (the rate-\(2\) direction is motion along CH itself, absorbed by matching
the radial origin and CH scale) plus the response to the control, which tends to zero because the local cost tends to
zero; a cut-off on \([R,R+1]\) then changes \(P\) by \(O(W(R)\,\mathrm{dev}(R)^2)=O(e^{4R}e^{-8R})\to0\). For \(P\) (as
opposed to \(J_6\)) no linear boundary term arises, so rate \(>2\) in \(C^2\) suffices. The written proof must make the
rate-2 matching and the forced response precise.

**Consequences for the research line.**

- In the diagonal class, the relation between positive gap, approximation, attained infimum and exact Einstein
  existence reduces (under the stated noncollapse) to one finite-dimensional dynamical question: does the
  one-parameter separatrix family of diagonal Einstein ACH fillings of \(O(-1)\) (bolt radius \(b\), anisotropy at the
  separatrix) ever reach \(\rho_\infty=1\)? The branch data (Step 15) give \(\rho_\infty\ge2.1897\) on
  \(b\in[0.138,400]\), rising to \(5.88\) at \(b=0.138\) and \(\approx1.343b\) at large \(b\), and the \(b=0.8\) fate enumeration
  finds only the mirror pair \(\rho,1/\rho\). A validated proof that \(\rho_\infty(b)\ne1\) for all \(b\) and both bolt-slot
  sectors, with the \(b\to0\) (Taub-bolt/Burns) and \(b\to\infty\) asymptotics handled analytically, would give
  \(p^{\rm diag}_{1,0}>0\) modulo alternatives 2–4.
- The escape branch therefore cannot be used to manufacture zero-cost diagonal cells from Theorem E; Theorem E is
  isolated from the standard-end cell problem in cost.
- The unresolved diagonal alternatives (collapsed connectors, large bolts, non-Euclidean interior necks) are exactly the
  collapse and concentration phenomena the closed problem must also control. The closed problem additionally needs
  actual-field identification of the CH bulk, assignment of several exceptional classes, interaction control, and
  passage from asymptotically-CH components to exact collars.

## 4. Status

Proved this step: identity (1.1) and Lemma P with its sharp linear constant; Corollary P1; the face reduction and its
\(q\)-independence. Numerical: the unstable-face fates. Conditional: Theorem D (needs truncation lemma, shadowing lemma,
and the noncollapse hypotheses). Open and decisive: the collapsed-connector branch, the large-bolt branch, and
\(\rho_\infty\ne1\) along the full diagonal Einstein separatrix family.



---

## Source step26_truncation_flux_and_branch_completeness.md

Original: [sources/Sessions/S1003A02/workspace/notes/step26_truncation_flux_and_branch_completeness.md](../sources/Sessions/S1003A02/workspace/notes/step26_truncation_flux_and_branch_completeness.md)

# Step 26 — Standard-CR truncation, Euler-flux collapse separation, and Einstein branch tests

Session S1003A02, Agent3. Conventions are those of Step 25: diagonal Bianchi IX metrics
\[
g=dt^2+\sum_{i=f,g,h}a_i^2\sigma_i^2,\qquad d\sigma_i=2\sigma_j\wedge\sigma_k,
\qquad W=a_fa_ga_h,
\]
with \(\int_{S^3}\sigma_{123}=2\pi^2\), \(\widehat P=P/(8\pi^2)\), normalized complex-hyperbolic Einstein constant \(\operatorname{Ric}=-6g\), and compact end variables \((y_f,y_g,y_h,\kappa,q,\zeta)\).

This note strengthens two parts of the conditional diagonal structure theorem and records what remains. The truncation direction is now reduced to explicit stable-mode estimates rather than an informal decay statement. For collapse, ordinary product/ALF Berger necks are separated from a developed Rossi interior by an exact Euler transgression; only a scale-invariant high-shear transition remains. The Einstein fate enumeration was also extended beyond \(b=.8\).

## 1. Independent reading of Lemma P

A two-branch TTCS verifier and peer S1003A01 independently checked the exact identity and constant. For every diagonal metric,
\[
\widetilde\Phi=q+\frac14(y_g-y_h)-\zeta\sinh q
\]
satisfies
\[
\widetilde\Phi'=F-\frac14(e_g-e_h),\qquad e_i=\operatorname{Ric}_{ii}+6,
\tag{1.1}
\]
where
\[
F=(y_g-y_h)\left(1-\frac{y_f+y_g+y_h}{4}-\zeta\cosh q\right)
+\zeta\sinh q\,(y_g+y_h-2)
+\frac{2\zeta^2}{\kappa^2}\sinh(2q).
\tag{1.2}
\]
The equality \(e_g-e_h=\operatorname{Ric}^\circ_{gg}-\operatorname{Ric}^\circ_{hh}\) is exact. In raw variables, \(F\) is not globally a regular multiple of \(\zeta^2\). In the ACH block coordinates of `ach_block_verify.py`, however, every transverse deviation is \(O(\zeta)\), and the exact symbolic computation in `ach_phi_drift.py` proves \(F=\zeta^2G\) with bounded polynomial/rational \(G\). This is the correct scope of the notation in Step 25.

Since
\[
P_I\ge \pi^2\int_IW(e_g-e_h)^2dt,
\]
weighted Cauchy--Schwarz gives
\[
\left|\Delta\widetilde\Phi-\int_IFdt\right|
\le\left(\frac{\widehat P_I}{2}\right)^{1/2}
\left(\int_I\frac{dt}{W}\right)^{1/2}.
\tag{1.3}
\]
All constants are correct. The peer check identified that the linear exterior null-line energy and Lemma P measure the **same** Rossi mismatch; they must not be added as separate charges. The script `squash_escape_cost.py` has one harmless output-only typo: the coefficient in \(w\sim e^{-4t}/8\) is extracted from \(we^{4t}\), not \(we^{-4t}\). Its numerical value function is unaffected.

A useful intrinsic block consequence, if \(y_g+y_h\ge c_B>0\) and \(\kappa\ge\kappa_{\min}>0\), is
\[
\widehat P_{[T,\infty)}\ge
4c_B\kappa_{\min}\frac{(|\widetilde\Phi(T)|-\delta(T))_+^2}{\zeta(T)^2},
\qquad
\delta(T)=\frac{\sup_B|G|}{2c_B}\zeta(T)^2.
\tag{1.4}
\]
This avoids choosing a radial origin. The earlier \(\frac12e^{4T}\) form follows from the stronger comparison \(W\ge ce^{4t}/16\).

## 2. The standard-CR truncation theorem

The TTCS verification computed the full spectrum at
\[
E(0)=(2,1,1,1,0,0):
\]
\[
\begin{array}{c|c|l}
\lambda&v_\lambda&\text{meaning}\\ \hline
 2&(4,-3,-3,5,0,0)&\text{outgoing Einstein mode},\\
 0&(0,0,0,0,1,0)&\text{Rossi/CR deformation},\\
 -2&(0,1,1,1,0,2)&\text{CH radial phase/defining-function mode},\\
 -4&(0,1,-1,0,-\tfrac12,0)&\text{physical antisymmetric mode},\\
 -6&(-4,1,1,1,0,0)&\text{physical symmetric mode},\\
 -8&(2,1,1,0,0,0)&\text{Einstein-constraint transverse mode}.
\end{array}
\tag{2.1}
\]
The exact CH orbit parametrized by \(z=\zeta\) is
\[
H(z)=\left(\sqrt{1+z}+\frac1{\sqrt{1+z}},\sqrt{1+z},\sqrt{1+z},\sqrt{1+z},0,z\right),
\tag{2.2}
\]
and \(H'(0)\) is half the \(-2\) vector. Thus the slow \(e^{-2t}\) mode is radial phase, not a physical metric perturbation. It must be matched exactly, rather than paid for in the splice.

For a non-Einstein scalar-\(-24\) end, the \(-8\) mode must be retained. If \(\mathcal C\) is the Einstein Hamiltonian constraint expression, then
\[
\mathcal C=e_0=-(e_f+e_g+e_h),\qquad e_0=\operatorname{Ric}_{tt}+6,
\tag{2.3}
\]
so this component is a forced response controlled by \(P\). The phrase in Step 25 that only rates \(4,6\) occur is exact for Einstein ends after phase matching, but not for general finite-\(P\), scalar-normalized ends.

**Theorem T (diagonal standard-CR truncation).** Let \(g\) be a complete diagonal metric whose tail remains in one sufficiently small standard ACH block. Assume
\[
s_g=-24,\qquad P(g)<\infty,\qquad \widetilde\Phi(t)\to0.
\]
Then there are diagonal metrics \(g_R\), equal to \(g\) on \(t\le R\) and exactly normalized CH on \(t\ge R+1\), such that
\[
P(g_R)\to P(g).
\tag{2.4}
\]
The same proof with \(J_6<\infty\) works without separately fixing scalar curvature, and gives \(J_6(g_R)\to J_6(g)\).

**Proof structure.** Subtract the exact CH state at the same \(\zeta\), so the \(-2\) phase is removed. Use transverse coordinates \(U,V_6,V_8,d,\widetilde\Phi\), with rates \(2,-6,-8,-4,0\). In the block, their controlled equations have the normal form
\[
V'=\Lambda V+N(\zeta,V)+B e,
\qquad |N|\le C(\zeta+|V|)|V|,
\tag{2.5}
\]
where \(e=(e_0,e_f,e_g,e_h)\). Since \(s=-24\),
\[
\widehat P_{\rm tail}=\frac14\int W\sum_\alpha e_\alpha^2dt,
\qquad W\asymp e^{4t},
\tag{2.6}
\]
so \(e^{2t}e_\alpha\in L^2\). Stable Duhamel formulas, the terminal integral formula for the bounded outgoing component, and (1.3) for the neutral component imply
\[
|U|+|V_6|+|V_8|+|d|+|\widetilde\Phi|=o(e^{-2t}).
\tag{2.7}
\]
Because \(\partial_q\widetilde\Phi=1-\zeta\cosh q\) stays positive, \(q=o(e^{-2t})\) too. For an Einstein end, \(e=0\), \(V_8=0\), and the stable-manifold expansion improves the physical deviation to \(O(e^{-4t})\).

Choose the CH radial phase so that its \(\zeta\) equals \(\zeta(R)\), and write \(D_i=\log a_i-\log a_i^{\rm CH}\). Then on a fixed interval,
\[
\sup_{[R,R+1]}(|D|+|D'|)=o(e^{-2R}).
\tag{2.8}
\]
Cut off \(D\) to zero on \([R,R+1]\). The diagonal Ricci formulas are affine in \(D''\), and the original \(D''\) is controlled by the residual equations. Therefore
\[
\int_{[R,R+1]\times S^3}|\operatorname{Ric}_{g_R}+6g_R|^2dV
\le C\int_R^{R+1}W|e|^2dt
+C\,W(R)\sup_{[R,R+1]}(|D|+|D'|)^2\to0.
\tag{2.9}
\]
The discarded tail has vanishing \(P\)-mass. This proves (2.4). The weakest useful fixed-width requirement is exactly the phase-matched \(o(e^{-2R})\) condition, plus vanishing weighted residual. No \(C^2\) decay assumption is needed separately.

This theorem closes the truncation direction in Theorem D once scalar normalization and block membership are stated. It also gives the correct logical implications:
\[
\text{standard-CR diagonal Einstein ACH filling}\Longrightarrow p_{1,0}^{\rm diag}=0,
\tag{2.10}
\]
and
\[
p_{1,0}^{\rm diag}=0+\text{attainment in the complete scalar-}(-24)\text{ class}
\Longrightarrow \operatorname{Ric}=-6g.
\tag{2.11}
\]
Zero infimum without compactness does not imply existence. Attainment occurs in the extended complete standard-CR ACH class; exact-CH-ended zero cost is impossible by exact-collar rigidity.

The Step-22 conformal barrier theorem has a different decay window: its Yamabe factor satisfies every rate \(4<m<2+2\sqrt3\), which is more than enough for its linear boundary transgressions. Theorem T uses a direct squared-residual splice and needs only physical rate greater than \(2\); the two thresholds are consistent and should not be conflated.

## 3. Euler flux and ordinary collapsed connectors

The TTCS generator proposed an Euler transgression. It was independently checked exactly against the Cartan curvature source. Define the intrinsic sectional curvature of a principal orbit by
\[
K^{(3)}_{jk}=
\frac{(a_j^2-a_k^2)^2+2a_i^2(a_j^2+a_k^2)-3a_i^4}
{a_i^2a_j^2a_k^2},\qquad \{i,j,k\}=\{f,g,h\},
\tag{3.1}
\]
and
\[
\mathfrak b=W\left(y_fK^{(3)}_{gh}+y_gK^{(3)}_{hf}+y_hK^{(3)}_{fg}-y_fy_gy_h\right).
\tag{3.2}
\]
The new script `workspace/scripts/verify_euler_flux_identity.py` imports the independent exact Cartan formulas and proves symbolically that on every diagonal annulus
\[
\widehat P(C)=\mathfrak b(t_1)-\mathfrak b(t_0)
+\frac1{4\pi^2}\int_C(|W^+|^2+|W^-|^2)
+\frac1{96\pi^2}\int_Cs^2.
\tag{3.3}
\]
The symbolic residual is exactly zero. It also verifies the normalization \(\mathfrak b=2\) on a Euclidean round sphere and
\[
\mathfrak b_{\rm CH}(t)=2-6\sinh^4t.
\tag{3.4}
\]
Thus
\[
\widehat P(C)\ge\mathfrak b(t_1)-\mathfrak b(t_0).
\tag{3.5}
\]

The script `workspace/scripts/ach_euler_flux.py` evaluated this flux on the validated Theorem-E transport. It verifies (3.4) symbolically and, using Arb on all 40 CAPD endpoint boxes at \(t=2.75\), proves
\[
\mathfrak b(T)\in[-64533.46135866161,-64275.41699256702].
\tag{3.6}
\]
The corresponding floating central value is \(-64403.79098545\); the same orbit has \(\widetilde\Phi\simeq0.78448\), so it has already acquired the Rossi infinity to within the validated tail drift \(<4.57\times10^{-4}\).

For a biaxial orbit \(a_g=a_h=A\), \(a_f=B\), let \(\lambda=B/A\), \(U=A'\), and \(V=A(B'/B)\). Then
\[
\mathfrak b=\lambda\left[V(4-3\lambda^2-U^2)+2U\lambda^2\right].
\tag{3.7}
\]
Hence a quasi-product Berger neck has \(\mathfrak b\approx0\), and an ALF neck with \(A\sim R\), \(B\to m\) has \(\lambda\to0\), \(U\to1\), \(V\to0\), again \(\mathfrak b\to0\). Any connector that evolves **outward** from the developed Rossi orbit (3.6) to such a neck pays at least about \(6.4\times10^4\) in units \(8\pi^2\), enormously above the certified \(0.99585\) cell cost.

This establishes a useful curved-neck extension of Lemma Q' for a natural class: collapse does not remove the charge of a developed ACH region when the later neck becomes quasi-product or ALF. The conclusion is scale invariant; shrinking the whole configuration does not change \(\mathfrak b\).

The remaining collapsed connector is much more specific: it must keep \(\mathfrak b\) highly negative by developing large normalized second fundamental form, rather than pass through an ordinary Berger or ALF regime. In volume/shape variables
\[
a_f=re^{2\beta/3},\quad a_g=re^{-\beta/3+q/2},\quad a_h=re^{-\beta/3-q/2},\quad h=\log r,
\tag{3.8}
\]
the diagonal defect has the exact scale-invariant action
\[
\widehat P=\int r^3\left(\frac3{16}H^2+\frac16E^2+\frac18D^2\right)dt,
\tag{3.9}
\]
where \(D=R_{gg}-R_{hh}\), \(E=R_{ff}-(R_{gg}+R_{hh})/2\), and \(H=R_{00}-(R_{ff}+R_{gg}+R_{hh})/3\). Under \(t=\varepsilon x\), \(r=\varepsilon R\), this action is unchanged. Thus small orbit volume alone does not make the high-shear connector cheap. The exact control equations supplied by TTCS are preserved in `trace/ttcs/results/step26_ttcs01_generator1_integration.md`; they should be independently symbolically checked before being promoted to a theorem.

Scientific consequence: the target configuration “Rossi Einstein interior + small ordinary Berger/ALF neck + standard CH exterior” is excluded. A possible cheap collapsed reset must occur **before** the orbit reaches a developed ACH state, or must follow a singular high-shear trajectory that never enters a product/ALF neck after the Rossi state. This is a much narrower branch than the generic Taub-bolt language suggested.

## 4. Einstein branch completeness tests

`workspace/scripts/ach_fate_enum.py` was run at additional bolt radii. The finite signed logarithmic \(d\)-grid is the same as at \(b=.8\); the computations are floating classification tests, not exhaustive interval proofs.

At \(b=.35\), the four fate changes are:
- a mirror ACH1/ACH2 pair at \(d=\pm0.00469762690656\), with \(\rho=2.808059256\) and reciprocal;
- remote SING/OTHER boundaries at \(|d|\approx4.37263\), whose closest ACH deviations exceed \(2.28\).
No ACH3 branch is approached.

At \(b=.2\), the same topology appears:
- a mirror ACH1/ACH2 pair at \(d=\pm6.16704965495\times10^{-6}\), with the positive branch approaching ACH1 to \(3.38\times10^{-5}\) and \(\rho\approx4.2387822\) (the finite closest-approach readout is less accurate than the projected section method);
- remote SING/OTHER boundaries at \(|d|\approx0.45038\), whose closest ACH deviations exceed \(3.14\).
Again there is no ACH3 approach.

At \(b=2\), the four fate changes again consist of the mirror ACH1/ACH2 pair at \(d=\pm1.55505759790\), with positive-branch closest-approach \(\rho\approx3.1718171\), plus remote SING/OTHER boundaries at \(|d|\approx59.2108\); every ACH3 deviation is at least \(1.0009\). At \(b=20\), the mirror pair is at \(d=\pm18.0795443515\), with \(\rho\approx26.951825\), while the remote boundaries lie at \(|d|\approx606.871\); every ACH3 deviation is at least \(1.043\). The large-b value agrees with the existing asymptotic \(\rho\sim1.343b\).

Together with the existing \(b=.8\) enumeration, these tests support one mirror perpendicular ACH pair and no aligned ACH branch across \(b=.2,.35,.8,2,20\). They also correct the earlier impression that the perpendicular branch starts near \(b=.29\): the branch persists at \(b=.2\), but \(d_*\) becomes extremely small and \(\rho\) grows. These runs do not prove branch completeness because a finite grid can miss a narrow double transition, and the labels OTHER/SING depend on finite-time thresholds. The proper next proof is interval fate enclosure plus asymptotics as \(b\to0,\infty\), not more root scans based on the flawed unstable-coordinate sign test.

## 5. Revised diagonal structure statement

With Theorem T, the noncollapsed standard-tail part of Theorem D no longer depends on an unspecified truncation assertion. The remaining hypotheses are:
1. scalar normalization or finite \(J_6\);
2. a common ACH block for the tails;
3. genuine compact-state and curvature bounds at the bolt and on compact intervals, not merely lower bolt/orbit-radius bounds;
4. exclusion of high-shear collapse/interior necks and large-bolt escape;
5. a validated no-return statement for large-volume face excursions.

Under these hypotheses, a minimizing sequence converges to a complete standard-CR diagonal minimizer in the extended ACH class, and its value equals the exact-ended infimum by Theorem T. The equivalence between zero value and a standard-CR diagonal Einstein filling then follows only with attainment. Theorem E cannot supply such a filling by late, large-volume CR correction; ordinary post-Rossi Berger/ALF collapse is now also excluded by (3.5)--(3.7). The hard residual geometry is the high-shear scale-invariant connector, together with the large-bolt and phase-portrait branches.

## 6. Files and status

New exact/checking files:
- `workspace/scripts/verify_euler_flux_identity.py`: exact Cartan verification of (3.3), residual zero.
- `workspace/scripts/ach_euler_flux.py`.
- `workspace/data/ach_capd/euler_flux_b0.8.json`: symbolic CH/Euclidean checks, floating trajectory profile, and Arb enclosure (3.6).
- `workspace/data/ach_fate/fate_b0.2.json`, `fate_b0.35.json`, `fate_b2.json`, `fate_b20.json`.
- TTCS integration: `trace/ttcs/results/step26_ttcs01_verifier1_integration.md` and `step26_ttcs01_generator1_integration.md`.

Proved or reduced to explicit estimates this step: Lemma-P scope and constants; mode classification; phase-matched truncation theorem for scalar-\(-24\) diagonal ends; exact Euler-flux identity; certified flux of the validated Rossi filling; exclusion of post-developed-Rossi product/ALF connectors.

Still open: an independently checked coercive lower bound for the high-shear action; validated global face portrait/shadowing; complete interval enumeration of all Einstein ACH branches for every bolt radius; large-bolt coercivity; unrestricted non-diagonal collapse.



---

## Source step27_chiral_transgression_and_small_bolt.md

Original: [sources/Sessions/S1003A02/workspace/notes/step27_chiral_transgression_and_small_bolt.md](../sources/Sessions/S1003A02/workspace/notes/step27_chiral_transgression_and_small_bolt.md)

# Step 27 — Chiral Euler transgressions, sharp blow-up/neck charges, and the small-bolt Einstein structure

Session S1003A02, Agent2. Conventions: diagonal Bianchi-IX metrics
\(g=dt^2+a^2\sigma_1^2+b^2\sigma_2^2+c^2\sigma_3^2\), \(d\sigma_i=2\sigma_j\wedge\sigma_k\), \(\int_{S^3}\sigma_{123}=2\pi^2\),
\(W=abc\), \(\widehat P=P/(8\pi^2)=\int W|\mathrm{Ric}^\circ|^2dt/4\). Block norms \(B_A=\operatorname{tr}W_A^2\), \(B_B=\operatorname{tr}W_B^2\)
of the two chiral \(3\times3\) Weyl blocks are taken from the independent Cartan module
`Sessions/S1003A01/workspace/scripts/perp_cartan_verify.py`, in the convention of `verify_euler_flux_identity.py`
(\(\frac1{4\pi^2}\int|W|^2\leftrightarrow\int W(B_A+B_B)/2\,dt\)).

Scripts and data: `workspace/scripts/chiral_flux_identity.py` → `workspace/data/chiral_flux.json`;
`workspace/scripts/chiral_flux_models.py` → `workspace/data/chiral_flux_models.json`;
`workspace/scripts/small_b_separatrix_fit.py` → `workspace/data/small_b_separatrix_fit.json`;
new fate records `workspace/data/ach_fate/fate_b0.1.json`, `fate_b0.14.json`.

## 1. The chiral transgression theorem

Step 26 found the Euler flux \(\mathfrak b\) with \(\widehat P(C)=\Delta\mathfrak b+\frac1{4\pi^2}\int_C|W|^2+\frac1{96\pi^2}\int_Cs^2\).
The Euler flux alone cannot see which Weyl chirality is created or deleted, and that is exactly the information
that controls blow-up cells (Theorem C: the cost channel is \(4\Delta W_+\)). The missing object is the signature
transgression.

**Theorem X (chiral transgressions).** Let \(p_i=a_i'\), \(\gamma_i=(a_j^2+a_k^2-a_i^2)/(a_ja_k)\). There is an explicit
scale-invariant polynomial \(\mathfrak s\) in \(p_i\) with coefficients rational of degree zero in \(a_i\)
(the exact formula is the field `S` of `data/chiral_flux.json`, normalized here by \(\mathfrak s=S-6\); the raw JSON `bA,bB` fields use the unshifted `S`, so the normalized charges are `bA+6,bB-6`) such that
\[
\mathfrak s'=\tfrac12W(B_A-B_B)
\]
identically on all 2-jets. Put \(\mathfrak b_\pm=\mathfrak b\mp\mathfrak s\). Then for every diagonal annulus \(C=[t_0,t_1]\)
\[
\boxed{\ \widehat P(C)=\mathfrak b_\pm(t_1)-\mathfrak b_\pm(t_0)+\frac1{2\pi^2}\int_C|W^\pm|^2+\frac1{96\pi^2}\int_Cs^2\ }
\tag{1.1}
\]
where \(W^+\) is block \(A\), the block that carries the Kähler Weyl curvature of complex hyperbolic space in this frame.

*Proof.* `chiral_flux_identity.py` solves the linear system for a general 84-term ansatz
(\(\sum_{|\alpha|\le3}p^\alpha\cdot\) polynomial in \(\gamma\) of degree \(\le3-|\alpha|\)) against the Cartan-derived
\(W(B_A-B_B)/2\). The solution is unique up to the additive constant; the symbolic residual of \(\mathfrak s'\) is \(0\).
Both chiral identities (1.1) are then verified with exact residual \(0\) against the independent
\(|\mathrm{Ric}^\circ|^2\) and \(s\) of the Cartan module. \(\square\)

The normalization \(\mathfrak s=0\) at a smooth centre is the one for which (1.1) is the localization of the
Hitchin–Thorpe densities \(4\pi^2(2\chi\pm3\tau)=\int(2|W^\pm|^2+s^2/24-|\mathrm{Ric}^\circ|^2/2)\) (up to the factor 2 in
\(\widehat P\)): on a closed manifold \(\widehat P=\frac1{2\pi^2}\int|W^\pm|^2+\frac1{96\pi^2}\int s^2-(2\chi\pm3\tau)\).

### Charges (exact, `chiral_flux.json`, `chiral_flux_models.json`)

| orbit type | \(\mathfrak b\) | \(\mathfrak b_+\) | \(\mathfrak b_-\) |
|---|---|---|---|
| smooth centre (round, \(a_i\sim t\)) | 2 | 2 | 2 |
| regular bolt of \(O(-1)\) (any \(b\), any triaxial jet) | 4 | 1 | 7 |
| biaxial or controlled near-biaxial Hopf-collapsed Berger orbit, fibre \(\varepsilon\to0\), bounded normalized jets | 0 | −2 | 2 |
| CH orbit at radius \(t\) (\(\mathrm{Ric}=-6\)) | \(2-6\sinh^4t\) | \(2-9\sinh^4t\) | \(2-3\sinh^4t\) |
| real-hyperbolic orbit (any normalization) | \(\mathfrak b_{H}\) | \(\mathfrak b_H\) | \(\mathfrak b_H\) |

The bolt row is \(2\chi\pm3\tau\) for the disc bundle with \(\chi=2,\tau=-1\): the frame orientation in which CH
is Kähler with \(W^+\neq0\) is automatically the orientation in which the bolt has self-intersection \(-1\). This is
the blow-up orientation, confirmed independently by the frame, not imposed. The collapsed Berger value is exact:
\[
\mathfrak s=2+\frac{\varepsilon^2}{R^2}\Bigl(U^2-2UV+V^2-4\Bigr)+\frac{2\varepsilon^4}{R^4},\qquad
\mathfrak b=-\frac{\varepsilon}{R}\Bigl(U^2V-4V\Bigr)+O(\varepsilon^3/R^3)
\]
for \(a=\varepsilon\) (fibre), \(b=c=R\), \(b'=c'=U\), \(a'/a=V/R\); the formula is symmetric under the choice of the
collapsing slot.

**Collapse asymmetry.** Under Hopf collapse with bounded normalized geometry the Euler flux tends to \(0\), but the
signature transgression tends to the nonzero adiabatic value \(\mathfrak s\to2\). For unrestricted anisotropic collapsed jets the charge acquires shear terms and need not equal \((-2,2)\). This is the cohomogeneity-one form of
the fact used by Cheeger–Tian: the Chern–Gauss–Bonnet boundary term vanishes on collapsed boundaries with
bounded geometry, while the \(\eta\)/Chern–Simons term does not. The chiral fluxes therefore assign a definite
charge \((-2,2)\) to every collapsed neck; a collapsed neck is invisible to \(\mathfrak b\) but not to \(\mathfrak b_\pm\).

### Model checks

* **Burns** (\(a=b=r,\ c=r\sqrt{1-m/r^2},\ dt=dr/\sqrt{1-m/r^2}\)): exactly \(s=0\), \(B_A=0\) (ASD in the blow-up
  orientation), \(B_B=24/r^8\), \(|\mathrm{Ric}^\circ|^2=16/r^8\). Charges: \(\mathfrak b_+\) goes from \(1\) to \(2\), \(\mathfrak b_-\) from \(7\) to \(2\);
  \(\int WB_A=0\), \(\int WB_B=6\). Hence \(\widehat P(\mathrm{Burns})=2-1=1\) with every non-flux term in the \(+\) identity zero.
* **Taub-bolt** (\(a=b=2\sqrt{r^2-n^2}\), \(c=4n\sqrt V\), \(V=(r^2-\frac52nr+n^2)/(r^2-n^2)\), bolt \(r=2n\)): Ricci-flat, regular
  on \(O(-1)\) in the blow-up orientation. With \(n=1\), \(B_A=\frac{243}{8(r+1)^6}\) and \(B_B=\frac3{8(r-1)^6}\). The charges run from \((1,7)\) at
  the bolt to the collapsed value \((-2,2)\) at the ALF end, and the quadratures give \(\int WB_A=3.000\), \(\int WB_B=5.000\).
  So there is no orientation obstruction: Taub-bolt is a legitimate zero-cost core for the \((-1)\)-class, and it
  converts the bolt charge into the collapsed-neck charge with \(\frac1{2\pi^2}\int|W^+|^2=3\) and \(\frac1{2\pi^2}\int|W^-|^2=5\).
* CH, H\(^4\), Euclidean profiles are exact closed forms (table above). In H\(^4\) both blocks vanish and \(\mathfrak s\equiv0\).

## 2. Consequences for blow-up cells

From (1.1), every non-flux term is nonnegative, so for every \(t_0<t_1\)
\[
\widehat P[t_0,t_1]\ \ge\ \mathfrak b_+(t_1)-\mathfrak b_+(t_0)+\frac1{96\pi^2}\int_{[t_0,t_1]}s^2,
\qquad\text{and the same for }\mathfrak b_-.
\tag{2.1}
\]
The total upward variation of each chiral flux along a cell is at most \(\widehat P\).

**Corollary X1 (sharp bubble inequality, Burns-extremal).** For any diagonal metric on the disc bundle of
\(O(-1)\) and any orbit \(t\),
\[
\widehat P[0,t]\ \ge\ \mathfrak b_+(t)-1 .
\]
If the orbit at \(t\) is \(C^1\)-close in scale-normalized sense to a round Euclidean sphere, then \(\mathfrak b_+(t)=2-O(\delta)\) and
\(\widehat P[0,t]\ge1-O(\delta)\). Burns attains equality at every \(t\), since \(W^+\equiv0\) and \(s\equiv0\); its total is \(\widehat P=1\). This replaces Lemma Q′:
no almost-flatness of an annulus is needed, only the 1-jet of a single orbit, and the constant is sharp with an
explicit extremal. It also states the mechanism of Burns cost: the whole \(8\pi^2\) is the \(+\)-chiral charge
difference \(2-1\), paid with \(W^+\equiv0\) and \(s\equiv0\).

**Corollary X2 (nothing in a subthreshold cell is round).** If \(\widehat P(g)<1\) then \(\mathfrak b_+(t)<1+\widehat P<2\) for all \(t\). No orbit
of a subthreshold cell is close to a round Euclidean sphere, whatever its scale. A CH orbit at radius \(\tau\) has
\(\mathfrak b_+=2-9\sinh^4\tau\); compatibility requires \(\sinh^4\tau\ge(1-\widehat P)/9\), so sufficiently small positive CH radii are also excluded. This is
the global form of the statement that cheap cells must be glued into curved bulk.

**Corollary X3 (decollapse price).** Passing from a Hopf-collapsed orbit (\(\mathfrak b_+\approx-2\)) to an orbit with
\(\mathfrak b_+=\beta\) costs at least \(\beta+2\). In particular:
* to a round Euclidean orbit: at least \(4\);
* to a CH-like orbit of radius \(\tau\): at least \(4-9\sinh^4\tau\), which exceeds \(1\) for \(\sinh\tau<3^{-1/4}\), i.e. \(\tau<0.700\).

Thus a subthreshold cell with a Taub-bolt-type collapsed core cannot open into CH-like geometry inside CH radius
\(0.70\). It must remain collapsed out to scale one, or open through geometry that is not CH-like.

**Corollary X4 (bolt bubbles).** Let \(g_n\) be diagonal cells with \(\widehat P(g_n)\le1-\eta\) and bolt radius \(b_n\to0\). Rescaled by \(b_n\), any
noncollapsed limit region is a complete diagonal metric on \(O(-1)\) with \(s\equiv0\) and \(\widehat P\le1-\eta\), so its far orbits
satisfy \(\mathfrak b_+\le 2-\eta\) and cannot be asymptotically round. Its end is therefore not ALE. If it is Ricci-flat (the
\(\widehat P\to0\) case) with Hopf-collapsed ALF end, the charge balance is exactly the Taub-bolt one: \(\frac1{2\pi^2}\int|W^+|^2=3\),
\(\frac1{2\pi^2}\int|W^-|^2=5\). The scale-separated ALE bubble is excluded for every inner geometry, recovering
Step 25's exclusion with the sharp constant.

### Relation to Theorem C and to the absolute cell channel

Applying (1.1)\(_+\) to the whole exact-CH-ended cell and subtracting the CH ball (charges \(1\) versus \(2\) at the origin)
gives, for \(s\equiv-24\),
\[
\widehat P_{\rm cell}=1+\frac1{2\pi^2}\Delta_{\rm ren}\!\int|W^+|^2+12\,\Delta_{\rm ren}\!\int W\,dt
\;=\;1+\frac{4\Delta W_++48\,\mathrm{RV}}{8\pi^2},
\]
which is Theorem C at the Yamabe-normalized representative. The \(-\) identity gives the relative-signature form
\(\widehat P_{\rm cell}=-5+\frac1{2\pi^2}\int|W^-|^2+48\mathrm{RV}/(8\pi^2)\). Theorem X localizes both: the cell channel is now the
running quantity
\[
\Pi_+(t)=\mathfrak b_+(t)-1+\frac1{2\pi^2}\int_0^t|W^+|^2+\frac1{96\pi^2}\int_0^ts^2=\widehat P[0,t],
\]
and the question \(p_{1,0}>0\) asks whether the \(+\)-charge can be driven from \(1\) to the CH profile with a total deletion of
\(\int|W^+|^2+\frac1{48}\int s^2\) relative to the ball approaching \(2\pi^2\) (in the \(\frac1{2\pi^2}\) normalization, one unit).

## 3. The small-bolt Einstein regime: Taub-bolt core, collapsed AdS-Taub-NUT neck, saturation

New fate enumerations at \(b=0.14\) and \(b=0.1\) (`fate_b0.14.json`, `fate_b0.1.json`) have the same four-transition topology
as \(b=.2,.35,.8,2,20\): one mirror perpendicular ACH1/ACH2 pair and two remote SING/OTHER boundaries; ACH3 deviations
stay above \(1.29\). At \(b=0.14\), \(d_*=4.4934\times10^{-9}\), closest ACH approach \(1.8\times10^{-3}\), \(\rho\approx5.809\). At \(b=0.1\) the separatrix is at
\(|d|\lesssim3\times10^{-13}\), at the floating resolution of the grid; its readout (\(\rho\approx8.1\), closest approach \(0.31\)) is not resolved.

**Mechanism.** As \(b\to0\) the rescaled biaxial Einstein bolt solution converges to Taub-bolt (§1), whose ALF circle
has length parameter \(c\to4n\) with \(n=b/(2\sqrt3)\). At scale one the circle remains collapsed and the solution follows the
\(n\to0\) Λ-Taub-NUT form, \(c\simeq4n\cosh(\sqrt2\,t)\), \(a\simeq b\simeq\sinh(\sqrt2t)/\sqrt2\) (Ric \(=-6g\)). On a Berger orbit with fibre
\(c=\varepsilon\), the triaxial mode \(q=\log(a/b)\) satisfies, from the exact Ricci formulas,
\[
\mathrm{Ric}_{aa}-\mathrm{Ric}_{bb}=-(q''+\theta q')+\frac{16}{\varepsilon^2}q+O(q/R^2,q^2),
\]
so the Einstein condition makes it grow at rate \(4/\varepsilon\). The separatrix needs the initial anisotropy to be amplified
to order one exactly once, so
\[
\log\frac1{d_*}\simeq4\int\frac{dt}{c}=\frac{4}{4n}\int_0^\infty\frac{dt}{\cosh\sqrt2t}=\frac{\pi}{2\sqrt2\,n}
=\frac{\pi\sqrt{3/2}}{b}=\frac{3.84765}{b},
\]
up to logarithmic corrections from the bolt region where \(c\sim t\).

**Test.** A fit of \(\log d_*=-\kappa/b+\gamma\log b+c_0\) to \(b=.14,.2,.35\) gives \(\kappa=3.8543\), versus the predicted \(3.8476\) (0.17%), with
\(\gamma=-2.90\). With \(\kappa\) fixed to the prediction, the residuals are \(\le2\times10^{-3}\) and \(\gamma=-2.871\). The prediction also places \(d_*(0.1)\approx2\times10^{-13}\),
consistent with the unresolved bracket. The Rossi readout satisfies \(\rho b=0.983,0.848,0.813\) at \(b=.35,.2,.14\). This is
consistent with \(\rho\simeq c_*/b\), \(c_*\approx0.8\): the contact plane of the eventual ACH end (slots \(b\) and \(c\) when slot \(a\) becomes
the CH fibre) inherits the ratio between a base direction and the collapsed Taub-bolt circle, frozen at the saturation
radius where \(W\) is already large (Lemma P).

**Consequences.**
1. The small-\(b\) end of the Einstein branch has \(\rho\to\infty\), so \(\rho_\infty(b)\neq1\) there is explained by a matched
   three-region structure: a Taub-bolt core at scale \(b\), a collapsed Λ-Taub-NUT neck with circle \(\simeq4n\cosh\sqrt2t\), and a
   saturation/ACH region at scale one. A proof needs a rigorous version of this matching (Fenichel/exchange-lemma
   type estimates along the collapsed slow manifold) together with the large-\(b\) law \(\rho\sim1.343b\). Validated interval
   computation then covers the compact middle range.
2. The cell-side collapsed branch has the same geometry. A cheap cell with a Taub-bolt-type core reaches charge
   \((-2,2)\) for free, but then (X3) cannot open into CH-like geometry before CH radius \(0.70\). If it stays collapsed, its
   natural Einstein continuation lands on Rossi \(\rho\sim0.8/b\gg1\), and Lemma P charges the CR correction wherever \(W\) is large. A
   cheap standard-CR cell along this branch must therefore perform the CR correction inside the collapsed neck itself,
   where \(\int dt/W\) is large. That is exactly where the Einstein dynamics of \(q\) is exponentially unstable with rate
   \(4/\varepsilon\), and the free drift \(F\) of Lemma P is of size \(q/\varepsilon\). The residual collapsed problem is therefore a
   single, well-posed linear-quadratic control problem: steer the unstable \(q\)-mode on the collapsed slow manifold so
   that its saturated value gives standard CR, with cost \(\int W\,(\mathrm{Ric}_{aa}-\mathrm{Ric}_{bb})^2/8\). Its value as \(b\to0\) is the
   cell-side quantity that decides this branch.

## 4. Cheeger–Tian and the closed-manifold transfer

The retrieved account of Cheeger–Tian (Ge–Jiang, arXiv 1707.05511, Theorem 1.1 and Theorem 3.4 [ChTi06, Li])
gives ε-regularity for Einstein 4-manifolds without a volume bound, \(\int_{B_r}|\mathrm{Rm}|^2\le\varepsilon\Rightarrow|\mathrm{Rm}|\le Cr^{-2}\) on
\(B_{r/2}\). The key curvature estimate (Theorem 3.4) needs a **pointwise** Ricci bound \(|\mathrm{Ric}|\le3\), and its proof uses
chopping/N-structures, the Chern–Gauss–Bonnet transgression and almost-cone rigidity. Ge–Jiang §5.2 shows that the
estimate fails for critical metrics, \(\Delta\mathrm{Ric}=\mathrm{Rm}*\mathrm{Ric}\): scalar-flat Kähler products \(N_a\times S^2_a\), with \(N\) a cusped
hyperbolic surface, have arbitrarily small local \(L^2\) curvature and curvature \(a^{-2}\). Remark 5.4 there notes that bounded
Ricci is necessary.

The transfer to closed near-minimizers is therefore precise. An \(L^2\) Ricci-defect bound alone cannot yield
Cheeger–Tian regularity; the Ge–Jiang examples are critical metrics, but they are not near-Einstein in
\(\widehat P\), so they do not contradict a \(\widehat P\)-small version. The usable statement has the form of Theorem X: the
Euler transgression vanishes on collapsed boundaries with bounded geometry, while the signature transgression keeps
an adiabatic charge (here \(\mathfrak s\to2\)). In the diagonal class, cohomogeneity one replaces the pointwise Ricci bound,
because (1.1) holds exactly with no regularity input. A closed-manifold analogue must supply either a pointwise
Ricci bound on the collapsed region (for example from a selection principle) or a substitute for the 1-dimensional
structure, such as an F-structure along which the transgressions can be integrated.

## 5. Status

Proved this step (exact symbolic): Theorem X, the charge table, the Burns and Taub-bolt charge balances, and
Corollaries X1–X4 as consequences of (1.1).

Numerical and asymptotic, not yet a proof:
* the small-\(b\) law \(\log(1/d_*)\sim\pi\sqrt{3/2}/b\), with its derivation from the collapsed \(q\)-mode;
* \(\rho b\to c_*\approx0.8\);
* branch topology at \(b=0.1,0.14\).

Open:
* rigorous matching for \(b\to0\) and \(b\to\infty\);
* the collapsed-neck CR-control problem of §3(2);
* the high-shear (Kasner-type) connector of Step 26, for which (1.1) gives no obstruction while \(\mathfrak b\) decreases;
* face no-return;
* compact-state control near the bolt.



---

## Source step28_saturation_control_and_revised_diagonal_structure.md

Original: [sources/Sessions/S1003A02/workspace/notes/step28_saturation_control_and_revised_diagonal_structure.md](../sources/Sessions/S1003A02/workspace/notes/step28_saturation_control_and_revised_diagonal_structure.md)

# Step 28 — Scale-free saturation control and the revised diagonal structure theorem

Conventions are those of Steps 25–27.  The exact cost is
\[
\widehat P=\frac{P}{8\pi^2}=\int W\,|\operatorname{Ric}^\circ|^2/4\,dt,
\qquad W=a_fa_ga_h.
\]
The purpose of this Step was to turn the remaining collapsed branch into a single executable problem rather than continue pricing the long small-volume neck, and to make Theorem D depend only on the geometric escape mechanisms that remain.

## 1. Independent verification and corrections to Theorem X

Two TTCS verifier branches independently read the Cartan source, the transgression scripts, the data, and the Step-27 theorem note.  The integrated direct derivation is in
`trace/ttcs/results/step28_ttcs01_verifier1_integration.md`.

The substantive theorem is verified.  With
\[
\gamma_i=\frac{a_j^2+a_k^2-a_i^2}{a_ja_k},\qquad p_i=a_i',
\]
the long symbolic answer simplifies to
\[
S_0=\sum_i p_i^2-\sum_{\rm cyc}\gamma_i p_jp_k+2\sum_i\gamma_i^2,
\qquad \mathfrak s=S_0-6,
\]
and the algebraic identity
\[
\sum_i\gamma_i^2+\gamma_1\gamma_2\gamma_3=4
\]
gives directly
\[
\mathfrak s'=\frac W2(B_+-B_-).
\]
Here block A is genuinely \(W^+\): its basis consists of the self-dual forms \((e^{01}+e^{23})/\sqrt2\), etc.; on complex hyperbolic space its eigenvalues are \((-4,2,2)\), while the other block vanishes.  Burns has self-dual Kähler form in the same frame orientation, and the exceptional sphere has square \(-1\).  Thus the CH complex orientation and the blow-up orientation agree.

The localized identities are therefore
\[
\widehat P(C)=\Delta\mathfrak b_+
 +\frac1{2\pi^2}\int_C|W^+|^2
 +\frac1{96\pi^2}\int_Cs^2,
\]
\[
\widehat P(C)=\Delta\mathfrak b_-
 +\frac1{2\pi^2}\int_C|W^-|^2
 +\frac1{96\pi^2}\int_Cs^2.
\]
The centre, bolt, CH, Burns and Taub-bolt charge calculations are correct.  In particular Burns realizes \((1,7)\to(2,2)\) with \(\widehat P=1\), and Ricci-flat Taub-bolt realizes \((1,7)\to(-2,2)\) with chiral energies \(3,5\).

Three repairs were inserted in `step27_chiral_transgression_and_small_bolt.md`:

1. the Chern–Weil prefactor is \(4\pi^2(2\chi\pm3\tau)\), not \(8\pi^2(2\chi\pm3\tau)\);
2. `data/chiral_flux.json` stores unshifted \(S_0\), so its raw `bA,bB` become normalized charges only after `bA+6,bB-6`;
3. the limit \((-2,2)\) applies to biaxial or controlled near-biaxial Berger collapse.  Anisotropic collapsed jets contain extra shear contributions and cannot be assigned this charge without further control.

The Corollary-X2 prose was also corrected: for a CH-shaped orbit, subthreshold compatibility requires \(\sinh^4\tau\ge(1-\widehat P)/9\); not every positive radius is allowed.

## 2. Exact scale-free full-control problem

Write
\[
a_f=re^{2\beta/3},\qquad
 a_g=re^{-\beta/3+q/2},\qquad
 a_h=re^{-\beta/3-q/2},\qquad h=\log r.
\]
Let
\[
D=R_{gg}-R_{hh},\quad
E=R_{ff}-\frac{R_{gg}+R_{hh}}2,\quad
H=R_{00}-\frac{R_{ff}+R_{gg}+R_{hh}}3.
\]
Then
\[
\begin{aligned}
D&=-q''-3h'q'+e^{-2h}\mathcal V_D,\\
E&=-\beta''-3h'\beta'+e^{-2h}\mathcal V_E,\\
H&=-2h''-\frac23(\beta')^2-\frac12(q')^2+e^{-2h}\mathcal V_H,
\end{aligned}
\]
with
\[
\begin{aligned}
\mathcal V_D&=8(e^{-4\beta/3}\sinh2q-e^{2\beta/3}\sinh q),\\
\mathcal V_E&=4e^{8\beta/3}-4e^{2\beta/3}\cosh q-8e^{-4\beta/3}\sinh^2q,\\
\mathcal V_H&=\frac23e^{8\beta/3}-\frac83e^{2\beta/3}\cosh q
 +\frac83e^{-4\beta/3}\sinh^2q.
\end{aligned}
\]
The full action is exactly
\[
\widehat P=\int r^3\left(\frac3{16}H^2+\frac16E^2+\frac18D^2\right)dt.
\tag{2.1}
\]
The independent randomized check `scripts/check_shape_control_jax.py` compared these formulas against the exact diagonal Ricci equations at 10,000 random two-jets and found maximum absolute error \(3.98\times10^{-13}\).  A direct full symbolic substitution script was also written but proved too expensive; it timed out rather than producing evidence.

Set
\[
d\tau=dt/r,
\quad p=rh',\quad \xi=r\beta',\quad \eta=rq',
\quad (\bar H,\bar E,\bar D)=r^2(H,E,D).
\]
Then, for \(Y=(\beta,q,p,\xi,\eta)\),
\[
\begin{aligned}
\dot\beta&=\xi,&\dot q&=\eta,\\
\dot p&=p^2-\xi^2/3-\eta^2/4+\mathcal V_H/2-\bar H/2,\\
\dot\xi&=-2p\xi+\mathcal V_E-\bar E,\\
\dot\eta&=-2p\eta+\mathcal V_D-\bar D,
\end{aligned}
\tag{2.2}
\]
and
\[
\widehat P=\int\left(\frac3{16}\bar H^2+\frac16\bar E^2+\frac18\bar D^2\right)d\tau.
\tag{2.3}
\]
All absolute scale has disappeared.  This establishes the strategist's central point: the long collapsed neck does not carry a new \(b\)-dependent price.  The decisive object is a scale-one saturation map.

For numerical work, regularize collapse by
\[
x=\beta-q/2=\log(a_f/a_g),\qquad z=e^{-q/3}=(a_h/a_g)^{1/3},
\qquad \chi=\xi-\eta/2.
\]
The Taub-bolt/\(\Lambda\)-Taub-NUT entry ray at a scale-one base radius \(A\) is
\[
I_\varepsilon(A)=\left(
 x=0,
 z=\varepsilon^{1/3},
 p=z(2U+V)/3,
 \chi=0,
 \eta=z(U-V)
\right),
\]
where
\[
U=\sqrt{1+2A^2},\qquad V=\frac{2A^2}{\sqrt{1+2A^2}}.
\]
This retains the first-jet matching and does not enlarge the entry set to arbitrary Berger data.

The target is the nonlinear standard-CR stable set of the uncontrolled Einstein compact flow, on a fixed section such as \(\zeta=10^{-2}\).  It is not characterized by the finite formula \(\widetilde\Phi=0\) alone: one also needs the Hamiltonian constraint, absence of the nonlinear outgoing mode, and limiting \(\Phi_\infty=0\).  The mathematical value is
\[
\mathcal V_{\rm sat}
=\liminf_{\varepsilon\downarrow0}\inf
 \int\left(\frac3{16}\bar H^2+\frac16\bar E^2+\frac18\bar D^2\right)d\tau,
\tag{2.4}
\]
over solutions of (2.2) joining the entry ray to that stable set.

The full derivation, terminal map, Pontryagin equations, Gramian test and Hamilton–Jacobi subsolution inequality are in
`trace/ttcs/results/step28_ttcs01_generator1_integration.md`.  For a lower bound one must keep all three controls.  In particular, for effective shape acceleration \(a=-\bar E+\bar D/2\),
\[
\min_{-\bar E+\bar D/2=a}\left(\bar E^2/6+\bar D^2/8\right)=a^2/8,
\]
so a \(D\)-only model gives the wrong value.

## 3. Pilot optimal control and what it establishes

`scripts/saturation_optimal_control.py` implements (2.2)–(2.3) by Hermite–Simpson collocation and IPOPT.  It uses the regularized potentials, free entry phase \(A\), free duration, and all controls \(\bar H,\bar E,\bar D\).  `scripts/saturation_endpoint_residuals.py` independently maps endpoints back to compact ACH variables and follows their uncontrolled Einstein fate.

The first terminal test deliberately required an exact finite CH orbit.  This is much stronger than standard-CR stable-set membership and, more importantly, it is not scale-consistent with a finite \(\zeta=10^{-2}\) section: the pilot produced costs
\[
3.38823\quad(\varepsilon=.25,N=30),\qquad
3.75033\quad(\varepsilon=.125,N=40),
\]
but the mapped endpoints lie far outside the ACH block and flow to the real-hyperbolic face.  These values do **not** estimate (2.4).

A second test imposed only the Hamiltonian constraint, the linear outgoing covector and \(\widetilde\Phi=0\).  Its nominal cost \(3.37634\) was also rejected: the endpoint's uncontrolled Einstein continuation left the block and became singular.  This computation is useful because it proves that the linear terminal equations are not a substitute for the nonlinear stable manifold.

Two progressively stronger stable-set proxies were tried: eigenmode data at \(\zeta=.01\), then backward integration from \(\zeta=10^{-4}\) using the physical stable modes.  The best feasible pilot on the latter proxy at \(\varepsilon=.25,N=50\) has cost about \(4.616\), but the endpoint constraint residual under the independently reconstructed compact variables is still about \(10^{-5}\), and its forward fate drifts to the real-hyperbolic face.  It therefore remains a route-finding computation, not a lower bound and not a certified competitor.  The next computation must parameterize the exact stable manifold by validated backward shooting, rather than impose approximate finite-section formulas inside the optimizer.

The negative result from the pilot is nevertheless sharp enough to change method: no trustworthy evidence of a sub-\(0.99585\) collapsed construction has appeared, but numerical optimization cannot establish positivity.  The branch now asks for either an exact low-cost stable-set connection or a Hamilton–Jacobi/subsolution estimate for (2.2).

## 4. Revised diagonal compactness statement

The chiral identities reorganize the compactness argument.  On every region where orbit shape and \(W\) stay in a compact set, \(\mathfrak b_\pm\) are bounded and the exact annular formulas control the weighted chiral curvature and scalar curvature by \(\widehat P\) plus bounded endpoint flux.  In one dimension, the Ricci combinations enter the second-order state equations affinely; hence finite cost gives local weak \(H^2\) control, and after excluding collapse and shear this upgrades to local compactness.  Bolt regularity fixes the starting charge \((1,7)\), while Theorem T gives exact-CH truncation once a limiting tail enters the verified standard block.

This removes arbitrary a priori "bolt bounds and block tails" from the conceptual statement.  Failure of compactness for a diagonal minimizing sequence can occur only by:

1. small-bolt collapse through the saturation problem (2.4), including anisotropic shear;
2. large-bolt escape;
3. an interior high-shear/volume-bounce path on which a chiral flux falls sufficiently to evade upward-variation bounds;
4. end escape along the conformal-infinity face.

Scale-separated ALE concentration is already excluded sharply by \(\mathfrak b_+\); nonstandard-CR escape in a large-volume ACH block is excluded by Lemma P; ordinary post-Rossi product/ALF collapse is excluded by the Euler flux; exact standard-CR ends are provided by Theorem T after convergence.

**Revised Theorem D.**  Let \(g_j\) be scalar-\(-24\) diagonal exact-CH-ended metrics on \(O(-1)\), with \(\widehat P(g_j)\) approaching the diagonal infimum.  If the four mechanisms above admit positive costs exceeding the available minimizing budget (or are excluded by the corresponding exact flow statement), then a subsequence converges to a complete scalar-\(-24\) standard-CR ACH minimizer; Theorem T identifies its value with the exact-ended infimum.  Therefore
\[
p^{\rm diag}_{1,0}=0
\quad\Longleftrightarrow\quad
\text{there exists a complete diagonal Einstein ACH filling of }O(-1)
\text{ with standard CR infinity},
\]
provided those four branch results hold.  The implication from Einstein existence to zero infimum is already unconditional by Theorem T.  The reverse implication follows from the compactness conclusion and attainment.

This is shorter than the Step-25 form: bounded bolt size, compact noncollapse and block entry are consequences once the actual escape mechanisms are excluded, rather than independent assumptions.

## 5. Closed-manifold transfer

Ge–Jiang's account of Cheeger–Tian shows that collapsed \(\varepsilon\)-regularity uses a pointwise Ricci bound and fails for general critical metrics.  The diagonal chiral identities bypass that input because they are exact one-dimensional transgressions.  The unrestricted closed problem has no such automatic replacement.  Its collapse theorem must therefore use the near-minimizing property itself — for example a field/variational equation generating a pointwise Ricci floor, or an F-structure along which the Euler and signature transgressions can be integrated — rather than invoke regularity theory from critical \(L^2\) control alone.

## 6. Next mathematical work

The high-value continuation is now precise:

* build a validated two-dimensional parameterization of the nonlinear standard-CR Einstein stable set on \(\zeta=.01\), by interval backward shooting from the \(-4,-6\) modes, and couple it to the full-control collocation;
* compute the finite-\(\varepsilon\) value along several decreasing \(\varepsilon\) only after terminal membership is independently verified;
* derive a Hamilton–Jacobi subsolution for the full scale-free system on the residual high-shear domain, using the exact chiral fluxes as state barriers;
* prove large-bolt and face no-return estimates, completing the remaining branches of revised Theorem D.



---

## Source step29_collapsed_saturation_value_four.md

Original: [sources/Sessions/S1003A02/workspace/notes/step29_collapsed_saturation_value_four.md](../sources/Sessions/S1003A02/workspace/notes/step29_collapsed_saturation_value_four.md)

# Step 29 — The collapsed saturation value is the Berger-to-round chiral gap 4

Conventions are those of Steps 25–28: \(\widehat P=P/8\pi^2=\int W|\operatorname{Ric}^\circ|^2/4\,dt\), diagonal Bianchi-IX metrics \(dt^2+\sum a_i^2\sigma_i^2\) with \(d\sigma_i=2\sigma_j\wedge\sigma_k\), block A \(=W^+\) in the CH/blow-up orientation, chiral fluxes \(\mathfrak b_\pm\) with charges: smooth centre \((2,2)\), \(O(-1)\) bolt \((1,7)\), biaxial Berger collapse \((-2,2)\), CH orbit \((2-9\sinh^4\tau,\,2-3\sinh^4\tau)\).

## 1. The exact-CH terminal is the correct terminal (correction of Step 28)

Step 28 rejected the exact-CH terminal of `scripts/saturation_optimal_control.py` because its endpoints, mapped to compact ACH variables, "left the ACH block". That rejection was an artifact of the checker `scripts/saturation_endpoint_residuals.py`: `to_compact` always places the endpoint on the section \(\zeta=10^{-2}\). In compact variables \(\zeta=1/(a_ga_h)\) in absolute units with \(\operatorname{Ric}=-6\) (from \(\mathrm{fac}=\sqrt\zeta e^{-\beta/3}=1/r\)). A CH orbit of radius \(t_{\rm ch}\approx1.9\) has \(a_ga_h=\sinh^2t_{\rm ch}\approx11\), so forcing \(\zeta=.01\) rescales it by about a factor of 3. The rescaled state is a homothetic CH jet with the wrong curvature scale, and its Einstein evolution with \(\Lambda=-6\) is meaningless.

The correct statement is simple.

**Lemma S (terminal reduction).** Let a controlled trajectory of the scale-free system (Step 28, (2.2)) end at the scale-free first jet \(Y_{\rm CH}(t_{\rm ch})\) of a complex-hyperbolic orbit. Continue the metric by the exact homothetic CH collar beyond that orbit and rescale the whole metric so that the collar has \(\operatorname{Ric}=-6\). The result is a \(C^{1,1}\) diagonal metric with an exact CH collar. Its \(\widehat P\) equals the trajectory action, because \(\widehat P\) charges only the trace-free Ricci tensor and is scale invariant.

The zero-control flow is Einstein: the trace-free equations together with the contracted Bianchi identity force \(s\) to be constant. Hence zero-control continuation from \(Y_{\rm CH}(t)\) is exactly CH, and the exact-CH ray is contained in the standard-CR stable set. Conversely, Theorem T (Step 26) truncates every trajectory entering the standard ACH block with \(\widetilde\Phi\to0\) to an exact CH collar at \(o(1)\) added cost. Therefore
\[
\inf_{\text{exact-CH terminal, free }t_{\rm ch}}=\inf_{\text{standard-CR stable-set terminal}} ,
\]
and the nonlinear stable-manifold parameterization proposed in Step 28 is not needed to formulate or compute the saturation value. The scalar normalization is also harmless. The exact-ended \(P\)-problem and the scalar-\(-24\) problem have the same infimum (Theorem C plus the weak-barrier Yamabe solution), and \(P(g)-P(\hat g)=24\int|\nabla u|^2+3\int(\Delta u/u)^2\ge0\). So any exact-CH competitor yields a scalar-\(-24\) competitor that is at least as cheap.

The Step-28 "stable" mode is a legitimate but harder parameterization. Its costs (4.05–6.16) come from a terminal restricted by the bounds \(|q|\le.3\), \(\kappa\in[.7,1.3]\), and they were not converged in the stable-set parameters.

## 2. Computation

New and modified scripts:

* `scripts/saturation_optimal_control.py` gains optional environment controls: `SAT_A0`, `SAT_T0CH` and `SAT_TAU0` set the cold-start guess, `SAT_TCH_LO` and `SAT_TCH_HI` set the opening-radius window, `SAT_XB` sets the state box, and `SAT_TAG` sets the file tag.
* `scripts/saturation_eps_chain.py` runs continuation in \(\varepsilon\) with warm starts. Outputs: `data/saturation_control/chain_N40_c40.json` and `chain_N80_c80.json`, plus the per-run files `eps*_N*_ch_c40|c80.json`.
* `scripts/saturation_opening_profile.py` minimizes with \(t_{\rm ch}\) confined to windows \([\tau_0,\tau_0+.25]\). Outputs: `data/saturation_control/opening_profile_eps0p0625_N60pjson` and `opening_profile_eps0p25_N60pjson`. The odd suffix comes from a string-replacement slip; these are JSON files.
* `scripts/saturation_metric_cost.py` gives an independent evaluation. From the node data alone it builds an actual \(C^1\) metric: cubic Hermite interpolation in \(\tau\), \(h=\int p\,d\tau\) computed exactly, \(t=\int e^h d\tau\). It then computes the Ricci tensor from the classical diagonal formulas \(\operatorname{Ric}_{00}=-\sum(y_i'+y_i^2)\), \(\operatorname{Ric}_{ii}=-y_i'-y_i\sum y_j+\mathrm{Pot}_i\), with analytic second derivatives of the interpolant. Gauss–Legendre quadrature, 24 nodes per cell, gives \(\widehat P\). The potential/control formulas are never used.
* `scripts/saturation_verify.py` is a multiple-shooting re-integration. It is useful only as a diagnostic: in the collapsed neck the forward dynamics grows like \(e^{h/z^2}\), and single-cell re-shooting diverges at small \(\varepsilon\) even for accurate collocation.

### 2.1 Value along the entry ray

The minimum over the entry phase \(A\), the duration and \(t_{\rm ch}\), with all three controls \((\bar H,\bar E,\bar D)\):

| \(\varepsilon\) | \(\mathfrak b_+(\text{entry})\) | gap \(2-\mathfrak b_+\) | collocation \(N=40\) | collocation \(N=80\) | actual-metric \(\widehat P\) | \(t_{\rm ch}\) | \(\max\mathfrak b_+\) |
|---|---|---|---|---|---|---|---|
| 1/2 | −0.446 | 2.446 | 2.3396 | 2.3310 | 2.5173 (N80) | 2.62 | 1.21 |
| 1/4 | −1.413 | 3.413 | 3.3852 | 3.3798 | 3.4773 (N80) | 2.33 | 1.57 |
| 1/8 | −1.762 | 3.762 | 3.7503 | 3.7461 | 3.8167 (N80) | 2.18 | 1.68 |
| 1/16 | −1.895 | 3.895 | 3.8896 | 3.8949* | 3.9343 (N40) | 1.73 | 1.79 |
| 1/32 | −1.951 | 3.951 | 3.9484 | 3.9509* | 3.9815 (N40) | 1.60 | 1.83 |
| 1/64 | −1.976 | 3.976 | 3.9763* | 3.9763* | — | 0.70 | 2.000 |
| 1/128 | −1.988 | 3.988 | 3.9884* | 3.9884* | 3.98841 (N80) | 0.70 | 2.000 |
| 1/256 | −1.994 | 3.994 | 3.9937 | — | 3.99632 (N40) | 0.70 | 2.000 |

\* IPOPT stopped at its iteration cap with constraint violation \(\le2\times10^{-5}\). These runs are converged in value but not certified as KKT points.

The actual-metric costs are 0.001–8% above the collocation values, and the difference shrinks under mesh refinement. They are genuine \(\widehat P\) values of explicit \(C^1\) metrics, up to quadrature error. The two meshes agree to \(<0.3\%\).

### 2.2 Opening-radius profile

The minimal cost with \(t_{\rm ch}\in[\tau_0,\tau_0+.25]\):

| \(\tau_0\) | 0.75 | 1.0 | 1.25 | 1.5 | 1.75 | 2.0 | 2.25 | 2.5 | 2.75 | 3.0 | 3.25 | 3.5 | 3.75 | 4.0 | 4.25 | 4.5 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| \(\varepsilon=1/16\) | 3.894 | 3.893 | — | 3.889 | — | 3.888 | — | 4.146 | — | 7.91 | — | 33.7 | — | 207 | — | 2848 |
| \(\varepsilon=1/4\) | (3.41 at 1.0) | 3.408 | — | 3.397 | — | 3.384 | 3.38 | — | 3.656 | — | 7.05 | — | 28.0 | — | 226 | — |

Late opening is priced at least exponentially. Successive costs grow by factors 4–8 per 0.5 in \(\tau\), consistent with the \(e^{4\tau}\) CR-pinning law of Lemma P. Opening below \(\tau\approx.70\) is priced by Corollary X3 at \(\ge4-9\sinh^4\tau\). The intermediate band costs \(\approx\) gap.

The largest late windows are under-resolved: at \(\tau_0=3\) the actual-metric cost is 45 against collocation 7.9. They are upper evidence of large cost, not values.

## 3. What the computation shows

1. **No collapsed competitor.** No computed collapsed saturation comes anywhere near the certified \(0.99585\) cell. The minimal value along the matched Taub-bolt/\(\Lambda\)-Taub-NUT entry ray increases monotonically as the neck deepens, from 2.33 at \(\varepsilon=1/2\) to 3.994 at \(\varepsilon=1/256\).

2. **The limit is the chiral gap 4.** The value tracks \(2-\mathfrak b_+(\text{entry})\) to within \(3\times10^{-3}\) for \(\varepsilon\le1/16\), and to within \(10^{-5}\) for \(\varepsilon\le1/64\). Here \(\mathfrak b_+(\text{entry})\to-2\), the biaxial Berger charge. Thus
\[
\mathcal V_{\rm sat}:=\lim_{\varepsilon\to0}\inf\widehat P_{\rm sat}=4 \qquad(\text{numerical}).
\]

3. **Structure of the minimizer.** For \(\varepsilon\le1/64\) the optimizer reaches \(\max\mathfrak b_+=2.000\), the value of a Euclidean-round orbit. Its cost equals the rise \(\mathfrak b_+(\mathrm{round})-\mathfrak b_+(\mathrm{entry})\) to \(10^{-5}\). By the chiral identity \(\widehat P=\Delta\mathfrak b_++\frac1{2\pi^2}\int|W^+|^2+\frac1{96\pi^2}\int s^2\), the rising part therefore has \(W^+\approx0\) and \(s\approx0\): it is asymptotically **anti-self-dual and scalar flat**. After the round orbit the trajectory follows a CH ball from radius \(\approx0\) at zero cost. The value then does not depend on \(t_{\rm ch}\); the lower bound \(0.701\) that the optimizer meets is inert.

   So the collapsed branch degenerates into a scale-separated bubble: a Ricci-flat Taub-bolt core, its ALF/Berger end, then an ASD scalar-flat decollapse region (cost 4) onto an almost-Euclidean neck at a point of CH. This is the ALF analogue of the Burns bubble. Burns joins the bolt charge 1 to the round charge 2 at cost 1. The collapsed route first drops freely to \(-2\) and must then pay \(2-(-2)=4\).

4. **Consequence for the Theorem-D branch list.** Mechanism 1, small-bolt collapse, is numerically priced at \(\approx4\) per collapsed bubble, with a factor-four margin over the best cell. The numerics also say where the remaining work lies: the minimizer approaches a near-round orbit, where \(\mathfrak b_+\) is already a sharp barrier, and openings far from round are more expensive.

## 4. The lower-bound problem, sharpened

The data identify the Hamilton–Jacobi subsolution that must be proved. The target is
\[
\Psi=\mathfrak b_++G(Y),\qquad \dot\Psi\le L \ \text{ for all controls},
\]
with \(G\ge0\), \(G\to0\) on the collapsed boundary, and \(G(Y_{\rm CH}(\tau))\ge9\sinh^4\tau-3+\delta\) along the CH ray. The \(-3+\delta\) is the slack needed only to beat \(1\); the sharp value corresponds to \(-\delta\). Then \(\widehat P_{\rm sat}\ge\Psi(\mathrm{end})-\Psi(\mathrm{entry})\ge1+\delta\) for every trajectory.

Writing \(\sigma_+=(|W^+|^2+s^2/48)W\,dt/d\tau\), which is quadratic in the controls, the requirement is the pointwise inequality
\[
\min_u\bigl[\sigma_+(Y,u)-\nabla G\cdot(f_0(Y)+Bu)\bigr]\ge0 .
\]
On the CH ray, \(\sigma_+=36W\,dt/d\tau\), so \(G\) must grow like \(9\sinh^4\tau\): this is the regenerated CH \(W^+\)-plus-volume energy. The tangency condition at the CH ray forces \(G\) to depend on the velocities \((p,\chi,\eta)\), not only on the shape.

The profile in §2.2 indicates the three regimes of \(G\):

* \(G\approx0\) near round orbits, where \(\mathfrak b_+\) alone already gives the sharp bound;
* \(G\) of Lemma-P type, \(\sim e^{4\tau}(\Delta\log\rho)^2\), on late openings;
* an interpolating band \(0.7\lesssim\tau\lesssim2.5\), where the numerical value is \(\approx\) gap and some slack of order 3 is available for \(\ge1\).

A practical route is polynomial/interval verification of a candidate \(G\) on the compact band, plus asymptotic arguments on the two ends.

An alternative, possibly shorter, rigorous route uses the minimizer's structure: show directly that any trajectory with \(\widehat P_{\rm sat}<1\) must reach a CH-like orbit with \(\tau<0.70\) (then Corollary X3 applies), using Lemma P to exclude \(\tau\gtrsim2.5\) and a compact computation for the band.

## 5. Frozen form of Theorem D

See `theorem_package_v1.md` §4.1, entry "Theorem D (frozen statement, Step 29)". That entry records the current status of each mechanism; mechanism 1 is now numerically priced at 4 (§3 above), and its proof is the subsolution of §4.



---

## Source step30_Qdoubleprime_beta_pinning_and_anisotropic_collapse.md

Original: [sources/Sessions/S1003A02/workspace/notes/step30_Qdoubleprime_beta_pinning_and_anisotropic_collapse.md](../sources/Sessions/S1003A02/workspace/notes/step30_Qdoubleprime_beta_pinning_and_anisotropic_collapse.md)

# Step 30 — Q″, fibre/base pinning, and anisotropic collapsed entries

Conventions are those of Steps 27–29.  For a diagonal Bianchi–IX annulus,

\[
\widehat P(C)=\Delta\mathfrak b_+
 +\frac1{2\pi^2}\int_C|W^+|^2
 +\frac1{96\pi^2}\int_Cs^2. \tag{1}
\]

The charge orientation and normalization are the independently checked ones: a smooth round centre has \(\mathfrak b_+=2\), an \(O(-1)\) bolt has \(\mathfrak b_+=1\), a regular Berger end has \(\mathfrak b_+=-2\), and a CH orbit of radius \(t\) has \(\mathfrak b_+=2-9\sinh^4t\).

## 1. Lemma Q″: diagonal bubble-end pricing

**Lemma Q″.** Let \(C_j=[T_j,S_j]\times S^3\) be diagonal annuli whose inner orbits converge in normalized chiral first-jet data to a bubble end with finite plus charge \(b_{\mathrm{end}}\). Suppose an outer orbit converges in the same data to a round Euclidean sphere, so its charge tends to \(2\). Then
\[
\liminf_j\widehat P(C_j)\ge 2-b_{\mathrm{end}}. \tag{2}
\]
More generally, between two convergent normalized first-jet limits,
\[
\liminf_j\widehat P(C_j)
 \ge b_+^{\mathrm{out}}-b_+^{\mathrm{in}}. \tag{3}
\]

**Proof.** Integrate (1) and discard the two nonnegative integrals. At a collapsed end, the required convergence is precisely convergence of the normalized chiral connection coefficients \(u_i=p_i-\gamma_i\), or equivalent data that make \(\mathfrak b_+\) converge; convergence of the raw state alone is insufficient. \(\square\)

Consequences:

* Burns joins the \(O(-1)\) bolt charge \(1\) to the round charge \(2\), hence pays at least \(1\). It is scalar-flat ASD in this orientation and attains equality.
* The Ricci-flat Taub-bolt path carries the same bolt freely to the Berger/ALF charge \(-2\). Any subsequent controlled decollapse to a round orbit pays at least \(2-(-2)=4\). The Step-29 scale-free minimizers approach equality through an ASD scalar-flat decollapse.
* This is the diagonal version of a general bubble-end principle: the topology price is a relative characteristic transgression at the end, rather than a universal cost assigned to the compact core alone.

The closed-manifold form suggested by (2) is the following precise research target. On an F-structure neck surrounding a collapsed bubble, define the adiabatic Euler/signature boundary limit from the Levi-Civita Chern–Simons forms. If this limit exists and the neck can be compared to a round link, then its topology cost should be the round characteristic charge minus the adiabatic end charge, with nonnegative bulk curvature terms. Q″ proves this in diagonal symmetry. Establishing existence and functoriality of that adiabatic limit beyond symmetry would supply exactly the collapse accounting that pointwise-Ricci regularity presently does not provide.

### Finite-charge anisotropic Berger limit

A useful normalized first-jet class can be described exactly. In the regular scale-free coordinates
\[
x=\log(a_f/a_g),\quad z=(a_h/a_g)^{1/3},\quad
p=rh',\quad\chi=r(x'),\quad\eta=rq',
\]
consider the collapsed first-jet family
\[
x=Xz^3+o(z^3),\quad p=Pz+o(z),\quad
\chi=Cz+o(z),\quad\eta=Nz+o(z). \tag{4}
\]
The exact symbolic calculation `scripts/collapse_chiral_charge_limit.py` gives
\[
\mathfrak b_+^{\mathrm{end}}=-2-(C+4X)^2. \tag{5}
\]
Therefore shear cannot raise this finite-charge end above \(-2\); it either preserves the Berger price, when \(C+4X=0\), or increases the round-decoupling price to
\[
2-\mathfrak b_+^{\mathrm{end}}=4+(C+4X)^2. \tag{6}
\]
The opposite charge is
\[
\mathfrak b_-^{\mathrm{end}}=2+(C-4X)^2. \tag{7}
\]
Thus \(P\) and \(N\) cancel from both limits. Equation (5) rigorously controls a finite-charge anisotropic entrance to the high-shear branch. It does not by itself assert bounded ambient curvature. At fixed base scale, bounded orbit curvature requires the stronger \(x=O(z^6)\), and bounded mixed curvature forces stronger shear decay such as \(\chi=O(z^4)\), together with radial second-derivative control. In that genuinely bounded-geometry regime \(X,C\to0\) and \(\mathfrak b_+\to-2\). Fixed \(O(1)\) values of \(x,\chi,\eta\) as \(z\to0\) are outside even the finite-charge class.

## 2. A fibre/base analogue of CR pinning

Use compact ACH variables for fibre \(f\):
\[
\kappa=\frac{a_f}{a_ga_h},\qquad
\zeta=\frac1{a_ga_h},\qquad q=\log\frac{a_g}{a_h},
\]
and put
\[
v=y_f-\frac{y_g+y_h}{2}=\beta',\qquad
\widetilde B=
\log\frac{\kappa}{\sqrt{1+\zeta}}
 +\frac14\left(v-\kappa^{-1}\right). \tag{8}
\]
The correction is adapted to the CH geometry: on every CH orbit
\(\kappa=\coth t\), \(\zeta=\operatorname{csch}^2t\), and \(v=\tanh t=\kappa^{-1}\), so \(\widetilde B=0\). The coefficient \(1/4\) is not forced by CH vanishing alone; it is useful because it removes a fibre-velocity term from the linear ACH drift.

Let
\[
E=\operatorname{Ric}_{ff}
 -\frac{\operatorname{Ric}_{gg}+\operatorname{Ric}_{hh}}2.
\]
Direct symbolic differentiation using the exact diagonal Ricci equations gives
\[
\widetilde B'=F_\beta-\frac14E, \tag{9}
\]
where \(F_\beta\) is the same expression evaluated on the uncontrolled Einstein equations. The identity and CH vanishing are in `scripts/beta_pinning_identity.py` and `data/beta_pinning_identity.json`. The tensor normalization is
\[
|\operatorname{Ric}^{\circ}|^2
 =\frac34H^2+\frac23E^2+\frac12D^2,
\]
so \(\widehat P\ge\frac16\int WE^2dt\). Hence
\[
\boxed{
\left|\Delta\widetilde B-\int F_\beta\,dt\right|
 \le
 \sqrt{\frac{3\widehat P}{8}}
 \left(\int\frac{dt}{W}\right)^{1/2}.}
\tag{10}
\]
This is the exact fibre/base counterpart of Lemma P. Its control factor differs because the traceless diagonal tensor associated with \(E\) has squared norm \(2E^2/3\).

On an exact CH tail,
\[
W=\sinh^3t\cosh t,
\quad
I(T):=\int_T^\infty\frac{dt}{W}
 =\frac1{2\sinh^2T}
 -\frac12\log(1+\sinh^{-2}T). \tag{11}
\]
If the correction interval is exact CH—or if a separate comparison proves \(\int W_g^{-1}dt\le I(T)\)—and the drift-corrected mismatch is \(C\), then
\[
\widehat P\ge\frac{8C^2}{3I(T)}. \tag{12}
\]
For a general connector, the denominator remains its actual \(\int W_g^{-1}dt\); a CH terminal first jet alone does not justify substituting \(I(T)\). The threshold table is `data/beta_pinning_threshold.json`. With the CH denominator, overlap with Corollary X3 at \(t=.70\) requires mismatch at least
\[
C_*=\sqrt{3I(.70)/8}=0.370125\ldots. \tag{13}
\]
The raw shape change \(\beta\) is not itself enough: the first-jet correction in (8) cancels exact CH radial evolution, and the uncontrolled drift \(F_\beta\) must be bounded along the pre-ACH connector. In the verified ACH block, the Taylor calculation has zero constant term and linear term
\[
z\left(-\frac15s_2+\frac25u-\cosh q+1\right). \tag{14}
\]
It is not sign-definite, and the factor \(z\) only makes it small when \(q\) is also controlled. Thus (10) explains the large-radius exponential behavior in a standard ACH block, but a volume comparison and a geometric mismatch estimate—or a compact interval enclosure—are still needed on the saturation region.

## 3. Anisotropic entry computation

`scripts/saturation_anisotropic_scan.py` runs the full three-control Hermite–Simpson problem with altered entry first jets. `data/saturation_control/step30_anisotropic_summary.json` records the runs.

Two classes must be separated.

### 3.1 Finite-charge first-jet perturbations

The finite-charge mode uses (4): \(x=Xz^3\), \(\chi=Cz\), \(\eta=Nz\). At \(\varepsilon=1/16\), the charge-changing examples behaved as predicted:

* \(X=0,C=1\): cost \(4.9625\), initial \(\mathfrak b_+=-2.9417\);
* \(X=1,C=0\): cost \(21.727\), initial \(\mathfrak b_+=-19.512\) at this not-yet-asymptotic scale;
* the charge-kernel direction \(X=1,C=-4\): cost \(3.5789\), initial \(\mathfrak b_+=-1.5854\); at \(\varepsilon=1/32\) the cost is \(3.7783\), moving toward the limiting value \(4\).

A large finite-charge \(N=-8\) perturbation lowers the finite-\(\varepsilon\) cost to \(2.2668\), but (5) says it cannot alter the limiting plus charge. This normalized-jet ansatz is not automatically bounded-curvature geometry. The run shows a finite-scale matching effect, not evidence against Q″.

### 3.2 Enlarged raw entry jets

Allowing fixed \(O(1)\) perturbations as the circle collapses can make the connector much cheaper. The strongest run at \(\varepsilon=1/16\), raw \(\Delta\eta=-8\), has collocation cost \(0.54541\); independent actual-metric reconstruction gives \(0.57446\). The connector alone is below the certified Burns-core cell, but the run is not a regular bolt/collapse construction: its scaling violates (4), and the same raw perturbation at \(\varepsilon=1/32\) costs \(2.94250\), with reconstructed cost \(2.94303\). Fixed raw \(x=\pm .25\) produces enormous charges and costs \(221\)–\(361\).

The cheap raw jet already has \(\mathfrak b_+=1.45194\), so the omitted bolt-to-entry prefix costs at least \(1.45194-1=0.45194\). Adding this to the reconstructed connector gives at least \(1.0264\), above the certified cell. This run therefore does not undercut the cell even before a regular-prefix construction is imposed. It shows instead that arbitrary first jets can destroy the connector's value-four law at finite scale. The exact identity
\[
\mathfrak b_+=-2-(u_f-u_g)^2+\delta(4-u_fu_g)-\delta^2,
\qquad \delta=u_h+2,
\]
explains the mechanism: raw opening rate \(\delta\ne0\) can raise the entry charge. Thus \(\eta\), the contact-slot shear velocity, is the dangerous high-shear coordinate. A small-bolt theorem must show that regular bolt data enter a finite-charge or bounded-geometry class, or account for the cost of producing raw \(O(1)\) shear before the selected section.

## 4. Consequences and next proof work

1. Q″ rigorously prices any collapsed-to-round annulus once its normalized entry charge is known. Bounded-geometry Berger collapse has \(\mathfrak b_+\to-2\), hence pays at least \(4-o(1)\).
2. Finite-charge anisotropy changes the price to \(4+(C+4X)^2\); the kernel \(C+4X=0\) retains charge \(-2\), but it is not automatically bounded-curvature geometry.
3. The live branch is loss of normalized first-jet control, especially raw contact shear \(\eta\). This is the high-shear volume-bounce mechanism.
4. The beta-pinning identity (10) supplies the late-opening tool. Closing the branch by it and X3 requires an actual \(W^{-1}\) comparison and a drift-corrected mismatch bound; with the exact CH denominator at \(t=.70\), the needed value is \(0.370125\ldots\).
5. Beyond symmetry, the transferable target is an adiabatic characteristic charge of a collapsed F-structure link and a relative bulk transgression. That would replace unavailable pointwise-Ricci regularity in the global collapse passage.



---

## Source step31_charge_variation_constraint_pinning_nonround_opening.md

Original: [sources/Sessions/S1003A02/workspace/notes/step31_charge_variation_constraint_pinning_nonround_opening.md](../sources/Sessions/S1003A02/workspace/notes/step31_charge_variation_constraint_pinning_nonround_opening.md)

# Step 31 — Charge variation, scalar-normalized constraint pinning, non-round opening, and the large-bolt face limit

Conventions are those of Steps 25–30: diagonal Bianchi–IX metrics \(g=dt^2+\sum a_i^2\sigma_i^2\), \(y_i=a_i'/a_i\), \(W=a_fa_ga_h\), \(\widehat P=\int W|\operatorname{Ric}^\circ|^2/4\,dt\), \(|\operatorname{Ric}^\circ|^2=\tfrac34H^2+\tfrac23E^2+\tfrac12D^2\). The best certified cell value is \(p_*=0.995848\).

## 1. The charge-variation functional

The chiral identities of Theorem X hold on every annulus, hence pointwise in \(t\):
\[
\frac{d\widehat P}{dt}=\frac{d\mathfrak b_\pm}{dt}+\omega_\pm,\qquad
\omega_\pm=\frac{W}{2\pi^2}\Big(|W^\pm|^2\text{-density}\Big)+\frac{W}{96\pi^2}\Big(s^2\text{-density}\Big)\ge0 .
\]
**Lemma V.** For every diagonal annulus \(C=[a,b]\times S^3\),
\[
\widehat P(C)\ \ge\ \int_a^b\max\{0,\mathfrak b_+',\mathfrak b_-'\}\,dt\ \ge\ \max\{V^+_C(\mathfrak b_+),V^+_C(\mathfrak b_-)\},
\]
where \(V^+\) is positive variation. In particular, for an \(O(-1)\) cell with bolt charges \((\mathfrak b_+,\mathfrak b_-)=(1,7)\),
\[
\widehat P\ \ge\ \sup_t\max\{\mathfrak b_+(t)-1,\ \mathfrak b_-(t)-7\},
\qquad
\widehat P\ \ge\ \sup_{s<t}\big(\mathfrak b_\pm(t)-\mathfrak b_\pm(s)\big).
\]
*Proof.* Integrate the pointwise identity and drop \(\omega_\pm\); on any finite disjoint family of intervals the increments add. \(\square\)

The opposite charge is \(\mathfrak b_-=\sum w_i^2-w_fw_gw_h-2\), \(w_i=a_i'+\gamma_i\) (scale-free normalization \(r=1\)), with \(\mathfrak b_+=2-\sum u_i^2-u_fu_gu_h\), \(u_i=a_i'-\gamma_i\). Checks: smooth centre \(u=0,w=(2,2,2)\Rightarrow(2,2)\); bolt with \(a_h'(0)=1\), \(\gamma_h=2\): \(u=(0,0,-1)\), \(w=(0,0,3)\Rightarrow(1,7)\); CH orbit \(\mathfrak b_-=2-3\sinh^4t\) (numerically \(1.00657\) at \(t=.7\), \(-59.667\) at \(t=1.5\), exact agreement; `data/saturation_control/two_sided_bounds.json`).

**Consequences.**

1. *Round passages.* Any cell that passes an orbit with \(\mathfrak b_+\ge 1+p_*\) costs more than \(p_*\). A cheap cell stays in \(\{\mathfrak b_+<1+p_*,\ \mathfrak b_-<7+p_*\}\), and after any section \(s\) it satisfies \(\mathfrak b_\pm(t)<\mathfrak b_\pm(s)+p_*\).
2. *The raw high-shear escape is excluded by the bolt prefix alone.* The Step-30 entry state with \(\Delta\eta=-8\) has \(\mathfrak b_+=1.45194\) and \(\mathfrak b_-=8.54957\). Any trajectory from an \(O(-1)\) bolt to that state therefore costs at least \(8.54957-7=1.5496\) before the connector begins. This replaces the Step-30 reconstructed total \(\ge1.0264\) by a connector-independent bound, using only the opposite chirality.
3. *Reduction of mechanisms 1 and 3.* A cheap cell that ever reaches a collapsed section (\(\mathfrak b_+\approx-2\)) satisfies \(\mathfrak b_+<-2+p_*\approx-1.004\) afterwards. Since a CH orbit has \(\mathfrak b_+=2-9\sinh^4\tau\), it must first reach CH shape at \(\tau>0.70\). The small-bolt saturation branch and every shear bounce that collapses therefore reduce to one problem: **non-round late opening** — a path from a collapsed or sheared state to a CH orbit at \(\tau\ge0.70\) along which \(\mathfrak b_+\) stays below \(-1\).

## 2. Non-round late opening: numerical value

`scripts/saturation_optimal_control.py` now accepts `SAT_BPMAX=c`, imposing \(\mathfrak b_+\le c\) at every collocation node, with the CH opening radius free in \([0.701,4.6]\). Outputs: `data/saturation_control/eps*_ch_bpmax_*.json`.

| \(\varepsilon\) | \(N\) | cap \(c\) | cost | \(t_{\rm CH}\) |
|---|---|---|---|---|
| 1/16 | 60 | none (Step 29) | 3.888 | 2.0 |
| 1/16 | 60 | 1 | 4.035 | 2.14 |
| 1/16 | 60 | 0 | 4.810 | 2.24 |
| 1/16 | 60 | −0.5 | 5.501 | 2.26 |
| 1/16 | 60 | −1 | 6.478 (two warm starts agree to \(10^{-9}\)) | 2.28 |
| 1/16 | 80 | −1 | 6.437 | 2.39 |
| 1/16 | 60 | −1.5 | 7.890 | 2.29 |
| 1/16 | 60 | −2.5 | 11.874 | 2.53 |
| 1/4 | 60 | −1 | 5.374 | 2.62 |
| 1/32 | 80 | −1 | 6.551 | 2.30 |
| 1/64 | 80 | −1 | 6.619 | 2.22 |

All runs converged with collocation residual \(\le10^{-10}\). The non-round value increases as \(\varepsilon\to0\) and is mesh-stable. These are feasible constrained paths returned by a local optimizer (explicit upper constructions for the constrained problem), not lower bounds; they show that the cheapest paths the optimizer finds in the reduced problem of §1 have cost about six times \(p_*\).

The cost is not paid by charges. `scripts/charge_variation_bound.py` (output `data/saturation_control/charge_variation.json`) evaluates the discrete Lemma-V functional: it recovers \(3.85/3.89\) and \(3.994/3.994\) of the round-reopening paths, but only \(1.49\) of the \(c=-1\) cost \(6.48\) and \(1.54\) of the \(c=-2.5\) cost \(11.87\). The channel split of the \(c=-1\) optimum is \((H,E,D)=(0.53,1.70,4.30)\); for \(c=-2.5\) it is \((2.58,2.73,6.61)\). Non-round opening is paid mainly through \(D\), the slot channel that opens the collapsed circle into a contact direction, at large orbit volume. This is the Weyl/scalar part \(\omega_\pm\) of the cost, i.e. a pinning effect rather than a transgression effect.

## 3. Lemma N: the H channel is the Hamiltonian constraint

In compact variables \(y_i'=6-y_iS+P_i-e_i\), \(e_i=\operatorname{Ric}_{ii}+6\), \(R^{(3)}=\sum P_i\), and \(e_0=\operatorname{Ric}_{00}+6\). Put
\[
\mathcal C=\sigma_2(y)-6-\tfrac12R^{(3)}
=\kappa^2+y_fy_g+y_gy_h+y_hy_f-4\zeta\cosh q-6+4\zeta^2\sinh^2q/\kappa^2 .
\]
**Lemma N.** For every diagonal metric:
1. \(\mathcal C=G_{00}-6=\tfrac12(e_0-\sum_ie_i)\);
2. (Bianchi propagation) \(\mathcal C'=-2S\mathcal C-\sum_i(S-y_i)e_i\);
3. if \(s\equiv-24\), then \(\mathcal C=\operatorname{Ric}^\circ_{00}=-\tfrac34H\), so
\[
\widehat P=\int W\Big(\frac{\mathcal C^2}{3}+\frac{E^2}{6}+\frac{D^2}{8}\Big)dt ;
\]
4. if \(s\equiv-24\), then \(S'=18-S^2+R^{(3)}+\mathcal C\).

All four identities, the norm decomposition, and \(\mathcal C=0\) on CH are verified exactly by `scripts/scalar_normalized_constraint.py` (`data/scalar_normalized_constraint.json`, all residuals \(0\)).

By Theorem C and the weak-barrier theorem, \(P(g)-P(\hat g)=24\int|\nabla u|^2+3\int(\Delta u/u)^2\ge0\) for the scalar-\(-24\) conformal metric \(\hat g=u^2g\); the radial \(u\) preserves the diagonal class. It does **not** literally preserve an exact CH collar (\(u\to1\) only at rate \(m\in(4,2+2\sqrt3)\)), and it rescales the bolt radius to \(u(0)b\). The correct statement (Step-32 independent reading): the exact-ended diagonal infimum equals the infimum of \(P\) over diagonal scalar-\(-24\) metrics asymptotic to the marked standard CH end at rate \(>4\); conversely such a metric is truncated to an exact CH collar with vanishing added cost by Theorem T. In the scalar-normalized class (3) holds. A large-bolt statement must use the normalized bolt scale \(u(0)b\) or control \(u(0)\) separately. In that class the trace channel is not a third first-order pinning observable but a **zeroth-order pointwise penalty**: the state must lie on the Einstein constraint surface \(\mathcal C=0\) wherever \(W\) is large. The chiral density also strengthens there to \(d\widehat P/dt=\mathfrak b_\pm'+3\widehat V'+(\text{Weyl}^\pm\text{ density})\), \(\widehat V=2\operatorname{Vol}/\pi^2\); see the volume-renormalized charges in `notes/step33_link_charges_global_decomposition_static_channel.md`.

This answers the proposed scale-channel mechanism precisely. The Einstein constant \(\hat\lambda=-G_{00}\) has zero free drift and is pinned, but the collapsed \(\Lambda\)-Taub–NUT neck already has \(\hat\lambda=-6\). The trace channel therefore cannot be where late opening is paid, consistent with the \(D\)-dominated split in §2.

**Lemma W (volume comparison).** Let \(s\equiv-24\) on \([T,T_1]\), suppose \(R^{(3)}\ge-\rho_0\) there with \(A^2=18-\rho_0>0\), and let \(0<\sigma_0<m:=\min\{S(T),A\}\). If
\[
m-\Big(\frac{3\widehat P_{[T,T_1]}}{\sigma_0W(T)}\Big)^{1/2}\ >\ \sigma_0,
\]
then \(S>\sigma_0\) on \([T,T_1]\), \(W(t)\ge W(T)e^{\sigma_0(t-T)}\), and \(\int_T^{T_1}dt/W\le1/(\sigma_0W(T))\) (hypothesis with strict inequality \(>\sigma_0\)).

*Proof (last-crossing form, repaired after the Step-32 independent reading).* Let \(T^*=\sup\{t\le T_1:S\ge\sigma_0\text{ on }[T,t]\}\). On \([T,T^*]\), \(W'=SW\ge\sigma_0W\), so \(\int_T^tdt/W\le1/(\sigma_0W(T))\) and, by (3) and Cauchy–Schwarz, \(\int_T^t|\mathcal C|\le(3\widehat P)^{1/2}(\sigma_0W(T))^{-1/2}\). Fix \(t\in[T,T^*]\). If \(S(t)\ge m\) there is nothing to prove. Otherwise let \(t_0=\sup\{s\in[T,t]:S(s)\ge m\}\); it exists because \(S(T)\ge m\), and \(S(t_0)\ge m\) by continuity. On \((t_0,t]\), \(0<\sigma_0\le S<m\le A\), hence \(S'\ge A^2-S^2+\mathcal C>-|\mathcal C|\) by (4), and \(S(t)\ge m-\int_{t_0}^t|\mathcal C|\ge m-(3\widehat P/(\sigma_0W(T)))^{1/2}>\sigma_0\). (When \(S(T)>A\) the curve may first decrease freely while \(S>A\); the last crossing of the level \(m\) is what makes the argument valid.) Thus \(S>\sigma_0\) at \(T^*\), so \(T^*=T_1\). \(\square\)

Lemma W supplies the volume comparison needed to apply Lemma P and fibre/base pinning to a general connector: on an interval with \(R^{(3)}\ge-\rho_0\), the actual \(\int W^{-1}\) is bounded by \(1/(\sigma_0W(T))\). It also prices the high-shear volume bounce: \(S\) can fall below \(\min\{S(T),A\}\) only by \(\int|\mathcal C|\), which costs \(\ge(\Delta S)^2\sigma_0W/3\). Two residual inputs remain. The orbit curvature hypothesis \(R^{(3)}\ge-\rho_0\) is a bound on \(\kappa\) and on \(\zeta^2\sinh^2q/\kappa^2\), and the drifts \(F,F_\beta\) of the first-order pinning observables are small only in an ACH block.

## 4. Large bolt: the Rossi datum is fixed at volume \(b^2\)

`scripts/large_bolt_volume_profile.py` integrates the validated ACH1 separatrices (`data/ach_fate/large_bolt_volume_profile.json`). Along the Einstein orbit from the bolt, \(W\) is monotone; there is no base-shrinking excursion. The minimum of \(W\) on \(t\ge.05\) is at \(t=.05\), with value \(\approx b^2t\). The Rossi observable is set early, in a region of volume \(\sim b^2\):

| \(b\) | \(\widetilde\Phi(0.77)\) | \(\widetilde\Phi(1.15)\) | \(\widetilde\Phi_\infty=\log\rho\) | \(W(0.77)\) |
|---|---|---|---|---|
| 0.8 | 0.096 | 0.630 | 0.7847 | 2.96 |
| 2 | 0.680 | 1.061 | 1.1543 | 13.2 |
| 20 | 2.861 | 3.213 | 3.2941 | 1212 |

Profiles are close to \(b\)-independent in \(\kappa(t)\) (2.63, 1.43, 1.14 at \(t=.38,.77,1.15\) for \(b=20\); 2.66, 1.46, 1.16 for \(b=2\)), while \(\zeta b\) and \(\widetilde\Phi-\log b\) converge. This suggests the **face limit**: as \(b\to\infty\), the separatrix converges in \((y,\kappa,\zeta b,\widetilde\Phi-\log b)\) to an Einstein trajectory of the \(\zeta=0\) face from the bolt corner \(\kappa=\infty\) to \(E(q)\). The face system is \(q\)-independent, so \(q\) is cyclic there and its offset is \(\log b\).

The face limit is confirmed numerically by `scripts/large_bolt_face_limit.py` (`data/ach_fate/large_bolt_face_limit.json`), which bisects the AH/SING separatrix near \(d\approx0.9b\):

| \(b\) | \(d/b\) | \(\kappa(1)\) | \(\zeta b\,(1)\) | \(W/b^2\,(1)\) | \(\widetilde\Phi-\log b\) at \(t=0.5,1,2,3\) |
|---|---|---|---|---|---|
| 20 | 0.903977 | 1.21352 | 0.38711 | 8.0979 | −1.2418, 0.14396, 0.29593, 0.29828 |
| 50 | 0.905139 | 1.21330 | 0.38724 | 8.0910 | −1.2425, 0.14262, 0.29439, 0.29674 |
| 100 | 0.905305 | 1.21327 | 0.38726 | 8.0900 | −1.2426, 0.14243, 0.29417, 0.29652 |
| 200 | 0.905346 | 1.21326 | 0.38727 | 8.0898 | −1.2426, 0.14238, 0.29412, 0.29646 |

Hence \(d\sim0.90535\,b\) and \(\rho_\infty\sim e^{0.2965}b\approx1.345\,b\), in agreement with the earlier fit \(1.343b\). Every rescaled face quantity converges with differences of order \(b^{-2}\). The Rossi offset is produced between \(t=0.5\) and \(t\approx1.5\), where \(W/b^2\in[0.97,64]\). The large-bolt Einstein orbit is therefore an \(O(b^{-2})\) perturbation of one face Einstein trajectory, and its CR datum differs from the standard one by \(\log(1.345b)\), carried at volume \(\asymp b^2\). (The \(b=2\) bracket \([0.8b,b]\) contained no transition; the \(b=2\) separatrix at \(d=1.555\) lies outside it and is consistent with the trend \(d/b\uparrow0.905\).)

**Theorem L (programme).** For standard-CR diagonal cells with bolt \(b\to\infty\), \(\widehat P\to\infty\), heuristically as \(b^2(\log b)^2\).

The proposed proof has three steps.
1. Bounded \(\widehat P\) together with \(W\gtrsim b^2t\) forces \(\int(\mathcal C^2+E^2+D^2)\,W/b^2\to0\) at face scale. This uses Lemma N, with the bolt series controlling \(t\lesssim b^{-2}\).
2. Lemma W and face compactness give convergence on \([t_0,T_0]\) to face Einstein trajectories. Their ACH separatrices have \(\widetilde\Phi-\log b\to\phi_1\), with \(|\phi_1|\) bounded; this includes the mirror ACH2.
3. At \(T_0\) the state lies in a standard ACH block at volume \(W\gtrsim b^2e^{4T_0}\). Lemma P with Lemma W then charges the shift \(\log b\) by at least \(c\,b^2(\log b)^2\).

A linear-response estimate near the bolt shows that earlier correction is not cheaper. Forcing \(\Delta e=A\) on \([0,t_1]\), where \(W\sim b^2t\), shifts \(\int(y_g-y_h)\) by \(-At_1^2/4\) at cost \(\sim b^2A^2t_1^2\). A shift of \(\log b\) therefore costs \(\sim b^2(\log b)^2/t_1^2\), which is minimized at \(t_1\sim1\).

## 5. Revised compactness statement

The converse of Theorem D now needs three inputs instead of four:

* **(N) non-round late opening** — covers small-bolt saturation, collapsed shear and every collapsing bounce. It is numerically \(\ge5.37\) for every tested \(\varepsilon\), and round reopening is excluded by Lemma V;
* **(L) large bolt** — follows from the face-limit programme of §4, with growth \(b^2(\log b)^2\);
* **(F) conformal-face escape** — the large-bolt face analysis takes place on the same \(\zeta=0\) face. The face spectrum at \(E(q)\) (\(2,0,-4,-6,-8\)), the AH attractor \(y_i=\sqrt2,\kappa=0\), and Lemma W are the common tools.

Raw high shear that does not collapse is excluded by Lemma V Consequence 2 whenever it raises \(\mathfrak b_-\) above \(7+p_*\) or \(\mathfrak b_+\) above \(1+p_*\). A shear bounce that does neither falls under Lemma W, which prices the volume bounce through \(\mathcal C\).



---

## Source step33_link_charges_global_decomposition_static_channel.md

Original: [sources/Sessions/S1003A02/workspace/notes/step33_link_charges_global_decomposition_static_channel.md](../sources/Sessions/S1003A02/workspace/notes/step33_link_charges_global_decomposition_static_channel.md)

# Step 33 — Chiral link charges without symmetry, the link-separated global decomposition, and the static charge channel for non-round opening

Conventions. \(P(g;\Omega)=\int_\Omega|\operatorname{Ric}^\circ|^2d\mu\), \(\widehat P=P/8\pi^2\). Orientation is the blow-up orientation (the exceptional sphere has square \(-1\); the CH Kähler block is \(W^+\)). For a compact oriented \(\Omega\) with boundary, the Gauss–Bonnet–Chern and Atiyah–Patodi–Singer formulas are written
\[
\chi(\Omega)=\int_\Omega e+\mathcal E(\partial\Omega),\qquad
\int_\Omega L=\tau(\Omega)+\mathcal H(\partial\Omega),
\]
\(e=\frac1{8\pi^2}(|W|^2-\frac12|\operatorname{Ric}^\circ|^2+\frac{s^2}{24})\), \(L=\frac1{12\pi^2}(|W^+|^2-|W^-|^2)\). \(\mathcal E\) is Chern's boundary transgression (intrinsic curvature and second fundamental form of \(\partial\Omega\)); \(\mathcal H=\eta(\partial\Omega)+\int_{\partial\Omega}T_{p_1}\) is the APS eta invariant of the odd signature operator plus the local transgression to a product collar. Both depend only on the metric near \(\partial\Omega\); \(\mathcal E\) and \(\mathcal H\) of a boundary component change sign when its orientation is reversed. With several boundary components, each is oriented as the boundary of \(\Omega\).

## 1. Theorem G (chiral characteristic identity)

For every compact \(\Omega\subset(M^4,g)\) with smooth boundary,
\[
\widehat P(\Omega)=\frac1{2\pi^2}\int_\Omega|W^\pm|^2+\frac1{96\pi^2}\int_\Omega s^2-\bigl(2\chi(\Omega)\pm3\tau(\Omega)\bigr)+\mathcal Q_\pm(\partial\Omega),
\qquad \mathcal Q_\pm=2\mathcal E\mp3\mathcal H .
\]
*Proof.* \(2e\pm3L=\frac1{4\pi^2}(2|W^\pm|^2-\frac12|\operatorname{Ric}^\circ|^2+\frac{s^2}{24})\); integrate and insert the two boundary formulas. \(\square\)

Consequently, for every \(\Omega\),
\[
\widehat P(\Omega)\ \ge\ \max_\pm\bigl[\mathcal Q_\pm(\partial\Omega)-(2\chi\pm3\tau)(\Omega)\bigr],\tag{G}
\]
and on an annulus \(C\) with inner and outer links, \(\widehat P(C)\ge\max_\pm[\mathcal Q_\pm(\text{out})-\mathcal Q_\pm(\text{in})]\) (the inner link enters with reversed orientation). In diagonal Bianchi-IX symmetry \(\mathfrak b=2\mathcal E\), \(\mathfrak s=3\mathcal H\), \(\mathfrak b_\pm=\mathcal Q_\pm\): Theorem X, Lemma Q″ and Lemma V are the symmetric reductions of (G).

### Model link charges \((\mathcal Q_+,\mathcal Q_-)\)

Each value is the charge of the link as outer boundary of the region it encloses.

1. **Small geodesic sphere / round link in an almost flat region:** \((2,2)\). (Ball: \(\chi=1,\tau=0\), interior integrals \(\to0\).)
2. **Flat-conical or ALE spherical-space-form end \(S^3/\Gamma\):** for an exact flat-conical collar, or in the limit along an ALE end, \(\mathcal E\to1/|\Gamma|\), \(\mathcal H\to\eta_\Gamma\), where the eta sign is fixed by the outgoing-link orientation and \(\int L=\tau+\mathcal H\). Thus \(\mathcal Q_\pm\to2/|\Gamma|\mp3\eta_\Gamma\). The intrinsic round metric alone does not determine this charge if the radial first jet is arbitrary. Applied to a smooth complete scalar-flat ALE bubble \(N\), (G) gives \(\widehat P(N)\ge 2/|\Gamma|-2\chi+3|\tau+\eta_\Gamma|\), exactly Lemma Q of Step 20; its near-Euclidean \(\Gamma=1\) neck form is Lemma Q′. Regions containing an actual orbifold singularity require the orbifold characteristic corrections.
3. **Thin tube around an embedded surface \(\Sigma\) with self-intersection \(n\neq0\):** for a fixed smooth ambient metric, as the tube radius tends to zero, \(\int e,\int L\to0\) on the disk bundle \(D(n)\), \(\chi(D)=\chi(\Sigma)\), \(\tau(D)=\operatorname{sgn}n\). Hence \(\mathcal E\to\chi(\Sigma)\), \(\mathcal H\to-\operatorname{sgn}n\), and
\[
\mathcal Q_\pm(\text{tube})=2\chi(\Sigma)\pm3\operatorname{sgn}n .
\]
For the \((-1)\)-sphere this is \((4-3,\,4+3)=(1,7)\), the diagonal bolt charge, now derived without symmetry and without any regularity of the bolt beyond smoothness.
4. **Taub–NUT-chirality Hopf-adiabatic Berger link with controlled collar:** \((-2,2)\). Reversing the four-dimensional orientation exchanges the two charges, giving \((2,-2)\). Self-contained derivation: for the Taub–NUT metric (a ball, \(\chi=1,\tau=0\), Ricci-flat, \(W^-=0\) in this orientation), the outer link at radius \(R\to\infty\) is an adiabatically collapsing Berger sphere with bounded base geometry and bounded second fundamental form, so \(\mathcal E\to0\): every term of Chern's boundary integrand contains a principal curvature times link curvature or a cubic in principal curvatures; here the fibre principal curvature is \(O(R^{-2})\), the base ones \(O(R^{-1})\), the link sectional curvatures \(O(R^{-2})\) (base–base) and \(O(R^{-4})\) (fibre–base), and the link area is \(O(R^2)\), so \(\mathcal E=O(R^{-2})\). The index structure of Chern's integrand is essential here: its terms pair a principal curvature with the sectional curvature of the complementary plane, or multiply all three principal curvatures. Then Gauss–Bonnet gives \(\frac1{8\pi^2}\int|W^+|^2=1\), hence \(\int L=2/3\) and \(\mathcal H\to2/3\). So \(\mathcal Q_+=0-2=-2\), \(\mathcal Q_-=0+2=2\). This derivation uses the Ricci-flat half-conformally-flat Taub–NUT filling. It is not a formula for an arbitrary half-conformally-flat filling: in general the scalar and trace-free Ricci terms alter the relation between \(\mathcal H\) and \(\mathcal E\).
   The diagonal formula (`scripts/berger_eta_charge.py`, `data/berger_eta_charge.json`) gives for \(h_\lambda=\lambda^2\sigma_f^2+\sigma_g^2+\sigma_h^2\) with radial jets \(a_f'=\lambda V\), \(a_g'=a_h'=U\):
   \[
   \mathfrak s=2(1-\lambda^2)^2+\lambda^2(U-V)^2 ,
   \]
   exact (residual 0). The first term is intrinsic and equals \(3\eta_{\rm APS}(\lambda)\) with \(\eta_{\rm APS}=\frac23(1-\lambda^2)^2\) (blow-up orientation, lift anchored by \(\eta(1)=0\)); its \(\lambda\to0\) value \(2/3\) agrees with the Taub–NUT derivation above, which uses no eta formula at all. (The script encodes the eta formula as an input; the Taub–NUT argument is the independent check.) The second term is the collar transgression \(\int T_{p_1}\): it vanishes for a product or conical collar and is the precise reason an intrinsic eta cannot price uncontrolled radial shear.
5. **CH geodesic sphere of radius \(\tau\):** \((2-9\sinh^4\tau,\ 2-3\sinh^4\tau)\); from (G) on the CH ball, since \(\frac1{96\pi^2}\int_{B_\tau}s^2=3\sinh^4\tau\) (\(\operatorname{Vol}B_\tau=\frac{\pi^2}2\sinh^4\tau\)) and \(\frac1{2\pi^2}\int_{B_\tau}|W^+|^2=6\sinh^4\tau\).

The lower pricing rule "bubble cost is at least outgoing charge minus incoming charge" is therefore a theorem about links, not about symmetry (and applies in this pure form to a product-topology annulus): an exceptional class enclosed by a round link costs \(2-1=1\); after Hopf-adiabatic collapse, reopening to a round link costs \(2-(-2)=4\); a CH sphere is a link whose \(\mathcal Q_+\) deficit \(9\sinh^4\tau\) equals the Weyl-plus-scalar energy deleted from the CH ball.

### Volume-renormalized charges (scalar-normalized class)

If \(s\equiv-24\) on \(\Omega\), \(\frac1{96\pi^2}\int_\Omega s^2=3\widehat V(\Omega)\) with \(\widehat V=2\operatorname{Vol}/\pi^2\) (CH ball: \(\widehat V=\sinh^4\tau\)). Put \(\mathfrak B_\pm=\mathcal Q_\pm+3\widehat V\). Then \(\widehat P(\Omega)\ge\mathfrak B_\pm(\partial\Omega)-(2\chi\pm3\tau)\), and pathwise on a radial family \(\widehat P\ge\int\max\{0,\mathfrak B_+',\mathfrak B_-'\}\). On CH, \(\mathfrak B_-\) is constant and \(\mathfrak B_+\) strictly decreasing. For an \(O(-1)\) cell ending in an exact CH collar at \(\tau\), the \(\mathfrak B_-\) bound is the relative-signature form \(-5+3(\widehat V_{\rm cell}-\widehat V_{\rm CH})+\dots\) of Theorem C. For a non-round opening from a collapsed section (charges \((-2,2)\), volume \(\widehat V_c\)) to a CH sphere at \(\tau\):
\[
\widehat P\ \ge\ 4-9\sinh^4\tau+3\Delta\widehat V,\qquad \widehat P\ \ge\ 3(\Delta\widehat V-\sinh^4\tau),
\]
so a cell below \(p_*\) must satisfy \(\Delta\widehat V<\sinh^4\tau+p_*/3\) and \(9\sinh^4\tau>4-p_*+3\Delta\widehat V\). These are volume budgets for the opening; with Riccati control of the mean curvature they do not by themselves exclude opening at \(\tau\gtrsim0.8\).

## 2. The link-separated global decomposition

Let \(M=X\#k\overline{\mathbb{CP}}^2\#\ell(S^1\times S^3)\) and let \(D\subset M\) be a compact region with connected boundary link such that \(D\cong(\#k_D\overline{\mathbb{CP}}^2\#\ell_D(S^1\times S^3))\setminus B^4\). Then \((2\chi+3\tau)(D)=2-k_D-4\ell_D\), and (G) gives
\[
P(g)\ \ge\ P(g;D)\ \ge\ 8\pi^2\Bigl[k_D+4\ell_D-\bigl(2-\mathcal Q_+(\partial D)\bigr)\Bigr].\tag{G1}
\]
The constant \(k+4\ell\) of Theorem C is the round-link value. Disjoint regions add.

**Corollary G2 (disjoint round separation forces the bubble price).** If \(D_1,\dots,D_m\) are pairwise disjoint, carry \(k_i\) exceptional classes and \(\ell_i\) handles, and \(\mathcal Q_+(\partial D_i)\ge2-\varepsilon_i\), then \(P(g)\ge8\pi^2\sum_i(k_i+4\ell_i-\varepsilon_i)\). Since the charge of an outer \(S^3\) collar converging after rescaling in \(C^2\) to the flat-conical germ on the bounded side is \(2-o(1)\), a sequence with pairwise disjoint regions satisfying \(\sum_i k_i=k\) and \(\sum_i\varepsilon_i=o(1)\) has \(\liminf P\ge8\pi^2k\). A single region enclosing all \(k\) classes gives the same conclusion. Merely giving each class some possibly nested or intersecting link does not allow the local energies to be added.

**Corollary G3 (subunit sequences admit no Euclidean-round \(S^3\) separation of the exceptional subtree).** Let \(X\) be a compact ball quotient whose injectivity radius exceeds the outer radius of the certified cell (available on suitable finite covers). Inserting the certified perpendicular cell gives a metric on \(X\#\overline{\mathbb{CP}}^2\) with \(\widehat P\le p_*=0.995848\). By (G1), every metric with \(\widehat P<1-\varepsilon\) and every standard negative-definite blow-up region \(D\) with \(b_2^-(D)=1,b_2^+(D)=b_1(D)=0\) satisfy
\[
\mathcal Q_+(\partial D)\le1+\widehat P(D)\le1+\widehat P(g)<2-\varepsilon.
\]
Thus such a region cannot have an outer \(S^3\) collar converging to the Euclidean flat-conical germ, even if the exceptional subtree contains further inner bubbles. More generally, any separating link with \(\mathcal Q_+>1+\widehat P(g)\) is excluded. This does **not** exclude orbifold \(S^3/\Gamma\) necks, Taub–NUT-chirality Hopf collapse with \(\mathcal Q_+\approx-2\), curved or sheared links below the charge threshold, pure bulk bubbling, or regions also carrying positive intersection form.

For several classes, if pairwise disjoint standard negative-definite regions carrying a total of \(K\) classes all satisfy \(\mathcal Q_+\ge2-\varepsilon\), then \(K\le\lfloor\widehat P/(1-\varepsilon)\rfloor\). With a separated-cell upper bound of order \(kp_*\), this guarantees only that at least \(k-\lfloor kp_* /(1-\varepsilon)\rfloor\) classes fail such disjoint round separation; it does not keep every class unseparated. In real-hyperbolic bulk, by contrast, the conditional Theorem H gives \(\inf P=8\pi^2k\) with Burns sequences realizing round-link concentration.

**What the decomposition leaves.** (G1) prices cells by their links but the bulk \(B=M\setminus\cup D_i\) satisfies the complementary identity
\[
\widehat P(B)=\frac1{2\pi^2}\int_B|W^+|^2+\frac1{96\pi^2}\int_Bs^2-(2\chi+3\tau)(B)-\sum_i\mathcal Q_+(\partial D_i),
\]
whose lower bound requires field information on \(B\). The global LeBrun/Seiberg–Witten estimates are integrated over all of \(M\). Their localization to \(B\) produces two link terms of the same type: the flux \(\oint_{\partial B}\partial_\nu|\psi|^2\) from \(\int\Delta|\psi|^2\) in the Weitzenböck identity, and the Chern–Simons term \(\mathrm{CS}(A|_{\partial B})\) in \(\frac1{4\pi^2}\int_B(|F_A^+|^2-|F_A^-|^2)=c_1^2[B]+\mathrm{CS}\). A matching bulk-plus-cells theorem therefore needs **link regularity**: a selection of links \(\partial D_i\) on which (a) the Euler and signature transgressions converge (in particular the second fundamental form, including the \(\lambda^2(U-V)^2\)-type collar shear, is controlled), (b) the SW flux and Chern–Simons terms converge, and (c) along collapsing links, the small nonzero eigenvalues of the odd signature operator contribute the Dai adiabatic correction in a controlled way. (For noncollapsing links, \(C^2\) collar convergence—or an equivalent Sobolev hypothesis controlling the boundary connection, curvature, and second fundamental form—gives convergence of these terms; \(C^1\) collar convergence alone is insufficient for the Chern–Simons/transgression integrals.) Under link regularity the problem splits exactly into cell infima priced by \(\mathcal Q_\pm\) jumps and a bulk-with-links SW problem. Supplying (a)–(c) from near-minimality and critical \(L^2\) control, without pointwise Ricci bounds, is the precise remaining selection problem of the global passage.

## 3. Static test of Lemma V for non-round opening (Lemma Z)

In scale-free first-jet coordinates \(X=(u_f,u_g,u_h,\beta,q)\), \(u_i=a_i'-\gamma_i\),
\[
\mathfrak b_+=2-|u|^2-u_fu_gu_h\quad(\text{independent of shape}),\qquad
\mathfrak b_-=|w|^2-w_fw_gw_h-2,\ w=u+2\gamma(\beta,q).
\]
Collapsed (Taub–NUT/ALF) state: \(u\to(1,1,-2)\), \(h\)-slot collapsed. CH orbit at \(\tau\): \(u=(3\sinh^2\tau,0,0)\), \(\beta=\log\cosh\tau\), \(q=0\).

**Lemma Z.** (i) \(\mathfrak b_+\) alone gives no static obstruction: for \(A>5/2\) the path \((1,1,-2)\to(A,1,-2)\to(A,s,-2s)_{s:1\to0}\) has \(|u|^2+u_fu_gu_h=(A-1)^2+4\), then \(A^2+s^2(5-2A)\), both nondecreasing, so \(\mathfrak b_+\) is nonincreasing; the shape is free because \(\mathfrak b_+\) does not depend on it. The endpoint is the CH orbit with \(3\sinh^2\tau=A\) (\(\tau>0.816\)). (ii) On the jet family \(u=(A,A,-2)\) (base expansion rate \(A\)), \(\mathfrak b_+\equiv-2\) exactly, and at collapsed shape with ratio \(\lambda\), \(\mathfrak b_-=2(1+\lambda^2(A^2-4)+4A\lambda^3+6\lambda^4)\to2\): the base expansion rate is charge-neutral in the collapsed limit. (Exact checks of (i),(ii): `scripts/lemmaZ_exact.py`, `data/lemmaZ_exact.json`.) (iii) Jointly, numerical minimization of the polygonal \(\Lambda=\int\max(0,d\mathfrak b_+,d\mathfrak b_-)\) (`scripts/static_charge_path.py`, `data/static_charge/path_*.json`, step bound 0.25, 120 nodes, refined 40× on the linear interpolation) finds paths from the collapsed state (\(\lambda=0.02\)) to CH orbits at \(\tau\approx0.82\)–\(0.84\) with refined \(\Lambda=0.050\) and \(0.021\), \(|u|\le2.7\), maximal rises above running minima \(\le0.008\). With the endpoint forced to \(\tau\in[0.70,0.71]\) and \(|u|\le3\) (200 nodes) the minimizer has \(\Lambda=0.824\), essentially the unavoidable endpoint increment \(\mathfrak b_+(\tau)-\mathfrak b_+(\text{start})=0.816\): the static value is the endpoint bound \(\max\{0,4-9\sinh^4\tau\}\) up to discretization, nothing more. (Two further random/detour starts at 200/320 nodes did not converge and are not evidence.)

So Lemma V cannot prove the non-round input by any static argument: the sublevel geometry contains a monotone channel. The channel is explicit (data file): the state stays triaxial with \(a_f\) the largest slot throughout (\(a_f/a_g\) from 1 to 1.38, never round), \(u_f\) rises to \(\approx2.6\) while \(\mathfrak b_-\) stays at \(\approx2\), then \(q\) descends from \(3.9\) to \(0\) (slot \(h\) opens to match \(g\)) while both charges decrease. This is the same triaxial swap the dynamic optimizer performs (Step 32 profile). What the static test ignores is kinematics: shape velocity is not free but determined by the jets (\(q'=y_g-y_h\), \(\beta'\) similarly) and jets change only through the controlled second-order flow. The cost of the swap therefore lives in the Weyl/scalar densities \(\omega_\pm\) along kinematically admissible paths, consistent with the \(D\)-dominated split (4.30 of 6.48). A lower theorem for (N) must be a Hamilton–Jacobi subsolution \(V=\mathfrak b_++\phi(X)\) with \(\phi\) shape/jet dependent and \(\nabla\phi\cdot f\le\omega_+\) on the kinematic band, or the peer Green identity \(M=-\int WDK\) with kinematics; charges alone are exhausted.

## 4. Status

Proved: Theorem G; model charges 1–5 with the collar, chirality, and smooth-tube scopes stated above; (G1); the corrected finite disjoint-region G2; and the one-blow-up charge bound (G3), which excludes Euclidean-round \(S^3\) separation of the standard exceptional subtree but not general bubble trees. Proved exact: Lemma Z(i),(ii). Numerical: Lemma Z(iii). Open: link-regularity selection; the matching bulk estimate using global field information and same-metric cell accounting; the kinematic lower bound for (N); large-bolt Theorem L and face no-return. Step 34 gives the independent verification, the symmetry-free constraint calculus, and the exact obstruction to a \(\mathfrak b_++\phi(q,\eta)\) certificate.



---

## Source step34_characteristic_constraint_calculus_and_N_probe.md

Original: [sources/Sessions/S1003A02/workspace/notes/step34_characteristic_constraint_calculus_and_N_probe.md](../sources/Sessions/S1003A02/workspace/notes/step34_characteristic_constraint_calculus_and_N_probe.md)

# Step 34 — Verified characteristic–constraint link calculus and the first HJ probe of non-round opening

Conventions are those of Steps 27–33: the curvature sign makes round spheres positively curved; on a collar in Gaussian gauge
\[
g=dt^2+h_t,
\qquad K=\tfrac12\partial_t h_t,
\qquad \Theta=\operatorname{tr}_{h_t}K,
\]
and \(\widehat P=P/(8\pi^2)\). The four-dimensional orientation is the blow-up orientation unless explicitly reversed.

## 1. Independent verification and corrections to Theorem G

The two independent readings in
`trace/ttcs/results/step34_ttcs01_verifier1_integration.md` confirmed the normalization
\[
\widehat P(\Omega)=\frac1{2\pi^2}\int_\Omega|W^\pm|^2
 +\frac1{96\pi^2}\int_\Omega s^2
 -(2\chi\pm3\tau)(\Omega)+\mathcal Q_\pm(\partial\Omega),
\qquad
\mathcal Q_\pm=2\mathcal E\mp3\mathcal H,
\tag{G}
\]
where
\[
\chi=\int e+\mathcal E,
\qquad
\int L=\tau+\mathcal H.
\]
For a product-topology annulus the inner link has the reversed boundary orientation, so
\[
\widehat P(C)\ge \mathcal Q_\pm(\Sigma_{\rm out})-\mathcal Q_\pm(\Sigma_{\rm in}).
\]
If the region between the links carries topology, the term \(-(2\chi\pm3\tau)(C)\) remains. A charge jump is therefore a lower payment; it is the complete energy only when the chosen Weyl and scalar remainders vanish.

The following model signs were confirmed.

* A thin radius-\(r\) disk bundle around a fixed smooth embedded \(\Sigma\) of normal Euler number \(n\) has
  \[
  \chi(D(n))=\chi(\Sigma),\quad \tau(D(n))=\operatorname{sgn}n,
  \quad
  \mathcal Q_\pm\to2\chi(\Sigma)\pm3\operatorname{sgn}n.
  \]
  Hence a \((-1)\)-sphere has \((\mathcal Q_+,\mathcal Q_-)=(1,7)\). Along a degenerating metric sequence the tube must be taken below the curvature scale for this fixed-smooth-germ limit to apply.

* At a flat-conical/ALE end \(S^3/\Gamma\), with the outgoing-link orientation and APS convention above,
  \[
  \mathcal Q_\pm\to\frac2{|\Gamma|}\mp3\eta_\Gamma.
  \]
  Thus a smooth complete scalar-flat ALE bubble satisfies
  \[
  \widehat P\ge\frac2{|\Gamma|}-2\chi+3|\tau+\eta_\Gamma|,
  \]
  exactly Lemma Q. The intrinsic round quotient alone does not determine the charge if its radial first jet is arbitrary; actual orbifold singularities also require orbifold characteristic corrections.

* For Taub–NUT in the blow-up orientation, \(W^-=0\), \(\operatorname{Ric}=0\), \(\chi=1\), \(\tau=0\). At its ALF links, the Euler transgression is \(O(R^{-2})\): the alternating index structure pairs the small fibre principal curvature with the complementary base curvature, or multiplies all three principal curvatures. Hence \(\mathcal E\to0\), \(\mathcal H\to2/3\), and
  \[
  (\mathcal Q_+,\mathcal Q_-)\to(-2,2).
  \]
  Reversing four-dimensional orientation exchanges the charges, yielding \((2,-2)\). The relation between \(\mathcal H\) and \(\mathcal E\) used here is a property of the Ricci-flat half-conformally-flat filling, not of an arbitrary half-conformally-flat filling. Unbounded radial collar shear also changes the limiting charge.

For
\[
D\cong(\#^{k_D}\overline{\mathbb{CP}}^{\,2}\#^{\ell_D}(S^1\times S^3))\setminus B^4,
\]
the verified bound remains
\[
\widehat P(D)\ge k_D+4\ell_D-(2-\mathcal Q_+(\partial D)).
\tag{G1}
\]
Its Betti-number form for an \(S^3\) boundary is
\[
\widehat P(D)\ge b_2^-+4b_1-5b_2^+-(2-\mathcal Q_+(\partial D)).
\]
The finite disjoint-region addition is valid. The old broader reading of G3 was corrected: when \(k=1\) and \(\widehat P<1-\varepsilon\), every standard negative-definite blow-up region obeys
\[
\mathcal Q_+(\partial D)\le1+\widehat P(D)\le1+\widehat P(g)<2-\varepsilon.
\tag{G3}
\]
Thus the exceptional subtree cannot be separated from the bulk by an outer \(S^3\) collar converging in \(C^2\) to the Euclidean flat-conical germ. This remains true even if there are deeper inner bubbles. It does not exclude \(S^3/\Gamma\) necks, Taub–NUT-chirality collapse, curved or sheared links under the charge threshold, bulk bubbling, or regions carrying positive intersection form. For multiple classes, addition requires pairwise disjoint regions (or one region enclosing all classes), so the numerical count applies only to the classes contained in such a disjoint family.

The detailed corrections were inserted into `notes/step33_link_charges_global_decomposition_static_channel.md` and should supersede its original G3 title and broad degeneration sentence.

## 2. The symmetry-free characteristic–constraint link calculus

The hypersurface equations give the second half of the link theory. The traced Gauss equation implies
\[
R_{h_t}=s-2\operatorname{Ric}(\nu,\nu)+\Theta^2-|K|^2.
\]
Define
\[
\mathcal C:=\operatorname{Ric}^\circ(\nu,\nu)
 =\frac12(\Theta^2-|K|^2-R_h)+\frac{s}{4},
\tag{2.1}
\]
so for \(s=-24\), \(\mathcal C=\frac12(\Theta^2-|K|^2-R_h)-6\). Contracted Codazzi gives the momentum residual
\[
\mathcal J:=\operatorname{Ric}^\circ(\nu,\cdot)
 =\operatorname{div}_{h_t}K-d\Theta.
\tag{2.2}
\]
The tangential trace-free evolution residual is
\[
\mathcal S:=\left(\operatorname{Ric}^\circ|_{T\Sigma_t}\right)^{\circ_h}
 =\left(\operatorname{Ric}^{h_t}-\partial_tK-\Theta K+2K^2\right)^{\circ_h}.
\tag{2.3}
\]
Orthogonality gives the exact pointwise identity
\[
|\operatorname{Ric}^\circ|^2
 =\frac43\mathcal C^2+2|\mathcal J|^2+|\mathcal S|^2.
\tag{2.4}
\]
Thus \(P\) controls the squared Hamiltonian, momentum, and tangential evolution residuals, but it does not separately control \(R_h\), \(K\), \(\Theta\), injectivity radius, lapse, focal radius, or any boundary transgression.

Every exact transport identity
\[
\mathcal A(\Sigma_b)-\mathcal A(\Sigma_a)-\mathcal F
=\int_C\bigl(f\mathcal C+\langle X,\mathcal J\rangle+\langle T,\mathcal S\rangle\bigr)d\mu
\tag{2.5}
\]
has the dual consequence
\[
\widehat P(C)\ge
\frac{|\mathcal A_b-\mathcal A_a-\mathcal F|^2}
{8\pi^2\int_C(\frac34f^2+\frac12|X|^2+|T|^2)d\mu}.
\tag{2.6}
\]
The reference drift \(\mathcal F\) is indispensable: an Einstein metric can have nontrivial hypersurface evolution at zero defect.

In diagonal Bianchi IX, \(\mathcal J=0\), and
\[
\mathcal C=\sigma_2(y)-6-\frac12R^{(3)},
\qquad
\widehat P=\int W\left(\frac{\mathcal C^2}{3}+\frac{E^2}{6}+\frac{D^2}{8}\right)dt.
\]
This is Lemma N. The CR observable satisfies \(\widetilde\Phi'=F_\Phi-D/4\), and the fibre/base observable satisfies \(\widetilde B'=F_\beta-E/4\); these are projections of \(\mathcal S\), not of the Codazzi momentum residual. The exact Green identity for \((Wq')'=W(P_g-P_h-D)\) is another weighted transport form of the same \(D\)-channel.

The unified statement is therefore:

* the characteristic channel (G) prices topology and boundary-germ changes through Euler, APS, and collar transgressions;
* the constraint/kinematic channel (2.1)–(2.6) prices drift-corrected changes of intrinsic link geometry and second fundamental form through \(\mathcal C,\mathcal J,\mathcal S\);
* their lower bounds are generally combined by a maximum, not added, unless the regions or defect components have been separated;
* link regularity is convergence/control of precisely the link germ \((h,K)\), its characteristic and spectral transgressions, and any field boundary data needed on the bulk side.

This is a theorem-level accounting principle, not a compactness result. Critical \(L^2\) control of \(\operatorname{Ric}^\circ\) alone does not supply controlled links, convergence of transgressions, Dai small-eigenvalue terms, or localized Seiberg–Witten fluxes.

## 3. Exact HJ reduction and why \(\mathfrak b_++\phi(q,\eta)\) does not strengthen N

For the exact scale-free controlled system
\[
X=(x,z,p,\chi,\eta),\quad q=-3\log z,
\]
\[
\begin{aligned}
x'&=\chi,&q'&=\eta,\\
p'&=A_p-\bar H/2,&
\chi'&=A_\chi-\bar E+\bar D/2,&
\eta'&=A_\eta-\bar D,
\end{aligned}
\]
with
\[
L=\frac{3\bar H^2}{16}+\frac{\bar E^2}{6}+\frac{\bar D^2}{8},
\]
let \(b=\mathfrak b_+\) and \(V=b+\phi(q,\eta)\). Maximizing \(\dot V-L\) over the three controls yields
\[
\bar H_*=-\frac43b_p,
\qquad
\bar E_*=-3b_\chi,
\qquad
\bar D_*=2b_\chi-4(b_\eta+\phi_\eta).
\]
A direct exact SymPy reduction (`scripts/hj_symbolic_reduction.py`, `data/saturation_control/hj_symbolic_reduction.json`) proves
\[
\sup_{\bar H,\bar E,\bar D}(\dot b-L)\equiv0.
\tag{3.1}
\]
This is the Hamilton–Jacobi form of the chiral identity: the charge itself is an exact calibration, not a strict subsolution with unused pointwise slack. Put
\[
K=A_\eta-2b_\chi+4b_\eta.
\]
Then \(V=b+\phi(q,\eta)\) is a global subsolution only if
\[
\boxed{\eta\phi_q+K\phi_\eta+2\phi_\eta^2\le0}
\tag{3.2}
\]
pointwise on the domain. The exact, nonzero formula for \(K\) is stored in the same JSON file.

Equation (3.2) exposes the obstruction. At a fixed \((q,\eta)\), the hidden variables \((x,p,\chi)\) vary \(K\). A common \(\phi\) must work for the whole hidden-state fibre. Any \(q\)-only potential satisfies \(\eta\phi_q\le0\). On the swap band \(\eta<0\), increasing the endpoint lower bound requires the opposite sign of \(\phi_q\), so no \(q\)-only function improves the charge bound. Allowing \(\phi_\eta\) can exploit the linear \(K\)-term only if the hidden-state fibres give coherent sign and magnitude for \(K\); the nonnegative \(2\phi_\eta^2\) prevents a universal gain where \(K\) changes sign or approaches zero.

`scripts/hj_qeta_probe.py` evaluated the exact reduction on the cap-\(-1\) optimizer trajectories for \(\varepsilon=1/16,1/32,1/64\), writing `data/saturation_control/hj_qeta_probe.json`. This is a finite-sample route probe, not a proof over state space. It found:

* \(\sup(\dot b-L)\) is zero to floating error (sampled \(m=-\sup(\dot b-L)\) in \([-2.9\times10^{-11},3.0\times10^{-12}]\));
* \(K\) ranges from about \(-3.34\) to \(4.46\) along the three paths and changes sign through the swap;
* a convex search for \(\phi=-aq+bq^2+cq\eta+d\eta^2\) on the sampled descending swap segments returns zero maximal \(\phi\)-gain (\(-1.7\times10^{-10}\) numerically), with coefficients essentially zero.

So the bounded-effort \(\phi(q,\eta)\) route is exhausted more strongly than anticipated: the exact charge calibration has no pointwise margin to redistribute, and the sampled hidden-state dynamics makes the \(K\)-lever sign-incoherent. A nontrivial subsolution must use at least one additional geometric/jet variable, split the domain into regions with boundary matching, or use a different exact structure rather than merely decorating \(\mathfrak b_+\) by \((q,\eta)\).

## 4. The canonical almost-Kähler identity is the stronger next structure

Peer S1003A01 supplied an exact identity for every smooth diagonal exact-CH perpendicular \(O(-1)\) cell; see `Sessions/S1003A01/workspace/notes/step28_AK_gap_identity_nijenhuis_transport.md`. The metric is canonically conformal to a diagonal almost-Kähler metric \(\hat g=u^2g\), and with its Nijenhuis scalar \(\nu\), \(W_3^+\) eigenvalue \(\lambda\), and the nonnegative quantities \(H,G,Q_\delta,Q_A,N\) defined there,
\[
\boxed{
\widehat P-1
=12H+6G+\frac32Q_\delta+\frac12Q_A-\frac32N+\Sigma.
}
\tag{4.1}
\]
For \(s=-24\), \(\Sigma=0\). The only negative term is the Nijenhuis energy. The exact transport
\[
\lambda=\frac12\nu_T+\beta\nu,
\qquad
(\mu\nu)_T=2\mu\lambda,
\tag{4.2}
\]
forces the perpendicular bolt's Nijenhuis charge to unwind before the CH collar. A Hardy estimate makes
\[
2\int\lambda^2d\hat V-6\int\nu^2d\hat V\ge0
\]
on every tail where \(\Lambda\ge4\sqrt3\); on CH this begins at \(\sinh^2R=3+3\sqrt{15}/4\). Hence every possible subunit saving is generated in a compact near zone. The numerical \(x_0=.038,X=128\) identity is satisfied to \(2.1\times10^{-10}\):
\[
\widehat P-1=-0.0047126289,
\]
with contributions
\[
12H=0.0033318,
\quad6G=0.0556282,
\quad\tfrac32Q_\delta=0.0011325,
\quad\tfrac12Q_A=0.0328569,
\quad-\tfrac32N=-0.0976572,
\]
and \(\Sigma=-4.75\times10^{-6}\).

An independent Step-34 verification (`trace/ttcs/results/step34_ttcs02_verifier1_integration.md`) checked every coefficient and exposed the correct near-zone object. Two scope points matter. The canonical almost-Kähler metric is singular at the perpendicular bolt, although all displayed energies are integrable; Stokes arguments must be made on a truncated cell and passed to the bolt using the smooth original-metric expansions. Also the header of `step28_ak_nu_structure.py` says \(A_gA_h=2\phi\), but the formulas and the correct normalization have \(A_gA_h=\phi\).

Put \(v=u^{-1}\), \(\rho=(\log v)_T\), \(w=A_fA_gA_h\), and \(m_0=(\log w)_T\). The exact scalar/conformal coupling is
\[
\delta=\rho_T+\rho^2+m_0\rho+\nu^2+4(1-v^2),
\]
while \(2\lambda=\nu_T+2\beta\nu\). Thus at \(s=-24\)
\[
\widehat P-1=\int w\left[6\rho^2-6\nu^2+\frac12(\nu_T+2\beta\nu)^2+\frac32\delta^2+12(v^2-1)^2\right]dT.
\tag{4.3}
\]
Equivalently, with \(z=\mu\nu\) and \(m=w/\mu^2\), the indefinite sector is
\[
\int m\left(\frac12z_T^2-6z^2\right)dT,
\]
a compact weighted Sturm–Liouville problem with forced bolt charge and zero terminal charge. The far Hardy estimate is an endpoint interval statement: it uses \(\nu=0\) at the exact collar and cannot be applied to a disconnected set merely because \(\Lambda\ge4\sqrt3\) there.

This identity is stronger than \(b_++\phi(q,\eta)\), but it does not support a universal \(\widehat P\ge1\): the certified subthreshold cells are precisely negative middle-zone modes. In the \(x_0=.038\) record the near zone contributes approximately \(-0.01059\), while the far tail returns only \(+0.00588\), leaving the observed deficit \(-0.00471\). The plausible theorem is therefore a sharp subunit lower value and classification of the coupled weighted mode, or a conditional unit bound under an additional coercive middle-zone hypothesis—not a contradiction of the already certified subunit metrics. The next construction task for N is to determine the lowest coupled compact action (4.3), with the smooth-bolt and exact-CH boundary data, and compare it with the required branch threshold. If one focused attempt does not produce a rigorous estimate, N should remain a named numerical-margin input while work moves to the large-bolt and face theorems.

## 5. Consequences for the global programme

The characteristic–constraint calculus now supplies the requested common mechanism beyond symmetry:

1. Theorem G, Lemma Q, Theorem F, and Q″ are relative characteristic calibrations. They price topology only after the whole boundary germ—including radial collar data—is controlled.
2. Gauss–Codazzi splitting and transport identities price the shape and first-jet changes that charges cannot see. Lemma Z and (3.1) show why this second channel is mathematically independent rather than a technical refinement.
3. The global monopole estimate is blow-up blind through \(\beta^2(X\#k\overline{\mathbb{CP}}^2)=c_1^2(X)\). It should pin the regular bulk's global scalar/Weyl budget, while Theorem G and Theorem C price the cells on the same metric. A localized boundary-value monopole theory is not the first missing ingredient.
4. For a ball-quotient one-blow-up sequence below one unit, G3 excludes Euclidean-round separation of the exceptional ALE subtree. The remaining possibilities include collapse, curved/sheared links, orbifold necks, and bulk behaviour; these are exactly where controlled link germs and the constraint channel are needed. This is sharper than saying that all bubble trees are excluded.

The corrected link-charge note and this calculus should be used together. The central unresolved issue remains deriving controlled link germs and sufficient near-zone kinematic coercivity from near-minimality, not another static topological charge.


---

## Source step35_calibration_theorem_and_branch_classification.md

Original: [sources/Sessions/S1003A02/workspace/notes/step35_calibration_theorem_and_branch_classification.md](../sources/Sessions/S1003A02/workspace/notes/step35_calibration_theorem_and_branch_classification.md)

# Step 35 — The b₊ calibration, its leaves, and what the non-round input (N) actually lacks

Conventions: Steps 27–34. Scale-free state \(X=(x,z,p,\chi,\eta)\), \(q=-3\log z\), controls \(c=(\bar H,\bar E,\bar D)\), running cost \(L(c)=\frac3{16}\bar H^2+\frac16\bar E^2+\frac18\bar D^2\) (units \(8\pi^2\)).

## 1. Exact calibration statement

The chiral identity (Theorem X) gives, pointwise in \(\tau\),
\[
L(c)-\dot{\mathfrak b}_+(X,c)=\frac1{2\pi^2}|W^+|^2+\frac1{96\pi^2}s^2\quad(\text{normalized density})\ \ge0 .
\]
\(\dot{\mathfrak b}_+\) is affine in \(c\) and \(L\) is a positive-definite quadratic form \(M=\mathrm{diag}(3/16,1/6,1/8)\). Step 34 (`scripts/hj_symbolic_reduction.py`) proved \(\sup_c(\dot{\mathfrak b}_+-L)\equiv0\), attained at
\[
c^*=\Bigl(-\tfrac43\partial_p\mathfrak b_+,\ -3\partial_\chi\mathfrak b_+,\ 2\partial_\chi\mathfrak b_+-4\partial_\eta\mathfrak b_+\Bigr).
\]
Hence, exactly,
\[
\boxed{\;L(c)-\dot{\mathfrak b}_+=L(c-c^*)=:\omega_+\;,\qquad \widehat P=\Delta\mathfrak b_++\int\omega_+\,d\tau .}
\]
**Consequences.** (i) The calibrated curves (\(c=c^*\)) are exactly the diagonal metrics with \(W^+=0\), \(s=0\) (ASD scalar-flat). (ii) \(\ker M=0\), so the Cauchy–Schwarz route "\(\dot I=\ell\cdot(c-c^*)\Rightarrow\int\omega_+\ge(\Delta I)^2/\int\ell^TM^{-1}\ell\)" has no kernel defect; the human's first condition is automatically satisfied here. What remains for such a bound is a transverse function \(I\) with nonzero endpoint separation and a uniform denominator along *all* competing paths.
(iii) Corrections to the strategist note: Burns is a calibrated leaf (cost \(=\Delta\mathfrak b_+=1\)); **Taub-bolt is not** (it is Ricci-flat, \(\Delta\mathfrak b_+=-3\), \(\int|W^+|^2\)-part \(=3\)); CH is not (its ball from the centre has \(\Delta\mathfrak b_+=-9\sinh^4\tau\) and \(\int\omega_+=9\sinh^4\tau\)). Numerically \(L(c^*)=\dot{\mathfrak b}_+(c^*)\) to \(10^{-13}\) relative at random states, and \(\mathfrak b_+(\mathrm{ch}(\tau))=2-9\sinh^4\tau\) to \(10^{-15}\) (`data/saturation_control/calibrated_flow_leaves.json`).

## 2. The calibrated leaves through the two endpoints (endpoint separation)

`scripts/calibrated_flow_leaves.py` integrates \(f(X,c^*(X))\):

* **Forward from the Λ-Taub–NUT collapsed entry** (\(\varepsilon=1/16,1/64\); \(A=.5,1,2\)): every leaf converges to the Euclidean round fixed point \(X_0=(0,1,1,0,0)\), \(\mathfrak b_+\uparrow2\). This is the ASD scalar-flat decollapse found by the optimizer (cost \(2-\mathfrak b_+^{\rm entry}\to4\)). The transverse block at \(X_0\) has eigenvalues \(-2,-4\): the round point attracts the antisymmetric sector.
* **Backward from exact CH jets** \(\mathrm{ch}(\tau)\), \(\tau\in\{.5,.70,.72,.74,.758,.8,1,1.5,2.3\}\): every leaf stays in the biaxial set \(\Sigma=\{q=0,\eta=0\}\) and blows up (\(\chi\to\infty\), \(\mathfrak b_+\to-\infty\)) in finite \(\tau\in[.03,.66]\). None approaches the collapsed set or the bolt.

\(\Sigma\) is invariant under the full controlled flow with \(D=0\) and under the calibrated flow (exact \(g\leftrightarrow h\) symmetry; \(D^*|_\Sigma=0\) symbolically). All CH jets lie in \(\Sigma\); the collapsed entry has \(q\simeq\log(1/\varepsilon)\). **So the endpoint leaves are separated, and the separating coordinate is the antisymmetric pair \((q,\eta)\), which the controls reach only through \(\bar D\).** This is the structural reason the non-round costs are \(D\)-dominated (68% at cap \(-1\)).

## 3. The transverse block and the resisting region

On \(\Sigma\) the calibrated Jacobian splits; its antisymmetric block in \((q,\eta)\) is exactly (`scripts/transverse_block.py`)
\[
A_\Sigma=\begin{pmatrix}0&1\\ 8\chi e^{-2x/3}+8e^{2x/3}-16e^{-4x/3} & \tfrac43\chi+2e^{4x/3}-8e^{-2x/3}\end{pmatrix},
\]
independent of \(p\). Along CH jets the eigenvalues are \((-1.79,-4.00)\) at \(\tau=.2\), \((-0.31,-3.84)\) at \(.6\), \((0.24,-3.75)\) at \(.70\), \((0.59,-3.69)\) at \(.758\), \((1.56,-3.52)\) at \(.9\), \((-3.09,4.17)\) at \(1.2\): \(\Sigma\) is transversally attracting for \(\tau\lesssim.66\) and of saddle type beyond — exactly in the cap region \(\tau\ge.70\). However, sampling \(\Sigma\cap\{\mathfrak b_+\le-1\}\) (283 496 points, \(|x|\le3,|p|,|\chi|\le10\)) gives 38% transversally attracting, 62% saddle, <1% repelling points. Hence \(\Sigma\) contains capped states where the antisymmetric sector can be entered for free. **No static/frozen argument excludes a cheap non-round connector; the missing quantity is path weight**, namely the minimal \(\int L(\bar D-\bar D^*)\) to carry \(q\) from \(\log(1/\varepsilon)\) to the attracting part of \(\Sigma\) while \(\mathfrak b_+\le-1\), plus the symmetric-sector cost inside \(\Sigma\) to reach a CH jet. This is the precise "resisting region" asked for in the relay, and it agrees with Lemma Z and the Step-34 HJ result.

Of the three possible missing items (kernel direction, endpoint separation, path weight): the kernel is trivial (§1), endpoint separation holds structurally (§2), and **path weight is the open item**.

## 4. Two calibrations: \(\mathfrak b_+\) and the CH-renormalized \(B\)

The \(\mathfrak b_+\) decomposition is exact and nonnegative but degenerates at a CH end: for opening at \(t_{CH}=2.28\) (cap \(-1\) optimizer) \(\Delta\mathfrak b_+\approx-5024\) and \(\int\omega_+\approx5030\); the useful information is a tiny difference of huge terms. S1003A01's interface (their Step 29, verified there to \(6\times10^{-11}\)) supplies the CH-renormalized charge
\[
B=\mathfrak b_+-3\mathcal F-9\mathcal P_m^2-6Wuu',\qquad B_{\rm bolt}=1,\ B_{\rm CH}=2,\qquad \widehat P[t_0,t_1]=\int L_{AK}+\Delta B,
\]
with \(L_{AK}\) indefinite, whose only negative term is the Nijenhuis energy \(-6\nu^2d\widehat V\). Thus \(B\) has universal endpoint values but is not a calibration; \(\mathfrak b_+\) is a calibration but has endpoint values of size \(e^{4t}\). The lower problem for (N) is to interpolate between them: use \(\mathfrak b_+\) (with \(\omega_+\ge0\)) on the collapsed/swap band, and \(B\) (with the far-zone Hardy positivity of the Nijenhuis sector) on the CH tail, matched at an interface where both are finite. The certified subunit cells live entirely in the \(B\)-regime (negative Nijenhuis middle zone); a collapsed connector must cross the \(\mathfrak b_+\) band first. This matching is the concrete construction to attempt next; it requires the AK moment \(\mathcal P_m\) (defined from the perpendicular bolt) to be controlled across the collapsed band.

## 5. Corrections to the first draft of this note

An earlier version of this file (same step) evaluated \(L_{AK}\) on the scale-free saturation trajectories by finite differences, obtaining \(\int\mathrm{Ric}^\circ{}^2\approx351\) against the stored cost \(6.48\). That evaluation ignored the \(r\)-scaling of the scale-free variables and is invalid; `scripts/calibration_ak_analysis.py` and `data/saturation_control/calibration_ak_analysis.json` must not be used. The identity \(\widehat P=1+\int L_{AK}\) holds for whole cells from the smooth bolt to CH, not for connectors starting at a collapsed entry, so "\(\int L_{AK}=\mathrm{cost}-1\)" for saturation trajectories was wrong. The survey of 47 optimizer outputs (round reopening \(2.33\to3.99\) as \(\varepsilon\downarrow0\); caps \(1,0,-.5,-1,-1.5,-2.5\) give \(4.03,4.81,5.50,6.48,7.89,11.87\); late windows \(\tau\ge3\) up to \(2848\)) consists of feasible local-optimizer values, not lower bounds.

## 6. Status of (N)

(N) is now a named numerical-margin input: collapsed non-round connectors cost \(\approx5.4\)–\(6.6\) in all computed instances versus the needed \(>1-\mathfrak b_+\)-prefix accounting. Proved structure: the \(\mathfrak b_+\) calibration with trivial kernel; ASD scalar-flat calibrated leaves; leaf separation of collapsed entry (→ round point) and CH jets (in \(\Sigma\), backward blow-up); the explicit transverse block and its attracting/saddle regions in the cap. Open: the path-weight bound of §3, most plausibly via the \(\mathfrak b_+\)/\(B\) matching of §4.

Artifacts: `scripts/calibrated_flow_leaves.py` → `data/saturation_control/calibrated_flow_leaves.json`; `scripts/transverse_block.py` → `data/saturation_control/transverse_block.json`; Step-34 `scripts/hj_symbolic_reduction.py`.



---

## Source step38_kahler_and_paired_field_scope.md

Original: [sources/Sessions/S1003A02/workspace/notes/step38_kahler_and_paired_field_scope.md](../sources/Sessions/S1003A02/workspace/notes/step38_kahler_and_paired_field_scope.md)

# Step 38 — The Kähler blow-up tariff and the corrected paired-field problem

## 1. The closed same-metric form

Let \(M=X\#k\overline{\mathbf {CP}}^{2}\), where \(X\) is a fixed minimal complex surface of general type, \(A=K_X^2>0\), and orient \(M\) by its complex orientation. Put
\[
 C_+(g)=\frac1{2\pi^2}\int_M|W^+_g|^2+\frac1{96\pi^2}\int_Ms_g^2.
\]
The closed Chern--Weil identity is
\[
 \frac{P(g)}{8\pi^2}=C_+(g)-(A-k),\qquad P(g)=\int_M|\operatorname{Ric}^\circ_g|^2.
\]
Thus a universal tariff \(P/(8\pi^2)\ge ck\) is exactly
\[
 C_+(g)\ge A-(1-c)k
\]
for the same metric. The sharpened Arb enclosure for the authoritative perpendicular cell is
\[
 \frac{P_{\rm cell}}{8\pi^2}\in
 [0.995662732753254329\ldots,0.995662732771114200\ldots].
\]
Thus any per-blow-up coefficient compatible with the supplied sparse ramified/ball-quotient constructions must satisfy \(c\le0.995662732771115\).

## 2. Kähler blow-up theorem

Fix the blow-up complex structure \(\pi:M\to X\), write
\[
 K_0=\pi^*K_X,\qquad K_M=K_0+\sum_{i=1}^kE_i,
\]
so that \(K_0^2=A\), \(K_0\cdot E_i=0\), and \(E_i\cdot E_j=-\delta_{ij}\). For any Kähler metric \(g\) on this complex surface, with Kähler class \(\Omega=[\omega]\), put \(e_i=\Omega\cdot E_i>0\).

### Theorem K-blow-up

Every such Kähler metric satisfies
\[
 C_+(g)=\frac1{32\pi^2}\int_Ms_g^2\ge A,
 \qquad P(g)\ge8\pi^2k.
\]
If \(k>0\), both inequalities are strict.

### Proof

On a Kähler surface in the complex orientation the eigenvalues of \(W^+\) are \(s/6,-s/12,-s/12\). Hence \(|W^+|^2=s^2/24\) and
\[
 C_+=\frac1{32\pi^2}\int s^2.
\]
Also
\[
 \int_Ms\,d\mu=4\pi c_1(M)\cdot\Omega=-4\pi K_M\cdot\Omega,
 \qquad \operatorname{Vol}(g)=\frac{\Omega^2}{2}.
\]
Cauchy--Schwarz for the scalar function gives the exact decomposition
\[
 C_+(g)=\frac{(K_M\cdot\Omega)^2}{\Omega^2}
 +\frac1{32\pi^2}\int_M(s-\bar s)^2.
\]
Since \(K_X\) is nef and big, \(K_0\) and \(\Omega\) lie in the same positive cone closure. Hodge index gives
\[
 K_0\cdot\Omega\ge\sqrt{A\Omega^2}.
\]
Because \(K_M\cdot\Omega=K_0\cdot\Omega+\sum_i e_i\),
\[
\begin{aligned}
 C_+-A
 &\ge \frac{2\sqrt A\sum_i e_i}{\sqrt{\Omega^2}}
      +\frac{(\sum_i e_i)^2}{\Omega^2}
      +\frac1{32\pi^2}\int(s-\bar s)^2\ge0.
\end{aligned}
\]
When \(k>0\), every \(e_i>0\), so the result is strict. The closed identity then yields \(P>8\pi^2k\). A slightly stronger Hodge estimate follows from \(\Omega_0=\Omega+\sum_ie_iE_i\):
\[
 K_0\cdot\Omega\ge\sqrt{A(\Omega^2+\sum_ie_i^2)}.
\]

### Exact infimum: proved range and needed input

The theorem proves only \(\inf_{\rm Kahler}P\ge8\pi^2k\). Equality of the infimum requires a Kähler recovery family with exceptional areas tending to zero, Kähler classes tending to the canonical ray, and scalar variance tending to zero. It follows, for example, when \(K_X\) is ample and a standard small-exceptional-size Kähler blow-up construction supplies metrics converging off the exceptional curves to the negative Kähler--Einstein metric. In that setting
\[
 \inf_{\rm Kahler}P=8\pi^2k,
\]
and for \(k>0\) it is not attained. Theorem F's aligned Burns response \(1+6x_0+O(x_0^{6/5})\) is compatible with this upper approach but, by itself, is only a Riemannian local gluing theorem and does not prove that the glued metric is Kähler. The exact-infimum statement therefore must retain the Kähler-recovery hypothesis.

The strict subunit perpendicular cell is consequently genuinely non-Kähler. Its canonical almost-Kähler form has zero period on the exceptional sphere, whereas the Riemannian exceptional area is positive. Thus the cheap cell realizes monopole blindness geometrically: the class is null for the compatible field used by a LeBrun-type estimate, not merely lost by averaging sign classes.

## 3. Paired monopoles: exact line bundles and algebra

Assume the metric-wise simultaneous supply of monopoles for
\[
 a_\epsilon=c+\sum_i\epsilon_iE_i=c_1(L_\epsilon),\qquad \epsilon\in\{\pm1\}^k.
\]
For \(S^+_{\epsilon'}\cong S^+_\epsilon\otimes N_{\epsilon'\epsilon}\), Spin\(^c\) twisting gives
\[
 c_1(N_{\epsilon'\epsilon})=\frac{a_{\epsilon'}-a_\epsilon}{2}.
\]
With the Hermitian convention conjugate-linear in the first entry,
\[
 u_{\epsilon\epsilon'}=\langle\Phi_{\epsilon'},\Phi_\epsilon\rangle
 \in\Gamma(N_{\epsilon'\epsilon}^*),
 \qquad c_1(u)=\frac{a_\epsilon-a_{\epsilon'}}2,
\]
while
\[
 w_{\epsilon\epsilon'}=\Phi_\epsilon\wedge\Phi_{\epsilon'}
 \in\Gamma(\det S^+_\epsilon\otimes N_{\epsilon'\epsilon}),
 \qquad c_1(w)=\frac{a_\epsilon+a_{\epsilon'}}2.
\]
For a single sign flip at \(E_i\), \(c_1(u)=\pm E_i\), not \(\pm2E_i\). If \(A_{\epsilon'}=A_\epsilon+2B\), the relative curvature is
\[
 f_u=\frac{f_\epsilon-f_{\epsilon'}}2.
\]
This factor is essential for Chern--Weil. The nonzero class forces every transverse section \(u\) to have a zero cycle dual to \(\pm E_i\), but it does not force either spinor to vanish: \(u=0\) may instead mean pointwise orthogonality.

Let \(\rho_\epsilon=|\Phi_\epsilon|^2\), and write \(f_\epsilon^+=(\rho_\epsilon/\sqrt2)n_\epsilon\), \(|n_\epsilon|=1\). Fierz gives
\[
 |u|^2=\rho\rho'\frac{1+n\cdot n'}2,
 \qquad |w|^2=\rho\rho'\frac{1-n\cdot n'}2,
\]
so
\[
 |f_\epsilon^+-f_{\epsilon'}^+|^2
 =\frac{(\rho_\epsilon-\rho_{\epsilon'})^2}{2}+2|w_{\epsilon\epsilon'}|^2.
\]
Together with Walsh Parseval,
\[
 2\sum_{I\ne\varnothing}\|f_I^+\|_2^2
 =\mathbb E_{\epsilon,\epsilon'}\int
 \left[\frac{(\rho_\epsilon-\rho_{\epsilon'})^2}{2}+2|w_{\epsilon\epsilon'}|^2\right].
\]
The kinetic split is
\[
 |\nabla_A\Phi|^2=\frac{|\zeta|^2}{\rho}+\frac\rho4|\nabla n|^2,
 \qquad \zeta=\langle\Phi,\nabla_A\Phi\rangle.
\]
Thus a forced zero of \(u\) can be paid either by amplitude depletion or by relative spin-direction rotation. Static topology alone does not price the latter; a useful lower estimate needs a covariant vortex/winding inequality involving the relative connection.

## 4. Correct amplitude theorem at scalar \(-4\)

Suppose \(s_g=-4\), \(b_+\ge2\), and actual monopoles for the entire sign family are available on the same metric in the normalization
\[
 D_A\Phi=0,\qquad F_A^+=2i\sigma(\Phi),\qquad |\sigma(\Phi)|^2=|\Phi|^4/8.
\]
The integrated Weitzenböck identity gives
\[
 0\le\rho\le2,\qquad
 K_\epsilon=\int|\nabla_{A_\epsilon}\Phi_\epsilon|^2
 =\frac12\int\rho_\epsilon(2-\rho_\epsilon).
\]
Substitution into the simultaneous-field identity yields the exact nonnegative form
\[
\begin{aligned}
&P-8\pi^2Q+4\mathbb E_\epsilon\int(2-\rho_\epsilon)\\
={}&2\|f_\varnothing^-\|_2^2
+\mathbb E_{\epsilon,\epsilon'}\int
\left[\frac{(\rho_\epsilon-\rho_{\epsilon'})^2}{2}+2|w_{\epsilon\epsilon'}|^2\right]\\
&+\mathbb E_\epsilon\left[
8\|\zeta_\epsilon\|_2^2+4\|W^+-W_{0,\epsilon}\|_2^2
+\int(b(\rho_\epsilon)+2)(2-\rho_\epsilon)^2\right],
\end{aligned}
\]
where \(b(t)=(-t^2+8t+2)/6\ge1/3\) on \([0,2]\). In particular,
\[
 \boxed{P\ge8\pi^2Q-4\mathbb E_\epsilon\int(2-\rho_\epsilon).}
\]
This is the corrected clean amplitude theorem. An equivalent residual-polynomial form uses
\[
 m(\rho)=\frac{(2-\rho)(-\rho^3+10\rho^2-2\rho-4)}6,
\]
which changes sign; it cannot prove \(P\ge8\pi^2Q\) by itself. The coefficient four in the linear amplitude-deficit bound is sharp at \(\rho=2\).

## 5. The isolated cell monopole problem is different from closed supply

The invariant diagonal Bianchi--IX reduction was checked by Lichnerowicz. With
\[
 v_i=\alpha_i/a_i,\qquad
 c=\frac{\sum a_i^2}{2a_1a_2a_3}-\frac12\sum\dot a_i/a_i,
\]
and \(n=(\rho\cos\theta,0,\rho\sin\theta)\),
\[
\begin{aligned}
\dot{\log\rho}&=2c+v_1\cos\theta+v_3\sin\theta,\\
\dot\theta&=v_3\cos\theta-v_1\sin\theta,\\
\dot\alpha_1&=a_1\rho\cos\theta-2a_1\alpha_1/(a_2a_3),\\
\dot\alpha_3&=a_3\rho\sin\theta-2a_3\alpha_3/(a_1a_2).
\end{aligned}
\]
At a smooth slot-1 bolt, the regular charged family has two parameters \((\rho_0,\beta)\) and
\[
 \theta=\theta_\sigma-\sigma\beta t+O(t^3),\quad
 \alpha_1=\sigma\left[1-(\rho_0/2+b^{-2})t^2\right]+O(t^4),\quad
 \alpha_3=b\rho_0\beta t^2/4+O(t^4).
\]
The exact CH monopole is \(\rho=12\), \(\theta=\pi/2\), \(\alpha_1=0\), \(\alpha_3=3\sinh^2r\). Exact finite-radius matching to all four CH data is impossible for \(\sigma=\pm1\): the plane \(\theta=\pi/2,\alpha_1=0\) is invariant, hence backward uniqueness reaches bolt charge zero. The correct isolated problem is asymptotic convergence to the two-dimensional CH stable manifold, with far conditions
\[
 \mathcal B+6L=0,\qquad
 \mathcal A-(\sqrt{13}-1)\delta=0
\]
to leading order, where \(L=\log(\rho/12)\), \(\delta=\theta-\pi/2\), \(\mathcal A=\alpha_1/\sinh r\), and \(\mathcal B=(\alpha_3-3\sinh^2r)/(\sinh r\cosh r)\).

The Step-37 forward code imposed only \((\rho,\theta)=(12,\pi/2)\) at finite radius and was exponentially ill-conditioned; the first Step-38 collocation imposed limiting bolt values at a positive cutoff, omitted the regularity condition excluding the \(\alpha_3\sim t^{-2}\) mode, and again used the wrong terminal subspace. Its failed output is not monopole data. A corrected multiple-shoot attempt also timed out before any root or profile was produced. More importantly, a monopole on the closed host need not restrict to an invariant isolated-cell monopole with canonical CH asymptotics: its boundary trace is selected by the exterior, and nonlinear equations cannot be averaged to impose symmetry. Therefore cell ODE data, even if obtained, would be a model of one field channel rather than the metric-wise closed theorem required globally.

## 6. Consequence for the global route

The Kähler theorem identifies a complete unit tariff in the class where the canonical field sees every exceptional curve. The cheap cell identifies the opposite mechanism: the field period on \(E\) vanishes and the topology can be carried by relative spin-direction rotation rather than a holomorphic amplitude vortex. The paired formulation restores the class through \(c_1(u)=E_i\), but no current identity proves that its relative rotation has a positive metric-uniform energy. The next global advance must either derive such a covariant vortex bound on closed metrics or produce a family in which the relative rotation spreads with vanishing energy while the singleton curvature charge remains fixed. Isolated exact-end shooting cannot decide that global dichotomy by itself.

## 7. Anti-self-dual retention on a ramification neighbourhood

Let \(N\) be a fixed ramification neighbourhood and suppose \(g\) agrees with the Kähler--Einstein model \(g_0\) to the order needed for the Euler and signature transgressions to agree on \(\partial N\). No surgery topology is placed inside \(N\). Relative signature gives
\[
 \Delta_N\int|W^+|^2=\Delta_N\int|W^-|^2=:\Delta_N B.
\]
The relative closed/APS Chern--Weil identity, using \(\operatorname{Ric}^\circ(g_0)=0\), then gives the exact formula
\[
 \boxed{\Delta_N B=\frac14P_N(g)-\frac1{48}\Delta_N S.}
\]
Thus characteristic flux alone supplies no sign for anti-self-dual retention: it converts it exactly into the scalar-square channel. If both metrics are normalized to \(s=-4\), this becomes
\[
 \boxed{\Delta_N B=\frac14P_N(g)-\frac13\Delta_N V.}
\]
Consequently, a useful local retention estimate is equivalent to an upper relative-volume estimate. Depletion occurs precisely when the normalized relative-volume increase exceeds \(3P_N/4\). This is the same Weyl--volume exchange already exposed by Theorem C for exact-CH cells; the APS/calibration identities do not add an independent positive term. The global monopole scalar budget controls total \(S\), not its allocation among ramification and surgery regions, so it does not presently close this local estimate. A field localized to the ramification neighbourhood, or a construction showing favourable relative-volume increase there, is necessary to decide the true \(r\)-dependence.

## 8. Exact relative-curvature completion and the fate of the paired route

For one sign flip write \(a'=a+2E\), \(E^2=-1\), choose the relative twisting line \(N\) with \(c_1(N)=E\), and set
\[
 h=\frac{f-f'}2,\qquad \bar f=\frac{f+f'}2.
\]
Then \([h/(2\pi)]=-E\), while the SW curvature equations and Fierz identities give
\[
 |h^+|^2=\frac{(\rho-\rho')^2}{8}+\frac{|w|^2}{2}.
\]
Chern--Weil gives the exact Bogomolny completion
\[
 \boxed{\|h^-\|_2^2-\|h^+\|_2^2=4\pi^2,}
\]
\[
 \boxed{\|h\|_2^2=4\pi^2+\int\left[\frac{(\rho-\rho')^2}{4}+|w|^2\right].}
\]
Thus the fixed negative-square charge is stored in the anti-self-dual relative curvature. Amplitude mismatch and spin-direction disagreement measure only \(h^+\). The paired object does not produce an additional positive sector beyond the singleton Walsh curvature; it explains where that sector's topology lives.

There is also a topological unwinding mechanism. The combined bilinear
\[
 q=(u,w)\in N^*\oplus D,
 \qquad D=\det S_a^+\otimes N,
\]
has \(|q|^2=\rho\rho'\). In the pure one-flip situation \(c_1(N^*)=-E\), \(c_1(D)=c\), and \(c\cdot E=0\), so
\[
 c_2(N^*\oplus D)=0.
\]
Where both spinors are nonzero, \(q/|q|\) lies in \(S^3\). The phase winding of the \(u\)-component, which would be protected inside \(S^1\), can unwind through \(w\) because \(\pi_1(S^3)=0\). This makes the orthogonality zero mechanism precise.

The bilinear fields obey product Bochner equations, for example
\[
 \left(\nabla_{N^*}^*\nabla_{N^*}+\frac s2+\frac{\rho+\rho'}2\right)u
 =-2\sum_\alpha\langle\nabla_{A',e_\alpha}\Phi',\nabla_{A,e_\alpha}\Phi\rangle.
\]
The right side is an unsigned twistor cross term. Hence \(u\) is not a closed scalar vortex field on a general Riemannian four-manifold. The relative curvature enters derivative commutators multiplied by \(u\), precisely degenerating at the forced zero, while \(w\) couples to \(\bar f\), not \(h\).

For one pair, the simultaneous-field cost identity can be written
\[
 P-8\pi^2
 =2\|\bar f^-\|_2^2+2\|h^+\|_2^2
 +\frac{\mathcal R(\Phi)+\mathcal R(\Phi')}{2}-2(K+K'),
\]
where \(\mathcal R\) is the nonnegative alignment/amplitude remainder already recorded above. The topological \(8\pi^2\) has already been extracted from \(\|h^-\|^2-\|h^+\|^2=4\pi^2\). A positive excess would require an additional kinetic compensation estimate; the paired Bochner system does not supply one. Common amplitude depletion is linear in \(2-\rho\) while the displayed amplitude remainders are quadratic, and relative rotation can unwind through \(w\).

Accordingly, the paired construction is scientifically useful as a structural explanation but does not by itself improve the global lower bound. A positive excess can follow under extra projection/noncollapse input, e.g. \((E_g^+)^2\ge\delta>0\) together with a kinetic compensation inequality. Such projection input fails exactly in the perpendicular null-period regime. In a tube of radius \(r\) around an exceptional sphere of area \(A_E\), a relative spin rotation has the scale
\[
 \int|\nabla n|^2=O(A_E),\qquad \int|w|^2=O(A_Er^2),
\]
so both can vanish as \(A_E\to0\) while the fixed \(4\pi^2\) relative charge remains in \(h^-\). This is the field-theoretic countermechanism compatible with subunit perpendicular cells.

Independent derivation: `trace/ttcs/results/step38_ttcs02_generator1_integration.md`.



---

## Source step40_nijenhuis_form_and_pointwise_exhaustion.md

Original: [sources/Sessions/S1003A02/workspace/notes/step40_nijenhuis_form_and_pointwise_exhaustion.md](../sources/Sessions/S1003A02/workspace/notes/step40_nijenhuis_form_and_pointwise_exhaustion.md)

# Step 40 — The Nijenhuis form of the signed field cost, its Weyl form, and pointwise exhaustion at LeBrun's threshold

Session S1003A02, Agent2. Conventions are those of the simultaneous-field identity,
`Skills/geometric-analysis/research/paper/sections/variational_selection_and_global_cost.tex`
(Prop. *Simultaneous signed cost identity*, lines 319–447): \(s_g=-4\);
\(M=X\#k\overline{\mathbf{CP}}^2\#\ell(S^1\times S^3)\), \(Q=k+4\ell\); for each sign vector
\(\epsilon\) an actual solution \(D_{\mathcal A_\epsilon}\Phi_\epsilon=0\),
\(F^+_{\mathcal A_\epsilon}=2i\sigma(\Phi_\epsilon)\), \(\rho_\epsilon=|\Phi_\epsilon|^2\in[0,2]\),
\(\psi_\epsilon=2\sqrt2\sigma(\Phi_\epsilon)\) (so \(|\psi|=\rho\)),
\(W_{0,\epsilon}=\tfrac14(\rho^2 I/3-\psi\otimes\psi)\), \(\zeta=\langle\Phi,\nabla\Phi\rangle\),
\(M_\epsilon=W^+-W_{0,\epsilon}\). The field quantifiers are those verified in Step 39
(`trace/ttcs/results/step39_ttcs01_verifier{1,2}_integration.md`): fixed Spin\(^c\) structures
\(a_\epsilon=c+\sum\epsilon_iE_i\); for \(b^+\ge2\) chamber-independent nonzero invariants give
unperturbed solutions for every metric by LeBrun's limiting argument; when \(A-k>0\) every
solution is irreducible; the formula is applied to the scalar \(-4\) Yamabe representative
\(\hat g\) and \(P(g)\ge P(\hat g)\); handle summands need the higher-type supplier. Below,
"saving" means \(\mathfrak S:=8\pi^2Q-P\), and
\[
\mathcal W:=2\|f_\varnothing^-\|^2+2\sum_{I\neq\varnothing}\|f_I^+\|^2\ \ge0
\]
is the Walsh part of \(\mathscr A\). Starting identity (proved in the paper and rechecked in
Step 37/39):
\[
P-8\pi^2Q=\mathcal W+\mathbb E_\epsilon\Big[8\|\zeta\|^2+4\|M\|^2+\int b(\rho)(\rho-2)^2\Big]
-4\,\mathbb E_\epsilon K_\epsilon,\qquad K_\epsilon=\int|\nabla\Phi_\epsilon|^2 .
\tag{0}
\]

## 1. Pointwise anatomy of a monopole first jet

On \(\{\rho>0\}\) (complement of a null set by unique continuation) write
\(\Phi=\sqrt\rho\,u\), \(|u|=1\), \(\nabla_{\mathcal A}u=i\beta u+v\,u^\perp\) with \(\beta\) a real
1-form and \(v\in T^*\otimes\mathbf C\). Put \(a=d\sqrt\rho\), \(b=\sqrt\rho\,\beta\). Then
\[
|\nabla\Phi|^2=|a|^2+|b|^2+\rho|v|^2,\qquad |\zeta|^2=\rho(|a|^2+|b|^2),\qquad
|\nabla n|^2=4|v|^2,
\]
where \(n=\psi/\rho\) is the unit Bloch (almost-complex) direction of \(\Phi\).

**Lemma 1 (Dirac pins the Lee form; it never sees the Nijenhuis tensor).** Let
\(c(v)=\sum_ie_i\cdot(v_iu^\perp)\in S^-\). Then (i) \(cc^*=2\,\mathrm{Id}_{S^-}\);
(ii) \(\ker c\) equals the space of first jets of \(u\) for which the Bloch form satisfies
\(d\omega=0\) at the point, i.e. the Gray–Hervella almost-Kähler component \(\mathcal W_2\)
(equivalently the Nijenhuis component of \(\nabla J_n\)); its orthogonal complement is the Lee
component \(\mathcal W_4\); (iii) \((a+ib)\cdot u=(a+J'b)\cdot u\) for an orthogonal complex
structure \(J'\) and \(|(a+J'b)\cdot u|=|a+J'b|\). Writing \(v=v_2+v_4\), the equation
\(D_{\mathcal A}\Phi=(a+ib)\cdot u+\sqrt\rho\,c(v)=0\) is therefore equivalent to
\[
\rho|v_4|^2=\tfrac12|a+J'b|^2,\qquad v_2\ \text{unconstrained}.
\]
*Proof.* (i): \(c\) is \(U(2)\)-equivariant onto the irreducible real module \(S^-\);
\(\operatorname{tr}cc^*=4\cdot2\). (ii): both kernels are 4-dimensional; Taubes' canonical-spinor
identity \(D_{A_0}u_0=0\) for almost-Kähler \(\omega\) is pointwise algebraic in the first jet, so
\(\mathcal W_2\subset\ker c\). (iii) is Clifford linearity. All three were checked numerically at
random spinors (residuals \(\le4\times10^{-15}\); principal angles between the two kernels all
zero): `workspace/scripts/step40_nijenhuis_tariff_check.py`,
`workspace/data/step40_nijenhuis_tariff_check.json`. \(\square\)

Thus \(|\nabla n|^2_{\mathcal W_2}:=4|v_2|^2\) is the Nijenhuis (integrability-obstructing)
energy of the SW-selected almost-complex structure \(J_\epsilon\), and the Lee part of its
rotation is not free: it costs \(\zeta\).

## 2. Theorem N (Nijenhuis form of the saving)

The pointwise Weitzenböck formula for an actual solution at \(s=-4\) is
\(\tfrac12\Delta\rho+|\nabla\Phi|^2=\tfrac12\rho(2-\rho)\) (\(\Delta=d^*d\)); its integral is the
recorded \(K_\epsilon=\frac12\int\rho(2-\rho)\). Multiplying by \(\psi(\rho)=2\rho\) and
integrating gives \(\int2\rho|\nabla\Phi|^2+4\int\rho|a|^2=\int\rho^2(2-\rho)\). Adding
this zero to (0) after substituting \(K=\frac12\int\rho(2-\rho)\):

**Theorem N.** Under the quantifiers above,
\[
\boxed{\;
\mathfrak S\;=\;\frac12\mathbb E_\epsilon\!\int\rho_\epsilon^2|\nabla n_\epsilon|^2_{\mathcal W_2}
-\mathbb E_\epsilon\!\int\frac{(2-\rho)^2(2+2\rho-\rho^2)}6
-\mathbb E_\epsilon\!\int\rho\bigl(|a|^2+5|b|^2-2\langle a,J'b\rangle\bigr)
-4\mathbb E_\epsilon\|M_\epsilon\|^2-\mathcal W\; }
\]
Every subtracted term is nonnegative: \(2+2\rho-\rho^2>0\) on \([0,2]\); the quadratic form
\(\begin{psmallmatrix}1&-1\\-1&5\end{psmallmatrix}\) has determinant 4. Inputs:
\(m(\rho)-\rho^2(2-\rho)=-(2-\rho)^2(2+2\rho-\rho^2)/6\) with
\(m=(2-\rho)(-\rho^3+10\rho^2-2\rho-4)/6\), and the coefficient matrix
\(\begin{psmallmatrix}-\rho&\rho\\ \rho&-5\rho\end{psmallmatrix}\) (both in the JSON).

**Corollaries.**
1. *Hermitian tariff.* If, for a scalar \(-4\) metric, some simultaneous choice of the
   \(2^k\) solutions has Bloch structures \(J_\epsilon\) integrable on \(\{\Phi_\epsilon\ne0\}\),
   then \(P\ge8\pi^2Q\). This contains the scalar \(-4\) Kähler instance and every
   scalar \(-4\) metric whose monopole structures are Hermitian, Kähler or not. It does not by
   itself reproduce the Step-38 theorem for arbitrary Kähler metrics, because Yamabe
   normalization generally destroys Kählerness (Step 38 used Hodge index directly).
2. *Necessary condition on near-minimizers.* If \(P/(8\pi^2k)\to c<1\) (pure blow-ups), then
   \(\mathbb E_\epsilon\int\rho^2|\nabla n_\epsilon|^2_{\mathcal W_2}\ge16\pi^2(1-c)k\): the
   monopole almost-complex structures are non-integrable, with Nijenhuis energy at least
   \(16\pi^2(1-c)\) per class. For a closed replica of the certified \(X=128\) cell,
   \(1-c\in[0.0043372672289,0.0043372672468]\), i.e. asymptotically at least \(0.684914\)
   per class (an \(o(k)\) error is retained at finite \(k\)).
3. *Scale law* (for geometrically controlled regions of bounded multiplicity). Since the weight is \(\rho^2\le4\), rotation of \(J_\epsilon\) by a fixed angle
   across a region of diameter \(r\) buys at most \(O(r^2)\). Saving bounded away from zero per
   class requires the monopole almost-complex structure to rotate non-integrably across
   unit-size regions in the \(s=-4\) normalization. This is the precise field-side form of the
   observed hierarchy: Burns cells of scale \(\sqrt{x_0}\) are first-order neutral in
   \(\ker\mathbf R^+\), the second-order gain is \(x_0^2\log\), and the certified cell saves
   \(0.43\%\).
4. *Agreement with the almost-Kähler identity.* A01's identity has the single negative term
   \(-\tfrac32N\) (Nijenhuis); Theorem N shows that the same channel is the only free saving
   mode of the whole monopole family. The Lee component of \(\nabla J\), which in the
   Step-37 decomposition was mixed into \(\rho|\nabla n|^2\), is now shown to be paid by
   \(\zeta\).

## 3. Theorem W (Weyl form): rotation is Weyl deletion along the monopole direction

For the self-dual form \(\psi\), the Weitzenböck formula
\(\nabla^*\nabla\psi=\Delta_H\psi+2W^+\psi-\tfrac s3\psi\) integrates to
\(\int|\nabla\psi|^2=2\|d\psi\|^2+2\int(W^+-W_0)(\psi,\psi)+\int\tfrac{\rho^2}3(4-\rho^2)\),
using \(\|d^*\psi\|=\|d\psi\|\), \(W_0\psi=-\rho^2\psi/6\), \(s=-4\). With
\(|\nabla\psi|^2=4\rho|a|^2+4\rho^2|v_2|^2+2\rho|a+J'b|^2\) and, under the Dirac equation,
\(|d\psi|^2=2\rho|b|^2\) (the \(\mathcal W_2\) part lies in \(\ker d\); checked numerically, form
eigenvalues \(\{0^4,2^4\}\)), substitution into Theorem N gives, with
\(x_\epsilon=M_\epsilon(n_\epsilon,n_\epsilon)\):

**Theorem W.**
\[
\mathfrak S=\mathbb E_\epsilon\!\int\bigl[\rho^2x_\epsilon-4|M_\epsilon|^2\bigr]
+\mathbb E_\epsilon\!\int\frac{(2-\rho)(\rho-1)(3\rho+2)}3
-4\mathbb E_\epsilon\|\zeta_\epsilon\|^2-\mathcal W .
\]
(The \((a,b)\) form collapses exactly to \(-4(|a|^2+|b|^2)\rho=-4|\zeta|^2\); eigenvalues of the
combined form are all \(-4\) in the JSON.)

Interpretation. Non-integrable rotation of the monopole structure is, by the Weitzenböck formula,
the same thing as the Rayleigh component \(W^+(n_\epsilon,n_\epsilon)=x-\rho^2/6\) rising above
its aligned value \(-\rho^2/6\) (\(x>0\)); \(x\) is not an eigenvalue in general and \(x>0\)
alone does not force \(|W^+|<|W_0|\) (the exact channel is \(\rho^2x-4|M|^2\)).
This is exactly the sign of the Theorem-C channel on the certified cell
(\(4\Delta W_+=-0.07513\), paid by \(48\,\mathrm{RV}\approx+0.07080\); Step 39 numerics). The
field saving is thus Weyl-type, while the amplitude depletion terms \(m\) and
\((2-\rho)(\rho-1)(3\rho+2)/3\) are volume-type. The linear Weyl gain \(\rho^2x\) is quadratically
penalized by \(4|M|^2\ge6x^2\): densities of order one pay, diffuse low-density rotation does not.

## 4. Theorem E (pointwise exhaustion at LeBrun's threshold)

Combine the amplitude form \(\mathfrak S\le\mathbb E\int m-8\|\zeta\|^2-4\|M\|^2-\mathcal W\) and
Theorem W with weight \(\lambda\), and the closed identity
\(P=4W_++4V/3-8\pi^2(A-k)\) with \(|W^+|^2=\rho^4/24-\rho^2x/2+|M|^2\) with weight \(1-t\)
(pure blow-ups, \(Q=k\)). Using \(|M|^2\ge\frac32x^2\) and dropping
\(\zeta\)- and Walsh terms,
\[
P\ \ge\ 8\pi^2\bigl[k-(1-t)A\bigr]+\mathbb E_\epsilon\!\int g_{t,\lambda}(\rho_\epsilon),
\]
\[
g_{t,\lambda}=(1-t)\Bigl(\frac{\rho^4}6+\frac43\Bigr)
-t\Bigl[\lambda\frac{(2-\rho)(\rho-1)(3\rho+2)}3+(1-\lambda)m\Bigr]
-\frac{(t\lambda+2-2t)^2\rho^4}{24}.
\]
Exactly (sympy): \(g_{2/3,2/3}=-\tfrac2{243}(2\rho-3)^2(\rho^2-24\rho-18)\ge0\) on \([0,2]\),
which reproduces LeBrun's \(C_+\ge2A/3\), i.e. \(P/(8\pi^2)\ge k-A/3\); and
\(\max_\lambda g_{t,\lambda}(3/2)=-\tfrac34(3t-2)<0\) for every \(t>2/3\).

**Theorem E (affine pointwise exhaustion).** Constant affine combinations of the exact
identities (amplitude form, Nijenhuis/Weyl form, closed Weyl–volume identity), followed by
discarding terms of known sign and the sharp estimate \(|M|^2\ge\frac32x^2\), prove exactly
LeBrun's \(C_+\ge 2A/3\) and nothing more. (Not excluded: non-affine pointwise inequalities,
other weighted Weitzenböck multipliers, joint algebraic constraints among the \(2^k\) spinors
sharing one \(W^+\), and all differential/global information.) The envelope binds only at uniform amplitude \(\rho=3/2\), not at
Kähler–Einstein points (where \(g_{2/3,2/3}(2)=124/243>0\)).

Consequences for the route. (a) The "compensation inequality" sought in Step 39 cannot come
from this affine pointwise scheme: shallow depletion and Nijenhuis rotation can be spread at
low density with no pointwise penalty in it (see §5 for the explicit formal state). (b) Combined with the Step-38 blindness theorem (the exceptional charge of
a sign flip sits in \(h^-\), while all self-dual data measure \(h^+\); the forced zero of \(u\)
unwinds through \(w\) in \(S^3\)), every \(k\)-dependent improvement must come from genuinely
global or differential information: the Walsh self-dual energy, the harmonic-projection terms
\(J_\epsilon\), the \(\zeta\)-terms (which price the Lee component and amplitude gradients), or
elliptic/regularity structure of the actual solutions. (c) For constructions toward small \(c\),
the pointwise saving density (sign-averaged) is at most \(\max_\rho F_{3/4}=0.8\) (attained at \(\rho=1.6\);
\(F_\lambda=\max_\rho[\lambda^2\rho^4/24+\lambda p_2+(1-\lambda)m]\)), so the saving region must
have volume at least \(10\pi^2(1-c)\) per class in the \(s=-4\) normalization, with \(J_\epsilon\)
non-integrable and \(W^+(n_\epsilon,n_\epsilon)>-\rho^2/6\) there.

## 5. The formal common mode: the identities permit \(c\to0\), and what would forbid it

(Integrated from `trace/ttcs/results/step40_ttcs01_generator1_integration.md`, §7–8, and
checked by hand.) Take constant amplitude \(\rho=r\), \(\zeta=0\), \(d\psi=0\) (so \(b=0\),
\(v_4=0\)): an almost-Kähler structure \(\omega=\sqrt2 n\) with harmonic \(\psi=rn\). The spinor
Weitzenböck formula gives \(|\nabla n|^2=2(2-r)\); the self-dual one gives
\(x=(2-r)(4-r)/6\), i.e. \(W^+(n,n)=\tfrac43-r\). With \(M=\mathrm{diag}(x,-x/2,-x/2)\),
\(\mathcal W=0\) (so \(r^2V=8\pi^2A\) by \(\mathcal W=\mathbb E\int\rho^2-8\pi^2A\)) and the closed
identity,
\[
\frac{P}{8\pi^2}=k-A\beta(r),\qquad \beta(r)=\frac{16}r-5-\frac{12}{r^2},\qquad
\beta(2-h)=h-\tfrac{h^2}4+O(h^3).
\]
\(r=3/2\) is LeBrun's threshold \(\beta=1/3\). For \(h=k/A\), \(r=2-h\) gives \(P/(8\pi^2)=O(kh)=o(k)\)
with torsion \(|\nabla J|^2\sim2h\) spread uniformly over the volume \(2\pi^2A\). So the exact
identities are consistent with \(c\to0\) through a *uniform, low-density, common almost-Kähler
rotation*. Since all \(\psi_\epsilon\) coincide in this state, the harmonic self-dual parts of
all \(a_\epsilon\) coincide: every \(E_i\) is anti-self-dual harmonic for \(g\). This is the
global form of the null-period mechanism of the certified cell (zero almost-Kähler period on
\(E\)); the classes must be carried by small sign-dependent defects with charge in \(h^-\).

The decisive obstruction to this mode is linear versus quadratic. In the formal state
\(P\sim(\int|\nabla J|^2)^2/V\). Perturbatively about a Kähler–Einstein host \(g_0\),
\(g=g_0+tH\), both \(P=t^2\|\mathcal L_EH\|^2+O(t^3)\) and the torsion energy
\(t^2\|\mathcal TH\|^2\) are quadratic in \(t\); hence a finite *torsion quotient*
\[
C_{AK}(g_0)=\sup_{H\perp\text{gauge, KE moduli}}\frac{\|\mathcal TH\|^2}{\|\mathcal L_EH\|^2}
\]
forces \(P\gtrsim C_{AK}^{-1}\int|\nabla J|^2\), which is incompatible with the common mode
(\(P=o(\int|\nabla J|^2)\)). Koiso's theorem that Einstein deformations of negative KE surfaces
are Kähler makes the kernel torsion-free, so \(C_{AK}<\infty\) on each fixed host; the real
question is uniformity along cover towers (spectral gap of \(\mathcal L_E\) on TT tensors on
ball-quotient covers) and the nonperturbative regime. This is a quantitative negative-scalar
Goldberg problem: a uniform estimate \(P\ge\kappa\int|\nabla J|^2\) for monopole almost-Kähler
structures near negative KE metrics would make diffuse rotation pay linearly, confining any
saving to non-perturbative cores where the Theorem-G whole-core accounting applies.

## 6. What remains open

- A \(k\)-dependent lower bound for \(0<k<A/3\) needs differential input (Theorem E). The
  natural candidates are (i) a Bochner/elliptic estimate showing that the Nijenhuis energy of
  \(J_\epsilon\) cannot be diffuse because the Walsh singleton curvature (\(h^-\), fixed
  \(4\pi^2\)) localizes near a 2-cycle dual to \(E_i\); (ii) an argument that diffuse rotation of
  all \(2^k\) structures forces \(\sum_I\|f_I^+\|^2\) or \(J_\epsilon\) to grow; (iii) the converse
  construction: a metric family with \(\rho\approx1.6\), \(x>0\) on volume \(\gtrsim10\pi^2(1-c)k\)
  while \(\mathcal W\) and the \(\zeta\)-terms stay \(o(k)\).
- The pointwise identity \(|d\psi|^2=2\rho|b|^2=2|\operatorname{Im}\zeta|^2\) and the integrated
  self-dual Weitzenböck form were confirmed numerically and by the independent verification
  `trace/ttcs/results/step40_ttcs01_verifier1_integration.md` (Lemma 1, Theorems N, W, E
  verified as exact; repairs above incorporated). A direct residual \(\|Q_d-2I_b\|\) should
  be added to the script.



---

## Source step42_ak_torsion_profile_taubes_goldberg.md

Original: [sources/Sessions/S1003A02/workspace/notes/step42_ak_torsion_profile_taubes_goldberg.md](../sources/Sessions/S1003A02/workspace/notes/step42_ak_torsion_profile_taubes_goldberg.md)

# Step 42 — Almost-Kähler torsion profile, the Taubes period lemma, and the Goldberg reduction of the tariff

Session S1003A02, Agent2. Setting: \(M=X\#k\overline{\mathbb{CP}}^2\), \(X\) minimal with \(b^+(X)\ge2\),
Seiberg–Witten basic classes exactly \(\pm K_X\) modulo torsion (an assumption to be checked for each \(X\); it is not automatic for every minimal surface of general type), \(A=K_X^2>0\),
\(E_i\) the exceptional classes, \(0<k<A/3\) the open range. Closed identity
\(C_+:=\frac1{2\pi^2}\int|W^+|^2+\frac1{96\pi^2}\int s^2=A-k+P/(8\pi^2)\).
Script/data: `workspace/scripts/step42_ak_torsion_profile.py` → `workspace/data/step42_ak_torsion_profile.json`
(all algebra below verified symbolically).

Conventions for an almost-Kähler metric \((g,\omega)\), \(|\omega|^2=2\), \(u=\omega/\sqrt2\) (LeBrun,
*Four-manifolds, curvature bounds and convex geometry*, and *Ricci curvature, minimal volumes and SW theory*,
Prop. 2.4 and Blair's formula there):
\[
s^*=s+|\nabla\omega|^2=2W^+(\omega,\omega)+\tfrac s3,\qquad
\int(s+s^*)\,d\mu=8\pi\,c_1(\omega)\cdot[\omega]=-8\pi K_\omega\cdot[\omega],\qquad [\omega]^2=2V .
\]
Hence \(W^+(u,u)=s/6+\delta/4\) with \(\delta:=s^*-s=|\nabla\omega|^2\ge0\), and \(\delta\equiv0\) iff Kähler.

## 1. Taubes period lemma

**Lemma T.** Let \(\omega\) be a symplectic form on \(M\) (for instance a nowhere-vanishing self-dual
harmonic form of any metric). Then \(K_\omega=sK_X+\sum_i\epsilon_iE_i\) for signs \(s,\epsilon_i\), the classes
\(e_i:=\epsilon_iE_i\) and \(sK_X\) are represented by \(J\)-holomorphic curves for generic compatible \(J\), and
\[
K_\omega\cdot[\omega]=|K_X\cdot[\omega]|+\sum_i a_i,\qquad a_i:=|E_i\cdot[\omega]|>0 .
\]
*Proof.* \(b^+(M)\ge2\). Taubes: \(K_\omega\) is a basic class; by the blow-up formula the basic classes of
\(M\) are \(\pm K_X+\sum\pm E_i\). Taubes' SW\(\Rightarrow\)Gr: a class \(e\) with \(SW(2e-K_\omega)\neq0\) is
represented by a \(J\)-holomorphic curve, hence \(\omega\cdot e>0\) if \(e\ne0\). For \(e=e_i\),
\(2e_i-K_\omega=-(K_\omega-2e_i)\) and \(K_\omega-2e_i\) is the basic class with the \(i\)-th sign flipped;
for \(e=sK_X\), \(2sK_X-K_\omega=sK_X-\sum e_i\) is basic. So \(\omega\cdot e_i>0\), \(\omega\cdot sK_X>0\), and
\(K_\omega\cdot\omega=s K_X\cdot\omega+\sum\omega\cdot e_i\). \(\square\)

**Corollary T1 (null periods force zeros).** For any metric \(g\) on \(M\), a self-dual harmonic form with zero
period on some \(E_i\) vanishes somewhere. In particular, if some \(E_i\) is anti-self-dual harmonic for \(g\),
then \(g\) admits no nowhere-vanishing self-dual harmonic form (no conformally almost-Kähler structure).

**Corollary T2 (the Step-40 formal common mode is topologically excluded).** The Step-40 state
(constant \(\rho=r\), \(\zeta=0\), \(d\psi_\epsilon=0\), \(\psi_\epsilon\) independent of \(\epsilon\)) requires every
\(E_i\) to be ASD harmonic and \(\psi=r n\) to be a nowhere-vanishing harmonic self-dual form. This contradicts
T1. More precisely, if one monopole form \(\psi_\epsilon\) is closed and nowhere zero, then
\(\omega\propto\psi_\epsilon\) is symplectic, every \(E_i^{+,h}\ne0\), and the harmonic parts of the
\(\psi_{\epsilon}\) are genuinely sign-dependent.

*Consistency with the cell.* In the symmetric perpendicular cell the canonical closed self-dual form has zero
period on \(E\) and **vanishes along the exceptional sphere**: in A01's \(x_0=.038,X=128\) profile
(`Sessions/S1003A01/workspace/data/step28/gap_lm3_x00.038_X128_d24.json`) the conformal factor \(u\) with
\(|\omega|_g=\sqrt2u^2\) is \(0.0072\) at the first bolt sample and \(1\) at the CH end. In this symmetric model the
null-period mechanism is a degenerate (bolt-vanishing) closed form, not an almost-Kähler structure (in general a
zero integral over a sphere does not force pointwise vanishing on it); in a closed host it becomes a zero set of
the harmonic form or acquires a positive exceptional period.
Literature status (Step-42 verification): Lemma T packages a standard argument — LeBrun's 2001 Proposition 3.2
already uses the sign-flipped basic class and Taubes to contradict zero exceptional symplectic area. New here is
only its use against the Step-40 common mode.

*What T does not give.* No quantitative cost: the replacement for the common mode may use (a) tiny but
positive exceptional areas \(a_i\) (small \(J\)-holomorphic spheres, Walsh self-dual variance
\(\sim\sum a_i^2/V\)), or (b) thin near-symplectic zero sets of the harmonic part with \(\psi_\epsilon\)
non-closed, whose \(\zeta\)/\(d\psi\) cost tends to zero with the tube radius unless the geometry is bounded
at unit scale (and even then it is \(O(1)\) per zero component, not per class). Lemma T therefore turns
"exceptional classes are ASD" into "exceptional classes are small pseudoholomorphic spheres or are
linked to zeros of the harmonic form"; neither alternative carries a per-class tariff by itself.

## 2. Theorem AKΓ (almost-Kähler torsion-profile inequality)

**Theorem AKΓ.** For every almost-Kähler metric \((g,\omega)\) on \(M\), put
\[
\ell:=8\pi K_\omega\cdot[\omega]=8\pi\Bigl(|K_X\cdot\omega|+\sum_ia_i\Bigr),\qquad
\theta:=\frac1\ell\int(s^*-s)\,d\mu\ \ (\ge0).
\]
Then
\[
C_+\ \ge\ \frac{\ell^2}{128\pi^2V}\,\Gamma(\theta),\qquad \Gamma(\theta)=3\theta^2-2\theta+1,
\qquad \frac{\ell^2}{128\pi^2V}= A\,(\eta+\alpha)^2,\quad \eta=\frac{|K_X\cdot\omega|}{\sqrt{2AV}},\ \alpha=\frac{\sum a_i}{\sqrt{2AV}}>0 .
\]
Equivalently
\[
\frac{P}{8\pi^2}\ \ge\ k-A+A(\eta+\alpha)^2\Gamma(\theta).
\]
**Correction (Step-42 verification, `trace/ttcs/results/step42_ttcs01_verifier1_integration.md`).** The
first draft claimed \(\eta\ge1\) by reverse Cauchy–Schwarz. That is false when \(b^+\ge2\): two positive-square
classes need not span a Lorentzian plane. Counter-mechanism: on a Kähler \(X\) with \(p_g>0\),
\(\omega_t=\omega_0+t\operatorname{Re}\Omega\) is symplectic with \(K_{\omega_t}=K_X\), \(K_X\cdot\operatorname{Re}\Omega=0\), so \(\eta\to0\).
\(\eta\ge1\) holds under the Lorentzian hypothesis (H\(_L\)) \(|K_X\cdot\omega|\ge\sqrt{K_X^2[\omega]^2}\) (e.g. classes in one
\((1,1)\) Hodge-index plane, the Kähler case). Without (H\(_L\)) the almost-Kähler bound loses the period angle;
for arbitrary metrics LeBrun's monopole projection \((c_1^+)^2\ge c_1^2\) still gives \(2A/3\). Under (H\(_L\)):
\(P/(8\pi^2)\ge k-A(2\theta-3\theta^2)+A[(1+\alpha)^2-1]\Gamma(\theta)\).
*Proof.* With \(\sigma=-s\), \(|W^+|^2\ge\frac32W^+(u,u)^2\) (trace-free) gives the pointwise bound
\(C_+\)-density \(\ge G(\sigma,\delta)=[2\sigma^2+(3\delta-2\sigma)^2]/(192\pi^2)\), a positive-definite
quadratic form. Blair's formula fixes \(\int(2\sigma-\delta)=\ell\) exactly, so the means are
\(\bar\sigma=(1+\theta)\ell/2V\), \(\bar\delta=\theta\ell/V\); Jensen gives \(C_+\ge VG(\bar\sigma,\bar\delta)=
\ell^2\Gamma(\theta)/(128\pi^2V)\). Lemma T and the reverse Cauchy–Schwarz inequality
\(|K_X\cdot\omega|\ge\sqrt{K_X^2[\omega]^2}=\sqrt{2AV}\) for two positive-square classes give the prefactor. \(\square\)

Equality in the \(\ell\)-form holds iff \(W^+=\mathrm{diag}(\lambda,-\lambda/2,-\lambda/2)\) along \(\omega\) and
\(s,s^*\) are separately constant; then \(\lambda=\ell(2\theta-1)/(12V)\), so \(\omega\) is the lowest eigenvector only
for \(\theta<1/2\). This overlaps with, but is not identical to, LeBrun's saturating class of Prop. 2.4 (which
has \(s+s^*\) constant and \(\omega\) in the lowest eigenspace). Exact defect:
\(\mathfrak d_{AK}=\frac1{2\pi^2}\int(|W^+|^2-\frac32W^+(u,u)^2)+\int G(\sigma-\bar\sigma,\delta-\bar\delta)\ge0\).

**Readings.**
1. \(\theta=0\) (Kähler, where Hodge index gives (H\(_L\))): \(C_+\ge A(1+\alpha)^2\), i.e.
   \(P/(8\pi^2)\ge k+A[(1+\alpha)^2-1]\). This is the Step-38 Kähler tariff, strengthened by the exceptional areas.
2. \(\min_\theta\Gamma=2/3\) at \(\theta=1/3\) (\(\bar\delta=\bar\sigma/2\), i.e. \(s^*=s/2\), the extremal of
   LeBrun's Cauchy–Schwarz constant \(48\)): LeBrun's \(C_+\ge2A/3\). The almost-Kähler category alone therefore
   also stops at \(2/3\), at a definite torsion fraction rather than at a Kähler point; this is the
   almost-Kähler face of Theorem E (whose binding amplitude \(\rho=3/2\) corresponds to \(h=1/2\),
   \(\theta=h/(2-h)=1/3\)).
3. The Step-40 formal common mode is exactly the \(\alpha=0\) equality case: with \(r=2-h\) one finds
   \(\delta=4h\), \(\bar\sigma=4\), \(\theta=h/(2-h)\), and \(\beta(r)=2\theta-3\theta^2\) identically. Lemma T shows
   \(\alpha>0\) strictly, so the equality case is never attained on \(M\); but \(\alpha\) can be arbitrarily
   small, so the strictness is not quantitative.
4. **Linear torsion law (under (H\(_L\))).** \(1-\Gamma(\theta)=2\theta-3\theta^2\le2\theta\): in the almost-Kähler category the
   saving \(k-P/(8\pi^2)\) is at most \(2A\theta\), i.e. at most \(\frac{2A}{\ell}\int|\nabla\omega|^2\), linear in
   torsion. This is the almost-Kähler counterpart of Theorem N (whose free channel is the Nijenhuis energy).

## 3. The tariff is a quantitative Goldberg statement (reduction theorem)

**Proposition G (almost-Kähler form; conditional on (H\(_L\)), or on the inequality \(p\ge k-2A\theta\)).** Suppose a class \(\mathcal C\) of almost-Kähler metrics on \(M\) satisfying (H\(_L\))
satisfies the linear torsion estimate \(P\ge8\pi^2\kappa A\,\theta\) (scale-invariant; \(\theta\) as above). Then
every \(g\in\mathcal C\) satisfies
\[
\frac{P}{8\pi^2}\ \ge\ \frac{\kappa}{\kappa+2}\,k .
\]
*Proof.* \(p=P/8\pi^2\ge k-2A\theta\ge k-2p/\kappa\). \(\square\)

**Proposition G′ (all metrics, monopole form).** Under the all-metric field hypotheses of §3.6 of the
package (b⁺≥2 simple type, \(A-k>0\), scalar \(-4\) representative), Theorem N gives
\(8\pi^2k-P\le\mathcal N:=\frac12\mathbb E\int\rho^2|\nabla n|^2_{W_2}\). If \(P\ge\kappa\mathcal N\) on a class of
metrics, then \(P\ge8\pi^2k\,\kappa/(1+\kappa)\) there. Conversely, any sequence with \(P/(8\pi^2k)\to c\) has
\(\mathcal N/P\ge (1-c)/c\) asymptotically (since \(\mathcal N\ge8\pi^2k-P\)); a \(c\to0\) sequence is necessarily (not
conversely) a sequence along which the monopole Goldberg ratio \(\mathcal N/P\) is unbounded. The certified cell (if it had a
closed-host replica with the same normalized saving) would require \(\mathcal N/P\ge0.0043373/0.99566\approx0.004356\),
compatible with any \(\kappa\le229\); the certified upper coefficient bounds the best possible Goldberg constant
on the relevant class by \(\kappa\le c/(1-c)\approx229.6\) only if that replica exists.

So the per-blow-up tariff in the open range is implied by, and its failure \(c\to0\) implies the failure of, a
**linear** negative-scalar Goldberg estimate for the monopole almost-complex structures. Goldberg itself
(\(P=0\Rightarrow\nabla J=0\)) is open for \(s<0\) in general; Sekigawa's integral formula has the wrong sign there.
Within the saturating class of Theorem AKΓ (W⁺ Kähler-type along ω, \(s,s^*\) constant) the \(P=0\) endpoint
is Armstrong's theorem (no compact Einstein strictly almost-Kähler 4-manifold with ω an eigenvector of
\(W^+\)), cited by LeBrun as Corollary 2.5. The natural first coercive target is therefore a **quantitative
Armstrong theorem**: on the saturating (or near-saturating) class, \(P\ge\kappa\,A\theta\) with \(\kappa\)
independent of the cover. This is strictly weaker than quantitative Goldberg and is exactly what is needed
to exclude approximate common modes, because by AKΓ any almost-Kähler metric with saving comparable to
\(2A\theta\) must be close to the saturating class (the deficits in \(|W^+|^2\ge\frac32W^+(u,u)^2\) and in Jensen
are subtracted from the saving).

## 4. Superseded formulation

The Step-39/41 dichotomy "diffuse depletion pays unless \(W^+\) co-rotates with \(n\)" is superseded: in
almost-Kähler geometry \(W^+(n,n)\) rises with torsion automatically (\(W^+(u,u)=s/6+\delta/4\)), co-rotation is
free, the misalignment remainder is quadratic in torsion while the saving is linear (AKΓ, Theorem N). The
Cotton/Derdziński slack identified in Step 41 is still the correct name of the *stationary* endpoint
(δW⁺=0), but the coercive question is the linear Goldberg/Armstrong estimate above.

## 5. Open

- Correctly posed coercive target (from the Step-42 verification): **near-saturated quantitative Armstrong**,
  \(P/(8\pi^2)+C\,\mathfrak d_{AK}\ge c\,A\theta\) on a class with period control, with a companion control of the period
  loss \(A[1-(\eta+\alpha)^2]_+\); weaker nonperturbative variant on \(W^+(\omega)^\perp=0\):
  \(\int|\mathrm{Ric}^\circ|^2\ge c\int|\nabla\omega|^4\) (quartic, retains Armstrong's endpoint). Perturbative fixed-host version
  \(\int|\mathrm{Ric}^\circ|^2\ge c(g_0)\int|\nabla\omega|^2\) modulo gauge/KE moduli is elliptic; cover uniformity is the real
  content.
- Quantitative Armstrong on the saturating class: write AAD's differential Bianchi identities for
  \(W^+=\mathrm{diag}(\lambda,-\lambda/2,-\lambda/2)\) with constant \(s,s^*\) and determine whether \(\int|\mathrm{Ric}^\circ|^2\)
  controls \(\int|\nabla\omega|^2\) linearly; test on cohomogeneity-one almost-Kähler families.
- Monopole version: replace "almost-Kähler" by the monopole structure with \(\rho\) near constant; Lemma T
  says the harmonic part must vanish or carry positive exceptional periods; quantify either alternative.
- Gromov monotonicity gives \(a_i\ge c\,r_0^2\) when the almost-Kähler geometry is bounded at scale \(r_0\)
  around the sphere; with \(\alpha\ge kc r_0^2/\sqrt{2AV}\) this adds \(\approx2A\alpha\) to the right side of
  AKΓ, a per-class tariff proportional to \(r_0^2/\sqrt{AV}\) — real but scale-degenerate.



---

## Source step43_w0_cotton_quadratic_law_and_debts.md

Original: [sources/Sessions/S1003A02/workspace/notes/step43_w0_cotton_quadratic_law_and_debts.md](../sources/Sessions/S1003A02/workspace/notes/step43_w0_cotton_quadratic_law_and_debts.md)

# Step 43 — The corrected \(W_0\) tensor, Cotton transport, and the quadratic common-mode law

Session S1003A02, Agent3. This note enters the Step-39/41 material into the workspace and sharpens the Step-42 Goldberg reduction. It uses the scalar \(-4\) simultaneous-field conventions of `workspace/notes/step40_nijenhuis_form_and_pointwise_exhaustion.md`: for one monopole solution
\[
\psi=\rho n,\qquad |n|=1\text{ in }\Lambda^+,
\qquad
W_0=\frac14\left(\frac{\rho^2}{3}I-\psi\otimes\psi\right)
       = a\left(\frac13 I-n\otimes n\right),\quad a=\frac{\rho^2}{4}.
\]
Here \(M=W^+-W_0\) is the Weyl-alignment error of Theorems N/W.

## 1. Corrected \(W_0\) and the shallow-band geometry

The model tensor is not fixed by scalar normalization. It has eigenvalues
\[
-\frac{\rho^2}{6},\quad \frac{\rho^2}{12},\quad \frac{\rho^2}{12},
\qquad |W_0|^2=\frac{\rho^4}{24}.
\]
Thus the co-rotation forcing is strong only where the monopole amplitude is in the shallow band, especially \(\rho\approx2\); it weakens as \(\rho\to0\).

If two Kähler-type tensors have the same amplitude \(a=\rho^2/4\) and unit directions \(n,m\in\Lambda^+\), then
\[
\left|a\left(\frac13I-n\otimes n\right)-a\left(\frac13I-m\otimes m\right)\right|^2
 =2a^2(1-\langle n,m\rangle^2)
 =\frac{\rho^4}{8}\sin^2\theta .
\]
If the comparison amplitude \(b\ge0\) is optimized while the direction \(m\) is fixed and \(c=\langle n,m\rangle\), the distance from \(a(I/3-nn)\) to the ray \(b(I/3-mm)\) is
\[
\min_{b\ge0}|aK_n-bK_m|^2=
\begin{cases}
\displaystyle \frac{a^2}{2}(1-c^2)(1+3c^2),& c^2\ge\frac13,\\[4pt]
\displaystyle \frac{2a^2}{3},& c^2\le\frac13.
\end{cases}
\]
In particular \(W^+=0\) pays exactly \(|W_0|^2=\rho^4/24\), which is \(2/3\) at \(\rho=2\), but is not a universal pointwise cost.

The kinetic split is also rigid. From Step 40,
\[
K=\int|\nabla\Phi|^2=\int\frac{|\zeta|^2}{\rho}+\frac14\int \rho |\nabla n|^2.
\]
Before resolving the Lee part of \(\nabla n\), the two explicit appearances of \(|\zeta|^2\) have formal net coefficient \(8-4/\rho\), positive for \(\rho>1/2\). This is useful bookkeeping but not a final coefficient because the Dirac equation expresses the Lee component in the same amplitude/phase variables. The exact safe statement is Theorem N: after resolving that component, every non-Nijenhuis first-jet contribution occurs in the nonnegative form
\[
\rho\bigl(|d\sqrt\rho|^2+5|b|^2-2\langle d\sqrt\rho,J'b\rangle\bigr).
\]
Therefore shallow-band saving cannot be carried by amplitude/Lee kinetic energy; it must enter through the Nijenhuis/\(W_2\) rotation of \(n\), while the exact positive form and \(\zeta\) remain small.

## 2. Algebraic co-rotation is not the theorem: the AAD countermodel and the Cotton slack

Apostolov--Armstrong--Drăghici show that local strictly almost-Kähler four-manifolds can have Kähler-type algebraic curvature: in their notation \(\operatorname{Ric}_0^{\rm anti}=0\), \(W_2^+=0\), and in the unique proper three-symmetric model also \(W_3^+=0\), without \(J\) being integrable. Thus a pointwise theorem saying "\(W^+\) is rank-one and co-rotates with \(n\), hence \(\nabla n=0\)" is false. The missing information is differential.

Their differential Bianchi identities make the slack explicit. For an almost-Kähler structure in class \(\mathcal{AK}_3\), with
\(\nabla\Omega=a\otimes\phi-Ja\otimes J\phi\), \(W_3^+\) eigenvalue \(\lambda\), and conformal scalar \(\kappa\), they prove
\[
d(\kappa-s)=-12\lambda J\phi(a),
\qquad
\operatorname{Ric}_0(a)=\frac\kappa4a+2\lambda\phi(b)-J\phi(d\lambda),
\]
\[
\Delta(\kappa-s)=-\frac\kappa2(\kappa-s)-24\lambda^2+12\operatorname{Ric}_0(a,a).
\]
The proof identifies \(\delta W^+=C^+\), the self-dual Cotton tensor. In the same source, the Cotton components are written in terms of \(\nabla\operatorname{Ric}_0\), and for \(J\)-invariant Ricci the \(\mathcal V^-\) component satisfies \(\beta=-\frac12\operatorname{Ric}_0(a)\). Catino--Dameno's weighted Derdziński identity gives the eigenline version: for a divergence-free weighted self-dual Weyl tensor \(A\) with eigenvalues \(\mu_r\),
\[
d\mu_1=(\mu_1-\mu_2)\iota_{a^\sharp}\omega_3+(\mu_1-\mu_3)\iota_{c^\sharp}\omega_2,
\]
and after the conformal normalization with \(\mu_1=1\),
\[
(1-\rho)\iota_{a^\sharp}\omega_3+(2+\rho)\iota_{c^\sharp}\omega_2=0.
\]
So the stationary endpoint is indeed Derdziński/Cotton: if the weighted half-Weyl divergence vanishes and the eigenvalue gap is nonzero, eigenline rotation is constrained into conformal Kähler geometry. Away from stationarity, the source is \(\delta W^+=\nabla\operatorname{Ric}^\circ\), and the direct defect \(P=\int|\operatorname{Ric}^\circ|^2\) does not supply an \(L^2\) bound for that derivative.

## 3. Exact symbol calculation for \(\delta W_0\)

The script `workspace/scripts/step43_w0_divergence_symbol.py` computes the pointwise symbol for
\[
W_0=a\left(\frac13I-n\otimes n\right)
\]
in an oriented orthonormal frame of \(\Lambda^+\), restricting \(\nabla n\) to the almost-Kähler first-jet condition \(d(\sqrt2 n)=0\). The output is `workspace/data/step43_w0_divergence_symbol.json`.

With the script's tensor norms,
\[
\boxed{\quad
|\delta W_0|^2=\frac{a^2}{2}|\nabla n|^2+\frac13|\nabla a|^2,
\quad\text{and the two summands are orthogonal.}\quad}
\]
Equivalently, the generalized **squared** singular value of the torsion part is exactly \(1/2\), so the singular value is \(1/\sqrt2\): the characteristic polynomial is \((2\lambda-1)^4\). This is the clean algebraic core of the Cotton-transport mechanism. If \(E=W^+-W_0\), then
\[
\delta W_0=\delta W^+-\delta E=C^+-\delta E.
\]
The identity itself does **not** produce a lower bound from \(P\), because both terms on the right contain derivatives: \(C^+=\nabla\operatorname{Ric}^\circ\) and \(\delta E\). Pairing with the torsion part and integrating by parts is the only direct way to use \(P\). The displayed norm formula is restricted to a closed almost-Kähler first jet. A general monopole direction also has a Dirac-controlled Lee component; its divergence formula contains additional \(dn\) and amplitude--Lee cross terms, which must be retained or controlled by the exact \(\zeta\) form in Theorem N.

## 4. Cotton transport gives the quadratic, not linear, law

Let \(R\) denote the relevant sign-averaged Nijenhuis/rotation energy, e.g. on a shallow band
\[
R\sim\mathbb E_\epsilon\int |\nabla n_\epsilon|_{W_2}^2,
\]
and assume for this paragraph that \(a\) is bounded below on the region carrying the rotation, boundary/zero-set terms are controlled, and the almost-Kähler second-jet terms are controlled by curvature in the standard way (as in the AAD Ricci identities above). Pair the equation
\[
a\,\mathcal T(\nabla n)=\delta W^+-\delta E-\mathcal A(\nabla a)
\]
with \(\mathcal T(\nabla n)\). Integration by parts turns \(\delta W^+=C^+\) into \(\operatorname{Ric}^\circ\) paired with a first derivative of \(\mathcal T(\nabla n)\); the almost-Kähler Ricci identities express that derivative through curvature and first-jet terms. What follows is therefore a **conditional target**, not a theorem proved by the symbol calculation. On a closed constant-scalar almost-Kähler region, let \(U=\mathcal T(\nabla n)\), assume \(a\ge a_0>0\), and put \(E=W^+-W_0\). Exact integration by parts gives
\[
\frac12\int a|\nabla n|^2
 =\int\langle\operatorname{Ric}^\circ,\mathcal C^*U\rangle
  -\int\langle E,\delta^*U\rangle.
\]
Hence
\[
\frac{a_0}{2}\int|\nabla n|^2
\le \sqrt P\,\|\mathcal C^*U\|_2+\|E\|_2\,\|\delta^*U\|_2.
\]
To obtain the hoped-for scale-invariant estimate one still must prove a second-jet bound such as
\[
\|\mathcal C^*U\|_2+\|\delta^*U\|_2\le C_2\|\operatorname{Rm}\|_2.
\]
This is nontrivial: the left side contains \(\nabla^2n\) and \((\nabla n)^2\); the harmonic-form Weitzenböck formula controls only contracted Hessians. The AAD formulas supply this structure only under their additional \(\mathcal{AK}_3\) hypotheses. A localized monopole version also needs zero-set and shallow-band cutoff control, the Lee component, and amplitude-gradient products. In the exact almost-Kähler pairing the amplitude part is orthogonal to \(U\), so a separate \(\|\nabla a\|_2\) term appears only after such localization or in a more general Lee-containing test.

If these missing estimates are proved and \(E\) is noncircularly controlled, they would give
\[
R\lesssim(\sqrt P+\|E\|_2)\|\operatorname{Rm}\|_2,
\qquad \|\operatorname{Rm}\|_2^2=8\pi^2\chi(M)+P.
\]
For a ball quotient blow-up, \(\chi=A/3+k\). When \(E\) is negligible and \(A\) dominates, this becomes \(P\gtrsim R^2/A\), exactly the Step-40 common-mode scale. Thus a Cotton-source/Cauchy--Schwarz route, even if completed, yields a quadratic rather than linear law. The linear route remains perturbative spectral theory near a Kähler--Einstein host, where the Einstein operator has a finite torsion quotient after gauge and Kähler moduli are removed; cover-uniformity is a further theorem, not yet proved.

Combining a completed quadratic law with Theorem N would give a positive lower scale. Define the **total** sign-averaged \(W_2\) energy
\[
R:=\mathbb E_\epsilon\int|\nabla n_\epsilon|_{W_2}^2.
\]
Since \(0\le\rho\le2\), Theorem N gives exactly
\[
P\ge8\pi^2k-2R.
\]
If one independently proved \(P\ge R^2/(\Lambda A)\), exact optimization yields
\[
P\ge\left(\sqrt{\Lambda A+8\pi^2k}-\sqrt{\Lambda A}\right)^2
 =\frac{16\pi^4k^2}{\Lambda A}+O\!\left(\frac{k^3}{A^2}\right).
\]
This is a conditional scale law, not a current Einstein-gap theorem. A band-restricted \(R\) needs an extra complementary term. An error \(R\le C_T\sqrt A(\sqrt P+\varepsilon)\) gives only \(P\ge(R/(C_T\sqrt A)-\varepsilon)_+^2\), so no gap follows unless \(\varepsilon\) is controlled noncircularly. The heuristic numerical fraction at \(k=A/3\) is therefore not a proved constant and is not promoted. The structural constructive question remains whether closed near-minimizers can realize the diffuse quadratic scale.

## 5. Why \(E\) and \(\nabla a\) are the real escape terms

The current field identities do not bound \(\|E\|_2\) and \(\|\nabla a\|_2\) by \(P\) alone.

* \(E=M=W^+-W_0\) appears with a positive \(4\|M\|^2\) term in the signed identity, but that term is balanced against the kinetic saving \(-4K\). In a subunit sequence, \(\|M\|_2^2\) can be paid by the same shallow depletion that creates the saving; bounding it by the final value of \(P\) would be circular.
* \(a=\rho^2/4\) and \(\nabla a\) are controlled through the \(\zeta\)/amplitude-gradient terms and the depletion \(L=\mathbb E\int(2-\rho)_+\). But Theorem 39's shallow-band theorem says a subunit sequence must have \(L\gtrsim(1-c)k\). A bound through \(L\) gives only \(R\lesssim\sqrt{RA}\) at the common-mode scale, hence no positive lower bound.
* Deep depletion \(\rho<0.7758\ldots\) is unfavorable in the amplitude polynomial, but localized shallow depletion with nondegenerate \(W^+\) can still finance \(E\) and \(\nabla a\) unless a new localization or monotonicity statement is added.

Therefore the exact escape configuration is now precise: a near-minimizer avoiding a per-class tariff must keep \(a\) in the shallow band, keep \(\zeta\) small, make \(W^+\) nearly Kähler-type and co-rotating with \(n\) except for an \(E\) financed by depletion, and distribute Nijenhuis rotation over a volume comparable to \(A\), while Lemma T forces exceptional classes to appear as tiny positive-area pseudoholomorphic spheres or through zeros of the harmonic part rather than as exactly null periods of a nowhere-zero form.

## 6. Sekigawa/Kirchberg formula: the resisting term

Kirchberg's four-dimensional almost-Kähler identity records exactly the sign failure. With his conventions,
\[
Q(J)+\int\left(|\widetilde R|^2+4|\operatorname{Ric}_\star^-|^2+rac S2|\nabla J|^2+|\nabla J|^4\right)=0,
\]
and equivalently
\[
Q(J)+\frac12\int\left(|\widetilde R|^2+|\nabla J|^4+|W_+|^2-\frac{S^2}{6}\right)=0.
\]
For \(S=-4\), the term \((S/2)|\nabla J|^2=-2|\nabla J|^2\) has the wrong sign. The obstruction
\[
Q(J)=2\int\langle\varphi,\psi\rangle
\]
is a derivative-of-Ricci pairing: Kirchberg writes
\[
\langle\varphi,\psi\rangle=rac14\left\langle J\varphi(X^k,X^l),
(\nabla_{X_k}\operatorname{Ric})X_l-(\nabla_{X_l}\operatorname{Ric})X_k\right\rangle.
\]
Thus the exact resisting term is the same Cotton source identified above. If the relevant harmonic-Weyl/Eigenform conditions make \(Q(J)=0\), the additional Weyl algebra can force Kählerness, but for negative scalar curvature and only \(P\)-control, \(Q(J)\) is uncontrolled except by the quadratic Cauchy--Schwarz law.

## 7. Proper three-symmetric test object

The mandatory Apostolov--Armstrong--Drăghici local model has
\[
s=-\frac34,\qquad \kappa=\frac34,
\qquad \operatorname{spec}(\operatorname{Ric})=(0,0,-3/8,-3/8).
\]
Their identity \(\kappa-s=\frac32|\nabla\Omega|^2\) gives \(|\nabla\Omega|^2=1\). Exact arithmetic in `workspace/scripts/step43_proper3symmetric_test.py` gives
\[
|\operatorname{Ric}^\circ|^2=\frac9{64},
\qquad
\frac{|\operatorname{Ric}^\circ|^2}{|\nabla\Omega|^4}=\frac9{64}.
\]
Thus this strictly almost-Kähler, Kähler-curvature-type countermodel does not refute a quartic pointwise inequality, but any universal pointwise constant in these conventions is at most \(9/64\). It is local/noncompact and yields no closed-manifold gap.

## 8. Current mathematical consequence

The nonperturbative linear estimate
\[
P\ge \kappa\int |\nabla J|^2
\]
is a quantitative negative-scalar Goldberg theorem and should not be claimed. The honest coercive outputs now split into two precise, attackable statements:

1. **Perturbative KE theorem.** Near a negative Kähler--Einstein ball quotient, after gauge fixing and removing Kähler moduli, prove
\[
\int|\operatorname{Ric}^\circ|^2\ge \kappa_0\int |\nabla J|^2
\]
with \(\kappa_0\) independent of finite covers if the Bochner/Koiso constants are pointwise or have a cover-uniform spectral gap. This only excludes common-mode realizations close to the KE host.
2. **Quadratic transport theorem.** Prove the Cotton inequality above with exact cutoffs and zero-set terms. If \(E\) and \(\nabla a\) can be bounded by noncircular quantities, it gives \(P\gtrsim k^2/A\). If they cannot, the failure identifies the construction target: diffuse shallow depletion with co-rotating \(W^+\) and controlled exceptional-area/zero-set topology.

The direct global problem is still open, but the alternatives have changed. It is plausible that \(P>0\) for every fixed blow-up while the best per-class coefficient tends to zero along towers; this would reconcile positive Einstein gaps with the formal common mode and the certified subunit local cell.



---

## Source step44_perturbative_ke_coercivity_and_pocket_price.md

Original: [sources/Sessions/S1003A02/workspace/notes/step44_perturbative_ke_coercivity_and_pocket_price.md](../sources/Sessions/S1003A02/workspace/notes/step44_perturbative_ke_coercivity_and_pocket_price.md)

# Step 44 — Cover-independent coercivity at complex-hyperbolic hosts, and the price of \(s^*>0\) pockets

Session S1003A02, Agent2. Data/script: `workspace/scripts/step44_perturbative_ke.py` →
`workspace/data/step44_perturbative_ke.json`. Normalization unless stated: scalar curvature
\(s=-4\), \(\operatorname{Ric}=\lambda g\) with \(\lambda=-1\) at the Kähler–Einstein (KE) host;
\(P=\int|\operatorname{Ric}^\circ|^2\) (scale invariant in dimension four).

The Step-43 handoff asked for (i) the perturbative negative-KE torsion theorem with an explicit
statement of whether its constant is cover-independent, and (ii) a pricing of the "tiny positive
exceptional area" branch of Lemma T. Both are answered below. The nonperturbative quadratic
Cotton law and the second-jet estimate are untouched and remain open.

---

## 1. Four pointwise gaps at a complex-hyperbolic surface

Let \(X_\Gamma=B^4/\Gamma\) be any compact quotient of the complex-hyperbolic ball (\(\Gamma\subset PU(2,1)\)
torsion free, cocompact), with its KE metric \(g_\Gamma\). Each operator entering the linearization
of \(P\) and of the canonical monopole has a Weitzenböck form \(\nabla^*\nabla+\mathcal V\) (or a
sum of such) whose potential is a fixed algebraic function of the curvature of \(\mathbb{CH}^2\).
Hence every lower bound below holds with the same constant on every \(X_\Gamma\), in particular
uniformly along every tower of finite covers. A Γ-dependent spectral gap never enters.

**(G1) Einstein operator on TT tensors (Koiso, computed).** For TT \(h\) on an Einstein manifold,
\(L_E h=\nabla^*\nabla h-2\mathring R h\) and the \(d^\nabla\) Bochner identity gives
\[
\langle L_Eh,h\rangle=\|d^\nabla h\|^2+\langle(-\lambda-\mathring R)h,h\rangle\ \ge\ (-\lambda-a)\|h\|^2,
\qquad a=\max\operatorname{spec}\mathring R|_{S^2_0}.
\]
Exact computation on \(\mathbb{CH}^2\) with holomorphic sectional curvature \(-4\) (\(\lambda=-6\),
sectional curvatures in \([-4,-1]\)): \(\mathring R=-2\) on the 3-dimensional \(J\)-invariant
trace-free tensors and \(\mathring R=+4\) on the 6-dimensional \(J\)-anti-invariant ones. Thus
\(a=4\) and the pointwise Koiso gap is \(-\lambda-a=2=|\lambda|/3\). (Control: real hyperbolic
\(K=-1\), \(n=4\): \(\mathring R\equiv1\), gap \(2\), the known rigid case.) On the \(J\)-invariant
sector the Hodge identification \(L_E\leftrightarrow\Delta_d-2\lambda\) on primitive (1,1)-forms
gives the larger gap \(2|\lambda|\). In the \(s=-4\) normalization:
\[
\langle L_Eh,h\rangle\ \ge\ \tfrac13\|h\|^2\qquad(h\ \text{TT}).
\]
So the infinitesimal Einstein rigidity of ball quotients (Calabi–Vesentini/Koiso) is, in real
dimension four, a pointwise Bochner statement; the \(J\)-anti-invariant sector, which carries
complex-structure deformations, is the binding one with margin \(|\lambda|/3\).

**(G2) Conformal channel.** \(\operatorname{Ric}^\circ(e^{2f}\hat g)=\operatorname{Ric}^\circ(\hat g)
-2(\hat\nabla^2f-df\otimes df)^\circ\), and on an Einstein background with \(\lambda<0\)
\[
\|(\nabla^2f)^\circ\|^2=\tfrac34\|\Delta f\|^2+|\lambda|\,\|\nabla f\|^2 ,
\]
which controls \(\|df\|_{H^1}^2\) (not \(\|f-\bar f\|^2\), which is not needed: \(P\) and the monopole
direction depend on \(f\) only through \(df\), see §2).

**(G3) Gauge.** The conformal Killing operator satisfies
\(\|(L_Xg)^\circ\|^2=2\|\nabla X\|^2+2(1-\tfrac2n)\|\operatorname{div}X\|^2+2|\lambda|\|X\|^2\ge2|\lambda|\|X\|^2\),
so the York decomposition \(h=h_{TT}+L_Xg+fg\) and the Ebin slice have uniformly bounded inverses.

**(G4) Linearized Seiberg–Witten operator at the canonical Kähler solution.** At a KE surface
the canonical solution \((A_0,\Phi_0)\) of the class \(K\) has \(\nabla_{A_0}\Phi_0=0\),
\(|\Phi_0|^2=-s\), \(c(F^+_{A_0})=(\Phi_0\Phi_0^*)_0\). With the gauge-fixed linearization
\[
\mathcal L(a,\psi)=\Bigl(d^*a-\tfrac12\,i\operatorname{Im}\langle\Phi_0,\psi\rangle,\ d^+a-\sigma'(\psi),\ D_{A_0}\psi+\tfrac12a\cdot\Phi_0\Bigr),
\]
the Clifford-model computation verifies: (i) all first-order cross terms in \(\|\mathcal L(a,\psi)\|^2\)
cancel identically at the symbol level (mismatch \(2\times10^{-16}\); every other sign/gauge
coefficient tested fails), so they vanish exactly when \(\nabla\Phi_0=0\); (ii) the zeroth-order
potential at \(s=-4\) has eigenvalues \(\tfrac12\) (four, on \(a\): \(\lambda/2+|\Phi_0|^2/4\)),
\(2\) (real part of \(\psi\parallel\Phi_0\)), \(1\) (gauge direction), and \(0,0\) on
\(\psi_\perp\in\Phi_0^\perp\cong\Lambda^{0,2}\cong K^{-1}\). The two zero eigenvalues are lifted
by the Kodaira/Landau identity \(\nabla^*\nabla=2\bar\partial^*\bar\partial+i\Lambda F=2\partial^*\partial-i\Lambda F\)
on the parallel line subbundle \(\Phi_0^\perp\), whose curvature \(\mp i\lambda\omega\) has constant
\(|i\Lambda F|=2|\lambda|\). Therefore
\[
\|\mathcal L(a,\psi)\|^2\ \ge\ \tfrac12\|\nabla a\|^2+\|\nabla\psi\|^2+\tfrac{|\lambda|}2\|(a,\psi)\|^2 ,
\]
a cover-independent gap \(|\lambda|/2\). (The 1-form part uses \(\|d^*a\|^2+\|d^+a\|^2\ge\tfrac12\langle\Delta_da,a\rangle\).)

Because the curvature of \(\mathbb{CH}^2\) is negative, the exponential map at any point of
\(X_\Gamma\) is a covering on every ball, so local elliptic (Schauder/\(L^p\)) estimates can be done on
lifts to \(T_pX_\Gamma\); combined with an \(L^2\) gap this gives uniformly bounded Hölder inverses
(Agmon/Combes–Thomas decay of the Green kernel). No lower bound on the injectivity radius of
\(X_\Gamma\) is needed.

## 2. Theorem A (perturbative torsion quotient, cover independent)

**Theorem A.** There are universal constants \(\varepsilon_0,\kappa,C>0\) (depending only on the
geometry of \(\mathbb{CH}^2\)) such that for every compact ball quotient \(X_\Gamma\) and every metric
\(g\) on \(X_\Gamma\) with \(\inf_{\phi,c}\|\phi^*g-c\,g_\Gamma\|_{C^{2,\alpha}}\le\varepsilon_0\)
(Hölder norms on unit balls):

1. (quadratic Einstein gap) writing, after a diffeomorphism and scaling, \(g=e^{2f}(g_\Gamma+k)\)
   with \(k\) transverse-traceless,
   \[
   P(g)\ \ge\ \kappa\bigl(\|k\|_{H^2}^2+\|df\|_{H^1}^2\bigr);
   \]
2. (unique canonical branch) the Seiberg–Witten equations of the class \(K\) for \(g\) have a
   unique solution within \(C\varepsilon_0\) of the canonical Kähler solution (in the slice), and
   its almost-complex structure \(n_g\) satisfies
   \[
   \int|\nabla n_g|^2\ \le\ C\bigl(\|k\|_{H^1}^2+\|df\|_{L^2}^2\bigr)\ \le\ \tfrac C\kappa\,P(g);
   \]
3. hence for the Nijenhuis energy \(R(g)=\int\rho^2|\nabla n_g|^2_{W_2}\) of that branch
   \(R(g)\le C' P(g)\). For the scalar \(-4\) Yamabe representative \(\hat g\) (itself
   \(C\varepsilon_0\)-close to the host, the linearized Yamabe operator \(6\Delta+2|s|\) being uniformly
   invertible), Theorem N at \(Q=0\) gives \(2P(\hat g)\le R(\hat g)\le C'P(\hat g)\):
   near a complex-hyperbolic host the Einstein defect and the monopole Nijenhuis energy are
   comparable, uniformly in \(\Gamma\).

*Proof.* (a) Slice. Ebin's slice for Diff ⋉ Conf at \(g_\Gamma\) has uniform constants by (G2)–(G3);
write \(g=\phi_*e^{2f}(g_\Gamma+k)\), \(\delta k=0\), \(\operatorname{tr}k=0\), \(|f|+\|k\|_{C^{2,\alpha}}\le C\varepsilon_0\).
(b) Expansion. \(\operatorname{Ric}^\circ(g_\Gamma+k)=\tfrac12L_Ek+Q_1(k)\) with
\(|Q_1|\le C\varepsilon_0(|\nabla^2k|+|\nabla k|+|k|)\); the conformal formula of (G2) is exact and
contains only \(df,\nabla^2f\). The \(TT\) and Hessian channels are \(L^2\)-orthogonal
(\(\int\langle L_Ek,\nabla^2u\rangle=\int\langle k,\nabla^2(\Delta-2\lambda)u\rangle=0\)). Hence
\(P\ge(1-\eta)\bigl(\tfrac14\|L_Ek\|^2+4\|(\nabla^2f)^\circ\|^2\bigr)-C_\eta\varepsilon_0^2(\|k\|^2_{H^2}+\|df\|^2_{H^1})\),
and (G1), (G2) with elliptic regularity give item 1 for \(\varepsilon_0\) small. (c) Monopole. Scale
covariance is exact: for constant \(c\), \(\Phi\mapsto e^{-c}\Phi\) maps solutions of \(g\) to those of
\(e^{2c}g\) and fixes \(n\). For \(\tilde g=e^{2f}\hat g\), the ansatz \(\tilde\Phi=e^{-f}\Phi_{\hat g}\)
solves the curvature equation exactly (\(F^+\) and \(\sigma\) are both conformally natural as
2-forms) and the Dirac equation up to \(\tfrac12 e^{-5f/2}df\cdot\Phi\). By (G4) and the uniform
implicit function theorem, the true branch solution differs from the ansatz by \(O(\|df\|)\) and
from the Kähler solution by \(O(\|k\|_{H^1})\) through the \(k\)-dependence of the Levi-Civita and
spin connections. Since \(\nabla n=0\) at \(g_\Gamma\), \(\nabla n_g\) is bounded by these
differences, giving item 2. Item 3 combines item 2 with Theorem N at \(Q=0\), where all
non-Nijenhuis terms are nonnegative. ∎

**What Theorem A establishes and what it does not.** It is the cover-uniform perturbative
Goldberg statement: diffuse almost-complex rotation costs linearly in \(P\) near every compact
complex-hyperbolic host, with one universal constant. Because the formal common mode needs
\(R\sim\sqrt{PA}\) (Step 43), while Theorem A forces \(R\le C'P\), a common mode with
\(P\ll A\) cannot sit within \(\varepsilon_0\) of a KE host. The constant is pointwise; the binding
input is the \(J\)-anti-invariant Koiso margin \(|\lambda|/3\).

It is not the tariff. On \(M=X_\Gamma\#k\overline{\mathbb{CP}}^2\) no metric is globally
\(C^2\)-close to the host. The localized version, "if \(g\) is \(\varepsilon_0\)-close to \(g_\Gamma\) on a
bulk domain \(\Omega\), then the bulk Nijenhuis energy is \(\le C\,P\) on a slightly larger domain,"
needs two further inputs that are **not** proved:

- *Bulk selection.* An actual solution on \(M\) for each sign class must be close to the canonical
  solution on \(\Omega\). The \(L^2\) bound \(\int(|\Phi|^2+s)^2\le\int s^2-32\pi^2c_1^2\) coming from
  the Weitzenböck formula is extensive. It allows localized depletion of unit size anywhere in a
  large bulk, which is exactly what the Step-39 depletion law requires of a subunit
  near-minimizer. So bulk-closeness of the field is not implied by bulk-closeness of the metric.
- *Lower-order outer layer.* Locally, Einstein deformations of \(\mathbb{CH}^2\) exist, so a local
  coercive estimate always carries a term \(\int_{\Omega'\setminus\Omega}|k|^2\). It is not controlled
  by \(P\) without global input.

The correct structural reading is therefore: *every subunit near-minimizer has, in each region
where it is \(C^{2,\alpha}\)-close to a complex-hyperbolic metric, either a monopole far from the
canonical one there (depletion/vortex) or negligible Nijenhuis saving there.* The saving must be
financed either away from KE geometry or by field depletion, which is the Step-39 channel.

## 3. Proposition Π (price of \(s^*\ge0\) pockets in the almost-Kähler profile)

In an almost-Kähler 4-manifold, \(W^+(\hat\omega,\hat\omega)=s/6+|\nabla\omega|^2/4\), so
\(\mathbb R^+(\hat\omega,\hat\omega)=W^+(\hat\omega,\hat\omega)+s/12=s^*/4\) with
\(s^*=s+|\nabla\omega|^2\). By Theorem F, a Burns insertion of parameter \(x_0\) whose exceptional
sphere is aligned with \(\omega\) (small *positive* symplectic area) changes \(P\) by
\(8\pi^2(1-x_0s^*(p)/4)+O(x_0^{6/5})\). It saves at first order exactly where \(s^*>0\), i.e. where
the torsion density \(\delta=|\nabla\omega|^2\) exceeds \(\sigma=-s\).

**Proposition Π.** Let \((M,g,\omega)\) be a closed almost-Kähler 4-manifold, \(V\) its volume,
\(\ell=8\pi K_\omega\cdot[\omega]>0\), \(\theta=\int|\nabla\omega|^2/\ell\), and
\(\varphi=\operatorname{Vol}\{s^*\ge0\}/V\in[0,1)\). Then
\[
C_+\ \ge\ \frac{\ell^2}{128\pi^2V}\Bigl[\Gamma(\theta)+\frac{\varphi}{1-\varphi}(1-\theta)_+^2\Bigr]
\ \ge\ \frac{\ell^2}{128\pi^2V}\cdot\frac{2}{3-2\varphi},
\]
the last minimum attained at \(\theta=1/(3-2\varphi)\). At \(\varphi=0\) this is AKΓ (minimum \(2/3\));
\(\varphi=1/2\) already forces the Kähler constant \(1\).

*Proof.* AKΓ's pointwise step gives \(C_+\ge\int G(\sigma,\delta)\) with the convex quadratic
\(G=[2\sigma^2+(3\delta-2\sigma)^2]/192\pi^2\). Split \(M\) into the pocket \(\Omega_+=\{\delta\ge\sigma\}\) and
its complement. Jensen within each region reduces to constants \(v_1\in\{\delta\ge\sigma\}\), \(v_2\)
with \(\varphi v_1+(1-\varphi)v_2=\bar v\). Writing \(v_1=\bar v+(1-\varphi)u\), \(v_2=\bar v-\varphi u\), the
mixed terms cancel and \(\varphi G(v_1)+(1-\varphi)G(v_2)=G(\bar v)+\varphi(1-\varphi)G(u)\). The
constraint is \(u_\delta-u_\sigma\ge(\bar\sigma-\bar\delta)/(1-\varphi)\). The minimum of
\(2x^2+(3y-2x)^2\) on \(y-x=D\) is \(6D^2\) (symbolic). Blair fixes \(\ell=V(2\bar\sigma-\bar\delta)\), so
\(\bar\sigma-\bar\delta=\tfrac{\ell}{2V}(1-\theta)\), and \(VG(\bar v)=\ell^2\Gamma(\theta)/(128\pi^2V)\) (Step 42). The
optimization in \(\theta\) is elementary. A brute-force two-region search reproduces the formula
(e.g. \(38.684\) sampled vs \(38.667\) exact at \(\varphi=.1\)). ∎

**Consequences for the tiny-area branch of Lemma T.**
(a) Uniform \(s^*>0\) is prohibitively expensive (\(\theta\ge1\), \(\Gamma\ge2\)). First-order savings
must be localized in pockets.
(b) Per sphere, the Theorem-F saving is linear in \(x_0\), while a pocket of radius \(r\gg\sqrt{x_0}\)
costs \(O(r^4)\) in the convex profile. So convexity does **not** exclude the pocket route at small
\(x_0\). What limits it is the perturbative range of Theorem F, which delivers only \(c=1-O(x_0)\).
Driving \(c\) far below one through aligned tiny-area spheres needs nonperturbative cells, which
is the regime of the certified perpendicular cell, but with the opposite (aligned) orientation.
(c) Theorem A makes pockets incompatible with KE-closeness: \(\delta\ge\sigma=4\) on a pocket forces
\(\int|\nabla n|^2\ge4\operatorname{Vol}(\Omega_+)\), while near a host \(\int|\nabla n|^2\le CP\). In the
regime \(P\ll\operatorname{Vol}\) the pockets therefore live in regions far from KE geometry.
(d) Scope. Π is an almost-Kähler (\(\ell\)-form) statement. Converting \(\ell\) to \(A\) needs the
Lorentzian hypothesis \(H_L\). Under \(H_L\) it gives \(P/8\pi^2\ge k-A\bigl[1-2(\eta+\alpha)^2/(3-2\varphi)\bigr]\),
which is informative only for \(\varphi\) near \(1/2\). Π does not see the monopole field.

## 4. Updated global picture

- **Perturbative regime: settled.** Near any compact complex-hyperbolic host there is one universal
  constant pricing diffuse rotation linearly, \(R\le C'P\), and the defect is quadratically coercive
  modulo Diff ⋉ scaling, with both constants pointwise. Within \(\varepsilon_0\) of KE, \(P\asymp R\).
- **Nonperturbative regime: open.** It is still governed by the conditional quadratic law
  \(P\gtrsim R^2/A\) (Step 43), whose missing inputs are the second-jet/Cotton estimate and the
  noncircular control of \(E=W^+-W_0\) and \(\nabla a\). Theorem A supplies the linear
  complement: the two regimes join only if one proves that a near-minimizer which is far from KE
  everywhere still pays (a quantitative non-Kähler–Einstein bulk statement). That is the true
  remaining global question for diffuse modes.
- **Construction side (for A01).** Any \(c\to0\) family must be, in most of its volume, outside the
  \(\varepsilon_0\)-neighbourhood of every KE metric (Theorem A), or have bulk monopoles away from
  canonical (depletion). Aligned tiny-area exceptional spheres need \(s^*>0\) pockets priced by Π;
  the perpendicular/null-period alternative needs the closed form to vanish on the spheres (Lemma T).



---

## Source theorem_package_v1.md

Original: [sources/Sessions/S1003A02/workspace/notes/theorem_package_v1.md](../sources/Sessions/S1003A02/workspace/notes/theorem_package_v1.md)

# Einstein gaps on four-manifolds: dependence-ordered theorem package (v1)

This file is a research map for the Discovery loop. It records the mathematical objects, proved results, certified computations, numerical structures, and open implications in dependency order. It is not a paper and does not turn construction-level information into a theorem about the unrestricted infimum.

## 1. Functionals, scale, and distinct questions

Let \(M\) be a closed oriented smooth four-manifold. The direct Einstein defect \(\mathcal E\), its trace-free Ricci component
\[
P(g)=\int_M |\operatorname{Ric}^{\circ}_g|^2\,d\mu_g,
\]
and the field-alignment functionals \(\kappa_\beta\) are distinct. The invariant of interest is \(\alpha(M)=\inf_g\mathscr D(g)\), with the precise normalization and admissible class inherited from the geometric-analysis corpus. Any passage among \(\mathcal E\), \(P\), and \(\kappa_\beta\) must use its stated scalar/Yamabe normalization and same-metric identities.

Research status vocabulary used below:

- **Proved:** analytic argument with its hypotheses recorded.
- **Certified:** a fixed explicit metric or flow is enclosed by interval arithmetic, with exact input data.
- **Numerical structure:** reproducible computation that guides a theorem but is not itself a general theorem.
- **Open:** an implication needed for the unrestricted \(\alpha\)-problem has not been established.

## 2. Actual fields control the regular bulk

### 2.1 Bounded-form interface and linear coercivity — Proved

The inherited bounded-form theorem has the form \((1+B_\psi)d_\psi\ge c(K)\). The I40/I41 estimates retain differential information from an actual field; schematically,
\[
\Sigma\le C\{\Pi+\sqrt{\Pi Y}\}.
\]
Formal Chern--Weil and monopole-number budgets do not imply this estimate. Hence a localization theorem for near-minimizers must carry the actual field, or an equivalent differential object, through regular regions and concentration regions.

Primary paths: `Skills/geometric-analysis/research/supplements/20261004_classical_and_quantitative_gaps.tex`; `Skills/geometric-analysis/research/paper/sections/variational_selection_and_global_cost.tex`; `workspace/notes/step1_field_compatibility_and_route_portfolio.md`.

### 2.2 Density-free finite-\(\beta\) alignment theorem — Proved

Assume metric-wise conformal monopole supply with \(p\ge A>0\), \(a^2\ge T_+\), and \(T_+\le\theta A\) for \(\theta<3/4\). Then every finite \(\beta\ge2\) has a uniform positive lower bound for \(\kappa_\beta\). The algebra is governed by
\[
a(\theta,\beta)=
\frac{(\frac34-\theta)\beta^2+(\frac12-\frac{11}{4}\theta)\beta+6-\theta}
{\beta(9\beta-\theta+6)},
\]
whose numerator has discriminant
\[
\frac{57}{16}\left(\theta-\frac23\right)
\left(\theta+\frac{142}{19}\right).
\]
At \(\theta=2/3\) it is \((\beta-8)^2/12\). This explains the thresholds \(2/3\), \(\beta=8\), and \(3/4\). The verified Kähler application is restricted to the recorded minimal general-type, \(p_g\ge1\), blow-up setting. This is an alignment theorem and does not imply a positive direct Einstein gap.

Primary paths: `workspace/notes/step4_O10_localization_and_orbifold_test.md`; `workspace/scripts/o10_localization.py`; Step-5 records.

### 2.3 Charged concentration tangents — Proved model calculation

One- and multi-centre Gibbons--Hawking spaces carry genuine solutions of the leading coupled tangent equations, with
\[
\int|\nabla v|^2=8\pi^2m_*k\ell^2,
\qquad
\int|d|v|^2|^2=\frac{16\pi^2}{3}m_*^2k\ell^2.
\]
The \(k\)-centre topology has \(b_2=k-1\) and boundary \(L(k,1)\). These tangents rule out a leading-order density-free Liouville argument; they do not by themselves produce closed-manifold escape sequences.

Primary paths: `workspace/scripts/verify_gh_tangent.py`; `workspace/scripts/gh_multicentre_energy.py`.

## 3. Zero gap, attainment, exact Einstein existence, and entropy-supplied nonexistence

### 3.1 Canonical-model resolutions — Proved construction

For the stated minimal Kähler surfaces of general type, resolving canonical negative Kähler--Einstein orbifolds with shrinking Ricci-flat ALE pieces gives smooth metrics with \(\mathcal E\to0\), hence \(\alpha=0\). The core contribution vanishes because its volume tends to zero even though \(|\operatorname{Ric}+g|^2=4\) there. In this zero-gap class, attainment is equivalent to existence of a smooth non-Ricci-flat Einstein metric on the underlying smooth manifold. Ampleness supplies the canonical Kähler--Einstein case; nef/nonample does not exclude all other complex or non-Kähler Einstein metrics.

### 3.2 Rational-blowdown examples — Proved construction with source attribution

Şuvaina-type generalized rational blowdowns provide further zero-gap manifolds, including simply connected minimal symplectic non-Kähler examples. Exact Einstein exterior, scaled Ricci-flat filler, bounded-curvature shrinking collar, and vanishing filler volume yield \(\alpha=0\). The source establishes non-Kählerness, not absence of every complex structure.

Primary paths: `workspace/notes/step6_theorems_and_O11_rotation.md`; `Knowledge/objects/papers/The-Yamabe-invariant-of-a-class-of-symplectic-4-manifolds--93fc75a3247d--f4170b4b9bdb/object.md`.

### 3.3 Real-hyperbolic blow-ups: exact Einstein nonexistence from entropy — Proved

Let \(Y\) be a closed oriented real-hyperbolic four-manifold and \(X=Y\#k\overline{\mathbb{CP}}^{\,2}\). The pinch map \(X\to Y\) has degree one, while
\[
\chi(X)=\chi(Y)+k,\qquad \sigma(X)=-k.
\]
Kotschick's entropy-strengthened Einstein inequality and its Sambusetti/BCG degree corollary require every Einstein \(X\) mapping with degree \(d\ne0\) to \(Y\) to satisfy
\[
\chi(X)\ge\frac32|\sigma(X)|+|d|\chi(Y).
\]
For the pinch map this would give \(k\ge3k/2\), impossible for every \(k\ge1\). Hence no real-hyperbolic blow-up carries an Einstein metric. This is a new actual supplier beyond monopole classes: the input is homological minimal-volume entropy. It is an exact existence obstruction, not by itself a positive critical-\(L^2\) Einstein-gap theorem for the low-blow-up range. The source does not compute the Yamabe invariant of these blow-ups.

Primary paths: `workspace/notes/step21_entropy_hyperbolic_cells_and_offbolt_weyl.md`; `Knowledge/objects/papers/ENTROPIES-VOLUMES-AND-EINSTEIN-METRICS--0ee1eb110f9d--94203f883336/object.md`; `trace/ttcs/results/step21_ttcs01_verifier1_integration.md`.

### 3.4 Real-hyperbolic blow-ups: the gap is the Yamabe problem — Proved identity; sharp value conditional on one Yamabe identity (Step 23)

For every metric on \(X_k=Y\#k\overline{\mathbb{CP}}^2\), with \(Y_{\rm hyp}^2/12=16\pi^2\chi(Y)\),
\[
P=8\pi^2k+4\int|W^+|^2+\frac{Y[g]^2-Y_{\rm hyp}^2}{12}+3\int(\Delta u/u)^2+24\int|\nabla u|^2\quad(Y[g]<0),
\]
where \(u^2g\) is the \(\hat s=-24\) Yamabe metric (exact form of LeBrun's \(\int s^2\ge Y[g]^2\)). **Theorem H:** if \(\mathcal Y(X_k)=Y_{\rm hyp}\) (Schoen's conjecture plus blow-up invariance), then \(P>8\pi^2k\) for every metric, \(\inf P=8\pi^2k\) (Burns concentration, Theorem F with \(\mathbf R^+=-2I\)), not attained (equality would make \(g\) a Yamabe-invariant-attaining metric, hence Einstein; LeBrun 1996), and \(\alpha(X_k)=\inf\mathcal E=\inf\mathcal J=4k/(k+6\chi(Y))\) for \(1\le k\le2\chi(Y)\), not attained for \(k<2\chi(Y)\). At \(k=2\chi(Y)\) the infimum is unconditionally \(1\) and its attainment is equivalent to an anti-self-dual (for \(\mathcal E\): anti-self-dual constant-scalar) metric, not excluded here. Arbitrary minimizing sequences are globally asymptotically half-conformally-flat and Yamabe-extremal; the allocation of \(8\pi^2\) to each exceptional class is proved only for Burns sequences. Unconditionally, with \(y_k=\mathcal Y(X_k)^2/Y_{\rm hyp}^2\): \(P\ge8\pi^2k-(1-y_k)16\pi^2\chi(Y)\), and \(\alpha(X_k)>0\) whenever \(y_k>1-k/(2\chi(Y))\); \(y_k=1\) is sufficient, not proved necessary, for \(\inf P=8\pi^2k\). For \(k>2\chi(Y)\), \(\mathcal E\ge\mathcal J>1\) pointwise but \(\inf\mathcal J=1\) by conformal inflation and \(\inf\mathcal E\in[1,4k/(k+6\chi(Y))]\) is undetermined. The conformal identity is already implicit in LeBrun's 1996 Lemma 1. Theorem H\(_\varepsilon\) is the pointwise-Ricci shadow. Path: `workspace/notes/step23_yamabe_identity_hyperbolic_sharp_gap_and_cell_channels.md` §3.
### 3.5 Kähler blow-up tariff and paired actual fields — Proved restricted theorem; global paired coercivity open (Step 38)

For a fixed blow-up complex structure \(M=X\#k\overline{\mathbb{CP}}^2\), \(A=K_X^2\), every Kähler metric in the complex orientation satisfies
\[
 C_+=\frac1{2\pi^2}\int|W^+|^2+\frac1{96\pi^2}\int s^2
 =\frac1{32\pi^2}\int s^2\ge A,
 \qquad P\ge8\pi^2k.
\]
Writing \(K_M=K_0+\sum E_i\), \(\Omega=[\omega]\), and \(e_i=\Omega\cdot E_i>0\), the Hodge-index proof is
\[
 C_+=\frac{(K_M\cdot\Omega)^2}{\Omega^2}+\frac1{32\pi^2}\int(s-\bar s)^2,
 \qquad K_0\cdot\Omega\ge\sqrt{A\Omega^2}.
\]
Hence the inequalities are strict when \(k>0\). Equality of the Kähler infimum with \(8\pi^2k\) additionally needs a Kähler recovery family; Theorem F alone is Riemannian and does not supply that input.

For sign-family monopoles \(a_\epsilon=c+\sum\epsilon_iE_i\), the paired inner product is a section of the relative twisting line with
\[
 c_1(u_{\epsilon\epsilon'})=\frac{a_\epsilon-a_{\epsilon'}}2;
\]
a single sign flip therefore gives \(c_1(u)=\pm E_i\), not \(\pm2E_i\). Its zero may be an amplitude vortex or pointwise spinor orthogonality. In scalar \(-4\) normalization, simultaneous actual solutions give the exact nonnegative amplitude form and in particular
\[
 P\ge8\pi^2Q-4\,\mathbb E_\epsilon\int(2-|\Phi_\epsilon|^2).
\]
The paired field recovers individual exceptional topology lost by convex projection, but it is exactly the singleton Walsh sector rather than an additional positive sector. For one sign flip, with relative curvature \(h=(f-f')/2\),
\[
 |h^+|^2=\frac{(\rho-\rho')^2}{8}+\frac{|w|^2}{2},\qquad
 \|h^-\|_2^2-\|h^+\|_2^2=4\pi^2.
\]
The fixed negative-square charge lies in the field-undetermined anti-self-dual relative curvature. Moreover the combined bilinear \((u,w)\) lies in a rank-two bundle of \(c_2=0\); its normalized value is \(S^3\)-valued where both spinors are nonzero, so the \(u\)-phase vortex can unwind through \(w\). No metric-uniform vortex/relative-rotation excess follows without extra projection/noncollapse and kinetic-compensation input. The cheap perpendicular cell has zero compatible almost-Kähler period on \(E\), showing that this rotation channel is geometrically real.

The SU(2)-invariant isolated-cell monopole ODE is exact, but the Step-37/38 numerical attempts imposed incorrect finite-end or cutoff conditions and produced no monopole profile. Exact finite-radius matching to the complete canonical CH monopole is impossible in a charged invariant sector by backward uniqueness; asymptotic convergence requires matching the two-dimensional CH stable manifold. Closed-host monopoles need not induce that isolated invariant boundary problem.

For a topology-preserving ramification neighbourhood with the same controlled boundary germ as its Kähler--Einstein model, relative signature and the relative \(P\) identity give exactly
\[
 \Delta B=\frac14P_N-\frac1{48}\Delta S;
\]
in scalar \(-4\) normalization, \(\Delta B=P_N/4-\Delta V/3\). Hence characteristic flux alone has no anti-self-dual retention sign: retention is precisely a relative-volume upper problem, and depletion occurs when \(\Delta V>3P_N/4\).

Primary path: `workspace/notes/step38_kahler_and_paired_field_scope.md`; independent verification: `trace/ttcs/results/step38_ttcs01_verifier1_integration.md`, `step38_ttcs01_verifier2_integration.md`.

### 3.6 The monopole family on arbitrary metrics: amplitude, Nijenhuis and Weyl forms; affine exhaustion at LeBrun's threshold; the common mode — Proved identities; tariff open (Steps 39–40)

*Quantifiers.* Fixed Spin\(^c\) structures \(a_\epsilon=c+\sum\epsilon_iE_i\); for \(b^+\ge2\), chamber-independent nonzero invariants give unperturbed solutions for every metric (LeBrun's limiting argument); if \(A-k>0\) all solutions are irreducible; apply to the scalar \(-4\) Yamabe representative (\(P(g)\ge P(\hat g)\)); benchmark \(8\pi^2Q\) uses simple type; handles need the higher-type supplier. Saving \(\mathfrak S=8\pi^2Q-P\), Walsh part \(\mathcal W\ge0\), \(M=W^+-W_0\), \(x=M(n,n)\).

*Amplitude form (Step 39).* \(\mathfrak S=\mathbb E\int m(\rho)-8\mathbb E\|\zeta\|^2-4\mathbb E\|M\|^2-\mathcal W\), \(m=(2-\rho)(-\rho^3+10\rho^2-2\rho-4)/6\); positive only on \(0.7758<\rho<2\), \(m_{\max}=1.01555\). Hence \(P/(8\pi^2k)\to c<1\) forces \(\mathbb E\int(2-\rho)\ge2\pi^2(1-c)k-o(k)\).

*Lemma 1 (Step 40).* The Dirac equation fixes the Lee (\(\mathcal W_4\)) component of the rotation of the monopole almost-complex structure, \(\rho|v_4|^2=\frac12|a+J'b|^2\) (\(a=d\sqrt\rho\), \(b=\sqrt\rho\beta\)), and does not see the Nijenhuis (\(\mathcal W_2\)) component (\(\ker\) Clifford contraction \(=\mathcal W_2\), \(cc^*=2\)).

*Theorem N (exact).* \(\mathfrak S=\frac12\mathbb E\int\rho^2|\nabla n|^2_{\mathcal W_2}-\mathbb E\int\frac{(2-\rho)^2(2+2\rho-\rho^2)}6-\mathbb E\int\rho(|a|^2+5|b|^2-2\langle a,J'b\rangle)-4\mathbb E\|M\|^2-\mathcal W\). Corollaries: Hermitian tariff \(P\ge8\pi^2Q\) for scalar \(-4\) metrics admitting a simultaneous integrable choice; near-minimizers with ratio \(c<1\) have \(\liminf k^{-1}\mathbb E\int\rho^2|\nabla n|^2_{\mathcal W_2}\ge16\pi^2(1-c)\) (\(\ge0.684914\) per class for a closed replica of the certified cell).

*Theorem W (exact).* \(\mathfrak S=\mathbb E\int[\rho^2x-4|M|^2]+\mathbb E\int\frac{(2-\rho)(\rho-1)(3\rho+2)}3-4\mathbb E\|\zeta\|^2-\mathcal W\), using \(|d\psi|^2=2|\operatorname{Im}\zeta|^2\). Saving is Weyl-type (rise of \(W^+(n,n)\) above \(-\rho^2/6\)) plus volume-type shallow depletion.

*Theorem E (affine pointwise exhaustion).* Constant affine combinations of these forms with \(P=4W_++4V/3-8\pi^2(A-k)\), \(|W^+|^2=\rho^4/24-\rho^2x/2+|M|^2\), \(|M|^2\ge\frac32x^2\) give \(P\ge8\pi^2[k-(1-t)A]+\mathbb E\int g_{t,\lambda}\) with \(g_{2/3,2/3}=-\frac2{243}(2\rho-3)^2(\rho^2-24\rho-18)\ge0\) (LeBrun's \(C_+\ge2A/3\)) and \(\max_\lambda g_{t,\lambda}(3/2)=-\frac34(3t-2)\): nothing beyond LeBrun; contact at \(\rho=3/2\), not at KE.

*Formal common mode.* Constant \(\rho=r\), \(\zeta=0\), \(d\psi=0\) (almost-Kähler, all \(E_i\) ASD-harmonic, null periods) gives \(P/(8\pi^2)=k-A\beta(r)\), \(\beta=16/r-5-12/r^2\); \(r=2-k/A\) gives \(P=o(k)\) with uniform torsion \(|\nabla J|^2\approx2k/A\). Thus the exact identities are consistent with \(c\to0\). **Step-42 correction:** the exact mode is topologically excluded for \(b^+\ge2\) (Lemma T of §3.7: a nowhere-zero self-dual harmonic form has positive period on every exceptional class); it is the \(\alpha=0\) equality case of Theorem AKΓ, with \(\beta(r)=2\theta-3\theta^2\), \(\theta=h/(2-h)\). Approximate modes (tiny positive exceptional areas, or thin zero sets of the harmonic part) are not excluded, so the obstruction must still be a linear coercivity of diffuse torsion (§3.7, Proposition G).

Paths: `workspace/notes/step40_nijenhuis_form_and_pointwise_exhaustion.md`; `workspace/scripts/step40_nijenhuis_tariff_check.py`; `workspace/data/step40_nijenhuis_tariff_check.json`; verification `trace/ttcs/results/step40_ttcs01_verifier1_integration.md`; mechanisms `trace/ttcs/results/step40_ttcs01_generator1_integration.md`; Step 39: `workspace/scripts/step39_amplitude_band_and_curvature_channels.py`, `trace/ttcs/results/step39_ttcs01_verifier{1,2}_integration.md`.

### 3.7 Blindness theorem, Taubes period lemma, almost-Kähler torsion profile, and the Goldberg reduction — Proved (Step 42); coercive estimate open

*Setting.* \(M=X\#k\overline{\mathbb{CP}}^2\), \(X\) minimal, \(b^+(X)\ge2\), basic classes exactly \(\pm K_X\) modulo torsion (hypothesis), \(A=K_X^2\), \(0<k<A/3\). In this range with \(b^+\ge2\) simple type, nonzero invariants plus \(A-k>0\) give irreducible unperturbed solutions of every sign class for every metric; \(b^+=1\) keeps its chamber input.

*Theorem B (blindness of the self-dual sign-family data; Step 38).* For one sign flip at \(E_i\), the relative curvature \(h=(f_\epsilon-f_{\epsilon^i})/2\) satisfies \(\|h^-\|^2-\|h^+\|^2=4\pi^2\); every self-dual quantity of the family (amplitudes, \(\psi_\epsilon\), Walsh self-dual energy) sees only \(h^+\), which may vanish, and the forced zero of \(u\) unwinds through \(w\) (\(S^3\)-valued pair, \(\pi_1(S^3)=0\)). Consequently no estimate built only from monopole amplitudes and self-dual curvature of the sign family yields a \(k\)-dependent excess; together with Theorem E this closes the Seiberg–Witten-identity route as a source of the tariff.

*Lemma T (Taubes period lemma).* For any symplectic \(\omega\) on \(M\) (e.g. a nowhere-zero self-dual harmonic form of any metric), \(K_\omega\cdot\omega=|K_X\cdot\omega|+\sum_i|E_i\cdot\omega|\) with every \(|E_i\cdot\omega|>0\) (Taubes SW⇒Gr plus the blow-up formula). Corollary: a self-dual harmonic form with a null exceptional period vanishes somewhere. The symmetric perpendicular cell's canonical closed form has null period and vanishes along the bolt (A01 profile: \(|\omega|_g=\sqrt2u^2\), \(u=0.0072\) at the first bolt sample); it is not an almost-Kähler structure. Lemma T packages a standard argument (LeBrun 2001, Prop. 3.2); new is its use against the common mode.

*Theorem AKΓ.* For every almost-Kähler \((g,\omega)\) on \(M\), with \(\ell=8\pi K_\omega\cdot[\omega]\), \(\theta=\ell^{-1}\int|\nabla\omega|^2\), \(\alpha=\sum|E_i\cdot\omega|/\sqrt{2AV}>0\), \(\eta=|K_X\cdot\omega|/\sqrt{2AV}\):
\[
C_+\ge\frac{\ell^2}{128\pi^2V}(3\theta^2-2\theta+1)=A(\eta+\alpha)^2(3\theta^2-2\theta+1).
\]
(Pointwise \(|W^+|^2\ge\frac32W^+(u,u)^2\), \(W^+(u,u)=s/6+|\nabla\omega|^2/4\); Blair's \(\int(s+s^*)=-8\pi K_\omega\cdot\omega\) fixes the means; Jensen; Lemma T.) \(\eta\ge1\) is **not** automatic for \(b^+\ge2\) (verified counter-mechanism \(\omega_0+t\operatorname{Re}\Omega\)); it holds under the Lorentzian hypothesis (H\(_L\)), e.g. in the Kähler case, where then \(P/(8\pi^2)>k-A(2\theta-3\theta^2)\). \(\theta=0\): Kähler tariff strengthened by areas. \(\min\Gamma=2/3\) at \(\theta=1/3\) (\(s^*=s/2\)): LeBrun's constant. Equality iff \(W^+=\mathrm{diag}(\lambda,-\lambda/2,-\lambda/2)\) along ω and \(s,s^*\) separately constant (ω lowest only for \(\theta<1/2\)); the Step-40 common mode is the formal \(\eta=1,\alpha=0\) member. Under (H\(_L\)) the saving is \(\le2A\theta\): linear in torsion.

*Proposition G (reduction).* Under (H\(_L\)) (or directly assuming \(p\ge k-2A\theta\)), if \(P\ge8\pi^2\kappa A\theta\) on a class of almost-Kähler metrics, then \(P\ge8\pi^2k\,\kappa/(\kappa+2)\) there. Monopole form (unconditional beyond §3.6 hypotheses): if \(P\ge\kappa\mathcal N\), \(\mathcal N=\frac12\mathbb E\int\rho^2|\nabla n|^2_{\mathcal W_2}\), then \(P\ge8\pi^2k\,\kappa/(1+\kappa)\); conversely \(P/(8\pi^2k)\to c\) forces \(\mathcal N/P\ge(1-c)/c\) (one-way). The tariff in the open range is thus implied by a linear negative-scalar Goldberg estimate. Its \(P=0\) endpoint on the eigenvector class is Armstrong's theorem; the correctly posed coercive target is a near-saturated quantitative Armstrong estimate \(P/(8\pi^2)+C\mathfrak d_{AK}\ge cA\theta\) with period-loss control, or the quartic variant \(\int|\mathrm{Ric}^\circ|^2\ge c\int|\nabla\omega|^4\) on \(W^+(\omega)^\perp=0\).

*Superseded.* The Step-39/41 co-rotation dichotomy: co-rotation is automatic in almost-Kähler geometry; misalignment is quadratic in torsion and the saving linear.

Paths: `workspace/notes/step42_ak_torsion_profile_taubes_goldberg.md`; `workspace/scripts/step42_ak_torsion_profile.py`; `workspace/data/step42_ak_torsion_profile.json`; verification `trace/ttcs/results/step42_ttcs01_verifier1_integration.md`.

### 3.8 The corrected \(W_0\), divergence symbol, Cotton pairing and quadratic-law reduction — exact local identities; global estimate open (Steps 41–43)

For one monopole field, \(W_0=aK_n\), \(a=\rho^2/4\), \(K_n=I/3-n\otimes n\). Hence
\[
\operatorname{spec}(W_0)=(-\rho^2/6,\rho^2/12,\rho^2/12),\qquad |W_0|^2=\rho^4/24.
\]
For unit \(n,m\), \(|aK_n-aK_m|^2=2a^2(1-\langle n,m\rangle^2)=\rho^4\sin^2\theta/8\), and
\[
\min_{b\ge0}|aK_n-bK_m|^2=
\begin{cases}
\frac{a^2}{2}(1-c^2)(1+3c^2),&c^2\ge1/3,\\
\frac{2a^2}{3},&c^2\le1/3,
\end{cases}\quad c=\langle n,m\rangle.
\]
Thus Kähler-type co-rotation is forced quantitatively only where \(\rho\) is bounded below. AAD's proper three-symmetric almost-Kähler model proves that this algebraic structure does not force integrability; the differential slack is the Cotton source \(\delta W^+=C^+=\nabla\operatorname{Ric}^\circ\).

**Proposition 43.B (exact divergence symbol).** For a smooth unit \(n\in\Lambda^+\),
\[
\delta W_0=\mathcal A(da)+a\mathcal T(\nabla n).
\]
If \(d(\sqrt2n)=0\) (the almost-Kähler first-jet condition), then in the standard induced tensor norm
\[
|\delta W_0|^2=\frac13|da|^2+\frac{a^2}{2}|\nabla n|^2,
\]
and the amplitude and torsion images are orthogonal. The torsion map has squared singular value \(1/2\), singular value \(1/\sqrt2\). For a general monopole direction the Dirac-controlled Lee component adds \(dn\) and amplitude--Lee cross terms; the restricted formula cannot be applied to the full jet without Theorem N's \(\zeta\) control.

**Proposition 43.C (exact Cotton pairing).** On a closed constant-scalar almost-Kähler four-manifold, write \(\omega=\sqrt2n\), assume \(a\ge a_0>0\), put \(E=W^+-W_0\), \(U=\mathcal T(\nabla n)\). Then
\[
\frac12\int a|\nabla n|^2=\int\langle\operatorname{Ric}^\circ,\mathcal C^*U\rangle-\int\langle E,\delta^*U\rangle,
\]
so
\[
\frac{a_0}{2}\int|\nabla n|^2\le\sqrt P\,\|\mathcal C^*U\|_2+\|E\|_2\,\|\delta^*U\|_2.
\]
No estimate of the adjoint norms by \(C\|\operatorname{Rm}\|_2\) is currently proved: they contain \(\nabla^2n\) and \((\nabla n)^2\). A localized monopole version additionally needs zero-set/band cutoffs, Lee torsion, amplitude-gradient products and control of \(E\). Hence the hoped-for quadratic transport law is conditional, not a theorem.

**Conditional optimization.** With total sign-averaged \(W_2\) energy \(R=\mathbb E\int|\nabla n|_{W_2}^2\), Theorem N gives exactly \(P\ge8\pi^2k-2R\). If an independent theorem gives \(P\ge R^2/(\Lambda A)\), then
\[
P\ge\bigl(\sqrt{\Lambda A+8\pi^2k}-\sqrt{\Lambda A}\bigr)^2
=\frac{16\pi^4k^2}{\Lambda A}+O(k^3/A^2).
\]
This would give a positive fixed-topology gap of order \(k^2/A\) without a uniform per-class tariff, but it is conditional on the missing transport/error estimate. Perturbative linear coercivity near a negative Kähler--Einstein host remains a separate spectral theorem; cover-uniformity is open.

**Kirchberg--Sekigawa resisting term.** In Kirchberg's norms, for scalar \(S=-4\),
\[
Q(J)+\int\bigl(|\widetilde R|^2+4|\operatorname{Ric}_\star^-|^2-2|\nabla J|^2+|\nabla J|^4\bigr)=0,
\]
with \(Q(J)=2\int\langle\varphi,\psi\rangle\) an explicit torsion--\(\nabla\operatorname{Ric}\) (Cotton) pairing. The adverse \(-2|\nabla J|^2\) and uncontrolled \(Q(J)\) are exactly why the negative-scalar formula does not give nonperturbative linear Goldberg coercivity from \(P\). AAD's proper three-symmetric local test has \(s=-3/4\), \(\kappa=3/4\), \(|\nabla\Omega|^2=1\), \(|\operatorname{Ric}^\circ|^2=9/64\); it allows Kähler-type algebraic curvature with nonzero torsion and caps any pointwise quartic constant at \(9/64\) in those conventions, but is noncompact/local.

Paths: `workspace/notes/step43_w0_cotton_quadratic_law_and_debts.md`; `workspace/scripts/step43_w0_divergence_symbol.py`; `workspace/data/step43_w0_divergence_symbol.json`; `workspace/scripts/step43_proper3symmetric_test.py`; `workspace/data/step43_proper3symmetric_test.json`; verification `trace/ttcs/results/step43_ttcs01_verifier1_integration.md`.

## 4. Curvature-sensitive marked blow-up cells

For an exact-complex-hyperbolic-collar marked cell,
\[
P_{\rm cell}-8\pi^2=4\Delta W_++\frac1{12}\Delta S.
\]
This same-metric identity is the reason a Weyl-energy improvement alone does not control the direct defect.

### 4.1 First-order response for a general bulk — Proved (Theorem F, Step 20) as an upper construction

The aligned Kähler seed obeys
\[
\frac{P_K}{8\pi^2}=1+6\kappa x_0+9(\kappa^2+X^{-2})x_0^2+O_X(x_0^3).
\]
**Theorem F.** Let \((M,g)\) be closed and oriented, \(p\in M\), and \(\zeta\in\Lambda^+_p\) a unit form. Glue the Burns metric \(\delta+x_0h\), whose exceptional curve has area \(\pi x_0\), into \(g\)-normal coordinates with cutoff radius \(x_0^{1/5}\). This gives metrics on \(M\#\overline{\mathbb{CP}}^2\) with
\[
P(\hat g_{x_0})=P(g)+8\pi^2\big(1-x_0\mathbf R^+_p(\zeta,\zeta)\big)+O(x_0^{6/5}),
\]
and the same law holds for \(J\) when \(g\) is Einstein. The proof rests on two facts: the Burns tail is pointwise linearly self-dual-flat and scalar-flat, and its exact cut-annulus transgression is \(\Phi^{++}=\pi^2\,\hat\zeta\hat\zeta^T\), \(\Phi^{--}=\frac{\pi^2}3I\), \(\Phi^{+-}=0\) (exact sympy on \(S^3\)). The scalar flux \(4\pi^2x_0=4\pi\,\mathrm{area}(E)\) reproduces the Kähler identity \(\int s=4\pi c_1\cdot[\omega]\). Theorem F recovers the signed complex-space-form slopes \(+6,0,-6\). At a negative Kähler–Einstein point, \(\ker\mathbf R^+=\omega^\perp\) is first-order free and coincides with the directions allowed by the first \(A_1\) desingularization obstruction \(\mathbf R^+\zeta=0\). On real hyperbolic bulk \(\mathbf R^+=\frac s{12}I<0\), so every direction costs at first order. The matching lower bound for the cell infimum is open.

Primary paths: `workspace/notes/step20_burns_response_and_neck_quantization.md`; `workspace/scripts/burns_transgression_flux.py`; `workspace/data/burns_transgression_flux.json`; `workspace/scripts/o11_general_bulk_cell.py`.

**CR pinning (Lemma P, Step 25; independently verified in Step 26) — Proved.** For every diagonal metric, the Rossi variable \(\widetilde\Phi=q+\frac14(y_g-y_h)-\zeta\sinh q\) obeys exactly \(\widetilde\Phi'=F-\frac14(\mathrm{Ric}^\circ_{gg}-\mathrm{Ric}^\circ_{hh})\), hence \(|\Delta\widetilde\Phi-\int F|\le(\widehat P/2)^{1/2}(\int dt/W)^{1/2}\). In an ACH block, and only with that scope, \(F=\zeta^2G\) with bounded \(G\). Changing the Rossi squashing at radius \(T\) costs at least \(\frac12e^{4T}(\Delta\log\rho)^2\) (units \(8\pi^2\)), and the constant \(\frac12\) is the exact linearized optimum; the null-line value function and Lemma P measure the same charge and are not additive.

**Standard-CR truncation (Theorem T, Step 26) — Proved for diagonal scalar-\(-24\) ends in one small ACH block.** The CH linear rates are \(2,0,-2,-4,-6,-8\). The \(-2\) mode is exactly radial phase, while the physical Einstein modes begin at \(-4\); the \(-8\) mode is a forced constraint response for non-Einstein scalar-normalized ends. After matching radial phase, finite \(P\) and \(\widetilde\Phi\to0\) give transverse deviation \(o(e^{-2t})\), enough to splice on a unit annulus with added squared Einstein residual tending to zero. Hence a complete standard-CR diagonal Einstein ACH filling implies \(p^{\rm diag}_{1,0}=0\), while the converse needs attainment/compactness.

**Euler-flux collapse separation (Step 26) — Proved for diagonal annuli.** For \(\mathfrak b=W(\sum_i y_iK^{(3)}_{jk}-y_1y_2y_3)\), exact Cartan computation gives \(\widehat P(C)=\Delta\mathfrak b+\int|W|^2/(4\pi^2)+\int s^2/(96\pi^2)\). On CH, \(\mathfrak b=2-6\sinh^4t\). Arb evaluation on all 40 validated Theorem-E endpoint boxes gives \(\mathfrak b\in[-64533.462,-64275.416]\) once \(\widetilde\Phi\approx0.7845\). Product and ALF Berger necks have \(\mathfrak b\to0\), so a post-developed-Rossi connector to such a neck costs far above the certified cell value. High-shear scale-invariant connectors and resets before the developed ACH regime remain open.

Theorem E is therefore not a bounded-cost limit of exact-CH diagonal cells whose correction remains in the ACH block, nor can it first develop to the validated orbit and then pass through an ordinary product/ALF neck. The conditional structure Theorem D now has a proved truncation direction; its remaining inputs are compactness, high-shear/interior-collapse and large-bolt control, and validated no-return dynamics. Paths: `workspace/notes/step25_diagonal_cell_compactness_and_CR_pinning.md`; `workspace/notes/step26_truncation_flux_and_branch_completeness.md`; `workspace/scripts/cr_pinning_check.py`; `workspace/scripts/squash_escape_cost.py`; `workspace/scripts/verify_euler_flux_identity.py`; `workspace/scripts/ach_euler_flux.py`.

**Chiral transgressions (Theorem X, Step 27) — Proved for diagonal annuli (exact symbolic).** There is an explicit signature transgression \(\mathfrak s\) with \(\mathfrak s'=\frac12W(B_+-B_-)\). With \(\mathfrak b_\pm=\mathfrak b\mp\mathfrak s\),
\(\widehat P(C)=\Delta\mathfrak b_\pm+\frac1{2\pi^2}\int_C|W^\pm|^2+\frac1{96\pi^2}\int_Cs^2\).

The charges \((\mathfrak b_+,\mathfrak b_-)\) are:
- smooth centre: \((2,2)\);
- \(O(-1)\) bolt in the blow-up orientation: \((1,7)\);
- biaxial or controlled near-biaxial Hopf-collapsed Berger orbit in the Taub–NUT/blow-up chirality: \((-2,2)\), since the Euler flux vanishes on collapse while \(\mathfrak s\) keeps an adiabatic charge; the opposite four-dimensional orientation gives \((2,-2)\), and unrestricted anisotropic collapsed jets have additional shear terms;
- CH orbit: \((2-9\sinh^4t,\ 2-3\sinh^4t)\).

Consequences:
- \(\widehat P[0,t]\ge\mathfrak b_+(t)-1\). This is the sharp, Burns-extremal replacement of Lemma Q′: Burns has \(W^+=s=0\) and \(\widehat P=2-1\).
- A cell with \(\widehat P<1\) has no orbit close to round.
- Decollapse from a collapsed neck to a CH-like orbit of radius \(\tau\) costs at least \(4-9\sinh^4\tau\).
- Taub-bolt is a regular zero-cost core in the blow-up orientation, with \(\frac1{2\pi^2}\int|W^\pm|^2=3,5\).

Step 28 independently verified the formula, signs, orientation and model balances. The normalized transgression is \(\mathfrak s=S_0-6\); raw `chiral_flux.json` fields use \(S_0\), so its `bA,bB` require shifts \(+6,-6\). The Hitchin–Thorpe prefactor is \(4\pi^2(2\chi\pm3\tau)\).

Files: `notes/step27_chiral_transgression_and_small_bolt.md`, `scripts/chiral_flux_identity.py`, `scripts/chiral_flux_models.py`; independent reading `trace/ttcs/results/step28_ttcs01_verifier1_integration.md`.

**Small-bolt Einstein structure (Step 27) — Matched-asymptotic mechanism, numerically confirmed.** As \(b\to0\) the perpendicular ACH separatrix is a Taub-bolt core followed by a collapsed \(\Lambda\)-Taub-NUT neck with circle \(\simeq4n\cosh\sqrt2t\), \(n=b/(2\sqrt3)\), and then saturation at scale one. The triaxial mode grows at rate \(4/\varepsilon\) in the neck, which predicts \(\log(1/d_*)\sim\pi\sqrt{3/2}/b=3.8476/b\); the fit gives \(3.854\). The Rossi parameter behaves as \(\rho\simeq0.8/b\to\infty\). A rigorous matching proof remains open.

**Scale-free saturation problem (Step 28) — Exact reduction; value open.** With \(a_f=re^{2\beta/3}\), \(a_g=re^{-\beta/3+q/2}\), \(a_h=re^{-\beta/3-q/2}\), \(d\tau=dt/r\), and \((\bar H,\bar E,\bar D)=r^2(H,E,D)\), the full diagonal dynamics and action become independent of the bolt scale:
\[
\widehat P=\int\left(3\bar H^2/16+\bar E^2/6+\bar D^2/8\right)d\tau.
\]
The collapsed branch is the control value from the Taub-bolt/\(\Lambda\)-Taub-NUT entry ray to the standard-CR end. All three controls are essential. Path: `notes/step28_saturation_control_and_revised_diagonal_structure.md`.

**Collapsed saturation value (Step 29) — Terminal reduction proved; value \(=4\) numerically.**

*Terminal reduction (Lemma S).* An exact-CH terminal jet followed by the homothetic exact CH collar is a legitimate exact-collar competitor. Two facts make this work: \(\widehat P\) is scale invariant, and zero-control flow is Einstein by the contracted Bianchi identity. By Theorem T this terminal has the same infimum as the standard-CR stable set, so no stable-manifold parameterization is needed. Step 28's rejection of these endpoints came from its checker, which forced the compact section \(\zeta=1/(a_ga_h)=10^{-2}\) and thereby rescaled CH jets.

*Numerical value.* The minimal action rises monotonically along the entry ray:

| \(\varepsilon\) | 1/2 | 1/4 | 1/8 | 1/16 | 1/32 | 1/64 | 1/128 | 1/256 |
|---|---|---|---|---|---|---|---|---|
| minimal action | 2.33 | 3.38 | 3.75 | 3.89 | 3.95 | 3.976 | 3.988 | 3.994 |

Independent actual-metric evaluations of the same runs give 2.52, 3.48, 3.82, 3.93, 3.98 at \(\varepsilon=1/2\) to \(1/32\), 3.98841 at \(1/128\), and 3.9963 at \(1/256\). The values track the chiral gap \(2-\mathfrak b_+(\text{entry})\to4\).

*Structure of the minimizer.* For small \(\varepsilon\) the minimizer rises with \(W^+\approx0\) and \(s\approx0\), an ASD scalar-flat decollapse, to an exactly round orbit with \(\mathfrak b_+=2\). It then follows a CH ball at zero cost. The collapsed branch is therefore an ALF analogue of the Burns bubble. Burns pays \(2-1=1\); the collapsed route pays \(2-(-2)=4\).

*Opening radius.* Opening late is priced at least exponentially, roughly like \(e^{4\tau}\) (Lemma P): at \(\varepsilon=1/16\), windows starting at \(\tau=2.5,3,3.5,4\) cost about 4.1, 7.9, 34, 207.

*What remains.* The diagonal transgression itself now proves the first branch estimate in a precise finite-charge normalized-jet class. If a collapsed normalized first-jet family obeys
\[
x=Xz^3+o(z^3),\qquad p=Pz+o(z),\qquad \chi=Cz+o(z),\qquad \eta=Nz+o(z),
\]
then exact symbolic evaluation gives
\[
\mathfrak b_+^{\rm end}=-2-(C+4X)^2,
\]
so every annulus joining it to a round orbit satisfies the **Q″ inequality**
\[
\liminf\widehat P\ge2-\mathfrak b_+^{\rm end}=4+(C+4X)^2.
\]
Thus anisotropy in this finite-charge normalized-jet class cannot lower the Berger-to-round payment. The opposite charge is \(\mathfrak b_-^{\rm end}=2+(C-4X)^2\); \(P,N\) cancel from both limits. This class is not automatically bounded-curvature geometry: fixed-base-scale bounded orbit/mixed curvature imposes stronger decay, such as \(x=O(z^6)\), \(\chi=O(z^4)\), and radial second-derivative control, which force \(X,C\to0\). Burns and Taub-bolt/ALF decollapse are priced by the same rule: round charge minus bubble-end charge, respectively \(2-1=1\) and \(2-(-2)=4\). What remains for small-bolt matching is to prove that regular bolt trajectories enter a finite-charge or bounded-geometry class, or charge the production of an uncontrolled high-shear first jet.

**Fibre/base pinning (Step 30) — Proved identity.** Put \(v=y_f-(y_g+y_h)/2\) and
\[
\widetilde B=\log\frac{\kappa}{\sqrt{1+\zeta}}+\frac14(v-\kappa^{-1}).
\]
This vanishes on every CH orbit and obeys exactly
\[
\widetilde B'=F_\beta-\frac14\left(\operatorname{Ric}_{ff}-\frac{\operatorname{Ric}_{gg}+\operatorname{Ric}_{hh}}2\right),
\]
hence
\[
\left|\Delta\widetilde B-\int F_\beta dt\right|
\le\sqrt{\frac{3\widehat P}{8}}\left(\int\frac{dt}{W}\right)^{1/2}.
\]
On an exact CH tail, \(\int_T^\infty W^{-1}dt=\frac1{2\sinh^2T}-\frac12\log(1+\sinh^{-2}T)\), giving an exponential late-opening payment once the effective mismatch is known. For a general connector this CH denominator requires a separate comparison with its actual \(\int W_g^{-1}dt\). With the CH denominator, overlap with the early-opening bound at \(T=.70\) needs mismatch at least \(0.370125\ldots\); volume comparison and free-drift control on the saturation region remain missing.

An enlarged-entry numerical test confirms why first-jet control matters. At \(\varepsilon=1/16\), imposing a fixed raw \(\Delta\eta=-8\) produces an explicit collocation path of cost \(0.5454\) and independently reconstructed metric cost \(0.5745\), below the certified cell; but this violates the finite-charge scaling above and at \(\varepsilon=1/32\) the same raw perturbation costs \(2.9425\). It is not a regular bolt construction. Its entry charge is already \(1.45194\), so the omitted bolt-to-entry prefix costs at least \(0.45194\); prefix plus reconstructed connector is at least \(1.0264\). It identifies uncontrolled contact-slot shear as the remaining high-shear escape mechanism rather than refuting Q″. Paths: `notes/step30_Qdoubleprime_beta_pinning_and_anisotropic_collapse.md`, `scripts/collapse_chiral_charge_limit.py`, `scripts/beta_pinning_identity.py`, `scripts/saturation_anisotropic_scan.py`, `data/saturation_control/step30_anisotropic_summary.json`.

**Theorem D (frozen statement, Step 29).**

*Setting.* Let \(p^{\rm diag}_{1,0}\) be the infimum of \(\widehat P\) over diagonal Bianchi-IX metrics on \(O(-1)\) with an exact CH collar. By Theorem C and the Yamabe solution, this equals the scalar-\(-24\) standard-CR value.

*(i) Einstein \(\Rightarrow\) zero — proved, unconditional.* If a complete diagonal Einstein ACH metric on \(O(-1)\) with standard CR infinity exists, then \(p^{\rm diag}_{1,0}=0\). This is Theorem T.

*(ii) Compactness — conditional on four branch inequalities.* Let \(g_j\) be a minimizing sequence. On bounded-shape, bounded-\(W\) regions the chiral identities bound the weighted curvature, and the state equations are affine in the Ricci controls. Hence a subsequence converges to a complete minimizer with standard CR infinity, unless one of four mechanisms occurs. In each case it suffices to show that the mechanism costs more than \(\min(p^{\rm diag}_{1,0}+\delta,\ 0.99585)\).

1. *Small-bolt collapse/saturation.* Finite-charge normalized entries are now priced rigorously by Q″ at \(4+(C+4X)^2\), while genuinely bounded-geometry Berger entries have \(X,C\to0\) and price \(4-o(1)\). The remaining work is the matched-entry theorem showing regular small-bolt sequences satisfy one of these asymptotic regimes; if they do not, the escaping first-jet shear joins mechanism 3.
2. *Large-bolt escape.* Status: open.
3. *Interior high-shear/volume-bounce connector.* The exact formula \(\mathfrak b_+^{\rm end}=-2-(C+4X)^2\) handles the finite-charge normalized-jet class, and bounded-geometry Berger collapse is a stronger subcase. Uncontrolled raw contact shear \(\eta\) can sharply lower finite-scale connector cost and is the remaining escape mechanism; it must either be excluded by regular bolt/interior matching or charged before the selected section.
4. *Conformal-infinity face escape.* Status: the face flow from \(E(q)\) has been computed and shows no return (Step 25, floating); a validated no-return proof is open.

Scale-separated ALE concentration (\(\mathfrak b_+\)), large-volume nonstandard-CR escape (Lemma P) and post-Rossi product/ALF collapse (Euler flux) are already excluded.

*Step-31 revision of (ii) — three inputs.* The chiral identities hold pointwise in \(t\), which yields the charge-variation bound Lemma V:
\[
\widehat P\ge\int\max\{0,\mathfrak b_+',\mathfrak b_-'\}\,dt,
\qquad
\widehat P\ge\sup_t\max\{\mathfrak b_+(t)-1,\ \mathfrak b_-(t)-7\}.
\]
Here \(\mathfrak b_-=\sum w_i^2-\prod w_i-2\) with \(w_i=a_i'+\gamma_i\), and the bolt charges are \((1,7)\). Two consequences follow. Any round passage costs at least \(1-o(1)\). The raw \(\Delta\eta=-8\) entry has \(\mathfrak b_-=8.5496\), so its bolt prefix alone costs at least \(1.5496\).

Mechanisms 1 and 3 therefore reduce to **(N) non-round late opening**: after a collapsed section, \(\mathfrak b_+\) must stay below \(-1\) until CH shape is reached at \(\tau>0.70\). Constrained collocation (`SAT_BPMAX`) gives non-round values \(6.48\) (cap \(-1\), \(\varepsilon=1/16\), two warm starts; \(N=80\): \(6.44\)), \(5.37\), \(6.55\) and \(6.62\) at \(\varepsilon=1/4,1/32,1/64\), and \(4.03,4.81,5.50,7.89,11.87\) for caps \(1,0,-.5,-1.5,-2.5\). These costs are paid mainly in the \(D\) channel and not by charges.

Lemma N (independently verified, Step 32, and by S1003A01) shows that in the scalar-normalized class \(s\equiv-24\) the \(H\) channel is the Hamiltonian-constraint residual \(\mathcal C=\sigma_2(y)-6-R^{(3)}/2\), with \(\widehat P\supset\int W\mathcal C^2/3\). The normalization is not a literal preservation of the exact CH collar: the exact-ended diagonal infimum equals the scalar-\(-24\) infimum over metrics asymptotic to the marked standard CH end at rate \(>4\), followed by Theorem-T truncation; the bolt radius becomes \(u(0)b\). Lemma N also gives \(\mathcal C'=-2S\mathcal C-\sum(S-y_i)e_i\) and \(S'=18-S^2+R^{(3)}+\mathcal C\). Lemma W (last-crossing proof, repaired Step 33) uses these identities to supply the \(\int W^{-1}\) volume comparison wherever \(R^{(3)}\ge-\rho_0\), \(\rho_0<18\). The constrained collocation values above are feasible paths returned by a local optimizer, not lower estimates.

*Steps 33–34 additions.* Lemma V is exhausted as a static tool for (N): in scale-free jet coordinates \(\mathfrak b_+=2-|u|^2-\prod u\) depends on \(u=a'-\gamma\) only, an explicit path from the collapsed jet \((1,1,-2)\) to the CH jet \((3\sinh^2\tau,0,0)\) makes \(\mathfrak b_+\) monotone, and joint minimization finds triaxial never-round paths with \(\int\max(0,d\mathfrak b_+,d\mathfrak b_-)\approx0.02\) (Lemma Z). The exact control minimization goes further: for \(V=\mathfrak b_++\phi(q,\eta)\), SymPy gives \(\sup_{\bar H,\bar E,\bar D}(\dot{\mathfrak b}_+-L)\equiv0\), so the HJ condition is \(\eta\phi_q+K\phi_\eta+2\phi_\eta^2\le0\). A sampled convex search on the cap-\(-1\) swap trajectories gives zero gain for every quadratic \(\phi(q,\eta)\); \(K\) changes sign from about \(-3.34\) to \(4.46\). Thus decorating the already exact chiral calibration by \((q,\eta)\) does not expose the missing cost. The stronger next structure is S1003A01's exact canonical almost-Kähler identity
\[
\widehat P-1=12H+6G+\tfrac32Q_\delta+\tfrac12Q_A-\tfrac32N+\Sigma,
\]
whose only negative term is Nijenhuis energy and whose transport/Hardy estimate makes the far zone nonnegative. An independent check confirms the coefficients but also shows that the certified subunit cells realize a genuine negative compact middle-zone mode; this route should determine a sharp subunit lower value and near-extremal mode (or a unit bound only under additional coercive hypotheses), not contradict the certified metrics. The unresolved inequality is the lowest coupled compact action for the forced bolt Nijenhuis charge, conformal factor, and \(W_3^+\) transport. Paths: `notes/step34_characteristic_constraint_calculus_and_N_probe.md`, `scripts/hj_symbolic_reduction.py`, `data/saturation_control/hj_qeta_probe.json`, and `Sessions/S1003A01/workspace/notes/step28_AK_gap_identity_nijenhuis_transport.md`.

*Step-35 addition (calibration and leaves).* Since \(\dot{\mathfrak b}_+\) is affine in the controls and \(\sup_c(\dot{\mathfrak b}_+-L)\equiv0\), one has exactly \(L(c)-\dot{\mathfrak b}_+=L(c-c^*)\), so \(\widehat P=\Delta\mathfrak b_++\int L(c-c^*)\) with positive-definite weight (no kernel defect); calibrated curves are the ASD scalar-flat diagonal metrics (Burns yes; Taub-bolt and CH no). Calibrated leaves from the collapsed entry converge to the Euclidean round fixed point (transverse eigenvalues \(-2,-4\)); backward leaves from all CH jets stay in the invariant biaxial set \(\Sigma=\{q=\eta=0\}\) and blow up without approaching the collapsed set. The endpoints are therefore leaf-separated in the antisymmetric pair \((q,\eta)\), reachable only through \(\bar D\) — the structural origin of the \(D\)-dominance. The exact transverse block on \(\Sigma\) is attracting on 38% and saddle on 62% of sampled \(\Sigma\cap\{\mathfrak b_+\le-1\}\), so no frozen argument excludes a cheap connector: (N) lacks path weight, not kernel or separation. It is recorded as a numerical-margin input. The proposed route is to match the \(\mathfrak b_+\) calibration on the swap band with S1003A01's CH-renormalized \(B\) (\(B_{\rm bolt}=1,B_{\rm CH}=2\)) on the tail. Paths: `notes/step35_calibration_theorem_and_branch_classification.md`, `scripts/calibrated_flow_leaves.py`, `scripts/transverse_block.py`.

**(L) large bolt:** the Einstein separatrix has an exact face limit, with \(d/b\to0.90535\), \(\rho\sim1.345b\), and the Rossi offset \(\log b\) produced at \(W\asymp b^2\). Shadowing together with Lemma P therefore predicts cost \(\gtrsim b^2(\log b)^2\). **(F)** conformal-face escape is analysed on the same \(\zeta=0\) face. Path: `notes/step31_charge_variation_constraint_pinning_nonround_opening.md`.

*(iii) Zero \(\Rightarrow\) Einstein.* Under (ii), \(p^{\rm diag}_{1,0}\) is attained. If \(p^{\rm diag}_{1,0}=0\), the minimizer is an Einstein metric of this type. Hence
\[
p^{\rm diag}_{1,0}>0\iff \text{no standard-CR diagonal Einstein filling of } O(-1).
\]

*(iv) Expected route to positivity.* Positivity would follow from \(\rho\neq1\) along all Einstein separatrices. Floating fate maps give \(\rho\ge2.19\) on ACH1 and its mirror \(\rho\le1/2.19\) on ACH2 at the sampled \(b\in\{.14,.2,.35,.8,2,20\}\) (minimum near \(b=.8\)), with \(\rho\sim0.8/b\) as \(b\to0\). This requires interval fate enclosure and large/small-\(b\) asymptotics.

### 4.2 Kernel-direction neck response — Exact reduced calculation; general remainder open

The calibrated neck density is
\[
x_0^2\left[\frac{(v_s+2v-3)^2}{4}-6v\right],
\]
with minimum \(-18x_0^2\) at \(v=9/2\). The exact constant-mode expansion gives the common minimizer \((C_1,C_2,C_3)=(9/4,3/4,1/2)\) for \(P\) and \(J\), predicting
\[
\frac{P}{8\pi^2},\frac{J}{8\pi^2}
=1-9x_0^2\log(1/x_0)+O(x_0^2).
\]
The coefficient and cancellations are exact in the reduced family; a uniform error estimate for general bulk metrics remains open.

Primary paths: `workspace/scripts/o11_neck_density_sympy.py`; `workspace/scripts/o11_perp_logneck.py`; `workspace/data/o11logneck/`.

### 4.3 Explicit subthreshold cells — Certified

The exact-dyadic \(x_0=0.01, X=8\) cell satisfies
\[
P/(8\pi^2)=0.999108702733592648\ldots,
\qquad
J_6/(8\pi^2)=0.999116243135324311\ldots
\]
with pure-Arb enclosures and exact bolt/collar matching data. The stronger area-selected \(x_0=3/100, X=64\) cell satisfies
\[
P/(8\pi^2)\in[0.9958484075845568,0.9958484075911518],
\]
\[
J_6/(8\pi^2)\in[0.9958546908532724,0.9958546908569237].
\]
The authoritative Step-33 extension to \(X=128\), degree 20, has the sharpened exact-dyadic Arb enclosure
\[
P/(8\pi^2)\in[0.995662732753254329\ldots,0.995662732771114200\ldots],
\]
\[
J_6/(8\pi^2)\in[0.995670030344086466\ldots,0.995670030355130639\ldots].
\]
Thus the isolated blow-up cost can be strictly below \(8\pi^2\) in negative Kähler--Einstein bulk. The area/collar sweeps suggest a finite-radius preferred scale, but do not prove existence or uniqueness of a complete-cell minimizer.

Primary paths: `workspace/data/o11_strict_arb_x001_X8_256.json`; `workspace/notes/step11_subthreshold_perpendicular_cell.md`; `Sessions/S1003A01/workspace/data/perp_area/rigorous_x00.03_X64_d16.json`; `Sessions/S1003A01/workspace/data/step33/rigorous_x00.03_X128_d20_{P,J,S}_exact.json`.

## 5. Cell infima, handles, and balanced upper bounds

Let \(\mathfrak P_{k,\ell}\) and \(\mathfrak J_{k,\ell}\) denote infima over smooth marked cells of topology \(D\#k\overline{\mathbb{CP}}^{\,2}\#\ell(S^1\times S^3)\), exact CH on an outer collar, with radius allowed to vary.

### 5.1 Subadditivity and balanced specific energy — Proved at construction level

Disjoint placement gives subadditivity and therefore
\[
\gamma_{\rm bal}=
\lim_{n\to\infty}\frac{\mathfrak P_{8n,7n}}{72\pi^2n}
=\inf_n\frac{\mathfrak P_{8n,7n}}{72\pi^2n}.
\]
This does not identify \(\gamma_{\rm bal}\) with the unrestricted closed-manifold \(\alpha\)-coefficient.

### 5.2 Pure handles — Proved sharp infimum

\[
\mathfrak P_{0,\ell}=\mathfrak J_{0,\ell}=32\pi^2\ell.
\]
For \(\ell>0\), the value is approached by shrinking cores and is not attained by a fixed smooth cell. Mixed-cell nonadditivity remains open.

### 5.3 Balanced sequence — Proved existential upper construction

Residual-finite covers provide disjoint placements, exact-collar smoothing has arbitrarily small loss, and the certified \(x_0=3/100, X=128\) blow-up cell together with the pure-handle construction yields a suitably selected balanced family with
\[
\limsup \alpha(M_j)/h_j<3.9961512+\varepsilon.
\]
This is not a statement for every prescribed cover sequence and does not determine the sharp coefficient. The separated bookkeeping is \(28/9+(8/9)p_{1,0}\), not \(4p_{1,0}\).

## 6. A complete nonstandard-boundary Einstein filling (Theorem E)

### 6.1 Theorem — Proved by analytic local construction and validated flow

There exists a complete real-analytic diagonal Bianchi--IX metric on the total space of \(\mathcal O(-1)\to\mathbb{CP}^1\) satisfying \(\operatorname{Ric}=-6g\). It is ACH with fibre slot 1 and convergence rate at least \(O(e^{-1.99t})\). Its conformal infinity is a nonstandard Rossi sphere with
\[
\rho_\infty\in[2.19013,2.19242].
\]
The bolt has \(b=4/5\), while the free fourth-order anisotropy lies in the validated interval used by the Fuchsian/CAPD passage.

Proof components: analytic Fuchsian solution in \(s=t^2\); exact constraint propagation; source-level equivalence of the compact CAPD vector field and the Einstein system; interval transport of a tiled bolt family to a verified cusp block; opposite unstable-face crossings; Ważewski continuation; and quadratic drift control of
\[
\widetilde\Phi=q+\frac{y_g-y_h}{4}-\zeta\sinh q.
\]

Primary paths: `workspace/notes/step15_ach_projected_theory.md`; `workspace/scripts/ach_bolt_fuchs.py`; `workspace/data/ach_capd/fuchs_boxes_N6_complex.json`; `workspace/scripts/ach_capd_field_check.py`; `workspace/data/ach_capd/wazewski_T2.75.json`; `workspace/scripts/ach_block_verify.py`; `workspace/scripts/ach_phi_drift.py`; `workspace/data/ach_capd/rossi_enclosure_b0.8.json`.

### 6.2 Exact bolt geometry — Proved

At \(b=4/5\), the scalar curvature is \(-24\). The earlier values \(\operatorname{diag}(-139/16,57/16,41/8)\) and \(\operatorname{diag}(-385/16,203/16,91/8)\) were produced by a symbol-collision bug in the peer script (peer message 771) and are withdrawn. The repaired exact computation, which agrees with the independent coordinate limit (operator norms \(39.3985\), \(194.083\)), gives the unordered chiral curvature-operator Weyl blocks
\[
\operatorname{diag}(-41/16,-41/16,41/8),
\qquad
\operatorname{diag}(-91/16,-91/16,91/8),
\]
   Neither bolt block has the Kähler--Einstein spectrum. More strongly, the CAPD off-bolt calculation now transports all forty outward-rounded analytic Fuchsian boxes to \(t=.5\) and proves that both chiral Weyl blocks have simple spectrum there. The weakest pairwise gap lower bounds are \(0.9669947784\) and \(0.003926698448\), and the discriminant lower bounds are \(66.1883\) and \(0.0006333125\). A point-box comparison with the independent coordinate/JAX curvature calculation agrees within \(5.6\times10^{-15}\). Thus the metric is not conformally Kähler on any nonempty open set in either orientation; analyticity excludes an open conformally Kähler region after the discriminant is nonzero at the certified orbit.

Primary paths: `Sessions/S1003A01/workspace/scripts/ach_bolt_weyl_exact.py`; `workspace/scripts/ach_bolt_weyl_series_check.py`; `workspace/scripts/ach_weyl_interval.cpp`; `workspace/scripts/ach_weyl_interval_run.py`; `workspace/data/ach_capd/weyl_discriminant_t0.5.json`.

### 6.3 Relation to the marked-cell problem

Theorem E changes the boundary CR structure and therefore is not an exact-CH-collar zero-cost cell. The certified cheap cells also do not shadow this Einstein trajectory: their positive action is concentrated near a Burns-like core and their collar returns rapidly to CH. The theorem supplies a possible compactness endpoint and an existence result, not a proof that \(p_{1,0}=0\).

The Biquard--Herzlich identity places the convergent combined curvature integral against \(\chi-3\tau+\nu\). For the blown-up ball \(\chi-3\tau=5\); the standard sphere value leaves slack, so topology does not exclude a standard-boundary filling. Numerical branch-wide nonexistence at \(\rho=1\) remains open and would be dynamical even in the diagonal class. The off-bolt conformal-Kähler question is now closed by the interval theorem in §6.2.

## 7. Common mechanism and its present mathematical scope

The proved pieces support the following schema. Actual metric-wise fields and their differential prolongations control regular bulk geometry. A topology change is realized by a complete marked cell whose leading response depends on the ambient self-dual curvature, not solely on the topology. Kernel directions can evade the linear payment and exploit a negative quadratic interaction. Volume entropy supplies a separate field-free obstruction to exact Einstein metrics on real-hyperbolic blow-ups. Pure handles retain the exact \(32\pi^2\) cost, while blow-ups admit certified costs below \(8\pi^2\) in CH bulk. Exact Einstein filling can occur after moving the CR boundary away from the standard CH value. The unrestricted \(\alpha\)-problem requires a compactness/localization theorem linking global near-minimizers to these bulk and cell objects.

The general-bulk first-order law is now proved as an upper construction (Theorem F). Still open: the full \(-9\) remainder, positivity of \(p_{1,0}\), equality of global and cell asymptotics, standard-CR diagonal nonexistence, and a universal degeneration theorem. Two rigid inputs constrain degeneration. First, an almost-Euclidean neck enclosing a blow-up class carries \(P\ge8\pi^2-C\varepsilon\), and a scalar-flat ALE bubble with \(\Gamma=1\) carries \(P\ge8\pi^2(k+4\ell)\). Second, no nontrivial exact-CH-collar cell is Einstein: the locally symmetric developing-map argument removes the temporary \(\ell=2k\) exception. Hence \(\mathfrak P_{1,0}<8\pi^2\) forbids almost-flat concentration of the class, and \(\mathfrak P_{k,\ell}=0\) for any \((k,\ell)\ne(0,0)\) requires escape of the collar, collapse, or concentration through curved necks.

The real-hyperbolic contrast now has two theorems beyond the numerical scan. On closed \(Y\#k\overline{\mathbb{CP}}^2\) with \(s=-12\), a Ricci floor \(\operatorname{Ric}\ge-3(1+\varepsilon)g\) gives
\[
P\ge8\pi^2k-12\operatorname{Vol}(Y)[1-(1+\varepsilon)^{-2}]
\]
by BCG entropy and Bishop comparison. For a complete exact-\(H^4\)-exterior cell, the scalar floor \(s\ge-24\) forces the manifold to be hyperbolic by the non-spin Chruściel--Delay positive-energy theorem in dimension four. Details and sources are in `workspace/notes/step22_hyperbolic_volume_mass_and_weyl_certificate.md`.

**Two-channel cell identity (Theorem C, Steps 23–24).** For a complete cell of marked topology \((k,\ell)\), exactly equal to the model outside a compact set for a fixed end marking, with Yamabe representative \(\hat g=u^2g\), \(\hat s=-24\), \(u\to1\) (derivative decay faster than inverse volume growth),
\[
P_{\rm cell}-8\pi^2(k+4\ell)=4\Delta W_++48\,\mathrm{RV}(\hat g)+3\int(\Delta u/u)^2+24\int|\nabla u|^2,
\]
where \(\mathrm{RV}\) is the matched relative volume: matched truncations of cell and model plus the whole-cell integral \(\int(u^4-1)d\mu_g\). For exact-CH ends \(u\) exists uniquely for **every** smooth cell (S1003A01 weak-barrier theorem, no sign condition on \(s\)), so the exact-ended \(J_6\) infimum equals the \(P\) infimum over complete scalar \(-24\) metrics asymptotic to the marked CH end at rate \(>4\). The H\(^4\) cell bound \(P\ge8\pi^2\) is reduced to \(\mathrm{RV}(\hat g)\ge0\). Numerically (11 diagonal cells, both bulks, \(x_0\le1\)) \(\mathrm{RV}(\hat g)>0\) always; \(48\mathrm{RV}\approx-x_0s_p/12\) and \(4\Delta W_+\approx-x_0W^+_p(\zeta,\zeta)\) to first order: the two halves of \(\mathbf R^+\) in Theorem F are the volume and Weyl channels. The certified CH witness pays \(+0.0706\) in volume and saves \(-0.0747\) in Weyl (units \(8\pi^2\)). The scalar floor does not separate the two bulks (both families of competitors dip below the background scalar); the Weyl channel does. Relative signature for the one-blow-up CH cell gives \(\Delta W_+-\int|W^-|^2=-12\pi^2\); at \(P=0\) Theorem C then reproduces the relative Biquard–Herzlich identity, \(\mathrm{RV}=5\pi^2/6-\int|W^-|^2/12\), so these identities alone give no obstruction to a standard-CR Einstein filling.

**Monopole estimates give no per-blow-up cell payment (Step 24).** For minimal general type \(X\), LeBrun's convex invariant satisfies \(\beta^2(X\#k\overline{\mathbb{CP}}^2)=c_1^2(X)\), independent of \(k\): averaging the monopole classes \(\pm c_1(X)\pm E_1\pm\cdots\pm E_k\) puts \(c_1(X)\) in the convex hull, and scalar-recovery metrics give the reverse inequality (`Knowledge/objects/papers/Four-Manifolds-Curvature-Bounds-and-Convex-Geometry--9dec43e67dff--ae37fe317499/object.md`). Thus \(\int s^2\) and \(\int(s-\sqrt6|W_+|)^2\) see only the minimal model; the \(k\)-dependence of \(8\pi^2(k-A/3)\) enters only through \(\chi,\tau\) in Chern–Weil. Positivity of \(p_{1,0}\) must come from intrinsic Weyl–volume geometry, not from localizing a Seiberg–Witten estimate.

## 8. The missing global passage

**Steps 33–34: characteristic–constraint link calculus (proved identities and corrected consequences).** For every compact \(\Omega\subset M\) with smooth boundary,
\[
\widehat P(\Omega)=\frac1{2\pi^2}\int_\Omega|W^\pm|^2+\frac1{96\pi^2}\int_\Omega s^2-(2\chi\pm3\tau)(\Omega)+\mathcal Q_\pm(\partial\Omega),\qquad\mathcal Q_\pm=2\mathcal E\mp3\mathcal H,
\]
with \(\mathcal E\) Chern's boundary term and \(\mathcal H=\eta+\int T_{p_1}\) the APS boundary term (Theorem G). Verified model charges are: round flat-conical link \((2,2)\); flat-conical/ALE \(S^3/\Gamma\) limit \((2/|\Gamma|\mp3\eta_\Gamma)\), recovering Lemma Q; a fixed-smooth-metric thin tube around a surface of self-intersection \(n\), \((2\chi(\Sigma)\pm3\operatorname{sgn}n)\), giving the bolt \((1,7)\); the controlled Taub–NUT-chirality Hopf-adiabatic link \((-2,2)\), with the opposite chirality \((2,-2)\); and the CH sphere \((2-9\sinh^4\tau,2-3\sinh^4\tau)\). The radial collar jet is part of every charge. For \(D\cong(\#k_D\overline{\mathbb{CP}}^2\#\ell_D S^1\times S^3)\setminus B^4\),
\[
P(g)\ge8\pi^2[k_D+4\ell_D-(2-\mathcal Q_+(\partial D))].
\]
Disjoint regions add. For one blow-up with \(\widehat P<1-\varepsilon\), a standard negative-definite blow-up region has \(\mathcal Q_+\le1+\widehat P<2-\varepsilon\); therefore an exceptional subtree cannot be separated from the bulk by a \(C^2\)-Euclidean-round \(S^3\) germ. This does not exclude orbifold necks, Taub–NUT-chirality collapse, curved/sheared links, bulk bubbling, or regions containing positive intersection form.

The complementary symmetry-free foliation identity is
\[
|\operatorname{Ric}^\circ|^2=\frac43\mathcal C^2+2|\mathcal J|^2+|\mathcal S|^2,
\quad
\mathcal C=\tfrac12(\Theta^2-|K|^2-R_h)+s/4,
\quad
\mathcal J=\operatorname{div}K-d\Theta,
\]
where \(\mathcal S\) is the trace-free tangential evolution residual. Lemma N is the diagonal Hamiltonian component; Lemma P and fibre/base pinning use the two diagonal tangential-evolution projections, not the Codazzi component. Exact transport identities tested against \((\mathcal C,\mathcal J,\mathcal S)\) give weighted Cauchy–Schwarz lower bounds. Thus characteristic transgressions price topology and boundary-germ changes, while Gauss–Codazzi/evolution residuals price drift-corrected shape changes. Their bounds are generally combined by a maximum unless regions or orthogonal components are separated. **Link regularity** is control/convergence of the intrinsic link geometry, second fundamental form, characteristic and Dai spectral transgressions, and the field boundary data actually used on the bulk. Critical \(L^2\) defect alone does not establish it. Details: `notes/step33_link_charges_global_decomposition_static_channel.md`, `notes/step34_characteristic_constraint_calculus_and_N_probe.md`, and the Step-34 TTCS integrations.

The classical handle-free lower interval is
\[
8\pi^2\max\{0,k-A/3\}\le\inf P\le8\pi^2k,
\]
so present lower information vanishes for \(0<k<A/3\). A successful global passage must do more than extract an ideal limit: it must preserve family-uniform scale control, distinguish collapse from noncollapsed convergence, identify the CH bulk through actual-field coercivity, assign topological charge to complete bubbles or cells, and compare asymptotically CH cells with exact-collar infima by truncation.

On the scalar-minus-four class, put
\[
R_1(g)=\int_M|\nabla\operatorname{Rm}_g|^2\,d\mu_g.
\]
If \(P(g_0)\le p+\delta\), \(0<R_1(g_0)<\infty\), \(\varepsilon=\delta/R_1(g_0)\), and \(g\) is a \(\delta\)-near-minimizer of \(P+\varepsilon R_1\), then the elementary comparison proves
\[
P(g)-p\le3\delta,\qquad R_1(g)\le3R_1(g_0).
\]
This selection lemma is valid and needs neither an attained minimum nor a gauge. It does not yet give a uniform compactness theorem: the comparison \(g_0=g_0(\delta)\) may have \(R_1(g_0)\to\infty\), the certified upper construction is not known to be \(\delta\)-close to the unknown infimum for arbitrarily small \(\delta\), and an intrinsic derivative-curvature bound gives a uniform \(L^4\) bound only after a uniform Sobolev or harmonic-radius input. Across the balanced family, even an extensive bound \(R_1=O(A)\) permits scales of order \(A^{-1/2}\) and is not local equiintegrability. The corrected statement and the independent reading of Theorem E are in `workspace/notes/step19_theorem_package_and_selection_lemma.md`.

## 9. Highest-return next theorems

1. Prove positivity of the absolute cell channel \(\inf\{8\pi^2+4\Delta W_++48\mathrm{RV}(\hat g)\}>0\) over complete scalar \(-24\) metrics asymptotic to the standard marked CH end on \(O(-1)\). (The earlier linear trade-off \(4\Delta W_+\ge-\Lambda48\mathrm{RV}-\eta\), \(\Lambda\in[1.03,1.06]\), is withdrawn: \(\Lambda\to1\) is forced by Theorem F in the kernel direction and \(\Lambda>1\) gives no absolute bound.) The first complete form of this is the diagonal compactness/trichotomy theorem of `workspace/notes/step25_diagonal_cell_compactness_and_CR_pinning.md`.
2. Real-hyperbolic: prove \(\mathrm{RV}(\hat g)\ge0\) for \(\hat s\equiv-24\) AH metrics on \(D\#k\overline{\mathbb{CP}}^2\) conformal to exact-collar metrics (local topological Schoen problem), and on the closed side the identity \(\mathcal Y(Y\#k\overline{\mathbb{CP}}^2)=Y_{\rm hyp}\), which is now the only input missing from the sharp theorem H.
3. Study the regularity profile \(\mathcal R_*(\delta)=\inf\{R_1(g):P(g)\le p+\delta,\ s_g=-4\}\), and either bound it uniformly or derive a local Sobolev/harmonic-radius estimate from the penalized equation with constants that survive \(\varepsilon\to0\).
4. Use actual-field coercivity to identify a noncollapsed bulk and localize topological charge; separately analyze collapse and the entropy/Ricci critical-exponent obstruction.
5. Prove truncation equivalence between asymptotically CH complete cells and exact-collar cell infima; determine whether \(p_{1,0}>0\) and whether global near-minimizers decompose into cells at that cost.
6. Analyze the exact-standard-CR endpoint in and beyond the diagonal class. Theorem E now has certified non-conformal-Kählerness, but its Rossi boundary remains nonstandard.


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

# Step 4: Near-equality route and Taub--Bolt boundary calibration

## Purpose

This note corrects the Step 3 boundary-mechanism interpretation and records two research assets for Yau Problem 26:

1. a source-based near-equality mechanism for the mixed Seiberg--Witten estimate in the four-dimensional negative branch;
2. a computational calibration of exact `Ric = -g` Taub--Bolt--AdS bolt fillings, used only as attainable boundary data for a cap/matching problem.

The full problem is not reduced to these four-dimensional tests. They are boundary investigations for the strongest known no-Einstein reservoir.

---

## 1. Correction to the small-bubble interpretation

The previous Step 3 statement about ALE cores was too broad. An exactly Ricci-flat ALE metric remains Ricci-flat after scaling. Thus an uncorrected Ricci-flat core, inserted in a metric normalized to target `Ric = -g`, has normalized endomorphism defect

\[
\|g^{-1}(\operatorname{Ric}+g)\|_{op}=1
\]

on the core, independent of scale. This observation only excludes the bare uncorrected core from being a small-defect region.

It does **not** exclude a corrected gluing construction. If the core metric is scaled by `t^2`, an `O(t^2)` relative correction to the scaled core can produce an order-one contribution to the original-scale Ricci endomorphism. Whether such a correction can supply the target `-I`, match the exterior Cauchy data, and keep the unweighted defect small is a linearized solvability and matching problem. The first-obstruction analysis from the peer route remains relevant: a nonzero first obstruction leaves an order-one residual on the ALE core, but a first-obstruction-zero / higher-obstruction construction remains a live mathematical possibility until a further argument rules it out.

Consequently, the useful cap question is not whether every exceptional handle must live at a natural scale. It is whether corrected local models with the correct topology and boundary data can be made uniformly close to `Ric = -g` in unweighted operator norm after matching to the exterior metric.

---

## 2. Source-corrected provenance of the mixed estimate

The coefficient used in the Step 3 pinching bound is source-supported, but not by the withdrawn Weyl-only argument. The relevant chain is:

- LeBrun 2001, *Ricci curvature, minimal volumes, and Seiberg--Witten theory*, Proposition 2.1--2.4 and Proposition 3.1, in `Knowledge/objects/papers/Ricci-curvature-minimal-volumes-and-Seiberg-Witten-theory--16b01946d13f--cab40be18df4/object.md`.
- Ishida--LeBrun connected-sum applications restate the consequence as Proposition 4 / Theorem D in `Knowledge/objects/papers/math-0111228-Curvature-Connected-Sums-and-Seiberg-Witten-Theory--84e6ef833958--5b74c8864d85/object.md` and `Knowledge/objects/papers/Spin-Manifolds-Einstein-Metrics-and-Differential-Topology--1a2235341441--f19aa00d70c8/object.md`.

The direct inequality is

\[
I(g):=\frac1{4\pi^2}\int_M\left(\frac{s^2}{24}+2|W_+|^2\right)d\mu
\ge \frac23(a^+)^2 .
\]

Its proof in LeBrun 2001 does not say that `F_A^+` is harmonic or that a Weyl-only lower bound holds. It starts from the Seiberg--Witten spinor Weitzenböck formula and a Weitzenböck formula for self-dual 2-forms, passes through an estimate involving the lowest eigenvalue `w` of `W_+`, uses a conformal rescaling with `s+3w` constant, and obtains

\[
\int_M\left(\frac23s-2\sqrt{\frac23}|W_+|\right)^2 d\mu
\ge 32\pi^2(a^+)^2 .
\]

The displayed `2/3` estimate follows by a triangle inequality and Cauchy--Schwarz in a two-dimensional norm space. Therefore near-saturation of the final estimate can be studied through the concrete inequalities in LeBrun's proof, not through a false harmonicity assertion for `F_A^+`.

---

## 3. Equality mechanism recovered from the source

LeBrun 2001 Proposition 2.4 says that equality in the squared estimate or its `L^2` descendants forces an almost-Kähler structure with special curvature alignment:

- the almost-Kähler form `ω` belongs pointwise to the lowest eigenspace of `W_+`;
- `s+s^*` is a non-positive constant, where `s^*=s/3+2W_+(ω,ω)`;
- the first Chern class of the almost-complex structure agrees with the relevant spin^c first Chern class;
- for the stronger descendant estimate, `W_+` is also invariant under the almost-complex structure.

Conversely, compact almost-Kähler metrics with these properties saturate the corresponding estimates. If such a saturating metric is Einstein, LeBrun cites Armstrong to conclude it is actually Kähler--Einstein.

For blow-ups, LeBrun 2001 Proposition 3.2 adds a topological obstruction to exact equality. In the proof, equality would require the almost-Kähler class to have zero pairing with every exceptional class `E_j`. Taubes's theorem would then represent an exceptional class by a pseudo-holomorphic sphere of positive symplectic area, contradicting the zero pairing. Thus exact equality is excluded for `k>0`.

This exact-equality picture is directly relevant to the Yau 26 boundary regime: if a no-Einstein sequence has `δ_- -> 0` and `k/A -> 1/3`, the mixed estimate is forced close to equality after normalization by `A`. The problem becomes whether the exact-equality contradiction has a quantitative version robust under collapse and concentration.

---

## 4. Forced near-equality calculation

Let

\[
I=\frac1{4\pi^2}\int\left(\frac{s^2}{24}+2|W^+|^2\right),\qquad
J=\frac1{4\pi^2}\int\frac{|\mathring r|^2}{2},\qquad
q=k-\frac A3 .
\]

For `M=X#k CPbar^2` with `A=c_1^2(X)`, Chern--Gauss--Bonnet gives

\[
I-J=A-k.
\]

For a monopole class chosen by LeBrun's sign trick, `(a^+)^2 >= A`. Define the mixed-estimate deficit

\[
D_a=I-\frac23(a^+)^2\ge0.
\]

Then

\[
D_a
=J+(A-k)-\frac23(a^+)^2
\le J+(A-k)-\frac23A
=J-q.
\]

Therefore, in any sequence with `δ_-(g)->0`, `k/A -> 1/3` from above, and the standard negative-branch normalization `Ric ≈ -g`, the pointwise bound `|\mathring r|^2 <= 4δ^2` plus the CGB volume upper bound gives `J/A=O(δ^2)`. Hence

\[
\frac{D_a}{A}\to 0.
\]

This conclusion does **not** require extra assumptions that `W_+` is small, that the CGB volume bound is saturated, or that the exceptional classes are already known to be nearly anti-self-dual.

If one additionally uses the maximum over all sign choices, the algebraic identity

\[
2^{-k}\sum_\varepsilon (a_\varepsilon^+)^2
=(c_1(X)^+)^2+\sum_j(E_j^+)^2
\]

implies

\[
J\ge q+\frac23\sum_j(E_j^+)^2 .
\]

Thus `δ -> 0` and `q/A -> 0` force

\[
\frac1A\sum_j(E_j^+)^2\to0.
\]

This is a consequence for actual Ricci-pinched metrics, not an abstract intersection-form lower bound. The intersection form alone permits a positive subspace nearly orthogonal to many exceptional directions; any useful positive lower bound must come from the geometry and analysis of the metrics themselves.

---

## 5. Near-equality rigidity route

The source-recovered equality mechanism suggests the following route. For a hypothetical sequence with `δ_- -> 0` on no-Einstein blow-ups near `k/A=1/3`, one obtains normalized near-vanishing of the analytic slack in LeBrun's proof. The concrete terms to track are:

1. slack in the spinor Weitzenböck/Hölder chain of Proposition 2.1, which should force the Seiberg--Witten spinor quadratic form to behave like a constant-norm self-dual harmonic form on most of the volume;
2. slack in the conformal minimization step for `s+3w`, which may fail to compactify cleanly under collapse or Weyl concentration;
3. slack in replacing the lowest eigenvalue `w` by `-|W_+| sqrt(2/3)`, which controls alignment of the emerging almost-Kähler form with the lowest eigenspace of `W_+`;
4. slack in the triangle and Cauchy--Schwarz steps producing the final `I >= 2/3(a^+)^2` estimate;
5. the Taubes area contradiction for exceptional classes, now with exceptional areas possibly tending to zero and concentrating topology in regions that carry small normalized trace-free Ricci energy.

A proof route would show that these slacks cannot all be `o(A)` under two-sided pointwise Ricci pinching unless the smooth manifold carries an Einstein metric or the exceptional topology disappears into a controlled Einstein-compatible degeneration. A counterexample route would construct geometry where exceptional topology concentrates in regions that are invisible to the normalized mixed-estimate defects while preserving `Ric≈-g` in unweighted operator norm.

This is more directly connected to Yau 26 than sampling abstract Hodge projections: the latter does not encode Ricci pinching or Seiberg--Witten spinor behavior.

---

## 6. Taub--Bolt--AdS boundary-data calibration

I implemented `workspace/scripts/step4_taub_bolt_boundary_probe.py` using Akbar's displayed Taub--Bolt--AdS metric with `Lambda=-1`, so `Ric=-g`. For the period `Delta psi=4pi` case the regularity range is

\[
0<L^2\le \frac{2-\sqrt3}{4}\approx0.0669872981.
\]

The script samples the two bolt branches and records, at finite cutoffs, the induced Berger boundary metric

\[
a^2(\sigma_1^2+\sigma_2^2)+b^2\sigma_3^2
\]

together with the two principal second-fundamental-form ratios `(da/dt)/a` and `(db/dt)/b`. Outputs:

- `workspace/data/step4_taub_bolt_ads_boundary_samples.csv` with 52,800 sampled boundary Cauchy data points;
- `workspace/data/step4_taub_bolt_ads_summary.json` summarizing ranges and representative zero-defect examples;
- `workspace/figures/step4_taub_bolt_boundary_map.png` plotting attained `(a,b/a)` data.

Key computational observations under these conventions:

- every sampled point is an exact zero-defect cap for its own first and second boundary data, because the interior metric is Einstein with `Ric=-g`;
- the sampled p=1 Akbar convention gives `b/a` roughly in `[7.8e-3,0.397]` on one branch and `[4e-6,0.330]` on the other branch over the sampled finite boundaries;
- the summary records a reliable zero-defect example near `b/a=0.25`, with `L≈0.216`, `rho_boundary≈21.86`, `a≈21.85`, and mean curvature trace `≈1.734`.

The computation has a precise mathematical meaning: an exceptional-handle-type `O(-1)->S^2` filling has no intrinsic negative-Einstein residual for its attained boundary data. Therefore a cap residual infimum over unconstrained `U(2)`-invariant metrics cannot establish a general obstruction. A useful computation must instead ask which boundary Cauchy data are attainable by smooth `Ric≈-g` caps and whether those data match exterior regions in a closed no-Einstein manifold without creating unweighted Ricci defect in the transition.

I also wrote `workspace/scripts/step4_akbar_polynomial_check.py` to test Akbar's displayed seventh-degree boundary polynomial for selected `(A,B)=(a^2,b^2)`. The roots from my quick transcription did not consistently satisfy the unsquared branch equations, so the polynomial transcription is not being used as evidence. The parametric Einstein equations and direct boundary data are the reliable calibration here.

---

## 7. Revised mathematical picture after this step

The mixed estimate remains a strong four-dimensional obstruction. It eliminates any LeBrun-style no-Einstein counterexample sequence with `k/A` bounded above `1/3` by a positive amount. It does not eliminate the boundary families where the no-Einstein theorem is strict but the normalized mixed-estimate margin tends to zero, such as the connected-sum forms in Ishida--LeBrun Theorem 7 with `k+4=A/3` or `k+8=A/3`.

The cap probe and the near-equality route should now be developed together:

- exact Taub--Bolt--AdS models show that local exceptional-handle topology can occur in negative-Einstein geometry for suitable boundary data;
- the relevant obstruction, if any, is in global matching, transition geometry, or the quantitative near-equality form of LeBrun's Seiberg--Witten argument;
- first-obstruction-zero corrected ALE gluing remains a serious route to examine, not something excluded by the bare Ricci-flat-core calculation;
- a rigorous proof would need to convert `D_a/A -> 0` plus `δ->0` into geometric rigidity strong enough to activate the exact-equality contradiction or to produce an Einstein metric on the same smooth manifold;
- a rigorous refutation would need a construction preserving unweighted two-sided Ricci pinching through all caps, necks, and corrections on smooth no-Einstein manifolds.

This step therefore reorients the next work away from a single free bolt optimization and toward boundary-data matching plus quantitative near-equality analysis.

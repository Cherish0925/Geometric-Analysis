# TTCS Independent Branch Record

```json
{
  "step_id": 84,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A02/workspace/notes/step84_preceptor_interval_variational_audit.md",
    "Sessions/S0910A02/workspace/notes/step83_near_pinched_construction_and_frontier_reduction.md",
    "Sessions/S0910A02/workspace/data/step84_interval_variational_audit.json",
    "Knowledge/objects/papers/Orbifold-compactness-for-spaces-of-Riemannian-metrics-and-applications--30aa929b9159--a0e9497fbde6/object.md",
    "Knowledge/objects/papers/Moduli-spaces-of-critical-Riemannian-metrics-in-dimension--4e6975d02959--2513743a9d1b/object.md",
    "Knowledge/objects/papers/Rigidity-and-stability-of-Einstein-metrics-for-quadratic-curvature-funct--84d7f54aa988--cf9608570634/object.md",
    "Sessions/S0910A02/workspace/notes/step11_cz_spike_and_proposition_A.md",
    "Sessions/S0910A02/workspace/notes/step79_alignment_closure_and_collapse_transition.md"
  ]
}
```

## Task

The active target is Yau Problem 26 as stated in the session: prove or refute the dimension-only Ricci pinching implies Einstein-existence proposition, without changing quantifiers. A new possible instrument was identified in Step 84: on the audited A1 positive and negative mirror mixed rows, the four-dimensional functional F(g)=∫(|W|^2+s^2/24) satisfies F=8π²χ+(1/2)∫|E|², and the near-pinched families show inf F=8π²χ with no energy gap; Einstein existence is exactly attainment of this lower bound. Read the context and develop a scientific memo on whether this F-attainment/concentration-compactness route can be made into a concrete proof or obstruction strategy for the mixed rows. Identify the strongest plausible lemmas, the needed compactness/Palais-Smale/epsilon-regularity inputs, how Anderson/Tian-Viaclovsky/Gursky-Viaclovsky results could and could not be adapted, the main escape mechanisms (collapse, conformal degeneration, noncritical minimizing sequences, bubbling with exact energy saturation), and cheap discriminating calculations or source checks that would most clarify the route. Do not invent literature or claim the route works; give mathematically precise possibilities and failure modes useful for the next core agent.

## Output

# Memo: \(F\)-attainment and concentration–compactness on the mixed \(A_{1}\) rows

## 1. The functional is best written as a squared Einstein defect

Set
\[
\mathcal Z(g):=\int_M |E_g|^2\,dV_g,
\qquad
E=\operatorname{Ric}-\frac{s}{4}g.
\]
Then
\[
F(g)=8\pi^2\chi(M)+\frac12\mathcal Z(g).
\]
Thus the variational problem is exactly
\[
\inf \mathcal Z=0,
\qquad
\mathcal Z(g)=0\Longleftrightarrow g\text{ is Einstein}.
\]

This reformulation exposes both the strength and the central obstruction. The \(A_1\) constructions show that the relaxed problem has zero-energy generalized minimizers consisting of an Einstein orbifold together with Ricci-flat ALE pieces. Since every component has \(E=0\), bubbling loses no \(\mathcal Z\)-energy. Consequently, a direct method naturally produces an orbifold–ALE tree rather than a smooth metric.

The curvature decomposition still gives useful coercivity:
\[
F(g_i)\to 8\pi^2\chi
\quad\Longrightarrow\quad
\int |W_{g_i}|^2\le C,\qquad
\int s_{g_i}^2\le C,\qquad
\int |E_{g_i}|^2\to0,
\]
hence \(\int|\mathrm{Rm}_{g_i}|^2\le C\). The missing ingredient is not total curvature energy; it is smooth compactness across zero-cost Ricci-flat bubbles.

## 2. Euler equation and the exact link with Gursky–Viaclovsky

In four dimensions,
\[
\mathcal Z=\int |\operatorname{Ric}|^2-\frac14\int s^2,
\]
so this is Gursky–Viaclovsky’s functional \(\mathcal F_\tau\) at
\[
\tau=-\frac14.
\]
Using the first-variation formulas in the supplied source, its gradient is
\[
\begin{aligned}
\mathcal G(g)
={}&-\Delta_L\operatorname{Ric}
+\frac12\nabla^2s
-2\operatorname{Ric}\circ\operatorname{Ric}
+\frac{s}{2}\operatorname{Ric}\\
&+\left(\frac12|\operatorname{Ric}|^2-\frac18s^2\right)g.
\end{aligned}
\]
Its trace is
\[
\operatorname{tr}_g\mathcal G=-\frac12\Delta s.
\]
Therefore every smooth critical metric of \(\mathcal Z\) has constant scalar curvature. Substituting \(\operatorname{Ric}=E+\frac{s}{4}g\) then gives
\[
\mathcal G
=
-\Delta_LE-2E\circ E-\frac{s}{2}E+\frac12|E|^2g.
\]
This is the elliptic critical-metric system to which Anderson/Tian–Viaclovsky methods are most naturally attached.

At an Einstein metric with scalar curvature \(R\), the Gursky–Viaclovsky Jacobi operator has particularly favorable factorization. On transverse-traceless tensors,
\[
J_{\mathrm{TT}}
=\frac12\left(\Delta_L+\frac{R}{2}\right)^2,
\]
while on conformal variations \(h=fg\),
\[
\operatorname{tr}J(fg)=\frac12(3\Delta+R)\Delta f
\]
with their Laplacian convention. Thus every Einstein metric is variationally stable modulo scaling, diffeomorphisms, and infinitesimal Einstein deformations. This is strong local information, but its constants depend on the spectral gap of the Einstein operator. Along an orbifold–EH degeneration, approximate kernel modes arise on the necks and bubbles, so no uniform coercivity is expected.

For the positive product orbifold, \(R=4\), and the TT root is \(-\Delta_L=2\). The cover \(S^2\times S^2\) has TT eigenvalues \(0,4,\ldots\) in the supplied Gursky–Viaclovsky calculation, suggesting invertibility of the orbifold base at \(\tau=-1/4\), after removing isometries. The hyperbolic product base has integrable Einstein deformations coming from the Teichmüller spaces of the two factors; the invariant subspace under \(\iota\times\iota\) should be computed explicitly.

## 3. A realistic compactness theorem and what it would produce

A useful approximate-critical compactness statement would have the following form.

Let \(g_i\) be unit-volume constant-scalar-curvature metrics on a fixed closed four-manifold such that

\[
C_S(g_i)\le C,\qquad
\int |\mathrm{Rm}_{g_i}|^2\le\Lambda,\qquad
b_1(M)\le B,
\]
and suppose
\[
\mathcal Z(g_i)\to0,
\qquad
r^{\,4-4/p}
\|\mathcal G(g_i)\|_{L^p(B_r)}\to0
\]
uniformly on relevant balls for some \(p>2\). Then one expects, after diffeomorphisms and passage to a subsequence:

1. smooth convergence away from finitely many points to an Einstein orbifold;
2. rescaled convergence at concentration points to scalar-flat critical ALE spaces;
3. because \(\mathcal Z(g_i)\to0\), every smooth bubble is Ricci-flat;
4. an energy identity for \(F\), \(\mathcal Z\), and the two Weyl chiralities;
5. smooth attainment precisely when no nonflat bubble occurs.

This is the closest adaptation of Tian–Viaclovsky. Their local regularity begins with
\[
\Delta\operatorname{Ric}=\mathrm{Rm}*\operatorname{Ric}.
\]
An approximate equation with source \(T_i\) can plausibly be handled when \(T_i\) is small in a scale-compatible \(L^p\) space with \(p>2\). Moser iteration and harmonic-coordinate elliptic estimates then acquire additive \(T_i\)-terms. A source controlled only in \(W^{-2,2}\), or even at the scale-critical \(L^2\) level, does not furnish the same pointwise curvature estimates.

Even the strongest version of this theorem would yield a compactified minimizer, not automatically a smooth one. On the audited families it would reproduce exactly
\[
\text{Einstein orbifold}+\text{Eguchi--Hanson bubbles},
\]
with
\[
16\pi^2+N\cdot12\pi^2=8\pi^2\chi(M).
\]
There is no missing energy whose disappearance could force removal of the singular points.

## 4. Why ordinary Palais–Smale control is probably too weak

A minimizing sequence is automatically weakly almost critical. The first variation satisfies schematically
\[
|D\mathcal Z_g[h]|
\le
C\|E\|_{L^2}
\left(
\|\nabla^2h\|_{L^2}
+\|\mathrm{Rm}\|_{L^2}\|h\|_{L^\infty}
+\|h\|_{L^\infty}
\right)
+C\|E\|_{L^2}^2\|h\|_{L^\infty}.
\]
Hence, under the available \(L^2\)-curvature bound,
\[
\|D\mathcal Z_g\|_{(W^{2,2}\cap L^\infty)^*}\to0.
\]
Thus Ekeland selection in a weak metric-space topology adds little: the explicit \(A_1\) sequence already has this form of Palais–Smale behavior.

The log annulus may satisfy even an \(L^2\)-gradient estimate. For
\[
h=\chi(t)K,\qquad t=\log r,
\]
with \(K=r^2\widehat K(\theta)\), the leading trace-free Ricci term is
\[
E_{\mathrm{lin}}
=
-\frac12\left(\chi_{tt}+6\chi_t\right)\widehat K.
\]
For the logarithmic profile \(\chi(t)=\psi((t-t_b)/L)\),
\[
|E_{\mathrm{lin}}|=O(L^{-1}),
\qquad
|\mathcal G_{\mathrm{lin}}|=O((Lr^2)^{-1}).
\]
Consequently,
\[
\|\mathcal G_{\mathrm{lin}}\|_{L^2(A_{b,R})}^2
\asymp
\frac1{L^2}\int_b^R \frac{dr}{r}
=O(L^{-1}),
\]
whereas for \(p>2\),
\[
\|\mathcal G_{\mathrm{lin}}\|_{L^p(A_{b,R})}
\asymp
\frac{b^{4/p-2}}{L},
\]
which grows as \(b\to0\). A sector-by-sector symbolic calculation using the existing ten-dimensional Weyl basis would verify whether any angular component cancels the displayed leading term.

This model indicates a sharp distinction:

- \(L^2\)-gradient Palais–Smale compactness can coexist with EH bubbling.
- An \(L^p\), \(p>2\), residual estimate would suppress this particular neck mechanism, but there is no evident variational selection principle producing such an estimate.

## 5. The \(L^2\) functional is even less sensitive to matching than the pointwise pinching construction

For the annular interpolation,
\[
\mathcal Z_{\mathrm{ann}}^{\mathrm{lin}}
=
\frac14
\left(\int_{S^3/\{\pm1\}}|\widehat K|^2\right)
\int_{t_b}^{t_R}
e^{4t}\bigl(\chi_{tt}+6\chi_t\bigr)^2\,dt.
\]
Unlike the \(C^0\) Ricci defect, this integral strongly rewards moving the transition toward the tiny inner radius. A cutoff changing over a fixed logarithmic width near \(r\asymp b\) has order-one Ricci defect there but costs only
\[
\mathcal Z_{\mathrm{ann}}=O(b^4).
\]
Therefore \(\mathcal Z\) does not retain the logarithmic matching obstruction that was visible in the pointwise estimate. The transition radius \(b\) is also not canonical; changing \(b=a^\gamma\) changes the decay rate. A renormalized quantity such as \(b^{-4}\mathcal Z\) may detect the Weyl mismatch \(K\), but it depends on the chosen neck scale unless that scale is recovered intrinsically from curvature concentration.

This is the critical-capacity mechanism behind exact energy saturation: topology carried by a Ricci-flat ALE piece can be inserted through a shrinking region at vanishing \(\mathcal Z\)-cost even when the Einstein matching equations are not solvable.

## 6. What the three existing source families contribute

### Anderson

For the explicit audited metrics, one already has two-sided pointwise Ricci control, fixed macroscopic volume, fixed diameter, and bounded \(L^2\) full curvature. Anderson’s Ricci-bounded four-dimensional compactness machinery is therefore well suited to recovering the Einstein orbifold limit in \(C^{1,\alpha}\) and weak \(W^{2,p}\) form. Curvature spikes may disappear in this topology, exactly as in the Calderón–Zygmund example.

Anderson’s 2003 theorem assumes noncollapse, total \(L^{n/2}\) curvature control, and a small-curvature estimate. It does not derive the latter merely from \(\mathcal Z\to0\). Its conclusion is orbifold compactness, which is fully compatible with the mirror degenerations.

### Tian–Viaclovsky

Exact \(\mathcal Z\)-critical metrics fit the same elliptic pattern as their critical classes: constant scalar curvature and
\[
\Delta\operatorname{Ric}=\mathrm{Rm}*\operatorname{Ric}.
\]
Their Sobolev, energy, volume, and \(b_1\) hypotheses are natural for the simply connected rows. The most plausible extension is an approximate equation with a source small in \(L^p\), \(p>2\). At \(p=2\), the log annulus calculation above supplies a model for concentration that remains Palais–Smale.

### Gursky–Viaclovsky

Their results identify the correct local Hessian and provide strict local minimization whenever the Einstein operator has no kernel. They apply in a \(C^{2,\alpha}\) neighborhood of a fixed smooth Einstein metric. The \(A_1\) families leave every such fixed neighborhood because curvature diverges and the injectivity geometry changes. Near the compactification stratum, the relevant replacement is a weighted orbifold–ALE Kuranishi theory; its finite-dimensional equations would be close relatives of the Einstein desingularization coefficients already studied by Biquard and Ozuch.

## 7. Main escape mechanisms

### Exact-saturation bubbling

The orbifold part and every EH bubble separately satisfy \(E=0\). The relaxed minimizer therefore has the same \(\mathcal Z\)-value as a smooth Einstein metric. No estimate involving only \(F\), scalar energy, total Weyl energy, or \(\mathcal Z\) separates these alternatives.

### Collapse

After volume normalization, \(\mathcal Z\to0\) and bounded \(F\) do not give a Ricci lower bound, diameter control, or a Sobolev inequality. A general minimizing sequence may collapse or develop long regions. The explicit mirror sequences are macroscopically noncollapsed, but this does not control every minimizing sequence on the same smooth manifold.

A compactness theorem restricted to metrics with a uniform Sobolev constant would still be valuable, but it would describe only that controlled sector of the metric space.

### Conformal degeneration

For the positive mirror, conformal Yamabe replacement is genuinely useful. If \(g\) has positive scalar curvature and unit volume, and \(\widehat g\in[g]\) is a Yamabe metric, then
\[
Y([g])^2
\le
\left(\int s_g\,dV_g\right)^2
\le
\int s_g^2\,dV_g.
\]
Since \(\int|W|^2\) is conformally invariant,
\[
F(\widehat g)\le F(g),
\qquad
\mathcal Z(\widehat g)\le\mathcal Z(g).
\]
Thus the positive sequence can be replaced by constant-scalar-curvature minimizers without increasing the defect.

For the \(\sigma=-1\) mirror, squaring the Yamabe inequality reverses this argument. Constant-scalar-curvature normalization would instead require a perturbative maximum-principle and Bochner estimate using \(s_g=-4+o(1)\).

Both product orbifolds have volume \(8\pi^2\) and scalar curvature \(s=\pm4\), so their Yamabe values have magnitude
\[
|Y|=4\sqrt{8\pi^2}=8\sqrt2\,\pi.
\]
For comparison,
\[
Y(S^4)=8\sqrt6\,\pi.
\]
The positive product value is separated from the spherical bubbling value by the factor \(1/\sqrt3\), which may help establish uniform Yamabe compactness for the specific conformal classes.

### Noncritical minimizing sequences

Small \(\mathcal Z\) controls the size of \(E\), not its derivatives. The neck may have \(\mathcal G\) large in every \(L^p\), \(p>2\), even while \(\mathcal Z\to0\). Converting an arbitrary minimizer into a strongly almost-critical sequence while preserving Sobolev and concentration geometry is itself a fourth-order PDE problem.

### Other Einstein strata

A local analysis near the displayed \(A_1\) tree cannot exclude an Einstein metric elsewhere in the metric space, possibly with the opposite scalar sign or zero scalar curvature. Since \(\mathcal Z\) is sign-neutral, every such metric is another zero of the same functional. An obstruction argument based on \(F\) therefore needs a global compactification of the entire low-\(\mathcal Z\) set, not merely the known mirror stratum.

## 8. Two substantive routes beyond the direct method

### A. Critical-point selection plus orbifold–ALE rigidity

A strong theorem would classify exact \(\mathcal Z\)-critical sequences with
\[
\mathcal Z(g_i)\to0,\qquad C_S(g_i)\le C,\qquad \int|\mathrm{Rm}|^2\le\Lambda.
\]
The expected alternatives are:

1. eventual Einstein metrics;
2. convergence to a zero-energy orbifold–ALE tree satisfying explicit finite-dimensional stationarity equations.

The second alternative is more restrictive than merely being an approximate Einstein tree. The weighted Jacobi operators on the orbifold base and EH pieces, their kernels, and the interaction matrix would determine whether an exact fourth-order critical branch can approach the compactification stratum.

A min–max or degree construction producing exact critical metrics with levels tending to zero could then become decisive: if the finite-dimensional stationarity equations admit no tree branch, the critical metrics must be Einstein. Without such a critical-point construction, the infimum alone drifts freely into the compactification stratum.

### B. A compactified degree for the Einstein-defect map

The map
\[
g\longmapsto E_g
\]
modulo diffeomorphisms and scaling has linearization equal to the Einstein operator. One could seek a Fredholm degree on a compactified low-\(\mathcal Z\) moduli space, with contributions from smooth Einstein zeros and from orbifold–ALE strata. The positive product base appears spectrally favorable at \(\tau=-1/4\), while EH contributes known scale and rotational modes. Filling chirality may change the orientation or spectral flow of the interaction matrix.

Such a degree could in principle either force a smooth zero or account for the entire degree through compactification-stratum contributions. This requires control of every low-energy degeneration on the fixed row, not only the product degeneration, and a gluing-compatible determinant-line theory.

## 9. High-value calculations and source verification

1. **Annular gradient computation.** Apply the full ten-sector Weyl basis to \(L^*L(\chi K)\), integrate its \(L^2\) and \(L^p\) norms, and determine the exact leading constants. This would establish whether the audited metrics are natural \(L^2\)-Palais–Smale sequences.

2. **Zone-by-zone \(\mathcal Z\) asymptotics.** Compute core, log-annulus, and ambient contributions as functions of \(a,b,R\). Optimizing over \(b\) and \(R\) will show whether any renormalized energy coefficient is intrinsic or cutoff-dependent.

3. **Base spectral calculation.** Verify that the positive orbifold has no invariant TT eigenmode at \(-\Delta_L=2\), and compute the invariant Teichmüller kernel for the hyperbolic product quotient.

4. **Uniform Sobolev constants for the explicit families.** The positive family should follow from Ricci lower bounds, macroscopic volume, and diameter control. The \(\sigma=-1\) family needs a direct neck isoperimetric argument. A uniform result would place the mirror sequences inside the Tian–Viaclovsky compactness regime except for criticality.

5. **Exact-critical gap literature.** The precise search topic is: “four-dimensional critical metrics of \(\int|\operatorname{Ric}^\circ|^2\), small traceless Ricci energy, Yamabe constant, orbifold compactness.” Any theorem must be inspected for additional Weyl-energy, Bach-flatness, or pointwise curvature hypotheses.

6. **Approximate-critical regularity.** Search for “Palais–Smale sequences for quadratic curvature functionals in dimension four” and “orbifold compactness with \(L^p\) Euler–Lagrange residual.” The essential distinction is residual control at \(p>2\) versus the scale-critical \(p=2\).

7. **ALE energy threshold.** Verify whether a general Ricci-flat ALE four-manifold has a universal smallest nonzero
\[
\int|W|^2=8\pi^2\left(\chi-\frac1{|\Gamma|}\right)
\]
equal to the EH value \(12\pi^2\), or whether non-\(\mathrm{SU}(2)\) groups allow smaller values. This affects removable-singularity thresholds but not the displayed EH saturation.

In summary, \(F\)-attainment gives a precise compactified variational formulation and a natural fourth-order elliptic equation. The direct method alone lands on the already-known zero-energy orbifold–EH tree. The route becomes substantially stronger only when paired with either strong-residual compactness plus a critical-point selection mechanism, or a global degree/min–max theory that records contributions from all zero-energy compactification strata.
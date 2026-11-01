# TTCS Independent Branch Record

```json
{
  "step_id": 7,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step7_local_vs_global_rigidity.md",
    "Sessions/S0910A01/workspace/notes/step5_curvature_ratio_and_rigidity.md",
    "Sessions/S0910A01/workspace/notes/step4_near_equality_and_boundary_calibration.md"
  ]
}
```

## Task

For Yau Problem 26 (negative branch, dimension 4): we have established that a hypothetical near-pinching sequence on LeBrun blow-ups M_i = X#k_i C̄P² with δ_i→0 and k_i/A_i→1/3 satisfies:
- ∫(s+8√6|W+|)² ≤ 864π²D_a with D_a/A→0
- The local analysis on smooth Einstein pointed limits gives conformally Kähler geometry, but this does NOT contradict the calibrated Weyl profile locally
- The argument is inherently global: on compact manifolds, Stokes forces the conformal factor to be constant, giving a Kähler contradiction

The gap: making the global argument quantitative on the original compact M_i. The obstacles:
(a) The Taubes exceptional-sphere area argument requires an exact symplectic structure, not an approximate one
(b) The SW spinor defines an approximate almost-Kähler form, but dω_i ≠ 0 in general
(c) The Gromov energy quantum may degenerate as the geometry degenerates

Generate promising approaches to close this gap. Consider:
- Direct quantitative versions of LeBrun's equality exclusion (Prop 3.2) that work for near-equality
- Integer-invariant stability arguments (c₁·E_j is topological, independent of metric)
- Ricci flow approaches starting from the near-Einstein metric
- Chern-Weil identities that constrain the exceptional class areas from below
- Alternative global mechanisms that don't pass through symplectic geometry
- Whether the problem admits a counterexample construction instead

Which approach has the best chance of resolving the negative branch, and what specific mathematical steps would be needed?

## Output

For the \(4\)-dimensional \(\lambda<0\) branch, the most structurally leveraged route is **not** a quantitative Gromov energy quantum. The better target is a **compact Stokes mechanism made quantitative through LeBrun’s near-equality structure**, with Taubes used only if one can first recover an exact closed symplectic class. The reason is that the decisive exact contradiction is global and analytic:

\[
\Delta f=-\frac12 f,\qquad f>0,\qquad M\ \text{compact}
\]

is impossible by integration. If near-equality can be converted into an approximate version of this equation on the original compact \(M_i\), with flux through high-curvature/collapsed sets controlled, the calibrated conformal-Kähler noncompact escape is eliminated without needing a uniform pseudoholomorphic energy lower bound.

Below are the main promising mechanisms.

---

## 1. Quantitative compact Derdziński–Stokes mechanism

Near equality should be unpacked inside LeBrun’s proof, not only at the final inequality. Let \(w_i\) be the lowest eigenvalue of \(W_i^+\). The known remainder gives

\[
\frac1{A_i}\int (s_i+8\sqrt6 |W_i^+|)^2\,d\mu_i\to0,
\]

and Ricci pinching gives \(s_i\to -4\). Hence

\[
|W_i^+|\to \frac1{2\sqrt6}
\quad\text{in normalized }L^2.
\]

The internal slack in the step

\[
w\ge -\sqrt{\frac23}|W^+|
\]

should further give

\[
w_i+\sqrt{\frac23}|W_i^+|\to0
\quad\text{in normalized }L^2,
\]

so the Weyl eigenvalues approach

\[
\left(-\frac16,\frac1{12},\frac1{12}\right).
\]

Thus on the good region the lowest eigenspace of \(W_i^+\) is separated by a fixed spectral gap. One obtains a well-defined local eigenline \(L_i\subset \Lambda_i^+\), with unit section \(\omega_i\) after choosing sign locally.

For an exact Einstein metric with this two-eigenvalue profile, Derdziński gives a conformal Kähler form and a positive factor \(f\) satisfying

\[
\Delta f=-\frac12 f.
\]

The quantitative target is therefore a weak equation of the form

\[
\Delta f_i+\frac12 f_i=\rho_i
\]

on the good region, with

\[
\frac1{A_i}\|\rho_i\|_{H^{-1}\ \text{or}\ L^1}\to0,
\qquad
\int f_i\,d\mu_i\ge cA_i.
\]

Then compact integration gives the contradiction:

\[
\frac12\int f_i
=
-\int \Delta f_i+\int \rho_i
\approx 0,
\]

while \(\int f_i\sim A_i\).

The hard part is flux through the complement of the good region. This suggests a capacity formulation. If \(S_i\) denotes the high-curvature / bad-eigenvalue / bad-harmonic-radius set, choose cutoffs \(\chi_i\) with \(\chi_i=1\) away from \(S_i\). Testing gives

\[
\frac12\int \chi_i f_i
=
-\int \langle \nabla \chi_i,\nabla f_i\rangle
-\int \chi_i\rho_i.
\]

A useful theorem would show

\[
\|\nabla \chi_i\|_{L^2}^2=o(A_i),
\qquad
\|\nabla f_i\|_{L^2}^2=O(A_i),
\]

so the flux term is \(o(A_i)\). This is exactly where Cheeger–Naber codimension-four control can enter: if the bad set consists of \(O(A_i)\) many small curvature-concentration cores, its normalized capacity can still tend to zero after choosing the tubular radius small.

This route directly attacks the compact/noncompact distinction: noncompact pointed limits allow eigenfunctions with \(\Delta f=-f/2\); compact manifolds do not, unless all mass escapes through sets of substantial capacity. The desired theorem is therefore a **removable compact Stokes theorem for the near-Derdziński factor**.

Specific mathematical work needed:

1. Decompose LeBrun’s Prop. 2.3 and Prop. 3.1 proof into explicit slack terms:
   \[
   s+8\sqrt6|W^+|,\quad
   w+\sqrt{2/3}|W^+|,\quad
   \Pi_{L^\perp}\sigma(\Phi),\quad
   \text{conformal-minimization slack}.
   \]

2. Prove these slacks are \(o(A_i)\) for every near-pinching sequence with \(k_i/A_i\to1/3\).

3. On noncollapsed harmonic-radius balls, derive the finite-\(i\) approximate Derdziński equation by passing through the smooth Einstein blow-up calculation.

4. Patch the local factors \(f_i\) across the good region using the spectral gap of the lowest \(W^+\)-eigenline.

5. Prove the capacity-flux estimate through the complement.

If this works, it bypasses the need for exact symplectic geometry and also explains precisely why local conformal-Kähler geometry is harmless on pointed noncompact limits but impossible on the original compact sequence.

---

## 2. Exact cohomology route using harmonic self-dual forms

A second promising route is to avoid the nonclosed SW quadratic form and instead use the exact closed form already present in the Hodge decomposition.

For a monopole class \(a_\varepsilon\), let

\[
\Omega_\varepsilon=2\pi\,a_\varepsilon^+
\]

be its harmonic self-dual representative. This form is closed. In exact equality, \(\Omega_\varepsilon\) becomes the almost-Kähler form. Near equality should force \(\Omega_\varepsilon\) to be close, in a strong sense, to the calibrated lowest-eigenline form.

The key theorem shape would be:

> If \(\Omega\) is a closed self-dual harmonic form with \([\Omega]^2>0\), and LeBrun near-equality plus Ricci pinching force \(|\Omega|\) to be almost constant and aligned with the lowest \(W^+\)-eigenline outside a set of small capacity, then \(\Omega+d\alpha\) can be made symplectic in the same cohomology class.

Then LeBrun’s sign trick becomes decisive. For a suitable exceptional class \(E_j\), one obtains

\[
[\Omega]\cdot E_j=a_\varepsilon^+\cdot E_j\le 0.
\]

But if \(\Omega+d\alpha\) is symplectic in the same class, Taubes gives a pseudoholomorphic representative of \(E_j\) with area

\[
\int_{E_j}(\Omega+d\alpha)=[\Omega]\cdot E_j>0,
\]

contradicting the sign.

The important point is that this route does **not** require a uniform positive energy quantum. The cohomology pairing has the wrong sign exactly. The missing ingredient is stronger: near-equality must force an exact symplectic representative in the same class.

Specific mathematical work needed:

1. Show that LeBrun near-equality controls the harmonic representative \(a_\varepsilon^+\), not only the SW spinor quadratic form.

2. Prove an \(L^\infty\), capacity, or near-symplectic replacement theorem for \(\Omega_\varepsilon\).

3. Use Taubes only after the cohomology class is genuinely symplectic.

This is conceptually close to LeBrun Prop. 3.2 and preserves the integer/topological sign exactly.

---

## 3. Multi-monopole integer-flux mechanism

Because all sign choices

\[
a_\varepsilon=c_1(X)+\sum_j \varepsilon_j E_j
\]

are monopole classes, and near equality forces

\[
(a_\varepsilon^+)^2=A_i+o(A_i)
\]

for many signs, one should exploit simultaneous near-saturation.

For two signs differing only at \(E_j\), the difference of the corresponding spin\(^c\) connections represents \(2E_j\). Thus its curvature has an integral period:

\[
\frac{i}{2\pi}\int_{E_j}(F_{A_\varepsilon}-F_{A_{\varepsilon'}})=\pm 2.
\]

Near equality should force the self-dual parts of these curvatures to align with the same calibrated eigenline. Hence the integer flux must be carried either by anti-self-dual curvature or by concentration regions.

A possible global packing estimate is:

\[
\sum_{j=1}^{k_i}\text{integer flux carried by }E_j
\lesssim
\text{capacity of bad set}
+
\text{normalized LeBrun slack}.
\]

Since \(k_i\sim A_i/3\), a bad set with \(o(A_i)\) effective capacity cannot carry all exceptional fluxes.

This route has real content because integer periods cannot disappear under perturbation. Its weak point is that abelian anti-self-dual curvature can naturally carry \(E_j^2=-1\) at \(O(1)\) energy per class, and the signature identity already allows substantial \(W^-\)-energy. Thus the flux argument must be tied to the calibrated \(W^+\) eigenline or to SW spinor lower bounds; integrality alone is not enough.

---

## 4. Ricci flow as a smoothing auxiliary

The normalized flow

\[
\partial_t g=-2(\operatorname{Ric}+g)
\]

is attractive because the initial velocity is \(o(1)\) in \(C^0\). If one could flow for a uniform time while keeping the LeBrun slack \(o(A_i)\), derivative control would improve, and the approximate Derdziński–Stokes route would become much cleaner.

The needed estimates would be:

\[
\|\operatorname{Ric}_{g(t)}+g(t)\|_{C^0}=o(1),
\qquad
\frac1{A_i}D_a(g(t))\to0,
\qquad
t\in[0,t_0].
\]

However, this is difficult as a standalone method because \(W^-\) and full curvature may concentrate while Ricci remains pinched. Short-time smoothing without noncollapse is delicate. Ricci flow looks most useful as a local regularization device on harmonic-radius regions, not as the main global engine.

---

## 5. Chern–Weil charge localization on exceptional caps

Another route is to avoid symplectic geometry and localize topology directly. For a tubular region \(N\) carrying one exceptional handle, Chern–Weil with transgression gives

\[
\frac1{4\pi^2}\int_N
\left(2|W^+|^2+\frac{s^2}{24}-\frac{|E|^2}{2}\right)
+
T_+(\gamma,\mathrm{II})
=
2\chi(N)+3\tau(N).
\]

For an \(O(-1)\to S^2\) cap,

\[
2\chi+3\tau=1.
\]

Near pinching fixes \(s\approx -4\). Near LeBrun equality fixes

\[
|W^+|\approx \frac1{2\sqrt6}.
\]

Thus each exceptional handle must realize a very specific Chern–Weil charge while keeping the curvature-ratio remainder

\[
\int_N(s+8\sqrt6|W^+|)^2
\]

small.

This suggests a concrete cap optimization problem:

\[
\inf
\int_N(s+8\sqrt6|W^+|)^2
\]

over metrics on \(O(-1)\) disk bundles satisfying

\[
\|\operatorname{Ric}+g\|_{op}\le\delta
\]

and prescribed interface first/second fundamental forms. If this infimum has a positive lower value per exceptional handle for all matchable interface data, then summing over \(k_i\sim A_i/3\) contradicts the global \(o(A_i)\) remainder.

The Taub–Bolt–AdS computation is valuable here: it shows exact Ricci caps exist for some interface data, so the functional must measure the calibrated Weyl-ratio cost, not just Ricci defect. A decisive figure would plot attainable interface data colored by

\[
\int(s+8\sqrt6|W^+|)^2
\]

and by the Chern–Simons transgression values.

This approach is computationally and geometrically concrete, but proving a universal cap lower bound over arbitrary metrics is hard.

---

## 6. Counterexample construction route

A counterexample sequence would need to satisfy all of the already-forced equalities:

\[
\|\operatorname{Ric}+g\|_{op}\to0,
\qquad
\frac1{A_i}\int(s+8\sqrt6|W^+|)^2\to0,
\qquad
k_i/A_i\to1/3.
\]

Thus it cannot look like a product hyperbolic collapse or a Kähler-Einstein region, because those have the wrong \(W^+\)-profile.

A viable construction would need one of the following:

1. **Corrected ALE blowup:** an \(O(t^2)\) relative correction to the scaled Ricci-flat core producing order-one \(\operatorname{Ric}\approx -g\), with the first obstruction vanishing and the transition error \(o(1)\) in operator norm.

2. **Exact \(\lambda<0\) caps:** local Einstein fillings with \(O(-1)\) topology whose interface data match the exterior and whose \(W^+\)-profile has small calibrated remainder.

3. **Derdziński-type conformally Kähler pieces:** noncompact Einstein pieces with \(\Delta f=-f/2\), calibrated \(|W^+|\), and compactifiable interfaces through which the Stokes flux can escape.

The observable test is per-handle cost:

\[
\mathcal E_{\text{cap}}
=
\int_{\text{cap}}(s+8\sqrt6|W^+|)^2.
\]

If every exceptional handle costs \(\ge \eta>0\), then \(k_i\sim A_i\) gives total cost \(\ge \eta A_i\), impossible. If a family has \(\mathcal E_{\text{cap}}\to0\) while matching exterior data, it becomes a serious counterexample mechanism.

---

## Most promising resolution path

The strongest proof-oriented route is:

\[
\boxed{
\text{LeBrun slack decomposition}
\Longrightarrow
\text{approximate Derdziński factor}
\Longrightarrow
\text{compact Stokes with capacity control}.
}
\]

It attacks the actual global mechanism responsible for the exact contradiction and avoids dependence on a uniform pseudoholomorphic area quantum.

A close second is the harmonic self-dual cohomology route:

\[
\boxed{
a_\varepsilon^+\ \text{closed}
\Longrightarrow
\text{same-class symplectic representative}
\Longrightarrow
a_\varepsilon^+\cdot E_j\le0
\ \text{contradicts Taubes}.
}
\]

This route is elegant because the exceptional pairing sign is exact; the hard theorem is the same-class symplectic replacement from near-equality.

For a counterexample, the most concrete route is the cap/interface program: find calibrated \(\lambda<0\) exceptional caps with vanishing per-handle Weyl-ratio cost and matchable Cauchy data. Existing Taub–Bolt–AdS caps show Ricci defect alone is the wrong functional; the decisive quantity is the calibrated LeBrun remainder.
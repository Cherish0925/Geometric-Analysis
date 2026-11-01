# TTCS Independent Branch Record

```json
{
  "step_id": 49,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A02/workspace/notes/step49_positive_branch_wall_and_operator_norm.md",
    "Sessions/S0910A02/workspace/data/step49_operator_norm_and_enumeration.json",
    "Sessions/S0910A02/workspace/notes/step48_H4dual_and_biKahler_realizability.md",
    "Sessions/S0910A02/workspace/notes/step45_preceptor_review_biKahler_loophole.md",
    "Knowledge/objects/papers/The-Calabi-metric-and-desingularization-of-Einstein-orbifolds--3b9fd6e4b2cd--c8fe6b2cf08c/object.md",
    "Knowledge/objects/papers/Higher-order-obstructions-to-the-desingularization-of-Einstein-metrics--94f76f3b5378--19c12fb27fae/object.md",
    "Knowledge/objects/papers/Desingularizations-of-Conformally-Kaehler-Einstein-Orbifolds--8fe1aa31deb8--5b19d560b771/object.md"
  ]
}
```

## Task

Verify the Step 49 correction for the Yau-26 positive noncollapsed route. Read the Step 49 note and supporting data/sources. Check: (i) whether the scaling from MV/Ozuch refined estimates really shows that after the first obstruction term t*lambda*o is killed, the glued approximate metrics have ||Ric-Lambda g||_op = O(t^{1/2}) on the four-dimensional EH/Calabi replacement, while second/higher obstruction residuals are invisible to C^0 operator pinching; (ii) whether the H4_dual compactness obstruction must be formulated as the normalized boundary flux B/t_i^2 with quantitative two-scale matching, not the unnormalized B; (iii) whether the finite product-quotient orientation enumeration and known-Einstein/mixed-row status are stated with correct caveats. Identify any mathematical errors, hidden assumptions, or needed repairs that would change the route allocation. Do not invent external facts; if a needed source is absent, say exactly what source should be retrieved.

## Output

# Scientific verification memo

## 1. Refined EH scaling and \(C^{0}\) Ricci pinching

The central scaling correction in Step 49 is mathematically sound for the explicit first-refined gluing construction.

Let \(t\) denote the **metric scale**, so that the inserted core metric is comparable to \(t\,g_{\mathrm{EH}}\) and the attaching map is \(z=\sqrt t\,x\). The refined local estimate has the form
\[
\left|
\operatorname{Ric}_{g_t}-\Lambda g_t
-t\sum_k\lambda_k\chi_t\,o_k
\right|_{g_{\mathrm{EH}}}
\le C t^2\rho^2 ,
\]
with \(\rho\le 2t^{-1/4}\). Metric positivity and uniform comparability follow from
\[
|t h_2|_{g_{\mathrm{EH}}}\le Ct\rho^2\le Ct^{1/2},
\qquad
C^{-1}t g_{\mathrm{EH}}\le g_t\le Ct g_{\mathrm{EH}}.
\]
For a \((0,2)\)-tensor, changing from \(g_{\mathrm{EH}}\) to \(t g_{\mathrm{EH}}\) multiplies its endomorphism norm by \(t^{-1}\). Consequently,
\[
\left\|g_t^{-1}
\left(\operatorname{Ric}_{g_t}-\Lambda g_t
-t\sum_k\lambda_k\chi_t o_k\right)
\right\|_{\mathrm{op}}
\le Ct\rho^2
\le Ct^{1/2}.
\]
The transition annulus \(\rho\asymp t^{-1/4}\) is exactly where the maximum \(Ct^{1/2}\) occurs. The orbifold exterior is unchanged and Einstein, so its contribution is zero. For finitely many disjoint replacements, the same estimate holds with a larger constant depending on the fixed orbifold and fixed attaching data.

If some \(\lambda_k\neq0\), then on a fixed EH core
\[
\left\|g_t^{-1}\!\left(t\sum_k\lambda_k o_k\right)\right\|_{\mathrm{op}}
\asymp
\left|\sum_k\lambda_k o_k\right|_{g_{\mathrm{EH}}},
\]
which is order one. Finite-dimensional norm equivalence gives a uniform lower estimate after fixing unit directions. Thus the first vector coefficient is visible in the Yau–26 norm.

If all \(\lambda_k=0\), the displayed \(Ct^{1/2}\) estimate already follows without solving the second or later exact Einstein equations. A second obstruction term \(t^2\mu_k o_k\) has core endomorphism size \(O(t)\); more generally, a mode coefficient \(t^q\) has core size \(O(t^{q-1})\). The decay \(o_k=O(\rho^{-4})\) makes these terms smaller in the transition region. Therefore later Ozuch coefficients do not prevent the explicitly constructed metrics from satisfying
\[
\sup_M\left\|g_t^{-1}
(\operatorname{Ric}_{g_t}-\Lambda g_t)\right\|_{\mathrm{op}}
\longrightarrow0.
\]

Two qualifications are important.

1. The phrase “complete local condition” is stronger than the supplied analysis establishes. The source material proves that \(R_\varepsilon(p)\zeta=0\) is sufficient for this explicit first-refined ansatz. Its necessity for every possible \(C^0\)-Ricci-pinched EH degeneration still depends on the normalized two-scale theorem discussed below.

2. The formula “a \(q\)-th obstruction gives \(t^{q-1}\)” is directly justified for obstruction tensors proportional to the EH Jacobi modes. Higher correction tensors may have other \(\rho\)-profiles. This does not affect the main conclusion because the first-refined metric, before constructing the later tower, already has the uniform \(O(t^{1/2})\) Ricci defect.

### Source adequacy

The Morteza–Viaclovsky Lemma 4.2 passage supports the scaling computation exactly, but that paper’s principal compact statements use complex dimension \(n\ge3\), where the Calabi obstruction space is one-dimensional. EH in real dimension four has three rotational/scale modes. MV alone therefore does not source the four-dimensional vector statement needed for kernel directions \(e_2,e_3\).

Ozuch’s supplied lines do provide the necessary EH ingredients:
\[
P_{\mathrm{EH}_\zeta}\underline h_2
=\Lambda\,\mathrm{EH}_\zeta+\sum_k\lambda_k(\zeta)o_k(\zeta),
\qquad
\lambda_k=c\langle R^\pm(H_2)\zeta,\zeta_{(k)}\rangle,
\]
together with the improved asymptotics when all \(\lambda_k=0\). What is not displayed as a single theorem in the excerpts is the direct ungauged Ricci estimate
\[
|\,\operatorname{Ric}-\Lambda g\,|_{g_{\mathrm{EH}}}
\le Ct^2\rho^2
\]
for the resulting four-dimensional cutoff metric. It follows by the same Taylor and cutoff calculation as MV, but an independently citable presentation would require the corresponding passage from Biquard’s *Désingularisation de métriques d’Einstein I*, especially its refined construction and Section 14 estimates, or the full local estimate surrounding Ozuch’s approximate metric \(g_{\zeta,v}^{A}\).

After fixing the chirality assignment and attaching maps, changing \(t\) only changes radii through isotopy. Thus the metric family lives on one fixed smooth manifold \(M_\varepsilon\), not on a topology varying with \(t\). The notation \(M_{\varepsilon,t}\) in Step 49 obscures this point.

## 2. Normalization of the H4-dual spherical flux

The normalization by the square of the **length scale** is necessary to recover the ambient curvature coefficient.

Let \(\epsilon_i\) be the EH length scale and write
\[
\widetilde g_i=\epsilon_i^{-2}g_i
=g_{\mathrm{EH}}+h_i .
\]
In a quantitatively matched gauge, the ambient quadratic term has size
\[
h_i=\epsilon_i^2 H_2+o(\epsilon_i^2)
\]
on a fixed large EH annulus. For
\[
\mathcal B_k(R,i)
=\frac12\int_{\{\rho=R\}}
\left(
\langle\nabla_\nu h_i,o_k\rangle
-\langle h_i,\nabla_\nu o_k\rangle
\right)d\sigma ,
\]
one has \(H_2=O(R^2)\), \(\nabla H_2=O(R)\), \(o_k=O(R^{-4})\), \(\nabla o_k=O(R^{-5})\), and \(d\sigma=O(R^3)\). Both Wronskian terms are therefore \(O(\epsilon_i^2)\). Hence
\[
\epsilon_i^{-2}\mathcal B_k(R,i)
\]
is the quantity with a finite curvature-dependent limit. For fixed \(R\), ordinary \(C^{1,\alpha}\) convergence gives \(h_i\to0\) and therefore only
\[
\mathcal B_k(R,i)\to0,
\]
which contains no information about \(H_2\).

The Ricci-defect scaling is also correct. If
\[
\|\operatorname{Ric}_{g_i}-\Lambda g_i\|_{\mathrm{op},g_i}
\le\delta_i,
\]
then in the rescaled metric
\[
\left|
\operatorname{Ric}_{\widetilde g_i}
-\Lambda\epsilon_i^2\widetilde g_i
\right|_{\widetilde g_i}
\le \epsilon_i^2\delta_i .
\]
Since \(\int_{\rho\le R}|o_k|=O(1+\log R)\),
\[
\left|\int_{\rho\le R}
\left\langle
\operatorname{Ric}_{\widetilde g_i}
-\Lambda\epsilon_i^2\widetilde g_i,o_k
\right\rangle
\right|
\le C\epsilon_i^2\delta_i(1+\log R).
\]
After normalization, the relative contribution is
\[
O\!\left(\delta_i(1+\log R)\right),
\]
which vanishes when \(i\to\infty\) for fixed \(R\), followed by \(R\to\infty\).

The cutoff commutator cannot be discarded after this normalization. On \(\rho\asymp R\),
\[
h_i=O(\epsilon_i^2R^2),
\qquad
[P,\chi_R]o_k=O(R^{-6}),
\qquad
\operatorname{Vol}(A_{R,2R})=O(R^4),
\]
so its integral is \(O(\epsilon_i^2)\). Dividing by \(\epsilon_i^2\) leaves an order-one term, precisely the cutoff representation of the Wronskian.

The genuinely unresolved analytic statement is therefore an expansion at relative precision \(o(\epsilon_i^2)\), not merely convergence to EH. It requires:

- compatible harmonic/Bianchi gauges on both scales;
- modulation removing EH scale, rotational Jacobi modes, and pure diffeomorphism modes;
- exclusion or explicit treatment of intermediate bubbles;
- \(C^1\) control of
  \[
  \epsilon_i^{-2}h_i-H_2
  \]
  on fixed large annuli;
- identification of the limiting Wronskian with
  \[
  c\langle R_\varepsilon(p)\zeta,\zeta_{(k)}\rangle .
  \]

There is also a notation inconsistency in Step 49: Section 1 uses \(t\) as metric scale, whereas the H4 discussion uses \(t_i^2\) as the signal size, meaning \(t_i\) is a length scale. A uniform notation such as \(t=\epsilon^2\) removes the ambiguity.

## 3. Product-quotient arithmetic and topology

### Diagonal \(\mathbb Z_2\) quotient

The numerical table is correct. The underlying quotient has
\[
\chi_{\mathrm{top}}
=\frac{\chi(S^2\times S^2)+\chi(\operatorname{Fix}\sigma)}2
=\frac{4+4}{2}=4.
\]
Replacing four cone points by EH disk bundles adds one to Euler characteristic at each point, giving \(\chi=8\). Rationally, the quotient contributes one positive and one opposite-sign class. If \(r\) insertions contribute \(+2\) exceptional classes and \(4-r\) contribute \(-2\) classes, then
\[
(b_+,b_-)=(1+r,5-r),\qquad \tau=2r-4.
\]
Thus all five rows in Step 49 are arithmetically correct.

The topology qualifications can be sharpened:

- For \(r=1,3\), the intersection form must be odd: an even unimodular form cannot have signature \(\mp2\). Their exact smooth types are still not established by the supplied material.
- For \(r=2\), signature zero permits either the odd form \(I_{3,3}\) or the even form \(3H\). Spin/evenness remains unresolved.
- Armstrong’s theorem supports simple connectedness of the quotient, but the van Kampen passage through the four \(\mathbb{RP}^3\) attaching hypersurfaces should still be written explicitly before invoking Freedman-type identifications.

For \(r=0\), the complex minimal resolution is a rational weak degree-4 del Pezzo surface; its complex structure contains \((-2)\)-curves, so it need not itself be Kähler–Einstein. What matters here is the smooth diffeotype, expected to be
\[
\mathbb{CP}^2\#5\,\overline{\mathbb{CP}}^{\,2},
\]
which carries a positive Einstein metric in some unrelated complex structure. The LeBrun–Ozuch source supports Einstein existence once the Del Pezzo diffeotype is established, but it does not by itself identify this particular quotient resolution. A toric fan computation, rational-surface argument, or Kirby diagram is the missing direct source passage. The \(r=4\) row is the orientation-reversed counterpart.

### Diagonal \(V_4\) quotient

The count of six \(A_1\) points is correct: each of the three nontrivial half-turns fixes four points in the product, giving twelve cover points with stabilizer \(C_2\), hence six quotient orbits. The quotient again has Euler characteristic \(4\), and resolving six points gives \(\chi=10\). Therefore
\[
(b_+,b_-)=(1+r,7-r),\qquad \tau=2r-6
\]
is correct.

The balanced row \(r=3\) has \((4,4)\); its parity and smooth type are unresolved. Every other mixed row has signature \(\pm2\) or \(\pm4\), which already forces an odd intersection form, though not a standard smooth connected-sum identification. The all-one-chirality endpoint is expected to have the degree-2 Del Pezzo diffeotype, but the supplied files do not contain the required quotient-resolution computation.

No supplied source establishes either Einstein existence or Einstein nonexistence for any mixed row. Describing them as unresolved in the session record is accurate; describing them as known examples without Einstein metrics would not be supported.

### Finite graph-action calculation

The modular-weight argument is correct under its stated assumptions. For a cyclic stabilizer of order \(m\), endpoint choices produce weights \((1,a)\) and \((1,-a)\). Requiring both to lie in \(SU(2)\) gives
\[
1+a\equiv0,\qquad 1-a\equiv0\pmod m,
\]
hence \(m\mid2\). A finite rotation group in \(SO(3)\) with no stabilizer order above two is \(C_2\) or \(V_4\). Thus the all-ADE graph-action list is finite. This does not include factor exchanges or actions with noninjective projections, exactly as Step 49 records.

## 4. Scientific consequence

The main Step 49 correction is valid:

- killing the vector first obstruction produces explicit smooth metrics with \(C^0\) Ricci endomorphism defect \(O(t^{1/2})\);
- later exact-Einstein obstruction coefficients do not obstruct these approximate pinched families;
- the unnormalized spherical flux cannot recover the first coefficient;
- necessity of \(R_\varepsilon(p)\zeta=0\) for arbitrary pinched EH degenerations still rests on the quantitative normalized matching theorem;
- the orientation tables are correct, while mixed smooth types and endpoint quotient identifications require additional topology;
- none of the mixed rows presently yields a Yau–26 refutation without a theorem excluding Einstein metrics of every sign on the actual glued smooth manifold.
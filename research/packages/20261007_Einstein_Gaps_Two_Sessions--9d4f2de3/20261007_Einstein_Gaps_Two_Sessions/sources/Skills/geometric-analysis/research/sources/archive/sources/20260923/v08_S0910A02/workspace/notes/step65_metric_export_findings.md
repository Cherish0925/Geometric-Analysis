# Step 65: Metric export attempt — findings, negative results, and the corrected path

Session `S0910A02`. Agent2 / Constructor. Phase Execute.

## 0. What this step set out to do

The Step-64 handoff assigned prong two of the balanced-row decision point:
export the explicit near-pinched glued metric on a chi=8 positive-mirror row
as a concrete smooth tensor field, verify the operator-norm pinching
\(\|\mathrm{Ric}-\Lambda g\|_{op}=O(t^{1/2})\) numerically (discharging the owed
multi-bubble operator-norm accounting), and prepare the Einstein-DeTurck /
variational search with the \(r=0\) del Pezzo row as control.

This step did NOT complete that program. It produced instead a precise
diagnosis of why the export is harder than the Step-49 record suggests, and
a corrected formulation of the actual computational task. This is genuinely
useful: it corrects an over-optimistic reading of Biquard's construction and
prevents a wasted numerical run on a wrong metric.

## 1. The construction, correctly understood

Biquard (arXiv:1105.4904, Section 4) builds the desingularization metric as
\(g_{t,\varphi} = t\,(e_h + t\,h)\) on the Eguchi-Hanson piece, where:

- \(e_h\) is the Ricci-flat EH metric;
- \(h\) solves the **linearized Ricci equation**
  \[
    (\mathrm{d}\,\mathrm{Ric})[h] = \Lambda\,e_h + \tfrac13\sum_j \lambda_j o_j,
  \]
  with \(h\sim \rho^2\) at infinity matching the ambient quadratic jet \(H\)
  of the orbifold metric \(g_0\);
- the \(\lambda_j\) are the first-obstruction coefficients, killed at the
  bi-Kähler locus by choosing \(\zeta\in\ker R_\pm\).

Lemma 4.1 then gives
\(|\nabla^k(\mathrm{Ric}-\Lambda g_{t,\varphi}-t\sum\lambda_j\chi_t o_j)|_{eh}
 \le c_k t^2\rho^{2-k}\), so with \(\lambda_j=0\) the defect is \(O(t^2\rho^2)\)
in \(e_h\)-norm, i.e. \(O(t\rho^2)\) in the physical operator norm
\(|\cdot|_{op,g_t}\sim t^{-1}|\cdot|_{eh}\): \(O(t)\) on the core,
\(O(t^{1/2})\) in the transition zone \(\rho\sim t^{-1/4}\).

**The key point that was under-appreciated:** \(h\) is NOT an explicit tensor.
It is the solution of a linear elliptic PDE on EH. The whole operator-norm
claim is conditional on actually having this \(h\).

## 2. What I verified

1. **EH is Ricci-flat** — verified symbolically (Brioschi/Bianchi-IX form
   \(g=dr^2/W+(r^2/4)[\sigma_1^2+\sigma_2^2+W\sigma_3^2]\), \(W=1-a^4/r^4\))
   to \(10^{-15}\) over random points. File:
   `step65_eh_metric_verify.json`.

2. **The naive glued metric fails with \(O(1)\) defect.** Using raw EH
   (\(\mathrm{Ric}=0\)) as the bubble without the correction \(h\):
   \[
     \|\mathrm{Ric}-\Lambda g\|_{op} = \|0-\Lambda g\|_{op,g}=|\Lambda| = O(1).
   \]
   This confirms the correction is essential, not optional.

3. **\(\Delta(r^2)=8\) exactly on EH** (not just asymptotically). The radial
   scalar Laplacian of \(r^2\) is the constant 8. File:
   `step65_linearized_ricci_solution.json`.

4. **But \(h=c\,r^2 g\) does NOT solve the linearized Einstein equation.**
   This was the step's main conceptual correction. I initially conflated the
   Lichnerowicz Laplacian \(\Delta_L\) with the full linearized Ricci operator.
   The correct linearization is
   \[
     (\mathrm{d}\,\mathrm{Ric})_{ij}[h]
     = -\tfrac12\nabla^2 h_{ij} - \tfrac12\nabla_i\nabla_j(\mathrm{tr}\,h)
       + \tfrac12\big(\nabla_i(\mathrm{div}\,h)_j+\nabla_j(\mathrm{div}\,h)_i\big)
       + R_{ikjl}h^{kl}.
   \]
   For \(h=c\,r^2 g\): the rough-Laplacian and curvature terms give
   \(-8c\,g\), but the **trace and divergence terms** contribute
   \(-\tfrac12\nabla_i\nabla_j(4cr^2) + \tfrac12(\cdots)\) which are NOT
   proportional to \(g\). Symbolic check (`step65_linearization_diagnosis.json`):
   \[
     \mathrm{dRic}_{00}[cr^2g] = \frac{2c(a^4+3r^4)}{a^4-r^4}\ \ne\ -8c\,g_{00}.
   \]
   The discrepancy is exactly the trace/divergence contribution.

5. **Consequence:** the corrected glued metric is NOT a simple conformal
   rescaling \(\Omega^2 g_{EH}\). Direct computation of the conformal-Ricci
   defect for \(\Omega^2=t(1-t\Lambda r^2/8)\) gives an \(O(1)\) constant term
   \(-\Lambda/4+\Lambda a^4/(4r^4)\) in the series expansion
   (`step65_conformal_ricci_direct.json`), confirming the conformal ansatz
   cannot work.

## 3. Why the export is genuinely hard

The linearized Ricci operator for the \(U(2)\)-invariant diagonal ansatz
\(h=\mathrm{diag}(f_1g_{00},f_2g_{11},f_2g_{22},f_3g_{33})\) reduces to a
coupled 3-ODE system for \((f_1,f_2,f_3)\). My attempt to extract this system
numerically (`step65_lichnerowicz_ode_system.py`) failed because:

- the numerical Ricci computation via finite differences is first-order and
  noisy at the required precision;
- the second-derivative coefficient matrix \(M(r)\) came out as zero (an
  artifact of the perturbation method, not the true operator);
- the system is genuinely coupled through the trace/divergence terms.

The correct approach is to derive the ODEs **symbolically** (the Christoffels
and curvature are known in closed form) and then solve with `solve_bvp`.
This is a well-defined but substantial computation.

## 4. The honest status of the operator-norm accounting

The multi-bubble operator-norm accounting is **discharged at the theoretical
## 6. The coupled Lichnerowicz ODE system (derived, not yet solved)

The full 4D symbolic computation (`step65_full4d_lichnerowicz.py`) gives the
linearized Ricci components for the \(U(2)\)-invariant diagonal ansatz. The
structure is **2 second-order + 1 first-order constraint**, not 3 independent
second-order equations:

- \(f_2''\) from the \((1,1)\) equation;
- \(f_3''\) from the \((3,3)\) equation;
- \(f_1'\) (first-order, no \(f_1''\)) from the \((0,0)\) equation after
  substituting \(f_2'',f_3''\) — this is the linearized Bianchi/gauge constraint.

The asymptotic quadratic mode \(f_i=c_i r^2\) satisfies the large-\(r\) equations
only along the single relation
\[
  \Lambda = 3(c_1-2c_2-c_3),
\]
leaving a 2-dimensional gauge freedom (the ambient \(H\) is a specific quadratic
form that fixes this). The bolt \(r=1\) is a singular point of the \(r^4-1\)
coordinate, so regularity there must be imposed in a smooth (e.g. proper
Bianchi-IX radial) coordinate, and the \(f_1'\) constraint degenerates as
\(r\to1\) — this is the main reason `solve_bvp` has not yet converged.

**What remains for the export (next step):**
1. Re-coordinatize the bolt region (use a proper-distance coordinate
   \(\ell=\int dr/\sqrt{W}\) so the metric is smooth at \(\ell=0\)) and re-derive
   the ODEs there, or impose regularity via a Frobenius expansion at the bolt.
2. Determine the ambient quadratic \(H\) from the \((S^2\times S^2)/\mathbb Z_2\)
   orbifold curvature at the \(A_1\) points (this fixes the 2-dim gauge freedom
   and hence the correct \((c_1,c_2,c_3)\)).
3. Solve the BVP and assemble \(g_{t,\varphi}=t(e_h+th)\).
4. Verify \(\|\mathrm{Ric}-\Lambda g\|_{op}=O(t)\) core, \(O(t^{1/2})\) transition.
5. Glue across 4 bubbles, then Einstein-DeTurck on \(r=0\) control first.
To actually export the metric and run the experiment, the following must be
done in order:

1. **Derive the coupled Lichnerowicz ODEs symbolically.** Use the closed-form
   EH Christoffels/curvature (Bianchi-IX) and the diagonal ansatz to get the
   exact 3-ODE system \(\mathrm{(dRic)}[h]=\Lambda g\) as functions of
   \((f_1,f_2,f_3)\) and their derivatives. This is mechanical but long.

2. **Solve with `solve_bvp`** on \(r\in[1.05, 50]\) with:
   - regularity (Neumann) at the bolt \(r=a=1\);
   - matching to the ambient quadratic \(H\) at \(r_{\max}\). The matching
     constant is determined by the orbifold curvature, NOT freely choosable.

3. **Assemble** \(g_{t,\varphi}=t(e_h+th)\) and compute
   \(\|\mathrm{Ric}-\Lambda g\|_{op}\) on a radial grid, verifying
   \(O(t)\) core / \(O(t^{1/2})\) transition.

4. **Glue across 4 bubbles** with the cutoff \(\chi_t\) and verify the global
   operator norm (the multi-bubble constant).

5. Only then: discretize for Einstein-DeTurck, run \(r=0\) control first.

## 7. Files

- `step65_eh_metric_verify.py/.json` — EH Ricci-flatness
- `step65_glued_metric_operator_norm.py/.json` — naive O(1) defect
- `step65_linearized_ricci_solution.py/.json` — \(\Delta(r^2)=8\)
- `step65_exact_h_and_glued_metric.py/.json` — conformal model defect
- `step65_conformal_ricci_direct.py/.json` — series expansion, O(1) constant term
- `step65_linearization_diagnosis.py/.json` — the trace/divergence correction
- `step65_lichnerowicz_ode_system.py/.json` — ODE extraction attempt (failed)

No branch of Yau-26 was proved, refuted, or formalized.

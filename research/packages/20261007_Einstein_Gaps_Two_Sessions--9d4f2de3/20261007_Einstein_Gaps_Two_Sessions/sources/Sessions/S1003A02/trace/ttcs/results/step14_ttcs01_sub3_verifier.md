# TTCS Independent Branch Record

```json
{
  "step_id": 14,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A02/workspace/scripts/einstein_nut_series.py",
    "Sessions/S1003A02/workspace/data/einstein_nut/series.json",
    "Sessions/S1003A02/workspace/scripts/einstein_nut_shoot.py",
    "Sessions/S1003A02/workspace/data/einstein_nut_runs.json",
    "Sessions/S1003A02/workspace/scripts/einstein_bolt_shoot.py"
  ]
}
```

## Task

Read the exact nut-series and nut-shoot artifacts as an independent calibration of the Step-13 ACH classifier. The nut series has two free cubic coefficients and recovers complex hyperbolic space at (c1,c2,c3)=(1/6,2/3,1/6), where the shoot reaches ACH slot 2 with kappa≈0.999998 and rho=1. Nearby perturbations display the expected AH/singular saddle behavior while rho remains near one at closest approach. Determine what this validates, any numerical-instability caveats, and whether the ball test supports the interpretation of rho on the O(-1) bolt branch. Also comment on the failed attempt to interpret generic ball parameters as a continuum of ACH fillings; distinguish what is actually shown from Biquard's local deformation theory.

## Output

## Scientific verification memo

### 1. Exact nut series and complex-hyperbolic calibration

The series file gives
\[
c_{1,3}=1-c_{2,3}-c_{3,3},
\]
with \(q=c_{2,3}\) and \(r=c_{3,3}\) free. Thus the regular Einstein germs at a nut form a two-parameter local family in the diagonal ansatz.

For
\[
(c_{1,3},c_{2,3},c_{3,3})=\left(\frac16,\frac23,\frac16\right),
\]
substitution into the recorded fifth-order formulas gives
\[
(c_{1,5},c_{2,5},c_{3,5})
 =\left(\frac1{120},\frac2{15},\frac1{120}\right).
\]
These are exactly the Taylor coefficients of
\[
a_1(t)=a_3(t)=\sinh t,\qquad
a_2(t)=\sinh t\cosh t=\frac12\sinh(2t).
\]
Hence the series reproduces the complex-hyperbolic metric with fibre slot \(2\), in the normalization \(\operatorname{Ric}=-6g\) and \(d\sigma_i=2\sigma_j\wedge\sigma_k\).

For this exact solution,
\[
y_1=y_3=\coth t,\qquad y_2=2\coth(2t),
\]
and
\[
\kappa_2=\frac{a_2}{a_3a_1}=\coth t,\qquad
\rho_2=\frac{a_3}{a_1}=1.
\]
Therefore
\[
(y_1,y_2,y_3)\longrightarrow(1,2,1),\qquad
\kappa_2\longrightarrow1,\qquad \rho_2=1.
\]
The two cyclic copies in `einstein_nut_runs.json` verify the corresponding slot-1 and slot-3 formulas. This is a strong exact calibration of:

- the target growth vector \((2,1,1)\) with the fibre entry placed in the selected slot;
- the exponent in \(\kappa_k=a_k/(a_i a_j)\);
- the ordering in \(\rho_k=a_i/a_j\);
- the normalization \(\kappa\to1\) for the standard complex-hyperbolic model.

The slot-2 numerical record reaches
\[
\min\operatorname{dev}=2.025\times10^{-5},\quad
\kappa_2=0.999998337,\quad
\rho_2=0.99999999999994.
\]
The cyclic slot-3 record has essentially the same numbers, while the slot-1 copy reaches a smaller deviation \(2.32\times10^{-6}\) with \(\kappa_1=1.00000492\). The slot cycling is therefore implemented correctly.

### 2. Geometric meaning of \(\kappa\) and \(\rho\)

Suppose an ACH trajectory with fibre slot \(k\) has
\[
a_k=A_ke^{2t}(1+o(1)),\qquad
a_i=A_ie^t(1+o(1)),\qquad
a_j=A_je^t(1+o(1)).
\]
Then
\[
\kappa=\frac{A_k}{A_iA_j},\qquad
\rho=\frac{A_i}{A_j}.
\]
The leading metric is
\[
g\sim dt^2+A_k^2e^{4t}\sigma_k^2
       +e^{2t}\bigl(A_i^2\sigma_i^2+A_j^2\sigma_j^2\bigr).
\]
Writing
\[
\theta=A_k\sigma_k,\qquad e^i=A_i\sigma_i,\qquad e^j=A_j\sigma_j,
\]
the Maurer–Cartan normalization gives
\[
d\theta=2\kappa\,e^i\wedge e^j.
\]
Thus \(\kappa=1\) is exactly the normalized Levi/contact compatibility in the conventions of the scripts.

The same conclusion follows directly from the Einstein constraint. At the ACH target \(y_k=2,\ y_i=y_j=1\), the potential terms satisfy
\[
P_k\longrightarrow2\kappa^2,\qquad
P_i,P_j\longrightarrow-2\kappa^2.
\]
Consequently the constraint tends to
\[
(2\cdot1+1\cdot1+1\cdot2)-6-\frac12(2\kappa^2-2\kappa^2-2\kappa^2)
=\kappa^2-1.
\]
An exact ACH end therefore has \(\kappa=1\). In contrast, \(\rho\) drops out of this leading equation and labels the horizontal CR anisotropy.

If \(X_i,X_j\) are dual to \(\sigma_i,\sigma_j\), the compatible complex structure has, up to orientation convention,
\[
JX_i=\rho\,X_j,\qquad JX_j=-\rho^{-1}X_i.
\]
The ratio of horizontal metric coefficients is \(\rho^2\), while the ratio of horizontal lengths is \(\rho\). Interchanging the two horizontal axes sends \(\rho\mapsto\rho^{-1}\). Therefore the script’s quantity has the correct geometric role, although a literature parameter for the Rossi family may be written as \(\rho\), \(\rho^2\), \(\log\rho\), or a fractional transformation of these, depending on convention.

### 3. What the saddle experiment actually shows

The biaxial path in the nut script is
\[
q=\frac{1-r}{2},
\]
so \(c_{1,3}=c_{2,3}\). Its complex-hyperbolic point is the slot-3 copy
\[
(q,r)=\left(\frac16,\frac23\right).
\]
The sampled values on opposite sides behave as expected:

- \(r=0.5\) evolves to the AH state, with all three terminal \(y_i\) equal to \(\sqrt2\) to numerical precision.
- \(r=0.8\) reaches the large-\(|y|\) event at finite \(t\), with \(y_3=60\) and \(y_1=y_2\approx-52.64\).
- The exact point shadows the ACH slot-3 state.

This gives a qualitative AH/ACH/singular separatrix picture. It does not quantify the unstable eigenvalue or exhibit a long sequence of increasingly tuned nonexact trajectories. The two nearest sampled perturbations are not especially close to the full ACH data:
\[
\begin{array}{c|c|c|c}
r & \min\operatorname{dev}_{\mathrm{ACH3}} & \kappa_3 & \rho_3\\ \hline
0.5 & 0.714 & 0.662 & 1.000000000002\\
0.8 & 0.614 & 1.933 & 1.000000000001
\end{array}
\]
Their unit value of \(\rho_3=a_1/a_2\) is enforced by the exact biaxial relation \(a_1=a_2\). It is therefore a useful indexing and symmetry test, but not independent evidence for how a nonunit Rossi parameter evolves.

For slot \(3\), the near-nut horizontal anisotropy is
\[
c_{1,3}-c_{2,3}=1-2q-r.
\]
The tested biaxial line sets this expression identically to zero. A genuine homogeneous Rossi direction must leave that line, with
\[
2\,\delta q+\delta r\ne0.
\]
No tuned triaxial nut trajectory appears in the supplied run file.

### 4. Numerical sensitivity of the separatrix computation

The exact complex-hyperbolic solution should approach its ACH state monotonically for all \(t\). The numerical trajectory instead reaches its closest point near \(t=6.234\) and then departs strongly. At \(t=12\), the slot-2 run reports
\[
(y_1,y_2,y_3)=(1.25165,1.65547,1.25165),
\]
whereas the analytic solution has
\[
(y_1,y_2,y_3)
=(\coth12,\,2\coth24,\,\coth12)
=(1+O(10^{-10}),\,2+O(10^{-21}),\,1+O(10^{-10})).
\]
Thus the endpoint is not a numerical approximation to the exact asymptotic state; it is a nearby constraint-preserving trajectory amplified along an unstable direction.

Even at the reported closest time, the exact formula gives
\[
\coth(6.23419)\approx1.00000769,
\]
while the run gives
\[
\kappa_2=0.99999834.
\]
The order-\(10^{-5}\) discrepancy and reversal of the sign of \(\kappa-1\) show that digits beyond the basic “very near one” statement are not geometrically meaningful here.

Several numerical facts explain this behavior:

1. At \(t_0=0.002\), the variables \(y_i\) and potential terms involve quantities of order \(10^2\) and \(10^5\!-\!10^6\), respectively. The initial constraint residual \(3.5\times10^{-10}\) is therefore only about \(10^{-15}\) relative to the cancelling terms.
2. The omitted \(t^7\) terms at this \(t_0\) are at or below double-precision resolution in \(a_i\). Increasing the formal series order alone would not remove the main perturbation without higher-precision arithmetic.
3. A small constraint residual only verifies consistency with the first integral. It does not distinguish the desired separatrix from a nearby Einstein trajectory lying on the same constraint hypersurface.
4. The minimum is taken over 3000 uniformly sampled dense-output points, not by a continuous minimization. This is adequate for recognizing the passage but does not attach high precision to the minimum.
5. The substantially different shadowing times for cyclic copies of the same exact solution are another signature of amplified roundoff and local truncation error.

Accordingly, the `min_dev` construction successfully recognizes passage near the ACH saddle. Endpoint classification alone would misidentify even the analytically exact complex-hyperbolic initial data after numerical drift. Likewise, a very long floating-point bisection interval refinement does not by itself yield comparable geometric precision; plateau length and stability under changes of \(t_0\), arithmetic precision, tolerance, and terminal time carry the substantive information.

### 5. Consequences for the \(O(-1)\) bolt branch

The ball calculation supports the \(O(-1)\) interpretation in a specific and useful sense. The nut script imports the same right-hand side, constraint, and slot formulas used by `einstein_bolt_shoot.py`. In particular, the cyclic complex-hyperbolic test with fibre slot \(1\) directly calibrates
\[
\kappa_1=\frac{a_1}{a_2a_3},\qquad
\rho_1=\frac{a_2}{a_3},
\]
which is exactly the bolt script’s `rossi_a2_over_a3` readout. It confirms that:

- \(\rho_1=1\) is the standard isotropic CR point;
- nonunit \(\rho_1\) measures horizontal anisotropy;
- swapping horizontal labels replaces \(\rho_1\) by its reciprocal;
- \(\kappa_1\to1\) is required by the Einstein constraint and contact normalization.

What the ball data do not establish is that a particular \(O(-1)\) trajectory remains ACH for infinite radial time, or that its reported nonunit number equals a named Rossi coordinate without a convention conversion. The ball and \(O(-1)\) interiors also have different topology. The calibration transfers the asymptotic geometry and code normalization, not the existence or completeness of the bolt solution.

A convincing nonunit bolt readout would have \((y_k,y_i,y_j)\) increasingly close to \((2,1,1)\), \(\kappa\) increasingly close to \(1\), a growing shadowing interval under refined shooting, and a stable value of \(\rho\) across that interval. A small \(y\)-deviation at one time without corresponding control of \(\kappa\) is weaker, as the \(r=0.5\) and \(r=0.8\) ball trajectories illustrate.

### 6. Generic nut parameters versus Biquard deformation theory

The two free cubic coefficients describe regular local Einstein germs at the nut. They are not automatically coordinates on complete ACH fillings. Completeness and ACH behavior impose global dynamical conditions on the outward evolution. The present computations show an open collection of regular germs going to AH behavior or finite-time singular behavior, together with the exact complex-hyperbolic separatrix.

Biquard’s local deformation theory, when its nondegeneracy and gauge hypotheses apply, is instead an existence result for complete Einstein metrics associated with sufficiently small CR data at infinity near the complex-hyperbolic model. It does not say that every arbitrary pair \((q,r)\) of center-jet coefficients produces such a metric.

Within the homogeneous diagonal reduction, a one-parameter family of CR structures labeled by \(\rho\) would naturally appear as a tuned curve in the two-dimensional \((q,r)\)-plane through the complex-hyperbolic point, not as an open two-dimensional set. The tested biaxial line fixes \(\rho=1\), so it probes a transverse AH/singular direction rather than the nontrivial Rossi direction. The supplied files contain no triaxial tuning calculation that recovers such a curve.

Thus the artifacts establish:

- a correct exact CH calibration of the ACH slot, \(\kappa\), and the unit-\(\rho\) basepoint;
- qualitative saddle behavior across a biaxial slice;
- a geometrically sound interpretation of \(\rho\) as horizontal CR anisotropy.

They neither numerically produce a continuum of nonunit ACH ball fillings nor conflict with a local deformation theorem that would select specially tuned complete solutions. No source passage specifying the precise version of Biquard’s theorem was supplied, so its exact regularity spaces, gauge formulation, and uniqueness statement cannot be verified from these artifacts alone.
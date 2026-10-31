# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 14,
  "task_field": "verifier",
  "task_index": 2,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step14_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step14_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Read the exact nut-series and nut-shoot artifacts as an independent calibration of the Step-13 ACH classifier. The nut series has two free cubic coefficients and recovers complex hyperbolic space at (c1,c2,c3)=(1/6,2/3,1/6), where the shoot reaches ACH slot 2 with kappa≈0.999998 and rho=1. Nearby perturbations display the expected AH/singular saddle behavior while rho remains near one at closest approach. Determine what this validates, any numerical-instability caveats, and whether the ball test supports the interpretation of rho on the O(-1) bolt branch. Also comment on the failed attempt to interpret generic ball parameters as a continuum of ACH fillings; distinguish what is actually shown from Biquard's local deformation theory.

## Integrated Scientific Memo

## Verification memo: nut calibration of the Step-13 ACH classifier

### 1. What is exactly validated

The nut expansion has two free cubic coefficients:
\[
q=c_{2,3},\qquad r=c_{3,3},\qquad c_{1,3}=1-q-r.
\]
Thus smooth diagonal Einstein germs at the nut form a two-parameter local family. At
\[
(c_{1,3},c_{2,3},c_{3,3})
=\left(\frac16,\frac23,\frac16\right),
\]
the recorded fifth-order formulas give
\[
(c_{1,5},c_{2,5},c_{3,5})
=\left(\frac1{120},\frac2{15},\frac1{120}\right),
\]
matching
\[
a_1=a_3=\sinh t,\qquad a_2=\frac12\sinh 2t.
\]
This is complex hyperbolic space in the stated normalization, with fibre slot \(2\). Analytically,
\[
(y_1,y_2,y_3)=\bigl(\coth t,\,2\coth 2t,\,\coth t\bigr),
\]
and
\[
\kappa_2=\frac{a_2}{a_3a_1}=\coth t\to1,\qquad
\rho_2=\frac{a_3}{a_1}=1.
\]

The run reaches
\[
\min\operatorname{dev}=2.03\times10^{-5},\qquad
\kappa_2=0.99999834,\qquad \rho_2=1+O(10^{-13}).
\]
The cyclic copies recover ACH in slots \(1\) and \(3\). Hence the artifacts strongly validate:

- the ACH growth target \(y_k\to2,\ y_i,y_j\to1\);
- fibre-slot indexing and cyclic permutation;
- the formulas
  \[
  \kappa_k=\frac{a_k}{a_i a_j},\qquad \rho_k=\frac{a_i}{a_j};
  \]
- the normalization \(\kappa_k\to1\) at the standard complex-hyperbolic model;
- consistency of the nut series, ODE, and classifier near the exact model.

The Einstein constraint independently forces the same \(\kappa\)-normalization. At an ACH limit,
\[
P_k\to2\kappa^2,\qquad P_i,P_j\to-2\kappa^2,
\]
so the constraint tends to \(\kappa^2-1\). Therefore every genuine ACH end in these conventions must have \(\kappa=1\).

By contrast, \(\rho\) is unconstrained at leading order and records the ratio of horizontal lengths. Interchanging the two horizontal axes sends \(\rho\mapsto\rho^{-1}\). Literature parameters for homogeneous Rossi structures may instead use \(\rho^2,\log\rho\), or another reparametrization, so numerical equality with a named convention requires an explicit conversion.

### 2. Saddle behavior and the numerical caveat

Linearization about the ACH state explains both the successful calibration and its limited time horizon. With fibre slot \(k\), set
\[
s=\delta y_i+\delta y_j,\quad v=\delta y_k,\quad
w=\log\kappa,\quad m=\delta y_i-\delta y_j.
\]
The leading constrained dynamics has rates
\[
-6,\qquad +2,\qquad -4,\qquad 0,
\]
where \(+2\) is the transverse unstable mode, \(-4\) controls horizontal anisotropy, and the zero mode is \(\log\rho\). The unstable eigenvector satisfies, up to scale,
\[
(\delta y_i,\delta y_j,\delta y_k,w)
=(-0.6,-0.6,0.8,1).
\]
Consequently:

- \(\kappa<1\) gives \(y_k\) decreasing and \(y_i,y_j\) increasing, the AH exit;
- \(\kappa>1\) gives the singular/blow-up exit.

The printed complex-hyperbolic runs depart along precisely this unstable direction. They therefore shadow the exact separatrix only until about \(t=6\!-\!7\). For example, the analytic slot-2 solution at \(t=12\) is still essentially \((1,2,1)\), whereas the numerical endpoint is
\[
(1.25165,1.65547,1.25165).
\]
That endpoint is not an approximation to complex hyperbolic infinity; it is a nearby constraint-preserving trajectory whose tiny initial error has been exponentially amplified.

This gives several important cautions:

1. **Closest approach, not the terminal state, is the valid calibration.** Endpoint classification would fail even for data intended to represent the exact CH solution.

2. **The last digits of \(\kappa\) are not geometric precision.** At the slot-2 closest time, the exact value is \(\coth t>1\), while the numerical value is slightly below \(1\), already reflecting the unstable numerical mode.

3. **A small constraint residual does not certify the separatrix.** It only certifies proximity to the Einstein constraint hypersurface; the unstable direction lies within that hypersurface.

4. **The initial residual \(O(10^{-10})\) is compatible with floating-point cancellation.** At \(t_0=0.002\), individual terms are \(O(t_0^{-2})\sim2.5\times10^5\). The omitted higher-order nut terms are already near or below double-precision resolution.

5. **Uniform sampling gives only an approximate minimum.** The reported minimum over 3000 dense-output samples is adequate for detecting passage near ACH, not for assigning many accurate digits.

Thus the run validates the classifier structurally, but not long-time numerical convergence of the separatrix. Higher precision or better regularized variables are needed for a longer shadowing interval.

### 3. What the sampled perturbations establish

The biaxial line used in the script is
\[
q=\frac{1-r}{2},\qquad c_1=c_2.
\]
Its complex-hyperbolic point is the **slot-3** point
\[
(c_1,c_2,c_3)=\left(\frac16,\frac16,\frac23\right),
\qquad r=\frac23,
\]
not \(r=\frac16\). Hence most listed samples are not genuinely close perturbations of that point. The relevant bracketing samples are:

- \(r=0.5\): AH, with terminal \(y_i\to\sqrt2\);
- \(r=0.8\): finite-time singular exit;
- \(r=2/3\): exact CH data shadowing the ACH saddle.

This supports the qualitative picture that ACH is a separatrix between AH and singular behavior. It does not yet measure the separatrix accurately, determine an unstable exponent numerically, or produce a tuned family of nonstandard ACH ends. The nearest sampled off-separatrix points have minimum ACH deviations about \(0.71\) and \(0.61\), so they never enter a quantitatively close ACH regime.

Moreover, on this biaxial line
\[
\rho_3=\frac{a_1}{a_2}\equiv1
\]
by symmetry. Thus “\(\rho\) stays near one at closest approach” is expected identically and is mainly a symmetry/indexing check, not evidence about nonunit Rossi parameters.

### 4. Consequence for the \(O(-1)\) bolt branch

The ball test does support the bolt interpretation at the level of **formula, normalization, and basepoint**. Both scripts use the same ODE and the same slot convention. For bolt fibre slot \(1\),
\[
\kappa_1=\frac{a_1}{a_2a_3},\qquad
\rho_1=\frac{a_2}{a_3},
\]
exactly the bolt script’s `rossi_a2_over_a3`. The nut calibration confirms:

- \(\rho_1=1\) is the standard horizontally isotropic CR point;
- nonunit \(\rho_1\) represents horizontal CR anisotropy;
- exchanging horizontal axes sends \(\rho_1\mapsto\rho_1^{-1}\);
- a true ACH end must have \(\kappa_1\to1\).

The linearized mechanism also supports reading \(\rho\) at closest approach: the unstable mode has no \(\rho\)-component to first order, while horizontal anisotropy decays. Therefore a well-developed ACH plateau should have nearly constant \(\rho\), even though the orbit eventually exits along the unstable direction.

But the present ball experiments test only \(\rho=1\). They do **not** independently calibrate any nonunit bolt value, prove that a bolt trajectory remains ACH for infinite radial time, or identify the numerical ratio with a particular published Rossi coordinate. Nor does the ball topology prove existence or completeness on \(O(-1)\).

For a convincing bolt readout one needs simultaneous evidence that, under refined shooting,

\[
(y_k,y_i,y_j)\to(2,1,1),\qquad \kappa_k\to1,
\]
the ACH shadowing interval grows, and \(\rho_k\) stabilizes across that interval. A one-time small \(y\)-deviation without \(\kappa\approx1\) is insufficient.

There is also a bisection caveat in the bolt code: `classify` calls a run AH only when its endpoint at fixed \(T\) is already within \(0.02\) of \(\sqrt2(1,1,1)\). A very finely tuned AH-side trajectory may still be lingering near ACH at time \(T\) and be labeled `other`, which is then treated as non-AH in the bisection. The sign of \(\kappa-1\) immediately after closest approach is a more local and reliable side diagnostic.

### 5. Generic nut parameters are not a continuum of ACH fillings

The two free cubic coefficients parameterize **local smooth Einstein germs at the nut**, not complete ACH fillings. Global integration imposes an additional dynamical condition: the unstable ACH mode must be tuned away. The computations show open sets evolving to AH or singular behavior and isolated exact CH data on their boundary. Dynamically, one expects an ACH locus of codimension one in the two-dimensional nut-parameter plane—locally a curve for each fibre slot—not an open two-parameter family.

The sampled biaxial line fixes \(\rho=1\), so it probes a transverse AH/ACH/singular direction. It cannot reveal the nontrivial Rossi modulus. A genuine nonunit test must leave that line; for slot \(3\), the near-nut horizontal anisotropy is
\[
c_{1,3}-c_{2,3}=1-2q-r,
\]
so one needs \(2\,\delta q+\delta r\neq0\), followed by tuning in the remaining direction to eliminate the ACH unstable mode.

### 6. Relation to Biquard’s local deformation theory

The numerical result must not be conflated with Biquard’s theorem. What is shown here is:

- exact CH calibration in all three slots;
- correct \(\kappa\) and unit-\(\rho\) normalization;
- qualitative AH/singular saddle behavior;
- no computed nonunit ACH ball trajectory.

Biquard’s local deformation theory is a boundary-value existence theory near complex hyperbolic space, subject to its analytic, gauge, and nondegeneracy hypotheses. It concerns specially selected complete ACH Einstein fillings for sufficiently small CR deformations at infinity. It does not assert that every arbitrary pair of nut cubic coefficients integrates to a complete ACH metric.

Within the homogeneous diagonal reduction, such a theorem would predict a specially tuned one-dimensional curve through the CH point, with \(\rho\) varying near \(1\). The supplied computations neither construct nor test that curve. They therefore do not contradict local deformation theory; they only refute the incorrect interpretation that the entire two-parameter family of local nut germs is a continuum of ACH fillings. Exact claims about Biquard’s regularity spaces, uniqueness, self-duality, or inclusion of particular Rossi structures cannot be certified from the supplied artifacts alone.

## Bottom line

The nut artifacts are a strong independent calibration of the Step-13 ACH **slot, growth-vector, \(\kappa\), and \(\rho=1\) basepoint** conventions. They also expose the expected unstable-saddle numerics: closest approach is meaningful, long-time endpoints are not. They support interpreting bolt \(\rho=a_i/a_j\) as horizontal CR anisotropy, but do not validate nonunit bolt values or prove bolt ACH completeness. Finally, generic ball parameters demonstrably do not form a continuum of ACH fillings; any local Biquard family would occur as a tuned codimension-one locus that has not yet been computed here.
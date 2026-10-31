# TTCS Independent Branch Record

```json
{
  "step_id": 14,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A02/workspace/scripts/einstein_chirality_check.py",
    "Sessions/S1003A02/workspace/data/einstein_bolt_chirality.json",
    "Sessions/S1003A02/workspace/notes/step13_einstein_fillings_blown_up_ball.md",
    "Sessions/S1003A02/workspace/scripts/einstein_bolt_shoot.py"
  ]
}
```

## Task

Independently interpret the Step-14 curvature experiment on the Step-13 diagonal SU(2) Einstein O(-1) bolt branch. The coordinate/JAX curvature routine is calibrated on complex hyperbolic space: CH has WA≈0 and WB=24. Along the numerical bolt branch, Ric0≈0 and scalar≈-24, while WA is large near the bolt but decays to 10^{-12}–10^{-16} on the ACH plateau; WB remains nonzero around 23–26. Decide precisely what this establishes and what it does not: is the full metric self-dual, asymptotically self-dual, or merely approaching the CH end? Check whether any orientation or 2-jet reconstruction issue could explain the result. Then assess how this changes the proposed route through Hitchin/Biquard versus interval enclosure. Give a mathematical memo, not procedural advice.

## Output

# Mathematical memo: interpretation of the Step-14 Weyl-block experiment

## 1. Orientation and identification of the two blocks

For an oriented Einstein four-manifold, the curvature operator has the decomposition
\[
\mathcal R=
\begin{pmatrix}
W^+ + \frac{s}{12}I & 0\\
0 & W^-+\frac{s}{12}I
\end{pmatrix}
\qquad\text{on }\Lambda^2_+\oplus\Lambda^2_-.
\]

The complex-hyperbolic calibration identifies the JAX blocks rather sharply. For a Kähler surface with its complex orientation,
\[
\operatorname{spec}(W^+)=\left\{\frac{s}{6},-\frac{s}{12},-\frac{s}{12}\right\},
\qquad
|W^+|^2=\frac{s^2}{24}.
\]
At \(s=-24\), this gives \(|W^+|^2=24\). Complex hyperbolic space also has \(W^-=0\). The computed values
\[
W_A^2\simeq0,\qquad W_B^2=24
\]
therefore identify, relative to the orientation
\[
dt\wedge\sigma_1\wedge\sigma_2\wedge\sigma_3,
\]
\[
W_A=W^-,\qquad W_B=W^+.
\]

This agrees with the Step-13 convention: every
\[
\omega_i=a_i\,dt\wedge\sigma_i+a_ja_k\,\sigma_j\wedge\sigma_k
\]
is self-dual in that orientation. Moving the asymptotic Kähler slot from slot \(2\) in the calibration to slot \(1\) on the bolt branch does not reverse the manifold orientation. An orientation reversal would merely exchange \(A\) and \(B\); it could not turn two simultaneously nonzero blocks into a half-conformally-flat curvature tensor.

## 2. What the computed interior curvature says

For all three sampled near-separatrix trajectories, both Weyl halves are substantially nonzero near the bolt. At \(t=0.08\),
\[
\begin{array}{c|cc}
b&|W^-|^2&|W^+|^2\\ \hline
0.35&2369.60&409.52\\
0.8&167.83&36.13\\
4&7.96&6.40
\end{array}
\]
and both halves remain visibly nonzero at \(t=0.2\) and \(t=0.5\).

Thus the three represented Einstein metrics are neither
\[
W^-\equiv0
\quad\text{nor}\quad
W^+\equiv0.
\]
In particular, they are not self-dual Einstein metrics in either orientation. A single interior point with \(|W^-|^2>0\) already excludes \(W^-\equiv0\); the large values here are far beyond any plausible floating-point residue.

The files sample only three values of \(b\). They therefore do not exclude an isolated half-conformally-flat member elsewhere on the numerical branch. They do exclude identifying the observed one-parameter ACH bolt family as a self-dual Einstein family.

The scalar and traceless-Ricci output,
\[
s=-24+O(10^{-11}),\qquad |\operatorname{Ric}_0|^2\lesssim10^{-22},
\]
confirms that the reconstructed jets satisfy \(\operatorname{Ric}=-6g\) to numerical precision. Since \(a''\) is itself generated from the Einstein ODE, this is primarily a strong consistency test of the ODE-to-coordinate-curvature translation and Hamiltonian constraint, rather than an independent proof that the shot is the exact infinite-time separatrix.

## 3. What happens on the ACH plateau

The small Weyl block decreases very rapidly once the orbit enters the ACH regime. Between \(t=1\) and \(t=2\),
\[
\begin{array}{c|ccc}
b&|W^-|^2(t=1)&|W^-|^2(t=2)&
-\log\!\bigl(|W^-|^2(2)/|W^-|^2(1)\bigr)\\ \hline
0.35&4.50\times10^{-3}&4.55\times10^{-7}&9.20\\
0.8&2.47\times10^{-2}&3.13\times10^{-6}&8.97\\
4&2.17\times10^{-2}&4.71\times10^{-6}&8.44
\end{array}
\]
and the later pairs give effective squared-norm exponents close to \(8.1\). Thus the data are consistent with
\[
|W^-|^2=O(e^{-8t}),\qquad |W^-|=O(e^{-4t})
\]
along the plateau. At \(t=2\),
\[
|W^+|^2=23.903,\ 23.967,\ 24.004
\]
for the three cases, matching the complex-hyperbolic value \(24\).

This has a precise interpretation:

* The numerical shots enter a regime whose pointwise curvature approaches the complex-hyperbolic curvature tensor.
* Conditional on an exact complete separatrix satisfying
  \[
  y\longrightarrow(2,1,1),\qquad
  \kappa_1=\frac{a_1}{a_2a_3}\longrightarrow1,
  \]
  that metric satisfies
  \[
  |W^-|_g\longrightarrow0,\qquad |W^+|_g^2\longrightarrow24.
  \]
  It is therefore asymptotically self-dual in the pointwise Weyl-norm sense.
* It is not self-dual on the full manifold, because \(W^-\) is large in the bolt region.

“Approaching the CH end” and “asymptotically self-dual” are not two different phenomena here. The latter is a curvature consequence of the former. It does not supply the first-order self-dual Einstein equations in the interior.

The observed \(e^{-4t}\) decay of \(|W^-|\) is stronger information than the bare statement \(|W^-|\to0\), but the finite shots do not provide a formal all-orders expansion. The last values \(10^{-12}\)–\(10^{-16}\) for the squared norm also approach the regime where coordinate conditioning and cancellation matter; the values around \(10^{-6}\) at \(t=2\) already establish the robust many-order decay.

## 4. Why this does not identify the standard complex-hyperbolic filling

The Rossi ratio survives even though the leading pointwise curvature becomes complex hyperbolic. Write the ACH leading behavior as
\[
a_1\sim C_2C_3e^{2t},\qquad
a_2\sim C_2e^t,\qquad
a_3\sim C_3e^t,
\qquad
\rho=\frac{C_2}{C_3}.
\]
After rescaling the horizontal coframe by
\[
\widetilde\sigma_2=C_2\sigma_2,\qquad
\widetilde\sigma_3=C_3\sigma_3,\qquad
\widetilde\sigma_1=C_2C_3\sigma_1,
\]
the leading Heisenberg relation is independent of \(\rho\). Consequently the leading solvable metric has the CH curvature tensor for every fixed \(\rho\), while \(\rho\) remains encoded in the CR structure at infinity and in lower-order terms.

Hence
\[
|W^-|\to0,\qquad |W^+|^2\to24
\]
does not imply \(\rho=1\), standard CR infinity, or an exterior region exactly isometric to CH. The Step-13 values \(\rho\simeq2.2\) and larger are fully compatible with the Step-14 curvature output. Zeroth-order scalar curvature invariants cannot distinguish the standard sphere from these Rossi ends.

The files also contain finite-precision shots that shadow the ACH fixed set for a long interval and then leave it. They do not by themselves construct an exact trajectory converging as \(t\to\infty\). The values \(22.94\), \(23.11\), and \(26.16\) for the large Weyl block at the recorded \(t_{\min}\) reflect finite corrections and the eventual departure of the pseudo-orbits; the especially close agreement with \(24\) at \(t=2\) is the clearer fixed-point comparison.

## 5. The quadratic reconstruction is not the source of the effect

At a selected time, the script replaces each axis by
\[
a_i(r)=a_i(0)+a_i'(0)r+\frac12a_i''(0)r^2.
\]
At \(r=0\), this has exactly the same radial \(0\)-, \(1\)-, and \(2\)-jet as the original metric. The Riemann tensor depends only on the metric \(2\)-jet, so no third or higher radial derivative enters. Moreover,
\[
a_i'=a_i y_i,\qquad
a_i''=a_i(y_i'+y_i^2),
\]
and `jet_from_state` uses precisely these formulas with \(y_i'\) supplied by the Einstein ODE. The angular dependence remains the exact Euler/Maurer–Cartan dependence through `euler_E`.

The CH tests at three radii simultaneously verify:

1. the normalization \(d\sigma_i=2\sigma_j\wedge\sigma_k\);
2. the scalar-curvature convention;
3. the Hodge-block decomposition;
4. the radial \(2\)-jet reconstruction.

The Euler point used is away from an angular coordinate pole. Near \(t=0.08\) the metric is anisotropic but not sufficiently ill-conditioned to turn roundoff into Weyl norms of order \(1\)–\(10^3\). At the latest \(b=4\) point the axis ratio is about \(405\), so the reported \(4\times10^{-16}\) squared norm is less quantitatively secure; this affects the last digits of the decay, not the distinction between large interior \(W^-\) and small plateau \(W^-\).

Orientation ambiguity also cannot explain the result. Reversing orientation exchanges the two displayed columns, and both are nonzero in the interior.

## 6. Consequences for the Hitchin/Biquard route

Hitchin’s Painlevé-VI reduction concerns SU(2)-invariant self-dual Einstein metrics, where one Weyl half vanishes identically and the second-order Einstein system reduces to a special first-order integrable system. The sampled O\((-1)\) bolt trajectories violate that defining equation in the interior. Their asymptotic decay \(W^-\to0\) does not place them in Hitchin’s family.

Likewise, Biquard’s self-dual metrics on the ball describe a different subfamily. They remain valuable as nut/ball comparison solutions and as a calibration of the Rossi parameter, but they do not parametrize the observed blown-up-ball bolt branch. Biquard’s general ACH Einstein deformation and Fredholm framework remains relevant because it does not require \(W^-\equiv0\); it can organize the ACH asymptotic data \((\rho,\) mass-type coefficient, radial shift\()\), but it does not supply the desired global bolt-to-infinity classification or the numerical lower value \(\rho_{\min}\).

The mathematical object still absent from the Step-13 result is therefore an enclosure for the full Einstein ODE, not a Painlevé-VI identification: an exact bolt-regular orbit converging to the ACH fixed set, together with controlled dependence of its limiting Rossi ratio on \(b\). The Step-14 curvature data sharpen this distinction by showing that the branch is genuinely Einstein but generically non-self-dual in its interior, while becoming CH-like and pointwise self-dual only at infinity.

**Bottom line:** the experiment supports asymptotic vanishing of \(W^-\), approximately at \(|W^-|=O(e^{-4t})\), for the finite near-separatrix shots. It decisively rejects global half-conformal flatness for the three sampled metrics. The vanishing block at large \(t\) records approach to the universal CH curvature model of an ACH end and does not convert the bolt branch into a Hitchin/Biquard self-dual family or identify its Rossi infinity with the standard sphere.
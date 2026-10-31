# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 14,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step14_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step14_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Independently interpret the Step-14 curvature experiment on the Step-13 diagonal SU(2) Einstein O(-1) bolt branch. The coordinate/JAX curvature routine is calibrated on complex hyperbolic space: CH has WA≈0 and WB=24. Along the numerical bolt branch, Ric0≈0 and scalar≈-24, while WA is large near the bolt but decays to 10^{-12}–10^{-16} on the ACH plateau; WB remains nonzero around 23–26. Decide precisely what this establishes and what it does not: is the full metric self-dual, asymptotically self-dual, or merely approaching the CH end? Check whether any orientation or 2-jet reconstruction issue could explain the result. Then assess how this changes the proposed route through Hitchin/Biquard versus interval enclosure. Give a mathematical memo, not procedural advice.

## Integrated Scientific Memo

# Mathematical memo: what the Step‑14 chirality experiment establishes

Fix the orientation
\[
dt\wedge \sigma_1\wedge\sigma_2\wedge\sigma_3>0.
\]
For the Step‑13 convention, the three forms
\[
\omega_i=a_i\,dt\wedge\sigma_i+a_ja_k\,\sigma_j\wedge\sigma_k
\]
are self-dual in this orientation. On a Kähler surface with complex orientation,
\[
|W^+|^2=\frac{s^2}{24}.
\]
Thus for complex hyperbolic space with \(s=-24\),
\[
|W^+|^2=24,\qquad W^-=0.
\]
The CH calibration \(WA\simeq0,\ WB=24\) therefore identifies
\[
WA=|W^-|^2,\qquad WB=|W^+|^2
\]
in this orientation.

## 1. The sampled bolt metrics are not globally self-dual

Near the bolt, both Weyl blocks are unequivocally nonzero. At \(t=0.08\),
\[
\begin{array}{c|cc}
b&|W^-|^2&|W^+|^2\\ \hline
0.35&2369.60&409.52\\
0.8&167.83&36.13\\
4&7.96&6.40
\end{array}
\]
and both remain nonzero at subsequent interior samples. Hence each of the three sampled near-separatrix metrics satisfies
\[
W^-\not\equiv0,\qquad W^+\not\equiv0.
\]
They are therefore neither self-dual nor anti-self-dual, in either orientation, and are not conformally flat.

This rules out identifying the numerically observed \(O(-1)\) ACH bolt family with a Hitchin/Tod self-dual Einstein family. Strictly, three sampled values of \(b\) do not exclude an isolated half-conformally-flat solution elsewhere in the two-parameter bolt moduli space, but they decisively exclude self-duality as a property of the observed branch.

The data also contradict Kählerity of the sampled metrics. An Einstein Kähler surface with \(s=-24\) would have the Weyl block containing its Kähler form of squared norm \(24\) everywhere. Neither displayed block has this behavior through the interior. This supports the Step‑13 local Kähler obstruction, although it is not needed for the main chirality conclusion.

## 2. The end is CH-like and asymptotically half-conformally flat

On the ACH plateau,
\[
|W^-|^2=WA\longrightarrow0,\qquad |W^+|^2=WB\longrightarrow24
\]
to the accuracy allowed by the finite shots. For example, at \(t=2\),
\[
WA=(4.55\times10^{-7},\,3.13\times10^{-6},\,4.71\times10^{-6}),
\]
while
\[
WB=(23.903,\,23.967,\,24.004)
\]
for \(b=0.35,0.8,4\), respectively.

The observed decay is compatible with
\[
|W^-|^2=O(e^{-8t}),\qquad |W^-|=O(e^{-4t}).
\]
Indeed, comparing \(t=2\) with the late plateau samples gives effective squared-norm exponents approximately \(8.27,8.13,8.05\).

The precise conclusion is therefore:

* the full metric is not self-dual;
* the numerical orbit approaches a curvature regime in which the vanishing CH Weyl half tends to zero;
* conditional on an exact complete separatrix converging to the ACH fixed set, the resulting metric is **asymptotically self-dual in the pointwise sense**
  \[
  |W^-|_g\to0;
  \]
* this asymptotic self-duality is a consequence of approaching the local complex-hyperbolic curvature model, not evidence that the interior satisfies the self-dual Einstein equations.

The experiment itself uses finite-precision near-separatrix trajectories that shadow the ACH set and eventually depart. It consequently does not prove existence of an exact complete orbit or an infinite-time asymptotic expansion. In particular, the final \(10^{-12}\!-\!10^{-16}\) values occur where scaling and cancellation are least favorable. The decay already visible by \(t=1,2\) is the more robust conclusion.

## 3. Curvature convergence does not imply standard CR infinity

The Step‑14 result is completely compatible with the Step‑13 Rossi ratios \(\rho\gtrsim2.2\). In the ACH\(_1\) regime one has schematically
\[
a_1\sim C_2C_3e^{2t},\qquad
a_2\sim C_2e^t,\qquad
a_3\sim C_3e^t,\qquad
\rho=\frac{C_2}{C_3}.
\]
After adapting the horizontal coframe, the leading solvable metric has the CH curvature tensor independently of the fixed value of \(\rho\). The ratio \(\rho\) remains encoded in the CR structure at infinity and in lower-order asymptotic data.

Consequently,
\[
W^-\to0,\qquad |W^+|^2\to24
\]
does **not** imply any of the following:

\[
\rho=1,\qquad \text{standard spherical CR infinity},\qquad
\text{an exact CH exterior},\qquad
\text{a globally self-dual filling}.
\]

Thus “approaching the CH end” and “asymptotically self-dual” describe the same leading curvature phenomenon here, whereas the standard-versus-Rossi distinction lies in asymptotic boundary data not detected by these leading scalar curvature norms.

The recorded late values \(WB=22.94,23.11,26.16\) should not be interpreted as limiting constants: the corresponding shots are already at their closest finite approach and beginning to feel the residual stable/unstable displacement. They do not weaken the clear convergence toward \(24\) visible earlier on the plateau.

## 4. Neither orientation nor jet reconstruction explains the pattern

### Orientation

Changing orientation interchanges \(W^+\) and \(W^-\), hence merely swaps \(WA\) and \(WB\). It cannot make a metric with both blocks nonzero near the bolt into a half-conformally-flat metric.

Nor does changing the asymptotic Kähler slot from the CH calibration slot to slot \(1\) reverse orientation: all three \(\omega_i\) lie in the same self-dual bundle for the fixed volume form. Therefore the CH calibration and bolt computation use a consistent chirality identification.

### Quadratic radial reconstruction

At each sample time the script replaces the axes locally by
\[
a_i(r)=a_i+a_i'r+\frac12a_i''r^2.
\]
At \(r=0\), this reproduces exactly the radial \(0\)-, \(1\)-, and \(2\)-jets. Since the Riemann tensor depends only on the metric \(2\)-jet, no higher radial derivative is required. The derivatives are reconstructed as
\[
a_i'=a_i y_i,\qquad
a_i''=a_i(y_i'+y_i^2),
\]
with \(y_i'\) supplied by the Einstein ODE, while the full angular dependence is retained through the Euler-frame matrix.

The CH checks at three radii recover
\[
s=-24,\qquad \operatorname{Ric}_0=0,\qquad WA=0,\qquad WB=24
\]
to roundoff. This simultaneously checks the curvature normalization, angular-frame convention, Weyl splitting, and radial \(2\)-jet procedure. Therefore the large interior \(WA\) is genuine, not a reconstruction artifact.

The very small late values have less reliable relative precision because of large axis ratios, but conditioning cannot explain the transition from \(WA\sim1\!-\!10^3\) near the bolt to \(WA\ll1\) on the plateau.

The values
\[
s=-24+O(10^{-11}),\qquad |\operatorname{Ric}_0|^2\lesssim10^{-22}
\]
are strong consistency checks between the Step‑13 Einstein ODE and the independent coordinate-curvature routine. Because \(a''\) is generated using that ODE, they are not an independent proof that the numerically shot trajectory is the exact infinite-time separatrix.

## 5. Consequence for Hitchin/Biquard versus the full Einstein ODE

Hitchin’s Painlevé‑VI/Tod reduction applies to SU(2)-invariant **self-dual Einstein** metrics, where one Weyl half vanishes identically and the second-order Einstein equations reduce to a special first-order integrable system. The observed \(O(-1)\) bolt branch has large nonzero \(W^-\) in the interior, so it is not an orbit of that system. Decay \(W^-\to0\) at an ACH end does not restore the missing first-order equations.

Similarly, Biquard’s self-dual ball fillings remain relevant as:

* a calibration of the Rossi boundary parameter;
* a comparison family passing through CH at \(\rho=1\);
* a reference self-dual slice of ACH end data.

They do not parametrize the blown-up-ball bolt branch and cannot establish its existence, its fold/minimum \(\rho_{\min}\), or exclusion of \(\rho=1\).

Biquard’s **general** ACH Einstein deformation/Fredholm framework remains conceptually relevant because it does not assume global self-duality. However, the supplied evidence does not justify stronger claims that the observed exit modes are tangent to a self-dual invariant set, nor that \(W^-=O(e^{-4t})\) is automatically universal for every ACH Einstein end; those require an explicit linearized/asymptotic calculation not present here.

The unresolved rigorous object is therefore the full diagonal Einstein boundary-value problem:

1. an exact bolt-regular trajectory converging to the ACH fixed set;
2. its limiting Rossi ratio \(\rho(b)\);
3. control of the full branch, including the apparent fold and a certified lower bound such as \(\rho(b)>1\).

That is naturally an interval-enclosure problem for the complete constrained Bianchi IX Einstein system, using an ACH asymptotic expansion with the boundary ratio and free decaying coefficients. The self-dual theory supplies comparison and calibration data, not the governing classification.

## Conclusion

The Step‑14 experiment shows that the sampled diagonal SU(2) \(O(-1)\) Einstein bolt metrics are **genuinely non-self-dual in the bulk**, while their near-separatrix ends become **asymptotically self-dual because their pointwise curvature approaches the complex-hyperbolic model**. It does not show that the global metrics are self-dual, that their CR infinity is standard, or even by itself that an exact complete separatrix exists. Orientation reversal only exchanges the two Weyl blocks, and the exact \(2\)-jet reconstruction cannot account for the observed effect. Consequently, Hitchin/Biquard self-dual classifications cannot replace enclosure of the full Einstein ODE; their remaining role is as an asymptotic and ball-filling reference theory.
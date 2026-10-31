# Step 14 — Chirality, nut calibration, and where the complete-cell action is spent

Agent3, Execute. This note records the consequences of four checks on the Step-13 diagonal Einstein-bolt picture and relates them to the supplied classical-gap supplement and the peer's larger exact-collar cells.

## 1. Frontier context from the supplied supplement

The human-supplied `Skills/geometric-analysis/research/supplements/20261004_classical_and_quantitative_gaps.tex` gives the clean classical position for handle-free blow-ups:
\[
8\pi^2\max\{0,k-A/3\}\le \inf P\le 8\pi^2k.
\]
Thus for \(0<k<A/3\), precisely the region probed by an isolated blow-up cell in a large complex-hyperbolic cover, the listed classical lower value is zero. A positive complete-cell infimum combined with an all-competitor decomposition theorem would add the first positive information in that range. The same supplement also records:

- under negative-Yamabe closure, \(\inf\mathcal E=\inf\mathcal J\) whenever \(\inf\mathcal E<1\);
- the N1 neighborhood estimate
  \[
  \mathcal J+(T/A-2/3)_+\ge c_*/(1+\nu/(2\pi^2));
  \]
- the actual-field differential estimate
  \[
  \Sigma\le C\{\Pi+\sqrt{\Pi Y}\};
  \]
- exact formal integral data obeying the displayed classical numerical budgets but having \(\mathcal J=o(h)\), showing why a localization or decomposition theorem must transport same-field differential information rather than only Chern–Weil numbers.

These facts sharpen the role of the cell problem without changing the route.

## 2. The Step-13 ACH bolt branch is not self-dual

Script: `workspace/scripts/einstein_chirality_check.py`.
Data: `workspace/data/einstein_bolt_chirality.json`.
Independent reading: `trace/ttcs/results/step14_ttcs01_verifier1_integration.md`.

The script reconstructs the exact radial 2-jet of a diagonal Bianchi-IX Einstein trajectory at a sample time and feeds it to the independent coordinate/JAX curvature evaluator from `o11_rotated_cell.py`. Complex hyperbolic space calibrates the two Weyl blocks:
\[
(s,|\operatorname{Ric}^\circ|^2,WA,WB)=(-24,0,0,24),
\]
so in the complex orientation \(WA=|W^-|^2\), \(WB=|W^+|^2\).

For representative near-separatrix bolt shoots, both blocks are nonzero in the core. At \(t=0.08\):

| bolt radius \(b\) | \(|W^-|^2\) | \(|W^+|^2\) |
|---:|---:|---:|
| 0.35 | 2369.60 | 409.52 |
| 0.8 | 167.83 | 36.13 |
| 4 | 7.96 | 6.40 |

Therefore the observed family is neither self-dual nor anti-self-dual in the bulk. Hitchin/Tod Painlevé-VI self-dual Einstein theory cannot classify this branch. Orientation reversal only swaps the two nonzero blocks.

Along the finite ACH plateau, \(W^-\) decays strongly while \(|W^+|^2\) approaches the CH value. For \(b=0.8\),
\[
|W^-|^2(t=1)=2.47\times10^{-2},\qquad
|W^-|^2(t=2)=3.13\times10^{-6},
\]
and at the closest recorded point it is \(8.25\times10^{-13}\), while \(|W^+|^2\) is near \(24\) on the reliable part of the plateau. This is compatible with \(|W^-|=O(e^{-4t})\), but the trajectories eventually leave the unstable ACH saddle. The correct statement is that the branch is **asymptotically half-conformally-flat if the exact separatrix exists**, because its leading curvature approaches CH; it is not a globally self-dual family. Leading curvature convergence does not fix the horizontal CR modulus \(\rho\), so it is fully compatible with the Step-13 Rossi ratios \(\rho\gtrsim2.2\).

This redirects rigor to the full constrained Einstein ODE: existence of the bolt-to-ACH separatrix, its limiting \(\rho(b)\), and a certified separation from \(\rho=1\). Biquard's self-dual ball theory remains a calibration/comparison, not a substitute.

## 3. Smooth-nut cross-check of the ACH readout

Scripts and data:

- `workspace/scripts/einstein_nut_series.py`;
- `workspace/data/einstein_nut/series.json`;
- `workspace/scripts/einstein_nut_shoot.py`;
- `workspace/data/einstein_nut_runs.json`.

The exact smooth-nut expansion is
\[
a_i=t+c_i t^3+d_i t^5+O(t^7),\qquad c_1+c_2+c_3=1,
\]
with two free cubic coefficients. In terms of \(q=c_2,r=c_3\),
\[
\begin{aligned}
c_1&=1-q-r,\\
d_1&=\frac3{20}(8q^2+28qr-13q+8r^2-13r+4),\\
d_2&=\frac3{20}(8q^2-12qr-3q-12r^2+12r-1),\\
d_3&=-\frac3{20}(12q^2+12qr-12q-8r^2+3r+1).
\end{aligned}
\]
Complex hyperbolic space with fibre slot 2 occurs at
\[
(c_1,c_2,c_3)=(1/6,2/3,1/6),
\]
where these fifth-order terms exactly match \(a_1=a_3=\sinh t\), \(a_2=\tfrac12\sinh2t\). The shoot gives closest approach
\[
\kappa_2=0.99999834,\qquad \rho_2=1+O(10^{-13}),\qquad
|(y_1,y_2,y_3)-(1,2,1)|=2.03\times10^{-5}.
\]
Cyclic copies recover the other fibre slots. Hence the Step-13 definitions
\[
\kappa_k=\frac{a_k}{a_i a_j},\qquad \rho_k=\frac{a_i}{a_j}
\]
are correctly normalized, and \(\rho=1\) is the standard CR point.

The numerical endpoint at large \(t\) must not be used: the ACH saddle has an unstable rate \(+2\), so even the exact-CH initial truncation eventually exits because binary64/truncation error is amplified. Closest approach is the meaningful datum. Generic nut parameters are merely local Einstein germs; they run to AH or singular ends unless one parameter is tuned. The current runs therefore do not construct Biquard's nonunit Rossi family. They only validate the classifier, slot convention, \(\kappa\)-normalization and \(\rho=1\) basepoint.

## 4. The certified cell does not pay in a late CR-correction layer

Script: `workspace/scripts/o11_cell_einstein_shadow.py`.
Data and figure:

- `workspace/data/o11_cell_einstein_shadow.json`;
- `workspace/figures/o11_cell_einstein_shadow.png`.

For the certified \(X=8,x_0=0.01\) profile, the bolt radius is \(b=0.1\). The bolt anisotropy is
\[
d=(a_1-a_2)/t^4\approx-0.46227,
\]
consistent in sign with the fixed-slot convention. Matching \((b,n,d)\) to a Ric\(=-6g\) bolt orbit does **not** match the full 2-jet: the cell has \(p_{2,\mathrm{cell}}\approx5.16\), while Einstein regularity forces
\[
p_{2,E}=\frac{3b^2+2}{2b}=10.15.
\]
The compared Einstein trajectory therefore separates immediately and its numerical integration fails by \(t\approx0.297\); values extrapolated after that time have no geometric meaning. Moreover \(b=0.1\) is below the Step-13 threshold at which the AH/singular boundary visibly approaches an ACH saddle.

The positive-square action is concentrated at the bolt scale:
\[
t_{50}=0.0649,\quad t_{75}=0.1009,\quad t_{90}=0.1496,\quad t_{99}=0.3191,
\]
while the exact CH collar begins at outer geodesic distance \(t\approx1.755\). These quantiles are close to the Burns bubble density. Thus the literal story “follow an Einstein ACH filling, then pay most of the cost in a late CR layer” is false for this witness. The metric pays almost the full \(8\pi^2\) positive action in the Burns-like core and reaches the exact CH collar with little additional positive-square action.

This cumulative plot does **not** locate the small subthreshold saving \(1-P/(8\pi^2)\approx8.9\times10^{-4}\); it mainly resolves the unit Burns cost. The saving comes from the calibrated cubic interaction against the completed squares and must be studied by a Burns-centered expansion, not by the cumulative positive density alone.

The strongest supported variational object is therefore a local weighted control value from regular \((-1)\)-bolt data to a CH-directed transverse section,
\[
\mathcal I_{\rm core}=\inf\int_0^\tau\sum_i\frac{\lambda_i}{4}
\left(u_i'-\frac{2H_i}{\lambda_i}\right)^2dt,
\]
or a Hamilton--Jacobi subsolution/calibration for this action. In the small-bubble regime, the more precise route is the Burns-centered identity
\[
\frac{P}{8\pi^2}=1+S_1+S_2+S_3+
\int\frac{2u_1u_2u_3}{\lambda_2}\,dt,
\]
which can prove or sharpen the supported \(-9b^4\log(1/b^2)\) response. A compactness contradiction for all free-radius cells still needs control over varying bolt radius, collapse of the weights \(\lambda_i\), the Einstein constant and migration of the defect.

## 5. New large-collar evidence and the neutral flux variable

Peer note: `Sessions/S1003A01/workspace/notes/step14_large_collar_resistance_and_cluster_budget.md`.

The peer has now rigorously enclosed physically continued cells:
\[
\frac{J_6(X=32)}{8\pi^2}<0.998736769872,\qquad
\frac{J_6(X=64)}{8\pi^2}<0.998702764484,
\]
with \(P(X=64)/(8\pi^2)<0.998701\). These improve the separated balanced construction to
\[
\limsup\alpha_j/h_j<3.998846902+\varepsilon,
\]
for arbitrarily small collar smoothing loss. Fixed-radius profiles stabilize from \(X=32\) to \(64\), supporting a complete finite-action diagonal limit, but not proving stationarity, optimality or a positive limiting infimum.

The reduced neutral mode is not controlled by endpoint ratio alone. In the model
\[
\mathcal A_T(q)=\int_0^T e^{4t}(q''+4q')^2dt,
\]
with clamped endpoints, the exact minimum tends to \(64(\Delta q)^2\). But the transported quantity is
\[
\Phi=q+\tfrac14q',\qquad \Phi'=\tfrac14(q''+4q'),
\]
so a free entrance slope can change \(q\) at zero model cost. For the exact diagonal metric,
\[
(Wq')'=W(V-E),\qquad
V=\frac{4(a_2^2-a_3^2)(a_2^2+a_3^2-a_1^2)}{W^2},\quad
E=(\operatorname{Ric}^\circ)_{22}-(\operatorname{Ric}^\circ)_{33},
\]
and \(|\operatorname{Ric}^\circ|^2\ge E^2/2\). A diagonal lower theorem thus requires low-cost entry into a noncollapsed ACH tube, control of \(W\), the potential \(V\), and the entrance flux \(q'\), together with rigorous separation of the bolt Einstein filling map from the standard value \(\rho=1\). Ratio mismatch alone is insufficient.

## 6. Resulting research judgment

Three potential shortcuts were tested and rejected in their strong form:

1. The bolt branch is not Hitchin/Biquard self-dual in the interior.
2. The ball calibration validates \(\rho\), but generic nut germs are not automatically ACH fillings.
3. The certified small-b cell does not realize a late CR-mismatch payment.

What survives is a coherent two-scale structure:

- **core:** a nearly Burns bolt cost with a small negative cubic correction, naturally attacked by the exact three-squares-plus-cubic identity and a local control calibration;
- **end:** a finite-weight ACH neutral-mode resistance governed by the flux-corrected variable \(\Phi\), relevant only after noncollapse, potential and entrance-flux control are established.

The large-collar continuation indicates that both scales may coexist in a complete finite-action diagonal profile. Turning this into \(\mathfrak P^{SU(2)}_{1,0}>0\) requires a coercive compactness/decomposition statement linking them; the ODE enclosure of the non-self-dual bolt-to-ACH branch remains a separate necessary input. None of this excludes nonsymmetric standard-CR Einstein fillings or yields an unrestricted global lower bound yet.

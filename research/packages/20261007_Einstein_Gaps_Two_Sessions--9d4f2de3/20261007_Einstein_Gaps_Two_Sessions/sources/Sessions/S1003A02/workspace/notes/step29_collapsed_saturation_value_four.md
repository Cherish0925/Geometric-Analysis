# Step 29 — The collapsed saturation value is the Berger-to-round chiral gap 4

Conventions are those of Steps 25–28: \(\widehat P=P/8\pi^2=\int W|\operatorname{Ric}^\circ|^2/4\,dt\), diagonal Bianchi-IX metrics \(dt^2+\sum a_i^2\sigma_i^2\) with \(d\sigma_i=2\sigma_j\wedge\sigma_k\), block A \(=W^+\) in the CH/blow-up orientation, chiral fluxes \(\mathfrak b_\pm\) with charges: smooth centre \((2,2)\), \(O(-1)\) bolt \((1,7)\), biaxial Berger collapse \((-2,2)\), CH orbit \((2-9\sinh^4\tau,\,2-3\sinh^4\tau)\).

## 1. The exact-CH terminal is the correct terminal (correction of Step 28)

Step 28 rejected the exact-CH terminal of `scripts/saturation_optimal_control.py` because its endpoints, mapped to compact ACH variables, "left the ACH block". That rejection was an artifact of the checker `scripts/saturation_endpoint_residuals.py`: `to_compact` always places the endpoint on the section \(\zeta=10^{-2}\). In compact variables \(\zeta=1/(a_ga_h)\) in absolute units with \(\operatorname{Ric}=-6\) (from \(\mathrm{fac}=\sqrt\zeta e^{-\beta/3}=1/r\)). A CH orbit of radius \(t_{\rm ch}\approx1.9\) has \(a_ga_h=\sinh^2t_{\rm ch}\approx11\), so forcing \(\zeta=.01\) rescales it by about a factor of 3. The rescaled state is a homothetic CH jet with the wrong curvature scale, and its Einstein evolution with \(\Lambda=-6\) is meaningless.

The correct statement is simple.

**Lemma S (terminal reduction).** Let a controlled trajectory of the scale-free system (Step 28, (2.2)) end at the scale-free first jet \(Y_{\rm CH}(t_{\rm ch})\) of a complex-hyperbolic orbit. Continue the metric by the exact homothetic CH collar beyond that orbit and rescale the whole metric so that the collar has \(\operatorname{Ric}=-6\). The result is a \(C^{1,1}\) diagonal metric with an exact CH collar. Its \(\widehat P\) equals the trajectory action, because \(\widehat P\) charges only the trace-free Ricci tensor and is scale invariant.

The zero-control flow is Einstein: the trace-free equations together with the contracted Bianchi identity force \(s\) to be constant. Hence zero-control continuation from \(Y_{\rm CH}(t)\) is exactly CH, and the exact-CH ray is contained in the standard-CR stable set. Conversely, Theorem T (Step 26) truncates every trajectory entering the standard ACH block with \(\widetilde\Phi\to0\) to an exact CH collar at \(o(1)\) added cost. Therefore
\[
\inf_{\text{exact-CH terminal, free }t_{\rm ch}}=\inf_{\text{standard-CR stable-set terminal}} ,
\]
and the nonlinear stable-manifold parameterization proposed in Step 28 is not needed to formulate or compute the saturation value. The scalar normalization is also harmless. The exact-ended \(P\)-problem and the scalar-\(-24\) problem have the same infimum (Theorem C plus the weak-barrier Yamabe solution), and \(P(g)-P(\hat g)=24\int|\nabla u|^2+3\int(\Delta u/u)^2\ge0\). So any exact-CH competitor yields a scalar-\(-24\) competitor that is at least as cheap.

The Step-28 "stable" mode is a legitimate but harder parameterization. Its costs (4.05–6.16) come from a terminal restricted by the bounds \(|q|\le.3\), \(\kappa\in[.7,1.3]\), and they were not converged in the stable-set parameters.

## 2. Computation

New and modified scripts:

* `scripts/saturation_optimal_control.py` gains optional environment controls: `SAT_A0`, `SAT_T0CH` and `SAT_TAU0` set the cold-start guess, `SAT_TCH_LO` and `SAT_TCH_HI` set the opening-radius window, `SAT_XB` sets the state box, and `SAT_TAG` sets the file tag.
* `scripts/saturation_eps_chain.py` runs continuation in \(\varepsilon\) with warm starts. Outputs: `data/saturation_control/chain_N40_c40.json` and `chain_N80_c80.json`, plus the per-run files `eps*_N*_ch_c40|c80.json`.
* `scripts/saturation_opening_profile.py` minimizes with \(t_{\rm ch}\) confined to windows \([\tau_0,\tau_0+.25]\). Outputs: `data/saturation_control/opening_profile_eps0p0625_N60pjson` and `opening_profile_eps0p25_N60pjson`. The odd suffix comes from a string-replacement slip; these are JSON files.
* `scripts/saturation_metric_cost.py` gives an independent evaluation. From the node data alone it builds an actual \(C^1\) metric: cubic Hermite interpolation in \(\tau\), \(h=\int p\,d\tau\) computed exactly, \(t=\int e^h d\tau\). It then computes the Ricci tensor from the classical diagonal formulas \(\operatorname{Ric}_{00}=-\sum(y_i'+y_i^2)\), \(\operatorname{Ric}_{ii}=-y_i'-y_i\sum y_j+\mathrm{Pot}_i\), with analytic second derivatives of the interpolant. Gauss–Legendre quadrature, 24 nodes per cell, gives \(\widehat P\). The potential/control formulas are never used.
* `scripts/saturation_verify.py` is a multiple-shooting re-integration. It is useful only as a diagnostic: in the collapsed neck the forward dynamics grows like \(e^{h/z^2}\), and single-cell re-shooting diverges at small \(\varepsilon\) even for accurate collocation.

### 2.1 Value along the entry ray

The minimum over the entry phase \(A\), the duration and \(t_{\rm ch}\), with all three controls \((\bar H,\bar E,\bar D)\):

| \(\varepsilon\) | \(\mathfrak b_+(\text{entry})\) | gap \(2-\mathfrak b_+\) | collocation \(N=40\) | collocation \(N=80\) | actual-metric \(\widehat P\) | \(t_{\rm ch}\) | \(\max\mathfrak b_+\) |
|---|---|---|---|---|---|---|---|
| 1/2 | −0.446 | 2.446 | 2.3396 | 2.3310 | 2.5173 (N80) | 2.62 | 1.21 |
| 1/4 | −1.413 | 3.413 | 3.3852 | 3.3798 | 3.4773 (N80) | 2.33 | 1.57 |
| 1/8 | −1.762 | 3.762 | 3.7503 | 3.7461 | 3.8167 (N80) | 2.18 | 1.68 |
| 1/16 | −1.895 | 3.895 | 3.8896 | 3.8949* | 3.9343 (N40) | 1.73 | 1.79 |
| 1/32 | −1.951 | 3.951 | 3.9484 | 3.9509* | 3.9815 (N40) | 1.60 | 1.83 |
| 1/64 | −1.976 | 3.976 | 3.9763* | 3.9763* | — | 0.70 | 2.000 |
| 1/128 | −1.988 | 3.988 | 3.9884* | 3.9884* | 3.98841 (N80) | 0.70 | 2.000 |
| 1/256 | −1.994 | 3.994 | 3.9937 | — | 3.99632 (N40) | 0.70 | 2.000 |

\* IPOPT stopped at its iteration cap with constraint violation \(\le2\times10^{-5}\). These runs are converged in value but not certified as KKT points.

The actual-metric costs are 0.001–8% above the collocation values, and the difference shrinks under mesh refinement. They are genuine \(\widehat P\) values of explicit \(C^1\) metrics, up to quadrature error. The two meshes agree to \(<0.3\%\).

### 2.2 Opening-radius profile

The minimal cost with \(t_{\rm ch}\in[\tau_0,\tau_0+.25]\):

| \(\tau_0\) | 0.75 | 1.0 | 1.25 | 1.5 | 1.75 | 2.0 | 2.25 | 2.5 | 2.75 | 3.0 | 3.25 | 3.5 | 3.75 | 4.0 | 4.25 | 4.5 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| \(\varepsilon=1/16\) | 3.894 | 3.893 | — | 3.889 | — | 3.888 | — | 4.146 | — | 7.91 | — | 33.7 | — | 207 | — | 2848 |
| \(\varepsilon=1/4\) | (3.41 at 1.0) | 3.408 | — | 3.397 | — | 3.384 | 3.38 | — | 3.656 | — | 7.05 | — | 28.0 | — | 226 | — |

Late opening is priced at least exponentially. Successive costs grow by factors 4–8 per 0.5 in \(\tau\), consistent with the \(e^{4\tau}\) CR-pinning law of Lemma P. Opening below \(\tau\approx.70\) is priced by Corollary X3 at \(\ge4-9\sinh^4\tau\). The intermediate band costs \(\approx\) gap.

The largest late windows are under-resolved: at \(\tau_0=3\) the actual-metric cost is 45 against collocation 7.9. They are upper evidence of large cost, not values.

## 3. What the computation shows

1. **No collapsed competitor.** No computed collapsed saturation comes anywhere near the certified \(0.99585\) cell. The minimal value along the matched Taub-bolt/\(\Lambda\)-Taub-NUT entry ray increases monotonically as the neck deepens, from 2.33 at \(\varepsilon=1/2\) to 3.994 at \(\varepsilon=1/256\).

2. **The limit is the chiral gap 4.** The value tracks \(2-\mathfrak b_+(\text{entry})\) to within \(3\times10^{-3}\) for \(\varepsilon\le1/16\), and to within \(10^{-5}\) for \(\varepsilon\le1/64\). Here \(\mathfrak b_+(\text{entry})\to-2\), the biaxial Berger charge. Thus
\[
\mathcal V_{\rm sat}:=\lim_{\varepsilon\to0}\inf\widehat P_{\rm sat}=4 \qquad(\text{numerical}).
\]

3. **Structure of the minimizer.** For \(\varepsilon\le1/64\) the optimizer reaches \(\max\mathfrak b_+=2.000\), the value of a Euclidean-round orbit. Its cost equals the rise \(\mathfrak b_+(\mathrm{round})-\mathfrak b_+(\mathrm{entry})\) to \(10^{-5}\). By the chiral identity \(\widehat P=\Delta\mathfrak b_++\frac1{2\pi^2}\int|W^+|^2+\frac1{96\pi^2}\int s^2\), the rising part therefore has \(W^+\approx0\) and \(s\approx0\): it is asymptotically **anti-self-dual and scalar flat**. After the round orbit the trajectory follows a CH ball from radius \(\approx0\) at zero cost. The value then does not depend on \(t_{\rm ch}\); the lower bound \(0.701\) that the optimizer meets is inert.

   So the collapsed branch degenerates into a scale-separated bubble: a Ricci-flat Taub-bolt core, its ALF/Berger end, then an ASD scalar-flat decollapse region (cost 4) onto an almost-Euclidean neck at a point of CH. This is the ALF analogue of the Burns bubble. Burns joins the bolt charge 1 to the round charge 2 at cost 1. The collapsed route first drops freely to \(-2\) and must then pay \(2-(-2)=4\).

4. **Consequence for the Theorem-D branch list.** Mechanism 1, small-bolt collapse, is numerically priced at \(\approx4\) per collapsed bubble, with a factor-four margin over the best cell. The numerics also say where the remaining work lies: the minimizer approaches a near-round orbit, where \(\mathfrak b_+\) is already a sharp barrier, and openings far from round are more expensive.

## 4. The lower-bound problem, sharpened

The data identify the Hamilton–Jacobi subsolution that must be proved. The target is
\[
\Psi=\mathfrak b_++G(Y),\qquad \dot\Psi\le L \ \text{ for all controls},
\]
with \(G\ge0\), \(G\to0\) on the collapsed boundary, and \(G(Y_{\rm CH}(\tau))\ge9\sinh^4\tau-3+\delta\) along the CH ray. The \(-3+\delta\) is the slack needed only to beat \(1\); the sharp value corresponds to \(-\delta\). Then \(\widehat P_{\rm sat}\ge\Psi(\mathrm{end})-\Psi(\mathrm{entry})\ge1+\delta\) for every trajectory.

Writing \(\sigma_+=(|W^+|^2+s^2/48)W\,dt/d\tau\), which is quadratic in the controls, the requirement is the pointwise inequality
\[
\min_u\bigl[\sigma_+(Y,u)-\nabla G\cdot(f_0(Y)+Bu)\bigr]\ge0 .
\]
On the CH ray, \(\sigma_+=36W\,dt/d\tau\), so \(G\) must grow like \(9\sinh^4\tau\): this is the regenerated CH \(W^+\)-plus-volume energy. The tangency condition at the CH ray forces \(G\) to depend on the velocities \((p,\chi,\eta)\), not only on the shape.

The profile in §2.2 indicates the three regimes of \(G\):

* \(G\approx0\) near round orbits, where \(\mathfrak b_+\) alone already gives the sharp bound;
* \(G\) of Lemma-P type, \(\sim e^{4\tau}(\Delta\log\rho)^2\), on late openings;
* an interpolating band \(0.7\lesssim\tau\lesssim2.5\), where the numerical value is \(\approx\) gap and some slack of order 3 is available for \(\ge1\).

A practical route is polynomial/interval verification of a candidate \(G\) on the compact band, plus asymptotic arguments on the two ends.

An alternative, possibly shorter, rigorous route uses the minimizer's structure: show directly that any trajectory with \(\widehat P_{\rm sat}<1\) must reach a CH-like orbit with \(\tau<0.70\) (then Corollary X3 applies), using Lemma P to exclude \(\tau\gtrsim2.5\) and a compact computation for the band.

## 5. Frozen form of Theorem D

See `theorem_package_v1.md` §4.1, entry "Theorem D (frozen statement, Step 29)". That entry records the current status of each mechanism; mechanism 1 is now numerically priced at 4 (§3 above), and its proof is the subsolution of §4.

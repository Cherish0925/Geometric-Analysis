# Step 6 — Perpendicular O11 cells: distinct P/J costs, bolt-adapted transgression, and a relative calibration

Session S1003A01, Step 6, Execute. The peer correction in S1003A02 Step 8 invalidated the earlier orientation-penalty interpretation: a fixed-slot blow-up with Burns direction perpendicular to the CH Kähler form cancels the order-\(x_0\) trace-free Ricci cost. This step reconstructs that branch independently, separates the trace-free cost from the Einstein cell cost, and joins it to the slice transgression of Step 5.

## 1. Two costs in the peer normalization

The peer code uses the complex-hyperbolic normalization
\[
\operatorname{Ric}_{g_{CH}}=-6g_{CH},\qquad s_{CH}=-24.
\]
Put
\[
P(g)=\int |\operatorname{Ric}^{\circ}_g|^2dV_g,
\qquad J_6(g)=\int |\operatorname{Ric}_g+6g|^2dV_g.
\]
The orthogonal splitting of Ricci gives the exact relation
\[
\boxed{J_6=P+\frac14\int(s+24)^2dV.}\tag{1.1}
\]
If \(\widetilde g=6g\), then \(J_6(g)=J_1(\widetilde g)\), so this is exactly the I54/I55 cell cost after rescaling to \(\operatorname{Ric}=-g\). The fixed-parameter expression \(J_6\) is not itself invariant under arbitrary scaling with 6 held fixed; it is covariant under simultaneous rescaling of the Einstein constant.

This distinction is consequential. A fixed cell with \(J_6<8\pi^2\) enters the direct I54 finite-cell transfer. A profile with only \(P<8\pi^2\) can still matter through the inherited global \(\inf P\) reduction, but its scalar/conformal selection has to be handled separately. Therefore `scripts/perp_dual_cost.py` optimizes and records both costs.

## 2. Fixed-slot perpendicular ansatz and regular bolt-adapted axes

The implemented metric is
\[
g=\frac{dx^2}{4G(x)}+F(x)\sigma_1^2+x\sigma_2^2+xe^{w(x)}\sigma_3^2,
\quad x_0\le x\le X=1.\tag{2.1}
\]
The bolt collapses in the old \(\sigma_1\)-slot; the CH fibre is old \(\sigma_3\). The smooth bolt mode has \(w=O((x-x_0)^2)=O(t^4)\); this is the peer option `wpow=2`. The earlier statement that the transgression variable is singular in the perpendicular branch was coordinate-dependent. Use the orientation-preserving cyclic relabeling
\[
(a,b,c)=(\sqrt{x},\sqrt{xe^w},\sqrt F),
\qquad dt=\frac{dx}{2\sqrt G},\tag{2.2}
\]
so that \(c\) is again the collapsing distinguished slot. Then the Step-5 decomposition is regular and
\[
Y_{bolt}=-1,\quad \Pi_{bolt}=0,\quad \mathcal T_{bolt}=8\pi^2.\tag{2.3}
\]
On the exact CH collar \(F=x, G=x(1+x), e^w=1+x\), direct substitution gives
\[
p_+=0,\quad p_-=3x(1+x)^{-1/4},\quad Y=0,\quad
\Pi=9x^2,\quad \frac{\mathcal T}{8\pi^2}=9x^2.\tag{2.4}
\]
Writing the I54 radius as \(R^2=6x\), this is \(\Pi=R^4/4\), exactly the Strategist substitution. At the script's \(X=1\), the collar charge is \(9\cdot8\pi^2\); after rescaling to Ric=-g it is again \(4d\). Thus charge has not disappeared; it transfers from the scalar flux \(Y\) to the Kähler-defect term \(\Pi\). Choosing the bolt's own flux therefore does not restore an obligatory zero-charge crossing.

`perp_dual_cost.py` independently evaluates this transgression on the peer profile. For the peer's smooth \(x_0=.01\) P-optimized profile it finds
\[
P/(8\pi^2)=1.001996388,
\quad J/(8\pi^2)=1.002453337,
\quad (J-P)/(8\pi^2)=4.56948\times10^{-4}.\tag{2.5}
\]
The charge dips to \(\mathcal T/(8\pi^2)=0.0515617\) near \(x=0.06095\), then grows entirely through \(\Pi\) to 9 at the collar. The same profile has \(Y\to0,\Pi\to9\) at the collar to numerical precision. This verifies the axis conversion and the two-cost distinction on an actual near-minimizer. It does not prove positivity of the infimum.

## 3. New dual optimization results

`scripts/run_perp_dual_sweep.py` reoptimizes the same smooth fixed-slot ansatz separately for \(P\) and \(J\), at degrees 6 and 8, using 400–500 Gauss nodes. The final data are in `data/perp_dual/`; each record contains the full coefficients, independent scalar term, optimization termination, and bolt-adapted transgression profile. The sweep completed all sixteen degree/target cases; the canonical table is `data/perp_dual/summary.csv`.

The degree-8 results already returned were:

| \(x_0\) | target | \(P/8\pi^2\) | \(J/8\pi^2\) | scalar deviation | \(\min \mathcal T/8\pi^2\) |
|---:|:---:|---:|---:|---:|---:|
| .003 | P | 1.000121440 | 1.000198631 | 7.72e-5 | .01705 |
| .003 | J | 1.000121630 | 1.000130599 | 8.97e-6 | .01698 |
| .01 | P | 1.001936966 | 1.002381323 | 4.44e-4 | .05146 |
| .01 | J | 1.001855826 | 1.001939414 | 8.36e-5 | .05152 |
| .03 | P | 1.017890798 | 1.021006185 | 3.12e-3 | .11848 |
| .03 | J | 1.018432695 | 1.019029297 | 5.97e-4 | .12032 |
| .1 | P | 1.149762740 | 1.220934254 | 7.12e-2 | .21663 |
| .1 | J | 1.162214888 | 1.170416666 | 8.20e-3 | .22182 |

All returned competitors remain above both thresholds. Optimizing \(J\) does not merely repeat P optimization: it sharply reduces scalar deviation and changes the profile, e.g. at \(x_0=.01\), while leaving a positive margin. Conversely P optimization accepts a larger scalar deviation to reduce trace-free Ricci cost. These are upper bounds on class infima, not certified minimizers; some `success=true` records still have gradients of order 1e-4 because L-BFGS stopped on function reduction. Degree-10/12 continuation and two random restarts per degree were completed for \(x_0=.01\) in `scripts/perp_degrees.py`. The best J-target profile had \(J/(8\pi^2)=1.001895793\), \(P/(8\pi^2)=1.001831515\); the best P-target profile had \(P/(8\pi^2)=1.001866502\). These results remain above threshold and differ from the degree-8 values by at most \(4.4\times10^{-5}\) on the optimized target. Gradient norms remain \(10^{-4}\)–\(10^{-3}\), so this is useful stability evidence rather than a resolved infinite-dimensional minimum.

The values support the peer's vanishing first-order coefficient, but they do not yet determine whether the leading residual is \(c x_0^2\), \(x_0^2\log(1/x_0)\), or another second-order law. No subthreshold cell was found.

## 4. Chern–Simons connection variables

The bolt-adapted transgression has a more revealing symmetric form. Define
\[
u_1=e^{\varpi}p_+,
\quad u_2=e^{-\varpi}p_-,
\quad u_3=Y-\frac12p_+p_-,
\qquad e^{2\varpi}=a/b.\tag{4.1}
\]
Equivalently, cyclically in \((i,j,k)\),
\[
u_i=\dot a_i-\frac{a_j^2+a_k^2-a_i^2}{a_ja_k}.\tag{4.2}
\]
Then the charge is the cubic Chern–Simons polynomial
\[
\boxed{C(u):=\frac{\mathcal T}{8\pi^2}
=u_1^2+u_2^2+u_3^2+u_1u_2u_3.}\tag{4.3}
\]
The endpoint states are
\[
u_{bolt}=(0,0,-1),\qquad u_{CH}=(0,3x,0).\tag{4.4}
\]
Thus the perpendicular cell transports charge from the \(u_3\)-axis to the \(u_2\)-axis through a nearly uncharged neck. This is a heteroclinic transfer problem rather than a scalar sign-crossing problem.

Set
\[
H_i=u_i+\frac12u_ju_k,
\qquad \lambda_i=\frac{a_ja_k}{a_i}.\tag{4.5}
\]
A direct invariant-curvature computation yields
\[
\frac{P}{8\pi^2}=\int\sum_i\frac{\lambda_i}{4}
\left(\dot u_i-\frac{2H_i}{\lambda_i}\right)^2dt.\tag{4.6}
\]
Subtract the outgoing CH charge and use the relative calibration
\[
\Phi=C-u_2^2=u_1^2+u_3^2+u_1u_2u_3,
\quad \Phi_{bolt}=1,\ \Phi_{CH}=0.\tag{4.7}
\]
Completing squares gives
\[
\boxed{\begin{aligned}
\frac{P}{8\pi^2}-1=\int\Bigg[&
\frac{\lambda_1}{4}\left(\dot u_1+\frac{2H_1}{\lambda_1}\right)^2
+\frac{\lambda_3}{4}\left(\dot u_3+\frac{2H_3}{\lambda_3}\right)^2\\
&+\frac{\lambda_2}{4}\left(\dot u_2-\frac{2u_2-u_1u_3}{\lambda_2}\right)^2
+\frac{2u_1u_2u_3}{\lambda_2}\Bigg]dt.
\end{aligned}}\tag{4.8}
\]
Everything except one cubic interaction is nonnegative. In particular,
\[
u_1u_2u_3\ge0\ \hbox{pointwise}\quad\Longrightarrow\quad
P\ge8\pi^2\quad\hbox{and}\quad J\ge8\pi^2.\tag{4.9}
\]
But the actual \(x_0=.01\) near-minimizer spends 85.5% of the sampled logarithmic interval in the negative chamber. `scripts/perp_spin_diagnostics.py` evaluates every term in (4.8) and independently matches the JAX curvature integral to \(1.4\times10^{-9}\):
\[
S_1=0.00113124,\quad S_2=0.000217907,\quad S_3=0.00207890,
\quad C_{cubic}=-0.00143166,\tag{4.10}
\]
so
\[
S_1+S_2+S_3+C_{cubic}=0.0019963874=P/(8\pi^2)-1.\tag{4.11}
\]
The negative cubic is not a negligible perturbation: it cancels about 42% of the three positive relative-flow squares. The positive threshold margin is a genuine coupled compensation, precisely of the kind sought in Steps 3–4.

For \(J\), the exact additional term is
\[
\frac{J-P}{8\pi^2}=\frac14\int abc\left[
\sum_i\left(\frac{\dot u_i}{a_i}+\frac{2H_i}{a_ja_k}\right)-12
\right]^2dt.\tag{4.12}
\]
This independently matches the scalar deviation in (2.5) to \(2.1\times10^{-12}\). Consequently a proof for J may succeed even if P admits a lower competitor; the two theorem targets must remain separate.

## 5. The analytic problem isolated by the computation

Equation (4.8) turns the full fixed-slot P threshold into the exact inequality
\[
\int(S_1+S_2+S_3)dt\ge
2\int\frac{(-u_1u_2u_3)_+}{\lambda_2}dt.\tag{5.1}
\]
Treating the outgoing \(u_2\) channel as background and \(\eta=(u_1,u_3)^T\), the transverse part is a 2×2 weighted Sturm/Hardy form. On an exact CH segment, after diagonalizing with \(v_\pm=u_1\pm u_3\), one obtains
\[
\mathcal Q_+=\int\left[\frac{x(1+x)}4(v_+')^2+
\frac{4+18x+15x^2}{16x(1+x)}v_+^2\right]dx,\tag{5.2}
\]
\[
\mathcal Q_-=\int\left[\frac{x(1+x)}4(v_-')^2+
\frac{4-18x+3x^2}{16x(1+x)}v_-^2\right]dx.\tag{5.3}
\]
Only the minus channel has a sign-changing potential. Pointwise positivity is therefore false and unnecessary; the natural theorem is positivity of the weighted Sturm operator with the bolt-to-collar endpoint behavior, or a positive matrix Riccati supersolution through the transition region.

An alternative Hamilton–Jacobi route searches for a scale-invariant calibration \(B(a,u)\) with \(B_{bolt}=1, B_{CH}=0\) and nonnegative residual after square completion. The zeroth approximation is \(B_0=C-u_2^2\). Its only residual is the cubic in (4.8). The correction
\[
\psi=-\frac{a_2^2}{a_1a_3}u_1u_3\tag{5.4}
\]
has an \(a_2\)-transport term that cancels the bare cubic. `scripts/perp_relative_checks.py` verifies the relative completion symbolically and computes the full residual for \(B_0+\psi\). That residual is not manifestly nonnegative—it contains mixed quadratic, cubic and quartic terms—so (5.4) is only a concrete first Hamilton–Jacobi correction, not a theorem. It must be localized or repaired at endpoints and combined with further terms if this route is to close.

For J, the scalar square (4.12) adds rank-one coercivity to the same Sturm system. This is likely the easier direct finite-cell theorem. For P, the result would be stronger and feed the global inf-P route directly.

## 6. Implementation cautions and present mathematical status

- The peer file's docstring mentions \(xe^{-w}\), but the implemented fixed-slot metric is exactly (2.1), \(\operatorname{diag}(F,x,xe^w)\). All calculations here follow the implementation.
- `wpow=1` gives only \(w=O(t^2)\) and is not the smooth charge-four transverse mode. All new main optimizations use `wpow=2`; the rough peer profiles are used only as initial coefficients before imposing the smooth envelope.
- The polynomial envelopes match the CH metric through the derivatives needed by the integrated curvature calculation, but are not literally equal on an open collar. A flat terminal cutoff gives smooth exact-collar approximants with convergent L2-curvature cost; the numerical profile itself should be called a matched cell rather than an exact-collar metric.
- The charge minima are sampled values, not interval-arithmetic bounds.
- Optimization gives explicit upper competitors and local stationarity evidence, not lower bounds for the infinite-dimensional class.
- No profile found here has \(P<8\pi^2\) or \(J<8\pi^2\). The all-profile perpendicular inequality, the aligned Conjecture Z, the full cell conjecture, and the unrestricted balanced coefficient remain open.

The research advance is a sharper mechanism. The perpendicular branch is now simultaneously (i) the only tested direction with order-x0 cancellation, (ii) a genuine P/J bifurcation, and (iii) an exact relative-calibration problem with one signed cubic. The immediate next mathematical work is to establish or disprove the matrix Hardy/Riccati inequality underlying (5.1), using the stored profiles to test proposed weights and the high-degree runs to resolve the second-order sign.

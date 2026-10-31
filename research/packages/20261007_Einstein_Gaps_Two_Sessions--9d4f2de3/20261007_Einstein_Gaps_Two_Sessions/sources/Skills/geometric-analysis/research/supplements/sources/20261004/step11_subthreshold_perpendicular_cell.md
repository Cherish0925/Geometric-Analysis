# Step 11 — Finite-scale perpendicular cell below the Burns threshold

## 1. Frozen cell

Use the degree-eight coefficient vector in

`Sessions/S1003A01/workspace/data/perp_collar/x0.01_X8_J_d8.json`.

It defines on \(x\in[x_0,X]\), \(x_0=.01\), \(X=8\),
\[
 g=\frac{dx^2}{4G}+F\sigma_1^2+x\sigma_2^2+xe^w\sigma_3^2,
\]
with the \(\sigma_1\)-circle collapsing at the bolt and the complex-hyperbolic Kähler fibre in the \(\sigma_3\) slot. The background normalization is \(\operatorname{Ric}=-6g\). Set
\[
 P=\int |\operatorname{Ric}^\circ|^2,
 \qquad J_6=P+\frac14\int(s+24)^2=\int|\operatorname{Ric}+6g|^2.
\]
The one-cell topological threshold is \(8\pi^2\).

## 2. Independent reconstruction

`workspace/scripts/o11_collar_independent_verify.py` reconstructs the profile from the frozen decimal coefficients without importing the peer's cell, curvature, or spin-diagnostic code. It uses the Cartan variables
\[
 u_i=\dot a_i-\frac{a_j^2+a_k^2-a_i^2}{a_ja_k},\quad
 H_i=u_i+\frac12u_ju_k,\quad \lambda_i=\frac{a_ja_k}{a_i}
\]
and evaluates both
\[
 \frac P{8\pi^2}=\int\sum_i\frac{\lambda_i}{4}
 \left(\dot u_i-\frac{2H_i}{\lambda_i}\right)^2dt
\]
and the relative calibration
\[
 \frac P{8\pi^2}-1=\int(S_1+S_2+S_3+2u_1u_2u_3/\lambda_2)dt,
\]
together with the scalar square. Split Gauss orders 200, 400 and 800 agree to the displayed precision:
\[
\begin{aligned}
S_1&=.00159729167196687,\\
S_2&=.00052244698325698,\\
S_3&=.00109028656646375,\\
C_3&=-.00410132248809498,\\
P/(8\pi^2)&=.9991087027335926,\\
(J_6-P)/(8\pi^2)&=7.54040173166\times10^{-6},\\
J_6/(8\pi^2)&=.9991162431353243.
\end{aligned}
\]
The positive-square and relative evaluations of \(P\) differ by less than \(5\times10^{-15}\). This independently reproduces peer computations but does not by itself turn floating quadrature into a proof.

The script also verifies
\[
 F=G=w=0,\quad F'G'=1,\quad w'=0
\]
at the bolt, and exact complex-hyperbolic values and first jets at \(X\). On 20,001 points,
\[
\min G/(x-x_0)=1.0321404811,\qquad
\min F/(x-x_0)=.9661766585.
\]
Metric positivity is in fact analytic from
\[
F=(x-x_0)e^{q_F}+x_0S(u)>0,
\quad G=((x-x_0)+(x^2+x_0)S(u))e^{q_G}>0,
\]
with \(0\le S\le1\).

## 3. Ball arithmetic status

`workspace/scripts/o11_collar_arb_certificate.py` is a second independent evaluator in 160-bit python-flint/Arb. It propagates the decimal coefficients and all derivatives entering the spin formula through a second-order jet algebra. Composite Simpson meshes 500, 1000 and 2000 give the normalized defect integral
\[
J_6/(8\pi^2)-1=
-.0008837566079749,
-.0008837568484957,
-.0008837568636623.
\]
Inflating the finest Richardson change by a factor \(1000\) gives
\[
J_6/(8\pi^2)<.99911624414745<1.
\]
The Arb balls rigorously contain the finite Simpson sums and their roundoff propagation, but the Simpson remainder is still estimated from mesh convergence rather than a proved interval bound for the fourth derivative; the decimal JSON values were also first parsed as binary64 in this exploratory script. Thus this is strong high-precision evidence, not yet a theorem-level certificate. Raw interval subdivision is ineffective near the bolt because the spin expressions have severe dependency cancellation. The right final certification route is to parse each decimal as an exact rational and factor
\[
y=x-x_0,\quad F=y\widehat F,\quad G=y\widehat G,
\quad w=y^2\widehat w
\]
and simplify the relative-plus-scalar density before Arb subdivision, or to derive an analytic derivative bound for the transformed integrand. TTCS derived regular variables \(u_1=\sqrt y\,U_1\), \(u_2=\sqrt y\,U_2\), \(u_3=U_3\), which cancel every half-power in the density; the complete formulas and a rigorous Taylor/Simpson enclosure scheme are in `trace/ttcs/results/step11_ttcs01_generator1_integration.md`. The boundary primitive is \(u_1^2+u_3^2+u_1u_2u_3\), not \(\sum u_i^2+u_1u_2u_3\); this auxiliary diagnostic was corrected in the independent script and did not enter the reported energy. The fixed margin is \(8.84\times10^{-4}\), so only a modest global bound is required.

## 4. Smooth collar

The stored profile agrees with complex hyperbolic space through the second \(x\)-jet at \(X\), because every free perturbation carries \((1-u)^3\). It is therefore a smooth bolt metric with a \(C^2\) direct CH attachment. Multiplying the third-order deviation by a flat cutoff in a collar of width \(\delta\) changes the curvature defect by \(O(\delta)\) pointwise on volume \(O(\delta)\), and hence changes \(J_6\) by \(O(\delta^3)\). Since the deficit is strict, sufficiently small \(\delta\) produces a smooth exact-CH-collar cell with \(J_6<8\pi^2\). A quantitative cutoff bound can be added after the frozen integral receives a theorem-level enclosure; no optimization enters this smoothing statement.

## 5. Consequence for O11

After scaling \(\widetilde g=6g\),
\[
\int|\operatorname{Ric}_{\widetilde g}+\widetilde g|^2dV_{\widetilde g}=J_6(g).
\]
For a complex-hyperbolic ball quotient, residual finiteness first supplies a fixed finite cover containing the required radius-\(\sqrt6\,\operatorname{arsinh}\sqrt8\) ball, plus a smoothing buffer. Further covers supply disjoint lifts proportional to the covering degree. The inherited one-cell transfer formula is
\[
\limsup\frac{\alpha(M_j)}{h_j}
\le \frac{28}{9}+\frac{J_1}{9\pi^2}
=4-\frac{8\varepsilon_0}{9},
\qquad \frac{J_1}{8\pi^2}=1-\varepsilon_0.
\]
For the frozen numerical value, \(\varepsilon_0=.0008837568647\), giving coefficient approximately
\[
3.9992144383<4.
\]
Accordingly, once the one remaining integral enclosure is completed, O11 has a negative answer: the handle coefficient four is not the blow-up coefficient. The upper construction uses a finite-scale perpendicular cell, not a bubbling Burns limit. The sharp blow-up coefficient is then the infimum of the complete-cell cost (including nonsymmetric cells), which remains open.

## 6. Relation to the logarithmic neck and curvature response

The Step-10 shrinking-cell family has
\[
J_6/(8\pi^2)=1-9x_0^2\log(1/x_0)+O(x_0^2).
\]
The fixed \(X=8\), \(x_0=.01\) cell produces a much larger practical deficit and shows that constant reduction is secondary to proving one cell. The logarithmic mechanism remains structurally important: it explains why the kernel direction \(\zeta\perp\omega\) is eventually subthreshold even though its first-order response vanishes.

A cheap exact sign test was recorded in `o11_neck_sign_quick.py`. Under analytic continuation from CH to the positive complex-space-form collar, the mixed constants reverse sign but the minimized P and J neck forms retain value \(-18\), so the integrated coefficient remains \(-9\) on both curvature signs. This supports a quadratic second-order curvature response: first order is \(-a^2\mathbf R^+(\zeta,\zeta)\), while the logarithmic kernel response is even in the ambient curvature. This continuation is not yet an independent general-bulk derivation, but it strengthens the conjectural coefficient \(-|\mathbf R^+|^2a^4\log(1/a^2)/4\) in the rank-one Kähler block, since \(|\mathbf R^+|^2/4=9\) for eigenvalue magnitude six.

## 7. Rigorous enclosure completed

Peer S1003A01 subsequently supplied `workspace/scripts/perp_rigorous_enclosure.py`, which implements a stronger version of the required regularization directly for the orthonormal Ricci tensor. It factors
\[
y=x-x_0,\quad F=y\widehat F,\quad G=y\widehat G,\quad w=y^2\widehat w,
\]
rewrites every Ricci component without removable bolt singularities, and calls python-flint's `acb.integral`. The integrator contracts the callback with `analytic=True` on complex ellipses; the code forwards this flag to every logarithm and square root, while the removable entire function \(\phi(z)=(e^z-1)/z\) uses a direct quotient away from zero and a series with a rigorous tail near zero. The witness is the exact binary64 coefficient vector stored in the JSON record, with \(x_0=1/100\) and \(X=8\) exact; this is a legitimate explicit real metric even though it is not the exact-decimal-rational witness proposed above.

I reran the enclosure independently at 160, 256, and 320 bits. TTCS identified one formal weakness in the peer implementation: the near-zero Taylor remainder radius for \(\phi\) was obtained by a float conversion with a large safety factor. `workspace/scripts/perp_rigorous_enclosure_strict.py` replaces this by the pure-Arb bound `abs(z).upper()` and otherwise preserves the bolt-regular Ricci code. Its 256-bit output is `workspace/data/o11_strict_arb_x001_X8_256.json`. At tolerance \(10^{-20}\), it gives
\[
\begin{aligned}
J_6/(8\pi^2)&\in[0.999116243135324311\pm2.25\times10^{-19}],\\
P/(8\pi^2)&\in[0.999108702733592648\pm4.58\times10^{-19}],\\
(J_6-P)/(8\pi^2)&\in[7.540401731663\times10^{-6}\pm3.80\times10^{-19}].
\end{aligned}
\]
The 160- and 320-bit runs also enclose the same value strictly below one. The upper bound certifies
\[
\boxed{J_6<8\pi^2},\qquad
\varepsilon_0:=1-J_6/(8\pi^2)>0.0008837568646756.
\]
The closed Ricci formula and all desingularized rewritings were checked symbolically against the independent Cartan derivation by `Sessions/S1003A01/workspace/scripts/check_bianchi_ricci_closed_form.py`; the run returned zero for all four Ricci components and the \(D_1,A_1,A_2,A_3\) rewrites. The binary64 coefficient vector is itself an exact dyadic-rational witness after freezing; at 256 bits `arb(float(v))` contains that dyadic with zero radius, so no optimizer convergence or uncertain target coefficients enter the proof.

Therefore the strict O11 counterexample is now a theorem: after smooth exact-CH attachment and residual-finite replication,
\[
\boxed{
\limsup_{j\to\infty}\frac{\alpha(M_j)}{h_j}
\le4-\frac89\varepsilon_0
<3.999214438342511<4.
}
\]
This disproves the universal coefficient-four conjecture for the balanced blow-up family. It does not determine the sharp coefficient: the cell infimum within and beyond diagonal \(SU(2)\) symmetry, a matching global lower bound, and the near-extremal structure remain open.

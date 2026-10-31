# Step 26 — Standard-CR truncation, Euler-flux collapse separation, and Einstein branch tests

Session S1003A02, Agent3. Conventions are those of Step 25: diagonal Bianchi IX metrics
\[
g=dt^2+\sum_{i=f,g,h}a_i^2\sigma_i^2,\qquad d\sigma_i=2\sigma_j\wedge\sigma_k,
\qquad W=a_fa_ga_h,
\]
with \(\int_{S^3}\sigma_{123}=2\pi^2\), \(\widehat P=P/(8\pi^2)\), normalized complex-hyperbolic Einstein constant \(\operatorname{Ric}=-6g\), and compact end variables \((y_f,y_g,y_h,\kappa,q,\zeta)\).

This note strengthens two parts of the conditional diagonal structure theorem and records what remains. The truncation direction is now reduced to explicit stable-mode estimates rather than an informal decay statement. For collapse, ordinary product/ALF Berger necks are separated from a developed Rossi interior by an exact Euler transgression; only a scale-invariant high-shear transition remains. The Einstein fate enumeration was also extended beyond \(b=.8\).

## 1. Independent reading of Lemma P

A two-branch TTCS verifier and peer S1003A01 independently checked the exact identity and constant. For every diagonal metric,
\[
\widetilde\Phi=q+\frac14(y_g-y_h)-\zeta\sinh q
\]
satisfies
\[
\widetilde\Phi'=F-\frac14(e_g-e_h),\qquad e_i=\operatorname{Ric}_{ii}+6,
\tag{1.1}
\]
where
\[
F=(y_g-y_h)\left(1-\frac{y_f+y_g+y_h}{4}-\zeta\cosh q\right)
+\zeta\sinh q\,(y_g+y_h-2)
+\frac{2\zeta^2}{\kappa^2}\sinh(2q).
\tag{1.2}
\]
The equality \(e_g-e_h=\operatorname{Ric}^\circ_{gg}-\operatorname{Ric}^\circ_{hh}\) is exact. In raw variables, \(F\) is not globally a regular multiple of \(\zeta^2\). In the ACH block coordinates of `ach_block_verify.py`, however, every transverse deviation is \(O(\zeta)\), and the exact symbolic computation in `ach_phi_drift.py` proves \(F=\zeta^2G\) with bounded polynomial/rational \(G\). This is the correct scope of the notation in Step 25.

Since
\[
P_I\ge \pi^2\int_IW(e_g-e_h)^2dt,
\]
weighted Cauchy--Schwarz gives
\[
\left|\Delta\widetilde\Phi-\int_IFdt\right|
\le\left(\frac{\widehat P_I}{2}\right)^{1/2}
\left(\int_I\frac{dt}{W}\right)^{1/2}.
\tag{1.3}
\]
All constants are correct. The peer check identified that the linear exterior null-line energy and Lemma P measure the **same** Rossi mismatch; they must not be added as separate charges. The script `squash_escape_cost.py` has one harmless output-only typo: the coefficient in \(w\sim e^{-4t}/8\) is extracted from \(we^{4t}\), not \(we^{-4t}\). Its numerical value function is unaffected.

A useful intrinsic block consequence, if \(y_g+y_h\ge c_B>0\) and \(\kappa\ge\kappa_{\min}>0\), is
\[
\widehat P_{[T,\infty)}\ge
4c_B\kappa_{\min}\frac{(|\widetilde\Phi(T)|-\delta(T))_+^2}{\zeta(T)^2},
\qquad
\delta(T)=\frac{\sup_B|G|}{2c_B}\zeta(T)^2.
\tag{1.4}
\]
This avoids choosing a radial origin. The earlier \(\frac12e^{4T}\) form follows from the stronger comparison \(W\ge ce^{4t}/16\).

## 2. The standard-CR truncation theorem

The TTCS verification computed the full spectrum at
\[
E(0)=(2,1,1,1,0,0):
\]
\[
\begin{array}{c|c|l}
\lambda&v_\lambda&\text{meaning}\\ \hline
 2&(4,-3,-3,5,0,0)&\text{outgoing Einstein mode},\\
 0&(0,0,0,0,1,0)&\text{Rossi/CR deformation},\\
 -2&(0,1,1,1,0,2)&\text{CH radial phase/defining-function mode},\\
 -4&(0,1,-1,0,-\tfrac12,0)&\text{physical antisymmetric mode},\\
 -6&(-4,1,1,1,0,0)&\text{physical symmetric mode},\\
 -8&(2,1,1,0,0,0)&\text{Einstein-constraint transverse mode}.
\end{array}
\tag{2.1}
\]
The exact CH orbit parametrized by \(z=\zeta\) is
\[
H(z)=\left(\sqrt{1+z}+\frac1{\sqrt{1+z}},\sqrt{1+z},\sqrt{1+z},\sqrt{1+z},0,z\right),
\tag{2.2}
\]
and \(H'(0)\) is half the \(-2\) vector. Thus the slow \(e^{-2t}\) mode is radial phase, not a physical metric perturbation. It must be matched exactly, rather than paid for in the splice.

For a non-Einstein scalar-\(-24\) end, the \(-8\) mode must be retained. If \(\mathcal C\) is the Einstein Hamiltonian constraint expression, then
\[
\mathcal C=e_0=-(e_f+e_g+e_h),\qquad e_0=\operatorname{Ric}_{tt}+6,
\tag{2.3}
\]
so this component is a forced response controlled by \(P\). The phrase in Step 25 that only rates \(4,6\) occur is exact for Einstein ends after phase matching, but not for general finite-\(P\), scalar-normalized ends.

**Theorem T (diagonal standard-CR truncation).** Let \(g\) be a complete diagonal metric whose tail remains in one sufficiently small standard ACH block. Assume
\[
s_g=-24,\qquad P(g)<\infty,\qquad \widetilde\Phi(t)\to0.
\]
Then there are diagonal metrics \(g_R\), equal to \(g\) on \(t\le R\) and exactly normalized CH on \(t\ge R+1\), such that
\[
P(g_R)\to P(g).
\tag{2.4}
\]
The same proof with \(J_6<\infty\) works without separately fixing scalar curvature, and gives \(J_6(g_R)\to J_6(g)\).

**Proof structure.** Subtract the exact CH state at the same \(\zeta\), so the \(-2\) phase is removed. Use transverse coordinates \(U,V_6,V_8,d,\widetilde\Phi\), with rates \(2,-6,-8,-4,0\). In the block, their controlled equations have the normal form
\[
V'=\Lambda V+N(\zeta,V)+B e,
\qquad |N|\le C(\zeta+|V|)|V|,
\tag{2.5}
\]
where \(e=(e_0,e_f,e_g,e_h)\). Since \(s=-24\),
\[
\widehat P_{\rm tail}=\frac14\int W\sum_\alpha e_\alpha^2dt,
\qquad W\asymp e^{4t},
\tag{2.6}
\]
so \(e^{2t}e_\alpha\in L^2\). Stable Duhamel formulas, the terminal integral formula for the bounded outgoing component, and (1.3) for the neutral component imply
\[
|U|+|V_6|+|V_8|+|d|+|\widetilde\Phi|=o(e^{-2t}).
\tag{2.7}
\]
Because \(\partial_q\widetilde\Phi=1-\zeta\cosh q\) stays positive, \(q=o(e^{-2t})\) too. For an Einstein end, \(e=0\), \(V_8=0\), and the stable-manifold expansion improves the physical deviation to \(O(e^{-4t})\).

Choose the CH radial phase so that its \(\zeta\) equals \(\zeta(R)\), and write \(D_i=\log a_i-\log a_i^{\rm CH}\). Then on a fixed interval,
\[
\sup_{[R,R+1]}(|D|+|D'|)=o(e^{-2R}).
\tag{2.8}
\]
Cut off \(D\) to zero on \([R,R+1]\). The diagonal Ricci formulas are affine in \(D''\), and the original \(D''\) is controlled by the residual equations. Therefore
\[
\int_{[R,R+1]\times S^3}|\operatorname{Ric}_{g_R}+6g_R|^2dV
\le C\int_R^{R+1}W|e|^2dt
+C\,W(R)\sup_{[R,R+1]}(|D|+|D'|)^2\to0.
\tag{2.9}
\]
The discarded tail has vanishing \(P\)-mass. This proves (2.4). The weakest useful fixed-width requirement is exactly the phase-matched \(o(e^{-2R})\) condition, plus vanishing weighted residual. No \(C^2\) decay assumption is needed separately.

This theorem closes the truncation direction in Theorem D once scalar normalization and block membership are stated. It also gives the correct logical implications:
\[
\text{standard-CR diagonal Einstein ACH filling}\Longrightarrow p_{1,0}^{\rm diag}=0,
\tag{2.10}
\]
and
\[
p_{1,0}^{\rm diag}=0+\text{attainment in the complete scalar-}(-24)\text{ class}
\Longrightarrow \operatorname{Ric}=-6g.
\tag{2.11}
\]
Zero infimum without compactness does not imply existence. Attainment occurs in the extended complete standard-CR ACH class; exact-CH-ended zero cost is impossible by exact-collar rigidity.

The Step-22 conformal barrier theorem has a different decay window: its Yamabe factor satisfies every rate \(4<m<2+2\sqrt3\), which is more than enough for its linear boundary transgressions. Theorem T uses a direct squared-residual splice and needs only physical rate greater than \(2\); the two thresholds are consistent and should not be conflated.

## 3. Euler flux and ordinary collapsed connectors

The TTCS generator proposed an Euler transgression. It was independently checked exactly against the Cartan curvature source. Define the intrinsic sectional curvature of a principal orbit by
\[
K^{(3)}_{jk}=
\frac{(a_j^2-a_k^2)^2+2a_i^2(a_j^2+a_k^2)-3a_i^4}
{a_i^2a_j^2a_k^2},\qquad \{i,j,k\}=\{f,g,h\},
\tag{3.1}
\]
and
\[
\mathfrak b=W\left(y_fK^{(3)}_{gh}+y_gK^{(3)}_{hf}+y_hK^{(3)}_{fg}-y_fy_gy_h\right).
\tag{3.2}
\]
The new script `workspace/scripts/verify_euler_flux_identity.py` imports the independent exact Cartan formulas and proves symbolically that on every diagonal annulus
\[
\widehat P(C)=\mathfrak b(t_1)-\mathfrak b(t_0)
+\frac1{4\pi^2}\int_C(|W^+|^2+|W^-|^2)
+\frac1{96\pi^2}\int_Cs^2.
\tag{3.3}
\]
The symbolic residual is exactly zero. It also verifies the normalization \(\mathfrak b=2\) on a Euclidean round sphere and
\[
\mathfrak b_{\rm CH}(t)=2-6\sinh^4t.
\tag{3.4}
\]
Thus
\[
\widehat P(C)\ge\mathfrak b(t_1)-\mathfrak b(t_0).
\tag{3.5}
\]

The script `workspace/scripts/ach_euler_flux.py` evaluated this flux on the validated Theorem-E transport. It verifies (3.4) symbolically and, using Arb on all 40 CAPD endpoint boxes at \(t=2.75\), proves
\[
\mathfrak b(T)\in[-64533.46135866161,-64275.41699256702].
\tag{3.6}
\]
The corresponding floating central value is \(-64403.79098545\); the same orbit has \(\widetilde\Phi\simeq0.78448\), so it has already acquired the Rossi infinity to within the validated tail drift \(<4.57\times10^{-4}\).

For a biaxial orbit \(a_g=a_h=A\), \(a_f=B\), let \(\lambda=B/A\), \(U=A'\), and \(V=A(B'/B)\). Then
\[
\mathfrak b=\lambda\left[V(4-3\lambda^2-U^2)+2U\lambda^2\right].
\tag{3.7}
\]
Hence a quasi-product Berger neck has \(\mathfrak b\approx0\), and an ALF neck with \(A\sim R\), \(B\to m\) has \(\lambda\to0\), \(U\to1\), \(V\to0\), again \(\mathfrak b\to0\). Any connector that evolves **outward** from the developed Rossi orbit (3.6) to such a neck pays at least about \(6.4\times10^4\) in units \(8\pi^2\), enormously above the certified \(0.99585\) cell cost.

This establishes a useful curved-neck extension of Lemma Q' for a natural class: collapse does not remove the charge of a developed ACH region when the later neck becomes quasi-product or ALF. The conclusion is scale invariant; shrinking the whole configuration does not change \(\mathfrak b\).

The remaining collapsed connector is much more specific: it must keep \(\mathfrak b\) highly negative by developing large normalized second fundamental form, rather than pass through an ordinary Berger or ALF regime. In volume/shape variables
\[
a_f=re^{2\beta/3},\quad a_g=re^{-\beta/3+q/2},\quad a_h=re^{-\beta/3-q/2},\quad h=\log r,
\tag{3.8}
\]
the diagonal defect has the exact scale-invariant action
\[
\widehat P=\int r^3\left(\frac3{16}H^2+\frac16E^2+\frac18D^2\right)dt,
\tag{3.9}
\]
where \(D=R_{gg}-R_{hh}\), \(E=R_{ff}-(R_{gg}+R_{hh})/2\), and \(H=R_{00}-(R_{ff}+R_{gg}+R_{hh})/3\). Under \(t=\varepsilon x\), \(r=\varepsilon R\), this action is unchanged. Thus small orbit volume alone does not make the high-shear connector cheap. The exact control equations supplied by TTCS are preserved in `trace/ttcs/results/step26_ttcs01_generator1_integration.md`; they should be independently symbolically checked before being promoted to a theorem.

Scientific consequence: the target configuration “Rossi Einstein interior + small ordinary Berger/ALF neck + standard CH exterior” is excluded. A possible cheap collapsed reset must occur **before** the orbit reaches a developed ACH state, or must follow a singular high-shear trajectory that never enters a product/ALF neck after the Rossi state. This is a much narrower branch than the generic Taub-bolt language suggested.

## 4. Einstein branch completeness tests

`workspace/scripts/ach_fate_enum.py` was run at additional bolt radii. The finite signed logarithmic \(d\)-grid is the same as at \(b=.8\); the computations are floating classification tests, not exhaustive interval proofs.

At \(b=.35\), the four fate changes are:
- a mirror ACH1/ACH2 pair at \(d=\pm0.00469762690656\), with \(\rho=2.808059256\) and reciprocal;
- remote SING/OTHER boundaries at \(|d|\approx4.37263\), whose closest ACH deviations exceed \(2.28\).
No ACH3 branch is approached.

At \(b=.2\), the same topology appears:
- a mirror ACH1/ACH2 pair at \(d=\pm6.16704965495\times10^{-6}\), with the positive branch approaching ACH1 to \(3.38\times10^{-5}\) and \(\rho\approx4.2387822\) (the finite closest-approach readout is less accurate than the projected section method);
- remote SING/OTHER boundaries at \(|d|\approx0.45038\), whose closest ACH deviations exceed \(3.14\).
Again there is no ACH3 approach.

At \(b=2\), the four fate changes again consist of the mirror ACH1/ACH2 pair at \(d=\pm1.55505759790\), with positive-branch closest-approach \(\rho\approx3.1718171\), plus remote SING/OTHER boundaries at \(|d|\approx59.2108\); every ACH3 deviation is at least \(1.0009\). At \(b=20\), the mirror pair is at \(d=\pm18.0795443515\), with \(\rho\approx26.951825\), while the remote boundaries lie at \(|d|\approx606.871\); every ACH3 deviation is at least \(1.043\). The large-b value agrees with the existing asymptotic \(\rho\sim1.343b\).

Together with the existing \(b=.8\) enumeration, these tests support one mirror perpendicular ACH pair and no aligned ACH branch across \(b=.2,.35,.8,2,20\). They also correct the earlier impression that the perpendicular branch starts near \(b=.29\): the branch persists at \(b=.2\), but \(d_*\) becomes extremely small and \(\rho\) grows. These runs do not prove branch completeness because a finite grid can miss a narrow double transition, and the labels OTHER/SING depend on finite-time thresholds. The proper next proof is interval fate enclosure plus asymptotics as \(b\to0,\infty\), not more root scans based on the flawed unstable-coordinate sign test.

## 5. Revised diagonal structure statement

With Theorem T, the noncollapsed standard-tail part of Theorem D no longer depends on an unspecified truncation assertion. The remaining hypotheses are:
1. scalar normalization or finite \(J_6\);
2. a common ACH block for the tails;
3. genuine compact-state and curvature bounds at the bolt and on compact intervals, not merely lower bolt/orbit-radius bounds;
4. exclusion of high-shear collapse/interior necks and large-bolt escape;
5. a validated no-return statement for large-volume face excursions.

Under these hypotheses, a minimizing sequence converges to a complete standard-CR diagonal minimizer in the extended ACH class, and its value equals the exact-ended infimum by Theorem T. The equivalence between zero value and a standard-CR diagonal Einstein filling then follows only with attainment. Theorem E cannot supply such a filling by late, large-volume CR correction; ordinary post-Rossi Berger/ALF collapse is now also excluded by (3.5)--(3.7). The hard residual geometry is the high-shear scale-invariant connector, together with the large-bolt and phase-portrait branches.

## 6. Files and status

New exact/checking files:
- `workspace/scripts/verify_euler_flux_identity.py`: exact Cartan verification of (3.3), residual zero.
- `workspace/scripts/ach_euler_flux.py`.
- `workspace/data/ach_capd/euler_flux_b0.8.json`: symbolic CH/Euclidean checks, floating trajectory profile, and Arb enclosure (3.6).
- `workspace/data/ach_fate/fate_b0.2.json`, `fate_b0.35.json`, `fate_b2.json`, `fate_b20.json`.
- TTCS integration: `trace/ttcs/results/step26_ttcs01_verifier1_integration.md` and `step26_ttcs01_generator1_integration.md`.

Proved or reduced to explicit estimates this step: Lemma-P scope and constants; mode classification; phase-matched truncation theorem for scalar-\(-24\) diagonal ends; exact Euler-flux identity; certified flux of the validated Rossi filling; exclusion of post-developed-Rossi product/ALF connectors.

Still open: an independently checked coercive lower bound for the high-shear action; validated global face portrait/shadowing; complete interval enumeration of all Einstein ACH branches for every bolt radius; large-bolt coercivity; unrestricted non-diagonal collapse.

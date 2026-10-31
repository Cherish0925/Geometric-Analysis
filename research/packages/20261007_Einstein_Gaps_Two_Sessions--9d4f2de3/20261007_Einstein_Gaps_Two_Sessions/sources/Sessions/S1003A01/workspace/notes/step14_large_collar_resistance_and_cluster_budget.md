# Step 14 — Large-collar continuation, quantitative resistance, and a many-cell energy ceiling

## 1. What was tested

The pair-tail experiment from Step 13 is a genuine numerical interaction between two **fixed witnesses**, but its deepest continuation is not to multiply its best pair value by a coordination number. Two questions were separated:

1. How much cost can any cluster remove while geometrically protected cores remain unchanged?
2. Does increasing the exact-CH collar radius reveal an inexpensive long drift toward the perpendicular ACH Einstein trajectory, or a finite positive resistance to the standard conformal infinity?

The functional is in the \(\operatorname{Ric}=-6g\) normalization,
\[
 J_6(g)=\int |\operatorname{Ric}+6g|^2,\qquad
 P(g)=\int |\operatorname{Ric}^{\circ}|^2,
\]
reported in units of \(8\pi^2\).

## 2. A cluster bound that precedes packing

Let \(g_i\) be isolated exact-collar cells and choose pairwise disjoint protected cores \(C_i\), on which a cluster metric is required to agree with \(g_i\). Positivity of the defect density gives the exact inequality
\[
 J(g_{\rm cluster})\ge \sum_i J(g_i;C_i).
\]
Therefore
\[
 \boxed{\sum_iJ(g_i)-J(g_{\rm cluster})
 \le \sum_i J(g_i;M_i\setminus C_i).}\tag{2.1}
\]
This bound counts each adjustable exterior once, independent of how many neighbours it meets. At quadratic order the same fact is
\[
 \int\Big|\sum_iAh_i\Big|^2\ge0,
\]
so one cannot minimize every pair cross term independently and add the minima.

`scripts/cell_exterior_budget.py` computes the right side for the frozen radial cells. For the certified \(X=8\) witness, choosing the largest Step-13 overlap \(w=1.6\) protects only
\[
 r<\rho-w=0.16275,
\]
not the weak tail \(r<1\). The adjustable one-cell energy is
\[
 J(r>0.16275)/(8\pi^2)=0.15106,
\]
whereas the observed pair saving is only \(1.25\times10^{-5}\). For a pair, (2.1) therefore permits as much as \(0.30213\); it is far too weak to constrain ordinary finite-coordination packing in this deep-overlap geometry. Thus the \(r>1\) value \(1.99\times10^{-4}\) cannot be used to dismiss that experiment, but neither may the pair saving be multiplied freely. If instead one explicitly protects \(r<1\), the adjustable energy is \(1.99\times10^{-4}\) per cell.

The bound is deliberately geometric: its force depends on where the cores are frozen. It supplies a universal ceiling for frozen-core clustering but says nothing comparable once core regions are jointly reoptimized. The tabulated exterior values are numerical radial quadratures (the \(X=8\) total differs from the stored cost by \(2.21\times10^{-7}\)); the inequality itself is exact.

## 3. The pair effect weakens for the better \(X=16\) cell

A second 4D autodiff run used the independently validated \(X=16\) profile. At overlap depths \(w=1.2,1.4,1.6\), the best phases gave
\[
 \Delta J/(8\pi^2)=-1.91\times10^{-7},\ -6.11\times10^{-7},\ -1.54\times10^{-6},
\]
respectively (`data/pair_overlap/sweep_X16_check.json`). The weight-four phase law persists, but the \(w=1.6\) saving is eight times smaller than for \(X=8\). The nonlinear difference from the quadratic term remains about \(10^{-8}\), and the sampled metrics remain positive.

This confirms the structural interaction but changes its role: optimizing a larger single cell suppresses separated frozen-tail cooperation rather than amplifying it. Certification of the pair sign would be mathematically reusable, but is not the principal lever on the upper coefficient.

## 4. Physical continuation to larger collars

The old `perp_collar_scan.py` starts from zero and stretches the transition across the whole logarithmic interval. To test the true monotone cell problem, `scripts/perp_collar_continue.py` was introduced. It first extends the previous optimized cell by an exact CH annulus, projects that same physical metric into a higher-degree Chebyshev basis on the larger interval, and then optimizes. The projection is not energy preserving at finite degree, so it is only an initialization; the final profile is evaluated and enclosed independently by the cancellation-free Arb code.

The continuation produced:

| outer \(X\) | degree | \(J_6/(8\pi^2)\), rigorous enclosure | certified \(\eta=1-J\) |
|---|---:|---:|---:|
| 8 | 8 | \(0.999116243135324311\pm2.24\times10^{-19}\) | \(0.0008837568646756\) |
| 16 | 8 | \(0.99890294372\) (prior enclosure) | \(\approx0.0010970563\) |
| 32 | 12 | \(0.99873676987\pm7.43\times10^{-12}\) | \(0.0012632301285\) |
| 64 | 16 | \(0.99870276448\pm6.15\times10^{-12}\) | \(0.0012972355165\) |

The new authoritative outputs are:

- `data/perp_collar/continued_X16_to_X32_J_d12.json`
- `data/perp_collar/rigorous_continued_X16_to_X32_J_d12.json`
- `data/perp_collar/continued_X32_to_X64_J_d16.json`
- `data/perp_collar/rigorous_continued_X32_to_X64_J_d16.json`.

The corresponding \(P\) values are rigorously below one as well:
\[
 P_{32}/(8\pi^2)=0.99873214738\pm8.39\times10^{-12},\qquad
 P_{64}/(8\pi^2)=0.99870008590\pm7.30\times10^{-12}.
\]
The same analytic positivity, bolt smoothness and exact-collar smoothing argument used for the \(X=8\) witness applies to these profiles. Hence the \(X=64\) cell improves the existential balanced-sequence construction to
\[
 \limsup\frac{\alpha(M_j)}{h_j}
 \le 4-\frac{8\eta_{64}}9+\varepsilon
 <3.998846902+\varepsilon,
\]
for arbitrarily small smoothing loss \(\varepsilon>0\). This remains an upper construction, not the unrestricted optimum.

The improvement increments in \(\eta\) are approximately \(2.13,1.66,0.34\times10^{-4}\) from \(8\to16\to32\to64\). This is evidence of saturation near a positive cost, not proof of the limit or of optimality within the ansatz. The \(X=64\) optimizer stopped with gradient infinity norm \(3.2\times10^{-3}\), so further basis/optimization work could still lower it.

## 5. Fixed-radius geometry suggests a complete asymptotic profile

`scripts/large_collar_profile_compare.py` compares the metrics at fixed physical CH radii. For \(X=8,16,32,64\), the ratios of the four diagonal coefficients to CH and the defect shell densities stabilize on compact radii. Representative examples:

- At \(r=0.3\), the radial ratio is about \(1.095,1.093,1.092,1.092\), while the collapsing-slot ratio is about \(0.862,0.861,0.860,0.860\).
- At \(r=1.0\), the radial ratio is about \(1.0166,1.0165,1.0168,1.0171\), and the two nontrivial tangential ratios are near \(0.98\)--\(0.99\).
- At \(r=1.6\), the \(X=32,64\) ratios differ only at roughly \(10^{-4}\), and the shell energy is \(5.48\times10^{-5}\) versus \(4.77\times10^{-5}\).

The data are in `data/perp_collar/large_collar_profile_compare.json`. They support compact convergence toward a complete finite-energy diagonal CH-asymptotic metric rather than a transition that simply runs outward. This remains numerical: coercive compactness and the asymptotic mode are not yet proved.

The tail decomposition also changes systematically. For the \(X=32\) and \(X=64\) profiles, the energy beyond \(r=1\) is dominated by the perpendicular weight-two mode:
\[
 (E_{\rm inv},E_{\rm wt2})_{r>1}
 =(1.21\times10^{-5},3.03\times10^{-4}),
 \quad(8.95\times10^{-6},2.65\times10^{-4}).
\]
Thus the same channel responsible for pair phase-locking is the slowly decaying single-cell mode, but its integrated cost stays finite.

## 6. The Rossi neutral mode has finite positive ACH resistance

The peer Einstein shooting gives perpendicular ACH Einstein fillings with Rossi ratio \(\rho\gtrsim2.196\), while exact CH has \(\rho=1\). Put
\[
 q=\log(a_2/a_3),\qquad \Delta=\log(2.196)=0.7866375.
\]
Near an ACH trajectory the neutral mode satisfies schematically
\[
 q''+4q'=f,
\]
where \(f\) is forced by trace-free Ricci defect. The essential point for a calibration inequality is the weight. In a noncollapsed ACH end, orbit volume grows like \(e^{4t}\), so the reduced action is
\[
 \mathcal A_T(q)=\int_0^T e^{4t}(q''+4q')^2dt,
\quad q(0)=0,\ q(T)=\Delta,\ q'(0)=q'(T)=0.\tag{6.1}
\]
`scripts/neutral_mode_resistance.py` solves this exactly. The minimum is exactly
\[
 \inf\mathcal A_T=
 \frac{\Delta^2}{(1-e^{-4T})/64-T^2e^{-4T}/[4(1-e^{-4T})]}
 \longrightarrow64\Delta^2=39.6031,\tag{6.2}
\]
already within \(2.3\%\) at \(T=2\) and \(3\times10^{-5}\) at \(T=4\). In contrast, the same problem **without** the ACH weight has minimum tending to zero (numerically \(0.639\) by \(T=16\), with \(\sim T^{-1}\) behavior). The exact output is `data/perp_collar/neutral_mode_resistance.json`. The script's field `resistance` is the compliance \(\Delta^2/\mathcal A_T\to1/64\); the energetic coefficient is \(64\).

The quantity directly differentiated by the forcing is the flux-corrected mode
\[
 \Phi=q+\frac14q',\qquad \Phi'=\frac14(q''+4q').
\]
The clamped endpoint conditions make \(\Delta\Phi=\Delta q\), but a free entrance slope changes this conclusion: \(q(t)=\Delta(1-e^{-4t})\) solves the homogeneous equation with zero action and nonzero initial slope. Hence a long noncollapsed ACH transition does not destroy resistance only when the volume normalization and the relevant boundary flux are controlled. A quantitative cell lower bound can fail through collapse of the orbit-volume coefficient, departure from the ACH regime, concentration in another mode, or loss of entrance-slope control. This is the precise missing content in an invariant estimate
\[
 |\Delta\Phi|^2\le \frac{P}{8\pi^2}R_\Phi.
\]
The endpoint ratio mismatch alone is not enough; one needs a uniform **upper** bound on the actual compliance \(R_\Phi\), or equivalently a lower comparison of the true action with (6.1), together with a nonzero flux-corrected mismatch.

## 7. What this changes

The evidence now joins three previously separate facts:

1. Exact diagonal Einstein fillings miss standard CH infinity by a finite Rossi displacement (peer computation).
2. Larger exact-collar competitors appear to converge on compact sets and their costs saturate near \(J/(8\pi^2)\approx0.9987\), rather than tending rapidly toward zero.
3. The reduced neutral mode has a finite positive action for arbitrarily long ACH transitions because of the \(e^{4t}\) volume weight.

Together they support a quantitative diagonal coercivity programme: prove that every low-cost cell enters a uniformly noncollapsed ACH tube; compare its neutral-mode forcing with \(|\operatorname{Ric}^{\circ}|\); control the entrance flux; then use the Rossi endpoint separation and the weighted action. For an actual diagonal metric, if \(W=a_1a_2a_3\) and \(q=\log(a_2/a_3)\), subtracting the \(22\) and \(33\) Ricci equations yields
\[
 (Wq')'=W(V-E),\qquad
 V=\frac{4(a_2^2-a_3^2)(a_2^2+a_3^2-a_1^2)}{W^2},
\]
where \(E=(\operatorname{Ric}^{\circ})_{22}-(\operatorname{Ric}^{\circ})_{33}\) and \(|\operatorname{Ric}^{\circ}|^2\ge E^2/2\). Thus the nonlinear calibration must also control the potential term \(V\), not merely replace \(W'/W\) by four. What is still missing is decisive and explicit: low-cost compactness into the tube, a uniform orbit-volume comparison, bounds for this potential contribution, entrance-flux control, and rigorous separation of the Einstein filling map from \(\rho=1\). Without these, the numerical Einstein nonexistence statement does not imply a positive least defect.

The pair interaction remains a reusable phase mechanism, but the large-collar/resistance connection now bears more directly on a matching lower theory for \(\mathfrak J_{1,0}\) and on degeneration of minimizing cells.

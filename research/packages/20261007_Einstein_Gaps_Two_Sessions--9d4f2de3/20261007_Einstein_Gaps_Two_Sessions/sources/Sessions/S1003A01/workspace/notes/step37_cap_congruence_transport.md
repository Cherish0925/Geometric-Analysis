# Step 37 — Congruence transport of the full certified cell into the Calabi cap

Conventions: closed-family scale `Ric=-g`, \(D=\int|\operatorname{Ric}+g|^2\), \(P=\int|\operatorname{Ric}^\circ|^2\), values reported as \(D/(8\pi^2)\). The certified CH cell has \(D/(8\pi^2)\le0.995670030355131\) (`data/step33/rigorous_x00.03_X128_d20_J_exact.json`). Everything below is floating (scrambled Sobol, stratified radial shells) evidence for a construction question, not an enclosure or a lower bound.

## 1. Construction

Let \(g_*\) be the certified \(x_0=.03,\ X=128\) perpendicular cell, scaled by 6 and written in the CH exponential chart \(\xi\in\mathbb R^4\) at its centre (`step36` marking, \(x=\sinh^2(r/\sqrt6)\)). Off the bolt, \(g_*\) and \(g_{\rm CH}\) are diagonal in the same Euclidean-orthonormal equivariant frame \(v_0=z,\ v_1=(-\bar z_2,\bar z_1),\ v_2=iv_1,\ v_3=iz\), so
\[
L=(g_{\rm CH}^{-1}g_*)^{1/2}=\sum_k\sqrt{\lambda_k/\lambda_k^{\rm CH}}\;v_kv_k^{T}
\]
is explicit. With the \(C^3\) smoother \(H\) on \(a<r<b\) and \(\bar g=(1-H)g_{\rm CH}+Hg_{\rm out}\),
\[
G=L\,\bar g\,L\quad(r\ge a),\qquad G=g_*\quad(r<a).
\]
\(G\) is positive by congruence; it equals \(g_*\) identically when \(g_{\rm out}=g_{\rm CH}\) (any \(a,b\)); it equals \(g_{\rm out}\) for \(r\ge R_{\rm cell}=\sqrt6\operatorname{arsinh}\sqrt{128}=7.6451\), because the profile is exactly CH there. Bolt, topology, rel-boundary marking and the exact exterior are those of the certified cell. A variant tapers the deformation, \(L_{\rm taper}=L^{1-H((r-c)/(d-c))}\). Script: `scripts/step37_cap_congruence_transport.py`; core \(r<a\) is integrated radially exactly (step36 `core_integrals`), the rest in 4D.

**Pipeline check.** With \(g_{\rm out}=g_{\rm CH}\), the 4D shells plus the radial core give \(0.99568\) (\(2^9\) points/shell, `data/step37/ch_control_a05_b15_n9.json`) and \(0.99565\pm0.0019\) (\(2^{11}\), `data/step37/base/base_ch_s1.json`), reproducing the certified value. The CH control is therefore exact by construction, removing the representation loss of Step 36 (which gave 1.54 for its CH control).

## 2. Cap results in the step-36 (Fermi-type) chart

The cap \(g_C\) is written in \((X,Y)\) flat divisor coordinates and \((Z,W)\) proper normal exponential coordinates; this is a Fermi-type chart about \(D'\), not the cap's exponential chart at \(p\).

| construction | \(D/(8\pi^2)\) | file |
|---|---|---|
| \(a=.5,b=1.5\), full cell | 2.330 | `cap_a05_b15_n9.json` |
| \(a=.45,b=.7\), full cell | 1.916 ± 0.010 (two seeds 1.9165, 1.9157) | `base/base_cap_s{1,2}.json` |
| \(a=.43,b=.6\) | 1.880 ± 0.010 | `base/base_cap_a043_b06_s1.json` |
| \(a=.45,b=.7\), taper 2:4 (CH same: 1.145) | 1.383 | `scan/` |
| \(a=.45,b=.7\), taper 2.5:6 (CH same: 1.014) | 1.410 | `scan/` |
| wider/later bands, e.g. \(a=.5,b=3\) | 6.26 | `scan/` |

The excess over CH is positive in every radial shell. Angular binning (`scripts/step37_excess_angular.py`, `data/step37/angular/excess_angular.json`, \(2^{13}\) points/shell) by \(c_2=(|z_1|^2-|z_2|^2)/r^2\) (\(+1\): divisor directions, \(-1\): normal directions) localizes it:

- near-bolt band \(0.45<r<0.7\): excess \(0.155\), largest in the most normal bin (0.053 of it);
- \(0.7<r<2\): small (0.025);
- tail \(2<r<7.65\): excess \(0.74\), concentrated in intermediate normal-leaning directions \(c_2\in[-0.75,-0.25]\) and nearly zero along \(D'\).

Since the far cap is locally almost CH (\(|W^-|^2=8/(3u^6)\)), a tail excess concentrated away from \(D'\) indicates that most of it is caused by the marking, i.e. by comparing a CH-exponential object with a Fermi-type cap chart, rather than by \(W^-\) itself.

## 3. Response optimization (Fermi chart)

`scripts/step37_cap_response_opt.py` adds 350 compactly supported \(U(1)_-\)-invariant modes: 7 radial \(C^3\) bumps from 0.45 to 6.6, angular functions \(1,c_2,c_2^2,\operatorname{Re}(z_1z_2)/r^2,\operatorname{Im}(z_1z_2)/r^2\), and all 10 symmetric products of the transported orthonormal coframe. L-BFGS used 20 shells × \(2^{10}\) nodes, then was validated on two fresh \(2^{12}\)-per-shell seeds (`data/step37/opt1/`):

| run | base | optimized, validated |
|---|---|---|
| cap, full cell | 1.9152 | 1.8961, 1.8955 |
| cap, taper 2.5:6 | 1.4006 | 1.3828, 1.3825 |
| CH, full cell | 0.995674 | 0.995676, 0.995676 |
| CH, taper 2.5:6 | 1.01428 | 1.00178, 1.00178 |

In-sample and validation values agree, so there is no overfitting. However, the coefficients stayed below \(1.3\times10^{-3}\) after 200 iterations: the modes are badly scaled, because the large-volume outer bumps dominate the gradient. These numbers therefore bound what this optimizer achieved; they do not measure the response infimum. Two facts are nevertheless robust:

1. The certified CH cell shows no descent in this nonsymmetric \(U(1)_-\) space; the in-sample change was \(-4\times10^{-6}\) and validation shows none.
2. With the same modes, about 0.0125 of the CH taper loss is recovered, but the cap's excess of about 0.9 does not move appreciably.

## 4. Cap in its own geodesic normal coordinates

`scripts/step37_cap_expmap_transport.py` pulls the cap back by its exponential map at \(p\in D'\), \(\phi(\xi)=\gamma_\xi(1)\). It uses 64-step RK4 for the geodesic equation, with all derivatives taken by JAX through the discrete flow, and the cap metric is rewritten to be analytic at \(D'\) using series for \(u,q/n^2\). Checks (`data/step37/expmap/smoke.json`):

- Gauss lemma \(g_{\rm exp}\xi=\xi\) to \(10^{-12}\)–\(10^{-5}\) for \(r=.5\)–\(7.6\);
- the same ODE exponential map applied to the Bergman metric reproduces the analytic CH chart to \(3\times10^{-11}\)–\(10^{-5}\);
- \(\det D\phi>0\) at the sampled radii, with no conjugate point;
- relative cap–CH metric difference \(0.03,0.20,0.63,0.17,0.17\) at \(r=.5,1.5,3,5,7.6\), versus a ratio of order 10 in the Fermi chart at large \(r\).

This is the geometrically correct marking for the Strategist's congruence transport.

**Results** (`data/step37/expmap/runs/`, 16 quadratic shells × \(2^9\), compared on identical edges with the CH control `ch_control_expedges_s1.json`, whose value is 0.99562):

| run | \(D/(8\pi^2)\) | total shell excess over CH |
|---|---|---|
| \(a=.45,b=.7\), seed 1 | 1.0522 ± 0.008 | +0.0566 |
| \(a=.45,b=.7\), seed 2 | 1.0632 ± 0.008 | +0.0676 |
| \(a=.43,b=.6\), seed 1 | 1.0571 ± 0.011 | — |
| \(a=.45,b=.7\), taper 2.5:6 | 1.0666 ± 0.008 | (taper loss included) |

Changing the marking from Fermi-type to exponential lowers the cap value from **1.916 to about 1.057**. The Fermi-chart tail excess of 0.74 was almost entirely marking. The remaining excess, about \(+0.06\pm0.01\), separates into two parts:

- **Interpolation band** \(0.48<r<0.70\): \(+0.047\) to \(+0.057\). This is the cost of switching from \(g_{\rm CH}\) to \(g_C\) under \(L\) near the bolt, where \(g_C-g_{\rm CH}\approx-\frac13W^-(\xi,\cdot,\xi,\cdot)=O(0.03)\). It is an artifact of the trial's interpolation; the true cost of re-adapting the core is not known.
- **Intrinsic tail interaction** \(0.7<r<7.65\): \(+0.0100\) (seed 1) and \(+0.0100\) (seed 2), spread smoothly with no interpolation. Here \(G=L g_{\rm exp}L\) and \(g_{\rm exp}\) is exactly Einstein, so this is the response of the unchanged certified deformation to the cap's \(W^-\) geometry. Its sign is **positive**.

Symmetry explains why there is no favorable linear term at the centre. The transported cell is invariant under the standard \(SU(2)\subset U(2)\), which acts on \(\Lambda^-\) as \(SO(3)\). The constant part of \(W^-(p)\) has spin 2 in \(\Lambda^-\), so its first-order pairing with the cell vanishes. Linear pairings with the cell first arise from the \(SU(2)\)-invariant part of the four-jet of \(W^-\) (\(\nabla^4W^-\)) and from terms quadratic in \(W^-\). Neither has a sign that makes the cap favorable here.

**Distance from the divisor** (partial, `data/step37/expmap/runs_n0/`, still running). The cell centre is placed at normal distance \(n_0\) from \(D'\), using an exponential chart with orthonormal frame \(\operatorname{diag}(u^{-1/2},u^{-1/2},1,n_0/\sqrt q)\), which preserves the complex orientation. The band shell \(0.48<r<0.56\) has CH value 0.28147. The cap values are

| \(n_0\) | band shell value | excess |
|---|---|---|
| 0 | 0.3008, 0.3050 | +0.019 to +0.024 |
| 0.5 | 0.2915 | +0.010 |
| 1 | 0.2832 | +0.0017 |
| 2 | 0.28145 | ≈0 |
| 3 | 0.28148 | ≈0 |

The decay is fast, consistent with \(|W^-|\propto u^{-3}\). The tail shells for \(n_0>0\), where the cell's long collar reaches back toward \(D'\), were still being computed when the Step closed. With 64 steps, Gauss-lemma residuals reach \(10^{-3}\) at \(r=7.6\) for \(n_0>0\); increase `--nstep` for final numbers.

## 5. Current understanding

1. The Strategist's congruence transport realizes the full successful CH cell inside an exact Calabi cap with exact outer geometry, unchanged bolt, and exact CH control. Under the correct exponential marking, the cap version of the certified cell costs \(D/(8\pi^2)\approx1.057\). That is about 6% above the CH cell, not the factor 2 seen in Step 36.
2. No tested ingredient gives a cap advantage:
   - band placement;
   - taper;
   - 350 nonsymmetric \(U(1)_-\) response modes, which were badly scaled (Fermi chart);
   - distance from the divisor (band part).
   The only intrinsic piece measured cleanly, the tail interaction of the unchanged deformation with \(W^-\), is \(+0.010\).
3. The Step-36 conclusion that the cap is "intrinsically" much more expensive was a marking effect. Comparisons of cells across environments must use exponential (geodesic normal) charts at the centre. Fermi-type charts produce O(1) spurious costs at the 7.6 collar scale.
4. The certified CH cell showed no descent along 350 compactly supported \(U(1)_-\)-invariant nonsymmetric modes (validated change \(<3\times10^{-6}\)). This is weak evidence of stationarity beyond the diagonal sector, limited by the mode scaling.
5. Orientation reversal identifies CH's \(\omega\) with the cap's \(\bar\omega\). That would place the cell in a Kähler-type positive \(W^+_{\rm eff}=\operatorname{diag}(4/3,-2/3,-2/3)\) environment, analogous to Fubini–Study, which lowered Kähler cells in Step 8. It would also turn the blow-up into a \(\mathbb{CP}^2\) summand relative to the background orientation. This is a different signed-surgery problem with different Seiberg–Witten field supply, and it is not pursued in the current problem.

**Remaining constructive questions.**
- Re-optimize the core in the cap using exponential-chart responses concentrated on \(0.43<r<1.5\), with modes scaled by local volume. The question is whether the +0.05 band loss is mostly removable, and whether the residual is of order \(|W^-|^2\) and positive.
- Finish the \(n_0\) sweep, including the tail. This gives the sign and the decay of the full environment effect.
- Compute the far-regime linear coefficient. Expect it to vanish at leading order by the \(SU(2)\) spin argument above.

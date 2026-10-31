# Step 35 — The b₊ calibration, its leaves, and what the non-round input (N) actually lacks

Conventions: Steps 27–34. Scale-free state \(X=(x,z,p,\chi,\eta)\), \(q=-3\log z\), controls \(c=(\bar H,\bar E,\bar D)\), running cost \(L(c)=\frac3{16}\bar H^2+\frac16\bar E^2+\frac18\bar D^2\) (units \(8\pi^2\)).

## 1. Exact calibration statement

The chiral identity (Theorem X) gives, pointwise in \(\tau\),
\[
L(c)-\dot{\mathfrak b}_+(X,c)=\frac1{2\pi^2}|W^+|^2+\frac1{96\pi^2}s^2\quad(\text{normalized density})\ \ge0 .
\]
\(\dot{\mathfrak b}_+\) is affine in \(c\) and \(L\) is a positive-definite quadratic form \(M=\mathrm{diag}(3/16,1/6,1/8)\). Step 34 (`scripts/hj_symbolic_reduction.py`) proved \(\sup_c(\dot{\mathfrak b}_+-L)\equiv0\), attained at
\[
c^*=\Bigl(-\tfrac43\partial_p\mathfrak b_+,\ -3\partial_\chi\mathfrak b_+,\ 2\partial_\chi\mathfrak b_+-4\partial_\eta\mathfrak b_+\Bigr).
\]
Hence, exactly,
\[
\boxed{\;L(c)-\dot{\mathfrak b}_+=L(c-c^*)=:\omega_+\;,\qquad \widehat P=\Delta\mathfrak b_++\int\omega_+\,d\tau .}
\]
**Consequences.** (i) The calibrated curves (\(c=c^*\)) are exactly the diagonal metrics with \(W^+=0\), \(s=0\) (ASD scalar-flat). (ii) \(\ker M=0\), so the Cauchy–Schwarz route "\(\dot I=\ell\cdot(c-c^*)\Rightarrow\int\omega_+\ge(\Delta I)^2/\int\ell^TM^{-1}\ell\)" has no kernel defect; the human's first condition is automatically satisfied here. What remains for such a bound is a transverse function \(I\) with nonzero endpoint separation and a uniform denominator along *all* competing paths.
(iii) Corrections to the strategist note: Burns is a calibrated leaf (cost \(=\Delta\mathfrak b_+=1\)); **Taub-bolt is not** (it is Ricci-flat, \(\Delta\mathfrak b_+=-3\), \(\int|W^+|^2\)-part \(=3\)); CH is not (its ball from the centre has \(\Delta\mathfrak b_+=-9\sinh^4\tau\) and \(\int\omega_+=9\sinh^4\tau\)). Numerically \(L(c^*)=\dot{\mathfrak b}_+(c^*)\) to \(10^{-13}\) relative at random states, and \(\mathfrak b_+(\mathrm{ch}(\tau))=2-9\sinh^4\tau\) to \(10^{-15}\) (`data/saturation_control/calibrated_flow_leaves.json`).

## 2. The calibrated leaves through the two endpoints (endpoint separation)

`scripts/calibrated_flow_leaves.py` integrates \(f(X,c^*(X))\):

* **Forward from the Λ-Taub–NUT collapsed entry** (\(\varepsilon=1/16,1/64\); \(A=.5,1,2\)): every leaf converges to the Euclidean round fixed point \(X_0=(0,1,1,0,0)\), \(\mathfrak b_+\uparrow2\). This is the ASD scalar-flat decollapse found by the optimizer (cost \(2-\mathfrak b_+^{\rm entry}\to4\)). The transverse block at \(X_0\) has eigenvalues \(-2,-4\): the round point attracts the antisymmetric sector.
* **Backward from exact CH jets** \(\mathrm{ch}(\tau)\), \(\tau\in\{.5,.70,.72,.74,.758,.8,1,1.5,2.3\}\): every leaf stays in the biaxial set \(\Sigma=\{q=0,\eta=0\}\) and blows up (\(\chi\to\infty\), \(\mathfrak b_+\to-\infty\)) in finite \(\tau\in[.03,.66]\). None approaches the collapsed set or the bolt.

\(\Sigma\) is invariant under the full controlled flow with \(D=0\) and under the calibrated flow (exact \(g\leftrightarrow h\) symmetry; \(D^*|_\Sigma=0\) symbolically). All CH jets lie in \(\Sigma\); the collapsed entry has \(q\simeq\log(1/\varepsilon)\). **So the endpoint leaves are separated, and the separating coordinate is the antisymmetric pair \((q,\eta)\), which the controls reach only through \(\bar D\).** This is the structural reason the non-round costs are \(D\)-dominated (68% at cap \(-1\)).

## 3. The transverse block and the resisting region

On \(\Sigma\) the calibrated Jacobian splits; its antisymmetric block in \((q,\eta)\) is exactly (`scripts/transverse_block.py`)
\[
A_\Sigma=\begin{pmatrix}0&1\\ 8\chi e^{-2x/3}+8e^{2x/3}-16e^{-4x/3} & \tfrac43\chi+2e^{4x/3}-8e^{-2x/3}\end{pmatrix},
\]
independent of \(p\). Along CH jets the eigenvalues are \((-1.79,-4.00)\) at \(\tau=.2\), \((-0.31,-3.84)\) at \(.6\), \((0.24,-3.75)\) at \(.70\), \((0.59,-3.69)\) at \(.758\), \((1.56,-3.52)\) at \(.9\), \((-3.09,4.17)\) at \(1.2\): \(\Sigma\) is transversally attracting for \(\tau\lesssim.66\) and of saddle type beyond — exactly in the cap region \(\tau\ge.70\). However, sampling \(\Sigma\cap\{\mathfrak b_+\le-1\}\) (283 496 points, \(|x|\le3,|p|,|\chi|\le10\)) gives 38% transversally attracting, 62% saddle, <1% repelling points. Hence \(\Sigma\) contains capped states where the antisymmetric sector can be entered for free. **No static/frozen argument excludes a cheap non-round connector; the missing quantity is path weight**, namely the minimal \(\int L(\bar D-\bar D^*)\) to carry \(q\) from \(\log(1/\varepsilon)\) to the attracting part of \(\Sigma\) while \(\mathfrak b_+\le-1\), plus the symmetric-sector cost inside \(\Sigma\) to reach a CH jet. This is the precise "resisting region" asked for in the relay, and it agrees with Lemma Z and the Step-34 HJ result.

Of the three possible missing items (kernel direction, endpoint separation, path weight): the kernel is trivial (§1), endpoint separation holds structurally (§2), and **path weight is the open item**.

## 4. Two calibrations: \(\mathfrak b_+\) and the CH-renormalized \(B\)

The \(\mathfrak b_+\) decomposition is exact and nonnegative but degenerates at a CH end: for opening at \(t_{CH}=2.28\) (cap \(-1\) optimizer) \(\Delta\mathfrak b_+\approx-5024\) and \(\int\omega_+\approx5030\); the useful information is a tiny difference of huge terms. S1003A01's interface (their Step 29, verified there to \(6\times10^{-11}\)) supplies the CH-renormalized charge
\[
B=\mathfrak b_+-3\mathcal F-9\mathcal P_m^2-6Wuu',\qquad B_{\rm bolt}=1,\ B_{\rm CH}=2,\qquad \widehat P[t_0,t_1]=\int L_{AK}+\Delta B,
\]
with \(L_{AK}\) indefinite, whose only negative term is the Nijenhuis energy \(-6\nu^2d\widehat V\). Thus \(B\) has universal endpoint values but is not a calibration; \(\mathfrak b_+\) is a calibration but has endpoint values of size \(e^{4t}\). The lower problem for (N) is to interpolate between them: use \(\mathfrak b_+\) (with \(\omega_+\ge0\)) on the collapsed/swap band, and \(B\) (with the far-zone Hardy positivity of the Nijenhuis sector) on the CH tail, matched at an interface where both are finite. The certified subunit cells live entirely in the \(B\)-regime (negative Nijenhuis middle zone); a collapsed connector must cross the \(\mathfrak b_+\) band first. This matching is the concrete construction to attempt next; it requires the AK moment \(\mathcal P_m\) (defined from the perpendicular bolt) to be controlled across the collapsed band.

## 5. Corrections to the first draft of this note

An earlier version of this file (same step) evaluated \(L_{AK}\) on the scale-free saturation trajectories by finite differences, obtaining \(\int\mathrm{Ric}^\circ{}^2\approx351\) against the stored cost \(6.48\). That evaluation ignored the \(r\)-scaling of the scale-free variables and is invalid; `scripts/calibration_ak_analysis.py` and `data/saturation_control/calibration_ak_analysis.json` must not be used. The identity \(\widehat P=1+\int L_{AK}\) holds for whole cells from the smooth bolt to CH, not for connectors starting at a collapsed entry, so "\(\int L_{AK}=\mathrm{cost}-1\)" for saturation trajectories was wrong. The survey of 47 optimizer outputs (round reopening \(2.33\to3.99\) as \(\varepsilon\downarrow0\); caps \(1,0,-.5,-1,-1.5,-2.5\) give \(4.03,4.81,5.50,6.48,7.89,11.87\); late windows \(\tau\ge3\) up to \(2848\)) consists of feasible local-optimizer values, not lower bounds.

## 6. Status of (N)

(N) is now a named numerical-margin input: collapsed non-round connectors cost \(\approx5.4\)–\(6.6\) in all computed instances versus the needed \(>1-\mathfrak b_+\)-prefix accounting. Proved structure: the \(\mathfrak b_+\) calibration with trivial kernel; ASD scalar-flat calibrated leaves; leaf separation of collapsed entry (→ round point) and CH jets (in \(\Sigma\), backward blow-up); the explicit transverse block and its attracting/saddle regions in the cap. Open: the path-weight bound of §3, most plausibly via the \(\mathfrak b_+\)/\(B\) matching of §4.

Artifacts: `scripts/calibrated_flow_leaves.py` → `data/saturation_control/calibrated_flow_leaves.json`; `scripts/transverse_block.py` → `data/saturation_control/transverse_block.json`; Step-34 `scripts/hj_symbolic_reduction.py`.

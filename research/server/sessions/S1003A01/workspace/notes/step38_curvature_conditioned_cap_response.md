# Step 38 — Curvature-conditioned response of the transported cell

Conventions: \(\operatorname{Ric}=-g\),
\[
D(g)=\int|\operatorname{Ric}+g|^2,\qquad D/(8\pi^2)
\]
is the reported local cost.  All new values are floating JAX/Sobol calculations, not interval bounds.  The certified CH reference remains
\[
D(g_*)/(8\pi^2)\in[0.995670030344086,0.995670030355131].
\]

## 1. Purpose and representation

Step 37 showed that putting the full certified cell into the Calabi cap by the cap exponential chart reduces the apparent penalty from about \(0.92\) in the Fermi marking to about \(0.06\).  The remaining test had two numerical weaknesses: total-action sampling was noisy compared with the certified saving, and the 350 raw modes were poorly conditioned in a fourth-order objective.

`scripts/step38_expmap_gn_response.py` implements the two requested repairs.

* The base is the Step-37 congruence transport in the cap's geodesic normal chart.
* A response is a sum of compactly supported radial/angular symmetric-coframe tensors, with the nonlinear representation
  \[
  g(c)=B(c)^Tg_0B(c),\qquad B=I+\tfrac12g_0^{-1}h(c).
  \]
  Its first variation at zero is exactly \(h\), since \(B^Tg_0B=g_0+h+\frac14h g_0^{-1}h\). It is positive whenever \(B\) is nonsingular; the sampled minimum eigenvalues are positive but do not prove nonsingularity at every continuum point. The trial used here has support \(0.45<r<0.78\), so it leaves a whole bolt neighbourhood and all bolt jets unchanged.
* At the fitting nodes, the residual is the ten-component Cholesky-frame tensor \(\operatorname{Ric}(g)+g\), weighted so the Euclidean square is the quadrature approximation to \(D/(8\pi^2)\). If \(J\) is the derivative of this complete weighted residual, the singular-value decomposition of \(J\) removes weak directions and the map \(T=V\Sigma^{-1}\) makes \(JT\) orthonormal. Thus optimization uses the discrete Gauss--Newton form of the full moving-frame, moving-volume residual map. At a non-Einstein base this includes derivatives of the frame and volume as well as \(D(\operatorname{Ric}+g)[h]\); it is not the intrinsic frozen-weight Einstein-operator norm. This is nevertheless the directly relevant conditioning for the nonlinear least-squares objective.
* Validation uses paired samples.  On each common point it subtracts the CH cell density including its own volume factor.  More importantly for the response itself it also subtracts the unmodified cap base density.  The resulting differences are much less noisy than either total.

## 2. CH control

The well-sampled CH run is `data/step38/ch_band_gn1_fit32.json`: one radial bump, ten symmetric tensor components, 32 Sobol nodes in each of three fitting shells.  All ten curvature-residual singular directions were retained; their singular values range from \(13.676\) to \(0.0734\).  In whitened units the full linear least-squares direction has norm only
\[
6.60\times10^{-4}.
\]
The nonlinear one-step line test changes the fitted support cost from \(0.68057087199\) to \(0.68057044577\).  Four independent paired validation replicates give a mean partial change
\[
(-5.89\pm9.10)\times10^{-7}
\]
(the uncertainty here is across scrambled replicates).  Therefore this conditioned radial response space sees no material descent of the certified CH cell.  This is a clean statement about these ten modes, not unrestricted stationarity.

## 3. Cap response: what the coarse and refined fits show

The first coarse fit `data/step38/cap_band_gn1_cv.json` used only four nodes per fitting shell. The whitened direction appeared large (norm \(9.36\times10^{-2}\)) and lowered the in-sample support cost by \(0.00992\), but paired validation found it **increased** the response-region action by
\[
+0.00870\pm0.00109.
\]
This is a direct demonstration that curvature-residual whitening repairs coefficient scaling but cannot replace adequate spatial sampling: a high-leverage anisotropic direction can still fit four nodes and fail off-sample. The failure is localized: the two inner validation shells improve by about \(-0.0115\), while the outer shell \(0.597<r<0.78\) rises by roughly \(+0.019\) to \(+0.022\), reversing the net sign. In the JSON the field named `response_improvement` is actually \(D_{\rm opt}-D_{\rm base}\), so positive means worse.

The refined cap calculation `data/step38/cap_band_gn1_fit32.json` uses the same ten-mode family with 32 Sobol fitting nodes per shell and independent paired validation. Its whitened linear-response norm is \(2.94\times10^{-2}\), about 45 times the CH control. The nonlinear line gives an in-sample support reduction of \(8.55\times10^{-4}\), but the four paired validation replicates give
\[
D(g_{\rm opt})-D(g_{\rm base})
=(+7.05\pm7.26)\times10^{-4}
\]
over \(0.45<r<0.78\), where the uncertainty is the standard error across four scrambled replicates. Thus no net responsive improvement is resolved. The shell pattern is stable: the first two shells improve by about \(-0.00275\) to \(-0.00334\), while the outer shell increases by \(+0.00206\) to \(+0.00475\). This shows a genuine inward response coupled to an unresolved or adverse outer compensation, not an everywhere-unfavorable direction. Sampled minimum metric eigenvalues stay above \(0.1115\).

The paired optimized cap-minus-CH difference over this band is \(0.05897\pm0.00953\) across replicates. It is only a band quantity and cannot be added to the certified total as though it were the full cap correction. Only the paired opt-minus-base integral is complete for the response because the response vanishes outside the band. The refined fixed-bolt response therefore supplies no reason to invest further in more versions of the same outer-bolt-preserving one-bump family, but it speaks only about the transported certified deformation and this responsive family. It does not determine a cap-cell infimum, exclude cap-adapted bolt area/jets, exclude mixed topology, or imply a background-independent lower principle.

## 4. Centre displacement

The Step-37 background task `s37_t34_tool2` was cancelled in Step 38 after more than three hours of computation. It had reached only \(r\approx2.25\) for the normal offsets \(n_0=0,0.5,1,2,3\), with no final JSON totals. The useful partial shell records remain in `data/step37/expmap/runs_n0/*.log`; the authoritative cancelled record is `workspace/tasks/s37_t34_tool2/result.json`. Completing the very expensive centre sweep did not resolve the construction question now addressed more directly by the conditioned response, and the long collar prevents interpreting it as a weak-environment expansion in any case. These partial values locate geometric effects but do not isolate powers of \(|W^-|\): the cell radius \(7.645\) allows inward directions to return to the strong cap region. Any later quantitative use should first replace the slow higher-derivative exponential-map pipeline and compare 64/128-step markings. The current response calculation uses a 16-step discrete exponential map; JAX differentiates that discrete map exactly, but its marking should be checked against 32/64/128 steps before quantitative interpretation.

## 5. Relation to the paired-field work

Peer messages 805--806 and
`Sessions/S1003A02/workspace/notes/step42_ak_torsion_profile_taubes_goldberg.md`,
`step43_w0_cotton_quadratic_law_and_debts.md` change the global interpretation.

* On a closed blow-up with the stated basic-class hypotheses, a nowhere-zero self-dual harmonic form cannot have zero exceptional period.  The local perpendicular cell is consistent because its canonical closed self-dual form degenerates at the bolt.  The transported-cell calculation therefore does **not** realize the excluded closed symplectic common mode.
* The cap and CH have the same \(R^+\) seen by the first Burns response.  No existing flux, monopole, or transgression identity fixes the sign of the \(SU(2)\)-invariant \(O(|W^-|^2)\) environment term.  The Step-37 positive \(+0.010\) tail is construction evidence for one unchanged deformation and marking, not an intrinsic cap tariff.
* The corrected model tensor is \(W_0=(\rho^2/4)(I/3-nn)\), and for closed almost-Kähler first jets
  \[
  |\delta W_0|^2=\tfrac13|d(\rho^2/4)|^2+\tfrac{\rho^4}{32}|\nabla n|^2.
  \]
  The missing global estimate is differential: Cotton supplies \(\nabla\operatorname{Ric}^\circ\), not a quantity controlled linearly by \(P=\int|\operatorname{Ric}^\circ|^2\).  A completed integration-by-parts route naturally gives a conditional quadratic scale \(P\gtrsim R^2/A\), unless additional perturbative spectral structure is available.

These results separate the two most informative next directions.  On the construction side, vary bolt area or a small number of bolt-compatible jets if the refined fixed-bolt band remains expensive; shell modes supported outside \(r=.45\) cannot test that freedom.  On the global side, pursue either a cover-uniform perturbative Armstrong estimate near the KE host or a closed approximate common mode that records exceptional areas/zero sets, amplitude, \(W^+-W_0\), Nijenhuis energy, and the AK\(\Gamma\) defect.  A zero-period nowhere-vanishing almost-Kähler model is topologically unavailable.

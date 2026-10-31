# Step 86 route map: from ordinary Moser to a weighted localization/resolvent problem

> **SUPERSEDED by Step 87 route map.** The resolvent comparison theorem gives a clean
> universal threshold δ* ≈ 0.246 without local Moser iteration.

## Established in the free-OT reflected class

1. Exact orbit maps obey the Step 85 comparison
   \[
   \tfrac12Le\ge\tfrac12e(e-6),
   \qquad
   \sup e\le\max\{6,\sup_{\rm exit}e\}.
   \]
   Together with the center average at least `12`, this excludes exact connectors with low-energy exits.

2. For \(\|E\|_{\rm op}\le\delta\), the orbit forcing is geometrically small:
   \[
   F=\tau_\sigma(U)\leftrightarrow-2\widehat E_0,
   \qquad |F|\le2\delta.
   \]
   No expanding-collar conformal factor remains in this invariant norm.

3. The correct weighted curvature input is
   \[
   \operatorname{Ric}^{4}_{f}
   =-3\gamma_B+\tfrac12U^*h+E_B
   \ge-(3+\delta)\gamma_B,
   \qquad f=-\sigma.
   \]
   It gives effective-four-dimensional normalized local geometry on buffered balls, not an unnormalized volume-independent Sobolev constant.

4. For \(u=(e-k_*)_+\),
   \[
   k_*=3+b+\sqrt{(3+b)^2+2f^2}=6+O(\delta),
   \]
   the exact superlevel reaction is \(Su^2+u^3/2\). Small exit data yield global Dirichlet, \(L^2\), and \(L^3\) control proportional to the weighted measure of the superlevel set.

## What Step 86 ruled out as an immediate argument

- The divergence term does not reduce only to a cutoff pairing under the superlevel test. It also contributes
  \[
  -\int\eta^2\langle V,\nabla u\rangle.
  \]
- Local normalized Moser regularity does not automatically produce the near-sharp global ceiling \(6+C\delta\).
- A \(C^0\)-small tension may have a large derivative on a thin layer and cancel the quartic Bochner reaction pointwise.
- Neither a radius-scale bound \(C(1+r^{-2})\) nor a global unnormalized excess bound contradicts the center floor by itself.

## Main mathematical opportunity

The exact round cusp has more than a curvature-dimension lower bound. Its measure is \(e^{3r}drdz\), and the drift operator
\[
L=\partial_{rr}+3\partial_r+e^{-2r}\partial_{zz}
\]
has radial Dirichlet gap
\[
\lambda_1(-L)\ge\frac94+\frac{\pi^2}{4R^2}.
\]
The gap remains \(9/4\) as length grows. The coupled area equation may force an approximate version of this expansion/spectral structure even for nontrivial orbit maps.

The next high-value task is therefore to derive a length-independent massive-resolvent or superlevel localization estimate from the **full coupled area equation**, not from \(CD(K,4)\) alone. A concrete new variable is
\[
W=e+c|\nabla\sigma|^2.
\]
The area equation \(L\sigma=6-\operatorname{tr}_{\rm orb}E\) combines with the orbit Bochner formula to give, schematically,
\[
\tfrac12LW\ge\operatorname{div}_\sigma J+rac{W^2}{2(1+c)}-(3+\delta)W-D_c(\delta)+\mathcal P,
\quad |J|\le2(1+\sqrt c)\delta\sqrt W,
\]
with \(\mathcal P\ge0\). For \(c=1/2\), the zero-defect reaction threshold is `9`, below the center floor `12`. Moreover, a bound \(W\le B\) would imply a weighted Cheeger gap through \(L\sigma\ge6-2\delta\). This creates a nonlinear bootstrap candidate rather than assuming spectral control externally.

Useful equivalent targets are:

1. a uniform bound for the gradient of the Green kernel of \(-L+S\) on the doubled connector with low-energy exit data;
2. a weighted Cheeger/Poincaré lower bound recovered from orbit-area expansion;
3. a density or inradius lower bound for every component of \(\{e>k_*\}\);
4. an elliptic consequence of the full OT system excluding \(C^0\)-small, \(C^1\)-large \(F=-2\widehat E_0\) layers;
5. or a constraint-compatible construction of such a layer, which would identify the escape mechanism rather than merely show an estimate failed.

## Scope

Even success would exclude only reflected, free-\(T^2\), orthogonally transitive connectors with controlled exits. Approximate twist, nonfree actions, and general graph metrics remain outside the theorem. The \(N\#N\) route has collapsing \(T^2\) axes and needs a different treatment. The positive branch remains independent.

## Evidence

- `workspace/notes/step86_forced_bochner_superlevel_and_localization.md`
- `workspace/scripts/step86_forced_caccioppoli_verify.py`
- `workspace/data/step86_forced_caccioppoli_verify.json`
- `workspace/scripts/step86_weighted_cylinder_spectrum.py`
- `workspace/data/step86_weighted_cylinder_spectrum.json`
- `workspace/scripts/step86_combined_orbit_area_energy.py`
- `workspace/data/step86_combined_orbit_area_energy.json`
- `trace/ttcs/results/step86_ttcs01_generator1_integration.md`
- `trace/ttcs/results/step86_ttcs01_verifier1_integration.md`

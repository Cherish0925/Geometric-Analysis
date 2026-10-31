# Step 13 — Two certified cells with overlapping CH tails: a phase-locked weight-two interaction

Session S1003A01, Agent2, Execute.  Builds on the certified frozen perpendicular cell
(`data/perp_collar/x0.01_X8_J_d8.json`, strict enclosure `strict_rigorous_x0.01_X8_J_d8.json`,
\(J_6/(8\pi^2)=0.999116243135324311\ldots\)) and the Step-12 two-blow-up programme
\(\mathfrak J_{8,7}\le 4\mathfrak J_{2,0}+224\pi^2\).

## 1. The trial metric and the exact localisation identity

Normalisation \(\operatorname{Ric}_{CH}=-6g\) (holomorphic sectional curvature \(-4\)); ball model
\(g_B=\operatorname{Re}\big[|dz|^2/(1-|z|^2)+|\langle dz,z\rangle|^2/(1-|z|^2)^2\big]\), so
\(r(0,z)=\operatorname{artanh}|z|\).  The frozen cell lives on \(x_0\le x\le X=8\), \(x=\sinh^2 r\), and
on the region \(x>x_0\) it is written over CH as \(g_1=g_B+h_1\) with \(h_1\) diagonal in the CH
orthonormal coframe \((dr,\ \sinh r\,\sigma_{\rm bolt},\ \sinh r\,\sigma_{\rm contact},\ \sinh r\cosh r\,\sigma_{\rm fibre})\):
\[
 g_1=\sum_s\lambda_s(r)\,(\hat e^s)^2,\qquad
 \lambda=\Big(\frac{x+x^2}{G},\ \frac{F}{x},\ 1,\ \frac{e^{w}}{1+x}\Big),
\]
and \(h_1=0\) for \(r\ge\rho=\operatorname{asinh}\sqrt X=1.762747\).  In ball coordinates the cell
frame at \(z\) is \((z,\ jz,\ kz,\ iz)\) (quaternionic \(C^2=\mathbb H\)), the fibre being \(J\nu=iz\).
The second cell is \(g_2=(\varphi_a\circ L_\theta)^*\)-transport of the same cell, \(\varphi_a\) the
holomorphic involution exchanging \(0\) and \(a=(\tanh d,0)\) (the geodesic symmetry of the midpoint)
and \(L_\theta z=e^{i\theta}z\), which rotates the cell's contact frame by \(2\theta\).  Modulo the
symmetries of the two cells, \((d,\theta)\) parametrise all relative placements.

Trial metric: \(g_{12}=g_B+h_1+h_2\).  If \(d\ge\rho+r_0+\) margin, \(r_0=\operatorname{asinh}\sqrt{x_0}\),
each tail vanishes near the other bolt, so \(g_{12}\) is a \(C^{2,1}\) metric on \(D\#2\overline{\mathbf{CP}}{}^2\)
with an exact CH exterior; the Step-10 \(O(\delta^3)\) cutoff lemma applies verbatim near each sphere
piece (the second tail is smooth there), so smoothing changes \(J\) by \(o(1)\).  Outside the lens
\(L=B_\rho(0)\cap B_\rho(a)\) the metric coincides with one cell or with CH, hence exactly
\[
 J(g_{12})-J(g_1)-J(g_2)=\int_L\Big(|E(g_{12})|^2dV_{g_{12}}-|E(g_1)|^2dV_{g_1}-|E(g_2)|^2dV_{g_2}\Big),
 \qquad E=\operatorname{Ric}+6g,
\]
with quadratic part \(2\int_L\langle E(g_1),E(g_2)\rangle_{g_B}dV_B\) and a remainder that is cubic
in the tail data.  Overlap depth \(w=2\rho-d\); the admissible range is \(0<w<\rho-r_0\approx1.66\).

## 2. Phase structure (exact at quadratic order)

The cell defect is diagonal, \(E={\rm diag}(E_0,E_1,E_2,E_3)\) (radial, bolt slot, contact slot,
fibre).  Under \(L_\theta\) only the contact block moves; writing \(m=(E_1+E_2)/2\), \(d=(E_1-E_2)/2\),
the traceless part \(d\) has weight two in the rotation angle \(2\theta\), i.e. weight four in \(\theta\).
Hence the quadratic interaction is exactly
\[
 I(w,\theta)=I_0(w)+\operatorname{Re}\big(I_4(w)e^{4i\theta}\big),\qquad
 \min_\theta I=I_0-|I_4|,
\]
and \(I_0\) is the pairing with the phase average (\(U(2)\)-invariant part) of the second defect.
So a strict saving exists for some phase as soon as \(|I_4|>I_0\), whatever the sign of \(I_0\).

## 3. Computation

`scripts/pair_overlap_trial.py` builds \(g_B,h_1,h_2\) explicitly in \(\mathbb R^4\) and computes all
Ricci tensors by forward-mode autodiff of the coordinate metric (no symmetry used).
`scripts/pair_overlap_check.py`: \(|\operatorname{Ric}(g_B)+6g_B|\le5\times10^{-15}\); the autodiff
\(|E(g_1)|^2\) equals the Bianchi-IX value \(\sum_a(R_{aa}+6)^2\) of `FrozenCell` at
\(r=0.3,\dots,1.75\) to 12–14 digits (e.g. 26.14499751412 vs 26.14499751412 at \(r=0.3\)).  Lens
integrals use scrambled Sobol points (\(2^{15}\) per run) in cell-1 polar coordinates; two seeds
at \(w=1.5\) differ by 0.5%.  Data: `data/pair_overlap/sweep_X8/w*_s0.json`, table
`data/pair_profile/pair_overlap_table_X8.csv`, figure `figures/pair_overlap_interaction_X8.png`.

| \(w\) | \(\Delta J/8\pi^2\), \(\theta=0\) | \(\theta=\pi/8\) | \(\theta=\pi/4\) | best saving | \(\int_L|E_1|^2/8\pi^2\) | max \(|\Delta J-{\rm quad}|\) |
|---|---|---|---|---|---|---|
| 0.1 | \(3.74\times10^{-10}\) | \(1.70\times10^{-10}\) | \(-3.26\times10^{-11}\) | \(3.3\times10^{-11}\) | \(3.4\times10^{-10}\) | \(3\times10^{-15}\) |
| 0.4 | \(4.43\times10^{-8}\) | \(-3.7\times10^{-9}\) | \(-5.17\times10^{-8}\) | \(5.2\times10^{-8}\) | \(5.8\times10^{-8}\) | \(9\times10^{-12}\) |
| 0.6 | \(1.446\times10^{-7}\) | \(-1.0\times10^{-9}\) | \(-1.467\times10^{-7}\) | \(1.5\times10^{-7}\) | \(2.1\times10^{-7}\) | \(3\times10^{-10}\) |
| 0.8 | \(1.59\times10^{-7}\) | \(1.0\times10^{-8}\) | \(-1.39\times10^{-7}\) | \(1.4\times10^{-7}\) | \(6.2\times10^{-7}\) | \(3\times10^{-9}\) |
| 1.0 | \(-2.95\times10^{-7}\) | \(-2\times10^{-9}\) | \(2.95\times10^{-7}\) | \(3.0\times10^{-7}\) | \(2.8\times10^{-6}\) | \(7\times10^{-9}\) |
| 1.2 | \(-1.75\times10^{-6}\) | \(1.9\times10^{-8}\) | \(1.80\times10^{-6}\) | \(1.8\times10^{-6}\) | \(1.8\times10^{-5}\) | \(2\times10^{-8}\) |
| 1.4 | \(-5.29\times10^{-6}\) | \(5.6\times10^{-8}\) | \(5.43\times10^{-6}\) | \(5.3\times10^{-6}\) | \(1.7\times10^{-4}\) | \(5\times10^{-8}\) |
| 1.6 | \(-1.2455\times10^{-5}\) | \(9.6\times10^{-8}\) | \(1.283\times10^{-5}\) | \(1.25\times10^{-5}\) | \(6.1\times10^{-3}\) | \(6\times10^{-8}\) |

The trial metric stayed positive (smallest coordinate eigenvalue 0.62 at \(w=1.6\)).

## 4. What the numbers say

1. **The interaction is almost purely weight-two.**  \(I_0\approx\Delta J(\pi/8)\) is \(10^{-2}\) of the
   amplitude; \(\Delta J(0)\approx-\Delta J(\pi/4)\).  The reason is visible in the radial
   decomposition (`scripts/pair_defect_profile.py`, `data/pair_profile/defect_profile_X8*`,
   `figures/pair_defect_profile_X8.png`): for \(r>1\) the weight-two energy \(2\int d^2\) is
   \(1.80\times10^{-4}\) against \(1.87\times10^{-5}\) for the invariant part.  The optimised cell's
   tail defect is a perpendicular-plane anisotropy — the \(\omega^\perp\) channel of Steps 7–8 —
   and the scalar/fibre components are nearly paid off.
2. **The preferred phase flips with depth.**  \(d(r)\) changes sign once, at \(r=1.297\).  The lens
   is centred near \(r=\rho-w/2\), which crosses \(1.297\) at \(w\approx0.93\); the observed switch of
   \(\operatorname{Re}I_4\) between \(w=0.8\) and \(1.0\) matches.
3. **Near tangency the pair repels.**  `scripts/pair_boundary_jet.py`
   (`data/pair_overlap/boundary_jet_X8.json`): the one-sided collar jet of \(E\) is
   \(e=(0.04889,\,0.09456,\,0,\,-0.04566)\) per unit geodesic depth (the contact slot vanishes because
   \(h_2\equiv x\)).  As \(w\to0\), \(I\sim 2\langle e,R_\theta e\rangle\int_L(\rho-r_1)(\rho-r_2)\sim c\,w^{9/2}\),
   with \(\min_\theta\langle e,R_\theta e\rangle=e_0^2+e_3^2+2e_1e_2=0.00448>0\), and the cubic remainder is
   \(O(w^{15/2})\).  So the collective saving comes from the interior structure of the tail, not from
   the collar jet; the crossover lies below \(w=0.1\).
4. **Size.**  The best saving, \(1.25\times10^{-5}\cdot8\pi^2\) at \(w=1.6\), is 1.4% of the certified
   single-cell deficit \(\eta_8=8.84\times10^{-4}\) and 0.2% of the Cauchy–Schwarz scale
   \(\int_L|E_1|^2\).  The nonlinear remainder is \(<0.5\%\) of the saving.  If certified it would give
   \(J_{20}\le2\overline J_{10}-1.2\times10^{-5}\cdot8\pi^2\) and lower the balanced coefficient by
   \(\frac49\times1.2\times10^{-5}\approx5\times10^{-6}\) through
   \(\mathfrak J_{8,7}\le4\mathfrak J_{2,0}+224\pi^2\).  The \(X=8\to16\) single-cell improvement
   (\(\Delta\eta=2.1\times10^{-4}\)) is seventeen times larger.

## 5. Status and consequences

* **Status.**  Numerical: QMC lens integrals of autodiff curvature, double precision, seed variation
  0.5%, sign margin about 200 standard errors at \(w\ge1.2\).  Not a certificate.  A certificate would
  need (i) a validated 4D lens integral of the quadratic term, which involves only the two radial
  defect profiles (already Arb-enclosable) and explicit CH frame-transport algebra, and (ii) an explicit
  pointwise bound for the cubic remainder in terms of \(|h|,|\nabla h|,|\nabla^2h|\) on \(L\).
* **Strict non-additivity of explicit constructions is real** in negative curvature, and its channel
  is identified: phase-locking of the weight-two perpendicular anisotropy of the tails.  The sum
  \(I_0\) (the orientation-averaged interaction) is essentially zero, so a random-phase cluster is
  additive to \(10^{-7}\); only phase-aligned neighbours save.
* **Quasi-additivity mechanism.**  An optimised cell puts \(>99.9\%\) of its defect inside \(r<0.8\);
  frozen-tail interaction is bounded by the tail energies and is tiny.  Collective savings comparable to
  \(\eta\) therefore require (a) many phase-aligned neighbours per cell (hyperbolic packing at
  \(d\approx1.9\) allows many; frustration of the phase field around triangles is the open
  question), (b) a jointly relaxed exterior, or (c) genuine core–core cooperation at distances below
  \(\rho+r_0\), where the tail representation breaks and a cohomogeneity-two (e.g. toric, two
  iterated blow-ups at a \(T^2\)-fixed point) ansatz is needed.
* The single-cell infimum \(\kappa_1=\mathfrak J_{1,0}/8\pi^2\) remains the dominant lever for the
  upper bound; S1003A02's Step-13 finding (diagonal \(SU(2)\) Einstein fillings of
  \(D\#\overline{\mathbf{CP}}{}^2\) are ACH with Rossi-sphere infinity, ratio \(\ge2.196\), never
  standard) bears directly on whether \(\kappa_1\) is bounded away from zero in the class.

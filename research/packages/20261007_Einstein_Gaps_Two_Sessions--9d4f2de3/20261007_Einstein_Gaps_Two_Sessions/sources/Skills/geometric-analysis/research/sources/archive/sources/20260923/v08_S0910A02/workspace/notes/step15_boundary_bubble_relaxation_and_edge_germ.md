# Step 15: pinched relaxations, localized edge curvature, and the boundary-bubble germ

Session S0910A02, Agent3/Actuator, Execute.

## 0. Scope relative to Yau Problem 26

The active goal remains the full sign-unrestricted Yau-26 proposition.  This
step does **not** prove or refute the proposition, and it does not even prove
or refute the four-dimensional positive branch.  It attacks one sharpened
subproblem from Steps 13--14: in the simply connected toric/invariant laboratory,
can the positive branch volume gap fail through many collapsing fixed spheres
(rods), i.e. through localized negative base curvature / boundary bubbles?

The Step-15 strategist correctly warned that solving the **exact** reduced
Einstein system on polygons with many corners is the wrong computation for the
pinched problem.  The relevant object is a sequence of \(\delta\)-pinched
metrics with \(\delta\to0\), not exact Einstein metrics on high-corner toric
polygons.  Exact equations remain useful only as local models and obstruction
limits.

## 1. Source-scope correction about the exact toric list

The strategist's practical warning against exact high-corner Einstein searches
is right, but the source status must be stated carefully.

* The paper `Toric Einstein 4-manifolds with non-negative sectional curvature`
  says that compact Hermitian Einstein four-manifolds have a complete
  classification: Kähler-Einstein del Pezzo metrics plus the Page and
  Chen--LeBrun--Weber exceptions (object lines 37--38).  It also says that the
  general \(T^2\)-invariant Einstein case is "much less known" (line 41).  Its
  main classification theorem is under the additional assumption of
  non-negative sectional curvature (Theorem 1.1, lines 47--49).  Therefore we
  should **not** cite it as a complete classification of all smooth
  \(T^2\)-invariant positive Einstein four-manifolds.
* LeBrun's Hermitian theorem (`On Einstein, Hermitian 4-Manifolds`, lines
  24 and 40--44) classifies compact Hermitian Einstein four-manifolds as
  Kähler-Einstein, Page on \(\mathbb{CP}^2\#\overline{\mathbb{CP}}^2\), or
  Chen--LeBrun--Weber on \(\mathbb{CP}^2\#2\overline{\mathbb{CP}}^2\).  This is
  a Hermitian/conformally Kähler statement, not an arbitrary invariant
  Einstein classification.
* The exact-system search on \(m=8,10\) would still be a poor test of the
  Yau-26 pinched volume-gap question: failure to find an exact Einstein metric
  on a high-corner toric/quasitoric topology would not rule out
  \(\delta\)-pinched collapsing metrics, and success would be a major exact
  Einstein discovery rather than the intended relaxation test.

## 2. R0: coarse edge-ODE / spectral / Gauss--Bonnet relaxation collapses

File: `workspace/scripts/step15_boundary_bubble_relaxation.py`.
Data: `workspace/data/step15_boundary_bubble_relaxation.json`.

The coarsest model uses only the Step-14 rod equation for a constant edge
curvature
\[
  K_B|_{\text{edge}}=-A,
  \qquad Q''+(1+2A)Q=0,
\]
with smooth two-sphere endpoint conditions \(Q(0)=0,Q'(0)=1,Q(L)=0,Q'(L)=-1\).
Then
\[
  L=\frac{\pi}{\sqrt{1+2A}},\qquad
  \Phi=\int_0^L Q(s)\,ds=\frac{2}{1+2A},
\]
where \(\Phi\) is the rod flux / fixed-sphere area divided by \(2\pi\).
For a polygon with \(m=\chi\) rods, taking \(A=m^2\) gives
\[
  \Phi_{\rm total}=m\frac{2}{1+2m^2}\sim \frac1m,
  \qquad
  \operatorname{Vol}_4=2\pi^2\Phi_{\rm total}\to0.
\]
The base area can be kept fixed above the Step-13/14 Faber--Krahn floor, and
the negative Gauss--Bonnet curvature can be stored in boundary collars whose
width is comparable to the bubble scale in this relaxation.

**Conclusion.**  The unweighted spectral area lower bound, signed
Gauss--Bonnet, and rod unit closure alone cannot prove a \(\chi\)-uniform volume
gap.  They permit a formal collapse if edge curvature is allowed to become
very negative and nonuniform/localized.  Any BUILD proof must use additional
four-dimensional Ricci/gluing/topological information.

This corrects the optimistic reading of the uniform-\(K_B\) stabilization from
Step 14: the uniform model is safe, but the nonuniform enemy is not defeated by
those coarse constraints.

## 3. R2D: localized negative edge curvature is spectrally allowed

Files:
* `workspace/scripts/step15_edge_spike_spectral_fd.py`
* `workspace/scripts/step15_edge_spike_spectral_signs.py`

Data:
* `workspace/data/step15_edge_spike_spectral_fd.json`
* `workspace/data/step15_edge_spike_spectral_signs.json`

To test the statement "McKean/Cheng forbids the boundary curvature spike", I
solved a two-dimensional generalized eigenproblem on conformal rectangles
\((\Omega,e^{2\phi}(dx^2+dy^2))\):
\[
  -\Delta_E u=\lambda e^{2\phi}u,
\]
then normalized the metric to fixed area \(A_0=10>\pi j_0^2/2\).  Taking
\(\phi=f(d)\) with \(d\) the distance to the boundary and \(f'(0)=0\) keeps
straight edges geodesic and right angles right angles in this relaxed model.
For \(f=-a e^{-(d/w)^2}\), the analytic edge curvature is negative:
\[
  K_{\rm edge}=-e^{-2f(0)}f''(0)<0.
\]

The sign-controlled run found many cases with \(K_{\rm edge}<0\) and
\(\lambda_1^{\rm Dir}\le2\) after fixed-area normalization.  For example:

| amp | width | \(\lambda_1\) | analytic \(K_{\rm edge}\) |
|---:|---:|---:|---:|
| 0.25 | 0.03 | 1.9062 | -916 |
| 0.50 | 0.05 | 1.8717 | -1087 |
| 1.00 | 0.03 | 1.8974 | -16420 |
| 3.00 | 0.05 | 1.7915 | -968229 |

The compensating positive curvature lies in an adjacent subcollar, as required
by Gauss--Bonnet.  This is only a 2D relaxation and not a toric 4D metric, but
it demonstrates the exact point needed here: the Dirichlet spectral bound
\(\lambda_1\le2(1+\delta)\) and global negative-curvature comparison intuition do
not by themselves prohibit arbitrarily sharp localized negative curvature at
geodesic edges.

**Conclusion.**  A proof of the invariant volume gap cannot be a pure
base-spectral/McKean argument.  It must use the full reduced Ricci inequalities,
smooth toric closure, Chern--Weil/ALE quantization, or Biquard--Ozuch-type
obstruction information.

## 4. Page calibration: mild edge curvature, but primitive rod normalization unresolved

Files:
* `workspace/scripts/step15_page_edge_profile.py`
* `workspace/data/step15_page_edge_profile.json`

Source: `Toric-U(2)-and-LeBrun-metrics` gives an explicit Page formula in
lines 319--340.  For the \(T^2\) generated by two Euler-angle rotations, the
quotient metric has the form
\[
  g_B=S\bigl(A(r)dr^2+C(r)d\theta^2\bigr).
\]
Computing
\[
  K_B=-\frac1{\sqrt{G}}\frac1{\sqrt{E}}\frac d{dr}
  \left(\frac{d\sqrt{G}/dr}{\sqrt{E}}\right)
\]
gives a mild sign-changing profile in the normalization used:
\[
  K_B\in[-0.0952,0.0754].
\]
The samples are symmetric: negative near the two \(r\)-end rods, positive near
the middle.  Thus Page is a useful nontrivial calibration but **not** a large
negative boundary-bubble example.

The same script prints rod-flux diagnostics, but these are not source-grade
per-sphere Gauss--Bonnet checks because the U(2)/Euler-angle chart is not yet
converted to primitive toric rod coordinates.  The two \(\theta\)-edges give
\(\int(1-2K_B)q\,ds\approx1.986\), close to the primitive value 2, while the
\(r\)-edges differ substantially, likely because of lattice/period
normalization and non-diagonal rod generators.  Do not use these flux values as
proof without a primitive-coordinate conversion.

CLW was **not** computed in this step.  Hall--Murphy says the CLW metric has
cohomogeneity two and its existence proof is nonconstructive; the retrieved
source gives moment-polytope/integral data but not enough explicit orbit metric
data to compute edge \(K_B\) directly.  CLW remains a calibration target for a
future numerical/extremal-Kähler implementation.

## 5. Local edge Ricci test: rigid failure was artificial

File/data pair:
* `workspace/scripts/step15_edge_einstein_series.py`
* `workspace/data/step15_edge_einstein_series.json`

The first local test froze the base normal metric as
\(a(r)=\cosh(\sqrt A r)\), i.e. it imposed constant base curvature \(-A\) off
the rod.  It recovered only the Step-12 leading coefficients
\[
  R_2=A/2,
  \qquad p_3=-A/3-1/6,
\]
and then failed at order \(r^2\).  This is **not** evidence of a local Einstein
obstruction; it is an artifact of overconstraining the off-rod base jets.  Step
12 fixes the boundary coefficient \(a_2=A=-K_B|_{\rm edge}\), not the whole
function \(a(r)\).

The data file has been patched to say this explicitly.

## 6. Flexible formal edge series: arbitrary negative edge curvature is locally compatible

File/data pair:
* `workspace/scripts/step15_edge_einstein_series_flexible.py`
* `workspace/data/step15_edge_einstein_series_flexible.json`

Allow instead
\[
\begin{aligned}
  g&=dr^2+a(r)^2ds^2+P(r)^2d\theta^2+(R(r)Q(s))^2d\phi^2,\\
  a(r)&=1+\frac A2r^2+a_4r^4+a_6r^6+\cdots,\\
  P(r)&=r+p_3r^3+p_5r^5+\cdots,\\
  R(r)&=1+R_2r^2+R_4r^4+\cdots,\\
  Q''+(1+2A)Q&=0.
\end{aligned}
\]
Solving \(\operatorname{Ric}=g\) formally gives a recursive solution through the
checked order:
\[
\begin{aligned}
  R_2&=A/2,\qquad p_3=-(2A+1)/6,\\
  R_4&=a_4=-A(2A+1)/24,\\
  p_5&=(22A^2+10A+1)/120,\\
  R_6&=a_6=A(22A^2+10A+1)/720,\\
  p_7&=-(584A^3+312A^2+42A+1)/5040,
\end{aligned}
\]
and similarly to order 10 in the data.  All four Einstein residual components
vanish through the checked order after substitution.  A striking pattern is
\(R(r)=a(r)\) to the checked order.

**Conclusion.**  Large negative edge curvature is not locally forbidden by the
Einstein equations.  The sought obstruction cannot be a local edge maximum
principle.  It must be global: rod/polygon compatibility, an orbifold/cone
closure obstruction, ALE bubble accounting, or a Biquard--Ozuch first obstruction
when trying to smooth/resolve the limiting boundary bubble.

## 7. Exact separated edge germ and latent cone/orbifold cap

File/data pair:
* `workspace/scripts/step15_edge_germ_first_integral.py`
* `workspace/data/step15_edge_germ_first_integral.json`

The pattern \(R=a\) leads to an exact local/cohomogeneity-one edge germ:
\[
  g=dr^2+p(r)^2d\theta^2+a(r)^2g_{S^2(\kappa)},
  \qquad \kappa=1+2A,
\]
with the first smooth bolt conditions
\[
  a(0)=1,
  \quad a'(0)=0,
  \quad p(0)=0,
  \quad p'(0)=1,
  \quad a''(0)=A.
\]
The Einstein equations imply
\[
  a'=A p,
  \qquad
  2aa''+(a')^2=\kappa-a^2,
\]
and the first integral
\[
  a(a')^2=\kappa(a-1)-\frac{a^3-1}{3}.
\]
The next zero of \(p\) occurs at
\[
  a_+=\frac{-1+\sqrt{9+24A}}2,
\]
and, if the period of \(\theta\) is chosen to make the original rod smooth, the
absolute slope at this second parallel collapse is
\[
  \mu(A)=\frac{2a_++1}{a_+(a_++2)}.
\]
For \(A>0\), \(\mu(A)<1\); hence the simplest separated block closes with a cone
angle \(2\pi\mu(A)\), not smoothly, unless \(A=0\).  Numerically:

| \(A\) | rod flux \(2/(1+2A)\) | \(a_+\) | \(\mu(A)\) | \(1/\mu\) |
|---:|---:|---:|---:|---:|
| 1 | 0.6667 | 2.372 | 0.5538 | 1.81 |
| 9 | 0.1053 | 7.000 | 0.2381 | 4.20 |
| 100 | 0.00995 | 24.041 | 0.0784 | 12.76 |
| 10000 | 0.00010 | 244.454 | 0.00813 | 122.98 |

This is the most informative computation of the step.  It says that the large
negative rod-curvature bubble is locally a legitimate Einstein germ, but in the
simplest separated completion it wants to become an orbifold/conical cap.  A
smooth toric metric that uses such edge bubbles must either avoid the latent
second cone by nonseparated polygon/corner geometry or resolve/glue it.  This is
precisely the Biquard/Ozuch boundary-bubble obstruction wall, not a separate
Faber--Krahn wall.

Caution: the conical second-bolt calculation is for the separated cap only.  It
is not a proof that all boundary bubbles are conical, and it is not a closed
pinched counterexample.

## 8. Consequences for the BUILD/BREAK fork

Step 15 resolved several possible shortcuts:

1. **Exact high-corner Einstein FEM is not decisive.**  The pinched problem
   requires relaxed inequalities; exact high-corner failure would mostly
   rediscover known/nonknown exact-Einstein limitations.
2. **Uniform edge curvature is safe but not representative.**  Step 14's
   uniform-\(K_B\) stabilization gives a lower bound, but nonuniform localized
   edge curvature can formally beat it.
3. **Base spectral geometry alone is too weak.**  \(\lambda_1\le2\) and
   Gauss--Bonnet allow localized negative edge curvature in 2D relaxations.
4. **Local edge equations are also too weak.**  The flexible and exact separated
   germ show arbitrary negative edge curvature is locally Einstein-compatible.
5. **The decisive wall is boundary bubbling.**  Collapse in the invariant class
   should be modeled as many shrinking fixed spheres / boundary bubbles.  BUILD
   requires proving that smooth toric closure or ALE/orbifold desingularization
   of these boundary bubbles creates an \(O(1)\) non-scalar Ricci defect (or an
   energy/topological contradiction) under \(\delta\to0\).  BREAK requires an
   actual \(\delta\)-pinched construction that smooths/glues these bubbles while
   keeping total flux and volume tending to zero.

A useful next target is therefore not a general FEM solve of equations 1--6, but
a **boundary-bubble obstruction calculation**:

* identify the local orbifold/cone model associated to the separated germ (and
  its possible cyclic order when \(\mu=1/N\));
* compare its first obstruction with Biquard/Ozuch's Eguchi--Hanson/ALE
  obstruction, now placed on a toric rod rather than an interior orbifold point;
* determine whether resolving \(m\sim\chi\) such boundary bubbles can keep the
  Ricci defect \(o(1)\) in operator norm, or whether each bubble contributes a
  fixed non-scalar defect in the Step-1/Step-7 sense;
* relate the required bubble orders/scales to the Step-8/9 Weyl-energy tail
  \(\int |W|^2\ge16\pi^2 k-O(1)\) for \(\#_k(S^2\times S^2)\).

This is a sharper and more faithful Execute target for the invariant positive
branch.  It still would only address the invariant/collapse gap; the general
collapse-to-invariant reduction remains open after the Step-11 CZ regularity
counterexample, and the all-dimensional \(n\ge5\) part of Yau-26 remains largely
untouched.

## 9. Files produced in Step 15

| File | Content |
|---|---|
| `scripts/step15_boundary_bubble_relaxation.py` | Coarse edge-ODE/spectral/GB relaxation and cubic local jet probe |
| `data/step15_boundary_bubble_relaxation.json` | Collapse scaling \(A=m^2\), flux \(\sim1/m\); cubic-jet Ricci samples |
| `scripts/step15_edge_spike_spectral_fd.py` | Conformal-rectangle spectral probe for localized curvature collars |
| `data/step15_edge_spike_spectral_fd.json` | 2D relaxation showing localized curvature compatible with \(\lambda_1\le2\) in some regimes |
| `scripts/step15_edge_spike_spectral_signs.py` | Sign-controlled geodesic-edge curvature/eigenvalue test |
| `data/step15_edge_spike_spectral_signs.json` | Negative edge curvature with \(\lambda_1\le2\) examples |
| `scripts/step15_page_edge_profile.py` | Page quotient \(K_B\) profile from explicit U(2) formula |
| `data/step15_page_edge_profile.json` | Page \(K_B\in[-0.095,0.075]\); flux diagnostics marked nonprimitive |
| `scripts/step15_edge_einstein_series.py` | Rigid cosh-base test; patched as overconstrained failure |
| `data/step15_edge_einstein_series.json` | Rigid failure after leading coefficients; do not use as obstruction |
| `scripts/step15_edge_einstein_series_flexible.py` | Flexible formal edge Einstein series |
| `data/step15_edge_einstein_series_flexible.json` | Series coefficients through checked order, residuals vanish |
| `scripts/step15_edge_germ_first_integral.py` | Exact separated edge germ and second-bolt cone slope |
| `data/step15_edge_germ_first_integral.json` | First integral, samples, latent cone/orbifold diagnosis |

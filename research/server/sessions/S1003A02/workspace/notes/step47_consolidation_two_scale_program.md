# Step 47 — Consolidated O11 account and the two-scale program

Session S1003A02, Agent1, Express.  This note consolidates the pure-blow-up closed-manifold line after Steps 38--46.  It is meant to make the current mathematics usable in proof order and to identify the next work that can change the global judgment.  It does not change the scope of any theorem in `theorem_package_v1.md`.

Conventions below: pure blow-ups
\[
M=X\#k\overline{\mathbb{CP}}^{2},\qquad A=K_X^2,
\]
in the simple-type, all-sign-family range recorded in the theorem package, usually with \(0<k<A/3\).  Metrics are put in scalar \(-4\) Yamabe normalization when the simultaneous-field identities are used.  Write
\[
P(g)=\int|\operatorname{Ric}^{\circ}_g|^2,\qquad
\mathfrak S=8\pi^2k-P .
\]

---

## 1. Dependency spine of the closed O11 line

1. **Same-metric closed identity.**
   \[
   C_+(g)=\frac1{2\pi^2}\int|W^+|^2+\frac1{96\pi^2}\int s^2
   =A-k+\frac{P(g)}{8\pi^2}.
   \]
   Thus a blow-up tariff is a same-metric lower bound on \(C_+\), not a comparison of separate scalar and Weyl infima.  The open range \(0<k<A/3\) is invisible to LeBrun's \(C_+\ge2A/3\).

2. **Kähler tariff.**  For a fixed blow-up complex structure, Hodge index gives \(C_+\ge A\) for every Kähler metric, hence \(P\ge8\pi^2k\), strict for \(k>0\).  This is a category theorem.  A01's rotated cells show that conformally almost-Kähler/symplectic metrics can be subthreshold; the Kähler proof does not extend to them.

3. **Blindness of ordinary and paired monopole budgets.**  Ordinary sign averaging and \(\beta^2\) retain only the \(A\)-budget.  The paired field remembers an individual \(E_i\) through a relative line, but the fixed charge sits in \(h^-\), and the forced zero of the scalar cross-bilinear unwinds through the complementary component.  Hence the paired topology is already the singleton Walsh sector and supplies no additional positive self-dual payment.

4. **All-sign amplitude theorem.**  For actual solutions of all sign structures on the scalar \(-4\) representative,
   \[
   P-8\pi^2k+4L=S_{\rm field}\ge0,
   \qquad L=\mathbb E_\epsilon\int(2-\rho_\epsilon)_+ .
   \]
   Therefore \(P/(8\pi^2k)\le c\) forces
   \[
   L\ge2\pi^2(1-c)k.
   \]
   The saving band is shallow: \(0.7757889809\ldots<\rho<2\); deep depletion is unfavorable.

5. **Theorems N/W/E.**  The only free field-side channel is \(W_2\)/Nijenhuis rotation of the monopole almost-complex direction.  Keep distinct the weighted and unweighted energies
   \[
   R_\rho:=\mathbb E_\epsilon\int\rho_\epsilon^2|\nabla n_\epsilon|_{W_2}^2,
   \qquad R_0:=\mathbb E_\epsilon\int|\nabla n_\epsilon|_{W_2}^2.
   \]
   Theorem N gives \(8\pi^2k-P\le R_\rho/2\), hence
   \[
   R_\rho\ge16\pi^2(1-c)k
   \]
   for any sequence with \(P/(8\pi^2k)\le c\).  Since \(R_\rho\le4R_0\), it also gives \(P\ge8\pi^2k-2R_0\).  The equivalent Weyl form says that this is exactly a Rayleigh/Weyl-departure channel.  The affine pointwise scheme stops at LeBrun's \(2/3\); no further affine combination of the existing SW identities gives a \(k\)-dependent open-range lower bound.

6. **AK\(\Gamma\), Lemma T, and why the AK gauge does not solve the metric problem.**  The almost-Kähler profile
   \[
   C_+\ge\frac{\ell^2}{128\pi^2V}(3\theta^2-2\theta+1)
   \]
   explains LeBrun's threshold and the formal common mode.  Lemma T excludes a nowhere-zero self-dual harmonic form with null exceptional periods.  But A01's rotated certified cells have nonzero tiny exceptional periods and are conformally almost-Kähler at subthreshold cost.  Step 46 shows the almost-Kähler representative then pays an unbounded scalar-variance term as the period tends to zero; AK-gauge lower bounds do not transfer to \(P\) of the original metric without conformal-factor control.

7. **Perturbative complex-hyperbolic theorem \(A_C\).**  Lemma M and the uniformly local nonlinear slice prove that on closed ball quotients globally in a cover-uniform \(C^{2,\alpha}_b\) neighbourhood of the complex-hyperbolic metric, the canonical monopole branch obeys
   \[
   R_{\rm can}\le C P .
   \]
   This excludes diffuse canonical-branch rotation on globally close closed quotients.  It does not yet give a localized statement on the CH bulk of a blow-up, select the branch of every solution there, or include collars/cores.

8. **Theorem K.**  Under the same all-metric sign-family hypotheses,
   \[
   8\pi^2k-P(g)\le\frac{4\sqrt6}{3}\int\operatorname{dist}(W^+_{\hat g},\mathcal K)
   \]
   on the scalar \(-4\) Yamabe representative, where \(\mathcal K\) is the scalar \(-4\) Kähler Weyl orbit.  Thus
   \[
   P(g)\le8\pi^2ck\quad\Longrightarrow\quad
   \int\operatorname{dist}(W^+_{\hat g},\mathcal K)\ge\sqrt6\pi^2(1-c)k.
   \]
   The constant is sharp at first order.  There is no pointwise quadratic replacement: at canonical amplitude the first variation is linear.

9. **Certified and rotated upper objects.**  The authoritative diagonal isolated cell has the interval certificate
   \[
   P/(8\pi^2)\in[0.995662732753254329\ldots,0.995662732771114200\ldots].
   \]
   A01's rotation argument is a separate rigorous continuity construction: a monotone frame rotation has \(p'(0)=-\pi\int\chi'\Phi>0\), the invariant self-dual form is nowhere zero for \(p\ne0\), and strict subthreshold cost persists for sufficiently small rotation.  Thus pure blow-ups admit subthreshold metrics conformal to smooth almost-Kähler metrics with tiny nonzero exceptional periods.  The rotated cost is not enclosed by the diagonal interval certificate.  The correct bolt model is \(f_p^2=a^2p^2+\kappa^2r^2+\cdots\); the almost-Kähler representative has scalar variance \(\asymp p^{-2}\), not the superseded \(p^{-1}\) law.  Any lower theorem must accommodate both objects.

---

## 2. Governing two-scale conjecture supported by the identities

The combined identities now point to a two-scale picture rather than a universal per-class tariff.

**Diffuse quadratic-transport conjecture.**  For a specified pure-blow-up family (for example a cover family with constants uniform in the cover degree and in \(0<k/A<1/3\)), the diffuse channel should satisfy a lower scale
\[
\inf_g P(g)\ge c_0\frac{k^2}{A}
\]
with a family-uniform positive constant coming from a noncircular quadratic transport theorem.  The constant and exact hypotheses are unknown.  Whether this is the unrestricted sharp scale still depends on nonperturbative cores/collars and on a matching upper construction.  For one fixed manifold a manifold-dependent \(c_0\) would largely repackage positivity and is not the intended statement.

The structural reason is exact.  Theorem K says saving is at most linear in the \(L^1\) Weyl departure from the Kähler orbit.  The signed identities and closed identity make the natural diffuse cost quadratic in that departure and in volume/scalar excess.  The formal common mode spreads departure of size \(k/A\) over volume \(\asymp A\), producing total saving \(\asymp k\) while paying \(\asymp k^2/A\).  The Cotton route of Step 43 gives precisely this possible law:
\[
P\ge\frac{R_0^2}{\Lambda A},\qquad
P\ge8\pi^2k-2R_0
\quad\Longrightarrow\quad
P\ge\left(\sqrt{\Lambda A+8\pi^2k}-\sqrt{\Lambda A}\right)^2.
\]
If the transport theorem is instead written for \(R_\rho\), both the linear coefficient and \(\Lambda\) must be renormalized; the two energies must not be identified.
A_C proves the linear quotient only in the perturbative KE canonical-branch regime; it does not settle the intermediate, noncanonical or collar/core regimes.

This is not a weakening of the research goal.  A positive fixed-topology bound in \(0<k<A/3\) would already exclude Einstein metrics in a range not reached by LeBrun's lower bound and would identify the correct mechanism for degeneration.  What remains is to prove the quadratic transport estimate beyond the perturbative regime, or to construct closed metrics realizing the quadratic scale.

---

## 3. Cheap consistency calculation: Theorem K on the formal common mode

Let \(h=k/A\), \(r=2-h\).  In the Step-40 formal common mode,
\[
\frac{P}{8\pi^2}=A\left(h-\beta(r)\right),\qquad
\beta(r)=\frac{16}{r}-5-\frac{12}{r^2},
\]
and exact algebra gives
\[
\beta(2-h)=\frac{h(4-5h)}{(2-h)^2},\qquad
h-\beta(2-h)=\frac{h^2(1+h)}{(2-h)^2}.
\]
Hence
\[
\frac{P}{8\pi^2k}=c(h)=\frac{h(1+h)}{(2-h)^2},
\qquad
1-c(h)=\frac{4-5h}{(2-h)^2}.
\]
Using the common mode's axial ansatz \(M=\operatorname{diag}(x,-x/2,-x/2)\), not merely its Rayleigh component, the self-dual Weyl tensor has eigenvalues
\[
\left(-\frac23+h,\ \frac13-\frac h2,\ \frac13-\frac h2\right)
\]
in the same direction as the Kähler orbit, so the pointwise distance to \(\mathcal K\) is
\[
\sqrt{h^2+2(h/2)^2}=\sqrt{\frac32}\,h.
\]
The formal identity \(r^2V=8\pi^2A\) gives
\[
D_{\mathcal K}:=\int\operatorname{dist}(W^+,\mathcal K)
=\sqrt{\frac32}h\frac{8\pi^2A}{(2-h)^2}
=\frac{4\sqrt6\pi^2k}{(2-h)^2}.
\]
The Theorem-K lower threshold for this value of \(c(h)\) is
\[
D_{\min}=\sqrt6\pi^2(1-c(h))k
=\frac{\sqrt6\pi^2(4-5h)k}{(2-h)^2}.
\]
Therefore
\[
\frac{D_{\mathcal K}}{D_{\min}}=\frac4{4-5h}
=1+\frac54h+O(h^2).
\]
The formal common mode nearly saturates the pointwise algebraic inequality underlying Theorem K in the tower limit \(h\to0\).  At the edge \(h=1/3\) the ratio is \(12/7\).  More exactly,
\[
\frac{4\sqrt6}{3}D_{\mathcal K}-(8\pi^2k-P)=\frac{5}{1+h}P,
\]
so the Theorem-K slack is itself of order \(k^2/A\).  This is an algebraic consistency test, not an admissible closed family: Lemma T excludes the exact common mode.  Near-saturation of the linear \(L^1\) inequality does not prove the quadratic lower law.

---

## 4. Quantitative construction targets for A01 and for our lower-bound work

Any closed family in the pure-blow-up range with \(P/(8\pi^2k)\le c<1\) must exhibit all of the following on the scalar \(-4\) Yamabe representative and actual sign-family fields:

\[
\int\operatorname{dist}(W^+,\mathcal K)\ge\sqrt6\pi^2(1-c)k,
\]
\[
R_\rho\ge16\pi^2(1-c)k,
\]
\[
L=\mathbb E\int(2-\rho)_+\ge2\pi^2(1-c)k,
\]
and its positive saving must lie in the shallow amplitude band.  The closed form or symplectic representative must carry exceptional classes through tiny nonzero areas, zero sets, collars/cores, or noncanonical field behaviour; exact null periods of a nowhere-zero form are excluded by Lemma T.  If an almost-Kähler representative is used, its scalar variance near tiny exceptional periods must be measured, because Step 46 shows that the AK gauge can pay an unbounded amount that is absent from the original metric.

For a potential \(c\to0\) closed upper family these become, to leading order,
\[
\int\operatorname{dist}(W^+,\mathcal K)\gtrsim\sqrt6\pi^2k,
\qquad
R_\rho\gtrsim16\pi^2k,
\qquad
L\gtrsim2\pi^2k.
\]
A_C adds only that such rotation cannot be the nearby canonical branch on a globally CH-close closed quotient unless \(P\) is also order \(k\).  The corresponding conclusion for the CH bulk of a blow-up awaits localization and branch selection; a small-per-class construction may use noncanonical depleted fields, nonperturbative bulk regions, or collars/cores/zero tubes.  Proposition \(\Pi\) prices positive \(s^*\) pockets per unit volume but allows shrinking pockets; nonperturbative aligned pockets remain a legitimate construction target.

These measurements are separate from balanced handle families and density-free O10.  The balanced construction already has its own sub-four upper law and does not decide the pure-blow-up quadratic scale.  O10 concerns actual field concentration and remains an independent endpoint.

---

## 5. Route judgment after consolidation

The highest-return next theorem is not a revived per-class tariff.  It is a localized **Riemannian** complex-hyperbolic coercivity theorem with an explicit collar flux, after which the quadratic field law can be attacked on the remaining core/collar channel.

Promising entry points, in order of present value:

1. **Localized CH Einstein coercivity, without branch selection.**  Let \(\Omega\Subset\Omega_1\) lie in a scalar-normalized metric uniformly \(C^{2,\alpha}\)-close to CH on \(\Omega_1\).  In local DeTurck/Bianchi gauge, seek
   \[
   \int_\Omega\bigl(|W^-|^2+|W^+-W^+_{CH}|^2\bigr)+\mathcal V_\Omega
   \le C\left(\int_{\Omega_1}|\operatorname{Ric}^\circ|^2+\mathcal B(\Omega_1\setminus\Omega)\right),
   \]
   where \(\mathcal V_\Omega\) is the coercive scalar-normalized volume departure after its signed boundary flux is separated and \(\mathcal B\) is an explicit gauge-invariant collar/outer-layer term.  No sign for raw relative volume is assumed.  This localizes the proved Riemannian half of A_C, retains the anti-self-dual ledger, and would force order-\(k\) curvature into nonperturbative cores/collars before any marked-cell lower bound is used.

2. **Yamabe-gauge quadratic transport on a shallow band.**  Starting from Proposition 43.C, prove in a restricted setting that the adjoint terms \(\mathcal C^*U\), \(\delta^*U\) are controlled by \(A^{1/2}\) times a noncircular quantity, with explicit shallow-band cutoffs and \(E=W^+-W_0\), \(\nabla a\) retained.  The first target should be a conditional theorem with a small explicit list of error terms, then tests on A01's rotated cells.

3. **Construction side with A01.**  Ask for measurements on the scalar \(-4\) Yamabe representative, not only on the conformal AK representative: \(\int\operatorname{dist}(W^+,\mathcal K)\), \(P\), \(\int|W^-|^2\), and, if actual or model fields are available, depletion and weighted/unweighted \(W_2\) energies.  Scalar variance belongs on the conformal AK representative (the Yamabe scalar is constant); the exact conformal difference \(P(g)-P(\hat g)=[S(g)-S(\hat g)]/12\) should be retained.  The formal common-mode values above give the reference scaling.

4. **Density-free O10** remains important but is less connected to the newly consolidated O11 anatomy.  Return to it when the next action can use the current field/transport structure rather than repeating early concentration analysis.

A critical review of this consolidation is valuable before a long proof push, because several statements now interact: all-metric sign quantifiers, Yamabe normalization, A_C branch selection, A01's conformally-AK upper family, and the conditional Cotton law.  After that review, Execute should attack item 1 or 2 with the exact error terms visible.

---

## 6. New-source transfer after reading the completed §§10–12

Actual material read this Step: the collection map and `connections.md` §§2–12; the original De Giorgi equations (5.6)–(5.8) and Lemma 9.3/(9.10); the original Coulomb minimizer-entry and global dual identity; the exact-two-form inverse in hypersymplectic Lemma 10.4; and the scalar–simplicial-volume theorem statement.  The new §10 inputs were checked at the level of their stated hypotheses.

### 6.1 What changes the next O11 proof object

The De Giorgi identity is valuable because it does not merely state Hessian nonnegativity.  The same actual amplitude obeys an equation whose stability test gives
\[
0\le Q(q\eta)=\int q^2|d\eta|^2-\int q^3D\eta^2.
\]
The negative defect-mass term is what makes localization coercive.  For SW, the naive test \((a,\varphi)=(0,\eta\Phi)\) gives only
\[
Q^{SW}(0,\eta\Phi)=\int |\Phi|^2|d\eta|^2+4\eta^2|q(\Phi)|^2,
\]
so it cannot price Nijenhuis/alignment defect.  A useful field theorem must instead construct a coupled connection–spinor variation and preserve the common variance term when local branches are combined.  This is a precise target, not an imported result.

The Coulomb argument changes the global architecture: geometric separation is proved only for finite-volume minimizers, then an exact globally compatible comparison transfers the estimate to every competitor.  The Einstein problem needs the analogue
\[
\text{infimum-preserving approximation}\to\text{entry for minimizing objects}
\to\text{global comparison}\to\text{all metrics}.
\]
It is therefore invalid to assume arbitrary metrics already have exact-CH cells.  The first plausible bridge is a localized **Riemannian** CH coercivity theorem: in Bianchi/DeTurck gauge on \(\Omega\Subset\Omega_1\), control the departure of both Weyl blocks from CH by local \(P\) plus an explicit collar term.  This uses the proved Riemannian half of \(A_C\), avoids immediate monopole branch selection, and determines whether order-\(k\) curvature is forced into cores/collars.

The family-348 representation calculation reinforces that route only at the design level: use Bianchi constraints before estimating the curvature action and retain Cotton sources.  Its final positivity still uses \(\sec\ge0\) and retains \(W^-\); neither hypothesis is available here.  Accordingly, the localized target must keep \(W^-\) and boundary/Cotton terms rather than claiming their cancellation.

The exact-form identity
\[
\|h\|_2^2=2\|h^+\|_2^2,
\qquad h=2dd^*G\varphi,
\]
is a useful auxiliary for period-preserving collar corrections because it avoids a one-form spectral gap.  It does not control \(E=W^+-W_0\), remove the harmonic exceptional charge, or preserve the coupled Dirac equation, so it is not the missing quadratic law.

Family 351 supplies conditional controlled-collar extension with quadratic Ricci cost, but the collars must first be obtained from the original competitors and the total added cost must be \(o(Q)\).  Its tree functional is not \(P\); an \(O(M^2)\) reduction error does not preserve a leading term of the same order.  The new §10 rigidity/limit-space results need hypotheses absent from small \(P\): strict negative sectional curvature, a sectional upper bound, actual dissipation, or RCD/noncollapse.  They do not alter the main route.

### 6.2 Two additional proved consequences to retain

Under the full conformal-class actual supply in O10, resetting the finite-density budget to the conformally invariant actual square \(A_j=p_j\) proves that any sequence with \(\beta_j\to\infty\), \(\kappa_{\beta_j}\to0\) must satisfy
\[
\frac{\chi(M_j)}{p_j}\to\infty,
\qquad
\frac{p_j}{V_j}\to\frac{2}{9\pi^2},
\qquad
\frac{W^-_j}{V_j}\to\infty.
\]
Thus density-free O10 is an unbounded **actual-density** problem; fixed-energy compactness is not the endpoint.  The positive-current source suggests that concentrated energy may survive as a closed geometric current, but an oriented current and uniform directional/transverse moments must be constructed from the actual field equations.

Assuming the external scalar–simplicial-volume theorem, if
\[
H=a_4\|M\|>0,
\qquad b=\frac{96\pi^2(2\chi-3|\tau|)_+}{H}<1,
\]
then Chern–Weil gives
\[
\mathcal E\ge\mathcal J\ge\frac{4(1-b)}{4-b}.
\]
This expands the topological supply for normalized gaps, but in the original balanced small-\(h\) window one has \(b\ge1+h\), so it does not determine that coefficient.

Finally, the completed §11 gives a direct application of any true positive \(P\)-gap.  If \(Y(M)<0\), \(\inf_gP(g)>0\), and family-351's finite-time bounded-scalar extension theorem is used, every maximal volume-normalized Ricci flow has unbounded scalar curvature on its maximal interval.  The immortal branch uses
\[
\bar s'=\frac{2P}{V}-\frac12\fint(s-\bar s)^2
\]
and the negative-Yamabe minimum estimate.  This is a rigorous downstream consequence of a future fixed-topology gap, not a substitute for proving it.  A lower bound for \(P+D_2\) suffices only when \(D_2\) is the scalar variance (both terms then become time-integrable); an unrelated field defect does not.

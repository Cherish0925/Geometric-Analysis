# Step 40 — Harmonic-class compatibility, period stiffness, and symplectic realization of the sub-four cells

Conventions: computational profile scale \(\operatorname{Ric}_{CH}=-6g\); \(J=J_6/(8\pi^2)\);
SU(2)-invariant cells \(g=dt^2+H_{ij}(t)\sigma_i\sigma_j\), \(d\sigma_i=2\sigma_j\wedge\sigma_k\) (cyclic),
orientation \(dt\wedge\sigma_1\wedge\sigma_2\wedge\sigma_3>0\), \(\int_{S^3}\sigma_1\sigma_2\sigma_3=2\pi^2\),
\(\int_E\sigma_2\wedge\sigma_3=\pi\).  Peer slot order: slot 1 = the circle collapsing at the perpendicular
bolt (\(a_h\) in Step-39 notation), slot 2 = transverse (\(a_g\)), slot 3 = CH Kähler fibre (\(a_f\)).
\(\Omega=\tfrac12 d(\sum\phi_i\sigma_i)\) is the Step-39 canonical form, \(\phi=(0,0,\phi_f)\) for diagonal cells,
equal to the host Kähler form \(\tfrac12d(x\sigma_f)\) on the exact collar.  Hence
\[ t:=\int_E\Omega=\pi\,\phi_1(0). \]
Script `workspace/scripts/step40_harmonic_class_period.py`; data `workspace/data/step40/harmonic_class_period.json`
(Hessian-based stiffness) and `workspace/data/step40/period_functional_certified.json` (certified profile).
Independent verification: `trace/ttcs/results/step40_ttcs01_verifier1_integration.md`; it found a factor-two
period normalization error in the first version of this note (period of \(2\Omega\) instead of \(\Omega\)),
corrected below.

## 1. Conformal invariance of pair classes

In dimension four \(\star\) on two-forms is conformally invariant.  If \(\Omega\) is closed and \(g\)-self-dual,
it is closed, \(u^2g\)-self-dual and \(u^2g\)-harmonic, with the same class, periods, zero set and (non)vanishing.
For a class \(\mathcal C\) of exact-CH-ended pairs \((g,\Omega)\) defined only by such conformally invariant
conditions on \(\Omega\) (zero exceptional period, prescribed period \(t\), prescribed zero topology,
nowhere-vanishing), the Step-21–23 scalar normalization \(-6\Delta u+su+24u^3=0\), \(u\to1\), and the cutoff
recovery \(u_R^2g\) keep the pair in \(\mathcal C\).  Since \(J_6\ge P\) and \(J_6(u^2g)=P(u^2g)\le P(g)\) up to
vanishing recovery loss,
\[ \inf_{\mathcal C}P=\inf_{\mathcal C}J_6 \]
after the infimum over outer radius.  This does not extend to conditions that involve \(g\) explicitly
(\(|\Omega|_g^2=2\), almost-Kähler normalization, amplitude bounds), because \(|\Omega|_{u^2g}=u^{-2}|\Omega|_g\);
and before recovery \(\Omega\) is not the Kähler form of \(u^2g\) (that is \(u^2\Omega\)).  For \(m\) cores, \(o(m)\)
total recovery loss needs room for disjoint recovery radii.  Equality of infima is not attainment, and the
\(J_6\) Hessian below need not equal the period-resolved \(P\) Hessian.

## 2. The compatibility condition and where it lives

With fixed class on the closed glued manifold, \(\dot\Omega=da\), \((da)^-=\tfrac12\dot\star_h\Omega\), and
solvability is
\[ \int\langle h^\circ,\Omega\circ\beta\rangle\,dV=0\qquad\forall\beta\in\mathcal H^-_g \tag{2.1}\]
(up to a convention constant), the derivative of the period map \(g\mapsto\mathcal H^+_g\).

**Proposition 2.1.** On the principal-orbit region an SU(2)-invariant closed 2-form is
\(d(\sum\phi_i\sigma_i)\), self-dual iff \(\phi'=\frac{2}{\sqrt{\det H}}H\phi\), anti-self-dual iff
\(\psi'=-\frac2{\sqrt{\det H}}H\psi\).  At a smooth perpendicular bolt (\(H=\operatorname{diag}(t^2,b^2,b^2)+\dots\)
with the standard smooth jets) the SD indicial exponents are \((0,2,2)\): every solution is smooth,
\(\phi_1=c_1+O(t^2)\) is free and \(\int_Ed(\phi_1\sigma_1)=2\pi c_1\), \(\phi_{2,3}=O(t^2)\).  The ASD exponents are
\((0,-2,-2)\): the only bolt-regular invariant ASD form is \(\beta_E=d(\psi_-\sigma_1)\), \(\psi_-=1/\psi_+\),
\(\psi_+=\exp\int2H_{11}/\sqrt{\det H}\).  (When \(c_1\ne0\) the potential \(\phi_1\sigma_1\) is connection-like at
the bolt; the two-form is smooth.)

Consequences.
1. *Diagonal sector, exact and nonlinear.* For every diagonal cell \(\phi=(0,0,\phi_f)\) solves the system with the
   collar value; the period is zero.  All diagonal variations — profile, bolt area, conformal, and the Step-19
   antisymmetric exterior mass mode — preserve the pullback class and its zero period.
2. *Averaging.* For invariant \(h\) supported in an invariant cell \(U\), averaging \(\beta|_U\) gives
   \(c(\beta)\beta_E\), \(c(\beta)\propto\int_E\beta\); (2.1) collapses to one condition per cell,
   \(\int_U\langle h^\circ,\Omega\circ\beta_E\rangle=0\), and distinct cells give independent conditions.  For such a
   variation with unchanged collar the inward SD solution equals the host form outside \(U\): host periods, hence
   the period angle \(\eta\), are unchanged exactly; only the exceptional component (the AKΓ term \(e\)) moves.
3. *Nontrivial isotypes.* A \(j\ge1\) variation pairs to zero with the invariant local mode
   \(\Omega\circ\beta_E\).  Globally, however, the harmonic ASD representative of the exceptional direction need not be
   SU(2)-invariant on the cell, and its non-invariant parts can pair with \(j\ge1\) variations.  So the separation
   "invariant = exceptional, \(j\ge1\) = host" holds for the local invariant model and is not proved globally.
4. *Character localization.* The Klein group of sign changes fixes diagonal cells and acts on
   \(h_{12},h_{13},h_{23}\) by three distinct characters; diagonal modes are trivial.  Linearizing with
   \(\delta\phi_1(t_c)=0\),
   \[ \delta\phi_1(0)=-\psi_+(0)\int_0^{t_c}\frac{2\,\delta H_{13}\,\phi_f}{\sqrt{\det H}\,\psi_+}dt, \tag{2.3}\]
   while \(\delta H_{12}\) never enters and \(\delta H_{23}\) produces a regular \(\delta\phi_2=O(t^2)\).  The local
   exceptional-period differential lives entirely in the \(h_{13}\) block — rotation of the collapsing circle toward the
   CH fibre, i.e. from the perpendicular toward the aligned orientation.  The Step-21 \(U(1)\) phase mode lies in
   \(h_{12}\) and is class-preserving; the mass-null direction has zero Hessian coupling to \(h_{13}\).  Moreover
   \(J\) is even in each off-diagonal channel at a diagonal cell, so \(J=J_*+O(\delta^2)\) along \(h_{13}\) **without any
   stationarity assumption**.
5. *Rotation formula.* For \(\delta H_{13}=\theta(H_{11}-H_{33})\), \(\theta(t_c)=0\), with
   \(\Phi=\psi_+(0)\phi_f/\psi_+\): \(\delta\phi_1(0)=-\int_0^{t_c}\theta'\Phi\,dt\) and, for constant rotation,
   \(\int2(H_{11}-H_{33})\phi_f/(\sqrt{\det H}\psi_+)dt=-X\) exactly.  \(\Phi\) vanishes at the bolt and grows like the
   Kähler potential outward.  (Constant rotations are gauge only if metric, form, collar frame and gluing are rotated
   together.)

## 3. Nowhere-vanishing forms and the symplectic realization theorem

**Lemma 3.1.** A nonzero bolt-regular invariant SD solution never vanishes on a principal orbit (the form vanishes
there iff \(\phi=\phi'=0\), and the ODE then forces \(\phi\equiv0\)).  At the bolt its value is
\(2c_1b^{-2}(e^{01}+e^{23})\) plus terms vanishing with \(t\).  Hence the canonical SD form of an invariant cell is
nowhere zero iff its exceptional period is nonzero; for \(t=0\) its zero set is exactly the bolt (Step 39).

**Proposition 3.2 (symplectic realization of the certified saving).** Let \(g_*\) be the certified
\(x_0=.03,X=128\) cell, \(J(g_*)\le0.995670030355131\).  Let
\(g_\psi=R(\psi\chi)\,g_*\,R(\psi\chi)^T\), \(R\) the rotation in the (bolt, fibre) plane,
\(\chi=(1-u)^3(1+3u+6u^2)\) (\(\chi=1+O(u^3)\) at the bolt, third-order contact with \(0\) at the collar).  Then for all
sufficiently small \(\psi\ne0\):
(a) \(g_\psi\) is a smooth exact-CH-collar blow-up cell (near the bolt it is a constant right translation of
\(g_*\) up to \(O(t^6)\)) with \(J(g_\psi)<1\), and \(J(g_\psi)=J(g_*)+O(\psi^2)\) by Klein evenness;
(b) its canonical SD harmonic form \(\Omega_\psi\), equal to the host Kähler form on the collar, has exceptional
period \(t(\psi)=\psi\,t'(0)+O(\psi^2)\) with
\[ t'(0)=\pi\psi_+(0)\int\chi\,(H_{33}-H_{11})\,\frac{2\phi_f}{\sqrt{\det H}\,\psi_+}dt=0.6960. \]
The integrand is pointwise nonnegative because \(H_{33}-H_{11}\in[0.03,16384]\) on the whole profile
(`period_functional_certified.json`: density range \([0,0.458]\)), so \(t'(0)>0\) does not depend on cancellation;
(c) \(\Omega_\psi\) is nowhere zero (Lemma 3.1).  Choosing the sign of \(\psi\), \(t\) has either sign.

Gluing \(k\) such cells into the marked balls of a compact ball quotient or ramified Kähler–Einstein host gives,
for **pure blow-ups** \(X\#k\overline{\mathbb{CP}}^2\), closed metrics carrying a closed **nowhere-vanishing self-dual
harmonic form**, i.e. a symplectic form whose conformal metric \(\widehat g=(|\Omega|_g/\sqrt2)\,g\) is smooth
almost-Kähler, with small exceptional areas of the chosen sign and per-cell cost arbitrarily close to the certified
value.  The pure-blow-up upper law \(\limsup\alpha/h\le4(1-\eta_{\rm cert})\) (\(\theta=1\)) therefore holds already
within metrics that are conformally almost-Kähler with a symplectic form in the class
\(\tfrac16K_X^{\rm pull}+\sum_i(t_i/\pi)\,\mathrm{PD}\text{-dual of }E_i\) (profile scale, up to the period convention).
Families with handles are excluded from this statement: by Kotschick's connected-sum theorem (to be source-checked
before citation) \(X\#(S^1\times S^3)\) admits no symplectic structure, so there the cell form is only a local
object.

Status: (a) uses the certified enclosure, smoothness of the rotated bolt (as in Step 21), and continuity of \(J\) in
the metric two-jet; (b) uses Proposition 2.1 and a floating quadrature of a strictly positive integrand with a large
margin; it is upgradeable to Arb with the existing certified-profile evaluator.  The construction makes no claim
about the size of the admissible \(\psi\)-interval.

What it means.  The Taubes period theorem excludes zero-period nowhere-zero forms; the subthreshold saving does
not need them.  It is realized by metrics conformal to almost-Kähler metrics with genuine symplectic forms of small
positive exceptional area.  Therefore no lower-bound argument whose only extra input is "the metric carries a
self-dual symplectic form / is conformally almost-Kähler" can restore the unit per-blow-up tariff
(coefficient four) on pure blow-ups of these hosts; any such
argument must use quantities that degenerate as \(t\to0\) (the conformal factor \(|\Omega_t|/\sqrt2\) is \(O(t)\) at the
bolt, and Step 39 showed \(\int\widehat s^2\) of the singular limit diverges), host-period drift, interface flux or
genuinely global field constraints.  This is consistent with A02's unit Kähler tariff: Kähler cells pay linearly in
area, the conformally almost-Kähler non-Kähler cell does not.

## 4. Period stiffness on the stationary \(x_0=.038\) cells

With the Step-21 \(h_{13}\) Hessian blocks (exact bolt rotation \(+\) \(n\) Chebyshev modes; computed with the rotation
\(\psi(\chi-1)\), isometric to \(\psi\chi\); the mixed-term difference is an order-\(\psi c\) diagonal variation, harmless
at the numerically stationary cell), and \(L=\pi\,\partial\phi_1(0)/\partial c\):
\[ \Delta J_{\rm Ritz}=\frac{t^2}{2L^TH^{-1}L}=:\tfrac12K_\Omega t^2. \]
\[
\begin{array}{c|cccc}
 & X=128,n=16 & X=512,n=10 & n=16 & n=24\\ \hline
K_\Omega & 32.354 & 32.378 & 32.345 & 32.344\\
\text{Schur (fixed rotation, bumps relaxed)} & 0.60456 & 0.60598 & 0.60528 & 0.60524
\end{array}
\]
So \(\Delta J\simeq16.17\,t^2\) (\(\operatorname{Ric}=-g\) scale, \(t_g=6t\): \(\Delta J\simeq0.449\,t_g^2\)), converged in
basis and collar length; positive on the fixed-period hyperplane.  Checks: gauge identity to \(1.2\times10^{-10}\);
nonlinear integration of the SD system agrees with the linear functional to \(10^{-8}\) (amplitude \(10^{-4}\)).
Comparison of truncated expansions: Kähler aligned \(J=1+6t/\pi+\dots\) crosses \(J_0+16.17t^2\) near \(t\approx0.12\);
the quadratic truncation stays below 1 for \(t\lesssim0.017\) (\(t_g\lesssim0.10\)) — indicative only, higher orders
uncontrolled.  This is a floating, fixed-collar, finite-dimensional invariant Ritz upper value; \(t=0\) is a local
minimum in the block, so positive periods do not lower the cost — they are merely cheap.

## 5. Open directions sharpened by this step

* The \(j=1\) host-period stiffness: global, couples each cell to \(b^-\) host ASD classes; it is where many cores can
  interact through the period map, and where (2.1) is a genuine \(O(A)\)-dimensional constraint.
* Lower bounds for the conformally almost-Kähler symplectic family of §3 in terms of the original metric \(g\): which
  term of the AK identities (Step 28, AKΓ, Cotton transport) blows up as \(t\to0\), and whether the per-class tariff
  can be expressed through \(t\)-independent quantities of \(g\).
* Period-resolved nonlinear cost \(j(t)\) beyond second order and outside SU(2) symmetry.

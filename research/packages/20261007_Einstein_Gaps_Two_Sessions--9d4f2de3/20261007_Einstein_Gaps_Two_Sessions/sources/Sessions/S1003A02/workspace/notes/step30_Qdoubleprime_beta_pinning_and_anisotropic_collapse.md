# Step 30 — Q″, fibre/base pinning, and anisotropic collapsed entries

Conventions are those of Steps 27–29.  For a diagonal Bianchi–IX annulus,

\[
\widehat P(C)=\Delta\mathfrak b_+
 +\frac1{2\pi^2}\int_C|W^+|^2
 +\frac1{96\pi^2}\int_Cs^2. \tag{1}
\]

The charge orientation and normalization are the independently checked ones: a smooth round centre has \(\mathfrak b_+=2\), an \(O(-1)\) bolt has \(\mathfrak b_+=1\), a regular Berger end has \(\mathfrak b_+=-2\), and a CH orbit of radius \(t\) has \(\mathfrak b_+=2-9\sinh^4t\).

## 1. Lemma Q″: diagonal bubble-end pricing

**Lemma Q″.** Let \(C_j=[T_j,S_j]\times S^3\) be diagonal annuli whose inner orbits converge in normalized chiral first-jet data to a bubble end with finite plus charge \(b_{\mathrm{end}}\). Suppose an outer orbit converges in the same data to a round Euclidean sphere, so its charge tends to \(2\). Then
\[
\liminf_j\widehat P(C_j)\ge 2-b_{\mathrm{end}}. \tag{2}
\]
More generally, between two convergent normalized first-jet limits,
\[
\liminf_j\widehat P(C_j)
 \ge b_+^{\mathrm{out}}-b_+^{\mathrm{in}}. \tag{3}
\]

**Proof.** Integrate (1) and discard the two nonnegative integrals. At a collapsed end, the required convergence is precisely convergence of the normalized chiral connection coefficients \(u_i=p_i-\gamma_i\), or equivalent data that make \(\mathfrak b_+\) converge; convergence of the raw state alone is insufficient. \(\square\)

Consequences:

* Burns joins the \(O(-1)\) bolt charge \(1\) to the round charge \(2\), hence pays at least \(1\). It is scalar-flat ASD in this orientation and attains equality.
* The Ricci-flat Taub-bolt path carries the same bolt freely to the Berger/ALF charge \(-2\). Any subsequent controlled decollapse to a round orbit pays at least \(2-(-2)=4\). The Step-29 scale-free minimizers approach equality through an ASD scalar-flat decollapse.
* This is the diagonal version of a general bubble-end principle: the topology price is a relative characteristic transgression at the end, rather than a universal cost assigned to the compact core alone.

The closed-manifold form suggested by (2) is the following precise research target. On an F-structure neck surrounding a collapsed bubble, define the adiabatic Euler/signature boundary limit from the Levi-Civita Chern–Simons forms. If this limit exists and the neck can be compared to a round link, then its topology cost should be the round characteristic charge minus the adiabatic end charge, with nonnegative bulk curvature terms. Q″ proves this in diagonal symmetry. Establishing existence and functoriality of that adiabatic limit beyond symmetry would supply exactly the collapse accounting that pointwise-Ricci regularity presently does not provide.

### Finite-charge anisotropic Berger limit

A useful normalized first-jet class can be described exactly. In the regular scale-free coordinates
\[
x=\log(a_f/a_g),\quad z=(a_h/a_g)^{1/3},\quad
p=rh',\quad\chi=r(x'),\quad\eta=rq',
\]
consider the collapsed first-jet family
\[
x=Xz^3+o(z^3),\quad p=Pz+o(z),\quad
\chi=Cz+o(z),\quad\eta=Nz+o(z). \tag{4}
\]
The exact symbolic calculation `scripts/collapse_chiral_charge_limit.py` gives
\[
\mathfrak b_+^{\mathrm{end}}=-2-(C+4X)^2. \tag{5}
\]
Therefore shear cannot raise this finite-charge end above \(-2\); it either preserves the Berger price, when \(C+4X=0\), or increases the round-decoupling price to
\[
2-\mathfrak b_+^{\mathrm{end}}=4+(C+4X)^2. \tag{6}
\]
The opposite charge is
\[
\mathfrak b_-^{\mathrm{end}}=2+(C-4X)^2. \tag{7}
\]
Thus \(P\) and \(N\) cancel from both limits. Equation (5) rigorously controls a finite-charge anisotropic entrance to the high-shear branch. It does not by itself assert bounded ambient curvature. At fixed base scale, bounded orbit curvature requires the stronger \(x=O(z^6)\), and bounded mixed curvature forces stronger shear decay such as \(\chi=O(z^4)\), together with radial second-derivative control. In that genuinely bounded-geometry regime \(X,C\to0\) and \(\mathfrak b_+\to-2\). Fixed \(O(1)\) values of \(x,\chi,\eta\) as \(z\to0\) are outside even the finite-charge class.

## 2. A fibre/base analogue of CR pinning

Use compact ACH variables for fibre \(f\):
\[
\kappa=\frac{a_f}{a_ga_h},\qquad
\zeta=\frac1{a_ga_h},\qquad q=\log\frac{a_g}{a_h},
\]
and put
\[
v=y_f-\frac{y_g+y_h}{2}=\beta',\qquad
\widetilde B=
\log\frac{\kappa}{\sqrt{1+\zeta}}
 +\frac14\left(v-\kappa^{-1}\right). \tag{8}
\]
The correction is adapted to the CH geometry: on every CH orbit
\(\kappa=\coth t\), \(\zeta=\operatorname{csch}^2t\), and \(v=\tanh t=\kappa^{-1}\), so \(\widetilde B=0\). The coefficient \(1/4\) is not forced by CH vanishing alone; it is useful because it removes a fibre-velocity term from the linear ACH drift.

Let
\[
E=\operatorname{Ric}_{ff}
 -\frac{\operatorname{Ric}_{gg}+\operatorname{Ric}_{hh}}2.
\]
Direct symbolic differentiation using the exact diagonal Ricci equations gives
\[
\widetilde B'=F_\beta-\frac14E, \tag{9}
\]
where \(F_\beta\) is the same expression evaluated on the uncontrolled Einstein equations. The identity and CH vanishing are in `scripts/beta_pinning_identity.py` and `data/beta_pinning_identity.json`. The tensor normalization is
\[
|\operatorname{Ric}^{\circ}|^2
 =\frac34H^2+\frac23E^2+\frac12D^2,
\]
so \(\widehat P\ge\frac16\int WE^2dt\). Hence
\[
\boxed{
\left|\Delta\widetilde B-\int F_\beta\,dt\right|
 \le
 \sqrt{\frac{3\widehat P}{8}}
 \left(\int\frac{dt}{W}\right)^{1/2}.}
\tag{10}
\]
This is the exact fibre/base counterpart of Lemma P. Its control factor differs because the traceless diagonal tensor associated with \(E\) has squared norm \(2E^2/3\).

On an exact CH tail,
\[
W=\sinh^3t\cosh t,
\quad
I(T):=\int_T^\infty\frac{dt}{W}
 =\frac1{2\sinh^2T}
 -\frac12\log(1+\sinh^{-2}T). \tag{11}
\]
If the correction interval is exact CH—or if a separate comparison proves \(\int W_g^{-1}dt\le I(T)\)—and the drift-corrected mismatch is \(C\), then
\[
\widehat P\ge\frac{8C^2}{3I(T)}. \tag{12}
\]
For a general connector, the denominator remains its actual \(\int W_g^{-1}dt\); a CH terminal first jet alone does not justify substituting \(I(T)\). The threshold table is `data/beta_pinning_threshold.json`. With the CH denominator, overlap with Corollary X3 at \(t=.70\) requires mismatch at least
\[
C_*=\sqrt{3I(.70)/8}=0.370125\ldots. \tag{13}
\]
The raw shape change \(\beta\) is not itself enough: the first-jet correction in (8) cancels exact CH radial evolution, and the uncontrolled drift \(F_\beta\) must be bounded along the pre-ACH connector. In the verified ACH block, the Taylor calculation has zero constant term and linear term
\[
z\left(-\frac15s_2+\frac25u-\cosh q+1\right). \tag{14}
\]
It is not sign-definite, and the factor \(z\) only makes it small when \(q\) is also controlled. Thus (10) explains the large-radius exponential behavior in a standard ACH block, but a volume comparison and a geometric mismatch estimate—or a compact interval enclosure—are still needed on the saturation region.

## 3. Anisotropic entry computation

`scripts/saturation_anisotropic_scan.py` runs the full three-control Hermite–Simpson problem with altered entry first jets. `data/saturation_control/step30_anisotropic_summary.json` records the runs.

Two classes must be separated.

### 3.1 Finite-charge first-jet perturbations

The finite-charge mode uses (4): \(x=Xz^3\), \(\chi=Cz\), \(\eta=Nz\). At \(\varepsilon=1/16\), the charge-changing examples behaved as predicted:

* \(X=0,C=1\): cost \(4.9625\), initial \(\mathfrak b_+=-2.9417\);
* \(X=1,C=0\): cost \(21.727\), initial \(\mathfrak b_+=-19.512\) at this not-yet-asymptotic scale;
* the charge-kernel direction \(X=1,C=-4\): cost \(3.5789\), initial \(\mathfrak b_+=-1.5854\); at \(\varepsilon=1/32\) the cost is \(3.7783\), moving toward the limiting value \(4\).

A large finite-charge \(N=-8\) perturbation lowers the finite-\(\varepsilon\) cost to \(2.2668\), but (5) says it cannot alter the limiting plus charge. This normalized-jet ansatz is not automatically bounded-curvature geometry. The run shows a finite-scale matching effect, not evidence against Q″.

### 3.2 Enlarged raw entry jets

Allowing fixed \(O(1)\) perturbations as the circle collapses can make the connector much cheaper. The strongest run at \(\varepsilon=1/16\), raw \(\Delta\eta=-8\), has collocation cost \(0.54541\); independent actual-metric reconstruction gives \(0.57446\). The connector alone is below the certified Burns-core cell, but the run is not a regular bolt/collapse construction: its scaling violates (4), and the same raw perturbation at \(\varepsilon=1/32\) costs \(2.94250\), with reconstructed cost \(2.94303\). Fixed raw \(x=\pm .25\) produces enormous charges and costs \(221\)–\(361\).

The cheap raw jet already has \(\mathfrak b_+=1.45194\), so the omitted bolt-to-entry prefix costs at least \(1.45194-1=0.45194\). Adding this to the reconstructed connector gives at least \(1.0264\), above the certified cell. This run therefore does not undercut the cell even before a regular-prefix construction is imposed. It shows instead that arbitrary first jets can destroy the connector's value-four law at finite scale. The exact identity
\[
\mathfrak b_+=-2-(u_f-u_g)^2+\delta(4-u_fu_g)-\delta^2,
\qquad \delta=u_h+2,
\]
explains the mechanism: raw opening rate \(\delta\ne0\) can raise the entry charge. Thus \(\eta\), the contact-slot shear velocity, is the dangerous high-shear coordinate. A small-bolt theorem must show that regular bolt data enter a finite-charge or bounded-geometry class, or account for the cost of producing raw \(O(1)\) shear before the selected section.

## 4. Consequences and next proof work

1. Q″ rigorously prices any collapsed-to-round annulus once its normalized entry charge is known. Bounded-geometry Berger collapse has \(\mathfrak b_+\to-2\), hence pays at least \(4-o(1)\).
2. Finite-charge anisotropy changes the price to \(4+(C+4X)^2\); the kernel \(C+4X=0\) retains charge \(-2\), but it is not automatically bounded-curvature geometry.
3. The live branch is loss of normalized first-jet control, especially raw contact shear \(\eta\). This is the high-shear volume-bounce mechanism.
4. The beta-pinning identity (10) supplies the late-opening tool. Closing the branch by it and X3 requires an actual \(W^{-1}\) comparison and a drift-corrected mismatch bound; with the exact CH denominator at \(t=.70\), the needed value is \(0.370125\ldots\).
5. Beyond symmetry, the transferable target is an adiabatic characteristic charge of a collapsed F-structure link and a relative bulk transgression. That would replace unavailable pointwise-Ricci regularity in the global collapse passage.

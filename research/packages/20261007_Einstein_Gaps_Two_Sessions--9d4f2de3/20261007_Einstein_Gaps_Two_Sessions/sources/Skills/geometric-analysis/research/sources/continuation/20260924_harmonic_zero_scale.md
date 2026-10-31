# Harmonic zeros have a fourth-order scale cost

24 September 2026. This note strengthens the whole-filling criterion in
[Harmonic/contact Milnor matching](20260924_harmonic_contact_milnor_matching.md).
Its qualitative hypothesis that the actual harmonic representative have no
zeros is replaced by a quantitative comparison between the original
Einstein/calibration defect and a metric coordinate scale on the **entire
filling**. No identification of a terminal ALE space with that filling is
made.

The analytic ingredient is an elementary local Hodge estimate, composed
with the inherited actual-form theorem. A classical local construction of
Taubes supplies the complementary example: even a fixed actual monopole
class, unchanged periods and boundary data, exact harmonicity, and vanishing
averaged structure errors do not by themselves prevent zero circles. The
example is not pointwise almost Einstein. These two statements specify
exactly which additional scale information the present bridge uses.

## 1. A metric scale and a local theorem

Fix \(0<\alpha<1\) and \(Q\ge 2\). A number \(0<\rho\le1\) is an
**admissible coordinate scale** at \(x\in(M,g)\) if there is a smooth
embedding \(\phi:B_2(0)\subset\mathbb R^4\longrightarrow M\), with
\(\phi(0)=x\), such that
\[
 \widehat g=\rho^{-2}\phi^*g,\qquad
 Q^{-1}I\le\widehat g\le QI,\qquad
 \|\widehat g\|_{C^{1,\alpha}(B_2)}\le Q.                \tag{1}
\]
Changing the harmless numerical convention in the coordinate norm changes
only the constants below. Write \(U_{x,\rho}=\phi(B_2)\), and denote the
supremum of these scales by \(r_{\alpha,Q}(x)\). Smoothness supplies a
positive scale at every point, after increasing the fixed \(Q\) if needed.
The scale is capped at 1 because the target Einstein normalization has
already fixed an ambient length unit. Harmonic coordinates satisfying (1)
can be used, but their coordinate functions need not be harmonic.

Thus (1) is a condition solely on the metric, independent of the harmonic
form or its zeros. It is not a lower bound on the injectivity radius of
the entire manifold, and no uniform positive lower bound for this scale
will be imposed on a sequence.

**Theorem 1 (a harmonic zero costs normalized amplitude energy).** There
is \(c=c(\alpha,Q)>0\) with the following property. Let \(\Omega\) be a
smooth two-form satisfying
\[
                         d\Omega=d_g^*\Omega=0
\]
on \(U_{x,\rho}\), where (1) holds. If \(\Omega(x)=0\), then
\[
 \boxed{\displaystyle
  \int_{U_{x,\rho}}\bigl(|\Omega|_g-\sqrt2\bigr)^2\,d\mu_g
       \ge c\rho^4.}                                      \tag{2}
\]
Self-duality is unnecessary for this local assertion. The normalization
\(\sqrt2\) is the one used by the global monopole construction.

**Proof.** Pull back and rescale both objects by
\[
          \widehat g=\rho^{-2}\phi^*g,\qquad
          \widehat\Omega=\rho^{-2}\phi^*\Omega.
\]
Then \(|\widehat\Omega|_{\widehat g}=|\Omega|_g\circ\phi\), the
Hodge equations remain homogeneous, and the integral in (2) is
\(\rho^4\) times the corresponding integral on \(B_2\). Work at this
unit scale and call that integral \(A\). If \(A\ge1\), the conclusion
holds with any \(c\le1\). Otherwise
\[
 \int_{B_2}|\widehat\Omega|^2\,d\mu_{\widehat g}
 \le 2A+4\operatorname{Vol}_{\widehat g}(B_2)\le C(Q).       \tag{3}
\]

Here is the regularity input, including its coefficient requirements.
View \(D=d+d_{\widehat g}^*\) on the full exterior-algebra bundle. Its
principal symbol is Clifford multiplication and is uniformly invertible
away from the zero covector. In coordinates its principal coefficients
are uniformly \(C^{1,\alpha}\), and its zero-order coefficients are
bounded, by (1). The local first-order elliptic estimate on nested balls is
\[
 \|u\|_{W^{1,p}(B_a)}
 \le C(p,Q,\alpha,a,b)
       \bigl(\|Du\|_{L^p(B_b)}+\|u\|_{L^p(B_b)}\bigr),
 \qquad 0<a<b<2.                                         \tag{4}
\]
One obtains (4) by freezing the principal coefficients on uniformly small
coordinate balls, applying the constant-coefficient Fourier-multiplier
estimate, absorbing their oscillation, and using a cutoff; the bounded
zero-order term is retained on the right. A finite covering gives the
displayed constants. This argument needs no bound on second metric
derivatives and takes no derivative of Ricci curvature.

Apply (4) to the pure-degree form \(\widehat\Omega\), viewed as an
inhomogeneous form. Its full Hodge--Dirac image is zero. Starting from
(3), successively use \(W^{1,2}\hookrightarrow L^4\), the interior
\(W^{1,4}\) estimate, the critical embedding into each finite \(L^p\),
and the \(W^{1,8}\) estimate. Morrey's inequality gives, on \(B_1\),
\[
       \|\widehat\Omega\|_{C^{0,1/2}(B_1)}\le C(\alpha,Q).
                                                               \tag{5}
\]
Since \(\widehat\Omega(0)=0\), uniform ellipticity and (5) imply
\(|\widehat\Omega|_{\widehat g}\le1/2\) throughout \(B_\theta\)
for a fixed \(\theta=\theta(\alpha,Q)>0\). Consequently
\[
 A\ge(\sqrt2-1/2)^2\operatorname{Vol}_{\widehat g}(B_\theta)
   \ge(\sqrt2-1/2)^2Q^{-2}|B_\theta|>0.
\]
Taking the minimum of this lower bound and 1 and rescaling proves (2).
\(\square\)

In particular, the theorem is not a new bounded-Ricci regularity theorem:
it uses a declared coordinate scale. Its content for this project is that
the actual Hodge equation turns the supplied mean amplitude into a
quantitative obstruction to zeros at that scale.

## 2. Eliminating the auxiliary form from the condition

Use the input and conventions of
[Actual-form composition](../mathematics/current/line1_composed_application.md).
Thus \(M\) is closed, connected, oriented and four-dimensional, and
\(a\) is the first Chern class of a Spin\(^c\) structure whose
unperturbed Seiberg--Witten equations are solvable for every metric in
\([g]\). The structure remains fixed as the positive weight varies.
Let
\[
 \begin{split}
 V&=\operatorname{Vol}(M,g),\qquad p=(a_g^+)^2>0,\\
 r&=\fint_M|\operatorname{Ric}_g+g|^2,\\
 q&=V^{-1}\left[\frac32\int_M(s^2+12|W^+|^2)
                                      -72\pi^2p\right],
 \qquad \kappa=r+q\le1/2880.
 \end{split}                                             \tag{6}
\]
The curvature functional gives \(q\ge0\). Let \(H\) denote the
harmonic self-dual representative of \(a_g^+\), not the harmonic
representative of the whole class when \(a_g^-\ne0\), and put
\(\Omega=-2\pi H\).

**Lemma 2 (actual harmonic amplitude).** The inherited supply theorem
implies directly
\[
 \boxed{\displaystyle
  \int_M\bigl(|\Omega|-\sqrt2\bigr)^2\,d\mu
                          \le818\kappa V.}             \tag{7}
\]
There is no remaining auxiliary weight or negative-square budget in (7).

**Proof.** For every \(\eta>0\) sufficiently small, the same actual
class supplies a smooth form \(\omega\) satisfying
\[
 \int|\omega-\Omega|^2\le(49\kappa+\eta)V,\qquad
 \int(|\omega|^2-2)^2\le(720\kappa+\eta)V.
\]
The reverse triangle inequality and
\[
       (t-\sqrt2)^2=\frac{(t^2-2)^2}{(t+\sqrt2)^2}
                      \le\tfrac12(t^2-2)^2,\qquad t\ge0,
\]
give
\[
 \int(|\Omega|-\sqrt2)^2
 \le2\int|\Omega-\omega|^2+\int(|\omega|^2-2)^2
 \le(818\kappa+3\eta)V.
\]
The left side is independent of the weight and of \(\eta\). Let
\(\eta\downarrow0\). No convergence of the auxiliary forms is
asserted or needed. \(\square\)

Combining (2) and (7) yields a purely raw-input consequence:
\[
 \boxed{H(x)=0\quad\Longrightarrow\quad
       r_{\alpha,Q}(x)^4\le C(\alpha,Q)\kappa V.}        \tag{8}
\]
Indeed apply (2) at every admissible scale and then take their supremum.
This also handles the case where that supremum is not attained.

## 3. Whole-core matching and exact realization

Retain the raw compactification hypotheses
\[
 \operatorname{diam}(M_j,g_j)\le D,\qquad
 (a_j^+)^2\ge A_0>0,\qquad
 \delta_j+q_j\longrightarrow0,
 \quad \delta_j=\|\operatorname{Ric}_{g_j}^{\sharp}+I\|_{\infty,\mathrm{op}}.
                                                               \tag{9}
\]
Each \(a_j\) is supplied by an actual conformally solvable Spin\(^c\)
structure, with the fixed-structure/variable-weight quantifier of Section 2.
By [Orbifold smoothing bridge](20260924_orbifold_smoothing_bridge.md),
Theorem A, a subsequence has a compact negative KE orbifold limit
\((X,h,J)\). Its regular exterior, with fixed small collars around the
singular links, embeds in \(M_j\). Let \(B_{\nu,j}\) be the
complementary **whole** connected fillings, with their actual markings.
As in that theorem, each chosen link bounds its indicated filling. All
nested necks and bubbles are included in \(B_{\nu,j}\).

For each \(j\), suppose metric data supply a number \(\rho_j>0\)
such that every point of \(\bigcup_\nu B_{\nu,j}\) has an admissible
coordinate scale at least \(\rho_j\), with fixed \(\alpha,Q\).
The coordinate neighborhoods lie in \(M_j\) and may cross the fixed
boundary collars. This avoids any boundary estimate for the Hodge equation.

**Theorem 3 (defect-to-core-scale realization).** There is
\(c_0=c_0(\alpha,Q)>0\) such that the following conditions, for all
sufficiently large indices in the extracted subsequence, force marked
Milnor matching:

1. \((r_j+q_j)V_j<c_0\rho_j^4\);
2. each singular filling satisfies either
   - its limiting singularity is \(A_1\) and
     \(b_2(B_{\nu,j};\mathbb Q)=1\), or
   - \(B_{\nu,j}\) is a rational homology four-ball.

The second alternative forces the limiting singularity to be Wahl,
\(\frac1{n^2}(1,na-1)\), with \(n\ge2\), \(0<a<n\), and
\((a,n)=1\). Every actual marked filling is diffeomorphic to the
corresponding local Q-Gorenstein Milnor fiber.

If, in addition, the complex orbifold \(X\) admits a projective
Q-Gorenstein smoothing, then each such \(M_j\), on its original smooth
structure, admits a negative Kähler--Einstein metric. A sufficient global
smoothing test is \(H^2(Z,T_Z(-\log E))=0\), with the resolution and
divisor as in Lee--Park's criterion used in the inherited bridge.

The first condition is implied by either of the more directly recorded
conditions
\[
           \frac{(r_j+q_j)V_j}{\rho_j^4}\longrightarrow0,
 \qquad\text{or}\qquad
           \frac{(4\delta_j^2+q_j)V_j}{\rho_j^4}
                                     \longrightarrow0.          \tag{10}
\]

**Proof.** Since \(r_j\le4\delta_j^2\), (9) puts the sequence within
the range of Lemma 2. If \(H_j\) vanished at a point of a whole
filling, (2) and (7), applied at the supplied scale, would imply
\(c\rho_j^4\le818(r_j+q_j)V_j\). Choose \(c_0<c/818\).
Thus every \(H_j\) is zero-free on the entire filling.

The inherited harmonic/contact theorem now applies, with no change to
its remaining hypotheses. For clarity, its implications are as follows.
The actual \(\Omega_j=-2\pi H_j\) converges to the limiting Kähler
form in \(C^{1,\beta}\) on each fixed regular collar. Therefore it
gives the canonical strong convex contact boundary. Self-duality and
closedness, together with the newly proved nonvanishing throughout the
core, make \((B_{\nu,j},\Omega_j)\) a strong symplectic filling.
Classical filling classification gives the \(A_1\) Milnor filling in
the first case, and a Wahl rational ball in the second. The boundary
mapping-class extension argument in that theorem gives the actual
relative marking, not merely an unmarked diffeomorphism.

If a global smoothing exists, its exterior trivialization and these
relative diffeomorphisms glue to an oriented diffeomorphism from \(M_j\)
to a smooth fiber. The canonical divisor is ample, by the negative KE
metric on \(X\) and openness of ampleness in the Q-Gorenstein family.
Aubin--Yau gives a negative KE metric on the smooth fiber; pull it back.
This proves existence on \(M_j\), without an Einstein inverse or a
claim that the new metric is close to \(g_j\). \(\square\)

There is no positive lower bound on \(\rho_j\): the theorem permits
concentration at arbitrarily small scales if the original total defect
decays faster than the fourth power of the smallest supplied core scale.
The metric scale, the Betti/rational-ball condition, and the global
smoothing test are separate verifiable inputs; none is declared to
follow from (9) alone. The result includes non-Einstein inputs: sufficiently
small smooth perturbations of any negative KE metric with its compatible
actual class satisfy the criterion on prescribed cores, by continuity of
the Hodge projection and the functionals. On a degenerating KE sequence,
one may choose the perturbations separately at each positive \(\rho_j\).
This observation establishes nonemptiness, not a new construction of KE
metrics or a new smoothing example.

**Corollary 4 (non-Wahl rational cores have a quantitative cost).** In
(9), suppose a whole filling is a rational homology ball but its limiting
singularity is not Wahl. Then for large \(j\) it contains an interior
zero \(x_j\) of \(H_j\), and
\[
               r_{\alpha,Q}(x_j)^4
                    \le C(\alpha,Q)(r_j+q_j)V_j.         \tag{11}
\]
If all its points have a supplied scale at least \(\rho_j\), then
\((r_j+q_j)V_j\ge c_0\rho_j^4\), after reducing \(c_0\).

**Proof.** The inherited contact-filling obstruction forces a zero, and
its regular collar contains none. Apply (8). \(\square\)

## 4. Unchanged periods and harmonicity do not remove the scale issue

The following construction is classical at its source. Its quantitative
rescaling identifies a genuine limitation of replacing the new condition
by averaged form information alone.

**Proposition 5 (small-support harmonic zero circles).** Let
\((S,g_0,J,\Omega_0)\) be a fixed closed Kähler surface, with
\(|\Omega_0|_{g_0}=\sqrt2\). There are smooth metrics \(g_\rho\)
and closed self-dual forms \(\Omega_\rho\), for \(\rho\downarrow0\),
such that:

1. \(g_\rho=g_0\) and \(\Omega_\rho=\Omega_0\) outside a fixed
   Darboux ball of radius \(C\rho\);
2. \([\Omega_\rho]=[\Omega_0]\), and \(\Omega_\rho\) is its
   **actual harmonic representative** for \(g_\rho\);
3. \(\Omega_\rho\) has a transverse zero circle in that ball;
4. \(g_\rho\) is uniformly bilipschitz to \(g_0\),
   \(\|\Omega_\rho\|_\infty\le2\sqrt3\), and
\[
 \begin{split}
 \int_S(|\Omega_\rho|^2-2)^2\,d\mu_{g_\rho}&=O(\rho^4),\\
 \int_S|\Omega_\rho-\Omega_0|_{g_\rho}^2\,d\mu_{g_\rho}
                                                    &=O(\rho^4),\\
 \int_S|\nabla^{g_\rho}\Omega_\rho|^2\,d\mu_{g_\rho}
                                                    &=O(\rho^2),\\
 \int_S|\nabla^{2,g_\rho}\Omega_\rho|^2\,d\mu_{g_\rho}
                                                    &=O(1).
 \end{split}                                                   \tag{12}
\]
In particular the first three integrals tend to zero, although zeros
persist. The volumes stay bounded above and below, so the same conclusions
hold for averaged integrals. The Hodge Laplacian of each form is exactly
zero.

**Proof.** Taubes [T06], Proposition 2.1 and its proof in Section 2,
construct a near-symplectic form on a standard symplectic ball which
equals the standard form outside a compact interior set and has one
transverse zero circle. Its compactly supported difference from the
standard form is exact: \(H_c^2(B^4;\mathbb R)=0\). Fix one such
model, denoted \(\widetilde\Omega\), on a ball of fixed radius.

Auroux--Donaldson--Katzarkov [ADK05], Proposition 1, supply a smooth
metric making this closed form self-dual and hence harmonic. The metric
may be prescribed to be Euclidean near the boundary, where the form is
standard. To see the relative assertion directly from their Section 7.2,
positive three-plane bundles containing a given positive two-form form a
convex set in the graph parametrization of the positive Grassmannian.
Extend the positive plane determined near the zero circle, and splice it
to the Euclidean positive plane on the exterior annulus, where the form
is nonzero. This constructs a conformal class agreeing with the prescribed
one there. Choose a smooth conformal factor agreeing with 1 there and
large enough on the interior to arrange
\(|\widetilde\Omega|\le2\sqrt3\). This rescaling preserves
self-duality of two-forms in dimension four. We may also arrange that its
Ricci tensor is nonzero at some interior point: a further smooth conformal
perturbation supported away from the zero circle can prescribe a nonzero
Hessian at a point, and the conformal Ricci formula then ensures this.
Take the perturbation small enough to retain the amplitude bound, first
leaving a strict margin there. Fix the resulting smooth model metric.

Take Darboux coordinates for \(\Omega_0\) at a point of \(S\), with
\(g_0\) equal to the Euclidean metric at the origin. Transplant the
model by dilation \(x=\rho y\): its coordinate coefficients are
\(\widetilde g(x/\rho)\) and
\(\widetilde\Omega_{ab}(x/\rho)\). Equivalently, the pullbacks
under dilation are \(\rho^2\widetilde g\) and
\(\rho^2\widetilde\Omega\). The form equals \(\Omega_0\)
near the boundary and glues exactly. On a surrounding annulus keep that
form fixed and interpolate the compatible positive planes from the model
metric to those of \(g_0\). Since \(g_0(\rho y)\) is uniformly
smooth and tends to its value at the origin, this relative interpolation
has uniformly bounded derivatives in the \(y\) coordinates. Its
conformal factor can again enforce the stated amplitude bound and match
\(g_0\). Both objects are unchanged outside the enlarged ball.

The compactly supported exactness proves equality of classes. Closedness
and self-duality give \(d^*_{g_\rho}\Omega_\rho=0\); on the closed
manifold Hodge uniqueness makes it the actual harmonic representative.
The inserted transverse zero circle is unaffected by the outer annulus.

In rescaled coordinates the metrics are uniformly smooth and elliptic,
the form is uniformly smooth, and the changed region has volume
\(O(\rho^4)\). One and two covariant derivatives of the form are
respectively \(O(\rho^{-1})\) and \(O(\rho^{-2})\) there. Outside,
the original Kähler form is parallel for the original metric. These facts
prove all four estimates (12). \(\square\)

This applies with an actual class, rather than merely a real cohomology
class. For example take the negative KE product of two closed hyperbolic
curves of genus at least two. Put \(a=c_1(S,J)\), so
\([\Omega_0]=-2\pi a\), and \(a^2>0\). Its canonical Spin\(^c\)
class and its negative are ordinary monopole classes, by the classical
Seiberg--Witten input recalled in LeBrun [L06], Section 3. In particular
the same structure is solvable for all metrics, hence for all conformal
weights for each \(g_\rho\). Proposition 5 gives
\[
       a^+_{g_\rho}=a,\qquad a^-_{g_\rho}=0,\qquad
       -2\pi H_{g_\rho}=\Omega_\rho,
\]
with \(p=a^2\) fixed and positive. All periods, the positive projection
budget, and the negative-square cost are unchanged; there are nevertheless
harmonic zero circles and arbitrarily small averaged structure errors.

The construction is also relative on any prescribed symplectic Milnor
filling: perform it in an interior Darboux ball of an \(A_1\) or Wahl
fiber, away from its contact collar. The filling, its boundary marking,
its boundary form and **every period on every closed two-cycle** are
unchanged. It creates interior zeros of a closed self-dual harmonic form.
On a filling this means a solution of the interior Hodge equations; no
uniqueness for an unspecified boundary value problem is claimed. On a
closed ambient manifold the uniqueness assertion is the one in
Proposition 5. No zero-free hypothesis can be deduced from these period
and collar data alone.

At a zero of the inserted model, (1) holds with scale at least
\(c_1\rho\), for fixed \(\alpha,Q\). Theorem 1 supplies the reverse
order of magnitude for the amplitude error, while (12) supplies the
upper bound. Thus the power four in (2) is the correct scaling for the
local statement: a hypothesis \(A=o(\rho^\gamma)\) with
\(\gamma<4\) would allow these zero-circle examples. This is not a
claim of sharp constants or sharpness within pointwise almost-Einstein
sequences.

## 5. Exact scope of the new bridge

The conclusion added to the previous theorem is
\[
 \boxed{\text{actual raw defect below the fourth power of the whole-core
 scale}\ \Longrightarrow\ \text{marked Milnor matching}}
\]
in its stated \(A_1\)/rational-ball topological regimes. After the
separate global Q-Gorenstein test this gives an Einstein metric on the
original smooth manifold, as required by Yau26 for the covered inputs.

The zero-circle construction explains why keeping only global averages
would lose relevant information. It does **not** satisfy the claimed
small pointwise Ricci hypothesis (9): the fixed nonzero model Ricci tensor
in the preceding proof gives
\(\delta_-(g_\rho)\ge c\rho^{-2}-1\) at its transplanted point.
Thus the pointwise Ricci defect actually diverges. Nor do (12) establish
that the raw functional \(r_\rho+q_\rho\) tends to zero. Therefore
it neither disproves automatic matching under the complete original
input nor supplies a Yau26 counterexample. What it disproves is inference
of nonvanishing from the listed harmonic, period and average-form
properties alone.

The remaining mathematical question is consequently specific: does the
pointwise Ricci equation plus actual near-saturation force the ratio in
(10), or provide a different zero-removal mechanism on the concentration
cores? That implication has not been proved here. The present theorem
allows the ratio to be checked directly and quantifies its failure when
contact topology forces a zero; it does not assume that all relevant ALE
information has already classified the whole core.

## References and inherited dependencies

- [T06] C. H. Taubes, *A proof of a theorem of Luttinger and Simpson about
  the number of vanishing circles of a near-symplectic form on a
  4-dimensional manifold*, Mathematical Research Letters **13** (2006),
  no. 4, 557--570. Proposition 2.1 and the compactly supported birth
  construction in Section 2. [Publisher PDF](https://intlpress.com/api/bgcloud-front/resource/pdf/volume/1806605523900329985-1806605523900329985-9fa5106dca972fdc95f65c34eac2bf03.pdf).
- [ADK05] D. Auroux, S. K. Donaldson and L. Katzarkov, *Singular Lefschetz
  pencils*, Geometry & Topology **9** (2005), 1043--1114. Proposition 1
  and its positive-plane-bundle proof in Section 7.2.
  [Original manuscript](https://arxiv.org/html/math/0410332).
- [L06] C. LeBrun, *Four-Manifolds, Curvature Bounds, and Convex Geometry*,
  preprint (2006). Section 3 for actual monopole classes, and Section 2
  for Hodge and chirality conventions.
  [Original manuscript](https://arxiv.org/html/math/0611450).
- [Supply] [Actual-form composition](../mathematics/current/line1_composed_application.md),
  the inherited theorem, estimates (2) and (4). Their constants give 818
  in (7); their proof is not replaced by this note.
- [Compactification] [Orbifold smoothing bridge](20260924_orbifold_smoothing_bridge.md),
  Theorems A and C, and Corollary D. These supply the bounded-Ricci
  compactification and the separately checked global smoothing input.
- [Matching] [Harmonic/contact Milnor matching](20260924_harmonic_contact_milnor_matching.md),
  Theorem 1 and Corollaries 6--7, including its classical filling
  classifications and boundary-extension proofs. Only its whole-core
  nonvanishing premise is replaced here.

No priority claim is made for the local elliptic estimate or the
zero-circle construction. The new project-level application is their
composition with actual monopole supply and marked filling classification.

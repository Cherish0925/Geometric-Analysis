# Step 39 — The actual harmonic-zero test object and the next tariff problem

## 1. Scope and normalization

The established local metric is the perpendicular exact-complex-hyperbolic blow-up cell

after its sixfold rescaling to the closed-family convention \(\operatorname{Ric}=-g\).  On the
unrescaled computational profile \(\operatorname{Ric}_{CH}=-6g\), let
\[
 \Omega=\frac12d(\phi\sigma_f),\qquad
 \frac{\phi'}{\phi}=\frac{2a_f}{a_ga_h},
 \qquad \phi=a_ga_h\quad\hbox{on the exact CH collar}.
\]
Then
\[
 \Omega=u^2(e^{0f}+e^{gh}),\qquad u^2=\frac{\phi}{a_ga_h},
 \qquad |\Omega|_g^2=2u^4.
\]
It is smooth, closed and self-dual for the actual cell metric, hence harmonic.  Near the
perpendicular bolt, \(a_h=t+O(t^3)\), \(a_f,a_g=b+O(t^2)\), and the ODE gives
\(\phi=Ct^2(1+O(t^2))\); the invariant potential has the required smooth vanishing.  It equals
the host Kähler form on an open exact collar, extends by that form over the untouched host without
a cutoff, has zero period on the exceptional sphere, and vanishes along the bolt.  Replicating the
cells gives a closed smooth harmonic form on the actual closed construction, with a zero surface in
each cell.
This is consistent with the Taubes period statement: the excluded object was a nowhere-zero
zero-period symplectic form, not a harmonic form with zeros.

The form is in the pullback of the host Kähler ray.  In \(2\pi\)-integral normalization on the
unrescaled \(\operatorname{Ric}=-6g\) host, \([\Omega]/2\pi=\pm K_X/6\), so its square and canonical
pairing are \(A/36\) and \(A/6\).  After \(\bar g=6g\) and \(\psi=6\Omega\),
\([\psi]/2\pi=\pm K_X\).  In either normalization the homogeneous period angle is exactly
\(\eta=1\), while the exceptional-area contribution is zero.  This is special to the fixed
pullback class; an unrestricted harmonic/self-dual direction may drift out of the Kähler
Hodge-index plane, and then \(\eta\) must remain a variable.

On the complement of the zeros, \(\widehat g=u^2g\) has \(|\Omega|^2_{\widehat g}=2\) and is
almost-Kähler.  However, \(\widehat g\) has the anisotropic power-law singularity already described
in Step 28 at every bolt.  Consequently the closed smooth AKΓ theorem and its pocket refinement
cannot be applied directly to \((\widehat g,\Omega)\); any localization must expose the bolt flux or
zero-set term rather than silently discard it.

## 2. New computations on the actual form

The reproducible evaluator is `workspace/scripts/step39_harmonic_zero_profile.py`.  It uses the
same Cartan curvature package as Steps 27–29 and evaluates both the floating
\(x_0=.038,X=128\) profile and the exact-dyadic coefficient profile underlying the certified cell.
The latter's form statistics remain floating, while its Ricci cost retains the independent Arb
certificate.

Outputs:

* `workspace/data/step39/harmonic_zero_certifiedprofile_x003_X128.json`;
* `workspace/data/step39/harmonic_zero_x0038_X128.json`.

The volume pinning
\[
 \int u^4dV_g=V_{CH}
\]
is reproduced to \(7.8\times10^{-9}\) (certified profile) and \(1.8\times10^{-9}\)
(floating profile), in the script's \(2\pi^2\) units.  The smooth harmonic form has, per cell:

\[
\begin{array}{c|cc}
 & x_0=.03\ \hbox{certified coefficients} & x_0=.038\ \hbox{floating}\\ \hline
\int(q-2)^2\,dV_{g\;(\mathrm{Ric}=-g)}/(2\pi^2) &0.0765841&0.1097711\\
\int|\nabla\psi|^2\,dV_{g\;(\mathrm{Ric}=-g)}/(2\pi^2)&0.4524720&0.5891247\\
\int|W^+-A_{\psi,1/2}|^2\,dV/(2\pi^2)&0.0224054&0.0336106
\end{array}
\]
where under the rescaling \(\bar g=6g\) we use \(\psi=6\Omega\), so
\(|\psi|^2_{\bar g}=|\Omega|^2_g=q\).  The one-derivative energy scales by six, the amplitude
integral by thirty-six, and the Weyl-model integral is scale invariant.  The gradient integral is
computed by the integrated harmonic-form Weitzenböck identity; its displayed integrand is not a
pointwise norm density and changes sign locally.

There are two nearby augmented numerators and they must not be conflated.  The trace-free version
\[
 d^P_{1/2}V=\int\bigl(|\operatorname{Ric}^{\circ}|^2+|W^+-A_{\psi,1/2}|^2+(q-2)^2\bigr)
\]
equals \(4.0816409\,(2\pi^2)\) per certified-profile cell.  Replacing the first term by the full
Einstein residual \(|\operatorname{Ric}+g|^2\) adds the record's scalar-deviation term and gives
\(4.0816701\,(2\pi^2)\).  The difference is tiny for this profile but conceptually essential.
Replicated at \(k\) sites on a reference host with \(V=2\pi^2A\), the full version contributes
\(4.08167\,k/A\) at sparse density; the actual final glued volume produces the usual finite-density
correction.  Thus the actual zero-form geometry lies at the **linear surgery-density scale**, not at
a diffuse quadratic scale.  It is an excellent baseline for asking whether the localized
zero/rotation can spread, but it is not itself a low-tariff construction.

The singular hatted AK complement has no \(s^*>0\) region in either tested profile:
\[
 s^*=\widehat s+4\nu^2<0
\]
throughout the quadrature domain (sample maxima \(-23.50\) and \(-23.43\) in the
\(\operatorname{Ric}_{CH}=-6g\) scale).  Hence these perpendicular cells contain no aligned
positive-area Burns-saving pocket.  This does not invoke the closed pocket theorem; it only says
that the actual hatted mechanism is on the zero-set/perpendicular branch rather than secretly
using the newly identified \(s^*>0\) aligned branch.

The hatted torsion integrals \(\int4\nu^2dV_{\widehat g}/(2\pi^2)\) are \(0.0488589\) and
\(0.0651043\) in the profile scale, or \(0.2931532\) and \(0.3906259\) after rescaling to
\(\operatorname{Ric}=-g\).  Near the bolt, \(\widehat s\) and \(s^*\) diverge negatively; the
torsion integral remains finite but \(\int\widehat s^2dV_{\widehat g}\) diverges.  A correct
localization of AKΓ or Cotton transport must therefore be
written on the punctured cell and retain the limiting Chern/interface flux.  Steps 28–31 already
supply that flux for the diagonal cell; it is not a negligible regularity error.

## 3. Consequences for the diffuse-mode proposal

Three density regimes must remain separate.

### 3.1 Balanced and two-parameter families inside the inherited window

For
\[
 h=Q/A,\qquad r=\Delta/Q,\qquad\theta=k/Q,
 \qquad\sigma=4r+18\theta<4+c_0,
\]
the existing all-metric theorem gives \(\alpha\ge c(\sigma)h\).  No construction with
\(\alpha=o(Q/A)\) can exist there.  A conditional estimate of the form \(P\gtrsim R^2/A\) is only a
lower scale and cannot be read as an upper construction; if its quadratic scale were formally
smaller than the established linear lower order, some omitted field, amplitude, period-angle,
zero-set, or marked-core term must carry the difference.

### 3.2 Pure blow-ups outside that window

For \(\ell=0\), \(Q=k\), \(\theta=1\), and (for a ball-quotient host) \(r=0\), so
\(\sigma=18\): both inherited linear branches vanish.  This is the clean family on which a
diffuse zero/rotation construction could change the per-blow-up tariff without contradicting the
known theorem.  It must still be a coupled closed metric/form construction.  Spreading a direction
on a fixed Einstein host is insufficient; shrinking exceptional periods does not remove the marked
cell's finite action; and the glued harmonic form is not a monopole bilinear without solving or
controlling the field equations.

### 3.3 Density-free O10

Sparse blow-ups of ball quotients satisfy \(\chi/A=1/3+k/A\), which remains bounded.  Even a
successful pure-blow-up diffuse construction would address the tariff and near-minimizer geometry,
not density-free O10.  O10 additionally needs \(\chi/A\to\infty\) with its original actual-field
supply, normalization and parameter quantifiers.  These programmes may share a mechanism, but one
is not evidence for the other.

## 4. Route comparison after the cap tests

### The fixed transported-cell cap branch

Correct exponential marking and curvature-residual conditioning removed the old representation
loss.  The fixed-bolt response has a real inward relaxation coupled to an outer payment, with no
resolved net improvement.  No favorable linear term exists because CH and the Calabi cap have the
same \(R^+\), and the SU(2)-invariant constant \(W^-\) pairing vanishes.  Continuing this exact
fixed-bolt family is now lower value than the global tariff question.  A future cap return should
change the core (bolt area or bolt-compatible jets) rather than enlarge the same shell basis.

### Perturbative complex-hyperbolic coercivity

A02 Step 44 establishes a cover-independent absolute-global-Sobolev theorem near compact CH
quotients: the Einstein operator, conformal channel, gauge slice and canonical monopole branch have
model Bochner gaps, yielding \(P\ge\kappa(\|k\|_{H^2}^2+\|df\|_{H^1}^2)\) and canonical-branch
Nijenhuis energy \(R\le CP\).  This decisively rules out a diffuse common mode inside a fixed
absolute \(H^2\) neighbourhood of the KE host.

It does not yet price the actual blow-up configuration because the metric is not globally near the
host.  The needed theorem is a localized bulk statement with two genuine additions:

1. canonical-branch selection on the host-like bulk for every sign class, despite possible localized
   depletion/vortex behavior;
2. control of the collar/zero-set outer layer by the complete marked cores, rather than an
   uncontrolled \(L^2\) trace term.

The actual glued \((g,\Omega)\) is the right test: it is exactly host-Kähler on the bulk and contains
explicit unit-scale zero cores.  Any localized theorem should reproduce an \(O(k)\) exceptional
term on this object, not incorrectly force the form to be almost-Kähler through its zeros.

### Diffuse construction

To improve substantially on the localized \(O(k)\) baseline, a sequence must enlarge the region
where the metric/form pair departs from the KE branch so the rotation is carried over host-scale
volume, while keeping Ricci cost lower than the sum of marked core costs.  The new computation shows
what must decrease together: amplitude defect, harmonic-form derivative energy, negative-Kähler
Weyl-model error, and Ricci action.  The period-angle remains \(\eta=1\) only while the cohomology
class stays in the pullback Kähler plane.  If the class/direction drifts, AKΓ has prefactor
\(A(\eta+e)^2\) and that drift is a separate escape channel.  If the exceptional periods become
positive, the aligned route needs \(s^*>0\) pockets and no longer describes the perpendicular zero
cell.  These are materially different constructions.

### Mixed blow-up–handle cells

This remains an independent high-value construction front because pure handles are exactly priced
but their shared geometry with blow-ups is unknown.  It could alter the coefficient within the
linear-window families, whereas a pure-blow-up diffuse mode probes a region where current lower
bounds vanish.  No existing computation ranks it above the now-concrete harmonic-zero localization
problem, but it should not be discarded.

## 5. Main direction

The strongest next line is a two-sided study of the **localized-to-diffuse transition for the actual
harmonic-zero configuration**:

* Proof side: formulate a domain decomposition on a pure CH blow-up family.  The host-like bulk uses
  cover-uniform CH coercivity; each zero core uses the complete relative cell data; the interface is
  the full metric first jet together with the harmonic-form flux.  Determine whether the sum is
  necessarily linear in \(k\), or whether the bulk/cores can exchange a mode whose compliance grows
  with host volume.  The exterior mass null direction and Chern primitive from Steps 19 and 29 must
  be retained, not charged twice.
* Construction side: create a realizable closed family interpolating from localized zeros to diffuse
  harmonic-form degeneration, and solve the coupled metric and harmonic equation.  Measure
  \(P\), \(q=|\psi|^2\), \(\|W^+-A_{\psi,1/2}\|_2^2\), \(\|\nabla\psi\|_2^2\), zero geometry,
  \(\eta\), exceptional periods, and field-equation residuals.  The first discriminating target is a
  pure-blow-up tower outside the inherited window; a later connection to O10 requires a separate
  unbounded-density supplier.

This line connects the certified construction, Taubes topology, perturbative CH rigidity and the
unrestricted tariff on one actual object.  It is more likely to change the global coefficient than
another cap shell optimization or another conditional common-mode inequality.

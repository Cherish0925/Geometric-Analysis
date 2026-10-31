# First-line advance: a new topological application and equation-supplied structure

23 September 2026. Research baseline: commit `6065e33`. All work is local;
the running Qiushi instances, Sessions and installed Skills are unchanged.
The package preserves the earlier Skill snapshot and complete proof chain.

## 1. Main result: two chiralities, not another one-third threshold

For a minimal general-type complex surface \(X\), put
\[
 M=X\#k\overline{\mathbb{CP}}^{\,2}\#m(S^1\times S^3),\quad
 A=c_1^2(X)>0,\quad h=(k+4m)/A\in(0,1/3),
\]
\[
 U=\frac{3(2\chi(M)-3|\tau(M)|)}{A},\qquad
 F(h)=\frac{(4-\sqrt{1-3h})^2}{9}.
\]
The new theorem, using the existing integral functional-pencil theorem,
is
\[
 \boxed{\mathcal E(g)+(U-F(h))_+\ge c h^2}
\]
for every smooth metric, with a universal positive constant. Here
\(\mathcal E\) is the normalized integral distance to nonzero Einstein
rays. Ricci-flat metrics are excluded separately by the actual monopole
scalar estimate. In particular, a sufficiently small topological surplus
\(U-F(h)\) gives a positive integral gap and both pointwise Ricci gaps
on the same manifold.

The proof adds a genuine global upper bound to the earlier lower energy
envelope: both Chern--Weil identities give
\(e(1-\mathcal E)\le U\), where
\(e=\int|\operatorname{Ric}|^2/(8\pi^2A)\). This upper bound applies to
all candidate metrics and does not depend on a selected construction or
an energy-minimizing sequence.

There is an explicit realized infinite family. Let \(X_j\) be unbounded
finite covers of a compact complex-hyperbolic surface and \(A_j=c_1^2(X_j)\).
Choose
\[
 k_j=\lfloor29A_j/2025\rfloor,\qquad
 m_j=\lfloor397A_j/32400\rfloor-2.
\]
Then \(h_j\to19/300\), while \(0<U_j-F(h_j)<62/A_j\).
Every sufficiently large member therefore has a uniform positive
\(\mathcal E\)-gap and no Einstein metric of any sign. This lies outside
the previously recorded near-\(1/3\) strip and passes the specific
classical numerical tests compared in the proof. It is new coverage
relative to this research package; worldwide priority is not established.

Read the full proof and gauge inputs:
[two-chirality topology](line1_two_chirality_topology.md),
[PDF](line1_two_chirality_topology.pdf).

## 2. Analytic improvement: remove the auxiliary derivative budget

The complementary analytic result concerns a different question: what
geometric structure follows when the two upper eigenvalues of harmonic
\(W^+\) nearly coincide?

Write \(t=-3\lambda_1/4>0\), \(b=\lambda_3-\lambda_2\), and
\(z=b/(4t)<1\), with the lowest eigenvalue simple. The signed conformal
harmonic-Weyl identity yields
\[
 \int\frac32\frac{1-z^2}{1+z^2}t^{2/3}|Q|^2
 =\frac32\int t^{-1/3}b^2.
\]
Together with the scalar restoring equation, this gives, under fixed
\(m\le t\le M\) and \(z\le\theta<1\),
\[
 \fint\bigl[|dt|^2+(t-1/2)^2+|\nabla\omega|^2\bigr]
 \le C\fint[b^2+(s+4)^2].
\]
No auxiliary Hessian budget appears. The actual curvature supplies the
eigenform. This uses and explicitly credits the first-order method of
Catino--Dameno; the signed branch and scalar restoring argument are
written out. Unlike their positive-largest-eigenvalue rigidity theorem,
the negative-lowest-eigenvalue formula is an energy balance, not a claim
that every small splitting vanishes.

For exact \(\operatorname{Ric}=-g\), relative pinching
\(z\le\theta<1/\sqrt3\) also supplies the upper amplitude automatically:
\(t\le[2(1-3\theta^2)]^{-1}\). The lower amplitude remains a hypothesis.
Combining with a positive actual monopole budget forces a quantitative
spectral splitting on the blow-up/handle family.

Read [the signed harmonic-Weyl proof](line1_signed_harmonic_weyl.md)
([PDF](line1_signed_harmonic_weyl.pdf)) and
[the Einstein spectral application](line1_einstein_spectral_application.md)
([PDF](line1_einstein_spectral_application.pdf)).

A separate [half-Weyl regularity theorem](line1_half_weyl_regularity.md)
([PDF](line1_half_weyl_regularity.pdf)) supplies second-order estimates
from the actual curvature equation and extends to a nonzero equation
residual. It requires bounded Ricci, bounded \(W^+\), and an isolated
eigenline for the spectral-model estimates, but no control of \(W^-\),
Sobolev constant or injectivity radius. Its residual is not automatically
small under pointwise Ricci pinching.

## 3. Relation to Yau26

The topological theorem enlarges a specified class of smooth types on
which arbitrarily tight pointwise Ricci pinching is impossible. It does
not construct a counterexample: it excludes the proposed input there as
well as the Einstein output. Nor does this specified family exhaust all
smooth four-manifolds.

The harmonic-Weyl result studies an allowed geometric branch. It produces
an actual integral structure estimate, not an exact repair or a global
classification for arbitrary near-Einstein metrics. The two results have
different hypotheses and are not combined through an unproved implication.

## 4. Proof continuity and reproduction

The new topological chain is

`line1_integral_rigidity_paper.md` (core mechanism)
→ `line1_functional_pencil.md` (parameterized quantitative estimate)
→ `line1_energy_envelope_gap.md` (all-sign energy envelope)
→ `line1_two_chirality_topology.md` (both-chirality topological application).

The original Skill, round proofs, polarized closure, previous variable
calibration and new sources remain in this package. The present entrypoint
does not replace their proofs with this synopsis.

Run the four new finite checks with the local scientific Python:

```bash
python verify_line1_equation.py --output new-check-results
```

The output directory must be new. Exact algebra checks and deliberate
error tests support the formulas; the differential estimates and gauge
theory rely on the written proofs and cited inputs. See
[verification and proof review](line1_equation_verification.md) for the
actual scope. No publication, priority or journal-acceptance claim is made.

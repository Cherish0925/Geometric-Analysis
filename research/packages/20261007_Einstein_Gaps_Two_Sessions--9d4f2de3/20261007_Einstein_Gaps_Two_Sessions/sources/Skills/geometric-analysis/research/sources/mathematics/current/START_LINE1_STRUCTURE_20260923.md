# Pointwise input, conformal normalization, and global structure

23 September 2026. This continuation studies two proposed steps beyond
integral Einstein-defect estimates. It gives proofs, not a replacement
research roadmap. The inherited integral gap and its classical applications
are unchanged.

Write \(\delta_-(g)=\|g^{-1}\operatorname{Ric}_g+I\|_{\infty,\mathrm{op}}\).

## 1. A scalar-normalization theorem with a genuine endpoint counterexample

For every closed four-manifold with \(\delta_-(g)\le\epsilon\le1/4\),
the unique scalar-\(-4\) metric \(\widehat g=u^2g\) satisfies

\[
1-\epsilon\le u^2\le1+\epsilon,\qquad
\|du\|_\infty\le4\epsilon,
\]
\[
\fint_g\bigl((u-1)^2+|du|^2+|\nabla^2u|^2\bigr)\le6\epsilon^2,
\qquad
\fint_{\widehat g}|\operatorname{Ric}_{\widehat g}+\widehat g|^2
\le\frac{4\epsilon^2}{(1-\epsilon)^2}.
\]

No monopole, injectivity-radius, Sobolev, or scalar spectral-gap hypothesis
is needed. The gradient estimate comes from a positive-mass heat resolvent;
the Hessian estimate comes from integrated Bochner. The Ricci-energy
monotonicity is the inherited conformal Chern--Weil argument, not a new
curvature identity.

The corresponding maximum-norm Ricci assertion is false. On one fixed
product of closed hyperbolic surfaces there are Kähler input metrics with

\[
\delta_-(g_L)\longrightarrow0,
\qquad
\delta_-(\widehat g_L)\longrightarrow\infty.
\]

The inputs have bounded sectional curvature and diameter, a uniformly
positive injectivity radius and scalar spectral gap, and converge in every
fixed \(C^{1,\alpha}\), \(\alpha<1\), to an Einstein product. A logarithmic
Hessian concentration survives the actual scalar-normalizing equation.
This is a counterexample to that operation, not to Einstein existence:
the underlying product already carries an Einstein metric.

[Complete proof and explicit bump](line1_yamabe_endpoint.md).

## 2. Exact canonical supply does not force Kähler topology

The earlier closed shear metrics already had bounded curvature, pointwise
Ricci error tending to zero, and closed constant-norm harmonic forms. Those
facts are not counted again as new results.

For the identity-mapping-class, balanced-profile specialization, the added
calculation gives the exact cohomology identity

\[
[\Omega_\ell]=-2\pi c_1(TM,J_\ell).
\]

An auxiliary Euler connection has one correction term
\(a_\ell'z'\,dt\wedge\beta\). Its integral across the collar vanishes
by odd/even parity, so it has a global compactly supported primitive.
Moser's theorem then puts the entire family on one fixed symplectic form
\(\omega\), not merely on a fixed smooth manifold.

For the pulled-back metrics \(q_\ell\), with \(T=2\chi+3\tau>0\),

\[
|\omega|^2=2,\quad d\omega=0,\quad\Delta_H\omega=0,
\quad p=(c_1^+)^2=c_1^2=T,
\]
\[
\|\operatorname{Ric}_{q_\ell}+q_\ell\|_\infty
+\|W^+_{q_\ell}-A_{\omega,1/2}\|_\infty=O(\ell),
\qquad D_{\rm LB}=\Theta(\ell^3),
\]

where \(A_{\omega,1/2}=(|\omega|^2I/3-\omega\otimes\omega)/2\).
The manifold has no Kähler finite cover, by the inherited group-theoretic
proof. This specialization belongs to the earlier Dehn-twist surface-bundle
family; it is not a newly discovered smooth topology.

Thus actual canonical-class supply, zero anti-self-dual canonical period,
zero Hodge source, and pointwise Weyl/Einstein calibration still do not
force a Kähler structure. The fixed relative integer shear flux survives
while its curvature cost is multiplied by the shrinking circle radius.

[Complete Euler-class and fixed-form proof](line1_canonical_shear.md).

There is a useful precise comparison with the classical exact result:
Apostolov--Armstrong--Drăghici prove that a compact almost-Kähler
four-manifold with **exactly** \(J\)-invariant Ricci tensor and with its
fundamental form **exactly** a Weyl eigenform is Kähler
([Theorem 2 and the equivalent curvature conditions](https://arxiv.org/pdf/math/0109098)).
The shear family has both curvature errors tending to zero, but not equal
to zero. It shows why that exact theorem cannot simply be replaced by a
uniform small-error theorem in this degenerating class.

## 3. What this changes in the first research line

The integral gap works at a forbidden curvature calibration. The present
shear family lies at the allowed negative root \(t=1/2\), where the
Round-21 spectral left side is zero. Better supply at this allowed root
cannot by itself turn the result into a topological Kähler theorem.

Likewise, scalar normalization legitimately improves the integral
Einstein defect, but is not a way to carry the Yau26 maximum-norm input
through a change of metric. The new counterexample does not invalidate
earlier scalar repairs for families with the stronger uniform local
derivative estimates actually used in their proofs.

The remaining global question is exact and unchanged: does the fixed
shear manifold admit a genuinely non-Kähler negative Einstein metric?
The current results neither exclude nor construct such a metric. They do
determine that two proposed universal shortcuts to that decision are false.

## 4. Evidence and inheritance

- The Yamabe paper contains the universal estimate and the full nonlinear
  counterexample proof, including the fixed-background implicit-function
  argument. Its elementary Laplacian/Hessian mechanism is classical; no
  priority claim is made for the realization here.
- The shear paper distinguishes its new balanced canonical identity and
  fixed-symplectic-form conclusion from Rounds 11--15's construction,
  topology, harmonic forms, and product-curvature estimates.
- The core bundle-Hessian lemma was independently rederived by commuting
  derivatives on a bundle-valued one-form; it introduces no derivative of
  connection curvature and no Sobolev constant. This is verification of
  an inherited lemma, not a third new theorem.
- Both new manuscripts have independent proof reviews and executable
  finite checks. [Verification record](line1_structure_verification.md)
  separates those checks from the analytic and topological arguments.

The local research snapshot retains the previous proofs, uploaded sources,
and Skill snapshot. No live system, Session, or installed Skill is changed.

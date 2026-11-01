# Step 103 — independent reading of the realized Wahl sector, cone isotropy, and the known-construction barrier

Session S1003A02, Agent4, Execute.  Main object: `step102_wahl_orbifold_realization_and_K2_invariance.md`.
Primary embedding source: Park–Park–Shin, Corollary 4.3, Proposition 4.4 and Proposition 5.1, in
`staging/acquired/1508_03724__Smoothly_embedded_rational_homology_balls_c10bca9ef1ed278c/content.md`,
\cite{parksmoothly}.  Comparison sources read for the construction assessment:
Fine–Premoselli, `Knowledge/objects/papers/1802.00608-Examples-of-compact-Einstein-four-manifolds-with-negative-cur--0cf90b17bddb--6ee68cdf69a3/object.md`, and
`Knowledge/objects/papers/Negatively-curved-Einstein-metrics-on-Gromov-Thurston-manifolds--a10264adf1d6--f7e1951c4aff/object.md`.
A01's independent isotropy computation is in `Sessions/S1003A01/workspace/scripts/step89_wahl_isotropy.py` and
`Sessions/S1003A01/workspace/data/step89/wahl_isotropy.json`.

## 1. Independent reading of Theorem 102.R

### 1.1 Embeddings and orientation

PPS proves:

* `Cor. 4.3`: \(B_{n,1}\subset V_{-(n+1)}\) for every \(n\ge2\);
* `Prop. 4.4`: \(B_{n,1}\subset V_{-4}\) for odd \(n\ge3\), and
  \(B_{n,1}\subset B_{2,1}\#\overline{\mathbb{CP}}^2\) for even \(n\ge3\).

Tubing four disjoint exceptional spheres in \(\#_4\overline{\mathbb{CP}}^2\) gives an oriented embedded sphere in
class \(E_1+E_2+E_3+E_4\), of square \(-4\); tubing three gives a \(-3\)-sphere.  The normal Euler number is negative in
M's complex orientation, so its regular neighbourhood is the oriented disk bundle \(V_{-4}\) (or \(V_{-3}\)).  PPS first
constructs its embedding in a complex surface model and then uses smooth local triviality of the family; the Milnor fibre
and the neighbourhood therefore carry the complex orientations used for the Wahl singularity and Şuvaina's \(d=1\)
Kähler Ricci-flat filler.  This is exactly the orientation needed by Lemma 86.S.  For even \(n\), Cor. 4.3 at \(n=2\)
gives \(B_{2,1}\subset V_{-3}\), and the fourth reversed projective-plane summand gives the ambient
\(B_{2,1}\#\overline{\mathbb{CP}}^2\) required by PPS 4.4.  Thus the block cost \(\kappa(2)=3\),
\(\kappa(n)=4\) for \(n\ge3\), is correct.

### 1.2 Coning, fundamental group, and rational blow-up

The embedded balls lie in simply connected exceptional-summand blocks, so \(\pi_1(B_{n,1})\to\pi_1(M)\) is trivial.
Since \(\pi_1(\partial B_{n,1})\to\pi_1(B_{n,1})=\mathbb Z_n\) is onto, van Kampen gives the same quotient
\(\pi_1(W)/\langle\!\langle\pi_1\partial B\rangle\!\rangle\) after gluing the rational ball or the cone.  Hence the
ordinary fundamental group of the coned underlying space is \(\pi_1(V)=\pi_1(M)=\pi_1(X)\).  This is not a computation
of the orbifold fundamental group: the latter retains local isotropy and surjects onto the ordinary group after killing
local groups.  Statements about a locally symmetric orbifold must use its orbifold lattice, while the degree-one map and
ordinary group still identify the host quotient.

PPS Proposition 5.1 gives the needed rational blow-up statement directly: replacing its embedded \(B_{p,q}\) by the
minimal-resolution plumbing gives the neighbourhood obtained by the explicit blow-ups used in the construction.  For
\(B_{n,1}\) this adds the \(n-1\) vertices of \([n+2,2,\ldots,2]\).  Blockwise gluing therefore yields
\[
 \widetilde V\cong X\#\bigl(k+\sum_j(n_j-1)\bigr)\overline{\mathbb{CP}}^2.
\]
This is stronger and cleaner than relying only on the informal flip sentence in Step 102.  The degree-one map follows
because the usual pinch is constant on the exceptional-summand blocks, hence descends after coning.

**Reading result.**  Theorem 102.R stands.  Its orientation, \(\pi_1\), degree-one-map and resolution assertions are
supported by the source, with the ordinary/orbifold fundamental-group distinction made explicit above.

## 2. Independent reading of Proposition 102.K

For a complex-oriented Wahl point \(1/n^2(1,n-1)\), the identity
\[
 s(n-1,n^2)=\frac{n^2-1}{6n^2}
\]
gives
\[
 \Delta\chi_{\rm orb}=-(1-n^{-2}),\qquad
 \Delta\tau_{\rm orb}=\frac23(1-n^{-2}).
\]
The sign is also forced by the orientation-matched scalar-flat Kähler filler: its \(+\)-charge is zero.  Therefore
\(2\chi_{\rm orb}+3\tau_{\rm orb}=A-k\), while the minus combination drops by
\(4(1-n^{-2})\).  The defect sign and the \(K^2\)-invariance statement are correct.

Resolving an arbitrary orbifold metric by Şuvaina's \(d=1\) scalar-flat Kähler ALE fillers transfers both LeBrun
inequalities because the filler has \(s=W^+=0\) in the selected orientation and 86.S controls the cutoff.  For an Einstein
orbifold, Cauchy–Schwarz in the mixed inequality gives exactly the supporting-edge equation used in Step 102.  Its maximum
forces \(k\le A/3\), and the smaller root gives
\[
 D\ge4\pi^2k+\frac{8\pi^2A}{9}
 \bigl(1-\sqrt{1-3k/A}\bigr)^2.
\]
The \(W^-\)-side is weaker by the stated Wahl correction and is slack for the realized block range because
\(4\sum(1-n_j^{-2})<4t\le k\).  Finally, a negative Kähler–Einstein orbifold would satisfy
\(\int s^2=32\pi^2(2\chi_{\rm orb}+3\tau_{\rm orb})=32\pi^2(A-k)\), contradicting the transferred
\(\int(s^-)^2\ge32\pi^2A\).  Proposition 102.K(a)–(c) stands.

Part (d) contains two different assertions.  The cohomology exact sequence
\[
 0\longrightarrow H^2(M)\longrightarrow H^2(W)
 \longrightarrow\bigoplus_j\mathbb Z_{n_j}\longrightarrow0
\]
is the dual form of the already verified Wahl complement sequence, so it stands (up to the usual affine choice when it is
used for spin\(^c\) structures).  However, the asserted equality between orbifold SW invariants and those of the minimal
resolution for matching chain restrictions was not sourced.  Fintushel–Stern rational blowdown and monopole-L-space
replacement theorems concern selected extending structures and require hypotheses; they do not prove the blanket
orbifold–resolution correspondence stated there.  Accordingly, 102.K(d)'s SW paragraph is **conditional** and is not used
in (a)–(c) or in the class-blindness theorem.

## 3. Cone-isotropy lemma for an Einstein Wahl orbifold

**Lemma 103.I (Weyl degeneracy forced at a Wahl cone).**  Let \(p\) be an orbifold point of type
\(1/n^2(1,n-1)\), \(n\ge3\), with its complex orientation, and let \(g\) be any smooth orbifold Riemannian metric.  Then
both \(W^+_p\) and \(W^-_p\), regarded as trace-free symmetric endomorphisms of \(\Lambda^\pm_p\), have a repeated
eigenvalue.  More precisely, each local isotropy action fixes one real axis and rotates its orthogonal plane through an
angle different from \(0\) and \(\pi\); every invariant symmetric endomorphism is \(\operatorname{diag}(a,b,b)\) in that
axis-plane decomposition.

*Proof.*  In a uniformizing complex chart the generator is
\(\gamma=\operatorname{diag}(\zeta,\zeta^{n-1})\), \(\zeta^{n^2}=1\).  On \(\Lambda^+\), the Kähler form is fixed and
the real \((2,0)\)-plane is multiplied by \(\det_{\mathbb C}\gamma=\zeta^n\), a rotation of angle \(2\pi/n\).
On \(\Lambda^-\), the effective \(SU(2)\)-factor is the ratio of the two complex eigenvalues, hence rotates the
orthogonal plane through angle \(2\pi(n-2)/n^2\) (up to sign).  For \(n\ge3\), neither angle is \(0\) or \(\pi\)
modulo \(2\pi\).  Since orbifold curvature commutes with isotropy, the restriction of either symmetric Weyl block to the
rotated plane is scalar and there are no axis-plane cross terms.  Trace-freeness leaves eigenvalues \((-2b,b,b)\).
\(\square\)

This is a pointwise Kähler-type algebraic condition, not a local obstruction: invariant Einstein germs exist, and no
Einstein-operator kernel/cokernel calculation is warranted without a global candidate.  At \(n=2\), the \(-\)-angle is
zero, so the two-block conclusion fails exactly in the paired-\(A_1\) case.

A01's separate exact weight calculation strengthens the field-side local statement.  For the canonical complex-orbifold
spin\(^c\) structure twisted by the \(\mathbb Z_n\) character \(\chi^j\), \(\Phi(p)\) can be nonzero only for \(j=0,1\),
and \(\nabla\Phi(p)=0\) for every \(j\); any almost-Kähler form is \(\pm\omega_0\) at \(p\), and its torsion vanishes to
order at least two for \(n\ge3\).  These facts are recorded, not promoted to an obstruction.  Step 102 did not identify
which torsion coset carries a nonzero orbifold SW invariant, because the needed SW correspondence is precisely the
conditional part of 102.K(d).

## 4. Locally symmetric exclusion and the resulting existence question

**Corollary 103.L (the unconditional local-symmetry exclusions).**  On a realized
\(V_{X,\mathbf n,k}\) in the hard window, complex-hyperbolic/Kähler locally symmetric type is impossible.  Real-hyperbolic
type is impossible whenever \(\tau_{\rm orb}(V)\ne0\).

*Proof.*  Complex-hyperbolic type is Kähler in its complex orientation, contradicting 102.K(c); reversing orientation
changes the sign of its nonzero signature and cannot reproduce V's fixed oriented characteristic data except in a
separately checked sign case.  Real-hyperbolic type has \(W=0\), hence the orbifold signature integral is zero.  For a
ball-quotient host the actual signature is
\[
 \tau_{\rm orb}(V)=\frac A9-k+\frac23\sum_j(1-n_j^{-2}),
\]
not \(A/3-k+\cdots\).  Thus nonzero \(\tau_{\rm orb}\) excludes it. \(\square\)

The distinction matters.  Since \(A>3k\) does not force the displayed number to be positive, the blanket positivity
proposed in Spirit #117 used \(A/3\) where the signature of a ball quotient is \(A/9\).  For the first realized one-point
block \(k=4\), \(A\in9\mathbb Z\), \(A\ge18\), the signature is negative at \(A=18,27\) and positive for \(A\ge36\), so it
is nonzero in all these cases and real-hyperbolic type is still excluded.  With several points, however, exact cancellation
\[
 \frac A9-k+\frac23\sum_j(1-n_j^{-2})=0
\]
is arithmetically possible in principle and has not been ruled out here.  A blanket `not locally symmetric' theorem in
that zero-signature subcase would need a correct orbifold-group rigidity argument: Step 102 computed only the ordinary
fundamental group, while a locally symmetric orbifold is classified by its orbifold lattice.  No such group argument is
silently assumed.

Thus any Einstein metric on V is non-Kähler; for \(n\ge3\) both Weyl blocks are Kähler-type at the cone; and whenever
\(\tau_{\rm orb}\ne0\) it is not real hyperbolic.  This is the exact cheap conclusion.

## 5. Why the known non-Kähler construction mechanisms do not enter this family

This is a bounded route assessment, not a nonexistence theorem.

1. **Fine–Premoselli / Gromov–Thurston ramified covers.**  Their input is a real-hyperbolic manifold containing a
null-homologous totally geodesic codimension-two submanifold with very large normal injectivity radius.  Their approximate
metric is a branched-cover smoothing of a real-hyperbolic metric, with error on a distant annulus and a uniformly
invertible Einstein operator.  V instead is made by coning a rational ball inside exceptional connected-sum blocks of a
complex-hyperbolic host.  It is not a cyclic branched cover, has isolated cyclic singularities rather than a smooth
codimension-two branch locus, and supplies neither an exact real-hyperbolic exterior nor the large-radius parameter that
makes the inverse-function theorem close.  The construction therefore has no entry datum on V.

2. **Anderson–Bamler generalized Dehn filling.**  Their input is a finite-volume real-hyperbolic manifold with toral
cusps, replaced by long toral black-hole pieces.  The output contains incompressible \(T^{n-2}\) core groups.  The Wahl
operation has a spherical lens-space link, a finite cyclic local group, and no long cusp or Dehn-slope parameter; its
ordinary fundamental group remains that of the compact ball quotient.  Thus there is no toral cusp to fill and no
analytic degeneration parameter of the required kind.

3. **Kähler–Einstein / cscK smoothing.**  Proposition 102.K(c) excludes the endpoint before deformation theory begins.
There is no Kähler comparison metric on V, so the Biquard–Rollin/cscK branch and A01's nodal calibration cannot seed an
Einstein perturbation here.

These failures do not prove nonexistence.  They say that the realized Wahl family requires a genuinely new global
non-Kähler Einstein mechanism, or a class-sensitive obstruction that uses more than curvature integrals.  The local cone
itself supplies no obstruction.

## 6. Corrected status of the centre

For \(0<k<A/3\), the nonattained-zero alternative now has three distinct subchannels.

1. **Wahl / negative Einstein orbifold.**  The family 102.R is geometrically realized.  All aggregate curvature methods
are blind by 102.K(a)–(c).  Existence is open.  Any metric would be non-Kähler and satisfy Lemma 103.I; real-hyperbolic type is excluded whenever \(\tau_{\rm orb}\ne0\), and the known construction mechanisms above do not apply.
2. **\(D_{\ge6}\) prism complement.**  96.K gives necessary filler/rank data only.  No compatible compact complement or
negative Einstein orbifold is constructed.
3. **Einstein cusp domain or exceptional-class-carrying collapse.**  These remain admissible in the conditional
Anderson picture but are undeveloped; no realizing sequence is known.

The smooth alternatives remain positive gap versus a smooth negative Einstein metric.  The actual mathematical centre is
therefore still open; the Wahl advance isolates a concrete existence problem rather than solving the trichotomy.

# TTCS Independent Branch Record

```json
{
  "step_id": 94,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 2,
  "status": "complete",
  "usable": true,
  "partial": false,
  "failure_kind": "",
  "error": "",
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step93_wfl_theorem_removability_index_transfer_and_wahl_self_similarity.md",
    "Sessions/S1003A01/trace/ttcs/results/step93_ttcs01_verifier1_integration.md",
    "Sessions/S1003A01/workspace/notes/step89_endpoint_jet_stabilizer_and_derivative_ladder.md",
    "Sessions/S1003A01/workspace/notes/step90_review_and_tn_projected_charge5.md"
  ]
}
```

## Task

Seek a genuinely point-sensitive use of the *marked* Wahl spin^c character, not merely scalar undersaturation. Given an exact negative Einstein orbifold metric, an actual irreducible SW solution with a forced order-at-least-two zero at p, and W+(p)=mu diag(2,-1,-1), investigate whether the character fixes a nonzero boundary/relative invariant on small lens-space links (Dirac eta, Chern–Simons, normalized spinor map degree, relative Euler/Chern current, stress-energy flux, or Pohozaev residue) that must be transported into W+ or trace-free Ricci energy. Determine carefully which candidate invariants vanish as the link shrinks, can migrate into a Ricci-flat bubble, or are already exactly contained in APS/index/Chern–Weil data transferred in Step 93. If one survives, derive its formula and how it enters an Einstein incompatibility; if none survives with present information, isolate the first missing differential datum. Use the exact character/index and removability results in the files; do not infer obstruction from the forced zero alone.

## Output

# Marked Wahl characters and shrinking-link residues

Let
\[
\Gamma=\mathbb Z_{N},\qquad N=n^{2},\qquad
\gamma(z_{1},z_{2})=(\zeta z_{1},\zeta^{\,n-1}z_{2}),
\]
and write an extendible spin\(^c\) twist as
\[
m=nj\in \mathbb Z_{N}.
\]
Relative to the canonical complex lift, the two \(S^{+}\)-weights are
\[
(m,m-n)=(nj,n(j-1)),
\]
and the determinant weight is
\[
d_j=2m-n=n(2j-1).
\]
The forced cases have \(j\notin\{0,1\}\).

The removability theorem gives a genuinely smooth \(\Gamma\)-equivariant pair on the uniformizing ball. In geodesic and radial gauges,
\[
g_{ab}=\delta_{ab}+O(r^{2}),\qquad
A|_{S_r}=A_m^{\rm flat}+O(r^{2}).
\]
Strong unique continuation and the forced value and first-jet vanishing give a finite expansion
\[
\Phi(r,\theta)=r^\ell\phi_\ell(\theta)+O(r^{\ell+1}),
\qquad \ell\ge2,
\]
where
\[
D_{S^{3}}\phi_\ell=-\Bigl(\ell+\frac32\Bigr)\phi_\ell
\]
and \(\phi_\ell\) belongs to the \(m\)-equivariant spherical mode. Also
\[
F_A^+=q(\Phi)=O(r^{2\ell}).
\]

## 1. Dirac eta: the marked extendible characters have identical values

Let \(\bar\eta_m\) denote the reduced eta invariant of the round lens-space Dirac operator with twist \(m\). The exact Step-93 formula gives
\[
\delta(m)=\delta(0)\quad\Longleftrightarrow\quad m\in n\mathbb Z/N\mathbb Z.
\]
Since the round link Dirac operators are invertible, APS on the positive-scalar-curvature cone cap yields
\[
\boxed{\bar\eta_m=\bar\eta_0\qquad(m=nj).}
\]
Equivalently, the Dirac rho invariant of every extendible character relative to the canonical lift is zero.

For the actual small link, the rescaled metric tends to the round metric and the connection tends to \(A_m^{\rm flat}\). Thus
\[
\bar\eta(D_{S_r/\Gamma,A})-\bar\eta_m=o(1).
\]
Its curvature-sensitive correction is the usual local APS transgression and tends to zero. Along a collapsing geometric sequence it may become an APS contribution of an ALE bubble, but it is then the same index information already transferred by Lemma 93.I.

Hence Dirac eta contains no distinction among the forced extendible characters.

## 2. Abelian Chern–Simons: the extendible subgroup is isotropic

Put \(q=n-1\), so
\[
q^{-1}\equiv-(n+1)\pmod N.
\]
The lens-space linking pairing has the form
\[
\ell(k,l)=\frac{q^{-1}kl}{N}\pmod{\mathbb Z}.
\]
For two extendible characters,
\[
\ell(nj,nk)=q^{-1}jk=0\pmod{\mathbb Z}.
\]
Thus
\[
n\mathbb Z/N\mathbb Z
\]
is an isotropic subgroup of order \(n\). This is precisely the subgroup realized by flat torsion lines over the Wahl rational ball.

For the determinant characters,
\[
\frac{q^{-1}(d_j^{2}-d_0^{2})}{N}
=4q^{-1}j(j-1)\in\mathbb Z.
\]
Even the spin\(^c\) quadratic normalization sees no difference, since
\[
\frac{q^{-1}(d_j^{2}-d_0^{2})}{8N}
=\frac{q^{-1}j(j-1)}2\in\mathbb Z.
\]
This agrees with the identical Dirac eta values.

Therefore every natural relative abelian Chern–Simons invariant of the marked twist is zero modulo its integral ambiguity. The common absolute value is representable by a flat connection and costs no \(L^{2}\) curvature.

## 3. Normalized spinor degree and the relative \(c_{2}\) class

Suppose first that \(p\) is isolated in the zero set, so that
\[
\widehat\Phi_r=\frac{\Phi}{|\Phi|}:S^{3}\longrightarrow S(S^+)
\]
is defined for all sufficiently small \(r\). Let \(d_p\) be its ordinary equivariant degree upstairs.

The tangent representation has equivariant Euler class
\[
e(T_0B)=q\,u^{2}\in H^{4}(B\Gamma;\mathbb Z)\cong\mathbb Z_N,
\]
while the positive-spinor representation has
\[
e(S^+_0)=m(m-n)u^{2}.
\]
Equivariant degree gives
\[
d_p\,q\equiv m(m-n)\pmod N.
\]
For \(m=nj\),
\[
m(m-n)=n^{2}j(j-1)=0\pmod N,
\]
and hence
\[
\boxed{d_p\equiv0\pmod{n^{2}}.}
\]
Thus the orbifold local index \(d_p/n^{2}\), when defined, is an integer. The marked character fixes no nonzero fractional Euler residue.

The same calculation appears directly in the local Chern class:
\[
c_2^\Gamma(S^+)=m(m-n)u^{2}=0\in H^{4}(B\Gamma;\mathbb Z).
\]
Globally, for the supplied expected-dimension-zero structures,
\[
\int_Vc_2(S^+)
=\frac14\left(a^{2}-T_+^{\rm orb}\right)=0,
\]
because both terms equal \(A-k\). This is already part of the transferred \(+\)-chirality characteristic package.

Several further facts prevent an integer local degree from producing an Einstein contradiction:

* The forced zero need not be isolated. If its nodal set meets every small link, no normalized map degree exists.
* Even for an isolated zero, an isolated zero of a smooth map \(\mathbb R^{4}\to\mathbb R^{4}\) may have degree zero.
* The Dirac equation does not impose one sign on local degrees. With the Euclidean quaternionic Dirac convention,
  \[
  P_+(x)=3x_0+i x_1+jx_2+kx_3,\qquad
  P_-(x)=x_0+i x_1+jx_2-kx_3
  \]
  are linear monogenic maps of degrees \(+1\) and \(-1\), respectively.
* The degree controls a scale-invariant \(W^{1,3}\) quantity of \(\widehat\Phi\), or a critical \(W^{1,4}\) quantity on annuli. The Seiberg–Witten estimates control \(\nabla\Phi\), not \(\nabla\widehat\Phi\). Since \(\Phi=O(r^\ell)\),
  \[
  \int_{B_r}|\nabla\Phi|^{2}=O(r^{2\ell+2}),
  \]
  so an angular degree is energetically inexpensive in the available norm.

Consequently a normalized-spinor degree can survive as an unspecified integer, but it is neither fixed by the character nor coupled to \(W^+\)-energy by the present equations.

## 4. Gravitational eta and the algebra of \(W^+(p)\)

The signature defect
\[
\frac23\left(1-\frac1{n^{2}}\right)
\]
does survive on the lens link. It is independent of the spin\(^c\) character and is already included in the orbifold signature formula and in the altered \(T_-^{\rm orb}\).

The special value
\[
W^+(p)=\mu\,\mathrm{diag}(2,-1,-1)
\]
does not create an additional shrinking-link residue. Indeed,
\[
\int_{B_r/\Gamma}|W^+|^{2}
=\frac{3\pi^{2}}{n^{2}}\mu^{2}r^{4}+o(r^{4})
\]
with the usual endomorphism norm. The rescaled link metric differs from the round quotient by \(O(r^{2})\), so every curvature-sensitive eta or gravitational Chern–Simons correction tends to zero.

At the point itself,
\[
F_A^+(p)=q(\Phi(p))=0.
\]
Thus there is no field value selecting the \(\omega_0\)-eigenline of \(W^+(p)\). Moreover,
\[
[\nabla_i,\nabla_j]\Phi(p)=\mathcal R_{ij}\Phi(p)=0,
\]
and differentiating once still gives zero because \(\nabla\Phi(p)=0\). The leading Hessian or higher homogeneous jet therefore sees the flat Dirac equation, not \(\mu\). Curvature first enters the spinor expansion two orders after the leading monogenic term. Polynomial right inverses for the flat Dirac operator, averaged over \(\Gamma\), solve the corresponding equivariant recursion, so no local resonance forces an algebraic relation between \(\mu\) and the marked character.

## 5. Stress-energy and Pohozaev fluxes vanish

For \(\ell\ge2\),
\[
|\Phi|=O(r^\ell),\qquad
|\nabla\Phi|=O(r^{\ell-1}),\qquad
F_A^+=O(r^{2\ell}).
\]
A standard radial Pohozaev integrand therefore obeys
\[
\int_{S_r/\Gamma}
T(\nu,r\partial_r)
=
O(r^{2\ell+2})+O(r^{4}),
\]
where the \(O(r^4)\) term covers smooth full curvature contributions. First-order Dirac currents vanish at least as rapidly.

This also follows conceptually from removability: the Dirac and curvature equations hold distributionally across the point, so no point-supported source remains for a divergence identity. A residue can be manufactured only by normalizing with powers of \(|\Phi|^{-1}\) or \(r^{-1}\); such a residue depends on the leading jet rather than on the original finite-energy fields.

There is also no Einstein–Seiberg–Witten stress coupling here. The monopole is an auxiliary field; its stress tensor is not the source of the Einstein equation. A conserved monopole flux therefore has no identity forcing trace-free Ricci curvature.

## 6. What can migrate into a Ricci-flat ALE bubble

The exact Wahl ALE model makes the migration mechanism explicit:

* Every extendible character is represented by a flat torsion determinant connection on the rational ball.
* The ALE APS Dirac index is zero and there are no \(L^{2}\) harmonic spinors in either chirality.
* The Ricci-flat Kähler metric has \(W^+=0\) in its complex orientation.
* The gravitational lens-space defect is carried by the opposite-chirality curvature and is already represented in \(T_-^{\rm orb}\).

Thus the marked holonomy, Dirac eta package, and gravitational defect can all reside on the ALE piece without abelian curvature energy or \(W^+\)-energy.

A rescaled monopole itself usually tends to zero under the natural SW scaling because the original spinor is bounded. Dividing additionally by its vanishing amplitude can produce a growing harmonic spinor or homogeneous monogenic polynomial on the bubble. Such a mode is not \(L^{2}\), so Lemma 93.I does not remove it. It can carry angular degree or frequency data without contributing a quantized SW energy.

## 7. The first genuinely new differential datum

The character determines the admissible equivariant spherical modes, but not the actual leading mode:
\[
\boxed{
\Phi=r^\ell\phi_\ell+O(r^{\ell+1}),\qquad
\ell\in\mathcal I_m,\quad
0\ne\phi_\ell\in E_{\ell,m}.
}
\]
Neither \(\ell\), the direction of \(\phi_\ell\), nor its amplitude relative to the global \(L^{4}\)-mass follows from the marked character.

Equivalently, the surviving local datum is the limiting Almgren frequency and normalized trace:
\[
N(0)=\ell,\qquad
\frac{\Phi|_{S_r}}
{\|\Phi\|_{L^2(S_r)}}\longrightarrow
\frac{\phi_\ell}{\|\phi_\ell\|_{2}}.
\]
A curvature-sensitive point mechanism would need a definite pairing of the form
\[
\mathcal Q_m(\phi_\ell;\mu,\lambda)
\]
appearing in an unrenormalized conserved flux. Standard stress and Pohozaev fluxes tend to zero; their renormalized coefficients are not topological and are not constant in \(r\).

For a metric-uniform integral consequence, this local datum must be accompanied by quantitative propagation from the global monopole mass to the marked point—equivalently, a uniform doubling estimate or a lower dimensionless regularity scale \(\lambda r_0^2\). Without that information the leading coefficient may be arbitrarily small at the marked point, while the required \(\int|\Phi|^4\) is carried elsewhere.

In summary: the marked Wahl character survives as flat holonomy and as a restriction on equivariant spinor modes. Its eta, abelian Chern–Simons, fractional Euler, and fractional normalized-degree residues all vanish relative to the canonical extendible lift; the gravitational residue is character-independent and already present in APS/Chern–Weil data. The remaining integer spinor degree and frequency data have no present transport law into \(W^+\) or trace-free Ricci energy.
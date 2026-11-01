# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 94,
  "task_field": "generator",
  "task_index": 2,
  "type": "Generator",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step94_ttcs01_sub3_generator.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step94_ttcs01_sub4_generator.md"
    }
  ]
}
```

## Exact Task

Seek a genuinely point-sensitive use of the *marked* Wahl spin^c character, not merely scalar undersaturation. Given an exact negative Einstein orbifold metric, an actual irreducible SW solution with a forced order-at-least-two zero at p, and W+(p)=mu diag(2,-1,-1), investigate whether the character fixes a nonzero boundary/relative invariant on small lens-space links (Dirac eta, Chern–Simons, normalized spinor map degree, relative Euler/Chern current, stress-energy flux, or Pohozaev residue) that must be transported into W+ or trace-free Ricci energy. Determine carefully which candidate invariants vanish as the link shrinks, can migrate into a Ricci-flat bubble, or are already exactly contained in APS/index/Chern–Weil data transferred in Step 93. If one survives, derive its formula and how it enters an Einstein incompatibility; if none survives with present information, isolate the first missing differential datum. Use the exact character/index and removability results in the files; do not infer obstruction from the forced zero alone.

## Integrated Scientific Memo

# Marked Wahl characters: shrinking-link invariants and the missing differential information

## Conclusion

For the **marked, extendible** Wahl spin\(^c\) structures in Step 93, no candidate considered here gives a character-fixed, nonzero shrinking-link invariant that must be represented by \(W^+\) or trace-free Ricci energy.

This conclusion is stronger than saying that a forced zero is energetically small:

- the **relative Dirac rho invariant is exactly zero** for every extendible twist;
- the extendible torsion subgroup is **isotropic for the lens-space linking pairing**;
- an isolated spinor zero, if present, has **no character-forced fractional local Euler charge**;
- ordinary curvature, stress and Pohozaev fluxes vanish at the removable point;
- the marked flat holonomy is compatible with the explicit Ricci-flat Wahl filler, where \(W^+=0\).

An integer normalized-spinor degree may survive, but the character neither determines it nor supplies a transport law turning it into the desired curvature energy. The first unprovided differential datum is the **actual leading equivariant Dirac jet**, followed by quantitative control of its behavior at the Einstein regularity scale.

Two distinctions are essential:

1. The prescribed recovery-family transfer in Step 93 proves no loss of abelian field energy. It does **not** describe all bubbles of arbitrary degenerating Einstein metrics.
2. There is already an Euler/Chern transgression involving \(W^+\). What is missing is not that identity, but a character-fixed boundary value and a sign/coercivity mechanism for using it.

---

## 1. Local form supplied by removability and the marked lift

Set
\[
N=n^2,\qquad q=n-1,\qquad
\gamma(z_1,z_2)=(\zeta z_1,\zeta^qz_2).
\]
Relative to the canonical complex spin\(^c\) lift, an extendible twist is
\[
m=nj\in n\mathbb Z/N\mathbb Z.
\]
Its positive-spinor weights and determinant weight are
\[
(w_0,w_1)=(m,m-n),\qquad d_j=2m-n.
\]
For \(j\notin\{0,1\}\), both the value and first covariant jet of the spinor vanish. These conclusions concern the marked extendible family, not arbitrary orbifold twists.

The repaired Lemmas 93.R–93.Q extend the actual pair smoothly and equivariantly on the uniformizing ball, **without changing its character**. In normal coordinates and radial gauge,
\[
g_{ab}=\delta_{ab}+O(r^2),\qquad A-A_{\rm flat}=O(r)
\]
in physical components; after pullback to a fixed unit sphere, the connection difference is \(O(r^2)\).

Strong unique continuation for the smooth Dirac equation gives a finite first nonzero Taylor term for the irreducible solution:
\[
\Phi(x)=P_\ell(x)+O(r^{\ell+1}),\qquad
D_0P_\ell=0,\qquad \ell\ge2.
\]
Here \(P_\ell\) is a homogeneous, \(\Gamma\)-equivariant polynomial spinor. Equivalently,
\[
\Phi(r,\theta)=r^\ell\phi_\ell(\theta)+O(r^{\ell+1}),\qquad
D_{S^3}\phi_\ell=-\left(\ell+\frac32\right)\phi_\ell
\]
with the convention \(D=r^{-1}c(dr)(r\partial_r+\tfrac32+D_{S^3})\).

Consequently,
\[
|\nabla_A\Phi|=O(r^{\ell-1}),\qquad
F_A^+=q(\Phi)=O(r^{2\ell}).
\]
The full \(F_A\) is smooth; its anti-self-dual part need not vanish at \(p\).

The character fixes the admissible equivariant modes. It does not determine which admissible mode occurs, its amplitude, its nodal set, or its local degree.

---

## 2. Dirac eta: exact relative vanishing

Write \(\bar\eta_m=(\eta_m+h_m)/2\) for the reduced eta invariant of the round lens-space Dirac operator with the full marked spin\(^c\) lift. The boundary operator is invertible:
\[
h_m=0,\qquad |\nu|\ge\frac32.
\]

The exact all-\(n\) result in the Step-93 verifier is
\[
\delta(m)=\delta(0)
\quad\Longleftrightarrow\quad
m\in n\mathbb Z/N\mathbb Z,
\]
where
\[
\delta(m)=\frac1N\sum_{k=1}^{N-1}
\frac{\zeta^{km}}{(1-\zeta^{-k})(1-\zeta^{-qk})},
\qquad
\delta(0)=\frac{1-N^{-1}}{12}.
\]

To extract eta rather than merely quote an index identity, use the same positive-scalar-curvature orbifold cap for all twists. Its APS index is zero for every character. Flat twisting changes neither its ordinary Chern–Weil density nor its metric. Subtracting the orbifold APS formulas therefore gives
\[
\bar\eta_m-\bar\eta_0=\delta(m)-\delta(0)
\]
up to a common orientation convention. Thus
\[
\boxed{\bar\eta_{nj}-\bar\eta_0=0.}
\]

This is exact equality, not just equality modulo integers. The absolute eta value need not vanish, but it does not distinguish the forced characters from the canonical extendible lift.

For the actual small links \(L_r\), rescale their metrics to unit size. The metrics and connections converge to the round quotient and its marked flat connection; the spectral gap persists. Hence
\[
\bar\eta(D_{L_r,A})-\bar\eta_m\longrightarrow0,
\]
and smooth perturbation gives an \(O(r^2)\) estimate.

**Correction to a proposed flux formula.** Eta variation is not, without qualification, just the integral of a bounded four-dimensional density over the physical annulus. The APS formula also requires the appropriate collar/product correction or gravitational transgression. The limiting correction still vanishes, but an \(O(r^4)\) annular argument alone does not justify that conclusion.

The surviving absolute Dirac boundary term is precisely the APS/Kawasaki information already accounted for in Step 93.

---

## 3. Abelian Chern–Simons: flat holonomy without mandatory curvature

Up to orientation and generator conventions, the lens-space linking pairing is
\[
b(k,l)=\frac{q^{-1}kl}{N}\pmod{\mathbb Z},
\qquad q^{-1}\equiv-(n+1)\pmod N.
\]
For extendible twists,
\[
b(nj,nk)=q^{-1}jk=0\pmod{\mathbb Z}.
\]
Thus the subgroup \(n\mathbb Z/N\mathbb Z\), of order \(n\), is isotropic. This is the subgroup realized by torsion flat lines over \(B_{n,1}\).

The determinant characters also lie in this subgroup:
\[
d_j=n(2j-1).
\]
Their squared linking data do not distinguish them. For example,
\[
\frac{q^{-1}(d_j^2-d_0^2)}{N}
=4q^{-1}j(j-1)\in\mathbb Z.
\]
A quadratic refinement must be specified with its spin/spin\(^c\) marking; one cannot assign a universal factor \(1/2\) or \(1/8\) without that choice. The Dirac refinement relevant here is already controlled by the exact rho calculation above.

For the actual connection, write \(A=A_{\rm flat}+ia\). Its ordinary relative abelian transgression satisfies
\[
\int_{L_r}a\wedge da=O(r^4),
\]
and the corresponding local Chern–Weil integral obeys
\[
\int_{B_r/\Gamma}F_A\wedge F_A=O(r^4).
\]
Both vanish as \(r\to0\).

The full character nevertheless remains detectable as flat holonomy. That is genuine marked information, but it can exist with **zero curvature energy**. No obstruction follows merely from retaining this holonomy.

---

## 4. Normalized spinor degree: the fractional charge is zero

This candidate requires an extra hypothesis: the spinor must be nonzero on every sufficiently small link. Forced vanishing at \(p\) does not imply that its zero is isolated.

Assuming isolation, trivialize the positive-spinor bundle upstairs and define
\[
\widehat\Phi_r=\frac{\Phi}{|\Phi|}:S^3\longrightarrow S^3.
\]
Let its degree be \(D_p\). The equivariant degree congruence is
\[
D_p\,q\equiv m(m-n)\pmod N.
\]
One way to derive it is to compare the equivariant Euler classes of the source and target representations:
\[
e_\Gamma(T_0B)=q\,u^2,\qquad
c_2^\Gamma(S^+_0)=m(m-n)u^2,
\quad
H^4(B\Gamma;\mathbb Z)\cong\mathbb Z_N.
\]

For \(m=nj\),
\[
m(m-n)=N\,j(j-1)=0\quad\text{in }\mathbb Z_N,
\]
so
\[
\boxed{D_p\equiv0\pmod{n^2}.}
\]
The orbifold local index \(D_p/n^2\), when defined, is therefore an integer. The marked character forces **no nonzero fractional Euler residue**.

This resolves the apparent weight-quotient possibility. The expression
\[
\frac{w_0w_1}{u_1u_2}
=\frac{n^2j(j-1)}{n-1}
\]
is not the local multiplicity of the actual nonlinear, nontransverse SW spinor. Its applicable topological content is the congruence above, not a forced positive charge.

Neither the forced order nor the Dirac equation alone supplies positivity of local degrees. Even ordinary flat monogenic linear maps can have either degree sign. Nor does the available energy control the normalized map:
\[
\int_{B_r/\Gamma}|\nabla_A\Phi|^2
=O(r^{2\ell+2}),
\]
whereas \(\nabla(\Phi/|\Phi|)\) can have \(r^{-1}\) angular behavior. An integer degree is consequently cheap in the unnormalized \(H^1\) norm. This is the same distinction exposed by the rank-two example in Step 89.

### The Euler transgression exists, but does not give the desired inequality

The positive-spinor bundle already has the characteristic identity
\[
4c_2(S^+)=a^2-p_1(\Lambda^+).
\]
For the induced connections, its four-dimensional Chern–Weil density can be written, with the normalizations of Step 93, as
\[
c_2(S^+,\nabla_A)
=
\frac1{16\pi^2}
\left(
|F_A^+|^2-|F_A^-|^2
-2|W^+|^2-\frac{s^2}{24}
+\frac{|\mathring{\operatorname{Ric}}|^2}{2}
\right)dV.
\]
Thus an Euler/Chern current involving \(W^+\) is **not missing**.

An angular transgression determined by a nonzero boundary spinor satisfies, with consistent orientations,
\[
\operatorname{ind}_{B_r}(\Phi)
=
\int_{B_r}c_2(S^+,\nabla_A)
-\int_{L_r}\mathcal T(\widehat\Phi,\nabla_A).
\]
The bounded curvature integral tends to zero. A nonzero integer index is then retained by the angular transgression, whose coefficients involve normalization by \(|\Phi|\). It is not converted into a nonzero local curvature integral.

For the supplied expected-dimension-zero structures,
\[
\int_Vc_2(S^+)=\frac14(a^2-T_+^{\rm orb})=0.
\]
This total characteristic identity is already transferred. It does not force every local zero index to vanish, because neither zero indices nor the displayed curvature density have a suitable global positivity property.

Accordingly, the missing ingredient here is a **fixed boundary charge together with sign/coercivity**, not another formal Chern identity.

---

## 5. The special \(W^+(p)\) algebra does not create a residue

At the marked point,
\[
W^+(p)=\mu\,\operatorname{diag}(2,-1,-1),
\qquad F_A^+(p)=0.
\]
With the usual endomorphism norm,
\[
\int_{B_r/\Gamma}|W^+|^2
=
\frac{3\pi^2}{n^2}\mu^2r^4+o(r^4).
\]
There is no scale-independent local \(W^+\) mass.

The forced zero also postpones curvature detection by the spinor:
\[
[\nabla_i,\nabla_j]\Phi(p)=0,
\]
and its once-differentiated curvature terms vanish because \(\nabla_A\Phi(p)=0\). The leading jet therefore solves the flat Dirac equation and is not constrained by \(\mu\).

In normal coordinates and radial gauge, the first metric and connection corrections to \(D_0P_\ell\) have order \(r^{\ell+1}\). They enter the recursion for \(P_{\ell+2}\):
\[
D_0P_{\ell+2}
=
-\mathcal L_1(R(p),F_A(p))P_\ell,
\]
with possible free monogenic terms at intermediate orders. This is where a genuine curvature-sensitive pairing first becomes available. It involves the actual leading spinor mode and connection curvature, not just the character or the number \(\mu\).

The character-independent signature defect
\[
\tau_{\rm CW}-\tau_{\rm top}
=\frac23(1-n^{-2})
\]
does survive on the link. It is already part of the orbifold signature formula and the changed \(T_-^{\rm orb}\); it is not a new marked \(W^+\) charge.

---

## 6. Stress-energy and Pohozaev residues vanish

Let \(s=-\lambda\). The local integrated Weitzenböck identity is
\[
4\int_{B_r}|\nabla_A\Phi|^2
-\int_{B_r}U(\lambda-U)
=
4\int_{L_r}\operatorname{Re}
\langle\nabla_\nu\Phi,\Phi\rangle.
\]
The boundary term is
\[
O(r^{2\ell+2}),
\]
while
\[
\int_{B_r}U(\lambda-U)=O(r^{2\ell+4}).
\]
There is no point residue.

For a radial Pohozaev flux, contracting the stress tensor with \(r\partial_r\) supplies the additional radial factor. The spinor contribution is \(O(r^{2\ell+2})\); smooth full-curvature contributions are at most \(O(r^4)\). Fluxes with a unit radial vector instead also vanish, with one fewer power of \(r\).

These estimates are consistent with the distributional removability proof: neither the curvature equation nor the Dirac equation leaves a point-supported source. A residue obtained by dividing by powers of \(r\) or \(|\Phi|\) is a **renormalized jet invariant**, not an unrenormalized conserved flux.

Moreover, the monopole is an auxiliary solution on an Einstein background. Its stress tensor is not the source of the Einstein equation. A stress identity therefore cannot be interpreted as an automatic payment in trace-free Ricci energy.

---

## 7. What the Wahl bubble can carry—and what is not established

The explicit Step-93 ALE filler demonstrates that the following coexist:

- every extendible marked spin\(^c\) structure;
- a flat determinant connection;
- zero APS Dirac index and no \(L^2\) harmonic spinors;
- \(s=0\), \(W^+=0\), and \(\mathring{\operatorname{Ric}}=0\);
- nontrivial opposite-chirality geometric curvature accounting for the gravitational topology.

Thus flat marked holonomy and the transferred index/signature data do not require the desired energy payment.

Under the natural SW blow-up scaling
\[
\widetilde g=\varepsilon^{-2}g,\qquad
\widetilde\Phi=\varepsilon\Phi,
\]
a bounded spinor tends to zero on a bubble. Further division by its vanishing amplitude may expose a non-\(L^2\) harmonic mode. The absence of \(L^2\) Dirac kernels does not exclude such a normalized mode or its angular information.

Two stronger assertions are **not justified**:

- The existence of this filler does not construct an Einstein degeneration carrying the specified nonzero outer monopole.
- An arbitrary integer degree of a positive-spinor zero cannot simply be declared to migrate into \(W^-\). For a flat determinant on the Ricci-flat Kähler filler, the displayed \(c_2(S^+)\) curvature density is zero. Transport of an integer degree would require boundary-section matching, zeros, or relative transgression data.

For the prescribed recovery metrics, WFL proves that abelian curvature and spinor gradient energy do not concentrate in the filler. For arbitrary Einstein bubble trees, the marked field-matching problem remains unresolved.

---

## 8. The first missing differential datum and its quantitative consequence

The minimal new local object is
\[
\boxed{
(\ell,P_\ell),\qquad
0\ne P_\ell\in
\ker D_0\cap
\operatorname{Hom}_\Gamma(\operatorname{Sym}^{\ell}T_0B,S^+_0).
}
\]
A first curvature-sensitive calculation must then determine the projected \(P_{\ell+2}\) equation and any pairing it produces with \(W^+(p)\), \(s\), and \(F_A(p)\). Character data alone do not determine this pairing.

For a uniform Einstein-gap estimate, even that jet information is insufficient without a scale estimate. If a uniformizer ball of radius \(r_0\) has controlled rescaled metric and coupled elliptic coefficients, with \(\lambda r_0^2\) bounded, the maximum bound \(|\Phi|\le\sqrt\lambda\) and double zero give
\[
|\Phi(x)|\le C\sqrt\lambda\left(\frac{r}{r_0}\right)^2.
\]
On a fixed smaller fraction of the ball, \(U\le\lambda/2\), and therefore
\[
\boxed{
\int_{B_{cr_0}/\Gamma}(\lambda^2-U^2)
\ge c'\frac{\lambda^2r_0^4}{n^2}.
}
\]
This estimate needs no lower bound on the leading coefficient. Its unresolved geometric input is a lower bound for the dimensionless coupled regularity scale \(\lambda r_0^2\), or an analysis of what replaces this payment when that scale collapses.

The forced-subfamily selection from the Step-93 verifier retains
\[
\int U^2\ge32\pi^2A.
\]
Thus class selection is not the obstacle. For each fixed metric, the forced zero already yields strict scalar undersaturation; no uniform excess follows.

**Precise remaining problem.** Determine whether an actual marked Einstein degeneration can shrink the coupled regularity scale to zero while matching the outer leading Dirac mode through Ricci-flat bubbles at vanishing global defect. A positive resolution requires a signed relative transport identity or quantitative scale control. A negative resolution requires an actual compatible degeneration, not merely a flat filler or an equivariant jet.

The supplied material settles the fractional/topological link accounting. The unresolved information is differential: the leading mode, its curvature-sensitive continuation, and its matching across a collapsing geometric scale.
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

The marked Wahl character is genuinely point-sensitive at the level of jets, but the removability result converts the punctured-cone problem into an orbifold-smooth one. Because of that, every candidate link invariant has to be separated into two kinds of information:

1. a flat/topological character phase already present on the cone or on the Wahl filler;  
2. an actual curvature/stress flux that could be transported into \(W^+\) or trace-free Ricci energy.

With the Step-93 removability, index transfer, and exact Kawasaki identities in force, the second kind does not yet appear. The first kind is already contained in the transferred APS/index/Chern–Weil package or can be carried by a Ricci-flat ALE bubble with \(W^+=0\) and trace-free Ricci zero.

Below is a detailed local accounting.

---

## 1. Local analytic form of the marked character

Use a uniformizer with complex coordinates \((z_1,z_2)\) in which
\[
\Gamma=\frac1{n^2}(1,n-1),\qquad
\gamma\cdot(z_1,z_2)=(\zeta z_1,\zeta^{\,n-1}z_2),\quad
\zeta=e^{2\pi i/n^2}.
\]
For the marked extendible spin\(^c\) twist
\[
m=nj\in n\mathbb Z/n^2\mathbb Z,
\]
the two positive-spinor weights are
\[
w_0=nj,\qquad w_1=n(j-1).
\]
For \(j=0\) the value component in \(\Lambda^{0,0}\) is invariant; for \(j=1\) the value component in \(\Lambda^{0,2}\) is invariant. For \(j\notin\{0,1\}\) there is no invariant value and no invariant first jet. Hence a smooth equivariant spinor has
\[
\Phi=O(r^{d_j}),\qquad d_j\ge2,
\]
and the actual vanishing order \(d(\Phi)\) is at least \(d_j\). More intrinsically,
\[
d_j=\min\{d\ge0:\operatorname{Hom}_\Gamma(\operatorname{Sym}^dT^*_0,W^+_{\chi_j})\neq0\}.
\]
The character therefore fixes the first allowed isotypic jet space, not a fixed nonzero coefficient.

Because the abelian pair is orbifold-smooth by Lemma 93.R and Lemma 93.Q,
\[
F_A\in L^2,\qquad \Phi\in L^\infty,\qquad
F_A^+=q(\Phi)=O(r^{2d(\Phi)}),
\]
and the determinant connection has no point-supported curvature source. The local Einstein curvature is also bounded in the orbifold uniformizer; the algebra
\[
W^+(p)=\mu\operatorname{diag}(2,-1,-1)
\]
means only that the invariant self-dual direction at \(p\) is the cone Kähler direction. It does not by itself create a singular flux.

The basic scaling consequence is:
\[
|\Phi|=O(r^d),\qquad |\nabla_A\Phi|=O(r^{d-1}),\qquad
|F_A^+|=O(r^{2d}),\qquad d\ge2.
\]
Any link flux built polynomially from \(\Phi,\nabla_A\Phi,F_A\) and bounded curvature therefore tends to zero with a positive power of \(r\). This already removes many possible residues.

---

## 2. Dirac eta and APS link contributions

Let \(L_r\) be the small lens-space link around \(p\), equipped with the rescaled metric \(r^{-2}g|_{L_r}\), and let \(D_{r,\chi_j}\) be the spin\(^c\) Dirac operator on \(L_r\) with the marked flat twist \(\chi_j\). As \(r\to0\), the rescaled link metrics converge to the round spherical space form and the determinant connection converges to the flat connection of character \(\chi_j\). The round twisted link Dirac operator satisfies the Friedrich gap
\[
|\mu|\ge \frac32,
\]
so it is invertible. Therefore for sufficiently small \(r\),
\[
\ker D_{r,\chi_j}=0,
\]
and the eta invariant varies smoothly:
\[
\eta(D_{r,\chi_j})=\eta_{\mathrm{round}}(\chi_j)+O(r^2).
\]

The APS contribution of the excised cone is, up to the standard sign convention,
\[
-\frac12\bigl(\eta(D_{r,\chi_j})+h(D_{r,\chi_j})\bigr),
\]
and \(h=0\) for small \(r\). The local Kawasaki term \(\delta(m)\) is exactly the singular APS/index contribution associated with this link operator. Step 93 gives the exact all-\(n\) identity
\[
\delta(m)=\delta(0)
\quad\Longleftrightarrow\quad
m\in n\mathbb Z/n^2\mathbb Z.
\]
Thus every extendible marked character has the same local Dirac-index contribution as the untwisted extendible structure.

The radius variation of eta is also harmless. Since the rescaled link family is smooth and invertible,
\[
\eta(D_{r',\chi_j})-\eta(D_{r,\chi_j})
=
\int_{A_{r,r'}} \widehat A(R)\operatorname{ch}(F_A)
+
\text{spectral-flow term},
\]
and the spectral-flow term is absent for sufficiently small links. The integrand is bounded, so the annular integral is \(O(|r'^4-r^4|)\to0\). No \(r\)-independent flux into \(W^+\) or trace-free Ricci arises.

Conclusion: the Dirac eta/APS link invariant is already exactly contained in the Step-93 index transfer and Kawasaki computation. It does not produce a new point-sensitive Einstein obstruction.

---

## 3. Determinant Chern–Simons and relative Chern current

Choose a flat reference connection \(A_{\chi_j}\) on \(L_r\) representing the marked character. Write
\[
A=A_{\chi_j}+a.
\]
Orbifold smoothness and \(F_A\in L^2\) allow a gauge in which \(a=O(r)\) on \(L_r\). The relative \(U(1)\) Chern–Simons functional is
\[
\operatorname{CS}(A,A_{\chi_j};L_r)
=
\int_{L_r} a\wedge F_A,
\]
because \(F_{\chi_j}=0\). Pointwise,
\[
|a\wedge F_A|=O(r),
\]
and \(\operatorname{vol}(L_r)=O(r^3)\), hence
\[
\operatorname{CS}(A,A_{\chi_j};L_r)=O(r^4)\to0.
\]
Equivalently,
\[
\int_{B_r}F_A\wedge F_A\to0
\]
because \(F_A\in L^2\).

The absolute Chern–Simons invariant of the flat connection \(A_{\chi_j}\) can be nonzero as a torsion phase, but it exists with zero curvature and zero spinor energy. It is a flat character datum, not a curvature flux. It is precisely the kind of datum matched by the rational-ball filler and by the extendibility condition \(m\in n\mathbb Z/n^2\mathbb Z\). It does not force \(W^+\) energy or trace-free Ricci energy.

Conclusion: the determinant Chern–Simons/relative Chern current either vanishes in the shrinking-link limit or is a flat torsion phase already accounted for by extendibility and filler gluing.

---

## 4. Normalized spinor degree and relative Euler current

This is the only candidate with genuine point-sensitive potential.

If \(\Phi\) is nonzero on \(L_r\), one may normalize:
\[
\varphi_r=\frac{\Phi}{|\Phi|}:L_r\longrightarrow S(W^+_{\chi_j}).
\]
The degree or Mathai–Quillen current of this map is related to the Euler current of the positive spinor bundle. Schematically,
\[
[\operatorname{Zero}(\Phi)] + d\alpha(\Phi,\nabla_A\Phi)
=
e(\Omega^{W^+_{\chi_j}}),
\]
where \(\alpha\) is a Chern–Simons/Mathai–Quillen form and \(e(\Omega^{W^+_{\chi_j}})\) is the Euler/Pfaffian curvature form. Integrating over the small ball gives
\[
\int_{L_r}\alpha(\Phi,\nabla_A\Phi)
=
\int_{B_r} e(\Omega^{W^+_{\chi_j}})
-
\operatorname{mult}_p(\Phi).
\]

The character restricts the possible local Euler charge. For a purely linear equivariant model, equivariant localization would produce a weight quotient of the form
\[
\frac{w_0w_1}{u_1u_2},
\]
where \(u_1=1\), \(u_2=n-1\) are the tangent weights and
\[
w_0=nj,\qquad w_1=n(j-1)
\]
are the positive-spinor weights. After the usual orbifold normalization, the numerator is
\[
w_0w_1=n^2j(j-1),
\]
so the normalized linear-model charge is proportional to \(j(j-1)\). This is zero for \(j=0,1\), matching the fact that those twists allow a nonzero value at \(p\), and is nonzero for many forced twists.

However, the actual Seiberg–Witten spinor is not a transverse linear section. For \(j\notin\{0,1\}\), the invariant linear part is absent; the first nonzero term is a homogeneous equivariant polynomial of degree \(d\ge2\). The local zero multiplicity is then the topological degree of that leading homogeneous term, not a number determined by \(\chi_j\) alone. Different nonzero leading coefficients in the same isotypic jet space can have different multiplicities. The marked character fixes the allowed representation and the minimal order, but it does not fix a unique nonzero degree.

More importantly, even if the normalized map degree is nonzero, it is carried by the zero current. The curvature representative
\[
e(\Omega^{W^+_{\chi_j}})
\]
has bounded coefficients in the orbifold uniformizer, so
\[
\int_{B_r} e(\Omega^{W^+_{\chi_j}})=O(r^4)
\]
as a regular curvature integral. The singular orbifold Euler contribution is a topological term, not an \(L^2\) \(W^+\)-energy term. In a smoothing or bubble-tree description such a local topological charge can be carried by an ALE bubble. For the Wahl ALE filler, the metric is Ricci-flat and has \(W^+=0\) in the relevant orientation, so this charge can be transported into anti-self-dual curvature rather than into \(W^+\) or trace-free Ricci energy.

Thus the normalized spinor degree is the most point-sensitive object available, but with the present equations it does not become a forced \(W^+\) or trace-free Ricci flux. It would become decisive only if one had an additional identity identifying the spinor zero current with a \(W^+\)-Chern current for Einstein metrics. No such identity follows from the unperturbed Seiberg–Witten system.

Conclusion: the spinor map degree/relative Euler current can be nonzero and is sensitive to the marked character, but it is either an analytic multiplicity not fixed by the character alone or a singular topological current that need not be represented by \(W^+\) or trace-free Ricci energy.

---

## 5. Stress-energy and Pohozaev residues

For an Einstein orbifold metric with scalar curvature
\[
s=-\lambda,\qquad \lambda>0,
\]
the Weitzenböck formula is
\[
4\nabla_A^*\nabla_A\Phi-\lambda\Phi+|\Phi|^2\Phi=0.
\]
With \(U=|\Phi|^2\), integration over a small ball \(B_r\) gives
\[
4\int_{B_r}|\nabla_A\Phi|^2
-
\int_{B_r}U(\lambda-U)
=
4\int_{L_r}\operatorname{Re}\langle\nabla_{\nu}\Phi,\Phi\rangle.
\]
If \(\Phi=O(r^d)\) with \(d\ge2\), then
\[
\int_{L_r}\operatorname{Re}\langle\nabla_{\nu}\Phi,\Phi\rangle
=
O(r^{2d+2})\to0.
\]
The local bulk contribution also vanishes:
\[
\int_{B_r}U(\lambda-U)=O(r^{2d+4})\to0.
\]
So there is no local Weitzenböck residue.

A Pohozaev identity obtained by contracting the stress-energy tensor with the radial vector has the same structure. The link term contains expressions of the form
\[
\int_{L_r}
\Bigl(
|\nabla_\nu\Phi|^2
-
\frac12|\nabla_A\Phi|^2
+
\frac18|\Phi|^4
-\frac{\lambda}{4}|\Phi|^2
+\text{curvature couplings}
\Bigr).
\]
The spinor terms scale as \(r^{2d+2}\) or faster. The curvature couplings involve bounded tensors such as \(W^+\), scalar curvature, and trace-free Ricci; their flux through \(L_r\) is \(O(r^4)\) or smaller. Hence
\[
\lim_{r\to0}\operatorname{Pohozaev}(L_r)=0.
\]

The algebraic condition
\[
W^+(p)=\mu\operatorname{diag}(2,-1,-1)
\]
does not alter this scaling. It restricts the invariant tensor direction at \(p\), but it does not introduce a homogeneous degree-zero singular mode. Removability excludes such a mode for the abelian Seiberg–Witten pair.

Conclusion: stress-energy fluxes and Pohozaev residues vanish in the shrinking-link limit. The forced high-order zero makes them smaller, not larger.

---

## 6. Trace-free Ricci and almost-Einstein bubbling

For an exact Einstein metric, the trace-free Ricci tensor is identically zero, so there is no trace-free Ricci energy to force. The relevant issue is what happens along almost-Einstein sequences or degenerations.

If curvature concentrates at \(p\), one rescales and obtains a bubble. The marked character can migrate into the bubble as a flat spin\(^c\) twist on the asymptotic link. The relevant question is whether the bubble must carry \(W^+\) or trace-free Ricci energy because of that twist.

For the explicit Wahl ALE filler, the answer supplied by Step 93 is no:

- the filler carries a flat determinant connection for every relevant spin\(^c\) structure;
- the APS index of the filler is zero for every extendible twist;
- the exact Kawasaki computation shows that the extendible characters have the same local index contribution;
- the filler has \(s=0\), \(W^+=0\), and trace-free Ricci zero.

Thus the marked character can be absorbed by a Ricci-flat ALE bubble without producing \(W^+\) or trace-free Ricci energy. A point-sensitive obstruction would require either a non-Wahl bubble with a nonzero relative APS/Chern contribution, or a differential identity that forces the character into the \(W^+\) sector. Neither is present in the current data.

---

## 7. What survives from the marked character

The marked character does give real point-sensitive information:

1. **Forced vanishing.**  
   For \(j\notin\{0,1\}\), the spinor satisfies
   \[
   \Phi(p)=0,\qquad \nabla_A\Phi(p)=0,
   \]
   and the zero has order at least two.

2. **Forced subfamily selection.**  
   The forced set of sign classes is closed under complement, and the verifier’s averaging argument shows that one can retain the full lower bound
   \[
   \int U^2\ge32\pi^2A
   \]
   while selecting only forced-zero structures. This gives strictness
   \[
   \int (s^-)^2>32\pi^2A
   \]
   for each fixed orbifold metric, but not a uniform quantitative gap.

3. **Local \(W^+\) algebra.**  
   For \(n\ge3\), the invariant self-dual algebra at the Wahl point is Kähler-type:
   \[
   W^+(p)=\mu\operatorname{diag}(2,-1,-1).
   \]
   This is a structural constraint but not yet an energy estimate.

What does **not** survive, with the present information, is a nonzero character-fixed link flux that must be transported into \(W^+\) or trace-free Ricci energy.

---

## 8. The first missing differential datum

The missing object is not another topological character invariant. The missing object is a quantitative local differential datum connecting the forced jet to the Einstein curvature scale.

A decisive point-sensitive estimate would need one of the following.

### 8.1 A controlled leading jet coefficient

Let \(d_j\) be the minimal invariant order for the character \(\chi_j\), and let
\[
\phi_j\in \operatorname{Hom}_\Gamma(\operatorname{Sym}^{d_j}T^*_0,W^+_{\chi_j})
\]
be the leading coefficient:
\[
r^{-d_j}\Phi(r,\theta)\to \phi_j(\theta).
\]
Unique continuation implies that an irreducible solution cannot vanish to infinite order, so some leading coefficient exists. But the character does not fix its norm.

One would need an estimate of the form
\[
\int_{B_{c r_0}} U(\lambda-U)
\ge
C(n,j,\phi_j)\,\lambda^2 r_0^4,
\]
where \(r_0\) is an Einstein regularity radius at the orbifold point and \(C(n,j,\phi_j)>0\) depends on the leading jet. Then a lower bound on the dimensionless regularity scale
\[
\lambda r_0^2
\]
would produce a uniform local defect. Without such a lower bound, the defect can collapse.

### 8.2 A bubble-tree statement for the marked character

If \(\lambda r_0^2\to0\) along an Einstein or almost-Einstein sequence, one must rescale and analyze the bubble tree while retaining the marked spin\(^c\) character. The decisive quantities would be relative invariants of the bubble end:
\[
\Delta\eta
=
\eta_{\text{bubble end}}(\chi_j)-\eta_{S^3/\Gamma}(\chi_j),
\]
\[
\Delta\operatorname{CS}
=
\operatorname{CS}(A_{\text{bubble}},A_{\chi_j}),
\]
and the corresponding relative Euler/Chern current. For the explicit Wahl filler these relative APS/index quantities vanish, and the filler has \(W^+=0\) and trace-free Ricci zero. A surviving obstruction would require a bubble for which one of these relative quantities is nonzero and is represented by \(W^+\) or trace-free Ricci energy.

### 8.3 A relative Euler-current identity involving \(W^+\)

The spinor zero current is the only point-sensitive current that could potentially become topological. To use it, one would need an identity of the form
\[
d\alpha(\Phi,\nabla_A\Phi)
=
\operatorname{Pf}(\Omega^{W^+})
+
\text{Einstein-curvature remainder},
\]
with a link integral forced by \(\chi_j\). No such identity is available for the unperturbed Seiberg–Witten equations on a general Einstein four-orbifold. In Kähler or almost-Kähler settings, holomorphicity can convert zeros into divisor intersection numbers; here the Einstein metric is non-Kähler, and the local \(W^+\) algebra at \(p\) does not integrate to a global holomorphic structure.

### 8.4 A Kähler-wall test on the complex orbifold \(Y\)

A constructive way to test whether the forced zero can have arbitrarily small cost is to use the complex orbifold realization \(Y=\widehat X/C_{n,1}\). One would identify the effective orbifold divisor or line representing the forced twist, degenerate its area, and solve the unperturbed Kähler Seiberg–Witten/vortex equations along that wall. If the excess
\[
\int U(\lambda-U)
\]
or the LeBrun slack can be made arbitrarily small while preserving the forced zero, then the point-sensitive character cannot yield a uniform Einstein obstruction. If instead the vortex energy has a positive lower proportionality to a controlled area or curvature scale, that would supply the missing local estimate. The required datum is the explicit divisor/line corresponding to the marked twist and the energy asymptotics of the unperturbed Kähler monopoles.

---

## 9. Net scientific reading

The marked Wahl character changes the local jet structure of supplied Seiberg–Witten fields. It forces high-order zeros for explicit sign classes and gives a strict scalar inequality on the orbifold. But the exact removability and index-transfer machinery removes the point as an abelian curvature source, and the exact Kawasaki identity makes the extendible characters indistinguishable at the APS/index level.

The candidate link invariants behave as follows:

- Dirac eta / APS: already contained in the exact Kawasaki/index transfer; no new flux.
- Determinant Chern–Simons: flat torsion phase or vanishing relative term; no curvature cost.
- Relative Chern current: regular part vanishes as the link shrinks; torsion part is filler-compatible.
- Normalized spinor degree / Euler current: potentially nonzero and point-sensitive, but carried by the zero current and not forced into \(W^+\) or trace-free Ricci energy.
- Stress-energy / Pohozaev residue: vanishes with the link radius because the spinor is orbifold-smooth and has order at least two.
- Bubble transport: the explicit Wahl ALE filler can carry the marked character with \(W^+=0\) and trace-free Ricci zero.

Thus, with the current information, no character-fixed nonzero link invariant survives as a mandatory \(W^+\) or trace-free Ricci energy flux. The first missing differential datum is a quantitative connection between the forced leading jet of \(\Phi\) and an Einstein regularity scale, or a bubble-tree/relative APS computation showing that the character cannot migrate into a Ricci-flat bubble without paying \(W^+\) or trace-free Ricci energy.
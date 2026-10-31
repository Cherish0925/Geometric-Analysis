# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 32,
  "task_field": "verifier",
  "task_index": 2,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step32_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step32_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Analyze the proposed identification of the diagonal collapsed Berger signature charge with an APS/Dai adiabatic eta invariant. Starting from the exact diagonal signature transgression and the Hopf Berger family, determine the needed eta formula, sign, factor, and endpoint convention. Check whether an explicit odd-signature eta formula eta=-(2/3)(1-lambda^2)^2 would imply s=-3 eta and collapsed jump 2; explain kernel/reduced-eta and orientation issues. Then state the strongest justified symmetry-free collapsed-end pricing formulation, separating established APS/Dai consequences from conjectural extension to arbitrary critical-L2 near-minimizers.

## Integrated Scientific Memo

## 1. Exact diagonal identification

For the Hopf–Berger orbit
\[
h_\lambda=R^2\bigl(\lambda^2\sigma_f^2+\sigma_g^2+\sigma_h^2\bigr),
\qquad \lambda=\varepsilon/R,
\]
write
\[
a_f=\varepsilon,\qquad a_g=a_h=R,\qquad
a_g'=a_h'=U,\qquad \frac{a_f'}{a_f}=\frac VR .
\]
The normalized signature transgression of Step 27, namely \(\mathfrak s=S_0-6\), is
\[
\boxed{\;
\mathfrak s
=2+\lambda^2(U^2-2UV+V^2-4)+2\lambda^4
=2(1-\lambda^2)^2+\lambda^2(U-V)^2 .
\;}
\tag{1}
\]

Thus there are two distinct pieces:

* the intrinsic Berger contribution \(2(1-\lambda^2)^2\);
* a collar/second-fundamental-form contribution \(\lambda^2(U-V)^2\).

Consequently, an intrinsic eta invariant alone identifies the diagonal charge only for product, conical, or sufficiently controlled adiabatic collars. It does **not** determine \(\mathfrak s\) for unrestricted first jets.

For \(U=V\), and in particular for a product jet \(U=V=0\),
\[
\mathfrak s_{\mathrm{Berger}}=2(1-\lambda^2)^2.
\tag{2}
\]
Therefore the proposed formula
\[
\eta_H(\lambda)=-\frac23(1-\lambda^2)^2
\tag{3}
\]
indeed implies
\[
\boxed{\mathfrak s=-3\eta_H}
\tag{4}
\]
in that orientation/operator convention. In full biaxial first-jet form,
\[
\boxed{\mathfrak s=-3\eta_H+\lambda^2(U-V)^2.}
\tag{5}
\]

The additive normalization matters: using the raw symbolic field \(S_0\) instead of \(S_0-6\) would produce a spurious constant \(6\).

---

## 2. Why the factor is exactly \(3\)

With the conventions of the source,
\[
L(g)=\frac{|W^+|^2-|W^-|^2}{12\pi^2}\,d\mu_g .
\]
Since an orbit has volume \(2\pi^2W\) and
\[
\mathfrak s'=\frac12W(B_+-B_-),
\]
one obtains on a diagonal annulus
\[
\int L
=\frac1{12\pi^2}(2\pi^2)\int W(B_+-B_-)\,dt
=\frac13\Delta\mathfrak s.
\]
Hence
\[
\boxed{\Delta\mathfrak s=3\int L.}
\tag{6}
\]

This fixes the coefficient independently of spectral normalization. A coefficient \(3/2\) arises only if one uses an odd-signature operator convention whose spectrum is doubled; a coefficient \(6\) generally signals use of reduced eta without retaining its kernel constant.

---

## 3. APS sign and orientation

Use the APS convention
\[
\tau(X)=\int_XL-\eta_{\rm APS}(\partial X)
\tag{7}
\]
for an outward-oriented boundary and product collar. For a cobordism,
\[
\int_XL
=\tau(X)+\eta_{\rm APS}(Y_{\rm out})
-\eta_{\rm APS}(Y_{\rm in}),
\tag{8}
\]
with an additional local Gilkey/Chern–Simons correction for nonproduct collars.

The Taub-bolt data in the source fix the sign. In the blow-up orientation,
\[
\tau=-1,\qquad
\frac1{2\pi^2}\int|W^+|^2=3,\qquad
\frac1{2\pi^2}\int|W^-|^2=5,
\]
so
\[
\int L=\frac{6\pi^2-10\pi^2}{12\pi^2}=-\frac13.
\]
Equation (7) then gives
\[
-1=-\frac13-\eta_{\rm APS}^{\rm ad},
\qquad
\boxed{\eta_{\rm APS}^{\rm ad}=+\frac23.}
\tag{9}
\]

Thus the eta in (3) has the opposite orientation or operator sign:
\[
\boxed{\eta_{\rm APS}=-\eta_H.}
\tag{10}
\]
In the frame orientation where complex hyperbolic space has \(W^+\neq0\) and the bolt has self-intersection \(-1\),
\[
\eta_{\rm APS}(\lambda)=+\frac23(1-\lambda^2)^2,
\]
and
\[
\boxed{\mathfrak s
=3\eta_{\rm APS}+\lambda^2(U-V)^2.}
\tag{11}
\]

Accordingly, the formula \(\eta=-(2/3)(1-\lambda^2)^2\) is not intrinsically “wrong”; it uses the reverse three-dimensional orientation or the operator \(-B_{\rm sig}\). Any use of it must state that convention.

For an inner boundary of an annulus, its boundary orientation is opposite to the fixed orbit orientation. Equivalently, retain one orbit orientation and insert the inner endpoint with a minus sign. This is exactly the \(\Delta\mathfrak s\) convention in the diagonal identity.

---

## 4. Endpoint convention and the collapsed jump

Anchor the continuous real eta lift at the round Berger sphere:
\[
\lambda=1,\qquad \eta(1)=0,\qquad \mathfrak s(1)=0.
\]
Then take the one-sided adiabatic limit through nondegenerate metrics:
\[
\lambda\downarrow0.
\]
For the convention (3),
\[
\eta_H^{\rm ad}=-\frac23,
\qquad
\mathfrak s^{\rm ad}=2.
\tag{12}
\]
For the APS/blow-up orientation,
\[
\eta_{\rm APS}^{\rm ad}=+\frac23,
\qquad
\mathfrak s^{\rm ad}=2.
\tag{13}
\]

Thus the signature charge changes by \(2\) between the round normalization and controlled Hopf collapse. This is an **adiabatic endpoint difference**, not a discontinuity of eta at a metric with \(\lambda=0\): the limiting tensor at \(\lambda=0\) is degenerate and is not itself a three-dimensional Riemannian metric.

Controlled collapse requires at least
\[
\lambda^2(U-V)^2\longrightarrow0.
\tag{14}
\]
Without this, the endpoint contains a nonzero collar correction. This is the precise diagonal warning against identifying arbitrary collapsed first jets with the intrinsic eta limit.

---

## 5. Kernel and reduced eta

For the standard even odd-signature operator on \(S^3\),
\[
\ker B_{\rm sig}\cong H^0(S^3)\oplus H^2(S^3),
\qquad h=\dim\ker B_{\rm sig}=1.
\]
The reduced eta is therefore
\[
\bar\eta=\frac{\eta+h}{2}=\frac{\eta+1}{2}.
\tag{15}
\]

For the convention (3),
\[
\bar\eta_H(1)=\frac12,\qquad
\bar\eta_H^{\rm ad}=\frac16,
\]
and (4) becomes
\[
\boxed{\mathfrak s=3-6\bar\eta_H}
\tag{16}
\]
on the product/conical Berger family.

For the APS/blow-up convention,
\[
\bar\eta_{\rm APS}(1)=\frac12,\qquad
\bar\eta_{\rm APS}^{\rm ad}=\frac56,
\]
and
\[
\boxed{\mathfrak s=6\bar\eta_{\rm APS}-3.}
\tag{17}
\]

Hence neither \(\mathfrak s=6\bar\eta\) nor \(\mathfrak s=-6\bar\eta\) is correct without the kernel-dependent additive constant. Under orientation reversal,
\[
\eta\mapsto-\eta,\qquad
\bar\eta\mapsto1-\bar\eta.
\]

APS’s topological signature formula can be written directly with the raw eta convention used above; Dai’s adiabatic theorem is often naturally expressed using reduced eta, vertical harmonic forms, and spectral-sequence corrections. To obtain a real endpoint charge rather than merely a class modulo integers, one must choose a continuous lift anchored at the round endpoint. In more general families, spectral flow and Dai’s small-eigenvalue correction must be retained together with the relative signature.

---

## 6. Symmetry-free characteristic identity

For a compact oriented four-dimensional cobordism \(X\), define endpoint transgressions by
\[
\chi(X)=\int_X e(g)+\mathcal E_{\rm out}-\mathcal E_{\rm in},
\tag{18}
\]
and
\[
\int_XL(g)
=\tau(X)+\mathcal H_{\rm out}-\mathcal H_{\rm in}.
\tag{19}
\]
Here:

* \(\mathcal E\) is the Gauss–Bonnet boundary transgression;
* \(\mathcal H\) is the APS eta contribution plus the local nonproduct-collar correction;
* for a product collar, \(\mathcal H=\eta_{\rm APS}\).

Set
\[
\mathcal Q_+=2\mathcal E-3\mathcal H.
\tag{20}
\]
Combining Chern–Gauss–Bonnet, APS signature, and the four-dimensional curvature decomposition gives
\[
\boxed{
\frac1{8\pi^2}\int_X|\Ric^\circ|^2
=
\frac1{2\pi^2}\int_X|W^+|^2
+\frac1{96\pi^2}\int_Xs^2
-(2\chi(X)+3\tau(X))
+\mathcal Q_{+,\rm out}-\mathcal Q_{+,\rm in}.
}
\tag{21}
\]

In the diagonal normalization,
\[
\mathfrak b=2\mathcal E,\qquad
\mathfrak s=3\mathcal H,\qquad
\mathfrak b_+=\mathfrak b-\mathfrak s=\mathcal Q_+.
\]
Thus (21) is exactly the symmetry-free version of Theorem X.

For a topological annulus, \(\chi=\tau=0\), and therefore
\[
\boxed{
\frac1{8\pi^2}\int_X|\Ric^\circ|^2
\ge \mathcal Q_{+,\rm out}-\mathcal Q_{+,\rm in}.
}
\tag{22}
\]

This is the correct general pricing principle: the endpoint object is the full **chiral characteristic charge**, not eta alone.

---

## 7. Regular Hopf-collapse price

At a round Euclidean outer link,
\[
\mathcal E_{\rm round}=1,\qquad
\mathcal H_{\rm round}=0,\qquad
\mathcal Q_{+,\rm round}=2.
\tag{23}
\]

For a regular Hopf-collapse endpoint in the blow-up orientation, under bounded collapsed geometry and controlled collar first jet,

1. the Gauss–Bonnet transgression tends to zero:
   \[
   \mathcal E_{\rm ad}=0;
   \]
2. APS/Dai gives
   \[
   \mathcal H_{\rm ad}=\eta_{\rm APS}^{\rm ad}=\frac23;
   \]
3. the nonproduct correction vanishes, equivalently in the biaxial formula,
   \[
   \lambda^2(U-V)^2\to0.
   \]

Hence
\[
\mathcal Q_{+,\rm ad}
=2(0)-3\left(\frac23\right)=-2.
\tag{24}
\]
The annular pricing inequality becomes
\[
\boxed{
\liminf\frac1{8\pi^2}\int_X|\Ric^\circ|^2
\ge 2-(-2)=4.
}
\tag{25}
\]

The “collapsed jump \(2\)” refers to the signature transgression
\[
0\longrightarrow2.
\]
The full collapsed-to-round **price \(4\)** is the chiral-charge difference
\[
\mathfrak b_+^{\rm round}-\mathfrak b_+^{\rm ad}
=2-(-2)=4,
\]
combining the Euler and signature endpoint changes.

---

## 8. Exact scope of APS/Dai versus the open extension

### Established without diagonal symmetry

The following is justified whenever the geometry supplies:

* a fixed smooth circle fibration, or another fibration covered by the applicable adiabatic theorem;
* controlled horizontal metric and connection;
* bounded collapsed-frame geometry;
* controlled second fundamental form/collar first jet;
* convergence of the Euler and signature Chern–Simons transgressions;
* a fixed orientation and continuous eta lift.

Under these hypotheses:

1. the exact characteristic identity (21) holds;
2. APS/Dai computes the adiabatic endpoint \(\mathcal H_{\rm ad}\), including vertical-kernel and spectral-sequence corrections;
3. the resulting \(\mathcal Q_+^{\rm ad}\) gives the lower price (22).

For the regular Hopf fibration in the blow-up orientation,
\[
\mathcal Q_+^{\rm ad}=-2,
\]
so passage to a round Euclidean link costs at least \(4\) in units of \(8\pi^2\).

The value \(-2\) is not universal for all collapsed links: different circle bundles, orientations, orbifold/Seifert data, or Dai correction terms can change the endpoint charge.

### Not established for arbitrary critical-\(L^2\) near-minimizers

The strongest natural conjectural statement is:

> Selected links around a topology-carrying collapsed region of a critical-\(L^2\) near-minimizing sequence admit a functorial adiabatic chiral charge \(\mathcal Q_+^{\rm ad}\), compatible with cutting, and
> \[
> \liminf_j\widehat P(C_j)
> \ge
> \mathcal Q_{+,\rm out}-\mathcal Q_+^{\rm ad}.
> \]

The supplied results do not prove the geometric compactness needed for this statement. An \(L^2\) Ricci-defect bound alone does not ensure:

* existence of a fixed circle or \(F\)-structure on selected links;
* pointwise curvature control in the collapsed collar;
* control of the second fundamental form;
* convergence of local Chern–Simons terms;
* control of small eigenvalues and spectral flow;
* localization of the topology into a regular cobordism.

The diagonal formula already shows why these hypotheses are essential:
\[
\mathfrak s
=3\eta_{\rm APS}+\lambda^2(U-V)^2.
\]
The intrinsic collapsed metric fixes eta, but radial shear changes the endpoint charge. Step 30’s finite-charge anisotropic limits similarly give
\[
\mathfrak b_+^{\rm end}=-2-(C+4X)^2,
\]
while uncontrolled raw shear can move the charge more drastically. Therefore an eta-only assignment to arbitrary collapsed ends is false without first-jet/transgression control.

The strongest justified symmetry-free result is thus the exact identity (21), together with APS/Dai adiabatic evaluation for regular bounded-geometry collapsing fibrations. Extending the same pricing mechanism to arbitrary critical-\(L^2\) near-minimizers remains a compactness, slice-selection, and transgression-convergence theorem, not an established consequence of the present sources.
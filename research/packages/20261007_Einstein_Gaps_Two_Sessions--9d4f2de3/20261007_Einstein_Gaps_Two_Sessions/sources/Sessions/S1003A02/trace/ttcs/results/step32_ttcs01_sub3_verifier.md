# TTCS Independent Branch Record

```json
{
  "step_id": 32,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step27_chiral_transgression_and_small_bolt.md",
    "Sessions/S1003A02/workspace/notes/step30_Qdoubleprime_beta_pinning_and_anisotropic_collapse.md",
    "Sessions/S1003A02/workspace/notes/step20_burns_response_and_neck_quantization.md",
    "Sessions/S1003A02/workspace/notes/theorem_package_v1.md"
  ]
}
```

## Task

Analyze the proposed identification of the diagonal collapsed Berger signature charge with an APS/Dai adiabatic eta invariant. Starting from the exact diagonal signature transgression and the Hopf Berger family, determine the needed eta formula, sign, factor, and endpoint convention. Check whether an explicit odd-signature eta formula eta=-(2/3)(1-lambda^2)^2 would imply s=-3 eta and collapsed jump 2; explain kernel/reduced-eta and orientation issues. Then state the strongest justified symmetry-free collapsed-end pricing formulation, separating established APS/Dai consequences from conjectural extension to arbitrary critical-L2 near-minimizers.

## Output

## Scientific memo: Berger collapse, odd-signature \(\eta\), and chiral endpoint price

### 1. Exact diagonal comparison

Write the Hopf Berger orbit as  
\[
h_\lambda=R^2\bigl(\lambda^2\sigma_f^2+\sigma_g^2+\sigma_h^2\bigr),
\qquad \lambda=\varepsilon/R,
\]
with \(a_f=\varepsilon\), \(a_g=a_h=R\). Using the first-jet notation from Step 27,
\[
a_g'=a_h'=U,\qquad \frac{a_f'}{a_f}=\frac VR,
\]
the normalized diagonal signature transgression \(\mathfrak s=S-6\) is exactly
\[
\begin{aligned}
\mathfrak s
 &=2+\lambda^2\bigl(U^2-2UV+V^2-4\bigr)+2\lambda^4\\
 &=2(1-\lambda^2)^2+\lambda^2(U-V)^2. \tag{1}
\end{aligned}
\]

This immediately separates the intrinsic Berger contribution from the radial first-jet contribution:

* for a homothetic or conical first jet, \(U=V\),
  \[
  \mathfrak s_{\rm cone}(\lambda)=2(1-\lambda^2)^2; \tag{2}
  \]
* for controlled collapse satisfying
  \[
  \lambda^2(U-V)^2\longrightarrow0,
  \]
  the same expression gives
  \[
  \mathfrak s\longrightarrow2; \tag{3}
  \]
* an intrinsic \(\eta\)-invariant cannot determine \(\mathfrak s\) for arbitrary first jets, because the second term in (1) depends on the second fundamental form of the orbit.

Thus the proposed identification is exact on the conical Berger family and asymptotically exact for controlled Hopf collapse. It is not an identity for unrestricted collapsed jets.

If the odd-signature formula is
\[
\eta_H(\lambda)=-\frac23(1-\lambda^2)^2, \tag{4}
\]
then (2) gives exactly
\[
\boxed{\mathfrak s_{\rm cone}=-3\eta_H.} \tag{5}
\]
More generally,
\[
\boxed{\mathfrak s=-3\eta_H+\lambda^2(U-V)^2.} \tag{6}
\]

At the round endpoint \(\lambda=1\),
\[
\eta_H(1)=0,\qquad \mathfrak s(1)=0.
\]
At the one-sided adiabatic endpoint \(\lambda\downarrow0\),
\[
\eta_H^{\rm ad}=-\frac23,\qquad \mathfrak s^{\rm ad}=2. \tag{7}
\]
The value \(2\) is therefore an endpoint difference from the round normalization, not a spectral discontinuity at a Riemannian metric with \(\lambda=0\); the metric is degenerate there.

The comparison must use the normalized \(\mathfrak s=S-6\). Using the raw symbolic field \(S\) would introduce an additive \(6\).

---

### 2. Why the factor is \(3\)

Let
\[
L(g)=\frac{|W^+|^2-|W^-|^2}{12\pi^2}\,d\mu_g
\]
be the four-dimensional Hirzebruch density in the conventions of the notes. Since an orbit has volume \(2\pi^2W\) and
\[
\mathfrak s'=\frac12W(B_A-B_B),
\]
one obtains
\[
\begin{aligned}
\int_{[t_0,t_1]\times S^3}L
 &=\frac1{12\pi^2}\,2\pi^2
   \int_{t_0}^{t_1}W(B_A-B_B)\,dt\\
 &=\frac13\bigl[\mathfrak s(t_1)-\mathfrak s(t_0)\bigr]. \tag{8}
\end{aligned}
\]
Hence
\[
\boxed{\Delta\mathfrak s=3\int L.} \tag{9}
\]

This fixes the factor independently of any spectral convention. Any proposed APS identification with a factor \(3/2\) or \(6\) is using a different object, typically a reduced eta or a chiral index correction rather than the raw odd-signature eta entering the topological signature theorem.

---

### 3. APS sign and the Taub-bolt test

Assign every orbit the orientation \(+\sigma_{123}\), while the four-dimensional orientation is \(dt\wedge\sigma_{123}\). Use the APS topological signature convention
\[
\tau(X)=\int_X L-\eta_{\rm APS}(Y) \tag{10}
\]
for one outer end-link with a product collar. For a cobordism with inner and outer links this becomes
\[
\int_X L
=\tau(X)+\eta_{\rm APS}(Y_{\rm out})
-\eta_{\rm APS}(Y_{\rm in}), \tag{11}
\]
up to the standard local collar transgression when the metric is not product there.

On a topological annulus, \(\tau=0\), so (9) and (11) give
\[
\Delta\mathfrak s
=3\bigl(\eta_{\rm APS,out}-\eta_{\rm APS,in}\bigr). \tag{12}
\]
With the round anchor, the diagonal convention therefore uses
\[
\mathfrak s=3\eta_{\rm APS} \tag{13}
\]
when the local collar term vanishes.

The Taub-bolt data give a decisive sign test. The recorded values are
\[
\frac1{2\pi^2}\int|W^+|^2=3,\qquad
\frac1{2\pi^2}\int|W^-|^2=5.
\]
Therefore
\[
\int L
=\frac{6\pi^2-10\pi^2}{12\pi^2}
=-\frac13.
\]
Since \(O(-1)\) has \(\tau=-1\), equation (10) gives
\[
-1=-\frac13-\eta_{\rm APS}^{\rm ad},
\qquad
\boxed{\eta_{\rm APS}^{\rm ad}=+\frac23.} \tag{14}
\]

Consequently, the eta in (4) is related to the APS eta used by the blow-up orientation through
\[
\boxed{\eta_{\rm APS}=-\eta_H.} \tag{15}
\]
Equivalently, one may retain \(\eta_H\) and write the signature theorem as
\[
\tau=\int L+\eta_H.
\]

The sign reversal can come from either of two equivalent convention changes:

1. reversing the orientation of the three-link;
2. replacing the odd-signature operator \(B\) by \(-B\).

The supplied formula (4) cannot be attached to the diagonal orientation merely from the name “odd-signature eta”; its operator sign and Hopf orientation must be stated. The Taub-bolt calculation fixes the required translation without ambiguity.

In the blow-up orientation,
\[
\eta_{\rm APS}(\lambda)=+\frac23(1-\lambda^2)^2,
\]
and the full biaxial first-jet identity is
\[
\boxed{
\mathfrak s
=3\eta_{\rm APS}+\lambda^2(U-V)^2.
} \tag{16}
\]

---

### 4. Kernel and reduced eta

For the usual odd-signature operator on even forms on \(S^3\),
\[
\ker B_{\rm sig}\cong H^0(S^3)\oplus H^2(S^3),
\]
so
\[
h:=\dim\ker B_{\rm sig}=1. \tag{17}
\]
This harmonic zero mode persists for every \(\lambda>0\).

The reduced eta is
\[
\bar\eta=\frac{\eta+h}{2}=\frac{\eta+1}{2}. \tag{18}
\]
For the convention in (4),
\[
\bar\eta_H(1)=\frac12,\qquad
\bar\eta_H^{\rm ad}=\frac16.
\]
Equation (5) becomes
\[
\boxed{\mathfrak s=3-6\bar\eta_H} \tag{19}
\]
on the conical Berger family.

For the APS orientation fixed by Taub-bolt,
\[
\bar\eta_{\rm APS}(1)=\frac12,\qquad
\bar\eta_{\rm APS}^{\rm ad}=\frac56,
\]
and
\[
\boxed{\mathfrak s=6\bar\eta_{\rm APS}-3.} \tag{20}
\]

Thus neither \(\mathfrak s=-6\bar\eta\) nor \(\mathfrak s=6\bar\eta\) is correct without the constant arising from the persistent kernel.

Orientation reversal sends
\[
\eta\mapsto-\eta,\qquad
\bar\eta\mapsto1-\bar\eta.
\]
Accordingly, the values \(1/6\) and \(5/6\) describe the same Hopf collapse with opposite three-dimensional orientation.

Dai’s adiabatic theorem is often formulated most naturally using reduced eta, vertical harmonic forms, and Leray spectral-sequence corrections. A real-valued endpoint price therefore requires a continuous lift, not only \(\bar\eta\in\mathbb R/\mathbb Z\). The appropriate lift here is anchored by
\[
\eta(1)=0,\qquad \bar\eta(1)=\frac12.
\]
For more general metric paths, zero crossings contribute spectral-flow integers. Those integers must remain paired with the relative signature and collar transgressions.

---

### 5. Symmetry-free characteristic formulation

There is a symmetry-free formulation that contains the diagonal identity as a special case.

Let \(X\) be an oriented compact four-dimensional cobordism with inner and outer three-links. Fix a collar convention and define endpoint quantities \(\mathcal E\) and \(\mathcal H\) by
\[
\chi(X)
=\int_X e(g)
+\mathcal E_{\rm out}-\mathcal E_{\rm in}, \tag{21}
\]
\[
\int_X L(g)
=\tau(X)
+\mathcal H_{\rm out}-\mathcal H_{\rm in}. \tag{22}
\]
Here:

* \(\mathcal E\) is the Gauss–Bonnet endpoint transgression;
* \(\mathcal H\) is the APS eta contribution together with the local productization transgression determined by the first jet of the collar;
* for a product collar, \(\mathcal H=\eta_{\rm APS}\);
* changing the collar convention changes the endpoint quantity and the inserted collar integral by equal and opposite amounts.

Define the plus-chiral endpoint charge
\[
\mathcal Q_+:=2\mathcal E-3\mathcal H. \tag{23}
\]
A direct combination of (21), (22), and the four-dimensional curvature decomposition gives
\[
\boxed{
\frac1{8\pi^2}\int_X|\operatorname{Ric}^{\circ}|^2
=
\frac1{2\pi^2}\int_X|W^+|^2
+\frac1{96\pi^2}\int_Xs^2
-(2\chi(X)+3\tau(X))
+\mathcal Q_{+,\rm out}-\mathcal Q_{+,\rm in}.
} \tag{24}
\]

In the diagonal convention,
\[
\mathfrak b=2\mathcal E,\qquad
\mathfrak s=3\mathcal H,\qquad
\mathfrak b_+=\mathcal Q_+.
\]
Thus (24) is precisely the symmetry-free version of Theorem X.

For an annulus, \(\chi=\tau=0\), and both curvature integrals on the right of (24) are \(\ge0\). Hence
\[
\boxed{
\frac1{8\pi^2}\int_X|\operatorname{Ric}^{\circ}|^2
\ge
\mathcal Q_{+,\rm out}-\mathcal Q_{+,\rm in}.
} \tag{25}
\]

---

### 6. Regular Hopf collapse and the value four

Use the Euclidean first-jet convention at the outer round link. Then
\[
\mathcal E_{\rm round}=1,\qquad
\mathcal H_{\rm round}=0,\qquad
\mathcal Q_{+,\rm round}=2. \tag{26}
\]

For a regular adiabatic Hopf collapse in the blow-up orientation:

1. the Gauss–Bonnet transgression tends to zero under the bounded-geometry collapse hypotheses used in the Cheeger–Tian setting;
2. Dai’s eta limit, or the explicit Berger formula, gives
   \[
   \eta_{\rm APS}^{\rm ad}=\frac23;
   \]
3. the nonproduct signature correction tends to zero when
   \[
   \lambda^2(U-V)^2\to0.
   \]

Therefore
\[
\mathcal E_{\rm ad}=0,\qquad
\mathcal H_{\rm ad}=\frac23,\qquad
\mathcal Q_{+,\rm ad}=-2. \tag{27}
\]
Equation (25) then gives the symmetry-free regular-neck price
\[
\boxed{
\liminf\frac1{8\pi^2}
\int_X|\operatorname{Ric}^{\circ}|^2
\ge 2-(-2)=4.
} \tag{28}
\]

This is exactly the diagonal Q″ value. It depends on the complete chiral endpoint charge, not on eta alone: the outer value \(2\) comes from the Euclidean Gauss–Bonnet transgression, while the inner value \(-2\) comes from the Hopf adiabatic signature contribution.

The Taub-bolt balance also fits (24):
\[
2\chi+3\tau=1,\qquad
\frac1{2\pi^2}\int|W^+|^2=3,\qquad
\mathcal Q_{+,\rm ad}=-2,
\]
so
\[
\widehat P=3-1-2=0.
\]
For Burns with a round outer link,
\[
\widehat P=0-1+2=1.
\]

---

### 7. What APS/Dai presently provides, and what remains conjectural

#### Established under regular adiabatic geometry

The following implication uses no Bianchi–IX symmetry:

* a fixed smooth circle fibration with adiabatically shrinking fibers;
* controlled horizontal metric, connection, and collar first jet;
* the full Dai eta limit, including vertical-kernel and Leray spectral-sequence terms;
* convergence of the Gauss–Bonnet and signature collar transgressions;
* a fixed orientation, framing, and continuous eta lift.

Under these hypotheses, \(\mathcal Q_+^{\rm ad}\) is well defined and (24)–(25) give a relative collapsed-end price. For the Hopf fibration with the blow-up orientation, this gives \(\mathcal Q_+^{\rm ad}=-2\), and a regular annular passage to a round Euclidean link costs at least \(4\) in units of \(8\pi^2\).

For another circle bundle or another orientation, Dai’s full expression must be evaluated; \(-2\) is not a universal value for every collapsed three-link.

#### Conjectural extension to arbitrary critical-\(L^2\) near-minimizers

The natural proposed statement is that topology-carrying collapsed ends in an arbitrary critical-\(L^2\) near-minimizing sequence admit selected links with a functorial adiabatic charge \(\mathcal Q_+^{\rm ad}\), compatible with cutting, such that
\[
\liminf_j\widehat P(C_j)
\ge
\mathcal Q_{+,\rm out}
-\mathcal Q_+^{\rm ad}. \tag{29}
\]

The supplied work does not yet provide the geometric passage needed for (29) in that generality. In particular, an \(L^2\) Ricci-defect estimate by itself does not produce:

* a fixed smooth circle or \(F\)-structure on selected links;
* pointwise curvature control on the collapsing collar;
* controlled second fundamental forms;
* convergence of local Chern–Simons transgressions;
* convergence of eta through small-eigenvalue formation and spectral flow;
* localization of all relevant topology into one regular cobordism.

The exact diagonal formula (1) already exhibits the essential obstruction to an eta-only formulation: the intrinsic Berger metric fixes \(\eta(\lambda)\), while uncontrolled radial shear contributes
\[
\lambda^2(U-V)^2
\]
to \(\mathfrak s\). The more general high-shear entries in Step 30 similarly alter the chiral endpoint charge through first-jet data not recorded by the intrinsic link metric.

Accordingly, the strongest current symmetry-free statement is (24) together with Dai’s adiabatic evaluation whenever a regular collapsing fibration and convergent collar transgressions are present. The universal assignment of the same charge to collapsed ends arising from arbitrary critical-\(L^2\) near-minimizers remains a conjectural compactness-and-transgression theorem.
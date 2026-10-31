# TTCS Independent Branch Record

```json
{
  "step_id": 34,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step33_link_charges_global_decomposition_static_channel.md",
    "Sessions/S1003A02/workspace/notes/step31_charge_variation_constraint_pinning_nonround_opening.md",
    "Sessions/S1003A02/workspace/notes/step30_Qdoubleprime_beta_pinning_and_anisotropic_collapse.md",
    "Sessions/S1003A01/workspace/notes/step26_action_budget_matching.md"
  ]
}
```

## Task

Derive and critically assess the proposed symmetry-free two-part link calculus. Starting from a hypersurface foliation of a scalar-normalized four-manifold, write the Gauss and Codazzi constraints in conventions compatible with Ric°(nu,nu), Ric°(nu,.) and the second fundamental form; explain exactly which squared constraint components are controlled by integral |Ric°|^2 and how the diagonal Lemmas N, P and beta-pinning instantiate them. Compare this kinematic/constraint channel with Theorem G's characteristic boundary channel. Give a precise theorem-level general principle without claiming compactness or link regularity from L2 control alone. Note sign/convention dependencies that must be stated.

## Output

# Scientific memo: a symmetry-free two-part link calculus

## 1. Foliation conventions and the Gauss–Codazzi fields

Let \(U^4\) be foliated by closed oriented hypersurfaces \(\Sigma_t\). In Gaussian coordinates,
\[
g=dt^2+h_t,\qquad \nu=\partial_t,
\]
and use
\[
K(X,Y)=g(\nabla_X\nu,Y)=\frac12\partial_t h_t(X,Y),\qquad
\Theta=\operatorname{tr}_{h_t}K .
\]
Thus an outward Euclidean sphere has \(K>0\). Take
\[
R(X,Y)Z=\nabla_X\nabla_YZ-\nabla_Y\nabla_XZ-\nabla_{[X,Y]}Z,
\]
with spheres having positive sectional curvature.

The contracted Gauss equation is
\[
R_{h_t}=s-2\operatorname{Ric}(\nu,\nu)+\Theta^2-|K|^2,
\]
hence
\[
G(\nu,\nu)
=\operatorname{Ric}(\nu,\nu)-\frac{s}{2}
=\frac12\bigl(\Theta^2-|K|^2-R_{h_t}\bigr).
\]
Since in dimension four
\[
\operatorname{Ric}^{\circ}=\operatorname{Ric}-\frac{s}{4}g,
\]
the scalar Gauss residual is
\[
\boxed{
\mathcal C
:=\operatorname{Ric}^{\circ}(\nu,\nu)
=\frac12\bigl(\Theta^2-|K|^2-R_{h_t}\bigr)+\frac{s}{4}.
}
\tag{1}
\]
For the scalar normalization \(s=-24\),
\[
\boxed{
\mathcal C
=\frac12\bigl(\Theta^2-|K|^2-R_{h_t}\bigr)-6.
}
\tag{2}
\]

The contracted Codazzi equation, with the same conventions, is
\[
\boxed{
\mathcal J
:=\operatorname{Ric}^{\circ}(\nu,\cdot)
=\operatorname{Ric}(\nu,\cdot)
=\operatorname{div}_{h_t}K-d\Theta .
}
\tag{3}
\]
The scalar subtraction has no mixed component.

If the foliation is written as \(g=N^2dt^2+h_t\) with zero shift, equations (1)–(3) remain valid when \(K=\frac12\mathcal L_\nu h\), \(\nu=N^{-1}\partial_t\), and \(d\mu_g=N\,dt\,d\mu_h\). Transport equations then contain \(N\) and \(\operatorname{Hess}_{h}N\). A nonzero shift adds the corresponding Lie derivatives.

For Gaussian coordinates, the tangential Ricci evolution is
\[
\operatorname{Ric}^{g}_{ij}
=\operatorname{Ric}^{h}_{ij}
-\partial_tK_{ij}-\Theta K_{ij}
+2(K^2)_{ij}.
\]
Therefore the tangential trace-free residual is
\[
\boxed{
\mathcal S
:=\bigl(\operatorname{Ric}^{\circ}|_{T\Sigma_t}\bigr)^{\circ_{h_t}}
=
\bigl(\operatorname{Ric}^{h}-\partial_tK-\Theta K+2K^2\bigr)^{\circ_{h_t}}.
}
\tag{4}
\]
Only \(\mathcal C\) and \(\mathcal J\) are the usual Hamiltonian and momentum constraint fields. The tensor \(\mathcal S\) is the trace-free evolution residual. This distinction is important when interpreting the diagonal pinning identities.

---

## 2. Exact orthogonal decomposition of \(\operatorname{Ric}^{\circ}\)

Relative to \(T U=\mathbb R\nu\oplus T\Sigma_t\),
\[
\operatorname{Ric}^{\circ}
=
\mathcal C\,\nu^\flat\otimes\nu^\flat
+2\nu^\flat\odot\mathcal J
+\mathcal S-\frac{\mathcal C}{3}h_t .
\]
Consequently,
\[
\boxed{
|\operatorname{Ric}^{\circ}|^2
=\frac43\mathcal C^2+2|\mathcal J|^2+|\mathcal S|^2.
}
\tag{5}
\]

Thus the integral defect controls precisely
\[
\frac43\int_U\mathcal C^2\,d\mu
+2\int_U|\mathcal J|^2\,d\mu
\le P(g;U),
\tag{6}
\]
and separately
\[
\int_U\mathcal C^2\,d\mu\le\frac34P(g;U),\qquad
\int_U|\mathcal J|^2\,d\mu\le\frac12P(g;U).
\tag{7}
\]

Equation (5) is stronger and more precise than the statement that the normal Ricci components are merely bounded by the full tensor norm. The coefficient \(4/3\) occurs because a nonzero \(\mathcal C\) forces the tangential trace \(-\mathcal C\); the coefficient \(2\) occurs because mixed components appear twice in the norm of a symmetric tensor.

A useful invariant dual estimate follows immediately. For every scalar \(f\), tangential vector field \(X\), and tangential trace-free tensor \(T\),
\[
\begin{aligned}
\left|
\int_U
\bigl(f\mathcal C+\langle X,\mathcal J\rangle+\langle T,\mathcal S\rangle\bigr)
\,d\mu
\right|^2
\le {}&
P(g;U)\\
&\times
\int_U
\left(\frac34f^2+\frac12|X|^2+|T|^2\right)d\mu .
\end{aligned}
\tag{8}
\]
This is the symmetry-free source of weighted pinning inequalities. Whenever a geometric observable \(\mathcal A\) satisfies an exact transport relation
\[
\mathcal A(\Sigma_b)-\mathcal A(\Sigma_a)-\int_U F\,d\mu
=
\int_U
\bigl(f\mathcal C+\langle X,\mathcal J\rangle+\langle T,\mathcal S\rangle\bigr)d\mu ,
\tag{9}
\]
one obtains
\[
\boxed{
\widehat P(g;U)
\ge
\frac{
\left|\mathcal A(\Sigma_b)-\mathcal A(\Sigma_a)-\int_UF\,d\mu\right|^2
}{
8\pi^2\displaystyle\int_U
\left(\frac34f^2+\frac12|X|^2+|T|^2\right)d\mu
}.
}
\tag{10}
\]
The drift \(F\) represents shape evolution already present on an Einstein metric. Only the drift-corrected mismatch is priced by \(\operatorname{Ric}^{\circ}\).

Small \(L^2\) size of \(\mathcal C\) says only that
\[
\frac12(\Theta^2-|K|^2-R_h)\approx6
\]
in an integral sense. It does not control \(R_h\), \(K\), or \(\Theta\) separately. Likewise, small \(\mathcal J\) controls only the combination \(\operatorname{div}K-d\Theta\). These facts prevent direct extraction of collar geometry from (6).

---

## 3. Exact relation with the diagonal identities

For a diagonal Bianchi–IX metric,
\[
g=dt^2+a_f^2\sigma_f^2+a_g^2\sigma_g^2+a_h^2\sigma_h^2,
\qquad
y_i=\frac{a_i'}{a_i},
\]
the eigenvalues of \(K\) are \(y_f,y_g,y_h\). Put
\[
\Theta=y_f+y_g+y_h,\qquad
\sigma_2(y)=y_fy_g+y_gy_h+y_hy_f.
\]
Since
\[
\frac12(\Theta^2-|K|^2)=\sigma_2(y),
\]
equation (2) becomes
\[
\boxed{
\mathcal C=\sigma_2(y)-6-\frac12R^{(3)}.
}
\tag{11}
\]
This is exactly Lemma N’s Hamiltonian field.

If
\[
e_\alpha=\operatorname{Ric}_{\alpha\alpha}+6,
\]
then \(s=-24\) gives
\[
e_0+e_f+e_g+e_h=0
\]
and
\[
\mathcal C=e_0
=\frac12(e_0-e_f-e_g-e_h).
\]
In the notation of Lemma N, where the radial trace channel is denoted by \(H_{\rm def}\),
\[
\mathcal C=-\frac34H_{\rm def}.
\]

Define the two diagonal tangential trace-free projections
\[
E_{\rm fb}=e_f-\frac{e_g+e_h}{2},\qquad
D_{\rm c}=e_g-e_h.
\]
Then
\[
|\mathcal S|^2
=\frac23E_{\rm fb}^2+\frac12D_{\rm c}^2,
\]
and (5) becomes
\[
\boxed{
|\operatorname{Ric}^{\circ}|^2
=\frac43\mathcal C^2+\frac23E_{\rm fb}^2+\frac12D_{\rm c}^2
=\frac34H_{\rm def}^2+\frac23E_{\rm fb}^2+\frac12D_{\rm c}^2.
}
\tag{12}
\]
With the orbit normalization used in the notes,
\[
\boxed{
\widehat P
=\int W\left(
\frac{\mathcal C^2}{3}
+\frac{E_{\rm fb}^2}{6}
+\frac{D_{\rm c}^2}{8}
\right)dt .
}
\tag{13}
\]

The remaining identities in Lemma N are symmetry reductions of contracted Bianchi and mean-curvature evolution:
\[
\mathcal C'
=-2\Theta\mathcal C-\sum_i(\Theta-y_i)e_i,
\qquad
\Theta'=18-\Theta^2+R^{(3)}+\mathcal C.
\tag{14}
\]

### 3.1 Lemma P is a tangential evolution identity

Let
\[
q=\log\frac{a_g}{a_h},\qquad q'=y_g-y_h,
\]
and let
\[
\Pi=P_g-P_h
\]
be the corresponding intrinsic Ricci drift. The exact anisotropy equation is
\[
(Wq')'=W(\Pi-D_{\rm c}).
\tag{15}
\]
For
\[
\widetilde\Phi=q+\frac14q',
\]
equation (15) gives
\[
\boxed{
\widetilde\Phi'
=
\left(1-\frac{\Theta}{4}\right)q'
+\frac14\Pi-\frac14D_{\rm c}
=:F_\Phi-\frac14D_{\rm c}.
}
\tag{16}
\]
Thus
\[
\left|
\Delta\widetilde\Phi-\int F_\Phi\,dt
\right|
\le
\sqrt{\frac{\widehat P}{2}}
\left(\int\frac{dt}{W}\right)^{1/2},
\tag{17}
\]
or equivalently
\[
\boxed{
\widehat P
\ge
\frac{2\left|\Delta\widetilde\Phi-\int F_\Phi dt\right|^2}
{\displaystyle\int W^{-1}dt}.
}
\tag{18}
\]

This is not a Codazzi estimate. It uses the \(D_{\rm c}\) projection of the tangential evolution tensor \(\mathcal S\). The Green identity
\[
M=-\int W D_{\rm c}K_G\,dt
\]
is the corresponding second-order weighted form and yields
\[
\widehat P\ge
\frac{M^2}{8\int WK_G^2dt}.
\]

### 3.2 Beta-pinning is the other tangential projection

With
\[
v=\beta'=y_f-\frac{y_g+y_h}{2},
\]
and
\[
\widetilde B=
\log\frac{\kappa}{\sqrt{1+\zeta}}
+\frac14(v-\kappa^{-1}),
\]
the exact identity is
\[
\boxed{
\widetilde B'=F_\beta-\frac14E_{\rm fb}.
}
\tag{19}
\]
Equation (13) then gives
\[
\boxed{
\left|
\Delta\widetilde B-\int F_\beta dt
\right|
\le
\sqrt{\frac{3\widehat P}{8}}
\left(\int\frac{dt}{W}\right)^{1/2},
}
\tag{20}
\]
and hence
\[
\widehat P
\ge
\frac{8\left|\Delta\widetilde B-\int F_\beta dt\right|^2}
{3\displaystyle\int W^{-1}dt}.
\tag{21}
\]

Therefore:

* Lemma N is the diagonal Hamiltonian constraint.
* Lemma P uses one diagonal component of \(\mathcal S\).
* Beta-pinning uses the other diagonal component of \(\mathcal S\).
* The momentum field \(\mathcal J\) vanishes identically in the homogeneous diagonal ansatz.

The last point matters for a symmetry-free extension. Diagonal calculations do not test the mixed Ricci sector \(\operatorname{Ric}^{\circ}(\nu,\cdot)\). In a general foliation this sector measures spatial inhomogeneity of \(K\) through \(\operatorname{div}K-d\Theta\).

The specific observables \(q,\beta,\widetilde\Phi,\widetilde B\) also require the distinguished \(f,g,h\) splitting. Equation (8) is invariant, but a nonsymmetric analogue of Lemma P or beta-pinning requires additional geometric structure supplying a preferred tensor \(T\) and a computable drift.

---

## 4. Comparison with Theorem G’s characteristic link channel

For an oriented compact region \(U\), Theorem G states
\[
\widehat P(U)
=
\frac1{2\pi^2}\int_U|W^\pm|^2
+\frac1{96\pi^2}\int_U s^2
-(2\chi(U)\pm3\tau(U))
+\mathcal Q_\pm(\partial U).
\tag{22}
\]
For \(s=-24\),
\[
\frac1{96\pi^2}\int_U s^2
=3\widehat V(U),
\qquad
\widehat V(U)=\frac{2\operatorname{Vol}(U)}{\pi^2}.
\]
Hence
\[
\boxed{
\widehat P(U)
\ge
\mathcal Q_\pm(\partial U)
+3\widehat V(U)
-(2\chi(U)\pm3\tau(U)).
}
\tag{23}
\]

For a product slab \(U_{ab}\cong[a,b]\times\Sigma\), one has \(\chi(U_{ab})=\tau(U_{ab})=0\). If each link charge is recorded using the nested-family normal \(+\nu\), then the inner link contributes with the opposite orientation:
\[
\boxed{
\widehat P(U_{ab})
\ge
\mathcal Q_\pm(\Sigma_b)-\mathcal Q_\pm(\Sigma_a)
+3\widehat V(U_{ab}).
}
\tag{24}
\]

The two channels contain different information.

### Characteristic channel

Equation (22):

* is symmetry-free and does not require a foliation;
* retains topology through \(2\chi\pm3\tau\);
* prices changes of the Euler/signature transgression;
* depends only on the two end links and the bulk Weyl/scalar terms;
* can be weak along a path on which both charges decrease.

The charge is not determined by the intrinsic link metric alone. Chern and Pontryagin transgressions also involve the second fundamental form. The Berger formula
\[
3\mathcal H
=
2(1-\lambda^2)^2+\lambda^2(U-V)^2
\]
exhibits explicitly how radial shear changes the link charge.

### Kinematic/constraint channel

Equations (5), (8), and (10):

* require a chosen foliation or another transport construction;
* resolve the defect into Hamiltonian, momentum, and tangential evolution sectors;
* can price shape or first-jet changes after subtracting Einstein drift;
* naturally produce denominators such as \(\int W^{-1}dt\), so volume growth is essential;
* do not see topology unless topology is supplied separately.

The static channel found in Lemma Z is consistent with this distinction. A triaxial path can keep the characteristic charges low or decreasing while changing the contact-slot geometry. The diagonal action then appears mainly in \(D_{\rm c}\), hence in \(\mathcal S\), and is detected by Lemma P or its Green form rather than by upward charge variation.

The two estimates apply to the same quantity \(\widehat P\), so their lower estimates are generally combined by taking a maximum. They should not be added mechanically. Additivity is available for disjoint regions, or after an explicit allocation using the orthogonal decomposition (5).

---

## 5. Precise two-part principle

### Theorem: characteristic–transport link principle

Let \((U^4,g)\) be oriented, \(s=-24\), and suppose \(U\) admits a smooth Gaussian foliation by closed links \(\Sigma_t\). Define \(K,\Theta,\mathcal C,\mathcal J,\mathcal S\) by (1)–(4).

1. **Defect decomposition.**
   \[
   P(g;U)
   =
   \int_U
   \left(
   \frac43\mathcal C^2+2|\mathcal J|^2+|\mathcal S|^2
   \right)d\mu .
   \tag{25}
   \]

2. **Characteristic identity.**
   For either chirality,
   \[
   \widehat P(U)
   =
   \frac1{2\pi^2}\int_U|W^\pm|^2
   +3\widehat V(U)
   -(2\chi(U)\pm3\tau(U))
   +\mathcal Q_\pm(\partial U).
   \tag{26}
   \]

3. **Transport estimate.**
   Every exact relation of the form (9) satisfies (10).

Consequently,
\[
\boxed{
\widehat P(U)\ge
\max\left\{
0,\,
\max_\pm\!\left[
\mathcal Q_\pm(\partial U)
+3\widehat V(U)
-(2\chi(U)\pm3\tau(U))
\right],\,
\frac{|\mathcal M|^2}{8\pi^2\mathcal D}
\right\},
}
\tag{27}
\]
where
\[
\mathcal M=
\mathcal A(\Sigma_b)-\mathcal A(\Sigma_a)-\int_UF\,d\mu
\]
and
\[
\mathcal D=
\int_U
\left(\frac34f^2+\frac12|X|^2+|T|^2\right)d\mu .
\]

This theorem is fully symmetry-free. Its useful numerical content depends on finding an invariant transport observable \(\mathcal A\), estimating its Einstein drift \(F\), and controlling the dual weight \(\mathcal D\). The diagonal Lemmas P and beta-pinning provide such observables only after choosing the Bianchi–IX slot splitting.

---

## 6. What \(L^2\) defect control does not provide

Neither part of the calculus yields compactness or link regularity from \(L^2\) control alone.

1. Equation (25) controls combinations of \(R_h\), \(K\), and \(\nabla K\), not those quantities separately.

2. An \(L^2\) estimate in four dimensions gives no direct trace control for \(K\) or the intrinsic link curvature on an arbitrarily selected leaf.

3. The Chern and Pontryagin transgressions require first-jet collar information. The APS term also involves the spectral geometry of the link. Under collapse, small eigenvalues and the adiabatic correction are additional data.

4. Scalar normalization makes \(\mathcal C=\operatorname{Ric}^{\circ}(\nu,\nu)\), but it does not force the foliation to have controlled lapse, injectivity radius, second fundamental form, or intrinsic curvature.

5. Even \(\operatorname{Ric}^{\circ}=0\) permits substantial evolution of \(h_t\) and \(K_t\). The drift terms in (9), (16), and (19) are therefore indispensable.

Accordingly, the calculus gives exact accounting once suitable links and transport structures are available. It does not by itself select those links or prove convergence of \(\mathcal Q_\pm\), APS data, Seiberg–Witten fluxes, or Chern–Simons terms.

---

## 7. Sign and normalization dependencies

All numerical link charges require the following conventions to be fixed.

1. **Riemann tensor:** the formulas above use the convention for which round spheres have positive sectional curvature.

2. **Second fundamental form:** \(K(X,Y)=g(\nabla_X\nu,Y)\). Replacing this by its opposite changes the displayed Codazzi sign and all transgression formulas involving odd powers of \(K\).

3. **Normal direction:** under \(\nu\mapsto-\nu\),
   \[
   K\mapsto-K,\qquad
   \Theta\mapsto-\Theta,\qquad
   \mathcal J\mapsto-\mathcal J,
   \]
   while \(\mathcal C\) is unchanged. An inner link of a slab therefore contributes oppositely to an outer link.

4. **Four-dimensional orientation:** reversing it exchanges \(W^+\) and \(W^-\), changes the sign of \(\tau\), and interchanges the two chiral identities after all induced link orientations are adjusted.

5. **APS normalization:** the definition of the eta term, inclusion of kernel terms, and the local \(p_1\) transgression must match the stated formula
   \[
   \int_U L=\tau(U)+\mathcal H(\partial U).
   \]
   Changing the eta convention without changing \(\mathcal H\) changes the numerical values assigned to \(\mathcal Q_\pm\).

6. **Scalar scale:** the constant \(-6\) in (2) is specific to \(s=-24\). If a fixed reference scalar \(s_0\) is inserted while the actual scalar is not \(s_0\), then
   \[
   \frac12(\Theta^2-|K|^2-R_h)+\frac{s_0}{4}
   =
   \operatorname{Ric}^{\circ}(\nu,\nu)+\frac{s_0-s}{4}.
   \]

7. **Bianchi–IX orbit normalization:** equation (13) uses the normalization in which integration over an orbit converts \(\widehat P\) to \(\frac14\int W|\operatorname{Ric}^{\circ}|^2dt\). Rescaling the invariant one-forms changes the displayed \(W\)-coefficients.

The resulting picture is coherent: Theorem G supplies a topological and characteristic link accounting, while Gauss–Codazzi plus tangential evolution supplies a foliation-dependent transport accounting. Their symmetry-free intersection is the exact decomposition (25) together with the dual estimate (10); the diagonal pinning identities are structured projections of this general tensor statement, not substitutes for link regularity or compactness.
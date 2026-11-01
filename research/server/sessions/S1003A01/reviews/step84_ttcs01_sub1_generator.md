# TTCS Independent Branch Record

```json
{
  "step_id": 84,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step83_normalized_action_weyl_deficit_and_AKE_degenerations.md",
    "Sessions/S1003A01/workspace/notes/step79_second_tier_dWplus_kodaira_and_log_torsion_identity.md",
    "Sessions/S1003A01/workspace/notes/step80_regularized_torsion_transport.md",
    "Knowledge/objects/papers/2603.09028-Einstein-deformations-of-Kähler-Einstein-metrics--062c0a015de6--2a0f3c1e029d/object.md",
    "Knowledge/objects/papers/Integrability-of-Einstein-deformations-and-desingularizations--8e63541ce32f--b5af64ba3e90/object.md",
    "Knowledge/objects/papers/Higher-order-obstructions-to-the-desingularization-of-Einstein-metrics--94f76f3b5378--19c12fb27fae/object.md",
    "Knowledge/objects/papers/Deformations-of-nodal-Kähler-Einstein-Del-Pezzo-surfaces-with-discrete--9b4cc6f157f8--c134bd6a8c7c/object.md"
  ]
}
```

## Task

Develop the strongest concrete matched-analysis route for the following problem. We have a sequence of closed negative almost-Kähler Einstein four-manifolds converging noncollapsed with bounded diameter to a Kähler–Einstein orbifold with one A1 point, and Step 83 proves that all self-dual Weyl/torsion concentration vanishes and the unique bubble is orientation-matched Ricci-flat Kähler Eguchi–Hanson. We want local exclusion of strict AKE pairs near this one-level degeneration, not finiteness of the entire compactified Einstein moduli. Read the supplied notes and sources. Separate the actual tangent directions (Kähler complex/smoothing deformations and gauge) from a hypothetical nonintegrable AKE normal direction, and derive what a contradiction/blow-up argument would need on the exterior, cone neck, and Eguchi–Hanson core. Identify a precise weighted normal operator, its likely kernel/cokernel, matching data, and one estimate or finite-dimensional map whose proof would settle the local question. Be alert to the fact that negative KE Einstein Jacobi fields are J-anti-invariant Kodaira–Spencer tensors and are tangent to Kähler families, while the AKE torsion is a derivative quantity; do not confuse these. Also incorporate the hyperkähler rotation freedom of Eguchi–Hanson and explain whether it is tangent Kähler/smoothing data or a possible strict-AKE entrance. Produce a mathematical memo with equations and a decisive next calculation, not general advice.

## Output

# Mathematical memo: a one-\(A_{1}\) matched reduction for excluding strict AKE pairs

Normalize
\[
\operatorname{Ric}(g)=\lambda g,\qquad \lambda<0,\qquad s=4\lambda,
\]
and let \((V,g_{0},J_{0},\omega _0)\) be the Kähler–Einstein orbifold with one \(\mathbb R^{4}/\mathbb Z_{2}\) point \(p\). Write the bubbling length as \(\varepsilon\), so the core metric is \(\varepsilon ^2g_{\mathrm{EH}}\). Step 83 gives, for every AKE sequence in this geometry,

* convergence of \(\omega_\varepsilon\) to \(\omega _0\) away from \(p\);
* an Eguchi–Hanson core with a parallel self-dual limit form;
* zero concentration of \(W^{+}\) and of the AKE torsion density.

The remaining issue is therefore not energy loss. It is whether a new component of coupled Einstein–almost-Kähler solutions can approach the Kähler one-\(A_{1}\) stratum while being separated from it by a distance tending to zero with \(\varepsilon\).

## 1. The correct coupled linearization

Use a Bianchi slice for the Einstein equation:
\[
\Phi_{\bar g}(g)
=\operatorname{Ric}(g)-\lambda g+\delta_g^{*}B_{\bar g}g.
\]
At an Einstein metric its linearization is, in the conventions of Ozuch,
\[
P_g h=\frac12\nabla^{*}\nabla h-\mathring Rh .
\]

For the almost-Kähler structure use a two-form \(\Omega\) satisfying
\[
d\Omega=0,\qquad *_g\Omega=\Omega,\qquad |\Omega|_g^{2}=2.
\]
At a Kähler pair \((g,\omega)\), with variation \((h,\alpha)\), the coupled linear operator is
\[
\boxed{
\mathbb L_g(h,\alpha)=
\left(
P_gh,\;
d\alpha,\;
\alpha-*\alpha-\dot *_{h}\omega,\;
2\langle\alpha,\omega\rangle-\operatorname{tr}h
\right).
}
\tag{1.1}
\]
Here
\[
\dot *_{h}\omega
=
*\left[\frac12(\operatorname{tr}h)\omega-h^{\sharp}\!\cdot\omega\right],
\qquad
2\alpha^{-}=\dot *_{h}\omega .
\]
A Fredholm realization replaces the closedness block by the self-dual Hodge–Dirac operator
\[
D^{+}=d^{*}:\Omega^{+}\longrightarrow\Omega^{1},
\]
after the anti-self-dual part of \(\alpha\) has been prescribed by \(h\). Since a self-dual two-form is closed exactly when it is coclosed, this replacement loses no equation.

The linearized Kählerity tensor is
\[
\mathbb T(h,\alpha)
=
\nabla\alpha-\dot\nabla_{h}\omega.
\tag{1.2}
\]
It is essential that \(\mathbb L(h,\alpha)=0\) does not automatically imply \(\mathbb T(h,\alpha)=0\).

### Exterior kernel

For a compact \(s<0\) Kähler–Einstein metric, Nagy’s description gives
\[
hJ=-Jh,\qquad \bar\partial h=0,\qquad \delta h=0
\tag{1.3}
\]
for every TT Einstein Jacobi field. These are Kodaira–Spencer tensors. For such \(h\) there is a canonical variation \(\alpha_{K}(h)\) satisfying
\[
\mathbb T(h,\alpha_K(h))=0.
\]
Thus the Kähler infinitesimal sector is
\[
\mathcal K_{\mathrm{ext}}
=
\{(h,\alpha_K(h)):h\in\ker P,\ \bar\partial h=0\}.
\tag{1.4}
\]
Only those directions lying in the zero set of the complex Kuranishi map are actual tangents to Kähler families. The full linear kernel can be larger.

There is also a genuinely different kernel:
\[
(h,\alpha)=(0,\sigma),\qquad
\sigma\in
\bigl(H^{2,0}(V)\oplus H^{0,2}(V)\bigr)_{\mathbb R}.
\tag{1.5}
\]
Indeed \(\sigma\) is harmonic, self-dual, and pointwise orthogonal to \(\omega_0\), so all linearized algebraic equations hold, while
\[
\mathbb T(0,\sigma)=\nabla\sigma.
\]
This is the first possible AKE-normal direction. It changes the harmonic self-dual form without changing the metric to first order. Its torsion is a derivative quantity:
\[
q(t)=|\nabla\Omega_t|^{2}
=t^{2}|\nabla\sigma|^{2}+O(t^{3}).
\tag{1.6}
\]

Gauge directions are
\[
(h,\alpha)=\bigl(\mathcal L_Xg,\mathcal L_X\omega\bigr),
\]
and are removed by the Bianchi slice and a marked harmonic-form normalization.

## 2. The Eguchi–Hanson parameter and why its rotations are Kähler data

Fix a cone framing identifying \(\Lambda^{+}_{p}\) with the asymptotic parallel self-dual forms on Eguchi–Hanson. Kronheimer’s \(A_{1}\) parameter is a vector
\[
\zeta\in\Lambda^{+}_{p}\cong\mathbb R^{3},
\qquad \varepsilon\asymp |\zeta|^{1/2}.
\]
The three \(L^{2}\) Einstein Jacobi fields on Eguchi–Hanson are the derivatives with respect to the three components of \(\zeta\). Their leading terms are the \(r^{-4}\) tensors \(O_{k}^{4}\) recorded in Ozuch’s work.

At a Kähler–Einstein point,
\[
\mathcal R^{+}
=
W^{+}+\frac{s}{12}I
=
\frac{\lambda}{2}\,\omega_0\otimes\omega_0,
\tag{2.1}
\]
because
\[
\mathcal R^{+}\omega_0=\lambda\omega_0,
\qquad
\ker\mathcal R^{+}=\omega_0^{\perp}.
\]
The leading Eguchi–Hanson matching equations are therefore
\[
\boxed{
\mathfrak m_{\mathrm{EH}}(\zeta)
=
C\,\mathcal R^{+}_{g_0}(p)\zeta
=
C\lambda\,\frac{\langle\zeta,\omega_0\rangle}{2}\,\omega_0.
}
\tag{2.2}
\]
This is the Green pairing of the exterior quadratic term \(H_{2}\) with the three \(L^{2}\) Eguchi–Hanson Jacobi fields, exactly of the form derived by Ozuch.

Consequently,

* the component \(\zeta_{\parallel}\in\mathbb R\omega_0\) is removed by a nonzero scalar matching equation;
* the two components
  \[
  \zeta_{\perp}\in\omega_0^{\perp}
  \tag{2.3}
  \]
  survive and form the complex \(A_{1}\)-smoothing parameter.

In hyperkähler period language, \(\langle\zeta,\omega_0\rangle=0\) says that the vanishing sphere has zero period for the Kähler form matching \(\omega_0\); it is the smoothing, rather than Kähler-resolution, configuration. Thus the two rotational parameters in \(\omega_0^{\perp}\) are Kähler complex/smoothing data. They do not provide a strict-AKE entrance.

A second rotational freedom changes the chosen parallel form on a fixed Eguchi–Hanson metric. It also has zero core torsion. Globally it must match either:

1. the variation of the Kähler form induced by an exterior Kodaira–Spencer deformation, or
2. the value at \(p\) of an exterior primitive harmonic form \(\sigma\).

Only the second option can carry torsion, and that torsion is located in the exterior where \(\nabla\sigma\neq0\), not in the Eguchi–Hanson core.

## 3. Model kernels on the three regions

Choose
\[
0<\delta<2
\tag{3.1}
\]
and a radius function
\[
\rho_\varepsilon\simeq
\begin{cases}
\varepsilon(1+R),&\text{on the scaled Eguchi--Hanson core},\\
r,&\text{on the cone neck},\\
1,&\text{on the far exterior}.
\end{cases}
\]
For a tensor \(u\), set
\[
\|u\|_{C^{k,\alpha}_{\delta,\varepsilon}}
=
\sum_{j=0}^{k}\sup
\rho_\varepsilon^{\,j-\delta}|\nabla^{j}u|
+
\bigl[
\rho_\varepsilon^{\,k+\alpha-\delta}\nabla^{k}u
\bigr]_{\alpha}.
\tag{3.2}
\]
The constant cone modes, exterior Jacobi fields, and \(L^{2}\) Eguchi–Hanson fields are split off as finite coefficients, as in Ozuch’s decoupling norms.

### Exterior

After orbifold removable-singularity regularity, the kernel consists of

* Kodaira–Spencer Einstein tensors with their Kähler form variations;
* primitive harmonic self-dual forms \(\sigma\);
* gauge terms before slicing.

### Cone neck

On \((\mathbb R^{4}/\mathbb Z_{2},e)\),
\[
P_e=\frac12\Delta
\]
componentwise. The \(\mathbb Z_{2}\)-invariant homogeneous modes have degrees \(0,2,\ldots\); degree-one coefficients are odd and do not descend. The self-dual Hodge block has the same relevant gap: constants at degree \(0\), followed by quadratic modes. Hence the open weight interval \((0,2)\) contains no new neck mode once constant matching data have been separated.

This gap is what prevents torsion from living only in an expanding cone annulus.

### Eguchi–Hanson core

For the Einstein block:

* the \(L^{2}\) kernel is three-dimensional, generated by the \(\zeta\)-variations;
* gauge terms are Lie derivatives;
* the cokernel is the same three-dimensional space by self-adjointness.

For the self-dual Hodge block:

* bounded self-dual harmonic forms are the three parallel hyperkähler forms;
* the unique \(L^{2}\) harmonic two-form is anti-self-dual in the orientation used here;
* there is therefore no localized self-dual harmonic mode that vanishes at infinity.

This last point is decisive. An AKE-normal form cannot concentrate on the core while disappearing on the exterior. A nonzero core parallel form has a nonzero constant asymptotic trace and must match an exterior harmonic self-dual form or a Kähler frame variation.

## 4. The uniform one-level estimate

Let \(\mathcal Z_\varepsilon\) contain

* actual Kähler complex deformations;
* the two \(A_{1}\)-smoothing directions \(\zeta_\perp\);
* the associated hyperkähler frame changes;
* primitive exterior harmonic forms \(\sigma\), retained as a finite normal center;
* gauge directions before slicing.

Let \(x^\perp=(h,\alpha)^\perp\) be orthogonal to these modes, and let \(u_\parallel\) be the coefficient of the remaining Eguchi–Hanson mode \(\zeta_\parallel\). The required estimate is
\[
\boxed{
\|x^\perp\|_{\mathcal X_{\varepsilon,\delta}}
+|u_\parallel|
\le
C\left(
\|\mathbb L_\varepsilon x^\perp\|_{\mathcal Y_{\varepsilon,\delta}}
+
|\mathfrak m_{\mathrm{EH}}(u_\parallel)|
\right),
}
\tag{4.1}
\]
with \(C\) independent of \(\varepsilon\).

A contradiction proof has exactly three possible concentration locations.

1. **Exterior concentration.** A normalized sequence converges to an exterior kernel element. Projection away from Kodaira–Spencer and \(\sigma\) modes makes the limit zero.

2. **Core concentration.** Rescaling gives an Eguchi–Hanson kernel element. The two smoothing modes and parallel-form rotations have already been extracted; the remaining \(\zeta_\parallel\) coefficient is annihilated by (2.2). The limit is zero.

3. **Intermediate neck concentration.** Rescaling by the maximizing radius gives a homogeneous solution on \(\mathbb R^{4}/\mathbb Z_{2}\). The indicial gap \(0<\delta<2\), together with vanishing traces at both ends, makes this solution zero.

Thus (4.1) reduces the coupled problem to finitely many center variables.

## 5. The finite-dimensional AKE equation

For an Einstein metric \(g\), any compatible almost-Kähler form is a harmonic self-dual form. Choose a period-normalized analytic basis
\[
\Psi_1(g),\ldots,\Psi_{b^+}(g)
\]
of \(\mathcal H_g^{+}\), using the matched Hodge estimate implicit in (4.1), and write
\[
\Omega(g,c)=\sum_i c_i\Psi_i(g).
\]
Normalize its mean square to \(2\). The constant-length equation can then be encoded by the single real-analytic functional
\[
\boxed{
\mathcal A(g,c)
=
\int_M
\left(
|\Omega(g,c)|_g^{2}
-
\fint_M|\Omega(g,c)|_g^{2}\,dV_g
\right)^{2}dV_g.
}
\tag{5.1}
\]
Near \(\omega\), \(\mathcal A=0\) is exactly the almost-Kähler condition.

For a pure exterior normal form \(\sigma\),
\[
\Omega_t=\omega+t\sigma+O(t^{2}),
\]
and
\[
\mathcal A(g,\Omega_t)
=
t^{4}
\int_V
\left(
|\sigma|^{2}-\fint_V|\sigma|^{2}
\right)^{2}dV
+O(t^{5}).
\tag{5.2}
\]
The quadratic coefficient vanishes only for \(\sigma=0\). Indeed, constant \(|\sigma|\neq0\) would give a nowhere-vanishing holomorphic \(2\)-form of constant norm, while
\[
i\partial\bar\partial\log|\sigma|^{2}
\]
is tied to the Ricci form and cannot vanish when \(\lambda\neq0\).

Equivalently, on the finite-dimensional primitive harmonic space,
\[
\int_V
\left(
|\sigma|^{2}-\fint_V|\sigma|^{2}
\right)^{2}dV
\ge
c\,\|\sigma\|_{L^{2}}^{4}.
\tag{5.3}
\]
Uniformity as \(\varepsilon\to0\) follows from the absence of a self-dual localized Eguchi–Hanson harmonic form and the cone indicial gap.

There is a subtler entrance with \(\sigma=0\). If \(h_1\) is a Kodaira–Spencer Einstein field, Nagy’s second-order formula produces
\[
\Theta_2
=
\bar\partial\mathbf h_2+[h_1,h_1]^c,
\qquad
\bar\partial\Theta_2=0,\qquad
\delta\Theta_2=0.
\tag{5.4}
\]
When \(\Theta_2\neq0\), the metric and compatible form are Kähler to first order but torsion can first appear at second or higher order. Thus first-order identification of \(h_1\) with a complex deformation does not by itself settle the local problem.

## 6. How the local exclusion follows from a one-level analytic reduction

Estimate (4.1), the known real-analytic Einstein-modulo-obstructions maps on the fixed orbifold and ALE pieces, and the explicit one-\(A_{1}\) matching produce a finite-dimensional map on the real blow-up of the gluing parameter:
\[
\mathfrak K(v,\zeta,c,\varepsilon)=0.
\tag{6.1}
\]
Its components include

\[
\mathfrak K_{\mathrm{EH}}
=
C\,\mathcal R^+_{g_v}(p)\zeta+\text{higher terms},
\tag{6.2}
\]
the exterior Einstein Kuranishi projection, and the harmonic constant-length equation (5.1). The one-level geometry has no degenerate bubble tree, which is precisely the setting where Ozuch’s unresolved analyticity issue for general trees is absent.

If this reduction is real-subanalytic through \(\varepsilon=0\), any sequence of strict AKE zeros approaching the orbifold produces, by curve selection, an arc
\[
t\longmapsto (g(t),\Omega(t)),\qquad t>0,
\]
of strict AKE Einstein pairs converging to \((V,g_0,\omega_0)\).

Along the arc, the normalized Einstein action, hence the Weyl deficit,
\[
D(g)=\frac{\widehat S(g)^2}{16}-2\pi^2T_+(M),
\]
is constant. Step 83 gives zero \(W^{+}\)-concentration for the AKE arc and a Kähler–Einstein endpoint, so
\[
\lim_{t\downarrow0}D(g(t))=0.
\]
Therefore \(D(g(t))\equiv0\). But for every AKE pair,
\[
D(g(t))
=
T_{\mathrm{AK}}(g(t))
=
\int_M
\left(
|W_3^+|^2+\frac{3}{32}q^2
\right)dV.
\]
Hence \(q\equiv0\) and every pair on the arc is Kähler, contradicting strictness.

This uses only the local one-\(A_{1}\) reduction, not any global finiteness property of the compactified Einstein moduli.

## Decisive calculation

The most useful concrete target is the uniform estimate (4.1). Its only model input not already explicit in the supplied sources is the coupled Eguchi–Hanson classification
\[
\ker_{\delta}\mathbb L_{\mathrm{EH}}
=
\{\text{three hyperkähler metric variations}\}
\oplus
\{\text{three parallel self-dual form variations}\}
\oplus
\{\text{gauge}\},
\qquad 0<\delta<2,
\tag{7.1}
\]
together with the asymptotic trace map and the pairing
\[
\mathfrak m_{\mathrm{EH}}(\zeta)
=
C\mathcal R^+_{g_0}(p)\zeta
=
C\lambda
\frac{\langle\zeta,\omega_0\rangle}{2}\omega_0.
\tag{7.2}
\]
Once (7.1) is proved in the decoupled weighted spaces, the exterior/core/neck blow-up gives (4.1), the finite-dimensional real-analytic reduction follows, and the action-plus-no-concentration argument removes every possible higher-order AKE-normal entrance, including the tensor \(\Theta_2\) in (5.4).
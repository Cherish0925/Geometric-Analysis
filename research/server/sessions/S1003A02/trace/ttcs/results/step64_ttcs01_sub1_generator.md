# TTCS Independent Branch Record

```json
{
  "step_id": 64,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step64_diffuse_twist_AAD_and_SW_zeros.md",
    "Sessions/S1003A02/workspace/notes/step63_frame_twist_flux_and_AK_identity.md",
    "Sessions/S1003A02/workspace/notes/step40_nijenhuis_form_and_pointwise_exhaustion.md",
    "Sessions/S1003A02/workspace/notes/step43_w0_cotton_quadratic_law_and_debts.md",
    "Knowledge/objects/papers/Local-models-and-integrability-of-certain-almost-Kahler-4-manifolds--89a416df784a--79aaa9509e7d/object.md"
  ]
}
```

## Task

Starting from the verified frame-twist theorem and the Step-64 diffuse-twist template, seek a genuinely stronger route toward either a global lower bound or a closed cheap construction. The hard quantity is the harmonic ASD projection of t_J^-=(alpha wedge beta)^- for a smooth best-sign almost complex structure, while AAD controls only derivatives/amplitude of torsion and normalized SW spinors are singular at zeros. Develop precise mathematical possibilities: an identity or inequality coupling H^-(t_J^-) to the second AAD Bianchi equation; a relative/renormalized spinor formula that retains zero/Hopf charges without divergent normalization; or a construction scheme realizing a diffuse nearly harmonic twist with shrinking zero cores and small Ricci defect. Distinguish consequences that follow now from conjectural entrances. Aim for testable formulas or an explicit model, not general suggestions.

## Output

Four mathematical mechanisms sharpen the problem. The first gives an explicit harmonic-ASD test of the second AAD equation. The second replaces singular spinor normalization by smooth relative Chern forms. The third supplies an exact diffuse almost-Kähler family and clarifies what perturbative Einstein theory actually controls. The fourth gives an Einstein exceptional filling whose entire cost lies in its joining to the host.

## 1. A harmonic-ASD test of the second AAD equation

Assume initially that \((g,J,\Omega)\) is almost-Kähler, with constant scalar curvature \(s\). Write
\[
V_Z=\nabla_Z\Omega,\qquad
u=\frac14|\nabla\Omega|^2,\qquad
t^-=-(\vartheta\wedge J\vartheta)^-,
\]
where
\[
\nabla\Omega=\vartheta\otimes\phi-J\vartheta\otimes J\phi.
\]
Let \(h\) be any smooth harmonic ASD form. Regard \(h\) as a skew endomorphism, and define the \(\Lambda_J^{0,2}\)-valued one-form
\[
(\eta_h)_Z=V_{h(Z)}.
\]

The crucial algebraic contraction is
\[
\boxed{\quad
\sum_i\langle V_{Je_i},V_{h(e_i)}\rangle
=-4\langle t^-,h\rangle .
\quad}                                                     \tag{1.1}
\]
Indeed,
\[
\langle V_X,V_Y\rangle
=2\bigl[\vartheta(X)\vartheta(Y)+J\vartheta(X)J\vartheta(Y)\bigr],
\]
and an ASD endomorphism commutes with \(J\). Thus this test sees the **orientation and harmonic component of the twist**, rather than merely \(du\).

Pairing AAD’s second equation with \(\eta_h\), summing over an orthonormal frame, and using \(\kappa=s+6u\), gives the exact identity
\[
\boxed{\quad
s\,\langle \mathsf H^-(t^-),h\rangle_{L^2}
=\mathcal F_h-6\int_Mu\langle t^-,h\rangle\,d\mu ,
\quad}                                                     \tag{1.2}
\]
where
\[
\begin{aligned}
\mathcal F_h=\int_M\sum_i\bigl[
 &\langle(du\wedge e_i^\flat)'',V_{h(e_i)}\rangle
 -\langle V_{\rho_0(e_i)},V_{h(e_i)}\rangle\\
 &+\langle V_{\rho_*''(e_i)},V_{h(e_i)}\rangle
 +2\langle(\delta W_3^+)_{e_i},V_{h(e_i)}\rangle\\
 &+\langle\nabla_{Je_i}\rho_*'',V_{h(e_i)}\rangle
 +\langle(A_{e_i}^+)'',V_{h(e_i)}\rangle
\bigr]\,d\mu .
\end{aligned}                                               \tag{1.3}
\]
In particular, at \(s=-4\),
\[
4\langle \mathsf H^-(t^-),h\rangle
=6\int u\langle t^-,h\rangle-\mathcal F_h.                    \tag{1.4}
\]

This is a concrete identity coupling the requested harmonic projection to the second AAD equation. Taking \(h=\mathsf H^-(t^-)\) makes its left side \(4\|\mathsf H^-(t^-)\|_2^2\).

### The remaining analytic substance is an adjoint estimate

The curvature-derivative terms in (1.3) can all be integrated by parts. Their resulting tests involve
\[
\nabla\eta_h
=(\nabla V)\circ h+V\circ\nabla h,
\]
together with terms quadratic in \(V\). Consequently, the derivative-source portion satisfies an estimate of the form
\[
\begin{aligned}
|\mathcal F_h^{\rm der}|
\le C\bigl(\|W_3^+\|_2+\|\rho_*''\|_2+\sqrt P\bigr)
\bigl(&\||h|\,|\nabla^2\Omega|\|_2\\
 &+\||\nabla h|\,|\nabla\Omega|\|_2
 +\||h|\,|\nabla\Omega|^2\|_2\bigr).
\end{aligned}                                               \tag{1.5}
\]
No curvature derivative remains. Unlike the amplitude transport estimate, however, the test retains \(\nabla h\), hence the direction of the harmonic flux.

A useful representation of the same test comes from Maxwell stress. Define
\[
H_h(X,Y)
=\langle\iota_X\Omega,\iota_Yh\rangle
+\langle\iota_Y\Omega,\iota_Xh\rangle .
\]
Then
\[
\boxed{\qquad \operatorname{tr}H_h=0,\qquad \delta H_h=0.\qquad} \tag{1.6}
\]
To see this, apply the divergence identity for Maxwell stress to the harmonic form \(\Omega+h\). The individual SD and ASD stresses vanish pointwise; their cross term is \(H_h\). Thus harmonic ASD flux supplies a canonical TT tensor, without a choice of potential or gauge.

Equations (1.2) and (1.6) suggest a sharper comparison than an unrestricted second-jet estimate: the adjoints in (1.3) can be expressed through this TT tensor and its derivatives. The scientifically relevant question is whether their \(W_2/W_3\) components cancel, or are spectrally separated from the components financing
\[
\int u(4-5u)
\]
in the exact AK identity. A bound retaining their full norms can still reproduce the Goldberg balance. An improvement needs information about these **specific harmonic-flux tests**, not just a smaller constant in Cauchy–Schwarz.

There is also a useful geometric scale calculation. On a complex-hyperbolic KE host normalized by \(s=-4\), \(W^-=0\), so every harmonic ASD form satisfies
\[
\nabla^*\nabla h=\frac43h,\qquad
\int|\nabla h|^2=\frac43\int|h|^2.                            \tag{1.7}
\]
A diffuse exceptional representative therefore still changes direction on the Einstein length scale. Diffuse amplitude does not mean a slowly varying ASD direction. This is precisely the information absent from the \(du\)-only estimate.

## 2. Relative spinor Chern forms: finite harmonic flux, explicit Hopf charges

Let \(L=\det S^+\), let \(f_{\mathcal A}=-iF_{\mathcal A}\), and put
\[
\rho=|\Phi|^2,\qquad v=\Phi/\sqrt\rho
\]
on the complement of the spinor zero set. Define the Berry one-form
\[
\beta=-i\langle v,\nabla_{\mathcal A}v\rangle
=\frac{\operatorname{Im}\langle\Phi,\nabla_{\mathcal A}\Phi\rangle}{\rho}.
\]
The spinor line and its orthogonal line give the connection on
\(\Omega^\perp\simeq\operatorname{Hom}(\mathbb Cv,(\mathbb Cv)^\perp)\).
With the real-curvature convention used above,
\[
\boxed{\qquad
\gamma_J=f_{\mathcal A}-2d\beta
=R(\Omega)+t_J .
\qquad}                                                     \tag{2.1}
\]
This formula retains the determinant connection instead of attempting to replace the punctured \(J\) by a smooth unit field.

For isolated transverse zeros, \(\beta=O(r^{-1})\) and \(t_J=O(r^{-2})\). The twist is locally \(L^1\), although its \(L^2\) norm has the logarithmic behavior found in Step 64. Hence pairing with a smooth harmonic ASD form is finite. Moreover,
\[
\int_{\partial B_\epsilon}\beta\wedge h=O(\epsilon^2),
\]
so Stokes’ formula gives
\[
\boxed{\quad
\int_M\langle t_J^-,h\rangle\,d\mu
=2\pi\langle a^-,h\rangle
-\int_M\langle R(\Omega)^-,h\rangle\,d\mu .
\quad}                                                     \tag{2.2}
\]
This is a relative version of the frame-flux theorem. The harmonic flux survives even when the normalized field has infinite unweighted twist energy.

### A completely smooth regularization

For \(\delta>0\), set
\[
\beta_\delta
=\frac{\operatorname{Im}\langle\Phi,\nabla_{\mathcal A}\Phi\rangle}
       {\rho+\delta},
\qquad
w_\delta=\frac{\rho}{\rho+\delta},
\qquad
\gamma_\delta=f_{\mathcal A}-2d\beta_\delta.
\]
These are smooth globally, and \([\gamma_\delta]=2\pi a\). On \(\{\rho>0\}\),
\[
\boxed{\quad
\gamma_\delta^-
=w_\delta\bigl(R(\Omega)^-+t_J^-\bigr)
 +(1-w_\delta)f_{\mathcal A}^-
 -2(dw_\delta\wedge\beta)^- .
\quad}                                                     \tag{2.3}
\]
Thus, for every harmonic ASD \(h\),
\[
\begin{aligned}
2\pi\langle a^-,h\rangle
={}&\int w_\delta\langle R(\Omega)^-+t_J^-,h\rangle\\
 &+\int(1-w_\delta)\langle f_{\mathcal A}^-,h\rangle
 -2\int\langle(dw_\delta\wedge\beta)^-,h\rangle .
\end{aligned}                                               \tag{2.4}
\]
This partitions the flux among a weighted geometric twist, ASD determinant curvature in the small-amplitude region, and an amplitude-transition term. It does not introduce a divergent normalized-field norm.

For a transverse zero, the transition term paired with smooth \(h\) tends to zero; its elementary radial size is \(O(\delta\log(1/\delta))\). The difficult connection to Theorem N is now explicit: that theorem controls a \(\rho^2\)-weighted rotation, whereas (2.4) contains \(w_\delta t_J\) and the small-amplitude \(f_{\mathcal A}^-\) reservoir. A useful global estimate has to couple these two carriers through the actual SW equations.

### Hopf charges enter in degree four, not in (2.2)

Squaring (2.1) yields
\[
\boxed{\quad
\gamma_J\wedge\gamma_J-f_{\mathcal A}\wedge f_{\mathcal A}
=4d\bigl(\beta\wedge d\beta-\beta\wedge f_{\mathcal A}\bigr).
\quad}                                                     \tag{2.5}
\]
For a transverse zero, with orientations fixed consistently,
\[
q_z=\frac1{4\pi^2}\lim_{\epsilon\to0}
       \int_{\partial B_\epsilon(z)}\beta\wedge d\beta
\]
is its signed Hopf index. Thus the punctured Chern–Weil identity retains the zero charges while the divergent SD and ASD energies cancel in their signed difference.

There is an additional topological fact specific to the best-sign structures:
\[
\left\langle c_2(S^+),[M]\right\rangle
=\frac{a^2-(2\chi+3\tau)}4=0.                                \tag{2.6}
\]
This follows from
\[
p_1(\mathfrak{su}S^+)=c_1(L)^2-4c_2(S^+),
\qquad
\mathfrak{su}S^+\simeq\Lambda^+.
\]
Consequently, when all zeros are transverse and isolated,
\[
\sum_z q_z=0.                                               \tag{2.7}
\]

The local Hopf obstruction is therefore compatible with cancellation between different zeros. It does not require a nonzero total charge. But cancellation is spatially nonlocal: a rescaled unit-field texture transported through a tube of radius \(\epsilon\) and length \(L\) has the dimensional critical-energy scale \(L/\epsilon\). Pairing zero indices alone does not supply a low-energy repair. Formula (2.4) avoids that repair altogether.

For zero sets of other types, the corresponding relative current and transgression formulas require their actual local structure; the isolated transverse calculation cannot simply be substituted.

## 3. An exact diffuse AK family that changes the perturbative picture

There is a simple bulk model which is stronger than a formal torsion density.

Let \((g_0,J_0,\Omega_0)\) be KE with
\[
\operatorname{Ric}_{g_0}=-g_0,\qquad |\Omega_0|^2=2.
\]
Let \(v\) be a harmonic SD form pointwise orthogonal to \(\Omega_0\), for example the real part of a holomorphic \(2\)-form. Put
\[
f=|v|_{g_0}^2,\qquad
\Omega_\epsilon=\Omega_0+\epsilon v,\qquad
g_\epsilon=\left(1+\frac{\epsilon^2f}{2}\right)^{1/2}g_0.
\]
Because the Hodge star on \(2\)-forms is conformally invariant,
\[
d\Omega_\epsilon=0,\qquad
*_{g_\epsilon}\Omega_\epsilon=\Omega_\epsilon,\qquad
|\Omega_\epsilon|_{g_\epsilon}^2=2.
\]
Therefore \((g_\epsilon,J_\epsilon,\Omega_\epsilon)\) is an **exact smooth almost-Kähler family**.

Write \(g_\epsilon=e^{2w_\epsilon}g_0\), where
\[
w_\epsilon=\frac14\log\left(1+\frac{\epsilon^2f}{2}\right)
=\frac{\epsilon^2f}{8}+O(\epsilon^4).
\]
The conformal Ricci formula gives
\[
\operatorname{Ric}_{g_\epsilon}^{\circ}
=-2\bigl(\nabla^2w_\epsilon-dw_\epsilon\otimes dw_\epsilon\bigr)_0,
\]
and hence, on a fixed host,
\[
\boxed{\quad
P(g_\epsilon)
=\frac{\epsilon^4}{16}
 \int|\nabla^2_0 f|^2\,d\mu_{g_0}+O(\epsilon^6).
\quad}                                                     \tag{3.1}
\]
Meanwhile,
\[
\int|\nabla\Omega_\epsilon|^2\,d\mu_{g_\epsilon}
=\epsilon^2\int|\nabla v|^2\,d\mu_{g_0}+O(\epsilon^3).         \tag{3.2}
\]
Thus a linear estimate
\[
P\ge c\int|\nabla\Omega|^2
\]
cannot hold for all nearby AK pairs when \(v\) is nonparallel. The metric moves at order \(\epsilon^2\), while the almost-complex structure moves at order \(\epsilon\). An Einstein-operator estimate for metric variations alone misses this independent motion of \(J\).

The coefficient in (3.1) is directly computable. Since \(\operatorname{Ric}_{g_0}=-g_0\),
\[
\int|\nabla^2_0f|^2
=\frac34\int(\Delta f)^2+\int|df|^2.                          \tag{3.3}
\]
For \(v\) arising from a holomorphic \(2\)-form on this KE surface,
\[
\nabla^*\nabla v=2v,\qquad
\Delta f=4f-2|\nabla v|^2.
\]
Thus the leading defect is determined entirely by the amplitude variation of an explicit harmonic form.

### Why this does not yet carry exceptional flux

The family is homotopic through almost-complex structures to \(J_0\), and conformal change preserves harmonic SD/ASD decomposition. Therefore
\[
c_1(J_\epsilon)^-=0.
\]
The frame-flux identity gives
\[
\mathsf H^-(t_{J_\epsilon}^-)
=-\mathsf H^-(\rho_0^{J_\epsilon}),\qquad
\|\mathsf H^-(t_{J_\epsilon}^-)\|_2\le\sqrt{P(g_\epsilon)/2}.   \tag{3.4}
\]
It produces diffuse twist with inexpensive torsion, but its twist does not carry an independent exceptional harmonic class.

Also, its scalar-\(-4\) Yamabe representative is \(g_0\). The AK structure becomes a non-AK orthogonal structure after that normalization. This distinguishes a freely supplied AK field from the field supplied by the monopole equations at the Yamabe metric.

At the Step-64 scale, \(u\sim\epsilon^2\) and
\[
\epsilon^4\sim k/A.
\]
A generic member has \(P\sim\epsilon^4A\sim k\). Smaller cost would require both an unusually small amplitude-Hessian coefficient and a genuine change of harmonic twist class. Equation (3.4) shows that optimizing the bulk amplitude alone cannot accomplish the second requirement.

This exact family is nevertheless a valuable model: it isolates a real diffuse mechanism and identifies the topological information that it lacks.

## 4. An exact Einstein exceptional filling and a concrete joining problem

The unrestricted metric problem also has a route not organized around AK fields. A Euclidean Taub–Bolt–AdS metric provides an Einstein filling of the disk bundle with Euler number \(-1\).

Let \(\psi\) have period \(4\pi\), set
\[
\eta=d\psi+\cos\theta\,d\varphi,
\]
and define
\[
\begin{aligned}
g_{\rm TB}
&=\frac{dr^2}{V(r)}
 +(r^2-n^2)(d\theta^2+\sin^2\theta\,d\varphi^2)
 +4n^2V(r)\eta^2,\\
V(r)
&=\frac{r^2-2mr+n^2+
 \ell^{-2}(r^4-6n^2r^2-3n^4)}{r^2-n^2}.
\end{aligned}                                               \tag{4.1}
\]
It satisfies
\[
\operatorname{Ric}=-\frac3{\ell^2}g.
\]
Taking \(\ell^2=3\) gives \(s=-4\).

A smooth bolt at \(r=r_b>n\) requires
\[
V(r_b)=0,\qquad V'(r_b)=\frac1{2n},
\]
with
\[
r_b=\frac{\ell^2\pm
 \sqrt{\ell^4-48n^2\ell^2+144n^4}}{12n}.                     \tag{4.2}
\]
The mass \(m\) is then determined by \(V(r_b)=0\). The normalized circle connection \(\eta/2\) has Chern number \(-1\), so a compact cut \(r_b\le r\le R\) has the exceptional-cap topology. Its Ricci defect is exactly zero.

Thus exceptional topology by itself cannot price the cap through \(P\). The localized Chern–Weil formula necessarily records its geometric mismatch with the host.

That mismatch is explicit. On the cut \(r=R\), the intrinsic coefficients and principal curvatures are
\[
\begin{aligned}
a_R^2&=R^2-n^2,&
b_R^2&=4n^2V(R),\\
k_a&=\frac{R\sqrt{V(R)}}{R^2-n^2},&
k_b&=\frac{V'(R)}{2\sqrt{V(R)}}.
\end{aligned}                                               \tag{4.3}
\]
These four quantities define the filling’s metric/normal-derivative data.

For comparison, a complex-hyperbolic geodesic sphere at \(s=-4\) has
\[
a(t)=\frac{\sqrt6}{2}\sinh(t/\sqrt6),\qquad
b(t)=\frac{\sqrt6}{2}\sinh(t/\sqrt6)\cosh(t/\sqrt6),
\]
and
\[
k_a\longrightarrow\frac1{\sqrt6},\qquad
k_b\longrightarrow\frac2{\sqrt6}.                            \tag{4.4}
\]
The Taub–Bolt end instead has
\[
k_a,k_b\longrightarrow\frac1{\sqrt3}.                        \tag{4.5}
\]
Consequently, cutting both pieces farther out does not make their first jets agree.

A precise construction problem is therefore the connector functional
\[
\mathcal J(n,R,T)
=\inf_{\text{smooth matching collars}}
 \int_{\rm collar}|\operatorname{Ric}^{\circ}|^2\,d\mu,       \tag{4.6}
\]
where one end has data (4.3) and the other has the complex-hyperbolic sphere data at radius \(T\). The infimum can first be studied in the diagonal Bianchi-IX representation and then compared with collars without that symmetry.

Both the host and the exceptional filling have \(P=0\); all defect of the joined metric resides in this connector. A family with \(\mathcal J\to0\), realizable inside hosts containing the corresponding disjoint balls, would give genuine closed blow-up constructions. A positive connector estimate would instead explain why an Einstein cap cannot exploit the vanishing cost of its interior.

The exact external source topic here is **Euclidean Taub–Bolt–AdS metrics, smooth bolt regularity, and Einstein filling Dirichlet-to-Neumann data**. The model equations themselves make the comparison calculable.

---

The common scientific issue is now sharper. Large unweighted twist is not equivalent to large **harmonic** twist; spinor zero charges are not equivalent to harmonic degree-two flux; and a zero-cost exceptional interior is not equivalent to a zero-cost joining. Equations (1.2), (2.4), (3.4), and (4.6) separate these quantities explicitly. They supply four distinct places where new differential or geometric information can enter, without returning to the already exhausted pointwise curvature algebra.
# TTCS Independent Branch Record

```json
{
  "step_id": 41,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step41_symplectic_closure_bolt_layer_and_new_inputs.md",
    "Sessions/S1003A01/workspace/scripts/step41_symplectic_bolt_layer.py",
    "Sessions/S1003A01/workspace/data/step41/symplectic_bolt_layer.json",
    "Sessions/S1003A01/workspace/notes/step40_harmonic_class_compatibility_and_period_stiffness.md",
    "Sessions/S1003A01/workspace/notes/step10_rigorous_subthreshold_cell_and_O11.md"
  ]
}
```

## Task

Verify the central Step-41 mathematics in the note and code/data: (i) the cutoff-rotation proof that the certified zero-period cell is in the closure of smooth exact-collar subthreshold cells carrying nowhere-vanishing closed self-dual forms; (ii) the corrected cohomological formula for eta; (iii) the smooth bolt expansion f_p(r)^2=a^2p^2+kappa^2 r^2+... for f=|Omega|/sqrt2, the distinction ghat=f g=v^2 g, and the leading scalar-square/variance divergence. Re-derive the radial coefficient and exponent independently, check orbit-volume normalization and whether the p^{-2} law and coefficient formula are correct, and compare to the JSON values. Also check the exact conformal Chern-Gauss-Bonnet identity and the interpretation that this is not an additional cost for the original metric. Identify any unsupported global extension in the symplectic pure-blow-up statement. Return a direct mathematical verification memo with corrections, not process advice.

## Output

# Mathematical verification memo

## 1. Cutoff rotation and the symplectic approximation

Let \(D=\operatorname{diag}(h_1,h_2,h_3)\) be the diagonal profile and
\[
H_\epsilon=R(\theta)DR(\theta)^T,\qquad \theta=\epsilon\chi .
\]
Writing the self-dual solution in the rotating eigenframe as \(\psi=R^T\phi\), its radial ODE has the form
\[
\psi'
=
\left(\frac{2D}{\sqrt{\det D}}-\theta' A_{13}\right)\psi ,
\]
where \(A_{13}\) generates rotation in the collapsing/fibre plane. At \(\epsilon=0\), the collar Kähler solution is
\(\psi=(0,0,\phi_f)\). Linearizing the first component and integrating inward from its zero collar value gives
\[
\partial_\epsilon\psi_1(0)\big|_{\epsilon=0}
=
-\int \chi'(r)\,
\psi_+(0)\frac{\phi_f(r)}{\psi_+(r)}\,dr.
\]
Since
\[
p=\int_E\Omega=\pi\psi_1(0),
\]
this yields
\[
p'(0)=-\pi\int\chi'(r)\Phi(r)\,dr,\qquad
\Phi=\psi_+(0)\frac{\phi_f}{\psi_+}>0\quad(r>0).
\]
For a decreasing cutoff, \(\chi'\le0\) and \(\chi'<0\) on a nonempty interval, so \(p'(0)\ne0\). This derivation indeed removes any need to know the sign of \(H_{33}-H_{11}\). The JSON value
\[
\frac{p}{\epsilon}\longrightarrow -0.175376\ldots
\]
has the opposite orientation convention from the displayed positive integral; replacing \(\epsilon\) by \(-\epsilon\) reconciles them.

The geometric smoothness argument is sound:

* Near the bolt, \(\chi\equiv1\), so \(H_\epsilon\) is a constant \(SO(3)\) rotation of the diagonal bolt model. This is induced by a fixed \(SU(2)\) right translation and gives a smooth filling with the rotated collapsing circle.
* Near the outer attachment, \(\chi\equiv0\), so the metric and marked CH germ are unchanged.
* Between these regions every orbit is principal, and a smooth positive definite \(H_\epsilon(r)\) defines a smooth metric.
* The right translation is isotopic to the identity on the principal \(S^3\), so the resulting filling is the same oriented blow-up cell relative to the outer marking.

For the self-dual form, the invariant norm identity is
\[
\frac{|\Omega|^2}{2}
=
\frac{\psi^T D\psi}{\det D}.
\]
Thus on a principal orbit, \(\Omega=0\) exactly when \(\psi=0\). ODE uniqueness would then force \(\psi\equiv0\), contradicting its collar value. At the bolt,
\[
f(0):=\frac{|\Omega|}{\sqrt2}
=\frac{|p|}{\pi b^2}>0
\]
whenever \(p\ne0\). Hence \(\Omega_\epsilon\) is nowhere zero for every sufficiently small \(\epsilon\ne0\). Since it is closed and self-dual,
\[
d^*\Omega_\epsilon=-*d*\Omega_\epsilon=-*d\Omega_\epsilon=0,
\]
so it is harmonic; also \(\Omega_\epsilon\wedge\Omega_\epsilon>0\), making it symplectic.

The action conclusion follows from continuity in the metric two-jet. In fact the discrete symmetry
\[
S=\operatorname{diag}(-1,-1,1)
\]
sends \(\epsilon\) to \(-\epsilon\), so \(J(\epsilon)\) is even and
\[
J(\epsilon)=J(0)+O(\epsilon^2).
\]
The data
\[
0.9971304,\ 0.9960351,\ 0.9957613,\ 0.99569285
\]
are consistent with convergence to the cited \(J(0)\le0.995670030355131\).

Two artifact details remain distinct from the analytic argument:

1. The referenced base record `data/perp_area/x00.03_X128_d20.json` and the imported curvature modules are not supplied here, so the base enclosure \(0.995670030355131\) cannot be reconstructed from the present files alone.
2. If this record has the finite-jet outer attachment used in Step 10 rather than an already smoothed exact collar, the Step-10 smoothing construction is needed first. The strict margin survives smoothing, and the rotation support lies away from that smoothing region, so the existence result remains valid.

The script’s `smooth_step` uses a clipped variable. As a real function this is not literally the standard \(C^\infty\) step on the tiny intervals \(0<z<10^{-8}\) and \(1-10^{-8}<z<1\); floating underflow makes it numerically flat there. The proof concerns the usual unclipped piecewise \(e^{-1/z}\) construction. This distinction has no visible effect on the reported floating values.

## 2. Cohomological formula for \(\eta\)

Let \(K_X\) denote the pullback of the canonical class of the unblown host, and set
\[
A=K_X^2.
\]
For
\[
[\psi]=\pm2\pi K_X-\sum_i s_i\,\mathrm{PD}(E_i),
\qquad K_X\cdot E_i=0,\qquad E_i\cdot E_j=-\delta_{ij},
\]
one obtains
\[
[\psi]^2=4\pi^2A-\sum_i s_i^2
\]
and
\[
2\pi K_X\cdot[\psi]=\pm4\pi^2A.
\]
Therefore
\[
\eta
=
\frac{|2\pi K_X\cdot[\psi]|}
{\sqrt{4\pi^2A[\psi]^2}}
=
\left(1-\frac{\sum_i s_i^2}{4\pi^2A}\right)^{-1/2}.
\]
Its small-period expansion is
\[
\eta
=
1+\frac{\sum_i s_i^2}{8\pi^2A}
+O\!\left(\frac{(\sum_i s_i^2)^2}{A^2}\right).
\]
Thus the host pairing remains fixed, while the denominator changes quadratically. The Step-40 assertion that \(\eta\) stays exactly one is incorrect once exceptional periods open.

This formula uses \(K_X\) as the host class. If \(K_X\) were instead interpreted as the canonical class of the blown-up manifold, then \(K_X\cdot E_i\ne0\) and the displayed derivation would not apply.

There is also a scale conversion: the JSON period \(p\) is in the \(\operatorname{Ric}=-6g\) normalization. After passing to \(\widetilde g=6g\) and scaling the collar Kähler form accordingly, the period in the \(\operatorname{Ric}=-g\) formula is
\[
s=6p.
\]
Using the JSON \(p\) directly in the \(\eta\) expression would miss a factor \(36\) in its quadratic term.

## 3. Bolt expansion and the conformal factor

Near the bolt,
\[
g=dr^2+r^2\sigma_1^2+b^2(\sigma_2^2+\sigma_3^2)+O(r^2),
\qquad b^2=x_0.
\]
Take the orthonormal coframe
\[
e^0=dr,\qquad e^1=r\sigma_1,\qquad e^2=b\sigma_2,\qquad e^3=b\sigma_3.
\]
If \(\phi_1(0)=p/\pi\), self-duality gives
\[
\Omega_p
=
\frac{p}{\pi b^2}(e^{01}+e^{23})
+\text{terms vanishing at the bolt}.
\]
Consequently
\[
f_p(0)=\frac{|\Omega_p(0)|}{\sqrt2}
=\frac{|p|}{\pi b^2},
\qquad
a=\frac1{\pi b^2}.
\]

For the zero-period solution, \(\phi_3=c\,r^2+O(r^4)\), so its leading form is proportional to the orthogonal self-dual direction
\[
e^{03}+e^{12}.
\]
Writing its coefficient as \(\kappa r\), orthogonality of the two self-dual directions gives
\[
f_p(r)^2
=
a^2p^2+\kappa^2r^2+\cdots.
\]

For this particular rotation family one can sharpen the remainder stated in the note. The matrix symmetry
\[
M(-\epsilon)=S M(\epsilon)S,\qquad S=\operatorname{diag}(-1,-1,1),
\]
fixes the collar vector \(e_3\), sends \(p\) to \(-p\), and leaves
\[
Q=f^2=\frac{\psi^TD\psi}{\det D}
\]
unchanged. Since \(p(\epsilon)\) is odd and locally invertible, \(Q\) is even in \(p\). Smooth bolt invariance then gives
\[
\boxed{
f_p(r)^2
=
a^2p^2+\kappa^2r^2
+O(p^2r^2+r^4).
}
\]
The weaker remainder \(O(|p|r^2)\) is enough for the leading equivalence \(C_E/p^2\), but not by itself for the sharper \(O(|\log|p||)\) remainder later in the note. The evenness just established supplies the needed strengthening.

The resolving radius follows from
\[
a^2p^2\asymp\kappa^2r^2,
\]
hence
\[
r\asymp |p|.
\]
There is no \(\sqrt{|p|}\) layer.

The conformal normalization is also correct:
\[
\widehat g_p=f_pg_p=v_p^2g_p,
\qquad v_p=\sqrt{f_p}.
\]
Indeed, for a two-form in dimension four,
\[
|\Omega|_{v^2g}=v^{-2}|\Omega|_g,
\]
so \(v^2=f=|\Omega|_g/\sqrt2\) gives \(|\Omega|_{\widehat g}=\sqrt2\).

## 4. Radial scalar calculation: one displayed formula needs correction

Set
\[
A=ap,\qquad
v_0(r)=(A^2+\kappa^2r^2)^{1/4}.
\]
Since the bolt has codimension two,
\[
\Delta v=v''+\frac1r v'+O(r)v'.
\]
A direct calculation gives
\[
\boxed{
\frac{\Delta v_0}{v_0}
=
\frac{\kappa^2(4A^2+\kappa^2r^2)}
{4(A^2+\kappa^2r^2)^2}.
}
\]
Equivalently,
\[
\frac{\Delta v_0}{v_0}
=
\frac{\kappa^2\left(A^2+\frac14\kappa^2r^2\right)}
{(A^2+\kappa^2r^2)^2}.
\]

The Step-41 note instead displays
\[
\frac{\kappa^2(2A^2+\kappa^2r^2)}
{(A^2+\kappa^2r^2)^2},
\]
which is incorrect. At \(r=0\) it is twice the correct value, and for \(r\gg|A|/\kappa\) it gives \(r^{-2}\) instead of the correct \((4r^2)^{-1}\).

The subsequent integral \(7/32\), however, agrees with the corrected formula:
\[
\begin{aligned}
\int_0^\infty
\left(\frac{\Delta v_0}{v_0}\right)^2r\,dr
&=
\frac{\kappa^2}{16A^2}
\int_0^\infty
\frac{x(4+x^2)^2}{(1+x^2)^4}\,dx\\
&=
\frac{\kappa^2}{16A^2}\cdot\frac72\\
&=
\boxed{\frac{7\kappa^2}{32a^2p^2}}.
\end{aligned}
\]

### Orbit-volume normalization

Using
\[
\int_{S^3}\sigma_1\wedge\sigma_2\wedge\sigma_3=2\pi^2,
\]
the bolt expansion gives
\[
d\mu_g
=
r b^2\,dr\,\sigma_1\wedge\sigma_2\wedge\sigma_3+\cdots.
\]
After integrating the orbit,
\[
\boxed{dV_{\mathrm{radial}}=2\pi^2b^2r\,dr+\cdots.}
\]
Equivalently, the bolt area is \(\pi b^2\) and the normal angular integral is \(2\pi\). No factor of two is missing.

The conformal scalar formula is
\[
\widehat s
=
v^{-3}(-6\Delta v+s_gv),
\qquad
\widehat s^{\,2}d\mu_{\widehat g}
=
\left(s_g-6\frac{\Delta v}{v}\right)^2d\mu_g.
\]
The leading square therefore has coefficient
\[
\boxed{
C_E
=
36(2\pi^2b^2)\frac{7\kappa^2}{32a^2}.
}
\]
The smooth scalar term and the cross term contribute at most logarithmically because
\[
\frac{\Delta v_0}{v_0}\sim\frac1{4r^2}
\quad\text{for}\quad |p|\ll r\ll1,
\]
and hence
\[
\int_{|p|}^{r_0}\frac1{r^2}\,r\,dr
=O(|\log|p||).
\]
Using the strengthened even expansion of \(f_p^2\), the geometric and profile corrections change \(\Delta v/v\) by \(O(1)\). Thus
\[
\boxed{
\int\widehat s_p^{\,2}\,d\mu_{\widehat g_p}
=
\frac{C_E}{p^2}+O(|\log|p||).
}
\]

The scalar mean remains bounded because
\[
\int\widehat s\,d\mu_{\widehat g}
=
\int\left(6|\nabla v|^2+s_gv^2\right)d\mu_g
=
\int\left(6f|\nabla\log v|^2+s_gf\right)d\mu_g,
\]
and near \(p=0\), \(v\sim r^{1/2}\) gives
\[
|\nabla v|^2\,d\mu_g\sim \frac1r\cdot r\,dr=O(dr).
\]
Also \(V(\widehat g)=\int f^2d\mu_g\) stays bounded and tends to a positive value. Hence the scalar variance has the same leading coefficient:
\[
\operatorname{Var}(\widehat s_p)
=
\frac{C_E}{p^2}+O(|\log|p||).
\]

## 5. Agreement with the JSON data

The exact bolt coefficient is
\[
a=\frac1{\pi(0.03)}
=10.61032953945969,
\]
matching the JSON exactly. The sampled values
\[
6.5022400,\ 6.5022589,\ 6.5022643,\ 6.5022662
\]
support
\[
\kappa=6.5022662256.
\]
Substitution gives
\[
C_E
=
36(2\pi^2\cdot0.03)
\frac{7(6.5022662256)^2}
{32(10.6103295395)^2}
=
1.7513514537,
\]
again exactly the stored prediction.

The variance data are
\[
p^2\operatorname{Var}(\widehat s_p)
=
1.743363,\ 1.749155,\ 1.750725,\ 1.751030,
\]
which approach \(1.75135145\). The corresponding Chern–Gauss–Bonnet coefficient is
\[
\frac{C_E}{12}=0.1459459545,
\]
while the JSON gives
\[
p^2(P_{\widehat g}-P_g)
=
0.1452384,\ 0.1457521,\ 0.1458910,\ 0.1459185.
\]
This is the expected convergence.

The raw values `p2_times_Shat`
\[
574.63,\ 144.99,\ 37.56,\ 10.70
\]
are not yet near \(C_E\) because \(S(g_p)\approx4.657\times10^7\) is a large bounded background contribution. At the smallest sampled period,
\[
p^2S(g_p)\approx8.95,\qquad
p^2S(\widehat g_p)\approx10.70,
\]
and their difference is approximately \(1.75\). As \(p\to0\), the scaled bounded background tends to zero.

The resolved trapezoidal value of \(S(g_p)\) differs from `Sg_gauss` by about \(1211\), or \(2.6\times10^{-5}\) relatively. At the largest sampled period this is about \(0.9\%\) of \(S(\widehat g_p)-S(g_p)\), while at the smallest period it is about \(0.013\%\). The code uses the same resolved grid for both terms, so common quadrature effects largely cancel. The integration-by-parts agreement at \(1.8\times10^{-10}\) is a strong internal consistency test, though it uses the same radial quadrature.

## 6. Exact conformal Chern–Gauss–Bonnet identity

For a closed four-manifold,
\[
8\pi^2\chi(M)
=
\int\left(
|W|^2-\frac12|\operatorname{Ric}^\circ|^2+\frac{s^2}{24}
\right)d\mu.
\]
Let
\[
P(g)=\int|\operatorname{Ric}^\circ_g|^2\,d\mu_g,
\qquad
S(g)=\int s_g^2\,d\mu_g.
\]
Since \(\int|W|^2d\mu\) is conformally invariant in dimension four, subtraction for \(g\) and \(\widehat g\) gives exactly
\[
\boxed{
P(\widehat g)-P(g)
=
\frac{S(\widehat g)-S(g)}{12}.
}
\]
Because \(f_p>0\) for \(p\ne0\), \(\widehat g_p=f_pg_p\) is smooth, so the identity applies without singular terms. It also applies cellwise when the conformal factor equals one on the collar, since the two metrics agree there.

The data field `P_hat_minus_P_from_CGB` is unnormalized, whereas `P_over_8pi2` in `original_metric` is divided by \(8\pi^2\). In normalized notation,
\[
\frac{P(\widehat g)-P(g)}{8\pi^2}
=
\frac{S(\widehat g)-S(g)}{96\pi^2}.
\]

The interpretation in Step 41 is correct: \(g_p\) converges smoothly to the zero-period metric and its original Einstein action remains below the unit threshold, while \(\widehat g_p\) is a different metric whose conformal factor develops a resolving layer. The \(p^{-2}\) term is curvature energy of this almost-Kähler representative, not an extra term in \(J_6(g_p)\). No conformal identity transfers that divergent \(P(\widehat g_p)\) back to \(P(g_p)\).

There is a notation inconsistency in the note: after setting \(J=J_6/(8\pi^2)\), the sentence \(J(g_p)<8\pi^2\) should read either
\[
J_6(g_p)<8\pi^2
\quad\text{or}\quad
J(g_p)<1.
\]

## 7. Global pure-blow-up statement

For a fixed compact Kähler–Einstein host already equipped with finitely many disjoint marked CH regions, the global gluing is valid: the local forms equal the host Kähler form on every collar, so they assemble into a smooth closed self-dual form, and choosing each local period away from zero makes the assembled form nowhere zero.

The local Step-41 argument by itself does not establish an assertion for every pure-blow-up four-manifold. The supported quantifier is: pure blow-ups of the compact CH or ramified Kähler–Einstein hosts occurring in the established marked-site construction. An asymptotic strict sub-four coefficient additionally uses the earlier packing or covering construction that supplies sufficiently many disjoint marked sites and the corresponding global energy bookkeeping. Those global ingredients are referenced but not proved in the supplied Step-41 note or script.

Subject to that host construction and the outer-seam smoothing point above, the symplectic pure-blow-up extension is mathematically consistent. The local argument supplies no analogous global form for handle additions.
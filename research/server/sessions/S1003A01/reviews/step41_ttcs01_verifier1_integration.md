# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 41,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step41_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step41_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the central Step-41 mathematics in the note and code/data: (i) the cutoff-rotation proof that the certified zero-period cell is in the closure of smooth exact-collar subthreshold cells carrying nowhere-vanishing closed self-dual forms; (ii) the corrected cohomological formula for eta; (iii) the smooth bolt expansion f_p(r)^2=a^2p^2+kappa^2 r^2+... for f=|Omega|/sqrt2, the distinction ghat=f g=v^2 g, and the leading scalar-square/variance divergence. Re-derive the radial coefficient and exponent independently, check orbit-volume normalization and whether the p^{-2} law and coefficient formula are correct, and compare to the JSON values. Also check the exact conformal Chern-Gauss-Bonnet identity and the interpretation that this is not an additional cost for the original metric. Identify any unsupported global extension in the symplectic pure-blow-up statement. Return a direct mathematical verification memo with corrections, not process advice.

## Integrated Scientific Memo

# Step-41 mathematical verification memo

## 1. Cutoff rotation: the local closure theorem is valid

Write the diagonal metric profile as \(D=\operatorname{diag}(h_1,h_2,h_3)\) and rotate the collapsing/fibre plane:
\[
H_\epsilon=R(\epsilon\chi)D\,R(\epsilon\chi)^T,
\]
where \(\chi\equiv1\) near the bolt and \(\chi\equiv0\) near the exact complex-hyperbolic collar.

In the rotating eigenframe, the self-duality equation for the invariant potential coefficients has the form
\[
\psi'
=
\left(\frac{2D}{\sqrt{\det D}}-\epsilon\chi' A_{13}\right)\psi .
\]
At \(\epsilon=0\), the inward solution determined by the collar Kähler form is
\[
\psi=(0,0,\phi_f).
\]
Linearizing its first component and integrating inward gives
\[
\frac{d}{d\epsilon}\psi_1(0)\bigg|_{\epsilon=0}
=
-\int \chi'(r)\,
\psi_+(0)\frac{\phi_f(r)}{\psi_+(r)}\,dr.
\]
Since
\[
p=\int_E\Omega=\pi\psi_1(0),
\]
one obtains
\[
\boxed{
p'(0)=-\pi\int\chi'(r)\Phi(r)\,dr,
\qquad
\Phi(r)=\psi_+(0)\frac{\phi_f(r)}{\psi_+(r)}>0\quad(r>0).
}
\]

The endpoint terms in the integration by parts vanish: \(\chi=0\) at the collar, while \(\phi_f=O(r^2)\) at the bolt. Thus any decreasing nonconstant cutoff has \(p'(0)\neq0\), without requiring a pointwise sign for \(H_{33}-H_{11}\). The JSON value
\[
p/\epsilon\longrightarrow-0.175376\ldots
\]
uses the opposite rotation orientation from the sign displayed in the note; this affects only which sign of \(\epsilon\) gives positive period.

### Smoothness and topology

Near the bolt the rotation is constant. More precisely, the map
\[
(r,q)\longmapsto (r,q\,h(\epsilon\chi(r)))
\]
is a diffeomorphism equal to a fixed right translation near the bolt and to the identity near the collar. It transports the rotated compactification to the original marked blow-up cell. Hence \(g_\epsilon\) is smooth and has the unchanged exact-CH boundary germ. The collapsing circle is conjugated near the bolt, rather than literally fixed, but this does not change the relative diffeomorphism type.

On a principal orbit,
\[
\frac{|\Omega|^2}{2}
=\frac{\psi^TD\psi}{\det D},
\]
so \(\Omega=0\) iff \(\psi=0\). ODE uniqueness would then imply \(\psi\equiv0\), contradicting the nonzero collar value. At the bolt,
\[
\frac{|\Omega(0)|}{\sqrt2}
=\frac{|p|}{\pi b^2},
\]
so \(p\neq0\) also excludes a bolt zero. Therefore \(\Omega_\epsilon\) is nowhere vanishing for all sufficiently small \(\epsilon\neq0\). Since it is closed and self-dual, it is harmonic and
\[
\Omega_\epsilon\wedge\Omega_\epsilon=|\Omega_\epsilon|^2\,d\mu_{g_\epsilon}>0,
\]
hence symplectic.

Continuity of the curvature action in the metric two-jet, together with the strict certified margin at \(\epsilon=0\), gives
\[
J(g_\epsilon)<1
\]
for sufficiently small \(|\epsilon|\). A Klein symmetry sends \(\epsilon\mapsto-\epsilon\), so in fact
\[
J(\epsilon)=J(0)+O(\epsilon^2),\qquad
p(\epsilon)=p_1\epsilon+O(\epsilon^3).
\]
The JSON values agree with these parity laws and converge to the cited base action \(0.99567003\ldots\).

Thus the certified zero-period cell is indeed in the closure of smooth exact-collar, subthreshold cells carrying nowhere-vanishing closed self-dual forms.

### Artifact qualifications

The supplied bundle does not include the base record `data/perp_area/x00.03_X128_d20.json` or the imported curvature modules, so the numerical certificate \(J(g_*)\le0.995670030355131\) cannot be reconstructed from these files alone. If that record has only a finite-jet rather than already smooth outer attachment, the Step-10 collar smoothing must be applied first; its error tends to zero and the rotation can be supported away from the smoothing region.

The script’s clipped implementation of `smooth_step` is not literally the standard \(C^\infty\) step in the tiny clipped transition intervals. The theorem should use the unclipped piecewise \(e^{-1/z}\) cutoff. This does not materially affect the reported floating computation.

---

## 2. Correct cohomological formula for \(\eta\)

Let \(K_X\) mean the pullback of the host canonical class and set
\[
A=K_X^2.
\]
For
\[
[\psi]=\pm2\pi K_X-\sum_i s_i\,e_i,
\qquad e_i=\mathrm{PD}(E_i),
\]
with
\[
K_X\cdot e_i=0,\qquad e_i\cdot e_j=-\delta_{ij},
\]
one has
\[
[\psi]^2=4\pi^2A-\sum_i s_i^2
\]
and
\[
2\pi K_X\cdot[\psi]=\pm4\pi^2A.
\]
Consequently
\[
\boxed{
\eta
=
\frac{|2\pi K_X\cdot[\psi]|}
{\sqrt{4\pi^2A[\psi]^2}}
=
\left(1-\frac{\sum_i s_i^2}{4\pi^2A}\right)^{-1/2}.
}
\]
Thus
\[
\eta
=
1+\frac{\sum_i s_i^2}{8\pi^2A}
+O\!\left(\frac{(\sum_i s_i^2)^2}{A^2}\right).
\]
The host numerator stays fixed, but \(\eta\) does not remain exactly one once exceptional periods are nonzero.

Two qualifications are essential:

1. This formula uses the **pulled-back host class**. If \(K\) denotes the canonical class of the blown-up symplectic manifold, it has exceptional components, and its pairing changes linearly in \(|s_i|\), not quadratically. The same distinction matters for Seiberg–Witten basic classes. Any AKΓ or gauge-theoretic comparison must specify which class is being paired with \([\psi]\).

2. The JSON period \(p\) is in the \(\operatorname{Ric}=-6g\) normalization. In the \(\operatorname{Ric}=-g\) normalization,
\[
s_i=6p_i.
\]
Using \(p_i\) directly in the displayed formula would miss a factor \(36\) in the quadratic correction.

The Step-40 profile-scale class formula is also misstated. With \(\rho=-6\omega\),
\[
[\omega]=\frac{\pi}{3}\pi^*K_X,
\]
and a form with exceptional periods \(p_i=[\Omega]\cdot E_i\) has
\[
\boxed{
[\Omega]=\frac{\pi}{3}\pi^*K_X-\sum_i p_i\,e_i
}
\]
for the stated orientation convention, not \(\frac16K_X+\sum(t_i/\pi)e_i\).

---

## 3. Bolt expansion and the distinction between \(f\) and the conformal scale

Near the bolt,
\[
g=dr^2+r^2\sigma_1^2+b^2(\sigma_2^2+\sigma_3^2)+O(r^2),
\qquad b^2=x_0.
\]
Use the orthonormal coframe
\[
e^0=dr,\qquad e^1=r\sigma_1,\qquad e^2=b\sigma_2,\qquad e^3=b\sigma_3.
\]
For
\[
\Omega=\frac12d(\phi_i\sigma_i),
\qquad \phi_1(0)=\frac p\pi,
\]
the constant bolt component is
\[
\Omega_p(0)
=
\frac{p}{\pi b^2}(e^{01}+e^{23}),
\]
hence
\[
f_p(0):=\frac{|\Omega_p(0)|}{\sqrt2}
=\frac{|p|}{\pi b^2}.
\]
Therefore
\[
\boxed{a=\frac1{\pi b^2}.}
\]

For the zero-period solution,
\[
\phi_3=c_3r^2+O(r^4),
\]
but division by the collapsing factor \(a_1a_2\sim rb\) makes the corresponding orthonormal two-form component linear:
\[
A_3=\frac{\phi_3}{a_1a_2}
=\kappa r+O(r^3).
\]
It lies in the self-dual direction \(e^{03}+e^{12}\), orthogonal to the constant \(e^{01}+e^{23}\) component. Thus
\[
f_p(r)^2
=
a^2p^2+\kappa^2r^2+\cdots.
\]

For this rotation family, Klein parity makes \(f^2\) even in \(p\). The correct sharpened expansion is therefore
\[
\boxed{
f_p(r)^2
=
a^2p^2+\kappa^2r^2
+O(p^2r^2+r^4).
}
\]
The note’s weaker \(O(|p|r^2)\) term is unnecessary and, if genuinely present, would be incompatible with the claimed \(O(|\log|p||)\) remainder in the scalar-square asymptotic.

Balancing the two leading terms gives
\[
r\asymp \frac{a}{\kappa}|p|,
\]
so the resolving layer has radius \(O(|p|)\).

The almost-Kähler metric is
\[
\boxed{
\widehat g_p=f_pg_p=v_p^2g_p,\qquad v_p=\sqrt{f_p}.
}
\]
Indeed, \(|\Omega|_{v^2g}=v^{-2}|\Omega|_g\), so choosing \(v^2=f=|\Omega|_g/\sqrt2\) gives \(|\Omega|_{\widehat g}=\sqrt2\).

The numerical values are consistent:
\[
a=\frac1{\pi(0.03)}=10.61032953945969,
\]
exactly as in the JSON, and the samples converge to
\[
\kappa\simeq6.50226623.
\]

---

## 4. Correct radial coefficient, exponent, and orbit normalization

Put
\[
A=ap,\qquad
v_0(r)=(A^2+\kappa^2r^2)^{1/4}.
\]
Because the bolt has codimension two,
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

This corrects the Step-41 display
\[
\frac{\kappa^2(2A^2+\kappa^2r^2)}
{(A^2+\kappa^2r^2)^2},
\]
which is wrong. For example, at \(A=0\), the correct asymptotic is
\[
\frac{\Delta\sqrt r}{\sqrt r}=\frac1{4r^2},
\]
not \(r^{-2}\).

The integral stated after the erroneous display is nevertheless correct:
\[
\begin{aligned}
\int_0^\infty
\left(\frac{\Delta v_0}{v_0}\right)^2r\,dr
&=
\frac{\kappa^2}{16A^2}
\int_0^\infty
\frac{x(4+x^2)^2}{(1+x^2)^4}\,dx\\
&=
\boxed{\frac{7\kappa^2}{32a^2p^2}}.
\end{aligned}
\]

### Orbit-volume factor

With
\[
\int_{S^3}\sigma_1\wedge\sigma_2\wedge\sigma_3=2\pi^2,
\]
the bolt volume form is
\[
d\mu_g
=
rb^2\,dr\,\sigma_1\wedge\sigma_2\wedge\sigma_3+\cdots.
\]
After orbit integration,
\[
\boxed{
dV_{\mathrm{radial}}
=
2\pi^2b^2\,r\,dr+\cdots.
}
\]
Equivalently, \(\operatorname{Area}_g(E)=\pi b^2\), multiplied by the normal angular factor \(2\pi r\,dr\). The normalization in the coefficient \(C_E\) is correct.

For \(\widehat g=v^2g\) in dimension four,
\[
\widehat s=v^{-3}(-6\Delta_gv+s_gv),
\]
and
\[
\widehat s^{\,2}d\mu_{\widehat g}
=
\left(s_g-6\frac{\Delta_gv}{v}\right)^2d\mu_g.
\]
Therefore
\[
\boxed{
\int\widehat s_p^{\,2}\,d\mu_{\widehat g_p}
=
\frac{C_E}{p^2}+O(|\log|p||),
}
\]
where
\[
\boxed{
C_E
=
36(2\pi^2b^2)\frac{7\kappa^2}{32a^2}.
}
\]

The \(p^{-2}\) exponent follows directly from codimension-two scaling:
\[
\left(\frac{\Delta v}{v}\right)^2\sim |p|^{-4},
\qquad
r\,dr\sim |p|^2,
\]
inside a layer \(r\sim|p|\). The cross term with the bounded background scalar is logarithmic because outside the core
\[
\frac{\Delta v}{v}\sim\frac1{4r^2},
\qquad
\int_{|p|}^{r_0}\frac1{r^2}r\,dr=O(|\log|p||).
\]

The note’s explanation of a possible \(p^{-1}\) law should be refined. Merely confusing \(f\) with \(v=\sqrt f\) changes the radial coefficient but not the dimensional \(p^{-2}\) exponent. A \(p^{-1}\) law instead results from incorrectly treating the norm of the zero-period form as quadratic in \(r\), i.e. confusing the potential coefficient
\[
\phi_3=O(r^2)
\]
with the orthonormal form component
\[
\phi_3/(a_1a_2)=O(r).
\]
That error produces a fictitious model \(f^2\sim p^2+r^4\) and layer \(r\sim\sqrt{|p|}\).

The scalar mean and volume remain bounded:
\[
\int\widehat s\,d\mu_{\widehat g}
=
\int\left(6|\nabla v|^2+s_gv^2\right)d\mu_g
=
\int\left(6f|\nabla\log v|^2+s_gf\right)d\mu_g,
\]
while
\[
V(\widehat g)=\int f^2\,d\mu_g.
\]
Hence subtracting the bounded mean-square term does not change the leading coefficient:
\[
\operatorname{Var}(\widehat s_p)
=
\frac{C_E}{p^2}+O(|\log|p||).
\]

---

## 5. Comparison with the JSON

Using
\[
b^2=0.03,\qquad
a=10.61032953945969,\qquad
\kappa=6.5022662255876895,
\]
gives
\[
C_E
=
36(2\pi^2\cdot0.03)
\frac{7(6.5022662256)^2}{32(10.6103295395)^2}
=
1.7513514537,
\]
exactly the stored prediction.

The measured values
\[
p^2\operatorname{Var}(\widehat s_p)
=
1.743363,\ 1.749155,\ 1.750725,\ 1.751030
\]
converge to \(1.75135145\), supporting both the exponent and coefficient.

Likewise,
\[
\frac{C_E}{12}=0.1459459545,
\]
while the JSON reports
\[
p^2(P(\widehat g_p)-P(g_p))
=
0.1452384,\ 0.1457521,\ 0.1458910,\ 0.1459185.
\]

The stored values `p2_times_Shat` are not themselves expected to approach \(C_E\) at these periods because \(\int s_{g_p}^2d\mu_{g_p}\approx4.657\times10^7\) is a large but bounded background. The difference \(S(\widehat g_p)-S(g_p)\), or the scalar variance, isolates the singular contribution.

The resolved trapezoidal and Gauss values of \(S(g_p)\) differ by about \(1.2\times10^3\), only \(2.6\times10^{-5}\) relatively. This explains part of the finite-grid floor in the smallest-\(p\) residuals. The integration-by-parts check at relative error \(1.8\times10^{-10}\) is a strong internal consistency test, although it uses the same radial discretization.

---

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
Since the Weyl energy is conformally invariant in dimension four, subtracting the two Chern–Gauss–Bonnet formulas gives
\[
\boxed{
P(\widehat g)-P(g)
=
\frac{S(\widehat g)-S(g)}{12}.
}
\]
For \(p\neq0\), \(f_p>0\), so \(\widehat g_p=f_pg_p\) is smooth and no singular correction is present. On a cell, the same identity applies by gluing to the unchanged collar, where \(f\equiv1\).

Thus
\[
P(\widehat g_p)-P(g_p)
\sim\frac{C_E}{12p^2}.
\]
This divergence belongs to the almost-Kähler conformal representative \(\widehat g_p\), not to the original metric \(g_p\). The original metrics converge smoothly to \(g_*\) and retain their subthreshold Einstein action. Any lower estimate applied to \(\widehat g_p\) must include the conformal conversion term before it can say anything about \(g_p\).

There is a normalization typo in the note. Since it defines \(J=J_6/(8\pi^2)\), the statement should be either
\[
J(g_p)<1
\]
or
\[
J_6(g_p)<8\pi^2,
\]
not \(J(g_p)<8\pi^2\).

---

## 7. Exact scope of the global symplectic statement

The local result supports the following global assertion:

> For a fixed compact locally complex-hyperbolic host equipped with finitely many disjoint marked exact-CH balls, replacing those balls by the rotated blow-up cells produces a closed metric carrying a global closed, self-dual, nowhere-vanishing form. The local form and host Kähler form coincide on each collar, so they glue exactly. Taking every exceptional period nonzero gives a symplectic form, and the per-cell action approaches the certified zero-period cost.

Combined with the earlier cover/packing and global energy bookkeeping, this yields the pure-blow-up asymptotic upper construction within the conformally almost-Kähler symplectic subclass.

The following broader readings are not justified by Step 41 alone:

1. **Arbitrary pure blow-ups.** The construction applies only to hosts for which the required disjoint exact-CH marked regions and global gluing setup have been established.

2. **General “ramified Kähler–Einstein hosts.”** A general Kähler–Einstein surface is not locally complex hyperbolic and need not contain exact-CH balls. A ramified or cone metric is not automatically an admissible smooth host. Such an extension requires a separate local model and seam analysis.

3. **Handle additions.** The local form construction gives no global symplectic extension across the handle surgeries. The note correctly excludes this case.

Accordingly, the central local Step-41 theorem is sound, the \(\eta\) formula is correct for the pulled-back host class, and the \(p^{-2}\) law and coefficient are correct. The principal mathematical correction is the displayed formula for \(\Delta v/v\); the principal scope correction is that the global symplectic result is restricted to the previously established locally-CH pure-blow-up host construction.
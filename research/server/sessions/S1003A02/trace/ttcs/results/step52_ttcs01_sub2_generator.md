# TTCS Independent Branch Record

```json
{
  "step_id": 52,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step52_residual_norm_selection_absorption.md",
    "Sessions/S1003A02/workspace/notes/step51_residual_entry_link_charges_and_kahler_recovery.md",
    "Knowledge/objects/papers/The-long-time-behavior-of-fourth-order-curvature-flows--5b1863f1c7b9--f1cab1a2d745/object.md"
  ]
}
```

## Task

The entry programme for minimizing sequences of P(g)=∫|Ric°|² on closed four-manifolds now hinges on Lemma 52.KS in the attached note: an own-scale concentration lemma for the energy-radius-weighted (frozen-weight) gradient flow of P — lifespan ≥ c1 in own-scale time, two-sided comparability of the energy radius, Sobolev persistence — the analogue of Kuwert–Schätzle's lemma for Willmore flow. P is in Bour's strongly parabolic class (a=b=0) but its gradient dissipates only the Ricci part; the Weyl energy must be controlled through the Pfaffian transgression and the Bianchi system δW ~ ∇Ric. Produce the strongest concrete proof architecture you can: the localized energy identity with cutoffs (exact form of d/dt ∫φ|Rm|² or of a better localized quantity), interpolation inequalities replacing Kuwert–Schätzle's, where the Sobolev constant enters, and how the weight's own-scale derivatives enter. If you believe the lemma is false, give a precise counter-mechanism (e.g. Weyl-energy transfer through necks at zero Ricci dissipation) and the weakest replacement that still yields a Palais–Smale minimizing sequence in the sense (PS_ε). Also propose an alternative selection mechanism (not a sixth-order regularization) if you see one that avoids flow lifetime altogether.

## Output

The strongest entry point is to use the four-dimensional affine relation between the Ricci-deviation energy and the total curvature energy. In the normalization used in the Step-51 and Step-52 notes, with \(E=\mathrm{Ric}^\circ\),

\[
P(g)=\int_M |E|^2\,d\mu_g,
\qquad 
F(g)=\int_M |\mathrm{Rm}|^2\,d\mu_g,
\]

one has

\[
F(g)=8\pi^2\chi(M)+\frac52 P(g).
\]

Indeed,

\[
|\mathrm{Rm}|^2=|W|^2+2|E|^2+\frac{s^2}{24},
\]

and the Euler form is

\[
\Omega_E=\frac1{8\pi^2}\Bigl(|W|^2-\frac12|E|^2+\frac{s^2}{24}\Bigr)d\mu,
\]

so

\[
|\mathrm{Rm}|^2d\mu=8\pi^2\Omega_E+\frac52 |E|^2d\mu.
\]

Consequently

\[
\operatorname{grad}F=\frac52 Q,
\]

and the frozen-weight flow

\[
\partial_t g=-wQ
\]

is the same as the weighted fourth-order curvature flow

\[
\partial_t g=-\frac25 w\,\operatorname{grad}F.
\]

This gives the exact global dissipation law

\[
\frac{d}{dt}F(g(t))
=-\frac52\int_M w|Q|^2d\mu,
\qquad
\frac{d}{dt}P(g(t))
=-\int_M w|Q|^2d\mu.
\]

The Weyl part is therefore globally tied to \(P\); locally it can move only through Pfaffian transgression and through the parabolic flux terms in the curvature evolution. This is the right place to build the Kuwert–Schätzle type argument.

---

## 1. Exact localized identity via Euler-form transgression

Let \(\varphi\) be a smooth cutoff. Write

\[
e=|\mathrm{Rm}|^2.
\]

The pointwise identity

\[
e\,d\mu=8\pi^2\Omega_E+\frac52 |E|^2d\mu
\]

gives

\[
\frac{d}{dt}\int_M \varphi e\,d\mu
=
8\pi^2\frac{d}{dt}\int_M \varphi \Omega_E
+\frac52\frac{d}{dt}\int_M \varphi |E|^2d\mu.
\]

For the Euler form there is an exact Chern–Weil transgression. Let \(\omega\) be the Levi-Civita connection and \(\Omega\) its curvature two-form. The Pfaffian/Euler form is

\[
\Omega_E=\frac1{32\pi^2}\epsilon_{abcd}\,\Omega^{ab}\wedge\Omega^{cd}.
\]

For a metric variation \(h=\partial_t g\), the variation of the connection is

\[
\dot\omega^{ab}_i
=
\frac12\left(
\nabla^a h^b{}_i+\nabla^b h^a{}_i-\nabla_i h^{ab}
\right),
\]

and

\[
\frac{d}{dt}\Omega_E=d\Theta(g;h),
\]

where

\[
\Theta(g;h)
=
\frac1{16\pi^2}\epsilon_{abcd}\,
\dot\omega^{ab}\wedge\Omega^{cd}.
\]

Hence

\[
\frac{d}{dt}\int_M \varphi \Omega_E
=
\int_M d\varphi\wedge \Theta(g;h).
\]

For the \(P\)-density, define the local variational current \(\mathcal J_P\) by the identity

\[
\frac{d}{dt}\int_M \varphi |E|^2d\mu
=
-\int_M \varphi w|Q|^2d\mu
+
\mathcal R_P(\varphi,wQ,g)
+
\int_M \varphi\,\mathcal L_X(|E|^2d\mu),
\]

where \(X\) is the DeTurck vector field and \(\mathcal R_P\) is the integration-by-parts remainder supported where \(\varphi\) varies. In harmonic coordinates, \(\mathcal R_P\) is a sum of terms of the form

\[
\int (\nabla\varphi)*\mathcal A_1(h,E,\nabla E)
+
\int (\nabla^2\varphi)*\mathcal A_2(h,E),
\]

with \(h=-wQ+\mathcal L_Xg\). Thus the exact localized energy identity is

\[
\boxed{
\begin{aligned}
\frac{d}{dt}\int_M \varphi |\mathrm{Rm}|^2d\mu
&=
-\frac52\int_M \varphi w|Q|^2d\mu
\\
&\quad
+\frac52\mathcal R_P(\varphi,wQ,g)
+8\pi^2\int_M d\varphi\wedge\Theta(g;-wQ+\mathcal L_Xg)
\\
&\quad
+\int_M \varphi\,\mathcal L_X(|\mathrm{Rm}|^2d\mu).
\end{aligned}
}
\]

This identity is useful because it separates the true dissipation, the Pfaffian flux, and the \(P\)-current flux. The only terms that can move local curvature energy without decreasing \(P\) are the two flux terms and the DeTurck transport term.

---

## 2. Coercive parabolic form of the same identity

For proving an own-scale lifespan and radius-comparability statement, the exact transgression identity should be combined with the parabolic curvature evolution. Since the flow is a weighted version of the \(L^2\)-curvature flow, the curvature tensor satisfies, schematically but with the correct principal structure,

\[
\partial_t \mathrm{Rm}
=
-\frac25 w\Delta^2\mathrm{Rm}
+
\frac25\nabla^2 w * \nabla^2\mathrm{Rm}
+
\frac25\nabla w * \nabla^3\mathrm{Rm}
+
\frac25 w\bigl(
\nabla^2\mathrm{Rm}*\mathrm{Rm}
+
\nabla\mathrm{Rm}*\nabla\mathrm{Rm}
+
\mathrm{Rm}^{*3}
\bigr)
+
\text{lower commutators}.
\]

After multiplying by \(\varphi\,\mathrm{Rm}\), integrating, and integrating by parts, one obtains the coercive local inequality

\[
\boxed{
\begin{aligned}
\frac12\frac{d}{dt}\int \varphi e
&+
c_0\int \varphi w|\Delta\mathrm{Rm}|^2
\\
&\le
C\int \varphi w\bigl(
|\nabla\mathrm{Rm}|^2e+e^2
\bigr)
\\
&\quad
+C\int \varphi\bigl(
|\nabla^2w|\,e
+
|\nabla w|\,|\mathrm{Rm}|\,|\nabla\mathrm{Rm}|
\bigr)
\\
&\quad
+C\int_{\operatorname{supp}|\nabla\varphi|}
w\bigl(
|\Delta\mathrm{Rm}|\,|\nabla\mathrm{Rm}|
+
|\nabla\mathrm{Rm}|^2
+
e^{3/2}
\bigr)
\\
&\quad
+C\int_{\operatorname{supp}|\nabla\varphi|}
\bigl(
|\nabla w|\,e
+
w|\mathrm{Rm}|\,|\nabla\mathrm{Rm}|
\bigr)
\\
&\quad
+C\int \varphi\bigl(
|X|\,|\nabla e|+|\nabla X|e
\bigr).
\end{aligned}
}
\]

Here \(e=|\mathrm{Rm}|^2\), \(c_0,C>0\) are universal, and \(w\) is the frozen weight. The term \(|\Delta\mathrm{Rm}|^2\) may be replaced by \(|\nabla^2\mathrm{Rm}|^2\) up to curvature-commutator terms that are absorbed by the nonlinear terms when local energy is small.

The DeTurck transport term can be handled in either of two ways:

1. Work in the pulled-back gauge where the DeTurck vector field is absorbed into diffeomorphisms.  
2. Keep the term and use that, in the frozen-weight step, the background is chosen at the beginning of the step, so \(X\) is initially zero and remains small in own-scale norm for short own-scale time.

---

## 3. Kuwert–Schätzle-type interpolation inequalities in dimension four

The local Sobolev constant enters through the dimension-critical interpolation estimates. Rescale a ball \(B(x,r)\) to unit size and suppose the frozen weight satisfies

\[
c\le w\le C,
\qquad
|\nabla^j w|\le C_j,
\]

which is exactly what one gets from smoothing \(r_\varepsilon^4\) at a fixed fraction of its own scale. Let

\[
E_B=\int_B e\,d\mu.
\]

Assume the local scale-invariant Sobolev constant on \(B\) is at most \(C_S\). The needed inequalities are the fourth-order analogues of the Willmore-flow inequalities.

### 3.1. \(L^4\) curvature absorption

For a tensor \(T\) on a unit ball with local Sobolev constant \(C_S\),

\[
\|T\|_{L^4}^2
\le
C_S\left(\|\nabla T\|_{L^2}+\|T\|_{L^2}\right)\|T\|_{L^2}.
\]

Taking \(T=\mathrm{Rm}\) and using the interpolation

\[
\|\nabla\mathrm{Rm}\|_{L^2}^2
\le
\|\mathrm{Rm}\|_{L^2}\,\|\Delta\mathrm{Rm}\|_{L^2}
+
C\|\mathrm{Rm}\|_{L^4}^2\|\mathrm{Rm}\|_{L^2}
\]

gives, after absorption when \(E_B\) is small,

\[
\boxed{
\int_B e^2
\le
\frac1{32}\int_B w|\Delta\mathrm{Rm}|^2
+
C(C_S)E_B^2,
}
\]

provided

\[
E_B\le \varepsilon_0(C_S).
\]

Scaling back to radius \(r\),

\[
r^4\int_{B(x,r/2)}|\mathrm{Rm}|^4
\le
\frac1{32}\int_{B(x,r)}w|\Delta\mathrm{Rm}|^2
+
C(C_S)\left(\int_{B(x,r)}|\mathrm{Rm}|^2\right)^2.
\]

### 3.2. Mixed gradient-curvature term

Similarly,

\[
\int_B |\nabla\mathrm{Rm}|^2e
\le
\|\nabla\mathrm{Rm}\|_{L^4}^2\|e\|_{L^2}.
\]

Using the local Sobolev estimate for \(\nabla\mathrm{Rm}\),

\[
\|\nabla\mathrm{Rm}\|_{L^4}^2
\le
C_S\|\nabla^2\mathrm{Rm}\|_{L^2}^{1/2}
\|\nabla\mathrm{Rm}\|_{L^2}^{3/2}
+
C_S\|\nabla\mathrm{Rm}\|_{L^2}^2,
\]

and then interpolating \(\|\nabla\mathrm{Rm}\|_{L^2}\) between \(\|\mathrm{Rm}\|_{L^2}\) and \(\|\Delta\mathrm{Rm}\|_{L^2}\), one obtains

\[
\boxed{
\int_B |\nabla\mathrm{Rm}|^2e
\le
\frac1{32}\int_B w|\Delta\mathrm{Rm}|^2
+
C(C_S)E_B^2,
}
\]

again for \(E_B\le \varepsilon_0(C_S)\).

### 3.3. Weight-derivative terms

If \(w\) is a smoothed version of \(r_\varepsilon^4\), then in rescaled units

\[
|\nabla w|\le C,
\qquad
|\nabla^2w|\le C.
\]

Thus

\[
\int_B |\nabla^2w|e
\le
C E_B,
\]

and

\[
\int_B |\nabla w|\,|\mathrm{Rm}|\,|\nabla\mathrm{Rm}|
\le
C E_B^{1/2}\|\nabla\mathrm{Rm}\|_{L^2}
\le
\frac1{32}\int_B w|\Delta\mathrm{Rm}|^2
+
C E_B.
\]

These are lower-order terms. They are harmless as long as \(E_B\) is small and the time interval in own-scale units is chosen short.

### 3.4. Annular flux terms

For a cutoff \(\varphi\) with \(\varphi=1\) on \(B_{r/2}\) and \(\operatorname{supp}\varphi\subset B_r\),

\[
|\nabla\varphi|\le Cr^{-1}.
\]

After rescaling to \(r=1\), the annular terms are controlled by

\[
\int_{B_1\setminus B_{1/2}}
w|\Delta\mathrm{Rm}|\,|\nabla\mathrm{Rm}|
\le
\frac1{32}\int_{B_1}w|\Delta\mathrm{Rm}|^2
+
C\int_{B_1\setminus B_{1/2}}|\nabla\mathrm{Rm}|^2,
\]

and

\[
\int_{B_1\setminus B_{1/2}}|\nabla\mathrm{Rm}|^2
\le
E_{B_1}^{1/2}
\left(\int_{B_1}|\Delta\mathrm{Rm}|^2\right)^{1/2}.
\]

Thus, if the annulus has small energy, these terms are also absorbed. In a point-picking argument one chooses the first bad point and radius so that the surrounding annuli still have energy controlled by the definition of \(r_\varepsilon\). This is precisely the role of the Lipschitz property of \(r_\varepsilon\).

---

## 4. How these estimates prove the own-scale persistence statement

Assume that at the beginning of a frozen step the energy radius at a point is \(r\). Rescale so that \(r=1\). Suppose

\[
\int_{B(x,1)}|\mathrm{Rm}|^2\le \varepsilon_1.
\]

Choose \(\varepsilon_1\) so small that all absorption constants above are below \(1/16\). Integrate the coercive local inequality from \(0\) to \(t\le c_1\). One obtains

\[
\sup_{0\le s\le t}
\int_{B(x,1/2)}|\mathrm{Rm}|^2(\cdot,s)
+
\int_0^t\int_{B(x,1/2)}w|\Delta\mathrm{Rm}|^2
\le
2\varepsilon_1
+
C c_1
+
C\int_0^t\int_{B(x,1)\setminus B(x,1/2)}e.
\]

Choosing \(c_1\) small compared with \(\varepsilon_1\) and using the annular energy control gives

\[
\int_{B(x,1/2)}|\mathrm{Rm}|^2(\cdot,s)
\le
\frac32\varepsilon_1,
\qquad
0\le s\le c_1.
\]

Hence the energy radius cannot drop below \(1/2\) in own-scale time \(c_1\). This gives the lower comparability

\[
r_\varepsilon(g(s),x)\ge \frac12 r_\varepsilon(g(0),x).
\]

For the upper side, one uses the same identity on a larger ball. If the radius at \(x\) were to increase from \(1\) to \(2\) before time \(c_1\), then the energy in \(B(x,2)\) would have to fall below \(\varepsilon\). The identity shows that such a drop requires either dissipation of order \(\varepsilon\) or Pfaffian/current flux of order \(\varepsilon\) through the annulus. The flux estimates above absorb the annular flux into the dissipation when the local energy is small. Thus, in a step whose total \(P\)-drop is much smaller than \(\varepsilon\), the radius cannot double. In a minimizing step with excess \(\delta\ll\varepsilon\), this gives the two-sided comparability

\[
\frac12 r_\varepsilon(g(t_n),x)
\le
r_\varepsilon(g(t),x)
\le
2r_\varepsilon(g(t_n),x),
\qquad
t\in[t_n,t_n+c_1r_\varepsilon(g(t_n),x)^4].
\]

Sobolev persistence follows from the same estimates. The local smoothing gives a small \(C^0\) change of the metric on own-scale balls:

\[
\sup_{B(x,r/2)}|g(t)-g(t_n)|_{g(t_n)}
\le
C(\varepsilon_1^{1/2}+c_1^{1/4}).
\]

Choosing \(\varepsilon_1,c_1\) small enough makes the metric locally bilipschitz to within a factor close to \(1\). Local Sobolev constants are stable under such \(C^0\) changes, so

\[
C_S(g(t))\le 2C_S(g(t_n))
\]

on the relevant balls.

Finally, once one has

\[
\int_0^{c_1}\int_{B(x,r/2)}w|\Delta\mathrm{Rm}|^2<\infty
\]

and small local energy, the standard Bour/Anderson harmonic-coordinate machinery gives \(W^{4,2}\) metric control, and parabolic bootstrap gives own-scale derivative bounds at the end of the step. This supplies the smoothness needed to refreeze the weight.

---

## 5. The precise flux mechanism that can break two-sided comparability

The above proof requires one substantive estimate: annular Pfaffian and \(P\)-current flux must be absorbed by local dissipation when the local energy is small. The full two-sided radius-comparability statement is not a consequence of the global energy law alone.

The dangerous mechanism is Weyl-energy transfer through a neck with almost no Ricci-deviation dissipation.

A model situation is a long neck joining two scalar-flat ALE-type pieces. Let the neck be chosen so that

\[
\int_{\text{neck}}|\mathrm{Ric}^\circ|^2
\]

is very small and the weighted residual

\[
\int_{\text{neck}}r_\varepsilon^4|Q|^2
\]

is also very small. The total \(P\)-energy of the neck can be made arbitrarily small by making the neck long or by tuning the gluing. However, the localized Euler/Pfaffian charge on either side can change by an amount of order one when a gluing parameter is varied. In the transgression identity this appears as

\[
\int_{\text{cross-section}}\Theta(g;\dot g)
\]

being of order one, while

\[
\int w|Q|^2
\]

is arbitrarily small.

Geometrically, Weyl curvature energy can be redistributed from one side of the neck to the other with almost no change in \(P\). Since the energy radius is built from total \(|\mathrm{Rm}|^2\), not from \(|\mathrm{Ric}^\circ|^2\) alone, a ball on one side can see its local curvature energy change by order one while the weighted residual remains tiny. In such a situation the radius at that ball can halve or double without a corresponding amount of \(P\)-dissipation.

This does not contradict

\[
\frac{d}{dt}F=-\frac52\int w|Q|^2.
\]

It only shows that the global dissipation law does not by itself control local redistribution of Weyl energy. The missing ingredient is a neck-flux absorption estimate of the form

\[
\left|
\int_{t_0}^{t_1}\int_{\text{annulus}}
\left(
8\pi^2 d\varphi\wedge\Theta
+\frac52\mathcal R_P
\right)
\right|
\le
\eta
\int_{t_0}^{t_1}\int_{\text{larger ball}}w|Q|^2
+
C\varepsilon
+
o(1),
\]

with \(\eta<1\). Without such an estimate, the strongest statement one can make is an integrated actual-weight estimate, not pointwise radius persistence.

---

## 6. Weakest replacement sufficient for \((\mathrm{PS}_\varepsilon)\)

The structure theorem does not need the full two-sided radius-comparability statement. It needs only the existence of a minimizing sequence satisfying

\[
\int_M r_\varepsilon(g_i)^4|Q(g_i)|^2d\mu_{g_i}\to0.
\]

A much weaker replacement for Lemma 52.KS is therefore enough.

### Replacement A: integrated actual-weight dissipation

It is enough to show that for a minimizing sequence \(g_i\) with \(P(g_i)\le\alpha+\delta_i\), there are smooth paths \(g_i(t)\) with \(g_i(0)=g_i\), existing for times \(T_i>0\), such that

\[
\frac{\delta_i}{T_i}\to0
\]

and

\[
\int_0^{T_i}\int_M r_\varepsilon(g_i(t))^4|Q(g_i(t))|^2d\mu\,dt
\le
C\bigl(P(g_i(0))-P(g_i(T_i))\bigr)+o(\delta_i).
\]

Then some \(t_i\in[0,T_i]\) satisfies

\[
\int_M r_\varepsilon(g_i(t_i))^4|Q(g_i(t_i))|^2d\mu
\to0,
\]

and \(P(g_i(t_i))\le P(g_i(0))\). This directly gives a \((\mathrm{PS}_\varepsilon)\) minimizing sequence.

No pointwise comparability of \(r_\varepsilon\) along the path is required.

### Replacement B: frozen weights plus controlled neck flux

If one insists on frozen weights, the needed statement is weaker than two-sided radius comparability. It is enough that for each frozen step,

\[
\int_0^{c_1}\int_M r_\varepsilon(g(t))^4|Q(g(t))|^2d\mu\,dt
\le
C\int_0^{c_1}\int_M w_n|Q(g(t))|^2d\mu\,dt
+
\mathcal F_n
+
o(\delta),
\]

where \(\mathcal F_n\) is the total Pfaffian/current flux through interfaces and

\[
\sum_n \mathcal F_n=o(\delta).
\]

Then the same averaging argument produces the desired \((\mathrm{PS}_\varepsilon)\) sequence.

### Replacement C: direct variational selection

One may bypass flow time entirely if one can prove the following static selection statement:

For every smooth unit-volume metric \(g\) with \(P(g)\le\alpha+\delta\), there exists another smooth unit-volume metric \(\tilde g\) with

\[
P(\tilde g)\le P(g)
\]

and

\[
\int_M r_\varepsilon(\tilde g)^4|Q(\tilde g)|^2d\mu
\le
\Psi(\delta),
\qquad
\Psi(\delta)\to0.
\]

This is exactly the selection input needed for Theorem 52.3.

---

## 7. A flow-free selection mechanism: one-step implicit descent

There is a promising way to obtain such a static selection without solving a flow for positive time. It is a one-step implicit descent in the energy-scale gauge.

Work on a ball \(B(x,r)\) with \(r=r_\varepsilon(x)\). Choose harmonic coordinates and impose the Bianchi-type gauge used for \(B^{1/6}\)-critical metrics. In this gauge the principal part of \(DQ\) is a uniformly elliptic fourth-order operator, essentially a tensorial bi-Laplacian:

\[
\mathcal P_g \sim \Delta^2.
\]

Let \(\chi\) be a cutoff supported in \(B(x,r)\), equal to \(1\) on \(B(x,r/2)\). Solve the elliptic problem

\[
\mathcal P_g u
=
\chi^2 r^4 Q(g)
\]

with zero Dirichlet data on the outer sphere and with the gauge and trace constraints imposed. Define a one-step perturbation

\[
g_\tau=g-\tau u,
\]

followed by a volume renormalization. Because \(u\) solves the principal linearized descent equation, the first variation gives

\[
P(g_\tau)
=
P(g)
-
\tau\int \chi^2 r^4|Q|^2
+
O\left(
\tau^2\int \chi^2 r^4|Q|^2
\right)
+
O\left(
\varepsilon\,\tau\int \chi^2 r^4|Q|^2
\right),
\]

where the last error comes from lower-order curvature terms and is small when the local energy is at most \(\varepsilon\).

If a near-minimizing metric had

\[
\int \chi^2 r^4|Q|^2\ge c>0,
\]

then for a fixed small universal \(\tau\) the perturbation would reduce \(P\) by an amount proportional to \(c\), contradicting near-minimality. Hence, along a minimizing sequence,

\[
\int_M r_\varepsilon^4|Q|^2\to0.
\]

This mechanism replaces flow lifetime by a local elliptic estimate for the principal part of \(DQ\). The analytic content is much smaller than a full own-scale flow theorem, although one must still handle gauge, volume normalization, and the possibility that the residual is concentrated in a region where the local energy is not small. The latter is treated by the same good/bad ball and energy-radius covering used in the flow argument.

---

## 8. Another flow-free route: Ekeland selection in a weighted length metric

A second alternative is purely variational. Define a length metric on the space of smooth unit-volume metrics by the tangent norm

\[
\|h\|_{w,g}^2
=
\int_M w(g)^{-1}|h|^2d\mu_g,
\]

with

\[
w(g)=r_\varepsilon(g)^4+\eta^4.
\]

The associated gradient norm of \(P\) is

\[
\|\operatorname{grad}P\|_{w,g}^2
=
\int_M w(g)|Q|^2d\mu_g.
\]

If the completion of this length space, restricted to metrics with controlled local Sobolev constants and volume normalized, makes \(P\) lower semicontinuous, then Ekeland’s variational principle gives, for every \(\delta>0\), a metric \(g_\delta\) with

\[
P(g_\delta)\le\alpha+\delta
\]

and

\[
\int_M (r_\varepsilon(g_\delta)^4+\eta^4)|Q(g_\delta)|^2d\mu_{g_\delta}
\le
\sqrt{\delta}.
\]

Letting \(\eta\to0\) along a diagonal sequence gives a \((\mathrm{PS}_\varepsilon)\) minimizing sequence without any flow lifetime argument.

The analytical work in this route is shifted to proving completeness and lower semicontinuity of the weighted length space. The natural compactness input is exactly the fourth-order compactness statement of Proposition 52.1: bounded \(P\), bounded local Sobolev constants, and small weighted residual give \(W^{4,2}\) control in harmonic coordinates.

---

## 9. A lighter flow alternative: dynamic own-scale weight

A third possibility is to keep a flow but remove frozen-weight comparability. Define a smoothed dynamic weight

\[
w(t,x)=\widetilde{r_\varepsilon(g(t),x)^4},
\]

where the smoothing is performed at a fixed fraction of the current energy radius. Then run

\[
\partial_tg=-w(t,x)Q(g(t)).
\]

The principal part remains strongly parabolic because \(w>0\). The energy law becomes

\[
\frac{d}{dt}P(g(t))
=
-\int_M r_\varepsilon(g(t))^4|Q(g(t))|^2d\mu_{g(t)}
+
\text{smoothing error}.
\]

If the smoothing error is controlled, then for a minimizing sequence with excess \(\delta_i\) one only needs existence up to a time \(T_i\) with \(\delta_i/T_i\to0\). Averaging directly gives

\[
\int_M r_\varepsilon(g_i(t_i))^4|Q(g_i(t_i))|^2\to0.
\]

This avoids the need to prove that a frozen weight remains comparable to the evolving radius. The price is that the coefficient \(w(t,x)\) now depends on the solution, so short-time existence requires a fixed-point argument in a space where the smoothed energy radius is locally Lipschitz. This is still analytic work, but it is weaker than proving full two-sided radius persistence.

---

## 10. Summary of the strongest architecture

The most direct proof architecture for Lemma 52.KS is:

1. Use the affine identity  
   \[
   F=8\pi^2\chi+\frac52P
   \]
   to regard the flow as weighted fourth-order curvature flow.

2. Use the exact Euler-form transgression identity to identify the only local energy-transfer terms: Pfaffian flux, \(P\)-current flux, and DeTurck transport.

3. Use the parabolic curvature evolution to obtain the coercive local inequality with dissipation  
   \[
   \int \varphi w|\Delta\mathrm{Rm}|^2.
   \]

4. Absorb nonlinear terms using the four-dimensional local Sobolev inequalities:
   \[
   \int e^2,\quad \int |\nabla\mathrm{Rm}|^2e
   \]
   are controlled by a small multiple of the dissipation when the local energy is below \(\varepsilon_0(C_S)\).

5. Control weight-derivative terms using
   \[
   |\nabla^j w|\le C_j r^{4-j}.
   \]

6. Prove lower radius persistence by showing that small-energy balls cannot gain energy faster than the dissipation and flux allow.

7. Prove upper radius persistence, in a minimizing step, by showing that a large increase of the energy radius would require either \(P\)-drop of order \(\varepsilon\) or neck flux of order \(\varepsilon\).

8. Deduce Sobolev persistence from \(C^0\)-closeness of the metric on own-scale balls.

9. Bootstrap to own-scale smoothness using Bour/Anderson harmonic-coordinate theory and parabolic regularity.

The delicate point is step 7. If neck Pfaffian flux can transfer Weyl energy with almost no Ricci dissipation, the two-sided radius-comparability form of Lemma 52.KS is too strong. The replacement needed for the entry programme is the integrated actual-weight estimate

\[
\int_0^{T_i}\int r_\varepsilon(g_i(t))^4|Q(g_i(t))|^2
\le
C(P(g_i(0))-P(g_i(T_i)))+o(\delta_i),
\]

or a static one-step implicit descent estimate. Either of these is sufficient to produce a \((\mathrm{PS}_\varepsilon)\) minimizing sequence and to bring Theorem 52.3 into force.
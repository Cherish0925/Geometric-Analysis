# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 84,
  "task_field": "generator",
  "task_index": 1,
  "type": "Generator",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step84_ttcs01_sub1_generator.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step84_ttcs01_sub2_generator.md"
    }
  ]
}
```

## Exact Task

Develop the strongest concrete matched-analysis route for the following problem. We have a sequence of closed negative almost-Kähler Einstein four-manifolds converging noncollapsed with bounded diameter to a Kähler–Einstein orbifold with one A1 point, and Step 83 proves that all self-dual Weyl/torsion concentration vanishes and the unique bubble is orientation-matched Ricci-flat Kähler Eguchi–Hanson. We want local exclusion of strict AKE pairs near this one-level degeneration, not finiteness of the entire compactified Einstein moduli. Read the supplied notes and sources. Separate the actual tangent directions (Kähler complex/smoothing deformations and gauge) from a hypothetical nonintegrable AKE normal direction, and derive what a contradiction/blow-up argument would need on the exterior, cone neck, and Eguchi–Hanson core. Identify a precise weighted normal operator, its likely kernel/cokernel, matching data, and one estimate or finite-dimensional map whose proof would settle the local question. Be alert to the fact that negative KE Einstein Jacobi fields are J-anti-invariant Kodaira–Spencer tensors and are tangent to Kähler families, while the AKE torsion is a derivative quantity; do not confuse these. Also incorporate the hyperkähler rotation freedom of Eguchi–Hanson and explain whether it is tangent Kähler/smoothing data or a possible strict-AKE entrance. Produce a mathematical memo with equations and a decisive next calculation, not general advice.

## Integrated Scientific Memo

# Local strict-AKE exclusion at a one-\(A_{1}\) KE degeneration

## 1. The remaining problem is a normal matching problem, not an energy-defect problem

Normalize
\[
\operatorname{Ric}(g)=\lambda g,\qquad \lambda<0,\qquad s=4\lambda,
\]
and let \((V,g_0,\omega_0)\) be the KE orbifold limit. Write the bubbling length as \(\varepsilon\), so the core metric is \(\varepsilon^2g_{\rm EH}\).

Step 83 supplies
\[
T_{\rm AK}(g_n)\longrightarrow0,\qquad
m_{W^+}=m_{\rm torsion}=0,
\]
and an orientation-matched Eguchi–Hanson core with a parallel limiting form. It does **not** supply a rate comparing torsion with the distance to the Kähler locus. In particular, after division by a vanishing normal amplitude, a nonzero exterior, neck, or core limit could still emerge.

The useful target is therefore a **coupled, finite-dimensional normal reduction** near this one-level degeneration. Its tangent variables must include genuine Kähler deformations and smoothing data; its center variables must also retain infinitesimal directions that are not known to integrate. A local exclusion proof must handle these latter variables, rather than silently quotienting them out.

---

## 2. Linearize the pair, not just the Einstein metric

At a Kähler pair \((g,\omega)\), put
\[
h=\dot g,\qquad a=\dot\omega.
\]
In a Bianchi slice, the Einstein block is
\[
P_gh=\frac12\nabla^*\nabla h-\mathring Rh.
\]
The exact linearized almost-Kähler equations are
\[
\boxed{
da=0,\qquad
(1-*)a=\dot *_h\omega,\qquad
2\langle a,\omega\rangle-\operatorname{tr}_g h=0,
}
\tag{2.1}
\]
where
\[
\dot *_h\omega
=*\left(\frac12(\operatorname{tr}h)\omega-h^\sharp\!\cdot\omega\right).
\]
Thus a precise constrained normal operator is
\[
\boxed{
\mathbb L_g(h,a)=
\left(P_gh,\ da,\ (1-*)a-\dot *_h\omega,\
2\langle a,\omega\rangle-\operatorname{tr}h\right),
}
\tag{2.2}
\]
with \(B_gh=0\), modulo simultaneous diffeomorphisms.

For elliptic estimates, use its second-order harmonic realization
\[
\boxed{
\mathbb H_g(h,a)=
\left(P_gh,\ \Delta_ga+\dot\Delta_h\omega\right),
}
\tag{2.3}
\]
retaining the algebraic equations in (2.1) and the closedness condition. On a closed manifold, a harmonic self-dual form is closed, so this is equivalent at the solution level. On the models, impose closedness or the appropriate boundary conditions explicitly.

This distinction matters: \(d^*:\Omega^+\to\Omega^1\) is overdetermined and is not a Fredholm map onto unrestricted \(\Omega^1\). Consequently, the cokernel of the **coupled** problem cannot simply be declared equal to the Einstein Jacobi space.

The torsion linearization is the first-order tensor
\[
\mathbb T(h,a)_{i\,jk}
=\nabla_i a_{jk}
-C(h)^l{}_{ij}\omega_{lk}
-C(h)^l{}_{ik}\omega_{jl},
\tag{2.4}
\]
where
\[
C(h)^l{}_{ij}
=\frac12g^{lm}
(\nabla_i h_{jm}+\nabla_jh_{im}-\nabla_mh_{ij}).
\]
It is \(\mathbb T\), not \(h^-\), that measures departure from Kählerity.

### Exterior center variables

Nagy’s supplied results give, for negative KE metrics,
\[
\ker P\cap{\rm TT}
=
\{h:hJ=-Jh,\ \bar\partial h=0,\ \delta h=0\}.
\tag{2.5}
\]
These are Kodaira–Spencer tensors. Their paired infinitesimal Kähler variations satisfy
\[
\mathbb T(h,a_K(h))=0.
\]
However:

* an infinitesimal Kodaira–Spencer tensor is not necessarily tangent to an **actual** complex family;
* negative KE Einstein deformations are unobstructed to second order even when complex deformations are obstructed.

Indeed, Nagy’s second-order solution satisfies
\[
\Delta_E\mathbf h_2=-2\delta[h_1,h_1]^c,
\]
and
\[
\Theta_2=\bar\partial\mathbf h_2+[h_1,h_1]^c
\in\ker\bar\partial\cap\ker\delta.
\tag{2.6}
\]
The vanishing of \(\Theta_2\) is the complex second-order integrability condition. If it does not vanish, first-order Einstein tangent identification does not exclude a higher-order normal entrance.

There is also a separate linearized-AKE center:
\[
(h,a)=(0,\sigma),\qquad
\sigma\in
\bigl(H^{2,0}(V)\oplus H^{0,2}(V)\bigr)_{\mathbb R}.
\tag{2.7}
\]
Here \(\sigma\) is harmonic, self-dual and orthogonal to \(\omega_0\), but
\[
\mathbb T(0,\sigma)=\nabla\sigma,\qquad
q(u)=u^2|\nabla\sigma|^2+O(u^3).
\]
These form rotations must be retained until their nonlinear obstruction is established.

Gauge directions are the paired variations
\[
(\mathcal L_Xg,\mathcal L_X\omega),
\]
not metric Lie derivatives alone.

---

## 3. Eguchi–Hanson rotations: two different freedoms

Fix a cone framing and identify its parallel self-dual forms with \(\Lambda^+_p\). Let
\[
I=\omega_0(p)/\sqrt2.
\]
For the KE curvature,
\[
\boxed{
\mathcal R^+(p)=W^+(p)+\frac{s}{12}{\rm Id}
=\lambda\,I\otimes I.
}
\tag{3.1}
\]

The framed EH metric parameter is
\[
\zeta\in\Lambda^+_p\simeq\mathbb R^3,\qquad
|\zeta|\asymp\varepsilon^2.
\]
Ozuch’s leading obstruction gives, up to the fixed nonzero normalization constant,
\[
\boxed{
\mathfrak m_{\rm EH}(\zeta)
=C\,\mathcal R^+(p)\zeta
=C\lambda\langle\zeta,I\rangle I.
}
\tag{3.2}
\]

Therefore the metric tilt toward \(I\) is transverse with coefficient \(C\lambda\neq0\), whereas
\[
\zeta\in I^\perp
\tag{3.3}
\]
is the leading smoothing configuration. The latter is not a strict-AKE mode.

### Correct smoothing-coordinate scale

The node parameter and the EH period parameter must not be conflated. In
\[
z_1^2+z_2^2+z_3^2=b,
\]
Spotti’s scaling gives
\[
|b|\asymp\varepsilon^4.
\]
On a marked, ramified deformation chart, the complex period
\[
z=\zeta_2+i\zeta_3
\]
satisfies, up to normalization,
\[
b=c z^2,\qquad z\sim-z
\]
under the \(A_1\) Weyl identification. Thus \(z\) is a period/simultaneous-resolution coordinate, not the unramified node parameter itself.

The second freedom is to change the **chosen parallel form on a fixed EH metric**. Every unit vector in its parallel self-dual three-plane defines a Kähler structure. Infinitesimally, fixed length permits **two**, not three, independent form rotations.

These rotations have zero core torsion. Their asymptotic constant trace must match either:

* the paired Kähler-form variation from an exterior complex deformation; or
* an exterior primitive harmonic form \(\sigma\).

Only the second possibility can have first-order torsion, and that torsion lies in the exterior. A radial interpolation between two parallel forms is not automatically closed and cannot be counted as a free AKE neck mode.

For a varying orbifold parameter \(v\), the tilt equation has the form
\[
t^{-1}{\rm Ob}_{\rm tilt}
=C\lambda\,\theta+O(t+|v|),\qquad t=|\zeta|.
\tag{3.4}
\]
Hence \(\theta=O(t+|v|)\), provided the required parameter-derivative estimates hold. The stronger \(\theta=O(t)\) is not justified for arbitrary varying \(v\). Moreover, tilt elimination gives a graph with higher-order corrections; it does not prove exact orthogonality \(\zeta\perp I\).

---

## 4. The three-region weighted contradiction

Use Ozuch’s decoupled norms with \(0<\beta<1\). Split off constant cone tensors and constant self-dual form traces. For the remainders, use

\[
\|u\|_{{\rm ext},\beta}
=
\sup r^{-\beta}\sum_{j\le k}r^j|\nabla^ju|
+\text{weighted Hölder term},
\]
and
\[
\|u\|_{{\rm EH},\beta}
=
\sup(1+R)^\beta
\sum_{j\le k}(1+R)^j|\nabla^ju|
+\text{weighted Hölder term}.
\tag{4.1}
\]
Apply these to the dimensionless pair variables \(g^{-1}h,g^{-1}a\), with the core pulled back and rescaled. A second-order output has weight shifted by two; a first-order closedness output has weight shifted by one.

The relevant estimate is
\[
\boxed{
\|x^\perp\|_{\mathcal X_{\varepsilon,\beta}}
\le C\left(
\|\mathbb L_\varepsilon x^\perp\|_{\mathcal Y_{\varepsilon,\beta}}
+|\operatorname{Tr}_{\rm match}x^\perp|
+|\Pi_{\rm model}x^\perp|
\right),
}
\tag{4.2}
\]
uniformly as \(\varepsilon\downarrow0\). Here \(x^\perp=(h,a)\); the finite projections remove all exterior formal centers, framed EH metric variations and form traces—not just actual integrable Kähler directions. The tilt coefficient is handled by the rescaled obstruction equation (3.4).

A failure of (4.2) produces one of the following normalized limits.

### Exterior

After removal of singular asymptotic terms, the limit extends orbifold-smoothly across \(p\). Its metric component lies in (2.5); its independent form component lies in (2.7). Projection away from both makes it zero.

A contradiction normalized merely by \(\|\nabla\omega_n\|\), without subtracting the paired Kähler directions, does not accomplish this: Kodaira–Spencer fields can dominate the metric normalization while contributing no first-order torsion.

### Cone neck

In Cartesian tensor components,
\[
P_e=\tfrac12\nabla^*\nabla,\qquad
\Delta_e=\nabla^*\nabla.
\]
For rank-two tensors and two-forms descending under \(x\mapsto-x\), the harmonic coefficients have even spherical degrees. The relevant indicial roots are
\[
\ldots,-4,-2,0,2,4,\ldots.
\tag{4.3}
\]
A neck limit with mild singularity at zero and subquadratic growth at infinity is therefore constant; the decoupled trace condition kills that constant.

Equivalently, a two-sided weight \(-2<\delta<0\) gives the familiar removable-singularity/decay Liouville argument after constants and matching tails are extracted. The weight must be imposed on the **pair**. Torsion is a derivative of the pair and has shifted exponents.

### Eguchi–Hanson core

The supplied source identifies the Einstein \(L^2\) kernel as three-dimensional:
\[
\mathcal O(g_{\rm EH})
=\operatorname{span}(o_1,o_2,o_3),
\tag{4.4}
\]
all generated by framed metric scale/rotation variations. The metric-block cokernel is the same space.

For the independent form block,
\[
W^+=0,\quad\operatorname{Ric}=0
\quad\Longrightarrow\quad
\Delta|_{\Omega^+}=\nabla^*\nabla.
\tag{4.5}
\]
There is no \(L^2\) self-dual harmonic form: integration by parts forces it to be parallel, and infinite volume then forces it to vanish. Likewise, a self-dual harmonic form with zero constant asymptotic trace and positive decay must vanish. With prescribed constant trace, it is the corresponding parallel form.

Thus the expected **constrained paired kernel**, with fixed asymptotic metric and allowing a form trace, consists of
\[
\boxed{
\text{three paired hyperkähler metric variations}
\;+\;
\text{two fixed-length parallel-form rotations}
\;+\;\text{residual gauge}.
}
\tag{4.6}
\]
Proving (4.6) with its trace map is the missing coupled model calculation. It shows why an independent strict-AKE core mode is unlikely: every allowable core form mode has a visible constant trace at infinity.

---

## 5. Matching data and surviving finite-dimensional equations

The metric expansions are
\[
g_0=e+H_2+H_4+\cdots,\qquad
g_{\rm EH}=e+H^4+\cdots,
\]
with
\[
|H_2|\sim r^2,\qquad
|H^4(\zeta)|\sim|\zeta|^2r^{-4}.
\tag{5.1}
\]
The metric matching data comprise:

* constant cone/frame changes;
* the exterior curvature jet \(H_2\);
* the EH \(r^{-4}\) tail;
* its Green pairings with \(o_k\);
* exterior Jacobi projections.

The form matching data comprise:

* the common constant self-dual form;
* its metric-dependent anti-self-dual completion in (2.1);
* the decaying EH paired-form tails;
* global harmonic-form coefficients and periods.

Ozuch’s equations include
\[
t\lambda_k(v,\phi)+t^2\mu_k(v,\phi)
+O(t^{5/2})=0,\qquad
\nu_l(t,\phi,v)=0.
\tag{5.2}
\]
At the KE endpoint, the rank-one curvature (3.1) already satisfies the curvature-form restrictions of the higher-order obstruction theorem. That theorem is consequently not a local strict-AKE exclusion theorem. Its stability, rigidity and integrability hypotheses also cannot be imported into the present setting without verification.

When the leading EH obstructions vanish, Ozuch’s Lemma 2.3 gives \(H_2^4=0\). This removes a mixed \(r^{-2}\) metric tail; it does not eliminate all higher-order normal equations.

After solving the infinite-dimensional complement using (4.2), retain a reduced map
\[
\boxed{
\mathfrak F(t,\phi,v,c)
=
\bigl({\rm Ob}_{\rm Einstein},\ {\rm AK}_{\rm length}\bigr)=0.
}
\tag{5.3}
\]
Here \(v\) includes **all formal** exterior Jacobi directions, and \(c\) records harmonic-form coefficients. For fixed \(g\), choose a local basis of \(\mathcal H_g^+\) and write \(\Omega(g,c)\). A convenient scalar encoding is
\[
{\rm AK}_{\rm length}(g,c)
=
\int_M\left(
|\Omega(g,c)|_g^2-\fint_M|\Omega(g,c)|_g^2
\right)^2dV_g,
\tag{5.4}
\]
together with mean-square normalization \(2\). Its zero set is exactly the constant-length condition.

The full finite-dimensional cokernel includes the nonlinear length obstruction and possible complex-obstructed centers. It is not merely
\(\mathcal O(g_0)\oplus\mathcal O(g_{\rm EH})\).

---

## 6. What can already be ruled out, and what cannot

### Pure form rotation is second-order obstructed

On the fixed KE metric,
\[
\Omega_u=a(u)\omega_0+u\sigma,\qquad
a(u)=1+O(u^2),
\]
has constant length only if the order-\(u^2\) function \(|\sigma|^2\) is constant. A nonzero holomorphic two-form cannot have constant nonzero norm when \(\lambda\neq0\): on its nonvanishing set the curvature identity for its norm would force the Ricci form to vanish.

Consequently,
\[
\int_V
\left(|\sigma|^2-\fint_V|\sigma|^2\right)^2dV
\ge c\|\sigma\|_{L^2}^4
\tag{6.1}
\]
on the finite-dimensional primitive harmonic space. The same second-order obstruction applies to a paired deformation with \(h_1=0\), since its second-order Einstein variation is again a Jacobi field plus gauge.

This is useful, but does not yet dispose of mixed \((h_1,\sigma)\) variations or entrances whose first normal term occurs after several Kähler orders. Those require the full reduced map.

### A Kuranishi-square action formula is a proposal, not a consequence

The suggested quartic formula
\[
\widehat{\mathscr S}_{\rm red}(u)
-\widehat{\mathscr S}_{\rm red}(0)
\stackrel{?}{=}
C u^4\|\mathcal H[h_1,h_1]^c\|^2+O(u^5)
\tag{6.2}
\]
is a meaningful calculation, but its coefficient, sign and uniform degeneration error are not supplied by Nagy’s second-order theorem.

Nor may one use
\[
D=\frac{s^2}{16}\bigl(\operatorname{Vol}(g)-\operatorname{Vol}(V)\bigr)
\]
as an off-shell variational functional. That formula applies at normalized Einstein points. Off shell, the relevant functional is the normalized Einstein–Hilbert action, reduced in a compatible variational slice.

Similarly, Spotti proves positive-KE smoothing existence, not the negative-KE local completeness assertion needed here. Vanishing of a complex obstruction group could facilitate a Kähler comparison family, but the asserted exhaustion of all nearby Einstein metrics needs additional deformation, convergence and chart-completeness proofs.

---

## 7. A single local theorem that would settle the question

The strongest economical closure target is:

> **One-level paired curve-selection theorem.** After finite framing and ramified period coordinates, the zero set of (5.3), including its \(t=0\) face and the strict-AKE condition, admits local curve selection.

Real-subanalyticity of this particular paired zero set is sufficient. This is much narrower than finiteness or subanalyticity of the entire compactified Einstein moduli space.

To see why it settles the problem, suppose strict AKE zeros accumulate at the KE endpoint. Curve selection yields a differentiable arc of strict AKE pairs on the fixed smooth topology, converging to the endpoint. Along its Einstein metrics,
\[
\frac{d}{du}\widehat{\mathscr S}(g(u))=0.
\]
Hence
\[
D(g(u))
=\frac{\widehat{\mathscr S}(g(u))^2}{16}
-2\pi^2(2\chi+3\tau)
\]
is constant. Step 83 gives
\[
\lim_{u\downarrow0}D(g(u))=0.
\]
Thus \(D\equiv0\), whereas
\[
D=T_{\rm AK}
=\int_M\left(|W_3^+|^2+\frac{3}{32}q^2\right)dV.
\]
Therefore \(q\equiv0\), contradicting strictness. This argument automatically handles mixed form rotations and all higher-order Kodaira–Spencer entrances.

**The unresolved implication must be kept explicit:** analyticity on the fixed orbifold and ALE pieces, plus a uniform complement inverse, does not by itself prove subanalyticity through the gluing scale \(t=0\). Scale-dependent matching can introduce logarithmic or other nonanalytic behavior. The absence of a multilevel tree simplifies the issue but does not establish the required extension.

### Decisive next calculation

Compute the **paired EH trace/Green matrix**:

1. For each \(o_k=\partial_{\zeta_k}g_{\rm EH}\), differentiate its matched hyperkähler form to obtain \(a_k\), and verify
   \[
   \mathbb L_{\rm EH}(o_k,a_k)=0,\qquad
   \mathbb T(o_k,a_k)=0.
   \]
2. Classify every solution with the decoupled \(0<\beta<1\) asymptotics and prescribed constant form trace; prove (4.6).
3. Compute the boundary pairing with \((H_2,\text{exterior form jet})\), recovering
   \[
   \partial_{\zeta_\parallel}\mathfrak m_{\rm EH}=C\lambda\neq0,
   \]
   and identify whether the form matching creates any additional finite obstruction.
4. Track parameter derivatives and resonant/logarithmic terms in this same matching calculation.

This calculation supplies the precise core input for (4.2), identifies the genuine normal center, and determines what regularity remains to prove for (5.3). The local question is then reduced to one sharply defined object: **the regularity or a coercive normal estimate for the paired finite-dimensional zero set at \(t=0\)**—not a global compactified-moduli finiteness problem.
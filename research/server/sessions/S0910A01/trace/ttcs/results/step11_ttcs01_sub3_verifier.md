# TTCS Independent Branch Record

```json
{
  "step_id": 11,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step9_regularity_false_and_new_direction.tex",
    "Sessions/S0910A03/workspace/notes/step9_maximal_function_and_weitzenbock_rotation.tex",
    "Sessions/S0910A01/workspace/notes/step11_chart_accessibility_and_energy.md",
    "Sessions/S0910A01/workspace/notes/step8_derdzinski_measure_local_theorem.md"
  ]
}
```

## Task

Verify the Pontryagin localization mechanism for the four-dimensional negative-branch Yau 26 program.

1. VERIFY THE PONTRYAGIN DENSITY FORMULA: For a 4-manifold with curvature decomposition Rm = W⁺ + W⁻ + E + s, what is p₁(Λ²₊) as an integrand? Specifically, verify that on a region of regular fibered collapse (fiber dim d ≥ 1, base dim ≤ 3) where the self-dual forms are 'basic' (pulled back from the base), the contribution to ∫p₁(Λ²₊) = 8π²(2χ+3τ)/? vanishes or is constrained.

2. CHECK THE COUNTERMODEL: For the Taub-NUT-AdS metric with NUT parameter ν→0, verify:
   (a) The claim that the ψ-circle at distance 1/2 from the NUT is contractible in B₁.
   (b) The claim that the curvature |Rm|² remains bounded as ν→0 at fixed distance from the NUT.
   (c) Whether the maximal function bound ∫_{B_r}|Rm|² ≤ K₀·Vol(B_r) holds.

3. VERIFY THE WEITZENBÖCK COMPUTATION: For Einstein Ric=-g with calibrated W⁺ spectrum (-1/6,1/12,1/12), check that the Weitzenböck formula gives ∫|∇H|²/∫|H|² = 1 for the simple eigenform and 3/2 for the double eigenspace. Distinguish between the curvature-operator arrangement and the Weitzenböck R̃ arrangement.

4. CHECK THE DEFINITE-PAIR EXCLUSION: A03 claims flat rank ≥ 2 collapse is excluded. Verify the argument: two independent near-harmonic SD forms with locally nondegenerate Gram matrix, closedness, and constant amplitude → ∇ → 0, contradicting the Weitzenböck gradient energy. Is 'locally nondegenerate Gram matrix' automatic or an additional hypothesis?

5. ASSESS: Is the Pontryagin charge 4π²(A-k) correctly computed? Does basic collapse really contribute zero to this charge?

## Output

Scientific verification memo: Pontryagin localization and related local models
================================================================================

## 1. Pontryagin form for \(\Lambda^2_+\)

With the curvature-operator convention used in the supplied notes,

\[
\mathcal R=
\begin{pmatrix}
W^+ + \frac{s}{12}I & B\\
B^* & W^-+\frac{s}{12}I
\end{pmatrix},
\]

where \(E=\operatorname{Ric}-\frac{s}{4}g\), the standard Chern–Gauss–Bonnet and signature formulas are

\[
8\pi^2\chi(M)
=
\int_M
\left(
|W^+|^2+|W^-|^2-\frac12|E|^2+\frac{s^2}{24}
\right)d\mu,
\]

\[
12\pi^2\tau(M)
=
\int_M
\left(|W^+|^2-|W^-|^2\right)d\mu.
\]

Therefore

\[
2\chi+3\tau
=
\frac1{4\pi^2}
\int_M
\left(
2|W^+|^2-\frac12|E|^2+\frac{s^2}{24}
\right)d\mu.
\]

Thus, with the orientation convention matching \(\int p_1(\Lambda^2_+)=2\chi+3\tau\),

\[
\boxed{
p_1(\Lambda^2_+)
=
\frac1{4\pi^2}
\left(
2|W^+|^2-\frac12|E|^2+\frac{s^2}{24}
\right)d\mu .
}
\]

Equivalently, if \(\Omega^+\) is the \(\mathfrak{so}(3)\)-valued curvature of the Levi-Civita connection on \(\Lambda^2_+\),

\[
p_1(\Lambda^2_+)
=
-\frac1{8\pi^2}\operatorname{tr}(\Omega^+\wedge\Omega^+).
\]

So the raw scalar density

\[
\mathcal P_+
:=
2|W^+|^2-\frac12|E|^2+\frac{s^2}{24}
\]

satisfies

\[
\boxed{
\int_M \mathcal P_+\,d\mu
=
4\pi^2(2\chi+3\tau).
}
\]

This resolves the constant ambiguity:  
\(\int p_1(\Lambda^2_+)=2\chi+3\tau\), while \(\int \mathcal P_+d\mu=4\pi^2(2\chi+3\tau)\), and \(-\int\operatorname{tr}(\Omega^+\wedge\Omega^+)=8\pi^2(2\chi+3\tau)\).

---

## 2. Basic regular collapse and vanishing of the Chern–Weil form

For a regular fibration

\[
\pi:U^4\to B^m,\qquad m\le 3,
\]

if the \(\Lambda^2_+\)-connection descends to the base, i.e.

\[
\Omega^+ = \pi^*\Omega_B
\]

for some \(\mathfrak{so}(3)\)-valued \(2\)-form \(\Omega_B\) on \(B\), then

\[
\operatorname{tr}(\Omega^+\wedge\Omega^+)
=
\pi^*\operatorname{tr}(\Omega_B\wedge\Omega_B)
=
0,
\]

because \(B\) has dimension at most \(3\). Hence such a genuinely basic \(\Lambda^2_+\)-connection contributes no \(p_1(\Lambda^2_+)\) density.

A wording point matters mathematically: a nonzero self-dual \(2\)-form on a Riemannian four-manifold cannot literally be the pullback of a \(2\)-form from a \(3\)- or lower-dimensional base. Indeed, if \(\omega\in\Lambda^2_+\) and \(\omega\ne0\), then

\[
\omega\wedge\omega=|\omega|^2d\mu\ne0,
\]

whereas for \(\omega=\pi^*\beta\) with \(\dim B\le3\),

\[
\omega\wedge\omega=\pi^*(\beta\wedge\beta)=0.
\]

So the correct “basic” interpretation is not literal pullback of the self-dual \(2\)-forms as differential forms. It should mean that the rank-three bundle \(\Lambda^2_+\), its local frame, or its connection/curvature descends to the lower-dimensional model. Under that connection-level interpretation, the localization mechanism is mathematically valid.

Thus the Pontryagin localization statement is:

\[
\boxed{
\text{Regions where the }\Lambda^2_+\text{ curvature is pulled back from a base of dimension }\le3
\text{ carry zero }p_1(\Lambda^2_+)\text{ density.}
}
\]

Any nonzero total \(p_1(\Lambda^2_+)\) must therefore arise from regions where the \(\Lambda^2_+\)-connection has vertical, mixed, twisting, singular, or genuinely four-dimensional curvature content.

---

## 3. Taub–NUT–AdS model

The supplied metric is

\[
g_\nu =
\frac{dr^2}{F_\nu(r)}
+(r^2-\nu^2)(d\theta^2+\sin^2\theta\,d\phi^2)
+4\nu^2F_\nu(r)(d\psi+\cos\theta\,d\phi)^2,
\]

\[
F_\nu(r)=
\frac{r-\nu}{r+\nu}
\left(
1+\frac{(r-\nu)(r+3\nu)}{\ell^2}
\right),
\qquad \ell=\sqrt3.
\]

With this choice of \(\ell\), the Einstein equation is

\[
\operatorname{Ric}_{g_\nu}=-g_\nu.
\]

### (a) Contractibility of the \(\psi\)-circle

Near \(r=\nu\), set

\[
r=\nu+\frac{\rho^2}{8\nu}.
\]

Then

\[
F_\nu(r)=\frac{\rho^2}{16\nu^2}+O(\rho^4/\nu^4),
\]

and the metric has leading form

\[
g_\nu
=
d\rho^2+\frac{\rho^2}{4}
\left[
d\theta^2+\sin^2\theta\,d\phi^2
+(d\psi+\cos\theta\,d\phi)^2
\right]
+\text{higher terms}.
\]

For \(\psi\) of period \(4\pi\), this is the smooth Euclidean metric on \(\mathbb R^4\) in Hopf coordinates. The \(\psi\)-circle collapses to the NUT point \(\rho=0\). Hence the \(\psi\)-orbit through a point at distance \(1/2\) from the NUT contracts through the radial disk swept out by decreasing \(r\) to \(\nu\).

For \(\nu\) small, the \(\psi\)-circle length at fixed positive distance from the NUT is \(O(\nu)\). The contracting disk lies inside \(B_1(p_\nu)\); at worst one may move the chosen distance \(1/2\) slightly inward, say to \(0.49\), to avoid any open-ball endpoint convention. The topological content is solid: the short \(\psi\)-loop is nullhomotopic in the buffered ball containing the NUT, so the local universal cover does not unwrap that short fiber.

### (b) Curvature bounded at fixed distance from the NUT

Use the orthonormal coframe

\[
e^0=\frac{dr}{\sqrt{F_\nu}},\qquad
e^1=\sqrt{r^2-\nu^2}\,d\theta,
\]

\[
e^2=\sqrt{r^2-\nu^2}\sin\theta\,d\phi,\qquad
e^3=2\nu\sqrt{F_\nu}(d\psi+\cos\theta\,d\phi).
\]

On the annular distance band

\[
\operatorname{dist}(\cdot,\text{NUT})\in[1/6,5/6],
\]

the coordinate \(r\) stays in a compact subinterval of \((0,\infty)\) independent of small \(\nu\). In this band,

\[
r^2-\nu^2\sim r^2,\qquad F_\nu(r)\to 1+\frac{r^2}{\ell^2},
\]

and the structure coefficient coming from the Hopf connection is

\[
2\nu\sqrt{F_\nu}\,d(d\psi+\cos\theta\,d\phi)
=
-2\nu\sqrt{F_\nu}\sin\theta\,d\theta\wedge d\phi
=
O(\nu)\,e^1\wedge e^2.
\]

The remaining coframe structure coefficients and their first derivatives stay bounded on the same annulus. Hence

\[
\boxed{
\sup_{\operatorname{dist}\in[1/6,5/6]}|\operatorname{Rm}_{g_\nu}|\le C
}
\]

with \(C\) independent of \(\nu\).

### (c) Maximal mean curvature bound

If \(p_\nu\) is at distance \(1/2\) from the NUT, then

\[
B_{1/3}(p_\nu)
\subset
\{\operatorname{dist}(\cdot,\text{NUT})\in[1/6,5/6]\}.
\]

Therefore, for every \(0<r\le1/3\),

\[
\int_{B_r(p_\nu)}|\operatorname{Rm}_{g_\nu}|^2\,d\mu
\le
K_0\,\operatorname{Vol}(B_r(p_\nu)),
\]

and hence

\[
\fint_{B_r(p_\nu)}|\operatorname{Rm}_{g_\nu}|^2\,d\mu
\le K_0.
\]

The same estimate holds on the relevant lifted ball whenever the local cover does not unwrap the nullhomotopic \(\psi\)-circle. Thus the Taub–NUT–AdS model does show that a uniform mean \(L^2\) curvature bound at all small scales, plus Ricci lower control, does not by itself force noncollapse of the local universal cover.

---

## 4. Weitzenböck computation at the calibrated spectrum

For a \(4\)-dimensional Einstein metric with

\[
\operatorname{Ric}=\lambda g,\qquad s=4\lambda,
\]

the Weitzenböck formula on \(2\)-forms is

\[
(\Delta_d\omega)_{ij}
=
(\nabla^*\nabla\omega)_{ij}
+
R_i{}^k\omega_{kj}
+
R_j{}^k\omega_{ik}
-
2R_{ikjl}\omega_{kl}.
\]

For Einstein metrics,

\[
R_i{}^k\omega_{kj}+R_j{}^k\omega_{ik}
=
2\lambda\,\omega_{ij}.
\]

Write

\[
\widetilde R(\omega)_{ij}:=R_{ikjl}\omega_{kl}.
\]

Then

\[
\Delta_d\omega
=
\nabla^*\nabla\omega
+
(2\lambda I-2\widetilde R)\omega.
\]

On self-dual forms, under the conventions used in the supplied notes,

\[
\widetilde R|_{\Lambda^2_+}
=
W^+ + \frac{s}{12}I.
\]

Equivalently, the standard self-dual Weitzenböck formula is

\[
\Delta_d H
=
\nabla^*\nabla H
-
2W^+(H)
+
\frac{s}{3}H.
\]

If \(H\) is harmonic and lies in a \(W^+\)-eigenline with eigenvalue \(w\), then

\[
0=
\int |\nabla H|^2
+
\int\left(-2w+\frac{s}{3}\right)|H|^2,
\]

so

\[
\boxed{
\frac{\int|\nabla H|^2}{\int|H|^2}
=
2w-\frac{s}{3}.
}
\]

For

\[
\operatorname{Ric}=-g,\qquad s=-4,
\]

and

\[
\operatorname{Spec}(W^+)=
\left(-\frac16,\frac1{12},\frac1{12}\right),
\]

one obtains:

\[
w=-\frac16:
\qquad
2w-\frac{s}{3}
=
-\frac13+\frac43
=
1;
\]

\[
w=\frac1{12}:
\qquad
2w-\frac{s}{3}
=
\frac16+\frac43
=
\frac32.
\]

Thus the table in `step9_maximal_function_and_weitzenbock_rotation.tex` is numerically correct:

\[
\boxed{
\frac{\int|\nabla H|^2}{\int|H|^2}=1
\text{ on the simple eigenspace,}
\qquad
\frac32
\text{ on the double eigenspace.}
}
\]

One wording correction: the index arrangement \(R_{ikjl}\) is indeed the one appearing in the Weitzenböck term, and it should not be replaced blindly by \(R_{ijkl}\). However, for Einstein metrics on \(\Lambda^2_+\), with the conventions of these notes, its eigenvalues are exactly

\[
w_i+\frac{s}{12}.
\]

At the calibrated values these are

\[
-\frac16-\frac13=-\frac12,\qquad
\frac1{12}-\frac13=-\frac14,\qquad
\frac1{12}-\frac13=-\frac14.
\]

So the Weitzenböck energy computation is correct; the cleanest derivation is through

\[
\Delta_d H=\nabla^*\nabla H-2W^+(H)+\frac{s}{3}H.
\]

---

## 5. Definite-pair exclusion in flat-rank collapse

The rank-\(\ge2\) exclusion described in the A03 note needs a precise local input.

A single closed self-dual \(2\)-form of constant length does not force parallelism; this is the usual almost-Kähler situation. For two closed self-dual forms with constant Gram matrix, the algebra is stronger but still does not automatically force \(\nabla\to0\).

Let \(\{\omega_1,\omega_2,\omega_3\}\) be a local oriented orthonormal frame of \(\Lambda^2_+\). Write the \(\Lambda^2_+\)-connection as

\[
\nabla\omega_1=a\,\omega_2+b\,\omega_3,
\]

\[
\nabla\omega_2=-a\,\omega_1+c\,\omega_3,
\]

\[
\nabla\omega_3=-b\,\omega_1-c\,\omega_2,
\]

where \(a,b,c\) are \(1\)-forms. The equations

\[
d\omega_1=0,\qquad d\omega_2=0
\]

give two linear systems for \(a,b,c\), but they do not force

\[
a=b=c=0.
\]

There remains a torsion component. By contrast, if one also has

\[
d\omega_3=0,
\]

then the full orthonormal triple of closed self-dual forms gives a hyperkähler-type local structure and forces the \(\Lambda^2_+\)-connection to vanish, hence

\[
\nabla\omega_i=0.
\]

Therefore:

\[
\boxed{
\text{A full closed definite triple forces parallelism; a closed definite pair alone does not.}
}
\]

Consequently, the A03 flat-rank-\(\ge2\) exclusion is valid only with extra geometric input beyond “two independent near-harmonic self-dual forms with locally nondegenerate Gram matrix.” Such input could be, for example, an exact flat torus-product ansatz, closure of the algebraic third form, or collapse-model equations that eliminate the remaining torsion component.

Also,

\[
\boxed{
\text{local nondegeneracy of the Gram matrix is not automatic.}
}
\]

Global linear independence of harmonic or near-harmonic forms does not imply a pointwise lower bound for the Gram determinant on a given patch. Two forms can be globally independent while becoming nearly colinear or very unevenly distributed locally. Thus “locally nondegenerate Gram matrix” is a genuine local hypothesis.

---

## 6. Pontryagin charge for Ishida–LeBrun blow-ups

For a single minimal complex surface \(X\) of general type,

\[
A=c_1^2(X)=2\chi(X)+3\tau(X).
\]

For

\[
M=X\# k\,\overline{\mathbb{CP}}^{\,2},
\]

one has

\[
\chi(M)=\chi(X)+k,\qquad
\tau(M)=\tau(X)-k,
\]

so

\[
2\chi(M)+3\tau(M)
=
2\chi(X)+3\tau(X)-k
=
A-k.
\]

Therefore

\[
\boxed{
\int_M p_1(\Lambda^2_+)=A-k,
}
\]

and

\[
\boxed{
\int_M
\left(
2|W^+|^2-\frac12|E|^2+\frac{s^2}{24}
\right)d\mu
=
4\pi^2(A-k).
}
\]

At the critical value \(k=A/3\),

\[
A-k=\frac{2A}{3},
\]

so the normalized Pontryagin number is \(2A/3\), while the raw scalar-density integral is

\[
\frac{8\pi^2A}{3}.
\]

If the underlying Ishida–LeBrun manifold is a connected sum of several general-type pieces \(X_j\), the connected-sum formula inserts an additional \(-4\) for each connected sum operation. In that setting,

\[
2\chi+3\tau
=
\sum_j c_1^2(X_j)-4(m-1)-k
\]

for \(m\) summands, unless the parameter \(A\) has already been defined to absorb this correction. For the single-surface blow-up setting used in `step11_chart_accessibility_and_energy.md`, the formula \(A-k\) is correct.

---

## Overall assessment

The Pontryagin localization mechanism is mathematically sound in the following precise form:

\[
\boxed{
4\pi^2p_1(\Lambda^2_+)
=
\left(
2|W^+|^2-\frac12|E|^2+\frac{s^2}{24}
\right)d\mu,
}
\]

\[
\boxed{
\int p_1(\Lambda^2_+)=2\chi+3\tau.
}
\]

For \(M=X\#k\overline{\mathbb{CP}}^{\,2}\),

\[
\boxed{
\int p_1(\Lambda^2_+)=A-k,
\qquad
\int \mathcal P_+d\mu=4\pi^2(A-k).
}
\]

On a regular collapsed region, the \(p_1(\Lambda^2_+)\) density vanishes if the \(\Lambda^2_+\)-connection curvature descends from a base of dimension at most \(3\). The phrase “self-dual forms are pulled back from the base” should be replaced by a connection-level formulation, since nonzero self-dual \(2\)-forms cannot literally be pullbacks from a base of dimension \(\le3\).

The Taub–NUT–AdS model supports the intended geometric lesson: the short collapsing \(\psi\)-circle is contractible inside the buffered ball, curvature stays uniformly bounded on fixed annular distance bands, and the normalized \(L^2\) maximal curvature bound follows from the pointwise bound. Thus local universal covers need not become noncollapsed merely from Ricci lower control plus controlled mean \(L^2\) curvature.

The Weitzenböck computation is correct: the calibrated spectrum gives gradient-energy ratios \(1\) and \(3/2\). The clean formula is

\[
\int|\nabla H|^2=\int\left(2w-\frac{s}{3}\right)|H|^2.
\]

The flat-rank definite-pair exclusion needs strengthening: a full closed definite triple forces parallelism, but a closed definite pair with locally nondegenerate Gram matrix does not by itself force \(\nabla H\to0\). Local Gram nondegeneracy is an additional local hypothesis, not a consequence of global independence.
# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 39,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step39_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step39_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Independently check the Step-39 actual harmonic-zero test object and its computed/scaled quantities. Verify the differential-geometric assertions: collar gluing gives a smooth closed self-dual harmonic form on the closed replicated metric; zero exceptional period and bolt vanishing are consistent; the sixfold scaling of q, amplitude defect, one-derivative form energy, Weyl-model error, and Ricci cost is correct; the negative-Kähler target used in the script has the stated original-scale eigenvalues; eta=1 is justified for the fixed pullback Kähler cohomology class but not arbitrary directions; and the singular hatted AK s* calculation cannot directly invoke closed AKGamma. Read the script and JSONs rather than trusting the note. Identify any normalization or logical error and give corrected formulas/numbers. Then assess only what the evidence establishes about localized O(k) form cost versus a diffuse construction.

## Integrated Scientific Memo

# Step-39 verification memo

## 1. The glued harmonic-zero object is geometrically consistent

For
\[
g=dt^2+a_f^2\sigma_f^2+a_g^2\sigma_g^2+a_h^2\sigma_h^2,
\qquad d\sigma_f=2\sigma_g\wedge\sigma_h,
\]
with orientation \(*e^{0f}=e^{gh}\),
\[
\Omega=\frac12d(\phi\sigma_f)
=\frac{\phi'}{2a_f}e^{0f}+\frac{\phi}{a_ga_h}e^{gh}.
\]
The ODE
\[
\frac{\phi'}{\phi}=\frac{2a_f}{a_ga_h}
\]
therefore gives
\[
\Omega=u^2(e^{0f}+e^{gh}),\qquad
u^2=\frac{\phi}{a_ga_h},\qquad |\Omega|_g^2=2u^4.
\]
Thus \(\Omega\) is closed and self-dual. Once smoothness across the bolt is established, \(d^*\Omega=-*d\Omega=0\), so it is harmonic.

Near the perpendicular \(O(-1)\) bolt,
\[
a_h=t+O(t^3),\qquad a_f,a_g=b+O(t^2),
\]
and the ODE yields
\[
\phi=Ct^2(1+O(t^2)),\qquad u^2=\frac Cb\,t+O(t^3).
\]
The invariant potential \(\phi\sigma_f\) has the required smooth vanishing, so \(\Omega\) extends smoothly and vanishes on the bolt. Consequently
\[
\Omega|_E=0,\qquad \int_E\Omega=0.
\]
Both statements hold in this symmetric model; zero period alone would not imply pointwise bolt vanishing in general.

On the exact complex-hyperbolic collar,
\[
(a_ga_h)'=2a_f.
\]
The script normalizes \(\phi(X)=X=a_ga_h(X)\), hence uniqueness of the ODE gives
\[
\phi=a_ga_h,\qquad \Omega=\omega_{\rm CH}
\]
throughout the exact collar. Extension by the host Kähler form therefore involves no cutoff: all jets agree on an open collar. Replication at disjoint sites produces a smooth, closed, self-dual harmonic form on the closed glued metric, with one bolt zero sphere per cell. This is compatible with the Taubes period obstruction because the form is not nowhere vanishing.

The JSON Boolean fields merely report these facts; they are not themselves verification. The ODE, bolt asymptotics, and exact-collar equality provide the verification.

---

## 2. Sixfold scaling and the negative-Kähler target

Set
\[
\bar g=6g,\qquad \psi=6\Omega.
\]
On the CH region, \(\operatorname{Ric}_g=-6g\) becomes
\[
\operatorname{Ric}_{\bar g}=-\bar g.
\]
In dimension four,
\[
dV_{\bar g}=36\,dV_g,\qquad *_{\bar g}|_{\Lambda^2}=*_g|_{\Lambda^2}.
\]

### Norm and amplitude

For a two-form,
\[
|\psi|_{\bar g}^2=|6\Omega|_{6g}^2
=36\cdot 6^{-2}|\Omega|_g^2
=|\Omega|_g^2=:q=2u^4.
\]
Hence \(q\) is unchanged and
\[
\int(q-2)^2dV_{\bar g}
=36\int(q-2)^2dV_g.
\]
The script’s factor \(36\) is correct.

### One-derivative energy

The Levi-Civita connection is unchanged by constant scaling, so
\[
|\nabla\psi|_{\bar g}^2
=36\,6^{-3}|\nabla\Omega|_g^2
=\frac16|\nabla\Omega|_g^2.
\]
After multiplying by volume,
\[
\int|\nabla\psi|_{\bar g}^2dV_{\bar g}
=6\int|\nabla\Omega|_g^2dV_g.
\]
The script’s factor \(6\) is correct.

The integrated harmonic-form Weitzenböck formula gives
\[
\int|\nabla\Omega|^2
=\int q\left(2W^+_{ff}-\frac{s}{3}\right)dV.
\]
Accordingly,
```python
grad_density = W*qform*(2*Wff-scal/3)
```
is an integrated identity density, not the pointwise quantity \(|\nabla\Omega|^2\). Its negative sampled values are therefore harmless.

### Weyl model

With
\[
A_{\psi,1/2}=-\frac12(\psi\otimes\psi)_0
\]
on \(\Lambda^+\), its eigenvalues in the \(\bar g\) normalization are
\[
\left(-\frac q3,\frac q6,\frac q6\right).
\]
Pulled back to the original curvature scale, \(6A_{\psi,1/2}\) has eigenvalues
\[
\boxed{(-2q,q,q)}.
\]
This is exactly the script’s target. On the CH collar \(q=2\), it becomes
\[
(-4,2,2),
\]
the correct \(W^+\)-spectrum for the negatively oriented Kähler–Einstein metric with \(s_g=-24\).

Since \(W^+\) as an endomorphism scales by \(1/6\), while \(dV\) scales by \(36\),
\[
\int_{\bar g}|W^+_{\bar g}-A_{\psi,1/2}|^2dV_{\bar g}
=
\int_g|W^+_g-6A_{\psi,1/2}|^2dV_g.
\]
Thus the Weyl-model \(L^2\) error is scale invariant. The script uses the endomorphism/Frobenius norm convention consistent with the supplied Step-28 curvature formulas.

### Ricci action

The trace-free Ricci action is scale invariant:
\[
\int|\operatorname{Ric}_{\bar g}^{\circ}|^2dV_{\bar g}
=
\int|\operatorname{Ric}_g^{\circ}|^2dV_g.
\]
The record stores
\[
J=\frac1{8\pi^2}\int|\operatorname{Ric}^{\circ}|^2,
\]
so
\[
\frac1{2\pi^2}\int|\operatorname{Ric}^{\circ}|^2=4J.
\]
The factor \(4\) in the script is a change of reporting units, not a sixfold metric-scaling factor.

---

## 3. The main logical/normalization error: the displayed Ricci term

The note defines its branch numerator using
\[
\int|\operatorname{Ric}_{\bar g}+\bar g|^2dV_{\bar g},
\]
but the script actually inserts
\[
P=\int|\operatorname{Ric}_{\bar g}^{\circ}|^2dV_{\bar g}.
\]
These agree only when \(s_{\bar g}\equiv-4\). Here they do not: the JSON gives original-scale scalar ranges

\[
[-24.4577068,-23.9996840]
\]
for the certified-coefficient profile and
\[
[-24.0267349,-23.9544449]
\]
for the floating profile.

The exact decomposition is
\[
|\operatorname{Ric}_{\bar g}+\bar g|^2
=
|\operatorname{Ric}_{\bar g}^{\circ}|^2+\frac14(s_{\bar g}+4)^2.
\]
Under \(\bar g=6g\),
\[
\int_{\bar g}\frac14(s_{\bar g}+4)^2dV_{\bar g}
=
\int_g\frac14(s_g+24)^2dV_g.
\]
Therefore one must make one of the following corrections:

* If the intended defect uses trace-free Ricci, replace the note’s
  \[
  |\operatorname{Ric}+\bar g|^2
  \]
  by
  \[
  |\operatorname{Ric}^{\circ}|^2.
  \]
  Then the JSON totals are correct.

* If the intended defect really uses \(|\operatorname{Ric}+\bar g|^2\), add
  \[
  \boxed{
  I_s=\frac1{2\pi^2}\int_g\frac14(s_g+24)^2\,dV_g
  }
  \]
  to every quoted branch numerator. In the script’s normalized radial notation,
  ```python
  I_s = integ_dt(W*(scal+24.0)**2/4.0)
  ```
  The two supplied JSONs do not contain \(I_s\), so the corrected numerical total cannot be recovered from them alone.

This is the substantive error in the stated \(4.08167\) “\(|\operatorname{Ric}+g|^2\)” numerator.

---

## 4. Recomputed quantities

All numbers below are actual integrals divided by \(2\pi^2\).

### Certified-coefficient profile, \(x_0=0.03\)

\[
36(0.0021273360285258345)
=0.07658409702693005,
\]
\[
6(0.0754119998065093)
=0.45247199883905576,
\]
\[
E_W=0.022405367744409186,
\]
\[
4J=3.9826806443720573.
\]

Thus
\[
E_W+E_{\rm amp}
=0.09898946477133924,
\]
and the trace-free-Ricci branch sum is
\[
\boxed{
3.9826806443720573+0.09898946477133924
=4.0816701091433965.
}
\]
Including the separately reported derivative energy gives
\[
\boxed{
4.0816701091433965+0.45247199883905576
=4.534142107982452.
}
\]

If the Ricci term is instead \(|\operatorname{Ric}+\bar g|^2\), these become
\[
4.0816701091433965+I_s,\qquad
4.534142107982452+I_s.
\]

### Floating profile, \(x_0=0.038\)

\[
36(0.0030491974221540353)
=0.10977110719754526,
\]
\[
6(0.09818744461847811)
=0.5891246677108687,
\]
\[
E_W=0.03361064226893610,
\qquad
4J=3.9811508676845797.
\]
Hence
\[
E_W+E_{\rm amp}=0.14338174946648136,
\]
\[
\boxed{
3.9811508676845797+0.14338174946648136
=4.124532617151061,
}
\]
and with derivative energy,
\[
\boxed{
4.124532617151061+0.5891246677108687
=4.71365728486193.
}
\]

Again, \(I_s\) must be added if the full Einstein residual \(|\operatorname{Ric}+\bar g|^2\) is intended.

Only the Ricci action has the separate rigorous/Arb provenance mentioned in the note. The amplitude, derivative, Weyl-model, and hatted quantities are floating numerical quadratures.

### Pinning

The ODE implies
\[
(\phi^2)'=4Wu^4,
\]
so
\[
\int Wu^4dt=\frac{\phi(X)^2-\phi(0)^2}{4}=\frac{X^2}{4}.
\]
At \(X=128\), the exact target is \(4096\). The reported values
\[
4096.000000007811,\qquad 4095.999999998188
\]
agree to relative errors about \(1.9\times10^{-12}\) and \(4.4\times10^{-13}\). Likewise,
\[
\int q\,dV_g=2\int u^4dV_g=\frac{X^2}{2}=8192.
\]

---

## 5. Cohomological normalization and \(\eta\)

The statement \(\eta=1\) is correct, but the note conflates the original \(\Omega\) with the sixfold-rescaled form \(\psi=6\Omega\).

Write classes in \(2\pi\)-integral normalization. On the original \(\operatorname{Ric}=-6g\) host,
\[
\rho=-6\Omega,\qquad [\rho]/2\pi=-K_X,
\]
so, up to the fixed orientation sign irrelevant to absolute pairings,
\[
[\Omega]/2\pi=\frac16K_X.
\]
Zero exceptional periods imply no \(E_i\)-components. Therefore
\[
\left([\Omega]/2\pi\right)^2=\frac A{36},
\qquad
\left|K_X\cdot[\Omega]/2\pi\right|=\frac A6.
\]
For \(\psi=6\Omega\),
\[
[\psi]/2\pi=K_X,\qquad
([\psi]/2\pi)^2=A,\qquad
|K_X\cdot[\psi]/2\pi|=A.
\]

Thus the note’s
\[
[\Omega]^2=A,\qquad |K_X\cdot[\Omega]|=A
\]
is correct only if its symbol \(\Omega\) denotes the rescaled/integrally normalized \(\psi\)-class. For the script’s original \(\Omega\), the corrected values are \(A/36\) and \(A/6\).

The period angle is homogeneous of degree zero:
\[
\eta
=\frac{|K_X\cdot[\Omega]|}{\sqrt{A[\Omega]^2}}
=1,
\]
and likewise \(\eta(\psi)=1\). This is justified because the class is the fixed pullback Kähler class. It is not valid for an arbitrary harmonic self-dual direction when \(b^+>1\): positive-square directions can acquire components orthogonal to \(K_X\), so no general reverse Cauchy–Schwarz estimate forces \(\eta\ge1\).

---

## 6. The singular hatted almost-Kähler calculation

Away from the bolt,
\[
\widehat g=u^2g,\qquad |\Omega|_{\widehat g}^2=2,
\]
so \((\widehat g,\Omega)\) is almost-Kähler there. The script uses
\[
s^*=\widehat s+4\nu^2,
\]
the usual star scalar, whereas Step 28’s Chern/Hermitian scalar is
\[
s^\nabla=\widehat s+2\nu^2.
\]
The distinction is handled consistently in the script.

The sampled maxima are
\[
\max s^*=-23.5046830041,\qquad -23.4268853048
\]
in the original \(\operatorname{Ric}=-6g\) units. Thus the quadrature detects no \(s^*>0\) pocket in either tested profile. This is strong numerical evidence because the margin from zero is large, but it is not an interval-arithmetic proof over the entire radial continuum.

The Chern–Stokes consistency check is
\[
\int s^\nabla dV_{\widehat g}=-6X^2=-98304.
\]
Since \(s^*=s^\nabla+2\nu^2\) and
\[
N=\int4\nu^2dV_{\widehat g},
\]
one obtains
\[
\int s^*dV_{\widehat g}=-98304+\frac N2.
\]
For the two JSONs this predicts
\[
-98303.97557057,\qquad -98303.96744784,
\]
matching the reported values to the numerical quadrature accuracy.

### Why closed AKΓ cannot be applied

Near the bolt,
\[
u^2\sim ct,\qquad
\nu\sim t^{-3/2},\qquad
\widehat s\sim t^{-3},\qquad
dV_{\widehat g}\sim t^3dt.
\]
Hence
\[
\int \nu^2dV_{\widehat g}<\infty,
\]
but
\[
\boxed{
\int \widehat s^{\,2}dV_{\widehat g}
\sim\int t^{-3}dt=+\infty.
}
\]
Thus \(\widehat g\) is not merely a nonsmooth endpoint to which the closed AKΓ theorem has not yet been extended: its quadratic scalar-curvature functional diverges. Applying closed smooth AKΓ directly to \((\widehat g,\Omega)\) is therefore not meaningful as an estimate for the original smooth metric’s finite defect.

A valid punctured-cell identity must retain the zero-set/interface terms. In the supplied diagonal theory this role is played by the Step-28 finite replacement
\[
12H_s+6G+\frac32Q_\delta+\frac12Q_A-\frac32N
\]
together with the Step-29 boundary conversion \(B\). One must not silently discard that interface contribution.

### Torsion-scale labeling

The JSON values
\[
N=0.0488588655,\qquad 0.0651043119
\]
are in the original \(\operatorname{Ric}=-6g\) scale. Under \(\bar{\widehat g}=6\widehat g\), this one-derivative energy scales by six:
\[
N_{\operatorname{Ric}=-1}
=
0.2931531929,\qquad 0.3906258716.
\]
The sign of \(s^*\) is unchanged, while its point values divide by six. The note should label the quoted torsion numbers explicitly rather than placing them alongside \(\operatorname{Ric}=-g\) quantities without conversion.

---

## 7. What the evidence establishes about localized \(O(k)\) cost

For this fixed replicated construction, all defects vanish on the untouched host:
\[
q=2,\qquad \nabla\psi=0,\qquad
W^+=A_{\psi,1/2},\qquad
\operatorname{Ric}^{\circ}=0.
\]
Disjoint cells therefore contribute additively. The certified-profile per-cell quantities are

\[
E_{\rm amp}=0.07658410,\qquad
E_W=0.02240537,\qquad
E_{\nabla\psi}=0.45247200,
\]
\[
P/(2\pi^2)=3.98268064.
\]
Consequently this explicit harmonic-zero object realizes a finite localized numerator proportional to \(k\):
\[
4.08167011\,k
\]
for the trace-free-Ricci plus Weyl plus amplitude definition, or
\[
(4.08167011+I_s)k
\]
for the full \(|\operatorname{Ric}+\bar g|^2\) definition. Including the separately tracked derivative energy gives \(4.53414211k\), again plus \(I_s k\) if applicable.

Dividing by the reference host volume \(2\pi^2A\) gives the stated first-order scale
\[
4.08167011\,\frac{k}{A}.
\]
If normalization uses the actual final glued volume, the exact denominator must include the total cell volume correction; thus \(4.08167\,k/A\) is a reference-volume or sparse-density expression, not automatically the exact normalized quotient at finite density.

This establishes only an explicit localized **upper benchmark**:

* the actual closed metric/harmonic-form pair has nonzero finite cost per cell;
* its cost is additive and hence \(O(k)\);
* its form has zero exceptional periods and bolt zeros;
* its hatted profile exhibits no positive-\(s^*\) aligned pocket;
* its period angle remains \(\eta=1\) because the class is fixed.

It does **not** establish:

* an \(O(k)\) lower bound over all metrics or all harmonic directions;
* impossibility of an \(o(k)\) diffuse construction in the pure-blow-up regime;
* existence of any diffuse construction;
* control of a Seiberg–Witten monopole direction, since the tested \(\Omega\) is a harmonic representative, not a solved monopole bilinear;
* that separately reducing amplitude or Weyl error lowers the dominant per-cell cost—the trace-free Ricci term is about \(3.98\) of the \(4.08\) total.

The correct conclusion is therefore: the tested object lies on the localized linear scale and supplies a concrete benchmark against which a diffuse coupled metric/form construction must be compared. It gives no evidence that diffusion achieves sublinear cost, and no theorem excluding it.
# TTCS Independent Branch Record

```json
{
  "step_id": 45,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step45_lemmaM_and_weyl_departure.md",
    "Sessions/S1003A02/workspace/scripts/step45_resolvent_and_weyl_departure.py",
    "Sessions/S1003A02/workspace/data/step45_resolvent_and_weyl_departure.json",
    "Sessions/S1003A02/workspace/notes/step44_perturbative_ke_coercivity_and_pocket_price.md",
    "Sessions/S1003A02/workspace/notes/step40_nijenhuis_form_and_pointwise_exhaustion.md",
    "Knowledge/objects/papers/PDF-The-Meromorphic-continuation-of-the-resolvent-of-the--65f06f69884f--4497d74c3b78/object.md",
    "Knowledge/objects/papers/On-the-differential-form-spectrum-of-hyperbolic-manifolds--fcf89fd9f78a--65f0a8c7d896/object.md",
    "Knowledge/objects/papers/Spectral-density-for-the-Schrödinger-operator-with-magnetic-field-in-th--9e50435ffdf2--09f40f160194/object.md"
  ]
}
```

## Task

Verify the two main Step-45 mathematical advances in `workspace/notes/step45_lemmaM_and_weyl_departure.md`, using the exact script/data and the primary sources supplied. First, check Lemma M: identify K^{-1} on CH^2 with Will's homogeneous line-bundle character |l|=3; verify the calibration H_{K^{-1}}(nu)=13-nu^2 from the Landau bottom 12 at the lowest discrete-series parameter nu_d=1; verify that zero energy means nu=sqrt(13), that Will's Green kernel decays e^{-(2+sqrt13)r}, and that this is L1 against e^{4r} volume. Check possible normalization/sign/pole mistakes. Then verify the one-form inverse B_1^{-1}=2(Delta_1+12)^{-1}-d(Delta_0+6)^{-1}(Delta_0+12)^{-1}d*, the CH^2 exact/coexact Hodge thresholds alpha_0=4 and alpha_1=1, derivative/local-singularity control, and whether these facts genuinely give a quotient-independent L-infinity inverse by periodization. Judge whether this closes the uniformly local canonical-branch form A_C of Step-44 Theorem A, stating any remaining nonlinear slice issue precisely. Second, verify Theorem K: the exact factorization f(W_*,r,n)=-(2-r)^2(r+1)-r^2(1-q), expansion off the Kähler orbit, and the asserted sharp constant C_K=4sqrt6/3 in f<=C_K|E|. Check the passage to the integrated sign-family inequality and the certified-cell numerical consequence. Be exact about what is proved and do not infer a blow-up tariff.

## Output

# Scientific verification memo

## 1. Homogeneous Lemma M

### 1.1 Identification of \(K^{-1}\) with Will’s \(|l|=3\) line bundle

For
\[
K=S(U(2)U(1)),\qquad k=\operatorname{diag}(A,y),\qquad \det A\,y=1,
\]
the holomorphic tangent representation at the origin is \(z\mapsto Azy^{-1}\). Hence
\[
\det_{\mathbf C}T^{1,0}= \det(A)y^{-2}=y^{-3}.
\]
The canonical and anticanonical fibers therefore have characters \(y^{3}\) and \(y^{-3}\), respectively. Depending on the associated-bundle convention, \(K^{-1}\cong\Lambda^{0,2}\) corresponds to \(l=-3\) or \(l=3\); all of Will’s spectral and pole formulas depend on \(|l|\), so
\[
|l|=3
\]
is correct.

Will’s radial Jacobian is
\[
\delta(t)=2^{2n-1}(\sinh t)^{2(n-1)}\sinh 2t
       \sim C e^{2nt}.
\]
For \(n=2\), this is \(e^{4t}\), matching the complex-hyperbolic normalization with sectional curvatures in \([-4,-1]\), hence holomorphic sectional curvature \(-4\). There is no hidden factor of two in the distance variable used for the decay calculation.

### 1.2 Calibration of the rough Laplacian

Will’s spherical parameter satisfies
\[
\chi(\nu,l)=\nu^{2}-\rho^{2}+\tau_{-l}(C_{\mathfrak m}),
\qquad \rho=n=2.
\]
The geometric connection Laplacian is \(-C\) plus a bundle-dependent scalar, so its eigenvalue is necessarily
\[
H_{K^{-1}}(\nu)=A-\nu^{2}.
\]
Will’s pole list gives, for \(n=2\) and \(|l|=3\), the sole positive discrete-series parameter
\[
\nu_d=|l|-n=1.
\]

At \(\operatorname{Ric}=-6g\), the Kodaira/Landau identity on
\(\Lambda^{0,2}\cong K^{-1}\) gives
\[
\inf\operatorname{spec}_{L^{2}}(\nabla^{*}\nabla)
   =2|\lambda|=12,\qquad \lambda=-6,
\]
with equality on the lowest discrete-series sector. Therefore
\[
12=H_{K^{-1}}(1)=A-1,
\]
and hence
\[
\boxed{H_{K^{-1}}(\nu)=13-\nu^{2}}.
\]
The coefficient of \(-\nu^{2}\) comes directly from the Casimir formula, so calibration at \(\nu=1\) determines the entire affine relation.

The Askour–Bouaouid–Elhadouni magnetic spectrum is consistent with this Landau picture. Their displayed setup assumes a nonintegral magnetic parameter, however, so Will’s homogeneous-bundle calculation together with the Kodaira identity is the cleaner justification at the integral value \(|l|=3\).

### 1.3 Zero-energy kernel, decay, poles, and \(L^{1}\)

Zero energy means
\[
H_{K^{-1}}(\nu_0)=0,
\qquad
\nu_0=\sqrt{13}.
\]
Will’s \(Q_{\nu,l}\) contains the factors
\[
(2\cosh r)^{-l}(2\cosh r)^{-(\nu+\rho(l))},
\qquad \rho(l)=n-l,
\]
whose total exponent is \(-(\nu+n)r\), independently of the sign of \(l\). Thus
\[
|G_{K^{-1}}(r)|
   \le C e^{-(2+\sqrt{13})r}.
\]
Against shell volume \(e^{4r}\,dr\), the far integral is controlled by
\[
\int^{\infty}e^{-(\sqrt{13}-2)r}\,dr,
\]
and
\[
\sqrt{13}-2=1.605551275\ldots>0.
\]

Will’s Theorem 3.4(c) gives the local behavior \(r^{-2}\) in real dimension four. Since the local volume element is \(r^{3}dr\),
\[
\int_{0}^{1}r^{-2}r^{3}\,dr<\infty.
\]
Thus the full Green kernel is absolutely integrable.

The pole list from Will’s Theorem 4.1 is especially clean here:
\[
\nu=-5-2j,\qquad j\ge0,
\]
together with the positive pole \(\nu=1\). Therefore \(\sqrt{13}\) is not a pole. Moreover \(\sqrt{13}>2=\rho\), so this kernel lies in Will’s original resolvent half-plane; no meromorphic continuation is needed for the zero-energy inverse.

These calculations verify the line-bundle part of Lemma M without a normalization, sign, or pole mismatch.

---

## 2. One-form block

### 2.1 Exact inverse identity

Write
\[
B_1=dd^{*}+\frac12d^{*}d+6.
\]
On exact one-forms,
\[
d^{*}d=0,\qquad dd^{*}=\Delta_1,
\]
so \(B_1=\Delta_1+6\). On coexact one-forms,
\[
dd^{*}=0,\qquad d^{*}d=\Delta_1,
\]
so
\[
B_1=\frac12(\Delta_1+12).
\]

The proposed operator
\[
T=2(\Delta_1+12)^{-1}
-d(\Delta_0+6)^{-1}(\Delta_0+12)^{-1}d^{*}
\]
has multiplier
\[
\frac{2}{x+12}-\frac{x}{(x+6)(x+12)}
=\frac1{x+6}
\]
on the exact sector and multiplier \(2/(x+12)\) on the coexact sector. It also gives \(1/6\) on harmonic one-forms. Hence
\[
\boxed{
B_1^{-1}
=2(\Delta_1+12)^{-1}
-d(\Delta_0+6)^{-1}(\Delta_0+12)^{-1}d^{*}.}
\]
The two exact SymPy residuals in the supplied JSON correctly encode these exact/coexact computations.

### 2.2 Hodge thresholds and decay

Carron–Pedon, Theorem 2.4(2), gives on \(\mathbb{CH}^{2}\)
\[
\alpha_0=(2-0)^2=4,\qquad
\alpha_1=(2-1)^2=1.
\]
The exact one-form spectrum is inherited from scalar functions through \(d\), so its continuous threshold is \(4\). The lower one-form branch beginning at \(1\) is coexact.

For the coexact term,
\[
(\Delta_1+12)^{-1}
=(\Delta_1-\alpha_1+s_c^2)^{-1},
\qquad
s_c^2=1+12=13.
\]
Carron–Pedon’s Green estimate therefore gives
\[
|G_c(r)|\le Ce^{-(2+\sqrt{13})r}.
\]

For the exact correction,
\[
(\Delta_0+6)^{-1}
=(\Delta_0-\alpha_0+s_e^2)^{-1},
\qquad
s_e^2=4+6=10.
\]
The other scalar factor has parameter
\[
s^2=4+12=16.
\]
Consequently the slow scalar exponent is
\[
e^{-(2+\sqrt{10})r}.
\]
Differentiation does not change the exponential rate, so the exact part has \(L^{1}\) margin
\[
\sqrt{10}-2=1.162277660\ldots>0.
\]

### 2.3 Local singularities

A shifted second-order Green kernel in four dimensions behaves as \(r^{-2}\). For the correction term one may use
\[
(\Delta_0+6)^{-1}(\Delta_0+12)^{-1}
=\frac16\bigl((\Delta_0+6)^{-1}-(\Delta_0+12)^{-1}\bigr).
\]
Before applying \(d\) and \(d^{*}\), this is an operator of order \(-4\), with logarithmic local behavior. Two derivatives restore an order-\(-2\) kernel, hence again an \(r^{-2}\) singularity. It is locally integrable in dimension four. This also confirms that no unexamined derivative singularity is hidden in the formula.

### 2.4 Periodization and the uniform \(L^\infty\) inverse

Let \(K\) denote either homogeneous Green kernel and let \(F_{\Gamma'}\) be a fundamental domain for any finite-index lattice subgroup \(\Gamma'\). Unitary bundle transport preserves the fiber norm, and unfolding gives
\[
\begin{aligned}
\sup_x\int_{X_{\Gamma'}}|K_{\Gamma'}(x,y)|\,dy
&\le
\sup_x\sum_{\gamma\in\Gamma'}
 \int_{F_{\Gamma'}}|K(\tilde x,\gamma\tilde y)|\,dy\\
&=
\sup_x\int_{\mathbb{CH}^{2}}|K(\tilde x,z)|\,dz.
\end{aligned}
\]
The right side is finite and does not depend on \(\Gamma'\). Therefore
\[
\|K_{\Gamma'}f\|_{\infty}
\le \|K\|_{L^{1}(\mathbb{CH}^{2})}\|f\|_{\infty}.
\]
The local singularity is integrable, while the far series converges because each decay exponent exceeds the orbit-growth exponent \(4\). Thus periodization genuinely supplies a finite-cover-independent \(L^\infty\) inverse.

Local Schauder estimates on lifted model balls then yield
\[
\|u\|_{C_b^{2,\alpha}}
\le C\bigl(\|Nu\|_{C_b^{0,\alpha}}+\|u\|_\infty\bigr)
\le C'\|Nu\|_{C_b^{0,\alpha}},
\]
with model constants. Rescaling from scalar curvature \(-24\) to scalar curvature \(-4\) multiplies the operators and distances by fixed factors; integrability and the finite-cover uniformity are unchanged.

### 2.5 Relation to the extensive canonical branch

The homogeneous spectral part of Lemma M is complete and removes the missing model inverse from Step 44. The supplied note, however, does not itself write the full bounded-Hölder nonlinear slice argument needed for \(A_C\). The precise additional analytic statement is:

1. The closeness hypothesis must use one global diffeomorphism and one global scale,
   \[
   \|\phi^{*}g-cg_\Gamma\|_{C_b^{2,\alpha}}<\varepsilon,
   \]
   rather than unrelated identifications on separate model balls.

2. The Diff\(\ltimes\)Conf slice must satisfy finite-cover-independent estimates in \(C_b^{k,\alpha}\). The gauge and conformal operators from Step 44 have pointwise-positive zeroth-order parts, so the needed model inverses are available; the nonlinear slice map still has to be estimated in these norms.

3. For the first-order SW operator, the normal inverse gives
   \[
   \mathcal L^{-1}
   =(\mathcal L^{*}\mathcal L)^{-1}\mathcal L^{*}
   \]
   once surjectivity is included. The real index is
   \[
   \frac{c_1(K^{-1})^2-(2\chi+3\tau)}4=0,
   \]
   while the normal operator has zero kernel, so surjectivity follows on each compact quotient. The differentiated normal Green kernel behaves as \(r^{-3}\), still locally \(L^{1}\) in four dimensions, and retains the same far exponential. This provides the first-order \(L^\infty\) right inverse required by the SW implicit-function argument.

4. For a perturbed metric one needs the uniform estimate
   \[
   \|(N_g-N_0)u\|_{C_b^{0,\alpha}}
   \le C\varepsilon\|u\|_{C_b^{2,\alpha}},
   \]
   followed by a Neumann-series inverse, together with the local quadratic estimate
   \[
   \|Q(u)-Q(v)\|_{C_b^{0,\alpha}}
   \le C(\|u\|_{C_b^{1,\alpha}}+\|v\|_{C_b^{1,\alpha}})
         \|u-v\|_{C_b^{1,\alpha}}.
   \]

With this global slice lemma, the nearby canonical branch and its finite-cover-independent estimates follow in the usual way. Without writing that lemma, Step 45 proves the missing homogeneous resolvent statement but leaves the nonlinear globalization implicit. In all cases, uniqueness concerns only the small canonical-branch neighborhood, not every monopole on a blow-up.

---

## 3. Theorem K

### 3.1 Exact factorization at the Kähler orbit

Write
\[
W_*=\frac13I-\hat\omega\otimes\hat\omega,\qquad
q=\langle n,\hat\omega\rangle^2,
\]
and
\[
M_*=W_*-\frac{r^2}{4}\left(\frac I3-n\otimes n\right).
\]
Directly,
\[
M_*(n,n)=\frac13-q+\frac{r^2}{6},
\]
and
\[
|M_*|^2
=\frac23+\frac{r^4}{24}
-\frac{r^2}{2}\left(q-\frac13\right).
\]
Therefore
\[
r^2M_*(n,n)-4|M_*|^2
=r^2\left(q-\frac13\right)-\frac83.
\]
Adding
\[
p(r)=\frac{(2-r)(r-1)(3r+2)}3
\]
and factoring gives
\[
\boxed{
f(W_*,r,n)
=-(2-r)^2(r+1)-r^2(1-q).}
\]
This agrees with the exact zero residual in the script. Equality requires
\[
r=2,\qquad q=1.
\]

### 3.2 Expansion away from the orbit

For \(W^+=W_*+E\), with \(E\in S^2_0(\Lambda^+)\),
\[
f(W_*+E,r,n)
=f(W_*,r,n)+\langle G_{r,n},E\rangle-4|E|^2,
\]
where
\[
G_{r,n}=r^2(nn)_0-8M_*.
\]
Using \(|(nn)_0|^2=2/3\), \(|W_*|^2=2/3\), and
\[
\langle (nn)_0,W_*\rangle=\frac13-q,
\]
one obtains
\[
\boxed{
|G_{r,n}|^2
=\frac23r^4+\frac{128}{3}
-16r^2\left(q-\frac13\right).}
\]
At \(r=2,q=1\),
\[
|G|^2=\frac{32}{3},
\qquad
|G|=\frac{4\sqrt6}{3}.
\]

### 3.3 Exact proof of the sharp coefficient

Set
\[
a=(2-r)^2(r+1)+r^2(1-q)=-f(W_*,r,n).
\]
For fixed \(r,q\), optimizing over the length and direction of \(E\) gives
\[
\sup_{E\ne0}\frac{f(W_*+E,r,n)}{|E|}
=
\max\{0,\ |G_{r,n}|-4\sqrt a\}.
\]
Thus the numerical optimizer in the script is supported by an exact reduction.

Put \(u=1-q\). Then
\[
a=A+r^2u,\qquad A=(2-r)^2(r+1),
\]
and
\[
|G|^2=B+16r^2u,\qquad
B=\frac23(8-r^2)^2.
\]
For
\[
F(u)=\sqrt{B+16r^2u}-4\sqrt{A+r^2u},
\]
one has, whenever \(A+r^2u>0\),
\[
F'(u)
=-\frac{2r^2}{\sqrt{B+16r^2u}\sqrt{A+r^2u}}\,F(u).
\]
Hence every positive value of \(F\) decreases as \(u\) increases, so the positive maximum occurs at \(u=0\), namely \(q=1\).

At \(q=1\),
\[
F(0)=\sqrt{\frac23}(8-r^2)-4(2-r)\sqrt{r+1}.
\]
Since
\[
\begin{aligned}
F(0)-4\sqrt{\frac23}
&=(2-r)\left[
\sqrt{\frac23}(r+2)-4\sqrt{r+1}
\right]\\
&\le0,\qquad 0\le r\le2,
\end{aligned}
\]
the exact uniform coefficient is
\[
\boxed{C_{\mathcal K}=\frac{4\sqrt6}{3}}.
\]
Equality is approached only at \(r=2,q=1\) with \(E\to0\) in the \(G\)-direction. That direction is normal to the \(SO(3)\)-orbit, so the same coefficient is sharp when \(|E|\) is the actual distance to \(\mathcal K\).

### 3.4 Integrated sign-family inequality

Theorem W gives
\[
8\pi^2k-P(\hat g)
=\mathbb E_\epsilon\int f(W^+_{\hat g},r_\epsilon,n_\epsilon)
-4\mathbb E_\epsilon\|\zeta_\epsilon\|^2-\mathcal W.
\]
The last two terms are \(\le0\). Since the pointwise estimate holds for every \(W_*\in\mathcal K\),
\[
f(W^+,r,n)
\le \frac{4\sqrt6}{3}\inf_{W_*\in\mathcal K}|W^+-W_*|.
\]
No measurable choice of nearest orbit element is needed. Together with
\(P(g)\ge P(\hat g)\), this yields
\[
\boxed{
8\pi^2k-P(g)
\le8\pi^2k-P(\hat g)
\le\frac{4\sqrt6}{3}
 \int_M\operatorname{dist}(W^+_{\hat g},\mathcal K)\,d\mu_{\hat g}.}
\]

If \(P(g)\le8\pi^2ck\), then
\[
\boxed{
\int_M\operatorname{dist}(W^+_{\hat g},\mathcal K)\,d\mu_{\hat g}
\ge \sqrt6\,\pi^2(1-c)k.}
\]

For \(c=0.995662732762\),
\[
\sqrt6\,\pi^2(1-c)=0.1048556\ldots.
\]
Thus \(0.10486\) is the value rounded to the nearest \(10^{-5}\); a decimal guaranteed by truncation is \(0.10485\). The same conclusion follows from the certified interval recorded in Step 40.

This is a total \(L^1\) Weyl-orbit departure on the smooth closed scalar-\(-4\) representative. It does not distribute that departure among individual exceptional cores, control gluing interfaces, or produce a blow-up tariff.
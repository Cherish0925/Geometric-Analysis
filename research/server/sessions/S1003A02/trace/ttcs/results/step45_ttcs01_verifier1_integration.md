# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 45,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step45_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step45_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the two main Step-45 mathematical advances in `workspace/notes/step45_lemmaM_and_weyl_departure.md`, using the exact script/data and the primary sources supplied. First, check Lemma M: identify K^{-1} on CH^2 with Will's homogeneous line-bundle character |l|=3; verify the calibration H_{K^{-1}}(nu)=13-nu^2 from the Landau bottom 12 at the lowest discrete-series parameter nu_d=1; verify that zero energy means nu=sqrt(13), that Will's Green kernel decays e^{-(2+sqrt13)r}, and that this is L1 against e^{4r} volume. Check possible normalization/sign/pole mistakes. Then verify the one-form inverse B_1^{-1}=2(Delta_1+12)^{-1}-d(Delta_0+6)^{-1}(Delta_0+12)^{-1}d*, the CH^2 exact/coexact Hodge thresholds alpha_0=4 and alpha_1=1, derivative/local-singularity control, and whether these facts genuinely give a quotient-independent L-infinity inverse by periodization. Judge whether this closes the uniformly local canonical-branch form A_C of Step-44 Theorem A, stating any remaining nonlinear slice issue precisely. Second, verify Theorem K: the exact factorization f(W_*,r,n)=-(2-r)^2(r+1)-r^2(1-q), expansion off the Kähler orbit, and the asserted sharp constant C_K=4sqrt6/3 in f<=C_K|E|. Check the passage to the integrated sign-family inequality and the certified-cell numerical consequence. Be exact about what is proved and do not infer a blow-up tariff.

## Integrated Scientific Memo

# Step-45 verification memo

## Verdict

- **Lemma M, homogeneous kernels:** verified. In the holomorphic-sectional-curvature \(-4\) normalization, \(K^{-1}\) has Will character \(|l|=3\), its Bochner eigenvalue is \(13-\nu^2\), and the zero-energy kernel has parameter \(\nu=\sqrt{13}\), decay \(e^{-(2+\sqrt{13})r}\), and is \(L^1\). No distance normalization, sign, or pole error was found.
- **One-form block:** the inverse formula, exact/coexact thresholds, decay rates, and local singularity estimates are correct. Periodization yields a finite-cover-independent \(L^\infty\) inverse.
- **Scope of \(A_C\):** Step 45 supplies the missing homogeneous resolvent input, but the note overstates completion unless the uniformly local nonlinear slice/IFT argument is written down. The remaining issue is analytic globalization of the nearby branch, not another spectral calculation.
- **Theorem K:** the factorization, off-orbit expansion, and sharp constant
  \[
  C_{\mathcal K}=\frac{4\sqrt6}{3}
  \]
  are correct. The script’s numerical optimization can be replaced by an exact proof.
- **Integrated consequence:** (K3)–(K4) are valid under the stated all-metric sign-family hypotheses. The certified coefficient gives \(0.1048556\ldots\,k\), so “at least \(0.10486\ldots\)” is slightly too strong if interpreted as a lower bound.
- None of these results implies a blow-up tariff.

---

## 1. Lemma M: \(K^{-1}\) line sector

### 1.1 Homogeneous character and normalization

For
\[
K=S(U(2)U(1)),\qquad k=\operatorname{diag}(A,y),\qquad \det(A)y=1,
\]
the isotropy action on \(T^{1,0}_0\mathbb{CH}^2\) is \(z\mapsto Azy^{-1}\). Thus
\[
\det_{\mathbb C}T^{1,0}= \det(A)y^{-2}=y^{-3}.
\]
According to the associated-bundle convention, \(K^{-1}\) is represented by \(l=3\) or \(l=-3\); Will’s relevant spectral and pole formulas use \(|l|\), hence
\[
\boxed{|l|=3}.
\]

Will’s radial density is
\[
\delta(r)=2^{2n-1}(\sinh r)^{2(n-1)}\sinh 2r\sim Ce^{2nr}.
\]
For \(n=2\), shell volume grows as \(e^{4r}\). This is exactly the metric with sectional curvatures in \([-4,-1]\), hence holomorphic sectional curvature \(-4\). There is no factor-of-two error in the radial distance.

### 1.2 Calibration \(H_{K^{-1}}(\nu)=13-\nu^2\)

Will gives the spherical Casimir eigenvalue
\[
\chi(\nu,l)=\nu^2-\rho^2+\tau_{-l}(C_{\mathfrak m}),\qquad \rho=n=2.
\]
Since the geometric connection Laplacian differs from \(-C\) by a fixed bundle scalar,
\[
H_{K^{-1}}(\nu)=A-\nu^2.
\]

For \(|l|=3,n=2\), Will’s positive discrete parameter is
\[
\nu_d=|l|-n=1.
\]
The Kodaira/Landau identity at \(\operatorname{Ric}=-6g\) gives
\[
\inf\operatorname{spec}_{L^2}(\nabla^*\nabla)=2|\lambda|=12,
\qquad \lambda=-6,
\]
and equality occurs on the lowest holomorphic/antiholomorphic discrete-series sector. Consequently
\[
12=H_{K^{-1}}(1)=A-1,
\]
so
\[
\boxed{H_{K^{-1}}(\nu)=13-\nu^2}.
\]

This is also consistent with the middle-degree Hodge calculation. On the \(\Lambda^{2,0}\) or conjugate line,
\[
\nabla^*\nabla=\Delta_2+12,
\]
while Carron–Pedon give the continuous middle-degree Hodge threshold \(\alpha_2=1\); hence the corresponding rough-Laplacian continuous threshold is \(13\), above the discrete Landau state \(12\).

The supplied script does **not independently verify** this calibration: it inserts \(12+\nu_d^2=13\). The calibration is nevertheless justified by the source formulas and Kodaira identity above.

### 1.3 Zero energy, decay, poles, and integrability

Zero energy satisfies
\[
13-\nu^2=0,
\qquad
\boxed{\nu_0=\sqrt{13}}.
\]
Will’s formula has
\[
Q_{\nu,l}(r)\sim e^{-(\nu+\rho)r},
\]
because the \(l\)-dependent factors cancel in the total exponent. Thus
\[
\boxed{|G_{K^{-1}}(r)|\le Ce^{-(2+\sqrt{13})r}}.
\]
Against shell volume \(e^{4r}\,dr\),
\[
|G|\,d\mathrm{vol}
=O\!\left(e^{-(\sqrt{13}-2)r}\right)dr,
\]
and
\[
\sqrt{13}-2=1.605551275\ldots>0.
\]
The kernel is therefore integrable at infinity.

Near the diagonal, Will’s Theorem 3.4(c) gives the four-dimensional Green singularity \(r^{-2}\). Since
\[
r^{-2}r^3\,dr=r\,dr,
\]
it is locally \(L^1\).

For \((n,|l|)=(2,3)\), Will’s poles are
\[
\nu=-5-2j,\qquad j\ge0,
\]
and the sole positive pole \(\nu=1\). Hence \(\sqrt{13}\) is not a pole. More strongly,
\[
\sqrt{13}>\rho=2,
\]
so the zero-energy kernel lies in Will’s original resolvent half-plane, without requiring meromorphic continuation. Its normalization \(2\nu c(\nu,l)\) is nonzero there.

Thus the line-bundle portion of Lemma M is verified.

---

## 2. One-form block

### 2.1 Exact inverse

The operator is
\[
B_1=dd^*+\frac12d^*d+6.
\]
On exact one-forms,
\[
B_1=\Delta_1+6,
\]
and on coexact one-forms,
\[
B_1=\frac12(\Delta_1+12).
\]
Therefore
\[
\boxed{
B_1^{-1}
=2(\Delta_1+12)^{-1}
-d(\Delta_0+6)^{-1}(\Delta_0+12)^{-1}d^*.}
\]

Indeed, on an exact eigenmode with \(\Delta_1\)-eigenvalue \(x\), the proposed multiplier is
\[
\frac{2}{x+12}-\frac{x}{(x+6)(x+12)}
=\frac1{x+6},
\]
while on a coexact mode it is \(2/(x+12)\). The script’s exact and coexact residuals equal zero and correctly check this algebra.

### 2.2 Thresholds and decay

Carron–Pedon, Theorem 2.4, gives for \(\mathbb{CH}^2\)
\[
\boxed{\alpha_0=4,\qquad \alpha_1=1}.
\]
Here the exact one-form branch inherits the scalar threshold \(4\), whereas the lower one-form branch beginning at \(1\) is coexact.

For the exact inverse \((\Delta_1+6)^{-1}\),
\[
s_e^2=\alpha_0+6=10,
\]
so its slow decay is
\[
e^{-(2+\sqrt{10})r},
\qquad
\sqrt{10}-2=1.162277660\ldots>0.
\]

For the coexact inverse \(2(\Delta_1+12)^{-1}\),
\[
s_c^2=\alpha_1+12=13,
\]
so its decay is
\[
e^{-(2+\sqrt{13})r}.
\]

A cleaner treatment of the correction term is
\[
(\Delta_0+6)^{-1}(\Delta_0+12)^{-1}
=\frac16\left[(\Delta_0+6)^{-1}-(\Delta_0+12)^{-1}\right].
\]
The two scalar parameters are \(\sqrt{10}\) and \(4\); hence the slow rate is again \(e^{-(2+\sqrt{10})r}\). Differentiating the homogeneous Fuchsian expansion does not alter the exponential exponent.

### 2.3 Local singularity after differentiation

Each scalar resolvent separately has an \(r^{-2}\) singularity in dimension four. Their difference above cancels that leading term, leaving logarithmic behavior for the order-\(-4\) product. Applying \(d_xd_y\) yields \(O(r^{-2})\). Therefore the full one-form kernel is locally \(L^1\); no principal-value interpretation is needed.

Thus the one-form Green kernel is \(L^1\), with binding far-field margin
\[
\boxed{\sqrt{10}-2}.
\]

---

## 3. Periodization and quotient-independent inverses

Let \(K(x,y)\) be one of the homogeneous kernels and \(F_\Gamma\) a fundamental domain. Fiber transport is unitary, and absolute convergence gives
\[
\begin{aligned}
\sup_x\int_{X_\Gamma}|K_\Gamma(x,y)|\,dy
&\le
\sup_{\tilde x}\sum_{\gamma\in\Gamma}
\int_{F_\Gamma}|K(\tilde x,\gamma\tilde y)|\,dy\\
&=
\sup_{\tilde x}\int_{\mathbb{CH}^2}|K(\tilde x,z)|\,dz.
\end{aligned}
\]
Hence
\[
\boxed{
\|K_\Gamma f\|_\infty
\le \|K\|_{L^1(\mathbb{CH}^2)}\|f\|_\infty,}
\]
with a constant independent of the finite cover.

To identify the periodized operator with the inverse, one uses cutoff approximation for bounded periodic data, local elliptic regularity, and uniqueness. Uniqueness is uniform because
\[
B_1\ge6,\qquad \nabla^*\nabla_{K^{-1}}\ge12.
\]
The same argument is unaffected by harmonic one-forms on compact quotients: \(B_1\) acts by \(6\) on them.

Interior Schauder estimates applied to lifted periodic solutions then give model-uniform estimates such as
\[
\|u\|_{C_b^{2,\alpha}}
\le C\bigl(\|Nu\|_{C_b^{0,\alpha}}+\|u\|_\infty\bigr)
\le C'\|Nu\|_{C_b^{0,\alpha}}.
\]
No injectivity-radius constant is needed when these estimates are run on fixed universal-cover balls.

Therefore the **linear content of Lemma M is proved**, and it genuinely yields finite-cover-independent \(L^\infty\) and uniformly local Hölder inverses.

---

## 4. Does this close the uniformly local canonical branch \(A_C\)?

It closes the previously missing homogeneous spectral input, but the Step-45 note does not itself supply a complete nonlinear proof. A rigorous \(A_C\) statement still requires the following uniformly local slice/IFT package.

1. **Global notion of closeness.** The hypothesis must be formulated using one global diffeomorphism and one global scale,
   \[
   \|\phi^*g-cg_\Gamma\|_{C_b^{2,\alpha}}<\varepsilon,
   \]
   not unrelated identifications on individual balls.

2. **Metric slice.** The Diff\(\ltimes\)Conf slice must be constructed with finite-cover-independent \(C_b^{k,\alpha}\) bounds. The scalar conformal operator and Bianchi gauge operators have positive mass and are controlled by Kato domination. If a full York/conformal-Killing inverse is used, its exact/coexact splitting must also be included; it has the same favorable resolvent structure.

3. **First-order SW inverse.** The implicit-function theorem uses \(\mathcal L^{-1}\), not only \((\mathcal L^*\mathcal L)^{-1}\). One needs
   \[
   \mathcal L^{-1}=(\mathcal L^*\mathcal L)^{-1}\mathcal L^*
   \]
   after establishing surjectivity. Differentiating the normal Green kernel gives a local \(r^{-3}\) singularity, still \(L^1\) in four dimensions, with unchanged far exponent. On each compact quotient the normal kernel is zero; together with the index-zero canonical linearization this gives surjectivity.

4. **Perturbed-operator and nonlinear estimates.**
   \[
   \|(N_g-N_0)u\|_{C_b^{0,\alpha}}
   \le C\varepsilon\|u\|_{C_b^{2,\alpha}}
   \]
   must be combined with a Neumann series, and the SW nonlinearity must satisfy a cover-independent local estimate such as
   \[
   \|Q(u)-Q(v)\|_{C_b^{0,\alpha}}
   \le C(\|u\|_{C_b^{1,\alpha}}+\|v\|_{C_b^{1,\alpha}})
      \|u-v\|_{C_b^{1,\alpha}}.
   \]

With these standard but presently unwritten steps, the extensive theorem holds for the **nearby canonical branch**, with uniqueness only among solutions uniformly close to the canonical monopole. It does not select arbitrary global monopoles on a blow-up and does not by itself give a localized bulk theorem.

Accordingly, the Step-45 sentence “this proves \(A_C\)” should be weakened to: **Lemma M proves the missing cover-uniform model inverses; \(A_C\) follows once the above uniformly local slice and nonlinear perturbation lemma is supplied.**

---

## 5. Theorem K: exact pointwise algebra

Let
\[
W_*=\frac13I-\hat\omega\otimes\hat\omega,
\qquad
q=\langle n,\hat\omega\rangle^2,
\]
and
\[
M_*=W_*-\frac{r^2}{4}\left(\frac I3-n\otimes n\right).
\]
Then
\[
M_*(n,n)=\frac13-q+\frac{r^2}{6},
\]
and
\[
|M_*|^2
=\frac23+\frac{r^4}{24}
-\frac{r^2}{2}\left(q-\frac13\right).
\]
Substituting into
\[
f=r^2M(n,n)-4|M|^2+
\frac{(2-r)(r-1)(3r+2)}3
\]
gives
\[
\boxed{
f(W_*,r,n)=-(2-r)^2(r+1)-r^2(1-q).}
\]
Thus \(f\le0\), with equality exactly at
\[
r=2,\qquad q=1.
\]

For \(W^+=W_*+E\),
\[
\boxed{
f(W_*+E,r,n)
=f(W_*,r,n)+\langle G_{r,n},E\rangle-4|E|^2,}
\]
where
\[
G_{r,n}=r^2(nn)_0-8M_*.
\]
Using
\[
|(nn)_0|^2=\frac23,\qquad |W_*|^2=\frac23,\qquad
\langle(nn)_0,W_*\rangle=\frac13-q,
\]
one obtains
\[
\boxed{
|G_{r,n}|^2
=\frac23r^4+\frac{128}{3}
-16r^2\left(q-\frac13\right).}
\]
These formulas match the script’s symbolic residuals.

At \(r=2,q=1\),
\[
|G|^2=\frac{32}{3},
\qquad
|G|=\frac{4\sqrt6}{3}.
\]

---

## 6. Exact proof of the sharp constant

Define
\[
a=(2-r)^2(r+1)+r^2(1-q)=-f(W_*,r,n).
\]
For fixed \(r,q\), optimization over \(E=tG/|G|\) gives
\[
\sup_{E\ne0}\frac{f(W_*+E,r,n)}{|E|}
=\max\{0,\ |G|-4\sqrt a\}.
\]

Put \(u=1-q\),
\[
A=(2-r)^2(r+1),\qquad
B=\frac23(8-r^2)^2.
\]
Then
\[
a=A+r^2u,\qquad |G|^2=B+16r^2u.
\]
For
\[
F(u)=\sqrt{B+16r^2u}-4\sqrt{A+r^2u},
\]
direct differentiation shows
\[
F'(u)
=-\frac{2r^2F(u)}
{\sqrt{B+16r^2u}\sqrt{A+r^2u}}.
\]
Consequently every positive value decreases with \(u\); the positive maximum occurs at \(u=0\), i.e. \(q=1\).

At \(q=1\),
\[
F(0)=\sqrt{\frac23}(8-r^2)-4(2-r)\sqrt{r+1}.
\]
Moreover,
\[
F(0)-4\sqrt{\frac23}
=(2-r)\left[
\sqrt{\frac23}(r+2)-4\sqrt{r+1}
\right]\le0
\]
for \(0\le r\le2\). Hence
\[
\boxed{
f(W_*+E,r,n)\le\frac{4\sqrt6}{3}|E|,}
\]
and
\[
\boxed{C_{\mathcal K}=\frac{4\sqrt6}{3}}
\]
is the exact sharp constant.

Sharpness is compatible with choosing \(W_*\) as a closest point of the orbit. At \(r=2,n=\hat\omega\),
\[
M_*=0,\qquad G=-4W_*.
\]
The radial direction \(W_*\) is normal to the fixed-norm \(SO(3)\)-orbit, so small \(E\) proportional to \(-W_*\) is an admissible normal departure and realizes the first-order constant.

At the equality state,
\[
f=4E(\hat\omega,\hat\omega)-4|E|^2,
\]
so no uniform pointwise quadratic estimate in \(|E|\) can replace the linear estimate.

---

## 7. Sign-family integration

Theorem W gives
\[
8\pi^2k-P(\hat g)
=
\mathbb E_\epsilon\int f(W^+_{\hat g},r_\epsilon,n_\epsilon)
-4\mathbb E_\epsilon\|\zeta_\epsilon\|^2-\mathcal W.
\]
Dropping the two nonpositive terms and taking the infimum over \(W_*\in\mathcal K\) pointwise gives
\[
8\pi^2k-P(\hat g)
\le
\frac{4\sqrt6}{3}
\int_M\operatorname{dist}(W^+_{\hat g},\mathcal K)\,d\mu_{\hat g}.
\]
Since Yamabe normalization satisfies \(P(g)\ge P(\hat g)\),
\[
\boxed{
8\pi^2k-P(g)
\le8\pi^2k-P(\hat g)
\le\frac{4\sqrt6}{3}
\int_M\operatorname{dist}(W^+_{\hat g},\mathcal K)\,d\mu_{\hat g}.}
\]
No measurable nearest-point selection is needed: the pointwise estimate holds for every \(W_*\in\mathcal K\), so one can directly take the infimum.

If
\[
P(g)\le8\pi^2ck,
\]
then
\[
\boxed{
\int_M\operatorname{dist}(W^+_{\hat g},\mathcal K)\,d\mu_{\hat g}
\ge \sqrt6\,\pi^2(1-c)k.}
\]

For
\[
c=0.995662732762,
\]
the coefficient is
\[
\sqrt6\,\pi^2(1-c)=0.1048556\ldots.
\]
Thus a certified downward rounding is \(0.10485\,k\); \(0.10486\,k\) is ordinary nearest rounding, not a rigorously valid lower truncation.

This quantity is a necessary total \(L^1\) Weyl-orbit departure on the smooth scalar-\(-4\) Yamabe representative. It is not a measurement on an isolated cell and does not allocate cost to exceptional cores or collars.

---

## 8. Corrections to the note

1. The central formulas in §3 contain corrupted `\frac`/`\tfrac` control characters and should be repaired.
2. The Weyl-departure integral in §4 must be evaluated for the scalar-\(-4\) Yamabe representative \(\hat g\), unless the original smooth metric \(g\) already has scalar curvature \(-4\).
3. The script verifies the algebra after entering the Landau bottom and discrete parameter; it does not independently derive the calibration \(13\).
4. The phrase “derivatives remain locally integrable after convolution” is correct but unnecessarily opaque; the scalar partial-fraction identity gives the local cancellation directly.
5. The result should not be presented as a blow-up tariff. To obtain one would still require bulk monopole selection, collar/interface control, and an integrated mechanism converting the linear Weyl departure into a coercive core cost.